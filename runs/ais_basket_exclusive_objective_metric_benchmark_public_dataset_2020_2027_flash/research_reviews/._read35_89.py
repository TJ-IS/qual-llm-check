# -*- coding: utf-8 -*-
import io
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = io.open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
i = main.find('## 八、')
print(main[i:])
