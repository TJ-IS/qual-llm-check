# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
p = os.path.join(DIR, '73_三篇第二章文献综述逐段核对与批次五修改落盘记录.md')
text = io.open(p, encoding='utf-8').read()
subs = [
 ('用户要求逐段严格审计、回到原文挑选参考并模仿', '用户要求逐段严格核对、回到原文挑选参考并模仿'),
 ('综述节不设置带指引的预缺口列举；DSDL 综述节', '综述节不设置带指引的预缺口列举。DSDL 综述节'),
 ('两篇共享风险降低与效用保持的权衡前沿、掩蔽特征与噪声水平长串；DSDL 与 ACAA', '两篇共享风险降低与效用保持的权衡前沿、掩蔽特征与噪声水平长串。DSDL 与 ACAA'),
 ('34 基于上述缺口……、35 综合上述缺口……、36 针对上述缺口……', '34 基于上述缺口、35 综合上述缺口、36 针对上述缺口'),
 ('换言之，……', '换言之，'),
]
for old, new in subs:
    text = text.replace(old, new)
text = text.replace('；', '。')
text = text.replace('……', '')
text = text.replace('…', '')
io.open(p, 'w', encoding='utf-8', newline='').write(text)
print('done')