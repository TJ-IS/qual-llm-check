# -*- coding: utf-8 -*-
"""Missing-keyword analysis: for 23 M1-missed gold papers, find security words in metadata not in query term list."""
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
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    for row in csv.DictReader(fh):
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

missed=[]
for g in gold:
    doi=norm_doi(g.get("doi")); rec=find_csv(doi,g.get("title"))
    csv_doi=norm_doi(rec.get("DOI")) if rec else None
    m1=(csv_doi in m1_dois) if csv_doi else (doi in m1_dois)
    if not m1: missed.append((g,rec))

# security word candidates (broad list) to detect which words appear in metadata of missed papers
cand_words = ["attack","attacks","attacker","adversarial","malicious","malware","phish","fraud","fraudulent",
"decept","deceit","manipulat","spam","fake","bot","sockpuppet","shill","collusion","collusive","rating inflation",
"review manipulation","privacy","re-identif","de-identif","disclosure","anonym","confidential","breach","leak",
"security","vulnerab","exploit","intrusion","hack","hacker","hacking","cyber","cybercrime","cyberbully","cyberharass",
"aggression","griefing","flaming","doxing","trolling","troll","harass","abuse","abusive","stalking","predator","predation",
"solicitation","identity theft","insider threat","piracy","pirate","pirated","copyright","drm","counterfeit","forgery",
"audit","forensic","forensics","misconduct","unauthorized","illegal","criminal","crime","offense","violation","theft",
"steal","stolen","corruption","bribery","bribe","extortion","espionage","terror","ransom","darknet","dark web",
"control","access control","authentication","authorization","credential","password","key management","signature",
"watermark","tamper","tampering","poison","injection","jailbreak","prompt","oversharing","self-disclosure",
"computer abuse","monitoring","surveillance","privacy breach","information security","data security"]

out=[]
out.append("# 23 篇 M1 漏检的元数据安全词探测（哪些词可补入词表）\n")
for g,rec in sorted(missed,key=lambda x:x[0]["source_file"]):
    if rec is None:
        out.append(f"\n## {g['source_file']} | 无CSV记录")
        continue
    blob = ((rec.get("Title") or "")+" "+(rec.get("Abstract") or "")+" "+(rec.get("Author Keywords") or "")+" "+(rec.get("Index Keywords") or "")).lower()
    found=[w for w in cand_words if w in blob]
    out.append(f"\n## {g['source_file']}")
    out.append(f"- {rec.get('Title')} | {rec.get('Year')} | {rec.get('Source title')}")
    out.append(f"- 命中候选词: {', '.join(found) if found else '（无）'}")
with open(os.path.join(ROOT,"missed23_keywords.txt"),"w",encoding="utf-8") as f:
    f.write("\n".join(out))
print("written missed23_keywords.txt")

