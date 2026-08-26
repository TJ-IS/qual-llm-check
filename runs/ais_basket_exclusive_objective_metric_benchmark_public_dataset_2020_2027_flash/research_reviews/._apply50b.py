# -*- coding: utf-8 -*-
import io
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = io.open(fn, encoding='utf-8').read()
old = "就 IS 文献谱系而言，本文所填补的空白是清晰的。融合、验证与鲁棒化方法已在诸多检测情境中确立先例，但均未涉及编码智能体的流式信息操纵攻击检测。"
new = "融合、验证与鲁棒化方法已在诸多检测情境中确立先例，但均未涉及编码智能体的流式信息操纵攻击检测。"
c = t.count(old)
print('count:', c)
if c == 1:
    io.open(fn, 'w', encoding='utf-8', newline='').write(t.replace(old, new))
    print('E17 applied')
