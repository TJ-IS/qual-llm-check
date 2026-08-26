import re, itertools
from difflib import SequenceMatcher
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
def collect(fn):
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    out = []
    for m in re.finditer(r'^#{2,3} [^\n]+', main, re.M):
        start = m.end()
        nxt = re.search(r'^#{2,3} ', main[m.end():], re.M)
        end = m.end() + nxt.start() if nxt else len(main)
        sec = main[start:end]
        sec_norm = norm(sec)
        out.append((m.group(0), sec_norm, sec))
    return out
for n, fn in files.items():
    secs = collect(fn)
    flagged = []
    for (h1, a, ra), (h2, b, rb) in itertools.combinations(secs, 2):
        sim = SequenceMatcher(None, a, b).ratio()
        if sim >= 0.60:
            flagged.append((round(sim,3), h1, h2))
    print(f'== {n}: 章节级 >=0.60 的 {len(flagged)} 对')
    for sim, h1, h2 in sorted(flagged, reverse=True)[:10]:
        print(f'   {sim} | {h1[:30]} <-> {h2[:30]}')
