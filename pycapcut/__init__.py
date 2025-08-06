import sys

from .local_materials import CropSettings, VideoMaterial, AudioMaterial
from .keyframe import KeyframeProperty

from .time_util import Timerange
from .audio_segment import AudioSegment
from .video_segment import VideoSegment, StickerSegment, ClipSettings
from .effect_segment import EffectSegment, FilterSegment
from .text_segment import TextSegment, TextStyle, TextBorder, TextBackground

from .metadata import FontType
from .metadata import MaskType
from .metadata import TransitionType, FilterType
from .metadata import IntroType, OutroType, GroupAnimationType
from .metadata import TextIntro, TextOutro, TextLoopAnim
from .metadata import AudioSceneEffectType
from .metadata import VideoSceneEffectType, VideoCharacterEffectType

from .track import TrackType
from .template_mode import ShrinkMode, ExtendMode
from .script_file import ScriptFile
from .draft_folder import DraftFolder

# 仅在Windows系统下导入自动导出功能
ISWIN = (sys.platform == 'win32')
if ISWIN:
    pass

from .time_util import SEC, tim, trange

# 基础__all__列表（所有平台通用）
__all__ = [
    "FontType",
    "MaskType",
    "FilterType",
    "TransitionType",
    "IntroType",
    "OutroType",
    "GroupAnimationType",
    "TextIntro",
    "TextOutro",
    "TextLoopAnim",
    "AudioSceneEffectType",
    "VideoSceneEffectType",
    "VideoCharacterEffectType",
    "CropSettings",
    "VideoMaterial",
    "AudioMaterial",
    "KeyframeProperty",
    "Timerange",
    "AudioSegment",
    "VideoSegment",
    "StickerSegment",
    "ClipSettings",
    "EffectSegment",
    "FilterSegment",
    "TextSegment",
    "TextStyle",
    "TextBorder",
    "TextBackground",
    "TrackType",
    "ShrinkMode",
    "ExtendMode",
    "ScriptFile",
    "DraftFolder",
    "SEC",
    "tim",
    "trange",
]
