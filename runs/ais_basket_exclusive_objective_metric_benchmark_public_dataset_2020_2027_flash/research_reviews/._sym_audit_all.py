# -*- coding: utf-8 -*-
import io, re, glob
# 1) papers full text (including references)
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
syms = {'\uff1a':'全角冒号','\uff1b':'全角分号','\u2014':'破折号','\u2013':'短横线','\u201c':'左双引','\u201d':'右双引','\u2018':'左单引','\u2019':'右单引','\u2026':'省略号','\u2192':'箭头',':':'半角冒号','\"':'半角双引',"'":'半角单引'}
print('== papers full text ==')
for k, f in files.items():
    t = io.open(f, encoding='utf-8').read()
    hits = {}
    for ch, n in syms.items():
        c = t.count(ch)
        if c:
            hits[n] = c
    print(k, hits or 'clean')
print()
print('== records 82-105 ==')
bad = 0
for fn in sorted(glob.glob('[89][0-9]_*.md') + glob.glob('9[0-9]_*.md') + glob.glob('10[0-5]_*.md')):
    t = io.open(fn, encoding='utf-8').read()
    hits = {}
    for ch, n in syms.items():
        c = t.count(ch)
        if c:
            hits[n] = c
    if hits:
        bad += 1
        print(fn, hits)
print('records bad:', bad)
