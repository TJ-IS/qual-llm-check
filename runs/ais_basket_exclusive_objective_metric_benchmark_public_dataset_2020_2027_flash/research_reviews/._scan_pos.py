# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
out = []
for k, f in files.items():
    lines = io.open(os.path.join(DIR, f), encoding='utf-8').read().split('\n')
    for i, l in enumerate(lines):
        for w in ['没有系统生成的攻击', '压力测试', '最坏情况', '不加区分', '掩蔽特征']:
            if w in l:
                t = l.strip()
                out.append('%s L%d [%s]: %s' % (k, i+1, w, t[:110]))
io.open(os.path.join(DIR, '_phrase_pos.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')