# -*- coding: utf-8 -*-
import io
fn = "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()
old = "上述文献缺口与理论推导共同表明，编码智能体防御研究依赖系统化的攻击生成与威胁建模，本文据此提出以下三个研究问题。"
new = "上述文献缺口与理论推导共同表明，编码智能体防御研究依赖系统化的攻击生成、威胁建模与带真值的攻击基准，本文据此提出以下三个研究问题。"
assert t.count(old) == 1
t = t.replace(old, new)
io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply93 done")
