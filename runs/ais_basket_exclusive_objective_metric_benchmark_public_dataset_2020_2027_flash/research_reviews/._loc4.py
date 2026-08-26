# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t35 = open(base+'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
def show(t, kw, tag):
    print('====', tag, kw)
    for m in re.finditer(kw, t):
        s = t.rfind('。', 0, m.start()-100)
        e = t.find('。', m.start()+len(kw))
        print('   ...', t[s+1:e+1][:260])
    print()
show(t35, '评估协议同时报告安全收益与效用代价', '35')
show(t36, '意图与行为背离这一情境特有的检测信号', '36')
show(t36, '输出逐时间步攻击概率与通道级归因', '36')
