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
    for i, ln in enumerate(lines):
        # 跳过参考文献区
        if ln.startswith('## 参考文献'):
            break
        for ch, name in [(';','半角分号'), ("'","半角单引号"), ('(','半角括号'), ('{','花括号'), ('=','等号'), ('·','中点'), ('|','竖线'), ('[','方括号'), ('+','加号'), ('−','减号U2212')]:
            if ch in ln:
                out.append('L%d %s: %s' % (i+1, name, ln[:120]))
                break
io.open(os.path.join(DIR, '_sym_locate79.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
