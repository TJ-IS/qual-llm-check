# -*- coding: utf-8 -*-
import io, re
jobs = [
 ('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'),
]
starts = ['此外', '然而', '因此', '由此', '据此', '同时', '换言之', '进一步', '总体', '综上', '具体', '为此', '在此基础上', '该', '本文', '我们']
for k, f in jobs:
    t = io.open(f, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    sents = [s.strip() for s in re.split(r'(?<=[。？！])', body) if s.strip()]
    from collections import Counter
    c = Counter()
    for s in sents:
        for st in starts:
            if s.startswith(st):
                c[st] += 1
                break
    print('='*12, k, '句数', len(sents))
    print('  句首统计:', dict(c))
    print('  进行:', body.count('进行'), ' 被期望:', body.count('被期望'), ' 即作为:', body.count('，即'))
