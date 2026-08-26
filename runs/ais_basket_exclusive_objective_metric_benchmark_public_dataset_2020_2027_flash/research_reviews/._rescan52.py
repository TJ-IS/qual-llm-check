# -*- coding: utf-8 -*-
import io
t = io.open('52_第二章逐段对照与引言讨论贡献对应性核对记录.md', encoding='utf-8').read()
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
syms = {'：':'full-colon','；':'semi','—':'dash','“':'lquote','”':'rquote','‘':'lq','’':'rq'}
hits = {w: t.count(w) for w in banned if t.count(w)}
print('52 record banned:', hits if hits else 'none')
sh = {k: t.count(k) for k in syms if t.count(k)}
print('52 record symbols:', sh if sh else 'all zero')
