# -*- coding: utf-8 -*-
import io, unicodedata, collections
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
for n, fn in files.items():
    t = io.open(fn, encoding='utf-8').read()
    body = t.split('## 参考文献')[0]
    print('='*12, n, '='*12)
    cnt = collections.Counter()
    for ch in body:
        if ord(ch) > 127 and not ('\u4e00' <= ch <= '\u9fff'):
            cnt[(ch, unicodedata.name(ch, '?'))] += 1
    for (ch, name), c in sorted(cnt.items(), key=lambda x: -x[1]):
        print(f'  {ch!r} {name}: {c}')
