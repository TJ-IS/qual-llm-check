# -*- coding: utf-8 -*-
import io
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def sec(fn, start, end):
    t = io.open(base+'\\'+fn, encoding='utf-8').read()
    i = t.find(start); j = t.find(end, i+1)
    return t[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 16409 6 Contributions and Implications =====')
print(sec('16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md','6. Contributions and Implications','## 7. Conclusion'))
