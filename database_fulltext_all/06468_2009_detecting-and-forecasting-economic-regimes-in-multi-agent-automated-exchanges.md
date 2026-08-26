---
otero_id: 6468
otero_key: "9D56NCBG"
title: "Detecting and forecasting economic regimes in multi-agent automated exchanges"
authors: "Wolfgang Ketter; John Collins; Maria Gini; Alok Gupta; Paul Schrater"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.05.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Detecting and forecasting economic regimes in multi-agent automated exchanges

Wolfgang Ketter <sup>a,</sup>⁎, John Collins <sup>b</sup>, Maria Gini <sup>b</sup>, Alok Gupta <sup>c</sup>, Paul Schrater <sup>b</sup>

<sup>a</sup> Department of Decision and Information Sciences, Rotterdam Sch. of Mgmt., Erasmus University, 3000 DR Rotterdam, Netherlands

<sup>b</sup> Department of Computer Science and Engineering, University of Minnesota, Minneapolis, MN 55455, USA

<sup>c</sup> Carlson School of Management, University of Minnesota, Minneapolis, MN 55455, USA

## a r t i c l e i n f o

Available online 21 May 2009

Keywords: Trading agents Agent-mediated electronic commerce Machine learning Market forecasting Dynamic pricing

## a b s t r a c t

We show how an autonomous agent can use observable market conditions to characterize the microeconomic situation of the market and predict market trends. The agent can use this information for tactical decisions, such as pricing, and strategic decisions, such as product mix and production planning. We present methods to learn dominant market conditions, such as over-supply or scarcity, from historical data using Gaussian mixture models We show how this model combined with real-time observable information is used to identify the current dominant market condition and to forecast market changes over a planning horizon. Market changes are forecast via both a Markov correction–prediction process and an exponential smoother. Empirical analysis shows that the exponential smoother yields more accurate predictions for the current and next day (supporting tactical decisions), while the Markov process is better for longer term predictions (supporting strategic decisions). Our approach offers more <sup>fl</sup>exibility than traditional regression based approaches, since it does not assume a <sup>fi</sup>xed functional relationship between dependent and independent variables. We validate our methods by presenting experimental results in a case study, the Trading Agent Competition for Supply Chain Management.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Business organizations seeking advantage are increasingly looking to automated decision support systems. In recent years, these systems have become increasingly sophisticated. Advanced decision support systems are evolving into software agents that can act rationally on behalf of their users in a variety of application areas. Examples include procurement [31,7], scheduling and resource management [15,4], and personal information management [2,25].

In this paper, we show how machine learning techniques can be used to support rational decision making in competitive sales environments. We are particularly interested in environments that are constrained by capacity and material availability, and that are characterized by limited visibility of signi<sup>fi</sup>cant factors, such as the inventory positions of competitors. Such environments exist in virtually all manufacturing industries. They are more interesting for our present study than other environments where either capacity or materials are not constrained. For example, in the airline industry capacity is constrained but material is typically not a major constraint. In <sup>fi</sup>nancial markets, neither capacity nor materials are real constraints. We focus on these types of complex problems because it is easier to transfer results from complex situations to simpler ones.

Our method characterizes market conditions by detecting distinguishable statistical patterns in historical data and uses those patterns to classify the range of economic environments that a system is expected to encounter in the future. By distinguishable pattern we mean a pattern which has computationally identi<sup>fi</sup>able properties such as price, inventory, or demand. These patterns are obtained by clustering historical data, and identifying, via a semi-supervised approach, clusters that re<sup>fl</sup>ect qualitatively distinct economic conditions. We call these patterns economic regimes.

We outline how to identify regimes from observable data and how to forecast regime transitions. This prediction, in turn, can be used to allocate resources to current and future sales in a way that maximizes resource value. While this type of prediction about the economic environment is commonly used at the macro economic level [28], such predictions are rarely used at the micro economic level.

Because economic regimes re<sup>fl</sup>ect qualitative distinctions in the economic environment, they can be used to drive decision criteria for both short-term (tactical) and medium-to-long term (strategic) decisions. For example, suppose we are in an environment where there is balance in supply and demand, but we predict that supply will outstrip demand in the near future. We might decide to lower our prices to reduce inventory and slow the acquisition of raw materials. However, if we predict that in future demand will outstrip supply, we may want to raise prices and increase our acquisition of raw materials. Therefore, identi<sup>fi</sup>cation and prediction of regimes can help with tactical (pricing) and strategic (procurement) planning.

After a review of the relevant literature, we describe the information an agent needs to make strategic and tactical sales decisions. This is followed by a discussion of the concept of “economic regimes” and their representation using learned probability density functions. We demonstrate our approach in the context of an autonomous agent that is designed to compete in the Trading Agent Competition for Supply Chain Management (TAC SCM) [6]. A TAC SCM agent must make resource allocation and pricing decisions using the limited visible information about the state of the market. Agents must simultaneously compete in two separate but interrelated markets: the market from which the agents must buy their supplies and the market to which the agents must sell their <sup>fi</sup>nished products. Agents have a large number of decisions to make in a limited time, so computational ef<sup>fi</sup>ciency of the decision-making process is essential.

While it is conceivable that in future more operations will be conducted with greater levels of autonomy by computer systems (similar to stock trading on Nasdaq), such systems are currently not extensively deployed. TAC SCM affords a rich but risk free environment for testing economic decision processes. A simulated environment, such as TAC SCM, has also the advantage that we can set it up to enable repeating experiments with different algorithms and parameters [33]. This allows us to tease apart subtle interactions among decision processes in the agent and in its interactions with the other agents that would be hard to <sup>fi</sup>nd and study in the real world.

In addition to the supply-chain trading example we present here, there are many other domains that could bene<sup>fi</sup>t from our approach. Examples include agents for automated trading in <sup>fi</sup>nancial markets, such as the Penn-Lehman Automated Trading Project [16], auctionbased contracting environments, such as MAGNET [5], and other auctions, such as auctions for IBM PCs [24] or PDA's on eBay [11].

Our approach contributes to the research and development of Smart Business Networks (SBN) [37,36] since it creates value through providing regimes as a tool to gather network knowledge and to facilitate decision making, both for humans and for autonomous software agents. Simulations like TAC SCM help to construct and test economic models of real world SBNs.

For reading convenience, we present a summary of our notation in Appendix A.

## 2. Literature review

Human and automated decision makers are often faced with the need to predict prices. Kephart et al. [17] explored several dynamic pricing algorithms for information goods, where shopbots look for the best price, and pricebots adapt their prices to attract business. Wellman [39] compared approaches used by agents to predict hotel and <sup>fl</sup>ight prices in the TAC classic game. He analyzed the approaches and developed metrics, such as the Euclidean distance between the predicted and the actual price.

Massey and Wu [26] show in their analysis that the ability of decision makers to correctly identify the onset of a new regime can be the difference between success and failure. Furthermore they found strong evidence that individuals pay inordinate attention to the signal (price in our case), and neglect diagnosticity (regime probabilities) and transition probability (Markov matrix), the aspects of the system that generates the signal. Individuals who do not pay enough attention to regime identi<sup>fi</sup>cation and prediction have the tendency to overor under-react to market conditions, since they have dif<sup>fi</sup>culties in distinguishing the signal from the noise.

Ghose et al. [12] empirically analyze the degree to which used products cannibalize new product sales for books on Amazon.com. In their study they show that product prices go through different regimes over time. Marketing research methods have been developed to understand the conditions for growth in performance and the role that marketing actions can play to improve sales. For instance, in [30], an analysis is presented on how in mature economic markets strategic windows of change alternate with long periods of stability.

Much work has focused on models for rational decision-making in autonomous agents. Ng and Russell [27] show that an agent's decisions can be viewed as a set of linear constraints on the space of possible utility (reward) functions. However, the simple reward structure they used in their experiments will not scale to predict prices in more complex situations such as TAC SCM or indeed most real-world markets.

Sales strategies used in previous TAC SCM competitions have attempted to model the probability of receiving an order for a given offer price, either by estimating the probability by linear interpolation of the minimum and maximum daily prices [29], or by estimating the relationship between offer price and order probability with a linear cumulative density function (CDF) [1], or by using a reverse CDF and factors such as quantity and due date [19]. The Jackaroo team [40] applied a game theoretic approach to set offer prices, using a variation of the Cournot game for modeling the product market. The SouthamptonSCM [13] team used fuzzy reasoning to set offer prices. Similar techniques have been used outside TAC SCM to predict offer prices in <sup>fi</sup>rst price sealed bid reverse auctions for IBM PCs [24] or PDA's on eBay [11].

In [20] the authors demonstrate a method for predicting future customer demand in the TAC SCM game environment, and use the predicted future demand to inform agent behavior. Their approach is speci<sup>fi</sup>c to the TAC SCM situation, since it depends on knowing the formula by which customer demand is computed. Note also that customer demand is only one of the factors that characterizes the multi-dimensional regime parameter space, and is not by itself a good short-term predictor of prices.

All these methods fail to take into account market conditions that are not directly observable. They are essentially regression models, and do not represent qualitative differences in market conditions. Our method, in contrast, is able to detect and forecast a broader range of market conditions. Regression based approaches (including nonparametric variations) assume that the functional form of the relationship between dependent and independent variables has a consistent structure. Our approach models variability directly and does not assume a well-de<sup>fi</sup>ned functional relationship.

An analysis [21] of the TAC SCM 2004 competition shows that supply and demand (which are expressed as regimes in our method) are key factors in determining market prices, and that agents which were able to detect and exploit these conditions had an advantage.

## 3. Tactical and strategic decisions

We are primarily interested in competitive market environments that are constrained by resources or production capacity or both. In such environments, a manager who wants to maximize the value of available resources should be concerned about both strategic and tactical decisions. The basic strategic decision is how to allocate the available resources (<sup>fi</sup>nancial, production capacity, inventory, etc.) over some time horizon in a way that is expected to return the maximum yield. For example, in a market that has a strong seasonal variation, one might want to build up an inventory of <sup>fi</sup>nished goods during the off season, when demand is low and prices are weak, in order to prepare for an expected period of high demand and strong prices.

For the purpose of this paper, tactical decisions are concerned with setting prices to maximize pro<sup>fi</sup>t within the parameters set by the strategic decisions. So, for instance, if the forecast sales volume for the current week is 100,000 units, we would want to <sup>fi</sup>nd the highest sales price that would move that volume. According to ef<sup>fi</sup>cient market theory [10], prices subsume information about customer demand and other relevant factors. Therefore, with a good method for predicting prices we implicitly account for the other factors that are encoded in the price.

Our technique of modeling economic regimes can be used to inform both the strategic and tactical decision processes. Fig. 1 shows in a schematic way how on-line regime identi<sup>fi</sup>cation and prediction can support these processes.

In our formulation, a regime is essentially a distribution of prices over sales volume. At the tactical level, by modeling the probability of selling a product at a given price and combining that probability with demand values, we obtain directly pricing decisions. In other words, we are able to <sup>fi</sup>nd a good approximation of the highest price the market will support for a given sales volume.

In order to take advantage of regimes to inform the strategic decision process, we need to forecast regime shifts in the market. In our formulation, regime prediction is done either as a Markov correction–prediction process or using a double exponential smoother, as we will show later in Section 4.3. If the forecast shows an upcoming period of low demand and weak prices, the agent needs to sell more aggressively in the short term, and limit procurement and production to prevent driving the market into oversupply. On the other hand, if the forecast shows an upcoming period of high demand and strong prices, the agent needs to increase procurement and production and raise short-term prices, in order to be well-positioned for the future.

## 4. Economic regimes

Market conditions change over time, and this should affect the strategy used in procurement, production planning, and product pricing. Different market conditions relate to different points on the supply and demand curves [14]. The law of supply and demand states that the equilibrium market price of a product is the intersection of consumer demand curve and producer supply curve.

We de<sup>fi</sup>ne a “scarcity” condition [8] when demand is elastic relative to supply, giving suppliers pricing power. This commonly occurs when market demand exceeds supplier capacity, at least temporarily. Oversupply occurs when supply is elastic relative to demand, and prices are not strongly affected by demand. Faced with an oversupply situation, the agent should primarily control costs, and therefore either price based on costs, or wait for better market conditions. A “balanced” market is not dominated by effects of elasticity. In balanced situations, prices are affected by variations in both demand and supply, so the agent has a range of options for maximizing expected pro<sup>fi</sup>t.

Our approach can be used to support decisions in both the procurement and sales markets. In the procurement market, we may have little or no control over the availability of parts, but we can control the usable supply to a certain degree. When there is scarcity of parts, the prices for parts will increase. It is common that scarcity of parts results from excess demand for parts, which is likely to occur when demand for associated products is high. This is precisely why prediction of regimes is important. If we can predict future demand (via prices) well, then we may decide to acquire materials early, thereby reducing prices for material and increasing our pro<sup>fi</sup>t margin.

![](/api/attachments/9D56NCBG/fulltext/images/d8118c3b6d12dbe90d0dc6ca029094aaf5940c4b0a1f45675961eb1e3b7dfe48.jpg)  
Fig. 1. Process chart. Regime identi<sup>fi</sup>cation is a tool for tactical decision making, regime prediction is a tool for strategic decision making.

Rapidly changing market conditions are often observed with commodities, such as oil or semiconductor chips. Such markets often experience high price volatility. For instance, the price of oil might go up due to shortage in supply or to inventories build up due to a softening demand in Asia. We believe that even though a market may be constantly changing, there are some underlying dominant patterns or economic regimes that characterize market conditions. Agents can guide their decision processes by mapping observed market conditions to a learned regime model and by predicting regime shifts over a planning horizon, as we describe in the following sections.

We use the term “order probability” with respect to price to represent the probability that an active customer (a customer who accepts an offer from some seller) will accept an offer at a particular price. If the market is in a scarcity condition, order probability remains high up to relatively high pro<sup>fi</sup>t margins. The contrary is true if the market is in an oversupply situation. In this case, pro<sup>fi</sup>t margins are low, and a small price increase will dramatically reduce the probability of order. In balanced situations the probability of order curve is between those two extremes. Fig. 2 shows curves for the probability of receiving an order as a function of offer price depending on the regime (left) or the time in the market (right). As we can see in the <sup>fi</sup>gure, the slope of the curve and its position changes over time as market conditions change.

Our approach includes (1) an off-line learning phase, where historical data are used to characterize the regimes, and (2) an online phase where current market data are used to identify the dominant regime and to make predictions.

## 4.1. Analysis of historical data to characterize market regimes

The <sup>fi</sup>rst phase in our approach is to identify and characterize market regimes by analyzing data from past sales.

Our model makes three speci<sup>fi</sup>c assumptions about availability and quality of data. First, we assume that suf<sup>fi</sup>cient, relevant historical data are available for analysis. Second, we assume that the historical data are suf<sup>fi</sup>ciently representative of present and future market conditions. Third, to support online identi<sup>fi</sup>cation of regimes, we assume that some price information is available in real time.

Since product prices are likely to have different ranges for different products, we normalize them. We call $\mathrm { n p } _ { \mathrm { g } }$ the normalized price for good g and de<sup>fi</sup>ne it as follows:

$$
\begin{array}{r l} \mathrm{np} _ {g} & = \frac {\text {ProductPrice} _ {g}}{\text {NominalProductCost} _ {g}} \\ & = \frac {\text {ProductPrice} _ {g}}{\text {AssemblyCost} _ {g} + \sum_ {j = 1} ^ {\text {numParts}} \text {NominalPartCost} _ {g , j}} \end{array}\tag{1}
$$

where NominalPartCos $t _ { \mathrm { g } , j }$ is the nominal cost of the j-th part for good ${ \boldsymbol { g } } ,$ numParts is the number of parts needed to make the good $^ { g , }$ and Assembly $\mathrm { \Delta } _ { \mathrm { \cdot } } O S t _ { \mathrm { g } }$ is the cost of manufacturing the good g. An advantage of using normalized prices is that we can easily compare price patterns across different products. In the following, for simplicity of notation, we use np instead of $\mathrm { n p } _ { \mathrm { g } } .$

Historical data are used to estimate the price density, p(np), and to characterize regimes. We start by <sup>fi</sup>tting a Gaussian mixture model (GMM) [35] to historical normalized price data. We use a GMM since it is able to approximate arbitrary density functions. Another advantage is that the GMM is a semi-parametric approach which allows for fast computing and uses less memory than other approaches.

In this paper, we present results using a GMM with <sup>fi</sup>xed means, μ , and <sup>fi</sup>xed variances, $\sigma _ { i } ,$ since we want one set of Gaussians to work for all cases off-line and online. We use the Expectation-Maximization (EM) Algorithm [9] to determine the prior probability, $P ( \zeta _ { i } )$ , of the

Balanced:  
![](/api/attachments/9D56NCBG/fulltext/images/6886a8cf2865ca262ad9dd42134e05eb85af1030ca1d6e0727655ec9a5cd7cb9.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/c1ae100c22e239c321274d83f729aca0558e446662ee96fef292af3c1779ef05.jpg)  
Extreme Oversupply:

![](/api/attachments/9D56NCBG/fulltext/images/ac42026f14dc977052441f472280df7e7f6dce877e9398e375c773f7f35cc92b.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/b7f47de2352bd4c720bb2b317915ff94ce9da29eb4f1c85873cfbe085b33adf5.jpg)  
Fig. 2. The reverse cumulative price density function represents the probability of order by price. The <sup>fi</sup>gure shows order probability curves for the medium market in a TAC SCM game during regimes of extreme scarcity (left top), balanced (left middle) and extreme oversupply (left bottom). The <sup>fi</sup>gure also shows (right) experimental order probability curves, computed every twenty days, during one of the games.

Gaussian components of the GMM. The means, $\mu _ { i } ,$ are uniformly distributed and the variances, $\sigma _ { i } ^ { 2 } ,$ , tile the space. Speci<sup>fi</sup>cally variances were chosen so that adjacent Gaussians are two standard deviations apart.

The density of the normalized price can be written as:

$$
p (\mathrm{np}) = \sum_ {i = 1} ^ {N} p (\mathrm{np} | \zeta_ {i}) P (\zeta_ {i})\tag{2}
$$

where $p ( \mathfrak { n p } | \zeta _ { i } )$ is the i-th Gaussian from the GMM, i.e.,

$$
p (\mathrm{np} | \zeta_ {i}) = p (\mathrm{np} | \mu_ {i}, \sigma_ {i}) = \frac {1}{\sigma_ {i} \sqrt {2 \pi}} e ^ {\left[ \frac {- (\mathrm{np} - \mu_ {i}) ^ {2}}{2 \sigma_ {i} ^ {2}} \right]}\tag{3}
$$

where $\mu _ { i }$ is the mean and $\sigma _ { i }$ is the standard deviation of the i-th Gaussian from the GMM. An example of a GMM is shown in Fig. 3. While the choice of N, the number of Gaussians, in a GMM is arbitrary, the choice should re<sup>fl</sup>ect a balance between accuracy and computational overhead. By accuracy we mean prediction accuracy, which is not the same as <sup>fi</sup>t accuracy. Creating a model with a very good <sup>fi</sup>t to the observed data does not always translate well into good predictions. The more degrees of freedom the model has, the higher is the likelihood of over<sup>fi</sup>tting the data.

Using Bayes' rule we determine the posterior probabilities for each Gaussian $\zeta _ { i } \colon$

$$
P (\zeta_ {i} | \mathrm{np}) = \frac {p (\mathrm{np} | \zeta_ {i}) P (\zeta_ {i})}{\sum_ {i = 1} ^ {N} p (\mathrm{np} | \zeta_ {i}) P (\zeta_ {i})} \forall i = 1, \dots , N\tag{4}
$$

We then de<sup>fi</sup>ne the posterior probabilities of all Gaussians given the normalized price, np, as the following N-dimensional vector:

$$
\overrightarrow {\eta} (\mathrm{np}) = [ P (\zeta_ {1} | \mathrm{np}), P (\zeta_ {2} | \mathrm{np}), \dots , P (\zeta_ {N} | \mathrm{np}) ].\tag{5}
$$

For each observed normalized price np we compute the vector of the posterior probabilities, $\overrightarrow { \eta } ( \mathrm { n p } _ { j } )$ , which is $\overrightarrow { \eta }$ evaluated at each observed normalized price np .

The intuitive idea of a regime as a recurrent economic condition is captured by discovering price distributions that recur across time periods in the market. We de<sup>fi</sup>ne regimes by clustering price distributions over time periods using the k-means algorithm with a similarity measure on the probability vectors $\overrightarrow { \eta } ( \mathrm { n p } _ { j } )$ and normalized prices np. The clusters found by this method correspond to frequently occurring price distributions with support on contiguous ranges of np.<sup>1</sup>

![](/api/attachments/9D56NCBG/fulltext/images/6a56d5580e400a851d40f42cfb8e04555d154936d17700029b4c869a0da5a662.jpg)  
Fig. 3. The price density function, p(np), (right y-axis) estimated by a Gaussian mixture model with 16 components <sup>fi</sup>ts well the historical normalized price data (left y-axis represents product quantity) for a sample market. Data are from 18 games from the semi-<sup>fi</sup>nals and <sup>fi</sup>nals of TAC SCM 2005.

The center of each cluster (ignoring the last component which contains the rescaled price information) is a probability vector that corresponds to regime $r = R _ { k }$ for $k = 1 , \cdots , M ,$ where M is the number of regimes. Collecting these vectors into a matrix yields the conditional probability matrix P(ζ|r). The matrix has N rows, one for each component of the GMM, and M columns, one for each regime.

We marginalize the product of the density of the normalized price, np, given the i-th Gaussian of the GMM, p(np|ζ<sub>i</sub>), and the conditional probability clustering matrix, $P ( \zeta _ { i } | R _ { k } )$ , over all Gaussians $\zeta _ { i } .$ We obtain the density of the normalized price np dependent on the regime $R _ { k } \mathrm { : }$

$$
p (\mathrm{np} | R _ {k}) = \sum_ {i = 1} ^ {N} p (\mathrm{np} | \zeta_ {i}) P (\zeta_ {i} | R _ {k}).\tag{6}
$$

The probability of regime $R _ { k }$ dependent on the normalized price np can be computed using the Bayes rule as:

$$
P (R _ {k} | \mathrm{np}) = \frac {p (\mathrm{np} | R _ {k}) P (R _ {k})}{\sum_ {k = 1} ^ {M} p (\mathrm{np} | R _ {k}) P (R _ {k})} \forall k = 1, \dots , M.\tag{7}
$$

where M is the number of regimes. The prior probabilities, $P ( R _ { k } )$ , of the different regimes are determined by a counting process over past data. Fig. 4 depicts the regime probabilities for a sample market in TAC SCM. Each regime is clearly dominant over a range of normalized prices.

The intuition behind regimes is that prices communicate information about future expectations of the market. However, absolute prices do not mean much because the same price point can be achieved in a static mode (i.e., when prices don't change), when prices are increasing, or when prices are decreasing. Regimes provide a better assessment of market conditions.

In our experiments we tried different numbers of Gaussians for the GMM, typically 16 and 25, as discussed later in Section 6, and different numbers of regimes, typically 3 or 5. We found out that the number of regimes does not signi<sup>fi</sup>cantly affect the results regarding price trend predictions. We also tried k-means clustering with different initial conditions, but it consistently converged to the same results. More details are given in [18].

In Fig. 4 we distinguish <sup>fi</sup>ve regimes, which we can call extreme oversupply $\left( R _ { 1 } \right)$ , oversupply $\left( R _ { 2 } \right)$ , balanced $\left( R _ { 3 } \right)$ , scarcity $\left( R _ { 4 } \right)$ , and extreme scarcity $\left( R _ { 5 } \right)$ . We decided to use <sup>fi</sup>ve regimes instead of the three basic regimes which are suggested by economic theory because in this way we are able to isolate outlier regimes, such as extreme oversupply (price war) and extreme scarcity (temporary monopoly), in a market. Regimes $R _ { 1 }$ and $R _ { 2 }$ represent a situation where there is a glut in the market, i.e. an oversupply situation, which depresses prices. Regime $R _ { 3 }$ represents a balanced market situation, where most of the demand is satis<sup>fi</sup>ed. In regime $R _ { 3 }$ the agent has a range of options of price vs sales volume. Regimes $R _ { 4 }$ and $R _ { 5 }$ represent a situation where there is scarcity of products in the market, which increases prices.

## 4.2. Online identification of dominant regime

After historical sales data have been used to characterize different market regimes, an agent can use this information in real-time to identify the dominant regime. This can be done by estimating the normalized prices for the current time step. Time is discretized either in days, like in TAC SCM, or in other time units relevant to the domain.

Since complete current price information might not be available, we indicate the estimated normalized price at time t by $\overline { { n p } } _ { t }$ Depending on the application domain, the price estimate can be accurate, or can be an approximation, as shown later for TAC SCM in Section 5.2.

The current dominant regime is the one which has the highest probability, i.e.

$$
\widetilde {R} _ {c} s. t. c = \underset {1 \leq k \leq M} {\operatorname{argmax}} \overrightarrow {P} \left(R _ {k} | \widetilde {\mathrm{np}} _ {t}\right).\tag{8}
$$

## 4.3. Online regime prediction

We model the prediction of future regimes in two different ways, as a Markov correction–prediction process, and using an exponential smoother.

## 4.3.1. Markov correction–prediction

We construct a Markov transition matrix, $\mathbf { T } ( r _ { d + 1 } | r _ { d } ) ,$ which represents the posterior probability of transitioning at time $d + 1$ to

![](/api/attachments/9D56NCBG/fulltext/images/839a41f8f31b3590dda942fe23e5ab96da21c0cc0509db4d8670a25ef9f7fb90.jpg)

Fig. 4. An example of learned regime probabilities, P(R |np), over normalized price np, with <sup>fi</sup>ve regimes for a sample market in TAC SCM after training.

![](/api/attachments/9D56NCBG/fulltext/images/117b0cc3aa7578297dc8cab7a0b0509aa9b0d0a7806976890f3307cf066ff70f.jpg)  
Fig. 5. Schematic overview of a typical TAC SCM game scenario.

regime $r _ { d + 1 }$ given the current regime $r _ { d }$ at time d. The matrix is computed off-line by a counting process over historical data.

The prediction is based on two distinct operations:

(1) a correction (recursive Bayesian update) of the posterior probabilities for the regimes based on the value of the normalized price (if available, or of its estimate) obtained from the <sup>fi</sup>rst measurement until the previous time, d 1. We use $\overrightarrow { P } ( r _ { d - 1 } |$ $\{ \widetilde { n p } _ { 1 } , \cdots , \widetilde { n p } _ { d - 1 } \} )$ , to indicate a vector of the posterior probabil ities of all the regimes at time $d - 1 .$

(2) a prediction of regime posterior probabilities for the current time, d. The prediction of the posterior distribution of regimes n time units into the future, $\overrightarrow { P } ( r _ { d + n } | \{ \widetilde { n p } _ { 1 } , \cdots , \widetilde { n p } _ { d - 1 } \} )$ , is done by multiplying the prediction matrix n times, as follows:

![](/api/attachments/9D56NCBG/fulltext/images/347ce8fddbc0e64c1fc6116fbdfff0ad98f60bd453cbe7b1b29bc7899a8617bf.jpg)  
Fig. 6. Minimum, maximum, mean, mid-range, and smoothed mid-range daily normalized prices of computers sold, as reported during the game every day for the medium market segment in the 3721@tac3, one of the <sup>fi</sup>nal games. The mean price is computed after the game using the game data, which include complete information on all the transactions

$$
\begin{array}{l} \overrightarrow {P} (r _ {d + n} | \{\widetilde {\mathrm{np}} _ {1}, \dots , \widetilde {\mathrm{np}} _ {d - 1} \}) \\ = \sum_ {r _ {d + n}} \dots \sum_ {r d - 1} \left\{\overrightarrow {P} (r _ {d - 1} | \widetilde {\mathrm{np}} _ {1}, \dots , \widetilde {\mathrm{np}} _ {d - 1}). \prod_ {j = 0} ^ {n} T _ {1} ^ {h + 1} (r _ {d + j} | r _ {d + j - 1}) \right\} \end{array}
$$

where

9

$$
\mathbf {T} _ {1} ^ {\mathbf {h} + 1} (r _ {d} | r _ {d - 1}) = \prod_ {n = 0} ^ {h} \mathbf {T} _ {1} (r _ {d} | r _ {d - 1})\tag{10}
$$

## 4.3.2. Exponential smoother prediction

As an alternative to the Markov prediction process, we describe a method for regime predictions based on exponentially smoothed price predictions. We assume that price observations are only available for the past, up to the previous period d−1. We <sup>fi</sup>rst calculate the price trend, $t r _ { d - 1 }$ using a Brown linear exponential smoother [3]:

$$
t r _ {d - 1} = \frac {\alpha}{1 - \alpha} \cdot (\widetilde {\mathrm{np}} _ {d - 1} ^ {\prime} - \widetilde {\mathrm{np}} _ {d - 1} ^ {\prime \prime})\tag{11}
$$

where

$$
\widetilde {\mathsf {n p}} _ {d - 1} ^ {\prime} = \alpha \cdot \widetilde {n p} _ {d - 1} + (1 - \alpha) \cdot \widetilde {\mathsf {n p}} _ {d - 2} ^ {\prime}\tag{12}
$$

$$
\widetilde {\mathrm{np}} _ {d - 1} ^ {\prime \prime} = \alpha \cdot \widetilde {\mathrm{np}} _ {d - 1} ^ {\prime} + (1 - \alpha) \cdot \widetilde {\mathrm{np}} _ {d - 2} ^ {\prime \prime}\tag{13}
$$

We can then estimate normalized prices for current and future periods as

$$
\widetilde {\mathrm{np}} _ {d + n} = \widetilde {\mathrm{np}} _ {d - 1} + (1 + n) \cdot \widetilde {t r} _ {d - 1}, \forall n = 0, \dots , h\tag{14}
$$

Given the current and future price estimates, we can use Eq. (7) to predict future regimes.

## 5. A case study: TAC SCM

The Trading Agent Competition for Supply Chain Management [6] (TAC SCM) is a market simulation in which six autonomous agents compete to maximize pro<sup>fi</sup>ts in a computer-assembly scenario (see Fig. 5). An agent in TAC SCM is a software entity that represents a virtual manufacturer. Over <sup>fi</sup>fty academic or industrial research groups world wide have implemented agents for TAC SCM. During a game, agents make fully autonomous decisions without any human intervention. A game simulation takes place over 220 virtual days, each lasting <sup>fi</sup>fteen seconds of real time. Agents earn money by selling computers they assemble out of parts they purchase from suppliers. Each agent has a limited-capacity assembly facility, and must pay for warehousing its inventory. Each agent begins with an empty bank account. The agent with the highest bank balance at the end of the game wins.

An agent can produce 16 different types of computers, that are categorized into three different market segments (low, medium, and high). Demand in each market segment varies randomly during the game. Other variables, such as storage costs and interest rates vary between games.

To obtain parts, an agent must send a Request For Quotes (RFQ) to an appropriate supplier. Each RFQ speci<sup>fi</sup>es a component type, a quantity, and a due date. The next day, the agent will receive a response to each request. Suppliers respond by evaluating each RFQ to determine how many components they can deliver on the requested due date, considering the outstanding orders they have committed to. If the supplier can produce the desired quantity on time, it responds with an offer that contains the price of the components. If not, the supplier responds with two offers: (1) an earliest complete offer with a revised due date and a price. This revised due date is the <sup>fi</sup>rst day in which the supplier believes it will be able to provide the entire quantity requested; and (2) a partial offer with a revised quantity and a price with the requested due date. The agent can accept either of these alternative offers, or reject both. Suppliers may deliver late, due to uncertainty in their production capacities. Suppliers discount prices according to the ratio of supply to demand.

Every day each agent receives a set of RFQs from potential customers. Each customer RFQ speci<sup>fi</sup>es the type of computers requested, along with quantity, due date, reserve price, and penalty for late delivery. Each agent may choose to bid on some or all of the day's RFQs. Customers accept the lowest bid that is at or below the reserve price, and notify the winning agent. The agent must ship customer orders on time, or pay the penalty for each day an order is late. If a product is not shipped within <sup>fi</sup>ve days of the due date the order is canceled, the agent receives no payment, and no further penalties accrue.

![](/api/attachments/9D56NCBG/fulltext/images/238763e2449a5fd9ab5de3b7315d8c7dfcb97a53a2f3b0233b8d3f59293c82e8.jpg)  
Fig. 7. Regime probabilities over time computed online every day for the medium market segment in game 3721@tac3 (Final TAC SCM 2005).

![](/api/attachments/9D56NCBG/fulltext/images/21772c7b729596c4dd71d76ea93de2e4462b554f48c5d32da0ee1353c376d577.jpg)  
Fig. 8. Daily entropy values of the <sup>fi</sup>ve regimes for the medium market segment in game 3721@tac3. Notice how the entropy values match the regime probabilities shown in Fig. 7.

The other agents playing in the same game affect signi<sup>fi</sup>cantly the market, since they all compete for the same parts and customers. This complicates the operational and strategic decisions an agent has to make every day, which include how many parts to buy, when to get the parts delivered, how to schedule its factory production, what types of computers to build, when to sell them, and at what price.

## 5.1. Experimental setup

For our experiments, we used data from a set of 24 games (18 for training<sup>2</sup> and 6 for testing<sup>3</sup>) played during the semi-<sup>fi</sup>nals and <sup>fi</sup>nals of TAC SCM 2005. The mix of players changed from game to game, the total number of players was 12 in the semi-<sup>fi</sup>nals and 6 in the <sup>fi</sup>nals.

Since supply and demand in TAC SCM change in each of the market segments (low, medium, and high) independently of the other segments, our method is applied to each individual market segment.

Each type of computer has a nominal cost, which is the sum of the nominal cost of each of the parts needed to build it. In TAC SCM the cost of the facility is sunk, and there is no per-unit assembly cost. We normalize the prices across the different computer types in each market segment, as shown in Eq. (1).

## 5.2. Estimate of prices of previous day sales

Every day the agent receives a report which includes the minimum and maximum prices of all the computers sold the day before, but not the quantities sold. The mid-range price, np, the mean of the minimum and maximum prices, can be used to approximate the mean price. However, it does not always provide an accurate estimate of the mean price because of local <sup>fl</sup>uctuations in minimum and maximum prices. In other words, since the minimum and maximum prices could be unusual and temporary <sup>fl</sup>uctuation, they may be outliers and not within the true distribution of the prevailing prices.

An example which shows how the mid-range value differs from the mean value is in Fig. 6. The mean value is computed after the game, when the entire game data are available. We observe that the mid-range price is different from the mean price. In this example, around day 110, 120,140 and at the end, we observe a high spike in the maximum price. This was caused by an opportunistic agent who discovered a small amount of unsatis<sup>fi</sup>ed demand, but most of that day's orders were sold at a much lower price.

![](/api/attachments/9D56NCBG/fulltext/images/a0a626fdb53efbd1a164a4eb42b7fef13d8b92dd117fdddf7105cf1a88fa9e90.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/be289710c8abed6f045223cb4a78daffd1d0417f9b985b2e758b18146b8c12b8.jpg)  
Fig. 9. Game 3721@tac3 (Final TAC SCM 2005) — relationships between regimes and normalized prices in the medium market. On the left axis, we show in the top <sup>fi</sup>gure the daily factory utilization (FU) and in the bottom <sup>fi</sup>gure the available <sup>fi</sup>nished goods inventory (FG) of all the agents. In both <sup>fi</sup>gures we show the ratio of offer to demand (which ranges from 0 to 5.38), scaled to <sup>fi</sup>t between the minimum and maximum values on the left axis. On the right axis we show the normalized prices. The dominant regimes are labeled along the bottom

To reduce the impact of <sup>fl</sup>uctuations in minimum and maximum prices, we compute the smoothed mid-range price $\bar { n p } _ { d }$ on day d as the average of the smoothed minimum normalized price\~ $\widetilde { n p } _ { d } ^ { m i n }$ and the smoothed maximum normalized price $\widetilde { n p } _ { d } ^ { m a x }$ for the same day:

![](/api/attachments/9D56NCBG/fulltext/images/c5a652c1a1c1d0f357410359d6fb810a68032a6ac5147e4ea923b3b3d2de242c.jpg)  
Fig. 10. Correlation coef<sup>fi</sup>cients between regimes and quantity of <sup>fi</sup>nished goods inventory, factory utilization, the ratio of offer to demand, and normalized price (np) in the medium market segment using a training set of 18 games. All values are signi<sup>fi</sup>cant at the p=0.01 level.

![](/api/attachments/9D56NCBG/fulltext/images/da1717416f21c952ed46d9e9544308e292e2ac8cf2b57afad67deaa74807ed1d.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/13907f5efd4e0c74ff7dd227c547fc7f2f673c2fd726bd9e1995f15105352838.jpg)  
Fig. 11. Regime predictions for game 3721@tac3 starting on day 80 for 20 days into the future for the medium market segment.

$$
\widetilde {\mathrm{np}} _ {d} = \frac {\widetilde {\mathrm{np}} _ {d} ^ {m i n} + \widetilde {\mathrm{np}} _ {d} ^ {m a x}}{2}\tag{15}
$$

We smooth the minimum normalized price (and, similarly, the maximum normalized price) using a Brown linear (i.e. double) exponential smoother, shown earlier in Eq. (11), with α=0.5:

$$
\widetilde {\mathsf {n p}} _ {d} ^ {m i n} = 2 \cdot \widetilde {\mathsf {n p}} _ {d} ^ {m i n ^ {'}} - \widetilde {\mathsf {n p}} _ {d} ^ {m i n ^ {' '}}\tag{16}
$$

where

$$
\widetilde {\mathrm{np}} _ {d} ^ {m i n ^ {\prime}} = \alpha \cdot \mathrm{np} _ {d} ^ {m i n} + (1 - \alpha) \cdot \widetilde {\mathrm{np}} _ {d - 1} ^ {m i n ^ {\prime}}\tag{17}
$$

$$
\widetilde {\mathrm{np}} _ {d} ^ {m i n ^ {' '}} = \alpha \cdot \widetilde {\mathrm{np}} _ {d} ^ {m i n ^ {'}} + (1 - \alpha) \cdot \widetilde {\mathrm{np}} _ {d - 1} ^ {m i n ^ {' '}}\tag{18}
$$

This results in a better approximation of the mean price than smoothing only the mid-range price from the previous day, as shown in the example in Fig. 6.

## 5.3. Online identification of dominant regime

During the game, the agent estimates on day d the current regime by calculating the smoothed mid-range normalized price $\overline { { n p } } _ { d }$ <sub>1</sub> for the previous day (recall that the agent every day receives the price ranges for the previous day) and by selecting the regime which has the\~ highest probability, i.e. argmax $\mathsf { \widetilde { \Lambda } } _ { 1 \leq k \leq M } \overrightarrow { P } \left( R _ { k } | \widetilde { n p } _ { d - 1 } \right)$

![](/api/attachments/9D56NCBG/fulltext/images/c8f61db7adcf465611c60087a0b845af2276d25e956f65dfa27e9f45e67f158e.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/34984124889802b1aab391dfe5829c18d399393a41690ee30f15a357c5343d9b.jpg)  
Fig. 12. Regime predictions for game 3721@tac3 starting on day 110 for 30 days into the future for the medium market segment.

![](/api/attachments/9D56NCBG/fulltext/images/4ab758095ffb075de9afa2b73aae3476229d2855b115bf33e8329d47c5159aa3.jpg)

![](/api/attachments/9D56NCBG/fulltext/images/a1caab591a638bbe10379a814b711156609b18319bbb8a45d13123f0361375b1.jpg)  
Fig. 13. Success rate of correct regime shift prediction. The left <sup>fi</sup>gure is generated using a GMM with 16 components and the right <sup>fi</sup>gure with 25 components. The predictions are tested across the low, medium, and high priced computer market.

Fig. 7 shows the relative probabilities of each regime over the course of a game. The graph shows that different regimes are dominant at different points in the game, and that there are brief intervals during which two regimes are almost equally likely.

A measure of the con<sup>fi</sup>dence in the regime identi<sup>fi</sup>cation is the entropy of the set S of the probabilities of the regimes obtained from\~ the daily price reports $\widetilde { n p } _ { d } ,$ where

$$
S = \left\{P \left(R _ {1} \mid \widetilde {\mathrm{np}} _ {d}\right), \dots , P \left(R _ {M} \mid \widetilde {\mathrm{np}} _ {d}\right) \right\}\tag{19}
$$

and

$$
\operatorname{Entropy} (S) \equiv \sum_ {k = 1} ^ {M} - P \left(R _ {k} \mid \widetilde {\mathrm{np}} _ {d}\right) \log_ {2} P \left(R _ {k} \mid \widetilde {\mathrm{np}} _ {d}\right)\tag{20}
$$

An entropy value close to zero corresponds to a high con<sup>fi</sup>dence in the current regime and an entropy value close to its maximum, i.e. for M regimes $\mathsf { l o g } _ { 2 } M ,$ , indicates that the current market situation is a mixture of M almost equally likely regimes. An example for the medium market segment in game 3721@tac3 is shown in Fig. 8. Since the market is usually dominated by two regimes, i.e. scarcity and balanced, an alternative measure is the ratio of the highest regime probability to the second highest regime probability. More details on this measure can be found in [18].

## 5.4. Relationship between regimes and market variables

For our experiments we selected the number of regimes after examining the data and looking at economic analyses of market situations. The regimes we chose are: EO (or $R _ { 1 } )$ which represents extreme oversupply, O (or $R _ { 2 } )$ oversupply, B (or $R _ { 3 } )$ balanced, S (or $R _ { 4 } )$ scarcity, and ES (or $R _ { 5 } )$ extreme scarcity.

Fig. 9 (top) shows the factory utilization (FU) in percent, the ratio of offer to demand, which represents the proportion of the market demand that is satis<sup>fi</sup>ed, and the normalized price over time. In the bottom <sup>fi</sup>gure we display the quantity of the unsold <sup>fi</sup>nished goods inventory (FG) instead of factory utilization.<sup>4</sup>

The <sup>fi</sup>gure shows that when the offer to demand ratio is high (i.e. oversupply) prices are low and vice versa. We can observe that the ratio of offer to demand changes signi<sup>fi</sup>cantly during the game. For instance, on day 111 the ratio of offer to demand is 1.95 and prices are high. On day 208 the ratio of offer to demand is much higher, 5.38, and prices are lower. We can also observe that prices tend to lag changes in ratio of offer to demand. These factors clearly correlate with market regimes, but they are not directly visible to the agent during the game.

An advantage of using 5 regimes instead of 3 is that we gain two degrees of freedom, which improves our ability to isolate outliers in the market. For example, regime EO (extreme oversupply) is different from regime O (oversupply) since it presents a potential price war situation. Another difference between regime EO and regime O is that regime EO is universally unpro<sup>fi</sup>table and that regime O is marginally pro<sup>fi</sup>table for at least some agents. Regimes B and S are universally pro<sup>fi</sup>table and in regime ES some agents have left the market. The major difference between the scarcity regime, S, and the extreme scarcity regime, ES, is that in regime S the factory runs at full capacity, because of excess demand, while in regime ES there is a scarcity of parts, so production capacity is underutilized.

We expect the regimes to qualitatively represent the status of important hidden market factors. A correlation analysis of market parameters of the training set is shown in Fig. 10. The p-values for the correlation analysis are all less than 0.01. Regime EO (extreme oversupply) correlates positively with quantity of <sup>fi</sup>nished goods inventory, negatively with percent of factory utilization, positively with the ratio of offer to demand, and negatively with normalized price. On the other hand, in regime ES (extreme scarcity) we observe a negative correlation with the amount of unsold <sup>fi</sup>nished goods inventory, with the percent of factory utilization, and the ratio of offer to demand, and positively with normalized price.

## 6. Performance of regime predictions in TAC SCM

Our method is useful to the extent that it characterizes and predicts real qualities of the market. There are many hidden variables in a competitive market, such as the inventory positions and procurement arrangements of the competitors. Our method uses observable historical and current data to guide tactical and strategic decision processes. In this section we evaluate the practical value of regime prediction.

## 6.1. Prediction of regime transitions

We set the prior regime probability for the <sup>fi</sup>rst day to 100% extreme scarcity, since all the agents start out with zero inventory on the <sup>fi</sup>rst day. Examples of regime predictions for game 3721@tac3 for the medium market segment are shown in Figs. 11 and 12. The <sup>fi</sup>gures show the real regimes computed after the game using the game data and the predictions made by our method during the game. As it can be seen in the <sup>fi</sup>gures, the match between predictions and real data is very good.

Table 1  
Average number of regime changes and standard deviation for the testing set.

<table><tr><td rowspan="2"></td><td rowspan="2"># Gaussians</td><td>Low market</td><td>Medium market</td><td>High market</td></tr><tr><td>Avg/stdev</td><td>Avg/stdev</td><td>Avg/stdev</td></tr><tr><td># Regime changes</td><td>16</td><td>11.20/3.16</td><td>14.3/3.47</td><td>13.4/3.58</td></tr><tr><td># Regime changes</td><td>25</td><td>11.25/3.56</td><td>13.5/5.2</td><td>12.75/3.44</td></tr></table>

Fig. 11 shows a predicted change from an oversupply situation to a balanced situation. This means that the agent should sell less today and build up more inventory for the future. On the other hand in Fig. 12 we see a predicted change from scarcity to a balanced situation. In this case the agent should sell more aggressively the current day, since prices will be decreasing in the future.

We measure the accuracy of regime prediction using a count of how many times the regime predicted is the correct one. As ground truth we measure regime switches and their time off-line using the entire data set from the game. Starting with day 1 until day 199, we forecast every day the regimes for the next 20 days and we forecast when a regime transition would occur. The reason for limiting the prediction to 20 days is that every 20 days the agent receives a report which includes the mean price of each of the computer types sold since the last market report, and so it can correct, if needed, its current regime identi<sup>fi</sup>cation. Experimental results for a GMM with 16 and 25 components are shown in Fig. 13.

Table 1 reports the average number of regime changes and standard deviation for each market segment of the testing set. We see that the method produces robust results with respect to the number of Gaussians in the GMM.

## 6.2. Prediction of regime distribution

The above results are based on discrete regimes, i.e. using only the dominant regime of each predicted day to the actual regime of that day. A measure which can be used to determine the closeness of all individual predicted regime probabilities to the actual ones is called the Kullback-Leibler (KL) divergence [23,22]. This is a quantity which measures the difference between two probability distributions in bits, meaning that the smaller the measure the closer the predictions are to optimal. We can calculate the Kullback-Leibler divergence, $K L ( P ( R ) ^ { p r e d } | | P ( R ) ^ { a c t u a l } )$ as:

$$
K L \left(P (R) ^ {p r e d} \Vdash P (R) ^ {a c t u a l}\right) = \sum_ {r \in \mathcal {R}} P (R) ^ {p r e d} \log \left(\frac {P (R) ^ {p r e d}}{P (R) ^ {a c t u a l}}\right)\tag{21}
$$

The KL difference can be interpreted in terms of how much additional data are needed to achieve optimal prediction performance. The precision of this data is given by the number of bits in the KL-divergence measure. For example a 1 bit difference would require an additional binary piece of information [32], like: “Were yesterday's bids all satis<sup>fi</sup>ed?” If the difference between the two distributions is 0 than the predictions are optimal in sense that all the probabilistic information about pricing behavior is accurate (e.g. the predicted and actual distributions match).

![](/api/attachments/9D56NCBG/fulltext/images/d7e42a2f2148a2ecdc2ce531d14fda11bdde6faf6361d1eeae646306834a2541.jpg)

In Fig. 14 we show prediction results in terms of KL-divergence for a GMM with 16 components (left) and for a GMM with 25 components (right). Our predictions differ between 0.3 bits and 1 bits of information, as opposed to the Exponential Smoother predictions which vary between 0.3 and 3.5 bits for a GMM with 16 components and between 0.2 and 6.5 (not shown to maintain the same scale for the KL-divergence with the right <sup>fi</sup>gure) bits for a GMM with 25 components. The 20 days predictions of the exponential smoother are approximately 5.6 and 45 times worse than the Markov predictions. It is typically acceptable to have a KL-divergence less than or close to one. There will not be signi<sup>fi</sup>cant gains by obtaining more information in the estimation procedure.

We observe that the GMM with 25 components <sup>fi</sup>ts the actual regime probabilities better for the <sup>fi</sup>rst three days (tactical decision making) and the GMM with 16 components <sup>fi</sup>ts the actual regime probabilities better in the long term (strategic decision making). The best estimate for the current day is given by the exponential smoother and as a result should be used as an input to generate sales offer prices for the current day.

The KL-divergence tells us that the predicted regime distribution in the long term is closer to the real distribution with a GMM with 16 components than the one with 25 components. On the other hand we observe in Fig. 13 the opposite is true. Here actually the GMM with 25 components has a higher regime change prediction accuracy. The regime change success rate is based on discrete regime identi<sup>fi</sup>cation, but the KL-divergence measures the closeness of the whole distribution. A close match of the whole distribution is important for automated applications, e.g. dynamic pricing algorithms, that utilize the continuous distribution. A human decision maker, on the other side, might get insights from prediction of discrete future regimes, since they could translate directly into some actions on the procurement or sales side.

## 6.3. Prediction error

We also measured the prediction error for the price distributions generated by our model. Because the mixture of Gaussians can only approximate the true price distributions, we measured the difference between the observed price frequencies and predictions using a

![](/api/attachments/9D56NCBG/fulltext/images/f9a918a837d7b39a96ccc1e553977c16e9843d2eee74c125066ca39c797bcb99.jpg)  
Fig. 14. Normalized KL-divergence between the Markov predicted regime distribution and the actual distribution (circle), and the double exponentially smoothed predicted distribution and the actual distribution (diamond) over the planning horizon. KL-divergences are computed using 5 regimes for the medium market segment over the testing set. The left figure is generated using a GMM with 16 components and the right figure a GMM with 25 components

Monte Carlo method. Price frequencies were computed for 64 bins from game data to form an empirical histogram. Simulated price data were sampled from the mixture model and binned as per real data. Prediction error was de<sup>fi</sup>ned as the 1-norm (sum of absolute differences) distance between simulated and measured histograms, averaged across 1000 simulated data samples. In Fig. 15 we present the algorithm used to analyze price predictions when sampling from the learned GMM. Table 2 displays the results for the <sup>fi</sup>tted GMMs.

The results show that the total error introduced by the mixture model approximation varied between 5% and 8%, with more components resulting in slightly lower errors.

## 7. Conclusions and future work

We have presented an approach for identifying and predicting market conditions in markets for durable goods that are constrained by capacity and materials availability, and characterized by limited visibility of signi<sup>fi</sup>cant factors. We have demonstrated the effectiveness of our approach using games played in the semi-<sup>fi</sup>nals and <sup>fi</sup>nals from TAC SCM 2005. An advantage of our proposed method is that it works in any market for durable goods, since the computational process is completely data driven and no classi<sup>fi</sup>cation of the market structure (for instance, monopoly vs competitive) is needed. The historical data needed to train the model are typically kept by companies as part of their business data. Many places, such as Amazon.com or eBay.com, are willing to make data on past sales available for study.

## 7.1. Contributions

Our approach recognizes that different market situations have qualitative differences that can be used to guide the strategic and tactical behavior of an agent. Unlike regression-based methods that try to predict prices directly from demand and other observable factors, our approach recognizes that prices are also in<sup>fl</sup>uenced by non-observable factors, such as the inventory positions of the competitors.

Our approach learns the dynamics and durations of price regimes, and when to expect a shift in the dominant regime. This is important information that is dif<sup>fi</sup>cult to represent with regression-based methods. For example, regression in an expanding market (where prices increase) will extrapolate increasing prices using the slope of recent price data. On the other hand, the regime approach can learn that expansion (or scarcity) regimes are typically limited in duration and predictably followed by other regimes. When prices are increasing, it is important to know if prices will fall by the end of the planning horizon, which can be invaluable information for a decision maker.

Our method enables an agent to anticipate and prepare for regime changes, for example by building up inventory in anticipation of better prices in the future or by aggressive selling in anticipation of an upcoming oversupply situation.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 Inputs:
2 $pnp_{avg}$: original normalized price density
3 numBins: number of histogram bins
4 numNP: number of np in the training set
5 GMM: learned Gaussian Mixture Model
6 maxIter: number of iterations
7 Output:
8 PredErr: the overall mean prediction error
9 Process:
10 for j = 1 until maxIter
11 $pnp_{samp} = Monte\_Carlo\_Sampling(GMM, numNP)$
12 Error(j) = $\frac{|pnp_{avg}-pnp_{samp}|}{numBins}$
13 end
14 meanErr = Error
15 PredErr = numBins · Σ meanErr
16 return PredErr
</div>

Fig. 15. Prediction error algorithm

Table 2  
Overall prediction error for a 16 and a 25 GMM in the three market segments

<table><tr><td></td><td># Gaussians</td><td>Low market</td><td>Medium market</td><td>High market</td></tr><tr><td>% Prediction error</td><td>16</td><td>6.69</td><td>6.89</td><td>8.99</td></tr><tr><td>% Prediction error</td><td>25</td><td>5.75</td><td>5.48</td><td>5.95</td></tr></table>

Results were obtained after averaging over 1000 iterations.

## 7.2. Future directions

Our approach represents the uncertainty in price prediction by maintaining a price distribution, which allows an agent to avoid overcommitting to risky decisions. We intend to apply our method in other domains where predicting price distributions appears fruitful, such as Amazon.com, eBay.com, and <sup>fi</sup>nancial applications like stock tracking and forecasting.

We have implemented the regime identi<sup>fi</sup>cation and prediction method in a TAC SCM agent and begun to integrate it into the overall decision making process of the agent. We are currently using regime predictions to generate price trend forecasts, in order to support strategic decision making in the sales component of our agent. We have begun design of an algorithm that will use regime predictions for tactical decision making as well. Ultimately, we plan to combine probability information supplied by the regime model with information about possible consequences of actions to optimize decision making. In particular, we plan to use the full regime-based predicted price density to optimize tactical sales pricing by maximizing expected utility [38].

In addition, we plan to apply reinforcement learning [34] to map economic regimes to internal operational regimes and operational regimes to actions, such as procurement and production scheduling. We envision an approach that treats an operational regime as a set of rules and parameters that are speci<sup>fi</sup>c to a current or forecast regime, and that uses them to guide agent decision processes. For example, short-term procurement tends to be relatively expensive, but might be justi<sup>fi</sup>ed when a scarcity situation is anticipated in the near future.

## Appendix A. Summary of notation

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td>np</td><td>Normalized price</td></tr><tr><td> $\overline{np}$ </td><td>Mid-range normalized price</td></tr><tr><td> $np$ </td><td>Smoothed mid-range normalized price</td></tr><tr><td> $np^{min}$ </td><td>Smoothed minimum normalized price</td></tr><tr><td> $np^{max}$ </td><td>Smoothed maximum normalized price</td></tr><tr><td> $\alpha$ </td><td>Smoothing coefficient</td></tr><tr><td>p(np)</td><td>Density of normalized price</td></tr><tr><td>GMM</td><td>Gaussian mixture model</td></tr><tr><td>N</td><td>Number of Gaussians in the GMM</td></tr><tr><td>p(np| $\zeta_i$ )</td><td>Density of the normalized price, np, given i-th Gaussian of the GMM</td></tr><tr><td> $\mu_i$ </td><td>Mean of i-th Gaussian of the GMM</td></tr><tr><td> $\sigma_i$ </td><td>Standard deviation of i-th Gaussian of the GMM</td></tr><tr><td>P( $\zeta_i$ )</td><td>Prior probability of i-th Gaussian of the GMM</td></tr><tr><td>P( $\zeta_i$ np)</td><td>Posterior probability of the i-th Gaussian of the GMM given a normalized price np</td></tr><tr><td> $\overrightarrow{\eta}$  (np)</td><td>N-dimensional vector of posterior probabilities, P( $\zeta_i$ np), of the GMM components</td></tr><tr><td>M</td><td>Number of regimes</td></tr><tr><td>Rk</td><td>k-th regime, k=1, $\cdots$ , M</td></tr><tr><td>P( $\zeta$ lr)</td><td>Conditional probability matrix (N rows and M columns) resulting from k-means clustering</td></tr><tr><td>p(np|Rk)</td><td>Density of the normalized price np given a regime Rk</td></tr><tr><td>P(Rk|np)</td><td>Probability of regime Rk given a normalized price np</td></tr><tr><td>d</td><td>Current time</td></tr><tr><td>T( $r_{d+1}$ r_d)</td><td>Markov transition matrix</td></tr></table>

## References

[1] M. Benisch, A. Greenwald, I. Grypari, R. Lederman, V. Naroditskiy, M. Tschantz, Botticelli: a supply chain management agent designed to optimize under uncertainty, ACM Transactions on Computer Logic 4 (3) (2004) 29–37.

[2] P. Berry, K. Conley, M. Gervasio, B. Peintner, T. Uribe, N. Yorke-Smith, Deploying a personalized time management agent, Proc. of the Fifth Int'l Conf. on Autonomous Agents and Multi-Agent Systems, Hakodate, Japan, 2006.

[3] R.G. Brown, R.F. Meyer, D.A. D'Esopo, The fundamental theorem of exponential smoothing, Operations Research 9 (5) (1961) 673–687.

[4] J. Collins, C. Bilot, M. Gini, B. Mobasher, Decision processes in agent-based automated contracting, IEEE Internet Computing 5 (2) (2001) 61–72.

[5] J. Collins, W. Ketter, M. Gini, A multi-agent negotiation testbed for contracting tasks with temporal and precedence constraints, International Journal of Electronic Commerce 7 (1) (2002) 35–57.

[6] J. Collins, R. Arunachalam, N. Sadeh, J. Ericsson, N. Finne, S. Janson, The supply chain management game for the 2005 Trading Agent Competition, Tech. Rep. CMU-ISRI-04-139, Carnegie Mellon University, Pittsburgh, PA, 2004, December.

[7] CombineNet, Sourcing solutions http://www.combinenet.com/sourcing\_solutions/ (2006).

[8] A. Cox, Understanding buyer and supplier power: a framework for procurement and supply competence, Journal of Supply Chain Management 37 (2) (2001) 8–15.

[9] A.P. Dempster, N.M. Laird, D.B. Rubin, Maximum likelihood from incomplete data via the EM algorithm. Journal of the Royal Statistical Society. Series B 39 (1) (1977) 1–38.

[10] E.F. Fama, Ef<sup>fi</sup>cient capital markets: a review of theory and empirical work, Journal of Finance 25 (2) (1970) 383–417.

[11] R. Ghani, Price prediction and insurance for online auctions, Int'l Conf. on Knowledge Discovery in Data Mining, Chicago, Illinois, 2005.

[12] A. Ghose, M.D. Smith, R. Telang, Internet exchanges for used books: an empirical analysis of product cannibalization and welfare impact, Information Systems Research 17 (1) (2006) 3–19.

[13] M. He, A. Rogers, E. David, N.R. Jennings, Designing and evaluating an adaptive trading agent for supply chain management applications, IJCAI 2005 Workshop on Trading Agent Design and Analysis, Edinburgh, Scotland, 2005.

[14] T. Humphrey, Marshallian cross diagrams and their uses before Alfred Marshall: the origins of supply and demand geometry, Economic Review (1992) 3–23.

[15] I2, Next-generation planning, http://i2.com/solution\_library/ng\_planning.cfm (2006).

[16] M. Kearns, L. Ortiz, The Penn-Lehman automated trading project, IEEE Intelligent Systems (2003) 22–31.

[17] J.O. Kephart, J.E. Hanson, A.R. Greenwald, Dynamic pricing by software agents, Computer Networks 32 (6) (2000) 731–752.

[18] W. Ketter, Identi<sup>fi</sup>cation and prediction of economic regimes to guide decision making in multi-agent marketplaces, Ph.D. thesis, University of Minnesota, Twin-Cities, USA (January 2007).

[19] W. Ketter, E. Kryzhnyaya, S. Damer, C. McMillen, A. Agovic, J. Collins, M. Gini, MinneTAC sales strategies for supply chain TAC, Int'l Conf. on Autonomous Agents and Multi-Agent Systems New York 2004

[20] C. Kiekintveld, M.P. Wellman, S. Singh, J. Estelle, Y. Vorobeychik, V. Soni, M. Rudary, Distributed feedback control for decision making on supply chains, Int'l Conf. on Automated Planning and Scheduling, Whistler, BC, Canada, 2004.

[21] C. Kiekintveld, Y. Vorobeychik, M.P. Wellman, An analysis of the 2004 supply chain management trading agent competition, IJCAI 2005 Workshop on Trading Agent Design and Analysis, Edinburgh, Scotland, 2005.

[22] S. Kullback, Information Theory and Statistics, Dover Publications, New York, 1959.

[23] S. Kullback, R.A. Leibler, On information and suf<sup>fi</sup>ciency, Annals of Mathematical Statistics 22 (1951) 79–86.

[24] R. Lawrence, A machine learning approach to optimal bid pricing, 8th INFORMS Computing Society Conf. on Optimization and Computation in the Network Era, Arizona, 2003.

[25] B. Mark, R.C. Perrault, Calo: cognitive assistant that learns and organizes, 2006 http://www.ai.sri.com/project/CALO.

[26] C. Massey, G. Wu, Detecting regime shifts: the causes of under- and overestimation, Management Science 51 (6) (2005) 932–947.

[27] A. Ng, S. Russell, Algorithms for inverse reinforcement learning, Proc. of the 17th Int'l Conf. on Machine Learning, Palo Alto, 2000.

[28] D.R. Osborn, M. Sensier, The prediction of business cycle phases: <sup>fi</sup>nancial variables and international linkages, National Institute Economic Review 182 (1) (2002) 96–105.

[29] D. Pardoe, P. Stone, Bidding for customer orders in TAC SCM: a learning approach, Workshop on Trading Agent Design and Analysis at AAMAS, New York, 2004.

[30] K. Pauwels, D. Hanssens, Windows of change in mature markets, European Marketing Academy Conf., Braga, Portugal, 2002.

[31] T. Sandholm, Expressive commerce and its application to sourcing: how we conducted \$35 billion of generalized combinatorial auctions, AI Magazine 28 (3) (2007) 45–58.

[32] C. E. Shannon, A mathematical theory of communication, Bell System Technical Journal 27 (3) (1948) 379–423 and 623–656.

[33] E. Sodomka, J. Collins, M. Gini, Ef<sup>fi</sup>cient statistical methods for evaluating trading agent performance, Proc. of the Twenty-Second National Conference on Arti<sup>fi</sup>cial Intelligence, 2007.

[34] R.S. Sutton, A.G. Barto, Reinforcement Learning — an Introduction, The MIT Press, Cambridge, 1998.

[35] D. Titterington, A. Smith, U. Makov, Statistical Analysis of Finite Mixture Distributions, Wiley, New York, 1985.

[36] E. van Heck, P. Vervest, Smart business networks: how the network wins, Communications of the ACM 50 (6) (2007) 28–37.

[37] P. Vervest, E. van Heck, K. Preiss, L.F. Pau, Smart Business Networks, Springer Verlag, Berlin, 2005.

[38] J. von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, 2nd edition Princeton University Press, Princeton, N.J., 1947

[39] M.P. Wellman, D.M. Reeves, K.M. Lochner, Y. Vorobeychik, Price prediction in a trading agent competition, Journal of Arti<sup>fi</sup>cial Intelligence Research 21 (2004) 19–36.

[40] D. Zhang, K. Zhao, C.M. Liang, G.B. Huq, T.H. Huang, Strategic trading agents via market modeling, SIGecom Exchanges 4 (3) (2004) 46–55.

![](/api/attachments/9D56NCBG/fulltext/images/a26b7f8ee6038e69751ed04503f7a2a8500e0ad55df0ee15d6f6c9757f5ae02a.jpg)

Wolfgang Ketter is Assistant Professor at the Department of Decision and Information Sciences at the Rotterdam School of Management of the Erasmus University. He received his Ph.D. in Computer Science from the University of Minnesota in 2007. He founded and runs the Learning Agents Research Group at Erasmus (LARGE). The primary objective of LARGE is to research, develop, and apply autonomous and mixed-initiative intelligent agent systems to support human decision making in the area of business networks, electronic markets, and supplychain management. His research has been published in various information systems, and computer science journals such as Decision Support Systems, Electronic Commerce Research and Applications, and International Journal of Electronic Commerce.

He serves on the editorial board of Electronic Commerce Research and Applications.

![](/api/attachments/9D56NCBG/fulltext/images/fd54543e9bdb25d78482f343bc385e3369917c4c583c985304cdd759edef32a6.jpg)

John Collins spent 30 years in industry doing research and product development before returning to the University of Minnesota, where he completed his Ph.D. in 2002. He is currently Director of Graduate Studies for the professional Masters program in Software Engineering at Minnesota. He teaches in the areas of software engineering and arti<sup>fi</sup>cial intelligence. His research focuses on economic decision processes in autonomous software agents.

![](/api/attachments/9D56NCBG/fulltext/images/92ea7334907396c9bdef490e160c1e4c24968aefb1e601d3ee32640289f24e1b.jpg)

Maria Gini is a Professor at the Department of Computer Science and Engineering of the University of Minnesota. Her work has included coordinated behaviors among robots and in multi-agent systems, learning of opponent behaviors, and autonomous economic agents. She has coauthored over 200 technical papers. She is currently the chair of ACM Special Interest Group on Arti<sup>fi</sup>cial Intelligence (SIGART), and a member of the board of the International Foundation of Autonomous Agents and Multi-Agent Systems. She is on the editorial board of numerous journals, including the Journal of Autonomous Agents & Multi-Agent Systems, Electronic Commerce Research and Applications. Web Intelligence and Agent Systems, Autonomous Robots, and Integrated

Computer-Aided Engineering. She is a Fellow of the Association for the Advancement of Arti<sup>fi</sup>cial Intelligence.

![](/api/attachments/9D56NCBG/fulltext/images/6c8ebe60b195993b5f344bfa910ced7189d8afdafa6e22a44afc2b7b1091e132.jpg)

Alok Gupta holds Curtis L. Carlson school-wide chair in Information Management at the Carlson School of Management, University of Minnesota. His research has been published in various information systems, economics, and computer science journals such as Management Science, ISR, MIS quarterly, CACM, JMIS, Journal of Economic Dynamics and Control, Computational Economics and Decision Support Systems. He was awarded a prestigious NSF CAREER Award for his research on dynamic pricing mechanisms on the internet. He serves on the editorial boards of Management Science, ISR, JMIS, DSS and Brazilian Electronic Journal of Economics.

![](/api/attachments/9D56NCBG/fulltext/images/699ae56d201e71daf830656c4333c138e25ff2200c1f383860af462a51a1fd5d.jpg)

Paul R. Schrater received the Ph.D. degree in Neuroscience from the University of Pennsylvania in 1999, Currently he is Assistant Professor of Psychology and Computer Science & Eng. at the University of Minnesota and head of the Computational Perception and Action Laboratory. His research interests involve probabilistic models of perception, control and learning in man and machine, He has published over 50 journal and conference papers in the above areas (twenty refereed journal papers). He has received grants from NIH, NSF, and ONR.
