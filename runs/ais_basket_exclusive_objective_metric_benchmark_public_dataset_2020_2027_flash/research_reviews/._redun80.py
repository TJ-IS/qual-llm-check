# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
pats = ['进行', '加以', '予以', '能够', '非常', '十分', '相当', '比较大', '比较大', '较为', '比较而言', '基本上', '实际上', '事实上', '本质上', '来说', '而言', '所谓', '某种', '某种程度', '一定', '一定程度的', '较为明显', '较为显著', '更加', '更为', '进一步地', '进一步来说', '换句话说', '换言之', '可以说', '可见', '显然', '值得注意的是', '重要的是', '关键的是', '同时，', '此外，', '然而，', '因此，', '由此，', '据此，', '进而', '从而', '以便', '从而使得', '使得']
out = []
for k, f in files.items():
    t = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    m = re.search(r'\n## 参考文献\n', t)
    body = t[:m.start()] if m else t
    out.append('===== %s =====' % k)
    for p in pats:
        c = body.count(p)
        if c > 0:
            out.append('  %s x%d' % (p, c))
io.open(os.path.join(DIR, '_redun80.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
