# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk7.txt','w',encoding='utf-8')
t36 = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
refs = t36.split('## 参考文献')[1]
for m in re.finditer(r'^\s*\[\d+\][^\n]*', refs, re.M):
    line = m.group(0)
    if any(w in line for w in ['Benjamin','Raghu','Kumar','Vamosi','Zhu','Gopal','Gupta','Glancy','Siering','Humpherys']):
        out.write(line.strip()[:160] + '\n')
out.close()
