import io, re
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
for fn in ["34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
           "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
           "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md"]:
    t = io.open(base + "\\" + fn, encoding="utf-8").read()
    body = t.split("## 参考文献")[0]
    print("="*10, fn[:14])
    for m in re.finditer(r"^#{2,3} .*$", body, flags=re.M):
        line = m.group(0)
        # 统计该节下段落数（粗略）
        print(" ", line)