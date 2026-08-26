import re
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
pat = re.compile(r'Yang[^。\n]{0,60}2023')
for m in pat.finditer(main):
    s = max(0, m.start()-60); e = min(len(main), m.end()+40)
    print('>>>', main[s:e].replace(chr(10),' '))
    print()
