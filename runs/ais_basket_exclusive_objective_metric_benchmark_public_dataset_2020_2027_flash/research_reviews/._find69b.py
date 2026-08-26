# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
p = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\69_35与36全文逐段对照_新发现十二处修改落盘记录.md'
t = open(p, encoding='utf-8').read()
i = t.find('写作纪律')
print('index', i)
print(repr(t[i-30:i+30]))
