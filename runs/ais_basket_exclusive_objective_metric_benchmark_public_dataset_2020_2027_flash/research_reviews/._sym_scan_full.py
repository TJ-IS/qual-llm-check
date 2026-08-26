# -*- coding: utf-8 -*-
import io, collections
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
syms = ['\uff1a','\uff1b','\u2014','\u2013','-','\u201c','\u201d','\u2018','\u2019','"',"'",'\u2026','\u2192','\u21d2','\uff5e','\u301c','\u00b7','\u2208','\u03b1','\u03a3','\u03b8','\u03c4','\u03b3','\u03ba','\u03c0','\u03c9','\u2264','\u2265','\u00d7','\u2212','\u0394','\u03bb','\u03c3','[',']','{','}','(',')','\uff08','\uff09','<','>','=','~']
for k, f in files.items():
    t = io.open(f, encoding='utf-8').read()
    body = t.split('\u300a\u53c2\u8003\u6587\u732e')[0] if '\u300a\u53c2\u8003\u6587\u732e' in t else t.split('## \u53c2\u8003\u6587\u732e')[0]
    cnt = collections.Counter()
    for ch in body:
        if ch in syms:
            cnt[ch] += 1
    print('====', k)
    for ch, n in cnt.most_common():
        print('  %r (U+%04X): %d' % (ch, ord(ch), n))
