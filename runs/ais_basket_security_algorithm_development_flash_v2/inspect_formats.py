# -*- coding: utf-8 -*-
import os
CORPUS = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
OUT = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_security_algorithm_development_flash_v2\output_v1\format_inspect.txt"
lines = []
for f in ["06870_2014_innovating-financial-information-infrastructures-the-transition-of-legacy-assets-to-the-securiti.md",
          "26444_2002_assessing-the-validity-of-is-success-models-an-empirical-test-and-theoretical-analysis.md",
          "26481_2002_the-security-of-confidential-numerical-data-in-databases.md",
          "05320_2012_b-research-note-b-generating-shareable-statistical-databases-for-business-value-multiple-imputat.md",
          "00606_2016_the-impact-of-fake-reviews-on-online-visibility-a-vulnerability-assessment-of-the-hotel-industry.md",
          "12102_2014_filtering-trust-opinions-through-reinforcement-learning.md"]:
    with open(os.path.join(CORPUS, f), encoding="utf-8", errors="ignore") as fh:
        raw = fh.read(6000)
    lines.append("="*100)
    lines.append(f)
    lines.append(raw[:2600])
with open(OUT, "w", encoding="utf-8") as fh:
    fh.write("\n".join(lines))
print("written")

