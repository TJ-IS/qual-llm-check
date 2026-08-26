# -*- coding: utf-8 -*-
import io, os, glob, re
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
out = io.open(base + "/_fullsym74.txt", "w", encoding="utf-8")
for f in sorted(glob.glob(base + "/*_v3.1.md")):
    t = io.open(f, encoding="utf-8").read()
    out.write("="*20 + " " + os.path.basename(f)[:3] + " " + "="*20 + "\n")
    # 全角符号（除英文引号与DOI冒号外的合规项逐一列出）
    for ch, name in [("：","全角冒号"),("；","全角分号"),("—","破折号"),("…","省略号"),("→","箭头"),("“","中文左引"),("”","中文右引"),("‘","中文左单引"),("’","中文右单引")]:
        idx = 0
        while True:
            i = t.find(ch, idx)
            if i < 0: break
            line_no = t.count("\n", 0, i) + 1
            s = max(0, i-40); e = min(len(t), i+50)
            out.write("  %s line %d ...%s...\n" % (name, line_no, t[s:e].replace("\n"," ")))
            idx = i + 1
    # 半角引号清单（应为英文标题引号）
    idx = 0
    while True:
        i = t.find('"', idx)
        if i < 0: break
        line_no = t.count("\n", 0, i) + 1
        s = max(0, i-40); e = min(len(t), i+50)
        out.write("  半角引号 line %d ...%s...\n" % (line_no, t[s:e].replace("\n"," ")))
        idx = i + 1
out.close()
print("done")
