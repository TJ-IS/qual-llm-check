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
def split_sentences(text):
    body = text.split("## 参考文献")[0]
    body = re.sub(r"^#{1,4}.*$", "", body, flags=re.M)
    parts = re.split(r"(?<=[。？！])", body)
    return [p for p in parts if len(re.sub(r"\s","",p)) >= 12]
sents = {}
for k, f in FILES.items():
    with io.open(f, "r", encoding="utf-8") as fh:
        sents[k] = split_sentences(fh.read())

def find(k, kw):
    return [s for s in sents[k] if kw in s]

pairs = [
 ("34","36","缺陷修复、功能实现与测试维护"),
 ("34","36","直至任务完成"),
 ("34","36","一个自然的方案是"),
 ("34","36","已知已被发现"),
 ("34","36","这些研究共同表明"),
 ("34","35","终局目的"),
 ("35","36","实现这一"),
 ("34","35","实现这一"),
 ("35","36","具体地，将"),
 ("34","35","知之甚少"),
 ("35","36","知之甚少"),
 ("34","36","知之甚少"),
]
for a, b, kw in pairs:
    sa = find(a, kw)
    sb = find(b, kw)
    if not sa or not sb:
        print(f"{a}/{b} [{kw}]: 未找到 {a}={len(sa)} {b}={len(sb)}")
        continue
    for s1 in sa:
        for s2 in sb:
            r = sim(s1, s2)
            if r >= 0.7:
                print(f"R={r:.3f} {a}/{b} [{kw}]")
                print(f"  A: {s1.strip()}")
                print(f"  B: {s2.strip()}")