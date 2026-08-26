# -*- coding: utf-8 -*-
import os, re
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
OUT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1\abstract_marker_check.txt"
files = ["26444_2002_assessing-the-validity-of-is-success-models-an-empirical-test-and-theoretical-analysis.md",
         "00606_2016_the-impact-of-fake-reviews-on-online-visibility-a-vulnerability-assessment-of-the-hotel-industry.md",
         "26481_2002_the-security-of-confidential-numerical-data-in-databases.md",
         "13512_2015_insider-threats-in-a-financial-institution-analysis-of-attack-proneness-of-information-systems-a.md",
         "05320_2012_b-research-note-b-generating-shareable-statistical-databases-for-business-value-multiple-imputat.md",
         "15088_2014_the-most-popular-news-recommender-count-amplification-and-manipulation-resistance.md"]
lines = []
for f in files:
    with open(os.path.join(CORPUS, f), encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    lines.append("="*100)
    lines.append(f"len={len(raw)}")
    for m in re.finditer(r"(?i)abstract", raw):
        s = max(0, m.start()-80)
        ctx = re.sub(r"\s+", " ", raw[s:m.end()+200])
        lines.append(f"  @{m.start()}: ...{ctx}...")
    # also look for 'a b s t r a c t' spaced
    for m in re.finditer(r"(?i)a[\.\s]*b[\.\s]*s[\.\s]*t[\.\s]*r[\.\s]*a[\.\s]*c[\.\s]*t", raw):
        ctx = re.sub(r"\s+", " ", raw[max(0,m.start()-60):m.end()+150])
        lines.append(f"  spaced@{m.start()}: ...{ctx}...")
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("written")
