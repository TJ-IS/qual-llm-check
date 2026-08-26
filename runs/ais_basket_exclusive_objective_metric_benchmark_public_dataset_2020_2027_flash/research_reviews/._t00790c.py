# -*- coding: utf-8 -*-
import io
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def sec(fn, start, end):
    t = io.open(base+'\\'+fn, encoding='utf-8').read()
    i = t.find(start); j = t.find(end, i+1)
    return t[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 00790 5 Conclusion =====')
print(sec('00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md','## 5 Conclusion','## References'))
