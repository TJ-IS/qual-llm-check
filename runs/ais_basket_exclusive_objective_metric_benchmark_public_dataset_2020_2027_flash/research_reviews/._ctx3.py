# -*- coding: utf-8 -*-
import io, re
out = io.open('_ctx_out3.txt','w',encoding='utf-8')
text = io.open('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md', encoding='utf-8').read()
m = re.search(r'### 2\.5[^\n]*\n(.*?)(?=\n### 2\.6|\n## 3\.|\n### 3\.)', text, re.S)
out.write(m.group(0) if m else 'NOT FOUND')
out.close()
