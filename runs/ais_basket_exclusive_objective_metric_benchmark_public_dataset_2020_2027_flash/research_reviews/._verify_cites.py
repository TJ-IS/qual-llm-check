import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
ref_first_authors = {
 '34': set('Apruzzese Rai Jimenez Yuan Goosen Li Sutton Kolter Shostack Gregor Yang Ebrahimi Ghoshal Menon Qu Lausen Madry Kwon Ampel Benjamin Hevner Walls Goodfellow Schulman Bertsimas Greshake OWASP'.split()),
 '35': set('Jimenez Yang Apruzzese Lin Zhang Qu Gregor Rai Ampel Wang Shangguan Yang Yang Ray Tsagkarakis du Wu Ghoshal Menon Li Lausen Hevner Walls Yang'.split()),
 '36': set('Jimenez Yang Apruzzese Li McCornack Glancy Humpherys Siering Walther Lausen Zhang Kumar Gopal Benjamin Liang Gregor Rai Walls Hevner Yang Gupta Vamosi Zhu Shan Ebrahimi Ghoshal Menon Qu Lin'.split()),
}
pat = re.compile(r'([A-Z][A-Za-z\-]+)(?:\s*et al\.|\s*等|\s*&\s*[A-Z][A-Za-z\-\.]+|\s*与\s*[A-Z][A-Za-z\-\.]+|\s*[A-Z][A-Za-z\-\.]+)?[，,]?\s*[（(]?\s*(\d{4}[ab]?)')
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = re.sub(r'【占位[^】]*】', '', t.split('## 参考文献')[0])
    uniq = {}
    for m in pat.finditer(main):
        uniq.setdefault((m.group(1), m.group(2)), 0)
        uniq[(m.group(1), m.group(2))] += 1
    miss = [(a,y,c) for (a,y),c in uniq.items() if a not in ref_first_authors[n] and a != 'Jardin']
    print(f'{n}: 正文引用组 {sum(uniq.values())} 个；首作者不在参考文献: {miss if miss else "无"}')
    # per-ref check for Hevner/Yang 2004/2023b in 36
    if n == '36':
        print('  36 Hevner+2004:', len(re.findall(r'Hevner[^。\n]{0,25}2004', main)), '; Yang+2023b:', len(re.findall(r'Yang[^。\n]{0,25}2023b', main)))
