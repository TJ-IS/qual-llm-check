import io, re
fn = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\40_引言段落句子级二轮核对与模板对照改写记录.md"
t = io.open(fn, encoding="utf-8").read()
for ch, name in [("；","中文分号"),("—","破折号"),("–","短横"),("“","左引"),("”","右引")]:
    idxs = [m.start() for m in re.finditer(re.escape(ch), t)]
    if idxs:
        print(name, len(idxs))
        for i in idxs[:8]:
            print("   ...", t[max(0,i-45):i+45].replace("\n"," "))