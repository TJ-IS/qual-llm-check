# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\69_35与36全文逐段对照_新发现十二处修改落盘记录.md'
t = open(p, encoding='utf-8').read()
old = 'DSDL 与 ACAA 的写作纪律是先承认既有研究的有效部分，再指出适用边界'
new = 'DSDL 与 ACAA 的表述原则是先承认既有研究的有效部分，再指出适用边界'
assert t.count(old) == 1
open(p, 'w', encoding='utf-8').write(t.replace(old, new))
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
syms = {'：':'全角冒号','；':'全角分号','—':'破折号','“':'引号','”':'引号','‘':'引号','’':'引号','…':'省略号','→':'箭头'}
hits = {w: t.count(w) for w in banned if t.count(w)}
sh = {n: t.count(c) for c, n in syms.items() if t.count(c)}
print('禁词', hits or '无')
print('符号', sh or '全零')
