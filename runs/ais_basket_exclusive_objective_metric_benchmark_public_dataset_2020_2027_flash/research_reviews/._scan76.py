# -*- coding: utf-8 -*-
import io, glob, os
out = io.open("_r76_allsym.txt", "w", encoding="utf-8")
syms = {
 "\u2014":"破折号EM", "\u2013":"短横EN", "-":"连字符HY", "\u2015":"横线BAR",
 "\u300a":"书名号《", "\u300b":"书名号》",
 "\uff1a":"全角冒号", ":":"半角冒号",
 "\uff1b":"全角分号", ";":"半角分号",
 "\u201c":"左双引", "\u201d":"右双引", "\u2018":"左单引", "\u2019":"右单引", "\"":"半角双引",
 "\u2026":"省略号", "...":"三点省略",
 "\u2192":"箭头R", "\u2190":"箭头L", "\u21d2":"箭头D",
 "\uff08":"全角左括", "\uff09":"全角右括",
 "&":"与号", "/":"斜杠", "|":"竖线", "\\":"反斜杠",
}
def scan(path, tag):
    t = io.open(path, encoding="utf-8").read()
    hits = {}
    for ch, name in syms.items():
        c = t.count(ch)
        if c: hits[name] = c
    out.write("### %s | %s | %d chars\n" % (tag, os.path.basename(path), len(t)))
    if hits:
        for name, c in sorted(hits.items(), key=lambda x:-x[1]):
            out.write("   %s x%d\n" % (name, c))
    else:
        out.write("   (no symbols)\n")
    return t
for p in sorted(glob.glob("3[456]_*.md")):
    scan(p, "BODY")
for p in sorted(glob.glob("archive/*.md")):
    scan(p, "ARCHIVE")
out.close()
print("done")
