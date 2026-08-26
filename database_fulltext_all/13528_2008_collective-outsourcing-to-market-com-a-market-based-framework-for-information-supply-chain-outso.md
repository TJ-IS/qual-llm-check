---
otero_id: 13528
otero_key: "E5DTKBME"
title: "Collective Outsourcing to Market (Com): A Market-Based Framework for Information Supply Chain Outsourcing"
authors: "Andrew Whinston; Fang Fang; Zhiling Guo"
year: "2008"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00157"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 9 Issue 4

Article 11

4-2008

# Collective Outsour cing to Market (Com): A Mark  et-Based Framework for Information Supply Chain Outsourcing

Andrew B. Whinston , abw@uts.sc.utexas.edu

Fang Fang

, fangfang@csusm.edu

Zhiling Guo

, zguo@umbc.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Journal of the Association for Information Systems JAIS

Special Issue

Collective Outsourcing to Market (COM): A Market-Based Framework for Information Supply Chain Outsourcing

Fang Fang College of Business Administration California State University at San Marcos fangfang@csusm.edu

Zhiling Guo Department of Information Systems, University of Maryland, Baltimore County (UMBC) zguo@umbc.edu

Andrew B. Whinston McCombs School of Business The University of Texas at Austin abw@uts.cc.utexas.edu

## Abstract

This paper discusses the importance of and a solution to separating the information flow from the physical product flow in a supply chain. Motivated by the inefficient demand forecast caused by information asymmetry and lack of an incentive among supply chain partners to share valuable information, we propose a radically new framework called collective outsourcing to market (COM) to address many information supply chain design challenges. To validate the COM framework, we consider a supply chain with one manufacturer and multiple downstream retailers. Retailers privately acquire demand forecast information that they do not have incentive to share horizontally with other retailers or vertically with the upstream manufacturer. We consider two alternative market mechanisms that can be used to outsource the information-intensive demand forecasting task for the whole supply chain. The specially organized market can be viewed as a cost effective way of acquiring quality information that, at the same time, aligns individual retailers' incentives to credibly share their private information. We further discuss the real world implementation issues including market design and the costs and benefits of proposed solutions

Keywords: information supply chain, market mechanism, outsourcing, demand forecasting

# Collective Outsourcing to Market (COM): A Market-Based Framework for Information Supply Chain Outsourcing

## 1. Introduction

Unarguably, demand forecasting plays a critical role in supply chain management. Companies now invest aggressively in software and consulting in order to acquire more relevant information and produce better forecasts. However, in current practice, supply chain partners independently manage their forecasting activities and are extremely unwilling to disclose their forecasts to other supply chain partners in order to maintain their own competitive advantages. The overall supply chain does not benefit from individual companies’ information acquisition. Even though researchers have addressed the benefits of information sharing in supply chain management, how to provide the chain partners with the correct incentives to conduct their demand forecasting activities in a more cost-effective way and in a way that benefits the entire supply chain remains a challenging task. This paper proposes a general framework to induce collective information acquisition and demand forecast sharing using market mechanisms. We suggest that outsourcing the forecasting activity to a dedicated market can improve efficiency and willingness to share, and we call this novel framework collective outsourcing to market (COM).

In a supply chain, the uncertain market demands of individual firms are usually driven by some macro-level, industry-related or economy-related environmental factors. Individually managed demand forecasts cause supply chain inefficiency in three ways. First, supply chain partners invest repeatedly in acquiring highly correlated demand information, which increases the overall cost of demand forecasting. Second, the quality of individual forecasts is generally sub-optimal, since individual companies have only limited access to information sources and limited ability to process them, which results in less accurate forecasts and inefficient decision making. Third, but not least, firms vary in their capability to produce good quality forecasts. Significant information asymmetry leads to strategic plays and has been reported to be the main reason for many coordination failures, such as the well-known “bullwhip” effect (Lee et al., 1997).

In this paper, we propose an innovative way to reorganize the demand forecasting process so as to benefit the whole supply chain. Our proposed COM solution consists of two key elements. First, we propose that companies collectively outsource the process of demand forecasting, especially the correlated part of the demand, to a specialized independent third party. The third party can undertake the task, manage the budget and consulting resources for the companies, and integrate available pieces of information into an overall accurate forecast. Second, we propose that the information third party adopt market mechanisms to create incentive-aligned information sharing among the supply chain partners, provide trust inside the supply chain, and aggregate dispersed information from various information sources.

The idea of adopting outsourcing to induce efficiency is not new in supply chain practice. In a technological environment characterized by rapid innovation, original equipment manufacturers (OEMs) outsource asset-intensive production to contract manufacturers who cut OEMs’ costs, free up capital, and improve productivity. Another innovative business process outsourcing (BPO) application is Vendor Managed Inventory (VMI), wherein vendors (the external service providers) who specialize in specific functional areas perform those functions for a company more efficiently at lower cost. Likewise, the concept of BPO in supply chain management would shift information intensive processes to external service providers, with the intention of improving decision making in firms with limited information processing capabilities (Mani et al., 2006). Our proposed COM framework builds on this trend and suggests that outsourcing can collectively improve information quality in the information sharing process and facilitate supply chain coordination. In our COM framework, supply chain efficiency can be achieved both by economies of scale and by tapping the expertise and investments of a service provider who focuses solely on that process. In addition, the collective outsourcing framework requires firms to commit to information sharing via the market reward mechanism, which is a challenging task when the demand forecast is produced in-house.

As to the mechanism that can be used to manage market-type relationships and encourage cooperation and efficiency in the process of supply chain information outsourcing, the prediction market is one viable concept. Cowles (1933) concluded that expert forecasters could not improve the accuracy of forecasts derived from the actions of a market, and other research findings have generally supported this conclusion. In addition, some recent applications have validated the role of markets in effective information aggregation, including innovations in financial markets, betting on sporting events, and prediction markets.

Particularly, a prediction market is an emerging market type that is designed with the sole purpose of forecasting future events. Prediction markets trade specially designed contingent contracts whose payoff depends on the outcomes of certain future events. These markets are usually set up as online futures markets and have trading processes that essentially resemble those of existing stock exchanges such as continuous time double auctions. Traders buy or sell contingent contracts based on their private predictions of the future value of the contracts (i.e., the outcome of future events). The market price of the contingent contracts fluctuates according to the traders’ activities and integrates all the traders’ predictions into an aggregate forecast. Prototypes of such markets were used in predicting the most recent presidential election outcome (the Iowa Electronic Market, http://www.biz.uiowa.edu/iem) and forecasting movie sales (Hollywood Stock Exchange Market, http://www.hsx.com). (Please refer to Wolfers and Zitzewitz (2004) for a comprehensive review of prediction markets.) Hewlett-Packard has already pioneered business applications in sales forecasting and now uses internal prediction markets in several business units (Foroohar, 2003). A handful of large companies, such as IBM, Microsoft, and Ford, are eager to join market experiments that utilize their predictive power. The impact of prediction markets on science and business is becoming more and more evident.

In addition to the double auction mechanisms mentioned above, some researchers have suggested other types of prediction markets where contingent contracts are explicitly priced before the market opens. The price takes into account the fact that the traders need to incur costs to acquire good information, and the market rewards the traders if the information is, in fact, of good quality. Chen et al. (2001, 2004) have used logarithmic reward functions to show that the market (combined with other design features) can integrate information when traders are risk-averse or when traders’ information has some correlation. Fang et al. (2007) have suggested a special family of quadratic reward functions that can reveal not only the traders’ private forecasts but their beliefs on forecast accuracy. Such a market mechanism can be adopted when traders have heterogeneous abilities and nonnegligible costs to acquire and process information.

Although different market reward structures can be constructed to achieve the specific information acquisition and aggregation objectives, choosing the underlying market instrument is a nontrivial task. Guo et al. (2006) have suggested the use of a futures contract written on a macro-level index that will affect the demand of all the retailers in a supply chain setting. The innovative idea of creating a macro-level index for the supply chain demand forecasting purpose has far extended the scope of current prediction market applications. This paper extends Guo et al. (2006) to a collective outsourcing framework and carefully studies the role of the information third party in designing, managing, and implementing proper market solutions. This paper also examines the conditions under which firms can use pre-priced betting markets to produce reliable and accurate predictions in different business environments. More specifically, we discuss an alternative market design demonstrated in Fang et al. (2007) to address different information elicitation and aggregation challenges under different informational assumptions.

Our major contribution can be briefly summarized as a new supply chain outsourcing initiative enabled by an innovative market-based information revelation and aggregation mechanism. We specifically focus on one important challenge in the information supply chain design – the demand forecasting process – that is traditionally conducted in-house and is viewed as private knowledge and a source of competitive advantage. Our market design provides supply chain partners with an attractive venue to implicitly outsource their demand forecasting functions. The COM framework is viewed as a cost effective way to collectively outsource such an information-intensive task and achieve consensus among supply chain partners in truthful and effective information sharing.

The rest of the paper is organized as follows. Section 2 reviews related literature. Section 3 outlines our COM framework. We first illustrate the market mechanism design and demonstrate the value of collective outsourcing in the information supply chain using a framework adopted by Guo et al. (2006). We then extend our model to a different information scenario using an alternative betting market design proposed by Fang et al. (2007). In Section 4, we compare the two market designs and discuss the market implementation issues. We conclude our paper in Section 5.

## 2. Related Literature

Extensive work in the supply chain literature has addressed the problem of asymmetric information and the importance of information sharing. For example, the well-known bullwhip effect (Lee et al., 1997) refers to the information distortion in the supply chain due to separate ownership of information. It has been viewed as a major source of inefficiency in forecast-driven distribution channels, and information sharing has been widely recognized as a solution to alleviate the bullwhip effect (Chen et al. 2000). Cachon and Fisher (2000) showed that full information sharing lowers supply chain total cost by 2.2 percent, on average. Since demand forecasting is a significant part of the information sharing process, Aviv (2001) explored the benefit of sharing forecasts of future demand. Li (2002) showed that the information leakage concern discourages retailers from sharing their demand information with manufacturers. Therefore, how to implement truthful information sharing, and in particular, demand forecast sharing, remains a challenge.

The existing supply chain literature has explored various design possibilities for complicated contracts among chain partners hoping that self-interested retailers will see that it is in their best interests to release their private information. Whang and Zou (2003) proposed to use spot market trading of commodities as an opportunity to share information about demand uncertainty and readjust inventory positions. Shin and Tunca (2006) studied a variety of contract forms and concluded that some traditional contracts, such as wholesale price contracts, quadratic contracts, and two-part tariffs, lead retailers to over-invest in their demand forecasts when they are competing for market demand in a Cournot fashion. As an incentive-compatible solution, they proposed a so-called “market-based” contracting, where each retailer’s price depends not only on her own order quantity but also on the order quantities submitted by other retailers. Their proposed solution resembles a VCG (Vickrey, 1961; Clarke, 1971; and Groves, 1973) type payment rule that ties the price one pays to the total demand for the product (Bergemann and Välimäki, 2002). Each retailer needs to “conjecture correctly” others’ orders to decide her optimal quantities. This assumption is too demanding, if not entirely unrealistic, in real contract design and implementation.

There are three potential problems with the “contracting” solution. First, the existence of an incentivecompatible contract is sensitive to how the information is distributed among the retailers. In fact, all of the papers above assume that retailers are homogeneous in both their ability to acquire information and their ex-ante demand distribution. It is not clear whether their results can be generalized to heterogeneous retailers. Second, in order to achieve truthful information sharing, the manufacturer has to write and enforce individual specific contracts contingent on the orders from all participating retailers, which unarguably complicates the contract management issue. Since the informationrevealing equilibrium requires a large number of participants, the contracting cost will be prohibitive. Third, the solution attempts to manage the information flow along with the physical product orders. It generally focuses on collecting information from supply chain partners and ignores the fact that there are outside sources that may provide better information in a more cost-effective way. Since the traditional supply chain is managed in a closed-loop community, the “contracting” solution lacks the flexibility to acquire and aggregate all the available information relevant for decision making.

In contrast, our approach emphasizes the importance of an independent information management scheme in the supply chain. We introduce an independent third party that manages a prediction market to trade a macroeconomic index whose future payoff depends on the realization of a macro factor correlated with the supply chain demand forecast goal. The idea of trading a macro index is consistent with observations that a firm’s demand has a strong correlation with some financial index (Gaur and Seshadri, 2005). However, different from the preexisting publicly traded macroeconomic index, we allow the trading instrument to be constructed and tailored to the supply chain-specific demand forecast needs. Under our framework, demand uncertainty information can be revealed early and be incorporated into the supply chain partners’ contract specifications. Our solution is robust to both the information and physical structures of the supply chain. That is, we allow retailers who have access to various sources of information to participate in and benefit from the trading platform because the information flow is managed independently by a third party and does not intertwine with retailers’ physical orders. The prediction market also has the ability to incorporate outside information. The COM framework suggests a new business process outsourcing and reengineering approach that sheds some light on managing the information supply chain.

The idea of business process outsourcing is supported by the literature in transaction cost theory, first coined by Coase (1937) and later generalized by Williamson (1979). It posits that certain economic tasks will be performed by firms, while others will be performed by the market, depending on the transaction cost of producing and distributing particular goods or services. Cost reduction and quality improvement are cited as the most important motivations for BPO (DiRomualdo and Gurbaxani, 1998). Information technologies have greatly reduced communication costs and increased interorganizational coordination efficiency, which make it possible for firms to source business processes from remote locations (Hagel and Singer, 1999). The literature has further suggested that firms with limited information processing capability need to employ BPO to collect and deliver quality information for decision making (Mani et al., 2006).

In our proposed framework, the prediction market plays an important role in aggregating and integrating dispersed information sources. Prediction market mechanism design is an emerging research area with much potential in the business world. There are two different streams of research exploring how to construct the prediction market. One type of prediction market is structured similar to the stock market, where contracts contingent on the outcomes of future events are actively traded. Fama (1970) postulated that prices in such competitive markets reflect all available information. This is traditionally known as the Efficient Market Hypothesis (EMH). The theoretical foundation of the EMH concept is based on rational expectations equilibrium (REE) models (Muth, 1961). In general, this stream of literature, represented by market microstructure models (Glosten and Milgrom, 1985; Kyle, 1985), analyzes price informativeness by linking prices to individual trading behaviors. Recently, research has focused on the reliability of the market price as a prediction vehicle (Spann and Skiera, 2003; Wolfers and Zitzewitz, 2004). Experimental results suggest that prices perform well as forecasts regardless of the specific characteristics of the prediction market (i.e., the effectiveness of market price as the prediction device is independent of the types of events to be predicted, whether the trading asset is virtual or real money, etc.). The forecasting capability of price appears to be better than that of existing benchmark methods such as opinion polls (Berg et al., 2005) or surveys of experts (Chen and Plott, 2002). Therefore, the prediction market can be used to elicit particular information of interest with great accuracy. In addition, prediction markets are recommended to serve as decision support tools to aid effective decision making in organizations under various business environments (Berg and Rietz, 2003).

Another research stream deviates from a zero-sum market game (in which informed traders with quality information earn positive expected profits at the cost of uninformed traders who do not possess good information) and links the market compensation mechanism with the cost of information acquisition. To our knowledge, Osband (1989) was among the first in this research stream to explicitly incorporate agent learning costs into a forecast elicitation model. The analysis suggests that organizations that operate on a “need-to-know” principle can reduce planning costs and control planning efficiency so that forecasting expertise is selected from among a handful of capable individuals. Chen et al. (2001, 2004) discussed incentive mechanisms to aggregate decentralized information within a small group to forecast the probability of a future event. Fang et al. (2007) proposed a novel betting mechanism to forecast the future value of a business subject when forecasters have heterogeneous ability to acquire signals with different precisions. Such a mechanism can motivate participants to incur certain costs to acquire relevant information. Decentralized information is aggregated efficiently, as the reliability of each forecast is utilized to weigh each piece of information. With special attention to the cost of information acquisition, Fang et al. showed that the betting market needs to be externally subsidized to insure that every trader is appropriately rewarded and, consequently, truthfully reveals her private information.

This paper builds and improves upon recent innovative research outcomes in the information systems and supply chain management fields. We discuss the design and implementation of different market mechanisms in the COM framework and aim to advance our understanding of both the opportunities and challenges in managing the market-based information supply chain.

## 3. The Collective Outsourcing to Market (COM) Framework

## 3.1 The General Framework

In a dynamically changing marketplace, both the manufacturer and the retailers need to effectively forecast product demand to reduce their operation overhead. However, individually, each firm has limited capability in its demand forecasting. If each of the retailers chooses an outsourcing vendor to help with the demand forecast, they have to individually negotiate the outsourcing contracts. Not only do they lack the necessary negotiation power, but there is no guarantee that they will be able to find a quality service provider. By collectively outsourcing the demand forecasting function to a specialized third party service vendor, retailers can realize economies of scale and be assured of information quality.

![](/api/attachments/E5DTKBME/fulltext/images/95429ffc26ea3580b27df407961584f6e9e712d3c4891235acecb6a18f3df803.jpg)  
Figure 1. The COM Framework

To demonstrate our collective outsourcing idea, we adopt a typical supply chain framework with one upstream manufacturer and multiple downstream retailers. Such a framework has been widely adopted in recent studies of supply chain coordination (e.g., Guo et al., 2006; Shin and Tunca, 2006; Wang and Zou, 2003). Figure 1 illustrates our general idea of separating the information flow from the physical product order flow. The information market acts as an information third party that is capable of eliciting and processing information from a variety of sources. Rather than negotiating a complex outsourcing contract on a one-to-one basis, the information third party designs a standard tradable contract and operates a market in which agents individually determine their respective outsourcing needs. To be specific, the tradable contract specifies a reward structure that is contingent on the future value of a macro economic factor that directly affects all retailers’ future market demand and, therefore, is related to their forecasting needs. We call the macro factor the retail index.

The input to the information market can come from sources both inside and outside the supply chain. First, individual retailers usually obtain private forecasts about the retail index that are more accurate than those of the manufacturer, which may result from their closer observation of the market. Aggregation of such information can form a quality forecast that is better than any individual prediction. Second, the information market can collect additional relevant information from sources outside the supply chain. That is, the market can be opened to outside traders under certain conditions so as to attract more valuable inputs. The aggregated information revealed in the market can be used to aid the decision making of both the manufacturer and the retailers. To achieve this, the contract must be designed to reward traders according to the accuracy of their information after future uncertainty is resolved. Those with better information will be encouraged to provide inputs and can expect to earn positive payoffs.

There are several important benefits of outsourcing to the information third party. The first benefit is its superior ability to process information and produce quality forecasts. The market has the ability to attract, analyze, and integrate all relevant information. It can extend the range of information elicitation beyond the physical supply chain boundary and hence increase its prediction power. The ability to absorb useful information from sources outside the supply chain is a unique feature of our model that is beyond the scope of traditional supply chain coordination research.

Second, the COM framework can properly align incentives from different parties through its reward mechanism. Since the retailers who make better predictions can expect higher payoffs, the quantitative reward will induce retailers to express their own predictions based on the best of their knowledge.

In addition, the market-based outsourcing contract can benefit all parties by reducing their agency costs. Agency costs refer to the additional efforts and costs incurred in managing contractual relationships such as monitoring the outsourcing vendor’s behavior and aligning the actions of the outsourcing vendor with the interests of the clients. On the one hand, the performance of the third party service provider is guaranteed by the effectiveness of the market’s informational role. The commitment to credible information sharing is achieved automatically by the market’s ability to aggregate information through the market price formation process. The market outcome is independent of the action and self-interest of the third party vendor. On the other hand, the third party vendor is neutral in the supply chain. By interacting with the information third party, supply chain partners can avoid the potential for gaming and strategic concerns. Therefore, our proposed COM framework can address both the process uncertainty in supply chain management and relational uncertainty in traditional outsourcing contract design.

Recent studies on prediction markets provide us with several mechanisms to consider in our COM framework. This paper discusses two major trends in prediction market mechanism design and the issue of choosing the appropriate mechanism under different supply chain forecasting environments.

## 3.2 A Simple Supply Chain Framework

In this section, we mathematically formulate the one-manufacturer-multiple-retailer supply chain to discuss the forecasting inefficiency in a decentralized supply chain environment. Then, in Sections 3.3 and 3.4, we discuss the candidate market designs proposed in Guo et al. (2006) and Fang et al. (2007), respectively. In Section 3.5 we compare the two designs and discuss other potential market implementations. Appendix C provides a summary of all the mathematic notations used in Sections 3.2 through 3.5.

Assume that there are N geographically distributed retailers who order a homogeneous product from a manufacturer. Each retailer faces uncertain market demand that can be expressed as a linear function of a macro factor, X, representing the systematic risk with an identically and independently distributed error term $\varepsilon _ { j }$ capturing the idiosyncratic risk for retailer i : $\boldsymbol { { D } _ { i } } = \boldsymbol { { a } _ { i } } + \boldsymbol { { b } _ { i } } \boldsymbol { { X } } + \boldsymbol { { \varepsilon } _ { i } }$ $i = 1 , \cdots , N$ , where $\pmb { \mathscr { a } } _ { j }$ and $b _ { i }$ are retailer-specific parameters that are common knowledge in the supply chain. We assume $\begin{array} { r } { X \sim N \left( s _ { 0 } , \frac { 1 } { \tau _ { 0 } } \right) , \varepsilon _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { \varepsilon } } \right) } \end{array}$ are both normally distributed.

We further assume that each retailer can privately observe a noisy signal $s _ { j }$ of the future value for the macro economic factor, $X = x$ . Specifically, we assume that $\pmb { S } _ { i } = \pmb { X } + \delta _ { i }$ where $\begin{array} { r } { \delta _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { i } } \right) } \end{array}$ is also identically and independently distributed, indicating the forecast error.

Ideally, if all retailers share their private forecasts truthfully among themselves and with the manufacturer, they will form a common belief on the uncertain macro factor $X , \quad \mathrm { i . e . }$ $\quad \ : \times \mid \{ s _ { i } , \tau _ { i } \} _ { i = 1 } ^ { N } \sim N \left( \frac { \sum _ { i = 0 } ^ { N } \tau _ { i } s _ { i } } { \sum _ { i = 0 } ^ { N } \tau _ { i } } , \frac { 1 } { \sum _ { i = 0 } ^ { N } \tau _ { i } } \right)$ . This aggregated forecast sharing scenario (indexed by “a”) provides

us with a full information benchmark solution to evaluate the collective outsourcing efficiency. Another benchmark scenario is a fully decentralized supply chain model without forecast outsourcing (indexed $\mathsf { b y } \ ^ { * } d ^ { \prime } )$ . In the decentralized model, the information assumption is that individual retailers can only utilize their own signals to make order decisions. The manufacturer, however, has no private signal and can only rely on the common prior belief $\begin{array} { r } { X \sim N \Big ( s _ { 0 } , \frac { 1 } { \tau _ { 0 } } \Big ) } \end{array}$

We model the supply chain as a manufacturer Stackelberg game as follows. The manufacturer announces a wholesale price $w ^ { j } \ ( \ j = \ a , d )$ . All retailers simultaneously order an amount $\boldsymbol { Q } _ { j } ^ { j }$ based on their own available information set $F _ { i } ^ { j }$ , for $i = 1 , \cdots , N$ . Specifically, let r be the retail price. Retailer $\boldsymbol { \bar { \mathbf { \Lambda } } }$ profit under scenario j is $\Pi _ { i } ^ { j } \left( Q _ { i } ^ { j } \mid w ^ { j } \right) = r \mathsf { m i n } \left[ Q _ { i } ^ { j } , D _ { i } \right] - w ^ { j } Q _ { i } ^ { j }$ , for $i = 1 , \cdots , N$ . In the second stage, the retailer i chooses an order quantity $\boldsymbol { Q } _ { i } ^ { j }$ to maximize her expected profit, based on her information set $F _ { i } ^ { j }$ , where $F _ { i } ^ { a } = \{ ( s _ { 1 , } s _ { 2 } , \cdots , s _ { N } ) \}$ and $\begin{array} { r } { F _ { i } ^ { d } = \left\{ s _ { i } \right\} } \end{array}$ . The retailer’s decision problem can be expressed as:

$$
\underset {Q _ {i} ^ {j} \geq 0} {\text { Max }} E \left[ \Pi_ {i} ^ {j} \left(Q _ {i} ^ {j} \mid w ^ {j}\right) \mid F _ {i} ^ {j} \right], \text { for } i = 1, \dots , N.\tag{1}
$$

Let c be the unit production cost. The manufacturer’s profit $\Pi _ { 0 } ^ { j } = \Big ( { \boldsymbol w } ^ { j } - { \boldsymbol c } \Big ) \sum _ { i = 1 } ^ { N } Q _ { i } ^ { j }$ . In the first stage, the manufacturer maximizes her expected profit by choosing the wholesale price $W ^ { j }$ based on her expected order quantities from the retailers, conditional on her own information set $F _ { 0 } ^ { j }$ , where $F _ { 0 } ^ { a } = \{ ( s _ { 1 , } s _ { 2 } , \cdots , s _ { N } ) \}$ and $F _ { 0 } ^ { d } = \mathcal { O }$ . The manufacturer’s decision problem is:

$$
\underset {w ^ {j} \geq 0} {\text { Max }} E \left[ \Pi_ {0} ^ {j} \left(w ^ {j}\right) \mid F _ {0} ^ {j} \right].
$$

(2)

To evaluate the efficiency of the supply chain coordination, we define $E \Pi ^ { j } \triangleq \sum _ { i = 0 } ^ { N } E \Pi _ { i } ^ { j }$ for $j = a , d$ to represent the expected supply chain profit, which is calculated as the sum of profits gained by all the chain partners under the respective supply chain scenarios.

Proposition 1: The expected supply chain profit in the aggregated scenario is higher than that in the decentralized scenario, i.e., $E \Pi ^ { a } > E \Pi ^ { d }$

Proposition 1 shows that fully shared information helps improve overall supply chain efficiency by allowing chain partners to make better decisions. It also illustrates an outstanding supply chain coordination problem in a decentralized decision making environment. Therefore, from a social

In fact, the signal can be of any linear combination of the macro factor. For example, ${ \pmb S } _ { i } = \alpha _ { 0 } + \alpha _ { 1 } { \pmb x } + \alpha _ { 2 } \delta _ { i }$ . We can always transfer such a signal $s _ { j }$ to a standardized $\begin{array} { r } { \tilde { \pmb { \mathscr { S } } } _ { i } = \frac { \pmb { \mathscr { S } } _ { i } - \alpha _ { 0 } } { \alpha _ { 1 } } = \pmb { X } + \tilde { \delta } _ { i } } \end{array}$ where $\begin{array} { r } { \tilde { \delta } _ { i } = \frac { \alpha _ { 2 } } { \alpha _ { 1 } } \delta _ { i } } \end{array}$

welfare perspective it is essential to construct incentive mechanisms that effectively attract all retailers to participate in the sharing paradigm – a collective information supply chain outsourcing. The real challenge, however, is that altruistic sharing rarely exists in real world settings. In the following, we discuss our proposed market-based mechanisms to address such fundamental issues as where the incentives come from and how to induce chain partners to share their private information truthfully.

## 3.3 Outsourcing to an Index Market

In this section, we discuss the information market mechanism design using the framework proposed in Guo et al. (2006). We show the influence of the market-based collective outsourcing on supply chain demand forecasting accuracy and its effect on the overall system efficiency.

Guo et al. (2006) proposed a publicly traded macro index and proved the efficiency improvement of the overall supply chain under certain circumstances. One important assumption in the Guo et al. model is that the supply chain has a symmetric information structure, where all the retailers have similar abilities to produce their forecasts, yet no one is pivotal. That is, $\tau _ { i } = \tau _ { \delta }$ for $i = 1 , 2 , \cdots , N$ Most existing literature that studies the supply chain coordination assumes a symmetric structure for tractability. We adopt this convention here to derive our major insights. In Section 3.4, we relax this assumption and discuss the possibility of designing a market mechanism to aggregate heterogeneous sources of information.

The index market operates like an open book call futures market (Fan et al., 2002). Participants can buy or sell contingent contracts that pay \$x if the future true value of the macro factor $X = x$ . The current market price p is determined based on the participants’ respective sources of information. Market trading aggregates the initially locally available forecast information as if participants engage in collaborative forecasting projects under the market coordination. This is our COM scenario (indexed by $j = m i .$ ).

The supply chain partners’ decision problems have the same form as described in Section 3.2. The only difference is the available information. In the second stage game, when a retailer orders from the manufacturer, she can not only look at her private signal $s _ { j }$ , but also can refer to the index market price $p$ to find more information about other market participants’ perceptions of the future macro economic environment that will affect the demand. Therefore, the information set is expressed as $F _ { i } ^ { m i } = \{ s _ { i } , p \}$ , for $i = 1 , 2 , \cdots , N$ . In the first stage, the manufacturer makes a decision based purely on the index market price. That is, ${ F _ { 0 } ^ { m i } = \{ p \} }$ . In the following, we discuss how the market price $p$ incorporates decentralized information.

## 3.3.1 The Index Market Price

While the market price is determined by the market clearing mechanism that could vary according to different market microstructures, we focus on one type of market structure where the market maker responds to the aggregate net order by taking an opposite position. We assume that the market maker does not have any private information. Thus, to prevent economic loss, the market maker sets the index price as the expected value of the future payoff given the current aggregate net orders in the market.

We assume that there are M risk-neutral informed traders in the market, which is composed of N retailers and $N _ { 0 }$ traders from outside the supply chain. That is, $M = N + N _ { 0 }$ . We do not distinguish among informed traders’ forecast abilities. That is, we assume all informed traders in the market, including retailers, observe $\begin{array} { r } { \pmb { \mathscr { s } } _ { i } = \pmb { X } + \delta _ { i } , \delta _ { i } \sim \pmb { N } \big ( 0 , \frac { 1 } { \tau _ { \delta } } \big ) } \end{array}$ , for $i = 1 , 2 , \cdots , M$ . But this simplification will not affect the major model insights. We also assume that some uninformed traders submit a random, exogenous aggregate net order $\omega \sim N \left( 0 , \frac { \ d _ { 1 } } { \tau _ { \omega } } \right)$ . Note that the noisy traders’ assumption incorporates all the unpredictable elements that may come from market participants’ random liquidation demands or irrational behaviors. Similar assumptions have been used throughout the finance literature.

The concept of Rational Expectations Equilibrium (REE) is the key theoretical concept that explains how individual traders’ information gets integrated into the market price. We provide the definition of REE in Appendix A. The following proposition states an informed trader’s equilibrium trading strategy and shows how the dispersed information is aggregated in the equilibrium market price. Guo et al. (2006) provided a complete proof of the results.

Proposition $z ^ { 2 } { \mathrm { ; } }$ : There exists a unique linear rational expectations equilibrium (REE) in which

1) An informed trader i adopts a linear trading strategy $o _ { i } = B _ { 0 } + B _ { 1 } s _ { i } + B _ { 2 } p _ { i }$

2) The equilibrium market price $\begin{array} { r } { p = A _ { 0 } + A _ { 1 } \Bigg ( \underset { i = 1 } { \overset { M } { \sum } } s _ { i } + \frac { \omega } { L } \Bigg ) ; } \end{array}$

where $A _ { 0 } , A _ { 1 } , B _ { 0 } , B _ { 1 } , B _ { 2 } ,$ and L are constants.

Therefore, the index price p can be viewed as a noise signal of the aggregated prediction $\sum _ { i = 1 } ^ { M } s _ { i }$ . The existence and uniqueness of the linear REE guarantee a one-to-one mapping from the dispersed market signals to the aggregate market price. L, which often represents market liquidity in the REE literature, reflects the precision of the information transformation. The larger the value of $L ,$ and/or the less the influence of $\omega$ , the more precise $p$ is as an aggregate indicator of the useful signals.

It is also worth noting that the index market price reflects the average signal $\frac { 1 } { M } \sum _ { i = 1 } ^ { M } s _ { i }$ rather than each individual signal. By law of large numbers, such a signal is “manipulation free” when the number of informed market participants is large. In other words, suppose one retailer submits an order $O _ { i } = B _ { 0 } + B _ { 1 } \left( s _ { i } + \kappa _ { i } \right) + B _ { 2 } p$ intending to mislead the market using a disturbed signal $s _ { i } + \kappa _ { i }$

$$
s _ {i}
$$

accuracy is discounted by a factor $A _ { 1 } / M$ . We can easily show that, when M is large enough, one single trader’s effort to mislead the market price will be in vain. Given that the equilibrium market price is insensitive to one trader’s signal distortion, the trader will in fact be worse off if she deviates from the equilibrium trading strategy that maximizes her expected payoff. Hence, no one agent has an incentive to manipulate the market. Agents’ best strategy is to follow the one described in Proposition 2. This shows that the market-based information revelation is incentive compatible.

The aggregate forecasts revealed by the market price can be extremely accurate when the number of informed traders approaches infinity. To quantify this effect, we define price informativeness as $P I \triangleq { \frac { 1 } { \mathsf { v a r } ( x | p ) } }$ . That is to say, the less variation of X is conditional on $p ,$ the more informative the index price $p$ is. We use the reciprocal to capture this relationship in the definition.

Proposition 3: The market price becomes more informative when the number of informed traders in the market increases, i.e., PI increases in M. Moreover, when the number of informed traders in the market approaches infinity, the index market price converges to the true value of the retail index, $\boldsymbol { i . 6 . , }$ lim $P I = \infty$ and lim $p = X$ M→∞ M→∞

Since price precision increases in the number of informed traders, informational efficiency rises as

more useful information is impounded in the market price.

## 3.3.2 Value of the Index Market on Forecasting

In this section, we show that the demand forecast generated by a specially designed index market is more accurate than the individual retailer’s own forecast (the decentralized supply chain scenario where no forecast information is shared). In addition, we show that the collective demand forecast can be as precise as that of an aggregate forecast (the aggregated supply chain scenario where all supply chain partners truthfully share their own demand forecasts). Finally, we show that it is possible that the overall prediction power of the supply chain partners improves because the prediction market has the ability to incorporate outside information sources. For example, if the useful information possessed by $N _ { 0 }$ informed outside traders dominates the noisy information possessed by those uninformed traders, then the open market’s prediction power will be greater than that of a closed supply chain forecast sharing model.

Using the Bayesian rule of update, we can derive the respective means $\bar { X } _ { i } ^ { j }$ and variances $\frac { 1 } { \Gamma _ { i } ^ { j } }$ of retailer i's forecasted demand distribution, for $i = 1 , 2 , \cdots , N$ , under the three supply chain models $( \mathfrak { i . e . , \ j } = \mathfrak { a , } d , m ^ { i } )$

$$
\bar {X} _ {i} ^ {a} = \frac {\tau_ {0}}{N \tau_ {\delta} + \tau_ {0}} \mathsf {s} _ {0} + \frac {\tau_ {\delta}}{N \tau_ {\delta} + \tau_ {0}} \sum_ {i = 1} ^ {N} \mathsf {s} _ {i}, \bar {X} _ {i} ^ {d} = \frac {\tau_ {0}}{\tau_ {\delta} + \tau_ {0}} \mathsf {s} _ {0} + \frac {\tau_ {\delta}}{\tau_ {\delta} + \tau_ {0}} \mathsf {s} _ {i},
$$

$$
\overline {{X}} _ {i} ^ {m i} = \frac {\tau_ {0}}{\tau_ {\delta} + \tau_ {0} + (M - 1) ^ {2} \tau_ {v}} \mathsf {S} _ {0} + \frac {\tau_ {\delta}}{\tau_ {\delta} + \tau_ {0} + (M - 1) ^ {2} \tau_ {v}} \mathsf {S} _ {i} + \frac {(M - 1) \tau_ {v}}{\tau_ {\delta} + \tau_ {0} + (M - 1) ^ {2} \tau_ {v}} \big (\mathsf {S} _ {- i} + \frac {\omega}{L} \big)
$$

where $\begin{array} { r } { \pmb { \mathscr { s } } _ { - i } \triangleq \sum _ { j = 1 } ^ { N } \pmb { \mathscr { s } } _ { j } - \pmb { \mathscr { s } } _ { i } , \quad \tau _ { v } \triangleq \left( \frac { M - 1 } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { \omega } } \right) ^ { - 1 } , } \end{array}$ and $\begin{array} { r } { \frac { 1 } { \Gamma _ { i } ^ { a } } = \frac { b _ { i } ^ { 2 } } { \tau _ { 0 } + N \tau _ { \delta } } + \frac { 1 } { \tau _ { \varepsilon } } , \quad \frac { 1 } { \Gamma _ { i } ^ { d } } = \frac { b _ { i } ^ { 2 } } { \tau _ { 0 } + \tau _ { \delta } } + \frac { 1 } { \tau _ { \varepsilon } } } \end{array}$ $\begin{array} { r } { \frac { 1 } { \Gamma _ { i } ^ { m i } } = \frac { b _ { i } ^ { 2 } } { \tau _ { 0 } + \tau _ { \delta } + ( M - 1 ) \tau _ { v } } + \frac { 1 } { \tau _ { \varepsilon } } . } \end{array}$

Since the prior demand distribution (before observing any signal s<sub>i</sub>) is a normal distribution with mean $\overline { { X } } _ { i } ^ { 0 } = a _ { i } + b _ { i } s _ { 0 }$ and variance $\begin{array} { r } { \frac { 1 } { \Gamma _ { i } ^ { 0 } } = \frac { b _ { i } ^ { 2 } } { \tau _ { 0 } } + \frac { 1 } { \tau _ { \varepsilon } } } \end{array}$ , by simple comparison we obtain the following result.

Proposition 4: The index market-based forecasting yields the same mean but higher precision than the prior demand distribution, i.e., $E \big ( \bar { X } _ { i } ^ { m i } \big ) = \bar { X } _ { i } ^ { 0 } , \ \Gamma _ { i } ^ { m i } \geq \Gamma _ { i } ^ { 0 }$ . Furthermore, there are conditions under which the index market-based forecasting outperforms the aggregated forecasting, i.e., $\Gamma _ { i } ^ { m i } \geq \Gamma _ { i } ^ { a } . ^ { 3 }$

Proposition 4 demonstrates the demand forecasting accuracy under the COM framework. The index market-based forecasting not only improves upon the prior knowledge about the demand distribution, but may be more accurate than the aggregate forecast. This is because the market not only incorporates all the private signals from the retailers, but also integrates other information sources from the $N _ { 0 }$ outside traders. The more useful information that comes from outside traders, the better the COM framework is compared to the full-information benchmark where all the retailers truthfully share their private information.

## 3.3.3 Value of Information Sharing on the Bullwhip Effect

The bullwhip effect is a well-known informational problem in the supply chain represented by the observed increasing order variances from downstream partners in the supply chain (Lee et al., 1997). We show that improved demand forecasting reduces the retailers’ order variation and thus alleviates the information distortion (e.g., the bullwhip effect) in the supply chain.

It is easy to show that, in our newsvendor-based model, retailer i ’s optimal order quantity is determined by

$$
Q _ {i} ^ {j} = a _ {i} + b _ {i} \overline {{X}} _ {i} ^ {j} + \frac {1}{\sqrt {\Gamma_ {i} ^ {j}}} \Phi^ {- 1} \left(1 - \frac {\omega^ {j}}{r}\right), f o r j = a, d, m i.
$$

We see that variation of the retailer’s order quantity is proportional to its forecasting standard deviation. Comparing the order quantities, we obtain the following result.

Proposition 5: With the information revealed from the index market, the manufacturer can estimate each retailer’s order with more accuracy, i.e., var $\left( Q _ { i } ^ { m i } \mid p \right) < \mathsf { v a r } \left( Q _ { i } ^ { d } \right)$ . Moreover, when the index market is more liquid, the order variance decreases, i.e., var $\left( Q _ { i } ^ { m i } \mid p \right)$ decreases as M increases. When the index market is extremely efficient, the order variance approaches $0 , \quad i . e .$ lim va $\harpoonright A _ { i } ^ { m i } \mid p \rangle = \mathsf { v a r } \left( Q _ { i } ^ { a } \mid ( S _ { i } ) _ { i = 1 } ^ { N } \right) = 0$ M →∞

Since the index market price is precise enough to forecast the macro uncertainty, retailers can more accurately forecast the macro economy and their own demand when making their order decisions. The index market-based forecast sharing helps reduce order variance from the retailers. The manufacturer can also benefit by making more accurate inferences about the expected aggregate orders from her contracted retailers.

## 3.3.4 Value of COM on Supply Chain Efficiency

The outsourced supply chain generates greater total system efficiency than the non-outsourced (decentralized) supply chain. Under certain conditions, COM could produce more accurate forecasts and greater economic gain than the aggregate supply chain solution (the full information benchmark).

The total expected supply chain profit is determined by the sum of all supply chain partners’ expected profits. After simple algebraic manipulation, it can be expressed as:

$$
E \Pi^ {j} = \sum_ {i = 0} ^ {N} E \Pi_ {i} ^ {j} = (r - c) E \left[ \sum_ {i = 0} ^ {N} Q _ {i} ^ {j} \right] - r E \sum_ {i = 0} ^ {N} \Psi_ {i, j} (Q _ {i} ^ {j}),
$$

where $\begin{array} { r } { \Psi _ { i , j } \left( \boldsymbol { Q } _ { i } ^ { j } \right) = \frac { 1 } { \sqrt { \Gamma _ { i } ^ { d } } } \int _ { \infty } ^ { - t _ { j } } \boldsymbol { \Phi } \left( t \right) } \end{array}$ dt  and $t _ { j } = \Phi ^ { - 1 } \left( \frac { \omega ^ { d } } { r } \right)$ , for $j = a , d , m i$

Proposition 6: Under mild regularity conditions, the expected supply chain profit is higher under the index market coordination than that in the decentralized scenario, i.e., $E \Pi ^ { m i } > E \Pi ^ { d }$ . Moreover, the expected supply chain profit under the index market coordination approaches the full information benchmark when the number of retailers approaches infinity, i.e., $\operatorname* { l i m } _ { M  \infty } E \Pi ^ { m i } = \operatorname* { l i m } _ { N  \infty } E \Pi ^ { a }$

The traditional supply chain literature considers the incentive and coordination issues by viewing the supply chain as a closed system. Our proposed framework demonstrates the value of useful information from outside sources to increase overall supply chain efficiency. This framework is extremely suitable in situations where the number of supply chain partners is large.

## 3.4 A Betting Market When Precision is Heterogeneous

In some supply chain practices, the number of chain partners may not be large. In addition, they may have heterogeneous abilities to predict future uncertainty. That is, the reliability of each retailer’s private signal can be different due to retailers’ access to potentially different information sources. In this section, we revise the assumption on the information structure in the previous model to address this issue. Specifically, we assume that each retailer i obtains a private signal $\pmb { s } _ { i } = \pmb { x } + \delta _ { i }$ , where $\begin{array} { r } { \delta _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { i } } \right) } \end{array}$ are independent forecasting errors. $\tau _ { j }$ is the precision of each private signal, which is different for each retailer. The larger the $\tau _ { j }$ , the less the variance of $\delta _ { j }$ and the more precise is the private forecast of retailer i.

If all the retailers share their signals $\left\{ \thinspace s _ { i } \right\} _ { i = 1 , 2 , \cdots , N }$ honestly, and the precisions of those signals $\left\{ \tau _ { i } \right\} _ { i = 1 , 2 , \cdots , N }$ are public information, we shall have that $\begin{array} { r } { X \mid \{ s _ { i } , \tau _ { i } \} _ { i = 1 } ^ { N } \sim N \left( \frac { \sum _ { i = 0 } ^ { N } \tau _ { i } s _ { i } } { \sum _ { i = 0 } ^ { N } \tau _ { i } } , \frac { 1 } { \sum _ { i = 0 } ^ { N } \tau _ { i } } \right) } \end{array}$ following Normal Learning Theorem (DeGroot, 1970). It is obvious that an efficient aggregation of all the retailers’ private forecasts is a weighted average of all the retailers’ signals $\left\{ \thinspace s _ { i } \right\} _ { i = 1 , 2 , \cdots , N }$ and that the weights are proportional to the precision of their signals $\left\{ \tau _ { i } \right\} _ { i = 1 , 2 , \cdots , N }$ . Therefore, in order to get the best aggregation of the signals, not only shall each retailer share her private forecast $s _ { j }$ , she shall also reveal her reliability $\tau _ { j }$ . However, the market mechanism discussed in Section 3.2 has a reward structure that is based only on $s _ { j }$ and is generally unable to distinguish the precision $\tau _ { j }$ . After all, the signal is just a “guess” about the future uncertainty. Two retailers may get two signals of the same value, while one is extremely confident but the other is not so sure about it. A mechanism needs to be specifically designed to elicit both $s _ { j }$ and $\tau _ { j }$ from a retailer.

Recall that in our index market design there is a one-to-one mapping between the trading volume and a trader’s signal. If the task of information aggregation is two dimensional (both the signal and the precision), then theoretically we need two market parameters. To fulfill this task, we adopt the market mechanism proposed by Fang et al. (2007). The mechanism was designed based on the popular saying, “putting your money where your mouth is.” Specifically, the information third party can run a betting market to allow each participant i to submit a report $r _ { i }$ on the possible future value of X and place a certain amount of money as a bet on his or her report, $B _ { i }$ The task of the third party is to design a reward function $\boldsymbol { f } \left( \boldsymbol { r } _ { i } , \boldsymbol { B } _ { i } , \boldsymbol { X } \right)$ paid to each of the participants, which is contingent on the corresponding report and bet, $\left( r _ { i } , \boldsymbol { B _ { i } } \right)$ . To effectively aggregate the information, the reward function should:

1. induce each participant to report truthfully her private forecast of the future value of $X ,$ that is, $r _ { i } = E [ X \mid s _ { i } ]$ ;

2. elicit the precision of each bettor’s private signal $s _ { j }$ , that is, $B _ { i } = g ( \tau _ { i } )$ where $g ( \cdot )$ is monotonic.

One of the candidate reward functions satisfying the above requirement is a quadratic loss function $f \left( r _ { i } , B _ { i } , X \right) = 2 B _ { i } ^ { \frac { 1 } { 2 } } \left( \tau - \left( r _ { i } - X \right) ^ { 2 } \right)$ , where the participant maximizes the payoff when the report coincides with the future value of X.

For each risk-neutral retailer, the overall maximization problem is to decide the report, bet, and future order quantity so as to maximize her aggregate expected payoff from both the betting market and local commodity markets. Since all the retailers are risk neutral, the two decisions are independent. Proposition 7 shows the best strategy of each bettor.

Proposition 7: The bettor $i s$ optimal betting strategy is $\begin{array} { r } { r _ { i } ^ { \star } = E [ X \mid \pmb { \mathscr { s } } _ { i } ] = \frac { \tau _ { 0 } \pmb { \mathscr { s } } _ { 0 } + \tau _ { i } \pmb { \mathscr { s } } _ { i } } { \tau _ { 0 } + \tau _ { i } } } \end{array}$ and $\begin{array} { r } { B _ { i } ^ { ' } = \frac { \tau _ { i } ^ { 2 } } { \tau _ { 0 } ^ { 2 } \left( \tau _ { 0 } + \tau _ { i } \right) ^ { 2 } } } \end{array}$ with a positive expected payoff $\frac { \tau _ { i } ^ { 2 } } { \left( \tau _ { 0 } + \tau _ { i } \right) ^ { 2 } }$

A rational bettor will bet a positive amount of money as long as her precision is positive $( \tau _ { i } > 0 )$ . In addition, the bet increases when the signal is more precise (i.e., as $\tau _ { j }$ increases). A bettor with no relevant information $( \tau _ { i } = 0 )$ will not place a bet. Therefore, the market can effectively aggregate all the relevant information without generating noisy traders.

Proposition 8: Based on bettor i's report and bet $\left( r _ { i } , \boldsymbol { B _ { i } } \right)$ , the market maker can distill the bettor’s private information and precision using the following formulae $\begin{array} { r } { \pmb { S _ { i } } = \frac { \tau _ { 0 } B _ { i } ^ { \frac { 1 } { 2 } } + r _ { i } - s _ { 0 } } { \tau _ { 0 } B _ { i } ^ { \frac { 1 } { 2 } } } } \end{array}$ and $\tau _ { i } = \frac { \tau _ { 0 } } { 1 - \tau _ { 0 } B _ { i } ^ { \frac { 1 } { 2 } } } - \tau _ { 0 }$

This shows that the betting mechanism will reveal both the bettor’s signal and its precision. The information can then aggregate all $\{ s _ { i } , \tau _ { i } \} _ { i = 1 } ^ { N }$ , achieving the objective of the two dimensional information aggregation.

## 4. Discussion and Implementation

The proposed COM framework advances supply chain information coordination through its ability to aggregate dispersed information under different informational assumptions and from a variety of sources. A market mechanism is important, as its reward structure provides an incentive for retailers to reveal their private forecasts. In the following, we first compare the two market mechanisms that we discussed above. Then we demonstrate the role of the information third party and discuss the benefits and costs of implementation.

## 4.1 Comparison of Market Mechanisms

The index market is an open system. Its ability to extract and aggregate valuable information from outside of the supply chain is its major advantage. Accordingly, this market mechanism is suitable in a forecasting environment where the subject is not sensitive, and the subject itself attracts participation from outside experts. Some macroeconomic variables tend to be insensitive subjects. For example, economic indicators such as the U.S. gross domestic product and retail sales fall in this category. Moreover, these macro level factors generate public attention easily, so traders outside of the supply chain can contribute to the information aggregation and improve the market’s prediction power. Therefore, this market mechanism has the potential to generate forecasts that are more accurate than those of any individual retailer or what can be obtained through a closed supply chain system.

Compared to the index market mechanism, a betting mechanism has an advantage over aggregate information when the sources of dispersed information are not evenly distributed. In addition, the information third party can control all the bets and reports that are not observable to other bettors. This provides a secure way to incorporate outside information without reviewing the aggregate prediction. The betting market mechanism is especially useful when the forecasting subject is sensitive and the dissemination of information should be restricted within the supply chain. Very often, such a sensitive forecasting subject does not attract attention from the public, and thus it is impractical to trade in an open market environment. Therefore, the betting mechanism is suitable for restricted participation when the supply chain partners have heterogeneous forecasting capabilities and some retailers have better information than others.

## 4.2 Benefits of Market Implementation

In addition to the various benefits discussed in Section 3.1., another aspect of the market-based incentive alignment is its immunity to the moral hazard problem in traditional contract design and coordination (Grossman and Hart, 1983). For example, as a risk sharing mechanism, a buy-back contract allows retailers to sell back unsold products at a pre-specified salvage value to the manufacturer. The retailer may not put much effort into selling products if the promotion cost is higher than the guaranteed salvage value. The market-contingent contract can solve this moral hazard problem, since it is written on the retail index, which is highly correlated with the retailers’ demand, but retailers still have to bear the residual risk of their own uncertain market demand.

Understanding the tradeoff between risk and incentive has been a complex task (Tirole, 1998). The market-based framework extends the range of information sharing beyond the traditional supply chain boundaries. It also opens the door for other market innovations including the introduction of securities and derivatives for the purpose of managing corporate risk. By separating the information flow from the physical product flow, retailers may hedge their own operational risk effectively using financial instruments available in the information market. Retailers’ self-selected risk management may be more effective than relying on the construction of overly complex and hard-to-implement contracts to achieve the coordination.

## 4.3 Costs of Market Implementation

The information third party plays a crucial role in successfully managing the information supply chain. The third party should be trusted by all the chain members to share information truthfully via the designed reward mechanism. In constructing an open market, the information third party should also be capable of understanding the supply chain information structure, investigating the correlations of the retailers’ demands, and identifying the macro factor to forecast. In choosing an effective market mechanism, the third party also needs to estimate how the private information is distributed among all the chain partners and whether outside information sources are needed. The information third party is then able to design the appropriate type of prediction market and to deliver the aggregate prediction with the desired solution quality.

However, there will always be costs associated with the third party, for example, the cost to hire such a third party and the cost for each company to communicate with the third party. In order to manage an electronic prediction market, the supply chain partners would have to provide the budget to invest in the hardware and software to develop and support the market function. However, with the decreasing cost of the IT infrastructure and the increasing popularity and acceptance of prediction markets, such costs are becoming more affordable. One possibility is that supply chain partners share the cost. Another possibility is that the manufacturer or whoever benefits the most from the final prediction provides the subsidy.

The cost of running a prediction market varies depending on the choice of market mechanism. An index market discussed in Section 3.2 is essentially a zero-sum market, meaning that the market maker (generally the information third party) does not provide explicit compensation and expects no profit (or loss). The traders purchase contracts expecting to make money from less-informed traders (generally called the noisy traders). The presence of noisy traders can therefore motivate informed traders to participate in the market. However, their random orders may reduce the overall precision of the equilibrium price. If adopting the betting mechanism described in Section 3.3, the market maker designs the betting contract so that each participant can expect a positive payoff if she has quality information. The more precise the information source, the higher payoff the participant can expect to get. The reward mechanism lures traders to research and improve their information precision. The market maker, therefore, has to compensate for the cost of information acquisition in order to get more precise information. Fortunately, the compensation costs can be controlled by the design of contract parameters. Fang et al. (2007) has proven that the gain from getting more accurate predictions can always exceed the overall compensation cost, if the contract parameters are chosen appropriately.

Being aware of the potential cost associated with the collective outsourcing, supply chain members must jointly decide whether the gain in efficiency will overcome the cost and how the cost should be shared among the partners. The choice could vary in different scenarios. Our discussion attempts to provide a general guideline for selecting who will participate and how the collective outsourcing activities work.

## 5. Conclusion

Parallel to the physical supply chain, and fundamentally integral to it, are the information supply chains that help achieve business objectives by enhancing critical business processes. By separating the information flow from the physical order flow in the supply chain, we are able to find a more efficient way of managing the information supply chain that brings a number of important supply chain benefits. Specifically, we propose a market-based framework centralizing the entire supply chain demand forecasting task by collectively outsourcing to a market that supports information-intensive business process reengineering. Our outsourcing market can be organized as an open, real market that trades futures contracts based on a properly identified macroeconomic factor. It can also be designed as a closed betting market with pre-specified reward structures.

The two market mechanisms represent two radically new forms of information sharing to deal with different supply chain information management challenges. The index market has the potential to extract information from outside the supply chain and provides a foundation for hedging other economic risks on an aggregate level. The betting market mechanism is particularly powerful in eliciting private information with different reliabilities. Depending on the characteristics of forecast subjects and their information sharing needs, an information third party can choose the proper mechanism to fulfill the outsourcing task.

This paper examines new opportunities in supply chain process innovation. We present an alternative outsourcing model that has some important potential benefits. First, we focus on the economic value derived from a collective knowledge base by considering outsourcing the demand forecast functions that enable supply chain business process reengineering. Second, collaborative forecasts can be implicitly elicited and effectively coordinated in the marketplace without costly individual contract negotiation and enforcement. Incentives for different supply chain entities to share private information are properly aligned in our market-based framework. In addition, collective outsourcing is more efficient in that it not only pools knowledge from individual firms, but elicits information from other knowledgeable experts who may not necessarily be included in the outsourcing contract. Finally, the market-based framework opens up opportunities for other business innovations (Hull, 1993; Shiller, 1993). The trading platform has the IT option value that can be fully leveraged to implement other financial innovations such as trading various derivative contracts for supply chain partners to hedge their operational risks.

We contribute to supply chain information systems design by bridging the current research gap between collective outsourcing and supply chain coordination. Future work could extend the informational role of markets to their function of hedging firms’ operational risk from the supply chain risk management perspective.

## References

Aviv, Y. (2001) “The effect of collaborative forecasting on supply chain performance”, Management Science, 47(10), pp. 1326-1343.

Berg, J.E., R. Forsythe, T. Nelson, and T. Rietz (2005) “What Makes Markets Predict Well? Evidence from the Iowa Electronic Markets”, in Handbook of Experimental Economic Results, (eds) by C. Plott and V. Smith. Elsevier.

Berg, J. E. and T. A. Rietz (2003) “Prediction Markets as Decision Support Systems”, Information Systems Frontiers, 5(1), pp. 79-93.

Bergemann, D. and J. Välimäki (2002) “Information Acquisition and Efficient Mechanism Design”, Econometrica, 70(3), pp. 1007-1033.

Cachon, G. and M. Fisher. (2000) “Supply chain inventory management and the value of shared information”, Management Science, 46(8), pp. 1032-1048.

Chen, F., Z. Drezner, J. K. Ryan, and D. Simchi-Levi (2000) “Quantifying the Bullwhip Effect in a Simple Supply Chain: The Impact of Forecasting, Lead Times and Information”, Management Science, 46(3), pp. 436-443.

Chen, K.Y., L. R. Fine, and B. A. Huberman (2001) “Forecasting Uncertain Events with Small Groups”, Proc. ACM EC’01 Conf. ACM, Tampa, FL.

Chen, K.Y., L. R. Fine, and B. A. Huberman (2004) “Eliminating Public Knowledge Biases in Information-Aggregation Mechanisms”, Management Science, 50(7), pp. 983-994.

Chen, K.Y. and C. Plott (2002) “Information Aggregation Mechanisms: Concept, Design and

Implementation for a Sales Forecasting Problem”, California Institute of Technology, working paper.

Clarke, E. H. (1971) “Multipart pricing of public goods”, Public Choice, pp. 17–33.

Coase, R. (1937) “The Nature of the Firm”, Econometrica, 4, pp. 386-405.

Cowles, A. (1933) “Can stock market forecasters forecast?” Econometrica, 1, pp. 309-324.

DeGroot, M.H. (1970) Optimal Statistical Decision, New Yok, NY: McGraw Hill.

DiRomualdo, A. and V. Gurbaxani (1998) “Strategic Intent for IT Outsourcing”, Sloan Management Review, 39(4), pp. 67-80.

Fama, E.F. (1970) “Efficient Capital Markets: A Review of Theory and Empirical Work”, Journal of Finance, 25(2), pp. 383-417.

Fan, M., S. Srinivasan, J. Stallaert, and A. B. Whinston (2002) Electronic Commerce and the Revolution in Financial Markets. Thomson Learning.

Fang, F., M. B. Stinchcombe, and A. B. Whinston (2007) “Putting Your Money Where Your Mouth is – A Betting Platform for Better Prediction”, Review of Network Economics, 6(2), pp. 214-238.

Foroohar, R. (2003) “A New Wind Tunnel for Companies: Testing Economics Theories through Expriments” Newsweek, Oct. 20 http://msnbc.msn.com/id/3087117/

Gaur, V. and S. Seshadri. (2005) “Hedging Inventory Risk Through Market Instruments”, Manufacturing & Service Operations Management, 7(2), pp. 103-120.

Grossman, S. J. and O. D. Hart (1983) “An Analysis of the Principal-Agent Problem”, Econometrica, 51, pp. 7-45.

Glosten, L.R. and P.R. Milgrom (1985) “Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders”, Journal of Financial Economics, 14, pp. 71-100.

Groves, T. (1973) “Incentives in team”,. Econometrica, pp. 617–631.

Guo, Z., F. Fang, and A. B. Whinston (2006) “Supply Chain Information Sharing in a Macro Prediction Market”, Decision Support Systems, 42, pp. 1944-1958.

Hagel, J. and M. Singer (1999) “Unbundling the Corporation”, Harvard Business Review, 77(2), pp. 133-141.

Hull, J. C. (1993) Options, Futures, and Other Derivative Securities, Englewood Cliffs, NJ: Prentice Hall.

Kyle, A. S. (1985) “Continuous Auctions and Insider Trading”, Econometrica, 53, pp. 1315-1336.

Lee, H., P. Padmanabhan, and S. Whang (1997) “Information Distortion in a Supply Chain: The Bullwhip Effect”, Management Science, 43(4), pp. 546-558.

Li, L. (2002) Information sharing in a supply chain with horizontal competition. Management Science 48(9), pp. 1196-1212.

Mani, D., Barua, A., and A. B. Whinston (2006) “Successfully Governing Business Process Outsourcing Relationships”, MIS Quarterly Executive, 5(1), pp. 15-29.

Muth, J.F. (1961) “Rational Expectations and the Theory of Price Movements”, Econometrica, 29, pp. 315-335.

Osband, K. (1989) “Optimal Forecasting Incentives”, Journal of Political Economy, 97(5), pp. 1091- 1112.

Shiller, R. (1993) Macro Markets: Creating Institutions for Managing Society's Largest Economic Risks, Oxford University Press.

Shin, H. and T. I. Tunca (2006) Beating the accuracy trap: Overinvestment in demand forecasting and supply chain coordination with information acquisition under downstream competition. Working paper. Stanford University.

Spann, M. and B. Skiera (2003) “Internet-Based Virtual Stock Markets for Business Forecasting”, Management Science, 49(10), pp. 1310-1326.

Tirole, J. 1998. The Theory of Industrial Organization. The MIT Press: Cambridge, Massachusetts.

Vickrey, W. (1961) “Counterspeculation, auctions and competitive sealed tenders” Journal of Finance, pp. 8–37.

Whang, S. and Y. Zou (2003) “The Informational Role of the Secondary Market on the Supply Chain”, working paper, Stanford University.

Williamson, O.E. (1979) “Transaction Cost Economics: The Governance of Contractual Relations”, Journal of Law and Economics, 22, pp. 233-262.

Wolfers, J. and E. Zitzewitz (2004) “Prediction markets”, Journal of Economic Perspectives, 18(2), pp. 107-127.

## Appendix

## A. REE in the Macro Index Market

We assume that each informed trader $i = 1 , 2 , \cdots , M$ , obtains a private signal $\pmb { \mathscr { s } } _ { i } = \pmb { \mathscr { x } } + \delta _ { i }$ , where $\begin{array} { r } { \delta _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { \delta } } \right) } \end{array}$ and places an order $O _ { j }$ while taking the price information into account to maximize her expected return from the index market.

$$
\max _ {o _ {i}} E [ (X - p (y)) o _ {i} \mid s _ {i}, p ]\tag{A1}
$$

There are also some uninformed traders whose aggregate net order is random and exogenously given, i.e., $\begin{array} { r } { \omega \sim N \big ( 0 , \frac { 1 } { \tau _ { \omega } } \big ) . \mathbf { \Psi } ^ { 4 } \mathsf { A } } \end{array}$ rational expectations equilibrium (REE) is defined by two components. First, a trading strategy $O _ { j }$ , for $i = 1 , 2 , \cdots , M$ , that solves the above maximization problem given pricing function $p ( y )$ . Second, a pricing function $p ( y )$ such that given the trading strategy $o _ { j }$ $i = 1 , 2 , \cdots , M$ , we have

$$
p (y) = E \Big [ X | y = \sum_ {i = 1} ^ {M} o _ {i} + \omega \Big ]\tag{A2}
$$

where $\textstyle y = \sum _ { i = 1 } ^ { M } o _ { i } + \omega$ is the aggregate demand.

The system of equations (A1) and (A2) collectively define the REE in the macro index market.

## B. Proofs of Propositions

## Sketch of Proofs of Propositions 1 & 6:

The expected supply chain profits under three supply chain structures are

$$
\begin{array}{r l r} & & E \Pi^ {d} = (r - c) E \Big [ \sum_ {i = 1} ^ {N} Q _ {i} ^ {d} \Big ] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\Gamma_ {i} ^ {d}}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) d t \\ & & = (r - c) \Big [ \sum_ {i = 1} ^ {N} a _ {i} + \sum_ {i = 1} ^ {N} b _ {i} s _ {0} - \frac {1}{\mathrm{T} ^ {d}} t _ {d} \Big ] - \frac {r}{\mathrm{T} ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) d t \\ & & E \Pi^ {m i} = E _ {p} \Bigg \{(r - c) E \Big [ \sum_ {i = 1} ^ {N} Q _ {i} ^ {m i} | p \Big ] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\Gamma_ {i} ^ {m i}}} \int_ {- \infty} ^ {- t _ {m i}} \Phi (t) d t \Bigg \} \\ & & = (r - c) \Big [ \sum_ {i = 1} ^ {N} a _ {i} + \sum_ {i = 1} ^ {N} b _ {i} s _ {0} - \frac {1}{\mathrm{T} ^ {m i}} E t _ {m i} \Big ] - E \Big [ \frac {r}{\mathrm{T} ^ {m i}} \int_ {- \infty} ^ {- t _ {m i}} \Phi (t) d t \Big ] \\ & & E \Pi^ {a} = E _ {\{s _ {1}, s _ {2}, \dots , s _ {N} \}} \Bigg \{(r - c) E \Big [ \sum_ {i = 1} ^ {N} Q _ {i} ^ {a} | (s _ {1}, s _ {2}, \dots , s _ {N}) \Big ] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\Gamma_ {i} ^ {a}}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) d t \Bigg \} \\ & & = (r - c) \Big [ \sum_ {i = 1} ^ {N} a _ {i} + \sum_ {i = 1} ^ {N} b _ {i} s _ {0} - \frac {1}{\mathrm{T} ^ {a}} t _ {a} \Big ] - E _ {\{s _ {1}, s _ {2}, \dots , s _ {N} \}} \Big [ \frac {r}{\mathrm{T} ^ {a}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) d t \Big ] \end{array}
$$

where $\begin{array} { r } { \frac { 1 } { \mathrm { T } ^ { j } } = \sum _ { i = 1 } ^ { N } \frac { 1 } { \sqrt { \Gamma _ { i } ^ { j } } } } \end{array}$ , for $j = a , d , m i$ . Therefore,

$$
E \left[ \Pi^ {m i} - \Pi^ {d} \right] = (r - c) \left(\frac {t _ {d}}{\mathrm{T} ^ {d}} - \frac {E t _ {m i}}{\mathrm{T} ^ {m i}}\right) + \frac {r}{\mathrm{T} ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) d t - E _ {\rho} \left[ \frac {r}{\mathrm{T} ^ {m i}} \int_ {- \infty} ^ {- t _ {m i}} \Phi (t) d t \right]
$$

$$
E \big [ \Pi^ {a} - \Pi^ {d} \big ] = (r - c) \Big (\frac {t _ {d}}{\mathrm{T} ^ {d}} - \frac {E t _ {a}}{\mathrm{T} ^ {a}} \Big) + \frac {r}{\mathrm{T} ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) d t - E _ {\{s _ {1}, s _ {2}, \dots , s _ {N} \}} \left[ \frac {r}{\mathrm{T} ^ {a}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) d t \right]
$$

Further manipulation of the terms in $E [ \Pi ^ { a } - \Pi ^ { d } ]$ and $E \big [ \Pi ^ { m i } - \Pi ^ { d } \big ]$ we can show that and $E \Pi ^ { a } > E \Pi ^ { d }$ and $E \Pi ^ { m i } > E \Pi ^ { d }$ under mild regularity condition min $\left( w ^ { m i } , w ^ { d } \right) > \frac { r } { 2 } > c$ . Further discussion on the condition and complete proofs on the supply chain efficiency property can be found in Guo et al. (2006).

Finally, $\operatorname* { l i m } _ { M  \infty } E _ { \omega } \bar { X } _ { i } ^ { m i } = \operatorname* { l i m } _ { N  \infty } \bar { X } _ { i } ^ { a }$ , and $\operatorname* { l i m } _ { M \to \infty } \Gamma _ { i } ^ { m i } = \operatorname* { l i m } _ { N \to \infty } \Gamma _ { i } ^ { a }$ . The same forecasts yield the same expected supply chain profits. This concludes the proof of Proposition 6.

Proof of Proposition 5:

$$
\mathsf {v a r} \left(Q _ {i} ^ {d}\right) = b _ {i} ^ {2} \mathsf {v a r} \left(\overline {{X}} _ {i} ^ {d}\right) = \frac {b _ {i} ^ {2} \tau_ {\delta} ^ {2}}{\left(\tau_ {0} + \tau_ {\delta}\right) ^ {2}} \mathsf {v a r} \left(\mathsf {s} _ {i}\right) = \frac {b _ {i} ^ {2} \tau_ {\delta} ^ {2}}{\left(\tau_ {0} + \tau_ {\delta}\right) ^ {2}} \left(\frac {1}{\tau_ {0}} + \frac {1}{\tau_ {\delta}}\right) = \frac {b _ {i} ^ {2} \tau_ {\delta}}{\tau_ {0} \left(\tau_ {0} + \tau_ {\delta}\right)}
$$

$$
\mathsf {v a r} \left(Q _ {i} ^ {m i} \mid p\right) = b _ {i} ^ {2} \mathsf {v a r} \left(\overline {{X}} _ {i} ^ {m i} \mid p\right) = b _ {i} ^ {2} \left[ \frac {\tau_ {\delta} - (M - 1) \tau_ {p}}{\tau_ {0} + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {p}} \right] ^ {2} \left(\frac {1}{\tau_ {0}} + \frac {1}{\tau_ {\delta}}\right)
$$

where $\begin{array} { r } { \tau _ { p } \triangleq \left( \frac { M } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { \omega } } \right) ^ { - 1 } } \end{array}$ , L is a constant market parameter (Guo et al., 2006).

Comparing equations yields var $\left( Q _ { i } ^ { d } \right) \geq \mathsf { v a r } \left( Q _ { i } ^ { m i } \mid p \right)$ with equality holds when $M { = } 1$ . So var $\left( Q _ { i } ^ { d } \right) \geq \mathsf { v a r } \left( Q _ { i } ^ { m i } \mid p \right)$ when $M \geq 2$ . Proof of the asymptotic property requires substitution of related market parameters. We omit its proof here.

## Proof of Proposition 7:

Given the reward function $f \left( r _ { i } , B _ { i } , X \right) = 2 B _ { i } ^ { \frac { 1 } { 2 } } \left( 1 - \left( r _ { i } - x \right) ^ { 2 } \right)$ , an agent maximizes expected payoff by choosing the optimal report and bet $\left( r _ { i } , { \cal B } _ { i } \right)$

$$
\max _ {r _ {i}, B _ {i}} E \left[ f \left(r _ {i}, B _ {i}, X\right) - B _ {i} \mid \left(s _ {i}, \tau_ {i}\right) \right].
$$

The expected payoff is expressed as:

$$
\begin{array}{r l} & E [ f (r _ {i}, B _ {i}, X) - B _ {i} | (\mathsf {s} _ {i}, \tau_ {i}) ] = 2 B _ {i} ^ {\frac {1}{2}} \frac {1}{\tau_ {0}} - B _ {i} - 2 B _ {i} ^ {\frac {1}{2}} E [ (r _ {i} - X) ^ {2} | (\mathsf {s} _ {i}, \tau_ {i}) ] \\ & \qquad = 2 B _ {i} ^ {\frac {1}{2}} \frac {1}{\tau_ {0}} - B _ {i} - 2 B _ {i} ^ {\frac {1}{2}} [ r _ {i} - E [ X | (\mathsf {s} _ {i}, \tau_ {i}) ] ] ^ {2} - 2 B _ {i} ^ {\frac {1}{2}} \operatorname{var} [ X | (\mathsf {s} _ {i}, \tau_ {i}) ] \\ & \qquad \leq 2 B _ {i} ^ {\frac {1}{2}} \frac {1}{\tau_ {0}} - B _ {i} - 2 B _ {i} ^ {\frac {1}{2}} \operatorname{var} [ X | (\mathsf {s} _ {i}, \tau_ {i}) ] \\ & \qquad = 2 B _ {i} ^ {\frac {1}{2}} \frac {1}{\tau_ {0}} - B _ {i} - 2 \frac {B _ {i} ^ {\frac {1}{2}}}{\tau_ {0} + \tau_ {i}} \end{array}
$$

with the maximum obtained when $\begin{array} { r } { r _ { i } ^ { * } = E [ X | ( s _ { i } , \tau _ { i } ) ] = \frac { \tau _ { 0 } s _ { 0 } + \tau _ { i } s _ { i } } { \tau _ { 0 } + \tau _ { i } } } \end{array}$ . To determine the optimal bet, simply taking first order derivative on $B _ { i } ^ { \frac { 1 } { 2 } }$ of the above equation and solve for $B _ { i }$ , we obtain $\begin{array} { r } { B _ { i } ^ { ' } = \frac { \tau _ { i } ^ { 2 } } { \tau _ { 0 } ^ { 2 } \left( \tau _ { 0 } + \tau _ { i } \right) ^ { 2 } } } \end{array}$

## Proof of Proposition 8:

Solving equations in Proposition 7 for $\left( s _ { i } , \tau _ { i } \right)$ we have the results immediately.

## C. Notation Table

<table><tr><td colspan="2">Table 1: Mathematic Notations</td></tr><tr><td colspan="2"></td></tr><tr><td>i=0,1,2,...,N</td><td>Index of the manufacturer (i=0) and the retailers (i=1,2,...,N)</td></tr><tr><td>j=a,d,mi,mb</td><td>Index of different supply chain coordination scenarios. a = aggregated forecast sharing scenario; d = decentralized forecasting scenario; m = market coordination scenario (mi denotes index market; mb denotes betting market).</td></tr><tr><td>Di</td><td>Retailer i&#x27;s local market demand</td></tr><tr><td>εi</td><td>Idiosyncratic demand risk associated with retailer i</td></tr><tr><td> $\frac{1}{\tau_{\varepsilon}}$ </td><td>Variance of the local idiosyncratic demand risk</td></tr><tr><td>ai, bi</td><td>Retailer-specific parameters in the demand function</td></tr><tr><td>X</td><td>The macro-economic factor that drives the retailers&#x27; underlying demand</td></tr><tr><td>S0</td><td>The expected value of X in the common prior belief</td></tr><tr><td>τ0</td><td>The precision of the prior knowledge about X</td></tr><tr><td>Si</td><td>Retailer i&#x27;s private forecast of X</td></tr><tr><td>δi</td><td>Retailer i&#x27;s forecast error of X</td></tr><tr><td>τi</td><td>Precision of retailer i&#x27;s private forecast (reciprocal of var(δi))</td></tr><tr><td> $\overline{X}_{i}^{0}$ </td><td>Mean of retailer i&#x27;s prior demand distribution</td></tr><tr><td> $\frac{1}{\Gamma_{j}^{0}}$ </td><td>Variance of retailer i&#x27;s prior demand distribution</td></tr><tr><td> $\overline{X}_{i}^{j}$ </td><td>Retailer i&#x27;s forecast mean of the demand distribution under scenario j</td></tr><tr><td> $\frac{1}{\Gamma_{i}^{j}}$ </td><td>Retailer i&#x27;s forecast variance of the demand distribution under scenario j</td></tr><tr><td>wj</td><td>The wholesale price charged by the manufacturer in scenario j.</td></tr><tr><td>r</td><td>Retail price charged by all retailers</td></tr><tr><td>c</td><td>Unit production cost for the manufacturer</td></tr><tr><td>Fij</td><td>The information set available to supply chain member i in scenario j.</td></tr><tr><td>Qij</td><td>Retailer i&#x27;s order quantity to the manufacturer in scenario j.</td></tr><tr><td>oi</td><td>Informed trader i&#x27;s order in the index market.</td></tr><tr><td>ω</td><td>Aggregate random net order submitted by uninformed noisy traders.</td></tr><tr><td> $\frac{1}{\tau_{\omega}}$ </td><td>Variance of the aggregate random net order from uninformed traders.</td></tr><tr><td>L</td><td>Market liquidity measure</td></tr><tr><td>p</td><td>Equilibrium market price of the retail index.</td></tr><tr><td>PI</td><td>Price informativeness measure</td></tr><tr><td>EIIj</td><td>The expected overall supply chain profit in scenario j.</td></tr><tr><td>EIIj</td><td>The expected supply chain member i&#x27;s profit in scenario j.</td></tr><tr><td>ri</td><td>Report by retailer i on the future value of X.</td></tr><tr><td>Bi</td><td>Bet placed by retailer i on her report.</td></tr><tr><td>f(ri,Bi,X)</td><td>The reward function in the betting market.</td></tr><tr><td>N</td><td>Total number of retailers.</td></tr><tr><td>N0</td><td>Total number of outside informed traders.</td></tr><tr><td>M</td><td>Total number of informed traders in the index market. M=N+N0.</td></tr></table>

## About the Authors

Fang Fang is an Assistant Professor in the College of Business Administration at California State University at San Marcos. Her research interests include knowledge markets, business predictions, information economics, and supply chain coordination. She has a Ph.D. in Management Information Systems from the University of Texas at Austin.

Zhiling Guo is an Assistant Professor of Information Systems at UMBC (University of Maryland, Baltimore County). Her research interests include electronic commerce, financial markets, information economics, and supply chain management. She has a Ph.D. in Management Information Systems from the University of Texas at Austin.

Andrew B. Whinston is a Professor of Information Systems, Economics, Computer Science, and Library and Information Sciences, Hugh Roy Cullen Centennial Chair in Business Administration, and director of the Center for Research in Electronic Commerce at the University of Texas, Austin. He has published more than 300 papers in top-rated scientific journals including Management Science, Information Systems Research, MIS Quarterly, Journal of Economic Theory, Marketing Science, Journal of Marketing, among others.

Copyright © 2008, by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers for commercial use, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via e-mail from ais@gsu.edu.

ISSN: 1536-9323

Editor Kalle Lyytinen Case Western Reserve University, USA

<table><tr><td colspan="4">Senior Editors</td></tr><tr><td>Izak Benbasat</td><td>University of British Columbia, Canada</td><td>Robert Fichman</td><td>Boston College, USA</td></tr><tr><td>Varun Grover</td><td>Clemson University, USA</td><td>Rudy Hirschheim</td><td>Louisiana State University, USA</td></tr><tr><td>Juhani livari</td><td>University of Oulu, Finland</td><td>Robert Kauffman</td><td>University of Minnesota, USA</td></tr><tr><td>Frank Land</td><td>London School of Economics, UK</td><td>Jeffrey Parsons</td><td>Memorial University of Newfoundland, Canada</td></tr><tr><td>Suzanne Rivard</td><td>Ecole des Hautes Etudes Commerciales, Canada</td><td>Bernard C.Y. Tan</td><td>National University of Singapore, Singapore</td></tr><tr><td>Yair Wand</td><td>University of British Columbia, Canada</td><td></td><td></td></tr><tr><td colspan="4">Editorial Board</td></tr><tr><td>Steve Alter</td><td>University of San Francisco, USA</td><td>Michael Barrett</td><td>University of Cambridge, UK</td></tr><tr><td>Cynthia Beath</td><td>University of Texas at Austin, USA</td><td>Anandhi S. Bharadwaj</td><td>Emory University, USA</td></tr><tr><td>Francois Bodart</td><td>University of Namur, Belgium</td><td>Marie-Claude Boudreau</td><td>University of Georgia, USA</td></tr><tr><td>Susan A. Brown</td><td>University of Arizona, USA</td><td>Tung Bui</td><td>University of Hawaii, USA</td></tr><tr><td>Dave Chatterjee</td><td>University of Georgia, USA</td><td>Patrick Y.K. Chau</td><td>University of Hong Kong, China</td></tr><tr><td>Wynne Chin</td><td>University of Houston, USA</td><td>Ellen Christiaanse</td><td>University of Amsterdam, Nederland</td></tr><tr><td>Mary J. Culnan</td><td>Bentley College, USA</td><td>Jan Damsgaard</td><td>Copenhagen Business School, Denmark</td></tr><tr><td>Samer Faraj</td><td>University of Maryland, College Park, USA</td><td>Chris Forman</td><td>Carnegie Mellon University, USA</td></tr><tr><td>Guy G. Gable</td><td>Queensland University of Technology, Australia</td><td>Dennis Galletta</td><td>University of Pittsburg, USA</td></tr><tr><td>Hitotora Higashikuni</td><td>Tokyo University of Science, Japan</td><td>Kai Lung Hui</td><td>National University of Singapore, Singapore</td></tr><tr><td>Bill Kettinger</td><td>University of South Carolina, USA</td><td>Rajiv Kohli</td><td>College of William and Mary, USA</td></tr><tr><td>Chidambaram Laku</td><td>University of Oklahoma, USA</td><td>Ho Geun Lee</td><td>Yonsei University, Korea</td></tr><tr><td>Jae-Nam Lee</td><td>Korea University</td><td>Kai H. Lim</td><td>City University of Hong Kong, Hong Kong</td></tr><tr><td>Mats Lundeberg</td><td>Stockholm School of Economics, Sweden</td><td>Ann Majchrzak</td><td>University of Southern California, USA</td></tr><tr><td>Ji-Ye Mao</td><td>Remnin University, China</td><td>Anne Massey</td><td>Indiana University, USA</td></tr><tr><td>Emmanuel Monod</td><td>Dauphine University, France</td><td>Eric Monteiro</td><td>Norwegian University of Science and Technology, Norway</td></tr><tr><td>Mike Newman</td><td>University of Manchester, UK</td><td>Jonathan Palmer</td><td>College of William and Mary, USA</td></tr><tr><td>Paul Palou</td><td>University of California, Riverside, USA</td><td>Yves Pigneur</td><td>HEC, Lausanne, Switzerland</td></tr><tr><td>Dewan Rajiv</td><td>University of Rochester, USA</td><td>Sudha Ram</td><td>University of Arizona, USA</td></tr><tr><td>Balasubramaniam Ramesh</td><td>Georgia State University, USA</td><td>Timo Saarinen</td><td>Helsinki School of Economics, Finland</td></tr><tr><td>Rajiv Sabherwal</td><td>University of Missouri, St. Louis, USA</td><td>Raghu Santanam</td><td>Arizona State University, USA</td></tr><tr><td>Susan Scott</td><td>The London School of Economics and Political Science, UK</td><td>Olivia Sheng</td><td>University of Utah, USA</td></tr><tr><td>Carsten Sorensen</td><td>The London School of Economics and Political Science, UK</td><td>Ananth Srinivasan</td><td>University of Auckland, New Zealand</td></tr><tr><td>Katherine Stewart</td><td>University of Maryland, USA</td><td>Mani Subramani</td><td>University of Minnesota, USA</td></tr><tr><td>Dov Te&#x27;eni</td><td>Tel Aviv University, Israel</td><td>Viswanath Venkatesh</td><td>University of Arkansas, USA</td></tr><tr><td>Richard T. Watson</td><td>University of Georgia, USA</td><td>Bruce Weber</td><td>London Business School, UK</td></tr><tr><td>Richard Welke</td><td>Georgia State University, USA</td><td>George Westerman</td><td>Massachusetts Institute of Technology, USA</td></tr><tr><td>Youngjin Yoo</td><td>Temple University, USA</td><td>Kevin Zhu</td><td>University of California at Irvine, USA</td></tr><tr><td colspan="4">Administrator</td></tr><tr><td>J. Peter Tinsley</td><td>AIS, Executive Director</td><td colspan="2">Association for Information Systems, USA</td></tr><tr><td>Reagan Ramsower</td><td>Publisher</td><td colspan="2">Baylor University</td></tr></table>
