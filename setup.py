from setuptools import setup, find_packages

setup(
    name="pycapcut",
    version="0.0.3",
    author="gary318",
    description="A lightweight, flexible, and easy-to-use Python tool for generating and exporting CapCut drafts to build fully automated video editing/remix pipelines!",
    long_description=open("pypi_readme.md", "r", encoding="utf-8").read(),
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
