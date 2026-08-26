# -*- coding: utf-8 -*-
import io, sys
def load(fn): return io.open(fn, encoding='utf-8').read()
def save(fn, t): io.open(fn, 'w', encoding='utf-8', newline='').write(t)
f35 = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'
edits = [
 (f35, "仅依赖问题文本的预测器将漏报仓库投毒类攻击，其信号完全位于仓库结构通道。",
       "仅依赖问题文本的预测器将漏报仓库文件注入类攻击，其信号完全位于仓库结构通道。", 'T1'),
 (f36, "文本伪装类攻击（问题改写）主要由文本意图通道与行为通道的背离暴露，仓库投毒类攻击主要由调用图结构通道暴露【占位】。",
       "文本伪装类攻击（问题改写）主要由文本意图通道与行为通道的背离暴露，仓库文件注入类攻击主要由调用图结构通道暴露【占位】。", 'T2'),
]
texts = {f35: load(f35), f36: load(f36)}
ok = True
for fn, old, new, tag in edits:
    c = texts[fn].count(old)
    if c != 1:
        print(f'FAIL {tag}: count={c}'); ok = False
    else:
        texts[fn] = texts[fn].replace(old, new)
        print(f'OK {tag}')
if ok:
    save(f35, texts[f35]); save(f36, texts[f36])
    print('ALL SAVED')
else:
    print('NOT SAVED'); sys.exit(1)
