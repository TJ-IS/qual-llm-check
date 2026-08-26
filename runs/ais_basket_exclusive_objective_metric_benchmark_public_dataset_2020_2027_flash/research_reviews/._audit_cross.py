import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    print(f'========== {n}: 研究一二三互引 ==========')
    for kw in ['研究一', '研究二', '研究三', 'D_att', '攻击基准']:
        hits = [m.start() for m in re.finditer(kw, main)]
        if hits:
            print(f'--- {kw} x{len(hits)}')
            for h in hits[:8]:
                s = max(0, h-70); e = min(len(main), h+90)
                print('   ', main[s:e].replace(chr(10),' '))
    print()
