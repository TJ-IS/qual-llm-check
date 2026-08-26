---
otero_id: 5222
otero_key: "DYBMEF2C"
title: "An analytical approach to bundling in the presence of customer transition effects"
authors: "Seokjoo Andrew Chang; Giri Kumar Tayi"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An analytical approach to bundling in the presence of customer transition effects

Seokjoo Andrew Chang ⁎, Giri Kumar Tayi

School of Business, State University of New York at Albany, 1400 Washington Ave., Albany, NY 12222, United States

## a r t i c l e i n f o

Article history: Received 4 November 2008 Received in revised form 17 April 2009 Accepted 7 July 2009 Available online 15 July 2009

Keywords: Decision making/process Dynamic systems Bundling Life-time-value maximization

## a b s t r a c t

Service product bundling is a widespread practice in current e-commerce environment. While many studies have examined optimal bundling and pricing in a static time domain, there has been a lack of attention to the dynamic nature of customer transition among bundles and the consequent long-term strategy. This paper considers subscription-based service bundling problem. In this context, an existing customer can choose the same bundle or switch to another bundle, whereas a new customer can adopt any of the bundles that are being offered. An analytical model that explicitly captures the customer transition over multiple time periods is developed using a dynamic systems approach. Using this model, we analyze the effect of adoption, retention, and switching simultaneously on optimal bundle con<sup>fi</sup>guration and pricing. We discuss several managerial insights, along with numerical examples and validating simulations, which are relevant to bundling strategy. We provide analytical results which enable an effective and ef<sup>fi</sup>cient decision support too to predict future demand stream for different bundles. We present a monotonicity property for the optimality condition which signi<sup>fi</sup>cantly reduces the computational burden.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Service product bundling is a widespread practice in current e-commerce environment. It involves combining two or more items or services as a bundle and is offered at a special price. There are many examples of bundling such as cable companies' entertainment package, computer hardware and software bundles and telecommunication service packages to name a few. In most cases, customers can save money by selecting bundles at discounted price while sellers can increase their revenue with appropriate bundling strategies.

In this paper, we consider a service provider's bundling problem in which customers subscribe to a set of services and each customer can opt-in or opt-out at anytime. Our problem domain covers telecommunication services, cable/entertainment package and online newspaper subscription services. Major service-providers such as Verizon and Time Warner offer bundled services including voice, Internet, and entertainment service. News providers such as Wall Street Journal provide bundled content delivery services. These service providers expect that properly bundled services will increase revenue, reduce administrative costs and create loyal customers.

When a provider offers multiple services, the optimal bundling strategy can be characterized in terms of the decisions regarding bundle pricing and component or item selection. While many studies have examined optimal bundling and pricing in a static time domain, they have not explained how the customers' retention or lifetimevalue could in<sup>fl</sup>uence the seller's long-term strategy. Due to the advances in Computer and Internet technologies, consumers can now switch to different services whenever they want with relative ease thereby introducing a high degree of volatility in demand stream. An optimal bundling strategy at a particular time may not be optimal for other time periods. Further, items that are bundled together might generate a synergy effect which can alter consumer's perceptions and eventually the lifetime value. In such cases, it is critical to understand the time trajectory of the customer transition in designing the optimal bundles.

In this paper, we develop an analytical model, which utilizes a dynamic systems approach [7] over multiple time periods. New customer adoption and existing customer retention of a particular bundle and switching to a different bundle are explicitly characterized in our model. We analyze how the new customer adoption rate for a bundle is determined by jointly distributed reservation prices and offered prices. We provide an effective and ef<sup>fi</sup>cient decision support mechanism to predict future demand stream for different bundles. Based on eigen-values and eigen-vectors, which explain the magnitude and direction of customer transition among bundles, future customer distribution can be predicted and the ensuing results can be used by the seller to determine the optimal marketing and production resource plans. To depict real-world scenarios, we considered three different cases, which involve different customer transition pattern, and conducted simulation studies for validation purposes. We present a monotonicity property for the optimality condition which signi<sup>fi</sup>- cantly reduces the computational burden. A myopic optimal solution for a one period problem inductively solves multi-period problems when a certain condition holds. Several numerical examples are used to illustrate the theoretical properties of our model and to draw relevant managerial insights.

The paper is organized as follows. In Section 2, we review the bundling literature which provides motivation for our dynamic model. In the following section, we develop a model to analyze the optimal bundle pricing and component selection strategy in a multi-period setting. To illustrate our analytical results, we provide numerical examples involving several different numbers of bundles in Section 4. In Section 5, we discuss managerial insights that can be derived from our model and results are validated using simulation analysis.

## 2. Relevant literature

By bundling, <sup>fi</sup>rms should deliver substantial value-added that cannot be achieved from component items separately. Since additional values offered from the bundle have a greater impact on buyers perceptions than savings offered by individual items, the <sup>fi</sup>rms will <sup>fi</sup>nd it optimal to bundle value-added products for long-term bene<sup>fi</sup>ts [6,12,16].

To realize the bene<sup>fi</sup>t of bundling, product management decisions about the bundle should be made by taking into account the value perceptions of customers [15]. Since the consumer perceptions in bundles are affected by their characteristics such as the number of items in the bundle and the level of variation in the value of bundled items ([1,3]), the perceptions and bundle savings in the market should be carefully analyzed. In fact, for the case of zero marginal cost which is common in information goods, as discussed in Bakos and Brynjolfsson [2], and Geng et al. [4], consumer valuation as well as the dispersion of valuation plays a signi<sup>fi</sup>cant role in bundling decision.

Since bundle price may affect the consumption pattern of customers [11], the bundle price should be strategically determined so that consumers will perceive the attractiveness of bundles. The <sup>fi</sup>rms should also limit the promotions of component items or the consumers will use the price information of individual items as external reference prices [14].

For computation of the optimal price of bundles, Hanson and Martin [5] developed a mixed integer linear programming algorithm to consider multiple component items, cost and customer reservation prices. In addition to the customer reservation price, multiple-choice dimensions such as the availability of time to use the service have been considered in Venkatesh and Mahajan [13].

Although bundling is a pervasive practice in today's market and continues to receive growing attention in the marketing and operations literature, most of studies however are focused on shortterm effect of bundling strategy in a static time domain. A departure has been made in [4], where bundling strategy has been studied in the context of decreasing value of information goods. The speed of valuedrop over time generates different variance in consumer valuation and it in turn alters the bundling decision.

The time effect, particularly the long-term effect based on customers' loyalty or retention has not been studied extensively in the literature. As in Schmittlein et al. [10] and Reinartz and Kumar [8], since the duration of customer relationship is an important factor for a <sup>fi</sup>rm's pro<sup>fi</sup>tability, the bundling strategy for subgroups of customers should be accompanied with accurate characterization of the lifetime values. In this paper, we address a bundling strategy which is based on the long-term effect of existing customer retention and new customer adoption in a multi-period time domain to dynamically capture the migrating effect of customers among the bundles and analyze the impact on the optimal strategy.

## 3. Analytical model

In our model, we consider the case where the service provider offers multiple services in a bundled format. Typically, this is the case in the cable news and entertainment service industry. We de<sup>fi</sup>ne a bundle as a set of services or items in a package. Each bundle can include non-zero number of services which implies that a single item is also a bundle. We assume that the service subscription occurs over multiple time periods. To resemble the real world market setting, our model allows existing customers, who already subscribe to a bundle, to switch to any other bundle at anytime. Each time period<sup>1</sup>, a group of potential customers may start subscribing to any of the <sup>fi</sup>rm's bundle services. The new customer's subscription decision is contingent on the offered price and their reservation price. To address the individual level heterogeneity in the market reservation prices, we use a probability density function as in Salinger [9] and Venkatesh and Mahajan [13]. The probability that a new customer chooses a particular bundle is jointly determined by offered price and reservation price for the bundle. As is the case in the real world setting, we assume that each customer can select only one bundle during each time period. Their bundle choice will be based on payoffs that maximize the consumer surplus.

Our model is unique in that it captures the synergistic effect of bundling on product demand due to changes in customer retention and switching behavior. This in turn affects the life time value of the bundle for the <sup>fi</sup>rm. On the contrary when only individual items (no bundles) are offered, the synergistic effect, which alters the lifetime value, cannot be addressed. This motivates us to investigate the impact of customer retention and switching behavior on bundling strategies.

Now we introduce the parameters and variables along with the relevant assumptions that describe the model.

## 3.1. Parameters and variables

i : bundle index, $i = 1 , . . . , I ,$ includes single and multi-item bundles, when there are k single-item-bundles $^ 2 , I = 2 ^ { k } - 1$

$N _ { i } ( t ) \colon$ number of existing customers who subscribe to bundle i at time period t

$u ( t ) \colon$ total number of potential customers at time t

$P _ { i } \colon$ offered price of bundle i

$R _ { i } \colon$ customer reservation price for bundle i which has a PDF $f _ { R _ { i } } ( R _ { i } )$ . We assume that when bundle i and bundle j are subsets of bundle h, ${ \bf \nabla } R _ { h } = R _ { i } + R _ { j } ,$ . Without loss of generality, $R _ { i }$ is time-invariant.

$f _ { R _ { i } } ( R _ { i } ) { \mathrm { : } }$ : PDF of customer reservation price for bundle i. We assume that $f _ { R _ { i } } ( R _ { i } )$ is independent of time.

$S _ { i } { \mathrm { : } }$ consumer surplus for bundle $i , \ ( S _ { i } = R _ { i } - P _ { i } )$ . As found in practice, we assume that a customer selects only one bundle which maximizes the surplus during each time period t.

$C _ { i } \mathrm { : }$ seller's cost of bundle i

$\mu _ { * }$ periodic discount rate

Now the <sup>fi</sup>rm's net present value of the total pro<sup>fi</sup>t or total lifetime value, π over time periods 1 through T is given as

$$
\pi = \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {I} \mu^ {t - 1} (P _ {i} - C _ {i}) N _ {i} (t)\tag{1}
$$

To model the subscriber dynamics, we consider four possibilities regarding bundle i: some of the existing subscribers could retain bundle i, some of the existing customers could switch to bundle i from another bundle j (where $j \neq i$ and $i , j \in I )$ , some of the new customers may adopt bundle i whereas some of the existing customers of bundle i could opt out. The evolution of this dynamics over time is modeled using a multi-period recursion system as proposed by Luenberger [7]. The existing customer retention or switching rate among the bundles is represented by the transition rate $a _ { i j } ( t )$ where i and j are bundle indices. Note that in this case, $\begin{array} { r } { 1 - \sum _ { i } a _ { i j } ( t ) } \end{array}$ re<sup>fl</sup>ects the opt-out rate from bundle j. Each time period t, new customers, with probability $b _ { i } ( t )$ , choose bundle i. Now the subscriber dynamics can be stated as follows.

$$
\begin{array}{c} N _ {1} (t + 1) = a _ {1 1} (t) N _ {1} (t) + a _ {1 2} (t) N _ {2} (t) + \dots + a _ {1 I} (t) N _ {I} (t) + b _ {1} (t) u (t) \\ N _ {2} (t + 1) = a _ {2 1} (t) N _ {1} (t) + a _ {2 2} (t) N _ {2} (t) + \dots + a _ {2 I} (t) N _ {I} (t) + b _ {2} (t) u (t) \\ \vdots \\ N _ {I} (t + 1) = a _ {I 1} (t) N _ {1} (t) + a _ {I 2} (t) N _ {2} (t) + \dots + a _ {I I} (t) N _ {I} (t) + b _ {I} (t) u (t) \end{array}\tag{2}
$$

Using a matrix notation, the dynamics can be expressed in the following equivalent form

$$
\mathbf {N} (t + 1) = \mathbf {A} (t) \cdot \mathbf {N} (t) + \mathbf {B} (t) \cdot u (t)
$$

where

$$
\left( \begin{array}{c} N _ {1} (t + 1) \\ N _ {2} (t + 1) \\ \vdots \\ N _ {I} (t + 1) \end{array} \right) = \left( \begin{array}{c c c c} a _ {1 1} (t) & a _ {1 2} (t) & & \\ a _ {2 1} (t) & & \ddots & \\ & & & a _ {I I} (t) \end{array} \right) \left( \begin{array}{c} N _ {1} (t) \\ N _ {2} (t) \\ \vdots \\ N _ {I} (t) \end{array} \right) + \left( \begin{array}{c} b _ {1} (t) \\ b _ {2} (t) \\ \vdots \\ b (t) \end{array} \right) u (t)\tag{3}
$$

The matrix components are as follows.

• State vector: the number of customers at each time period t.

$$
\mathbf {N} (t) = \left( \begin{array}{c} N _ {1} (t) \\ N _ {2} (t) \\ \vdots \\ N _ {I} (t) \end{array} \right) = \left( \begin{array}{c} \text { Number   of   product   1   customers   at   time } t \\ \text { Number   of   product   2   customers   at   time } t \\ \vdots \\ \text { Number   of   product   I   customers   at   time } t \end{array} \right)
$$

u(t): total number of potential new customers at time period t

• Transition matrices: We use two matrices to capture the subscriber dynamics. Matrix A(t) captures the dynamics of how the existing customers transition from the current time period t to the next time period t+1.

$$
\mathbf {A} (t) = \left( \begin{array}{c c c c} a _ {1 1} (t) & a _ {1 2} (t) & & \\ a _ {2 1} (t) & & \ddots & \\ & & & a _ {I I} (t) \end{array} \right)
$$

$a _ { i j } ( t ) \colon$ proportion of existing customers who migrate from bundle j at time t to bundle i at time t+1.

If i = j, it implies retention and if $i \neq j ,$ it implies switching and $1 - \sum _ { i } a _ { i j } ( t )$ means that the existing customer opts out without choosing any bundles. Note that we use the transition matrix $\pmb { A } ( t )$ to model the retention and switching behavior of customers among the bundles being offered. Bundling strategy is not only an effective price discrimination method to extract more surplus, but is also a good way to improve the customer perception about the bundles being offered. This in turn leads to greater loyalty and customer retention. An ideal bundle is a package of services that becomes an integral part of the subscriber's lifestyle and, therefore, increases the total lifetime value. By understanding the needs and wants of the target population, the choice of items to be included in a bundle should aim to maximize the synergistic effect among them. This synergistic effect in<sup>fl</sup>uences the customer retention and switching behavior which has not been well explained in the literature. Our model incorporates the synergistic effect through the transition matrix A(t).

When a new customer adopts a bundle, his or her reservation price will determine the adoption probability which is modeled separately by the matrix $\mathbf { B } ( t )$ . Matrix ${ \bf \delta B } ( t )$ captures the entry dynamics of new customers.

$$
\mathbf {B} (\mathbf {t}) = \left( \begin{array}{c} b _ {1} (t) \\ b _ {2} (t) \\ \vdots \\ b _ {I} (t) \end{array} \right)
$$

b (t): proportion of new customers who choose bundle i at time t

At each time period t, new customers select one of the offered bundles. The proportion of new customers who select bundle i at time t is given as

$$
\begin{array}{l} b _ {i} (t) = P r \Big [ (S _ {i} \geq 0) \cap (S _ {i} > S _ {1}) \cap \dots \Big (S _ {i} > S _ {j} \Big) \dots \cap (S _ {i} > S _ {I}) \Big ] \\ \text {where} j \neq i \text {and} i, j \in I \\ \quad = P r \Big [ (R _ {i} - P _ {i} \geq 0) \cap (R _ {i} - P _ {i} > R _ {1} - P _ {1}) \cap \dots \\ \quad \times \Big (R _ {i} - P _ {i} > R _ {j} - P _ {j} \Big) \dots \cap (R _ {i} - P _ {i} > R _ {I} - P _ {I}) \Big ] \\ \quad = \int ... \int f _ {R _ {i}} (R _ {I}) \dots f _ {R _ {i}} (R _ {I}) d R _ {1} \dots d R _ {I} \text {for all} i, j \in I \end{array}\tag{4}
$$

Eq. (4) implies that each customer chooses bundle i which yields the greatest non-negative surplus that maximizes their payoff. The recursion in Eq. (3) can be represented in terms of initial state vector N(0), vector u(t), and transition matrices $\pmb { A } ( t )$ and ${ \bf B } ( t )$ . For the case of $t = 3$ periods, the recursion is as follows.

$$
\begin{array}{l} \mathbf {N} (1) = \mathbf {A} (0) \mathbf {N} (0) + \mathbf {B} (0) u (0) \\ \mathbf {N} (2) = \mathbf {A} (1) \mathbf {N} (1) + \mathbf {B} (1) u (1) = \mathbf {A} (1) \mathbf {A} (0) \mathbf {N} (0) + \mathbf {A} (1) \mathbf {B} (0) u (0) + \mathbf {B} (1) u (1) \\ \mathbf {N} (3) = \mathbf {A} (2) \mathbf {N} (2) + \mathbf {B} (2) u (2) = \mathbf {A} (2) \mathbf {A} (1) \mathbf {A} (0) \mathbf {N} (0) + \mathbf {A} (2) \mathbf {A} (1) \mathbf {B} (0) u (0) \\ \qquad + \mathbf {A} (2) \mathbf {B} (1) u (1) + \mathbf {B} (2) u (2) \end{array}
$$

We can now determine the optimal price of each bundle so as to maximize the total pro<sup>fi</sup>t or total life time value during time period t=1 to T.

$$
\text { Max } \pi = \sum_ {t = 1} ^ {T} \mu^ {t - 1} (\mathbf {P} - \mathbf {C}) ^ {\text { Transpose }} \mathbf {N} (t)\tag{5.1}
$$

s.t.

$$
\begin{array}{l} P _ {i} \leq R _ {i} \\ b _ {i} = \operatorname * {P r} \left[ (R _ {i} - P _ {i} \geq 0) \cap \left(R _ {i} - P _ {i} > R _ {j} - P _ {j}\right) \right] \text { for   all } j \neq i \text { and } i, j \in I \end{array} \tag {5.}\tag{5.2}
$$

<sub>ð</sub>5:3<sub>Þ</sub>

$$
\begin{array}{r l} \mathbf {N} (t) & = \mathbf {A} (t - 1) \mathbf {N} (t - 1) + \mathbf {B} (t - 1) u (t - 1) \\ & = \mathbf {A} (t - 1) \mathbf {A} (t - 2) \dots \mathbf {A} (0) \mathbf {N} (0) + \mathbf {A} (t - 1) \mathbf {A} (t - 2) \dots \mathbf {A} (1) \mathbf {B} (0) u (0) \\ & \quad + \mathbf {A} (t - 1) \mathbf {A} (t - 2) \dots \mathbf {A} (2) \mathbf {B} (1) u (1) + \dots + \mathbf {B} (t - 1) u (t - 1) \end{array}\tag{5.4}
$$

where

$$
\begin{array}{c} \mathbf {P} = \left( \begin{array}{c} P _ {1} \\ P _ {2} \\ \vdots \\ P _ {I} \end{array} \right), \quad \mathbf {C} = \left( \begin{array}{c} C _ {1} \\ C _ {2} \\ \vdots \\ C _ {I} \end{array} \right), \quad \mathbf {N} (t) = \left( \begin{array}{c} N _ {1} (t) \\ N _ {2} (t) \\ \vdots \\ N _ {I} (t) \end{array} \right), \quad \mathbf {A} (t) \\ = \left( \begin{array}{c c c c} a _ {1 1} (t) & a _ {1 2} (t) & & \\ a _ {2 1} (t) & & \\ & \ddots & \\ & & a _ {I I} (t) \end{array} \right), \quad \mathbf {B} (t) = \left( \begin{array}{c} b _ {1} (t) \\ b _ {2} (t) \\ \vdots \\ b _ {I} (t) \end{array} \right) \end{array}
$$

When the transition matrices ${ \bf A } ( t ) , { \bf B } ( t )$ and input vector $u ( t )$ are time invariant, we can derive a simpli<sup>fi</sup>ed general equation for N(t).

$$
\mathbf {N} (t) = \mathbf {A} ^ {t} \cdot \mathbf {N} (0) + \sum_ {l = 0} ^ {t - 1} \mathbf {A} ^ {t - l - 1} \mathbf {B} u \quad t, l = 0, 1, 2, \dots\tag{6.1}
$$

In Eq. (6.1), we have

$$
\sum_ {l = 0} ^ {t - 1} \mathbf {A} ^ {t - l - 1} = \mathbf {A} ^ {t - 1} + \mathbf {A} ^ {t - 2} + \dots + \mathbf {I}\tag{6.2}
$$

Therefore,

$$
\mathbf {A} \sum_ {l = 0} ^ {t - 1} \mathbf {A} ^ {t - l - 1} = \mathbf {A} ^ {t} + \mathbf {A} ^ {t - 1} + \dots + \mathbf {A}\tag{6.3}
$$

Now subtracting Eq. (6.3) from Eq. (6.2), we have

$$
(\mathbf {I} - \mathbf {A}) \sum_ {l = 0} ^ {t - 1} \mathbf {A} ^ {t - l - 1} = \mathbf {I} - \mathbf {A} ^ {t} \text { and } \sum_ {l = 0} ^ {t - 1} \mathbf {A} ^ {t - l - 1} = (\mathbf {I} - \mathbf {A}) ^ {- 1} \left(\mathbf {I} - \mathbf {A} ^ {t}\right)\tag{6.4}
$$

Therefore,

$$
\mathbf {N} (t) = \mathbf {A} ^ {t} \cdot \mathbf {N} (0) + (\mathbf {I} - \mathbf {A}) ^ {- 1} \left(\mathbf {I} - \mathbf {A} ^ {t}\right) \mathbf {B} u\tag{6.5}
$$

where

$$
\begin{array}{l l} \mathbf {A} (0) = \mathbf {A} (1) = \dots = \mathbf {A} (t) = \mathbf {A} & t = 0, 1, 2, \dots \\ \mathbf {B} (0) = \mathbf {B} (1) = \dots = \mathbf {B} (t) = \mathbf {B} & t = 0, 1, 2, \dots \\ u (0) = u (1) = \dots = u (t) = u & t = 0, 1, 2, \dots \end{array}
$$

Using the time invariant system given in Eq. (6.5), we can explicitly determine the number of users in the system at a particular time period t.

## 4. Illustrative examples

Now we use several numerical examples to illustrate the features of the proposed model and also show how the customer behavior in<sup>fl</sup>uences the long-term bundling strategy.

4.1. Numerical example with two single item and one multi-item bundles

Consider the service provider's bundling strategy which includes price decision and item selection over multiple time periods (12 periods).

Optimal bundling strategies with two individual items and one bundle: varying bundle retention rate.

<table><tr><td> $a_{AA}$ </td><td> $a_{BB}$ </td><td> $a_{ABAB}$ </td><td>Optimal  $P_A$ </td><td>Optimal  $P_B$ </td><td>Optimal  $P_{AB}$ </td><td>Max profit over 12 time periods</td></tr><tr><td>0.6</td><td>0.7</td><td>0</td><td>$15</td><td>$13</td><td>$40</td><td>$4320</td></tr><tr><td>0.6</td><td>0.7</td><td>0.1</td><td>$15</td><td>$13</td><td>$40</td><td>$4320</td></tr><tr><td>0.6</td><td>0.7</td><td>0.2</td><td>$15</td><td>$13</td><td>$29</td><td>$4346</td></tr><tr><td>0.6</td><td>0.7</td><td>0.3</td><td>$15</td><td> $15^a$ </td><td>$27</td><td>$4474</td></tr><tr><td>0.6</td><td>0.7</td><td>0.4</td><td>$15</td><td>$15</td><td>$25</td><td>$4726</td></tr><tr><td>0.6</td><td>0.7</td><td>0.5</td><td> $25^a$ </td><td>$15</td><td>$24</td><td>$5302</td></tr><tr><td>0.6</td><td>0.7</td><td>0.6</td><td>$25</td><td>$15</td><td>$24</td><td>$6353</td></tr><tr><td>0.6</td><td>0.7</td><td>0.7</td><td>$25</td><td>$15</td><td>$24</td><td>$7872</td></tr><tr><td>0.6</td><td>0.7</td><td>0.8</td><td>$25</td><td>$15</td><td>$24</td><td>$10,184</td></tr><tr><td>0.6</td><td>0.7</td><td>0.9</td><td>$25</td><td>$15</td><td>$24</td><td>$13,891</td></tr><tr><td>0.6</td><td>0.7</td><td>1</td><td>$25</td><td>$15</td><td>$24</td><td>$20,104</td></tr></table>

<sup>a</sup> Once the price reaches the maximum reservation price, the item is not offered.

![](/api/attachments/DYBMEF2C/fulltext/images/b072cb9af0aa6d25c93b82e79579955d2e816b9a59de0ef3a8869be284ece55a.jpg)  
Fig. 1. Optimal price of A, B, and AB where $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7$ and varying a<sub>ABAB</sub>.

• Three bundles are offered: A, B, and AB (2 single item bundles and 1 multi-item bundle).

• We assume C =0 for all i.

• The reservation prices for item A and B are drawn from uniform distributions and the reservation price of A is higher than B while the bundle AB's reservation price is the sum of the reservation prices of items A and B.

$$
\begin{array}{l} - R _ {A} \sim U [ 1 5, 2 5 ] \\ - R _ {B} \sim U [ 5, 1 5 ] \\ - R _ {A B} = R _ {A} + R _ {B} \end{array}
$$

• Without loss of generality, the initial number of customers for three bundles is assumed to be zero.

$$
\mathbf {N} (0) = \left( \begin{array}{c c c} 0 & 0 & 0 \end{array} \right) ^ {T}
$$

• The potential new customers at each time period are assumed to be constant.

$$
u (0) = u (1) = u (2) = \dots = u (1 1) = 1 0
$$

• There is no discounting and hence $\mu { = } 1 .$

To examine the impact of the bundle retention behavior on the optimal pricing strategy, we consider the individual item retention rates as $a _ { A A } = 0 . 6$ and $a _ { B B } = 0 . 7$ for all t and varying the retention rate of $A B , a _ { A B A B }$ from 0 to 1. Table 1 and Fig. 1 show that as the retention rate of bundle AB increases, it is optimal to lower the price of AB since the profit also increases. This is because as the retention rate of the bundle AB increases, the service provider can reduce the bundle price which in turn attracts many more new customers to the bundle AB rather than items A and B. Figs. 2 and 3 illustrate that as the bundle retention rate AB increases the total number of customers who choose individual items A and B reduces dramatically. Once the bundle retention rate reaches a threshold point (=0.5), the optimal price of items A and B reach their individual maximum reservation prices while the optimal bundle price levels out. This implies that from that point onward it is not economical to offer individual items A and B (as can be seen in Fig. 3 where the total number of customers for A and B is zero) and hence only offering AB is the optimal strategy as it yields

![](/api/attachments/DYBMEF2C/fulltext/images/d120c9d765e82fa43112fcbcd08e2e0900d24ea3d35d9bbfd48ad12abc5c619e.jpg)  
Fig. 2. Number of customers for A, B, and AB where $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7 ,$ and $a _ { A B A B } = 0 . 4 .$

Table 2

![](/api/attachments/DYBMEF2C/fulltext/images/251fce0b45868952d58204c0e46659dce6912f09cb79401dbdf0c6ae654706fa.jpg)  
Fig. 3. Number of customers for A, B, and AB where $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7 ,$ and $a _ { A B A B } = 0 . 7 .$

maximum pro<sup>fi</sup>t or total lifetime value. In Section 5, we provide a rigorous rationale for this observation.

Figs. 2 and 3 show how the number of customers varies based on the varying retention rate. When A and B have retention rate of 0.6 and 0.7 respectively and AB has a lower retention rate of 0.4, the number of users in the system grows like Fig. 2.

When $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7 ,$ and $a _ { A B A B } = 0 . 7 ,$ the number of users in the system grows like Fig. 3. Note that when the retention rate of AB grows to 0.7 the optimal price of AB dropts to \$24. Consequently, more users adopt AB and the number of the users of AB grows faster.

Given the varying retention rate and the optimal price set the seller pro<sup>fi</sup>t is presented in the following <sup>fi</sup>gure. While the retention rate of AB varies, the seller's optimal policy varies and the total pro<sup>fi</sup>t over 12 time periods increases exponentially (Fig. 4).

## 4.2. Numerical example with more than one multi-item bundle

We now consider more than one multi-item bundle case. Suppose there are three single-item bundles A, B, and C with reservation prices, $R _ { A } { \sim } U [ 1 5 , 2 5 ] , R _ { B } { \sim } U [ 1 5 , 2 5 ] ,$ , and $R _ { C } \sim U [ 5 ,$ , 15] respectively and two multi-item bundles AC and BC with $R _ { A C } = R _ { A } + R _ { C }$ and $R _ { B C } = R _ { B } + R _ { C } .$ Suppose the retention rates of A, B, and C are 0.9, 0.9 and 0.6 respectively. To analyze the insights into the optimal policy we vary the retention rates of AC and BC from 0 to 1. As was the case with in Section 4.1, Table 2 shows that the optimal prices of AC and BC decreases as their retention rate increase. Since the same retention rates are applied to individual items A and B and the bundles AC and BC, we observe identical optimal prices for A and B, and AC and BC.

Table 2, Figs. 5 and 6 show the optimal prices and the distribution of number of customers. When the retention rate of AC and BC are lower than or equal to 0.6, the optimal strategy is not to offer bundles AC and BC. Instead attracting more customers for high retention items A and B yields the maximum pro<sup>fi</sup>t. However, when the retention rates of AC and BC are greater than 0.6, the service provider should lower the price of AC and BC to increase the adoption rates. When the retention rates reach 0.9, the optimal strategy is to offer only bundles AC and BC.

![](/api/attachments/DYBMEF2C/fulltext/images/e24f788e15a641c9c39a060f6aaea255e37746ba29d47109eeadaad4cf77a2ab.jpg)  
Fig. 4. Total pro<sup>fi</sup>t for 12 time periods where $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7 ,$ and varying a<sub>ABAB</sub>.

Optimal bundling strategies with three individual items and two bundles: same bundle reservation price range and bundle retention rates varying in the same direction.

<table><tr><td> $a_{AA}$ </td><td> $a_{BB}$ </td><td> $a_{CC}$ </td><td> $a_{ACAC}$ </td><td> $a_{BCBC}$ </td><td>Optimal  $P_A$ </td><td>Optimal  $P_B$ </td><td>Optimal  $P_C$ </td><td>Optimal  $P_{AC}$ </td><td>Optimal  $P_{BC}$ </td><td>Max profit</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0</td><td>0</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.1</td><td>0.1</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.2</td><td>0.2</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.3</td><td>0.3</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.4</td><td>0.4</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.5</td><td>0.5</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.6</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.7</td><td>0.7</td><td>$18</td><td>$18</td><td>$15</td><td>$31</td><td>$31</td><td>$10,338</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.8</td><td>0.8</td><td>$18</td><td>$18</td><td>$15</td><td>$27</td><td>$27</td><td>$11,484</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.9</td><td>0.9</td><td>$25</td><td>$25</td><td>$15</td><td>$26</td><td>$26</td><td>$15,176</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>1</td><td>1</td><td>$25</td><td>$25</td><td>$15</td><td>$26</td><td>$26</td><td>$21,964</td></tr></table>

Interestingly, when we varied the retention rate of AC and BC in the opposite direction as in Table 3, the optimal prices also move in the opposite direction in a symmetric pattern. The maximum pro<sup>fi</sup>t is obtained when the retention rate of AC (BC) is at its highest (lowest) level and vice versa. We consistently observe that the optimal price decreases as the retention rate increases.

From Table 3 and Fig. 7, it can be seen that with low retention rates the optimal bundle prices approach their reservation price implying that those bundles need not be offered. For example, with a retention rate of 0.2, optimal price of bundle BC approaches the reservation price of \$40 and hence it is not optimal to offer that bundle. Same is the case with bundle C. Offering only A, B, and AC at the prices shown in Table 3, yields the maximum pro<sup>fi</sup>t. The symmetric pattern of optimal prices produces a U-shaped pro<sup>fi</sup>t curve as in Fig. 8.

Now we consider a new set of bundles AB and AC with $R _ { A B } = R _ { A } + R _ { B }$ and $R _ { A C } = R _ { A } + R _ { C }$ where $R _ { A B } { \sim } U [ 3 0 , 5 0 ]$ and $R _ { A C } { \sim } U [ 2 0 , 4 0 ]$ respectively. From Table 4, we again observe that as the retention rate of a bundle increases, the optimal strategy is to lower the price of the bundle so that more customers adopt the bundle and stay as loyal customers.

In the next section, we provide a rigorous analysis of the patterns observed from the numerical examples along with validating simulations.

## 5. Analysis, managerial insights and implications

In this section we <sup>fi</sup>rst provide analytical results that support the observations of the above section along with insights which should enable the service provider to develop pragmatic pricing policies, select bundle components, and predict future customer distribution.

1. We observe that as the retention rate of a bundle increases its optimal price drops. This implies that in order to increase the adoption rate of new customers for bundle i, the <sup>fi</sup>rm should lower the price while holding the prices of other bundles constant.This can be explained as follows. The proportion of customers who select bundle i over j (where i, j∈I) is given as

![](/api/attachments/DYBMEF2C/fulltext/images/624bca37685478238423c0c242b623bb989fe6007c460358fd4c008ada7c25f0.jpg)  
Fig. 5. Number of customers of A, B, C, AC and BC where $a _ { A A } = 0 . 9 , a _ { B B } = 0 . 9 , a _ { C C } = 0 . 6 ,$ $a _ { A C A C } = 0 . 5$ and $a _ { B C \ B C } = 0 . 5 .$

![](/api/attachments/DYBMEF2C/fulltext/images/ef21c1425a3065fd366c72ebe5226a5abca738808bd3142a268bad215aa008f3.jpg)  
Fig. 6. Number of customers of A, B, C, AC and BC where $a _ { A A } = 0 . 9 , a _ { B B } = 0 . 9 , a _ { C C } = 0 . 6 ,$ $a _ { A C A C } { = } 0 . 9$ and $a _ { B C \ B C } = 0 . 9$

$$
\begin{array}{l} P r \left[ (R _ {i} \geq P _ {i}) \cap \left(R _ {i} - P _ {i} > R _ {j} - P _ {j}\right) \right] \\ = \int_ {P _ {i}} ^ {R _ {i} \text { Max }} \int_ {R _ {j} \text { Min }} ^ {R _ {i} - P _ {i} + P _ {j}} f _ {R _ {i}} (R _ {i}) f _ {R _ {j}} \left(R _ {j}\right) d R _ {j} d R _ {i} \end{array}\tag{7.1}
$$

Fig. 9 depicts the computation of Eq. (7.1). It can be seen that by lowering the price $P _ { i } ,$ the probability (shaded area) of adoption always increases so that the proportion of new customers who choose i over other bundles also increases.

2. A common problem facing the service provider is the selection of items to include in a bundle. Normally the selection is in<sup>fl</sup>uenced by factors such as item prices, retention and adoption rates. However these factors often change without much notice thereby requiring the service provider to repeatedly compute new item prices. We now present a monotonicity property which can reduce the computational burden signi<sup>fi</sup>cantly while improving the effectiveness of component selection.Let items i and j be the components of bundle h. In a particular time period t, if offering-only-h (=pure bundling strategy without offering the components i and j) is the optimal strategy, then that strategy with the corresponding price set will also be optimal for all future time periods, if the retention rate of bundle h is higher than or equal to that of the individual items i and j. This can be explained as follows.

Initially, let us consider the <sup>fi</sup>rst period problem where $N _ { h } ( 0 ) = 0 ,$ so

$$
(P _ {h} - C _ {h}) (N _ {h} (0) + b _ {h} u (0)) = (P _ {h} - C _ {h}) b _ {h} u\tag{8.1}
$$

Optimal bundling strategies with three individual items and two bundles: same bundle reservation price range and bundle retention rates varying in opposite direction

<table><tr><td> $a_{AA}$ </td><td> $a_{BB}$ </td><td> $a_{CC}$ </td><td> $a_{ACAC}$ </td><td> $a_{BCBC}$ </td><td>Optimal  $P_A$ </td><td>Optimal  $P_B$ </td><td>Optimal  $P_C$ </td><td>Optimal  $P_{AC}$ </td><td>Optimal  $P_{BC}$ </td><td>Max profit</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0</td><td>1</td><td>$23</td><td>$23</td><td>$15</td><td>$40</td><td>$24</td><td>$20,235</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.1</td><td>0.9</td><td>$20</td><td>$20</td><td>$15</td><td>$40</td><td>$25</td><td>$14,261</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.2</td><td>0.8</td><td>$19</td><td>$19</td><td>$15</td><td>$40</td><td>$27</td><td>$11,207</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.3</td><td>0.7</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$31</td><td>$10,331</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.4</td><td>0.6</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.5</td><td>0.5</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.4</td><td>$18</td><td>$18</td><td>$14</td><td>$40</td><td>$40</td><td>$10,294</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.7</td><td>0.3</td><td>$18</td><td>$18</td><td>$14</td><td>$31</td><td>$40</td><td>$10,331</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.8</td><td>0.2</td><td>$19</td><td>$19</td><td>$15</td><td>$27</td><td>$40</td><td>$11,207</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.9</td><td>0.1</td><td>$20</td><td>$20</td><td>$15</td><td>$25</td><td>$40</td><td>$14,261</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>1</td><td>0</td><td>$23</td><td>$23</td><td>$15</td><td>$24</td><td>$40</td><td>$20,235</td></tr></table>

![](/api/attachments/DYBMEF2C/fulltext/images/4095b942fa49d31516a32a0971d41de9e12e1d5975b87676de1978484f214e96.jpg)  
Fig. 7. Number of customers of A, B, C, AC and BC where $a _ { A A } = 0 . 9 , a _ { B B } = 0 . 9 , a _ { C C } = 0 . 6 ,$ $a _ { A C A C } = 0 . 8$ and $a _ { B C \ B C } = 0 . 2 .$

If offering-only-h is optimal, and $P _ { h } ^ { * }$ and $b _ { h } ^ { * }$ are the optimal price and corresponding adoption rate respectively, then the following condition holds.

$$
\begin{array}{l} \left(P _ {h} ^ {*} - C _ {h}\right) b _ {h} ^ {*} u \geq (P _ {i} - C _ {i}) b _ {i} u + \left(P _ {j} - C _ {j}\right) b _ {j} u \\ \quad + (P _ {h} - C _ {h}) b _ {h} u \quad \text { for   all } \mathbf {P} \neq \mathbf {P} ^ {*} \end{array}\tag{8.2}
$$

Multiplying Eq. (8.2) on both sides by $a _ { h } ,$ we have

$$
\left(P _ {h} ^ {*} - C _ {h}\right) a _ {h} b _ {h} ^ {*} u \geq (P _ {i} - C _ {i}) a _ {h} b _ {i} u + \left(P _ {j} - C _ {j}\right) a _ {h} b _ {j} u + (P _ {h} - C _ {h}) a _ {h} b _ {h} u\tag{8.3}
$$

Since $a _ { h } \ge a _ { i }$ and $a _ { h } \ge a _ { j } ,$ we can represent $a _ { i }$ and a<sub>j</sub> using nonnegative scalars $\delta _ { i }$ and $\delta _ { j }$ such that $a _ { h } = a _ { i } + \delta _ { i } = a _ { j } + \delta _ { j } ,$ then

$$
\begin{array}{l} \left(P _ {h} ^ {*} - C _ {h}\right) a _ {h} b _ {h} ^ {*} u \geq \left(P _ {i} - C _ {i}\right) a _ {i} b _ {i} u + \left(P _ {j} - C _ {j}\right) a _ {j} b _ {j} u + \left(P _ {h} - C _ {h}\right) a _ {h} b _ {h} u \\ + \left(P _ {i} - C _ {i}\right) \delta_ {i} b _ {i} u + \left(P _ {j} - C _ {j}\right) \delta_ {j} b _ {j} u \end{array} \tag {8.4}
$$

or

$$
\left(P _ {h} ^ {*} - C _ {h}\right) a _ {h} b _ {h} ^ {*} u \geq (P _ {i} - C _ {i}) a _ {i} b _ {i} u + \left(P _ {j} - C _ {j}\right) a _ {j} b _ {j} u + (P _ {h} - C _ {h}) a _ {h} b _ {h} u\tag{8.5}
$$

Combining Eqs. (8.2) and (8.5), we can verify that

$$
\begin{array}{l} \left(P _ {h} ^ {*} - C _ {h}\right) \left(a _ {h} b _ {h} ^ {*} u + b _ {h} ^ {*} u\right) \geq (P _ {i} - C _ {i}) (a _ {i} b _ {i} u + b _ {i} u) \\ \quad + \left(P _ {j} - C _ {j}\right) \left(a _ {j} b _ {j} u + b _ {j} u\right) + (P _ {h} - C _ {h}) (a _ {h} b _ {h} u + b _ {h} u) \end{array}\tag{8.6}
$$

![](/api/attachments/DYBMEF2C/fulltext/images/7579b373d9a2c88375f70896b87ff63c88882d1fabfe69804bbc5659bf2e9112.jpg)  
Fig. 8. Total pro<sup>fi</sup>t for 12 time periods where $a _ { A A } = 0 . 9 , a _ { B B } = 0 . 9 , a _ { C C } = 0 . 6 ,$ , and varying $a _ { A C A C }$ with $a _ { B C B C } = 1 - a _ { A C A C } .$

and hence $P _ { h } ^ { * }$ is optimal for the second period also. Similarly the following equation holds for the third period.

$$
\begin{array}{l} \left(P _ {h} ^ {*} - C _ {h}\right) \left(a _ {h} ^ {2} b _ {h} ^ {*} u + a _ {h} b _ {h} ^ {*} u + b _ {h} ^ {*} u\right) \geq \left(P _ {i} - C _ {i}\right) \left(a _ {i} ^ {2} b _ {i} u + a _ {i} b _ {i} u + b _ {i} u\right) \\ \quad + \left(P _ {j} - C _ {j}\right) \left(a _ {j} ^ {2} b _ {j} u + a _ {j} b _ {j} u + b _ {j} u\right) \\ \quad + \left(P _ {h} - C _ {h}\right) \left(a _ {h} ^ {2} b _ {h} u + a _ {h} b _ {h} u + b _ {h} u\right) \end{array} \tag {8.7}
$$

Thus, the optimality of $P _ { h } ^ { * }$ and $b _ { h } ^ { * }$ can be generalized for all t such that

$$
\begin{array}{l} \left(P _ {h} ^ {*} - C _ {h}\right) \left(a _ {h} ^ {t - 1} b _ {h} ^ {*} u + a _ {h} ^ {t - 2} b _ {h} ^ {*} u + \dots + a _ {h} b _ {h} ^ {*} u + b _ {h} ^ {*} u\right) \\ \geq (P _ {i} - C _ {i}) \left(a _ {i} ^ {t - 1} b _ {i} u + a _ {i} ^ {t - 2} b _ {i} u + \dots + a _ {i} b _ {i} u + b _ {i} u\right) \\ \quad + \left(P _ {j} - C _ {j}\right) \left(a _ {j} ^ {t - 1} b _ {j} u + a _ {j} ^ {t - 2} b _ {j} u + \dots + a _ {j} b _ {j} u + b _ {j} u\right) \\ \quad + (P _ {h} - C _ {h}) \left(a _ {h} ^ {t - 1} b _ {h} u + a _ {h} ^ {t - 2} b _ {h} u + \dots + a _ {h} b _ {h} u + b _ {h} u\right) \end{array}\tag{8.8}
$$

When there are three bundles A, B, and AB with $R _ { A } \sim U [ 1 5 , 2 5 ] ,$ $R _ { B } \sim U [ 5 , 1 5 ] ,$ , and $R _ { A B } = R _ { A } + R _ { B } ,$ the optimal strategy of the oneperiod problem is to provide only AB (pure bundling strategy). The optimal price set in this case is (N/A, N/A, \$24). This policy is optimal for any multi-period problem $( { \mathrm { i . e . , } } t { = } 2 , 3 , 4 , ^ { \cdots \infty } )$ as long as $a _ { A B A B } { \geq } a _ { A A }$ and $a _ { A B A B } { \geq } A _ { B B } .$ As shown in Table 1, the same strategy (pure bundling with \$25, \$15, \$24) is optimal for multi-period $\left( t = 1 2 \right)$ problem when $a _ { A B A B } { \geq } a _ { A A }$ and $a _ { A B A B } \geq a _ { B B } .$ . Note that, instead of resolving the 12-period problem, we can use the optimal solution of the one-period problem $( \$ 25,45,524 ) ^ { 3 }$ for all cases where the condition $a _ { A B A B } { \geq } a _ { A A }$ and $a _ { A B A B } 2 a _ { B B }$ holds.

3. To conduct target advertisement and promotion campaigns, a service provider needs to predict what proportion of customers would purchase what types of bundles by taking into account the bundle price set, retention and adoption rates of both existing and future customers. The model developed above can serve as an effective prediction tool to make optimal resource allocation decisions for marketing and production.

We now describe a method, using the eigen-values and eigenvectors of the transition matrix A, to predict the customer distribution among the types of bundles being offered.A scalar value λ is an eigen-value of an n×n matrix A if there is a nonzero n×1 vector e such that $\pmb { \mathrm { A e } } = \lambda \mathbf { e }$ . The corresponding vector e is called an eigen-vector of the matrix A. The eigen-values are calculated using the characteristic equation, det $[ \pmb { A } - \lambda \mathbf { I } ] = 0$ and eigen-vectors can be obtained accordingly. In our example from Table 1, when $a _ { A A } = 0 . 6 , a _ { B B } = 0 . 7 ,$ , and $a _ { A B A B } { = } 0 . 8$ , we <sup>fi</sup>nd 3 eigenvalues and 3 linearly independent eigen-vectors. They are

$$
\begin{array}{l} \mathrm{A} = \left( \begin{array}{c c c} 0. 6 & 0 & 0 \\ 0 & 0. 7 & 0 \\ 0 & 0 & 0. 8 \end{array} \right) \quad \lambda_ {1} = 0. 6 \quad \mathbf {e} _ {1} = \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right), \quad \lambda_ {2} = 0. 7 \quad \mathbf {e} _ {2} \\ = \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right), \quad \lambda_ {3} = 0. 8 \quad \mathbf {e} _ {3} = \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right) \end{array}
$$

Recall that Eq. (6.5) can be rewritten as follows

$$
\mathbf {N} (t) = \mathbf {A} ^ {t} \cdot \mathbf {N} (0) + (\mathbf {I} - \mathbf {A}) ^ {- 1} \left(\mathbf {I} - \mathbf {A} ^ {t}\right) \mathbf {B} u\tag{9.1}
$$

$$
\mathbf {N} (t) = \mathbf {A} ^ {t} \cdot \mathbf {N} (0) + (\mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} u - (\mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {A} ^ {t} \mathbf {B} u\tag{9.2}
$$

Optimal bundling strategies with three individual items and two bundles: different bundle reservation price range and bundle retention rates varying in the same direction.

<table><tr><td> $a_{AA}$ </td><td> $a_{BB}$ </td><td> $a_{CC}$ </td><td> $a_{ABAB}$ </td><td> $a_{ACAC}$ </td><td>Optimal  $P_A$ </td><td>Optimal  $P_B$ </td><td>Optimal  $P_C$ </td><td>Optimal  $P_{AB}$ </td><td>Optimal  $P_{AC}$ </td><td>Max profit</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0</td><td>0</td><td>$18</td><td>$18</td><td>$14</td><td>$50</td><td>$40</td><td>$10,314</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.1</td><td>0.1</td><td>$18</td><td>$18</td><td>$14</td><td>$50</td><td>$40</td><td>$10,314</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.2</td><td>0.2</td><td>$18</td><td>$18</td><td>$14</td><td>$50</td><td>$40</td><td>$10,314</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.3</td><td>0.3</td><td>$25</td><td>$25</td><td>$14</td><td>$32</td><td>$31</td><td>$10,848</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.4</td><td>0.4</td><td>$25</td><td>$25</td><td>$14</td><td>$32</td><td>$31</td><td>$12,413</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.5</td><td>0.5</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$14,491</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.6</td><td>0.6</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$17,362</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.7</td><td>0.7</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$21,513</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.8</td><td>0.8</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$27,834</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>0.9</td><td>0.9</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$37,964</td></tr><tr><td>0.9</td><td>0.9</td><td>0.6</td><td>1</td><td>1</td><td>$25</td><td>$25</td><td>$15</td><td>$32</td><td>$31</td><td>$54,944</td></tr></table>

Now using the eigen-values and eigen-vectors of A, we have

$$
\mathbf {A} ^ {t} \cdot \mathbf {N} (0) = \lambda_ {1} ^ {t} z _ {1} \mathbf {e} _ {1} + \lambda_ {2} ^ {t} z _ {2} \mathbf {e} _ {2} + \dots + \lambda_ {I} ^ {t} z _ {I} \mathbf {e} _ {I}\tag{9.3}
$$

$$
\mathbf {A} ^ {t} \cdot \mathbf {B} u = \lambda_ {1} ^ {t} w _ {1} \mathbf {e} _ {1} + \lambda_ {2} ^ {t} w _ {2} \mathbf {e} _ {2} + \dots + \lambda_ {I} ^ {t} w _ {I} \mathbf {e} _ {I}\tag{9.4}
$$

where $z _ { 1 } , z _ { 2 } , \cdots , z _ { I }$ and $w _ { 1 } , w _ { 2 } , \cdots , w _ { I }$ are scalars Substituting Eqs. (9.3) and (9.4) into Eq. (9.2), we have

$$
\begin{array}{l} \mathbf {N} (t) = \left(\lambda_ {1} ^ {t} z _ {1} \mathbf {e} _ {1} + \lambda_ {2} ^ {t} z _ {2} \mathbf {e} _ {2} + \dots + \lambda_ {l} ^ {t} z _ {l} \mathbf {e} _ {l}\right) + (\mathbf {I} - \mathbf {A}) ^ {- 1} \cdot \mathbf {B} u \\ \qquad - (\mathbf {I} - \mathbf {A}) ^ {- 1} \cdot \left(\lambda_ {1} ^ {t} w _ {1} \mathbf {e} _ {1} + \lambda_ {2} ^ {t} w _ {2} \mathbf {e} _ {2} + \dots + \lambda_ {l} ^ {t} w _ {l} \mathbf {e} _ {l}\right) \end{array}\tag{9.5}
$$

This equation allows the service provider to predict the long-term behavior of the customer. Recall from our example in Table 1 that $\mathbf { N } ( 0 ) = ( 0 0 0 ) ^ { \mathrm { T } } \mathrm { a n d } u = 1 0$

![](/api/attachments/DYBMEF2C/fulltext/images/ae05d4a346404a23e3d79ae2d52d1d0c82b9a2d6706732473fbbb5b24b226635.jpg)  
Fig. 9. Computation of customer adoption rate $b _ { i } { = } P r [ ( R _ { i } { - } P _ { i } { \geq } 0 ) \cap ( R _ { i } { - } P _ { i } { > } R _ { j } { - } P _ { j } ) ]$

Transition matrices of Case 1. Retentions only, Case 2. Full switching, Case 3.

<table><tr><td colspan="4">A</td><td colspan="3">Eigen-values and corresponding eigen-vectors</td></tr><tr><td rowspan="2">Case 1</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.6 & 0 & 0 \\0 & 0.7 & 0 \\0 & 0 & 0.8\end{pmatrix}$ </td><td>0.6</td><td>0.7</td><td>0.8</td></tr><tr><td> $\begin{pmatrix}1.000 \\0.000 \\0.000\end{pmatrix}$ </td><td> $\begin{pmatrix}0.000 \\1.000 \\0.000\end{pmatrix}$ </td><td> $\begin{pmatrix}0.000 \\0.000 \\1.000\end{pmatrix}$ </td></tr><tr><td rowspan="2">Case 2</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.2 & 0.15 & 0.1 \\0.1 & 0.55 & 0.05 \\0.2 & 0.1 & 0.633\end{pmatrix}$ </td><td>0.134</td><td>0.511</td><td>0.737</td></tr><tr><td> $\begin{pmatrix}-0.925 \\0.182 \\0.334\end{pmatrix}$ </td><td> $\begin{pmatrix}-0.097 \\-0.684 \\0.723\end{pmatrix}$ </td><td> $\begin{pmatrix}0.271 \\0.381 \\0.884\end{pmatrix}$ </td></tr><tr><td rowspan="2">Case 3</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.4 & 0 & 0.1 \\0 & 0.625 & 0.05 \\0.2 & 0.1 & 0.633\end{pmatrix}$ </td><td>0.330</td><td>0.591</td><td>0.737</td></tr><tr><td> $\begin{pmatrix}-0.816 \\-0.097 \\0.570\end{pmatrix}$ </td><td> $\begin{pmatrix}0.283 \\-0.793 \\0.540\end{pmatrix}$ </td><td> $\begin{pmatrix}0.262 \\0.393 \\0.881\end{pmatrix}$ </td></tr></table>

Partial switching N(0) = (0 0 0)<sup>T</sup>, u = 10, and B = (0.25 0.25 0.25)<sup>T</sup>.

Now given an ad hoc price set of (20, 10, 30), we obtain B=(0.25 0.25 0.25)<sup>T</sup>. Therefore,

$$
\mathbf {A} ^ {t} \cdot \mathbf {N} (0) = 0. 6 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right) + 0. 7 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right) + 0. 8 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right)
$$

$$
\mathbf {A} ^ {t} \cdot \mathbf {B} u = 0. 6 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right) + 0. 7 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right) + 0. 8 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right)
$$

The eigen-values are $| \lambda _ { 1 } | < 1 , | \lambda _ { 2 } | < 1 , | \lambda _ { 3 } | < 1$ , which implies that the <sup>fi</sup>rst and third term of Eq. (9.5) approach zero as t increases. Thus the second term becomes dominant when t increases. In this example, as t increases, the vector N(t) eventually reaches $( \mathbf { I } - \mathbf { A } ) ^ { - 1 } { \boldsymbol { \cdot } } \mathbf { B } u = ( 6 . 2 5 $ 8.33 12.5)<sup>T</sup>, which is the equilibrium point of the customer distribution, that is, the distribution of customers among products A, B and AB is 6.25, 8.33 and 12.5 respectively. We consider two additional cases which involve switching behavior of customers. Case 2 re<sup>fl</sup>ects full switching which implies that switching occurs among all the bundles. Case 3, however, re<sup>fl</sup>ects switching between A and AB and B and AB bundles only and hence is named as partial switching. Accordingly, some of the off-diagonal elements of the transition matrix are zero (see Table 5).

The detailed analysis, using eigen-values and corresponding eigenvectors, for predicting future customer distribution is presented in Appendix A. Based on Eq. (9.5), we predict that all three cases converge to a customer distribution of (6.25 8.33 12.5). Since switching occurs across bundles, the magnitude of diagonal elements (retention rates) of Case 2 and Case 3 are smaller than Case 1 where no switching occurs. It implies that as the magnitude of off-diagonal elements increases (switching from other bundles increases), low levels of retention can maintain the same level of customer distribution. To validate the theoretical predictions provided by the model, we conducted 100 separate simulations using randomly generated customers with the system parameters $( R _ { A } , R _ { B } , R _ { A B } , { \bf N } ( 0 )$ and u(t)) as given in Section 4.1. Each customer follows the PDFs of reservation prices and has the probability of transition from a bundle to another as speci<sup>fi</sup>ed in transition matrices of Case 1, Case 2 and Case 3. The results con<sup>fi</sup>rm the predictions as can be seen in Figs. 10–15.

For example, when customer switching among bundles exist as in Case 2, for bundle AB, only about 79% of the retention rate is required to achieve the same level of demand as in Case 1. In Case 1, the number of customers for AB, $N _ { A B } ( t )$ is 12.5 when t=40, which consists of 10 customers who continue to subscribe AB plus 2.5 new customers who adopt AB. However, in Case 2, $N _ { A B } ( t )$ is still 12.5 when t=40 but consists of only 7.91 customers who continue to subscribe AB, 1.25 customers switch from bundle A and 0.83 from bundle B. A similar pattern can be seen for bundles A and B when switching is allowed. Thus our model driven prediction mechanism serves as a valuable decision support tool to analyze the link between customer migration patterns and the long-term demand for various bundles being offered by the service provider. Quantifying this linkage enables managers to develop optimal marketing and production resource allocation plans.

## 6. Conclusions

In this paper, we developed an analytical model, which can be used by a service provider to plan its service bundling strategy. We speci<sup>fi</sup>cally consider both adoption rate of new customers and retention rate of existing customers for each bundle being offered. In our model the bundling strategy takes into account the dynamics and volatility associated with customer migration which could occur over multiple time periods.

Our model indicates that as the bundle retention rate increases the service provider can reduce the bundle price so as to increase its adoption rate by new customers. Although the bundle price is reduced, the high retention rate allows customers to be loyal longer thereby compensating the service provider with increased total lifetime value.

An advantage of dynamic system representation is that it allows the use of eigen-values and eigen-vectors to predict the long-term distribution of customers. We characterized customer migration among the bundles in three different ways, which can be generalized to real-world scenarios, and conducted simulation studies to validate the model properties and provide insights on how future demand stream can be predicted. Our model driven prediction mechanism can serve as an effective and ef<sup>fi</sup>cient decision support tool for optimal allocation of marketing and production resources.

![](/api/attachments/DYBMEF2C/fulltext/images/45e3ea36896a44c8befe679471b633969f2edafeed0b828d6bffe966da8d2a41.jpg)  
Fig. 10. Theoretically predicted number of customers.

$$
\begin{array}{r l} & \mathbf {A} = \\ & \left[ \begin{array}{l l l} 0. 6 & 0 & 0 \\ 0 & 0. 7 & 0 \\ 0 & 0 & 0. 8 \end{array} \right] \end{array}
$$

![](/api/attachments/DYBMEF2C/fulltext/images/91a44aa56d752dbd236336d59241475233f303c9ac748d495b7228cd21775797.jpg)  
Fig. 11. Simulated number of customers.

$$
\mathbf {A} = \left[ \begin{array}{l l l} 0. 2 & 0. 1 5 & 0. 1 \\ 0. 1 & 0. 5 5 & 0. 0 5 \\ 0. 2 & 0. 1 & 0. 6 3 3 \end{array} \right]
$$

![](/api/attachments/DYBMEF2C/fulltext/images/d7544c4c11bb5aa349b169c9023a902cbb02f104eee40ff79214f98b8ba4950b.jpg)  
Fig. 12. Theoretically predicted number of customers.

$$
\mathbf {A} = \left[ \begin{array}{l l l} 0. 2 & 0. 1 5 & 0. 1 \\ 0. 1 & 0. 5 5 & 0. 0 5 \\ 0. 2 & 0. 1 & 0. 6 3 3 \end{array} \right]
$$

![](/api/attachments/DYBMEF2C/fulltext/images/3454952e8a8a90d3591761b0b868d757e961d3be6534a26d97f5823fccd92880.jpg)  
Fig. 13. Simulated number of customers.

$$
\mathbf {A} = \left[ \begin{array}{l l l} 0. 4 & 0 & 0. 1 \\ 0 & 0. 6 2 5 & 0. 0 5 \\ 0. 2 & 0. 1 & 0. 6 3 3 \end{array} \right]
$$

![](/api/attachments/DYBMEF2C/fulltext/images/e6ed045ed71073425edbaa46533117346eac8bd536ff6de7b6d210670761b608.jpg)  
Fig. 14. Theoretically predicted number of customers.

![](/api/attachments/DYBMEF2C/fulltext/images/4687bd68b1b0db8943fbafe0978891f2ce054354b241ef7d18f94cb43157fa9d.jpg)  
Fig. 15. Simulated number of customers

The monotonicity condition derived from our model can signi<sup>fi</sup>- cantly reduce the computational burden. We showed that when the bundle retention rate is greater than either of the individual component retention rates and if pure bundling strategy is optimal for one period then the condition ensures that the same strategy will solve the multi-period problem and the optimal price set remains the same for all the multiple time periods as well.

Although we developed analytical properties, provided numerical illustrations, and conducted simulations to validate the results, it will be helpful to empirically test the proposed model with real-world data as this would enable further model re<sup>fi</sup>nement and to sharpen the managerial insights. This in turn would form a basis for developing a practical decision support tool. This is a fruitful avenue for future research.

## Appendix A. Transition matrices

Case 1 Retentions only Case 2. Full switching Case 3. Partial switching ${ \bf N } ( 0 ) = ( 0 0 0 ) ^ { \mathrm { T } } , u = 1 0 ,$ , and $\mathbf { B } = ( 0 . 2 5 0 . 2 5 0 . 2 5 ) ^ { \mathrm { T } }$

<table><tr><td></td><td colspan="3">A</td><td colspan="3">Eigen-values and corresponding eigen-vectors</td></tr><tr><td rowspan="2">Case 1</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.6 & 0 & 0 \\0 & 0.7 & 0 \\0 & 0 & 0.8\end{pmatrix}$ </td><td>0.6</td><td>0.7</td><td>0.8</td></tr><tr><td> $\begin{pmatrix}1.000 \\0.000 \\0.000\end{pmatrix}$ </td><td> $\begin{pmatrix}0.000 \\1.000 \\0.000\end{pmatrix}$ </td><td> $\begin{pmatrix}0.000 \\0.000 \\1.000\end{pmatrix}$ </td></tr><tr><td rowspan="2">Case 2</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.2 & 0.15 & 0.1 \\0.1 & 0.55 & 0.05 \\0.2 & 0.1 & 0.633\end{pmatrix}$ </td><td>0.134</td><td>0.511</td><td>0.737</td></tr><tr><td> $\begin{pmatrix}-0.925 \\0.182 \\0.334\end{pmatrix}$ </td><td> $\begin{pmatrix}-0.097 \\-0.684 \\0.723\end{pmatrix}$ </td><td> $\begin{pmatrix}0.271 \\0.381 \\0.884\end{pmatrix}$ </td></tr><tr><td rowspan="2">Case 3</td><td rowspan="2" colspan="3"> $\begin{pmatrix}0.4 & 0 & 0.1 \\0 & 0.625 & 0.05 \\0.2 & 0.1 & 0.633\end{pmatrix}$ </td><td>0.330</td><td>0.591</td><td>0.737</td></tr><tr><td> $\begin{pmatrix}-0.816 \\-0.097 \\0.570\end{pmatrix}$ </td><td> $\begin{pmatrix}0.283 \\-0.793 \\0.540\end{pmatrix}$ </td><td> $\begin{pmatrix}0.262 \\0.393 \\0.881\end{pmatrix}$ </td></tr></table>

Case 1. From Eq. (9.3)

$$
\mathbf {A} ^ {t} \cdot \mathbf {N} (0) = 0. 6 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right) + 0. 7 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right) + 0. 8 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right)
$$

From Eq. (9.4)

$$
\mathbf {A} ^ {t} \cdot \mathbf {B} u = 0. 6 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 1 \\ 0 \\ 0 \end{array} \right) + 0. 7 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0 \\ 1 \\ 0 \end{array} \right) + 0. 8 ^ {t} \cdot (2. 5) \cdot\tag{\( \begin{pmatrix}0\\ 0\\ 1\end{pmatrix} \}
$$

From Eq. (9.5)

$$
\lim _ {t \rightarrow \infty} \mathbf {N} (t) = (\mathbf {I} - \mathbf {A}) ^ {- 1} \cdot \mathbf {B} u = (6. 2 5 8. 3 3 1 2. 5) ^ {\mathrm{T}}
$$

Case 2. From Eq. (9.3)

$$
\begin{array}{l} \mathbf {A} ^ {t} \cdot \mathbf {N} (0) = 0. 1 3 4 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} - 0. 9 2 5 \\ 0. 1 8 2 \\ 0. 3 3 4 \end{array} \right) + 0. 5 1 1 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} - 0. 0 9 7 \\ - 0. 6 8 4 \\ 0. 7 2 3 \end{array} \right) \\ + 0. 7 3 7 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0. 2 7 1 \\ 0. 3 8 1 \\ 0. 8 8 4 \end{array} \right) \end{array}
$$

From Eq. (9.4)

$$
\begin{array}{l} \mathbf {A} ^ {t} \cdot \mathbf {B} u = 0. 1 3 4 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} - 0. 9 2 5 \\ 0. 1 8 2 \\ 0. 3 3 4 \end{array} \right) + 0. 5 1 1 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} - 0. 0 9 7 \\ - 0. 6 8 4 \\ 0. 7 2 3 \end{array} \right) \\ + 0. 7 3 7 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0. 2 7 1 \\ 0. 3 8 1 \\ 0. 8 8 4 \end{array} \right) \end{array}
$$

From Eq. (9.5)

$$
\lim _ {t \rightarrow \infty} \mathbf {N} (t) = (\mathbf {I} - \mathbf {A}) ^ {- 1} \cdot \mathbf {B} u = (6. 2 5 8. 3 3 1 2. 5) ^ {\mathrm{T}}
$$

Case 3. From Eq. (9.3)

$$
\begin{array}{l} \mathbf {A} ^ {t} \cdot \mathbf {N} (0) = 0. 3 3 0 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} - 0. 8 1 6 \\ - 0. 0 9 7 \\ 0. 5 7 0 \end{array} \right) + 0. 5 9 1 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0. 2 8 3 \\ - 0. 7 9 3 \\ 0. 5 4 0 \end{array} \right) \\ + 0. 7 3 7 ^ {t} \cdot 0 \cdot \left( \begin{array}{c} 0. 2 6 2 \\ 0. 3 9 3 \\ 0. 8 8 1 \end{array} \right) \end{array}
$$

From Eq. (9.4)

$$
\begin{array}{l} \mathbf {A} ^ {t} \cdot \mathbf {B} u = 0. 3 3 0 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} - 0. 8 1 6 \\ - 0. 0 9 7 \\ 0. 5 7 0 \end{array} \right) + 0. 5 9 1 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0. 2 8 3 \\ - 0. 7 9 3 \\ 0. 5 4 0 \end{array} \right) \\ + 0. 7 3 7 ^ {t} \cdot (2. 5) \cdot \left( \begin{array}{c} 0. 2 6 2 \\ 0. 3 9 3 \\ 0. 8 8 1 \end{array} \right) \end{array}
$$

From Eq. (9.5)

lim $\mathbf { N } ( t ) = \left( \mathbf { I } - \mathbf { A } \right) ^ { - 1 } { \cdot } \mathbf { B } u \ = \left( 6 . 2 5 \ 8 . 3 3 \ 1 2 . 5 \right) ^ { T }$ t→∞

## References

[1] A. Ansari, S. Siddarth, C.B. Weinberg, Pricing a bundle of products or services: the case of nonpro<sup>fi</sup>ts, Journal of Marketing Research 33 (1) (1996) 86–93.

[2] Y. Bakos, E. Brynjolfsson, Bundling information goods: pricing, pro<sup>fi</sup>ts, and ef<sup>fi</sup>ciency, Management Science 45 (12) (1999) 1613–1630.

[3] H. Estelami, Consumer savings in complementary product bundles, Journal of Marketing Theory and Practice 7 (3) (1999) 107–114.

[4] X. Geng, M.B. Stinchcombe, A.B. Whinston, Bundling information goods of decreasing value, Management Science 51 (4) (2005) 662–667.

[5] W. Hanson, R.K. Martin, Optimal bundle pricing, Management Science 36 (2) (1990) 155–174.

[6] M.A. Koschat, W.P. Putsis Jr., Audience characteristics and bundling: a hedonic analysis of magazine advertising rates, Journal of Marketing Research 39 (2) (2002) 262–273.

[7] D.G. Luenberger, Introduction to dynamic systems: theory, models, and applications John Wiley & Sons, 1979.

[8] W.J. Reinartz, V. Kumar, On the pro<sup>fi</sup>tability of long-life customers in a noncontractual setting: an empirical investigation and implications for marketing Journal of Marketing 64 (4) (2000) 17–35.

[9] M.A. Salinger, A graphical analysis of bundling, Journal of Business 68 (1) (1995) 85–98.

[10] D.C. Schmittlein, D.G. Morrison, R. Colombo, Counting your customers: who are they and what will they do next? Management Science 33 (1) (1987) 1–24.

[11] D. Soman, J.T. Gourville, Transaction decoupling: how price bundling affects the decision to consume, Journal of Marketing Research 38 (1) (2001) 30–44.

[12] S. Stremersch, G.J. Tellis, Strategic bundling of products and prices: a new synthesis for marketing, Journal of Marketing 66 (1) (2002) 55–72.

[13] R. Venkatesh, V. Mahajan, A probabilistic approach to pricing a bundle of products, Journal of Marketing Research 30 (4) (1993) 494–508.

[14] G. Wuebker, Bundles' effectiveness is often undermined, Marketing News 36 (6) (2002) 9–10.

[15] M.S. Yadav, How buyers evaluate product bundles: a model of anchoring and adjustment, Journal of Consumer Research 21 (2) (1994) 342–353.

[16] M.S. Yadav, K.B. Monroe, How buyers perceive savings in a bundle price, Journal of Marketing Research 30 (3) (1993) 350–358.

![](/api/attachments/DYBMEF2C/fulltext/images/67951313b2dde607fa6986fb8d4bfe784ca563b93e4a5939efab62b2978651ac.jpg)

Seokjoo Andrew Chang is an Assistant Professor of Information Systems at SUNY, Albany. He received his Ph.D. in Operations and Information Management from the University of Connecticut in 2006. His research interests include economics of information systems, stochastic decision processes, and operations management. His papers have been presented in major MIS conferences and workshops such as WISE and WITS.

![](/api/attachments/DYBMEF2C/fulltext/images/169820eff44065d3e6aa7d415a0dea4b74a2af68d90f88965deabd8016b126db.jpg)

Giri Kumar Tayi is a Professor of Management Science and Information Systems at SUNY, Albany. His research interests are in the areas of information systems, operations management and operations research. His interests include information quality, modeling and analysis of communication networks, data mining and knowledge discovery, interorganizational information integration and information security His research has appeared in Management Science, Operations Research, MIS Quarterly, IEEE Transactions on Systems, Man and Cybernetics, INFORMS Journal on Computing, EJOR, Networks and several other journals. He serves on the editorial board of Information Technology & Management, Information Systems Frontiers and Information & Manage-

ment. He has also co-guest edited several special issues for journals such as EJOR, Communications of ACM. In addition he serves on the program committees of several academic conferences.
