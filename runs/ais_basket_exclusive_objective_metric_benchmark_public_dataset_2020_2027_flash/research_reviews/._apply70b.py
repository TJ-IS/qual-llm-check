# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
f35 = base + '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(f35, encoding='utf-8').read()
old = '深度攻击面预测器分别编码三类静态信号，经跨通道注意力融合后输出单元级操纵风险与任务级风险分。'
new = '深度攻击面预测器分别编码三类静态信号，经跨通道注意力融合后得到单元级操纵风险与任务级风险分。'
assert t.count(old) == 1, t.count(old)
open(f35, 'w', encoding='utf-8').write(t.replace(old, new))
t2 = open(f35, encoding='utf-8').read()
print('输出单元级操纵风险与任务级风险分', t2.count('输出单元级操纵风险与任务级风险分'))
print('done')
