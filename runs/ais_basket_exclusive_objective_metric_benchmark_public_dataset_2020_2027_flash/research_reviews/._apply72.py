# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
edits = {
 '35': [
   ("防御机制可使智能体的良性任务完成率明显下降【占位，需核对公开出处】",
    "防御机制可使智能体的正常任务完成率明显下降【占位，需核对公开出处】"),
   ("这一评估规范同时回应了防护机制损害良性任务完成率的实证担忧【占位，需核对公开出处】",
    "这一评估规范同时回应了防护机制损害正常任务完成率的实证担忧【占位，需核对公开出处】"),
 ],
 '36': [
   ("编码智能体根据问题描述与仓库上下文推进任务，在任务执行中依次读取文件、编辑代码、运行测试并调用工具，直至任务完成（Yang et al., 2024）。",
    "编码智能体根据问题描述与仓库上下文推进任务，在执行中读写文件、运行命令并调用工具，直至任务完成（Yang et al., 2024）。"),
   ("面对信息操纵威胁，实时识别攻击已成为编码智能体安全防护的当务之急。",
    "面对信息操纵威胁，实时识别攻击已成为编码智能体安全防护的首要任务。"),
   ("检测器在对抗样本下的表现亦未被报告，检测规则可被针对性地规避（Li & Chai, 2022）。",
    "检测器在对抗样本下的表现亦未被评估，检测规则可被针对性地规避（Li & Chai, 2022）。"),
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
            log.append('[%s] 匹配 %d 次，未落盘: %s' % (k, c, old[:40]))
            continue
        text = text.replace(old, new)
        log.append('[%s] 已落盘: %s' % (k, old[:44]))
    io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply72_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')