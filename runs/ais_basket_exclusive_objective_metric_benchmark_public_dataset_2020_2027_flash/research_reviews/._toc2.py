# -*- coding: utf-8 -*-
import io, re
for n in ['34','35','36']:
    fn = {'34':'34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
          '35':'35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
          '36':'36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'}[n]
    t = io.open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print('='*10, n, '='*10)
    for m in re.finditer(r'^#{2,3} .*$', main, re.M):
        print(m.group(0))
