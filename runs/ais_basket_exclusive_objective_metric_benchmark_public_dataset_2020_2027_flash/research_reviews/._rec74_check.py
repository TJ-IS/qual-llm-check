# -*- coding: utf-8 -*-
import io
p = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\74_三篇跨篇重复扫描与批次六修改落盘记录.md"
t = io.open(p, encoding="utf-8").read()
banned = ["旗舰","不可修改","外部层","只能做","裸","冲突","审计","逐句","写作纪律","病毒库","弹窗","重跑"]
syms = {"：":"全角冒号","；":"全角分号","—":"破折号","“":"引号","”":"引号","‘":"引号","’":"引号","…":"省略号","→":"箭头"}
hits = {w: t.count(w) for w in banned if w in t}
sh = {n: t.count(c) for c, n in syms.items() if c in t}
out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\_rec74_check.txt", "w", encoding="utf-8")
out.write("禁词: %s\n符号: %s\n" % (hits or "无", sh or "全零"))
out.close()
print("done")
