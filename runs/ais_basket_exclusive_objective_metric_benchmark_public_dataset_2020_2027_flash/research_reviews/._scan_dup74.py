# -*- coding: utf-8 -*-
import io, re, difflib, itertools, os, glob
base = "E:/github/qual-llm-check-IS-utd/runs/ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash/research_reviews"
fs = {}
for p in glob.glob(base + "/*_v3.1.md"):
    fn = os.path.basename(p)
    if fn.startswith("34_"): fs["34"] = p
    elif fn.startswith("35_"): fs["35"] = p
    elif fn.startswith("36_"): fs["36"] = p
names = ["AgentShield-Adversary","AgentShield-Anticipate","AgentShield-Detect","AttackRL-Agent","D_att","SWE-bench","AgentDojo","SWExploit","IssueTrojanBench","MalSkillBench","PPO","MDP","RLbreaker","FCV"]
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
for k in ["34","35","36"]:
    with io.open(fs[k], "r", encoding="utf-8") as fh:
        sents[k] = split_sentences(fh.read())
def sim(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()
out = io.open(base + "/_dup_sent74.txt", "w", encoding="utf-8")
pairs = []
for (k1, k2) in itertools.combinations(["34","35","36"], 2):
    for i, s1 in enumerate(sents[k1]):
        for j, s2 in enumerate(sents[k2]):
            r = sim(s1, s2)
            if r == 1.0:
                pairs.append((1.0, k1, k2, s1.strip()[:80], s2.strip()[:80]))
            elif r > 0.80:
                pairs.append((round(r,3), k1, k2, s1.strip()[:80], s2.strip()[:80]))
pairs.sort(key=lambda x: -x[0])
out.write("total pairs: %d\n\n" % len(pairs))
for r, k1, k2, a, b in pairs:
    out.write("[%s] %s-%s\n  A(%s): %s\n  B(%s): %s\n\n" % (r, k1, k2, k1, a, k2, b))
out.close()
print("done")
