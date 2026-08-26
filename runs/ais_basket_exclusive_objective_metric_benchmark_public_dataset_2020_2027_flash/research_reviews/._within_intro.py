# -*- coding: utf-8 -*-
import io, re, difflib
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
def intro_sents(k):
    with io.open(FILES[k], "r", encoding="utf-8") as fh:
        text = fh.read()
    body = text.split("## 参考文献")[0]
    intro = body.split("## 二、")[0]
    intro = re.sub(r"^#{1,4}.*$", "", intro, flags=re.M)
    parts = re.split(r"(?<=[。？！])", intro)
    return [p for p in parts if len(re.sub(r"\s","",p)) >= 12]
out = io.open("._within_intro_out.txt", "w", encoding="utf-8")
for k in ["34","35","36"]:
    ss = intro_sents(k)
    out.write(f"===== {k} within-intro =====\n")
    for i in range(len(ss)):
        for j in range(i+1, len(ss)):
            r = sim(ss[i], ss[j])
            if r >= 0.60:
                out.write(f"R={r:.3f} S{i+1}/S{j+1}\n  A: {ss[i].strip()}\n  B: {ss[j].strip()}\n\n")
out.close()
print("done")