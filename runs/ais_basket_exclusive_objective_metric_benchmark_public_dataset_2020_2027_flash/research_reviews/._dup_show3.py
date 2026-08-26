# -*- coding: utf-8 -*-
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
def sents_with_sec(fn):
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    out = []
    hd = '?'
    for line in main.split('\n'):
        if re.match(r'^#{2,3} ', line):
            hd = line.strip(); continue
        if not line.strip(): continue
        for s in re.split(r'(?<=[。！？])', line):
            s = s.strip()
            if len(s) >= 15:
                out.append((hd, norm(s), s))
    return out
for n, fn in files.items():
    ss = sents_with_sec(fn)
    for (h1,a,r1),(h2,b,r2) in itertools.combinations(ss, 2):
        if h1 == h2: continue
        if re.match(r'^RQ\d', r1) or re.match(r'^RQ\d', r2): continue
        sim = SequenceMatcher(None, a, b).ratio()
        if sim >= 0.82:
            print(f'{n} {round(sim,3)} | {h1[:16]} <-> {h2[:16]}')
            print(f'  A: {r1}')
            print(f'  B: {r2}')
