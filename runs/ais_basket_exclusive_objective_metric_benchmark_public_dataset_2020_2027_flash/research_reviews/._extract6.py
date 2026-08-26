# -*- coding: utf-8 -*-
import io, re
def sec(fn, start, end):
    t = io.open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    i = main.find(start); j = main.find(end, i+1) if end else len(main)
    return main[i:j] if i>=0 else 'NOT FOUND: '+start
for n, fn in [('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'),
              ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
              ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    print('='*20, n, '第六章', '='*20)
    print(sec(fn, '## 六、预期结果', '## 七、'))
