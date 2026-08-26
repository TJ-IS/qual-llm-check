# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
out = []
for k, f in files.items():
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    m = re.search(r'^## 二、.*?(?=^## 三、)', text, re.M | re.S)
    out.append('##### %s 第二章 #####' % k)
    if m:
        out.append(m.group(0).strip())
    else:
        out.append('未找到')
    out.append('')
io.open(os.path.join(DIR, '_ch2_all.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')