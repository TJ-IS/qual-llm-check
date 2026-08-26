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
    body = text.split('## 参考文献')[0]
    lines = [l.strip() for l in body.split('\n') if l.strip() and not l.startswith('#')]
    para = ' '.join(lines)
    sents = [s.strip() for s in re.split(r'(?<=[。])', para) if len(s.strip()) >= 60]
    sents.sort(key=len, reverse=True)
    out.append('===== %s 引言及其他长句 Top 25 =====' % k)
    for s in sents[:25]:
        out.append('[%d字] %s' % (len(s), s[:150]))
io.open(os.path.join(DIR, '_long_sents.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')