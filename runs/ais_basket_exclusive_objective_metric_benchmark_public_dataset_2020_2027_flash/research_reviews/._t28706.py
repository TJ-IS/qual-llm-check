# -*- coding: utf-8 -*-
import io
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def sec(fn, start, end):
    t = io.open(base+'\\'+fn, encoding='utf-8').read()
    i = t.find(start); j = t.find(end, i+1)
    return t[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 28706 6 Contributions and Implications =====')
print(sec('28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md','6. Contributions and Implications','## 7. Conclusion'))
