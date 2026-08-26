# -*- coding: utf-8 -*-
import io

edits = {
 "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md": [
   ("在公开基准 SWE-bench Verified 上，主流编码智能体的真实问题修复成功率",
    "以公开基准 SWE-bench Verified 为例，主流编码智能体的真实问题修复成功率"),
 ],
 "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md": [
   ("并在编码智能体部署上投入日益增长的防御资源", "并为此投入日益增长的防御资源"),
   ("恶意问题描述穿透现有防护机制的比例相当可观",
    "例如，恶意问题描述穿透现有防护机制的比例相当可观"),
 ],
 "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md": [
   ("承担日益关键的执行角色，自动化缺陷修复", "承担日益关键的执行角色，负责自动化缺陷修复"),
   ("给定问题描述与仓库上下文，编码智能体在任务执行中依次读取文件、编辑代码、运行测试与调用工具，直至任务完成",
    "在给定问题描述与仓库上下文之后，编码智能体于任务执行中依次读取文件、编辑代码、运行测试与调用工具，直至任务完成"),
   ("恶意问题描述可穿透输入侧防护", "例如，恶意问题描述可穿透输入侧防护"),
 ],
}

for fname, pairs in edits.items():
    with io.open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    for old, new in pairs:
        cnt = text.count(old)
        assert cnt == 1, (fname, old[:20], cnt)
        text = text.replace(old, new)
    with io.open(fname, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("done", fname[:20])
