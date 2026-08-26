import re
fn = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
t = open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
m = re.search(r'### 5.5 D_att 基准构建\n(.*?)\n### 5.6', main, re.S)
print('===== 34 5.5 D_att 基准构建 =====')
print(m.group(1).strip()[:3500])
