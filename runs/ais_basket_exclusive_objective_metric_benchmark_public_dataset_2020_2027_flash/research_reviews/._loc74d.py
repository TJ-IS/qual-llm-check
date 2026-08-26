# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
out = io.open(base + "/._loc74d.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    pats = {"34": ["编码智能体对抗攻击的系统化生成与"], "35": ["编码智能体攻击面的事前预判与"], "36": ["编码智能体信息操纵攻击的流式检测与"]}
    for pat in pats[k]:
        start = 0
        while True:
            idx = t.find(pat, start)
            if idx < 0: break
            line_no = t.count("\n", 0, idx) + 1
            out.write("%s | %s | line %d\n" % (k, pat, line_no))
            for i in range(max(0,line_no-2), min(len(lines), line_no+2)):
                out.write("    |%s\n" % lines[i][:400])
            start = idx + 1
out.close()
print("done")
