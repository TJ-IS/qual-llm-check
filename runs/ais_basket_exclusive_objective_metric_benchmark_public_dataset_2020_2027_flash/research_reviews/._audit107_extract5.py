# -*- coding: utf-8 -*-
import io, re
t = io.open('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md', encoding='utf-8').read()
m = re.search(r'^## 二、$(.*)$', t, flags=re.M|re.S)
out = io.open('._audit107_body34.txt', 'w', encoding='utf-8')
out.write(m.group(1) if m else t)
out.close()
print('saved', len(m.group(1)) if m else 0)
