"""经 CapCut 草稿与导出验证的音色元数据。"""

from .effect_meta import EffectEnum, EffectMeta, EffectParam


class ToneEffectType(EffectEnum):
    """音频片段可用的 CapCut 音色；当前仅验证“花栗鼠”。"""

    # effect_id 与 md5 不参与已验证的五字段草稿结构，暂无 CapCut 原生取证值。
    花栗鼠 = EffectMeta(
        "花栗鼠", False, "7021052742021943810", "", "", [
            EffectParam("change_voice_param_pitch", 0.5, 0.0, 1.0),
            EffectParam("change_voice_param_timbre", 0.5, 0.0, 1.0),
        ],
    )
    """参数依次为音调与音色，默认均为 50，范围 0～100。"""
