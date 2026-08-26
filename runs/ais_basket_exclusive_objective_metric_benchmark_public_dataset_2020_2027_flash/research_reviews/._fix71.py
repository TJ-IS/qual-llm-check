# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
oldp = os.path.join(DIR, '71_三篇第三至九章逐段审计与批次三修改落盘记录.md')
newp = os.path.join(DIR, '71_三篇第三至九章逐段核对与批次三修改落盘记录.md')
text = io.open(oldp, encoding='utf-8').read()
text = text.replace('# 71 号 34、35、36 第三至九章逐段审计与批次三修改落盘记录', '# 71 号 34、35、36 第三至九章逐段核对与批次三修改落盘记录')
text = text.replace('每写一段即回到原文逐句对比，分析落到每一句是否达到原文水平，并跨文献多次对照后再落盘。', '每写一段即回到原文做句子级对比，分析落到每一句是否达到原文水平，并跨文献多次对照后再落盘。')
io.open(newp, 'w', encoding='utf-8', newline='').write(text)
os.remove(oldp)
print('done')