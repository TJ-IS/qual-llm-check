import io, re
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
# 打印 34 引言 P1 与 P4 修改段、35 P3/P7 修改句、36 P1/P4 修改段
t34 = io.open(base + r"\34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md", encoding="utf-8").read()
intro34 = t34.split("## 二、")[0]
paras34 = [p.strip() for p in re.split(r"\n\s*\n", intro34) if p.strip()]
print("=== 34 P1 ===")
print(paras34[1][:1200])
print()
print("=== 34 P4 ===")
print(paras34[4][:900])