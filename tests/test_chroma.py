import json
import unittest
from pathlib import Path

from pycapcut import ScriptFile, TrackType, VideoSegment, trange_seconds


VIDEO = Path(__file__).resolve().parents[1] / "readme_assets" / "tutorial" / "video.mp4"


class ChromaTest(unittest.TestCase):
    def test_default_values_and_single_foreground_reference(self):
        script = ScriptFile(640, 360)
        script.add_track(TrackType.video, "background", relative_index=0)
        script.add_track(TrackType.video, "foreground", relative_index=2)
        script.add_segment(VideoSegment(str(VIDEO), trange_seconds(0, duration=4)), "background")

        foreground = VideoSegment(str(VIDEO), trange_seconds(1, duration=2))
        self.assertIs(foreground.add_chroma("#00FE00FF"), foreground)
        script.add_segment(foreground, "foreground")

        content = json.loads(script.dumps())
        self.assertEqual(len(content["materials"]["chromas"]), 1)
        chroma = content["materials"]["chromas"][0]
        self.assertEqual(chroma, {
            "color": "#00fe00ff",
            "edge_smooth_value": 0.0,
            "id": chroma["id"],
            "intensity_value": 0.2,
            "shadow_value": 0.0,
            "should_transfer_color": True,
            "spill_value": 0.0,
            "type": "chroma",
            "version": "v2",
        })

        tracks = {track["name"]: track for track in content["tracks"]}
        self.assertNotIn(chroma["id"], tracks["background"]["segments"][0]["extra_material_refs"])
        self.assertEqual(tracks["foreground"]["segments"][0]["extra_material_refs"].count(chroma["id"]), 1)

    def test_native_reference_parameters(self):
        segment = VideoSegment(str(VIDEO), trange_seconds(0, duration=2))
        segment.add_chroma("#00FE00FF", 36, 10, 3, 26)

        script = ScriptFile(640, 360)
        script.add_track(TrackType.video)
        script.add_segment(segment)
        chroma = json.loads(script.dumps())["materials"]["chromas"][0]
        self.assertEqual(
            (chroma["intensity_value"], chroma["shadow_value"],
             chroma["edge_smooth_value"], chroma["spill_value"]),
            (0.36, 0.1, 0.03, 0.26),
        )
        self.assertNotIn("path", chroma)
        self.assertNotIn("resource_id", chroma)

    def test_invalid_input_and_duplicate_rejected_without_partial_reference(self):
        segment = VideoSegment(str(VIDEO), trange_seconds(0, duration=2))
        original_refs = list(segment.extra_material_refs)
        for color, kwargs in [
            ("#00FE00", {}),
            ("#00FG00FF", {}),
            ("#00FE00FF", {"intensity": float("nan")}),
            ("#00FE00FF", {"shadow": -1}),
            ("#00FE00FF", {"edge_smooth": 101}),
            ("#00FE00FF", {"spill": float("inf")}),
        ]:
            with self.subTest(color=color, kwargs=kwargs):
                with self.assertRaises(ValueError):
                    segment.add_chroma(color, **kwargs)
                self.assertIsNone(segment.chroma)
                self.assertEqual(segment.extra_material_refs, original_refs)

        segment.add_chroma("#00FE00FF")
        with self.assertRaises(ValueError):
            segment.add_chroma("#00FE00FF")
        self.assertEqual(segment.extra_material_refs.count(segment.chroma.global_id), 1)


if __name__ == "__main__":
    unittest.main()
