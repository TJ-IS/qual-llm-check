# -*- coding: utf-8 -*-
import io
for k, f, sec in [
 ('34','34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md','7.2'),
 ('35','35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md','7.3'),
 ('36','36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md','7.3')]:
    text = io.open(f, encoding='utf-8').read()
    body = text.split('## 参考文献')[0]
    idx = body.find('### '+sec)
    seg = body[idx:idx+1500]
    print('#'*25, k, sec)
    print(seg.replace(chr(10),' ')[:1400])
    print()
