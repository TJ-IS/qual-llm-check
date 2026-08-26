# -*- coding: utf-8 -*-
import re, difflib
names = ["AgentShield-Adversary","AgentShield-Anticipate","AgentShield-Detect","AttackRL-Agent","D_att","SWE-bench","AgentDojo","SWExploit","IssueTrojanBench","MalSkillBench","PPO","MDP"]
def norm(s):
    s = re.sub(r"【[^】]*】", "P", s)
    s = re.sub(r"\s+", "", s)
    for n in names:
        s = s.replace(n, "A")
    return s
def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
def check(label, triples):
    keys = list(triples.keys())
    bad = []
    for i in range(len(keys)):
        for j in range(i+1, len(keys)):
            r = sim(triples[keys[i]], triples[keys[j]])
            if r >= 0.82: bad.append("%s-%s:%.3f" % (keys[i], keys[j], r))
    print(label, "=>", "ALL OK" if not bad else bad)

check("A2 范式句", {
 "34": "本文属于计算设计科学（computational design science）范式（Walls et al., 1992; Hevner et al., 2004; Rai, 2017），该范式主张以计算方法开发解决实际问题的信息技术工件，并以理论指导设计决策。",
 "35": "本文基于计算设计科学（computational design science）范式，以计算方法开发解决实际问题的新型信息技术工件，并以理论指导设计决策（Walls et al., 1992; Hevner et al., 2004; Rai, 2017）。",
 "36": "本文遵循计算设计科学（computational design science）范式，以计算方法开发解决实际问题的信息技术工件，设计决策均有理论依据（Walls et al., 1992; Hevner et al., 2004; Rai, 2017）。",
})
check("G2 RQ总起", {
 "34": "综合前文的理论推导与文献缺口，本文提出三个研究问题。",
 "35": "由理论分析与文献缺口出发，本文提出以下研究问题。",
 "36": "综合上述理论分析与文献缺口，本文提出以下三个研究问题。",
})
check("N2 8.3(1)", {
 "35": "（1）核心结论以相对比较报告（预置前后、与基线的差异），不依赖单一绝对数字。",
 "36": "（1）结论报告采用相对比较方式（与基线的差异），不依赖单一绝对数字。",
})
check("O3 知识库贡献", {
 "34": "本文对信息系统知识库的贡献主要有三点。",
 "35": "对信息系统知识库而言，本文的贡献包括三个方面。",
 "36": "就信息系统知识库而言，本文的贡献可归纳为三点。",
})
check("C2 图1", {
 "34": "AgentShield-Adversary 的整体架构如图 1 所示。",
 "35": "图 1 勾勒了 AgentShield-Anticipate 的整体架构。",
 "36": "图 1 呈现 AgentShield-Detect 的整体架构。",
})
check("E2 数据来源", {
 "34": "本文使用的全部数据均来自公开资源。",
 "35": "本文所用数据全部来自公开资源。",
 "36": "本文所用数据均取自公开资源。",
})
