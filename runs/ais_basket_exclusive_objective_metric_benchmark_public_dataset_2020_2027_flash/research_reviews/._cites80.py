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
    t = io.open(os.path.join(DIR, f), encoding='utf-8').read()
    m = re.search(r'\n## 参考文献\n', t)
    body = t[:m.start()] if m else t
    out.append('===== %s =====' % k)
    # 叙述性引用：Xxx 等（2020）或 X 与 Y（2020）
    narr = re.findall(r'[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z .\-]{0,40}?等（\d{4}[a-z]?）|[\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z .\-]{0,40}?与 [\u4e00-\u9fffA-Za-z][\u4e00-\u9fffA-Za-z .\-]{0,40}?（\d{4}[a-z]?）', body)
    out.append('  叙述性引用 %d 处:' % len(narr))
    for n in narr:
        out.append('    %s' % n)
    # 括注引用：全半角括号内的 et al. 或 &
    paren = re.findall(r'[（(][^（()）]*?(?:et al\.|&)[^（()）]*?[)）]', body)
    out.append('  括注引用 %d 处（样本）:' % len(paren))
    for p in paren[:12]:
        out.append('    %s' % p)
    # 检查叙述性引用中是否混用 et al. 或 &（应为 等 或 与）
    bad = re.findall(r'[\u4e00-\u9fff][\u4e00-\u9fffA-Za-z .\-]{0,30}?(?:et al\.|&)[\u4e00-\u9fffA-Za-z .\-]{0,20}?（\d{4}', body)
    out.append('  叙述位置英文格式 %d 处:' % len(bad))
    for b in bad:
        out.append('    %s' % b)
    # 检查括注中是否混用中文 等（应为 et al.）
    bad2 = re.findall(r'[（(][^（()）]*?等[^（()）]*?\d{4}[a-z]?[)）]', body)
    out.append('  括注位置中文格式 %d 处:' % len(bad2))
    for b in bad2[:12]:
        out.append('    %s' % b)
io.open(os.path.join(DIR, '_cites80.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print('done')
