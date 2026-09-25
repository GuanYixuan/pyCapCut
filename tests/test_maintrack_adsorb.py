import json
import tempfile
import unittest
from pathlib import Path

from pycapcut import DraftFolder


class MaintrackAdsorbTest(unittest.TestCase):
    def test_draft_creation_and_template_round_trip(self):
        with tempfile.TemporaryDirectory() as root:
            folder = DraftFolder(root)

            for name, option, expected in (
                ("default", {}, True),
                ("off", {"maintrack_adsorb": False}, False),
            ):
                with self.subTest(name=name):
                    draft = folder.create_draft(name, 1920, 1080, **option)
                    draft.save()

                    content_path = Path(root) / name / "draft_content.json"
                    content = json.loads(content_path.read_text(encoding="utf-8"))
                    self.assertIs(content["config"]["maintrack_adsorb"], expected)

                    loaded = folder.load_template(name)
                    self.assertIs(loaded.maintrack_adsorb, expected)
                    self.assertIs(json.loads(loaded.dumps())["config"]["maintrack_adsorb"], expected)


if __name__ == "__main__":
    unittest.main()
