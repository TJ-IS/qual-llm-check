import io, re
def split_sent(txt):
    parts = re.split(r"(?<=[.!?])\s+", txt)
    return [p.strip() for p in parts if p.strip()]
out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._radar_sent.txt","w",encoding="utf-8")
radar = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._radar_intro_out.txt",encoding="utf-8").read()
# intro ends before "## Research Background"
intro = radar.split("## Research Background")[0]
intro = intro.replace("## Introduction","").strip()
# split paragraphs by double newline or by markers
paras = [p.strip() for p in re.split(r"\n\s*\n", intro) if p.strip()]
for pi,p in enumerate(paras,1):
    out.write(f"--- RADAR P{pi} ---\n")
    for si,s in enumerate(split_sent(p),1):
        out.write(f"S{si}: {s}\n")
out.close()
print("ok")