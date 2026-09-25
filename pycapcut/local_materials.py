import os
import uuid
import pymediainfo

from typing import Optional, Literal
from typing import Dict, Any


def _coerce_numeric(value: object, *, field_name: str) -> float:
    """将 MediaInfo 返回的数值字段统一转换为浮点数。"""
    if value is None:
        raise ValueError(f"媒体字段 '{field_name}' 为空")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            raise ValueError(f"媒体字段 '{field_name}' 为空字符串")
        return float(stripped)
    raise TypeError(f"媒体字段 '{field_name}' 的类型不受支持: {type(value)}")


def _coerce_int(value: object, *, field_name: str) -> int:
    """读取 MediaInfo 的整数尺寸字段。"""
    return int(round(_coerce_numeric(value, field_name=field_name)))


def _pick_first_numeric(*candidates: object, field_name: str) -> float:
    """选择媒体轨道或容器中第一个可用的数值。"""
    last_error: Optional[Exception] = None
    for candidate in candidates:
        if candidate is None:
            continue
        try:
            return _coerce_numeric(candidate, field_name=field_name)
        except (TypeError, ValueError) as exc:
            last_error = exc
    if last_error is not None:
        raise last_error
    raise ValueError(f"媒体字段 '{field_name}' 不存在")


class CropSettings:
    """素材的裁剪设置, 各属性均在0-1之间, 注意素材的坐标原点在左上角"""

    upper_left_x: float
    upper_left_y: float
    upper_right_x: float
    upper_right_y: float
    lower_left_x: float
    lower_left_y: float
    lower_right_x: float
    lower_right_y: float

    def __init__(self, *, upper_left_x: float = 0.0, upper_left_y: float = 0.0,
                 upper_right_x: float = 1.0, upper_right_y: float = 0.0,
                 lower_left_x: float = 0.0, lower_left_y: float = 1.0,
                 lower_right_x: float = 1.0, lower_right_y: float = 1.0):
        """初始化裁剪设置, 默认参数表示不裁剪"""
        self.upper_left_x = upper_left_x
        self.upper_left_y = upper_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.lower_right_x = lower_right_x
        self.lower_right_y = lower_right_y

    def export_json(self) -> Dict[str, Any]:
        return {
            "upper_left_x": self.upper_left_x,
            "upper_left_y": self.upper_left_y,
            "upper_right_x": self.upper_right_x,
            "upper_right_y": self.upper_right_y,
            "lower_left_x": self.lower_left_x,
            "lower_left_y": self.lower_left_y,
            "lower_right_x": self.lower_right_x,
            "lower_right_y": self.lower_right_y
        }

class VideoMaterial:
    """本地视频素材（视频或图片）, 一份素材可以在多个片段中使用"""

    material_id: str
    """素材全局id, 自动生成"""
    local_material_id: str
    """素材本地id, 意义暂不明确"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""
    duration: int
    """素材时长, 单位为微秒"""
    height: int
    """素材高度"""
    width: int
    """素材宽度"""
    crop_settings: CropSettings
    """素材裁剪设置"""
    material_type: Literal["video", "photo"]
    """素材类型: 视频或图片"""

    def __init__(self, path: str, material_name: Optional[str] = None, crop_settings: CropSettings = CropSettings()):
        """从指定位置加载视频（或图片）素材

        Args:
            path (`str`): 素材文件路径, 支持mp4, mov, avi等常见视频文件及jpg, jpeg, png等图片文件.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用文件名作为素材名称.
            crop_settings (`CropSettings`, optional): 素材裁剪设置, 默认不裁剪.

        Raises:
            `FileNotFoundError`: 素材文件不存在.
            `ValueError`: 不支持的素材文件类型.
        """
        path = os.path.abspath(path)
        postfix = os.path.splitext(path)[1]
        if not os.path.exists(path):
            raise FileNotFoundError(f"找不到 {path}")

        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid4().hex
        self.path = path
        self.crop_settings = crop_settings
        self.local_material_id = ""

        if not pymediainfo.MediaInfo.can_parse():
            raise ValueError(f"不支持的视频素材类型 '{postfix}'")

        info: pymediainfo.MediaInfo = \
            pymediainfo.MediaInfo.parse(path, mediainfo_options={"File_TestContinuousFileNames": "0"})  # type: ignore
        # 有视频轨道的视为视频素材
        if len(info.video_tracks):
            video_track = info.video_tracks[0]
            general_track = info.general_tracks[0] if len(info.general_tracks) else None
            self.material_type = "video"
            self.duration = int(round(_pick_first_numeric(
                getattr(video_track, "duration", None),
                getattr(general_track, "duration", None) if general_track is not None else None,
                field_name="video duration"
            ) * 1e3))
            self.width = _coerce_int(getattr(video_track, "width", None), field_name="video width")
            self.height = _coerce_int(getattr(video_track, "height", None), field_name="video height")
        # gif文件使用imageio库获取长度
        elif postfix.lower() == ".gif":
            import imageio
            gif = imageio.get_reader(path)

            self.material_type = "video"
            self.duration = int(round(gif.get_meta_data()['duration'] * gif.get_length() * 1e3))
            self.width = _coerce_int(getattr(info.image_tracks[0], "width", None), field_name="gif width")
            self.height = _coerce_int(getattr(info.image_tracks[0], "height", None), field_name="gif height")
            gif.close()
        elif len(info.image_tracks):
            self.material_type = "photo"
            self.duration = 10800000000  # 相当于3h
            self.width = _coerce_int(getattr(info.image_tracks[0], "width", None), field_name="image width")
            self.height = _coerce_int(getattr(info.image_tracks[0], "height", None), field_name="image height")
        else:
            raise ValueError(f"输入的素材文件 {path} 没有视频轨道或图片轨道")

    def export_json(self) -> Dict[str, Any]:
        video_material_json = {
            "audio_fade": None,
            "category_id": "",
            "category_name": "local",
            "check_flag": 63487,
            "crop": self.crop_settings.export_json(),
            "crop_ratio": "free",
            "crop_scale": 1.0,
            "duration": self.duration,
            "height": self.height,
            "id": self.material_id,
            "local_material_id": self.local_material_id,
            "material_id": self.material_id,
            "material_name": self.material_name,
            "media_path": "",
            "path": self.path,
            "type": self.material_type,
            "width": self.width
        }
        return video_material_json

class AudioMaterial:
    """本地音频素材"""

    material_id: str
    """素材全局id, 自动生成"""
    material_name: str
    """素材名称"""
    path: str
    """素材文件路径"""

    duration: int
    """素材时长, 单位为微秒"""

    def __init__(self, path: str, material_name: Optional[str] = None):
        """从指定位置加载音频素材, 注意视频文件不应该作为音频素材使用

        Args:
            path (`str`): 素材文件路径, 支持mp3, wav等常见音频文件.
            material_name (`str`, optional): 素材名称, 如果不指定, 默认使用文件名作为素材名称.

        Raises:
            `FileNotFoundError`: 素材文件不存在.
            `ValueError`: 不支持的素材文件类型.
        """
        path = os.path.abspath(path)
        if not os.path.exists(path):
            raise FileNotFoundError(f"找不到 {path}")

        self.material_name = material_name if material_name else os.path.basename(path)
        self.material_id = uuid.uuid4().hex
        self.path = path

        if not pymediainfo.MediaInfo.can_parse():
            raise ValueError("不支持的音频素材类型 %s" % os.path.splitext(path)[1])
        info: pymediainfo.MediaInfo = pymediainfo.MediaInfo.parse(path)  # type: ignore
        if len(info.video_tracks):
            raise ValueError("音频素材不应包含视频轨道")
        if not len(info.audio_tracks):
            raise ValueError(f"给定的素材文件 {path} 没有音频轨道")
        audio_track = info.audio_tracks[0]
        general_track = info.general_tracks[0] if len(info.general_tracks) else None
        self.duration = int(round(_pick_first_numeric(
            getattr(audio_track, "duration", None),
            getattr(general_track, "duration", None) if general_track is not None else None,
            field_name="audio duration"
        ) * 1e3))

    def export_json(self) -> Dict[str, Any]:
        return {
            "app_id": 0,
            "category_id": "",
            "category_name": "local",
            "check_flag": 3,
            "copyright_limit_type": "none",
            "duration": self.duration,
            "effect_id": "",
            "formula_id": "",
            "id": self.material_id,
            "local_material_id": self.material_id,
            "music_id": self.material_id,
            "name": self.material_name,
            "path": self.path,
            "source_platform": 0,
            "type": "extract_music",
            "wave_points": []
        }
