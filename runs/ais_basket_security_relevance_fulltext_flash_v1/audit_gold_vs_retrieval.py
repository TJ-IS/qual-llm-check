# -*- coding: utf-8 -*-
"""Audit: fulltext-screened gold standard (388) vs retrieval layers (M1/F2/F3)."""
import json, os, re, csv

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"\s+", "", d).rstrip(".")
    return d

# gold standard
gold = []
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        if o.get("security_include") is True:
            gold.append(o)
print("gold:", len(gold))

# load retrieval candidate sets
def load_list(path):
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

f2 = load_list(os.path.join(OLD, "fulltext_candidates_head8000_Q1-Q8_extra.txt"))
f3 = load_list(os.path.join(OLD, "fulltext_candidates_T6_Q1-Q8.txt"))

# M1 metadata candidates (DOI set) from slr_metadata_candidates.txt (cols: idx,title,year,journal,doi)
m1_dois = set()
m1_by_doi = {}
with open(os.path.join(OLD, "slr_metadata_candidates.txt"), encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 5 and parts[4]:
            d = norm_doi(parts[4])
            m1_dois.add(d)
            m1_by_doi.setdefault(d, []).append(line)
print("M1 candidates:", len(m1_dois))

# CSV records for reverse mapping (doi -> title/year/journal) for missed-by-M1 analysis
csv_rec = {}
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
        d = norm_doi(row.get("DOI"))
        if d:
            csv_rec.setdefault(d, row)

# per gold paper: hit status for each layer
report = []
report.append("# 金标准（全库全文筛选 388 篇）× 三层检索：对比审计\n")
report.append(f"- 金标准：`ais_basket_security_relevance_fulltext_flash_v1` security_include=true，{len(gold)} 篇（deepseek-v4-flash 全文判定，13,909 篇全量，0 失败）")
report.append(f"- M1 元数据检索（Title+Abstract+Keywords）：{len(m1_dois)} 条")
report.append(f"- F2 head-8000 全文检索：{len(f2)} 篇")
report.append(f"- F3 全文检索：{len(f3)} 篇\n")

def stats_for(key):
    hit = sum(1 for g in gold if key(g))
    return hit, len(gold)

rows = []
for g in gold:
    doi = norm_doi(g.get("doi"))
    m1 = doi in m1_dois
    f2h = g["source_file"] in f2
    f3h = g["source_file"] in f3
    rows.append((g, doi, m1, f2h, f3h))

m1_hit = sum(1 for _, _, m1, _, _ in rows if m1)
f2_hit = sum(1 for _, _, _, f2h, _ in rows if f2h)
f3_hit = sum(1 for _, _, _, _, f3h in rows if f3h)
report.append("| 检索层 | 金标准召回 | 召回率 | 命中数 | 对金标准的精度(命中∩金/命中) |")
report.append("|---|---|---|---|---|")
for name, hit, total in [("M1 元数据", m1_hit, len(m1_dois)),
                          ("F2 head-8000", f2_hit, len(f2)),
                          ("F3 全文", f3_hit, len(f3))]:
    prec = hit / total if total else 0
    report.append(f"| {name} | {hit}/{len(gold)} | {hit/len(gold):.1%} | {total} | {prec:.1%} |")

# missed by M1
missed_m1 = [r for r in rows if not r[2]]
report.append(f"\n## M1 漏检的金标准（{len(missed_m1)} 篇）\n")
for g, doi, m1, f2h, f3h in sorted(missed_m1, key=lambda r: r[0]["source_file"]):
    rec = csv_rec.get(doi)
    title = rec["Title"] if rec else g.get("title")
    report.append(f"- {g['source_file']} | {title}")
    report.append(f"  - F2命中={f2h} F3命中={f3h} | 摘要前180字: {(rec['Abstract'][:180].replace(chr(10),' ') if rec else '无CSV记录')}")

# noise samples: M1 hits not in gold (sample 25 by journal variety)
m1_noise = []
for d in m1_dois:
    if d not in {r[1] for r in rows}:
        rec = csv_rec.get(d)
        if rec:
            m1_noise.append(rec)
report.append(f"\n## M1 命中但未通过金标准（噪声，{len(m1_noise)} 条）抽样 25 条\n")
for rec in m1_noise[:25]:
    report.append(f"- {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')}")

# summary per status among M1 noise? optional: sample reasons from decisions for a few
out = os.path.join(ROOT, "audit_gold_vs_retrieval.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("written", out)
