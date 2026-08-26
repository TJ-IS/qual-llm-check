# -*- coding: utf-8 -*-
import re, difflib
def norm(s):
    s = re.sub(r"【[^】]*】", "", s)
    s = re.sub(r"（[^）]*）", "", s)
    s = re.sub(r"\s+", "", s)
    return s
def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
s34 = "给定问题描述与仓库上下文，编码智能体能够自主规划并执行读取文件、编辑代码、运行测试、调用工具等动作，直至完成任务（Yang et al., 2024）。"
variants = {
 "B": "给定问题描述与仓库上下文，编码智能体在任务执行中依次执行读取文件、编辑代码、运行测试与调用工具，直至任务完成（Yang et al., 2024）。",
 "D": "在给定问题描述与仓库上下文之后，编码智能体于任务执行中依次读取文件、编辑代码、运行测试与调用工具，直至任务完成（Yang et al., 2024）。",
 "E": "给定问题描述与仓库上下文，编码智能体在任务执行中依次进行文件读取、代码编辑、测试运行与工具调用，直至任务完成（Yang et al., 2024）。",
 "F": "在给定问题描述与仓库上下文后，编码智能体于任务执行中依次读取文件、编辑代码、运行测试与调用工具，直至任务完成（Yang et al., 2024）。",
}
for k, v in variants.items():
    print(k, round(sim(s34, v), 4), v[:40])
