# -*- coding: utf-8 -*-
import io, glob
fn = glob.glob("34_*.md")[0]
t = io.open(fn, encoding="utf-8").read()
pairs = [
 ("威胁模型刻画攻击者目标、可用通道、操纵载体与手法以及预算约束",
  "威胁模型刻画攻击通道、操纵载体与手法以及攻击预算与功能保持约束"),
 ("编码智能体的信息环境由问题描述、仓库文件与工具描述构成",
  "编码智能体的信息环境由问题描述、仓库文件以及工具与技能描述构成"),
]
for old, new in pairs:
    n = t.count(old)
    assert n == 1, (old, n)
    t = t.replace(old, new)
io.open(fn, "w", encoding="utf-8", newline="").write(t)
print("ok")
