# 52 篇候选文献的软件制品类级贡献审计

- 输入：52
- 审计 A 纳入：21
- 审计 B 纳入：16
- 两轮分歧：9
- 最终纳入：16
- 最终排除：36

## 最终纳入

### Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- 年份 / 期刊：2024 / MIS Quarterly
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：文章聚焦于个性化e-learning系统的设计科学贡献，明确提出并实例化了可推广的‘相关交错（related-interleaving）’学习会话设计，包含弱主题检测、知识地图和调度引擎三个可复用软件机制；研究问题和贡献声明均指向这类系统应如何设计和配置，实验评价将学习绩效提升归因于该设计机制而非仅底层算法；运行实例是一个个性化学习系统，是所声称类别的典型实例。因此满足全部七道gate，属于类级软件制品贡献。

### Design Principles for Robust Fraud Detection:  The Case of Stock Market Manipulations

- 年份 / 期刊：2021 / Journal of the Association for Information Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：论文明确以设计科学研究范式提出鲁棒欺诈检测系统的设计原则和设计特征，直接指向欺诈检测系统这一可识别软件制品类别；核心贡献是设计如何构建鲁棒分类器机制，而非仅提出算法或领域政策；分类器实例实证支持了设计机制（语言特征、组合特征、集成学习）对鲁棒性的改进，且作者明确表示设计知识可推广到其他文本欺诈检测场景，因此通过七道门槛。

### ForeSim-BI: A predictive analytics decision support tool for capacity planning

- 年份 / 期刊：2020 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：本文核心贡献是提出了一个用于维护能力规划的预测分析决策支持工具（ForeSim-BI），该工具由预测、贝叶斯推断、模拟和贝叶斯网络四个模块集成，并辅以LP模型解决区间选择问题；其设计机制可复用于其他复杂产品系统的维护能力规划DSS。论文以真实飞机MRO案例为实例，验证了该工具相比工程估计的显著精度提升，并将改进归因于工具设计。因此满足类级软件制品贡献标准。

### Geo-semantic-parsing: AI-powered geoparsing by traversing semantic knowledge graphs

- 年份 / 期刊：2020 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：论文提出并实现了一个地理解析（geoparsing）技术 GSP，该技术属于可识别且可重复实例化的地理解析软件制品类别。作者设计并实验了可复用的扩展策略（拼写、潜在语义、拓扑）和基于回归的候选选择机制，这些是地理解析系统的核心功能组件。核心贡献明确指向如何设计地理解析软件及其组件，并通过客观指标（precision/recall/F1）将性能提升归因于这些设计机制。实验实例（Python 实现的 GSP）是该类别的一个运行实例。删除具体数据集和场景后，保留的三阶段流程仍提供了关于地理解析软件应如何设计的可推广知识。因此通过七道门。

### Designing Conversational Dashboards for Effective Use in Crisis Response

- 年份 / 期刊：2023 / Journal of the Association for Information Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：作者核心贡献明确指向'危机响应对话式仪表板'这一软件制品类别，提出了三条可复用的设计原则及系统架构（自然语言交互、双模态选择、对话式入职），并实例化为可运行的COVID-19仪表板。该类别独立于单一案例，设计理论在文中明确表明可推广到其他危机；核心研究产出是这类软件应如何设计，而非某个算法或领域机制。E实验评价中，透明交互、效率和有效性等指标改进被归因于具体设计机制。移除COVID案例与专门界面后，剩下的仍是关于该类软件设计的可复用知识。

### Automated dynamic approach for detecting ransomware using finite-state machine

- 年份 / 期刊：2020 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：论文核心贡献是一个可推广的勒索软件检测系统设计，基于FSM的可复用行为监控和决策机制，并在多勒索软件家族上验证，符合类级软件制品贡献的所有门槛。

### Applied machine learning for a zero defect tolerance system in the automated assembly of pharmaceutical devices

- 年份 / 期刊：2021 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / implicit_but_well_supported / core_research_contribution
- 结论：论文的核心研究对象是可识别的软件制品类别——自动化装配线质量控制系统，而非仅为特定案例实现算法；作者实质设计了该系统中可复用的多层机制（异常检测、集成分类、投票、可解释性），并明确将贡献声明为QC系统的设计；软件是研究贡献本身，而非算法外包层；评价将客观指标（FNR/FPR、延迟）归因于系统设计机制（如AD、投票方案）；在真实工业用例中运行实例验证了该类软件的可实例化能力；移除具体用例后仍保留关于QC系统设计的可推广知识，因此通过七道门槛。

### A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- 年份 / 期刊：2021 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：该文的核心贡献是设计和开发了一个可运行的飞机维修计划优化DSS，其软件制品类别明确（决策支持系统），独立于单一案例（可推广到火车/公交等类似维护计划问题），作者实质设计或修改了排程、任务分配和轮班计划这些可复用功能机制，核心贡献指向该类软件应如何设计，软件本身不是包装或实验工具，评价将客观KPI改善归因于DSS的设计机制（AMPO-1/2/3集成），实际运行的实例充分体现了所声称的DSS类别。因此七道gate全部通过。

### An interactive decision support system for real-time ambulance relocation with priority guidelines

- 年份 / 期刊：2022 / Decision Support Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / implicit_but_well_supported / core_research_contribution
- 结论：文章围绕一个明确可识别的制品类别——实时救护车重定位决策支持系统——展开，核心贡献在于设计并实现了一套含优化模型、数据库、用户界面和实时风险评估机制的DSS。该类别独立于德黑兰案例，具有可推广性。DSS本身是论文的核心研究对象，而非算法或模型的包装/演示工具。实验评价将覆盖率、响应时间等客观指标的改善归因于DSS支持的政策（即实时重定位和动态覆盖机制），而非仅验证数学模型更优。实际运行的C++/.NET原型实例化了所声称的DSS类别及可复用设计机制。因此七道gate全部通过，class_level_include=true。

### Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- 年份 / 期刊：2022 / Journal of Management Information Systems
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：作者针对可识别的软件制品类别——对抗鲁棒的文本分类系统——提出了可推广的设计框架：绩效比率和性能-扰动曲线度量，以及集成学习与迭代对抗重训练机制。ARText系统是该类的运行实例，并在垃圾评论和垃圾邮件检测任务上得到评估；评估中的鲁棒性指标提升被明确归因于上述系统设计机制，而非仅验证底层算法。移除具体数据集和测试任务后，剩余的是关于预测分析/文本分类系统应如何设计与运行以实现对抗鲁棒性的类级知识。因此满足七道gate，应纳入类级软件制品贡献。

### When Variety Seeking Meets Unexpectedness: Incorporating Variety-Seeking Behaviors into Design of Unexpected Recommender Systems

- 年份 / 期刊：2024 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：论文明确以'意外推荐系统'这一软件制品类别作为设计目标；核心贡献在于推荐系统内部如何根据消费者variety-seeking水平动态调节unexpectedness权重，这是一种可复用的推荐机制设计；文章在多数据集和生产系统上部署运行，验证机制带来的客观业务指标（CTR、观看时长等）提升，并将这些改善明确归因于新的推荐系统设计机制。因此通过所有七道gate，属于类级软件制品贡献。

### Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- 年份 / 期刊：2025 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：本文明确提出并测试短暂分享（ephemeral sharing）作为一种隐私增强的软件设计机制，该机制在社交平台中已有先例但在在线约会情境中进行了新的设计适配（匹配请求页UI、照片上传交互、自动消失与限制下载/截屏等）。核心贡献声明指向在线匹配平台及其他隐私敏感平台应如何实现此类设计以鼓励披露、改善匹配；实验中的客观指标（照片披露数、含脸照片数、匹配数、接收者消息数）的改善被归因于短暂分享设计机制，且Summer平台上的短暂照片功能就是该设计类别的实际运行实例。移除案例名称和数据后，仍保留关于短暂分享这类软件功能组件应如何设计（自动消失、不可追溯、限制转发、UI传达）以降低隐私顾虑的知识。因此满足全部七道门槛。

### HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- 年份 / 期刊：2025 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：文章明确提出HyperCARS方法，针对上下文感知推荐系统（CARS）这一可识别软件制品类别，设计了双曲嵌入与层次聚类结合的上下文建模组件，并以簇ID路径形式实现松耦合接口，使之可嵌入多种推荐算法。该方法在Frappe、Gowalla、Yelp等多个数据集上实例化运行，并带来了RMSE、MAE、Hit@K、MRR@K等客观指标的显著改进。移除具体数据集和界面后，仍保留关于CARS系统应如何设计层次化上下文表示与组件集成的可复用知识，因此满足全部七道类级软件制品贡献门槛。

### Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- 年份 / 期刊：2024 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：本文核心贡献是设计和评估一个名为FleetPower的决策支持系统（DSS），该系统实时分配多产品资源（SEV电池）到租赁和电力平衡市场。制品类别明确（DSS），独立于单一案例（可用于其他多产品资源）。作者设计了可复用的五阶段机制（数据收集、规划、投标、再规划、执行），并明确提供蓝图供类似场景推广。评估指标（利润、利用率、决策准确性）直接归因于DSS设计机制，而非仅验证底层算法。因此满足全部七道gate，属于类级软件制品贡献。

### Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- 年份 / 期刊：2023 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：论文的核心贡献直接指向密码强度计这一类软件制品的设计：作者在不改变底层算法的情况下，通过ELM理论设计并在实际密码强度计中实现了三种说服性反馈机制，并通过受控实验和实地实验证明这种设计改进能显著提高用户密码强度。软件部署是密码强度计类别的真实实例，且贡献明确泛化到该类软件的呈现组件设计，而非仅报告某个特定案例或纯算法效果。因此满足所有类级贡献门槛。

### Augmenting Social Bot Detection with Crowd-Generated Labels

- 年份 / 期刊：2023 / Information Systems Research
- 贡献对象 / 推广范围 / 软件角色：software_artifact_class / explicit_within_artifact_class / core_research_contribution
- 结论：文章明确以'社交机器人检测系统'这一可识别软件制品类别为贡献目标，提出了一个结合人群反应和言语行为评估的可复用系统设计机制，并实际构建、运行和评估了一个符合该类别和机制的实例。核心贡献不是单纯的算法或领域政策，而是系统级的设计策略，且论文明确声称框架可推广到其他社交平台。所有七道门均满足，因此class_level_include为true。
