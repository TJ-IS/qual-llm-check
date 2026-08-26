# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t35 = open(base+'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
i = t35.find('为弥合这一缺口')
print('== 35 引言 P5 ==')
print(t35[i:i+900])
print()
j = t36.find('为回答这些问题')
print('== 36 引言 P5 ==')
print(t36[j:j+700])
