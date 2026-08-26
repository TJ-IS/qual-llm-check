# -*- coding: utf-8 -*-
"""Audit v3 (final): title-first matching, DOI as fallback, full B-part classification."""
import json, os, re, csv, unicodedata

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"\s+", "", d).rstrip(".")
    d = d.replace("10.1016/i.", "10.1016/j.").replace("10.1016/i,", "10.1016/j.")
    d = d.replace(",", "/").rstrip("/)").rstrip(".")
    return d

def norm_title(t):
    t = (t or "").lower()
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", t)

def find_csv(doi, title, csv_by_doi, csv_by_title):
    t = norm_title(title)
    if t and t in csv_by_title:
        return csv_by_title[t]
    if doi and doi in csv_by_doi:
        return csv_by_doi[doi]
    return None

csv_by_doi, csv_by_title, csv_rows = {}, {}, []
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
        csv_rows.append(row)
        d = norm_doi(row.get("DOI"))
        if d: csv_by_doi.setdefault(d, row)
        t = norm_title(row.get("Title"))
        if t: csv_by_title.setdefault(t, row)

gold = []
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        if o.get("security_include") is True:
            gold.append(o)

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
            m1_dois.add(d); m1_records.append(parts)

rows = []
for g in gold:
    doi_raw = norm_doi(g.get("doi"))
    rec = find_csv(doi_raw, g.get("title"), csv_by_doi, csv_by_title)
    csv_doi = norm_doi(rec.get("DOI")) if rec else None
    m1 = (csv_doi in m1_dois) if csv_doi else (doi_raw in m1_dois)
    rows.append({"g": g, "rec": rec, "doi_raw": doi_raw, "csv_doi": csv_doi,
                 "m1": m1, "f2": g["source_file"] in f2, "f3": g["source_file"] in f3})

m1_hit = sum(1 for r in rows if r["m1"]); f2_hit = sum(1 for r in rows if r["f2"]); f3_hit = sum(1 for r in rows if r["f3"])
missed = [r for r in rows if not r["m1"]]

# decisions lookup
dec_by_file = {}
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line); dec_by_file[o["source_file"]] = o
title2file = {}
for o in dec_by_file.values():
    title2file.setdefault(norm_title(o.get("title")), o["source_file"])

# M1 noise records (CSV rows whose DOI in M1, not gold)
gold_dois = {r["csv_doi"] or r["doi_raw"] for r in rows}
m1_noise = [rec for rec in csv_rows if norm_doi(rec.get("DOI")) in m1_dois and norm_doi(rec.get("DOI")) not in gold_dois]
print("M1 noise records:", len(m1_noise))

strong_attack_title = re.compile(
    r"phish|malware|ransom|trojan|botnet|backdoor|spyware|hack|breach|intrusion|exploit|zero-day|"
    r"adversarial|adversary|malicious|cyberattack|cyber attack|injection|jailbreak|deepfake|dark web|darknet|"
    r"honeypot|bot detection|social bot|identity theft|insider threat|data leak|data exfil|poisoning|"
    r"covert|steganograph|snoop|attack|attacker|cyberharass|cyberbully|online fraud|financial fraud", re.I)

out = []
out.append("# 审计 v3（最终修正）：388 金标准 × 三层检索\n")
out.append("- 匹配通道：归一化标题 → CSV（主）；DOI（辅）。decisions.doi 来自全文库 md 头部，存在错配（如 28238 头部 DOI 是 Racial Bias 一文的），标题匹配可消除。")
out.append(f"- M1 候选：{len(m1_dois)} 个唯一 DOI（{len(m1_records)} 条记录）；F2：{len(f2)} 篇；F3：{len(f3)} 篇\n")
out.append("| 检索层 | 金标准召回 | 召回率 | 命中数 | 精度 |")
out.append("|---|---|---|---|---|")
for name, hit, total in [("M1 元数据", m1_hit, len(m1_dois)), ("F2 head-8000", f2_hit, len(f2)), ("F3 全文", f3_hit, len(f3))]:
    out.append(f"| {name} | {hit}/{len(gold)} | {hit/len(gold):.1%} | {total} | {hit/total:.1%} |")

# A: missed list
out.append(f"\n## A. M1 漏检（修正后 {len(missed)} 篇）\n")
for r in sorted(missed, key=lambda x: x["g"]["source_file"]):
    rec = r["rec"]
    if rec is None:
        out.append(f"- {r['g']['source_file']} | {r['g'].get('title')} | 无CSV匹配")
        out.append(f"  - F2={r['f2']} F3={r['f3']}")
        continue
    abs_ = (rec.get("Abstract") or "").replace("\n", " ")
    kw = ((rec.get("Author Keywords") or "") + " | " + (rec.get("Index Keywords") or ""))[:180]
    out.append(f"- {r['g']['source_file']} | {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')} | CSVdoi={r['csv_doi']}")
    out.append(f"  - F2={r['f2']} F3={r['f3']} | 摘要: {abs_[:180]}")
    out.append(f"  - 关键词: {kw}")

# B: noise classification
out.append(f"\n## B. M1 噪声（命中但金标准排除，{len(m1_noise)} 条）分类复核\n")
in_fulltext = [rec for rec in m1_noise if title2file.get(norm_title(rec.get("Title")))]
not_in_fulltext = [rec for rec in m1_noise if not title2file.get(norm_title(rec.get("Title")))]
out.append(f"- 不在全文库 13,909（无法判定，需全文后才可复核）：{len(not_in_fulltext)} 条")
out.append(f"- 在全文库且被金标准排除：{len(in_fulltext)} 条\n")

# B1: attack-word titles among in-fulltext noise
b1 = []
for rec in in_fulltext:
    if strong_attack_title.search(rec.get("Title") or ""):
        b1.append(rec)
out.append(f"### B1. 标题含强攻击词但被金标准排除（{len(b1)} 条）——最可能漏判，逐条列理由\n")
for rec in sorted(b1, key=lambda r: (r.get("Source title") or "", r.get("Title") or "")):
    sf = title2file[norm_title(rec.get("Title"))]
    o = dec_by_file[sf]; sec = o.get("security_relevance") or {}
    out.append(f"- {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')} | status={sec.get('status')}")
    out.append(f"  - reason: {str(sec.get('reason_cn') or o.get('decision_reason_cn') or '')[:260]}")

# B2: peripheral-context among in-fulltext noise (title contains any security-ish word)
periph = []
for rec in in_fulltext:
    sf = title2file[norm_title(rec.get("Title"))]
    o = dec_by_file[sf]; sec = o.get("security_relevance") or {}
    if sec.get("status") == "security_peripheral_context":
        periph.append((rec, o))
out.append(f"\n### B2. 金标准判 peripheral 且 M1 命中（{len(periph)} 条）——边界案例备查\n")
for rec, o in sorted(periph, key=lambda x: (x[0].get("Source title") or "", x[0].get("Title") or "")):
    sec = o.get("security_relevance") or {}
    out.append(f"- {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')}")
    out.append(f"  - reason: {str(sec.get('reason_cn') or '')[:220]}")

with open(os.path.join(ROOT, "audit_v3_final.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("M1 recall:", m1_hit, "/", len(gold), "| missed:", len(missed))
print("noise:", len(m1_noise), "| in_fulltext:", len(in_fulltext), "| not_in_fulltext:", len(not_in_fulltext))
print("B1:", len(b1), "| B2:", len(periph))
print("written audit_v3_final.md")
