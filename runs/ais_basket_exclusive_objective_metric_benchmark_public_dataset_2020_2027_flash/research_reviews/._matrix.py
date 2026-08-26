# -*- coding: utf-8 -*-
import io, sys, re, glob, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
for f in sorted(glob.glob(base + '[0-9][0-9]_*.md')):
    t = open(f, encoding='utf-8').read()
    m = re.match(r'# \d+ 号[^\n]*', t)
    title = m.group(0) if m else f
    # 范围行
    scope = ''
    for ln in t.split('\n')[:20]:
        if ln.startswith('- 范围'):
            scope = ln.strip()
            break
    print(os.path.basename(f)[:40], '|', title[:60])
    if scope: print('     ', scope[:110])
