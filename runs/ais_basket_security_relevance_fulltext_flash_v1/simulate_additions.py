# -*- coding: utf-8 -*-
"""Keyword-addition simulation for M1 recall improvement."""
import json, os, re, csv, unicodedata

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_relevance_fulltext_flash_v1\output_v1"
OLD = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"

def norm_doi(d):
    d=(d or "").strip().lower(); d=re.sub(r"\s+","",d).rstrip(".")
    d=d.replace("10.1016/i.","10.1016/j.").replace("10.1016/i,","10.1016/j.")
    d=d.replace(",","/").rstrip("/)").rstrip("."); return d
def norm_title(t):
    t=(t or "").lower(); t=unicodedata.normalize("NFKD",t).encode("ascii","ignore").decode()
    return re.sub(r"[^a-z0-9]+","",t)

csv_by_doi,csv_by_title={},{}
csv_rows=[]
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
        csv_rows.append(row)
        d=norm_doi(row.get("DOI"))
        if d: csv_by_doi.setdefault(d,row)
        t=norm_title(row.get("Title"))
        if t: csv_by_title.setdefault(t,row)

def find_csv(doi,title):
    t=norm_title(title)
    if t in csv_by_title: return csv_by_title[t]
    if doi in csv_by_doi: return csv_by_doi[doi]
    return None

gold=[]
with open(os.path.join(ROOT,"decisions.jsonl"),encoding="utf-8") as f:
    for line in f:
        o=json.loads(line)
        if o.get("security_include") is True: gold.append(o)

m1_dois=set()
with open(os.path.join(OLD,"slr_metadata_candidates.txt"),encoding="utf-8") as f:
    for line in f:
        p=line.rstrip("\n").split("\t")
        if len(p)>=5 and p[4]: m1_dois.add(norm_doi(p[4]))

# candidate additions: words that would have caught missed papers (from missed23 analysis + security lexicon)
additions = {
 "doxing": ["doxing"],
 "internet aggression": ["aggression"],
 "griefing": ["griefing"],
 "flaming": ["flaming"],
 "cyberharassment": ["cyberharass"],
 "piracy/drm/copyright": ["piracy","pirated","drm","copyright","rights management"],
 "forensics": ["forensic","forensics"],
 "audit(ing)": ["audit","auditing","edp audit","computer audit"],
 "corruption": ["corruption","bribery","bribe"],
 "abuse (computer/malicious)": ["computer abuse","malicious abuse"],
 "solicitation/predation": ["solicitation","predator","predation","grooming"],
 "trolling": ["trolling","troll"],
 "shilling": ["shill","shilling","ballot stuffing"],
 "bot/automated accounts": ["bot","bots","social bot"],
 "identity fraud": ["identity fraud"],
 "impersonation": ["impersonation","masquerade"],
 "anonymity attack": ["anonym"],
}
# flatten unique
add_words = sorted({w for ws in additions.values() for w in ws})

# simulate: recompute M1 hit with additions on metadata (title+abstract+keywords)
def meta_blob(rec):
    return ((rec.get("Title") or "")+"\n"+(rec.get("Abstract") or "")+"\n"+(rec.get("Author Keywords") or "")+"\n"+(rec.get("Index Keywords") or "")).lower()

missed_gain = []
for g in gold:
    doi=norm_doi(g.get("doi")); rec=find_csv(doi,g.get("title"))
    csv_doi=norm_doi(rec.get("DOI")) if rec else None
    m1=(csv_doi in m1_dois) if csv_doi else (doi in m1_dois)
    if m1 or rec is None: continue
    blob=meta_blob(rec)
    hits=[w for w in add_words if w in blob]
    if hits: missed_gain.append((g,rec,hits))

print("missed:", len([g for g in gold if not ((norm_doi((find_csv(norm_doi(g.get('doi')),g.get('title')) or {}).get('DOI')) in m1_dois) if find_csv(norm_doi(g.get('doi')),g.get('title')) else False)]))
print("recoverable by additions:", len(missed_gain))
for g,rec,hits in missed_gain:
    print(f"  {g['source_file'][:50]} | {rec.get('Title')[:60]} | +{hits}")
