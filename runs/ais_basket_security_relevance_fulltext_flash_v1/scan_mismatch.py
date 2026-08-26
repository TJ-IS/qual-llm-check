# -*- coding: utf-8 -*-
"""Scan fulltext corpus for content-mismatch: title keywords missing from body head."""
import os, re, json, unicodedata

CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
def norm(t):
    t = (t or "").lower()
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", t)

def title_words(title):
    words = re.findall(r"[a-z]{4,}", (title or "").lower())
    # drop common generic words
    stop = {"with","from","that","this","into","their","them","based","using","under","about","between","after","before","through","during","among","against","without","toward","within","across"}
    return [w for w in words if w not in stop][:6]

rows = []
for fn in os.listdir(CORPUS):
    if not fn.endswith(".md"):
        continue
    p = os.path.join(CORPUS, fn)
    with open(p, encoding="utf-8", errors="ignore") as f:
        txt = f.read(12000)
    m = re.search(r"title:\s*[\"']?(.*?)[\"']?\s*$", txt, re.M)
    title = m.group(1) if m else fn
    words = title_words(title)
    body = txt[500:]  # skip yaml+title area
    nbody = norm(body)
    miss = [w for w in words if w not in nbody]
    ratio = (len(words)-len(miss))/len(words) if words else 1
    if ratio == 0:  # none of the title words in body
        rows.append((fn, title[:90], 0))
    elif ratio <= 0.4:
        rows.append((fn, title[:90], ratio))
print("total checked:", len(os.listdir(CORPUS)))
print("zero-title-word-in-body:", len([r for r in rows if r[2]==0]))
print("low-ratio:", len([r for r in rows if 0<r[2]<=0.4]))
with open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1\corpus_mismatch_scan.txt","w",encoding="utf-8") as f:
    for fn, t, r in sorted(rows, key=lambda x:x[2]):
        f.write(f"{r:.2f}\t{fn}\t{t}\n")
print("written corpus_mismatch_scan.txt")
