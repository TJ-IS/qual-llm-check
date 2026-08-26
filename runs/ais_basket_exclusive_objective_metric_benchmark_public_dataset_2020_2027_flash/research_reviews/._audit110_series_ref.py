# -*- coding: utf-8 -*-
import io, re
jobs = [
 ('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'),
]
for k, f in jobs:
    t = io.open(f, encoding='utf-8').read()
    print('='*15, k)
    for m in re.finditer(r'研究[一二三]', t):
        s = max(0, m.start()-50); e = min(len(t), m.end()+60)
        print('  ...', t[s:e].replace(chr(10),' '))
