# -*- coding: utf-8 -*-
import io, re
out = io.open('_upd_chk.txt','w',encoding='utf-8')
for f in ['65_34的25节_句子级对照与跨文献对比记录.md','66_三篇全文逐段严格审计_符号纪律与表述力对标原文.md','67_35引言逐句严格审计记录.md','68_36引言逐句严格审计记录.md']:
    t = io.open(f, encoding='utf-8').read()
    out.write('### ' + f + '\n')
    for pat in [r'状态。[^\n]*', r'实际落盘待用户确认。', r'验收结果（模拟）', r'更新本记录状态', r'待用户确认落盘[^\n]*']:
        out.write(pat + ' :: ' + str(re.findall(pat, t)) + '\n')
    out.write('\n')
out.close()
