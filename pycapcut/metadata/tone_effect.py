"""CapCut 传统参数类音色元数据。"""

from .effect_meta import EffectEnum, EffectMeta, EffectParam


class ToneEffectType(EffectEnum):
    """音频片段的参数类音色"""

    # 当前缓存中 11 项均未标记 is_voice_conversion，且均有 1～2 个滑块参数。
    # effect_id 不参与五字段草稿结构；缓存的 common_attr.effect_id 等于资源 ID，
    # 并非独立取证得到的草稿 effect_id，因此这里保持为空。

    # 免费
    Squirrel = EffectMeta("Squirrel", False, "7338257533796094466", "", "b2b3f551b703c87e8e057ad8f92fafbb", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    怪物 = EffectMeta("怪物", False, "7021052602091573761", "", "ce0bc10d76e22a718094c152f7beae25", [
        EffectParam("change_voice_param_pitch", 0.65, 0.0, 1.0),
        EffectParam("change_voice_param_timbre", 0.78, 0.0, 1.0),
    ])
    机器人 = EffectMeta("机器人", False, "7021052669863137794", "", "123114835bda73b8de4aa106ccde0bb2", [
        EffectParam("change_voice_param_strength", 1.0, 0.0, 1.0),
    ])
    花栗鼠 = EffectMeta(
        "花栗鼠", False, "7021052742021943810", "", "4ff3edc0229bfac112c1caefe75e7039", [
            EffectParam("change_voice_param_pitch", 0.5, 0.0, 1.0),
            EffectParam("change_voice_param_timbre", 0.5, 0.0, 1.0),
        ],
    )
    """参数依次为音调与音色，默认均为 50，范围 0～100。"""
    萝莉 = EffectMeta("萝莉", False, "7021052754512581122", "", "bbf0f0d1532a249e9a1f7f3444e1e437", [
        EffectParam("change_voice_param_pitch", 0.75, 0.0, 1.0),
        EffectParam("change_voice_param_timbre", 0.6, 0.0, 1.0),
    ])

    # 订阅
    E_T = EffectMeta("E·T", True, "7338256913865380354", "", "c80c8c31d933b15e93299648e773de3d", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    Giant = EffectMeta("Giant", True, "7338257108795658753", "", "20702d7511d03d006a718ece130ffa92", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    Mermaid = EffectMeta("Mermaid", True, "7350562007357067778", "", "795f4215cf7ed6851808ccd5a606f7a1", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    Radio_Announer = EffectMeta("Radio Announer", True, "7418494159553565185", "", "6c17b5822b5ea7ec690810233873a390", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    Space_Robot = EffectMeta("Space Robot", True, "7338257399356068354", "", "751b0cf3f501a9f1ad4c025a28cb0f27", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
    拳击播报员 = EffectMeta("拳击播报员", True, "7418494022110417409", "", "f8e846c82d49d5c7dc72283026d94194", [
        EffectParam("strength", 1.0, 0.0, 1.0),
    ])
