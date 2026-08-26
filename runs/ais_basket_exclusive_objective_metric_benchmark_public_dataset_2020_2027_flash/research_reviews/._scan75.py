# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
pats = ["基础设施", "成本可选", "成本递增", "两类信号", "三类信号", "所有攻击通道", "所有智能体", "全部基线", "回答防御动作强度", "guardrail", "新的且重要的", "新的且", "成功率最高", "代价最低"]
out = io.open(base + "/_scan75.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    for pat in pats:
        start = 0
        while True:
            idx = t.find(pat, start)
            if idx < 0: break
            line_no = t.count("\n", 0, idx) + 1
            s = max(0, idx-60); e = min(len(t), idx+80)
            out.write("%s | %s | line %d | ...%s...\n" % (k, pat, line_no, t[s:e].replace("\n"," ")))
            start = idx + 1
out.close()
print("done")
