# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for k,f in files.items():
    t = io.open(f, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    # split into sentences
    sents = [s for s in re.split(r'(?<=[。？！])', body) if s.strip()]
    print('='*20, k)
    for i in range(len(sents)-1):
        a = set(re.findall(r'[（(]([^（）()]*?\d{4}[^（）()]*?)[）)]', sents[i]))
        b = set(re.findall(r'[（(]([^（）()]*?\d{4}[^（）()]*?)[）)]', sents[i+1]))
        if a and a & b:
            inter = a & b
            print('  S%d 与 S%d 重复引用:' % (i+1, i+2), inter)
            print('    A:', sents[i].strip()[:110])
            print('    B:', sents[i+1].strip()[:110])
