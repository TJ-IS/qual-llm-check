# -*- coding: utf-8 -*-
import io, os, re
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
terms = ['编码智能体', '信息操纵攻击', '攻击面', '操纵单元', '预算约束', '误报', '威胁模型', '危害判定器', '攻击通道', '风险分', '门控', '对抗重训', '基准', '真值', '单元级', '任务级', '流式', '事前', '预置防御', '加载', '护栏', 'guardrail', '知识库', '设计科学', '处方性知识', '纵深防御', '鲁棒性', '规避路径', '处置层级']
out = []
for k, f in files.items():
    t = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    m = re.search(r'\n## 参考文献\n', t)
    body = t[:m.start()] if m else t
    out.append('===== %s =====' % k)
    for term in terms:
        c = body.count(term)
        if c > 0:
            out.append('  %s x%d' % (term, c))
io.open(os.path.join(DIR, '_terms79.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
