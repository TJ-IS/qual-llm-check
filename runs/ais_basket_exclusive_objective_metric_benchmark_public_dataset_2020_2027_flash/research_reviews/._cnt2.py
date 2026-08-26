# -*- coding: utf-8 -*-
import io
for fn in ['._scan_result.txt', '._scan_result2.txt']:
    with io.open(fn, encoding='utf-8') as f:
        t = f.read()
    print(fn, 'R= 行数:', t.count('R='))
