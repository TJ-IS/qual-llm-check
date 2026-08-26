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
t34 = "本文属于计算设计科学（computational design science）范式，该范式主张以计算方法开发解决实际问题的信息技术工件，并以理论指导设计决策（Walls et al., 1992; Hevner et al., 2004; Rai, 2017）。"
t35 = "本文以计算设计科学（computational design science）范式为依据，开发解决实际问题的新型信息技术工件，并以理论指导设计决策（Walls et al., 1992; Hevner et al., 2004）。"
t36 = "本文遵循计算设计科学（computational design science）范式，以计算方法开发解决实际问题的信息技术工件，设计决策均有理论依据（Walls et al., 1992; Hevner et al., 2004; Rai, 2017）。"
print("A5 范式句:", round(sim(t34,t35),3), round(sim(t34,t36),3), round(sim(t35,t36),3))
# E4
e34 = "本文使用的全部数据均来自公开资源。"
e35 = "本文所用的数据均来自公开资源。"
e36 = "本文的数据均取自公开资源。"
print("E4 数据来源:", round(sim(e34,e35),3), round(sim(e34,e36),3), round(sim(e35,e36),3))
