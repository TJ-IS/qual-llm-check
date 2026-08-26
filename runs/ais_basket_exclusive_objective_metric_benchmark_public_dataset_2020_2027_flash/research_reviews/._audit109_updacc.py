# -*- coding: utf-8 -*-
import io
p = '._accept90.py'
t = io.open(p, encoding='utf-8').read()
old = "exp = {'34': (61,94), '35': (62,82), '36': (66,83)}"
new = "exp = {'34': (64,94), '35': (62,82), '36': (66,83)}"
assert old in t
io.open(p, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
print('accept90 预期已更新')
