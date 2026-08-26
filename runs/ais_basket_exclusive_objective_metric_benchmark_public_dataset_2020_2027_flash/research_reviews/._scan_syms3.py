# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
syms = {
 '\u2014':'破折号—', '\u2013':'短横–', '\u2015':'横线―', '\u201c':'左双引“', '\u201d':'右双引”',
 '\u2018':'左单引‘', '\u2019':'右单引’', '\uff1a':'全角冒号：', '\uff1b':'全角分号；',
 '\u2026':'省略号…', '\u2192':'箭头→', '\u2039':'‹', '\u203a':'›', '\u00ab':'«', '\u00bb':'»',
 '\uff08':'（', '\uff09':'）', '\u300a':'《', '\u300b':'》',
}
for k, f in files.items():
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    refs = text.split('## 参考文献',1)[1]
    print('=====', k, '=====')
    for part_name, part in [('正文', body), ('参考文献', refs)]:
        found = []
        for ch, name in syms.items():
            cnt = part.count(ch)
            if cnt:
                found.append('%s:%d' % (name, cnt))
        if found:
            print(part_name, '|', ', '.join(found))
        else:
            print(part_name, '| 上述符号全零')
    # 半角冒号/分号统计（正文，仅英文引文内合规）
    half_colon = len(re.findall(r':', body))
    half_semi = len(re.findall(r';', body))
    print('正文半角冒号:', half_colon, '| 正文半角分号:', half_semi)