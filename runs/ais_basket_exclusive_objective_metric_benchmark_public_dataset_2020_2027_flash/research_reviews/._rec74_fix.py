# -*- coding: utf-8 -*-
import io
p = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\74_三篇跨篇重复扫描与批次六修改落盘记录.md"
t = io.open(p, encoding="utf-8").read()
old = "回到模板原文逐句对照"
new = "回到模板原文逐段对照"
assert t.count(old) == 1
t = t.replace(old, new)
io.open(p, "w", encoding="utf-8", newline="").write(t)
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
syms = ["：","；","—","“","”","‘","’","…","→"]
hits = {w: t.count(w) for w in banned if w in t}
sh = {c: t.count(c) for c in syms if c in t}
print("禁词:", hits or "无", "| 符号:", sh or "全零")
