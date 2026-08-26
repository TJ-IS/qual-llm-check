# -*- coding: utf-8 -*-
"""Head-scope (title/abstract/intro) scan with same 183 terms; cache separate."""
import json, os, pickle, time

CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
HEAD_CHARS = 8000

from fulltext_recall_test import BLOCKS

EXTRA_TERMS = ["collusion", "ballot stuffing", "badmouthing", "identity fraud", "impersonation attack"]

files = sorted(f for f in os.listdir(CORPUS) if f.endswith(".md"))
terms = []
for bname, tlist in BLOCKS.items():
    for t in tlist:
        terms.append((bname, t.lower()))
for t in EXTRA_TERMS:
    terms.append(("Q_extra", t.lower()))
TERM_ID = {(bn, t): i for i, (bn, t) in enumerate(terms)}

CACHE = os.path.join(ROOT, "fulltext_scan_head_cache.pkl")
cache_key = (files, [t for (_, t) in terms], HEAD_CHARS)
if os.path.exists(CACHE):
    with open(CACHE, "rb") as fh:
        ck, masks = pickle.load(fh)
    if ck != cache_key:
        masks = None
else:
    masks = None

if masks is None:
    t0 = time.time()
    masks = [0] * len(files)
    for i, f in enumerate(files):
        with open(os.path.join(CORPUS, f), encoding="utf-8", errors="ignore") as fh:
            txt = fh.read(HEAD_CHARS + 2000).lower()
        txt = txt[:HEAD_CHARS]
        m = 0
        for j, (_, t) in enumerate(terms):
            if t in txt:
                m |= (1 << j)
        masks[i] = m
    with open(CACHE, "wb") as fh:
        pickle.dump((cache_key, masks), fh)
    print(f"head scan done {time.time()-t0:.0f}s files={len(files)}")
else:
    print("head cache loaded")

