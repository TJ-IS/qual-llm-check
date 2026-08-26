# -*- coding: utf-8 -*-
"""Generate recommended candidate list: head-8000 scope, Q1-Q8 + extra terms."""
import os, pickle

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"

with open(os.path.join(ROOT, "fulltext_scan_head_cache.pkl"), "rb") as fh:
    ck, masks = pickle.load(fh)
files, terms, head_chars = ck
TERM_ID = {t: i for i, t in enumerate(terms)}

allmask = 0
for t in terms:
    allmask |= (1 << TERM_ID[t])

hits = [i for i, m in enumerate(masks) if m & allmask]
out = os.path.join(ROOT, "fulltext_candidates_head8000_Q1-Q8_extra.txt")
with open(out, "w", encoding="utf-8") as f:
    for i in hits:
        f.write(files[i] + "\n")
print(f"candidates: {len(hits)} -> {out}")
