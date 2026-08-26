# Individual software design examples

Completed: 1832 / 1832
Retained: 77

## Bringing transparency and trustworthiness to loot boxes with blockchain and smart contracts

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113508
- Artifact: LootBoxes smart contract and the corresponding web-based DApp (proof of concept)
- Individual user/task: 单个游戏玩家在购买/开启Loot Box时查看可赢物品与概率，并在购买后核验抽取结果是否确实来自区块链上的智能合约。
- Design delta: 将随机抽取逻辑从游戏闭源代码中解耦到公开区块链智能合约：购买前公开可验证的物品/概率列表；用block.timestamp和screenName的keccak256哈希生成伪随机数；限制同一区块内每个玩家只能购买一次；仅允许游戏开发者地址调用drawItem函数；所有调用和结果上链可审计。
- Design process: 遵循Peffers et al. (2007)的问题中心设计科学研究框架：先识别Loot Box的透明性和信任问题，用决策理论说明个体玩家需要可见概率才能做出理性购买决策，再用Pedersen et al. (2019)的区块链决策模型论证公有区块链方案的适用性，随后设计并实现智能合约与DApp，最后通过卡方检验、Securify/MythX安全分析和gas成本分析进行评价。作者明确说明未优化用户界面，UI设计超出该文范围。
- Potential coding-agent design value: 该源码方法可为编码智能体产品设计提供借鉴：用一个小型可运行的原型把原本不透明的随机/决策过程改造成用户可验证、可审计的交互流程，例如在编码辅助工具中增加透明决策日志、可验证的约束控制或可审计的步骤信息。
- Decision: 三个条件全部满足：设计聚焦于单个玩家购买和开启Loot Box的个体使用场景；作者实际构建并部署了可在浏览器中使用的Web DApp和智能合约这一可运行的个体面向软件制品；开发为单作者完成的有界原型，使用公开测试网和API，无需企业合作、大规模数据或基础设施，适合小研究团队复现。
- Confidence: 0.96

## Enhancing Customer Service Chatbot Effectiveness: The Effect of Dyadic Communication Traits on Customer Purchase Intention

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00931
- Artifact: Alimebot-based customer service chatbots (warmth, competence, and control versions)
- Individual user/task: 个体顾客在淘宝移动端与客服聊天机器人就T恤购买进行至少五次问答，然后形成购买决策；任务是获得售前商品信息支持并表达购买意向。
- Design delta: 通过Alimebot的“关键词-回复”映射为三个机器人配置不同的回复策略；在内容相同的情况下改变用户可见的沟通特质，包括温暖线索（如“亲爱的”、表情符号、“~”语气）和胜任线索（如专业措辞、Q&A列表、图标菜单、外链详细信息的点击图标）。
- Design process: 先对23名电商平台聊天机器人用户进行半结构化访谈，收集能体现温暖和胜任的副语言线索；随后进行两轮卡片分类（每轮8名研究生），用Cohen's kappa和item placement ratio筛选出16条可靠线索；基于这些线索在Alimebot上配置三种聊天机器人；通过两个前测（N=112和N=51）验证操纵有效性与任务真实性，再用于正式实验。
- Potential coding-agent design value: 该来源方法可帮助学习如何在现有对话式代理脚手架（如编码助手）上通过可配置的回复风格、界面特征和交互流程来实例化并测试面向用户的沟通特质，再用小型用户研究验证设计差异。
- Decision: 三项条件均满足：研究聚焦个体顾客与聊天机器人的一对一互动；作者实际构建并配置了三个可运行的、用户可真实对话的客服聊天机器人（Alimebot/淘宝）；开发方式为开放API配置、小规模访谈和用户实验，无需大型组织、庞大数据集或专用基础设施。
- Confidence: 0.96

## Achieving a Balance Between Privacy Protection and Data Collection: A Field Experimental Examination of a Theory-Driven Information Technology Solution

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1045
- Artifact: negotiation, active-recommendation privacy policy application
- Individual user/task: 个体消费者在移动银行应用场景中阅读或协商隐私政策，按自己的隐私偏好决定是否以及以何种粒度披露个人身份、收入等个人信息，以换取基础或个性化银行服务。
- Design delta: 相对传统单向隐私声明，新增两个可运行的产品功能：（1）协商功能——消费者可逐项调整要求披露的信息及其粒度，系统按公司下限策略判断是否接受或提示妥协；（2）主动推荐功能——根据消费者类别（隐私原教旨主义者/务实多数/边缘关注者）推荐个性化隐私策略，并据此定制默认信息请求。UI还包括下拉粒度选项、信息用途说明、冲突红色提示等具体交互细节。
- Design process: 首先基于正义理论（程序/互动/分配正义）将协商和主动推荐映射为隐私政策的两个IT特征；通过241名网银用户的调查和4位IS专家校验确定异质性隐私偏好的加权公式；访谈3位银行管理者确定信息项；对120名被试调查信息敏感度/使用担忧，采用隐私妥协值法和信息泛化方法设计三类消费者的上下限策略；随后开发三个应用，并通过三轮预测试（10名师生、46名被试、线下银行）迭代界面和流程；最后用现场实验随机分配336名被试检验效果，并用结构方程模型做post hoc机制分析。
- Potential coding-agent design value: 该文提供了一条“从理论构念推导用户可见功能→将有界Web原型分版本实现→通过预测试和个体用户实验迭代”的完整示例路径，可用于指导为编码代理设计个性化默认策略、用户可协商配置项和冲突提示等交互机制。
- Decision: 三项条件均满足：焦点是消费者个人在移动银行应用中的隐私协商与信息披露决策（个体层面）；作者实际开发并运行了三个Web移动银行应用原型，并实质性修改了隐私政策的产品功能（协商、主动推荐、界面控制）（可运行的个体面向软件工件）；其构建方式为有界Web原型开发加调查/访谈/预测试，不依赖组织变革、长期部署、硬件或大规模基础设施（小型研究团队可行）。
- Confidence: 0.95

## Animation as a dynamic visualization technique for improving process model comprehension

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2021.103478
- Artifact: Adaptive animation environment for process model comprehension
- Individual user/task: 单个过程模型使用者（学生、研究生、咨询师、研究人员）阅读理解BPMN过程模型的动态行为，并完成基于模型的转移型问题解决任务（如判断执行顺序、排他性、并发性、重复性及流程问题）。
- Design delta: 在静态过程模型之上增加动态可视化：增量颜色信号标识执行轨迹、活动状态从就绪到已执行的颜色变化、对并行/选择分支的时序抽象，以及两级交互性设计（低交互视频与高交互逐步执行），并支持用户在两种交互模式间自适应切换。
- Design process: 设计过程主要基于理论推演：作者从认知负荷理论和认知维度框架出发，识别过程模型理解中的四种认知挑战，再依据多媒体学习理论、动画与学习文献中的信号原则、注意引导、使能/助长功能、低交互性、工作样例、分段、交互性等原则，确定动画的视觉特征和交互功能。随后通过专家研究者检查过程模型、进行试点运行并确定正确答案，实验材料经过迭代校准。
- Potential coding-agent design value: 该来源方法可启发编码智能体产品设计中的自适应分步执行可视化与交互控制，例如为不同专业水平用户提供低交互的连续演示和高交互的逐步操作模式。
- Decision: 三项条件均通过：研究对象是个体过程模型用户及其理解任务；作者实际构建并运行了个体面向的自适应动画原型，并改变了过程模型的可视化与交互行为；该原型基于Web技术和开源库构建，规模适合小型学术团队。
- Confidence: 0.95

## Augmenting Password Strength Meter Design Using the Elaboration Likelihood Model: Evidence from Randomized Experiments

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1125
- Artifact: ELM-augmented password strength meter
- Individual user/task: 个人用户在网站注册账户时输入密码，密码强度计实时评估密码强度并显示警告信息，促使用户将弱密码修改为更强的密码。
- Design delta: 在保持密码强度算法和强度标签不变的前提下，仅改变用户可见的警告消息内容：（1）Time——显示估计破解时间（如'10秒破解'）；（2）Rank——显示密码在弱密码中的排名（如'300个最弱密码之一'）；（3）Probability——显示在100亿账户中估计有多少账户使用相同密码；另在实验室版本中加入'Tips towards strong passwords'可点击链接。
- Design process: 作者遵循设计科学研究范式，先从ELM理论提炼Type V'设计与行动'设计原则：通过中央路径处理（激发认知思考的消息）增强密码强度计的劝说效果；然后调研ELM在其它领域的应用，选出三类说服性消息（恐惧诉求、同伴比较、共同纽带），并将其操作化为密码强度计中的具体警告文本；随后依次通过调查实验（证明概念）、受控实验室实验（证明价值）和现场实验（证明使用）进行验证，并根据结果强调Rank（同伴比较）消息最有效。
- Potential coding-agent design value: 该文展示了一种可迁移的产品设计方法：用心理学理论（ELM）生成少量用户可见的消息变体，并通过随机实验比较不同反馈形式对个体行为的影响；这可为coding agent中用户可见的警告、进度、比较或提示信息设计提供借鉴。
- Decision: 三项条件均满足：研究焦点是个人用户在账户创建时的密码输入行为；作者实际构建并材料修改了可运行的网页密码强度计（含三种理论驱动的警告消息变体）；开发资源为公开数据集、客户端JavaScript和常规服务器，小团队可复现，合作网站仅用于现场验证而非构建人工物。
- Confidence: 0.95

## Bots with Feelings: Should AI Agents Express Positive Emotion in Customer Service?

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1179
- Artifact: Taylor（文本型AI客服聊天机器人）
- Individual user/task: 个体顾客（实验参与者）以客户身份与文本客服机器人聊天，解决一个具体的服务问题（如配送缺件、教材换货）。
- Design delta: 在保持脚本其余内容一致的前提下，将机器人消息中的积极情绪表达（情绪形容词、感叹号）从无到有地加入，形成 emotion-absent 与 emotion-present 两个版本；此外通过图标操纵代理身份。核心设计增量是聊天机器人的正面情绪表达这一对话风格/交互特征。
- Design process: 脚本依据 livechat.com 的客服最佳实践和 canned responses 改编；情绪强度操纵参考 Yin et al. (2017) 使用感叹号和情绪形容词；先通过预试验验证情绪强度感知和适当性，再在三个实验中逐步修改脚本（如更换服务问题、增加一条消息）并加入新的测量。
- Potential coding-agent design value: 该来源的方法可帮助小型团队学习如何为编码智能体（如编码助手聊天机器人）设计并测试用户可见的沟通风格特征——例如在交互脚本中系统性地加入或移除积极情绪表达，并通过可控的交互原型实验来评估其对个体用户体验的影响。
- Decision: 三个条件均满足：研究聚焦个体顾客与客服聊天机器人的交互；作者实际构建并运行了一个有脚本的、可逐轮输入回复的文本对话机器人，并通过消息文案和图标对情绪表达这一用户可见特性进行了实质性修改；开发仅为脚本式聊天原型，使用 MTurk/学生样本即可完成，无企业级或基础设施依赖，适合小型学术团队。
- Confidence: 0.95

## Bringing Machine Learning Systems into Clinical Practice: A Design Science Approach to Explainable Machine Learning-Based Clinical Decision Support Systems

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00820
- Artifact: RadiologyAI
- Individual user/task: 放射科医生（radiologists）在CT影像上检测和分类肺结节的诊断任务中使用该系统；医生查看ML模型的恶性概率建议并输入自己的分类。
- Design delta: 与无解释版本相比，设计增量是在CDSS中按类别加入并组织多类型解释：按需提供的模型解释（模型卡）、全局解释（因技术原因未实现）、默认可见的局部解释（恶性概率、热力图、结节特征、相似结节），并按医生工作流和知识进行表述，同时加入基于活检确诊和同行评议文献的确定性信息。
- Design process: 采用Peffers et al. (2007)与Vaishnavi & Kuechler (2007)的六阶段设计科学研究，迭代两轮：从XAI文献和可用性/认知努力文献推导元需求；第一轮通过57名医生在线调查形成四个初始设计原则并用Balsamiq实现线框图，经6名放射科医生walk-through评估；第二轮根据评估修订扩展为五个设计原则，实现为Web原型RadiologyAI，并通过45名放射科医生的在线实验评估。
- Potential coding-agent design value: 该来源的方法可帮助我们学习如何为一个面向个体专业用户的有界Web原型定义设计原则，并通过用户调查、walk-through和在线实验迭代地设计可解释、低认知负荷的产品功能（如解释信息的分类、按需呈现和工作流对齐）。
- Decision: 三个条件均满足：设计对象是放射科医生个体使用CDSS完成肺结节分类；作者实际构建了可运行的Web原型RadiologyAI并加入多类型解释；使用公开数据集和常规Web/ML开发，无医院部署或组织依赖，适合小团队。
- Confidence: 0.95

## Designing Conversational Dashboards for Effective Use in Crisis Response

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00801
- Artifact: Conversational Dashboard for the COVID-19 Pandemic
- Individual user/task: 普通公众个体用户（尤其是非技术型用户）通过语音或文字自然语言（以及可选的鼠标）与仪表板交互，查找COVID-19疫情相关信息（如各州病例数、死亡数、日期过滤、下钻/上卷），以支持日常决策。
- Design delta: 在传统GUI仪表板上新增自然语言交互能力（DP1：语音/文字输入可与仪表板交互），允许用户自由选择自然语言或鼠标（DP2），并新增对话式引导教程（DP3：按序演示并让用户复现过滤、下钻、上卷操作，同时提供即时反馈和错误提示）。
- Design process: 采用设计科学研究（DSR）方法（Kuechler & Vaishnavi, 2008），分两个构建-评价循环。第一轮进行文献综述和对6名非技术用户的访谈，基于TEU导出元需求（MR1、MR2）和三个初始设计原则，构建第一个原型（有帮助按钮但无对话式引导），并用15名参与者的出声思维与访谈评估；第二轮根据第一轮结果引入对话式引导，开发完整工件，并通过271名参与者的在线实验进行评价，最终综合为萌芽设计理论。
- Potential coding-agent design value: 该论文展示了一个小型研究团队如何基于公开数据、开源组件和云API构建并迭代一个有界但完整的对话式个体面向工具原型（含自然语言交互与引导式新手教程），可为编码智能体产品的自然语言交互、任务引导学习和以用户研究驱动的迭代设计提供可参照的模板。
- Decision: 三个条件均满足：研究聚焦于个体用户与仪表板的交互（非组织层面）；作者实际构建了可运行的对话式仪表板原型并进行了多版本迭代和实验评估（非仅算法或线框图）；开发基于开源组件、公开数据和可控众包评估，不需要组织合作、大型基础设施或长期现场部署，适合小型学术团队。
- Confidence: 0.95

## Designing Online Virtual Advisors to Encourage Customer Self-disclosure: A Theoretical Model and an Empirical Test

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1962595
- Artifact: Virtual Advisor (VA) for skin care advice
- Individual user/task: 成年女性消费者个体使用在线虚拟顾问，回答一系列护肤相关问题以获取个性化护肤建议，并可以选择不回答某些问题。
- Design delta: 在虚拟顾问的对话中加入了 why 解释（说明为何询问某问题）、how 解释（说明用户提供的信息将如何被使用/纳入决策）以及表达性言语行为（如表达关心），并分别以有/无进行 2×2×2 操纵；这些设计元素用于影响用户对顾问透明度和响应性的感知。
- Design process: 通过分析护肤网站和论坛确定需要询问的因素；通过四项预试验（Pilot Studies，见附录B）检验和筛选设计元素与脚本，最终保留 why 解释、how 解释和表达性言语行为三个设计元素；采用 2×2×2 被试间实验设计进行验证。
- Potential coding-agent design value: 该研究展示了如何在有界可运行的对话式顾问原型中，通过少量、可实现的交互设计元素（解释与表达性言语行为）系统性地操纵用户对助手透明度与响应性的感知，可为我们设计编码助手的信息呈现与对话反馈机制提供方法借鉴。
- Decision: 三个条件均满足：个体用户与在线虚拟顾问交互；研究者构建并运行了一个可交互的护肤建议虚拟顾问，并在其中实际操纵解释与言语行为等设计元素；该方法为有界网页原型加预试验与在线实验，无企业或基础设施依赖，适合小型学术团队。
- Confidence: 0.95

## Mental models and expectation violations in conversational AI interactions

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113515
- Artifact: Custom conversational agents (CAs) developed in ChatScript for a movie recommender chat system
- Individual user/task: 个体参与者通过文本聊天与对话智能体交互，回答关于电影偏好等问题，以接收电影推荐并评价对话体验。
- Design delta: 核心设计差异是对话能力的两种具体实现：低能力版在四个追问位置统一回复‘Okay. Can you tell me more about that?’；高能力版基于关键词触发的定制化后续问题，并设置回应的多样性；此外，交互前通过提示语告知用户对方是聊天机器人或人类，以操纵期望。
- Design process: 设计需求来自对话智能体文献中的对话能力构成（定制化回应、回应多样性、Grice 的关联准则）；研究团队为每个基础问题预先编写了10–20个预期关键词的回应语料，用 ChatScript 主题机制匹配同义词和相关词；随后进行试点测试，为未预料到的回答补充回应。高能力版在无法定制时使用少量合理的通用回应。
- Potential coding-agent design value: 该方法可帮助小型团队学习如何构建一个轻量级可运行的对话式原型，通过改变回复的定制化与多样性来操作产品行为，并配合用户期望提示，从而研究用户对编码智能体不同能力的感知与评价。
- Decision: 三项条件均满足：研究聚焦个体用户与对话智能体的交互；作者实际构建并运行了两个 ChatScript 定制对话智能体，作为可运行的个体面向软件原型，并对对话能力进行了具体设计改动；构建方式为脚本编写、语料开发和试点测试，无组织、硬件或大规模基础设施依赖，小型研究团队可行。
- Confidence: 0.95

## Mitigating the Security Intention-Behavior Gap:  The Moderating Role of Required Effort on the  Intention-Behavior Relationship

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00660
- Artifact: 
- Individual user/task: 个体用户（参与实验的学生）作为新员工或远程顾问，在模拟组织环境中完成财务报告、采购咨询或打印机评估等任务，同时遵守密码策略或客户信息保密策略。
- Design delta: 通过任务流程和界面特性操纵所需努力：实验1用单点登录 vs 多点登录（多套密码）改变认证步骤数；实验2用单因素 vs 多因素认证（需配置令牌、输入动态PIN）增加认证步骤；实验3在低努力条件下在访问供应商网站前显示即时政策提醒，高努力条件无提醒且需记忆政策。核心变化是增加/减少完成任务所需的认证步骤或认知负担。
- Design process: 作者从理论出发提出假设，然后设计了三个实验室实验，将所需努力作为被操纵的自变量嵌入任务软件中：通过改变认证机制（实验1和2）或是否提供即时提示（实验3）来形成高/低努力条件。研究过程包括训练视频、政策理解测验、意向与PBC问卷、操控检验（自报努力）和行为日志分析；未报告需求访谈或正式的设计迭代。
- Potential coding-agent design value: 该研究展示了如何用轻量级、可运行的界面特性（如即时提示、登录/认证流程中的步骤增减）在个体用户任务中操纵“所需努力”，并以行为日志检验其对意图-行为一致性的影响；这可以帮助编码代理产品设计者学习通过有界原型改变用户摩擦点并观察真实行为反应。
- Decision: 三个条件均满足：研究以个体用户在模拟任务中的密码合规和信息披露行为为对象；作者实际构建/配置了可运行的个体面向实验系统（尤其实验3的网站+自动聊天机器人+即时提示），并实质性改变了认证流程和提示行为；方法是有界实验室原型、学生样本和自建模拟环境，无组织级或重型资源依赖。
- Confidence: 0.95

## Mobile Advertising in Distracted Environments: Exploring the Impact of Distractions on Dual-Task Interference

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/17758
- Artifact: Custom anagram game app with pop-up ads (unnamed; JavaScript/HTML)
- Individual user/task: 个体用户在移动设备或电脑上玩变位词（anagram）游戏，同时观看NFL比赛视频等环境干扰；游戏过程中会被弹窗广告周期性打断。
- Design delta: 将弹窗广告作为任务中断器植入游戏，依据NFL视频内容（play/replay/commentary）决定广告投放时机；通过代言人与品牌同NFL的关联度操纵广告一致性（一致/半一致/不一致）；并通过分屏、多屏个人设备、多屏投影等显示方式改变任务与环境之间的空间距离。
- Design process: 基于DTI文献提出假设后，选择真实NFL比赛片段并逐秒分类为play/replay/commentary以确定广告投放时机；设计九则静态广告，按代言人与品牌与NFL的关联度构造三个一致性水平；编写定制app控制任务和广告时序，并在实验二中通过分屏/多屏/投影操纵空间距离；用app日志和事后调查测量任务参与度和广告参与度。
- Potential coding-agent design value: 该来源方法可帮助学习如何为编码智能体构建有界可运行原型，并在受控个体用户实验中系统操纵智能体消息或提示的时机、内容一致性和界面呈现方式（如同屏/分屏距离），以观察用户任务表现与提示处理的变化。
- Decision: 三项条件均满足：研究聚焦个体用户在移动设备上的任务与弹窗广告交互；团队实际构建并运行了JavaScript/HTML定制app和分屏网站，并实质操纵广告时机、内容一致性与空间距离；开发范围是有界原型，依赖常规设备与在线样本，适合小型研究团队。
- Confidence: 0.95

## Push It Cross the Finish Line—Designing Online Interfaces to Induce Choice Closure at the Postdecision Prepurchase Stage

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0085
- Artifact: Red Brick.com simulated e-commerce site
- Individual user/task: 个人在线消费者在模拟电商网站中选择健康追踪器，并在购物车页面（postdecision prepurchase stage）决定是否继续结账；研究通过界面线索促使其感知决策已完成并提高决策满意度。
- Design delta: 在购物车页面新增/调整决策强化界面元素：(1) 直接强化：15%折扣优惠券、表扬语（'It is a great product. You made the best choice!'）；(2) 社会强化：先前买家准确率/可靠性信息图（注明来源'Monthly Consumer Reports at the Red Brick'）或规范性同伴选择；(3) 呈现时机：将直接强化提示在产品详情页（决策前）与购物车页（决策后）之间切换；(4) 闭合界面：备选商品列表自动消失或需点击'Confirm Your Choice'关闭。
- Design process: 基于认知失调理论与自我辩护理论提出外部合理化界面提示；结合电商弃购实践（BigCommerce）和Amazon/BestBuy评论内容分析选择社会强化信息；通过焦点小组确定优惠券折扣水平（15%）并修订社会强化措辞；以预实验和三项受控实验迭代测试不同提示设计与呈现时机；通过操纵检验确认参与者感知到界面变化。
- Potential coding-agent design value: 该方法可启发编码代理产品设计中的做法：在有限的原型中实现基于理论的、小而具体的用户界面/交互变体（如强化提示、时机控制、任务完成动作），并通过个体用户受控使用观察其认知与行为效果。
- Decision: 符合三项条件：研究对象为个人消费者的在线购物决策；作者实际构建并运行了模拟电商网站'Red Brick.com'，并在购物车页面材料化地添加了多种决策强化界面元素（优惠券、表扬语、社会证明、闭合交互）；开发与实验规模有限（学生样本、焦点小组、公开评论内容），适合小型学术团队复现。因此target_match=true。
- Confidence: 0.95

## Pushing Yourself Harder: The Effects of Mobile Touch Modes on Users’ Self-Regulation

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1155
- Artifact: Experimental mobile beverage-choice app; experimental mobile fitness app; personal hygiene education app
- Individual user/task: 个人用户（消费者、健身者、学生）使用手机应用完成饮料选择、健身目标设定与锻炼、个人卫生学习与承诺等个体任务。
- Design delta: 核心设计差异是改变移动交互中的触摸方式：Study 1 中按压或轻点饮料图片以显示预览和详情页；Study 2 中在设定运动目标前执行一系列按压或轻点操作；Study 3 中以按压、轻点或长按按钮来表示对卫生实践的承诺。按压要求超过一定力度阈值，长按要求较长接触时长。
- Design process: 基于具身认知理论推导按压唤起接近动机、从而增强自我调节的假设，据此在移动应用中操作化按压与轻点交互；通过预测试验证饮料材料的健康/美味感知差异，通过试点测试确认实验程序和移动应用可用性；在 Study 2 中用增益/损失框架文章操纵健康导向（促进 vs 预防），并在 Study 3 中加入长按条件排除接触时长的替代解释。
- Potential coding-agent design value: 该来源的方法可启发我们在编码代理产品中实现一种微妙但可运行的交互层面助推，例如要求用户以更用力的手势或更投入的交互来提交目标或承诺，并用有界原型和小规模个体实验检验其对用户坚持性和目标设定的影响。
- Decision: 三项条件均满足：研究对象为个体用户；作者实际构建并运行了三个移动应用原型，并实质修改了个体用户面对的触摸交互方式（按压 vs 轻点）；开发方式为有界原型和现场个体实验，不依赖被排除的大型资源。
- Confidence: 0.95

## Scratch my back and I'll scratch yours: The impact of user effort and recommendation agent effort on perceived recommendation agent quality

- Year/journal: 2022 / Information & Management
- DOI: 10.1016/j.im.2021.103571
- Artifact: Custom-built web-based product recommendation agent (RA) for car and dating recommendations
- Individual user/task: 个体用户（参与者）在汽车（研究1）或在线约会（研究2）情境中，通过该推荐代理完成偏好表达，并从系统给出的推荐集中选择一辆公司租赁汽车或一个约会对象。
- Design delta: 核心设计差异包括：(1) RA努力线索：高RA努力条件下显示旋转加载器并延迟7秒，低RA努力条件下即时显示结果；(2) 用户努力设计差异：高用户努力条件下用户需对13个（研究1）或19个（研究2）属性给出重要性权重，低用户努力条件下从列表中选取3个（研究1）或5个（研究2）最重要属性。这两个操作用来改变用户感知的自身努力和感知的RA努力。
- Design process: 设计需求主要来自理论演绎：基于社会交换理论的互惠规范提出用户努力与RA努力影响感知质量的假设，再依据既有文献中的努力操纵方式（如属性数量、决策辅助的处理延迟）实例化界面功能；研究2还通过预测试筛选约会对象照片以确保推荐集质量可控，并用操纵检验确认界面线索成功引起感知差异。
- Potential coding-agent design value: 该来源的思路可帮助我们学习如何通过简单、可控的界面线索（如处理进度指示、任务量设计）在个体层面操作用户对智能体努力程度与自身投入的感知，从而为编码智能体的交互反馈与偏好收集流程设计提供示例。
- Decision: 三项条件均满足：研究聚焦个体用户（参与者）与推荐代理的人机交互；作者实际构建并运行了网络版推荐代理，并通过加载延迟和属性数量等界面线索对交互工作流进行了实质性修改；设计是有界实验原型，无需企业合作、专用硬件或长期部署，小型学术团队可复现。
- Confidence: 0.95

## Standardize or Let a Thousand Flowers Bloom? Interface Design Coordination between Software Platforms and Hosted Apps

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16484
- Artifact: 未命名的信息类笑话应用（研究团队开发）
- Individual user/task: 微信个人用户使用该应用浏览每日笑话，属于个体娱乐/信息浏览任务。
- Design delta: 对应用的用户界面和交互行为进行了具体改动：高相似性版本采用与微信相同的字体和背景色，低相似性版本采用对比样式；高嵌入性版本内容在微信界面内展示，低嵌入性版本在外部网页展示；高同步性版本即时加载，低同步性版本人为增加五秒等待时间。
- Design process: 作者基于基本格式塔理论提出三个界面设计原则，并将其操作化为具体的UI属性；随后开发八个版本来实例化这些设计差异，通过随机化现场实验进行操控检验和假设检验。
- Potential coding-agent design value: 该来源方法可帮助学习如何将理论驱动的界面/交互设计原则（如相似性、嵌入性、同步性）实例化为有界可运行原型的多个版本，并通过个体用户真实使用行为进行随机化现场实验来评估设计变更。
- Decision: 三项条件均满足：研究对象为个体用户对平台/应用的使用与感知；作者实际开发并部署了一个可运行的微信应用，并对界面相似性、嵌入性和同步性进行了具体软件层面的改动；开发方式为有界原型和公共平台应用，无组织、硬件或大规模数据依赖，适合小型研究团队。
- Confidence: 0.95

## That's interesting: An examination of interest theory and self‐determination in organisational cybersecurity training

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12374
- Artifact: Web-based cybersecurity training program (parameter tampering exercises)
- Individual user/task: 个体学员（IT相关专业大学生，作为非网络安全员工的替代样本）使用在线培训程序完成三个难度递进的参数篡改（parameter tampering）伦理黑客练习，并可观看教学视频、接收反馈、选择放弃。
- Design delta: 作者从零构建了完整的个体培训工件，其设计增量包括：三个基于OWASP参数篡改概念的递进练习、按先前学生完成情况排序的难度顺序、行为建模式示范视频、尝试后反馈、以及“I Give Up!”退出按钮（支持学习自主性）；整体设计旨在触发和维持情境兴趣（catch→hold）并支持自我决定动机。
- Design process: 先依据NICE框架确定知识域（Securely Provision与Protect and Defend），再参照OWASP参数篡改概念设计三个练习；难度和顺序基于以往大学作业/考试及学生完成数据；先运行N=40的试点研究，根据学员反馈和网络安全教员反馈修改测量条目并调整培训程序设计；正式研究中不显式操纵情境兴趣，而是测量自然产生的情境兴趣和动机。
- Potential coding-agent design value: 该来源方法可能有助于学习如何为一个有界、可运行的个体任务培训原型设计功能（如渐进难度、可选的示范视频、尝试后反馈、用户可退出控制），并利用兴趣与自我决定理论指导编码智能体产品的界面与交互设计。
- Decision: 满足三个条件：个体学员使用可运行的Web培训工件；作者实际构建了该工件并设计了反馈、视频、退出按钮等产品行为；PHP/MySQL原型、公开OWASP内容、大学生样本的规模对小型学术团队可行。
- Confidence: 0.95

## The Decoy Effect and Recommendation Systems

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1197
- Artifact: Custom-built online movie recommendation platform (unnamed in paper)
- Individual user/task: 个体用户（大学实验室学生或AMT参与者）在平台上先对至少20部电影评分，然后从系统给出的5部个性化或非个性化电影推荐列表中选择最想看的一部；部分条件中的推荐列表包含一个诱饵项。
- Design delta: 在推荐列表的构成和呈现上引入并操作诱饵项：诱饵与目标电影同类型、具有低预测分（个性化）或低平均评分（非个性化），被放在列表第二位使目标项形成不对称支配；同时在界面中改变推荐类型框架（个性化vs非个性化）以及是否显示预测分或平均评分。
- Design process: 设计由理论推演驱动：作者基于说服理论、个人化预期和既有诱饵效应文献提出关于个性化/非个性化情境下诱饵效应的假设，然后实现推荐平台并构造四种实验条件（个性化/非个性化 × 有无诱饵）进行受控比较；后续通过额外实验操纵诱饵质量、预测分/平均评分的展示方式和诱饵显著性来检验机制与稳健性。
- Potential coding-agent design value: 该来源可教会我们在一个可运行的、面向个体的推荐/任务支持界面中，如何通过理论驱动的单一设计变更（如选项集构成或呈现方式）构建原型并观察个人选择，这对在现有编码智能体代码库中实现和测试类似的界面级产品设计变量很有参考价值。
- Decision: 三项条件均满足：研究对象为个体用户面对推荐列表的选择行为；研究者实际构建并运行了个性化/非个性化电影推荐平台，并实质性改变了推荐集构成（加入诱饵项）；开发基于公开数据集、标准算法和有界Web原型，规模适合小型研究团队。
- Confidence: 0.95

## The Effectiveness of Social Norms in Fighting Fake News on Social Media

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1870389
- Artifact: Self-developed Facebook-like news feed with social norm messages
- Individual user/task: 个体社交媒体用户浏览一个仿Facebook的新闻信息流，并决定是否举报其认为虚假的新闻帖子。
- Design delta: 在信息流中新增并呈现两类社会规范消息：指令性规范消息作为信息流开头的提示文本，需用户确认；描述性规范消息以帖子上显示的举报人数（5/25/125/625/3,125）呈现，并随机增减至多10%来隐藏具体模式；同时简化了举报流程。实验通过2×2组合（有无指令性规范、有无描述性规范）改变了这些界面细节。
- Design process: 作者基于社会心理学文献推导假设，并依据社会规范信息应可信、应处于注意力焦点等建议设计了消息实现；通过预测试和两项在线实验迭代，Study 2进一步区分正向与负向描述性规范并调整假新闻材料，以提高实验区分度。参与者先通过教程学习举报功能，再在自然交互和虚假新闻评估阶段使用原型。
- Potential coding-agent design value: 该来源方法可帮助我们学习如何在小型可运行原型中设计并检验面向个体的界面提示或社会规范类信息（例如行为期望提示或社区举报计数）对用户行为的影响，从而为编码智能体增加类似的行为塑造或反馈功能提供设计参考。
- Decision: 三个条件均满足：研究对象是个体用户对虚假新闻的举报行为；作者构建并实际运行了一个可交互的仿Facebook新闻信息流原型，并实质性地修改了其中的社会规范消息和举报功能；该原型开发与在线实验的规模适合小型学术团队。
- Confidence: 0.95

## Website Localization Strategies to Promote Global E-Commerce: The Moderating Role of Individualism and Collectivism

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2022/15542
- Artifact: Fictitious localized snack company websites (8 experimental versions for the U.S. and 8 for China; e.g., geoffchina1.icoc.vc, wl1.geoffusa.com)
- Individual user/task: 美国和中国当地的消费者（被试）单独浏览一个虚构外国零食公司的网站主页，评估网站本地化感知、口碑意向和持续使用意向。
- Design delta: 在不同实验版本中系统地加入或去除三类本地化设计线索：本地文化符号（如中国灯笼/美国象征）、公司相对竞争者的差异说明、本地奖项/排名展示；其余页面元素保持一致，形成8种组合。
- Design process: 先以消费者-公司认同理论推导三种本地化策略；再分析美国财富1000强公司中文网站和中国财富500强公司英文网站，由两名双语博士生归纳出12种具体策略；随后访谈20名用户选择最有代表性的策略（本地符号、产品/服务差异、本地奖项）；选择零食作为中性产品构建8个版本的虚构公司主页；通过8名HCI/电商专家预测试修订问卷和网站。
- Potential coding-agent design value: 该方法可启发我们如何从用户认同相关的理论中推导出可操作的界面或交互特征，并以有界网页原型的方式快速实现多种产品变体，通过访谈和专家预测试迭代选择特征，用于编码助手类工具的产品设计。
- Decision: 三项条件均满足：研究对象是个人消费者浏览网站；作者实际构建并部署了可运行的虚构公司网站主页，并通过添加或移除三类本地化设计元素实现材料化修改；开发范围仅为有界网页原型和常规在线实验，小型团队可完成。
- Confidence: 0.95

## Designing Effective Mobile Health Apps: Does Combining Behavior Change Techniques Really Create Synergies?

- Year/journal: 2021 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2021.1912936
- Artifact: WORKLAX
- Individual user/task: 个体用户（以大学生为样本的压力人群）使用移动App进行渐进式肌肉放松训练以缓解压力；任务包括打开App、完成3分钟放松训练并阅读推送通知。
- Design delta: 控制原型只有基线功能；社会向上比较原型加入提示比较维度与负向绩效差距的推送消息，以及显示“其他用户平均使用频率高于本人”的匿名性能可见页面（数据被自动操纵以确保只能向上比较）；保护动机原型加入含威胁严重性/易感性和应对效能/自我效能/反应成本的恐惧诉求推送通知；组合原型同时具有社会比较和保护动机两类设计特征。
- Design process: 采用解释性设计理论化（explanatory design theorizing）：选择保护动机和社会向上比较作为内核理论，将理论变量实例化为设计特征；结合现有压力管理mHealth基线元素的内容分析确定基线功能；开发四个原型，并用30名学生的观察与访谈迭代和验证设计；随后通过5周田野实验比较四组使用行为，并用36名欧洲学生的定性访谈进一步佐证交互效应。
- Potential coding-agent design value: 该源方法可帮助我们学习如何在有界原型中把行为改变理论具体化为个人用户可见的功能变体（如提醒、社会比较反馈、说服性消息），并通过小规模田野实验和定性访谈检验这些面向个体的功能设计及其交互影响。
- Decision: 三个条件均满足：研究焦点是单个用户使用移动App进行压力缓解；作者实际构建并运行了四个可运行的个体面向mHealth原型，并物质性地修改了推送通知和性能可见页等设计特征；开发范围是有界原型加短期学生实验，不依赖被排除的大型组织、临床或基础设施资源。
- Confidence: 0.93

## Improving intention to back projects with effective designs of progress presentation in crowdfunding campaign sites

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113573
- Artifact: Simulated crowdfunding campaign webpage with progress bar design variants
- Individual user/task: 个人潜在支持者（大学生被试）浏览模拟的众筹项目网页，评估项目并表达支持（back）意向。
- Design delta: 对进度条这一用户可见组件的具体设计变更：运动属性（静态/动态）、颜色（蓝/红）、以及进度条周围额外进度信息的数量；同时考察了项目类型（享乐型/功利型）与颜色设计的匹配效果。
- Design process: 设计需求与特征先由理论（S-O-R框架、运动效应理论、视觉搜索理论、颜色心理学、信息诊断性文献）推导出假设，再结合商业众筹网站中常用的进度条设计（蓝/红两色、常见额外信息类型）确定具体操作水平；研究1检验运动与颜色，研究2进一步检验额外信息与颜色，并通过操纵检验确认被试正确识别了设计变体。
- Potential coding-agent design value: 该方法可帮助我们学习如何在一个有界的可运行原型中，对用户可见的进度/状态呈现进行小而理论驱动的设计变更（如运动、颜色、信息丰富度），并通过个体用户测试来观察其对感知与使用意向的影响，从而为编码智能体的进度反馈和状态展示设计提供参考。
- Decision: 三项条件均满足：研究对象是个体潜在支持者浏览众筹网页；作者实际构建并操作了可运行的模拟众筹网页这一面向个体的软件原型；开发范围是有界网页原型和大学生被试实验，小型学术团队可承担。
- Confidence: 0.93

## Privacy Concerns and Data Donations: Do Societal Benefits Matter?

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2024/16853
- Artifact: DataDonors (app mockup) and Fight COVID-19 (app simulation)
- Individual user/task: 个体用户（研究参与者/潜在数据捐赠者）通过移动应用决定是否捐赠个人数据（人口统计、医疗、行为数据）以支持医学研究或COVID-19研究。
- Design delta: 设计变体包括：(1) 是否提供细粒度隐私控制/设置（如控制访问者、撤销捐赠）；(2) 实验1在应用首页使用癌症/阿兹海默患者图片并搭配引导换位思考的文本以诱发共情（隐式社会收益），对照为海洋图片；(3) 实验2在应用内明确告知数据捐赠的社会收益或个人收益（显式社会收益 vs 个人收益基准）。
- Design process: 作者以隐私计算模型为主要理论视角，将理论构念操作化为应用界面的具体设计元素：隐私控制被操作为是否提供可配置的隐私设置；隐式社会收益被操作为主页共情图片与视角采择文本；显式社会收益被操作为应用内明确告知捐赠的社会或个人收益。随后通过两个2×2在线随机实验（MTurk招募被试）评估这些设计变体对实际数据捐赠行为的影响。设计过程为理论驱动的界面变体设计，而非基于用户研究的迭代式设计。
- Potential coding-agent design value: 该来源的方法可帮助我们学习如何为个体用户设计有界的交互式产品原型/模拟，并通过理论驱动的界面变体（如控制设置、提示信息、情感化内容）来检验产品行为对用户决策的影响，适用于在编码代理产品上实现可操作的界面/交互修改并开展小规模用户实验。
- Decision: 三项条件均满足：研究焦点是个体捐赠者的隐私决策；作者实际构建了两个可浏览/可交互的数据捐赠应用原型（尤其是Fight COVID-19应用模拟），并实质性修改了界面特征（隐私控制、共情诱导、社会收益信息）；开发与评估规模小，依赖在线实验和MTurk样本，不涉及组织转型、临床基础设施或大型数据工程。
- Confidence: 0.93

## Will Humans-in-the-Loop Become Borgs? Merits and Pitfalls of Working with AI

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16553
- Artifact: 
- Individual user/task: 单个实验参与者（MTurk 工人）对每张焦点图像从 10 个图像类别中选择一个最匹配类别；部分参与者在选择前收到 AI 建议、AI 确定性提示或个性化 AI 建议。
- Design delta: 材料性的设计差异包括：(1) 是否显示 AI 建议；(2) 是否将 AI 确定性以与人类自信度相同的四点量表呈现；(3) 是否采用个性化建议规则——当 AI 确定性低于个体临界比 r_h 时不显示建议。这些差异被实际实例化在不同实验处理中并影响用户交互。
- Design process: 设计需求与特征并非来自用户共创，而是先构建离散选择分析模型推导假设，再据此在实验系统中实例化三种建议模式（普通建议、附带确定性、个性化建议）；三个实验按预注册方案逐步检验和迭代，探讨 AI 建议对准确率和独特人类知识的影响。
- Potential coding-agent design value: 该来源方法可帮助小型团队学习如何在有界交互式决策支持原型中设计并测试具体的建议呈现与个性化特征（例如显示 AI 确定性、按个体阈值抑制低置信建议），并用少量个体用户完成行为验证。
- Decision: 三项条件均满足：研究对象是单个用户使用 AI 建议进行图像分类决策；作者实际构建并修改了可运行的建议界面（普通建议、确定性提示、个性化建议）；方法依赖预训练模型、公开数据和众包被试，开发范围适合小型学术团队。
- Confidence: 0.93

## “My Name is Alexa. What’s Your Name?” The Impact of Reciprocal Self-Disclosure on Post-Interaction Trust in Conversational Agents

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00839
- Artifact: Amanda
- Individual user/task: 单个个体用户（MTurk参与者）通过文本或语音与名为Amanda的会话代理进行一对一对话；任务是回答代理提出的12个逐步更私密的问题（如年龄、性别、业余爱好、失望、愧疚等），并随后完成关于拟人化和信任的问卷。
- Design delta: 核心设计差异是CA的互惠自我表露行为：处理条件下，CA在每轮提问前先表露自身逐步增高的私密信息（如年龄、性别、家乡、失望、愧疚等）；控制条件下，CA仅输出等长的程序性非表露文本（如“下一个问题是关于……”）。同时实现了语音端的自然轮替（自动检测语音结束+两秒宽限）、噪声消除、音量重置等交互特征，以支持流畅的对话体验。
- Design process: 研究者基于Moon（2000）的脚本化互惠自我表露方法设计对话流程，并针对CA情境调整了问题与表露内容（12题）；通过五次试点研究（N=80、100、30、30、50）迭代改进CA的技术设计（如语音识别、断句检测、Android兼容性）和操纵有效性，然后进行两个随机后测对照实验。
- Potential coding-agent design value: 该方法可为小型团队如何构建有界的会话代理原型（如编写脚本化对话流程、设计代理自我表露行为、实现自然语音轮替）并通过试点迭代和在线随机实验来评估个体用户对代理拟人化与信任感知提供可借鉴的模板。
- Decision: 三个条件均满足：研究聚焦于单个用户与CA的交互（个体层面）；研究者亲自动手构建了两个可运行的文本和语音会话代理，并实质性地改变了代理的自我表露行为和对话流程（可运行个体面向软件工件）；开发规模限于有界原型、标准API和MTurk样本，无需企业合作或大型基础设施，适合小型学术团队。
- Confidence: 0.93

## Delays in Information Presentation Lead to Brain State Switching, Which Degrades User Performance, and There May Not Be Much We Can Do about It

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17680
- Artifact: 
- Individual user/task: 单个参与者执行go/no-go警觉任务：屏幕显示数字1-9，参与者仅在数字为3时按空格键；系统在试次间插入短延迟（0.1-1秒）或长延迟（8-10秒），并在长延迟期间展示不同的干预界面。
- Design delta: 四种延迟期间的用户界面干预：(1) 同时显示累积绩效统计；(2) 分阶段逐条显示同一绩效统计；(3) 在'Loading…'下方显示倒计时器；(4) 在真实试次前插入不计分的虚拟任务试次。与仅显示'Loading…'的短/长延迟基线相比，这些改变了延迟期间的反馈内容、信息呈现节奏和任务预热流程。
- Design process: 干预设计源于Study 1的fMRI结果：长延迟引发脑状态切换，因此设计目标是在延迟期间维持或快速恢复任务相关脑状态；据此设计四种干预（任务相关的绩效反馈、分步反馈、倒计时提醒、主动虚拟任务），并通过667名Prolific被试的组间行为实验比较其速度与准确率。
- Potential coding-agent design value: 该来源展示了一种在系统延迟/等待期间设计并测试用户界面干预（如进度反馈、倒计时、预热任务）的小规模原型方法，可启发编码智能体在长延迟或后台处理时如何设计加载态、再参与提示与任务预热功能。
- Decision: 三项条件均满足：研究对象是单个用户执行警觉/评分任务；作者实际构建并修改了可运行的任务软件，实现了四种延迟期界面干预；开发与招募规模（简单实验程序+Prolific样本）对小型团队可行。Study 1的fMRI仅提供机制依据，不构成软件构件开发的必要依赖。
- Confidence: 0.92

## Designing Attentive Information Dashboards

- Year/journal: 2022 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00732
- Artifact: Attentive Information Dashboard with Individualized Visual Attention Feedback (VAF)
- Individual user/task: 单个决策者（实验中为大学生被试）在信息仪表盘上执行数据探索任务，通过浏览和记忆销售报告数据来准备与主管的会议。
- Design delta: 核心改动是新增个性化 VAF 功能：根据用户自己的实时眼动数据计算每个图表的注视时长，在首次探索结束后以条目形式反馈给用户，提示其注意分配情况；对照组仅收到一般文本提示。
- Design process: 采用 Kuechler & Vaishnavi (2012) 的 DSR 过程，分为三个设计周期；本文聚焦第二周期。第一周期通过文献综述和眼动预实验识别问题并形成初始元需求；第二周期细化元需求（MR1-MR4）与两条设计原则（DP1-DP2），将原则实例化为可运行原型，并在实验室实验中比较个性化 VAF 与一般 VAF。
- Potential coding-agent design value: 该来源方法可借鉴到编码代理的产品设计中：构建一个有界的可运行原型，利用用户自身的交互或注视数据生成个性化反馈，并通过小型受控实验检验该反馈对后续行为的影响。
- Decision: 三个条件均满足：研究对象是单个用户在仪表盘上的注意资源分配；作者实例化了一个可运行的、面向个体的仪表盘软件并提供个性化视觉注意力反馈；开发依赖低成本商用眼动仪、SDK 和有界原型与 92 名学生实验，规模适合小型学术团队。
- Confidence: 0.92

## On the Same Page? What Users Benefit from a Desktop View on Mobile Devices

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1140
- Artifact: 
- Individual user/task: 个体用户（大学生参与者）使用该网站完成在线酒店预订的多属性选择任务，在11个备选酒店中选出最符合其偏好的酒店。
- Design delta: 信息架构层面的具体设计变更：桌面IA在概览页单页呈现11个备选×8个属性的完整信息；移动IA在概览页仅呈现3个属性，其余属性需点击进入各详情页获取；实验2进一步操纵移动IA概览页所呈现的三个属性是与用户偏好最一致（一致条件）还是最不一致（不一致条件）的属性。
- Design process: 设计参数通过两轮初步研究确定：先对36名受访者调查16个酒店属性的重要性，选出最重要的8个属性；再从Booking.com搜索结果中抽样并平均生成22个备选，分成两组任务；实验1移动IA概览页展示3个属性是基于对11个流行酒店预订网站的探索性分析。实验2根据参与者事先给出的属性权重，将移动IA概览页的三个属性设为最不重要或最重要属性，构造不一致/一致的移动IA。
- Potential coding-agent design value: 该来源可为编码智能体产品设计提供一个方法示例：用有界可运行原型系统化地变体化信息架构/信息呈现方式（如概览与详情分层、呈现内容与用户偏好的对齐），并观察不同设计变体如何影响用户的决策努力与决策准确性。
- Decision: 三项条件均通过：研究对象为个体用户在可运行网站上单独完成的酒店选择任务；作者专门开发了可运行的实验网站，并实际变更了信息架构（桌面单页 vs 移动分页；一致/不一致移动IA）；开发方式为简单有界原型加适度学生样本，无组织、硬件或大规模数据依赖。
- Confidence: 0.92

## Prejudiced against the Machine? Implicit Associations and the Transience of Algorithm Aversion

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17961
- Artifact: AI-based weight estimation advisor (fictitious, unnamed in paper)
- Individual user/task: 个体用户逐张估计图片中人物体重，接收AI给出的体重估计作为建议，并可随后修正自己的估计；研究测量用户对AI建议的采纳程度（weight on advice）。
- Design delta: 关键设计差异包括：选择建议型、不可解释、客观任务的AI；设定AI输出偏差为1-5%并平衡方向；在两个区块之间向用户揭示隐含的性能信息以研究反馈对建议采纳的影响；开发了以“我”和“专家”为参照点的两个AI可信度IAT。
- Design process: 根据理论确定所研究AI的类型边界（建议角色、不可解释、客观任务）；参照Logg et al. (2019)的实验范式搭建虚构AI；开发两个IAT时遵循Serenko和Turel (2020)的步骤，咨询五位领域专家并据此细化词语；通过67人的试点研究检验IAT、量表、体重估计任务和整体范式；全部设计与分析计划预注册于OSF。
- Potential coding-agent design value: 该来源方法可帮助我们学习如何构建一个有边界、可模拟且输出行为可控的建议型AI原型（含性能反馈机制），用于在个体层面研究用户对智能体建议的初始依赖及其随反馈的变化，为编码代理产品的交互与反馈设计实验提供参照。
- Decision: 三项条件均满足：研究聚焦个体用户对AI建议的采纳（个体层面）；作者实际构建并运行了一个虚构的AI建议系统原型，并可控地改变了AI输出与性能反馈（可运行的个体面向软件原型）；实现依赖Qualtrics、iatgen和公开图像数据，无组织合作、临床、硬件或大规模数据等不可行资源（小团队可行）。
- Confidence: 0.92

## Roles of Feedback and Phishing Characteristics in Antiphishing Training Performance: Perspectives of Goal Setting and Skill Acquisition

- Year/journal: 2024 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00854
- Artifact: Unnamed Qualtrics-based phishing quiz and feedback system
- Individual user/task: 美国在线样本中的个体参与者独立阅读邮件并判断其是否为钓鱼邮件，可选择“钓鱼”“合法”或“跳过/不知道”，并在初步测试后接收不同类型的反馈，然后完成主测试中的邮件判断任务。
- Design delta: 实质性修改的面向用户的设计元素包括：(1) 反馈类型：示例型反馈（用真实钓鱼邮件展示如何识别假链接）对比正念型反馈（抽象提醒和反思类建议）；(2) 反馈数量：低量（只讲一个假链接检测技巧）对比高量（同时说明假链接、假域名、通用称呼、紧迫语气等多种线索）；(3) 钓鱼线索显著性：低（仅假链接）对比高（假链接加可疑域名以及紧迫语气/语法错误/通用称呼之一）；(4) 邮件类型：带链接邮件对比无链接邮件。
- Design process: 需求与特征来源于理论驱动：基于目标设定理论选取反馈特征、任务复杂性和自我效能；基于技能获得理论论证示例型反馈相对于抽象/正念反馈的优势；反馈内容改编自既有正念训练材料（Jensen et al., 2017; Nguyen et al., 2021a），示例型反馈参考了 Google 等在线钓鱼检测测试的做法；通过预测试/操控检验（如反馈所需思考程度、反馈中技巧数量感知）确认设计差异被用户感知，再用于正式实验。
- Potential coding-agent design value: 该来源方法可帮助学习如何在一个面向个体的任务/训练型软件原型中落地并变化反馈的内容、数量与具体性（例如基于示例的反馈与抽象指导的对比），并通过可运行的 Web 原型观察用户的任务表现与决策回避行为。
- Decision: 三项条件均满足：研究对象是个体参与者独立完成钓鱼邮件判断任务；作者实际构建并实质性修改了一个可运行的、面向个体的交互式测验与反馈原型（Qualtrics 网页测验，含可悬停链接、反馈内容与数量变化）；该原型为有界 Web 原型，不依赖组织、硬件或长期部署，小研究团队可复现类似设计。
- Confidence: 0.92

## Skipping class: improving human-driven data exploration and querying through instances

- Year/journal: 2022 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1869507
- Artifact: Tableau instance-based representation (instance-based condition)
- Individual user/task: 单独使用系统的内容消费者（如业务分析人员、学生、记者等非数据库专家），对人力资源数据集进行开放式数据探索和模式发现（实验一），以及在给定表示上口头描述数据检索/查询步骤（实验二）。
- Design delta: 将 Tableau 中数据的组织方式从预定义类（schema-first）改为无分类的实例/属性列表表示，允许用户按需自定义分组；两组除信息组织方式外，Tableau 功能完全相同。
- Design process: 基于 Parsons 和 Wand 的实例基础数据模型理论，将人力资源领域建模为节点+属性的图模型，并把同一数据集的属性以字母排序的平铺列表呈现，从而去除预定义分类；对实验材料进行试点测试（14人）后修改任务措辞；由两位建模专家检查实验材料；用户培训采用 Tableau 官方教程编辑的20分钟视频。
- Potential coding-agent design value: 该来源方法可以为小型团队提供一种在现有工具内改变用户面对的信息组织方式（如将任务上下文以无预设结构的实例/属性列表呈现，而非预定义分类/模板），并通过有界的实验室任务比较个体用户探索与查询表现的设计与评估模板。
- Decision: 三个条件均满足：研究对象是单独使用数据表示工具的内容消费者（个体层面）；实验一在 Tableau 中实际配置了可运行的个体面向表示，并实质性改变了数据组织方式（类→实例/属性列表）；配置现有工具+公开数据集+学生样本的实验室方法对小型团队可行。实验二的非交互静态材料不影响总体判断。
- Confidence: 0.92

## Why Do Data Analysts Take IT-Mediated Shortcuts? An Ego-Depletion Perspective

- Year/journal: 2022 / Journal of Management Information Systems
- DOI: 10.1080/07421222.2022.2063558
- Artifact: Custom analytics dashboard (simple and complex versions)
- Individual user/task: 个体数据分析师使用仪表板为一家虚构服装公司选择最佳产品、国家和渠道以最大化利润；他们被要求逐一点击并展开所有图表后再做决策。
- Design delta: 核心设计差异是仪表板复杂性：通过增加数据种类（结构化和非结构化）和动态性（每分钟更新）来操纵复杂性；同时明确指示用户必须逐一检查全部图表，并将跳过图表数作为客观行为记录。
- Design process: 复杂性操纵的设计依据大数据特征（多样性、速度）和认知复杂度理论；通过一项50人试点研究微调仪表板；另用18位数据分析师的改良德尔菲研究选择道德完整性和目标类型作为边界条件，再据此设计实验条件。
- Potential coding-agent design value: 该来源方法可帮助我们学习如何在编码代理原型中构建有边界的交互变体（如任务复杂度或强制步骤），并用系统日志客观测量用户是否跳过关键步骤或走捷径。
- Decision: 三个条件均满足：研究对象是单个数据分析师使用仪表板完成任务；作者实际构建并物质性修改了两个可运行的仪表板版本并记录交互行为；该原型构建与实验属于有边界、无组织依赖的常规开发，适合小型团队。
- Confidence: 0.92

## <scp>Context‐aware</scp> user profiles to improve media synchronicity for individuals with severe motor disabilities

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12337
- Artifact: AAC system prototype with context-aware user profiles
- Individual user/task: 患有严重运动障碍的个体（评估时使用非残疾大学生作为替代用户）通过扫描界面选择身体部位、症状和短语，向照护者或访客表达医疗与舒适需求，如“耳朵疼”“调整头部至中间”“我累了”。
- Design delta: 在AAC系统中加入情境感知用户画像：根据用户偏好、时间、地点和访客档案缩小或调整可选词语、短语和符号集，减少选择次数；同时引入医疗/舒适本体和身体图式符号集，取代逐字母拼写。
- Design process: 采用Peffers等人(2007)的设计科学研究方法（DSRM）和Strategy 2路径，通过与严重运动障碍个体、照护者和家人的互动及转录分析识别问题，形成5条设计需求；在设计/开发/演示活动间迭代；先进行人工论证，再构建医疗舒适本体和可运行原型，并用10名大学生进行自然主义评估，最后基于评估结果提炼设计原则。
- Potential coding-agent design value: 该研究的DSRM流程和“通过情境化用户画像缩小选项空间以加速个体产出”的设计思路，可启发为编码智能体设计情境感知的快捷选项、短语或意图推荐、可预演确认机制等有界功能原型。
- Decision: 三个条件均满足：软件面向单个AAC用户与访客的沟通，属个体层面；作者实际构建了可运行的AAC系统原型并让10名被试使用，包含有/无情境感知用户画像两个版本；原型开发、本体构建和大学生评估规模小，不依赖企业部署、专用硬件或大规模数据，符合小型研究团队可行性。
- Confidence: 0.9

## A social mechanism for task-oriented crowdsourcing recommendations

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2020.113449
- Artifact: Social Crowdsourcing Task (SCT) recommendation mechanism/system
- Individual user/task: 个体请求者使用 Web 系统提交众包任务并获取合适的贡献者推荐列表；个体贡献者收到任务邀请并决定是否接受，同时填写反馈问卷。
- Design delta: 核心设计增量是社交众包推荐机制：综合贡献者偏好（兴趣、能力、动机）、历史表现（浏览、选择、完成、被接受）和社交影响（社交关联与社交亲近度）计算适合度；使用 AHP 确定三类准则权重；推荐列表包含姓名、照片、社交关系、偏好、历史表现和 Facebook 链接等详细信息。
- Design process: 基于文献回顾提出三类推荐因素（贡献者偏好、贡献者历史、社交影响）；参照 Amazon Mechanical Turk 和 Taskcn 构建任务类型树；使用 Facebook 社交活动数据推断用户兴趣、能力和动机；通过 AHP 问卷确定不同准则的权重，并设置专业/非专业任务的默认权重；随后进行现场实验并与随机、内容、协同过滤和一般平台推荐模型比较。
- Potential coding-agent design value: 该来源的方法可帮助我们学习如何在编码智能体产品中构建一个有界的推荐/匹配原型：利用用户可观察的历史行为、偏好信号和社交/关系信号，设计个性化的建议或邀请功能，并通过小型用户试验验证设计。
- Decision: 三个条件均满足：研究焦点是个体请求者和贡献者使用推荐系统；作者实际构建并运行了一个 Web 推荐原型，而不仅是算法或模型；实现依赖常规 Web 开发、Facebook 数据和约 138 名志愿者，无排除性的组织、硬件或超大规模数据需求。
- Confidence: 0.9

## An assisted approach to business process redesign

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113749
- Artifact: ABPR prototype (Assisted Business Process Redesign prototype)
- Individual user/task: 单个流程设计师、流程经理或BPM顾问使用该桌面原型，以改进一个业务流程模型：选择性能目标（如时间、成本、灵活性、质量），获取基于重设计模式的重设计建议，手动或半自动修改流程模型，并通过仿真评估备选方案。任务聚焦于辅助个人用户完成业务流程重设计的逐步工作。
- Design delta: 在建模器中加入了引导式重设计工作流：基于四种自动化水平生成并排序重设计建议；实现了多个具体模式处理器（triage、activity automation为AL3，parallelism、extra resources为AL4）；通过A*启发式对建议多样化；扩展BPMN元模型以保存仿真配置和ABPR标注；模型linter识别配置问题；通过向导收集用户领域知识（如triage的拆分标准）并将其写入模型。
- Design process: 遵循设计科学研究（DSR）和参考架构开发方法：从文献识别问题并定义五个设计目标（DO1–DO5）；基于参考流程和现有BPR工具设计ABPR概念与参考架构；构建原型；通过两轮专家访谈（8人）、两个人工场景案例和KUKA真实案例进行迭代评估，并将反馈纳入原型（如扩展BPMN元素、增加tooltips、导入功能、改善仿真结果可视化）。
- Potential coding-agent design value: 该来源的“在现有建模器中嵌入引导式建议、分级自动化、模式处理器和用户领域知识收集向导”的软件设计方式，可启发我们在编码智能体产品中实现分级自动化建议、用户确认向导和可解释的修改操作。
- Decision: 满足三个条件：ABPR原型面向单个流程设计者/管理者，提供可运行的交互式桌面工具；该原型基于Camunda Modeler实现了实质性软件修改（建议生成、模式应用、仿真集成）；开发范围限于开源模型器的扩展和有限模式实现，无大规模数据或组织依赖，适合小型学术团队。故 target_match=true。
- Confidence: 0.9

## An interface between natural language and abstract argumentation frameworks for real-time debate analysis

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113694
- Artifact: WebAIPA (AIPA engine and AipaForum)
- Individual user/task: 参与辩论的个人用户（非论证专家）通过 WebAIPA/AipaForum 提交 Statement 或 Conclusion，实时查看论证图、辩论状态和论点间冲突，以构建自己的论证并理解他人的论证。
- Design delta: 为 Dung AAF 设计了 ADM 论证语义（Conclusion/StatementFor/StatementAgainst），定义了从自然语言论证到攻击图的两种翻译规则（Support 和 Optimistic），三种辩论状态判定（Accepted/Conflictual/Rejected），inFavor 函数以及结果解释规则，并在 WebAIPA 中实时可视化这些状态。
- Design process: 设计过程从文献综述出发，识别出参与式辩论支持的五项需求（论证语义、AAF 推理、翻译规则、实时计算、可视化），据此构建 ADM 模型并实现于 AIPA/WebAIPA；通过两个应用案例（8人实时辩论和事后分析676条论坛消息）演示工具，并根据反馈指出局限和未来改进方向。
- Potential coding-agent design value: 该文展示了一种小团队如何围绕一个理论框架定义论证语义、设计从自然语言输入到结构化表示的翻译规则，并以实时推理和可视化解释作为产品交互核心；这种“领域模型→翻译规则→实时推理→可视化解释”的界面设计方式可为编码代理的输入结构化、推理结果呈现和用户可解释性功能设计提供参照。
- Decision: 三个条件均满足：工具面向辩论中的个体参与者使用；实际构建并运行了 WebAIPA/AipaForum 交互式 Web 原型，能实时添加论点并可视化推理结果；开发依赖现成 AAF 引擎和常规 Web 技术，无组织级或重型资源依赖。
- Confidence: 0.9

## Design principles for learning analytics information systems in higher education

- Year/journal: 2021 / European Journal of Information Systems
- DOI: 10.1080/0960085x.2020.1816144
- Artifact: Learning Analytics Information System (LAIS) prototype based on Open edX
- Individual user/task: 授课教师作为主要个体用户，使用LAIS原型监控学生与课堂录像（LTR）的互动情况，识别学生跳过或重播的视频片段，以调整教学内容并进行及时教学干预；学生作为数据主体通过视频播放器产生交互事件。
- Design delta: 在视频学习平台之上实现了学习分析功能：视频事件追踪与分析管道、每周邮件报告、可视化仪表盘、灵活粒度报告、SSO登录集成，以及信息可用性和匿名保护等设计特征的迭代修改。
- Design process: 通过文献和干预理论构思初始设计原则；采用操作原型法（operational prototyping）开发LAIS原型；经过两轮演示与评估（试点研究、四个课程大规模使用），结合服务器日志、学生问卷和教师访谈修订设计原则。设计原则从最初的3条修订为最终4条（DP1-DP4）。
- Potential coding-agent design value: 该研究所展示的从内核理论推导设计原则、以操作原型法快速实现个体面向的分析/反馈工具并用真实用户反馈迭代设计的过程，可为设计编码助手的反馈、进度可视化或干预提醒等产品特性提供方法参考。
- Decision: 三个条件均满足：主要用户为个体教师（和学生）；作者基于Open edX构建并实质改进了可运行的个体面向LAIS原型（报告、仪表盘、SSO等）；开发方式为有界原型+操作原型法，不依赖被排除的重型资源。
- Confidence: 0.9

## Expl(AI)ned: The Impact of Explainable Artificial Intelligence on Users’ Information Processing

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2023.1199
- Artifact: oTree-based AI decision-support experiment (investment game and apartment price estimation)
- Individual user/task: Study 1: 普通参与者（laypeople）在抽象投资博弈中决定是否投资；Study 2: 房地产行业专家估计德国公寓的挂牌价格。
- Design delta: 核心设计差异是在不透明AI预测的基础上增加基于特征的可解释性说明：Study 1以彩色条形图展示LIME值，Study 2以数值形式展示SHAP值；同时通过无辅助/仅预测/预测+解释三种条件操纵用户可见的解释呈现，并用分阶段设计（Stage I–III/IV）测量信息处理和信念变化。
- Design process: 设计源于研究问题而非传统设计科学迭代：选择最流行的特征归因XAI方法（LIME/SHAP），用前期田野数据和爬取的真实房源数据训练固定AI模型，再在oTree中构建各阶段界面；通过对照条件（NoAid/AI/XAI）操纵解释呈现，并用投资决策、价格估计和信念滑杆测量认知变化。Study 2的特征选择部分基于技术原因和行业伙伴输入。
- Potential coding-agent design value: 该来源可帮助学习如何在一个可运行的个体面向决策支持原型中设计并操纵“解释”这一用户可见特征（例如在智能体预测旁显示特征归因），并通过分阶段任务测量用户信息处理与心智模型的变化。
- Decision: 三个条件均满足：研究对象是使用AI预测/解释的个体用户；作者实际构建了可运行的oTree交互原型并实质性地改变了用户界面中的解释呈现；开发方式为小型学术团队可行的在线实验系统。
- Confidence: 0.9

## It's not just about accuracy: An investigation of the human factors in users' reliance on anti-phishing tools

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113846
- Artifact: Experimental anti-phishing tool / mock Gmail-style email inbox
- Individual user/task: 个体用户（大学生被试）在模拟 Gmail 收件箱中识别钓鱼邮件，并借助反钓鱼工具的预测标记（红色警告、绿色对勾）完成判断。
- Design delta: 对邮件标记功能的实例化与改动：操纵被标记邮件的数量（频率）和预测正确率（准确性），在 Study 2 中增加一个解释工具决策方式的信息屏以提高透明度。
- Design process: 设计需求来自文献推导的研究假设（H1–H9），据此直接实例化工具特征：通过改变标记数量、标记正确率以及是否提供解释性信息屏来操作准确性、频率和透明度；没有进行用户中心设计迭代或正式的软件设计过程。
- Potential coding-agent design value: 该研究展示了一种小型团队可复现的做法：在现有问卷/原型环境中快速构建一个带可操作预测标记的个体任务工具，并通过操纵准确性、频率和透明性等界面行为特征来研究用户对智能助手的依赖，可迁移到对编码智能体产品的交互特征设计。
- Decision: 三项条件均满足：研究对象为个体用户与工具预测的交互；作者实际构建并运行了一个 JavaScript/Gmail 风格的模拟邮箱工具，并改变了标记准确性、频率及透明度信息屏；开发规模限于 Qualtrics 问卷中的有界原型和在校学生样本，小型团队可完成。
- Confidence: 0.9

## Long-term multi-criteria improvement planning

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113606
- Artifact: MCDMBM
- Individual user/task: 单个决策者（如大学战略规划人员）使用该软件输入多准则评价数据与参数，生成并比较针对某个实体（如一所大学）的长期多准则改进路径。
- Design delta: 核心设计增量是将改进路径建模为图中的路径，并为边引入三类指标：瓶颈风险、相对上一步的运营变更、排名/等级提升；通过可调惩罚权重将三者聚合成单一目标，从而生成并比较多组高效改进方案；每一步只改进一个准则以降低变革阻力。
- Design process: 作者先提出一个四步理论框架：构建偏好模型M；为每个准则找出可借鉴的观察备选集合Λ_k；按相似性规则选择中间基准β_k；按备选数量最多原则选择避免瓶颈的改进方向。随后构造有向元图，用Dijkstra算法在多个惩罚权重组合下生成高效改进路径，并与决策者一起分析路径的稳健性、现实性和合意性。案例中使用ARWU20公开数据，用二分法构造边际价值函数，并使用54组权重生成路径。
- Potential coding-agent design value: 该来源的方法可启发我们设计编码助手中的一个有界决策支持模块：让单个开发者或规划者基于多个代码质量准则生成并比较分步改进路径，并通过对运营变更和瓶颈风险的惩罚权重来调控方案的激进程度。
- Decision: 三个条件均满足：软件面向单个决策者使用（个体层面）；作者实际构建并公开了一个可运行、可交互的决策支持软件（MCDMBM）并包含界面可视化；该开发仅需公开数据、标准算法和单个Python/可执行文件，适合小规模学术团队。
- Confidence: 0.9

## Peer Effects in Competitive Environments: Field Experiments on Information Provision and Interventions

- Year/journal: 2021 / MIS Quarterly
- DOI: 10.25300/misq/2021/16085
- Artifact: Peer information intervention add-on for Canvas LMS
- Individual user/task: 本科生在商务分析课程中独立完成个人作业；软件通过Canvas和邮件向学生发送包含描述性同伴信息的提醒消息，目的是减少拖延并提高作业成绩。
- Design delta: 核心产品改动是在提醒消息中加入了实时描述性同伴信息（例如“你所在班级/小组中已有X%的同学开始做这项作业”）；研究III还通过课程评分政策操纵了竞争环境（排名制vs非排名制），研究IV操纵了消息中披露的同伴行为流行率（21%、41%、61%）。
- Design process: 采用构建-评估（build–evaluate）思路：设计需求来自拖延行为、社会规范和社会比较文献；将同伴信息通知功能实例化为Canvas插件；随后通过多个随机现场实验评估干预效果，并根据性别、性别构成、过去行为等调节因素分析异质性。
- Potential coding-agent design value: 该研究可启发如何在现有编码助手或IDE类产品中构建轻量级“同伴行为信息”通知或提示功能（例如显示其他开发者/学习者已开始某任务的百分比），并通过小规模现场实验观察其对个体任务启动时间和产品使用行为的影响。
- Decision: 三个条件均满足：聚焦对象是单个学生使用LMS并受消息影响的个人行为；作者实际构建并部署了一个可运行的Canvas插件，向个体学生发送实时同伴信息干预消息，属于对现有产品功能的实质性修改；开发范围是有限的LMS附加组件，不依赖企业级转型、专有硬件或大规模数据创建，小型学术团队可复制类似开发。
- Confidence: 0.9

## Proper and improper uses of MCDA methods in energy systems analysis

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2022.113848
- Artifact: MCDA-MSS (MCDA Methods Selection Software)
- Individual user/task: 决策分析师或决策者单独使用该系统，通过回答关于问题类型、偏好模型、偏好信息与偏好关系利用方式的特征问题，获得最适合其决策问题的 MCDA 方法推荐。
- Design delta: 将四条初始指南（权重与MCDA方法匹配、决策推荐类型选择、数值不总是定量、数值不一定是比率）和两条新增指南（并非所有MCDA方法采用相同步骤、准则间交互可细化偏好模型）集成到软件的规则库中；更新了PAIRS和MACBETH等方法的功能描述（如区间绩效评估、分层和定性准则处理）。
- Design process: 作者首先基于MCDA方法文献和MCDA过程分类法，在已有软件中制定并集成方法选择指南；然后用156个特征逐条描述56个已发表案例研究，运行MCDA-MSS检查所用方法与推荐方法是否匹配；对不匹配案例分析原因，必要时新增指南或更新方法数据库，形成迭代改进循环。
- Potential coding-agent design value: 该来源方法可启发如何设计一个面向个体的知识型推荐/辅助代理：引导用户结构化描述任务，基于可解释规则和内置指南推荐合适的方法、设置或流程，并通过案例应用迭代扩充知识库。
- Decision: 三项条件均满足：软件的用户是单独的决策分析师/决策者；作者实质升级了可运行的网络DSS MCDA-MSS（规则、指南、方法数据库）；整个方法以文献和公开案例为基础，属于增量式软件改进，无需组织、硬件或临床基础设施。
- Confidence: 0.9

## ROLEX: A Novel Method for Interpretable Machine Learning Using Robust Local Explanations

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17141
- Artifact: ROLEX (RObust Local EXplanations) prototype user interface
- Individual user/task: 医疗保健专家（医生）或患者个人使用该界面，选择一个患者，查看该患者未来脆性骨折风险的机器学习预测结果，并通过多模态局部解释（文本、系数、决策规则、可视化）理解该预测的理由，以支持个性化诊疗和医学知识发现。
- Design delta: 首次将 ROLEX 局部解释方法实例化为面向医生的交互式界面：一次只展示一个患者以避免信息过载；使用 LARS 提取 top-5 特征保证解释稀疏性；提供文本理由、局部系数、局部决策规则和多种交互可视化等不同解释模式；允许用户选择变量和缩放图表以促进迭代学习。
- Design process: 作者先提出 XAI 框架（情境相关性、伦理与安全、法规与公共利益三个 desiderata），据此设计解释机制；然后开发 ROLEX 方法生成局部解释；为增强人机可解释性，采用交互式机器学习设计原则，用 Python Plotly/Dash 开发原型；与医疗专家协作选择特征、解释患者案例，并通过 4 名专家的非结构化访谈进行归纳编码反馈，评估并计划进一步改进界面。
- Potential coding-agent design value: 该来源的设计方法可启发我们为编码智能体构建面向单个开发者的可解释性界面：用多种局部解释模式（系数、规则、可视化）和稀疏 top-k 特征来呈现智能体行为或输出结果的理由，并通过小型专家/用户反馈迭代改进界面。
- Decision: 三项条件均满足：目标用户为单个医疗专家/患者个体；论文实际构建了可运行的 ROLEX 原型界面（Plotly/Dash），属于有界的个体面向软件原型；其开发依赖公开数据集、普通 Python 库和少量专家咨询，无被排除的资源需求。
- Confidence: 0.9

## Rethinking Gamification Failure: A Model and Investigation of Gamified System Maladaptive Behaviors

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2021.0284
- Artifact: 
- Individual user/task: 个体参与者（多为美国大学生）在实验室内使用游戏化在线学习系统学习欧盟《通用数据保护条例》（GDPR）材料，并完成多项选择测验；系统通过积分、徽章和排行榜提供游戏目标。
- Design delta: 通过三轮规则变更实质性地改变产品行为：第1轮仅按完成时间计分；第2轮按完成时间与正确数计分且答错后立即显示正确答案；第3轮只按正确答案计分且不限时；隐藏积分计算方式，并在每轮设置一个无法仅凭材料作答的题目，以操纵游戏-任务目标错位、游戏-任务复杂度和游戏化结构不公正。
- Design process: 设计需求来自理论驱动的构念：基于目标设定理论确定游戏-任务目标错位、游戏-任务复杂度、游戏化结构不公正三类设计问题；基于自我决定理论在后续问卷中测量自主、胜任、关系需求。Study 2 将这些设计问题操作化为三轮具体游戏规则，并在实验室中运行原型，随后用问卷测量心理机制。未采用迭代式设计科学研究。
- Potential coding-agent design value: 该来源方法可帮助小型团队学习如何通过有界原型中可操纵的规则/反馈设计（如目标对齐、任务复杂度、公平性）来研究个体用户对编码智能体工具的采用、适应或误用行为，并为产品功能设计提供理论驱动的设计变量。
- Decision: 三项条件均满足：Study 2 的个体用户面对可运行的游戏化学习原型；作者实际构建并通过三轮规则变更实质性修改了产品行为与反馈；该有界网页原型不依赖组织或大型基础设施，适合小型学术团队。Study 1 是现有系统的调查，但 Study 2 足以支撑匹配。
- Confidence: 0.9

## The Role of Social Cues and Trust in Users’ Private Information Disclosure

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16288
- Artifact: VideoBook
- Individual user/task: 个体用户作为网站访客，在首次访问一个类YouTube的视频浏览平台时观看自然类视频，并被该网站请求填写个人隐私信息（如姓名、地址、出生日期）。
- Design delta: 核心产品设计差异是社交功能的存在与缺失（如“喜欢”按钮、评分、评论、观看人数等），以及信任线索的操纵（高信任隐私保护声明 vs. 低信任警告+俄语提示+八次短暂页面故障）；此外设计了内嵌于网站的“帮助改进”个人信息调查弹窗。
- Design process: 需求与特征来源于理论假设：研究者基于目标系统理论、信任文献和社交线索文献提出假设，并在VideoBook中实例化社交功能和信任线索；信任提示通过预测试筛选；平台功能（如点赞、评论、评分、观看人数等）作为实验操纵被构建进网站；随后通过在线实验测量用户感知和行为。
- Potential coding-agent design value: 该研究展示了如何在有界、可运行的个体面向Web原型中，通过理论驱动的界面/交互变化（社交线索、信任线索）来实例化产品特征并测量用户行为，这可以类比于在编码代理中变化建议呈现、验证机制、反馈方式或交互策略等用户可见功能，并评估其对个体开发者行为的影响。
- Decision: 三项条件均满足：研究对象是个体用户在网站上的行为；作者构建并运行了VideoBook这一可操作的个体面向软件原型，并对社交功能和信任线索进行了材料化的产品级设计修改；开发范围是有界Web原型，使用公开视频与在线被试，不依赖企业部署或大型基础设施。
- Confidence: 0.9

## Visual analytics of set data for knowledge discovery and member selection support

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113635
- Artifact: Visual analytics system for the NBA dataset
- Individual user/task: 单个用户（如球队经理或分析师）使用该系统分析过往球队、检验候选阵容、预测比赛结果并支持成员选择决策。
- Design delta: 实例化了“地形图作为双向交互界面”的设计：用户在地图上指定TOI后，各图动态改变着色以显示预测输出、对手胜率、成员密度和成员统计；通过下拉菜单切换可视化统计量；实现了球队属性与成员阵容之间的双向映射，以及对抗情境下的阵容模拟和“已确定若干成员后选择新成员”的交互场景。
- Design process: 作者先从目标用户场景（球队经理进行成员选择）出发，在Section 3定义系统应满足的需求（处理集合、双向映射、解耦相关因素、支持分析与预测、消除组合爆炸、可塑性），再提出以流形网络模型为核心的框架，并通过生成流形建模（GMM）实现；随后在NBA数据上演示交互分析过程，并与基准系统比较预测和重建性能。未报告正式用户研究或迭代式设计过程。
- Potential coding-agent design value: 该来源方法可为编码代理产品的可视化探索界面设计提供参考：如何让单个用户在低维“需求/配置地图”上指定兴趣目标，并即时查看代理行为、输出和模块/工具组合的预测结果，从而支持候选方案的选择与比较。
- Decision: 三项条件均满足：系统由单个用户（球队经理/分析师）交互使用，属于个人层面；作者实际构建了可运行的交互式可视化分析原型并给出交互示例与评估；实现基于NBA数据和GMM算法，无组织协作、专用硬件或大规模数据依赖，适合小型学术团队。
- Confidence: 0.9

## Would you please like my tweet?! An artificially intelligent, generative probabilistic, and econometric based system design for popularity-driven tweet content generation

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113497
- Artifact: Popularity-Driven Tweet Suggestion and Auto-Generation System
- Individual user/task: 单个社交媒体经理或内容创作者在发布推文前，使用系统获得推文的上下文、句法和语义特征建议，接收自动生成的推文词序列，并对多个候选推文进行预期参与度评估，以选择最优内容。
- Design delta: 核心设计增量是将推文内容创作从“从零起草”转变为“建议/编辑”工作流：系统根据目标参与度自动生成词性序列，再通过混合分布采样词语生成完整推文序列；同时提供描述性报告（高频词、情感词、PoS n-gram等），并用预测模型对用户或系统生成的候选推文打分，辅助选择。
- Design process: 设计过程主要是基于文献综合和系统模块化设计：从社交媒体流行度和NLG文献中提取内容特征（上下文、语义、句法），提出模块化框架；随后用Twitter API数据实现演示，通过滚动时间窗比较8个模型选择最佳预测模型，设定目标参与度后运行生成模型，生成并评估推文建议。未报告用户研究或迭代式需求收集，评估以数值实验展示预测性能为主。
- Potential coding-agent design value: 该来源方法可帮助我们学习如何为编码智能体设计“生成建议+候选评估”的产品功能：系统基于数据生成可编辑的候选输出和结构化特征报告，再用预测模型对候选结果评分以辅助用户选择。
- Decision: 三项条件均满足：系统面向单个社交媒体经理生成推文建议（个体层面）；作者实际用R实现了可运行的推文建议、生成和评估原型（可运行的个体面向软件工件）；实现仅依赖公共Twitter API、标准库和普通云服务器，小型学术团队可复现（可行性）。
- Confidence: 0.9

## Addressing Online Users’ Suspicion of Sponsored Search Results: Effects of Informational Cues

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2021.0364
- Artifact: Simulated Taobao.com search results page (experimental prototype)
- Individual user/task: 个体用户（网购者）在模拟的C2C电商平台上进行商品搜索（耳机或运动T恤），浏览搜索结果页并决定是否点击赞助搜索结果（SSR）。
- Design delta: 在搜索结果页的SSR旁增加或改变信息线索的类型（质量评分Q-cue vs 卖家信誉评分C-cue）、评分水平（高、低，相对自然结果）以及SSR品牌知名度（知名vs不知名），以观察用户对SSR的认知、情感和行为回避变化。
- Design process: 作者基于状态怀疑理论将怀疑解构为决策不确定性、平台恶意感知和SSR加工三个维度，提出信息线索通过内化机制减少怀疑的假设；通过预实验选择商品、品牌和评分值，然后在实验室中构建并操纵搜索结果页，通过问卷调查、眼动和点击行为检验设计效果。
- Potential coding-agent design value: 该来源方法可启示如何在编码智能体界面中设计和快速原型化用户可见的信息线索（如质量/信誉评分、品牌等可信度信号），并通过有界原型实验观察个体用户对工具输出的怀疑、回避与使用行为。
- Decision: 三项条件均满足：研究对象是个体用户对赞助搜索结果的搜索与点击决策；作者实际构建并操纵了可点击的模拟搜索结果页这一面向个体的可运行界面原型，并通过信息线索进行了实质性界面设计改动；方法为实验室模拟页面与短时实验，无企业、长周期或大规模数据依赖，适合小团队复制。
- Confidence: 0.88

## Seeker Exemplars and Quantitative Ideation Outcomes in Crowdsourcing Contests

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1054
- Artifact: 自建在线创意竞赛平台（实验用，集成Getty Images API）
- Individual user/task: 个人解题者（solver）参加在线众包创意竞赛，在平台中通过关键词搜索图片、将候选图片加入短名单，并从短名单中选择最多15张图片提交，为假设的饮料公司Ake Co.的企业文章配图。
- Design delta: 在平台项目简报中设计并展示四种seeker exemplars配置（仅本地、仅远距、混合、无）作为信息呈现处理；同时为实现可观测的中间创意结果，设计了'搜索-短名单-选择'的交互流程，包括关键词搜索、分页加载（Show More）、短名单功能和最多15张提交的约束。
- Design process: 设计源于理论驱动的实验研究：基于知识重用创新（KRI）模型的搜索-评估阶段，将创意过程拆分为扫描、短名单、选择三层，并据此在自建平台中实现可观测的搜索、短名单、提交流程；seeker exemplars的本地/远距分类通过预测试验证（本地示例与饮料行业的相关性显著高于远距示例）；随后在MTurk上随机分配被试到不同exemplar条件，用行为日志检验假设。没有采用迭代式用户设计或行动研究。
- Potential coding-agent design value: 该研究的方法可帮助我们学习如何为编码智能体设计并验证'示例/参考信息呈现 + 搜索-筛选-提交'这类个体工作流功能，并通过行为日志评估其对用户产出数量的影响。
- Decision: 三条件均满足：研究对象是单个解题者在自建在线平台上搜索、短名单和选择图片的个体行为；平台是可运行的个体面向软件原型（集成Getty Images API并实现搜索/短名单/提交功能），且研究者通过exemplar信息呈现和交互流程进行了材料设计；开发与实验规模（自建原型+MTurk样本）对小型学术团队可行。
- Confidence: 0.88

## A Warning Approach to Mitigating Bandwagon Bias in Online Ratings: Theoretical Analysis and Experimental Investigations

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00817
- Artifact: Bias warning approach (risk-alert / risk-alert-with-ranking-task warning strategies)
- Individual user/task: 个体在线评论者：在实验性微电影评分界面中观看微电影后，对目标微电影进行1-10星评分；部分用户会先收到关于平均评分从众偏差的警告，并可能执行一个排序任务后再评分。
- Design delta: 警告内容与交互设计的变化：从仅风险提示（direct warning）扩展为风险提示+排序任务（ranking task）；排序任务为用户提供相对偏好的信息，用于改善对偏差存在和幅度的判断；同时操纵了平均评分的显示（下调/不调）和警告弹窗的交互约束。
- Design process: 两步设计过程：先依据已有警告研究采用风险提示警告，并利用FCM分析其缺陷（在无偏差时引起不必要的纠正）；再依据行为经济学的估价理论提出排序任务作为补充设计因素，构建风险提示+排序任务策略；通过预实验验证偏差发生/不发生的操纵方法，并在主实验与三个补充实验中实例化、检验和调整警告设计。
- Potential coding-agent design value: 该来源方法可启发我们如何在有界可运行的编码Agent原型界面中设计和测试用户可见的防偏差/自我校正功能（例如警告信息或排序/对比辅助任务），并通过小规模个体用户实验验证其对用户行为的影响。
- Decision: 三项条件均满足：研究聚焦个体评分者的在线评分行为（个体层面）；作者在可运行的实验性评分界面中原型化并材料地修改了警告功能，包括风险提示和排序任务（个体可运行的软件制品）；方法基于Qualtrics原型、公开微电影和小规模学生样本，对小型研究团队可行。
- Confidence: 0.85

## An Activity Theory Approach to Leak Detection and Mitigation in Patient Health Information (PHI)

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00687
- Artifact: PHI Leak Detection and Mitigation Prototype (Java prototype)
- Individual user/task: 医生、研究人员及其他医务人员等个体用户以特定角色请求访问患者健康信息（PHI）；系统根据基于活动理论生成的权限集匹配请求，检测潜在PHI泄露并进行缓解（如拒绝访问、通知管理员或患者）。
- Design delta: 核心设计增量是将活动理论组件（主体、对象、社区、工具、规则、分工）映射到访问控制策略，并引入“访问请求”与“访问响应”两个交互活动系统：系统用活动理论元组（subject, object, community, tool, rule, responsibility）生成权限集，请求以同一元组生成，匹配则允许、不匹配则触发泄露缓解策略（deny、通知、脱敏等）。
- Design process: 设计过程遵循设计科学研究：首先从文献和现有访问控制模型提炼需求；通过半结构化访谈4名医疗管理者收集PHI泄露场景和访问控制策略，从两个医疗机构的访问报告中提取100余条访问控制策略；用活动理论六个组件对策略和场景进行编码，形成访问控制映射；将活动系统重构为“访问请求”和“访问响应”两个交互系统，构建模型；随后用参与者评审和事务测试评估模型，并实现Java原型作为概念验证。
- Potential coding-agent design value: 该来源可帮助我们学习如何用活动理论等框架把用户、任务、规则、工具和职责映射到产品功能元组，进而在编码代理中设计基于策略的权限控制、请求校验和违规缓解界面。
- Decision: 三个条件均通过：设计目标是单个用户在访问控制系统中请求/接收对患者数据的访问，属于个体层面；作者实际用Java构建了可运行的原型（含表单、数据库、策略匹配和泄露缓解界面），而非仅模型或算法；开发为有限原型并由4名研究生10个月完成，依赖少量专家访谈和组织文档，未涉及长期组织变革或临床部署，小型学术团队可复制。
- Confidence: 0.85

## Cognitive Challenges in Human–Artificial Intelligence Collaboration: Investigating the Path Toward Productive Delegation

- Year/journal: 2022 / Information Systems Research
- DOI: 10.1287/isre.2021.1079
- Artifact: 
- Individual user/task: MTurk工人作为个体用户，在网页界面中逐一将100张日常物体/动物图片归入所列10个类别之一；在委派条件下，可选择将单张图片委派给GoogLeNet AI，或对每张图片的作答自信度打分；部分条件下会收到作答反馈。
- Design delta: 核心产品交互差异是委派控件的存在与否：基线/反转条件要求被试分类全部图片；委派条件增加一个随机位置出现的“委派给AI”按钮；Study 2增加自信度评分、解释的委派规则，以及基于自信度自动委派给AI的强制执行逻辑；Study 3增加任务后反馈显示；Study 4通过降低图像分辨率改变任务难度。
- Design process: 设计过程由研究假设驱动而非形式化设计科学流程：作者基于三个成功委派边界条件（存在互补性、识别互补性、执行高效委派规则）选择图像分类任务，并设计实验处理来操作界面中的委派控件、自信度报告、解释/强制委派策略和反馈；在预注册假设下对不同被试组比较分类准确率，并通过稳健性研究调整反馈和任务难度。
- Potential coding-agent design value: 该研究的方法可启发我们设计并逐项实验验证编码代理中面向用户的委派/控制机制——例如“交给AI处理”按钮、用户自信度提示、解释或自动执行的委派策略、以及任务反馈显示——通过在可运行的个体界面原型中变化这些细节来观察用户行为。
- Decision: 三项条件均满足：研究对象是独立使用界面的MTurk个体；作者实际搭建并运行了可交互的图像分类/委派实验平台，并通过添加委派按钮、自信度量表、自动委派和反馈等界面功能进行了实质性修改；开发依赖公开数据集、预训练模型和普通在线实验基础设施，适合小型学术团队。
- Confidence: 0.85

## Comparing low sensory enabling (<scp>LSE</scp>) and high sensory enabling (<scp>HSE</scp>) virtual product presentation modes in e‐commerce

- Year/journal: 2022 / Information Systems Journal
- DOI: 10.1111/isj.12382
- Artifact: HSE and LSE virtual product presentation modes (custom web shop/VR shopping environment)
- Individual user/task: 个体消费者在虚拟网店中查看厨房电器产品，并为朋友挑选一件礼物放入购物车。
- Design delta: 核心设计差异是感官使能级别：相同产品信息和交互选项（视角变化、缩放/旋转），但视觉输出从桌面屏幕变为HMD，触觉输入从鼠标键盘变为自然头部/手部追踪与空间控制器，并将产品置于匹配的虚拟厨房场景中；此外根据前测将硬件从HTC VIVE升级为HTC VIVE Pro并改进3D模型与光照。
- Design process: 设计需求来自消费者学习理论（态度理论、线索总和理论、重复学习与记忆）以及以往虚拟产品呈现研究；选择适合现有VR技术能力的厨房电器产品类别；两种模式保持相同的网店结构、产品信息和交互选项，仅改变感官使能方式；通过74人前测（关键事件技术）识别视觉质量、光照和文字可读性问题，并据此升级硬件和改善3D场景。
- Potential coding-agent design value: 该源方法可帮助学习如何为个体使用的软件工具设计并比较不同的呈现/交互模式——例如在保持底层功能不变的情况下，以不同方式在IDE中展示编码代理的推理过程或建议。
- Decision: 三项条件均通过：研究对象是个体消费者；作者实际构建了两种可运行的个体面向的交互原型（桌面3D网店和沉浸式VR网店）并实质性地改变了感官使能方式；开发是有界的实验室原型，未依赖被排除的大型基础设施或组织资源，小团队可行。
- Confidence: 0.85

## Could Gamification Designs Enhance Online Learning Through Personalization? Lessons from a Field Experiment

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1123
- Artifact: KEEP (Knowledge & Education Exchange Platform) MOOC with gamified performance feedback; private course "Social Analytics and Business Intelligence"
- Individual user/task: 个体学习者（大学本科生）在 MOOC 平台上自定节奏地完成五个在线学习模块（视频、讲义、测验、论坛、反思），任务是学习社会分析与商业智能内容；软件通过游戏化绩效反馈支持其自我调节学习。
- Design delta: 核心产品行为变化是绩效反馈的呈现方式：(1) 比较类型（个人进度 vs 社会排名）；(2) 消息框架（强调获得奖励的积极框架 vs 强调损失/惩罚的消极框架）；具体包括徽章、排行榜/失败榜、帮助榜/吝啬榜、任务完成百分比和框架化邮件。
- Design process: 设计是理论驱动的：基于自我调节学习理论选择绩效反馈作为核心游戏化元素，依据目标导向理论与游戏化个性化原则系统变化比较类型和信息框架；通过预实验问卷测量目标导向，并通过操纵检验确认被试感知到了不同反馈。
- Potential coding-agent design value: 该来源的个性化游戏化反馈设计方法（根据用户目标导向调整反馈的比较类型与框架）可启发编码智能体产品中任务反馈与激励信息的个性化设计。
- Decision: 三个条件均满足：聚焦个体学习者；在既有 MOOC 平台上实际改造并实例化了可运行的游戏化绩效反馈功能；开发范围是修改既有平台的有界功能，不依赖被排除的重型资源。
- Confidence: 0.85

## Disclosure decisions and the moderating effects of privacy feedback and choice

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113717
- Artifact: YouH
- Individual user/task: 个体用户使用移动购物应用 YouH，在购买虚拟商品和使用个性化服务时决定是否披露个人信息（如电话号码、邮箱、性别、出生日期、兴趣、地址、教育背景）。
- Design delta: 新增并实现隐私反馈功能本身，包括多层信息展示（四层界面）、隐私偏好设置开关、客服沟通入口，以及“是否查看隐私反馈”的选择机制；实验中还通过反馈的有无和选择的有无进行了设计变量的操纵。
- Design process: 设计过程以理论驱动为主：首先基于 justice theory 确定隐私反馈在程序公正、信息公正、互动公正三个维度上的功能要求，再参考 Schaub 等人提出的隐私通知设计空间（design space）来规划界面在时间、渠道、模态和控制四个维度上的设计；随后将界面实现到虚构应用 YouH 中。研究者在正式实验前使用 10 位 IS 教师/研究生的访谈和 80 名学生的预测试对量表、实验流程和界面细节进行了调整。
- Potential coding-agent design value: 该研究展示了一种在小型原型产品中设计和实例化面向用户的反馈/选择功能并开展个体实验室实验的方法，可借鉴来设计和测试编码代理产品中的用户可见功能（如透明度反馈、用户控制选项）及其对个体行为的影响。
- Decision: 三个条件均满足：研究聚焦于个体用户的隐私披露决策；真实实现并可运行的虚构应用 YouH 中包含了实质性设计的隐私反馈功能和选择机制；该设计为有界原型，开发与实验范围适合小型学术团队。
- Confidence: 0.85

## How AI-Based Systems Can Induce Reflections: The Case of AI-Augmented Diagnostic Work

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/16773
- Artifact: ML-based clinical decision support system (CDSS) for chest X-ray diagnosis
- Individual user/task: 肺科医生（pneumologists）单独阅读胸部X光片，从9种肺病和“无异常”中做出影像诊断，并在第二阶段结合CDSS预测概率重新评估自己的诊断。
- Design delta: 核心设计增量是将ML系统定位为“反思伙伴”而非传统DSS：AI预测在医生形成初始判断后才呈现；用条形图给出10类概率；医生可在第二阶段重新评估同一X光片，体现“先判断后对照”的交互流程。
- Design process: 设计过程由反思实践理论引导：先构建基于AlexNet的CDSS并选择预测正确的20个病例；设计两阶段反思实习，在医生独立诊断后展示AI条形图预测，使其能重新评估；通过6人试点的出声思维协议和23人主研究的半结构化交互协议收集数据，以扎根理论（Gioia方法论）归纳出机器诱导反思模型，后续还通过小组反思补充设计需求（如算法透明性、临床信息）。
- Potential coding-agent design value: 该来源展示了一种“先让用户独立判断、再呈现模型预测”的反思伙伴式交互设计，并系统编码了确认/冲突引发的反思深度差异，可为编码代理工具设计“延迟建议/异议提示”类功能以促进开发者反思自身方案提供可借鉴的产品交互原型和理论化路径。
- Decision: 三项条件均满足：对象是个体医生及其诊断任务；作者实际构建了可运行的ML-CDS原型（AlexNet+条形图概率输出）并用于个体交互；开发依赖公开数据集和常规深度学习训练，样本为约29名医生，未涉及企业级或临床基础设施，小型学术团队可实现。
- Confidence: 0.85

## How Product Display Orientation Affects Customers’ Choice Satisfaction in Online Purchase: A Choice Closure Perspective

- Year/journal: 2025 / Information Systems Research
- DOI: 10.1287/isre.2022.0575
- Artifact: Experimental e-commerce product display web page (horizontal vs. vertical display prototype)
- Individual user/task: 个体在线购物者从一组可比商品中选择一个商品，并在选择后评价其选择满意度（choice satisfaction）。
- Design delta: 将商品列表的展示方向从垂直改为水平（或反之），并在部分条件下增加“The end”文本结束标记；这是网页上可见的信息表征与布局变化。
- Design process: 设计过程是理论驱动的：作者基于选择闭合理论与水平显示优势文献提出假设（H1–H3），然后构建实验性网页原型，在五个随机实验中系统操控展示方向和终结点线索，以验证设计特征对选择满意度的影响；未采用迭代式用户中心设计。
- Potential coding-agent design value: 该来源方法可能有助于我们学习如何对编码智能体的输出候选或方案展示进行可运行的界面级设计（如横向/纵向布局、终止提示），并通过随机实验评估用户对所选方案的满意度。
- Decision: 三项条件均满足：研究对象是个体在线购物者；研究者构建并改变了可运行的电商商品展示网页原型（水平/垂直布局及“The end”提示）；采用网页原型、在线/实验室小样本实验和低成本眼动仪，开发范围对小型学术团队可行。
- Confidence: 0.85

## More Than a Bot? The Impact of Disclosing Human Involvement on Customer Interactions with Hybrid Service Agents

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2022.0152
- Artifact: Lisa (field experiment hybrid service agent); custom chatbot (controlled online experiment, Microsoft Bot Framework)
- Individual user/task: 个体客户通过聊天界面联系电信公司客服，提出账单、合同或产品问题；在线实验中参与者需要就异常高额账单联系客服。
- Design delta: 在欢迎消息中增加前期披露语句（“如果我不知道答案，我的人类同事会阅读您的消息并回复”），以及在机器人无法回答时增加介入披露语句（“我将把问题转给我的人类同事”）；未披露条件使用等长的中性语句。在线实验还加入50秒延迟模拟人工介入。
- Design process: 基于受众设计理论和印象管理文献提出假设，将人类参与披露操作为欢迎消息和介入时消息中的文本差异；在线实验采用引导式对话和模拟人工介入，并通过操纵检验确认处理有效性；研究还通过鲁棒性检验排除了措辞本身等替代解释。
- Potential coding-agent design value: 该来源的方法可帮助我们学习如何在对话式编码代理中构建有界的可运行聊天原型，并通过改变单个用户可见的披露或交互提示（如人类参与提示）来观察个体用户行为的变化。
- Decision: 论文聚焦个体客户与混合服务代理的交互；作者通过修改真实聊天机器人并在受控实验中构建自定义聊天机器人，实质性地实例化了可运行的个体面向软件界面，并对用户可见的披露信息做了具体改变；受控在线实验的开发方式（Microsoft Bot Framework原型+在线招募）对小型团队可行。三个条件均满足。
- Confidence: 0.85

## Reach Out and Touch: Eliciting the Sense of Touch Through Gesture-Based Interaction

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00704
- Artifact: Unnamed experimental e-commerce website
- Individual user/task: 个体消费者在实验室中完成在线购物任务：浏览实验网站上的产品，检查产品图片和文字描述，并选择一件产品作为送给朋友的礼物。
- Design delta: 核心设计差异是交互通道：同一实验网站分别支持触摸屏直接触摸与中空气手势操作，改变用户与产品界面的身体交互方式；后续实验还改变了产品呈现格式（3D 图像）和移动设备情境。软件功能本身（浏览、点击、放大）保持简单，操纵主要体现在输入设备和交互方式上。
- Design process: 设计需求并非来自用户研究或设计迭代，而是从 feelings-as-information 理论和模拟触觉文献推导研究假设，然后为实验构建类似电商的网站；产品图片和文字描述取自 Amazon，品牌名被移除；产品类型（围巾/笔记本电脑、T恤/相机、毛绒玩具/牙膏）用于操纵产品触觉信息重要性；交互方式通过设备进行操纵，并进行了预测试和操作检查。
- Potential coding-agent design value: 该研究展示了一种用轻量实验网站和市售输入设备系统性地改变交互方式、测量个体感知体验并检验其对任务结果影响的途径，可帮助我们学会为编码代理设计者构建可运行的交互原型，并用小样本个体实验检验特定交互特征对使用者感知和满意度的影响。
- Decision: 三项条件均满足：研究对象为个体消费者在可运行实验电商网站上的购物任务；作者构建了可运行的交互式网站原型并使用不同手势输入设备；方法为实验室单次实验，开发量小、无组织依赖，适合小型研究团队。
- Confidence: 0.85

## Showcase: A Data-Driven Dashboard for Federal Criminal Sentencing

- Year/journal: 2023 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00796
- Artifact: ShowCase
- Individual user/task: 个体用户主要为联邦地区法院的量刑法官，也可扩展至辩护律师和检察官；任务是在量刑前综合查看指南、同行决策、公众意见、相似案例、犯罪者社会纽带因素、风险评分与需求，以作出更公平、客观、透明的量刑决定。
- Design delta: 设计增量包括：提出2×2矩阵四象限仪表盘结构（一般/个体 × 三角测量/具体化）；将不同量刑来源（指南、同行、公众等）以可点击、可筛选的多个区间呈现；增加'信息'按钮展示数据来源与收集方法；将通用再犯风险替换为基于宾夕法尼亚州量刑风险评估工具的个体化风险评分；增加被告需求模块；在迭代中加入可就业性、教育、帮派关联等因素，并将'crowdsourcing'改为'public opinion'。
- Design process: 采用设计科学研究（DSR）方法：先基于文献回顾和理论形成初始设计；然后用MTurk招募612名参与者对两个虚构犯罪场景（毒品持有、财务欺诈）进行定量调查，识别公众认为相关的法律外因素（均值≥2.5者可视化，前五名突出显示）；再用5位法律、技术、HCI专家进行半结构化访谈征求功能与设计意见并迭代；最后用11位法律专家访谈按effectiveness、efficacy、efficiency、ethics、elegance五标准评估原型。
- Potential coding-agent design value: 该来源方法可帮助我们学习如何为一个面向个体专业用户的编码代理产品设计有界的、理论驱动的交互式决策支持界面：通过文献与理论提炼需求、结合用户调查和小规模专家访谈迭代功能，并用可点击原型中的信息透明控件和可筛选参考信息呈现来支持用户决策。
- Decision: 三项条件均满足：焦点是个体法官使用仪表盘；作者实际构建了'ShowCase'接口原型并定义了可点击、可筛选的交互功能；开发方式为有界原型加公开数据、MTurk调查和小规模专家访谈，适合小型学术团队。
- Confidence: 0.85

## The Impact of Animated Banner Ads on Online Consumers:  A Feature-Level Analysis Using Eye Tracking

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00659
- Artifact: None (experiment website with animated banner ads)
- Individual user/task: 在线消费者（学生被试）在浏览或搜索任务中浏览包含动画横幅广告的实验网页。
- Design delta: 在同一广告位内系统改变横幅广告的动态行为：运动（随机移动）、延迟5秒出现、逐渐增大到全尺寸，并测试八个单独/组合条件（Appendix Table D1）。
- Design process: 从注意力理论推导出三个动画特征，通过多个预试验选择被试熟悉度一致的电影DVD、兴趣适中的文章、非烦扰的动画速度；使用焦点小组确定广告内容；用Graeco-Latin square平衡顺序效应；实验3基于真实旅游网站样式构建更复杂的网页以检验外部效度。
- Potential coding-agent design value: 该研究的特征级设计方法可启发编码Agent产品的界面动态设计，例如将通知出现、移动、缩放、延迟等行为分解为可独立操纵的设计特征，并通过浏览/搜索任务检验其对用户注意与记忆的影响。
- Decision: 三个条件均满足：研究对象是个体消费者；研究者实际构建并运行了带动画横幅广告的实验网页，并实质修改了动画特征；有界网页原型和小规模实验室实验对小型研究团队可行。
- Confidence: 0.85

## The Attraction Effect in Crowdfunding

- Year/journal: 2023 / Information Systems Research
- DOI: 10.1287/isre.2022.1152
- Artifact: Digital reward menu (在线众筹奖励菜单原型/真实 Kickstarter 奖励菜单)
- Individual user/task: 个体众筹支持者（backer）在奖励菜单中查看多个奖励选项并选择要支持的档位；研究目标是通过菜单构成（诱饵选项）改变这一购买/支持选择。
- Design delta: 在原有竞争者/目标两选项的基础上加入一个被目标选项支配的诱饵选项：价格诱饵（与目标质量相同但价格更高）或质量诱饵（与目标价格相同但质量更低），使目标选项的价值感提升，从而改变用户选择。
- Design process: 需求/特征来源于行为经济学和吸引力效应文献：先用数学例子按 salience theory 推导诱饵的属性值（价格诱饵或质量诱饵），再依据 Huber et al. (2014) 和 Lichters et al. (2015) 的诱饵设计指南实例化为具体的奖励组合，并在系列实验中逐步增加真实性（数字属性→非数字属性、假设选择→有经济后果的选择、实验室→真实平台）进行预测试和迭代。
- Potential coding-agent design value: 该方法可启发编码助手产品中的小规模选择架构设计：例如在计划方案、配置项或功能推荐菜单中，基于行为理论加入一个被目标选项支配的诱饵/备选来影响个体用户选择，并用有界原型和在线实验快速验证。
- Decision: 三项条件均满足：研究聚焦个体支持者在数字奖励菜单中的选择；作者实际构建或修改了可运行的奖励菜单页面（Qualtrics 原型、Kickstarter 仿制网站及真实 Kickstarter 奖励菜单）；核心设计手段是在有界网页原型中插入诱饵选项，规模适合小型研究团队。
- Confidence: 0.82

## The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings

- Year/journal: 2025 / MIS Quarterly
- DOI: 10.25300/misq/2025/18531
- Artifact: 
- Individual user/task: 个体用户在浏览器中执行图像分类任务，并处理穿插出现的浏览器性能通知和安全警告；研究者关注用户是否注意并遵从安全警告。
- Design delta: 将安全警告与普通通知在视觉外观上区分（实验1）；将警告的交互模式从标准“点击关闭”改为按住滑块或拖放滑块（实验2、3），并在保持视觉外观几乎不变的情况下仅改变交互模式（实验3）。
- Design process: 从提醒/通知与安全警告相似导致用户忽视的问题出发，基于泛化习惯化（双过程理论）和图式理论推导假设；据此设计两类干预（视觉区分、交互模式区分），在 Firefox 现成警告和 UI 组件基础上实现原型，并通过两个在线现场实验和一个 fMRI 实验进行检验；实验3通过同时包含按钮和禁用滑块的界面尽量保持视觉外观不变，以分离交互模式效应。
- Potential coding-agent design value: 该研究展示了如何针对个体用户的自动化和习惯化行为，通过在可运行原型中改变通知/警告类界面的视觉外观或交互模式来实现有理论依据的防御性产品设计；可启发编码代理中安全或重要提示/确认界面的设计，使其与普通通知区分以减少用户盲目跳过。
- Decision: 三个条件均满足：研究对象是单个用户对浏览器警告的行为与神经反应（个体层面）；作者实际构建并修改了可运行的浏览器警告原型和交互变体（可运行个体软件制品）；实现方式为对现有 Firefox UI 组件和开源 psiTurk 的有界修改，虽然 fMRI 评价需要专门设施，但软件设计和原型构建本身可由小团队完成。
- Confidence: 0.82

## Effects of Personalized Recommendations Versus Aggregate Ratings on Post-Consumption Preference Responses

- Year/journal: 2022 / MIS Quarterly
- DOI: 10.25300/misq/2022/16301
- Artifact: 
- Individual user/task: 个体消费者/被试在线阅读笑话，并在看到个性化预测评分和/或聚合用户评分后立即提交其对笑话的体验后偏好评分（1–5星）。
- Design delta: 核心设计差异是被试看到的推荐信息表示形式：聚合用户评分（“平均用户评分为X”）vs 个性化预测评分（“系统认为你会评为X”）vs 两者同时展示，以及评分值被随机设为高/低/中并控制展示顺序；同时收集即时评分以测量推荐偏差。
- Design process: 设计需求并非来自设计科学流程，而是从推荐偏差、锚定效应和社会影响等理论假设出发，通过实验操纵展示条件。作者随机分配被试到单推荐/双推荐条件，将推荐值随机设为高/低/中，以隔离因果效应；并通过先导评分阶段（Phase 1）构造控制变量。
- Potential coding-agent design value: 该来源方法可启示如何构建一个有边界的实验原型，仅变化一个面向个体的推荐/反馈显示特征（如个性化vs聚合、高vs低），并测量该特征对个体事后判断的影响，适用于测试编码代理输出或反馈展示形式的设计变体。
- Decision: 三项条件均满足：研究对象是个体消费者的体验后偏好；论文构建并运行了一个可操作的实验性评分界面，并实质性改变了个体看到的推荐信息表示形式；实验使用公开数据集和学生被试，开发与实施范围适合小型学术团队。
- Confidence: 0.8

## Human Behavior Mining: A Framework for Theorizing About mHealth Behavior Using Digital Trace Data

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00938
- Artifact: Custom mHealth app (unnamed)
- Individual user/task: 个体用户（大学生样本）使用 mHealth 应用记录身体活动、查看目标进度、调整目标、查看排行榜和社交动态，以支持身体活动行为改变。
- Design delta: 基于社会认知理论（SCT）将自我调节和交互决定论概念操作化为可用的应用功能（添加活动、查看进度、设定新目标、查询排行榜、访问社交动态），并加入内部日志埋点以采集行为追踪数据。
- Design process: 设计需求主要从社会认知理论演绎而来：先选择 SCT，指出其动态概念（自我调节、交互决定论）缺乏实证操作化，然后将理论构念映射为 mHealth 功能，并据此开发应用；未报告用户研究或迭代设计。
- Potential coding-agent design value: 该来源展示了如何从行为理论演绎出个体面向应用的功能集合，并通过内部事件日志对功能使用进行埋点，这可为编码代理工具的功能设计与使用行为追踪提供可借鉴的思路。
- Decision: 三个条件均满足：研究对象为个体 mHealth 用户；研究者实际构建了可运行的个体面向应用（自定义 mHealth 应用）并基于 SCT 实现了具体功能；开发与数据收集规模（自研应用、61 名用户四周）对小型学术团队可行。
- Confidence: 0.8

## Real-Effort Incentives in Online Labor Markets: Punishments and Rewards for Individuals and Groups

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/15166
- Artifact: 
- Individual user/task: 个体实验参与者（大学生）作为在线劳工市场工人，单独为复杂/模糊图像输入描述性标签；个人标签与同组其他三人的标签合并为小组标签列表，系统按与Google Cloud Vision API基准标签的相似度计算小组得分，进而决定个人收益。
- Design delta: 外生激励干预机制：在实验后半段将收益乘数从基准90调整为115（奖励）或65（惩罚），并作用于全部小组成员或仅最高/最低贡献者；系统自动识别前5轮表现最佳/最差成员，向参与者展示乘数变化消息，由此改变每个用户在后续任务中的收益函数和反馈。
- Design process: 基于公共品博弈和实验经济学文献建立假设，采用两阶段设计（前5轮基线、后5轮干预）；通过oTree实现随机分组、随机治疗分配、标签收集、相似度计算、乘数动态改变和信息展示；从Google Cloud Vision API和GloVe预训练向量选择客观基准与相似度度量，以支持实时反馈。
- Potential coding-agent design value: 该来源的方法可启发在编码代理产品中实现基于用户行为的外生激励与反馈机制（例如根据个体表现动态调整权限级别、奖励或惩罚性提示），并用小的受控个体使用实验来检验其对努力程度的影响。
- Decision: 三个条件均满足：参与者以个体身份使用可运行的图像标注实验系统；该oTree原型包含实质性的软件交互特征（收益乘数干预、通知消息、相似度反馈）；开发仅需开源平台、公开API和预训练模型以及184名志愿者，适合小团队。
- Confidence: 0.8

## The Effect of Risk Representation Using Colors and Symbols in Business Process Models on Operational Risk Management Performance

- Year/journal: 2021 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00676
- Artifact: RIC-extended BPMN process models delivered via a self-developed online experiment website
- Individual user/task: 具有会计或运营背景的个体参与者（MTurk workers）通过在线实验网站阅读带风险与控制信息表示的BPMN流程模型，完成风险理解、控制理解、控制改进建议和风险感知判断任务。
- Design delta: 在BPMN模型上添加RIC信息表示：主要符号扩展（风险警告三角+感叹号、控制放大镜+对勾）和次要符号扩展（红色风险、绿色控制），与纯文本注释的基础模型进行对比；所有变体保持信息等价，仅改变视觉线索。
- Design process: 基于双系统理论、色彩情境理论和有效视觉符号理论提出假设并推导设计；从既有RIC扩展文献中选取警告三角/感叹号和放大镜/对勾图标；通过两次预测试（N=131、N=125）迭代调整颜色强度和简化视觉线索组合；通过信息等价设计控制实验偏差。
- Potential coding-agent design value: 该来源方法可启发我们如何为编码代理界面设计并小规模测试风险/状态的信息表示（例如用红色和图标突出高风险操作、用绿色表示已受控项），并通过在线实验比较不同表示的个体理解效果。
- Decision: 三项条件均通过：研究聚焦个体参与者对信息的理解与风险判断；作者构建了可运行的在线实验网站，并在BPMN模型这一用户面对的信息表示上实质性地加入颜色和符号变体；自建网站+MTurk的开发与数据收集规模对小型研究团队可行。
- Confidence: 0.8

## Virtual Reality, Mental Models, and Mindful Decision-Making

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00933
- Artifact: HardwareOne website (Study 1); VR house-tour presentation on Meta Quest 2 (Study 2)
- Individual user/task: Study 1: individual students learning six computer hardware components on a website in preparation for an exam. Study 2: individual participants as house hunters viewing a house and deciding whether to purchase it.
- Design delta: Materially altered how the same product/house information is represented and controlled: added interactive viewing (mouse/keyboard rotation and zoom; head-turning and controller-based movement in VR) and depth cues (stereo 3D rendering/headset immersion), versus static 2D images, while keeping the information content equivalent across conditions.
- Design process: The design was derived from a conceptual distinction between two VR presentation features (interactive viewing and depth cues). Requirements and manipulations were instantiated in a self-built website and a VR house tour; pilot studies were used to refine the experimental websites and survey instruments and to check treatment effectiveness. Information amount was deliberately held constant across conditions to isolate the effects of presentation features.
- Potential coding-agent design value: This source demonstrates a feasible template for instantiating and comparing alternative user-facing presentation and interaction features (e.g., interactive control, depth/3D cues) in a bounded prototype and for measuring their effects on individual users' mental models and decision processes, which could inform design experiments for coding-agent interfaces.
- Decision: All three required conditions pass: the focal setting is individual users; the authors built and configured runnable individual-facing software artifacts (the HardwareOne website and the VR house-tour presentation) with material presentation and interaction deltas; and the approach relies on off-the-shelf devices, publicly available content, and modest lab samples, so it is feasible for a small academic team.
- Confidence: 0.8

## Ambivalence Is Better than Indifference: A Behavioral and Neurophysiological Assessment of Ambivalence in Online Environments

- Year/journal: 2023 / MIS Quarterly
- DOI: 10.25300/misq/2022/17123
- Artifact: Bivariate information representation (bivariate rating scale)
- Individual user/task: 在线购物情境中的个体消费者，在模拟电商页面中评估产品评分、描述和评论，并做出购买决策。
- Design delta: 将单一的2.5星/3星双极评分替换为双变量评分量尺（分别显示正面和负面评分强度），并在部分实验中配套显示评论；这是核心的产品表征变化，影响了用户对矛盾信息的感知、决策复杂度和购买行为。
- Design process: 作者先通过EEG实验确认ambivalence与indifference在双极表征下不可区分，并发现顺序效应；随后提出双变量评分表征作为干预，在实验2-4中迭代该表征：实验3加入新颖双极对照和真实评论以排除新颖性解释，实验4改为顺序呈现评论以提高生态效度。刺激材料通过对Amazon评论进行文本分类并人工提取属性生成。
- Potential coding-agent design value: 该论文提供了一个通过调整用户可见的信息表征（而非算法本身）来改变个体理解与决策的简洁设计迭代范例，可启发编码智能体产品设计如何用不同方式呈现模型输出、置信度、诊断信息或反馈以影响开发者的决策。
- Decision: 三个条件均满足：研究对象为在线购物中的个体用户；作者在实验室中实现并操作了一个可运行的模拟电商界面，并实质性修改了评分表征（双变量 vs 双极）；该界面原型和实验任务规模小、不依赖组织合作或重型基础设施（EEG仅为评估手段），适合小团队复现。
- Confidence: 0.78

## Decisions for information or information for decisions? Optimizing information gathering in decision-intensive processes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113632
- Artifact: MDP recommender / run-time recommendation tool for decision-intensive processes
- Individual user/task: 单个决策者（如报价流程中的知识工作者）在决策密集型流程中决定下一步是继续收集哪项信息，还是基于已有信息做出最终决策（如是否投标及报价）。
- Design delta: 核心产品级改动是引入‘Information or Decision’推荐环节：在用户 CMMN 模型中插入计划片段，每次任务完成后调用 MDP 推荐器，展示当前状态下允许的动作列表、最优动作以及各动作期望利润；用户可忽略建议，系统会在新状态下继续给出建议。
- Design process: 设计时阶段先由用户/流程建模者用 CMMN 建立 DIP 模型；然后按任务类型（决策任务、程序性任务、信息获取任务、附加任务）进行分类，并定义信息结构（收益函数）和概率分布；将模型过滤为 MDP 并用后向归纳求解，得到每个状态的最优动作；部署时将求解结果配置为运行期推荐工具，并在案例中与行业决策者共同验证模型和对比决策树。
- Potential coding-agent design value: 该来源可启发如何为一个面向单用户的工作步骤推荐器设计交互：在每步给出可选动作、期望收益和推荐动作，同时允许用户忽略建议并在后续状态继续给出建议。
- Decision: 三个条件均满足：研究对象是单个决策者；作者实际构建/配置了可运行的 MDP 推荐工具并在 CMMN 引擎中部署演示；开发规模为 Python 脚本、CMMN 模型与计划片段，适合小型学术团队。
- Confidence: 0.78

## Effects of Idea Set Partitioning on Selection Quality: An Exploratory Eye-Tracking Study of Information Processing

- Year/journal: 2025 / Journal of the Association for Information Systems
- DOI: 10.17705/1jais.00958
- Artifact: Idea selection platform (未命名的实验性网页选题界面)
- Individual user/task: 非专家评分者（研究生被试）在网页界面上从32个创意中选择最有前景的创意；每个屏幕呈现2个或4个创意，并包含标题、描述和点赞数、历史得分、创造力得分、标签等反馈线索。
- Design delta: 核心设计变化是选择集的划分粒度：同一32个创意集合被分为16屏×2个创意或8屏×4个创意（即子集大小2 vs 4）；此外为每个创意补充/呈现了四种反馈线索（likes、历史创意得分、创造力得分、标签），为评分者提供可比较的参照点。
- Design process: 设计特征源于理论推演而非用户共创：作者基于数字助推/选择架构、线索可评价性、信息处理策略等文献提出假设，然后从OpenIDEO真实竞赛中挑选32个创意，缩写描述并附加反馈线索（likes、历史得分、通过Toubia-Netzer接口计算的创造力得分、IBM NLU生成的标签），再以屏幕子集大小（2 vs 4）实现划分操作，并用随机数生成器决定每个被试的创意呈现顺序；没有报告迭代设计或用户研究。
- Potential coding-agent design value: 该文展示了一种轻量级的个体界面设计方法——通过改变同一选项集合在界面上的分组大小（如每次呈现2个还是4个建议）来调节用户的比较式信息加工与选择质量，可迁移到编码代理中候选代码方案、建议列表或反馈提示的呈现设计研究。
- Decision: 三项条件均满足：研究聚焦于个体评分者的选择任务；作者构建并使用了可运行的网页化创意选择平台，并通过子集大小实现了具体的界面设计变化；软件开发范围小、依赖公开数据和API，眼动测量仅用于评价而非构建工件，因此对小型研究团队可行。
- Confidence: 0.78

## How to elicit and cease herding behaviour? On the effectiveness of a warning message as a debiasing decision support system

- Year/journal: 2022 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113652
- Artifact: 
- Individual user/task: 个体网站访客在残疾保险和退休规划场景中做出个人财务决策；用户在模拟工具中输入家庭构成、收入、工作类型等信息，并从 Basic、Premium、Custom 三个选项中做出选择。
- Design delta: 材料设计变更包括：（1）在 Premium 选项上添加随机同行信息提示（“X% 的人选择了此选项”）；（2）在初始选择后增加一个警告消息弹窗，解释从众偏差并披露同行信息为随机生成，且允许用户修改选择。
- Design process: 设计需求来自行为经济学文献：先从同伴信息干预和去偏决策支持文献导出核心特征；实验中将同行比例随机设为 10%-90% 以探查触发点；警告消息的内容基于去偏文献中的警告类策略；没有报告迭代式设计过程。
- Potential coding-agent design value: 该方法可启发我们在个体使用的编码辅助工具中设计并嵌入有界的社会影响提示、警告/去偏提示以及用户重新考虑机制，并通过变化提示强度观察对用户选择的影响。
- Decision: 三项条件均满足：对象是个体财务决策者；作者构建并实质改动了可运行的交互式 DSS 网站（模拟工具、同伴信息提示、警告消息）；开发范围是有界 Web 原型，未依赖被排除的大型基础设施或组织资源。
- Confidence: 0.78

## Trust calibration of automated security IT artifacts: A multi-domain study of phishing-website detection tools

- Year/journal: 2021 / Information & Management
- DOI: 10.1016/j.im.2020.103394
- Artifact: Custom phishing-website detection tool (detector; Java-based experiment tool)
- Individual user/task: 个体用户在使用浏览器访问网站时，借助该检测工具判断网站是否为钓鱼网站，并决定是否访问、浏览或与网站交易。
- Design delta: 在检测工具界面中显式呈现信任校准信息（准确率、运行时间、错误后果严重程度、威胁类型），用进度条可视化运行过程，并在检测到钓鱼网站时显示警告页面。
- Design process: 以自动化信任与依赖（ATR）框架为内核理论，推导出性能（检测准确率）、过程（运行时间）、目的（错误后果严重性、威胁类型）三类信任校准器，并将这些信息作为界面特征实例化到检测工具中；通过预测试和试点测试完善实验工具与流程，再通过 2×2×2×2×2 全因子实验室实验检验校准器对信任的影响。
- Potential coding-agent design value: 该来源方法可帮助学习如何在编码代理等个体使用的工具界面中显式设计并呈现“能力/风险校准”信息（如准确率、错误后果、运行状态），以影响用户的信任与依赖行为。
- Decision: 三项条件均满足：研究聚焦个体用户的信任、依赖和使用行为；作者实际构建并运行了一个有界的 Java 钓鱼网站检测工具原型，并在其中实例化了信任校准信息显示、进度条和警告等用户界面特征；软件开发范围（有界原型、公开网站数据、常规实验工具）对小团队可行。
- Confidence: 0.78

## Cost-based analysis of the impact of data completeness and representational consistency

- Year/journal: 2023 / Decision Support Systems
- DOI: 10.1016/j.dss.2023.114044
- Artifact: In-house online SQL query platform; integrated PostgreSQL databases D_A, D_B, D_C
- Individual user/task: 单个参与者（修完入门数据库课程的大学生）通过在线平台书写并提交SQL查询，解决需要结合PubMed、ORCID、GRID中至少两个数据集信息才能完成的六项数据查询任务。
- Design delta: 对数据库进行了数据质量层面的实质性修改：合并重复作者行、为PubMed记录补充GRID标识符、用标准化表示替换缺失或不一致的标识符（如ORCID ID、FundRef ID）、改进数据库规范化结构；三个版本在数据完整性和表示一致性上不同。
- Design process: 基于“fitness for use”视角，从典型科研数据使用场景设计六项SQL任务（Table 1）；随后从原始数据库D_A出发，依次应用数据质量改进操作生成D_B和D_C；通过实验测量参与者的任务解决率、解决时间和查询次数来评估改进的实际影响。
- Potential coding-agent design value: 该来源方法可帮助学习如何通过可运行的工具平台和受控任务实验，量化数据质量或信息表示变化对用户任务完成效率的影响，从而为设计编码代理中的信息呈现与数据消歧功能提供成本型评估思路。
- Decision: 论文构建了可供单个用户实际使用的在线SQL查询平台和三个版本的集成数据库，并在个人层面通过实验衡量数据质量改进的影响；数据来源公开、工具常规、样本为学生，适合小团队复制，因此三项条件均满足。
- Confidence: 0.75

## Behaviorally Measuring Usability by Analyzing Users’ Mouse Movement Efficiency

- Year/journal: 2024 / MIS Quarterly
- DOI: 10.25300/misq/2023/17900
- Artifact: 
- Individual user/task: 个体用户（学生或MTurk参与者）在研究人员搭建的网站上执行任务：Study 1为顺序点击编号目标；Study 2为在线购物场景中查找并购买笔记本电脑配件；Study 3/4为试用商业软件各组件的真实用户。
- Design delta: 在Study 2中，保持页面布局和结构不变，通过增加/减少视觉杂乱（如横幅广告、无关侧边栏、文本链接排序等）实现高/低可用性两种界面变体；Study 1操纵干扰目标的数量；这些是已实例化的用户可见界面改变。MME度量本身（归一化AUC/AD、最大偏差）是新增的软件化测量功能。
- Design process: 研究团队从已有鼠标追踪文献中选取AUC、AD、MD三种偏差度量，基于BCT与RAM推导MME，提出个人化IRT与归一化处理，先在Study 1中通过实验迭代验证，再在Study 2-4中扩展到在线购物、商业Web和桌面产品。界面高/低可用性操纵依据可用性与视觉杂乱文献（如Altmann, 2001; Rosenholtz et al., 2007; Moacdieh & Sarter, 2014）设计。
- Potential coding-agent design value: 该研究可启发我们在编码代理的可交互原型中嵌入轻量级鼠标轨迹采集，以个体开发者正常使用时的操作效率来比较不同界面组件或工作流步骤的相对可用性。
- Decision: 三条件均通过：研究聚焦个体用户在网站/软件上的交互；作者实际搭建并/或配置了可运行的个体面向软件原型（Study 1-2自建网站，Study 3在现有应用安装追踪脚本），并实现了材料化的用户可见界面变更（高/低可用性、视觉杂乱）；核心开发范围对有界原型和小规模个体研究可行。
- Confidence: 0.72

## Retargeted vs. Generic Product Recommendations: When is it Valuable to Present Retargeted Recommendations?

- Year/journal: 2024 / Information Systems Research
- DOI: 10.1287/isre.2020.0560
- Artifact: Experimental e-commerce website for women's tops (retargeted vs. generic recommendation display)
- Individual user/task: 个体消费者（Amazon MTurk 美国女性）在实验网站上浏览女式上衣商品、将感兴趣的商品加入购物车，并在第二阶段可能购买商品；系统在焦点商品（FP）页面展示一个推荐商品（RP）。
- Design delta: 在 FP 页面展示一个推荐商品，并操纵推荐类型：通用推荐（基于 Slope-One 相似度）与重定向推荐（用户先前浏览过的商品）；现场实验对应显示/隐藏四个 RP 的版本。
- Design process: 在线实验的设计过程包括：先创建实验网站并保持与现场网站一致的页面组织；进行两个试点研究（大学行为实验室和 MTurk）以验证并改进实验设计；用 1,000 名 MTurk 女性对产品评分作为 Slope-One 算法的输入；第二阶段将参与者随机分配到显示/隐藏推荐和重定向/通用推荐条件。该过程是实验操纵设计，而非迭代式产品设计，但包含了试点验证和原型实现。
- Potential coding-agent design value: 该来源方法可帮助学习如何构建一个用于功能对比的有界交互原型：在简单 Web 应用中随机分配两种面向个体的策略（如基于用户历史的推荐 vs 通用推荐），并通过众包用户行为数据评估策略在不同用户阶段的效果，从而为编码智能体的个性化推荐/提示功能提供可复现的实验范式。
- Decision: 三项条件均满足：个体消费者在可运行的实验电商网站上独立使用推荐功能；作者从零构建了有界原型并实现了两种推荐策略的随机展示；在线实验所需的 Web 开发、众包评分和参与者招募对小型学术团队可行。现场实验虽依赖企业，但不影响对作者自建原型可行性的判断。
- Confidence: 0.72

## A probabilistic Bayesian inference model to investigate injury severity in automobile crashes

- Year/journal: 2021 / Decision Support Systems
- DOI: 10.1016/j.dss.2021.113557
- Artifact: WebSimulator
- Individual user/task: 决策者或非数据科学领域的主题专家通过网页模拟器输入事故相关变量（如车辆类型、行驶速度）的证据或信念，进行 what-if 分析，查看不同损伤严重度等级的概率及变量间依赖关系。
- Design delta: 将事故严重度贝叶斯网络模型封装为交互式 what-if 推理工具，提供变量证据输入、概率更新和可视化网络；相比纯算法/模型，增加了面向非技术用户的网页界面和交互查询能力。
- Design process: 作者未描述面向用户的软件设计流程；模拟器内容由贝叶斯网络模型驱动。模型构建过程包括多源数据合并、贝叶斯随机条件插补处理缺失值、交叉熵损失处理类别不平衡、TAN结构学习、十折交叉验证，并借助文献、统计分析和领域专家意见选择与编码变量。
- Potential coding-agent design value: 该来源可帮助学习如何将训练好的概率模型包装为面向个人用户的交互式 what-if 网页工具，为编码代理的推断结果提供可操作、可解释的用户界面。
- Decision: 三项条件均满足：模拟器面向个体决策者；作者将贝叶斯网络模型配置为可公开访问的网页交互式推理工具；使用公开数据和现有工具，无需组织合作或重型基础设施。但软件设计细节较少，故置信度中等。
- Confidence: 0.62
