# -*- coding: utf-8 -*-
import io, glob, os
out = io.open("_r76_ch4.txt", "w", encoding="utf-8")
for pre in ["34", "35", "36"]:
    p = glob.glob(pre + "_*.md")[0]
    lines = io.open(p, encoding="utf-8").read().split("\n")
    out.write("##### %s 第四章 #####\n" % pre)
    start = end = None
    for i, l in enumerate(lines):
        if l.startswith("## 四、"): start = i
        if l.startswith("## 五、") and start is not None:
            end = i
            break
    if start is not None:
        for n in range(start, (end or start+20)):
            out.write("%4d %s\n" % (n+1, lines[n]))
    out.write("\n")
out.close()
print("done")
