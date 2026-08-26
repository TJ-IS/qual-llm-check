# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
spots = {
 "34": [(5054,"SWExploit-1"),(11390,"SWExploit-2"),(11980,"SWExploit-3"),(184,"SWE-bench-1"),(385,"SWE-bench-2"),(939,"loop-1"),(7510,"loop-2"),(2340,"migr-1"),(8422,"migr-2")],
 "35": [(1588,"signal-1"),(5179,"signal-2"),(7416,"signal-3"),(1579,"obs-1"),(7407,"obs-2")],
 "36": [(10755,"adojo-1"),(12186,"adojo-2"),(16186,"adojo-3"),(1134,"imt-1"),(4445,"imt-2")],
}
out = io.open(base + "/._ctx74.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    out.write("="*30 + " " + k + " " + "="*30 + "\n")
    for pos, label in spots[k]:
        s = max(0, pos-220); e = min(len(t), pos+340)
        ctx = t[s:e].replace("\n","\\n")
        out.write("--- %s @%d ---\n" % (label, pos))
        out.write(ctx + "\n\n")
out.close()
print("done")
