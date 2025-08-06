"""视频画面特效元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class VideoSceneEffectType(EffectEnum):
    """视频画面特效枚举"""

    # 免费特效
    Beat_Shots           = EffectMeta("Beat Shots", False, "7399467127159278854", "7399467127159278854", "e258bc9e064d90c2b65ec5fed2320885", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    Betamax              = EffectMeta("Betamax", False, "7395469669638966534", "7395469669638966534", "37e4a3778510a091be8f436ef8ed47af", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认65%, 0% ~ 100%
    effects_adjust_sharpen: 默认25%, 0% ~ 100%
    effects_adjust_distortion: 默认40%, 0% ~ 100%
    effects_adjust_texture: 默认55%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%"""
    Blinking             = EffectMeta("Blinking", False, "7399469426078207238", "7399469426078207238", "6353300f8b3c913e3a1d60321fd2cc21", [
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    CD播放               = EffectMeta("CD播放", False, "7481555105532087558", "7481555105532087558", "830b6dd20ed09d54697bb93fd98c02e4", [])
    DV纹理               = EffectMeta("DV纹理", False, "7399471185815244037", "7399471185815244037", "65a1fb1567456e46d888a85f3efaa9a3", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    Doll                 = EffectMeta("Doll", False, "7298370919280561413", "7298370919280561413", "0663abd618ec2d473bb123ed5d6cc9a1", [])
    Flickery_Shots       = EffectMeta("Flickery Shots", False, "7399472470090157318", "7399472470090157318", "79ba3b0f0b1687e56a7514a0301e6af0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    Infrared_Lights      = EffectMeta("Infrared Lights", False, "7399469160071236869", "7399469160071236869", "04645a99412b56ada19400b5c65804c0", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    JVC                  = EffectMeta("JVC", False, "7399464976492023045", "7399464976492023045", "6060fe9faac1a35dd89c4362c57bd451", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%"""
    KTV灯光              = EffectMeta("KTV灯光", False, "7399467045676518661", "7399467045676518661", "ac75bc8cb54c6cf163065a31d4d6732b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    New_Year             = EffectMeta("New Year", False, "7399464845738888453", "7399464845738888453", "b3322fbbf99e1d4c9da1fb0b1e97d1a6", [
                              EffectParam("effects_adjust_size", 0.160, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.339, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认16%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    Shaky_Dolly          = EffectMeta("Shaky Dolly", False, "7399466115899870470", "7399466115899870470", "47b846ada207d95dce6bc0501102db85", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.220, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认22%, 0% ~ 100%"""
    Slit_Lighting        = EffectMeta("Slit Lighting", False, "7399468432799943941", "7399468432799943941", "8df52caeaddcd571a2b6bb325b7209ae", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%"""
    Spinning_Focus       = EffectMeta("Spinning Focus", False, "7399466076825799941", "7399466076825799941", "bfffafcc16a30af7d6faaf7816bd09cf", [
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Surreal              = EffectMeta("Surreal", False, "7347913743357037830", "7347913743357037830", "0db1b05e07d2eb3a38adeed4daa9515b", [])
    X_Signal             = EffectMeta("X-Signal", False, "7399464267428220166", "7399464267428220166", "ab9776213187c44b3c521b5a7ea6d1df", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _1998                = EffectMeta("1998", False, "7399466651126664454", "7399466651126664454", "d53096e8139dd33f7a2be6adcd7ce56b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    _3D动态照片          = EffectMeta("3D动态照片", False, "7298366024972324102", "7298366024972324102", "4289247a6b0c612eb45f12c0947f177d", [])
    _3D运镜              = EffectMeta("3D运镜", False, "7298366024972274950", "7298366024972274950", "585075b4beffbe2b580adbe12fdef188", [])
    _70s                 = EffectMeta("70s", False, "7399469779267964166", "7399469779267964166", "d1900db3d7ff04e7903d155114cab1d1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    kirakira             = EffectMeta("kirakira", False, "7399469087174233349", "7399469087174233349", "816803366dd866837e21380513b81e33", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认33%, 0% ~ 100%"""
    一键三连             = EffectMeta("一键三连 ", False, "7399467379165580549", "7399467379165580549", "240aa7d2cb97559978524678f84b6487", [])
    丁达尔光线           = EffectMeta("丁达尔光线", False, "7399468263731711237", "7399468263731711237", "858aa00b8938e4f0dde79225ef119f60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    万向镜像             = EffectMeta("万向镜像", False, "7417723109924409873", "7417723109924409873", "bf6fa505f4a9e6ebe3685196fa35e3e5", [
                              EffectParam("effects_adjust_rotate", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认12%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    万圣节快乐           = EffectMeta("万圣节快乐 ", False, "7399472034809466117", "7399472034809466117", "0b226c96ee570ed8c649d97f45879faa", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    下雨                 = EffectMeta("下雨", False, "7399469933865815301", "7399469933865815301", "40a59ce61692a825c049cd5b15bc6ded", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    不规则黑框           = EffectMeta("不规则黑框", False, "7399467547915013382", "7399467547915013382", "2457889e649132e1a427ccd9c258e51e", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    两屏分割             = EffectMeta("两屏分割", False, "7399471541601258758", "7399471541601258758", "2eba26aa15c0e44d2c258ce63a38d243", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认10%, 0% ~ 100%"""
    九屏                 = EffectMeta("九屏", False, "7399471604775832838", "7399471604775832838", "b9598da2197788df869a08ba617b58fd", [])
    五彩纸屑             = EffectMeta("五彩纸屑 ", False, "7399468218647170310", "7399468218647170310", "f0afbedd02a658dec54e2fb588cf8b69", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    五彩缤纷             = EffectMeta("五彩缤纷 ", False, "7399471468779670790", "7399471468779670790", "d12fa5eae2599adb73bade6dfa0bd34e", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    人鱼滤镜             = EffectMeta("人鱼滤镜", False, "7399470760227605765", "7399470760227605765", "f97bd68cfc43174bcb30406a6fc46952", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    仙女变身             = EffectMeta("仙女变身", False, "7399468681362803974", "7399468681362803974", "93b7e6f236713e3269b35a6534ca19d9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    仙尘闪闪             = EffectMeta("仙尘闪闪", False, "7399464427692625158", "7399464427692625158", "8b9da7f7b3cdd95bd73cc2444433017e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    低画质               = EffectMeta("低画质", False, "7395469544543816965", "7395469544543816965", "59142c1de4216f6883b4572f5a8d335a", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_sharpen: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    倒带                 = EffectMeta("倒带", False, "7399469142715272454", "7399469142715272454", "7eb38d3b30ae8e18748fcd3ed726aab2", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    倒计时_II            = EffectMeta("倒计时 II", False, "7399465816900783365", "7399465816900783365", "e01f6dadb794566d1ea3364d564f3f59", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    像素画               = EffectMeta("像素画", False, "7399467127159164166", "7399467127159164166", "0e6597e2bcbc35fe670bd05501ff37ed", [
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.755, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.688, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认76%, 0% ~ 100%
    effects_adjust_number: 默认69%, 0% ~ 100%
    effects_adjust_background_animation: 默认0%, 0% ~ 100%"""
    光晕                 = EffectMeta("光晕", False, "7399469248210275590", "7399469248210275590", "5dd6c29087b42206d70da0d13d4b7251", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    光晕_II              = EffectMeta("光晕 II", False, "7399464012418764037", "7399464012418764037", "63cf76363a869a8e0134f9dc6212957c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    光谱扫描             = EffectMeta("光谱扫描", False, "7399471534219250949", "7399471534219250949", "6d8fcac7a573c8ff756f131034946db5", [
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.614, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.642, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认61%, 0% ~ 100%
    effects_adjust_luminance: 默认64%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%"""
    入冬                 = EffectMeta("入冬 ", False, "7399470441850588422", "7399470441850588422", "8499da8c5ad5a2edc1f9566d5f066c00", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    全剧终               = EffectMeta("全剧终", False, "7399470808759815429", "7399470808759815429", "24749b428adbacfa9712b8a249912905", [])
    冰冷实验室           = EffectMeta("冰冷实验室 ", False, "7399470774723136774", "7399470774723136774", "0ba96868fd684b80b4cb82f058f35dc9", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.267, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认27%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    冲刺                 = EffectMeta("冲刺", False, "7399467232952143110", "7399467232952143110", "bac7325acc36e24c3af31df72d5ddaed", [])
    分屏涂鸦             = EffectMeta("分屏涂鸦", False, "7399464156782529798", "7399464156782529798", "87bf6e85345bb5b87f5d74b18be10805", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    动感模糊             = EffectMeta("动感模糊", False, "7399468627948440838", "7399468627948440838", "167deb8c5b35d5a3097cb107693c62c3", [
                              EffectParam("effects_adjust_horizontal_shift", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认85%, 0% ~ 100%"""
    动感色卡             = EffectMeta("动感色卡 ", False, "7399468056579247366", "7399468056579247366", "8ad3539910485cadfc27eb3f8853317e", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    单色涂鸦             = EffectMeta("单色涂鸦", False, "7398375723049798917", "7398375723049798917", "7647e2c7607c75922abb4cd232e83dff", [
                              EffectParam("effects_adjust_range", 0.760, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.360, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认76%, 0% ~ 100%
    effects_adjust_color: 默认36%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    南瓜光斑             = EffectMeta("南瓜光斑", False, "7399470074299452677", "7399470074299452677", "3626a4cba39f68ed0bbf43b58c023e07", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    南瓜笑脸             = EffectMeta("南瓜笑脸", False, "7399470071745121541", "7399470071745121541", "e28abcdb93864f4d4c1d340e9ce567a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    卡机                 = EffectMeta("卡机 ", False, "7399468171998055685", "7399468171998055685", "ea84ea931c93434b86263b92aabbadd4", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    发光                 = EffectMeta("发光", False, "7399472139515989254", "7399472139515989254", "5b7fdba4abb3d3b4fb5a3febe319e999", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认40%, 0% ~ 100%"""
    取景框_II            = EffectMeta("取景框 II", False, "7399468561376251142", "7399468561376251142", "a8af25fab9ceb2a477fb007d3dfc72b1", [])
    变彩色               = EffectMeta("变彩色", False, "7399471001949490438", "7399471001949490438", "0178a55e4f8c7deec8786d78d875d45e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    变清晰               = EffectMeta("变清晰", False, "7399471276215078150", "7399471276215078150", "feb43ab124f2c4bc8ee045a773741ed9", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认25%, 0% ~ 100%"""
    变焦推镜             = EffectMeta("变焦推镜", False, "7399468014107626757", "7399468014107626757", "1ef600710b33cc1e4d6f858c47e4b98a", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    变色锐化             = EffectMeta("变色锐化", False, "7399470774723022086", "7399470774723022086", "adce874b31124dad059e705d61e4032a", [
                              EffectParam("effects_adjust_sharpen", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认90%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认57%, 0% ~ 100%
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    变色闪光             = EffectMeta("变色闪光", False, "7399465314104151301", "7399465314104151301", "3f06e59c32f2e12dd4b63686844a0121", [
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认65%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%
    effects_adjust_blur: 默认85%, 0% ~ 100%"""
    告白氛围             = EffectMeta("告白氛围", False, "7399466294661139718", "7399466294661139718", "1c763cc141ab3041032ea9872dc22ea9", [])
    咔嚓                 = EffectMeta("咔嚓", False, "7399465246462676229", "7399465246462676229", "c742af6913646f7c936642aae51d58d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    噪点                 = EffectMeta("噪点", False, "7399470727122013446", "7399470727122013446", "3e5fc04a3ddff85aadb6b52681f00bcd", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    噪片映射             = EffectMeta("噪片映射", False, "7399471011801959686", "7399471011801959686", "e974f7b6381909e805e37d72c955ab1f", [
                              EffectParam("effects_adjust_noise", 0.343, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认34%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    四屏                 = EffectMeta("四屏", False, "7399467918615973125", "7399467918615973125", "5f86df016c27b44bf89d9634c4b1968a", [])
    回弹摇摆             = EffectMeta("回弹摇摆", False, "7399469592587832581", "7399469592587832581", "00cb18af745bc30702d78b9dae914465", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    圣诞日记             = EffectMeta("圣诞日记", False, "7399464537860181254", "7399464537860181254", "360c82d08c822cecb16e79b201768177", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认78%, 0% ~ 100%
    effects_adjust_filter: 默认10%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    圣诞星光             = EffectMeta("圣诞星光", False, "7399471084912807173", "7399471084912807173", "3e41badb29cc40f017f2ece636d26557", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    圣诞树               = EffectMeta("圣诞树", False, "7399470602496511237", "7399470602496511237", "abd3120d3e34fff00f916a70ccd45e54", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    地狱使者             = EffectMeta("地狱使者", False, "7399465530622512390", "7399465530622512390", "3ef0e7b7d8dd6ba3a7b20a893a17cf53", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    塑料封面_II          = EffectMeta("塑料封面 II", False, "7399470119199591685", "7399470119199591685", "0d08b6ff6fde15898e43468f99dc55de", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    塑料封面_III         = EffectMeta("塑料封面 III", False, "7399465854498327814", "7399465854498327814", "ee9f9dcd6d552a17fd93fdc8e1cc4a79", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    复古_DV              = EffectMeta("复古 DV", False, "7399470314947611909", "7399470314947611909", "19e1584168d4d3570a91185b8149ad03", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    复古发光             = EffectMeta("复古发光", False, "7399471416497736966", "7399471416497736966", "26589a4ec49ebd9e98088f4f952eb490", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%"""
    复古紫调             = EffectMeta("复古紫调", False, "7399469435964214533", "7399469435964214533", "eb8220e91369535e0cd5a471fd98b2a2", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.340, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.380, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.560, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认34%, 0% ~ 100%
    effects_adjust_sharpen: 默认38%, 0% ~ 100%
    effects_adjust_intensity: 默认26%, 0% ~ 100%
    effects_adjust_filter: 默认56%, 0% ~ 100%"""
    复古蓝调             = EffectMeta("复古蓝调", False, "7399472412791786757", "7399472412791786757", "971c462f47f17dd2827ad4fde77fc015", [
                              EffectParam("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认63%, 0% ~ 100%
    effects_adjust_blur: 默认35%, 0% ~ 100%
    effects_adjust_luminance: 默认63%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夜视仪               = EffectMeta("夜视仪", False, "7399465722574900485", "7399465722574900485", "8f50e2d05f748110d194a4e915912830", [])
    大雪                 = EffectMeta("大雪", False, "7399471559213174022", "7399471559213174022", "0ab2416c854073289f069711a36e82c1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    大雪纷飞             = EffectMeta("大雪纷飞", False, "7399471702746336517", "7399471702746336517", "84aa80de0bf14d5924dab46be29f7b5a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    天使光               = EffectMeta("天使光", False, "7399471617497156870", "7399471617497156870", "37c4098ac98fc25188a5a727064a7729", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    天使降临边框         = EffectMeta("天使降临边框", False, "7399464869172382982", "7399464869172382982", "0aee923ba4bd6cf0bcd62f036be00837", [])
    天啊                 = EffectMeta("天啊 ", False, "7399466287996472581", "7399466287996472581", "a6dcf93deb186e86f5a2288855c98d2a", [])
    失焦                 = EffectMeta("失焦", False, "7399464704118115590", "7399464704118115590", "bda93241b5c4690104b7b44862fb6040", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    定格闪烁             = EffectMeta("定格闪烁", False, "7399465660633386246", "7399465660633386246", "d3c2769c454f504272e2b5a1b96b5a61", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    宝丽莱_III           = EffectMeta("宝丽莱 III", False, "7399469045025737990", "7399469045025737990", "0397cc66371461e852276187a864caf3", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    小冬日               = EffectMeta("小冬日", False, "7399469756639726854", "7399469756639726854", "4c00bd23fd1c1697597a9298482314f2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    小圣诞               = EffectMeta("小圣诞", False, "7399470509722766598", "7399470509722766598", "6452c7efe85fb2af121d407974918c3a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    小彩虹               = EffectMeta("小彩虹", False, "7399465490659298565", "7399465490659298565", "137ff4df5d42ca851c52403a16e58ef0", [])
    屏幕律动             = EffectMeta("屏幕律动", False, "7399472023874931973", "7399472023874931973", "0736478f60e481067bdeadeb1c620e00", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    左右摇晃             = EffectMeta("左右摇晃", False, "7395465237777960198", "7395465237777960198", "e51ee36e6a6e41ce50c000956b9c71bf", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    幻彩文字             = EffectMeta("幻彩文字", False, "7399466192450161926", "7399466192450161926", "b985a3498d933a5e9d4620cc0aac4f7a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%"""
    幻影_II              = EffectMeta("幻影 II", False, "7399472218792529158", "7399472218792529158", "14e6364b3a6a1485f2583bdfc32b9f9a", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    幽灵漂浮             = EffectMeta("幽灵漂浮", False, "7399469453790006534", "7399469453790006534", "b678d12a5275aa28637557b455299c5c", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    广角                 = EffectMeta("广角", False, "7399467054375488773", "7399467054375488773", "17c3a4c4b6664d247c90a6e1bda8e6dd", [
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认45%, 0% ~ 100%"""
    开幕_I               = EffectMeta("开幕 I", False, "7399472638281649413", "7399472638281649413", "dc2ce1b151dd2e4dead3333902cb5afa", [])
    开幕_II              = EffectMeta("开幕 II", False, "7399470277530389765", "7399470277530389765", "be40f98619f47a8535158e873b273cce", [])
    弯曲故障             = EffectMeta("弯曲故障", False, "7405167267996044550", "7405167267996044550", "46b05fc90d596733bf661ec54a35c88c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.699, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认20%, 0% ~ 100%
    effects_adjust_texture: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认25%, 0% ~ 100%"""
    弹跳运镜             = EffectMeta("弹跳运镜", False, "7298366024972356870", "7298366024972356870", "1c1e53a5ed155f118cfe71a84e8b78da", [])
    强烈日光             = EffectMeta("强烈日光", False, "7530467303100534033", "7530467303100534033", "aaede06bf75bacc4655ca49e0096bf2d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    强锐化               = EffectMeta("强锐化", False, "7399467057764568326", "7399467057764568326", "c9ae5be2cd096747898e905fe2b6836b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认62%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    录制边框_III         = EffectMeta("录制边框 III", False, "7399468116423544070", "7399468116423544070", "bc759f18216aac435a0cf29b69bb5051", [])
    彩噪画质             = EffectMeta("彩噪画质", False, "7399471911815679237", "7399471911815679237", "fbdce889885763ee82ffa7138de4d36b", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认15%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认15%, 0% ~ 100%
    effects_adjust_sharpen: 默认35%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    彩色珠滴             = EffectMeta("彩色珠滴", False, "7399464627203067141", "7399464627203067141", "5a328a691ee44580205445581d96a679", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_background_animation: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认26%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    彩色电光             = EffectMeta("彩色电光", False, "7399464976492088581", "7399464976492088581", "4486aefcbd511057cafcdcbc13e4f057", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.680, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认68%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    彩色荧光             = EffectMeta("彩色荧光", False, "7399471143205211397", "7399471143205211397", "6a50bf39711faf7b7f94bf68fed7a33f", [])
    彩虹幻影             = EffectMeta("彩虹幻影", False, "7399467339302833414", "7399467339302833414", "a5f61f00265cbcf6fbc430780f5b4c03", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    彩虹水滴             = EffectMeta("彩虹水滴", False, "7399468659711724805", "7399468659711724805", "94de726c75d20dbe29314e02a1cfb903", [
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.602, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩虹电光             = EffectMeta("彩虹电光", False, "7395468419069529349", "7395468419069529349", "7a21f2671042a6e902620edf09a59093", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认12%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    彩钻                 = EffectMeta("彩钻", False, "7399466651126598918", "7399466651126598918", "a08b91114580a37c9e415aebd62e2b74", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    心跳                 = EffectMeta("心跳", False, "7399471312990702853", "7399471312990702853", "83aa305dcf2f6f4890efaca2546c4463", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    恐怖故事_III         = EffectMeta("恐怖故事 III", False, "7399468315476888837", "7399468315476888837", "472194dc4d5622347368fc59c753d827", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    截图放大镜           = EffectMeta("截图放大镜", False, "7399469878148664581", "7399469878148664581", "4c962a1294de796686ec24a81a63fe7e", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    抖动                 = EffectMeta("抖动", False, "7399465314104249605", "7399465314104249605", "950894d4ae28d859d9b7136a73265ee6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%"""
    抖动运镜             = EffectMeta("抖动运镜", False, "7298366024972373254", "7298366024972373254", "4d7cf3b3cd4bb77e29102d11a074eefd", [])
    摇摆_I               = EffectMeta("摇摆 I", False, "7399465143094103301", "7399465143094103301", "bb8e9483313416d32bea215d57855490", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    摇摆_II              = EffectMeta("摇摆 II", False, "7399466740012305669", "7399466740012305669", "332436443a8cbe9014d6bf7c8531ff60", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    撒星星_II            = EffectMeta("撒星星 II", False, "7399465816900799749", "7399465816900799749", "5c5349039a938e2348ae58a7dee34302", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    播放器               = EffectMeta("播放器", False, "7399469292892392709", "7399469292892392709", "187409b4bd22026b48df1bacdf2f3cfa", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    播放界面             = EffectMeta("播放界面", False, "7532323420499922193", "7532323420499922193", "b0a4d11ef076542c9c2c90d540ee7f92", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放映机抖动           = EffectMeta("放映机抖动", False, "7399471489407274246", "7399471489407274246", "3d7d53f809b52f7370380f358ef6081c", [
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认25%, 0% ~ 100%"""
    散光                 = EffectMeta("散光", False, "7399472616186055942", "7399472616186055942", "af6015fc0590a70892d5084082fd4490", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_range: 默认65%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_soft: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    斑斓                 = EffectMeta("斑斓", False, "7399466688342740229", "7399466688342740229", "9f8bb822ba38abb8db7f48aba67af7f5", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.040, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_number: 默认4%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    斜向模糊             = EffectMeta("斜向模糊", False, "7399468681362754822", "7399468681362754822", "03e0d6e34d341156533ec2c439f70b40", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认25%, 0% ~ 100%"""
    方形棱镜             = EffectMeta("方形棱镜 ", False, "7399471011797798150", "7399471011797798150", "3e52d9df4eee7090aea90817c62484b5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    无限穿越             = EffectMeta("无限穿越", False, "7298370919280545029", "7298370919280545029", "81d927e9568a07926b1bac21a922f888", [])
    星夜                 = EffectMeta("星夜", False, "7399471534219300101", "7399471534219300101", "1c75b4cf948ba65efeb1af5a25b41a7e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星星灯               = EffectMeta("星星灯", False, "7399468218647104774", "7399468218647104774", "9a20a02448ef8d95a81c3b16ca881742", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星月                 = EffectMeta("星月", False, "7399471024435268869", "7399471024435268869", "e64fb9cda4b4c83645be2ed819147c4b", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("sticker", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    sticker: 默认50%, 0% ~ 100%"""
    星河_II              = EffectMeta("星河 II", False, "7399469212877589766", "7399469212877589766", "2273947aec8664bd5c7a0f410c8bebfb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    星火                 = EffectMeta("星火", False, "7399468529818340613", "7399468529818340613", "e1f99bc44e7da14483e58a762a1bcbd2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星火_II              = EffectMeta("星火 II", False, "7399466570923248902", "7399466570923248902", "43a04949ebd13d27d7b38f5083882322", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星移                 = EffectMeta("星移", False, "7399470054053547270", "7399470054053547270", "f1c6583c2a7227b6ccf002863fdfdf65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星空                 = EffectMeta("星空", False, "7399470458866912518", "7399470458866912518", "cf7e2f2c81eba90828f32a9f0f99ef5e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星辰_I               = EffectMeta("星辰 I", False, "7399471800595303685", "7399471800595303685", "3c8c6e57ebbcca08e0202a2ce489a109", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    星辰_II              = EffectMeta("星辰 II", False, "7399469708560420102", "7399469708560420102", "4776e97efe2b615622586f9eba683b81", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    晴天光线             = EffectMeta("晴天光线", False, "7399465350317739270", "7399465350317739270", "a239820b1caf074292fe022c43353a85", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    暗夜                 = EffectMeta("暗夜", False, "7399471777350470917", "7399471777350470917", "17b5b34a9580eca1b093e3b9b730b5ad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    暗夜归来边框         = EffectMeta("暗夜归来边框", False, "7399463917145099526", "7399463917145099526", "6cae69adbcc67184a87c106dc6498de3", [])
    暗夜蝙蝠             = EffectMeta("暗夜蝙蝠", False, "7399471212943936774", "7399471212943936774", "bbe314aced3bb2ab605a2c7c6b0adf93", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    暗角                 = EffectMeta("暗角", False, "7399463239379209477", "7399463239379209477", "ef7abad9671e2f3da7993b7673ece5fc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    暗黑剪影             = EffectMeta("暗黑剪影", False, "7399470312338836741", "7399470312338836741", "e31ade9f9b38b5721fb601ad187bb163", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    暗黑蝙蝠             = EffectMeta("暗黑蝙蝠", False, "7399465620552666374", "7399465620552666374", "728d1a3d755122a887d8bd486416243f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认60%, 0% ~ 100%"""
    曝光降低             = EffectMeta("曝光降低", False, "7399466453944093957", "7399466453944093957", "be1c0676764ee83d32b63afc46272c28", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    条形光效             = EffectMeta("条形光效", False, "7531966204181826833", "7531966204181826833", "e43cdc29a37cc732166114d5a7be22d4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    柔光                 = EffectMeta("柔光", False, "7399467970071743749", "7399467970071743749", "258b5bd7ba1fb94dce800bc496a30ed9", [
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_soft: 默认70%, 0% ~ 100%"""
    梦境                 = EffectMeta("梦境", False, "7399471483837369606", "7399471483837369606", "361211e51fcca607a8ff03ed06f55826", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    梦境_III             = EffectMeta("梦境 III", False, "7399468898019593478", "7399468898019593478", "ae67e41be59533a1fa5de82ad641563a", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    梦境_IV              = EffectMeta("梦境 IV", False, "7399464110456507654", "7399464110456507654", "d5133f37d68785dbf342e95710116a39", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_soft: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    梦蝶                 = EffectMeta("梦蝶", False, "7399472432454569221", "7399472432454569221", "f6829a9af2cd1b32e1aac84543e0931b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    模糊                 = EffectMeta("模糊", False, "7399464929830423813", "7399464929830423813", "2db7bf49d9349e308ef0f46c39b14abf", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    模糊开幕             = EffectMeta("模糊开幕", False, "7399468886309162246", "7399468886309162246", "5dd4bf7e879fe7356e3e27e5105f5af1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认25%, 0% ~ 100%"""
    模糊星光             = EffectMeta("模糊星光", False, "7399466635947511046", "7399466635947511046", "81400757041b989a4f47ccdf417de1ea", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%"""
    横向闭幕             = EffectMeta("横向闭幕", False, "7399467149846121734", "7399467149846121734", "b7abe840af4f942b11e0ccda971d4df7", [])
    横纹故障_II          = EffectMeta("横纹故障 II", False, "7399465524997967110", "7399465524997967110", "83396b243328eacab9b423ebbb18f36b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    橘色负片             = EffectMeta("橘色负片", False, "7399472910978534662", "7399472910978534662", "95ddc63de88b65e1782c88c300c7e90e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    氛围边框             = EffectMeta("氛围边框", False, "7399466694239849734", "7399466694239849734", "bed13d336de9e335c6381dbd28a98c40", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.800),
                              EffectParam("effects_adjust_luminance", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 180%
    effects_adjust_luminance: 默认10%, 0% ~ 100%"""
    水波倒影             = EffectMeta("水波倒影", False, "7399469261418269957", "7399469261418269957", "d151e3575ce8eca803787e849b2ee7f4", [
                              EffectParam("effects_adjust_vertical_shift", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    水波纹               = EffectMeta("水波纹", False, "7399467020506483973", "7399467020506483973", "61ab10b10def92e31b0400ac87e43088", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%"""
    油画                 = EffectMeta("油画", False, "7298358335659642117", "7298358335659642117", "19f876ec6e9f85ebc76993ce66cebe20", [])
    油画纹理             = EffectMeta("油画纹理", False, "7399463847775554821", "7399463847775554821", "118b5e6a07a603581825a0fa8bb08e35", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    法式涂鸦             = EffectMeta("法式涂鸦", False, "7399470493742484741", "7399470493742484741", "77ce4a41e4d83f8fbaca4d954497fdff", [
                              EffectParam("effects_adjust_color", 0.610, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.661, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.720, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认61%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_texture: 默认66%, 0% ~ 100%
    effects_adjust_speed: 默认72%, 0% ~ 100%"""
    泛光爆闪             = EffectMeta("泛光爆闪", False, "7399465490659249413", "7399465490659249413", "7eeab42db5ca9a73186fe4f445b7613c", [
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    波浪丝印             = EffectMeta("波浪丝印", False, "7399470072797908229", "7399470072797908229", "b9dcf150237a8c60f3649c5e365a7fc6", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    波纹卡顿             = EffectMeta("波纹卡顿", False, "7473710408755319297", "7473710408755319297", "3217a5fc43a8a0af877ca1e12220603f", [
                              EffectParam("effects_adjust_distortion", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认33%, 0% ~ 100%"""
    波纹扭曲             = EffectMeta("波纹扭曲", False, "7399470005798063366", "7399470005798063366", "c0db14b731d4f04c95332348a0488089", [
                              EffectParam("effects_adjust_sharpen", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认35%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_distortion: 默认55%, 0% ~ 100%"""
    波纹抖动2            = EffectMeta("波纹抖动2", False, "7473710407337644545", "7473710407337644545", "c4a0883f975f9f935c12e62e43ef9c7b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    波纹抖动3            = EffectMeta("波纹抖动3", False, "7473710407333450257", "7473710407333450257", "2274d3a9b58ed12ac9a14cde2da41e60", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    波纹抖动             = EffectMeta("波纹抖动", False, "7473710407341838849", "7473710407341838849", "53a125c454b6e1a0b6ab2c2c093f1f5f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    浓雾                 = EffectMeta("浓雾", False, "7399469275754269957", "7399469275754269957", "102ee94c346f22275aec6e1077228b6b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    涂鸦日记_I           = EffectMeta("涂鸦日记 I", False, "7399465123708013829", "7399465123708013829", "cabba3df8d56e1a51369099de0ea9ec1", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    渐显开幕             = EffectMeta("渐显开幕", False, "7399469054718741765", "7399469054718741765", "a299b022ab4d7a1830ac72dce3d21d95", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    渐隐闭幕             = EffectMeta("渐隐闭幕", False, "7399468499044683013", "7399468499044683013", "05c17ac3298c0521cd91a720850a27de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    满屏问号             = EffectMeta("满屏问号", False, "7399465823011654918", "7399465823011654918", "168794f69f32cdb6011ebca4b5bf3382", [])
    火光                 = EffectMeta("火光", False, "7399470231229336838", "7399470231229336838", "fc346694609e66fccbc8cf5c171ac14d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    火光刷过             = EffectMeta("火光刷过", False, "7399469526443691270", "7399469526443691270", "2f79ecfe12481216bdcfd8ada5bb3afd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火光包围             = EffectMeta("火光包围", False, "7399466248272235782", "7399466248272235782", "a1aa2a5d030a3e96bc1f3fac839f5b24", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火光蔓延             = EffectMeta("火光蔓延", False, "7399466610827808005", "7399466610827808005", "253bf5ea7d03ec41b60c1837190350e2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火焰边框_I           = EffectMeta("火焰边框 I", False, "7399469048452369670", "7399469048452369670", "bd65acfadb0b7613c33100fa63abcf5e", [
                              EffectParam("effects_adjust_color", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认35%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%"""
    点赞                 = EffectMeta("点赞 ", False, "7399466044777155846", "7399466044777155846", "a927f8d9d6b8fcefd4671cb53455d8d5", [])
    烟花_III             = EffectMeta("烟花 III", False, "7399467830606875910", "7399467830606875910", "5d6d7516368c1dcdfb2bb274c2600416", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%"""
    爆炸                 = EffectMeta("爆炸", False, "7399469938068425990", "7399469938068425990", "b368d3f6335a5880ecc1c69c3d805cc3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    爱心Kira             = EffectMeta("爱心Kira", False, "7399470461379300614", "7399470461379300614", "74a62663b998596eb7f11485d8518b17", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    爱心光斑             = EffectMeta("爱心光斑", False, "7399466453944028421", "7399466453944028421", "58c897c26fa3df544d100541167c02b8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    爱心扫光             = EffectMeta("爱心扫光", False, "7399465043034656005", "7399465043034656005", "a80dca5cccc02be86ccb936a34fd736c", [
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_soft: 默认30%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    爱心投影             = EffectMeta("爱心投影", False, "7399468989082029317", "7399468989082029317", "24068e8b49b64d8802e7d62ca05acc07", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.435, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认44%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    爱心放射             = EffectMeta("爱心放射", False, "7399469700838591750", "7399469700838591750", "cbf62902df7101761116f28616cbbabc", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    爱心暗角             = EffectMeta("爱心暗角", False, "7399470760068254982", "7399470760068254982", "a41bc23f73e84416cd967ad89780dc94", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    爱心蝴蝶             = EffectMeta("爱心蝴蝶", False, "7399467244809358598", "7399467244809358598", "ad616b4657c4b98b75eb9019acaf2fdb", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    玻璃框选             = EffectMeta("玻璃框选", False, "7534564060835237137", "7534564060835237137", "896bf9509ef427014ffccd87363974d2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    玻璃边框             = EffectMeta("玻璃边框", False, "7399469147907689734", "7399469147907689734", "04c7efaeb9423d0214bffb26bb27ee60", [])
    琉璃拖影             = EffectMeta("琉璃拖影", False, "7399464812020813062", "7399464812020813062", "25ac2f9f90dae5ffb9155b73d984d9e4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    生日快乐             = EffectMeta("生日快乐", False, "7399470740849822982", "7399470740849822982", "7e2e3e9671c48ebdd4abf0f8efa0b3eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    电光包围             = EffectMeta("电光包围", False, "7399472028610301189", "7399472028610301189", "74c74b525f088396c37acc39c150da7b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    电光描边             = EffectMeta("电光描边", False, "7399471232170609925", "7399471232170609925", "15153b69c032c89f4087d12ef7a613ca", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%"""
    电光漩涡             = EffectMeta("电光漩涡", False, "7399468933562027270", "7399468933562027270", "ae1cdd841a45a6ca3ec36479b72f4182", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    电影感               = EffectMeta("电影感", False, "7399470065093152005", "7399470065093152005", "20175443ac3ff3f77c48019889186568", [])
    电视关机             = EffectMeta("电视关机", False, "7399465210030853382", "7399465210030853382", "c2ef989d8286f4b2e5a747bca129602a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认60%, 0% ~ 100%"""
    电视开机             = EffectMeta("电视开机", False, "7399470472959675654", "7399470472959675654", "b7f303766220a86078204b79a4db2566", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认60%, 0% ~ 100%"""
    电视纹理             = EffectMeta("电视纹理", False, "7399471480423107845", "7399471480423107845", "fbf351dd37a0d60885414e3157f838d9", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%"""
    画展边框             = EffectMeta("画展边框", False, "7399469589618347269", "7399469589618347269", "594fd22d6effa8153b7a619746b1dd0f", [])
    白色光波             = EffectMeta("白色光波", False, "7473710407333499393", "7473710407333499393", "d7c04ac964258cbaeeb82eaee137819a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    百叶窗_I             = EffectMeta("百叶窗 I", False, "7399464929830472965", "7399464929830472965", "bde8d2cb9d033a45c92615f9b18b47a1", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    相册_II              = EffectMeta("相册 II", False, "7399468458611625221", "7399468458611625221", "63b2bb486ee485a221c37961f5dea9ab", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    相片定格             = EffectMeta("相片定格", False, "7399468164804807941", "7399468164804807941", "a58e3178d3a498edac53074a3c3a7542", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认85%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    破冰                 = EffectMeta("破冰", False, "7399465112005856518", "7399465112005856518", "35814c493387bfc7af1eadf958e28d71", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    磨砂纹理             = EffectMeta("磨砂纹理", False, "7399467202413481222", "7399467202413481222", "3acc0bd2b4264cbf508bd2aa2e4c07dd", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    竖向闪光             = EffectMeta("竖向闪光", False, "7399472112223702278", "7399472112223702278", "7529d488cc18a6fb4a7e58c4ef3af378", [
                              EffectParam("effects_adjust_number", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.690, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认69%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    简约边框             = EffectMeta("简约边框", False, "7399467143697272069", "7399467143697272069", "a130a890772cc684fc987dcf2ec22124", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    粉色轻曝             = EffectMeta("粉色轻曝", False, "7529380429703449857", "7529380429703449857", "3c2358e499cae980fedfc937127ce8ad", [
                              EffectParam("effects_adjust_filter", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认10%, 0% ~ 100%"""
    粒子消散1            = EffectMeta("粒子消散1", False, "7298373731326676230", "7298373731326676230", "15628a5d158555acad8d69629992a0c6", [])
    粒子消散2            = EffectMeta("粒子消散2", False, "7298376175456357638", "7298376175456357638", "c78f05c23056dc80075ff323b84cabeb", [])
    精细锐化             = EffectMeta("精细锐化", False, "7399464661671775493", "7399464661671775493", "df34b01300ddefbfd8b04bee900ae432", [
                              EffectParam("effects_adjust_blur", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认12%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认8%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    紫光夜               = EffectMeta("紫光夜", False, "7395474150267030790", "7395474150267030790", "1a4c76312950f09d8fd14e68de775bd8", [
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    紫橘渐变             = EffectMeta("紫橘渐变", False, "7399469125124230406", "7399469125124230406", "37d67e5b34f923a72bb3991b01c680bd", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    纵向开幕             = EffectMeta("纵向开幕", False, "7399469048678960389", "7399469048678960389", "d75e138469226782f6d918983725d700", [])
    纵向模糊             = EffectMeta("纵向模糊", False, "7399470405741776133", "7399470405741776133", "301f4e40cf408cb323fca377af84f18e", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    细闪                 = EffectMeta("细闪", False, "7399467222843919622", "7399467222843919622", "9f35060cd9e36abab8c5ebb80d8efbf6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    细闪_II              = EffectMeta("细闪 II", False, "7399468209327394053", "7399468209327394053", "186c623a413a10ddbf28bfa0215a55f4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    网点丝印             = EffectMeta("网点丝印", False, "7399468802095795462", "7399468802095795462", "87e58ba33f7dc96c4e108cd67c67e2a4", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    羽毛                 = EffectMeta("羽毛", False, "7399469586913004806", "7399469586913004806", "2627845c8cff5d5bd99c36aa20f57a11", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    老照片               = EffectMeta("老照片", False, "7399470393884478725", "7399470393884478725", "473d207c1d0228446726704f0a54bea6", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    老电影_II            = EffectMeta("老电影 II", False, "7399469372986739974", "7399469372986739974", "62b508cb16fd1c0da7a2989da5bd49fd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    老电视卡顿           = EffectMeta("老电视卡顿", False, "7399467801653677317", "7399467801653677317", "47c83f6d6073edb2fee0f2d7ee0599a6", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    背景旋转             = EffectMeta("背景旋转", False, "7399470493742451973", "7399470493742451973", "4d06bd63f1081afc85f5c62833f64ee0", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认15%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%"""
    胶片                 = EffectMeta("胶片", False, "7399470602496658693", "7399470602496658693", "c85a5c6d8841e2e6dd65813cbe60505c", [
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    胶片框               = EffectMeta("胶片框", False, "7399464865909198086", "7399464865909198086", "d5f6e3f656074eaaaad12544b43dee93", [])
    胶片漏光             = EffectMeta("胶片漏光", False, "7399472317929245957", "7399472317929245957", "97fea18d6a469abd49e3f1d28628e61f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    胶片漏光_II          = EffectMeta("胶片漏光 II", False, "7399466219721608453", "7399466219721608453", "7b4f9381351d3e703cd06e95ab3a9b06", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    脉搏跳动             = EffectMeta("脉搏跳动", False, "7399465853118369030", "7399465853118369030", "c65fc5a267dde559e80e16c8fcc9cd6c", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%"""
    自然_II              = EffectMeta("自然 II", False, "7399465350313610501", "7399465350313610501", "7196a6d5e3b895f781a453e70abb971a", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    自然_III             = EffectMeta("自然 III", False, "7399466639261060358", "7399466639261060358", "6d80537f452debf98b09f2df79080e37", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    自然_IV              = EffectMeta("自然 IV", False, "7399472218792561926", "7399472218792561926", "264fbe6c96d9027b99cd066cad7adc1b", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    自然_V               = EffectMeta("自然 V", False, "7399469735873727750", "7399469735873727750", "6ff4d109673eb689778b2be2f5af1c3e", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    色差                 = EffectMeta("色差", False, "7399464427692526854", "7399464427692526854", "737c54ea0dcf628cc78714a77eef52a3", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    色差放大             = EffectMeta("色差放大", False, "7399470441850555654", "7399470441850555654", "91376f7887165bb15a4e149dc9be9d9b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    色差放射             = EffectMeta("色差放射", False, "7399470160203107589", "7399470160203107589", "53c8584c8174f887b2802540dd28955b", [
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认25%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认55%, 0% ~ 100%"""
    色差故障_II          = EffectMeta("色差故障 II", False, "7399464110456491270", "7399464110456491270", "c50d8f72262989088d0bc3c9eba4fe17", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    色差星闪             = EffectMeta("色差星闪", False, "7399468304080882949", "7399468304080882949", "a733e6809686e0ef344eccbf8feb6f54", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%"""
    节奏热成像           = EffectMeta("节奏热成像", False, "7416640327664013825", "7416640327664013825", "a56e9c4eb9b81ab28f6eb68e8a3afef0", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%"""
    花火                 = EffectMeta("花火", False, "7399470980713909509", "7399470980713909509", "7eed03f0203ac3c7dad4a60b433b8af3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    花瓣飘落             = EffectMeta("花瓣飘落", False, "7399464130664500486", "7399464130664500486", "a772c059e7fb8304292e7ebb870e8eb3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    花瓣飞扬             = EffectMeta("花瓣飞扬", False, "7399465350317739269", "7399465350317739269", "24c3c52fe9d54c8677ee514c0530528c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    荧光爱心             = EffectMeta("荧光爱心", False, "7399470030942981382", "7399470030942981382", "b9b9be20aed7761f81c6757a4428a034", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    荧光线描             = EffectMeta("荧光线描", False, "7399471609624481029", "7399471609624481029", "238fbd22ccb939c0b2198e9a6170962d", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    荧光蝙蝠             = EffectMeta("荧光蝙蝠", False, "7399465660633337094", "7399465660633337094", "ad61d53ca404616d198bc766e6c64df8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    荧幕噪点             = EffectMeta("荧幕噪点", False, "7399470295117073670", "7399470295117073670", "f090492c306fe35f917eed1216f14f8c", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    荧幕噪点_II          = EffectMeta("荧幕噪点 II", False, "7399469641170554117", "7399469641170554117", "53ff3188476c74715a73aa34f08a1edf", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    菱形变焦             = EffectMeta("菱形变焦", False, "7399471460445605125", "7399471460445605125", "fda851ab65ee2b7bd6bb568a0e8bc544", [
                              EffectParam("effects_adjust_size", 0.521, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认52%, 0% ~ 100%
    effects_adjust_intensity: 默认72%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%"""
    萤光                 = EffectMeta("萤光", False, "7399465395402411270", "7399465395402411270", "66a4a10a45c3c0b472f5c934c0de1681", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    萤火                 = EffectMeta("萤火", False, "7399468742276599046", "7399468742276599046", "811f6c870c1f8f0fc61dd6adc40c71c7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    落樱                 = EffectMeta("落樱", False, "7399470244357573893", "7399470244357573893", "7372d9708980266944aec9650ccde843", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    蒸汽腾腾             = EffectMeta("蒸汽腾腾", False, "7399466403327151366", "7399466403327151366", "f852e42917f0ea29be56bbb12891c920", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    蓝光爆闪             = EffectMeta("蓝光爆闪", False, "7399467531599170822", "7399467531599170822", "363de1da61a76d9d902e62a7bed611e6", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.650, 0.010, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认65%, 1% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%"""
    蓝色丝印             = EffectMeta("蓝色丝印", False, "7399472736231312646", "7399472736231312646", "0fceb871b844d51454db5d59da3636ef", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝色负片             = EffectMeta("蓝色负片", False, "7399467960076733701", "7399467960076733701", "c40c9ca0a5c2ea1a22c54a3dc943b3de", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    蓝调Kira             = EffectMeta("蓝调Kira", False, "7399465516982603013", "7399465516982603013", "87d59093e22181ec9a002a25da3c3b1b", [
                              EffectParam("effects_adjust_number", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    虚化                 = EffectMeta("虚化", False, "7399470097007414534", "7399470097007414534", "d022f68235da2c057cb3aa2495fb249c", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    蝙蝠kira             = EffectMeta("蝙蝠kira", False, "7399466823139314950", "7399466823139314950", "408ee7831b71cbae827138898d26c934", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    裸眼3D               = EffectMeta("裸眼3D", False, "7298370919280413957", "7298370919280413957", "1920b534e5850c85343a0b33f80115e1", [])
    负片闪烁             = EffectMeta("负片闪烁", False, "7399471841720503557", "7399471841720503557", "ed476f61f551e99709b62ce8ed922323", [
                              EffectParam("effects_adjust_speed", 0.560, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认56%, 0% ~ 100%"""
    负片闪频_II          = EffectMeta("负片闪频 II", False, "7418091500640145936", "7418091500640145936", "037aa3ce6e5b17d6623bf2d718104ac4", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    赛博未来             = EffectMeta("赛博未来", False, "7298370919280495877", "7298370919280495877", "d3bb25d0d8e34e5ddd6728e546494743", [])
    超级喜欢             = EffectMeta("超级喜欢", False, "7399466296666098950", "7399466296666098950", "39e3a29514be39477d164786fb4b3dd0", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    蹦迪光               = EffectMeta("蹦迪光", False, "7399470084449684742", "7399470084449684742", "c5bed1ab7aee34bfb9b3c6ab3705eb28", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    轻微抖动             = EffectMeta("轻微抖动", False, "7399466773713833222", "7399466773713833222", "7cb6c1646c43d86a394245e194e3f451", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认15%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    轻微放大             = EffectMeta("轻微放大", False, "7399463624906984709", "7399463624906984709", "c09004507723569a3e762494d4ffda7d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    边缘发光             = EffectMeta("边缘发光", False, "7399466236188298501", "7399466236188298501", "9768e7f5b5d8c89e82cf4ebd80768263", [
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认25%, 0% ~ 100%"""
    迷雾                 = EffectMeta("迷雾", False, "7399468230848318725", "7399468230848318725", "057c2404619359f8ceec96e20eee0f2f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    重复变焦             = EffectMeta("重复变焦", False, "7399467732749585670", "7399467732749585670", "a8a9919a707cecf6f5f2eb1fa5d0d959", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    金片_II              = EffectMeta("金片 II", False, "7399470420547652870", "7399470420547652870", "3100003d53722ae2d1e8ca0bde4a1043", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金粉                 = EffectMeta("金粉", False, "7399469925556833541", "7399469925556833541", "a7078ce916e55b0663390bcef1a5ff1e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金粉旋转             = EffectMeta("金粉旋转", False, "7399470812975172870", "7399470812975172870", "14fd0f24372acd5be33505ee5759ca11", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金粉闪闪             = EffectMeta("金粉闪闪", False, "7399471312990637317", "7399471312990637317", "a552dfa820b5aba27e4f09e3d83b8643", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金色亮片             = EffectMeta("金色亮片", False, "7399469667942763781", "7399469667942763781", "767cd468f9dc8d01d3e14fa10fc9b1f4", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    镜像                 = EffectMeta("镜像", False, "7399472757014007046", "7399472757014007046", "0e68989382af0ece7e1e864cc2107c67", [])
    镜像三格             = EffectMeta("镜像三格", False, "7399467129646501125", "7399467129646501125", "26e730a32387f88e9a67c4e8213d9920", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    镜头变焦             = EffectMeta("镜头变焦", False, "7399465441057328389", "7399465441057328389", "6f7b76eec49d46f9397eafb4980a17d4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 100%"""
    镭射边界             = EffectMeta("镭射边界", False, "7399472218792643846", "7399472218792643846", "bfb7e1244b2c158ad9ebb311c33e6463", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    闪光灯               = EffectMeta("闪光灯", False, "7399470959012498694", "7399470959012498694", "c602afac7537de506bb822c37e9f2191", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪屏                 = EffectMeta("闪屏", False, "7399472497780886790", "7399472497780886790", "51b2af1e78502e00abb3d47b21a55796", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    闪电                 = EffectMeta("闪电", False, "7399472765503278342", "7399472765503278342", "5a3581b92b7e459306a2be1e262b8bc7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    闪白                 = EffectMeta("闪白", False, "7399465317946264838", "7399465317946264838", "f0804cb2cb4e88a036ecf87dcf031cf0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪黑                 = EffectMeta("闪黑", False, "7399465518215941382", "7399465518215941382", "383b8ace93434f0c5d17689933140422", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪黑_II              = EffectMeta("闪黑 II", False, "7395474043438157062", "7395474043438157062", "3c25ccac35121fe42e647b119e37a21f", [
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_distortion: 默认40%, 0% ~ 100%"""
    闭幕                 = EffectMeta("闭幕", False, "7399468185046584581", "7399468185046584581", "93a3a5fbe5f3b343667f7affe22b97f9", [])
    闭幕_II              = EffectMeta("闭幕 II", False, "7399470472934526213", "7399470472934526213", "5653f70097408fcbcbe82af864d70b13", [])
    随机单色             = EffectMeta("随机单色", False, "7399471259907624198", "7399471259907624198", "3248139fce7804b507bf3790d9e0f753", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认75%, 0% ~ 100%"""
    随机闪切             = EffectMeta("随机闪切", False, "7399468315476774149", "7399468315476774149", "6a5fa04981e50a2c7bd67a4e03e4d3e6", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认20%, 0% ~ 100%"""
    随机马赛克           = EffectMeta("随机马赛克", False, "7399466502296014085", "7399466502296014085", "f7941de515b8f54194e836aff7e2deef", [
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_number: 默认22%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%
    effects_adjust_background_animation: 默认90%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    隐形人               = EffectMeta("隐形人 ", False, "7399469636405759238", "7399469636405759238", "2cf16035b605ce73f4b44bcd650adfb3", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认35%, 0% ~ 100%"""
    隔行扫描             = EffectMeta("隔行扫描", False, "7399470906407521542", "7399470906407521542", "e8349feb07866b44bbce9c9effa6f51a", [
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    雪花故障_I           = EffectMeta("雪花故障 I", False, "7399464937136950534", "7399464937136950534", "dad8ca94e3468a61bcc0e15b0e8c8dba", [
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认15%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认55%, 0% ~ 100%"""
    雪花细闪             = EffectMeta("雪花细闪", False, "7399465653700152582", "7399465653700152582", "5b1de91c85371d33e408df6eb164e1f8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    零点解锁             = EffectMeta("零点解锁", False, "7399466639260945670", "7399466639260945670", "e3628803155db5b9d465c9fbf5db249d", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    震动                 = EffectMeta("震动", False, "7399470393884527877", "7399470393884527877", "d11532bfbfbd6f9af59026c2c42f2570", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    震动发光             = EffectMeta("震动发光", False, "7399470511383710982", "7399470511383710982", "ce4e35169cec8e19b726e34e22eb0ffa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_soft: 默认60%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    霓虹光线             = EffectMeta("霓虹光线", False, "7399467959585885445", "7399467959585885445", "c2274095125803b495db0623740fcb22", [
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认45%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, 0% ~ 100%"""
    霓虹碎片             = EffectMeta("霓虹碎片", False, "7298373731326659846", "7298373731326659846", "7250c3027891d35c1ab66921cae70ae4", [])
    预警                 = EffectMeta("预警", False, "7399465244088618245", "7399465244088618245", "67ed6a4031987dbc9d980102b1faabf7", [])
    飘雪                 = EffectMeta("飘雪", False, "7399466442321612038", "7399466442321612038", "89b03a201271314608b58590dd0db188", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    飘雪_II              = EffectMeta("飘雪 II", False, "7399470840556932357", "7399470840556932357", "d11b0590308cd9e1222de5fd408c95e4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    飞速计算             = EffectMeta("飞速计算", False, "7399467244150885637", "7399467244150885637", "b08f9e05c86b2e980444d336d9db7427", [])
    马赛克               = EffectMeta("马赛克", False, "7399471143205244165", "7399471143205244165", "c9f3bf5b93d53bdc514be0d9c480fcf0", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    马赛克闪切           = EffectMeta("马赛克闪切", False, "7395472581324803334", "7395472581324803334", "6b0566a1868f7a088935c8835052db63", [
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.130, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认13%, 0% ~ 100%"""
    魔法变身             = EffectMeta("魔法变身", False, "7399471517320482054", "7399471517320482054", "d64c2ea963352c88d836778ebe93b347", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    魔法甜心             = EffectMeta("魔法甜心", False, "7399472755680464133", "7399472755680464133", "e1d9a7736e1b5e8d67f3a670b42235fb", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    鱼眼                 = EffectMeta("鱼眼", False, "7399466881364544773", "7399466881364544773", "d577e4744d29d971675ec9c71d94ca94", [
                              EffectParam("effects_adjust_distortion", 0.770, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认77%, 0% ~ 100%"""
    黄边噪片             = EffectMeta("黄边噪片 ", False, "7399472030828989701", "7399472030828989701", "777f6152f5b944918f20f487c148b750", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.320, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认32%, 0% ~ 100%"""
    黑白VHS              = EffectMeta("黑白VHS", False, "7399465644150000902", "7399465644150000902", "1a53630780dee01e236cff7233d35d01", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.530, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.430, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认53%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认43%, 0% ~ 100%"""
    黑白漫画             = EffectMeta("黑白漫画", False, "7399471674162367750", "7399471674162367750", "cb444409524d6b0f809c227a0fe31a9d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    黑白漫画_II          = EffectMeta("黑白漫画 II", False, "7399463691348888838", "7399463691348888838", "4de87320cab95ca35205388e919f6725", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑白线描             = EffectMeta("黑白线描", False, "7399470748277984517", "7399470748277984517", "7f913d28b2a6a7c9f2e2135a54cd78f2", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    黑白胶片             = EffectMeta("黑白胶片", False, "7399464367420493062", "7399464367420493062", "708a2e34f1ecf5774e910d8da7099304", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    黑羽毛_II            = EffectMeta("黑羽毛 II", False, "7399470654237576454", "7399470654237576454", "932dd2876d21de60a54af16a22c9818f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    黑色噪点             = EffectMeta("黑色噪点", False, "7399470796290166022", "7399470796290166022", "e7baebcf969437d4d5cdb607578bbf89", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""

    # 付费特效
    AD_Lens              = EffectMeta("AD Lens", True, "7439647267230847489", "7439647267230847489", "6003cb85205bfa86f67ffa3a7e8a8b6d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    B_W_Frame            = EffectMeta("B&W Frame", True, "7438462583469773329", "7438462583469773329", "2e09d555c348a0208d7ea1d7fe2afb67", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    B_W_电气             = EffectMeta("B&W 电气", True, "7498206555259637045", "7498206555259637045", "ff048447da90f8ad5972a0a7669fab7c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    Back_to_Focus        = EffectMeta("Back to Focus", True, "7395470517353942278", "7395470517353942278", "56400fdaa42b7f909659941e485b7cf4", [
                              EffectParam("effects_adjust_speed", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认66%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    Bling飘落            = EffectMeta("Bling飘落", True, "7399464571406224645", "7399464571406224645", "5425c855f5395166464034278b51afc2", [
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.450, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认15%, 0% ~ 100%
    effects_adjust_number: 默认45%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认45%, 0% ~ 100%"""
    Bouncing_Glow        = EffectMeta("Bouncing Glow", True, "7399470119199526149", "7399470119199526149", "1d1f9cc33d051f8c2942cbc86de9f6dd", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%"""
    Butterfly            = EffectMeta("Butterfly", True, "7399465823011753222", "7399465823011753222", "efec4ce01955d7883ca44294238f7515", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    CCD                  = EffectMeta("CCD", True, "7399468001512164614", "7399468001512164614", "a65d0dc07fa4d72485339880a4203b8f", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    sticker: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认10%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认10%, 0% ~ 100%"""
    CD                   = EffectMeta("CD", True, "7399466672702115078", "7399466672702115078", "63ae4f0e3162bf407a882a3f8578bfc9", [
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认8%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%"""
    CTR屏幕              = EffectMeta("CTR屏幕", True, "7528671478821195069", "7528671478821195069", "8c2cdb33dadb778c20bdf6c0a6e7e334", [
                              EffectParam("effects_adjust_filter", 1.002, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.520, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.650, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认52%, 0% ~ 100%
    effects_adjust_noise: 默认65%, 0% ~ 100%"""
    Camera_Beats         = EffectMeta("Camera Beats", True, "7399471617497206022", "7399471617497206022", "81bb946b8dfe47610a322d7f2d2496d9", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 200%
    effects_adjust_background_animation: 默认100%, 0% ~ 200%
    effects_adjust_luminance: 默认100%, 0% ~ 200%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Camera_Beats_2       = EffectMeta("Camera Beats 2", True, "7399471232170691845", "7399471232170691845", "5b71a4a5390f261a4e400c0dd2e31d0f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    Camera_Dance         = EffectMeta("Camera Dance", True, "7395474395025673478", "7395474395025673478", "f482dc307814b8b0697bbf9aa678b5e8", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    Chrome_Disco         = EffectMeta("Chrome Disco", True, "7527664096817253685", "7527664096817253685", "b08f9df7be385f6729ba27f19abb2cf2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    Close_Up             = EffectMeta("Close Up", True, "7405165803638934790", "7405165803638934790", "fb068afb4095572e738a13599a8a95f6", [
                              EffectParam("effects_adjust_speed", 0.318, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认32%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认78%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    Curvy_Blur           = EffectMeta("Curvy Blur", True, "7395470068928318726", "7395470068928318726", "2b3df5d27980949f8aee378b54f8cf38", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.366, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.425, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认37%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认42%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    DJ旋转               = EffectMeta("DJ旋转", True, "7510143687029034301", "7510143687029034301", "3cac446971c6c8aaea3dea5fe2fc91d5", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    DVD                  = EffectMeta("DVD", True, "7399464677408853253", "7399464677408853253", "a00c3045f162ade57c95eca2f241e079", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    DVD光盘框            = EffectMeta("DVD光盘框", True, "7399468872413334790", "7399468872413334790", "cfff37d85d05957ae0dfe1690fd088e9", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_noise: 默认15%, 0% ~ 100%
    effects_adjust_blur: 默认15%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    DV录制框             = EffectMeta("DV录制框", True, "7399466721725271301", "7399466721725271301", "fec95d8bc6cffc1d8fdad2b2685fab74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认20%, 0% ~ 100%"""
    Defrost              = EffectMeta("Defrost", True, "7449637236129141264", "7449637236129141264", "9f0f6762870860ab5b6ce49c580ffe9d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Diamond_Halo         = EffectMeta("Diamond Halo", True, "7395471598351961349", "7395471598351961349", "8baa04aecc7a8e40d9c71cb3c7a91f33", [
                              EffectParam("effects_adjust_filter", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.230, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认55%, 0% ~ 100%
    effects_adjust_range: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认23%, 0% ~ 100%
    effects_adjust_blur: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认75%, 0% ~ 100%"""
    Dolly_Back           = EffectMeta("Dolly Back", True, "7395468892388265221", "7395468892388265221", "5e3de3ba75f157a19687d84df4545bb0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%"""
    Dreamy_Halo          = EffectMeta("Dreamy Halo", True, "7399470472959773958", "7399470472959773958", "13e344af2899a8f53510969abcca85f2", [
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 2.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.500)])
    """参数:
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_range: 默认65%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_sharpen: 默认30%, 0% ~ 200%
    effects_adjust_blur: 默认20%, 0% ~ 150%"""
    Dripping_Blood       = EffectMeta("Dripping Blood", True, "7426951752663962128", "7426951752663962128", "0f9e6e2ca254ea99776f80dcb6b22f7d", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    Fisheye_Shine        = EffectMeta("Fisheye Shine", True, "7438462585222992401", "7438462585222992401", "9653ef598f10bfa680a4101317029663", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Fisheye_Spark        = EffectMeta("Fisheye Spark", True, "7438462583746597393", "7438462583746597393", "46b23446c66aa5fc8f91bc468724eeed", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Flash                = EffectMeta("Flash", True, "7399470564022291717", "7399470564022291717", "e92f5749fec01ea61ad9d6747d808f82", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认65%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    Flash_Light          = EffectMeta("Flash Light", True, "7395475049672609029", "7395475049672609029", "1b75db7dff420e3421c264bab304e5fb", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.270, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认75%, 0% ~ 100%
    effects_adjust_color: 默认27%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%"""
    Floating_Hearts      = EffectMeta("Floating Hearts", True, "7399466602967698694", "7399466602967698694", "2a84ea537b525994b2803d6a538960e1", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Focus_Shake          = EffectMeta("Focus Shake", True, "7399466143666212102", "7399466143666212102", "a36edfb925cbfa69a86a5bdd53f7237f", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Free_Focus           = EffectMeta("Free Focus", True, "7438462581452329473", "7438462581452329473", "d648bf579b3f003ca76c46068faadd70", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Ghosting             = EffectMeta("Ghosting", True, "7399464280061480197", "7399464280061480197", "f01002b2853ba8736b02ee943e132421", [
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_soft: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Glamor_Shots         = EffectMeta("Glamor Shots", True, "7504490082158546192", "7504490082158546192", "f7deaf6bef3c470008d059895ace7689", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Glitch_Intro         = EffectMeta("Glitch Intro", True, "7395471804006927621", "7395471804006927621", "cca147e79ccb7aa484b6821337782afb", [
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    HDR                  = EffectMeta("HDR", True, "7399464703925177606", "7399464703925177606", "bf30d65645d40d1a48a54e8bfdbfdf5d", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.230, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_number: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认23%, 0% ~ 100%"""
    Horror_画面          = EffectMeta("Horror 画面", True, "7519886085971791157", "7519886085971791157", "7018f015cdcec47da9d966a8b2b1fdb1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Ins描边              = EffectMeta("Ins描边", True, "7399464326702288133", "7399464326702288133", "c073d6636702e58d2db4d563a91f76a5", [
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.460, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_number: 默认46%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%"""
    Jackpot_Spin         = EffectMeta("Jackpot Spin", True, "7501595753505230133", "7501595753505230133", "a1bfafdb8e798a05915189087fa8d619", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    KIRA泡泡             = EffectMeta("KIRA泡泡", True, "7399466248272104710", "7399466248272104710", "618b19931987ad05f528edc3a307322f", [
                              EffectParam("effects_adjust_luminance", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认25%, 0% ~ 100%
    effects_adjust_soft: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%"""
    Lightflow_Scan       = EffectMeta("Lightflow Scan", True, "7395473269148699910", "7395473269148699910", "79582fc0a97afe1fcd4fb0199d07bc7d", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认66%, 0% ~ 100%"""
    Lightning_Twist      = EffectMeta("Lightning Twist", True, "7399449921776045318", "7399449921776045318", "86f6a7e75465c86d33144c98ab71c4dc", [
                              EffectParam("effects_adjust_luminance", 0.666, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认67%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    MV封面               = EffectMeta("MV封面", True, "7399463706603621637", "7399463706603621637", "658b5a2a87b51d71f8f968546790257a", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Move_Track           = EffectMeta("Move Track", True, "7399465771090398469", "7399465771090398469", "661a5b5dea5a090ef8d29f55d28e10c5", [
                              EffectParam("effects_adjust_speed", 55.000, 0.000, 100.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.980, 0.000, 1.000),
                              EffectParam("sticker", 0.240, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认5500%, 0% ~ 10000%
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认98%, 0% ~ 100%
    sticker: 默认24%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_texture: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%"""
    Neon_Flash           = EffectMeta("Neon Flash", True, "7399468051688738053", "7399468051688738053", "32ab9ae1b2f18168bb5d78bfdfda9176", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.825, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认82%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认100%, 0% ~ 100%"""
    Night_Snow           = EffectMeta("Night Snow", True, "7399472543192698118", "7399472543192698118", "e7ffbde00a94433fe9f2b9060fd1170f", [
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.100, 0.000, 1.000),
                              EffectParam("sticker", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认10%, 0% ~ 100%
    sticker: 默认60%, 0% ~ 100%"""
    OH                   = EffectMeta("OH ", True, "7399467897246010630", "7399467897246010630", "1b04f7dbc3f688a842123f4e596ce775", [])
    Old_Footage          = EffectMeta("Old Footage", True, "7395468919198321926", "7395468919198321926", "344d23dd983b3552a11d6d15801692aa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    PS2游戏              = EffectMeta("PS2游戏", True, "7460012201659616518", "7460012201659616518", "0294372ea81021e0135b49981e77dd66", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    Passion              = EffectMeta("Passion", True, "7433259001162240528", "7433259001162240528", "2c1f3566c8ff77f26376e2ab562ad200", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    Pixel_Glitch         = EffectMeta("Pixel Glitch", True, "7399464859097730309", "7399464859097730309", "7c04007ecac9bd5c70c1c5aa65b22063", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Pixel_Scan           = EffectMeta("Pixel Scan", True, "7399470385281895686", "7399470385281895686", "9ae5f3f5cde37092684a03e7aad1ae22", [
                              EffectParam("effects_adjust_rotate", 0.320, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认32%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认45%, 0% ~ 100%
    effects_adjust_sharpen: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认90%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Player_3             = EffectMeta("Player 3", True, "7414192016289991942", "7414192016289991942", "0e96b6ecf8c8e9760797677f7d905f05", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.219, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认22%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认85%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认67%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认67%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认100%, 0% ~ 100%"""
    Pulse_Line           = EffectMeta("Pulse Line", True, "7399468280848633094", "7399468280848633094", "798630fbe18ab78b9a751a48341aed8b", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.210, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认21%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_soft: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    RGB_Shake            = EffectMeta("RGB Shake", True, "7399467882129673478", "7399467882129673478", "b4d72c47be1ca1238cddf0790a8a0c55", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    RGB_故障             = EffectMeta("RGB 故障", True, "7477878980457090357", "7477878980457090357", "bf13c08912c5e5a2a72bc05c526f5818", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    RGB描边              = EffectMeta("RGB描边", True, "7399466347505257733", "7399466347505257733", "175536eb523aae867ae4b8cb94f09211", [
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认67%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    RGB闪光              = EffectMeta("RGB闪光", True, "7527148767439539509", "7527148767439539509", "abcfe0b32aac0ebb17578b34293247d3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    Rainbow_Twist        = EffectMeta("Rainbow Twist", True, "7395474293095812358", "7395474293095812358", "bf6fb74a7290e9a8d31dc36453736b66", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.660, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认66%, 0% ~ 100%"""
    Ripples_Clear        = EffectMeta("Ripples Clear", True, "7395466204183301381", "7395466204183301381", "d4009f4188b7c8293760896d5a606f0f", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%"""
    Sci_Fi_Scan          = EffectMeta("Sci-Fi Scan", True, "7399471245038734598", "7399471245038734598", "8b7a9733b393b42cf018ce2efdebca2a", [
                              EffectParam("effects_adjust_soft", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_soft: 默认75%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Shaky_Ripples        = EffectMeta("Shaky Ripples", True, "7399465637690772742", "7399465637690772742", "7d07628d9ac0b73dfc34611e1cf9ed79", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    Slide_Viral          = EffectMeta("Slide Viral", True, "7494120399211400449", "7494120399211400449", "5d69af04df8c529e497fc736f29d6157", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Slinky_扭转          = EffectMeta("Slinky 扭转", True, "7526846708576242997", "7526846708576242997", "4327ebed75c627189a661d42735322f3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.714, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认71%, 0% ~ 100%"""
    Snapshot             = EffectMeta("Snapshot", True, "7399465653700250886", "7399465653700250886", "49d70fec464c90afff087cb5854997dd", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    Spin_Shake           = EffectMeta("Spin & Shake", True, "7395472259441315078", "7395472259441315078", "a2df1870a268dac31ac369382c42cf43", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    Spin_Shake_2         = EffectMeta("Spin & Shake 2", True, "7395474848148999430", "7395474848148999430", "a080eeb37e5c98ff3a510c395463727a", [
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_rotate: 默认80%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认80%, 0% ~ 100%"""
    Step_Printing        = EffectMeta("Step Printing", True, "7399468524931910918", "7399468524931910918", "1d1a1e368ce8a19063aa0c801eb757f7", [
                              EffectParam("effects_adjust_blur", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认20%, 0% ~ 100%"""
    Stretch_Swivel       = EffectMeta("Stretch & Swivel", True, "7399468171998137605", "7399468171998137605", "8dd1ef0645dddee8170190583a1ff51a", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_distortion: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认67%, 0% ~ 100%"""
    Stretched_Rays       = EffectMeta("Stretched Rays", True, "7399466235026509061", "7399466235026509061", "3e1f119bd6387d1495fe234cf746e5f8", [
                              EffectParam("effects_adjust_number", 0.698, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    Sunshine             = EffectMeta("Sunshine", True, "7399468839571868934", "7399468839571868934", "5ee226902be5ac3294d53fb015b428d8", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%"""
    Swing                = EffectMeta("Swing", True, "7394782681134927110", "7394782681134927110", "bee293df8d3c2a62e722c60eca82aab3", [])
    S型运镜              = EffectMeta("S型运镜", True, "7488159889504668929", "7488159889504668929", "486e641056ec5e589900e50853a07a0b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    S运镜                = EffectMeta("S运镜", True, "7399471490363608325", "7399471490363608325", "1a137ba40b56a10809190892c3850f95", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_rotate: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    TV_Girl              = EffectMeta("TV Girl", True, "7517104774500617473", "7517104774500617473", "bb0742de6049b8d1d49dd6a593a54dcb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Take_Selfie          = EffectMeta("Take Selfie", True, "7399467531599105286", "7399467531599105286", "e9015b3c7ed322b9ede1fc39ad10f83d", [
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    Thunderbolt          = EffectMeta("Thunderbolt", True, "7399464269093408006", "7399464269093408006", "dfc0eec30caaa1a9f992332a85e89a7b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    Thunderbolt_2        = EffectMeta("Thunderbolt 2", True, "7395469416118455557", "7395469416118455557", "8129e3f83ad6973ba9e6613dbf7afb88", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    Tracking_Shot_2      = EffectMeta("Tracking Shot 2", True, "7399467027066375429", "7399467027066375429", "c669120668a01c7ff955bedb139703ab", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 0.900),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 90%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认80%, 0% ~ 100%"""
    Trendy_Graffiti      = EffectMeta("Trendy Graffiti", True, "7399465033895283973", "7399465033895283973", "cfebce70979bd33285976a65688e4131", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    Twisted_Focus        = EffectMeta("Twisted Focus", True, "7395471011677818117", "7395471011677818117", "83df4a1fadf009b94e737565720debef", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_distortion: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 100%"""
    T形展示              = EffectMeta("T形展示", True, "7491143613850668289", "7491143613850668289", "ae2644173e0bb554320799096f8c5b38", [])
    VCR                  = EffectMeta("VCR", True, "7399470774723071238", "7399470774723071238", "6b5dfc171f7c82078c76ffbcb2f6c003", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_sharpen: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    VX1000               = EffectMeta("VX1000", True, "7399468014107692293", "7399468014107692293", "1f49a03a6c27fb70d2d4568bf2fbd590", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_sharpen: 默认20%, 0% ~ 100%
    effects_adjust_distortion: 默认90%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    Vintage_Flash        = EffectMeta("Vintage Flash", True, "7399469589618232581", "7399469589618232581", "83e65027b467568dbc6dd666658e07d8", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认85%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    WOW                  = EffectMeta("WOW ", True, "7399466166831385862", "7399466166831385862", "cb6866e680ed221c0a546a055a4a0b9a", [])
    Waterfall            = EffectMeta("Waterfall", True, "7395473253902404869", "7395473253902404869", "ecd11cf24ab2644cc93ae00f4ad1a7d3", [
                              EffectParam("effects_adjust_speed", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认57%, 0% ~ 100%
    effects_adjust_intensity: 默认65%, 0% ~ 100%
    effects_adjust_texture: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认26%, 0% ~ 100%
    effects_adjust_range: 默认25%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%"""
    Whiplash             = EffectMeta("Whiplash", True, "7395465894941560069", "7395465894941560069", "c6f8519f592a44f74424411e304bd46b", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    Whippy_Twist         = EffectMeta("Whippy Twist", True, "7530124163437137213", "7530124163437137213", "8bf17d40b31a93293165551ed672c749", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    Y2K金属漩涡          = EffectMeta("Y2K金属漩涡", True, "7473710407329272337", "7473710407329272337", "e0d721a9c94e868d08dc57c7452d4d10", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    _321粒子倒数         = EffectMeta("321粒子倒数", True, "7483353118072245559", "7483353118072245559", "51305da4969626e9c5e98209209c6433", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _360度运镜           = EffectMeta("360度运镜", True, "7431850269475869201", "7431850269475869201", "d2035259bb0765fc66c528e0e13a2f70", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _360运镜_II          = EffectMeta("360运镜 II", True, "7434832634519228944", "7434832634519228944", "ac75ef9cb8e94297b5b2537e9e9f9edf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%"""
    _36倍复制            = EffectMeta("36倍复制", True, "7480827990973173053", "7480827990973173053", "19e974b8247fbbfeda8bba095cd33f3c", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认75%, 0% ~ 100%"""
    _3D_Love             = EffectMeta("3D Love", True, "7464124620363289105", "7464124620363289105", "c898b3e32d2cba4f7e91216c98fdd78b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    _3D_LoveII           = EffectMeta("3D LoveII", True, "7464124620359078401", "7464124620359078401", "bf536fc50c6c97b511f8b8bf7d1d3473", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    _3D_Surround         = EffectMeta("3D Surround", True, "7454130581283017232", "7454130581283017232", "96d33ee88360e17d149d61e53f71bcf3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    _3D互动弹窗          = EffectMeta("3D互动弹窗", True, "7476357155256291841", "7476357155256291841", "eede088e9adfd0d78a39146206a01b86", [])
    _3D卡片              = EffectMeta("3D卡片", True, "7478572703222418694", "7478572703222418694", "64139479c5c8b350f84e4dea5ac9f0ba", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    _3D卡片切开          = EffectMeta("3D卡片切开", True, "7474875426633026821", "7474875426633026821", "73b9cd9c2e7e2e01bfa11ab36627a221", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    _3D层次              = EffectMeta("3D层次", True, "7511584057067719952", "7511584057067719952", "94aa6ce560f55ad13e7b3a88dfb788e9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D手机2             = EffectMeta("3D手机2", True, "7529381361912663349", "7529381361912663349", "be44008e41e668e1706ae65497b630d0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D旋转小花          = EffectMeta("3D旋转小花", True, "7483025057317489975", "7483025057317489975", "bfb06ced38c1e9c0dd42717ac70d0584", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D气球掉落          = EffectMeta("3D气球掉落", True, "7483800844744297783", "7483800844744297783", "0b46aa1257f41ef724a132c1ab09d100", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    _3D浮动花朵          = EffectMeta("3D浮动花朵", True, "7476357155256275457", "7476357155256275457", "1930f696fd5516ee5841003a28d962d0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D消散              = EffectMeta("3D消散", True, "7490858499518319873", "7490858499518319873", "b567850952e13518081302a7ac5456a3", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    _3D爱心              = EffectMeta("3D爱心", True, "7464124620354884112", "7464124620354884112", "4370c6b2c559fb0edbbbdb2035b9aab4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D环绕屏            = EffectMeta("3D环绕屏", True, "7436469103449084432", "7436469103449084432", "58f30d06f89764104d9917d3e0b0a99e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.320, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认32%, 0% ~ 100%"""
    _3D轮播              = EffectMeta("3D轮播", True, "7519017840368700688", "7519017840368700688", "21b498f48353ddce16eefe7bc92e1d1f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3D透边框            = EffectMeta("3D透边框", True, "7509328194957298960", "7509328194957298960", "88dcc5b057681438ffdf57fe9d6ad481", [])
    _3d钻石              = EffectMeta("3d钻石", True, "7399470084755868934", "7399470084755868934", "afa5891d090fe132e4cf0a7196895863", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.548, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认55%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    _3条爆闪             = EffectMeta("3条爆闪", True, "7501211668895124753", "7501211668895124753", "5bb0f74d7ea762b2132194303c7ea291", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _3次推近             = EffectMeta("3次推近", True, "7488146934104952081", "7488146934104952081", "c7972ae9ba39ef74b9728bad232249e7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    _4K_HDR              = EffectMeta("4K HDR", True, "7399467795173477638", "7399467795173477638", "a3e3c15a34932caa71817181da4ade34", [
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.500),
                              EffectParam("effects_adjust_sharpen", 1.400, 0.000, 2.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认30%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 150%
    effects_adjust_sharpen: 默认140%, 0% ~ 200%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _90s                 = EffectMeta("90s", True, "7399470883863055621", "7399470883863055621", "9951245808ea4a3838a63023536ef720", [
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.070, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.090, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认7%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认9%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    _90s画质             = EffectMeta("90s画质", True, "7409873569586466054", "7409873569586466054", "2fe76441036c1e7d2ad8561d9265cfda", [
                              EffectParam("effects_adjust_texture", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认30%, 0% ~ 100%"""
    _90度缩小            = EffectMeta("90度缩小", True, "7525364051136875837", "7525364051136875837", "8fb2ba609c5f09f8b0012b5b58c6c2c8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    _9克隆介绍           = EffectMeta("9克隆介绍", True, "7530648494760054069", "7530648494760054069", "c790b53a5f01e393365a2ed0cb3b56f2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    ccd界面              = EffectMeta("ccd界面", True, "7509328682780003585", "7509328682780003585", "ee79612ffc92fa47cde0b7de75847847", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    ins边框              = EffectMeta("ins边框", True, "7399467797903838469", "7399467797903838469", "2a92fcc337bb33af058a2b90b111e704", [])
    ins边框放大镜        = EffectMeta("ins边框放大镜", True, "7399466299115539717", "7399466299115539717", "afe7daae94e810f06b339c96deafb5f8", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    一刀两断             = EffectMeta("一刀两断", True, "7399468886309211398", "7399468886309211398", "6e66b782a69fa0c2712deeaf50d4aadf", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    丁达尔旋焦           = EffectMeta("丁达尔旋焦", True, "7395466266540084486", "7395466266540084486", "815fe4564516ccb104dd6a12682e6ac2", [
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%"""
    万圣夜               = EffectMeta("万圣夜", True, "7399469293840256262", "7399469293840256262", "672d11ce209f6032348597f93e48dc7c", [
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    万花筒               = EffectMeta("万花筒", True, "7399471325254929670", "7399471325254929670", "b8f55aa81a228ab966bd9e8fbc599fba", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    万花筒_II            = EffectMeta("万花筒 II", True, "7399466557459549446", "7399466557459549446", "055c805b6618672c092f969c660462a5", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    三图抛掷             = EffectMeta("三图抛掷", True, "7531814758157126965", "7531814758157126965", "35fb461ddccb328eb35a1e73633bec48", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    三层展示             = EffectMeta("三层展示", True, "7512632938308128017", "7512632938308128017", "1de9c85168c989468416ad5186816d09", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三层闪光             = EffectMeta("三层闪光", True, "7509684266201042193", "7509684266201042193", "40a96d738e403de784b93dcc14ffa74c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三屏                 = EffectMeta("三屏", True, "7399471080097893638", "7399471080097893638", "ef3bfd8b9fb71755fcba8fcc8359a0f4", [])
    三格漫画             = EffectMeta("三格漫画", True, "7399465854498245894", "7399465854498245894", "82f7d80616022fb471a047e9bd4c7104", [])
    三段式黑白           = EffectMeta("三段式黑白", True, "7451535587820966401", "7451535587820966401", "5a47368758c30ac86bead6f943caf268", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三维旋转             = EffectMeta("三维旋转", True, "7519840408797515069", "7519840408797515069", "489de8ca7ea2731e4f0cab6374c791d1", [
                              EffectParam("effects_adjust_texture", 2.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认200%, 0% ~ 100%"""
    三维镜摇             = EffectMeta("三维镜摇", True, "7514875452096335120", "7514875452096335120", "e340bbe44fdafccec5f321e201e4a5b1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三连步               = EffectMeta("三连步", True, "7511717126357437757", "7511717126357437757", "2a489e71205579298a2cdc6b11e85115", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    三部手机             = EffectMeta("三部手机", True, "7524768853700660533", "7524768853700660533", "76f21e7b661339639c87c3173de31524", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    三重旋转             = EffectMeta("三重旋转", True, "7517973865587297589", "7517973865587297589", "7ba4c6730a16e4bd4feb69796eec8308", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三重照片             = EffectMeta("三重照片", True, "7517348063208344893", "7517348063208344893", "9685c0e35d77027d60e89c1c11a89ea3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    三重缩小             = EffectMeta("三重缩小", True, "7517175166900718909", "7517175166900718909", "e6737cd7915205aa139ecbae844ba520", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    三重面板             = EffectMeta("三重面板", True, "7527990343774539061", "7527990343774539061", "575c4d9588d87bd3383c8fa7073c9a19", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    上下摆动             = EffectMeta("上下摆动", True, "7506812707992063293", "7506812707992063293", "09a625134988d279db9d84f05deeacbd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    上下混乱             = EffectMeta("上下混乱", True, "7515003828912065845", "7515003828912065845", "2e1f8dc4f01e1cb80c638f9b45e76cb9", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_chromatic: 默认20%, 0% ~ 100%"""
    上下缩放             = EffectMeta("上下缩放", True, "7508980291550088509", "7508980291550088509", "7a6c04334c395c914fdc9f0639e8e5e7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    上升气泡             = EffectMeta("上升气泡", True, "7529463249654320437", "7529463249654320437", "8d20b499ce7170a3a67dbfdd01a82910", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    下拉菜单             = EffectMeta("下拉菜单", True, "7477491348795444533", "7477491348795444533", "8df3b885693eab8ec240b8c4c0464c3f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认75%, 0% ~ 100%"""
    下雨涟漪             = EffectMeta("下雨涟漪", True, "7434830442265580049", "7434830442265580049", "611edf767c951b6f31a2b4de0457db2d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    不和谐               = EffectMeta("不和谐", True, "7514924935664422197", "7514924935664422197", "f7cf6f0025af0d6fb2f16fd7f8ed09de", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    不稳定镜头           = EffectMeta("不稳定镜头", True, "7530480374481210685", "7530480374481210685", "36bccb4168b4cf39cbd4ca3df47b2e81", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    不规则拼图           = EffectMeta("不规则拼图", True, "7512109954380221749", "7512109954380221749", "b2240852a7816afbe12aa4566faebe3f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    不规则撕纸           = EffectMeta("不规则撕纸", True, "7414313031716375814", "7414313031716375814", "fc54905d7afe1b92ce907488cd8b6a17", [])
    丝印涂鸦             = EffectMeta("丝印涂鸦", True, "7399470314947759365", "7399470314947759365", "7770fc357d8dbbb746e67031dab7afe9", [
                              EffectParam("effects_adjust_color", 0.200, 0.050, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.570, 0.000, 0.810),
                              EffectParam("effects_adjust_speed", 0.430, 0.000, 0.700),
                              EffectParam("effects_adjust_texture", 0.120, 0.000, 0.500)])
    """参数:
    effects_adjust_color: 默认20%, 5% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认57%, 0% ~ 81%
    effects_adjust_speed: 默认43%, 0% ~ 70%
    effects_adjust_texture: 默认12%, 0% ~ 50%"""
    丝滑运镜             = EffectMeta("丝滑运镜", True, "7395466063724514565", "7395466063724514565", "9333197e30c47f6aab8eb7b6bba7bd38", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认67%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    两屏                 = EffectMeta("两屏", True, "7399469643334683909", "7399469643334683909", "7850519365aaef0e1d38574238117925", [])
    两张卡片             = EffectMeta("两张卡片", True, "7520061953826475325", "7520061953826475325", "86cae93ed16e3155f46f3b1a32594b77", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    九屏跑马灯           = EffectMeta("九屏跑马灯", True, "7399473125525605638", "7399473125525605638", "ff18dc9f6e55e6a8220d07546677d5b3", [])
    乱码涂鸦             = EffectMeta("乱码涂鸦", True, "7395470554397969670", "7395470554397969670", "a031c206a96ad96752aac14497648213", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    乱码背景             = EffectMeta("乱码背景", True, "7488915982379977985", "7488915982379977985", "ac2986ce1665a9a1e7e39815fbe390f8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    二层空间             = EffectMeta("二层空间", True, "7517122541882756353", "7517122541882756353", "79c717711eb4675962232e001c834f60", [])
    二次元运镜           = EffectMeta("二次元运镜", True, "7451535587820966416", "7451535587820966416", "eb9c27e0a6820a5378dfa46271a05a1f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    云空间垃圾           = EffectMeta("云空间垃圾", True, "7485954861247319349", "7485954861247319349", "9242ba4b0084a4474bc5bc2c07a25958", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    五图展开             = EffectMeta("五图展开", True, "7522752548894182717", "7522752548894182717", "6098e17a02ec92aa4d50ff26b6deede9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.498, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    五官乱飞             = EffectMeta("五官乱飞", True, "7483447800911433015", "7483447800911433015", "abba9fb192a46505720860db124f7e29", [
                              EffectParam("effects_adjust_speed", 0.440, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认44%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    五角旋转             = EffectMeta("五角旋转", True, "7526833237512047933", "7526833237512047933", "38e6f4efd0bfd90e67d5db7f58d7ccd2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.167, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认17%, 0% ~ 100%"""
    交叉分割             = EffectMeta("交叉分割", True, "7473741308079656253", "7473741308079656253", "c0585c43e2413bb57793f4f9c275b31d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    交叉模糊             = EffectMeta("交叉模糊", True, "7476324457078983997", "7476324457078983997", "8116a67103002db8486ab96af3f6adf3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    交叉置换             = EffectMeta("交叉置换", True, "7512271513807080720", "7512271513807080720", "ec482b79aec230ef570fcf28f66f7bd2", [])
    交叉震闪             = EffectMeta("交叉震闪", True, "7399471479596895494", "7399471479596895494", "946b0d91761e5ac85c2e133aa220d235", [
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%"""
    人行道混搭           = EffectMeta("人行道混搭", True, "7501170369559039293", "7501170369559039293", "cf21781ee5404c024692d1ea6123c0fc", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认30%, 0% ~ 100%"""
    仙女变身_II          = EffectMeta("仙女变身 II", True, "7399471489898073349", "7399471489898073349", "11a5fc7a98c10df98bdf01ea7720fd49", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    仙女棒               = EffectMeta("仙女棒", True, "7395472122757270790", "7395472122757270790", "0e18d5f130b2bdadf248c1c226b7b734", [
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    仙女棒II             = EffectMeta("仙女棒II", True, "7447086181742809617", "7447086181742809617", "d8d59ffd556810c73d7a65dd0aa8f523", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    低保真               = EffectMeta("低保真", True, "7399465317946395910", "7399465317946395910", "afb3e21fb90b170bc431dd088513b2ed", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认75%, 0% ~ 100%
    effects_adjust_sharpen: 默认20%, 0% ~ 100%"""
    低像素光效           = EffectMeta("低像素光效", True, "7460017740183653638", "7460017740183653638", "eaac5dfe25c3338ee958768f170f516d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    低像素风写真         = EffectMeta("低像素风写真", True, "7528084459535551805", "7528084459535551805", "89c784634a0058afdf1c0a7ec29efe84", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    低像素风写真镜头     = EffectMeta("低像素风写真镜头", True, "7514511314853711157", "7514511314853711157", "85ae8ee407a48be4ce3a6adfc5482518", [
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认67%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    侧滑模糊             = EffectMeta("侧滑模糊", True, "7395470533514595589", "7395470533514595589", "7b7baa2a697b1d7a119902167b7bff4a", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    信号不好             = EffectMeta("信号不好", True, "7517879021779160373", "7517879021779160373", "3481624207517389f0b315510d22d9ca", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    信号干扰             = EffectMeta("信号干扰", True, "7452646287314260497", "7452646287314260497", "49f0a32af467b676f274dc00af78e562", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    倍增                 = EffectMeta("倍增", True, "7527728724679101757", "7527728724679101757", "40d364e92680dc0473429b4d1ddd5573", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    倒置点               = EffectMeta("倒置点", True, "7516931178281159997", "7516931178281159997", "7987d37f17097cfc68672a3f6b7a7653", [
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    倒计时               = EffectMeta("倒计时", True, "7399464331236101381", "7399464331236101381", "06c20494725c2b5873c5aac7fcea3205", [])
    倒计时_III           = EffectMeta("倒计时 III", True, "7454159821902713345", "7454159821902713345", "7bd1e54fade0f0560b63b4ec3f76a6f4", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.375, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认38%, 0% ~ 100%"""
    倒转闪烁             = EffectMeta("倒转闪烁", True, "7510232010292563261", "7510232010292563261", "4593ba9c4ed314b9d5dd555156c1f7e1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    倾斜抽卡             = EffectMeta("倾斜抽卡", True, "7491900954673958160", "7491900954673958160", "29ea43b4281e0b57c07427bc7f6c5855", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    倾斜模糊             = EffectMeta("倾斜模糊", True, "7511260816528723261", "7511260816528723261", "26ee3c9c6bf65253cc47c24939a525a6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    假日闪闪             = EffectMeta("假日闪闪", True, "7399467240111869189", "7399467240111869189", "71562d36767edd689fa49c808414909d", [
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_number: 默认22%, 0% ~ 100%
    effects_adjust_rotate: 默认12%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%"""
    催眠                 = EffectMeta("催眠", True, "7507605563602128181", "7507605563602128181", "a287ad7dabaa82b8cbaf7c3386c81f2f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    像素屏幕             = EffectMeta("像素屏幕", True, "7478527226674203957", "7478527226674203957", "d3cfc7609643af3c42ac71261c1df9a5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    像素拉伸             = EffectMeta("像素拉伸", True, "7399466219721526533", "7399466219721526533", "2e8c70703d0bf2cf7119a3f49be9d57e", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认60%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    像素排序             = EffectMeta("像素排序", True, "7395468187455868166", "7395468187455868166", "24e9de1fa2c77ec26045f7113fdc79f9", [
                              EffectParam("effects_adjust_number", 0.940, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认94%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_noise: 默认0%, 0% ~ 100%"""
    像素条纹             = EffectMeta("像素条纹", True, "7514440776659651856", "7514440776659651856", "eeef686afe2b95704fe1cfc76855fd62", [])
    像素狂潮             = EffectMeta("像素狂潮", True, "7532909489985572149", "7532909489985572149", "f940f2ceb967a707dfc997609729ba92", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    像素翡翠             = EffectMeta("像素翡翠", True, "7511985228567661885", "7511985228567661885", "6abd403c349696dbc848a4cdfbca4123", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    像素迷雾             = EffectMeta("像素迷雾", True, "7533527311665138997", "7533527311665138997", "e7aaa5a1c94c333897732590f8027b87", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    光幕                 = EffectMeta("光幕", True, "7486089848235756853", "7486089848235756853", "546d28b3cc4d6aa10624c996957b810d", [
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认67%, 0% ~ 100%"""
    光影流动             = EffectMeta("光影流动 ", True, "7399469191780125958", "7399469191780125958", "158082f791a0166f9c7496a2822085d3", [
                              EffectParam("effects_adjust_noise", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.554, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.979, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.785, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认57%, 0% ~ 100%
    effects_adjust_range: 默认55%, 0% ~ 100%
    effects_adjust_intensity: 默认98%, 0% ~ 100%
    effects_adjust_filter: 默认79%, 0% ~ 100%"""
    光效扭曲             = EffectMeta("光效扭曲", True, "7525475753530608957", "7525475753530608957", "9fc644dd1af6be91fac751ed17ddc451", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    光球镜头             = EffectMeta("光球镜头", True, "7524215733056802101", "7524215733056802101", "b21004038d07705962478efbd1170925", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.501, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.501, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    光盘擦拭             = EffectMeta("光盘擦拭", True, "7530860913524526397", "7530860913524526397", "506d880303166b9de35fde8b8ccd8b8a", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    光线拖影             = EffectMeta("光线拖影", True, "7399466389246856454", "7399466389246856454", "1cee833d647541e86d24bb2f7b7635ea", [
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.340, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认34%, 0% ~ 100%"""
    光边卡片             = EffectMeta("光边卡片", True, "7517835491857681665", "7517835491857681665", "924da2e794bafd13f465807ff3adc46b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    光速淡紫色           = EffectMeta("光速淡紫色", True, "7514169300832341309", "7514169300832341309", "d6b9c9cde6ee92174151487c9aefc4e8", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    克隆排位             = EffectMeta("克隆排位", True, "7517191267667709245", "7517191267667709245", "1abb861a6982da1dd9942716163187b9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    入侵                 = EffectMeta("入侵", True, "7509117321634532661", "7509117321634532661", "3a50d9313e1bcbb014ef35aec22eb68d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    全息扫描             = EffectMeta("全息扫描", True, "7399465915508641030", "7399465915508641030", "8fc971df0b10b5e14e747adb301fae31", [
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.570, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认75%, 0% ~ 100%
    effects_adjust_blur: 默认26%, 0% ~ 100%
    effects_adjust_background_animation: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认57%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认60%, 0% ~ 100%"""
    六屏                 = EffectMeta("六屏", True, "7399465476688006405", "7399465476688006405", "fec1efb68fe608dbed22450913e70cc1", [])
    六边形光斑           = EffectMeta("六边形光斑", True, "7399466433782058245", "7399466433782058245", "bac385d0e3a690faf2bb5f953e033f13", [
                              EffectParam("effects_adjust_size", 0.521, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认52%, 0% ~ 100%
    effects_adjust_intensity: 默认72%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认33%, 0% ~ 100%"""
    冬日缤纷             = EffectMeta("冬日缤纷", True, "7399472194763427078", "7399472194763427078", "cffd7f17cd4d943957f52b9650101b45", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认90%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    冰霜                 = EffectMeta("冰霜", True, "7399471212944051462", "7399471212944051462", "17d279016b1f0961c4e0167f2554b0f5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    冲击波               = EffectMeta("冲击波", True, "7399467918850903301", "7399467918850903301", "ad8e0a154e7a3c78dc23407ec23da9b2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    冻结轮播             = EffectMeta("冻结轮播", True, "7488269454778895677", "7488269454778895677", "83b13291fdbfcbbd2c93fd035265dfae", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    凌乱踩踏             = EffectMeta("凌乱踩踏", True, "7514588684616813885", "7514588684616813885", "ed0c26b719215cfe454f03f0fbb19f16", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    分割光感             = EffectMeta("分割光感", True, "7526982599353388349", "7526982599353388349", "952720de5e5296527db8e67f9bbedd11", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    分割砖块             = EffectMeta("分割砖块", True, "7489003869591080253", "7489003869591080253", "8bc9fe6346ae1fcc26695806320d47af", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认75%, 0% ~ 100%"""
    分割素材             = EffectMeta("分割素材", True, "7532077401191288125", "7532077401191288125", "f9f39d641082949b6925c1f279a36a87", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    分割闪白             = EffectMeta("分割闪白", True, "7524592976048295184", "7524592976048295184", "58a6ff4ffbc202aedf499050b71c22bb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    分区显色             = EffectMeta("分区显色", True, "7452646287322649089", "7452646287322649089", "35a524c9ede1072f31f3b22ba1ede359", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    分层边框             = EffectMeta("分层边框", True, "7480033846457683253", "7480033846457683253", "d8abfd566e87d3b82deac619eacefaa8", [
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    分屏闪光             = EffectMeta("分屏闪光", True, "7399468524932009222", "7399468524932009222", "654fed1e76552e75468194bbadcd2003", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("sticker", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    sticker: 默认0%, 0% ~ 100%"""
    分格故障             = EffectMeta("分格故障", True, "7506004148077317392", "7506004148077317392", "db6f8a2e600202de9846a289ef35cf88", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    切削滑动             = EffectMeta("切削滑动", True, "7454509184315428157", "7454509184315428157", "c6a3ba023a249e95af9d06e02d795e2d", [])
    切碎拉伸             = EffectMeta("切碎拉伸", True, "7495627865124375869", "7495627865124375869", "29ff75a288d7ee15bb25350ce19a2790", [
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认10%, 0% ~ 100%"""
    初始展开             = EffectMeta("初始展开", True, "7521747692154834237", "7521747692154834237", "e631092dffc37bc61904b25208b7ffba", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    别致电梯             = EffectMeta("别致电梯", True, "7485385731129609525", "7485385731129609525", "4d6d89cf9f1642329f23aba6e1e34a15", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    剪贴                 = EffectMeta("剪贴", True, "7488021131195108669", "7488021131195108669", "14a86a96b64023c0a0a4c255b51f1385", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    剪辑模拟             = EffectMeta("剪辑模拟", True, "7414191511266692358", "7414191511266692358", "0b76b1bcc6b30b539e8d83a60404f3cc", [])
    力量模糊             = EffectMeta("力量模糊", True, "7514169958549556533", "7514169958549556533", "0054e676181da6f847914122ecf5872e", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    动态照片拼贴         = EffectMeta("动态照片拼贴", True, "7521556250937658685", "7521556250937658685", "23a01bf1443d3ca41028d257c5ff8d4f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    动态肖像             = EffectMeta("动态肖像", True, "7509757633725844789", "7509757633725844789", "9bf75101701de96287698b1ebcc74b97", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    动感光束             = EffectMeta("动感光束", True, "7399468708839558405", "7399468708839558405", "73ca708352e45556211ecebd51928528", [
                              EffectParam("effects_adjust_intensity", 0.581, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.398, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认58%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认40%, 0% ~ 100%"""
    动感光波             = EffectMeta("动感光波", True, "7517503216691498257", "7517503216691498257", "3682fdb0bbeddb3857a25fd7de88b76d", [])
    动感猛震             = EffectMeta("动感猛震", True, "7532303960275766545", "7532303960275766545", "b9bc93380eb6f0e65cad503d7a671261", [
                              EffectParam("effects_adjust_filter", 2.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认200%, 0% ~ 100%"""
    动感虚化             = EffectMeta("动感虚化", True, "7399467609608948997", "7399467609608948997", "beb9fe305631f5d4f3c997aff60fdf13", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%"""
    十字形模糊           = EffectMeta("十字形模糊", True, "7399468981905575174", "7399468981905575174", "1855e87e914fb04b0aae6a4e8bfe8eb0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%"""
    十字爆闪             = EffectMeta("十字爆闪", True, "7399466486819081478", "7399466486819081478", "4fd183401936b0e5ddccc73bcb9d538f", [
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    半屏闪光             = EffectMeta("半屏闪光", True, "7516432544800214333", "7516432544800214333", "b7d5f9c2ac09c3495e7fa8f7a12f527b", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    半色调反向           = EffectMeta("半色调反向", True, "7529060059918224693", "7529060059918224693", "440f3018e9d82ec771d2d379a1def730", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    华容道拼图           = EffectMeta("华容道拼图", True, "7523118322976623925", "7523118322976623925", "8e29ad6e2205ad41431914053806bafb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    单彩渐变             = EffectMeta("单彩渐变", True, "7395470449389374726", "7395470449389374726", "bb064dadbd40eda875b9a632d07c4e3f", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_rotate: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%"""
    单色                 = EffectMeta("单色", True, "7493141691440942389", "7493141691440942389", "f2944f75311ab16583863aed70508586", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    单色电影             = EffectMeta("单色电影", True, "7414191633908108550", "7414191633908108550", "695862ab1d10fb075addf71863b7de64", [
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认20%, 0% ~ 100%"""
    单色胶片             = EffectMeta("单色胶片", True, "7414191151403617541", "7414191151403617541", "90e29d786fc3a5980194ad485e4ac891", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    单色错误             = EffectMeta("单色错误", True, "7509778752084217141", "7509778752084217141", "128b588035cb4b4aad8a427276e496c6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    南瓜幽灵             = EffectMeta("南瓜幽灵 ", True, "7399471582768336134", "7399471582768336134", "c440724a491336aba4e24910d5c7f6f1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    卡带闪回             = EffectMeta("卡带闪回", True, "7399468263731662085", "7399468263731662085", "556deae0cd09fd1ba2835f6cedebca20", [
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片分屏             = EffectMeta("卡片分屏", True, "7530473508929801488", "7530473508929801488", "af36427cbdd8faabe59fa879536a023b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    卡片抽取             = EffectMeta("卡片抽取", True, "7511965315388034305", "7511965315388034305", "a2b6f3c2d1b79e2f3d855d3a4b13cb93", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片摇摆             = EffectMeta("卡片摇摆", True, "7519564288671976757", "7519564288671976757", "a0a52480641f467e5e0c642be4f95e6b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片运镜             = EffectMeta("卡片运镜", True, "7519354024731200785", "7519354024731200785", "23e5da4383e6468eff64073ea0276c67", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片遮挡             = EffectMeta("卡片遮挡", True, "7534567469185322241", "7534567469185322241", "5bc8d31c6a51bce3148b6a8457f18ef7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片闪屏             = EffectMeta("卡片闪屏", True, "7515196918142733584", "7515196918142733584", "de6fd127c74a0ba20efd47a090e61acd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片闪现             = EffectMeta("卡片闪现", True, "7517974201416846653", "7517974201416846653", "869208df090beeede0dd9e39555b30a2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡片飞幕             = EffectMeta("卡片飞幕", True, "7515220406698052880", "7515220406698052880", "8375088b88a9524cc667532a42db248c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    卡顿电视             = EffectMeta("卡顿电视", True, "7478206783106878726", "7478206783106878726", "f4e155532fc280eab21567da6ac9b77d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    卷动                 = EffectMeta("卷动", True, "7399466557459467526", "7399466557459467526", "431b2ce9d4b6e93443a9bbc273e14173", [])
    卷带滚动             = EffectMeta("卷带滚动", True, "7478353575911902525", "7478353575911902525", "bee94b28c3f58e10f2f41460d7c11598", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    原相机滤镜           = EffectMeta("原相机滤镜", True, "7441466472959840769", "7441466472959840769", "d90a78c5f18627218ddee1e1b6141d95", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    原相机缩放           = EffectMeta("原相机缩放", True, "7441466472968229377", "7441466472968229377", "2385a423c961fdacb62bfd518321f609", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    双切冲屏             = EffectMeta("双切冲屏", True, "7508549076158287105", "7508549076158287105", "c9b488030ae8980766cfc6b2c0b0f539", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    双层缩小             = EffectMeta("双层缩小", True, "7531711362096041277", "7531711362096041277", "988cdeb6951ce9b560a76d0f880edc51", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    双翻转               = EffectMeta("双翻转", True, "7488647709604285749", "7488647709604285749", "0c61e46835e56348b49b2edbf6d42fdc", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认0%, 0% ~ 100%"""
    双重爆闪             = EffectMeta("双重爆闪", True, "7490376418958920977", "7490376418958920977", "06e85407b5f204391dcda12155246b06", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    双重辉光             = EffectMeta("双重辉光", True, "7414312738849148166", "7414312738849148166", "cc39c639f79823193a72fb2af2510b41", [
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认30%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认30%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    双面旋转             = EffectMeta("双面旋转", True, "7508552010363325712", "7508552010363325712", "197d1cc3becdbeff040f22ea34093595", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    反向鱼眼             = EffectMeta("反向鱼眼", True, "7485951282574937397", "7485951282574937397", "b0f78800e6459e49335cf2df56573c24", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    反转开幕             = EffectMeta("反转开幕", True, "7399471215905082630", "7399471215905082630", "5c2e65bd2d5f0a551de63b58ab1bfa7d", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认10%, 0% ~ 100%"""
    反转片_I             = EffectMeta("反转片 I", True, "7399468872413285638", "7399468872413285638", "442b39ec01b7ddefd1a2dfe1ce66d00e", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    反转片_II            = EffectMeta("反转片 II", True, "7399471332041297157", "7399471332041297157", "d7e1b5a4083d40133cee470be5b3ed20", [
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认90%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认70%, 0% ~ 100%
    effects_adjust_noise: 默认40%, 0% ~ 100%"""
    反转间隙             = EffectMeta("反转间隙", True, "7532842796495981877", "7532842796495981877", "33ae95e1ec2c7ba4fda426f49479e5e9", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    发光HDR              = EffectMeta("发光HDR", True, "7399467465660534022", "7399467465660534022", "b8edf09f4d1a634d203cd4e30c23a90e", [
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_sharpen: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认90%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认15%, 0% ~ 100%"""
    发光_2               = EffectMeta("发光 2", True, "7409873342792043781", "7409873342792043781", "7ea9db818289cf323dc4eff20e79a23f", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    发光代码             = EffectMeta("发光代码", True, "7482611615402183941", "7482611615402183941", "01f079ddaafdbf77c2b80d34bf631e35", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    发光旋转器           = EffectMeta("发光旋转器", True, "7524608347685883197", "7524608347685883197", "bb7f0fdecd6b5b72a2c394bc87e8036a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    发光显示器           = EffectMeta("发光显示器", True, "7520018238919429393", "7520018238919429393", "ef8837293e36f5fa771cc3ffbfc40d2e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    发光漂移             = EffectMeta("发光漂移", True, "7522372621443370301", "7522372621443370301", "0822c9ed7b79142de46b3690a99ebe6a", [
                              EffectParam("effects_adjust_speed", 0.114, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    取景框               = EffectMeta("取景框", True, "7399471332041166085", "7399471332041166085", "1915e124716f1967476f78970f6e90b9", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    变形了               = EffectMeta("变形了", True, "7399470557198273797", "7399470557198273797", "14a104e40077679260fa7d622dce5178", [])
    变清晰_II            = EffectMeta("变清晰 II", True, "7399472015465286918", "7399472015465286918", "ed982716861fc309c79084adcc6d9e13", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    变焦烟花             = EffectMeta("变焦烟花", True, "7446716461734711824", "7446716461734711824", "be0a829782f17e209e1192f25347e784", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    变色狙击             = EffectMeta("变色狙击", True, "7399470402084277509", "7399470402084277509", "f4876e6aa0a710888c0dded6dd35879c", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    变速拉扭             = EffectMeta("变速拉扭", True, "7511915005583953169", "7511915005583953169", "14492ddbfebf6db8b1ec5891d85fc434", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    叠纸时空             = EffectMeta("叠纸时空", True, "7414312944600632581", "7414312944600632581", "5c6a2c3b5990f728c2d6722a452015cd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    古怪撕裂             = EffectMeta("古怪撕裂", True, "7508601897910095157", "7508601897910095157", "e99bcc3b11034b2a50cd1398cdc981f0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    古董相机             = EffectMeta("古董相机", True, "7519212528119958845", "7519212528119958845", "7a620aec7b658f4823a51066bf1db270", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    合集                 = EffectMeta("合集", True, "7528014184680869181", "7528014184680869181", "99a82415b58789d72a3dd1cd56fb5b91", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    名片                 = EffectMeta("名片", True, "7496036763891240193", "7496036763891240193", "8d6c4556edd4c732d8391b2f250acab1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    向上排队             = EffectMeta("向上排队", True, "7518353468973649205", "7518353468973649205", "65f1ee530a9a075e527081eb2c4a69c9", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    向右缩放             = EffectMeta("向右缩放", True, "7508685360466054453", "7508685360466054453", "e41fddf9f13a8e4ff6a25326ba829376", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    向左缩放             = EffectMeta("向左缩放", True, "7508704595741379893", "7508704595741379893", "9815483edb50acdb2cf1d69f76b0f8eb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    吻标记               = EffectMeta("吻标记", True, "7485415328890080573", "7485415328890080573", "d7ff769e02f015a9e152973ee0385e67", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.655, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认66%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    哈哈镜               = EffectMeta("哈哈镜", True, "7529889013671529789", "7529889013671529789", "2bb7b0b5d63eadb84dd7f32dfcba881e", [
                              EffectParam("effects_adjust_speed", 0.103, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认10%, 0% ~ 100%"""
    哈苏胶片             = EffectMeta("哈苏胶片", True, "7399471764062997766", "7399471764062997766", "2eead808b8408e1fa4b74b6ad3c74b8d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认30%, 0% ~ 100%"""
    嗖滑动               = EffectMeta("嗖滑动", True, "7483365389439749437", "7483365389439749437", "1c3c2b36e3b4ec9d895ffda171a0053b", [])
    噪点屏闪             = EffectMeta("噪点屏闪", True, "7426269857357763089", "7426269857357763089", "c7eb0a537b7ec9317a0f4f5912fc95eb", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    噪音闪震             = EffectMeta("噪音闪震", True, "7495955168005983504", "7495955168005983504", "acc18f49aafa45d6cd715853cd6112f4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    四分闪转             = EffectMeta("四分闪转", True, "7525577152335498497", "7525577152335498497", "f2b53461c893a0960a6a5f5bf080614f", [])
    四叶旋转             = EffectMeta("四叶旋转", True, "7528043345315204413", "7528043345315204413", "a0d1dc76a5a3320305689d3ccbd65281", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    四格递进             = EffectMeta("四格递进", True, "7515223872975768833", "7515223872975768833", "caa1aa34fedf7c050233c401c6312453", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    四点平移             = EffectMeta("四点平移", True, "7512073654902000949", "7512073654902000949", "2c330a7db234fe55a603c547575ec99a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    四色相组合           = EffectMeta("四色相组合", True, "7531429204462800189", "7531429204462800189", "cd702cdf27d1035cd7a5d48545a726fa", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    固定节奏             = EffectMeta("固定节奏", True, "7525422998925397301", "7525422998925397301", "f27ea560e327b7d6abe7c954ab772cc2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    图框缩放             = EffectMeta("图框缩放", True, "7485722216206716213", "7485722216206716213", "29f0b1e10f9e90f1235adc2da7f7affa", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    圣诞Kira             = EffectMeta("圣诞Kira", True, "7399469043415141638", "7399469043415141638", "25c17f4d81544882310f7a2c32dde3fa", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认0%, 0% ~ 100%"""
    圣诞kira             = EffectMeta("圣诞kira", True, "7446716461738889729", "7446716461738889729", "6e2013b11ab5a18c0084a6795bd6cc2f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    圣诞光斑             = EffectMeta("圣诞光斑", True, "7399465244088700165", "7399465244088700165", "8730af5a5d402cbd56e59877cc9fadf8", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    圣诞开幕             = EffectMeta("圣诞开幕", True, "7450046927875346960", "7450046927875346960", "086138606ef6119ee2c13b18f12fcb5e", [
                              EffectParam("effects_adjust_speed", 0.184, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认18%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    圣诞彩球             = EffectMeta("圣诞彩球", True, "7399466878789242117", "7399466878789242117", "190081444f1ae7df1b3b7ec148af4d45", [
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认25%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_number: 默认0%, 0% ~ 100%"""
    圣诞明信片           = EffectMeta("圣诞明信片", True, "7445221319781650961", "7445221319781650961", "f3e9fa3f91efcdec4d9521e800da3b98", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    圣诞派对             = EffectMeta("圣诞派对", True, "7399468161021611270", "7399468161021611270", "a5b8f7a13da0c2d2cd14149e6ba5de22", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.910, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认91%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    圣诞边框             = EffectMeta("圣诞边框", True, "7448891008437195280", "7448891008437195280", "67f5d6ad7ae49110f1fbb5fe49b0f412", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.003, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    在云端               = EffectMeta("在云端", True, "7409872890478202118", "7409872890478202118", "2c871332504a40b7dbe9e8e9e0c9283b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    地图剪切             = EffectMeta("地图剪切", True, "7518041757821586749", "7518041757821586749", "0f07581f7dae80ec70b87568b9ed1bbf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    地球变焦             = EffectMeta("地球变焦", True, "7532649023572921617", "7532649023572921617", "7dc1475941bc8759a1a40b4c0ed0be30", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    地铁涂鸦             = EffectMeta("地铁涂鸦", True, "7515090212142222645", "7515090212142222645", "6691f175741f977eafd0ff7d1c9832a3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    坏掉的电视_2         = EffectMeta("坏掉的电视 2", True, "7479298000917892405", "7479298000917892405", "ba8976cf3bf1f807d9d337b2ea58e6b5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    坚持模糊             = EffectMeta("坚持模糊", True, "7512637284684942645", "7512637284684942645", "627fee01a6d1d21b417e9b71abe8709d", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    城市交通             = EffectMeta("城市交通", True, "7514184828607073597", "7514184828607073597", "3405d485c0f90cc1122c338d60bbe57e", [
                              EffectParam("effects_adjust_speed", 0.111, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    堆叠屏幕             = EffectMeta("堆叠屏幕", True, "7517552590532414781", "7517552590532414781", "34e4fba1c398e0e041a6f836ec518d67", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    塑料包裹             = EffectMeta("塑料包裹", True, "7480960880474082621", "7480960880474082621", "73c5e3c93bd467dcc898590892d9d97d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    塑料封面             = EffectMeta("塑料封面", True, "7523971602581671221", "7523971602581671221", "9a173d256b9d240425190f5306cbc004", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    塑料花               = EffectMeta("塑料花", True, "7526790434895498549", "7526790434895498549", "21be1f8d7823cb6ac5865109e68d821a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    壁炉火光             = EffectMeta("壁炉火光", True, "7399466759058918662", "7399466759058918662", "6422961dbe02f34709668b2f7cac5ea7", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%"""
    声波涟漪             = EffectMeta("声波涟漪", True, "7521601391266123061", "7521601391266123061", "68d9c2a9cb95efc2739e0c3b819f5fa2", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认33%, 0% ~ 100%"""
    复制剪切             = EffectMeta("复制剪切", True, "7479786096788884789", "7479786096788884789", "da92601f98ef2638173e3e9319f980ca", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    复制堆叠             = EffectMeta("复制堆叠", True, "7522376386913307965", "7522376386913307965", "d190de4f6df1053ae95f6fe0a3670494", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复制幻灯片           = EffectMeta("复制幻灯片", True, "7460699936825330997", "7460699936825330997", "60866707e2f4acb37fc8f663f02f3861", [
                              EffectParam("effects_adjust_speed", 0.111, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    复古_DV_II           = EffectMeta("复古 DV II", True, "7399467763779046662", "7399467763779046662", "6979960d3bda8144b3406dee17e7255a", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    复古_DV_III          = EffectMeta("复古 DV III", True, "7399464865909312774", "7399464865909312774", "ff4ee88f3d727ac817750ae84df099cc", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    复古_DV_IV           = EffectMeta("复古 DV IV", True, "7399472232864435461", "7399472232864435461", "5fee9d2337a072ec018d77793b101aeb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认55%, 0% ~ 100%"""
    复古光盘             = EffectMeta("复古光盘", True, "7479082842736168245", "7479082842736168245", "16013b8982516dc41bf0fd133f53ac03", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认100%, 0% ~ 100%"""
    复古多屏             = EffectMeta("复古多屏", True, "7483775591108398342", "7483775591108398342", "1c36c53347a99106eedbaea051c1f6e4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    复古多格             = EffectMeta("复古多格", True, "7399463569366060294", "7399463569366060294", "19a3d5873d394ff550d6a4367ef18a45", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    复古录像带_III       = EffectMeta("复古录像带 III", True, "7399471143205276933", "7399471143205276933", "de0caa2ec7151990960b56f62fedd3fc", [])
    复古彩虹             = EffectMeta("复古彩虹", True, "7399471547548847366", "7399471547548847366", "e4e2be01974fb4c58c3cf3cb3795aa15", [
                              EffectParam("effects_adjust_size", 0.720, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认72%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 80%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认90%, 0% ~ 100%"""
    复古手机             = EffectMeta("复古手机", True, "7473710408818233857", "7473710408818233857", "80cb43f15a2fb7c18bd7421bd0fe1945", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复古投影仪           = EffectMeta("复古投影仪", True, "7493834309703404853", "7493834309703404853", "936b5cc3da073220ff9bcdfecce03db5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古撕纸             = EffectMeta("复古撕纸", True, "7414312242834935046", "7414312242834935046", "f9e0918d10b4442f3b919e241ab2b460", [])
    复古旧电视           = EffectMeta("复古旧电视", True, "7473710407337644560", "7473710407337644560", "fddf10c555bdeb00e6f8abc3dd471433", [])
    复古星光             = EffectMeta("复古星光", True, "7473014337687260469", "7473014337687260469", "d53d096457c5330d3f21e01141a1440b", [
                              EffectParam("effects_adjust_speed", 0.367, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认37%, 0% ~ 100%"""
    复古海报II           = EffectMeta("复古海报II", True, "7414191670725528837", "7414191670725528837", "27972940f34ff20c4af6dd4683c0597c", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    复古海报Ⅰ            = EffectMeta("复古海报Ⅰ", True, "7414191590572363013", "7414191590572363013", "31963f9f4aade5f74dc335614aacb550", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    复古游戏             = EffectMeta("复古游戏", True, "7459273669362191677", "7459273669362191677", "988672e44503703d5a6d93e8dc7d0145", [
                              EffectParam("effects_adjust_filter", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    复古漫画             = EffectMeta("复古漫画", True, "7399468748479925509", "7399468748479925509", "1f89b68447a46e9feb69654e4dc97a7f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古火花             = EffectMeta("复古火花", True, "7529129621820869941", "7529129621820869941", "c92aea27362c9c6b8496fc0ed5d9ac54", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复古甜心             = EffectMeta("复古甜心", True, "7399466693136895237", "7399466693136895237", "80dbaf8bbb2d7cecdaff271656a58126", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    复古电视             = EffectMeta("复古电视", True, "7488634466416577853", "7488634466416577853", "d2626ca5e2cbecef565c9ad6803a7b3e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复古电视机           = EffectMeta("复古电视机", True, "7449258379572154881", "7449258379572154881", "548f22047b7f7a55884c3b5efa25039d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复古碎钻             = EffectMeta("复古碎钻", True, "7399469847651962117", "7399469847651962117", "56f3d29724754f5fc9d50c7bf6c02e28", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    复古红调             = EffectMeta("复古红调", True, "7399465007848754437", "7399465007848754437", "22474ef534fe600e74348c17de3dff3e", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_sharpen: 默认70%, 0% ~ 100%"""
    复古胶片             = EffectMeta("复古胶片", True, "7399471002620611846", "7399471002620611846", "294e09ba63ed72dd245881d516f7a3c6", [
                              EffectParam("effects_adjust_speed", 0.301, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    复古蓝光             = EffectMeta("复古蓝光", True, "7473710407333483009", "7473710407333483009", "b5c26a7e8c684bd111de1b7018925fef", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    复古计算机           = EffectMeta("复古计算机", True, "7480795177490205957", "7480795177490205957", "eef46dd2ee0018c320de9892ab0ae758", [])
    复古负片效果         = EffectMeta("复古负片效果", True, "7482990427243597117", "7482990427243597117", "93d8075bbcb278a2f04a7c1f6016b8d1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    复古辉光             = EffectMeta("复古辉光", True, "7439647267235041808", "7439647267235041808", "d0e35be65f4fae73654b72609bc01edc", [])
    复古边框             = EffectMeta("复古边框", True, "7441466472951452177", "7441466472951452177", "62ce0da2496c633476e7fc2f11a22578", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    复古连拍             = EffectMeta("复古连拍", True, "7399466693136829701", "7399466693136829701", "154f59ff4dd71886d96aa36391656a64", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.160, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认16%, 0% ~ 100%"""
    复古闪切             = EffectMeta("复古闪切", True, "7524909530036112657", "7524909530036112657", "7fbb6d27775b3b9a0ac7ff66eecf63be", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    复古马赛克           = EffectMeta("复古马赛克", True, "7460764360382663989", "7460764360382663989", "e44278c80c79b1056a74c0499e26dcb7", [
                              EffectParam("effects_adjust_blur", 0.505, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    夕阳                 = EffectMeta("夕阳", True, "7399471547548699910", "7399471547548699910", "766398e7682640dc13bceb3f448847dc", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    多图快闪             = EffectMeta("多图快闪", True, "7522414591452679441", "7522414591452679441", "dbca02acbfcbfb8563892dee022493c7", [])
    多屏抖动             = EffectMeta("多屏抖动", True, "7509337222638783760", "7509337222638783760", "8310c6afb3263c0c0e535e1ecb1d2c04", [])
    多屏波普             = EffectMeta("多屏波普", True, "7395467370757721349", "7395467370757721349", "5131af04f764ffe264875b01c9b06999", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认40%, 0% ~ 100%
    effects_adjust_sharpen: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    多彩爱心             = EffectMeta("多彩爱心", True, "7464124620363272721", "7464124620363272721", "1993ba67d419dd24c63f0191ac4b8872", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    多机位               = EffectMeta("多机位", True, "7497008208700132624", "7497008208700132624", "38dd39a7d181e8e9ed942a25caf88a23", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    多种大小             = EffectMeta("多种大小", True, "7532810601920236853", "7532810601920236853", "dc0873a909ca497f5798fa87aacb897c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    多边形狂欢           = EffectMeta("多边形狂欢", True, "7506922226818485557", "7506922226818485557", "7be5512427be0f574296844be71c532c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    夜店弹跳             = EffectMeta("夜店弹跳", True, "7517134229700988213", "7517134229700988213", "a59c0b53d8f2b058aadfa21cce5527de", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    夜店氛围             = EffectMeta("夜店氛围", True, "7514946259543723317", "7514946259543723317", "1d26baa9c025a820698eedcd7d080c1c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    夜视电光             = EffectMeta("夜视电光", True, "7399470107455524101", "7399470107455524101", "e54419b9b13812271cd0dabd6cbca706", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    天使光辉             = EffectMeta("天使光辉", True, "7505300731801505077", "7505300731801505077", "1b496b6e462855d453a8f892df3dcc77", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.231, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认23%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%"""
    天堂之阳             = EffectMeta("天堂之阳", True, "7498261013754662205", "7498261013754662205", "03bdc7aa392e4bf14345f8b7f19a9090", [
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    天空裂缝             = EffectMeta("天空裂缝", True, "7508755342851984701", "7508755342851984701", "864dfca6b92d48a8fd432f2de305a801", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    天际扫描             = EffectMeta("天际扫描", True, "7495417415128452405", "7495417415128452405", "4015a7ac8c2f3bb9d188126e8602f0b4", [
                              EffectParam("effects_adjust_speed", 0.260, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认26%, 0% ~ 100%"""
    失去焦点             = EffectMeta("失去焦点", True, "7507101423780236605", "7507101423780236605", "36a44c357702f8e891fb5115b6f9f56d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    失焦光斑             = EffectMeta("失焦光斑", True, "7399469706563898629", "7399469706563898629", "e3e00d490d819edb7f33cf690a7a24e0", [
                              EffectParam("effects_adjust_size", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.340, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认12%, 0% ~ 100%
    effects_adjust_number: 默认85%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%"""
    夸张信号             = EffectMeta("夸张信号", True, "7451535587812577793", "7451535587812577793", "887f0d435a6721395ac38d90bcd1bfec", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    好莱坞光效           = EffectMeta("好莱坞光效", True, "7486772503474457917", "7486772503474457917", "d4d129d694b3ebd0363cc01b87276d4e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.602, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%"""
    安全摄像             = EffectMeta("安全摄像", True, "7486017789115878717", "7486017789115878717", "860b408a80c2e13d0c693ef64e6ab641", [
                              EffectParam("effects_adjust_vertical_shift", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认20%, 0% ~ 100%"""
    定格旋转木马_2       = EffectMeta("定格旋转木马 2", True, "7483778382082166069", "7483778382082166069", "973371af18ace7098284000be6876817", [
                              EffectParam("effects_adjust_blur", 0.615, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认62%, 0% ~ 100%"""
    实况开幕             = EffectMeta("实况开幕", True, "7399466247596936454", "7399466247596936454", "58a0d76b10a23a76f1d7834f097e888a", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%"""
    对角挤压             = EffectMeta("对角挤压", True, "7497204107288022325", "7497204107288022325", "1cd96db1c6e30be91a4338696d6f9a1a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    导演剪辑版           = EffectMeta("导演剪辑版", True, "7528813459690081589", "7528813459690081589", "1e89251795878937827fed3ef9330bfc", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    小心心表情符号       = EffectMeta("小心心表情符号", True, "7469361638982831421", "7469361638982831421", "4c88b6c34608bc3872290770b8618db2", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    小熊软糖             = EffectMeta("小熊软糖", True, "7483774735470398775", "7483774735470398775", "e7f0ec449bc26a9358b2a3df3481798f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    少女心事             = EffectMeta("少女心事", True, "7399467964358987014", "7399467964358987014", "ebba75bb53013a6347814b486c6063eb", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    尘光飞舞             = EffectMeta("尘光飞舞", True, "7511984393448099089", "7511984393448099089", "4cce39654a7e4df2b925dc1221f5a6f2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    局部上色             = EffectMeta("局部上色", True, "7526976548163816765", "7526976548163816765", "92307904af1d69ab073d2e2b23042da7", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    局部变色             = EffectMeta("局部变色", True, "7399471076859841797", "7399471076859841797", "62581bf77c3ea4f90eafbbc1115fefea", [
                              EffectParam("effects_adjust_range", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认95%, 0% ~ 100%
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_number: 默认35%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    局部推镜             = EffectMeta("局部推镜", True, "7399466635947445510", "7399466635947445510", "a607e28c273a94691df816231b0d5f3c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认40%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    层压效果             = EffectMeta("层压效果", True, "7525372064027413813", "7525372064027413813", "c3ca934459e85a96574b27833fd6a38f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    层叠                 = EffectMeta("层叠", True, "7490556430102170933", "7490556430102170933", "b4576571e73da995a3536579d8565924", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    层层冲击             = EffectMeta("层层冲击", True, "7498202618158681361", "7498202618158681361", "3b56f72f7c6d1e3828e20284131f582b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    层层飞近             = EffectMeta("层层飞近", True, "7512316287184325949", "7512316287184325949", "56b271878c2c15503ba49e29e803ff07", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    层次叠加             = EffectMeta("层次叠加", True, "7496717523937709329", "7496717523937709329", "f075a2bd92a185b2237f417e395a3866", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    居中闪切             = EffectMeta("居中闪切", True, "7399469731901705478", "7399469731901705478", "98283327a415b5719ca3bec1c713b707", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认0%, 0% ~ 100%"""
    屏幕暴雪             = EffectMeta("屏幕暴雪", True, "7509452824061676853", "7509452824061676853", "f573fa5ebbab61f2c9acc350b7cfb938", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    屏幕裂纹             = EffectMeta("屏幕裂纹", True, "7498695515748535605", "7498695515748535605", "ebebc94f34fa86d7d2edcb10e86ddd0c", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    屏幕通知             = EffectMeta("屏幕通知", True, "7478712838630985013", "7478712838630985013", "b44639e970463436c19c137571b2e0bd", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    岩石光感             = EffectMeta("岩石光感", True, "7528325987835088181", "7528325987835088181", "745094ab33729b740853ca3da1e93fcf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    岩石幻灯片           = EffectMeta("岩石幻灯片", True, "7504696804500360509", "7504696804500360509", "cce66d2a5e18fcea63e8d084f0df9aae", [
                              EffectParam("effects_adjust_speed", 0.111, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    岩石节拍             = EffectMeta("岩石节拍", True, "7515256131032223029", "7515256131032223029", "4d4e670ec1c737e12a3a9363cb5462f9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    左右微摇             = EffectMeta("左右微摇", True, "7509685071922662673", "7509685071922662673", "435ab7cf2f014a771a5bdffa6fbf3533", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    左右甩入             = EffectMeta("左右甩入", True, "7508553205966458128", "7508553205966458128", "04dd6707e67e9055452ad13cdf5594d7", [])
    巫师的光环           = EffectMeta("巫师的光环", True, "7519835821340364085", "7519835821340364085", "2ceb7e305fc375d5a086a30443b1c902", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    布拉格               = EffectMeta("布拉格", True, "7399471414518058246", "7399471414518058246", "a4d7d0dcf515869826f497d358b738fa", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    布艺涂鸦             = EffectMeta("布艺涂鸦", True, "7510536730831752509", "7510536730831752509", "784a0f97b319ddf019185d58de582f22", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    平拉放大             = EffectMeta("平拉放大", True, "7512252310995619089", "7512252310995619089", "c35d06198273506f4b5a0a1d51f8f88f", [])
    平滑复制             = EffectMeta("平滑复制", True, "7524255549089910077", "7524255549089910077", "53db2c9b026f8dc1a42b903308bd2dfd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    平铺视图旋转         = EffectMeta("平铺视图旋转", True, "7529847154240687421", "7529847154240687421", "95ce77840d3954d90bdc3563ab46aea7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    幻境漂移             = EffectMeta("幻境漂移", True, "7519366620800617729", "7519366620800617729", "8b4606ca0f424b6a561d6b2fe1f8921a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    幻彩故障             = EffectMeta("幻彩故障", True, "7399463349232389381", "7399463349232389381", "8032aeef1ca2ed78d0e0a2337d1ef042", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    幻影                 = EffectMeta("幻影", True, "7399464110456425734", "7399464110456425734", "44cb0b2f810fa3119f2c9f1ae396db9d", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    幻影缩放             = EffectMeta("幻影缩放", True, "7524605926989466941", "7524605926989466941", "61fe726f67f8bfaf72722e0ff6091868", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    幻影节拍             = EffectMeta("幻影节拍", True, "7529563100652096829", "7529563100652096829", "a4ac93367b9cb20d27cf461b6384b320", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    幻术摇摆             = EffectMeta("幻术摇摆", True, "7399468486642175237", "7399468486642175237", "3bb76ef02392a04f5b387dbd46942458", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    幻觉                 = EffectMeta("幻觉", True, "7399468710634818821", "7399468710634818821", "81244293ba7904eda4db87d1f8c59674", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    幻觉_II              = EffectMeta("幻觉 II", True, "7429591644795572752", "7429591644795572752", "3060aba349dbdf58c4a44c06843c8ad3", [
                              EffectParam("effects_adjust_speed", 0.120, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.050, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认12%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_soft: 默认5%, 0% ~ 100%"""
    幽影摇摆             = EffectMeta("幽影摇摆", True, "7524914764363926837", "7524914764363926837", "5aedc30464a1c255f4a09aa0886d4d3a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    幽灵鬼影             = EffectMeta("幽灵鬼影", True, "7520092993739574529", "7520092993739574529", "10307528e5a75c78ab97fac30c58cbd4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    广告故障             = EffectMeta("广告故障", True, "7486720570810191165", "7486720570810191165", "c00dffedeb2e3116ae4fce7af8242bdf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    广告故障_2           = EffectMeta("广告故障 2", True, "7493312550243732797", "7493312550243732797", "c00dffedeb2e3116ae4fce7af8242bdf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    广角畸变             = EffectMeta("广角畸变", True, "7399464944888057094", "7399464944888057094", "e282b9d0c816b5fa83c9099e72e1ab7b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认25%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认55%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    底部摇晃             = EffectMeta("底部摇晃", True, "7511715236311764277", "7511715236311764277", "0f67d604574ee4522e0a42562a316000", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    开关                 = EffectMeta("开关", True, "7519827768650108213", "7519827768650108213", "2f8fad036583ffe09da268a817aa5c11", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    开门                 = EffectMeta("开门", True, "7509022553411800321", "7509022553411800321", "99fb747ae85d0792e9d5816c896e0961", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%
    effects_adjust_texture: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    弧形丝滑滑动         = EffectMeta("弧形丝滑滑动", True, "7495961262099090704", "7495961262099090704", "0c630206f8a6b55cdebf01d95efdf5de", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    弧形开幕             = EffectMeta("弧形开幕", True, "7508922327808167169", "7508922327808167169", "eadfafcbf94451c907fda9a9f6308ce7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    弯曲透镜             = EffectMeta("弯曲透镜", True, "7459974908693531957", "7459974908693531957", "b2339c162fa8543eac76f7e063ed32a1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    弹出卡片             = EffectMeta("弹出卡片", True, "7509725394895899965", "7509725394895899965", "ce13a67bf90f1adcba9f683225762a76", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.010, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认1%, 0% ~ 100%"""
    弹出图框             = EffectMeta("弹出图框", True, "7528444042552626485", "7528444042552626485", "1cb9a3bfc8abd62a4887f837ebce78ae", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    弹出猫咪             = EffectMeta("弹出猫咪", True, "7530286087873269045", "7530286087873269045", "f4c568441a1297f72a74a2c71483cba8", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    弹弓相机             = EffectMeta("弹弓相机", True, "7460726978069400885", "7460726978069400885", "eae9b8155526868c700c299db16c4102", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    弹跳聚焦             = EffectMeta("弹跳聚焦", True, "7519781610212904245", "7519781610212904245", "ef004d500a448053cf502e9cd12f08aa", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    弹闪                 = EffectMeta("弹闪", True, "7399465722587450629", "7399465722587450629", "a852817db39ecb51dd2217523a53a032", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    弹震运镜             = EffectMeta("弹震运镜", True, "7399465788387773701", "7399465788387773701", "80e4086c6478ade8690a96c80d2e549e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认67%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    强速频闪             = EffectMeta("强速频闪", True, "7512634129205234945", "7512634129205234945", "68b6df39e8d5eaa9e2dad53db80b387d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    强震频闪             = EffectMeta("强震频闪", True, "7509706816587205905", "7509706816587205905", "5a2a6a968867dec154b810954ee57cb7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    强震黑框             = EffectMeta("强震黑框", True, "7511592872546716944", "7511592872546716944", "f9af3ee80265ae4511b2143137a49212", [])
    录像带               = EffectMeta("录像带", True, "7399467020506402053", "7399467020506402053", "c880d7f9eb6b4f94bf4e8f790fcf3dc0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认45%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认40%, 0% ~ 100%"""
    录像带_II            = EffectMeta("录像带 II", True, "7399464424576470278", "7399464424576470278", "12b20ba900b09a9cd833ffb15eec5f74", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    录像带恐慌           = EffectMeta("录像带恐慌", True, "7519065506989624637", "7519065506989624637", "996ad71c69308c3f77e20966e096a5f3", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    录像机               = EffectMeta("录像机", True, "7399466115899985158", "7399466115899985158", "f05977a18144296bdfa45ca3493d84a9", [])
    录像机边框           = EffectMeta("录像机边框", True, "7475631107128431120", "7475631107128431120", "9882be77427403de4e6294630e4b7aed", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    录制框               = EffectMeta("录制框", True, "7399470654237510918", "7399470654237510918", "3141b3cd5f3b7f5035020cb6466bfd5b", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认100%, 0% ~ 100%"""
    录制边框_II          = EffectMeta("录制边框 II", True, "7399470420526697733", "7399470420526697733", "05df74c3ef64c5ec8c97e7fef2caf46f", [])
    彩光幻影             = EffectMeta("彩光幻影", True, "7429186347430056465", "7429186347430056465", "2fd370f94d00285e5b49c2ecb3b2d23f", [
                              EffectParam("effects_adjust_speed", 0.474, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认47%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    彩光摇晃             = EffectMeta("彩光摇晃", True, "7399470385282026758", "7399470385282026758", "0e4016769c0b63e4a9e850d55d406d62", [
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认65%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认75%, 0% ~ 100%"""
    彩光流动_II          = EffectMeta("彩光流动 II", True, "7395472454346378501", "7395472454346378501", "eb006a9670d27e811c07bd7b689bbd99", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认3%, 0% ~ 100%
    effects_adjust_blur: 默认65%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    彩光流动_III         = EffectMeta("彩光流动 III", True, "7399467387038338310", "7399467387038338310", "98cae4ab9a4ae29ad83821f6b4629516", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认60%, 0% ~ 100%"""
    彩屏重影             = EffectMeta("彩屏重影", True, "7514860025546820865", "7514860025546820865", "106011e16273b329e8e1382fa2696093", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩带球               = EffectMeta("彩带球", True, "7399469985845808390", "7399469985845808390", "6ee2e117bfe728f1ca634e9f11a9f12c", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    彩幕展开             = EffectMeta("彩幕展开", True, "7521451308101029137", "7521451308101029137", "64e776b0340dcac7d95cc43c86105877", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩斑变焦             = EffectMeta("彩斑变焦", True, "7399471234192346373", "7399471234192346373", "1894598788c53e50431999e1964eb593", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.050, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认5%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    彩绘星星             = EffectMeta("彩绘星星", True, "7405166985262238981", "7405166985262238981", "a20eed3f4aca3150ff23e4d930634c0d", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    彩色Kira             = EffectMeta("彩色Kira", True, "7399471609624415493", "7399471609624415493", "1028af857b6bd15b408af36268f6635e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    彩色kira_II          = EffectMeta("彩色kira II", True, "7399466236188380421", "7399466236188380421", "a96fb9394be78b6d3e0de8efd8e86cf3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.753, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认75%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色像素             = EffectMeta("彩色像素", True, "7399468230848351493", "7399468230848351493", "8073d46c5c3b46cee867e6a3c0f86154", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.270, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认15%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认70%, 0% ~ 100%
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认27%, 0% ~ 100%"""
    彩色像素排序         = EffectMeta("彩色像素排序", True, "7395470361514560774", "7395470361514560774", "a0b46f005c19589d83743e33b8f7f05c", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认65%, 0% ~ 100%
    effects_adjust_color: 默认15%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色射线             = EffectMeta("彩色射线", True, "7486721948613954821", "7486721948613954821", "047719da706911c5c022601c529b406f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色影调             = EffectMeta("彩色影调", True, "7532391610819153213", "7532391610819153213", "6a132467278c2abed954869ae62c69e2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    彩色拖影             = EffectMeta("彩色拖影", True, "7399468898019527942", "7399468898019527942", "29d68043b21ce8a983b57ef5e73d6aef", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    彩色泼墨             = EffectMeta("彩色泼墨", True, "7405166447703461125", "7405166447703461125", "866a314c12ec66129742d15af3a24fb1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认30%, 0% ~ 100%"""
    彩色漫画             = EffectMeta("彩色漫画", True, "7399464864567151878", "7399464864567151878", "f80405484a283ecdc708c9bcd4e2a8d2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    彩色火焰             = EffectMeta("彩色火焰", True, "7399470557198224645", "7399470557198224645", "2a83206eb7f6f9d65af177a29ea223e2", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    彩色碎彩             = EffectMeta("彩色碎彩", True, "7395471949666848006", "7395471949666848006", "19e11d01cb81636297334c4a9e57991e", [
                              EffectParam("effects_adjust_speed", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认58%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    彩色碎闪             = EffectMeta("彩色碎闪", True, "7447050777173955089", "7447050777173955089", "2c31ede8085c9a6970a50639e2be1efd", [
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认66%, 0% ~ 100%
    effects_adjust_size: 默认65%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%"""
    彩色胶片             = EffectMeta("彩色胶片", True, "7399468004527967493", "7399468004527967493", "3c765f5eddfa9c3c451b0b219dec804f", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.510, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认51%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    彩色胶片_I           = EffectMeta("彩色胶片 I", True, "7405165908559219973", "7405165908559219973", "e8dabb72421c2773120bfc6d4d3785f0", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    彩色蝴蝶             = EffectMeta("彩色蝴蝶", True, "7399466682822970629", "7399466682822970629", "aaabe838a4c6a61d6018002854acbc6d", [])
    彩色负片             = EffectMeta("彩色负片", True, "7399470435060026630", "7399470435060026630", "a78b49205a5d3b7fbc04a19aebce80ea", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    彩色边缘             = EffectMeta("彩色边缘", True, "7399471864768187654", "7399471864768187654", "16ab73c82bb6f76bc2fba79f9dbd2650", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    彩色闪烁             = EffectMeta("彩色闪烁", True, "7399470719085595910", "7399470719085595910", "713fb74b0302a60142831084ef59584c", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认25%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩色雪花             = EffectMeta("彩色雪花", True, "7449401553254879745", "7449401553254879745", "510005a5c6cffd42ad6eb21b2a056aef", [
                              EffectParam("effects_adjust_color", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认75%, 0% ~ 100%
    effects_adjust_number: 默认66%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%"""
    彩虹光影             = EffectMeta("彩虹光影", True, "7399472645198073094", "7399472645198073094", "8a0b7b5798e7c211e9d1e404403c948b", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认40%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认66%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    彩虹棱镜             = EffectMeta("彩虹棱镜", True, "7395472908765662469", "7395472908765662469", "9a077856a5228a5e93d58b3610a1300f", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 100%"""
    彩虹气泡             = EffectMeta("彩虹气泡", True, "7399470727121947910", "7399470727121947910", "ae2e32daa7af0fa8f4b61a0c5aacd196", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    彩虹泛光             = EffectMeta("彩虹泛光", True, "7395475703916924166", "7395475703916924166", "75a2d417b48815ffec602d06baa28e02", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%"""
    彩虹立方体           = EffectMeta("彩虹立方体", True, "7521486648241163521", "7521486648241163521", "9ebaa08bdf65be9c751461af381965de", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    彩虹色差             = EffectMeta("彩虹色差", True, "7527473561934581009", "7527473561934581009", "20697ef0cfc16ce05bf6aabc299225ca", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%"""
    彩虹贴纸             = EffectMeta("彩虹贴纸", True, "7474891560170048821", "7474891560170048821", "57090d5eab88aaed005a91ded38a2982", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    彩虹闪屏             = EffectMeta("彩虹闪屏", True, "7399469653493370118", "7399469653493370118", "aaeae77e0c74db18769bd2cbab83360a", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    影印                 = EffectMeta("影印", True, "7522434271777230133", "7522434271777230133", "450eedf8a8c72106c2a7c590d136f0c1", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    循环训练             = EffectMeta("循环训练", True, "7522676162380795189", "7522676162380795189", "6a5f08d41de3fd63681a74af5b6cfe1b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.667, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认67%, 0% ~ 100%"""
    微型三重奏           = EffectMeta("微型三重奏", True, "7516172452024683829", "7516172452024683829", "be9f9a98b77cc6c08b91002ee64296f6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    微扭边框             = EffectMeta("微扭边框", True, "7509330282667855120", "7509330282667855120", "5a100c34a5001fb16cd51f7ab55fcca2", [])
    微震抖动             = EffectMeta("微震抖动", True, "7507110964391709968", "7507110964391709968", "866334f8dd74eee2bb4f911b969b290b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    微震闪黑             = EffectMeta("微震闪黑", True, "7395467839634803974", "7395467839634803974", "28471a0d035b66c5b99d954cbcbf496a", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认20%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%"""
    心形气泡             = EffectMeta("心形气泡", True, "7464280304824454461", "7464280304824454461", "33f064ff0646fe2057e78cebdb396e01", [
                              EffectParam("effects_adjust_size", 0.510, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.502, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.502, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认51%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    心形波纹             = EffectMeta("心形波纹", True, "7468305429152501053", "7468305429152501053", "5161b6106e09782b07f8d5ef2c85b438", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    心灵萌芽             = EffectMeta("心灵萌芽", True, "7465973693387181365", "7465973693387181365", "0359165ce195dd266e7acdd0ff1be53b", [
                              EffectParam("effects_adjust_speed", 0.474, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认47%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    心磁铁               = EffectMeta("心磁铁", True, "7475976912884518205", "7475976912884518205", "0718ae8da412c9a4e5e7039ab6b4b7d4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    心花怒放II           = EffectMeta("心花怒放II", True, "7448891008441405953", "7448891008441405953", "602d96dfa15a42e76945665b3b958ef4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    心跳_II              = EffectMeta("心跳 II", True, "7399469332314557701", "7399469332314557701", "e940e6b4377d03450c4a53ab618b99f0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.360, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认36%, 0% ~ 100%"""
    心跳之光_2           = EffectMeta("心跳之光 2", True, "7470641533029469493", "7470641533029469493", "756e829ed84c9b188ac461053af849a5", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    快照冲击波           = EffectMeta("快照冲击波", True, "7515363961919819061", "7515363961919819061", "8737e551b861f4e17a0407723e400bda", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    快照旋转             = EffectMeta("快照旋转", True, "7531986144125308213", "7531986144125308213", "1034efb0e11c0c94bf1164eead6f6b5e", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    快速变焦             = EffectMeta("快速变焦", True, "7395471447835151622", "7395471447835151622", "67d6996f98e260bded2ce9e06caa426c", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.285, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认28%, 0% ~ 100%"""
    快速条纹             = EffectMeta("快速条纹", True, "7477492852923043125", "7477492852923043125", "76fbb55f3022215debdc00d3286373b3", [
                              EffectParam("effects_adjust_speed", 0.474, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认47%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%"""
    快速模糊             = EffectMeta("快速模糊", True, "7514974587516390709", "7514974587516390709", "3d08ad675c3bf81f5b12062081e4f5da", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    快速缩放             = EffectMeta("快速缩放", True, "7516888804041493821", "7516888804041493821", "f1c81aa9d9ea0268e9cdfc77006d91c2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    快门闪光             = EffectMeta("快门闪光", True, "7486377481189051701", "7486377481189051701", "88a480fa0ea9fbe9fc540a4fc01f401b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    快闪运镜             = EffectMeta("快闪运镜", True, "7399464570751896837", "7399464570751896837", "4e85edcb46572136ce3343e9cdc197d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    怀旧浪漫喜剧         = EffectMeta("怀旧浪漫喜剧", True, "7470069413597777213", "7470069413597777213", "281d99ee1be572618881c6804be72948", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    怀旧边框             = EffectMeta("怀旧边框", True, "7399472290288733446", "7399472290288733446", "23af10c231cf1b88104e206ca5b6d9ad", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.660, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认66%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    怦然心动             = EffectMeta("怦然心动", True, "7399471803325893893", "7399471803325893893", "d5e216a1700db22637509d2966004b16", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    恍惚扭动             = EffectMeta("恍惚扭动", True, "7508042552801496381", "7508042552801496381", "67f881f1caa8cbbff6ab0ecbd17890db", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    恐怖故障             = EffectMeta("恐怖故障", True, "7426268842642379265", "7426268842642379265", "1f7b111effe937c3ec574a0791866cf9", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    恐怖来袭             = EffectMeta("恐怖来袭", True, "7524943663663762749", "7524943663663762749", "b4a1b986906bd2776b89a0efda01daa6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    恐怖涂鸦             = EffectMeta("恐怖涂鸦", True, "7399471803325795589", "7399471803325795589", "b37405a2ca50f0059744dae5b66ff997", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.220, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认22%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%"""
    恐慌频率             = EffectMeta("恐慌频率", True, "7505394826679045429", "7505394826679045429", "d0b17e98f6d5540ce4d2806fb0301466", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    情人节拼贴           = EffectMeta("情人节拼贴", True, "7464124622095520257", "7464124622095520257", "6f6607e42b78bde3c93ee862084f3894", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    情感分离             = EffectMeta("情感分离", True, "7508609132996365629", "7508609132996365629", "644d589e8458edf9b5654a3b59b4e6ea", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    情绪照片拼贴         = EffectMeta("情绪照片拼贴", True, "7517552540054015293", "7517552540054015293", "6f0bec56a2d9eb07025a1c6fc82224a1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    慢动作回声           = EffectMeta("慢动作回声", True, "7529872002216201533", "7529872002216201533", "3afd8a9f9588344afa6a9b225bc0a7d7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    慢动作摇摆           = EffectMeta("慢动作摇摆", True, "7511956428412702005", "7511956428412702005", "c89c233c8f7477cd74647d278d4f9a4b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    慢速快门             = EffectMeta("慢速快门", True, "7467184538821676341", "7467184538821676341", "e3cc4e5c376431b1d12c021cfa856866", [
                              EffectParam("effects_adjust_intensity", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    戏剧性旋转           = EffectMeta("戏剧性旋转", True, "7511948906679323965", "7511948906679323965", "623acb043ee6569f6077f514809924ec", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%"""
    手写日记             = EffectMeta("手写日记", True, "7399466667740318982", "7399466667740318982", "3490d85dc21f18ce5095832bf0d011a6", [
                              EffectParam("effects_adjust_color", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    手写边框             = EffectMeta("手写边框", True, "7399471013567810822", "7399471013567810822", "1562db9ef86c866cdd951885f1fa26f4", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.260, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认26%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%"""
    手持相机             = EffectMeta("手持相机", True, "7506549736204209461", "7506549736204209461", "6637fa99457b43aa65844d9f63543b4a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    手持运镜             = EffectMeta("手持运镜", True, "7436323942198940177", "7436323942198940177", "e83d397fd1b2c5fc0a3099a9a535c493", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    手绘小爱心           = EffectMeta("手绘小爱心", True, "7470416935671304720", "7470416935671304720", "fd9093b51597eecaaa332089fcfb6be1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    手绘星星             = EffectMeta("手绘星星", True, "7414311971358625029", "7414311971358625029", "5d0ee2a934b6d34920f01333ff2bcf00", [])
    手绘边框_III         = EffectMeta("手绘边框 III", True, "7399464038050123013", "7399464038050123013", "3e38e4db50217711e54dba3a3c284a6e", [])
    打开文件夹           = EffectMeta("打开文件夹", True, "7506742039782968629", "7506742039782968629", "91ef468081fb4edf83ca50848cf356ae", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    扫描复制             = EffectMeta("扫描复制", True, "7522707031837396277", "7522707031837396277", "04b2a40dd5173dd818e549226a82fcee", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    扫描展开             = EffectMeta("扫描展开", True, "7522413719364603152", "7522413719364603152", "f546c4bd70e2a2e872075e7b2d041ec9", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    扫描条               = EffectMeta("扫描条", True, "7502042778424085813", "7502042778424085813", "ebde521db6599b133e032c157feaac7f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    扭曲360              = EffectMeta("扭曲360", True, "7497820604922350865", "7497820604922350865", "f3e06e9fe9a92203621513b382af577c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    扭曲光感             = EffectMeta("扭曲光感", True, "7528023198005284149", "7528023198005284149", "35bfb84e80086b5a5a308c700e33e5ba", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    扭曲变焦             = EffectMeta("扭曲变焦", True, "7399467283006885126", "7399467283006885126", "643635cac6435ea88dd6c4a9ae91303f", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认20%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%"""
    扭曲旋入             = EffectMeta("扭曲旋入", True, "7395473622036450566", "7395473622036450566", "cc9bb0039ebba34a0951ff9c9b8118c4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    扭曲模糊             = EffectMeta("扭曲模糊", True, "7399469330183834885", "7399469330183834885", "a48e3fb197688fb20a959a961ab54383", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.455, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    扭曲缩放             = EffectMeta("扭曲缩放", True, "7522869574816107837", "7522869574816107837", "8f233c5206854a07538b646ab3d77fc6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    找到的影像           = EffectMeta("找到的影像", True, "7525746943327325501", "7525746943327325501", "ba53665428298d84ffb28a3c61bb4f5b", [
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    投影文字             = EffectMeta("投影文字", True, "7399471982066158854", "7399471982066158854", "46a3a7dbb114d888726b1cf9a22189c2", [
                              EffectParam("effects_adjust_soft", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_soft: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    抖动图框             = EffectMeta("抖动图框", True, "7523173891750055221", "7523173891750055221", "bc34c3599ded62f69f14fff382af5f4b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    抖动微闪             = EffectMeta("抖动微闪", True, "7486351825986260229", "7486351825986260229", "6463de0eeaa304346f3b6754e38f7ffe", [])
    抖动模糊             = EffectMeta("抖动模糊", True, "7395471669403356421", "7395471669403356421", "416a2f55681bf6951f25fd3c7336025b", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认20%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    抖动轮廓             = EffectMeta("抖动轮廓", True, "7476368425137343805", "7476368425137343805", "202f1c8a6935479d7f1aae247e0a801c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    抖动闪光             = EffectMeta("抖动闪光", True, "7517146109832072501", "7517146109832072501", "37078da012653a533c8c918c747f3b8c", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    折射光效             = EffectMeta("折射光效", True, "7491138615477685505", "7491138615477685505", "5b7a93fc0ffd188dedb3285340566f3b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    折痕                 = EffectMeta("折痕", True, "7399470789449256198", "7399470789449256198", "be4f37157bcaebf356e467050cf11248", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    折痕_II              = EffectMeta("折痕 II", True, "7399466759058902278", "7399466759058902278", "4efd4758f897b1d364549a688129e5d5", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    折痕_IV              = EffectMeta("折痕 IV", True, "7399464110456360198", "7399464110456360198", "b04966da3a2bbd9212aec61aaa995c33", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    折痕_V               = EffectMeta("折痕 V", True, "7399471609624530181", "7399471609624530181", "1530211bc181cd4003243fa6265574db", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    折纸_2               = EffectMeta("折纸 2", True, "7472334602913238333", "7472334602913238333", "0ece1eb2b79eecf6c08ef3cf86739821", [
                              EffectParam("effects_adjust_speed", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    护目镜视角           = EffectMeta("护目镜视角", True, "7533054848783142197", "7533054848783142197", "e57f264845a680ee33ec910382bd5687", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    报纸图框             = EffectMeta("报纸图框", True, "7527962842973179189", "7527962842973179189", "b090d36a6bea78174498e5932a5fd5d5", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    抽帧                 = EffectMeta("抽帧", True, "7399470312338803973", "7399470312338803973", "9a8d046fca7227aa1dcee2fafafac3aa", [
                              EffectParam("effects_adjust_speed", 0.660, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认66%, 0% ~ 100%"""
    拉伸快照             = EffectMeta("拉伸快照", True, "7523503974264114493", "7523503974264114493", "a44fc5bf8ef5b4e9826555790e2ccafd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拉伸魅力             = EffectMeta("拉伸魅力", True, "7493970441934032189", "7493970441934032189", "340e55cf3b59f05064a97e5fbef09828", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拉扯震动             = EffectMeta("拉扯震动", True, "7399467640009313542", "7399467640009313542", "ee70831a3086bb249d63ec00d5ca56ec", [
                              EffectParam("effects_adjust_distortion", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    拉远拍摄             = EffectMeta("拉远拍摄", True, "7513654049846119733", "7513654049846119733", "8b1c2eebc1ede6f82f9cb08c90159d81", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拍摄与堆叠           = EffectMeta("拍摄与堆叠", True, "7524962479726759229", "7524962479726759229", "2f1f606722ecbb6d666fc5f31fafe5b7", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    拍立得展开           = EffectMeta("拍立得展开", True, "7519375393971866881", "7519375393971866881", "a8c62695aab194e6f70ee98415e93f66", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拍立得成像           = EffectMeta("拍立得成像", True, "7450373165223514625", "7450373165223514625", "604e8b68d502dfbde501c667a95d694f", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    拖动放大             = EffectMeta("拖动放大", True, "7519401268255755581", "7519401268255755581", "15f7743fbf97067d42e5aa423852cb49", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    拖尾震动             = EffectMeta("拖尾震动", True, "7485975886852852998", "7485975886852852998", "0d1d2078d4d3830affb265db926e5afd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拖拽残影             = EffectMeta("拖拽残影", True, "7519381450513255696", "7519381450513255696", "255e09f66a474f04bed2e32301ceece0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拼图聚焦             = EffectMeta("拼图聚焦", True, "7515055457845710141", "7515055457845710141", "b9b2dad881fdd2558aa544aa71e0bb85", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    拼接隧道             = EffectMeta("拼接隧道", True, "7512310471802850561", "7512310471802850561", "4e7b58207e347a988380167a3c7f4826", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认75%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    拼贴开幕             = EffectMeta("拼贴开幕", True, "7399471489407356166", "7399471489407356166", "642662963583875bbc36fa6ca6410300", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    指尖缩放             = EffectMeta("指尖缩放", True, "7480110410847276349", "7480110410847276349", "ec3c0e0d9afacaa5052d7cd3c86a16c1", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.789, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认20%, 0% ~ 100%
    effects_adjust_background_animation: 默认79%, 0% ~ 100%"""
    振动飘动             = EffectMeta("振动飘动", True, "7527700807240650037", "7527700807240650037", "5282fff7eb4e958a58d73698b2be69d5", [
                              EffectParam("effects_adjust_speed", 0.367, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认37%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    损坏的_VHS           = EffectMeta("损坏的 VHS", True, "7486808708974923069", "7486808708974923069", "1dfa1bbadacd1b2f8309a30275fd6157", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    推拉跟随             = EffectMeta("推拉跟随", True, "7395121264685255942", "7395121264685255942", "a6fb9367f095b33fa0047a43c2161e74", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    推拉运镜             = EffectMeta("推拉运镜", True, "7395472388068019461", "7395472388068019461", "4b123b8db48a337b91327c2871ca81e0", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.656, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.849, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认66%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认85%, 0% ~ 100%"""
    推近推远             = EffectMeta("推近推远", True, "7434830442265596433", "7434830442265596433", "946248ab05631310e821625cee0948bf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    推闪三切             = EffectMeta("推闪三切", True, "7508897852182039809", "7508897852182039809", "f74e67e43c8d3cd131f3aacf4c79b414", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    摄像机_II            = EffectMeta("摄像机 II", True, "7399470740849904902", "7399470740849904902", "666fa93e6436e1585725aa3e40de6ea0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_sharpen: 默认45%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认20%, 0% ~ 100%"""
    摆动镜头             = EffectMeta("摆动镜头", True, "7511750179385576765", "7511750179385576765", "e629aad35741f11fcc89f880ac78d86e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    摇摆缩放             = EffectMeta("摇摆缩放", True, "7527728287376870717", "7527728287376870717", "80354dbe29da6e5a78ee66a7f5630270", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    摇摇晃晃地离开       = EffectMeta("摇摇晃晃地离开", True, "7513872224684723517", "7513872224684723517", "6ef0d614f5edc43dc350739ed284ff34", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    摇晃叠影             = EffectMeta("摇晃叠影", True, "7399467240111820037", "7399467240111820037", "2f82ba674fd1d78a14ccb5d384ee3704", [
                              EffectParam("effects_adjust_speed", 0.350, 0.100, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 10% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    摇晃推镜             = EffectMeta("摇晃推镜", True, "7399467327726587141", "7399467327726587141", "2b806738c3a5e3126a2013cebc2c4913", [
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    摇晃故障             = EffectMeta("摇晃故障", True, "7526984676796288317", "7526984676796288317", "c96d32a5f53a140eb8301f156631eaec", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    摇晃运镜             = EffectMeta("摇晃运镜", True, "7399472023874948357", "7399472023874948357", "bbc5f812f50b8ea1aadb3fd6ac2dd6f0", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%"""
    摇晃闪光灯           = EffectMeta("摇晃闪光灯", True, "7493749901319294225", "7493749901319294225", "592e8dab05a7d692434ff0a866d05ec5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    摇晃高光             = EffectMeta("摇晃高光", True, "7509347237605018933", "7509347237605018933", "55be0ffcba52d3cee609a2fd7447aa0f", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    摇曳光环             = EffectMeta("摇曳光环", True, "7504864086899871029", "7504864086899871029", "98f50a074931ff5dddcb51e9afe02e85", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    摇曳蒸汽             = EffectMeta("摇曳蒸汽", True, "7524958205932227901", "7524958205932227901", "fa8c13a1fabf50b79ac5ac6654b96331", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    撒星星               = EffectMeta("撒星星", True, "7399465000148012293", "7399465000148012293", "620d63550356df332ba5c014b310d6d2", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    撕拉片               = EffectMeta("撕拉片", True, "7503832070628625680", "7503832070628625680", "22c5f1bb1aac02f195b226c2c8dd9ba6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.167, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认17%, 0% ~ 100%"""
    撕纸动画             = EffectMeta("撕纸动画", True, "7414191291866680582", "7414191291866680582", "f8be5e0de726d30e0577faf83fa64b71", [])
    撕纸特写             = EffectMeta("撕纸特写", True, "7399472736231296262", "7399472736231296262", "c322a330e87f550e0e56c7cef60e6465", [
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    播放预览             = EffectMeta("播放预览", True, "7528258800063696181", "7528258800063696181", "924373c11123a2de4358396548797196", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    擦拭开幕             = EffectMeta("擦拭开幕", True, "7399468304080866565", "7399468304080866565", "6725bf6b227fc208a7bd343661637320", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    收缩焦点             = EffectMeta("收缩焦点", True, "7520308884901350717", "7520308884901350717", "aa8f305d5033751b28fad1fef162405b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放大镜               = EffectMeta("放大镜", True, "7511971362802634045", "7511971362802634045", "b75032eb8eade89d304e621a18a03e41", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放大镜盘             = EffectMeta("放大镜盘", True, "7528015661021285693", "7528015661021285693", "a1eb6a07005e70504887c163fe0b1b94", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放大镜视角           = EffectMeta("放大镜视角", True, "7451525189998744080", "7451525189998744080", "31143fd0a3da22429e96c2540f45727c", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    放射幻影             = EffectMeta("放射幻影", True, "7399464226240204038", "7399464226240204038", "e65ddd069b55e2f0526c46e1fa5cecdc", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放射性脉冲           = EffectMeta("放射性脉冲", True, "7529063657527856445", "7529063657527856445", "d112efbea24ed913fb0b4257b70ca63a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    放映机               = EffectMeta("放映机", True, "7399471911815630085", "7399471911815630085", "a8bffa5b39a0ff0c1cdc278216e5041d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.339, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认34%, 0% ~ 100%"""
    故障                 = EffectMeta("故障", True, "7508677224195771701", "7508677224195771701", "68e826d0ea420f9812dac29d2fb6ab21", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    故障_II              = EffectMeta("故障 II", True, "7399466347505175813", "7399466347505175813", "7bf041bbfb782aba4937b4c439193c65", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    故障卡带             = EffectMeta("故障卡带", True, "7399467244809489670", "7399467244809489670", "9014b58720d1bd19b6a8f7f0bb6fdb98", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.520, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认10%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认52%, 0% ~ 100%"""
    故障定格             = EffectMeta("故障定格", True, "7395468486648007941", "7395468486648007941", "e49b4ad03485d3f6691552c5be1b3704", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    故障录像带           = EffectMeta("故障录像带", True, "7504708471930015037", "7504708471930015037", "df4797fe59e4475bea06863271477a3a", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    故障扫屏             = EffectMeta("故障扫屏", True, "7473044437107479057", "7473044437107479057", "ffa98ce26e73bfb89275004e72c286e0", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    故障散影             = EffectMeta("故障散影", True, "7514831154910924049", "7514831154910924049", "544e7999664d399458f72a3901687b67", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    故障线闪             = EffectMeta("故障线闪", True, "7413306494495494673", "7413306494495494673", "17bcfd51adffb2a1a6bf075679acd74d", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    故障遮蔽             = EffectMeta("故障遮蔽", True, "7501230333166161205", "7501230333166161205", "5221c6a05039c5319055e7e2506a1604", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    故障镜头             = EffectMeta("故障镜头", True, "7524652746767633725", "7524652746767633725", "6226c71ebc2ecd8c14b6f8d86c325918", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    故障闪爆             = EffectMeta("故障闪爆", True, "7529387629939395857", "7529387629939395857", "01aec9f297cafa3398b974e0dd8406dd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    故障震闪             = EffectMeta("故障震闪", True, "7399470704489516293", "7399470704489516293", "510623ce6e6c3d77151024fe04eb30dd", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.714, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认71%, 0% ~ 100%"""
    散景漏光             = EffectMeta("散景漏光", True, "7492970715730251009", "7492970715730251009", "1c79224e61d860ef6618d16aac2c53c6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    数字相机             = EffectMeta("数字相机", True, "7519063783034096949", "7519063783034096949", "22c7202f4e4669ef2baac40b818af1db", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    数字矩阵             = EffectMeta("数字矩阵", True, "7399473259604905222", "7399473259604905222", "933acfd32f6fa44785c5ba93e42cbc59", [
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认33%, 0% ~ 100%"""
    数学公式             = EffectMeta("数学公式", True, "7414191438621101318", "7414191438621101318", "7284cfce882721a774684ae37d3dc9b4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    数据加载故障         = EffectMeta("数据加载故障", True, "7511982836790906113", "7511982836790906113", "61788c04773242ebe29d0e65ab8f19c6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认10%, 0% ~ 100%
    effects_adjust_texture: 默认10%, 0% ~ 100%"""
    数码相机             = EffectMeta("数码相机", True, "7488615612252540221", "7488615612252540221", "c9e568244739d65559946dca462bf539", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    斜线震动             = EffectMeta("斜线震动", True, "7395466439181749509", "7395466439181749509", "154a4e843d36fe8660f15624a330d2a1", [
                              EffectParam("effects_adjust_size", 0.409, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.704, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.339, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认41%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认34%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    断裂胶带             = EffectMeta("断裂胶带", True, "7500893529300831541", "7500893529300831541", "3a1c8bed8639832d3fe0912d6d118d6a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    新年仙女棒           = EffectMeta("新年仙女棒", True, "7395473102366330118", "7395473102366330118", "d3e0b2bc815a17fcd0802507515d6223", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.480, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.780, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认48%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认78%, 0% ~ 100%
    effects_adjust_range: 默认55%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    新年烟花             = EffectMeta("新年烟花", True, "7460143756264672518", "7460143756264672518", "f7cf5ec7f6c00d06238237d05f024477", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%"""
    新年烟花_II          = EffectMeta("新年烟花 II", True, "7446313241287856641", "7446313241287856641", "09b16968309c9a38e7bf8f26a9eba800", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    方块剪辑             = EffectMeta("方块剪辑", True, "7529805795832171829", "7529805795832171829", "af1ad7bb48bdbeb8615e4563d3dccac1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认100%, 0% ~ 100%"""
    方形模糊             = EffectMeta("方形模糊", True, "7395470784166251782", "7395470784166251782", "0883434b90fbeaf428ac86a0f87cb4fe", [
                              EffectParam("effects_adjust_blur", 0.877, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认88%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_color: 默认25%, 0% ~ 100%
    effects_adjust_luminance: 默认45%, 0% ~ 100%"""
    旋切冲屏             = EffectMeta("旋切冲屏", True, "7512632938308160785", "7512632938308160785", "d793718fb3b0f21f7f9bcecc0ece3586", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋焦                 = EffectMeta("旋焦", True, "7399467964359118086", "7399467964359118086", "ee5c7f8a1180bd5d8e0d4da0357e8d99", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋转与重聚焦         = EffectMeta("旋转与重聚焦", True, "7533150521692147005", "7533150521692147005", "3ef5d8c1b249d090c865e3f6bf61400c", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    旋转发光             = EffectMeta("旋转发光", True, "7395473457980493061", "7395473457980493061", "46f6856d1b6c40a7d6b7c6da0ae24439", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认15%, 0% ~ 100%
    effects_adjust_filter: 默认15%, 0% ~ 100%"""
    旋转圆球             = EffectMeta("旋转圆球", True, "7395472351418207493", "7395472351418207493", "bc332eeb63f21a5f48f90221ed709196", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    旋转快门             = EffectMeta("旋转快门", True, "7511938091821649213", "7511938091821649213", "1a30654d3a04a4b9f8efc2a8e4d49f6f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋转捕捉             = EffectMeta("旋转捕捉", True, "7509168045361810749", "7509168045361810749", "0d4e0a679349748fd74a7a65ae1144e4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋转模糊             = EffectMeta("旋转模糊", True, "7395468643028585734", "7395468643028585734", "b5087e64a4e5859c71177c099beb93f3", [
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认33%, 0% ~ 100%"""
    旋转空间             = EffectMeta("旋转空间 ", True, "7399468404941344005", "7399468404941344005", "ab8caff5408905d424c23bef34af0853", [
                              EffectParam("effects_adjust_size", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认34%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_rotate: 默认67%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    旋转缩放             = EffectMeta("旋转缩放", True, "7514220948397018421", "7514220948397018421", "251cf77c2c1abad907bc6f0b5cea787f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋转透镜             = EffectMeta("旋转透镜", True, "7399472139495034118", "7399472139495034118", "c0756258b4e9670347a055216890cec1", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.080, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认8%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_noise: 默认20%, 0% ~ 100%
    effects_adjust_distortion: 默认80%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%"""
    旋转镜头             = EffectMeta("旋转镜头", True, "7509371880155925813", "7509371880155925813", "ba18d656c3c767e14fa65462f6005373", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    旋转雪花             = EffectMeta("旋转雪花", True, "7464575494168563005", "7464575494168563005", "4dd6665db8e1b9b2ca28620ed4fbc22d", [
                              EffectParam("effects_adjust_speed", 0.107, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    旋风花瓣             = EffectMeta("旋风花瓣", True, "7470581434458099005", "7470581434458099005", "8e56a93a04c6d28d09c1bd2cb8ad44c6", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.510, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_size: 默认51%, 0% ~ 100%"""
    旗帜横幅             = EffectMeta("旗帜横幅", True, "7479310670832438589", "7479310670832438589", "8034c28de0fd87116fb77c4cc452fc14", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    无法修复             = EffectMeta("无法修复", True, "7530166563236891957", "7530166563236891957", "4a08a2bf4d89986e935cf28591e88aa2", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    日落魔法             = EffectMeta("日落魔法", True, "7473094315116465469", "7473094315116465469", "a46aa0411bb6e109883463802c5dc782", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    旧相机               = EffectMeta("旧相机", True, "7478672941337677109", "7478672941337677109", "1ab830806be350dd9a65d1c7a1522651", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    时尚涂鸦             = EffectMeta("时尚涂鸦", True, "7409874523106905350", "7409874523106905350", "90de3d14a2ed928534e397c20ddb6213", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    时空隧道             = EffectMeta("时空隧道", True, "7491142744274930945", "7491142744274930945", "01d49d05d15ac48aaf7a77445cbcd029", [])
    明亮光晕特效         = EffectMeta("明亮光晕特效", True, "7480495885000953141", "7480495885000953141", "3d2a55c08f7edaf2c667da40f6a29ce4", [
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    星光CCD              = EffectMeta("星光CCD", True, "7399469080203496709", "7399469080203496709", "a797a2716fecf515a3cd79b2b7998bdc", [
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.150, 0.000, 0.500),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 0.500)])
    """参数:
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_number: 默认70%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_noise: 默认15%, 0% ~ 50%
    effects_adjust_sharpen: 默认20%, 0% ~ 50%"""
    星光变焦             = EffectMeta("星光变焦", True, "7409873829574577413", "7409873829574577413", "6df68092bd384cd0b145cf573b4485eb", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    星光绽放             = EffectMeta("星光绽放", True, "7529543095239675189", "7529543095239675189", "00f39528e151532b6d61e669362927b9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    星光鱼眼             = EffectMeta("星光鱼眼", True, "7399465518215957766", "7399465518215957766", "40154bca16208133db05af06cfc684ca", [
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认15%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%
    effects_adjust_texture: 默认80%, 0% ~ 100%"""
    星星光晕             = EffectMeta("星星光晕", True, "7482611862488583429", "7482611862488583429", "a179b9836215c161cfc537babbb7891b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    星星变焦             = EffectMeta("星星变焦", True, "7511624354644364597", "7511624354644364597", "af0074df8cc309f712cdb1efb44b81f7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    星星飞舞             = EffectMeta("星星飞舞", True, "7495951149585927425", "7495951149585927425", "86a0c0ba634ad981eba73e9668fe310c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    星火消逝             = EffectMeta("星火消逝", True, "7501539128014572861", "7501539128014572861", "8184b7749b39700a94ebc322f963b5d7", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    星火炸开             = EffectMeta("星火炸开", True, "7399468413527051525", "7399468413527051525", "3caa2d665bc97ae2956e1130f6a4db6a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    星火碰撞             = EffectMeta("星火碰撞", True, "7399472543192648966", "7399472543192648966", "7ba6614d70f2265795265e102d049d7a", [])
    星辰_III             = EffectMeta("星辰 III", True, "7399464940316167429", "7399464940316167429", "9a657ba2f45132b0205cb49795251771", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    显微镜               = EffectMeta("显微镜", True, "7499717329056566589", "7499717329056566589", "b4f652473cbe7d560e57c185561ed50b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    景深扫光             = EffectMeta("景深扫光", True, "7522580713611332865", "7522580713611332865", "9a88b900950bbe851a4760b777f5beec", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    景深扫描             = EffectMeta("景深扫描", True, "7512321191072288001", "7512321191072288001", "3baeeec41b240ce4a9a9110e2209b00c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    暖冬光斑             = EffectMeta("暖冬光斑", True, "7399469045025672454", "7399469045025672454", "a750c706ee87fb4b56f03c9ee76fc1d2", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认65%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_soft: 默认35%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    暗夜精灵             = EffectMeta("暗夜精灵", True, "7399466367721753862", "7399466367721753862", "fd84a50ad750ae84e3b2ce62cd22a6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    暗黑频闪             = EffectMeta("暗黑频闪", True, "7399471712531778821", "7399471712531778821", "36428a0f09863af6fb665ece21677e4b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    曝光变焦             = EffectMeta("曝光变焦", True, "7395473374673259782", "7395473374673259782", "b66ceb2594aee2fd5a1ace6a67e4db0f", [
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    月光闪闪             = EffectMeta("月光闪闪", True, "7399473274016500998", "7399473274016500998", "72e1573314be95270038e193db1def8d", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认75%, 0% ~ 100%"""
    望远镜               = EffectMeta("望远镜", True, "7399467260064042245", "7399467260064042245", "63e50736865f6248f87b6280c5b0d88b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    望远镜视图           = EffectMeta("望远镜视图", True, "7515371947782393149", "7515371947782393149", "95134e474118c6f1aaa1b20eb739d6ee", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    朦胧幽影             = EffectMeta("朦胧幽影", True, "7532399566994394421", "7532399566994394421", "0872b960c101ed2f3808ba92ea14fe1c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    未排序的复制         = EffectMeta("未排序的复制", True, "7529904604650163509", "7529904604650163509", "2ff93a5ac0f57d3446c69b6370381dd9", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    未来揭示             = EffectMeta("未来揭示", True, "7501185188920134973", "7501185188920134973", "8c1e93a681828eabb69986126fed82b4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    未来红               = EffectMeta("未来红", True, "7510126078652976437", "7510126078652976437", "b436ea37ddf28d2043527115efbd69f8", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    末日故障             = EffectMeta("末日故障", True, "7525102068512656701", "7525102068512656701", "6ad29db1aa25ea22484e09a5cca117ba", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    条纹侵蚀             = EffectMeta("条纹侵蚀", True, "7526585545317780797", "7526585545317780797", "854480822b92bcdc9c00f606fd3a22bd", [
                              EffectParam("effects_adjust_speed", 0.095, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    条纹构图             = EffectMeta("条纹构图", True, "7530655558056103221", "7530655558056103221", "898e12dbbadd6ccba7a95be3b1fcd935", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%"""
    极光扫描             = EffectMeta("极光扫描", True, "7521650030617414973", "7521650030617414973", "0c289411a65c6a4517763302705d8fe4", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    极光棱镜             = EffectMeta("极光棱镜", True, "7528666996959956285", "7528666996959956285", "0f32f5eecdd910b4ed1c74be274514bc", [
                              EffectParam("effects_adjust_noise", 1.010, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.010, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认101%, 0% ~ 100%
    effects_adjust_filter: 默认101%, 0% ~ 100%"""
    极地光束             = EffectMeta("极地光束", True, "7511594090924920125", "7511594090924920125", "48f8b706810d4a007e3cf7e2c23d3a03", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    极闪速旋             = EffectMeta("极闪速旋", True, "7512625031545965825", "7512625031545965825", "3b1670916145f8701ad7050b7570d30a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    极限缩放             = EffectMeta("极限缩放", True, "7506228055552085301", "7506228055552085301", "e1c7f68c2ddf9ed162dbb4ee1bcc4348", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    枫叶飘落             = EffectMeta("枫叶飘落", True, "7527987829423525173", "7527987829423525173", "768237af884d868560d363fc3f67ac7a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认0%, 0% ~ 100%"""
    柔和辉光             = EffectMeta("柔和辉光", True, "7399469043465456901", "7399469043465456901", "805d415643265f3625c1fb9d55822e32", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认55%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    柔彩胶卷             = EffectMeta("柔彩胶卷", True, "7478710767840169269", "7478710767840169269", "04820094e5e543201c01e9562632f8a0", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    柜窗                 = EffectMeta("柜窗", True, "7526045471794564413", "7526045471794564413", "1fc4943a68b528114935c4984abd654d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    树影                 = EffectMeta("树影", True, "7399472139495132422", "7399472139495132422", "e94e1952adee72678c426490036dae61", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    树影_II              = EffectMeta("树影 II", True, "7399467871170039045", "7399467871170039045", "068b6e28050ccaa8d0832419a0a185c4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    格纹纸质_II          = EffectMeta("格纹纸质 II", True, "7399467306339863814", "7399467306339863814", "d14acf770151e493179289b5ffe11041", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    框架自适应摆动       = EffectMeta("框架自适应摆动", True, "7522349097160838453", "7522349097160838453", "840da965b6b1110cafa6ac0117df7aae", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    桌面摄像头           = EffectMeta("桌面摄像头", True, "7489341538464582965", "7489341538464582965", "5e382013caa1d074894807adc4608644", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.286, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认29%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    梦回回响             = EffectMeta("梦回回响", True, "7516855996958903613", "7516855996958903613", "22bca43d7e587014bd1d9536b279fa33", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    梦境KIRA             = EffectMeta("梦境KIRA", True, "7399466459547667717", "7399466459547667717", "6c7c372ae5bbb2e6e686f97584042f2e", [
                              EffectParam("effects_adjust_number", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认45%, 0% ~ 100%
    effects_adjust_blur: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认25%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    梦境_II              = EffectMeta("梦境 II", True, "7399466130177330438", "7399466130177330438", "715227fc796386820c16198a57fd5249", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    梦境印象             = EffectMeta("梦境印象", True, "7517119182350109968", "7517119182350109968", "94ebcbae719ae86acc0668f7837a4094", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    梦幻微光             = EffectMeta("梦幻微光", True, "7476386624306187581", "7476386624306187581", "fd68ee4a1bf265fa5958cd72e95cc2a0", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    梦幻投影             = EffectMeta("梦幻投影", True, "7478347766511471933", "7478347766511471933", "3d216974fcf11529625ccae5aa3d6c35", [
                              EffectParam("effects_adjust_intensity", 0.457, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认46%, 0% ~ 100%"""
    梦幻萤火虫           = EffectMeta("梦幻萤火虫", True, "7527958664204799293", "7527958664204799293", "980ebd4ebc6ea31b1f33667f8ef21fea", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    梦幻雪花             = EffectMeta("梦幻雪花", True, "7399468263719079173", "7399468263719079173", "0d95d3c97bfac92fd5abc0f5c04431a5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    棱镜幻影             = EffectMeta("棱镜幻影", True, "7512058077957360957", "7512058077957360957", "ca93932b9b590c536622b463050446d1", [
                              EffectParam("effects_adjust_color", 2.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.350, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认240%, 0% ~ 100%
    effects_adjust_blur: 默认35%, 0% ~ 100%"""
    棱镜镜像             = EffectMeta("棱镜镜像", True, "7506397154290781493", "7506397154290781493", "1931c1e1ba79b059b54bc3e1faf9e4c2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    棱镜闪烁             = EffectMeta("棱镜闪烁", True, "7526893776216788285", "7526893776216788285", "059986750d3fe36c65fe48242b7db205", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    模糊光环             = EffectMeta("模糊光环", True, "7460363748323183933", "7460363748323183933", "e989e6c544197d1e21e2366d5ea33a14", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    模糊旋转             = EffectMeta("模糊旋转", True, "7486402432189091127", "7486402432189091127", "454443ae7a3579f3954b643dde132a80", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    模糊爱心放大镜       = EffectMeta("模糊爱心放大镜", True, "7399464309824228613", "7399464309824228613", "2f62bf787eb44535dbd128d60f46a29c", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    模糊特写             = EffectMeta("模糊特写", True, "7509157525485292861", "7509157525485292861", "78afb5e7183905773c775b36b5bb3f48", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    模糊闭幕             = EffectMeta("模糊闭幕", True, "7528866008975559989", "7528866008975559989", "0f1b7587d0a814b89f974295e03ff539", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    模糊震动             = EffectMeta("模糊震动", True, "7532075505080667453", "7532075505080667453", "51117787e695c104b41f1f454a21ead0", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    横向闪光             = EffectMeta("横向闪光", True, "7395466053838556422", "7395466053838556422", "59c03b2fa8b9a17240674bf41eab539f", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.760, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认76%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    横向闪光_II          = EffectMeta("横向闪光 II", True, "7395472259441249542", "7395472259441249542", "0e48afbc4e9aa05505644493cbb7156a", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    横条开幕             = EffectMeta("横条开幕", True, "7395467471026785541", "7395467471026785541", "5fa33938a1ad4a956bbac1b3e9805969", [
                              EffectParam("effects_adjust_speed", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认67%, 0% ~ 100%
    effects_adjust_luminance: 默认55%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    横纹故障             = EffectMeta("横纹故障", True, "7399466422117666054", "7399466422117666054", "c0895daca20904a1418a5cc257a30d4a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    樱桃脉冲             = EffectMeta("樱桃脉冲", True, "7491954630709054781", "7491954630709054781", "edbb10101b9caa041aa5d4601e905ade", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.056, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认6%, 0% ~ 100%"""
    樱花定格             = EffectMeta("樱花定格", True, "7494178825870298384", "7494178825870298384", "73a5afad87702e7ac03387c4e1279f26", [])
    橙色故障             = EffectMeta("橙色故障", True, "7506036895667834173", "7506036895667834173", "5aae857da32e60c3013e805a5851f5d8", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    武士刀挥砍           = EffectMeta("武士刀挥砍", True, "7517651955133500733", "7517651955133500733", "974e104e2d8751258470f698338db4c3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    毛刺                 = EffectMeta("毛刺", True, "7399465720964287749", "7399465720964287749", "467d4eff311315de8fa6549625919286", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    毛绒边框             = EffectMeta("毛绒边框", True, "7399471093766966534", "7399471093766966534", "a38b0c9226a3fbf51af73484c7815af2", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    气球拉伸             = EffectMeta("气球拉伸", True, "7525479632804646197", "7525479632804646197", "9552b9139ee9a55f38bcd3787cbf9341", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    气球飘浮             = EffectMeta("气球飘浮", True, "7485578779696434487", "7485578779696434487", "eef67adcf3cefb8bdb2d6d9cffff9357", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    水光影               = EffectMeta("水光影", True, "7399471490363673861", "7399471490363673861", "0e8f5cf28c600c62140c2f3666dbe18b", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认15%, 0% ~ 100%"""
    水彩游戏             = EffectMeta("水彩游戏", True, "7530875642833866037", "7530875642833866037", "147252d07841433f5aee39b987ea6b1f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    水晶烟火             = EffectMeta("水晶烟火", True, "7509785875799133493", "7509785875799133493", "e953729ce9d8d51cf52a67da37b57225", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    水波模糊             = EffectMeta("水波模糊", True, "7395473132619910405", "7395473132619910405", "99199baa75373b4a0faa08aa1c27a37a", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_chromatic: 默认70%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    水波泛起             = EffectMeta("水波泛起", True, "7399468835549498629", "7399468835549498629", "eda468a5537c139c6355e5abd75004de", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.440, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.460, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认10%, 0% ~ 100%
    effects_adjust_number: 默认44%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认46%, 0% ~ 100%"""
    水波流动             = EffectMeta("水波流动", True, "7399469653493304582", "7399469653493304582", "7dd5dbc55d5db8553d233fee727c40ac", [
                              EffectParam("effects_adjust_distortion", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认35%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_number: 默认60%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    水波纹_I             = EffectMeta("水波纹 I ", True, "7399472030829038853", "7399472030829038853", "71c261b20cb54b4b3082b443ca56c867", [
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.335, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%"""
    水波负片             = EffectMeta("水波负片", True, "7438462583641739777", "7438462583641739777", "0e8047d765b4a29f10881df2c8137250", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    水滴扩散             = EffectMeta("水滴扩散", True, "7395474030045760773", "7395474030045760773", "b4690abcdd92f98e3291fdcb74444f5b", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    治疗通话             = EffectMeta("治疗通话", True, "7479476786124868925", "7479476786124868925", "3b64078266515c4aefbdae6559b98efb", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    法式暖调             = EffectMeta("法式暖调", True, "7399465469012348165", "7399465469012348165", "f47d4affff8b734ed6c3b9042e81f7a4", [
                              EffectParam("effects_adjust_size", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认30%, 0% ~ 100%
    effects_adjust_number: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    法式浪漫             = EffectMeta("法式浪漫", True, "7399464280061529349", "7399464280061529349", "9b2b775d306501df0b9175ffbf09bb2a", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.456, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认46%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_soft: 默认100%, 0% ~ 100%"""
    泛光扫描             = EffectMeta("泛光扫描", True, "7395468013832523014", "7395468013832523014", "5c2fe2a8c4212ee879c16bea71b31e96", [
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认75%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, 0% ~ 100%"""
    泛光闪动             = EffectMeta("泛光闪动", True, "7399471978194701574", "7399471978194701574", "b40ea6fd5dd0d0865f3322826739e2d3", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认35%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    泡泡光斑             = EffectMeta("泡泡光斑", True, "7399464679782894853", "7399464679782894853", "a8ef5cdbe91838c8092a05a4ee2abf28", [
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_number: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认10%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_soft: 默认30%, 0% ~ 100%"""
    泡泡冲屏             = EffectMeta("泡泡冲屏", True, "7399470071745219845", "7399470071745219845", "6bd31d1cff2d2b0566ffc5f636be95a4", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    泡泡变焦             = EffectMeta("泡泡变焦", True, "7399467609609080069", "7399467609609080069", "78b4842f3061f447864093db1352dc29", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%"""
    泡泡火花             = EffectMeta("泡泡火花", True, "7501226168079666493", "7501226168079666493", "0ddd6e450634b308b881c57a6b497ff8", [
                              EffectParam("effects_adjust_speed", 0.262, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认26%, 0% ~ 100%"""
    波浪热感应           = EffectMeta("波浪热感应", True, "7517501494795554065", "7517501494795554065", "5c86f881f7186f5171c61fd56467547a", [])
    波点彩绘             = EffectMeta("波点彩绘", True, "7489768822581284157", "7489768822581284157", "f80577e0fe0d55f733884e7ef10918e6", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    波纹故障             = EffectMeta("波纹故障", True, "7515671818980642109", "7515671818980642109", "6839a926875d82021536cd106278ba7a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    波纹色差             = EffectMeta("波纹色差", True, "7399467920155315462", "7399467920155315462", "34c4ef20e2bbbc8e16e051ed901c387d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%"""
    活泼涂鸦             = EffectMeta("活泼涂鸦", True, "7476039822193347901", "7476039822193347901", "2b579d9ac9bc9e9ebbaa8d44469d02ea", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.429, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认43%, 0% ~ 100%
    effects_adjust_background_animation: 默认10%, 0% ~ 100%"""
    派对节拍             = EffectMeta("派对节拍", True, "7512975881061633333", "7512975881061633333", "7f098d4d5d6bde29b622803f513d6808", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    流体冲屏             = EffectMeta("流体冲屏", True, "7395467698077011206", "7395467698077011206", "d7e8b7a3741a5345cc73c0fa42c5fd74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    流体荡开             = EffectMeta("流体荡开", True, "7395469644725079302", "7395469644725079302", "fa0a0cd4b5446445108d6b4d44466739", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    流光碎闪             = EffectMeta("流光碎闪", True, "7444806464687837697", "7444806464687837697", "a89658eda82aaec1e5de5e4b88e74473", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    流动回声             = EffectMeta("流动回声", True, "7532683380085869885", "7532683380085869885", "50fa8ab95817316ae46af972c0ffc974", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    流动放大             = EffectMeta("流动放大", True, "7491837815370599697", "7491837815370599697", "635fb401dbf4576a481ce94967b40638", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    流动画面             = EffectMeta("流动画面", True, "7491139107918204161", "7491139107918204161", "5abed64ffea0f8f8cd18838a12e25ca6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    流动缩放             = EffectMeta("流动缩放", True, "7512642612205997329", "7512642612205997329", "aadfee970e1b56b0b2c258070ba21a50", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    浏览器关闭           = EffectMeta("浏览器关闭", True, "7491138615477603585", "7491138615477603585", "14702de6e899295c2a77429ab1551c78", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    浓郁彩噪             = EffectMeta("浓郁彩噪", True, "7399471604775881990", "7399471604775881990", "26dafc6122a3f1cdbea2b1640f5d216a", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_noise: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_intensity: 默认65%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%"""
    浪漫烟火             = EffectMeta("浪漫烟火", True, "7446716461734728208", "7446716461734728208", "cbc7a73ca7cc18db127f52f834615faa", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    浮雕边框             = EffectMeta("浮雕边框", True, "7527506093912739089", "7527506093912739089", "7c3b7fc34efc178b697a16a8802c857e", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    海报描边             = EffectMeta("海报描边", True, "7399465123708030213", "7399465123708030213", "9b6e240d941ae5e77e573cd584265e77", [
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_number: 默认90%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%"""
    海鸥DC               = EffectMeta("海鸥DC ", True, "7399471674233474310", "7399471674233474310", "300cffce79937d5b8b2f0af3a008c494", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%"""
    涂绘嘉年华           = EffectMeta("涂绘嘉年华", True, "7494584491810344253", "7494584491810344253", "4040e0461a8a7789694cda0cb755fc2d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.100, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认33%, 0% ~ 100%
    effects_adjust_sharpen: 默认10%, 0% ~ 100%"""
    涂鸦抽帧             = EffectMeta("涂鸦抽帧", True, "7434872753355756048", "7434872753355756048", "f0656a8c99219b086ce5d16260ba0883", [
                              EffectParam("effects_adjust_speed", 0.310, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认31%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    涂鸦拍立得           = EffectMeta("涂鸦拍立得", True, "7414192101988093189", "7414192101988093189", "6cb3d1911999b9556e9ac854c14583db", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%"""
    涂鸦揭晓             = EffectMeta("涂鸦揭晓", True, "7490868338000710965", "7490868338000710965", "c6bd9ab593d8e5192528ef09c9638ca1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    涂鸦日记             = EffectMeta("涂鸦日记", True, "7399468698471271686", "7399468698471271686", "ccdb66eec215f4de2aab19eed576138f", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_noise: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    涂鸦曝光             = EffectMeta("涂鸦曝光", True, "7470879412746030397", "7470879412746030397", "de7af8c706e37537fbdbe2bc767de2bb", [
                              EffectParam("effects_adjust_speed", 0.207, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认21%, 0% ~ 100%"""
    涂鸦蓝               = EffectMeta("涂鸦蓝", True, "7473129599271013685", "7473129599271013685", "4d2a0d334a8dcddca6a102923beed08b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    涂鸦黄色             = EffectMeta("涂鸦黄色", True, "7475646285219974453", "7475646285219974453", "a7d7c24fb76a5ef48a6f1c11e24404a1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    涟漪摇摆             = EffectMeta("涟漪摇摆", True, "7515367302238440765", "7515367302238440765", "a0b0f1005574f7aacdd83cdb887751b5", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    液体螺旋             = EffectMeta("液体螺旋", True, "7525161059229961525", "7525161059229961525", "061bc32629384138692a728e14d1553f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    液态分离             = EffectMeta("液态分离", True, "7399469436727577861", "7399469436727577861", "c24d9c1a2bf816e305645ee216b75e30", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    液态金属             = EffectMeta("液态金属", True, "7399470458866830598", "7399470458866830598", "79e58b1a8a3155d809143298e518003f", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    深度出现             = EffectMeta("深度出现", True, "7439595537738764817", "7439595537738764817", "66c5ae12ac25ff6723881e81cbfe27ca", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.667, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认67%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认67%, 0% ~ 100%"""
    深红之夜             = EffectMeta("深红之夜", True, "7513806551421914429", "7513806551421914429", "5d1429e8a071de301037fb0fd525b874", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    深红噪点             = EffectMeta("深红噪点", True, "7532897606637210933", "7532897606637210933", "d35c80872257ebcfac1b9aa5d496f1e9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    混乱                 = EffectMeta("混乱", True, "7395472455550258438", "7395472455550258438", "fdec63c54f10bf1b8b557a3709196eff", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认58%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    混乱展示             = EffectMeta("混乱展示", True, "7523092480473058621", "7523092480473058621", "526ba01014971dc05e08c2b0e5da73a8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    混乱翻转             = EffectMeta("混乱翻转", True, "7514302778848595253", "7514302778848595253", "75ee736c5c7d97892da8d5bb2d34e609", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    混乱闪烁             = EffectMeta("混乱闪烁", True, "7516583576868015421", "7516583576868015421", "d4de2c635185cd31db170d4e2989d9e3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    渐变色               = EffectMeta("渐变色", True, "7399464193092586758", "7399464193092586758", "90161f2ec96277018cc41f9ee2986395", [])
    渐渐放大             = EffectMeta("渐渐放大", True, "7517222063510129981", "7517222063510129981", "8b3dead1741fc513f1b2251050248dde", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    溶液                 = EffectMeta("溶液", True, "7395473549529533702", "7395473549529533702", "7a025aad468db3e0473b36e987386a4b", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认63%, 0% ~ 100%
    effects_adjust_size: 默认75%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, 0% ~ 100%"""
    滑动碰撞             = EffectMeta("滑动碰撞", True, "7514715194610781501", "7514715194610781501", "11cac4dd72812c1f2ebadf0de8a5c98b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    滑动载入             = EffectMeta("滑动载入", True, "7442287977864106497", "7442287977864106497", "138bb98faf97cb00a770bc807533a6a7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认75%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认25%, 0% ~ 100%"""
    滑稽俄罗斯方块       = EffectMeta("滑稽俄罗斯方块", True, "7514972080354495797", "7514972080354495797", "1a27fa331027ef721d1c7ee97728b4b7", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%"""
    滑稽聚焦             = EffectMeta("滑稽聚焦", True, "7512256783113669949", "7512256783113669949", "fb39256f418e2bacbccaf1434c929b4f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    滚动缩放             = EffectMeta("滚动缩放", True, "7530228040652148029", "7530228040652148029", "68955f8b564d5f38724a001a154dc186", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    滚动胶片             = EffectMeta("滚动胶片", True, "7399470564022209797", "7399470564022209797", "19151c1293399104b1aed93d36427182", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    滚筒卷动             = EffectMeta("滚筒卷动", True, "7498300080097594641", "7498300080097594641", "5fa0eb570556304f00d8da2b4f928962", [
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%
    effects_adjust_sharpen: 默认70%, 0% ~ 100%"""
    漂浮的云             = EffectMeta("漂浮的云", True, "7499086522830916925", "7499086522830916925", "5bc2fda167b85b1e14f1fa9bf5cc4bcd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    漂浮空间             = EffectMeta("漂浮空间", True, "7493784823216082192", "7493784823216082192", "27f4d024b3ec631b5da461b09b95521f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    漏光噪点             = EffectMeta("漏光噪点", True, "7399464704118230278", "7399464704118230278", "e8d86b0790f9e125d208d874fe97c9e0", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    漏光对焦             = EffectMeta("漏光对焦", True, "7399465637690674438", "7399465637690674438", "6632e7eb09fe5120e0872660146c22b5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.700),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 170%
    effects_adjust_size: 默认100%, 0% ~ 200%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认60%, 0% ~ 100%"""
    漏光闪烁             = EffectMeta("漏光闪烁", True, "7413649665658196481", "7413649665658196481", "f772864cb56f826fa1cf67a00c4c55ae", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    漩涡背景             = EffectMeta("漩涡背景", True, "7399470300926168325", "7399470300926168325", "52e5b1690a75d4e6ca88c7f18f47b7e7", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    漫画冲刺             = EffectMeta("漫画冲刺", True, "7462247315059789117", "7462247315059789117", "73bb7d7776468a70bb39ffe1e7fc85b6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    漫画分割             = EffectMeta("漫画分割", True, "7509340213584334096", "7509340213584334096", "c01be93bed16154b85c317d26935b640", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    漫画边框             = EffectMeta("漫画边框", True, "7399471777350569221", "7399471777350569221", "96e81364ff14324f55dc61d1a45c30b4", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    激光故障             = EffectMeta("激光故障", True, "7480478982631083317", "7480478982631083317", "ff0866152ac38e9e04f61f84395c3de4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    激光滑动             = EffectMeta("激光滑动", True, "7513786212499475765", "7513786212499475765", "1ad0d2665475fc440d52f1f4b87f4297", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%"""
    火光翻滚             = EffectMeta("火光翻滚", True, "7399470107455507717", "7399470107455507717", "7d48bd65ad8de487fa84d13f692fcf97", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火热展示             = EffectMeta("火热展示", True, "7493351266370768129", "7493351266370768129", "2fca69bfaeb933b101e1459884e3239b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火焰爆发             = EffectMeta("火焰爆发", True, "7519520411982253365", "7519520411982253365", "5b301f6c9128b5b649116b26372263b5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火焰绽放             = EffectMeta("火焰绽放", True, "7519924612327623997", "7519924612327623997", "15df55c3e1acba9a262a604b1347efb3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    火焰边框_II          = EffectMeta("火焰边框 II", True, "7399467757776981253", "7399467757776981253", "2a366600ec2ff8e27ab4308bccdf3faa", [
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认90%, 0% ~ 100%"""
    火焰魔方             = EffectMeta("火焰魔方", True, "7511267138485767477", "7511267138485767477", "72bed337f3097b1f687e23793ac37397", [
                              EffectParam("effects_adjust_intensity", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认0%, 0% ~ 100%"""
    火花闪烁             = EffectMeta("火花闪烁", True, "7530895838684532029", "7530895838684532029", "23850cb9e52a8e9c2fe614e74ae16cdd", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    火花飞扬             = EffectMeta("火花飞扬", True, "7473006394577390909", "7473006394577390909", "08a7fd77f14a134f3852ce2be3b8c863", [
                              EffectParam("effects_adjust_speed", 0.367, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认37%, 0% ~ 100%"""
    火花飞溅             = EffectMeta("火花飞溅", True, "7477596943741406517", "7477596943741406517", "bc3a874e754d78c86e0a0265ce734a5b", [
                              EffectParam("effects_adjust_speed", 0.111, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%"""
    灰色震动             = EffectMeta("灰色震动", True, "7479441949607464245", "7479441949607464245", "1045fc1eea9199b4f46b2614d8ae7549", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    灵异幻觉             = EffectMeta("灵异幻觉", True, "7441909188025913857", "7441909188025913857", "38de70b802f171882f6f657e68bd247f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    灵魂出窍             = EffectMeta("灵魂出窍", True, "7528425993598504245", "7528425993598504245", "73fbb11a587ae08047e7b2b8fdfa26db", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    灵魂出窍_II          = EffectMeta("灵魂出窍 II", True, "7399464859097632005", "7399464859097632005", "4e2c3e0ff21146736ddfeea23e6affaa", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认60%, 0% ~ 100%
    effects_adjust_background_animation: 默认85%, 0% ~ 100%"""
    灼烧打孔             = EffectMeta("灼烧打孔", True, "7395473026407615749", "7395473026407615749", "9eb02d961cf0a69a4f11efdd4a3ad6b6", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认75%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    灿金彩带             = EffectMeta("灿金彩带", True, "7399471517320416518", "7399471517320416518", "9645243a72ff084a721bdc33e499264c", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认25%, 0% ~ 100%"""
    炙热电影             = EffectMeta("炙热电影", True, "7527493629099789629", "7527493629099789629", "f8c439d79b65d25813f3e4f9eef0534f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    点点心形             = EffectMeta("点点心形", True, "7519831636863634749", "7519831636863634749", "852b16259ce973d6d5fdc4f31524984f", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    点赞发布             = EffectMeta("点赞发布", True, "7527590629589716277", "7527590629589716277", "af2758403c05804c9e7f52bd5410817c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    烟火星河             = EffectMeta("烟火星河", True, "7450390477863391745", "7450390477863391745", "1d22ca051967621891fa576a8a3ba63d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    烟花2024             = EffectMeta("烟花2024", True, "7395471641997856005", "7395471641997856005", "1921b7ff285c19c7a7e3c0b8f5628663", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.770, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.625, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认77%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认62%, 0% ~ 100%"""
    烟花                 = EffectMeta("烟花", True, "7399471215905230086", "7399471215905230086", "66ad5b6b6159e44e426619a68208ddb6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    烟花之心             = EffectMeta("烟花之心", True, "7473013960413908285", "7473013960413908285", "0c924ec17e4ebafbd0cf61d79e105eb2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    烟花光晕             = EffectMeta("烟花光晕", True, "7446316654000116240", "7446316654000116240", "947ce77334e34be7c1747c3d3aab9dc5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    烟雾                 = EffectMeta("烟雾", True, "7496556770358480181", "7496556770358480181", "c268aa7af684b02d274bceafbc879b4a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    烟雾炸开             = EffectMeta("烟雾炸开", True, "7399465301210844422", "7399465301210844422", "d642aeba48679e0a96a6a35aeb40eb00", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    烧焦的拍立得         = EffectMeta("烧焦的拍立得", True, "7522406604302568757", "7522406604302568757", "4a3a9c8dc743c08b21696a16fa5f9cfd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.625, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认62%, 0% ~ 100%"""
    热恋                 = EffectMeta("热恋", True, "7399468004527852805", "7399468004527852805", "4c09ed46b5c680f701350aa22db8f915", [
                              EffectParam("effects_adjust_size", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.060, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认45%, 0% ~ 100%
    effects_adjust_number: 默认45%, 0% ~ 100%
    effects_adjust_rotate: 默认6%, 0% ~ 100%
    effects_adjust_blur: 默认15%, 0% ~ 100%
    effects_adjust_range: 默认55%, 0% ~ 100%
    effects_adjust_sharpen: 默认75%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    热成像               = EffectMeta("热成像", True, "7528249849179884861", "7528249849179884861", "2649b773bee615b6479a6f690ad8f4af", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    热浪                 = EffectMeta("热浪", True, "7475511515999685941", "7475511515999685941", "2f215db8e7065090ffb6fc4deb41a6c8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    热缩放               = EffectMeta("热缩放", True, "7521598703853948221", "7521598703853948221", "cc3fd6a6227fff0721cb5858dd682c85", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    热震                 = EffectMeta("热震", True, "7510186952113671485", "7510186952113671485", "556f3e199974fc8c4c2d7ed66adf7f04", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爆闪锐化             = EffectMeta("爆闪锐化", True, "7399466526073507077", "7399466526073507077", "389b3c8872b9a18e5fe570975e3aa2ae", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认70%, 0% ~ 100%"""
    爱心DISCO            = EffectMeta("爱心DISCO", True, "7399464662812642565", "7399464662812642565", "076a41421bbc4a6419fcccdc3c1ce80c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.634, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认63%, 0% ~ 100%"""
    爱心QQ糖             = EffectMeta("爱心QQ糖", True, "7470782964947751440", "7470782964947751440", "82febec09b8688b7fa27aa400c9961d3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    爱心kira2            = EffectMeta("爱心kira2", True, "7464124620359094785", "7464124620359094785", "b300d87f1ebe987cfda1d81bde468a1a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爱心光波             = EffectMeta("爱心光波", True, "7399465644149918982", "7399465644149918982", "6d42bba28607f45ca90a7359b7c6ab74", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爱心冲屏             = EffectMeta("爱心冲屏", True, "7470416935667110417", "7470416935667110417", "5696b2b2134a508847b84bb38ad9aa1e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爱心啵啵             = EffectMeta("爱心啵啵", True, "7399472971787603206", "7399472971787603206", "dce0f289716b6e4c4c7256a4ab364188", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    爱心扫光2            = EffectMeta("爱心扫光2", True, "7464124620367467009", "7464124620367467009", "f0ccdfd63319c9443f9f422cc615dab7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爱心模糊             = EffectMeta("爱心模糊", True, "7399470509722815750", "7399470509722815750", "6b72b7d3d6683d8c55c8748fb62eba5c", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认70%, 0% ~ 100%"""
    爱心炸开             = EffectMeta("爱心炸开", True, "7464124620354884097", "7464124620354884097", "9c9ec57cc3664468b77e0729293621b1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    爱心软糖             = EffectMeta("爱心软糖", True, "7399472682409954566", "7399472682409954566", "0bab0476804fd6ac903bda686f49f3cb", [
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认90%, 0% ~ 100%"""
    牌组洗牌             = EffectMeta("牌组洗牌", True, "7516903721872280893", "7516903721872280893", "956d73e4656c74f8c8354a23e759a55b", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    特写推进             = EffectMeta("特写推进", True, "7533186962929372477", "7533186962929372477", "2c12c3be1ca94cfe5d5bc988dca63ef7", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    特写高光             = EffectMeta("特写高光", True, "7516424014307331389", "7516424014307331389", "f5359ed0393e57583a1f6478755ed385", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    狂欢节羽毛           = EffectMeta("狂欢节羽毛", True, "7475631107128431121", "7475631107128431121", "3bff1ba39707167214a6213412f7304e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    猫眼凹槽             = EffectMeta("猫眼凹槽", True, "7516649204144426293", "7516649204144426293", "234f83a54d13a324869b1630c47cd744", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    玫瑰冲屏             = EffectMeta("玫瑰冲屏", True, "7463438435118748176", "7463438435118748176", "9909e3be25c7759aff9131551e92dc01", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    环形抽卡             = EffectMeta("环形抽卡", True, "7491831263167352081", "7491831263167352081", "be8c6c8242cdb8db44e8cbb9e0d0c4ae", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    环形棱镜             = EffectMeta("环形棱镜 ", True, "7399471416497704198", "7399471416497704198", "fabdd74074fa6e6b8ce11258707f3f1f", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_texture: 默认80%, 0% ~ 100%"""
    现实崩塌             = EffectMeta("现实崩塌", True, "7528383263627332925", "7528383263627332925", "d5e07ac70405a1ba7f59bc03cad865ec", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    玻璃滑动             = EffectMeta("玻璃滑动", True, "7527682790876302653", "7527682790876302653", "e8c0c333d60426d41fece2379e84e4c0", [
                              EffectParam("effects_adjust_speed", 0.045, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认4%, 0% ~ 100%"""
    珠光碎闪             = EffectMeta("珠光碎闪", True, "7399465956524707078", "7399465956524707078", "a59345675d5136ba39ec5a8ac214ba93", [
                              EffectParam("effects_adjust_filter", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.490, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认55%, 0% ~ 100%
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认49%, 0% ~ 100%
    effects_adjust_blur: 默认15%, 0% ~ 100%"""
    瓷砖分割             = EffectMeta("瓷砖分割", True, "7516843305678802229", "7516843305678802229", "497e8d8f0b590c7a8fc9a0c498b8b272", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    瓷砖拼盘             = EffectMeta("瓷砖拼盘", True, "7522427960473718077", "7522427960473718077", "c8af26cfe845f953549b735902b7f666", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    电光波动             = EffectMeta("电光波动", True, "7399464304388443397", "7399464304388443397", "9d7a93ea28f697fbc109cd26377d025d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_color", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 200%
    effects_adjust_color: 默认3%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    电光爱心             = EffectMeta("电光爱心", True, "7399471557430594822", "7399471557430594822", "04883bbcc4ce20a240d5f90dc34db76f", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.419, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.473, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.590, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认42%, 0% ~ 100%
    effects_adjust_intensity: 默认47%, 0% ~ 100%
    effects_adjust_color: 默认59%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认100%, 0% ~ 100%"""
    电击                 = EffectMeta("电击", True, "7519366155639786813", "7519366155639786813", "a7bf130541fa37d66ab9c5293081da39", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    电子复古粉           = EffectMeta("电子复古粉", True, "7434830442265612817", "7434830442265612817", "2102c9c79f38d0d3b802a5d09e5b36f0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    电子录屏             = EffectMeta("电子录屏", True, "7414191309986090245", "7414191309986090245", "ef594333400d339062523a326aab590b", [])
    电子模拟器           = EffectMeta("电子模拟器", True, "7414312196764617990", "7414312196764617990", "c6fb8594a27f1ce460add9d812fea950", [])
    电子炫目             = EffectMeta("电子炫目", True, "7504162035295358261", "7504162035295358261", "720ccf21b69fb0b5512347085f6ccdb1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    电子蝴蝶_I           = EffectMeta("电子蝴蝶 I", True, "7399467871169940741", "7399467871169940741", "107efe4bddc158b5ee8fe55b81329cc6", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认85%, 0% ~ 100%
    effects_adjust_range: 默认25%, 0% ~ 100%
    effects_adjust_texture: 默认25%, 0% ~ 100%"""
    电子蝴蝶_II          = EffectMeta("电子蝴蝶 II", True, "7399467795173379334", "7399467795173379334", "b5beb75ff71c08e4393bffd0ee56c330", [
                              EffectParam("effects_adjust_speed", 0.267, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认27%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    电气妖气             = EffectMeta("电气妖气", True, "7528325918805265725", "7528325918805265725", "69109e42fe600fb149a2219e6fbe6e32", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    电视商店             = EffectMeta("电视商店", True, "7499050327920921909", "7499050327920921909", "a2666d8b6066ae0d32ad921724cedbee", [
                              EffectParam("effects_adjust_size", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认25%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认25%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认25%, 0% ~ 100%"""
    电视彩虹屏           = EffectMeta("电视彩虹屏", True, "7399469686058011909", "7399469686058011909", "d6ef86b7e37c1996e336d6541f5c4d7a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    电视没信号_嘶_Bad_TV_3 = EffectMeta("电视没信号-嘶（Bad TV）3", True, "7513792905903967541", "7513792905903967541", "9e9d99c37498987e4a5bbc440dcbb9fb", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    电视边框             = EffectMeta("电视边框", True, "7399467311872199942", "7399467311872199942", "87b8b83900d283b06e02ead6f09111e5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    电视雪花             = EffectMeta("电视雪花", True, "7485585836772216117", "7485585836772216117", "c83945300e7d658cdeaeeb7151bd7751", [
                              EffectParam("effects_adjust_noise", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.430, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认25%, 0% ~ 100%
    effects_adjust_sharpen: 默认43%, 0% ~ 100%"""
    电视频率             = EffectMeta("电视频率", True, "7507166687683202365", "7507166687683202365", "f528f0f902b28f4b9847a9f4b02871db", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认20%, 0% ~ 100%"""
    画布模糊             = EffectMeta("画布模糊", True, "7476305314099318077", "7476305314099318077", "011c9209d64d256f608ae55cad21b343", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认75%, 0% ~ 100%"""
    画布颜色打开         = EffectMeta("画布颜色打开", True, "7499071811611528509", "7499071811611528509", "14adfd5d44f21b9a3d1c6b9e0cb4bd74", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    画面瑕疵             = EffectMeta("画面瑕疵", True, "7530563662415662397", "7530563662415662397", "c18b6449ba126a26c597c06f62682fdf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    疯狂搜索             = EffectMeta("疯狂搜索", True, "7523845358313655613", "7523845358313655613", "cde6033bbca85f9c5f89ac9187e0feba", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    疾速飞线             = EffectMeta("疾速飞线", True, "7514208048458583313", "7514208048458583313", "9ba79e6525984c1899adaa656a8b27a2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    瘫软在地             = EffectMeta("瘫软在地", True, "7484149082022350086", "7484149082022350086", "d7a9508aa91ef53e63906cf1d110d0d3", [
                              EffectParam("effects_adjust_texture", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%"""
    白胶边框             = EffectMeta("白胶边框", True, "7399471011797716230", "7399471011797716230", "77fb2991364f2882ef4b61317f7a10dc", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    白色凹槽             = EffectMeta("白色凹槽", True, "7526975680014273845", "7526975680014273845", "13fe390c5af5344286d4a398caf69d82", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    白色描边             = EffectMeta("白色描边", True, "7399470981087120646", "7399470981087120646", "647776c50dafcbfab55f1dcb36d28792", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    白色渐显             = EffectMeta("白色渐显", True, "7399466630230609157", "7399466630230609157", "94b1df840d30218f14e8a5e509df5c8e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    白色裂痕             = EffectMeta("白色裂痕", True, "7528340590497385789", "7528340590497385789", "cb25dff4e5a9891e2000a82adb398bbb", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    白色负片             = EffectMeta("白色负片", True, "7514219827007900945", "7514219827007900945", "6fc0bc0d54bf34bd9095e17e92eeab7c", [])
    白鸽                 = EffectMeta("白鸽", True, "7399471848464911622", "7399471848464911622", "3e6056fb9e3a1829a666c6680f7eab83", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    百叶窗_II            = EffectMeta("百叶窗 II", True, "7399465524997999878", "7399465524997999878", "380df1dbfbfb93a560b389d5683043e7", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    监控现场             = EffectMeta("监控现场", True, "7409873773400247558", "7409873773400247558", "5487531876f19bc15620efc82dc648e7", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_noise: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    目眩酷热             = EffectMeta("目眩酷热", True, "7527640833777028413", "7527640833777028413", "64413b4ccdd4201d91e80ad199f0f941", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    直播表情             = EffectMeta("直播表情", True, "7506433178094095677", "7506433178094095677", "38dee8a06d69d4bc5583219db9c31280", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    相机光标             = EffectMeta("相机光标", True, "7532405800132693309", "7532405800132693309", "2edca09046f25b725fa7f50e59ba91b1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    相机抓拍             = EffectMeta("相机抓拍", True, "7442284470150894081", "7442284470150894081", "afed56c097d6e532405e1988f89073c7", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.420, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认42%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    相机框抖动           = EffectMeta("相机框抖动", True, "7451535589481910785", "7451535589481910785", "aa7ee627cd11bbf4d8c83ae2b90f59ca", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    真爱至上             = EffectMeta("真爱至上", True, "7444847227786236417", "7444847227786236417", "8c1fda9166cda42b28966135c1d4241c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    眩光抽帧             = EffectMeta("眩光抽帧", True, "7476400566889878032", "7476400566889878032", "73026e410754524f7aa73025d7bf140d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    眩光滑动             = EffectMeta("眩光滑动", True, "7509310375985302800", "7509310375985302800", "4c2597975c75a1869355197ec1548d3f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    眩晕剪辑             = EffectMeta("眩晕剪辑", True, "7510092144720268605", "7510092144720268605", "eea2b354a8d2f48b036e1737c7194afd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    眩晕狂欢             = EffectMeta("眩晕狂欢", True, "7518641065507753269", "7518641065507753269", "1330b2c47ae2f5f327a78deaff20abf5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    瞬间模糊             = EffectMeta("瞬间模糊", True, "7399469080236821765", "7399469080236821765", "6decf1b703bdfdfaac0d6f6f9b14594f", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%"""
    矩形闪白             = EffectMeta("矩形闪白", True, "7436323942207328784", "7436323942207328784", "160ed769f0845a0e2d3f8944f14708ae", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    矩阵频闪             = EffectMeta("矩阵频闪", True, "7399471764062948614", "7399471764062948614", "51763569c67e833ffcb37bd41a365c75", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.880, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认88%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    破旧故障             = EffectMeta("破旧故障", True, "7527040887700966717", "7527040887700966717", "2bfefb1f83e29a0d6c67a3433c9e8917", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    破碎镜像             = EffectMeta("破碎镜像", True, "7507599734274624829", "7507599734274624829", "22de8a020aae3234f76380932523208d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    碎照片               = EffectMeta("碎照片", True, "7399470840556883205", "7399470840556883205", "c7cd5f0c0f6ed89ddd9f0a9539bc856c", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    碎纸故障             = EffectMeta("碎纸故障", True, "7512624139585228049", "7512624139585228049", "8b5c27cdcc2b472ed5ba09491f0896d9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    碎闪描边             = EffectMeta("碎闪描边", True, "7399466389246987526", "7399466389246987526", "680eaa2d8db4fd3a5d33cf5399e61518", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认55%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%"""
    磁力幻象             = EffectMeta("磁力幻象", True, "7517274464627805501", "7517274464627805501", "2cf74ee96dec7c5e4597aa52c3e9d9c6", [])
    磨砂水晶             = EffectMeta("磨砂水晶", True, "7399470748278082821", "7399470748278082821", "f0d404000523379787cffd6e1db715c2", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    禁忌俄罗斯方块       = EffectMeta("禁忌俄罗斯方块", True, "7522744926933732661", "7522744926933732661", "6b1563a63f55e5be533a6405ad9b7a29", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    秀场高光             = EffectMeta("秀场高光", True, "7524088817683418385", "7524088817683418385", "5063385d69b672284eb37560bf86deb3", [])
    移动像素             = EffectMeta("移动像素", True, "7494179236115172661", "7494179236115172661", "f2bb1d7a03dd1aa1be3a6f7fc14dd624", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    移动画布             = EffectMeta("移动画布", True, "7506109137848126773", "7506109137848126773", "385c6dda08635f33a51a25abfe3c9c47", [
                              EffectParam("effects_adjust_filter", 0.683, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 2.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认68%, 0% ~ 100%
    effects_adjust_color: 默认250%, 0% ~ 100%"""
    移动纹理             = EffectMeta("移动纹理", True, "7506486018783120693", "7506486018783120693", "8f6b5d6c468b8359ed4077da00212a8e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    移动肖像_2           = EffectMeta("移动肖像 2", True, "7512499719579471157", "7512499719579471157", "2918d1df1338584236b75cd409de80ae", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    移轴镜头             = EffectMeta("移轴镜头", True, "7399471517320432902", "7399471517320432902", "0e48f496d20d72124d9acbc6550028a0", [
                              EffectParam("effects_adjust_range", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认10%, 0% ~ 100%
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认0%, 0% ~ 100%"""
    空灵                 = EffectMeta("空灵 ", True, "7399467566395149573", "7399467566395149573", "c0bbb93750bb7fe5b9b2900ff853adb6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    空间扰动             = EffectMeta("空间扰动", True, "7519009209627839761", "7519009209627839761", "8d78ae0551cdb99f9d9f6cccd241b748", [
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
    空间旋动             = EffectMeta("空间旋动", True, "7519040171635936513", "7519040171635936513", "3890209ca0fca0b897e1f0aae4470bd6", [])
    窗格光               = EffectMeta("窗格光", True, "7399470419482250502", "7399470419482250502", "6bd27e2b68879bb788d7ef0265648795", [
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    竖向开幕             = EffectMeta("竖向开幕", True, "7395467620922789125", "7395467620922789125", "26c9cc8d460d2639fe4fbb0bbd012d41", [
                              EffectParam("effects_adjust_blur", 0.877, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认88%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_distortion: 默认60%, 0% ~ 100%"""
    竖线屏闪             = EffectMeta("竖线屏闪", True, "7399471802361122053", "7399471802361122053", "4444e09ba223f94827fb9d423f445a71", [
                              EffectParam("effects_adjust_luminance", 1.700, 0.000, 2.300),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 2.500),
                              EffectParam("effects_adjust_range", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 2.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认170%, 0% ~ 230%
    effects_adjust_blur: 默认100%, 0% ~ 250%
    effects_adjust_range: 默认15%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 200%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    竖闪模糊             = EffectMeta("竖闪模糊", True, "7395473030152998150", "7395473030152998150", "795af3daacce29e8d7732e5b2223e01a", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    童趣闪电             = EffectMeta("童趣闪电", True, "7434830442269774352", "7434830442269774352", "e95493493cc5a1390dc01cabc124640c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    简易框架             = EffectMeta("简易框架", True, "7514974004495551805", "7514974004495551805", "ace39e15f4ecd21ad4ba546d19b27e7a", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    箭头放大镜           = EffectMeta("箭头放大镜", True, "7399471130261654790", "7399471130261654790", "e0540ac533119123deb057f99419b6dc", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    篝火派对             = EffectMeta("篝火派对", True, "7399469932980784389", "7399469932980784389", "835bb9198b86d4433cbf540bf3243f4d", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    粉笔涂鸦             = EffectMeta("粉笔涂鸦", True, "7478937842081729853", "7478937842081729853", "13c07792568fe196333f89154c08e5cf", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    粉笔素描             = EffectMeta("粉笔素描", True, "7532413685717798197", "7532413685717798197", "421f34233f2e803abd69d19f0f588226", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    粉色光滴             = EffectMeta("粉色光滴", True, "7484122487723281717", "7484122487723281717", "541f301bdd29728b506eb1cc86021856", [
                              EffectParam("effects_adjust_speed", 0.136, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    粉色眨眼             = EffectMeta("粉色眨眼", True, "7463254687957912893", "7463254687957912893", "cb59ac948c1c286a5d0a599a0fe37532", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    粉色震波             = EffectMeta("粉色震波", True, "7501598219537878273", "7501598219537878273", "98e59d1f26d6f238be50da7d21bbf5a7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    粉雪                 = EffectMeta("粉雪", True, "7399469615832730886", "7399469615832730886", "54842ba545ec87e746a3a8f287c7be93", [
                              EffectParam("effects_adjust_background_animation", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.950, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认95%, 0% ~ 100%"""
    粒子模糊             = EffectMeta("粒子模糊", True, "7399469835417128198", "7399469835417128198", "c16410155f6fe0fbac8d4a58c06df3ca", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    粒子模糊_II          = EffectMeta("粒子模糊 II", True, "7399470035938381062", "7399470035938381062", "dab36cd2d944de4611f0040921c550a6", [
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    粒子空间             = EffectMeta("粒子空间", True, "7497827549150563600", "7497827549150563600", "90b9d1221fcf506f8b94d857fed76049", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    粗糙墙面             = EffectMeta("粗糙墙面", True, "7532884815079542077", "7532884815079542077", "2e5cc7734f6f251cad2aa3151a2cf5bf", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    精致辉光             = EffectMeta("精致辉光", True, "7395474950355733766", "7395474950355733766", "ad7fae5b6c5335be75113171ab5a6b6d", [
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_range: 默认85%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_soft: 默认60%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%"""
    精选聚焦             = EffectMeta("精选聚焦", True, "7500130248726416693", "7500130248726416693", "bd6feb07e9efa1a918918f7d4cfaf886", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    糖果微光             = EffectMeta("糖果微光", True, "7480425055101504821", "7480425055101504821", "10183a1d83d43f8a903eb46587e21a7c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    素材播放器           = EffectMeta("素材播放器", True, "7525701881088331061", "7525701881088331061", "d9bdbaeb9436cabfff2c2d4ae1d1aa41", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    紧急闪光             = EffectMeta("紧急闪光", True, "7508670195855084853", "7508670195855084853", "095a0de1f9542b1bb43aca48f14cce91", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    紫罗兰画布           = EffectMeta("紫罗兰画布", True, "7478224194292026685", "7478224194292026685", "fe3f8d0dc834cab22d9e75276bc61746", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    紫色失真             = EffectMeta("紫色失真", True, "7523171770849873213", "7523171770849873213", "c546760b6f1b7662b83176bc36c7785b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    紫色火花             = EffectMeta("紫色火花", True, "7527286701862014269", "7527286701862014269", "b97685de0811d68082538e71be3f40f8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    紫色负片             = EffectMeta("紫色负片", True, "7399463181166447877", "7399463181166447877", "a21c94f366e16f2aa8bd9e491ec226c5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    紫雾                 = EffectMeta("紫雾", True, "7399471006991142150", "7399471006991142150", "bf106ce53d50ff0a7ebabe323a69b097", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    繁花之镜_II          = EffectMeta("繁花之镜 II", True, "7395467565335645445", "7395467565335645445", "f0d388c9f42348261ed7b6871cfaa86e", [
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认20%, 0% ~ 100%
    effects_adjust_intensity: 默认80%, 0% ~ 100%
    effects_adjust_range: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 100%"""
    红色包装             = EffectMeta("红色包装", True, "7514578233413700917", "7514578233413700917", "067b9fd69e6e2476b785d533d505286c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    红色节奏             = EffectMeta("红色节奏", True, "7521644308869516597", "7521644308869516597", "fbc04b8ba9fa3b7365ad1fe2f5cba6f9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%"""
    红色节拍             = EffectMeta("红色节拍", True, "7488360440569793853", "7488360440569793853", "2394c6e8191349029c2067d618de6c8d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    红色闪耀             = EffectMeta("红色闪耀", True, "7516786512680308021", "7516786512680308021", "8205ce44c3669bcf52b465b5873720e0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    红边模糊             = EffectMeta("红边模糊", True, "7399472396350033158", "7399472396350033158", "1afa6bef0ff1ddd4e54c13a2d6a7c59a", [
                              EffectParam("effects_adjust_blur", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认90%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%"""
    红黄蓝扭曲           = EffectMeta("红黄蓝扭曲", True, "7478282894214057269", "7478282894214057269", "2cef9ca2da74d80595029bf170a7bcac", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    纵向抖动             = EffectMeta("纵向抖动", True, "7399465889323830533", "7399465889323830533", "95f1d0f51d2eb529ac7b97c8cddbfaf1", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认100%, 0% ~ 100%"""
    纵向滑动             = EffectMeta("纵向滑动", True, "7523105304674897205", "7523105304674897205", "fa628643e374b6f9f287aa574125f570", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    纵横拉扯             = EffectMeta("纵横拉扯", True, "7521482072578379009", "7521482072578379009", "99487bf094dfa518fc607f07ddb33944", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    纸张片头             = EffectMeta("纸张片头", True, "7414312717667912966", "7414312717667912966", "2d41e5e0eeb934e940f7004882ce8650", [])
    纸质抽帧             = EffectMeta("纸质抽帧", True, "7418460062231826945", "7418460062231826945", "25ead8365402ae331854eabd37ad44a8", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    纸质撕边             = EffectMeta("纸质撕边", True, "7399469293840174342", "7399469293840174342", "fd5588f68a681b8eba1449a5d0240097", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    纸质边框             = EffectMeta("纸质边框", True, "7399466881364577541", "7399466881364577541", "554d4d330b4d17f0b404e598a66f05c9", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    纸醉金迷             = EffectMeta("纸醉金迷 ", True, "7399465820318960902", "7399465820318960902", "dcfb9e8703b3ac243e73afdb664c2b2e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.801, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认80%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    纹理故障             = EffectMeta("纹理故障", True, "7504698329180228917", "7504698329180228917", "596a4d4c28f11b27469157a671399979", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    线光变速             = EffectMeta("线光变速", True, "7395472035318664454", "7395472035318664454", "87a99c8ae0f9e333abaef48b79a96c90", [
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认60%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    线描折痕             = EffectMeta("线描折痕", True, "7524926633912864017", "7524926633912864017", "f574b10bd8f69fdb628eadc554384a71", [])
    线条涂鸦             = EffectMeta("线条涂鸦", True, "7399466191577730310", "7399466191577730310", "8fa940bc27748548ab8bf3e2d26c7f3b", [
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 80%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    线框立方体           = EffectMeta("线框立方体", True, "7521512778331327760", "7521512778331327760", "9c785fa8d726f12ebda5ae86539de407", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    组合卡片             = EffectMeta("组合卡片", True, "7496717523937725713", "7496717523937725713", "c6ac4f5b77681c32d05d7c13e59d6990", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    细节展示             = EffectMeta("细节展示", True, "7496722952331726096", "7496722952331726096", "ab8da3e814fc61d9a80763b32516fc9a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    细节滑动             = EffectMeta("细节滑动", True, "7512272617915632897", "7512272617915632897", "2e46ff0dc22b4b42034dd1ace1b7ed90", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    细节灯照             = EffectMeta("细节灯照", True, "7512597407801052417", "7512597407801052417", "7ba31e15c866c4bbd7a48d8e7c0aa0e7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    细闪_III             = EffectMeta("细闪 III", True, "7399466602967600390", "7399466602967600390", "432b12f72fe1b0f081dc292bc415dbb0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    织布机编织           = EffectMeta("织布机编织", True, "7509871221870251317", "7509871221870251317", "49411eaa9e9191ff41b97250914d3d46", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    绚丽光斑             = EffectMeta("绚丽光斑", True, "7446312093990523408", "7446312093990523408", "4581a1c623e15aa42888ec59ce87b11a", [
                              EffectParam("effects_adjust_speed", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认67%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认75%, 0% ~ 100%"""
    绿光波纹             = EffectMeta("绿光波纹", True, "7511302134558674229", "7511302134558674229", "eefef18c1d8f36b1aef5193044c1cb81", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    绿光监控             = EffectMeta("绿光监控", True, "7399471115933961478", "7399471115933961478", "2c2c06b5bfa714e7dea247d5200d1513", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认80%, 0% ~ 100%
    sticker: 默认40%, 0% ~ 100%"""
    绿色双重             = EffectMeta("绿色双重", True, "7477450363151371573", "7477450363151371573", "a5c7c1727dba7ec67bb6d7d27a8b770d", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    绿色视野             = EffectMeta("绿色视野", True, "7497908199245368629", "7497908199245368629", "4232a1b712719d877fe1a08900859b1a", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    缓慢前进             = EffectMeta("缓慢前进", True, "7519411810915667253", "7519411810915667253", "155408c6f0a5ab8ccf582eeafdab856f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    编辑错误             = EffectMeta("编辑错误", True, "7516052333747309885", "7516052333747309885", "e74e60683ece778a249ccaaed6d40695", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    缤纷                 = EffectMeta("缤纷", True, "7399464552942832902", "7399464552942832902", "783debb6f0b544b13113102f74417460", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_number: 默认30%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    缤纷彩带             = EffectMeta("缤纷彩带", True, "7446716461734695441", "7446716461734695441", "bd76e2e89ffe2698d6e2f15a0e7918fa", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    缤纷烟花             = EffectMeta("缤纷烟花", True, "7395466308126559493", "7395466308126559493", "22a395e75968d0ba66285c3d9b9d400a", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.770, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认77%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    缩小翻转             = EffectMeta("缩小翻转", True, "7522451215943273789", "7522451215943273789", "a2f91f164014b548cdf3b986ba7b3bbb", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    缩放幻灯片           = EffectMeta("缩放幻灯片", True, "7523125264671444285", "7523125264671444285", "8fa3b7a5eafdfcd0bccd85383531a43c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    缩放摆动             = EffectMeta("缩放摆动", True, "7509366108651097397", "7509366108651097397", "14335c494c4d60d4b5b8f8923de6a7c5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    缩放网格             = EffectMeta("缩放网格", True, "7502051909629496637", "7502051909629496637", "beb7b5b78bccc383e909beb1f70b84d9", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    缩放运镜             = EffectMeta("缩放运镜", True, "7439647269499965968", "7439647269499965968", "cd385576887865cd23acfbad20a95440", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    缩略图导入           = EffectMeta("缩略图导入", True, "7527899287854779709", "7527899287854779709", "1ac55bd17737773a07b4f77bee44f190", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    网格故障             = EffectMeta("网格故障", True, "7468148484974087477", "7468148484974087477", "18fbc9a8a578094a6c0d058344b5ff0e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    网点闪亮             = EffectMeta("网点闪亮", True, "7529528608658918709", "7529528608658918709", "d31f5ca86289621d59ee0926abff0f04", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    美式                 = EffectMeta("美式", True, "7399470320958098694", "7399470320958098694", "d442ace251550cdb0c17d2e5c9c6a87c", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%"""
    美式_II              = EffectMeta("美式 II", True, "7399469156623469829", "7399469156623469829", "cd7423d39d5a115fc4d5d7f5db43658c", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    美式_III             = EffectMeta("美式 III", True, "7399465318617271558", "7399465318617271558", "55d588fc51565d218a444ec12efd68c0", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    美式_IV              = EffectMeta("美式 IV", True, "7399467242435431686", "7399467242435431686", "0bddd63da76f2f117140ff240c57daee", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.620, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认62%, 0% ~ 100%"""
    美式_V               = EffectMeta("美式 V", True, "7399471049210957061", "7399471049210957061", "26f287cc23166dc878589197c5800842", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    美式胶片             = EffectMeta("美式胶片", True, "7481226253459017013", "7481226253459017013", "7006b00d244b8f47584478ac09dc48ed", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认100%, 0% ~ 100%"""
    羽毛飘落             = EffectMeta("羽毛飘落", True, "7399470420547620102", "7399470420547620102", "46f1c56f6fcd3a2abd80ff7d701f6eb0", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.260, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.108, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认35%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认26%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认11%, 0% ~ 100%"""
    翻转变焦             = EffectMeta("翻转变焦", True, "7395465413527899398", "7395465413527899398", "fd70d11eb7a16891bd6f7c848455da9c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_sharpen: 默认40%, 0% ~ 100%
    effects_adjust_luminance: 默认40%, 0% ~ 100%"""
    翻转错误             = EffectMeta("翻转错误", True, "7526982603686038837", "7526982603686038837", "6ee392da7d113741451e15592ed89093", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%"""
    老式DV               = EffectMeta("老式DV", True, "7399468517923310854", "7399468517923310854", "ab52379826dfeffd80063240c5ed6389", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认63%, 0% ~ 100%
    effects_adjust_noise: 默认30%, 0% ~ 100%"""
    老式游戏机           = EffectMeta("老式游戏机", True, "7491144607795891509", "7491144607795891509", "fa2e5864c5fd6309977ca002b07a2e90", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    老纪录片             = EffectMeta("老纪录片", True, "7528625359508622645", "7528625359508622645", "f3ab333bdc2b606fe52304cd4e16517a", [
                              EffectParam("effects_adjust_speed", 0.429, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认43%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    聚光摇曳特效         = EffectMeta("聚光摇曳特效", True, "7480778693728619829", "7480778693728619829", "0be38680cb97f4ce71dec7cf3a5b15fb", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    聚光灯闪烁_2         = EffectMeta("聚光灯闪烁 2", True, "7478771189209402685", "7478771189209402685", "c236ce3089062d06a799409b8d476e9d", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    聚焦色散             = EffectMeta("聚焦色散", True, "7431083912467583489", "7431083912467583489", "9eeaa1bba5cd7bfa9c72bc0ce4d922a7", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.125, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_distortion: 默认12%, 0% ~ 100%
    effects_adjust_sharpen: 默认20%, 0% ~ 100%"""
    背光调节             = EffectMeta("背光调节", True, "7524362328574299453", "7524362328574299453", "c92f1de2f4ec84f57b164717d999e6db", [
                              EffectParam("effects_adjust_speed", 0.103, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认10%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    背景渐隐             = EffectMeta("背景渐隐", True, "7509881595126402357", "7509881595126402357", "26bc931f8f1f1d6a37f725be5af7b0df", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    胶片_I               = EffectMeta("胶片 I", True, "7399471460445621509", "7399471460445621509", "bcb9ebf14085e77e8b0e1cd1cf0a87f8", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    胶片_II              = EffectMeta("胶片 II", True, "7399471617497255174", "7399471617497255174", "52a78b591b893502154b101c757877db", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    胶片孔               = EffectMeta("胶片孔", True, "7478589595416793616", "7478589595416793616", "02f4bc12e84c2a8b62b877b72f5dd1eb", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    胶片显影             = EffectMeta("胶片显影", True, "7399468090834095365", "7399468090834095365", "a09195689037df58fd23db7f28d3a2b6", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_soft: 默认100%, 0% ~ 100%"""
    胶片框_II            = EffectMeta("胶片框 II", True, "7399465350317804805", "7399465350317804805", "fd84488800ef5683555188564886ab76", [])
    胶片框光斑           = EffectMeta("胶片框光斑", True, "7476357155264664065", "7476357155264664065", "59b6ad58a08a31dd06729180ea63bfc3", [])
    胶片漏光III          = EffectMeta("胶片漏光III", True, "7439647269202170384", "7439647269202170384", "ae1e56523970804e5171769ff23ff2fa", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    胶片燃烧             = EffectMeta("胶片燃烧", True, "7532036905764932925", "7532036905764932925", "f218d649f1b3f52c438645d2c07a2720", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    胶片翻转             = EffectMeta("胶片翻转", True, "7429593004123361809", "7429593004123361809", "6c7695a8700a520e4110bb14f298bd3e", [
                              EffectParam("effects_adjust_speed", 0.480, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认48%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    胶片边框             = EffectMeta("胶片边框", True, "7449634663254987265", "7449634663254987265", "024763692a9bc969e04c88f1341f6043", [])
    胶片连拍             = EffectMeta("胶片连拍", True, "7399468898019446022", "7399468898019446022", "cb017def5c29fc1af5de0041469d4ff4", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    胶片闪切             = EffectMeta("胶片闪切", True, "7395471804007009541", "7395471804007009541", "347713d7f8a7b69b1885ee9d38cd8de6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    脉冲漂移             = EffectMeta("脉冲漂移", True, "7522400716330159413", "7522400716330159413", "cf812758a8a226a84f38aeec28e510f0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认33%, 0% ~ 100%"""
    脉动聚焦             = EffectMeta("脉动聚焦", True, "7529426048820202805", "7529426048820202805", "1666aca501bb86dc0913fe233bef86f3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认75%, 0% ~ 100%"""
    脱色                 = EffectMeta("脱色", True, "7488764988757167421", "7488764988757167421", "64a4a0a23261a275ef378a61af196e93", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    膨胀闪光             = EffectMeta("膨胀闪光", True, "7529792982153743669", "7529792982153743669", "482dbd24dbcd32c8a9760bbb284d5dc2", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    自然_I               = EffectMeta("自然 I", True, "7399466034480090374", "7399466034480090374", "b692892ba55b4cbd18c97704102b9938", [
                              EffectParam("effects_adjust_size", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%"""
    致幻彩噪             = EffectMeta("致幻彩噪", True, "7484039446535376181", "7484039446535376181", "f9a5719fa44460de9d0be0c312bce9cb", [
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    舞动闪光             = EffectMeta("舞动闪光", True, "7463081288182828341", "7463081288182828341", "41a7ade4354cd686bade135c847f1f9b", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%"""
    舞蹈图框             = EffectMeta("舞蹈图框", True, "7509796481604390197", "7509796481604390197", "6ae8a33e3b10d9e294cff7a9d73b1dc8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    色偏复制             = EffectMeta("色偏复制", True, "7508350966819769661", "7508350966819769661", "dd517e45a48899b61fe62e9333cbe1b0", [])
    色差开幕             = EffectMeta("色差开幕", True, "7399469043465325829", "7399469043465325829", "fc98a601f63bacc514067ecfa2849137", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%"""
    色差拉伸             = EffectMeta("色差拉伸", True, "7520057373902294289", "7520057373902294289", "03600dac044ab7ec6b9a24d7fbee3350", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    色差故障2            = EffectMeta("色差故障2", True, "7483781094337203511", "7483781094337203511", "d0665d0f528350d0ae6a86bba431d418", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    色差故障             = EffectMeta("色差故障", True, "7399472112223767814", "7399472112223767814", "73814d72a1a8cba91943394efeda4b34", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认50%, 0% ~ 100%"""
    色差流动             = EffectMeta("色差流动", True, "7399470065093233925", "7399470065093233925", "87c19b93694c5647be185fc444d7a516", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.900, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%
    effects_adjust_texture: 默认90%, 0% ~ 100%
    effects_adjust_color: 默认90%, 0% ~ 100%"""
    色度脉冲             = EffectMeta("色度脉冲", True, "7470827295704354101", "7470827295704354101", "1fbb156ec17f3aeb0099ecf21d765450", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    色彩扫描             = EffectMeta("色彩扫描", True, "7529574950240324917", "7529574950240324917", "9dd1faced7420c586cadb3422ace0f3f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    色散冲击             = EffectMeta("色散冲击", True, "7395471053717277957", "7395471053717277957", "ed2771a77992c0f8d0958bbaadbba53e", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_chromatic", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_vertical_chromatic: 默认60%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%"""
    色散故障             = EffectMeta("色散故障", True, "7395468877502713094", "7395468877502713094", "5989d49ac22b81107c9741367ae6651d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    色相狂欢             = EffectMeta("色相狂欢", True, "7530124067391786293", "7530124067391786293", "c1034a373e4ccc51be4042c68d1127b5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    艺术背景             = EffectMeta("艺术背景", True, "7517177950052158773", "7517177950052158773", "10804b3d6261b8bdfef8a49a99f75858", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    节奏拉扯             = EffectMeta("节奏拉扯", True, "7520426707229134096", "7520426707229134096", "a6e88a43aace2dbd10a99d025e1ae4f3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    节奏游戏             = EffectMeta("节奏游戏", True, "7511951857443523893", "7511951857443523893", "05fc30ada39ce59b499bfeaf154deaaa", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    节奏缩放             = EffectMeta("节奏缩放", True, "7515363776007245109", "7515363776007245109", "d418cedfd2a464c9a801bf8f03a69e1d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    花卉邮票             = EffectMeta("花卉邮票", True, "7476362458614009141", "7476362458614009141", "0ad68b570ff58315878657c85c9bc26b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    花园图框             = EffectMeta("花园图框", True, "7499530651864010037", "7499530651864010037", "ec65f6644d6c0ee2ca933146345a0371", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    花屏故障             = EffectMeta("花屏故障", True, "7399466631983828230", "7399466631983828230", "6db775d8ec0ebc525e89ffbe21f2d589", [
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.143, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认14%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    花屏故障_II          = EffectMeta("花屏故障 II", True, "7395467839634705670", "7395467839634705670", "429436b9a9eac2edd4fea857b3074432", [
                              EffectParam("effects_adjust_intensity", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认75%, 0% ~ 100%
    effects_adjust_luminance: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    花朵模糊             = EffectMeta("花朵模糊", True, "7511581268509822224", "7511581268509822224", "e1c7f9a5abbc822be3c6fa9cf387e2c4", [])
    花瓣扑               = EffectMeta("花瓣扑", True, "7502281280759893301", "7502281280759893301", "db3281cf964754aca30bf3caa6ea9d9e", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    花瓣雨               = EffectMeta("花瓣雨", True, "7471193505331793213", "7471193505331793213", "5e74163b0afb52580b0dc1901f231959", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    苍白噪音             = EffectMeta("苍白噪音", True, "7508068800739216701", "7508068800739216701", "c169f226c15b875b73f4561f8d1bea4a", [
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    荡漾                 = EffectMeta("荡漾", True, "7399466667740302598", "7399466667740302598", "7a08a3c5aa067e55cd0f638cd3161a1b", [
                              EffectParam("effects_adjust_range", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.350, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认35%, 0% ~ 100%
    effects_adjust_intensity: 默认35%, 0% ~ 100%"""
    荡漾_II              = EffectMeta("荡漾 II", True, "7399467488058051845", "7399467488058051845", "4a10c82183001dba5c5006e6fb2222be", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_distortion: 默认30%, 0% ~ 100%
    effects_adjust_number: 默认30%, 0% ~ 100%"""
    荧光玫瑰             = EffectMeta("荧光玫瑰", True, "7450018653912699408", "7450018653912699408", "22ec77257edf26222b3bb9704b261908", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    落日印记             = EffectMeta("落日印记", True, "7527901928299236669", "7527901928299236669", "915a2401263fc8adb30e0722df51817f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蓝光扫描             = EffectMeta("蓝光扫描", True, "7399466987316890886", "7399466987316890886", "adf71a81fed9244a306fd47bf294009d", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%"""
    蓝屏dv               = EffectMeta("蓝屏dv", True, "7522603285489011985", "7522603285489011985", "cc0ef32e94595af437cad87042328aa1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    蓝色渐变             = EffectMeta("蓝色渐变", True, "7508734659350646077", "7508734659350646077", "309ae6702ab33d367955800d8c6dea09", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蓝调拖影             = EffectMeta("蓝调拖影", True, "7519354928133967105", "7519354928133967105", "dd2427c6cf71e186330086906235b69f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蓝边电子             = EffectMeta("蓝边电子", True, "7399467539224431878", "7399467539224431878", "1f9d32d0bfdf2119ab49ee0534bd848e", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.450, 0.200, 0.700)])
    """参数:
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_texture: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认45%, 20% ~ 70%"""
    虚焦拍摄             = EffectMeta("虚焦拍摄", True, "7460019286447246598", "7460019286447246598", "b0f2e809710213c7c9f00f9a606f3bd6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    虚线放大镜           = EffectMeta("虚线放大镜", True, "7399471049210858757", "7399471049210858757", "44370286a32ad2e26535a6af4842aa0b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%"""
    蛇形扭曲             = EffectMeta("蛇形扭曲", True, "7529573673540390197", "7529573673540390197", "272f918798be80e95a65b53f37bf6690", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蜡笔复刻             = EffectMeta("蜡笔复刻", True, "7498513612374347069", "7498513612374347069", "43067b638fec1436985c5fab487c305d", [
                              EffectParam("effects_adjust_horizontal_shift", 0.417, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认42%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    蜡笔趣味             = EffectMeta("蜡笔趣味", True, "7512387697932062013", "7512387697932062013", "30b9ea18bef4b3d3910d5ad3454cf516", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蝴蝶Kira             = EffectMeta("蝴蝶Kira", True, "7524024145760357649", "7524024145760357649", "ac68dff4f1a6a22f19d4eefa31940638", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蝴蝶光斑             = EffectMeta("蝴蝶光斑", True, "7399467918850788613", "7399467918850788613", "45377639fc1c0b29cc889f71f6ca2fd0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    蝴蝶投影             = EffectMeta("蝴蝶投影", True, "7399466044777106694", "7399466044777106694", "1232e724c96dba595e79ae7d2aa839b2", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.050, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认25%, 0% ~ 100%
    effects_adjust_number: 默认5%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    蝴蝶飞舞             = EffectMeta("蝴蝶飞舞", True, "7399465516982717701", "7399465516982717701", "48aafc4d01d3d25816e4c239fbf46b23", [
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    血墨晕染             = EffectMeta("血墨晕染", True, "7426286176236999169", "7426286176236999169", "66eb3c3f1b4c631de14e91993416c247", [
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认70%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    街头涂鸦             = EffectMeta("街头涂鸦", True, "7512343383352839425", "7512343383352839425", "82b654eeef8b2906427f7e540e5dae24", [])
    街机格斗             = EffectMeta("街机格斗", True, "7511254116488842557", "7511254116488842557", "c71630bdb4ddb60ed26ccb310c6ea96c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    表面模糊             = EffectMeta("表面模糊", True, "7395473608463666438", "7395473608463666438", "a1a88c0fa966966cbe13373ad2b7382d", [
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_sharpen: 默认80%, 0% ~ 100%"""
    被黑入的显示器       = EffectMeta("被黑入的显示器", True, "7532828159071358269", "7532828159071358269", "78ecf5627b927030d05a76da17b19dd1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    裂开的闪光           = EffectMeta("裂开的闪光", True, "7512074051431468349", "7512074051431468349", "977fbe4e2423fa811481a34eb40cd448", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    西海岸涂鸦           = EffectMeta("西海岸涂鸦", True, "7452652769455903249", "7452652769455903249", "cd245412884199a350400bffdb8a6ea8", [])
    视差堆叠             = EffectMeta("视差堆叠", True, "7516866432127356221", "7516866432127356221", "b40feead49ecde06ca12c8d2b00ea2ff", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    视频分割             = EffectMeta("视频分割", True, "7399471076859759877", "7399471076859759877", "d4dd2d402c07ceae4cc5b5c73773b011", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.670, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认67%, 0% ~ 100%"""
    角落夹击             = EffectMeta("角落夹击", True, "7520098913232096573", "7520098913232096573", "955bb13c4168f12c84353f313b33f273", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    解压图框             = EffectMeta("解压图框", True, "7488966848503893309", "7488966848503893309", "8ed3377d373b995d846444cd95b52848", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    诡异分割             = EffectMeta("诡异分割", True, "7399467918225935622", "7399467918225935622", "2755d9f7c9b46356a832ef58ef405df7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.630, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认63%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认70%, 0% ~ 100%"""
    诡异故障             = EffectMeta("诡异故障", True, "7426268503746810369", "7426268503746810369", "eec29209c7ab182a5fa9335ee5b7d933", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%"""
    负变异               = EffectMeta("负变异", True, "7519730725709466933", "7519730725709466933", "902066b10852adc22e3de6403e19328c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    负向滚动             = EffectMeta("负向滚动", True, "7510144494348635445", "7510144494348635445", "3991d0297168636d55a34c4cf63d27e2", [
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认0%, 0% ~ 100%"""
    负片分屏             = EffectMeta("负片分屏", True, "7399466860137237765", "7399466860137237765", "5a980a6a4a707fc1ad13caff77e3926a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认33%, 0% ~ 100%"""
    负片切割             = EffectMeta("负片切割", True, "7512274737435790593", "7512274737435790593", "315a92765fbdaad3202b2eee3ba76304", [])
    负片崩溃             = EffectMeta("负片崩溃", True, "7526861612511186229", "7526861612511186229", "baa108de09b54066e98e0c0a44967d73", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    负片拖影             = EffectMeta("负片拖影", True, "7399466827966975237", "7399466827966975237", "3ec3cd74c41f47a6e96720b8a96e17e3", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.390, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.950, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认95%, 0% ~ 100%
    effects_adjust_intensity: 默认39%, 0% ~ 100%
    effects_adjust_range: 默认95%, 0% ~ 100%"""
    负片描边             = EffectMeta("负片描边", True, "7436323942211523073", "7436323942211523073", "08ff70bd94ad0dc1ffac10995fca7b75", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    负片涂鸦             = EffectMeta("负片涂鸦", True, "7395466597961420038", "7395466597961420038", "0861963efbe5f75a06b61ea93cd76343", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    负片涂鸦_II          = EffectMeta("负片涂鸦 II", True, "7395469549094685958", "7395469549094685958", "02590242d94571bb62a8635b4fd5a3f7", [
                              EffectParam("effects_adjust_texture", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.320, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认75%, 0% ~ 100%
    effects_adjust_noise: 默认32%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    负片涂鸦_III         = EffectMeta("负片涂鸦 III", True, "7399464689287040261", "7399464689287040261", "96a028c1ac17f22a452c1e012d47f3ed", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认0%, 0% ~ 100%"""
    负片游移             = EffectMeta("负片游移", True, "7399470340239396102", "7399470340239396102", "bc811feeac5b5e4608cbb80c99a07d46", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%"""
    负片滑动             = EffectMeta("负片滑动", True, "7532431517566438709", "7532431517566438709", "eac4f8eadd7c4c804b905221b07ab170", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    负片漫画扭曲         = EffectMeta("负片漫画扭曲", True, "7517131139899755777", "7517131139899755777", "e06d71be69f6d65c4c609721ddf41079", [])
    负片闪电             = EffectMeta("负片闪电", True, "7488910617466735888", "7488910617466735888", "d6772f91ffa5d8b69df1ba48c8126e69", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    负片频闪             = EffectMeta("负片频闪", True, "7399472161422937350", "7399472161422937350", "c737112d913d14f6cc8871dbc51c8013", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认45%, 0% ~ 100%
    effects_adjust_filter: 默认85%, 0% ~ 100%"""
    负相擦除             = EffectMeta("负相擦除", True, "7526811536048917813", "7526811536048917813", "4642ca88e60bb50541ff2d482f30166d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    贴身粒子             = EffectMeta("贴身粒子", True, "7444139634029761041", "7444139634029761041", "35a5a86c96dbc1f8510cafb11240f804", [
                              EffectParam("effects_adjust_number", 0.180, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.340, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.240, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认18%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_size: 默认10%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认24%, 0% ~ 100%"""
    赛博故障             = EffectMeta("赛博故障", True, "7480164692896353589", "7480164692896353589", "2c85eb4134a0513d6bc1060b526b0200", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    超大光斑             = EffectMeta("超大光斑", True, "7395468542847618309", "7395468542847618309", "8f525928d0c73912e59702928d728ef2", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_number: 默认10%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认20%, 0% ~ 100%"""
    超强光感             = EffectMeta("超强光感", True, "7534209189707615541", "7534209189707615541", "97a2cda79fe14cb69ab9b0969e2de0e3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    超强锐化             = EffectMeta("超强锐化", True, "7395468877502631174", "7395468877502631174", "6e974f19820f7b1c56381ca6adb6ccd2", [
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    超强锐化_II          = EffectMeta("超强锐化 II", True, "7399465350317804806", "7399465350317804806", "f8bb528805bfb0fc8b503c4333d11b11", [
                              EffectParam("effects_adjust_sharpen", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认90%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    超级聚焦             = EffectMeta("超级聚焦", True, "7475273359295532341", "7475273359295532341", "4047f466f08ba0b98016ea755260a640", [
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认40%, 0% ~ 100%"""
    超级色彩震撼         = EffectMeta("超级色彩震撼", True, "7496001572862725429", "7496001572862725429", "44d7a870b6154942274b7bc6e687bdd1", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    超负面               = EffectMeta("超负面", True, "7506415249596108085", "7506415249596108085", "39ed77de7be74f008a0105f373d787a7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    超速模糊             = EffectMeta("超速模糊", True, "7519552120538811709", "7519552120538811709", "e2ce83579ace67ae4423f849f47a3bdd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    跟随运镜             = EffectMeta("跟随运镜", True, "7399471976714128645", "7399471976714128645", "b5d000eed1ce05e5e14f1ee54d868d5d", [
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.150, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认15%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认15%, 0% ~ 100%"""
    跳动空间             = EffectMeta("跳动空间", True, "7507509483195731217", "7507509483195731217", "e91d9aa39faab2e0b19981fe3ac0992f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    跳色四宫格           = EffectMeta("跳色四宫格", True, "7452646287318454801", "7452646287318454801", "7472057d48afda752984c3d22d84cb03", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    跷跷板滑动           = EffectMeta("跷跷板滑动", True, "7515833464000646461", "7515833464000646461", "1e1c3f563f605418a06d7638b44cf77c", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    蹦迪彩光             = EffectMeta("蹦迪彩光", True, "7399470257078816005", "7399470257078816005", "355d46c4bff8c9b6286f3324fb6e27b7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    车窗_II              = EffectMeta("车窗 II", True, "7399465732343418117", "7399465732343418117", "4d3830f0f3e83381c567c6137f62feeb", [
                              EffectParam("effects_adjust_range", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认55%, 0% ~ 100%
    effects_adjust_intensity: 默认45%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    车窗影               = EffectMeta("车窗影", True, "7399467960076668165", "7399467960076668165", "d37540d91f173eaeef40a3ac6a2de42e", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    轮廓错误             = EffectMeta("轮廓错误", True, "7516546597686234421", "7516546597686234421", "a4ca6b73ad823ddc9c2d17bafcb8b880", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    轰动摇动             = EffectMeta("轰动摇动", True, "7467214220761910581", "7467214220761910581", "33fdf7331900cd60462de67220076fb0", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    轰鸣闪光             = EffectMeta("轰鸣闪光", True, "7459772288313937213", "7459772288313937213", "5be922c60033c0175f754a49d29fdc29", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    轻微故障             = EffectMeta("轻微故障", True, "7426269244007911952", "7426269244007911952", "437d6da122ab141fd4988472a2150aa9", [
                              EffectParam("effects_adjust_speed", 0.091, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认9%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    轻流                 = EffectMeta("轻流", True, "7507978738584309053", "7507978738584309053", "d1c9dcadd9943b288b532aa1d33e12d8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    边缘加色             = EffectMeta("边缘加色", True, "7399471712531713285", "7399471712531713285", "1d5ac14cba4e6e8559cacd2c37d62c43", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    边缘加色_II          = EffectMeta("边缘加色 II", True, "7399469721789271301", "7399469721789271301", "ff84c6f908752eda1298021c2e382e0f", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    边缘加色_III         = EffectMeta("边缘加色 III", True, "7399471401343798534", "7399471401343798534", "dce8524b38da9a484412abd57274b821", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    边缘荧光             = EffectMeta("边缘荧光", True, "7399468568858905862", "7399468568858905862", "49db41dc5ace9aa5478f46c7beb9559b", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    过热切片             = EffectMeta("过热切片", True, "7509530600106118453", "7509530600106118453", "0db8ae660fd71390207bb637f20b1bca", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认33%, 0% ~ 100%"""
    运镜快门             = EffectMeta("运镜快门", True, "7493340469691256081", "7493340469691256081", "dbcbefbfb4e6ff4a1e94f5591f0eedca", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    迷幻故障             = EffectMeta("迷幻故障", True, "7399469507867151622", "7399469507867151622", "5ddfb1bd3479179af2c0ec0026b57e3e", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%"""
    迷幻模糊             = EffectMeta("迷幻模糊", True, "7395468812021157126", "7395468812021157126", "b898048f4457baae9d3e2b37520db6cf", [
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.300, 0.000, 0.500),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_blur: 默认30%, 0% ~ 100%
    effects_adjust_luminance: 默认30%, 0% ~ 50%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认100%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认100%, 0% ~ 100%"""
    迷幻荡漾             = EffectMeta("迷幻荡漾", True, "7395469106645880069", "7395469106645880069", "1ab6e40160a674cd19de3ade157a3d0b", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.550, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认55%, 0% ~ 100%
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    迷幻轮廓             = EffectMeta("迷幻轮廓", True, "7500971680571903293", "7500971680571903293", "b783af0033e916ff019e1a8c48d2d8a1", [
                              EffectParam("effects_adjust_intensity", 0.067, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认7%, 0% ~ 100%"""
    迷幻震动             = EffectMeta("迷幻震动", True, "7399467337235254534", "7399467337235254534", "e28a153a03d2dcf1a12384712196bc07", [
                              EffectParam("effects_adjust_distortion", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认65%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认75%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_color: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认40%, 0% ~ 100%"""
    迷离                 = EffectMeta("迷离", True, "7399465771090414853", "7399465771090414853", "7c2f3180ded615ee30e6d1a5bafc5392", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    迷醉蝴蝶             = EffectMeta("迷醉蝴蝶", True, "7399464859101859078", "7399464859101859078", "08f1ceba06fcc0e25a1342bc243a549d", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.300, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_number: 默认30%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%"""
    迷雾消散             = EffectMeta("迷雾消散 ", True, "7399464944883797253", "7399464944883797253", "2d4fc50b9d2a806a391a9bff06624e74", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    逆光对焦             = EffectMeta("逆光对焦", True, "7399469012566002949", "7399469012566002949", "ccba5bb5c3656e951ce7e6ec272dc606", [
                              EffectParam("effects_adjust_soft", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_soft: 默认70%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认33%, 0% ~ 100%"""
    选中框               = EffectMeta("选中框", True, "7399469938068524294", "7399469938068524294", "7f554e89af822763f78abd7c146cc19f", [])
    透视九宫格           = EffectMeta("透视九宫格", True, "7524064416212520208", "7524064416212520208", "b036e60530513607f73e8290ff6c28a3", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    速切闪黑             = EffectMeta("速切闪黑", True, "7508897852182056193", "7508897852182056193", "495542d9c282090daf76619a075a0a39", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    遮幕倒计时           = EffectMeta("遮幕倒计时", True, "7519001413259660560", "7519001413259660560", "3f16521dd5046e70bc1efe840fc9b9c0", [])
    重叠世界             = EffectMeta("重叠世界", True, "7501952769880788240", "7501952769880788240", "75e43c97d59b5d0194380abcb665eb20", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    重叠复制             = EffectMeta("重叠复制", True, "7530931692396236093", "7530931692396236093", "5193d4dfbbe6e3280adadce7c767be22", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    重复击打             = EffectMeta("重复击打", True, "7516838978054589757", "7516838978054589757", "7ae279d41cfda511aa21072cff845615", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    重复栅格             = EffectMeta("重复栅格", True, "7521482072578395393", "7521482072578395393", "fd55922b891ac16dc30a5cb432ac2da7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    重复震闪             = EffectMeta("重复震闪", True, "7399466247311707397", "7399466247311707397", "63a7958ffc3e6a73d3b9556f7ca04381", [
                              EffectParam("effects_adjust_luminance", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.250, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认80%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_blur: 默认70%, 0% ~ 100%
    effects_adjust_range: 默认25%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    重新上色闪耀         = EffectMeta("重新上色闪耀", True, "7521274246048402749", "7521274246048402749", "0b83a6a52dae6c12bff0bc709fbe94f8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    金片                 = EffectMeta("金片", True, "7399464053074185477", "7399464053074185477", "098e6d6982f2b6759b61e534573ce001", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金粉_III             = EffectMeta("金粉 III", True, "7399470643441388805", "7399470643441388805", "752d69c565983fbed6bb13c3d8542ca7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金粉飘落             = EffectMeta("金粉飘落", True, "7456798559417930257", "7456798559417930257", "d3cf50bb2189d96f515bbbcfdb383ec1", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.150, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认15%, 0% ~ 100%"""
    金色大爆炸           = EffectMeta("金色大爆炸", True, "7512488287714561333", "7512488287714561333", "f6041d5889319153b10d53d6169cdc03", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    金色的雪             = EffectMeta("金色的雪", True, "7465692165969169725", "7465692165969169725", "5fdef574e16d9cbec50a04ad1770c076", [
                              EffectParam("effects_adjust_speed", 0.107, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    金色碎片             = EffectMeta("金色碎片", True, "7399468579650882821", "7399468579650882821", "a24eabdabec50f5d52f7e6fb099c899c", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_noise: 默认30%, 0% ~ 100%"""
    金色负片             = EffectMeta("金色负片", True, "7482612489495006519", "7482612489495006519", "ea23c4ffb7eb22768d2f19af3dea7ef7", [])
    金色辉光             = EffectMeta("金色辉光", True, "7446716461734744592", "7446716461734744592", "cd968a21dec5e06bf4b85ea87c0312df", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    金色雪花             = EffectMeta("金色雪花", True, "7445221319781650945", "7445221319781650945", "c45225f02ac066e85ca418434e995970", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    金色魔法边框         = EffectMeta("金色魔法边框", True, "7399464331236166917", "7399464331236166917", "859e706706e662aed2b89e2585165566", [])
    金边闪烁             = EffectMeta("金边闪烁", True, "7399467288409263365", "7399467288409263365", "46b93ae5afcb00ecface4fd485014d9c", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%"""
    钻石碎片             = EffectMeta("钻石碎片", True, "7399470461379185926", "7399470461379185926", "7c201b5477a02796bddb330377b7fce7", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    钻石闪光             = EffectMeta("钻石闪光", True, "7522794242138262837", "7522794242138262837", "6d32ed5fc1966e8c6f973748276d6abf", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    铅笔涂鸦             = EffectMeta("铅笔涂鸦", True, "7414191272803585286", "7414191272803585286", "c76bc693a18e8dd16ff56d359564fecf", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    锐化负片             = EffectMeta("锐化负片", True, "7508672345494572349", "7508672345494572349", "3557e5e945777b70b5b7319ab97ef16f", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    错位                 = EffectMeta("错位", True, "7510514048945933629", "7510514048945933629", "52846af07a760994db9d490fae018338", [
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认50%, 0% ~ 100%"""
    锯齿像素             = EffectMeta("锯齿像素", True, "7461897836808965429", "7461897836808965429", "0aa11a322b91888e583dac47a01bc51a", [
                              EffectParam("effects_adjust_blur", 0.505, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    锯齿缩放             = EffectMeta("锯齿缩放", True, "7516057761965264181", "7516057761965264181", "3880953eaae7bccf074a9269c07a9d95", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    镜头宠儿             = EffectMeta("镜头宠儿", True, "7530246518779972917", "7530246518779972917", "4c203fe851896318a1f072712b4c7ea6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    镜头模糊             = EffectMeta("镜头模糊", True, "7399469294721027334", "7399469294721027334", "affe5e5a5b902d8d692c34b9d7a49f38", [
                              EffectParam("effects_adjust_range", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认60%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    镜面星星             = EffectMeta("镜面星星", True, "7414192219151666437", "7414192219151666437", "2ce1249a13defb5786492e80e6d94192", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    长虹玻璃             = EffectMeta("长虹玻璃", True, "7399471674233556230", "7399471674233556230", "2f5917be32e664eef67419212e54cad0", [
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%
    effects_adjust_rotate: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    闪亮亮焦点           = EffectMeta("闪亮亮焦点", True, "7512049639227477309", "7512049639227477309", "3404b06f14336b8710073a6c977021e7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪亮小星星           = EffectMeta("闪亮小星星", True, "7517816806996774145", "7517816806996774145", "0dd0c447b321fc4e8bb1223da65a929b", [
                              EffectParam("effects_adjust_speed", 0.250, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认25%, 0% ~ 100%"""
    闪亮星尘             = EffectMeta("闪亮星尘", True, "7493850383119420725", "7493850383119420725", "1192acd5c63f2d7daf323cc5336a7820", [
                              EffectParam("effects_adjust_speed", 0.262, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认26%, 0% ~ 100%"""
    闪亮登场             = EffectMeta("闪亮登场", True, "7399471410273471749", "7399471410273471749", "a1c096efd5f98b438ab0f762bea9c41a", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    闪亮的粉彩           = EffectMeta("闪亮的粉彩", True, "7511918835260345653", "7511918835260345653", "cbc0169f28fc6150e9ab446a5fac8cac", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪亮裂纹             = EffectMeta("闪亮裂纹", True, "7530186977262554429", "7530186977262554429", "4606758bc6668566d1456893c4fe434f", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.667, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.010, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认67%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认1%, 0% ~ 100%"""
    闪亮飞机             = EffectMeta("闪亮飞机", True, "7494217746968759613", "7494217746968759613", "ac19f8e6c55f9fb15c69748397bbfe92", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪光                 = EffectMeta("闪光", True, "7399471277012012294", "7399471277012012294", "464e44270e1180df009025956ef3a9c0", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.060, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认6%, 0% ~ 100%
    effects_adjust_noise: 默认20%, 0% ~ 100%
    effects_adjust_blur: 默认60%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    闪光上移             = EffectMeta("闪光上移", True, "7497084771856633105", "7497084771856633105", "68066556bc7d3e459e32eeb60514ea11", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    闪光摇动             = EffectMeta("闪光摇动", True, "7509785489126346037", "7509785489126346037", "71be728e0c54ec034008432d29e3c69f", [
                              EffectParam("effects_adjust_speed", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认20%, 0% ~ 100%"""
    闪光波浪             = EffectMeta("闪光波浪", True, "7501954871109651728", "7501954871109651728", "77acc4d8af83c41d1c64bc785aae43f7", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪光灯_I             = EffectMeta("闪光灯 I", True, "7395470405806394630", "7395470405806394630", "77651b697b0bb5a00b6fa6027f82d8af", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.650, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认65%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    闪光灯_II            = EffectMeta("闪光灯 II", True, "7395464766954802438", "7395464766954802438", "d57684957de7a84ab73d1d0cfde0cd4e", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    闪光灯_IV            = EffectMeta("闪光灯 IV", True, "7399469147907837190", "7399469147907837190", "db710dc6b5ea5b2f46595480d06d0d7d", [
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    闪光翻转             = EffectMeta("闪光翻转", True, "7531966286142721296", "7531966286142721296", "0506c44e0c1e3dae07d5cd18b3bc59e3", [
                              EffectParam("effects_adjust_luminance", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_luminance: 默认0%, 0% ~ 100%"""
    闪光跳动             = EffectMeta("闪光跳动", True, "7399464712909507846", "7399464712909507846", "e9233af07e9bce27ddca5bafc32eba63", [
                              EffectParam("effects_adjust_speed", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    闪光震动             = EffectMeta("闪光震动", True, "7399463959478291717", "7399463959478291717", "17416edf590446330a683c9eb4f5c9e3", [
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.580, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_range: 默认58%, 0% ~ 100%
    effects_adjust_background_animation: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪击                 = EffectMeta("闪击", True, "7517595077619830077", "7517595077619830077", "a4e9a098ee05cc8eefcc0d8dcc50ea6b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪刺晃影             = EffectMeta("闪刺晃影", True, "7519356411348913425", "7519356411348913425", "76531876bc1c07b2907498961b10ab98", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪动                 = EffectMeta("闪动", True, "7399465469012430085", "7399465469012430085", "0bc9ee34335ba4f9d75e4a2b21f4d6e5", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪动光影             = EffectMeta("闪动光影", True, "7520018238919413009", "7520018238919413009", "e283d29c635a27958b4f87874e810f10", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪动光斑             = EffectMeta("闪动光斑", True, "7399472112223669510", "7399472112223669510", "d7c42c303074967c0cad7c7a6adfe896", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    闪动拖影             = EffectMeta("闪动拖影", True, "7508920142714211585", "7508920142714211585", "3f1f4232eae583c3c6715654de48201a", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪动页面             = EffectMeta("闪动页面", True, "7525465607429442869", "7525465607429442869", "d8f73d9229dbfe2de2d558527ab7d15d", [
                              EffectParam("effects_adjust_speed", 0.429, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.010, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认43%, 0% ~ 100%
    effects_adjust_size: 默认1%, 0% ~ 100%"""
    闪屏雷电             = EffectMeta("闪屏雷电", True, "7399467146339716357", "7399467146339716357", "edd537366858130e593a074d28503dc7", [
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.800, 0.000, 1.000),
                              EffectParam("sticker", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_distortion: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认80%, 0% ~ 100%
    sticker: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    闪烁迪斯科           = EffectMeta("闪烁迪斯科", True, "7521668377052450109", "7521668377052450109", "24703c613602e8d06e72b4edaf3904d4", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪爆裂影             = EffectMeta("闪爆裂影", True, "7514843153279503632", "7514843153279503632", "25cb6016d2a6131c28263db27d21e941", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪白_II              = EffectMeta("闪白 II", True, "7399471480423189765", "7399471480423189765", "631162213ead8ced21aa7936bae06390", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 2.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 200%"""
    闪粉胶片             = EffectMeta("闪粉胶片", True, "7450390477871780369", "7450390477871780369", "bc79e33a6136c9f82ea8f42f3b60b942", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    闪闪发光             = EffectMeta("闪闪发光", True, "7399465788387675397", "7399465788387675397", "45e7f3bd70db43cc7d0ab6642be58012", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    闪闪发光_II          = EffectMeta("闪闪发光 II", True, "7399471349032340741", "7399471349032340741", "9a723996777d5f56d3802b53c8cc46bb", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_rotate: 默认100%, 0% ~ 100%"""
    闪闪蝴蝶             = EffectMeta("闪闪蝴蝶", True, "7399465395402345734", "7399465395402345734", "8742efc3bec68f67c01a4750b9c5b3c1", [
                              EffectParam("effects_adjust_size", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.030, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.850, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.950, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.820, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认3%, 0% ~ 100%
    effects_adjust_number: 默认3%, 0% ~ 100%
    effects_adjust_filter: 默认85%, 0% ~ 100%
    effects_adjust_intensity: 默认95%, 0% ~ 100%
    effects_adjust_speed: 默认82%, 0% ~ 100%"""
    阴影节拍             = EffectMeta("阴影节拍", True, "7515507277005081909", "7515507277005081909", "3e9e2101501b1da8d1f1096267dad5a5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    阴影负片             = EffectMeta("阴影负片", True, "7399468090834029829", "7399468090834029829", "88be03e7edfd52064c6995907f9be0ad", [
                              EffectParam("effects_adjust_range", 0.730, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_range: 默认73%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_size: 默认90%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    阻隔错误             = EffectMeta("阻隔错误", True, "7525096434656496949", "7525096434656496949", "9065d55eeeca1f34e4dec132b560f6ad", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    隐形现身             = EffectMeta("隐形现身", True, "7522556028756479249", "7522556028756479249", "a1bbd13787cfb7a5d0a47cddee215070", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    隐身人               = EffectMeta("隐身人", True, "7510138014480338193", "7510138014480338193", "3b8994115edbdcb5f6f5752b0a4e3dac", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%"""
    难过_II              = EffectMeta("难过 II", True, "7399466929569746181", "7399466929569746181", "813a84ae4b767072c35c958821e1b944", [])
    雨天                 = EffectMeta("雨天", True, "7530862388225133885", "7530862388225133885", "265cc07d2396995cd25f0c551ad9152c", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%"""
    雨季_I               = EffectMeta("雨季 I", True, "7399471982066126086", "7399471982066126086", "fe78f4e40b597e3170f46831622f8e06", [
                              EffectParam("effects_adjust_blur", 0.160, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认16%, 0% ~ 80%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%"""
    雨季_II              = EffectMeta("雨季 II", True, "7399466782085500165", "7399466782085500165", "e74b25973452e4c4b30e9afc39cf41d7", [
                              EffectParam("effects_adjust_blur", 0.160, 0.000, 0.800),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000)])
    """参数:
    effects_adjust_blur: 默认16%, 0% ~ 80%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认34%, 0% ~ 100%"""
    雨滴                 = EffectMeta("雨滴", True, "7409872299135962374", "7409872299135962374", "2ed20557bb6b691f66e05aafdbb13595", [
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认0%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_range: 默认0%, 0% ~ 100%"""
    雨滴晕开             = EffectMeta("雨滴晕开", True, "7399468051688623365", "7399468051688623365", "2bded973503eaa2ce5644ef44354d90d", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    雪仙子               = EffectMeta("雪仙子", True, "7517133842952604981", "7517133842952604981", "97b7d1b3b1de14659db92cbd5e48399d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    雪花冲屏             = EffectMeta("雪花冲屏", True, "7399470320958164230", "7399470320958164230", "2c07239e54041e85518b111b1ad8eb86", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    雪花变色             = EffectMeta("雪花变色", True, "7446316654000099856", "7446316654000099856", "8ede7d0c27d9423da48f3226a8384f95", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    雪花散落             = EffectMeta("雪花散落", True, "7449258379580543505", "7449258379580543505", "2ad9203b34bf8f5fd8bd1672f62dcbc8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    雪花闪闪             = EffectMeta("雪花闪闪", True, "7399467507288902918", "7399467507288902918", "84397e7b2a3a485a6f40e170b32fd48c", [
                              EffectParam("effects_adjust_size", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认70%, 0% ~ 100%
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_color: 默认50%, 0% ~ 100%"""
    雪雾                 = EffectMeta("雪雾", True, "7395471178091040005", "7395471178091040005", "bc0e8be4f1a2d7171824311ce9e57c44", [
                              EffectParam("sticker", 0.280, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.900, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.300, 0.000, 1.000)])
    """参数:
    sticker: 默认28%, 0% ~ 100%
    effects_adjust_filter: 默认90%, 0% ~ 100%
    effects_adjust_texture: 默认90%, 0% ~ 100%
    effects_adjust_background_animation: 默认30%, 0% ~ 100%"""
    雾气                 = EffectMeta("雾气", True, "7399471802361105669", "7399471802361105669", "bdda3043cfa04aa56d2806ada93367ae", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    雾窗                 = EffectMeta("雾窗", True, "7488783527509495093", "7488783527509495093", "0eff15d3123d7ac2a6c6cd7e5dfbf8f4", [
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    震动光束             = EffectMeta("震动光束", True, "7395466483096210693", "7395466483096210693", "71ec34ce27447c6d33a8f46857d8a642", [
                              EffectParam("effects_adjust_intensity", 0.420, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.160, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.490, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.750, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认42%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认16%, 0% ~ 100%
    effects_adjust_luminance: 默认49%, 0% ~ 100%
    effects_adjust_blur: 默认100%, 0% ~ 100%
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_range: 默认75%, 0% ~ 100%"""
    震动失真             = EffectMeta("震动失真", True, "7510813322657238325", "7510813322657238325", "4ca989f23f11b57c4a5053b371f75023", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%"""
    震动屏闪             = EffectMeta("震动屏闪", True, "7399469780043894021", "7399469780043894021", "bde09b5a2b7f8097343bbf1f55203a07", [
                              EffectParam("effects_adjust_speed", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认30%, 0% ~ 100%
    effects_adjust_intensity: 默认70%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认70%, 0% ~ 100%"""
    震动扫光             = EffectMeta("震动扫光", True, "7395469084944567558", "7395469084944567558", "3b86c556d5a92c8937b1120823bc34b2", [
                              EffectParam("effects_adjust_intensity", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.400, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认40%, 0% ~ 100%
    effects_adjust_speed: 默认60%, 0% ~ 100%
    effects_adjust_color: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认40%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认40%, 0% ~ 100%"""
    震动模糊             = EffectMeta("震动模糊", True, "7395474293095763206", "7395474293095763206", "5fd07aa6f1051732b710181c578cc2ce", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.750, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认75%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认60%, 0% ~ 100%"""
    震撼倒计时           = EffectMeta("震撼倒计时", True, "7493333125095886097", "7493333125095886097", "66dab57a6fe6da6c0ef5d67365492556", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    震闪渐黑             = EffectMeta("震闪渐黑", True, "7399465771090349317", "7399465771090349317", "dfddc3aedd22941d50e768623fbd60ba", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.100, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 10% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    震颤泛光             = EffectMeta("震颤泛光", True, "7414191072433147142", "7414191072433147142", "df1d4b0cd8a580af848889d4cc00cd87", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_soft", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_soft: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认33%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    霓虹印记             = EffectMeta("霓虹印记", True, "7524341118692019509", "7524341118692019509", "644997c2b56e33edca2bf48700b8bbe9", [
                              EffectParam("effects_adjust_speed", 0.143, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认14%, 0% ~ 100%"""
    霓虹彩边             = EffectMeta("霓虹彩边", True, "7509340213584350480", "7509340213584350480", "105f253ffda08f381062b240115796db", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_number", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_number: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    霓虹摇摆             = EffectMeta("霓虹摇摆", True, "7399468706759183622", "7399468706759183622", "ead112f7fba9cc2c2a448ebcc028b4a7", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_luminance: 默认100%, 0% ~ 100%"""
    霓虹旋转             = EffectMeta("霓虹旋转", True, "7508979826707942709", "7508979826707942709", "8184b1f03164742444067016df2fd2fd", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    霓虹碰撞             = EffectMeta("霓虹碰撞", True, "7526832679740902709", "7526832679740902709", "3b223bba5ebcaa6c3b40e20c609c84c8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    霓虹闪乱             = EffectMeta("霓虹闪乱", True, "7520411538956619025", "7520411538956619025", "14ab73d9df9e188c6c4250c037b0de84", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    霓虹鬼影             = EffectMeta("霓虹鬼影", True, "7516475067698515261", "7516475067698515261", "a6b41bfd3e57474c043ca2a72e54ff1e", [
                              EffectParam("effects_adjust_speed", 0.111, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认11%, 0% ~ 100%"""
    音乐播放器           = EffectMeta("音乐播放器", True, "7475635004979088701", "7475635004979088701", "b558e5ec011b00513d6d0a9cdb9e8a97", [
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.762, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认76%, 0% ~ 100%
    effects_adjust_background_animation: 默认33%, 0% ~ 100%"""
    音乐播放器_II        = EffectMeta("音乐播放器 II", True, "7489011034687130933", "7489011034687130933", "70420f1eb46721dfb6c1eea30c172df6", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%
    effects_adjust_background_animation: 默认50%, 0% ~ 100%"""
    频繁衰变             = EffectMeta("频繁衰变", True, "7533270749730180413", "7533270749730180413", "e8609aa10cbb48b6c3b7c526cc6ab74a", [
                              EffectParam("effects_adjust_intensity", 0.200, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认20%, 0% ~ 100%
    effects_adjust_noise: 默认20%, 0% ~ 100%"""
    颗粒爆闪             = EffectMeta("颗粒爆闪", True, "7514218276335930625", "7514218276335930625", "ae2f21d40b605790314eaeda71670044", [])
    颗粒特效             = EffectMeta("颗粒特效", True, "7480852119097068853", "7480852119097068853", "d5f3848694790be86020fccfe595f184", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_texture: 默认50%, 0% ~ 100%"""
    颗粒金黄色           = EffectMeta("颗粒金黄色", True, "7487654762490481973", "7487654762490481973", "a36c5c6d4a604a4b6071ea29958d69e4", [
                              EffectParam("effects_adjust_speed", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认100%, 0% ~ 100%
    effects_adjust_noise: 默认50%, 0% ~ 100%"""
    颗粒雾化             = EffectMeta("颗粒雾化", True, "7515402107508346165", "7515402107508346165", "530fcfc4c8219ca4979bef99fa0df520", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    颜色调整             = EffectMeta("颜色调整", True, "7514186078853532981", "7514186078853532981", "106164c659c61d08ab53577dfaa231ba", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    颜色频闪             = EffectMeta("颜色频闪", True, "7395467421525593349", "7395467421525593349", "c077c1e309c71b95691cd728c1f09566", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.300, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_color: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_intensity: 默认30%, 0% ~ 100%
    effects_adjust_blur: 默认50%, 0% ~ 100%"""
    颠倒分割             = EffectMeta("颠倒分割", True, "7503137226394586421", "7503137226394586421", "fb66fc401d80bcf4d942c406c73cc50b", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_noise", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_chromatic", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_noise: 默认100%, 0% ~ 100%
    effects_adjust_horizontal_chromatic: 默认50%, 0% ~ 100%"""
    风扇旋转             = EffectMeta("风扇旋转", True, "7520198267141950781", "7520198267141950781", "63ef146ddd5323625dcffd1f2234b870", [
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    飘落花瓣_II          = EffectMeta("飘落花瓣 II", True, "7399466068286246150", "7399466068286246150", "c39b069df62f67308de64f86b920dbbd", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    飞吻                 = EffectMeta("飞吻", True, "7463452240066481469", "7463452240066481469", "1781d51e44517c85bf614e1d35791ac0", [
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认50%, 0% ~ 100%"""
    飞机窗               = EffectMeta("飞机窗", True, "7415867772573323777", "7415867772573323777", "5a574229dd6bb651749f67b0ad3d1754", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.330, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_size: 默认0%, 0% ~ 100%
    effects_adjust_luminance: 默认33%, 0% ~ 100%"""
    飞舞的照片           = EffectMeta("飞舞的照片", True, "7513132849592061245", "7513132849592061245", "9fd5075d8288ebc8c04c6f880085d371", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    飞舞花瓣             = EffectMeta("飞舞花瓣", True, "7472644534304820533", "7472644534304820533", "f692ee15c5a1f7cac7c29831bdf05cac", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    马尾烟花             = EffectMeta("马尾烟花", True, "7463388577406128656", "7463388577406128656", "4ab7dac6b5d24bf7b1c4a91fc64081bf", [
                              EffectParam("effects_adjust_size", 0.201, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.100, 0.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认20%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_luminance: 默认50%, 0% ~ 100%
    effects_adjust_filter: 默认10%, 0% ~ 100%
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    马赛克人物投影       = EffectMeta("马赛克人物投影", True, "7498203525801856257", "7498203525801856257", "4b5f573600286ec41fe6803da43daf0a", [])
    马赛克变焦           = EffectMeta("马赛克变焦", True, "7399469878148746501", "7399469878148746501", "cb1be168772058aede4f8ccccdff200b", [
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.800, 0.000, 1.000),
                              EffectParam("effects_adjust_luminance", 0.450, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_size: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认80%, 0% ~ 100%
    effects_adjust_luminance: 默认45%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    马赛克群             = EffectMeta("马赛克群", True, "7496397470881074493", "7496397470881074493", "21bca79adc1582f62e8bf1818baaa480", [
                              EffectParam("effects_adjust_speed", 0.167, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认17%, 0% ~ 100%"""
    高光扫屏             = EffectMeta("高光扫屏", True, "7517108516432268545", "7517108516432268545", "b303b274ae2c145b85e47a26b7ec3a30", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_distortion: 默认50%, 0% ~ 100%"""
    高饱和负闪           = EffectMeta("高饱和负闪", True, "7517501742615891201", "7517501742615891201", "e870b7c28f8fe44c7cd6879f853d7c72", [])
    鬼影设备             = EffectMeta("鬼影设备", True, "7508893189315513653", "7508893189315513653", "a4f4fbd2520a6bca761b5dc95e55e526", [
                              EffectParam("effects_adjust_sharpen", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_blur", 0.200, 0.000, 1.000)])
    """参数:
    effects_adjust_sharpen: 默认50%, 0% ~ 100%
    effects_adjust_blur: 默认20%, 0% ~ 100%"""
    魔法                 = EffectMeta("魔法", True, "7399467736042130694", "7399467736042130694", "98296a4bc028cef2bb3b06ffbb490faf", [
                              EffectParam("effects_adjust_speed", 0.336, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.802, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认34%, 0% ~ 100%
    effects_adjust_filter: 默认80%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    魔法边框_II          = EffectMeta("魔法边框 II", True, "7399470760068173062", "7399470760068173062", "6f23fdea097c9e547d934e0c134cd0c9", [])
    魔法闪光             = EffectMeta("魔法闪光", True, "7525466112197184821", "7525466112197184821", "05611035259bf49416f72891a8dfb6d5", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    鱼眼IV               = EffectMeta("鱼眼IV", True, "7399472827910343942", "7399472827910343942", "ae54d40500bd55859922c0afaf05d42c", [
                              EffectParam("effects_adjust_intensity", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.350, 0.000, 1.000),
                              EffectParam("effects_adjust_texture", 0.550, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认60%, 0% ~ 100%
    effects_adjust_filter: 默认60%, 0% ~ 100%
    effects_adjust_size: 默认35%, 0% ~ 100%
    effects_adjust_texture: 默认55%, 0% ~ 100%"""
    鱼眼_II              = EffectMeta("鱼眼 II", True, "7399468161021594886", "7399468161021594886", "3961e7c38420d89d64c5d267a3068254", [
                              EffectParam("effects_adjust_speed", 0.000, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认0%, 0% ~ 100%
    effects_adjust_filter: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认80%, 0% ~ 100%"""
    鱼眼_III             = EffectMeta("鱼眼 III", True, "7399464845738855685", "7399464845738855685", "49646236952c1ba601086eccb7b6e7ed", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_distortion", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.300, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%
    effects_adjust_intensity: 默认100%, 0% ~ 100%
    effects_adjust_distortion: 默认100%, 0% ~ 100%
    effects_adjust_range: 默认30%, 0% ~ 100%"""
    鱼眼涂鸦             = EffectMeta("鱼眼涂鸦", True, "7454042506506801680", "7454042506506801680", "c043e3b26fac7d72d5db13d66a9b9049", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    鱼眼缩放             = EffectMeta("鱼眼缩放", True, "7476357155273052688", "7476357155273052688", "0837cdf83770ae0ef5d8f21023fca0f2", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_range", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%
    effects_adjust_range: 默认50%, 0% ~ 100%"""
    鲜艳闪光             = EffectMeta("鲜艳闪光", True, "7478938599086476597", "7478938599086476597", "cbab5184549f97855da226d34b9284c0", [
                              EffectParam("effects_adjust_number", 1.000, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_number: 默认100%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    鸽洞                 = EffectMeta("鸽洞", True, "7461957089364102453", "7461957089364102453", "ba28db81f0cbf79facb482dc6b1d1e3f", [
                              EffectParam("effects_adjust_noise", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_noise: 默认50%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    黑噪涂鸦             = EffectMeta("黑噪涂鸦", True, "7522413932234001665", "7522413932234001665", "0b80a1c0314ca3dd33c0abc6cf7558ef", [])
    黑白三格             = EffectMeta("黑白三格", True, "7399466631983893766", "7399466631983893766", "a0a1505a85fbb9b990daf6afdb7291a1", [])
    黑白十字绣           = EffectMeta("黑白十字绣", True, "7496416552527351101", "7496416552527351101", "b3472d7ef4e3386cb7bbc2481e3dd91d", [
                              EffectParam("effects_adjust_texture", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_vertical_shift", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_size", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认50%, 0% ~ 100%
    effects_adjust_horizontal_shift: 默认50%, 0% ~ 100%
    effects_adjust_vertical_shift: 默认50%, 0% ~ 100%
    effects_adjust_size: 默认50%, 0% ~ 100%"""
    黑白叠加             = EffectMeta("黑白叠加", True, "7481158410331852093", "7481158410331852093", "f21bac8386e6c82fff9bee88f463d1d8", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    黑白影调             = EffectMeta("黑白影调", True, "7520087996285095169", "7520087996285095169", "c771bd19c5f9bcc877af45e3ec1cb989", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    黑白滚动             = EffectMeta("黑白滚动", True, "7488152483081030973", "7488152483081030973", "cba6c022ac0fe4e5eaeca8663e1b6f77", [
                              EffectParam("effects_adjust_speed", 0.067, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认7%, 0% ~ 100%"""
    黑白疾闪             = EffectMeta("黑白疾闪", True, "7521486920178863376", "7521486920178863376", "74ad7bac630684f426effad532f32ded", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    黑白眩光             = EffectMeta("黑白眩光", True, "7514818253529632017", "7514818253529632017", "b4329d7bf9b9c1b783132cb5910a3465", [
                              EffectParam("effects_adjust_intensity", 0.714, 0.000, 1.000),
                              EffectParam("effects_adjust_color", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认71%, 0% ~ 100%
    effects_adjust_color: 默认100%, 0% ~ 100%"""
    黑白错误             = EffectMeta("黑白错误", True, "7488649586685349181", "7488649586685349181", "5798c8c77db9077c13d5257158936bd6", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000),
                              EffectParam("effects_adjust_intensity", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_intensity: 默认50%, 0% ~ 100%"""
    黑白雪花             = EffectMeta("黑白雪花", True, "7530172179627937025", "7530172179627937025", "ae6a061c924959ca0d159e7d1104d060", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    黑羽毛               = EffectMeta("黑羽毛", True, "7399471381659798790", "7399471381659798790", "95b22895abb9515a2777d382ec6b42d0", [
                              EffectParam("effects_adjust_speed", 0.330, 0.000, 1.000),
                              EffectParam("effects_adjust_background_animation", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%
    effects_adjust_background_animation: 默认100%, 0% ~ 100%"""
    黑胶边框             = EffectMeta("黑胶边框", True, "7399470906407406854", "7399470906407406854", "30c353317f11b9a5dcdf5b64708955ad", [
                              EffectParam("effects_adjust_texture", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_texture: 默认100%, 0% ~ 100%"""
    黑色故障             = EffectMeta("黑色故障", True, "7399472022398520581", "7399472022398520581", "be88751a3267768bba6eaef7036f7f32", [
                              EffectParam("effects_adjust_vertical_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_horizontal_shift", 0.000, -1.000, 1.000),
                              EffectParam("effects_adjust_speed", 0.500, 0.000, 1.000),
                              EffectParam("effects_adjust_rotate", 0.400, 0.000, 1.000),
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_vertical_shift: 默认0%, -100% ~ 100%
    effects_adjust_horizontal_shift: 默认0%, -100% ~ 100%
    effects_adjust_speed: 默认50%, 0% ~ 100%
    effects_adjust_rotate: 默认40%, 0% ~ 100%
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    黑色聚焦             = EffectMeta("黑色聚焦", True, "7529381141233585409", "7529381141233585409", "fb2a1a4fed5dc0097bf6b1a7f4630eda", [])
    黑边闪震             = EffectMeta("黑边闪震", True, "7522576191727897873", "7522576191727897873", "41b35421c4a5e0f7787d8d8d537476fd", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    鼠标选中             = EffectMeta("鼠标选中", True, "7496726039004040465", "7496726039004040465", "f2ef9612293d18cf0cb6dda528f00b11", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
    鼠标选择             = EffectMeta("鼠标选择", True, "7510057186425392400", "7510057186425392400", "5580ee0980e16188c7f805734ac21d1d", [
                              EffectParam("effects_adjust_speed", 0.333, 0.000, 1.000)])
    """参数:
    effects_adjust_speed: 默认33%, 0% ~ 100%"""
