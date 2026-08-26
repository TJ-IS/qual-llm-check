# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
out = io.open(base + "/_final74.txt", "w", encoding="utf-8")
t34 = io.open(fs["34"], encoding="utf-8").read()
i = t34.find("为此，本文以威胁驱动设计与强化学习理论为基础设计了")
out.write("[34 结论]\n" + t34[i-60:i+120] + "\n\n")
t35 = io.open(fs["35"], encoding="utf-8").read()
i = t35.find("把 IS 预测与优化文献的方法论置于")
out.write("[35 7.1]\n" + t35[i-80:i+80] + "\n\n")
i = t35.find("本文的预期实验结果显示")
out.write("[35 7.2]\n" + t35[i-40:i+90] + "\n\n")
t36 = io.open(fs["36"], encoding="utf-8").read()
i = t36.find("经由严格评估，我们预期该框架")
out.write("[36 9章]\n" + t36[i-60:i+180] + "\n")
out.close()
print("done")
