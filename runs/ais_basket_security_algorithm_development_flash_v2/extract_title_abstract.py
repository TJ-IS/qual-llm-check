# -*- coding: utf-8 -*-
"""Extract title + abstract from each fulltext md; cache as pickle; spot-check quality."""
import os, pickle, re, json, random

CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
OUT_CACHE = os.path.join(ROOT, "title_abstract_cache.pkl")

# abstract markers: allow spaces/dots between letters (e.g., "a b s t r a c t", "A B S T R A C T")
ABS_RE = re.compile(r"(?i)a[\.\s]*b[\.\s]*s[\.\s]*t[\.\s]*r[\.\s]*a[\.\s]*c[\.\s]*t")
# section cut markers (case-insensitive, may have ## prefix)
CUT_RE = re.compile(r"(?i)(\n\s*#{1,3}\s*)?(key\s*words?|introduction|1\.\s+intro|highlights|©|references?|a r t i c l e  i n f o|article info)")

def get_title(meta, text):
    t = ""
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', meta, re.M)
    if m:
        t = m.group(1)
    if not t:
        m = re.search(r'(?m)^#\s+(.+?)\s*$', text)
        if m:
            t = m.group(1)
    return t.strip()

def get_abstract(text):
    m = ABS_RE.search(text)
    if not m:
        return ""
    seg = text[m.end():]
    # cut at first section marker after abstract
    c = CUT_RE.search(seg)
    if c:
        seg = seg[:c.start()]
    seg = re.sub(r"\s+", " ", seg).strip()
    return seg[:2500]

def parse_one(f):
    path = os.path.join(CORPUS, f)
    with open(path, encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    meta = ""
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            meta = raw[:end]
            body = raw[end+4:]
    title = get_title(meta, body)
    abstract = get_abstract(body)
    return title, abstract

files = sorted(f for f in os.listdir(CORPUS) if f.endswith(".md"))
title_abstract = {}
for f in files:
    title, abstract = parse_one(f)
    title_abstract[f] = (title, abstract)

with open(OUT_CACHE, "wb") as fh:
    pickle.dump(title_abstract, fh)

# stats
empty_abs = [f for f, (t, a) in title_abstract.items() if not a]
print(f"total={len(files)} empty_abstract={len(empty_abs)}")
# spot check 8 files
for f in random.sample(files, 8):
    t, a = title_abstract[f]
    print("="*90)
    print(f)
    print("TITLE:", t[:120])
    print("ABS:", a[:300])

# 99-paper abstract availability
src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as fh:
    for line in fh:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]
missing99 = [f for f in src2rec if not title_abstract[f][1]]
print("\n99 papers with empty abstract:", len(missing99))
for f in missing99:
    print("-", src2rec[f], f)
