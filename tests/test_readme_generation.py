import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReadmeGenerationTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "tools").mkdir()
        self.script = self.root / "tools" / "generate_pypi_readme.py"
        shutil.copyfile(ROOT / "tools" / self.script.name, self.script)
        self.source = self.root / "english_readme.md"
        self.target = self.root / "pypi_readme.md"

    def run_generator(self, *args):
        # 从 tools/ 调用，确保路径解析与调用者的工作目录无关。
        return subprocess.run([sys.executable, str(self.script), *args], cwd=self.script.parent,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def write_source(self, body):
        self.source.write_text("Outside\n<!-- PYPI:BEGIN -->\n" + body +
                               "\n<!-- PYPI:END -->\nOutside too\n", encoding="utf-8")

    def test_generation_extracts_section_and_preserves_navigation(self):
        self.write_source("# Intro\n![Workflow](readme_assets/使用思路.jpg)\n"
                          "[Details](#add-text) [Demo](demo.py) [中文](README.md#安装)\n"
                          "[External](https://example.com/page#part)")
        result = self.run_generator()
        self.assertEqual(result.returncode, 0, result.stderr)
        generated = self.target.read_text(encoding="utf-8")
        self.assertNotIn("Outside", generated)
        self.assertNotIn("PYPI:BEGIN", generated)
        self.assertIn("Generated from english_readme.md", generated)
        self.assertIn("https://github.com/GuanYixuan/pyCapCut/raw/main/readme_assets/%E4%BD%BF%E7%94%A8%E6%80%9D%E8%B7%AF.jpg", generated)
        self.assertIn("[Details](https://github.com/GuanYixuan/pyCapCut/blob/main/english_readme.md#add-text)", generated)
        self.assertIn("[Demo](https://github.com/GuanYixuan/pyCapCut/blob/main/demo.py)", generated)
        self.assertIn("README.md#%E5%AE%89%E8%A3%85", generated)
        self.assertIn("[External](https://example.com/page#part)", generated)
        previous = self.target.read_bytes()
        self.assertEqual(self.run_generator().returncode, 0)
        self.assertEqual(self.target.read_bytes(), previous)

    def test_check_detects_missing_or_stale_output_without_writing(self):
        self.write_source("Current")
        self.assertNotEqual(self.run_generator("--check").returncode, 0)
        self.assertFalse(self.target.exists())
        self.assertEqual(self.run_generator().returncode, 0)
        self.assertEqual(self.run_generator("--check").returncode, 0)
        old = self.target.read_bytes()
        self.write_source("Changed")
        self.assertNotEqual(self.run_generator("--check").returncode, 0)
        self.assertEqual(self.target.read_bytes(), old)

    def test_invalid_markers_do_not_replace_existing_output(self):
        for source in ("No markers", "<!-- PYPI:END --><!-- PYPI:BEGIN -->",
                       "<!-- PYPI:BEGIN --><!-- PYPI:END -->",
                       "<!-- PYPI:BEGIN -->A<!-- PYPI:BEGIN --><!-- PYPI:END -->"):
            with self.subTest(source=source):
                self.source.write_text(source, encoding="utf-8")
                self.target.write_bytes(b"Keep previous output")
                self.assertNotEqual(self.run_generator().returncode, 0)
                self.assertEqual(self.target.read_bytes(), b"Keep previous output")


if __name__ == "__main__":
    unittest.main()
