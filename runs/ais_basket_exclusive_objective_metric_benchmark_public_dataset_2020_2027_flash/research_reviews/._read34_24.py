# -*- coding: utf-8 -*-
import io
def sec(fn, start, end):
    t = io.open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    i = main.find(start); j = main.find(end, i+1)
    return main[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 34 2.4 =====')
print(sec('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','### 2.4','### 2.5'))
