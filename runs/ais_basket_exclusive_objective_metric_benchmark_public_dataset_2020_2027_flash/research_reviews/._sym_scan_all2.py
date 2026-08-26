# -*- coding: utf-8 -*-
import io, os, glob
roots = [
 r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews",
 r"E:\github\qual-llm-check-IS-utd\thesis_collection",
 r"E:\github\qual-llm-check-IS-utd\thesis_papers_v3.1",
 r"E:\github\qual-llm-check-IS-utd\thesis_papers_v3",
 r"E:\github\qual-llm-check-IS-utd\thesis_papers_v6_xiao_style",
]
syms = {"—":"em", "―":"hor", "“":"lq", "”":"rq", "‘":"lsq", "’":"rsq", "：":"colon", "；":"semi", "…":"ell", "→":"arrow", "-":"hyphen"}
out = []
for root in roots:
    for p in glob.glob(os.path.join(root, "*.md")) + glob.glob(os.path.join(root, "archive", "*.md")):
        try:
            t = io.open(p, encoding="utf-8").read()
        except Exception as e:
            continue
        cnt = {n: t.count(c) for c, n in syms.items()}
        total = sum(cnt.values())
        if total > 0:
            out.append("%s | %d | %s" % (os.path.basename(p), total, ", ".join("%s=%d" % (n, cnt[n]) for n in sorted(cnt, key=lambda x: -cnt[x]) if cnt[n] > 0)))
out.sort(key=lambda x: -int(x.split(" | ")[1]))
io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\_sym_scan_all2.txt", "w", encoding="utf-8").write("\n".join(out) + "\n\n共 %d 个文件含符号\n" % len(out))
print("done")
