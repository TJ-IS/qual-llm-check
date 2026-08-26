# -*- coding: utf-8 -*-
import io, re
files = {
 "34": "34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md",
 "35": "35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md",
 "36": "36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md",
}
for k, f in files.items():
    with io.open(f, "r", encoding="utf-8") as fh:
        text = fh.read()
    body = text.split("## 参考文献")[0]
    print("=====", k)
    for name in ["Walls", "Hevner", "Rai"]:
        for m in re.finditer(name, body):
            start = max(0, m.start()-25)
            print(f"  {name} @ {m.start()}: ...{body[start:m.end()+20]}...")
