# -*- coding: utf-8 -*-
import io, glob, os
out = io.open("_r76_arch_ctx.txt", "w", encoding="utf-8")
for pat in ["12_*.md", "13_*.md", "14_*.md"]:
    fs = glob.glob(os.path.join("archive", pat))
    for p in fs:
        t = io.open(p, encoding="utf-8").read()
        out.write("##### %s #####\n" % os.path.basename(p))
        n = 0
        for ch, name in [("\u2014", "EMDASH"), ("\u201c", "LQ"), ("\u201d", "RQ"), ("\uff1a", "COLON")]:
            idx = 0
            shown = 0
            while True:
                i = t.find(ch, idx)
                if i < 0 or shown >= 6: break
                out.write("  %s: ...%s...\n" % (name, t[max(0,i-40):i+45].replace("\n"," / ")))
                idx = i + 1
                shown += 1
        out.write("\n")
out.close()
print("done")
