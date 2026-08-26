# -*- coding: utf-8 -*-
import io, re
fn = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(fn, encoding='utf-8').read()
i = t.find('## Discussion')
j = t.find('## Conclusion, Limitations, and Future Directions')
print(t[i:j])
