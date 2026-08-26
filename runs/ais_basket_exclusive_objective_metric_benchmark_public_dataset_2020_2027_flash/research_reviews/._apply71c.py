# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
f = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
p = os.path.join(DIR, f)
text = io.open(p, encoding='utf-8').read()
old = "开发了基于强化学习的攻击仿真框架 AgentShield-Adversary"
new = "开发了攻击仿真框架 AgentShield-Adversary"
c = text.count(old)
assert c == 1, c
text = text.replace(old, new)
io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply71c_log.txt'), 'w', encoding='utf-8').write('已落盘: %s\n' % old)
print('done')