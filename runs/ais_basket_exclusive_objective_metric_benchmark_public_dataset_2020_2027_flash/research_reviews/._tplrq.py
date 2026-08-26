# -*- coding: utf-8 -*-
import io, re
out = io.open("_r76_tpl_rq.txt", "w", encoding="utf-8")
for fn, tag in [("25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md", "ARText"),
                ("16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md", "DSDL"),
                ("28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md", "ACAA"),
                ("27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md", "RADAR")]:
    p = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all\\" + fn
    t = io.open(p, encoding="utf-8").read()
    t2 = re.sub(r"\s+", " ", t)
    out.write("##### %s #####\n" % tag)
    for kw in ["research question", "research gap", "research gaps", "we raise", "the following research", "how to assess", "how to improve", "to answer", "we aim to", "we seek to"]:
        ms = list(re.finditer(re.escape(kw), t2, re.I))
        if ms:
            out.write("### KW[%s] n=%d\n" % (kw, len(ms)))
            for m in ms[:3]:
                out.write("...%s...\n" % t2[max(0,m.start()-300):m.start()+420])
    out.write("\n")
out.close()
print("done")
