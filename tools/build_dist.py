#!/usr/bin/env python3
"""更新 PyPI 简介，构建并核对 sdist / wheel，保存到 dist/。"""

import json
import shutil
import subprocess
import sys
import tarfile
import tempfile
import textwrap
import zipfile
from email.parser import Parser
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
DIST_DIR = ROOT / "dist"


def verify_contents(files, metadata_name: str) -> None:
    """核对产物的模板资源、简介及不应发布的目录。"""
    for name in files:
        parts = PurePosixPath(name).parts
        if any(part in {"tests", "tools", "ignored", "readme_assets", "__pycache__"} for part in parts):
            raise RuntimeError(f"发布包包含不应发布的文件：{name}")
        if name.endswith((".lnk", ".log", ".pyc")) or PurePosixPath(name).name.startswith("AGENTS"):
            raise RuntimeError(f"发布包包含本机文件或缓存：{name}")
    for asset in (ROOT / "pycapcut" / "assets").glob("*.json"):
        name = "pycapcut/assets/" + asset.name
        if name not in files or files[name] != asset.read_bytes():
            raise RuntimeError(f"发布包中的模板资源缺失或内容不符：{name}")
        json.loads(files[name])
    metadata = Parser().parsestr(files[metadata_name].decode("utf-8"))
    expected = (ROOT / "pypi_readme.md").read_text(encoding="utf-8")
    description = metadata.get_payload()
    if not description:
        # 旧 setuptools 使用带八空格续行的 Description 头；新版写入正文。
        first, _, continuation = metadata.get("Description", "").partition("\n")
        description = first + "\n" + textwrap.dedent(continuation)
    if description.replace("\r\n", "\n").strip() != expected.strip():
        raise RuntimeError(f"{metadata_name} 的 PyPI 简介与生成文件不一致")


def verify_distributions(folder: Path):
    wheels = list(folder.glob("*.whl"))
    tarballs = list(folder.glob("*.tar.gz"))
    if len(wheels) != 1 or len(tarballs) != 1:
        raise RuntimeError("本次构建必须生成一份 wheel 和一份 sdist")
    with zipfile.ZipFile(wheels[0]) as archive:
        files = {name: archive.read(name) for name in archive.namelist() if not name.endswith("/")}
    metadata_name = next(name for name in files if name.endswith(".dist-info/METADATA"))
    verify_contents(files, metadata_name)
    with tarfile.open(tarballs[0], "r:gz") as archive:
        files = {member.name.split("/", 1)[1]: archive.extractfile(member).read()
                 for member in archive.getmembers() if member.isfile()}
    verify_contents(files, "PKG-INFO")
    if files.get("pypi_readme.md", b"").decode("utf-8").replace("\r\n", "\n") != (ROOT / "pypi_readme.md").read_text(encoding="utf-8"):
        raise RuntimeError("sdist 缺少最新的 pypi_readme.md")
    return wheels + tarballs


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_pypi_readme.py")], cwd=ROOT, check=True)
    DIST_DIR.mkdir(exist_ok=True)
    # 使用全新输出目录，仅核对本次产物；不清理已有 dist/ 和 build/。
    with tempfile.TemporaryDirectory(prefix=".build-", dir=str(DIST_DIR)) as staging:
        folder = Path(staging).resolve()
        if folder.parent != DIST_DIR.resolve():
            raise RuntimeError(f"临时构建目录不在 dist/ 内：{folder}")
        # build 默认先生成 sdist，再从 sdist 构建 wheel，以核对源码包完整性。
        # 复用维护者环境中的构建依赖，不联网创建隔离环境。
        subprocess.run([sys.executable, "-m", "build", "--no-isolation", "--outdir", str(folder)],
                       cwd=ROOT, check=True)
        for artifact in verify_distributions(folder):
            target = DIST_DIR / artifact.name
            shutil.copy2(artifact, target)
            print(f"已构建并核对：{target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
