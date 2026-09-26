import json
import unittest
from pathlib import Path

from pycapcut import MixModeType, ScriptFile, TrackType, VideoSegment, trange_seconds


VIDEO = Path(__file__).resolve().parents[1] / "readme_assets" / "tutorial" / "video.mp4"


class MixModeTest(unittest.TestCase):
    def test_verified_modes_have_unique_resource_and_effect_ids(self):
        modes = list(MixModeType)
        self.assertEqual(len(modes), 10)
        self.assertEqual(len({mode.value.resource_id for mode in modes}), 10)
        self.assertEqual(len({mode.value.effect_id for mode in modes}), 10)
        self.assertTrue(all(not mode.value.is_vip for mode in modes))

    def test_only_foreground_segment_references_mix_mode(self):
        script = ScriptFile(640, 360)
        script.add_track(TrackType.video, "background", relative_index=0)
        script.add_track(TrackType.video, "foreground", relative_index=2)
        script.add_segment(VideoSegment(str(VIDEO), trange_seconds(0, duration=4)), "background")
        foreground = VideoSegment(str(VIDEO), trange_seconds(1, duration=2))
        foreground.set_mix_mode(MixModeType.正片叠底)
        script.add_segment(foreground, "foreground")

        content = json.loads(script.dumps())
        effects = [effect for effect in content["materials"]["effects"] if effect["type"] == "mix_mode"]
        self.assertEqual(len(effects), 1)
        effect = effects[0]
        self.assertEqual(effect["effect_id"], "871333")
        self.assertEqual(effect["resource_id"], "6758325895519277582")
        self.assertNotIn("path", effect)
        tracks = {track["name"]: track for track in content["tracks"]}
        self.assertNotIn(effect["id"], tracks["background"]["segments"][0]["extra_material_refs"])
        self.assertIn(effect["id"], tracks["foreground"]["segments"][0]["extra_material_refs"])

    def test_repeated_set_keeps_one_material_and_reference(self):
        segment = VideoSegment(str(VIDEO), trange_seconds(0, duration=2))
        segment.set_mix_mode(MixModeType.正片叠底)
        first_id = segment.mix_mode.global_id
        script = ScriptFile(640, 360)
        script.add_track(TrackType.video)
        script.add_segment(segment)
        segment.set_mix_mode(MixModeType.滤色)

        content = json.loads(script.dumps())
        effects = [effect for effect in content["materials"]["effects"] if effect["type"] == "mix_mode"]
        self.assertEqual([effect["id"] for effect in effects], [first_id])
        self.assertEqual(effects[0]["effect_id"], MixModeType.滤色.value.effect_id)
        self.assertEqual(content["tracks"][0]["segments"][0]["extra_material_refs"].count(first_id), 1)


if __name__ == "__main__":
    unittest.main()
