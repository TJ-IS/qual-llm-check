# -*- coding: utf-8 -*-
import io, glob
out = io.open("_r76_36_72.txt", "w", encoding="utf-8")
p = glob.glob("36_*.md")[0]
lines = io.open(p, encoding="utf-8").read().split("\n")
start = end = None
for i, l in enumerate(lines):
    if "机制讨论" in l: start = i
    if start is not None and i > start and l.startswith("###") :
        end = i
        break
for n in range(start, (end or start+12)):
    out.write("%4d %s\n" % (n+1, lines[n]))
out.close()
print("done")
