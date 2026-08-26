import io
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md"
t = io.open(fn, encoding="utf-8").read()
i = t.find("逐句")
print("context:", t[max(0,i-80):i+80].replace("\n"," "))