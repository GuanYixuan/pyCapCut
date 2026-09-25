import unittest
from types import SimpleNamespace

from pycapcut import AudioSegment, StickerSegment, TextSegment, Timerange, VideoSegment


class ChangePitchTest(unittest.TestCase):
    def test_audio_and_video_segments_export_pitch_option(self):
        cases = (
            (AudioSegment, SimpleNamespace(material_id="audio", duration=8_000_000)),
            (VideoSegment, SimpleNamespace(material_id="video", duration=8_000_000, width=640, height=360)),
        )
        for segment_type, material in cases:
            for kwargs, expected in (({}, False), ({"change_pitch": False}, False), ({"change_pitch": True}, True)):
                with self.subTest(segment=segment_type.__name__, options=kwargs):
                    segment = segment_type(material, Timerange(0, 3_000_000), speed=2.0, **kwargs)
                    exported = segment.export_json()
                    self.assertIs(exported["is_tone_modify"], expected)
                    self.assertEqual(exported["source_timerange"]["duration"], 6_000_000)
                    self.assertEqual(exported["target_timerange"]["duration"], 3_000_000)

    def test_non_media_visual_segments_keep_existing_shape(self):
        segments = (
            StickerSegment("sticker-id", Timerange(0, 3_000_000)),
            TextSegment("label", Timerange(0, 3_000_000)),
        )
        for segment in segments:
            with self.subTest(segment=type(segment).__name__):
                self.assertNotIn("is_tone_modify", segment.export_json())


if __name__ == "__main__":
    unittest.main()
