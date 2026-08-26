# -*- coding: utf-8 -*-
import io, os, glob, re
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
# extract sections: 3.1, 2.5 tail, 6.0, 7.x for each paper
sections = ["### 3.1", "### 2.5", "## 六、预期结果", "### 6.0", "## 七、讨论与贡献", "### 7.1", "### 7.2", "### 7.3", "### 7.4", "### 7.5", "### 8.3"]
out = io.open(base + "/._sec74.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    out.write("\n" + "#"*40 + " PAPER " + k + " " + "#"*40 + "\n")
    for sec in sections:
        idx = -1
        for i, l in enumerate(lines):
            if l.strip().startswith(sec):
                idx = i; break
        if idx < 0:
            continue
        # collect until next header of same or higher level
        out.write("\n--- " + sec + " ---\n")
        for j in range(idx, min(len(lines), idx+40)):
            l = lines[j]
            if j > idx and re.match(r"^#{1,3} ", l.strip()) and not l.strip().startswith(sec):
                break
            out.write(l + "\n")
out.close()
print("done")
