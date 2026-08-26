---
otero_id: 7030
otero_key: "NTMEAXKZ"
title: "Supply chain information sharing in a macro prediction market"
authors: "Zhiling Guo; Fang Fang; Andrew B. Whinston"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.05.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Supply chain information sharing in a macro prediction market

Zhiling Guo <sup>a,⁎</sup>, Fang Fang <sup>b</sup>, Andrew B. Whinston <sup>c</sup>

<sup>a</sup> Department of Information Systems, UMBC (University of Maryland, Baltimore County), Baltimore, MD 21250, USA <sup>b</sup> Department of High Tech Management, College of Business Administration, Cal State Univ — San Marcos, San Marcos, CA 92096, USA <sup>c</sup> Department of Information, Risk, and Operations Management, McCombs School of Business, The University of Texas at Austin, Austin, TX 78712, USA

Received 4 April 2006; accepted 10 May 2006 Available online 17 July 2006

## Abstract

This paper aims to address supply chain partners' incentives for information sharing from an information systems design perspective. Specifically, we consider a supply chain characterized by N geographically distributed retailers who order a homogeneous product from one manufacturer. Each retailer's demand risk consists of two parts: a systematic risk part that affects all retailers and an idiosyncratic risk part that only has a local effect. We propose a macro prediction market to effectively elicit and aggregate useful information about systematic demand risk. We show that such information can be used to achieve accurate demand forecast sharing and better channel coordination in the supply chain system. Our market-based framework extends the range of information sharing beyond the supply chain system. It also opens the door for other corporate risk management opportunities to hedge against aggregate economic risk. © 2006 Elsevier B.V. All rights reserved

Keywords: Supply chain; Information sharing; Macro prediction market; Rational expectations equilibrium

## 1. Introduction

Information asymmetry is a main source of systems inefficiency in many areas. For example, the well-known bullwhip effect [22,31] refers to the information distortion that is caused by misaligned incentives to share private demand information truthfully among self-interested supply chain partners, resulting in direct deadweight losses in social welfare. Truthful information sharing has been proposed as a solution to the bullwhip effect. Over the past few years, new business initiatives enabled by emerging technologies such as Electronic Data Interchange (EDI), Radio Frequency Identification (RFID), and XML-streamlined workflow management have facilitated information sharing in decentralized business environments. However, a technologically effective system does not necessarily result in improved decision quality unless it is economically efficient as well. Systems could still be inefficient if users only strategically report information for their own benefit. We seek to investigate the incentive issues for supply chain information sharing. In particular, we propose a marketbased framework to understand how conflicting incentives can be aligned and useful information can be elicited in the new supply chain information systems design so that a broad scope of benefits can be achieved.

In this paper, we consider a simple two-echelon supply chain characterized by N geographically distributed retailers who order a homogeneous product from one manufacturer. Each retailer serves her own consumer market whose demand uncertainty can be expressed as the sum of two random elements — a macro risk factor and an idiosyncratic risk factor. The macro factor represents the systematic risks caused by uncertain macroeconomic events that affect all retailers, such as an economic downturn. The idiosyncratic factor represents local market risks unique to individual retailers, such as the effect of weather on their local markets. Before a selling season each retailer receives a noisy signal about the macro risk and order inventory from the manufacturer based on the information available to her. The manufacturer, who has no consumer demand information, is interested in forecasting expected aggregate orders from all retailers. The retailers, who bear the uncertainty of the consumer markets, are interested in effectively forecasting future demand. Our goal is to design a new supply chain information system that aligns different supply chain partners' self-interests and thus enables more effective information sharing and better decision-making. Some critical questions must be answered in pursuit of this goal: What information could and should be shared? How do we effectively share this information?

In answer to the first question, we argue that the new information system should focus on forecasting element at an appropriate aggregation level. A too broad forecasting goal may seem less relevant and a too narrow forecasting goal may not attract sufficient attention, leading to a less effective prediction. In this supply chain context, we should focus on the macro factor that will affect all the retailers instead of extracting individual retailers' overall forecasts. There are several reasons. First, the manufacturer is most interested in the macro factor forecast since the idiosyncratic risks are independent. The total idiosyncratic effects from all the retailers can be cancelled out by the Law of Large Numbers. Second, individual retailers are not interested in sharing their idiosyncratic factor forecasts because they have the best knowledge and are not concerned with the local risk of others. They are, however, interested in macro factor forecast because it affects the forecast accuracy of their own demand. This common interest among all supply chain partners can guarantee market liquidity and ensure that no individual's private interests can significantly mislead the aggregate opinion. Manipulation of information can be potentially reduced. Therefore, a market designed to forecast the macro factor (i.e., a macro prediction market) is a viable candidate mechanism to elicit and share dispersed information.

As to the mechanism for effective information sharing, using a prediction market to elicit information is an emerging research field. A prototype example is the Iowa Electronic Market (IEM: http://www.biz.uiowa.edu/iem/)

that predicts presidential election outcomes. Other examples include the Hollywood Stock Exchange Market (http://www.hsx.com), primarily used to predict entertainment events such as movie sales, and Goldman Sachs Economic Derivatives Market (http://www.gs.com/econderivs/), in which likely outcomes of future economic data releases (such as retail sales or industry production) are traded. In our context, the macro prediction market is designed as a real money futures market, in which a retail index with a payoff dependent on the future realization of the macro factor is traded.

The macro prediction market has many benefits. First, the market offers a good mechanism to effectively combine beliefs in producing a reliable forecast. Market participants with heterogeneous beliefs express their opinions about the retail index through their trading behaviors. Since traders who make better predictions can expect higher payoffs, the prediction market can effectively attract whoever have good information and aggregate it. Second, the market aligns traders' incentives to trade because no individual is pivotal in influencing market price. Once the number of participants is large enough, one retailer's nonparticipation or misrepresentation of information decreases only that retailer's own profitability. It affects neither market price nor the accuracy of market prediction conveyed in the price. Therefore, the retailer's dominant strategy is to trade according to true information. Third, the market is an open system that absorbs useful information from sources outside the supply chain system. Speculators, liquidity traders and others can participate as long as they believe they have relevant information. This increases market liquidity and improves forecast effectiveness as the number of market participants increases. Finally, using futures markets in macro variables affecting the economy to hedge currently unhedgeable risks is a market innovation advocated by Ref. [29]. Our idea of a macro prediction market opens the door for new opportunities in corporate risk management.

In this paper, we develop a model that shows that the information incorporated into the macro prediction market price is accurate enough to reduce the supply chain's total forecast uncertainty. The information also reduces the retailer's order variance, which can significantly alleviate the bullwhip effect. We demonstrate that demand forecast sharing and channel coordination can be collectively achieved in the macro prediction market-based supply chain information system. Expected supply chain efficiency is improved under market coordination.

To the best of our knowledge, this research is the first to incorporate a prediction market in a supply chain contractual context. Since our focus is the informational content of creating new market on supply chain efficiency, we limit our investigation of the contract format to the widely used price-only contract, i.e., the manufacturer sets a unit wholesale price and leaves the order quantity decisions to the retailers. Other complicated contract forms such as reorder/buy back contracts, non-linear pricing/quantity discount policy, and linear transfer payments are possible. We choose the simple contract form in order to generate and present some clean analytical insights.

This paper is organized as follows. We review related literature in Section 2. In Section 3, we present our base model under a supply chain information sharing framework. We analyze the manufacturer's and retailers' decision problems and discuss the construction of a macro prediction market. We further explore the value of information sharing and properties such as order variances and supply chain efficiency in Section 4. We extend the market's role of information aggregation to risk hedging in Section 5. We conclude in Section 6 with an agenda for future research.

## 2. Related literature

The value of information sharing has been widely studied in the supply chain literature (e.g., [8,9,24]). One solution to alleviate the bullwhip effect was centralizing demand information from supply chain partners [10]. However, information sharing across the supply chain is not easily achievable. In general, there is a conflict of incentives in supply chain systems; individuals manipulate information solely for their own benefit. An effective information system should be able to align incentives from users with conflicting objectives. Incentive alignment becomes an important third dimension (preceded by software engineering and user acceptance perspectives) for any sophisticated information systems design and evolution [2].

In this paper, following the finance literature, we represent retailers' demand uncertainty in two parts: systematic risk and idiosyncratic risk. Idiosyncratic risk sharing has attracted considerable attention in the supply chain field. For example, Risk pooling in inventory and allocation decisions by retailers facing local stochastic demands was considered in Ref. [1]. The impact of a secondary market was examined by Ref. [23] where retailers (“resellers” in their paper) can trade their excess inventories associated with independent demand risks among each other. Since systematic risk cannot be reduced by risk pooling, it was suggested to use macro economy related market instruments to hedge certain aggregate economic risks [29]. This paper complements previous work by investigating the role of information aggregation in dealing with systematic risk.

Economic theory has long recognized that a properly designed market efficiently collects and disseminates information [16]. New market efficiency research suggests that information markets can effectively aggregate information and produce advance forecasts of uncertain outcomes. An information market is primarily designed for the purpose of eliciting a particular piece of information. It is an emerging form of financial markets in which the settling contracts are futures contracts. It is also called “ideas futures”, “event futures”, “Internet-based virtual stock market”, etc. A survey on research in information markets was given by Ref. [34]. It was further suggested that information market-based forecast could be used for effective decision support [4]. Empirical study also showed evidence that Internet-based virtual stock market forecasts outperform alternative methods such as surveys and opinion polls [30]. It was proposed that organizing Internet-based interactions to better gather predictive information. We complement previous work by theoretically justifying the reliability of the market prediction mechanism. Moreover, we integrate the prediction function into the decision support and theoretically validate both market performance and efficiency improvement in the supply chain application.

Rational Expectations Equilibrium (REE; see e.g. Refs. [26,14]) is the theoretical support for the information revelation and aggregation in market transactions. The key to the REE concept is that the act of trading conveys information. The learning in the market is solved via an application of Bayesian rule [27]. This research shows how the market can provide an incentive to effectively aggregate and reveal private information and how market price is a sufficient statistic for predicting the demand macro factor. The concept of REE has been applied to supply chains to study the informational role of an industrial exchange (see Refs. [25,33]). Previous work viewed spot market trading as an opportunity to readjust inventory positions and share information about demand uncertainty. In contrast, we propose a futures market trading a financial index whose future payoff depends on realization of the macro factor. In our futures market, demand uncertainty information can be revealed early and incorporated into the supply chain partners' decision making. Our market has two other important advantages. First, the trading information indices rather than the physical commodities can reduce transaction costs and so improve market liquidity. Second, our prediction market allows outside traders to present their relevant knowledge, extending the range of information sharing.

Our modeling framework is distinct from all previous work in information economics. By dividing demand uncertainty into a systematic macro factor and an idiosyncratic local factor, we propose trading a retail index representing systematic risk in the supply chain in a macro prediction market, which has strong resemblance to a financial market. This idea is consistent with the findings that a firm's demand has a strong correlation with some financial index [13]. A number of details about the construction of new markets and a variety of new products to deal with macro economic uncertainty from a risk hedging perspective were provided by Ref. [29]. In contrast, we focus on the informational role of markets and extend its function to risk hedging in the supply chain information system.

We study a supply chain in the framework of newsvendor problem. The traditional newsvendor model only takes into account a single decision maker's order quantity decision when facing exogenous demand distribution [18]. Strategic interactions between a manufacturer and a retailer were studied by Ref. [21]. Their model allowed the manufacturer to change the wholesale price and the uncertain demand distribution can be updated through forecasting. We extend the demand forecast to multiple retailers in a market framework. In terms of market setup, our model is comparable with the work in Refs. [19] and [20] in which the information was revealed through the trading of a financial asset. As to the market structure, we both assume that orders are batched together to transact at a single regret-free, market-clearing price.

## 3. The model

Consider N geographically distributed retailers who order a homogeneous product from a manufacturer. Each retailer faces uncertain market demand, composed of systematic risks that affect all the markets and idiosyncratic risks that affect only the local market. We express the retailer $i \mathrm { { ^ { \circ } s } }$ demand as $D _ { i } { = } a _ { i } { + } b _ { i } \theta { + } \varepsilon _ { i } , i { = } 1 , . . . , N ,$ where $\theta ^ { \sim } N \left( \mu , \frac { 1 } { \tau } \right) ^ { 1 }$ is a systematic macro economic factor and $\mathrm { { \varepsilon } } _ { i } \sim N ( 0 , \frac { 1 } { \tau _ { c } } )$ is an $i . i . d .$ idiosyncratic random factor. We assume that $a _ { i }$ and $b _ { i }$ are known constants that could differ among different retailers but these are common knowledge in the supply chain.

We assume that each retailer can privately derive a forecast (or obtain a private signal) $\tilde { \theta } _ { i }$ for the macro economic factor θ. Denote $\tilde { \theta } _ { i } { = } \theta + \delta _ { i } ,$ where $\begin{array} { r } { \delta _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { \delta } } \right) } \end{array}$ is also $i . i . d .$ , indicating the forecast error. We also assume that $\tau _ { \delta } > \tau$ . This condition implies that the forecast is informative because the forecast variance is less than the variance of the prior distribution of the macro factor.

Suppose the private information from individual retailers can be aggregated and define the aggregate signal as $\overline { { \theta } } \equiv \frac { 1 } { N } \sum _ { i = 1 } ^ { N } \ \tilde { \theta } _ { i } = \theta + \frac { 1 } { N } \sum _ { { \scriptscriptstyle i } = 1 } ^ { N } \ \delta _ { i } ,$ , which is a sufficient statistic <sup>i¼1</sup>for the full information reflected in a set of signal realizations $( \widetilde { \theta } _ { 1 } , \widetilde { \theta } _ { 2 } , . . . , \widetilde { \theta } _ { N } ) . \ : \overline { { { \theta } } }$ is the best predictor compared with any individual forecast since it has the same mean but the least variance. We call this case truthful forecast sharing. Corresponding to this scenario is the aggregate information supply chain structure (Structure A). This provides us with a full information benchmark solution to which we compare two other supply chain structures: a fully decentralized one (Structure D) and a macro prediction market-coordinated one (Structure M).

The supply chain partners' decision problems are the same under all three supply chain structures. The manufacturer sets a wholesale price to maximize the expected profit based on the expected aggregate retailer order quantity. Given the manufacturer's wholesale price, each retailer decides on an optimal order quantity based on her demand distribution forecast. The only difference among the three structures is the information incorporated in forecasting the demand distribution. In the truthful forecast sharing scenario (Structure $\mathrm { A } ) _ { \cdot }$ , the manufacturer has access to all the information. In the fully decentralized scenario (Structure D), the manufacturer cannot observe any of the retailers' forecasts. From a social welfare perspective, full information sharing will generate higher expected supply chain profits. However, because higher individual retailer's profit is not guaranteed, it is not clear if a retailer will want to truthfully share information. To achieve the goal of information sharing, we design a macro prediction market-coordinated supply chain structure (Structure M) to trade a retail index. The retail index is an aggregate economic measure for the macro factor θ. For simplicity, we assume that the retail index payoff is exactly θ, depending on the future realized value of the macro factor. The index market price is a public signal that the manufacturer and retailers use to update their beliefs about demand distribution. We call this market-based forecast sharing. In this case, each retailer can gather information from a public signal and a private one. The retailer decides how much to rely on the public signal based on its precision. We will compare the supply chain performance under the two types of forecast sharing (Structures A and M). In addition, we characterize conditions under which the market-based forecast sharing will outperform the full information benchmark thus additional benefits can be generated in the supply chain.

In the following, we present a macro prediction market model and characterize its equilibrium and properties under the REE framework. We then use backward induction to solve the supply chain decision making problems under Structures A, D, and M. First, we derive the individual retailer's order decision in the supply chain as a best response function to the manufacturer's wholesale price. Then we solve the manufacturer's optimal pricing problem according to the expected aggregate orders from the retailers. We also characterize how the level of information sharing affects the supply chain partners' decision making.

## 3.1. The macro prediction market

The construction of the macro prediction market is an important market mechanism design issue that evokes various discussions. For our purposes, the trading asset is a futures contract based on a retail index $\theta ,$ whose payoff depends on the future likely outcome of macro economic events such as retail sales. For simplicity, we assume that one share of the retail index will pay out monetary units ${ \boldsymbol { \theta . } } ^ { 2 }$ The current price of the futures contract is denoted by $p .$

We assume that the macro prediction market operates like an open book call futures market (see [12] for a reference). The market opens at a pre-specified time, before which traders can update their orders according to their new information. Trades take place at an equilibrium price reflecting traders' regret-free trading decisions. For the sake of liquidity, we assume that only the risky asset $\theta$ is traded at the initial running of the market. Aggregate market information is revealed after the settlement for transaction of θ. At this point, nobody has an informational advantage to arbitrage the market. The market is complete and efficient under the REE. Once the index price is set, the index-based derivatives can be properly priced, and various index-based derivatives can be traded. Therefore, our macro prediction market allows for derivatives trading which can be used for risk hedging purpose (we will discuss this in Section 5). In the following, we derive the market equilibrium where only one risky asset, $\theta ,$ is traded.

The way of designing an effective pricing mechanism is not unique. In this paper, we focus on a market structure where the market maker responds to the aggregate net order by taking an opposite position. We assume that the market maker doesn't have any private information. Thus, to prevent economic loss, the market maker sets the index price as the expected value of the future payoff given the current aggregate net orders in the market.

We assume that there are M risk neutral informed traders in the market. $\scriptstyle M = N + N _ { 0 } ,$ where N is the number of retailers and $N _ { 0 }$ is the number of outside traders who have relevant information. We don't distinguish among informed traders' forecast abilities, but this simplification will not affect our results. We assume that each informed trader i obtains a private signal $\widetilde { \theta } _ { i } { = } \theta { + } \delta _ { i }$ , where $\begin{array} { r } { \delta _ { i } \sim N \left( 0 , \frac { 1 } { \tau _ { \delta } } \right) } \end{array}$ , and places an order $\pi _ { i }$ for $i { = } 1 , . . . , M . ^ { 3 }$ There are also some uninformed traders (also known as noise traders) whose aggregate net order is random and exogenously given, i.e $\scriptstyle { \tilde { X } } \sim { \bar { N } } \left( 0 , { \frac { 1 } { \tau _ { X } } } \right)$ Note that the noise traders' assumption incorporates all the unpredictable elements which may come from agents random liquidation demands or irrational behaviors. The random supply provided by noise traders is crucial in providing the informed traders with proper incentives to participate in the market. Informed retailers will earn positive expected profits at the expense of the noise traders' expected losses in equilibrium.

The informed trader i takes the price information into account and strategically orders $\pi _ { i }$ to maximize her expected return from the macro prediction market.

$$
\max _ {\pi_ {i}} E [ (\theta - p (y)) \pi_ {i} | \tilde {\theta} _ {i}, p ]\tag{I}
$$

A REE equilibrium is defined by two components. First, a trading strategy $\pi _ { i } ,$ for $i { = } 1 , { \ldots } , M ,$ that solves the above maximization problem given pricing function $p$ (y). Second, a pricing function $p ( \boldsymbol { y } )$ such that given the trading strategy $\pi _ { i } , i { = } 1 , . . . , M ,$ we have

$$
p (y) = E \left[ \theta | y = \sum_ {i = 1} ^ {M} \pi_ {i} + \tilde {X} \right]\tag{II}
$$

where $\begin{array} { r } { y = \sum _ { i = 1 } ^ { M } \pi _ { i } + \tilde { X } } \end{array}$ is the aggregate demand. The following propositions characterize the market equilibrium properties.

Proposition 1. For any given number of informed traders M, there exists a unique linear REE in which

1) An informed trader i adopts a linear trading strategy $\pi _ { i } = \beta _ { 0 } + \beta _ { I } \tilde { \theta } _ { i } + \beta _ { 2 } p$ , where $\beta _ { O } , \beta _ { I } ,$ , and $\beta _ { 2 }$ are constants; 2) The equilibrium market price $\begin{array} { r } { p = A _ { 0 } + A _ { 1 } \left( \sum _ { i = 1 } ^ { M } \tilde { \theta } _ { i } + \frac { \dot { X } } { L } \right) } \end{array}$ where $A _ { O } , A _ { I } ,$ and L are constants.

From Proposition 1, we can see that the symmetric linear trading strategy is revealing since an informed trader's private information $\tilde { \theta _ { i } }$ is indirectly transformed into the trader's market trading volume $\pi _ { i }$ based on any observed market price $p .$ In turn, observing the index price $p$ is equivalent to observing the signal $\left( \sum _ { i = 1 } ^ { M } \tilde { \theta } _ { i } + \frac { \tilde { X } } { L } \right)$ , which is an indicator of the available aggregate market information. It's worth mentioning that under the notion of REE, traders strategically reveal and manipulate their private information, although such behavior proves to be self-revealing.

The existence of linear REE guarantees that $p$ is also normally distributed. This fact allows us to characterize the supply chain partners' belief updates using the Normal Learning Theorem (actually a standard Bayesian update formula for normal distribution used in financial market trading, see Ref. [27]). The uniqueness of the linear REE guarantees one-to-one mapping from the dispersed market signals to the aggregate market price. $L ,$ which often represents market liquidity in the REE literature, reflects the precision of the information transformation. The larger the value of $L ,$ the less the influence of ${ \tilde { X } } .$ . Therefore, $p$ is a more precise indicator of the useful signals.

The accuracy of aggregate forecasts revealed by the market price can be increased when the number of informed traders increases. We define price informativeness as $\mathrm { P I } { = } \frac { 1 } { \mathrm { V a r } [ \theta | p ] } .$ . The uncertainty on $\theta$ should be reduced based on a good prediction $p .$ In other words, the less variation of $\theta$ conditional on $p ,$ the more informative the index price $p$ is. We use the reciprocal to capture this relationship in the definition.

Proposition 2. Price informativeness PI increases in M. lim $1 _ { M } {  } _ { \infty } \mathrm { P I } = \infty$ and $\operatorname* { l i m } _ { M \to \infty } p = \theta .$

Price precision is a function of the number of informed traders. Proposition 2 implies that when the number of informed traders approaches infinity, the information revealed in the macro prediction market will be accurate enough so that the index price converges to the true value of the macro factor.

It's worth noting that one retailer's macro prediction market order will have negligible effect on the information contained in the index price because the equilibrium price is determined by the sum of informed and uninformed traders' signals. No individual's order is pivotal. In the macro prediction market, retailers can increase profit by solely taking advantage of their superior private information. They do not profit by manipulating their trading orders hoping to mislead the manufacturer in her supply chain pricing decision. Therefore, retailers' macro prediction market decisions and physical supply chain order decisions are perfectly separable. In the following, we study the retailer's decision problem under different supply chain structures.

## 3.2. The retailer's decision problem

Suppose all retailers charge a fixed retail price $r$ in the consumer market. In this paper, we assume the retail price is exogenously given and cannot be influenced by either the retailer or the manufacturer. While strategic price determination either from the manufacturer or the retailers point of view is an interesting research topic, it is not our focus here. Introducing too much heterogeneity such as different prices in different markets or too much flexibility such as pricing decision in the consumer market will dramatically complicate our analysis without further incremental value in deriving our main insights.

In the following, we compare retailers' decision problems under three supply chain structures $\mathbf { A } ,$ D, and M. We use superscript $^ { a , }$ d and m to distinguish parameters in the three supply chain structures A, D, and M.

Given the wholesale price $s ^ { j } ,$ , for $\begin{array} { r } { j = a , d , m } \end{array}$ , the retailer chooses an order quantity $\mathcal { Q } _ { i } ^ { j } ,$ for ${ j = a , d , m }$ , to maximize the expected profit according to the different information at each setting. The retaile ${ \bf \ddot { s } }$ decision problem is (RA) (RD) and (RM).

$$
\max _ {Q _ {i} ^ {a} \geq 0} E \left[ r \min \left[ Q _ {i} ^ {a}, D _ {i} \right] - s ^ {a} Q _ {i} ^ {a} | \bar {\theta} \right]\tag{RA}
$$

$$
\max _ {Q _ {i} ^ {d} \geq 0} E \left[ r \min \left[ Q _ {i} ^ {d}, D _ {i} \right] - s ^ {d} Q _ {i} ^ {d} \mid \tilde {\theta} _ {i} \right]\tag{RD}
$$

$$
\max _ {Q _ {i} ^ {m} \geq 0} E \left[ r \min \left[ Q _ {i} ^ {m}, D _ {i} \right] - s ^ {m} Q _ {i} ^ {m} \mid \tilde {\theta} _ {i}, p \right]\tag{RM}
$$

where min $[ Q _ { i } ^ { j } , D _ { i } ]$ , for $_ { j } = a , d , m$ , is retailer $i \mathrm { \ ' } _ { \mathrm { S } }$ sale in the consumer market. These standard newsvendor problems have different demand distribution functions representing the retailer's uncertainty about future demand under different information and supply chain structures. The optimal order quantity is offered by the newsvendor solution; we only need to characterize the respective distribution functions. The demand cumulative distribution function is normal by construction in (RA) and (RD). In (RM), with the linear price function we derived in Proposition 1, the retailer's updated belief, based on the private signal and public price, will remain normal. We can apply the Normal Learning Theorem<sup>5</sup> (see [27] for a reference) to derive the analytical expressions for the distribution functions under Structures A, D, and M.

Lemma 1. Define $\begin{array} { r } { \tau _ { \nu } = \left( \frac { M - 1 } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { X } } \right) ^ { - 1 } } \end{array}$ and $\begin{array} { r } { \tilde { \theta } _ { - i } \equiv \sum _ { j \neq i } \tilde { \theta } _ { j } } \end{array}$

Retailer i's optimal order quantity is determined by

$$
Q _ {i} ^ {j} = a _ {i} + b _ {i} \mu_ {i} ^ {j} + \frac {1}{\sqrt {\tau_ {i} ^ {j}}} \Phi^ {- 1} \left(1 - \frac {s ^ {j}}{r}\right), \text {   for   } j = a, d, m
$$

where

$$
\begin{array}{l} \mu_ {i} ^ {a} = \frac {\tau}{N \tau_ {\delta} + \tau} \mu + \frac {N \tau_ {\delta}}{N \tau_ {\delta} + \tau} \overline {{\theta}}, \\ \mu_ {i} ^ {d} = \frac {\tau}{\tau + \tau_ {\delta}} \mu + \frac {\tau_ {\delta}}{\tau + \tau_ {\delta}} \tilde {\theta} _ {i}, \\ \mu_ {i} ^ {m} = \frac {\tau \mu}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} + \frac {\tau_ {\delta} \tilde {\theta} _ {i}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} \\ \qquad + \frac {(M - 1) \tau_ {\nu}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} \left(\tilde {\theta} _ {- i} + \frac {\tilde {X}}{L}\right) \end{array}
$$

$$
\begin{array}{l} \frac {1}{\tau_ {i} ^ {a}} = \frac {b _ {i} ^ {2}}{\tau + N \tau_ {\delta}} + \frac {1}{\tau_ {\varepsilon}}, \frac {1}{\tau_ {i} ^ {d}} = \frac {b _ {i} ^ {2}}{\tau + \tau_ {\delta}} + \frac {1}{\tau_ {\varepsilon}}, \\ \frac {1}{\tau_ {i} ^ {m}} = \frac {b _ {i} ^ {2}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} + \frac {1}{\tau_ {\varepsilon}}. \end{array}
$$

Lemma 2. lim $1 _ { M } {  } _ { \infty } E _ { X } \mu _ { i } ^ { m } = \mathrm { l i m } _ { N } {  } _ { \infty } \mu _ { i } ^ { a }$ , and lim $1 _ { M } {  } _ { \infty }$ $\begin{array} { r } { \tau _ { i } ^ { m } = \operatorname* { l i m } _ { N } \log _ { \infty } \tau _ { i } ^ { a } . } \end{array}$

Lemma 3.

$$
N <   1 + \frac {M - 1}{1 + \frac {2 (1 + M \frac {\tau \delta}{\tau}) M}{\sqrt {(5 M ^ {2} - 4) + (4 M - 2) M ^ {2} \frac {\tau \delta}{\tau} + M ^ {2} \frac {\tau \delta^ {2}}{\tau^ {2}}} - M (1 + \frac {\tau \delta}{\tau})}},
$$

then $\tau _ { i } ^ { m } > \tau _ { i } ^ { a }$

Lemma 2 implies that when both the number of informed market participants and the number of retailers approach infinity, the macro prediction market yields a forecast as accurate as the aggregate forecast in terms of the mean and variance of the forecasted demand distribution. Lemma 3 gives a condition under which the retailer's demand prediction is more precise using the macro prediction market than aggregate information sharing. Loosely speaking, given N retailers, the more precise each retailer's information (represented by $\tau _ { \delta } / \tau )$ , the more informed market participants are needed before the macro prediction market forecast will outperform the aggregate forecast. In addition, given the precision level of each retailer's information, the more retailers in the supply chain, the more informed market participants are needed before the macro prediction market forecast outperforms the aggregate forecast. This condition is easy to be satisfied. For example, given $\tau { = } 1 , \tau _ { \delta } { = } 2$ , if $N { = } 4$ , then M = 35; if $N { = } 6$ , then $M = 7 7 ;$ and if $N { = } 2 0$ then $M { = } 8 1 9$ . But given τ = 1, τ = 4, if $N { = } 4 .$ , then $M = 5 9$ if $N { = } 6 .$ , then $M = 1 3 7 ;$ and if $N { = } 2 0$ , then $M { = } 1 5 7 9$

Lemma 3 has important implications in the supply chain information systems design. In the absence of good incentives, truthful information sharing among retailers is problematic. In contrast, our proposed macro prediction market automatically aligns the retailers' incentives to reveal their private information. Furthermore, the macro market-coordinated information sharing can absorb useful information from other market participants. It has the potential to achieve more accurate forecast than what is available under truthful information sharing among retailers.

However, forecast accuracy alone cannot determine retailer profits because the manufacturer can use the same information to make pricing decisions.

## 3.3. The manufacturer's decision problem

The manufacturer wants to choose the most profitable wholesale price $s ^ { j } ,$ for ${ j = a , d , m }$ , based on the expected aggregate order from the retailers. We assume that there is no fixed cost and that unit production cost is a constant, $c .$ We also assume the manufacturer will produce an amount equal to her expected orders from retailers. The manufacturer's decision problems under the three supply chain structures can be expressed as follows:

$$
\max _ {s ^ {a} \geq 0} (s ^ {a} - c) \left[ \sum_ {i} Q _ {i} ^ {a} | \overline {{\theta}} \right]\tag{MA}
$$

$$
\max _ {s ^ {d} \geq 0} (s ^ {d} - c) \left[ \sum_ {i} E _ {\tilde {\theta} _ {i}} [ Q _ {i} ^ {d} ] \right]\tag{MD}
$$

$$
\max _ {s ^ {m} \geq 0} (s ^ {m} - c) \left[ \sum_ {i} E _ {\tilde {\theta} _ {i}} [ Q _ {i} ^ {m} | p ] \right]\tag{MM}
$$

In the truthful forecast sharing case (MA), the manufacturer shares the retailers' forecasts and so can precisely update her belief on all the retailers' demand distributions and infer retailers' order quantities. A single wholesale price is set. In (MD), the manufacturer does not have any information about retailers' orders, yet also sets a single wholesale price. She takes the expectations over her prior beliefs about all the retailers' private signal distributions. In the market-coordinated forecast sharing case (MM) the manufacturer sets a contingent wholesale price based on her rational expectation of the aggregate order quantity conditional on the current index price $p .$ Since the manufacturer does not know each retailer's private forecast, she infers it from the public observed index price $p .$ . The following proposition compares the manufacturer's pricing decisions under different supply chain information structures.

Proposition 3. The manufacturer's wholesale prices under supply chain structures A, D, and M have the following relations:

( a ) $s ^ { a }$ is strictly increasing with $\bar { \theta \ } . \quad { \cal I } f \ \bar { \theta } \geq$ $\underline { { a \left( N \tau _ { \delta } + \tau \right) \left( T ^ { d } - T ^ { a } \right) } } + b \mu [ \left( \bar { N \tau } _ { \delta } + \tau \right) T ^ { d } - \tau T ^ { a } ]$ ; then bN<sup>s</sup>dT<sup>a</sup> $s ^ { a } \geq s ^ { d } .$ . Otherwise, Otherwise, $\stackrel { \iota _ { \partial } } { s ^ { a } } < \mathnormal { s } ^ { d } .$

(b) $s ^ { m }$ is strictly increasing with ${ \overset { \cdot } { p } } _ { \cdot } H { p } \geq { \frac { a } { b } } { \frac { T ^ { d } - T ^ { m } } { T ^ { m } } } + \mu { \frac { T ^ { d } } { T ^ { m } } }$ then $s ^ { m } { \geq } s ^ { \dot { d } } .$ . Otherwise, $s ^ { m } < s ^ { d } .$

(c) If $\overline { { { \theta } } } \geq \frac { T ^ { m } ( a + b p ) ( N \tau _ { \delta } + \tau ) - T ^ { a } [ a N \tau _ { \delta } + \tau ( a + b \mu ) ] } { b N \tau _ { \delta } T ^ { a } }$ ; then $s ^ { a } { \geq } s ^ { m }$ . Otherwise, $s ^ { a } < s ^ { m }$

where $\begin{array} { r } { a = \sum _ { i = 1 } ^ { N } a _ { i } , b = \sum _ { i = 1 } ^ { N } b _ { i } } \end{array}$ ; and $\begin{array} { r } { T ^ { j } = \left( \sum _ { i = 1 } ^ { N } \ \frac { 1 } { \sqrt { \tau _ { i } ^ { j } } } \right) ^ { - 1 } } \end{array}$ for $j = a , d , m$

Proposition 3 details the conditions related to the manufacturer's pricing decision. Both 3(a) and 3(b) say that under truthful forecast sharing or macro prediction market-coordinated forecast sharing, there is a critical fractile above which the manufacturer will tend to set a higher wholesale price in supply chain Structure A and M than in Structure D. Proposition 3(c) further characterizes the relationship between aggregate signal θ<sup>¯</sup> and index market price p: a low index market price is likely to induce a low $s ^ { m }$ , and vice versa.

The wholesale price increases in both truthful forecast signal $\overline { { \theta } }$ and the index price p since higher values reflect an aggregate perception of a prosperous macro economy in the future. The manufacturer thus expects to reap more benefits by charging a high wholesale price. In the same situation, retailers tend to place larger orders than what they would based on just their own information. This seems to contradict the practice of quantity discounts, i.e., the higher the order quantity, the lower the wholesale price. The underlying driving force of this result is due to the manufacturer's confidence that the overall market condition is prosperous and her bargaining power in setting the market price. Although in such case the unit order cost increases, retailers can be compensated by the likely increased demand that is accurately predicted by the macro prediction market. In contrast, without the market prediction, the retailers will order according to their decentralized solutions. They face the opportunity cost of lost sales if demand surges. Therefore, the retailer will still be able to earn a high total profit even with a lower unit profit margin.

On the contrary, if the aggregate forecast signal θ<sup>¯</sup> or the index market price p is low, retailers will generally believe that the macro economy will worsen and so order less. The manufacturer may set a low price to encourage more orders in such an economic downturn. This is also accurately predicted by the macro prediction market. In this case, retailers' misfortune will be essentially compensated by the lower unit ordering price.

The index market price creditably conveys retailers' private forecasts about macro economy uncertainty. Demand forecast sharing among the manufacturer and retailers is achieved indirectly via the macro prediction market. The manufacturer can control retailers' order variance by adjusting the price in a direction that is socially desirable from the perspective of the supply chain. This adjustment is especially important in reducing the bullwhip effect.

## 4. The value of forecast sharing

We investigate two aspects of forecast sharing in this section: the impact on retailers' order variance and the expected supply chain efficiency.

## 4.1. The order variance

Retailers experience demand uncertainty from customers, but the manufacturer experiences it from the retailers. The manufacturer's decision making improves as retailer aggregate order variance drops. Under truthful forecast sharing, there is no order variance because the manufacturer precisely observes retailers' demand forecast thus perfectly infers their order quantities. When forecast sharing is unavailable, the decentralized order variances vary according to the different retailer signals. The macro prediction market significantly helps the manufacturer improve her inferred order accuracy.

Proposition 4. $V a r ( Q _ { i } ^ { m } | p ) < V a r ( Q _ { i } ^ { d } ) ; V a r ( Q _ { i } ^ { m } | p )$ decreases in M; lim $_ { M  \infty } \mathrm { V a r } ( Q _ { i } ^ { m } | p ) = \mathrm { V a r } ( Q _ { i } ^ { a } | \stackrel { \_ } { \theta } ) = 0$

Macro prediction market coordination helps reduce order variance because retailers can more accurately forecast the macro economy and their own demand uncertainty. The manufacturer can also make more accurate inferences about the macro economy. The macro prediction market induces less supply chain order variance when more useful information about the macro factor is incorporated. If the macro prediction market is precise enough, it can replicate truthful forecast sharing as order variance disappears. This has important implications for the bullwhip effect. This well-known informational problem is often represented by the observed increasing order variances from downstream partners in the supply chain. The literature has identified potential sources of the bullwhip effect but has not offered an effective solution to reduce the effect by properly managing conflicting incentives among supply chain partners. Our macro prediction market-coordinated supply chain structure can alleviate this effect. Note that by imposing a correlation across the consumer markets, potentially there is another dimension of the bullwhip effect — the rationing game (see Ref. [22]). We don't deal with this problem in this paper since we do not assume capacity constraints of the manufacturer.

## 4.2. The expected supply chain profit

A decentralized supply chain solution is generally suboptimal to an integrated, first-best solution. A first-best solution, which is usually impossible, requires the manufacturer to set the wholesale price equal to the marginal production cost. A number of articles on supply chain coordination discuss the use of more complex non-linear pricing contracts or real options contracts to achieve the first-best solution [7]. However, we are most interested in determining the best supply chain structure under the simple price-only contract, the most common contract format in the supply chain practice. We are interested in evaluating the impact of information sharing on overall supply chain efficiency.

The total expected supply chain profit is determined by the sum of all supply chain partners' expected profits. Under the supply chain structures A, D, and M, the expected supply chain profit can be expressed as

$$
\begin{array}{l} E \Pi^ {j} = \sum_ {i = 1} ^ {N} E \Pi_ {R} ^ {j} + E \Pi_ {M} ^ {j} \\ = (r - c) E \left[ \sum_ {i = 1} ^ {N} Q _ {i} ^ {j} \right] - r E \sum_ {i = 1} ^ {N} \Gamma_ {i, j} (Q _ {i} ^ {j}), \\ \text { where } \Gamma_ {i, j} (Q _ {i} ^ {j}) = \frac {1}{\sqrt {\tau_ {i} ^ {d}}} \int_ {- \infty} ^ {- t _ {j}} \Phi (t) \mathrm{d} t, j = a, d, m, \text { and } t _ {j} = \Phi^ {- 1} \left(\frac {s /}{r}\right). \end{array}
$$

Proposition 5. If mi $\begin{array} { c c c } { { \imath ( s ^ { d } , s ^ { m } , s ^ { a } ) \geq r / 2 > c , } } \end{array}$ then the expected supply chain profit satisfies $E I I ^ { a } > E I I ^ { d }$ $E I I ^ { m } { > } E I I ^ { d }$ , and $\begin{array} { r } { \operatorname* { l i m } _ { M \to \infty } E I I ^ { m } = \operatorname* { l i m } _ { N \to \infty } E I I ^ { a } } \end{array}$

Proposition 5 shows the value of information sharing in the supply chain. Under the condition $\operatorname* { m i n } ( s ^ { d } , \ s ^ { m }$ $s ^ { a } ) { \geq } r / 2 { > } c$ the expected supply chain profits under Structure A and M are greater than profits under Structure D. This condition is not hard to be satisfied. Since the manufacturer is the Stackelberg leader in the game, it is not a surprise that she will charge a wholesale price at least half of the retail price leaving retailers a smaller profit margin. Most industry products have retail prices less than two times the wholesale price. Compared to the decentralized supply chain, introducing the macro prediction market will improve supply chain efficiency by increasing the total pie to be divided, and the manufacturer's expected profit will increase since she has all the bargaining power. Retailers, however, may not benefit since the market condition affects the manufacturer's pricing decision as well as the division of total supply chain surplus. Retailers' expected positive profits as a return of their private knowledge will attract them to trade in the macro prediction market regardless of the market condition.

Total supply chain efficiency depends on market liquidity and information transparency, i.e., how much useful information about the macro factor can be forecasted and revealed to the supply chain partners. In general, whether the macro prediction market-coordinated supply chain efficiency will outperform the aggregate supply chain efficiency depends on the tradeoff between the level of information asymmetry and prediction precision. On the one hand, the aggregate supply chain has no information asymmetry and will tend to outperform the market prediction. On the other hand, the market prediction can incorporate useful outside information and so be more precise. When both the number of informed traders in the market and the number of retailers approach infinity, the supply chain structures M and Ayield the same expected profits.

The traditional supply chain literature considers the incentive and coordination issues within a closed system. Our work sheds new light on this area because of the additional benefits generated outside the supply chain system. Since the market is an open system, one retailer's non-participation decision will not compromise the information aggregation. But retailers who believe the market efficiently predicts the macro factor will tend to incorporate the market price information into their order decisions. Our proposed framework aligns retailers' incentives to share information and explores the value of useful information from other sources to increase overall supply chain efficiency.

## 5. Extensions and discussions

We consider extensions of our model in this section. First, we investigate how retailers' changing risk preferences influence their trading strategies. Second, we characterize the retailer's Pareto improving macro prediction market trading strategy. Third, we extend the index trading to the index-based derivative trading to demonstrate that our proposed macro prediction market structure can support supply chain risk management in corporate practice. Finally, we discuss the impact of the macro prediction market construction on moral hazard problems.

## 5.1. The risk-averse retailer

Retailers' supply chain order strategy and macro prediction market trading strategy are perfectly separable when they are risk-neutral. Their incentives to trade come from their superior knowledge about future uncertainty of the economy. No arbitrage opportunities exist under the REE framework. In equilibrium, no contingent claim matters to the retailers because they expect to pay the “average” value of the contingent claim based on the common market belief. Consequently, retailers cannot make extra money by trading more complex financial contracts. Since risk-neutral retailers only care about the mean effect of their profit, their strategy is simply to trade the index.

Retailers prefer to purchase the contingent claim as a type of insurance when they are risk-averse. A key component in our model is the retailer's piecewiselinear payoff function, and a kink occurs when the demand equals order quantity. This type of payoff function can be hedged via writing covered call options on the retail index [17]. Given the retailer's order quantity $\mathcal { Q } _ { i } ,$ trading the contingent claim is a Pareto improving strategy because the retailer's expected overall profit is the same in both the macro prediction market and the commodity market. However, options can cancel off some uncertainty thus reducing the profit variance. The contingent claim can be expressed as:

$$
\begin{array}{l} f _ {i} = - r \min [ Q _ {i}, a _ {i} + b _ {i} \theta ] = r \max [ - Q _ {i}, - a _ {i} - b _ {i} \theta ] \\ = - r a _ {i} - r b _ {i} \theta + r \max [ - Q _ {i} + a _ {i} + b _ {i} \theta , 0 ] \\ = - r a _ {i} - r b _ {i} \theta + r (a _ {i} + b _ {i} \theta - Q _ {i}) ^ {+} \\ = - r a _ {i} - r b _ {i} \theta + r b _ {i} \left(\theta - \frac {Q _ {i} - a _ {i}}{b _ {i}}\right) ^ {+} \end{array}
$$

The contingent claim can be generated by borrowing $r a _ { i }$ shares of riskless bonds and short selling $r b _ { i }$ shares of the index and long the same shares of call option with strike price $K _ { i } = \frac { Q _ { i } ^ { - } a _ { i } } { b _ { i } }$

Proposition 6. A risk-averse retailer's Pareto improving macro prediction market strategy when ordering $\mathcal { Q } _ { i }$ in the supply chain is to borrow $r a _ { i }$ shares of riskless bonds and short $r b _ { i }$ shares of the index θ and long $r b _ { i }$ shares of call option with strike price $K _ { i } = \frac { Q _ { i } - a _ { i } } { b _ { i } }$

<sup>i</sup>This insurance can deal with the supply chain operation and macro prediction market uncertainty by smoothing out the total payoff from both. The future index price is positively correlated with the retailer's consumer market demand, so the retailer may face a loss in her consumer market if it goes down. However, the retailer can earn a positive profit in the macro prediction market by short selling. If the future index price goes up, the retailer will not have enough inventory to cover demand and will lose in both the macro prediction market and the consumer market. However, this loss can be covered by the call options at hand. In any case, the retailer's risk exposure can be effectively hedged.

In the newsvendor model it is clear that risk-averse retailers will order less than the expected valuemaximizing quantity [11]. It was shown that, under very general conditions, the risk-averse retailer's optimal ordering quantity increases with hedging [13]. Therefore, opportunities for options trading help optimize retailers' inventory decisions.

## 5.2. The impact of the macro prediction market

Our macro prediction market-coordinated supply chain framework can bring risk management into corporate business practice. In the supply chain literature, risk sharing and transfer are obtained by bilateral contract commitments. Examples of widely used contract forms include reorder/buy back contracts [28], nonlinear pricing/quantity discount policy [32], and linear transfer payments [6]. It was shown in [3] that all these contracts can be classified as real options contracts. However, the question of whether the options contracts can be properly priced remains unanswered. Followingon work [5] proposed pricing real options in a bilateral contract using Arrow–Debreu securities. We extend the pricing of options contract in a market setting with multiple market players. Our proposed options contracts are based on a risky security (the retail index) with continuous payoffs. This is more realistic than using Arrow–Debreu securities.

Options contracts can provide retailers insurance to deal with operational risk. However, insurance may cause a moral hazard problem since the retailers may not take socially conscious actions when they feel economically secure. Moral hazard problems have been well-understood in economics [15] but are generally overlooked in the supply chain literature. For example, when the market is uncertain, a manufacturer may provide retailers with a put option allowing them to sell back unsold products at a prespecified salvage value (the strike price). The retailer may not put much effort into selling products if the promotion cost is higher than its opportunity loss. All bilateral real options contracts suffer this problem. One possible solution is to write contracts based on macro factors that correlate with the retailer's hedging needs but are not under the retailer's control. Trading indices or index-based derivatives can solve these problems since they are simply contingent claims written on the macro factor (the index). The retailers still incur residual risk in the marketplace. In addition, options trading can solve the market participation problem since there might be experts who are unwilling to trade in the macro prediction market for fear of financial losses. Buying or selling options with preferred strike prices can afford these experts a measure of protection.

## 6. Conclusion

The Internet has facilitated real-time information access across organizations, making it possible to integrate that information into decision models. While research on supply chain information systems design has focused on technological efficiency, such as XML-based workflow and database integration, our innovation is to build a macro prediction market into organizations' evolutionary information systems design to encourage information sharing and aid supply chain decision making. We show that the macro prediction market can be used to reduce the bullwhip effect in the supply chain. In addition, the market allows anyone with information to trade. More complete information makes the supply chain more efficient. We thus provide important insights in designing market-based information systems in guiding the structure of supply chain interactions.

We examine the impact of introducing a new type of market – a macro prediction market – on supply chain information sharing and decision making. We also make unique contributions to the emerging fields of prediction market and macro hedging market research. Prediction markets are indirectly influenced by financial markets. The significance of these markets is still limited to predicting elections, sport trades, and other utility stocks and no clear resource allocation issue has yet been studied. In contrast to existing research, we look at a concrete application in the class of supply chain problems to validate the significance of prediction markets for decision support in business practice.

In the macro hedging market literature, the key to hedging risk is sharing risk. Supply chain partners tend to act strategically in providing information due to payoff asymmetry thus preventing effective risk sharing. The strategy of creating macro indices to trade instead of trading physical products has a number of advantages. First, the trading asset is broad enough to attract sufficient liquidity in the market. The liquidity problem has been identified as an important reason for the failure of many B2B markets. Many industrial products are not suitable for market trading because of a lack of homogeneity. In addition, contracts specifying different quality, delivery times and other features are usually negotiated between buyer and seller, and so generate high transaction costs. Index-related financial contracts, in contrast, are essentially homogeneous products that can be traded with sufficient liquidity. Riskpooling can be realized without costly negotiation and contract enforcement between parties. Therefore, the creation of the macro prediction market makes possible the sharing of economic risks. The macro index-related financial contracts are also general enough to reduce the moral hazard problems arising from bilateral insurance contracts.

Certain limitations apply to this paper. We assume the retail prices are exogenously given and are the same for all retailers. Endogenizing the pricing decision is an interesting research question that can be studied in the future. Allowing different retailers to charge different retail prices sounds a more realistic relaxation. In the case of heterogeneous retail prices the manufacturer can be expected to also set heterogeneous wholesale prices.

Future work could extend this research to cases with multiple manufacturers and retailers. The construction of the index should also be studied. Different indices could be designed to represent a variety of products or tangible/ intangible assets in the supply chain network. The indices could be further distinguished to reflect regional environmental economic risks. More innovative and complex financial instruments, such as index-based derivatives, can also be introduced for risk hedging purposes. In addition, future researchers can extend our findings to other business applications.

## Acknowledgment

This paper was presented at several seminars including those at the University of Texas at Austin, University of Alberta, National University of Singapore, City University of New York — Baruch College, and University of Maryland, Baltimore County. We appreciate valuable feedback from seminar participants. We especially thank Anant Balakrishnan and Steve Gilbert for their helpful comments and suggestions. The authors take responsibility for all errors.

## Appendix A

Sketch of Proof of Proposition 1. We look for a linear equilibrium of the form

$$
\left\{ \begin{array}{l l} \mu_ {i} ^ {m} & = \alpha_ {0} + \alpha_ {1}   \tilde {\theta} _ {i} + \alpha_ {2} p \\ \pi_ {i} & = \beta_ {0} + \beta_ {1} \mu_ {i} ^ {m} + \beta_ {2} p \\ p (y) & = \lambda_ {0} + \lambda_ {1} y \end{array} \right.\tag{1}
$$

FOC w.r.t. $\pi _ { i }$ from Eq. (I) together with the equality in Eq. (II) we have the following

$$
\beta_ {0} = 0, \beta_ {1} = \frac {1}{\lambda_ {1}}, \beta_ {2} = - \frac {1}{\lambda_ {1}}\tag{2}
$$

$$
\begin{array}{l} p = \frac {\lambda_ {0} + M \alpha_ {0}}{M + 1 - M \alpha_ {2}} + \frac {\alpha_ {1}}{M + 1 - M \alpha_ {2}} \sum_ {i = 1} ^ {M} \tilde {\theta} _ {i} \\ \quad + \frac {\lambda_ {1}}{M + 1 - M \alpha_ {2}} \tilde {X} \equiv A _ {0} + A _ {i} \left(\sum_ {i = 1} ^ {M} \tilde {\theta} _ {i} + \frac {\tilde {X}}{L}\right) \end{array}\tag{3}
$$

where $L = { \frac { \alpha _ { 1 } } { \lambda _ { 1 } } } .$ So $A _ { 0 } = { \frac { \lambda _ { 0 } + M \alpha _ { 0 } } { M + 1 - M \alpha _ { 2 } } }$ and $A _ { 1 } = \frac { \alpha _ { 1 } } { M + 1 - M \alpha _ { 2 } } ,$ which are constants for given M.

To ensure that Eq. (I) is a well-behaved concave function of $\pi _ { i } , { \mathrm { S O C } }$ w.r.t. $\pi _ { i }$ from Eq. (I) yields $\lambda _ { 1 } { > } 0$

To solve the REE, we only need to solve for constants $\alpha _ { 0 } , \alpha _ { 1 }$ $\alpha _ { 2 } , \lambda _ { 0 } ,$ and $\lambda _ { 1 }$ . From Eq. (3) and Normal Learning Theorem, $p = E \Big [ \theta | \sum _ { i = 1 } ^ { M } \ \stackrel {  } { \theta } _ { i } + \frac { \tilde { x } } { L } \Big ] = \frac { \stackrel { \iota } { \tau } \mu ^ { \setminus } } { \tau \pm M ^ { 2 } \tau _ { p } } + \frac { M \tau _ { p } } { \tau + M ^ { 2 } \tau _ { p } } \frac { ( M + 1 - M \alpha _ { 2 } ) \stackrel {  } { p ^ { - } } ( \lambda _ { 0 } + M \alpha _ { 0 } ) } { \alpha _ { 1 } } ,$ where $\begin{array} { r } { \tau _ { p } = \left( \frac { M } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { X } } \right) ^ { - } } \end{array}$ 1

Rearranging terms and comparing with $p ( y ) { = } \lambda _ { 0 } { + }$ $\lambda _ { 1 } y$ yields

$$
\alpha_ {1} (\tau + M ^ {2} \tau_ {p}) = M \tau_ {p} (M + 1 - M \alpha_ {2})\tag{4}
$$

$$
\alpha_ {1} \tau \mu = M \tau_ {p} (\lambda_ {0} + M \alpha_ {0})\tag{5}
$$

Belief update by the Normal Learning Theorem yields

$$
\begin{array}{l} \mu_ {i} ^ {m} \equiv E \left[ \theta | \tilde {\theta} _ {i}, \tilde {\theta} _ {- i} + \frac {\tilde {X}}{L} \right] = \frac {\tau \mu}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {v}} + \frac {\tau_ {\delta} \tilde {\theta} _ {i}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {v}} \\ \quad + \frac {(M - 1) \tau_ {v}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {v}} \left(\tilde {\theta} _ {- i} + \frac {\tilde {X}}{L}\right), \end{array}
$$

where $\begin{array} { r } { \tau _ { \nu } = \left( \frac { M - 1 } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { X } } \right) ^ { - 1 } } \end{array}$

Substituting Eq. (3) into $\mu _ { i } ^ { m }$ yields

$$
\alpha_ {0} = \frac {\alpha_ {1} \tau \mu - (M - 1) (\lambda_ {0} + M \alpha_ {0}) \tau_ {v}}{\alpha_ {1} [ \tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {v} ]}\tag{6}
$$

$$
\alpha_ {1} = \frac {\tau_ {\delta} - (M - 1) \tau_ {v}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {v}}\tag{7}
$$

$$
\alpha_ {2} = \frac {(M - 1) (M + 1 - M \alpha_ {2}) \tau_ {\nu}}{\alpha_ {1} [ \tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu} ]}\tag{8}
$$

Since we have 5 unknowns $\alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } , \lambda _ { 0 } ,$ and L in the system of Eqs. (4)–(8). So it's solvable.

We suppress the expressions for all other parameters but L:

$$
L = \sqrt {\frac {\sqrt {(5 M ^ {2} - 4) \tau^ {2} + (4 M - 2) M ^ {2} \tau \tau_ {\delta} + M ^ {2} \tau_ {\delta} ^ {2}} - M (\tau + \tau_ {\delta})}{2 (\tau + M \tau_ {\delta}) M (M - 1) \tau_ {\chi}} \tau_ {\delta}}\tag{9}
$$

So L is a uniquely determined constant for given M. Define $k _ { 0 } = \beta _ { 0 } + \beta _ { 2 } p .$ , and $k _ { 1 } = \beta _ { 1 }$ , then $\pi _ { i } | p { = } k _ { 0 } { + } k _ { 1 } \tilde { \theta } _ { i }$ So at the equilibrium price an agent's order strategy is information revealing. □

Proof of Proposition 2.

$$
\begin{array}{l} \mathrm{PI} \equiv \frac {1}{\operatorname{Var} [ \theta | p ]} = \frac {1}{\operatorname{Var} \left[ \theta | \sum_ {i = 1} ^ {M} \tilde {\theta} _ {i} + \frac {\tilde {X}}{L} \right]} = \tau + M ^ {2} \tau_ {p} \\ = \tau + M ^ {2} \frac {L ^ {2} \tau_ {X} \tau_ {\delta}}{M L ^ {2} \tau_ {X} + \tau_ {\delta}} \end{array}
$$

Substituting $L ^ { 2 }$ from Eq. (9) and consider $N { \longrightarrow }$ ∞ yields

$$
\begin{array}{l} \lim _ {M \to \infty} \mathrm{PI} = \lim _ {M \to \infty} \tau \\ \qquad + \frac {M \tau_ {\delta}}{1 + \frac {2 (\tau + M \tau_ {\delta}) (M - 1)}{\sqrt {(5 M ^ {2} - 4) \tau^ {2} + (4 M - 2) M ^ {2} \tau \tau_ {\delta} + M ^ {2} \tau_ {\delta} ^ {2}} - M (\tau + \tau_ {\delta})}} \\ \qquad = \infty \end{array}
$$

$$
\begin{array}{l} \lim _ {M \to \infty} p = E \left[ \theta | \sum_ {i = 1} ^ {M} \tilde {\theta} _ {i} + \frac {\tilde {X}}{L} \right] \\ = \frac {\tau \mu}{\tau + M ^ {2} \tau_ {p}} + \frac {M \tau_ {p}}{\tau + M ^ {2} \tau_ {p}} \left(\sum_ {i = 1} ^ {M} \tilde {\theta} _ {i} + \frac {\tilde {X}}{L}\right) = \theta \end{array}
$$

This completes the proof.

Proof of Lemma 1. Since we formulate the retailer's problem as the traditional newsvendor problem, the newsvendor solutions give us $\mathcal { Q } _ { i } ^ { j } = F _ { i , j } ^ { - 1 } \big ( \bar { 1 } - \frac { s ^ { j } } { r } \big ) , j = a , d ,$ $m ,$ where $F _ { i , j } ( \cdot )$ denote the forecasted demand distribution by retailer i under scenario $j .$ . Normalizing the expression we write it as $\begin{array} { r l } & { \mathcal { Q } _ { i } ^ { j } = a _ { i } + b _ { i } \mu _ { i } ^ { j } + \frac { 1 } { \sqrt { \tau _ { i } ^ { j } } } \phi ^ { - 1 } \biggl ( 1 - \frac { s ^ { j } } { r } \biggr ) } \\ & { \mathbf { \Delta } _ { \mathbf { a } \mathbf { c } } \mathbf { \Delta } _ { \mathbf { f } \mathbf { o } } 1 \mathsf { l } _ { \mathbf { o u r c } } . } \end{array}$ where $\mu _ { i } ^ { j }$ and $\sqrt { \tau _ { i } ^ { j } }$ are derived as follows:

Recall that $\stackrel { \triangledown } { \boldsymbol { \theta } } = \frac { 1 } { N } \sum _ { i = 1 } ^ { N } { \tilde { \theta } } _ { i }$ . It's easy to verify that θ<sup>¯</sup> is normally distributed, $\begin{array} { r } { \overline { { \theta } } \sim N \bigg ( \mu , \frac { 1 } { \tau } + \frac { 1 } { N \tau _ { \delta } } \bigg ) } \end{array}$

Based on the Normal Learning Theorem, the belief update yields

$$
\mu_ {i} ^ {a} \equiv E [ \theta | \overline {{\theta}} ] = \frac {\tau}{N \tau_ {\delta} + \tau} \mu + \frac {N \tau_ {\delta}}{N \tau_ {\delta} + \tau} \overline {{\theta}}
$$

$$
\mu_ {i} ^ {d} \equiv E [ \theta | \tilde {\theta} _ {i} ] = \frac {\tau}{\tau + \tau_ {\delta}} \mu + \frac {\tau_ {\delta}}{\tau + \tau_ {\delta}} \tilde {\theta} _ {i}
$$

$$
\begin{array}{l} \mu_ {i} ^ {m} \equiv E \left[ \theta | \tilde {\theta} _ {i}, \tilde {\theta} _ {- i} + \frac {\tilde {X}}{L} \right] = \frac {\tau \mu}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} + \frac {\tau_ {\delta} \tilde {\theta} _ {i}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} \\ \qquad + \frac {(M - 1) \tau_ {\nu}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} \left(\tilde {\theta} _ {- i} + \frac {\tilde {X}}{L}\right), \end{array}
$$

where $\begin{array} { r } { \tau _ { \nu } = \left( \frac { M - 1 } { \tau _ { \delta } } + \frac { 1 } { L ^ { 2 } \tau _ { X } } \right) ^ { - 1 } } \end{array}$

$$
\begin{array}{l} \operatorname{Var} [ D _ {i} | \bar {\theta} ] = b _ {i} ^ {2} \operatorname{Var} [ \theta | \bar {\theta} ] + \frac {1}{\tau_ {\varepsilon}} = \frac {b _ {i} ^ {2}}{\tau + N \tau_ {\delta}} + \frac {1}{\tau_ {\varepsilon}} \equiv \frac {1}{\tau_ {i} ^ {a}} \\ \operatorname{Var} [ D _ {i} | \tilde {\theta} _ {i} ] = b _ {i} ^ {2} \operatorname{Var} [ \theta | \tilde {\theta} _ {i} ] + \frac {1}{\tau_ {\varepsilon}} = \frac {b _ {i} ^ {2}}{\tau + \tau_ {\delta}} + \frac {1}{\tau_ {\varepsilon}} \equiv \frac {1}{\tau_ {i} ^ {d}} \\ \operatorname{Var} [ D _ {i} | \tilde {\theta} _ {i}, p ] = b _ {i} ^ {2} \operatorname{Var} [ \theta | \tilde {\theta} _ {i}, p ] + \frac {1}{\tau_ {\varepsilon}} \\ = \frac {b _ {i} ^ {2}}{\tau + \tau_ {\delta} + (M - 1) ^ {2} \tau_ {\nu}} + \frac {1}{\tau_ {\varepsilon}} \equiv \frac {1}{\tau_ {i} ^ {m}} \end{array}
$$

This concludes the proof.

Proof of Lemma 2 and 3. Results are directly obtained by Lemma 1 and Eq. (9). □

Proof of Proposition 3.

$$
\begin{array}{l} Q _ {i} ^ {a} | \overline {{\theta}} = a _ {i} + b _ {i} \left[ \frac {\tau}{N \tau_ {\delta} + \tau} \mu + \frac {N \tau_ {\delta}}{N \tau_ {\delta} + \tau} \overline {{\theta}} \right] \\ \quad + \frac {1}{\sqrt {\tau_ {i} ^ {a}}} \Phi^ {- 1} \left(1 - \frac {s ^ {a}}{r}\right) \end{array}\tag{10}
$$

$$
\begin{array}{c} E _ {\tilde {\theta} _ {i}} [ Q _ {i} ^ {d} ] = a _ {i} + b _ {i} E _ {\tilde {\theta} _ {i}} [ \mu_ {i} ^ {d} ] + \frac {1}{\sqrt {\tau_ {i} ^ {d}}} \varPhi^ {- 1} \bigg (1 - \frac {s ^ {d}}{r} \bigg) \\ = a _ {i} + b _ {i} \mu + \frac {1}{\sqrt {\tau_ {i} ^ {d}}} \varPhi^ {- 1} \bigg (1 - \frac {s ^ {d}}{r} \bigg) \end{array}\tag{11}
$$

$$
\begin{array}{l} E _ {\tilde {\theta} _ {i}} [ Q _ {i} ^ {m} | p ] = a _ {i} + b _ {i} E _ {\tilde {\theta} _ {i}} [ \mu_ {i} ^ {m} | p ] \\ \quad + \frac {1}{\sqrt {\tau_ {i} ^ {m}}} \Phi^ {- 1} \left(1 - \frac {s ^ {m}}{r}\right) = a _ {i} + b _ {i} p \\ \quad + \frac {1}{\sqrt {\tau_ {i} ^ {m}}} \Phi^ {- 1} \left(1 - \frac {s ^ {m}}{r}\right) \end{array}\tag{12}
$$

Note that $\scriptstyle \mu _ { i } ^ { m } = E [ \theta | \tilde { \theta } _ { i } , p ] .$ , and $E _ { \widetilde { \theta } _ { i } } [ \mu _ { i } ^ { m } | p ] { = } E _ { \widetilde { \theta } _ { i } } [ E [ \theta | \widetilde { \theta } _ { i } , p ] ] { = }$ $E [ \theta | p ] = p$ . Substituting Eqs. $( 1 0 ) – ( 1 2 )$ into (MA), (MD), (MM) and taking FOC w.r.t. $s ^ { j } ,$ for j= a, d, m, we have

$$
\begin{array}{l} \Phi^ {- 1} \left(1 - \frac {s ^ {a}}{r}\right) + T ^ {a} \left(a + b \left[ \frac {\tau}{N \tau_ {\delta} + \tau} \mu + \frac {N \tau_ {\delta}}{N \tau_ {\delta} + \tau} \bar {\theta} \right]\right) \\ = \left(\frac {s ^ {a} - c}{r}\right) \frac {1}{\phi \left(\Phi^ {- 1} \left(1 - \frac {s ^ {a}}{r}\right)\right)} \end{array} \tag {13}\tag{13}
$$

$$
\Phi^ {- 1} \left(1 - \frac {s ^ {d}}{r}\right) + T ^ {d} (a + b \mu) = \left(\frac {s ^ {d} - c}{r}\right) \frac {1}{\phi \left(\Phi^ {- 1} \left(1 - \frac {s ^ {d}}{r}\right)\right)}\tag{14}
$$

$$
\Phi^ {- 1} \left(1 - \frac {s ^ {m}}{r}\right) + T ^ {m} (a + b p) = \left(\frac {s ^ {m} - c}{r}\right) \frac {1}{\phi \left(\Phi^ {- 1} \left(1 - \frac {s ^ {m}}{r}\right)\right)}\tag{15}
$$

where $\begin{array} { r } { a = \sum _ { i = 1 } ^ { N } a _ { i } , b = \sum _ { i = 1 } ^ { N } b _ { i } , a n d T ^ { j } = \left( \sum _ { i = 1 } ^ { N } \frac { 1 } { \sqrt { \tau _ { i } ^ { j } } } \right) ^ { - 1 } } \end{array}$ for ${ j = a , m , d . }$

Let $\scriptstyle \boldsymbol { x } _ { 0 } = \boldsymbol { c } / r , \boldsymbol { x } _ { j } = \boldsymbol { s } ^ { j } / r , t _ { j } = \boldsymbol { \varPhi } ^ { - 1 } ( \boldsymbol { x } _ { j } )$ , for ${ j = a , d , m }$ . Using the equality $\bar { \phi } ^ { - 1 } ( 1 - x _ { j } ) { = } { - } \bar { \phi } ^ { - 1 } ( x _ { j } )$ and, simplifying the expression, we derive

$$
\begin{array}{l} T ^ {a} \bigg (a + b \bigg [ \frac {\tau}{N \tau_ {\delta} + \tau} \mu + \frac {N \tau_ {\delta}}{N \tau_ {\delta} + \tau} \overline {{\theta}} \bigg ] \bigg) \\ = \frac {\Phi (t _ {a}) - x _ {0}}{\phi (t _ {a})} + t _ {a} \end{array}\tag{16}
$$

$$
T _ {d} (a + b \mu) = \frac {\Phi (t _ {d}) - x _ {0}}{\phi (t _ {d})} + t _ {d}\tag{17}
$$

$$
T _ {m} (a + b p) = \frac {\Phi (t _ {m}) - x _ {0}}{\phi (t _ {m})} + t _ {m}\tag{18}
$$

Let $g ( t ) = \frac { \phi ( t ) - x _ { 0 } } { \phi ( t ) } + t$ . Then $g ^ { ' } ( t ) = \frac { \phi ( t ) \phi ( t ) { - } ( \phi ( t ) { - } x _ { 0 } ) \phi ^ { ' } ( t ) } { \phi ^ { 2 } ( t ) } +$ $1 = 2 + \frac { t ( \phi ( t ) - x _ { 0 } ) } { \phi ( t ) } ,$ , where the second equality follows by the fact that $\phi ^ { \prime } ( t ) { = } - t \phi ( t )$ . Since $\varPhi ( t )$ is strictly increasing and <sup>/</sup>(t) is a strictly decreasing function of t when $t \ge 0 , g ^ { \prime \prime } ( t ) > 0$ for $t \geq 0$ . We also know that $t _ { j }$ is strictly increasing with $s _ { j }$ .

Comparing Eqs. (16), (17) and (18), we derive all the results for (a) – (c). □

Proof of Proposition 4.

$$
\begin{array}{c} \operatorname{Var} (Q _ {i} ^ {d}) = b _ {i} ^ {2} \operatorname{Var} (\mu_ {i} ^ {d}) = \frac {b _ {i} ^ {2} \tau_ {\delta} ^ {2}}{(\tau + \tau_ {\delta}) ^ {2}} \operatorname{Var} (\tilde {\theta} _ {i}) \\ = \frac {b _ {i} ^ {2} \tau_ {\delta} ^ {2}}{(\tau + \tau_ {\delta}) ^ {2}} \cdot \left(\frac {1}{\tau} + \frac {1}{\tau_ {\delta}}\right) = \frac {b _ {i} ^ {2} \tau_ {\delta}}{\tau (\tau + \tau_ {\delta})} \end{array}
$$

$$
\begin{array}{l} \operatorname{Var} (Q _ {i} ^ {m} | p) = b _ {i} ^ {2} \operatorname{Var} (\mu_ {i} ^ {m} | p) \\ \qquad = b _ {i} ^ {2} \left[ \frac {\tau_ {\delta} - (M - 1) \tau_ {p}}{\tau_ {+} \tau_ {\delta} + (M - 1) ^ {2} \tau_ {p}} \right] ^ {2} \left(\frac {1}{\tau} + \frac {1}{\tau_ {\delta}}\right) \end{array}
$$

Comparing equations yields $\operatorname { V a r } ( Q _ { i } ^ { d } ) { \geq } \operatorname { V a r } ( Q _ { i } ^ { m } | p )$ with equality holds when $M = 1$ . So $\mathrm { V a r } ( Q _ { i } ^ { d } ) { > } \mathrm { V a r } ( Q _ { i } ^ { m } |$ p) when $M { \ge } 2$

Note that $\mathrm { V a r } ( Q _ { i } ^ { m } | p ) = \frac { b _ { i } ^ { 2 } \tau _ { \delta } ^ { s } ( \tau + \tau _ { \delta } ) } { \tau [ ( ( M { - } 1 ) L ^ { 2 } \tau _ { X } + \tau _ { \delta } ) ( \tau + \tau _ { \delta } ) + ( M { - } 1 ) ^ { 2 } L ^ { 2 } \tau _ { X } \tau _ { \delta } ] ^ { 2 } } ,$ substituting Eq. (9) we can see it is a decreasing function of M. lim $_ { M  \infty } V a r ( Q _ { i } ^ { m } ) = 0$ . Clearly $\mathrm { V a r } ( Q _ { i } ^ { a } | \overline { { { \theta } } } ) { = } 0$ since full information sharing is imposed. □

Proof of Proposition 5. The expected supply chain profits under Structure $\mathrm { D } , \mathrm { A }$ , and M are

$$
\begin{array}{l} E \Pi^ {d} = (r - c) E \left[ \sum_ {i = 1} ^ {N} Q _ {i} ^ {d} \right] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\tau_ {i} ^ {d}}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) \mathrm{d} t \\ = (r - c) \left(a + b \mu - \frac {1}{T ^ {d}} t _ {d}\right) - \frac {r}{T ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) \mathrm{d} t \end{array}
$$

$$
\begin{array}{l} E \Pi^ {m} = E _ {p} \left\{(r - c) E \left[ \sum_ {i = 1} ^ {N} Q _ {i} ^ {m} | p \right] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\tau_ {i} ^ {m}}} \int_ {- \infty} ^ {- t _ {m}} \Phi (t) \mathrm{d} t \right\} \\ = (r - c) \left(a + b \mu - \frac {1}{T ^ {m}} E t _ {m}\right) - E _ {p} \left[ \frac {r}{T ^ {m}} \int_ {- \infty} ^ {- t _ {m}} \Phi (t) \mathrm{d} t \right] \end{array}
$$

$$
\begin{array}{l} E \Pi^ {a} = E _ {\bar {\theta}} ^ {-} \left\{(r - c) E \left[ \sum_ {i = 1} ^ {N} Q _ {i} ^ {a} | \bar {\theta} \right] - r \sum_ {i = 1} ^ {N} \frac {1}{\sqrt {\tau_ {i} ^ {a}}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) \mathrm{d} t \right\} \\ = (r - c) \left(a + b \mu - \frac {1}{T ^ {a}} E t _ {a}\right) - E _ {\bar {\theta}} ^ {-} \left[ \frac {r}{T ^ {a}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) \mathrm{d} t \right] \end{array}
$$

Therefore,

$$
\begin{array}{l} E [ \Pi^ {m} - \Pi^ {d} ] = (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {m}}{T ^ {m}}\right) \\ \qquad + \frac {r}{T ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) \mathrm{d} t - E _ {p} \left[ \frac {r}{T ^ {m}} \int_ {- \infty} ^ {- t _ {m}} \Phi (t) \mathrm{d} t \right] \\ \qquad > (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {m}}{T ^ {m}}\right) - E _ {p} \left[ \frac {r}{T ^ {m}} \int_ {- t _ {d}} ^ {- t _ {m}} \Phi (t) \mathrm{d} t \right] \\ \qquad > (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {m}}{T ^ {m}}\right) - \frac {r}{2 T ^ {m}} (- E t _ {m} + t _ {d}) \\ \qquad > \left(\frac {r}{2} - c\right) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {m}}{T ^ {m}}\right) \end{array}
$$

where the next to the last inequality follows from the condition min $\left( s ^ { m } , s ^ { d } \right) > \frac { r } { 2 }$ so that $- t _ { m } = \phi ^ { - 1 } \big ( 1 { - } \frac { s ^ { m } } { r } \big ) < 0$ and $- t _ { d } = \varPhi ^ { - 1 } \Bigl ( 1 - \frac { s ^ { d } } { r } \Bigr ) < 0$ . The last inequality requires that $\frac { r } { 2 } > c .$ By Eqs. (17) and (18), $\frac { 1 } { T ^ { d } } g ( t _ { d } ) \dot { = } a + b \mu = a + \stackrel { 2 } { b } E p =$ $\frac { 1 } { T ^ { m } } E g ( t _ { m } ) > \frac { 1 } { T ^ { m } } g ( E t _ { m } )$ . The inequality follows by the strict convexity of g(t) when $t \geq 0$ . Note that $g ( 0 ) \leq 0$ . For $\lambda = \frac { T ^ { d } } { T ^ { m } } < 1 .$ , we have $g ( t _ { d } ) > { \frac { T ^ { d } } { T ^ { m } } } g ( E t _ { m } ) > g \biggl ( { \frac { \breve { T } ^ { d } } { T ^ { m } } } E t _ { m } \biggr )$ . So $t _ { d } \ge \frac { T ^ { d } } { T ^ { m } } E t _ { m }$ . Therefore, $E [ I I ^ { m } - I I ^ { d } ] { > } 0$ . That is, $E I I ^ { m } > I I ^ { d } .$

$$
\begin{array}{l} E [ \Pi^ {a} - \Pi^ {d} ] = (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {a}}{T ^ {a}}\right) \\ \qquad + \frac {r}{T ^ {d}} \int_ {- \infty} ^ {- t _ {d}} \Phi (t) \mathrm{d} t - E _ {\overline {{\theta}}} \left[ \frac {r}{T ^ {a}} \int_ {- \infty} ^ {- t _ {a}} \Phi (t) \mathrm{d} t \right] \\ \qquad > (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {a}}{T ^ {a}}\right) - E _ {\overline {{\theta}}} \left[ \frac {r}{T ^ {a}} \int_ {- t _ {d}} ^ {- t _ {a}} \Phi (t) \mathrm{d} t \right] \\ \qquad > (r - c) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {a}}{T ^ {a}}\right) - \frac {r}{2 T ^ {a}} (- E t _ {a} + t _ {d}) \\ \qquad > \left(\frac {r}{2} - c\right) \left(\frac {t _ {d}}{T ^ {d}} - \frac {E t _ {a}}{T ^ {a}}\right) \end{array}
$$

By Eqs. (16) and (17), ${ \frac { 1 } { T ^ { d } } } g ( t _ { d } ) = a + b \mu = { \frac { 1 } { T ^ { a } } } E g ( t _ { a } ) >$ $\frac { 1 } { T ^ { a } } g ( E t _ { a } )$ . Since $\tau _ { i } ^ { a } { > } \tau _ { i } ^ { d } , T ^ { a } { > } \dot { T } ^ { d }$ . For $\lambda = \frac { T ^ { a } } { T ^ { a } } < 1 .$ , we have $\stackrel { \cdot } { g } ( t _ { d } ) > \frac { T ^ { d } } { T ^ { a } } g ( E t _ { a } ) > g \left( \frac { T ^ { d } } { T ^ { a } } E t _ { a } \right) $ . Therefore, $E I I ^ { a } { > } E I I ^ { d }$

By Lemma 2, lim ${ \ L } _ { M \to \infty } ^ { } E _ { X } \mu _ { i } ^ { m } = \operatorname* { l i m } _ { N \to \infty } \mu _ { i } ^ { a }$ ; and $\begin{array} { r } { \operatorname* { l i m } _ { M \to \infty } \tau _ { i } ^ { m } = \operatorname* { l i m } _ { N \to \infty } \tau _ { i } ^ { a } } \end{array}$ . The same forecasts yield the same expected supply chain profits. □

Proof of Proposition 6. Under REE, trading options neither increases retailers' macro prediction market profit nor affects their order quantity; the expected mean of retailers' profit is the same. However, by smoothing off the uncertain payoff function, the variance of wealth is decreased. It is a Pareto improving strategy for risk averse retailers. □

## References

[1] R. Anupindi, Y. Bassok, E. Zemel, A general framework for the study of decentralized distribution systems, Manufacturing and Service Operations Management 3 (4) (2001) 349–368.

[2] S. Ba, J. Stallaert, A.B. Whinston, Research commentary: introducing a third dimension in information systems design - the case for incentive alignment, Information Systems Research 12 (3) (2001) 225–239.

[3] D. Barnes-Schuster, Y. Bassok, R. Anupindi, Coordination and flexibility in supply contracts with options, Manufacturing and Service Operations Management 4 (3) (2002) 0171–0207.

[4] J.E. Berg, T.A. Rietz, Prediction markets as decision support systems, Information Systems Frontiers 5 (1) (2003) 79–93.

[5] A. Burnetas, P. Ritchken, Option pricing with downward-sloping demand curves: the case of supply chain options, Management Science 51 (4) (2005) 566–580.

[6] G.P. Cachon, Competitive supply chain inventory management, in: S. Tayur, R. Ganeshan, M. Magazine (Eds.), Quantitative Models for Supply Chain Management, Springer, 1998.

[7] G.P. Cachon, Supply chain coordination with contracts, in: S.C. Graves, A.G. De Kok (Eds.), Handbooks in Operations Research and Management Science: Supply Chain Management: Design, Coordination and Operation, Elsevier Publishing Company, 2003, Ch. 6.

[8] G.P. Cachon, M. Fisher, Supply chain inventory management and the value of shared information, Management Science 46 (8) (2000) 1032–1048.

[9] F. Chen, Information sharing and supply chain coordination, in: S. C. Graves, A.G. De Kok (Eds.), Handbooks in Operations Research and Management Science: Supply Chain Management: Design, Coordination and Operation, Elsevier Publishing Company, 2003, Ch. 7.

[10] F. Chen, Z. Drezner, J.K. Ryan, D. Simchi-Levi, Quantifying the bullwhip effect in a simple supply chain: the impact of forecasting, lead times and information, Management Science 46 (3) (2000) 436–443.

[11] L. Eeckhoudt, C. Gollier, H. Schlesinger, The risk-averse (and prudent) newsboy, Management Science 41 (5) (1995) 786–794.

[12] M. Fan, S. Srinivasan, J. Stallaert, A.B. Whinston, Electronic Commerce and the Revolution in Financial Markets, Thomson Learning, 2002.

[13] V. Gaur, S. Seshadri, Hedging inventory risk through market instruments, Manufacturing and Service Operations Management 7 (2) (2005) 103–120.

[14] S.J. Grossman, On the efficiency of competitive stock markets when traders have diverse information, Journal of Finance 31 (1976) 573–585.

[15] S.J. Grossman, O.D. Hart, An analysis of the principal-agen problem, Econometrica 51 (1983) 7–45.

[16] F. Hayek, The use of knowledge in society, American Economic Review 35 (4) (1945) 519–530.

[17] J.C. Hull, Options, Futures, and Other Derivative Securities, Prentice Hall, Englewood Cliffs, NJ, 1993.

[18] M. Khouja, The single-period (news-vendor) problem: literature review and suggestions for future research, Omega 27 (1999) 537–553.

[19] A.S. Kyle, Market structure, information, futures markets, and price formation, in: G. Story, A. Schmitz, A. Sarris (Eds.), International Agricultural Trade: Advanced Readings in Price Formation, Market Structure, and Price Instability, Westview Press, Boulder and London, 1984.

[20] A.S. Kyle, Continuous auctions and insider trading, Econometrica 53 (1985) 1315–1336.

[21] M.A. Lariviere, E.L. Porteus, Selling to the newsvendor: an analysis of price-only contracts, Manufacturing and Service Operations Management 3 (4) (2001) 293–305.

[22] H. Lee, P. Padmanabhan, S. Whang, Information distortion in a supply chain: The bullwhip effect, Management Science 43 (4) (1997) 546–558.

[23] H. Lee, S. Whang, The impact of the secondary market on the supply chain, Management Science 48 (6) (2002) 0719–0731.

[24] L. Li, Information sharing in a supply chain with horizontal competition, Management Science 48 (9) (2002) 1196–1212.

[25] H. Mendelson, T.I. Tunca, Liquidity in Industrial Exchanges, Working Paper, Stanford University, 2003.

[26] J.F. Muth, Rational expectations and the theory of price movements, Econometrica 29 (1961) 315–335.

[27] M. O'Hara, Market Microstructure Theory, Cambridge, Mass, 1995.

[28] V. Padmanabhan, I.P.L. Png, return policies: make money by making good, Sloan Management Review 37 (1) (1995) 65–72.

[29] R. Shiller, Macro Markets: Creating Institutions for Managing Society's Largest Economic Risks, Oxford University Press, 1993.

[30] M. Spann, B. Skiera, Internet-based virtual stock markets for business forecasting, Management Science 49 (10) (2003) 1310–1326.

[31] J.D. Sterman, Modeling managerial behavior: misperceptions of feedback in a dynamic decision making experiment, Management Science 35 (1989) 321–339.

[32] Z.K. Weng, Channel coordination and quantity discounts, Management Science 41 (9) (1995) 1509–1522.

[33] S. Whang, Y. Zou, The informational role of the secondary market on the supply chain, working paper, Stanford University, 2003.

[34] J. Wolfers, E. Zitzewitz, Prediction markets, Journal of Economic Perspectives 18 (2) (2004) 107–127.

Zhiling Guo is an Assistant Professor of Information Systems at UMBC (University of Maryland, Baltimore County). Her research interests include electronic commerce, financial markets, information economics, and supply chain management. She has a Ph.D. in Management Information Systems from the University of Texas at Austin.

Fang Fang is an Assistant Professor in the College of Business Administration at California State University at San Marcos. Her research interests include knowledge markets, financial markets, and network finance. She has a Ph.D. in Management Information Systems from the University of Texas at Austin.

Andrew B. Whinston is a Professor of Information Systems, Economics, Computer Science, and Library and Information Sciences, Hugh Roy Cullen Centennial Chair in Business Administration, and director of the Center for Research in Electronic Commerce at the University of Texas, Austin. He has published more than 300 papers in top-rated scientific journals and has recently co-authored the following books: The Frontiers of Electronic Commerce, Electronic Commerce: A Manager’s Guide, The Economics of Electronic Commerce, The Internet Economy: Technology and Practice, and Electronic Commerce and the Revolution in Financial Markets.
