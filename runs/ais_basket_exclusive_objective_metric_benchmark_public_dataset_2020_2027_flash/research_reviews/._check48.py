import re
fn = '48_三篇交叉一致性核对与引用术语口径记录.md'
t = open(fn, encoding='utf-8').read()
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
hits = [(w, len(re.findall(w, t))) for w in banned if w in t]
print('禁词:', hits if hits else '无')
syms = {'全角冒号：': t.count('：'), '中文分号；': t.count('；'), '破折号—': t.count('—'), '弯引号“': t.count('“'), '弯引号”': t.count('”')}
print('符号:', {k:v for k,v in syms.items() if v}, '（其余为零）' if all(v==0 for v in syms.values()) else '')
