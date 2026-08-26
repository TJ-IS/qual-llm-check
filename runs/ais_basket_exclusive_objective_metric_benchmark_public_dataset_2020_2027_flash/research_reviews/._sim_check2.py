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
s36_old = "给定问题描述与仓库上下文，编码智能体在任务执行中依次读取文件、编辑代码、运行测试与调用工具，直至任务完成（Yang et al., 2024）。"
s36_new = "给定问题描述与仓库上下文后，编码智能体在任务执行中依次执行读取文件、编辑代码、运行测试与调用工具等动作，直至任务完成（Yang et al., 2024）。"
print("34 vs 36改前:", sim(s34, s36_old))
print("34 vs 36改后:", sim(s34, s36_new))
