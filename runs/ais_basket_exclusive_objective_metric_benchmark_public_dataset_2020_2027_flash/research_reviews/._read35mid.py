# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
t = open(base+'_ch3end_35.txt', encoding='utf-8').read()
i = t.find('### 3.5 方法论挑战')
j = t.find('### 7.4 实践启示')
print(t[i:j])
