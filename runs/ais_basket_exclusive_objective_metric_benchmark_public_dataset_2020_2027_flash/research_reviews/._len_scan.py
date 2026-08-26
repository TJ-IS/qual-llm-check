import re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    body = re.sub(r'^#+ .*$', '', main, flags=re.M)
    sents = [s for s in re.split(r'(?<=[。！？])', body) if len(s.strip()) >= 12]
    lens = sorted([(len(s), s.strip()) for s in sents], reverse=True)
    print(f'===== {n}: 句子总数 {len(sents)}, 平均 {sum(l for l,_ in lens)//len(sents)} 字 =====')
    print('--- 最长的 8 句 ---')
    for l, s in lens[:8]:
        print(f'  [{l}] {s.strip()[:120]}...' if l > 90 else f'  [{l}] {s.strip()[:120]}')
    print()
