# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
f34 = base + '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
t = open(f34, encoding='utf-8').read()
old = 'Adversarial robustness—Theory and practice'
new = 'Adversarial robustness: Theory and practice'
assert t.count(old) == 1
open(f34, 'w', encoding='utf-8').write(t.replace(old, new))
# 复核参考文献中的引号是否都在英文标题内
for fn in ['34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md']:
    t2 = open(base+fn, encoding='utf-8').read()
    i = t2.find('“')
    print(fn[:6], '引号处:', repr(t2[max(0,i-80):i+80]))
