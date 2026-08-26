# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
files = {
 '34': '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md',
 '35': '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md',
 '36': '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md',
}
edits = {
 '34': [("表明此类攻击已在真实环境中发生。这些证据共同表明，编码智能体的输入通道是真实的攻击面，此类威胁并非假设性风险。",
         "表明此类攻击已在真实环境中发生。这些证据共同表明，编码智能体的输入通道是真实的攻击面，这一威胁并非假设性风险。")],
 '35': [("真实平台的漏洞披露表明此类攻击已在真实环境发生【占位，需核对公开出处】",
         "真实平台的漏洞披露显示此类攻击已实际发生【占位，需核对公开出处】")],
 '36': [("面对此类威胁，实时识别攻击已成为编码智能体安全防护的当务之急。",
         "面对信息操纵威胁，实时识别攻击已成为编码智能体安全防护的当务之急。")],
}
log = []
allok = True
for k, f in files.items():
    p = os.path.join(DIR, f)
    text = io.open(p, encoding='utf-8').read()
    for old, new in edits[k]:
        c = text.count(old)
        if c != 1:
            allok = False
            log.append('[%s] 匹配 %d 次，未落盘: %s' % (k, c, old[:40]))
            continue
        text = text.replace(old, new)
        log.append('[%s] 已落盘: %s' % (k, old[:44]))
    io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply71b_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')