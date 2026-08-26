import re
fn = '48_三篇交叉一致性核对与引用术语口径记录.md'
t = open(fn, encoding='utf-8').read()
for m in re.finditer('：', t):
    s = max(0, m.start()-60); e = min(len(t), m.end()+60)
    print(repr(t[s:e]))
