# -*- coding: utf-8 -*-
import io, re
t = io.open('._audit107_body34.txt', encoding='utf-8').read()
# locate section boundaries
heads = [(m.start(), m.group(0)) for m in re.finditer(r'^#{2,4} [^\n]+$', t, flags=re.M)]
def between(a, b):
    return t[a[0]:b[0] if b else len(t)]
pairs = []
for i,(p,h) in enumerate(heads):
    if h.startswith('### 2.3') or h.startswith('### 2.4') or h.startswith('### 2.5') or h.startswith('### 3.1') or h.startswith('### 3.2') or h.startswith('### 3.3'):
        pairs.append((p,h))
print([h for _,h in pairs])
out = io.open('._audit107_mid1.txt','w',encoding='utf-8')
start = pairs[0][0]; end = pairs[-1][0] + len(t[pairs[-1][0]:])
# end at next heading after 3.3
endpos = None
for p,h in heads:
    if p > pairs[-1][0] and h.startswith('## '):
        endpos = p; break
out.write(t[start:endpos])
out.close()
print('mid1 saved', endpos-start)
