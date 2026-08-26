# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
out = []
for k, f in files.items():
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    # 去掉标题/空行/占位符行，按句子切分
    lines = [l.strip() for l in body.split('\n') if l.strip() and not l.startswith('#')]
    para = ' '.join(lines)
    # 按句号切分（保留 RQ 与公式行）
    sents = re.split(r'(?<=[。])', para)
    stats = []
    for s in sents:
        s = s.strip()
        if len(s) < 20: continue
        has_cite = bool(re.search(r'[（(][^）)]*\d{4}[^）)]*[）)]', s))
        if not has_cite and '【占位' not in s:
            stats.append(s)
    out.append('===== %s 无引用断言句（%d 句）=====' % (k, len(stats)))
    for s in stats:
        out.append('- ' + s[:110])
io.open(os.path.join(DIR, '_nocite_sents.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')