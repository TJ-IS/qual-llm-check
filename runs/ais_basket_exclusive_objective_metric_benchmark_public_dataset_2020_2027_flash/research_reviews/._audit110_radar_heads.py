# -*- coding: utf-8 -*-
import io, re
f = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(f, encoding='utf-8').read()
# find Discussion and Conclusion headings
for m in re.finditer(r'^#{1,4}\s*[^\n]*(Discussion|Conclusion|CONCLUDING)[^\n]*$', t, flags=re.M):
    print(m.start(), repr(m.group(0)))
