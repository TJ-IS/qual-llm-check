import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# citation patterns: (Author et al., 2020) (Author & Author, 2020) (Author, 2020) Author et al. (2020) Author & Author (2020)
pat = re.compile(r'(?:（|\(|(?<![A-Za-z])\s)([A-Z][A-Za-z\-\.]+(?: et al\.| & [A-Z][A-Za-z\-\.]+)?|OWASP|MCP)(?:,|\s+|，)?\s*\(?(\d{4}[ab]?)\)?')
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    sections = re.split(r'\n(?=#)', main)
    print(f'########## {n} ##########')
    for sec in sections:
        title = sec.split('\n')[0][:60]
        hits = []
        for m in pat.finditer(sec):
            before = sec[max(0,m.start()-45):m.start()]
            after = sec[m.end():m.end()+25]
            ctx = (before+after).replace('\n',' ')
            hits.append((m.group(1), m.group(2), ctx))
        if hits:
            print(f'--- {title}')
            for a,b,c in hits:
                print(f'  {a}, {b}  ...{c}...')
