# -*- coding: utf-8 -*-
"""Which 99 are missed by V5 (all terms, head) and what their head text looks like."""
import json, os, pickle

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"

def load(path):
    with open(path, "rb") as fh:
        ck, masks = pickle.load(fh)
    return ck, masks

ck_head, masks_head = load(os.path.join(ROOT, "fulltext_scan_head_cache.pkl"))
files, terms, _ = ck_head
TERM_ID = {t: i for i, t in enumerate(terms)}

src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]
rec99 = [i for i, f in enumerate(files) if f in src2rec]

allmask = 0
for t in terms:
    allmask |= (1 << TERM_ID[t])

missed = [i for i in rec99 if not (masks_head[i] & allmask)]
out_lines = [f"V5 missed: {len(missed)}"]
for i in missed:
    f = files[i]
    with open(os.path.join(CORPUS, f), encoding="utf-8", errors="ignore") as fh:
        head = fh.read(4000)
    # strip frontmatter
    body = head
    if head.startswith("---"):
        end = head.find("---", 3)
        if end != -1:
            body = head[end+3:]
    out_lines.append("="*100)
    out_lines.append(src2rec[f] + " | " + f)
    out_lines.append(body[:900].replace(chr(10), " "))

with open(os.path.join(ROOT, "v5_missed_details.txt"), "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print("written")
