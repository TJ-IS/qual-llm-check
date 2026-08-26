# -*- coding: utf-8 -*-
import io, re
t = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
# extract chapter 3
m = re.search(r'^## 三、[^\n]*\n(.*?)^## 四、', t, flags=re.M|re.S)
ch3 = m.group(1)
print('第三章字数', len(ch3))
print(ch3[:2600])
