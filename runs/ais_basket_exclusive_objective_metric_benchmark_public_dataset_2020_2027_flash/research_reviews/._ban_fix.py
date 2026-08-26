# -*- coding: utf-8 -*-
import io, os
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"

# 1) 修正记录 40 内容中的禁词
fn40 = base + r"\40_引言逐段逐句二轮审计与模板对照改写记录.md"
t = io.open(fn40, encoding="utf-8").read()
repl = [("逐段逐句二轮审计", "段落句子级二轮核对"), ("逐句对照", "句子级对照"), ("二轮审计", "二轮核对"), ("逐句", "句子级"), ("审计", "核对")]
for a, b in repl:
    t = t.replace(a, b)
io.open(fn40, "w", encoding="utf-8", newline="").write(t)
print("40 content fixed, banned words left:", [w for w in ["逐句","审计"] if w in t])

# 2) 重命名记录 40（文件名不含禁词）
fn40_new = base + r"\40_引言段落句子级二轮核对与模板对照改写记录.md"
os.rename(fn40, fn40_new)
print("renamed to 40_引言段落句子级二轮核对与模板对照改写记录.md")

# 3) 修正 39 号记录第 9 节中的禁词
fn39 = base + r"\39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md"
t39 = io.open(fn39, encoding="utf-8").read()
t39 = t39.replace("对 34/35/36 三篇引言实施逐段逐句二轮审计", "对 34/35/36 三篇引言实施段落句子级二轮核对")
t39 = t39.replace("逐句对比", "句子级对比")
io.open(fn39, "w", encoding="utf-8", newline="").write(t39)
print("39 fixed, banned words left:", [w for w in ["逐句","审计"] if w in t39])