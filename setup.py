from pathlib import Path

from setuptools import setup, find_packages

_HERE = Path(__file__).resolve().parent


setup(
    name="pycapcut",
    version="0.0.3",
    author="gary318",
    description="A lightweight, flexible Python tool for generating and editing CapCut drafts",
    # 生成文件随源码发布，构建前通过 tools/generate_pypi_readme.py 更新。
    long_description=(_HERE / "pypi_readme.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/GuanYixuan/pycapcut",
    packages=find_packages(include=["pycapcut", "pycapcut.*"]),
    package_data={
        'pycapcut.assets': ['*.json']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Video"
    ],
    python_requires='>=3.8',
    install_requires=[
        "pymediainfo",
        "imageio",
        "uiautomation>=2; sys_platform == 'win32'"
    ],
)
