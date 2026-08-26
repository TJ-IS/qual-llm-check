# -*- coding: utf-8 -*-
import io, re
fn = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(fn, encoding='utf-8').read()
print('LEN', len(t))
for m in re.finditer(r'^(#{1,4}) .*$', t, re.M):
    print(m.group(0)[:100])
