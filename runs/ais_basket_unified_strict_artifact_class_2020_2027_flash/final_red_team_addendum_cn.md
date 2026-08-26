# 最终27篇红队审计（V4；与前文冲突时以本节为准）

输入文章已经被V3纳入，但V3不是权威结论。请从零阅读全文并主动寻找推翻纳入的证据。严格标准不变；本轮重点审计V3仍然容易犯的五类错误。

## 1. “有客观accuracy/F1”不等于目标构念客观

- actionable、relevant、PICO语义角色、实践技能表现、内容/事件解释、决策是否合适等，只要真值需要专家理解文本意义、任务质量或规范含义，就不是外部事实标签。
- 固定rubric、本体、代码簿、专家共识或冻结标签不能把语义判断变成完全客观构念。
- 因此必须重点反查social-listening平台的actionability/语义标注、数字技能自动评分、PICO抽取等任务；若核心成功指标依赖这种真值，排除。

## 2. 客观结果不能掩盖理论解释为核心

- 如果文章核心贡献是制度化、组织变革、责任、合法性、认知/注意机制或行为理论，而软件改动与客观指标主要用于展示/验证该理论，则`core_goal_status`不得判为`objective_improvement_primary`。
- 特别复查`Digital Institutionalization: The Case of E-Prescribing`：若核心贡献是数字制度化理论而非某类软件的客观性能改进，排除。

## 3. 可运行工具不能掩盖算法/分析方法贡献

- 自动流程仿真模型发现工具、检测方法、聚类/置信算法、求解器管道或Web工具，如果作者贡献实质是算法/方法性能，仍属于`algorithm_or_model_only`或`analytical_or_simulation_method_only`。
- `Automated discovery of business process simulation models from event logs`须检验删除Simod工具名称后是否只剩自动发现算法/方法；若是，排除。
- 不得因为代码公开、GUI、模块图、多数据集benchmark或运行实例就自动通过。

## 4. 领域DSS不能把一个案例问题命名成软件类别

- 应急、医院、港口、道路基础设施、飞机维修等系统若核心贡献是针对领域约束的优化/数据处理/运营方案，且缺少面向同类软件的明确可复用设计原则、功能/交互/工作流知识，则属于`case_specific_solution`或`domain_mechanism_or_policy`。
- `Providing more regular road signs infrastructure updates...`与`A novel decision support system for optimizing aircraft maintenance...`必须按此边界复核，不能仅凭“platform/DSS/architecture”通过。

## 5. 市场机制、仿真和运营蓝图不是软件制品贡献

- 资源分配/拍卖/市场设计、数学机制、仿真蓝图和运营策略，即使被称为DSS或实现为仿真系统，也不等于对软件制品类别贡献。
- `Smart Markets for Real-Time Allocation of Multiproduct Resources`若核心是市场机制/资源分配规则与仿真评价，必须排除。

## 正例边界仍须保持

不要反向过度排除以下逻辑：密码强度计的主观问卷只是机制检验；robust fraud detection明确把理论转译为FDS设计原则与特征；HyperCARS、ARText和social-bot detection以可复用系统组件形式实例化并评价。它们仍须凭当前全文证据通过，而不是仅因被列名通过。

只有文章抵御上述所有反查、三个模块各自全门通过，`strict_include`才可为true。输出结构和逻辑校验必须与V3完全相同。
