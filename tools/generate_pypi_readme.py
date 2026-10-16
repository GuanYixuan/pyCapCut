#!/usr/bin/env python3
"""从英文完整文档生成 PyPI 简介，并将相对链接指向本仓库。"""

import argparse
import re
from pathlib import Path
from urllib.parse import quote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "english_readme.md"
PYPI_README_PATH = ROOT / "pypi_readme.md"
REPO_BLOB_BASE = "https://github.com/GuanYixuan/pyCapCut/blob/main/"
REPO_RAW_BASE = "https://github.com/GuanYixuan/pyCapCut/raw/main/"
MARKER_BEGIN = "<!-- PYPI:BEGIN -->"
MARKER_END = "<!-- PYPI:END -->"


def extract_pypi_section(source: str) -> str:
    """提取唯一且顺序正确的 PyPI 区间，配置错误时停止生成。"""
    if source.count(MARKER_BEGIN) != 1 or source.count(MARKER_END) != 1:
        raise ValueError("english_readme.md 必须包含唯一一对 PYPI:BEGIN / PYPI:END 标记")
    start = source.index(MARKER_BEGIN) + len(MARKER_BEGIN)
    end = source.index(MARKER_END)
    if end < start:
        raise ValueError("english_readme.md 的 PYPI:END 必须位于 PYPI:BEGIN 之后")
    section = source[start:end].strip()
    if not section:
        raise ValueError("english_readme.md 的 PyPI 区间不能为空")
    return section + "\n"


def rewrite_links(text: str) -> str:
    """转换当前文档使用的行内链接，章节链接保留为英文全文入口。"""
    def replace(match: re.Match) -> str:
        image, label, target = match.groups()
        parts = urlsplit(target)
        if parts.scheme or parts.netloc:
            return match.group(0)
        path = parts.path or README_PATH.name
        target = (REPO_RAW_BASE if image else REPO_BLOB_BASE) + quote(path, safe="/._-%")
        if parts.query:
            target += "?" + parts.query
        if parts.fragment:
            target += "#" + quote(parts.fragment, safe="-._~%")
        return f"{image}[{label}]({target})"

    return re.sub(r"(!?)\[([^\]]*)\]\(([^)]+)\)", replace, text)


def build_pypi_readme() -> str:
    source = README_PATH.read_text(encoding="utf-8")
    header = "<!-- Generated from english_readme.md by tools/generate_pypi_readme.py. Do not edit directly. -->\n\n"
    return header + rewrite_links(extract_pypi_section(source))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="检查生成文件是否最新，不写入文件")
    args = parser.parse_args()
    generated = build_pypi_readme()
    if args.check:
        if not PYPI_README_PATH.is_file() or PYPI_README_PATH.read_text(encoding="utf-8") != generated:
            print("pypi_readme.md 缺失或已过期，请运行 python tools/generate_pypi_readme.py")
            return 1
        print("pypi_readme.md 已是最新")
    else:
        with PYPI_README_PATH.open("w", encoding="utf-8", newline="\n") as output:
            output.write(generated)
        print("已从 english_readme.md 生成 pypi_readme.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
