# -*- coding: utf-8 -*-
import io, os
DIR = r"E:\github\qual-llm-check-IS-utd\runs\ais_basket_exclusive_objective_metric_benchmark_public_dataset_2020_2027_flash\research_reviews"
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
p = os.path.join(DIR, f36)
text = io.open(p, encoding='utf-8').read()
edits = [
 ("我们预期，经由严格评估，该框架将显著提升检测性能【占位】，满足交互式门控的延迟要求【占位】，并将误报与任务效用损失控制在可接受范围内【占位】。",
  "经由严格评估，我们预期该框架将显著提升检测性能【占位】，满足交互式门控的延迟要求【占位】，并将误报与任务效用损失控制在可接受范围内【占位】。"),
 ("本文呈现了该框架对信息系统知识库的贡献，以及三条设计原则与实践启示。",
  "本文呈现了该框架对信息系统知识库的贡献，并总结了三条设计原则与实践启示。"),
]
log = []
allok = True
for old, new in edits:
    c = text.count(old)
    if c != 1:
        allok = False
        log.append('匹配 %d 次，未落盘: %s' % (c, old[:40]))
        continue
    text = text.replace(old, new)
    log.append('已落盘: %s' % old[:40])
io.open(p, 'w', encoding='utf-8', newline='').write(text)
io.open(os.path.join(DIR, '_apply74b_log.txt'), 'w', encoding='utf-8').write('\n'.join(log) + '\n\n总体: ' + ('通过' if allok else '存在未落盘项') + '\n')
print('done')
