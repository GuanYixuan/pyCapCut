"""视频人物特效元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class VideoCharacterEffectType(EffectEnum):
    """视频人物特效枚举"""

    # 免费特效
    CRASH                = EffectMeta("CRASH!", False, "7399480133914086661", "7399480133914086661", "7bec1a7f596be64787625a9e85f96e81", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    Pop_Out              = EffectMeta("Pop-Out", False, "7399482537774468357", "7399482537774468357", "f36c6922e91c3036495591591aba39d9", [])
    丁达尔效应           = EffectMeta("丁达尔效应", False, "7399483524597746950", "7399483524597746950", "b59ac3e268c20a1a82a9d7d0dabf33ff", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    中轴旋转             = EffectMeta("中轴旋转", False, "7399482402403273990", "7399482402403273990", "16c94e8b38c2d306c11b0d4cfb63dec9", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    九尾狐               = EffectMeta("九尾狐", False, "7399481106514431238", "7399481106514431238", "12afdb69b18ec5127874f04d6f3fdefd", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    人影爆闪             = EffectMeta("人影爆闪", False, "7399481114311642373", "7399481114311642373", "f307677e792d2970045b653267fca93b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    健美写真             = EffectMeta("健美写真", False, "7311300825593187590", "7311300825593187590", "711e4a0e5e0993d04ad67500f011d655", [])
    光环_I               = EffectMeta("光环 I", False, "7399482680515071238", "7399482680515071238", "ce2098aa7d557cfc63d896fc63ec2846", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    光环_II              = EffectMeta("光环 II", False, "7399482793962573061", "7399482793962573061", "adb70b2ea060371bb7d91ec43c031989", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    分身                 = EffectMeta("分身", False, "7399481765036952837", "7399481765036952837", "dca7518f6eb90654d1c2473406db2890", [
                              EffectParam("effects_adjust_distortion", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    分身_II              = EffectMeta("分身 II", False, "7399483154140073222", "7399483154140073222", "a42da906cd114315f798ba59b1692264", [
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.620, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认62%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认55%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认30%, 0% ~ 100%"""
    分身_III             = EffectMeta("分身 III", False, "7399480997512744197", "7399480997512744197", "5b218df611d57e62c26029c0df884b13", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 0.600),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 60%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    动感爱心             = EffectMeta("动感爱心", False, "7399483016080395525", "7399483016080395525", "9908a1656669aadf0d2de2d4935506e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    千层1                = EffectMeta("千层1", False, "7399480998175575301", "7399480998175575301", "5fdd2c8768a84832cd95e1af79ef6d45", [
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认95%, 0% ~ 100%
    effects_adjust_color: 默认95%, 0% ~ 100%
    effects_adjust_luminance: 默认90%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认90%, 0% ~ 100%"""
    千禧辣妹             = EffectMeta("千禧辣妹 ", False, "7399482976498748678", "7399482976498748678", "b5d70363ad099bd197d196c92dd7f6a8", [
                              EffectParam("effects_adjust_number", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    单向移动             = EffectMeta("单向移动", False, "7399485225044053253", "7399485225044053253", "1efa77e2563de9f51ecf4c8639a995bc", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.490, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_rotate: 默认49%, 0% ~ 100%"""
    啦啦队队长           = EffectMeta("啦啦队队长", False, "7311300825593203974", "7311300825593203974", "997d6b9c5899ab5b4850c11bd2cacbc1", [])
    喜欢                 = EffectMeta("喜欢", False, "7399481768698481926", "7399481768698481926", "aef40b9f0ed093f941936ce4e4920d87", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    声波                 = EffectMeta("声波", False, "7399483724942806278", "7399483724942806278", "ad688844376cd0661f5aa811a344d0e7", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    大嘴                 = EffectMeta("大嘴", False, "7395449013832633606", "7395449013832633606", "e213546a518c747cdf6342e39c1dfbb1", [])
    大头                 = EffectMeta("大头", False, "7395448176821505286", "7395448176821505286", "7518e7eb3e186350b688bf712b960c97", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    天使翅膀             = EffectMeta("天使翅膀", False, "7399480997512776965", "7399480997512776965", "8d081ccae6c612fa28d24b1f292b2561", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    委屈脸               = EffectMeta("委屈脸", False, "7399484332810947845", "7399484332810947845", "ff707d357a6e8fc5809a9fd4878a9f16", [])
    嬉皮士               = EffectMeta("嬉皮士", False, "7309019460441083142", "7309019460441083142", "2bd3ff6f4fb90fbcbf6c8250a2c17d2b", [])
    害羞                 = EffectMeta("害羞", False, "7399482664274742534", "7399482664274742534", "6904d753832ee54a39f46fb23e0c47fc", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    尴尬脸               = EffectMeta("尴尬脸", False, "7395448375660907781", "7395448375660907781", "e40a40c3b1406c65ac02c0d319508e0b", [])
    局部扭曲             = EffectMeta("局部扭曲 ", False, "7399483861056408837", "7399483861056408837", "da8f3f99ca659d2710b2f9dcecf5fe4c", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    局部模糊             = EffectMeta("局部模糊 ", False, "7399481185182813446", "7399481185182813446", "fe329834047296c53106b22f5d7d6d1a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    幻影                 = EffectMeta("幻影", False, "7399485048145087750", "7399485048145087750", "6699feabadc4f59732b8087620fc95a6", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    幻影脸               = EffectMeta("幻影脸", False, "7399484026400083206", "7399484026400083206", "327f6afb9dbdd910f127660c1beee71c", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    幽灵                 = EffectMeta("幽灵", False, "7399484574536944902", "7399484574536944902", "6cc1df4c330fce3c92fefc89fbe4b7f6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    彩色蜡笔描边         = EffectMeta("彩色蜡笔描边", False, "7405137088066243845", "7405137088066243845", "627fe88b5ef1638c561ccec8d2964b6a", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    彩色负片             = EffectMeta("彩色负片", False, "7399483078462196998", "7399483078462196998", "2cd6462bd0bde3023d5f7069cd549b17", [
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色重影             = EffectMeta("彩色重影", False, "7399480863555194117", "7399480863555194117", "3beec60f57b90ccc2b451a1b5c0152e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    彩虹流体             = EffectMeta("彩虹流体", False, "7399484125419146502", "7399484125419146502", "2725088e1378997bea428c8b04e2b15f", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩虹眼泪             = EffectMeta("彩虹眼泪 ", False, "7399482282290990342", "7399482282290990342", "58cb3f3ea65a610f558fc940a521e0d1", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    怦然心动             = EffectMeta("怦然心动", False, "7399481501693398277", "7399481501693398277", "5a015d4cb0277db6f8f68ca713f2fe1b", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认85%, 0% ~ 100%"""
    恶魔之翼             = EffectMeta("恶魔之翼", False, "7399483093180091654", "7399483093180091654", "99cdde82bb5587966f1a2bac10d024f2", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    恶魔印记             = EffectMeta("恶魔印记", False, "7399481862231575813", "7399481862231575813", "41cb4d0311f7e48a4449e41e509f2b9b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    情绪定格             = EffectMeta("情绪定格", False, "7399484519851592966", "7399484519851592966", "0214fe4b62e32eaba5e2e7b33d31f848", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认10%, 0% ~ 100%"""
    意识流               = EffectMeta("意识流", False, "7399482325517552902", "7399482325517552902", "737af2105f0e42907235947e04f1b1d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    我麻了               = EffectMeta("我麻了", False, "7399482884911860998", "7399482884911860998", "b3078ea7691c02789dec4360d7ebd5a5", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    打击                 = EffectMeta("打击", False, "7399484486112562438", "7399484486112562438", "b310c3ede33e6e0819859dbc67ffab7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认55%, 0% ~ 100%"""
    扫描_I               = EffectMeta("扫描 I", False, "7399483093179976966", "7399483093179976966", "8bf99848475e99658effbfcf7e22cfc9", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    拽酷                 = EffectMeta("拽酷", False, "7399482275659795718", "7399482275659795718", "fa8d8ef3f263d4f13327b6bddc10ed0a", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    描边发散_II          = EffectMeta("描边发散 II", False, "7399482034718117125", "7399482034718117125", "2bc7ecc4b79a372c9fed9a86b850d8a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    故障描边_I           = EffectMeta("故障描边 I", False, "7399482870496120069", "7399482870496120069", "81d3df834a57b08e7dd65682488b8361", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    敲打                 = EffectMeta("敲打", False, "7399482189454249222", "7399482189454249222", "67737d95f8256e6915b26c3efd41f305", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    文字环绕             = EffectMeta("文字环绕", False, "7399482784684788997", "7399482784684788997", "d12c4f42c3cf9dda4af70b8dbcd5b47d", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    星光放射             = EffectMeta("星光放射", False, "7399482324045384966", "7399482324045384966", "cfd7080a8db30efbe03aeafa5d667e22", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    星星拖尾             = EffectMeta("星星拖尾", False, "7399483188466158853", "7399483188466158853", "d53616c1e937c59555dda26f9f606a75", [])
    机械几何             = EffectMeta("机械几何", False, "7399483060611271942", "7399483060611271942", "fea80b64e8ecc79b44b169eafa597942", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械姬_II            = EffectMeta("机械姬 II", False, "7399483264680873222", "7399483264680873222", "d2a0fade121195a25cc45887af871c60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械环绕_I           = EffectMeta("机械环绕 I", False, "7399482993795943686", "7399482993795943686", "bff38e9886478c86635d990f78ca68cd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械环绕_II          = EffectMeta("机械环绕 II", False, "7399481709219106054", "7399481709219106054", "66eb2b1b98e4ada7cacba9c39d37be74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    棒球选手             = EffectMeta("棒球选手", False, "7309019460441050374", "7309019460441050374", "2047ee12a5f4a743e5cb1a22f8b06ef8", [])
    气体流动             = EffectMeta("气体流动", False, "7409873600536268037", "7409873600536268037", "9b45c0084913ee96062cda0f5b2d978d", [
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认67%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    气泡_I               = EffectMeta("气泡 I", False, "7399483264680889606", "7399483264680889606", "c6d3497d3574c8530982ff6481813dad", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    气泡_II              = EffectMeta("气泡 II", False, "7399481501693332741", "7399481501693332741", "baa4deca23e318235dde9d7435ec9923", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    气波                 = EffectMeta("气波", False, "7399483565936774406", "7399483565936774406", "d49684beffa531728f6d0b2f5823a465", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    沉沦                 = EffectMeta("沉沦", False, "7399483158132952326", "7399483158132952326", "521b388b76a4777d0e2fcee81e18ec82", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    波点分身             = EffectMeta("波点分身", False, "7399482976498617606", "7399482976498617606", "ea3cfc504a4f323a6139f768f8c4790c", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    流光描边             = EffectMeta("流光描边", False, "7409874352809823494", "7409874352809823494", "43de1121773eea81624460ed929b17e8", [
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认85%, 0% ~ 100%
    effects_adjust_size: 默认15%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    涂鸦鬼影             = EffectMeta("涂鸦鬼影 ", False, "7399480912217492742", "7399480912217492742", "9570d183c3973de1498c638834c5136d", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    火焰拖尾             = EffectMeta("火焰拖尾", False, "7399482290864131333", "7399482290864131333", "8cceb3e50ff34355a70fec18b66e8dd0", [])
    火焰描边II           = EffectMeta("火焰描边II", False, "7399484507654475013", "7399484507654475013", "403fafa6820bbcad95da45e27904f711", [
                              EffectParam("effects_adjust_color", 0.050, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认5%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    火焰描边_I           = EffectMeta("火焰描边 I", False, "7399482815789747462", "7399482815789747462", "c59e7d23c8ce0d8b6e783baaac417c45", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    火焰眼_I             = EffectMeta("火焰眼 I", False, "7399481296281439493", "7399481296281439493", "f540fbe1b2c8581bbbaead29b7f9bceb", [
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认15%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    火焰翅膀I            = EffectMeta("火焰翅膀I", False, "7399480912217427206", "7399480912217427206", "bab3b65e0ca81daf7fbef82971d57527", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    灵机一动_I           = EffectMeta("灵机一动 I", False, "7399480953715887365", "7399480953715887365", "e85be094fc8565285ab03b8854955213", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.600, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认60%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    灵魂出走             = EffectMeta("灵魂出走", False, "7399482680515005702", "7399482680515005702", "4331fabcec39447b514f38343026f7fc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    热力光谱             = EffectMeta("热力光谱", False, "7399482670608108805", "7399482670608108805", "b578d3e33d8c650dc445c19875f9613f", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    热力光谱_Ⅱ           = EffectMeta("热力光谱 Ⅱ", False, "7399482635732389125", "7399482635732389125", "b711586fdabf06e7975e4bc2f2d906e6", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    热恋                 = EffectMeta("热恋", False, "7399484442315705605", "7399484442315705605", "2aa9298939a522ca05e5219ab6e91cf6", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    焰火                 = EffectMeta("焰火", False, "7399482784684707077", "7399482784684707077", "3dc040bd8a6d3853428cc18030e7872a", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    爱心攻击             = EffectMeta("爱心攻击", False, "7399481781080083718", "7399481781080083718", "004327d32e6f38279d4f2e6d9d51ae28", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.350, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认35%, 0% ~ 100%"""
    爱心眼               = EffectMeta("爱心眼", False, "7399483093180009734", "7399483093180009734", "aeee56c74c823b2afda571c023d0f992", [
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.050, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认15%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认5%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    爱心美瞳             = EffectMeta("爱心美瞳", False, "7399482959058783494", "7399482959058783494", "56f06fc88908e0e8fad7c329bdea3d39", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    狼人                 = EffectMeta("狼人 ", False, "7399481430813723910", "7399481430813723910", "5227f6bbfb1ec8c7fa0d96fb1d9d6d82", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    猩猩脸               = EffectMeta("猩猩脸", False, "7395447966154198277", "7395447966154198277", "d7d8f40a09f8ff9a318cf0ce19b31756", [])
    生气                 = EffectMeta("生气", False, "7399484014848953605", "7399484014848953605", "197e65ef3a95cc74b5166c8f5fca1e44", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    电光扫描             = EffectMeta("电光扫描", False, "7399483445958692101", "7399483445958692101", "1a5266ab56ea0645c20f0160aee7743e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认90%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    电光描边_II          = EffectMeta("电光描边 II", False, "7399482577498688773", "7399482577498688773", "0177b9dd16527e7c082ad4ddfe59f0bc", [
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.110, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认75%, 0% ~ 100%
    effects_adjust_distortion: 默认65%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%
    effects_adjust_color: 默认11%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    电光放射             = EffectMeta("电光放射 ", False, "7399482290864196869", "7399482290864196869", "4382fab8340a892419f032990d55580b", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    电光氛围             = EffectMeta("电光氛围", False, "7399482351182564614", "7399482351182564614", "9a4b3a8a67ed675e0e6820356e03c473", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    电光灼烧             = EffectMeta("电光灼烧", False, "7399483565882379526", "7399483565882379526", "138833aba593bb8cf308ce1d449ce994", [
                              EffectParam("effects_adjust_rotate", 0.730, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认73%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    电光眼               = EffectMeta("电光眼", False, "7399483006278307077", "7399483006278307077", "12aed71e7e62dafe99b6ff5ef264a36d", [
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电击                 = EffectMeta("电击", False, "7399482670608043269", "7399482670608043269", "647a269d3f5f8183adb43912d4391397", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    眼神光               = EffectMeta("眼神光", False, "7399482461798894853", "7399482461798894853", "665fec8aacac1d793e7917a0a0ec3ab3", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    碎片分身             = EffectMeta("碎片分身", False, "7399482948094872838", "7399482948094872838", "86532426a7e3c08c229dd518c51a893c", [
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认95%, 0% ~ 100%
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    移形幻影_I           = EffectMeta("移形幻影  I", False, "7399484090472221957", "7399484090472221957", "c89c34b83924f3fb5c88f2ece2e095b8", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    立体相册             = EffectMeta("立体相册", False, "7298373731326627078", "7298373731326627078", "99972a8cdabaa211423f2bfe40ae38a1", [])
    笑哭                 = EffectMeta("笑哭", False, "7399483155058642181", "7399483155058642181", "c9d603c85b8bcf6e129e79e672ea2bba", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%"""
    篮球运动员           = EffectMeta("篮球运动员", False, "7309019460441066758", "7309019460441066758", "9372ae7b32165627ef7b227cfef0de49", [])
    纸质描边             = EffectMeta("纸质描边", False, "7399484014848969989", "7399484014848969989", "08b110f0dd5716125c852fda11087adb", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    美国女性_I           = EffectMeta("美国女性 I", False, "7399483917344017670", "7399483917344017670", "bde6e304a5de9614c0f44644fd3d15be", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国男性_II          = EffectMeta("美国男性 II", False, "7399482402403405062", "7399482402403405062", "b09c7a6c2134a95aeac139f06217cdde", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美式橄榄球           = EffectMeta("美式橄榄球", False, "7311300825593253126", "7311300825593253126", "7ddbdd20c0406dc042e7c9e48ebf4952", [])
    老钱风               = EffectMeta("老钱风", False, "7311300825593154822", "7311300825593154822", "242f9ebc6f8aa4e599bc20f52b1c6508", [])
    背景拖影             = EffectMeta("背景拖影", False, "7399483158133001478", "7399483158133001478", "e6c9f05435c8a8912b1321bfa9f39a4a", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认85%, 0% ~ 100%"""
    背景旋转             = EffectMeta("背景旋转", False, "7399480876050025734", "7399480876050025734", "cd94d767b9599d89e59d532a123d8bde", [
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    背景氛围II           = EffectMeta("背景氛围II", False, "7399482822592892165", "7399482822592892165", "d92206d19cb5ae6f8c704fea8639a90a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    脸红                 = EffectMeta("脸红 ", False, "7399482454282620165", "7399482454282620165", "ee9903ac2f08d10c172b1bd05a03c58d", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.802, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    脸部马赛克           = EffectMeta("脸部马赛克 ", False, "7399481303424437510", "7399481303424437510", "a2669cddba1a547ee9330215fe32e86b", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    舞者_II              = EffectMeta("舞者 II", False, "7399481998789709062", "7399481998789709062", "fd3b8de0e9c935aad28903d80d95aaca", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    色差扩散             = EffectMeta("色差扩散", False, "7399481832833666309", "7399481832833666309", "d37117a77c1710d52e88f5c4320add2e", [
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.650, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认65%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认65%, 0% ~ 100%"""
    荧光闪屏             = EffectMeta("荧光闪屏", False, "7399484270458178822", "7399484270458178822", "966eed9a941222efd6243c0df6159c59", [
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.254, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认85%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    萤火                 = EffectMeta("萤火", False, "7399482348162764037", "7399482348162764037", "000701418e2acde7230cfdcc680ef895", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    蝴蝶翅膀             = EffectMeta("蝴蝶翅膀", False, "7399482906378390789", "7399482906378390789", "9971f59512aeb3df57cf3fc26a97ae30", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    血迹_II              = EffectMeta("血迹 II ", False, "7399483392007376134", "7399483392007376134", "7ea503116f042e8a297efa3259d554f7", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    视线遮挡             = EffectMeta("视线遮挡 ", False, "7399482351182449926", "7399482351182449926", "9d6829ecbc85a6653ca44ccd18c9243f", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    赛博朋克_I           = EffectMeta("赛博朋克 I", False, "7399483006278257925", "7399483006278257925", "6ae35b45fc05d783fc60e5f1cf397ba4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    赛博朋克_II          = EffectMeta("赛博朋克 II", False, "7399481714298637574", "7399481714298637574", "7af7f6b4df582a2c06c143bb34f5b361", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    迷茫                 = EffectMeta("迷茫", False, "7399483664905686277", "7399483664905686277", "8650950b4b9d15219c9aeeb6a2e4adfa", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    镭射眼_Ⅰ             = EffectMeta("镭射眼 Ⅰ", False, "7399483006278192389", "7399483006278192389", "ea9d0666a569334a0c6b27c14ade2674", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    镭射眼_ⅠⅠ            = EffectMeta("镭射眼 ⅠⅠ", False, "7399482068146588933", "7399482068146588933", "3891948240e1594b7ea8025222341a9d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.620, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认62%, 0% ~ 100%"""
    闪电                 = EffectMeta("闪电", False, "7399483733931248901", "7399483733931248901", "9c97ab760617a5c3bc75491b3ad8406b", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    闪电眼               = EffectMeta("闪电眼", False, "7399481529723800838", "7399481529723800838", "6b6b4e9eb53581fea08118f62d55c1a9", [
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_luminance: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%"""
    难过                 = EffectMeta("难过", False, "7399484219753286918", "7399484219753286918", "0491f6c803d6983d38bd78f401b93168", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    霓虹涂鸦             = EffectMeta("霓虹涂鸦", False, "7399484335642004742", "7399484335642004742", "a96b78f7ee84b7cab457a31baf62a4f0", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认22%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%"""
    霓虹渐变             = EffectMeta("霓虹渐变", False, "7399480953715936517", "7399480953715936517", "1fca51ec5627ab19543f51e79beeab4d", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    音符拖尾_II          = EffectMeta("音符拖尾 II", False, "7399481883224001797", "7399481883224001797", "d3eeb550f3b10e253d9c6c4a7db9caf4", [])
    飞翔的帽子           = EffectMeta("飞翔的帽子", False, "7399482799171849478", "7399482799171849478", "a7ff6e41415354401d8c8ebf0a6f9d14", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""

    # 付费特效
    BOOM                 = EffectMeta("BOOM！", True, "7399482193548037381", "7399482193548037381", "996955736fc7f9cce0eaecad6bd6c804", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    Doll                 = EffectMeta("Doll", True, "7399484281845779718", "7399484281845779718", "c0c9995130fbb4ebf13bae19a0398d45", [])
    Motion_Pattern       = EffectMeta("Motion Pattern", True, "7399481699148516613", "7399481699148516613", "c85f145b3d2c840d2407957fb458db4a", [
                              EffectParam("effects_adjust_number", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认40%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    Neon_Motion          = EffectMeta("Neon Motion", True, "7399481303424421126", "7399481303424421126", "a30c2949ccfc35417421caf68261ae0b", [
                              EffectParam("effects_adjust_size", 0.510, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认51%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    X                    = EffectMeta("X ", True, "7399481652600229125", "7399481652600229125", "ec38784544361583ed45aa333ebdf2c9", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    X瞬移                = EffectMeta("X瞬移", True, "7399484332811013381", "7399484332811013381", "366528fe2ee5c5c851a694073cf4b855", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    _3_Love              = EffectMeta("<3 Love", True, "7399481628495580421", "7399481628495580421", "6c67631f71ea048811d54d51ffc07683", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    交叉移形             = EffectMeta("交叉移形", True, "7399484219753352454", "7399484219753352454", "51d5703a0b872d59a79abad1d1d1291b", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    人物发光I            = EffectMeta("人物发光I", True, "7414191273340439814", "7414191273340439814", "41c861f0d13e187e3e2e4e2621df22f1", [])
    人物故障             = EffectMeta("人物故障", True, "7414192006630493445", "7414192006630493445", "fac02dc9fa86764ff5fd478775349305", [])
    像素定格             = EffectMeta("像素定格", True, "7414191813944167685", "7414191813944167685", "7743c48164a2435146c5faae77c38fed", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    像素面具             = EffectMeta("像素面具", True, "7399482034713840902", "7399482034713840902", "7e2e6e1e8fcb38d5ffead61c04b0721c", [
                              EffectParam("effects_adjust_number", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.280, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认8%, 0% ~ 100%
    effects_adjust_color: 默认28%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    光溶解1              = EffectMeta("光溶解1", True, "7399481960285900038", "7399481960285900038", "8663c979a35c2483c86151b911e9271b", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 0.600),
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 60%
    effects_adjust_color: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    几何拖尾I            = EffectMeta("几何拖尾I", True, "7399482664505314565", "7399482664505314565", "1f441482ec9cf28fcf7373dce0c08ceb", [])
    几何拖尾II           = EffectMeta("几何拖尾II", True, "7399481784527867142", "7399481784527867142", "e4042d18c205074ab5dee4bf6c19bbbf", [])
    动态涂鸦             = EffectMeta("动态涂鸦", True, "7414192037219536133", "7414192037219536133", "b8909d685182002653669b6d00cd21db", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    千层2                = EffectMeta("千层2", True, "7399482941799288070", "7399482941799288070", "043ab3ce69a10f0c26efeba74eeacbe9", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.500)])
    """参数:
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认3%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 150%"""
    卡顿线条             = EffectMeta("卡顿线条", True, "7414191641054940422", "7414191641054940422", "cfd03ea2fdf53795db434bad0b1dc95d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    发光分身             = EffectMeta("发光分身", True, "7399480863555177733", "7399480863555177733", "dbff6732319cf9488da4816c188d9f1a", [
                              EffectParam("effects_adjust_color", 0.840, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.102, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认84%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%"""
    发光拖影             = EffectMeta("发光拖影", True, "7399483839392926982", "7399483839392926982", "21c91398cba50ea1d3ab84638a6cc2b2", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.710, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认71%, 0% ~ 100%
    effects_adjust_number: 默认95%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%"""
    发光标记             = EffectMeta("发光标记", True, "7399484008675020037", "7399484008675020037", "bf0d0faa47d9aba707db6a029a4c9aa2", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认25%, 0% ~ 100%"""
    发光溶解             = EffectMeta("发光溶解", True, "7399482392475356422", "7399482392475356422", "519e03449e68a63303473ab640263045", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认70%, 0% ~ 100%
    effects_adjust_distortion: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    发光贴纸             = EffectMeta("发光贴纸 ", True, "7399481862231493893", "7399481862231493893", "77fa7c8ef8f36dfc3c8f2f37a2b29e04", [
                              EffectParam("effects_adjust_number", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    可爱猪               = EffectMeta("可爱猪", True, "7395448362809429254", "7395448362809429254", "483efc4867b85d9bf7c39a6b1d878b8d", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    吸收溶解             = EffectMeta("吸收溶解", True, "7399483917343968518", "7399483917343968518", "16decb7d89bf1c35f3ffe139c1abfb5a", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    吸血鬼               = EffectMeta("吸血鬼", True, "7399482906378292485", "7399482906378292485", "dab4696a548436547e84bffce2c8b367", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    哥特                 = EffectMeta("哥特 ", True, "7399483785554824454", "7399483785554824454", "f0a791b47d3c747c81389457b07c6460", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    圣诞辣妺             = EffectMeta("圣诞辣妺", True, "7399482376784465158", "7399482376784465158", "6e3aae449238d6ed9c7750d0ad2f2da0", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    基础发光             = EffectMeta("基础发光", True, "7399482282291039494", "7399482282291039494", "60d661ed500294da06c78d48264fa417", [
                              EffectParam("effects_adjust_color", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认22%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    天使                 = EffectMeta("天使", True, "7399481832833682693", "7399481832833682693", "1733f4722c84469a54360d5e5946724e", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%"""
    天使光环             = EffectMeta("天使光环", True, "7399483565936856326", "7399483565936856326", "559472cf83d715d6e1b753133426f54b", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认85%, 0% ~ 100%
    effects_adjust_number: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    天使环               = EffectMeta("天使环", True, "7399481435129793797", "7399481435129793797", "5782ef42472fd9771f9113d98b6e4e58", [])
    孤独卓别林           = EffectMeta("孤独卓别林", True, "7414191809309445381", "7414191809309445381", "4a220dd2837f2ee520c03f42a4a69f0d", [])
    巴哥犬               = EffectMeta("巴哥犬", True, "7395447942288592134", "7395447942288592134", "6764c992938b5c0e62dfc6e46255bde7", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    幻彩流光             = EffectMeta("幻彩流光", True, "7399484020842614021", "7399484020842614021", "918e1a205ed6f71cebfb836b98a11685", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认95%, 0% ~ 100%
    effects_adjust_color: 默认20%, 0% ~ 100%"""
    幻影平移             = EffectMeta("幻影平移", True, "7399484626386832645", "7399484626386832645", "0eef8fceb4281f669643df7150e8f142", [
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    弥散流光             = EffectMeta("弥散流光 ", True, "7399483016080297221", "7399483016080297221", "eabd69cd578279cf0dc892e088f60da6", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%"""
    彩虹边缘             = EffectMeta("彩虹边缘", True, "7399482664505396485", "7399482664505396485", "f606204f1dd208987014bf12d6d95d85", [
                              EffectParam("effects_adjust_intensity", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认55%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认15%, 0% ~ 100%"""
    影分身               = EffectMeta("影分身", True, "7399480698286902533", "7399480698286902533", "8088e845f5e6b8aecd6a9245cf033cfb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    心动信号             = EffectMeta("心动信号 ", True, "7399482527376772358", "7399482527376772358", "a4758810ef78bfca76c45486faeac99d", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    心里是你             = EffectMeta("心里是你", True, "7399482664274709766", "7399482664274709766", "62cf1078f3a0e623c349cb4200f3de26", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    恐怖小丑             = EffectMeta("恐怖小丑 ", True, "7399483278450855174", "7399483278450855174", "f3b778abc80442b5be41554e9ace07d2", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    恶灵骑士             = EffectMeta("恶灵骑士", True, "7399481768698596614", "7399481768698596614", "424a452c0aebfe23b2f0be6f8c1906ae", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    恶魔尾巴             = EffectMeta("恶魔尾巴 ", True, "7399482941799140614", "7399482941799140614", "7ab5f92c75beb4747dc81731b447f53c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认100%, 0% ~ 100%"""
    恶魔角               = EffectMeta("恶魔角", True, "7399483157642317061", "7399483157642317061", "e3331ccd99a663f0561f82ac87441dcf", [])
    手绘描边             = EffectMeta("手绘描边", True, "7399481789602958597", "7399481789602958597", "c858135cf8832af09462c841daaf16e5", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 100%"""
    扫描_II              = EffectMeta("扫描 II", True, "7399484742187486469", "7399484742187486469", "994c0cfd5f8fb5fbe0caf76a034f34a6", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    拖影分身             = EffectMeta("拖影分身", True, "7399482897763224838", "7399482897763224838", "2efa12e4351be5d5cc88e3970d8dc360", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认15%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    拼贴海报             = EffectMeta("拼贴海报", True, "7399481296281505029", "7399481296281505029", "602c047f7cafe02427da4b327fd260cf", [
                              EffectParam("effects_adjust_vertical_chromatic", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.661, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_chromatic: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认10%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_texture: 默认66%, 0% ~ 100%
    effects_adjust_filter: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    描边发散_I           = EffectMeta("描边发散 I", True, "7399481013707132165", "7399481013707132165", "1b4bb97dcffe8d86aa6b1b93c301d833", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    旋转分身             = EffectMeta("旋转分身", True, "7399483338504850694", "7399483338504850694", "97aca86400b323ad6995d593ab70b8d4", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 0.750),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 75%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    旋转反弹             = EffectMeta("旋转反弹", True, "7399482189454396678", "7399482189454396678", "8dd47665186380dfb3ebc592c523f0db", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认65%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    旋转扭曲             = EffectMeta("旋转扭曲", True, "7399483016080313605", "7399483016080313605", "ef0208044a1a8224460aae8795057d67", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    旋转摆动             = EffectMeta("旋转摆动", True, "7399482527376837894", "7399482527376837894", "5ad68892dadfc4b15d43bb4572fefcd7", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_distortion: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%"""
    无限穿越             = EffectMeta("无限穿越", True, "7399484626386898181", "7399484626386898181", "9fd5f765ac79b8b8ed97de389cc8e24c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认0%, 0% ~ 100%"""
    未来眼镜             = EffectMeta("未来眼镜", True, "7399479867118570757", "7399479867118570757", "63218c521abe80cdae5d3fbb87085fc9", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    机械姬_I             = EffectMeta("机械姬 I", True, "7399483472135326982", "7399483472135326982", "0226967d2ceb5b64b15074a40a0353a0", [])
    梦境                 = EffectMeta("梦境", True, "7399483558999493894", "7399483558999493894", "b8fa368f9884388772c7b8d1d95e8851", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    流体故障             = EffectMeta("流体故障", True, "7399481013707246853", "7399481013707246853", "0f6cf4ee5dd24c6e6f55fdb0f8825efa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%"""
    涂鸦弹出             = EffectMeta("涂鸦弹出", True, "7478895946168929589", "7478895946168929589", "241e693dc1e317bfc992812bbe3b435e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    涂鸦扩散             = EffectMeta("涂鸦扩散", True, "7414313197915639046", "7414313197915639046", "0ef8c7fa34c946921395ca9acbf7699c", [])
    涂鸦闪光_2           = EffectMeta("涂鸦闪光 2", True, "7474929537348881717", "7474929537348881717", "52447a8a854394a086a7848f5d1d53c8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    漩涡溶解             = EffectMeta("漩涡溶解", True, "7399484143148518662", "7399484143148518662", "3281d02205f102f70c4b07021be5bc71", [
                              EffectParam("effects_adjust_distortion", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认45%, 0% ~ 100%
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认45%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认25%, 0% ~ 100%
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_range: 默认45%, 0% ~ 100%"""
    潮流入侵             = EffectMeta("潮流入侵 ", True, "7399482598499618053", "7399482598499618053", "4e77c3e9747705249571f6d7794ddd28", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认33%, 0% ~ 100%"""
    激光几何             = EffectMeta("激光几何", True, "7399485027047705861", "7399485027047705861", "61e81667f7930fa9f587f23c95f40311", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰图腾             = EffectMeta("火焰图腾", True, "7399484178372381957", "7399484178372381957", "35e9cbe081d47066558a717ce3a774d8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰恶魔角           = EffectMeta("火焰恶魔角", True, "7399481784527834374", "7399481784527834374", "7ef891a9373eec515dc91dc20557fa78", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认55%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    火焰环绕             = EffectMeta("火焰环绕", True, "7399479761107504390", "7399479761107504390", "0336f00d05b706cf8ab9742af8ee16c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    火焰眼II             = EffectMeta("火焰眼II", True, "7399482956953193734", "7399482956953193734", "a03eb99bf5acdfc69965fc12b3705a6f", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    火焰翅膀II           = EffectMeta("火焰翅膀II", True, "7399484090472254725", "7399484090472254725", "93fa02d91dd5f7fd2c41314358ba462d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    点赞                 = EffectMeta("点赞 ", True, "7399480629525564677", "7399480629525564677", "9f934cf082ec4d56a6f86e6e1aa2c8f6", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    热成像               = EffectMeta("热成像", True, "7399483157642284293", "7399483157642284293", "0b3ac634a1bf8aea5b7c7aa8dde94772", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    爱心焰火             = EffectMeta("爱心焰火", True, "7399483839392894214", "7399483839392894214", "a6acb1e8bd33d1fec2ac6a02cd685e1f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    爱心背景             = EffectMeta("爱心背景", True, "7399482870496070917", "7399482870496070917", "fabf8aa698dcd25b68894a751b9b2799", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    爱心荆棘             = EffectMeta("爱心荆棘 ", True, "7399483188466273541", "7399483188466273541", "63562b0e10da05ca83adf7fcdab92909", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    狱火                 = EffectMeta("狱火", True, "7399481781080165638", "7399481781080165638", "29903a65ede13673b23ac1eedc118b5d", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    猫耳女孩             = EffectMeta("猫耳女孩", True, "7395448796882160902", "7395448796882160902", "486df1ec5de1ca0a69210b844b912534", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    电光描边             = EffectMeta("电光描边", True, "7399483392007441670", "7399483392007441670", "145190d336ffd5ecf5f17f0d652a7eac", [
                              EffectParam("effects_adjust_color", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认85%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%"""
    电光耳机             = EffectMeta("电光耳机", True, "7399482670373145862", "7399482670373145862", "19a87efa0bebe59cdf36eda727a66664", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    电子屏故障           = EffectMeta("电子屏故障", True, "7399483820812078341", "7399483820812078341", "c8720830b4ca9dece113ef06e3d6c151", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    电流_I               = EffectMeta("电流 I", True, "7399483447196093701", "7399483447196093701", "d9511ac43cdb62b2470c0367892f45df", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    电流_II              = EffectMeta("电流 II", True, "7399484835187674373", "7399484835187674373", "b723ef9e84049ebbee327ba93c4d645f", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    眼机器               = EffectMeta("眼机器", True, "7479499141698145597", "7479499141698145597", "7ea5f158f0918b404181bebeb4be5c9b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    瞬移                 = EffectMeta("瞬移", True, "7399482948094889222", "7399482948094889222", "7e15930206e4c6b868409f564de9007e", [
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    碎闪边缘             = EffectMeta("碎闪边缘", True, "7399484344781294853", "7399484344781294853", "5cf6c328e08bab2a229818bc8c2353a1", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认15%, 0% ~ 100%"""
    科技氛围_II          = EffectMeta("科技氛围 II", True, "7399483900235353350", "7399483900235353350", "206a5e4755fd9e0316b179da31b78b27", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    科技氛围_III         = EffectMeta("科技氛围 III", True, "7399484418508754182", "7399484418508754182", "3af322e984347e0ab872bd3f51d15f07", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    移形回位             = EffectMeta("移形回位", True, "7399481430813805830", "7399481430813805830", "0c2b3fc80b6cc2c2bad4e8cd7ea420d5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    移形幻影2            = EffectMeta("移形幻影2", True, "7399483060611206406", "7399483060611206406", "036f417355069c71ba62b75acb876c94", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    空气流体             = EffectMeta("空气流体", True, "7399483558999444742", "7399483558999444742", "9882eb0caf97221ac6bd4161ead3a263", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.660, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认72%, 0% ~ 100%
    effects_adjust_size: 默认66%, 0% ~ 100%"""
    空间扰动             = EffectMeta("空间扰动", True, "7535399603122883856", "7535399603122883856", "8d78ae0551cdb99f9d9f6cccd241b748", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    箭头环绕             = EffectMeta("箭头环绕", True, "7399483838977690886", "7399483838977690886", "c4543904bdf336051dee6e64c8b5ebdd", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    粉色便便             = EffectMeta("粉色便便", True, "7395447877557832966", "7395447877557832966", "0c843a5ba39df7e037f4995040f79263", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    粒子弥散             = EffectMeta("粒子弥散", True, "7399484178372234501", "7399484178372234501", "7a72cd5b5950e933ca7f6df425537c21", [
                              EffectParam("effects_adjust_horizontal_shift", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认66%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    红恶魔               = EffectMeta("红恶魔 ", True, "7399484125419277574", "7399484125419277574", "111bd012c58bdcb7e2074b79e6cee5e7", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    纵轴旋转             = EffectMeta("纵轴旋转", True, "7399484900816096517", "7399484900816096517", "36609d6a90300cb14dd60a5930f24bc1", [
                              EffectParam("effects_adjust_speed", 0.530, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.060, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认53%, 0% ~ 100%
    effects_adjust_rotate: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认6%, 0% ~ 100%"""
    纸张拼贴             = EffectMeta("纸张拼贴", True, "7414191181501959430", "7414191181501959430", "e2b5e11e2f24940b65c91615723613f6", [])
    线条描边             = EffectMeta("线条描边", True, "7414312909318278405", "7414312909318278405", "0a6c8f773aa4fbfe7069b3205e6d58d0", [])
    绿怪                 = EffectMeta("绿怪", True, "7399484020842646789", "7399484020842646789", "f733adf3945ddca34efc9d07723bc46f", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美国女性_II          = EffectMeta("美国女性 II", True, "7399482520531684613", "7399482520531684613", "6d9b6990df1d66bad249c5defd435576", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国女性_III         = EffectMeta("美国女性 III", True, "7399481106514464006", "7399481106514464006", "43567fd71493d00bc90873169a742c7b", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国女性_IV          = EffectMeta("美国女性 IV", True, "7399481185182829830", "7399481185182829830", "c6df976c4473e4b8eeafc25bb4020926", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国男性_I           = EffectMeta("美国男性 I", True, "7399482959058734342", "7399482959058734342", "a6e9afde1f86efbb91c49ecd9d6a8fdc", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国男性_III         = EffectMeta("美国男性 III", True, "7399482275659828486", "7399482275659828486", "a572a62824360ad8c2a73f75751e388a", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    美国男性_IV          = EffectMeta("美国男性 IV", True, "7399482633811479814", "7399482633811479814", "2ee84c6f69fd3bd4bb081d75862629ee", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    脸部扫描特效         = EffectMeta("脸部扫描特效", True, "7480501931903946037", "7480501931903946037", "aa65e42719c444e5622a12f995d72351", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    脸部故障             = EffectMeta("脸部故障", True, "7399483861056457989", "7399483861056457989", "b00871e8d7e141731a2fe3ca29bb857a", [
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    舞者                 = EffectMeta("舞者", True, "7399482815789731078", "7399482815789731078", "028dc52a5001968b404f2fdeb6d74468", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    血迹_I               = EffectMeta("血迹 I ", True, "7399482680515104006", "7399482680515104006", "f7eb5ded35a0bed4cb68cab1cf5b0a5e", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    血迹_III             = EffectMeta("血迹 III ", True, "7399482948094840070", "7399482948094840070", "ef2d26cad0ce2446e87cb695d5ddbc70", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    轨迹定格             = EffectMeta("轨迹定格", True, "7414312465204350213", "7414312465204350213", "aa4c152f60ffcb4683f0f64032c00a5c", [])
    轮廓扫描             = EffectMeta("轮廓扫描", True, "7399483733931330821", "7399483733931330821", "7abf09f3d054331c74f328ed951db5cb", [
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    迷幻光效             = EffectMeta("迷幻光效", True, "7399480876049992966", "7399480876049992966", "ab326c65ea0b93a6c8951b960f84db59", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    迷幻分身             = EffectMeta("迷幻分身", True, "7399482398745873670", "7399482398745873670", "27ca91c2612822bdb59b86af4d797ce5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_rotate: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%
    effects_adjust_size: 默认85%, 0% ~ 100%"""
    迷幻拖影             = EffectMeta("迷幻拖影", True, "7399481660384873734", "7399481660384873734", "d8ac8b085fb4fdc75c6fc293dc2f8e5f", [
                              EffectParam("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    迷幻震波             = EffectMeta("迷幻震波", True, "7399483664905637125", "7399483664905637125", "efeea694b2f32b849d93e589d04f5211", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认66%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    金厲麋鹿             = EffectMeta("金厲麋鹿", True, "7399482884911910150", "7399482884911910150", "b95d4dd9004420703ee2b6b76fecbc03", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    闪光放大_III         = EffectMeta("闪光放大 III", True, "7399484021194886406", "7399484021194886406", "a64dcdf7a22d382739051486535a4704", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%"""
    闪影                 = EffectMeta("闪影 ", True, "7399481709219073286", "7399481709219073286", "864dcb150b85814ca7615946c7265941", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪烁眼镜             = EffectMeta("闪烁眼镜", True, "7477478878009642293", "7477478878009642293", "217b95705c424323c13408f2db16890c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    闪电漩涡             = EffectMeta("闪电漩涡", True, "7399482906378341637", "7399482906378341637", "d7bcda1fb35926fa6cb1a823661dd114", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.240, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_speed: 默认24%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    闪电环绕             = EffectMeta("闪电环绕", True, "7399484574536846598", "7399484574536846598", "d2459fb754b3d9dbb469d29f6af77423", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    闪闪骷髅             = EffectMeta("闪闪骷髅", True, "7399482348162632965", "7399482348162632965", "7e488b3f5bedf0ff560a75ecc7d6adde", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    阳光                 = EffectMeta("阳光", True, "7399483524597828870", "7399483524597828870", "28f4000825108ddfa5778df584f32259", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    阴暗面               = EffectMeta("阴暗面", True, "7399481699148582149", "7399481699148582149", "22e698c9e8aa9fd5ea95d16d03e25474", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    霓虹爱心             = EffectMeta("霓虹爱心", True, "7399481239062859013", "7399481239062859013", "9d6f972481069644431af54815c8a75b", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    音符拖尾             = EffectMeta("音符拖尾", True, "7399482635732503813", "7399482635732503813", "b435f8b5610503a677c487f3aeb47ac7", [])
    飓风                 = EffectMeta("飓风", True, "7399482239110663429", "7399482239110663429", "a0bf72f591c6dbba8a211894f618976f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    马赛克分身           = EffectMeta("马赛克分身", True, "7399483838977658118", "7399483838977658118", "609544771e463e00dabcec5277b4ae0e", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%"""
    鬼灯                 = EffectMeta("鬼灯 ", True, "7399481513567390981", "7399481513567390981", "45b89e8fa64efea58633c7509c499237", [
                              EffectParam("effects_adjust_background_animation", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认67%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    黑色眼泪             = EffectMeta("黑色眼泪 ", True, "7399482454282718469", "7399482454282718469", "750bd65463d6f3d910cf09e3edb39a03", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
