# -*- coding: utf-8 -*-
import io, os, re
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = [f for f in os.listdir(base) if f.endswith(".md") and not f.startswith("._")]
sym_names = {
 "：":"全角冒号", ";":"中文分号", "—":"破折号—", "–":"破折号–", "―":"破折号―", "——":"双破折号",
 "“":"左引号", "”":"右引号", "‘":"左单引", "’":"右单引", "「":"日引号", "」":"日引号",
}
def scan(fn):
    t = io.open(os.path.join(base, fn), encoding="utf-8").read()
    body = t.split("## 参考文献")[0] if "## 参考文献" in t else t
    hits = {}
    for ch, name in sym_names.items():
        c = body.count(ch)
        if c: hits[name] = hits.get(name,0)+c
    return hits
print("=== 论文文件 ===")
for fn in sorted(files):
    if fn[:2] in ("34","35","36","31","32","33","12","13","14","16","17","25"):
        h = scan(fn)
        print(f"{fn[:14]} -> {h if h else 'clean'}")
print()
print("=== 记录文件 ===")
for fn in sorted(files):
    if fn[:2] in ("37","38","39","40","18","19","20","21","22","23","24","26","27","28","29","30"):
        h = scan(fn)
        if h: print(f"{fn[:12]} -> {h}")