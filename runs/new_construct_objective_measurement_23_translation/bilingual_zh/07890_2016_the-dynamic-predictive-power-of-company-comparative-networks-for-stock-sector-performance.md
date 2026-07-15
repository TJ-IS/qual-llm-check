---
otero_id: 7890
otero_key: "H2Y9VY8C"
title: "The dynamic predictive power of company comparative networks for stock sector performance"
authors: "Kun Chen; Peng Luo; Dongming Xu; Huaiqing Wang"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.07.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The dynamic predictive power of company comparative networks for stock sector performance




---
奥特罗 ID：7890
otero_key: "H2Y9VY8C"
标题：“公司比较网络对股票行业表现的动态预测能力”
作者：“陈坤、罗鹏、徐东明、王怀庆”
年份：“2016”
期刊：《信息与管理》
doi：“10.1016/j.im.2016.07.005”
查询：“构造”
来源：“https://ais.kexu.win”
图片下载：假
---
# 公司比较网络对股票行业表现的动态预测能力


Kun Chen<sup>a,</sup>\*, Peng Luo<sup>b</sup>, Dongming Xu<sup>c</sup>, Huaiqing Wang<sup>a</sup>




陈坤<sup>a,</sup>\*、罗鹏<sup>b</sup>、徐东明<sup>c</sup>、王怀庆<sup>a</sup>


<sup>a</sup> Department of Finance, South University of Science and Technology, Shenzhen 518055, China




<sup>a</sup> 南方科技大学金融系, 深圳 518055


<sup>b</sup> School of Management, Harbin Institute of Technology, Harbin 150001, China




<sup>b</sup> 哈尔滨工业大学管理学院, 哈尔滨 150001


<sup>c</sup> UQ Business School, The University of Queensland, St Lucia, QLD 4072, Australia




<sup>c</sup> 昆士兰大学昆士兰大学商学院，圣卢西亚，QLD 4072，澳大利亚


## A R T I C L E I N F O




（代码、公式、图片引用或其他非语言内容，无需翻译。）


Article history: Received 4 July 2015 Received in revised form 13 June 2016 Accepted 19 July 2016 Available online xxx




文章历史记录： 收到日期 2015 年 7 月 4 日 收到修订版 2016 年 6 月 13 日 接受 2016 年 7 月 19 日 在线提供 xxx


Keywords: Company network Sentiment analysis Vector autoregression Stock sector performance




关键词： 公司网络 情感分析 向量自回归 股票板块表现


## A B S T R A C T




（代码、公式、图片引用或其他非语言内容，无需翻译。）


As economic integration and business connections increase, companies actively interact with each other in the market in cooperative or competitive relationships. To understand the market network structure with company relationships and to investigate the impacts of market network structure on stock sector performance, we propose the construct of a company comparative network based on public media data and sector interaction metrics based on the company network. All the market network structure metrics are integrated into a vector autoregression model with stock sector return and risk. Several <sup>fi</sup>ndings demonstrate the dynamic relationships that exist between sector interactions and sector performance. First, sector interaction metrics constructed based on company networks are signi<sup>fi</sup>cant leading indicators of sector performance. Interestingly, the interactions between sectors have greater predictive power than those within sectors. Second, compared with the company closeness network, the company comparative network, which labels the cooperative or competitive relationships between companies, is a better construct to understand and predict sector interactions and performance. Third, competitive company interactions between sectors impact sector performance in a slower manner than cooperative company interactions. The <sup>fi</sup>ndings enrich <sup>fi</sup>nancial studies regarding asset pricing by providing additional explanations of company/sector interactions and insights into company management using industry-level strategies.




随着经济一体化和商业联系的增加，企业在市场上积极互动，形成合作或竞争关系。为了理解具有公司关系的市场网络结构，并研究市场网络结构对股票行业绩效的影响，我们提出基于公共媒体数据和基于公司网络的行业互动指标构建公司比较网络。所有市场网络结构指标都集成到具有股票行业回报和风险的向量自回归模型中。多项<sup>调查</sup>证明了行业互动与行业绩效之间存在的动态关系。首先，基于公司网络构建的行业互动指标是行业绩效的重要领先指标。有趣的是，部门之间的相互作用比部门内部的相互作用具有更大的预测能力。其次，与公司紧密度网络相比，公司比较网络标记了公司之间的合作或竞争关系，是理解和预测行业互动和绩效的更好的结构。第三，行业之间的竞争性公司互动对行业绩效的影响比合作性公司互动慢。通过提供对公司/部门互动的额外解释以及使用行业级策略对公司管理的见解，<sup>调查结果</sup>丰富了有关资产定价的<sup>财务</sup>研究。


ã 2016 Elsevier B.V. All rights reserved.




ã 2016 Elsevier B.V. 保留所有权利。


## 1. Introduction




## 1.简介


As economic integration and business connections increase, companies actively interact with each other in the market in cooperative or competitive relationships. Such relationships often exhibit industry-related features. For example, competitive relationships often exist within an industry because of limited resources and customers. These cooperative relationships usually arise between the supply and demand sides across different industries. Complex interactive business relationships depict the economic market with intra-sector and cross-sector links. These links are helpful for understanding information and shock transfers within and across sectors [1–3]. For example, the spillover effect between sectors was observed during the global <sup>fi</sup>nancial crisis and the recent Chinese stock market crash. Consider the manufacturing sector and the utility sector in the Chinese stock market. Between June and July 2015, the manufacturing sector index<sup>1</sup> decreased by 29.96%, and the utility sector index decreased by 24.93%. The manufacturing sector suffered a much heavier loss than the utility sector. In market interactions, companies in the manufacturing sector have more business connections with other companies than companies in the utility sector. To understand market interactive structures and to explain the spillover effect between sectors, we designed this study.




随着经济一体化和商业联系的增加，企业在市场上积极互动，形成合作或竞争关系。这种关系通常表现出与行业相关的特征。例如，由于资源和客户有限，行业内经常存在竞争关系。这些合作关系通常发生在不同行业的供需双方之间。复杂的互动业务关系描绘了具有部门内和跨部门联系的经济市场。这些链接有助于理解部门内部和部门之间的信息和冲击转移[1-3]。例如，在全球金融危机和最近的中国股市崩盘期间，就观察到了行业之间的溢出效应。考虑一下中国股市的制造业和公用事业部门。 2015 年 6 月至 7 月期间，制造业指数<sup>1</sup>下降了 29.96%，公用事业指数下降了 24.93%。制造业的损失远大于公用事业部门。在市场互动中，制造业企业与其他企业的业务联系多于公用事业企业。为了了解市场互动结构并解释行业之间的溢出效应，我们设计了这项研究。


Previous accounting and <sup>fi</sup>nance studies have begun to establish the connection between market network structure and stock sector performance [1–3]. They have used trading data to create sector relationship graphs, and they have proposed the theory that sectoral shocks are transmitted to other sectors using networks of input and output linkages. However, the trade <sup>fl</sup>ow graphs are rather coarse tools for describing company relationships. In the <sup>fi</sup>eld of information systems (IS), some studies have




之前的会计和金融研究已经开始建立市场网络结构和股票行业绩效之间的联系[1-3]。他们利用交易数据创建部门关系图，并提出了部门冲击通过输入和输出联系网络传递到其他部门的理论。然而，贸易<sup>流</sup>图是描述公司关系的相当粗糙的工具。在信息系统（IS）领域，一些研究已经


K. Chen et al. / Information & Management xxx (2016) xxx–xxx




K.陈等人。 / 信息与管理 xxx (2016) xxx–xxx


constructed company relationship networks based on textual information mining. They have identi<sup>fi</sup>ed the co-occurrences of two companies’ names in documents [4–8]. This method helps to measure the closeness of two companies, but it cannot specify the types of comparative relationship, i.e., competitive relations or cooperative relations. In a real-world market, the relationship between Apple and Samsung is de<sup>fi</sup>nitely different from that between Apple and FoxCom. These different relationships have different spillover effects on stock performance. Therefore, to further investigate the connections between market network structure and stock sector performance, we focus on the following research questions.




基于文本信息挖掘构建公司关系网络。他们在文档中发现了两家公司名称的共现情况 [4-8]。该方法有助于衡量两个公司的紧密程度，但无法指定比较关系的类型，即竞争关系或合作关系。在现实市场中，苹果和三星之间的关系与苹果和富士康之间的关系截然不同。这些不同的关系对股票表现有不同的溢出效应。因此，为了进一步探讨市场网络结构与股票行业绩效之间的联系，我们重点关注以下研究问题。


(1) Does the company comparative network provide a stronger market indicator than the company closeness network?




(1) 公司比较网络是否比公司紧密度网络提供更强的市场指标？


(2) What are the intra-sector and inter-sector network effects on stock sector performance?




(2) 行业内和行业间的网络效应对股票行业绩效有何影响？


(3) What are the dynamics of the relationship between company comparative network metrics and stock sector performance?




(3) 公司比较网络指标与股票行业绩效之间的关系动态如何？


To answer these questions, we use public news<sup>2</sup> as a data source to build company networks because we believe that as an easily accessed Web-based data source, news describes richer business relationships between companies than simple trading data. Moreover, to identify network effects, we construct complex network metrics. First, we use comparative analysis, rather than co-occurrence analysis, to investigate the cooperative (positive) and competitive (negative) relationships identi<sup>fi</sup>ed by public information. Second, we construct inter-sector and intra-sector measurements to compare their different effects.




为了回答这些问题，我们使用公共新闻<sup>2</sup>作为构建公司网络的数据源，因为我们相信新闻作为一种易于访问的基于网络的数据源，比简单的交易数据描述了更丰富的公司之间的业务关系。此外，为了识别网络效应，我们构建了复杂的网络指标。首先，我们使用比较分析，而不是共现分析，来调查公共信息所识别的合作（正向）和竞争（负向）关系。其次，我们构建部门间和部门内的衡量标准来比较它们的不同效果。


In contrast to previous studies that aimed to detect the static correlations between company network and stock performances, our study uses a vector autoregression with exogenous variables (VARX) model to consider all of the intricate dynamic relationships among network metrics and stock sector performance. The timeseries model investigates continuous daily company network effects on stock sector performance, and it captures the dynamics of short- and long-term carryover effects over time.




与之前旨在检测公司网络和股票表现之间静态相关性的研究相比，我们的研究使用外生变量向量自回归（VARX）模型来考虑网络指标和股票行业表现之间所有复杂的动态关系。时间序列模型研究了公司网络对股票行业表现的连续日常影响，并捕捉了短期和长期结转效应随时间的动态变化。


This study has potential implications for theory and practice. Theoretically, our work con<sup>fi</sup>rms and extends <sup>fi</sup>nancial theories by introducing rich market network structure metrics based on public information. We use a time-series model to investigate the dynamic relationships between company comparative networks and stock sector performance. Our research also provides practical suggestions for sector-level strategies such as industry associations and investments.




这项研究对理论和实践具有潜在的影响。从理论上讲，我们的工作通过引入基于公共信息的丰富的市场网络结构指标来证实并扩展了<sup>金融</sup>理论。我们使用时间序列模型来研究公司比较网络与股票行业绩效之间的动态关系。我们的研究还为行业协会和投资等行业层面的战略提供了实用的建议。


We <sup>fi</sup>rst describe the theoretical background and hypotheses in Section 2. Section 3 introduces the data and the measurements. Section 4 describes the time-series model. The <sup>fi</sup>ndings are presented in Section 5. The <sup>fi</sup>nal section discusses the implications.




我们首先在第 2 节中描述理论背景和假设。第 3 节介绍数据和测量结果。第 4 节描述了时间序列模型。 <sup>最终结果</sup>在第 5 节中介绍。<sup>最后</sup>部分讨论了其影响。


## 2. Theoretical background and hypotheses




## 2.理论背景和假设


2.1. Intra-sector and inter-sector network effects on stock sector performance




2.1.行业内和行业间网络对股票行业绩效的影响


Stock sector performance has been demonstrated to be related to sector positions in market networks. In the <sup>fi</sup>nance domain, Aobdia, Caskey, and Ozel [3] constructed an industry network based on trade <sup>fl</sup>ows across different industries, and they found that <sup>fi</sup>rms in central industries are more exposed to systemic risks than other <sup>fi</sup>rms. Acemoglu et al. [1] argued that sectoral risks can be transmitted to other sectors through a network of input and output linkages in a system. Ahern and Harford [2] demonstrated that systematic risks constitute the aggregation of idiosyncratic shocks and that more central sectors in a network of intersectoral trade usually have higher returns because they experience greater exposure to systematic risks.




股票行业的表现已被证明与市场网络中的行业地位相关。在金融领域，Aobdia、Caskey和Ozel[3]基于不同行业的贸易流构建了行业网络，他们发现中心行业的企业比其他企业更容易受到系统性风险的影响。阿塞莫格鲁等人。 [1]认为部门风险可以通过系统中的输入和输出联系网络传递到其他部门。 Ahern 和 Harford [2] 证明，系统性风险构成了特殊冲击的聚合，并且部门间贸易网络中越中心的部门通常具有更高的回报，因为它们承受的系统性风险更大。


Because of the popularity of social media and Web 2.0, company interactions regarding sales, debts, and other <sup>fi</sup>nancial or operating activities are reported in public news in real time. Company networks based on keyword co-occurrence have been widely used to explain and predict <sup>fi</sup>nancial metrics such as company revenue; stock return; and risk. For example; Ma; Sheng; and Pant [6] predicted company revenue relationships based on a company network derived from company citations. Graph-theoretic measurements were used in the classi<sup>fi</sup>cation problem. Jin et al. [5] developed complex longitudinal features for company network evolution and proposed feature selection and prediction models to predict company pro<sup>fi</sup>t and revenue growth. Focusing on stock market performance; Creamer; Ren; and Nickerson [9] tested the relationships among company positions in networks; company stock returns; and volatility.




由于社交媒体和 Web 2.0 的普及，有关销售、债务和其他<sup>财务</sup>或运营活动的公司互动都会在公共新闻中实时报道。基于关键词共现的公司网络已被广泛用于解释和预测财务指标，例如公司收入；股票回报；和风险。例如;马;盛;和 Pant [6] 根据公司引用得出的公司网络预测了公司收入关系。图论测量用于分类问题。金等人。 [5] 为公司网络演化开发了复杂的纵向特征，并提出了特征选择和预测模型来预测公司利润和收入增长。关注股市表现；奶精；任； Nickerson [9] 测试了网络中公司职位之间的关系；公司股票回报；和波动性。


We expect that constructing sector-related metrics based on company networks might also provide a useful indicator for predicting sector performance. Compared with trade <sup>fl</sup>ow, which has been used in previous <sup>fi</sup>nancial studies [2,3], company networks encompass broader business relationships between companies.




我们预计，基于公司网络构建行业相关指标也可能为预测行业绩效提供有用的指标。与之前的<sup>财务</sup>财务研究中使用的贸易<sup>流</sup>流相比[2,3]，公司网络涵盖了公司之间更广泛的业务关系。


H1a. Sector interaction metrics constructed based on company networks have signi<sup>fi</sup>cant predictive relationships with sector performance.




H1a。基于公司网络构建的部门互动指标与部门绩效具有显着的预测关系。


To further investigate the sector-interactive characteristics, we construct two metrics: an inter-sector metric and an intra-sector metric. These two metrics have primarily been used in economics to distinguish trades between different industries or within the same industry [10,11]. These sector metrics have also been used in <sup>fi</sup>nancial studies that have investigated stock performances. Moskowitz and Grinblatt [12] and Aobdia, Caskey, and Ozel [3] demonstrated that inter-sector characteristics have predictive power for assessing <sup>fi</sup>rms’ stock returns. Conversely, Asness, Porter, and Stevens [13] found that intra-sector momentum is superior to inter-sector momentum in explaining stock returns. Because this study aims to inspect how sector-interactive characteristics affect stock returns, we followed the two popular metrics and proposed two competing hypotheses:




为了进一步研究部门交互特征，我们构建了两个指标：部门间指标和部门内指标。这两个指标主要在经济学中用于区分不同行业之间或同一行业内的交易[10,11]。这些行业指标也被用于调查股票表现的金融研究中。 Moskowitz 和 Grinblatt [12] 以及 Aobdia、Caskey 和 Ozel [3] 证明，行业间特征对于评估企业股票回报具有预测能力。相反，Asness、Porter 和 Stevens [13] 发现，在解释股票回报方面，行业内动量优于行业间动量。由于本研究旨在考察行业互动特征如何影响股票回报，因此我们遵循两个流行的指标并提出了两个相互竞争的假设：


H1b. The inter-sector metric has greater predictive power than the intra-sector metric.




H1b。扇区间度量比扇区内度量具有更大的预测能力。


H1b’. The intra-sector metric has greater predictive power than the inter-sector metric.




H1b’。扇区内度量比扇区间度量具有更大的预测能力。


## 2.2. Company comparative networks provide a stronger market indicator than closeness networks




## 2.2.公司比较网络提供比亲密网络更强的市场指标


In the business world, company comparative analysis refers to evaluating a list of company metrics to compare them. The targets are usually similar companies in the same industry, such as Ford versus Toyota and eBay versus Amazon. In IS and marketing research, comparative analysis has been extended to the analysis of comparative opinions between two entities [14–16]. Taking products as an example, comparative analysis aims to identify the relationship of two products as “product A is better than product B” or “product B is better than product A.” For example, Jindal and Liu [17,18] proposed using rules and naïve Bayes classi<sup>fi</sup>ers to identify comparative sentences and relationships in these sentences. Xu et al. [19] used a conditional random <sup>fi</sup>eldbased method to extract the comparative relationships between products from a sentence. Zhang et al. [8] proposed a sentiment analysis method for constructing product comparison networks on a coarse-granularity level. In a company analysis scenario, comparative analysis refers to identifying the relationships between companies, including competitive relationships and cooperative relationships. These relations are often hidden in news reports and other public information. Similar to previous sentiment analysis, competitive relationships usually exhibit negative comparative opinions, and cooperative relationships often feature positive comparative opinions.




在商业领域，公司比较分析是指评估一系列公司指标以进行比较。目标通常是同一行业的类似公司，例如福特与丰田、eBay 与亚马逊。在信息系统和营销研究中，比较分析已扩展到两个实体之间的比较意见分析[14-16]。以产品为例，比较分析的目的是识别两个产品的关系为“产品A优于产品B”或“产品B优于产品A”。例如，Jindal 和 Liu [17,18] 提出使用规则和朴素贝叶斯分类器来识别比较句子以及这些句子中的关系。徐等人。 [19]使用基于条件随机<sup>领域</sup>的方法从句子中提取产品之间的比较关系。张等人。 [8]提出了一种在粗粒度级别上构建产品比较网络的情感分析方法。在公司分析场景中，比较分析是指识别公司之间的关系，包括竞争关系和合作关系。这些关系往往隐藏在新闻报道和其他公共信息中。与之前的情感分析类似，竞争关系通常表现出消极的比较观点，而合作关系通常表现出积极的比较观点。


Although company comparative relationship networks are assumed to constitute a good market indicator, there is little evidence that supports this assumption. Inter-company relationships are currently extracted from textual news based on the cooccurrence of company names. The more frequently the documents mention two companies together, the closer those companies are to each other. This line of reasoning stems from the notion of memory-associative networks [20], and it has strong roots in the co-word analysis literature [21]. Company cooccurrence networks have been used to analyze company <sup>fi</sup>nancial performance.




尽管公司比较关系网络被认为构成了良好的市场指标，但几乎没有证据支持这一假设。目前，公司间关系是根据公司名称的共现性从文本新闻中提取的。文件中提及两家公司的次数越多，这些公司之间的关系就越密切。这种推理源于记忆关联网络的概念[20]，并且在共词分析文献[21]中有着深厚的根源。公司共现网络已用于分析公司<sup>财务</sup>财务绩效。


On the basis of above analysis, we want to build a company comparative network and compare its market predictive power with that of a company co-occurrence network. Thus, the following hypothesis is posited.




在上述分析的基础上，我们想要构建一个公司比较网络，并将其市场预测能力与公司共现网络进行比较。因此，提出以下假设。


H2a. Company comparative analysis provides a stronger sector interactive indicator than company closeness analysis.




H2a。公司比较分析提供了比公司紧密度分析更强的行业互动指标。


To further investigate the sentiment of comparative opinions, we divide company comparative relationships into two categories: cooperative (or positive) relationships and competitive (or negative) relationships. Sentiment analysis has been widely adopted in <sup>fi</sup>nancial studies to predict stock prices [22]. One research stream uses the polarity value of news as a predictive measure of stock performance, e.g., Li et al. [23], Yu, Duan, and Cao [24], and Tetlock, Saar-Tsechansky, and Macskassy [25]. The other stream inspects the differential impacts of positive and negative news on stocks. For example, Chan [26] found less drift for stocks with good news than for those with bad news. Van [27] found that arrival of bad news had a greater impact on volatility than did arrival of good news. This study aims to investigate whether a difference exists between the impact of cooperative (positive) relationships and competitive (negative) relationships. Thus, we propose the following competing hypotheses.




为了进一步研究比较意见的情绪，我们将公司比较关系分为两类：合作（或积极）关系和竞争（或消极）关系。情绪分析已广泛应用于金融研究中来预测股票价格[22]。一个研究流使用新闻的极性值作为股票表现的预测指标，例如，Li 等人。 [23]，Yu、Duan 和 Cao [24]，以及 Tetlock、Saar-Tsechansky 和 ​​Macskassy [25]。另一个流检查正面和负面消息对股票的不同影响。例如，Chan [26] 发现，有好消息的股票比有坏消息的股票漂移更小。 Van [27]发现坏消息的到来对波动性的影响比好消息的到来更大。本研究旨在调查合作（积极）关系和竞争（消极）关系的影响之间是否存在差异。因此，我们提出以下相互竞争的假设。


H2b. Cooperative (positive) sector interactive metrics have greater predictive power than competitive (negative) sector interactive metrics.




H2b。合作（积极）部门互动指标比竞争（消极）部门互动指标具有更大的预测能力。


H2b . Competitive (negative) sector interactive metrics have greater predictive power than cooperative (positive) sector interactive metrics.




H2b。竞争性（消极）部门互动指标比合作（积极）部门互动指标具有更大的预测能力。


## 2.3. The dynamics of the predictive value of company comparative networks




## 2.3。公司比较网络预测价值的动态


The previous literature has demonstrated the dynamics of stock market responses to word-of-mouth information and social media Luo, Zhang, and Duan [28] compared the short- and long-term effects of social media with those of conventional online behavioral metrics on a <sup>fi</sup>rm’s equity values. They found that social media metrics have faster predictive value. Additionally, Tirunillai and




先前的文献已经证明了股票市场对口碑信息和社交媒体的反应动态。Luo、Zhang 和 Duan [28] 将社交媒体与传统在线行为指标对公司股权价值的短期和长期影响进行了比较。他们发现社交媒体指标具有更快的预测价值。此外，蒂鲁尼莱和


Tellis [29] demonstrated that negative user reviews are related to stock returns, with signi<sup>fi</sup>cant wear-in effects. In dynamic analysis, the wear-in time, which is de<sup>fi</sup>ned as the time required to reach the peak predictive value, is valuable because it suggests a critical time period for decision-making, whereas the wear-out time, which is de<sup>fi</sup>ned as the time required before the predictive value reaches asymptotes, indicates the impact duration.




Tellis [29] 证明，负面用户评论与股票回报相关，具有显着的磨损效应。在动态分析中，磨合时间定义为达到峰值预测值所需的时间，它很有价值，因为它表明了决策的关键时间段，而磨损时间定义为预测值达到渐近线之前所需的时间，表明了影响持续时间。


Theoretically, the information diffusion model [30] has been widely used in the <sup>fi</sup>nance domain to explain the dynamic effects of information on stock returns. Hong et al. [31] demonstrated that bad news travels slowly through the investing public. Chan [26] also found that prices are slow to re<sup>fl</sup>ect bad public news. This study aims to investigate the differences in wear-in and wear-out effects on competitive and cooperative relationships. Thus, we propose the following two groups of competing hypotheses.




理论上，信息扩散模型[30]已广泛应用于金融领域来解释信息对股票收益的动态影响。洪等人。 [31]表明坏消息在投资大众中传播缓慢。 Chan [26] 还发现，价格对负面公共消息的反应速度很慢。本研究旨在调查磨损和磨损对竞争和合作关系影响的差异。因此，我们提出以下两组相互竞争的假设。


H3a. Cooperative (positive) sector interactive metrics have a shorter wear-in time than competitive (negative) sector interactive metrics.




H3a。合作（积极）部门互动指标比竞争（消极）部门互动指标的磨合时间更短。


H3a . Competitive (negative) sector interactive metrics have a shorter wear-in time than cooperative (positive) sector interactive metrics.




H3a。竞争性（消极）部门互动指标比合作（积极）部门互动指标的磨合时间更短。


H3b. Cooperative (positive) sector interactive metrics have a longer wear-out time than competitive (negative) sector interactive metrics.




H3b。合作（正）部门交互指标比竞争（负）部门交互指标具有更长的磨损时间。


H3b . Competitive (negative) sector interactive metrics have a longer wear-out time than cooperative (positive) sector interactive metrics.




H3b。竞争性（消极）部门互动指标比合作（积极）部门互动指标具有更长的磨损时间。


## 3. Data and measurements




## 3. 数据和测量


## 3.1. Data processing




## 3.1.数据处理


The raw data set consists of one year (2013) of Chinese business news for 300 companies in the Shanghai–Shenzhen 300 Index.<sup>3</sup> These companies span 10 sectors<sup>4</sup> within the Chinese stock market, including materials, <sup>fi</sup>nance, energy, and daily consumption, among others. The news stories are collected from a general search portal,<sup>5</sup> which covers 3000+ online sources, including discussion boards, news wires, and blogs. To obtain a clear overview of the information sources, we focus on the top 100 online news sources ranked by a number of news items. We <sup>fi</sup>nd that the top 100 online news sources cover 76.89% of the total news items online (the total number of news items is 946,935). Among these sources, we identify 74 news websites, 21 discussion boards, and 5 blogs. Discussion boards have the largest number of news items because anyone can freely post opinions about companies or stocks on discussion boards. From the 74 news websites, we con<sup>fi</sup>rm that the major Chinese <sup>fi</sup>nancial web media is covered. It includes government-operated media, such as renmin.com and xinhua.com, and 4 major security newspapers in China (cs.com.cn, cnstock.com, p52.net, and zqrb.ccstock.cn). The websites also include some popular <sup>fi</sup>nancial portals such as ifeng.com, hexun. com, jinrongjie.com, eastmony.com, business.sohu.com, and <sup>fi</sup>- nance.sina.com.cn. In this paper, we want to use a broad range of big data to identify company relationships. Both regular news and rumors are important for investigating the impact of market information. Therefore, we use a variety of news sources.




原始数据集包含沪深 300 指数中 300 家公司一年（2013 年）的中国商业新闻。<sup>3</sup>这些公司涵盖中国股市的 10 个板块<sup>4</sup>，包括材料、<sup>金融</sup>能源和日常消费等。这些新闻故事是从通用搜索门户<sup>5</sup>收集的，该门户涵盖 3000 多个在线资源，包括讨论区、新闻专线和博客。为了获得对信息来源的清晰概览，我们重点关注按新闻数量排名的前 100 名在线新闻来源。我们<sup>发现</sup>排名前100位的网络新闻源覆盖了网络新闻总数的76.89%（新闻总数为946,935条）。在这些来源中，我们确定了 74 个新闻网站、21 个讨论区和 5 个博客。讨论区拥有最多的新闻条目，因为任何人都可以在讨论区自由发表有关公司或股票的观点。从74家新闻网站中，我们确认覆盖了中国主要的财经网络媒体。包括人民网、新华网等官办媒体，以及中国四大证券报纸（cs.com.cn、cnstock.com、p52.net、zqrb.ccstock.cn）。这些网站还包括一些流行的金融门户网站，例如凤凰网、和讯网。 com、金融街网、东方财富网、搜狐商业网和<sup>fi</sup>-nance.sina.com.cn。在本文中，我们希望使用广泛的大数据来识别公司关系。常规新闻和谣言对于调查市场信息的影响都很重要。因此，我们使用各种新闻来源。


In the next step, we perform data clearing to delete repeated or forwarded news. According to the ef<sup>fi</sup>cient market hypothesis (EMH) [32], <sup>fi</sup>nancial markets respond to market information in an ef<sup>fi</sup>cient manner. There are three forms of the EMH (the weak form, the semi-strong form, and the strong form), which differ in terms of the information that can be captured in a market (historical public information, current public information, and hidden information). In agreement with the EMH, we must identify the <sup>fi</sup>rst published news to determine the market time of information. In this step, we use the cosine similarity [33] to compare the similarity of documents. For each news item, we fetch documents within a 30-day time window before and after the news is published. With textual features and the cosine similarity, we compare the similarity of two documents. If the similarity between the two documents is greater than 90%, we assume that the two pieces of news are repeated or forwarded news. The one published later is then deleted. After this step, there are 363,421 news items remaining.




下一步，我们进行数据清理，删除重复或转发的新闻。根据有效市场假说（EMH）[32]，金融市场以有效的方式响应市场信息。有效市场假说有三种形式（弱形式、半强形式和强形式），其区别在于可以在市场中捕获的信息（历史公开信息、当前公开信息和隐藏信息）。根据 EMH 的规定，我们必须确定<sup>第一个</sup>发布的新闻，以确定信息的市场时间。在这一步中，我们使用余弦相似度[33]来比较文档的相似度。对于每条新闻，我们都会在新闻发布前后 30 天的时间窗口内获取文档。通过文本特征和余弦相似度，我们比较两个文档的相似度。如果两个文档之间的相似度大于90%，我们就假设这两条新闻是重复或转发的新闻。稍后发布的内容将被删除。此步骤之后，还剩下 363,421 条新闻。


To identify intercompany relationships, we <sup>fi</sup>rst exclude documents that only mention one company or mention more than <sup>fi</sup>ve companies because a document that includes many company names is less important than a document that mentions only a few companies [5]. There are 314,475 news items remaining. The next task is to locate target companies in news stories. In contrast to previous studies [6,7,9,24], which assume that news websites clearly label the news with a target company, we believe that labeling news stories is an important task for cases in which news is collected broadly from the Web. Therefore, we de<sup>fi</sup>ne several rules for identifying target companies. If a company name appears in the title, it is the target company. If no company name appears in the title, we determine the most frequently mentioned target companies by counting the number of times that company names occur.




为了识别公司间关系，我们首先排除仅提及一家公司或提及超过五家公司的文档，因为包含许多公司名称的文档不如仅提及少数公司的文档重要[5]。还剩 314,475 条新闻。下一个任务是在新闻报道中定位目标公司。与之前的研究[6,7,9,24]相比，这些研究假设新闻网站明确地为新闻贴上目标公司的标签，我们认为，对于从网络上广泛收集新闻的情况来说，标记新闻报道是一项重要任务。因此，我们定义了一些识别目标公司的规则。如果标题中出现公司名称，则为目标公司。如果标题中没有出现公司名称，我们通过统计公司名称出现的次数来确定最常被提及的目标公司。


In the subsequent step, we want to identify comparative opinions between companies using machine-learning methods. In the training procedure, we randomly select 3000 news items, which include 8980 sentences containing company names other than the target companies. Then, we manually label these sentences as depicting positive or negative relationships between the appearing company and the target company. The reasons for only using positive and negative labels have previously been summarized [24]. First, a sentence that includes subjective expressions always implies either positive or negative feelings, and “neutral” is a fairly vague concept. Second, no mature methods exist for ef<sup>fi</sup>ciently and accurately identifying neutral sentiments. Using the labeled dataset, we compute the area under the curve (AUC) [34] of different classi<sup>fi</sup>ers based on a 10-fold crossvalidation.




在下一步中，我们希望使用机器学习方法来确定公司之间的比较意见。在训练过程中，我们随机选择了3000条新闻，其中包括8980个包含目标公司以外的公司名称的句子。然后，我们手动将这些句子标记为描述出现的公司和目标公司之间的积极或消极关系。之前已经总结了仅使用正面和负面标签的原因[24]。首先，包含主观表达的句子总是暗示着积极或消极的感受，而“中性”是一个相当模糊的概念。其次，目前还没有成熟的方法来有效、准确地识别中性情绪。使用标记数据集，我们基于 10 倍交叉验证计算不同分类器的曲线下面积 (AUC) [34]。


The receiver operating characteristic (ROC) curve illustrates the performance of a binary classi<sup>fi</sup>er system as its discrimination threshold varies. The curve is created by plotting the true positive rate against the false positive rate at various threshold settings. A ROC curve closer to the top-left corner indicates better dynamic performance. How close the ROC curve is to the top-left corner can be re<sup>fl</sup>ected in the AUC measurement, which is also used as an evaluation metric in this paper.




接收器操作特性 (ROC) 曲线说明了二元分类器系统在判别阈值变化时的性能。该曲线是通过绘制不同阈值设置下的真阳性率与假阳性率来创建的。 ROC曲线越靠近左上角，表明动态性能越好。 ROC曲线与左上角的接近程度可以在AUC测量中反映出来，这也是本文的评估指标。


During implementation, we use the bag-of-words feature model,<sup>6</sup> apply information gain (IG)-based feature selection, and tune the thresholds to test different classi<sup>fi</sup>ers’ performances using different feature sizes. We experiment with several popular machine learning algorithms including support vector machines (SVM), decision trees, random forest, and naïve Bayes. The results are displayed in Fig. 1. From Fig. 1 (a), we <sup>fi</sup>nd that classi<sup>fi</sup>ers perform best on the top 820 features ordered by IG. These 820 features are selected when the threshold of IG is set to 0. Fig. 1 (b) shows that the performance of SVM is much better than that of the other classi<sup>fi</sup>ers $( \mathrm { A U C } _ { \mathrm { S V M } } = 0 . 8 0 3 6 ,$ $\mathsf { A U C } _ { \mathrm { D e c i s i o n \_ T r e e } } = 0 . 6 2 1 8$ ${ \sf A U C } _ { \mathrm { N a i v e \_ B a y e s } } = 0 . 7 0 5 8 ,$ $\mathsf { A U C } _ { \mathrm { R a n d o m \_ F o r e s t } } = 0 . 7 1 0 8 )$ . Therefore, we use the 820 features and train the SVM model to classify company comparative sentences. We identify 13,110 negative relationships and 182,970 positive relationships. The ratio between the positive and negative relationships is supported by previous studies of sentiment classi<sup>fi</sup>cation using user-generated content [29].




在实现过程中，我们使用词袋特征模型，<sup>6</sup>应用基于信息增益 (IG) 的特征选择，并调整阈值以测试不同分类器使用不同特征大小的性能。我们尝试了几种流行的机器学习算法，包括支持向量机 (SVM)、决策树、随机森林和朴素贝叶斯。结果如图 1 所示。从图 1 (a) 中，我们<sup>发现</sup>发现分类器在 IG 排序的前 820 个特征上表现最佳。这820个特征是在IG阈值设置为0时选择的。图1(b)表明SVM的性能远优于其他分类器 $( \mathrm { A U C } _ { \mathrm { S V M } } = 0 . 8 0 3 6 ,$ $\mathsf { A U C } _ { \mathrm {决策 \_ T re e } } = 0 . ${ \sf A U C } _ { \mathrm { N a i v e \_ Bayes } } = 0 . 7 0 5 8 ,$ $\mathsf { A U C } _ { \mathrm { R a n d o m \_ For e s t } } = 0 7 1 0 8 )$ 。因此，我们使用820个特征并训练SVM模型来对公司比较句进行分类。我们确定了 13,110 种消极关系和 182,970 种积极关系。之前使用用户生成内容进行情感分类的研究支持了积极关系和消极关系之间的比率[29]。


## 3.2. Network construction




## 3.2.网络建设


Each node in the network represents a company, and a direct link indicates a comparative relationship between two companies. The corresponding weight of each link indicates the sentiment strength of the comparison relationship. This network is formally de<sup>fi</sup>ned as follows.




网络中的每个节点代表一个公司，直接链接表示两个公司之间的比较关系。每个链接对应的权重表示比较关系的情感强度。该网络的正式定义如下。


Assume that each sentence in the news for target company c1, along with a mention of company c2, is mapped into a comparison tuple $\boldsymbol { \mathsf { t } } = \{ \mathsf { c } 1 , \mathsf { c } 2 , \mathsf { P } / \mathsf { N } \}$ , where P/N indicates that the comparative opinion from c2 to c1 is positive or negative.




假设目标公司 c1 的新闻中的每个句子以及提及公司 c2 都被映射到比较元组 $\boldsymbol { \mathsf { t } } = \{ \mathsf { c } 1 , \mathsf { c } 2 , \mathsf { P } / \mathsf { N } \}$ ，其中 P/N 表示 c2 到 c2 的比较意见c1 为正或负。


We consider the following methods of network construction.




我们考虑以下网络构建方法。


![](/api/attachments/H2Y9VY8C/fulltext/images/4b661a961d58bdc59c67396284da3c111988bd3d9d7f691705500f8a61bdd6ea.jpg)  
(a) AUC values for different classifiers and feature sizes




![](/api/attachments/H2Y9VY8C/fulltext/images/4b661a961d58bdc59c67396284da3c111988bd3d9d7f691705500f8a61bdd6ea.jpg)  
(a) 不同分类器和特征大小的 AUC 值


![](/api/attachments/H2Y9VY8C/fulltext/images/7384570b9b64033001aaf2f87563e022c0ac122eb68ea8c269683fb7bf9e54b4.jpg)  
(b) ROC curve for a feature size of 820  
Fig. 1. Experimental results for sentiment classi<sup>fi</sup>cation.




![](/api/attachments/H2Y9VY8C/fulltext/images/7384570b9b64033001aaf2f87563e022c0ac122eb68ea8c269683fb7bf9e54b4.jpg)  
(b) 特征尺寸为 820 的 ROC 曲线  
图 1. 情感分类的实验结果。


## 3.2.1. Company closeness (undirected) networks




## 3.2.1.公司紧密（无向）网络


All n tuples are aggregated to produce a single link with a weight. An edge between nodes c1 and c2 is introduced when $( N _ { p d } + N _ { n d } ) > 0 ,$ , and the weight of the link is $w = ( N _ { p d } + N _ { n d } ) ,$ <sup>ð þ</sup>where $N _ { p d }$ <sup>¼ ð þ</sup>denotes the number of positive sentences and $N _ { n d }$ denotes the number of negative sentences.




所有 n 个元组被聚合以生成具有权重的单个链接。当 $( N _ { p d } + N _ { n d } ) > 0 ,$ 时，在节点 c1 和 c2 之间引入一条边，并且链接的权重为 $w = ( N _ { p d } + N _ { n d } ) ,$ <sup>ð þ</sup>其中 $N _ { p d }$ <sup>¼ ð þ</sup>表示肯定句的数量，$N _ { n d }$表示否定句的数量。


## 3.2.2. Company comparative (directed) networks




## 3.2.2.公司比较（定向）网络


We construct two categories of directed networks: positive and negative networks. In a positive network, an edge from node c1 to $^ { c 2 }$ is introduced when $N _ { p d } > 0 ,$ and the weight is $w = N _ { p d } .$ Similarly, when $N _ { n d } > 0 ,$ , we can introduce a link from c1 to c2 and set the weight as $w = N _ { n d }$




我们构建两类有向网络：正向网络和负向网络。在正网络中，当 $N _ { p d } > 0 ,$ 时，引入从节点 c1 到 $^ { c 2 }$ 的边，权重为 $w = N _ { p d } .$ 类似地，当 $N _ { n d } > 0 ,$ 时，我们可以引入从 c1 到 c2 的边，并将权重设置为 $w = N _ { n d }$


## 3.3. Measurements




## 3.3。测量值


## 3.3.1. Measurements of stock sector performance




## 3.3.1.股票行业表现的衡量


On the basis of previous research [28,35], we use two common measures to determine sector performance: sector return and risk. Return or abnormal return refers to sector stock value beyond what is expected based on the stock market average. Risk, which refers to the vulnerability of sector stock value, can be measured as the standard deviation of the residuals of the returns as follows:




在先前研究的基础上[28,35]，我们使用两种常用的衡量指标来确定行业绩效：行业回报和风险。回报或异常回报是指行业股票价值超出股市平均水平的预期。风险是指行业股票价值的脆弱性，可以用收益残差的标准差来衡量，如下所示：


$R _ { i t } - R _ { f t } = \alpha _ { i } + \beta _ { i } \big ( R _ { m t } - R _ { f t } \big ) + \varepsilon _ { i t } , ( 2$ )where t is the subscript for the time period, $R _ { i t }$ is the return of stock i at time t, $R _ { m t }$ is the average market return represented by the Shanghai Security Exchange Composite Index, $R _ { f t }$ is the risk-free rate of return, $\alpha _ { i }$ is the intercept, and $\varepsilon _ { i t }$ is the model residual. Eq. (2) is processed for a rolling window of 250 trading days before the target day. The abnormal return of stock i (AR ) is measured as the difference between the observed return and the expected return, and the risk is the standard deviation of the model residuals as indicated below:




$R _ { i t } - R _ { f t } = \alpha _ { i } + \beta _ { i } \big ( R _ { m t } - R _ { f t } \big ) + \varepsilon _ { i t } , ( 2$ )其中 t 为时间段的下标，$R _ { i t }$ 为股票 i 在该时间点的收益t，$R _ { m t }$ 为上证综合指数代表的平均市场收益，$R _ { f t }$ 为无风险收益率，$\alpha _ { i }$ 为截距，$\varepsilon _ { i t }$ 为模型残差。等式。 (2) 针对目标日之前 250 个交易日的滚动窗口进行处理。股票 i 的异常收益（AR ）衡量为观测收益与预期收益之间的差值，风险是模型残差的标准差，如下所示：


$$
A R _ {i t} = \left(R _ {i t} - R _ {f t}\right) - \left(\alpha_ {i} + \beta_ {i} \left(R _ {m t} - R _ {f t}\right)\right). \tag {3}
$$




$$
A R _ {i t} = \left(R _ {i t} - R _ {f t}\right) - \left(\alpha_ {i} + \beta_ {i} \left(R _ {m t} - R _ {f t}\right)\right)。 \标记{3}
$$


## 3.3.2. Measurements of sector interaction metrics




## 3.3.2.部门互动指标的测量


The modularity is de<sup>fi</sup>ned as the fraction of edges that fall within the communities minus the expected value of the same quantity if the edges are assigned at random, conditional on the given community memberships and the degree of the vertices [36]. In previous research, the modularity has primarily been used for evaluating community detection [37,38]. This study introduces the modularity to measure the strength of the connection between the nodes within (or between) groups. We divide stocks into different groups based on the sector to which they belong, and we use the modularity to calculate the intra- and inter-group interactions. When computing the interactions of two groups, we treat the two groups as a whole to yield the modularity value of the entire group.




模块化被定义为落在社区内的边的分数减去相同数量的期望值（如果边是随机分配的，条件是给定的社区成员资格和顶点的度数）[36]。在之前的研究中，模块化主要用于评估社区检测[37,38]。本研究引入了模块化来衡量组内（或组间）节点之间的连接强度。我们根据股票所属的行业将股票分为不同的组，并使用模块化来计算组内和组间的相互作用。在计算两个组的交互时，我们将两个组视为一个整体，以得出整个组的模块化值。


In the comparative (directed) network, let $c _ { i }$ be the community to which node i is assigned and let $\begin{array} { r } { \boldsymbol { w _ { i } ^ { i n } } = \sum _ { j } \boldsymbol { w _ { j i } } , \boldsymbol { w _ { i } ^ { o u t } } = \sum _ { j } \boldsymbol { w _ { i j } } } \end{array}$ . Then the modularity Q is given by Leicht and Newman [39] as follows:




在比较（有向）网络中，设 $c _ { i }$ 为节点 i 分配到的社区，并设 $\begin{array} { r } { \boldsymbol { w _ { i } ^ { i n } } = \sum _ { j } \boldsymbol { w _ { j i } } , \boldsymbol { w _ { i } ^ { o u t } } = \sum _ { j } \boldsymbol { w _ { i j } } } \end{array}$ 。那么模块性 Q 由 Leicht 和 Newman [39] 给出如下：


$\begin{array} { r } { Q = \frac { 1 } { m } { \displaystyle \sum _ { i j } } \bigg [ w _ { i j } - \frac { w _ { j } ^ { i n } w _ { i } ^ { o u t } } { m } \bigg ] \delta ( c _ { i } , c _ { j } ) } \end{array}$ <sub>;(4)where the</sub> d <sub>function</sub> $\delta ( u , v )$ is




$\begin{array} { r } { Q = \frac { 1 } { m } { \displaystyle \sum _ { i j } } \bigg [ w _ { i j } - \frac { w _ { j } ^ { i n } w _ { i } ^ { o u t } } { m } \bigg ] \delta ( c _ { i } , c _ { j } ) } \end{array}$ <sub>;(4)其中</sub> d <sub>函数</sub> $\delta ( u , v )$ 是


1 if $u = v$ and 0 otherwise, and $\begin{array} { r } { m = \sum _ { i j } w _ { i j } } \end{array}$ is the sum of the weights in the entire network.




如果 $u = v$ 则为 1，否则为 0，$\begin{array} { r } { m = \sum _ { i j } w _ { i j } } \end{array}$ 是整个网络中权重的总和。


This formula for the modularity is adjusted to measure the intra- and inter-sector interactions as follows:




调整模块化公式以衡量部门内和部门间的相互作用，如下所示：


$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{5}
$$




$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{5}
$$


$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})\tag{6}
$$




$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} ^ {i n} w _ {i} ^ {o u t}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})\tag{6}
$$


where $\delta ^ { \prime } ( c _ { i } , c _ { j } )$ is 1 when the two stocks i and j belong to the same sector; otherwise, the value is 0. The value of function $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ equals 1 if the two stocks belong to the two target sectors for which we want to calculate the value of inter-sector interactions; otherwise, the value is 0. In the closeness (undirected) network, according to Newman [40], we can measure the intra- and intersector closeness by replacing the w<sup>in</sup> or $w _ { i } ^ { o u t }$ with the sum of the weights that link node i $\begin{array} { r } { ( w _ { i } = \sum _ { j } w _ { i j } ) } \end{array}$ in Eqs. (5) and (6). The algorithms are presented as follows:




其中，当 i 和 j 两只股票属于同一板块时，$\delta ^ { \prime } ( c _ { i } , c _ { j } )$ 为 1；如果两只股票属于我们要计算行业间相互作用值的两个目标行业，则函数 $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ 的值为 1；否则值为 0。否则，值为 0。在紧密度（无向）网络中，根据 Newman [40]，我们可以通过将 w<sup>in</sup> 或 $w _ { i } ^ { o u t }$ 替换为链接节点 i 的权重之和 $\begin{array} { r } { ( w _ { i } = \sum _ { j } w _ { i 来测量扇区内和扇区间的紧密度j } ) } \end{array}$ 在等式中。 （5）和（6）。算法如下：


$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{7}
$$




$$
Q _ {x} ^ {\prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime} (c _ {i}, c _ {j})\tag{7}
$$


$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})
$$




$$
Q _ {x y} ^ {\prime \prime} = \frac {1}{m} \sum_ {i j} \left[ w _ {i j} - \frac {w _ {j} w _ {i}}{m} \right] \delta^ {\prime \prime} (c _ {i}, c _ {j})
$$


8




（代码、公式、图片引用或其他非语言内容，无需翻译。）


where $m = 0 . 5 \sum _ { i j } w _ { i j }$ , and the functions of $\delta ^ { \prime } ( c _ { i } , c _ { j } )$ and $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ are the same as those in Eqs. (5) and (6).




其中 $m = 0 。 5 \sum _ { i j } w _ { i j }$ ，$\delta ^ { \prime } ( c _ { i } , c _ { j } )$ 和 $\delta ^ { \prime \prime } ( c _ { i } , c _ { j } )$ 的功能与式(1)相同。 （5）和（6）。


## 3.3.3. Measurements of sector news sentiment




## 3.3.3.行业新闻情绪的测量


According to the EMH [32], stock price re<sup>fl</sup>ects all available market information. To control the in<sup>fl</sup>uences of market momentum on stock performances, we further measure the sentiment of market news [41]. The method of sentiment classi<sup>fi</sup>cation is similar to what we have undertaken in previous comparable relationship mining. We <sup>fi</sup>rst randomly collect 10,000 documents from the news set for labeling. We then select features and perform the test using the labeled data set.<sup>7</sup> With the trained classi<sup>fi</sup>er model, we perform binary classi<sup>fi</sup>cation of the whole news set. Then, we summarize the daily number of positive news about stock as $\boldsymbol { \mathrm { n _ { p } } }$ and the daily number of negative news about stock as $\mathrm { n } _ { \mathrm { n } } .$ The sentiment score of stock on that day is denoted as $n _ { p } - n _ { n }$ . For a sector measurement, the sentiment of individual stock is accumulated. Although other factors that in<sup>fl</sup>uence sector performance exist, as discussed in the conclusions section, we argue that price and market real-time news have covered the most important and popular parts of the available information in measuring an ef<sup>fi</sup>cient market.




根据有效市场假说[32]，股票价格反映了所有可用的市场信息。为了控制市场动量对股票表现的影响，我们进一步衡量市场新闻的情绪[41]。情感分类的方法和我们之前的可比关系挖掘类似。我们首先从新闻集中随机收集 10,000 个文档进行标记。然后，我们选择特征并使用标记的数据集执行测试。<sup>7</sup>通过经过训练的分类<sup>fi</sup>模型，我们对整个新闻集进行二元分类<sup>fi</sup>。然后，我们将每日有关股票的正面消息数量总结为 $\boldsymbol { \mathrm { n _ { p } } }$，每日有关股票的负面消息数量为 $\mathrm { n } _ { \mathrm { n } } 。$当天股票的情绪得分表示为 $n _ { p } - n _ { n }$ 。对于行业衡量，个股的情绪是累积的。尽管存在影响行业表现的其他因素，正如结论部分所讨论的，我们认为价格和市场实时新闻已经涵盖了衡量有效市场的可用信息中最重要和最受欢迎的部分。


## 3.4. An example




## 3.4。一个例子


Here we provide an example to illustrate the network construction and calculation of sector interaction metrics. First, we focus on stock 00002 (denoted as stock A) and stock 000024 (denoted as stock B). Both are from the <sup>fi</sup>nance sector on December 2, 2013. All the target stocks for the 3 negative links are stock A. Among the 14 positive links, the target stocks of 12 links are A, and the target stocks of the other 2 links are B. As indicated in Fig. 2, when constructing a closeness (undirected) network, only one edge exists between the two stocks, and the weight is $1 7 = 3 + 1 4$ . In the cooperative (positive) network, an edge between B and A exists, and the weight is 12. Simultaneously, an edge runs from A to B, the weight of which is 2. In the competitive (negative) network, the edge between B and A has a weight of 3.




这里我们通过一个例子来说明网络构建和部门交互指标的计算。首先，我们关注股票00002（记为股票A）和股票000024（记为股票B）。两者均来自2013年12月2日的<sup>金融</sup>行业。3个负向链接的目标股票均为A股。14个正向链接中，12个链接的目标股票为A，另外2个链接的目标股票为B。如图2所示，在构建紧密度（无向）网络时，两只股票之间仅存在一条边，权重为$1·7=3+1 4 美元。在合作（正）网络中，B和A之间存在一条边，权重为12。同时，有一条从A到B的边，权重为2。在竞争（负）网络中，B和A之间的边权重为3。


(c) Negative Network  
Table 1  
![](/api/attachments/H2Y9VY8C/fulltext/images/a827dc5c0d93f954ebbbff8627d80aec840b4f6d1e632e6f40fe6c4d26af9141.jpg)  
Fig. 2. Examples of constructing social networks.




(c) 负面网络  
表1  
![](/api/attachments/H2Y9VY8C/fulltext/images/a827dc5c0d93f954ebbbff8627d80aec840b4f6d1e632e6f40fe6c4d26af9141.jpg)  
图 2. 构建社交网络的示例。


Second, we use stock A and stock B on December 2, 2013, to calculate the sector interaction metrics. Taking the undirected network as an example, the total sum of weights on the links in the network is 1521; thus, $m = 1 5 2 1$ . Among all of the links, those with <sup>¼</sup>stock A at one end are used to calculate $\mathsf { W } _ { \mathsf { A } } ,$ , and $\mathsf { W } _ { \mathrm { A } } = 2 1 3$ . Similarly, those that have stock B at one end are used to calculate $\mathsf { W } _ { \mathsf { B } } ,$ and $\mathsf { W } _ { \mathrm { B } } = 2 3$ . The weights of the edges that link both stock A and stock B are used to calculate $\mathsf { W } _ { \mathsf { A B } } ,$ , and $\mathsf { W } _ { \mathsf { A B } } = 1 7 .$ Furthermore, stocks A and B belong to the same sector (<sup>fi</sup>nance); thus, $\delta ^ { \prime } ( c _ { A } , c _ { B } ) = 1$ <sup>ð Þ ¼</sup>Considering other stocks in the <sup>fi</sup>nance sector on the same day, we use Eq. (5) and <sup>fi</sup>nally obtain the intra-sector modularity (intra\_uq) of <sup>fi</sup>nance, which is 0.041.




其次，我们使用 2013 年 12 月 2 日的股票 A 和股票 B 来计算行业交互指标。以无向网络为例，网络中各链路的权重总和为1521；因此， $m = 1 5 2 1$ 。所有链接中，一端带有 <sup>1/4</sup>股票 A 的链接用于计算 $\mathsf { W } _ { \mathsf { A } } 、$ 和 $\mathsf { W } _ { \mathrm { A } } = 2 1 3$ 。类似地，一端有股票 B 的那些用于计算 $\mathsf { W } _ { \mathsf { B } } ,$ 和 $\mathsf { W } _ { \mathrm { B } } = 2 3$ 。连接股票 A 和股票 B 的边的权重用于计算 $\mathsf { W } _ { \mathsf { A B } } 、$ 和 $\mathsf { W } _ { \mathsf { A B } } = 1 7 。$此外，股票 A 和 B 属于同一板块 (<sup>fi</sup>nance)；因此， $\delta ^ { \prime } ( c _ { A } , c _ { B } ) = 1$ <sup>ð Þ ¼</sup>考虑到同一天<sup>金融</sup>领域的其他股票，我们使用等式： (5) 最终得到<sup>fi</sup>nance的部门内模块度(intra\_uq)，为0.041。


Given another stock C (601992) that belongs to the materials sector, we can obtain the corresponding values of m=1521, W =213, ${ \sf W } _ { \mathrm { C } } = 5 ,$ , and ${ \mathsf { W } } _ { \mathsf { A C } } = 2$ from the network in a similar manner. The value obtained is accumulated in the inter-sector modularity between materials and <sup>fi</sup>nance. As indicated in Table 1, the intersector modularity between <sup>fi</sup>nance and materials is 0.000306. Fig. 3 displays the relationships in the following three sectors: materials (green), daily consumption (blue), and <sup>fi</sup>nance (red).




给定另一只属于材料板块的股票C（601992），我们可以以类似的方式从网络中获得m=1521、W=213、${\sf W } _ {\mathrm { C } } = 5、$和${ \mathsf { W } } _ { \mathsf { A C } } = 2$的对应值。获得的价值是在材料和金融之间的跨部门模块化中积累的。如表 1 所示，财务和材料之间的交叉模块度为 0.000306。图3显示了以下三个部门的关系：材料（绿色）、日常消费（蓝色）和<sup>金融</sup>金融（红色）。


In the positive network, the sum of weights is 1448; thus, m = 1448. The links directed to stock A are used for calculating $w _ { A } ^ { i n }$ and the links directed to stock B are used for calculating w<sup>in</sup>: $w _ { A } ^ { i n } = 1 7 2 , w _ { B } ^ { i n } = 8$ . Conversely, the links that start from stock A are <sup>¼ ¼</sup>used for calculatingw<sup>out</sup>, and the links that start from stock B are used for calculating $v _ { B } ^ { o u t } \colon w _ { A } ^ { o u t } = 2 5 , w _ { B } ^ { o u t } = 1 2$ . The weight of the link from A to B is $2 \left( w _ { A B } = 2 \right)$ <sup>¼ ¼</sup>, and the weight of the link from B to A is $1 2 \ ( w _ { B A } = 1 2 )$ <sup>¼</sup>. Because stocks A and B belong to the same <sup>¼fi</sup>nancial sector, the value obtained from Eq. (5) is accumulated in the intra-sector modularity (intra\_pq) of <sup>fi</sup>nance in the positive network as 0.0686.




正网络中，权重之和为1448；因此，m = 1448。指向股票 A 的链接用于计算 $w _ { A } ^ { i n }$，指向股票 B 的链接用于计算 w<sup>in</sup>： $w _ { A } ^ { i n } = 1 7 2 , w _ { B } ^ { i n } = 8$ 。反之，从股票 A 开始的链接<sup>¼ ¼</sup>用于计算 w<sup>out</sup>，从股票 B 开始的链接用于计算 $v _ { B } ^ { o u t } \colon w _ { A } ^ { o u t } = 2 5 , w _ { B } ^ { o u t } = 1 2$ 。从 A 到 B 的链接权重为 $2 \left( w _ { A B } = 2 \right)$ <sup>¼ ¼</sup>，从 B 到 A 的链接权重为 $1 2 \( w _ {B A } = 1 2 )$ <sup>¼</sup>。由于股票 A 和 B 属于同一个<sup>1/4fi</sup>金融部门，因此从式（1）中得到的值： (5) 正网络中<sup>fi</sup>nance的部门内模块性(intra\_pq)累计为0.0686。


![](/api/attachments/H2Y9VY8C/fulltext/images/7964d41802857be0aa3aafeca1bdafaad749416cf1742655c1c5d9255ab84658.jpg)  
Fig. 3. Undirected network of three industries




![](/api/attachments/H2Y9VY8C/fulltext/images/7964d41802857be0aa3aafeca1bdafaad749416cf1742655c1c5d9255ab84658.jpg)  
图3. 三个行业的无向网络


## 4. Econometric model




## 4.计量经济模型


## 4.1. Rationale for VARX




## 4.1. VARX 的基本原理


We employ a VARX model, which is a time-series technique, for an empirical investigation. VARX models include exogenous variables, unlike standard VAR models. VARX models are suitable for examining the dynamics of the relationship between the sector interaction measures and sector performance with the following advantages. First, VARX models are particularly useful for describing interaction and feedback effects for forecasting. They allow for more than one evolving variable. All the variables in the model are treated symmetrically in a structural sense; each variable has an equation that explains its evolution based on its own lags (autoregressive carryover effects) and the lags of the other model variables (cross-effects). In this study, the VARX models capture not only the autoregressive carryover and crosseffects on sector interactions and sector performance but also the control effects of market sentiment. Second, VARX models can track the dynamic cumulative effects of the social network in predicting industry value in the short and long terms using generalized impulse response functions (GIRFs) [42]. This fact is particularly important because GIRFs can uncover dynamic effects that are not observable with other static models. Third, VARX models can assess the relative contributions of the different metrics of social networks using generalized forecast error variance decomposition (GFEVD) [42,43], which is quite helpful for performing hypothesis testing in the study. Recently, VARX models have been broadly adopted in marketing and IS research to investigate the time-series effects of information and economic metrics [28,29,35,44]. Similarly, we use VARX models to estimate complex effects and to determine the full predictive value of social networks.




我们采用 VARX 模型（一种时间序列技术）进行实证研究。与标准 VAR 模型不同，VARX 模型包含外生变量。 VARX模型适合研究部门互动指标与部门绩效之间的动态关系，具有以下优点。首先，VARX 模型对于描述预测的交互和反馈效应特别有用。它们允许多个不断变化的变量。模型中的所有变量在结构意义上都是对称处理的；每个变量都有一个方程，根据其自身的滞后（自回归残留效应）和其他模型变量的滞后（交叉效应）解释其演变。在本研究中，VARX 模型不仅捕捉到了行业互动和行业绩效的自回归结转和交叉效应，还捕捉了市场情绪的控制效应。其次，VARX 模型可以使用广义脉冲响应函数（GIRF）跟踪社交网络的动态累积效应，预测短期和长期的行业价值[42]。这一事实尤其重要，因为 GIRF 可以揭示其他静态模型无法观察到的动态效应。第三，VARX模型可以利用广义预测误差方差分解（GFEVD）[42,43]来评估社交网络不同指标的相对贡献，这对于研究中进行假设检验非常有帮助。最近，VARX 模型已广泛应用于营销和信息系统研究中，以研究信息和经济指标的时间序列效应[28,29,35,44]。同样，我们使用 VARX 模型来估计复杂效应并确定社交网络的完整预测价值。


Intra- and inter-sector modularities.




部门内和部门间的模块化。


<table><tr><td>Sector</td><td>Materials (green)</td><td>Daily consumption (blue)</td><td>Finance (red)</td></tr><tr><td>Materials (green)</td><td>0.0045</td><td>-0.00025</td><td>0.00030</td></tr><tr><td>Daily consumption (blue)</td><td>-0.00025</td><td>0.019</td><td>0.00056</td></tr><tr><td>Finance (red)</td><td>0.00030</td><td>0.00056</td><td>0.041</td></tr></table>




<table><tr><td>行业</td><td>物资（绿色）</td><td>日常消耗（蓝色）</td><td>金融（红色）</td></tr><tr><td>物资（绿色）</td><td>0.0045</td><td>-0.00025</td><td>0.00030</td></tr><tr><td>每日消耗量（蓝色）</td><td>-0.00025</td><td>0.019</td><td>0.00056</td></tr><tr><td>金融（红色）</td><td>0.00030</td><td>0.00056</td><td>0.041</td></tr></table>


Table 2 Sector distribution.




表2 行业分布。


<table><tr><td>Sector ID</td><td>Sector Name</td><td>No. of Stocks</td><td>Missing Days</td></tr><tr><td>1</td><td>Energy</td><td>28</td><td>2</td></tr><tr><td>2</td><td>Materials</td><td>45</td><td>0</td></tr><tr><td>3</td><td>Industry</td><td>56</td><td>0</td></tr><tr><td>4</td><td>Optional consumption</td><td>32</td><td>0</td></tr><tr><td>5</td><td>Daily consumption</td><td>27</td><td>0</td></tr><tr><td>6</td><td>Medical care</td><td>25</td><td>0</td></tr><tr><td>7</td><td>Finance</td><td>54</td><td>0</td></tr><tr><td>8</td><td>Information and technology</td><td>12</td><td>2</td></tr><tr><td>9</td><td>Telecom service</td><td>2</td><td>7</td></tr><tr><td>10</td><td>Utility</td><td>13</td><td>34</td></tr></table>




<table><tr><td>扇区ID</td><td>扇区名称</td><td>编号股票</td><td>缺失天</td></tr><tr><td>1</td><td>能量</td><td>28</td><td>2</td></tr><tr><td>2</td><td>材料</td><td> 45</td><td>0</td></tr><tr><td>3</td><td>行业</td><td>56</td><td>0</td></tr><tr><td>4</td><td>可选消费</td><td>32</td><td>0</td></tr><tr><td>5</td><td>每日消费</td><td>27</td><td>0</td></tr><tr><td>6</td><td>医疗护理</td><td>25</td><td>0</td></tr><tr><td>7</td><td>财务</td><td>54</td><td>0</td></tr><tr><td>8</td><td>信息和技术</td><td>12</td><td>2</td></tr><tr><td>9</td><td>电信服务</td><td>2</td><td>7</td></tr><tr><td>10</td><td>实用程序</td><td>13</td><td>34</td></tr></table>


## 4.2. Model specification




## 4.2.型号规格


We estimate a VARX model for each sector. The endogenous variables include the sector performance (return and idiosyncratic risk), undirected network metrics (inter-sector modularity value and intra-sector modularity value), positive network metrics (inter-sector modularity value and intra-sector modularity value), and negative network metrics (inter-sector modularity value and intra-sector modularity value). We include only one exogenous variable to control the market sentiment effects on sector performance. The VARX model is speci<sup>fi</sup>ed as follows:




我们估计每个部门的 VARX 模型。内生变量包括部门绩效（回报和异质风险）、无向网络指标（部门间模块化值和部门内模块化值）、正网络指标（部门间模块化值和部门内模块化值）和负网络指标（部门间模块化值和部门内模块化值）。我们仅包含一个外生变量来控制市场情绪对行业表现的影响。 VARX 模型的具体<sup>fi</sup>如下：


$$
\begin{array}{r l} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {U} Q _ {t} \\ \text {Inter} _ {A} U Q _ {t} \\ \text {Intra} _ {P} Q _ {t} \\ \text {Inter} _ {A} P Q _ {t} \\ \text {Intra} _ {N} Q _ {t} \\ \text {Inter} _ {A} N Q _ {t} \end{array} \right] & = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \\ \alpha_ {7} + \delta_ {7} t \\ \alpha_ {8} + \delta_ {8} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 8} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 8} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 8} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 8} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 8} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 8} ^ {k} \\ \phi_ {7, 1} ^ {k} \dots \phi_ {7, 8} ^ {k} \\ \phi_ {8, 1} ^ {k} \dots \phi_ {8, 8} ^ {k} \end{array} \right] \\ & . \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {U} Q _ {t - k} \\ \text {Inter} _ {A} U Q _ {t - k} \\ \text {Intra} _ {P} Q _ {t - k} \\ \text {Inter} _ {A} P Q _ {t - k} \\ \text {Intra} _ {N} Q _ {t - k} \\ \text {Inter} _ {A} N Q _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \\ \varepsilon_ {7 t} \\ \varepsilon_ {8 t} \end{array} \right] \end{array}\tag{9}
$$




$$
\begin{array}{r l} \left[ \begin{array}{c} \text {回报} _ {t} \\ \text {风险} _ {t} \\ \text {Intra} _ {U} Q _ {t} \\ \text {Inter} _ {A} U Q _ {t} \\ \text {Intra} _ {P} Q _ {t} \\ \text {Inter} _ {A} P Q _ {t} \\ \text {帧内} _ {N} Q _ {t} \\ \text {帧间} _ {A} N Q _ {t} \end{array} \right] & = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \\ \alpha_ {7} + \delta_ {7} t \\ \alpha_ {8} + \delta_ {8} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 8} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 8} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 8} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 8} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 8} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 8} ^ {k} \\ \phi_ {7, 1} ^ {k} \dots \phi_ {7, 8} ^ {k} \\ \phi_ {8, 1} ^ {k} \dots \phi_ {8, 8} ^ {k} \end{array} \right] \\ & . \left[ \begin{array}{c} \text {返回} _ {t - k} \\ \text {风险} _ {t - k} \\ \text {Intra} _ {U} Q _ {t - k} \\ \text {Inter} _ {A} U Q _ {t - k} \\ \text {Intra} _ {P} Q _ {t - k} \\ \text {Inter} _ {A} P Q _ {t - k} \\ \text {帧内} _ {N} Q _ {t - k} \\ \text {帧间} _ {A} N Q _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \\ \varepsilon_ {7 t} \\ \varepsilon_ {8 t} \end{array} \right] \end{array}\tag{9}
$$


where $I n t r a _ { U } Q ,$ , Intra Q, and $I n t r a _ { N } Q$ represent the intra-sector modularity values in the undirected network, positive network, and negative network, respectively; $I n t e r _ { A } U Q ,$ $I n t e r _ { A } P Q$ , and $I n t e r _ { A } N Q$ represent the average inter-sector modularity values in the undirected network, positive network, and negative network, respectively; $\alpha _ { i } ( i = 1 , 2 , \cdot \cdot \cdot , 8 )$ are constants; $\delta _ { i } , \phi _ { i , j } ^ { k } ( i , j = 1 , 2 , \cdots , 8 )$ are coef<sup>fi</sup>cients; $\tau _ { 1 , 1 }$ is the coef<sup>fi</sup>cient of the exogenous variable (sector news sentiment) $x _ { 1 t } ;$ K is the lag length, and $\varepsilon _ { i } ( i = 1 , 2 , \cdots , 8 )$ are white-noise residuals.




其中 $I n t r a _ { U } Q 、$ 、Intra Q 和 $I n t r a _ { N } Q$ 分别表示无向网络、正网络和负网络中的扇区内模块化值； $I nter _ { A } U​​ Q 、$ $I n ter _ { A } P Q$ 和 $I n ter _ { A } N Q$ 分别表示无向网络、正向网络和负向网络中的平均扇区间模块度值； $\alpha _ { i } ( i = 1 , 2 , \cdot \cdot \cdot , 8 )$ 是常量； $\delta _ { i } , \phi _ { i , j } ^ { k } ( i , j = 1 , 2 , \cdots , 8 )$ 是系数<sup>fi</sup>； $\tau _ { 1 , 1 }$ 是外生变量（行业新闻情绪）$x _ { 1 t } 的系数<sup>fi</sup>；$K 是滞后长度，$\varepsilon _ { i } ( i = 1 , 2 , \cdots , 8 )$ 是白噪声残差。


<sup>ð ¼    Þ</sup>The lag order in the VARX model is usually selected using Schwartz’s Bayesian information criterion (SIC) and the <sup>fi</sup>nal prediction error (FPE) [28,35]. Thus, we select the lag order with the minimized SIC and FPE in each model across 10 industries.




<sup>ð ¼ Þ</sup>VARX 模型中的滞后阶数通常使用 Schwartz 的贝叶斯信息准则（SIC）和<sup>最终</sup>最终预测误差（FPE）来选择[28,35]。因此，我们在 10 个行业的每个模型中选择具有最小化 SIC 和 FPE 的滞后阶数。


## 5. Estimation result




## 5. 估计结果


## 5.1. Time-series data




## 5.1.时间序列数据


To prepare the daily data for the time-series analysis, we investigate the daily sector return and risk, in addition to daily




为了准备时间序列分析的每日数据，除了每日的行业回报和风险外，我们还调查了每日的行业回报和风险。


## Table 3




## 表 3


Statistics regarding daily company networks.




有关日常公司网络的统计数据。


<table><tr><td></td><td>Undirected network</td><td>Positive network</td><td>Negative network</td></tr><tr><td>Mean</td><td>137</td><td>133</td><td>30</td></tr><tr><td>Maximum</td><td>276</td><td>274</td><td>116</td></tr><tr><td>Minimum</td><td>87</td><td>84</td><td>12</td></tr><tr><td>Median</td><td>120</td><td>116</td><td>21</td></tr></table>




<table><tr><td></td><td>无向网络</td><td>正网络</td><td>负网络网络</td></tr><tr><td>平均值</td><td>137</td><td>133</td><td>30</td></tr><tr><td>最大值</td><td>276</td><td>274</td><td>116</td> </tr><tr><td>最小值</td><td>87</td><td>84</td><td>12</td></tr><tr><td>中位数</td><td>120</td><td>116</td><td>21</td></tr></table>


social networks based on public news. First, we <sup>fi</sup>lter out 6 $\mathrm { \ s t o c k s ^ { 8 } }$ that have experienced long-term trading suspensions during this period. We divide the remaining 294 stocks into 10 sections (Table 2). We calculate the days that a sector does not appear in the company network, which indicates that the company network metrics for the sector are missing for those days. Fortunately, we <sup>fi</sup>nd that few data are missing. The utility sector has 204 valid days of a total of 238 days. We replace these missing data with 0, thus indicating no inter- or intra-sector interactions on that day.




基于公共新闻的社交网络。首先，我们<sup>筛选</sup>筛选出6只在此期间经历了长期停牌的$\mathrm { \ s t o c k s ^ { 8 } }$。我们将剩余 294 只股票分为 10 个部分（表 2）。我们计算某个扇区未出现在公司网络中的天数，这表明该扇区的公司网络指标在这些天数中缺失。幸运的是，我们<sup>发现</sup>发现几乎没有数据丢失。公用事业部门有 204 天有效，总计 238 天。我们将这些缺失的数据替换为 0，从而表明当天没有部门间或部门内的互动。


To further investigate the network density, we perform simple statistics for daily <sup>fi</sup>rm networks. As shown in Table 3, the daily <sup>fi</sup>rm network is not quite sparse, considering undirected (company closeness) networks. Even in the smallest network, 87 companies appear. The situation is quite similar for the positive (cooperative company) networks. However, for the negative (competitive company) networks, the nodes are sparse, with a minimum value of 12 companies, because the identi<sup>fi</sup>ed negative relations are much fewer than positive relations. Imbalances between positive and negative opinions have also been found in previous studies of user-generated content [29].




为了进一步调查网络密度，我们对日常网络进行简单的统计。如表 3 所示，考虑到无向（公司紧密度）网络，日常 <sup>fi</sup>rm 网络并不十分稀疏。即使在最小的网络中，也有 87 家公司出现。积极（合作公司）网络的情况非常相似。然而，对于负向（竞争公司）网络，节点稀疏，最小值为 12 个公司，因为识别出的负向关系远少于正向关系。在之前对用户生成内容的研究中也发现了正面和负面意见之间的不平衡[29]。


## 5.2. Tests for stationarity in the time series




## 5.2.时间序列的平稳性检验


We conduct stationary and unit root tests to examine the stability of sector performance metrics and company network metrics. These tests investigate whether the variables entering the system evolve continually or are stationary. We conduct augmented Dickey–Fuller (ADF) tests to assess stationarity [45]. As reported in Table 4, except for the risk and news sentiment, the results of ADF testing of all the metrics across 10 sectors are less than the critical value of 2.87, thus leading us to reject the null hypothesis <sup>-</sup>of a unit root at the 95% con<sup>fi</sup>dence level. We use the <sup>fi</sup>rst difference for the risk and sector news sentiment. Furthermore, we <sup>fi</sup>nd that the corrected data series range from 17.83 to 3.29 (Table 3), thereby indicating that the variable series do not co-integrate in equilibrium [28,46].




我们进行平稳和单位根测试，以检查部门绩效指标和公司网络指标的稳定性。这些测试研究进入系统的变量是持续变化还是静止的。我们进行增强迪基-富勒（ADF）测试来评估平稳性[45]。如表 4 所示，除了风险和新闻情绪外，ADF 对 10 个部门的所有指标进行测试的结果均小于临界值 2.87，因此我们在 95% 置信度水平上拒绝了单位根的原假设<sup>-</sup>。我们使用风险和行业新闻情绪的<sup>第一个</sup>差异。此外，我们<sup>发现</sup>发现校正后的数据序列范围从17.83到3.29（表3），从而表明变量序列在均衡状态下不协整[28,46]。


## 5.3. Tests for granger causality




## 5.3.格兰杰因果关系检验


The results of the Granger causality test [47] are reported in Tables 5 and 6. According to the results, we can conclude that several social network metrics have signi<sup>fi</sup>cant time-based causal relationships with sector performance. In Table 5, the undirected network metrics, including the average inter-sector modularity value and the intra-sector modularity value, can Granger-cause returns in sectors 2, 5, 7, 8, and 10. Additionally, the positive network metrics have strong effects on the returns in sectors 2, 7, and 10. However, the intra-sector modularity value in the negative network is suf<sup>fi</sup>ciently signi<sup>fi</sup>cant to cause a return only in sector 2 $\left( p = 0 . 0 0 5 \right)$ , and the average inter-sector modularity value in the negative network only causes a return in industries 2 and 8 (p = 0.004 and 0.08, respectively).




格兰杰因果关系检验[47]的结果如表 5 和表 6 所示。根据结果，我们可以得出结论，一些社交网络指标与行业绩效具有显着的基于时间的因果关系。在表5中，无向网络指标，包括平均部门间模块度值和部门内模块度值，可以格兰杰引起部门2、5、7、8和10的回报。此外，正网络指标对部门2、7和10的回报有很强的影响。然而，负网络中的部门内模块度值足够充分。仅在行业 2 $\left( p = 0 . 0 0 5 \right)$ 中显着<sup>fi</sup>无法引起回报，而负网络中的平均行业间模块化值仅在行业 2 和 8 中引起回报（分别为 p = 0.004 和 0.08）。


8




（代码、公式、图片引用或其他非语言内容，无需翻译。）


K. Chen et al. / Information & Management xxx (2016) xxx–xxx




K.陈等人。 / 信息与管理 xxx (2016) xxx–xxx


Table 4  
Stationarity test of the endogenous variables.




表4  
内生变量的平稳性检验。


<table><tr><td>Sector</td><td>Return</td><td>ΔRisk</td><td>Δns</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>-13.24</td><td>-14.85</td><td>-8.70</td><td>-15.13</td><td>-15.13</td><td>-15.34</td><td>-15.30</td><td>-13.74</td><td>-13.35</td></tr><tr><td>2</td><td>-17.10</td><td>-11.94</td><td>-6.25</td><td>-15.07</td><td>-15.02</td><td>-15.69</td><td>-15.62</td><td>-4.39</td><td>-4.39</td></tr><tr><td>3</td><td>-17.83</td><td>-6.94</td><td>-5.30</td><td>-14.82</td><td>-14.8</td><td>-14.2</td><td>-14.24</td><td>-15.77</td><td>-15.81</td></tr><tr><td>4</td><td>-15.34</td><td>-10.71</td><td>-5.66</td><td>-12.65</td><td>-12.33</td><td>-13.18</td><td>-12.85</td><td>-14.80</td><td>-14.76</td></tr><tr><td>5</td><td>-14.76</td><td>-12.61</td><td>-5.14</td><td>-12.26</td><td>-12.33</td><td>-12.49</td><td>-12.48</td><td>-13.80</td><td>-13.86</td></tr><tr><td>6</td><td>-13.79</td><td>-14.40</td><td>-3.65</td><td>-8.31</td><td>-8.23</td><td>-8.3</td><td>-8.25</td><td>-12.76</td><td>-12.72</td></tr><tr><td>7</td><td>-15.63</td><td>-8.19</td><td>-7.18</td><td>-11.7</td><td>-12.3</td><td>-12.21</td><td>-12.49</td><td>-14.80</td><td>-15.02</td></tr><tr><td>8</td><td>-14.76</td><td>-13.68</td><td>-3.31</td><td>-12.24</td><td>-12.49</td><td>-12.17</td><td>-12.33</td><td>-14.90</td><td>-15.08</td></tr><tr><td>9</td><td>-15.46</td><td>-13.64</td><td>-10.60</td><td>-3.29</td><td>-5.00</td><td>-14.56</td><td>-5.17</td><td>-15.53</td><td>-15.40</td></tr><tr><td>10</td><td>-13.80</td><td>-13.24</td><td>-5.46</td><td>-14.77</td><td>-14.76</td><td>-14.78</td><td>-14.78</td><td>-15.59</td><td>-15.58</td></tr></table>




<table><tr><td>行业</td><td>回报</td><td>Δ风险</td><td>Δns</td><td>intra_uq</td><td>inter_auq</td><td> intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>-13.24</td><td>-1 4.85</td><td>-8.70</td><td>-15.13</td><td>-15.13</td><td>-15.34</td><td>-15.30</td><td>-13.74</td><td>-13。 35</td></tr><tr><td>2</td><td>-17.10</td><td>-11.94</td><td>-6.25</td><td>-15.07</td><td>-15.02</td><td>-15 .69</td><td>-15.62</td><td>-4.39</td><td>-4.39</td></tr><tr><td>3</td><td>-17.83</td><td>-6.94</td><td>-5。 30</td><td>-14.82</td><td>-14.8</td><td>-14.2</td><td>-14.24</td><td>-15.77</td><td>-15.81</td></tr><tr><t d>4</td><td>-15.34</td><td>-10.71</td><td>-5.66</td><td>-12.65</td><td>-12.33</td><td>-13.18</td><td>-12.8 5</td><td>-14.80</td><td>-14.76</td></tr><tr><td>5</td><td>-14.76</td><td>-12.61</td><td>-5.14</td><td>-12。 26</td><td>-12.33</td><td>-12.49</td><td>-12.48</td><td>-13.80</td><td>-13.86</td></tr><tr><td>6</td><td>- 13.79</td><td>-14.40</td><td>-3.65</td><td>-8.31</td><td>-8.23</td><td>-8.3</td><td>-8.25</td><td>-12.76</td> td><td>-12.72</td></tr><tr><td>7</td><td>-15.63</td><td>-8.19</td><td>-7.18</td><td>-11.7</td><td>-12.3</t d><td>-12.21</td><td>-12.49</td><td>-14.80</td><td>-15.02</td></tr><tr><td>8</td><td>-14.76</td><td>-13.68< /td><td>-3.31</td><td>-12.24</td><td>-12.49</td><td>-12.17</td><td>-12.33</td><td>-14.90</td><td>-15.08</t d></tr><tr><td>9</td><td>-15.46</td><td>-13.64</td><td>-10.60</td><td>-3.29</td><td>-5.00</td><td>-14.56</t d><td>-5.17</td><td>-15.53</td><td>-15.40</td></tr><tr><td>10</td><td>-13.80</td><td>-13.24</td><td>-5.46< /td><td>-14.77</td><td>-14.76</td><td>-14.78</td><td>-14.78</td><td>-15.59</td><td>-15.58</td></tr></table>


Note: Augmented Dickey Fuller (ADF) test statistic critical value: 2.87 (5% level con<sup>fi</sup>dence interval)




注：Augmented Dickey Fuller (ADF) 检验统计量临界值：2.87（5% 水平置信区间）


Table 5  
Granger causality tests on returns.




表5  
回报的格兰杰因果检验。


<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.43</td><td>0.57</td><td>0.70</td><td>0.79</td><td>0.45</td><td>0.53</td></tr><tr><td>2</td><td>0.02**</td><td>0.01***</td><td>0.02**</td><td>0.02**</td><td>0.005***</td><td>0.004***</td></tr><tr><td>3</td><td>0.45</td><td>0.27</td><td>0.17</td><td>0.09*</td><td>0.97</td><td>0.92</td></tr><tr><td>4</td><td>0.77</td><td>0.17</td><td>0.71</td><td>0.15</td><td>0.61</td><td>0.21</td></tr><tr><td>5</td><td>0.01***</td><td>0.009***</td><td>0.12</td><td>0.13</td><td>0.76</td><td>0.80</td></tr><tr><td>6</td><td>0.09*</td><td>0.13</td><td>0.21</td><td>0.25</td><td>0.61</td><td>0.59</td></tr><tr><td>7</td><td>0.03**</td><td>0.08*</td><td>0.007***</td><td>0.01***</td><td>0.24</td><td>0.21</td></tr><tr><td>8</td><td>0.07**</td><td>0.09*</td><td>0.15</td><td>0.17</td><td>0.4</td><td>0.08*</td></tr><tr><td>9</td><td>0.95</td><td>0.76</td><td>0.95</td><td>0.83</td><td>0.36</td><td>0.36</td></tr><tr><td>10</td><td>0.01***</td><td>0.002***</td><td>0.01***</td><td>0.006***</td><td>0.56</td><td>0.54</td></tr></table>




<table><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1< /td><td>0.43</td><td>0.57</td><td>0.70</td><td>0.79</td><td>0.45</td><td> 0.53</td></tr><tr><td>2</td><td>0.02**</td><td>0.01***</td><td>0.02**</td ><td>0.02**</td><td>0.005***</td><td>0.004***</td></tr><tr><td>3</td><td> 0.45</td><td>0.27</td><td>0.17</td><td>0.09*</td><td>0.97</td><td>0.92</t d></tr><tr><td>4</td><td>0.77</td><td>0.17</td><td>0.71</td><td>0.15</td> <td>0.61</td><td>0.21</td></tr><tr><td>5</td><td>0.01***</td><td>0.009*** </td><td>0.12</td><td>0.13</td><td>0.76</td><td>0.80</td></tr><tr><td>6</td><td>0.76</td><td>0.80</td></tr><tr><td>6</td> td><td>0.09*</td><td>0.13</td><td>0.21</td><td>0.25</td><td>0.61</td><td> 0.59</td></tr><tr><td>7</td><td>0.03**</td><td>0.08*</td><td>0.007***</td ><td>0.01***</td><td>0.24</td><td>0.21</td></tr><tr><td>8</td><td>0.07**< /td><td>0.09*</td><td>0.15</td><td>0.17</td><td>0.4</td><td>0.08*</td></t r><tr><td>9</td><td>0.95</td><td>0.76</td><td>0.95</td><td>0.83</td><td>0 .36</td><td>0.36</td></tr><tr><td>10</td><td>0.01***</td><td>0.002***</td ><td>0.01***</td><td>0.006***</td><td>0.56</td><td>0.54</td></tr></table>


Note: The estimates of Granger causality are the means of the p-values of the join Wald statistics.  
\*p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




注意：Granger 因果关系的估计是连接 Wald 统计数据的 p 值的平均值。  
\*p < 0.1，\*\* p < 0.05，\*\*\* p < 0.01。


Granger causality tests on risk.




风险的格兰杰因果检验。


<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.64</td><td>0.45</td><td>0.51</td><td>0.59</td><td>0.56</td><td>0.71</td></tr><tr><td>2</td><td>0.58</td><td>0.71</td><td>0.63</td><td>0.75</td><td> $\mathbf{0.08}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>3</td><td> $\mathbf{0.002}^{***}$ </td><td> $\mathbf{0.0007}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.004}^{***}$ </td><td>0.34</td><td>0.42</td></tr><tr><td>4</td><td> $\mathbf{0.003}^{***}$ </td><td> $\mathbf{0.009}^{***}$ </td><td> $\mathbf{0.001}^{***}$ </td><td> $\mathbf{0.007}^{***}$ </td><td>0.41</td><td>0.73</td></tr><tr><td>5</td><td>0.77</td><td>0.67</td><td>0.68</td><td>0.63</td><td>0.86</td><td>0.85</td></tr><tr><td>6</td><td> $\mathbf{0.03}^{**}$ </td><td> $\mathbf{0.01}^{***}$ </td><td>0.72</td><td>0.60</td><td>0.61</td><td>0.64</td></tr><tr><td>7</td><td>0.71</td><td>0.95</td><td>0.52</td><td>0.67</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>8</td><td>0.65</td><td>0.57</td><td>0.57</td><td>0.80</td><td>0.96</td><td>0.73</td></tr><tr><td>9</td><td>0.84</td><td>0.67</td><td>0.91</td><td>0.69</td><td>0.57</td><td>0.75</td></tr><tr><td>10</td><td>0.16</td><td> $\mathbf{0.06}^{*}$ </td><td>0.19</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td></tr></table>




<table><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td>< td>0.64</td><td>0.45</td><td>0.51</td><td>0.59</td><td>0.56</td><td>0.71</td ></tr><tr><td>2</td><td>0.58</td><td>0.71</td><td>0.63</td><td>0.75</td><td> $\mathbf{0.08}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>3</td><td> $\mathbf{0.002}^{***}$ </td><td> $\mathbf{0.0007}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.004}^{***}$ </td><td>0.34</td><td>0.42</td></tr><tr><td>4</td><td> $\mathbf{0.003}^{***}$ </td><td> $\mathbf{0.009}^{***}$ </td><td> $\mathbf{0.001}^{***}$ </td><td> $\mathbf{0.007}^{***}$ </td><td>0.41</td><td>0.73</td></tr><tr><td>5</td><td>0.77</td><td>0.67</td ><td>0.68</td><td>0.63</td><td>0.86</td><td>0.85</td></tr><tr><td>6</td><td> $\mathbf{0.03}^{**}$ </td><td> $\mathbf{0.01}^{***}$ </td><td>0.72</td><td>0.60</td><td>0.61</td><td>0.64</td></tr><tr> <td>7</td><td>0.71</td><td>0.95</td><td>0.52</td><td>0.67</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.07}^{*}$ </td></tr><tr><td>8</td><td>0.65</td><td>0.57</td><td>0.57</td><td>0.80</td><td>0.96</td><td>0.73</td></tr><tr><td>9</td><td>9</td> td><td>0.84</td><td>0.67</td><td>0.91</td><td>0.69</td><td>0.57</td><td>0.75</td></tr><tr><td>10</td><td>0.16</td><td> $\mathbf{0.06}^{*}$ </td><td>0.19</td><td> $\mathbf{0.09}^{*}$ </td><td> $\mathbf{0.01}^{***}$ </td><td> $\mathbf{0.01}^{***}$ </td></tr></table>


Note: The estimates of Granger causality are the mean of the p-values of the joint Wald statistics.  
\*p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




注：Granger 因果关系的估计是 Wald 联合统计的 p 值的平均值。  
\*p < 0.1，\*\* p < 0.05，\*\*\* p < 0.01。


As indicated in Table 6, the results suggest that the undirected network metrics can cause risk in sectors 3, 4, and 6, followed by the negative network metrics in industries 2, 7, and 10 and the positive network metrics in sectors 3 and 4. These results support H1a in that the sector’s interactive metrics in company networks have predictive power for sector performance.




如表 6 所示，结果表明，无向网络指标可能会在行业 3、4 和 6 中造成风险，其次是行业 2、7 和 10 中的负网络指标以及行业 3 和 4 中的正网络指标。这些结果支持 H1a，因为公司网络中的行业互动指标对行业绩效具有预测能力。


## 5.4. Short- and long-term relationships between company comparative networks and sector performance




## 5.4。公司比较网络与行业绩效之间的短期和长期关系


We model the variable dynamics based on GIRFs. In this step, we use the estimated parameters of the VARX model $\phi _ { i , j } ^ { k }$ to generate the GIRFs with $\psi _ { i , j } ( t ) ,$ measuring the net effects of one unit of unexpected change in the social network metrics i on the industry value metric j at time t without assuming a causal ordering [45,48]. We obtain the standard errors by simulating the <sup>fi</sup>tted VARX model using a Monte Carlo method with 1000 runs, and the statistical signi<sup>fi</sup>cance of the parameters is tested. The short-term (immediate predictive value) and long-term (cumulative predictive value) effects are also derived from the GIRFs. We can also assess the dynamics of parameters relative to wear-in time by gauging the number of periods before the peak predictive value is reached and quantify the wear-out time by gauging the number of periods before the stable predictive value is reached.




我们基于 GIRF 对变量动态进行建模。在此步骤中，我们使用 VARX 模型的估计参数 $\phi _ { i , j } ^ { k }$ 生成 GIRF，其中 $\psi _ { i , j } ( t ) ,$ 测量社交网络指标 i 的一个意外变化单位在时间 t 对行业价值指标 j 的净影响，而不假设因果排序 [45,48]。我们通过使用蒙特卡罗方法模拟 1000 次运行的拟合 VARX 模型来获得标准误差，并测试参数的统计显着性。短期（即时预测值）和长期（累积预测值）效应也源自 GIRF。我们还可以通过测量达到峰值预测值之前的周期数来评估相对于磨合时间的参数动态，并通过测量达到稳定预测值之前的周期数来量化磨损时间。


We <sup>fi</sup>rst investigate the wear-in and wear-out effects on sector performance. Tables 7 and 8 present the results and averages of the outcomes of the time effects between social networks and sector values across 10 industries. From the results, we <sup>fi</sup>nd that negative comparative relationships have a shorter wear-in time on return than positive comparative relationships (F = 6.14, p < 0.01). Simultaneously, negative comparative relationships have a longer wearout time on return than positive comparative relationships




我们<sup>首先</sup>研究磨损和磨损对部门绩效的影响。表 7 和表 8 列出了 10 个行业的社交网络与部门价值之间的时间效应结果和平均值。从结果中，我们<sup>发现</sup>发现，负面比较关系的回报磨合时间比正面比较关系短（F = 6.14，p < 0.01）。同时，消极比较关系的回报磨损时间比积极比较关系更长


Table 7  
Duration of the short- and long-term impacts on return.




表7  
对回报的短期和长期影响的持续时间。


<table><tr><td colspan="7">Wear-in</td><td colspan="6">Wear-out</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>4</td><td>4</td><td>3</td><td>5</td><td>5</td></tr><tr><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>6</td><td>4</td><td>4</td><td>6</td><td>7</td></tr><tr><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>7</td><td>7</td><td>6</td><td>6</td><td>8</td><td>8</td></tr><tr><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td></tr><tr><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>2</td><td>2</td><td>8</td><td>8</td><td>7</td><td>8</td><td>8</td><td>9</td></tr><tr><td>6</td><td>4</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td>6</td><td>6</td><td>5</td><td>5</td><td>8</td><td>8</td></tr><tr><td>7</td><td>3</td><td>3</td><td>3</td><td>3</td><td>1</td><td>1</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>8</td><td>2</td><td>3</td><td>3</td><td>3</td><td>1</td><td>2</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td><td>7</td></tr><tr><td>9</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td></tr><tr><td>10</td><td>7</td><td>7</td><td>7</td><td>7</td><td>4</td><td>4</td><td>10</td><td>9</td><td>9</td><td>8</td><td>9</td><td>10</td></tr><tr><td>Average</td><td>2.8</td><td>3</td><td>2.6</td><td>2.6</td><td>1.5</td><td>1.6</td><td>5.6</td><td>5.9</td><td>5.4</td><td>5.4</td><td>6.8</td><td>7.1</td></tr><tr><td>Test</td><td colspan="6">Intra_pq + Inter_apq &gt; Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq &lt; Intra_nq + Inter_anq</td></tr><tr><td>F-test</td><td colspan="6">6.14***</td><td colspan="6">37.77***</td></tr></table>




<table><tr><td colspan="7">磨损</td><td colspan="6">磨损</td></tr><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq< /td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>in tra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</ td><td>4</td><td>4</td><td>3</td><td>5</td><td>5</td></tr><tr><td>2</td><td>1</td><td>2</td><td>1</td><td>1</td><td> 1</td><td>1</td><td>4</td><td>6</td><td>4</td><td>4</td><td>6</td><td>7</td></tr><tr><td>3</td><td>2</td><td>2</td> <td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>7</td><td>7</td><td>6</td><td>6</td><td>8</td><td>8</td></tr><tr><td>4< /td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td>< td>5</td></tr><tr><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>2</td><td>2</td><td>8</td><td>8</td><td>7</t d><td>8</td><td>8</td><td>9</td></tr><tr><td>6</td><td>4</td><td>4</td><td>2</td><td>2</td><td>1</td><td>1</td><td> 6</td><td>6</td><td>5</td><td>5</td><td>8</td><td>8</td></tr><tr><td>7</td><td>3</td><td>3</td><td>3</td><td>3</td> <td>1</td><td>1</td><td>4</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>8</td><td>2</td><td>3< /td><td>3</td><td>3</td><td>1</td><td>2</td><td>2</td><td>5</td><td>6</td><td>5</td><td>5</td><td>7</td><td>7</td></tr><tr><td >9</td><td>1</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</t d><td>6</td></tr><tr><td>10</td><td>7</td>7</td><td>7</td><td>7</td><td>7</td><td>4</td><td>4</td><td>10</td><td>9</td><t d>9</td><td>8</td><td>9</td><td>10</td></tr><tr><td>平均</td><td>2.8</td><td>3</td><td>2.6</td><td>2.6</td><td>1 .5</td><td>1.6</td><td>5.6</td><td>5.9</td><td>5.4</td><td>5.4</td><td>6.8</td><td>7.1</td></tr><tr><td>测试</td><td colspan="6">Intra_pq + Inter_apq > Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq < Intra_nq + Inter_anq</td></tr><tr><td>F 测试</td><td colspan="6">6.14***</td><td colspan="6">37.77***</td></tr></table>


Notes: \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




注：\* p < 0.1、\*\* p < 0.05、\*\*\* p < 0.01。


Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005




请在媒体上引用这篇文章：K. Chen 等人，公司比较网络对股票行业表现的动态预测能力，Inf。管理。 （2016），http://dx.doi.org/10.1016/j.im.2016.07.005


Table 8  
Duration of the short- and long-term impacts on risk.




表8  
对风险的短期和长期影响的持续时间。


<table><tr><td colspan="7">Wear-in</td><td colspan="6">Wear-out</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>6</td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>1</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>3</td><td>5</td><td>6</td></tr><tr><td>3</td><td>3</td><td>3</td><td>5</td><td>5</td><td>3</td><td>3</td><td>5</td><td>6</td><td>6</td><td>6</td><td>8</td><td>9</td></tr><tr><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>5</td><td>6</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>8</td><td>9</td><td>8</td><td>8</td><td>9</td><td>9</td></tr><tr><td>6</td><td>3</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td>6</td><td>7</td><td>7</td><td>7</td><td>9</td><td>9</td></tr><tr><td>7</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>3</td><td>5</td><td>6</td><td>5</td><td>4</td><td>6</td><td>6</td></tr><tr><td>8</td><td>1</td><td>3</td><td>1</td><td>1</td><td>1</td><td>3</td><td>4</td><td>5</td><td>6</td><td>5</td><td>7</td><td>6</td></tr><tr><td>9</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td><td>7</td><td>7</td></tr><tr><td>10</td><td>8</td><td>8</td><td>8</td><td>8</td><td>6</td><td>6</td><td>9</td><td>8</td><td>9</td><td>9</td><td>10</td><td>10</td></tr><tr><td>Average</td><td>2.6</td><td>2.9</td><td>2.9</td><td>2.9</td><td>2.6</td><td>2.8</td><td>5.5</td><td>5.9</td><td>6</td><td>5.8</td><td>7.3</td><td>7.4</td></tr><tr><td>Test</td><td colspan="6">Intra_pq + Inter_apq &gt; Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq &lt; Intra_nq + Inter_anq</td></tr><tr><td>F-test</td><td colspan="6">0.16</td><td colspan="6">50.79***</td></tr></table>




<table><tr><td colspan="7">磨损</td><td colspan="6">磨损</td></tr><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq< /td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>in tra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3</td><td>3</td><td>6</ td><td>5</td><td>5</td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>1</td><td>2</td><td>2</td><td> 1</td><td>1</td><td>2</td><td>1</td><td>3</td><td>3</td><td>5</td><td>6</td></tr><tr><td>3</td><td>3</td><td>3</td> <td>5</td><td>5</td><td>3</td><td>3</td><td>5</td><td>6</td><td>6</td><td>6</td><td>8</td><td>9</td></tr><tr><td>4< /td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td><td>1</td><td>5</td><td>6</td><td>5</td><td>5</td><td>6</td>< td>6</td></tr><tr><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>8</td><td>9</td><td>8</t d><td>8</td><td>9</td><td>9</td></tr><tr><td>6</td><td>3</td><td>3</td><td>2</td><td>2</td><td>1</td><td>1</td><td> 6</td><td>7</td><td>7</td><td>7</td><td>9</td><td>9</td></tr><tr><td>7</td><td>1</td><td>2</td><td>2</td><td>2</td> <td>3</td><td>3</td><td>5</td><td>6</td><td>5</td><td>4</td><td>6</td><td>6</td></tr><tr><td>8</td><td>1</td><td>3< /td><td>1</td><td>1</td><td>1</td><td>3</td><td>4</td><td>5</td><td>6</td><td>5</td><td>7</td><td>6</td></tr><tr><td >9</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>4</td><td>5</td><td>6</td><td>6</td><td>6</td><td>7</t d><td>7</td></tr><tr><td>10</td><td>8</td><td>8</td><td>8</td><td>8</td><td>6</td><td>6</td><td>9</td><td>8</td><td >9</td><td>9</td><td>10</td><td>10</td></tr><tr><td>平均</td><td>2.6</td><td>2.9</td><td>2.9</td><td>2.9</td><td >2.6</td><td>2.8</td><td>5.5</td><td>5.9</td><td>6</td><td>5.8</td><td>7.3</td><td>7.4</td></tr><tr><td>测试</td><td colspan="6">Intra_pq + Inter_apq > Intra_nq + Inter_anq</td><td colspan="6">Intra_pq + Inter_apq < Intra_nq + Inter_anq</td></tr><tr><td>F 检验</td><td colspan="6">0.16</td><td colspan="6">50.79***</td></tr></table>


Notes. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




笔记。 \* p < 0.1，\*\* p < 0.05，\*\*\* p < 0.01。


$( F = 3 7 . 7 7 , p < 0 . 0 1 )$ . Regarding risk measurement, the wear-in time exhibits no signi<sup>fi</sup>cant differences between positive and negative relationships. However, negative comparative relationships do have a longer wear-out time on risk $( F { = } 5 0 . 7 9 , p { < } 0 . 0 1 )$ . This <sup>fi</sup>nding is consistent with previous <sup>fi</sup>nancial studies (Hong et al. [31]) that reported that bad news travels slowly across the public domain and has a longer impact duration. Thus, H3a is partially supported by the sector return, and H3b is well supported by both the sector return and risk.




$( F = 3 7 . 7 7 , p < 0 . 0 1 )$ .在风险衡量方面，磨合时间在正向关系和负向关系之间没有表现出显着差异。然而，负面比较关系确实对风险$( F { = } 5 0 . 7 9 , p { < } 0 . 0 1 )$ 具有更长的磨损时间。这一<sup>发现</sup>与之前的<sup>金融</sup>金融研究（Hong等人[31]）一致，该研究报告称坏消息在公共领域传播缓慢，影响持续时间较长。因此，H3a 部分受到行业回报的支持，而 H3b 则受到行业回报和风险的良好支持。


To further investigate the immediate and cumulative impulsive response elasticities, we calculate the change in basis points (one basis point is one-hundredth of a percentage) of sector return or as a percentage of sector risk in response to one unit of unexpected change in sector interactive metrics [28,29]. Taking the <sup>fi</sup>nance sector (labeled as 7) as an example, Fig. 4 presents the accumulated impulse responses to sector interactive metrics. From the results presented in Tables 9 and 10, we observe that in the undirected network analysis, an unexpected increase in intra-sector closeness will predict a surge in daily sector return by 9.33 basis points in the short term and the accumulated impact of 12.52 basis points in




为了进一步研究即时和累积脉冲响应弹性，我们计算了行业回报基点的变化（一个基点是百分之一的百分比）或行业风险的百分比，以响应行业互动指标中一个单位的意外变化[28,29]。以<sup>金融</sup>金融部门（标记为7）为例，图4展示了对部门交互指标的累积脉冲响应。从表 9 和表 10 的结果来看，我们观察到，在无向网络分析中，行业内紧密度的意外增加将预测短期内行业日回报率将飙升 9.33 个基点，并在短期内累计影响 12.52 个基点。


20 days. However, an unexpected increase in the inter-sector closeness will immediately predict a decrease in the daily sector return by 9.06 basis points $\left( p < 0 . 0 1 \right)$ and accumulated impact of 12.08 basis points $( p < 0 . 1 )$ . In the positive network, the intrasector relationship has positive predictive value with returns both in the short term (11.19 basis points, $p { < } 0 . 1 )$ and the long term (14.52 basis points, $p { < } 0 . 1 )$ . In the negative network, the intrasector relationship is positively related immediately with risk (0.062 basis point, $p < 0 . 1 ) ;$ however, the inter-sector relationship is negatively related immediately with risk ( 0.070 basis point, $p { < } 0 . 1 )$ . Although these effects seem to be small in terms of the number of basis points, they have a substantial impact in terms of the dollar value. In monetary terms, the relationships between company network and sector performance could translate into a signi<sup>fi</sup>cant impact on the market capitalization of the sector [29]. For example, holding other factors constant, for the <sup>fi</sup>nance sector, one unit of unexpected increase in positive intra-sector could add approximately \$11.19 million to the average market capitalization in the short term and could accumulate approximately \$14.52 million over a 20-day period.




20天。然而，行业间紧密度的意外增加将立即预测每日行业回报率将下降 9.06 个基点 $\left( p < 0 . 0 1 \right)$ 并累积影响 12.08 个基点 $( p < 0 . 1 )$ 。在正向网络中，部门内关系具有正向预测值，短期回报（11.19 个基点，$p { < } 0 . 1 ）$ 和长期回报（14.52 个基点，$p { < } 0 . 1 ）$ 。在负网络中，部门内关系与风险直接正相关（0.062基点，$p<0.1）；$然而，部门间关系与风险直接负相关（0.070基点，$p{<}0.1）$。尽管从基点数量来看，这些影响似乎很小，但从美元价值来看，它们却产生了重大影响。从货币角度来看，公司网络和行业绩效之间的关系可能会对行业的市值产生重大影响[29]。例如，在其他因素不变的情况下，对于<sup>金融</sup>行业来说，行业内正值意外增加一单位可能会在短期内使平均市值增加约1,119万美元，并可能在20天内累积约1,452万美元。


![](/api/attachments/H2Y9VY8C/fulltext/images/45269b81ea6308333e6ef4171bafda08934c86e7eb42c8bcc35f13544c6111a8.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/45269b81ea6308333e6ef4171bafda08934c86e7eb42c8bcc35f13544c6111a8.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/5fb6442ef907d486e6c42b34bb0eff460c6967af7a664b677f5c5639e7286a2c.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/5fb6442ef907d486e6c42b34bb0eff460c6967af7a664b677f5c5639e7286a2c.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/72350fb3d2bbdb9ac261aa4be09f7db94d3c9e5f7d9ab3c1d59be03c50220ee7.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/72350fb3d2bbdb9ac261aa4be09f7db94d3c9e5f7d9ab3c1d59be03c50220ee7.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/8a72896f06ab96080711a912ff37020578e03dd1ae18ad40be25acb3d6320faf.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/8a72896f06ab96080711a912ff37020578e03dd1ae18ad40be25acb3d6320faf.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/683988e6c6409eb2d4931ecec6c116cc94db43ad9c31c884a881edfa5ab1e32e.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/683988e6c6409eb2d4931ecec6c116cc94db43ad9c31c884a881edfa5ab1e32e.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/f04aec888ce99144c27a40cadfccdb18eca114d6d948b683fc9b7a550679c147.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/f04aec888ce99144c27a40cadfccdb18eca114d6d948b683fc9b7a550679c147.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/9015d63a7e75b75e1a0051f8b076963df7618c83b78d1abecdb3a843483cc0de.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/9015d63a7e75b75e1a0051f8b076963df7618c83b78d1abecdb3a843483cc0de.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/36161bccd3d5489339fbc186713e2995773bb03727028b7fc36f7f1358183373.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/36161bccd3d5489339fbc186713e2995773bb03727028b7fc36f7f1358183373.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/45152af0e7ff2a0929bc1558d0004e143e5a3f0562bf57a7e033e485bdee027c.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/45152af0e7ff2a0929bc1558d0004e143e5a3f0562bf57a7e033e485bdee027c.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/8981cff01c22e9615e81d6b81fc7cb1b4f7b04ff52c8037f27c838c3991f5240.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/8981cff01c22e9615e81d6b81fc7cb1b4f7b04ff52c8037f27c838c3991f5240.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/f80acc51ce03f9cc40318207d24eace7cfbd17a3e9910f888f37273783bb1179.jpg)




![](/api/attachments/H2Y9VY8C/fulltext/images/f80acc51ce03f9cc40318207d24eace7cfbd17a3e9910f888f37273783bb1179.jpg)


![](/api/attachments/H2Y9VY8C/fulltext/images/fc9130909b5c02b0db9ad8fde02fd7a828d67a1fafeade6b85cae2d09ece242e.jpg)  
Fig. 4. Accumulated impulse response functions of social network metrics.




![](/api/attachments/H2Y9VY8C/fulltext/images/fc9130909b5c02b0db9ad8fde02fd7a828d67a1fafeade6b85cae2d09ece242e.jpg)  
图 4. 社交网络指标的累积脉冲响应函数。


Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005




请在媒体上引用这篇文章：K. Chen 等人，公司比较网络对股票行业表现的动态预测能力，Inf。管理。 （2016），http://dx.doi.org/10.1016/j.im.2016.07.005


K. Chen et al. / Information & Management xxx (2016) xxx–xxx




K.陈等人。 / 信息与管理 xxx (2016) xxx–xxx


Table 12  
Table 9  
Impulse response of return to company network metrics.




表12  
表9  
返回公司网络指标的脉冲响应。


<table><tr><td colspan="7">Immediate</td><td colspan="6">Accumulate</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>12.66*</td><td>-12.59*</td><td>14.39*</td><td>-14.59*</td><td>-3.84</td><td>2.89</td><td>12.75*</td><td>-12.79*</td><td>14.86*</td><td>-15.16*</td><td>-4.89</td><td>4.13</td></tr><tr><td>2</td><td>-2.32</td><td>2.69</td><td>-3.06</td><td>3.16</td><td>2.46</td><td>-2.01</td><td>-3.54</td><td>3.14</td><td>-4.26</td><td>3.63</td><td>1.01</td><td>-1.44</td></tr><tr><td>3</td><td>0.573</td><td>-0.852</td><td>2.21</td><td>-2.82</td><td>-3.44</td><td>3.19</td><td>2.32</td><td>-3.28</td><td>4.58</td><td>-6.13</td><td>-7.96</td><td>7.85</td></tr><tr><td>4</td><td>-0.105</td><td>2.85</td><td>-2.14</td><td>5.07</td><td>4.75</td><td>-4.42</td><td>-1.33</td><td>4.34</td><td>-3.32</td><td>6.51</td><td>4.53</td><td>-4.00</td></tr><tr><td>5</td><td>-25.35**</td><td>26.06**</td><td>-20.16*</td><td>19.84*</td><td>-0.196</td><td>-0.67</td><td>-28.62*</td><td>29.33*</td><td>-26.66*</td><td>26.36*</td><td>-0.73</td><td>-0.34</td></tr><tr><td>6</td><td>23.02*</td><td>-21.94*</td><td>14.84</td><td>-14.31</td><td>24.23</td><td>-23.39</td><td>27.83</td><td>-26.41</td><td>19.56</td><td>-18.84</td><td>28.21</td><td>-27.24</td></tr><tr><td>7</td><td>9.33</td><td>-9.06***</td><td>11.19*</td><td>-8.62</td><td>-1.06</td><td>0.544</td><td>12.52</td><td>-12.08*</td><td>14.52*</td><td>-11.92</td><td>-2.90</td><td>2.60</td></tr><tr><td>8</td><td>-8.02</td><td>8.03</td><td>-7.86</td><td>8.89</td><td>-7.32</td><td>16.11</td><td>-5.61</td><td>5.93</td><td>-5.19</td><td>6.41</td><td>-11.42</td><td>20.58</td></tr><tr><td>9</td><td>-3.42</td><td>8.49</td><td>-3.69</td><td>7.78</td><td>10.49</td><td>-4.84</td><td>-1.19</td><td>7.25</td><td>-1.53</td><td>7.47</td><td>15.52</td><td>-6.32</td></tr><tr><td>10</td><td>21.48*</td><td>-21.89*</td><td>21.78*</td><td>-22.5*</td><td>8.84</td><td>-9.11</td><td>21.38</td><td>-21.88</td><td>22.4</td><td>-23.31</td><td>4.27</td><td>-4.43</td></tr></table>




<table><tr><td colspan="7">立即</td><td colspan="6">累积</td></tr><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</ td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr> <td>1</td><td>12.66*</td><td>-12.59*</td><td>14.39*</td><td>-14.59* </td><td>-3.84</td><td>2.89</td><td>12.75*</td><td>-12.79*</td><td>1 4.86*</td><td>-15.16*</td><td>-4.89</td><td>4.13</td></tr><tr><td>2< /td><td>-2.32</td><td>2.69</td><td>-3.06</td><td>3.16</td><td>2.46</td> td><td>-2.01</td><td>-3.54</td><td>3.14</td><td>-4.26</td><td>3.63< /td><td>1.01</td><td>-1.44</td></tr><tr><td>3</td><td>0.573</td><td> -0.852</td><td>2.21</td><td>-2.82</td><td>-3.44</td><td>3.19</td><td >2.32</td><td>-3.28</td><td>4.58</td><td>-6.13</td><td>-7.96</td><td >7.85</td></tr><tr><td>4</td><td>-0.105</td><td>2.85</td><td>-2.14< /td><td>5.07</td><td>4.75</td><td>-4.42</td><td>-1.33</td><td>4.34</td> td><td>-3.32</td><td>6.51</td><td>4.53</td><td>-4.00</td></tr><tr><t d>5</td><td>-25.35**</td><td>26.06**</td><td>-20.16*</td><td>19.84*< /td><td>-0.196</td><td>-0.67</td><td>-28.62*</td><td>29.33*</td><td >-26.66*</td><td>26.36*</td><td>-0.73</td><td>-0.34</td></tr><tr><td >6</td><td>23.02*</td><td>-21.94*</td><td>14.84</td><td>-14.31</td> <td>24.23</td><td>-23.39</td><td>27.83</td><td>-26.41</td><td>19.56< /td><td>-18.84</td><td>28.21</td><td>-27.24</td></tr><tr><td>7</td> <td>9.33</td><td>-9.06***</td><td>11.19*</td><td>-8.62</td><td>-1.06 </td><td>0.544</td><td>12.52</td><td>-12.08*</td><td>14.52*</td><td> -11.92</td><td>-2.90</td><td>2.60</td></tr><tr><td>8</td><td>-8.02</td> td><td>8.03</td><td>-7.86</td><td>8.89</td><td>-7.32</td><td>16.11< /td><td>-5.61</td><td>5.93</td><td>-5.19</td><td>6.41</td><td>-11.42 </td><td>20.58</td></tr><tr><td>9</td><td>-3.42</td><td>8.49</td><td >-3.69</td><td>7.78</td><td>10.49</td><td>-4.84</td><td>-1.19</td><t d>7.25</td><td>-1.53</td><td>7.47</td><td>15.52</td><td>-6.32</td>< /tr><tr><td>10</td><td>21.48*</td><td>-21.89*</td><td>21.78*</td><td >-22.5*</td><td>8.84</td><td>-9.11</td><td>21.38</td><td>-21.88</td> <td>22.4</td><td>-23.31</td><td>4.27</td><td>-4.43</td></tr></table>


Notes: The coef<sup>fi</sup>cients of returns are in basis points (1 basis point = hundredth of a percentage). \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




注：回报率系数以基点为单位（1 个基点=百分之一）。 \* p < 0.1，\*\* p < 0.05，\*\*\* p < 0.01。


Impulse response of risk to company network metrics.




风险对公司网络指标的脉冲响应。


<table><tr><td colspan="7">Immediate</td><td colspan="6">Accumulate</td></tr><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.116*</td><td>-0.118*</td><td>0.113*</td><td>-0.114*</td><td>0.012</td><td>-0.016</td><td>0.131**</td><td>-0.133**</td><td>0.125**</td><td>-0.127**</td><td>0.027</td><td>-0.031</td></tr><tr><td>2</td><td>0.015</td><td>-0.017</td><td>-0.026</td><td>0.022</td><td>0.122***</td><td>-0.119***</td><td>0.011</td><td>-0.015</td><td>-0.041</td><td>0.037</td><td>0.172**</td><td>-0.175**</td></tr><tr><td>3</td><td>-0.046</td><td>0.055</td><td>-0.004</td><td>0.011</td><td>-0.088**</td><td>0.090**</td><td>-0.075</td><td>0.082</td><td>-0.004</td><td>0.009</td><td>-0.169*</td><td>0.169*</td></tr><tr><td>4</td><td>-0.096***</td><td>0.088***</td><td>-0.105***</td><td>0.089***</td><td>0.010</td><td>-0.0008</td><td>-0.163***</td><td>0.159***</td><td>-0.173***</td><td>0.157***</td><td>-0.015</td><td>0.028</td></tr><tr><td>5</td><td>-0.049</td><td>0.048</td><td>-0.025</td><td>0.021</td><td>0.016</td><td>-0.021</td><td>-0.056</td><td>0.055</td><td>-0.036</td><td>0.031</td><td>0.039</td><td>-0.048</td></tr><tr><td>6</td><td>0.05</td><td>-0.045</td><td>0.074</td><td>-0.072</td><td>-0.015</td><td>0.017</td><td>0.025</td><td>-0.019</td><td>0.068</td><td>-0.065</td><td>-0.081</td><td>0.084</td></tr><tr><td>7</td><td>0.012</td><td>-0.003</td><td>-0.014</td><td>0.016</td><td>0.062*</td><td>-0.070*</td><td>-0.002</td><td>0.007</td><td>-0.030</td><td>0.029</td><td>0.065</td><td>-0.078</td></tr><tr><td>8</td><td>0.027</td><td>-0.015</td><td>0.042</td><td>-0.037</td><td>-0.203*</td><td>0.181*</td><td>0.032</td><td>-0.016</td><td>0.048</td><td>-0.044</td><td>-0.220**</td><td>0.213*</td></tr><tr><td>9</td><td>-0.027</td><td>0.057</td><td>-0.065</td><td>0.087</td><td>0.122</td><td>-0.150</td><td>0.103</td><td>-0.091</td><td>0.079</td><td>-0.054</td><td>0.121</td><td>-0.144</td></tr><tr><td>10</td><td>-0.003</td><td>0.001</td><td>0.005</td><td>-0.008</td><td>-0.084</td><td>0.081</td><td>-0.031</td><td>0.027</td><td>-0.014</td><td>0.008</td><td>-0.143</td><td>0.139</td></tr></table>




<table><tr><td colspan="7">立即</td><td colspan="6">累积</td></tr><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td >inter_anq</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td >0.116*</td><td>-0.118*</td><td>0.113*</td><td>-0.114*</td><td>0.012</ td><td>-0.016</td><td>0.131**</td><td>-0.133**</td><td>0.125**</td><td> -0.127**</td><td>0.027</td><td>-0.031</td></tr><tr><td>2</td><td>0.015< /td><td>-0.017</td><td>-0.026</td><td>0.022</td><td>0.122***</td><td>-0 .119***</td><td>0.011</td><td>-0.015</td><td>-0.041</td><td>0.037</td> <td>0.172**</td><td>-0.175**</td></tr><tr><td>3</td><td>-0.046</td><td> 0.055</td><td>-0.004</td><td>0.011</td><td>-0.088**</td><td>0.090**</td ><td>-0.075</td><td>0.082</td><td>-0.004</td><td>0.009</td><td>-0.169*< /td><td>0.169*</td></tr><tr><td>4</td><td>-0.096***</td><td>0.088***</ td><td>-0.105***</td><td>0.089***</td><td>0.010</td><td>-0.0008</td><td >-0.163***</td><td>0.159***</td><td>-0.173***</td><td>0.157***</td><td> -0.015</td><td>0.028</td></tr><tr><td>5</td><td>-0.049</td><td>0.048</t d><td>-0.025</td><td>0.021</td><td>0.016</td><td>-0.021</td><td>-0.056 </td><td>0.055</td><td>-0.036</td><td>0.031</td><td>0.039</td><td>-0.04 8</td></tr><tr><td>6</td><td>0.05</td><td>-0.045</td><td>0.074</td><td> -0.072</td><td>-0.015</td><td>0.017</td><td>0.025</td><td>-0.019</td><t d>0.068</td><td>-0.065</td><td>-0.081</td><td>0.084</td></tr><tr><td>7 </td><td>0.012</td><td>-0.003</td><td>-0.014</td><td>0.016</td><td>0.06 2*</td><td>-0.070*</td><td>-0.002</td><td>0.007</td><td>-0.030</td><td> 0.029</td><td>0.065</td><td>-0.078</td></tr><tr><td>8</td><td>0.027</td ><td>-0.015</td><td>0.042</td><td>-0.037</td><td>-0.203*</td><td>0.181 *</td><td>0.032</td><td>-0.016</td><td>0.048</td><td>-0.044</td><td>-0。 220**</td><td>0.213*</td></tr><tr><td>9</td><td>-0.027</td><td>0.057</t d><td>-0.065</td><td>0.087</td><td>0.122</td><td>-0.150</td><td>0.103</td> td><td>-0.091</td><td>0.079</td><td>-0.054</td><td>0.121</td><td>-0.14 4</td></tr><tr><td>10</td><td>-0.003</td><td>0.001</td><td>0.005</td><t d>-0.008</td><td>-0.084</td><td>0.081</td><td>-0.031</td><td>0.027</td> <td>-0.014</td><td>0.008</td><td>-0.143</td><td>0.139</td></tr></table>


Notes: The coef<sup>fi</sup>cients of risk are in basis points (1 basis point = hundredth of a percentage). \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.




注：风险系数以基点为单位（1 个基点=百分之一）。 \* p < 0.1，\*\* p < 0.05，\*\*\* p < 0.01。


## 5.5. Relative importance of sector-interactive metrics




## 5.5。部门互动指标的相对重要性


We assess the relative impact of the company network metrics on sector performance using GFEVD. The GFEVD estimates are derived using the following algorithm:




我们使用 GFEVD 评估公司网络指标对部门绩效的相对影响。 GEVD 估计值是使用以下算法得出的：


$$
\theta_ {i, j} (t) = \frac {\sum_ {k = 0} ^ {t} \left(\psi_ {i , j} (k)\right) ^ {2}}{\sum_ {k = 0} ^ {t} \sum_ {j = 0} ^ {m} \left(\psi_ {i , j} (t)\right) ^ {2}}, i, j = 1, \dots , m.\tag{8}
$$




$$
\theta_ {i, j} (t) = \frac {\sum_ {k = 0} ^ {t} \left(\psi_ {i , j} (k)\right) ^ {2}}{\sum_ {k = 0} ^ {t} \sum_ {j = 0} ^ {m} \left(\psi_ {i , j} (t)\right) ^ {2}}, i, j = 1, \dots , m.\标签{8}
$$


GFEVD can identify the relative predictive value of all the company network metrics. It is appropriate to test the hypotheses proposed in our article. The relative value of the endogenous variables is established based on GFEVD over 20 days, which is intended to reduce the short-term functions, as suggested in previous research [28,29].




GEFEVD 可以识别所有公司网络指标的相对预测值。检验我们文章中提出的假设是适当的。内生变量的相对值是根据 20 天的 GFEVD 确定的，目的是减少短期函数，如先前研究 [28,29] 所示。


Variance decomposition of return explained by company network metrics




公司网络指标解释的回报方差分解


<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.26</td><td>0.58</td><td>0.12</td><td>0.09</td><td>0.21</td><td>0.41</td></tr><tr><td>2</td><td>0.09</td><td>2.18</td><td>0.29</td><td>1.93</td><td>0.76</td><td>3.20</td></tr><tr><td>3</td><td>0.39</td><td>1.40</td><td>0.95</td><td>2.32</td><td>2.25</td><td>0.30</td></tr><tr><td>4</td><td>0.10</td><td>0.08</td><td>0.36</td><td>0.29</td><td>1.10</td><td>0.65</td></tr><tr><td>5</td><td>3.38</td><td>2.52</td><td>1.57</td><td>2.61</td><td>4.83</td><td>0.57</td></tr><tr><td>6</td><td>1.82</td><td>2.05</td><td>1.01</td><td>1.67</td><td>0.17</td><td>0.93</td></tr><tr><td>7</td><td>1.03</td><td>0.37</td><td>0.50</td><td>3.77</td><td>0.13</td><td>1.25</td></tr><tr><td>8</td><td>0.99</td><td>0.73</td><td>1.13</td><td>0.47</td><td>0.17</td><td>2.60</td></tr><tr><td>9</td><td>0.38</td><td>0.56</td><td>0.18</td><td>0.67</td><td>0.44</td><td>1.81</td></tr><tr><td>10</td><td>2.25</td><td>8.78</td><td>2.46</td><td>8.30</td><td>2.54</td><td>2.14</td></tr><tr><td>Average</td><td>1.07</td><td>1.93</td><td>0.86</td><td>2.21</td><td>1.26</td><td>1.39</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F-test</td><td colspan="6">26.43***</td></tr><tr><td>Testing</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F-test</td><td colspan="6">-0.29</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ intra_pq+ intra_nq</td></tr><tr><td>F-test</td><td colspan="6">2.93*</td></tr></table>




<table><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td> 0.26</td><td>0.58</td><td>0.12</td><td>0.09</td><td>0.21</td><td>0.41</td></t r><tr><td>2</td><td>0.09</td><td>2.18</td><td>0.29</td><td>1.93</td><td>0.76< /td><td>3.20</td></tr><tr><td>3</td><td>0.39</td><td>1.40</td><td>0.95</td><t d>2.32</td><td>2.25</td><td>0.30</td></tr><tr><td>4</td><td>0.10</td><td>0.08 </td><td>0.36</td><td>0.29</td><td>1.10</td><td>0.65</td></tr><tr><td>5</td>< td>3.38</td><td>2.52</td><td>1.57</td><td>2.61</td><td>4.83</td><td>0.57</td> </tr><tr><td>6</td><td>1.82</td><td>2.05</td><td>1.01</td><td>1.67</td><td>0。 17</td><td>0.93</td></tr><tr><td>7</td><td>1.03</td><td>0.37</td><td>0.50</td ><td>3.77</td><td>0.13</td><td>1.25</td></tr><tr><td>8</td><td>0.99</td><td>0 .73</td><td>1.13</td><td>0.47</td><td>0.17</td><td>2.60</td></tr><tr><td>9</t d><td>0.38</td><td>0.56</td><td>0.18</td><td>0.67</td><td>0.44</td><td>1.81</td> td></tr><tr><td>10</td><td>2.25</td><td>8.78</td><td>2.46</td><td>8.30</td><t d>2.54</td><td>2.14</td></tr><tr><td>平均</td><td>1.07</td><td>1.93</td><t d>0.86</td><td>2.21</td><td>1.26</td><td>1.39</td></tr><tr><td>测试</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F 测试</td><td colspan="6">26.43***</td></tr><tr><td>测试</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F 测试</td><td colspan="6">-0.29</td></tr><tr><td>测试</td><td colspan="6">intra_uq+intra_pq+intra_nq</td></tr><tr><td>F 测试</td><td colspan="6">2.93*</td></tr></table>


Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.




注：回报系数为百分比值。 $^ { * } p < 0 。 1 , ^ { * * } p < 0 。 0 5 , ^ { * * * }$ p < 0.01。


The GFEVD of return and risk is used to assess the importance of sector interactive metrics, and Tables 11 and 12 provide the results. The results suggest the order of contributions in predicting sector return to be inter\_apq (2.21%), inter\_auq (1.93%), inter\_anq (1.39%), intra\_nq (1.26%), intra\_uq (1.07%), and intra\_pq (0.86%). Similarly, in predicting sector risk, the results of the contributions of the sector interactive metrics are ordered as inter\_apq (1.87%), inter\_auq (1.79%), inter\_anq (1.44%), intra\_uq (1.38%), intra\_pq (1.27%), and intra\_nq (1.01%). On the basis of these results, we acknowledge that the total directed network metrics (the positive




回报和风险的 GFEVD 用于评估部门交互指标的重要性，表 11 和表 12 提供了结果。结果表明，预测部门回报的贡献顺序为 inter\_apq (2.21%)、inter\_auq (1.93%)、inter\_anq (1.39%)、intra\_nq (1.26%)、intra\_uq (1.07%) 和 intra\_pq (0.86%)。同样，在预测行业风险时，行业交互指标的贡献结果排序为 inter\_apq (1.87%)、inter\_auq (1.79%)、inter\_anq (1.44%)、intra\_uq (1.38%)、intra\_pq (1.27%) 和 intra\_nq (1.01%)。根据这些结果，我们承认总有向网络指标（正向网络指标）


Variance decomposition of risk explained by company network metrics.




由公司网络指标解释的风险方差分解。


<table><tr><td>Sector</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td>0.92</td><td>1.02</td><td>0.25</td><td>0.64</td><td>1.50</td><td>0.09</td></tr><tr><td>2</td><td>0.08</td><td>0.12</td><td>0.89</td><td>0.42</td><td>0.36</td><td>2.38</td></tr><tr><td>3</td><td>0.34</td><td>1.46</td><td>2.41</td><td>3.38</td><td>1.45</td><td>0.64</td></tr><tr><td>4</td><td>3.80</td><td>0.17</td><td>0.21</td><td>3.93</td><td>0.90</td><td>0.22</td></tr><tr><td>5</td><td>0.93</td><td>0.30</td><td>1.20</td><td>0.94</td><td>0.78</td><td>0.78</td></tr><tr><td>6</td><td>1.35</td><td>5.30</td><td>4.00</td><td>0.90</td><td>0.60</td><td>0.63</td></tr><tr><td>7</td><td>1.80</td><td>0.87</td><td>0.51</td><td>0.49</td><td>0.43</td><td>2.19</td></tr><tr><td>8</td><td>0.30</td><td>2.88</td><td>0.61</td><td>0.87</td><td>0.27</td><td>0.51</td></tr><tr><td>9</td><td>1.28</td><td>1.08</td><td>0.48</td><td>1.53</td><td>1.29</td><td>0.97</td></tr><tr><td>10</td><td>2.96</td><td>4.65</td><td>2.17</td><td>5.62</td><td>2.54</td><td>5.99</td></tr><tr><td>Average</td><td>1.38</td><td>1.79</td><td>1.27</td><td>1.87</td><td>1.01</td><td>1.44</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F-test</td><td colspan="6">6.48***</td></tr><tr><td>Testing</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F-test</td><td colspan="6">-1.14</td></tr><tr><td>Testing</td><td colspan="6">intra_uq+ intra_pq+ intra_nq</td></tr><tr><td>F-test</td><td colspan="6">2.63*</td></tr></table>




<table><tr><td>扇区</td><td>intra_uq</td><td>inter_auq</td><td>intra_pq</td><td>inter_apq</td><td>intra_nq</td><td>inter_anq</td></tr><tr><td>1</td><td> 0.92</td><td>1.02</td><td>0.25</td><td>0.64</td><td>1.50</td><td>0.09</td></t r><tr><td>2</td><td>0.08</td><td>0.12</td><td>0.89</td><td>0.42</td><td>0.36< /td><td>2.38</td></tr><tr><td>3</td><td>0.34</td><td>1.46</td><td>2.41</td><t d>3.38</td><td>1.45</td><td>0.64</td></tr><tr><td>4</td><td>3.80</td><td>0.17 </td><td>0.21</td><td>3.93</td><td>0.90</td><td>0.22</td></tr><tr><td>5</td>< td>0.93</td><td>0.30</td><td>1.20</td><td>0.94</td><td>0.78</td><td>0.78</td> </tr><tr><td>6</td><td>1.35</td><td>5.30</td><td>4.00</td><td>0.90</td><td>0。 60</td><td>0.63</td></tr><tr><td>7</td><td>1.80</td><td>0.87</td><td>0.51</td ><td>0.49</td><td>0.43</td><td>2.19</td></tr><tr><td>8</td><td>0.30</td><td>2 .88</td><td>0.61</td><td>0.87</td><td>0.27</td><td>0.51</td></tr><tr><td>9</t d><td>1.28</td><td>1.08</td><td>0.48</td><td>1.53</td><td>1.29</td><td>0.97</td> td></tr><tr><td>10</td><td>2.96</td><td>4.65</td><td>2.17</td><td>5.62</td><t d>2.54</td><td>5.99</td></tr><tr><td>平均</td><td>1.38</td><td>1.79</td><t d>1.27</td><td>1.87</td><td>1.01</td><td>1.44</td></tr><tr><td>测试</td><td colspan="6">intra_uq+ inter_auq</td></tr><tr><td>F 测试</td><td colspan="6">6.48***</td></tr><tr><td>测试</td><td colspan="6">intra_pq+ inter_apq</td></tr><tr><td>F 测试</td><td colspan="6">-1.14</td></tr><tr><td>测试</td><td colspan="6">intra_uq+intra_pq+intra_nq</td></tr><tr><td>F 测试</td><td colspan="6">2.63*</td></tr></table>


Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.




注：回报系数为百分比值。 $^ { * } p < 0 。 1 , ^ { * * } p < 0 。 0 5 , ^ { * * * }$ p < 0.01。


Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005




请在媒体上引用这篇文章：K. Chen 等人，公司比较网络对股票行业表现的动态预测能力，Inf。管理。 （2016），http://dx.doi.org/10.1016/j.im.2016.07.005


and negative network metrics) contribute toward a greater proportion of the variance than the total undirected network metrics (5.72% versus 3.00% for return and 5.59% versus 3.17% for risk). According to the F statistics, the differences are statistically signi<sup>fi</sup>cant $( F = 2 6 . 4 3 , p < 0 . 0 1$ for return and $F = 6 . 4 8 , p < 0 . 0 1$ for risk), thereby supporting H2a because comparative analysis provides a stronger network indicator than closeness metrics.




和负网络指标）比总无向网络指标对方差的贡献更大（回报率分别为 5.72% 和 3.00%，风险分别为 5.59% 和 3.17%）。根据 F 统计数据，差异在统计上显着<sup>fi</sup>$（对于回报，F = 2 6 . 4 3 , p < 0 . 0 1$ 对于风险，$F = 6 . 4 8 , p < 0 . 0 1$），从而支持 H2a，因为比较分析提供了比紧密度指标更强的网络指标。


Furthermore, the total inter-sector metrics, including inter\_auq, inter\_apq, and inter\_anq, consist of a greater proportion of the variance than the total intra-sector metrics, including intra\_uq, intra\_pq, and intra\_nq (5.53% versus 3.19% for return and 5.10% versus 3.66% for risk). These differences are statistically signi<sup>fi</sup>cant according to the F statistics $( F { = } 2 . 9 3 , p { < } 0 . 1$ for return and F=2.63, $p < 0 . 1$ for risk). Thus, these results support H1b in that the intersector metrics have greater predictive power than the intra-sector metrics.




此外，总的部门间指标（包括 inter\_auq、inter\_apq 和 inter\_anq）比总的部门内指标（包括 intra\_uq、intra\_pq 和 intra\_nq）包含更大比例的方差（回报为 5.53% vs 3.19%，风险为 5.10% vs 3.66%）。根据 F 统计数据 $（F { = } 2 . 9 3 , p { < } 0 . 1$ 表示回报，F=2.63, $p < 0 . 1$ 表示风险），这些差异具有统计显着性。因此，这些结果支持 H1b，因为部门间指标比部门内指标具有更大的预测能力。


However, the relationship between the positive and negative network metrics is not supported. In a variance decomposition of return, the total negative network metrics account for a larger proportion of variance than the average total positive network metrics across the sectors, and adverse results occur in the variance decomposition of risk. The results are not statistically signi<sup>fi</sup>cant.




但是，不支持正负网络指标之间的关系。在收益方差分解中，总负网络指标所占方差的比例大于各部门平均总正网络指标的方差，在风险方差分解中会出现不利结果。结果在统计上并不显着<sup>显着</sup>。


## 5.6. Robustness testing




## 5.6。稳健性测试


We conduct several tests to ascertain the robustness of the results. We use alternative measurements of the inter-sector and intra-sector interactions, in addition to different subsamples of industries for the robustness tests. First, we replace the modularity measurement with the weighted link number to gauge the sector interaction. The intra-sector interaction is measured by the weighted link number among stocks within a sector. The metrics intra\_uln, intra\_pln, and intra\_nln represent the intra-sector weighted link numbers for the undirected network, positive network, and negative network, respectively. Similarly, the intersector interaction is gauged by the weighted link number among stocks that belong to different sectors. The metrics inter\_auln, inter\_apln, and inter\_anln are the inter-sector weighted link numbers for the undirected network, positive network, and negative network, respectively. Because the negative links are less than the positive links, the metrics of the undirected network variables (intra\_uln and inter\_auln) are strongly correlated with the metrics of the positive network variables (intra\_pln and inter\_apln). In this case, we cannot place all the variables into one VARX model. Therefore, we construct two models: model 1 for the undirected company network and model 2 for the directed company network. This construction enables us to compare two models using the adjusted $R ^ { 2 } [ 3 5 , 4 8 ]$




我们进行了多项测试以确定结果的稳健性。除了行业的不同子样本进行稳健性测试之外，我们还使用行业间和行业内相互作用的替代测量方法。首先，我们用加权链接数代替模块化测量来衡量部门交互。行业内的相互作用是通过行业内股票之间的加权链接数来衡量的。度量intra\_uln、intra\_pln和intra\_nln分别表示无向网络、正向网络和负向网络的扇区内加权链路数。同样，行业间的相互作用是通过属于不同行业的股票之间的加权链接数来衡量的。度量 inter\_auln、inter\_apln 和 inter\_anln 分别是无向网络、正网络和负网络的扇区间加权链路数。由于负链接少于正链接，无向网络变量（intra\_uln 和 inter\_auln）的度量与正网络变量（intra\_pln 和 inter\_apln）的度量强相关。在这种情况下，我们无法将所有变量放入一个 VARX 模型中。因此，我们构建了两个模型：模型1为无向公司网络，模型2为有向公司网络。这种结构使我们能够使用调整后的 $R ^ { 2 } [ 3 5 , 4 8 ]$ 来比较两个模型


$$
\begin{array}{c} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {U} L N _ {t} \\ \text {Inter} _ {A} U L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 4} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 4} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 4} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 4} ^ {k} \end{array} \right] \\ \cdot \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {U} L N _ {t - k} \\ \text {Inter} _ {A} U L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \end{array} \right] \end{array}\tag{12}
$$




$$
\begin{array}{c} \left[ \begin{array}{c} \text {返回} _ {t} \\ \text {风险} _ {t} \\ \text {Intra} _ {U} L N _ {t} \\ \text {Inter} _ {A} U L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 4} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 4} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 4} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 4} ^ {k} \end{array} \right] \\ \cdot \left[ \begin{array}{c} \text {回报} _ {t - k} \\ \text {风险} _ {t - k} \\ \text {内部} _ {U} L N _ {t - k} \\ \text {Inter} _ {A} U L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \end{array} \right] \end{array}\tag{12}
$$


Model 1




型号1


11




（代码、公式、图片引用或其他非语言内容，无需翻译。）


Using the two models, we obtain the following results. As indicated in Table 13, the $R ^ { 2 }$ value of model 2 is statistically signi<sup>fi</sup>cantly greater than the $R ^ { 2 }$ of model $\cdot \ ( F { = } 9 . 5 9 , \ p { < } 0 . 0 1$ for return and $F { = } 5 . 9 0 , p { < } 0 . 0 1$ for risk), thus supporting H2a in that the competitive analysis provides a stronger network indicator than the closeness metrics. Additionally, the inter-sector metrics (inter\_apln and inter\_anln) account for signi<sup>fi</sup>cantly greater proportions of the variance than the intra-sector metrics (intra\_pln and intra\_nln) in model 2: 2.53% versus 1.81% for return (F=8.03, $p < 0 . 0 1 $ ) and 5.57% versus 4.23% for risk $( F { = } 2 . 8 7 , p { < } 0 . 1 )$ . To further test the dynamic effects of the company comparative network, we calculate the wear-in and wear-out times in model 2. As indicated in Tables 14 and 15, the negative network metrics (intra\_nln and inter\_anln) have signi<sup>fi</sup>cantly shorter wear-in times than the positive network metrics (intra\_pln and inter\_apln): 3.1 days versus 4.0 days for return (F=4.31, $p < 0 . 0 5 )$ and 3.5 days versus 4.7 days for risk $( F { = } 3 . 2 7 , p { < } 0 . 0 5 )$ . The negative network metrics have signi<sup>fi</sup>cantly longer wear-out times than the positive network




使用这两个模型，我们得到以下结果。如表 13 所示，模型 2 的 $R ^ { 2 }$ 值在统计上显着大于模型 $\cdot \ ( F { = } 9 . 5 9 , \ p { < } 0 . 0 1$ 的返回值和 $F { = } 5 . 9 0 , p { < } 0 的 $R ^ { 2 }$ 值. 0 1$ 风险），因此支持 H2a，因为竞争分析提供了比紧密度指标更强的网络指标。此外，在模型 2 中，部门间指标（inter\_apln 和 inter\_anln）所占的方差比例显着高于部门内指标（intra\_pln 和 intra\_nln）：回报率分别为 2.53% 和 1.81%（F=8.03，$p < 0 . 0 1 $）和 5.57%风险为 4.23% $( F { = } 2 . 8 7 , p { < } 0 . 1 )$ 。为了进一步测试公司比较网络的动态效应，我们计算了模型 2 中的磨合时间和磨损时间。如表 14 和表 15 所示，负网络指标（intra\_nln 和 inter\_anln）的磨合时间明显短于正网络指标（intra\_pln 和 inter\_apln）：回报为 3.1 天，而回报为 4.0 天(F=4.31, $p < 0 . 0 5 )$ 和 3.5 天与 4.7 天的风险 $( F { = } 3 . 2 7 , p { < } 0 . 0 5 )$ 。负网络指标的磨损时间明显长于正网络指标


$$
\begin{array}{c} \left[ \begin{array}{c} \text {Return} _ {t} \\ \text {Risk} _ {t} \\ \text {Intra} _ {P} L N _ {t} \\ \text {Inter} _ {A} P L N _ {t} \\ \text {Intra} _ {N} L N _ {t} \\ \text {Inter} _ {A} N L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 6} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 6} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 6} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 6} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 6} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 6} ^ {k} \end{array} \right] \\ . \left[ \begin{array}{c} \text {Return} _ {t - k} \\ \text {Risk} _ {t - k} \\ \text {Intra} _ {P} L N _ {t - k} \\ \text {Inter} _ {A} P L N _ {t - k} \\ \text {Intra} _ {N} L N _ {t - k} \\ \text {Inter} _ {A} N L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \end{array} \right] \end{array}
$$




$$
\begin{array}{c} \left[ \begin{array}{c} \text {回报} _ {t} \\ \text {风险} _ {t} \\ \text {Intra} _ {P} L N _ {t} \\ \text {Inter} _ {A} P L N _ {t} \\ \text {Intra} _ {N} L N _ {t} \\ \text {Inter} _ {A} N L N _ {t} \end{array} \right] = \left[ \begin{array}{c} \alpha_ {1} + \delta_ {1} t \\ \alpha_ {2} + \delta_ {2} t \\ \alpha_ {3} + \delta_ {3} t \\ \alpha_ {4} + \delta_ {4} t \\ \alpha_ {5} + \delta_ {5} t \\ \alpha_ {6} + \delta_ {6} t \end{array} \right] + \sum_ {k = 1} ^ {K} \left[ \begin{array}{c} \phi_ {1, 1} ^ {k} \dots \phi_ {1, 6} ^ {k} \\ \phi_ {2, 1} ^ {k} \dots \phi_ {2, 6} ^ {k} \\ \phi_ {3, 1} ^ {k} \dots \phi_ {3, 6} ^ {k} \\ \phi_ {4, 1} ^ {k} \dots \phi_ {4, 6} ^ {k} \\ \phi_ {5, 1} ^ {k} \dots \phi_ {5, 6} ^ {k} \\ \phi_ {6, 1} ^ {k} \dots \phi_ {6, 6} ^ {k} \end{array} \right] \\ 。 \left[ \begin{array}{c} \text {返回} _ {t - k} \\ \text {风险} _ {t - k} \\ \text {内部} _ {P} L N _ {t - k} \\ \text {中间} _ {A} P L N _ {t - k} \\ \text {内部} _ {N} L N _ {t - k} \\ \text {内部} _ {A} N L N _ {t - k} \end{array} \right] + \tau_ {1, 1} x _ {1 t} + \left[ \begin{array}{c} \varepsilon_ {1 t} \\ \varepsilon_ {2 t} \\ \varepsilon_ {3 t} \\ \varepsilon_ {4 t} \\ \varepsilon_ {5 t} \\ \varepsilon_ {6 t} \end{array} \right] \end{array}
$$


Model 2




型号2


Results of the VARX model with network link metrics.




具有网络链路指标的 VARX 模型的结果。


<table><tr><td rowspan="2">Sector</td><td colspan="2">Return</td><td colspan="2">Risk</td><td colspan="4">Variance Decomposition of Return</td></tr><tr><td> $R^21$ </td><td> $R^22$ </td><td> $R^21$ </td><td> $R^22$ </td><td>intra_pIn</td><td>inter_apIn</td><td>intra_nIn</td><td>inter_anIn</td></tr><tr><td>1</td><td>0.021</td><td>0.024</td><td>0.043</td><td>0.045</td><td>0.050</td><td>0.119</td><td>0.135</td><td>0.371</td></tr><tr><td>2</td><td>0.068</td><td>0.095</td><td>0.153</td><td>0.177</td><td>1.448</td><td>4.002</td><td>1.875</td><td>2.597</td></tr><tr><td>3</td><td>0.050</td><td>0.072</td><td>0.247</td><td>0.264</td><td>1.156</td><td>0.673</td><td>0.982</td><td>2.075</td></tr><tr><td>4</td><td>0.112</td><td>0.176</td><td>0.300</td><td>0.384</td><td>2.977</td><td>2.628</td><td>2.441</td><td>4.701</td></tr><tr><td>5</td><td>0.043</td><td>0.052</td><td>0.106</td><td>0.124</td><td>0.129</td><td>0.978</td><td>0.497</td><td>0.225</td></tr><tr><td>6</td><td>0.038</td><td>0.041</td><td>0.012</td><td>0.014</td><td>0.157</td><td>0.087</td><td>0.005</td><td>0.358</td></tr><tr><td>7</td><td>0.058</td><td>0.084</td><td>0.174</td><td>0.244</td><td>3.055</td><td>3.071</td><td>2.059</td><td>1.868</td></tr><tr><td>8</td><td>0.026</td><td>0.029</td><td>0.029</td><td>0.033</td><td>0.202</td><td>0.146</td><td>0.203</td><td>0.044</td></tr><tr><td>9</td><td>0.004</td><td>0.006</td><td>0.029</td><td>0.030</td><td>0.115</td><td>0.357</td><td>0.077</td><td>0.054</td></tr><tr><td>10</td><td>0.048</td><td>0.084</td><td>0.064</td><td>0.071</td><td>0.220</td><td>0.577</td><td>0.312</td><td>0.322</td></tr><tr><td>Ave.</td><td>0.047</td><td>0.066</td><td>0.116</td><td>0.139</td><td>0.951</td><td>1.264</td><td>0.859</td><td>1.262</td></tr><tr><td>Testing</td><td colspan="2"> $R^21 < R^22$ </td><td colspan="2"> $R^21 < R^22$ </td><td colspan="4">intra_pIn+ intra_nIn &lt; inter_apIn + inter_anIn</td></tr><tr><td>F-test</td><td colspan="2">9.59***</td><td colspan="2">5.90***</td><td colspan="4">8.03***</td></tr></table>




<table><tr><td rowspan="2">行业</td><td colspan="2">回报</td><td colspan="2">风险</td><td colspan="4">回报方差分解</td></tr><tr><td> $R^21$ </td><td> $R^22$ </td><td> $R^21$ </td><td>$R^22$ </td><td>intra_pIn</td><td>inter_apIn</td><td>intra_nIn</td><td>inter_anIn</td></tr><tr><td>1</td ><td>0.021</td><td>0.024</td><td>0.043</td><td>0.045</td><td>0.050</td><td>0.119</td><td>0.135</t d><td>0.371</td></tr><tr><td>2</td><td>0.068</td><td>0.095</td><td>0.153</td><td>0.177</td><td>1。 448</td><td>4.002</td><td>1.875</td><td>2.597</td></tr><tr><td>3</td><td>0.050</td><td>0.072</td> <td>0.247</td><td>0.264</td><td>1.156</td><td>0.673</td><td>0.982</td><td>2.075</td></tr><tr><td> 4</td><td>0.112</td><td>0.176</td><td>0.300</td><td>0.384</td><td>2.977</td><td>2.628</td><td>2.4 41</td><td>4.701</td></tr><tr><td>5</td><td>0.043</td><td>0.052</td><td>0.106</td><td>0.124</td>< td>0.129</td><td>0.978</td><td>0.497</td><td>0.225</td></tr><tr><td>6</td><td>0.038</td><td>0.041 </td><td>0.012</td><td>0.014</td><td>0.157</td><td>0.087</td><td>0.005</td><td>0.358</td></tr><tr ><td>7</td><td>0.058</td><td>0.084</td><td>0.174</td><td>0.244</td><td>3.055</td><td>3.071</td><t d>2.059</td><td>1.868</td></tr><tr><td>8</td><td>0.026</td><td>0.029</td><td>0.029</td><td>0.033< /td><td>0.202</td><td>0.146</td><td>0.203</td><td>0.044</td></tr><tr><td>9</td><td>0.004</td><td> 0.006</td><td>0.029</td><td>0.030</td><td>0.115</td><td>0.357</td><td>0.077</td><td>0.054</td></t r><tr><td>10</td><td>0.048</td><td>0.084</td><td>0.064</td><td>0.071</td><td>0.220</td><td>0.577< /td><td>0.312</td><td>0.322</td></tr><tr><td>平均</td><td>0.047</td><td>0.066</td><td>0.116</td>< td>0.139</td><td>0.951</td><td>1.264</td><td>0.859</td><td>1.262</td></tr><tr><td>测试</td><td colspan="2"> $R^21 < R^22$ </td><td colspan="2"> $R^21 < R^22$ </td><td colspan="4">intra_pIn+ intra_nIn < inter_apIn + inter_anIn</td></tr><tr><td>F 测试</td><td colspan="2">9.59***</td><td colspan="2">5.90***</td><td colspan="4">8.03***</td></tr></table>


Table 13  
Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * } p < 0 . 0 1 .$




表13  
注：回报系数为百分比值。 $^ { * } p < 0 。 1 , ^ { * * } p < 0 。 0 5 , ^ { * * * } p < 0 。 0 1 .$


<table><tr><td colspan="4">Variance Decomposition of Risk</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>0.580</td><td>0.733</td><td>0.074</td><td>0.142</td></tr><tr><td>1.667</td><td>4.462</td><td>1.278</td><td>1.371</td></tr><tr><td>1.471</td><td>2.649</td><td>0.950</td><td>1.915</td></tr><tr><td>4.585</td><td>4.144</td><td>5.850</td><td>4.450</td></tr><tr><td>0.936</td><td>0.624</td><td>1.094</td><td>1.276</td></tr><tr><td>0.088</td><td>0.340</td><td>0.156</td><td>0.112</td></tr><tr><td>14.136</td><td>20.947</td><td>6.994</td><td>10.271</td></tr><tr><td>0.787</td><td>0.241</td><td>0.092</td><td>0.033</td></tr><tr><td>1.381</td><td>1.322</td><td>0.031</td><td>0.022</td></tr><tr><td>0.103</td><td>0.487</td><td>0.044</td><td>0.125</td></tr><tr><td>2.573</td><td>3.595</td><td>1.656</td><td>1.972</td></tr><tr><td colspan="4">intra_pln + intra_nln &lt; inter_apln + inter_anln 2.87*</td></tr></table>




<table><tr><td colspan="4">方差分解风险</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr>< td>0.580</td><td>0.733</td><td>0.074</td><td>0.142</td></tr><tr><td>1.667</td><td>4.462</td><td>1.278</td> td><td>1.371</td></tr><tr><td>1.471</td><td>2.649</td><td>0.950</td><td>1.915</td></tr><tr><td>4.585</t d><td>4.144</td><td>5.850</td><td>4.450</td></tr><tr><td>0.936</td><td>0.624</td><td>1.094</td><td>1.27 6</td></tr><tr><td>0.088</td><td>0.340</td><td>0.156</td><td>0.112</td></tr><tr><td>14.136</td><td>20。 947</td><td>6.994</td><td>10.271</td></tr><tr><td>0.787</td><td>0.241</td><td>0.092</td><td>0.033</td>< /tr><tr><td>1.381</td><td>1.322</td><td>0.031</td><td>0.022</td></tr><tr><td>0.103</td><td>0.487</td><t d>0.044</td><td>0.125</td></tr><tr><td>2.573</td><td>3.595</td><td>1.656</td><td>1.972</td></tr><tr><td colspan =“4”>intra_pln + intra_nln < inter_apln + inter_anln 2.87*</td></tr></table>


Please cite this article in press as: K. Chen, et al., The dynamic predictive power of company comparative networks for stock sector performance, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.07.005




请在媒体上引用这篇文章：K. Chen 等人，公司比较网络对股票行业表现的动态预测能力，Inf。管理。 （2016），http://dx.doi.org/10.1016/j.im.2016.07.005


Table 14  
Duration of the short- and long-term impacts on return.




表14  
对回报的短期和长期影响的持续时间。


<table><tr><td rowspan="2">Sector</td><td colspan="4">Wear-in</td><td rowspan="2">______intra_pln</td><td colspan="4">Wear-out</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>1</td><td>2</td><td>1</td><td>1</td><td>2</td><td>4</td><td></td><td>3</td><td>4</td><td>5</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>8</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>3</td><td>2</td><td>2</td><td>7</td><td></td><td>6</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td></td><td>5</td><td>5</td><td>5</td></tr><tr><td>5</td><td>1</td><td>3</td><td>1</td><td>2</td><td>7</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>6</td><td>2</td><td>1</td><td>1</td><td>2</td><td>5</td><td></td><td>5</td><td>6</td><td>5</td></tr><tr><td>7</td><td>3</td><td>4</td><td>1</td><td>2</td><td>7</td><td></td><td>8</td><td>9</td><td>9</td></tr><tr><td>8</td><td>1</td><td>3</td><td>3</td><td>1</td><td>6</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>9</td><td>1</td><td>1</td><td>1</td><td>1</td><td>5</td><td></td><td>6</td><td>6</td><td>7</td></tr><tr><td>10</td><td>3</td><td>4</td><td>1</td><td>4</td><td>6</td><td></td><td>7</td><td>7</td><td>9</td></tr><tr><td>Average</td><td>1.8</td><td>2.2</td><td>1.3</td><td>1.8</td><td>5.9</td><td></td><td>6.4</td><td>6.9</td><td>7.5</td></tr><tr><td>Test</td><td colspan="4">Intra_pln + inter_apln&gt;Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln&lt; Intra_nln + inter_anln</td></tr><tr><td>F-test</td><td colspan="4">4.31**</td><td colspan="5">57.45***</td></tr></table>




<table><tr><td rowspan="2">扇区</td><td colspan="4">磨损</td><td rowspan="2">______intra_pln</td><td colspan="4">磨损</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td ><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></t r><tr><td>1</td><td>2</td><td>1</td><td>1</td><td>2</td><td>4</td><td></td><td>3</td><td >4</td><td>5</td></tr><tr><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>8</td><t d></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>3</td><td>2</td><t d>2</td><td>7</td><td></td><td>6</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><t d>1</td><td>1</td><td>1</td><td>4</td><td></td><td>5</td><td>5</td><td>5</td></tr><tr><t d>5</td><td>1</td><td>3</td><td>1</td><td>2</td><td>7</td><td></td><td>8</td><td>8</td>< td>9</td></tr><tr><td>6</td><td>2</td><td>1</td><td>1</td><td>2</td><td>5</td><td></td>< td>5</td><td>6</td><td>5</td></tr><tr><td>7</td><td>3</td><td>4</td><td>1</td><td>2</td> <td>7</td><td></td><td>8</td><td>9</td><td>9</td></tr><tr><td>8</td><td>1</td><td>3</td> <td>3</td><td>1</td><td>6</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>9</td> <td>1</td><td>1</td><td>1</td><td>1</td><td>5</td><td></td><td>6</td><td>6</td><td>7</td ></tr><tr><td>10</td><td>3</td><td>4</td><td>1</td><td>4</td><td>6</td><td></td><td>7</t d><td>7</td><td>9</td></tr><tr><td>平均</td><td>1.8</td><td>2.2</td><td>1.3</td><td>1 .8</td><td>5.9</td><td></td><td>6.4</td><td>6.9</td><td>7.5</td></tr><tr><td>测试</td><td colspan="4">Intra_pln + inter_apln>Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln< Intra_nln + inter_anln</td></tr><tr><td>F 测试</td><td colspan="4">4.31**</td><td colspan="5">57.45***</td></tr></table>


Table 15  
Duration of the short- and long-term impacts on risk.




表15  
对风险的短期和长期影响的持续时间。


<table><tr><td rowspan="2">Sector</td><td colspan="4">Wear-in</td><td rowspan="2">intra_pln</td><td colspan="4">Wear-out</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></tr><tr><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>5</td><td></td><td>5</td><td>6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>5</td><td>1</td><td>1</td><td>6</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>5</td><td>3</td><td>2</td><td>7</td><td></td><td>8</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td></td><td>4</td><td>5</td><td>5</td></tr><tr><td>5</td><td>2</td><td>1</td><td>3</td><td>1</td><td>6</td><td></td><td>6</td><td>7</td><td>7</td></tr><tr><td>6</td><td>1</td><td>1</td><td>1</td><td>2</td><td>6</td><td></td><td>5</td><td>7</td><td>7</td></tr><tr><td>7</td><td>3</td><td>3</td><td>1</td><td>1</td><td>8</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>8</td><td>1</td><td>5</td><td>1</td><td>5</td><td>7</td><td></td><td>9</td><td>9</td><td>9</td></tr><tr><td>9</td><td>2</td><td>3</td><td>1</td><td>3</td><td>6</td><td></td><td>6</td><td>7</td><td>7</td></tr><tr><td>10</td><td>1</td><td>3</td><td>3</td><td>2</td><td>7</td><td></td><td>8</td><td>9</td><td>9</td></tr><tr><td>Average</td><td>1.8</td><td>2.9</td><td>1.6</td><td>1.9</td><td>6.2</td><td></td><td>6.7</td><td>7.4</td><td>7.6</td></tr><tr><td>Test</td><td colspan="4">Intra_pln + inter_apln&gt; Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln&lt; Intra_nln + inter_anln</td></tr><tr><td>F-test</td><td colspan="4">3.27**</td><td colspan="5">81.00***</td></tr></table>




<table><tr><td rowspan="2">扇区</td><td colspan="4">磨损</td><td rowspan="2">intra_pln</td><td colspan="4">磨损</td></tr><tr><td>intra_pln</td><td>inter_apln</td><td>intra_nln</td ><td>inter_anln</td><td></td><td>inter_apln</td><td>intra_nln</td><td>inter_anln</td></t r><tr><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>5</td><td></td><td>5</td><td >6</td><td>6</td></tr><tr><td>2</td><td>1</td><td>5</td><td>1</td><td>1</td><td>6</td><t d></td><td>8</td><td>8</td><td>9</td></tr><tr><td>3</td><td>3</td><td>5</td><td>3</td><t d>2</td><td>7</td><td></td><td>8</td><td>8</td><td>8</td></tr><tr><td>4</td><td>1</td><t d>1</td><td>1</td><td>1</td><td>4</td><td></td><td>4</td><td>5</td><td>5</td></tr><tr><t d>5</td><td>2</td><td>1</td><td>3</td><td>1</td><td>6</td><td></td><td>6</td><td>7</td>< td>7</td></tr><tr><td>6</td><td>1</td><td>1</td><td>1</td><td>2</td><td>6</td><td></td>< td>5</td><td>7</td><td>7</td></tr><tr><td>7</td><td>3</td><td>3</td><td>1</td><td>1</td> <td>8</td><td></td><td>8</td><td>8</td><td>9</td></tr><tr><td>8</td><td>1</td><td>5</td> <td>1</td><td>5</td><td>7</td><td></td><td>9</td><td>9</td><td>9</td></tr><tr><td>9</td> <td>2</td><td>3</td><td>1</td><td>3</td><td>6</td><td></td><td>6</td><td>7</td><td>7</td ></tr><tr><td>10</td><td>1</td><td>3</td><td>3</td><td>2</td><td>7</td><td></td><td>8</t d><td>9</td><td>9</td></tr><tr><td>平均</td><td>1.8</td><td>2.9</td><td>1.6</td><td>1 .9</td><td>6.2</td><td></td><td>6.7</td><td>7.4</td><td>7.6</td></tr><tr><td>测试</td><td colspan="4">Intra_pln + inter_apln> Intra_nln + inter_anln</td><td colspan="5">Intra_pln + inter_apln< Intra_nln + inter_anln</td></tr><tr><td>F 测试</td><td colspan="4">3.27**</td><td colspan="5">81.00***</td></tr></table>


metrics: 14.4 days versus 12.3 days for return $( F { = } 5 7 . 4 5 , p { < } 0 . 0 1 )$ and 15 days versus 12.9 days for risk $( F { = } 8 1 . 0 0 , p { < } 0 . 0 1 )$




指标：回报 $( F { = } 5 7 . 4 5 , p { < } 0 . 0 1 )$ 为 14.4 天，而风险为 12.9 天 $( F { = } 1 . 0 0 , p { < } 0 . 0 1 )$


To control outliers and to determine that our results are not driven by one particular sector, we eliminate one sector at a time on a rolling basis and examine the results. The new results remain similar to the original results. Table 16 presents the consistent variance decomposition results for the data excluding sector 1. UNM refers to the undirected network metrics (intra\_uq and inter\_auq), and DNM denotes the directed network metrics (intra\_pq, inter\_apq, intra\_nq, and inter\_anq). IRAM is the intrasector metrics (intra\_uq, intra\_pq, and intra\_nq), and IERM refers to the inter-sector metrics (inter\_auq, inter\_apq, and inter\_anq).




为了控制异常值并确定我们的结果不是由某个特定部门驱动的，我们滚动地一次消除一个部门并检查结果。新结果与原始结果相似。表16给出了排除扇区1的数据的一致方差分解结果。UNM指的是无向网络度量（intra\_uq和inter\_auq），DNM表示有向网络度量（intra\_pq、inter\_apq、intra\_nq和inter\_anq）。 IRAM 是扇区内指标（intra\_uq、intra\_pq 和intra\_nq），IERM 是指扇区间指标（inter\_auq、inter\_apq 和inter\_anq）。


Variance decomposition of return explained by company network metrics.




由公司网络指标解释的回报方差分解。


<table><tr><td rowspan="2">Sector</td><td colspan="4">Variance Decomposition of Return</td><td colspan="4">Variance Decomposition of Risk</td></tr><tr><td>UNM</td><td>DNM</td><td>IRAM</td><td>IERM</td><td>UNM</td><td>DNM</td><td>IRAM</td><td>IERM</td></tr><tr><td>2</td><td>2.28</td><td>6.18</td><td>1.15</td><td>7.31</td><td>0.19</td><td>4.04</td><td>1.33</td><td>2.91</td></tr><tr><td>3</td><td>1.79</td><td>5.81</td><td>3.59</td><td>4.02</td><td>1.80</td><td>7.88</td><td>4.20</td><td>5.48</td></tr><tr><td>4</td><td>0.18</td><td>2.40</td><td>1.56</td><td>1.02</td><td>3.97</td><td>5.26</td><td>4.91</td><td>4.31</td></tr><tr><td>5</td><td>5.90</td><td>9.58</td><td>9.79</td><td>5.70</td><td>1.24</td><td>3.70</td><td>2.91</td><td>2.03</td></tr><tr><td>6</td><td>3.87</td><td>3.77</td><td>2.99</td><td>4.65</td><td>6.66</td><td>6.12</td><td>5.95</td><td>6.83</td></tr><tr><td>7</td><td>1.40</td><td>5.66</td><td>1.66</td><td>5.39</td><td>2.67</td><td>3.62</td><td>2.73</td><td>3.55</td></tr><tr><td>8</td><td>1.72</td><td>4.37</td><td>2.29</td><td>3.80</td><td>3.18</td><td>2.27</td><td>1.19</td><td>4.26</td></tr><tr><td>9</td><td>0.94</td><td>3.09</td><td>0.99</td><td>3.04</td><td>2.37</td><td>4.27</td><td>3.05</td><td>3.59</td></tr><tr><td>10</td><td>11.03</td><td>15.44</td><td>7.24</td><td>19.22</td><td>7.61</td><td>16.32</td><td>7.67</td><td>16.26</td></tr><tr><td>Average</td><td>3.23</td><td>6.26</td><td>3.47</td><td>6.02</td><td>3.30</td><td>5.94</td><td>3.77</td><td>5.47</td></tr><tr><td>Test</td><td colspan="2">UNM &lt; DNM</td><td colspan="2">IRAM &lt; IERM</td><td colspan="2">UNM &lt; DNM</td><td colspan="2">IRAM &lt; IERM</td></tr><tr><td>F-test</td><td colspan="2">38.77***</td><td colspan="2">2.82*</td><td colspan="2">6.44***</td><td colspan="2">3.20*</td></tr></table>




<table><tr><td rowspan="2">行业</td><td colspan="4">收益的方差分解</td><td colspan="4">收益的方差分解风险</td></tr><tr><td>UNM</td><td>DNM</td><td>IRAM</td><td>IERM</td><td>UNM</td><td>DN M</td><td>IRAM</td><td>IERM</td></tr><tr><td>2</td><td>2.28</td><td>6.18</td><td>1.15</td> td><td>7.31</td><td>0.19</td><td>4.04</td><td>1.33</td><td>2.91</td></tr><tr><td>3</td ><td>1.79</td><td>5.81</td><td>3.59</td><td>4.02</td><td>1.80</td><td>7.88</td><td>4.20 </td><td>5.48</td></tr><tr><td>4</td><td>0.18</td><td>2.40</td><td>1.56</td><td>1.02</td> td><td>3.97</td><td>5.26</td><td>4.91</td><td>4.31</td></tr><tr><td>5</td><td>5.90</td> <td>9.58</td><td>9.79</td><td>5.70</td><td>1.24</td><td>3.70</td><td>2.91</td><td>2.03 </td></tr><tr><td>6</td><td>3.87</td><td>3.77</td><td>2.99</td><td>4.65</td><td>6.66</t d><td>6.12</td><td>5.95</td><td>6.83</td></tr><tr><td>7</td><td>1.40</td><td>5.66</td> <td>1.66</td><td>5.39</td><td>2.67</td><td>3.62</td><td>2.73</td><td>3.55</td></tr><tr> <td>8</td><td>1.72</td><td>4.37</td><td>2.29</td><td>3.80</td><td>3.18</td><td>2.27</t d><td>1.19</td><td>4.26</td></tr><tr><td>9</td><td>0.94</td><td>3.09</td><td>0.99</td>< td>3.04</td><td>2.37</td><td>4.27</td><td>3.05</td><td>3.59</td></tr><tr><td>10</td><t d>11.03</td><td>15.44</td><td>7.24</td><td>19.22</td><td>7.61</td><td>16.32</td><td>7.6 7</td><td>16.26</td></tr><tr><td>平均</td><td>3.23</td><td>6.26</td><td>3.47</td><td >6.02</td><td>3.30</td><td>5.94</td><td>3.77</td><td>5.47</td></tr><tr><td>测试</td><td colspan="2">UNM < DNM</td><td colspan="2">IRAM < IERM</td><td colspan="2">UNM < DNM</td><td colspan="2">IRAM < IERM</td></tr><tr><td>F 测试</td><td colspan="2">38.77***</td><td colspan="2">2.82*</td><td colspan="2">6.44***</td><td colspan="2">3.20*</td></tr></table>


Notes: The coef<sup>fi</sup>cients of return are percentage values. $^ { * } p < 0 . 1 , ^ { * * } p < 0 . 0 5 , ^ { * * * }$ p < 0.01.




注：回报系数为百分比值。 $^ { * } p < 0 。 1 , ^ { * * } p < 0 。 0 5 , ^ { * * * }$ p < 0.01。


## 6. Discussion and conclusions




## 6.讨论与结论


This study aims to construct an effective company relationship network using big data and to investigate the dynamic relationships between sector interactions and stock sector performance. The results suggest that company networks constructed based on public news provide predictive indicators for sector performance and that inter-sector interaction has a stronger predictive power than intra-sector interaction. Moreover, in the network construction, comparative analysis provides a better method than closeness analysis. The negative interactions have a shorter reaction time than the positive interactions for return, and they have longer effects for both sector return and risk. These <sup>fi</sup>ndings are also con<sup>fi</sup>rmed using the links as alternative metrics to re<sup>fl</sup>ect the interactions between sectors. Collectively, these <sup>fi</sup>ndings provide important implications for research regarding market structure and stock sector performance.




本研究旨在利用大数据构建有效的公司关系网络，并研究行业互动与股票行业绩效之间的动态关系。结果表明，基于公共新闻构建的公司网络为行业绩效提供了预测指标，并且行业间互动比行业内互动具有更强的预测能力。而且，在网络构建中，比较分析提供了比紧密度分析更好的方法。负面交互作用比正面交互作用对回报的反应时间更短，并且对行业回报和风险的影响更长。这些<sup>发现</sup>也通过使用链接作为替代指标来<sup>确认</sup>来反映部门之间的相互作用。总的来说，这些<sup>发现</sup>为市场结构和股票行业表现的研究提供了重要的启示。


## 6.1. Theoretical implications




## 6.1.理论意义


This study contributes to the IS and <sup>fi</sup>nance literature in several aspects. First, the network analysis method has been widely used in IS, focusing on the relationships among social entities, and it is an important addition to standard social and behavioral research. For example, the network effects and personal in<sup>fl</sup>uences relevant to product sales have been investigated [49,50]. Social communication and mood in<sup>fl</sup>uences have been used to study information effects on stock prices [4,51]. In contrast to these studies of social in<sup>fl</sup>uence, the present study focuses on the structure of company comparative networks and demonstrates how sector interactions have a predictive relationship with stock sector performance. The constructed company network is quite different from previous social networks. It describes the relationships between objective entities. The links between nodes are built based on a machinelearning algorithm instead of using observations. The network construction and analysis method inspires social in<sup>fl</sup>uence research from a technical perspective.




这项研究在几个方面对信息系统和金融文献做出了贡献。首先，网络分析方法在信息系统中得到了广泛的应用，重点关注社会实体之间的关系，是标准社会和行为研究的重要补充。例如，与产品销售相关的网络效应和个人影响已被调查[49,50]。社会沟通和情绪影响已被用来研究信息对股票价格的影响[4,51]。与这些社会影响力的研究相反，本研究重点关注公司比较网络的结构，并论证行业互动如何与股票行业绩效产生预测关系。构建的公司网络与以前的社交网络有很大不同。它描述了客观实体之间的关系。节点之间的链接是基于机器学习算法而不是使用观察来构建的。网络构建和分析方法从技术角度启发社会影响力研究。


Second, we present comparative analysis in network construction. In contrast to previous marketing studies that used comparative analysis for sales predictions [15,52], we examine the predictive power of the company comparative network for stock sector performance. Our study <sup>fi</sup>rst unveils the correlations between the positive (negative) sector interactions and sector performance. Although more positive than negative interactions are found, we observe that the negative interactions have more rapid effects on returns and that they have longer impacts on both returns and risk. Thus, this study motivates us to explore sentiment analysis between sector interactions in IS and <sup>fi</sup>nance.




其次，我们对网络建设进行了比较分析。与之前使用比较分析进行销售预测的营销研究相反[15,52]，我们检查了公司比较网络对股票行业表现的预测能力。我们的研究首先揭示了正（负）行业互动与行业绩效之间的相关性。尽管发现的积极互动多于消极互动，但我们观察到，消极互动对回报的影响更快，而且对回报和风险的影响更长。因此，这项研究促使我们探索信息系统和<sup>金融</sup>金融部门互动之间的情绪分析。


Finally, previous <sup>fi</sup>nance studies have demonstrated that the network structure between sectors affects sector performance [1– 3]. We agree with this <sup>fi</sup>nding and extend the breadth of research by introducing sector interaction metrics and time-series models. This study investigates both short-term effects and long-term and cumulative effects. Furthermore, we evaluate the dynamic effects of multiple interaction relationships (inter-, intra-, positive, and negative) with VARX models. Thus, this study provides a comprehensive and dynamic approach for both market structure and <sup>fi</sup>nancial research.




最后，之前的<sup>金融</sup>研究表明，部门之间的网络结构会影响部门绩效[1-3]。我们同意这一<sup>发现</sup>，并通过引入部门交互指标和时间序列模型来扩展研究的广度。这项研究调查了短期影响以及长期和累积影响。此外，我们使用 VARX 模型评估多种交互关系（内部、内部、正向和负向）的动态效应。因此，本研究为市场结构和<sup>财务</sup>研究提供了全面且动态的方法。


## 6.2. Practical implications




## 6.2.实际意义


This study contributes to sector-level strategies. First, both inter- and intra-sector interactions have predictive power for stock sector performance. This <sup>fi</sup>nding suggests that companies should strengthen their ties within an industry. For example, they can establish industry associations and frequently hold domain conferences. Simultaneously, companies should also encourage interactions between sectors, such as cooperation with companies in upstream or downstream industries.




这项研究有助于制定部门层面的战略。首先，行业间和行业内的相互作用对股票行业的表现具有预测能力。这一<sup>发现</sup>表明公司应该加强行业内的联系。例如，他们可以建立行业协会，经常举办领域会议。同时，企业还应该鼓励行业之间的互动，比如与上下游行业的企业合作。


Second, because the constructed company comparative network signi<sup>fi</sup>cantly in<sup>fl</sup>uences sector performance, companies should pay attention to public media information. They should strengthen efforts to promote public propaganda for improving exposure and should also monitor the company interactive dynamics reported by various media outlets. The shortest wearin time can provide an early warning signal to companies regarding future damage to sector performance, particularly when competitive or negative interactions occur. The company network also provides a good visualization method for understanding the market network structure.




其次，由于构建的公司比较网络对行业绩效影响显着，公司应关注公共媒体信息。加大宣传力度，提高曝光度，并关注各媒体报道的公司互动动态。最短的磨损时间可以为公司提供有关行业绩效未来受损的早期预警信号，特别是在发生竞争或负面互动时。公司网络还为了解市场网络结构提供了很好的可视化方法。


Third, the predictive model contributes to portfolio and risk management. Investors can apply the company comparative analysis and sector interactive analysis methods to predict sector returns and risks on a daily basis.




第三，预测模型有助于投资组合和风险管理。投资者可以运用公司比较分析和板块互动分析方法，每日预测板块收益和风险。


## 6.3. Limitations and future research




## 6.3。局限性和未来研究


Nevertheless, this study has several limitations that should be addressed in future research. First, we control for few exogenous variables. In this study, we use only news sentiment to control for market environment. In fact, there are many other factors that can have impact on sector performance. For example, the web search volume concerning a stock could indicate a dynamic “hot spot” in the market. Other likely control variables include sector productivity and pro<sup>fi</sup>ts. Second, we have noted that different sectors exhibit different reactions, potentially due to sector properties.




然而，这项研究有一些局限性，应在未来的研究中解决。首先，我们控制很少的外生变量。在本研究中，我们仅使用新闻情绪来控制市场环境。事实上，还有许多其他因素可能影响行业绩效。例如，有关股票的网络搜索量可能表明市场上的动态“热点”。其他可能的控制变量包括部门生产率和利润。其次，我们注意到不同的行业表现出不同的反应，这可能是由于行业特性所致。


Therefore, analyzing the sector-speci<sup>fi</sup>c results could be an important undertaking. Third, we propose that our results can be applied to portfolio and risk management. We intend to conduct future experiments using real-world data to test the effectiveness of the model for investing.




因此，分析特定行业的结果可能是一项重要的任务。第三，我们建议我们的结果可以应用于投资组合和风险管理。我们打算使用真实世界的数据进行未来的实验，以测试投资模型的有效性。


## Acknowledgement




## 致谢


This paper was supported by the Shenzhen Fundamental Research Grant (No.: JCYJ2010417105742712).




该论文得到深圳市基础研究基金资助（编号：JCYJ2010417105742712）。


## References




＃＃ 参考


[1] D. Acemoglu, et al., The network origins of aggregate <sup>fl</sup>uctuations, Econometrica 80 (5) (2012) 1977–2016.




[1] D. Acemoglu 等人，聚合<sup>波动</sup>的网络起源，Econometrica 80 (5) (2012) 1977-2016。


[2] K.R. Ahern, J. Harford, The importance of industry links in merger waves, J. Finance 69 (2) (2014) 527–576.




[2] K.R. Ahern, J. Harford，并购浪潮中行业联系的重要性，J. Finance 69 (2) (2014) 527–576。


[3] D. Aobdia, J. Caskey, N.B. Ozel, Inter-industry network structure and the crosspredictability of earnings and stock returns, Rev. Account. Stud. 19 (3) (2013) 1191–1224.




[3] D. Aobdia, J. Caskey, N.B. Ozel，行业间网络结构以及收益和股票回报的交叉预测性，Rev. Account。螺柱。 19（3）（2013）1191-1224。


[4] B. Han, L. Yang, Social networks, information acquisition, and asset prices Manage. Sci. 59 (6) (2013) 1444–1457.




[4] 韩斌，杨丽，社交网络、信息获取与资产价格管理。科学。 59（6）（2013）1444-1457。


[5] Y. Jin, et al., Mining dynamic social networks from public news articles for company value prediction, Soc. Netw. Anal. Min. 2 (3) (2012) 217–228.




[5] Y. Jin 等人，从公共新闻文章中挖掘动态社交网络以进行公司价值预测，Soc。网络。肛门。分钟。 2（3）（2012）217-228。


[6] Z. Ma, O.R. Sheng, G. Pant, Discovering company revenue relations from news: a network approach, Decis. Support Syst. 47 (4) (2009) 408–414.




[6] Z. Ma，O.R.盛，G.潘特，从新闻中发现公司收入关系：网络方法，Decis。支持系统。 47（4）（2009）408-414。


[7] Z.P. Ma, Gautam Sheng, R.L. Olivia, Mining competitor relationships from online news: a network-based appraoch, Electr. Comm. Res. Appl. 10 (2011) 418–427.




[7] Z.P. Ma、Gautam Shen、R.L. Olivia，从在线新闻中挖掘竞争对手关系：基于网络的方法，Electr。通讯。资源。应用。 10（2011）418-427。


[8] Z.G. Zhang, Chenhui Guo, Paulo Goes, Product comparison networks for competitive analysis of online word-of-mouth, ACM Trans. Manage. Inform. Syst. (TMIS) 3 (4) (2013) 20:1–20:22.




[8] Z.G.张，郭晨辉，Paulo Goes，在线口碑竞争分析的产品比较网络，ACM Trans。管理。通知。系统。 （TMIS）3（4）（2013）20：1–20：22。


[9] G.G. Creamer, Y. Ren, J.V. Nickerson, Impact of dynamic corporate news networks on asset return and volatility, Social Computing (SocialCom), 2013 International Conference On. 2013. IEEE (2016).




[9] G.G. Creamer, Y. Ren, J.V. Nickerson，动态企业新闻网络对资产回报和波动性的影响，社会计算 (SocialCom)，2013 年国际会议。 2013。IEEE（2016）。


[10] B. Handjiski, Enhancing Regional Trade Integration in Southeast Europe, World Bank Publications, 2010.




[10] B. Handjiski，《加强东南欧区域贸易一体化》，世界银行出版物，2010 年。


[11] R.J. Ruf<sup>fi</sup>n, The Nature and Signi<sup>fi</sup>cance of Intra-industry Trade, 4, Economic and <sup>fi</sup>nancial review-federal reserve Bank of Dallas, 1999, pp. 2–16.




[11] R.J. Ruf<sup>fi</sup>n，产业内贸易的本质和意义，4，经济和<sup>金融</sup>金融审查——达拉斯联邦储备银行，1999 年，第 2-16 页。


[12] T.J. Moskowitz, G. Mark, Do industries explain momentum? J. Finance 54 (4) (1999) 1249–1290.




[12] T.J. Moskowitz，G. Mark，工业可以解释动力吗？ J. 金融 54 (4) (1999) 1249–1290。


[13] C.S. Asness, R.B. Porter, R.L. Stevens, Predicting stock returns using industryrelative firm characteristics. Available at SSRN 213872. (2000).




[13] C.S. Asness、R.B. Porter、R.L. Stevens，利用行业相关公司特征预测股票回报。参见 SSRN 213872. (2000)。


[14] Y. Chen, Q. Wang, J. Xie, Online social interations: a natural experiment on word of mouth versus observational learning, J. Market. Res. 48 (2) (2011) 238– 254.




[14] Y. Chen，Q. Wang，J. Xie，在线社交互动：口碑与观察学习的自然实验，J. Market。资源。 48（2）（2011）238-254。


[15] Z. Zhang, X. Li, Y. Chen, Deciphering word-of-mouth in social media: textbased metrics of consumer reviews, ACM Trans. Manage. Inform. Syst. (TMIS) 3 (1) (2012) 5.




[15] Z. 张，X. Li，Y. Chen，解读社交媒体中的口碑：基于文本的消费者评论指标，ACM Trans。管理。通知。系统。 （TMIS）3（1）（2012）5。


[16] W. He, et al., A novel social media competitive analytics framework with sentiment benchmarks, Inform. Manage. 52 (7) (2015) 801–812.




[16] W. He 等人，一种带有情绪基准的新型社交媒体竞争分析框架，Inform。管理。 52（7）（2015）801-812。


[17] N. Jindal, B. Liu, Identifying comparative sentences in text documents, Proceedings of the 29th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM, 2006.




[17] N. Jindal、B. Liu，识别文本文档中的比较句子，第 29 届国际 ACM SIGIR 信息检索研究与发展年度会议论文集，ACM，2006 年。


[18] N. Jindal, B. Liu, Mining comparative sentences and relations, AAAI (2006).




[18] N. Jindal，B. Liu，挖掘比较句子和关系，AAAI (2006)。


[19] K. Xu, et al., Mining comparative opinions from customer reviews for Competitive Intelligence, Decis. Support Syst. 50 (4) (2011) 743–754.




[19] K. Xu 等人，从竞争情报的客户评论中挖掘比较意见，Decis。支持系统。 50（4）（2011）743-754。


[20] J.R. Anderson, G.H. Bower, Human Associative Memory, Psychology press, 1973.




[20] J.R.安德森，G.H. Bower，《人类联想记忆》，心理学出版社，1973 年。


[21] Q. He, Knowledge discovery through Co-Word analysis, Library Trends 48 (1) (1999) 133–159.




[21] Q. He，通过共词分析发现知识，图书馆趋势 48 (1) (1999) 133–159。


[22] S. Goel, H.A. Shawky, Estimating the market impact of security breach announcements on <sup>fi</sup>rm values, Inform. Manage. 46 (7) (2009) 404–410.




[22] S.戈埃尔，H.A. Shawky，估计安全漏洞公告对公司价值的市场影响，Inform。管理。 46（7）（2009）404-410。


[23] X. Li, et al., News impact on stock price return via sentiment analysis Knowledge-Based Syst. 69 (2014) 14–23.




[23] X. Li等人，基于情绪分析知识系统的新闻对股价回报的影响。 69（2014）14-23。


[24] Y. Yu, W. Duan, Q. Cao, The impact of social and conventional media on <sup>fi</sup>rm equity value: a sentiment analysis approach, Decis. Support Syst. 55 (4) (2013) 919-926




[24] Y. Yu，W. Duan，Q. Cao，社交媒体和传统媒体对企业股权价值的影响：情感分析方法，Decis。支持系统。 55（4）（2013）919-926


[25] P.C. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: quantifying language to measure firms' fundamentals L. Finance 63 (3) (2008) 1437–1467




[25] 电脑Tetlock, M. Saar-Tsechansky, S. Macskassy，不仅仅是语言：量化语言来衡量公司的基本面 L. Finance 63 (3) (2008) 1437–1467


[26] W.S. Chan, Stock price reaction to news and no-news: drift and reversal after headlines, J. Financial Econ. 70 (2) (2003) 223–260.




[26] W.S.陈，股票价格对新闻和非新闻的反应：头条新闻后的漂移和逆转，J. Financial Econ。 70 (2) (2003) 223–260。


[27] P.N. Van, A Good News or Bad News Has Greater Impact on the Vietnamese Stock Market? Banking Academy of Vietnam State Bank of Vietnam. 2015




[27] P.N.范，好消息还是坏消息对越南股市影响更大？越南国家银行越南银行学院。 2015年


[28] X. Luo, J. Zhang, W. Duan, Social media and <sup>fi</sup>rm equity value, Inform. Syst. Res. 24 (1) (2013) 146–163.




[28] 罗旭，张建，段伟，社交媒体与企业股权价值，Inform。系统。资源。 24（1）（2013）146-163。


[29] S. Tirunillai, G. Tellis, Does chatter matter? The impact of online consumer generated content on a <sup>fi</sup>rm’s <sup>fi</sup>nancial performance, Market. Sci. 31 (2) (2012) 198–215.




[29] S. Tirunillai、G. Tellis，闲聊重要吗？在线消费者生成的内容对<sup>公司</sup>公司的<sup>财务</sup>财务绩效的影响，市场。科学。 31（2）（2012）198-215。


[30] H. Hong, J.C. Stein, A uni<sup>fi</sup>ed theory of underreaction, momentum trading, and overreaction in asset markets. L. Finance 54 (1999) 2143–2184.




[30] H. Hong，J.C. Stein，资产市场反应不足、动量交易和过度反应的统一理论。 L. 金融 54 (1999) 2143–2184。


[31] H. Hong, T. Lim, J.C. Stein, Bad news travels slowly: size, analyst coverage, and the pro<sup>fi</sup>tability of momentum strategies, J. Finance 55 (1) (2000) 265–295.




[31] H. Hong、T. Lim、J.C. Stein，坏消息传播缓慢：规模、分析师覆盖率和动量策略的盈利能力，J. Finance 55 (1) (2000) 265–295。


[32] E. Fama, Ef<sup>fi</sup>cient capital markets: a review of theory and empirical work, J. Finance 25 (2) (1970) 383–417




[32] E. Fama，有效资本市场：理论和实证工作回顾，J. Finance 25 (2) (1970) 383–417


[33] A. Singhal, Modern information retrieval: a brief overview, Bull. IEEE Comput. Soc. Tech. Comm. Data Eng. 24 (4) (2001) 35–43.




[33] A. Singhal，现代信息检索：简要概述，Bull。 IEEE 计算。苏克。技术。通讯。数据工程24（4）（2001）35-43。


[34] K. Dejaeger, T. Verbraken, B. Baesens, Towards comprehensible software fault prediction models using Bayesian network classi<sup>fi</sup>ers, IEEE Trans. Software Eng. 39 (2) (2013) 237–257.




[34] K. Dejaeger、T. Verbraken、B. Baesens，使用贝叶斯网络分类器实现可理解的软件故障预测模型，IEEE Trans。软件工程。 39（2）（2013）237-257。


[35] X. Luo, J. Zhang, How do consumer buzz and traf<sup>fi</sup>c in social media marketing predict the value of the <sup>fi</sup>rm? J. Manage. Inform. Syst. 30 (2) (2013) 213–238.




[35] X. Luo，J. Zhang，社交媒体营销中的消费者热度和流量如何预测公司的价值？ J. 管理。通知。系统。 30（2）（2013）213-238。


[36] M.E. Newman, M. Girvan, Finding and evaluating community structure in networks, Phys. Rev. E 69 (2) (2004) (026113).




[36] M.E. Newman，M. Girvan，寻找和评估网络中的社区结构，物理学。修订版 E 69 (2) (2004) (026113)。


[37] Z. Bu, et al., A fast parallel modularity optimization algorithm (FPMQA) for community detection in online social network, Knowledge-Based Syst. 50 (2013) 246–259.




[37] Z. Bu 等人，用于在线社交网络中社区检测的快速并行模块化优化算法（FPMQA），基于知识的系统。 50（2013）246-259。


[38] M.E. Newman, Modularity and community structure in networks, Proc. Natl. Acad. Sci. 103 (23) (2006) 8577–8582.




[38] M.E. Newman，网络中的模块化和社区结构，Proc。国家。阿卡德。科学。 103（23）（2006）8577-8582。


[39] E.A. Leicht, M.E. Newman, Community structure in directed networks, Phys. Rev. Lett. 100 (11) (2008) (118703).




[39] E.A. Leicht，M.E. Newman，定向网络中的社区结构，物理学。莱特牧师。 100（11）（2008）（118703）。


[40] M.E. Newman, Analysis of weighted networks, Phys. Rev. E 70 (5) (2004) 056131.




[40] M.E. Newman，加权网络分析，物理学。修订版 E 70 (5) (2004) 056131。


[41] E. Rubin, A. Rubin, The impact of business intelligence systems on stock return, Inform. Manage. 50 (2–3) (2013) 67–75.




[41] E. Rubin，A. Rubin，商业智能系统对股票回报的影响，Inform。管理。 50（2-3）（2013）67-75。


[42] H.H. Pesaran, Y. Shin, Generalized impulse response analysis in linear multivariate models, Econ. Lett. 58 (1) (1998) 17–29.




[42] H.H. Pesaran，Y. Shin，线性多元模型中的广义脉冲响应分析，经济学。莱特。 58（1）（1998）17-29。


[43] G. Koop, M. Pesaran, S. Potter, Impulse response analysis in nonlinear multivariate models, J. Econom. 74 (1996) 119–147.




[43] G. Koop、M. Pesaran、S. Potter，非线性多元模型中的脉冲响应分析，J. Econom。 74（1996）119-147。


[44] G. Adomavicius, J. Bockstedt, A. Gupta, Modeling supply-side dynamics of IT components, products, and infrastructure: an empirical analysis using vector autoregression, Inform. Syst. Res. 23 (2) (2012) 397–417.




[44] G. Adomavicius、J. Bockstedt、A. Gupta，对 IT 组件、产品和基础设施的供应方动态进行建模：使用向量自回归进行实证分析，Inform。系统。资源。 23（2）（2012）397-417。


[45] M.G. Dekimpe, D.M. Hanssens, Sustained spending and persistent response: a new look at long-term marketing pro<sup>fi</sup>tability, J. Market. Res. 36 (4) (1999) 397–412.




[45] M.G.德金佩，D.M. Hanssens，持续支出和持续响应：对长期营销盈利能力的新看法，J. Market。资源。 36（4）（1999）397-412。


[46] J.D. Hamilton, Time Series Analysis, Princeton University Press, Princeton, NJ, 1994.




[46] J.D. Hamilton，时间序列分析，普林斯顿大学出版社，新泽西州普林斯顿，1994 年。


[47] C. Granger, Investigating causal relations by econometric models and crossspectral methods, Econometrica 37 (3) (1969) 424–438.




[47] C. Granger，通过计量经济学模型和交叉谱方法调查因果关系，计量经济学 37 (3) (1969) 424–438。


[48] S.V. Srinivasan, Koen Marc; Pauwels, Minset metrics in market response models: an integrative approach, J. Market. Res. 47 (3) (2010) 672–684.




[48] S.V.斯里尼瓦桑，科恩·马克； Pauwels，市场响应模型中的 Minset 指标：综合方法，J. Market。资源。 47（3）（2010）672-684。


[49] G.R. Gonzalez, D.P. Claro, R.W. Palmatier, Synergistic effects of relationship managers' social networks on sales performance, J. Market. 78 (1) (2014) 76– 94.




[49] G.R.冈萨雷斯，D.P. Claro, R.W. Palmatier，关系经理社交网络对销售业绩的协同效应，J. Market。 78（1）（2014）76-94。


[50] E. Moretti, Social learning and peer effects in consumption: evidence from movie sales, Rev. Econ. Stud. 78 (1) (2011) 356–393.




[50] E. Moretti，消费中的社会学习和同伴效应：来自电影销售的证据，Rev. Econ。螺柱。 78（1）（2011）356-393。


[51] J. Bollen, H. Mao, X. Zeng, Twitter mood predicts the stock market, J. Comput. Sci. 2 (1) (2011) 1–8.




[51] J. Bollen、H. Mao、X. Zeng，Twitter 情绪预测股市，J. Comput。科学。 2 (1) (2011) 1-8。


[52] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviewers, Manage. Sci. 57 (8) (2011) 1485–1509.




[52] N. Archak、A. Ghose、P.G. Ipeirotis，通过挖掘消费者评论者得出产品功能的定价能力，管理。科学。 57（8）（2011）1485-1509。


Kun Chen is an assistant professor in the Department of Finance at South University of Science and Technology of China. She received her Ph.D. from the Department of Information Systems at the City University of Hong Kong. Dr Chen’s research deals with business intelligence, text mining, and big data analytics. She has published in academic journals such as INFORMS Journal on Computing and Journal of Management Information Systems.




陈坤，南方科技大学金融系助理教授。她获得了博士学位。来自香港城市大学信息系统系。陈博士的研究涉及商业智能、文本挖掘和大数据分析。她曾在《INFORMS Journal on Computers》和《Journal of Management Information Systems》等学术期刊上发表文章。


Peng Luo is a Ph.D. student in Harbin Institute of Technology. His research focuses on network topology and social networks. Mr. Luo has published in academic journals such as Physica A, Journal of Informetrics, and Management Decisions.




罗鹏，博士。哈尔滨工业大学学生。他的研究重点是网络拓扑和社交网络。罗先生曾在Physica A、Journal of Informatics、Management Decisions等学术期刊上发表论文。


Dongming Xu is a senior lecturer in Business of Information Systems at the University of Queensland Business School and has a Ph.D. in the area of information systems from the City University of Hong Kong. Her interests include research knowledge management, eLearning effectiveness, <sup>fi</sup>nancial monitoring management systems, electronic commerce, and intelligent agent business applications. She has published in academic journals such as Information & Management and Decision Support Systems.




徐东明是昆士兰大学商学院信息系统商务高级讲师，拥有博士学位。香港城市大学信息系统专业。她的兴趣包括研究知识管理、电子学习有效性、<sup>财务监控管理系统、电子商务和智能代理业务应用程序。她曾在《信息与管理》和《决策支持系统》等学术期刊上发表文章。


Huaiqing Wang is a professor in the Department of Finance at South University of Science and Technology of China. He is also the Honorary Dean and a Guest Professor of the School of Information Engineering, Wuhan University of Technology, China. He received his Ph.D. from University of Manchester, UK, in 1987. Dr. Wang specializes in research on <sup>fi</sup>nancial intelligence and intelligent systems (such as intelligent <sup>fi</sup>nancial systems, intelligent learning systems, business process management systems, knowledge management systems, conceptual modeling, and ontology). He has published more than 70 international refereed SCI/SSCI journal articles and received more than 700 SCI citations




王怀庆，南方科技大学金融系教授。他也是中国武汉理工大学信息工程学院名誉院长、客座教授。他获得了博士学位。 1987年获英国曼彻斯特大学博士学位。王博士主要研究金融智能和智能系统（如智能金融系统、智能学习系统、业务流程管理系统、知识管理系统、概念建模和本体）。发表国际SCI/SSCI期刊文章70余篇，SCI引用700余次
