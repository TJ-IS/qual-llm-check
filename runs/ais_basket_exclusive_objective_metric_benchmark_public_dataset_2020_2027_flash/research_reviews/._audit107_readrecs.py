# -*- coding: utf-8 -*-
import io, glob
for n in [15, 54, 91, 94, 100]:
    fs = glob.glob(f'{n}_*.md')
    if not fs: continue
    t = io.open(fs[0], encoding='utf-8').read()
    print('='*20, n, fs[0])
    print(t[:1500])
    print()
