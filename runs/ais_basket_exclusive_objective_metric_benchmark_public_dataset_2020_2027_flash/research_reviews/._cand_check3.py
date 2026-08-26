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

# A3 范式句（三句结构差异最大）
t34 = "本文属于计算设计科学（computational design science）范式（Walls et al., 1992; Hevner et al., 2004; Rai, 2017），该范式主张以计算方法开发解决实际问题的信息技术工件，并以理论指导设计决策。"
t35 = "本文以计算设计科学（computational design science）范式为依据，开发解决实际问题的新型信息技术工件，并以理论指导设计决策（Walls et al., 1992; Hevner et al., 2004）。"
t36 = "本文遵循计算设计科学（computational design science）范式（Walls et al., 1992; Hevner et al., 2004; Rai, 2017），开发解决实际问题的信息技术工件，并以理论指导设计决策。"
print("A3:", sim(t34,t35), sim(t34,t36), sim(t35,t36))

# A4 范式句（36 完全重构）
t34b = "本文属于计算设计科学（computational design science）范式（Walls et al., 1992; Hevner et al., 2004; Rai, 2017），该范式主张以计算方法开发解决实际问题的信息技术工件，并以理论指导设计决策。"
t35b = "本文以计算设计科学（computational design science）范式为依据，开发解决实际问题的新型信息技术工件，并以理论指导设计决策（Walls et al., 1992; Hevner et al., 2004）。"
t36b = "本文遵循计算设计科学（computational design science）范式（Walls et al., 1992; Hevner et al., 2004; Rai, 2017），以计算方法开发解决实际问题的信息技术工件，设计决策均有理论依据。"
print("A4:", sim(t34b,t35b), sim(t34b,t36b), sim(t35b,t36b))

# G3 RQ总起（35 改"结合上述分析与研究缺口"）
g34 = "综合前文的理论推导与文献缺口，本文提出三个研究问题。"
g35 = "结合上述分析与研究缺口，本文提出以下研究问题。"
g36 = "综合上述理论分析与文献缺口，本文提出以下三个研究问题。"
print("G3:", sim(g34,g35), sim(g34,g36), sim(g35,g36))

# E3 数据来源
e34 = "本文使用的全部数据均来自公开资源。"
e35 = "本文所用数据均来自公开资源。"
e36 = "本文的数据均取自公开资源。"
print("E3:", sim(e34,e35), sim(e34,e36), sim(e35,e36))
