# -*- coding: utf-8 -*-
import io, re
out = io.open('_r35ch2.txt','w',encoding='utf-8')
t = io.open('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
m = re.search(r'## 二、文献综述与研究缺口\n(.*?)(?=\n## 三、理论基础与设计理由)', t, re.S)
out.write(m.group(1))
out.close()
