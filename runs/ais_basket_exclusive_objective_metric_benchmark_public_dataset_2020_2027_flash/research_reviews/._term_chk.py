import io, re
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
for fn in ["34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
           "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
           "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md"]:
    t = io.open(base + "\\" + fn, encoding="utf-8").read()
    idxs = [m.start() for m in re.finditer("信息操纵攻击", t)]
    print(fn[:12], "count:", len(idxs))
    for i in idxs[:6]:
        seg = t[max(0,i-40):i+20].replace("\n"," ")
        print("  ...", seg)
    # 术语界定句
    for kw in ["统称", "泛指", "即对手", "一类攻击", "此类攻击"]:
        for m in re.finditer(kw, t):
            seg = t[max(0,m.start()-50):m.start()+50].replace("\n"," ")
            print(f"  [{kw}] ...{seg}...")
            break