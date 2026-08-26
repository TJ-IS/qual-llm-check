# -*- coding: utf-8 -*-
"""Fulltext recall test for AIS security query blocks (99 papers as recall baseline)."""
import json, os, time

CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"

BLOCKS = {
    "Q1_malware": [
        "malware", "malicious software", "malicious code", "malicious program",
        "malicious application", "malicious file", "ransomware", "trojan", "botnet",
        "keylogger", "spyware", "backdoor", "computer virus", "email worm",
        "malicious payload", "worm", "virus propagation", "malware propagation",
        "malicious app", "steganography", "steganographic", "covert channel",
    ],
    "Q2_intrusion_network": [
        "intrusion detection", "intrusion", "denial of service", "denial-of-service",
        "ddos", "network attack", "cyberattack", "cyber attack", "cyber-attack",
        "attack detection", "attack graph", "sql injection", "code injection",
        "command injection", "cross-site scripting", "zero-day", "exploit",
        "vulnerability", "vulnerable", "unauthorized access", "privilege escalation",
        "account takeover", "credential theft", "data breach", "data exfiltration",
        "network security", "security attack", "attack simulation", "attack surface",
        "port scan",
    ],
    "Q3_adversarial": [
        "adversarial", "adversary", "adversarial attack", "adversarial example",
        "adversarial robustness", "attack model", "threat model",
    ],
    "Q4_phishing_auth": [
        "phishing", "spear phishing", "social engineering", "fake website",
        "spoofing", "spoof", "deceptive", "identity theft", "credential",
        "password", "impersonation", "masquerade", "authentication", "access control",
        "authorization", "key management",
    ],
    "Q5_attacker_threat": [
        "attacker", "malicious actor", "malicious insider", "insider threat",
        "cybercriminal", "cyber criminal", "hacker", "hacking", "threat intelligence",
        "cyber threat", "advanced persistent threat", "threat actor", "malicious",
        "cybercrime", "cyber crime",
    ],
    "Q6_content_manipulation": [
        "fake review", "review manipulation", "opinion spam", "shilling attack",
        "rating manipulation", "fake news", "false news", "misinformation",
        "disinformation", "false information", "fake follower", "social bot",
        "bot detection", "cyberbullying", "spam", "spamming", "deceptive review",
        "fraudulent review", "fake account", "manipulation", "fake content",
        "manipulative", "fraud", "fraudulent", "deception", "deceit", "concealed information",
    ],
    "Q7_privacy_disclosure": [
        "re-identification", "reidentification", "de-identification", "deidentification",
        "disclosure risk", "attribute disclosure", "identity disclosure", "record linkage",
        "k-anonymity", "k-anonymization", "anonymization", "anonymizing", "data masking",
        "data perturbation", "data sanitization", "privacy-preserving", "privacy protection",
        "privacy attack", "inference attack", "snooping", "snooper", "confidential data",
        "sensitive data", "sensitive information", "data leakage", "information leakage",
        "privacy disclosure", "privacy breach", "deanonymization", "de-anonymization",
        "statistical disclosure", "privacy", "confidentiality",
    ],
    "Q8_threat_intel_vuln": [
        "dark web", "darknet", "dark net", "hacker forum", "hacker community",
        "underground forum", "underground economy", "carding", "cve",
        "vulnerability management", "vulnerability assessment", "security vulnerability",
        "countermeasure", "security controls", "security control", "security investment",
        "security risk", "cyber risk", "cyber insurance", "information security",
        "it security", "cybersecurity", "cyber security", "security monitoring",
        "security management", "security analytics", "honeypot",
    ],
    "Q9_broad": ["attack", "security", "threat", "robustness", "defense", "detection"],
}

# load 99 mapping source_file -> record_id
src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]

files = sorted(f for f in os.listdir(CORPUS) if f.endswith(".md"))
file_idx = {f: i for i, f in enumerate(files)}

# flatten terms
terms = []
for bname, tlist in BLOCKS.items():
    for t in tlist:
        terms.append((bname, t.lower()))
TERM_ID = {(bn, t): i for i, (bn, t) in enumerate(terms)}
NBITS = len(terms)

import pickle
CACHE = os.path.join(ROOT, "fulltext_scan_cache.pkl")
cache_key = (files, [t for (_, t) in terms])
if os.path.exists(CACHE):
    with open(CACHE, "rb") as fh:
        ck, masks = pickle.load(fh)
    if ck != cache_key:
        masks = None
else:
    masks = None
if masks is None:
    t0 = time.time()
    masks = [0] * len(files)
    for i, f in enumerate(files):
        with open(os.path.join(CORPUS, f), encoding="utf-8", errors="ignore") as fh:
            txt = fh.read().lower()
        m = 0
        for j, (_, t) in enumerate(terms):
            if t in txt:
                m |= (1 << j)
        masks[i] = m
    with open(CACHE, "wb") as fh:
        pickle.dump((cache_key, masks), fh)
    print(f"scan done {time.time()-t0:.0f}s files={len(files)}")
else:
    print("cache loaded")

def files_with_mask(mask):
    return [i for i, m in enumerate(masks) if m & mask]

# block masks
block_mask = {}
for bname in BLOCKS:
    bm = 0
    for (bn, t) in terms:
        if bn == bname:
            bm |= (1 << TERM_ID[(bname, t)])
    block_mask[bname] = bm

# per-block per-term stats among 99
rec99 = [file_idx[f] for f in src2rec if f in file_idx]
rec99_idx = set(rec99)
print(f"99 mapped: {len(rec99)}")

def recall(blockname):
    bm = block_mask[blockname]
    hits = files_with_mask(bm)
    hit99 = [i for i in hits if i in rec99_idx]
    return len(hit99), len(hits)

# combined query (all blocks except Q9? report both)
combined_mask = 0
for bm in block_mask.values():
    combined_mask |= bm
combined_noQ9 = 0
for bname, bm in block_mask.items():
    if bname != "Q9_broad":
        combined_noQ9 |= bm

report = []
report.append("# 全文检索式 Recall 测试报告（以 99 篇为基准）\n")
report.append(f"- 语料：database_fulltext_all，{len(files)} 篇")
report.append(f"- 词块数：{len(BLOCKS)}，术语数：{len(terms)}")
report.append(f"- 99 篇映射到语料：{len(rec99)}/99\n")

report.append("## 各词块召回（99 篇中命中数 / 语料命中总数）\n")
report.append("| 词块 | 99命中 | 99召回率 | 语料命中 | 说明 |")
report.append("|---|---|---|---|---|")
for bname in BLOCKS:
    h99, htot = recall(bname)
    report.append(f"| {bname} | {h99} | {h99/99:.1%} | {htot} |  |")

h99_all, htot_all = recall("__all__") if False else (0,0)
# combined
def combined_stats(mask):
    hits = files_with_mask(mask)
    h99 = [i for i in hits if i in rec99_idx]
    return len(h99), len(hits)
for label, mask in [("Q1-Q8（全部词块）", combined_mask), ("Q1-Q8（不含 Q9 通用词）", combined_noQ9)]:
    h99, htot = combined_stats(mask)
    report.append(f"\n## {label}：99 命中 {h99}/99（{h99/99:.1%}），语料命中 {htot}\n")

# missed 99 by combined Q1-Q8
hits_all = set(files_with_mask(combined_noQ9))
missed = [f for f in src2rec if f in file_idx and file_idx[f] not in hits_all]
report.append("## Q1-Q8 未命中的 99 篇（需补词）\n")
for f in missed:
    report.append(f"- {src2rec[f]} | {f}")

# per-term coverage among 99 (top terms)
report.append("\n## 术语对 99 篇的覆盖（按命中数降序，前 60）\n")
term99 = []
for (bname, t) in terms:
    bit = 1 << TERM_ID[(bname, t)]
    cnt = sum(1 for i in rec99 if masks[i] & bit)
    term99.append((bname, t, cnt))
term99.sort(key=lambda x: -x[2])
for bname, t, cnt in term99[:60]:
    report.append(f"- [{bname}] {t}: {cnt}/99")

# sample non-99 hits per block (first 8)
report.append("\n## 各词块语料命中的非 99 样本（前 8，检查噪声）\n")
for bname in BLOCKS:
    bm = block_mask[bname]
    hits = [i for i in files_with_mask(bm) if i not in rec99_idx][:8]
    report.append(f"### {bname}")
    for i in hits:
        report.append(f"- {files[i]}")

out = os.path.join(ROOT, "fulltext_recall_report.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(report))
print("report written:", out)

