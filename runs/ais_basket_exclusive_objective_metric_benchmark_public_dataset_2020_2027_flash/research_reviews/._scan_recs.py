# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
for fn in ['69_35与36全文逐段对照_新发现十二处修改落盘记录.md','70_35与36全文档长串重复扫描_批次二修改落盘记录.md']:
    t = open(base+fn, encoding='utf-8').read()
    banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
    syms = {'：':'全角冒号','；':'全角分号','—':'破折号','“':'引号','”':'引号','‘':'引号','’':'引号','…':'省略号','→':'箭头'}
    hits = {w: t.count(w) for w in banned if t.count(w)}
    sh = {n: t.count(c) for c, n in syms.items() if t.count(c)}
    print(fn[:12], '禁词', hits or '无', '符号', sh or '全零')
