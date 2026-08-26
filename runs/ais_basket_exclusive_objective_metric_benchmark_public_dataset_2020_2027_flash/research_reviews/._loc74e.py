# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
out = io.open(base + "/._loc74e.txt", "w", encoding="utf-8")
t = io.open(fs["34"], encoding="utf-8").read()
lines = t.split("\n")
for pat in ["威胁建模", "威胁模型", "系统化生成"]:
    start = 0
    out.write("PAT %s\n" % pat)
    while True:
        idx = t.find(pat, start)
        if idx < 0: break
        line_no = t.count("\n", 0, idx) + 1
        out.write("  line %d: %s\n" % (line_no, lines[line_no-1][:160]))
        start = idx + 1
out.close()
print("done")
