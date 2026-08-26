# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t35 = open(base+'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
t36 = open(base+'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
def show(t, kw, tag):
    print('====', tag, kw)
    for m in re.finditer(kw, t):
        s = t.rfind('。', 0, m.start()-80)
        e = t.find('。', m.start()+len(kw))
        print('   ...', t[s+1:e+1][:220])
    print()
for kw in ['输出单元级操纵风险与任务级风险分','评估预测器的风险筛查与单元级定位','多模态攻击面预测器与基于约束优化的分配','我们采用任务级攻击风险的整体视角','在降低攻击风险的同时保持任务效用','评估协议同时报告安全收益与效用代价']:
    show(t35, kw, '35')
for kw in ['意图与行为背离这一情境特有的检测信号','仓库状态与环境反馈是外部可验证事实','技术威胁规避理论的规避成本机制','信息操纵理论、担保理论与技术威胁规避理论','检测与门控必须在智能体动作生效前完成','输出逐时间步攻击概率与通道级归因']:
    show(t36, kw, '36')
