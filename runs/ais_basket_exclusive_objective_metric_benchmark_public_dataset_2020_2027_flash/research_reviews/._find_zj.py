# -*- coding: utf-8 -*-
import io
with io.open("39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, ln in enumerate(lines, 1):
    if "逐句" in ln:
        print(i, ln.strip()[:120])
