"""音频场景特效元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class AudioSceneEffectType(EffectEnum):
    """音频"场景音"效果枚举"""

    # 免费特效
    Bibble               = EffectMeta("Bibble", False, "7376171667128586768", "7376171667128586768", "f554735f65a98cc4da17a1c53ef6a886", [])
    Big_House            = EffectMeta("Big House", False, "7350559836590838274", "7350559836590838274", "3b1d62bbe927104e393b0fc5043dc0a6", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Cranky_Kitten        = EffectMeta("Cranky Kitten", False, "7376171800184492561", "7376171800184492561", "f554735f65a98cc4da17a1c53ef6a886", [])
    Dramarama            = EffectMeta("Dramarama", False, "7338753296363950594", "7338753296363950594", "f554735f65a98cc4da17a1c53ef6a886", [])
    Elfy                 = EffectMeta("Elfy", False, "7311544785477571074", "7311544785477571074", "8dd8889045e6c065177df791ddb3dfb8", [])
    Fussy_Male           = EffectMeta("Fussy Male", False, "7337197310696231425", "7337197310696231425", "f554735f65a98cc4da17a1c53ef6a886", [])
    Good_Guy             = EffectMeta("Good Guy", False, "7259231960889823746", "7259231960889823746", "8dd8889045e6c065177df791ddb3dfb8", [])
    Lois                 = EffectMeta("Lois", False, "7360976360103219729", "7360976360103219729", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Pierce_G             = EffectMeta("Pierce G", False, "7372475060684067344", "7372475060684067344", "f554735f65a98cc4da17a1c53ef6a886", [])
    Psychic              = EffectMeta("Psychic", False, "7360975582726722064", "7360975582726722064", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Roba                 = EffectMeta("Roba", False, "7413437831810534661", "7413437831810534661", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Santa                = EffectMeta("Santa", False, "7311544442723242497", "7311544442723242497", "8dd8889045e6c065177df791ddb3dfb8", [])
    Spill_the_Tea        = EffectMeta("Spill the Tea", False, "7372474768022311441", "7372474768022311441", "f554735f65a98cc4da17a1c53ef6a886", [])
    Squirrel             = EffectMeta("Squirrel", False, "7338257533796094466", "7338257533796094466", "b2b3f551b703c87e8e057ad8f92fafbb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Witch                = EffectMeta("Witch", False, "7291557558584611330", "7291557558584611330", "8dd8889045e6c065177df791ddb3dfb8", [])
    bestie               = EffectMeta("bestie", False, "7252272084292735489", "7252272084292735489", "8dd8889045e6c065177df791ddb3dfb8", [])
    energetic            = EffectMeta("energetic", False, "7320193885114733057", "7320193885114733057", "99fee98d58dd023a9f54a772dffe1ac1", [
                              EffectParam("Intensity", 1.000, 0.000, 1.000)])
    """参数:
    Intensity: 默认100%, 0% ~ 100%"""
    亚裔美甲师           = EffectMeta("亚裔美甲师", False, "7393234397933081089", "7393234397933081089", "f554735f65a98cc4da17a1c53ef6a886", [])
    低保真               = EffectMeta("低保真", False, "7025484400313766402", "7025484400313766402", "44a00f0e2b85e0006f49ef345a305ec1", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    低声尖叫的人         = EffectMeta("低声尖叫的人", False, "7393234290022027777", "7393234290022027777", "f554735f65a98cc4da17a1c53ef6a886", [])
    变戏法的人           = EffectMeta("变戏法的人", False, "7254407946195440130", "7254407946195440130", "8dd8889045e6c065177df791ddb3dfb8", [])
    合成器               = EffectMeta("合成器", False, "7021052503919694337", "7021052503919694337", "0247a95158fda7a9e44ccd4f832a9a14", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    回音                 = EffectMeta("回音", False, "7021052523762946561", "7021052523762946561", "c37d02ae5853211ad84c13e6dca31b81", [
                              EffectParam("change_voice_param_quantity", 0.800, 0.000, 1.000),
                              EffectParam("change_voice_param_strength", 0.762, 0.000, 1.000)])
    """参数:
    change_voice_param_quantity: 默认80%, 0% ~ 100%
    change_voice_param_strength: 默认76%, 0% ~ 100%"""
    大叔                 = EffectMeta("大叔", False, "7021052537344102913", "7021052537344102913", "583e3ccf9d2daad3860aa70ad61b64ca", [
                              EffectParam("change_voice_param_pitch", 0.834, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认83%, 0% ~ 100%
    change_voice_param_timbre: 默认100%, 0% ~ 100%"""
    女王                 = EffectMeta("女王", False, "7337197136242545153", "7337197136242545153", "f554735f65a98cc4da17a1c53ef6a886", [])
    女生                 = EffectMeta("女生", False, "7021052551755731457", "7021052551755731457", "a83c56bd3fb17e93a1437d06498ab7ec", [
                              EffectParam("change_voice_param_pitch", 0.834, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.334, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认83%, 0% ~ 100%
    change_voice_param_timbre: 默认33%, 0% ~ 100%"""
    小甜甜               = EffectMeta("小甜甜", False, "7320193577613529602", "7320193577613529602", "ac2110d039d35ad01ca8452a6eadc921", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    怪物                 = EffectMeta("怪物", False, "7021052602091573761", "7021052602091573761", "ce0bc10d76e22a718094c152f7beae25", [
                              EffectParam("change_voice_param_pitch", 0.650, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.780, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认65%, 0% ~ 100%
    change_voice_param_timbre: 默认78%, 0% ~ 100%"""
    扩音器               = EffectMeta("扩音器", False, "7021052620592648705", "7021052620592648705", "b2ca5803b90f44ee0c833f34ef684d40", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    杰茜                 = EffectMeta("杰茜", False, "7254408415026352642", "7254408415026352642", "8dd8889045e6c065177df791ddb3dfb8", [])
    没电了               = EffectMeta("没电了", False, "7021052694370456065", "7021052694370456065", "a96ff559c9f1afec0603ae8bb107d98c", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    电音                 = EffectMeta("电音", False, "7021052717204247042", "7021052717204247042", "a6f883d8294fd5f49952cbf08544a0c5", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    男生                 = EffectMeta("男生", False, "7021052731091587586", "7021052731091587586", "e2e27786b25e4cf9b4e74558d6f6c832", [
                              EffectParam("change_voice_param_pitch", 0.375, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.250, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认38%, 0% ~ 100%
    change_voice_param_timbre: 默认25%, 0% ~ 100%"""
    花栗鼠               = EffectMeta("花栗鼠", False, "7021052742021943810", "7021052742021943810", "4ff3edc0229bfac112c1caefe75e7039", [
                              EffectParam("change_voice_param_pitch", 0.500, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.500, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认50%, 0% ~ 100%
    change_voice_param_timbre: 默认50%, 0% ~ 100%"""
    萝莉                 = EffectMeta("萝莉", False, "7021052754512581122", "7021052754512581122", "bbf0f0d1532a249e9a1f7f3444e1e437", [
                              EffectParam("change_voice_param_pitch", 0.750, 0.000, 1.000),
                              EffectParam("change_voice_param_timbre", 0.600, 0.000, 1.000)])
    """参数:
    change_voice_param_pitch: 默认75%, 0% ~ 100%
    change_voice_param_timbre: 默认60%, 0% ~ 100%"""
    颤音                 = EffectMeta("颤音", False, "7021052770924892674", "7021052770924892674", "337b1ba48ea61c95ac84ba238598ca0c", [
                              EffectParam("change_voice_param_frequency", 0.714, 0.000, 1.000),
                              EffectParam("change_voice_param_width", 0.905, 0.000, 1.000)])
    """参数:
    change_voice_param_frequency: 默认71%, 0% ~ 100%
    change_voice_param_width: 默认90%, 0% ~ 100%"""
    麦霸                 = EffectMeta("麦霸", False, "7021052785101640194", "7021052785101640194", "f2bab335416833134ab4bb780c128cd2", [
                              EffectParam("change_voice_param_room", 0.052, 0.000, 1.000),
                              EffectParam("change_voice_param_strength", 0.450, 0.000, 1.000)])
    """参数:
    change_voice_param_room: 默认5%, 0% ~ 100%
    change_voice_param_strength: 默认45%, 0% ~ 100%"""
    黑胶                 = EffectMeta("黑胶", False, "7025484451710767618", "7025484451710767618", "fe8fdb1bcec05647749e076a15443f08", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000),
                              EffectParam("change_voice_param_noise", 0.743, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%
    change_voice_param_noise: 默认74%, 0% ~ 100%"""

    # 付费特效
    ASMR                 = EffectMeta("ASMR", True, "7360977305759388176", "7360977305759388176", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Alien_Distortion     = EffectMeta("Alien Distortion", True, "7430730511477117441", "7430730511477117441", "c03a8ea715f47cf953dfd3f99f527d6f", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Ambitious_Guy        = EffectMeta("Ambitious Guy", True, "7338752962694484481", "7338752962694484481", "f554735f65a98cc4da17a1c53ef6a886", [])
    Auditorium           = EffectMeta("Auditorium", True, "7430730161005269520", "7430730161005269520", "e435a6afb76891dfc3b84dedd08a73e4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Autotune             = EffectMeta("Autotune", True, "7350562350396609026", "7350562350396609026", "f79be25dc2c4a8be4595653f68f4f10d", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    B_W_TV               = EffectMeta("B&W TV", True, "7423685933293113873", "7423685933293113873", "f26717b4ee99fe408dd57fe9f6ea3f1a", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Bahh                 = EffectMeta("Bahh", True, "7442210682201707009", "7442210682201707009", "d0da40cb78081c4a3ff76dae40739d6c", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Bandpass_Reverb      = EffectMeta("Bandpass Reverb", True, "7441136237194252816", "7441136237194252816", "50cf6f56da853c7f7dc88c72922cd500", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Bar_Performance      = EffectMeta("Bar Performance", True, "7495608273970679041", "7495608273970679041", "6fda29e2f2df98fa51395b14174a29a4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Bathroom             = EffectMeta("Bathroom", True, "7491143613850635521", "7491143613850635521", "fce90decda636ef3a5a0aae2eef56fa8", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Bianca               = EffectMeta("Bianca", True, "7338753649604039170", "7338753649604039170", "f554735f65a98cc4da17a1c53ef6a886", [])
    Booming              = EffectMeta("Booming", True, "7423685326264078849", "7423685326264078849", "b11c8c6f32dd81e874bc6a6aed1eb3e6", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Botilda              = EffectMeta("Botilda", True, "7478608140578114871", "7478608140578114871", "b73aef2b027465cced719c28dd9de276", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Broadway_1           = EffectMeta("Broadway 1", True, "7369113053855486481", "7369113053855486481", "723500d2eb3ddb4d7e0315d06f77cf69", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Broadway_2           = EffectMeta("Broadway 2", True, "7369112950780465665", "7369112950780465665", "9101ce8ed482028246c8c726462f0308", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Cassette_Tape        = EffectMeta("Cassette Tape", True, "7423685625162764801", "7423685625162764801", "78a29a117c38c73a3b7486e494baa553", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Cat_Translator       = EffectMeta("Cat Translator", True, "7527153148180450576", "7527153148180450576", "4dc40de81b15e45225b95898aea17c40", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Comedy_Gil           = EffectMeta("Comedy Gil", True, "7413439045545725189", "7413439045545725189", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Commuting            = EffectMeta("Commuting", True, "7519736602034277649", "7519736602034277649", "d0306190efb08b740dc26d2027a5c88c", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    strength: 默认100%, 0% ~ 100%"""
    Crystal_Clear        = EffectMeta("Crystal Clear", True, "7495597434429623568", "7495597434429623568", "d7d6fa0acc75f60fadf90843cb512cfe", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Daniel               = EffectMeta("Daniel", True, "7350566935240643073", "7350566935240643073", "5d6555c771bdfde333369126c8c0669e", [])
    David                = EffectMeta("David", True, "7413438951576571142", "7413438951576571142", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Desert               = EffectMeta("Desert", True, "7375069663727718913", "7375069663727718913", "5bd2772879c6273189d3fc7f07581e71", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    Distorted_Mic        = EffectMeta("Distorted Mic", True, "7369113160487277072", "7369113160487277072", "04613ff032c2e41b3558b1d0a25bb363", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Distrorted_Electron  = EffectMeta("Distrorted Electron", True, "7350562160440775170", "7350562160440775170", "7ad4a8e10626ed9b11661fe39cdc4bae", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Divina               = EffectMeta("Divina", True, "7478609283144322359", "7478609283144322359", "c4090a04268bb806296820433c1c3dad", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Doll                 = EffectMeta("Doll", True, "7291557779649597954", "7291557779649597954", "8dd8889045e6c065177df791ddb3dfb8", [])
    Double_Trouble       = EffectMeta("Double Trouble", True, "7425550882760036880", "7425550882760036880", "a0483de7565968e5cfe168b3e12dc17e", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Drip_Vocals          = EffectMeta("Drip Vocals", True, "7425551057993863697", "7425551057993863697", "828f481e377a79550f7bb5afe5bc42ec", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Drowned_Out          = EffectMeta("Drowned Out", True, "7369113373495005712", "7369113373495005712", "6487b1db377eb2f84d90d5abcaef04d2", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    E_T                  = EffectMeta("E·T", True, "7338256913865380354", "7338256913865380354", "c80c8c31d933b15e93299648e773de3d", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Echo_II              = EffectMeta("Echo II", True, "7423685555675730449", "7423685555675730449", "8fd30de86684a203e9495bc45accc775", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Echo_Plus            = EffectMeta("Echo Plus", True, "7399558386091561489", "7399558386091561489", "b78fd5df1a38db8fcf83412dfb6940e4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Ecko                 = EffectMeta("Ecko", True, "7478611711667244293", "7478611711667244293", "25cec694e3275a3462f9bcdb6d47a772", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Ethereal             = EffectMeta("Ethereal", True, "7350561590950760962", "7350561590950760962", "0af91133474d57e8ad8805cc991752fb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Ethereal_II          = EffectMeta("Ethereal II", True, "7423685792372888065", "7423685792372888065", "c5510b10d74b0babf4a4627395766d74", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
    Excited_Female       = EffectMeta("Excited Female", True, "7460853952335269126", "7460853952335269126", "f554735f65a98cc4da17a1c53ef6a886", [])
    Excited_Male         = EffectMeta("Excited Male", True, "7460853952335301894", "7460853952335301894", "f554735f65a98cc4da17a1c53ef6a886", [])
    Female_Sales         = EffectMeta("Female Sales", True, "7338753518653673986", "7338753518653673986", "f554735f65a98cc4da17a1c53ef6a886", [])
    Flirty_Female        = EffectMeta("Flirty Female", True, "7460745550229556485", "7460745550229556485", "f554735f65a98cc4da17a1c53ef6a886", [])
    Flute_Converter      = EffectMeta("Flute Converter", True, "7527145729714933009", "7527145729714933009", "ed2d8f5c938e140765276795c8f2a6e8", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Full_Stack           = EffectMeta("Full Stack", True, "7425551190701642257", "7425551190701642257", "b69018905a38fb2abfa2c5039490a42f", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Full_Voice           = EffectMeta("Full Voice", True, "7423685696159748609", "7423685696159748609", "24c5dbd2830b28ac85d1a6a5b73b24e0", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Fuller_Voice         = EffectMeta("Fuller Voice", True, "7495602511638842625", "7495602511638842625", "4befc0f686c64a159d74875e32455e63", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Giant                = EffectMeta("Giant", True, "7338257108795658753", "7338257108795658753", "20702d7511d03d006a718ece130ffa92", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    GingerBread          = EffectMeta("GingerBread", True, "7311544605806170625", "7311544605806170625", "8dd8889045e6c065177df791ddb3dfb8", [])
    Gloria               = EffectMeta("Gloria", True, "7337197238495482369", "7337197238495482369", "f554735f65a98cc4da17a1c53ef6a886", [])
    Gloria_2             = EffectMeta("Gloria 2", True, "7360977056684839441", "7360977056684839441", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Granny               = EffectMeta("Granny", True, "7338753737260798466", "7338753737260798466", "f554735f65a98cc4da17a1c53ef6a886", [])
    Gravelly_Alien       = EffectMeta("Gravelly Alien", True, "7430730350545867265", "7430730350545867265", "4f4b96834ece824728ca78ab4494b1d9", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Greek_Guy            = EffectMeta("Greek Guy", True, "7413437339797736710", "7413437339797736710", "c73613a258e33a7633211d4571339afe", [])
    Guitar_Delay         = EffectMeta("Guitar Delay", True, "7441136364898226704", "7441136364898226704", "09108ae99462020a2297f3a4abbd13fb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Hell                 = EffectMeta("Hell", True, "7375069259208069648", "7375069259208069648", "e456efe7bd89d565c1103fa48508ea57", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    Homer                = EffectMeta("Homer", True, "7413437709601099014", "7413437709601099014", "73fdd2aabc2a45acc3c915e7b897868a", [])
    IP动画人物           = EffectMeta("IP动画人物", True, "7393234534130520593", "7393234534130520593", "f554735f65a98cc4da17a1c53ef6a886", [])
    Ice_Cave             = EffectMeta("Ice Cave", True, "7375069129759265296", "7375069129759265296", "6b9cda93f6d75b9a3b19b2e8eb6ad40f", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    In_The_Rain          = EffectMeta("In The Rain", True, "7375070130469868049", "7375070130469868049", "0633c88a5d6344a5ac1c00aa05e43d5f", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    In_The_Wind          = EffectMeta("In The Wind", True, "7375069393438380561", "7375069393438380561", "33e99402b2b056ce4f44f820ceac5cb5", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    In_Womb              = EffectMeta("In Womb", True, "7508590567228525841", "7508590567228525841", "750ebb6e1368779f72adb570fad1893b", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    strength: 默认100%, 0% ~ 100%"""
    Indoor_Voice         = EffectMeta("Indoor Voice", True, "7495602211926461697", "7495602211926461697", "63c9d3cbc4560227959f850e7777b947", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Intercom             = EffectMeta("Intercom", True, "7350559625638318593", "7350559625638318593", "ee90781228939435d0d56b5c087526d4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Interference         = EffectMeta("Interference", True, "7423685833237991952", "7423685833237991952", "b76329633677e10e82c4fe78c4999b9c", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    John                 = EffectMeta("John", True, "7413435338808364293", "7413435338808364293", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Kiddo                = EffectMeta("Kiddo", True, "7338753225970946562", "7338753225970946562", "f554735f65a98cc4da17a1c53ef6a886", [])
    Leo                  = EffectMeta("Leo", True, "7415664293070294277", "7415664293070294277", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Live_House           = EffectMeta("Live House", True, "7409941151446209025", "7409941151446209025", "19f8b859169bd9c15306296805a619f8", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Live_Music           = EffectMeta("Live Music", True, "7491138873276386561", "7491138873276386561", "e7e2b968edda3ca9b0b254a782258c54", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Live_broadcast       = EffectMeta("Live broadcast", True, "7324621064137347585", "7324621064137347585", "1887694fc01aef43b116924e012147b4", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    Losing_Sanity        = EffectMeta("Losing Sanity", True, "7384761158189715969", "7384761158189715969", "3b3b09b530b0a64666f1c5b6d20d4018", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Market_Broadcast     = EffectMeta("Market Broadcast", True, "7430730098476585473", "7430730098476585473", "5492a8de6510cde08966d2e9ea6628ad", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
    Mermaid              = EffectMeta("Mermaid", True, "7350562007357067778", "7350562007357067778", "795f4215cf7ed6851808ccd5a606f7a1", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Mic_Malfunction      = EffectMeta("Mic Malfunction", True, "7519692247810542865", "7519692247810542865", "e7c14a3e7c3ea6d06b24e80d2148b443", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Movie_Announcer      = EffectMeta("Movie Announcer", True, "7460852751971470598", "7460852751971470598", "f554735f65a98cc4da17a1c53ef6a886", [])
    Muffler              = EffectMeta("Muffler", True, "7495596718457703696", "7495596718457703696", "dd0f809f5326040fa1e330c283984608", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Music_Enhancer       = EffectMeta("Music Enhancer", True, "7441136509580743184", "7441136509580743184", "9013e33221586d10c19727218ac0bef5", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Naive_Girl           = EffectMeta("Naive Girl", True, "7372474866471014913", "7372474866471014913", "f554735f65a98cc4da17a1c53ef6a886", [])
    No_Bass              = EffectMeta("No Bass", True, "7423685500369637889", "7423685500369637889", "fce32230dbe76e261e0c4430285a86ba", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Office               = EffectMeta("Office", True, "7508591136970263825", "7508591136970263825", "c4d41270683b5fa63ed0715e507f101a", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    strength: 默认100%, 0% ~ 100%"""
    Old_Hollywood        = EffectMeta("Old Hollywood", True, "7430729938598105601", "7430729938598105601", "d286bbff1c3a993da4cf8bc7d21ceaef", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Opposite_Duo         = EffectMeta("Opposite Duo", True, "7519689868239326480", "7519689868239326480", "6bba1ec27f141d10c7534eb7cda3333b", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Parking_Lot          = EffectMeta("Parking Lot", True, "7491140370965777680", "7491140370965777680", "a06a86fcbbc17acab5ad067976082a72", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Phone_Call           = EffectMeta("Phone Call", True, "7491147795483643137", "7491147795483643137", "30ff7eb77facbb554d8ba9d51c9cad17", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Playful              = EffectMeta("Playful", True, "7338753586630758914", "7338753586630758914", "f554735f65a98cc4da17a1c53ef6a886", [])
    Podcast              = EffectMeta("Podcast", True, "7441137618982539792", "7441137618982539792", "648e01d20c71297091b4759c7d52d018", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Police_officer       = EffectMeta("Police officer", True, "7360976647115248144", "7360976647115248144", "73fdd2aabc2a45acc3c915e7b897868a", [])
    PsyElectro           = EffectMeta("PsyElectro", True, "7375069530545984001", "7375069530545984001", "65ef01ba4626318fab4f007fec136e1e", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    Radiant_Echo         = EffectMeta("Radiant Echo", True, "7425551433124024849", "7425551433124024849", "84b063d12b7a2c786f1570a5d7e0e47a", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Radio_Announer       = EffectMeta("Radio Announer", True, "7418494159553565185", "7418494159553565185", "6c17b5822b5ea7ec690810233873a390", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Rap_Attitude         = EffectMeta("Rap Attitude", True, "7425551289326506497", "7425551289326506497", "651a83cdd17bec325f66e64407c14c5a", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Retro_Vibe           = EffectMeta("Retro Vibe", True, "7350562480453587457", "7350562480453587457", "a343ad6f0d755c8beadb219f9a2009ed", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Rick                 = EffectMeta("Rick", True, "7376171607376531969", "7376171607376531969", "f554735f65a98cc4da17a1c53ef6a886", [])
    Simon                = EffectMeta("Simon", True, "7415664293070277893", "7415664293070277893", "73fdd2aabc2a45acc3c915e7b897868a", [])
    Singer_Focus         = EffectMeta("Singer Focus", True, "7495602511638826241", "7495602511638826241", "afc8163cadc9e8f3dffef67c02afb141", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Sound_Widener        = EffectMeta("Sound Widener", True, "7519701648592227585", "7519701648592227585", "706ffdf3f2e511f97615f0eaf916b249", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Space_Robot          = EffectMeta("Space Robot", True, "7338257399356068354", "7338257399356068354", "751b0cf3f501a9f1ad4c025a28cb0f27", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Street_Anthem        = EffectMeta("Street Anthem", True, "7425551364584903185", "7425551364584903185", "5ae3488f43ac71725141b608ef6632f3", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Super_Echo           = EffectMeta("Super Echo", True, "7519711829296286993", "7519711829296286993", "d12282afb03c7a46e33885eb79622eab", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    The_Voice            = EffectMeta("The Voice", True, "7384761054930145793", "7384761054930145793", "7184386e75226a36942c60a5d5bb5618", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Tube_TV              = EffectMeta("Tube TV", True, "7430730274729628161", "7430730274729628161", "473f748b8555d8a5376e65158afeb102", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Valley               = EffectMeta("Valley", True, "7350561462173045250", "7350561462173045250", "941271aefaaf83833f98631d00336024", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Valley_Girl          = EffectMeta("Valley Girl", True, "7415664293070310661", "7415664293070310661", "c73613a258e33a7633211d4571339afe", [])
    Voice_Crisper        = EffectMeta("Voice Crisper", True, "7491147795483659521", "7491147795483659521", "afa899afa9b93e99cce244324bffe563", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Voice_Focus          = EffectMeta("Voice Focus", True, "7495597434429639952", "7495597434429639952", "87a3523ea6a92ea0469cffec77ce1472", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Werewolf             = EffectMeta("Werewolf", True, "7291557437218230786", "7291557437218230786", "8dd8889045e6c065177df791ddb3dfb8", [])
    Wispy                = EffectMeta("Wispy", True, "7423685388088119825", "7423685388088119825", "e659f90b814a319fae0616c33708809d", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    Zombie               = EffectMeta("Zombie", True, "7291557691753763330", "7291557691753763330", "8dd8889045e6c065177df791ddb3dfb8", [])
    _1950s_Announcer     = EffectMeta("1950s Announcer", True, "7430730015865573905", "7430730015865573905", "79b707b708bf0ce19ebb184815b56864", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    _3D_Surround_Sound   = EffectMeta("3D Surround Sound", True, "7350561041371107842", "7350561041371107842", "d145877a20a9f8673e35aaf410cfb908", [
                              EffectParam("strength", 0.000, 0.000, 1.000)])
    """参数:
    strength: 默认0%, 0% ~ 100%"""
    _8_bit               = EffectMeta("8-bit", True, "7491147795483610369", "7491147795483610369", "52c7d8dc600894b48dd1a23939f872de", [
                              EffectParam("Pitch", 0.500, 0.000, 1.000)])
    """参数:
    Pitch: 默认50%, 0% ~ 100%"""
    teenager             = EffectMeta("teenager", True, "7320193453835424257", "7320193453835424257", "687927d5722e9125b6b666cd47d02c23", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    一群花栗鼠           = EffectMeta("一群花栗鼠", True, "7472638680319020343", "7472638680319020343", "fb553fe189440d8a561afa3ba0f01402", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    人声增强             = EffectMeta("人声增强", True, "7290909345280168449", "7290909345280168449", "17096745c3b941fcf0fbaf81c3dfa9e2", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    低保真扩音器         = EffectMeta("低保真扩音器", True, "7460858241363348741", "7460858241363348741", "141f6c1f1064115ece93207fc163123a", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    低音增强             = EffectMeta("低音增强", True, "7290909185573655041", "7290909185573655041", "e7c09c96d10c163269fc4e35c1f4b1ee", [
                              EffectParam("change_voice_param_strength", 1.000, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认100%, 0% ~ 100%"""
    便宜麦克风           = EffectMeta("便宜麦克风", True, "7470825455810006327", "7470825455810006327", "2dc4d1c296fac7493aa6ff4634e83ff0", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    信号不好             = EffectMeta("信号不好", True, "7470820325681270071", "7470820325681270071", "25ea9bc76aa1c0461297793378070539", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
    军事广播             = EffectMeta("军事广播", True, "7472639295409392951", "7472639295409392951", "9d987952d12a71e9a7f1ebd196f28f92", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    冥想                 = EffectMeta("冥想", True, "7460858329443650821", "7460858329443650821", "32fdc35f2a4c0c2e72f16eb22b3b07a5", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    合唱                 = EffectMeta("合唱", True, "7470820860002127109", "7470820860002127109", "bf3feb9b8a9ae5a99d21709df5fb1272", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    听力受损             = EffectMeta("听力受损", True, "7470819796494322950", "7470819796494322950", "338e9a0912d2cd84cd6c71da2c27256e", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
    和声2                = EffectMeta("和声2", True, "7470822580463717637", "7470822580463717637", "c9d383e4838da90391bed0a25b5cdb77", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    和声                 = EffectMeta("和声", True, "7470820717563530502", "7470820717563530502", "d47258897a0a943d8b43aafde5f59a43", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    回忆人声             = EffectMeta("回忆人声", True, "7409940780892033552", "7409940780892033552", "294e84efcbc286113999e546ffe8a54b", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    坏掉的麦克风         = EffectMeta("坏掉的麦克风", True, "7469671392296881413", "7469671392296881413", "f70f30fadb270d6bc50c39608de22e04", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    声码器               = EffectMeta("声码器", True, "7475625038968818949", "7475625038968818949", "ce81a5c8f0f7e55d94ace6a231516846", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    复古电影             = EffectMeta("复古电影", True, "7469678047344512311", "7469678047344512311", "11c9e38a0d644a7ecb499176be4f2afd", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    外星电波             = EffectMeta("外星电波", True, "7402218432961188353", "7402218432961188353", "d014b954a65d1b5d9ab7c5c715459b32", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    失落灵魂             = EffectMeta("失落灵魂", True, "7469679204422995205", "7469679204422995205", "b902453cabf1d86c0a5ccd3ccb98e40e", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    守卫娃娃             = EffectMeta("守卫娃娃", True, "7469678901237730565", "7469678901237730565", "f477956baca3170c21a7960458fa7679", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    宽立体声             = EffectMeta("宽立体声", True, "7418494095284245008", "7418494095284245008", "49b3313b2b73f1a2541bdb946029a778", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    小喇叭               = EffectMeta("小喇叭", True, "7294188312237969921", "7294188312237969921", "4c2414e978b20fa2652c49b97e8ef775", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    小黄人               = EffectMeta("小黄人", True, "7393234347785982481", "7393234347785982481", "f554735f65a98cc4da17a1c53ef6a886", [])
    山洞cave             = EffectMeta("山洞cave", True, "7320193715165729282", "7320193715165729282", "0049c2dbdee2f3678c16e3702daf6ee3", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    房间                 = EffectMeta("房间", True, "7294185669272801794", "7294185669272801794", "ebaeafd89273784bad92665a0f9a478a", [])
    打电话中             = EffectMeta("打电话中", True, "7418494243519336961", "7418494243519336961", "91d6508e6627f6103fe19ffcfc1debeb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    拳击播报员           = EffectMeta("拳击播报员", True, "7418494022110417409", "7418494022110417409", "f8e846c82d49d5c7dc72283026d94194", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    教堂                 = EffectMeta("教堂", True, "7294185523407491585", "7294185523407491585", "bf3455d7ec1488cb21e62eca8b09c6f1", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    教室                 = EffectMeta("教室", True, "7294185380226535937", "7294185380226535937", "034a5c19d87ee7eb694a100e799f34bc", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    无限回声             = EffectMeta("无限回声", True, "7470823521296354566", "7470823521296354566", "ec980257a0cc546dd27dc4f277d427aa", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    时光扭曲             = EffectMeta("时光扭曲", True, "7404806783476175376", "7404806783476175376", "557034de13306b3730292aab6977055e", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    机上广播aircraft_broadcast = EffectMeta("机上广播aircraft broadcast", True, "7320193333148520961", "7320193333148520961", "c96920fad822429e349571650a2a33a4", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.743, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认74%, 0% ~ 100%"""
    机器人               = EffectMeta("机器人", True, "7475623013518495031", "7475623013518495031", "cacc887232f14710375d4c9976334019", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    氦气                 = EffectMeta("氦气", True, "7409940903239881217", "7409940903239881217", "bf098a08fbbd09a1b5377717b17eaefe", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    水下                 = EffectMeta("水下", True, "7470822714131975429", "7470822714131975429", "329b9d98d83df32750a4c66b70108308", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    波浪                 = EffectMeta("波浪", True, "7469681102261603639", "7469681102261603639", "35a25eaa743d34badfe9624c43754a18", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    浴室                 = EffectMeta("浴室", True, "7392071743306732033", "7392071743306732033", "543fa76977e80084f25067c94e4c08a8", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    深邃人声             = EffectMeta("深邃人声", True, "7409940842107900432", "7409940842107900432", "0a85f2bb0f23cff622cbb60444c010c6", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    演唱会               = EffectMeta("演唱会", True, "7409941025684197905", "7409941025684197905", "f1e947637780c0caddb1a68eb54105cd", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    电话                 = EffectMeta("电话", True, "7272267496520946178", "7272267496520946178", "4f50df8f3ea0cd2b2eb60d2aca54e739", [
                              EffectParam("change_voice_param_strength", 0.700, 0.000, 1.000)])
    """参数:
    change_voice_param_strength: 默认70%, 0% ~ 100%"""
    电音转换             = EffectMeta("电音转换", True, "7460858241375948037", "7460858241375948037", "440c260832910c9d52d408f628b6388e", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    留声机               = EffectMeta("留声机", True, "7294185276493009410", "7294185276493009410", "7addfc052cc0c9ba8464b540c7c909f8", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    破坏声               = EffectMeta("破坏声", True, "7419964141579801105", "7419964141579801105", "f2043e52f3e453df21ded62573eab160", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    磁性                 = EffectMeta("磁性", True, "7320193210658066946", "7320193210658066946", "b3f2117e61ddf375e5545270607e5648", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    管道                 = EffectMeta("管道", True, "7404806922026619408", "7404806922026619408", "b79ac6b31519dac47a9434b208a4a969", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    综艺真人秀主角       = EffectMeta("综艺真人秀主角", True, "7372475192393601537", "7372475192393601537", "f554735f65a98cc4da17a1c53ef6a886", [])
    老式家庭录像         = EffectMeta("老式家庭录像", True, "7404806654237086224", "7404806654237086224", "aaab7323282a64795b86481df3a5ff14", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    老式电话             = EffectMeta("老式电话", True, "7294185904342569474", "7294185904342569474", "660335913834f2dece440647e8d70023", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    蚊子                 = EffectMeta("蚊子", True, "7460856696697556229", "7460856696697556229", "132cfa28d365d795f93bb19aa2d47917", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    超级混响             = EffectMeta("超级混响", True, "7399558195653382673", "7399558195653382673", "1f12b2e77ec9b34c44ade6f430994ec4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    超重低音             = EffectMeta("超重低音", True, "7409940640198300161", "7409940640198300161", "ff679909749a20f4008f6f0f9128257b", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    跑调                 = EffectMeta("跑调", True, "7475625644274044165", "7475625644274044165", "a9275f6d2129284913b426068e79d569", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    迷幻                 = EffectMeta("迷幻", True, "7404807040519901712", "7404807040519901712", "91fd43917bbdd653c2706da791024d9b", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    遥远呼唤             = EffectMeta("遥远呼唤", True, "7475615357315730693", "7475615357315730693", "18ccb1021292076126811c3df1131940", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    重噪点电音扩音器     = EffectMeta("重噪点电音扩音器", True, "7475621160705740038", "7475621160705740038", "e6e5ff7afeaf23ad92870b52bd37bae1", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    金属管道             = EffectMeta("金属管道", True, "7475623130392808709", "7475623130392808709", "e7c29f6a6d49775398037b2e7ef7b4c1", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    震撼全景音           = EffectMeta("震撼全景音", True, "7409940969593770512", "7409940969593770512", "8213b95b258bb6e85fa80303361cfc74", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    音乐厅               = EffectMeta("音乐厅", True, "7409941093002777089", "7409941093002777089", "419883f349ba92fb4f9b5c6432dc1868", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    风扇                 = EffectMeta("风扇", True, "7469681174315797765", "7469681174315797765", "fda7204ad6d22850225c2698f3ce7a80", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    风琴                 = EffectMeta("风琴", True, "7475623977059208454", "7475623977059208454", "cd4dfdfc9b4faa21ba160a00a456dc37", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    高解析人声           = EffectMeta("高解析人声", True, "7409940513744228865", "7409940513744228865", "2a91c264145bdbb8770bacb8e9086c91", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    高音增强             = EffectMeta("高音增强", True, "7409940704362762768", "7409940704362762768", "39d9709c966a4c63d5722ef41cda54a4", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    鬼故事               = EffectMeta("鬼故事", True, "7470821423913749766", "7470821423913749766", "dfd998236e02dfb7c5da676fef37f1d3", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
    鸟叫                 = EffectMeta("鸟叫", True, "7472635776543624503", "7472635776543624503", "82bf7621b62d638f45237ddddb48bbfb", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    麦克风2              = EffectMeta("麦克风2", True, "7475625861073456439", "7475625861073456439", "0fc2f0f214a7809bb43e3fff2285070d", [
                              EffectParam("strength", 1.000, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%"""
    鼓掌                 = EffectMeta("鼓掌", True, "7469681106485251383", "7469681106485251383", "2e86197c0ba687a1daba527f64ea656e", [
                              EffectParam("strength", 1.000, 0.000, 1.000),
                              EffectParam("noise", 0.500, 0.000, 1.000)])
    """参数:
    strength: 默认100%, 0% ~ 100%
    noise: 默认50%, 0% ~ 100%"""
