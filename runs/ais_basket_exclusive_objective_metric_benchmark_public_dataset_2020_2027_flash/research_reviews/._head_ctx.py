# -*- coding: utf-8 -*-
import io, glob, re
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
out = io.open(rr + r"\_head_ctx.txt","w",encoding="utf-8")
for pat in ["策略头","通道选择头","内容生成头","生成头"]:
    out.write("===== %s =====\n" % pat)
    for m in re.finditer(re.escape(pat), t):
        out.write("  @%d: %s\n" % (m.start(), t[max(0,m.start()-70):m.start()+70].replace("\n"," ")))
out.close()
print("done")
