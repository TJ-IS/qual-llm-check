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
   ('本文框架以其系统化刻画编码智能体攻击面的新颖设计，贡献于 IS 安全研究。',
    '本文框架以系统化刻画编码智能体攻击面贡献于 IS 安全研究。'),
 ],
 '35': [
   ('但如何在任务开始前预测攻击面、并在预算约束下预置防御动作，目前知之甚少。',
    '但如何在任务开始前预测攻击面并在预算约束下预置防御动作，目前知之甚少。'),
 ],
 '36': [
   ('但如何在任务执行中实时识别攻击、以受控误报联动处置、并保持检测器自身对自适应攻击的鲁棒性，目前知之甚少。',
    '但如何在任务执行中实时识别攻击、以受控误报联动处置并保持检测器自身对自适应攻击的鲁棒性，目前知之甚少。'),
   ('而工具调用、文件读写与仓库状态等外部可验证信号难以同时被伪造',
    '而工具调用、文件读写与仓库状态等外部可验证信号难以被一同伪造'),
   ('说明安全性的改善并未以明显损害任务效用为代价。同时，本文方法单步端到端检测延迟低于【占位】毫秒',
    '说明安全性的改善并未以明显损害任务效用为代价。此外，本文方法单步端到端检测延迟低于【占位】毫秒'),
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
io.open(os.path.join(DIR, '_apply77_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')
