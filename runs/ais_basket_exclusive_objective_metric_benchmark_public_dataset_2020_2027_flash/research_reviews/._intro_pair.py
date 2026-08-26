# -*- coding: utf-8 -*-
import io, re, difflib, itertools
FILES = {
 "34": "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
 "35": "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
 "36": "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md",
}
names = ["AgentShield-Adversary","AgentShield-Anticipate","AgentShield-Detect","AttackRL-Agent","D_att","SWE-bench","AgentDojo","SWExploit","IssueTrojanBench","MalSkillBench","PPO","MDP"]
def norm(s):
    s = re.sub(r"【[^】]*】", "P", s)
    s = re.sub(r"\s+", "", s)
    for n in names:
        s = s.replace(n, "A")
    return s
def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
def split_sentences(text):
    body = text.split("## 参考文献")[0]
    body = re.sub(r"^#{1,4}.*$", "", body, flags=re.M)
    parts = re.split(r"(?<=[。？！])", body)
    return [p for p in parts if len(re.sub(r"\s","",p)) >= 12]
sents = {}
for k, f in FILES.items():
    with io.open(f, "r", encoding="utf-8") as fh:
        sents[k] = split_sentences(fh.read())
# intro only: first N sentences (34:8段, 35:7段, 36:8段) - approximate by taking until "## 二、"
def intro_sents(k):
    with io.open(FILES[k], "r", encoding="utf-8") as fh:
        text = fh.read()
    body = text.split("## 参考文献")[0]
    intro = body.split("## 二、")[0]
    intro = re.sub(r"^#{1,4}.*$", "", intro, flags=re.M)
    parts = re.split(r"(?<=[。？！])", intro)
    return [p for p in parts if len(re.sub(r"\s","",p)) >= 12]
out = io.open("._intro_pair_out.txt", "w", encoding="utf-8")
for (k1, k2) in itertools.combinations(["34","35","36"], 2):
    s1s, s2s = intro_sents(k1), intro_sents(k2)
    out.write(f"===== {k1} vs {k2} =====\n")
    for s1 in s1s:
        for s2 in s2s:
            r = sim(s1, s2)
            if r >= 0.60:
                out.write(f"R={r:.3f}\n  A[{k1}]: {s1.strip()}\n  B[{k2}]: {s2.strip()}\n\n")
out.close()
print("done, pairs >=0.60 written")