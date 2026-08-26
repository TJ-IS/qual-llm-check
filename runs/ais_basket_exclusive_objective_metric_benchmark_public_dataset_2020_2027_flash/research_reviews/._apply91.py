# -*- coding: utf-8 -*-
import io
fn = "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()

reps = [
 ("针对上述缺口，本文提出三个研究问题。其一，如何系统化地生成覆盖多通道、可迁移、能逃避现有防护的编码智能体对抗攻击？其二，如何刻画编码智能体攻击面在通道、载体与手法上的脆弱性分布？其三，如何构建带真值标注、可支撑防御算法系统评估的公开攻击基准？为回答这些问题，本文基于计算设计科学范式（Gregor & Hevner, 2013; Rai, 2017），设计并开发了强化学习驱动的编码智能体对抗攻击仿真框架 AgentShield-Adversary。",
  "针对上述缺口，本文提出三个研究问题，分别对应攻击生成、攻击面刻画与攻击基准构建。为回答这些问题，本文基于计算设计科学范式（Gregor & Hevner, 2013; Rai, 2017），设计并开发了强化学习驱动的编码智能体对抗攻击仿真框架 AgentShield-Adversary。"),
 ("模板化方法无法覆盖通道、载体与操纵手法的组合空间。",
  "模板化方法无法覆盖通道、载体与手法的组合空间。"),
 ("操纵载体与手法（改写、注入、篡改）以及攻击预算与功能保持约束（修改步数上限、任务可执行性）。",
  "操纵载体与手法（改写、注入、篡改、组合）以及攻击预算与功能保持约束（修改步数上限、任务可执行性）。"),
]
for old, new in reps:
    assert t.count(old) == 1, "NOT UNIQUE or MISSING: " + old[:30]
    t = t.replace(old, new)

io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply91 done, %d replacements" % len(reps))
