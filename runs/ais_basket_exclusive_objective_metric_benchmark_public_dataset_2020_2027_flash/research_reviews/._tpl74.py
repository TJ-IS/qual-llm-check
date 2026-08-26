# -*- coding: utf-8 -*-
import io, re, glob
base = "E:/github/qual-llm-check-IS-utd/database_fulltext_all"
files = {
 "RADAR": base + "/27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md",
 "ARText": base + "/25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md",
 "DSDL": base + "/16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md",
 "ACAA": base + "/28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md",
}
pats = [r"[^.]*rationale[^.]*\.", r"[^.]*[Dd]esign [Ss]cience[^.]*\.", r"[^.]*Gregor[^.]*\.", r"[^.]*experiment[^.]*organiz[^.]*\.", r"[^.]*First constraint[^.]*\."]
out = io.open("E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews/_tpl74.txt", "w", encoding="utf-8")
for k, f in files.items():
    t = io.open(f, encoding="utf-8").read()
    t = re.sub(r"\s+", " ", t)
    out.write("\n" + "#"*25 + " " + k + "\n")
    for pat in pats:
        ms = re.findall(pat, t)
        seen = set()
        for m in ms:
            m = m.strip()
            if m not in seen and len(m) < 400:
                seen.add(m)
                out.write("  * " + m + "\n")
out.close()
print("done")
