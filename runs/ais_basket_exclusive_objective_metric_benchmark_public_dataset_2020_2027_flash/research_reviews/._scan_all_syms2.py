# -*- coding: utf-8 -*-
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
base = r'E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews\\'
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
syms = {
 '：': '全角冒号', ':': '半角冒号', '；': '全角分号', ';': '半角分号',
 '—': '破折号', '–': '短横线', '―': '横线', '——': '双破折号',
 '“': '左双引号', '”': '右双引号', '‘': '左单引号', '’': '右单引号',
 '…': '省略号', '⋯': '省略号2', '→': '箭头', '⇒': '箭头2',
 '（': '全角左括号', '）': '全角右括号', '『': '引号2', '』': '引号2',
}
for k, f in files.items():
    t = open(base+f, encoding='utf-8').read()
    print('====', k, '全文件长度', len(t))
    # 按行统计：正文行 vs 参考文献行
    lines = t.split('\n')
    ref_start = None
    for idx, ln in enumerate(lines):
        if ln.startswith('## 参考文献'):
            ref_start = idx
            break
    body_lines = lines[:ref_start] if ref_start is not None else lines
    ref_lines = lines[ref_start:] if ref_start is not None else []
    body = '\n'.join(body_lines)
    refs = '\n'.join(ref_lines)
    for part_name, part in [('正文', body), ('参考文献', refs)]:
        hits = {}
        for c, n in syms.items():
            cnt = part.count(c)
            if cnt:
                hits[n + '(' + c + ')'] = cnt
        if hits:
            print(' ', part_name, hits)
        else:
            print(' ', part_name, '全零')
    # 全角括号配平
    print('  全角括号', '(', body.count('（'), body.count('）'), ')', '参考文献', '(', refs.count('（'), refs.count('）'), ')')
