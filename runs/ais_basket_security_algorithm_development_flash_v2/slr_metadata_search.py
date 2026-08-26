# -*- coding: utf-8 -*-
"""SLR-style metadata search: Title+Abstract+Author Keywords+Index Keywords on ALL_AIS_Basket_11.csv.
Compare recall on 99 vs fulltext head-8000 results."""
import csv, json, os, pickle, re

CSV_PATH = r"E:\github\qual-llm-check-IS-utd\database\ALL_AIS_Basket_11.csv"
ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"

# terms: reuse head cache terms (188 incl extras)
with open(os.path.join(ROOT, "fulltext_scan_head_cache.pkl"), "rb") as fh:
    ck, _ = pickle.load(fh)
files, terms, head_chars = ck
EXTRA = ["collusion","ballot stuffing","badmouthing","identity fraud","impersonation attack"]
Q_TERMS = [t for t in terms if t not in EXTRA]

def norm_doi(d):
    d = (d or "").strip().lower()
    d = re.sub(r"\s+", "", d)
    d = d.rstrip(".")
    return d

# load CSV
recs = []
doi2idx = {}
title2idx = {}
with open(CSV_PATH, encoding="utf-8-sig", errors="ignore", newline="") as fh:
    r = csv.DictReader(fh)
    for i, row in enumerate(r):
        recs.append(row)
        d = norm_doi(row.get("DOI"))
        if d:
            doi2idx.setdefault(d, []).append(i)
        t = re.sub(r"\s+", " ", (row.get("Title") or "")).strip().lower()
        if t:
            title2idx.setdefault(t, []).append(i)
print("csv records:", len(recs))
empty_abs = sum(1 for row in recs if not (row.get("Abstract") or "").strip())
print("csv empty abstract:", empty_abs)

# map 99 fulltext files -> csv records
src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as fh:
    for line in fh:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]

def frontmatter_doi(f):
    p = os.path.join(CORPUS, f)
    with open(p, encoding="utf-8", errors="ignore") as fh:
        head = fh.read(800)
    m = re.search(r"^doi:\s*\"?([^\"]+)\"?\s*$", head, re.M)
    return m.group(1) if m else ""

mapped = []
unmapped = []
for f in src2rec:
    d = norm_doi(frontmatter_doi(f))
    if d and d in doi2idx:
        mapped.append((f, doi2idx[d][0]))
    else:
        unmapped.append(f)
print(f"99 mapped by DOI: {len(mapped)}, unmapped: {len(unmapped)}")
for f in unmapped:
    print("  unmapped:", src2rec[f], f)

def rec_text(row):
    return " ".join([row.get("Title") or "", row.get("Abstract") or "",
                     row.get("Author Keywords") or "", row.get("Index Keywords") or ""]).lower()

# scan
hits_all = set()
hit_terms = {}
for i, row in enumerate(recs):
    txt = rec_text(row)
    m = 0
    for j, t in enumerate(terms):
        if t in txt:
            m |= (1 << j)
    if m:
        hits_all.add(i)
    hit_terms[i] = m

print("metadata query hits:", len(hits_all))

# recall on 99
missed99 = []
for f, idx in mapped:
    if idx not in hits_all:
        missed99.append((f, idx))
print(f"99 recall: {len(mapped)-len(missed99)}/{len(mapped)}")
for f, idx in missed99:
    row = recs[idx]
    print("  MISSED:", src2rec[f], "|", row.get("Title")[:100])
    print("    abs:", (row.get("Abstract") or "")[:200].replace("\n"," "))
    print("    kw:", (row.get("Author Keywords") or "")[:150], "|", (row.get("Index Keywords") or "")[:150])

# per-block stats on metadata
BLOCK_TERMS = {
    "Q1_malware": ["malware","malicious software","malicious code","malicious program","malicious application","malicious file","ransomware","trojan","botnet","keylogger","spyware","backdoor","computer virus","email worm","malicious payload","worm","virus propagation","malware propagation","malicious app","steganography","steganographic","covert channel"],
    "Q2_intrusion_network": ["intrusion detection","intrusion","denial of service","denial-of-service","ddos","network attack","cyberattack","cyber attack","cyber-attack","attack detection","attack graph","sql injection","code injection","command injection","cross-site scripting","zero-day","exploit","vulnerability","vulnerable","unauthorized access","privilege escalation","account takeover","credential theft","data breach","data exfiltration","network security","security attack","attack simulation","attack surface","port scan"],
    "Q3_adversarial": ["adversarial","adversary","adversarial attack","adversarial example","adversarial robustness","attack model","threat model"],
    "Q4_phishing_auth": ["phishing","spear phishing","social engineering","fake website","spoofing","spoof","deceptive","identity theft","credential","password","impersonation","masquerade","authentication","access control","authorization","key management"],
    "Q5_attacker_threat": ["attacker","malicious actor","malicious insider","insider threat","cybercriminal","cyber criminal","hacker","hacking","threat intelligence","cyber threat","advanced persistent threat","threat actor","malicious","cybercrime","cyber crime"],
    "Q6_content_manipulation": ["fake review","review manipulation","opinion spam","shilling attack","rating manipulation","fake news","false news","misinformation","disinformation","false information","fake follower","social bot","bot detection","cyberbullying","spam","spamming","deceptive review","fraudulent review","fake account","manipulation","fake content","manipulative","fraud","fraudulent","deception","deceit","concealed information"],
    "Q7_privacy_disclosure": ["re-identification","reidentification","de-identification","deidentification","disclosure risk","attribute disclosure","identity disclosure","record linkage","k-anonymity","k-anonymization","anonymization","anonymizing","data masking","data perturbation","data sanitization","privacy-preserving","privacy protection","privacy attack","inference attack","snooping","snooper","confidential data","sensitive data","sensitive information","data leakage","information leakage","privacy disclosure","privacy breach","deanonymization","de-anonymization","statistical disclosure","privacy","confidentiality"],
    "Q8_threat_intel_vuln": ["dark web","darknet","dark net","hacker forum","hacker community","underground forum","underground economy","carding","cve","vulnerability management","vulnerability assessment","security vulnerability","countermeasure","security controls","security control","security investment","security risk","cyber risk","cyber insurance","information security","it security","cybersecurity","cyber security","security monitoring","security management","security analytics","honeypot"],
}

lines = ["# SLR 元数据检索（Title+Abstract+Keywords）测试报告\n"]
lines.append(f"- 元数据源：ALL_AIS_Basket_11.csv，{len(recs)} 条（空摘要 {empty_abs} 条）")
lines.append(f"- 检索字段：Title + Abstract + Author Keywords + Index Keywords（Scopus 标准 SLR 字段）")
lines.append(f"- 词表：Q1–Q8（183 词）+ 补充 5 词，共 {len(terms)} 词")
lines.append(f"- 元数据命中：{len(hits_all)} 条")
lines.append(f"- 99 篇 DOI 映射：{len(mapped)}/99；元数据检索召回：{len(mapped)-len(missed99)}/{len(mapped)}（含未映射则 {len(mapped)-len(missed99)}/99）\n")

lines.append("## 各词块在元数据层的命中\n")
lines.append("| 词块 | 元数据命中 |")
lines.append("|---|---|")
for b, ts in BLOCK_TERMS.items():
    cnt = sum(1 for i in hits_all if any(t in rec_text(recs[i]) for t in ts))
    lines.append(f"| {b} | {cnt} |")

# save candidate list
out = os.path.join(ROOT, "slr_metadata_candidates.txt")
with open(out, "w", encoding="utf-8") as fh:
    for i in sorted(hits_all):
        row = recs[i]
        fh.write(f"{i}\t{row.get('Title')}\t{row.get('Year')}\t{row.get('Source title')}\t{row.get('DOI')}\n")
lines.append(f"\n候选清单：{out}")

with open(os.path.join(ROOT, "slr_metadata_search_report.md"), "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("report written")
