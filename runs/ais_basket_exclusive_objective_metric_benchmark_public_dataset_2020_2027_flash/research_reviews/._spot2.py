import io
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
t34 = io.open(base + r"\34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md", encoding="utf-8").read()
t35 = io.open(base + r"\35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md", encoding="utf-8").read()
t36 = io.open(base + r"\36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md", encoding="utf-8").read()
kws = [
 ("34", t34, "开源编码智能体亦在公开基准"),
 ("34", t34, "为实现这一目的，我们借鉴"),
 ("35", t35, "信息操纵攻击已留下可观测的线索"),
 ("35", t35, "构成有效的事前防御设计原则"),
 ("35", t35, "鉴于信息操纵攻击在任务执行前已留下可观测的线索"),
 ("36", t36, "直至任务完成（Yang et al., 2024）"),
 ("36", t36, "在编码智能体情境中，这一理论逻辑指向"),
 ("36", t36, "我们将任务执行中可观测的信息划分为三个通道"),
]
for tag, t, kw in kws:
    i = t.find(kw)
    print(f"--- {tag} [{kw}] ---")
    print(t[max(0,i-160):i+len(kw)+120].replace("\n"," "))
    print()