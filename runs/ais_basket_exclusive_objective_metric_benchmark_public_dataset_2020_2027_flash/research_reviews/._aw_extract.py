import io, re
base = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
files = {
 "artext_25465": "25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md",
 "wolf_00790": "00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md",
}
out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._artext_wolf_intro.txt","w",encoding="utf-8")
for key, fn in files.items():
    txt = io.open(base + "\\" + fn, encoding="utf-8").read()
    m = re.search(r"#+\s*1\.\s*Introduction", txt) or re.search(r"#+\s*Introduction", txt)
    if not m:
        out.write("===== " + key + " =====\nNO INTRO HEADER FOUND\n")
        out.write(txt[:1500] + "\n\n")
        continue
    start = m.end()
    nxt = re.search(r"\n#+\s", txt[start:])
    end = start + nxt.start() if nxt else len(txt)
    blk = txt[start:end].replace("\r","")
    paras = [re.sub(r"\s+"," ",p.strip()) for p in re.split(r"\n\s*\n", blk) if p.strip()]
    out.write("===== " + key + " =====\n")
    for i,p in enumerate(paras):
        out.write(f"[P{i+1}] {p}\n\n")
    out.write("\n")
out.close()
print("done")