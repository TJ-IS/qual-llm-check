import re
fn = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
m = re.search(r'### 3.5 方法论挑战\n(.*?)\n## 四、研究问题', main, re.S)
print('===== 35 3.5 方法论挑战 =====')
print(m.group(1).strip()[:3500])
print()
m = re.search(r'### 8.1 数据可得性\n(.*?)\n### 8.2', main, re.S)
print('===== 35 8.1 数据可得性 =====')
print(m.group(1).strip()[:2500])
