# -*- coding: utf-8 -*-
import io
def sec(fn, start, end):
    t = io.open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    i = main.find(start); j = main.find(end, i+1)
    return main[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 35 2.4 =====')
print(sec('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','### 2.4','### 2.5'))
print()
print('===== 36 2.4 =====')
print(sec('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','### 2.4','### 2.5'))
