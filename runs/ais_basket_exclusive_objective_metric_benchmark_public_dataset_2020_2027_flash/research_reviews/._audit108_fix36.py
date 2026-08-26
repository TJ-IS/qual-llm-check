# -*- coding: utf-8 -*-
import io
f = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = io.open(f, encoding='utf-8').read()
old = '（相关证据的综述见 2.2 节）。\n\n据此，本文的融合检测设计以跨通道注意力建模通道间的交互。'
new = '（相关证据的综述见 2.2 节）。本文将背离信号形式化为逐时间步信任分数，背离越明显，信任分数越低，其计算实例为 5.1 节定义的攻击概率 p_t。\n\n据此，本文的融合检测设计以跨通道注意力建模通道间的交互。'
n = t.count(old)
print('匹配数', n)
if n == 1:
    io.open(f, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('已修改 36')
