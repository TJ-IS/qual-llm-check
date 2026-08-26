# -*- coding: utf-8 -*-
import io
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = io.open(fn, encoding='utf-8').read()
old = "第三，我们采用任务级流式检测的整体视角，以通道级归因在时间步级统一解决安全与效用权衡，使检测决策在拦截攻击与保持任务效用之间取得平衡。"
new = "第三，我们提出任务级流式检测与门控的整体设计，以通道级归因将安全与效用权衡落实到每一时间步的处置决策。"
c = t.count(old)
print('count:', c)
if c == 1:
    io.open(fn, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('N4b applied')
