# -*- coding: utf-8 -*-
import io, re
f = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(f, encoding='utf-8').read()
m = re.search(r'#+\s*Introduction\s*(.*?)(?:\n#+\s*2|\n#+\s*Theory|\n#+\s*Related|\n#+\s*Background)', t, flags=re.S|re.I)
out = io.open('._audit107_radar_intro.txt', 'w', encoding='utf-8')
out.write(m.group(1).strip() if m else t[:3000])
out.close()
print('saved', len(m.group(1)) if m else 0)
