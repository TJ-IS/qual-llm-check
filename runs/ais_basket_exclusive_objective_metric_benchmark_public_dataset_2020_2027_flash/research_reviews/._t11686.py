# -*- coding: utf-8 -*-
import io
base = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all'
def sec(fn, start, end):
    t = io.open(base+'\\'+fn, encoding='utf-8').read()
    i = t.find(start); j = t.find(end, i+1)
    return t[i:j] if i>=0 else 'NOT FOUND: '+start
print('===== 11686 Practical Implications + Contributions =====')
print(sec('11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md','## Practical Implications and Contributions to the IS Knowledge Base','## Conclusion And Future Directions'))
