# -*- coding: utf-8 -*-
"""Audit v2 (corrected): title-based matching, DOI mismatch fix, full B-part review."""
import json, os, re, csv, unicodedata

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"\s+", "", d).rstrip(".")
    # fix common OCR-ish typos found in corpus: i->j before .dss/.im, trailing /, parentheses
    d = d.replace("10.1016/i.", "10.1016/j.")
    d = d.replace("10.1016/i,", "10.1016/j.")
    d = d.replace(",", "/")
    d = d.rstrip("/)").rstrip(".")
    return d

def norm_title(t):
    t = (t or "").lower()
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", t)

def find_csv(doi, title, csv_by_doi, csv_by_title):
    if doi and doi in csv_by_doi:
        return csv_by_doi[doi]
    t = norm_title(title)
    if t in csv_by_title:
        return csv_by_title[t]
    return None

# ---- load CSV ----
csv_by_doi = {}
csv_by_title = {}
csv_rows = []
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
        csv_rows.append(row)
        d = norm_doi(row.get("DOI"))
        if d:
            csv_by_doi.setdefault(d, row)
        t = norm_title(row.get("Title"))
        if t:
            csv_by_title.setdefault(t, row)

# ---- load gold ----
gold = []
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        if o.get("security_include") is True:
            gold.append(o)
print("gold:", len(gold))

# ---- load retrieval sets ----
def load_list(path):
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

f2 = load_list(os.path.join(OLD, "fulltext_candidates_head8000_Q1-Q8_extra.txt"))
f3 = load_list(os.path.join(OLD, "fulltext_candidates_T6_Q1-Q8.txt"))

m1_dois = set()
m1_records = []
with open(os.path.join(OLD, "slr_metadata_candidates.txt"), encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 5 and parts[4]:
            d = norm_doi(parts[4])
            m1_dois.add(d)
            m1_records.append(parts)
print("M1 unique DOIs:", len(m1_dois), "records:", len(m1_records))

# ---- per gold: resolve CSV record (title-first), compute hits ----
rows = []
for g in gold:
    doi_raw = norm_doi(g.get("doi"))
    rec = find_csv(doi_raw, g.get("title"), csv_by_doi, csv_by_title)
    csv_doi = norm_doi(rec.get("DOI")) if rec else None
    m1 = (csv_doi in m1_dois) if csv_doi else (doi_raw in m1_dois)
    # doi mismatch flag
    doi_mismatch = bool(rec) and csv_doi != doi_raw
    rows.append({
        "g": g, "rec": rec, "doi_raw": doi_raw, "csv_doi": csv_doi,
        "m1": m1, "f2": g["source_file"] in f2, "f3": g["source_file"] in f3,
        "doi_mismatch": doi_mismatch,
    })

m1_hit = sum(1 for r in rows if r["m1"])
f2_hit = sum(1 for r in rows if r["f2"])
f3_hit = sum(1 for r in rows if r["f3"])
mism = [r for r in rows if r["doi_mismatch"]]
print("M1 recall:", m1_hit, "/", len(gold))
print("F2 recall:", f2_hit, "/", len(gold))
print("F3 recall:", f3_hit, "/", len(gold))
print("DOI mismatches within gold:", len(mism))

# missed by M1 (corrected)
missed = [r for r in rows if not r["m1"]]
print("M1 missed (corrected):", len(missed))

# ---- output ----
out = []
out.append("# 审计 v2（修正版）：388 金标准 × 三层检索（标题主通道匹配）\n")
out.append(f"- 修正内容：decisions.jsonl 的 doi 字段来自全文库 md 头部，存在 166 处与 CSV（按标题映射）不一致；本审计以『归一化标题→CSV→CSV DOI』为主通道，DOI 仅作辅助。")
out.append(f"- M1 候选：{len(m1_dois)} 个唯一 DOI（{len(m1_records)} 条记录）")
out.append(f"- F2 head-8000：{len(f2)} 篇；F3 全文：{len(f3)} 篇\n")
out.append("| 检索层 | 金标准召回 | 召回率 | 命中数 | 精度(命中∩金/命中) |")
out.append("|---|---|---|---|---|")
for name, hit, total in [("M1 元数据", m1_hit, len(m1_dois)),
                          ("F2 head-8000", f2_hit, len(f2)),
                          ("F3 全文", f3_hit, len(f3))]:
    out.append(f"| {name} | {hit}/{len(gold)} | {hit/len(gold):.1%} | {total} | {hit/total:.1%} |")

# DOI mismatch list
out.append(f"\n## 金标准 388 中 DOI 错配（decisions.doi ≠ CSV.doi，{len(mism)} 篇）\n")
for r in sorted(mism, key=lambda x: x["g"]["source_file"]):
    rec = r["rec"]
    out.append(f"- {r['g']['source_file']} | {rec.get('Title')}")
    out.append(f"  - decisions.doi={r['doi_raw']} → CSV.doi={r['csv_doi']} | M1命中={r['m1']}")

# missed list with classification
out.append(f"\n## M1 漏检（修正后 {len(missed)} 篇）\n")
for r in sorted(missed, key=lambda x: x["g"]["source_file"]):
    rec = r["rec"]
    if rec is None:
        cls = "CSV无匹配记录"
    else:
        abs_ = (rec.get("Abstract") or "").replace("\n", " ")
        cls = "摘要无词表命中(全文命中)" if r["f3"] else "全文也未命中"
    out.append(f"- {r['g']['source_file']} | {rec.get('Title') if rec else r['g'].get('title')} | {rec.get('Year') if rec else '?'} | {rec.get('Source title') if rec else '?'}")
    out.append(f"  - 分类: {cls} | F2={r['f2']} F3={r['f3']}")
    if rec:
        out.append(f"  - 摘要前200字: {abs_[:200]}")

# ---- B: full suspicious-noise review ----
# M1-hit but gold-excluded records
gold_keys = {norm_title(r["g"].get("title")) for r in rows}
m1_noise = []
for rec in csv_rows:
    t = norm_title(rec.get("Title"))
    if not t or t in gold_keys:
        continue
    if norm_doi(rec.get("DOI")) in m1_dois:
        m1_noise.append(rec)
print("M1 noise records:", len(m1_noise))

# strong security keywords in title/abstract to flag suspicious noise
strong = re.compile(
    r"phish|malware|ransom|virus|trojan|botnet|backdoor|spyware|hack|breach|intrusion|exploit|"
    r"adversarial|adversary|malicious|maliciou|cyber|cybersecurity|cyber security|security attack|"
    r"attack|attacker|zero-day|injection|jailbreak|prompt injection|deepfake|fake news|misinform|"
    r"disinform|identity theft|account takeover|data leak|data exfil|insider threat|dark web|darknet|"
    r"honeypot|fraud|fraudulent|deception|deceit|spam|shilling|bot detection|social bot|phishing|"
    r"privacy attack|re-identif|de-identif|k-anonym|sanitiz|poisoning|covert|steganograph|snoop",
    re.I)

susp = []
for rec in m1_noise:
    blob = (rec.get("Title") or "") + " " + (rec.get("Abstract") or "")[:600]
    if strong.search(blob):
        susp.append(rec)
print("suspicious noise:", len(susp))

# decisions lookup for reasons
dec_by_file = {}
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        dec_by_file[o["source_file"]] = o

# map CSV rec -> source_file via title
title2file = {}
for o in dec_by_file.values():
    title2file.setdefault(norm_title(o.get("title")), o["source_file"])

out.append(f"\n## B 完整复核：M1 命中但金标准排除的疑似安全文献（{len(susp)} 条）\n")
out.append("> 判定标准：标题或摘要前600字命中强安全词。以下逐条给出金标准判定理由，供判断是否漏判。\n")
for rec in sorted(susp, key=lambda r: (r.get("Source title") or "", r.get("Title") or "")):
    t = norm_title(rec.get("Title"))
    sf = title2file.get(t)
    o = dec_by_file.get(sf) if sf else None
    sec = (o or {}).get("security_relevance") or {}
    reason = sec.get("reason_cn") or (o or {}).get("decision_reason_cn") or "（无判定记录）"
    status = sec.get("status") or "?"
    out.append(f"- {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')} | status={status}")
    out.append(f"  - reason: {str(reason)[:300]}")

with open(os.path.join(ROOT, "audit_v2_corrected.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("written audit_v2_corrected.md")
