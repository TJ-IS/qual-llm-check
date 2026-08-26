# -*- coding: utf-8 -*-
import io
with io.open('39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md', encoding='utf-8') as f:
    t = f.read()
print('总字符数:', len(t))
print('='*30)
print(t[:6000])
