import re
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
for kw in ['研究一', '研究二', '研究三', 'D_att', 'AgentShield-Adversary', 'AttackRL-Agent']:
    hits = [m.start() for m in re.finditer(kw, main)]
    print(f'--- {kw} x{len(hits)}')
    for h in hits:
        s = max(0, h-90); e = min(len(main), h+110)
        print('   ', main[s:e].replace(chr(10),' '))
        print()
