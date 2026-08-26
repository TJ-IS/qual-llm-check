import re
files = {
 '34': ('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','### 7.1 对信息系统知识库的贡献','### 7.2'),
 '35': ('35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','### 7.1 对信息系统知识库的贡献','### 7.2'),
 '36': ('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','### 7.1 对信息系统知识库的贡献','### 7.2'),
}
for n, (fn, a, b) in files.items():
    t = open(fn, encoding='utf-8').read()
    m = re.search(re.escape(a)+r'\n(.*?)\n'+re.escape(b), t, re.S)
    print(f'========== {n} 7.1 ==========')
    print(m.group(1).strip())
    print()
