# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# 1) 十六字长串重复（单篇内部）
print('== 单篇十六字长串重复 ==')
for k, f in files.items():
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    body = re.sub(r'【占位[^】]*】', 'P', body)
    body = re.sub(r'（[^）]*\d{4}[^）]*）', 'C', body)
    n = len(body)
    seen = {}
    for i in range(n-16):
        s = body[i:i+16]
        if 'C' in s or 'P' in s: continue
        seen.setdefault(s, []).append(i)
    dup = {s: pos for s, pos in seen.items() if len(pos) > 1}
    if not dup:
        print(k, '无重复')
    else:
        for s, pos in list(dup.items())[:10]:
            print(k, repr(s), pos[:4])
# 2) 目标串确认
print('== 目标串存在性 ==')
targets = {
 '34': ['确立先例，但均未涉及编码智能体的内容级攻击生成', '从攻击生成到防御评估的攻防闭环', '这一威胁并非假设性风险'],
 '35': ['能够同时编码意图与攻击面的方法', '预期危害降低的增幅逐步收窄', '对预期危害降低的贡献有限', '规则基线在追求高预防率时', '由预防的安全事故带来的成本节省有望显著超过预置防御的投入', '这些治理边界确保', '损害权重 d_i 表示单元被利用后', '离线处理时长为', '降低组织编码智能体安全风险方面的实践价值', '显示此类攻击已实际发生'],
 '36': ['以伪造的代码审查意见形式歪曲任务要求', '背离信号的通道分布', '拦截安全事故所避免的损失有望显著高于检测与门控的运营成本', '离线处理时长为', '是遏制编码智能体攻击危害的关键途径', '度量其偏离正常任务模式的程度', '面对信息操纵威胁'],
}
for k, f in files.items():
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    for t in targets[k]:
        print(k, t[:24], '->', text.count(t))