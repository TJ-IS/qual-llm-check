# -*- coding: utf-8 -*-
import io, glob
out = io.open("_r76_ethics.txt", "w", encoding="utf-8")
for pre in ["34", "35", "36"]:
    p = glob.glob(pre + "_*.md")[0]
    lines = io.open(p, encoding="utf-8").read().split("\n")
    out.write("##### %s 伦理 #####\n" % pre)
    start = end = None
    for i, l in enumerate(lines):
        if ("伦理" in l and l.startswith("###")): start = i
        if start is not None and i > start and l.startswith("## ") :
            end = i
            break
    if start is not None:
        for n in range(start, (end or start+6)):
            out.write("%4d %s\n" % (n+1, lines[n]))
    out.write("\n")
# RADAR ethics
r = io.open(r"E:\github\qual-llm-check-IS-utd\database_fulltext_all\27598_2025_radar-a-framework-for-developing-adversarially-robust-cyber-defense-ai-agents-with-deep-reinforc.md", encoding="utf-8").read()
import re
r2 = re.sub(r"\s+", " ", r)
out.write("##### RADAR ethics #####\n")
for kw in ["ethical", "Ethical", "precaution", "misuse", "abuse", "dual"]:
    ms = list(re.finditer(re.escape(kw), r2))
    if ms:
        out.write("### KW[%s] n=%d\n" % (kw, len(ms)))
        for m in ms[:3]:
            out.write("...%s...\n" % r2[max(0,m.start()-260):m.start()+330])
out.close()
print("done")
