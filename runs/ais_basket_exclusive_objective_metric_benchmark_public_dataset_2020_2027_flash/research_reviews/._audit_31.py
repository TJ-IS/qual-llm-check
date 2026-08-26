import re
for n, fn, start, end in [
 ('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','### 3.1','### 3.2'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','### 3.1','### 3.2'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','### 3.1','### 3.2'),
]:
    t = open(fn, encoding='utf-8').read()
    m = re.search(re.escape(start)+r'\n(.*?)'+re.escape(end), t, re.S)
    print(f'========== {n} {start} ==========')
    print(m.group(1).strip()[:3200])
    print()
