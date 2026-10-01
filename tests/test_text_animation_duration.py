import json
import unittest

from pycapcut import ScriptFile, TextIntro, TextOutro, TextSegment, TrackType, trange_seconds


class TextAnimationDurationTest(unittest.TestCase):
    def test_default_intro_and_outro_use_effect_durations(self):
        script = ScriptFile(640, 360)
        script.add_track(TrackType.text)
        segment = TextSegment("标题", trange_seconds(0, duration=4))
        segment.add_animation(TextIntro.复古打字机)
        segment.add_animation(TextOutro.打字机)
        script.add_segment(segment)

        content = json.loads(script.dumps())
        animations, = content["materials"]["material_animations"]
        self.assertEqual(
            [(item["type"], item["start"], item["duration"]) for item in animations["animations"]],
            [("in", 0, 800000), ("out", 2000000, 2000000)],
        )
        self.assertIn(animations["id"], content["tracks"][0]["segments"][0]["extra_material_refs"])

    def test_explicit_duration_and_segment_limit(self):
        segment = TextSegment("短标题", trange_seconds(0, duration=1))
        segment.add_animation(TextIntro.复古打字机, "0.3s")
        segment.add_animation(TextOutro.打字机)
        animations = segment.animations_instance.export_json()["animations"]

        self.assertEqual(
            [(item["type"], item["start"], item["duration"]) for item in animations],
            [("in", 0, 300000), ("out", 0, 1000000)],
        )


if __name__ == "__main__":
    unittest.main()
