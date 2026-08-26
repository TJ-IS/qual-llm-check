# -*- coding: utf-8 -*-
import io
fn = "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()

reps = [
 ("每类文献的综述均以指出其有效边界收束，研究缺口据此识别。",
  "每类文献的综述均以指出其适用边界收束，研究缺口据此识别。"),
 ("预测组件刻画不确定性，优化组件在约束下将预测转化为决策。预测与处方必须协同，没有预测，分配决策缺乏风险依据。",
  "预测组件刻画不确定性，优化组件在约束下将预测转化为决策。预测与优化必须协同，没有预测，分配决策缺乏风险依据。"),
 ("综合上述缺口，本文在第 4 节形式化研究问题，随后在第 5 节开发并详述 AgentShield-Anticipate 框架。",
  "基于上述缺口，本文在第 4 节形式化研究问题，随后在第 5 节开发并详述 AgentShield-Anticipate 框架。"),
]
for old, new in reps:
    assert t.count(old) == 1, "NOT UNIQUE or MISSING: " + old[:30]
    t = t.replace(old, new)

io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply95 done, %d replacements" % len(reps))
