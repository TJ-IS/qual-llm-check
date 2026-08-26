---
otero_id: 21079
otero_key: "ACUGBECD"
title: "Transaction risk in electronic commerce"
authors: "J.Christopher Westland"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(02)00010-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Transaction risk in electronic commerce

J. Christopher Westland\*

Department of Information and Systems Management, The Hong Kong University of Science and Technology, Clear Water Bay, Kowloon, Hong Kong SAR, China

Accepted 28 November 2001

## Abstract

Electronic commerce business models can add value by elimination of control and risk-bearing borne by channel intermediaries. But such markets may be less robust encouraging risky behavior. We explore a model of transaction risk in the migration from broker-mediated to electronic markets. The research finds that: (1) the risk of falsely accepting ‘bad’ orders is the critical risk measure for optimal control choice; (2) control policies and operational policies must be established simultaneously; (3) optimal control choice is strongly influenced by risk preferences; (4) at the margin, the decrease in risk from an additional increment of control is proportional to the market’s transaction volume; and (5) the discretionary budget sets the upper limit to control. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Electronic market structure; Accounting control; Transaction risk; Network

## 1. Transaction risk in markets

This paper provides a model for examining the importance of properly controlling transaction risk in electronic commerce. The paper addresses the question ‘‘what level of managerial control is required to reliably assure that payment and services will be rendered, goods delivered, and quality will be adequate.’’

Transaction risk results when markets fail to provide one or more of these when processing a transaction. Controls are subsystems that limit the frequency or magnitude of damage from failed transactions. This paper assumes that control is applied at the order level and draws conclusions about the level of risk and control required to provide a viable market.

Control of transaction risk in electronic commerce has become important because electronic commerce often adds value over its physical counterparts by allowing high transaction volumes at significant operating economies, but at the cost of less flexibility, robustness and control over risk, due to the loss of human channel intermediaries (brokers) in physical markets, usually relegating them to digital surrogates, or just transmission bandwidth. The problem has been highlighted in the recent U.S. Federal Bureau of Investigation inquiry into whether rings of shill bidders on eBay have committed fraud by bidding up the prices of one another’s online auction offerings [3]. The problem is considered widespread in Web-based auctions.

The control of transaction risk is of increasing concern as electronic markets become pervasive.

Electronic markets discard many broker-based controls inherent in traditional markets. The brokerage function has been especially important in high-volume markets such as stock exchanges. The broker’s agency<sup>1</sup> relationship with the trader allows securities markets to operate at high capacity with high reliability and low risk. In these markets, monitoring of individual transactions is transferred to many individual brokers, leaving the market to concentrate on matching orders.

In U.S. securities markets, controls are highly developed with several stages of indemnification. Individuals do not trade directly in these markets, but must trade through brokers who guarantee to the market that the individual can deliver goods or services, and that settlement can be made [2]. The broker may engage a clearing agent on the market floor to assure the broker that buy and sell orders will be matched. The clearing agent is indemnified by a clearinghouse, which assures his or her performance.

Counterparts to the brokerage function appear in markets for many non-financial goods and services. Food, for example, is sold by grocery stores that are responsible for purchase, delivery, and assurance of quality and freshness. Liquidity and matching demand with supply are particularly important with perishables. Building contractors procure subcontractors who provide specialized labor for construction as well as assurances that a construction project will be completed properly, on-time and within budget.

To assure that brokers can effectively control transaction risk, securities markets set minimum earnings and capital requirements for firms that list their securities on their exchanges, and monitor these brokers extensively. Exchanges that have set slack listing requirements—in recent history the Denver Exchange and the Vancouver Exchange are examples—have seen their reputations erode, and have watched their traders move elsewhere to conduct business.

Markets for goods and services over the past decade have invested significantly in automation of various market components through electronic data interchange and other technologies.<sup>2</sup> Without automation, markets are constrained to operate at the speed of their human facilitators—frequently too slow for complex or high-volume market services. In order to speed up transaction processing, traditional markets may be stripped of all but market matching functions, and other functions dispersed to brokers, clearing houses and similar operations.

Electronic markets have naturally focused on the particular services that are well suited to technology— matching and information dissemination. Much of design has been ad hoc-based more on what technology can do rather than what technology needs to do to provide an efficient, reliable market. There is little research on design to guide appropriate investment [3].

Electronic markets generally assume a direct information link with buyers and sellers—e.g., through VDTs, television sets or kiosks. The structure and implications of this direct linkage have been discussed extensively in the prior literature, e.g., in Refs. [1,2,4 – 7,11,14,15], and Ref. [12]. Such an architecture eliminates broker control or risk-bearing, and relegates transaction risk control to surrogates built into the electronic market systems. Being software algorithms, surrogate broker systems are not likely to be perfect (or necessarily even close) substitutes for human brokers. Brokers can maintain personal contact with customers, using intuition, experience and judgment to winnow good business from bad. Thus, stakeholders in electronic commerce systems should be interested in the cost of increased transaction risk, and prospects for its control.

The subsequent analysis examines risk-bearing and control as markets evolve from broker-mediated to electronic. Section 2 explores the contrasting architectures of broker-mediated and electronic markets. Section 3 presents a formal model of supply and demand for market services. Section 4 discusses risk assessments by market participants. Section 5 computes the optimal control level for a linear model of supply and demand with Gaussian uncertainty. Section 6 draws general conclusions on requirements for control as markets relinquish broker-based controls in their move to automate.

![](/api/attachments/ACUGBECD/fulltext/images/0a84556ae994ff85860ca69ef86f29d0c848dc487ca83a4d1cd26d55f1dad014.jpg)  
Fig. 1. Schematic of a brokered market.

## 2. Transaction risk in brokered and electronic markets

In this research, we assume that the broker-market community is responsible for managing its own internal operations, and ultimately for providing an adequate level of service and control over transaction risk. This risk is ultimately borne by traders — the buyer – seller community — they are the primary, but not sole beneficiaries, of control over transaction risk.

This research adopts a simple schematic of market transactions. Goods or services are bought and sold by placing orders in the market. Orders to sell a good or service have an ask price; orders to buy a good or service have a bid price. Order flows in a brokered market are depicted in the schematic in Fig. 1; order flows in an electronic market are depicted in Fig. 2.

Responsibility for rejecting risky business in the brokered market lies with humans, possibly supported by automation; software and automated mechanisms are responsible for rejecting risky business in an electronic market. Brokers and markets control risky business through procedures that allow ‘‘good’’ orders to be discriminated from ‘‘bad’’ or ‘‘risky’’ orders. Risk, for the purposes of this model, was defined previously as arising from the buyer receiving goods or service of at a quality less than expected; the seller not receiving full payment; or the transaction not being initiated or completed within a reasonable expanse of time. To couch risk in economic terms, loss from these exposures must be combined with probability of exposure. This is the subject of subsequent section.

Dichotomization of orders into ‘‘good’’ and ‘‘bad’’ (where there is insufficient evidence to gauge their true qualities) is the theme of the Neyman–Pearson statistical framework.<sup>3</sup> Each order transaction is tested against the hypothesis that it is ‘‘good’’ (i.e., of acceptable risk) and a decision is made whether to forward the order for matching in the market, or reject it as being ‘‘bad’’ (i.e., not ‘‘good’’) That decision may be right or wrong — Table 1 shows the standard 2  2 matrix of possible outcomes.

The order source is exogenous to the market, and is determined by seller and buyer preferences. In this case broker risk-bearing is captured in a- and b-risks:<sup>4</sup>

$$
\alpha = P r [ \text { type   I   error } ]
$$

$$
= P r [ \text { good   orders   are   turned   away } ]
$$

$$
\beta = P r [ \text { type   II   error } ] = P r [ \text { bad   orders   are   accepted } ].
$$

The a-risk of falsely turning good orders away is a cost to the potential seller or buyer and lowers order volume and liquidity of the market. The b-risk of falsely accepting bad orders is of greater concern to buyers and sellers because they are likely to be more concerned when a market systematically accepts bad business. Type b-risk damages the reputation of the market, and deters potential buyers and sellers from participating in the market on future transactions. The problems arising from bad orders must also be dealt with ex posteriori, presenting options that are almost always more expensive than rejecting bad orders. There are also likely to be liquidity effects from the choice of a- and b-risks—e.g., a-risk would reduce revenue both directly through reduced order flow and subsequently through reduced liquidity could further reduce order flow. This paper concentrates only on the risk/reliability effects, and leaves questions of risk induced changes in liquidity to future research.

![](/api/attachments/ACUGBECD/fulltext/images/a6ce854b1595c10c50918391f9076142538d81b25bfbd5f217a90eb136827c2e.jpg)  
Fig. 2. Schematic of an electronic market.

A broker or market would like to operate so that a = b = 0. But this is impossible for an scantily understood, exogenously determined order flow, within the constraints of any finite control budget. Thus, the broker-market community must trade positive levels of a- and b-risks against each other. The trade-off between a- and b-risks will be determined by the brokermarket community’s willingness to pay to avoid either type of risks, constrained by the budget, and the efficiency of systems for risk monitoring.

Consider the effects of a conversion from a brokermediated market to an electronic market summarized in Table 2.

## Table 1

Decision outcomes in determining good and bad orders

<table><tr><td></td><td>Order accepted</td><td>Order rejected</td></tr><tr><td>The order actually constitutes “good” business</td><td>correct decision</td><td>type I error</td></tr><tr><td>The order actually constitutes “bad” business</td><td>type II error</td><td>correct decision</td></tr></table>

When order risk is ignored, an electronic market provides obvious benefits—operating costs are lower (because of reduced human effort) and accessibility to market and speed of transaction processing are likely to improve significantly once human brokers are out of the loop. Ceteris paribus, demand for market services should increase.

Obviously, new risks arise as broker-agents acting on behalf of buyers and sellers disappear from the markets in which they trade. For example, the electronic auction system AUCNET for used cars in Japan

When transaction risk<sup>5</sup> is factored in, some if not all of this benefit may be lost. Higher risk drives buyers and sellers away. This effect is non-linear — a small amount of risk is tolerable, but beyond a certain critical levels, most buyers and sellers will rapidly leave the market. In addition, the mix of traders may change, with speculators and other liquidity providers favoring markets with certain risk characteristics. The market bears the onus, ex post, of figuring out what to do when buyers or sellers default on an obligation, when fraudulent information is provided, or in other risky situations. Buyer demand drops in a risky market. The demand curve shifts down: buyers are willing to pay less for a given quantity of good or service, not because of qualitative changes in the good or service, but entirely because of market characteristics [13].

Table 2  
Consequences of a shift from broker-mediated to electronic markets

<table><tr><td></td><td>Broker-mediated markets</td><td>Electronic markets</td><td>Demand price shift</td><td>Supply price shift</td></tr><tr><td>Transaction (Operating) Costs</td><td>High</td><td>Low</td><td>None</td><td>Significantly lower</td></tr><tr><td>Risk Level</td><td>Low</td><td>Moderate to High</td><td>Lower</td><td>Higher</td></tr><tr><td>Accessibility of Market</td><td>Difficult to Moderate</td><td>Very High</td><td>Higher</td><td>None</td></tr><tr><td>Speed of Transaction Processing</td><td>Slow to Moderate</td><td>Very High</td><td>Higher</td><td>None</td></tr></table>

only lets newer cars to be traded. The quality risks associated with older cars are difficult to control through any sort of cost-effective inspection process. The potential for ‘‘lemons’’ to sully the reputation of the entire market reputation is sufficient for AUC-NET’s management to have decided not to impose this market-centric (since the market can easily filter car transactions by age of the car) risk on their dealer – traders [8 – 10,16].

Controlling risk imposes a cost on the market, and higher risk implies higher marginal costs of transaction processing, since control processes will be more active in high risk environments. This effect is accelerated by the fact that control and error correction are highly error prone themselves, and by the fact that poor market reputation tends to reinforce existing prejudices. Under exemplary conditions, the market system may be able to rectify the occasional error. But increasing numbers of defaults, frauds and so forth quickly swamp control systems, and can potentially bring a market to a halt. The marginal cost of control can be highly non-linear.

Fig. 3 shows how assessed risk $\rho ,$ stated as an arbitrary function of $\nsim$ and b-risks, is influenced by market automation. At all levels of a and $\beta ,$ assessed risk are likely to be higher in electronic markets than in traditional brokered markets. In electronic markets, layers of control over risky transactions have been removed on both the buyer and seller side.

## 3. Supply and demand for market services under risk

This section formalizes the concepts broached in the prior sections with transaction risk central to the analysis. Electronic markets will have inherently higher risk $\rho ,$ and inherently higher order processing capacity G than traditional brokered markets. Let demand be downward sloping and supply be upward sloping in quantity g of market services rendered. Assume that in addition to quantity of service, demand and supply depend on the assessed risk $\rho$ of the order transaction, which can be reduced by increasing the level of control $\scriptstyle \theta \in [ \theta _ { 1 } , \theta _ { 2 } ]$ over adverse events such as non-delivery, non-payment, failure to clear, and so forth. Let $g ( \theta )$ be a continuous schedule representing the additional number of orders that the market can process at control level h. This reflects the trade-off, with a control budget fixed in the short run, between tightly controlling risk in a few orders, or loosely controlling risk in a larger number of orders, thus<sup>6</sup> $g _ { \theta } < 0$ . Let $\begin{array} { r } { G ( \theta _ { 2 } ) = \int _ { \theta _ { 1 } } ^ { \theta _ { 2 } } g ( t ) \ d t } \end{array}$ dt be the total order processing capacity of the market over the range of control levels. Redefine these constructs through a normalized control level $\scriptstyle \zeta = [ ( G ( \theta ) ) / ( G ( \theta _ { 2 } ) ) ] \in [ 0 , 1 ]$ with schedule f(n) <sup>f</sup> Uniform [0,1] and total capacity of $\begin{array} { r } { F ( 1 ) = \int _ { 0 } ^ { 1 } g ( t ) \mathrm { d } t = 1 } \end{array}$

Let the marginal cost of control be $\kappa ( \boldsymbol { \xi } )$ . At the control margin, this is the opportunity cost of processing an additional order at a control level that is as high or higher than control level of any previously processed order. Budgets, labor constraints and alternative markets all influence the maximal level of control $\hat { \xi } ,$ which will be provided by a given broker-market community.

Buyers and sellers are not directly concerned with level of control. Rather, they are interested in the $\varnothing -$ and b-risks of transacting in the market, which is influenced by the level of control. The more good orders that are turned away, increasing a-risk, the lower the demand; the more bad business taken in, increasing b-risk, the worse the reputation of the market, and the lower the demand.

![](/api/attachments/ACUGBECD/fulltext/images/3ed9224f5c7af8b341dff7e9a3b64d7b0eb50118225554dc60e0f351cf0cabdd.jpg)  
Fig. 3. Shift in transaction risk from broker-mediated to electronic market.

If the market is efficient in the sense that actual risks are effectively communicated to buyers and sellers<sup>7</sup> then demand $\delta ( \rho , \eta )$ is a function of:

(1) risk $\rho ,$ which is a ‘‘bad,’’ thus there is utility in trading out of it; and

(2) the quantity of orders processed $\eta .$

Assume that $\eta { \in } [ 0 , 1 ]$ is normalized in the same fashion as $\xi ,$ and thus represents a proportion of the peak number of orders that can be serviced by the market. Market services will be provided to cover a proportion of orders $\eta$ determined by the maximal control level $\hat { \xi } .$

At the control margin, buyers and sellers will be willing to pay $\delta ( \rho , \eta )$ depending on risk $\rho = \rho ( \hat { \xi } ) =$ $\rho ( \alpha ( \hat { \boldsymbol { \xi } } ) , \beta ( \hat { \boldsymbol { \xi } } ) )$ with $\delta _ { \rho } { < } 0 , \delta _ { \eta } { > } 0$ and $\rho _ { \xi } { < } 0$ . These relationships depend on how actual risk $^ { ( \alpha , \beta ) }$ is mapped into assessed risk $\rho .$

Risk preferring buyers and sellers will be willing to incur high risk (perhaps in hopes of gaining high returns in a thinly traded market) and will complete transactions on the most risky orders. Slightly less risk preferring traders will not trade unless more control is implemented, and so on until relatively risk averse traders complete transactions at the minimum available level of risk $\rho ( \hat { \xi } )$ given the best available control level $\hat { \xi } .$ . The total proportion of orders that is cleared at best control level $\hat { \xi }$ will be:

$$
\eta = \int_ {\hat {\xi}} ^ {1} \mathrm{d} \rho (t) = 1 - \rho (\hat {\xi}).\tag{1}
$$

Control level $\hat { \xi } ^ { * }$ equilibrium will result in marginal prices:

$$
\delta (\rho (\hat {\xi} ^ {*}); 1 - \rho (\hat {\xi} ^ {*})) = \kappa (\hat {\xi} ^ {*}).\tag{2}
$$

The demand side of Eq. (2) is a function of the actual level of risk $^ { ( \alpha , \beta ) }$ thus the result of a mapping $( \alpha , \beta ) \to \rho \to \delta$ . The supply side depends directly on control level $\xi$ and the marginal cost j of achieving it. Completing the cycle, control technology maps control level in to actual risk $\xi \to ( \alpha , \beta )$ . The mapping of actual risk to the risk assessed for demand decisions $( \alpha , \beta ) \to \rho$ is discussed in Section $^ { 4 , }$ and the implications of a given control technology $\xi \to ( \alpha , \beta )$ are discussed in Section 5.

Eq. (2) giving equilibrium control level is meaningful only if $\kappa ( \boldsymbol { \xi } )$ is increasing faster than $\delta ( \xi ) _ { \cdot }$ implying the condition $\kappa _ { \xi } { > } \delta _ { \xi } { = } \delta _ { \rho } \rho _ { \xi } { + } \delta _ { \eta } \eta _ { \zeta }$ <sub>n</sub> around the neighborhood $\boldsymbol { \xi } = \boldsymbol { \hat { \xi } } ^ { * } ,$ . The broker-market community makes choices concerning the level of control $\xi$ and supply of service $\kappa ( \boldsymbol { \xi } )$ based on some objective. Spence (1975) and Westland (1992) suggest the surplus measure net value $\nu$ (in this case to the broker-market community) as an appropriate objective for such choices, where

$$
v = \int_ {0} ^ {\hat {\xi}} \int_ {0} ^ {\eta} \delta (\rho (s), t) d t - \kappa (s) d s\tag{3}
$$

for some quantity $\eta$ and maximal control $\boldsymbol { \xi } . ^ { 8 }$ Substitute $\eta = 1 - \rho ( \hat { \xi } )$ and note that $( \partial \nu ) / ( \partial \hat { \xi } ) = 0$ at the net value maximizing level of control $\hat { \xi } ;$ expanding

$$
\begin{array}{l} \frac {\partial \nu}{\partial \hat {\xi}} = \frac {\partial}{\partial \hat {\xi}} \\ \qquad \times \left[ \int_ {0} ^ {\hat {\xi}} \left[ \int_ {0} ^ {1 - \rho (\hat {\xi})} \delta (\rho (t), s) \mathrm{d} s - \kappa (t) \right] \mathrm{d} t \right] \\ \qquad = \delta (\rho (\hat {\xi}); 1 - \rho (\hat {\xi})) \frac {\partial (1 - \rho (\hat {\xi}))}{\partial \hat {\xi}} - \kappa (\hat {\xi}) \\ \qquad = 0. \end{array}\tag{4}
$$

Eq. (4) satisfies equilibrium condition (2) only where $[ ( \partial \rho ( \hat { \xi } ) ) / ( \partial \hat { \xi } ) ] = - 1$ . This is the only condition where both willingness to provide control coincides with willingness to pay for it and which maximizes the broker-market community’s net value. When $[ ( \partial \rho ( \hat { \xi } ) ) / ( \partial \hat { \xi } ) ] > - 1$ demand can still be increased to the benefit of the broker-market community. When $[ ( \partial \rho ( \hat { \xi } ) ) / ( \partial \hat { \xi } ) ] < - 1$ , there will be insufficient demand to cover costs of operations. This is a reasonable conclusion about control choice — i.e., control should be increased as long as the marginal decrease in preference for risk exceeds the marginal increase in control.

The relationship of control to risk appears linear, but is actually more complex. Control level $\xi$ is derived from a transformation of the original control metric $\theta ,$ which is in units of the original measurement. Since $g ( \theta )$ is a continuous schedule representing the number of orders that the market can process at control level h, $\begin{array} { r } { G ( \theta ) = \int _ { \theta _ { 1 } } ^ { \theta } g ( t ) \mathrm { d } t } \end{array}$ and $\scriptstyle \xi = [ G ( \theta ) /$ $( G ( \theta _ { 2 } ) ) ] { \in } [ 0 , 1 ]$ . Multiplying both sides of $[ ( \partial \rho ( \hat { \xi } ) ) /$ $\partial \hat { \xi } ] = - 1$ by $\bar { \partial } \hat { \xi } / ( \partial \hat { \theta } )$ gives first order condition:

$$
\frac {\partial \rho}{\partial \hat {\theta}} = \frac {\partial \hat {\xi}}{\partial \hat {\theta}} = - \frac {1}{G (\theta_ {2})} \frac {\partial G (\hat {\theta})}{\partial \hat {\theta}} = - \frac {g (\hat {\theta})}{G (\theta_ {2})}\tag{5}
$$

which is likely to be non-linear. Note that control choice $\hat { \xi }$ does not depend on choice of d or of $\kappa ,$ which are likely to be specific to the firms, markets, and circumstances in any particular case. Eq. (5) describes solely a technical constraint, which measures the market’s choice of control level in terms of buyers and sellers risk assessment. The next section investigates how buyers and sellers assess risk.

## 4. The assessment of transaction risk

This section describes how buyers and sellers arrive at a single assessed risk measure $\rho$ given a and $\beta .$ The realized values of $\mathscr { X }$ and $\beta$ are the product of control choice $\hat { \xi } , { ^ 9 }$ which requires data acquisition and decision making about orders. Where there is no information discriminating good orders from bad and control $\hat { \xi } = 0 ;$ implying that choice of the $^ { ( \alpha , \beta ) }$ vector is random. Mapping a against $\beta$ this implies a point on the line from $( \alpha , \beta ) { = } ( 1 , 0 )$ to (0,1). In contrast, perfect control $\hat { \xi } = 1$ would be based on perfect information about orders, and thus no risk—i.e., the point $( \alpha , \beta ) { = } ( 0 , 0 )$ . If the point $( \alpha , \beta ) { = } ( 0 , 0 )$ is not available, then the point $( \alpha , \beta ) { = } ( 1 , 1 )$ is also not available, because if one could be sure of making a mistake, then by doing the exact opposite one could be sure of making perfect decisions. By an extension of this argument, the choice of efficient decisions (in the sense that all available information is used) must be symmetric about the line from $( \alpha , \beta ) { = } ( 1 , 0 )$ to (0,1) because if it were not, one could always adopt a contrarian decision procedure to improve on the existing choices. Reduction in one type of risk necessarily leads to an increase in the other type, and thus the frontier of efficient decisions in concave to the origin.

The transformation r maps from the Neyman – Pearson risk vector $^ { ( \alpha , \beta ) }$ to a assessed risk measure $\rho _ { i } ;$ it determines the choice of $^ { ( \alpha , \beta ) }$ on the efficient frontier. Fig. 4 shows the iso-risk curves $\rho ( \alpha , \beta ) = \rho _ { i } ,$ which sketch out a control expansion path as control is increased and the efficient frontier curves toward the origin.

In practice, risk mapping is made with a variety of judgmental and ad hoc approaches. Choice of a specific approach in practice depends on the information available to discriminate between good orders (which should be accepted by the market) and bad orders (which should be rejected) in addition to the cost of making an error in accepting or rejecting an order. Ad hoc approaches are formalized by one of three widely accepted statistical approaches—fixed significance level, minimax, and cost-benefit approaches for selecting a and $\beta \colon$

![](/api/attachments/ACUGBECD/fulltext/images/ba51d813418b5700a57604024a61412584a7b1a98c21f6d3e3abd1767fe8812e.jpg)  
Fig. 4. Increasing control increases concavity of the efficient frontier.

( fixed significance level) Set a to a constant and minimize $\beta ;$ this is done where significance of a hypothesis test is fixed, and power is maximized. (minimax) Minimize the maximum of either a or $\beta .$ (cost-benefit) Minimize the total cost of risk.

Each selection process implies a specific assessed risk $\rho$ and a specific control expansion path. The following paragraphs argue that these three formal approaches encompass the ad hoc approaches used in practice, since each is a response to one of three levels of knowledge about the real world.

The first approach, setting a to a constant, is probably the most commonly encountered. For example, confidence bounds on hypothesis testing are typically set to $\alpha { = } 0 . 0 5$ . This is equivalent to forcing the price elasticity of a-risk to zero —i.e., dictating a fixed level of a-risk. Where $\mathrm { H } _ { 0 }$ sets some parameter to zero, this becomes a test of significance for some effect. It is the option chosen when there exists almost no information about the decision parameters.

In a market context, this selection process is likely to be sub-optimal, unless buyers, sellers and markets are truly indifferent to a. Setting a too high means the market rejects too many good orders, and loses too much revenue. Setting a too low invites bad orders into the market, which may foster a poor reputation and unnecessary losses to buyers and sellers. The approach forces a horizontal information expansion path at $\alpha { = } 0 . 0 5$ , and is inconsistent with any rational set of preferences.

A second approach minimizes the maximum of either $\nsim$ or b-risk. One may assume that in this situation, the decision-maker has some information about the null $\mathrm { H } _ { 0 }$ and alternative hypothesis $\mathrm { H } _ { 1 } ,$ since without this additional information, $\beta$ could not be computed. It is a simple approach to decision making that considers both a- and b-risks, but only addresses one at a time.

The third approach minimizes the expected cost of a- and b-risks. It assumes that the broker market community has knowledge of both hypotheses, as well as knowledge of the costs of a- and b-risks. $\operatorname { I f } p$ is the probability that a particular order to buy or sell is ‘‘good,’’ and $( 1 - p )$ that it is ‘‘bad’’ then the expected cost is $c _ { \alpha } \alpha p + c _ { \beta } \beta ( 1 - p ) = \rho ( \alpha , \beta )$ . This is shown in Fig.

5c for $c _ { \alpha } p = 2$ and $c \beta ( 1 - p ) = 1$ . Note that the steep angle of the indifference curves in Fig. 5c reflects the assumption of a significantly greater impact of b-risk on demand than of a-risk on demand from the buyer – seller community.

![](/api/attachments/ACUGBECD/fulltext/images/5feaf2617dd727bfcc8c4164e2526725293cf5e0006577923df4dd7052e2179c.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/b76eeb2b4b82a4ebc328e282365e322c76d1d34bec9f22423da721168b23ac20.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/3e8af54302473c137319133d187a127fdd8d5f53e27e4093bab52bbf0a805930.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/8c10fa872b3df8fd546fbe4066f7ae2c5af59ffceac14085b3a8e0c6bcd443f3.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/96beb3a3729ce2d727535c75e6d42b4abc764ea38296c421cd661f1d9efdda72.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/841666efd6d35fe79b7a40279ca665290e3c85d1ea09e5ef4777754ec909b657.jpg)  
Fig. 5. (a) a = 0.5; (b) minimax; (c) full cost-benefit.

Fig. 5c’s preference curves will always be straight lines. This can be shown through a straightforward argument. Assume that a decision-maker is indifferent between two points $( \alpha _ { 0 } , \beta _ { 0 } )$ and $( \alpha _ { 1 } , \beta _ { 1 } )$ which are (tautologically) on the same iso-preference curve. Thus, one could randomize, choosing the first point with probability p and the second with probability $( 1 - \pi )$ . After randomization, the a-risk and b-risk are $( \alpha _ { 0 } \pi + \alpha _ { 1 } ( 1 - \pi ) , \beta _ { 0 } \pi + \beta _ { 1 } ( 1 - \pi ) )$ . Since $\mathscr { X }$ and $\beta$ are both probabilities, in the $( \alpha , \beta )$ space of decision making the decision-maker is indifferent to any point on the line sketched out by the arbitrary values of p between points $( \alpha _ { 0 } , \beta _ { 0 } )$ and $( \alpha _ { 1 } , \beta _ { 1 } )$ . This implies that the indifference curves must be straight lines in $^ { ( \alpha , \beta ) }$ space.

These three approaches formally define points in a continuum of ad hoc approaches probably used in practice, but which are less well articulated. The ‘‘cost-benefit’’ approach does not ignore one type of risk while choosing the other, and fits well a financial perspective. Unfortunately it may be difficult to implement in practice. Cost information for ad hoc decisionmaking is often not available. Even if it is in theory, it may be fugitive information<sub>U</sub>i.e., not available in the time period necessary for decision-making.

Use of fixed significance, minimax, and other incomplete mappings is testimony to the difficulty of acquiring precise information about the cost of processing good or bad orders. This is unfortunate given the ease and facility with which the costbenefit approach fits traditional linear accounting cost categories, and is consistent with various other reasons suggested for allocating costs, e.g., [17]. By the brief argument put forth, it is seen that the tradeoff between a-risk and b-risk in this approach are nearly linear, based on the unit costs of each type of error.

## 5. Optimal control in a linear model with Gaussian risk

This section examines the consequences of each of the prior equilibrium and risk assessment choices under the customary assumptions of linearity and Gaussian populations. Let demand for matching and order completion services offered by the market depend on quantity of service and transaction risk

$$
\delta (\rho , \eta) = \eta + m \rho\tag{6}
$$

where coefficient m emphasizes the comparative importance of service level to risk—higher m implies that transaction risk is more important to traders in the market. Let the marginal cost of provision of matching and order completion services increase linearly in $\hat { \xi } .$ ˆ ˆ ð7Þ

$$
\kappa (\hat {\xi}.) = \hat {\xi}.\tag{7}
$$

Substituting into equilibrium condition (2) shows that at equilibrium, risk is linearly proportional to control

$$
\rho (\hat {\xi} ^ {*}) = \frac {\hat {\xi} ^ {*} - 1}{m - 1}\tag{8}
$$

Transaction risk is reduced by collecting more information about a potential order to be matched and completed in the market, and improving the probability of correctly deciding whether or not to reject it. At the net value maximizing control choice $\hat { \xi } ,$ $m = 0$ and demand becomes insensitive to risk. The returns for collecting more information about an order must be diminishing, since $\nsim$ or b-risk cannot decrease below zero but one can collect additional information forever.

Assume a Gaussian population where $\mu$ and r are mean and standard deviation, respectively, let $\hat { \xi }$ be in proportion to the sample size that, in turn, provides an indication of control budget and effort.

Let the risk level $\rho$ depend on two choice parameters: (1) the cut-off, or discriminant, variable z that discriminates between good and bad orders, and (2) the control level $\xi$ that reflects the effectiveness of resources spent limiting the risk, and is determined by the economic decision process specified in the prior section. Each set of choice values $( \xi , z )$ determines aand b-risks; $\mathrm { i . e . , }$ there exists a transformation which maps $( \xi , z ) \longrightarrow ( \alpha , \beta )$ . Thus, there is an implicit risk associated with each set of choice variables (n,z).

Where control level is relatively difficult to change, e.g., when risk arises externally, and is only poorly controlled by managerial decisions, choice variable z will determine the function $\rho ( \alpha , \beta )$ . In this case, z selects a single point on the frontier of efficient decisions.

![](/api/attachments/ACUGBECD/fulltext/images/64638f510099dc7e7144a4b5cb48193b46c42cf45a26d2bde6c4bf9e76dc306d.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/b731c600864735d0cde18f802db072ceaadfddc52331611a944b9ae02c1007e0.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/d98f4a5864a3d0cbc467292b151b6abe9061c70697b16a17b089160ec76a8a35.jpg)  
Fig. 6. (a) $\rho ( z )$ where $m = 0 . 5$ and $\rho = \beta | { \boldsymbol { \alpha } } = 0 . 0 5 ;$ (b) $\rho ( z )$ where $m = 0 . 5$ and q = min(b,a); (c) $\rho ( z )$ where $m = 0 . 5$ and $\rho = \alpha + 2 \beta$

![](/api/attachments/ACUGBECD/fulltext/images/9e604fb15ce28e778884d8a158cba188be2aca5047801d0924b111092e789086.jpg)  
Fig. 7. a and b for $\mu _ { 0 } = 0 , \mu _ { 1 } = 1$ and $\sigma = 1 0 0$

The mapping $( \xi , z ) \longrightarrow ( \alpha , \beta )$ assuming a Gaussian population with $\mu$ and $\sigma$ is

$$
\alpha (\hat {\xi}, z \mid \mu , \sigma) = \sqrt {\frac {\hat {\xi}}{\sigma^ {2} 2 \pi} \int_ {z} ^ {\infty} \exp \left[ - \frac {(t - \mu) ^ {2}}{2 \sigma^ {2} / \hat {\xi}} \right] \mathrm{d} t}\tag{9a}
$$

$$
\beta (\hat {\xi}, z \mid \mu , \sigma) = \sqrt {\frac {\hat {\xi}}{\sigma^ {2} 2 \pi} \int_ {- \infty} ^ {z} \exp \left[ - \frac {(t - \mu) ^ {2}}{2 \sigma^ {2} / \hat {\xi}} \right] d t}\tag{9b}
$$

The mapping $( \alpha [ \xi , z ] , \beta [ \xi , z ] ) \to \rho$ may be accomplished using the fixed significance, minimax or costbenefit approaches delineated previously. The mappings are computed in a Mathematicak script.

Consider the situation where $\mu _ { 0 } = 0 , \ \mu _ { 1 } = 1$ and $\sigma = 1 0 0$ reflecting the relatively high dispersion of market statistics. Risk $\rho$ is a unique function of parameter z as shown in Fig. $6 \mathbf { a } .$ , b and c. As a consequence, z chooses the level of risk preference from the efficient frontier in this example, and thus determines the tradeoff between a- and b-risk.

(a)  
![](/api/attachments/ACUGBECD/fulltext/images/e2e1aa86f01a31d0e6f78c1b5931f0c7d24878cdde466d29fb48423c507be0f5.jpg)

(b)  
![](/api/attachments/ACUGBECD/fulltext/images/cb239265a80df6dcb1c50c15ed7b848d002355141d60d3122eee1c779afda612.jpg)  
(d)

(c)  
![](/api/attachments/ACUGBECD/fulltext/images/ce723be4c79c0d55a3b400cfa625bf397856d1dc752b14c1afee54a170859533.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/dd3a79d28bf71aa74a8554a622f3d7fb06bbe07846db285fff68dd10a514ae83.jpg)  
(f)

(e)  
![](/api/attachments/ACUGBECD/fulltext/images/ab6870ff4211616d7fca46f98ef66e8f616d97fd216d5ee6d8374eeecd6b1f96.jpg)

![](/api/attachments/ACUGBECD/fulltext/images/f1b36a6c0ba3016c760ffdabe3760bd15778bbe62525fc02a1f9540d6cdd9c50.jpg)  
Fig. 8. (a) Equilibrium values $\hat { \xi } ^ { * }$ where $m = 0 . 5$ and $\rho = \operatorname* { m i n } \beta | \alpha = 0 . 0 5 ;$ (b) equilibrium values $\hat { \xi } ^ { * }$ where $z = 3$ and $\rho = \operatorname* { m i n } \beta | \alpha = 0 . 0 5 ;$ (c) equilibrium values $\hat { \xi } ^ { * }$ where $m = 0 . 5$ and $\rho = \operatorname* { m i n } _ { . } ( \alpha , \beta ) ;$ (d) equilibrium values $\hat { \xi } ^ { * }$ where $z = 3$ and $\rho = \operatorname* { m i n } ( \alpha , \beta ) ; ( \mathbf { e } )$ equilibrium values $\hat { \xi } ^ { * }$ where $m = 0 . 5$ and $\rho = \alpha + 2 \beta ; ( \mathrm { f } )$ equilibrium values $\hat { \xi } ^ { * }$ where $z = 3$ and $\rho = \alpha + 2 \beta .$

Parameter z has a straightforward interpretation in selection of a- and b-risks as shown in Fig. 7, which graphs a series of parametric plots for $\hat { \xi } = 1 0 , 1 0 0 , 2 0 0$ 4 and 300 on parameter z for this function with $\mu _ { 0 } = 0$ (indicating a ‘‘good’’ order), $\mu _ { 1 } = 1$ (indicating a $\mathrm { \Delta ^ { 6 6 d } \vec { \Omega } } ^ { 5 6 }$ order) and $\sigma = 1 0 0$ . Note that the z parameter chooses a particular $^ { ( \alpha , \beta ) }$ vector from the efficient frontier— small z favors smaller b-risk and larger a-risk; a large z favors the opposite. The two parameters, $\hat { \xi }$ and z, jointly select a given risk vector $^ { ( \alpha , \beta ) }$ . Parameter z is preferred to $\rho$ in graphing choice decisions because it is a choice parameter, whereas $\rho$ is an outcome of choice of $\boldsymbol { \cdot } \boldsymbol { \hat { \xi } }$ and z jointly.

Consider the equilibrium $\hat { \xi } ^ { * }$ values where $\rho$ is decided upon by a significance test $\rho = \beta | \alpha < 0 . 0 5 .$ The two demand parameters which have not been fixed at this point are z and m; the selection of $\hat { \xi } ^ { \ast }$ is shown in Fig. 8a fixing $m = 0 . 5$ and Fig. 8b fixing z = 3.

Note that a large z favors a larger b-risk (since arisk is fixed) and thus requires at equilibrium proportionately less expenditure on control, implying smaller $\hat { \xi } ^ { \ast }$

On the other hand, as overall risk becomes more important as reflected in larger $m ,$ then keeping b-risk at an acceptable level, given that a-risk is fixed requires rapidly expanding expenditure on control, implying significantly larger $\hat { \xi } ^ { * }$

In contrast to choice with a fixed significance level, the minimax approach requires decreasing control at equilibrium up to the point that $\alpha = \beta ,$ and then equilibrium control level $\hat { \xi } ^ { * }$ must increase.

Fig. 8d indicates that where m is small, or even negative, i.e., where buyers and sellers are actually risk preferring, multiple equilibria exist with an unstable middle equilibrium between $m { = } ( - 2 . 5 , 1 )$ . Where risk is to be avoided, a fairly high and stable level of control is required for equilibrium.

Immediately apparent from inspection of Fig. 8e is that at all levels of z the required control level is less than half of that for the other two approaches. This results from setting, i.e., the relatively modest importance that risk has in determining demand for market services. Fig. 8f shows that control level is quite sensitive to $m ,$ , more than in the other two approaches. Larger z requires less control, because b-risk in this example is twice as important as a-risk, $\mathrm { i . e . , } \rho = \alpha + 2 \beta .$

The cost-benefit approach outperforms the fixed significance approach in this example, yielding net value maximizing equilibrium risk levels which are about half of those for a fixed significance level $\alpha { = } 0 . 0 5$ for the same control level. Constraining a to.05 or to any fixed value will force the buyers and sellers to incur a cost that is always greater than $c _ { \alpha } \alpha .$ Fig. 9 shows that the total cost of risk $c _ { \alpha } \alpha + c _ { \beta } \beta$ to buyers and sellers of cost-based decisions will always be lower than the total cost of decisions requiring a to be fixed.

![](/api/attachments/ACUGBECD/fulltext/images/85a162e544682d2642b2001b2456bec6ad109797e5b7d5342ea087fb150c6359.jpg)  
Fig. 9. Full cost-benefit versus fixed significance decisions.

The levels of a- and b-risks, which yield a given $\rho$ with full cost information (Fig. 5c), will be greater than or equal to those for a minimax decision (Fig. 5b), which in turn will be greater than or equal to that for a fixed significance level (Fig. 5a). Since $\rho$ depends on $\xi$ through a and $\beta ,$ this implies that for a given $\xi _ { 0 } .$

$$
\rho_ {\text { cost - benefit }} (\xi_ {0}) \geq \rho_ {\text { minimax }} (\xi_ {0}) \geq \rho_ {\text { fixed   significance }} (\xi_ {0}).
$$

Note that since risk $\rho$ is undesirable, these values become negative.

## 6. Conclusions: the elements of optimal control over transaction risk

The previous results can now be consolidated into a set of five results that guide control choice as markets migrate from brokered to electronic systems. These results provide insight into electronic commerce systems design, an important consideration as operating cost reductions and attractive novel features make electronic commerce increasingly effective in reaching new customers.

(Conclusion 1) b-risk directly increases buyers’ and sellers’ risks of participating in the market. As a result, b- risk of falsely accepting ‘‘bad’’ orders is the critical risk measure for optimal control choice.

Exposures arising from bad orders must also be dealt with after a loss — this is almost always more expensive than rejecting bad orders since the buyer or seller has already suffered the crime. Small value orders for goods and services may be able to support larger quantities of bad orders (and the consequent higher b-risk), but large value items will not be traded in risky markets. To date, electronic markets have had the greatest success in trading low valued goods — e.g., freeware and shareware where marginal cost of the good is close to zero. This is likely a reflection of significantly higher b-risk in existing electronic markets.

At certain critical masses of bad orders, two additional effects (outside the scope of this paper) impact buyer – seller participation in the markets: reputation effects, and reduced network externalities as participants leave the market. Poor reputation tends to reinforce itself, and will drive some of the more riskaverse participants away. This lowers the total participation in the market, and thus makes it less liquid forcing longer delays in clearing orders. Thus, it is less attractive for reasons independent of risk. These latter influences reflect the reduction in the market’s network externality.

The move away from brokered markets toward integrated electronic commerce systems increases $\beta -$ risk. Electronic commerce, in contrast, favors direct information links which circumvent broker control or risk-bearing. Surrogate risk monitoring systems in electronic markets cannot be perfect (or necessarily even close) substitutes for human brokers. Real brokers can maintain personal contain with customers, using intuition, experience and judgment to winnow good business from bad. This systematic lowering of control in electronic commerce is a trade-off for their faster, cheaper transaction processing.

The discriminant choice variable z discriminates between good and bad orders, and through mapping $( \xi , z ) \longrightarrow ( \alpha , \beta )$ determines the level of a- and b-risks. If control levels are relatively difficult to change, which is often the case, z alone selects a single point $^ { ( \alpha , \beta ) }$ on the frontier of efficient decisions. From this perspective, the a-risk of falsely turning good orders away is significantly less important than b-risk in the control of transaction risk. It does not directly influence risk of participating in the market. It does influence long run demand for market services, because it lowers order volume and liquidity making the market less attractive to the potential seller or buyer. It does not lead to poor reputation, nor are there operational problems that impose a cost to the market or its participants. There is always be a certain amount of business that will be rejected, even where most of that business is good business. If this good business is significant, other broker-market communities will accept it and this can lead to a significant loss of revenue. Since the move to electronic commerce is also a move to high-volume, low-margin retailing, the network externality is significant and indirect effects of lower volume can significantly lower demand for market services.

The analysis showed that the b-risk of falsely accepting bad orders is most important. b-Risk directly increases buyers and sellers risk of participating in the market. It is likely to be important when large sums of money are at stake, and any gambles in the market are potentially ruinous. Discriminant parameter z should therefore be chosen to minimize $\beta -$ risk.

Note that the ability to efficiently control transaction risk depends on the existence of internal accounting systems that can effectively gather data on, and compute:

(i) the ‘‘price’’ traders are willing to pay to avoid aand b-risks (for use in computing ‘‘cost-benefit’’ risk mapping),

(ii) values for h the actual measure of control, and

(iii) the influence of control level on order processing, given by $g ( \theta )$ and capacity $G ( \theta _ { 2 } )$ .

(Conclusion 2) Control policies (which determine control level n) and operational policies (which determines the discriminant function’s cut-off value z) must be established simultaneously. Setting one policy independently of the other results in unreliable risk assessments and poor control.

The control level $\xi$ reflects the effectiveness of resources, at marginal cost $\kappa ( \boldsymbol { \xi } )$ , spent limiting risk. Fig. 6a–c shows that $\xi$ multiplies the effect on risk of the discriminant choice variable z on risk $\rho . \operatorname { I f } \left( \alpha , \beta \right)$ $ \rho$ by ‘‘fixed significance level’’ approaches, then the multiplier is some monotonic function with range $^ { ( 0 , 1 ) }$ If $( \alpha , \beta ) \to \rho$ by ‘‘minimax’’ approaches, then the multiplier is still in the range (0,1) but has a peak, and will be significantly smaller than the ‘‘fixed significance level’’ multiplier.

If $( \alpha , \beta ) \to \rho$ by ‘‘cost-benefit’’ approaches, then the multiplier is some monotonic function with range $( 0 , \infty )$ reflecting the inclusion of cost figures which may substantially exceed 1. This approach yields a ‘‘price’’ of risk, in contrast to the other two approaches are probabilistic functions which favor either a and $\beta$ given a particular situation.

In any case, the conclusion that should be drawn from elements 1 and 2 is that control policies (which determine $\xi )$ and operational policies (which determine z) must be established concurrently. Establishing one policy without the other will produce unreliable risk assessments. The effect of each policy is multiplicative, and thus not easily separated from the effect of the other policy. An exception to this conclusion occurs when control level is relatively difficult to change, e.g., when risk arises externally, and is only poorly controlled by managerial decisions. Then risk $\rho$ will depend entirely on the discriminant variable z.

(Conclusion 3) Optimal control choice is strongly influenced by the preferences of traders for risk (i.e., risk aversion or risk preference). As new traders enter the market, and as former traders leave, optimal control choice may change substantially.

Traders have a demand curve for a particular level of controls, mapped $( \alpha , \beta ) \to \delta ( \rho , 1 - \rho )$ . This may be perceived as an alternative measure of risk aversion. The prior discussion of Fig. 8a–f explored the impact of trader risk aversion. The ‘‘fixed significance level’’ approach led to control choice that was overly sensitive to the risk aversion of traders. The ‘‘minimax’’ approach tended to arbitrarily favor either a- or b-risk in different ranges of the parameters, leading to multiple, conflicting control choices. The ‘‘cost-benefit’’ approach avoided the objections of the other two models by more completely incorporating information about $\nsim$ or b-risk, but required the collection of information on risk and control preferences of traders.

Though this is desirable, trader risk preferences are exogenous to the market, and are likely to be costly to ascertain in the process of setting market policy.

The marginal increase in the control $\partial \hat { \xi }$ , i.e., the normalized fraction of market capacity which can be processed at a given control level, is proportional to the marginal decrease in risk $\partial \rho$ at net value maximizing equilibrium, i.e., $\partial \boldsymbol { \rho } = - \partial \boldsymbol { \hat { \xi } }$ . This relationship is simple and intuitive but applies to two derived variables. Control $\partial \hat { \xi }$ depends on the derived $\hat { \xi }$ which is known only through $\theta , g ( . )$ , and maximum systems order processing capacity $G ( \theta _ { 2 } )$ . Risk $\partial \rho$ depends on discriminant function $z ,$ control level $\hat { \xi }$ and the approach used to map $( \alpha , \beta ) \to \rho$

Fig. 8a–f explored this equilibrium condition. Fig. 8a and b looked at the ‘‘fixed significance level’’ approach. For high values of m, i.e., as transaction risk becomes relatively more importance to traders in the market, the equilibrium levels of control accelerate to extreme heights. This suggests that optimal control choices under this approach would be volatile, and subject to the exogenous whims of traders in the market. While this may indeed be the case, it is difficult to set control policy with a decision model which demands vastly different levels of control expenditure $\kappa ( \boldsymbol { \xi } )$ from day to day as traders preferences change.

Fig. 8c and d looked at the ‘‘minimax’’ approach. The approach tends to arbitrarily favor either a- or $\beta -$ risk in different ranges of the parameters. But prior discussion emphasized the importance of b-risk to traders, while indicating that trading would be much less sensitive to a-risk. Worse, Fig. 8c indicates broad ranges of trader risk preference m in which the model suggests multiple optimal choice of marginal control expenditure $\kappa ( \boldsymbol { \xi } )$ . The ‘‘minimax’’ approach, though applicable in certain statistical decision problems, furnishes unrealistic and ambiguous options for control choice. For these reasons, it is not to be recommended as risk mapping model in control choice.

Fig. 8e and f looked at the ‘‘cost-benefit’’ approach. This approach provides control choices that are robust (monotonic and smoothly varying) in the parameter $m$ and choice variable z. It avoids the objections to the other two models. In addition, it provides an estimate of loss in $( 0 , \infty )$ , rather than a probability in (0,1), and thus bears more information about the choice.

This matters, since marginal control expenditure $\kappa ( \boldsymbol { \xi } )$ is likely to be smooth and monotonic increasing, and order processing $g ( \theta )$ volume at control level $\theta$ is likely to be smooth and monotonic decreasing. $\mathrm { A }$ smooth monotonic mapping $( \alpha , \beta ) \to \rho$ will yield robust choices for optimal control. Optimal control $\hat { \xi }$ yielding net value maximizing equilibrium $\partial \boldsymbol { \rho } = - \partial \boldsymbol { \hat { \xi } }$ is best realized through a cost-benefit assessment of risk.

(Conclusion 4) At the margin, the decrease in risk from an additional increment of control is proportional to the market’s transaction volume. Thus, a busy market, with a high volume of trading will benefit more from increased controls; conversely, thinly traded markets will find less need for controls over transaction risk.

The marginal decrease in risk $\rho$ is proportional to the marginal increase in the actual measured control $\hat { \theta }$ times the factor $g ( \hat { \theta } ) / \mathrm { G } ( \theta _ { 2 } )$ , i.e., the number of orders which can be processed at a given control level $\hat { \theta }$ divided by the market’s total ability to process orders at all control levels. The monotonic decreasing function $g ( \theta )$ reflects the trade-off between tightly controlling risk in a few orders, or loosely controlling risk in an larger number of orders. Optimal control will satisfy the restated equilibrium condition:

$$
\partial \rho / \partial \hat {\theta} = - g (\hat {\theta}) / G (\theta_ {2}).
$$

At the control margin, the incremental increase in risk from an additional increment of control is proportional to the order processing volume at that level of control. With some reservations, this result can be viewed as assigning a characteristic ‘‘packet’’ of risk to each order processed, and assuming that total risk is approximately additive (which will be true for very small probabilities). This conclusion provides a useful ‘‘rule of thumb’’ for risk assessment.

(Conclusion 5) The discretionary budget for spending on controls over transaction risk provides an upper limit to control which may limit optimal control choice. This budget is

$$
K (\theta) = \frac {1}{G \left(\theta_ {2}\right)} \int_ {0} ^ {\theta} \kappa \left(\frac {G (\theta)}{G \left(\theta_ {2}\right)}\right) g (\theta) d \theta .
$$

Marginal control expenditure $\kappa ( \boldsymbol { \xi } )$ must come out of a discretionary control budget $K ( \xi )$ which is typically fixed for a year. Let $K ( \theta )$ be the control budget stated in terms of the known measure $\theta ,$ and recall that the transformation from $\theta \longrightarrow \xi$ is $\xi = ( G ( \theta ) ) / ( G ( \theta _ { 2 } ) ) \Rightarrow$ $\theta = G ( \theta _ { 2 } ) G ^ { - 1 } ( \zeta )$ where $G ^ { - 1 }$ is the inverse function of $G .$ Then

$$
\begin{array}{c} K (\theta) = \int_ {0} ^ {\theta} \kappa \bigg (\frac {G (\theta)}{G (\theta_ {2})} \bigg) \mathrm{d} \frac {G (\theta)}{G (\theta_ {2})} \\ = \frac {1}{G (\theta_ {2})} \int_ {0} ^ {\theta} \kappa \bigg (\frac {G (\theta)}{G (\theta_ {2})} \bigg) g (\theta) \mathrm{d} \theta \end{array}\tag{10a}
$$

$$
\kappa (\xi) = \frac {\partial K (\theta)}{\partial \xi} = \frac {\partial K (G (\theta_ {2}) G ^ {- 1} (\xi)) .}{\partial \xi}\tag{10b}
$$

Eq. (10a) computes the budget for control at level $\theta ,$ given $G ( . )$ and j. Eq. (10b) provides entries for the right-hand side of the equilibrium Eq. (2) in terms of $G ( . )$ and a priori budget K.

The move from a broker-mediated to a fully electronic market holds the potential to dramatically increase processing volume and transaction risk. Thus, the costs and benefits of each of these factors have to be carefully weighed against each other. Increased processing volumes can induce network externalities, which lock traders into the market; but if volume comes at a cost of excessive $\beta \mathrm { - r i s k }$ , reputation effects may drive traders elsewhere. Since the incremental risk is proportional to order processing volume at a given level of control, network externalities from increased order volume must rise faster than risk if the move to electronic markets is not seen to be excessively risky. Perhaps the current hesitance of individuals to abandon mail order, television and public auctions in exchange for Internet commerce arises from order volume not increasing faster than risk. This may be a problem for some time, since optimal control choice can be highly sensitive to trader risk aversion, at the same time that information about trader risk aversion is difficult to collect.

Reputation and excessive b-risk can be limited by control processes and effective selection of orders— both are crucial to market success, and the influence of both is multiplicative. It is advisable that measurement and assessment of risk entail a full cost-benefit model, in order that control expenses not be overly sensitive to market risk tolerance.

Where the trading community is not currently using the cost-benefit approach, the research suggests that it should be willing to pay up to its current control expenditures to build or purchase an internal accounting system which can provide the data needed to control transaction risk. In light of this, formal computer algorithms for control, process modeling and accounting should become increasingly important over the next decade. The results of this research may be seen as imperatives for future market design, as well as conditions for choice between brokered and electronic commerce.

## References

[1] A. Barua, Information technologies and business value: an analytic and empirical investigation, Information Systems Research 6 (1) (Mar 1995) 3 – 23.

[2] E. Brynjolfsson, Does information technology lead to smaller firms? Management Science 40 (12) (Dec 1994) 1628 – 1644.

[3] E. Brynjolfsson, Information assets, technology, and organiza tion, Management Science 40 (12) (Dec 1994) 1645–1662.

[4] R.H. Coase, The Firm, the Market, and the Law, Univ. of Chicago Press, Chicago, 1988.

[5] V. Gurbaxani, Modeling vs. forecasting: the case of information systems spending, Information Systems Research 5 (2) (Jun 1994) 180–190.

[6] R.A. Kalakota, R.A. Balakrishnan, Document-centered information systems to support reactive problem-solving in manufacturing, International Journal of Production Economics 38 (1) (Mar 1995) 31 – 58.

[7] S. Kekre, Impact of electronic data interchange technology on quality improvement and inventory reduction programs: a field study, International Journal of Production Economics 28 (3) (Dec 1992) 265–282.

[8] C.F. Kemerer, C.M. Hess, Computerized loan origination systems: an industry case study of electronic markets hypothesis, MIS Quarterly 18 (3) (Sep 1994) 251 – 275.

[9] H.G. Lee, T. Clark, Impacts of electronic marketplace on transaction cost and market structure, Journal of Electronic Commerce 2 (1) (1997) 7– 22.

[10] H.G. Lee, T. Clark, Market process reengineering through electronic market systems: opportunities and challenges, Journal of Management Information Systems 13 (3) (Winter 1997) 113–136.

[11] H.G. Lee, J.C. Westland, S. Hong, The impact of electronic marketplaces on product prices: an empirical study of AUC-NET, International Journal of Electronic Commerce 4 (2) (Winter 1999 – 2000) 45 – 60.

[12] H. Lux, Company plans to trade its own stock on Web, Investment Dealers Digest 62 (10) (March 1996) 8.

[13] B.R. Nault, Adoption, transfers, and incentives in a franchise network with positive externalities, Marketing Science 13 (4) (Fall 1994) 412– 423.

[14] Reuters, http://www.reuters.com; FBI opens investigation into eBay bids, Jun 7, 2000.

[15] F.J. Riggins, T. Mukhopadhyay, The growth of interorganizational systems in the presence of network externalities, Management Science 40 (8) (Aug 1994) 984 – 998.

[16] K. Srinivasan, T. Mukhopadhyay, Impact of electronic data interchange technology on JIT shipments, Management Science 40 (10) (Oct 1994) 1291 – 1304.

[17] A. Warbelow, J. Kokuryo, AUCNET: TV auction network system. Harvard Business School Case Study, 9-190-001, (July 1989) 1 – 17.

[18] J.C. Westland, Congestion and network externalities in the short run pricing of information systems services, Management Science 38 (6) (July 1992) 992– 1099.

[19] J.C. Westland, assessing the economic benefits of information systems auditing, Information Systems Research 1 (3) (September 1990) 309 – 324.

[20] J. Zimmerman, The costs and benefits of cost allocations, The Accounting Review, (July 1979) 504–521.
