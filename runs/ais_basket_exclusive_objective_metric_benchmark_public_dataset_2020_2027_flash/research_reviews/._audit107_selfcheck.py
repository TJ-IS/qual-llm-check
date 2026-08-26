# -*- coding: utf-8 -*-
import io
t = io.open('107_三篇全文独立复读审计与微修_记录.md', encoding='utf-8').read()
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
hits = {w: t.count(w) for w in banned if w in t}
syms = {c: t.count(c) for c in ['：','；','—','“','”','‘','’','…','→'] if c in t}
print('禁词:', hits or '无')
print('全角符号:', syms or '全零')
