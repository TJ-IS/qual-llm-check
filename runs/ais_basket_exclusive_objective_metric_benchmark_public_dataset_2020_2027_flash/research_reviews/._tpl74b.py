# -*- coding: utf-8 -*-
import io, re
f = "E:/github/qual-llm-check-IS-utd/database_fulltext_all/27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md"
t = io.open(f, encoding="utf-8").read()
t = re.sub(r"\s+", " ", t)
out = io.open("E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews/_tpl74b.txt", "w", encoding="utf-8")
for pat in [r"## Conclusion(.{2500})", r"Experiment 1.{2000}", r"we compared.{800}"]:
    m = re.search(pat, t, re.S)
    if m:
        out.write("--- " + pat + " ---\n" + m.group(0) + "\n\n")
# Introduction P1
i = t.find("With the recent increase")
out.write("--- INTRO P1 ---\n" + t[i:i+1500] + "\n")
out.close()
print("done")
