# -*- coding: utf-8 -*-
import io, glob, re
rr = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
fn = glob.glob(rr + r"\34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
out = io.open(rr + r"\_ch53_34.txt","w",encoding="utf-8")
i = t.find("### 5.2")
j = t.find("### 5.4")
out.write(t[i:j] + "\n\n===== 一是/二是 counts =====\n")
for pat in ["一是","二是","三是"]:
    n = len(re.findall(pat, t))
    out.write("%s: %d\n" % (pat, n))
out.write("\n===== 8.2 节标题 =====\n")
for m in re.finditer(r"^#{2,4} 8[\.\d]*[^\n]*", t, re.M):
    out.write(m.group(0) + "\n")
out.write("\n===== 基准名出现 =====\n")
for pat in ["AgentDojo","MalSkillBench","SWExploit","IssueTrojanBench","SWE-bench"]:
    out.write("%s: %d\n" % (pat, len(re.findall(pat, t))))
out.close()
print("done")
