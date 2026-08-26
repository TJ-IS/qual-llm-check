import re
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
m = re.search(r'## 九、结论与未来研究\n(.*)', main, re.S)
print(m.group(1).strip()[:2600])
