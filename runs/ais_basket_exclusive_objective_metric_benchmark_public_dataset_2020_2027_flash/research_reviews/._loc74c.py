# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
spots = {"34": 15241, "35": 1732, "36": 2439}
out = io.open(base + "/._loc74c.txt", "w", encoding="utf-8")
for k, pos in spots.items():
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    line_no = t.count("\n", 0, pos) + 1
    out.write("%s line %d:\n" % (k, line_no))
    for i in range(max(0,line_no-2), min(len(lines), line_no+1)):
        out.write("  |%s\n" % lines[i][:500])
    out.write("\n")
out.close()
print("done")
