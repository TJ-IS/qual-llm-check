import io, re
base = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
files = {
 "dsdl_16409": "16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md",
 "artext_25465": "25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md",
 "acaa_28706": "28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md",
 "wolf_00790": "00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md",
 "ampel_11686": "11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md",
}
def intro_block(txt):
    # find the introduction heading (## 1. Introduction / ## Introduction)
    m = re.search(r"#+\s*1\.\s*Introduction", txt)
    if not m:
        m = re.search(r"#+\s*Introduction", txt)
    if not m:
        return None, txt[:200]
    start = m.end()
    # find next heading level 1 or 2
    nxt = re.search(r"\n#+\s", txt[start:])
    end = start + nxt.start() if nxt else len(txt)
    return txt[start:end], None

out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._tpl_intro_blocks.txt","w",encoding="utf-8")
for key, fn in files.items():
    txt = io.open(base + "\\" + fn, encoding="utf-8").read()
    blk, err = intro_block(txt)
    out.write("===== " + key + " =====\n")
    if err: out.write("ERR: " + err + "\n")
    else:
        # collapse whitespace into paragraphs
        blk = blk.replace("\r","")
        paras = [p.strip() for p in re.split(r"\n\s*\n", blk) if p.strip()]
        for i,p in enumerate(paras):
            p2 = re.sub(r"\s+"," ",p)
            out.write(f"[P{i+1}] {p2}\n\n")
    out.write("\n")
out.close()
print("done")