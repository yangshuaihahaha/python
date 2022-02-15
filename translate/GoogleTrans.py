# -*- coding: utf-8 -*-
import re
import time
import urllib
import urllib2

import execjs
from raven.utils import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class GoogleTrans(object):
    def __init__(self):
        self.url = 'https://translate.google.cn/translate_a/single'
        self.TKK = "434674.96463358"  # 随时都有可能需要更新的TKK值
        self.header = {
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": "NID=188=M1p_rBfweeI_Z02d1MOSQ5abYsPfZogDrFjKwIUbmAr584bc9GBZkfDwKQ80cQCQC34zwD4ZYHFMUf4F59aDQLSc79_LcmsAihnW0Rsb1MjlzLNElWihv-8KByeDBblR2V1kjTSC8KnVMe32PNSJBQbvBKvgl4CTfzvaIEgkqss",
            "referer": "https://translate.google.cn/",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "x-client-data": "CJK2yQEIpLbJAQjEtskBCKmdygEIqKPKAQi5pcoBCLGnygEI4qjKAQjxqcoBCJetygEIza3KAQ==",
        }
        self.data = {
            "client": "webapp",  # 基于网页访问服务器
            "sl": "auto",  # 源语言,auto表示由谷歌自动识别
            "tl": "vi",  # 翻译的目标语言
            "hl": "zh-CN",  # 界面语言选中文，毕竟URL都是cn后缀了，就不装美国人了
            "dt": ["at", "bd", "ex", "ld", "md", "qca", "rw", "rm", "ss", "t"],  # dt表示要求服务器返回的数据类型
            "otf": "2",
            "ssel": "0",
            "tsel": "0",
            "kc": "1",
            "tk": "",  # 谷歌服务器会核对的token
            "q": ""  # 待翻译的字符串
        }
        self.js = '''
                var uo = function (a, b) {
                                for (var c = 0; c < b.length - 2; c += 3) {
                                    var d = b.charAt(c + 2);
                                    d = "a" <= d ? d.charCodeAt(0) - 87 : Number(d);
                                    d = "+" == b.charAt(c + 1) ? a >>> d : a << d;
                                    a = "+" == b.charAt(c) ? a + d & 4294967295 : a ^ d
                                }
                                return a
                            },
                wo = function (a, tkk) {
                    var d = tkk.split(".");
                    var b = Number(d[0]);
                    for (var e = [], f = 0, g = 0; g < a.length; g++) {
                        var h = a.charCodeAt(g);
                        128 > h ? e[f++] = h :
                            (2048 > h ? e[f++] = h >> 6 | 192 :
                                    (55296 == (h & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (h = 65536 + ((h & 1023) << 10) + (a.charCodeAt(++g) & 1023), e[f++] = h >> 18 | 240, e[f++] = h >> 12 & 63 | 128) :
                                        e[f++] = h >> 12 | 224, e[f++] = h >> 6 & 63 | 128), e[f++] = h & 63 | 128)
                    }
                    a = b;
                    for (f = 0; f < e.length; f++)
                        a += e[f],
                        a = uo(a, "+-a^+6");
                    a = uo(a, "+-3^+b+-f");
                    a ^= Number(d[1]) || 0;
                    0 > a && (a = (a & 2147483647) + 2147483648);
                    a %= 1E6;
                    return (a.toString() + "." + (a ^ b))
                };
                '''
        self.js_fun = execjs.compile(self.js)

        # 构建完对象以后要同步更新一下TKK值
        # self.update_TKK()

    def update_TKK(self):
        url = "https://translate.google.cn/"
        req = urllib2.Request(url=url, headers=self.header)
        page_source = urllib2.urlopen(req).read().decode("utf-8")
        self.TKK = re.findall(r"tkk:'([0-9]+\.[0-9]+)'", page_source)[0]

    def construct_url(self):
        base = self.url + '?'
        for key in self.data:
            if isinstance(self.data[key], list):
                base = base + "dt=" + "&dt=".join(self.data[key]) + "&"
            else:
                base = base + key + '=' + self.data[key] + '&'
        base = base[:-1]
        return base

    def query(self, q, lang_to=''):
        if q is not None:
            try:
                print '字符串长度', len(q)
                q = q.encode("utf-8")
                self.data['q'] = urllib.pathname2url(q)
                self.data['tk'] = self.js_fun.call('wo', q, self.TKK)
                self.data['tl'] = lang_to
                url = self.construct_url()
                req = urllib2.Request(url=url, headers=self.header)
                response = json.loads(urllib2.urlopen(req).read().decode("utf-8"))
                targetText = response[0][0][0]
                print '翻译成功 --------------------------- '
                return targetText
            except Exception as e:
                if e.code == 429:
                    print '太多请求，休眠后重新翻译 --------------------------- ' + e.msg
                    time.sleep(1)
                    return GoogleTrans.query(q, lang_to)
                elif e.code == 413:
                    print '字符串过大，翻译失败 --------------------------- ' + e.msg
                elif type(e.reason) != str and e.reason.strerror == 'Operation timed out':
                    print '请求超时，重新翻译 --------------------------- ' + e.msg
                    return GoogleTrans.query(q, lang_to)
                else:
                    print '翻译失败， --------------------------- ' + e.msg
                print 'q --------------------------- :' + q
                pass


if __name__ == '__main__':
    text = '''肝脏活检中存在肝硬化。
    患有1型糖尿病。
    签署ICF前有恶性肿瘤史，除非已有5年以上无瘤期，或签署ICF前因活动性或疑似恶性肿瘤正在接受评估，经过充分治疗的基底细胞癌或鳞状细胞皮肤癌或者原位宫颈癌除外。
    在访视1/筛选前5年内（含）有减肥手术史（Roux-en-Y胃旁路手术、袖状胃切除术、胃束带）。 注：对于在访视1/筛选之前已获得基线肝脏活检的受试者，该活检之前≤5年必须没有减肥手术史，直至访视1/筛选。
    在签署≤ICF前3个月进行了大手术，或者在研究期间计划进行大手术。 注：在访视1/筛选前≤3个月接受过小手术且完全康复的受试者或计划进行小手术的受试者可参与研究。小手术定义为涉及局部麻醉的外科手术。
    以下病史或证据： NASH以外的慢性肝病 乙型肝炎（定义为存在HBsAg） 丙型肝炎，定义为存在HCV RNA或阳性丙型肝炎抗体（抗HCV）；如果HCV PCR阴性≥3年，则可纳入具有HCV感染史的受试者 注：对于在访视1/筛选之前已进行肝脏活检的受试者，该肝脏活检之前≥3年必须HCV PCR呈阴性，直至访视1/筛选。 药物性肝损伤 持续性自身免疫性肝病 失代偿性肝病（腹水、食管或胃静脉曲张破裂出血、肝性脑病或晚期肝病的其他体征或症状） HIV 原发性胆汁性肝硬化 原发性硬化性胆管炎 瑞氏综合征 脾肿大 威尔森病 记录在案的库欣病、库欣综合征或任何与皮质醇增多相关的疾病（即，大量的循环皮质醇，可能是病理或非病理疾病[如，功能性肾上腺腺瘤、小结节和大结节增生]） 甲状腺功能减退、甲状腺功能亢进或亚临床甲状腺疾病 注：亚临床甲状腺疾病定义为血清TSH水平异常，FT4和三碘甲状腺原氨酸水平在正常参考范围内。 α-1抗胰蛋白酶缺乏症 血色素沉着病或铁超负荷 自发性细菌性腹膜炎 已知胆管梗阻 肝细胞癌 未经治疗的阻塞性睡眠呼吸暂停 凝血障碍（如，Von Willebrand病、血友病、因子V Leiden血栓形成倾向、镰状细胞病、红细胞增多症、白血病） 造血系统疾病（如再生障碍性贫血、骨髓增生性或骨髓增生异常综合征、血小板减少症）
    除肝脏疾病外，还存在明显的全身性或重大疾病，包括最近发生（访视1/筛选前≤6个月）的充血性心力衰竭（美国心脏协会的纽约心脏病协会（NYHA）功能分类III-IV级）、不稳定型冠心病、动脉血运重建、肺病、肾功能衰竭、卒中、短暂性脑缺血发作或器官移植。
    对IMP中的任何活性成分或辅料的已知过敏史。
    在访视1/筛选前≤2个月经历过任何骨创伤、骨折或骨手术。
    在访视1/筛选时有骨质疏松症病史或需要使用排除标准#18中所列类别的骨活性药物治疗的适应症。 注：如果在完成访视1/筛选后发现需要使用排除标准#18中所列类别的骨活性药物治疗的适应症，则受试者不会被排除在研究参与之外。这包括在安慰剂导入期间通过DXA成像诊断为骨质疏松症的任何受试者（见第4.3.3节）。
    在访视1/筛选前≤24个月，有连续超过3个月的大量饮酒史或既往史。大量饮酒被定义为女性平均每周约7份标准酒精性饮品，男性平均每周约14份标准酒精性饮品。一份标准酒精性饮品被定义为任何含有14 g纯酒精的饮料，或根据当地指南的定义。 注：对于在访视1/筛选之前进行了基线肝脏活检的受试者，在该肝脏活检日之前≤24个月必须无连续3个月以上上述大量饮酒史，直至访视1/筛选。
    无法可靠地定量饮酒量。
    最近有药物滥用史（定义为≤3年）或在访视1/筛选时正在使用娱乐性药物或违禁药物。
    根据研究者的意见，患有已知的精神病或任何其他认知障碍，这将会干扰受试者与研究要求合作的能力。
    根据临床访谈和C-SSRS上的回答，研究者认为受试者存在即将发生自我伤害或伤害他人的风险。如果受试者在过去2个月内报告自杀意念与意图、有或无计划或方法自杀（例如，C-SSRS上的自杀意念评估中对项目4或5有积极回应）或过去6个月有自杀行为，则必须将其排除在外。更多详情参见第8.3.10.1.1节。
    PHQ-9的总评分>12（参见第8.3.10.1.2节）。 注：如果受试者在PHQ-9的问题#9中得分≥1（见附录11），但该受试者对C-SSRS的所有问题都回答“否”，则研究者必须核对其中的不一致以确定受试者的研究资格。
    正在使用或在访视1/筛选前≤24个月曾使用以下药物治疗： 噻唑烷二酮类（即吡格列酮，罗格列酮） 纤维酸衍生物（即贝特类） 奥贝胆酸 高剂量维生素E（>400 IU/天） L-鸟氨酸L-天冬氨酸 注：对于在访视1/筛选前进行了基线肝脏活检的受试者，在该肝脏活检日前≤24个月直至访视1/筛选期间禁止使用这些药物。
    正在使用或在访视1/筛选前24个月内已经使用下列类别的骨活性药物进行治疗。 双膦酸盐 降钙素 选择性雌激素受体调节剂（雌激素受体激动剂/拮抗剂） 甲状旁腺素（PTH）和PTH类似物 RANK配体抑制剂 抗硬化素抗体 芳香酶抑制剂 GnRH激动剂 注：如果在完成访视1/筛选后根据所确定的适应症而开始使用这些类别的药物，则受试者不会被排除在研究参与之外。这包括在安慰剂导入期间通过DXA成像诊断为骨质疏松症的任何受试者（见第4.3.3节）。
    在访视1/筛选前≤6个月接受过NAFLD治疗或使用过相关药物： 胺碘酮 合成类固醇 化疗药（即5-氟尿嘧啶、他莫西芬、伊立替康、顺铂与天冬酰胺酶） 可卡因 决奈达隆 剂量高于激素替代或避孕所用剂量水平的雌激素 甲氨蝶呤 核苷类逆转录酶抑制剂 四环素（高剂量静脉给药） 丙戊酸 其他已知的肝脏毒性 注： 在研究治疗干预给药期间，应避免接受具有肝毒性的药物（即产品说明书中警告具有肝毒性的药物）。鼓励研究者通过检索ncbi网站，搜索每种用药的潜在肝毒性。 对乙酰氨基酚最大允许剂量为4000 mg/天。 对于在访视1/筛选前进行了基线肝脏活检的受试者，在肝脏活检日前≤6个月直至访视1/筛选期间禁止使用这些药物。
    正接受治疗，或可能需要≥14天连续治疗，或多个疗程药理学剂量的皮质类固醇（如5 mg泼尼松或其他同等剂量糖皮质激素）。 注：允许使用吸入式、经鼻式、经眼式与局部给药的皮质类固醇药物，以及肾上腺类固醇的生理替代给药。
    在接受抗凝药物治疗（如华法林、肝素）。
    处于AHA治疗阶段，或使用表1所列其他用药且未处于表1所规定的稳定剂量。药物及其他物质的稳定用药的定义，详见临床试验方案表1.
    当前正在参加或在本研究前≤6个月内参加了使用试验性化合物或器械的干预性临床研究。可纳入参加观察性研究的受试者，入选这类受试者需要审查每例受试者的具体情况，并经申办方批准。
    出现表2所列的应排除的实验室检查值。 注：如果符合表2中列出的任何一项实验室排除标准，研究中心可以对该异常值进行一次复测。 实验室排除标准，详见临床试验方案表2.
    进行此研究中要求的常规外周血采集的静脉通路不佳。
    在访视1/筛选之前≤2个月内输入过血液制品和/或在访视1/筛选之前≤1个月内捐献过血液制品。 注：受试者在整个研究期间不得捐献血液制品。
    ECG出现临床显著性异常，需进一步诊断评价或治疗（如新发临床显著性心律不齐或传导障碍）。
    存在幽闭恐惧症，程度严重到无法承受MRI扫描检查。研究者可根据需要进行药物镇静。
    体内有任何阻碍无法进行MRI检查的金属移植物，包括但不限于：动脉瘤夹、金属异物、血管接枝物或心脏移植物、神经刺激器、金属节育器、金属纹身、无法取出的体环、人工耳蜗或MRI检查的任何其他禁忌物品。
    如果存在研究者认为会妨碍受试者完成研究的能力或依从性，或可能阻碍完成研究的任何其他病况。
    参加此研究的研究中心或申办方工作人员本人或其直系亲属（如配偶、父母/法定监护人、兄弟姐妹或子女）。'''
    targetText = GoogleTrans().query(text, lang_to='en')
    print targetText
