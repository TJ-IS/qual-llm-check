# -*- coding: utf-8 -*-
import io, re
for f, tag in [('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','34'),
               ('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','35'),
               ('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','36')]:
    lines = io.open(f, encoding='utf-8').read().splitlines()
    print('====', tag)
    # Latin followed directly by CJK, or CJK followed directly by Latin (no space)
    pat = re.compile(r'([A-Za-z0-9\u03b1-\u03c9\u0394\u03a3])([\u4e00-\u9fff\u3001\uff08\uff09\uff0c\u3002])|([\u4e00-\u9fff])([A-Za-z0-9])')
    for i, ln in enumerate(lines, 1):
        if ln.startswith('## \u53c2\u8003\u6587\u732e'):
            break
        for m in pat.finditer(ln):
            start = max(0, m.start()-12)
            end = min(len(ln), m.end()+12)
            print('  %3d ...%s...' % (i, ln[start:end]))
