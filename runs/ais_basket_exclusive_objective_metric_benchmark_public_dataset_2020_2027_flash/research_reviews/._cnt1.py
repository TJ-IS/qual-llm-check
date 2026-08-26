# -*- coding: utf-8 -*-
import io, re, ast
with io.open('._apply_diff.py', encoding='utf-8') as f:
    src = f.read()
# 提取 edits 字典部分
m = re.search(r'edits = (\{.*?\n\})', src, re.S)
d = ast.literal_eval(m.group(1))
total = 0
for fn, lst in d.items():
    print(fn[:14], '替换数:', len(lst))
    total += len(lst)
print('合计:', total)
