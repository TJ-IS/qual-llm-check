# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
# 提取每篇从第三章到文末（不含参考文献）
for k, f in files.items():
    t = open(base+f, encoding='utf-8').read()
    m = re.search(r'## 三、.*?(?=\n## 参考文献)', t, re.S)
    out = m.group(0) if m else ''
    open(base + f'_ch3end_{k}.txt', 'w', encoding='utf-8').write(out)
    print(k, '第三至九章长度', len(out))
