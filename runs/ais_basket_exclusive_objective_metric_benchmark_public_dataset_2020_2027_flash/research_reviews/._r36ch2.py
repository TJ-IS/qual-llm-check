# -*- coding: utf-8 -*-
import io, re
out = io.open('_r36ch2.txt','w',encoding='utf-8')
t = io.open('36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md', encoding='utf-8').read()
m = re.search(r'## 二、文献综述与研究缺口\n(.*?)(?=\n## 三、理论基础与设计理由)', t, re.S)
out.write(m.group(1))
out.close()
