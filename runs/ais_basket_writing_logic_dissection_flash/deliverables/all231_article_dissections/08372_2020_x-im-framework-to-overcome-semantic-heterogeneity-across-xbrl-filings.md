# X-IM Framework to Overcome  Semantic Heterogeneity Across XBRL Filings

- 作者：Dapeng Liu; Ugochukwu Etudo; Victoria Yoon
- 年份 / 期刊：2020 / Journal of the Association for Information Systems
- DOI：10.17705/1jais.00626
- 源文件：08372_2020_x-im-framework-to-overcome-semantic-heterogeneity-across-xbrl-filings.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：problem_theory_design_test_return
- 置信度：0.88

## 文章级论证概况

- 核心问题：如何设计一种全自动算法，将不同XBRL申报文件中的XBRL元素准确映射到上层本体（投资者本体）中的财务概念，以克服XBRL申报之间的语义异构？

- 制品与设计：X-IM（XBRL Indexing-based Mapping）框架，由EDGAR网络爬虫、IOnto生成器和IBC学习器三部分组成；核心设计是利用XBRL标签链接库中的人类可读标签术语和设计性信息（余额类型、期间类型），构建索引本体（IOnto），并通过基于索引的分类器（IBC）将XBRL元素映射到投资者本体中的财务概念。

- 客观结果：在S&P 100公司2011和2012财年10-K文件上，X-IM的总体精确率达到0.998，召回率0.869-0.922，F值0.923-0.951；显著优于现有最先进水平FinCEM（精确率0.878，召回率0.752，F值0.796）。

- 核心贡献：作者声称：（1）提供了一个体现表示理论（representation theory）中本体清晰度（ontological clarity）的IT制品X-IM；（2）通过实证证明，纠正数据标准语法中的构造赤字（construct deficit）和构造冗余（construct redundancy）能使该语法生成的脚本更可互操作，从而将表示理论扩展到语义互操作领域；（3）证明了XBRL标签链接库中的人类可读标签术语富含语义信息，可有效支持异构XBRL元素的映射。

- 整篇论证链：论文从美国SEC强制采用XBRL但实际利用率低、不同公司申报文件间互操作性差的现象出发，将问题定性为语义异构。作者指出现有基于语义Web和本体映射的解决方案要么没有提出完整的映射策略，要么映射精度有待提高，且往往缺乏理论支撑。在此缺口上，作者引入表示理论中的本体清晰度模型，论证US GAAP分类标准（UGT）存在构造赤字（允许扩展元素）和构造冗余（同一概念可有多个XBRL元素标签），导致生成的XBRL实例文档不能互操作。基于这一理论诊断，论文提出X-IM框架：通过投资者本体解决构造赤字问题，通过利用标签链接库中label terms的向量化语义相似度解决构造冗余问题。系统架构包括EDGAR爬虫、IOnto生成器和IBC学习器。评价部分采用信息检索标准指标（精确率、召回率、F值），通过四个实验：阈值灵敏度分析、投资者本体有无的消融实验、与FinCEM的比较实验、训练数据规模效应实验，证明X-IM在精确率和F值上显著优于现有方法。最后，论文将结果提升为一般设计知识：当数据标准存在构造赤字和构造冗余时，利用语法元数据中的并行名义信息可以自动增强标准的可互操作性；并将理论贡献定位为将表示理论扩展到语义互操作领域。

## 类型与写作弧线判定

- 论文主类型判定：作者明确声明遵循设计科学研究方法（DSRM，Peffers et al., 2007），整个研究按问题识别、目标明确、设计策略、展示与评价、沟通的流程展开。研究交付的是一个IT制品（X-IM框架），包括系统架构、算法和实现细节，并用标准信息检索评价指标进行评价。虽然论文有较强的理论（表示理论/本体清晰度）指导，但其核心脉络是DSR的'需求—构建—评价—设计知识'，而非理论推导制品差异并实验检验的纯理论验证模式。

- 主导写作弧线判定：全文弧线为：现实问题（XBRL语义异构导致无法自动化消费）→理论（表示理论/本体清晰度，构造赤字与构造冗余）→设计（X-IM，投资者本体+标签术语向量分类）→检验（四个实验，消融+比较）→返回理论（纠正语法缺陷提高脚本互操作性，将表示理论扩展到语义互操作）。虽属DSR论文，但理论与设计的绑定非常紧密，理论在设计和检验中均被显性调用，因此写作弧线属于问题—理论—设计—检验—回到理论。

## 研究开展程序

- study_or_phase_count：8

- 研究阶段总序列：研究分为八个阶段：第一阶段（文献综述和理论化）将XBRL互操作问题定性为语义异构，引入表示理论的本体清晰度模型，识别UGT的构造赤字和构造冗余；第二阶段（设计需求生成）基于理论提出投资者本体（解决构造赤字）和标签术语利用（解决构造冗余）两大设计要求，并形式化假设H1a-c和H2a-c；第三阶段（制品构建）实现EDGAR爬虫、IOnto生成器、IBC学习器；第四阶段（阈值敏感性分析）确定相似度阈值1.2；第五阶段（投资者本体消融实验）检验H1a-c，发现投资者本体显著提升召回率和F值，但对精确率提升不显著；第六阶段（与FinCEM比较实验）检验H2a-c，发现X-IM在精确率和F值上显著优于FinCEM，但召回率差异不显著；第七阶段（训练数据规模实验）验证10家公司训练的有效性与效率；第八阶段（讨论与贡献）将结果上升为设计知识和理论贡献，并讨论边界。

### studies_or_phases

#### 1. 理论与问题定性阶段

- order：1

- name_cn：理论与问题定性阶段

- question_cn：XBRL申报文件间为什么不能互操作？语义异构的根本原因是什么？

- inputs_and_setting_cn：现有文献、Zhu & Wu (2011)的互操作性度量数据、SEC政策文件、从业者报告（如EY 2017评论信、CFO杂志报道）

- designed_or_compared_object_cn：无制品；对US GAAP分类标准（UGT）进行本体清晰度诊断

- baseline_control_or_counterfactual_cn：无；通过与表示理论的四项缺陷框架对照，评估UGT存在哪些缺陷

##### objective_metrics

（空）

- analysis_method_cn：概念论证和理论分析

- main_result_cn：UGT存在构造赤字（刻意允许扩展元素）和构造冗余（同一财务概念可对应多个XBRL元素），导致脚本不可互操作；构造过剩和构造过载不存在

- argumentative_role_cn：建立理论透镜，将互操作问题从技术性能问题转化为语法缺陷问题，为设计决策提供合法性依据

- remaining_uncertainty_cn：理论诊断是论证性的，尚不清楚针对这些缺陷设计的制品是否真的能提高互操作性

- link_to_next_phase_cn：理论诊断产生设计要求：用投资者本体弥补构造赤字，用标签术语向量解决构造冗余

##### evidence_pointers

1. Section 4（Theoretical Background）

2. Figure 1（Ontological Clarity and Semantic Interoperability Model）

3. Section 4.1（Construct Deficit）

4. Section 4.2（Construct Redundancy）

#### 2. 假设生成阶段

- order：2

- name_cn：假设生成阶段

- question_cn：针对构造赤字和构造冗余的设计选择是否可检验地改善映射性能？

- inputs_and_setting_cn：表示理论、投资者本体概念、XBRL标签链接库知识

- designed_or_compared_object_cn：两个设计差异：有无投资者本体、有无标签信息

- baseline_control_or_counterfactual_cn：无投资者本体的X-IM；无标签信息的映射方法

##### objective_metrics

（空）

- analysis_method_cn：假设形式化

- main_result_cn：生成H1a-c（投资者本体提升精确率、召回率、F值）和H2a-c（标签信息提升精确率、召回率、F值）

- argumentative_role_cn：将理论命题转化为可操作、可检验的实验假设，为后续实验提供靶子

- remaining_uncertainty_cn：假设是否成立未知；阈值等实现参数也需要确定

- link_to_next_phase_cn：假设需要具体制品实现来检验；阈值需先通过敏感性分析确定

##### evidence_pointers

1. Section 4.3（Hypotheses）

#### 3. 制品构建阶段

- order：3

- name_cn：制品构建阶段

- question_cn：如何将投资者本体和标签术语向量化的思想实现为可运行、可移植的X-IM系统？

- inputs_and_setting_cn：SEC EDGAR网站的10-K交互式财务报表、S&P 100公司的XBRL文件

- designed_or_compared_object_cn：X-IM系统的三个组件：EWC（EDGAR爬虫）、IOnto生成器、IBC学习器

- baseline_control_or_counterfactual_cn：无直接对照；通过IOnto避免频繁访问复杂XBRL本体，提高效率

##### objective_metrics

（空）

- analysis_method_cn：系统实现（Python、Selenium、JAVA/JENA、Protégé）

- main_result_cn：实现了可自动从EDGAR提取XBRL元素、标签术语和设计性信息并构建索引本体的系统；IBC学习器通过向量化Jaccard相似度计算公式实现分类映射

- argumentative_role_cn：提供可被评价的具体制品，使理论设计决策有可操作载体

- remaining_uncertainty_cn：系统性能未知；阈值需要确定；与现有方法相比是否更优未知

- link_to_next_phase_cn：系统实现后需要确定相似度阈值并启动正式评价实验

##### evidence_pointers

1. Section 5（Framework Design: X-IM System for XBRL Ontologies Mapping）

2. Figure 3（System Architecture）

3. Figure 10（IOnto Generation Method）

4. Figure 14（Logics of Indexing-Based Classification Method）

5. Formula (1)-(3)

#### 4. 实验1：阈值灵敏度分析

- order：4

- name_cn：实验1：阈值灵敏度分析

- question_cn：相似度阈值取什么值能最好地平衡精确率和召回率？

- inputs_and_setting_cn：S&P 100中10家随机公司的2011年10-K文件（训练），92家公司2012年10-K文件（测试）

- designed_or_compared_object_cn：阈值0.1到更高值的不同设定

- baseline_control_or_counterfactual_cn：不同阈值之间的比较

##### objective_metrics

1. F-measure

2. precision

3. recall

- analysis_method_cn：系统遍历：以0.1为增量计算各阈值下的精确率、召回率和F值

- main_result_cn：阈值1.2产生最高F值，故选择1.2作为实现阈值

- argumentative_role_cn：作为参数选择的合理性说明，为后续实验的可信度奠定基础；同时承认阈值影响结果，增加方法透明性

- remaining_uncertainty_cn：阈值是否在更大数据集或不同年份上仍然最优，未直接验证

- link_to_next_phase_cn：确定实现参数后，进入正式假设检验实验

##### evidence_pointers

1. Section 6.2（Experiment 1: Sensitivity Analysis of Threshold）

2. Figure 16（Threshold Effects on F-Measures）

#### 5. 实验2：投资者本体消融实验

- order：5

- name_cn：实验2：投资者本体消融实验

- question_cn：嵌入投资者本体是否为X-IM带来显著性能提升？（检验H1a、H1b、H1c）

- inputs_and_setting_cn：训练：10家随机公司的2011年10-K；测试：92家公司2012年10-K，18个财务概念

- designed_or_compared_object_cn：有投资者本体的X-IM vs 无投资者本体的X-IM

- baseline_control_or_counterfactual_cn：无投资者本体的X-IM作为消融对照

##### objective_metrics

1. precision

2. recall

3. F-measure

- analysis_method_cn：Wilcoxon符号秩检验（非参数配对检验，N=18个财务概念）

- main_result_cn：召回率显著提升（Z=2.934，p=0.003），F值显著提升（Z=2.934，p=0.003）；精确率提升不显著（Z=1.604，p=0.109），H1a不获支持，H1b、H1c获支持

- argumentative_role_cn：通过消融实验证明投资者本体（构造赤字解决方案）具有可测度的贡献，尤其提升了检索完整性

- remaining_uncertainty_cn：实验只针对2012年测试数据，跨年度泛化尚未验证；精确率不显著可能源于X-IM本身的精确率已接近天花板（0.962→0.998）

- link_to_next_phase_cn：需要与现有最先进方法比较，证明整体优势而非仅内部消融优势

##### evidence_pointers

1. Section 6.3（Experiment 2: Effect of Investor’s Ontology）

2. Table 4（Descriptive Statistics）

3. Table 5（Wilcoxon Signed-Ranks Test）

#### 6. 实验3：与FinCEM比较实验

- order：6

- name_cn：实验3：与FinCEM比较实验

- question_cn：与最先进方法FinCEM相比，X-IM的映射性能是否显著更优？（检验H2a、H2b、H2c）

- inputs_and_setting_cn：训练：10家随机公司2011年10-K；测试：82家公司2011年10-K和92家公司2012年10-K；18个财务概念（与FinCEM评价中9个概念重叠并扩展）

- designed_or_compared_object_cn：X-IM vs FinCEM

- baseline_control_or_counterfactual_cn：FinCEM作为现有最先进基准

##### objective_metrics

1. precision

2. recall

3. F-measure

- analysis_method_cn：描述性统计比较+Wilcoxon符号秩检验（36个观测值：18概念×2年份）

- main_result_cn：X-IM总体：精确率0.998 vs 0.878（Z=2.519，p=0.012，显著），召回率0.896 vs 0.752（Z=1.606，p=0.108，不显著），F值0.937 vs 0.796（Z=2.013，p=0.044，显著）；H2a、H2c获支持，H2b不获支持

- argumentative_role_cn：展示X-IM相对现有最先进方法的整体优势，证明'标签信息+设计性信息'的设计确实优于'仅计算链接库'的FinCEM

- remaining_uncertainty_cn：召回率虽然提高但未达统计显著；比较只涉及单一最先进基线，未与其他较旧方法逐一比较；测试年份只有两年

- link_to_next_phase_cn：还需检验训练数据规模对性能的影响，以证明小训练集的有效性并回应成本问题

##### evidence_pointers

1. Section 6.4（Experiment 3: Comparative Performance Analyses）

2. Table 6（Evaluation Results of X-IM and FinCEM）

3. Table 7（Comparisons on Descriptive Statistics）

4. Table 8（Wilcoxon Signed-Ranks Test）

#### 7. 实验4：训练数据规模效应

- order：7

- name_cn：实验4：训练数据规模效应

- question_cn：X-IM对训练数据规模是否敏感？小训练集（10家公司）是否足够？

- inputs_and_setting_cn：2011年10-K标签链接库生成10、20、40家公司的训练集；2012年标签链接库测试

- designed_or_compared_object_cn：三种训练集大小（10、20、40家公司）

- baseline_control_or_counterfactual_cn：不同训练规模之间的比较

##### objective_metrics

1. F-measure

2. computational time

- analysis_method_cn：对比F值和计算时间

- main_result_cn：训练集从10家扩到40家仅使平均F值从0.923提升到0.928（0.542%），但计算时间从117.9s增至178.9s（51.74%）；10家公司训练高效且有效

- argumentative_role_cn：回应了实际部署可行性问题（小样本成本低），同时排除训练集规模是性能优势来源的替代解释

- remaining_uncertainty_cn：实验只测试S&P 100样本；规模效应在其他行业或更长年份窗口中可能不同

- link_to_next_phase_cn：为讨论部分'开源、经济可行、可推广'的主张提供支撑

##### evidence_pointers

1. Section 6.5（Experiment 4: Effect of Training Data Sizes）

2. Table 9（F-Measure with Training Sizes of 10, 20, and 40 Companies）

#### 8. 讨论与理论返回阶段

- order：8

- name_cn：讨论与理论返回阶段

- question_cn：实验结果如何上升为设计知识和理论贡献？边界条件是什么？

- inputs_and_setting_cn：全部实验证据、现有文献（表示理论、XBRL互操作）

- designed_or_compared_object_cn：不设计新对象；整合证据并提炼一般化命题

- baseline_control_or_counterfactual_cn：无

##### objective_metrics

（空）

- analysis_method_cn：论述性综合

- main_result_cn：提出：（1）理论贡献：纠正语法构造缺陷能提高脚本互操作性，将表示理论扩展到语义互操作；（2）设计知识：利用标签链接库的并行名义信息（parallel nominal information）可实现高效映射；（3）适用条件：存在关于同一概念足够多的并行名义信息时，方法有效；（4）开源和民主化获取结构化财务数据的愿景

- argumentative_role_cn：闭合引言中'现有方法缺乏理论洞察和一般化知识'的缺口，将X-IM从一次性技术方案提升为有理论支撑的设计知识

- remaining_uncertainty_cn：一般化到非XBRL领域未经实证；部分财务概念未出现在报表中需要计算推理，超出当前制品能力

- link_to_next_phase_cn：指出来来研究方向：添加推理能力、主题分析、多级学习器

##### evidence_pointers

1. Section 7（Conclusion and Discussion）

## 各部分修辞架构

### abstract_moves

1. CONTEXT: XBRL语义异构阻碍了业务报告管道全自动化

2. PRACTICAL_STAKES: 现有方法映射精度不足

3. GAP: 需要改进映射精度

4. ARTIFACT_PRESENTATION: 提出X-IM框架，利用表示理论

5. DESIGN_FEATURE: 利用XBRL标签链接库作为标签术语与财务概念关系的存储库

6. RESULT: 标准信息检索指标下显著优于现有方法

### introduction_moves

1. CONTEXT: SEC 2009年强制XBRL，US GAAP分类标准（UGT）

2. PHENOMENON: SEC允许扩展元素；公司特定扩展元素导致互操作性低

3. PRACTICAL_STAKES: SEC自己不用XBRL数据；下游消费者购买商业数据库；企业抱怨标准问题多

4. PHENOMENON: 74%的XBRL报表含自定义标签，标记错误率高等

5. GAP: 现有方法ontologize XBRL但未解决异构标签；映射算法精度欠佳

6. LIMITATION: 现有设计缺乏理论洞察，不贡献一般化知识

7. RQ_OR_OBJECTIVE: 如何设计全自动算法将XBRL标签准确映射到上层本体财务概念？

8. THEORY_INTRO: 引入本体清晰度理论（表示理论）解释为何UGT下XBRL仍不互操作

9. CONTRIBUTION: 扩展表示理论到语义互操作领域

10. STUDY_OVERVIEW: 遵循DSRM，展示问题识别、目标、设计、评价、交流

### theory_and_knowledge_moves

1. PRIOR_KNOWLEDGE: 语义互操作文献的两类：数据模型开发 vs 半/全自动语义数据集成

2. LIMITATION: 数据模型开发不解决映射；标注差异使UGT自身不能自动互操作

3. PRIOR_KNOWLEDGE: Thiéblin等的双轴分类（输出、过程）

4. LIMITATION: 通用语义集成方法不针对XBRL特有情景，不利用标准存在这一事实，不贡献一般化理论

5. THEORY_INTRO: 表示理论（RT）的三个模型，重点为本体清晰度（表示模型）

6. THEORY_PROPOSITION: 本体清晰度四缺陷（构造赤字、构造过剩、构造冗余、构造过载）

7. MECHANISM: 任何语法缺陷导致生成脚本不可互操作

8. MECHANISM: UGT的构造赤字是故意的（扩展机制），构造冗余在于解释者的多种选择

9. EVIDENCE: 实践者经验、UGT规模、SEC简化努力、两个元素均可表示'净利润'的示例

10. REQUIREMENT: 需要用投资者本体补充构造赤字；需要用标签术语向量解决构造冗余

11. HYPOTHESIS_OR_PROPOSITION: H1a-c（投资者本体提升精确率、召回率、F值）和H2a-c（标签信息提升精确率、召回率、F值）

### artifact_design_moves

1. DESIGN_FEATURE: X-IM三组件——EDGAR爬虫、IOnto生成器、IBC学习器

2. METHOD_JUSTIFICATION: 用10-K而非10-Q，因其包含更丰富的XBRL元素集合

3. DESIGN_FEATURE: 利用标签链接库中的label linkbases

4. DESIGN_FEATURE: 获取设计性信息（余额类型、期间类型）辅助映射

5. DESIGN_FEATURE: IOnto（索引本体）将XBRL元素作为类、标签术语作为个体属性

6. DESIGN_FEATURE: 投资者本体封装等价财务术语（如short-term marketable securities, short marketable securities, short-term investments）

7. METHOD_JUSTIFICATION: 向量级相似度计算优于逐对相似度（如ProfitLoss与Net Income的词典相似度低但向量可能匹配）

8. DESIGN_FEATURE: 调整Jaccard相似度信号放大（0,1→[0,∞)）

9. DESIGN_FEATURE: 用设计性信息过滤假映射候选

10. IMPLEMENTATION: Selenium、XPath、正则表达式、JAVA/JENA、Python 2.7、Protégé

### evaluation_moves

1. METHOD_JUSTIFICATION: 使用Yu等（2009）正式本体评价方法，与先前XBRL互操作文献一致

2. BENCHMARK_OR_CONTRAST: 以FinCEM作为最先进基准

3. BENCHMARK_OR_CONTRAST: 建立18个财务概念（9个来自FinCEM指标+扩展）

4. METHOD_JUSTIFICATION: Wilcoxon符号秩检验（非参数，适合小样本非正态）

5. RESULT: 阈值1.2最优

6. RESULT: 投资者本体显著提升召回率和F值，但精确率提升不显著

7. RESULT: X-IM vs FinCEM，精确率显著高（0.998 vs 0.878），F显著高（0.937 vs 0.796），召回不显著（0.896 vs 0.752）

8. RESULT: 训练集规模10家已足够，扩大训练集只有微小提升但计算成本大增

### discussion_and_contribution_moves

1. CONTRIBUTION: 纠正标准差后脚本更可互操作，可视为表示理论的实例化

2. CONTRIBUTION: 标签链接库中的语义信息可提供异构XBRL元素的等价关系

3. BOUNDARY_CONDITION: 方法依赖同一概念存在足够并行名义信息的条件

4. PRACTICAL_STAKES: XBRL授权需下游价值的证明；X-IM可提供开源结构化财务数据

5. LIMITATION_AND_FUTURE: 缺失概念需计算推理；可增加推断能力；可增加主题分析；可建多级学习器

6. BOUNDARY_CONDITION: 方法可推广至其他存在并行名义信息的语义集成领域

## 理论/知识到设计的翻译

### 知识/理论基础

1. 表示理论（Representation Theory）/本体清晰度理论（Theory of Ontological Clarity, Wand & Weber, 1995）

2. 语义互操作/本体映射文献（Thiéblin et al., 2018; Heiler, 1995）

3. XBRL互操作文献（Chowdhuri et al., 2014; Etudo et al., 2017; Zhu & Wu, 2014）

4. 信息检索与自然语言处理中的词汇相似度/标签语义（Gefen & Larsen, 2017）

- 理论—设计耦合：direct

- 耦合判定理由：理论（本体清晰度）直接决定了两个核心设计选择：构造赤字→投资者本体；构造冗余→利用标签术语向量。假设H1a-c和H2a-c正是对这一理论翻译的检验；消融实验（删除投资者本体、对比无标签信息的FinCEM）直接证实了理论到设计的因果关系。

- 理论到设计翻译链：表示理论的本体清晰度主张（语法缺陷导致脚本不可互操作）→ 诊断UGT存在构造赤字和构造冗余 → 构造赤字的设计响应：构建'投资者本体'封装投资者常用等价财务概念，为UGT缺失的构造提供补充映射目标；构造冗余的设计响应：利用XBRL标签链接库中的人类可读标签术语构建向量化特征，通过Jaccard相似度聚合一组标签术语与投资者术语的相似度 → IOnto本体表示索引关系，IBC学习器进行分类映射 → 两种设计差异分别被消融实验（有无投资者本体）和比较实验（有标签信息X-IM vs 无标签信息的FinCEM）检验。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：构造赤字（construct deficit）：标准缺少代表真实世界概念的构造，导致脚本不可互操作

- mechanism_cn：UGT刻意允许扩展元素，公司自定义标签导致相同财务概念在不同文件中使用不同元素

- design_requirement_cn：需要提供一个补充的、稳定的概念层，使扩展元素可以被映射到统一概念

- artifact_choice_cn：显式定义投资者本体（investor’s ontology），封装投资者常用财务术语及其等义形式，作为上层映射目标

- evaluated_contrast_cn：有投资者本体的X-IM vs 无投资者本体的X-IM

- objective_result_cn：召回率显著提升（Z=2.934，p=0.003），F显著提升；精确率提升不显著（Z=1.604，p=0.109）

##### evidence_pointers

1. Section 4.1

2. Section 4.3（H1a-c）

3. Experiment 2（Table 4, Table 5）

#### 2. 2

- theory_or_knowledge_claim_cn：构造冗余（construct redundancy）：两个或多个构造映射到同一真实世界概念，导致脚本不可互操作

- mechanism_cn：UGT中同一财务概念（如net income）对应多个XBRL元素（us-gaap_ProfitLoss和us-gaap_NetIncomeLoss），不同编制者选择不同标签，但标签术语在词汇上接近

- design_requirement_cn：需要利用人类可读标签术语作为含义的指示器，对一组标签术语整体计算与投资者术语的相似度

- artifact_choice_cn：IBC学习器使用向量级相似度计算：每个XBRL元素对应其标签术语向量，用调整Jaccard相似度聚合后与投资者术语比较；并用设计性信息（余额类型、期间类型）过滤假候选

- evaluated_contrast_cn：X-IM（使用标签信息）vs FinCEM（使用计算链接库，无标签信息）

- objective_result_cn：精确率显著更高（0.998 vs 0.878，p=0.012），F显著更高（0.937 vs 0.796，p=0.044）；召回率不显著（0.896 vs 0.752，p=0.108）

##### evidence_pointers

1. Section 4.2

2. Section 4.3（H2a-c）

3. Experiment 3（Table 6, Table 7, Table 8）

#### 3. 3

- theory_or_knowledge_claim_cn：存在足够并行名义信息时，索引式映射可以有效解决异构性

- mechanism_cn：如果多主体使用同一概念的不同名义表达（label terms），则这些名义表达可被聚合为特征向量，用于分类映射

- design_requirement_cn：系统需要能自动从公共资源（EDGAR）中抽取XBRL元素、标签术语和设计性信息，构建可移植的索引本体

- artifact_choice_cn：IOnto（索引本体）将XBRL元素作为类、各公司使用的标签术语作为个体属性，并标注hasBalanceType和hasPeriodType，形成轻量级可移植本体

- evaluated_contrast_cn：IOnto的设计在逻辑上被训练数据规模实验隐含检验（10家公司训练vs 40家训练）

- objective_result_cn：10家公司训练平均F=0.923，40家公司训练平均F=0.928，差异微小；计算时间显著增加（117.9s→178.9s）

##### evidence_pointers

1. Section 5.3

2. Section 6.5（Table 9）

## 评价逻辑

### evaluation_modes

1. 消融实验（Ablation）：Investor ontology有/无

2. 基准比较（Benchmark comparison）：X-IM vs FinCEM

3. 参数敏感性分析（Threshold sensitivity analysis）

4. 训练集规模效应分析（Training size effect）

- why_these_evaluations_cn：论文需要证明：（1）X-IM整体优于现有最先进方法，故与FinCEM比较；（2）性能优势确实来源于理论指导的设计选择，故用消融实验分离投资者本体和标签信息的贡献；（3）系统需要实际可调参数，故做阈值敏感性分析；（4）小训练集部署是现实需求，故做训练规模分析以证明效率与有效性。四种评价共同构成从技术性能到设计知识到部署可行性的完整证据链。

- benchmark_and_contrast_chain_cn：以FinCEM为最先进基准（它在计算链接库上采用M3 Plus方法且全自动）→ 阈值敏感性分析确定X-IM自身的可调参数 → 消融实验检验投资者本体这个设计组件 → 与FinCEM比较检验标签信息+设计性信息整体设计 → 训练规模对照排除'大训练集才有优势'的替代解释 → 跨年度测试（2011、2012）排除单年偶然性。

### claim_evidence_ledger

#### 1. 投资者本体显著提升召回率和F值

- claim_cn：投资者本体显著提升召回率和F值

- evidence_cn：Wilcoxon检验：召回率Z=2.934, p=0.003；F值Z=2.934, p=0.003；精确率不显著（p=0.109）

- status_cn：部分支持：H1b、H1c支持，H1a不支持

- notes_cn：精确率不显著的可能解释是X-IM基线已接近天花板（0.962）

#### 2. 标签信息比无标签信息方法更优（H2a-c）

- claim_cn：标签信息比无标签信息方法更优（H2a-c）

- evidence_cn：X-IM vs FinCEM：精确率0.998 vs 0.878，p=0.012；F值0.937 vs 0.796，p=0.044；召回率0.896 vs 0.752，p=0.108

- status_cn：部分支持：H2a、H2c支持，H2b不支持

- notes_cn：召回率差异未达统计显著

#### 3. X-IM在整体上优于FinCEM（跨两年、跨18个概念）

- claim_cn：X-IM在整体上优于FinCEM（跨两年、跨18个概念）

- evidence_cn：Table 6显示2011和2012年X-IM在总体精确率、召回率、F值上均优于FinCEM

- status_cn：支持

- notes_cn：但逐概念比较中，部分概念（如Long-term debt、Cash generated by operating activities）FinCEM表现更好或相当

#### 4. X-IM在小训练集上高效且有效

- claim_cn：X-IM在小训练集上高效且有效

- evidence_cn：训练10vs20vs40公司，F值0.923→0.924→0.928，计算时间从117.9s增至178.9s

- status_cn：支持

- notes_cn：但未检验训练集规模与测试年份之间的交互

- internal_validity_strategy_cn：非参数检验处理小样本非正态问题；消融实验隔离设计组件；固定训练集、测试集分离；跨年份重复测试；训练公司随机选择增强代表性；阈值在实验前通过敏感性分析确定而非事后调整。

- external_validity_strategy_cn：以S&P 100跨行业公司为样本，覆盖多行业；使用2011、2012两个财年；与既往研究使用同一评价框架（Yu et al., 2009）和兼容的财务概念集；训练规模实验支持小样本泛化。

- what_is_not_actually_tested_cn：未直接检验表示理论'四项缺陷'的一般性主张，只检验了XBRL这一案例中的两个缺陷；未在不同司法管辖区/IFRS分类法上验证；未在真实投资者使用场景中进行用户研究；未测试系统对全新年份（如2013以后）的稳定性；未直接证明'下游消费者实际会使用X-IM输出'；召回率不显著的假设未得到解释性实验支持。

## 贡献闭环

- technical_claim_cn：X-IM在精确率、召回率、F值上优于现有最先进方法FinCEM，尤其在精确率上有显著优势（0.998 vs 0.878）。

- artifact_claim_cn：投资者本体被证明显著提升了召回率和F值，标签信息+设计性信息整体被证明显著提升了精确率和F值，说明X-IM中明确的设计组件（投资者本体、标签术语向量、设计性信息过滤）是性能优势的来源。

- mechanism_claim_cn：机制是：XBRL标签链接库中的人类可读标签术语蕴含财务概念的含义；向量化聚合标签术语可以通过词汇相似度桥接词面不同但语义等价的XBRL元素；设计性信息提供了附加的判别维度，可过滤错误候选。

- boundary_claim_cn：方法有效的前提是'存在足够并行名义信息'（sufficient parallel nominal information with respect to one concept）；在此条件下，索引式映射可在其他语义集成领域复用。

- reusable_design_knowledge_cn：（1）当语法允许扩展时，可用公开构建的投资者/用户上层本体补充构造赤字；（2）当语法由多编制者解释而产生构造冗余时，其元数据（标签链接库）中的名义标签可转化为索引特征以自动发现语义等价；（3）索引本体（IOnto）的构建可提高映射系统的效率和可移植性。

- theoretical_contribution_cn：将表示理论的本体清晰度模型从'语法评估'扩展到'语义互操作'：纠正语法缺陷会提高生成脚本的互操作性。论文将此表述为对表示理论的应用实例化，也是'纠正构造赤字和构造冗余以改善可互操作表示'的核验理论之一。

- how_discussion_closes_intro_gap_cn：引言指出现有方法存在两个问题：映射精度不足和缺乏理论洞察。讨论部分通过（1）报告显著更优的精确率和F值回答精度问题；（2）将X-IM的理论来源（表示理论）和一般化设计知识（并行名义信息、语法缺陷纠正）重新提出，回应'不贡献一般化知识'的缺口；（3）同时回扣现实利害：SEC和下游消费者不用XBRL的问题因X-IM而有了开源解决方案的可能性。

- overclaim_or_unsupported_leaps_cn：（1）将H2b（召回率）不显著归因于标签术语的判别力，但这是一种事后推测，未专门实验验证；（2）声称'显著优于现有方法'时，严格统计支持的是精确率和F值，而不是所有指标；（3）理论贡献的表述具有较强雄心（'纠正语法缺陷提高互操作性'），但只测试了两个缺陷、一个标准（UGT）和有限时间窗口（2011-2012），一般化需依赖边界条件的承认；（4）'开源=民主化'的主张带有政策修辞成分，未实证下游用户采用。

## 句级写作动作图谱

### 1. P1 S1

- order：1

- section：Abstract

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：XBRL中的语义异构阻碍了业务报告管道的完全自动化，而这正是SEC XBRL强制要求的动机。

- rhetorical_function_cn：开篇将论文的研究对象锚定在XBRL授权及其未实现的自动化目标上。

- depends_on_cn：无需先行信息。

- sets_up_cn：为后文提出'需要解决语义异构'这一目标提供背景框架。

- evidence_pointer：Abstract P1

### 2. P1 S2

- order：2

- section：Abstract

- locator：P1 S2

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有多种基于语义Web技术的方法被提出以缓解该问题。

- rhetorical_function_cn：承认已有工作，使论文不是从零开始，而是处于研究连续体中。

- depends_on_cn：S1确认问题存在。

- sets_up_cn：为后文指出这些方法的不足埋下伏笔。

- evidence_pointer：Abstract P1

### 3. P1 S3

- order：3

- section：Abstract

- locator：P1 S3

- move_code：LIMITATION

- paraphrase_cn：虽然一些方法有前景，但其解决语义异构的映射精度必须提高才能真正实现XBRL的收益。

- rhetorical_function_cn：直接指出现有方法的核心局限——精度不足，从而界定论文要解决的问题。

- depends_on_cn：S2介绍了已有方法。

- sets_up_cn：为提出X-IM框架并声明性能优势提供了问题空间。

- evidence_pointer：Abstract P1

### 4. P1 S4

- order：4

- section：Abstract

- locator：P1 S4

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：鉴于这一局限并遵循DSRM，作者开发了一个新框架X-IM，利用表示理论的表示模型来映射异构XBRL元素。

- rhetorical_function_cn：以方法论标签和理论标签介绍研究行动，声明论文的'设计科学'属性和理论依据。

- depends_on_cn：S3定义问题缺口。

- sets_up_cn：为X-IM的两种核心设计（投资者本体和标签术语向量）提供理论背书。

- evidence_pointer：Abstract P1 S4

### 5. P1 S5

- order：5

- section：Abstract

- locator：P1 S5

- move_code：THEORY_INTRO

- paraphrase_cn：将表示理论应用于设计过程，表明XBRL标签链接库可被视为'财务项目名称与其所描述概念之间关系的规律性'的存储库，这些概念对应投资者感兴趣的一组等价财务术语。

- rhetorical_function_cn：摘要层提前给出理论到设计的核心翻译：标签链接库=名义规律库。

- depends_on_cn：S4提及表示理论。

- sets_up_cn：为后文详细描述IOnto和IBC的向量分类机制提供概念先导。

- evidence_pointer：Abstract P1 S5

### 6. P1 S6-S7

- order：6

- section：Abstract

- locator：P1 S6-S7

- move_code：RESULT

- paraphrase_cn：实例化的设计制品被用标准信息检索指标彻底评估；实验显示X-IM显著优于现有方法。

- rhetorical_function_cn：摘要中以结果收束，给出性能声明。

- depends_on_cn：S4-S5介绍制品设计。

- sets_up_cn：吸引读者进入正文前先知道结论有利于引导阅读预期。

- evidence_pointer：Abstract P1 S6-S7

### 7. P1 S1-S3

- order：7

- section：Introduction

- locator：P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：2009年SEC发布互动数据规则，强制所有美国上市公司对年报、季报等使用XBRL；SEC、XBRL US和FASB开发了美国GAAP财务报告分类标准（UGT）的标签列表；公司在创建XBRL财务报告时应从UGT选取标签。

- rhetorical_function_cn：为论文提供制度背景和标准背景，使读者理解XBRL和UGT是什么及为何存在。

- depends_on_cn：无需先行信息。

- sets_up_cn：为后文说明UGT的缺陷（如扩展元素）提供事实基础。

- evidence_pointer：Introduction P1

### 8. P1 S4（引用SEC）

- order：8

- section：Introduction

- locator：P1 S4（引用SEC）

- move_code：PHENOMENON

- paraphrase_cn：SEC承认当公司需要非标准报表项时，会创建公司特定的扩展元素。

- rhetorical_function_cn：用监管机构自己的话引入扩展元素现象，增强说服力。

- depends_on_cn：P1 S1-S3说明标准列表存在。

- sets_up_cn：为后续'构造赤字'理论诊断提供官方引证。

- evidence_pointer：Introduction P1 quotation from SEC

### 9. P2 S1-S3

- order：9

- section：Introduction

- locator：P2 S1-S3

- move_code：PHENOMENON

- paraphrase_cn：Zhu和Wu（2011）用121份XBRL报表计算互操作性指标，平均两文件互操作性仅29.52%，三文件降到17.35%；低互操作性表明存在语义异构。

- rhetorical_function_cn：用定量证据证明问题规模，使'语义异构'从概念变成可测量的现实。

- depends_on_cn：P1介绍XBRL标准。

- sets_up_cn：为将问题定义为'语义异构'提供数据基础。

- evidence_pointer：Introduction P2

### 10. P2 S4-S5

- order：10

- section：Introduction

- locator：P2 S4-S5

- move_code：PRACTICAL_STAKES

- paraphrase_cn：CFO杂志报道国会致信SEC，SEC没有使用自己收集的XBRL数据而依赖商业数据库；2017年评论中公司指出标准问题太多不足以为进一步监管提供依据；74%报表含扩展标签且标注易错，下游消费者不依赖该标准。

- rhetorical_function_cn：将低互操作性从技术问题提升到政策与商业后果问题，强调问题的重要性。

- depends_on_cn：P2 S1-S3的量化证据。

- sets_up_cn：为论文'现实意义'主张提供证据，也为讨论部分'授权存亡'论述铺垫。

- evidence_pointer：Introduction P2 quotations and statistics

### 11. P2 S6

- order：11

- section：Introduction

- locator：P2 S6

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：语义异构的存在排除了XBRL申报的自动消费，尤其当需要按一组财务概念和度量比较公司绩效时。

- rhetorical_function_cn：明确点题：为什么需要解决语义异构——因为自动化跨公司比较无法完成。

- depends_on_cn：P2 S1-S5的问题证据。

- sets_up_cn：为提出研究目标提供直接条件。

- evidence_pointer：Introduction P2 S6

### 12. P3 S1-S3

- order：12

- section：Introduction

- locator：P3 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：已有研究用本体映射方法，ontology化XBRL表示财报概念语义；一些工作提供映射算法将XBRL连接到上层本体。

- rhetorical_function_cn：综述已有解决方向，显示作者知晓该领域进展。

- depends_on_cn：P2提出问题背景。

- sets_up_cn：为后文指出这些方法的不足做铺垫。

- evidence_pointer：Introduction P3 S1-S3

### 13. P3 S4-S5

- order：13

- section：Introduction

- locator：P3 S4-S5

- move_code：LIMITATION

- paraphrase_cn：这些方法因为只将单个文件翻译为描述逻辑而保留异构标签且无映射策略；即使有映射算法性能也不理想；这些设计缺乏明确理论洞察且不对应于语义互操作的一般化知识。

- rhetorical_function_cn：指出现有方案的两大缺陷：精度不足和理论缺失。

- depends_on_cn：P3 S1-S3介绍已有工作。

- sets_up_cn：为论文的研究问题提供双面缺口，尤其是理论缺口。

- evidence_pointer：Introduction P3 S4-S5

### 14. P3 S6

- order：14

- section：Introduction

- locator：P3 S6

- move_code：RQ_OR_OBJECTIVE

- paraphrase_cn：因此研究问题：如何设计全自动算法，将XBRL标签准确映射到上层本体中定义的财务概念？

- rhetorical_function_cn：在缺口之后直接提出研究问题，形成'问题—缺口—RQ'的经典循环。

- depends_on_cn：P3 S4-S5缺口。

- sets_up_cn：为后续设计目标提供锚点。

- evidence_pointer：Introduction P3 S6

### 15. P3 S7-S10

- order：15

- section：Introduction

- locator：P3 S7-S10

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者提出基于索引的分类器，用理论驱动特征空间分类；ontologize XBRL并将财务概念抽象到上层本体；展示表示理论至少部分解释为什么US XBRL不互操作；声称扩展表示理论到语义互操作空间。

- rhetorical_function_cn：在摘要和正文之间先行给出答案轮廓和理论贡献声明。

- depends_on_cn：P3 S6的RQ。

- sets_up_cn：为后续理论章节和框架设计提供预览。

- evidence_pointer：Introduction P3 S7-S10

### 16. P4 S1-S4

- order：16

- section：Introduction

- locator：P4 S1-S4

- move_code：STUDY_OVERVIEW

- paraphrase_cn：作者遵循DSRM，概述问题识别、目标、设计、展示和评价、沟通的流程；目标是设计精确自动的技术解决语义异构；制品是一种新颖的等价关系分类方案；评价用标准分类指标并采用实验、观察和性能测试哲学。

- rhetorical_function_cn：在引言结尾预告研究方法论和论文结构。

- depends_on_cn：P3的RQ和初步贡献。

- sets_up_cn：为读者提供整体框架，使后文各部分有预期。

- evidence_pointer：Introduction P4

### 17. P1 S1-S4

- order：17

- section：2 The XBRL Framework

- locator：P1 S1-S4

- move_code：CONTEXT

- paraphrase_cn：描述XBRL框架由分类法和实例文档组成，分类法包含XML schema和链接库；五种链接库（计算、定义、呈现、引用、标签）各有功能，标签链接库将人类可读文本与XBRL元素关联。

- rhetorical_function_cn：建立XBRL技术词汇表，为后文'使用标签链接库'的设计决策提供领域基础。

- depends_on_cn：Introduction已提及XBRL。

- sets_up_cn：为理论章节中'标签术语可作语义指示器'提供机制性支撑。

- evidence_pointer：Section 2 P1; Table 1

### 18. P1 S1-S3

- order：18

- section：3.1 Semantic Interoperability

- locator：P1 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：语义互操作主要关注发现不同来源数据点之间的等价关系；对跨多个自主异构数据源的查询至关重要；XBRL互操作是语义互操作的特例。

- rhetorical_function_cn：将XBRL问题嵌入更广的语义互操作研究传统。

- depends_on_cn：Section 2的XBRL背景。

- sets_up_cn：为文献分类和后续理论引入提供学术坐标。

- evidence_pointer：Section 3.1 P1

### 19. P2 S1-S4

- order：19

- section：3.1 Semantic Interoperability

- locator：P2 S1-S4

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：语义互操作文献分为数据模型发展和半/全自动语义数据集成两类；数据模型发展不解决映射问题，例如UGT是数据模型但使用它的报表不自动互操作。

- rhetorical_function_cn：建立二分框架，为将论文定位到'自动数据集成'一侧提供依据。

- depends_on_cn：P1的语义互操作定义。

- sets_up_cn：为下段详细讨论自动集成方法提供分类。

- evidence_pointer：Section 3.1 P2

### 20. P3 S1-S6

- order：20

- section：3.1 Semantic Interoperability

- locator：P3 S1-S6

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：半/全自动数据集成文献按输出和过程分类；输出可为逻辑关系、变换函数或块；过程可分为原子模式、复合模式、路径、树、无结构五类。

- rhetorical_function_cn：展示作者对复杂本体匹配文献的掌握，并将XBRL映射置于其中。

- depends_on_cn：P2的分类。

- sets_up_cn：为后文对比'我们的方法不同于通用方案'提供参照。

- evidence_pointer：Section 3.1 P3

### 21. P4 S1-S4

- order：21

- section：3.1 Semantic Interoperability

- locator：P4 S1-S4

- move_code：LIMITATION

- paraphrase_cn：先前自动数据集成方案没有解决XBRL特有的问题：它们是通用的、不针对标准创建脚本不互操作的情境；一个标准的存在重新界定了语义互操作问题；现有方案也不贡献一般理论。

- rhetorical_function_cn：通过三个'不'（不针对标准、不利用标准、不贡献理论）将论文从通用语义集成分支中区分。

- depends_on_cn：P3文献分类。

- sets_up_cn：为引入表示理论并声明四项命题铺路。

- evidence_pointer：Section 3.1 P4

### 22. P4 S5-S7

- order：22

- section：3.1 Semantic Interoperability

- locator：P4 S5-S7

- move_code：THEORY_PROPOSITION

- paraphrase_cn：作者提出表示理论与语义互操作之间的新颖连接，提出四个命题（其中两个显式检验）：语法的四种本体缺陷之一将导致脚本不可互操作；该理论公式足够一般化可适用于XBRL之外。

- rhetorical_function_cn：在文献限制后提出理论主张，为本文的设计贡献建立理论支点。

- depends_on_cn：P4 S1-S4的文献限制。

- sets_up_cn：为理论章节和对UGT的诊断设下框架。

- evidence_pointer：Section 3.1 P4 S5-S7

### 23. P1 S1-S3

- order：23

- section：3.2 XBRL Interoperability

- locator：P1 S1-S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：作者用ISDT框架（Gregor & Jones, 2007）组织现有XBRL互操作设计科学文献，按目的与范围、构念、形式与功能原则、正当性知识、实现原则五个维度。

- rhetorical_function_cn：用设计理论框架来系统化综述，为论文自身的DSR定位提供学科语法。

- depends_on_cn：Section 2的XBRL技术介绍。

- sets_up_cn：建立评价现有工作（包括自动性和正当性知识）的标准。

- evidence_pointer：Section 3.2 P1; Table 2

### 24. P2 S1-S5

- order：24

- section：3.2 XBRL Interoperability

- locator：P2 S1-S5

- move_code：LIMITATION

- paraphrase_cn：在实现原则上，现状是缺乏多种全自动方法；现有全自动方法包括Etudo and Yoon（2015）、Etudo et al.（2017）和Yaghoobirafi and Nazemi（2019），后者不能同时映射多个实例文档且基于IFRS；因此全自动多文档XBRL互操作领域有显著改进空间。

- rhetorical_function_cn：针对自动性缺口进行专利性论证。

- depends_on_cn：Table 2的文献盘点。

- sets_up_cn：为论文声称其全自动属性提供参照。

- evidence_pointer：Section 3.2 P2; Table 2

### 25. P2 S6-S7

- order：25

- section：3.2 XBRL Interoperability

- locator：P2 S6-S7

- move_code：GAP

- paraphrase_cn：最先进方法（Etudo & Yoon, 2015; Etudo et al., 2017）使用计算链接库进行启发式和机器学习，但没有考虑面向人类呈现和消费的自然语言标签信息，遗留了大量未利用信息；精度和召回率也有很大改进空间。

- rhetorical_function_cn：指出最先进方法的缺陷（未用标签信息、精度和召回率不足），定义论文的直接切入点。

- depends_on_cn：Table 2和P2 S1-S5的自动性讨论。

- sets_up_cn：为介绍X-IM的设计选择（标签链接库+投资者本体）做铺垫。

- evidence_pointer：Section 3.2 P2 S6-S7; Table 2

### 26. P1 S1-S3

- order：26

- section：4 Theoretical Background

- locator：P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：作者同意文献将XBRL互操作缺乏定性为语义互操作问题；分布式系统需按协议和语法交换数据；共享理解是语义互操作的前提。

- rhetorical_function_cn：将语义互操作的定义与XBRL案例绑定。

- depends_on_cn：Section 2和Section 3.1。

- sets_up_cn：为引入表示理论作为理解意义创建的理论框架做铺垫。

- evidence_pointer：Section 4 P1

### 27. P2 S1-S2

- order：27

- section：4 Theoretical Background

- locator：P2 S1-S2

- move_code：GAP

- paraphrase_cn：语义集成文献没有提供分布式系统中意义创建的通用框架；作者认为本体清晰度理论（表示理论的表示模型）可以提供结构化理解。

- rhetorical_function_cn：指出理论缺口，并宣布候选理论。

- depends_on_cn：P1关于语义互操作需要共享理解。

- sets_up_cn：为理论应用段落提供过渡。

- evidence_pointer：Section 4 P2

### 28. P3 S1-S4

- order：28

- section：4 Theoretical Background

- locator：P3 S1-S4

- move_code：THEORY_INTRO

- paraphrase_cn：表示理论认为信息系统是对真实世界现象的表征；Wand和Weber提出三个模型（表示、状态跟踪、良好分解）；本文聚焦表示模型（本体清晰度）。

- rhetorical_function_cn：正式引入理论谱系，说明选择的子理论及其来源。

- depends_on_cn：P2缺口的提出。

- sets_up_cn：为定义四项本体缺陷提供概念容器。

- evidence_pointer：Section 4 P3

### 29. P3 S5

- order：29

- section：4 Theoretical Background

- locator：P3 S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：核心论点：就数据标准（尤其美国XBRL实施）而言，本体上清晰的信息系统会产生语义上可互操作的脚本。

- rhetorical_function_cn：将抽象理论压缩为可直接应用的可检验命题。

- depends_on_cn：P3 S1-S4理论介绍。

- sets_up_cn：为后续UGT四处缺陷分析设定目标。

- evidence_pointer：Section 4 P3 S5

### 30. P4 S1-S5

- order：30

- section：4 Theoretical Background

- locator：P4 S1-S5

- move_code：THEORY_PROPOSITION

- paraphrase_cn：本体清晰度理论关注脚本符号；语法可能犯四种缺陷：构造赤字、构造过剩、构造冗余、构造过载；任何缺陷都会使生成的脚本不可互操作，纠正缺陷会提高互操作性。

- rhetorical_function_cn：给出四项缺陷定义和因果主张，形成论文的理论引擎。

- depends_on_cn：P3理论介绍。

- sets_up_cn：为对UGT进行缺陷评估提供框架。

- evidence_pointer：Section 4 P4; Figure 1

### 31. P1 S1-S3

- order：31

- section：4.1 Construct Deficit

- locator：P1 S1-S3

- move_code：MECHANISM

- paraphrase_cn：UGT的构造赤字是刻意的，为了支持公司特定扩展；扩展元素使用比例上升，且扩展比例高会降低可比性。

- rhetorical_function_cn：用数据和文献说明构造赤字确实存在且有影响。

- depends_on_cn：P4四项缺陷框架。

- sets_up_cn：为提出'投资者本体'作为补缺手段提供必要性论证。

- evidence_pointer：Section 4.1 P1

### 32. P2 S1-S2

- order：32

- section：4.1 Construct Deficit

- locator：P2 S1-S2

- move_code：REQUIREMENT

- paraphrase_cn：作者明确定义投资者本体，封装下游消费者重要的财务概念；投资者本体直接应对UGT内置的构造赤字。

- rhetorical_function_cn：从缺陷诊断转向设计要求：构造赤字→投资者本体。

- depends_on_cn：P1说明构造赤字的存在。

- sets_up_cn：为假设H1a-c和框架设计埋下伏笔。

- evidence_pointer：Section 4.1 P2

### 33. P1 S1-S4

- order：33

- section：4.2 Construct Redundancy

- locator：P1 S1-S4

- move_code：MECHANISM

- paraphrase_cn：UGT在客观上不大可能有构造冗余，但在编制者解释中主观显示构造冗余：同一财务概念可被映射到多个XBRL元素；UGT的规模使编制者面临多选一；图2展示ProfitLoss和NetIncomeLoss均可表示净利润。

- rhetorical_function_cn：解释构造冗余在本案例中如何产生——不是语法自身冗余，而是解释的选择性冗余。

- depends_on_cn：P4理论框架。

- sets_up_cn：为论证标签信息是解决此类冗余的信号提供逻辑基础。

- evidence_pointer：Section 4.2 P1; Figure 2

### 34. P1 S5-S7

- order：34

- section：4.2 Construct Redundancy

- locator：P1 S5-S7

- move_code：MECHANISM

- paraphrase_cn：编制者依靠标签信息（人类可读文本）判断XBRL元素是否适合财务概念；不同公司可能使用不同标签术语，但这些术语在词汇上应该接近；因此标签信息是XBRL元素含义的有用指示器，词汇接近是可以传达共享含义的强大载体。

- rhetorical_function_cn：在构造冗余和标签信息利用之间建立因果-指示关系，为设计的'标签向量'部分提供理论合理化。

- depends_on_cn：P1 S1-S4的冗余定义。

- sets_up_cn：为后文IBC的词汇相似度方法提供理论依据。

- evidence_pointer：Section 4.2 P1 S5-S7

### 35. P2-P3 S1-S5

- order：35

- section：4.2 Construct Redundancy

- locator：P2-P3 S1-S5

- move_code：OTHER

- paraphrase_cn：作者讨论Allen和March（2006）对表示理论基于Bunge本体而不适用于概念世界的批评，并给出三点反驳：概念模型本来就是简化；理论经受实证检验则仍有用；批评未提供替代框架。

- rhetorical_function_cn：预判并回应理论合法性质疑，保护论文的理论基础不被釜底抽薪。

- depends_on_cn：Section 4已引入表示理论。

- sets_up_cn：为后文声称'用表示理论作为设计依据'提供防御性合法性。

- evidence_pointer：Section 4.2 P2-P3

### 36. P4 S1-S2

- order：36

- section：4.2 Construct Redundancy

- locator：P4 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：作者声称从表示理论到XBRL案例生成两组可推广的设计原则：关于构造冗余（元数据可被自动代理用来检测语义等价）和构造赤字（可自动生成本体/分类法来渐进补充缺陷语法）。

- rhetorical_function_cn：将具体诊断上升为一般设计原则，为论文的'可复用设计知识'声明做准备。

- depends_on_cn：P3对批评的回应、P1对冗余/赤字的分析。

- sets_up_cn：为讨论部分'理论贡献'和'设计知识'提供材料。

- evidence_pointer：Section 4.2 P4

### 37. P1 S1-S6

- order：37

- section：4.3 Hypotheses

- locator：P1 S1-S6

- move_code：REQUIREMENT

- paraphrase_cn：X-IM用投资者本体和XBRL标签术语分别应对构造赤字和构造冗余；索引本体由爬虫提取的XBRL元素、标签术语和设计性信息组成；X-IM可以被视为投资者本体与索引本体之间的本体对齐框架。

- rhetorical_function_cn：将理论诊断转化为X-IM的具体设计目标，并预告框架的高级视图。

- depends_on_cn：Section 4.1和4.2的需求输出。

- sets_up_cn：为假设的提出提供设计语境。

- evidence_pointer：Section 4.3 P1

### 38. H1a-H2c

- order：38

- section：4.3 Hypotheses

- locator：H1a-H2c

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：H1a-c：有投资者本体的X-IM在精确率、召回率、F值上优于无投资者本体的X-IM；H2a-c：使用标签信息的X-IM在精确率、召回率、F值上优于无标签信息的方法。

- rhetorical_function_cn：以可检验命题形式固化理论到设计的翻译，为实验提供可操作目标。

- depends_on_cn：P1所述设计特征。

- sets_up_cn：为实验2和实验3提供假设靶子。

- evidence_pointer：Section 4.3 H1a-c; H2a-c

### 39. P1 S1-S6

- order：39

- section：5.1 System Architecture

- locator：P1 S1-S6

- move_code：DESIGN_FEATURE

- paraphrase_cn：X-IM由EDGAR爬虫、IOnto生成器、IBC学习器组成，分别负责提取、生成索引本体、进行基于索引的分类映射。

- rhetorical_function_cn：给出系统高层结构，将理论需求具体化为组件。

- depends_on_cn：Section 4.3的设计概述。

- sets_up_cn：为后续各组件的详细描述搭建框架。

- evidence_pointer：Section 5.1; Figure 3

### 40. P1 S1-P3 S1

- order：40

- section：5.2 The EDGAR Web Crawler

- locator：P1 S1-P3 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：爬虫自动从EDGAR交互式财务报表中提取XBRL元素、标签术语和设计性信息；使用10-K因为其比10-Q包含更丰富的元素；通过浏览器自动化工具定位公司文件。

- rhetorical_function_cn：说明制品的数据获取机制和选择10-K的理由。

- depends_on_cn：Section 5.1架构。

- sets_up_cn：为IOnto生成器提供输入特征。

- evidence_pointer：Section 5.2; Figure 4-9

### 41. P4 S1-S2

- order：41

- section：5.2 The EDGAR Web Crawler

- locator：P4 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：作者强调利用标签链接库将人类可读文本与XBRL元素相连（@xlink:label）；标签术语在EDGAR交互式报表中被解析；设计性信息（balance type和period type）创建离散类别，帮助X-IM注释和解释元素。

- rhetorical_function_cn：将理论所强调的'标签信息'落实到实际数据机制，并引入辅助特征（设计性信息）。

- depends_on_cn：Section 2标签链接库介绍和4.2标签信息论证。

- sets_up_cn：为IOnto本体的属性设计（hasLabelTerm、hasBalanceType、hasPeriodType）提供来源。

- evidence_pointer：Section 5.2 P4; Figure 8-9

### 42. P1 S1-S3

- order：42

- section：5.3 The IOnto Generator

- locator：P1 S1-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：IOnto生成器整合元素、标签术语和设计性信息；XBRL元素被表示为类，标签术语是类的个体属性，形成引用关系；索引本体方法有先例（Doan et al., 2002; Kaza & Chen, 2008）。

- rhetorical_function_cn：给出IOnto概念定义和文献先例，使设计在语义互操作传统中有根。

- depends_on_cn：Section 5.2提取结果。

- sets_up_cn：为IBC学习器的分类功能提供数据结构。

- evidence_pointer：Section 5.3 P1; Figure 10-11

### 43. P2 S1-S4

- order：43

- section：5.3 The IOnto Generator

- locator：P2 S1-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：IOnto的两个好处：避免频繁访问复杂XBRL本体，提高效率；提供可移植性，能在其他XBRL本体映射环境中重用。

- rhetorical_function_cn：对制品设计的经济性和可移植性进行论证，回应'设计是通用的而非一次性'的DSR要求。

- depends_on_cn：P1的IOnto结构。

- sets_up_cn：为讨论部分'可移植到其他本体映射环境'的主张提供依据。

- evidence_pointer：Section 5.3 P2

### 44. P1 S1-P2 S1

- order：44

- section：5.4 The IBC Learner

- locator：P1 S1-P2 S1

- move_code：DESIGN_FEATURE

- paraphrase_cn：IBC学习器用投资者本体和IOnto完成分类映射；投资者本体用Kieso等（2013）提炼的等价术语；其核心是基于索引的分类器，对每个XBRL元素与其标签术语向量计算与投资者术语的语义相似度。

- rhetorical_function_cn：将理论处理（构造冗余的标签信号）落实为具体算法流程，并说明投资者术语来源。

- depends_on_cn：Section 4.3设计概述和5.3 IOnto结构。

- sets_up_cn：为下段批判逐对映射和提出向量化方法做准备。

- evidence_pointer：Section 5.4 P1-P2; Figure 12-13

### 45. P2 S2-S4

- order：45

- section：5.4 The IBC Learner

- locator：P2 S2-S4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：作者指出现有逐对映射的局限（如ProfitLoss与Net Income的词典相似度低），转向向量级相似度计算以克服该局限。

- rhetorical_function_cn：提供向量化方法相对于逐对映射的明确优势，使IBC设计不是任意选择而是有针对性的改进。

- depends_on_cn：P2对逐对法的批判。

- sets_up_cn：为公式(1)-(3)介绍相似度计算铺路。

- evidence_pointer：Section 5.4 P2

### 46. P4 S1-S2

- order：46

- section：5.4 The IBC Learner

- locator：P4 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：相似度需超过阈值才接受映射；阈值影响精确率和召回率，需通过实验确定。

- rhetorical_function_cn：引入阈值参数并承认其调节作用，为实验1埋伏笔。

- depends_on_cn：公式(1)-(3)相似度定义。

- sets_up_cn：为实验1阈值敏感性分析提供理由。

- evidence_pointer：Section 5.4 P4; Figure 15

### 47. P5 S1-S2

- order：47

- section：5.4 The IBC Learner

- locator：P5 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：IBC通过设计性信息过滤假候选，将XBRL元素按其对应投资者术语分组并排除设计性信息不匹配的候选。

- rhetorical_function_cn：说明辅助信息如何提升映射精确率，完善制品设计逻辑。

- depends_on_cn：P2分类概念和P3-4相似度方法。

- sets_up_cn：为评价中高性能精确率提供解释性设计来源。

- evidence_pointer：Section 5.4 P5; Figure 14 method FilterFalseCandidates

### 48. P6 S1

- order：48

- section：5.4 The IBC Learner

- locator：P6 S1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：IBC用S&P 100中少量公司的年报训练，并用多年来更多公司的报表严格测试。

- rhetorical_function_cn：预告训练/测试设计，建立评价阶段的期待。

- depends_on_cn：前述IBC算法描述。

- sets_up_cn：为第五节末到第六节评价部分的转折做准备。

- evidence_pointer：Section 5.4 P6

### 49. P1 S1-S3

- order：49

- section：6.1 Evaluation Method and Frame of Reference

- locator：P1 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用Yu等（2009）正式本体评价方法，因为该方法已被用于评估先前的XBRL互操作制品（Etudo et al., 2017），也适用于基于本体的应用。

- rhetorical_function_cn：通过方法一致性保证与先前研究可比性。

- depends_on_cn：Section 3.2对FinCEM的综述。

- sets_up_cn：为介绍精确率、召回率、F值指标提供方法论框架。

- evidence_pointer：Section 6.1 P1

### 50. P2 S1-S3

- order：50

- section：6.1 Evaluation Method and Frame of Reference

- locator：P2 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用精确率度量检索相关性，用召回率度量检索完整性，F值为二者调和平均；评价框架构造了目标本体和导出本体之间的关系。

- rhetorical_function_cn：明确定义评价指标并建立指标体系。

- depends_on_cn：P1方法论选择。

- sets_up_cn：为后续表格中的P/R/F值提供统一度量。

- evidence_pointer：Section 6.1 P2; Formula

### 51. P3 S1-S3

- order：51

- section：6.1 Evaluation Method and Frame of Reference

- locator：P3 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：研究使用S&P 100中92家公司的2011和2012年10-K报告；S&P 100覆盖多行业，引入多样性。

- rhetorical_function_cn：描述样本来源和覆盖范围，建立外部效度证据。

- depends_on_cn：P2指标定义。

- sets_up_cn：为实验1-4提供数据基础。

- evidence_pointer：Section 6.1 P3

### 52. P4 S1-S3

- order：52

- section：6.1 Evaluation Method and Frame of Reference

- locator：P4 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：先前工作用三个财务指标（盈利、杠杆/流动、营运效率）依赖FinCEM的9个概念；本文扩展为18个广泛使用的财务概念。

- rhetorical_function_cn：通过扩展基准概念集，提示本文覆盖范围比FinCEM更广，增强评价的代表性。

- depends_on_cn：P3样本和指标。

- sets_up_cn：为表3列出18个概念和实验假设检验提供目标集。

- evidence_pointer：Section 6.1 P4; Table 3

### 53. P1 S1-S3

- order：53

- section：6.2 Experiment 1: Sensitivity Analysis of Threshold

- locator：P1 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：阈值过小会降低精确率，过大降低召回率；因此实验前先做阈值敏感性分析。

- rhetorical_function_cn：解释为何需要阈值灵敏度分析，防止读者认为阈值是任意设定的。

- depends_on_cn：Section 5.4阈值的引入。

- sets_up_cn：为实验结果'阈值1.2最优'提供依据。

- evidence_pointer：Section 6.2 P1

### 54. P2 S1-S2

- order：54

- section：6.2 Experiment 1: Sensitivity Analysis of Threshold

- locator：P2 S1-S2

- move_code：RESULT

- paraphrase_cn：不同阈值导致显著不同的精确率/召回率组合；图16显示阈值1.2产生最高F值，故选为实现阈值。

- rhetorical_function_cn：报告参数选择结果，用图表展示选择逻辑。

- depends_on_cn：P1阈值权衡论证。

- sets_up_cn：确保后续实验在固定且合理的参数下进行。

- evidence_pointer：Section 6.2 P2; Figure 16

### 55. P1 S1-S3

- order：55

- section：6.3 Experiment 2: Effect of Investor’s Ontology

- locator：P1 S1-S3

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：使用Wilcoxon符号秩检验，因为它是非参数检验，适用于小样本且不能假设正态分布的情况。

- rhetorical_function_cn：解释统计方法选择的正当性。

- depends_on_cn：实验设计（18个概念配对）。

- sets_up_cn：为表4-5的p值解释提供基础。

- evidence_pointer：Section 6.3 P1

### 56. P2 S1-S2

- order：56

- section：6.3 Experiment 2: Effect of Investor’s Ontology

- locator：P2 S1-S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：实验干预是有无投资者本体；两个X-IM实例用10家随机公司2011年10-K训练，用全部92家公司2012年10-K比较。

- rhetorical_function_cn：报告消融实验的具体操作，明确训练/测试分离和干预变量。

- depends_on_cn：P1统计方法。

- sets_up_cn：为表4-5结果提供情境。

- evidence_pointer：Section 6.3 P2

### 57. P3 S1-S3

- order：57

- section：6.3 Experiment 2: Effect of Investor’s Ontology

- locator：P3 S1-S3

- move_code：RESULT

- paraphrase_cn：加入投资者本体使精确率从0.962升至0.998但不显著（Z=1.604, p=0.109），H1a不支持；召回率和F值显著提高（Z=2.934, p=0.003），H1b和H1c支持。

- rhetorical_function_cn：报告消融实验的主要发现，并区分支持与不支持的结果，体现证据纪律。

- depends_on_cn：P2实验设置。

- sets_up_cn：为讨论部分解释精确率天花板效应做铺垫。

- evidence_pointer：Section 6.3 P3; Table 4-5

### 58. P1 S1-S3

- order：58

- section：6.4 Experiment 3: Comparative Performance Analyses

- locator：P1 S1-S3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：与最先进方法FinCEM比较；训练数据限定为2011年10家公司，测试用82家公司2011年和92家公司2012年，以验证跨年份泛化。

- rhetorical_function_cn：描述比较实验设定，强调小训练集和跨年份测试。

- depends_on_cn：Section 3.2中FinCEM综述。

- sets_up_cn：为表6-8比较结果提供上下文。

- evidence_pointer：Section 6.4 P1

### 59. P2 S1-S2

- order：59

- section：6.4 Experiment 3: Comparative Performance Analyses

- locator：P2 S1-S2

- move_code：RESULT

- paraphrase_cn：X-IM在2011和2012年的总体精确率、召回率、F值上均优于FinCEM；精确率达到99%。

- rhetorical_function_cn：报告总体比较结果，突出高精确率优势。

- depends_on_cn：P1实验设定。

- sets_up_cn：为p值显著性检验提供描述性前提。

- evidence_pointer：Section 6.4 P2; Table 6

### 60. P3 S1-S2

- order：60

- section：6.4 Experiment 3: Comparative Performance Analyses

- locator：P3 S1-S2

- move_code：RESULT

- paraphrase_cn：Wilcoxon检验显示：精确率差异显著（p=0.012），支持H2a；召回率差异不显著（p=0.108），H2b不支持；F值差异显著（p=0.044），支持H2c。

- rhetorical_function_cn：用统计检验收束比较实验结果，区分支持与不支持假设。

- depends_on_cn：P2描述统计。

- sets_up_cn：为讨论中'标签信号更判别力'的解释提供由头。

- evidence_pointer：Section 6.4 P3; Table 7-8

### 61. P1 S1-P2 S1

- order：61

- section：6.5 Experiment 4: Effect of Training Data Sizes

- locator：P1 S1-P2 S1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：为回应训练集大小对性能的影响，用2011年标签链接库构建10、20、40家公司的三个训练语料，2012年用于测试。

- rhetorical_function_cn：说明为何做训练规模实验以及操作方式。

- depends_on_cn：实验3使用10家公司训练。

- sets_up_cn：为表9结果提供设计。

- evidence_pointer：Section 6.5 P1

### 62. P2 S2

- order：62

- section：6.5 Experiment 4: Effect of Training Data Sizes

- locator：P2 S2

- move_code：RESULT

- paraphrase_cn：训练集从10家扩到40家，平均F值从0.923升至0.928，仅增0.542%，而计算时间从117.9s增至178.9s（增51.74%）；10家训练高效有效。

- rhetorical_function_cn：给出小训练集合理性的证据，回应实际部署成本。

- depends_on_cn：P1实验设置和表9数据。

- sets_up_cn：为讨论中'开源可行'主张提供支持。

- evidence_pointer：Section 6.5 P2; Table 9

### 63. P1 S1-S3

- order：63

- section：7 Conclusion and Discussion

- locator：P1 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：本文对实现真正XBRL互操作做出贡献；XBRL申报有术语歧义，互操作问题阻碍业务报告管道自动化，下游消费者仍没有开源跨公司比较方案。

- rhetorical_function_cn：回扣引言中的现实问题，并将贡献放在解决实际问题上。

- depends_on_cn：Introduction P2的现实问题。

- sets_up_cn：为理论贡献和现实意义段落做引。

- evidence_pointer：Section 7 P1

### 64. P2 S1-S3

- order：64

- section：7 Conclusion and Discussion

- locator：P2 S1-S3

- move_code：CONTRIBUTION

- paraphrase_cn：理论贡献：提供一个体现表示理论表示模型的IT制品，证明减少构造赤字和构造冗余可提高标准生成实例的互操作性；提出标签链接库中丰富语义信息可提供等价映射，并可作为减少两种缺陷的核验理论之一。

- rhetorical_function_cn：将实验结果上升为理论主张，回应引言中'不贡献理论'的缺口。

- depends_on_cn：实验2和实验3的结果。

- sets_up_cn：为边界条件和未来研究方向提供铺垫。

- evidence_pointer：Section 7 P2

### 65. P3 S1-S4

- order：65

- section：7 Conclusion and Discussion

- locator：P3 S1-S4

- move_code：PRACTICAL_STAKES

- paraphrase_cn：SEC强制令在实践中的存续需要下游价值证据；X-IM的开源性质有望降低结构化财务数据的获取成本，民主化数据访问。

- rhetorical_function_cn：将技术贡献嵌入制度-政治背景，强调社会意义。

- depends_on_cn：P1-P2贡献。

- sets_up_cn：为未来研究和开放性声明提供动机。

- evidence_pointer：Section 7 P3

### 66. P4 S1-P5 S2

- order：66

- section：7 Conclusion and Discussion

- locator：P4 S1-P5 S2

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：局限：某些财务概念在报表中不出现，需计算推理；未来可增加推理能力、主题分析、多级学习器等。

- rhetorical_function_cn：诚实声明局限性并指出迭代方向，防止读者认为方法万能。

- depends_on_cn：全部实验结果。

- sets_up_cn：引导后续研究进入系统增强方向。

- evidence_pointer：Section 7 P4-P5

### 67. P6 S1-S2

- order：67

- section：7 Conclusion and Discussion

- locator：P6 S1-S2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：方法可推广至其他语义集成领域，但依赖'同一概念存在足够并行名义信息'这一核心条件。

- rhetorical_function_cn：设定边界条件，保护一般化主张不被无限夸大。

- depends_on_cn：IOnto和IBC设计如何依赖标签术语。

- sets_up_cn：收束论文，使读者记住适用条件。

- evidence_pointer：Section 7 P6

### 68. Table A1

- order：68

- section：Appendix A

- locator：Table A1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：给出投资者本体中18个财务概念的等价投资者术语及其设计性信息，来源为Kieso等（2013）教材。

- rhetorical_function_cn：提供投资者本体的实质性内容，使设计透明可复现。

- depends_on_cn：Section 5.4对投资者本体的引用。

- sets_up_cn：为读者验证实验概念和结果提供数据附录。

- evidence_pointer：Appendix A Table A1

### 69. Table B1

- order：69

- section：Appendix B

- locator：Table B1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：用一个具体例子（净利润概念、两个XBRL元素及其标签术语向量）展示Jaccard相似度和调整后平均相似度计算过程。

- rhetorical_function_cn：通过小示例使公式(1)-(3)可人工验证，增强方法透明度。

- depends_on_cn：Section 5.4公式。

- sets_up_cn：支持正文中向量化相似度的表述。

- evidence_pointer：Appendix B Table B1

## 写作技术

- gap_construction_cn：论文用'三层渐进'方式构造缺口：第一层，用制度和量化事实（SEC引用、Interoperability 29.52%、CFO文章、EY评论）构建现实问题；第二层，在语义集成和XBRL互操作文献中区分现有方案的不足（精度不足、缺乏理论、不针对标准、不贡献一般知识）；第三层，在理论层面指出语义集成文献没有提供意义创建的通用框架，从而引入表示理论。这使得最终贡献同时覆盖技术改进、理论延伸和通用设计知识。

- signposting_cn：引言末尾明确列出DSRM流程；文献综述末尾预告X-IM要利用标签术语和设计性特征；4.3节在假设前先给出高级框架图（Figure 2；实际为标签术语示例）；5.1节在系统细节前给出架构图；6.1节在实验前解释评价框架和与FinCEM的关系。每一节都以'预告—展开—回顾'的方式衔接。

- transition_logic_cn：从现实问题到理论诊断的过渡：先证明低互操作是语义异构，再指出语义集成文献缺通用意义创建框架，进而用表示理论解释；从理论诊断到设计需求的过渡：用'构造赤字→投资者本体'和'构造冗余→标签术语'两条显式命题；从设计到评价的过渡：5.4末预告训练测试设计，6.1开头申明评价方法一致性；从评价结果到理论返回的过渡：7.2第一段把实验2/3的统计显著性改写为'减少构造赤字和构造冗余会提高互操作性'的理论命题。

- claim_evidence_rhythm_cn：每个重要主张都配以表格和统计检验：理论命题（缺陷导致不可互操作）→用数据和实践者报告支撑；设计需求→映射为具体组件；性能优势→先用描述性统计（Table 6）再用Wilcoxon检验（Table 8）；消融实验支持设计组件贡献（Table 4-5）。节奏是'主张—操作化—证据—限定'，尤其在H1和H2的接受/拒绝处理上非常透明。

- benchmark_narrative_cn：benchmark（FinCEM）不是简单对比对象，而是被嵌入连续叙事：文献综述中将其作为最先进的自动方法代表；评价方法中说明沿用其评价框架和9个概念；比较实验中使用其训练哲学（10家公司）并扩展概念集；结果汇报中同时给出总体性和逐概念表现；讨论中把与FinCEM的差异归因于设计特征（标签信息+设计性信息）。这使benchmark成为论文自己的理论设计叙事的一部分。

- theory_return_cn：实验结果返回理论的路径是：实验2证明'投资者本体（构造赤字补充）'提高召回率和F值；实验3证明'标签信息（构造冗余信号）'提高精确率和F值；讨论段落将这些具体差异合并为一般命题'纠正语法缺陷→脚本更互操作'，并称其为表示理论的一个实例。作者还从理论批评的回应中提取两条可复用设计原则（元数据可检测语义等价；自动生成本体可补充缺陷语法），将案例知识升格为设计知识。

- contribution_positioning_cn：贡献被放置在三个层面：技术贡献（算法更准）、理论贡献（扩展表示理论到语义互操作）、社会/政策贡献（开源、民主化数据获取、XBRL授权存续）。论文特意将理论贡献与技术贡献并置，避免被认为是纯技术报告。

- novelty_protection_cn：通过三重保护防止贡献退化为一次性性能结果：（1）理论锚定——将性能改进归因于表示理论可解释的构造缺陷修正；（2）设计知识开发——提出一般化设计原则和适用条件（并行名义信息）；（3）跨问题域外推——声称方法可适用于其他语义集成领域。即使技术改进本身有限，理论框架和一般化条件也构成独立贡献。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：以制度/数据/政策引证确立现实问题的必要性和严重性；定量/定性证据并举说明问题造成后果。

- research_job_cn：找到可量化且影响广泛的领域问题（如XBRL低互操作性）。

- required_evidence_cn：权威数据点（如互操作性百分比、政策文件引用、行业评论）。

- transition_to_next_cn：将现实问题重新描述为文献可处理的研究问题（语义异构）。

#### 2. 2

- step：2

- writing_job_cn：综述相关文献并建立既有方案的能力边界；明确既有方案的两类缺口：性能缺口和理论缺口。

- research_job_cn：识别基线方法（如FinCEM）和评价框架。

- required_evidence_cn：文献分类表、基线方法细节、评价指标来源。

- transition_to_next_cn：因'性能不足且无理论'，引入候选理论作为设计依据。

#### 3. 3

- step：3

- writing_job_cn：介绍理论，将理论构念（构造赤字、构造冗余）与具体标准/案例进行诊断性对照；必要时回应理论批评。

- research_job_cn：论证所选理论确实适用于案例，并确定哪些理论缺陷存在于案例中。

- required_evidence_cn：案例证据或实践者文献支持缺陷诊断；对理论批评的回应。

- transition_to_next_cn：从缺陷诊断直接导出设计要求：'构造缺陷X→设计组件Y'。

#### 4. 4

- step：4

- writing_job_cn：将设计需求转化为具体算法/系统组件，逐组件写出输入、输出、处理逻辑和公式；给出架构图。

- research_job_cn：实现可运行的制品，并准备可复现的数据抽取和算法细节。

- required_evidence_cn：系统架构图、伪代码、公式、示例。

- transition_to_next_cn：说明制品需要调参（如阈值）和正式评价，引入实验。

#### 5. 5

- step：5

- writing_job_cn：先处理参数敏感性（若有），再针对设计的理论组件做消融实验，最后与已识别的最先进基线做比较；用统计检验和表格汇报。

- research_job_cn：设计训练/测试集分离、对比条件、评价指标；运行实验；做统计显著性检验。

- required_evidence_cn：训练/测试描述、Wilcoxon符号秩检验结果、跨年份或跨样本外验证。

- transition_to_next_cn：在讨论中把各组实验结果的'显著/不显著'综合为对假设的整体判断，再上升为理论主张。

#### 6. 6

- step：6

- writing_job_cn：讨论部分回扣缺口：技术表现如何优于基线；理论命题如何被支持；哪些组成部分获得支持（F值）而哪些未获支持（如精确率不显著）；给出一般化条件和局限。

- research_job_cn：反思假设未获支持的可能解释；提炼可复用设计知识；指出未来工作。

- required_evidence_cn：对每项假设的接受/拒绝状态；对异常结果的事后解释；边界条件声明。

- transition_to_next_cn：以'可迁移条件'和'未来方向'收束全文。

### most_transferable_moves_cn

1. 三层缺口构造：现实—文献—理论，使技术改进同时具备现实必要性和理论意义

2. 理论到设计的显式翻译：用'缺陷→设计要求→组件→假设→消融/比较'的链条展示设计不是试错

3. 从逐条统计结果到整体理论命题的上升：不回避不显著假设，将其解释为天花板或判别力问题

4. 用基准（FinCEM）和评价框架的一致性保证可比性，同时扩展概念集以显示超越

5. 在结尾设置边界条件（并行名义信息）来保护一般化主张

### resource_intensive_or_nonstandard_parts_cn

1. 依赖SEC EDGAR和指定年份的XBRL 10-K文件，需要访问公开数据和构建网络爬虫，但数据获取成本对一般研究者相对可控

2. 需要人工构建投资者本体（基于Kieso等教材），并非完全零成本

3. 需要与既有系统（FinCEM）进行对比，这要求复现或获取基线实现

4. Wilcoxon检验和大量人工编码的相似度计算虽不昂贵，但跨年份和多概念测试需要中等规模计算资源

5. 一般化主张的长期验证（例如在IFRS或其他司法管辖区测试）需要额外数据源和领域知识

### what_not_to_copy_superficially_cn

1. 仅复制'标签术语向量+Jaccard相似度'而不说明标签链接库与标准缺陷（构造冗余）的关系，会沦为技术堆砌

2. 仅声明'表示理论指导设计'而无消融实验/比较实验证明对应设计组件贡献，理论将被视为事后包装

3. 仅报告总体P/R/F值而不报告逐概念细节和统计检验，无法支撑'显著优于现有方法'的结论

4. 仅做单一年份测试而不做跨年份和训练规模实验，泛化性主张将缺乏证据

5. 无边界条件（如并行名义信息）地宣称可适用于任意语义集成场景，会陷入过度主张

- single_best_description_of_the_routine_cn：先用理论和量化证据把领域问题诊断为标准语法缺陷，然后让每个设计选择直接对应一个缺陷，并用消融和与最先进方法的比较实验同时验证组件的独立贡献和系统的整体优势，最后把统计结果沿'缺陷—组件—性能—理论'的链条上升为可复用的设计知识。

## 分析边界

论文全文为PDF文本转换，图片（Figure 1-16）和部分屏幕截图未完整显示内容，但相关文字说明足以支撑分析。个别公式数字表达有OCR损坏（如????????????），不影响核心逻辑判断。表格（Table 2等）内容较完整。未纳入附录中未展示的其他材料。对论文中'图2'与文本引用位置有轻微不一致（正文4.2和4.3两处描述同一图例），不影响结构判断。
