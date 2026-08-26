# -*- coding: utf-8 -*-
import io, glob
out = io.open("_r76_echo.txt", "w", encoding="utf-8")
kws = ["确保", "可纠正", "无约束", "为上限", "公开报告", "不应用于", "可解释", "可申诉", "以公开基准", "仅向", "受监控", "治理边界", "安全名义", "代价", "干预", "牺牲", "披露", "上限约束", "开放访问"]
for pre in ["34", "35", "36"]:
    p = glob.glob(pre + "_*.md")[0]
    t = io.open(p, encoding="utf-8").read()
    body = t.split("## 参考文献")[0]
    out.write("### %s ###\n" % pre)
    for kw in kws:
        idx = 0
        cnt = 0
        while True:
            i = body.find(kw, idx)
            if i < 0: break
            out.write("  %s: ...%s...\n" % (kw, body[max(0,i-40):i+48].replace("\n"," / ")))
            idx = i + 1
            cnt += 1
            if cnt > 8: break
out.close()
print("done")
