# -*- coding: utf-8 -*-
import io, re
out = io.open('_r35ch67.txt','w',encoding='utf-8')
t = io.open('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
m = re.search(r'## 六、预期结果\n(.*?)(?=\n## 八、可行性分析)', t, re.S)
out.write(m.group(1))
out.close()
