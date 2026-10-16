# 文档与发布工具

`tools/` 中的正式维护工具随仓库管理；本机实验、缓存、日志和生成结果放在 `ignored/`，不在这里混放。维护工具不随库的安装包发布。

`english_readme.md` 是英文完整文档，`pypi_readme.md` 是从其中 `PYPI:BEGIN` / `PYPI:END` 区间生成的发布简介。生成文件随源码发布，不手工编辑。

更新英文文档后运行：

```bash
python tools/generate_pypi_readme.py
python tools/generate_pypi_readme.py --check
```

脚本将相对图片链接转换为本仓库的图片地址，将章节链接转换为英文完整文档中的对应章节。`--check` 只检查，缺失或过期时返回非零退出码。

构建发布包需要当前 Python 环境安装 `build`、`setuptools` 和 `wheel`，它们属于维护工具依赖。运行：

```bash
python tools/build_dist.py
```

该入口先更新简介，再使用当前环境构建 sdist，并从 sdist 构建 wheel；核对模板 JSON、包介绍，以及是否意外收录测试或本机文件，通过后将产物保存到 `dist/`。同名版本产物会被替换，其他已有文件保留。该命令不会上传到 PyPI。

这些脚本可从其他工作目录用绝对路径调用。源码检出及源码包均包含生成后的 `pypi_readme.md`，普通安装无需运行文档生成工具。
