"""滤镜效果元数据"""

from .effect_meta import EffectEnum
from .effect_meta import EffectMeta, EffectParam

class FilterType(EffectEnum):
    """滤镜效果类型"""

    # 免费特效
    BW_2                 = EffectMeta("BW 2", False, "6857756260339552776", "6857756260339552776", "cf310593309fbc18a306324e2c8f7ed0", [])
    BW_3                 = EffectMeta("BW 3", False, "6857709401382326792", "6857709401382326792", "c54a59f32bc352ba5ba272addaec180f", [])
    Badbunny             = EffectMeta("Badbunny", False, "7291189124009038338", "7291189124009038338", "5c211c1bee5b969175627919376cb702", [])
    Daisies_Glow         = EffectMeta("Daisies Glow", False, "7530963885273238845", "7530963885273238845", "dcc3bf12f8e4915b6ac3601fac37586c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Lover_Blue           = EffectMeta("Lover Blue", False, "7529873693665676605", "7529873693665676605", "f6825bb07c12c96d475346dfed6bafa1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Party_Tonight        = EffectMeta("Party Tonight", False, "7236681895281431041", "7236681895281431041", "37cd0ae39a917c72b90d3c1ebc6fd019", [])
    Peach_Fuzz           = EffectMeta("Peach Fuzz", False, "7530963293570190645", "7530963293570190645", "e832b6153d3ebbe8adecc3fddc119420", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Purple_Sunset        = EffectMeta("Purple Sunset", False, "7309061242323227137", "7309061242323227137", "b5f113f20405956e083e61df671333ac", [])
    Reindeer             = EffectMeta("Reindeer", False, "7309381372341129729", "7309381372341129729", "f416becd7aae5c908e17ec8277fa68ec", [])
    Short_n_Sweet        = EffectMeta("Short n' Sweet", False, "7529873927229738301", "7529873927229738301", "57fe5c4332feabf7d6bb56f844b00ad1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Soft_Grain           = EffectMeta("Soft Grain", False, "7530963947583802677", "7530963947583802677", "3159db74910b73849648cd106d550490", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Tropical_Velvet      = EffectMeta("Tropical Velvet", False, "7529874009232641341", "7529874009232641341", "a9042720e3c1fc5420c38b7c7ba1c491", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Tyler_s_Play         = EffectMeta("Tyler's Play", False, "7532132725931707701", "7532132725931707701", "4d35b2f8744261317add0aedfbd1fecf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    VHS_I                = EffectMeta("VHS I", False, "6764669083926401547", "6764669083926401547", "b5edce113227711682db00832b078c9d", [])
    VHS_II               = EffectMeta("VHS II", False, "6764669215120036360", "6764669215120036360", "16ad790502c469a8970f88ad6ee25095", [])
    VHS_III              = EffectMeta("VHS III", False, "6764669298095952396", "6764669298095952396", "125005ff8622fedec443640b406d0af8", [])
    _1980                = EffectMeta("1980", False, "6735689609675543054", "6735689609675543054", "0ca04f5056c81899b0b059a9f6e6f36b", [])
    cowboy_retro         = EffectMeta("cowboy retro", False, "7529873868928879925", "7529873868928879925", "5297dc4e0c38a9a8914764abb945d779", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    不要抬头             = EffectMeta("不要抬头", False, "7169544534353777154", "7169544534353777154", "c6d2481c2062b6d7bd8699f13aadd02f", [])
    傍晚                 = EffectMeta("傍晚", False, "7201040374675018241", "7201040374675018241", "a7d5b2d494c72f441208e889d3dd0ec0", [])
    冰城                 = EffectMeta("冰城", False, "7172131241032946178", "7172131241032946178", "c77cf41bd7a47b96b44be1bb59aa50ea", [])
    冷蓝                 = EffectMeta("冷蓝", False, "7145435225860870657", "7145435225860870657", "a20cf9437f500c936706539e1723a399", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    冷调                 = EffectMeta("冷调", False, "6803536886498333191", "6803536886498333191", "2d3dc8630bc80e6b873c001f7b7ba9de", [])
    净透                 = EffectMeta("净透", False, "7146486658211254786", "7146486658211254786", "8bb6b7ce29bc6ec5ffdaf58c8a076b69", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    十二月               = EffectMeta("十二月", False, "7174011644291322369", "7174011644291322369", "6c4777d97c44ddf740e6ea1784d79d5e", [])
    南瓜                 = EffectMeta("南瓜", False, "7156494381812290049", "7156494381812290049", "26a2bae746e68923b8023b5ce8277128", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古2                = EffectMeta("复古2", False, "7200967331189625345", "7200967331189625345", "ae1c8093b04514707995869a01ff96b9", [])
    复古3                = EffectMeta("复古3", False, "7202170603057451522", "7202170603057451522", "64f4fd6dc0e88cbd679ae6d54e8a3520", [])
    夜视仪               = EffectMeta("夜视仪", False, "7213668281759044097", "7213668281759044097", "219591424156905239345047767df381", [])
    奶绿                 = EffectMeta("奶绿", False, "7047117823188931073", "7047117823188931073", "ebabf4fb31e84dca1f9c3e8663d72463", [])
    好梦                 = EffectMeta("好梦", False, "7252621996821844481", "7252621996821844481", "34629c6fa17414e863c4aad0920af6bf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    姜饼红               = EffectMeta("姜饼红", False, "7042613770857746946", "7042613770857746946", "faf27206e4453d4e4088529b5a7f0d2c", [])
    布达佩斯             = EffectMeta("布达佩斯", False, "7226655167662264834", "7226655167662264834", "76eb7329e796894b87a812fb27ba24f9", [])
    幻境                 = EffectMeta("幻境", False, "7167219399168889346", "7167219399168889346", "2b3b28a75c5a09969ba1a84aede1a376", [])
    幽灵                 = EffectMeta("幽灵", False, "7156488852658508290", "7156488852658508290", "9672bb83ae2bc3114a5c4a7a37aed415", [])
    幽蓝                 = EffectMeta("幽蓝", False, "7167219372476338690", "7167219372476338690", "09cfd36e5da7b9027cc43a3a7721acf7", [])
    怦然心动             = EffectMeta("怦然心动", False, "7187670332273070594", "7187670332273070594", "6626c59335d30fee5754caf769a719ab", [])
    拉斯维加斯           = EffectMeta("拉斯维加斯", False, "7263042670824526337", "7263042670824526337", "abb505888500a18210aba9e477a08eb7", [])
    拐杖糖               = EffectMeta("拐杖糖", False, "7173938587522568706", "7173938587522568706", "76eb50a403804ec22399681eaedfa1b5", [])
    敦刻尔克             = EffectMeta("敦刻尔克", False, "6706773528240198156", "6706773528240198156", "cd9078b66e777bb81eb7a13e3f255f82", [])
    料理                 = EffectMeta("料理", False, "7083809725615198721", "7083809725615198721", "9abe64b86e1cc15b78c914e590513250", [])
    日常1                = EffectMeta("日常1", False, "7202170685601354242", "7202170685601354242", "8e2236b914709d60d243ae22616c1fc6", [])
    日常2                = EffectMeta("日常2", False, "7202170603061662209", "7202170603061662209", "ad7cce78c0c798f66ce6595a807404df", [])
    日食                 = EffectMeta("日食", False, "6706773371931070989", "6706773371931070989", "8535e30d00f1e4d7825bc92c35162e26", [])
    旧金山               = EffectMeta("旧金山", False, "7263042670820364802", "7263042670820364802", "02a35a0ddf352bc802a591d447e1df78", [])
    普林斯顿             = EffectMeta("普林斯顿", False, "6956140250657722881", "6956140250657722881", "8b2a6771a593f53884fd78924f383553", [])
    晴空                 = EffectMeta("晴空", False, "6706773372107248136", "6706773372107248136", "ca5a8561d8b7aac434976dbb8f8769f0", [])
    晴空_ll              = EffectMeta("晴空 ll", False, "7199880100525920769", "7199880100525920769", "3f28be17f60edd4084eb8367cab00014", [])
    暖黄                 = EffectMeta("暖黄", False, "7169544534349582850", "7169544534349582850", "266a199df6aae07371eee30cd6fd6068", [])
    暗棕                 = EffectMeta("暗棕", False, "7209932093193720321", "7209932093193720321", "915d3c05b6850c5b5661f1dc016d9285", [])
    暗调                 = EffectMeta("暗调", False, "7187785578010644994", "7187785578010644994", "48cf90438953e5acd2f0a9e58c086214", [])
    月夜                 = EffectMeta("月夜", False, "7145435307083567617", "7145435307083567617", "175620528d0c8cd63be2e4ffb65f29ba", [])
    有一天               = EffectMeta("有一天", False, "6909290170483216897", "6909290170483216897", "24363839297ba7f5d1bd2e07b996e2cb", [])
    松果棕               = EffectMeta("松果棕", False, "7042613983316021761", "7042613983316021761", "c818ac242ec13234ca5c8d504f8d1aa5", [])
    柏林                 = EffectMeta("柏林", False, "7267828535375434301", "7267828535375434301", "5299a1ebba6de69cfee64249fd81eb83", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    槲寄生               = EffectMeta("槲寄生", False, "7173955553268339201", "7173955553268339201", "ce40c54ed721eca0484b177a27a14e8c", [])
    橙蓝                 = EffectMeta("橙蓝", False, "7145435227442123265", "7145435227442123265", "cf181a3dbd0b60512efce7da2f6d0a89", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    比佛利               = EffectMeta("比佛利", False, "6956140590157271554", "6956140590157271554", "4990c599b47d1e1e07a511d1c5995bf3", [])
    江浙沪               = EffectMeta("江浙沪", False, "6742406075246449155", "6742406075246449155", "ef3375806a7bbc22d485274dc154db42", [])
    法餐                 = EffectMeta("法餐", False, "7083809725615215106", "7083809725615215106", "6a68924efffd65a9244946f75af5ab63", [])
    流光金属             = EffectMeta("流光金属", False, "7145435284937642498", "7145435284937642498", "fb9af359279f18178d7936e4e7ec4ef6", [])
    深沙滩色             = EffectMeta("深沙滩色", False, "7177662632403407361", "7177662632403407361", "6930573553d278229001c78dada00b6d", [])
    深褐                 = EffectMeta("深褐", False, "7145435257431396865", "7145435257431396865", "aa22adc098273eead87b4fce364c4d3d", [])
    温柔                 = EffectMeta("温柔", False, "7252628290706346498", "7252628290706346498", "0e60f19851233979d2ce5ccf1db272ed", [])
    灰调                 = EffectMeta("灰调", False, "7187676220962640386", "7187676220962640386", "36cea4aabdc2788fc06ff177a2021d25", [])
    烘焙                 = EffectMeta("烘焙", False, "7083809725615231490", "7083809725615231490", "ce1cc6ccc4217c3c33144500a82a22e6", [])
    焰色                 = EffectMeta("焰色", False, "7140917025781584386", "7140917025781584386", "e7e3f2f95190ebb809b89ce056e0608e", [])
    照片展位             = EffectMeta("照片展位", False, "7136167373895111170", "7136167373895111170", "b91fc3f71b29d91f00612c773f15d7f3", [])
    熔金                 = EffectMeta("熔金", False, "7145435317539967490", "7145435317539967490", "e4746bc0b2b624b7d82652f589149e56", [])
    爵士                 = EffectMeta("爵士", False, "6909339815557206530", "6909339815557206530", "cc12c235d7a594a0285be34410120665", [])
    牛皮纸               = EffectMeta("牛皮纸", False, "6706773528319889924", "6706773528319889924", "dc77aba88dc3595595e6a85dd54e220d", [])
    白茶                 = EffectMeta("白茶", False, "6909393344711889409", "6909393344711889409", "767a44ffbb53041f8a9f850eed53e178", [])
    砂金                 = EffectMeta("砂金", False, "7140917022275146242", "7140917022275146242", "9f707a139e7a1d4b18b705d35b4e8c2c", [])
    硬朗                 = EffectMeta("硬朗", False, "7083799736326558210", "7083799736326558210", "d74e79999c296b8fb1894cb72c614742", [])
    磨砂肌               = EffectMeta("磨砂肌", False, "7273775812346647041", "7273775812346647041", "d72e6228993d45b6a76fadc07a809e09", [])
    秋天                 = EffectMeta("秋天", False, "6803536804868788743", "6803536804868788743", "22a7eeb81be85b8750d321e77da66015", [])
    简餐                 = EffectMeta("简餐", False, "7083799735387116034", "7083799735387116034", "163e608dd708b91fe4635f273d58f156", [])
    紫红                 = EffectMeta("紫红", False, "7207767289184129537", "7207767289184129537", "db31278efcbea0853502ff12169edbfb", [])
    红与蓝               = EffectMeta("红与蓝", False, "6706773528319906308", "6706773528319906308", "f6d0e038c2f82b7e262f7a7698e7f642", [])
    红棕                 = EffectMeta("红棕", False, "6803536487670354439", "6803536487670354439", "6c11d05aaa7b2c184b8c78d2245d0d81", [])
    绝对红               = EffectMeta("绝对红", False, "6717164095121920519", "6717164095121920519", "9536bf5985ffd39b97f67b37b629d007", [])
    绿湖                 = EffectMeta("绿湖", False, "7216238850677412354", "7216238850677412354", "683adc726eaa5598eb02c45412f5211e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    美食1                = EffectMeta("美食1", False, "7202207923613733378", "7202207923613733378", "3463dc09e68bb0e08c38d4420a899295", [])
    美食2                = EffectMeta("美食2", False, "7202207923613749761", "7202207923613749761", "305d64e5deb1702ceae6d6ca42e681b9", [])
    自然                 = EffectMeta("自然", False, "6803536213660668424", "6803536213660668424", "08156abb09a573579ea2833cd11363ed", [])
    自由                 = EffectMeta("自由", False, "7268192649864024578", "7268192649864024578", "b9b16167ddc75ccdd2677c27d0f68e00", [])
    航程                 = EffectMeta("航程", False, "7199880100521742850", "7199880100521742850", "1fa64ebcf5c915c22fdacfc8cf10c3f8", [])
    落日                 = EffectMeta("落日", False, "7167219264644977154", "7167219264644977154", "36b8dd63509cf812806b83719d54d348", [])
    蒸汽波               = EffectMeta("蒸汽波", False, "6706773372820263427", "6706773372820263427", "c830f12edf6a0f5c7caea8e1a29815ec", [])
    蓝魔                 = EffectMeta("蓝魔", False, "7156488852662653442", "7156488852662653442", "43df7e9006066bd3fd8ebe77ffa7acc7", [])
    蜜桃                 = EffectMeta("蜜桃", False, "6909401121010225666", "6909401121010225666", "06d28c24085facc59569ab2d0ac86cec", [])
    西西里               = EffectMeta("西西里", False, "7140917056995594753", "7140917056995594753", "e6d9959240b793a0ed2d62b2e5d49393", [])
    西餐                 = EffectMeta("西餐", False, "7083809725615247874", "7083809725615247874", "beb08b8d630926f0337bbe8e792db021", [])
    谦逊                 = EffectMeta("谦逊", False, "7234412249404674562", "7234412249404674562", "7a8b962882ef68e06bff2f565766b6e6", [])
    贝松绿               = EffectMeta("贝松绿", False, "7042613888738660866", "7042613888738660866", "ffd53e4ef4a498378a06c5e5da34a99e", [])
    赛博朋克             = EffectMeta("赛博朋克", False, "6746808141544952323", "6746808141544952323", "e5013b39c80ee98713bc2a16128cc6b4", [])
    迷林                 = EffectMeta("迷林", False, "7167219346576511489", "7167219346576511489", "bd5985bf6fafeef5b91778dd513fe728", [])
    酚蓝                 = EffectMeta("酚蓝", False, "7140917035432677890", "7140917035432677890", "7b3a36c674d67c46b6ee356bbcacb179", [])
    金200                = EffectMeta("金200", False, "7239695254914339329", "7239695254914339329", "eeac1f77548b84f473d646485214b481", [])
    金属                 = EffectMeta("金属", False, "7083809725615198722", "7083809725615198722", "a4eb0d8c77d467779aaa9b0425f9248f", [])
    铃儿响叮当           = EffectMeta("铃儿响叮当", False, "7173684203744137730", "7173684203744137730", "436cbeab90391bffb532601e438fb9cc", [])
    隧道                 = EffectMeta("隧道", False, "7199578056002900482", "7199578056002900482", "ccdb686a4c3ce3e2677784e4dbf7b4a1", [])
    青橙                 = EffectMeta("青橙", False, "7145435326419309057", "7145435326419309057", "7be45ac2927146f0cc083c8cd28f1c50", [])
    青灰                 = EffectMeta("青灰", False, "7145435225856676354", "7145435225856676354", "ce242b2d01cecee4b99c82713f9f1f91", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    青黄                 = EffectMeta("青黄", False, "7145435268382724610", "7145435268382724610", "8a06c387b287277640b958a2ee4bbe7d", [])
    骄傲                 = EffectMeta("骄傲", False, "7232207955146314241", "7232207955146314241", "35949af23e67d4629310d4f6fba5eb10", [])
    高光肌               = EffectMeta("高光肌", False, "7273807383137096193", "7273807383137096193", "4b6df756d1da497ff17a737f2c3300b6", [])
    高饱和战士           = EffectMeta("高饱和战士", False, "7533251206391663925", "7533251206391663925", "c41a9ff56311a0c387311703ff23aaef", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜艳_I               = EffectMeta("鲜艳 I", False, "7216239325426487809", "7216239325426487809", "074c7b99ee1dd9f0a214fabe2c67168d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鲜艳_II              = EffectMeta("鲜艳 II", False, "7216239430833541633", "7216239430833541633", "3e5ace7f4b813c28db844469e489a02a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黄铜                 = EffectMeta("黄铜", False, "7208531724811112961", "7208531724811112961", "d327f8b3d35bb5cb523037672057e2cf", [])
    默片                 = EffectMeta("默片", False, "6706773373562655243", "6706773373562655243", "958ac213ec97c661d56e6875cc900852", [])

    # 付费特效
    Anime_B_W            = EffectMeta("Anime B&W", True, "7503100854430403901", "7503100854430403901", "ea53c1a20c0bd4b59f60befc7ae1d948", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Anora                = EffectMeta("Anora", True, "7498012937391492413", "7498012937391492413", "680df4d9029c95113da7bd8682201a60", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Blue_Hour            = EffectMeta("Blue Hour", True, "7325369035455992322", "7325369035455992322", "25506d8aae5c5405eed483416d0b7be0", [])
    Blur                 = EffectMeta("Blur", True, "7309061242323210753", "7309061242323210753", "28de524639e4238ecca1d36ef73032b5", [])
    Candlelight          = EffectMeta("Candlelight", True, "7532053717005192501", "7532053717005192501", "a58e42673a42a9823a2f3b29aa9814ab", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Center_Light         = EffectMeta("Center Light", True, "7389526627408941584", "7389526627408941584", "8178b0d39e4c0d8ff29842ed7d90b7e0", [])
    Cinematic_Dusk       = EffectMeta("Cinematic Dusk", True, "7533276240418032957", "7533276240418032957", "d80474f390559692e6f090ee57a30292", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Cool_CCD             = EffectMeta("Cool CCD", True, "7434502433008521745", "7434502433008521745", "4b508c7a838560659d4acca26a7ffea0", [])
    Cozy_Xmas            = EffectMeta("Cozy Xmas", True, "7309381372332741122", "7309381372332741122", "47ec9b773458039ac81ca6c0eaf7f2c9", [])
    Crisp_Air            = EffectMeta("Crisp Air", True, "7291663642586518018", "7291663642586518018", "2188abe95181d25b1d440f31170ccea5", [])
    Cyan_Nature          = EffectMeta("Cyan Nature", True, "7532046206596369717", "7532046206596369717", "46ad9e0faaaf3d730ebd9c6bf5f28d16", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Cyber_Shot           = EffectMeta("Cyber Shot", True, "7405899632133280272", "7405899632133280272", "8f477291126cd664912c643c004cbc58", [])
    Cyber_Shot_2         = EffectMeta("Cyber Shot 2", True, "7405942881908691473", "7405942881908691473", "c25c9c951a974502b89dbf3dc75d99a2", [])
    Cyberpunk            = EffectMeta("Cyberpunk", True, "7325369035451814401", "7325369035451814401", "5223639d347222817ff21d7161b72d0d", [])
    Dark_Gold            = EffectMeta("Dark Gold", True, "7498685235144641845", "7498685235144641845", "7aeed616043f78014001760cf2ce9bd4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Dark_Humble          = EffectMeta("Dark Humble", True, "7529950655541234997", "7529950655541234997", "8c3aa8f2bd984510ecb804ace2e0f837", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Deadpool             = EffectMeta("Deadpool", True, "7398464405337281040", "7398464405337281040", "694d9ddd16e8cd73573ebe8df7eae71b", [])
    Dreamy_Halo          = EffectMeta("Dreamy Halo", True, "7410397554510139920", "7410397554510139920", "90d6c94a6db76c9c4b70829b168c9c17", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    Dune_1               = EffectMeta("Dune 1", True, "7358071742750790160", "7358071742750790160", "44cfa5224a19da51218fd6874ef90f8b", [])
    Dune_2               = EffectMeta("Dune 2", True, "7358753189425844737", "7358753189425844737", "84fadb3d1f2cb10d948b3417562d8bce", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Enhance              = EffectMeta("Enhance", True, "7289393505166692866", "7289393505166692866", "0cef35f4090468586ca961c4baa51c83", [])
    Fall_Foliage         = EffectMeta("Fall Foliage", True, "7278664241706439170", "7278664241706439170", "9572bc56fdad4101ac9211ce5151a034", [])
    Flash_CCD            = EffectMeta("Flash CCD", True, "7434502159204356609", "7434502159204356609", "107711a55b5260cbe491cad54c8d1d12", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Focus                = EffectMeta("Focus", True, "7278664241702261249", "7278664241702261249", "d985185586de86505a1cf7841b43dd7e", [])
    GTA_I                = EffectMeta("GTA I", True, "7311986078397796866", "7311986078397796866", "f6ca12ca496d23497845027e3ca357bf", [])
    GTA_II               = EffectMeta("GTA II", True, "7311986078397780482", "7311986078397780482", "9af344c302899047ebd48b5ed14cf5a7", [])
    GTA_III              = EffectMeta("GTA III", True, "7311986078397764098", "7311986078397764098", "59971b9c271e6419e1d59b334217ee7c", [])
    Glowing_Tan          = EffectMeta("Glowing Tan", True, "7327952948128911874", "7327952948128911874", "6ea7aa4fe8878d3ed8c206e66a8d9c34", [])
    Gritty_Noir          = EffectMeta("Gritty Noir", True, "7509129519043792189", "7509129519043792189", "746f52da526b6c01b93e5a4c6f50f57a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    HD_Dark              = EffectMeta("HD Dark", True, "7309061242327405057", "7309061242327405057", "ada2f425698c9bf80a4e2a502f457572", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Kendall              = EffectMeta("Kendall", True, "7308710164268323329", "7308710164268323329", "478394c668a7de71c4bb8153f5c84d9a", [])
    Leaf_Gaze            = EffectMeta("Leaf Gaze", True, "7291928991068344833", "7291928991068344833", "99cc2a8b34fd3f87215efd222c7eea2e", [])
    Like_Jennie          = EffectMeta("Like Jennie", True, "7503961392723037493", "7503961392723037493", "d6e1db0c829a7491fa75afdee70de967", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Lo_Fi                = EffectMeta("Lo-Fi", True, "7327952948133122562", "7327952948133122562", "db39172ffff69e973886c2e8598dbc75", [])
    Lucid_Plus           = EffectMeta("Lucid Plus", True, "7531966023201819920", "7531966023201819920", "284c0055836f6789030b8c99b1061d1f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Moody_Fall           = EffectMeta("Moody Fall", True, "7291928991068328449", "7291928991068328449", "49a90ab4904cdef83bb4405c6452101d", [])
    Mulled_Wine          = EffectMeta("Mulled Wine", True, "7447441585471492625", "7447441585471492625", "e70731374ffcd93a96725ce6d7ecd24a", [])
    Nikon胶片            = EffectMeta("Nikon胶片", True, "7527244727129754941", "7527244727129754941", "8ecdc1af238ad8b01a0a2f9ac43aeaf2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Nostalgic_Negative   = EffectMeta("Nostalgic Negative", True, "7447417062000955905", "7447417062000955905", "f8e710a616e788c1387e4c73c438f519", [])
    Peach_Fuzz_2         = EffectMeta("Peach Fuzz 2", True, "7325369035447620098", "7325369035447620098", "94c58fa75cc2f875540fb115637eb423", [])
    Pink_World           = EffectMeta("Pink World", True, "7309331648162566657", "7309331648162566657", "7937da12c962caf9435953fd40b579f8", [])
    Platinum_Bell        = EffectMeta("Platinum Bell", True, "7309381372336935426", "7309381372336935426", "0d9d4f9bd738da2aadee825222e133a0", [])
    Poor_Things          = EffectMeta("Poor Things", True, "7311986078397764097", "7311986078397764097", "6b5f8dcbaa61b782825a3979f40a33be", [])
    Sea_Blue             = EffectMeta("Sea Blue", True, "7389156616957858320", "7389156616957858320", "926c22f31392078609c6a63ec1fa0f95", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Soft_Light           = EffectMeta("Soft Light", True, "7445184125465530881", "7445184125465530881", "df5987edb80af9ff108beb38d9b73ecc", [])
    Somber_Green         = EffectMeta("Somber Green", True, "7511570653871377665", "7511570653871377665", "d436e456905fbd23f3440ef68f449deb", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    Speakeasy            = EffectMeta("Speakeasy", True, "7325369035456008706", "7325369035456008706", "448d523479d6f4f365174cbc704a213f", [])
    Summer_Shine         = EffectMeta("Summer Shine", True, "7389581446031086096", "7389581446031086096", "98d42b65fb5eca9f684172fadb11a7fe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Sun_drenched         = EffectMeta("Sun-drenched", True, "7291663642582323714", "7291663642582323714", "89a91e56813e5b72118b57e35b76c8ae", [])
    Sunlight             = EffectMeta("Sunlight", True, "7308710164264129026", "7308710164264129026", "a2e5c4d721ca3ad5e387eb162d4e0671", [])
    Sunsoaked            = EffectMeta("Sunsoaked", True, "7309061242319016449", "7309061242319016449", "bc46155b0e8d1d1f254302b6fe4727ab", [])
    Tangerine_Dream      = EffectMeta("Tangerine Dream", True, "7532414303220141365", "7532414303220141365", "0b8e85100ba311439de9765ffdbbbfce", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Throwback_Vintage    = EffectMeta("Throwback Vintage", True, "7308710164272517634", "7308710164272517634", "db59e9ce9edb02c5c56f52d33ed5f30c", [])
    Twilight_Star        = EffectMeta("Twilight Star", True, "7389578047529161233", "7389578047529161233", "8f9563659b00a6a26128e300b69c83a5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Vintage_Pink         = EffectMeta("Vintage Pink", True, "7532045902668713269", "7532045902668713269", "0d6d4d29ced70bd0b2d710895f6e8439", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Vivid                = EffectMeta("Vivid", True, "7278664241702244865", "7278664241702244865", "c501effb56dfa6116b29474da3487c3b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Vivid_2              = EffectMeta("Vivid 2", True, "7358753189421650433", "7358753189421650433", "8847598657b88253551fd5d1f2208bb1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Wild_Venture         = EffectMeta("Wild Venture", True, "7337963250362896897", "7337963250362896897", "6ba05d7c28cfe3d93370bfbf2a78ff4f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    Wong_Kar_wai         = EffectMeta("Wong Kar-wai", True, "7325369035447603714", "7325369035447603714", "edb784ee78c6c61aba98cd13076fcd2b", [])
    Wreath               = EffectMeta("Wreath", True, "7309331648162566658", "7309331648162566658", "22056025f22ffd497e8f0ea3357fb745", [])
    Yellowed_Memories    = EffectMeta("Yellowed Memories", True, "7532414434803731773", "7532414434803731773", "064dbce909e3a84581f9c456a07961e4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _4K画质              = EffectMeta("4K画质", True, "7426678351957332497", "7426678351957332497", "3381cda21304c1eb4664f3bdfe945869", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    _8K画质              = EffectMeta("8K画质", True, "7480476382338813239", "7480476382338813239", "ccd56f031f17b773af5f03961641827a", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    ins古早_2            = EffectMeta("ins古早 2", True, "7405899632120697361", "7405899632120697361", "c1b73af042d70e313ac2e734d698a015", [])
    上色                 = EffectMeta("上色", True, "7505051000252730677", "7505051000252730677", "249a25cb30ee5850bc149b7f03e9d0f8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    专注                 = EffectMeta("专注", True, "7503942587426868541", "7503942587426868541", "9c07f4c1e8505a86f495c1656fc2e7ab", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    东京夜场             = EffectMeta("东京夜场", True, "7520979225025809725", "7520979225025809725", "f4a4777efc33e7aa351b23e6afcb1801", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    中性褪色             = EffectMeta("中性褪色", True, "7494295031608560949", "7494295031608560949", "7fc4148606d0e7e9a43e7d717ed26d6b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    丹宁                 = EffectMeta("丹宁", True, "7203242134739096065", "7203242134739096065", "06c610d468faa60075e5a0dc0f49ebdc", [])
    亮古铜               = EffectMeta("亮古铜", True, "7363171656434455057", "7363171656434455057", "c9c4fc5607ecd65baf5116860a32e3ce", [])
    亮白黑白             = EffectMeta("亮白黑白", True, "7494296032025562429", "7494296032025562429", "a0ba72673fc2203eddaa5ac5aaf2b386", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    低调                 = EffectMeta("低调", True, "7234418876828619266", "7234418876828619266", "5ba0c819788210ad1c4961d0f95f82a0", [])
    低调褪色             = EffectMeta("低调褪色", True, "7498681561999527221", "7498681561999527221", "3ae01350199de77f053acfd3a4e194ac", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    佛罗里达             = EffectMeta("佛罗里达", True, "7212538379076899329", "7212538379076899329", "ba6a4144fb057c5c81b60038a0ff7e8b", [])
    佛罗里达乐园         = EffectMeta("佛罗里达乐园", True, "7278957935324041729", "7278957935324041729", "686b861edda87bf023a880aae62cb1b3", [])
    假日                 = EffectMeta("假日", True, "7501218542730136833", "7501218542730136833", "deb5b9c72a991e461cd40a35e8ffd460", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    假日复古             = EffectMeta("假日复古", True, "7522010107073334589", "7522010107073334589", "62571e839b8131bd66a573b20918ab2e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    健康古铜             = EffectMeta("健康古铜", True, "7484177321889451270", "7484177321889451270", "6eeaf14d344fffb888d2f865214d7edc", [])
    光辉                 = EffectMeta("光辉", True, "7366470603416539665", "7366470603416539665", "2ab6a99ef5e93e1675b67c3c9c551f35", [])
    冷都                 = EffectMeta("冷都", True, "7206205884324647425", "7206205884324647425", "51556a13a189346da057fcc2c9b9a76d", [])
    冷静                 = EffectMeta("冷静", True, "7252652561759474178", "7252652561759474178", "ec67a0ca2b3d8dd17c31ca17dc6953cf", [])
    加州阳光             = EffectMeta("加州阳光", True, "7199603575524168194", "7199603575524168194", "fd60e3dfa5176a6f7638702f149d026b", [])
    北欧厨房             = EffectMeta("北欧厨房", True, "7527263204502752573", "7527263204502752573", "7724f77aa3ee3ed277b43e76975a8666", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    南法假日             = EffectMeta("南法假日", True, "7529889781417889077", "7529889781417889077", "debaf710d6ae30ddac68e24ed62c1438", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    南法午后             = EffectMeta("南法午后", True, "7428567845216195073", "7428567845216195073", "d18cea0dee88d1d53b9de79ea00e208d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    卡萨布兰卡           = EffectMeta("卡萨布兰卡", True, "7224040604806681089", "7224040604806681089", "223c924d0a56a8d3d987f8cb3fa93127", [])
    去灰                 = EffectMeta("去灰", True, "7369118659945435649", "7369118659945435649", "2ee8e01215fdaf1c0b7791597ddcee51", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    去雾                 = EffectMeta("去雾", True, "7473464797070103056", "7473464797070103056", "d6f7687aaf45df25fa8547d1edd9fb72", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    发光橘子             = EffectMeta("发光橘子", True, "7524340468612664629", "7524340468612664629", "d0ca0f21630807a2318a93544d7c85f3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早                 = EffectMeta("古早", True, "7405899632129085953", "7405899632129085953", "0b611eb1bd5db3057e90815171498a8a", [])
    古早光感             = EffectMeta("古早光感", True, "7512836381383724349", "7512836381383724349", "b4a24548abd2896e18fefbb49c395915", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早微曝             = EffectMeta("古早微曝", True, "7497652953382227253", "7497652953382227253", "eef58f9bf8885e64fe3fe06b9aa206ac", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古早棕调             = EffectMeta("古早棕调", True, "7505829401481825597", "7505829401481825597", "ec128baf2fde8353759b608477c32d56", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    古铜色               = EffectMeta("古铜色", True, "7187754194814636546", "7187754194814636546", "0bf790a93ca002b1caabfcafd8aac18d", [])
    可可                 = EffectMeta("可可", True, "7187793219113980417", "7187793219113980417", "21278397e1d8bc95452092bbfdc14b8a", [])
    哈苏2                = EffectMeta("哈苏2", True, "7411451160642458129", "7411451160642458129", "050d6a7617642b438166975e0a73f81a", [])
    哈苏                 = EffectMeta("哈苏", True, "7409977607392875024", "7409977607392875024", "1dabe62d10dc8a7f434e1927856942cd", [])
    圣善夜               = EffectMeta("圣善夜", True, "7173955553268339202", "7173955553268339202", "1ab6eb37bdd3a1fc57d7185b14ad4a4f", [])
    圣塔莫妮卡           = EffectMeta("圣塔莫妮卡", True, "7172150483329487362", "7172150483329487362", "051c6c430392a7e33670da57247bddfb", [])
    地下铁               = EffectMeta("地下铁", True, "7226300464646590978", "7226300464646590978", "0bd8e1cbb5a2ec5032796f737ef762c0", [
                              EffectParam("effects_adjust_intensity", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_intensity: 默认100%, 0% ~ 100%"""
    城市穿行             = EffectMeta("城市穿行", True, "7524340146263559485", "7524340146263559485", "8daed62f99a68b51d468717f8a76495d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    增色                 = EffectMeta("增色", True, "7369511187072946704", "7369511187072946704", "7dd84fae852e9f1dffa077a56fc0ee04", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    墨绿对比             = EffectMeta("墨绿对比", True, "7503100157790129469", "7503100157790129469", "7f61b8f0c6fc3a5ef5f53e7da2f4a746", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    墨蓝                 = EffectMeta("墨蓝", True, "7208483922999513602", "7208483922999513602", "3479e36849852ddf9e0e45de3e218ab2", [])
    复古1                = EffectMeta("复古1", True, "7202170603686597121", "7202170603686597121", "b30c423ba99de5ea85de2598d6a1092c", [])
    复古1968             = EffectMeta("复古1968", True, "7231842938471322113", "7231842938471322113", "f29cbad1093f7c7229eecc8da9c5d960", [])
    复古1978             = EffectMeta("复古1978", True, "7231520066238419458", "7231520066238419458", "407cca3f5fe37ee9a79860a62fcb6f1b", [])
    复古1988             = EffectMeta("复古1988", True, "7224040604831846913", "7224040604831846913", "fd634838692f8632772dd6022aeb4a83", [])
    复古1998             = EffectMeta("复古1998", True, "7231085912451453441", "7231085912451453441", "bd07a4e6767a2ec4831d4ff4ce373962", [])
    复古4                = EffectMeta("复古4", True, "7208466244872180225", "7208466244872180225", "a3bd222053af87e0b53cb75f200a659f", [])
    复古90S              = EffectMeta("复古90S", True, "7140917040746861057", "7140917040746861057", "972c80d25a1cd53e1ddc0d10b1ad40fd", [])
    复古吧台             = EffectMeta("复古吧台", True, "7520981027750235445", "7520981027750235445", "5f1bde3585adf2670ae9b166fbebcf1f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古暖潮             = EffectMeta("复古暖潮", True, "7506516096204164413", "7506516096204164413", "87432292d7c83c765c808405ad0dc2b1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古橙红             = EffectMeta("复古橙红", True, "7505069099198713149", "7505069099198713149", "30f797d915180ea2462d1756482a1e40", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古流金             = EffectMeta("复古流金", True, "7501717836117855549", "7501717836117855549", "f364d0963b25d9684da4d79ed7885da7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古纽约             = EffectMeta("复古纽约", True, "7505829919176330549", "7505829919176330549", "c5cff926118669b06a64bf486c68eab4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古肉桂             = EffectMeta("复古肉桂", True, "7494295933023194421", "7494295933023194421", "457fdccb3a839f26c92afd7340475554", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    复古胶片             = EffectMeta("复古胶片", True, "7504953412107160885", "7504953412107160885", "4be1409cb4abe51f1c533c55731083f8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    夏天的故事           = EffectMeta("夏天的故事", True, "7400647790373638657", "7400647790373638657", "b32c4699a87d898441ec2dcec5d633e0", [])
    夏威夷               = EffectMeta("夏威夷", True, "7263042670816154114", "7263042670816154114", "56916b234a78b17267ca19a56d85b515", [])
    夏日怀旧             = EffectMeta("夏日怀旧", True, "7481560369551527223", "7481560369551527223", "3886ffa5563cbd0f8e66eb5e134cb176", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    大热                 = EffectMeta("大热", True, "7236341696965906945", "7236341696965906945", "e49aec23820038b585bce5829e4cd7a7", [])
    奥本海默             = EffectMeta("奥本海默", True, "7257829716885770754", "7257829716885770754", "f7f2c1344b512476213b573a9e940770", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    好莱坞1              = EffectMeta("好莱坞1", True, "7199880690945495553", "7199880690945495553", "c1dd33bc7fed5e5213bb269d350c0ba7", [])
    好莱坞2              = EffectMeta("好莱坞2", True, "7199880100521726466", "7199880100521726466", "61e4e7e2b3c0ef9937f9c87f52fd9000", [])
    嬉皮士               = EffectMeta("嬉皮士", True, "7140917038301581825", "7140917038301581825", "e9394e54b148974b7739efe90b09dbf5", [])
    子弹列车             = EffectMeta("子弹列车", True, "7177638621829140993", "7177638621829140993", "d43e0b23e226ea6218572c4ddcab665d", [])
    寂静岭_棕            = EffectMeta("寂静岭（棕）", True, "7509159524834512189", "7509159524834512189", "41ccf60f03087ec0862f14560a2aa0ae", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    富士回忆             = EffectMeta("富士回忆", True, "7524969471308516669", "7524969471308516669", "9d8a584372c9773d1d76bdeba024ff83", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    富士胶片             = EffectMeta("富士胶片", True, "7530315149341707581", "7530315149341707581", "23acd8ebc4ae90c7db511f19fff18759", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    小麦肤感             = EffectMeta("小麦肤感", True, "7526965761693240637", "7526965761693240637", "2eba594f8053aecb80984954f1d22e43", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    少年梦               = EffectMeta("少年梦", True, "7236685502718415361", "7236685502718415361", "6a574408d5419cb210f4ddcca9ab4014", [])
    巫师                 = EffectMeta("巫师", True, "6909339094451491330", "6909339094451491330", "c2b4995d13b0498d9ff57e6c273af507", [])
    希望                 = EffectMeta("希望", True, "7268192649864024577", "7268192649864024577", "6eef1f46d1e431be774ac527ea153ced", [])
    干枯玫瑰             = EffectMeta("干枯玫瑰", True, "7207778250536260097", "7207778250536260097", "b52109f4908647df8a24b48a5016b7ce", [])
    幽影光华             = EffectMeta("幽影光华", True, "7395868471394832897", "7395868471394832897", "685364ca759bbd78c9313b28b2ae0683", [])
    康尼岛               = EffectMeta("康尼岛", True, "7212475600143913473", "7212475600143913473", "1a6d20239c95804aecff84ecec892fb3", [])
    彩虹                 = EffectMeta("彩虹", True, "7241883343246070274", "7241883343246070274", "4170cb6eb308eb5ccf7f18df51f583a4", [])
    徒步                 = EffectMeta("徒步", True, "7216239188931252737", "7216239188931252737", "2b07d59e2615348dc665d98b2a3d59bd", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    微光                 = EffectMeta("微光", True, "7366470603420733953", "7366470603420733953", "a111af6893b0a4c125ff29c1a476a8c9", [])
    微暗                 = EffectMeta("微暗", True, "7503100513483885885", "7503100513483885885", "6a8ebb6aaab78cc2d887d850fd44678b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    微暗清晰             = EffectMeta("微暗清晰", True, "7524321059546352949", "7524321059546352949", "dcbe8c54479e6ec8e1ab5f546667548f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    怀旧                 = EffectMeta("怀旧", True, "7202170603057467906", "7202170603057467906", "4d33ea68b3de418468b1ba3730c1720a", [])
    怪诞                 = EffectMeta("怪诞", True, "7294210778826019329", "7294210778826019329", "8ec6b294ff7def3078d623e5951f3a8c", [])
    悠长夏日             = EffectMeta("悠长夏日", True, "7532142299443137845", "7532142299443137845", "45cd16b27341da2ec649fc0ee6be557b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    户外饱和_加州嬉皮士  = EffectMeta("户外饱和（加州嬉皮士）", True, "7521748564381306165", "7521748564381306165", "ad873ac26a7c1dbe0f0f5411d9d97382", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    报纸                 = EffectMeta("报纸", True, "7200967331189641729", "7200967331189641729", "2793ebd9b65f11587ed717b3ab14cf7d", [])
    拽酷                 = EffectMeta("拽酷", True, "7208437359245791746", "7208437359245791746", "453f6f1e88ad2e7af08079fbd8873d98", [])
    提亮                 = EffectMeta("提亮", True, "7369142076316848641", "7369142076316848641", "e5a11878ce98229572e69b5a3256623c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    摩登                 = EffectMeta("摩登", True, "7140917039161414145", "7140917039161414145", "99f3672047e471140e8dec7ac35346c3", [])
    撒丁岛               = EffectMeta("撒丁岛", True, "7267828534914060860", "7267828534914060860", "6becc745678dc543cd0f8e936cb8370b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    断背山               = EffectMeta("断背山", True, "7177662632411795969", "7177662632411795969", "0989e2f6db1bfb01c4272059c9fff564", [])
    日光吻               = EffectMeta("日光吻", True, "7201049338343068161", "7201049338343068161", "018d32d6fb582ab649708124777d9a16", [])
    日光浴               = EffectMeta("日光浴", True, "7213295794466591234", "7213295794466591234", "38d5c2ea39e088dfa2531a5209c78ff7", [])
    日照                 = EffectMeta("日照", True, "7252650354154672642", "7252650354154672642", "c108bf59fa0b23a70dab2666e29bc5f7", [])
    旧时来信             = EffectMeta("旧时来信", True, "7503602649992908085", "7503602649992908085", "889c4a1648a1cf011d0286a1d445aced", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明媚初夏             = EffectMeta("明媚初夏", True, "7379881822349431297", "7379881822349431297", "4502ef88123132e8edc28cc681ac1eaa", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    明快街拍             = EffectMeta("明快街拍", True, "7524338818363821373", "7524338818363821373", "dc5b14c69c97779b4bbe910081d7fbf4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    春日暖黄             = EffectMeta("春日暖黄", True, "7529890014377954613", "7529890014377954613", "2be71c98eea3765981fdbfb95c1dc11d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    普罗维亚100          = EffectMeta("普罗维亚100", True, "7239663172972450305", "7239663172972450305", "18b388b329620808c6c676c723e3edaa", [])
    晴天野餐             = EffectMeta("晴天野餐", True, "7529950488339533109", "7529950488339533109", "aaebdb4cb94963db3a9810f68c98c622", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴好假日             = EffectMeta("晴好假日", True, "7374404639036281345", "7374404639036281345", "e45b735dc7837a0fbd00374cbc8c0c26", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    晴朗                 = EffectMeta("晴朗", True, "7202170467904393730", "7202170467904393730", "eaf968fc16c24c85f8ba22d55a54cd2b", [])
    智性灰               = EffectMeta("智性灰", True, "7501978890135506193", "7501978890135506193", "dd844579f9a4b7cee8ed9c6608b3d3ba", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    暖橙街影             = EffectMeta("暖橙街影", True, "7532050452993674549", "7532050452993674549", "dcc95ec9d76cb489f1fcf3938e46a640", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暖调时光_顶楼咖啡时间 = EffectMeta("暖调时光（顶楼咖啡时间）", True, "7520981480303119677", "7520981480303119677", "dc9f457e995456ab5aed840382dcf85d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暖调褪色             = EffectMeta("暖调褪色", True, "7405899632124891665", "7405899632124891665", "d311001314793f2ce18bcf6b26782d69", [])
    暖阳                 = EffectMeta("暖阳", True, "6803536715836297742", "6803536715836297742", "a894daba99c1f9f59a09b9a8d0fd5899", [])
    暗光提亮             = EffectMeta("暗光提亮", True, "7429313870931431937", "7429313870931431937", "f85598ada312c86238f4402d075feb66", [])
    暗夜                 = EffectMeta("暗夜", True, "7212511268819702274", "7212511268819702274", "e75ec225fa9f0df1eaa8949eeef80072", [])
    暗夜发光             = EffectMeta("暗夜发光", True, "7507672667026115893", "7507672667026115893", "1f8409416a8e3366469017feb8e03f9f", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗夜暖金             = EffectMeta("暗夜暖金", True, "7501372352509529405", "7501372352509529405", "159caeb3bfcc9e8df9b868dfeb995e50", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗灰低调             = EffectMeta("暗灰低调", True, "7512467005417590077", "7512467005417590077", "0abe725e1a7bff49352623cc85780b07", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗紫                 = EffectMeta("暗紫", True, "7208509810424156674", "7208509810424156674", "c358a5d6d41f71fa8e9343bc4dffbd65", [])
    暗调ll               = EffectMeta("暗调ll", True, "7213685871516586498", "7213685871516586498", "82b869fe4013f0886bd7a4261686534b", [])
    暗调发光             = EffectMeta("暗调发光", True, "7519739336028327185", "7519739336028327185", "7cc68edc2b6f358f4efee2e2b26a13ed", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调复古             = EffectMeta("暗调复古", True, "7532142501164043573", "7532142501164043573", "23faf5062121ac39b8f788ca0d391139", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗调电影             = EffectMeta("暗调电影", True, "7441899331591868945", "7441899331591868945", "9f0388872801037b8791684a4913d068", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暗银                 = EffectMeta("暗银", True, "7188085278026764802", "7188085278026764802", "344a41d587f848e92975679680b0a054", [])
    暗黑王               = EffectMeta("暗黑王", True, "7498684358874778941", "7498684358874778941", "99f1f07d994bf4c63589735979c03e4d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    暧昧                 = EffectMeta("暧昧", True, "7212538379081093633", "7212538379081093633", "270a6ff48faf7ace41922a8427f916f2", [])
    暮光                 = EffectMeta("暮光", True, "7223738264736240129", "7223738264736240129", "1de2e713e6fe55dfa6d5647f13b7760c", [])
    月升王国             = EffectMeta("月升王国", True, "7226278850701824514", "7226278850701824514", "c2f1cc811135d63095de8fdbd7c69966", [])
    未来感胶片           = EffectMeta("未来感胶片", True, "7516797638327553297", "7516797638327553297", "7508b91094767af4e15a18ea2bc14c25", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    杜乐丽               = EffectMeta("杜乐丽", True, "7267828534905672229", "7267828534905672229", "17530e40e530018a002d3e4b3a3fdf08", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    柯达500T             = EffectMeta("柯达500T", True, "7507169416816250165", "7507169416816250165", "073aa3083b09c2b0805774c9c7d52c63", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    柯达ektar100         = EffectMeta("柯达ektar100", True, "7524969965997296957", "7524969965997296957", "b732b6176db568a2c1f73fefeb442a10", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    柯达gold200          = EffectMeta("柯达gold200", True, "7532046670159252789", "7532046670159252789", "b23f19fe76ead631c9be7e2661e5cfef", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    棒棒糖               = EffectMeta("棒棒糖", True, "7208455387354239490", "7208455387354239490", "683ec38fdf2876bdc8ffa7bf63315d10", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    棕榈世界             = EffectMeta("棕榈世界", True, "7202170685601354241", "7202170685601354241", "7e3bb31e3c8c665706cb5606cabfd23a", [])
    棕石                 = EffectMeta("棕石", True, "7201023584804803074", "7201023584804803074", "a8e95ce289962ea349afa7dad756b82a", [])
    森山                 = EffectMeta("森山", True, "7224040604810875394", "7224040604810875394", "90b190bca40216df8d1a6926a70238e1", [])
    模糊_II              = EffectMeta("模糊 II", True, "7366915042547077649", "7366915042547077649", "9a3289615a50ebd47b19ebf483f3bef5", [])
    橘子干               = EffectMeta("橘子干", True, "7202170603061645825", "7202170603061645825", "b56756a5a8aa42bba870b5b14b72c7da", [])
    橘子海               = EffectMeta("橘子海", True, "7519721968254438657", "7519721968254438657", "0b4b43fb40421615fa7ef2c67da51c93", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    气质                 = EffectMeta("气质", True, "7234421022244475393", "7234421022244475393", "9a18ab8bb375a0e1ed51461b912017ef", [])
    水光肌               = EffectMeta("水光肌", True, "7273803990909850114", "7273803990909850114", "39dc595b5c17098cf4816a2cff399fd5", [])
    水光蜜桃             = EffectMeta("水光蜜桃", True, "7304576577881264642", "7304576577881264642", "92194a317f8133e773c85c560b422019", [])
    沿途                 = EffectMeta("沿途", True, "7208820250500928001", "7208820250500928001", "afe164f922dd0147f43d0cbb90e94d30", [])
    法棍                 = EffectMeta("法棍", True, "7169558621611627010", "7169558621611627010", "c6a5d1c15347cbfae9bb742cf2613df7", [])
    派遣                 = EffectMeta("派遣", True, "7226719507530650113", "7226719507530650113", "19b1eb32b5adb90b2a31b6fec1e927c3", [])
    流行90s              = EffectMeta("流行90s", True, "7236723623635980801", "7236723623635980801", "a37a079678976f7c3623310f86a129eb", [])
    浓橘胶粒             = EffectMeta("浓橘胶粒", True, "7526964010546203957", "7526964010546203957", "f8af7d3eaa5add5e1f5e23faf8a27c49", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    浓烈                 = EffectMeta("浓烈", True, "7202170685605548545", "7202170685605548545", "b42d8f55db77ee2e45b6c9bac71f9d48", [])
    浓郁彩色             = EffectMeta("浓郁彩色", True, "7498671794308549941", "7498671794308549941", "d297d91bf6294cedb9f71a7d67cbfc75", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海洋之眼             = EffectMeta("海洋之眼", True, "7277400058260099621", "7277400058260099621", "df349a177a03ce389fcd0d1b2a2ae616", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    海边度假             = EffectMeta("海边度假", True, "7522010692430400821", "7522010692430400821", "689e1184925cdac5da1943c594232754", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    润粉皮               = EffectMeta("润粉皮", True, "7308710164259934722", "7308710164259934722", "b4cfb0c506b243b958a510fe3f53bb9b", [])
    淡彩                 = EffectMeta("淡彩", True, "7503100062524837181", "7503100062524837181", "368383396519f28481d8c6d4516aca77", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    深蜜糖色             = EffectMeta("深蜜糖色", True, "7213307585741459970", "7213307585741459970", "e1b5433ed6f1a3b25be4dbe2e20f2e37", [])
    清凉夏意             = EffectMeta("清凉夏意", True, "7372483191497560593", "7372483191497560593", "9f72ce968f0d44c800f28ba66c32359c", [])
    清晖绿野             = EffectMeta("清晖绿野", True, "7532034958538345781", "7532034958538345781", "b3d31dc52ce9e2d20528e17d67b041b5", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清晰                 = EffectMeta("清晰", True, "7220376712406635009", "7220376712406635009", "fd570f8f78c2b9a38492ded9f4366e19", [])
    清晰冷调             = EffectMeta("清晰冷调", True, "7494497335750233345", "7494497335750233345", "6b9e4b6fde8a8b4a86223de09ea4138d", [])
    清晰去灰             = EffectMeta("清晰去灰", True, "7522793725911649589", "7522793725911649589", "f028d2b9dee7e3c0d9cf31da7e99b701", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    清透净白             = EffectMeta("清透净白", True, "7521748683499539773", "7521748683499539773", "fdeb2da5b8fe4bfa2f55abd8c838661d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    温情肯尼亚           = EffectMeta("温情肯尼亚", True, "7527263060256443701", "7527263060256443701", "b980f05fd9d43a57c8dac32d2f0e1e02", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    灰野暖红             = EffectMeta("灰野暖红", True, "7529562473020607805", "7529562473020607805", "e217f2b5eed4de5286ede70a9d6113ba", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    灿金彩带             = EffectMeta("灿金彩带", True, "7468243149073158672", "7468243149073158672", "6616e3a1d378a44ed14ea50d8d25ca67", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    炎夏假日             = EffectMeta("炎夏假日", True, "7512862077078359357", "7512862077078359357", "49b6ccb60ab2fe6b870ec9050c960e3b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    炙热                 = EffectMeta("炙热", True, "7223722259985207810", "7223722259985207810", "087f06b5e926078bc850d70b23c75112", [])
    炭烧                 = EffectMeta("炭烧", True, "7202207923613749762", "7202207923613749762", "9610534e2df5b5470b4ec7e7e298b944", [])
    烈日灼痕             = EffectMeta("烈日灼痕", True, "7532146445542001981", "7532146445542001981", "7731e87994cbf3a2fd781d84c31bc8b7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    焕肤                 = EffectMeta("焕肤", True, "7178786757331128834", "7178786757331128834", "073940956259c1077acaec764f52f31c", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    爱之城2              = EffectMeta("爱之城2", True, "7400732394245853713", "7400732394245853713", "ef8b9a00f56bff3070abfaae8e86d91e", [])
    爱之城               = EffectMeta("爱之城", True, "7140917053799535105", "7140917053799535105", "b1d74e1a3e2dc6a6e8e7467a8e72709a", [])
    爱克发400            = EffectMeta("爱克发400", True, "7239647853029626369", "7239647853029626369", "c6d99ab303429db5cbc8f895f871b4a5", [])
    爱在日落黄昏时       = EffectMeta("爱在日落黄昏时", True, "7187289768592413185", "7187289768592413185", "cdf297cc8ba869e4869f471e91df493b", [])
    独行侠               = EffectMeta("独行侠", True, "7197691167985635842", "7197691167985635842", "7650665e1e8ee0fde1d817ff0229161d", [])
    琥珀                 = EffectMeta("琥珀", True, "7277400059962987063", "7277400059962987063", "ed9cac9747906633d9745e8bc927ebea", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    璀璨                 = EffectMeta("璀璨", True, "7434522269264646657", "7434522269264646657", "da0d70b6d9194b356f971b8fcdaad992", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    生化危机_红          = EffectMeta("生化危机（红）", True, "7509439242896969013", "7509439242896969013", "9b195bfe704aec0f985ad85644cdf3ee", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    田园野餐             = EffectMeta("田园野餐", True, "7372483191497576977", "7372483191497576977", "c4cf8383a4e421206877a8bb26fe9179", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    电影光效             = EffectMeta("电影光效", True, "7476442091040591110", "7476442091040591110", "7959aafed226def8b475dc1d92ee8245", [
                              EffectParam("effects_adjust_filter", 0.800, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认80%, 0% ~ 100%"""
    电视广告片           = EffectMeta("电视广告片", True, "7216230381756879362", "7216230381756879362", "afaf861bebf931edb85d6cbcc2fa529b", [])
    画质修复             = EffectMeta("画质修复", True, "7484157038403112197", "7484157038403112197", "c97fe4d535712dde45743764259482a4", [
                              EffectParam("effects_adjust_filter", 0.500, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认50%, 0% ~ 100%"""
    病娇                 = EffectMeta("病娇", True, "7294210778834407937", "7294210778834407937", "3ece2f745123896f9b23e4492ee07493", [])
    白莲花浓Rich_white_lotus = EffectMeta("白莲花浓Rich white lotus", True, "7498013408046943541", "7498013408046943541", "f2bd6c68da906eb4732e9b26385301d1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    白莲花淡Pale_white_lotus = EffectMeta("白莲花淡Pale white lotus", True, "7495798434524433717", "7495798434524433717", "24d4e6f37d1bbdd1b525c0a572dd07de", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    盐系                 = EffectMeta("盐系", True, "7083809725615231489", "7083809725615231489", "d28d3e8e86a30b6d5486d69918acfc6b", [])
    盗梦空间             = EffectMeta("盗梦空间", True, "6843297277516190221", "6843297277516190221", "ca05a3261993f8926dffc96fa287122b", [])
    磨砂小麦             = EffectMeta("磨砂小麦", True, "7304638155687203329", "7304638155687203329", "74b3d29c48d840cf60c0e1c07b30a843", [])
    磨砂小麦II           = EffectMeta("磨砂小麦II", True, "7358071742746595857", "7358071742746595857", "07b71e38332d425cd7fab1680cb211d1", [])
    秋枫                 = EffectMeta("秋枫", True, "7426658427583074832", "7426658427583074832", "1791b34d40dc29c7fe8a2e89c56813e8", [])
    空谷                 = EffectMeta("空谷", True, "7145435320031384066", "7145435320031384066", "392bef5edc13ee25d195decc1f33db77", [])
    粉蔼霓虹             = EffectMeta("粉蔼霓虹", True, "7506523550765960509", "7506523550765960509", "489c852e14d3a1deab329a7463e4ddf9", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    紫罗兰之梦           = EffectMeta("紫罗兰之梦", True, "7524339318630960445", "7524339318630960445", "f780f0c1c78d40dd262cba878a42ad9e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    红色沙漠             = EffectMeta("红色沙漠", True, "7530324886615625013", "7530324886615625013", "a824bff6023e675537e9d87b96b27843", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    红魔                 = EffectMeta("红魔", True, "7156488852658475522", "7156488852658475522", "28cfa087c7a7132accb1b592329be1be", [])
    经典电影             = EffectMeta("经典电影", True, "7509426641886514493", "7509426641886514493", "f1432e280aee654fe805b566b2809d99", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    绿光监控             = EffectMeta("绿光监控", True, "7425938478682083857", "7425938478682083857", "14b59ea9f7ede192ce5dd9d64376a136", [
                              EffectParam("effects_adjust_filter", 0.600, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认60%, 0% ~ 100%"""
    绿幽精灵             = EffectMeta("绿幽精灵", True, "7497652887393291581", "7497652887393291581", "1651e5600917bc1c4ab4a011d05580fe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    绿洲                 = EffectMeta("绿洲", True, "6909290311265030657", "6909290311265030657", "84caf0603dfc2a620d4a8111d42118ac", [])
    罗马假日             = EffectMeta("罗马假日", True, "7394781900813898257", "7394781900813898257", "092d88e9174ada8f00ca2038d941e700", [])
    美式灰粉             = EffectMeta("美式灰粉", True, "7507257098254830909", "7507257098254830909", "bf8ce6ee8cdd8f6f22cc3fe80e088c4e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    老友记               = EffectMeta("老友记", True, "6956140811171926529", "6956140811171926529", "9de5f4c770b58ac9efb1911d600681f0", [])
    肉桂                 = EffectMeta("肉桂", True, "7212516023184921089", "7212516023184921089", "e03ff4ed5615359fa383c684d8944470", [])
    背景虚化             = EffectMeta("背景虚化", True, "7442221880838197777", "7442221880838197777", "dec7c5f75f568e41cf63d4a810f430a9", [])
    腰果                 = EffectMeta("腰果", True, "7202170603053273602", "7202170603053273602", "099a2fce18a31bf4d6b844a6909092ad", [])
    自然褪色1            = EffectMeta("自然褪色1", True, "7503603399640878397", "7503603399640878397", "c39eb8cc03a4ff158954c3e8576b75b2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    自然褪色2            = EffectMeta("自然褪色2", True, "7504329357448531253", "7504329357448531253", "341eb22c6109f064d1bd94ff8700a4f2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    艳丽暖肤             = EffectMeta("艳丽暖肤", True, "7501712260402842941", "7501712260402842941", "4024bdae4c190a325c331034e667c333", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    芭比                 = EffectMeta("芭比", True, "7254095097095000578", "7254095097095000578", "a6349b45380d61aa64461041f21936b0", [])
    花园                 = EffectMeta("花园", True, "7199603574714667521", "7199603574714667521", "bc9c591706d754e61545ecf9e3b7a401", [])
    花海暖阳             = EffectMeta("花海暖阳", True, "7512496022359117117", "7512496022359117117", "428148ad9f3175e3c4c7a30f8b4847cf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    苍橘                 = EffectMeta("苍橘", True, "7140917052650295810", "7140917052650295810", "872e0e53cf276475aab1a64acc7757c2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    茶红                 = EffectMeta("茶红", True, "7047117625830150657", "7047117625830150657", "945d87dc41c21c5e5a956a2b83ad6426", [])
    荆红                 = EffectMeta("荆红", True, "7167219283863278082", "7167219283863278082", "ae792eb3fbe7ebbebf752bfc60f91414", [])
    落叶棕               = EffectMeta("落叶棕", True, "6706773372740571660", "6706773372740571660", "f8a40964007cb05b4d623b4535beeeba", [])
    落日派对             = EffectMeta("落日派对", True, "7374404639027892752", "7374404639027892752", "349905cf639e3a9cc1751a925a494b82", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝灰                 = EffectMeta("蓝灰", True, "7145435331087569409", "7145435331087569409", "c32955608ddc91b23b80afd4bcdcb99c", [])
    蓝珀光影             = EffectMeta("蓝珀光影", True, "7506516276190268725", "7506516276190268725", "1c6ac3c82e0649c5cc5560d3af9e1f7b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝紫锈影             = EffectMeta("蓝紫锈影", True, "7514216267822206269", "7514216267822206269", "6e81dd5b3972c64994c62d92ee6d4871", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝绿胶片             = EffectMeta("蓝绿胶片", True, "7517916533016841525", "7517916533016841525", "2e880d3f7db7816e77d5c59f7304e3cf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    蓝雾                 = EffectMeta("蓝雾", True, "7506515475052924213", "7506515475052924213", "fabe66c745d40dcfbf82d304b9f2cbe8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    褪色黄调             = EffectMeta("褪色黄调", True, "7516927733763542325", "7516927733763542325", "c1e9c1f2521dbceb7f86c84773fc1fd1", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    褪色黑白             = EffectMeta("褪色黑白", True, "7494295577140694333", "7494295577140694333", "67d5ba99a2ea9214b8fbd3a60dd64af7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    西冷                 = EffectMeta("西冷", True, "7145435258102485505", "7145435258102485505", "582a118ed87f8ddfbf2bab6ce6ccbba2", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    西雅图               = EffectMeta("西雅图", True, "7263042670816137730", "7263042670816137730", "c66b029e097f7c05656184d8e6c0b08b", [])
    调亮微光             = EffectMeta("调亮微光", True, "7512856913961356605", "7512856913961356605", "16178c10bc82e33eb69f8e7c53724762", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    贝果                 = EffectMeta("贝果", True, "7145435271880774146", "7145435271880774146", "21f8c68e7dd3fe22071ed06d21cc328a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    负片                 = EffectMeta("负片", True, "7220347310721470977", "7220347310721470977", "c24783c3a2f5304b6d0b4c6067de0460", [])
    质感                 = EffectMeta("质感", True, "7199651880903905794", "7199651880903905794", "2bdc2c535ac37c4d474faefd51878e56", [])
    质感压暗             = EffectMeta("质感压暗", True, "7501715761593978173", "7501715761593978173", "ccf56b33a0470965535eae8594cd8b01", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    质感对比             = EffectMeta("质感对比", True, "7503953192330284341", "7503953192330284341", "f8dc96d83be5868c4bfca63627e3d1e8", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    赛博2077             = EffectMeta("赛博2077", True, "7145435245712511489", "7145435245712511489", "a14db3e51944ebff8e96b8e41e96d2c2", [])
    赛博蓝               = EffectMeta("赛博蓝", True, "7506744864302845237", "7506744864302845237", "6f14ee3d0dd993a004210df248a12452", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    轻冷灰调             = EffectMeta("轻冷灰调", True, "7532414854607523125", "7532414854607523125", "64bed38c23e722bd32a2b49e5fd64fbf", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    轻微复古             = EffectMeta("轻微复古", True, "7512474535866764605", "7512474535866764605", "524434dcd8b5fb8aa4d3fd002abbaefc", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    轻暖鹅黄             = EffectMeta("轻暖鹅黄", True, "7524337307109969213", "7524337307109969213", "aed604b7b9ba930498fec5ebb4c02a17", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    迈阿密               = EffectMeta("迈阿密", True, "6956140706721174017", "6956140706721174017", "e1ea1c63079c06ef196a643208fefabb", [])
    迷雾                 = EffectMeta("迷雾", True, "7156494381824872962", "7156494381824872962", "5143fc0b35bca33c7b010458ffe8f1d7", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    逆光拯救             = EffectMeta("逆光拯救", True, "7503485016869997840", "7503485016869997840", "35b02b951accd187d30a834d759b8230", [
                              EffectParam("effects_adjust_filter", 0.700, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认70%, 0% ~ 100%"""
    邂逅                 = EffectMeta("邂逅", True, "7268192649864040961", "7268192649864040961", "a5411f5c5e6ce9e59ff55fc569839db9", [])
    里昂                 = EffectMeta("里昂", True, "7140917038913950209", "7140917038913950209", "b02bbbe41c73080147c38a13ef7749b2", [])
    野餐                 = EffectMeta("野餐", True, "6909398740516213249", "6909398740516213249", "da94b48772ac6eb616c5730efd2dba63", [])
    金粉飘落             = EffectMeta("金粉飘落", True, "7457450272957141521", "7457450272957141521", "0367f5e04e48d7526c33f0b210ebb41d", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    鎏金旧笺             = EffectMeta("鎏金旧笺", True, "7506516052734463293", "7506516052734463293", "262894da8167ab702606126fcb852ed4", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    钢铁与汗水           = EffectMeta("钢铁与汗水", True, "7520980429495684405", "7520980429495684405", "5c3731a0f5bada546758b43bf22b687b", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    银蓝                 = EffectMeta("银蓝", True, "7145435472209121793", "7145435472209121793", "be706eacb2da6eb3821d530aa5cd5304", [])
    银质                 = EffectMeta("银质", True, "7234421204881248770", "7234421204881248770", "e110a8d546bb7859720a689df92cd697", [])
    镜粉                 = EffectMeta("镜粉", True, "7145435293523382786", "7145435293523382786", "dec543a4d9b39cb30b41d10358d411c5", [])
    闪耀派对             = EffectMeta("闪耀派对", True, "7471157993615135248", "7471157993615135248", "90405c0fccb69ecbeb0715ee26f52d0a", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    闻香识人             = EffectMeta("闻香识人", True, "6706773528282141196", "6706773528282141196", "2dfab2bf85360b23f586328a6bfa8b5b", [])
    阳光色               = EffectMeta("阳光色", True, "7187239358582231554", "7187239358582231554", "d73164eb949d8d95153a79283916df53", [])
    阴天                 = EffectMeta("阴天", True, "7202170467904393729", "7202170467904393729", "ae048b9f0650d3d10d815e9ea594a29c", [])
    阴天拯救             = EffectMeta("阴天拯救", True, "7379881822349431313", "7379881822349431313", "34bc68e2d6a2de79d13f441828f5ee8e", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    随性                 = EffectMeta("随性", True, "7268192649864040962", "7268192649864040962", "56000a0f9c36da8e1beeabf338350015", [])
    雪莉_现实的愿景      = EffectMeta("雪莉：现实的愿景", True, "7278957935332430338", "7278957935332430338", "cbd17f9ef5634ecd9a25cb2d2b5f4fde", [])
    雷诺阿               = EffectMeta("雷诺阿", True, "7278957935328236034", "7278957935328236034", "71cbd610e38a6fb7d0fbb5f12e4baf49", [])
    霓虹_I               = EffectMeta("霓虹 I", True, "7241871358555066882", "7241871358555066882", "f56992896e4d943094dc5c8b8cfd69b7", [])
    霓虹_II              = EffectMeta("霓虹 II", True, "7241871358546678274", "7241871358546678274", "56c2233808d4dbf91537eb72e0a8d9d2", [])
    青红                 = EffectMeta("青红", True, "7257826609908945409", "7257826609908945409", "00ef783dc1047fec7be487bdbfe035e3", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    风景提亮_北欧列车    = EffectMeta("风景提亮（北欧列车）", True, "7520980581165894973", "7520980581165894973", "3ab75c3d0c7187b676e59cc8187f8528", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    飘雪圣诞             = EffectMeta("飘雪圣诞", True, "7446726004447384081", "7446726004447384081", "c600ca5dfe2a38c88ce7772a8043bf90", [
                              EffectParam("effects_adjust_filter", 0.730, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认73%, 0% ~ 100%"""
    食色                 = EffectMeta("食色", True, "7145435270819615233", "7145435270819615233", "8540ba0ddb988c6f5f4b69742ca94136", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    香槟之宴             = EffectMeta("香槟之宴", True, "7374404639032087056", "7374404639032087056", "bf70901848aa258c18fbf3fc2abdb4e6", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    香槟色老钱风         = EffectMeta("香槟色老钱风", True, "7405899632129102337", "7405899632129102337", "0412126dd3c805b6c0d1852f165e7371", [])
    香芋粉               = EffectMeta("香芋粉", True, "7047117739231547905", "7047117739231547905", "2b6a28443d5e06df19aae97d4386589d", [])
    马尔代夫             = EffectMeta("马尔代夫", True, "7246697364080038402", "7246697364080038402", "1914ac777ddb29d31915a3c891497058", [])
    高清增质             = EffectMeta("高清增质", True, "7442232228639150609", "7442232228639150609", "b8dc71511600efc38fb8f97a46a38169", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清影视荧幕         = EffectMeta("高清影视荧幕", True, "7446710887122997777", "7446710887122997777", "058528ce01cfc95dacae4d7603099516", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清暖调             = EffectMeta("高清暖调", True, "7431520244448891409", "7431520244448891409", "b48c7a7077dce7ed8d6a6004d06318d0", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高清美食             = EffectMeta("高清美食", True, "7441898838178140688", "7441898838178140688", "ef412640d836216b3e94330eb23ca568", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高级暗调             = EffectMeta("高级暗调", True, "7501373363269406013", "7501373363269406013", "fd1ad5a8e75fcf239f9203fa87884ebe", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高级灰               = EffectMeta("高级灰", True, "7505830521537072445", "7505830521537072445", "efece282596e29b53bf661d259794e04", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    高质1                = EffectMeta("高质1", True, "7220354135336423937", "7220354135336423937", "81f43e96e1c9938f02ec47018ff755b8", [])
    高质2                = EffectMeta("高质2", True, "7220376610380190210", "7220376610380190210", "3ec0d714ea1b0fb34e998e23a89e544f", [])
    高饱和               = EffectMeta("高饱和", True, "7145435244370334209", "7145435244370334209", "bb528a7fc6d356c7866ad592c972226b", [])
    鬼魅                 = EffectMeta("鬼魅", True, "7294210778830213633", "7294210778830213633", "2e32e3b4e71767f65e9daa4761eb471a", [])
    黄石                 = EffectMeta("黄石", True, "7212475600143929857", "7212475600143929857", "0c1f3337ec66a2fec5fce2ba860cf6dd", [])
    黄紫                 = EffectMeta("黄紫", True, "7226300464646607362", "7226300464646607362", "1c51b13e80dc529a0da9ed940d529157", [])
    黄金时刻             = EffectMeta("黄金时刻", True, "7206214079315186177", "7206214079315186177", "1ebad962a9d55a71eccb565d40e92879", [])
    黄金海岸             = EffectMeta("黄金海岸", True, "7212516438605566466", "7212516438605566466", "e1e7c1dd9a9bb039278297947c110081", [])
    黑冰                 = EffectMeta("黑冰", True, "7145435242445148674", "7145435242445148674", "bbd7f8c5166876f8c5ad3614d2e04dbd", [])
    黑森林               = EffectMeta("黑森林", True, "6875940953635426817", "6875940953635426817", "75a5027b98be7a31efb2c2f93239205a", [])
    黑白幽光             = EffectMeta("黑白幽光", True, "7524339063055289653", "7524339063055289653", "dbc84e30b924ae82191bdea938c24276", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑白负片             = EffectMeta("黑白负片", True, "7496116989040151869", "7496116989040151869", "8b01da1004317314592fd92ccfde07ae", [
                              EffectParam("effects_adjust_filter", 1.000, 0.000, 1.000)])
    """参数:
    effects_adjust_filter: 默认100%, 0% ~ 100%"""
    黑胶                 = EffectMeta("黑胶", True, "7394399556227568129", "7394399556227568129", "c35e784804029d3cbae7cec81cc72f56", [])
    黑豹                 = EffectMeta("黑豹", True, "7198431381368607234", "7198431381368607234", "7832398e5265f0e071594b8aed73dac0", [])
    黑金                 = EffectMeta("黑金", True, "7146475570623156738", "7146475570623156738", "9bd1add435ea65bdf3c51f5e8597952d", [])
    黑黄                 = EffectMeta("黑黄", True, "7226300464638202370", "7226300464638202370", "3b8072fd5557a0480151e937fa4c2c51", [])
