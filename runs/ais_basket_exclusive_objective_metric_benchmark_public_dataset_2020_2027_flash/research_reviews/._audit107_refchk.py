# -*- coding: utf-8 -*-
import io, re
for k, f in [('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
             ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md')]:
    t = io.open(f, encoding='utf-8').read()
    refs = t.split('## 参考文献',1)[1]
    print('='*20, k)
    # print all numbered entries with line breaks preserved
    for m in re.finditer(r'^\[(\d+)\]\s*(.*?)(?=^\[\d+\]|\Z)', refs, flags=re.M|re.S):
        num = m.group(1)
        if k=='35' and num in ('13','16','24') or k=='36' and num=='20':
            print(f'  [{num}] {m.group(2).strip()[:300]}')
