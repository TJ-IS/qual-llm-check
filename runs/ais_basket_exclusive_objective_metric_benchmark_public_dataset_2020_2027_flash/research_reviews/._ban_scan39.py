import io
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md"
t = io.open(fn, encoding="utf-8").read()
for w in ["逐句","审计","旗舰","不可修改","外部层","只能做","裸","冲突","写作纪律","病毒库","弹窗","重跑"]:
    c = t.count(w)
    if c:
        i = t.find(w)
        print(w, c, "|", t[max(0,i-40):i+40].replace("\n"," "))
print("done")