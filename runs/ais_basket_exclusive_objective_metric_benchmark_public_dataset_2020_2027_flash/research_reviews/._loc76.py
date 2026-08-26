# -*- coding: utf-8 -*-
import io, glob, os
out = io.open("_r76_locate.txt", "w", encoding="utf-8")
pats = {":": "半角冒号", "\"": "半角双引", "...": "三点省略", "|": "竖线", "/": "斜杠", "-": "连字符"}
for p in sorted(glob.glob("3[456]_*.md")):
    t = io.open(p, encoding="utf-8").read()
    ref_i = t.find("## 参考文献")
    body, refs = t[:ref_i], t[ref_i:]
    out.write("##### %s #####\n" % os.path.basename(p)[:2])
    for ch, name in pats.items():
        for label, seg, off in [("BODY", body, 0), ("REFS", refs, ref_i)]:
            idx = seg.find(ch)
            if idx >= 0:
                out.write("  %s %s first at: ...%s...\n" % (name, label, seg[max(0,idx-55):idx+70].replace("\n"," / ")))
    # count colons/quotes in refs vs body
    out.write("  半角冒号 BODY=%d REFS=%d | 半角双引 BODY=%d REFS=%d | 三点省略 BODY=%d REFS=%d | 竖线 BODY=%d REFS=%d\n" % (
        body.count(":"), refs.count(":"), body.count('"'), refs.count('"'), body.count("..."), refs.count("..."), body.count("|"), refs.count("|")))
out.close()
print("done")
