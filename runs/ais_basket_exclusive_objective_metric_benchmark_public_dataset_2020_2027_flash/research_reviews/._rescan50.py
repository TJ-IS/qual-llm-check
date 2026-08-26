# -*- coding: utf-8 -*-
import io, re
t = io.open('50_第六章第七章_模板逐段对照与句子级优化记录.md', encoding='utf-8').read()
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
syms = {'：':'full-colon','；':'semi','—':'dash','“':'lquote','”':'rquote','‘':'lq','’':'rq'}
hits = {w: t.count(w) for w in banned if t.count(w)}
print('50 record banned:', hits if hits else 'none')
sh = {k: t.count(k) for k in syms if t.count(k)}
print('50 record symbols:', sh if sh else 'all zero')
print('Walls:', t.count('Walls'))
