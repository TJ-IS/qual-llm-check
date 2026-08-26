---
otero_id: 1452
otero_key: "V2F98EBC"
title: "Location-based scheduling and pricing for energy and reserves: a responsive reserve market proposal"
authors: "Jie Chen; Timothy D. Mount; James S. Thorp; Robert J. Thomas"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Location-based scheduling and pricing for energy and reserves: a responsive reserve market proposal

Jie Chen<sup>a,\*</sup>, Timothy D. Mount<sup>b</sup>, James S. Thorp<sup>a</sup>, Robert J. Thomas<sup>a</sup>

<sup>a</sup>School of Electrical and Computer Engineering, Cornell University, Ithaca, NY 14853, USA <sup>b</sup>Department of Applied Economics and Management, Cornell University, Ithaca, NY 14853, USA

## Abstract

It is well known that given a network that can become constrained on voltage or real power flows, reserves must also be spatially located in order to handle all credible contingencies. However, to date, there is no credible science-based method for assigning and pricing reserves in this way. Presented in this paper is a responsive-reserve scheduling algorithm incorporating constraints imposed by grid security considerations, which include one base case (intact system) and a list of credible contingencies (line out, unit lost, and load growth) of the system. By following a cost-minimizing co-optimization procedure, both power and reserves are allocated spatially for the combined energy and reserve markets. With the Lagrange multipliers obtained, the scheduling algorithm also reveals the locational shadow prices for the reserve and energy requirements. Unlike other pricing and scheduling methods in use, which are usually ad hoc and are based on engineering judgment and experience, this proposed formulation is likely to perform better in restructured markets when market power is a potential problem. An illustrative example of a modified IEEE 30-bus system is used to introduce concepts and present results. <sup>D</sup> 2004 Elsevier B.V. All rights reseved.

Keywords: Reserve market; Responsive reserves; Location-based pricing; Co-optimization

## 1. Introduction

## 1.1. Background of operating reserves

An overriding factor in the power system operation is the maintenance of system security.

Historically, the term security, when applied to the electric power system, refers to the ability of the bulk system to withstand sudden disturbances such as electric short circuits or unanticipated loss of system components [6]. The static nature of the problem, that is, guaranteeing that in the postcontingency state all power system components are operating within established limits, is tractable once the set of credible contingencies is known. Generally, the most severe contingency is the sudden and unanticipated loss of a large generating unit although the loss of a critical line or a sudden and large increase in load at strategic locations could be just as catastrophic. The problem of whether or not the system can survive the transition, that is, the dynamic nature of system security, is still a hard and unresolved problem. Since in most systems load is not dispatchable, the security of the system depends on having the proper level, location and type of operating reserves available when needed to meet a contingency.

In the era of electricity regulation, vertically integrated utilities provided operating reserves through the advice of North American Electric Reliability Council (NERC) and regional reliability councils. Under deregulation, however, their procurement usually is the duty of the Independent System Operator (ISO). In the restructured system, reserves have both an engineering role and an economic role. The engineering role is to ensure that load is met in an environment where there is a regulatory obligation to serve load. The economic role of reserves is to avoid the losses associated with outages. The need for reserves is exacerbated by the fact that load usually is price inelastic. That is, there is an obligation to serve demand regardless of its level or location. Because of the network and the constraints it imposes, load may be isolated from generation if reserves are not placed properly with respect to a contingency.

## 1.2. Existing reserve market-fixed reserve requirement

Although the focus of deregulation has been on the design of markets for the efficient delivery of electricity, the role of reserves in maintaining the safe and reliable system operation is equally critical to the market performance. And a well functioning reserve market can also help mitigate price spikes and solve the capacity problem. Currently, there are markets for energy, and markets for reserves exist in some form in most currently operating ISOs. Also, a specific form of reserve market is proposed in the Standard Market Design Notice of Proposed Rulemaking (SMD NOPR) issued recently by the Federal Energy Regulatory Commission (FERC). Although there are different ways of procuring reserves, a common feature does exist: deterministic reserve requirement, which ensures that the reserve is sufficient to make up for the loss of the largest unit or that the reserve must be a given percentage of forecasted peak demand or some combination of these. Ref. [7] shows an example of fixed reserve requirement currently in use in New York ISO. There are three different requirements for three zones, and the assignment is based on the most severe New York Control Area (NYCA) operating capability loss.

Currently, reserves are only thought of as having time dependent properties, that is, they must be spinning or able to synchronize in ten minutes or within other predefined time frames. However, it is well known that given a network that can become constrained on voltage or real power flows, reserves must also be spatially located in order to handle all the contingencies that could occur. To date, there is no credible science-based method for assigning reserves in this way. Virtually all methods are ad hoc and are based on engineering judgment and experience.

The fixed reserve requirement works well under regulation, because all generators in a given area cooperate to configure the flows to maintain the system in operation. In a deregulated market, however, no cooperation exists. One potential problem with the fixed reserve requirement is that the reserve procurement may not be locationally distributed as desired. The consequence could be that some contingencies, if they occur, may not be covered with the procured reserves (not because of a shortfall in quantity, but due to the allocations being in the wrong place), resulting in increased operating costs from the use of expensive emergency resources. To avoid this situation or at least try to minimize the chance of it happening, one possible way is to procure more reserves so that more generators will have to carry reserves. The reserve assignment then might be able to cover every planned contingency, but the extra allocation of reserves means wasting resources. The system would require less reserves if they can be locationally assigned in a <sup>b</sup>smart<sup>Q</sup> way.

In the arena of deregulated electric power markets, the concept of Location-Based Marginal Pricing (LBMP) is well established and is commonly used to set electricity prices at a nodal level. The economic rationale for applying marginal cost pricing to an electricity network using the concepts of LBMP was presented in Ref. [8]. LBMP in electricity recognizes that the marginal price may differ at different locations and times. Differences result from transmission congestion and transmission losses. LBMP is believed to be an efficient market-based method for transmission congestion control and was also recommended in the SMD NOPR. Currently, LBMP is being used in the PJM, NYISO and ISO-NE energy markets. However, in the reserve markets, no standard methods for location-based pricing of reserves exist. Most of the ISOs are pricing reserves uniformly. Part of the problem lies in the fact that reserves procured in the market are based on a deterministic reserve requirement, which is similar to an energy dispatch based on the Economic Dispatch (ED) with no consideration of underlying transmission networks, in which there is only one electricity price for all nodes in one specific control region.

## 1.3. Alternative market proposal-variable/responsive reserve requirement

This paper explores a different way to allocate and price reserves. The requirement here is that the reserves procured in this way will maintain the same level of security for the transmission system, i.e., be able to cover the same set of contingencies considered in the fixed reserve market. It is similar to the method used in Refs. [1,2], in which system security is evaluated using probability-weighted performance indices over a set of power-flow cases or a set of credible contingencies. There is no fixed reserve requirement in the optimization. Instead, the same set of contingencies used in the deterministic reserve requirement will be included in the proposed scheduling and pricing algorithm. Locational assignments and locational prices for energy and reserves are available through the algorithm and are based on a <sup>b</sup>true<sup>Q</sup> co-optimization of both energy and reserves. The actual amount of reserves assigned varies with different system demands and energy-reserve offers. Hence, we call this new cooptimization Responsive Reserves (RR) to distinguish it from the conventional form of Fixed Reserves (FR).

## 2. Underlying optimization framework

## 2.1. Notation

The following notation will be used herein. Additional symbols will be introduced when necessary.

<table><tr><td>i</td><td>generator index (i=1,2,...,I)</td></tr><tr><td>j</td><td>bus index (j=1,2,...,J)</td></tr><tr><td>l</td><td>transmission line index (l=1,2,...,L)</td></tr><tr><td>k</td><td>contingency index (k=0,1,...,K), 0 indicates the base case (intact system), predefined contingencies otherwise</td></tr><tr><td> $P_{ik}/Q_{ik}$ </td><td>real/reactive power output of generator i in the kth contingency</td></tr><tr><td> $R_{ik}$ </td><td>spinning reserve carried by generator i in the kth contingency</td></tr><tr><td> $\theta_{jk}$ </td><td>voltage angle of bus j in the kth contingency</td></tr><tr><td> $V_{jk}$ </td><td>voltage magnitude of bus j in the kth contingency</td></tr><tr><td> $S_{lk}$ </td><td>power flow of line l in the kth contingency</td></tr><tr><td> $P_{i}^{\min}, P_{i}^{\max}$ </td><td>minimum and maximum real power capacity for generator i</td></tr><tr><td> $Q_{i}^{\min}, Q_{i}^{\max}$ </td><td>minimum and maximum reactive power capacity for generator i</td></tr><tr><td> $R_{i}^{\max}$ </td><td>maximum reserve for generator i</td></tr><tr><td> $V_{j}^{\min}, V_{j}^{\max}$ </td><td>voltage magnitude limits for bus j</td></tr><tr><td> $S_{l}^{\max}$ </td><td>power flow limit for line l</td></tr><tr><td> $C_{P_{i}}(P_{ik})$ </td><td>energy cost for operating generator i at output level  $P_{ik}$  in the kth contingency</td></tr><tr><td> $C_{R_{i}}(R_{ik})$ </td><td>reserve cost for generator i carrying  $R_{ik}$ </td></tr><tr><td></td><td>spinning reserve in the kth contingency</td></tr><tr><td> $P_{k}$ </td><td>the probability of the kth contingency</td></tr></table>

## 2.2. Co-optimization (CO-OPT) formulation

A few assumptions are made below in order to conceptually elaborate the proposed scheduling algorithm. However, they do not necessarily limit the algorithm and the solution.

(1) Only 10-min spinning reserves are considered.

(2) No double auction is considered for simplicity. The demand side is fixed, price-inelastic.

(3) Inter-temporal constraints are ignored, and schedules of different trading periods are independently determined.

(4) The CO-OPT considers a base case-intact system that runs smoothly with no failures, and a set of specified contingencies, which may contain line-out, unit failure, or unexpected load growth. These cases are predefined, and only one case happens at a time.

(5) A set of probabilities assigned to the base case and listed contingencies are also known.

The ISO requires an optimization procedure to determine the schedules to every supplier. The objective here is to minimize the total expected cost (operating energy cost plus the spinning reserve cost) over the predefined base case and credible contingencies, stated as follows,

$$
\min _ {P, R} \sum_ {k = 0} ^ {K} P _ {k} \left\{\sum_ {i = 1} ^ {I} \left[ C _ {P _ {i}} (P _ {i k}) + C _ {R _ {i}} (R _ {i k}) \right] \right\}\tag{1}
$$

The minimization is subject to network and system constraints imposed by each of the base case and contingencies. These constraints include nodal power balancing constraints,

$$
F _ {j k} (\theta , V, P, Q) = 0, \quad j = 1, \dots , J \quad k = 0, \dots , K\tag{2}
$$

line power flow constraints (detailed formulations for Eqs. (2) and (3) are referred to [10]),

$$
| S _ {l k} | \leq S _ {l} ^ {\max}, \quad l = 1, \dots , L \quad k = 0, \dots , K\tag{3}
$$

voltage limits

$$
V _ {j} ^ {\min} \leq V _ {j k} \leq V _ {j} ^ {\max}, \quad j = 1, \dots , J \quad k = 0, \dots , K\tag{4}
$$

real power limits

$$
P _ {i} ^ {\min} \leq P _ {i k} \leq P _ {i} ^ {\max}, \quad i = 1, \dots , I \quad k = 0, \dots , K\tag{5}
$$

reactive power limits

$$
Q _ {i} ^ {\min} \leq Q _ {i k} \leq Q _ {i} ^ {\max}, \quad i = 1, \dots , I \quad k = 0, \dots , K\tag{6}
$$

spinning reserve ramping limits

$$
0 \leq R _ {i k} \leq R _ {i} ^ {\max}, \quad i = 1, \dots , I \quad k = 0, \dots , K\tag{7}
$$

and unit capacity limits

$$
P _ {i k} + R _ {i k} \leq P _ {i} ^ {\max}, \quad i = 1, \dots , I \quad k = 0, \dots , K\tag{8}
$$

Notice that in Eqs. $( 5 ) – ( 8 ) , P _ { i } ^ { \mathrm { m a x } }$ and $R _ { i } ^ { \operatorname* { m a x } }$ are from the submitted offers, which may be lower than the actual physical limits due to sellers’ intentionally withholding of capacity.

The formulation so far can be decoupled into K+1 separate sub-problems (corresponding to specified K+1 systems) unless the concept of Total Unit Committed Capacity (TUCC) is introduced to tie them up. The TUCC of unit i in the kth contingency is defined as

$$
G _ {i k} = P _ {i k} + R _ {i k}, \quad i = 1, \dots , I \quad k = 0, \dots , K\tag{9}
$$

If a contingency such as a line-out or a unit failure occurs, the common remedy will be to fix the problem as soon as possible and bring the power grid back to its normal operating conditions (the base case). Hence, units are also expected to return to the base case dispatches (the least cost solution) upon the return of the failed component. To make this remedy possible for every listed contingency case, the TUCC required in each of the contingencies should be more than or at least equal to the base case TUCC. Meanwhile since our goal here is to minimize the total cost, we want as little capacity committed into the market as possible while still meeting the security criteria. For this purpose, the TUCC for any generator i is required to be the same over all K+1 cases, that is,

$$
G _ {i k _ {i}} = G _ {i k _ {2}}, \quad i = 1, \dots , I \quad k _ {1}, k _ {2} = 0, \dots , K\tag{10}
$$

From Eqs. (9) and (10), $R _ { i k }$ can be written as

$$
R _ {i k} = R _ {i 0} + P _ {i 0} - P _ {i k}, \quad i = 1, \dots , I \quad k = 1, \dots , K\tag{11}
$$

The equality constraints (11) then tie up the whole problem. Meanwhile, in the implementation, we can keep the base case reserve decision variables $R _ { i 0 }$ $( i { = } 1 , \ldots . , I )$ only and get rid of all other reserve decision variables by substituting the right-hand side of Eq. (11) for wherever $R _ { i k } \ ( i { = } 1 , . . . . , I , k { = } 1 , . . . , K )$ is used. By doing so, the problem size can be reduced such that implementation efficiency is improved. However, for the ease of conceptual illustration, we keep all $R _ { i k }$

## 2.3. Solution properties

P<sub>i</sub><sup>min</sup>, $P _ { i } ^ { \mathrm { m a x } }$ and $R _ { i } ^ { \operatorname* { m a x } }$ are the physical limits for unit i. They define the outer box (dotted line) in Fig. 1, together with the 45-degree line that indicates the unit capacity limit constraint,

$$
P _ {i} + R _ {i} \leq P _ {i} ^ {\max}\tag{12}
$$

The region inside the box is the feasible operating region for unit i. But, usually participating units will make strategic offers by withholding capacity according to real-time market situations. The offered-in limits $\tilde { P } _ { i } ^ { \mathrm { m a x } }$ and $\tilde { R } _ { \mathrm { i } } ^ { \mathrm { m a x } } ( P _ { \mathrm { i } } ^ { \mathrm { m i n } } { \leq } \tilde { P } _ { i } ^ { \mathrm { m a x } } { \leq } P _ { i } ^ { \mathrm { m a x } }$ , 0V $\tilde { R } _ { i } ^ { \mathrm { m a x } } { \leq } R _ { i } ^ { \mathrm { m a x } } )$ thus define a smaller feasible operating region (the inner dashed box), within which the optimal dispatch for unit i is scheduled.

The co-optimization contains (K+1) Optimal Power Flows (OPFs) only coupled by the reserve costs and the dependence of reserves on generation. Generally speaking, the optimal solution is different than (K+1) separate OPFs that do not consider the reserves. Assume the optimal energy dispatch for all K+1 cases, expressed in matrix, is

![](/api/attachments/V2F98EBC/fulltext/images/003f28ec54e048afe4dab8e817bb8f5b2c5ba7367da0871ead1d7f6ce83a3925.jpg)  
Fig. 1. Offer and solution pattern.

$$
\mathbf {P} = \left[ \begin{array}{c c c c} P _ {1 0} & P _ {2 0} & \dots & P _ {I 0} \\ P _ {1 1} & P _ {2 1} & \dots & P _ {I 1} \\ \vdots & \vdots & \vdots & \vdots \\ P _ {1 K} & P _ {2 K} & \dots & P _ {I K} \end{array} \right]\tag{13}
$$

Likewise, the optimal reserve allocation is

$$
\mathbf {R} = \left[ \begin{array}{c c c c} R _ {1 0} & R _ {2 0} & \dots & R _ {I 0} \\ R _ {1 1} & R _ {2 1} & \dots & R _ {I 1} \\ \vdots & \vdots & \vdots & \vdots \\ R _ {1 K} & R _ {2 K} & \dots & R _ {I K} \end{array} \right]\tag{14}
$$

$$
\begin{array}{l} G _ {i} ^ {\min} = \min (P _ {i 0}, P _ {i 1}, \ldots , P _ {i K}) \\ G _ {i} ^ {\max} = \max (P _ {i 0}, P _ {i 1}, \ldots , P _ {i K}) \quad i = 1, \ldots , I \end{array}\tag{15}
$$

In the optimal dispatch, for any unit i, there exists at least one case (out of K+1 cases) whose TUCC is consumed as energy only. That means, for that particular case (usually is the <sup>b</sup>worst<sup>Q</sup> system contingency for unit i), unit i does not carry any spinning reserve. All the spinning reserves it carries pick up part of the unserved load due to failure of other components. So, $G _ { i } ^ { \mathrm { m a x } }$ is unit i’s TUCC

$$
G _ {i k} = G _ {i} ^ {\max}, \qquad i = 1, \dots , I \qquad k = 0, \dots , K\tag{16}
$$

So, by performing the co-optimization, the ISO will assign every participating unit a response interval $[ G _ { i } ^ { \mathrm { m i n } } , \bar { G } _ { i } ^ { \mathrm { m a x } } ]$ . This interval means that no matter what the state of nature the power system is, unit i has to provide at least $G _ { i } ^ { \mathrm { m i n } }$ MW, additional energy within that interval may or may not be scheduled depending on whether the system is in the base or in one of the listed contingencies. The residual capacity in that interval will still be available and paid as reserves. That is, the actual operating point is on the solid line shown in Fig. 1, but the location varies dependent upon the actual real-time conditions.

## 2.4. Augmented Optimal Power Flow (AOPF)

The objective of the CO-OPT is to minimize the expected costs over all K+1 cases, therefore, the associated energy and reserve shadow prices are also in such an <sup>b</sup>expected<sup>Q</sup> fashion. However, suppliers would expect to be paid in a real-time, state-dependent fashion, i.e., the payment should correspond to the actual real-time system condition. Hence, a single OPF-like optimization is still needed under the framework of Responsive Reserves to solve for the real-time market, not only producing the same dispatches as in the CO-OPT solutions but also revealing spot prices. The Augmented OPF (AOPF), which adds reserves to the traditional OPF, is introduced below as such a real-time optimizing tool to accomplish this goal.

The AOPF is defined as the sub-problem of the cooptimization, which is the cost-minimizing optimization for one of the specified K+1 systems (the base case or contingencies). The objective of the kth AOPF is to minimize the total energy and reserve cost for the kth case.

$$
\min _ {P, R} \sum_ {i = 1} ^ {I} \left[ C _ {P _ {i}} (P _ {i k}) + C _ {R _ {i}} (R _ {i k}) \right]\tag{17}
$$

The constraints established for the kth system in Eqs. (2)–(7) still hold but with the change that the generation limits $( P _ { i } ^ { \operatorname* { m i n } } , P _ { i } ^ { \operatorname* { m a x } } )$ are replaced by the response intervals $( G _ { \mathrm { i } } ^ { \mathrm { m i n } } , G _ { i } ^ { \mathrm { m a x } } )$ obtained from the CO-OPT. In particular, generation limits in Eq. (5) are rewritten as

$$
G _ {i} ^ {\mathrm{min}} \leq P _ {i k} \leq G _ {i} ^ {\mathrm{max}}\tag{18}
$$

And the available spinning reserve is defined as

$$
R _ {i k} = G _ {i} ^ {\mathrm{max}} - P _ {i k}\tag{19}
$$

The AOPF has the required property as shown by the following proposition.

Proposition 1. If P (13) and R (14) are the optimal solutions to the CO-OPT (1), then for any $k { \in } \{ 0 , I , . . . . , K \} , \ \bar { P } _ { k } { = } P ( k , . )$ and $\bar { R } _ { k } { = } R ( k , : )$ are also the solutions to the kth AOPF (17\~19).

Proof. If not, then there exists at least one k(0VkVK), such that $( \hat { \bar { \mathrm { P } } } _ { \mathrm { k } } , \hat { \bar { \mathrm { R } } } _ { \mathrm { k } } )$ is the optimal solution to the kth AOPF, but $\bar { \mathsf { P } } _ { \mathrm { k } } { \neq } \bar { \mathsf { P } } _ { \mathrm { k } }$ and $\hat { \bar { \mathrm { R } } } _ { \mathrm { k } } { \neq } \bar { \bar { \mathrm { R } } } _ { \mathrm { k } } .$ . Since $( \hat { \bar { \mathrm { P } } } _ { \mathrm { k } } , \hat { \bar { \mathrm { R } } } _ { \mathrm { k } }$ produces lower cost to the kth AOPF than $( \bar { \mathsf { P } } _ { \mathrm { k } } , ~ \bar { \mathsf { R } } _ { \mathrm { k } } )$ does, substituting $( \bar { \mathrm { P } } _ { \mathrm { k } } , \ \bar { \mathrm { R } } _ { \mathrm { k } } )$ with $( \hat { \bar { \mathrm { P } } } _ { \mathrm { k } } , \ \hat { \bar { \mathrm { R } } } _ { \mathrm { k } } )$ in the optimal solution (P, R) to (1) should not only form a feasible solution, but also produce lower total expected cost, contradicting the fact that (P, R) is the optimal solution. 5

## 2.5. Real-time nodal pricing

The AOPF therefore will solve for the real-time market. The incremental costs—<sup>b</sup>the extra cost of producing an extra unit of output<sup>Q</sup> [9]—of energy and reserves are used to set prices at a nodal level.

The price definition is straightforward in a traditional OPF, and the nodal energy prices can be numerically calculated following the steps below (for the energy price at bus j):

(1) Do the original OPF, record the optimum operating cost as $f _ { 0 } .$

(2) Perturb the system by adding an extra unit of load at bus $j .$

(3) Do the perturbed OPF, record the minimum post-perturbation operating cost as $f _ { 1 }$

(4) The difference of $\mathrm { { { f } } } _ { 1 } \mathrm { { - } } f _ { 0 }$ then is the wanted nodal energy price.

In the RR market, nodal energy and reserve prices can be found in a similar way, but the perturbation is a bit subtler. Since we rely on the CO-OPT for the energy and reserve scheduling, the redispatch after perturbation in the AOPF should be consistent with the corresponding perturbed CO-OPT solution. From Proposition 1, we have a guarantee that both AOPF and CO-OPT have the same generator response intervals for each unit. So, in order to get energy prices, the perturbation has to be done to both CO-OPT and AOPF. In particular, the numerical calculation is performed as follows (for the energy price at bus j):

(1) Do the original co-optimization, carrying solved $[ G _ { i } ^ { \mathrm { m i n } } , G _ { \mathrm { i } } ^ { \mathrm { m a x } } ]$ for every unit to the AOPF; do the AOPF, record the optimum cost as $f _ { 0 } .$

(2) Perturb the co-optimization by adding one extra unit of load at bus j for each of the K+1 systems.

(3) Do the perturbed co-optimization, finding out the new response interval [newG<sub>i</sub><sup>min</sup>, new $G _ { i } ^ { \mathrm { m a x } } ]$ for every unit.

(4) Perturb the AOPF by adding one extra unit of load at bus $j .$

(5) Do the perturbed AOPF with [newG<sub>i</sub><sup>min</sup>, new $G _ { i } ^ { \operatorname* { m a x } } ]$ enforced, record the optimum post-perturbation operating cost as $f _ { 1 }$

(6) The difference of $f _ { 1 } - f _ { 0 }$ then is the wanted nodal energy price.

A similar procedure can be used to reveal the nodal reserve prices. Steps 1–3 are the same as above, but instead of doing a perturbed AOPF, an unperturbed AOPF is computed with [newG<sub>i</sub><sup>min</sup>, new $G _ { i } ^ { \operatorname* { m a x } } ]$ enforced such that the one extra unit of generation from the CO-OPT stage becomes one extra unit of reserve for bus j in the AOPF. Thus the cost difference is equal to the nodal reserve price at bus $j .$

Although the above procedures help understand the economic meaning of nodal prices, the numerical perturbation is very time-consuming to implement, especially for large-scale systems. In practice, postoptimization sensitivity analysis can provide a much more efficient way to compute these prices. Assume $\lambda _ { j }$ is the Lagrange multiplier associated with nodal real power balancing at bus j from the AOPF; $\mu _ { G _ { i } \mathrm { m i n } }$ and $\mu _ { G _ { i } \mathrm { m a x } } ~ ( i { = } 1 , 2 , . ~ . , I )$ are the Lagrange multipliers obtained from the AOPF related to the lower and upper boundaries of the generator response intervals. Define

$$
\alpha_ {i j} = \frac {\Delta G _ {i} ^ {\mathrm{min}}}{\Delta D _ {j}}\tag{20}
$$

$$
\beta_ {i j} = \frac {\Delta G _ {i} ^ {\mathrm{max}}}{\Delta D _ {j}}\tag{21}
$$

where $D _ { j }$ is the real load at bus $j . ~ \alpha _ { i j }$ is the sensitivity of change of $G _ { i } ^ { \mathrm { m i n } }$ with respect to the change of bus j load, that is, if there is one unit of load variation at bus $j , \alpha _ { i j }$ indicates the corresponding shift of $G _ { \mathrm { i } } ^ { \mathrm { m i n } } . \beta _ { i j }$ has a similar definition for $G _ { i } ^ { \mathrm { m a x } }$ . The real-time nodal energy price at bus $j , \bar { \lambda } _ { j } ,$ , then can be calculated as

$$
\bar {\lambda} _ {j} = \lambda_ {j} + \sum_ {i = 1} ^ {I} (\alpha_ {i j} \mu_ {G _ {i} ^ {\min}} + \beta_ {i j} \mu_ {G _ {i} ^ {\max}}), \quad j = 1, \dots , J\tag{22}
$$

The real-time nodal reserve price at bus $j , \bar { \mu } _ { j } ,$ is formulated as

$$
\bar {\mu} _ {j} = \sum_ {i = 1} ^ {I} (\alpha_ {i j} \mu_ {G _ {i} ^ {\min}} + \beta_ {i j} \mu_ {G _ {i} ^ {\max}}), \quad j = 1, \dots , J\tag{23}
$$

Therefore,

$$
\bar {\lambda} _ {j} - \bar {\mu} _ {j} = \lambda_ {j}\tag{24}
$$

The interpretation of these calculations can still be put in the context of load perturbation. $\lambda _ { j }$ will reflect the cost change in the AOPF if the load perturbation is done at bus j. Since the perturbation is performed in the AOPF without changing $[ G _ { i } ^ { \operatorname* { m i n } } , \ G _ { i } ^ { \operatorname* { m a x } } ]$ intervals, one unit of reserve will be called on to pick up the load perturbation, that is, one unit of reserve becomes one unit of energy. Therefore, the cost change involves both energy incremental cost and reserve decremental cost. That explains Eq. (24). Since the reserve price can be obtained by doing the unperturbed AOPF with [new $G _ { i } ^ { \mathrm { m i n } }$ , new $G _ { i } ^ { \operatorname* { m a x } } ]$ , the change of $[ G _ { i } ^ { \mathrm { m i n } } , G _ { i } ^ { \mathrm { m a x } } ]$ actually affects the reserve allocation and hence its price, which is consistent with the formulation of Eq. (23). The numerical check of Eqs. (22)–(24) has been done in Ref. [4], and the method used to compute $\alpha _ { i j }$ and $\beta _ { i j }$ is provided in Ref. [5].

## 3. Test system

The test system being used for the proposed RR market is a heavily modified IEEE 30-bus system [3] shown in Fig. 2. There are six firms in the joint market run by the ISO. Firm 1, 2, 3 and 4 are located in zone A while firm 5 and 6 are located in zone B. The transmission capacity between zone A and zone B is relatively limited (only 23 MVA in this case) compared to the transmission capacity within the two areas. Each firm owns two generators with a combined maximum capacity of 60 MW. The first generator has a maximum capacity of 40 MW, and the second has that of 20 MW. The two generators of each firm are the same within each area but different between areas. Table 1 lists generator data for firms in both areas. The system is designed so that the tie lines between areas are usually congested making zone B a load pocket, in which market power is easy to exploit. Interesting problems, such as the effects of transmission constraints and market power mitigation, therefore, can be studied using this test system (but they are beyond the scope of this paper, and are not addressed here).

![](/api/attachments/V2F98EBC/fulltext/images/0add8d2418997da92f1f9a8f80cea916fc152162d834659080b7f97bcf578d80.jpg)  
Fig. 2. Modified IEEE 30-bus test system.

## 4. Market tests

## 4.1. Incentive of market tests

The computer simulations in our previous work [4] have shown that the RR market outperforms the FR market (lower operating cost) with the same energy and reserve offers. However, it cannot determine whether or not the RR market is more efficient in revealing true energy and reserve costs, which is a very important issue in the market design. Another issue of great interest to us is the effect of replacing the reserve market by Opportunity Cost (OC) payments. In the joint energyreserve market, the OC for a generator is the foregone profit associated with the provision of reserves, which is equal to the product of: (1) the quantity of reserves provided and (2) the price difference between (a) the LBMP existing at the time the generator was instructed to provide reserves and (b) the generator’s energy offer for the same MW segment. Fig. 3 further illustrates how the OC is calculated. Payment of OC for the reserves actually makes the firm indifferent, in the sense of profit-making, to supplying energy or reserves, thus encouraging electricity suppliers to offer enough reserve capacity into the market. Also, notice in Fig. 3(b) that suppliers have the risk of providing free reserves if their energy offers are too high, thus discouraging speculative behavior. Our objective is to determine whether it is more efficient paying reserves directly versus paying an opportunity cost for energy forgone.

<table><tr><td rowspan="2"></td><td colspan="2">Zone A firms (1, 2, 3, 4)</td><td colspan="2">Zone B firms (5, 6)</td></tr><tr><td>Gen #1</td><td>Gen #2</td><td>Gen #1</td><td>Gen #2</td></tr><tr><td> $P_{i}^{\min }$ (MW)</td><td>8.0</td><td>0.0</td><td>8.0</td><td>4.0</td></tr><tr><td> $P_{i}^{\max }$ (MW)</td><td>40.0</td><td>20.0</td><td>40.0</td><td>20.0</td></tr><tr><td> $R_{i}^{\max }$ (MW)</td><td>5.0</td><td>10.0</td><td>20.0</td><td>16.0</td></tr><tr><td>Energyvariable cost(US$/MWh)</td><td>20.0</td><td>40.0</td><td>45.0</td><td>55.0</td></tr></table>

Experimental economics offers a tractable way to test markets. Knowledgeable subjects (students who have experiences with energy market experiments) are used to do the market test. The following sequence of tests using the same subjects is performed. The test starts with a relatively simple auction and adds new features one at a time, so that the subjects can learn how to exploit each new feature during the sequence of experiments. This type of evolution of a market structure in a sequence of tests represents a close parallel to the way that a real market like PJM has developed over time.

![](/api/attachments/V2F98EBC/fulltext/images/a7f7c982a38c90eecce11f9bd569fcc843e744345c6e44b1486e80c2f64f7f54.jpg)

(b) Energy offer at (G+R) > LBMP  
![](/api/attachments/V2F98EBC/fulltext/images/833f62962aef8cfce1abf41f6152951be0b9c1a0f75d496abf13da764bba589a.jpg)  
Fig. 3. Illustration of OC computation.

TEST I: Fixed Reserves (Two Markets, <sup>b</sup>New York-like Market Rules<sup>Q</sup>). Specify fixed MW amounts of reserves in the load pocket and overall to meet a specified set of contingencies. Minimize the cost of energy and reserves. Firms submit offers for both energy and reserves.

TEST II: Variable/Responsive Reserves (Two Markets, CO-OPT based). Minimize the expected cost of offers for energy and reserves over the same set of contingencies. The amount of reserves purchased is not constant and depends on the offers submitted and system conditions. Firms submit offers for both energy and reserves.

TEST III: Variable/Responsive Reserves (One Market+Opportunity Cost, CO-OPT based). Minimize the expected cost of offers for energy over the same set of contingencies. Firms submit offers for energy only. However, capacity submitted to the auction can be used for energy or for reserves. Capacity selected for reserves is paid the OC for foregone profit on energy.

## 4.2. Experimental design and market setup

The basic experimental design is to have two firms in a load pocket (zone B) interact with competitive suppliers in other regions to provide energy and reserves for the whole network. These four generators (two firms) are relatively expensive, and are represented by different individuals in a central auction. A price cap is enforced, but withholding capacity from the market is allowed. The other eight generators (four firms) outside the load pocket (zone A) are relatively inexpensive and they are price takers. Computer agents represent these eight generators and submit <sup>b</sup>honest offers<sup>Q</sup> for all of their capacity at the true cost in all periods. Nodal prices for energy and reserves are determined and paid to each supplier. The system load on the network is price inelastic, and it varies from period

to period with no forecasting errors. All of the markets will meet a specified level of reliability (i.e., providing reserves to cover the same set of contingencies). The market is a one-settlement market, representing a real-time market in which there is uncertainty about which one of the listed contingencies could occur.

The reserve requirement for the Fixed Reserve (FR) market is set such that the loss of the largest unit can be covered. Due to transmission limits between areas, the regional reserve requirement is established, which is a close parallel to the way that NYISO sets the reserve requirement: 40 MW reserves are required inside zone B and 60 MW total are required for the whole system. So that, if the largest unit in zone B (40 MW) is lost, the 40

(a) Average payment  
![](/api/attachments/V2F98EBC/fulltext/images/5dfa7e9ef8a6546d2820666a631a08ab90aa732c4028a95e2bbf8203e7c80170.jpg)

(b) Average earnings  
![](/api/attachments/V2F98EBC/fulltext/images/5524d3a4487c162369f842cf127439333de883da4d33970bb79cf920ceeb0b69.jpg)  
Fig. 4. Experiment results for TEST I.

MW reserves inside zone B are able to cover the contingency; if the largest unit in zone A (40 MW) is lost, presumably, there will be 20 MW reserves available in zone A and another 20 MW can be pulled out from the tie lines (normally the power transferring from zone A to zone B congests the tie lines) to handle the loss of the unit, and 20 MW is also needed in zone B to compensate the missing 20 MW withdrawn from the tie lines.

(a) Average payment  
![](/api/attachments/V2F98EBC/fulltext/images/42c17ebd846bbc2533fe3d2c91ae254c0010d9d0ed43194a8d31cf38a3311730.jpg)

(b) Average earnings  
![](/api/attachments/V2F98EBC/fulltext/images/82246aa133bff5dda07d6ec656e166bdc077e949b0493f28b19b3fe0f45e280d.jpg)  
Fig. 5. Experiment results for TEST II.

For the RR market, six contingencies are considered in the credible contingency list, which are 10% unexpected load growth and the failure of the biggest unit (40 MW unit) of all firms except firm 2 (firm 1 and firm 2 are in similar situations, both of them affect the system in a similar fashion, hence only one of them is considered in order to shorten the contingency list). These contingencies are selected so that both the FR and RR markets can cover the

(a) Average payment

![](/api/attachments/V2F98EBC/fulltext/images/18a26dd602917a3fe6206ced0e7e21dcf6669df1b926c056cdba05ec2f2e23f6.jpg)  
(b) Average earnings

TEST III : Variable Reserve Requirements  
(Co-optimization & Pay Opportunity Cost) Average Payment/Firm/Period  
![](/api/attachments/V2F98EBC/fulltext/images/e903184d8a9d8ce88e19f030e5e4b6113faca0e46712491add48b286d8d9bd8c.jpg)  
Fig. 6. Experiment results for TEST III.

same set of contingencies in order to do fair comparisons.

The base load of the test market is set to be 220 MW with 150.8 MW in zone A and the rest in zone B, as shown in Fig. 2. The load varies proportionally across the network from one trading period to another and is within F40 MW of the base load. Most of the time (80%), the power grid runs smoothly without any failures, which is the designated base case. However, there is a 20% chance that one of the credible contingencies will occur. The six contingencies will occur equally likely. Six firms, each manipulating two units, will submit energy and reserve offers to the market. Although a piecewiselinear offer curve can be handled [3], the offer curve for each generator is linear in these tests. That is, each unit is only allowed to submit one block and one offer price for energy and reserves respectively, but some capacity can be withheld.

## 4.3. Test results

There are eight groups of subjects participating in TEST I and TEST II, and seven groups of subjects participating in TEST III. Each test consists of 25 trading periods.

The experiment results for the three tests are shown in Figs. 4–6, respectively. The (a)-subfigures compare the average payment (defined in Eq. (25)) in different regions for each of the 25 trading periods. The solid line denotes the average payment in zone B, the dotted line represents that of zone A, and the dashed line shows the average payment regarding the whole system.

Average payment

$$
\begin{array}{r l} & = (\text { total   energy   payout } + \text { total   reserve   payout }) \\ & / \text { total   energy   amount   generated } \end{array}\tag{25}
$$

Average earnings

¼ total earnings in one region

$$
/ \text { number   of   firms   in   that   region }\tag{26}
$$

The (b)-subfigures examine the average earnings (defined in Eq. (26)) of computer agents in zone A (white bars) and those of subjects in zone B (black bars); the results are displayed for each group. The mean of the average payment in zone B decreases from TEST I to TEST III monotonically. In particular, US\$121.82/MWh in TEST I, US\$94.37/MWh in TEST II, and US\$70.62/MWh in TEST III. The differences between these numbers are significant. So are the average earnings of zone B firms, numerically US\$1706.50 in TEST I, US\$1166.43 in TEST II, and only US\$430.00 in TEST III.

The comparison between TEST I and II shows that the co-optimization is more efficient in revealing generators’ true costs, which means the RR market is more competitive. Notice that the market design includes a <sup>b</sup>load pocket<sup>Q</sup>. In the FR market, only two firms compete against each other for the zone B (the load pocket) reserve requirement; however, in the RR market, all six firms will compete for reserves because of the <sup>b</sup>smart<sup>Q</sup> way (the CO-OPT) of allocating reserves. Therefore, the market power within zone B is easier to identify and exploit in the FR market, and this accounts for the higher prices in TEST I. The comparison also suggests that the RR market can mitigate market power to some extent. Another observation is that the range of the average payments in TEST I is much wider than that of TEST II, which implies that the RR market was not fully exploited in some cases. Prices in TEST I could have been even higher if the tests had been run longer. The further decreased average payment and earnings in TEST III compared to those in TEST II suggest that the OC payment actually discourage speculative behavior in the RR market. This is a good signal for market design and the ultimate goal-competitive market.

## 5. Conclusions and future research

The RR framework for an integrated energyreserve market has been presented in this paper. Energy and reserves interact more effectively with each other in the RR framework than they do in the FR market. Hence the RR market has the potential advantage of being more difficult to exploit when market power is a potential problem. The underlying optimization procedure provides not only locational assignments but also locational prices for both energy and reserves. Primary tests on the market design have been done based on a modified IEEE 30-bus system.

Market tests were performed using students, and more tests with experienced professionals are needed to confirm the results. The results from the class tests show that,

(1) Using variable/responsive reserves (CO-OPT) is a promising way to reduce the market power, which is inherent with fixed zonal reserves, as well as to calculate nodal prices for both energy and reserves.

(2) Paying reserves the opportunity cost of forgone profits for energy is a promising way to mitigate speculative behavior compared to paying separate prices for energy and reserves. (Greedy suppliers who try to get high energy prices also provide low cost reserves.)

The unit thermal constraints, such as minimum up/ down time, start-up costs, and other temporal issues, were ignored in the current stage of development. However, the optimization framework and solutions are not necessarily limited by the assumptions made in this paper. Solving the unit commitment procedure based on the same optimization framework will be an important next step.

The test system used so far is only a small-size system. Applying the proposed RR framework to real-size systems is also an important next step. The RR framework is tested here in a one-settlement market setup, but the same concept can also be applied to other market forms, for example, a twosettlement market. The co-optimization can be used, for instance, in the day-ahead market to determine the optimum pattern of energy dispatch and reserves to meet the forecasted load and cover specified contingencies. In addition, various forms of dayahead financial commitments, dependent upon different sets of market rules, can also be included in the co-optimization solutions.

Our main conclusion is that the RR framework will improve market performance and achieve better economic efficiency than the existing form of market with fixed requirements for reserves.

## Acknowledgements

This work was coordinated by the Consortium for Electric Reliability Technology Solutions, and funded by the Assistant Secretary of Energy

Efficiency and Renewable Energy, Office of Distributed Energy and Electricity Reliability, Transmission Reliability Program of the U.S. Department of Energy under Interagency Agreement No. DE-AI-99EE35075 with the National Science Foundation.

## References

[1] F.L. Alvarado, et al., The Value of Transmission Security, EPRI TR-103634 Research Project 4000-14, Final Report (Aug. 1994).

[2] Y. Chen, V. Venkatasubramanian, Automatic on-line controller for coordinated slow voltage control, IEEE Trans. on Power Systems, in press.

[3] J. Chen, J.S. Thorp, R.J. Thomas, Time–space methods for determining locational reserves: a framework for locationbased pricing and scheduling for reserve markets, CERTS Report on Reliability Adequacy Tools, 2002 (Dec.).

[4] J. Chen, J.S. Thorp, R.J. Thomas, T.D. Mount, Locational pricing and scheduling for an integrated energy-reserve market, 36th Hawaii International Conference on System Science (Hawaii, Jan.), 2003.

[5] J. Chen, J.S. Thorp, T.D. Mount, Coordinated interchange scheduling and opportunity cost payment: a market proposal to seams issues, 37th Hawaii International Conference on System Science (Hawaii, Jan.), 2004.

[6] A.A. Fouad, Dynamic security assessment practices in North America, IEEE Transactions on Power Systems 3 (3) (1988 (Aug.)) 1310 – 1321.

[7] NYISO reserve requirement, http://www.nyiso.com/oasis/ misc\_pdf/nyiso\_locational\_reserve\_reqmts.pdf.

[8] F.C. Schweppe, M.C. Caraminis, R.D. Tabors, R.E. Bohn, Spot Pricing of Electricity, Kluwer Academic Publishers, 1988.

[9] S. Stoft, Power System Economics: Designing Markets for Electricity, Wiley-IEEE Press, 2002 (May).

[10] A.J. Wood, B.F. Wollenberg, Power Generation, Operation, and Control, John Wiley and Sons, New York, 1996.

![](/api/attachments/V2F98EBC/fulltext/images/04e0d7eee77cc1430bf0025fca6a1422a3b290ce39468709bea2859b7e221c5a.jpg)  
Jie Chen was born in China in 1974. He received a BS degree and a MS degree in Electrical Engineering from Tsinghua University, China in 1997 and 1999. He is currently enrolled in the PhD program in Electrical Engineering at Cornell University in Ithaca, NY, USA. His research interests include computer simulation of power systems, electricity market and complex systems.

![](/api/attachments/V2F98EBC/fulltext/images/3d035416e64371d5b2df9799e6b1921b10d2b40b378d614cf3dbf7fcd4dd3448.jpg)  
Timothy D. Mount is a professor in applied economics and management at the Cornell University. His research interests include econometric modeling and policy analysis relating to the use of fuels and electricity, and to their environmental consequences (acid rain, smog, and global warming). He is currently conducting research on the restructuring of markets for electricity and the implications for price behavior in auctions for

![](/api/attachments/V2F98EBC/fulltext/images/6a0e399f3a22141d7e26be0159c3197b85a56961ceb52237a7607d75014e1e05.jpg)  
Robert J. Thomas is a professor in electrical and computer engineering at the Cornell University. His current research interests are broadly in the areas of analysis and control of nonlinear continuous and discrete-time systems with applications to large-scale electric-utility systems and electromechanical-drive systems.

electricity, the rates charged to customers, and the environment.

![](/api/attachments/V2F98EBC/fulltext/images/b007fa744e1b9ab5d17c25828aba561ead9b1610a927f0156b2804f3dd3e5e52.jpg)

James S. Thor is the Charles N. Mellowes Professor in Engineering. In 1976, he was a faculty intern at the AEP Service Corporation. He was an associate editor for IEEE Transactions on Circuits and Systems from 1985 to 1987. In 1988, he was an overseas fellow at Churchill College, Cambridge, England. He is a member of the National Academy of Engineering, a Fellow of IEEE and a member of the IEEE Power System Relaying Committee, CIGRE, Eta Kappa

Nu, Tau Beta Pi and Sigma Xi. From 1994 to 2000, he was Director of the School of Electrical Engineering at Cornell University.
