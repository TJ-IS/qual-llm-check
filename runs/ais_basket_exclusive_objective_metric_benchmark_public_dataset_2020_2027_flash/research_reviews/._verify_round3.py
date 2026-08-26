import io, re
base = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
t = io.open(base + r"\35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md", encoding="utf-8").read()
body = t.split("## 参考文献")[0]
print("35 信息操纵攻击 count:", body.count("信息操纵攻击"))
for m in re.finditer("信息操纵攻击", body):
    seg = body[max(0,m.start()-50):m.start()+25].replace("\n"," ")
    print(" ...", seg)
print()
t34 = io.open(base + r"\34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md", encoding="utf-8").read()
print("34 开源句:", "开源编码智能体亦在公开基准上展现出有竞争力的修复能力" in t34)
print("34 桥接句:", "为实现这一目的，我们借鉴鲁棒优化与强化学习两种理论" in t34)
t35 = t
print("35 收束句:", "由此，在危害发生之前识别风险并预置干预动作，构成有效的事前防御设计原则" in t35)
print("35 鉴于句:", "鉴于信息操纵攻击在任务执行前已留下可观测的线索（Yang et al., 2024）" in t35)
t36 = io.open(base + r"\36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md", encoding="utf-8").read()
print("36 Lausen 篇内重复已删:", "Lausen 等（2020）在金融中介不当行为检测中按外部验证级别递增组织特征集" not in t36)
print("36 Lausen 仍保留于综述段:", "在不当行为检测情境中，Lausen 等（2020）证明按外部验证级别递增组织的特征集" in t36)