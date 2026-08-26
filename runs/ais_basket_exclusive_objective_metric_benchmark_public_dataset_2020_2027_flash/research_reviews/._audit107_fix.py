# -*- coding: utf-8 -*-
import io
fixes = [
 ('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
  '威胁驱动设计是安全工程中以攻击者为中心的方法论，主张安全设计始于系统化理解攻击者如何行动，再据此设计防御（Shostack, 2014）。缺乏对攻击者行为建模的防御设计难以应对未见攻击（Shostack, 2014）。',
  '威胁驱动设计是安全工程中以攻击者为中心的方法论，主张安全设计始于系统化理解攻击者如何行动，再据此设计防御（Shostack, 2014）。缺乏对攻击者行为建模的防御设计难以应对未见攻击。'),
 ('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
  '这些机制被期望识别并阻断攻击，防止其造成危害（Apruzzese et al., 2019; Yang et al., 2024）。',
  '这些机制旨在识别并阻断攻击，防止其造成危害（Apruzzese et al., 2019; Yang et al., 2024）。'),
]
for f, old, new in fixes:
    t = io.open(f, encoding='utf-8').read()
    n = t.count(old)
    if n != 1:
        print('!!', f, '匹配数', n)
        continue
    io.open(f, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('已修改', f)
