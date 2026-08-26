# -*- coding: utf-8 -*-
import io, re
f = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(f, encoding='utf-8').read()
disc = t[94592:99496]
out = io.open('._audit110_radar_disc.txt','w',encoding='utf-8').write(disc)
print(disc[:5200])
