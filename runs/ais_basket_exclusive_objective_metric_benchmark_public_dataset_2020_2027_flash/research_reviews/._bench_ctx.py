# -*- coding: utf-8 -*-
import io, glob, re
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
out = io.open(rr + r"\_bench_ctx.txt","w",encoding="utf-8")
for pat in ["AgentDojo","MalSkillBench","IssueTrojanBench","SWExploit","FCV","RLbreaker"]:
    out.write("===== %s =====\n" % pat)
    for m in re.finditer(re.escape(pat), t):
        out.write("  @%d: %s\n" % (m.start(), t[max(0,m.start()-90):m.start()+90].replace("\n"," ")))
out.close()
print("done")
