# -*- coding: utf-8 -*-
"""Check a sample of 198xx/204xx files for the same philosophy-page content."""
import os, re
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
confim = "confim"
hits = []
for fn in os.listdir(CORPUS):
    if not fn.endswith(".md"): continue
    if not re.match(r"(198|204|206)\d\d_", fn): continue
    p = os.path.join(CORPUS, fn)
    with open(p, encoding="utf-8", errors="ignore") as f:
        head = f.read(3000)
    if confim in head.lower():
        hits.append(fn)
print("confim-content files among 198xx/204xx/206xx:", len(hits))
for h in sorted(hits):
    print("  ", h)
