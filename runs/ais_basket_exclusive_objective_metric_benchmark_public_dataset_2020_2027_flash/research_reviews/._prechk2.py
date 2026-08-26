import re
for n, fn, kw in [
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','不加区分'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','植入恶意内容'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','植入恶意内容'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','逐步生效'),
]:
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print(f'== {n} {kw} x{len(re.findall(kw, main))}')
    for m in re.finditer(kw, main):
        s = max(0, m.start()-70); e = min(len(main), m.end()+70)
        print('   ', main[s:e].replace(chr(10),' '))
    print()
