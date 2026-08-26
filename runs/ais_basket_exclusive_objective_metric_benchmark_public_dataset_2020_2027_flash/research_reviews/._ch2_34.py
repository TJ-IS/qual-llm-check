import re
fn = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
t = open(fn, encoding='utf-8').read()
m = re.search(r'## 二、文献综述与研究缺口\n(.*?)\n## 三、', t, re.S)
open('._ch2_34.txt','w',encoding='utf-8').write(m.group(1).strip())
print(len(m.group(1)))
