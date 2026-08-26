# -*- coding: utf-8 -*-
import io, sys

def load(fn): return io.open(fn, encoding='utf-8').read()
def save(fn, t): io.open(fn, 'w', encoding='utf-8', newline='').write(t)

f34 = '34_论文一_AgentShield-Adversary_编码智能体对抗攻击的系统化生成与威胁建模_v3.1.md'
f35 = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'

edits = [
 (f34, "今天，领先的软件与云厂商已将编码智能体嵌入开发者工作流，以自动化代码生成、缺陷修复与安全审查保护其软件资产。",
       "今天，领先的软件与云厂商已将编码智能体嵌入开发者工作流，以自动化代码生成、缺陷修复与安全审查提升研发效率并保护其软件资产。", 'M1'),
 (f34, "本文认为，攻击生成的终局目的不是制造孤立的越狱样例，而是为防御研究提供可系统复用的威胁证据。",
       "攻击生成的目的不在于制造孤立的越狱样例，而在于为防御研究提供可系统复用的威胁证据。", 'M2'),
 (f34, "以威胁模型作为理论限定的中间状态，连接攻击者如何行动与攻击生成算法如何构造。",
       "以威胁模型作为理论限定的中间状态，连接攻击者的行为逻辑与攻击生成算法的构造。", 'M3'),
 (f35, "本文认为，防御的终局结果不是扩大检测覆盖面，而是在攻击造成危害之前以可负担的代价预防攻击。",
       "事前防御的目的不在于扩大检测覆盖面，而在于以可负担的代价在攻击造成危害之前预防攻击。", 'M4'),
 (f35, "这一预测在前、干预提前的逻辑在 IS 文献中已得到反复验证。",
       "这一先预测后干预的逻辑在 IS 文献中已得到反复验证。", 'M5'),
 (f36, "本文认为，检测的终局目的不是扩大过滤覆盖面，而是在危害动作生效之前以受控的误报代价拦截攻击。",
       "检测的目的不在于扩大过滤覆盖面，而在于以受控的误报代价在危害动作生效之前拦截攻击。", 'M6'),
 (f36, "事实上，信息操纵攻击具有流式特性。",
       "信息操纵攻击具有流式特性。", 'M7'),
]
texts = {f34: load(f34), f35: load(f35), f36: load(f36)}
ok = True
for fn, old, new, tag in edits:
    c = texts[fn].count(old)
    if c != 1:
        print(f'FAIL {tag}: count={c}'); ok = False
    else:
        texts[fn] = texts[fn].replace(old, new)
        print(f'OK {tag}')
if ok:
    save(f34, texts[f34]); save(f35, texts[f35]); save(f36, texts[f36])
    print('ALL SAVED')
else:
    print('NOT SAVED'); sys.exit(1)
