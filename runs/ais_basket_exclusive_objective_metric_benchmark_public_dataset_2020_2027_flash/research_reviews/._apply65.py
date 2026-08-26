# -*- coding: utf-8 -*-
import io
p = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md"
t = io.open(p, encoding="utf-8").read()

edits = [
    # M6 2.4 P3 桥接句：去掉形式化缺口名“评估基础设施缺口”，只保留节内真值所指
    ("正是对这一评估基础设施缺口的直接回应。", "正是对这一真值缺失问题的直接回应。"),
    # M1+M5 2.5 S1 吸收IS整合缺口，S6“此外”句整体删除
    ("综合以上文献，编码智能体攻击生成存在三个相互关联的缺口。",
     "综合上述文献，编码智能体攻击生成存在三个相互关联的缺口，且现有研究均未以设计科学方法在编码智能体情境中整合相关范式。"),
    # M2 2.5 S3 删除括号（与引言第五段、2.3节第二段、句内“覆盖多通道”重复）
    ("其在编码智能体情境（内容级语义操纵、多通道信息环境）中的适用性尚未被研究。",
     "其在编码智能体情境中的适用性尚待研究。"),
    # M3 2.5 S4 换词避免与引言第四段、7.1节重复
    ("攻击实例彼此孤立地散布于多个基准（Yang et al., 2024），统一的攻击分类学与攻击面地图尚未建立，防御投入的优先级无从确定。",
     "攻击实例零散分布于多个基准（Yang et al., 2024），统一的攻击分类学与攻击面地图尚未建立，防御投入的优先次序无从确定。"),
    # M4 2.5 S5 换词避免与引言第五段、2.1节第三段、2.4节第三段、引言第四段及5.5/6/7.1节重复
    ("缺乏带统一真值标注的攻击基准，防御算法无法在统一压力测试下比较（Li & Chai, 2022）。",
     "攻击基准缺少一致的成功真值，防御算法难以在相同压力条件下比较（Li & Chai, 2022）。"),
    # M5 删除“此外”句（被M1吸收）
    ("此外，IS 文献虽然已确立以强化学习开发攻击侧工件的范式（Ebrahimi et al., 2025; Kwon & Lee, 2024），以及数据操纵与数据效用权衡的分析框架（Ghoshal et al., 2020; Menon et al., 2022），但这些范式与框架均未在编码智能体情境中得到整合。",
     ""),
]

for old, new in edits:
    c = t.count(old)
    if c != 1:
        print("SKIP/ERR count=%d : %s" % (c, old[:40]))
        continue
    t = t.replace(old, new)
    print("OK : %s" % old[:40])

io.open(p, "w", encoding="utf-8", newline="").write(t)
print("saved")
