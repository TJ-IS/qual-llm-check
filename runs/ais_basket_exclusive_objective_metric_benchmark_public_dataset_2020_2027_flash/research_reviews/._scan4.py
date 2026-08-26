# -*- coding: utf-8 -*-
import io, re, difflib, itertools
files = {
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
out = io.open("._scan_result2.txt", "w", encoding="utf-8")
ident, near = 0, 0
for (k1, k2) in itertools.combinations(["34","35","36"], 2):
    for s1 in sents[k1]:
        for s2 in sents[k2]:
            r = sim(s1, s2)
            if r >= 0.82:
                tag = "ID" if r >= 0.999 else "N"
                if r >= 0.999: ident += 1
                else: near += 1
                out.write("R=%.3f %s %s/%s\n  A: %s\n  B: %s\n\n" % (r, tag, k1, k2, s1.strip(), s2.strip()))
out.close()
print("identical:", ident, " near(>=0.82):", near)
