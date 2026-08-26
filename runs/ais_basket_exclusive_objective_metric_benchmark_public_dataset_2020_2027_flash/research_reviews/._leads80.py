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
    lines = io.open(os.path.join(DIR, f), encoding='utf-8').read().split('\n')
    out.append('===== %s =====' % k)
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r'^#{2,4} \d', ln) or re.match(r'^## [一二三四五六七八九]', ln):
            # 找标题后第一个非空行
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                first = lines[j].strip()
                if first.startswith('#'):
                    out.append('%s  -> (标题连排)' % ln)
                else:
                    out.append('%s  -> %s' % (ln, first[:90]))
            i = j
        else:
            i += 1
io.open(os.path.join(DIR, '_leads80.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
