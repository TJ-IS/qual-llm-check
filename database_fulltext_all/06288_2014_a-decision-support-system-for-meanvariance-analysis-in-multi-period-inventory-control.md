---
otero_id: 6288
otero_key: "DEK3ZWWA"
title: "A decision support system for mean–variance analysis in multi-period inventory control"
authors: "Preetam Basu; Suresh K. Nair"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.09.012"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for mean–variance analysis in multi-period inventory control

Preetam Basu <sup>a,</sup>⁎, Suresh K. Nair <sup>b,1</sup>

<sup>a</sup> Operations Management Group, Indian Institute of Management Calcutta, Diamond Harbor Road, Kolkata 700104, India

<sup>b</sup> Operations and Information Management, School of Business, University of Connecticut, Storrs, CT 06269, USA

## a r t i c l e i n f o

Article history: Received 5 April 2013 Received in revised form 15 September 2013 Accepted 18 September 2013 Available online 27 September 2013

Keywords: Stochastic dynamic programming Risk-reward heuristic Mean–variance analysis Ef<sup>fi</sup>cient frontier analysis Inventory management

## a b s t r a c t

Traditionally inventory management models have focused on risk-neutral decision making with the objective of maximizing the expected rewards or minimizing costs over a speci<sup>fi</sup>ed time horizon. However, for items marked by high demand volatility such as fashion goods and technology products, this objective needs to be balanced against the risk associated with the decision. Depending on how the product performs vis-à-vis the seller's original forecast, the seller could end up with losses due to either short or surplus supply. Unfortunately, traditional models do not address this issue. Stochastic dynamic programming models have been extensively used for sequential decision making in the context of multi-period inventory management, but in the traditional way where one either minimizes costs or maximizes pro<sup>fi</sup>ts. Risk is implicitly considered by accounting for stockout costs. Considering risk and reward simultaneously and explicitly in a stochastic dynamic setting is a cumbersome task and often dif<sup>fi</sup>cult to implement for practical purposes, since dynamic programming is designed to optimize on one variable, not two. In this paper we develop an algorithm, Variance-Retentive Stochastic Dynamic Programming that tracks variance as well as expected reward in a stochastic dynamic programming model for inventory control. We use the mean–variance solutions in a heuristic, RiskTrackr, to construct ef<sup>fi</sup>cient frontiers which could be an ideal decision support tool for risk-reward analysis.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Inventory control plays a critical role in day-to-day business operations and is often a crucial differentiator in determining the success or failure of <sup>fi</sup>rms. Traditionally inventory control models have focused on risk-neutral decision making where the usual optimization criteria have been either maximizing the sum of discounted rewards or minimizing the sum of accumulated costs over a speci<sup>fi</sup>ed time horizon. Starting from as early as the 1950's operations researchers have studied inventory control models under various economic and market conditions. Arrow et al. [5] and Dvoretzky [20] were the <sup>fi</sup>rst to analyze a single-period inventory control model under stochastic demand which became popularly known as the newsvendor model. We refer the reader to Khouja [32] for a comprehensive review of the classical newsvendor model and its many extensions. Subsequently the single period stochastic inventory model was extended to multiple periods. The well-known (s,S) policy was proposed where an order is placed to bring the inventory level to S whenever the level fell below s. Signi<sup>fi</sup>cant contributions in this line of inquiry were made by Karlin and Fabens [30], Iglehart [28], Veinott [53] and Sethi and Cheng [47]. Recent papers by Caro [14], Jain [29], Sana [42–44] and Xu [60] have advanced the extant literature in this <sup>fi</sup>eld. The focus of the majority of these models is on optimizing the average reward criteria. However, using expected total reward criteria may yield optimal policies that are unacceptable to a risk-sensitive decision maker. For products marked by high demand variability such as fashion goods or technology products, where on the one hand there are risks associated with unsold inventory and on the other potential loss of revenues due to shortages, the variability of the rewards is as important as the expected values. Implicitly considering stock-out costs as a measure of risk is not suf<sup>fi</sup>cient in these cases. Instead of identifying one policy to achieve the stated objective, managers are often interested in considering risks more explicitly and obtaining sets of policies at different levels of risk.

There has not been much research done on risk-sensitive inventory management. The limited literature in this domain mainly focuses on single-period models, namely, newsvendor and its various extensions (see reviews by Khouja [32] and Qin et al. [39]) in a single period setting. However, in many managerial scenarios, multiple periods of ordering is involved. Based on demand and available stock-on-hand, <sup>fi</sup>rms place orders over multiple periods. Even in the context of fashion supply chains, to take advantage of more accurate demand information, <sup>fi</sup>rms often split their orders into an early order and some late orders based on market indicators (Tang et al. [50]). One of the methodologies that has been extensively used in solving these multi-period inventory problems is stochastic dynamic programming. These models provide optimal sequential decisions where present ordering decisions are taken in consideration of future outcomes. At a speci<sup>fi</sup>ed point in time, which is referred to as a decision epoch, the decision maker observes the state of the system and based on that chooses the order size. This action produces an immediate reward and the system moves to a different state in the next time-period according to a probability distribution. Dynamic programming chooses actions based on reward (whether pro<sup>fi</sup>t or cost), and does not track the risk associated with the optimal decision, resulting in a point in the risk continuum that corresponds to the maximum expected reward. The contribution of this paper is in developing a novel methodology to track both mean and variance of rewards of a set of ordering policies in the stochastic dynamic programming model. We call our methodology Variance-Retentive Stochastic Dynamic Programming (Variance-Retentive SDP). We use the resulting mean–variance solutions in a simple heuristic, which we call RiskTrackr, for creating ef-<sup>fi</sup>cient risk-reward frontiers, similar to those used in portfolio analysis in <sup>fi</sup>nance literature (Voros [54]; Markowitz [35,36]; Elton et al. [22]). This is a challenging task from an implementation standpoint, since this requires carrying information on both risk and reward simultaneously for each state, in which standard dynamic programming is not designed to do. The Variance-Retentive SDP algorithm and the RiskTrackr heuristic can be used in practice as a decision support tool for mean–variance analysis in multi-period inventory management systems.

Risk-reward trade-offs are an essential component of inventory decisions. The variability of the possible outcomes often plays an important role in determining the “best” set of ordering decisions. Financial planning models often involve systematic trade-off analysis between an expected return criterion and the variability or the risk associated with the returns. Variance of the outcomes about the expected value is a widely used measure of risk in portfolio theory. Investors use variance to measure the risk of a portfolio of stocks. The basic idea is that variance is a measure of volatility and the more a stock's returns vary from the stock's average return, the more volatile is the stock. Portfolios of <sup>fi</sup>nancial instruments are chosen to minimize the variance of the returns subject to a level of expected return or vice versa to maximize expected return subject to a level of variance of the return. This paradigm was <sup>fi</sup>rst introduced by Markowitz's [35] mean–variance analysis for which contribution he was honored with the Nobel Prize in Economics. Mean–Variance analysis has become a standard tool in portfolio management (Fama [23]; Copeland and Weston [19]). In many operational decisions also managers are interested in the mean–variance trade-offs. In inventory control, especially of items marked by high demand volatility, it is extremely important to ascertain the variability associated with a set of policies rather than just the expected return. If the variance of the outcome is large, the chance of deviating from the expected return will also be high. In this paper we de<sup>fi</sup>ne risk as the volatility associated with the outcomes of each of the policies and we measure risk by the variance of the possible outcomes.

In a single period newsvendor model, it is easy to enumerate the mean and the variance of the pro<sup>fi</sup>t values for different order-sizes. In Fig. 1a we present the mean–variance solutions for a single period newsvendor model on an ef<sup>fi</sup>cient frontier. The newsvendor optimal solution is obtained by a trade-off between cost of under-stocking and overstocking and maximizes the expected reward. But the optimal solution also has very high risk, as seen by the variance of the solution in the graph. If a decision maker is not comfortable with that level of risk, he may be well served by choosing an alternate solution on the ef<sup>fi</sup>cient frontier to the left of the newsvendor optimal solution that has lower reward but comes with lower risk. However, traditional newsvendor solutions do not present the decision maker with this choice, since it presents only one “optimal” answer. Similar logic can be applied for the mean–variance solutions for multi-period inventory control models also. However, for multi-period stochastic dynamic programming formulations, enumerating the mean and variance of the pro<sup>fi</sup>t values for different order sizes becomes an impossible task as state space increases exponentially. In Fig. 1b we present the mean–variance ef<sup>fi</sup>cient frontier for a multi-period inventory model with <sup>fi</sup>ve time-periods using Monte Carlo simulation to illustrate the number of sample paths possible and the presence of an ef<sup>fi</sup>cient frontier. The model that we use for the numerical analysis later in Section 5 has ten time periods and $1 0 ^ { 5 }$ possible states, and in each state there are 16 possible actions. This problem has millions of possible policies and even higher number of sample paths. In problems of such dimension it is impossible to enumerate all the possible sample paths and policy tables. Further, dynamic programming models need to be modi<sup>fi</sup>ed completely to track both risk and reward, and this is not an obvious extension of the basic methodology of recursion. In such practical scenarios, we propose the Variance-Retentive SDP algorithm and the RiskTrackr heuristic to construct near-optimal ef<sup>fi</sup>- cient frontiers. The bold curve in Fig. 1b is the ef<sup>fi</sup>cient frontier obtained by using the RiskTrackr heuristic.

The remainder of the paper is organized as follows: Section 2 provides a literature review. Section 3 develops the analytical model. We present the Variance-Retentive SDP algorithm and the RiskTrackr heuristic for obtaining risk-reward curves in Section 4. Managerial insights are given in Section 5. Finally, we make concluding remarks in Section 6.

## 2. Literature review

Our main contribution in this paper is in the <sup>fi</sup>eld of mean–variance analysis in inventory control. Most of the research in this stream considers single-period inventory models. Lau [33] analyzes the classical newsvendor model under two different objectives namely, maximizing the decision-maker's expected utility of total pro<sup>fi</sup>t and maximizing the probability of a certain level of pro<sup>fi</sup>t. Chung [17] deduces an algorithm for determining optimal stocking policies for a risk-averse decision maker. Bouakiz and Sobel [12] adopt the utility function approach to characterize the risk attitude in the inventory replenishment strategy. Eeckhoudt et al. [21] analyze the effect of changes in prices and cost parameters on a riskaverse newsvendor. Agrawal and Seshadri [4] consider the problem of a risk-averse retailer who decides on both the order quantity and the selling price. Parlar and Weng [37] propose a methodology for maximizing the probability of exceeding the expected profit for an extended version of the newsvendor model. Tapiero [51] applies the value at risk measure to a single-period inventory control model. Choi et al. [16] carry out a mean variance analysis of the classical single period newsvendor model. Wu et al. [59] also analyze the risk-averse newsvendor model and deduce that under stock-out penalty the ordering policy for a risk-averse decision maker is similar to that of a risk-neutral newsvendor. Buzacott et al. [13] develop a model for investigating risks of commitment–option contracts with information updates. Wei and Choi [55] explore the use of a wholesale pricing and pro<sup>fi</sup>t sharing scheme for coordinating supply chains under the mean–variance framework. Some notable papers in the <sup>fi</sup>eld of risk analysis in multi-period inventory control are by Berling and Rosling [10], Ahmed et al. [1], Chen et al. [15], Zhang et al. [61]. Berling and Rosling [10] analyze the effects of <sup>fi</sup>nancial risks on (R,Q) inventory policies and derive the discount rate used in inventory control models based on systematic risks in a real options framework. Ahmed et al. [1] study coherent risk measures in inventory models and Chen et al. [15] propose a general framework for incorporating risk-aversion in a multiperiod inventory model through the application of utility function approach. They extend the traditional models to scenarios where the riskaverse decision maker can hedge the operational risk through <sup>fi</sup>nancial securities. Zhang et al. [61] study multi-period inventory control models under risk-averse constraints expressed through Value at risk and Conditional Value at Risk as risk measures. Wang and Webster [56] use loss aversion to model a risk-sensitive manager's decision-making behavior in the single-period newsvendor problem. However, none of the above papers provide methodologies to derive the entire risk continuum or the ef<sup>fi</sup>cient mean–variance frontiers. The frontiers are useful as they provide ef<sup>fi</sup>cient solutions at different levels of risk-tolerance. We contribute in this stream of literature by providing an easy-to-use methodology to construct ef<sup>fi</sup>cient mean variance frontiers.

![](/api/attachments/DEK3ZWWA/fulltext/images/c517488942151e74bdfe83dd07bca723b7ea736234f5d44c7f57741fb60a6f89.jpg)  
a) Single-period Newsvendor Model

![](/api/attachments/DEK3ZWWA/fulltext/images/63eb90f5a7db4c71675a691192d0227eddfd1dd15fad5f98f64880d2e9d9a8d5.jpg)  
b) Multi-period Inventory Control Model  
Fig. 1. Mean–variance ef<sup>fi</sup>cient frontiers.

Capturing risk and reward in a multi-period inventory control model is a challenging task. One of the most widely used methodologies to solve these multi-period inventory models is stochastic dynamic programming. There has been some limited research in the <sup>fi</sup>eld of risksensitive decision-making where mean–variance trade-offs are considered in sequential stochastic dynamic programming problems. Variance sensitive Markov Decision Processes (MDP), which constitute a special kind of sequential stochastic problems, have been studied by Howard and Matheson [27], Sobel [48,49], Baykal-Gursoy and Ross [8], and Chung [18]. The variance-penalized MDPs are formulated as mathematical programs with linear constraints and nonlinear objective function. Kawai [31] analyzes randomized policies that minimize the variance of the reward with the mean not less than a speci<sup>fi</sup>ed value in the steady state of a discrete time MDP. Wu and Lin [58] develop an MDP model with countable state space and reward set with the objective of <sup>fi</sup>nding a policy which minimizes the probability (risk) that the total discounted rewards do not exceed a speci<sup>fi</sup>ed target value. However as Filar et al. [24] point out one of the drawbacks of these formulations is that they lead to formidable mathematical dif<sup>fi</sup>culties and are dif<sup>fi</sup>cult to implement for practical purposes. We refer the reader to a survey done by White [57] for a review in risk-sensitive optimization of MDP. Recently risk-averse stochastic programming has attracted renewed attention. Notable contribution has come from Borkar and Meyn [11], Artzner et al. [6], Shapiro [45] and Ruszczynski [40]. Borkar and Meyn [11] analyze risk-sensitive optimal control for MDPs under monotone cost function. Artzner et al. [6] study coherent risk measures which are extended by Shapiro [45] to multi-stage risk-averse stochastic programming problem. Ruszczynski [40] introduces the concept of Markov risk measure and apply it to risk-averse Markov decision models. However, the methodologies presented in these papers involve complex non-linear mathematical programming that is cumbersome and dif<sup>fi</sup>cult to implement for practical purposes. Our proposed Variance-Retentive SDP algorithm and the RiskTrackr heuristic, on the other hand, are easy to use and provide a useful decision support tool.

In the Variance-Retentive SDP algorithm, as we will see in the next section, we carry information about the variance of a set of decisions in addition to expected rewards and this information about the variance is utilized in selecting the optimal policies for each state. Our RiskTrackr heuristic uses the mean–variance solutions to construct ef<sup>fi</sup>cient frontiers which can be used to ascertain risk exposure of a set of ordering policies. Once the management identi<sup>fi</sup>es the risk exposure of a set of policies they can choose their actions based on risk tolerance. Our present work contributes in the <sup>fi</sup>eld of operational risk management by providing a decision support tool for ef<sup>fi</sup>cient frontier analysis in inventory control. The literature on decision support systems (DSS) in inventory control includes work by Achabal et al. [3] who develop a DSS for a vendor managed inventory system. Ahuja and Hanna [2] emphasize the importance of DSS in business operations when quantitative inventory models such as EOQ are used. Behesti [9] presents a decision support model that seeks to improve the performance of inventory control in a supply chain network. Sana [41] develops an integrated productioninventory decision support model for a three-layer supply chain considering both perfect and imperfect quality items. Hong Zhen and Lee [26] propose a novel decision support framework which helps the buyer to make optimal procurement decision in the existence of correlated demand, yield and spot price uncertainties.

Next we present the stochastic dynamic formulation of the multiperiod inventory control model.

## 3. Stochastic dynamic programming formulation for inventory control

Stochastic dynamic programming has been extensively used in inventory control models. These models are widely applicable in a variety of business problems such as determining order-sizes in a supply chain set-up and even for managing cash balances. Here we present a simpli-<sup>fi</sup>ed version of that model for completeness, and can be skipped by readers familiar with such models.

The model is based on Puterman [38]. Each time period the manager looks at the current inventory or stock-on-hand of a single product and decides whether or not to order additional stock from a supplier. We look at a <sup>fi</sup>nite-horizon model with T time-periods. The state of the system at any time-period is given by z which denotes the stock-on-hand. We assume that demand for the product at each time-period, d, is random and independent and follows a discrete probability distribution $p ( d )$ . Backordering of unmet demand is not considered in this model. Let q be the units of stock ordered at each time-period andq^ be the maximum possible order-size. The unit selling price is given by s and the unit purchase cost of the product is u and the unit holding cost is h. The salvage value, at the boundary $( = T )$ , for unit unsold inventory is given by $\lambda . f _ { t } ^ { d } ( z )$ is the maximal net present value of being in state, z, when optimal actions are taken in each time period from period t to T. β is the discount factor that captures the time-value of future rewards. The following recursive functional equations specify the model:

$$
f _ {t} ^ {T} (z) = \underset {q} {\text { Max }} \sum_ {d} p (d) \left[ s \widetilde {d} - u q - h \widetilde {z} + \beta f _ {t + 1} ^ {T} (z - \widetilde {d} + q) \right]\tag{1}
$$

$$
\text { where } \widetilde {d} = \text { Minimum } (d, z) \text { and } \widetilde {z} = \text { Maximum } (0, z - d)
$$

The boundary condition is given by:

$$
f _ {T} ^ {T} (z) = \lambda z\tag{2}
$$

At each time period the quantity sold is equal to the minimum of demand realized and the inventory-on-hand. This is denoted by d. So the revenues earned are given by sd. The total ordering cost is given by uq.

The amount of leftover inventory in each time-period is captured by z. If the demand realized is more than the inventory-on-hand, z, then there is no left-over inventory otherwise the left-over inventory that is carried on to the next time-period is given by $z - d .$ . Hence the total holding cost at each time-period is hz. The quantity $s d - u q - h \widetilde { z }$ is the revenue minus the sum of the ordering and holding costs and is reward earned in the present time-period, t. The problem then moves to the next time period $t + 1$ . At the beginning of the next time-period, $t + 1$ the quantity ordered at t arrives and so the inventory-on-hand is given by $z - \tilde { d } + q$ . The model is then solved by backward recursion.

In a <sup>fi</sup>nite-horizon discrete-time dynamic programming problem such as the inventory control model explained above, the information about the expected reward for a set of optimal actions is carried at each state. However, the reward values will have a variance, which is completely ignored in traditional dynamic programming. When the decision maker is also interested in the risk or the variability associated with each policy, a straightforward application of dynamic programming is not suf<sup>fi</sup>cient

Next we explain the Variance-Retentive SDP algorithm and the RiskTrackr heuristic that provide an easy-to-use decision tool for mean–variance analysis in inventory management.

## 4. Variance-Retentive SDP and heuristic for risk-reward curve

In a dynamic programming formulation it is not possible to optimize based on both the average reward as well as the variance criteria in one objective function. In this paper, we develop a novel methodology, Variance-Retentive SDP, where we use backward recursion algorithm to solve the dynamic programming model and in addition to carrying information about the expected reward, we also keep track of the variance of a set of policies at each state. In Variance-Retentive SDP we use the variance information to identify order-sizes that maximize average reward but at various levels of variance. The objective function of our dynamic programming model maximizes the average reward, as is given in Eq. (1), but at each time-period we consider the order-sizes based on the reward and the variance associated with them. We use the average reward as well as the variance of the rewards in a heuristic, RiskTrackr, to obtain average reward at different levels of variance. Here we trim the possible action set at each decision-epoch by considering the ratio of average reward over variance for each of the possible order-sizes. In the process we control the variance of the order-sizes and maximize the reward at a particular level of variance or risktolerance. The RiskTrackr heuristic is explained in detail in Section $4 . 1$ We now describe the Variance-Retentive SDP algorithm.

The expected reward for any order size q, at any decision epoch t, is computed from Eq. (1) and we denote it by ${ \cal W } _ { q } ( z ) ; { \cal W } _ { q } ( z ) = \sum _ { \epsilon } p ( d )$ $\left\lceil s \widetilde { d } - u q - h \widetilde { z } + \beta f _ { t + 1 } ^ { T } \left( z - \widetilde { d } + q \right) \right\rceil$ : This is in tune with the traditional approach used in dynamic programming to calculate expected reward at any decision epoch. The novelty in Variance-Retentive SDP comes in tracking the variance about the expected reward associated with any order size q. The variance of the possible outcomes for any order size q at any state z is denoted by $\gamma _ { q } ( z )$ . This variance information for any order size q that we capture in $\gamma _ { q } ( z )$ can be used to calculate measures which in turn can be applied in conjunction with the expected reward to determine the optimal order-size at any decision epoch. In RiskTrackr we have used the ratio of average reward over the variance values to come up with a criterion to determine optimal order sizes. $\gamma _ { q } ( z )$ is computed using the following equation:

$$
\begin{array}{c} \gamma_ {q} (z) = \sum_ {d} p (d) \beta^ {2} V _ {t + 1} ^ {T} \Big [ z - \widetilde {d} + q \Big ] + \sum_ {d} p (d) \Big (\widetilde {s d} - u q - h \widetilde {z} + \beta F _ {t + 1} ^ {T} \Big [ z - \widetilde {d} + q \Big ] \Big) ^ {2} \\ - \sum_ {d} p (d) \Big (\widetilde {s d} - u q - h \widetilde {z} + \beta F _ {t + 1} ^ {T} \Big [ z - \widetilde {d} + q \Big ] \Big) \mu_ {t + 1} ^ {T} (z) \end{array}\tag{3}
$$

$$
\text { where }, \mu_ {t + 1} ^ {T} (z) = \sum_ {d} p (d) \left(s \widetilde {d} - u q - h \widetilde {z} + \beta F _ {t + 1} ^ {T} [ z - \widetilde {d} + q ]\right)
$$

The details of the derivation of $\operatorname { E q . } \left( 3 \right)$ are provided in the Appendix A. The maximal expected reward at any state, z corresponding to the optimal order size $q ^ { * }$ is captured by the functional value $f _ { t } ^ { T } ( z ) = w ^ { * } =$ $M a x w _ { q } ( z )$ : Here we use two arrays $\dot { F } _ { t } ^ { T } [ z ]$ and $V _ { t } ^ { T } [ z ]$ to capture the values of the average reward and variance at each state of the dynamic program corresponding to the optimal action $q ^ { * }$ . The value of the maximum expected reward $f _ { t } ^ { T } ( z )$ is stored in $F _ { t } ^ { T } [ z ]$ and the variance corresponding to the optimal action $q ^ { * }$ , is stored in $V _ { t } ^ { T } [ z ]$ . The basic difference between a standard backward recursion solution methodology and Variance-Retentive $\mathsf { S D P }$ is in a standard backward recursion methodology at each decision epoch all the possible order-sizes are considered and then the one that gives the maximum average reward is picked whereas in Variance-Retentive SDP we track both the expected value and the variance of the rewards and then use both these information to determine the optimal order-sizes.

$\mathbb { A } \mathrm { t } \mathrm { \Delta } t = T ,$ i.e., at the boundary, the variance at any state is zero since no actions are taken. Then at any preceding decision epoch $( t = T \mathrm { - } 1 , T \mathrm { - } 2$ $\ldots , 0 )$ the variance at any state for each of the possible actions is calculated based on Eq. (3).

Next we explain the Risktrackr heuristic in detail.

## 4.1. The RiskTrackr heuristic

In the RiskTrackr heuristic, we use the expected reward for any order size q, at any decision epoch t, denoted by $w _ { q } ( z )$ and the variance of the possible outcomes for any order size q at any state z denoted by $\gamma _ { q } ( z )$ which we track by the Variance-Retentive SDP. This variance information is then used to evaluate the optimal action $q ^ { * }$ at each decision epoch. At each decision epoch of the problem, we develop a ratio based on average reward to variance for each of the possible order sizes. We call this ratio “Incremental Variance Criteria”, IVC for short, and denote it by $K _ { q } ( z )$

$$
K _ {q} (z) = \frac {w _ {q} (z)}{\gamma_ {q} (z)}\tag{4}
$$

The IVC is similar to the Sharpe ratio (Sharpe [46]) used in investment analysis. It is a reward-to-variability ratio that measures the return (or risk premium) per unit of deviation in an investment, The IVC value is used in determining the optimal order size. We solve the model $( 1 ) - ( 2 )$ iteratively and at each iteration we sequentially increase the possible order sizes that we consider while determining the optimal order size at any decision epoch. The possible order sizes that come under consideration are determined based on their corresponding IVC values. The number of order sizes that is considered at each state, based on their IVC values, is denoted by j. The increment factor that is used to sequentially increase j is denoted by $y ( j = 1 , 1 + y , 1 + 2 y , . . . . , \hat { q } ) ; \hat { q }$ is the maximum order-size. We <sup>fi</sup>rst solve the model $( 1 ) - ( 2 )$ by backward recursion for ${ \mathrm { j } } = 1 , { \mathrm { i . e . } }$ , at each state we pick the order size that gives the highest IVC value. As we solve the model repeatedly, at each state we rank all the order sizes in a descending order based on their IVC values. Then for the kth run of the model we consider the top k order sizes in each state based on their IVC values and pick the one that corresponds to the maximum average reward. The average reward and variance for the optimal order size at any state z are stored in $F _ { t } ^ { T } ( z )$ and $V _ { t } ^ { T } ( z )$ respectively. In this process, at any state, we are ranking the order sizes in descending order based on the IVC values and then we are picking the top j order sizes. Then out of the top j order sizes, we are picking the order size that gives the maximum reward. The basic idea behind this heuristic is trimming the possible order sizes based on the IVC values and then sequentially increasing them by increasing the range of the IVC values being considered. This in turn increases the range of the variance values or the risk exposure of the model. Therefore instead of using just the expected reward to pick the optimal order size as is done in the traditional approach towards solving dynamic programming models, we also use variance information to evaluate the optimal order size at each state.

$\begin{array} { r } { \mathbb { A } \mathrm { t } \mathrm { \Delta } t = 0 , } \end{array}$ , for each of the j runs of the model, $F _ { 0 } ^ { T } ( z )$ and $V _ { 0 } ^ { T } ( z )$ give the average reward and variance for a sequence of optimal actions executed at each of the time periods, $t = 0 , 1 , . . . , T .$ We store the average reward and variance values at $t = 0 , \mathrm { i . e . } , F _ { 0 } ^ { T } ( z )$ and $V _ { 0 } ^ { T } ( z )$ for each of the j runs in E[j] and Var[j] respectively. For example, in any intermediate run of the model when $j = k ,$ we solve the model (1)–(2) by backward recursion and at each decision epoch we only consider the top k order sizes based on their IVC values. The average reward and variance values corresponding to $t = 0$ for the kth run of the model are stored in E[k] and Var[k]. We continue the above process until $j = \hat { q }$ , i.e., until all the order sizes have been considered. E[j] and Var[j] for all $j = 1 , 1 + y , 1 + 2$ $y , . . . . , \acute { c }$ are then used to construct the ef<sup>fi</sup>cient risk-reward curve. The algorithm for the RiskTrackr heuristic is given in Fig. 2.

The intuition behind the RiskTrackr heuristic is at each decision epoch when we are using the IVC values of the order sizes, we are considering order sizes that are most ef<sup>fi</sup>cient in terms of average reward over variance. Then we are picking the order-size that has the highest average reward out of the ranked order sizes. At each iteration of RiskTrackr as we increase j (or the number of order sizes being considered) we increase the range of IVC values being considered by going down in the list of IVC values ranked in descending order. As we consider more IVC values from the ranked list of IVC values we in turn increase the range of the variance values associated with the order sizes that come into consideration for picking the optimal order size. And then at a higher variance value or risk exposure the order size that has the maximum average reward is picked. So RiskTrackr systematically increases the risk-exposure by considering more order-sizes based on their average reward over variance value. The outcomes start from very low riskexposure and increase to the maximum risk-exposure. Managers, using this heuristic, can pick the policies at different levels of risk tolerance based on their risk sensitivity. As we show later our heuristic performs quite creditably in constructing near-optimal risk-reward curves. We now explain the RiskTrackr heuristic using a numerical example.

## 4.2. A numerical example

Consider a problem with T = 3 and possible order sizes $0 , 1 , \ldots , 4 .$ Let the selling price be $s = \$ 6$ and the unit cost of an item be $u = \mathbb { S } 2$ and the unit holding cost be h = \$1. Let the salvage value of unsold inventory at the end of the time-horizon be zero and the step-size in incrementing j be one $( y = 1 )$ and the discount factor $\beta = 0 . 9 8$ . Let the initial inventory on hand be 2. We start with $j = 1$ and solve the inventory control model by backward recursion using the Variance-Retentive SDP with initial inventory level at 2. Suppose in the backward recursion algorithm at the boundary, i.e., at $t = 3$ a state (2) is reached, then we set $V _ { 3 } ^ { 3 } [ 2 ] = 0$ and $F _ { 3 } ^ { 3 } [ 2 ] \overset { \cdot } { = } 0$ since the salvage value: $\lambda = 0$ Similarly, for all the terminal states $V _ { 3 } ^ { 3 } [ z ] = 0$ and $F _ { 3 } ^ { 3 } [ z ] = 0 $

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Step 1: (Initialization)
- Set $j = 1$
Step 2: (Locate points on the efficient frontier)
- Declare two arrays $F_{t}^{T}[z]$ and $V_{t}^{T}[z]$
- $V_{T}^{T}(z) = 0$ and $F_{T}^{T}[z] = f_{T}^{T}(z)$
- For each state $z$ at $t = T - 1, T - 2, ..., 1$ find the expected reward $w_{q}(z)$ and variance $\gamma_{q}(z)$ for each action $q$ using Variance-Retentive SDP
$w_{q}(z) = \sum_{d} p(d)[s\widetilde{d} - uq - h\widetilde{z} + \beta f_{t+1}^{T}(z - \widetilde{d} + q)]$ $\gamma_{q}(z)$ is computed using equation (3).
- Rank all order sizes in descending order based on their IVC value using (4)
- Pick the top $j$ order sizes
- Out of the top $j$ order sizes, pick $q^{*}$ with the maximum reward, $w^{*}$, $w^{*} = Max_{q} w_{q}(z)$;
- Set $F_{t}^{T}[z] = w^{*}, \&amp; V_{t}^{T}[z] = \gamma_{q^{*}}(z)$.
- For $t = 0,$, save the reward and variance $E[j] = F_{0}^{T}[z], Var[j] = V_{0}^{T}[z]$.
Step 3:
- $j = j + y$, If $j &lt; \hat{q}$, go to step 2.
Step 4:
- Use $E[j]$ &amp; $Var[j]$, $j = 1, 1 + y, 1 + 2y, ..., \hat{q}$, to construct the risk-reward curve
</div>

Next suppose at $t = 2 ,$ , the backward recursion algorithm reaches a state (3). Let the possible demand realizations be $0 , 1 , 2 , 3 ,$ and 4 with the corresponding probabilities as follows: $\begin{array} { r } { p ( d = 0 ) = 0 . 2 , } \end{array}$ $p ( d = 1 ) = 0 . 2 , p ( d = 2 ) = 0 . 2 5 , p ( d = 3 ) = 0 . 2$ and $p ( d = 4 ) =$ 0.15. We need to <sup>fi</sup>gure out the expected reward and variance for all the possible order sizes in state (3) at $t = 2 .$ To obtain the optimal order size we need to calculate $\gamma _ { 0 } ( 3 ) , \gamma _ { 1 } ( 3 ) , . . . , \gamma _ { 4 } ( 3 )$ and the corresponding $K _ { 0 } ( 3 ) , K _ { 1 } ( 3 ) , . . . , K _ { 4 } ( 3 )$ . For illustrative purposes we show the calculation for γ<sub>2</sub>(3) and $K _ { 2 } ( 3 )$ , the other values can be obtained using similar calculations.

$$
\begin{array}{l} \gamma_ {2} (3) = 0 + 0. 2 (- 7) ^ {2} + 0. 2 (0) ^ {2} + 0. 2 5 (7) ^ {2} + 0. 3 5 (1 4) ^ {2} - (5. 2 5) ^ {2} \\ = 6 3. 0 9 \end{array}
$$

$$
K _ {2} (3) = \frac {5 . 2 5}{6 3 . 0 9} = 0. 0 8 3
$$

Similarly, we need to <sup>fi</sup>gure out the IVC values for the other four order sizes and rank them in descending order. Here j = 1 i.e., we are only considering the order size that gives the maximum IVC value and so in this case, the optimal order size will be the one that gives the maximum IVC value. When j N 1 we will consider the top j order sizes with IVC values and then pick the one among them that leads to maximum average reward. $\mathtt { A t } t = 2$ , the other IVC values for the state (3) are as follows: $K _ { 0 } ( 3 ) = 0 . 1 4 7 , K _ { 1 } ( 3 ) = 0 . 1 1 5 , K _ { 3 } ( 3 ) = 0 . 0 5 2$ and $K _ { 4 } ( 3 ) =$ 0.02. Hence, the optimal order size is 0. Since this is the <sup>fi</sup>rst run of the model $( \mathrm { j } = 1 )$ the maximum average reward earned here does not need to go through the additional check. Therefore, $w _ { 0 } ( 3 ) = w ^ { * }$ and $F _ { 2 } ^ { 3 } [ 3 ] = \bar { f } _ { 2 } ^ { 3 } ( 3 ) = \bar { 9 } . 2 5 \mathrm { a n d } V _ { 2 } ^ { 3 } [ 3 ] = 6 3 . 0 9 .$

We continue the backward recursion until $t = 0 ,$ where we repeat the above process of evaluating the IVC values for each of the possible order-sizes based on the average reward and variance of the subsequent states. Then we pick the optimal order size by ordering the IVC values in descending order and picking the one that has the maximum IVC value. Suppose the optimal order-size is 1 the corresponding average reward and variance are 30 and 10 respectively. Therefore, $F _ { 0 } ^ { 3 } [ 2 ] = f _ { 0 } ^ { 3 } ( 2 ) =$ 30 and $V _ { 0 } ^ { 3 } [ 2 ] = 1 0 .$ . We store the average reward and variance value at t = 0 in E[j = 1] = 30 and $V a r [ j = 1 ] = 1 0 .$

Next, we increment $j = 1 + y = 2$ and solve the inventory control model again starting with the initial state (2) and using backward recursion algorithm. As before at the terminal states $V _ { 3 } ^ { 3 } [ z ] = 0 \mathrm { a n d } F _ { 3 } ^ { 3 } [ z ] = 0 .$ Now suppose at a subsequent time-period t = 1, the problem reaches the state (1). We now <sup>fi</sup>gure out the IVC values for each of the possible actions. We sort the actions in descending order based on the IVC values. Then we consider the actions with respect to the top two IVC values since in this run $j = 2$ . Let the top two order sizes based on their IVC values along with their corresponding functional values be:

$$
f _ {1} ^ {3} (1) = \left\{ \begin{array}{l} q _ {1} = 1: 2 0 \\ q _ {1} = 2: 1 5 \end{array} \right.
$$

Here the maximum average reward corresponds with the order size equal to 1. Therefore, $w ^ { * } = 2 0$ . We store the variance and average reward values corresponding to order-size = 1 in $V _ { 1 } ^ { 3 } [ 2 ]$ and $F _ { 1 } ^ { 3 } [ 2 ]$

We continue the backward recursion until $t = 0 .$ Using the actions corresponding to the top two IVC values we pick the optimal order size based on the maximum average reward and then checking with the average reward that was earned in the previous run. We store the average reward and the variance corresponding to the optimal order size at t = 0 in E[j = 2] and $V a r [ j = 2 ]$ ] respectively. Next, we again increment j = 3 and continue the above process. We do this until j = 4. We then use the E[j] and $V a r [ j ] \ \forall j = 1 , 2 , 3 ,$ 4 to construct the riskreward curve.

Now, we check the performance of our heuristic by comparing the risk-reward frontier obtained by our heuristic against the risk-reward associated with all enumerated outcomes of the inventory control model.

## 4.3. Performance analysis of the RiskTrackr heuristic

Next we present the performance analysis of our heuristic against the ef<sup>fi</sup>cient frontier of the enumerated solutions obtained by running the inventory control model for different demand distributions. For simulating the different demand distributions we used the beta distribution and we discretized it to obtain different demand distributions by varying the values of the two shape parameters of the beta distribution, α and β. Beta distribution has been extensively used in a wide variety of applications because of its <sup>fl</sup>exibility in generating different kinds of probability distributions (see, for example, Fry et al. [25], Tripathi et al. [52], Basu and Nair [7], and Lieckens et al. [34]). The beta parameters used for generating the demand distributions are given in Table 1. For the performance evaluation, we picked a 5-period problem with maximum order-size equal to 10 in each state. Here the unit purchasing cost $u = \$ 3$ , unit holding cost per time period $h = \$ 1$ and the unit selling price $s = \$ 10$ . We assume that the salvage value for unsold inventory at the boundary is zero and the discount factor $\beta = 0 . 9 8 .$ . We assume that the demand possibilities range from 0 to 10. The demand distributions are given in detail in Appendix A.2. We used a small-dimension problem here so that we can enumerate all the possible risk-reward outcomes. In the RiskTrackr heuristic we increased the increment factor y by one in each subsequent run. The problem considered above has around one thousand possible paths and equivalent number of possible solutions. We then compared the performance of the risk-reward curve obtained from RiskTrackr against the enumerated ef<sup>fi</sup>cient frontier.

Performance of the heuristics ef<sup>fi</sup>cient frontiers against enumerated ef<sup>fi</sup>cient frontiers for the inventory control model.

<table><tr><td colspan="2">Beta parameters</td><td rowspan="2">Shape of the probability density function of the demand distribution</td><td rowspan="2">Mean % deviation from enumerated efficient frontier</td><td colspan="3">Hit rate (% occurrence of solutions with deviations from enumerated efficient frontier)</td></tr><tr><td>α</td><td>β</td><td>&lt;1%</td><td>&lt;2%</td><td>&lt;5%</td></tr><tr><td>5</td><td>10</td><td>Right skewed</td><td>0.00%</td><td>100.0%</td><td>100.0%</td><td>100.0%</td></tr><tr><td>1</td><td>1</td><td>Uniform</td><td>0.02%</td><td>99.2%</td><td>99.2%</td><td>100.0%</td></tr><tr><td>5</td><td>5</td><td>Bell-shaped</td><td>0.02%</td><td>99.2%</td><td>99.6%</td><td>100.0%</td></tr><tr><td>10</td><td>5</td><td>Left skewed</td><td>0.04%</td><td>99.2%</td><td>99.2%</td><td>100.0%</td></tr></table>

a  
![](/api/attachments/DEK3ZWWA/fulltext/images/b9be29bac4eaef0efb04cbf0d41700b11fc6e685fccffdbb9eecdc5c1df96913.jpg)

![](/api/attachments/DEK3ZWWA/fulltext/images/814782ab142e679e048482cb411c1d669170ecef4a37b27bad0d0e3e73bf1bfb.jpg)  
Fig. 3. Risk-reward solutions at different levels of risk for demand distribution with high variance.

Since we used an increment factor of one in the RiskTrackr heuristic we needed to run it 10 times q^ 10 to get the risk-reward frontier. Therefore, out of a thousand possible solutions our heuristics picks 10 that are on the ef<sup>fi</sup>cient frontier. For the problems studied here the RiskTrackr heuristic took around 15 min to run on a 2-GHz PC whereas for the same problems to enumerate all the solutions it took around 4 h. The run time for RiskTrackr to provide the risk-reward solutions depends on the granularity of the increment factor y, if y is low, there will be more iterations, run time will be higher and there will be more number of risk-reward solutions to draw the ef<sup>fi</sup>cient frontier. Here we used y = 1 so the heuristic was run for the maximum possible iterations.

Table 1 presents the performance evaluation results of the ef<sup>fi</sup>cient frontier constructed by RiskTrackr compared to the enumerated ef<sup>fi</sup>- cient frontier for various demand distributions. Here we have used four different demand distributions, viz., right-skewed, bell-shaped, uniform and left-skewed. We study the Mean percentage deviation of the RiskTrackr ef<sup>fi</sup>cient frontier from the enumerated ef<sup>fi</sup>cient frontier. We also analyze the Hit-rate of the RiskTrackr efficient frontier Hit-rate of the RiskTrackr heuristic is de<sup>fi</sup>ned as the percentage of risk-reward solutions with deviations from the enumerated ef<sup>fi</sup>cient frontier. We calculated the reward at various levels of risk along the two ef<sup>fi</sup>cient frontiers and computed the Mean percentage deviation and Hit-rate of the RiskTrackr heuristic at b 1%, b 2% and 5% deviations from the enumerated ef<sup>fi</sup>cient frontier. We <sup>fi</sup>nd that on an average the

Mean percentage deviation between the heuristics and the enumerated ef<sup>fi</sup>cient frontiers were less than 0.04% and the Hit-rate of the heuristics ef<sup>fi</sup>cient frontier is 100% at the 5% level. Based on the above accuracy measures we can conclude that our heuristic performs creditably in constructing ef<sup>fi</sup>cient frontiers.

Based on the above performance evaluations of our heuristic we can safely conclude that our methodology provides a novel and useful way of obtaining risk-reward curves in a stochastic looking for different policies at various levels of risk-exposure. Next, we focus on the managerial insights for the inventory control model based on the risk-reward curves.

## 5. Managerial insights

The utility of our methodology is in identifying optimal inventory policies that tradeoff rewards at different levels of risk. We illustrate the managerial insights that can be obtained by tracking the optimal rewards at different levels of risk for demand distributions that have the same mean but different variances. As before we used the beta distribution and discretized it to obtain different demand distributions by varying the values of the two parameters of the beta distribution, α and β. The different values of α and β used in the analysis are shown in Appendix A.3. The demand possibilities take values from 0 to 15 with the probability weights determined by the discretized beta distribution.

![](/api/attachments/DEK3ZWWA/fulltext/images/1e51cec08938844ff8e56a80cc2b73a682af62e5d262f68266044a09c72af4c7.jpg)

b  
![](/api/attachments/DEK3ZWWA/fulltext/images/c13727f33099efa34002d84e71e9a37828115f94024df8760aabc4d8e055c208.jpg)  
Fig. 4. Risk-reward solutions at different levels of risk for demand distribution with low variance.

![](/api/attachments/DEK3ZWWA/fulltext/images/d5ce62d202fe38684a0db78f2c8c2b58fa6a59fc34032732b1b7c4afa3d50fc3.jpg)  
Fig. 5. Percentage reduction in average pro<sup>fi</sup>t from maximum pro<sup>fi</sup>t vs. percentage reduction in variance of pro<sup>fi</sup>t values.

Here we analyze a problem with 10 time periods $( T = 1 0 )$ and initial inventory equal to 5. We kept the unit purchase cost $u = \$ 3$ unit holding cost $h = \$ 1$ , salvage value $\lambda = 0 ,$ , unit selling price s = \$10 and the discount factor $\beta = 0 . 9 8 .$ . The maximum order size, q, at any state is 20. We ran the model for various other parameter values and similar results were obtained; however for presentation brevity and illustrative purposes, we are going to use the results for the above dataset. On a 2-GHz PC it took around 4 h for RiskTrackr to provide the risk-reward solutions for these larger sized problem sets.

In Fig. 3(a) we present the ef<sup>fi</sup>cient frontier obtained by using our methodology for the demand distribution that has high variance. From the ef<sup>fi</sup>cient frontier we track the optimal pro<sup>fi</sup>ts at different levels of the variance of the pro<sup>fi</sup>t values and present the results in Fig. 3(b). We show the maximum reward for the unconstrained problem which is 180 corresponding to a variance of 1719 units. Then we highlight the reduction in optimal rewards by constraining the level of risk given as some percentage of the maximum reward. For example, the optimal reward when the variance is less than 500% of the maximum reward, i.e., less than 900 the reward reduces to 171, and when variance is less than 100% of the maximum reward, i.e., less than 180 the reward reduces to 150. Similar graphs are shown for the demand distribution that has lower variance in Fig. 4(a) and (b). We <sup>fi</sup>nd that in both cases there are risk-reward solutions that provide minor reduction in average profit from the maximum reward but at the same time lead to considerable reduction in variance or risk. Moreover, when the variance is high, we <sup>fi</sup>nd that substantial bene<sup>fi</sup>ts can be obtained. This is of particular importance when the demand distribution is assumed to be uniform which, relative to other distributions, has high variance. In practice, when only limited information is known about the demand other that its range, it is common to assume a uniform distribution.

Order size with Increasing risk under right-skewed demand distributior

In Fig. 5, we illustrate how the average pro<sup>fi</sup>t from inventory policies falls by limiting the variance of the policy. It shows that if we wish to remove all the risk from the policies (the right side of the curves), the loss in pro<sup>fi</sup>t can be steep. We also find that the loss in reward is lesser when the demand variability is higher, once again emphasizing the usefulness of our methodology for high risk scenarios, such as the uniform distribution. Overall these risk-reward solutions are extremely useful for a risksensitive decision-maker because losing a little in terms of average profit but gaining signi<sup>fi</sup>cantly in risk-exposure could be highly bene<sup>fi</sup>cial.

![](/api/attachments/DEK3ZWWA/fulltext/images/d632a4878c0864c603a8081f7315c2d342e4342b1b5292bb28c16cb205d8b05c.jpg)  
a  
Order size with increasing risk under bell-shaped demand distribution

Order size with increasing risk under uniform demand distribution  
![](/api/attachments/DEK3ZWWA/fulltext/images/67350af1cd1cbc6a00b8a5bf9f51042323195c3d687612b700024f042ef64ad6.jpg)  
b

![](/api/attachments/DEK3ZWWA/fulltext/images/76f9feee4449119d7f326a0b7e7da2f2adbc93b08f11237c2f04f49ab0d69e5c.jpg)  
c

Order size with increasing risk under left-skewed demand distribution  
![](/api/attachments/DEK3ZWWA/fulltext/images/12d5d10ee1fa8a776945970ffec6e778be733a89b96353126355adf00ff4e3bc.jpg)  
Fig. 6. Order sizes at varying levels of risk for different demand distributions.

Next, in Fig. 6 we analyze the inventory decisions at varying levels of risk. Here we study the order sizes that lead to the most ef<sup>fi</sup>cient outcomes, i.e., the ones that earned the highest reward at a particular level of risk. We ran the inventory control model for different demand distributions viz., right-skewed, bell-shaped, uniform and left-skewed. The demand distributions are given in detail in Appendix A.3. The other exogenous parameters are the same as in the previous set of results. We find that for all the different demand distributions, order sizes increase with increasing risk. The conclusion is that <sup>fi</sup>rms willing to take greater risks should increase their order sizes to increase profits. On the other hand, if a firm wants to minimize its risk exposure then it should order less, this would lead to less variability in the outcomes though the associated reward will also be lower. The above results provide managers with critical insights into the inventory decisions at different levels of risk and they can implement these actions based on their risk tolerance.

## 6. Conclusions and future research directions

The main theoretical contributions of this paper are two-fold. Firstly, we propose a methodology, Variance-Retentive SDP, for tracking the variance of the possible outcomes at each stage and state of a stochastic dynamic program. Variance-Retentive SDP provides an algorithm for solving stochastic dynamic programming problems where the optimization is done over two metrics, mean and variance, instead of the usual one. Secondly, given the popularity of ef<sup>fi</sup>cient frontier approaches, we develop a heuristic, RiskTrackr, to identify such mean– variance frontiers in multi-period inventory control using our Variance-Retentive SDP algorithm. In many real-life scenarios, inventory managers are concerned about the risks or the variability associated with a set of inventory policies and not just the expected reward. Instead of identifying one policy to achieve the stated objective, managers are often interested in obtaining set of policies at different levels of risk sensitivity. Risk-sensitive managers can use RiskTrackr to construct ef<sup>fi</sup>- cient risk-reward curves and identify a set of ordering policies that maximizes pro<sup>fi</sup>t at various levels of risk.

We applied our Variance-Retentive SDP algorithm and the RiskTrackr heuristic to construct ef<sup>fi</sup>cient risk-reward curves for different demand distributions having varving levels of variability. We identi<sup>fi</sup>ed risk-reward solutions that provide signi<sup>fi</sup>cant reduction in variance of the pro<sup>fi</sup>t values with negligible reduction in pro<sup>fi</sup>t from the maximum expected reward. We <sup>fi</sup>nd that the reward loss compared to the variance reduction is lesser when the demand variability is higher. This result makes our methodology more useful in risky scenarios marked by high demand volatility. We analyzed the ordering decisions for different demand scenarios. We <sup>fi</sup>nd that a <sup>fi</sup>rm willing to take more risks should increase their order sizes which would lead to higher average rewards but at the same time expose the <sup>fi</sup>rm to greater risks. On the other hand, if a <sup>fi</sup>rm wants to minimize its risk exposure then it should order less; this would lead to less variability in the outcomes though the associated reward will also be lower. These results provide useful insights for managers looking for optimal inventory decisions at different levels of risk.

There are a number of avenues for extending this current research in the future. Here we have applied our heuristics to a <sup>fi</sup>nite-horizon stochastic dynamic programming model for inventory control. In the future, we could look at developing heuristics that provide risk-reward solutions for in<sup>fi</sup>nite horizon inventory control models. Risk-sensitive optimization in stochastic dynamic setting is an important area that has seen very limited research. Developing ef<sup>fi</sup>cient heuristics for constructing risk-reward curves for other popular stochastic programming models such as capacity expansion, advertising investments and cash management could be worthwhile research topics. Practitioners often face multi-dimensional problems where inventory policies are derived in conjunction with marketing and capital budgeting decisions.

Analyzing risk in those real-life situations might require risk management at a portfolio level. This could be an interesting future research area where the decisions could be correlated. There are other important stochastic dynamic problems that fall under the umbrella of optimal stopping rule models such as equipment replacement, options exercising and secretary problems. Coming up with ef<sup>fi</sup>cient heuristics that can be used to construct risk-reward curves for these models could be interesting future research endeavors. In this paper we have used variance as a measure of risk. Using downside risk measures such as semivariance, value at risk or lower partial moments to deduce the riskreward solutions will be a worthwhile future research study.

## Appendix A

## A.1. Derivation of Eq. (3)

If a random variable Z takes values $X _ { i }$ with probability $p _ { i } , i = 1 , 2$ n, the ${ \begin{array} { l } { \displaystyle { 1 E ( Z ) = E [ E ( Z | X _ { 1 } , X _ { 2 } , . . . , X _ { n } ) ] = E \left[ \sum _ { i = 1 } ^ { n } p _ { i } X _ { i } \right] = \sum _ { i = 1 } ^ { n } p _ { i } E ( X _ { i } ) = \sum _ { i = 1 } ^ { n } p _ { i } \mu _ { i } } } \\ { \displaystyle \mu _ { i } = E ( X _ { i } ) . } \end{array} }$ where

The future states in the dynamic programming problem are random variables because the future states depend on chance or the probability nodes. Therefore, for our problem Z is the present state at t and $X _ { i } ^ { \prime } s$ are the states that can be traversed in $t + 1$

$$
E \left(Z ^ {2}\right) = \sum_ {i = 1} ^ {n} p _ {i} E \left(X _ {i} ^ {2}\right)
$$

Now;

The variance of $X _ { i }$ is given by: $\sigma _ { i } ^ { 2 } = E ( X _ { i } ^ { 2 } ) - \mu _ { i } ^ { 2 } .$ . Then,

$$
E \left(Z ^ {2}\right) = \sum_ {i = 1} ^ {n} p _ {i} \left(\sigma_ {i} ^ {2} + \mu_ {i} ^ {2}\right)
$$

Now the variance of Z, denoted by $V a r ( Z )$ is given by:

$$
\begin{array}{l} \operatorname{Var} (Z) = E \left(Z ^ {2}\right) - [ E (Z) ] ^ {2} \\ \qquad = \sum_ {i = 1} ^ {n} p _ {i} \left(\sigma_ {i} ^ {2} + \mu_ {i} ^ {2}\right) - \left(\sum_ {i = 1} ^ {n} p _ {i} \mu_ {i}\right) ^ {2} \\ \qquad = \sum_ {i = 1} ^ {n} p _ {i} \sigma_ {i} ^ {2} + \sum_ {i = 1} ^ {n} p _ {i} \mu_ {i} ^ {2} - \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} p _ {i} p _ {j} \mu_ {i} \mu_ {j} \end{array}\tag{5}
$$

In the inventory model, Eqs. (1) and (2), from any state $( z )$ at time t, the problem goes to the possible states in $t + 1$ with probability $p ( d )$ based on actions q. Then using Eq. (5), the variance for any order size $q ,$ at any state (z) is given by:

$$
\begin{array}{l} \gamma_ {q} (z) = \sum_ {d} p (d) \beta^ {2} V _ {t + 1} ^ {T} [ z - \widetilde {d} + q ] \\ \quad + \sum_ {d} p (d) (\widetilde {s d} - u q - h \widetilde {z} + \beta F _ {t + 1} ^ {T} [ z - \widetilde {d} + q ]) ^ {2} \\ \quad - \sum_ {d} p (d) (\widetilde {s d} - u q - h \widetilde {z} + \beta F _ {t + 1} ^ {T} [ z - \widetilde {d} + q ]) \mu_ {t + 1} ^ {T} (z) \end{array}
$$

where $\begin{array} { r } { \mu _ { t + 1 } ^ { T } ( z ) = \sum _ { d } p ( d ) \Big ( \widetilde { s d } - u q - h \widetilde { z } + \beta F _ { t + 1 } ^ { T } \Big [ z - \widetilde { d } + q \Big ] \Big ) . } \end{array}$

The variance at any state (z) is denoted by V<sup>T</sup>[z] and it is the variance corresponding to the optimal order size $q ^ { * }$ . The expected reward corresponding to the optimal actions is denoted by F<sup>T</sup>[z].

A.2. Demand distribution used in the performance analysis of RiskTrackr in Section 4.3

<table><tr><td rowspan="3" colspan="2">Beta Parameters</td><td rowspan="3">Shape of the probability density function of the demand distribution</td><td colspan="11">Demand structure</td></tr><tr><td colspan="11">Demand possibilities</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>α</td><td>β</td><td></td><td>Probability distribution of demand</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>10</td><td>Right-skewed</td><td>0.01</td><td>0.09</td><td>0.23</td><td>0.29</td><td>0.22</td><td>0.11</td><td>0.04</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>1</td><td>1</td><td>Uniform</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td><td>0.09</td></tr><tr><td>5</td><td>5</td><td>Bell-shaped</td><td>0.00</td><td>0.01</td><td>0.06</td><td>0.13</td><td>0.19</td><td>0.22</td><td>0.19</td><td>0.13</td><td>0.06</td><td>0.01</td><td>0.00</td></tr><tr><td>10</td><td>5</td><td>Left-skewed</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.04</td><td>0.11</td><td>0.22</td><td>0.29</td><td>0.23</td><td>0.09</td><td>0.01</td></tr></table>

## A.3. Demand distributions used in Section 5

<table><tr><td rowspan="2" colspan="2">Beta parameters</td><td rowspan="2">Shape of the probability density function of the demand distribution</td><td rowspan="2">Mean</td><td rowspan="2">Variance</td><td colspan="16">Demand structure</td></tr><tr><td colspan="16">Demand possibilities</td></tr><tr><td rowspan="2">α</td><td rowspan="2">β</td><td rowspan="2"></td><td rowspan="2"></td><td rowspan="2"></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td colspan="16">Probability distribution of demand</td></tr><tr><td>5</td><td>10</td><td>Right-skewed</td><td>5.33</td><td>3.56</td><td>0.00</td><td>0.02</td><td>0.08</td><td>0.15</td><td>0.20</td><td>0.20</td><td>0.16</td><td>0.10</td><td>0.06</td><td>0.02</td><td>0.01</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>10</td><td>5</td><td>Left-skewed</td><td>10.67</td><td>3.56</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.02</td><td>0.06</td><td>0.010</td><td>0.16</td><td>0.20</td><td>0.20</td><td>0.15</td><td>0.08</td><td>0.02</td><td>0.00</td></tr><tr><td>5</td><td>5</td><td>Bell-shaped</td><td>8</td><td>5.82</td><td>0.00</td><td>0.00</td><td>0.01</td><td>0.03</td><td>0.07</td><td>0.10</td><td>0.13</td><td>0.15</td><td>0.15</td><td>0.13</td><td>0.10</td><td>0.07</td><td>0.03</td><td>0.01</td><td>0.00</td><td>0.00</td></tr><tr><td>1</td><td>1</td><td>Uniform</td><td>8</td><td>21.33</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td><td>0.06</td></tr></table>

The bell-shaped and uniform demand distributions are used for the analysis where we kept the mean of the demand distributions the same and varied the variances. The left and the right-skewed distribution along with the bell-shaped and uniform distributions are used for the analysi presented in Fig. 6.

## References

[1] S. Ahmed, U. Çakmak, A. Shapiro, Coherent risk measures in inventory problems, European Journal of Operational Research 182 (1) (2007) 226–238.

[2] R.K. Ahuja, M.M. Hanna, Decision support systems development: an essential part of OR education, OR/MS Today (April 2004) 12–13.

[3] D.D. Achabal, S.H. Mcintyre, S.A. Smith, K. Kalyanam, A decision support system for vendor managed inventory, Journal of Retailing 76 (4) (2004) 430–454.

[4] V. Agrawal, S. Seshadri, Impact of uncertainty and risk aversion on price and order quantity in the newsvendor problem, Manufacturing Service Operations Management 2 (4) (2000) 410–423.

[5] K.J. Arrow, T. Harris, J. Marschak, Optimal inventory policy, Econometrica 29 (1951) 250–272.

[6] P. Artzner, F. Delban, J.-M. Eber, D. Heath, H. Ku, Coherent multiperiod risk adjusted values and Bellman's principle, Annals of Operations Research 152 (2007) 5–22.

[7] P. Basu, S.K. Nair, Analysis of back-of<sup>fi</sup>ce outsourcing contracts for <sup>fi</sup>nancial services operations, Journal of the Operational Research Society 63 (2012) 1679–1692.

[8] M. Baykal-Gursoy, K.W. Ross, Variability sensitive Markov decision processes, Mathematics of Operations Research 17 (3) (1992) 558–571.

[9] H.M. Beheshti, A decision support system for improving performance of inventory management in a supply chain network, International Journal of Productivity and Performance Management 59 (5) (2010) 452–467

[10] P. Berling, K. Rosling, The effects of <sup>fi</sup>nancial risks on inventory policy, Management Science 51(12)(2005) 1804-1815

[11] V.S. Borkar, S.P. Meyn, Risk-sensitive optimal control for Markov decision processes with monotone cost, Mathematics of Operations Research 27 (1) (2002) 192–209.

[12] M. Bouakiz, M.J. Sobel, Inventory control with an exponential utility criterion, Operations Research 40 (1992) 603-608

[13] J. Buzacott, H. Yan, H. Zhang, Risk analysis of commitment–option contracts with forecast updates, IIE Transactions 43 (2011) 415–431

[14] F. Caro, J. Gallien, Inventory management of a fast-fashion retail network, Operations Research 58 (2) (2010) 257–273.

[15] X. Chen, M. Sim, D. Simchi-Levi, P. Sun, Risk aversion in inventory management, Operations Research 55 (5) (2007) 828–842

[16] T. Choi, D. Li, H. Yan, Mean–variance analysis for the newsvendor problem, IEEE Transactions on Systems, Man, and Cybernetics - Part A: Systems and Humans 38 (5) (2008) 1169–1180.

[17] K. Chung, Risk in inventory models: the case of newsboy problem—Optimality conditions, Journal of Operational Research Society 41 (2) (1990) 173–176.

[18] K.J. Chung, Mean–variance tradeoffs in an undiscounted MDP: the unichain case, Operations Research 42 (1994) 184–188.

[19] T. Copeland, J. Weston, Financial Theory and Corporate Policy, Addison-Wesley, Reading, MA, 1983.

[20] A. Dvoretzky, J. Kiefer, J. Wolfowitz, On the optimal character of the (s, S) policy in inventory theory, Econometrica 20 (1953) 586–596.

[21] L. Eeckhoudt, C. Gollier, H. Schlesinger, The risk-averse (and prudent) newsboy, Management Science 41 (5) (1995) 786–794.

[22] E.J. Elton, M.J. Gruber, S.J. Brown, W.N. Goetzmann, Modern Portfolio Theory and Investment Analysis, John Wiley & Sons, 2009

[23] E. Fama, Foundations of Finance, Basic Books, New York, 1976.

[24] J.A. Filar, L.C.M. Kallenberg, H.M. Lee, Variance-penalized Markov decision processes, Mathematics of Operations Research 14 (1) (1989) 147–161.

[25] M.J. Fry, M.J. Magazine, U.S. Rao, Fire<sup>fi</sup>ghter staf<sup>fi</sup>ng including temporary absences and wastage, Operations Research 54 (2) (2006) 353–365.

[26] Z. Hong, C.K.M. Lee, A decision support system for procurement risk management in the presence of spot market, Decision Support Systems 55 (1) (2013) 67–78.

[27] R.A. Howard, J.E. Matheson, Risk-sensitive Markov decision processes,, Management Science 18 (7) (1972) 356–369.

[28] D. Iglehart, Optimality of (s, S) policies in the in<sup>fi</sup>nite horizon dynamic inventory problem, Management Science 9 (1963) 259–267.

[29] H. Jain, H. Groenevelt, N. Rudi, Periodic review inventory management with contingent use of two freight modes with <sup>fi</sup>xed costs, Naval Research Logistics (NRL) 58 (4) (2011) 400–409.

[30] S. Karlin, A. Fabens, The (s,S) inventory model under Markovian demand process, in: J. Arrow, S. Karlin, P. Suppes (Eds.), Mathematical Methods in the Social Sciences, Stanford Univ. Press, Stanford, CA, 1959

[31] H. Kawai, A variance minimization problem for a Markov decision process, European Journal of Operational Research 31 (1) (1987) 140–145.

[32] M. Khouja, The single-period (newsvendor) problem: literature review and suggestions for future research, Omega 27 (5) (1999) 537–553.

[33] H.S. Lau, The newsboy problem under alternative optimization objectives, Journal of Operational Research Society 31 (6) (1980) 525–535

[34] K.T. Lieckens, P.J. Colen, M.R. Lambrecht, Optimization of a stochastic remanufacturing network with an exchange option, Decision Support Systems 54 (4) (2012) 1548–1557.

[35] H. Markowitz, Portfolio selection: ef<sup>fi</sup>cient diversi<sup>fi</sup>cation of investment, Cowls Foundation Monograph, 16, Yale University Press, New Haven, 1959.

[36] H.M. Markowitz, Foundations of portfolio theory, The Journal of Finance 46 (2) (1991).469-477

[37] M. Parlar, Z.K. Weng, Balancing desirable but con<sup>fl</sup>icting objectives in the newsvyendor problem JIE Transactions 35 (2003) 131–142

[38] M.L. Puterman, Markov Decision Processes, Discrete Stochastic Dynamic Program ming John Wiley and Sons New York 2005.

[39] Y. Qin, R. Wang, A.J. Vakharia, Y. Chen, M.M. Seref, The newsvendor problem: review and directions for future research, European Journal of Operational Research 213 (2) (2011) 361–374.

[40] A. Ruszczynski, Risk-averse dynamic programming for Markov decision processes, Mathematical Programming 125 (2010) 235–261.

[41] S.S. Sana, A production-inventory model of imperfect quality products in a three-layer supply chain, Decision Support Systems 50 (2) (2011) 539–547.

[42] S.S. Sana, Price sensitive demand with random sales price—a newsboy problem, International Journal of Systems Science 43 (3) (2012) 491–498.

[43] S.S. Sana, The stochastic EOQ model with random sales price, Applied Mathematics and Computation 218 (2) (2011) 239–248.

[44] S.S. Sana, An economic order quantity model for nonconforming quality products, Service Science 4 (4) (2012) 331–348.

[45] A. Shapiro, On a time consistency in risk averse multistage stochastic programming, Operations Research Letters 39 (2009) 143–147.

[46] W.E. Sharpe, The Sharpe ratio, The Journal of Portfolio Management 21 (1) (1994) 49–58.

[47] P.S. Sethi, F. Cheng, Optimality of (s, S) policies in inventory models with Markovian demand, Operations Research 45 (6) (1997) 931–939.

[48] M. Sobel, The variance of discounted Markov decision processes, Journal of Applied Probability 19 (4) (1982) 794–802.

[49] M. Sobel, Mean–variance tradeoffs in an undiscounted MDP, Operations Research 42 (1) (1994) 175–183.

[50] C.S. Tang, K. Rajaram, A. Alptekinoglu, J. Ou, The bene<sup>fi</sup>ts of advance booking discount programs: model and analysis, Management Science 50 (4) (2004) 465–478.

[51] C.S. Tapiero, Value at risk and inventory control, European Journal of Operational Research 163 (3) (2005) 769–775.

[52] A.K. Tripathi, S.K. Nair, G.G. Karuga, Optimal lot sizing policies for sequential online auctions, IEEE Transactions on Knowledge and Data Engineering 21 (4) (2009) 554–567.

[53] A. Veinott Jr., On the optimality of (s, S) inventory policies: new conditions and a new proof, SIAM Journal of Applied Mathematics 14 (1966) 1067–1083.

[54] J. Vörös, Portfolio analysis—an analytic derivation of the ef<sup>fi</sup>cient portfolio frontier, European Journal of Operational Research 23 (3) (1986) 294–300.

[55] Y. Wei, T.M. Choi, Mean–variance analysis of supply chains under wholesale pricing and pro<sup>fi</sup>t sharing scheme, European Journal of Operational Research 204 (2010) 255–262.

[56] C.X. Wang, S. Webster, The loss-averse newsvendor problem, Omega 37 (1) (2009) 93–105.

[57] D.J. White, Mean variance and probabilistic criteria in <sup>fi</sup>nite Markov decision processes: a review, Journal of Optimization Theory and Applications 56 (1988) 1–30.

[58] C. Wu, Y. Lin, Minimizing risk models in Markov decision processes with policies depending on target values, Journal of Mathematical Analysis and Applications 231 (1) (1999) 47–67.

[59] J. Wu, J. Li, S. Wang, T.C.E. Cheng, Mean–variance analysis of the newsvendor model with stockout cost, Omega 37 (2009) 724–730.

[60] M. Xu, Y.F. Chen, X. Xu, The effect of demand uncertainty in a price-setting newsvendor model, European Journal of Operational Research 207 (2) (2012) 946–957.

[61] D. Zhang, H. Xu, Y. Wu, Single and multi-period optimal inventory control models with risk-averse constraints, European Journal of Operational Research 199 (2009) 420–434.

Preetam Basu is an Assistant Professor in the Operations Management Group at the Indian Institute of Management Calcutta. He has a doctorate degree in Operations Management from the University of Connecticut, USA. Earlier, he did his MS in Applied Mathematics from the University of Minnesota, USA. His research interests include supply chain management, start-up operations, services outsourcing, supply chain <sup>fi</sup>nance, and revenue management. His research has been published in the Journal of Operational Research Society, Business Process Management Journal and International Journal of Logistics Systems and Management.

Suresh Nair is a Professor, an Ackerman Scholar and a Dun & Bradstreet CITI Research Fellow in the Operations and Information Management Department at the School of Business in University of Connecticut, USA. He has more than 25 years of experience in teaching and consulting, and has been a consultant to several <sup>fi</sup>rms such as JP Morgan Chase, General Electric, Merrill Lynch and Booz & Company. He was part of the team that received the 2002 Wagner Prize for the Practice of Operations Research for work he did in credit cards. Dr. Nair works on the interface of operations, <sup>fi</sup>nance and marketing, is a Senior Editor of Production and Operations Management, and has several publications in leading journals such as Management Science, Production and Operations Management, Interfaces, Decision Sciences, Decision Support Systems and European Journal of Operational Research.
