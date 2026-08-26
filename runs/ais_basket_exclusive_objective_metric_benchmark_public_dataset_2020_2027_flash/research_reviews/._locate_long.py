import re
for n, fn in [
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'),
]:
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    body = re.sub(r'^#+ .*$', '', main, flags=re.M)
    sents = [s for s in re.split(r'(?<=[。！？])', body) if len(s.strip()) >= 12]
    for s in sorted(sents, key=len, reverse=True)[:6]:
        if len(s) >= 130:
            # locate section
            pos = main.find(s[:50])
            sec = main[:pos].split('\n')[-1].strip()
            # find heading
            hs = [m for m in re.finditer(r'^#{2,3} [^\n]+', main, re.M) if m.start() < pos]
            hd = hs[-1].group(0) if hs else '?'
            print(f'== {n} [{len(s)}] 位于 {hd}')
            print('   ', s.strip()[:400])
            print()
