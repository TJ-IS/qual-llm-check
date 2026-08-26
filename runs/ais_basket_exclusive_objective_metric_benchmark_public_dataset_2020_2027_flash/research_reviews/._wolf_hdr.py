import io, re
fn = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all\00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md"
txt = io.open(fn, encoding="utf-8").read()
m = re.search(r"## 1 Introduction", txt)
nxt = re.search(r"\n#+\s", txt[m.end():])
end = m.end() + nxt.start() if nxt else len(txt)
blk = txt[m.end():end].replace("\r","")
paras = [re.sub(r"\s+"," ",p.strip()) for p in re.split(r"\n\s*\n", blk) if p.strip()]
out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._wolf_intro.txt","w",encoding="utf-8")
for i,p in enumerate(paras):
    out.write(f"[P{i+1}] {p}\n\n")
out.close()
print(len(paras), "paragraphs")