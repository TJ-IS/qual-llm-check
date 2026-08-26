# -*- coding: utf-8 -*-
import io
fn = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
t = io.open(fn, encoding='utf-8').read()
main = t.split('## 参考文献')[0]
i = main.find('## 四、'); j = main.find('## 五、')
print(main[i:j])
