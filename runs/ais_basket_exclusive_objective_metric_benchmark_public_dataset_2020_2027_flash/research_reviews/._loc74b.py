# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
want = {"34": [143], "35": [43, 73, 155], "36": [15, 83, 151, 161, 183]}
out = io.open(base + "/._loc74b.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    out.write("\n" + "#"*15 + " %s\n" % k)
    for ln in want[k]:
        out.write("\n--- line %d ---\n" % ln)
        for i in range(max(0,ln-1), min(len(lines), ln+1)):
            out.write("  |%s\n" % lines[i][:700])
out.close()
print("done")
