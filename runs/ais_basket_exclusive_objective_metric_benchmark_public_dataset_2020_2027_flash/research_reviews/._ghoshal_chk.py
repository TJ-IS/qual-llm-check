import io, re, glob
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
kws = ["Ghoshal", "Menon", "可用性与安全性"]
for fn in ["12_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模.md",
           "16_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v2.md",
           "31_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.md",
           "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
           "28_论文一v3_逐段对照重写记录.md",
           "11_三研究_预期结果讨论贡献_对标IS权威文献逐句审计.md"]:
    try:
        t = io.open(base + "\\" + fn, encoding="utf-8").read()
    except Exception as e:
        print(fn, "ERR", e); continue
    print("="*20, fn)
    for kw in kws:
        for m in re.finditer(re.escape(kw), t):
            s = max(0, m.start()-60); e_ = min(len(t), m.end()+60)
            seg = t[s:e_].replace("\n", " ")
            print(f"[{kw}] ...{seg}...")
            break