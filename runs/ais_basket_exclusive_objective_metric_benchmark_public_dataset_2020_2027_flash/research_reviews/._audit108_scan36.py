# -*- coding: utf-8 -*-
import io, re
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t36 = io.open(f36, encoding='utf-8').read()
for term in ['信任分数', '攻击概率', '攻击意图', '逐时间步', '通道级归因']:
    hits = [m.start() for m in re.finditer(term, t36)]
    print(term, len(hits))
    for h in hits[:4]:
        print('   ...', t36[max(0,h-40):h+40].replace(chr(10),' '))
