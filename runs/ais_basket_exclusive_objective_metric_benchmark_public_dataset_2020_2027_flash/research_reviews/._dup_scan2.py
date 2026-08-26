# -*- coding: utf-8 -*-
import io, re, difflib, itertools

files = {
 "34": "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
 "35": "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
 "36": "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md",
}
names = ["AgentShield-Adversary","AgentShield-Anticipate","AgentShield-Detect","AttackRL-Agent","D_att","SWE-bench","AgentDojo","SWExploit","IssueTrojanBench","MalSkillBench","PPO","MDP"]
def norm(s):
    s = re.sub(r"【[^】]*】", "P", s)  # 占位→P
    s = re.sub(r"\s+", "", s)
    for n in names:
        s = s.replace(n, "A")
    return s

def split_sentences(text):
    body = text.split("## 参考文献")[0]
    body = re.sub(r"^#.*$", "", body, flags=re.M)
    body = re.sub(r"^##.*$", "", body, flags=re.M)
    body = re.sub(r"^###.*$", "", body, flags=re.M)
    parts = re.split(r"(?<=[。？！])", body)
    return [p for p in parts if len(re.sub(r"\s","",p)) >= 12]

sents = {}
for k, f in files.items():
    with io.open(f, "r", encoding="utf-8") as fh:
        sents[k] = split_sentences(fh.read())

def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()

identical, near = [], []
for (k1, k2) in itertools.combinations(["34","35","36"], 2):
    for s1 in sents[k1]:
        for s2 in sents[k2]:
            r = sim(s1, s2)
            if r == 1.0:
                identical.append((k1, k2, s1.strip()[:70], s2.strip()[:70]))
            elif r > 0.82:
                near.append((round(r,3), k1, k2, s1.strip()[:70], s2.strip()[:70]))
print("identical:", len(identical))
for x in identical: print("  ID:", x)
print("near >0.82:", len(near))
for x in sorted(near, reverse=True): print("  N:", x)
