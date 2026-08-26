# -*- coding: utf-8 -*-
import io, glob, re
fs = glob.glob('15_*.md')
t = io.open(fs[0], encoding='utf-8').read()
print('len', len(t))
# list all section headers
for m in re.finditer(r'^#{1,3} .*$', t, flags=re.M):
    print(m.start(), m.group(0))
