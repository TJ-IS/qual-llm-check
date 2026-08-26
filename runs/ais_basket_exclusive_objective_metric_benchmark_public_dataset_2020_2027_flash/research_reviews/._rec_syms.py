# -*- coding: utf-8 -*-
import io, glob, re
for fn in sorted(glob.glob('[89][0-9]_*.md') + glob.glob('9[0-9]_*.md') + glob.glob('10[0-5]_*.md')):
    t = io.open(fn, encoding='utf-8').read()
    for ch in [':', "'", '\u2019']:
        for m in re.finditer(re.escape(ch), t):
            start = max(0, m.start()-30)
            end = min(len(t), m.end()+30)
            print(fn, repr(ch), '...' + t[start:end].replace(chr(10),' ') + '...')
