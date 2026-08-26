# -*- coding: utf-8 -*-
import io
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def sec(fn, start, end):
    t = io.open(base+'\\'+fn, encoding='utf-8').read()
    i = t.find(start); j = t.find(end, i+1)
    return t[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 25465 Conclusions =====')
print(sec('25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md','## Conclusions','## Notes'))
