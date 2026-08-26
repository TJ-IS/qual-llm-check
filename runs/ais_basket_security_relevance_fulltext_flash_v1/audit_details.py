# -*- coding: utf-8 -*-
"""Detailed audit: classify M1-missed gold papers; check suspicious noise; 99-paper coverage."""
import json, os, re, csv

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"\s+", "", d).rstrip(".")
    return d

def norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", (t or "").lower())

gold = []
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        if o.get("security_include") is True:
            gold.append(o)
print("gold:", len(gold))

# CSV: doi -> rec, title -> rec
csv_by_doi = {}
csv_by_title = {}
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
        d = norm_doi(row.get("DOI"))
        if d:
            csv_by_doi.setdefault(d, row)
        t = norm_title(row.get("Title"))
        if t:
            csv_by_title.setdefault(t, row)

def find_csv(doi, title):
    if doi and doi in csv_by_doi:
        return csv_by_doi[doi]
    t = norm_title(title)
    if t in csv_by_title:
        return csv_by_title[t]
    return None

def load_list(path):
    with open(path, encoding="utf-8") as f:
        return {line.strip() for line in f if line.strip()}

m1_dois = set()
with open(os.path.join(OLD, "slr_metadata_candidates.txt"), encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 5 and parts[4]:
            m1_dois.add(norm_doi(parts[4]))

# 1) M1-missed gold: classify
lines = ["# 审计细节：M1 漏检金标准 25 篇分类 + 疑似误纳/误排检查\n"]
lines.append("## A. M1 漏检的金标准（25 篇）：分类\n")
missed = []
for g in gold:
    doi = norm_doi(g.get("doi"))
    if doi in m1_dois:
        continue
    rec = find_csv(doi, g.get("title"))
    in_csv = rec is not None
    missed.append((g, rec, doi, in_csv))

lines.append(f"共 {len(missed)} 篇；按『CSV 中是否有该文』区分：\n")
not_in_csv = [m for m in missed if not m[3]]
in_csv_no_hit = [m for m in missed if m[3]]
lines.append(f"### A1. 不在 CSV（元数据检索天然够不到，语料覆盖问题）：{len(not_in_csv)} 篇\n")
for g, rec, doi, _ in not_in_csv:
    lines.append(f"- {g['source_file']} | {g.get('title')} | doi={doi}")
    lines.append(f"  - 判定理由: {(g.get('security_relevance') or {}).get('reason_cn','')}")
lines.append(f"\n### A2. 在 CSV 但摘要/标题/关键词无词表命中（真漏词或摘要无攻防词）：{len(in_csv_no_hit)} 篇\n")
for g, rec, doi, _ in in_csv_no_hit:
    lines.append(f"- {g['source_file']} | {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')}")
    abs_ = (rec.get("Abstract") or "").replace("\n", " ")
    lines.append(f"  - 摘要前 250 字: {abs_[:250]}")
    lines.append(f"  - 关键词: {(rec.get('Author Keywords') or '')[:200]} | {(rec.get('Index Keywords') or '')[:200]}")
    lines.append(f"  - 判定理由: {(g.get('security_relevance') or {}).get('reason_cn','')}")

# 2) suspicious noise: M1-hit but gold-excluded, check decisions for a few known security titles
lines.append("\n## B. 噪声中疑似安全文献的判定复核（抽样）\n")
suspicious = ["Improving Phishing Reporting Using Security Gamification",
              "Hate Speech Detection on Online News Platforms",
              "Adversarial knowledge-sharing in a coopetitive environment",
              "On information technology and the safety of police officers",
              "Can bots help create knowledge?"]
dec_by_file = {}
with open(os.path.join(ROOT, "decisions.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        dec_by_file[o["source_file"]] = o
# find by title
for s in suspicious:
    for o in dec_by_file.values():
        if s.lower()[:50] in (o.get("title") or "").lower():
            sec = o.get("security_relevance") or {}
            lines.append(f"- {o.get('title')} | {o.get('year')} | {o.get('journal')}")
            lines.append(f"  - status={sec.get('status')} include={o.get('security_include')}")
            lines.append(f"  - reason: {sec.get('reason_cn','')}")
            lines.append(f"  - decision: {o.get('decision_reason_cn','')}")
            break

# 3) 99-paper coverage in gold
src2rec = {}
with open(os.path.join(OLD, "data_publicness_v3.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]
gold_files = {o["source_file"] for o in gold}
missing99 = [f for f in src2rec if f not in gold_files]
lines.append(f"\n## C. 99 篇（v2 算法开发金标准）在新金标准 388 中的覆盖：{99-len(missing99)}/99\n")
for f in missing99:
    o = dec_by_file.get(f)
    sec = (o or {}).get("security_relevance") or {}
    lines.append(f"- {src2rec[f]} | {f} | status={sec.get('status')} reason={sec.get('reason_cn','')}")

out = os.path.join(ROOT, "audit_details.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written")
