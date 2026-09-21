from pathlib import Path

from setuptools import setup, find_packages

_HERE = Path(__file__).parent


def _long_description() -> str:
    """Read the PyPI description.

    ``pypi_readme.md`` is only produced when building a release, so a plain
    git checkout does not have it. Fall back to ``README.md`` so that
    ``pip install .`` and ``pip install git+https://...`` keep working.
    Paths are resolved relative to this file rather than the current working
    directory, which is not guaranteed to be the project root during a build.
    """
    for name in ("pypi_readme.md", "README.md"):
        path = _HERE / name
        if path.is_file():
            return path.read_text(encoding="utf-8")
    return ""


setup(
    name="pycapcut",
    version="0.0.3",
    author="gary318",
    description="A lightweight, flexible, and easy-to-use Python tool for generating and exporting CapCut drafts to build fully automated video editing/remix pipelines!",
    long_description=_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/GuanYixuan/pycapcut",
    packages=find_packages(),
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
