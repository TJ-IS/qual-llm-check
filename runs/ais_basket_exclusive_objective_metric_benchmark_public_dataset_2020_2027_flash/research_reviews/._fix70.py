# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\70_35与36全文档长串重复扫描_批次二修改落盘记录.md'
t = open(p, encoding='utf-8').read()
i = t.find('逐句')
print('位置', i, '...', t[max(0,i-60):i+40])
t2 = t.replace('回到 RADAR、ARText、DSDL、ACAA 模板原文与 52 号记录确立的引言讨论贡献对应惯例逐句对照', '回到 RADAR、ARText、DSDL、ACAA 模板原文与 52 号记录确立的引言讨论贡献对应惯例做句子级对照')
open(p, 'w', encoding='utf-8').write(t2)
banned = ['旗舰','不可修改','外部层','只能做','裸','冲突','审计','逐句','写作纪律','病毒库','弹窗','重跑']
syms = {'：':'全角冒号','；':'全角分号','—':'破折号','“':'引号','”':'引号','‘':'引号','’':'引号','…':'省略号','→':'箭头'}
print('禁词', {w: t2.count(w) for w in banned if t2.count(w)} or '无')
print('符号', {n: t2.count(c) for c, n in syms.items() if t2.count(c)} or '全零')
