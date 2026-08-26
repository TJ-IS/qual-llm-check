# -*- coding: utf-8 -*-
import io, os, re
roots = ["thesis_papers","thesis_papers_v2","thesis_papers_v3","thesis_papers_v3.1","thesis_papers_v4_trainable","thesis_papers_v5_effective_use","thesis_papers_v6_xiao_style","thesis_papers_v7_semantic_continuity","thesis_papers_v8_reliable_action"]
base = r"E:\github\qual-llm-check-IS-utd"
sym_names = {"：":"全角冒号","；":"中文分号","—":"破折号","–":"短横","——":"双破折","“":"左引号","”":"右引号","‘":"左单引","’":"右单引"}
for r in roots:
    p = os.path.join(base, r)
    if not os.path.isdir(p): 
        print(r, "MISSING"); continue
    files = sorted(os.listdir(p))
    print("====", r, len(files))
    for f in files[:12]:
        fp = os.path.join(p, f)
        try:
            t = io.open(fp, encoding="utf-8").read()
        except Exception as e:
            print("  ", f, "ERR", e); continue
        body = t.split("## 参考文献")[0] if "## 参考文献" in t else t
        hits = {}
        for ch, name in sym_names.items():
            c = body.count(ch)
            if c: hits[name] = c
        if hits:
            print("  ", f[:30], "->", hits)