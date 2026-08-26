# -*- coding: utf-8 -*-
import io, glob
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
out = io.open(rr + r"\_ch23_34.txt","w",encoding="utf-8")
i = t.find("### 2.3")
j = t.find("### 2.4")
out.write(t[i:j])
out.close()
print("done")
