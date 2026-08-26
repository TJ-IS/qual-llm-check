# -*- coding: utf-8 -*-
import io
fixes = [
 ('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
  'IS 检测文献已为通道互补提供经验基础（相关证据的综述见 2.2 节）。据此，本文的融合检测设计以跨通道注意力建模通道间的交互。',
  'IS 检测文献已为通道互补提供经验基础（相关证据的综述见 2.2 节）。本文将背离信号形式化为逐时间步信任分数，背离越明显，信任分数越低，其计算实例为 5.1 节定义的攻击概率 p_t。据此，本文的融合检测设计以跨通道注意力建模通道间的交互。'),
 ('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
  '为保护编码智能体部署，组织正在部署输入过滤、沙箱隔离、权限控制与行为监控等防护机制（Yang et al., 2024）',
  '为保护编码智能体部署，组织正在建立输入过滤、沙箱隔离、权限控制与行为监控等防护机制（Yang et al., 2024）'),
]
for f, old, new in fixes:
    t = io.open(f, encoding='utf-8').read()
    n = t.count(old)
    if n != 1:
        print('!!', f, '匹配数', n)
        continue
    io.open(f, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('已修改', f)
