import re
for n, fn, start, end in [
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','## 二、文献综述与研究缺口','## 三、'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','## 二、文献综述与研究缺口','## 三、'),
]:
    t = open(fn, encoding='utf-8').read()
    m = re.search(re.escape(start)+r'\n(.*?)\n'+re.escape(end), t, re.S)
    open(f'._ch2_{n}.txt','w',encoding='utf-8').write(m.group(1).strip())
    print(n, len(m.group(1)))
