# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
pat = re.compile(r'【占位[^】]*】')
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    for m in pat.finditer(body):
        s = m.group(0)
        if s != '【占位】' and s != '【占位，':
            print(n, '|', s, '| ctx:', body[max(0,m.start()-25):m.end()+8].replace('\n',' '))
    if '需核对' in body:
        print(n, 'HAS 需核对:', body.count('需核对'))
