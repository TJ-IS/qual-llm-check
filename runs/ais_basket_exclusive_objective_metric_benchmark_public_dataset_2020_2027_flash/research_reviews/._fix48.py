fn = '48_三篇交叉一致性核对与引用术语口径记录.md'
t = open(fn, encoding='utf-8').read()
old = '现于其后新增一句：Yang 等（2023b）'
new = '现于其后新增一句，Yang 等（2023b）'
assert t.count(old) == 1
t = t.replace(old, new)
open(fn,'w',encoding='utf-8',newline='').write(t)
print('fixed')
# recheck
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
hits = [w for w in banned if w in t]
syms = {k: t.count(k) for k in ['：','；','—','“','”']}
print('禁词:', hits if hits else '无', '| 符号:', {k:v for k,v in syms.items() if v} or '全零')
