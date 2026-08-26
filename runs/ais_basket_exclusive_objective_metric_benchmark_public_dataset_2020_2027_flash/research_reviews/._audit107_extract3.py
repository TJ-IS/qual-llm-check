# -*- coding: utf-8 -*-
import io, re
f = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(f, encoding='utf-8').read()
# find all heading-like lines with 'Intro' or 'intro'
for m in list(re.finditer(r'^#{1,4}\s*[^\n]*[Ii]ntroduction[^\n]*$', t, flags=re.M))[:5]:
    print(m.start(), repr(m.group(0)))
print('--- first 1200 chars ---')
print(t[:1200])
