---
otero_id: 21660
otero_key: "6BG9AXKS"
title: "Scheduling of thermal units with a nonlinear load flow network model"
authors: "Carlos Murillo-Sánchez; Robert J. Thomas"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00073-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Scheduling of thermal units with a nonlinear load flow network model

Carlos Murillo-Sanchez <sup>a,)</sup>, Robert J. Thomas <sup>b,1</sup> ´

a Cornell UniÕersity, School of Electrical Engineering, 428 Phillips Hall, Ithaca, NY 14853, USA

<sup>b</sup> Cornell UniÕersity, School of Electrical Engineering, 428D Phillips Hall, Ithaca, NY 14853, USA

## Abstract

We describe a formulation of the thermal unit commitment problem that includes AC network constraints, which allows taking into account VAr production as a criterion for generator commitment for the first time. The formulation makes it possible to use the Lagrangian Relaxation technique as a solution algorithm even though the network constraints are not linear. Although the solution method is computationally intensive, the problem exhibits a separation structure and a price coordination schedule that suggest several ways of improving the performance. Preliminary test results are reported. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Unit commitment; Resource scheduling; Lagrangian relaxation; Separable programming

## 1. Introduction

Lagrangian relaxation as a technique for unit commitment has come a long way since it was first introduced, but there has been one constant central theme all along, namely, that of separability. Since the early papers 13,14 , this decomposability has been the sought-after quality, and for a good reason: the unit commitment problem, being of a mixed-integer nature, suffers from combinatoric complexity as the number of generators increases. It is this feature that dooms other algorithms intended for solving it, such as dynamic programming: the combined state space of several generators in a dynamic program has a size that is too large to be able to tackle many realistic problems, even with limited-memory schemes. And it only gets worse as other constraints that increase the required state space such as limited ramp rates are introduced.Ž .

Lagrangian relaxation permits the decomposition of the problem into several one-machine problems at each iteration; the coupling to other constraints involving more machines is achieved by sharing price information that is updated from one iteration to another. The complexity of a given iteration becomes linear in the number of generators instead of geometric. This property is what has given the technique an increased acceptance when compared to other techniques such as dynamic programming and branch and bound algorithms.

Mathematically, the unit commitment problem can be formulated as:

$$
\min _ {P, Q, U} \left\{F (P, U) + K (U) \mid (P, U) \in \mathscr {D}, (P, Q, U) \in \mathscr {S}, (P, Q, U) \in \mathscr {C} \right\}\tag{1}
$$

where $F ( P , U )$ is the total production cost; $K ( U )$ is the sum of any startup costs; P is $( p ^ { i , t } ) , i = 1 , . . . , n _ { \mathrm { g } }$ $t = 1 , \ldots , n _ { \mathrm { t } } ; Q$ $n _ { \mathrm { t } } ; Q \mathrm { ~ i s ~ } ( q ^ { i , t } ) , i = 1 , \ldots , n _ { \mathrm { g } } , t = 1 , \ldots , n _ { \mathrm { t } } ; U \mathrm { ~ i s ~ } ( u ^ { i , t } ) , i = 1 , \ldots , n _ { \mathrm { g } } , t = 1 , \ldots , n _ { \mathrm { t } } ; p ^ { i , t } \in \mathbb { Z } .$ is the real power output for generator i at time $t ; \ q ^ { i , \breve { t } }$ is the reactive power output for generator i at time $t ; \boldsymbol { u } ^ { i , t }$ is the on<sup>r</sup>off status 1 or 0 for generator Ž . i at time $t ; n _ { \mathrm { t } }$ is the length of the planning horizon; $n _ { \mathrm { g } }$ is the number of generators to schedule; <sub>D</sub> is a set of dynamic generator-wise constraints; $\mathcal { S }$ is a set of static instantaneous constraints; $\mathcal { C }$ is a set of nonseparable constraints.

It is assumed that the production cost function F is convex and separable over each generator and time period so that $\begin{array} { r } { F ( P , U ) = \mathrm { \bar { \sum } } _ { t = 1 } ^ { n _ { \mathrm { t } } } \sum _ { i = 1 } ^ { n _ { \mathrm { g } } } u ^ { i , t } F ^ { i } ( p ^ { i , t } ) } \end{array}$ . For our purposes, the constraints of the problem have been separated into three kinds: The set $\mathcal { D }$ contains constraints that pertain to a single generator, but may span several time periods. These include minimum up or down times and ramping constraints. The set $\mathcal { S }$ contains constraints that span the complete system but involve only one time period, such as load<sup>r</sup>demand matching, voltage limits, reserve constraints and generation upper<sup>r</sup>lower limits. Finally, $\mathcal { C }$ is the set of constraints that involve more than one generator and more than one time period. A typical example is the infeasibility of turning on more than one unit at a time in a given location because of crew constraints.

Muckstadt and Koenig 14 introduced a first version of Lagrangian relaxation for the unit commitment <sup>w</sup> <sup>x</sup> problem. They considered a lumped one-node network with losses modeled as a fixed penalty factors. Reserve constraints were also considered. To illustrate the separation structure, we write an example formulation including demand and reserve constraints. Their relaxation yields a Lagrangian

$$
\mathfrak {L} (P, U, \lambda , \beta) = F (P, U) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \lambda^ {t} \left(P _ {\mathrm{D}} ^ {t} - \sum_ {i = 1} ^ {n _ {\mathrm{g}}} u ^ {i, t} p ^ {i, t}\right) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \beta^ {t} \left(R ^ {t} - \sum_ {i = 1} ^ {n _ {\mathrm{g}}} u ^ {i, t} P _ {\max} ^ {i}\right)\tag{2}
$$

where $P _ { \mathrm { ~ D ~ } } ^ { t }$ is the real power demand in period t and $R ^ { t }$ is the desired minimum total committed capacity for the same period. One can then consider the dual objective

$$
q (\lambda , \beta) = \min _ {P, U} \mathfrak {L} (P, U, \lambda , \beta)\tag{3}
$$

and corresponding dual problem

$$
\max _ {\lambda \geq 0,   \beta \geq 0} q (\lambda , \beta)\tag{4}
$$

which can be written explicitly in the following form after collecting terms on a per-generator basis

$$
\max _ {\lambda \geq 0, \beta \geq 0} \left\{\sum_ {t = 1} ^ {n _ {\mathrm{t}}} \left(\lambda^ {t} P _ {\mathrm{D}} ^ {t} + \beta^ {t} R ^ {t}\right) + \min _ {P, U} \left[ \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \left(u ^ {i, t} F ^ {i} \left(p ^ {i, t}\right) - \lambda^ {t} u ^ {i, t} p ^ {i, t} - \beta^ {t} u ^ {i, t} P _ {\max} ^ {i}\right) \right] \right\}.\tag{5}
$$

Thus, for fixed and $\beta _ { : }$ , finding the value of $q ( \lambda , \beta )$ amounts to solving $n _ { \mathrm { g } }$ separate, single-generator dynamic programs of the form

$$
\min _ {p ^ {i:}, u ^ {i:}} \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \left(u ^ {i, t} F ^ {i} \big (p ^ {i, t} \big) - \lambda^ {t} u ^ {i, t} p ^ {i, t} - \beta^ {t} u ^ {i, t} P _ {\max} ^ {i}\right).\tag{6}
$$

These dynamic programs can actually accommodate any <sub>D</sub>-type constraint such as minimal up or down times, as well as any startup costs. Ramp rate constraints can also be introduced by discretizing the generation range for the unit, although the size of the state space grows considerably. For a detailed description of a dynamic programming graph including most of these constraints, see Ref. 10 . <sup>w</sup> <sup>x</sup>

This suggests that a dual maximization algorithm is better suited to this particular problem because it can exploit the separation structure of the dual objective. A subgradient-based dual maximization algorithm applied to the unit commitment problem proceeds as follows:

## Algorithm 1: Classical Lagrangian relaxation

Step 0. k§0.

Step 1. Initialize $\lambda _ { k }$ and $\beta _ { k }$ to a sensible under estimate value. Ž .

Step 2. Compute

$$
\left(\hat {P} _ {k}, \hat {U} _ {k}\right) \leftarrow \arg \min _ {\text { feasible } P, U} \mathfrak {L} (P, U, \lambda_ {k}, \beta_ {k})
$$

by solving $n _ { \mathrm { g } }$ single-generator dynamic programs that incorporate any ${ \mathcal { D } } .$ type constraints and any startup costs.

Step 3. The dual cost is $q ( \lambda _ { k } , \beta _ { k } ) = \mathfrak { L } ( \hat { P _ { k } } , \hat { U _ { k } } , \lambda _ { k } , \beta _ { k } ) .$

Step 4. The primal cost is infinite if the schedule $\hat { U } _ { k }$ is infeasible; else it is the value of

$$
\min _ {\text { feasible } P} F \big (P, \hat {U} _ {k} \big)
$$

where P being feasible means that it satisfies the demand. This problem is separable into $n _ { \mathrm { t } }$ economic dispatches. If there are any startup costs, they should be added, too.

Step 5. Compute the duality gap at this iteration as primal cost–dual cost.

Step 6. If the gap is small enough, stop; else, update ,  according to a subgradient maximization technique, for example, Poljak’s formula:

$$
\lambda_ {k + 1} ^ {t} \leftarrow \lambda_ {k} ^ {t} + \frac {1}{\alpha_ {0} + \alpha_ {1} k} \left(P _ {\mathrm{D}} ^ {t} - \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \hat {u} ^ {i, t} \hat {p} ^ {i, t}\right)
$$

$$
\beta_ {k + 1} ^ {t} \leftarrow \beta_ {k} ^ {t} + \frac {1}{\alpha_ {0} + \alpha_ {1} k} \left(R ^ {t} - \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \hat {u} ^ {i, t} P _ {\max} ^ {i}\right)
$$

Step 7. $k \gets k + 1$ ; go to Step 2.

Such is the basic idea behind Lagrangian relaxation. In the past 20 years, advances have been made in several areas, enhancing the number and type of constraints that can be treated, addressing some convergence issues when the cost is not strongly convex, and so on. In 1983, Bertsekas et. al. 6 described an algorithm that included many refinements in the dynamic programming subproblem, as well as proof that the expected relative duality gap is inversely proportional to the number of generators; this was good news for large-scale problems. Also in 1983, Merlin and Sandrin 11 reported a Lagrangian relaxation method with linear costs, reserve<sup>w</sup> <sup>x</sup> constraints, exponential restart costs but not banking capabilities and special -updates that take into account the kind of constraints that are violated and some properties of linear cost functions. In 1988, Zhuang and Galiana 19 reported a three-stage method involving 1 standard Lagrangian relaxation without reserve  Ž . constraint, 2 a reserve feasibility search, and 3 an economic dispatch stage. At the time, several methodolo-Ž . Ž . gies for achieving reserve feasibility were being tested. Most relied on further stepping up the multipliers for the demand constraints, thus increasing the number of committed generators. At issue was whether to raise all multipliers simultaneously or sequentially, starting with those of time periods where the reserve constraint was most unfulfilled. Reserve feasibility search has been an active area and the difficulty is especially important in so-called indirect methods. In Ref. 16 , Shaw distinguishes between<sup>w</sup> <sup>x</sup> direct and indirect methods, where the former address reserve feasibility and other Optimal Power Flow OPF constraints in the dual optimizationŽ . phase, whereas the latter deal with such constraints only after having generated a commitment schedule with a dual maximization that did not include such constraints and thus make post factum corrections. Clearly, if some constraints were not included in the formulation of the dual problem in the first place, primal feasibility is even more of an issue.

Sophisticated as the schemes were becoming, the underlying network was being largely ignored. In Ref. 15 ,<sup>w</sup> <sup>x</sup> Ruzic and Rajakovic include transmission line transfer limits using a DC flow model and transmission lossesˇ ´ ´ using constant factors. This can be done because in the Lagrangian such relaxed constraints are linear in $u ^ { i , t } p ^ { i , t }$ and $\boldsymbol { u } ^ { i , t }$ , so it is still possible to collect all terms on a per-generator basis, achieving separation into $n _ { \mathrm { g } }$ dynamic programs. However, even with just two congested lines the computation times escalated. This seems to be inherent to binding constraints in subgradient methods, especially if poorly scaled.

Several other papers have followed the DC flow formulation in their incorporation of line limits to the dual maximization, including Refs. 1,4,5,16,18 . Baldick 4 uses a general formulation that could in principle be <sup>w</sup> <sup>x</sup> <sup>w x</sup> used to address AC flow constraints, but the specific algorithm that he describes still uses a basic DC flow approximation. It seems that the general rule of thumb is: if a constraint is linear, then add it to the Lagrangian, appropriately relaxed with a multiplier, and separation will be preserved. As a matter of fact, any constraint $\begin{array} { r } { g ( P , U ) = \sum _ { t = 1 } ^ { n _ { \mathrm { t } } } \sum _ { i = 1 } ^ { n _ { \mathrm { g } } } g ^ { i , t } ( u ^ { i , t } , p ^ { i , t } ) } \end{array}$ can be addressed in the dual maximization while preserving separation. Others have followed this trend of addressing more and more linear constraints in the dual optimization. For example, in Ref. 9 , ramping constraints are relaxed as well, so that the dynamic programs do not have to deal<sup>w</sup> <sup>x</sup> explicitly with ramp constraints, but $2 n _ { \mathrm { t } } n _ { \mathrm { g } }$ more multipliers are needed. This idea is also used in Ref. 17 . <sup>w</sup> <sup>x</sup>

There are several possible drawbacks to this overall scheme of adding more linear constraints to the formulation and dealing with them in the dual optimization phase. The first one is that the number of dual variables grows very large. In general, this does not seem to be a problem with regards to convergence, unless many of the constraints that they represent are actually binding. However, it does increase the amount of memory needed: for line limit multipliers, for example, $2 n _ { \mathrm { l } } n _ { \mathrm { t } }$ variables may be needed, $n _ { 1 }$ being the number of lines in the network.

The second drawback applies to only some types of constraints, such as line limits modeled by means of DC flow sensitivities: they are not sparse, although one could conceivably zero out small elements. This does not apply to inherently sparse constraints such as ramp rate limits, but hinders the scalability of the non-augmented Ž . i.e., not including angle variables DC flow approach to incorporation of line limits. This is especially true when considering line outages that are valid only for some time periods, because then it would be necessary to consider several sets of sensitivities.

However, the fundamental drawback of the DC flow model comes from the fact that it is just an approximation that 1 may be significantly off in some cases, and 2 throws away information that is important Ž . Ž . for the formulation of some important constraints. As an example of the first problem, consider line transfer limits. The DC flow model approximates the amount of real power flowing in a given line. However, line limits are best modeled as current limits or MVA limits, since these quantities are more directly related to the actual heating of the wires than the amount of real power flowing in a line. Now let us consider voltage limits as an example of the second problem. Such important constraints cannot be formulated as linear; it is necessary to perform a power flow to investigate their values. However, one should notice that, complicated as AC OPF constraints are, they still fall neatly into the category of <sub>S</sub>-type constraints: they apply to all generators, but only at one time period. We shall take advantage of this in Section 2.

## 2. Unit commitment with AC OPF formulation

Our approach has its roots in the Õariable duplication technique credited to Guy Cohen in Ref. 5 by Batut<sup>w</sup> <sup>x</sup> and Renaud. This same technique was used later by Baldick 4 in his more general formulation of the unit<sup>w</sup> <sup>x</sup> commitment problem. The main technical achievement of our paper is the inclusion of reactive power output variables to the formulation, so that better loss management may be performed and generators that are necessary because of their VAr output but not their real power are actually committed. This is the logical next step in the development of Lagrangian relaxation techniques for the unit commitment problem. At this point, when typical algorithms reduce the duality gap to figures close to 1%, it is important to recognize that a better handling of the reactive power considerations at the unit commitment stage may have a payoff that is higher than those few last percentage points in the duality gap.

We start by defining two sets of variables, the dynamic Õariables and the static ones:

$$
u ^ {i, t}
$$

Commitment status 0,1 for generator  4 i at time t

$$
d _ {\mathrm{p}} ^ {i, t}
$$

Real power output for generator i at time t

$$
d _ {\mathrm{q}} ^ {i, t}
$$

VAr output for generator i at time t

$$
U
$$

$$
(u ^ {i, t}), i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}
$$

$$
D _ {\mathrm{p}}
$$

$$
(d _ {\mathrm{p}} ^ {i, t}), i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}
$$

$$
D _ {\mathrm{q}}
$$

$$
(d _ {\mathrm{q}} ^ {i, t}), i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}
$$

$$
(D _ {\mathrm{p}}, D _ {\mathrm{q}})
$$

Static

Real power output for generator i at time t

$$
S _ {\mathrm{q}} ^ {l, t}
$$

VAr output for generator i at time t

$$
S _ {\mathrm{p}}
$$

$$
(s _ {\mathrm{p}} ^ {i, t}), i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}
$$

$$
S _ {\mathrm{q}}
$$

$$
(s _ {\mathrm{q}} ^ {i, t}), i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}
$$

$$
S
$$

$$
(S _ {\mathrm{p}}, S _ {\mathrm{q}})
$$

Then the following optimization problem is defined.

$$
\min _ {D, U, S} \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \left[ u ^ {i, t} F ^ {i} \left(d _ {\mathrm{p}} ^ {i, t}\right) + K ^ {i, t} \left(u ^ {i, \cdot}\right) \right]\tag{7}
$$

subject to the following constraints.

Ž .i <sub>D</sub>-type constraints:

$$
u ^ {i, t} P _ {\mathrm{min}} ^ {i} \leq u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} \leq u ^ {i, t} P _ {\mathrm{max}} ^ {i},\tag{8}
$$

$$
u ^ {i, t} Q _ {\min} ^ {i} \leq u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} \leq u ^ {i, t} Q _ {\max} ^ {i},\tag{9}
$$

U satisfies minimal up and down times.

10 Ž .

Ž . ii <sub>S</sub>-type constraints:

$$
0 \leq s _ {\mathrm{p}} ^ {i, t} \leq P _ {\max} ^ {i},\tag{11}
$$

$$
Q _ {\mathrm{min}} ^ {i} \leq s _ {\mathrm{q}} ^ {i, t} \leq Q _ {\mathrm{max}} ^ {i},\tag{12}
$$

$\left( S _ { \mathrm { p } } , S _ { \mathrm { q } } \right)$ satisfies the network load flow equations while respecting line MVA limits and voltage limits.

Ž . 13

Ž . iii The following additional constraints:

$$
R ^ {l, t} - \sum_ {i \in Z _ {l}} u ^ {i, t} P _ {\max} ^ {i} \leq 0, \quad l = 1, \dots , n _ {\mathrm{z}}, t = 1, \dots , n _ {\mathrm{t}}\tag{14}
$$

$$
s _ {\mathrm{p}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} = 0, \qquad i = 1, \ldots , n _ {\mathrm{g}}, t = 1, \ldots , n _ {\mathrm{t}}\tag{15}
$$

$$
s _ {\mathrm{q}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} = 0, \quad i = 1, \dots , n _ {\mathrm{g}}, t = 1, \dots , n _ {\mathrm{t}}\tag{16}
$$

where $R ^ { l , t }$ is the minimum combined capacity that is acceptable for the lth zone in the tth period and $Z _ { l }$ is the set of indices of generators in the lth zone.

We will assume that we can enforce both the $\mathcal { D }$ constraints 8–10 and theŽ . $\mathcal { S }$ Ž .constraints 11–13 , so that we only relax the three last constraints 14–16 , which leads to the following Lagrangian:Ž .

$$
\begin{array}{l} \mathfrak {L} (U, D, \lambda , \beta) = \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \Big [ u ^ {i, t} F ^ {i} \big (d _ {\mathrm{p}} ^ {i, t} \big) + K ^ {i, t} (u ^ {i, \cdot}) \Big ] + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {l = 1} ^ {n _ {\mathrm{z}}} \beta^ {l, t} \bigg (R ^ {l, t} - \sum_ {i \in Z _ {l}} u ^ {i, t} P _ {\max} ^ {i} \bigg) \\ \qquad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \lambda_ {\mathrm{p}} ^ {i, t} \big (s _ {\mathrm{p}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} \big) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \lambda_ {\mathrm{q}} ^ {i, t} \big (s _ {\mathrm{q}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} \big) \end{array}\tag{17}
$$

$$
+ \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \left(\lambda_ {\mathrm{p}} ^ {i, t} s _ {\mathrm{p}} ^ {i, t} + \lambda_ {\mathrm{q}} ^ {i, t} s _ {\mathrm{q}} ^ {i, t}\right) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {l = 1} ^ {n _ {\mathrm{z}}} \beta^ {l, t} R ^ {l, t}\tag{18}
$$

$$
\mathfrak {L} (U, D, \lambda , \beta) = \mathfrak {L} _ {1} (U, D, \lambda , \beta) + \mathfrak {L} _ {2} (S, \lambda) + \mathfrak {L} _ {3} (\beta)\tag{19}
$$

where $\lambda = \big ( \lambda _ { \mathfrak { p } } ^ { i , t } , \lambda _ { \mathfrak { q } } ^ { i , t } \big )$ are multipliers on the relaxed equalities of the two kinds of variables, $\beta ^ { l , t }$ is the multiplier associated with the lth zone’s reserve requirement at the tth period, and $\boldsymbol { z } ( i )$ returns the index of the zone to which generator i belongs.

The separation structure of the Lagrangian is obvious upon looking at Eqs. 18 and 19 . It makes it possible Ž . Ž . to write the dual objective as

$$
\begin{array}{l l} q (\lambda , \beta) & = \min _ {U, D, S} \left\{\mathfrak {L} _ {1} (U, D, \lambda , \beta) + \mathfrak {L} _ {2} (S, \lambda) + \mathfrak {L} _ {3} (\beta) \right\} \\ & = \min _ {U, D} \mathfrak {L} _ {1} (U, D, \lambda , \beta) + \min _ {S} \mathfrak {L} _ {2} (S, \lambda) + \mathfrak {L} _ {3} (\beta) \end{array}\tag{20}
$$

By looking again at 18 and 20 , it can be seen that the first term can be computed by solvingŽ . Ž . $n _ { \mathrm { g } }$ dynamic programs again; the second term separates into $n _ { \mathrm { t } }$ optimal power flow problems with all generators committed but with special cost curves $\lambda _ { \mathrm { p } } ^ { i , t } s _ { \mathrm { p } } ^ { i , t } + \lambda _ { \mathrm { q } } ^ { i , t } s _ { \mathrm { q } } ^ { i , t }$ for generator i at time t. Notice that $s _ { \mathrm { q } } ^ { i , t }$ also has a price. It is assumed that the solutions of the dynamic programs meet the $\mathcal { D }$ constraints and that the solutions of the optimal power flows meet the $\mathcal { S }$ constraints.

It would be tempting to apply a dual maximization procedure to the dual objective as stated, but there are some issues that prevent us from doing that without some modification of the Lagrangian. The first issue is that the cost of $d _ { \mathrm { q } } ^ { i , t }$ reflected in the dynamic programs, being linear, is not strongly convex; this can cause unwanted oscillations in the $d _ { \mathrm { q } } ^ { i , t }$ prescribed by the dynamic program see Ref. 5 . Therefore, we set out to fix this beforeŽ <sup>w</sup> <sup>x</sup>. addressing any other problems by augmenting the Lagrangian with quadratic functions of the equality constraints. This will introduce nonseparable terms, but using the Auxiliary Problem Principle described by G. Cohen in Refs. 7,8 , we can linearize those terms about the previous iteration values, rendering them separable.<sup>w</sup> <sup>x</sup> Thus, we write the new augmented Lagrangian as

$$
\begin{array}{l} \mathfrak {L} (U, D, S, \lambda , \beta) = \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \Big [ u ^ {i, t} F ^ {i} \big (d _ {\mathrm{p}} ^ {i, t} \big) + K ^ {i, t} (u ^ {i, \cdot}) \Big ] + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {l = 1} ^ {n _ {\mathrm{z}}} \beta^ {l, t} \bigg (R ^ {l, t} - \sum_ {i \in Z _ {l}} u ^ {i, t} P _ {\max} ^ {i} \bigg) \\ \qquad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \lambda_ {\mathrm{p}} ^ {i, t} \big (s _ {\mathrm{p}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} \big) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \lambda_ {\mathrm{q}} ^ {i, t} \big (s _ {\mathrm{q}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} \big) \\ \qquad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \frac {c _ {\mathrm{p}}}{2} \big (s _ {\mathrm{p}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} \big) ^ {2} + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \frac {c _ {\mathrm{q}}}{2} \big (s _ {\mathrm{q}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} \big) ^ {2}. \end{array}\tag{21}
$$

The Auxiliary Problem Principle allows us to substitute the augmentation terms by the following at iteration k Žsee Ref. 5<sup>w</sup> <sup>x</sup>.

$$
\begin{array}{l} \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} c _ {\mathrm{p}} \left(\bar {s} _ {\mathrm{p}} ^ {i, t} - \bar {u} _ {\mathrm{p}} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t}\right) \left(s _ {\mathrm{p}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{p}} ^ {i, t}\right) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \frac {b _ {\mathrm{p}}}{2} \left\{\left(s _ {\mathrm{p}} ^ {i, t} - \bar {s} _ {\mathrm{p}} ^ {i, t}\right) ^ {2} + \left(u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t}\right) ^ {2} \right\} \\ + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} c _ {\mathrm{q}} \left(\bar {s} _ {\mathrm{q}} ^ {i, t} - \bar {u} _ {\mathrm{q}} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t}\right) \left(s _ {\mathrm{q}} ^ {i, t} - u ^ {i, t} d _ {\mathrm{q}} ^ {i, t}\right) + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \frac {b _ {\mathrm{q}}}{2} \left\{\left(s _ {\mathrm{q}} ^ {i, t} - \bar {s} _ {\mathrm{q}} ^ {i, t}\right) ^ {2} + \left(u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t}\right) ^ {2} \right\} \end{array}\tag{22}
$$

where $\overline { { u } } ^ { i , t } , \overline { { d } } _ { \mathrm { p } } ^ { i , t } , \overline { { d } } _ { \mathrm { q } } ^ { i , t } , \overline { { s } } _ { \mathrm { p } } ^ { i , t }$ and $\overline { { S } } _ { \mathbf { q } } ^ { i , t }$ are the values obtained at the $( k - 1 ) \mathrm { t h }$ Ž .  iteration. Since 22 is separable, we can collect terms of the augmented Lagrangian on a per-generator basis, so that at the kth iteration we are faced with

$$
\begin{array}{l} \mathfrak {L} (U, D, S, \lambda , \beta , \bar {U}, \bar {D}, \bar {S}) = \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \left\{u ^ {i, t} F ^ {i} \left(d _ {\mathrm{p}} ^ {i, t}\right) + K ^ {i, t} \left(u ^ {i;}\right) + \frac {b _ {\mathrm{p}}}{2} u ^ {i, t} \left(d _ {\mathrm{p}} ^ {i, t}\right) ^ {2} + \frac {b _ {\mathrm{q}}}{2} u ^ {i, t} \left(d _ {\mathrm{q}} ^ {i, t}\right) ^ {2} \right. \\ \quad + \left[ - \lambda_ {\mathrm{p}} ^ {i, t} - c _ {\mathrm{p}} \left(\bar {s} _ {\mathrm{p}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t}\right) - b _ {\mathrm{p}} \bar {u} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t} \right] u ^ {i, t} d _ {\mathrm{p}} ^ {i, t} + \left[ - \lambda_ {\mathrm{q}} ^ {i, t} - c _ {\mathrm{q}} \left(\bar {s} _ {\mathrm{q}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t}\right) \right. \\ \quad - b _ {\mathrm{q}} \bar {u} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t} ] u ^ {i, t} d _ {\mathrm{q}} ^ {i, t} + [ - \beta^ {z (i), t} P _ {\max} ^ {i} ] u ^ {i, t} \Bigg \} \\ \quad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \left\{\frac {b _ {\mathrm{p}}}{2} \left(s _ {\mathrm{p}} ^ {i, t}\right) ^ {2} + \frac {b _ {\mathrm{q}}}{2} \left(s _ {\mathrm{q}} ^ {i, t}\right) ^ {2} + \left[ \lambda_ {\mathrm{p}} ^ {i, t} + c _ {\mathrm{p}} \left(\bar {s} _ {\mathrm{p}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t}\right) - b _ {\mathrm{p}} \bar {s} _ {\mathrm{p}} ^ {i, t} \right] s _ {\mathrm{p}} ^ {i, t} \right. \\ \quad + \left[ \lambda_ {\mathrm{q}} ^ {i, t} + c _ {\mathrm{q}} \left(\bar {s} _ {\mathrm{q}} ^ {i, t} - \bar {u} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t}\right) - b _ {\mathrm{q}} \bar {s} _ {\mathrm{q}} ^ {i, t} \right] s _ {\mathrm{q}} ^ {i, t} \Bigg \} \\ \quad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {i = 1} ^ {n _ {\mathrm{g}}} \left\{\frac {b _ {\mathrm{p}}}{2} \left[ (\bar {s} _ {\mathrm{p}} ^ {i, t}) ^ {2} + (\bar {u} ^ {i, t} \bar {d} _ {\mathrm{p}} ^ {i, t}) ^ {2} \right] + \frac {b _ {\mathrm{q}}}{2} \left[ (\bar {s} _ {\mathrm{q}} ^ {i, t}) ^ {2} + (\bar {u} ^ {i, t} \bar {d} _ {\mathrm{q}} ^ {i, t}) ^ {2} \right] \right\} \\ \quad + \sum_ {t = 1} ^ {n _ {\mathrm{t}}} \sum_ {l = 1} ^ {n _ {\mathrm{z}}} \beta^ {l, t} R ^ {l, t} \end{array}\tag{23}
$$

$$
\mathfrak {L} (U, D, S, \lambda , \beta , \bar {U}, \bar {D}, \bar {S}) = \mathfrak {L} _ {1} (U, D, \lambda , \beta , \bar {U}, \bar {D}, \bar {S}) + \mathfrak {L} _ {2} (S, \lambda , \bar {U}, \bar {D}, \bar {S}) + \mathfrak {L} _ {3} (\beta).\tag{24}
$$

Notice that 24 has the same separation structure as 19 . Ž . Ž .

Now that the separability issue has been resolved, we propose the following.

Algorithm 2: AC Augmented Lagrangian relaxation.

Step 0. $k \gets 0$

Step 1. Initialize $( \lambda _ { \mathfrak { p } } ^ { i , t } , \lambda _ { \mathfrak { q } } ^ { i , t } )$ to the values of the multipliers on the power flow equality constraints at generator buses when running an OPF with all units committed. Initialize $( \overline { { U } } , \overline { { D } } , \overline { { S } } )$ to zeros.

Step 2a. Compute

$$
(\hat {U}, \hat {D}) \leftarrow \arg \min _ {\text { feasible   } U, D} \mathfrak {L} _ {1} (U, D, \lambda , \beta , \overline {{U}}, \overline {{D}}, \overline {{S}})
$$

by solving $n _ { \mathrm { g } }$ one-generator dynamic programs.

Step 2b. Compute

$$
\hat {S} \leftarrow \arg \min _ {\text { feasible   } S} \mathfrak {L} _ {2} (S, \lambda , \overline {{U}}, \overline {{D}}, \overline {{S}})
$$

by solving $n _ { \mathrm { t } } ~ { \mathrm { O P F s } }$ in which all generators are committed, their generation range has been expanded to include $P _ { \operatorname* { m i n } } ^ { i } = 0$ and the special cost $\mathfrak { L } _ { 2 } ( S , \lambda , \overline { { U } } , \overline { { D } } , \overline { { S } } )$ is used. Note: all tasks in Steps 2a and 2b can be solved in parallel.

Step 3. If the commitment schedule $\hat { U }$ is not in a database of tested commitments, perform a cheap primal feasibility test. If the results are not encouraging, store the schedule in the database and label it ‘infeasible’, then go to Step 6.

Step 4. Perform a more serious primal feasibility test by actually attempting to run $n _ { \mathrm { t } }$ OPFs with the original $P _ { \mathrm { m i n } }$ constraints. If all OPFs are successful, store the commitment in the database, together with the primal cost including startup costs, and the duality gap the dual cost was available upon sol- Ž ving Steps 2a and 2b . Else label the commitment as ‘infeasible’, store it in the database, and go to . Step 6.

Step 5. If the duality gap is small enough, stop.

Step 6. Update all multipliers using subgradient techniques, and

$$
\overline {{U}} \leftarrow \hat {U}
$$

$$
\overline {{D}} \leftarrow \hat {D}
$$

$$
\bar {S} \leftarrow \hat {S}
$$

$$
k \leftarrow k + 1
$$

Step 7. Go to Step 2.

The proposed algorithm is very OPF-intensive: the major computational cost is that of computing $n _ { \mathrm { t } }$ OPFs for every iteration in order to solve the static subproblems, plus extra OPFs in selected iterations when a given commitment is promising. Thus, every effort possible must be made to try to alleviate the burden of OPF computation. The first thing that can be done is to use as a starting point for the OPF the result of the previous iteration for the same time period. Most of the time, the only difference in the data for the OPF would be a small change in the costs reflected by the change inŽ . from one iteration to another . This should result in fewer iterations needed for the OPF.

Another drawback of the algorithm is that a different set of OPF computations must be performed to compute the value of the dual objective and to compute the value of the primal. Thus, before even trying to compute the value of the primal objective, one should make sure that such a costly computation is worth doing. Some of the cheap tests include verifying that the reserve constraint is met and that the mismatch between the S and the D variables is small. With respect to the latter, we have found that if $u ^ { 1 , t } = 1$ , a smaller mismatch should be asked for as requisite to feasibility than if $u ^ { i , t } = 0$ . More costly feasibility tests would involve power flow problems starting from appropriate initial values. Finally, since Alsac et al. 3 claim that LP-based OPF methods can be faster in detecting infeasibility, it might be advantageous to use such methods.

## 3. Preliminary computational results

We have written a preliminary implementation of the algorithm in the MATL ${ \bf A B } ^ { \mathrm { T M } }$ environment. The dynamic subproblems can accommodate minimal up or down times, warm start and cold startup costs. The static subproblems are solved by an OPF code see Ref. 20 that incorporates box constraints on generators P and Q, Ž <sup>w</sup> <sup>x</sup>. polynomial cost functions for both P and Q, voltage constraints, line MVA limits and of course, the power flow equations. The program has been tested on a modified IEEE 30-bus system 2 with six generators and a<sup>w</sup> <sup>x</sup> planning horizon of length 6. For comparison purposes, a version of the Lagrangian relaxation algorithm with DC flow-based relaxed line limits was also written. It turns out that generator number 4, located at bus number 27, is needed for voltage support for many load levels even though it is most uneconomical to operate. The AC-based algorithm correctly identified this unit as a must-run for those time periods, even providing some price information on the MVArs that this unit produced by means of the corresponding $\lambda _ { \mathrm { q } } ^ { i , t } .$ . The number of iterations required was usually in the vicinity of 100. In contrast, the DC flow-based algorithm failed to commit unit 4 for any period, producing a commitment schedule that was infeasible in light of the AC power flow constraints.

![](/api/attachments/6BG9AXKS/fulltext/images/2907d077cbff7af551e3fbff7a804dbc397f6cda6748186bb615cfd5c44aa4d9.jpg)  
Fig. 1. Evolution of multipliers in a typical run.

The importance of proper selection of the $( c _ { \mathrm { p } } , b _ { \mathrm { p } } , c _ { \mathrm { q } } , b _ { \mathrm { q } } )$ parameters was apparent from the beginning. We obtained good results with $c _ { \mathsf { p } } = 0 . 0 5$ $b _ { \mathrm { p } } = 4 c _ { \mathrm { p } } ^ { \cdot } , \ c _ { \mathrm { q } } ^ { \cdot } = \dot { 0 } . 0 8$ and $b _ { \mathrm { q } } = 4 c _ { \mathrm { q } }$ . However, other choices tended to produce somewhat smooth, damped oscillations in the values of some of the $( \lambda _ { \mathfrak { p } } ^ { i , t } , \lambda _ { \mathfrak { q } } ^ { i , t } )$ .

To highlight one of the new features found in the algorithm, we show the evolution of $( \lambda _ { \mathrm { p } } ^ { i , t } , \lambda _ { \mathrm { q } } ^ { i , t } )$ vs. iteration number for a typical run in Fig. 1. The multipliers with the higher values are all P-type multipliers. Those with the smaller values correspond to the $\lambda _ { \mathrm { q } } ^ { i , t }$ . Most of them settle to zero, indicating that Q is essentially free almost always. However, a few of them actually have high prices: these belong to generators and time periods where the OPF tries to use their MVArs in order to force feasibility or guided by economic considerations, but the generators are not actually committed. In the course of the algorithm, these $\lambda _ { \mathrm { q } } ^ { i , t }$ may grow so large that they trigger the respective unit on. Once this happens, such multipliers tend to approach zero again, since Q is now plentiful. In Fig. 1 there are two clear examples of this behavior, corresponding to unit 4 being committed for certain time periods. As the multiplier approaches zero, the static copy $s _ { \mathbf { q } } ^ { i , t }$ will approach the dynamic $d _ { \mathfrak { q } } ^ { i , t }$

At the time that this paper was written, the implementation served the purpose of testing the overall algorithm’s expected behavior. The results that were obtained encourage us to believe that the formulation is sound. However, clearly more work is needed in order to produce anything close to practical. More kinds of constraints e.g., ramp limits need to be included in the implementation. Preparations for testing larger scaleŽ . systems are under way, and, if successful, a parallel implementation will be worth pursuing

We conclude this paper with the following comment: since computer capacity grows much faster than the size of the electrical power systems in the world, we believe that this algorithm or a variant of it could well be solving real life unit commitment problems in a few years.

## Acknowledgements

We wish to thank Ray Zimmerman and Deqiang Gan for their stimulating critique and for modifying MATPOWER 20 , their OPF code, to handle costs in VAr generation. We would also like to thank Csaba<sup>w</sup> <sup>x</sup> Meszaros, whose QP program 12 BPMPD we used.´ ´ <sup>w</sup> <sup>x</sup>

## References

<sup>w</sup> <sup>x</sup> 1 K.H. Abdul-Rahman, S.M. Shahidehpour, M. Aganagic, S. Mokhtari, A practical resource scheduling with OPF constraints, IEEE Transactions on Power Systems 11 1 1996 254–259.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 O. Alsac, B. Stott, Optimal load flow with steady-state security, IEEE Transactions on Power Apparatus and Systems PAS 93 3Ž . Ž . 1974 745–751.

<sup>w</sup> <sup>x</sup> 3 O. Alsac, J. Bright, M. Prais, B. Stott, Further development in LP-based optimal power flow, IEEE Transactions on Power Systems 5 Ž . Ž . 3 1990 697–711.

<sup>w</sup> <sup>x</sup> 4 R. Baldick, The generalized unit commitment problem, IEEE Transactions on Power Systems 10 1 1995 465–475.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 J. Batut, A. Renaud, Daily generation scheduling optimization with transmission constraints: a new class of algorithms, IEEE Transactions on Power Systems 7 3 1992 982–989.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 D.P. Bertsekas, G.S. Lauer, N.R. Sandell, T.A. Posbergh, Optimal short-term scheduling of large-scale power systems, IEEE Transactions on Automatic Control AC 28 1 1983 1–11.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 G. Cohen, Auxiliary problem principle and decomposition of optimization problems, Journal of Optimization Theory and Applications 32 3 1980 277–305.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 G. Cohen, D.L. Zhu, Decomposition coordination methods in large scale optimization problems: the nondifferentiable case and the use of augmented Lagrangians, in: J.B. Cruz Ed. , Advances in Large Scale Systems, Vol. 1, JAI Press 1984 , pp. 203–266.Ž . Ž .

<sup>w</sup> <sup>x</sup>9 X. Guan, P.B. Luh, H. Yan, An optimization-based method for unit commitment, Electrical Power and Energy Systems 14 1 1992 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 G.S. Lauer, D.P. Bertsekas, N.R. Sandell, T.A. Posbergh, Solution of large-scale optimal unit commitment problems, IEEE Transactions on Power Apparatus and Systems PAS 101 1 1982 79–85.Ž . Ž .

<sup>w</sup> <sup>x</sup>11 A. Merlin, P. Sandrin, A new method for unit commitment at Electricite de France, IEEE Transactions on Power Apparatus and´ Systems PAS 102 5 1983 1218–1225.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 Cs. Meszaros, The efficient implementation of interior point methods for linear programming and their applications, PhD Thesis, ´ ´ Eotvos Lorand University of Sciences 1996 .¨ ¨ ´ Ž .

<sup>w</sup> <sup>x</sup> 13 J.A. Muckstadt, R.C. Wilson, An application of mixed-integer programming duality to scheduling thermal generating systems, IEEE Transactions on Power Apparatus and Systems PAS 87 12 1968 1968–1978.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 J.A. Muckstadt, S.A. Koenig, An application of Lagrange relaxation to scheduling in power-generation systems, Operations Research 25 3 1977 387–403.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 S. Ruzic, N. Rajakovic, A new approach for solving extended unit commitment problem, IEEE Transactions on Power Systems 6 1ˇ ´ ´ Ž . Ž . 1991 269–277.

<sup>w</sup> <sup>x</sup> 16 J.J. Shaw, A direct method for security-constrained unit commitment, IEEE Transactions on Power Systems 10 3 1995 1329–1339.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 A.J. Svoboda, C.L. Tseng, C.A. Li, R.B. Johnson, Short-term resource scheduling with ramp constraints, IEEE Transactions on Power Systems 12 1 1997 77–83. Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 S.J. Wang, S.M. Shahidehpour, D.S. Kirschen, S. Mokhtari, G.D. Irisarri, Short-term generation scheduling with transmission and environmental constraints using an augmented Lagrangian relaxation, IEEE Transactions on Power Systems 10 3 1995 1294–1301. Ž . Ž .

<sup>w</sup> <sup>x</sup> 19 F. Zhuang, F.D. Galiana, Towards a more rigorous and practical unit commitment by Lagrangian relaxation, IEEE Transactions on Power Systems 3 2 1988 763–773.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 R. Zimmerman, D. Gan, MATPOWER: A Matlab Power System Simulation Package http: Ž . <sup>rr</sup>www.pserc.cornell.edu<sup>r</sup>matpower<sup>r</sup> .

Carlos Murillo-Sanchez studied Electronics Engineering at Instituto Tecnologico y de Estudios Superiores de Monterrey. He then studied at´ ´ the University of Wisconsin-Madison, where he obtained a masters degree in Electrical Engineering and Control Systems. He worked in several universities in Mexico and Colombia before enrolling at Cornell, where he currently pursues a PhD degree in Electrical Engineering. ´

Robert J. Thomas currently holds the position of Professor of Electrical Engineering at Cornell University. He has held sabbatical positions with the US Department of Energy Office of Electric Energy Systems EES in Washington, DC and at the National Science Foundation asŽ . the first Program Director for the Power Systems Program in the Engineering Directorate’s Division of Electrical Systems Engineering Ž .ESE . He has been a consultant to several entities on various electric utility system related issues. He is the author of over 90 technical papers. He has been a member of the IEEE United States Activity Board’s Energy Policy Committee since 1991 and is currently the committee’s chair. He is a member of the IEEE Technology Policy Council and has been a member of several university, government and industry advisory boards or panels. His current technical research interests are broadly in the areas of analysis and control of nonlinear continuous and discrete time systems with applications to large-scale electric power systems. He is a member of Tau Beta Pi, Eta Kappa Nu, Sigma Xi, ASEE and a Fellow of the IEEE. He was an EPRI ERA Professor in 1988–1989. He is currently the Director of the National Science Foundation Industry<sup>r</sup>University Cooperative Research Center, PSERC, a Center focused on problems of restructuring of the electric power industry. PSERC is comprised of the universities of Cornell, Berkeley, Howard, Illinois and Wisconsin.
