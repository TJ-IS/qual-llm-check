# -*- coding: utf-8 -*-
import io, re
fn = '51_全文通读审计与表述强化_符号普查与定调句优化记录.md'
t = io.open(fn, encoding='utf-8').read()
for m in re.finditer('审计', t):
    print('审计 ctx:', t[max(0,m.start()-25):m.end()+25].replace('\n',' '))
for m in re.finditer('；', t):
    print('分号 ctx:', t[max(0,m.start()-40):m.end()+40].replace('\n',' '))
