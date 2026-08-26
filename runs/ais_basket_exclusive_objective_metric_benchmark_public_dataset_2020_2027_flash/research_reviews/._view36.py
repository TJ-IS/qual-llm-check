# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
i = t.find('检测的目的不在于扩大过滤覆盖面')
print(t[i:i+560])
print()
j = t.find('为回答这些问题')
print(t[j:j+430])
