# -*- coding: utf-8 -*-
import io
fn = '51_全文通读审计与表述强化_符号普查与定调句优化记录.md'
t = io.open(fn, encoding='utf-8').read()
reps = [
 ("# 51 号 全文通读审计与表述强化_符号普查与定调句优化记录",
  "# 51 号 全文通读核对与表述强化_符号普查与定调句优化记录"),
 ("做全文逐章通读审计，对全部特殊符号做类别普查",
  "做全文逐章通读核对，对全部特殊符号做类别普查"),
 ("例如 03 号审计记录含破折号 99 处",
  "例如 03 号旧稿记录含破折号 99 处"),
 ("## 2. 全文逐章通读审计",
  "## 2. 全文逐章通读核对"),
 ("审计方法。对三篇逐章通读",
  "核对方法。对三篇逐章通读"),
 ("覆盖引言、第二至九章与参考文献之外的正文；另对工作区全部 md 文档做符号普查",
  "覆盖引言、第二至九章与参考文献之外的正文，另对工作区全部 md 文档做符号普查"),
]
ok = True
for old, new in reps:
    c = t.count(old)
    if c != 1:
        print('FAIL count', c, '|', old[:30]); ok = False
    else:
        t = t.replace(old, new)
if ok:
    io.open(fn, 'w', encoding='utf-8', newline='').write(t)
    print('FIXED')
