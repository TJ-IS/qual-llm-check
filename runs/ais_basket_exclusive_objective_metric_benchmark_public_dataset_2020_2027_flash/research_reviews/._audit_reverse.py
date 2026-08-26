import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# canonical author keys per paper from reference lists (last names)
ref_authors = {
 '34': set('Apruzzese Rai Jimenez Yuan Goosen Li Sutton Kolter Shostack Gregor Yang Ebrahimi Ghoshal Menon Qu Lausen Madry Kwon Ampel Benjamin Hevner Walls Goodfellow Schulman Bertsimas Greshake OWASP'.split()),
 '35': set('Jimenez Yang Apruzzese Lin Zhang Qu Gregor Rai Ampel Wang Shangguan Ray Tsagkarakis du Wu Ghoshal Menon Li Lausen Hevner Walls'.split()),
 '36': set('Jimenez Yang Apruzzese Li McCornack Glancy Humpherys Siering Walther Lausen Zhang Kumar Gopal Benjamin Liang Gregor Rai Walls Hevner Gupta Vamosi Zhu Shan Ebrahimi Ghoshal Menon Qu Lin'.split()),
}
# narrative citation: Author/等/et al. followed within 40 chars by (year) or , year
pat = re.compile(r'([A-Z][A-Za-z\-\.]+(?:\s*等|\s*et al\.|\s*&\s*[A-Z][A-Za-z\-\.]+)?)[，,、]?\s*[（(]?\s*(\d{4}[ab]?)')
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    # remove 占位 annotations to avoid false positives
    main2 = re.sub(r'【占位[^】]*】', '', main)
    found = []
    for m in pat.finditer(main2):
        name = m.group(1).strip()
        yr = m.group(2)
        found.append((name, yr))
    # dedupe consecutive duplicates (same group repeated)
    uniq = []
    for x in found:
        if not uniq or uniq[-1] != x:
            uniq.append(x)
    # flag author not in ref list
    print(f'##### {n} 正文引用作者清单（去重）#####')
    for name, yr in uniq:
        last = name.split()[-1].replace('&','').strip()
        flag = '  <-- 不在参考文献' if last not in ref_authors[n] else ''
        print(f'  {name}, {yr}{flag}')
    print()
