# -*- coding: utf-8 -*-
import io, re
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    print('='*12, n, '全文（含参考文献）', '='*12)
    for ch, name in [("'",'half squote'),('·','middot'),('—','em'),('“','lq'),('”','rq'),('：','colon'),('；','semi'),('…','ellipsis'),('～','tilde'),('–','en')]:
        c = t.count(ch)
        if c:
            print(f'  {name}: {c}')
            for m in re.finditer(re.escape(ch), t):
                print('    ctx:', t[max(0,m.start()-40):m.end()+40].replace('\n',' '))
                if c > 8 and list(re.finditer(re.escape(ch), t)).index(m) >= 7:
                    print('    ... more')
                    break
