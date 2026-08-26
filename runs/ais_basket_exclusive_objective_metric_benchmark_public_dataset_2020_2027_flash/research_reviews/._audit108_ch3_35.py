# -*- coding: utf-8 -*-
import io, re
t = io.open('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
m = re.search(r'^## 三、[^\n]*\n(.*?)^## 四、', t, flags=re.M|re.S)
ch3 = m.group(1)
print('=== 35 第三章 ===')
print(ch3[:4200])
