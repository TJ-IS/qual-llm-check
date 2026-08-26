# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t35 = open(base+'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
for kw in ['将任务可操纵的内容划分为单元集合', '任务开始前的可观测信号（问题文本']:
    print('==== 35', kw)
    for m in re.finditer(kw, t35):
        print('...', t35[max(0,m.start()-130):m.start()+70].replace(chr(10),' '))
        print()
for kw in ['信息操纵理论（information manipulation theory）解释了']:
    print('==== 36', kw)
    for m in re.finditer(kw, t36):
        print('...', t36[max(0,m.start()-130):m.start()+80].replace(chr(10),' '))
        print()
