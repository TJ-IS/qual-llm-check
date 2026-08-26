# -*- coding: utf-8 -*-
import io
fn = "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()

reps = [
 ("SWExploit 通过恶意问题诱导自动修复智能体生成带漏洞补丁【占位，需核对公开出处】。",
  "SWExploit 通过恶意问题诱导自动修复智能体生成带漏洞的补丁【占位，需核对公开出处】。"),
 ("对每一类文献，我们既归纳其已确立的结论，也指出其有效边界，并据此识别研究缺口。",
  "对每一类文献，我们既归纳其已确立的结论，也指出其适用边界，并据此识别研究缺口。"),
 ("然而，这些攻击资源在支撑系统防御研究方面存在明显边界。",
  "然而，这些攻击资源在支撑系统防御研究方面存在明显局限。"),
]
for old, new in reps:
    assert t.count(old) == 1, "NOT UNIQUE or MISSING: " + old[:30]
    t = t.replace(old, new)

io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply92 done, %d replacements" % len(reps))
