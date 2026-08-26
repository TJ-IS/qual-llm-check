# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
out = io.open(base + "/_quotes74.txt", "w", encoding="utf-8")
for f in sorted(glob.glob(base + "/*_v3.1.md")):
    t = io.open(f, encoding="utf-8").read()
    for ch, name in [("“","左引"),("”","右引"),("‘","左单"),("’","右单"),("—","破折"),("：","冒号"),("；","分号"),("…","省略"),("→","箭头")]:
        idx = 0
        while True:
            i = t.find(ch, idx)
            if i < 0: break
            line_no = t.count("\n", 0, i) + 1
            s = max(0, i-50); e = min(len(t), i+60)
            out.write("%s | %s | line %d | ...%s...\n" % (os.path.basename(f)[:3], name, line_no, t[s:e].replace("\n"," ")))
            idx = i + 1
out.close()
print("done")
