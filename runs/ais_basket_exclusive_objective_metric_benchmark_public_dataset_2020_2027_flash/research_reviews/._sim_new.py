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
def sents(fn):
    t = open(fn, encoding='utf-8').read()
    main = t.split('## 参考文献')[0]
    body = re.sub(r'^#+ .*$', '', main, flags=re.M)
    return [(norm(x), x.strip()) for x in re.split(r'(?<=[。！？])', body) if len(x) >= 12]
new = 'Yang 等（2023b）在金融风险预测中示范了理论驱动设计的完整路径，将沟通理论构念落实为模型输入与结构的可操作定义，为理论到工件的转化提供了参照。'
nn = norm(new)
for n in ['34','35']:
    best = []
    for sn, raw in sents(files[n]):
        r = SequenceMatcher(None, nn, sn).ratio()
        if r >= 0.5:
            best.append((round(r,3), raw[:80]))
    best.sort(reverse=True)
    print(f'--- 新句 vs {n} 最高相似句:')
    for r, raw in best[:3]:
        print(f'  {r} | {raw}')
