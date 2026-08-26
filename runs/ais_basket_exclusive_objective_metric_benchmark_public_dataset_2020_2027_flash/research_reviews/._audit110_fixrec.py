# -*- coding: utf-8 -*-
import io, glob
f = glob.glob('110_*.md')[0]
t = io.open(f, encoding='utf-8').read()
t2 = t.replace('逐句对应', '句级对应')
io.open(f, 'w', encoding='utf-8', newline='').write(t2)
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
hits = {w: t2.count(w) for w in banned if w in t2}
syms = {c: t2.count(c) for c in ['：','；','—','“','”','‘','’','…','→'] if c in t2}
print('修正后禁词:', hits or '无')
print('全角符号:', syms or '全零')
