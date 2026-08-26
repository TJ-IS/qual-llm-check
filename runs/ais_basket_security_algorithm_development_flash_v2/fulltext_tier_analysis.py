# -*- coding: utf-8 -*-
"""Tier analysis on cached masks: recall/hits for query combinations + block coverage of 99."""
import json, os, pickle

ROOT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1"
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"

BLOCKS = {
    "Q1_malware": ["malware","malicious software","malicious code","malicious program","malicious application","malicious file","ransomware","trojan","botnet","keylogger","spyware","backdoor","computer virus","email worm","malicious payload","worm","virus propagation","malware propagation","malicious app","steganography","steganographic","covert channel"],
    "Q2_intrusion_network": ["intrusion detection","intrusion","denial of service","denial-of-service","ddos","network attack","cyberattack","cyber attack","cyber-attack","attack detection","attack graph","sql injection","code injection","command injection","cross-site scripting","zero-day","exploit","vulnerability","vulnerable","unauthorized access","privilege escalation","account takeover","credential theft","data breach","data exfiltration","network security","security attack","attack simulation","attack surface","port scan"],
    "Q3_adversarial": ["adversarial","adversary","adversarial attack","adversarial example","adversarial robustness","attack model","threat model"],
    "Q4_phishing_auth": ["phishing","spear phishing","social engineering","fake website","spoofing","spoof","deceptive","identity theft","credential","password","impersonation","masquerade","authentication","access control","authorization","key management"],
    "Q5_attacker_threat": ["attacker","malicious actor","malicious insider","insider threat","cybercriminal","cyber criminal","hacker","hacking","threat intelligence","cyber threat","advanced persistent threat","threat actor","malicious","cybercrime","cyber crime"],
    "Q6_content_manipulation": ["fake review","review manipulation","opinion spam","shilling attack","rating manipulation","fake news","false news","misinformation","disinformation","false information","fake follower","social bot","bot detection","cyberbullying","spam","spamming","deceptive review","fraudulent review","fake account","manipulation","fake content","manipulative","fraud","fraudulent","deception","deceit","concealed information"],
    "Q7_privacy_disclosure": ["re-identification","reidentification","de-identification","deidentification","disclosure risk","attribute disclosure","identity disclosure","record linkage","k-anonymity","k-anonymization","anonymization","anonymizing","data masking","data perturbation","data sanitization","privacy-preserving","privacy protection","privacy attack","inference attack","snooping","snooper","confidential data","sensitive data","sensitive information","data leakage","information leakage","privacy disclosure","privacy breach","deanonymization","de-anonymization","statistical disclosure","privacy","confidentiality"],
    "Q8_threat_intel_vuln": ["dark web","darknet","dark net","hacker forum","hacker community","underground forum","underground economy","carding","cve","vulnerability management","vulnerability assessment","security vulnerability","countermeasure","security controls","security control","security investment","security risk","cyber risk","cyber insurance","information security","it security","cybersecurity","cyber security","security monitoring","security management","security analytics","honeypot"],
}

with open(os.path.join(ROOT, "fulltext_scan_cache.pkl"), "rb") as fh:
    cache_key, masks = pickle.load(fh)
files, terms = cache_key
TERM_ID = {t: i for i, t in enumerate(terms)}
file_idx = {f: i for i, f in enumerate(files)}

src2rec = {}
with open(os.path.join(ROOT, "data_publicness_v3.jsonl"), encoding="utf-8") as f:
    for line in f:
        o = json.loads(line)
        src2rec[o["source_file"]] = o["record_id"]
rec99 = [file_idx[f] for f in src2rec if f in file_idx]
rec99_set = set(rec99)

# block masks (terms are already lowercased in cache list; BLOCKS terms are lowercase too)
block_mask = {}
for bname, tlist in BLOCKS.items():
    bm = 0
    for t in tlist:
        if t in TERM_ID:
            bm |= (1 << TERM_ID[t])
    block_mask[bname] = bm

def stats(blocks):
    mask = 0
    for b in blocks:
        mask |= block_mask[b]
    hits = [i for i, m in enumerate(masks) if m & mask]
    h99 = [i for i in hits if i in rec99_set]
    return len(h99), len(hits)

tiers = {
    "T1 恶意代码+对抗鲁棒": ["Q1_malware", "Q3_adversarial"],
    "T2 攻击对抗核心(T1+入侵+攻击者)": ["Q1_malware", "Q3_adversarial", "Q2_intrusion_network", "Q5_attacker_threat"],
    "T3 内容操纵+钓鱼": ["Q4_phishing_auth", "Q6_content_manipulation"],
    "T4 隐私披露": ["Q7_privacy_disclosure"],
    "T5 威胁情报/漏洞": ["Q8_threat_intel_vuln"],
    "T6 安全全量(Q1-Q8)": list(BLOCKS.keys()),
    "T7 非隐私安全(T6-T4)": [b for b in BLOCKS if b != "Q7_privacy_disclosure"],
    "T8 高信号精简(仅特定术语块)": ["Q1_malware", "Q3_adversarial", "Q2_intrusion_network"],
}

lines = ["# 分层检索组合（tier）分析\n", "| 组合 | 99命中 | 召回率 | 语料命中 | 需筛数量级 |"]
lines.append("|---|---|---|---|---|")
for name, blocks in tiers.items():
    h99, htot = stats(blocks)
    lines.append(f"| {name} | {h99}/99 | {h99/99:.1%} | {htot} | ~{htot} |")

# coverage: which blocks each of 99 hit
lines.append("\n## 99 篇的词块覆盖（每篇命中哪些块）\n")
cov = []
for f in src2rec:
    i = file_idx[f]
    bnames = [b for b in BLOCKS if masks[i] & block_mask[b]]
    cov.append((src2rec[f], f, bnames))
# 只列出覆盖块数 <= 2 的（最依赖单一词块的，风险最高）
few = [c for c in cov if len(c[2]) <= 2]
lines.append(f"仅命中 1-2 个词块的 99 篇（{len(few)} 篇）：\n")
for rid, f, bnames in few:
    lines.append(f"- {rid} | {f} | {','.join(bnames)}")

# papers hit ONLY via Q7 or ONLY via Q6 etc. (dependence)
lines.append("\n## 单块依赖（仅被某一块覆盖）\n")
for b in BLOCKS:
    only = [c for c in cov if c[2] == [b]]
    if only:
        lines.append(f"### 仅 {b}：{len(only)} 篇")
        for rid, f, _ in only:
            lines.append(f"- {rid} | {f}")

out = os.path.join(ROOT, "fulltext_tier_analysis.md")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("written", out)
