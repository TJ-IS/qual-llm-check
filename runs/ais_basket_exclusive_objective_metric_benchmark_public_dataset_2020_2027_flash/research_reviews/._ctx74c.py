# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
targets = {
 "34": ["SWE-bench Verified 上修复了约", "通道选择、内容生成与结果反馈构成循环", "系统化地生成覆盖多通道、可迁移"],
}
out = io.open(base + "/._ctx74c.txt", "w", encoding="utf-8")
for k in ["34"]:
    t = io.open(fs[k], encoding="utf-8").read()
    lines = t.split("\n")
    for pat in targets[k]:
        out.write("\n" + "#"*20 + " %s : %s\n" % (k, pat))
        start = 0
        while True:
            idx = t.find(pat, start)
            if idx < 0: break
            line_no = t.count("\n", 0, idx) + 1
            hdr = ""
            for i in range(line_no-2, -1, -1):
                l = lines[i].strip()
                if l.startswith("#"):
                    hdr = l; break
            out.write("  [line %d] (sec: %s)\n" % (line_no, hdr))
            for i in range(max(0,line_no-2), min(len(lines), line_no+2)):
                out.write("    |%s\n" % lines[i][:600])
            out.write("  ---\n")
            start = idx + 1
out.close()
print("done")
