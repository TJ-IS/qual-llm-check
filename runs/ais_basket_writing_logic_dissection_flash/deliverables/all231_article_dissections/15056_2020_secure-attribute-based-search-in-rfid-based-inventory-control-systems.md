# Secure attribute-based search in RFID-based inventory control systems

- 作者：Robin Doss; Rolando Trujillo-Rasua; Selwyn Piramuthu
- 年份 / 期刊：2020 / Decision Support Systems
- DOI：10.1016/j.dss.2020.113270
- 源文件：15056_2020_secure-attribute-based-search-in-rfid-based-inventory-control-systems.md
- 论文主类型：build_evaluate_design_science
- 主导写作弧线：requirements_build_evaluate_design_principles
- 置信度：0.8

## 文章级论证概况

- 核心问题：在资源受限的被动RFID标签和EPC标准约束下，如何设计并形式化验证一种支持按属性集合同时搜索多个标签、同时保护标签身份与库存隐私的安全搜索协议？

- 制品与设计：提出一种基于二次剩余属性的轻量级RFID属性搜索协议：标签端只需128位PRNG和模平方运算，借助服务器公钥加密标签响应，由服务器解密并校验查询；阅读器与服务器之间使用对称密钥保证完整性，标签初始化时可写入包含真实产品属性的超集以形成库存不确定性。

- 客观结果：通过Scyther工具对高规格协议P_1和P_2进行形式化验证，并归纳证明P_n满足非注入一致性（抗重放和冒充攻击）；在无消息阻断且prod-info⊆tag-info条件下证明协议完备；隐私分析证明标签匿名、不可追踪性、k-匿名和库存不确定性；与已有协议的特征对比显示只有本方案同时支持属性搜索和EPC合规。

- 核心贡献：作者声称提出了第一个安全属性搜索RFID协议，将RFID搜索从基于标识符扩展到基于任意属性列表，并在满足被动标签硬件约束的前提下实现EPC合规、Dolev-Yao安全性和标签/库存隐私。

- 整篇论证链：文章从RFID库存控制中的实际需要出发，指出现有安全搜索协议只能按标签ID搜索单标签，而库存盘点需要安全地按产品属性查找一组标签；同时被动RFID标签的硬件资源极有限，已有密码原语难以满足EPC标准。作者因此将搜索问题形式化为属性搜索协议并定义声音性和完备性，随后选择二次剩余构造轻量级公钥加密，使标签只需执行PRNG和模平方运算；协议采用阅读器发起查询、标签用服务器公钥加密响应、服务器解密并校验查询语义的两阶段结构。为证明安全性，作者将协议抽象为支持理想加密的高层规范，用Scyther验证P_1/P_2的非注入一致性，并通过归纳证明推广到任意标签数量，进而推导出抗重放、抗冒充及Dolev-Yao下的声音性；在限制消息不被打断且tag-info包含prod-info的条件下还能获得完备性。隐私分析依次证明秘密性、标签不可追踪性、k-匿名等价类以及库存不确定性，并说明通过给标签写入超集属性可在查询为合取/析取式时保持声音性、同时向攻击者虚增库存规模。最后用特征对比表证明本协议是唯一同时满足属性搜索和EPC合规的方案，并坦承不支持双向认证、强不可追踪性未达到，从而把边界条件纳入贡献。

## 类型与写作弧线判定

- 论文主类型判定：文章不是理论驱动实验，也不是基于数据集的计算制品benchmark；而是从应用要求（属性搜索、被动标签约束、EPC合规）出发构建协议制品，通过形式化验证、门数估算和特征对比完成评价，最后输出可复用的设计知识（二次剩余轻量公钥、属性超集库存隐私）。

- 主导写作弧线判定：全文主线是：明确应用与硬件要求→设计两阶段属性搜索协议→用形式化验证和特征对比评价→总结设计原则与边界。没有行为实验或现场部署，属于典型的需求-构建-评价-设计原则弧线。

## 研究开展程序

- study_or_phase_count：5

- 研究阶段总序列：文章没有传统实证Study，而是由五个承担不同论证任务的阶段累积完成：Phase 1将应用问题形式化为可验证的正确性定义；Phase 2根据正确性定义和硬件约束设计具体协议；Phase 3用Scyther形式化验证安全属性并将结论推广到任意标签数；Phase 4进行隐私分析并引入库存不确定性设计；Phase 5通过特征对比表将协议定位到现有文献并给出边界。

### studies_or_phases

#### 1. 属性搜索协议的形式化定义与正确性要求

- order：1

- name_cn：属性搜索协议的形式化定义与正确性要求

- question_cn：在RFID库存场景中，属性搜索协议应当满足怎样的功能正确性？

- inputs_and_setting_cn：无实证数据；基于概念化RFID标签属性集合和查询函数。

- designed_or_compared_object_cn：将身份搜索扩展为属性搜索协议的定义，提出声音性和完备性两个功能性质。

- baseline_control_or_counterfactual_cn：以传统基于标识符的搜索协议作为对照。

##### objective_metrics

（空）

- analysis_method_cn：形式定义与逻辑推理；证明有限制条件下声音性与完备性的关系。

- main_result_cn：给出属性搜索协议的定义；声音性要求无假阳性，完备性要求无假阴性；指出当q(prod-info)蕴含q(tag-info)且消息不被阻断时可同时保证声音与完备。

- argumentative_role_cn：确立整篇论文的制品验收标准，使后续协议设计和形式验证有精确目标。

- remaining_uncertainty_cn：尚未说明在何种敌手模型下成立，也未给出具体加密和消息结构。

- link_to_next_phase_cn：定义了正确性需求后，作者转向如何用轻量密码原语构造满足该定义的协议。

##### evidence_pointers

1. Section 3.1

2. Definition 1

3. Section 3.1末尾的完备性讨论

#### 2. 基于二次剩余的轻量属性搜索协议设计

- order：2

- name_cn：基于二次剩余的轻量属性搜索协议设计

- question_cn：如何使属性搜索协议只需约2.5K门以内的标签端实现并符合EPC标准？

- inputs_and_setting_cn：二次剩余数论性质、EPC C1G2对被动标签的计算约束、已有文献的PRNG和模平方门数估算。

- designed_or_compared_object_cn：两阶段协议：阅读器发送查询和随机数；符合属性条件的标签用服务器公钥加密响应；阅读器收集后转交服务器；服务器解密、校验并返回产品属性集合。

- baseline_control_or_counterfactual_cn：对照哈希、AES、ECC等因门数过高而无法用于被动标签或不符合EPC的方案。

##### objective_metrics

1. 标签端操作类型：仅128位PRNG和模运算

2. 实现门数估算<2500门

3. EPC标准合规性

- analysis_method_cn：基于已有硬件实现文献进行门数估算和协议组件设计。

- main_result_cn：得到完整的初始化阶段、两阶段协议消息序列、服务器侧校验规则以及密钥管理策略。

- argumentative_role_cn：该阶段交付制品本身，回答“设计是什么”以及“为什么能轻量级”。

- remaining_uncertainty_cn：协议安全性尚未经过形式验证；标签端轻量级基于文献估算而非实际流片测试。

- link_to_next_phase_cn：有了具体协议后，下一阶段将其抽象为高层规范并用Scyther证明安全性质。

##### evidence_pointers

1. Section 3.2-3.5

2. Fig. 1协议图

3. Section 3.2第三段门数估算

#### 3. 高层规范与Scyther形式化安全验证

- order：3

- name_cn：高层规范与Scyther形式化安全验证

- question_cn：在Dolev-Yao敌手模型下，协议能否满足非注入一致性、抗重放和抗冒充，并保持声音性/完备性？

- inputs_and_setting_cn：Cremers-Mauw符号安全模型、Scyther验证工具、将模指数替换为理想公钥加密的高层MSC规范、附录中的Scyther代码。

- designed_or_compared_object_cn：对P_1和P_2进行编码验证，并归纳推广到P_n。

- baseline_control_or_counterfactual_cn：非注入一致性作为安全基准；Dolev-Yao敌手可窃听、阻断、篡改和发送消息，并可能泄露长期密钥。

##### objective_metrics

1. Scyther非注入一致性claim是否通过

2. P_n归纳证明是否成立

3. 声音性定理是否成立

- analysis_method_cn：Scyther自动化验证加数学归纳法。

- main_result_cn：P_1/P_2满足非注入一致性；由单标签响应独立性推广到P_n；协议在Dolev-Yao下是声音的，且在无阻断且prod-info⊆tag-info时完备；非注入一致性意味着抗重放和抗冒充。

- argumentative_role_cn：为制品提供最强形式化安全证据，连接协议设计与论文声称的安全贡献。

- remaining_uncertainty_cn：验证基于理想加密假设，未直接证明二次剩余实际实现上的计算安全性；Scyther只编码P_1/P_2。

- link_to_next_phase_cn：安全性已证明后，下一阶段转向更细的隐私性质（标签匿名、不可追踪、库存隐私）。

##### evidence_pointers

1. Section 4.1-4.3

2. Fig. 2

3. Lemma 1, Lemma 2, Theorem 1

4. Appendix A Scyther规范

#### 4. 标签匿名、不可追踪性与库存隐私分析

- order：4

- name_cn：标签匿名、不可追踪性与库存隐私分析

- question_cn：虽然消息可证明安全，协议是否还能泄露标签身份、标签位置或库存规模信息？如何形式化并控制这种泄露？

- inputs_and_setting_cn：未受攻击的标签集合、查询响应、标签属性集合与产品属性集合。

- designed_or_compared_object_cn：将标签初始化为写入比真实产品属性更大的tag-info超集；引入库存不确定性度量。

- baseline_control_or_counterfactual_cn：以Avoine强不可追踪性为对照，表明本协议不满足该强定义；以k-匿名和库存不确定性作为替代隐私目标。

##### objective_metrics

1. 识别两消息属于同一标签的概率

2. 等价类大小

3. 库存不确定性定义值

- analysis_method_cn：形式化命题、推论、定理及概率论证。

- main_result_cn：未受损标签的ID和非随机数保持秘密；消息因含新鲜秘密nonce而不可区分；响应满足k-匿名等价类；通过设置tag-info⊇prod-info可让攻击者高估库存，同时只要查询属于Q_A，协议依然声音。

- argumentative_role_cn：把安全主张从“消息不可读”提升到“标签身份与库存数量受保护”，并给出可调的设计尺度。

- remaining_uncertainty_cn：没有实证确定匿等价类大小或库存不确定性阈值应如何选取；强不可追踪性被主动放弃。

- link_to_next_phase_cn：隐私分析和边界确定后，下一阶段用特征表与既有协议比较，定位本方案的整体贡献。

##### evidence_pointers

1. Section 4.4

2. Proposition 1, Corollary 1, Proposition 2, Definition 3, Theorem 2

#### 5. 与既有RFID安全搜索协议的特征对比和贡献定位

- order：5

- name_cn：与既有RFID安全搜索协议的特征对比和贡献定位

- question_cn：与现有协议相比，本方案在属性搜索、安全、隐私和EPC合规方面的相对位置是什么？

- inputs_and_setting_cn：Huang et al., Won et al., Tan et al., Zuo, Kulseng et al., Kim et al.等已发表协议的特征分析（主要来自文献[52]和[10]）。

- designed_or_compared_object_cn：比较的属性包括属性搜索、双向认证、标签匿名、标签不可追踪、抗重放、抗DoS/去同步、EPC合规。

- baseline_control_or_counterfactual_cn：六个已有安全搜索协议作为基线。

##### objective_metrics

1. P1属性搜索

2. P2双向认证

3. P3标签匿名

4. P4标签不可追踪

5. A1抗重放

6. A2抗DoS/去同步

7. C1 EPC合规

- analysis_method_cn：特征矩阵对比和定性论证。

- main_result_cn：只有本方案支持属性搜索且符合EPC标准；本方案满足标签匿名、抗重放、抗DoS/去同步，但双向认证未满足，不可追踪性仅为部分满足。

- argumentative_role_cn：将前面的形式化结果放到文献坐标系中，保护“首创”声明并坦诚边界。

- remaining_uncertainty_cn：特征对比是定性的，未提供通信开销、计算时间等量化实验；无实际标签硬件实现。

- link_to_next_phase_cn：对比之后自然进入结论章节，重述库存管理动机、总结贡献并列出未来权衡研究。

##### evidence_pointers

1. Section 4.5

2. Table 1

3. Section 5

## 各部分修辞架构

### abstract_moves

1. CONTRIBUTION: 声明开发安全属性搜索协议

2. DESIGN_FEATURE: 说明可同时识别共享属性值的一组物品

3. CONTRIBUTION: 宣称这是首项此类工作，可增强RFID库存应用安全与智能

4. DESIGN_FEATURE: 强调轻量、被动标签、EPC合规，并指出借助二次剩余实现

5. RESULT: 声明通过形式化验证严格证明安全隐私性质

### introduction_moves

1. CONTEXT: RFID相对条码的技术优势

2. PRIOR_KNOWLEDGE: RFID系统组件和被动标签的通信方向

3. PHENOMENON: 库存零售中单件级RFID可支持搜索与盘点

4. PRACTICAL_STAKES: 库存控制错误影响底线、导致缺货或过度库存

5. LIMITATION: 现有标签数量估计方案缺乏隐私安全，敌手可追踪标签

6. GAP: 安全搜索协议多基于ID只能搜索单个标签，无法安全按属性查询库存水平

7. WHY_GAP_MATTERS: 大型库存控制需要按产品类型查询而非定位个别标签

8. LIMITATION: 被动RFID标签硬件门数极有限，传统密码原语不可行

9. CONTRIBUTION: 提出基于二次剩余的轻量属性搜索协议并给出形式化证明

### theory_and_knowledge_moves

1. THEORY_INTRO: 介绍二次剩余数论性质及其难解性

2. THEORY_PROPOSITION: 将属性搜索协议定义为满足声音性和完备性的通信协议

3. MECHANISM: 说明二次剩余解密需要因子分解，标签端只需模平方

4. THEORY_INTRO: 引入Cremers-Mauw符号安全模型和非注入一致性

5. METHOD_JUSTIFICATION: 使用Scyther进行自动化协议验证

6. THEORY_PROPOSITION: 定义k-匿名等价类和库存不确定性

### artifact_design_moves

1. REQUIREMENT: 将正确的属性搜索解释为无假阳性且无假阴性

2. DESIGN_FEATURE: 标签端使用128位PRNG、模平方、服务器公钥加密响应

3. DESIGN_FEATURE: 阅读器向服务器转发标签响应并用共享密钥加密查询和哈希

4. DESIGN_FEATURE: 服务器解密后校验随机数、标签ID和属性查询语义

5. DESIGN_FEATURE: 初始化时可为标签写入包含真实产品信息的属性超集

6. BOUNDARY_CONDITION: 因追求轻量和可证明安全，主动放弃双向认证

### evaluation_moves

1. METHOD_JUSTIFICATION: 将实际密码运算抽象为理想公钥加密，以检测协议逻辑漏洞

2. BENCHMARK_OR_CONTRAST: 通过Scyther验证P_1/P_2并归纳推广到P_n

3. RESULT: 证明非注入一致性、声音性、完备性

4. ROBUSTNESS_OR_BOUNDARY_TEST: 讨论消息阻断对完备性的影响、强不可追踪性不满足

5. BENCHMARK_OR_CONTRAST: 用Table 1特征矩阵与六个既有协议对比

### discussion_and_contribution_moves

1. CONTRIBUTION: 重述首个属性搜索协议、轻量级、EPC合规、形式化证明安全

2. BOUNDARY_CONDITION: 明确不支持双向认证，强不可追踪性未达到，完备性依赖无阻断

3. LIMITATION_AND_FUTURE: 未来研究库存不确定性与可扩展性的实际权衡

4. CONTRIBUTION: 将结果回接到库存数据库不准确和RFID自动盘点的初始动机

## 理论/知识到设计的翻译

### 知识/理论基础

1. RFID库存控制与单件级可见性文献

2. EPC C1G2标准对被动标签的资源约束

3. 二次剩余数论性质与模平方轻量实现文献

4. 128位PRNG的低门数实现

5. Cremers-Mauw符号安全模型与Scyther验证器

6. RFID隐私文献中的不可追踪性、k-匿名和库存不确定性

- 理论—设计耦合：direct

- 耦合判定理由：设计的关键选择直接由知识基础前瞻性决定并被形式化评价直接检验：二次剩余的性质决定标签端只需模平方；EPC门数约束决定排除哈希/公钥加密/AES；Dolev-Yao模型决定用Scyther高规格验证；k-匿名和库存不确定性决定tag-info超集初始化策略。

- 理论到设计翻译链：库存盘点需要按属性查询一组标签（应用需求）→ 形式化为属性搜索协议的声音/完备定义（功能要求）→ 被动标签只能承受约2.5K门且EPC要求ITF（硬件与标准要求）→ 二次剩余提供服务器公钥加密而标签端只需模平方+PRNG（机制选择）→ 初始化和两阶段协议消息设计（制品）→ 高规格转为Scyther规范并进行安全证明（安全验证）→ tag-info⊇prod-info超集策略为库存隐私提供可量化的不确定性（隐私机制）→ 特征表证明属性搜索和EPC合规双重优势（定位）。

### mapping_table

#### 1. 1

- theory_or_knowledge_claim_cn：RFID库存控制需要识别满足某属性列表的一组标签，而不是定位单个ID标签

- mechanism_cn：查询函数作用于标签属性集合，匹配的标签集体响应

- design_requirement_cn：协议必须支持按属性集合搜索，且不产生假阳性/假阴性

- artifact_choice_cn：阅读器发送查询q，标签判断q(tag-info)后决定是否响应；服务器再校验q(prod-info)

- evaluated_contrast_cn：与只支持ID搜索的既有协议对比

- objective_result_cn：只有本方案在Table 1中满足属性搜索P1

##### evidence_pointers

1. Section 1.1

2. Section 3.1

3. Table 1

#### 2. 2

- theory_or_knowledge_claim_cn：被动RFID标签只能分配约2.5K门给安全功能，AES/ECC/哈希均不现实

- mechanism_cn：二次剩余公钥加密可把复杂解密放在服务器，标签只做模平方

- design_requirement_cn：标签端只允许128位PRNG和模平方/模运算

- artifact_choice_cn：标签用服务器公钥n加密(N_R||N_i||ID_i)，采用f(x)=x^2+kn的计算方法

- evaluated_contrast_cn：与需要数千门的哈希、AES、ECC方案对比

- objective_result_cn：标签端门数估计<2500门，且符合EPC标准

##### evidence_pointers

1. Section 1.1 Contributions

2. Section 3.2

3. Section 4.5

#### 3. 3

- theory_or_knowledge_claim_cn：Dolev-Yao敌手可窃听、阻断、篡改和发送消息，因此协议必须满足非注入一致性

- mechanism_cn：阅读器-服务器共享密钥保证转发消息完整性；服务器公钥保证标签响应机密性；一次性随机数保证新鲜性

- design_requirement_cn：在标准符号安全模型下，协议所有参与方须对消息内容达成一致

- artifact_choice_cn：两阶段协议及Scyther高层规范P_n

- evaluated_contrast_cn：Scyther验证P_1/P_2，再归纳推广到P_n

- objective_result_cn：P_n满足非注入一致性，抗重放和冒充；Dolev-Yao下声音

##### evidence_pointers

1. Section 4.1-4.3

2. Lemma 1

3. Lemma 2

4. Theorem 1

#### 4. 4

- theory_or_knowledge_claim_cn：即使消息不可读，响应本身仍会泄露标签属性满足查询这一事实

- mechanism_cn：同类响应的标签形成等价类；等价类越小匿名越弱

- design_requirement_cn：应使攻击者无法区分两个未受损标签的响应，并量化库存泄露

- artifact_choice_cn：每条响应含标签生成的新鲜nonce并用服务器公钥加密；用tag-info超集初始化

- evaluated_contrast_cn：以Avoine强不可追踪性为边界对照

- objective_result_cn：标签不可追踪概率为1/等价类大小；库存不确定性可最小化假计数

##### evidence_pointers

1. Section 4.4

2. Corollary 1

3. Proposition 2

4. Definition 3

#### 5. 5

- theory_or_knowledge_claim_cn：给标签写入比真实产品属性更大的属性集可让敌手高估库存，但同时增加通信量

- mechanism_cn：超集tag-info使更多标签响应查询；服务器通过正确的prod-info数据库排除假阳性

- design_requirement_cn：在合取/析取查询类Q_A上，超集策略不得破坏声音性

- artifact_choice_cn：初始化时令prod-info(T)⊆tag-info(T)，由库存所有者决定超集大小

- evaluated_contrast_cn：与tag-info=prod-info时零库存隐私的情况对比

- objective_result_cn：Theorem 2保证协议在Q_A上声音；库存不确定性是该策略的直接度量

##### evidence_pointers

1. Section 4.4

2. Theorem 2

3. Definition 3

## 评价逻辑

### evaluation_modes

1. 形式化协议验证：用Scyther对P_1/P_2验证非注入一致性

2. 数学归纳证明：将P_1/P_2的验证结果推广到任意标签数P_n

3. 定理证明：声音性、完备性、秘密性、不可追踪性、库存不确定性

4. 特征对比：与六个既有RFID安全搜索协议进行性质矩阵比较

5. 门数估算：基于已有硬件文献估算标签端实现成本

- why_these_evaluations_cn：本文是安全协议设计论文，核心贡献是正确性和安全性，因此评价必须以形式化验证为核心；由于Scyther无法直接验证任意数量标签，作者用归纳法弥补；因没有实际标签硬件，门数证据来自成熟文献；特征对比用于把新协议放到已有方案坐标系中，证明其不可替代性。

- benchmark_and_contrast_chain_cn：没有数值benchmark。评价链为：功能定义（声音/完备）→轻量约束（门数）→安全模型（Dolev-Yao）→形式验证（Scyther P_1/P_2+归纳）→隐私模型（k-匿名/库存不确定性）→文献特征矩阵（Table 1）。每类对照服务于一个论证层次：正确性、可实现性、安全性、隐私性、文献位置。

### claim_evidence_ledger

#### 1. 协议是声音的：在Dolev-Yao敌手下输出无假阳性

- claim_cn：协议是声音的：在Dolev-Yao敌手下输出无假阳性

- evidence_cn：Theorem 1由非注入一致性推导；Scyther验证P_1/P_2并归纳到P_n

- status_cn：有形式化证据支持，但依赖理想加密假设和二次剩余安全性

#### 2. 协议在无阻断且prod-info⊆tag-info时完备

- claim_cn：协议在无阻断且prod-info⊆tag-info时完备

- evidence_cn：Theorem 1证明：所有满足查询的标签都响应且不被服务器丢弃

- status_cn：证据局限于敌手不能阻断tag-to-reader通信，正文已明确边界

#### 3. 标签匿名和不可追踪性

- claim_cn：标签匿名和不可追踪性

- evidence_cn：Proposition 1用Scyther证明N_i和ID_i保密；Corollary 1和Proposition 2给出不可区分概率

- status_cn：有形式化支持；未满足Avoine强不可追踪性，作者以边界形式承认

#### 4. 抗重放和抗冒充

- claim_cn：抗重放和抗冒充

- evidence_cn：由非注入一致性结论推导，且随机数新鲜性通过Lemma 2覆盖任意n

- status_cn：支持较充分；但正文同时说明需要消息间有足够变化

#### 5. EPC合规且轻量

- claim_cn：EPC合规且轻量

- evidence_cn：引用文献中128位PRNG约1.5K门、模平方约几百门，合计<2.5K门

- status_cn：基于文献门数估算，没有实际硬件实现或流片测试

#### 6. 库存隐私可通过tag-info超集提高

- claim_cn：库存隐私可通过tag-info超集提高

- evidence_cn：Definition 3和Theorem 2证明超集导致敌手错误计数增加且协议保持声音

- status_cn：形式化支持，但未给出现实中应取多少超集的准则

#### 7. 首次提出属性搜索安全协议

- claim_cn：首次提出属性搜索安全协议

- evidence_cn：相关工作部分声明“没有现存的属性安全搜索协议”，Table 1显示P1仅本方案满足

- status_cn：依赖文献检索的完备性和对“属性搜索”的定义；可能存在限定范围内的首创声明

- internal_validity_strategy_cn：使用Scyther自动化工具对高规格协议进行形式化验证，并引入数学归纳法把两个标签情形推广到任意标签数；通过非注入一致性捕捉协议逻辑上的抗重放/冒充；通过命题、推论和定理逐层建立隐私结论。

- external_validity_strategy_cn：外部有效性主要靠EPC标准合规和标签端门数文献支撑，表明协议可迁移到被动RFID硬件；高规格规范保留与真实协议的消息结构映射；未来实际库存系统权衡被明确列为研究前瞻。

- what_is_not_actually_tested_cn：没有实际RFID标签或阅读器实现；没有真实库存环境部署；Scyther验证使用理想加密，未直接对抗二次剩余的具体数学攻击；标签端门数是文献估算而非实测；消息阻塞导致完备性失效的边界没有实证；双向认证缺失带来的部署影响没有实验评估。

## 贡献闭环

- technical_claim_cn：提出了首个安全属性搜索RFID协议；标签端只需128位PRNG和模平方，门数估算<2.5K；满足EPC标准；在Dolev-Yao模型下形式化证明抗重放、抗冒充、声音性/完备性条件。

- artifact_claim_cn：协议的具体设计组件——服务器公钥二次剩余加密、阅读器转发哈希、服务器三重校验（nonce、ID、q(tag-info)=q(prod-info)）——共同实现了可证明安全的属性搜索。

- mechanism_claim_cn：二次剩余使标签端加密计算极度轻量而解密由服务器完成；新随机nonce让每次响应互不可链接；tag-info超集初始化使攻击者只能获得被夸大且非精确的库存响应，服务器数据库仍是语义正确的权威来源。

- boundary_claim_cn：协议声音性在完整Dolev-Yao下成立；完备性需要消息不被阻断且prod-info⊆tag-info；不支持双向认证；不满足Avoine强不可追踪性；若服务器私钥泄露则机密性丢失。

- reusable_design_knowledge_cn：可复用原则包括：用二次剩余类轻量公钥密码把复杂解密下沉到服务器；在标签上使用超集属性初始化以控制库存隐私与通信开销的权衡；通过服务器侧语义校验（而非标签侧）保证无假阳性；在无法直接验证任意n时用Scyther验证小规模再归纳。

- theoretical_contribution_cn：将RFID搜索协议的问题空间从身份搜索扩展到属性搜索；形式化定义声音性和完备性；把标签匿名概念连接到k-匿名等价类；引入库存不确定性作为隐私度量。

- how_discussion_closes_intro_gap_cn：结论回到库存数据库不准确和人工盘点耗时等初始问题，说明本协议可同时识别阅读器范围内满足属性的一组物品；然后重申轻量、EPC合规和Dolev-Yao安全，正好回应引言中“既有协议只能ID搜索”和“被动标签资源受限”两个缺口。

- overclaim_or_unsupported_leaps_cn：“第一次/首项”声明依赖文献搜索边界；称为“rigorously proven”时依赖理想加密和Scyther不编码查询匹配逻辑；门数合规是文献估算而非实测；“EPC合规”指计算操作的可行性，不是全协议通过EPC标准认证；从P_1/P_2归纳到P_n建立在标签响应相互独立的假设上。

## 句级写作动作图谱

### 1. S1

- order：1

- section：Abstract

- locator：S1

- move_code：CONTRIBUTION

- paraphrase_cn：我们开发了一个RFID安全属性搜索协议。

- rhetorical_function_cn：开门见山声明核心交付物。

- depends_on_cn：无，独立进入。

- sets_up_cn：为全文定义主题词“属性搜索”。

- evidence_pointer：Abstract第一句

### 2. S2

- order：2

- section：Abstract

- locator：S2

- move_code：DESIGN_FEATURE

- paraphrase_cn：该协议可同时识别共享一组属性值的物品组。

- rhetorical_function_cn：解释属性搜索的独特能力，区别于单标签ID搜索。

- depends_on_cn：依赖于S1的协议声明。

- sets_up_cn：指向库存盘点中按产品类型查询的需求。

- evidence_pointer：Abstract第二句

### 3. S3

- order：3

- section：Abstract

- locator：S3

- move_code：CONTRIBUTION

- paraphrase_cn：据我们所知这是首项此类工作，可能显著增强RFID库存应用的安全与智能。

- rhetorical_function_cn：建立新颖性主张。

- depends_on_cn：需要S2的“属性搜索”概念成立。

- sets_up_cn：让读者期待文献缺口。

- evidence_pointer：Abstract第三句

### 4. S4

- order：4

- section：Abstract

- locator：S4

- move_code：DESIGN_FEATURE

- paraphrase_cn：协议轻量、适合基本被动标签、符合EPC标准，通过二次剩余零知识性质实现。

- rhetorical_function_cn：概述设计约束和核心密码原语。

- depends_on_cn：承接S3的首创声明，转入可实现性。

- sets_up_cn：引出后续的轻量实现细节。

- evidence_pointer：Abstract第四句

### 5. S5

- order：5

- section：Abstract

- locator：S5

- move_code：RESULT

- paraphrase_cn：协议的安全与隐私性质通过形式化验证严格证明。

- rhetorical_function_cn：预先给出评价方式与强度。

- depends_on_cn：S4的设计需要验证，S5给出承诺。

- sets_up_cn：为正文的Scyther验证章节做预告。

- evidence_pointer：Abstract第五句

### 6. P1 S1-S3

- order：6

- section：Introduction

- locator：P1 S1-S3

- move_code：CONTEXT

- paraphrase_cn：RFID标签利用无线电波在自动识别应用中工作，相比条码在形状、遮挡、光线和批量读取方面有优势。

- rhetorical_function_cn：建立RFID技术背景并解释其相对条码的独特价值。

- depends_on_cn：无。

- sets_up_cn：为后文说明RFID单件级库存管理潜力铺路。

- evidence_pointer：Introduction第1段

### 7. P2 S3

- order：7

- section：Introduction

- locator：P2 S3

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：昂贵的有源标签可主动发起通信，而常用的无源标签需要阅读器先通信。

- rhetorical_function_cn：给出被动标签的关键行为约束。

- depends_on_cn：P1的RFID背景。

- sets_up_cn：为协议采用EPC的Interrogator Talks First原则做知识铺垫。

- evidence_pointer：Introduction第2段

### 8. P3 S1

- order：8

- section：Introduction

- locator：P3 S1

- move_code：PHENOMENON

- paraphrase_cn：RFID与条码的关键差异在于RFID可支持单件级信息并可搜索定位感兴趣标签。

- rhetorical_function_cn：引入单件级可见性和搜索场景。

- depends_on_cn：前面RFID优势的讨论。

- sets_up_cn：为零售库存应用举例做铺垫。

- evidence_pointer：Introduction第3段

### 9. P3 零售店示例之后

- order：9

- section：Introduction

- locator：P3 零售店示例之后

- move_code：PRACTICAL_STAKES

- paraphrase_cn：多家零售商已在部分商品上部署单件级RFID标签，主要动机是库存控制和损耗管理。

- rhetorical_function_cn：用行业事实说明问题不是理论而是现实。

- depends_on_cn：P3 S1的单件级能力。

- sets_up_cn：引出下段库存控制的重要性和损耗后果。

- evidence_pointer：Introduction第3段末尾

### 10. P4 S1

- order：10

- section：Introduction

- locator：P4 S1

- move_code：PRACTICAL_STAKES

- paraphrase_cn：库存控制是零售业的重要方面，不当库存会显著影响利润。

- rhetorical_function_cn：提高应用问题严重性。

- depends_on_cn：P3的部署动机。

- sets_up_cn：为单件级可见性作为库存控制核心做铺垫。

- evidence_pointer：Introduction第4段

### 11. P5 S1

- order：11

- section：Introduction

- locator：P5 S1

- move_code：CONTEXT

- paraphrase_cn：库存控制的重要元素是单件级可见性。

- rhetorical_function_cn：从一般库存控制收紧到单件级RFID的具体机制。

- depends_on_cn：P4库存控制重要性。

- sets_up_cn：解释为什么标签数量和信息属性很重要。

- evidence_pointer：Introduction第5段开头

### 12. P5 损耗段落

- order：12

- section：Introduction

- locator：P5 损耗段落

- move_code：PRACTICAL_STAKES

- paraphrase_cn：损耗发生在进出点之间，会导致库存记录与实际不符，进而造成缺货或过度库存。

- rhetorical_function_cn：说明单件级信息缺失的实际后果，为安全标签搜索提供场景。

- depends_on_cn：P5 S1的可见性概念。

- sets_up_cn：引出搜索并核对属性值（如过期日期、过季）的需求。

- evidence_pointer：Introduction第5段

### 13. P6 S1-S3

- order：13

- section：Introduction

- locator：P6 S1-S3

- move_code：LIMITATION

- paraphrase_cn：估算标签群体规模的通信方案虽高效，但未纳入隐私安全，敌手可追踪甚至冒充标签或阅读器。

- rhetorical_function_cn：指出现有高效方案的安全缺口。

- depends_on_cn：前段单件级可见性的价值。

- sets_up_cn：为安全搜索协议的出现和后续改进提供动机。

- evidence_pointer：Introduction第6段

### 14. P1 S1

- order：14

- section：1.1 Motivation

- locator：P1 S1

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：安全搜索协议的目标是让合法阅读器安全查询一个或多个感兴趣的标签；现有协议多基于单个标签标识符。

- rhetorical_function_cn：总结安全搜索领域的现状。

- depends_on_cn：Introduction末尾提到的安全搜索协议。

- sets_up_cn：为指出“只能按ID搜索”的限制做铺垫。

- evidence_pointer：Section 1.1第1段

### 15. P1 S2

- order：15

- section：1.1 Motivation

- locator：P1 S2

- move_code：GAP

- paraphrase_cn：库存控制中往往需要安全地查询某类产品（如鞋子）的库存水平，而非定位单个标签；本工作把搜索协议扩展到这个方向。

- rhetorical_function_cn：第一次明确提出属性搜索的需求和本文目标。

- depends_on_cn：前一句对ID搜索现状的总结。

- sets_up_cn：定义“属性搜索协议”这一新问题。

- evidence_pointer：Section 1.1第1段

### 16. P2 S1

- order：16

- section：1.1 Motivation

- locator：P2 S1

- move_code：LIMITATION

- paraphrase_cn：虽有多个安全搜索协议，但都只支持基于ID的搜索。

- rhetorical_function_cn：用文献证据支持属性搜索缺口。

- depends_on_cn：P1 S2提出的属性搜索方向。

- sets_up_cn：强化“现有解释/制品不能实现”的类型。

- evidence_pointer：Section 1.1第2段

### 17. P2 S2

- order：17

- section：1.1 Motivation

- locator：P2 S2

- move_code：WHY_GAP_MATTERS

- paraphrase_cn：在大型应用中预先掌握特定标签ID并不现实，库存控制更关注不同物品的库存水平而不是定位单个标签。

- rhetorical_function_cn：解释ID搜索为何不能满足应用。

- depends_on_cn：P2 S1的现状。

- sets_up_cn：引出“按共同属性列表搜索”的需要。

- evidence_pointer：Section 1.1第2段

### 18. P2 S4

- order：18

- section：1.1 Motivation

- locator：P2 S4

- move_code：GAP

- paraphrase_cn：需要一类新的RFID协议，可以安全且私密地搜索共享属性列表的一个或多个标签；本文将这类协议称为属性搜索协议。

- rhetorical_function_cn：明确命名和定义本文要填补的空缺。

- depends_on_cn：P2 S2的实用场景。

- sets_up_cn：为后文Section 3.1的形式化定义做出概念基础。

- evidence_pointer：Section 1.1第2段

### 19. P3 S1-S3

- order：19

- section：1.1 Motivation

- locator：P3 S1-S3

- move_code：LIMITATION

- paraphrase_cn：无源RFID标签不能支持计算昂贵和存储大的安全实现；安全哈希需8K-10K门，而便宜标签只有约2.5K门可用于安全；RSA/AES/ECC都难以嵌入。

- rhetorical_function_cn：建立硬件资源这一硬约束，决定协议设计边界。

- depends_on_cn：P2的属性搜索需求。

- sets_up_cn：说明为什么需要二次剩余这一轻量原语。

- evidence_pointer：Section 1.1第3段

### 20. Contributions P1 S1

- order：20

- section：1.1 Motivation

- locator：Contributions P1 S1

- move_code：CONTRIBUTION

- paraphrase_cn：我们设计了一个适用于便宜无源RFID标签的轻量搜索协议。

- rhetorical_function_cn：转向本文贡献，回应前面所有缺口。

- depends_on_cn：前面ID搜索缺口和硬件约束。

- sets_up_cn：给出协议的总体定位。

- evidence_pointer：Section 1.1 Contributions段

### 21. Contributions P1 S2-S3

- order：21

- section：1.1 Motivation

- locator：Contributions P1 S2-S3

- move_code：DESIGN_FEATURE

- paraphrase_cn：设计利用二次剩余性质，标签端只需128位PRNG和模运算，门数小于2.5K。

- rhetorical_function_cn：把贡献具体化为可验证的技术选择。

- depends_on_cn：P3的硬件约束。

- sets_up_cn：让后文门数估算具有针对性。

- evidence_pointer：Section 1.1 Contributions段

### 22. Contributions P2 S1-S2

- order：22

- section：1.1 Motivation

- locator：Contributions P2 S1-S2

- move_code：CONTRIBUTION

- paraphrase_cn：我们提供安全形式化证明，说明协议在Dolev-Yao敌手下可正确运行；并给出初始化条件使标签隐私和库存隐私得到满足。

- rhetorical_function_cn：从功能贡献扩展到安全贡献。

- depends_on_cn：P1 S2的轻量设计。

- sets_up_cn：预告第4节的形式验证和隐私分析。

- evidence_pointer：Section 1.1 Contributions段

### 23. Contributions P3 属性列表

- order：23

- section：1.1 Motivation

- locator：Contributions P3 属性列表

- move_code：CONTRIBUTION

- paraphrase_cn：协议支持标签匿名、标签不可追踪、抗重放和抗冒充等标准安全属性。

- rhetorical_function_cn：列举将被证明的安全性质，给读者验收清单。

- depends_on_cn：P2 S1的证明承诺。

- sets_up_cn：设置后文Proposition/Theorem编号对应的具体主张。

- evidence_pointer：Section 1.1 Contributions段

### 24. Organization段

- order：24

- section：1.1 Motivation

- locator：Organization段

- move_code：STUDY_OVERVIEW

- paraphrase_cn：给出论文剩余结构：相关工作、协议、安全隐私分析、结论。

- rhetorical_function_cn：为读者装载阅读地图。

- depends_on_cn：前面贡献全部列出之后。

- sets_up_cn：让各节标题与论证职责对齐。

- evidence_pointer：Section 1.1 Organization段

### 25. P1 S1

- order：25

- section：Related work

- locator：P1 S1

- move_code：CONTEXT

- paraphrase_cn：在众多RFID标签中搜索或定位某个标签被认为是RFID系统的重要功能。

- rhetorical_function_cn：把搜索协议置于RFID功能领域。

- depends_on_cn：Introduction的属性搜索问题。

- sets_up_cn：为文献综述定义范围。

- evidence_pointer：Section 2第1段

### 26. P2 S1

- order：26

- section：Related work

- locator：P2 S1

- move_code：GAP

- paraphrase_cn：目前尚不存在现成的属性安全搜索协议。

- rhetorical_function_cn：直接声明文献缺口。

- depends_on_cn：P1对搜索功能的定位。

- sets_up_cn：让后续对已有安全搜索协议的批评都服务于本文首创主张。

- evidence_pointer：Section 2第2段开头

### 27. P2 综述

- order：27

- section：Related work

- locator：P2 综述

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：Huang和Shieh直接在密文上搜索、性能高，可检测受损阅读器，但不符EPC标准；Won等用AES和时间戳，但需要约3400门且不符EPC。

- rhetorical_function_cn：总结现有代表性搜索协议及其安全属性。

- depends_on_cn：P2 S1的属性缺口。

- sets_up_cn：为后文特征对比表中的各项打分提供基础。

- evidence_pointer：Section 2第2段

### 28. P2 噪声标签讨论

- order：28

- section：Related work

- locator：P2 噪声标签讨论

- move_code：LIMITATION

- paraphrase_cn：用噪声标签回应以保护标签匿名的方法，在ID结构化等情况下会失效。

- rhetorical_function_cn：说明已有匿名保护技巧的缺陷。

- depends_on_cn：P2对Tan等协议的讨论。

- sets_up_cn：强调同时满足隐私和EPC合规是难点。

- evidence_pointer：Section 2第2段

### 29. P3

- order：29

- section：Related work

- locator：P3

- move_code：LIMITATION

- paraphrase_cn：Kim等服务器无关方法在标签少时匿名性差；Zuo协议需要阅读器保存所有标签ID，阅读器被盗时增大了克隆风险；Kulseng等基于PUF的方案受追踪和去同步攻击。

- rhetorical_function_cn：逐个排除既有方案作为安全属性搜索基线的可能性。

- depends_on_cn：P2综述。

- sets_up_cn：强化“现有制品不能实现”的缺口。

- evidence_pointer：Section 2第3段

### 30. P4 S1-S2

- order：30

- section：Related work

- locator：P4 S1-S2

- move_code：LIMITATION

- paraphrase_cn：哈希类方案使用HMAC或布隆过滤器，资源密集；同时满足EPC标准要求和标准安全目标并非易事。

- rhetorical_function_cn：从密码原语角度说明轻量与安全很难兼得。

- depends_on_cn：P2/P3的协议类型梳理。

- sets_up_cn：引出128位PRNG和二次剩余这一替代路径。

- evidence_pointer：Section 2第4段

### 31. P4 后续

- order：31

- section：Related work

- locator：P4 后续

- move_code：PRIOR_KNOWLEDGE

- paraphrase_cn：EPC标准建议16位CRC和16位PRNG，这些容易受暴力攻击；128位PRNG方案已出现，可在廉价被动标签上实现。

- rhetorical_function_cn：介绍与本方案最接近的轻量原语状态。

- depends_on_cn：P4的EPC挑战。

- sets_up_cn：为后文选择128位PRNG作为设计组件背书。

- evidence_pointer：Section 2第4段

### 32. P5 S1

- order：32

- section：Related work

- locator：P5 S1

- move_code：CONTRIBUTION

- paraphrase_cn：与先前工作相反，本协议符合EPC标准，并解决比身份匹配更一般的标签搜索问题。

- rhetorical_function_cn：对文献综述做小结，明确区分本文。

- depends_on_cn：P2-P4的已有方案缺陷。

- sets_up_cn：进入第3节协议设计。

- evidence_pointer：Section 2第5段

### 33. P1

- order：33

- section：Section 3

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：第三节将介绍基于二次剩余、模运算和128位PRNG的协议，包括正确性定义、轻量原语、设置和运行阶段。

- rhetorical_function_cn：预告本节内部结构。

- depends_on_cn：Related work的缺口。

- sets_up_cn：让读者沿定义→密码→协议展开。

- evidence_pointer：Section 3开头

### 34. P1-P2

- order：34

- section：Section 3.1

- locator：P1-P2

- move_code：THEORY_PROPOSITION

- paraphrase_cn：将身份搜索自然扩展到属性搜索：验证者可对一群证明者执行查询，标签用属性集合刻画，并定义tag-info和prod-info。

- rhetorical_function_cn：给出属性搜索的形式化语义基础。

- depends_on_cn：前面“属性搜索协议”这一概念。

- sets_up_cn：为Definition 1提供记号。

- evidence_pointer：Section 3.1前两段

### 35. Definition 1后

- order：35

- section：Section 3.1

- locator：Definition 1后

- move_code：REQUIREMENT

- paraphrase_cn：定义声音性要求输出没有假阳性，完备性要求所有满足查询的标签都包含在输出中，即无假阴性。

- rhetorical_function_cn：把功能目标变成可验证的正式标准。

- depends_on_cn：Definition 1的定义。

- sets_up_cn：决定后文协议正确性证明的目标。

- evidence_pointer：Section 3.1 Definition 1解释段

### 36. 末段

- order：36

- section：Section 3.1

- locator：末段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：完备性是比声音性更强的性质；协议在完整Dolev-Yao敌手控制网络时只能保证声音性，完备性需要敌手不能阻断标签到阅读器的消息。

- rhetorical_function_cn：预先声明可达精确性边界，防止后续证明被误读为最强结果。

- depends_on_cn：Definition 1的声音/完备定义。

- sets_up_cn：为Theorem 1的设置直接铺垫。

- evidence_pointer：Section 3.1末段

### 37. P1

- order：37

- section：Section 3.2

- locator：P1

- move_code：THEORY_INTRO

- paraphrase_cn：介绍二次剩余的定义及其用于轻量公钥加密/解密的数论性质。

- rhetorical_function_cn：引入协议唯一的密码学知识基础。

- depends_on_cn：Section 3.1的形式化需求。

- sets_up_cn：说明为什么标签能做轻量模平方而服务器能解密。

- evidence_pointer：Section 3.2第1段

### 38. P2

- order：38

- section：Section 3.2

- locator：P2

- move_code：MECHANISM

- paraphrase_cn：当n是大素数乘积时，判断二次剩余的解需要因子分解，因而很难求出x；若把x替换为x^2则只有一个有效二次剩余。

- rhetorical_function_cn：解释二次剩余加解密的安全性来源。

- depends_on_cn：P1的QR定义。

- sets_up_cn：为协议中加密X_i=(X_i^2)^2 mod n提供数学依据。

- evidence_pointer：Section 3.2第2段

### 39. P3

- order：39

- section：Section 3.2

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：模平方在低端设备上可用x^2+kn形式的整数平方实现，使用128位寄存器和PRNG，总门数小于1000。

- rhetorical_function_cn：把数论性质落到RFID标签可实现的具体运算。

- depends_on_cn：P2的二次剩余性质。

- sets_up_cn：支撑EPC合规和轻量级声明。

- evidence_pointer：Section 3.2第3段

### 40. P1-P2

- order：40

- section：Section 3.3

- locator：P1-P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：初始化阶段为服务器、阅读器和标签分配角色、共享密钥、服务器公钥、标签秘密ID以及属性信息。

- rhetorical_function_cn：说明协议建立的信任前提和密钥材料。

- depends_on_cn：Section 3.2的密码原语。

- sets_up_cn：为两阶段协议的消息交换提供初始状态。

- evidence_pointer：Section 3.3

### 41. P1

- order：41

- section：Section 3.4

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：协议假设参与方之间的信道不安全，且网络受标准Dolev-Yao敌手控制，因此适用于固定/移动阅读器和云端服务器。

- rhetorical_function_cn：明确安全模型假设，避免把协议局限到安全信道场景。

- depends_on_cn：Section 3.3的密钥信任假设。

- sets_up_cn：为第4节安全模型设定敌手能力。

- evidence_pointer：Section 3.4第1段

### 42. P2

- order：42

- section：Section 3.4

- locator：P2

- move_code：DESIGN_FEATURE

- paraphrase_cn：遵循EPC的ITF原则，搜索查询由阅读器发起；标签和阅读器之间不共享秘密，而是采用协同认证：服务器验证阅读器后才释放标签信息。

- rhetorical_function_cn：解释协议的发起者和信任边界。

- depends_on_cn：EPC标准和P1的不安全信道假设。

- sets_up_cn：说明为什么标签消息必须加密给服务器而非阅读器。

- evidence_pointer：Section 3.4第2段

### 43. P3

- order：43

- section：Section 3.4

- locator：P3

- move_code：DESIGN_FEATURE

- paraphrase_cn：第一阶段阅读器发送nonce和查询；匹配的标签用服务器公钥加密nonce+新nonce+ID并回复；阅读器收集后连同查询、自己的nonce和响应哈希用与服务器共享密钥加密后发给服务器。

- rhetorical_function_cn：描述协议核心消息流，为后文形式化编码提供内容。

- depends_on_cn：P2的ITF和协同认证。

- sets_up_cn：为Fig.1时序图和第4节高规格规范提供消息细节。

- evidence_pointer：Section 3.4第3段

### 44. P4

- order：44

- section：Section 3.4

- locator：P4

- move_code：DESIGN_FEATURE

- paraphrase_cn：服务器解密每个标签响应后检查阅读器nonce是否匹配、标签ID有效、q(tag-info)和q(prod-info)都为真；不满足的响应被丢弃，最后把有效标签的产品属性返回给阅读器。

- rhetorical_function_cn：说明服务器如何实现声音性并完成查询语义过滤。

- depends_on_cn：P3的消息结构和服务器密钥。

- sets_up_cn：让Theorem 1的声音性证明针对具体的校验逻辑。

- evidence_pointer：Section 3.4第4段

### 45. P2

- order：45

- section：Section 3.5

- locator：P2

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：作为首个属性搜索协议，本文优先正确性、可证明安全和标签端复杂度，因此不采用标签与阅读器之间的双向认证。

- rhetorical_function_cn：坦诚设计取舍，防止读者用通用RFID认证标准批评。

- depends_on_cn：P1对单公钥选择的说明。

- sets_up_cn：后文Table 1中P2标注‘×’的理由。

- evidence_pointer：Section 3.5第2段

### 46. P3

- order：46

- section：Section 3.5

- locator：P3

- move_code：MECHANISM

- paraphrase_cn：标签用唯一秘密和服务器公钥加密，使服务器通过数据库查找即可认证标签；若改用对称密钥，要么牺牲标签隐私，要么需要服务器穷举搜索正确密钥。

- rhetorical_function_cn：解释为什么选择非对称方案而不是更常见的对称认证。

- depends_on_cn：P2对双向认证的排除。

- sets_up_cn：为隐私-可扩展性权衡讨论铺垫。

- evidence_pointer：Section 3.5第3段

### 47. P4-P5

- order：47

- section：Section 3.5

- locator：P4-P5

- move_code：LIMITATION_AND_FUTURE

- paraphrase_cn：若服务器私钥泄露，机密性将被破坏；密钥撤销和更新不在本文范围。许多RFID协议追求无服务器、双向认证和对称加密，但这些不是属性搜索协议的首要目标，可留作未来工作。

- rhetorical_function_cn：界定安全失效条件和后续方向，避免读者高估协议。

- depends_on_cn：单公钥设计选择。

- sets_up_cn：为第4节边界讨论和结论中的未来权衡做铺垫。

- evidence_pointer：Section 3.5第4-5段

### 48. P1

- order：48

- section：Section 4

- locator：P1

- move_code：STUDY_OVERVIEW

- paraphrase_cn：接下来通过把协议转化为高层规范，用Scyther证明正确性，并进行形式化隐私分析。

- rhetorical_function_cn：预告评价阶段的两个组成部分。

- depends_on_cn：Section 3的协议定义。

- sets_up_cn：把读者从设计引向验证。

- evidence_pointer：Section 4开头

### 49. P1-P2

- order：49

- section：Section 4.1

- locator：P1-P2

- move_code：THEORY_INTRO

- paraphrase_cn：使用Cremers和Mauw的符号安全模型：敌手可窃听、阻断、修改、发送消息，并可能通过损坏参与者学到长期密钥；协议被建模为角色和事件序列，敌手控制所有接收事件。

- rhetorical_function_cn：建立本文安全证明的权威基础。

- depends_on_cn：协议采用Dolev-Yao敌手（Section 3.4）。

- sets_up_cn：让Scyther验证结果具有正式语义。

- evidence_pointer：Section 4.1第1-2段

### 50. Definition 2后

- order：50

- section：Section 4.1

- locator：Definition 2后

- move_code：THEORY_PROPOSITION

- paraphrase_cn：非注入一致性是指当诚实主体完成任务时，另一方确实此前也运行了该协议，且双方在运行中的原子数据上达成一致。

- rhetorical_function_cn：定义用于验证的主要安全属性。

- depends_on_cn：Cremers-Mauw模型。

- sets_up_cn：Scyther检验这一属性即可推出抗重放和冒充。

- evidence_pointer：Section 4.1 Definition 2

### 51. P4

- order：51

- section：Section 4.1

- locator：P4

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Scyther是Cremers和Mauw开发的自动化验证工具，能无界验证并保证终止；本文目标是用法表达协议并用它证明安全属性。

- rhetorical_function_cn：解释选择Scyther作为评价工具的理由。

- depends_on_cn：前面的Symbolic模型。

- sets_up_cn：第4.2节的高层规范。

- evidence_pointer：Section 4.1第4段

### 52. P1

- order：52

- section：Section 4.2

- locator：P1

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：Cremers-Mauw模型假设理想加密，因此需把模指数等运算替换为带同等功能和安全目标的符号公钥加密。

- rhetorical_function_cn：说明从实际协议到可验证规范的映射方式。

- depends_on_cn：Scyther的建模能力限制。

- sets_up_cn：让后续验证结果适用于原协议的逻辑结构。

- evidence_pointer：Section 4.2第1段

### 53. P3

- order：53

- section：Section 4.2

- locator：P3

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：用P_n表示规范化的n标签协议，核心主张是原属性搜索协议的安全性可由P_n的安全性推出。

- rhetorical_function_cn：把实际协议的安全责任转移到可验证对象上。

- depends_on_cn：P1的映射说明和Fig.2规范。

- sets_up_cn：下一节Lemma 1/2和Theorem 1的证明对象。

- evidence_pointer：Section 4.2第3段

### 54. Lemma 1证明

- order：54

- section：Section 4.3

- locator：Lemma 1证明

- move_code：RESULT

- paraphrase_cn：用Scyther验证P_1和P_2满足非注入一致性，在阅读器角色末尾放置claim事件。

- rhetorical_function_cn：给出小规模标签数下的机器验证证据。

- depends_on_cn：附录中的Scyther规范。

- sets_up_cn：支撑下一步归纳推广。

- evidence_pointer：Section 4.3 Lemma 1

### 55. Lemma 2证明

- order：55

- section：Section 4.3

- locator：Lemma 2证明

- move_code：METHOD_JUSTIFICATION

- paraphrase_cn：因为每个标签的响应独立，P_1/P_2的Scyther验证可推广到任意n；再通过假设P_n成立证明P_{n+1}成立，把n标签情形扩展到n+1。

- rhetorical_function_cn：通过归纳法突破Scyther不能直接验证任意标签数的限制。

- depends_on_cn：Lemma 1和标签响应独立性。

- sets_up_cn：让后续安全性主张对任意n成立。

- evidence_pointer：Section 4.3 Lemma 2

### 56. Theorem 1前

- order：56

- section：Section 4.3

- locator：Theorem 1前

- move_code：MECHANISM

- paraphrase_cn：非注入一致性是很强的安全属性，意味着协议抵抗重放和冒充攻击；还需证明它满足Definition 1的正确性。

- rhetorical_function_cn：把安全属性转化为攻击抵抗的直观含义。

- depends_on_cn：Lemma 2的结果。

- sets_up_cn：引出Theorem 1的声音/完备证明。

- evidence_pointer：Section 4.3第4段

### 57. Theorem 1

- order：57

- section：Section 4.3

- locator：Theorem 1

- move_code：RESULT

- paraphrase_cn：P_n在Dolev-Yao敌手下是声音搜索协议；若敌手不阻断标签到阅读器通信，且对每个标签和查询都有q(prod-info)蕴含q(tag-info)，则协议同时声音且完备。

- rhetorical_function_cn：给出本文最关键的功能正确性定理。

- depends_on_cn：Lemma 2的一致性和服务器校验规则。

- sets_up_cn：为后文库存隐私和tag-info超集策略提供依据。

- evidence_pointer：Section 4.3 Theorem 1

### 58. Theorem 1证明

- order：58

- section：Section 4.3

- locator：Theorem 1证明

- move_code：MECHANISM

- paraphrase_cn：声音性源于参与者一致性：服务器和阅读器看到相同消息视图；完备性源于所有满足查询的标签都会响应且消息不被阻断。

- rhetorical_function_cn：解释定理成立的因果机制。

- depends_on_cn：协议中的服务器校验和标签匹配规则。

- sets_up_cn：让读者理解为何声音性比完备性更强也更现实。

- evidence_pointer：Section 4.3 Theorem 1证明

### 59. 末段

- order：59

- section：Section 4.3

- locator：末段

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：定理给出声音和完备的充分条件；声音性最现实，完备性只在可建立无敌手环境（如抗干扰）的关键应用中发挥作用。

- rhetorical_function_cn：界定完备性的适用条件，防止过度外推。

- depends_on_cn：Theorem 1。

- sets_up_cn：为第4.4节隐私分析中的不完美条件铺垫。

- evidence_pointer：Section 4.3末段

### 60. P1-Prop 1

- order：60

- section：Section 4.4

- locator：P1-Prop 1

- move_code：HYPOTHESIS_OR_PROPOSITION

- paraphrase_cn：未被攻陷的标签对阅读器挑战的响应中，敌手无法学到标签生成的nonce或标签ID。

- rhetorical_function_cn：先证明消息内容的保密性，这是隐私分析的第一步。

- depends_on_cn：Scyther对P_2的秘密性验证。

- sets_up_cn：为不可追踪性结论提供必要前提。

- evidence_pointer：Section 4.4 Proposition 1

### 61. Prop 1后

- order：61

- section：Section 4.4

- locator：Prop 1后

- move_code：MECHANISM

- paraphrase_cn：因为未损坏标签的每条消息都包含新生成且保密的nonce，所以标签自己不同轮次和不同标签之间的响应都无法区分。

- rhetorical_function_cn：解释秘密性如何转为不可追踪性。

- depends_on_cn：Proposition 1。

- sets_up_cn：Corollary 1直接利用这一机制。

- evidence_pointer：Section 4.4第2段

### 62. Corollary 1

- order：62

- section：Section 4.4

- locator：Corollary 1

- move_code：RESULT

- paraphrase_cn：给定某未损坏标签的响应，敌手无法以高于1/2的概率判断其来自两个候选标签中的哪一个。

- rhetorical_function_cn：形式化标签不可追踪性。

- depends_on_cn：Proposition 1和消息不可区分机制。

- sets_up_cn：与后文的k-匿名等价类呼应。

- evidence_pointer：Section 4.4 Corollary 1

### 63. P3

- order：63

- section：Section 4.4

- locator：P3

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：需要注意，安全隐私分析采用理想密码学假设，即密码原语不会被破解。

- rhetorical_function_cn：明确安全证明的密码学前提。

- depends_on_cn：Prop1/Corollary1。

- sets_up_cn：避免读者将符号模型证明与实现安全性混淆。

- evidence_pointer：Section 4.4第3段

### 64. P4

- order：64

- section：Section 4.4

- locator：P4

- move_code：LIMITATION

- paraphrase_cn：尽管消息不可追踪，敌手仍可从标签是否回复某查询推断其属性满足查询；因此定义满足同一查询的标签等价关系~q。

- rhetorical_function_cn：指出消息层面的不可追踪并不等于属性层面的不可推断。

- depends_on_cn：Corollary 1的不可追踪性。

- sets_up_cn：引入k-匿名等价类。

- evidence_pointer：Section 4.4第4段

### 65. Proposition 2后

- order：65

- section：Section 4.4

- locator：Proposition 2后

- move_code：RESULT

- paraphrase_cn：协议满足k-匿名：响应者被分成等价类，匿名强度与等价类大小成比例；确定适当大小是情境依赖问题。

- rhetorical_function_cn：把隐私性质连接到经典匿名文献。

- depends_on_cn：Proposition 2的概率公式。

- sets_up_cn：为后文库存不确定性作铺垫过渡。

- evidence_pointer：Section 4.4 Proposition 2后

### 66. P6

- order：66

- section：Section 4.4

- locator：P6

- move_code：BOUNDARY_CONDITION

- paraphrase_cn：协议不满足Avoine的强不可追踪性，因为那要求两标签不可区分概率不可忽略；除非建立很大的匿名类，否则会牺牲通信复杂度。

- rhetorical_function_cn：明确放弃何种隐私标准，避免被抽象标准否定。

- depends_on_cn：Corollary 1和Proposition 2。

- sets_up_cn：引出以库存隐私为目标的替代分析。

- evidence_pointer：Section 4.4第6段

### 67. Definition 3前后

- order：67

- section：Section 4.4

- locator：Definition 3前后

- move_code：THEORY_PROPOSITION

- paraphrase_cn：定义库存不确定性为所有查询中，敌手按tag-info错误计数的标签数与服务器按prod-info正确计数之差的最小值。

- rhetorical_function_cn：提出本文自己的库存隐私度量。

- depends_on_cn：tag-info/prod-info的区别和查询集合。

- sets_up_cn：解释tag-info超集策略的收益。

- evidence_pointer：Section 4.4 Definition 3

### 68. Definition 3后

- order：68

- section：Section 4.4

- locator：Definition 3后

- move_code：MECHANISM

- paraphrase_cn：库存不确定性与可扩展性存在权衡：越多标签错误响应，通信复杂度越大；库存所有者需在初始化时决定如何平衡；若tag-info=prod-info则无库存隐私。

- rhetorical_function_cn：解释隐私机制的成本和选择权归属。

- depends_on_cn：Definition 3。

- sets_up_cn：为Theorem 2的超集策略提供动机。

- evidence_pointer：Section 4.4第7-8段

### 69. Theorem 2

- order：69

- section：Section 4.4

- locator：Theorem 2

- move_code：RESULT

- paraphrase_cn：如果每个标签都满足prod-info⊆tag-info，则协议对Q_A上的合取/析取查询保持声音性。

- rhetorical_function_cn：证明超集初始化的正确性边界。

- depends_on_cn：Theorem 1和单调属性蕴含。

- sets_up_cn：使库存隐私增强策略具有形式保证。

- evidence_pointer：Section 4.4 Theorem 2

### 70. Theorem 2后

- order：70

- section：Section 4.4

- locator：Theorem 2后

- move_code：MECHANISM

- paraphrase_cn：通过让标签存储真实产品属性的超集，可让攻击者误以为库存更大；只有服务器数据库能判断标签是否真正满足查询。

- rhetorical_function_cn：把定理翻译成可操作的设计意图。

- depends_on_cn：Theorem 2。

- sets_up_cn：供第4.5节对比时作为库存隐私优势。

- evidence_pointer：Section 4.4 Theorem 2后

### 71. P1-Table 1

- order：71

- section：Section 4.5

- locator：P1-Table 1

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：用表1比较本协议与Huang、Won、Tan、Zuo、Kulseng、Kim等协议在属性搜索、双向认证、匿名、不可追踪、抗重放、抗DoS和EPC合规方面的表现。

- rhetorical_function_cn：建立文献参照系，通过特征矩阵显示相对位置。

- depends_on_cn：既有协议文献分析[52,10]。

- sets_up_cn：为下段逐个解释差异点。

- evidence_pointer：Section 4.5 Table 1

### 72. P2

- order：72

- section：Section 4.5

- locator：P2

- move_code：RESULT

- paraphrase_cn：属性搜索功能只有本协议提供；其他方案都只做身份搜索；本协议符合EPC是因为标签只需PRNG和模平方，这两者可小于1000门。

- rhetorical_function_cn：把表1中的两个关键差异（P1和C1）解释为设计选择的结果。

- depends_on_cn：Section 3.2门数估算和Table 1。

- sets_up_cn：强调本文同时占据功能属性和实现合规优势。

- evidence_pointer：Section 4.5第2段

### 73. P3

- order：73

- section：Section 4.5

- locator：P3

- move_code：BENCHMARK_OR_CONTRAST

- paraphrase_cn：Zuo的方案能防止基于查询内容的追踪但不符EPC；本协议EPC合规且部分不可追踪，按匿名类大小保护；双向认证据知是EPC约束下难以同时实现的特征。

- rhetorical_function_cn：诚实标注本方案在P2/P4上的边界。

- depends_on_cn：Table 1数据和Proposition 2。

- sets_up_cn：防止读者把所有安全协议标准都想当然套用。

- evidence_pointer：Section 4.5第3段

### 74. P4

- order：74

- section：Section 4.5

- locator：P4

- move_code：RESULT

- paraphrase_cn：本协议在标准Dolev-Yao模型中被形式验证，因此抗重放和冒充，且不使用更新密钥故无DoS/去同步问题。

- rhetorical_function_cn：汇集前面验证结论并映射到表1的A1/A2。

- depends_on_cn：Lemma 2, Theorem 1和表1。

- sets_up_cn：进入结论总结。

- evidence_pointer：Section 4.5第4段

### 75. P1

- order：75

- section：Conclusion

- locator：P1

- move_code：CONTEXT

- paraphrase_cn：有效库存管理依赖准确库存、缺货和需求知识；人工盘点耗时，条码自动化不可行，数据库又不准确；RFID方案已在零售自动库存管理应用十余年。

- rhetorical_function_cn：回接引言中的库存管理现实问题。

- depends_on_cn：Introduction第4-5段。

- sets_up_cn：为结论中的协议贡献提供应用锚点。

- evidence_pointer：Conclusion第1段

### 76. P2

- order：76

- section：Conclusion

- locator：P2

- move_code：CONTRIBUTION

- paraphrase_cn：我们提出安全属性搜索轻量协议，基于二次剩余，避免昂贵密码原语和哈希，满足EPC，在Dolev-Yao下安全，并为单个标签和整个库存提供隐私，代价是服务器计算增加；未来研究实际库存系统中的权衡。

- rhetorical_function_cn：重述所有贡献并指出未来方向。

- depends_on_cn：全文各节结果。

- sets_up_cn：以“未来权衡”结束，呼应第3.5和第4.4中的开放问题。

- evidence_pointer：Conclusion第2段

## 写作技术

- gap_construction_cn：作者将缺口分成两层：功能缺口（现有安全搜索都只是ID搜索，无法按属性搜索一组库存物品）和约束缺口（现有密码原语因门数限制无法在被动RFID标签上部署并符合EPC）。然后宣称这两种缺口的交汇处无人占据，形成“首个属性搜索协议”的空间。

- signposting_cn：在引言末尾提供Organization段；第3节开头预告“正确性定义、密码原语、设置和操作阶段”；第4节开头预告“Scyther正确性证明＋隐私分析”；每一小节的标题和Definition/Lemma/Prop编号也形成可预期的阅读路径。

- transition_logic_cn：从功能定义过渡到密码选择（“为满足Definition 1需要轻量加密”）；从密码原语过渡到密钥初始化；从协议设计过渡到形式验证（“下一步用Scyther证明”）；从安全过渡到隐私（“还需证明消息不泄露身份和库存”）；从隐私过渡到对比（“用标准性质表定位”）。每一段的最后一句常为下一段提出问题。

- claim_evidence_rhythm_cn：论文采用“定义/定理—证明—解释”的节奏：先给数学命题，再给Scyther或逻辑证明，再用一两句话把证明翻译成直观的安全含义。Table 1则把抽象结果压缩成特征矩阵，作为最终证据。

- benchmark_narrative_cn：没有数值benchmark；作者把benchmark转化为特征矩阵：以Huang、Won、Tan、Zuo、Kulseng、Kim为基线，在属性搜索、双向认证、匿名、不可追踪、抗重放、抗DoS和EPC合规七个维度对比，让本方案在P1和C1两项上占据唯一正面位置，同时诚实列出P2未满足。

- theory_return_cn：所有安全证明都返回第3.1节定义的声音/完备方程；隐私证明返回tag-info与prod-info的关系；最终结论再次回到“库存数据库不准确”的应用理论，使形式化结果不是孤立的密码学产物，而是面向IS库存决策的设计知识。

- contribution_positioning_cn：作者用一个三重定位：功能上“一般化身份搜索”、实现上“EPC合规轻量”、证据上“Dolev-Yao形式验证”。在对比表中突出其他方案缺少P1或C1之一，从而让“首个属性搜索”不只是一个名称，而是清空邻近方案后的唯一位置。

- novelty_protection_cn：通过把“属性搜索”定义为一个新的协议类型（Definition 1），并把ID搜索描述为其特例，作者把新方案与旧工作区分开；通过Scyther归纳证明和多层隐私属性，使得贡献不易被视为一次性性能结果；通过明确提出不完备性、无双向认证、未满足强不可追踪性，反而增加可信度并保护核心贡献不被过度推攻击。

## 可复用研究与写作程序

### structure_steps

#### 1. 1

- step：1

- writing_job_cn：建立应用背景：从RFID库存控制的重要性和现存安全搜索的ID限制之间制造缺口。

- research_job_cn：梳理现有安全搜索协议，确认没有属性搜索方案，并识别被动标签硬件约束。

- required_evidence_cn：至少需要若干现有协议的特征证据、EPC标准对门数的限制、零售库存场景示例。

- transition_to_next_cn：从“现有只能ID搜索”过渡到“需要定义属性搜索协议的正确性”。

#### 2. 2

- step：2

- writing_job_cn：形式化问题：用定义给出协议类型和验收标准（声音性、完备性）。

- research_job_cn：将非正式需求翻译为精确的形式化功能性质，并区分现实可达到与理想性质。

- required_evidence_cn：能证明“声音性在Dolev-Yao下成立、完备性需要更强条件”的逻辑理由。

- transition_to_next_cn：形式化需求引出具体密码原语选择。

#### 3. 3

- step：3

- writing_job_cn：设计制品：选择满足硬件约束的密码原语并描述协议消息流。

- research_job_cn：用门数证据和密码学性质筛选标签端运算；设计两阶段消息和服务器校验。

- required_evidence_cn：每个标签端操作的门数或已有实现文献；EPC标准中的ITF要求；协议消息结构。

- transition_to_next_cn：协议消息结构齐备后，引入形式化验证工具。

#### 4. 4

- step：4

- writing_job_cn：形式化验证：把协议抽象为高规格规范并在Scyther中验证小规模情形，再用归纳扩展到任意规模。

- research_job_cn：编码协议角色和claim，运行Scyther，补数学归纳证明。

- required_evidence_cn：Scyther规范、验证结果、归纳证明步骤；同时说明理想加密假设。

- transition_to_next_cn：安全证明完成后转向隐私分析。

#### 5. 5

- step：5

- writing_job_cn：隐私分析：证明消息机密性、不可追踪性、k-匿名和库存不确定性，并明确放弃的隐私标准。

- research_job_cn：设计隐私度量；用命题/推论/定理建立隐私性质；设定超集初始化策略。

- required_evidence_cn：Scyther秘密性claim、概率定理、库存不确定性定义和定理证明。

- transition_to_next_cn：隐私边界明确后，与既有协议比较。

#### 6. 6

- step：6

- writing_job_cn：对比定位：用特征矩阵显示本方案相对基线的唯一优势与边界。

- research_job_cn：收集既有协议的性质，建立公平对比维度。

- required_evidence_cn：每个协议在所选性质上的结论来源；本方案在同维度上的证明或直接设计结果。

- transition_to_next_cn：对比完成，进入结论重述贡献和未来。

#### 7. 7

- step：7

- writing_job_cn：结论闭环：重述初始库存问题，归纳贡献，坦诚限制并给未来权衡方向。

- research_job_cn：把抽象协议贡献回放到IS应用层。

- required_evidence_cn：前面各阶段的定理和对比表；明确不做的工作。

- transition_to_next_cn：无后续步骤。

### most_transferable_moves_cn

1. 把应用需求转化为可证明的功能定义（声音/完备）

2. 用硬件门数证据限制密码原语选择

3. 用Scyther验证小规模并归纳到任意规模的证据链

4. 通过特征矩阵而不是数值benchmark定位新制品

5. 在每个强断言旁主动给出边界条件，增加可信度

### resource_intensive_or_nonstandard_parts_cn

1. 需要RFID安全协议和数论知识的深度积累

2. 需要Scyther工具使用和形式化协议编码能力

3. 门数估算依赖已有硬件文献而非自有实现

4. 没有真实标签硬件和库存环境，无法直接套用部署结论

5. 属性搜索首创声明需要系统且更新的文献检索支持

### what_not_to_copy_superficially_cn

1. 不能只写“首个”而不做全面的文献对比矩阵

2. 不能声称形式化安全却只给非正式讨论，必须有Scyther规范和归纳证明

3. 不能声称EPC合规却只写“轻量”，必须指出每个标签端运算的门数来源

4. 不能只给出强不可追踪性声明，而要说明为何在低端标签上不追求该标准

5. 不能把形式验证的结果等同于真实密码实现安全性，必须明示理想加密假设

- single_best_description_of_the_routine_cn：把应用缺口形式化为功能性质，用轻量密码原语构造制品，再用Scyther小规模验证加归纳证明来支撑安全，用特征矩阵定位文献空间，最后把隐私边界和未来权衡一并写进贡献。

## 分析边界

本文基于全文文本和图片占位符分析；表格和MSC图内容通过OCR/文本恢复，未提供物理页码；Scyther附录代码保留但不足以执行复现，只能从文本判断其作用；无实际实验数据，故评价完全依赖形式验证和文献门数，无法交叉核验真实硬件性能。
