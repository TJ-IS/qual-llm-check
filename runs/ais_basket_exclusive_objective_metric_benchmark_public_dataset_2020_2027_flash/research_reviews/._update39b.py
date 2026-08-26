# -*- coding: utf-8 -*-
import io
path = '39_论文v3.3_各节句子级对照核验与系列内差异化管理记录.md'
with io.open(path, encoding='utf-8') as f:
    t = f.read()

sec88 = """
### 8.8 第二轮改写句的模板原文对照核验

以下对 8.3 所列 15 个句位的最终表述逐一回到模板原文比对，核验功能、引用支撑与句式是否达到模板水平。模板出处与 39 号第 0 节一致。

| 句位 | 模板原文（节选） | 功能对照 | 引用支撑 | 结论 |
|---|---|---|---|---|
| 范式句（3.1） | RADAR 引言 P5 以 Drawing on the computational design science paradigm 引出设计；RADAR Discussion 首句以 Guided by the computational design science paradigm (Gregor & Hevner, 2013; Rai, 2017) 将引用紧随范式术语 | 三篇均以范式身份加设计使命双从句收束（属于加主张、为依据加开发、遵循加构建），引用紧随范式术语，与 RADAR Discussion 句式一致 | Walls, Hevner, Rai 分组引用，每篇正文各文献至少一处，双向一致 | 达标 |
| 挑战总起（3.4 至 3.6） | DSDL 理论节以 albeit with great importance, is fraught with challenges 起句，后接 One major challenge 枚举 | 三篇均以挑战总起句引出第一、第二、第三对挑战对策句，功能与 DSDL 挑战段一致 | 无引用，与模板同 | 达标 |
| RQ 总起（4 节） | RADAR Research Gaps and Questions 以 Given these gaps, the following research questions are posed 引出 (1)(2)(3) | 三篇均以缺口综合句加本文提出句引出其一其二其三，功能与 RADAR 句式一致 | 无引用，与模板同 | 达标 |
| 图 1 句（5.0） | RADAR Proposed Design 以 Figure 1 illustrates an overview of this framework 指向图注 | 34 用整体架构如图 1 所示，35 用图 1 勾勒了，36 用图 1 呈现，均为图指引句 | 无引用 | 达标 |
| 节首句（6 节） | DSDL 4.1 节首以流程句预告本节内容；Wolf 3.7 以评估组织句说明实验安排 | 三篇均以本节报告尚未实施的实验设计及其预期发现起句，映射句分别为对应、如下、保持一致，功能为节首路线图 | 无引用 | 达标 |
| 设计原则引出（7.2 与 7.3） | ARText Technical Novelties 以 three-fold 加 First、Second、Third 组织三点 | 三篇均以三条设计原则总起加第一、第二、第三枚举，且以理论推导与预期实验证据为来源，符合设计科学范式要求 | 无引用，与模板同 | 达标 |
| 知识库贡献（7.1） | RADAR Discussion 以 Our contribution to the IS knowledge base is threefold 加 First、Second、Third | 三篇均以对信息系统知识库的贡献加三点枚举，总起句措辞分别为主要有三点、包括三个方面、可归纳为三点 | 无引用，与模板同 | 达标 |
| 数据来源（8.1） | Wolf 3.2 以 we used BrokerCheck as our starting point 声明数据源；Ampel Data Collection 以 We collected three sources 声明来源集合 | 三篇均以公开资源声明起句，随后逐项列举公开基准与语料，功能与两模板一致 | 逐项列举句带 Yang 等引用与占位出处 | 达标 |
| 中间状态前提（35 3.2 与 36 3.3） | DSDL 理论节以构念导出句限定中间构念的前提条件 | 35 用需要满足两个前提，36 用同时满足三个前提，前提数量随各自理论构成 | 无引用，与模板同 | 达标 |
| 鲁棒性前提（35 5.4 与 36 5.5） | ARText 以 vulnerability ... warrants further investigation 论证鲁棒性评估的必要性 | 35 用前提句，36 用决定句，均为鲁棒性评估必要性论证 | Li & Chai, 2022 在前文已支撑 | 达标 |
| 基线句（5.5 与 5.6） | RADAR 以 Experiment 1 compared RADAR's performance ... to eight leading ... baselines 声明比较对象 | 三篇分别声明三类与五类基线方法及比较动词（进行比较、展开比较、逐一比较） | 无引用，与模板同 | 达标 |
| 检验句（5.5 与 5.6） | Wolf 3.7.1 以 Statistical Evaluation 报告显著性检验与交叉验证；ARText 以 rigorously evaluated in comparison with benchmark methods 声明评估规范 | 三篇均声明统计显著性检验与置信区间报告，36 进一步说明置信区间以 bootstrap 构造 | 无引用，与模板同 | 达标 |
| 闭环句（7.4） | RADAR Discussion 实践段以可部署性主张收束实践启示 | 35 用秒级推理运行可叠加于现有部署之上，36 用增量推理运行可直接叠加于现有部署，均为部署可行性声明 | 无引用，与模板同 | 达标 |
| 实施周期（8.2） | Wolf 3.7 与 Ampel 研究设计段报告实验资源与工作量 | 三篇均以实施周期约【占位】周报告工作量，并各自说明研究一构建周期是否计入 | 无引用，与模板同 | 达标 |
| 8.3 第 1 条 | ARText 以相对比较与基准对照方式声明评估有效性 | 34 保留评估以相对比较为主，35 保留预置前后与基线差异，36 改为结论以相对比较为主不依赖单一绝对数字 | 无引用，与模板同 | 达标 |

核验结论。15 个句位的改写均保留原句位的功能链位置与模板对应关系，引用支撑与模板同层（需要引用的句位带引用，模板本身不引用的句位不加引用），句式差异只发生在系列内三篇之间，未降低任一句相对模板的水平。跨文献多次对比确认，同一功能的句位在三篇中分别对应 RADAR、DSDL、ARText、Wolf、Ampel 的不同写法，系列差异化以模板多样性为据，而非任意改写。
"""
t = t.rstrip() + "\n" + sec88
with io.open(path, 'w', encoding='utf-8') as f:
    f.write(t)
print('39号记录第 8.8 节已追加，总字符数:', len(t))
