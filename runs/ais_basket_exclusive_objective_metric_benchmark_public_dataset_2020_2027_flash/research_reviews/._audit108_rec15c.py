# -*- coding: utf-8 -*-
import io, glob
fs = glob.glob('15_*.md')
t = io.open(fs[0], encoding='utf-8').read()
print(t[12083:])
