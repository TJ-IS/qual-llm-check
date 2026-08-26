# -*- coding: utf-8 -*-
import io
fn = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
t = io.open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
i = main.find('## 二、'); j = main.find('## 四、')
print(main[i:j])
