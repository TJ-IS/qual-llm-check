# -*- coding: utf-8 -*-
import io, glob, re
fs = glob.glob('15_*.md')
t = io.open(fs[0], encoding='utf-8').read()
# find final recommendation section
idx = t.find('最终推荐')
print('=== 最终推荐 位置:', idx)
print(t[idx-200:idx+3000] if idx>0 else t[-3000:])
