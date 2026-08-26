# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
edits = {
 '34': [
   ('在这些措施到位的前提下，善意使用的收益可显著超过恶意滥用的风险。',
    '在这些措施到位后，善意使用的收益可显著超过恶意滥用的风险。'),
 ],
 '35': [
   ('其二，防御计划应可解释、可申诉，隔离与延迟动作附有风险分依据，人工审查通道确保误判可纠正。',
    '其二，防御计划应可解释、可申诉，隔离与延迟动作附有风险分依据，误判经人工审查通道纠正。'),
 ],
 '36': [
   ('其二，门控动作应可解释、可申诉。通道级告警使被阻断的开发者能够理解处置依据，人工审查通道确保误报可纠正。',
    '其二，门控动作应可解释、可申诉。通道级告警使被阻断的开发者能够理解处置依据，误报可经人工复核纠正。'),
   ('其三，检测器以公开基准训练与评估，其误报率与效用损失以【占位】为上限公开报告，避免以安全名义无约束地干预正常开发流程。',
    '其三，检测器以公开基准训练与评估，其误报率与效用损失以【占位】为上限公开报告，正常开发流程所受干预以处置必要为限。'),
 ],
}
log = []
allok = True
for k, f in files.items():
    p = os.path.join(DIR, f)
    text = io.open(p, encoding='utf-8').read()
    for old, new in edits.get(k, []):
        c = text.count(old)
        if c != 1:
            allok = False
            log.append('[%s] 匹配 %d 次，未落盘: %s' % (k, c, old[:36]))
            continue
        text = text.replace(old, new)
        log.append('[%s] 已落盘: %s' % (k, old[:36]))
    io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply76_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')
