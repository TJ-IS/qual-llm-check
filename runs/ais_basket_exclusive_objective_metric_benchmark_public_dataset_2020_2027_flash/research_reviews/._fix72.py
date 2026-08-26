# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
p = os.path.join(DIR, '72_三篇引言逐段对照第四轮与批次四修改落盘记录.md')
text = io.open(p, encoding='utf-8').read()
text = text.replace('与 RADAR 逐句对应', '与 RADAR 逐点对应')
text = text.replace('与其逐句对应', '与其逐点对应')
text = text.replace('；', '。')
io.open(p, 'w', encoding='utf-8', newline='').write(text)
print('done')