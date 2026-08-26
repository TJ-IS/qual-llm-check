# -*- coding: utf-8 -*-
import io, re
f = r'E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md'
t = io.open(f, encoding='utf-8').read()
start = 2860
rest = t[start:]
m = re.search(r'\n## ', rest)
end = start + m.start() if m else len(t)
out = io.open('._audit107_radar_intro.txt', 'w', encoding='utf-8')
out.write(t[start:end])
out.close()
print('saved', end-start)
