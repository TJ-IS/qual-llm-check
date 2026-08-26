import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    m = re.search(r'## 参考文献(.*)', t, re.S)
    refs = m.group(1).strip()
    entries = re.findall(r'\[(\d+)\]\s*(.*?)(?=\n\[\d+\]|\Z)', refs, re.S)
    out = []
    for num, body in entries:
        one = ' '.join(body.split())
        out.append(f'[{num}] {one}')
    open(f'._refs_{n}.txt','w',encoding='utf-8').write('\n'.join(out))
    print(n, len(entries))
