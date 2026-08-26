# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
def clean(text):
    body = text.split('## 参考文献')[0]
    body = re.sub(r'【占位[^】]*】', 'P', body)
    body = re.sub(r'[（(][^）)]*\d{4}[^）)]*[）)]', 'C', body)
    body = re.sub(r'AgentShield-[A-Za-z-]+', 'A', body)
    body = re.sub(r'D_att', 'D', body)
    body = re.sub(r'AttackRL-Agent', 'R', body)
    return body
texts = {k: clean(io.open(os.path.join(DIR, f), encoding='utf-8').read()) for k, f in files.items()}
out = []
# 单篇内部重复
for k, t in texts.items():
    n = len(t)
    seen = {}
    for i in range(n-16):
        s = t[i:i+16]
        if 'P' in s or 'C' in s or 'A' in s or 'D' in s or 'R' in s: continue
        seen.setdefault(s, []).append(i)
    dup = {s: pos for s, pos in seen.items() if len(pos) > 1}
    out.append('===== %s 单篇重复 (%d) =====' % (k, len(dup)))
    for s, pos in sorted(dup.items(), key=lambda x: -len(x[1]))[:20]:
        out.append('  %s x%d @%s' % (s, len(pos), pos[:4]))
# 跨篇重复
pairs = [('34','35'), ('34','36'), ('35','36')]
for a, b in pairs:
    ta, tb = texts[a], texts[b]
    seta = {ta[i:i+16] for i in range(len(ta)-16) if 'P' not in ta[i:i+16] and 'C' not in ta[i:i+16]}
    setb = {tb[i:i+16] for i in range(len(tb)-16) if 'P' not in tb[i:i+16] and 'C' not in tb[i:i+16]}
    common = seta & setb
    out.append('===== %s-%s 跨篇重复 (%d) =====' % (a, b, len(common)))
    for s in sorted(common)[:30]:
        out.append('  %s' % s)
io.open(os.path.join(DIR, '_dup_scan2.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')