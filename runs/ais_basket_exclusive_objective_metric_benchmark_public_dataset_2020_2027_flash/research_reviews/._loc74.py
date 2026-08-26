# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
targets = ["放行低风险", "实践中有用的", "评估协议以", "评估协议将", "实验一展示", "实验一评估", "设计理由", "范式为依据", "遵循计算设计科学", "揭示了事前防御", "揭示了流式检测"]
out = io.open(base + "/._loc74.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    out.write("\n" + "#"*15 + " %s\n" % k)
    for pat in targets:
        start = 0
        hits = []
        while True:
            idx = t.find(pat, start)
            if idx < 0: break
            line_no = t.count("\n", 0, idx) + 1
            hdr = ""
            for i in range(line_no-2, -1, -1):
                l = lines[i].strip()
                if l.startswith("#"):
                    hdr = l; break
            hits.append((line_no, hdr))
            start = idx + 1
        if hits:
            out.write("  %s -> %s\n" % (pat, hits))
out.close()
print("done")
