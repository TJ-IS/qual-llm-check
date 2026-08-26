# -*- coding: utf-8 -*-
import io
fn = '52_第二章逐段对照与引言讨论贡献对应性核对记录.md'
t = io.open(fn, encoding='utf-8').read()
old = "经逐句核对均达模板水平"
new = "经句子级核对均达模板水平"
c = t.count(old)
print('count:', c)
if c == 1:
    io.open(fn, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('fixed')
