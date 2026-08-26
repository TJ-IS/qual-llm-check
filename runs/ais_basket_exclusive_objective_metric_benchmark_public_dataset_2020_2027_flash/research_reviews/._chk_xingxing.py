# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
for k in ['34','35','36']:
    t = open(base+f'{k}_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md' if k=='34' else (base+f'{k}_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md' if k=='35' else base+f'{k}_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'), encoding='utf-8').read()
    hits = [m.start() for m in re.finditer('新兴、高风险情境', t)]
    print(k, '新兴、高风险情境', len(hits))
    for i in hits:
        print('   ...', t[max(0,i-60):i+30].replace(chr(10),' '))
