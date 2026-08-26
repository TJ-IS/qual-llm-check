---
otero_id: 568
otero_key: "7SEUV3RY"
title: "An inventory model with capacity flexibility in the existence of advance capacity information"
authors: "Esra Çınar; Refik Güllü"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An inventory model with capacity <sup>fl</sup>exibility in the existence of advance capacity information

Esra Çınar ⁎, Refik Güllü

Boğaziçi University, Department of Industrial Engineering, 34342 Bebek, Istanbul, Turkey

a r t i c l e i n f o

Available online 25 January 2012

Keywords: Advance capacity information Inventory management Outsourcing Order-up-to policy

## a b s t r a c t

In this paper we study the inventory/production problem of a <sup>fi</sup>rm that uses operational level outsourcing to hedge against uncertainty. We consider an environment in which the maximum amount that can be produced in a period, the regular capacity of the system, is uncertain, but information on its realization (which we call the “advance capacity information” (ACI)) is available. We model the uncertainty in regular capacity, and present an ACI process that tracks and updates the information on the availability of the regular capacity. For this system we propose an ACI-dependent order-up-to level policy. We characterize the optimal solution under the order-up-to level policy, and through a numerical study we derive managerial insights with respect to the bene<sup>fi</sup>ts of using outsourcing option and ACI.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In planning and managing inventory/production systems, two main strategies can be used to manage uncertainty: gradually building inventory to hedge against possible future shortages, or temporarily increasing the capacity by purchasing extra capacity. The ability to adjust the total capacity temporarily by acquiring extra resources, such as subcontracting, overtime production, hiring temporary workers, leads to capacity <sup>fl</sup>exibility. In the existence of capacity <sup>fl</sup>exibility, inventory/production related costs may be reduced by managing the capacity and inventory in a joint fashion. We consider an inventory/production system under ACI with <sup>fl</sup>exible capacity, where <sup>fl</sup>exibility is obtained with an outsourcing option to replenish the inventory to reach the target inventory level in any planning period.

The bene<sup>fi</sup>t of using outsourcing can be substantial to hedge against capacity and/or demand uncertainties caused by <sup>fl</sup>uctuating demand, unreliable suppliers, and disruptions in in-house factors such as the work force and machinery. The capacity of a production system can be uncertain due to breakdowns or unplanned maintenance activities of machinery. Also, the resource can be shared by several items, and due to randomness in yield and rework activities, the capacity allocated to an item may exhibit random <sup>fl</sup>uctuations. Ciarallo et al. [6] is the <sup>fi</sup>rst paper in the literature to consider uncertainty in the production/inventory capacity. The objective of this study is to analyze the operational level outsourcing and inventory/ production decision making for a manufacturer with limited uncertain capacity and volatile demand.

Our work is related to the papers in the capacity management literature that attempt to exploit the interactions between capacity planning and inventory/production decisions. Capacity management problems have been studied at different levels of decision making. Research on tactical outsourcing mostly has been concentrated on the strategic questions related to price setting, capacity investing, and contract writing (Yang et al. [20]). Some papers that deal with capacity investing are Rocklin et al. [14], Eberly and VanMieghem [7] and Angelus and Porteus [3]. Rocklin et al. [14] consider a make-toorder system where capacity can be reduced or increased at exogenously set unit prices. For a system where capacity is costly reversible, such as costly labor lay-offs, they give conditions under which the optimal capacity plan is a target interval policy. With the target interval policy it is optimal not to change the capacity as long as it is in the region de<sup>fi</sup>ned by an interval. On the other hand, if the capacity is outside the interval, it is optimal to adjust the capacity to the nearest point on the boundary of the interval. In other words, if the initial capacity is below the lower target limit, then the aim is to bring the capacity up to that limit. And if the initial capacity is above the upper target limit, then the aim is to bring the capacity down to that limit. Otherwise, no capacity changes are made. Eberly and VanMieghem [7] generalize this result to multiple resources with linear or convex adjustment cost functions and concave operating pro<sup>fi</sup>t functions for both <sup>fi</sup>nite and in<sup>fi</sup>nite planning horizons. Angelus and Porteus [3] study optimal capacity and production planning for a make-to-stock system, where capacity can be reduced, as well as added. They consider both short life cycle products and products that can be carried over to future periods, incurring holding costs for the latter. In both cases a target interval policy is shown to be optimal.

They characterize the target intervals for short life cycle products, assuming demand <sup>fi</sup>rst increases stochastically, then decreases.

In these studies capacity expansion and reduction are strategic decisions leading to the ownership of the capacity; there is either a salvage value or price for capacity reduction at the end of each planning period for unsold units/unused capacity. In our setting we do not consider the ownership of the capacity, but consider the usage of the capacity temporarily. The reader is referred to Van Mieghem [19] for a review of the literature on strategic capacity management under uncertainty.

In a contract setting environment Kamien and Li [9] present conditions under which tactical outsourcing mechanisms should be carried out, and they show that such mechanisms have the effect of production smoothing. Van Mieghem [18] uses a game-theoretical model to analyze outsourcing conditions for different types of contracts between a <sup>fi</sup>rm and its subcontractor. Tan [15] analyzes an environment with a capacitated producer and a capacitated subcontractor. The availability of the subcontractor is subject to uncertainty; however, a level of availability is guaranteed by a contract. The producer decides how much to produce and how much to subcontract at a given time using a threshold-type policy that depends on the state of the inventory. Our work is different from this line of work in that we do not consider contracting issues, but we assume that there is a given contract (that sets the price of outsourcing option) with an exogenous supplier.

Bradley [5] considers a continuous time inventory/production model to minimize the average cost. The inventory can be replenished through two possible resources, in-house production and a subcontractor, both with <sup>fi</sup>nite capacity. Assuming that the manufacturer uses a base-stock policy to control replenishment from the two sources, the authors propose using a Brownian approximation of the optimal control problem for determining the <sup>fi</sup>xed capacity level and optimal production quantities. They show through numerical studies the value of the outsourcing option. Tan and Gershwin [17] study a similar continuous-time model with several subcontractors having different unit costs and capacities. We differ from these papers in two respects: (1) we consider a periodic review setting, and (2) we explicitly model capacity uncertainty.

Yang et al. [20] consider a Markovian in-house production capacity, and the outsourcing option with setup cost. They show that the <sup>fi</sup>rm's optimal outsourcing policy is a capacity-dependent (s,S) policy. For the case of deterministic capacity they show that the optimal production policy is a modi<sup>fi</sup>ed base-stock policy. In their study they make the assumption that the outsourcing decision is made before the production decision and the outsourced amount is fully used, whereas in our setting the outsourcing and production decisions are simultaneous, enabling more <sup>fl</sup>exible use of the outsourcing option.

Tan and Alp [16] consider the usage of contingent capacity in terms of temporary workers. Assuming limited contingent and inhouse capacity they show that the optimal operational policy, for any given <sup>fi</sup>xed permanent capacity level, is of state-dependent order-up-to type. In a similar setting Alp and Tan [1] also consider the permanent workforce size to be utilized through the planning horizon as a decision variable. Including <sup>fi</sup>xed costs for both initiating production and for using contingent capacity, they provide the optimal solution to the single-period problem. For the multi-period problem they characterize the optimal policy for some special cases, and argue that the optimal policy does not have a simple form. In Pac et al. [11] this model is extended to include uncertainty in the contingent capacity received from external resources, where a certain number of workers can be guaranteed through contracts at a reservation cost. The decisions are the number of contracted contingent workers, the optimal level of permanent capacity, the number of workers to be hired, and the quantity of production in each period. Pinker and Larson [12] consider a setting where holding inventory is not allowed and the absenteeism of regular workers is expected. The number of regular and contingent workers is <sup>fi</sup>xed for the entire planning horizon, but the capacity is adjusted by using the labor force overtime (both permanent and contingent workers). Mincsovics et al. [10] extend the model in Alp and Tan [1] to include constant lead time associated with the acquisition of contingent capacity. They characterize the optimal policy for the operational decisions and the optimal permanent capacity level. They prove that the inventory, the pipeline contingent capacity, the contingent capacity to be ordered, and the permanent capacity are economic substitutes. The value of <sup>fl</sup>exibility remains considerable even when the capacity acquisition lead time is relatively long.

Obtaining the true optimal policy for a system facing volatile demand in the existence of outsourcing option is dif<sup>fi</sup>cult. Even for a system where the regular capacity is deterministic and stationary, the form of the optimal policy is complicated (Alp and Tan [1]). We propose an ACI-dependent order-up-to level policy with <sup>fl</sup>exible capacity in which whenever the target base-stock level cannot be reached using the currently available capacity at a given period, the short amount can be bought from an exogenous supplier.

Our work also is related to the papers that model advance capacity information. This line of work is more recent and scarce. Altug and Muharremoglu [2] and Jaksic et al. [8] incorporate advance information on capacity in the inventory replenishment problem. In Altug and Muharremoglu [2] advance supply information is available in terms of capacity forecasts provided by the supplier. They model the evolution of the capacity availability forecasts via the Martingale Method of Forecast Evolution, and show that state-dependent basestock policies are optimal. In Jaksic et al. [8] the ACI for a number of future periods is not updated every period, but it is <sup>fi</sup>xed after it has been observed. They show that the optimal ordering policy is a state-dependent modi<sup>fi</sup>ed base-stock policy, and that most bene<sup>fi</sup>ts of using ACI can be reached with only limited future visibility.

In an environment with uncertain capacity, advance information has the potential to improve inventory-related decision making, either by in<sup>fl</sup>ating the order to avoid shortages in future periods, or avoiding unnecessary inventory holding costs. The capacity of the inventory system we consider is the maximum amount that can be produced in a period, which we call the regular capacity of the system. We assume that the regular capacity for the inventory process is uncertain and non-stationary, but the manufacturer observes a signal on its realization in advance.

Our contributions in this paper can be summarized as follows: We <sup>fi</sup>rst model the uncertainty in regular capacity, and present an ACI process that tracks and updates the information on the availability of the regular capacity. Then, we discuss the operating characteristics of the inventory system and propose an ACI-dependent order-up-to level policy. We develop an expression for the average cost of the system, and characterize the optimal solution under the order-up-to level policy. Then using the <sup>fi</sup>rst order conditions and the properties of the optimal solution we describe a solution procedure. Finally, we derive managerial insights through a numerical study. The rest of the paper is organized as follows. We introduce our model in Section 2. The solution procedure is presented in Section 3. The results of the numerical study and the managerial insights are given in Section 4.

## 2. Description of the model

In this section we present and analyze a model where the maximum amount that can be produced in a period (the regular capacity of the system) is uncertain, but information on its realization (which we call the “advance capacity information” (ACI)) is available one period in advance. We <sup>fi</sup>rst model the uncertainty in regular capacity, and present an ACI process that tracks and updates the information on the availability of regular capacity. Then we discuss the operating characteristics of the inventory system and propose an ACI dependent order-up-to level policy.

## 2.1. Modeling capacity uncertainty and the evolution of the ACI process

For the system that we consider the regular capacity for the inventory process is uncertain. Moreover, the distribution of capacity is non-stationary, and in any period n the capacity is realized from one of two possible random variables, $C _ { 1 }$ and $C _ { 2 } .$ . Speci<sup>fi</sup>cally, in a typical period the amount of regular capacity is realized from the random variable $C _ { 1 } ~ ( C _ { 2 } )$ with probability $p \ ( q = 1 - p )$ independent of other period's capacity realization. It is natural to impose some order on these random variables. That ${ \mathrm { i } } s ,$ it is natural to assume that the realizations of regular capacity in some periods are expected to be larger than the capacity realizations in other periods. For instance in weeks where maintenance activities are carried out, or in cases where there are workforce disruptions, the regular capacity realizations are expected to be lower. Without loss of generality we let $C _ { 1 }$ represents $\mathrm { \Delta _ { \mathrm { ~ \AA ~ } } } ^ { \mathrm { \omega _ { h i g h } \prime \prime } }$ regular capacity variable, whereas $C _ { 2 }$ represents $\mathsf { a } \ ^ { \ast } \mathrm { l o w } ^ { \ast }$ capacity variable. One may impose a stochastic ordering on $C _ { 1 }$ and $C _ { 2 }$ by assuming that $C _ { 1 } { \geq } _ { s t } C _ { 2 } ( { \geq } _ { s t }$ means stochastically larger). Let $B _ { j }$ be the distribution function for $C _ { j } , j = 1 , 2$ . Then, we require $B _ { 1 } ( x ) { \overset { } { \leq } } B _ { 2 } ( x )$ for all x. On the other hand, one can also consider a situation where $C _ { j }$ is not a random variable, but a constant, that ${ \mathrm { i } } s ,$ $C _ { j } \equiv c _ { j } , j = 1 , 2$ . In this case, we require $c _ { 1 } \geq c _ { 2 } .$ . We note that, by letting $c _ { 1 } = \infty ,$ , and $c _ { 2 } = 0$ one can model a system where the capacity is either unrestricted, or completely unavailable. We also should note that our setup implies that the number of consecutive periods for which the regular capacity is observed from the “high” distribution is geometrically distributed with parameter p.

In general, at the beginning of a period, before making a decision on how much to order, the system manager does not know the capacity distribution for any of the subsequent periods. In this paper we propose and model a situation where the system has knowledge on the distribution of the capacity for the current and the next period. We note that the particular realization of the capacity is still not known at the time of making a decision, but a window of information availability (the knowledge of the exact distribution) exists, for the current and the next period. Speci<sup>fi</sup>cally, at the beginning of a period $n ,$ the system observes a signal on the availability of the regular capacity in the form of $A C I _ { n } { = } ( j _ { 0 } , j _ { 1 } )$ where $j _ { 0 } \in \{ 1 , 2 \} , j _ { 1 } \in \{ 1 , 2 \}$ , and this advance information reveals that the regular capacity in period n will be realized from the random variable $C _ { j _ { 0 } } ,$ whereas the regular capacity in period $n + 1$ will be realized from the random variable $C _ { j _ { 1 } } .$ As time rolls one period, this information is updated, and ACI at the beginning of period $n + 1$ becomes $A C I _ { n + 1 } = ( j _ { 1 } , J )$ where J is a random variable. $J { = } 1$ with probability $p ,$ and $J { = } 2$ with probability $q = 1 - p .$ . Therefore, the evolution of the advance information, $\{ A C I _ { n } , n = 0 , 1 , \ldots \}$ can be described by a simple Markov chain.

## 2.2. Description of the replenishment policy

As noted before, the amount of inventory that can be replenished by using the regular capacity is restricted. Any shortfall (in excess of the regular capacity) can be purchased from an outside supplier by paying a higher unit cost. We assume that the following order of events takes place in a typical period n.

1. The inventory position at the beginning of the period, $I _ { n } ,$ is observed.

2. ACI information on the availability of the regular capacity, $A C I _ { n } = ( j _ { 0 } , j _ { 1 } )$ , is observed.

3. The replenishment order is placed. The current period's regular capacity, $C _ { j _ { 0 } }$ is realized. If the current period's regular capacity is not suf<sup>fi</sup>cient to ful<sup>fi</sup>ll the order, then the shortfall is acquired from an exogenous supplier at a higher cost.

4. The demand for period $n , D _ { n } ,$ is observed, and inventory holding/ backorder costs are incurred.

We assume that the period length is long enough to justify that the production lead-time is zero. Our aim is to <sup>fi</sup>nd a tractable and easily implementable policy which takes into account the availability of the ACI. To this end we propose an ACI-dependent order-up-to level policy. We should note that obtaining the true optimal policy for the system described above is dif<sup>fi</sup>cult. Even for a system where the regular capacity is deterministic and stationary (that is, ${ \cal C } _ { 1 } \equiv { \cal C } _ { 2 } \equiv c ,$ a constant) form of the optimal policy is complicated (Alp and Tan [1]). In this paper we con<sup>fi</sup>ne ourselves to timestationary order-up-to level policies that partially depend on the observed ACI: if an ACI of $A C I _ { n } = ( j _ { 0 } , j _ { 1 } )$ is observed at the beginning of period n, then the inventory position of that period is raised to the level $S _ { j _ { 1 } }$ (as long as there is no excess inventory from the previous period).

In order to see that an ACI-dependent order-up-to level policy is suitable, consider the following extreme situation. Suppose that in a period the regular capacity is either unrestricted or completely unavailable $( C _ { 1 } \equiv \infty$ and $C _ { 2 } \equiv 0 )$ . If the next period's capacity is $^ { \infty } ,$ then this period's optimum inventory policy is to place an order to raise the inventory level up to the newsvendor solution, which is described in Porteus [13] (since we already know that any amount that we order in the next period will be available). On the other hand, if the next period's capacity is 0, then the order amount should not only cover this period's demand, but also should take into account the (certain) unavailability of the capacity in the next and possibly in the future periods. Therefore any reasonable inventory policy should depend on the observed ACI.

Note that the order-up-to level policy described above does not explicitly depend on the realization of the current capacity, $C _ { j _ { 0 } }$ . If the capacity constraint is a hard constraint (that is, if acquiring the shortfall from an exogenous supplier is not possible), then this form of the order-up-to level would be exact, as the current period's capacity will not have an in<sup>fl</sup>uence on the determination of the orderup-to level (the current period's capacity determines whether this order-up-to level is achievable or not). However, as any shortfall can be ful<sup>fi</sup>lled at the expense of paying a higher cost, the current period's capacity may become important in determining the orderup-to level. In that regard our analysis leads to approximately optimal order-up-to levels. On the other hand, including the full knowledge of capacity information would lead to a model which is quite untractable.

If one imposes a stochastic ordering on $C _ { 1 }$ and $C _ { 2 } \mathsf { a s } C _ { 1 } \mathsf { \geq } _ { s t } C _ { 2 } ,$ , then in an optimal solution $S _ { 1 } { \le } S _ { 2 }$ is expected. In the light of the foregoing discussion, we revise the third term in the order of events that takes place in a period as follows,

3. An order of size $u _ { n } { = } \operatorname* { m a x } \{ S _ { j _ { 1 } } { - } I _ { n } , 0 \}$ is placed. The current period's regular capacity, $C _ { j _ { 0 } }$ is realized. If $u _ { n } > C _ { j _ { 0 } }$ , then the shortfall $u _ { n } - C _ { j _ { 0 } }$ is acquired from an exogenous supplier at a higher cost.

In Fig. 1 we present a schematic description of the order of events that occur in a period. Note that h, b and γ refer to the unit holding backorder and outsourcing costs, respectively.

In our model the order-up-to level takes two values. This is due to the fact that the regular capacity in a period is realized from one of the two possible distributions, and in deciding the order-up-to level we only consider the information on the next period's capacity. The assumption of two possible capacity distributions is suitable in situations where the regular capacity is either severely disrupted or distributed around its usual average respective random durations. A typical example would be $C _ { 2 } \equiv 0$ (complete capacity disruption) and $C _ { 1 }$ represents the capacity random variable when it is not disrupted. In cases where the capacity in a period can be realized from more than two possible distributions, our model can be used as an approximation by grouping possible capacity realizations into two groups.

![](/api/attachments/7SEUV3RY/fulltext/images/0efed67be8e8105bdb94a3e8db7fb8e9f5a9415b5bcc90e6f9d8a25645ff248a.jpg)  
Fig. 1. Order of events.

## 3. Analysis of the model

In this section we develop an expression for the average cost of the inventory system that we described in Section 2, whence one can obtain <sup>fi</sup>rst order optimality equations for the order-up-to levels. Then we discuss the properties of the optimal solution and describe the solution procedure.

## 3.1. Derivation of the average cost function

In obtaining the average cost function we will consider regenerative cycles where without loss of generality the periods of a cycle is indexed as $1 , 2 , \ldots$ Consider the beginning of a cycle in period 1 with $I _ { 1 } = S _ { 2 } ,$ and $A C I _ { 1 } = ( 1 , 2 )$ . A regenerative cycle is de<sup>fi</sup>ned as the evolution of the process until the next time we observe $A C I _ { n } = ( 1 , 2 )$ and raise the inventory level to $I _ { n } { = } S _ { 2 }$ . The length of the renewal interval is de<sup>fi</sup>ned as:

$$
T = \min \left\{n > 1: A C I _ {n + 1} = (1, 2) \right\}.
$$

Note that because of the nature of the process, $T { \geq } 2 \ ( T { = } 2$ occurs i $\mathsf { f } A C I _ { 2 } = ( 2 , 1 )$ and $A C I _ { 3 } = ( 1 , 2 ) )$ . Also let

$$
T _ {1} = \min \left\{n \geq 1: A C I _ {n + 1} = (2, 1) \right\},
$$

as the length of a subinterval for which the order-up-to level stays at $S _ { 2 }$ and switches from $S _ { 2 }$ to $S _ { 1 }$ at the beginning of period $T + 1$ . Also let

$$
T _ {2} = \min \left\{n \geq 1: A C I _ {T _ {1} + n + 1} = (1, 2) \right\}.
$$

Note that $T _ { 1 }$ and $T _ { 2 }$ are geometrically distributed independent random variables with parameters p and $q ,$ respectively. Moreover, $T { = } T _ { 1 } { + } T _ { 2 }$ and clearly $E [ T ] = ( 1 / p ) + ( 1 / q )$ is the expected length of a renewal cycle. If $G ( S _ { 1 } , S _ { 2 } )$ is the expected cost of a renewal cycle (to be derived subsequently), then the average cost per unit time is given by $G ( S _ { 1 } , S _ { 2 } ) / E [ T ]$ , and the aim is to <sup>fi</sup>nd $S _ { 1 }$ and $S _ { 2 }$ that minimize this average cost per period.

Let $D _ { 1 } , D _ { 2 } , \ldots$ be demand realizations for successive periods in a cycle, and de<sup>fi</sup>ne $\begin{array} { r } { D ( k , m ) = \sum _ { i = k } ^ { m } D _ { i } } \end{array}$ for $m \geq k .$ Let $F _ { i } ( x )$ and $F _ { ( k , m ) } ( x )$ be the cumulative distribution function for $D _ { i } ,$ and $D ( k , m )$ , respectively. Although per period demands are stationary random variables, we would like to keep the time related subscripts on the distribution functions for clarity of exposition. Whenever there is no danger of confusion, we will simply write $F ( x )$ for the distribution function of a single period's demand.

Let $\{ C _ { j , i } , i = 1 , 2 , 3 , \ldots \}$ be independent and identically distributed copies of $C _ { j } \mathrm { f o r } j = 1 , 2 . \ : C _ { j , i }$ denotes the capacity random variable associated with the ith period in the cycle, whenever it is of type j. De<sup>fi</sup>ne $\Delta = S _ { 2 } - S _ { 1 } { \geq } 0$

<sup>¼</sup>Whenever the order-up-to level switches from $S _ { 2 }$ to $S _ { 1 }$ (at the beginning of period $T _ { 1 } + 1 )$ , the inventory level may be above $S _ { 1 }$ (recall that $S _ { 1 } { \le } S _ { 2 } )$ . Therefore, it is important to characterize the time at which it is feasible to bring the inventory position up to level $S _ { 1 } .$ For a given value of $T _ { 1 }$ and T de<sup>fi</sup>ne

$$
\tau = \min \{n \in \left\{T _ {1}, T _ {1} + 1, \dots , T \right\}: D \left(T _ {1}, n\right) \geq \Delta \},\tag{1}
$$

as the <sup>fi</sup>rst period on or after $T _ { 1 }$ that the cumulative demand exceeds $\Delta { = } S _ { 2 } { - } S .$ . If no such τ exists $( \mathrm { i f } D ( T _ { 1 } , T ) { < } \Delta )$ then we set $\tau = T .$ Then, <sup>ð Þ</sup>τ determines the <sup>fi</sup>rst period in a cycle in which the inventory level can be raised to the order-up-to level S .

Fig. 2 illustrates a typical sample path of the inventory process for $C _ { i } = c _ { i } , \ i = 1 , 2$ (constant capacity levels). The cycle starts with $A C I _ { 1 } = ( 1 , 2 )$ , where $c _ { 1 }$ is the currently available capacity and $c _ { 2 }$ is the capacity observation for the next period. Hence the inventory level is raised to the base stock level of $S _ { 2 } .$ . Then, for a number of periods we observe $c _ { 2 } " s$ until the <sup>fi</sup>rst time a $c _ { 1 }$ is observed (which leads to $T _ { 1 } )$ . Then, c 's are observed until we observe the next $A C I = ( 1 , 2 )$ and the cycle ends. In Fig. 2 the circles denote the target base-stock levels. As the cycle progresses, the inventory level is increased to its target level in a given period, either using the available regular capacity or by acquiring the shortfall from an outside supplier. Whenever the inventory level is higher than $S _ { 1 } ,$ , while $S _ { 1 }$ is the target inventory level, no action is taken. The <sup>fi</sup>rst time the target inventory shifts from $S _ { 2 }$ to $S _ { 1 }$ is when the <sup>fi</sup>rst time $A C I = ( 2 , 1 )$ is observed.

![](/api/attachments/7SEUV3RY/fulltext/images/1c1a2e1f0ad02726983ccf7787211a2db3d2b62def19dc9623b18a025ebc4aa7.jpg)  
Fig. 2. A renewal cycle.

Our next goal is to characterize the total expected cost of a renewal cycle. Let $L _ { i } ( y )$ be inventory related costs associated with period i:

$$
L _ {i} (y) = h \left(y - D _ {i}\right) ^ {+} + b \left(D _ {i} - y\right) ^ {+},
$$

where h and b are the inventory holding and backorder costs per unit per unit time, respectively, and $( a ) ^ { + } { = } m a x ( a , 0 )$ . The unit cost of acquiring items from an outside supplier is denoted by γ. We do not explicitly consider the unit cost of the regular capacity, but it can easily be included in the analysis. Suppose that $D _ { 1 } , D _ { 2 } , \ldots$ is a given demand sequence, and we are also given $\{ C _ { j , i } , i = 1 , 2 , 3 , \ldots \}$ for $j = 1 , 2$ and the values of $T _ { 1 } \geq 1$ and $T _ { 2 } \ge 1$ (recall that $T = T _ { 1 } + T _ { 2 } ) . \mathrm { A }$ speci<sup>fi</sup>c demand sequence, along with $T _ { 1 }$ determines the value of τ (see Eq. (1)).

Let $\tilde { G } ( S _ { 1 } , S _ { 2 } , T _ { 1 } , T , \tau )$ be the random realization of the total cycle cost for given $T _ { 1 } , T , \tau .$ . Obviously, $\tilde { G } ( S _ { 1 } , S _ { 2 } , T _ { 1 } , T , \tau )$ also depends on <sup>ð Þ</sup>the demand and capacity sequences. We suppress these dependencies in our notation for convenience. Then,

$$
\begin{array}{l} \tilde {G} (S _ {1}, S _ {2}, T _ {1}, T, \tau) = \sum_ {i = 1} ^ {T _ {1} - 1} \Big \{L _ {i} (S _ {2}) + \gamma \Big (D _ {i} - C _ {2, i + 1} \Big) ^ {+} \Big \} + L _ {T _ {1}} (S _ {2}) + \gamma \tilde {g} _ {T _ {1}} 1 _ {\{\tau = T _ {1} \}} \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {\tau} L _ {i} (S _ {2} - D (T _ {1}, i - 1)) + \gamma \sum_ {i = T _ {1} + 1} ^ {T} \tilde {g} _ {i} 1 _ {\{\tau = i \}} \\ \qquad + \sum_ {i = \tau + 1} ^ {T} \{L _ {i} (S _ {1}) + \gamma \tilde {\nu} _ {i} \}, \end{array}\tag{2}
$$

where $1 _ { ( A ) }$ is equal to 1 if A is true, and 0 otherwise, and

$$
\tilde {g} _ {i} = \left\{ \begin{array}{l l} \Big (D _ {T _ {1}} - C _ {2, i + 1} - \Delta \Big) i = T _ {1} \\ \Big (D (T _ {1}, i) - C _ {1, i + 1} - \Delta \Big) ^ {+}   i = T _ {1} + 1,..., T - 1 \\ \Big (D (T _ {1}, T) - C _ {1, i + 1} \Big) ^ {+} & i = T, \end{array} \right.
$$

$$
\tilde {v} _ {i} = \left\{ \begin{array}{l l} \left(D _ {i} - C _ {1, i + 1}\right) ^ {+} & i = \tau + 1,..., T - 1 \\ \left(D _ {T} + \Delta - C _ {1, i + 1}\right) ^ {+} & i = T, \end{array} \right.
$$

with the convention that $\sum { } _ { i = a } ^ { b } = 0$ whenever bba.

We explain Eq. (2) term by term. The renewal cycle starts with the inventory level $S _ { 2 } .$ In the <sup>fi</sup>rst $T _ { 1 } - 1$ periods of the renewal cycle, the ACI for the next period is of type 2 (low capacity). Therefore the inventory is raised to level $S _ { 2 }$ and at the end of period $i { \in } \{ 1 , 2 ,$ $\ldots , T _ { 1 } - 1 \}$ an inventory/backorder cost of $L _ { i } ( S _ { 2 } )$ is incurred. Moreover, at the end of each such period (at the beginning of period i+1) the capacity available is $C _ { 2 , i + 1 }$ , and hence any demand in excess of this capacity level incurs a unit cost of $\gamma .$ This explains the <sup>fi</sup>rst term in the <sup>fi</sup>rst line of $\operatorname { E q . }$ (2). The second term in the <sup>fi</sup>rst line of $\operatorname { E q . } \left( 2 \right)$ is the inventory/backorder cost of period $T _ { 1 } .$ . At the end of period $T _ { 1 }$ the order-up-to level switches to $S _ { 1 }$ and $\mathrm { i f } \tau = T _ { 1 }$ then the starting inventory level at the beginning of period $T + 1$ is $S _ { 1 }$ and a unit cost of γ is paid if $S _ { 1 } - ( S _ { 2 } - D _ { T _ { 1 } } ) = D _ { T _ { 1 } } - \Delta > C _ { 2 , T _ { 1 } + 1 }$ , which explains the last <sup>¼ þ</sup>term in the <sup>fi</sup>rst line of Eq. (2). Next, we explain the second line of Eq. (2). If $\tau { \geq } T _ { 1 } + 1$ inventory related costs of a period $i = \{ T _ { 1 } + 1$ $\ldots , \tau \}$ is $L _ { i } ( S _ { 2 } - D ( T _ { 1 } , i - 1 ) )$ . Moreover, if $\tau { \in } \{ T _ { 1 } { + } 1 , . . . , T \}$ , then the cost of acquiring necessary shortfall from the outside supplier is given by $\gamma \tilde { g } _ { i }$ (regular capacity realizations for these periods are drawn from the random variable $C _ { 1 } )$ . Note that $\tilde { g } _ { T }$ is de<sup>fi</sup>ned differently, as the order-up-to level switches back to $S _ { 2 }$ at the end of period T. The third line of Eq. (2) vanishes if $\tau = T .$ Otherwise, for $i { = } { \tau } { + } 1 , { - } { \ldots } , T ,$ inventory/backorder costs are given by $L _ { i } ( S _ { 1 } )$ , and $\mathrm { f o r } i = \tau + 1 , . . . , T -$ 1 the cost for that period's shortfall is $\gamma \tilde { { v } } _ { i }$ . Since the order-up-to level switches to $S _ { 2 }$ at the end of period T, and the ACI becomes $A C I _ { T + 1 } =$ $( 1 , 2 )$ , a cost of $\gamma ( ( S _ { 2 } - ( S _ { 1 } - D _ { T } ) - \ C _ { 1 , T + 1 } ) ) ^ { + } = \gamma ( \Delta + D _ { T } - C _ { 1 , T + 1 } ) ^ { + } =$ $\gamma \tilde { v } _ { T }$ <sup>ðð ð Þ þ ÞÞ ¼ þ þ ¼</sup>is incurred. This brings the inventory level at the beginning of period $T + 1$ (the beginning of the next renewal cycle) to level $S _ { 2 }$ and the current cycle ends.

By algebraic manipulation, which basically involves rewriting some of the summations in (2), we obtain:

$$
\begin{array}{l} \tilde {G} (S _ {1}, S _ {2}, T _ {1}, T, \tau) = \sum_ {i = 1} ^ {T _ {1} - 1} \Big \{L _ {i} (S _ {2}) + \gamma \Big (D _ {i} - C _ {2, i + 1} \Big) ^ {+} \Big \} + L _ {T _ {1}} (S _ {2}) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} L _ {i} (S _ {2} - D (T _ {1}, i - 1)) 1 _ {\{\tau \geq i \}} - \sum_ {i = T _ {1} + 1} ^ {T} L _ {i} (S _ {1}) 1 _ {\{\tau \geq i \}} \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} L _ {i} (S _ {1}) + \sum_ {i = T _ {1} + 1} ^ {T} \gamma \tilde {\nu} _ {i} - \sum_ {i = T _ {1} + 1} ^ {T} \gamma \tilde {\nu} _ {i} 1 _ {\{\tau \geq i \}} + \sum_ {i = T _ {1}} ^ {T} \tilde {g} _ {i} 1 _ {\{\tau = i \}}. \end{array}\tag{3}
$$

Next, we observe that the event $\{ \tau \geq i \}$ is equal to the event that $\{ D ( T _ { 1 } , i - 1 ) < \Delta \}$ . Therefore, $D _ { i }$ is independent of $1 _ { \{ \tau \geq i \} }$ . Moreover,

$$
E \left[ 1 _ {\{\tau \geq i \}} \right] = P r \{\tau \geq i \} = F _ {(T _ {1}, i - 1)} (\Delta).
$$

De<sup>fi</sup>ne $\mathcal { L } ( y ) = E [ L _ { i } ( y ) ]$ , as the expectation of $L _ { i } ( y )$ over demand. Also let

$$
g _ {i} = E \left[ \tilde {g} _ {i} 1 _ {\{\tau = i \}} \right]\tag{4}
$$

$$
v _ {i} = E [ \tilde {v} _ {i} ],\tag{5}
$$

and

$$
G _ {0} (S _ {1}, S _ {2}, T _ {1}, T) = E \Big [ \tilde {G} (S _ {1}, S _ {2}, T _ {1}, T, \tau) \Big ],\tag{6}
$$

where the expectations in Eqs. $( 4 ) , ( 5 )$ , and (6) are taken over the capacity and demand related random variables (hence τ does not appear anymore). Then,

$$
\begin{array}{l} G _ {0} (S _ {1}, S _ {2}, T _ {1}, T) = \sum_ {i = 1} ^ {T _ {1} - 1} \Big \{\mathcal {L} (S _ {2}) + \gamma E \Big [ \Big (D _ {i} - C _ {2, i + 1} \Big) ^ {+} \Big ] \Big \} + \mathcal {L} (S _ {2}) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} (S _ {2} - x) d F _ {(T _ {1}, i - 1)} (x) + \mathcal {L} (S _ {1}) \sum_ {i = T _ {1} + 1} ^ {T} \Big (1 - F _ {(T _ {1}, i - 1)} (\Delta) \Big) \\ \qquad + \gamma \sum_ {i = T _ {1} + 1} ^ {T} v _ {i} \Big (1 - F _ {(T _ {1}, i - 1)} (\Delta) \Big) + \gamma \sum_ {i = T _ {1}} ^ {T} g _ {i}. \end{array}\tag{7}
$$

Note that, in Eq. (7)

$$
\begin{array}{l} E \Big [ L _ {i} (S _ {2} - D (T _ {1}, i - 1)) 1 _ {\{\tau \geq i \}} \Big ] = \int_ {0} ^ {\Delta} \mathcal {L} (S _ {2} - x) d F _ {(T _ {1}, i - 1)} (x), \\ g _ {T _ {1}} = E \Big [ \Big (D _ {T _ {1}} - C _ {2, T _ {1} + 1} - \Delta \Big) ^ {+} 1 _ {(\tau = T _ {1})} \Big ] = \int_ {y = 0} ^ {\infty} \int_ {x = \Delta + y} ^ {\infty} (x - \Delta - y) d F _ {T _ {1}} (x) d B _ {2} (y), \\ g _ {i} = E \Big [ \Big (D (T _ {1}, i) - C _ {1, i + 1} - \Delta \Big) ^ {+} 1 _ {(\tau = i)} \Big ] \\ = \int_ {y = 0} ^ {\infty} \int_ {x _ {1} = 0} ^ {\Delta} \int_ {x _ {2} = \Delta + y - x _ {1}} ^ {\infty} (x _ {1} + x _ {2} - y - \Delta) d F _ {i} (x _ {2}) d F _ {(T _ {1}, i - 1)} (x _ {1}) d B _ {1} (y), a n d \\ v _ {i} = E \Big [ \Big (D _ {i} - C _ {1, i + 1} \Big) ^ {+} \Big ] = \int_ {y = 0} ^ {\infty} \int_ {x = y} ^ {\infty} (x - y) d F _ {i} (x) d B _ {1} (y), \end{array}\tag{8}
$$

for $i { = } T _ { 1 } { + } 1 , { \ldots } , T { - } 1$ , and

$$
\begin{array}{l} g _ {T} = E \Big [ \Big (D (T _ {1}, T) - c _ {1, T + 1} \Big) ^ {+} 1 _ {(\tau = T)} \Big ] \\ \qquad = \int_ {y = 0} ^ {\infty} \int_ {x _ {1} = 0} ^ {\Delta} \int_ {x _ {2} = y - x _ {1}} ^ {\infty} (x _ {1} + x _ {2} - y) d F _ {T} (x _ {2}) d F _ {(T _ {1}, T - 1)} (x _ {1}) d B _ {1} (y), \\ v _ {T} = E \Big [ \Big (D _ {T} + \Delta - C _ {1, T + 1} \Big) ^ {+} = \int_ {y = 0} ^ {\infty} \int_ {x = y - \Delta} ^ {\infty} (x + \Delta - y) d F _ {T} (x) d B _ {1} (y). \end{array}
$$

Finally, let $G ( S _ { 1 } , S _ { 2 } ) = E [ G _ { 0 } ( S _ { 1 } , S _ { 2 } , T _ { 1 } , T ) ]$ be the expected cost of a renewal cycle, where the last expectation is taken over the random variables $T _ { 1 }$ and T:

$$
G (S _ {1}, S _ {2}) = \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} q ^ {m} p ^ {n} G _ {0} (S _ {1}, S _ {2}, m, n + m).
$$

Then, the optimization problem becomes <sup>fi</sup>nding the values of $S _ { 1 }$ and $S _ { 2 } ,$ that minimize the average cost per period:

$$
\min _ {S _ {1}, S _ {2}} A C P P (S _ {1}, S _ {2}) = \frac {G (S _ {1} , S _ {2})}{E [ T ]}.\tag{9}
$$

## 3.2. Properties of the optimal solution

In this section our objective is to derive various properties of the optimal solution for the problem (9). Unfortunately, the average cost function, $A C P P ( S _ { 1 } , S _ { 2 } )$ is not necessarily jointly convex in $( S _ { 1 }$ $S _ { 2 } )$ . Nevertheless, useful characteristics of an optimal solution can still be derived. We note that the denominator of $A C P P ( S _ { 1 } , S _ { 2 } )$ , E[T], does not depend on $( S _ { 1 } , S _ { 2 } )$ . We also note that any behavior of $G _ { 0 } ( S _ { 1 } , S _ { 2 } , T _ { 1 } , T )$ with respect to $S _ { 1 }$ or $S _ { 2 }$ for a <sup>fi</sup>xed $T _ { 1 }$ and T is preserved in $G ( S _ { 1 } , S _ { 2 } )$ , as $G ( S _ { 1 } , S _ { 2 } )$ is simply a convex combination of countably many $G _ { 0 }$ terms. We make a simple notational transformation and replace $S _ { 2 }$ with Δ in the de<sup>fi</sup>nition of the costs functions. For example, $G _ { 0 } ( S _ { 1 } , S _ { 2 } , T _ { 1 } , T )$ becomes $G _ { 0 } ( S _ { 1 } , \Delta , T _ { 1 } , T )$ . It is more convenient to work with $( S _ { 1 } , \Delta )$ <sup>ð Þ</sup>as decision variable pair, and $S _ { 2 }$ can easily be recovered using $S _ { 2 } = \Delta + S _ { 1 }$

Proposition 1. $A C P P ( S _ { 1 } , \Delta )$ is convex in $S _ { 1 }$ for a given fixed value of $\Delta .$

Proof. The proof of Proposition 1 is in Appendix A, along with the proofs of other Propositions. □

Based on the <sup>fi</sup>rst derivative of $G _ { 0 } ( S _ { 1 } , \Delta , T _ { 1 } , T )$ with respect to $S _ { 1 }$ <sup>ð</sup>(de<sup>fi</sup>ned below), we make two observations.

$$
\begin{array}{l} \partial G _ {0} (S _ {1}, \Delta , T _ {1}, T) / \partial S _ {1} = \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime} (S _ {1} + \Delta) + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} \Big (1 - F _ {(T _ {1}, i - 1)} (\Delta) \Big) \mathcal {L} ^ {\prime} (S _ {1}), \end{array}\tag{10}
$$

Our <sup>fi</sup>rst observation is that, for a given value of Δ the corresponding optimal value of $S _ { 1 }$ does not depend on the capacity random variables $C _ { 1 }$ or $C _ { 2 } .$ Note that we penalize the shortfall from the order-up-to level $S _ { 1 }$ (by paying an expensive unit ordering cost) whenever the capacity is not suf<sup>fi</sup>cient, irrespective of the absolute value of $S _ { 1 }$ . Our second observation involves the behavior of the optimal $S _ { 1 }$ with respect to Δ. By differentiating Eq. (10) with respect to $\Delta$ we obtain:

$$
\begin{array}{l} \partial^ {2} G _ {0} (S _ {1}, \Delta , T _ {1}, T) / \partial S _ {1} \partial \Delta = \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \geq 0. \end{array}
$$

Therefore, optimal $S _ { 1 }$ decreases as Δ increases. The impact of the increase in Δ is to incur increased holding costs. The system decreases $S _ { 1 }$ in order to balance this effect. The convexity result of Proposition 1 enables us to easily compute optimal value o $\mho _ { 1 }$ for a given value of $\Delta .$ .

We infer more properties of the optimal solution by checking the <sup>fi</sup>rst order optimality condition with respect to Δ:

$$
\begin{array}{l} \partial G _ {0} (S _ {1}, \Delta , T _ {1}, T) / \partial \Delta = \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime} (S _ {1} + \Delta) + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \\ \qquad - \int_ {y = 0} ^ {\infty} \gamma (1 - F (\Delta + y)) d B _ {2} (y) \\ \qquad - \gamma \sum_ {i = T _ {1} + 1} ^ {T - 1} \int_ {y = 0} ^ {\infty} \int_ {x _ {1} = 0} ^ {\Delta} \int_ {x _ {2} = \Delta + y - x _ {1}} ^ {\infty} d F (x _ {2}) d F _ {(T _ {1}, i - 1)} (x _ {1}) d B _ {1} (y) \\ \qquad + \gamma \int_ {y = 0} ^ {\infty} (1 - F (y - \Delta)) \Big (1 - F _ {(T _ {1}, T - 1)} (\Delta) \Big) d B _ {1} (y). \end{array}\tag{11}
$$

One immediate consequence of Eq. (11) is the following result on the effect of the “low” capacity random variable.

Proposition 2. Let $C _ { 2 } ^ { a }$ and $C _ { 2 } ^ { b }$ be two random variables, representing two different $" l o w "$ capacity random variables, where $C _ { 2 } ^ { a } \ge _ { s t } C _ { 2 } ^ { b } .$ . Let $\bar { \Delta ^ { a } }$ and $\Delta ^ { b }$ be optimal values for Δ under capacity random variables $C _ { 2 } ^ { a }$ and $C _ { 2 } ^ { b } ,$ respectively. Then, $\varDelta ^ { a } \leq \Delta ^ { b }$

The signi<sup>fi</sup>cance of Proposition 2 is that it enables us to narrow the search space for the optimal Δ as the distribution for $C _ { 2 }$ changes from one data set to another. If we <sup>fi</sup>nd the optimal Δ value for a given random capacity $C _ { 2 } ,$ we know that the optimal $\Delta$ value for a stochastically larger $C _ { 2 }$ cannot be more than the one obtained previously.

By differentiating Eq. (11) with respect to $S _ { 1 }$ we obtain:

$$
\sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta) \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \geq 0,
$$

and therefore we conclude that optimal Δ decreases as $S _ { 1 }$ increases.

## 3.3. A characterization of the optimal solution

We obtain a characterization of the optimal solution to the model (9) whenever the solution satis<sup>fi</sup>es the <sup>fi</sup>rst order optimality equations:

$$
\partial E [ G _ {0} (S _ {1}, \Delta , T _ {1}, T) ] / \partial S _ {1} = 0\tag{12}
$$

$$
\partial E [ G _ {0} (S _ {1}, \Delta , T _ {1}, T) ] / \partial \Delta = 0,\tag{13}
$$

where the expected values are taken over $T _ { 1 }$ and T. Let S<sup>∗</sup> and $S _ { 2 } ^ { * } =$ $\Delta ^ { * } + S _ { 1 } ^ { * }$ be such a solution. First note that

$$
\begin{array}{l} E [ \tau | T _ {1}, T ] = \sum_ {i = 0} ^ {\infty} P r \{\tau > i | T _ {1}, T \} \\ \qquad = \sum_ {i = 0} ^ {T _ {1} - 1} P r \{\tau > i | T _ {1}, T \} + \sum_ {i = T _ {1}} ^ {T - 1} P r \{\tau > i | T _ {1}, T \} \\ \qquad = T _ {1} + \sum_ {i = T _ {1} + 1} ^ {T} P r \{\tau \geq i | T _ {1}, T \} \\ \qquad = T _ {1} + \sum_ {i = T _ {1} + 1} ^ {T} P r \{D (T _ {1}, i - 1) <   \Delta \} = T _ {1} + \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, i - 1)} (\Delta), \end{array}
$$

where the second and the third lines follow by $P r \{ \tau > T | T _ { 1 } , T \} = 0$ and $P r \{ \tau > i | T _ { 1 } , T \} = 1$ for $i { = } 0 , 1 , { \ldots } , T _ { 1 } { - } 1$ <sup>f</sup>. Therefore,

$$
E [ \tau ] = E [ T _ {1} ] + E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, i - 1)} (\Delta) \right].
$$

Then, $\begin{array} { r } { E \Big [ \sum _ { i = T _ { 1 } + 1 } ^ { T } \left( 1 - F _ { ( T _ { 1 } , i - 1 ) } ( \Delta ) \right) \Big ] = \mathrm { E } [ \mathrm { T } ] \mathrm { - E } [ \tau ] . } \end{array}$ . De<sup>fi</sup>ne

$$
\begin{array}{l} H (\Delta) = \int_ {y = 0} ^ {\infty} (1 - F (\Delta + y)) d B _ {2} (y) \\ \quad + E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} \int_ {y = 0} ^ {\infty} P \{D (T _ {1}, i - 1) <   \Delta , D (T _ {1}, i) > y + \Delta \} d B _ {1} (y) \right. \\ \quad \left. - \int_ {y = 0} ^ {\infty} (1 - F (y - \Delta)) \Big (1 - F _ {(T _ {1}, T - 1)} (\Delta) \Big) d B _ {1} (y) \right], \end{array}
$$

so that Eqs. (11) and (13) imply that

$$
E \left[ \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime} \left(S _ {1} ^ {*} + \Delta^ {*}\right) + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta^ {*}} \mathcal {L} ^ {\prime} \left(S _ {1} ^ {*} + \Delta^ {*} - x\right) d F _ {\left(T _ {1}, i - 1\right)} (x) \right] = \gamma H \left(\Delta^ {*}\right).\tag{14}
$$

Similarly, by using Eqs. (10), (12) and (14) we obtain that

$$
\mathcal {L} ^ {\prime} \left(S _ {1} ^ {*}\right) E \left[ \sum_ {i = T _ {1} + 1} ^ {T} \left(1 - F _ {\left(T _ {1}, i - 1\right)} \left(\Delta^ {*}\right)\right) \right] = - \gamma H \left(\Delta^ {*}\right)
$$

Noting that $\mathcal { L } ^ { \prime } ( S _ { 1 } ^ { * } ) = - b + ( h + b ) F ( S _ { 1 } ^ { * } )$ and $E \Big [ \sum _ { i = T _ { 1 } + 1 } ^ { T } ( 1 -$ $ F _ { ( T _ { 1 } , i - 1 ) } ( \Delta ^ { * } ) ) | = E [ T ] { - } E [ \bar { \tau } ]$ we get

$$
F \left(S _ {1} ^ {*}\right) = \frac {b - \gamma R \left(\Delta^ {*}\right)}{h + b}\tag{15}
$$

where $R ( \Delta ^ { * } ) = H ( \Delta ^ { * } ) / ( E [ T ] - E [ \tau ] )$ in Eq. (15). It can be seen that $R ( \Delta ^ { * } ) { \leq } 1 $

$$
\begin{array}{l} (1 - F (\Delta + y)) \leq 1 - F (\Delta), \\ P \{D (T _ {1}, i - 1) <   \Delta , D (T _ {1}, i) > y + \Delta \} \leq 1 - F _ {(T _ {1}, i)} (\Delta), \\ (1 - F (y - \Delta)) \Big (1 - F _ {(T _ {1}, T - 1)} (\Delta) \Big) \geq 0. \end{array}
$$

Therefore, $\begin{array} { r } { H ( \Delta ) \leq E \left[ \sum _ { i = T _ { 1 } } ^ { T _ { 1 } - 1 } \left( 1 - F _ { ( T _ { 1 } , i ) } ( \Delta ) \right) \right] = E \left[ \sum _ { i = T _ { 1 } + 1 } ^ { T _ { 1 } } ( 1 - F _ { ( T _ { 1 } , i - 1 ) } ( \Delta ) ) \right] = } \end{array}$ $E [ T ] { - } E [ \tau ]$ <sup>¼ ¼ þ</sup>. We should stress that E[τ] is also a function of $\Delta ^ { * }$

<sup>- ½ -</sup>Eq. (15) provides us a criteria for testing the quality of any numerical procedure for obtaining a <sup>fi</sup>rst order condition based optimal solution. If the right hand side of Eq. (15) is not close to the left hand side, then we should further seek to improve the current solution in a numerical search method.

Note that for $\gamma = 0 ,$ , Eq. (15) reduces to $\begin{array} { r } { F ( S _ { 1 } ^ { * } ) = \frac { b } { h + b } , } \end{array}$ the newsven-<sup>¼</sup>dor solution. An important special case is given by $C _ { 1 } \equiv \infty$ and $\begin{array} { r } { C _ { 2 } \equiv 0 \colon } \end{array}$ full supply availability and supply disruption durations are respective geometrically distributed random variables. In this case $H ( \Delta )$ simpli<sup>fi</sup>es to $\begin{array} { r } { H ( \Delta ) = 1 - F ( \Delta ) } \end{array}$

We now present upper bounds on the optimal values of Δ and $S _ { 1 }$ Let $S _ { 1 } ^ { U B }$ be the upper bound for $S _ { 1 } ,$ , and $\Delta _ { U B }$ be the upper bound for Δ.

Proposition 3. There exists at least one Δ solving Eq. (16). Let $\Delta _ { U B }$ be the smallest solution of $E q . ( 1 6 )$ . Then, $\varDelta ^ { * } \leq \Delta _ { U B }$ .

$$
E \left[ T _ {1} \right] F (\Delta) + E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T, i)} (\Delta) \right] = \frac {\gamma (E [ T ] - E [ \tau ]) + b E [ \tau ]}{h + b}.\tag{16}
$$

Since we do not have a convexity result with respect to $\Delta ,$ Proposition 3 can be used to limit the search space for the optimum Δ value.

Proposition 4. There exists an upper bound for $S _ { 1 } ,$ , which is equal to the newsvendor solution.

We have shown the existence of upper bounds. And we have shown that, given $\Delta ,$ it is easy to search for $S _ { 1 }$ since the inventory cost is convex in $S _ { 1 }$ and also the <sup>fi</sup>rst order condition does not depend on any of the possible capacity distributions. We also have characterized the <sup>fi</sup>rst order conditions for the optimal solution.

We conclude this section by presenting the solution procedure to find $\Delta ^ { * }$ and S<sub>1</sub><sup>∗</sup>. A similar procedure is used in Babai et al. [4] in a different problem context.

Initialize: Set $\Delta = \Delta _ { U B }$

Step 1. Given Δ, <sup>fi</sup>nd the corresponding optimal $S _ { 1 }$ by using the golden section search method on $[ 0 , S _ { 1 } ^ { U B } ]$

Step 2. STOP if $S _ { 1 }$ and $\Delta$ found in Step 1 satis<sup>fi</sup>es Eq. (15). Otherwise, set $\Delta = \Delta - \varepsilon$ (for small ε) and GO TO Step 1.

## 4. Numerical analysis

In this section we present the results of our computational study that we have conducted to gain insights into the effects of using ACI and outsourcing on the costs. We <sup>fi</sup>rst present the experimental setting used in the numerical study, then we describe how the value of using outsourcing and ACI are evaluated, present and discuss our numerical <sup>fi</sup>ndings.

## 4.1. Experimental setting

For the numerical study we use Gamma distributed random demand with varying mean, $\mu _ { D } { \in } ( 3 , 4 , 5 , 7 )$ , and standard deviation, $\sigma _ { D } \in ( 1 , 3 , 5 )$ . Gamma distribution allows us to control the mean and variation of demand. We <sup>fi</sup>x the backorder cost to $b = 1 0$ and the holding cost to $h = 1$ , and vary the unit outsourcing cost, γ, with $\gamma \in ( 0 , 5 , 1 0 , 1 5 )$ , to see the relative effect of these costs. We choose the cost parameters b and h so as to obtain a high service level, b being considerably higher than h. And in another case we <sup>fi</sup>x b and $\gamma ,$ and vary h to see its effect on the percent cost reductions, with $h \in ( 2 , 3 , 4 , 5 )$

For the capacities $C _ { 1 }$ and $C _ { 2 }$ we consider deterministic values with $\boldsymbol { C } _ { 1 } \equiv \boldsymbol { c } _ { 1 }$ and $C _ { 2 } \equiv c _ { 2 } .$ . We use <sup>fi</sup>ve different levels for the probability of having high capacity, $p { \in } ( 0 . 1 , 0 . 3 , 0 . 5 , 0 . 7 , 0 . 9 )$ , and one of the following values of $c _ { 1 }$ and $c _ { 2 } , c _ { 1 } \in ( 6 , 1 2 , 2 0 )$ , and $c _ { 2 } \in ( 0 , 4 )$ , We choose $c _ { 1 }$ and $c _ { 2 }$ to alter the capacity utilization and to observe how the utilization level affects the value of ACI and outsourcing. With these parameters we cover a wide range of capacity utilization. For example, for $p { = } 0 . 1 , c _ { 1 } { = } 6$ and $c _ { 2 } = 4 ,$ , the expected capacity 4.2. And if $\mu _ { D } = 5 ,$ then the expected demand is approximately 20% higher than the expected regular capacity of a period. We choose <sup>fi</sup>xed values for $C _ { 1 }$ and $C _ { 2 }$ to be able to eliminate the effect of variability of the capacity in a period, given that it is realized from high or low distribution.

The case where $C _ { 1 } \equiv 2 0$ and ${ \cal C } _ { 2 } \equiv 0 ,$ , for example, is representative of a case where the capacity is either unrestricted or completely unavailable for the demand parameters that we use.

In our experiments we use a combination of a set of input parameters to see their effects on the value of ACI and value of outsourcing. We provide explanations to our results. We only present a subset of our numerical observations, but our <sup>fi</sup>ndings are veri<sup>fi</sup>ed through several experiments.

We use Monte Carlo simulation to calculate the average costs of the systems we consider in our experiments. With Monte Carlo simulation multiple trial runs are obtained using randomly generated capacity and demand values in each period. We simulate the inventory system for 1500 periods to compute the average costs.

## 4.2. Value of outsourcing

We study the bene<sup>fi</sup>t of using the outsourcing option under different parameters. Value of outsourcing is de<sup>fi</sup>ned as the percent cost decrease caused by using the outsourcing opportunity. To evaluate the value of outsourcing we compare the costs of the ACI-dependent base-stock policy we propose in this paper to a policy where ACI is observed, but there is no outsourcing option. For the latter policy we exhaustively search for the base-stock levels $S _ { 1 }$ and $S _ { 2 }$ since no optimality conditions can be de<sup>fi</sup>ned for them. The value of outsourcing, $V 0 ,$ is de<sup>fi</sup>ned as follows:

$$
V O = 1 0 0 \frac {A C P P ^ {I} - A C P P ^ {F}}{A C P P ^ {I}},
$$

where $A C P P ^ { F }$ is the average cost of the <sup>fl</sup>exible system that has an outsourcing option, and $A C P P ^ { I }$ is the average cost of the in<sup>fl</sup>exible system with no outsourcing option.

The percent cost savings due to the outsourcing opportunity under various parameters are given in Table 1. From this table one can observe that very high cost reductions are possible due to outsourcing. When outsourcing is more expensive VO decreases, having the highest value at $\gamma = 0 .$ Another important factor that determines the value of outsourcing is the capacity utilization, $\mu _ { D } / \mu _ { C }$ . When the capacity utilization is signi<sup>fi</sup>cantly less than 1 (when the availability of the regular capacity is high), the outsourcing option is not very needed and it is used less, and the difference between the costs of the two systems becomes smaller. The difference is insigni<sup>fi</sup>cant in some cases, especially when the variance of capacity is also not high. This can be observed from Table 1, for example, for $c _ { 1 } = 1 2$ $c _ { 2 } = 4 , p = 0 . 3$ and $( \mu _ { D } , \sigma _ { D } ) = ( 5 , 5 )$ . We also observe that the value of the outsourcing option increases quickly as the demand level increases, for the same capacity parameters, for example, for capacity parameters $c _ { 1 } = 1 2 , c _ { 2 } = 0$ and $p { = } 0 . 5$

For similar utilization values we observe from our experimental results that as the variation of capacity increases the value of outsourcing also increases. For example, for the same demand parameters and similar utilization values of $\mu _ { D } / \mu _ { C } = 5 / 6 . 4$ and $\mu _ { D } / \mu _ { C } = 5 / 6$ , as the coef<sup>fi</sup>cient of variation of capacity, $c v _ { C } { = } { \sigma } _ { C } / \mu _ { C }$ , increases from 0.57 (for $c _ { 1 } = 1 2 , c _ { 2 } = 4 , p = 0 . 3 )$ to 1 (for $c _ { 1 } = 1 2 , c _ { 2 } = 0 , p = 0 . 5 )$ VO also increases. The explanation is that when the variation of capacity is high the inventory level of the system with no outsourcing option becomes very high, and this system incurs high inventory costs. On the other hand, when the availability of the capacity is low and its variance is high, this system incurs both high inventory holding and penalty costs.

The outsourcing option is also more valuable when inventory costs are higher, again since the in<sup>fl</sup>exible system carries too much inventory. This is illustrated in Fig. 3, where VO is plotted for varying cost parameters with $h \in ( 2 , 3 , 4 , 5 )$ and $\gamma { \in } ( 5 , 7 , 9 , 1 1 , 1 3 )$ , for the following demand and capacity parameters, $( \mu _ { D } = 5 , \sigma _ { D } = 5 )$ and $( c _ { 1 } = 1 2 , c _ { 2 } = 4 , p = 0 . 5 )$

VO for different levels of γ and cost parameters

<table><tr><td colspan="4"> $c_1=12\ c_2=0\ p=0.5$ </td><td colspan="4"> $c_1=12\ c_2=0\ p=0.7$ </td></tr><tr><td> $(\mu_D,\sigma_D)=$ </td><td>(5,1)</td><td>(5,3)</td><td>(5,5)</td><td> $(\mu_D,\sigma_D)=$ </td><td>(5,1)</td><td>(5,3)</td><td>(5,5)</td></tr><tr><td> $\gamma=0$ </td><td>95.58</td><td>86.90</td><td>84.67</td><td> $\gamma=0$ </td><td>84.60</td><td>68.97</td><td>50.86</td></tr><tr><td>5</td><td>73.90</td><td>72.20</td><td>68.79</td><td>5</td><td>53.54</td><td>43.64</td><td>23.66</td></tr><tr><td>10</td><td>58.49</td><td>51.16</td><td>56.48</td><td>10</td><td>35.61</td><td>24.56</td><td>2.70</td></tr><tr><td>15</td><td>47.49</td><td>41.95</td><td>45.52</td><td>15</td><td>16.48</td><td>5.42</td><td>0.24</td></tr><tr><td colspan="4"> $c_1=12\ c_2=0\ p=0.5$ </td><td colspan="4"> $c_1=12\ c_2=4\ p=0.3$ </td></tr><tr><td> $(\mu_D,\sigma_D)=$ </td><td>(3,3)</td><td>(4,3)</td><td>(5,3)</td><td> $(\mu_D,\sigma_D)=$ </td><td>(5,1)</td><td>(5,3)</td><td>(5,5)</td></tr><tr><td> $\gamma=0$ </td><td>56.71</td><td>74.71</td><td>86.90</td><td> $\gamma=0$ </td><td>75.42</td><td>65.47</td><td>69.44</td></tr><tr><td>5</td><td>25.76</td><td>45.93</td><td>72.20</td><td>5</td><td>36.29</td><td>38.19</td><td>45.74</td></tr><tr><td>10</td><td>5.93</td><td>20.61</td><td>51.16</td><td>10</td><td>4.97</td><td>2.02</td><td>25.01</td></tr><tr><td>15</td><td>2.76</td><td>1.77</td><td>41.95</td><td>15</td><td>2.17</td><td>1.28</td><td>0.70</td></tr></table>

## 4.3. Value of ACI

We also check the possible percentage cost improvements achieved by using one-period ahead ACI, for a <sup>fl</sup>exible system with the outsourcing option. We compare the costs of the ACI-dependent base-stock policy we propose in this paper to a policy where inventory is managed by an optimal interval policy, also using the outsourcing option. With the interval policy (where capacity reduction is not allowed) the inventory level, I, is brought to be between the extremities of the interval $S _ { 1 }$ and $S _ { 2 } ,$ with $S _ { 2 } { > } S _ { 1 }$ , whenever possible. The short amount is outsourced if $\dot { \boldsymbol { S } } _ { 1 }$ cannot be reached, and no action is taken if $I { \ge } S _ { 2 }$ . This also can be seen as a modi<sup>fi</sup>ed base-stock policy with a target level equal to $S _ { 2 } ,$ where the inventory is not allowed to be lower than $S _ { 1 }$ . Since there is no optimality conditions for the optima $S _ { 1 }$ and $S _ { 2 } ,$ we search for them exhaustively. Since the capacity information is not observed, we take c, the average expected capacity, as the capacity level. The target inventory level for this policy, y, is given as follows,

$$
y = \left\{ \begin{array}{c c} S _ {1} & I _ {n} \leq S _ {1} - c \\ I + c & S _ {1} - c \leq I \leq S _ {2} - c \\ S _ {2} & S _ {2} - c \leq I \leq S _ {2} \\ I & S _ {2} \leq I \end{array} \right.
$$

![](/api/attachments/7SEUV3RY/fulltext/images/67d06d093af26e65ca014fb0efb86968ff2b3c2939fc876b8bbcdc79f58de8bf.jpg)  
Fig. 3. VO as a function of outsourcing and holding costs.

Table 4

We de<sup>fi</sup>ne the value of using ACI, VACI, as the percent cost decrease caused by using the ACI, which we calculate as follows:

$$
V A C I = 1 0 0 \frac {A C P P ^ {n o A C I} - A C P P ^ {A C I}}{A C P P ^ {n o A C I}},
$$

where $A C P P ^ { A C I }$ is the average cost of the system that works under ACI, and $A C P P ^ { n o A C I }$ is the average costs of the system that does not observe ACI. Note that, since both systems considered in this section use outsourcing option, we can consider cases where the utilization of capacity, μ /μ , is higher than 1.

Some numerical results for the value of ACI are given in Tables 2, 3 and 4. Having the capacity information even for one-period ahead can result in signi<sup>fi</sup>cant cost reductions, especially when the cost of outsourcing, γ, is high. The value of observing capacity information increases as γ increases.

For a given capacity, as the mean demand increases VACI changes according to the utilization level. For example, when the utilization is increased from $\mu _ { D } / \mu _ { C } = 3 / 1 0 . 8$ to 5/10.8 VACI increases. But then further increasing $\mu _ { D } / \mu _ { C }$ to 7/10.8 VACI decreases, since there is not as much capacity <sup>fl</sup>exibility to use the obtained information by changing the ordering decisions. In a similar, way when capacity is <sup>fl</sup>exible enough to alter the ordering decision, for example when $\mu _ { D } / \mu _ { C } = 3 /$ 6, increasing it to $5 / 6 ,$ , and further to $7 / 6 ,$ results in an increase in VACI. These results can be observed from Table 2.

We also analyze the relation between VACI and capacity variability. This relation also depends on the capacity utilization level. Given the demand parameters, as the capacity variation increases VACI increases as long as the utilization is not too high. This is due to the fact that there is not enough <sup>fl</sup>exibility to react to the observed information. And given the expected value of the capacity, the increase in the capacity variance always results in an increase in VACI. These can be observed from Table 3: $p { = } 0 . 5$ yields a system where capacity variability is higher as compared to $p { = } 0 . 9 ,$ , and also given γ and p, the capacity variability increases as $\left( c _ { 1 } , c _ { 2 } \right)$ moves from (12, 4) to (20, 4) and further to (12, 0). Although the optimal interval policy does not take ACI into account, it is expected to perform well when the capacity is not too variable. And in fact it can perform better than the ACI-dependent base-stock policy.

VACI for different levels of γ, p and μ for $c _ { 1 } = 1 2 , c _ { 2 } = 0$ and $\sigma _ { D } = 3 .$

<table><tr><td rowspan="2"></td><td colspan="4"> $c_1=12\ c_2=0$ </td></tr><tr><td> $(\mu_D,\sigma_D)$ </td><td>(3, 3)</td><td>(5, 3)</td><td>(7, 3)</td></tr><tr><td>p=0.5</td><td>γ=0</td><td>0.51</td><td>0.03</td><td>3.50</td></tr><tr><td rowspan="3"> $μ_C=6$ </td><td>5</td><td>15.73</td><td>20.76</td><td>30.50</td></tr><tr><td>10</td><td>23.99</td><td>26.07</td><td>52.79</td></tr><tr><td>15</td><td>26.94</td><td>29.42</td><td>56.29</td></tr><tr><td>p=0.9</td><td>0</td><td>0.03</td><td>0.27</td><td>0.08</td></tr><tr><td rowspan="3"> $μ_C=10.8$ </td><td>5</td><td>6.57</td><td>11.25</td><td>7.55</td></tr><tr><td>10</td><td>13.00</td><td>20.23</td><td>12.76</td></tr><tr><td>15</td><td>17.32</td><td>25.67</td><td>19.33</td></tr></table>

VACI for different levels of γ, p and cost parameters for $\mu _ { D } = 5$ and $\sigma _ { D } = 3 .$

<table><tr><td rowspan="2"></td><td colspan="4"> $\mu_D=5\sigma_D=3$ </td></tr><tr><td> $(c_1,c_2)$ </td><td>(12,4)</td><td>(20,4)</td><td>(12,0)</td></tr><tr><td rowspan="4">p=0.5</td><td>γ=0</td><td>0.72</td><td>0.66</td><td>0.03</td></tr><tr><td>5</td><td>6.27</td><td>8.85</td><td>20.76</td></tr><tr><td>10</td><td>11.25</td><td>16.32</td><td>26.07</td></tr><tr><td>15</td><td>13.62</td><td>22.27</td><td>29.42</td></tr><tr><td rowspan="4">p=0.9</td><td>0</td><td>0.68</td><td>0.81</td><td>0.27</td></tr><tr><td>5</td><td>2.15</td><td>5.03</td><td>11.25</td></tr><tr><td>10</td><td>3.41</td><td>11.24</td><td>20.23</td></tr><tr><td>15</td><td>4.09</td><td>16.66</td><td>25.67</td></tr></table>

VACI for different levels of γ, p and $\sigma _ { D }$ for $c _ { 1 } = 1 2 , c _ { 2 } = 0$ and $\mu _ { D } = 5 .$

<table><tr><td rowspan="2"></td><td colspan="4"> $c_1=12\ c_2=0$ </td></tr><tr><td> $(\mu_D,\sigma_D)$ </td><td>(5, 1)</td><td>(5, 3)</td><td>(5, 5)</td></tr><tr><td rowspan="4">p=0.1</td><td>γ=0</td><td>6.54</td><td>0.87</td><td>0.41</td></tr><tr><td>5</td><td>2.38</td><td>3.51</td><td>3.15</td></tr><tr><td>10</td><td>3.73</td><td>4.98</td><td>4.02</td></tr><tr><td>15</td><td>5.34</td><td>5.38</td><td>4.56</td></tr><tr><td rowspan="4">p=0.3</td><td>0</td><td>5.86</td><td>0.03</td><td>0.33</td></tr><tr><td>5</td><td>26.62</td><td>20.76</td><td>12.57</td></tr><tr><td>10</td><td>35.70</td><td>26.07</td><td>16.32</td></tr><tr><td>15</td><td>38.86</td><td>29.42</td><td>19.99</td></tr></table>

As the variation of demand increases, both systems react by increasing the associated inventory levels that characterize the optimal solutions. But since our solution tries to achieve base-stock levels while the interval policy only tries to stay in the interval range (and probably incurring less outsourcing cost, since it does not always try to reach the higher boundary of the interval), the bene<sup>fi</sup>t of ACI can be smaller when the demand variability is high. Our results showing how VACI changes as demand variability increases can be seen in Table 4 for $c _ { 1 } = 1 2$ and $c _ { 2 } = 0$

## 5. Conclusion

In this paper we study an inventory/production system under Advance Capacity Information with <sup>fl</sup>exible capacity, where <sup>fl</sup>exibility is obtained with an outsourcing option to replenish the inventory to reach the target inventory level in any planning period. Since obtaining the optimal policy for the system with outsourcing option and ACI is dif<sup>fi</sup>cult, we propose an ACI-dependent order-up-to level policy.

We model the ACI as a signal on the regular capacity distribution, where information is updated every planning period. We develop an expression for the average cost, from which one can obtain <sup>fi</sup>rst order optimality equations for the order-up-to levels. Then using the <sup>fi</sup>rst order conditions and the properties of the optimal solution we describe a solution procedure. Through a numerical analysis we show conditions under which the outsourcing option and ACI are more valuable. We show that observing information is more valuable when the utilization of the regular capacity is neither too low nor too high. Then the system can take advantage of the observed ACI. The value of both outsourcing and ACI are higher whenever the variability of the capacity is high.

In this paper we consider one-period ahead ACI, specifying the distribution of the regular capacity from two alternatives. A possible extension to this study could be a case where ACI is available for a general number of future periods, or a case where capacity can be realized from a general number of possible distributions. Modeling these extensions is not too dif<sup>fi</sup>cult, but the derivation of the average cost per period and the computation of the order-up-to policies are considerably harder. Speci<sup>fi</sup>cally, our approach, which is based on obtaining the average cost expression, cannot be easily extended to a case where information is available for more than two periods. Intuitively, the information on the capacity of the most immediate future period should have the greatest impact on the inventory decision. Therefore, as a future research direction one can think of heuristic approaches that combine our model with a simpler treatment of capacity information on the further away periods.

We note that an unlimited amount can be outsourced at the <sup>fi</sup>xed unit cost γ. This may not be realized in some practical applications. We can extend our model by incorporating an increasing and convex ordering cost γ(x), (where x is the amount outsourced) in order to re-<sup>fl</sup>ect that it becomes marginally more dif<sup>fi</sup>cult to outsource as x increases.

## Acknowledgments

The authors are thankful to the guest editors for an ef<sup>fi</sup>cient review process. We would like to thank the reviewers for their helpful comments and suggestions. This research is partially funded by the Bogazici University Research Fund (BAP) Project 08HA302-D.

## Appendix A. Proofs of the Propositions

Proof of Proposition 1. It is suf<sup>fi</sup>cient to show the convexity of $G _ { 0 } ( S _ { 1 } , \Delta , T _ { 1 } , T ) \big ] ,$ , as E[T] does not depend on the decision variables, and the sum of convex functions is convex. Then,

$$
\begin{array}{l} \partial G _ {0} (S _ {1}, \Delta , T _ {1}, T) / \partial S _ {1} = \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime} (S _ {1} + \Delta) + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} \Big (1 - F _ {(T _ {1}, i - 1)} (\Delta) \Big) \mathcal {L} ^ {\prime} (S _ {1}), \end{array}\tag{A.1}
$$

where $\begin{array} { r } { \mathcal { L } ^ { \prime } ( y ) = - b + ( b + h ) F ( y ) } \end{array}$ . Taking one more derivative:

$$
\begin{array}{l} \partial^ {2} G _ {0} (S _ {1}, \Delta , T _ {1}, T) / \partial S _ {1} ^ {2} = \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta) + \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime \prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \\ \qquad + \sum_ {i = T _ {1} + 1} ^ {T} \Big (1 - F _ {(T _ {1}, i - 1)} (\Delta) \Big) L ^ {\prime \prime} (S _ {1}) \geq 0, \end{array}
$$

since $\begin{array} { r } { \mathcal { L } ^ { ' \prime } ( y ) = ( b + h ) d F ( y ) { \geq } 0 } \end{array}$ , and this establishes the convexity of <sup>L</sup>APPC in $S _ { 1 }$ <sup>Þ ¼ ð Þþ ð Þ</sup>for a <sup>fi</sup>xed value of $\Delta , \sqsubset$

Proof of Proposition 2. We <sup>fi</sup>rst note that $C _ { 2 }$ affects $\partial G _ { 0 } ( S _ { 1 } , \Delta , T _ { 1 } , T ) / \partial \Delta$ through the expectation on the second line of <sup>ð</sup>Eq. (11). Let $B _ { 2 } ^ { a } ( x )$ and $B _ { 2 } ^ { b } ( x )$ be distribution functions for C<sup>a</sup> and $C _ { 2 } ^ { b } ,$ respectively. Since $( 1 - F ( \Delta + y ) )$ is a decreasing function of $y ,$ and $C _ { 2 } ^ { a } \geq _ { s t } C _ { 2 } ^ { b }$ we have

$$
- \int_ {y = 0} ^ {\infty} \gamma (1 - F (\Delta + y)) d B _ {2} ^ {a} (y) \geq - \int_ {y = 0} ^ {\infty} \gamma (1 - F (\Delta + y)) d B _ {2} ^ {b} (y),
$$

for all $\Delta \geq 0 ,$ , and the claim follows. Intuitively, if the realizations of capacity get smaller (stochastically), then the corresponding optimal $\Delta$ gets larger in order to avoid incurring excessive shortfall costs. □

Proof of Proposition 3. We consider terms of equation $\partial E [ G _ { 0 } ( S _ { 1 } , \Delta ,$ $T _ { 1 } , T ) ] / \partial \Delta$ (see Eq. (11)) one by one and bound them: (1) Since $\mathcal { L } ^ { \prime } ( y )$ is an increasing function

$$
E \left[ \sum_ {i = 1} ^ {T _ {1}} \mathcal {L} ^ {\prime} (S _ {1} + \Delta) \right] \geq E [ T _ {1} ] \mathcal {L} ^ {\prime} (\Delta).
$$

(2) The second term:

$$
\begin{array}{l} E \left[ \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime} (S _ {1} + \Delta - x) d F _ {(T _ {1}, i - 1)} (x) \right] \geq E \left[ \sum_ {i = T _ {1} + 1} ^ {T} \int_ {0} ^ {\Delta} \mathcal {L} ^ {\prime} (\Delta - x) d F _ {(T _ {1}, i - 1)} (x) \right] \\ = - b E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, i - 1)} (\Delta) \right] + (h + b) E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, 1)} (\Delta) \right] \\ = - b (E [ \tau ] - E [ T _ {1} ]) + (h + b) E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, i)} (\Delta) \right]. \end{array}
$$

(3) The third term:

$$
\int_ {y = 0} ^ {\infty} \gamma (1 - F (\Delta + y)) d B _ {2} (y) \leq \gamma (1 - F (\Delta)).
$$

(4) The fourth term:

$$
\begin{array}{l} \gamma E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} \int_ {y = 0} ^ {\infty} \int_ {x _ {1} = 0} ^ {\Delta} \int_ {x _ {2} = \Delta + y - x _ {1}} ^ {\infty} d F (x _ {2}) d F _ {(T _ {1}, i - 1)} (x _ {1}) d B _ {1} (y) \right] \\ = \gamma E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} \int_ {y = 0} ^ {\infty} P r \{D (T _ {1}, i - 1) \leq \Delta , D (T _ {1}, i) \geq y + \Delta \} d B _ {1} (y) \right] \\ \leq \gamma E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} P r \{\Delta , D (T _ {1}, i) \geq \Delta \} \right] = \gamma E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} \left(1 - F _ {(T _ {1}, i)} (\Delta)\right) \right]. \end{array}
$$

(5) For the last term:

$$
\gamma \int_ {y = 0} ^ {\infty} (1 - F (y - \Delta)) \left(1 - F _ {(T _ {1}, T - 1)} (\Delta)\right) d B _ {1} (y) \geq 0.
$$

Combining the right hand sides and the left hand sides of the inequalities and noting that

$$
E \left[ \sum_ {i = T _ {1} + 1} ^ {T - 1} \left(1 - F _ {\left(T _ {1}, i\right)} (\Delta)\right) \right] + (1 - F (\Delta)) = E \left[ \sum_ {i = T _ {1}} ^ {T - 1} \left(1 - F _ {\left(T _ {1}, i\right)} (\Delta)\right) \right] = E [ T ] - E [ \tau ]
$$

yields

$$
\partial E [ G _ {0} (S _ {1}, \Delta , T _ {1}, T) ] / \partial \Delta \geq G _ {L B} ^ {\prime},
$$

where

$$
\begin{array}{l} G _ {L B} ^ {\prime} (\Delta) = E [ T _ {1} ] \mathcal {L} ^ {\prime} (\Delta) - b (E [ \tau ] - E [ T _ {1} ]) \\ \qquad + (h + b) E \left[ \sum_ {i = T _ {1} + 1} ^ {T} F _ {(T _ {1}, i)} (\Delta) \right] - \gamma (E [ T ] - E [ \tau ]). \end{array}
$$

$G _ { L B } ^ { \prime } ( \Delta )$ is continuous in $\Delta , G _ { L B } ^ { \prime } ( \Delta ) {  } { - } b E [ T _ { 1 } ] { - } { \gamma } ( E [ T ] { - } E [ T _ { 1 } ] ) { < } 0$ as $\Delta \to 0$ <sup>ð</sup>(since $E [ \tau ]  E [ T _ { 1 } ] )$ , and $G _ { L B } ^ { \prime } ( \Delta ) {  } h E [ T ] > |$ <sup>-</sup>0 as $\Delta \to \infty$ <sup>½ -</sup>(since $E [ \tau ] \to E [ T ] )$ <sup>ð Þ</sup>Therefore, there is a solution to $G _ { L B } ^ { \prime } ( \Delta ) = 0$ . Let $\Delta _ { U B }$ be the smallest solution. The claim and $\operatorname { E q . }$ <sup>ð Þ ¼</sup>. (16) follow by rearranging $G _ { L B } ^ { \prime } ( \Delta ) . \square$

Proof of Proposition 4. Since $S _ { 1 }$ is decreasing inΔ it can take its highest value at $\Delta = 0 .$ . We have shown that given Δ the inventory cost is convex in $S _ { 1 } ,$ <sup>¼</sup>, hence $S _ { 1 }$ can be found from the following <sup>fi</sup>rst order condition,

$$
\begin{array}{l} \partial E [ G _ {0} (S _ {1}, \Delta , T _ {1}, T) ] / \partial S _ {1} = \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} q ^ {m} p ^ {n} \partial G _ {0} (S _ {1}, \Delta , m, n) / \partial S _ {1} \\ = \sum_ {m = 1} ^ {\infty} \sum_ {n = 1} ^ {\infty} q ^ {m} p ^ {n} \sum_ {i = 1} ^ {m} \mathcal {L} ^ {\prime} (S _ {1} + \Delta) + \sum_ {i = m + 1} ^ {n} \int_ {0} ^ {\Delta} \mathcal {L} (S _ {1} + \Delta - x) d F _ {(m, i - 1)} (x) \\ + \sum_ {i = m + 1} ^ {n} \Big (1 - F _ {(m, i - 1)} (\Delta) \Big) \mathcal {L} ^ {\prime} (S _ {1}) = 0. \end{array}
$$

For $\Delta = 0$ the <sup>fi</sup>rst order condition becomes,

$$
\partial E \left[ G _ {0} \left(S _ {1}, \Delta , T _ {1}, T\right) \right] / \partial S _ {1} = \sum_ {n = 1} ^ {\infty} p ^ {n} \sum_ {i = 1} ^ {n} \mathcal {L} ^ {\prime} \left(S _ {1}\right) = \mathcal {L} ^ {\prime} \left(S _ {1}\right) \sum_ {n = 1} ^ {\infty} p ^ {n} n = 0.
$$

From this equation we can conclude that the upper bound $S _ { 1 } ^ { U B }$ is equal to the newsvendor solution. □

## References

[1] O. Alp, T. Tan, Tactical capacity management under capacity <sup>fl</sup>exibility, IIE Transactions 40 (2008) 221–237.

[2] M.S. Altug, A. Muharremoglu, Inventory management with advance supply information, International Journal of Production Economics 129 (2011) 302–313.

[3] A. Angelus, E.L. Porteus, Simultaneous capacity and production management of short-life-cycle, produce-to-stock goods under stochastic demand, Management Science 48 (2002) 399–413.

[4] M.Z. Babai, Z. Jemai, Y. Dallery, Analysis of order-up-to-level inventory systems with compound poisson demand, European Journal of Operational Research 210 (2011) 552–558.

[5] J.R. Bradley, A brownian approximation of a production-inventory system with a manufacturer that subcontracts, Operations Research 52 (2004) 765–784.

[6] F.W. Ciarallo, R. Akella, T.E. Morton, A periodic review, production planningmodel with uncertain capacity and uncertain demand — optimality of extended myopic policies, Management Science 40 (1994) 320–332.

[7] J.C. Eberly, J.A. VanMieghem, Multi-factor dynamic investment under uncertainty, Journal of Economic Theory 75 (1997) 345–387.

[8] M. Jaksic, J.C. Fransoo, T. Tan, A.G. de Kok, B. Rusjan, Inventory management with advance capacity information, Naval Research Logistics 58 (2011) 355–369.

[9] M.I. Kamien, L. Li, Subcontracting, coordination, <sup>fl</sup>exibility, and production smoothing in aggregate planning, Management Science 36 (1990) 1352–1363.

[10] G. Mincsovics, T. Tan, O. Alp, Integrated capacity and inventory management with capacity acquisition lead times, European Journal of Operational Research 196 (2009) 949–958.

[11] M.F. Pac, O. Alp, T. Tan, Integrated workforce capacity and inventory management under labour supply uncertainty, International Journal of Production Research 47 (2009) 4281–4304.

[12] E.J. Pinker, R.C. Larson, Optimizing the use of contingent labor when demand is uncertain, European Journal of Operational Research 144 (2003) 39–55.

[13] E.L. Porteus, Foundations of Stochastic Inventory Theory, Stanford University Press, Stanford, CA, 2002.

[14] S.M. Rocklin, A. Kashper, G.C. Varvaloucas, Capacity expansion contraction of a facility with demand augmentation dynamics, Operations Research 32 (1984) 133–147.

[15] B. Tan, Subcontracting with availability guarantees: production control and capacity decisions, IIE Transactions 36 (2004) 711–724.

[16] T. Tan, O. Alp, An integrated approach to inventory and <sup>fl</sup>exible capacity management subject to <sup>fi</sup>xed costs and non-stationary stochastic demand, OR Spectrum 31 (2009) 337–360.

[17] B. Tan, S.B. Gershwin, Production and subcontracting strategies for manufacturers with limited capacity and volatile demand, Annals of Operations Research 125 (2004) 205–232.

[18] J.A. Van Mieghem, Coordinating investment, production, and subcontracting Management Science 45 (1999) 954–971.

[19] J.A. Van Mieghem, Capacity management, investment, and hedging: review and recent developments, Manufacturing and Service Operations Management 5 (2003) 269–302.

[20] J. Yang, X.T. Qi, Y.S. Xia, A production-inventory system with Markovian capacity and outsourcing option, Operations Research 53 (2005) 328–349.

![](/api/attachments/7SEUV3RY/fulltext/images/40e7dab9f56e0748029454c93aa35362d1049a2bd2ed14a93778be4d19b8f834.jpg)  
Esra Çinar is a PhD candidate of Industrial Engineering at Bogaziçi University, Istanbul, Turkey. She received her B.S. degree in Industrial Engineering from Galatasaray University, and M.S. degree in Industrial Engineering from Bogaziçi University. Her current research interests are inventory modeling and healthcare management.

![](/api/attachments/7SEUV3RY/fulltext/images/c4c388a99ea4ff91d27bfed4ddec2916181829667ac3c49f0b9cfed9094cd0ad.jpg)

Re<sup>fi</sup>k Güllü is a Professor in the Industrial Engineering Department of Bogaziçi University, Istanbul, Turkey. He received his B.S. and M.S. degrees in Industrial Engineering from the Middle East Technical University, Ankara, Turkey, and M.S. and Ph.D. degrees in Operations Research from the School of ORIE, Cornell University, New York. Dr. Güllü worked at Middle East Technical University as a faculty member before joining Bogaziçi University. Dr. Güllü's main research interests are stochastic modeling of production/inventory systems, queueing theory, and supply uncertainty problems.
