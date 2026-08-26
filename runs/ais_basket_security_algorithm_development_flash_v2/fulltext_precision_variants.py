# -*- coding: utf-8 -*-
"""Precision variants v2: head-8000 scope, extras (collusion etc.), vs full baseline."""
import json, os, pickle

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"

def load(path):
    with open(path, "rb") as fh:
        ck, masks = pickle.load(fh)
    return ck, masks

ck_head, masks_head = load(os.path.join(ROOT, "fulltext_scan_head_cache.pkl"))
files_head, terms_head, head_chars = ck_head
ck_full, masks_full = load(os.path.join(ROOT, "fulltext_scan_cache.pkl"))
files_full, terms_full = ck_full
assert files_head == files_full
files = files_head
N = len(files)
TERM_ID = {t: i for i, t in enumerate(terms_head)}

src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]
rec99 = [i for i, f in enumerate(files) if f in src2rec]
rec99_set = set(rec99)

multi = [t for t in terms_head if " " in t]
strong_singles = ["malware","ransomware","trojan","botnet","keylogger","spyware","backdoor","worm",
                  "steganography","adversarial","adversary","attacker","hacker","malicious","phishing",
                  "cyberbullying","deception","spoof","deceptive","fraudulent","snooper","masquerade",
                  "collusion"]
extra_terms = [t for t in terms_head if t in ("collusion","ballot stuffing","badmouthing","identity fraud","impersonation attack")]

def mask_of(tset):
    m = 0
    for t in tset:
        if t in TERM_ID:
            m |= (1 << TERM_ID[t])
    return m

V1_terms = multi
V2_terms = multi + [t for t in strong_singles if t in ("malware","ransomware","trojan","botnet","keylogger","spyware","backdoor","worm","steganography")]
V3_terms = multi + strong_singles
V5a_terms = terms_head  # all incl extras
V5b_terms = [t for t in terms_head if t not in extra_terms]  # all except extras

def stats(tset, masks):
    m = mask_of(tset)
    hits = [i for i in range(N) if masks[i] & m]
    h99 = [i for i in hits if i in rec99_set]
    return len(h99), len(hits)

variants = [
    ("V1 短语only-head8000", V1_terms, masks_head),
    ("V2 短语+恶意代码单数-head8000", V2_terms, masks_head),
    ("V3 短语+强攻击单数(含collusion)-head8000", V3_terms, masks_head),
    ("V5a Q1-Q8全词块-head8000(不含extra)", V5b_terms, masks_head),
    ("V5b Q1-Q8+extra-head8000(推荐主用)", V5a_terms, masks_head),
    ("V6 Q1-Q8全词块-full(基线)", terms_full, masks_full),
]

lines = ["# 检索精度增强 v2：head=标题+摘要+引言前8000字符；full=全文\n"]
lines.append("| 变体 | 99命中 | 召回率 | 语料命中 | 命中密度(99/命中) |")
lines.append("|---|---|---|---|---|")
for name, tset, masks in variants:
    h99, htot = stats(tset, masks)
    dens = h99 / htot if htot else 0
    lines.append(f"| {name} | {h99}/99 | {h99/99:.1%} | {htot} | {dens:.2%} |")

# V5b missed list
m5 = mask_of(V5a_terms)
missed = [i for i in rec99 if not (masks_head[i] & m5)]
lines.append(f"\n## V5b（推荐主用）head8000 漏掉的 99 篇：{len(missed)} 篇\n")
for i in missed:
    f = files[i]
    catch = [t for t in terms_full if t not in terms_head and (masks_full[i] & (1 << TERM_ID[t] if t in TERM_ID else 0))]
    lines.append(f"- {src2rec[f]} | {f}")

# collusion noise check: how many non-99 docs hit collusion in head
cm = 1 << TERM_ID["collusion"] if "collusion" in TERM_ID else 0
coll_hits = [i for i in range(N) if masks_head[i] & cm]
coll_non99 = [i for i in coll_hits if i not in rec99_set]
lines.append(f"\n## 补充词噪声检查（head8000）\n")
lines.append(f"- 'collusion' 命中 {len(coll_hits)} 篇（其中 99 篇 {len([i for i in coll_hits if i in rec99_set])}），非99样本：")
for i in coll_non99[:12]:
    lines.append(f"  - {files[i]}")

out = os.path.join(ROOT, "fulltext_precision_analysis.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written", out)

