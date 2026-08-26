# -*- coding: utf-8 -*-
import io, re
out = io.open('_struct.txt','w',encoding='utf-8')
for k, f in [('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    t = io.open(f, encoding='utf-8').read()
    out.write('### '+k+'\n')
    for m in re.finditer(r'^#{2,4} [^\n]+$', t, re.M):
        out.write(m.group(0)+'\n')
    out.write('\n')
out.close()
