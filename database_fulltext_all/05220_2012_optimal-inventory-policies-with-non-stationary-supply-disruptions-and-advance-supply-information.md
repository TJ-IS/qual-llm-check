---
otero_id: 5220
otero_key: "XRRHSWKX"
title: "Optimal inventory policies with non-stationary supply disruptions and advance supply information"
authors: "Bilge Atasoy; Refik Güllü; Tarkan Tan"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal inventory policies with non-stationary supply disruptions and advance supply information

Bilge Atasoy <sup>a,1</sup>, Refik Güllü <sup>a,</sup>⁎, Tarkan Tan

<sup>a</sup> Bogazici University Industrial Engineering Department, Bebek, 34342 Istanbul, Turkey <sup>b</sup> School of Industrial Engineering, Eindhoven University of Technology, The Netherlands

a r t i c l e i n f o

Available online 25 January 2012

Keywords: Supply uncertainty Advance supply information Inventory Optimal policy

## a b s t r a c t

We consider the production/inventory problem of a manufacturer (or a retailer) under non-stationary and stochastic supply availability. Although supply availability is uncertain, the supplier would be able to predict her near future shortages – and hence supply disruption to (some of) her customers – based on factors such as her pipeline stock information, production schedule, seasonality, contractual obligations, and noncontractual preferences regarding other manufacturers. We consider the case where the information on the availability of supply for the near future, which we refer to as advance supply information (ASI), is provided by the supplier. The customer demand is deterministic but non-stationary over time, and the system costs consist of <sup>fi</sup>xed ordering, holding and backorder costs. We consider an all-or-nothing type of supply availability structure and we show the optimality of a state-dependent (s,S) policy. For the case with no <sup>fi</sup>xed ordering cost we prove various properties of the optimal order-up-to levels and provide a simple characterization of optimal order-up-to levels. For the model with <sup>fi</sup>xed ordering cost, we propose a heuristic algorithm for <sup>fi</sup>nding a good ordering strategy. Finally, we numerically elaborate on the value of ASI and provide managerial insights.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction and related literature

Numerous success and failure stories have taught us that supply chains need to take potential supply disruptions into account in the planning phase, rather than ‘<sup>fi</sup>re-<sup>fi</sup>ghting’ when disruptions take place. The supply process in a supply chain can be disrupted for various reasons, which can be classi<sup>fi</sup>ed into two groups: i) unpredictable disruptions, which arise from natural disasters, terrorist attacks, accidents, and the like, and ii) predictable disruptions, which basically originate from capacity restrictions and scarcity of some resources at the supplier. Further, a predictable disruption might be either due to a temporary total lack of the supplier's production capacity (in which case none of her customers are satis<sup>fi</sup>ed), or the supplier's choice in allocating her restricted capacity to other manufacturers and/or products. The supplier would possibly be able to predict her near future shortages – and hence supply disruption to (some of) her customers – based on factors such as her pipeline stock information, production schedule, seasonality, contractual obligations and non-contractual preferences regarding other manufacturers, and the like. Nevertheless, a predictable disruption might remain unpredictable to the manufacturer (or the retailer) if the supplier does not inform him – at least to a certain extent – about this disruption. We refer to such information concerning future disruptions that are known to the supplier as advance supply information (ASI). The supplier might want to provide the manufacturer with ASI for several reasons including reputation and improving collaboration.

In this paper we consider the production/inventory problem of a manufacturer (or a retailer) under non-stationary stochastic supply uncertainty and availability of ASI. The supply chain environment that we consider consists of a manufacturer facing non-stationary deterministic demand, and an outside supplier with uncertainties in the delivery times and amounts. Novel features of our model are that (1) the supply availability over the planning horizon is time dependent, and (2) the supplier provides the manufacturer information regarding the supply conditions over a limited speci<sup>fi</sup>ed horizon (the ASI horizon). Moreover, since both the customer demand sequence, and the supply availability structure is time dependent, our model can also be used to capture possible correlations between the customer demand and the disruption duration in supply.

The supply structure that we consider is of all-or-nothing type and is similar to a clearing process: in a given period, the order placed by the manufacturer along with its backorders is supplied with a probability that depends on the period. Under this environmental setting, the manufacturer's problem becomes determining the optimal order amount in each period that minimizes expected linear holding and backorder costs and the cost of ordering over the planning horizon. As the manufacturer keeps track of the supply availability information provided by its supplier, any optimal policy should be a function of ASI as well as the time dependent nature of supply uncertainty. In this article we characterize the structure of the optimal policy and provide managerial insights on the impact of ASI on the optimal system performance. To the best of our knowledge, our paper is the <sup>fi</sup>rst one that provides an exact and near-explicit expression for optimal order-up-to levels as a function of the supply information.

The environment described above is suitable for the planning problem of a parts manufacturer where customer orders are the <sup>fi</sup>rm production quantities dictated by an upstream stage through a master production schedule. The parts manufacturer, now facing deterministic customer orders, needs to plan its own order quantities from an outside supplier whose delivery performance is time dependent and uncertain. The parts manufacturer tries to reduce the supply uncertainty by receiving the supply availability information from the supplier a number of periods in advance. Under the assumption of allor-nothing type supply structure, ASI is equivalent to knowing the timing of the supply availability (when the order is fully delivered and any backorders are cleared), and supply unavailability (nothing is delivered) periods during the ASI horizon. From this perspective our system also resembles a supply system where the inter-delivery times are non-stationary random variables, the supplier keeps track of the manufacturer's inventory position and a partial knowledge of the delivery times is revealed to the manufacturer.

Papers in production/inventory literature that model uncertainties in the supply side can be divided into three research tracks. Papers in the <sup>fi</sup>rst track model supply uncertainty by considering random durations in which supply is either completely unavailable or completely available (our paper falls into this group). [17] and [18] are early examples of allowing random supply disruptions in inventory literature. In both of these papers supply availability and unavailability durations are respective exponential random variables and the inventory models follow assumptions of Economic Order Quantity (EOQ) model. In particular, the demand process is continuous and stationary over time. [17] allows a replenishment (when the supply is available) when the inventory level drops to zero, whereas [18] incorporates a possibly non-zero reorder level and multiple suppliers. Under a Poisson demand process and fairly general availability and unavailability durations, [15] evaluates an (s,Q) type inventory policy. [8] considers a periodic review variation of the model in [17] where the supply unavailability durations are non-stationary random variables, and the demand quantities in successive periods are dynamic deterministic values. [8] presents a newsboy-like expression for obtaining the optimal order-up-to levels.

The second research track treats supply uncertainty as randomness in yield, where the quantity received is a random fraction of the quantity ordered starting with the pioneering work of Karlin, Yano and Lee, Gerchak et al., Henig and Gerchak, Wang and Gerchak, and Hsu and Bassok [13,23,6,9,22,10] which presents various production/inventory model incorporating random yield. In a recent article Yeo and Yuan [24] consider a model with random yield and demand cancelation, and show that the optimal ordering policy has a reorder point structure.

In the last research track, the production capacity, rather than the supply is considered to be random. Note that there is a subtle difference between uncertainty in supply and randomness in production capacity. In supply uncertainty models, when the supply is available it is assumed to be fully available. Therefore, supply uncertainty often occurs not as a constraint on the amount that can be ordered, but as an external factor that affects the quantity received (either nothing or a fraction of the ordered amount is received during the unavailability duration). In random capacity models on the other hand, the maximum amount that can be ordered (or produced) is a random variable, and hence the treatment of models with <sup>fi</sup>nite (but random) capacity is quite different. [4,11,7] consider periodic review inventory problems under random capacity. In these papers, demand and supply processes are assumed to be stationary. [5] considers the same problem, but allow the distribution of capacity to vary according to a Markov chain.

In the supply uncertainty literature, information on availability of future supply is typically modeled through considering supply uncertainty as a Markov process. In these models the probability distribution of supply availability in the next period depends on the current availability state (see, for example, [16,19,21,3]). We differ from the literature by explicitly including the supply information for a number of periods in our state de<sup>fi</sup>nition. Among the papers that treat production capacity as a random variable, [12,1] explicitly consider the existence of advance information on production capacity in their models. In these papers the evolution of capacity information follows stationary processes. Main differences of our work from previous papers that incorporate supply or capacity information in their models are that we allow the supply process to be nonstationary, and we provide exact and near-explicit expressions for the optimal policy parameters in a <sup>fi</sup>nite horizon setting.

In this article we make four major contributions: (1) we consider non-stationary supply uncertainty and model advance supply information, (2) we provide characterization for the optimal policies and when the <sup>fi</sup>xed cost is zero we provide easy-to-compute, nearexplicit solution for the optimal base stock levels as a function of ASI, (3) we propose and test a heuristic solution for the non-zero <sup>fi</sup>xed cost case, and (4) we provide managerial insights on the value of ASI.

The rest of the paper is organized as follows. In Section 2 we introduce our dynamic programming model and analyze the form of the optimal ordering policy. In Section 3 we consider the model with no <sup>fi</sup>xed cost and analyze the optimal policy. In Section 4 we present a heuristic approach for the model with <sup>fi</sup>xed ordering cost and discuss the performance of the heuristic. In Section 5 we provide a comprehensive numerical analysis. We conclude the paper in Section 6.

## 2. Description of the model

In this section we present the dynamic programming model for the problem and provide the optimal ordering policy. We <sup>fi</sup>rst describe the structure of supply uncertainty and ASI. The following notation is to be used throughout the paper but we introduce additional notation as need arises.

N number of periods in the planning horizon,

$D _ { n }$ demand in period n for n=1,2,…,N,

h holding cost per unit per period,

b backorder cost per unit per period,

A <sup>fi</sup>xed ordering cost

M Length of the ASI horizon, M≥1

$p _ { n }$ probability that supply is fully available in period n.

## 2.1. Structure of supply uncertainty and ASI

Supply uncertainty has an all-or-nothing type structure, such that in a given period supply is either fully available or completely unavailable. When supply is available in a given period we denote this period as a supply period. Supply availability probability is nonstationary over the planning horizon and supply availability in a period is independent of other periods. In addition, the supplier provides supply availability information to the manufacturer regarding the future periods. Therefore, manufacturer may reduce the uncertainty with the help of ASI. Suppose that at the beginning of period n the manufacturer receives information on supply availability. Then, the supply availability of the next M periods is known (in addition to the supply availability of the current period), which constitutes the ASI horizon. To be able to characterize the ASI vector accurately we de<sup>fi</sup>ne $\Omega _ { M }$ as an M dimensional vector, with elements in $\{ 0 , \infty \}$ . That is,

$$
\Omega_ {M} = \{(q _ {1}, \dots , q _ {M}): q _ {i} \in \{0, \infty \}, i = 1, 2, \dots , M \},
$$

where $q _ { i } = \infty$ implies a supply state meaning that supply is available, and $q _ { i } = 0$ implies a no-supply state meaning that supply is unavailable.

We de<sup>fi</sup>ne $W _ { n }$ as the random vector denoting the supply availability state for periods $n + 1 , . . . , n + M .$ . Note that $W _ { n } \in \Omega _ { M } .$ . Also let $Q _ { n }$ be the supply availability state for the current period n. We de<sup>fi</sup>ne $Z _ { n } = ( Q _ { n } , W _ { n } )$ as the supply availability state for periods $n , n + 1 , . . . , n + M .$ . Let $z _ { n } , w _ { n }$ and $q _ { n }$ be the realizations of $Z _ { n } , W _ { n }$ and $Q _ { n } ,$ respectively.

We can state $w _ { n }$ as $w _ { n } = \left( o _ { l } , r _ { M - l } \right)$ where o is a vector of size $l ~ ( 0 \leq l \leq M )$ with all entries being zero, and $r _ { M - l } \textbf { a }$ vector of size M−l with the <sup>fi</sup>rst entry being ∞ (the remaining entries can be either $\sim ~ 0 \Gamma$ zero). The value of l gives us the <sup>fi</sup>rst period after n (and before $n + M )$ that the supply will be available. If $l = 0 ,$ then $w _ { n } = r _ { M }$ (the supply is fully available in period $n + 1 )$ , and if $l = M , \ w _ { n } = o _ { M }$ (supply is unavailable in periods $n + 1 , n + 2 , . . . ,$ $n + M )$

## 2.2. Dynamic programming model

Let $L _ { n } ( y )$ denote the expected single-period inventory-related costs incurred at the end of period n where the inventory level after the realization of supply is y.

$$
L _ {n} (y) = h \max (0, y - D _ {n}) + b \max (0, D _ {n} - y).
$$

$L _ { n } ( y )$ is the sum of two convex functions, and hence it is convex in y. For $n = 1 , 2 , . . . , N + 1$ we de<sup>fi</sup>ne $C _ { n } ( I , z _ { n } )$ as the minimum expected cost of operating the system through periods $n , n + 1 , . . . , N + 1$ when the inventory level at the beginning of period n is I and supply availability state (i.e. the information vector) is ${ z _ { n } } = ( q _ { n } , w _ { n } )$ with $C _ { N + 1 } ( I , z ) \equiv 0$

The dynamic programming recursion for this problem is

$$
C _ {n} (I, z _ {n}) = \min _ {I \leq y \leq I + q _ {n}} \left\{A \delta (y - I) + L _ {n} (y) + E \left[ C _ {n + 1} \left(y - D _ {n}, w _ {n}, Q _ {n + M + 1}\right) \right] \right\},\tag{1}
$$

where $\delta ( y - I )$ is 1 when $y { > } I ,$ and zero otherwise. $Q _ { n + M + 1 }$ is the unknown supply availability state for period $n + M + 1$ , and its realization is to be known in period $n + 1$ . Stochasticity is due to the unknown supply state of period $n + M + 1$ . It will be with probability $p _ { n + M + 1 }$ and 0 with probability $1 - p _ { n + M + 1 }$

The sequence of events is as follows: (1) At the beginning of period n the new supply information for period n+M is received, and hence the new supply availability state becomes ${ z _ { n } } = ( q _ { n } , w _ { n } )$ . (2) The replenishment decision is made by taking z into account. (3) At the end of the period demand realization occurs and relevant costs are incurred.

For ease of notation, we de<sup>fi</sup>ne the auxiliary function $G _ { n } ( y , w _ { n } ) { : = }$ $L _ { n } ( y ) + E [ C _ { n + 1 } ( y - D _ { n } , w _ { n } , Q _ { n + M + 1 } ) ]$ . The dynamic programming recursion Eq. (1) then becomes

$$
C _ {n} (I, z _ {n}) = \min _ {I \leq y \leq I + q _ {n}} \left\{A \delta (y - I) + G _ {n} (y, w _ {n}) \right\},\tag{2}
$$

where the recurrence relation is considered within $G _ { n } .$

Cost functions $C _ { n }$ and $G _ { n }$ are not convex under the existence of a <sup>fi</sup>xed ordering cost. Theorem 1 states the A-convexity of cost functions. Therefore optimal policy is a state dependent (s,S) policy.

Theorem 1. For $n = 1 , 2 , . . . , N .$

(i) $G _ { n } ( y , w _ { n } )$ is A-convex in y for all $w _ { n } ,$ (ii) the optimal ordering policy is a state dependent $( s _ { n } ( w _ { n } ) , S _ { n } ( w _ { n } ) )$ policy where $S _ { n } ( w _ { n } )$ minimizes $G _ { n } ( y , w _ { n } )$ and $s _ { n } ( w _ { n } )$ is the smallest value of y for which $G _ { n } ( y , w _ { n } ) { = } A + G _ { n } ( S _ { n } ( w _ { n } ) , w _ { n } ) ,$

(iii) $C _ { n } ( I , z _ { n } )$ is A-convex in I for all $z _ { n }$ and it is minimized at $S _ { n } ( w _ { n } )$

Proof. Proof follows as in [2], and details are provided in [14]. □

In Theorem 1 we show that $G _ { n } ( y , w _ { n } )$ is A-convex in y and $C _ { n } { \left( I , z _ { n } \right) }$ is A-convex in I which are both minimized at $S _ { n } ( w _ { n } )$ . By the property of A-convexity, for $A = 0$ these functions are convex and hence the optimal policy is of state dependent order-up-to level type: if inventory level is below some $y _ { n } ( w _ { n } )$ , then order-up-to $y _ { n } ( w _ { n } )$ , otherwise do not order anything. These results are stated in the next corollary, which is needed for the succeeding sections.

Corollary 1. When $A = 0 ,$ we have the following properties for $n =$ $1 , 2 , . . . , N \colon$

(i) $G _ { n } ( y , w _ { n } )$ is convex in y. Let the minimum of ${ \bf \dot { G } } _ { n } ( y , w _ { n } )$ be attained $\tau y _ { n } ( w _ { n } ) ,$

(ii) $C _ { n } ( I , z _ { n } ) = C _ { n } ( I , q _ { n } , w _ { n } )$ is convex in I and it is minimized at $I { = }$ $y _ { n } ( w _ { n } ) ,$

(iii) the optimal ordering policy is of order-up-to type. The ordering quantity at the beginning of the period is $u _ { n } ( w _ { n } ) { = } m a x \{ y _ { n } ( w _ { n } ) - I , 0 \}$

## 3. Characterization of the optimal order-up-to levels when there is no <sup>fi</sup>xed ordering cost

In this section we provide structural results regarding the optimal policy when there is no <sup>fi</sup>xed ordering cost. In particular, we provide the full-characterization of order-up-to levels. We start by showing that order-up-to level of a period is not less than the demand of that period, which is stated in the next proposition.

Proposition 1. $y _ { n } ( w _ { n } ) { \geq } D _ { n } f o r a l l n { = } 1 , 2 { , } { \ldots } , N .$

Proof. The proof is provided in the Appendix A.

The rest of the section is organized as follows. In Section 3.1 we characterize the optimal order-up-to levels when supply is available in one of the periods in the ASI horizon, that is when $w _ { n } { = } \left( o _ { l } , r _ { M - l } \right)$ with $l { \in } \{ 0 , 1 , { \ldots } , M - 1 \}$ . In this case, order-up-to level for such an ASI state can be found easily and it is independent of the supply availability distribution. However when there is no supply period in the information horizon (that is, $w _ { n } = o _ { M } )$ ) the problem is more challenging. For this case, a simple exact algorithm is provided in Section 3.2 for <sup>fi</sup>nding the order-up-to levels.

## 3.1. Characterization when there is a supply period in the ASI horizon

In this subsection, we consider the case when there is at least one period with available supply in the ASI horizon. First we show that when supply is available in the next period, it is optimal to order up-to the demand of the current period, which is the minimum value for the order-up-to level. This result is stated in the following proposition.

Proposition 2. Let $w _ { n } = \left( o _ { l } , r _ { M - l } \right)$ for some $l { \in } \{ 0 , 1 , { \ldots } , M - 1 \}$ then $y _ { n } ( w _ { n } )$ is minimized at $l = 0 .$ . That is $y _ { n } ( r _ { M } ) = D _ { n } \leq y _ { n } ( w _ { n } ) ,$ , for any $w _ { n } { \in } \Omega _ { M } , \forall n { = } 1 , 2 , . . . , N .$

Proof. The proof is provided in the Appendix A.

When there is at least one supply period in the ASI horizon, the corresponding order-up-to level can be found easily and it does not depend on the supply availability distribution. Let us <sup>fi</sup>rst denote the sum of demands in periods n through $n { + j }$ as $D ( n , n + j )$ $\mathrm { i . e . } \ D ( n , n + j ) = D _ { n } + D _ { n + 1 } + \cdots + D _ { n + j }$ for a given integer $j { \geq } 0$

Proposition 3. Suppose $M { \ge } 2$ and let $w = \left( o _ { l } , r _ { M - l } \right)$ for some l ∈ {1,2, …, $M - 1 \}$ . Then there exists $K ( w ) \in \{ 1 , 2 , . . . , l + 1 \}$ such that $y _ { n } ( w ) =$ $D ( n , n + K ( w ) - 1 )$ . Moreover,

$$
K (w) = \left\{ \begin{array}{l l} 1 & \text {   if   } h \geq l b, \\ j & \text {   if   } h \in \left\{\frac {l - j + 1}{j} b, \frac {l - j + 2}{j - 1} b \right\} \\ l + 1 & \text {   if   } h <   \frac {1}{l} b. \end{array} \right. \quad j = 2,..., l,\tag{3}
$$

Proof. The proof is provided in the Appendix A.

Remark 1. For $M = 1$ and $l { = } 0 , \ K ( w ) { = } 1$ as already shown in Proposition 2.

Proposition 3 gives rise to the next corollary, which states that an order-up-to level monotonically increases as the <sup>fi</sup>rst period of supply availability gets further away in the ASI vector.

Corollary 2. For $n = 1 , 2 , . . . , N , \ y _ { n } ( o _ { l _ { 1 } } , r _ { M - l _ { 1 } } ) \leq y _ { n } ( o _ { l _ { 2 } } , r _ { M - l _ { 2 } } )$ for $l _ { 1 } < l _ { 2 } ,$ $l _ { i } { \in } \{ 1 , 2 , { \ldots } , M - 1 \} ( i { = } 1 , 2 )$

Proof. K(w) in Proposition 3 is non-decreasing in l, as can be seen from Eq. (3) (or from Eq. (A.2)). □

An order-up-to level reaches its maximum value when there is no supply period in the ASI horizon, since there will be no other ordering opportunity during the ASI horizon. This is stated in the next result.

Proposition 4. $y _ { n } ( w ) { \leq } y _ { n } ( o _ { M } )$ for any $w = \left( o _ { l } , r _ { M - l } \right)$ where $l { < } M ,$ and $n = 1 , 2 , . . . , N .$

Proof. The proof is provided in Appendix A.

□

3.2. Characterization when there is no supply period in the ASI horizon

As shown in Proposition 3, whenever w $\neq 0 _ { M } ,$ the order-up-to level of any period n can be written as $y _ { n } ( w ) { = } D ( n , n + K ( w ) - 1 )$ ). Note that $K ( w )$ does not depend on n. In what follows, we characterize the optimal order-up-to level of a period when $w = o _ { M } .$ To this end, we need another property of order-up-to levels, which is stated in Proposition 5: the order-up-to level of a period is not greater than the sum of that period's demand and the maximum order-up-to level of the next period.

Proposition 5. $y _ { n } ( w _ { n } ) { \leq } D _ { n } { + } y _ { n + 1 } ( o _ { M } )$ for all $w _ { n } { \in } \Omega _ { M } , n { = } 1 , 2 , . . . , N .$

Proof. The proof is provided in Appendix A.

Given that ${ z _ { n } } = ( q _ { n } , w _ { n } )$ , we de<sup>fi</sup>ne:

$$
R _ {w} (n) = \min \left\{k: k \in \{1, 2, \dots , N - n \}: Z _ {n + k} = (\infty , w) \right\}.
$$

If no such k exists, set $R _ { w } ( n ) = \infty$ . Note that $R _ { w } ( n )$ is the <sup>fi</sup>rst time after n a supply state $z = ( \infty , w )$ is observed, given that we start at the supply state ${ z _ { n } } = ( q _ { n } , w _ { n } )$ . In particular, whenever $w = o _ { M }$

$$
R _ {o _ {M}} (n) = \min \left\{k: k \in \{1, 2, \dots , N - n \}: Z _ {n + k} = (\infty , o _ {M}) \right\}.
$$

We also de<sup>fi</sup>ne for $i { = } 1 , 2 , . . . , N { - } n ,$

$$
\mathcal {P} _ {n} (i) = \operatorname * {P r} \left\{R _ {w} (n) > i, \forall w \in \Omega_ {M} \right\}\tag{4}
$$

and

$$
\mathcal {Q} _ {n} (i, j) = \operatorname * {P r} \left\{R _ {w} (n) > i, \forall w \in \Omega_ {M}, w \neq o _ {M}, K (w) \geq j - i + 1, \text {   and   } R _ {o _ {M}} > i \right\},\tag{5}
$$

for $i { = } 1 , 2 , { \ldots } , N { - } n$ and $j { = } 1 , 2 , { \ldots } , K ( w ) . \ K ( w )$ in $\operatorname { E q . } \left( 5 \right)$ is de<sup>fi</sup>ned in Propositions 2 and 3. Intuitively, $\mathcal { P } _ { n } ( i )$ is the probability that supply <sup>P ð Þ</sup>does not become available for the periods $n + 1 , . . . , n + i$ (the <sup>fi</sup>rst supply period is after period $n { \mathrel { + { i } } } )$ . On the other hand, $\mathcal { Q } _ { n } ( i , j )$ is the probability that the inventory level cannot be raised to the optimal order-up-to level in periods $n + 1 , . . . , n + i$ whenever the starting inventory at the beginning of period n is $D ( n , n + j )$ . The following proposition is the central result of this section, where we show that once the optimal order-up-to level of period $n + 1$ is known, the optimality condition for period n can be obtained.

Proposition 6. Assume that $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , n + J )$ (J-period demand) for some $n { \in } \{ 1 , 2 , { \ldots } N - 1 \}$ and $1 { \le } J { \le } N - n$ . Then, $f o r j = 1 , 2 , . . . , J ,$

$$
G _ {n} (D (n, n + j), o _ {M}) \leq G _ {n} (D (n, n + j) - \eta , o _ {M}) \forall 0 \leq \eta \leq D _ {n + j}
$$

if and only if

$$
\frac {\sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)}{1 + \sum_ {i = 1} ^ {j - 1} \mathcal {Q} _ {n} (i , j) + \sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)} \geq \frac {h}{h + b},\tag{6}
$$

where

$$
\mathcal {P} _ {n} (i) = \left\{ \begin{array}{l l} 1 & \text { if } \quad i <   M + 1 \\ \prod_ {k = M + 1} ^ {i} \left(1 - p _ {n + k}\right) & \text { if } \quad i \geq M + 1. \end{array} \right.
$$

Proof. The proof is provided in the Appendix A.

Proposition 6 will be utilized in the following manner: Since $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , N + J )$ , we know that $y _ { n } ( o _ { M } ) { \leq } D _ { n } + D ( n + 1 , n + J )$ As Eq. (6) does not depend on $\eta , y _ { n } ( o _ { M } )$ is equal to one of the values $\{ D _ { n } , D ( n , n + 1 ) , . . . , D ( n , n + J ) \}$ . Moreover, convexity of $G _ { n } ( y , o _ { M } )$ , together with Eq. (6) immediately yields the optimal value of $y _ { n } ( o _ { M } )$ (see Theorem 2). The only term which is not given in an explicit form in Proposition 6 is $\mathcal { Q } _ { n } ( i , j )$ . This probability can be obtained in a recursive manner using the <sup>fi</sup>rst hitting time probabilities of an appropriately constructed non-stationary Markov chain. The details are provided in Appendix A.

## 3.3. Computation of the optimal order-up-to levels

We conclude this section by presenting a simple computational method for the optimal order-up-to levels at a given ASI state. Notice that the inequality $\operatorname { E q . }$ (6) in Proposition 6 does not depend on the demand sequence, but only depends on the supply uncertainty structure and the cost parameters. Also note that for w $\prime \neq 0 _ { M }$ , the optimal order-up-to levels can be expressed as $K ( w )$ -period cumulative demand. Moreover, Proposition 6 guarantees that an optimal orderup-to level corresponding to $w = o _ { M }$ occurs in one of the cumulative demand points, as long as the same is true for the succeeding period. That ${ \mathrm { i } } s ,$ if there is a cost bene<sup>fi</sup>t of increasing (decreasing) the orderup-to level a small amount $\eta ,$ it should be increased (decreased) up to the next cumulative demand point. We summarize our <sup>fi</sup>ndings in the following Theorem.

Theorem 2. The optimal order-up-to level for period $\pm \smash { n \in \{ 1 , 2 , . . . , N \} }$ is equal $t o \ J _ { n }$ period demand, $D ( n , n + J _ { n } - 1 )$ , for some $1 \leq J _ { n } \leq N - n + 1$ with $J _ { N } = 1$ . Given that $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , n + J )$ for some 1≤ J≤ $N - n + 1$ and $\imath = N - 1 , N - 2 , . . . , 1 ,$ , it holds that $y _ { n } ( o _ { M } ) = D ( n , n + J ^ { \prime } )$ where

$$
J ^ {\prime} = \max \left\{j = 1, 2,..., J: \frac {\sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)}{1 + \sum_ {i = 1} ^ {j - 1} \mathcal {Q} _ {n} (i , j) + \sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)} \geq \frac {h}{h + b} \right\},\tag{7}
$$

If no such J′ exists, then $J ^ { \prime } { = } 0 $

## Proof. The proof is provided in Appendix A.

Combining the characterization of the order-up-to levels for different types of ASI vectors, we can <sup>fi</sup>nd the optimal order-up-to levels for any given ASI vector. When the next period is a supply period, optimal ordering decision is to order up-to current demand as stated in Proposition 2. When there is at least one supply period in the ASI horizon we can <sup>fi</sup>nd the optimal order-up-to levels with the help of Proposition 3. Finally when there is no supply period in the ASI horizon order-up-to levels are determined by the algorithm given as Algorithm A, which follows from Theorem 2. Note that the characterization (obviously not the amounts) of optimal order-up-to levels (in terms of the number of demand periods to be covered) does not depend on the speci<sup>fi</sup>c values of demands, as an optimal order-upto level can be simply written as a cumulative demand point.

Algorithm A

$$
\begin{array}{l l} \text {Step 0.} & J = 1 (y _ {N} (o _ {M}) = D _ {N}) \\ \text {Step 1.} & \text {For n = N - 1 to 1, find J ^ {\prime} satisfying Eq. (7).} \\ & \text {Set y_{n} (o_{M}) = D(n,n+ J^{\prime}) and J = J^{\prime} + 1}. \\ & \text {If no such J ^ {\prime} exists, set y_{n} (o_{M}) = D_{n} and J = 1.} \end{array}
$$

## 3.4. Infinite horizon model under stationary supply uncertainty

We conclude Section 3 by presenting an in<sup>fi</sup>nite horizon extension of our model. Let $\alpha \in ( 0 , 1 )$ be the discount factor, and assume that the supply availability probabilities are stationary over time. That is, ${ { p } _ { n } } = p$ for all $n = 1 , 2 , \ldots$ . Then, the dynamic programming recursion becomes:

$$
C _ {n} (I, z _ {n}) = \min _ {I \leq y \leq I + q _ {n}} \left\{L _ {n} (y) + \alpha E \left[ C _ {n + 1} \left(y - D _ {n}, w _ {n}, Q _ {n + M + 1}\right) \right] \right\}.
$$

Provided that $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , n + J )$ for some $n { = } 1 , 2 , { \ldots } , N { - } n ,$ and $J = 1 , 2 , . . . , N - n$ , we can show that (by following similar steps in Proposition 6)

$$
G _ {n} (D (n, n + j), o _ {M}) \leq G _ {n} (D (n, n + j) - \eta , o _ {M}) \forall 0 \leq \eta \leq D _ {n + j}
$$

if and only if

$$
\frac {\sum_ {i = j} ^ {N - n} \alpha^ {i} \mathcal {P} (i)}{1 + \sum_ {i = 1} ^ {j - 1} \alpha^ {i} \mathcal {Q} (i , j) + \sum_ {i = j} ^ {N - n} \alpha^ {i} \mathcal {P} (i)} \geq \frac {h}{h + b},\tag{8}
$$

$\mathrm { f o r } j = 1 , 2 , . . . , J .$ . Note that $\mathcal { P } ( i )$ and $\mathcal { Q } ( i , j )$ in Eq. (8) do not depend on n. <sup>Pð Þ Qð</sup>Moreover, it can also be shown that $y _ { n } ( o _ { M } ) = D ( n , n + J )$ if the inequality in Eq. (8) holds. Otherwise, $y _ { n } ( o _ { M } ) = D ( n , n + J - 1 )$ . Intuitively, since the supply availability probabilities are stationary, if the order-up-to level for period $n + 1$ covers the demand over J periods, the order-up-to level for period n should cover the demand for no less than J periods whenever the same ASI vector $o _ { M }$ is observed in periods n and $n + 1$ . Now, we let the number of periods in the planning horizon to be in<sup>fi</sup>nity: $N \to \infty$ . Consider two consecutive periods n and $n + 1 .$ . Suppose that $y _ { n } ( o _ { M } ) = D ( n , n + J - 1 )$ and $y _ { n + 1 } ( o _ { M } ) =$ $D ( n + 1 , n + J )$ . That is, periods n and $n + 1$ have the same orderup-to levels (in terms of the number of demand periods covered). Essentially, this happens if the reverse inequality holds in Eq. (8). Then, any period kbn should also have the same demand coverage: $y _ { k } ( o _ { M } ) = D ( k , k + J - 1 )$ , since the left hand side of Eq. (8) does not depend on n as $N \to \infty .$ This observation leads to the following result regarding the optimal order-up-to level of the stationary problem: Let $J _ { \infty }$ be the smallest integer $J { \in } \{ 1 , 2 , \ldots \}$ satisfying

$$
\frac {\sum_ {i = J} ^ {\infty} \alpha^ {i} \mathcal {P} (i)}{1 + \sum_ {i = 1} ^ {J - 1} \alpha^ {i} \mathcal {Q} (i , J) + \sum_ {i = J} ^ {\infty} \alpha^ {i} \mathcal {P} (i)} <   \frac {h}{h + b}.\tag{9}
$$

The order-up-to level for period n is given by $y _ { n } ( o _ { M } ) = D ( n , n + J _ { \infty } - 1 )$ It is straightforward to show that

$$
\sum_ {i = J} ^ {\infty} \alpha^ {i} \mathcal {P} (i) = \left\{ \begin{array}{c c} \frac {\alpha^ {J} - \alpha^ {M + 1}}{1 - \alpha} + \frac {\alpha^ {M + 1} (1 - p)}{1 - \alpha (1 - p)} & \text {if} J \leq M \\ \frac {\alpha^ {J} (1 - p) ^ {J - M}}{1 - \alpha (1 - p)} & \text {if} J \geq M + 1 \end{array} \right..
$$

No such closed form expression for $Q ( i , J )$ exists, with the exception of the special case $M = 1$ (only one-period ahead ASI is used). In this case $Q ( i , J ) = ( 1 - p ) ^ { i - 1 } { \mathrm { f o r } } i = 1 , 2 , . . . , J - 1$ and Eq. (9) simpli<sup>fi</sup>es to

$$
\frac {\alpha^ {J} (1 - p) ^ {J - 1}}{1 + \alpha p} <   \frac {h}{h + b}.\tag{10}
$$

Therefore, $J _ { \infty }$ is simply the minimum $J { \in } \{ 1 , 2 , \ldots \}$ satisfying Eq. (10).

## 4. A heuristic solution when there is non-zero <sup>fi</sup>xed ordering cost

If the <sup>fi</sup>xed ordering cost is non-zero and with the ASI horizon (M) is large, the dynamic programming approach for <sup>fi</sup>nding the optimal inventory policy $( ( s ( w ) , S ( w ) )$ pairs) is computationally intractable with a complexity of $0 ( N ^ { 2 } 2 ^ { M } \bar { D } _ { \operatorname* { m a x } } )$ , where $D _ { \mathrm { m a x } }$ is the maximum demand value in the planning horizon. Therefore in this section we propose a heuristic for <sup>fi</sup>nding a good ordering strategy in a reasonably short time.

The suggested heuristic is a forward method, like Silver–Meal Heuristic $( [ 2 0 ] )$ , which requires determining the average cost per period as a function of the number of periods the current order is to span. The number of periods to span is increased until the average cost per period starts increasing. Because of the stochastic nature of supply availability, we need to consider the expected backorder costs in addition to the holding and set-up costs of the classical Silver–Meal Heuristic. Moreover, we have supply availability information for a number of periods so we also need to incorporate this information into the method.

Suppose that at the beginning of period n the on hand inventory is equal to $D ( n , n + n ^ { + } - 1 )$ , for $n ^ { + } \in \{ 0 , 1 , . . . , N - n + 1 \}$ , where $D ( n ,$ $n - 1 ) { : = } 0 .$ . This essentially means that we have suf<sup>fi</sup>cient stock for $n ^ { + }$ periods. Let B be the amount of backorders $( B = 0 \mathrm { i f } n ^ { + } \geq 1 )$ . Let ${ z _ { n } } = ( q _ { n } , w _ { n } )$ be the current ASI state, and recall the decomposition $w _ { n } = ( o _ { l } , r _ { M - l } ) . \mathrm { ~ I f ~ } q _ { n } = i n f t y$ then we can place an order, and suppose that we place an order to raise the inventory up-to $D ( n , T )$ Obviously $T { \ge } n { + } n ^ { + } - 1$ , with $T = n + n ^ { + } - 1$ corresponding to not ordering anything. Let $C _ { n } ( T )$ be the average expected cost per period for ordering up-to $D ( n , T )$ , where averaging is performed over the effective duration for which $D ( n , T )$ is expected to cover the system demand. Even though $C _ { n } ( T )$ depends on $w _ { n }$ and B (but not the on on-hand inventory) we suppress this dependency in the notation for sake of brevity. We compute $C _ { n } ( T )$ for $T { \geq } n + n ^ { + }$ (where B is cleared by ordering up-to a positive amount) until $C _ { n } ( T + 1 ) >$ $C _ { n } ( T )$ , and record the minimizer $T _ { a } { = } \mathrm { a r g m i n } C _ { n } ( T )$ . Then we compute $C _ { n } ( T )$ for $T = n + n ^ { + } - 1$ , and conclude that the best T is $T ^ { * } =$ $T _ { a }$ if $C _ { n } \big ( T _ { a } \big ) < C _ { n } \big ( n + n ^ { + } - 1 \big )$ ), and set $T ^ { * } = n + n ^ { + } - 1$ otherwise.

In what follows we present how we develop $C _ { n } ( T )$ for $T { < } n { + } M$ and for a particular form of $w _ { n } .$ . The other case, $T { \ge } n + M ,$ or other structures of $w _ { n }$ are handled in the same spirit and omitted here. For the case $T { < } n { + } M ,$ , we order up-to $D ( n , T )$ . In this case, we have supply availability information beyond the periods that this order covers, that is, for periods $T + 1 , . . . , T + M .$ . Let $\nu = n + M - T .$ . Let $\tilde { w } _ { n }$ be the last v entries of $w _ { n \cdot }$ Then, $\tilde { w } _ { n }$ is the ASI that we have for the periods $T + 1 , . . . , T + M$ . Following our standard notation, we can write $\tilde { w } _ { n } = ( \tilde { o } _ { l } , \tilde { r } _ { \nu - l } )$ . Consider the case $\scriptstyle 0 < l < \nu : \tilde { w } _ { n }$ starts with zero, but includes at least one supply period. In this case, the total holding cost incurred is: $h \sum _ { i = 1 } ^ { T - n } i D _ { n + i } .$ . The system backorders demands of periods $D _ { T + 1 } , . . . , D _ { T + }$ and has an ordering opportunity at the beginning of period $T + l + 1$ (as given by $\tilde { w } _ { n } )$ . The total backordering cost incurred until this ordering opportunity is: $\begin{array} { r } { b \sum _ { i = 1 } ^ { l } ( l - i + 1 ) D _ { T + i } . } \end{array}$ Consequently, $D ( n , T )$ has an affect on periods $n , n + 1 , . . . , T + l .$ Therefore,

$$
C _ {n} (T) = \frac {A + h \sum_ {i = 1} ^ {T - n} i D _ {n + i} + b \sum_ {i = 1} ^ {l} (l - i + 1) D _ {T + i}}{T + l - n + 1}.
$$

For instance, if $\tilde { w } _ { n } = ( \tilde { o } _ { l } , \tilde { r } _ { \nu - l } )$ is such that $\nu - l = 0 ( \tilde { w } _ { n }$ consists of all zeros), then we need to consider expected backorder costs that might be incurred beyond the information horizon, in addition to the backorder costs that are to be certainly incurred.

Accordingly, Algorithm B can be used for executing the heuristic that we propose.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm B
Set I=0, TotalCost=0,  $n^{+}=0$ , B=0
Observe the supply availability information  $z_{1}=(q_{1},w_{1})$ 
for n=1 to N
    if  $q_{n}=\infty$  then
    find  $T^{*}$  as outlined above
    if  $I&lt;D(n,T^{*})$  then
    set  $I=D(n,T^{*})$ ,  $n^{+}=T^{*}-n+1$ 
    set TotalCost=TotalCost+A
    end
    end
    set  $I=I-D_{n}$ 
    set  $B=\max(0,-I)$ 
    set  $n^{+}=\max(0,n^{+}-1)$ 
    TotalCost=TotalCost+h max(0,I)+b max(0,-I)
    Observe supply availability information for period  $n+M+1$ 
    update supply availability information vector
end
</div>

To assess the performance of the heuristic, optimal solution and heuristic results are compared for a number of problem instances. As the performance criteria, percent deviation from the optimal value is used.

Our model assumes deterministic demand and we generated demand values by discretizing Gamma distribution. We use Gamma distribution for the sake of obtaining non-negative demand and generating demand values with different coef<sup>fi</sup>cient of variation values. We used 9 Gamma distributions having 3 different means $( \mu : \mu _ { 1 } , \mu _ { 2 } , \mu _ { 3 } )$ and 3 different coef<sup>fi</sup>cient of variation $( c \nu ; c \nu _ { 1 } , c \nu _ { 2 } , c \nu _ { 3 } )$ values, which can be seen in Table 1. For each of the given demand distributions, 100 different demand sets (that is, demand values for a planning horizon of 12 periods) are generated randomly. For each demand set, a million replications are taken to reduce variation. In Table 2 we present some results with 2-period ASI (that is, M=1). Supply availability is assumed to be stationary with 3 levels: 0.1, 0.5, and 0.9. Holding cost is <sup>fi</sup>xed at h=1, and b=5 and b=10 are used for backorder cost. Fixed ordering cost is taken as a multiple of backorder cost, assuming the values of 5b and 10b. We report the% average deviation (%av) of 100 demand sets that are generated for each demand distribution. In addition we report the standard deviation of %av (σ).

Analyzing the results in Table 2 we can make some observations. In general %av and σ are higher when cv is higher. The intuition is, when there is non-zero <sup>fi</sup>xed ordering cost the optimal policy depends on the demand pattern and it is more dif<sup>fi</sup>cult for the heuristic to capture the optimal order-up-to levels when there is high variation in the demand. Heuristic method performs best for low availability case $( p { = } 0 . 1 )$ . The optimal ordering decision, which is also mimicked by heuristic method, is to place a big amount of order that covers the demand of a several number of periods for such a low availability. For low availability case $( p { = } 0 . 1 )$ , heuristic algorithm has an average %av deviation of 0.8%. For moderate $( p = 0 . 5 )$ and high availability cases (p=0.9) this deviation is 5.6% and 3.2% respectively. Note that moderate availability case has the biggest variability in terms of the supply availability and therefore heuristic algorithm performs better in low and high availability cases.

Parameters of the demand distributions.

<table><tr><td> $\mu_1$ </td><td>5</td><td> $cv_1$ </td><td>0.1</td></tr><tr><td> $\mu_2$ </td><td>10</td><td> $cv_2$ </td><td>0.5</td></tr><tr><td> $\mu_3$ </td><td>15</td><td> $cv_3$ </td><td>1</td></tr></table>

Table 2  
Performance of the heuristic algorithm.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3"> $CV_1$ </td><td colspan="3"> $CV_2$ </td><td colspan="3"> $CV_3$ </td></tr><tr><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td></tr><tr><td colspan="11"> $p=0.1$ </td></tr><tr><td>b=5</td><td>%av</td><td>0.71</td><td>0.83</td><td>0.83</td><td>0.67</td><td>0.75</td><td>0.86</td><td>2.11</td><td>1.69</td><td>1.39</td></tr><tr><td>A=25</td><td>σ</td><td>0.22</td><td>0.24</td><td>0.22</td><td>0.30</td><td>0.35</td><td>0.37</td><td>2.42</td><td>1.90</td><td>1.48</td></tr><tr><td>b=5</td><td>%av</td><td>0.72</td><td>0.71</td><td>0.77</td><td>0.63</td><td>0.61</td><td>0.69</td><td>2.10</td><td>1.60</td><td>1.29</td></tr><tr><td>A=50</td><td>σ</td><td>0.20</td><td>0.24</td><td>0.23</td><td>0.27</td><td>0.32</td><td>0.33</td><td>2.42</td><td>1.91</td><td>1.46</td></tr><tr><td>b=10</td><td>%av</td><td>0.09</td><td>0.10</td><td>0.14</td><td>0.13</td><td>0.17</td><td>0.17</td><td>2.14</td><td>1.39</td><td>1.07</td></tr><tr><td>A=50</td><td>σ</td><td>0.06</td><td>0.05</td><td>0.06</td><td>0.10</td><td>0.12</td><td>0.10</td><td>3.14</td><td>2.31</td><td>1.73</td></tr><tr><td>b=10</td><td>%av</td><td>0.24</td><td>0.15</td><td>0.17</td><td>0.23</td><td>0.18</td><td>0.19</td><td>2.26</td><td>1.42</td><td>1.07</td></tr><tr><td>A=100</td><td>σ</td><td>0.13</td><td>0.11</td><td>0.12</td><td>0.14</td><td>0.14</td><td>0.14</td><td>3.14</td><td>2.35</td><td>1.73</td></tr><tr><td colspan="11"> $p=0.5$ </td></tr><tr><td>b=5</td><td>%av</td><td>0.47</td><td>2.12</td><td>1.25</td><td>2.41</td><td>5.24</td><td>5.95</td><td>4.09</td><td>5.15</td><td>5.47</td></tr><tr><td>A=25</td><td>σ</td><td>0.40</td><td>0.30</td><td>0.99</td><td>1.39</td><td>1.96</td><td>2.12</td><td>2.75</td><td>2.48</td><td>2.78</td></tr><tr><td>b=5</td><td>%av</td><td>1.85</td><td>0.25</td><td>3.14</td><td>1.77</td><td>2.55</td><td>3.75</td><td>3.29</td><td>4.12</td><td>4.23</td></tr><tr><td>A=50</td><td>σ</td><td>0.69</td><td>0.31</td><td>0.44</td><td>1.00</td><td>1.42</td><td>1.57</td><td>2.58</td><td>2.08</td><td>2.24</td></tr><tr><td>b=10</td><td>%av</td><td>2.68</td><td>6.87</td><td>6.15</td><td>6.12</td><td>10.45</td><td>12.22</td><td>11.00</td><td>13.32</td><td>14.47</td></tr><tr><td>A=50</td><td>σ</td><td>1.11</td><td>0.52</td><td>0.38</td><td>3.09</td><td>3.63</td><td>4.01</td><td>6.88</td><td>5.36</td><td>5.99</td></tr><tr><td>b=10</td><td>%av</td><td>2.72</td><td>2.47</td><td>4.03</td><td>4.53</td><td>6.81</td><td>8.41</td><td>9.85</td><td>11.63</td><td>11.72</td></tr><tr><td>A=100</td><td>σ</td><td>0.83</td><td>0.95</td><td>0.89</td><td>2.90</td><td>3.27</td><td>3.00</td><td>5.52</td><td>5.38</td><td>4.83</td></tr><tr><td colspan="11"> $p=0.9$ </td></tr><tr><td>b=5</td><td>%av</td><td>0.85</td><td>1.53</td><td>1.09</td><td>2.33</td><td>3.19</td><td>3.63</td><td>3.61</td><td>3.76</td><td>5.13</td></tr><tr><td>A=25</td><td>σ</td><td>1.02</td><td>1.22</td><td>1.01</td><td>2.58</td><td>2.44</td><td>2.44</td><td>3.56</td><td>3.50</td><td>3.78</td></tr><tr><td>b=5</td><td>%av</td><td>5.23</td><td>1.52</td><td>0.79</td><td>2.86</td><td>2.21</td><td>2.75</td><td>3.33</td><td>2.78</td><td>4.29</td></tr><tr><td>A=50</td><td>σ</td><td>3.96</td><td>1.61</td><td>0.41</td><td>3.06</td><td>2.32</td><td>2.75</td><td>3.90</td><td>3.02</td><td>3.66</td></tr><tr><td>b=10</td><td>%av</td><td>3.22</td><td>2.51</td><td>0.51</td><td>3.16</td><td>3.93</td><td>5.72</td><td>4.47</td><td>6.04</td><td>7.96</td></tr><tr><td>A=50</td><td>σ</td><td>1.83</td><td>1.62</td><td>0.45</td><td>3.28</td><td>3.73</td><td>4.01</td><td>5.19</td><td>5.22</td><td>4.96</td></tr><tr><td>b=10</td><td>%av</td><td>0.67</td><td>3.10</td><td>0.22</td><td>2.88</td><td>2.91</td><td>2.58</td><td>3.62</td><td>4.39</td><td>5.36</td></tr><tr><td>A=100</td><td>σ</td><td>0.90</td><td>2.01</td><td>0.27</td><td>4.25</td><td>3.40</td><td>2.92</td><td>4.69</td><td>4.04</td><td>5.09</td></tr></table>

Finally it is important to mention the advantage of the heuristic algorithm in terms of computational time. The heuristic algorithm has a polynomial computation time with an order of $O ( N ^ { 2 } )$ compared to the dynamic programming which has a non-polynomial computation time with an order of complexity of $O ( N ^ { 2 } 2 ^ { M } D _ { \mathrm { m a x } } )$

## 5. Numerical analysis

In this section we present the results of our numerical experi ments. Parameter settings used are the same with that in Section 4. We <sup>fi</sup>rst state our observations as to the optimal policy under different parameter settings: For 2-period ASI (that $\mathrm { i } s , M = 1 )$ an important observation is that $S _ { n } ( 0 ) { \geq } S _ { n } ( \infty )$ and $S _ { n } ( 0 ) { \geq } S _ { n } ( \infty )$ . For the same backorder cost and same level of the supply availability, order-up-to levels monotonically increase and re-order points monotonically decrease in <sup>fi</sup>xed ordering cost. Intuitively, when there is high <sup>fi</sup>xed ordering cost the model becomes reluctant to order frequently and whenever an order is placed the amount ordered becomes higher due to economies of scale. We also observe that total expected cost increases as supply availability decreases, as expected.

Next, we study the value of information (VOI) aspect of ASI. We consider various factors. Firstly, the effect of the length of ASI horizon is investigated. The value of an additional period's supply information is referred to as the marginal %VOI. We denote the marginal %VOI of 2-period ASI (M=1) by %VOI<sub>0 1</sub> which gives the additional value resulting from 2-period ASI. Similarly, the marginal %VOI of 3-period ASI (M= 2) and 4-period ASI (M= 3) are denoted by $\% \mathrm { { V O I } } _ { 1 - 2 }$ and $\% \mathrm { { V O I } } _ { 2 - 3 } ,$ respectively. To <sup>fi</sup>nd the marginal %VOI, we use Eq. (11):

$$
\% \mathrm{VOI} _ {i - j} = \frac {\text { Cost   for } (M = i) - \text { Cost   for } (M = j)}{\text { Cost   for } (M = i)} * 1 0 0,\tag{11}
$$

where the term ‘Cost’ refers to the total expected cost in the system. In addition to %VOI, absolute VOI is also analyzed and it is calculated as in Eq. (12):

$$
\operatorname{VOI} _ {i - j} = \text { Cost   for } (M = i) - \text { Cost   for } (M = j).\tag{12}
$$

## 5.1. Investigation of VOI when there is no fixed ordering cost

In this subsection, VOI is analyzed when there is no <sup>fi</sup>xed ordering cost, that is A=0. The two other cost parameters are set as $h = 1$ and $b = 5 ,$ . Marginal %VOI and absolute VOI for the cases with no ASI, 2-period ASI, 3-period ASI, and 4-period ASI are presented in Table 3. We make various observations for the selected setting:

• %VOI increases as the supply availability probability increases from 0.1 to 0.9. When there is low supply availability in the system, large quantities are ordered and hence ASI does not play a key role. On the other hand, when there is high supply availability, orders are placed more frequently which facilitates better usage of ASI in decision making in the sense that the system without ASI faces the risk of having no stock and backordering all the demand when the unlikely event of supply unavailability occurs, while the presence of ASI prevents those prospective backorder costs. Consequently, %VOI is high in this setting although unavailability probability is low, because backorder costs constitute a large portion of the total expected cost.

• The variability in supply availability is the highest when availability probability is 0.5. Therefore absolute VOI is higher in this case compared to the other two cases.

• There is a diminishing rate of return of ASI for medium and high availability of supply, both for marginal %VOI and absolute VOI. When there is high supply availability, the most valuable information is the availability of the immediate next period's supply, as a large amount of backorder might be avoided. On the other hand, when there is low availability, ASI regarding a longer time interval is relatively more useful, as it becomes more likely to avoid a large order.

## 5.2. The effect of fixed ordering cost

In what follows we consider the effect of <sup>fi</sup>xed ordering cost and different parameter settings on %VOI. The results are summarized in Fig. 1 for 2-period ASI and b=5. Main observations regarding the selected parameter settings can be listed as follows:

• For the same backorder cost and for the same demand distribution, %VOI decreases as the <sup>fi</sup>xed ordering cost increases. %VOI is the highest when there are no <sup>fi</sup>xed costs, for all supply availability levels. This is because the supply availability of the future periods becomes less important in the ordering decision as <sup>fi</sup>xed ordering cost increases: orders are placed in large quantities regardless of the supply availability to avoid the ordering costs. Same observations are valid for the absolute VOI.

• When <sup>fi</sup>xed ordering cost is positive, the optimal policy becomes dependent on the demand pattern. As the average demand and the variability of demand increase, the effect of an over-stocking (or under-stocking) decision on the system cost becomes more prevalent. Therefore, %VOI increases as the variability (cv) and the size (μ) of the demand increase.

## 5.3. Effect of non-stationary supply availability

We conduct a numerical experiment to study the effects of nonstationary supply availability and ASI on the optimal ordering decision and the value of ASI. We considered different forms of nonstationarity to re<sup>fl</sup>ect various cases of supply availability in real life, such as a seasonal structure re<sup>fl</sup>ecting time dependence where supply is scarce in some periods (for example, summer) and mostly available (“abundant”) in some other periods, a cyclical structure re<sup>fl</sup>ecting state-of-the-world dependence such as the economical state where periods of scarcity are followed by periods of abundance, an alternating structure re<sup>fl</sup>ecting instability where each scarce supply period is followed by an abundant one, etc. We also considered stationary high availability and stationary low availability cases to re<sup>fl</sup>ect the known high or low reliability of the supplier. Moreover, we considered different demand patterns, such as cyclical demand, seasonal demand (for example, Christmas sales), increasing demand, decreasing demand, and stationary demand, keeping the average demand unchanged over all periods, for a fair comparison.

VOI for 3 levels of availability.

<table><tr><td rowspan="2"></td><td colspan="3"> $CV_1$ </td><td colspan="3"> $CV_2$ </td><td colspan="3"> $CV_3$ </td></tr><tr><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td><td> $\mu_1$ </td><td> $\mu_2$ </td><td> $\mu_3$ </td></tr><tr><td colspan="10">p=0.1</td></tr><tr><td> $\%VOI_{0-1}$ </td><td>0.240</td><td>0.240</td><td>0.240</td><td>0.237</td><td>0.238</td><td>0.237</td><td>0.244</td><td>0.241</td><td>0.230</td></tr><tr><td> $\%VOI_{1-2}$ </td><td>0.396</td><td>0.396</td><td>0.396</td><td>0.391</td><td>0.393</td><td>0.390</td><td>0.404</td><td>0.395</td><td>0.378</td></tr><tr><td> $\%VOI_{2-3}$ </td><td>0.444</td><td>0.444</td><td>0.444</td><td>0.438</td><td>0.439</td><td>0.438</td><td>0.457</td><td>0.439</td><td>0.422</td></tr><tr><td> $VOI_{0-1}$ </td><td>2.29</td><td>4.55</td><td>6.80</td><td>2.28</td><td>4.68</td><td>6.65</td><td>2.24</td><td>4.39</td><td>7.19</td></tr><tr><td> $VOI_{1-2}$ </td><td>3.76</td><td>7.48</td><td>11.19</td><td>3.74</td><td>7.70</td><td>10.93</td><td>3.70</td><td>7.18</td><td>11.77</td></tr><tr><td> $VOI_{2-3}$ </td><td>4.20</td><td>8.35</td><td>12.49</td><td>4.18</td><td>8.58</td><td>12.21</td><td>4.18</td><td>7.96</td><td>13.08</td></tr><tr><td colspan="10">p=0.5</td></tr><tr><td> $\%VOI_{0-1}$ </td><td>16.25</td><td>16.20</td><td>16.19</td><td>16.00</td><td>16.12</td><td>16.02</td><td>16.18</td><td>16.50</td><td>15.83</td></tr><tr><td> $\%VOI_{1-2}$ </td><td>15.86</td><td>15.83</td><td>15.79</td><td>15.57</td><td>15.67</td><td>15.53</td><td>15.74</td><td>16.07</td><td>15.20</td></tr><tr><td> $\%VOI_{2-3}$ </td><td>8.65</td><td>8.64</td><td>8.61</td><td>8.44</td><td>8.54</td><td>8.46</td><td>8.54</td><td>8.72</td><td>8.13</td></tr><tr><td> $VOI_{0-1}$ </td><td>25.75</td><td>51.15</td><td>76.47</td><td>25.64</td><td>52.83</td><td>74.89</td><td>24.85</td><td>49.96</td><td>81.80</td></tr><tr><td> $VOI_{1-2}$ </td><td>21.04</td><td>41.88</td><td>62.51</td><td>20.96</td><td>43.08</td><td>60.94</td><td>20.26</td><td>40.62</td><td>66.11</td></tr><tr><td> $VOI_{2-3}$ </td><td>9.66</td><td>19.24</td><td>28.71</td><td>9.59</td><td>19.80</td><td>28.04</td><td>9.27</td><td>18.50</td><td>29.98</td></tr><tr><td colspan="10">p=0.9</td></tr><tr><td> $\%VOI_{0-1}$ </td><td>67.56</td><td>67.42</td><td>67.37</td><td>66.85</td><td>67.28</td><td>67.22</td><td>67.42</td><td>67.92</td><td>66.56</td></tr><tr><td> $\%VOI_{1-2}$ </td><td>14.69</td><td>14.62</td><td>14.59</td><td>14.31</td><td>14.49</td><td>14.36</td><td>14.59</td><td>15.03</td><td>14.05</td></tr><tr><td> $\%VOI_{2-3}$ </td><td>1.10</td><td>1.10</td><td>1.09</td><td>1.07</td><td>1.08</td><td>1.08</td><td>1.09</td><td>1.12</td><td>1.03</td></tr><tr><td> $VOI_{0-1}$ </td><td>22.39</td><td>44.44</td><td>66.43</td><td>22.24</td><td>45.99</td><td>65.40</td><td>21.57</td><td>43.29</td><td>71.17</td></tr><tr><td> $VOI_{1-2}$ </td><td>1.58</td><td>3.14</td><td>4.70</td><td>1.58</td><td>3.24</td><td>4.58</td><td>1.52</td><td>3.07</td><td>5.02</td></tr><tr><td> $VOI_{2-3}$ </td><td>0.10</td><td>0.20</td><td>0.30</td><td>0.10</td><td>0.21</td><td>0.29</td><td>0.10</td><td>0.19</td><td>0.32</td></tr></table>

% VOI - low availability  
![](/api/attachments/XRRHSWKX/fulltext/images/d2e92a28bd66193756a9598d1bbfb36947ac5547e380ec07583b8acbeea49fcd.jpg)  
Fig. 1. %VOI for b=5.

We worked with a 4-period problem where the demand patterns and supply availability probability patterns as presented in Tables 4 and 5, respectively. To be able to analyze the effect of ASI, 3-period ASI, 2-period ASI and no ASI are considered. Cost parameters are h=1, b=5, A=0 and 20.

The order-up-to levels of the experiment for the <sup>fi</sup>rst period in the horizon are presented in Table 6. For ease of exposition, order-up-to levels are given as the cumulative demand of corresponding number of periods such that level of 1 corresponds to one-period demand, and same convention holds for other values. We also report %VOI , that is the relative value of having a 3-period ASI compared to no ASI. When A=0, we obtained the same number of demand periods to be covered for all demand patterns within a particular scenario, which we restrain from repeating in Table 6. We make the following observations:

• In the absence of <sup>fi</sup>xed costs, the optimal policy is insensitive to the non-stationarity of demand. This does not necessarily hold when there exists a <sup>fi</sup>xed cost of ordering, which makes it more dif<sup>fi</sup>cult to manage the system. However, the availability of ASI diminishes the impact of the demand pattern on the optimal policy. Consequently, ASI does not only make the system less costly to operate, but it also makes it more robust in terms of dependency on the demand pattern.

• The optimal order quantity is sensitive to the supply availability structure when there is no or little information on this availability. More information into future supply availability makes the system more robust in terms of dependency on the supply availability pattern, as it practically replaces this pattern.

• ASI that signals an upcoming supply period decreases the system's desire to stock against supply scarcity. Accordingly, ASI decreases the inventory-related costs in the system, especially when it signals the unlikely supply state, resulting in a higher value of ASI in those cases. Similarly, ASI that signals an upcoming supply scarcity elevates the order-up-to levels protecting the system from shortage. This effect is stronger when supply availability probability is higher, as a costly shortage might be avoided which would not have been anticipated without ASI.

• Not only the content of ASI, but also the mere existence of ASI may change the optimal solution. This is because the overall uncertainty of the problem decreases as the length of ASI horizon increases, which might effect the ordering decision whatever the information is. For example, under scenario 6 for demand pattern 4, S(∞) is greater than both S(∞,∞) and S(∞,0). That is, the optimal order-up-to level in this case decreases with an additional one-period ASI, both for a supply period signal as well as a shortage signal.

• The existence of the <sup>fi</sup>xed ordering cost triggers intricate cost interactions in the system, which makes it dif<sup>fi</sup>cult to draw simple conclusions regarding the order-up-to level as a function of ASI. For example, ASI that signals supply availability in period 3 in our experiment results in an increased order-up-to level compared to an ASI that signals shortage in period 3, that is, S(∞,∞)≥S(∞,0), contrary to what one might expect.

Table 4 Demand patterns.

<table><tr><td>Demand</td><td>Period 1</td><td>Period 2</td><td>Period 3</td><td>Period 4</td></tr><tr><td>1</td><td>5</td><td>15</td><td>25</td><td>35</td></tr><tr><td>2</td><td>35</td><td>25</td><td>15</td><td>5</td></tr><tr><td>3</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>4</td><td>10</td><td>10</td><td>10</td><td>50</td></tr><tr><td>5</td><td>30</td><td>10</td><td>30</td><td>10</td></tr></table>

Table 5 Probability patterns.

<table><tr><td>Scenarios</td><td>Period 1</td><td>Period 2</td><td>Period 3</td><td>Period 4</td></tr><tr><td>Scenario 1</td><td>0.9</td><td>0.9</td><td>0.9</td><td>0.9</td></tr><tr><td>Scenario 2</td><td>0.9</td><td>0.9</td><td>0.1</td><td>0.1</td></tr><tr><td>Scenario 3</td><td>0.9</td><td>0.1</td><td>0.9</td><td>0.1</td></tr><tr><td>Scenario 4</td><td>0.1</td><td>0.1</td><td>0.1</td><td>0.1</td></tr><tr><td>Scenario 5</td><td>0.1</td><td>0.1</td><td>0.9</td><td>0.9</td></tr><tr><td>Scenario 6</td><td>0.1</td><td>0.9</td><td>0.1</td><td>0.9</td></tr></table>

Table 6 Order-up-to levels.

<table><tr><td rowspan="2">ASI</td><td colspan="5">M=2</td><td colspan="2">M=1</td><td colspan="2">M=0</td></tr><tr><td>y(0,0)</td><td>y(0,∞)</td><td>y(∞,0)</td><td>y(∞,∞)</td><td>y(0)</td><td>y(∞)</td><td>y</td><td></td><td></td></tr><tr><td>Scenario 1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td>Scenario 2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>2</td><td></td><td></td></tr><tr><td>Scenario 3</td><td>4</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td></td><td></td></tr><tr><td>Scenario 4</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>4</td><td></td><td></td></tr><tr><td>Scenario 5</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td></td><td></td></tr><tr><td>Scenario 6</td><td>3</td><td>2</td><td>1</td><td>1</td><td>3</td><td>1</td><td>1</td><td></td><td></td></tr><tr><td colspan="10">A=20</td></tr><tr><td colspan="2">ASI</td><td colspan="3">M=2</td><td colspan="2">M=1</td><td colspan="3">M=0</td></tr><tr><td>Scenario 1</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>22.33</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>1</td><td>11.31</td></tr><tr><td></td><td>3</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>9.14</td></tr><tr><td></td><td>4</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>2</td><td>3</td><td>19.86</td></tr><tr><td></td><td>5</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>13.67</td></tr><tr><td>Scenario 2</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>2</td><td>22.64</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>4</td><td>18.21</td></tr><tr><td></td><td>3</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>2</td><td>23.03</td></tr><tr><td></td><td>4</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>2</td><td>17.43</td></tr><tr><td></td><td>5</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>4</td><td>19.93</td></tr><tr><td>Scenario 3</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>4</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>17.88</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>8.97</td></tr><tr><td></td><td>3</td><td>4</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>12.85</td></tr><tr><td></td><td>4</td><td>4</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>12.40</td></tr><tr><td></td><td>5</td><td>4</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>17.97</td></tr><tr><td>Scenario 4</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>4</td><td>0.43</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>4</td><td>0.05</td></tr><tr><td></td><td>3</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>4</td><td>0.17</td></tr><tr><td></td><td>4</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>4</td><td>0.53</td></tr><tr><td></td><td>5</td><td>4</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>4</td><td>0.13</td></tr><tr><td>Scenario 5</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>7.39</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>0.14</td></tr><tr><td></td><td>3</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>1</td><td>2</td><td>0.44</td></tr><tr><td></td><td>4</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>2</td><td>3</td><td>8.83</td></tr><tr><td></td><td>5</td><td>3</td><td>2</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>0.63</td></tr><tr><td>Scenario 6</td><td>Demand</td><td>S(0,0)</td><td>S(0,∞)</td><td>S(∞,0)</td><td>S(∞,∞)</td><td>S(0)</td><td>S(∞)</td><td>S</td><td>%VOI0-2</td></tr><tr><td></td><td>1</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>1</td><td>3</td><td>9.25</td></tr><tr><td></td><td>2</td><td>4</td><td>2</td><td>1</td><td>1</td><td>4</td><td>1</td><td>4</td><td>0.86</td></tr><tr><td></td><td>3</td><td>3</td><td>2</td><td>1</td><td>1</td><td>3</td><td>1</td><td>3</td><td>3.64</td></tr><tr><td></td><td>4</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>3</td><td>3</td><td>10.06</td></tr><tr><td></td><td>5</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>1</td><td>1</td><td>0.63</td></tr></table>

## 6. Conclusions and future work

In this paper, we analyzed a single-item, periodic review, deterministic demand inventory system under non-stationary supply availability with ASI. This paper contributes to the supply uncertainty literature in that, ASI is incorporated into an inventory model and near-explicit solutions are obtained under ASI. Optimal policy is characterized and shown to be a state dependent $( s _ { n } ( w _ { n } ) , S _ { n } ( w _ { n } ) )$ ) policy.

For the model with no <sup>fi</sup>xed ordering cost optimal ordering policy is shown to be of order-up-to type, based on the convexity of the relevant cost functions. Several characteristics of the optimal orderup-to levels are presented and a simple algorithm is constructed for <sup>fi</sup>nding the optimal order-up-to levels for an arbitrary length of ASI horizon. When there is <sup>fi</sup>xed ordering cost, analytical solutions for the re-order point and the order-up-to level are dif<sup>fi</sup>cult to obtain and the dynamic programming model becomes hard to solve for a large state space. Therefore a heuristic algorithm is suggested for <sup>fi</sup>nding a good ordering strategy. Proposed heuristic algorithm is an alternative for <sup>fi</sup>nding good ordering strategies, especially when there is scarcity in supply. Heuristic algorithm is satisfactory considering the deviation from the optimal solution, and it is computationally much faster.

In addition to the analytical results, we also provide a numerical analysis that yields important managerial insights. Based on our numerical experiments, we conclude that contractual agreements regarding information sharing would be more valuable when there exist non-stationarity in supply availability (e.g. low supply availability during holiday periods) or demand (e.g. seasonality), where the value increases in the degree of non-stationarity. On the other hand, information sharing might not be pro<sup>fi</sup>table enough when the ordering costs are high and when the supply availability is consistently low in the system. For the low availability case, information sharing could be justi<sup>fi</sup>ed if the ASI spans a long horizon, whereas if supply is known to be reliable, most important information is provided by the near future periods which eliminates the need for an agreement over a long ASI horizon. We also observe that the bene<sup>fi</sup>t of ASI is not only in terms of costs, but also in terms of robustness in managing the system under non-stationarity.

As a further research, stochastic demand structure can be considered and advance demand information (ADI) can be incorporated into the model having the needed technological infrastructure already at hand for ASI. Inclusion of the ADI will strengthen the supply chain by decreasing the overall costs. ASI in this paper is considered to be a perfect information and another extension can be the model with imperfect ASI, which might be more realistic in some inventory systems.

## Acknowledgments

The authors are thankful to the guest editors for an ef<sup>fi</sup>cient and timely review process. We would like to thank the reviewers for helpful suggestions that led to improvements in content and presentation of the paper.

## Appendix A. Proofs of the results

Proof of Proposition 1. For $n = N , y _ { N } ( w _ { N } ) = D _ { N }$ and the assertion holds. Assume that, the statement is true for $n + 1 .$ . Since $C _ { n + 1 } ( I , z _ { n + 1 } )$ is convex and it is minimized at $I { = } y _ { n { + } 1 } ( w _ { n { + } 1 } ) ,$ , it follows that for $y < D _ { n } , ~ C _ { n + 1 } ( y - D _ { n } , z _ { n + 1 } ) \geq C _ { n + 1 } ( 0 , z _ { n + 1 } ) \geq C _ { n + 1 } ( y _ { n + 1 } ( w _ { n + 1 } ) , z _ { n + 1 } )$ for any $z _ { n + 1 }$ since $y _ { n + 1 } ( w _ { n + 1 } ) { \ge } D _ { n + 1 } { \ge } 0 { \ge } y - D _ { n } .$ We also know that $L _ { n } ( y )$ is minimized at $D _ { n } \thinspace s 0 \thinspace L _ { n } ( y ) { \geq } L _ { n } ( D _ { n } )$

$$
\begin{array}{l} G _ {n} (y, w _ {n}) = L _ {n} (y) + E \big [ C _ {n + 1} \big (y - D _ {n}, w _ {n}, Q _ {n + M + 1} \big) \big ] \\ = L _ {n} (y) + p _ {n + M + 1} C _ {n + 1} (y - D _ {n}, w _ {n}, \infty) + (1 - p _ {n + M + 1}) C _ {n + 1} (y - D _ {n}, w _ {n}, 0) \\ \geq L _ {n} (D _ {n}) + p _ {n + M + 1} C _ {n + 1} (D _ {n} - D _ {n}, w _ {n}, \infty) + (1 - p _ {n + M + 1}) C _ {n + 1} (D _ {n} - D _ {n}, w _ {n}, 0) \\ = G _ {n} (D _ {n}, w _ {n}). \end{array}
$$

Therefore, for $y < D _ { n }$ we have $G _ { n } ( y , w _ { n } ) { \geq } G _ { n } ( D _ { n } , w _ { n } )$ and this completes the proof. □

Proof of Proposition 2. Choose $\eta \in [ 0 , D _ { n + 1 } ]$ , and let $y = D _ { n } + \eta .$ . We will show that $G _ { n } ( y , r _ { M } )$ increases in η and this together with the convexity of $G _ { n } ( y , r _ { M } )$ and $y _ { n } ( w ) { \geq } D _ { n }$ will imply that $y _ { n } ( r _ { M } ) = D _ { n } .$ First recall that

$$
G _ {n} (y, r _ {M}) = L _ {n} (y) + E \left[ C _ {n + 1} (y - D _ {n}, r _ {M}, Q) \right],\tag{A.1}
$$

where $Q \in \{ 0 , \infty \}$ with respective probabilities $1 - p$ and p. Also note that since the supply is fully available in period n+1 and as $y - D _ { n } = \eta \leq D _ { n + 1 }$ , the system reaches its target inventory position $y _ { n + 1 } ( w )$ at the beginning of period $n + 1$ . Hence $E [ C _ { n + 1 } ( y - D _ { n } , r _ { M } ,$ $Q ) ] = E [ G _ { n + 1 } ( y _ { n + 1 } ( W _ { n + 1 } ) , W _ { n + 1 } ) ] ,$ . The speci<sup>fi</sup>c form of $W _ { n + 1 }$ is induced by $( r _ { M } , Q )$ but happens to be irrelevant. Now, note that $G _ { n } ( y , r _ { M } )$ is minimized by minimizing $L _ { n } ( y ) = L _ { n } ( D _ { n } + \eta )$ , and achieves its minimum at $\eta = 0 .$ By Proposition 1 we know that $y _ { n } ( w _ { n } ) { \geq } D _ { n }$ so we can conclude that $y _ { n } ( r _ { M } ) = D _ { n } { \leq } y _ { n } ( w _ { n } )$ □

Proof of Proposition 3. First note that since $w = \left( o _ { l } , r _ { M - l } \right)$ for some $l { \in } \{ 1 , 2 , { \ldots } , M - 1 \}$

$$
\begin{array}{l} G _ {n} (y, w) = L _ {n} (y) + \sum_ {j = 1} ^ {l} L _ {n + j} (y - D (n, n + j - 1)) \\ \qquad + E \big [ C _ {n + l + 1} \big (y - D (n, n + l), \infty , W _ {n + l + 1} \big) \big ]. \end{array}
$$

De<sup>fi</sup>ne $\begin{array} { r } { V _ { n } ( y ) = L _ { n } ( y ) + \sum _ { j = 1 } ^ { l } L _ { n + j } ( y - D ( n , n + j - 1 ) ) } \end{array}$ . First note that $V _ { n } ( y )$ increases for $y { > } D ( n , n + l )$ . Also, since the supply state in period $n + l + 1$ is ∞, that is, since we can raise the inventory level of period $n + l + 1 \mathrm { ~ t o ~ } y _ { n + l + 1 } \big ( w _ { n + l + 1 } \big )$ as long as $y - D ( n , n +$ $\begin{array} { r } { l ) < y _ { n + l + 1 } ( w _ { n + l + 1 } ) , \subset _ { n + l + 1 } ( y - D ( n , n + l ) , \infty , w _ { n + l + 1 } ) } \end{array}$ is nondecreasing for $y { > } D ( n , n + l )$ . Therefore at optimality we have $y _ { n } ( w ) { \leq } D ( n , n + l )$

Moreover, for $y \le D ( n , n + l ) , y - D ( n , n + l ) \le 0 \le y _ { n + l + 1 } ( w _ { n + l + 1 } ) .$ Hence,

$$
E \left[ C _ {n + l + 1} (y - D (n, n + l), \infty , W _ {n + l + 1}) \right] = E \left[ G _ {n + l + 1} \left(y _ {n + l + 1} \left(W _ {n + l + 1}\right), W _ {n + l + 1}\right) \right],
$$

which is a constant. Then $G _ { n } ( y , w )$ is minimized by minimizing

$$
V _ {n} (y) = L _ {n} (y) + \sum_ {j = 1} ^ {l} L _ {n + j} (y - D (n, n + j - 1)).
$$

$V _ { n } ( y )$ is not differentiable at $\{ D ( n , n ) , D ( n , n + 1 ) , . . . , D ( n , n + l ) \}$ but for any $i { \in } \{ 1 , 2 , . . . , l \}$ and $y \in ( D ( n , n + i - 1 ) , D ( n , n + i ) )$ , the derivative of $V _ { n } ( y ) { \mathrm { ~ i s ~ } } V _ { n } ^ { \prime } ( y ) = i h - ( l - i + 1 ) b .$ . Then $G _ { n } ( y , w )$ is minimized by

$$
y _ {n} (w) = \min \left\{y: V _ {n} ^ {\prime} (y) \geq 0 \right\},
$$

and we can write $y _ { n } ( w ) { = } D ( n , n + K ( w ) - 1 )$ where

$$
K (w) = \min \{i \in \{1, 2,..., l \}: i \geq (l + 1) b / (h + b) \}.\tag{A.2}
$$

$\operatorname { L e t } K ( w ) = l + 1$ if no such $K ( w )$ exists. Then, K(w) can be rewritten as in $\operatorname { E q } . \left( 3 \right)$ □

Proof of Proposition 4. For any $w = \left( o _ { l } , r _ { M - l } \right)$ where $l { < } M , y _ { n } ( w ) =$ $D ( n , n + K ( w ) - 1 )$ for $K ( w ) { \in } \{ 1 , 2 , { \ldots } , l + 1 \}$ (note that $K ( w ) { \leq } M )$ Proposition 3 states that ${ \mathrm { i f ~ } } h { \in } \left\{ \frac { ( l - j + 1 ) } { j } b , \frac { ( l - j + 2 ) } { j - 1 } b \right\} { \mathrm { ~ f o r ~ } } j { \in } \{ 2 , . . . , $ $l + 1 \}$ then $K ( w ) = j .$ . This means that, for any $K ( w ) \in \{ 2 , . . . , l + 1 \}$ we need to have $h { \in } \biggl \{ \frac { ( l { - } K ( w ) + 1 ) } { K ( w ) } b , \frac { ( l { - } K ( w ) + 2 ) } { K ( w ) { - } 1 } b \biggr \}$ . Notice that we <sup>ð Þ</sup>can write the upper bound on h as $h ( K ( w ) - 1 ) { < } ( l - K ( w ) + 2 ) b$ .

We can write $G _ { n } ( y , o _ { M } )$ as

$$
\begin{array}{c} G _ {n} (y, o _ {M}) = L _ {n} (y) + \sum_ {j = 1} ^ {M} L _ {n + j} (y - D (n, n + j - 1)) \\ \qquad + E \big [ C _ {n + M + 1} \big (y - D (n, n + M), Z _ {n + M + 1} \big) \big ]. \end{array}\tag{A.3}
$$

Choose $y \in ( D ( n , n + K ( w ) - 2 ) , D ( n , n + K ( w ) - 1 ) )$ . Then $y - D ( n ,$ $n + M ) < D ( n , n + K ( w ) - 1 ) - D ( n , n + M ) < 0 < y _ { n + M + 1 } ( w _ { n + M + 1 } )$ since $K ( w ) { \leq } M .$ De<sup>fi</sup>ne $V _ { n } ( y ) = L _ { n } ( y ) + \sum _ { i = 1 } ^ { M } L _ { n + j } ( y - D ( n , n + j - 1 ) )$ for the ease of <sup>¼</sup>notation. Select η in such a way that $y + \eta { \in } ( D ( n , n + K ( w ) - 2 ) , D ( n ,$ $n + K ( w ) - 1 ) ,$ ). Then we can write

$$
\begin{array}{r l} & G _ {n} (y + \eta , o _ {M}) - G _ {n} (y, o _ {M}) = V _ {n} (y + \eta) - V _ {n} (y) \\ & \quad + E \big [ C _ {n + M + 1} \big (y + \eta - D (n, n + M), Z _ {n + M + 1} \big) \big ] \\ & \quad - E \big [ C _ {n + M + 1} \big (y - D (n, n + M), Z _ {n + M + 1} \big) \big ]. \end{array}\tag{A.4}
$$

We know that $C _ { n + M + 1 } ( y , z _ { n + M + 1 } )$ is convex in y and minimized at $y _ { n + M + 1 } ( w _ { n + M + 1 } ) { \ge } D _ { n + M + 1 } { \ge } 0 .$ . Then $C _ { n + M + 1 } ( 0 , Z _ { n + M + 1 } ) <$ $C _ { n + M + 1 } ( y + \eta - D ( n , n + M ) , Z _ { n + M + 1 } ) < C _ { n + M + 1 } ( y - D ( n , n + M )$ $Z _ { n + M + 1 } )$ for any such selected η. Therefore

$$
E \left[ C _ {n + M + 1} (y + \eta - D (n, n + M), Z _ {n + M + 1}) - C _ {n + M + 1} (y - D (n, n + M), Z _ {n + M + 1}) \right] <   0.
$$

Also we can write $V _ { n } ( y + \eta ) - V _ { n } ( y ) = ( K ( w ) - 1 ) h \eta - ( M - K ( w ) +$ 2)bη since under both y and $y + \eta$ we have on-hand inventory for periods $n , n + 1 , . . . , n + K ( w ) - 2$ and insuf<sup>fi</sup>cient inventory for periods $n + K ( w ) - 1 , n + K ( w ) , . . . , n + M ,$ . We know from Proposition 3 that $h ( K ( w ) - 1 ) { < } ( l - K ( w ) + 2 ) b$ . Therefore $h ( K ( w ) - 1 ) { < } ( M - K ( w ) +$ 2)b since $l { < } M .$ Therefore $V _ { n } ( y + \eta ) - V _ { n } ( y ) \le 0$

As a result $G _ { n } ( y + \eta , o _ { M } ) - G _ { n } ( y , o _ { M } ) \le 0$ meaning that $y _ { n } ( o _ { M } ) \ge$ $D ( n , n + K ( w ) - 1 ) = y _ { n } ( w )$ for any $w = \left( o _ { l } , r _ { M - l } \right)$ with l b M. □

Proof of Proposition 5. It is suf<sup>fi</sup>cient to show that $y _ { n } ( o _ { M } ) \leq D _ { n } +$ $y _ { n + 1 } ( o _ { M } )$ since Proposition 4 states that $y _ { n } ( w _ { n } ) { \leq } y _ { n } ( o _ { M } )$ for all $w _ { n } .$ Assertion holds for $n { = } N ,$ , because $y _ { N } ( w _ { N } ) = D _ { N }$ and $y _ { N + 1 } ( w _ { N + 1 } ) = 0$ for all $w _ { N + 1 } .$

Suppose $y > D _ { n } + y _ { n + 1 } \big ( o _ { M } \big )$ , we need to show that $G _ { n } ( y , o _ { M } ) \ge$ $G _ { n } ( D _ { n } + y _ { n + 1 } ( o _ { M } ) , o _ { M } )$ . We need the following ingredients:

$\bullet L _ { n } ( y ) \geq L _ { n } ( D _ { n } + y _ { n + 1 } ( o _ { M } ) ) \mathop { \mathrm { a s } } L _ { n } ( y )$ is convex and minimized $\mathtt { a t } y = D _ { n }$ $\bullet _ { \mathbf { \lambda } } C _ { n + 1 } ( y - D _ { n } , o _ { M } , \infty ) \geq C _ { n + 1 } ( y _ { n + 1 } ( o _ { M } ) , o _ { M } , \infty )$ because we know that $y _ { n + 1 } ( o _ { M } ) \ge y _ { n + 1 } ( o _ { M - 1 } , \infty ) .$ So b $\prime \mathrm { c o n v e x i t y } \mathrm { o f } C _ { n + 1 } , C _ { n + 1 } ( y - D _ { n } , o _ { M } , \infty ) \ge C _ { n + 1 } ( D _ { n } + y _ { n + 1 } ( o _ { M } ) -$ $D _ { n } , o _ { M } , \infty ) \ge C _ { n + 1 } ( y _ { n + 1 } ( o _ { M - 1 } , \infty ) , o _ { M } , \infty ) .$ $\bullet \ C _ { n + 1 } ( y - D _ { n } , o _ { M } , 0 ) \geq C _ { n + 1 } ( y _ { n + 1 } ( o _ { M } ) , o _ { M } , 0 )$ since $C _ { n + 1 } ( y , o _ { M } , 0 )$ is minimized at $y _ { n + 1 } ( o _ { M } )$ by Corollary 1.

Putting everything together:

$$
\begin{array}{l} G _ {n} (y, o _ {M}) = L _ {n} (y) + p _ {n + M + 1} C _ {n + 1} (y - D _ {n}, o _ {M}, \infty) + (1 - p _ {n + M + 1}) C _ {n + 1} (y - D _ {n}, o _ {M}, 0) \\ \geq L _ {n} \big (D _ {n} + y _ {n + 1} (o _ {M}) \big) + p _ {n + M + 1} C _ {n + 1} \big (y _ {n + 1} (o _ {M}), o _ {M}, \infty \big) \\ \quad + \big (1 - p _ {n + M + 1} \big) C _ {n + 1} \big (y _ {n + 1} (o _ {M}), o _ {M}, 0 \big) \\ = G _ {n} \big (D _ {n} + y _ {n + 1} (o _ {M}), o _ {M} \big). \end{array}
$$

Proof of Proposition 6. Suppose that $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , n + J )$ and fo $\cdot j { \in } \{ 1 , 2 , . . . , J \} \sec y { = } D ( n , n + j ) - \eta$ for some $\eta \in [ 0 , D _ { n + j } ]$ . The evolution of the inventory level in periods $n + 1 , n + 2 , \ldots$ depends on the choice of η.

For a <sup>fi</sup>xed $j { \in } \{ 1 , 2 , . . . , J \}$ de<sup>fi</sup>ne $\tau _ { n } ( \eta )$ as the <sup>fi</sup>rst time after n that the inventory level is raised to the optimal order-up-to level (possibly by ordering zero) when the inventory level after ordering at the beginning of period n is equal to y.

First note that $\tau _ { n } ( \eta ) = i$ implies that (1) the supply availability information in period $n + i$ should be of the form $z _ { n + i } = ( \infty , w )$ for some w and (2) the inventory level before ordering at period $n + i$ should be less than $y _ { n + i } ( w )$ . In periods prior to n + i it is either not possible to order (that is, supply is not available), or the inventory level is above the period's respective order-up-to level.

With this de<sup>fi</sup>nition of $\cdot _ { n } ( \eta )$ we can write $G _ { n } ( y ) \operatorname { f o r } y = D ( n , n + j ) - \eta$ as

$$
\begin{array}{l} G _ {n} (y, o _ {M}) = L _ {n} (y) + \sum_ {i = 1} ^ {N - n} P r \{\tau_ {n} (\eta) > i \} L _ {n + i} (y - D (n, n + i - 1)) \\ \qquad + \sum_ {i = 1} ^ {N - n} \sum_ {w} P r \{\tau_ {n} (\eta) = i, W _ {n + i} = w \} G _ {n + i} (y _ {n + i} (w), w). \end{array}\tag{A.5}
$$

The second term in Eq. (A.5) stands for the case that ordering occurs at a period later than n+i and hence the starting inventory level of period $n + i \mathrm { i } s y - D ( n , n + i - 1 )$ , and a cost of $L _ { n + i } ( y - D ( n , n + i - 1 ) )$ is incurred in period n+i.

The third term in Eq. (A.5) is due to the fact that if $\tau _ { n } = i$ and $W = w ,$ , then the starting inventory level of period n+i after ordering is $y _ { n + i } ( w )$ and the expected cost incurred is $G _ { n + i } ( y _ { n + i } ( w ) , w )$

It can be shown that the distribution of $\tau _ { n } ( \eta ^ { \prime } )$ is the same for all $0 { \le } { \eta } ^ { \prime } { \le } { \eta }$ and in particular for $\eta ^ { \prime } = 0 .$ . Note that if it is not possible to order prior to period $n + i$ for a particular $\eta { > } 0$ , then in the same periods an ordering cannot occur for $0 \leq \eta ^ { \prime } \leq \eta .$

Moreover, if an ordering occurs in period $n + i$ (by raising the inventory position up to $y _ { n + i } ( w ) )$ with $\eta { > } 0 ,$ , then for any $0 { \le } \eta ^ { \prime } { \le } \eta$ an ordering occurs in period n+i by raising the inventory level to the same order-up-to level $y _ { n + i } ( w )$

Suppose that $\{ \tau _ { n } ( \eta ) = i , W = w \}$ with $w = o _ { M }$ (the case w≠o<sub>M</sub> is sim ilar). Note that $y = D ( n , n + j ) - \eta \le D _ { n } + y _ { n + 1 } ( o _ { M } )$ since $y _ { n + 1 } ( o _ { M } ) =$ $D ( n + 1 , n + J )$ and $j { \in } \{ 1 , 2 , . . . , J \}$ . By Proposition 5 we know that $y _ { n + 1 } ( o _ { M } ) \leq D _ { n + 1 } + y _ { n + 2 } ( o _ { M } )$ so we can write $y _ { n + 1 } ( o _ { M } ) { \leq } D ( n +$ $1 , n + i - 1 ) + y _ { n + i } ( o _ { M } )$ (that is, $y _ { n + i } ( o _ { M } ) \ge D ( n + i , n + J ) )$ . Therefore $y = D ( n , n + j ) - \eta \leq D ( n , n + i - 1 ) + y _ { n + i } ( o _ { M } )$ . Note that for $\eta = 0$ we will have an inventory of $D ( n , n + j )$ at the beginning of period n. Having no available supply till period $n + i ,$ at the beginning of period n+i we will have an inventory of $D ( n , n + j ) - D ( n , n + i -$ $1 ) = D ( n + i , n + j ) \leq D ( n + i , n + J ) \leq y _ { n + i } ( o _ { M } )$ . This enables us to drop η from $\tau _ { n } ( \eta )$ and write Eq. (A.5) as:

$$
\begin{array}{l} G _ {n} (y, o _ {M}) = L _ {n} (y) + \sum_ {i = 1} ^ {N - n} P r \{\tau_ {n} > i \} L _ {n + i} (y - D (n, n + i - 1)) \\ \qquad + \sum_ {i = 1} ^ {N - n} \sum_ {w} P r \{\tau_ {n} = i, W _ {n + i} = w \} G _ {n + i} (y _ {n + i} (w), w). \end{array}\tag{A.6}
$$

Therefore we can write the difference $G _ { n } ( y , o _ { M } ) - G _ { n } ( D ( n , n + j ) , o _ { M } )$ as

$$
\begin{array}{l} G _ {n} (y, o _ {M}) - G _ {n} (D (n, n + j), o _ {M}) = L _ {n} (y) - L _ {n} (D (n, n + j)) \\ \qquad + \sum_ {i = 1} ^ {N - n} P r \{\tau_ {n} > i \} \left[ L _ {n + i} (y - D (n, n + i - 1)) - L _ {n + i} (D (n + i, n + j)) \right]. \end{array}\tag{A.7}
$$

For $i \geq j , y - D ( n , n + i - 1 ) = D ( n + i , n + j ) - \eta \leq D _ { n + i } .$ We know from Proposition 1 that $y _ { n + i } ( w ) { \geq } D _ { n + i } { \sf S } 0$ we can write

$$
\mathcal {P} _ {n} (i) := \operatorname * {P r} \left\{\tau_ {n} > i \right\} = \operatorname * {P r} \left\{R _ {w} (n) > i, \forall w \right\}.
$$

For i bj, the inventory level is raised to $y _ { n + i } ( o _ { M } )$ whenever $Z _ { n + i } = ( \infty , 0 _ { M } ) . \mathrm { I f } Z _ { n + i } = ( \infty , w )$ for $\prime \neq 0 _ { M }$ then an order is placed $\operatorname { i f } y$ $- D ( n , n + i - 1 ) \le y _ { n + i } ( w )$ . Therefore

$$
\begin{array}{l} \operatorname * {P r} \{\tau_ {n} > i \} = P r \bigl \{R _ {w} (n) > i: y - D (n, n + i - 1) \leq y _ {n + i} (w) \bigr \} \\ \qquad = P r \Bigl \{R _ {o _ {M}} (n) > i, R _ {w} (n) > i, \forall w \in \Omega , w \neq o _ {M}, y - D (n, n + i - 1) \leq y _ {n + i} (w). \Bigr \} \end{array}
$$

For $w \neq o _ { M } , y - D ( n , n + i - 1 ) \leq y _ { n + i } ( w )$ implies that $D ( n , n +$ $j ) - \eta - D ( n , n + i - 1 ) = D ( n + i , n + j ) - \eta \leq y _ { n + i } ( w ) = D ( n + i , n + i + 1 ) , \qquad i = 0 , \dots , N - 1 ,$ $K ( w ) - 1 )$ . Therefore $n + j \leq n + i + K ( w ) - 1$ which implies $K ( w ) \geq$ $j - i + 1$ . Hence for i bj

$$
\begin{array}{c} \mathcal {Q} _ {n} (i, j) := P r \{\tau_ {n} > i \} \\ := P r \Bigl \{R _ {o _ {M}} (n) > i, R _ {w} (n) > i: \forall w: w \neq o _ {M}, K (w) \geq j - i + 1 \Bigr \} \end{array}
$$

where $K ( w )$ is de<sup>fi</sup>ned as in Proposition 3. Also note that $L _ { n } ( y ) -$ $L _ { n } ( D ( n , n + j ) ) = - \eta h$ . Now, putting these together, Eq. (A.7) can be written as

$$
G _ {n} (y, o _ {M}) - G _ {n} (D (n, n + j), o _ {M}) = - h \eta - h \eta \sum_ {i = 1} ^ {j - 1} \mathcal {Q} _ {n} (i, j) + b \eta \sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)
$$

We also note that for $i \geq j , \mathcal { Q } _ { n } ( i , j ) = \mathcal { P } _ { n } ( i )$ (since $K ( w ) { \geq } 1 )$ . Therefore

$$
\begin{array}{c} \sum_ {i = 1} ^ {j - 1} \mathcal {Q} _ {n} (i, j) = \sum_ {i = 1} ^ {N - n} \mathcal {Q} _ {n} (i, j) - \sum_ {i = j} ^ {N - n} \mathcal {Q} _ {n} (i, j) \\ = \sum_ {i = 1} ^ {N - n} \mathcal {Q} _ {n} (i, j) - \sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i). \end{array}
$$

Therefore $G _ { n } ( D ( n , n + j ) , \allowbreak o _ { M } ) \leq G _ { n } ( y , \ t _ { 0 _ { M } } )$ if and only if

$$
\frac {\sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)}{1 + \sum_ {i = 1} ^ {j - 1} \mathcal {Q} _ {n} (i , j) + \sum_ {i = j} ^ {N - n} \mathcal {P} _ {n} (i)} \geq \frac {h}{h + b}.
$$

The probability term $P r \{ R _ { w } ( n ) > i ; \forall w \}$ is in fact the probability that there is no available supply in one of the periods from period $n +$ $M + 1$ (note that we know the supply state of the periods $n , n + 1$ $\ldots , n + M )$ up to and including period $n + i .$ Therefore $P r \{ R _ { w } ( n ) >$ $i ; \forall w \} = 1$ for $i { < } M + 1$ since we know that in periods $n + 1 , . . . ,$ n + M supply is unavailable. For $i \ge M + 1 , P r \{ R _ { w } ( n ) > i ; \forall w \} =$ $\prod _ { k = M + 1 } ^ { i } ( 1 - p _ { n + k } )$ □

Derivation of $\mathcal { Q } _ { n } ( i , j )$ . First note that the evolution of ASI process $\{ Z _ { n } , n \ge 1 \}$ <sup>Q ð Þ</sup>is a time-dependent Markov chain on $\Omega _ { M + 1 } .$ For all $z \in \varOmega _ { M + 1 }$ and $z ^ { \prime } \in \varOmega _ { M + 1 }$ de<sup>fi</sup>ne $P _ { z , z ^ { \prime } } ( n ) = P \{ Z _ { n + 1 } = z ^ { \prime } | Z _ { n } = z \}$ , and let $\mathcal { U } ( n )$ be the square matrix with entries $\{ P _ { z , z ^ { \prime } } ( n ) , z , z ^ { \prime } \in \varOmega _ { M + 1 } \} .$ $\mathcal { U } ( n )$ <sup>ð Þ</sup>is the time-dependent transition matrix of the Markov chain. Note that given $Z _ { n } = z = ( q , w ) , Z _ { n + 1 }$ only depends on w, but not on the current supply state.

For a <sup>fi</sup>xed $j { \in } \{ 1 , 2 , . . . , J \}$ and $i { \in } \{ 1 , 2 , { \ldots } , j - 1 \}$ de<sup>fi</sup>ne

$$
E _ {i, j} = \left\{\left(\infty , w\right): w \in \Omega_ {M}, w = o _ {M} \text {or} K (w) \geq j - i + 1 \right\}.
$$

De<sup>fi</sup>ne:

$$
f _ {z} ^ {(k)} (n, E _ {i, j}) = \operatorname * {P r} \left\{Z _ {n + 1} \notin E _ {i, j}, Z _ {n + 2} \notin E _ {i, j}, \dots , Z _ {n + k} \notin E _ {i, j} | Z _ {n} = z \right\}.
$$

Since given $Z _ { n } = ( q , w ) , Z _ { n + 1 }$ depends only on w,

$$
f _ {0, o _ {M}} ^ {(i)} (n, E _ {i, j}) = f _ {\infty , o _ {M}} ^ {(i)} (n, E _ {i, j}).
$$

Therefore,

$$
\begin{array}{c} \mathcal {Q} _ {n} (i, j) = P r \Bigl \{R _ {o _ {M}} (n) > i, R _ {w} (n) > i: \forall w: w \neq o _ {M}, K (w) \geq j - i + 1 \Bigr \} \\ = f _ {\infty , o _ {M}} ^ {(i)} \Bigl (n, E _ {i, j} \Bigr). \end{array}
$$

De<sup>fi</sup>ne $f ^ { ( k ) } ( n , E _ { i , j } )$ as the column vector $\{ f _ { z } ^ { ( k ) } ( n , E _ { i , j } ) , z \in \Omega _ { M + 1 } \} ^ { T } ,$ . Let $\tilde { \mathcal { U } } ^ { ( i ) } ( n )$ be the matrix $\mathcal { U } ( n )$ where columns corresponding to $E _ { i , j }$ are replaced by zeros.

$$
f _ {z} ^ {(1)} \Big (n, E _ {1, j} \Big) = P r \Big \{Z _ {n + 1} \not \in E _ {1, j} \big | Z _ {n} = z \Big \} = \sum_ {z ^ {^ {\prime}} \not \in E _ {1, j}} P r \Big \{Z _ {n + 1} = z ^ {^ {\prime}} \big | Z _ {n} = z \Big \}.
$$

Therefore $f ^ { ( 1 ) } \big ( n , E _ { 1 , j } \big ) = \tilde { \mathcal { U } } ^ { ( 1 ) } ( n ) \mathrm { ~ \underline { { ~ 1 ~ } } ~ }$ , where 1 is the column vector whose entries are all 1's and whose size matches $\tilde { \mathcal { U } } ^ { ( 1 ) } ( n )$

We can <sup>fi</sup>nd $f _ { z } ^ { ( 2 ) } ( n , E _ { 2 , j } )$ as:

$$
\begin{array}{l} f _ {z} ^ {(2)} \Big (n, E _ {2, j} \Big) = P r \Big \{Z _ {n + 1} \not \in E _ {2, j}, Z _ {n + 2} \not \in E _ {2, j} \big | Z _ {n} = z \Big \} \\ = \sum_ {z ^ {'} \not \in E _ {2, j}} P _ {z, z ^ {'} (n)} P r \Big \{Z _ {n + 2} \not \in E _ {2, j} \big | Z _ {n + 1} = z ^ {'} \Big \} \\ = z ^ {t h} \text {entry of the column vector} \quad \tilde {U} ^ {(2)} (n) f ^ {(1)} \Big (n + 1, E _ {2, j} \Big). \end{array}
$$

since $P r \{ Z _ { n + 2 } \notin E _ { 2 , j } | Z _ { n } = z ^ { \prime } \} = f _ { z ^ { \prime } } ^ { ( 1 ) } ( n + 1 , E _ { 2 , j } ) .$

In general,

$$
\begin{array}{l} f _ {z} ^ {(i)} \Big (n, E _ {i, j} \Big) = P r \Big \{Z _ {n + 1} \not \in E _ {i, j},..., Z _ {n + i} \not \in E _ {i, j} \Big | Z _ {n} = z \Big \} \\ = \sum_ {z ^ {'} \not \in E _ {i, j}} P _ {z, z ^ {'}} (n) P r \Big \{Z _ {n + 2} \not \in E _ {i, j},..., Z _ {n + i} \not \in E _ {i, j} \Big | Z _ {n + 1} = z ^ {'} \Big \} \end{array}
$$

where $P r \{ Z _ { n + 2 } \notin E _ { i , j } , . . . , Z _ { n + i } \notin E _ { i , j } | Z _ { n + 1 } = z ^ { \prime } \} = f _ { z ^ { \prime } } ^ { ( i - 1 ) } ( n + 1 , E _ { i , j } ) ,$ Therefore,

$$
f ^ {(i)} (n, E _ {i, j}) = \tilde {\mathcal {U}} ^ {(i)} (n) f ^ {(i - 1)} (n + 1, E _ {i, j})
$$

$$
\text {   for   } i = 1, 2,..., j - 1 \text {   with   } f ^ {(0)} \equiv 1.
$$

Proof of Theorem 2. Since $G _ { N } ( y , w ) = L _ { N } ( y ) , y _ { N } ( w ) = \cal { D } _ { N }$ and therefore $J _ { N } = 1$ as desired. Assume that the assertions hold for $n + 1$ and in particular $y _ { n + 1 } ( o _ { M } ) = D ( n + 1 , n + J )$ . Note that $y _ { n } ( o _ { M } ) \geq D _ { n }$ n by Proposition 1 and $y _ { n } ( o _ { M } ) { \leq } D _ { n } + y _ { n + 1 } ( o _ { M } ) { = } D ( n , n { + } J )$ by Proposition 5. These observations assure that the minimum of $G _ { n } ( y , w )$ will occur on $\{ D _ { n } , D ( n , n + 1 ) , . . . , D ( n , n + J ) \}$ . Since $G _ { n } ( y , w )$ is convex, the minimum of it is equal to $D ( n , n + J ^ { \prime } )$ , where J′ is the greatest number satisfying

$$
G _ {n} \left(D (n, n + J ^ {\prime}), w\right) \leq G _ {n} \left(D (n, n + J ^ {\prime} - 1), w\right),
$$

which is found by Eq. (7). If J′ = J, then $G _ { n } ( y , w )$ is a decreasing convex function and the order-up-to level for period n is set to its highest possible value (J+1−period demand). However if no such J′ exists then $G _ { n } ( y , w )$ is an increasing convex function and hence $y _ { n } ( o _ { M } ) = D _ { n } .$ □

## References

[1] M.S. Altuğ, A. Muharremoğlu, Inventory management with advance supply information, International Journal of Production Economics 129 (2011) 302–314.

[2] D. Bertsekas, Dynamic Programming: Deterministic and Stochastic Models, Prentice-Hall, Englewood Cliffs, NJ, 1987.

[3] F. Chen, B. Yu, Quantifying the value of leadtime information in a single-location inventory system, Manufacturing & Service Operations Management 7 (2005) 144–151.

[4] F.W. Ciarallo, R. Akella, T.E. Morton, A periodic review production planning model with uncertain capacity and uncertain demand-optimality of extended myopic policies, Management Science 40 (1994) 320–332.

[5] A.S. Erdem, S. Özekici, Inventory models with random yield in a random environment, International Journal of Production Economics 78 (2002) 239–253.

[6] Y. Gerchak, R. Vickson, M. Parlar, Periodic review production models with variable yield and uncertain demand, IIE Transactions 20 (1988) 144–150.

[7] R. Güllü, Base stock policies for production/inventory problems with uncertain capacity levels, European Journal of Operational Research 105 (1998) 43–51.

[8] R. Güllü, E. Önol, N. Erkip, Analysis of a deterministic demand production/inventory system under non-stationary supply uncertainty, IIE Transactions 29 (1997) 703–709.

[9] M. Henig, Y. Gerchak, The structure of periodic review policies in the presence of random yield, Operations Research 38 (1990) 634–643.

[10] A. Hsu, Y. Bassok, Random yield and random demand in a production system with downward substitution, Operations Research 47 (1999) 277–290.

[11] T. Iida, A non-stationary periodic review production-inventory model with uncertain production capacity and uncertain demand, European Journal of Operational Research 140 (2002) 670–683.

[12] M. Jaksic, J.C. Fransoo, T. Tan, A.G. de Kok, B. Rusjan, Inventory management with advance capacity information, Naval Research Logistics 58 (2011) 355–369.

[13] S. Karlin, One stage models with uncertainty, in: K.J. Arrow, S. Karlin, H. Scarf (Eds.), Studies in the Mathematical Theory of Inventory and Production, Standford University Press, Standford, CA, 1958, pp. 109–134.

[14] B. Küçük, A deterministic demand inventory model with advance supply information, Master's thesis, Bogazici University, 2009.

[15] E. Mohebbi, A replenishment model for the supply-uncertainty problem, International Journal of Production Economics 87 (2004) 25–37.

[16] S. Özekici, M. Parlar, Inventory models with unreliable suppliers in a random environment, Annals of Operations Research 91 (1999) 123–136.

[17] M. Parlar, D. Berkin, Future supply uncertainty in EOQ models, Naval Research Logistics 38 (1991) 107–121.

[18] M. Parlar, D. Perry, Inventory models of future supply uncertainty with single and multiple suppliers, Naval Research Logistics 43 (1996) 191–210.

[19] M. Parlar, Y. Wang, Y. Gerchak, A periodic review inventory model with Markovian supply availability, International Journal of Production Economics 42 (1995) 131–136.

[20] E.A. Silver, H.C. Meal, A heuristic for selecting lot size quantities for the case of a deterministic time-varying demand rate and discrete opportunities for replenishment, Production and Inventory Management Journal 2 (1973) 64–74.

[21] J.S. Song, P.H. Zipkin, Inventory control with information about supply conditions, Management Science 42 (1996) 1409–1419.

[22] Y. Wang, Y. Gerchak, Periodic review production models with variable capacity, random yield, and uncertain demand, Management Science 42 (1996) 130–137.

[23] C.A. Yano, H.L. Lee, Lot sizing with random yields: a review, Operations Research 43 (1995) 311–334.

[24] W.M. Yeo, X. Yuan, Optimal inventory policy with supply uncertainty and demand cancellation, European Journal of Operational Research 211 (2011) 26–34.

![](/api/attachments/XRRHSWKX/fulltext/images/533215c08c9631a734c1a4e8b61d0f25032c89eede3634ab3dca006e159fe3d7.jpg)

![](/api/attachments/XRRHSWKX/fulltext/images/b69f149c5937bcfb9c533e46546e791a7332c7b5f461925ef7214689d4101826.jpg)

Bilge Atasoy is a PhD student in TRANSP-OR laboratory at Ecole Polytechnique Fédérale de Lausanne (EPFL). She received her BSc. and MSc. degrees in Industrial Engineering from Boğaziçi University, Turkey. In her MSc. she worked on inventory management models. Now she is working on airline <sup>fl</sup>eet assignment models in the context of her PhD Thesis. She is interested in the impact of a new aircraft methodology, which is designed at EPFL, on the operations of airlines and airports. She is also interested in integrating supply–demand interactions into airline <sup>fl</sup>eet assignment process through advance demand models

Re<sup>fi</sup>k Güllü is a Professor in the Industrial Engineering Department of Bogazici University, Istanbul, Turkey. He received his B.S. and M.S. degrees in Industrial Engineering from the Middle East Technical University, Ankara, Turkey, and M.S. and Ph.D. degrees in Operations Research from the School of ORIE, Cornell University, New York, Dr. Güllü worked at Middle East Technical University as a faculty member before joining Bogazici University. Dr. Güllü's main research interests are stochastic modeling of production/inventory systems, queueing theory, and supply uncertainty problems.

![](/api/attachments/XRRHSWKX/fulltext/images/76a8dd40061eb5b2ebba3daa1390d528d6201e0f0d3264049f0f2b13f31c9ed7.jpg)  
Dr. Tarkan Tan is an Assistant Professor in the School of Industrial Engineering at Eindhoven University of Technology, The Netherlands. Dr. Tan received his Ph.D. in Industrial Engineering from the Middle East Technical University, Ankara, Turkey, in 2002. He pursued one year of his studies toward his Ph.D. degree at Columbia University, Graduate School of Business, Management Science/Operations Research division, New York, as a Fulbright scholar. He joined Eindhoven University of Technology as a post-doc researcher in 2003 and started working as an assistant professor the same year in the Operations, Planning, Accounting, and Control group. He has recently spent an academic term at the University of California, Los Angeles, as a visiting scholar. Dr. Tan is an executive board member of the European Supply Chain Forum. His research interests include inventory theory, capacity management, spare parts management, and supply chain management with a particular focus on the effects of carbon emissions.
