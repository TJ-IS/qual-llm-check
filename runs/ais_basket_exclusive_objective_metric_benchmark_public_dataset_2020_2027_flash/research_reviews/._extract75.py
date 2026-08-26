# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
for p in sorted(glob.glob(base + "/*_v3.1.md")):
    t = io.open(p, encoding="utf-8").read()
    body = t.split("## 参考文献")[0]
    fn = os.path.basename(p)[:3] + "_full.txt"
    io.open(base + "/" + fn, "w", encoding="utf-8").write(body)
print("done")
