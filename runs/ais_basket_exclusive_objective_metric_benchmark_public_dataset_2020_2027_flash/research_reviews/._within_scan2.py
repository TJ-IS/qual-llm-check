import re, itertools, os
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
names = ["AgentShield-Adversary","AgentShield-Anticipate","AgentShield-Detect","AttackRL-Agent","D_att","SWE-bench","AgentDojo","SWExploit","MalSkillBench","PPO","MDP"]
def norm(s):
    for n in names: s = s.replace(n, 'A')
    s = s.replace('【占位】','P').replace('【占位，','P，').replace('】','')
    return re.sub(r'\s+','',s)
def split_sents(sec):
    return [x for x in re.split(r'(?<=[。！？])', sec) if len(x) >= 12]
from difflib import SequenceMatcher
for n, fn in files.items():
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    secs = [s for s in re.split(r'\n(?=#)', main) if s.strip()]
    sents = []
    for s in secs:
        body = re.sub(r'^#+ .*$', '', s, flags=re.M)
        for x in split_sents(body):
            sents.append((norm(x), x.strip()))
    flagged = []
    for (a, ra), (b, rb) in itertools.combinations(sents, 2):
        sim = SequenceMatcher(None, a, b).ratio()
        if sim >= 0.82:
            flagged.append((round(sim,3), ra[:70], rb[:70]))
    print(f'== {n}: 篇内跨节 >=0.82 共 {len(flagged)} 对')
    for sim, ra, rb in flagged:
        print(f'  {sim} | {ra} ||| {rb}')
