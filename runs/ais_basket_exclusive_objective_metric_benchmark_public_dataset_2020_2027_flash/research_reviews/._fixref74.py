# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
log = []
for f in sorted(glob.glob(base + "/*_v3.1.md")):
    t = io.open(f, encoding="utf-8").read()
    old = "Who is the next \u201cWolf of Wall Street\u201d?"
    new = "Who is the next \"Wolf of Wall Street\"?"
    c = t.count(old)
    log.append("%s: %d" % (os.path.basename(f)[:3], c))
    if c == 1:
        t = t.replace(old, new)
    io.open(f, "w", encoding="utf-8", newline="").write(t)
io.open(base + "/_fixref74_log.txt", "w", encoding="utf-8").write("\n".join(log) + "\n")
print("done")
