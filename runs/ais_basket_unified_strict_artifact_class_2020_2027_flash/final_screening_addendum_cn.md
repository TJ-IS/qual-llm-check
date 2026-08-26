# 全集最终筛选补充边界（V3；与前文冲突时以本节为准）

在V2修订基础上，再执行以下压力测试：

## “系统”命名不能替算法模型取得资格

`A hybrid decision support system for adaptive trading strategies: Combining a rule-based expert system with a deep reinforcement learning strategy`应排除。全文虽然反复称其为hybrid decision support system/trading system，但研究贡献明确列为：组合RB与深度RL的金融模型、状态空间、交易量机制和benchmark收益表现，并自称对machine learning和finance作贡献。它没有实例化独立于算法回测的软件产品功能、交互或工作流，删除“system”命名后贡献完整保留为同一交易模型。因此属于`algorithm_or_model_only`与`algorithm_or_analytical_method`。

由此推广：

- 架构图、模块命名、输入/输出管道、回测、仿真、多个数据集、benchmark、ablation和未来真实应用潜力，都不能单独证明存在合格软件制品或类级设计贡献。
- 如果作者列出的贡献实质都是模型结构、特征、状态空间、目标函数、策略、求解机制和预测/收益性能，通常排除，即使标题写DSS/system/framework。
- 只有作者把这些技术元素转译为某类软件制品的可复用设计原则/要求/特征或功能机制，并将运行实例作为该类软件的实例来评价，才能按V2的五项条件纳入。

最终判定必须以全文的研究问题、贡献列表、制品实现和评价对象共同为据，不可只引用标题或摘要中的“system”。
