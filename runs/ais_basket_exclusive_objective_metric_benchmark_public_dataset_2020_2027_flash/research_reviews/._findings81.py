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
    lines = io.open(os.path.join(DIR, f), encoding='utf-8').read().split('\n')
    out.append('===== %s 预期发现标签 =====' % k)
    for i, ln in enumerate(lines):
        m = re.search(r'预期发现([一二三四五六])（([^）]+)）', ln)
        if m:
            # 取标签后第一个句子的前40字作为内容摘要
            rest = ln[m.end():]
            seg = re.split(r'[。？]', rest)
            content = seg[0].strip()[:60] if seg and seg[0].strip() else ''
            out.append('L%d 预期发现%s（%s）: %s' % (i+1, m.group(1), m.group(2), content))
io.open(os.path.join(DIR, '_findings81.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
