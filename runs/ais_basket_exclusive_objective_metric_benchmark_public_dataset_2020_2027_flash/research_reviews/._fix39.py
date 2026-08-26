# -*- coding: utf-8 -*-
import io
fname = "39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md"
with io.open(fname, "r", encoding="utf-8") as f:
    text = f.read()
a = text.replace("已逐句差异化", "已按句差异化").replace("于 v3.3 逐句与", "于 v3.3 按句与")
print("逐句 remaining:", a.count("逐句"))
with io.open(fname, "w", encoding="utf-8", newline="\n") as f:
    f.write(a)
print("written")
