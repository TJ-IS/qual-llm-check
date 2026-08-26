# -*- coding: utf-8 -*-
import io, os, re
roots = [
    r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews',
    r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\archive',
    r'E:\github\qual-llm-check-IS-utd\thesis_collection',
]
targets = {'破折号—': '—', '双破折号——': '——', '中文引号“': '“', '中文引号”': '”', '单引号‘': '‘', '单引号’': '’', '全角冒号：': '：', '全角分号；': '；', '省略号…': '…'}
rows = []
for root in roots:
    if not os.path.isdir(root): continue
    for dirpath, dirs, files in os.walk(root):
        for f in files:
            if not f.endswith('.md'): continue
            p = os.path.join(dirpath, f)
            try:
                t = io.open(p, encoding='utf-8').read()
            except Exception:
                continue
            counts = {k: t.count(ch) for k, ch in targets.items() if t.count(ch)}
            if counts:
                rows.append((sum(counts.values()), os.path.relpath(p, root), counts))
rows.sort(reverse=True)
for total, rel, counts in rows[:40]:
    print(f'{total:4d}  {rel[:70]}')
    for k, v in counts.items():
        print(f'       {k}: {v}')
