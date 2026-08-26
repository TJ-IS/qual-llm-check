# -*- coding: utf-8 -*-
import io, re
out = io.open('_chk4.txt','w',encoding='utf-8')
text = io.open('34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md', encoding='utf-8').read()
i = text.find('系统防御此类攻击的关键前提')
out.write(repr(text[i-120:i+700]))
out.close()
