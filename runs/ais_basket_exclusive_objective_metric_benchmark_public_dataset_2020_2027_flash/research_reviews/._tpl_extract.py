import re, io
base = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
files = {
 "dsdl_16409": "16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md",
 "artext_25465": "25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md",
 "acaa_28706": "28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md",
 "wolf_00790": "00790_2020_who-is-the-next-wolf-of-wall-street-detection-of-financial-intermediary-misconduct.md",
 "ampel_11686": "11686_2024_creating-proactive-cyber-threat-intelligence-with-hacker-exploit-labels-a-deep-transfer-learning.md",
}
out = io.open(r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\._tpl_intros.txt", "w", encoding="utf-8")
for key, fn in files.items():
    txt = io.open(base + "\\" + fn, encoding="utf-8").read()
    out.write("===== " + key + " =====\n")
    # print first 6000 chars as intro approximation
    out.write(txt[:6500])
    out.write("\n\n")
out.close()
print("done")