# -*- coding: utf-8 -*-
import io, re
t = io.open('._audit107_body34.txt', encoding='utf-8').read()
heads = [(m.start(), m.group(0)) for m in re.finditer(r'^#{2,4} [^\n]+$', t, flags=re.M)]
st = en = None
for p,h in heads:
    if h.startswith('### 5.4'): st = p
    if h.startswith('### 7.4'):
        en = p; break
out = io.open('._audit107_mid2.txt','w',encoding='utf-8')
out.write(t[st:en])
out.close()
print('mid2 saved', en-st)
