# -*- coding: utf-8 -*-
import io, re
t = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
m = re.search(r'^### 5\.4 分层动作门控\n(.*?)^## 六、', t, flags=re.M|re.S)
print(m.group(1).strip())
