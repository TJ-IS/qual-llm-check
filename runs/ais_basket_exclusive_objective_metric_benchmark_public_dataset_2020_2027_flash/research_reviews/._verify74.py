# -*- coding: utf-8 -*-
import io, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
targets = {
 "34": ["SWExploit 的恶意问题模板", "通道选择、内容生成与结果反馈构成循环", "用于编码智能体对抗攻击的系统化生成与威胁建模", "在同一基准上修复了约"],
 "35": ["（问题文本、仓库结构、工具元数据）", "可靠的设计理由是", "本文的预期实验结果揭示了事前防御", "随后在第 5 节", "把 IS 预测与优化文献的方法论置于"],
 "36": ["信息操纵理论（information manipulation theory）", "设计理由的可靠性是", "检测与门控后的完成率损失被限制在", "一并放行", "先在第 4 节形式化研究问题", "实验二关注本文方法的实践效用", "把对正常开发任务的干扰降到最低", "公开攻击基准，D_att 仅作"],
}
out = io.open(base + "/_verify74.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    t = io.open(fs[k], encoding="utf-8").read()
    for pat in targets.get(k, []):
        c = t.count(pat)
        out.write("%s | %s | %d 次\n" % (k, pat, c))
out.close()
print("done")
