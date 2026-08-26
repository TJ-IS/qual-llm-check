# -*- coding: utf-8 -*-
import io, re
t36 = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
m = re.search(r'### 3\.4 信号互补与意图行为背离\n\n(.*?)(?=### 3\.5)', t36, flags=re.S)
print('=== 36 3.4 修改后 ===')
print(m.group(1).strip()[:900])
t35 = io.open('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md', encoding='utf-8').read()
m2 = re.search(r'为保护编码智能体部署[^。]*。', t35)
print()
print('=== 35 P1 修改后 ===')
print(m2.group(0))
