---
otero_id: 4762
otero_key: "NKZ3UA48"
title: "A stochastic, contingency-based security-constrained optimal power flow for the procurement of energy and distributed reserve"
authors: "Carlos E. Murillo-Sánchez; Ray D. Zimmerman; C. Lindsay Anderson; Robert J. Thomas"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.04.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve ☆

Carlos E. Murillo-Sánchez <sup>a</sup>, Ray D. Zimmerman <sup>b</sup>, C. Lindsay Anderson <sup>b,</sup>⁎, Robert J. Thomas <sup>b</sup>

<sup>a</sup> National University of Colombia, Manizales, Colombia <sup>b</sup> Cornell University, Ithaca, NY 14853, United States

## a r t i c l e i n f o

Article history: Received 23 March 2012 Received in revised form 22 March 2013 Accepted 23 April 2013 Available online xxxx

Keywords: Electricity markets Power systems Smart grid Stochastic optimization Reserve market Responsive reserves

## a b s t r a c t

It is widely agreed that optimal procurement of reserves, with explicit consideration of system contingencies, can improve reliability and economic ef<sup>fi</sup>ciency in power systems. With increasing penetration of uncertain generation resources, this optimal allocation is becoming even more crucial. Herein, a problem formulation is developed to solve the day-ahead energy and reserve market allocation and pricing problem that explicitly considers the redispatch set required by the occurrence of contingencies and the corresponding optimal power <sup>fl</sup>ow, static and dynamic security constraints. Costs and bene<sup>fi</sup>ts, including those arising from eventual demand deviation and contingency-originated redispatch and shedding, are weighted by the contingency probabilities, resulting in a scheme that contracts the optimal amount of resources in a stochastic day-ahead procurement setting. Furthermore, the usual assumption that the day-ahead contracted quantities correspond to some base case dispatch is removed, resulting in an optimal procurement as opposed to an optimal dispatch. Inherent in the formulation are mechanisms for rescheduling and pricing dispatch deviations arising from realized demand <sup>fl</sup>uctuations and contingencies. Because the formulation involves a single, one stage, comprehensive mathematical program, the Lagrange multipliers obtained at the solution are consistent with shadow prices and can be used to clear the day-ahead and spot markets of the different commodities involved.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

This work combines several standard problems found in systems operation and planning in a single mathematical programming framework. The advantages of this formulation are found in greater clarity with respect to the underlying problem to be solved, and for ease of extraction of sensitivity information from the solution. The problems herein considered are

• The optimal power <sup>fl</sup>ow problem with a full AC nonlinear network model and constraints;

• The N − 1 contingency security problem with both static (postcontingency voltage and MVA limits) and dynamic (generator ramp rate limits; voltage angle difference limits; post-contingency load pickup governed by participation factors) constraints;

• The problem of procuring an adequate supply of both active and reactive power and corresponding geographically adequate distributed reserves in a day-ahead market scenario in light of the uncertainty of the actual realized demand and the occurrence of speci<sup>fi</sup>c contingencies, while taking into account the costs and constraints on the corresponding post-contingency <sup>fl</sup>ows;

• The problem of setting the price for the day-ahead contracts for power and reserve; and

• A consistent mechanism for re-dispatching and pricing the next day under a speci<sup>fi</sup>c realization of the set of all uncertain quantities involved.

Each of these problems is usually tackled separately, in a sequential process that revises the original dispatch produced by an optimal power <sup>fl</sup>ow solver to accommodate the additional restrictions. However, the sequential nature of typical practice does not ensure that these are introduced in a way that preserves optimality for the overall problem, nor allows for the original LBMPs to be used correctly for pricing both active and reactive power and reserve, or for understanding the price of security. The approach employed here tries to accommodate as many of the issues involved as possible in a single, consistent mathematical program, avoiding the use of proxies of the constraints. The speci<sup>fi</sup>c novelty in this work lies in 1) the decoupling of the concept of day-ahead programmed dispatch and day-ahead contracted quantity, resulting in an optimal day-ahead hedge for the system operator; 2) a single stage, comprehensive problem formulation for energy and

## Nomenclature

<table><tr><td> $p_{ik}, q_{ik}$ </td><td>ith active and reactive injection in kth post-contingency state (k=0 for base case).</td></tr><tr><td> $C_{Pi}(\cdot), C_{Qi}(\cdot)$ </td><td>cost function for ith active and reactive injections.</td></tr><tr><td> $p_{ci}, q_{ci}$ </td><td>purchase amounts specified in the day-ahead contract for active and reactive power from the ith injection.</td></tr><tr><td> $p_{ik}^{+}, q_{ik}^{+}$ </td><td>ith active and reactive upward deviations from contracted amount in kth post-contingency state; k=0 means realized deviation from contract with no contingencies.</td></tr><tr><td> $C_{Pi}^{+}(\cdot), C_{Qi}^{+}(\cdot)$ </td><td>cost for incremental deviations from contract day-ahead quantity.</td></tr><tr><td> $p_{ik}^{-}, q_{ik}^{-}$ </td><td>ith active and reactive downward deviations from contracted amount in kth post-contingency state.</td></tr><tr><td> $C_{Pi}^{-}(\cdot), C_{Qi}^{-}(\cdot)$ </td><td>cost for decremental deviations from contracted day-ahead quantity.</td></tr><tr><td> $r_{Pi}^{+}, r_{Qi}^{+}$ </td><td>upward active and reactive reserve amount provided by ith injection.</td></tr><tr><td> $C_{RPi}^{+}(\cdot), C_{RQi}^{+}(\cdot)$ </td><td>cost functions for upward reserve purchased from ith injection.</td></tr><tr><td> $r_{Pi}^{-}, r_{Qi}^{-}$ </td><td>downward active and reactive reserve amount provided by ith injection.</td></tr><tr><td> $C_{RPi}^{-}(\cdot), C_{RQi}^{-}(\cdot)$ </td><td>cost functions for downward reserve purchased from ith injection.</td></tr><tr><td> $(\Theta^{k}, V^{k}, P^{k}, Q^{k})$ </td><td>voltage angles and magnitudes, active and reactive injections for power flow in kth post-contingency state (k=0 means no contingency occurred).</td></tr><tr><td> $g^{k}(\cdot)$ </td><td>nonlinear power flow equations in kth post-contingency state.</td></tr><tr><td> $h^{k}(\cdot)$ </td><td>transmission, voltage, generation and other limits in kth post-contingency state.</td></tr><tr><td> $\pi_{k}$ </td><td>probability of kth contingency ( $\pi_{0}$  is the probability of no contingency).</td></tr><tr><td> $n_{g}$ </td><td>number of generators and dispatchable or curtailable loads initially available.</td></tr><tr><td> $n_{c}$ </td><td>number of contingencies considered.</td></tr><tr><td> $G^{k}$ </td><td>set of indices of generators present in the kth contingency. Individual variables can be grouped in vectors, such as  $p_{ik}$  into  $P^{k}$ , and it will be consistent with the context.</td></tr></table>

reserve allocation that is appropriate for extraction of sensitivity information important to microeconomics, namely, meaningful locationbased shadow prices. The resulting problem is formidable to solve but it exhibits a structure that is amenable to decomposition and coordination approaches to its solution, making a parallel implementation possible and desirable.

Secure operation of generation and transmission systems addresses a plethora of issues. It involves planning so that the system can survive the occurrence of certain kinds of events, most notably so-called “contingencies”, in which a piece of equipment goes of<sup>fl</sup>ine suddenly. But it also involves planning so that the system can continue to perform if the operating conditions expected at the decision-making moment do not materialize exactly, i.e. if there is uncertainty in the prediction of load, climate, wind or river <sup>fl</sup>ow. Of these two types of issues, perhaps the <sup>fi</sup>rst results in more acute concerns, because a sudden realization of a contingency disturbs the state of the system before much can be done by the operators.

Several events occur in different time frames after a contingency. First, new bus voltages can be reached in a matter of seconds as the transient governed by automatic reactive controls takes place. If the controls steer the voltage towards a stable equilibrium, it still remains to be seen if the overall voltage pro<sup>fi</sup>le that is reached is appropriate. In a longer time scale involving tens of seconds, frequency controls steer generators to balance the active power and make up for lost generation or load. Under-frequency relays may trigger network recon<sup>fi</sup>guration events in extreme cases at this stage. In a time frame of a few minutes, area exchange controls balance deviations from scheduled transactions, and operator-originated redispatches start to take place. In some cases, an automatic redispatch is initiated right after the contingency in order to improve the security and economy of the initial post-contingency operating point.

A key planning decision is the amount and location of spinning reserve that must be set aside for eventual use in case of a contingency. The required redispatches might not be feasible otherwise. Thus, correctly solving the planning problem requires addressing the issue of geographically appropriate reserve allocation. Furthermore, correct pricing of this commodity requires that it be explicitly included in the formulation.

A taxonomy of system states with respect to security is offered in [1]. The normal state is that of “secure”, when no operating limits are violated and no limits would be violated in the event of a contingency. Secure operation requires planning with respect to credible contingencies in order to both position the current state accordingly and to plan for corrective rescheduling strategies in the event that one of them does occur. There are many approaches to solving this problem, depending on the formulation, the simpli<sup>fi</sup>cations, the available tools, and on the numerical method used. Some are only approximate in light of the simpli<sup>fi</sup>cations, e.g. DC <sup>fl</sup>ow instead of AC <sup>fl</sup>ow, and require further examination before claiming that the solution is engineering-feasible. Others do not produce accurate pricing information due to the nature of the solution method employed, or the use of proxy constraints instead of precise models of the physical limitations. One key criterion is whether the approach is 1) direct, 2) base <sup>fl</sup>ow data modi<sup>fi</sup>cationbased or 3) base <sup>fl</sup>ow with added self-contained constraints. The <sup>fi</sup>rst approach is used, for example, in [2–12] and involves actual simultaneous formulation of the post-contingency <sup>fl</sup>ows with additional constraints that bound the deviations of the injections in the post-contingency <sup>fl</sup>ows from those in the base case. These are the only coupling constraints; voltage security and rating limits are imposed directly on the postcontingency <sup>fl</sup>ows. Clearly, as more contingencies are considered the problem's size becomes formidable and it is tempting to exploit the problem structure with a decomposition framework, typically a price coordination scheme such as Benders' decomposition or Lagrangian relaxation, among others.

The second idea relies on modi<sup>fi</sup>cation of the original problem data for the base case OPF so as not to violate limits in a post-contingency state. A typical example is to arti<sup>fi</sup>cially reduce the rating in a transmission line or the maximum generation capacity in a given unit to alleviate a congestion problem that would occur in a post-contingency state. This is amenable to sequential modi<sup>fi</sup>cation of a base case OPF after a given OPF solution is analyzed and found to be insecure with respect to contingencies. However, the order in which contingencies are studied might be important in determining the <sup>fi</sup>nal secure dispatch, which raises the possibility of not <sup>fi</sup>nding the true optimum.

The third idea adds more constraints to the base case OPF to force the resulting solution to be secure. Like the second approach, it is amenable to sequential introduction of constraints into the base OPF, dictated by an analysis of the security of a given solution. These new constraints may typically be linearizations of the constraints that were violated in a post-contingency <sup>fl</sup>ow, and are thus proxies that may not be entirely accurate.

We now discuss some of the ingredients of the overall problem and how they have been dealt with over the years. Every now and then, reference will be made to speci<sup>fi</sup>c MATPOWER implementation conventions and algorithms. This stems from the fact that this software package's generalized optimal power <sup>fl</sup>ow capabilities have been taken advantage of in order to code the prototype implementation. A detailed description of its capabilities and algorithms can be found in [13,14].

C.E. Murillo-Sánchez et al. / Decision Support Systems xxx (2013) xxx–xxx

## 1.1. Modeling post-contingency constraints

Survival of a contingency implies a state trajectory that does not exceed system ratings or operating limits and which reaches an equilibrium that does not violate any limits. Then, the system can be steered towards a more economical and secure operating point with the resources available. The initial response is automatic, as voltage, frequency and automatic generation controls respond to errors. Assuming that no dynamic instability occurs, the <sup>fi</sup>nal resting point is easy to predict when the ramp rates, participation factors, scheduled area interchanges and voltage setpoints are known. It takes a load <sup>fl</sup>ow with a particular form of distributed slack to solve this [15]. In this work, a direct approach (as explained earlier) is employed, meaning that all of the post-contingency situations are modeled by speci<sup>fi</sup>c load <sup>fl</sup>ows that join the overall problem formulation. Once the variables de<sup>fi</sup>ning those <sup>fl</sup>ows are incorporated, they become available to impose coupling constraints such as ramp rates on them, as well as normal voltage, generator capability and transmission capacity limits for the postcontingency solution. This is different from continuation load <sup>fl</sup>ow approaches to voltage security such as [16].

If post-contingency load shedding is a possibility, then such loads are modeled as price-responsive loads with their <sup>fi</sup>rst block priced at the same level as the value of lost load. This is consistent with a welfare maximization problem formulation.

## 1.2. Modeling dispatchable generation limits

Most previous works model the generation limits using box bounds on the active and reactive output. True generator capability curves, however, come from the intersection of several curves, each arising from physical limits being reached in a speci<sup>fi</sup>c component of the generator [17]. A trapezoidal approximation to these curves is employed in the underlying MATPOWER [13] OPF formulation which is closer to true generator capability curves.

## 1.3. Market-based offer specification

In market-based scheduling settings, offers for both generation and curtailable loads are usually structured in blocks at a given price, not as a polynomial cost. Block-based costs resulting in convex piece-wise linear cost functions are dealt with by internally adding new linear constraints and variables using the capability of the generalized OPF solver in MATPOWER; this is transparent to the user. The speci<sup>fi</sup>c method employed de<sup>fi</sup>nes one cost variable $y _ { i }$ for each generator or load with block-based costs, which is added to the problem's cost functional, and then constraints of the form

$$
y _ {i} \geq m _ {j} p _ {i} + b _ {j}, \quad j = 1... \# \text {   of   cost   segments   }\tag{1}
$$

are formulated, resulting in a convex feasible region for $( y _ { i } , p _ { i } )$ . The minimization process drives (y ,p ) against the boundary, which is exactly the cost curve; see [13,18] for further details. Of course, also allows polynomial costs and these two representations can both be present in a given problem.

## 1.4. Responsive load and load shedding specification

The generalized formulation employed in allows the speci<sup>fi</sup>cation of price-responsive loads as negative injections. For welfare maximization, the negative of the bene<sup>fi</sup>t function can be speci<sup>fi</sup>ed; market bids are assumed otherwise (Fig. 1). Thus, a load demand as in Fig. 2 can be converted to an injection offer. Because a load's reactive consumption cannot be dispatched, price-responsive injections with negative active power are assumed to exhibit a constant power factor. This models the behavior of such loads more accurately and is a standard feature in .

![](/api/attachments/NKZ3UA48/fulltext/images/e59f683847663e00ea18fd9d1c6b49996c75462eef72ea7252712603844bbbc9.jpg)  
Fig. 1. Demand curve.

Load shedding can be modeled by specifying a demand curve whose <sup>fi</sup>rst block's price corresponds to that of the value of lost load. This approach is appropriate for maximization of social welfare, where the value of lost load should be taken into account. If the actual value of lost load should not be allowed to set the nodal prices at the solution, an alternative approach is to use whatever price caps are in effect in the market. This models load shedding in a setting in which the consumers are not compensated.

It should be noted, however, that true load shedding is a non-convex problem; normally, if the <sup>fi</sup>rst block in a load's demand curve is made price-responsive to model load shedding, this does not mean that there is an ability to dispatch it half-way through; in a normal OPF setting the solution algorithm might try to split the block. This would require an adjustment to the post-contingency <sup>fl</sup>ow in order to shed the whole block.

## 1.5. Reserve allocation in a day-ahead setting

Secure dispatch and post-contingency rescheduling require that resources be available for redispatch if needed. Traditional security rules include the $N - 1$ spinning reserve criterion for each control area, in which the amount of reserve must be enough to cover the loss of the largest generation unit. Other rules specify 10 and 30 minute reserve as a percentage of the load being served. Non-integrated market approaches such as [19,20] require pre-speci<sup>fi</sup>ed amounts of reserve to

![](/api/attachments/NKZ3UA48/fulltext/images/39e809cfc1748f3dc667c984bd562fbe7f7ac065cc7836995c502f0da527a197.jpg)  
Fig. 2. Equivalent offer for an injection.

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

![](/api/attachments/NKZ3UA48/fulltext/images/9f1e59bb655f7933f4dc9222a2908c81a0b47fac7ed61870c1f140dc266e642e.jpg)  
Fig. 3. General tree structure for representation of transitions

be met, usually divided by zones. However, the true locational aspect of reserve has not always been addressed. The reserve resources must have an appropriate geographic distribution to be able to harness their energy should it be needed if a contingency occurs. Works such as [5–7] address exactly this issue, as opposed to, for example [21–23], in which an integrated market is optimized but the reserve amounts to be met are speci<sup>fi</sup>ed in a zone by zone basis, not a contingency analysis-originated basis. The direct formulation approach used there, without simpli<sup>fi</sup>cation of network constraints, is helpful for obtaining solutions that need no further adjustment. The approach suggested in [5] simply provides a solution from which it is feasible to transition to any of the post-contingency states considered; the raison d'être for reserve is implicit in the dispatch itself. In [6,7], the concept of reserve amount and reserve contract is introduced, so that reserve markets can be designed, and a full AC <sup>fl</sup>ow setting is employed. This work expands [7] to consider both upward and downward excursions as “reserve”, albeit of a different kind, as well as reactive reserve. This makes it easier to integrate the approach to a day-ahead marketbased scheduling framework in which there must be a real time follow-through. Other efforts have included [24–27] with a linear <sup>fl</sup>ow formulation.

## 1.6. Receding horizon, stochastic transition and cost framework

Security-constrained OPF models that rely on explicit formulation of post-contingency <sup>fl</sup>ows can be thought of as multi-scenario planning models with coupling constraints. These constraints are there to model transition-related limits, ramp rates in particular. This suggests a tree structure for the problem, the branches representing both transitions and coupling constraints. This approach has been suggested explicitly in the setting of unit commitment algorithms [28] but is certainly inherent in other “direct” treatments of the securityconstrained OPF. In fact, this approach can be generalized further by allowing several tree structures in a single problem. This way, more than one probability-weighted “base case” can be considered, each with corresponding contingency-originated transitions and constraints, also probability-weighted. The probability weightings used here can be computed from individual equipment failure rates and line outage probabilities based also on weather prediction, as well as historic data.

The proposed scheme can be useful to model high-load and lowload predictions in addition to the central 24 hour-ahead load prediction. Of course, this adds to the dimension of the problem. An example of such a tree is shown in Fig. 3, which considers two base cases, with two contingencies considered for each. Here, an additional re<sup>fi</sup>nement has been introduced in that the transition to a post-contingency state can be modeled in two stages if necessary, the <sup>fi</sup>rst being the immediate post-contingency state of the system, after voltage controls have acted, but before AGC has had a chance to correct frequency and area interchange; and a second and <sup>fi</sup>nal stage in which economic redispatch is assumed to have taken place.

In the proposed scheme, the cost of operation for every scenario is weighted by its probability of occurrence, making the problem one of constrained stochastic optimization. This makes economic sense as it solves for the least expected cost of procurement.

One could certainly consider $( N - 2 ) { \mathrm { - t y p e } }$ contingencies sprouting from each of the terminal N − 1 contingency nodes, but it is clear that the dimensionality of the problem would become unmanageable with both current and envisioned computing capabilities. Even when the ramp limits are ignored and a linear (DC) network model is used as in [29], N − 2 security results in huge mathematical programs.

This approach, in which the transition direction is important, is different from that considered in [6,7], where the redispatch amount needed to transition between any two considered scenarios is bounded to be less than the available “ramp rate”. Thus the formulation in this work is less conservative.

A related view of the problem is that of a receding-horizon optimal stochastic control problem. The N 1 security translates to a onestage horizon from the moment that the control actions are implemented, and the 24 hour-ahead planning translates to a 24-hour control delay. The probabilities employed in the formulation are those estimated day-ahead, which will certainly be different from those in real time, when there is little uncertainty about the load level and the weather. It is important to recognize this because the realized system state one day later is bound to be at least slightly different from the central day-ahead prediction, i.e. the base case. Thus, for completeness of the problem, any real-time or spot rescheduling mechanisms must be taken into account in the day-ahead planning. That is the reason why in this work additional costs on deviations from the contracted day-ahead quantity are employed; these must be provided by participants in the market at the same time that they offer in the day-ahead energy and reserve market.

## 1.7. Base case dispatch vs. optimal

A major feature of the proposed formulation is that the day-ahead contract quantities are not constrained to be equal to the base case dispatch. Rather, additional contracted quantity variables together with several sets of inequalities involving the incremental dispatches, reserve variables and actual base and post-contingency dispatches are employed. This offers more <sup>fl</sup>exibility in selecting a day-ahead optimal contract to the independent system operator. In integrated, cooptimized markets this <sup>fl</sup>exibility is actually needed in some cases to be able to reach an optimum hedge. When the contracted quantities are set to be equal to the base case dispatch, the shadow prices on energy may require modi<sup>fi</sup>cation and the system cost can increase.

The remainder of the paper is organized as follows: Section 2 poses the formulation of the day-ahead problem; Section 3 analyzes the Lagrangian and shadow prices relationships; Section 4 analyzes the real-time redispatch adjustment, Section 5 discusses a test implementation based on and Section 6 presents some preliminary numerical results using the IEEE 30-bus and 118-bus systems. Finally, conclusions and closure are offered in Section 7.

## 2. Day-ahead problem formulation

For simplicity of notation, we consider a tree with only one root, namely, the base case. More subindices would be required for

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

additional roots, perhaps replacing k by $k ^ { j } ,$ , with j being the root index. The functional to minimize is the expected cost

$$
\min_{\substack{\theta ,V,P,Q,\\ P^{+},P^{-},Q^{+},Q^{-},\\ P_{c},Q_{c},R_{P},R_{Q}}}f_{P}(P) + f_{Q}(Q) + f_{RP}(R_{P}) + f_{RQ}\left(R_{Q}\right)\tag{2}
$$

where the active power cost component is

$$
f _ {P} (P) = \sum_ {k = 0} ^ {n _ {c}} \pi_ {k} \sum_ {i \in G ^ {k}} \left[ C _ {P i} \left(p _ {i k}\right) + C _ {P i} ^ {+} \left(p _ {i k} ^ {+}\right) + C _ {P i} ^ {-} \left(p _ {i k} ^ {-}\right) \right],\tag{3}
$$

with three sub-components. Here, $\pi _ { k }$ is the probability of transition to the kth contingency from the day-ahead base case; $C _ { P i } ( p _ { i k } )$ is the production cost or offer for the ith generator in the kth contingency; $C _ { P i } ^ { + } ( p _ { i k } ^ { + } )$ is an incremental cost, additional to the production cost, on upward deviations from the quantity that is contracted for in the day-ahead market. Similarly, $C _ { P i } ^ { - } ( p _ { i k } ^ { - } )$ is an additional cost imposed on downward deviations from the day-ahead contract. These costs allow generators to signal a reluctance to vary their power output from the contracted day-ahead quantities, which can be valid for some types of base load units. Likewise, the reactive power cost is

$$
f _ {Q} (Q) = \sum_ {k = 0} ^ {n _ {c}} \pi_ {k} \sum_ {i \in G ^ {k}} \left[ C _ {Q i} (q _ {i k}) + C _ {Q i} ^ {+} \Big (q _ {i k} ^ {+} \Big) + C _ {Q i} ^ {-} (q _ {i k} ^ {-}) \right],\tag{4}
$$

the active reserve cost is

$$
f _ {R P} (R _ {P}) = \sum_ {i = 1} ^ {n _ {g}} \left[ C _ {R P i} ^ {+} \left(r _ {P i} ^ {+}\right) + C _ {R P i} ^ {-} \left(r _ {P i} ^ {-}\right) \right],\tag{5}
$$

and the reactive reserve cost is

$$
f _ {R Q} (R _ {Q}) = \sum_ {i = 1} ^ {n _ {g}} \left[ C _ {R Q i} ^ {+} \left(r _ {Q i} ^ {+}\right) + C _ {R Q i} ^ {-} \left(r _ {Q i} ^ {-}\right) \right].\tag{6}
$$

Here, upward and downward reserves de<sup>fi</sup>ne a dispatch range relative to the day-ahead contracted quantities, $( p _ { c i } , q _ { c i } )$

All of this is subject to nonlinear active and reactive power <sup>fl</sup>ow constraints in the base case <sup>fl</sup>ow and all contingencies,

$$
g _ {P} ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) = 0, \quad k = 0 \dots n _ {c},\tag{7}
$$

$$
g _ {Q} ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) = 0, \quad k = 0... n _ {c},\tag{8}
$$

transmission capacity, generation capability curve, voltage limit, dispatchable load power factor, and maximum angular separation constraints for all <sup>fl</sup>ows,

$$
h ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) \leq 0, \quad k = 0 \dots n _ {c},\tag{9}
$$

and new, additional constraints that couple the base case and the post-contingency <sup>fl</sup>ows, de<sup>fi</sup>ning the deviation variables and the reserve variables, as illustrated in Fig. 4. The <sup>fi</sup>rst three such constraints de<sup>fi</sup>ne upward deviations from contract quantity and upward reserves.

$$
0 \leq p _ {i k} ^ {+} \quad 0 \leq q _ {i k} ^ {+} \quad \forall i, k\tag{10}
$$

$$
p _ {i k} - p _ {c i} \leq p _ {i k} ^ {+} q _ {i k} - q _ {c i} \leq q _ {i k} ^ {+} \forall i, k
$$

$$
p _ {i k} ^ {+} \leq r _ {P i} ^ {+} \leq R _ {P i} ^ {\max +} \quad q _ {i k} ^ {+} \leq r _ {Q i} ^ {+} \leq R _ {Q i} ^ {\max +} \quad \forall i, k\tag{11}
$$

<sub>ð</sub><sup>12</sup><sub>Þ</sub>

The next three do the same for downward deviations and reserves.

$$
0 \leq p _ {i k} ^ {-} \quad 0 \leq q _ {i k} ^ {-} \quad \forall i, k\tag{13}
$$

![](/api/attachments/NKZ3UA48/fulltext/images/3012794902b8c9b52cd1e34f98d148a51c74b8c4be3ac24c9a4d683757993532.jpg)  
Fig. 4. Reserve structure.

$$
p _ {c i} - p _ {i k} \leq p _ {i k} ^ {-} \quad q _ {c i} - q _ {i k} \leq q _ {i k} ^ {-} \quad \forall i, k\tag{14}
$$

$$
p _ {i k} ^ {-} \leq r _ {P i} ^ {-} \leq R _ {P i} ^ {\max -} \quad q _ {i k} ^ {-} \leq r _ {Q i} ^ {-} \leq R _ {Q i} ^ {\max -} \quad \forall i, k\tag{15}
$$

Then, the deviations from the base case (not from the contracted amount) are bounded by the physical ramp rate of each unit.

$$
\begin{array}{l l} - \Delta_ {P i} ^ {-} \leq p _ {i k} - p _ {i 0} \leq \Delta_ {P i} ^ {+} \\ - \Delta_ {Q i} ^ {-} \leq q _ {i k} - q _ {i 0} \leq \Delta_ {Q i} ^ {+} \end{array} \quad \forall i, \quad k = 1... n _ {c}\tag{16}
$$

Finally, these constraints allow imposing or relaxing an equality constraint between the contracted quantities and the base case dispatch quantities by choice of α so that the contracted quantity can be speci<sup>fi</sup>ed to be equal to the base case dispatch if so desired.

$$
\begin{array}{l l} - \alpha \leq p _ {i 0} - p _ {c i} \leq \alpha & \forall i \\ - \alpha \leq q _ {i 0} - q _ {c i} \leq \alpha \end{array}\tag{17}
$$

In this formulation, for the bounds in Eqs. (11), (12), (14), and (15) to be tight at the solution it is necessary that marginal costs on deviations and reserves (p<sup>+</sup>, p<sup>−</sup>, r<sup>+</sup>, r<sup>−</sup>, q<sup>+</sup>, q<sup>−</sup>, $r _ { Q i } ^ { + } , r _ { Q i } ^ { - } )$ be positive. They can be allowed to be zero but that may require adjusting the bounds to be tight as a post-solution procedure that does not affect the cost. Negative marginal costs are not appropriate for this formulation.

The overall problem can be formidable in size, and while many of the constraints are linear, the power <sup>fl</sup>ow constraints in Eqs. (7) and (8) and thermal limits in Eq. (9) make the problem a nontrivial one. Indeed, the standard power <sup>fl</sup>ow equations are nominally nonconvex in voltage angles and magnitudes, however, as practitioners know, real-life instances of these problems can be indeed solved. While it is out of the scope of this work to delve in the details of these issues, the reader interested in issues related to the degree of convexity in the optimal power <sup>fl</sup>ow problem is urged to review the recent work in [30] and extensions in [31] for details on how realistic network losses make the problem much more amenable to numerical treatment.

The solution to the day-ahead problem yields optimal day-ahead contract quantities $( P _ { c } , R _ { P } ^ { + } , R _ { P } ^ { - } , Q _ { c } , R _ { Q } ^ { + } , R _ { Q } ^ { - } )$ as well as generation ranges; for all considered scenarios, the ith generator's active output will lie in $[ p _ { c i } - r _ { P i } ^ { - } , p _ { c i } + r _ { P i } ^ { + } ]$ , except perhaps in the scenario in which that unit is off-line as a result of a contingency. The treatment of the reactive output is similar. The day-ahead planning then results in a contract for providing a nominal quantity $p _ { c i }$ at a price determined by the chosen auction institution and the marginal cost of energy at the generator's location, with the additional obligation to abide by any redispatch issued by the ISO in real time within the range $[ p _ { c i } - r _ { P i } ^ { - } , p _ { c i } + r _ { P i } ^ { + } ]$ Such redispatch incurs the incremental costs, in addition to energy

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

costs, computed as a function of the amount of deviation from the energy contract. This range of generation is re<sup>fl</sup>ected in the amounts of reserves $r _ { P i } ^ { + }$ and $r _ { P i } ^ { - }$ procured from the ith generator. A day-ahead settlement can be executed or the parties can wait until the real-time pricing and redispatch are performed the next day.

## 3. Analysis of the Lagrangian function for the day-ahead problem

The day-ahead problem is considered at this point, and for simplicity of notation it is assumed that there are no reactive power offers in the treatment and that there is only one generation unit at a given bus. The case in which reactive costs are considered is straightforward because of the similar treatment of offers, costs and constraints.

Thus, the Lagrangian function for an active-only procurement problem is given by Eq. (18) where $\lambda _ { i k }$ are the multipliers on the active power <sup>fl</sup>ow equality constraints whenever there is a generator involved, $g _ { \mathrm { o t h e r } }$ and h are all other equality and nonlinear inequality constraints with corresponding multipliers $\lambda _ { \mathrm { o t h e r } }$ and $\mu _ { \mathrm { o t h e r } } ,$ and $\left\{ \mu _ { P _ { i k } ^ { \operatorname* { m a x } } } \right\}$ $\left\{ \mu _ { P _ { i k } ^ { \mathrm { m i n } } } \right\} , \left\{ \mu _ { i k } ^ { ( 1 0 ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 1 ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 2 a ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 2 b ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 3 ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 4 ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 4 ) } \right\}$ $\left\{ \mu _ { i k } ^ { ( 1 5 b ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 6 a ) } \right\} , \left\{ \mu _ { i k } ^ { ( 1 6 b ) } \right\} , \left\{ \mu _ { i } ^ { ( 1 7 a ) } \right\}$ , and $\left\{ \mu _ { i } ^ { \left( 1 7 b \right) } \right\}$ are KKT multipliers on the additional inequalities de<sup>fi</sup>ning the incremental variables, contract quantity variables and reserve variables. The numbered superscripts on the various μ variables refer to the equation number of the corresponding constraint, and when followed by a or b refer the <sup>fi</sup>rst or second inequality respectively for the given equation number.

$$
\begin{array}{l} L (\Theta , V, P, Q, P _ {c}, P ^ {+}, P ^ {-}, R _ {P} ^ {+}, R _ {P} ^ {-}, \lambda , \mu) \\ = \sum_ {k = 0} ^ {n _ {c}} \pi_ {k} \sum_ {i \in G ^ {k}} \left[ C _ {P i} (p _ {i k}) + C _ {P i} ^ {+} (p _ {i k} ^ {+}) + C _ {P i} ^ {-} (p _ {i k} ^ {-}) \right] \\ \quad + \sum_ {i = 1} ^ {n _ {g}} \left[ C _ {R P i} ^ {+} (r _ {P i} ^ {+}) + C _ {R P i} ^ {-} (r _ {P i} ^ {-}) \right] + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \lambda_ {i k} \Big (g _ {P g i k} - p _ {i k} + P _ {D i} \Big) \\ \quad + \lambda_ {\text {other}} ^ {T} g _ {\text {other}} + \mu_ {\text {other}} ^ {T} h + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {P _ {i k} ^ {\max}} (- P _ {i k} ^ {\max} + p _ {i k}) \\ \quad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {P _ {i k} ^ {\min}} \Big (P _ {i k} ^ {\min} - p _ {i k} \Big) + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 0)} (- p _ {i k} ^ {+}) \\ \quad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 1)} (p _ {i k} - p _ {c i} - p _ {i k} ^ {+}) + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 2 a)} (p _ {i k} ^ {+} - r _ {P i} ^ {+}) \\ \quad + \sum_ {i = 1} ^ {n _ {g}} \mu_ {i} ^ {(1 2 b)} (r _ {P i} ^ {+} - R _ {P i} ^ {\max +}) + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 3)} (- p _ {i k} ^ {-}) \\ \quad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 4)} (p _ {c i} - p _ {i k} - p _ {i k} ^ {-}) + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 5 a)} (p _ {i k} ^ {-} - r _ {P i} ^ {-}) \\ \quad + \sum_ {i = 1} ^ {n _ {g}} \mu_ {i} ^ {(1 5 b)} (r _ {P i} ^ {-} - R _ {P i} ^ {\max -}) + \sum_ {k = 1} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(1 6 a)} (- p _ {i k} + p _ {i 0} - \Delta_ {P i} ^ {-}) \\ \quad + \sum_ {\substack {k = 1 \\ n _ {\mathrm{g}}}} ^ {\frac {}{n _ {\mathrm{g}}}} \sum_ {\substack {\mathrm{i} \in G ^ {\mathrm{k}} \\ n _ {\mathrm{g}}}} \mu_ {\mathrm{i}} ^ {(1 6 b)} (p _ {\mathrm{i}} - p _ {\mathrm{i0}} - \Delta_ {\mathrm{i}} ^ {\mathrm{+}}) + \sum_ {\mathrm{i=1}} ^ {\frac {}{n _ {\mathrm{g}}}} \mu_ {\mathrm{i}} ^ {(1 7 a)} (p _ {\mathrm{i}} - p _ {\mathrm{i0}} - \alpha) \\ \quad + \sum_ {\mathrm{i=1}} ^ {\frac {}{n _ {\mathrm{g}}}} \mu_ {\mathrm{i}} ^ {(1 7 b)} (p _ {\mathrm{i0}} - p _ {\mathrm{i}} - \alpha). \end{array}\tag{18}
$$

The <sup>fi</sup>rst order optimality conditions obtained by differentiation with respect to $( p _ { i k } , p _ { i k } ^ { + } , p _ { i k } ^ { - } , r _ { p i } ^ { + } , r _ { p i } ^ { - } , p _ { c i } )$ can be rearranged and combined to obtain

$$
C _ {R P i} ^ {+ ^ {\prime}} \left(r _ {p i} ^ {+}\right) + \mu_ {i} ^ {(1 2 b)} = \sum_ {k = 0} ^ {n _ {c}} \mu_ {i k} ^ {(1 2 a)},\tag{19}
$$

$$
C _ {R P i} ^ {- ^ {\prime}} \left(r _ {p i} ^ {-}\right) + \mu_ {i} ^ {(1 5 b)} = \sum_ {k = 0} ^ {n _ {c}} \mu_ {i k} ^ {(1 5 a)},\tag{20}
$$

$$
- \sum_ {k = 0} ^ {n _ {c}} \mu_ {i k} ^ {(1 1)} + \sum_ {k = 0} ^ {n _ {c}} \mu_ {i k} ^ {(1 4)} = \mu_ {i} ^ {(1 7 b)} - \mu_ {i} ^ {(1 7 a)},\tag{21}
$$

and

$$
\begin{array}{l} \frac {\partial L}{\partial P _ {D i}} = \sum_ {k = 0} ^ {n _ {c}} \lambda_ {i k} \\ \qquad = \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {\prime} (p _ {i k}) + \mu_ {P _ {i k} ^ {\max}} - \mu_ {P _ {i k} ^ {\min}} \right] \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {+ ^ {\prime}} (p _ {i k} ^ {+}) - \mu_ {i k} ^ {(1 0)} \right] \\ \qquad - \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {- ^ {\prime}} (p _ {i k} ^ {-}) - \mu_ {i k} ^ {(1 3)} \right] \\ \qquad + C _ {R P i} ^ {+ ^ {\prime}} (r _ {p i} ^ {+}) + \mu_ {i} ^ {(1 2 b)} \\ \qquad - C _ {R P i} ^ {- ^ {\prime}} (r _ {p i} ^ {-}) - \mu_ {i} ^ {(1 5 b)} - \mu_ {i} ^ {(1 7 a)} + \mu_ {i} ^ {(1 7 b)}. \end{array}\tag{22}
$$

Eqs. (19) and (20) explain the marginal cost of reserves. Eq. (21) explains that when the equality of the base case dispatch and the contracted quantity is relaxed, the expected marginal costs of the upward and downward deviations must be equal at the solution. Finally, Eq. (22) explains the components in the cost of an extra unit of load at a bus, when considered equally over all scenarios. Notice that there can be a shadow price adjustment if the equality of the base case dispatch and the contract quantities is enforced, yielding possibly nonzero $\mu _ { i } ^ { ( 1 7 b ) }$ or $\mu _ { i } ^ { ( 1 7 a ) }$ <sup>)</sup>. In formulations which implicitly force an equality of the base dispatch and the contracted amount, the value of $\dot { \mu } _ { i } ^ { ( 1 7 \bar { b } ) }$ or $\mu _ { i } ^ { ( 1 7 a ) }$ is actually embedded in $\textstyle \sum _ { k = 0 } ^ { n _ { c } } \lambda _ { i k }$

## 4. Real-time adjustment of dispatch

The problem of balancing and pricing the real-time market is now subject to the contract issued the previous day. Reserve quantities have already been determined and paid for; a generation range, together with the original energy and incremental energy offers and the current state of the network are what is available to the ISO to compute any needed re-dispatch. Incremental amounts and costs are now determined from the $p _ { c i }$ agreed upon the previous day. Security is still desirable, of course, and the dispatch should still consider the possibility of transitioning to other network con<sup>fi</sup>gurations as a result of contingencies. At this point in time, however, the probabilities of occurrence for contingencies have changed and in some cases the uncertainty is no longer there, such as in the case of the speci<sup>fi</sup>c realized demand. Thus the time-viewpoint available to the planner now is not the same as was available the previous day. More information is available; either the system is “intact” and exhibits the con<sup>fi</sup>guration of the base case (with perhaps a somewhat different demand) or a contingency has happened and the system has undergone a transition.

## 4.1. Redispatching the intact system

Assume that an intact system con<sup>fi</sup>guration is realized; that is, the con<sup>fi</sup>guration contemplated in the base case, even if the demand is slightly different. While the transition restrictions needed to enforce a secure dispatch should still be included in the model, the probabilities of contingencies used for a pricing run of the model should be set to zero, i.e., the contingencies did not materialize. However, the formulation to follow could also be used for an hour-ahead or 10 minute-ahead redispatch, in which case some probabilities would not be zero. Thus, the problem at this stage becomes

$$
\min_{\substack{\theta ,V,P,Q,\\ P^{+},P^{-},\\ Q^{+},Q^{-}}}\sum_{k = 0}^{n_{c}}\pi_{k}\sum_{i\in C^{k}}\left\{ \begin{array}{l}C_{Pi}(p_{ik}) + C_{Qi}(q_{ik})\\ +C_{Pi}^{+}(p_{ik}^{+}) + C_{Qi}^{+}(q_{ik}^{+})\\ +C_{Pi}^{-}(p_{ik}) + C_{Qi}^{-}(q_{ik}) \end{array} \right\}\tag{23}
$$

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

subject to

$$
g _ {P} ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) = 0, \quad k = 0 \dots n _ {c},\tag{24}
$$

$$
g _ {Q} ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) = 0, \quad k = 0 \dots n _ {c},\tag{25}
$$

$$
h ^ {k} \left(\theta^ {k}, V ^ {k}, P ^ {k}, Q ^ {k}\right) \leq 0, \quad k = 0 \dots n _ {c},\tag{26}
$$

$$
0 \leq p _ {i k} ^ {+}, \quad 0 \leq q _ {i k} ^ {+}, \quad \forall i, k,\tag{27}
$$

$$
p _ {i k} - \hat {p} _ {c i} \leq p _ {i k} ^ {+}, \quad q _ {i k} - \hat {q} _ {c i} \leq q _ {i k} ^ {+}, \quad \forall i, k,\tag{28}
$$

$$
p _ {i k} ^ {+} \leq \hat {r} _ {P i} ^ {+} q _ {i k} ^ {+} \leq \hat {r} _ {Q i} ^ {+} \forall i, k,\tag{29}
$$

$$
0 \leq p _ {i k} ^ {-}, \quad 0 \leq q _ {i k} ^ {-}, \quad \forall i, k,\tag{30}
$$

$$
\hat {p} _ {c i} - p _ {i k} \leq p _ {i k} ^ {-}, \quad \hat {q} _ {c i} - q _ {i k} \leq q _ {i k} ^ {-}, \quad \forall i, k,\tag{31}
$$

$$
p _ {i k} ^ {-} \leq \hat {r} _ {P i} ^ {-}, \quad q _ {i k} ^ {-} \leq \hat {r} _ {Q i} ^ {-}, \quad \forall i, k,\tag{32}
$$

$$
\begin{array}{l l} - \Delta_ {P i} ^ {-} \leq p _ {i k} - p _ {i 0} \leq \Delta_ {P i} ^ {+} \\ - \Delta_ {Q i} ^ {-} \leq q _ {i k} - q _ {i 0} \leq \Delta_ {Q i} ^ {+} & \forall i, \quad k = 1... n _ {c}, \end{array}\tag{33}
$$

where $( \hat { P } _ { c } , \hat { R } _ { P } ^ { + } , \hat { R } _ { P } ^ { - } , \hat { Q } _ { c } , \hat { R } _ { Q } ^ { + } , \hat { R } _ { Q } ^ { - } )$ ) are now <sup>fi</sup>xed parameters, taken from the day-ahead solution. There is no need to enforce box limits $( P _ { \mathrm { m i n } } , P _ { \mathrm { m a x } } ,$ $Q _ { \mathrm { m i n } } , Q _ { \mathrm { m a x } } )$ , since they are implicit in the reserves contracts $( \hat { r } _ { P i } ^ { + } , \hat { r } _ { P i } ^ { - }$ $\hat { r } _ { Q i } ^ { + } , \hat { r } _ { Q i } ^ { - } )$ . However, it should be noted that for generators with trapezoidal $\left( p _ { i } , q _ { i } \right)$ feasible regions like those employed in MATPOWER, the upper and lower sloped linear constraints still need to be enforced (which MATPOWER does) and if binding, the corresponding shadow prices can be decomposed into equivalent $\mu _ { \mathrm { P m a x } }$ and $\mu _ { \mathrm { { P m i n } } }$ multipliers.

The Lagrangian function for this problem, again assuming an active power-only problem is

$$
\begin{array}{l} L \big (\Theta , V, P, Q, P ^ {+}, P ^ {-}, \lambda , \mu \big) = \sum_ {k = 0} ^ {n _ {c}} \pi_ {k} \sum_ {i \in G ^ {k}} \big [ C _ {P i} (p _ {i k}) + C _ {P i} ^ {+} (p _ {i k} ^ {+}) + C _ {P i} ^ {-} (p _ {i k} ^ {-}) \big ] \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \lambda_ {i k} \Big (g _ {P g i k} - p _ {i k} + P _ {D i} \Big) \\ \qquad + \lambda_ {\text {other}} ^ {T} g _ {\text {other}} + \mu_ {\text {other}} ^ {T} h \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(2 7)} (- p _ {i k} ^ {+}) \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(2 8)} (p _ {i k} - \hat {p} _ {c i} - p _ {i k} ^ {+}) \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(2 9)} (p _ {i k} ^ {+} - \hat {r} _ {P i} ^ {+}) \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(3 0)} (- p _ {i k} ^ {-}) \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(3 1)} (\hat {p} _ {c i} - p _ {i k} - p _ {i k} ^ {-}) \\ \qquad + \sum_ {k = 0} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(3 2)} (p _ {i k} ^ {-} - \hat {r} _ {P i} ^ {-}) \\ \qquad + \sum_ {k = 1} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(3 3 a)} (- p _ {i k} + p _ {i 0} - \Delta_ {P i} ^ {-}) \\ \qquad + \sum_ {k = 1} ^ {n _ {c}} \sum_ {i \in G ^ {k}} \mu_ {i k} ^ {(3 3 b)} (p _ {i k} - p _ {i 0} - \Delta_ {P i} ^ {+}). \end{array}\tag{34}
$$

In a way similar to the day-ahead problem, the <sup>fi</sup>rst order optimality conditions with respect to $( p _ { i k } , p _ { i k } ^ { + } , p _ { i k } ^ { - } )$ can be combined and arranged to yield

$$
\frac {\partial L}{\partial P _ {D i}} = \sum_ {k = 0} ^ {n _ {c}} \lambda_ {i k}
$$

$$
= \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {\prime} (p _ {i k}) + \mu_ {i k} ^ {(2 8)} - \mu_ {i k} ^ {(3 1)} \right]\tag{35}
$$

$$
= \sum_ {k = 0} ^ {n _ {c}} \pi_ {k} C _ {P i} ^ {\prime} (p _ {i k})
$$

$$
+ \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {+ ^ {\prime}} (p _ {i k} ^ {+}) - \mu_ {i k} ^ {(2 7)} + \mu_ {i k} ^ {(2 9)} \right]
$$

$$
- \sum_ {k = 0} ^ {n _ {c}} \left[ \pi_ {k} C _ {P i} ^ {- ^ {\prime}} (p _ {i k} ^ {-}) - \mu_ {i k} ^ {(3 0)} + \mu_ {i k} ^ {(3 2)} \right]\tag{36}
$$

which again exhibits a clear cost decomposition.

## 4.2. Redispatching in a post-contingency state

Once the base case no longer describes the system con<sup>fi</sup>guration, possible transitions represent what would have been an $( N - 2 ) { \mathrm { - t y p e } }$ event the day-ahead. While the transition to the present state should have been feasible thanks to the resources committed day-ahead, it is by no means clear that transitioning to yet another state is allowed at this point. Yet, it makes sense to try to run the problems (23)–(33), with the base case replaced by the present system state and a set of (currently) credible contingencies, to see if it is still possible to redispatch the system securely and economically with the available resources.

## 5. Implementation

The generalized OPF solver in the MATPOWER [32] package employs an AC OPF formulation with additional functionality

$$
\min _ {X, Z} \sum_ {i = 1} ^ {n _ {g}} \left[ f _ {P} ^ {i} (p _ {i}) + f _ {Q} ^ {i} (q _ {i}) \right] + f (X, Z)\tag{37}
$$

where ${ \cal { X } } = ( \theta , V , P , Q )$ are the traditional AC OPF optimization variables, Z are additional user variables, $f _ { P } , f _ { Q }$ are any mix of piecewise linear or polynomial costs on injections (generalized to dispatchable loads), and

$$
f (\Theta , V, P, Q, Z) = \frac {1}{2} w ^ {T} H w + C w\tag{38}
$$

is a general quadratic cost on a vector w that is derived from the optimization variables in two steps: First, a linear combination r of the optimization variables is de<sup>fi</sup>ned by

$$
r = N \left[ \begin{array}{c} \theta \\ V \\ P \\ Q \\ Z \end{array} \right].\tag{39}
$$

Then, a translation, a dead zone, and individual, scalar functions chosen by the user out of a prede<sup>fi</sup>ned library set, are applied to each of the elements in r to yield w. This way, many classes of functions can be applied to all of the optimization variables in the problem. This is subject to

$$
\begin{array}{l l} g _ {P} (\Theta , V, P, Q) = 0 & \text { active   load   flow } \\ g _ {Q} (\Theta , V, P, Q) = 0 & \text { reactive   load   flow } \end{array}\tag{40}
$$

<sub>ð</sub><sup>41</sup><sub>Þ</sub>

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

C.E. Murillo-Sánchez et al. / Decision Support Systems xxx (2013) xxx–xxx

$$
S _ {F} (\Theta , V, P, Q) \leq S _ {F} ^ {+} \quad \text { MVA   limit   ``from''   end }\tag{42}
$$

$$
S _ {T} (\Theta , V, P, Q) \leq S _ {T} ^ {+} \quad \text { MVA   limit   ``to''   end }\tag{43}
$$

$$
l \leq A \left[ \begin{array}{c} \theta \\ V \\ P \\ Q \\ Z \end{array} \right] \leq u \quad \text { general   linear   constraints }\tag{44}
$$

$$
(p _ {i}, q _ {i}) \in \mathcal {C} ^ {i} \quad \text { gen.   capability   curve }\tag{45}
$$

$$
V ^ {\min} \leq V \leq V ^ {\max} \quad \text { voltage   limits }\tag{46}
$$

$$
\theta_ {l m} ^ {\min} \leq \theta_ {l} - \theta_ {m} \leq \theta_ {l m} ^ {\max} \quad \text { angle   differences. }\tag{47}
$$

With these capabilities, it is possible to pose both the day-ahead and the real-time problems by <sup>fi</sup>rst making copies of the original base case, modifying them to account for the equipment changes that give rise to each of the considered contingencies, and then lump all of these systems together in a large network with $( n _ { c } + 1 )$ islands. The coupling constraints and the additional variables and linear constraints can be cast using the general linear constraint capability, while the costs on reserves and deviations from contract can be speci<sup>fi</sup>ed using the generalized cost component. This has been implemented in MATLAB for a single-root scenario tree which on all other accounts of the formulation is general and can be applied to any system in the MATPOWER data format. A single routine takes the original network data, performs the modi<sup>fi</sup>cations on it according to a contingency modi<sup>fi</sup>cation data table, assembles the large disjoint system and speci<sup>fi</sup>es the additional linear constraints and generalized cost, proceeding then to call the generalized OPF solver in MATPOWER.

## 6. Preliminary numerical results

Numerical simulations were conducted with both 30-bus and 118-bus networks to illustrate that the endogenous determination of optimal reserves, described in this paper, results in a more economically ef<sup>fi</sup>cient and reliable dispatch than the more traditional approach of using <sup>fi</sup>xed reserve margins. The metrics for comparison include cost of reserve allocations, overall cost of serving load, and avoidance of load shedding scenarios.

Comparison of Reserve Costs (\$)  
![](/api/attachments/NKZ3UA48/fulltext/images/21538d4c5a12dbf5b57a0c93b37839a87ab0af4f983005f4b45b05d52e092d7a.jpg)  
Fig. 5. Cost of reserve comparison, 30-bus system.

![](/api/attachments/NKZ3UA48/fulltext/images/d848fb99c382fc91c0903642f8106129999fab8433c29dd2c5c4b01d5c52d302.jpg)  
Fig. 6. Reserves allocated and load shed, 30-bus system.

## 6.1. IEEE 30-bus system

Initial numerical tests employed a variant of the 30-bus IEEE system, which has six generators. The original system data had to be modi<sup>fi</sup>ed to alleviate reactive security issues that prevented it from being able to meet most contingencies. Results shown here include twelve contingencies, including outages of each generator. Line outages have emphasized those lines actually representing long distance connections. For most tests, two contingencies representing higher and lower than expected demands have been included in the contingency set, with deviations of 10% from the central load forecast uniformly across the network. Subsequently, the real time balancing and pricing formulation has been run on each of the assumed scenarios.

Using this system, the effectiveness of reserve allocations was compared for varying load levels based on the metrics previously discussed. Fig. 5 shows the allocated reserves for various load levels. This <sup>fi</sup>gure shows that for all load levels, higher total reserves are allocated when using <sup>fi</sup>xed reserve allocations than under the optimal reserve allocations made possible by this framework, designated SOPF in the <sup>fi</sup>gures. It is natural to assume that this results in a more secure dispatch. However, results shown in Fig. 6, illustrate that the opposite is true. The <sup>fi</sup>xed reserve methodology also exhibits a higher probability of load shedding than in the co-optimization approach of the SOPF. Fig. 7 shows the total cost for generation, reserves and load shedding for the same system

![](/api/attachments/NKZ3UA48/fulltext/images/41009e5526e97e9fee7841c038b8a0db154ba0dbb9cf67e1986f1aec40c6765b.jpg)  
Fig. 7. Total cost of serving load, 30-bus system

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

with the same conditions. While the actual cost of reserve allocations is higher in the SOPF case, the <sup>fi</sup>nal cost of generation and load shedding is signi<sup>fi</sup>cantly lower. In fact, the results of these numerical tests indicate that load shedding can be avoided in all contingencies with proper allocation of reserves.

## 6.2. IEEE 118-bus system

In addition to numerical validation with the IEEE 30-bus system, it was deemed necessary to test the formulation on a larger network. The IEEE 118-bus system was selected as a basis for this task. This network has a total of 54 generators, and the problem formulation includes twelve contingencies; six possible generator outages, and six line outages.

In the same order, we consider a comparison of allocated reserves, load shedding and cost of load served in Figs. 8 and 9.

Fig. 8 presents the MW of load shedding required to meet system requirements with the optimally allocated reserves of the SOPF, and with increasing exogenously determined <sup>fi</sup>xed reserve margins. The important point to note is that the SOPF solution has no load shedding, whereas the <sup>fi</sup>xed reserve margins exhibit load shedding in at least one contingency until the margins reach 115% of the aggregate reserves as determined by the SOPF.

Fig. 9 compares the expected cost of serving load with the reserve allocations determined endogenously (SOPF) and with increasing <sup>fi</sup>xed reserve margins.

## 6.3. Solution tightness

Indeed, the day-ahead solution determined by the algorithm procures the reserve amounts needed in light of the scenarios considered and nothing more than that. Thus, if the scenarios do not capture the actual breadth of looming dispatch possibilities, it is possible that real-time conditions will reveal that not enough reserve was procured to operate securely. For the single-root scenario tree, it is therefore important to include not just equipment failures in the contingency set, but also deviations from forecasted load. Given an estimate of the uncertainty of the load forecast, it is possible to bound the estimate with 95 or 99% con<sup>fi</sup>dence interval brackets and use these as the lower and higher-than-expected demand scenarios. These two scenarios can capture locational demand differences if the uncertainty in the predictions is known down to a more local (bus or zone) level.

![](/api/attachments/NKZ3UA48/fulltext/images/9ed53750cf2e6bd4a99e23060c0832938defd61e62dfb228ae14ca4a7d10ab8b.jpg)  
Fig. 8. MW of load shed with increasing reserve level, 118-bus system.

![](/api/attachments/NKZ3UA48/fulltext/images/e7ec08c96ea172733d24bc4628f6a732ec54eeea922ad47434a40f08b2fe568e.jpg)  
Fig. 9. Cost of reserves, 118-bus system.

## 6.4. Completion of optimization in post-contingency dispatches

When the probabilities employed in some contingencies are very small, the contribution to the cost function by the injections considered in that contingency can be minimal. Therefore, it is possible that the optimizer being employed will stop the process after asserting that the corresponding portion of the gradient of the cost has a norm smaller than some tolerance, leading to an incomplete optimization of the dispatch for that contingency. This is a scaling issue inherent in the typical sets of probabilities employed in this problem; it would not be present if all outcomes were more or less equiprobable. It makes sense to run the real-time algorithm for each of the scenarios considered immediately after solving the day-ahead problem to see if there are any major differences in the dispatches obtained as a check on this issue. Note that a decomposition and coordination approach to solving this problem, currently under development, may eliminate this issue altogether.

## 7. Conclusion

The formulation proposed in this work is appropriate for clearing a multi-commodity market and preliminary numerical testing with small systems con<sup>fi</sup>rms its theoretical advantages. It is now possible to test how true multi-commodity markets with realistic price signals derived from <sup>fi</sup>rst principles might behave using experimental economics techniques.

While detailed physical modeling is retained for accuracy of the solution, at the same time the procurement amount is not arti<sup>fi</sup>cially bound to be the same as the base case dispatch, thus allowing more freedom in choosing the day-ahead optimal procurement. Whether the optimal procurement differs signi<sup>fi</sup>cantly from the base case dispatch depends on the cost/offer data, as expected. This difference needs to be explored further with data derived from experiments employing human subjects or actual market data in order to quantify the bene<sup>fi</sup>t of decoupling the procurement quantity and the base case dispatch.

For larger scale implementation, several issues still need to be addressed, among them the robustness and warm start capability of the underlying generalized OPF solver, the speci<sup>fi</sup>c decomposition and coordination scheme used to separate the problems into smaller units for parallelization purposes, and the integration of the formulation into a unit commitment setting. This last issue may be resolved by employing the basic ideas in [32].

Please cite this article as: C.E. Murillo-Sánchez, et al., A stochastic, contingency-based security-constrained optimal power <sup>fl</sup>ow for the procurement of energy and distributed reserve, Decision Support Systems (2013), http://dx.doi.org/10.1016/j.dss.2013.04.006

## References

[1] O. Alsac, B. Stott, Optimal load <sup>fl</sup>ow with steady state security, IEEE Transactions on Power Apparatus and Systems PAS-93 (3) (May 1974) 745–751

[2] J. Arroyo, F. Galiana, Energy and reserve pricing in security and network-constrained electricity markets, IEEE Transactions on Power Systems 20 (2) (May 2005) 634–643.

[3] F. Bouffard, F. Galiana, A. Conejo, Market-clearing with stochastic security—part I: formulation, IEEE Transactions on Power Systems 20 (4) (November 2005) 1818–1826.

[4] R. Burchett, H. Happ, Large scale security dispatching: an exact model, IEEE Transactions on Power Apparatus and Systems PAS-102 (9) (September 1983) 2995–2999.

[5] F. Capitanescu, L. Wehenkel, Improving the statement of the corrective securityconstrained optimal power-<sup>fl</sup>ow problem, IEEE Transactions on Power Systems 22 (2) (May 2007) 867–889.

[6] P. Carpentier, G. Cohen, J.-C. Culioli, A. Renaud, Stochastic optimization of unit commitment: a new decomposition framework, IEEE Transactions on Power Systems 11 (2) (May 1996) 1067–1073.

[7] J. Carpentier, D. Menniti, A. Pinnarelli, N. Scoordino, N. Sorrentino, An algorithm for direct solution of active secure economic dispatch with an improved economic statement, Proc. Powercon 2000, 2000, pp. 1239–1244.

[8] J. Carpentier, D. Menniti, A. Pinnarelli, N. Scoordino, N. Sorrentino, A model of the ISO insecurity costs management in a deregulated market scenario, in: IEEE (Ed.), Proc, 2001 IEEE Porto Power Tech Conf 2001

[9] J. Chen, J. Thorp, R. Thomas, T. Mount, Locational pricing and scheduling for an integrated energy-reserve market, in: IEEE (Ed.), Proc. 36th Annual Hawaii International Conf. on System Sciences, January 2003.

[10] J. Chen, T. Mount, J. Thorp, R. Thomas, Location-based scheduling and pricing for energy and reserve: a responsive reserve market proposal, Decision Support Systems 40 (3) (October 2005).563–577.

[11] J. Condren, T. Gedra, P. Damrongkulkamjorn, Optimal power <sup>fl</sup>ow with expected security costs, IEEE Transactions on Power Systems 21 (2) (May 2006) 541–547.

[12] P. Damrongkulkamjorn, T. Gedra, Optimal power <sup>fl</sup>ow with expected security costs, 31st Annual Frontiers of Powers Conf., Stillwater, Oklahoma, October 1998.

[13] F. Galiana, F. Bouffard, J. Arroyo, J. Restrepo, Scheduling and pricing of coupled energy and primary, secondary, and tertiary reserves, Proceedings of the IEEE 93 (11) (November 2005) 1970–1983.

[14] R. Jabr, A. Coonick, B. Cory, A homogeneous linear programming algorithm for the security constrained economic dispatch problem, IEEE Transactions on Power Systems 15 (3) (August 2000) 930–936.

[15] R. Kaye, F. Wu, P. Varaiya, Pricing for system security, IEEE Transactions on Power Systems 10 (2) (May 1995) 575–583.

[16] J. Lavaei, S. Low, Zero duality gap in optimal power <sup>fl</sup>ow problem, IEEE Transactions on Power Systems 27 (1) (February 2012) 92–107.

[17] J. López-Lezama, C. Murillo-Sánchez, L. Zuluaga, J. Gutiérrez-Gómez, A contingencybased security-constrained optimal power <sup>fl</sup>ow model for revealing the marginal cost of a blackout risk-equalizing policy in the Colombian electricity market, in: IEEE (Ed.), Proc. 2006 Transmission and Distribution Conference and Exposition: Latin America, 2006.

[18] M. Madrigal, V. Quintana, A security-constrained energy and spinning reserve market clearing system using an interior-point method, IEEE Transactions on Power Systems 15 (4) (November 2000) 1410–1416.

[19] F. Milano, C. Cañizares, A. Conejo, Sensitivity-based security-constrained OPF market clearing model, IEEE Transactions on Power Systems 20 (4) (November 2005) 2051–2060.

[20] A. Monticelli, M. Pereira, S. Granville, Security-constrained optimal power <sup>fl</sup>ow with post contingency corrective rescheduling, IEEE Transactions on Power Systems 2 (1) (February 1987) 175–181.

[21] O. Moya, A spinning reserve, load shedding, and economic dispatch solution by Bender's decomposition, IEEE Transactions on Power Systems 20 (1) (February 2005).384-388.

[22] C. Murillo-Sánchez, R.J. Thomas, Scheduling of thermal units with a nonlinear load <sup>fl</sup>ow model, Decision Support Systems 24 (1999) 311–320.

[23] H. Singh, A. Papalexopoulos, Competitive procurement of ancillary services by an independent system operator, IEEE Transactions on Power Systems 14 (2) (May 1999) 498–504.

[24] S. Sojoudi, J. Lavaei, Physics of power networks makes hard optimization problems easy to solve. Power Engineering Society General Meeting, IEEE, 2012.

[25] B. Stott, O. Alsac, A. Monticelli, Security analysis and optimization, Proceedings of the IEEE 75 (12) (December 1987) 1623–1644

[26] C. Taylor, Power System Voltage Stability, McGraw-Hill, 1994.

[27] J. Thorp, C. Murillo-Sánchez, R. Thomas, Time-space methods for determining locational reserves: a framework or location-based pricing and scheduling for reserve markets, Tech Report, Cornell University, November 2001.

[28] H. Wang, C. Murillo-Sánchez, R. Zimmerman, R. Thomas, On computational issues of market-based optimal power <sup>fl</sup>ow, IEEE Transactions on Power Systems 22 (3) (August 2007) 1185–1193.

[29] S. Wong, J. Fuller, Pricing energy and reserves using stochastic optimization in an alternative electricity market, IEEE Transactions on Power Systems 22 (2) (May 2007) 631–638.

[30] T. Wu, M. Rothleder, Z. Alaywan, A. Papalexopoulos, Pricing energy and ancillary services in integrated market systems by an optimal power <sup>fl</sup>ow, IEEE Transactions on Power Systems 19 (1) (February 2004) 339–347.

[31] R. Zimmerman, C. Murillo-Sánchez, R.J. Thomas, Matpower's extensible optimal power <sup>fl</sup>ow architecture, in: IEEE (Ed.), Proc. Power and Energy Society General Meeting, July 2009.

[32] R. Zimmerman, C. Murillo-Sánchez, R. Thomas, Matpower: steady-state operations, planning, and analysis tool for power systems research and education, IEEE Transactions on Power Systems 26 (1) (February 2011) 12–19.

Carlos Edmundo Murillo-Sánchez received the electronics engineering degree from ITESM, Monterrey, Mexico, in 1987, the M.Sc. degree in electrical engineering from the University of Wisconsin-Madison in 1991, and the Ph.D. degree in electrical engineering from Cornell University, Ithaca, NY, in 1999. He is an Associate Professor of engineering at Universidad Nacional de Colombia, in Manizales, Colombia. He is a founding member of the Colombian Automation Society (Asociación Colombiana de Automática). His interests include power systems operation and control, control systems applications, optimization, simulation, and mechatronics.

Ray Daniel Zimmerman is a Senior Research Associate in electrical engineering and applied economics and management at Cornell University, Ithaca, NY. He is the lead developer of the PowerWeb electricity market simulation platform and the MATPOWER power system simulation software. His current research interests center on the interactions between the economic and engineering aspects of electric power system operations and planning. Other interests include software tools for education and research.

Catherine Lindsay Anderson received the Ph.D. degree in Applied Mathematics from Western University, Canada in 2004. She is currently an Assistant Professor, and the Norman R. Scott Sesquicentennial Faculty Fellow, in Biological and Environmental Engineering at Cornell University in Ithaca, NY. Her interests are in optimization and simulation of stochastic systems, with applications in sustainable energy. She has published work in <sup>fi</sup>nance and electricity markets, wind integration, and bioenergy.

Robert John Thomas received the PhD. degree in electrical engineering from Wayne State University, Detroit, MI, in 1973. He is currently Professor Emeritus of Electrical and Computer Engineering at Cornell University, Ithaca, NY. His technical background is broadly in the areas of systems analysis and control of large-scale electric power systems. He has published in the areas of transient control and voltage collapse problems as well as technical economic, and institutional impacts of restructuring. Prof, Thomas is a member of Tau Beta Pi. Eta Kappa Nu. Sigma Xi, and ASEE. He has received five teaching awards and the IEEE Centennial and Millennium medals. He has been a member of the IEEE-USA Energy Policy Committee since 1991 and was the committee's Chair from 1997 to 1998. He is the founding Director of the 13-university-member National Science Foundation Industry/University Cooperative Research Center, PSerc and he currently serves as one of the 30 inaugural members of the U.S. Department of Energy Secretary's Electricity Advisory Committee (EAC).
