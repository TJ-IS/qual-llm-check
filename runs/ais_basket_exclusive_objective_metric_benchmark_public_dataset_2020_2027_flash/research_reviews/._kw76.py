# -*- coding: utf-8 -*-
import io, glob, os
out = io.open("_r76_kw.txt", "w", encoding="utf-8")
for pre in ["34", "35", "36"]:
    p = glob.glob(pre + "_*.md")[0]
    t = io.open(p, encoding="utf-8").read()
    body = t.split("## 参考文献")[0]
    out.write("### %s ###\n" % pre)
    for kw in ["实质", "简化假设", "结构价值", "上限", "治理边界", "人工审查", "人工复核", "可申诉", "安全相关信号"]:
        idx = 0
        cnt = 0
        while True:
            i = body.find(kw, idx)
            if i < 0: break
            out.write("  %s: ...%s...\n" % (kw, body[max(0,i-45):i+55].replace("\n"," / ")))
            idx = i + 1
            cnt += 1
            if cnt > 6: break
out.write("\n##### ARCHIVE #####\n")
for fn in sorted(os.listdir("archive")):
    out.write(fn + "\n")
out.close()
print("done")
