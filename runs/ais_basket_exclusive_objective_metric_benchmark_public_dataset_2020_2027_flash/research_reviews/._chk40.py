import io, re
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\40_引言逐段逐句二轮审计与模板对照改写记录.md"
t = io.open(fn, encoding="utf-8").read()
print("chars:", len(t))
print("lines:", t.count("\n"))
for h in re.findall(r"^#{1,3} .*$", t, flags=re.M):
    print(h)