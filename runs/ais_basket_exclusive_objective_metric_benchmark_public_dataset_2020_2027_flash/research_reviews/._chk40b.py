import io
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\40_引言段落句子级二轮核对与模板对照改写记录.md"
t = io.open(fn, encoding="utf-8").read()
print("40 chars:", len(t))
left = [w for w in ["逐句","审计"] if w in t]
print("40 left:", left)
# 检查 4.2 节修正后的内容
i = t.find("### 4.2")
print(t[i:i+900])