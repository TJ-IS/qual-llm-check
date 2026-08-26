# -*- coding: utf-8 -*-
import io, re, os
out = io.open("_r76_tpl_refs.txt", "w", encoding="utf-8")
base = r"E:\github\qual-llm-check-IS-utd\database_fulltext_all"
for fn, tag in [("27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md", "RADAR"),
                ("25465_2022_assessing-and-enhancing-adversarial-robustness-of-predictive-analytics-an-empirically-tested-des.md", "ARText"),
                ("16409_2023_a-theory-driven-deep-learning-method-for-voice-chatbased-customer-response-prediction.md", "DSDL"),
                ("28706_2024_attending-to-customer-attention-a-novel-deep-learning-method-for-leveraging-multimodal-online-re.md", "ACAA")]:
    t = io.open(os.path.join(base, fn), encoding="utf-8").read()
    m = re.search(r"(?i)references?\s*$", t, re.M)
    refs = t[m.start():] if m else ""
    out.write("### %s | refs chars=%d | 全角冒号=%d 半角冒号=%d 引号=%d 破折号=%d\n" % (
        tag, len(refs), refs.count("\uff1a"), refs.count(":"), refs.count("\u201c")+refs.count("\u201d")+refs.count('"'), refs.count("\u2014")))
    # sample colon titles
    n = 0
    for mm in re.finditer(r"[A-Z][^.]{10,90}:[^.]{5,90}\.", refs):
        if n >= 4: break
        out.write("   colon-title: %s\n" % mm.group(0)[:120])
        n += 1
    # sample quoted titles
    n = 0
    for mm in re.finditer(r"\u201c[^\u201d]{3,80}\u201d|\"[^\"]{3,80}\"", refs):
        if n >= 4: break
        out.write("   quoted-title: %s\n" % mm.group(0)[:120])
        n += 1
out.close()
print("done")
