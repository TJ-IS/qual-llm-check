# -*- coding: utf-8 -*-
import io, os
base = r"E:\github\qual-llm-check-IS-utd"
targets = {"\u2014":"EMDASH","\u201c":"LQUOTE","\u201d":"RQUOTE","\uff1a":"COLON"}
rows = []
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d != ".git"]
    for fn in files:
        if not fn.endswith(".md"): continue
        p = os.path.join(root, fn)
        try:
            t = io.open(p, encoding="utf-8").read()
        except Exception:
            continue
        hits = {}
        for ch, name in targets.items():
            c = t.count(ch)
            if c: hits[name] = c
        if hits:
            total = sum(hits.values())
            rel = os.path.relpath(p, base)
            rows.append((total, rel, hits))
rows.sort(reverse=True)
out = io.open(os.path.join(base, "runs", "ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash", "research_reviews", "_r76_repo_scan.txt"), "w", encoding="utf-8")
for total, rel, hits in rows:
    out.write("%4d | %s | %s\n" % (total, rel, hits))
out.close()
print("done", len(rows))
