# -*- coding: utf-8 -*-
import io
fn = "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md"
t = io.open(fn, encoding="utf-8", newline="").read()
old = "攻击者必须在任务执行前完成恶意内容植入，攻击痕迹在任务开始前已经存在。"
new = "攻击者必须在任务执行前完成恶意内容植入，攻击线索在任务开始前已经存在。"
assert t.count(old) == 1
t = t.replace(old, new)
io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("apply96 done")
