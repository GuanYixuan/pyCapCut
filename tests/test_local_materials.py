import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from pycapcut import AudioMaterial, VideoMaterial


class MediaInfoFallbackTest(unittest.TestCase):
    def test_video_uses_container_duration_when_track_duration_is_missing(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "sample.webm"
            path.touch()
            info = SimpleNamespace(
                video_tracks=[SimpleNamespace(duration=None, width="1920", height="1080")],
                general_tracks=[SimpleNamespace(duration="1234.5")],
                image_tracks=[],
            )
            with patch("pycapcut.local_materials.pymediainfo.MediaInfo.can_parse", return_value=True), \
                    patch("pycapcut.local_materials.pymediainfo.MediaInfo.parse", return_value=info):
                material = VideoMaterial(str(path))

            self.assertEqual(material.duration, 1_234_500)
            self.assertEqual((material.width, material.height), (1920, 1080))
            self.assertEqual(material.export_json()["duration"], 1_234_500)

    def test_audio_uses_container_duration_when_track_duration_is_missing(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "sample.webm"
            path.touch()
            info = SimpleNamespace(
                video_tracks=[],
                audio_tracks=[SimpleNamespace(duration=None)],
                general_tracks=[SimpleNamespace(duration="2500")],
            )
            with patch("pycapcut.local_materials.pymediainfo.MediaInfo.can_parse", return_value=True), \
                    patch("pycapcut.local_materials.pymediainfo.MediaInfo.parse", return_value=info):
                material = AudioMaterial(str(path))

            self.assertEqual(material.duration, 2_500_000)
            self.assertEqual(material.export_json()["duration"], 2_500_000)


if __name__ == "__main__":
    unittest.main()
