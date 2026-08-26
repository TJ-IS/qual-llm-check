# 统一严格筛选：红队复核结果

- Stage 1候选：39
- 红队完成：39
- 最终纳入：27

## 最终纳入

### Gamifying knowledge sharing in humanitarian organisations: a design science journey

- 年份/期刊：2020 / European Journal of Information Systems
- 判定：核心成功指标为系统日志中的访问次数、新增条目数和评论/点赞数，完全客观，且这些指标是H1a/H1b的主要因变量；主观的sociometric status感知和专家质量评分是机制解释或补充验证，不替代客观核心目标。作者实际设计并运行了Graasp KMS中的游戏化个人资料和虚拟水族箱组件，并通过现场A/B测试和实验室实验将参与度提升归因于这些设计机制。贡献指向可推广的KMS游戏化反馈设计类别，而非单纯算法、仿真或一次性案例方案。

### Design Principles for Signal Detection in Modern Job Application Systems: Identifying Fabricated Qualifications

- 年份/期刊：2020 / Journal of Management Information Systems
- 判定：文章核心目标是客观识别求职申请中的虚构资质，使用由自我报告变化规则生成的确定标签，并以分类准确率、精确率、召回率和F1作为核心结果；作者设计并实际运行了SIGHT原型系统；贡献明确指向一类可复用的求职申请信号检测软件系统的设计原则，符合三个模块的全部条件。红队复核未发现足以推翻纳入的反证：核心指标并非主观量表，原型并非算法包装或实验场景，泛化声明指向制品类别而非仅方法迁移。

### A decision support system for home dialysis visit scheduling and nurse routing

- 年份/期刊：2020 / Decision Support Systems
- 判定：客观指标：核心成功指标为总行驶距离、总行驶时间、所需护士数和成本节省，均为可审计事实，且是文章设计目标和核心贡献；评价将HDSS与人工计划对比。真实软件制品：作者不仅提出MILP模型，还设计、实现并实际运行了完整DSS（HDSS），包括优化模块、地图模块、用户界面、可视化与报告模块；系统在TOH真实数据上运行并获得部署批准；指标改善归因于该系统的路线生成与交互机制。类级贡献：文章明确将自身定位为家庭健康护理排程路由问题中少数DSS开发工作之一，并声称HDSS可移植到其他医院/地区的家庭透析项目，核心可复用机制为模块化DSS架构、可参数化多目标MILP组件、地图集成和用户中心界面；移除TOH案例和专门界面后仍保留对同类DSS的设计知识。红队检查未发现推翻证据：客观指标不是实验行为因变量；系统不是仅有数学模型的Web包装，而是实际实现和运行的多模块DSS；泛化声明明确针对同类诊所/程序；当前系统已部署日常使用而非仅未来计划；核心指标不依赖人工语义/质量判断。

### Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice

- 年份/期刊：2020 / MIS Quarterly
- 判定：红队复核未发现推翻纳入资格的证据。客观指标为系统日志记录的真实处方调整行为和预设药物成本，均不依赖主观语义评价；核心目标明确为通过软件系统降低医疗成本，成本降低是最终贡献而非次要变量；作者设计并实际运行了一个成本敏感临床推荐系统原型，160名真实处方者使用，行为结果由系统记录；贡献声明明确面向'effective real-time healthcare recommender systems'这一软件制品类别的设计，提出了成本框架、时间压力处理、用户适配等可复用机制，而非一次性案例解决方案。因此三个模块全部通过，strict_include为true。

### Ingredients for successful badges: evidence from a field experiment in bike commuting

- 年份/期刊：2020 / European Journal of Information Systems
- 判定：客观指标方面，本文以每周骑行天数为最终目标和核心因变量，数据由RFID自动记录，完全客观且不涉及主观评价或语义判断；文章明确以提升目标行为（骑行）为核心设计目标。软件制品方面，作者在现有通勤信息系统中实际设计并集成了徽章组件（奖励、标志符、完成逻辑），重新设计了新闻通讯和仪表板并进行了七周运行，客观骑行天数的改善可归因于这些徽章设计机制；分享链接虽然被故意限制为仅显示道歉页面，但仍是实际运行的用户可见功能，目的是隔离分享预期效应。类级贡献方面，文章针对徽章设计的一般性研究缺口，分解出可复用的徽章设计维度，贡献目标明确指向徽章/游戏化信息系统这一类软件，而非特定案例、算法或领域政策；移除案例和数据后仍保留对某类软件应如何设计的可推广知识。因此三项条件全部满足，红队复核未发现足以推翻的全文反证。

### A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- 年份/期刊：2023 / Journal of the Association for Information Systems
- 判定：客观指标DDAR是研究的核心因变量，直接度量个体评分向显示均值偏移的客观数值，不依赖主观语义判断；研究目标、假设和贡献声明均以降低bandwagon bias为核心。警告策略被明确称为debiasing artifact，并在Qualtrics实验中以可运行的弹窗、计时和拖拽排序交互方式实例化；其设计机制（风险提醒+排序任务）被定位为在线评分平台可采用的通用警告组件，而非单纯一次性实验材料或算法包装。因此三个模块全部通过，strict_include为true。

### Conversational Recommender Systems and natural language:

- 年份/期刊：2020 / Decision Support Systems
- 判定：客观指标门通过：论文以Accuracy、MAP、NQ、TPQ、IT、QD、HitRate@k等可由行为选择和日志计数得到的指标作为核心评价，这些指标独立于人的感受和语义好坏判断；虽然附带ResQue问卷，但问卷是补充性的主观测量且未显示交互模式间显著差异，不构成共同的主要成功标准。核心目标通过：RQ1-RQ4和实验评价均围绕通过软件设计提升推荐准确率和降低交互成本。真实制品通过：作者明确设计并实现了ConveRSE框架，包括五个可复用组件、三种交互模式和推荐/解释/critiquing功能，并在电影、图书、音乐三个领域实例中实际运行。类级贡献通过：贡献指向对话式推荐系统这一软件制品类别的设计知识，结论可迁移到同类CoRS的设计（如何时用按钮辅助自然语言）；移除具体领域和数据集后仍剩下可复用的CoRS组件和交互机制设计。红队复核未发现足以推翻纳入的反证：满意度问卷不是成功的主要判据，框架不是纯算法包装，泛化声明针对CoRS软件设计而非仅算法。

### Interleaved Design for E-Learning: Theory, Design, and Empirical Findings

- 年份/期刊：2024 / MIS Quarterly
- 判定：该文以电子学习后测成绩等完全客观的学习绩效作为核心设计目标和贡献指标；作者设计并实际运行了一款个性化电子学习系统，其核心机制为相关交错（related-interleaving）调度，包含弱主题检测、知识图谱和调度引擎，指标改善归因于该设计机制；贡献目标是可复用的电子学习会话设计/软件制品类别，而非仅算法、场景或一次性案例，因此三个模块均通过。

### ForeSim-BI: A predictive analytics decision support tool for capacity planning

- 年份/期刊：2020 / Decision Support Systems
- 判定：红队复核未发现足以推翻的强证据。客观指标方面：预测误差（PE/MAE/MAPE）以真实维护工时与预测值的确定性比较计算，核心成功标准完全是客观事实性指标，且作者明确以工具更准确预测和成本节省潜力作为核心贡献。软件制品方面：ForeSim-BI是可识别的维护能力规划DSS类别的实例，作者明确开发并实现了集成的四模块工具和LP自动区间选择机制，并用真实数据实际运行产生预测结果，CRediT软件贡献佐证了实现。类级贡献方面：作者明确声明该工具是维护规划决策支持工具的通用方案，适用于满足一般数据特征的广泛复杂产品系统；模块化预测-更新-仿真-推理流程和LP机制是可在同类DSS中复用的设计组件，不是单一算法或案例专用包装。虽然缺少界面和代码级实现细节，尚不足以推翻资格，因此strict_include保持true。

### Containing COVID-19 through physical distancing: the impact of real-time crowding information

- 年份/期刊：2020 / European Journal of Information Systems
- 判定：红队复核未发现足以推翻Stage 1纳入结论的证据。核心结果是实际选择行为（所选医疗诊所的拥挤等级），由实验系统直接记录且选项拥挤程度由操纵预先固定，完全符合客观可观测要求；提高用户选择低拥挤地点的概率是文章的研究问题、设计目标和核心实证贡献，健康焦虑等主观测量仅作调节或操纵检验。作者设计、实现并运行了虚构网站find-your-doctor.org，实际呈现CI及即时性提示机制，343名参与者实际完成选择，客观效果（4.6倍选择低拥挤地点）明确归因于该信息显示设计。文章将CI作为一个DSS功能特征引入数字选择环境并提出对显示CI的DSS类别（如诊所选择、超市拥挤度、实时交通容量等）可迁移的设计建议，类别与机制均独立于当前COVID-19医疗案例。红队特别检查项也未触发排除：软件不是算法或数学优化模型，作者面向一类软件的设计而非单个医院管理问题，网站实际运行而非未来部署，且核心成功指标不依赖语义真值或主观质量判断。

### A new emergency decision support system: the automatic interpretation and contextualisation of events to model a crisis situation in real-time

- 年份/期刊：2020 / Decision Support Systems
- 判定：客观指标方面：核心评价指标是事件解释、情境化和可视化的处理延迟，以及事件是否被确定性规则正确解释和情境化，均不依赖人的语义或偏好。核心目标方面：研究问题和贡献声明都指向构建能够实时采集、解释和情境化事件以更新通用态势图的决策支持系统，目标不是解释心理或组织理论，而是改善系统处理能力。软件制品方面：作者设计和实现了AIC信息系统，包括CEP引擎、消息代理、图数据库连通、可视化界面和事件模拟器，并在洪水案例上实际运行和测量。类级贡献方面：文章面向紧急决策支持系统这一软件类别，明确其架构可作为未来DSS研究的框架，可复用的机制（CEP规则查询情境模型、元模型支撑的解释/情境化规则、事件订阅与通用态势图更新）可迁移到其他复杂协作场景。因此三个模块均通过，strict_include为true。

### Unlocking the Power of Voice for Financial Risk Prediction: A Theory-Driven Deep Learning Design Approach

- 年份/期刊：2023 / MIS Quarterly
- 判定：红队复核未发现推翻Stage 1纳入的证据。本文以股票收益波动率这一完全客观、可审计的金融指标为核心预测目标，并以MSE、out-of-sample R²和期权交易收益作为核心成功指标，目标构念不依赖人的感受或语义判断。DeepVoice不是单纯算法研究：作者设计并实际运行了从数据采集、文本-音频对齐、声学特征提取、两阶段LSTM声文融合到元学习堆叠的完整系统组件，并通过与多种基线的对比和消融实验将预测改进归因于这些系统设计机制。作者采用设计科学框架提出meta-requirements、metadesigns并总结可泛化设计原则，将DeepVoice实例化为财务风险预测系统这一软件类别的实例，达到了类级软件制品贡献的要求。

### Designing Attentive Information Dashboards

- 年份/期刊：2022 / Journal of the Association for Information Systems
- 判定：客观指标方面，三项核心成功指标均为Tobii眼动仪自动记录的注视时长、注视次数、AOI间转移数和标准差，不依赖主观体验、语义判断或人工质量评分，属于完全客观且可复核的行为日志类指标，且文章没有将满意度等主观构念作为核心结果。核心目标方面，研究问题、设计原则、假设和贡献声明均指向通过设计attentive dashboard软件提升用户注意力管理和信息处理，客观眼动指标改善是设计效果的主要评价依据。真实软件制品方面，作者开发并实际运行了自研C#/.NET仪表盘软件，包含实时眼动追踪、注意力分析和个体化VAF反馈组件，指标改善可归因于该制品的反馈设计机制。类级贡献方面，文章明确贡献系统架构和DP1/DP2设计原则，对象是attentive information dashboards这一软件制品类别，当前实现是该类别的一个实例；移除具体案例后仍保留可复用的类级设计知识。红队检查未发现足以推翻纳入资格的反证。

### The crowd against the few: Measuring the impact of expert recommendations

- 年份/期刊：2020 / Decision Support Systems
- 判定：红队复核未发现推翻纳入的反证。核心指标全部为客观可审计行为或按固定公式计算的推荐属性；文章以提升平台使用等客观行为指标为最终设计目标与核心贡献，满意度问卷只是附加且无差异。作者实质修改并运行了真实推荐系统（加入专家推荐混合组件），并非仅提出算法或未来集成。贡献对象是推荐系统这一软件制品类别，机制（专家推荐列表混合展示）可迁移到其他同类系统，具备类级可复用设计知识。

### Designing Conversational Dashboards for Effective Use in Crisis Response

- 年份/期刊：2023 / Journal of the Association for Information Systems
- 判定：客观指标方面，透明交互、效率和有效性分别基于导航步骤日志、时间戳和事实答案，均为确定性可审计的客观指标，且这些指标是研究问题和设计理论的核心目标；主观自我效能仅作为操纵检验。软件制品方面，作者设计并实现了六个版本的危机响应对话式仪表板，包含自然语言交互、交互管理、NLP组件和对话式入门，并在271人实验中实际运行；指标改善被归因于这些设计机制。类级贡献方面，作者明确提出针对危机响应对话式仪表板这一软件类别的设计理论（DP1-DP3、系统架构、可测试命题），实例是COVID-19危机响应仪表板，但设计知识面向该类别并可迁移至其他危机实例，而非一次性案例解决方案。三个模块全部通过，因此严格纳入。

### Automated dynamic approach for detecting ransomware using finite-state machine

- 年份/期刊：2020 / Decision Support Systems
- 判定：客观指标：论文以勒索软件检测的准确性、TPR、FPR为核心目标和核心贡献；这些指标基于勒索软件/合法应用事实标签以及系统监控产生的行为事件，不依赖人工感受、语义或质量判断，满足客观可验证要求；核心目标是提升检测性能。软件制品：作者设计并实现了一个可识别的勒索软件动态检测系统，包含行为分析模块（文件监控、横向移动、系统资源、持久化四个监听组件）和决策模块（FSM状态机、状态变更监听器、告警与进程终止），实际作为Windows应用在guest OS中运行并评估；指标改善归因于监听机制和FSM状态转换机制而非仅底层算法。类级贡献：贡献声明明确指向一类通用勒索软件检测系统，FSM行为建模和四类监控机制是可进入同类检测系统的可复用设计；反事实检验表明移除特定样本和界面后仍保留可复用的系统设计知识；实际运行的检测系统是该类别的一个实例。红队复核未发现足以推翻的排除性反证，因此strict_include为true。

### Responsible cognitive digital clones as decision-makers: a design science research study

- 年份/期刊：2023 / European Journal of Information Systems
- 判定：红队复核未发现足以推翻纳入的证据。客观指标方面，核心成功指标是F1决策准确性、节省人时和运行流程数，均来自系统记录、事实性标签和可审计时间，且论文以提升这些客观指标为制品的核心设计目标与贡献。软件制品方面，Pi-Mind agent不是纯粹算法或模型包装，而是作者设计并实质改造的真实运行软件制品：个人价值系统、T|C-SGAN训练架构、决策本体、克隆生命周期和门户流程被实现并运行，F1提升与时间节省也被归因于该制品。类级贡献方面，论文面向“认知数字克隆决策代理”这一可反复实例化的软件制品类别提出设计原则和可复用机制，案例只是该类别的运行实例，而非一次性案例方案。主观社会影响仅为proof of use的补充情境，不构成共同核心成功标准。

### A novel decision support system for optimizing aircraft maintenance check schedule and task allocation

- 年份/期刊：2021 / Decision Support Systems
- 判定：红队复核未发现足以推翻初步纳入的反证。(1) 客观指标：核心成功度量是未使用FH/FC、A/C检总次数、每架飞机货币收益/节省/成本和系统运行时间，均由飞机使用参数、检查次数和航空公司固定经济参数确定，不依赖主观质量或语义判断；主观性仅存在于航空公司专家对可行性的确认，并非核心成功标准。(2) 真实软件制品：文章不是只给出算法，而是设计和实现了一个可识别的DSS软件类别（AMPO），包括数据库/模型/GUI三层、三个可运行优化模块和人工修改约束后重优化的交互机制；系统已转换为exe、在51架飞机真实数据上运行并生成3年排程、6万任务分配和班次工卡。将指标改善归因于DSS整体设计（集成排程/任务分配/轮班）和模型层的组织机制，而不仅是某个算法；AMPO-1/2分别引用作者和合作者已发表的DP/WFD算法，但本文贡献在于它们被实现、集成并作为DSS模块运行，GUI和交互机制也实际存在。(3) 类级贡献：论文的贡献声明对象是“第一个同时优化维修检查排程和任务分配的DSS”这一类DSS，且从文献对比指出现有商业/学术DSS缺少自动优化功能；作者明确称框架可调整用于火车/公交维修等同类排程DSS，而非仅声称算法可迁移到其他数据集。移除航空公司案例和专用界面后仍留下DSS架构、模块分解、bin机制、轮班工作流和用户交互-重优化机制等可复用设计知识。因此严格纳入条件继续成立。

### An interactive decision support system for real-time ambulance relocation with priority guidelines

- 年份/期刊：2022 / Decision Support Systems
- 判定：红队复核未发现足以推翻纳入的反证。客观指标方面，核心成功指标是响应时间、覆盖率、可用车辆数和工作时长，均为可审计、可确定性计算的运营事实，不依赖人对质量或语义的判断，且摘要、第5节和结论均以其改善作为DSS价值证据。软件制品方面，作者不是只写了优化模型或算法脚本，而是设计了并实现了包含数据库、过程模型、GUI、求解器集成的DSS，并以真实数据运行一周仿真；改进可归因于DSS内部实际运行的再定位决策组件。类级贡献方面，目标明确指向“实时救护车再定位DSS”这一类可重复实例化的软件系统；事件触发流程、动态覆盖数修正、工作量约束和RRARR优先级指南是可迁移至同类系统的功能结构，德黑兰案例只是该类软件的一个运行实例。RRARR中的主观输入和交互式选择不是核心成功指标，也不削弱客观绩效目标的主导地位。

### Animation as a dynamic visualization technique for improving process model comprehension

- 年份/期刊：2021 / Information & Management
- 判定：客观指标方面，核心结果变量是过程模型理解测试得分，答案由专家依据BPMN控制流语义预先确定，属于可验证事实的固定答案计分；主观认知负荷和感知有用性仅为补充探索结果。核心目标方面，论文的核心假设和贡献以动画提升过程模型理解绩效为中心，且回归分析显示动画具有显著正向效应。软件制品方面，作者设计并实际实现了自适应动画环境，具备颜色变换、活动状态、时间抽象和两级自适应交互机制，194名参与者实际使用。类级贡献方面，该环境属于过程建模工具动画可视化这一可识别软件类别，作者明确主张其可集成到工业建模工具；移除具体模型、数据集和实验界面后，仍留下关于这类工具动画与交互设计机制的可复用知识。因此三个模块均通过。

### Assessing and Enhancing Adversarial Robustness of Predictive Analytics: An Empirically Tested Design Framework

- 年份/期刊：2022 / Journal of Management Information Systems
- 判定：客观指标：核心成功指标是对抗鲁棒性（性能比和性能-扰动曲线下面积），基于固定spam标签和模型输出计算，不依赖人类体验、语义质量或偏好；研究问题、摘要和贡献声明均以提升该客观指标为核心目标。真实软件制品：ARText不是算法抽象，而是被设计为文本分类系统，包含对抗样本生成、鲁棒性度量、bagging集成和迭代对抗重训练等实质组件，并以设计图和算法说明其构造，在两个数据集上实际运行和评价；指标改善被归因于这些组件设计（集成学习的多样性策略和对抗重训练），而非单纯底层算法。类级贡献：文章以设计框架和可复用设计原则为核心贡献，目标指向预测分析/文本分类类软件应如何评估和增强对抗鲁棒性；ARText是该类软件的一个实例，删除具体数据集和界面后剩留的是可进入同类系统的组件设计知识。红队复核未发现推翻性反证：虽然部分标签来自人工标注，但垃圾/非垃圾属于可外部核验的事实类别；实验以离线方式评价系统组件，但系统本身被实现和运行，且这不是仅未来部署的概念。

### Overcoming Breakdowns in Customer-Chatbot Interaction: Design and Impact of Collaborative Repair Strategies

- 年份/期刊：2026 / MIS Quarterly
- 判定：红队复核未发现推翻Stage 1纳入的证据。该文核心目标是通过软件设计提升客户服务聊天机器人故障解决的客观行为表现；故障解决率和立即放弃率是基于对话日志的完全客观指标，且文章明确称其为最重要的结果。作者在真实运行系统中实现并评价了协作式修复组件（故障类型学、自适应修复消息、自适应修复类型、实时故障处理），而非仅提出算法或包装。贡献面向'客户服务聊天机器人修复策略'这一类软件的可复用设计，元设计明确为类级解决方案，并可作为其他公司蓝图。主观满意度/反馈作为辅助影响检验，不构成共同主要成功标准。因此三个模块全部通过。

### Enhancing User Privacy Through Ephemeral Sharing Design: Experimental Evidence from Online Dating

- 年份/期刊：2025 / Information Systems Research
- 判定：红队复核未发现推翻Stage 1纳入的证据。客观指标为系统记录的照片数、含人脸照片数、匹配数和接收方消息数，均为不依赖主观感受或语义评价的外部可观察事实；研究问题和贡献声明明确以提升这些客观指标为核心，在线实验中的隐私顾虑和披露意愿仅作为机制解释，不是核心成功标准。短暂分享不是算法、仿真或理论框架，而是在Summer生产系统Version 3.8.2中实际实现并随机投放的软件组件（匹配请求页照片上传按钮、弹窗、短暂可见且不可追踪的技术约束），效果可归因于该组件设计。贡献面向在线匹配/交友平台这一可辨识软件制品类别的可复用设计模式，并明确扩展至其他隐私敏感平台；移除Summer案例、数据集和专门界面后，仍保留关于这类平台应如何在初始请求阶段设计短暂分享功能的可推广知识。因此三个模块全部通过，strict_include为true。

### HyperCARS: Using Hyperbolic Embeddings for Generating Hierarchical Contextual Situations in Context-Aware Recommender Systems

- 年份/期刊：2025 / Information Systems Research
- 判定：核心目标是通过 HyperCARS 组件提升上下文感知推荐的客观性能（RMSE、MAE、Hit@K、MRR@K），这些指标基于真实交互记录和固定计算公式，不依赖主观感受或语义优劣判断；聚类质量和可解释性代理指标也是客观计算的，且可解释性仅作为附加贡献。论文明确设计并实际运行了 CARS 的核心组件机制（双曲 VAE 嵌入+层次聚类生成 hcs+松耦合接入推荐模型），改进可归因于该组件设计。贡献指向 CARS 类软件可复用的上下文表示组件，而非单一数据集或算法包装。解释性没有以人类主观评分作为共同主要成功标准，因此三个模块全部通过。

### Smart Markets for Real-Time Allocation of Multiproduct Resources: The Case of Shared Electric Vehicles

- 年份/期刊：2024 / Information Systems Research
- 判定：红队复核未发现足够反证。核心贡献是FleetPower这一DSS，通过真实数据参数化的离散事件模拟运行，核心评价指标为利润、利用率、决策准确性，均属完全客观可测结果；研究目标和贡献声明明确指向提升这些客观指标。FleetPower被呈现为可推广到共享电动车、共享出租车、零工经济、热电联产等多产品实时分配DSS类别的五阶段蓝图，移除具体城市与数据后仍保留可复用的DSS组件设计知识。虽然实现证据主要依赖模拟而非真实部署，且文章以‘conceptual approach’起笔，但五阶段机制被明确称为DSS并实际运行，因此三类资格均通过。

### Augmenting Social Bot Detection with Crowd-Generated Labels

- 年份/期刊：2023 / Information Systems Research
- 判定：客观指标：核心成功指标为机器人检测的precision/recall/F1/AUC及time-to-detection，面对的是账号是否为bot这一外部事实标签；ground truth虽是众包报告但代表可核验账号类别，非主观体验或语义质量评价；提升检测性能是RQ1-3和摘要、引言、结论中的核心目标与贡献。真实制品：论文实现了一个可识别的社交机器人检测系统，具体设计了crowd reaction特征生成、BERT中间分类组件和speech act可信度加权机制，并在Reddit真实数据、2019新数据和实时检测模拟中实际运行评价，性能提升归因于该制品设计而非单纯底层BERT算法。类级贡献：作者明确声明系统可部署到任何社交平台、可自然扩展到已有检测系统、并可作为检测其他算法生成内容的模型基础；反事实移除Reddit案例后仍保留面向社交机器人检测系统类别的人群反应特征和speech act加权组件设计知识。红队检查未发现推翻性反证；红队担心的主观语义真值仅存在于中间特征生成器，不构成核心成功指标，且bot/nonbot事实标签可脱离人类感受成立。

### Ephemeral State-Dependent Recommendation for Digital Content

- 年份/期刊：2025 / Information Systems Research
- 判定：核心结果指标均为平台日志与交易记录的客观行为（阅读率、阅读时长、支付、溢出阅读），不存在以主观语义评价作为成功标准；研究问题和贡献声明以状态依赖推荐方案带来消费/利润提升为核心。作者通过与真实电子书平台合作，在10.8万用户上实际运行状态依赖推荐组件，实现了对推荐系统中策略-状态配对机制的设计、检验和量化。该机制被明确表述为可适用于不同数字内容类型和平台的可复用设计，而非一次性案例或仅算法泛化声明；因此符合三族严格标准。
