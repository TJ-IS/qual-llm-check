# -*- coding: utf-8 -*-
import io, re
for k, f in [('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
             ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    t = io.open(f, encoding='utf-8').read()
    m = re.search(r'^## 二、[^\n]*\n(.*?)^## 参考文献', t, flags=re.M|re.S)
    io.open(f'._audit107_body{k}.txt','w',encoding='utf-8').write(m.group(1).strip())
    print(k, 'saved', len(m.group(1)))
