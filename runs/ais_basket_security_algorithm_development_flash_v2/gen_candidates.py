# -*- coding: utf-8 -*-
"""Generate the T6 (Q1-Q8) fulltext candidate list."""
import json, os, pickle

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"

BLOCKS = ["Q1_malware","Q2_intrusion_network","Q3_adversarial","Q4_phishing_auth","Q5_attacker_threat","Q6_content_manipulation","Q7_privacy_disclosure","Q8_threat_intel_vuln"]

with open(os.path.join(ROOT, "fulltext_scan_cache.pkl"), "rb") as fh:
    cache_key, masks = pickle.load(fh)
files, terms = cache_key
TERM_ID = {t: i for i, t in enumerate(terms)}

# rebuild block masks from the report's term lists (import from the test script would be cleaner, inline here)
from fulltext_recall_test import BLOCKS as ALL_BLOCKS  # reuse
block_mask = {}
for bname, tlist in ALL_BLOCKS.items():
    bm = 0
    for t in tlist:
        if t.lower() in TERM_ID:
            bm |= (1 << TERM_ID[t.lower()])
    block_mask[bname] = bm

mask = 0
for b in BLOCKS:
    mask |= block_mask[b]
hits = [i for i, m in enumerate(masks) if m & mask]

# write candidate list with title from frontmatter? simpler: file names
out = os.path.join(ROOT, "fulltext_candidates_T6_Q1-Q8.txt")
with open(out, "w", encoding="utf-8") as f:
    for i in hits:
        f.write(files[i] + "\n")
print(f"candidates: {len(hits)} -> {out}")
