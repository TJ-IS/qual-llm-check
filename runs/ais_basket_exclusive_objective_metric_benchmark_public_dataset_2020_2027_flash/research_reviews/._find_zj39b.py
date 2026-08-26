import io
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md"
t = io.open(fn, encoding="utf-8").read()
idxs = []
start = 0
while True:
    i = t.find("逐句", start)
    if i == -1: break
    idxs.append(i)
    start = i + 1
print("count:", len(idxs))
for i in idxs:
    print("---", t[max(0,i-60):i+60].replace("\n"," "))