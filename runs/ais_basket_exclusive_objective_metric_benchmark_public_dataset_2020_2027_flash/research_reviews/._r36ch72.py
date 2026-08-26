# -*- coding: utf-8 -*-
import io, re
out = io.open('_r36ch72.txt','w',encoding='utf-8')
t = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
m = re.search(r'### 7\.1 对信息系统知识库的贡献\n(.*?)(?=\n### 7\.3 设计原则)', t, re.S)
out.write(m.group(1))
out.close()
