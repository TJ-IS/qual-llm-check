# -*- coding: utf-8 -*-
"""Cross-check: mismatched corpus files vs gold 388 / M1 noise."""
import json, re

MISMATCH = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1\corpus_mismatch_scan.txt"
DEC = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1\decisions.jsonl"
mism = {}
with open(MISMATCH, encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 3:
            mism[parts[1]] = (float(parts[0]), parts[2])

gold = []
dec_by_file = {}
with open(DEC, encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        dec_by_file[o["source_file"]] = o
        if o.get("security_include") is True:
            gold.append(o["source_file"])
print("gold:", len(gold))
gold_mism = [g for g in gold if g in mism]
print("gold WITH mismatched fulltext:", len(gold_mism))
for g in gold_mism:
    print("  ", g, "|", mism[g][1])

# security-word titles among mismatch files (0.0 ratio)
sec_word = re.compile(r"phish|malware|hack|breach|attack|cyber|secur|fraud|privacy|spam|fake|bot|deepfake|misinform|adversarial|intrusion|exploit|risk", re.I)
print("\nMismatched files whose TITLE contains security words (should have been security if fulltext ok):")
for fn, (ratio, title) in sorted(mism.items()):
    if ratio <= 0.4 and sec_word.search(title):
        o = dec_by_file.get(fn)
        st = (o or {}).get("security_status")
        inc = (o or {}).get("security_include")
        print(f"  {fn} | ratio={ratio} | title={title[:80]} | status={st} include={inc}")
