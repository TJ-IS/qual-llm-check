# -*- coding: utf-8 -*-
import io, sys

def load(fn): return io.open(fn, encoding='utf-8').read()
def save(fn, t): io.open(fn, 'w', encoding='utf-8', newline='').write(t)

f35 = '35_论文二_AgentShield-Anticipate_编码智能体攻击面的事前预判与预算化预置防御_v3.1.md'
f36 = '36_论文三_AgentShield-Detect_编码智能体信息操纵攻击的流式检测与动作门控_v3.1.md'

edits = [
 (f35, "综合上述文献，编码智能体事前防御研究存在三个相互关联的缺口。三个缺口共同指向一个事实，即现有研究均未以设计科学方法在编码智能体情境中整合相关范式。",
       "综合上述文献，编码智能体事前防御研究存在三个相互关联的缺口，且现有研究均未以设计科学方法在编码智能体情境中整合相关范式。", 'N1'),
 (f36, "这一检测性能、对抗绕过率与任务效用的三维评估规范是本文遵循并期望确立的评估标准，其依据来自 IS 检测与鲁棒性文献的共识。评估必须同时报告安全收益与效用代价（Li & Chai, 2022; Lin & Fang, 2021）。",
       "这一检测性能、对抗绕过率与任务效用的三维评估规范，直接来自 IS 检测与鲁棒性文献的共识，是本文采用的评估标准。", 'N2'),
 (f35, "第三，我们提出了三条指导编码智能体安全运营的设计原则，并展示了预测与处方方法协同的实践价值。",
       "第三，我们采用任务级攻击风险的整体视角，在单元级统一解决安全与效用权衡，使事前防御在降低攻击风险的同时保持任务效用。", 'N3'),
 (f36, "第三，我们以公开攻击基准建立了检测器对抗重训与绕过率报告的评估规范，使检测器自身不再是鲁棒性评估的例外（Li & Chai, 2022）。",
       "第三，我们采用任务级流式检测的整体视角，以通道级归因在时间步级统一解决安全与效用权衡，使检测决策在拦截攻击与保持任务效用之间取得平衡。", 'N4'),
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
