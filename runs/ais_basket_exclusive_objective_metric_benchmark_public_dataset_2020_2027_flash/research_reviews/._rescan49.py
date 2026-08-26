# -*- coding: utf-8 -*-
import io, re
fname = '49_三篇句子级对照与表述强化_跨节回声消除记录.md'
t = io.open(fname, encoding='utf-8').read()
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
syms = {'：':'full-colon','；':'semi','—':'dash','“':'lquote','”':'rquote','‘':'lq','’':'rq'}
hits = {w: t.count(w) for w in banned if t.count(w)}
print('49 record banned:', hits if hits else 'none')
sh = {k: t.count(k) for k in syms if t.count(k)}
print('49 record symbols:', sh if sh else 'all zero')
print('49 placeholders:', len(re.findall(r'【占位', t)))
