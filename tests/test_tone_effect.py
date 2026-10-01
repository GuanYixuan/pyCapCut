import json
import unittest
from pathlib import Path

from pycapcut import (AudioSceneEffectType, AudioSegment, ScriptFile, ToneEffectType,
                      TrackType, trange_seconds)
from pycapcut.metadata import ToneEffectType as MetadataToneEffectType


AUDIO = Path(__file__).resolve().parents[1] / "readme_assets" / "tutorial" / "audio.mp3"


class ToneEffectTest(unittest.TestCase):
    def test_public_api_exports_capcut_five_field_tone(self):
        self.assertIs(ToneEffectType, MetadataToneEffectType)
        self.assertEqual(len(ToneEffectType), 11)
        self.assertNotIn("7376171800184492561", {item.value.resource_id for item in ToneEffectType})

        script = ScriptFile(640, 360)
        script.add_track(TrackType.audio, "voice")
        segment = AudioSegment(str(AUDIO), trange_seconds(0, duration=2))
        self.assertIs(segment.add_effect(ToneEffectType.花栗鼠, [50, 42]), segment)
        script.add_segment(segment, "voice")

        content = json.loads(script.dumps())
        effect, = content["materials"]["audio_effects"]
        self.assertEqual(set(effect), {"audio_adjust_params", "id", "name", "resource_id", "type"})
        self.assertEqual(effect["name"], "花栗鼠")
        self.assertEqual(effect["resource_id"], "7021052742021943810")
        self.assertEqual(effect["type"], "audio_effect")
        self.assertEqual(
            [(p["name"], p["value"], p["default_value"]) for p in effect["audio_adjust_params"]],
            [("change_voice_param_pitch", 0.5, 0.5),
             ("change_voice_param_timbre", 0.42, 0.5)],
        )
        self.assertEqual(content["tracks"][0]["segments"][0]["extra_material_refs"].count(effect["id"]), 1)

    def test_other_parameter_tone_exports_same_shape(self):
        script = ScriptFile(640, 360)
        script.add_track(TrackType.audio)
        segment = AudioSegment(str(AUDIO), trange_seconds(0, duration=2))
        segment.add_effect(ToneEffectType.机器人, [35])
        script.add_segment(segment)

        effect, = json.loads(script.dumps())["materials"]["audio_effects"]
        self.assertEqual(set(effect), {"audio_adjust_params", "id", "name", "resource_id", "type"})
        self.assertEqual(effect["resource_id"], "7021052669863137794")
        self.assertEqual(
            [(p["name"], p["value"]) for p in effect["audio_adjust_params"]],
            [("change_voice_param_strength", 0.35)],
        )

    def test_tone_defaults_duplicate_rule_and_scene_effect_shape(self):
        segment = AudioSegment(str(AUDIO), trange_seconds(0, duration=2))
        segment.add_effect(ToneEffectType.花栗鼠)
        refs = list(segment.extra_material_refs)
        with self.assertRaises(ValueError):
            segment.add_effect(ToneEffectType.花栗鼠, [50, 42])
        with self.assertRaises(ValueError):
            segment.add_effect(ToneEffectType.花栗鼠, [50, 42, 30])
        self.assertEqual(segment.extra_material_refs, refs)

        segment.add_effect(next(iter(AudioSceneEffectType)))
        script = ScriptFile(640, 360)
        script.add_track(TrackType.audio)
        script.add_segment(segment)
        effects = json.loads(script.dumps())["materials"]["audio_effects"]
        tone = next(effect for effect in effects if effect["name"] == "花栗鼠")
        scene = next(effect for effect in effects if effect["name"] != "花栗鼠")
        self.assertEqual([p["value"] for p in tone["audio_adjust_params"]], [0.5, 0.5])
        self.assertEqual(scene["category_id"], "sound_effect")
        self.assertEqual(scene["category_name"], "场景音")
        self.assertEqual(scene["sub_type"], 1)
        self.assertEqual(scene["time_range"], {"duration": 0, "start": 0})


if __name__ == "__main__":
    unittest.main()
