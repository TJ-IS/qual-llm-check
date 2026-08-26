# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = ['34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md']
out = []
for f in files:
    text = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    out.append('===== %s =====' % f[:2])
    for w in ['良性', '当务之急', '依次读取', '未被报告', '运行测试并调用工具', '自主规划执行步骤', '直至任务完成']:
        c = body.count(w)
        if c:
            out.append('  %s: %d' % (w, c))
io.open(os.path.join(DIR, '_term_scan.txt'), 'w', encoding='utf-8').write('\n'.join(out))
print('done')