# 严格筛选后的直接编程研究

共 28 篇：包含人类实际编程任务 21 篇；直接分析代码制品或编程技术、但没有人类编程任务 7 篇。

## 一、包含人类实际编程任务（21篇）

### 1. [Performance Outcomes of Test-Driven Development: An Experimental Investigation](../../../database_fulltext_all/13262_2020_performance-outcomes-of-test-driven-development-an-experimental-investigation.md)

- 年份：2020；期刊：Journal of the Association for Information Systems；作者：Vikram Bhadauria; RadhaKanta Mahapatra; Sridhar Nerur；DOI：10.17705/1jais.00628
- 原研究层级：individual；直接焦点类型：programming_method_process；人类编程任务：True

**直接编程研究概要：** 本文通过严格控制的实验室实验，直接比较了测试驱动开发（TDD）与传统test-last方法对软件质量和开发者任务满意度的影响。84名学生被随机分到两组，分别完成相同的编程任务。结果发现，TDD组在代码质量（通过详细评分标准评估，p<0.01）和任务满意度（p<0.01）上均显著优于test-last组，且未增加额外时间成本，证明TDD作为一种编程方法能提升代码产出和开发者体验。

**保留理由：** 替换测试无法通过：若将“程序员/开发者”替换为一般知识工作者，将“代码/软件质量”替换为一般工作产出，则TDD特有的测试驱动、代码重构循环将失去具体编程情境，软件质量评估标准（如类设计、接口、语法正确性）和实验任务（编写Java程序）均无法替换。文章的核心研究问题、实验处理（TDD vs test-last）、测量（代码评分、编程任务满意度）及结论均紧密围绕实际编程活动和方法过程，编程是不可替代的研究对象。

### 2. [The Effects of Information Request Language and Template Usage on Query Formulation](../../../database_fulltext_all/08748_2016_the-effects-of-information-request-language-and-template-usage-on-query-formulation.md)

- 年份：2016；期刊：Journal of the Association for Information Systems；作者：Leo Vijayasarathy; Gretchen Casterella；DOI：10.17705/1jais.00440
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 研究以认知负荷理论为基础，通过2×2×2重复测量实验检验请求语言（伪SQL vs. 经理英语）和查询模板使用对SQL查询编写表现的影响。结果发现，伪SQL请求在低复杂度查询中提高准确率，但对高复杂度查询无益；模板使用在高复杂度查询中提高准确率、减少尝试次数并增强信心，但在低复杂度查询中起反作用。

**保留理由：** 替换测试：若将“编写SQL查询”替换为一般知识工作（如撰写报告），则伪SQL/经理英语的信息请求操纵、基于SQL语法的Halstead难度测量、模板内容等核心处理均无法成立，研究问题和结论失去基础。文章直接观察、操纵和解释特定的编程操作（SQL代码编写、调试、语法修正），主要因变量为查询准确率、时间、尝试次数等编程表现，因此属于直接编程研究。

### 3. [Exploring the Impact of Soclo-Technlcal Core-Periphery Structures in Open Source Software Development](../../../database_fulltext_all/06398_2010_exploring-the-impact-of-soclo-technlcal-core-periphery-structures-in-open-source-software-develo.md)

- 年份：2010；期刊：Journal of Information Technology；作者：Chintan Amrit; Jos van Hillegersberg；DOI：10.1057/jit.2010.7
- 原研究层级：project；直接焦点类型：code_artifact_analysis；人类编程任务：True

**直接编程研究概要：** 本文提出一种通过分析软件调用图聚类确定核心-边缘结构，并计算平均核心-边缘距离度量（CPDM）的方法，以评估开源项目的健康状况。研究发现稳定的核心-边缘移动趋势（如无远离核心的移动）与项目健康相关，而远离核心或振荡移动可能指示衰退。

**保留理由：** 替换测试：若将“程序员”替换为一般知识工作者，“代码/软件项目”替换为一般工作任务或产出，则本研究的核心变量（基于代码依赖的核心-边缘距离度量）和机制（代码模块依赖关系及修改）将完全失去意义。文章直接分析源代码的内部结构（调用图、类间依赖）和具体的编程活动（开发者修改哪些文件），其结论解释的是编程行为与软件结构的关系，而非一般团队协作或项目绩效。核心证据来自代码制品分析和开发者编程记录，属于不可替代的编程研究对象。

### 4. [Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries](../../../database_fulltext_all/09878_2010_is-query-reuse-potentially-harmful-anchoring-and-adjustment-in-adapting-existing-database-querie.md)

- 年份：2010；期刊：Information Systems Research；作者：Gove Allen; Jeffrey Parsons；DOI：10.1287/isre.1080.0189
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 研究通过实验让157名新手查询编写者在熟悉和不熟悉的领域中，部分提供可复用的SQL查询样本，部分无样本，完成信息请求的查询编写。发现复用样本导致查询准确性更低、编写时间更短、过度自信更高（置信度与实际正确性关联更弱），并且锚定调整偏见在深层结构锚（如连接条件）比表面结构锚（如属性值）更严重。域熟悉度影响不同类型的调整能力。

**保留理由：** 本文以SQL查询编写为核心研究对象，直接观察和测量参与者编写SQL查询的过程和结果（准确性、时间、置信度）。替换测试：若将‘程序员/开发者’替换为一般知识工作者，将‘SQL查询’替换为一般工作任务，研究问题、变量和结论将不再成立，因为锚定调整效应是基于特定编程工件（SQL查询）的文本和结构特征。因此这是不可替代的编程研究。

### 5. [An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity](../../../database_fulltext_all/15408_2009_an-empirical-investigation-of-end-user-query-development-the-effects-of-improved-model-expressiv.md)

- 年份：2009；期刊：Information Systems Research；作者：Paul L. Bowen; Robert A. O'Farrell; Fiona H. Rohde；DOI：10.1287/isre.1080.0181
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 研究对比了精简型与通过本体清晰度增强表达性的较大逻辑数据模型对终端用户编写SQL查询的准确性（语义错误）、时间和信心的影响。发现当模型增大后，更表达性的模型导致更多语义错误、更长时间和更低信心，因为协调复杂性（更多表、更多连接）的增加超过了组件复杂性降低的收益。

**保留理由：** 替换测试：若将SQL查询编写替换为一般知识工作者的文档写作任务，并将数据模型替换为文档模板，则研究的核心机制（如FROM/JOIN错误、组件与协调复杂性的权衡）将不成立，因为这些机制直接依赖于编程语言的结构和数据库查询的特定认知操作。该研究直接观察和测量人类编写代码（SQL）的过程和产物（查询准确性），编程活动是研究对象不可替代的核心。

### 6. [Are Two Heads Better than One for Software Development? The Productivity Paradox of Pair Programming1](../../../database_fulltext_all/05946_2009_are-two-heads-better-than-one-for-software-development-the-productivity-paradox-of-pair-programm.md)

- 年份：2009；期刊：MIS Quarterly；作者：VenuGopal Balijepally; RadhaKanta Mahapatra; Sridhar Nerur; Kenneth H. Price；DOI：10.2307/20650280
- 原研究层级：dyadic；直接焦点类型：programming_method_process；人类编程任务：True

**直接编程研究概要：** 通过控制实验比较结对编程与个体编程在软件质量、满意度和信心上的差异。参与者实际编写和修改 Java 代码，代码质量由评估量规客观评分。发现结对编程的软件质量高于名义配对中的第二优成员，但未超过最优成员；结对编程的满意度和信心更高。

**保留理由：** 替换测试：若将程序员替换为一般知识工作者，编程任务替换为一般问题解决任务，则群体与个体绩效比较的结论虽可能仍成立，但本研究直接操纵和测量实际的代码编写活动与代码质量，且理论框架基于编程任务的智力性与可论证性特征。编程本身是不可替代的核心研究对象，故判 true。

### 7. [The Role of Visualization Tools in Spreadsheet Error Correction from a Cognitive Fit Perspective](../../../database_fulltext_all/16148_2008_the-role-of-visualization-tools-in-spreadsheet-error-correction-from-a-cognitive-fit-perspective.md)

- 年份：2008；期刊：Journal of the Association for Information Systems；作者：Suparna Goswami; Hock Chan; Hee Kim；DOI：10.17705/1jais.00162
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 研究通过实验室实验，以认知拟合理论为基础，考察了可视化工具（箭头显示单元格引用关系）对电子表格公式纠错性能的影响。结果表明，当工具支持追踪单元格关系的任务（链接错误）时，能显著提高纠错速度；但对不依赖关系追踪的非链接错误，工具没有促进作用，甚至可能干扰。

**保留理由：** 文章核心研究电子表格公式纠错这一具体的终端用户编程活动，参与者实际阅读、追踪和修改公式，并测量其编程任务表现（纠错时间、自信心）。若将程序员替换为一般知识工作者，将公式纠错替换为一般文本查错，则公式引用追踪、链接与非链接错误的区别、箭头可视化工具的作用机制将完全失效，因此编程活动不可替换，符合直接编程研究标准。

### 8. [Developing maintainable software: The Readable approach](../../../database_fulltext_all/10622_2006_developing-maintainable-software-the-readable-approach.md)

- 年份：2006；期刊：Decision Support Systems；作者：Cecil Eng Huang Chua; Sandeep Purao; Veda C. Storey；DOI：10.1016/j.dss.2005.04.002
- 原研究层级：individual；直接焦点类型：programming_method_process；人类编程任务：True

**直接编程研究概要：** 本文提出一种名为Readable的方法，将程序组件、控制流和数据关系表示为表格，以增强程序理解。通过实验室实验比较使用Readable扩展的Java程序和传统Java程序的理解效果，发现Readable显著提高了对控制流的理解，且未对其他编程理解构念产生负面影响。

**保留理由：** 替换测试：如果将“程序员/开发者”替换为一般知识工作者，将“代码/软件项目”替换为一般工作任务，则研究问题（理解代码中的控制流）和机制（表格表示对程序理解的影响）将不复存在，核心处理、测量和结论会完全破坏。文章直接研究编程表示方法对程序理解的影响，编程是不可替代的核心对象。

### 9. [Selecting optimal instantiations of data models—Theory and validation of an ex ante approach](../../../database_fulltext_all/02594_2006_selecting-optimal-instantiations-of-data-modelstheory-and-validation-of-an-ex-ante-approach.md)

- 年份：2006；期刊：Decision Support Systems；作者：P.L. Bowen; R. Debreceny; F.H. Rohde; J. Basford；DOI：10.1016/j.dss.2005.10.002
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 本文提出并验证了一种前评估方法，通过计算各数据模型实例化下代表性查询的 Halstead 平均复杂度，预测哪种数据表示能使最终用户编写更准确的 SQL 查询。实验发现，对象-关系型实例化（OOR）的平均查询复杂度显著低于关系型实例化（3NF），参与者在 OOR 下编写的 SQL 查询语义错误显著更少，从而验证了复杂度预测的理论。

**保留理由：** 本研究以最终用户编写 SQL 查询作为核心且不可替代的研究对象，直接观测和分析查询编写过程及其代码复杂度、准确性、效率和信心等具体编程表现。研究问题、关键变量（查询复杂度、语义错误）和结论均紧密依赖于编程特有的查询语言和软件复杂度度量，若将“程序员”替换为一般知识工作者、将“SQL 查询”替换为一般工作任务，整个研究机制将不复成立。因此，该文属于直接以编程活动为研究焦点的文献。

### 10. [The Effects of State-Based and Event-Based Data Representation on User Performance in Query Formulation Tasks1,2](../../../database_fulltext_all/01578_2006_the-effects-of-state-based-and-event-based-data-representation-on-user-performance-in-query-form.md)

- 年份：2006；期刊：MIS Quarterly；作者：Gove N. Allen; Salvatore T. March；DOI：10.2307/25148731
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 文章直接研究状态基础与事件基础的数据表示对用户编写 SQL 查询时的准确性、信心和准确性预测的影响。实验发现事件基础视图使低熟悉度的用户能更好地预测查询准确性，且事件相关表示减少了查询编写时间。

**保留理由：** 替换测试：将“程序员”替换为一般知识工作者，将“SQL查询编写”替换为一般工作任务后，研究问题、处理、测量和结论将完全崩溃，因为研究核心是不同数据模型对具体编程任务（查询编写）表现的影响。文章直接观察和测量 SQL 查询的语义正确性、编写者信心等，编程对象不可替代。

### 11. [The Role of Cognitive Fit in the Relationship Between Software Comprehension and Modification1](../../../database_fulltext_all/00546_2006_the-role-of-cognitive-fit-in-the-relationship-between-software-comprehension-and-modification1.md)

- 年份：2006；期刊：MIS Quarterly；作者：Teresa M. Shaft; Iris Vessey；DOI：10.2307/25148716
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 本文研究软件维护中理解与修改的交互关系。通过实验让24名IT专业人员先研究COBOL程序，再进行功能修改或控制流修改，测量理解变化和修改表现。结果发现认知适应（心理表征与任务类型的匹配）调节二者关系：当程序员的领域模型或程序模型与修改任务类型（功能或控制流）匹配时，理解提升与修改表现正相关；不匹配时则呈负相关，揭示了编程中的双重任务干扰效应。

**保留理由：** 文章以源代码理解和修改为核心研究对象，主要变量（程序理解变化、修改任务类型、心理表征等）均与编程操作直接相关，理论机制依赖于编程领域特有的知识表征（领域模型与程序模型）。若将“程序员”替换为一般知识工作者、“代码”替换为一般文档，核心处理和结论不再成立，故符合直接编程研究标准。

### 12. [The effects of information request ambiguity and construct incongruence on query development](../../../database_fulltext_all/20989_2001_the-effects-of-information-request-ambiguity-and-construct-incongruence-on-query-development.md)

- 年份：2001；期刊：Decision Support Systems；作者：A.Faye Borthick; Paul L. Bowen; Donald R. Jones; Michael Hung Kam Tse；DOI：10.1016/s0167-9236(01)00097-5
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 该研究通过受控实验直接考察信息请求模糊性和构造不一致性对最终用户编写SQL查询的准确性、效率和信心的影响。结果发现模糊性降低准确性和效率，不一致性降低准确性、效率和信心。研究提出了查询开发过程的认知模型，并基于错误分析提供了改进查询界面和培训的建议。

**保留理由：** 替换测试：将“编写SQL查询”替换为一般知识工作任务后，研究问题（请求歧义、结构一致性与任务绩效的关系）的核心机制将不再成立，因为所分析的变量（SQL语法、数据表示、视图、外连接、Halstead复杂度等）和任务完全特定于编程。文章直接测量查询代码制品（微观/宏观错误）、开发行为和认知过程，主要结论解释编程行为本身，而非一般态度或组织结果。因此判定为直接编程研究。

### 13. [Using a structured design approach to reduce risks in end user spreadsheet development](../../../database_fulltext_all/22602_2000_using-a-structured-design-approach-to-reduce-risks-in-end-user-spreadsheet-development.md)

- 年份：2000；期刊：Information & Management；作者：Diane Janvrin; Joline Morrison；DOI：10.1016/s0378-7206(99)00029-4
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 文章通过两个现场实验考察结构化设计方法（基于数据流图）对终端用户电子表格开发错误和开发时间的影响。实验任务要求受试者完成一个包含多个工作表、大量链接的电子表格开发，研究直接分析受试者编写的电子表格中的链接错误、概念错误和疏忽错误。结果显示，采用结构化设计方法的受试者链接错误显著减少，但对概念错误、疏忽错误和开发时间无显著影响；性别、领域专长和应用专长也影响错误率和开发信心。

**保留理由：** 该文以终端用户电子表格开发为研究对象，核心问题是结构化设计方法对电子表格错误的影响。替换测试：若将“电子表格开发”替换为一般文档写作或计算任务，则链接错误、结构化设计方法等特有概念将失去意义，研究问题和结论无法成立。文章直接观察、操纵和分析了具体的编程操作（编写公式、创建链接）和代码制品属性（错误类型与数量），其主要结论解释的是设计方法对编程行为结果的影响，因此属于直接编程研究。

### 14. [Applying Code Inspection to Spreadsheet Testing](../../../database_fulltext_all/25049_1999_applying-code-inspection-to-spreadsheet-testing.md)

- 年份：1999；期刊：Journal of Management Information Systems；作者：Raymond R. Panko；DOI：10.1080/07421222.1999.11518250
- 原研究层级：mixed；直接焦点类型：programming_method_process；人类编程任务：True

**直接编程研究概要：** 本研究将代码审查方法应用于电子表格测试，发现个体检查平均发现63%的错误，小组审查提升至83%，但小组阶段并未发现新错误，仅汇集了个体阶段的发现。遗漏错误和长公式中的机械错误更难检测，且个体普遍存在过度自信。

**保留理由：** 替换测试：若将“程序员/开发者”替换为一般知识工作者，将“代码/软件项目”替换为一般工作任务或文档，则电子表格公式检查中的特定编程活动（如单元格引用、公式逻辑、机械错误）将消失，研究问题不再成立。文章的核心直接观察和分析了具体的编程任务（电子表格公式的审查和纠错），且主要结论针对编程方法在测试中的效果，具有不可替代性。

### 15. [Hitting the wall: errors in developing and code inspecting a `simple' spreadsheet model](../../../database_fulltext_all/21491_1998_hitting-the-wall-errors-in-developing-and-code-inspecting-a-simple-spreadsheet-model.md)

- 年份：1998；期刊：Decision Support Systems；作者：Raymond R Panko; Ralph H Sprague；DOI：10.1016/s0167-9236(97)00038-9
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 该研究直接考察终端用户编程（电子表格建模）中的错误，让152名学生开发简单电子表格模型，测量单元格错误率（CER）和错误类型（机械、逻辑、遗漏），并评估个人代码检查的纠错效果。研究发现即使任务简单，仍有35%的模型存在错误，CER为2.0%；逻辑错误和遗漏错误占主导；个人代码检查仅纠正了18%的错误。结论强调电子表格编程与专业编程相似，需要严格的测试和团队审查。

**保留理由：** 替换测试：若将‘电子表格开发者’替换为一般知识工作者，将‘电子表格模型/公式/单元格’替换为一般工作任务（如撰写报告），核心变量（CER、代码检查错误检测率）将无法定义，因为CER高度依赖电子表格的单元格和公式结构。研究直接测量了具体编程操作（公式编写）和代码制品（公式正确性），结论解释编程行为（错误率、代码检查有效性）。因此，编程本身构成不可替代的核心研究对象。

### 16. [The Relevance of Application Domain Knowledge: Characterizing the Computer Program Comprehension Process](../../../database_fulltext_all/24954_1998_the-relevance-of-application-domain-knowledge-characterizing-the-computer-program-comprehension.md)

- 年份：1998；期刊：Journal of Management Information Systems；作者：Teresa M. Shaft; Iris Vessey；DOI：10.1080/07421222.1998.11518196
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 该研究直接以程序理解过程为研究对象，通过口头协议分析刻画程序员在熟悉/不熟悉应用领域下的理解策略（自顶向下、自底向上和灵活过程）。发现熟悉领域导致更多应用知识引用，但不改变编程知识引用；使用自顶向下过程时应用知识引用更多且层次更高；灵活过程组（根据领域切换过程）的理解成绩最高。研究还探讨了元认知和经验对过程选择的影响。

**保留理由：** 执行替换测试：将“程序员”替换为一般知识工作者，将“代码/COBOL程序”替换为一般文档或工作任务，研究问题、认知机制、协议分析和知识类型将完全失效。文章核心在于刻画程序员在阅读和回答源代码理解问题时的具体认知活动（假设/推断、应用领域知识引用、编程领域知识引用、细节层次），且主要结论直接解释编程理解行为与绩效。因此，编程是不可替代的核心研究对象。

### 17. [Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces](../../../database_fulltext_all/26760_1997_why-is-programming-sometimes-so-difficult-programming-as-scientific-discovery-in-multiple-proble.md)

- 年份：1997；期刊：Information Systems Research；作者：Jinwoo Kim; F. Javier Lerch；DOI：10.1287/isre.8.1.25
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 本文将编程视为在规则、实例和表示三个问题空间中的科学发现过程，通过三项实验分析程序员在编写、理解和重用代码时的认知操作与表示变化，发现表示空间的搜索及其变化是导致编程困难的核心原因。

**保留理由：** 本文的核心研究对象是编程认知过程，包括程序的生成、理解和修改。研究中观察的Derive、Infer、Mental simulation等认知操作以及表示变化均直接关联具体的编程行为和代码属性，如果将“程序员”替换为一般知识工作者、“代码”替换为一般工作任务，则理论机制、实验任务和主要发现都将失去根基。文章的主要结论解释编程行为困难的原因，而非一般性团队、组织或市场现象，因此符合直编程研究的不可替代标准。

### 18. [An experimental investigation into the process of knowledge-based systems development](../../../database_fulltext_all/23206_1996_an-experimental-investigation-into-the-process-of-knowledge-based-systems-development.md)

- 年份：1996；期刊：European Journal of Information Systems；作者：S Lee; RM O'Keefe；DOI：10.1057/ejis.1996.29
- 原研究层级：artifact_system；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 通过受控实验，操纵知识表示（规则 vs 混合）、开发方法论（快速原型 vs 结构化原型）和程序员质量，分析这些因素对编程过程（编码时间、生产率、代码变更）和代码产品质量（异常、功能性、可用性）的影响。主要发现快速原型结合规则表示在功能上最佳，但快速原型结合混合表示最差；结构化混合方案更为稳健；程序员质量提升可带来更高的编码生产率和可用性。

**保留理由：** 替换测试：若将“程序员”替换为一般知识工作者，“代码”替换为一般工作任务，研究中的编码时间、代码行数、编程异常等测量将失去意义，且核心处理（知识表示与开发方法对编程过程和代码质量的影响）无法在一般工作任务中复现。文章直接观察和测量受试者实际的编程操作（CLIPS 编码）、分析代码制品（代码行数变化、异常类型）并解释编程行为与结果，故编程是不可替代的核心研究对象。

### 19. [The Influence of Database Structure Representation on Database System Learning and Use](../../../database_fulltext_all/24810_1996_the-influence-of-database-structure-representation-on-database-system-learning-and-use.md)

- 年份：1996；期刊：Journal of Management Information Systems；作者：Robert L. Leitheiser; Salvatore T. March；DOI：10.1080/07421222.1996.11518106
- 原研究层级：individual；直接焦点类型：programming_education_task；人类编程任务：True

**直接编程研究概要：** 本研究通过实验探讨了数据库结构表示（实体语义 vs 表格语义、图形 vs 纯文本、显式 vs 隐式关系）对终端用户学习 SQL 查询语言的影响。结果发现，有助于理解数据库内容的表示（如实体的语义和显式关系）反而阻碍了 SQL 的学习，表格语义和隐式关系表示更有利于查询语言的学习和使用。

**保留理由：** 文章核心研究终端用户学习 SQL 查询编写这一编程活动。实验要求参与者实际编写 SQL 查询，并测量了查询学习的正确率和时间。如果替换为一般知识工作者的非编程任务（如一般数据检索），则研究问题和理论机制（数据库表示如何影响查询语言学习）将完全破坏，因此不可替代，属于直接编程研究。

### 20. [Research Report—The Relevance of Application Domain Knowledge: The Case of Computer Program Comprehension](../../../database_fulltext_all/26710_1995_research-reportthe-relevance-of-application-domain-knowledge-the-case-of-computer-program-compre.md)

- 年份：1995；期刊：Information Systems Research；作者：Teresa M. Shaft; Iris Vessey；DOI：10.1287/isre.6.3.286
- 原研究层级：individual；直接焦点类型：human_programming_task；人类编程任务：True

**直接编程研究概要：** 文章探讨应用领域知识对程序理解过程的影响。通过让 24 名专业程序员口头报告理解熟悉（会计）和不熟悉（水文）领域的 COBOL 程序，分析其假设（自上而下）和推论（自底向上）数量，发现熟悉领域时程序员使用更自上而下的过程，表明应用领域知识影响程序理解的认知策略。

**保留理由：** 该研究以程序理解为核心对象，分析程序员阅读代码时的认知过程。替换测试：若将程序员替换为一般知识工作者，代码替换为一般文本，则程序理解特有的认知模型（如 Brooks 的假设验证、信标、编程计划）将失效，研究问题和结论无法成立。因此编程本身是不可替代的核心。

### 21. [On end-user computing productivity](../../../database_fulltext_all/18768_1991_on-end-user-computing-productivity.md)

- 年份：1991；期刊：Information & Management；作者：Prashant Palvia；DOI：10.1016/0378-7206(91)90067-c
- 原研究层级：individual；直接焦点类型：programming_method_process；人类编程任务：True

**直接编程研究概要：** 文章通过控制实验比较了四种程序开发方法（流程图、伪代码、叙述性描述、直接编写）对最终用户程序员编写的程序质量、开发时间和生产力的影响。结果表明，程序质量普遍较低，不同方法在程序的结构和正确性上没有显著差异；直接编写程序的开发时间最短，但伪代码和直接编写方法在生产力指标上表现最佳。

**保留理由：** 文章包含一个明确的编程实验，研究最终用户采用不同开发方法（流程图、伪代码等）编写实际程序的过程与产出。该实验以程序质量（结构、正确性、整体质量）和开发时间作为核心结果变量，这些变量不可替代为一般知识工作的产出或效率。替换测试中，若将“程序员”替换为“一般知识工作者”，将“程序”替换为“一般工作产出”，则研究问题、测量和结论均不成立，因为结构、正确性、代码行数等指标直接来源于编程活动。因此，本文不可替代地以编程方法及其对编程过程和制品的影响为核心研究对象。

## 二、直接分析代码制品或编程技术（无人类实际任务）（7篇）

### 1. [Atrophy in Aging Systems: Evidence, Dynamics, and Antidote](../../../database_fulltext_all/28664_2024_atrophy-in-aging-systems-evidence-dynamics-and-antidote.md)

- 年份：2024；期刊：Information Systems Research；作者：Amrit Tiwana; Hani Safadi；DOI：10.1287/isre.2023.1218
- 原研究层级：project；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 文章直接研究编程制品的内部结构演化，提出系统萎缩概念，定义为代码基内部逻辑一致性的时间间退化。利用1900万行代码、900万依赖关系等追踪数据，通过计算每单位代码的圈复杂度变化来衡量萎缩，并发现提高模块化可减缓萎缩但随系统年龄增长而失效。同时揭示了萎缩导致进化停滞、缺陷增加、开发者注意力流失和代码库采纳减少等编程相关后果。

**保留理由：** 文章核心研究问题是软件系统代码结构的退化机制，自变量和因变量均为源代码特有的属性（模块化、圈复杂度），分析对象为代码制品本身。若将“程序员/代码”替换为一般知识工作者/工作产出，研究问题、机制、测量和结论均无法成立，因为一般工作产出缺乏可类比的结构属性和度量。因此满足不可替代测试，属于直接研究编程。文章采用代码制品分析，无人类实际编程任务。

### 2. [Performance implications of stage-wise lead user participation in software development problem solving](../../../database_fulltext_all/09798_2014_performance-implications-of-stage-wise-lead-user-participation-in-software-development-problem-s.md)

- 年份：2014；期刊：Decision Support Systems；作者：Jorge Colazo；DOI：10.1016/j.dss.2014.08.007
- 原研究层级：project；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 文章以开源软件项目为背景，从代码仓库、缺陷追踪系统和邮件列表提取数据，研究领先用户参与软件开发问题解决各阶段对源代码质量和开发生产力的影响。发现：参与缺陷检测和移除与代码质量负相关，参与分析与质量正相关；所有阶段的参与均降低开发生产力；前端加载（早期修复更多缺陷）提高代码质量但降低生产力。研究核心直接聚焦于代码制品的质量和编程生产力。

**保留理由：** 替换测试：若将“程序员/开发者”替换为一般知识工作者，将“代码/软件项目/补丁”替换为一般工作任务、项目产出或问题报告，研究中的核心变量（如基于Halstead软件科学的预期缺陷数、源代码行数增长等代码质量/生产力度量）将失去意义，研究机制无法成立。文章直接分析软件缺陷检测、分析与修复的具体活动及其对源代码质量和开发生产力的影响，编程对象不可替代。

### 3. [Role of collective ownership and coding standards in coordinating expertise in software project teams](../../../database_fulltext_all/12156_2009_role-of-collective-ownership-and-coding-standards-in-coordinating-expertise-in-software-project.md)

- 年份：2009；期刊：European Journal of Information Systems；作者：Likoebe M Maruping; Xiaojun Zhang; Viswanath Venkatesh；DOI：10.1057/ejis.2009.24
- 原研究层级：team；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 文章通过收集56个软件项目团队的问卷调查数据（集体所有权、编码标准、专业知识协调）和项目结束后的编码错误数，采用回归分析检验这些实践的主效应和调节效应。研究发现集体所有权和编码标准均与更少的编码错误显著相关，且它们分别减弱和增强了专业知识协调（如知晓专业知识所在）对编码错误的影响，揭示了编程实践如何影响代码质量。

**保留理由：** 替换测试：若将“程序员/开发者”替换为一般知识工作者，将“代码/软件项目”替换为一般工作产出，自变量“集体所有权”和“编码标准”虽可泛化，但理论论证、测量（如编码标准指代码编写格式）和核心因变量“编码错误数”均紧密绑定编程制品。若替换，研究问题、机制和结论将被根本破坏，故判为 true。文章主要证据来自代码制品属性（错误数），且未直接观察人类编程任务，因此聚焦类型为代码制品分析。

### 4. [An exploratory study of object-oriented software component size determinants and the application of regression tree forecasting models](../../../database_fulltext_all/20163_2004_an-exploratory-study-of-object-oriented-software-component-size-determinants-and-the-application.md)

- 年份：2004；期刊：Information & Management；作者：Parag C. Pendharkar；DOI：10.1016/j.im.2003.12.004
- 原研究层级：artifact_system；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 文章通过分析 152 个实际 OO 软件组件的度量数据，运用多元回归、ANOVA 和回归树（CART、CHAID），识别影响组件 SLOC 的代码属性（方法数、子类数、GUI 元素数、事件数）和组件类型。结果表明这些属性均与 SLOC 显著正相关，且应用组件规模最大；回归树模型提供了可解释的预测规则。

**保留理由：** 替换测试：如果将方法数、子类数等 OO 特有度量替换为一般任务属性，研究将无法成立，因为这些属性是编程特有的代码制品特征。文章核心是对已完成的软件组件进行代码结构的量化分析，预测其规模，而非研究人的编程行为、认知或团队管理。因此符合代码制品分析（code_artifact_analysis）的直接编程研究。

### 5. [The Moderating Effects of Structure on Volatility and Complexity in Software Enhancement](../../../database_fulltext_all/26371_2000_the-moderating-effects-of-structure-on-volatility-and-complexity-in-software-enhancement.md)

- 年份：2000；期刊：Information Systems Research；作者：Rajiv D. Banker; Sandra A. Slaughter；DOI：10.1287/isre.11.3.219.12209
- 原研究层级：project；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 本研究以软件增强中的代码制品属性为核心，考察软件结构、复杂度和波动性如何共同影响增强成本和错误。通过分析两家公司COBOL应用的代码度量数据，发现结构对复杂度和波动性的增强成本效应有调节作用：更高的结构水平对更复杂和更易变的应用更有利，能减少增强成本和错误。此外，最优结构水平随复杂度和波动性增加而提高。研究还发现应用类型（如规划管理类与事务处理类）可预测复杂度和波动性，组织激励机制能促进高效设计选择。

**保留理由：** 替换测试：若将“程序员/代码”替换为一般知识工作者/工作产出，关键变量（如数据复杂度N2/FP、结构calls/FP、增强次数/FP）将失去编程特有的含义；理论机制（如结构化设计分解、理解代码结构、定位修改影响）直接依赖于编程活动与代码制品，无法泛化为一般工作情境。因此，编程不可替代，文章核心研究编程制品属性及其对增强结果的影响。

### 6. [A software complexity model of object-oriented systems](../../../database_fulltext_all/17415_1995_a-software-complexity-model-of-object-oriented-systems.md)

- 年份：1995；期刊：Decision Support Systems；作者：David P. Tegarden; Steven D. Sheetz; David E. Monarchi；DOI：10.1016/0167-9236(93)e0045-f
- 原研究层级：artifact_system；直接焦点类型：code_artifact_analysis；人类编程任务：False

**直接编程研究概要：** 该文提出了一个面向对象软件复杂度模型，在变量、方法、对象和系统四个级别定义了复杂度度量，这些度量基于耦合和凝聚，并考虑了继承、多态等编程特有概念，旨在量化面向对象设计的复杂性，以预测开发和维护成本。

**保留理由：** 文章的核心贡献是软件复杂度模型和度量定义，这些度量直接针对编程制品（源代码、类结构等）的特性，如变量多态、方法扇入扇出、继承冲突等。替换测试：若将“程序员”换成一般知识工作者，将“代码”换成一般工作产出，这些度量将失去意义，因为它们是编程语言特有的结构。因此该文直接以编程制品为研究对象，属于直接的编程研究。

### 7. [COD — A dynamic data flow analysis system for Cobol](../../../database_fulltext_all/18351_1987_cod-a-dynamic-data-flow-analysis-system-for-cobol.md)

- 年份：1987；期刊：Information & Management；作者：T.Y. Chen; H. Kao; M.S. Luk; W.C. Ying；DOI：10.1016/0378-7206(87)90061-9
- 原研究层级：artifact_system；直接焦点类型：programming_tool_language；人类编程任务：False

**直接编程研究概要：** 文章提出了一个针对Cobol程序的动态数据流分析系统COD，阐述了通过程序插桩监测数据项动作并基于状态转换图检测数据流异常的理论与实现方法，并验证了其在软件测试和开发中的有效性。

**保留理由：** 替换测试：若将“程序员/开发者”替换为一般知识工作者，将“代码/COBOL程序”替换为一般工作任务或产出，则数据流分析、程序插桩、状态转换等核心机制完全失效。研究问题、关键处理和贡献均直接围绕编程特有的源代码分析、动态检测和程序插桩技术，因此不可替代，属于直接编程研究。
