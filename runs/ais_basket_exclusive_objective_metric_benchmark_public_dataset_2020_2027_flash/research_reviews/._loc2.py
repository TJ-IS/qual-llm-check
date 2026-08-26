# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t35 = open(base+'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
i = t35.find('为弥合这一缺口，本文引入单元级操纵风险')
print('== 35 单元级操纵风险引入段 ==')
print(t35[max(0,i-500):i+620])
print()
j = t36.find('这一意图与行为背离信号在 IS 文献中已有理论依据')
print('== 36 引言动机段 ==')
print(t36[max(0,j-600):j+700])
