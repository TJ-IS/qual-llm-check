# -*- coding: utf-8 -*-
import io, os, re
BASE = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
out = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d != '.git']
    for fn in sorted(files):
        if not fn.lower().endswith('.md'): continue
        if re.match(r'^\d+_', fn) or re.match(r'^[A-Z]_', fn) or fn == 'README.md':
            p = os.path.join(root, fn)
            text = io.open(p, encoding='utf-8', errors='ignore').read()
            body = text.split('## 参考文献')[0] if '## 参考文献' in text else text
            b = body.count('\u2014') + body.count('\u2015') + body.count('\u2013')
            q = body.count('\u201c') + body.count('\u201d') + body.count('\u2018') + body.count('\u2019')
            c = body.count('\uff1a')
            e = body.count('\u2026')
            rel = os.path.relpath(p, BASE)
            out.append('%s | 破:%d 引:%d 冒:%d 略:%d' % (rel, b, q, c, e))
io.open(os.path.join(BASE, '_allpaper_syms.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done', len(out))