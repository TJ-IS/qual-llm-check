# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for k, f in files.items():
    lines = io.open(f, encoding='utf-8').read().splitlines()
    print('====', k)
    for i, ln in enumerate(lines, 1):
        if ln.startswith('## \u53c2\u8003\u6587\u732e'):
            break
        for ch in [':', '"', "'", '\u2013', '\u2014', '\uff1a', '\u201c', '\u201d']:
            if ch in ln:
                for m in re.finditer(re.escape(ch), ln):
                    start = max(0, m.start()-15)
                    end = min(len(ln), m.end()+15)
                    print('  %3d %r ...%s...' % (i, ch, ln[start:end]))
