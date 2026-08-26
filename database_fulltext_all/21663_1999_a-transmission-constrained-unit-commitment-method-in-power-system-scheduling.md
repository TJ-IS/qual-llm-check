---
otero_id: 21663
otero_key: "VM4RREM3"
title: "A transmission-constrained unit commitment method in power system scheduling"
authors: "Chung-Li Tseng; Shmuel S. Oren; Carol S. Cheng; Chao-an Li; Alva J. Svoboda; Raymond B. Johnson"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(98)00072-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A transmission-constrained unit commitment method in power system scheduling

Chung-Li Tseng <sup>a,)</sup>, Shmuel S. Oren <sup>a</sup>, Carol S. Cheng <sup>b</sup>, Chao-an Li <sup>b</sup>, Alva J. Svoboda <sup>b</sup>, Raymond B. Johnson b

<sup>a</sup> Department of Industrial Engineering Operations Research, UniÕersity of California, Berkeley, CA 94720, USA <sup>b</sup> Pacific Gas Electric Company, San Francisco, CA 94177, USA

## Abstract

This paper presents a transmission-constrained unit commitment method using a Lagrangian relaxation approach. Based on a DC power flow model, the transmission constraints are formulated as linear constraints. The transmission constraints, as well as the demand and spinning reserve constraints, are relaxed by attaching Lagrange multipliers. A three-phase algorithmic scheme is devised including dual optimization, a feasibility phase and unit decommitment. A large-scale test problem with more than 2200 buses and 2500 transmission lines is tested along with other test problems. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Power system scheduling; Unit commitment; Transmission-constrained unit commitment; Unit decommitment

## 1. Introduction

The unit commitment is an optimization problem that economically schedules generating units over a short-term planning horizon subject to the satisfaction of demand and other system operating constraints. The unit commitment problem is considered to be in the class of NP-hard problems 14 . Many optimization methods <sup>w</sup> <sup>x</sup> have been proposed to solve the unit commitment problem, e.g., see Ref. 4 for a survey. These methods include priority list methods 3 dynamic programming methods 10,11,18 sequential method 8 and La- <sup>w x</sup> <sup>w</sup> <sup>x</sup> <sup>w x</sup> grangian relaxation methods 2,4–6 , etc. Lagrangian relaxation methods are now among the most widely used<sup>w</sup> <sup>x</sup> approaches to solving unit commitment.

Because generating units of a utility company are normally located in different areas interconnected via transmission lines, power flows are subject to thermal limit of transmission lines. However, the transmission constraints were usually left out in the unit commitment problems. If the transmission constraints are not considered, the schedule obtained might cause some transmission lines to be overloaded. This may result in rescheduling of some generating units and may incur significant costs. This paper presents a method for solving the unit commitment problem which takes transmission constraints into account. A first attempt to incorporate AC load flow constraints in unit commitment optimization was detailed in Ref. 9 with promising although<sup>w</sup> <sup>x</sup> limited computational testing. At present, the computational requirements of that approach would be prohibitive for practical size problems but that might change with the rapid development in computation technology.

In this paper, the transmission constraints will be formulated as linear constraints based on a DC power flow model. Pang et al. have considered the transmission constrained unit commitment problem in Ref. 11 using a<sup>w</sup> <sup>x</sup> dynamic programming method. In Ref. 12 , Shaw has proposed a practical method for solving the security-constrained unit commitment problem using the Lagrangian relaxation approach. This approach relaxes not only the demand constraints and the spinning reserve constraints, but also the transmission constraints using multipliers. Shaw describes two methods in his paper 12 , a direct method and an indirect method. The former takes full account of the transmission constraints in the optimization phase, while the latter does so only in locating a feasible solution. The conclusion of Ref. 12 favors the direct method.

In this paper, we employ a three-phase algorithmic scheme 14–16 to solve the unit commitment problem. <sup>w</sup> <sup>x</sup> The three phases include dual optimization, a feasibility phase and unit decommitment. Algorithmically, the dual optimization phases of most Lagrangian relaxation-based approaches are alike. These approaches differentiate in obtaining a feasible solution. In this paper we will present a robust feasibility method using linear programming. The obtained feasible schedule will then be improved by a unit decommitment method. It has been shown in Ref. 15 that unit decommitment not only improves solution quality generally, but also mitigates <sup>w</sup> <sup>x</sup> unpredictable effects due to heuristics in the first two phases. In this paper, we apply our method to a practical test problem, which involves more than 2200 buses and 2500 transmission lines, and other small-scale test problems as well.

This paper is organized as follows: Section 2 gives the formulation of the unit commitment problem. A three-phase Lagrangian relaxation algorithm is presented in Section 3. Section 4 gives some numerical results. We conclude the paper in Section 5.

## 2. Problem formulation

<table><tr><td colspan="2">We first define the following nomenclature.</td></tr><tr><td>t:</td><td>Index for time (t=0,···,T)</td></tr><tr><td>b:</td><td>Index for the number of buses (b=1,···,B)</td></tr><tr><td> $\Lambda_b$ :</td><td>Index set of units at bus b</td></tr><tr><td>i:</td><td>Index for the number of units (i∈ $\Lambda_b$ , b=1,···,B)</td></tr><tr><td> $\ell$ :</td><td>Index for transmission lines (l=1,···,L)</td></tr><tr><td> $\Gamma_{\ell b}$ :</td><td>Line flow distribution factor for transmission line l due to the net injection at bus b</td></tr><tr><td> $F_\ell$ :</td><td>The transmission capacity on the transmission line l</td></tr><tr><td> $u_{it}$ :</td><td>Zero-one decision variable indicating whether unit i is up or down in time period t.</td></tr><tr><td> $x_{it}$ :</td><td>State variable indicating the length of time that unit i has been up or down in time period t</td></tr><tr><td> $t_i^{\text{on}}$ :</td><td>The minimum number of periods unit i must remain on after it has been turned on</td></tr><tr><td> $t_i^{\text{off}}$ :</td><td>The minimum number of periods unit i must remain off after it has been turned off</td></tr><tr><td> $p_{it}$ :</td><td>Variable indicating the amount of power unit i is generating in time period t</td></tr><tr><td> $p_i^{\text{min}}$ :</td><td>Minimum rated capacity of unit i</td></tr><tr><td> $p_i^{\text{max}}$ :</td><td>Maximum rated capacity of unit i</td></tr></table>

$$
C _ {i} (p _ {i t}):
$$

$$
S _ {i} (x _ {i, t - 1}, u _ {i t}, u _ {i, t - 1}):
$$

Fuel cost for operating unit i at output level $p _ { i t }$ in time period t Start-up cost associated with turning on unit i at the beginning of time period t Forecast demand requirement at bus b in time period t Spinning capacity requirement at bus b in time period t

$$
R _ {b t} \colon
$$

The transmission-constrained unit commitment problem is formulated as the following mixed-integer programming problem: note that the underlined variables are vectors in this paper, e.g. the components of Ž u are all legitimate $u _ { i t } )$

Minimize the total generating cost:

$$
\min _ {\underline {{u}}, \underline {{x}}, \underline {{p}}} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i \in \Lambda_ {b}} \left[ C _ {i} (p _ {i t}) u _ {i t} + S _ {i} (x _ {i, t - 1}, u _ {i t}, u _ {i, t - 1}) \right]\tag{1}
$$

subject to the following constraints:

Demand constraints

$$
\sum_ {b = 1} ^ {B} \sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} = D _ {t} \equiv \sum_ {b = 1} ^ {B} D _ {b t}, \forall t,\tag{2}
$$

Spinning capacity constraints

$$
\sum_ {b = 1} ^ {B} \sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max} u _ {i t} \geq R _ {t} \equiv \sum_ {b = 1} ^ {B} R _ {b t}, \forall t,\tag{3}
$$

Transmission constraints

$$
- F _ {\ell} \leq \sum_ {b = 1} ^ {B} \Gamma_ {\ell b} \left(\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} - D _ {b t}\right) \leq F _ {\ell}, \forall \ell , t,\tag{4}
$$

Local reserve constraints

$$
\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} \geq r _ {b t} D _ {b t}, r _ {b t} \in [ 0, 1 ], \forall b,\tag{5}
$$

$$
\sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max} u _ {i t} \geq s _ {b t} R _ {b t}, s _ {b t} \in [ 0, 1 ], \forall b,\tag{6}
$$

where $\boldsymbol { s } _ { b t }$ and $\boldsymbol { r } _ { b t }$ are scalars used to define the local minimum generation level and local spinning capacity level within bus b. Although constraints 5 and 6 are normally considered within an area instead of a bus, weŽ . Ž . int to present a method suitable for a generalized multi-area model.

Local unit constraints Unit capacity constraints, for all $\mathrm { i } \in \varLambda _ { b . }$ ;b and $t = 1 , \ldots , T ;$

$$
p _ {i} ^ {\mathrm{min}} \leq p _ {i t} \leq p _ {i} ^ {\mathrm{max}},\tag{7}
$$

the state transition equations

$$
x _ {i t} = \left\{ \begin{array}{l l} \max (x _ {i, t - 1}, 0) + 1, & \text { if   } u _ {i t} = 1, \\ \min (x _ {i, t - 1}, 0) - 1, & \text { if   } u _ {i t} = 0, \end{array} \right.\tag{8}
$$

the minimum uptime and downtime constraints,

$$
u _ {i t} = \left\{ \begin{array}{l l} 1, & \text { if } 1 \leq x _ {i, t - 1} <   t _ {i} ^ {\text { on }}, \\ 0, & \text { if } - 1 \geq x _ {i, t - 1} > - t _ {i} ^ {\text { off }}, \\ 0 \text { or } 1, & \text { otherwise }, \end{array} \right.\tag{9}
$$

and the initial conditions on $x _ { i t }$ at $t = 0$ for $\forall i .$

For simplicity, we do not consider ramp constraints in this paper. Regarding incorporating different kinds of ramp constraints in the unit commitment, the interested reader is directed to Refs. 13,14 . If considered, the<sup>w</sup> <sup>x</sup> ramp constraints should be treated as are other local unit constraints such as Eq. 7 within the correspondingŽ . bus subproblem to be detailed later.

## 3. Three-phase Lagrangian relaxation algorithm

The Lagrangian relaxation LR approach relaxes the demand constraints, the spinning reserve constraintsŽ . and the transmission constraints using Lagrange multipliers. Algorithmically, the dual optimization of most Lagrangian relaxation based approaches are alike. The dual approach presented in this closely corresponds to the it direct method in Ref. 12 .<sup>w</sup> <sup>x</sup>

## 3.1. Phase 1: the dual optimization

Letting $\lambda _ { t } , ~ \mu _ { t }$ be the corresponding nonnegative Lagrange multiplier of Eqs. 2 and 3 , respectively. AndŽ . Ž . $\alpha _ { t l } , \beta _ { t l }$ are corresponding to Eq. 4 , Ž . $\nu _ { b t }$ and $\rho _ { b t }$ Ž . Ž . to Eqs. 5 and 6 , respectively. We now have the following dual problem:

$$
(D) \max _ {(\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}}) \geq 0} d (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}})\tag{10}
$$

where

$$
\begin{array}{l} d (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}}) \\ \equiv \min _ {u _ {i t}, x _ {i t}, p _ {i t}} \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \sum_ {i \in \Lambda_ {b}} \left[ C _ {i} (p _ {i t}) u _ {i t} + S _ {i} (x _ {i, t - 1}, u _ {i t}, u _ {i, t - 1}) \right] \\ - \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \left[ \lambda_ {t} \left(\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} - D _ {b t}\right) + \mu_ {t} \left(\sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max} u _ {i t} - R _ {b t}\right) \right] \\ - \sum_ {t = 1} ^ {T} \sum_ {\ell = 1} ^ {L} \left[ \alpha_ {t \ell} \left(F _ {\ell} + \sum_ {b = 1} ^ {B} \Gamma_ {\ell b} \left(\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} - D _ {b t}\right)\right) + \beta_ {t \ell} \left(F _ {\ell} - \sum_ {b = 1} ^ {B} \Gamma_ {\ell b} \left(\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} - D _ {b t}\right)\right) \right] \\ - \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \left[ \nu_ {b t} \left(\sum_ {i \in \Lambda_ {b}} p _ {i t} u _ {i t} - r _ {b t} D _ {b t}\right) + \rho_ {b t} \left(\sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max} u _ {i t} - s _ {b t} R _ {b t}\right) \right] \end{array}\tag{11}
$$

subject to initial conditions, and the unit constraints. After rearrangement of the terms in Eq. 11 , the Ž . separability of $d ( \underline { { \lambda } } , \underline { { \mu } } , \underline { { \alpha } } , \underline { { \beta } } , \underline { { \nu } } , \underline { { \rho } } )$ appears.

$$
d \bigl (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \bigr) = \sum_ {b = 1} ^ {B} \sum_ {i \in \Lambda_ {b}} d _ {i} \bigl (b; \underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \bigr) + \sigma \bigl (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \bigr),\tag{12}
$$

where

$$
\begin{array}{l} \sigma (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}}) = \sum_ {t = 1} ^ {T} \left(\lambda_ {t} D _ {t} + \mu_ {t} R _ {t}\right) - \sum_ {t = 1} ^ {T} \sum_ {\ell = 1} ^ {L} \left[ \alpha_ {t \ell} \left(F _ {\ell} - \sum_ {b = 1} ^ {B} \Gamma_ {b \ell} D _ {b t}\right) + \beta_ {t \ell} \left(F _ {\ell} + \sum_ {b = 1} ^ {B} \Gamma_ {b \ell} D _ {b t}\right) \right] \\ + \sum_ {t = 1} ^ {T} \sum_ {b = 1} ^ {B} \left(\nu_ {b t} r _ {b t} D _ {b t} + \rho_ {b t} s _ {b t} R _ {b t}\right) \end{array} \tag {1}\tag{13}
$$

is a constant term given the multipliers, and

$$
\begin{array}{c} d _ {i} \big (b; \underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \big) = \min _ {u _ {i t}, x _ {i t}, p _ {i t}} \sum_ {t = 1} ^ {T} \Bigg [ c _ {i} \big (p _ {i t} \big) + S _ {i} \big (x _ {i, t - 1}, u _ {i t}, u _ {i, t - 1} \big) - \lambda_ {t} p _ {i t} - \mu_ {t} p _ {i} ^ {\max} \\ - \sum_ {\ell = 1} ^ {L} \big (\alpha_ {t \ell} - \beta_ {t \ell} \big) \Gamma_ {\ell b} p _ {i t} - \nu_ {b t} p _ {i t} - \rho_ {b t} p _ {i} ^ {\max} \Bigg ] u _ {i t}. \end{array}\tag{14}
$$

Once again, the minimization in Eq. 14 is subject to initial conditions and the unit constraints.Ž .

Note that $d _ { i }$ is a unit subproblem corresponding to unit i. We can further define a bus subproblem $d _ { b }$ such that

$$
d _ {b} \bigl (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \bigr) \equiv \sum_ {i \in \Lambda_ {b}} d _ {i} \bigl (b; \underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}} \bigr)\tag{15}
$$

and the dual objective 12 is equivalent to Ž .

$$
d (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}}) = \sum_ {b = 1} ^ {B} d _ {b} (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}}) + \sigma (\underline {{\lambda}}, \underline {{\mu}}, \underline {{\alpha}}, \underline {{\beta}}, \underline {{\nu}}, \underline {{\rho}})\tag{16}
$$

Each unit subproblem $d _ { i } \left( \operatorname { E q } . \left( 1 4 \right) \right)$ can be solved using dynamic programming. The dual function $d ( \lambda ,$ , , , $\underline { { \beta } } , \ \underline { { \nu } } , \ \underline { { \rho } } )$ Ž is concave, but not necessarily differentiable at all points e.g. Ref. 1 . A subgradient method is<sup>w</sup> <sup>x</sup>. employed to solve the dual maximization problem Ž . D .

A subgradient of the dual function d is an ascent direction of d. Let g be a point in the dual space, i.e. a vector of all multipliers, an iterative relation can be implemented to maximize the dual function $d \colon$

$$
g ^ {k + 1} \leftarrow g ^ {k} + s ^ {k} \Delta g ^ {k},\tag{17}
$$

where the superscript denotes iteration $k , s$ is the step size and $\varDelta g$ is a subgradient. The subgradient $\varDelta g ^ { k }$ used here is a vector of the mismatches of the relaxed constraints evaluated at $\mathit { \Pi } _ { \boldsymbol { g } ^ { k } } ^ { - }$ Ž<sup>w</sup> <sup>x</sup> 1 . The step size used in our. implementation has the following form,

$$
s ^ {k} = m _ {k} / \left\| g ^ {k} \right\|, m _ {k} > 0,\tag{18}
$$

where $m _ { k }$ is an adaptive constant. Our stopping criteria used in the algorithm combine the maximum number of iteration, the change of norm of subgradients at two consecutive iterations and the number of iterations without improvement in the dual objective value. For details of the dual optimization algorithm, the reader is referred to Ref. 16 . <sup>w</sup> <sup>x</sup>

## 3.2. Phase 2: the feasibility phase

Due to separability, the dual problem presented in the previous can be efficiently solved. Unfortunately, solving the dual problem is not necessarily equivalent to solving the primal original problem. This can be seen in a fact that the solution obtained through the dual optimization of the unit commitment is generally not feasible. A feasibility phase is therefore required to obtain a feasible solution.

Definition 1 With respect to a given spinning capacity requirement $\{ R _ { t } \}$ , a reserÕe-feasible commitment is a unit commitment $\left\{ u _ { i t } \right\}$ that satisfies the spinning reserve capacity constraints 2 , 6 , unit constraints 8 , 9 andŽ . Ž . Ž . Ž . the initial conditions $x _ { i 0 }$

Definition 2 With respect to a given load requirement $\{ D _ { t } \}$ , a unit commitment $\left\{ u _ { i t } \right\}$ is said to be dispatchable if there exists a set of dispatches $\{ p _ { i t } \}$ such that Eqs. 2 , 4 , 5 and 7 can be satisfied.Ž . Ž . Ž . Ž . B

In Ref. 19 , a method for obtaining feasible solutions to the single-area unit commitment problem is<sup>w</sup> <sup>x</sup> proposed. The basic idea is to obtain a reserve-feasible commitment in the single-area case, ignore Eq. 6 in theŽ . definition. In Ref. 19 a reserve-feasible commitment is found by projecting the subgradient onto the hour<sup>w</sup> <sup>x</sup> corresponding to the most unsatisfied capacity constraint and increasing only the multiplier $\mu _ { t }$ of this hour. This approach can be modified to simultaneously updating the multipliers $\mu _ { t } ^ { \mathbf { \Upsilon } , } \mathbf { s }$ of it all hours that the spinning capacity requirement is violated. Such a modification can speed up the feasibility phase at the cost of overcommitment 5,14 . Under the three-phase scheme, this overcommitment effect can nevertheless be corrected in the final unit decommitment phase to be addressed in a later section.

The feasibility phase presented in this paper contains two parts. Part 1 seeks a reserve-feasible commitment by increasing the multipliers $\mu _ { t }$ of all hours with insufficient spinning capacities. Starting from this reservefeasible commitment obtained, Part 2 solves a linear program LP for each hour to verify if this commitment isŽ . also dispatchable at this hour. If not, information can be extracted from the solution of the LP to determine how much additional spinning capacity at this hour is required so that a dispatchable commitment exists. The spinning reserve requirement of this hour is thus $u p l i f t$ . Part 1 is then rerun with respect to the new uplift Ž . spinning reserve requirements. Suppose Part 1 of the feasibility phase terminates at iteration k with an obtained commitment $\{ u _ { i t } ^ { k } \}$ . Let $q _ { \mathrm { b t } }$ be the variable representing the total generation to be dispatched to bus b in time t. Given a commitment $\{ u _ { i t } ^ { k } \}$ let $\begin{array} { r } { q _ { b t } ^ { \operatorname* { m i n } } = \sum _ { i \in \mathcal { A } _ { b } } p _ { i } ^ { \operatorname* { m i n } } u _ { i t } ^ { k } } \end{array}$ and $\begin{array} { r } { q _ { b t } ^ { \operatorname* { m a x } } = \sum _ { i \in \mathcal { N } _ { b } } p _ { i } ^ { \operatorname* { m a x } } u _ { i t } ^ { k } } \end{array}$ , which form an immediate lower bound and upper bound for $q _ { b t } .$

Ž Ž .. LP t

$$
\min _ {q _ {b t}, y _ {b t}} \sum_ {b = 1} ^ {B} \left(y _ {b t} - q _ {b t} ^ {\max}\right)\tag{19}
$$

$$
\mathrm{s.t.} q _ {b t} ^ {\min} \leq q _ {b t} \leq y _ {b t}, \forall b\tag{20a}
$$

$$
q _ {b t} ^ {\max} \leq y _ {b t} \leq \sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max}, \forall b\tag{20b}
$$

$$
\sum_ {b = 1} ^ {B} q _ {b t} = D _ {t}\tag{20c}
$$

$$
- F _ {\ell} \leq \sum_ {b = 1} ^ {B} \Gamma_ {\ell b} \left(q _ {b t} - D _ {b t}\right) \leq F _ {\ell}, \forall \ell\tag{20d}
$$

$$
q _ {b t} \geq r _ {b t} D _ {b t}, \forall b\tag{20e}
$$

In $( \mathrm { L P } ( t ) ) , \ y _ { b t }$ is a variable upper bound of both $q _ { b t }$ and $q _ { b t } ^ { \operatorname* { m a x } }$ . Let $y _ { b t } *$ Ž Ž .. be the solution of LP t . If $\{ u _ { i t } ^ { k } \}$ is dispatchable in time $t , y _ { b t } * = q _ { b t } ^ { \operatorname* { m a x } }$ solves $\mathrm { ( L P } ( t ) )$ Ž Ž .. and the optimal objective value of LP t is zero. If $\{ u _ { i t } ^ { k } \}$ is not dispatchable in time $t , \left( \mathrm { L P } ( t ) \right)$ yields a positive objective value, which indicates that to be dispatchable, more units should be committed in time t, and the target value of the new bus capacity requirement is now increased to $y _ { b t } *$ for each bus b in time t. That is, an additional bus spinning capacity requirement is imposed to each bus subproblem $d _ { b } \left( \cdot \right) \mathrm { : }$

$$
\sum_ {i \in \Lambda_ {b}} p _ {i} ^ {\max} u _ {i t} \geq y _ {b t} *.\tag{21}
$$

Part 1 of the feasibility phase is therefore rerun with respect to the updated capacity requirement 21 . The phase Ž . 2 algorithm is summarized below.

## 3.2.1. Phase 2 algorithm

Step 0: $k  0 ; \underline { { \mu } } ^ { 0 }$ and $\underline { { \rho } } ^ { 0 }$ and other multipliers are from Phase 1.

Step 1: Given $\underline { { \mu } } ^ { \mathrm { k } }$ and $\underline { { \rho } } ^ { \mathrm { k } }$ Ž .and other multipliers, solve the dual subproblems 14 to obtain $( \underline { { u } } ^ { k } , \underline { { p } } ^ { k } )$

Step 2: If 3 and 6 are satisfied, go to Step 5 if Step 5 has not been visited, otherwise stop.Ž . Ž .

$$
\begin{array}{l} \text {Step 3: For \forall b,t, \mu_{t} ^{k + 1} \leftarrow \mu_{t} ^{k} + s^{k} \cdot \min(0,R_{t} - \sum_{b = 1}^{B}\sum_ {i\in \Lambda_{b}} p_{i}^{\max} u_{it} ^{k}); \rho_{bt} ^{k + 1} \leftarrow \rho_{bt} ^{k} + s^{k} \cdot \min(0,s_{bt} R_{bt} - \\ \sum_ {i \in \Lambda_ {b}} p_{i}^{\max} u_{it} ^{k}).} \end{array}
$$

Step 4: $k \gets k + 1$ , go to Step 1.

Step 5: Solve $\textstyle ( \operatorname { L P } ( t ) )$ for all t. If the optimal value of $\textstyle ( \operatorname { L P } ( t ) )$ is 0 for all t, stop and $u ^ { k }$ is reserve-feasible and dispatchable. Otherwise, commit more units in any bus b and time t such that $\mathbf { y } _ { b t } ^ { - } * > q _ { b t } ^ { \operatorname* { m a x } }$ to satisfy Eq. Ž .21 , where $y _ { b t } *$ solves $\textstyle ( \operatorname { L P } ( t ) )$ . .

In the algorithm, the loop between Step 1 and Step 4 corresponds to the Part 1 of the feasibility phase, and Step 5 corresponds to Part 2.

The feasibility phase is nevertheless heuristic. An important issue is how robust the feasibility phase of a transmission-constrained unit commitment method is. To test the robustness of the feasibility phase, one can apply it to an instance in which each single bus has enough capacity to handle its own load over the planning horizon. Then the transmission line capacities are gradually reduced to zero. In such a problem, a feasible solution obviously exists, and it is equivalent to solving many single-area unit commitment problems. It can be easily verified that our feasibility phase reduces to solving many single-area problems in such an instance.

## 3.3. Economic dispatch

With the DC power flow model, the transmission constraints are formulated as linear constraints. If the fuel cost is represented by a quadratic function of the power generation, the transmission-constrained economic dispatch is a quadratic programming problem. Many methods can be used to solve this type of problem, e.g., the reduced gradient method. In our implementation, the transmission-constrained economic dispatch is solved by the commercial software MINOS, which does general nonlinear programming.

## 3.4. Phase 3: unit decommitment

A single area unit decommitment UD method was developed as a postprocessing method for the LRŽ . Ž . Ž . approach for solving the unit commitment problem in Ref. 15 . Given the demand requirement<sup>w</sup> <sup>x</sup> $D _ { t }$ , reserve requirement $R _ { t }$ and a feasible solution $( \underline { { \tilde { u } } } , \tilde { \underline { { p } } } )$ Žsatisfying $D _ { t } , \ R _ { i }$ . and all physical constraints , the unit decommitment method improves $( \underline { { \tilde { u } } } , ~ \underline { { \tilde { p } } } )$ while maintaining feasibility. Thus, the unit decommitment can be regarded as a primal approach. A transmission-constrained unit decommitment algorithm can be devised by repeatedly solving the single area unit decommitment to each bus. Suppose at iterationŽ . $k ,$ we have a feasible schedule $( \tilde { u } ^ { k } , \ \tilde { p } ^ { k } )$ . The schedule of bus b can be improved by the unit decommitment with respect to the it current load assigned to be the bus demand at this iteration, i.e., $\begin{array} { r } { \sum _ { i \in { \Lambda _ { b } } } \tilde { p } _ { i t } ^ { k } \tilde { u } _ { i t } ^ { k } } \end{array}$ . The unit decommitment method can obtain a more efficient schedule, if possible, which generates the same load $\begin{array} { r } { \sum _ { i \in { \cal { A } } _ { b } } \widetilde { p } _ { i t } ^ { k } \widetilde { u } _ { i t } ^ { k } } \end{array}$ . After the commitments of all buses are refined, a transmission-constrained economic dispatch is performed to redispatch the units in all buses. The decommitment procedure can thus proceed until no improvement in the total cost is made. Since at each iteration the decommitment procedure improves the commitment without affecting the aggregated bus generation, the transmission feasibility is retained at each iteration. The algorithm is as follows.

## 3.4.1. Transmission-constrained UD algorithm

Step 0: A feasible schedule $( \underline { { \tilde { u } } } ^ { 0 } , \underline { { \tilde { p } } } ^ { k } )$ is given, $k  0$

Step 1: Given $( \underline { { \tilde { u } } } ^ { k } , \ \underline { { \tilde { p } } } ^ { k } )$ each bus performs the unit decommitment presented in Ref. 15 independently with<sup>w</sup> <sup>x</sup> the current load assigned to be the demand requirement $\begin{array} { r } { \sum _ { i \in { \cal { A } } _ { b } } \tilde { p } _ { i t } ^ { k } \tilde { u } _ { i t } ^ { k } } \end{array}$ also subject to the satisfaction of Eq. Ž . 6 . The resultant commitment is denoted by $\hat { u } ^ { \hat { k } }$

Step 2: Apply the transmission-constrained economic dispatch with respect to $\underline { { \hat { u } } } ^ { k }$ to obtain a dispatch $\underline { { \hat { p } } } ^ { k } .$ . Let $( \tilde { u } ^ { k + 1 } , \tilde { p } ^ { k + 1 } ) \gets ( \tilde { u } ^ { k } , \tilde { p } ^ { k } )$

Step 3: If the total cost of $( \underline { { \tilde { u } } } ^ { k + 1 } , \underline { { \tilde { p } } } ^ { k + 1 } )$ is no better than that of $( \underline { { \tilde { u } } } ^ { k } , \underline { { \tilde { p } } } ^ { k } ) .$ , stop; otherwise $k \gets k + 1$ , and go to Step 1.

The above method works best for the cases with many generators in each bus. For other transmission-constrained unit decommitment approaches, the interested reader is referred to Ref. 14 .<sup>w</sup> <sup>x</sup>

## 4. Numerical results

The transmission-constrained unit commitment algorithm presented in this paper has been implemented in FORTRAN on an HP 700 workstation. This presents numerical results of some test problems.

Table 1

<table><tr><td>b_i</td><td> $Type^a$ </td><td> $p_i^{min}$ </td><td> $p_i^{max}$ </td><td> $x_{i0}$ </td><td> $t_i^{up}$ </td><td> $t_i^{down}$ </td><td> $t_i^{cold}$ </td><td> $a_{i0}$ </td><td> $a_{i1}$ </td><td> $a_{i2}$ </td><td> $S_i$ </td></tr><tr><td>1_1</td><td>C</td><td>4</td><td>20</td><td>1</td><td>1</td><td>1</td><td>2</td><td>63.999</td><td>20.000</td><td> $1.000×10^{-6}$ </td><td>40</td></tr><tr><td>1_2</td><td>C</td><td>4</td><td>20</td><td>2</td><td>1</td><td>1</td><td>2</td><td>63.999</td><td>20.000</td><td> $1.000×10^{-6}$ </td><td>40</td></tr><tr><td>1_3</td><td>S2</td><td>10</td><td>76</td><td>3</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>1_4</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>2_1</td><td>C</td><td>4</td><td>20</td><td>1</td><td>1</td><td>1</td><td>2</td><td>63.999</td><td>20.000</td><td> $1.000×10^{-6}$ </td><td>40</td></tr><tr><td>2_2</td><td>C</td><td>4</td><td>20</td><td>2</td><td>1</td><td>1</td><td>2</td><td>63.999</td><td>20.000</td><td> $1.000×10^{-6}$ </td><td>40</td></tr><tr><td>2_3</td><td>S2</td><td>10</td><td>76</td><td>10</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>2_4</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>7_1</td><td>S1</td><td>15</td><td>100</td><td>10</td><td>10</td><td>10</td><td>20</td><td>199.124</td><td>12.468</td><td> $1.532×10^{-2}$ </td><td>45</td></tr><tr><td>7_2</td><td>S1</td><td>15</td><td>100</td><td>10</td><td>10</td><td>10</td><td>20</td><td>199.124</td><td>12.468</td><td> $1.532×10^{-2}$ </td><td>110</td></tr><tr><td>7_3</td><td>S1</td><td>15</td><td>100</td><td>10</td><td>10</td><td>10</td><td>20</td><td>199.124</td><td>12.468</td><td> $1.532×10^{-2}$ </td><td>110</td></tr><tr><td>13_1</td><td>S1</td><td>20</td><td>197</td><td>12</td><td>12</td><td>12</td><td>24</td><td>209.546</td><td>13.928</td><td> $2.085×10^{-3}$ </td><td>100</td></tr><tr><td>13_2</td><td>S1</td><td>20</td><td>197</td><td>12</td><td>12</td><td>12</td><td>24</td><td>209.546</td><td>13.928</td><td> $2.085×10^{-3}$ </td><td>100</td></tr><tr><td>13_3</td><td>S1</td><td>20</td><td>197</td><td>12</td><td>12</td><td>12</td><td>24</td><td>209.546</td><td>13.928</td><td> $2.085×10^{-3}$ </td><td>100</td></tr><tr><td>15_1</td><td>S1</td><td>3</td><td>12</td><td>4</td><td>2</td><td>2</td><td>4</td><td>21.145</td><td>16.193</td><td> $9.553×10^{-2}$ </td><td>30</td></tr><tr><td>15_2</td><td>S2</td><td>3</td><td>12</td><td>-9</td><td>2</td><td>2</td><td>4</td><td>21.145</td><td>16.193</td><td> $9.553×10^{-2}$ </td><td>30</td></tr><tr><td>15_3</td><td>S1</td><td>3</td><td>12</td><td>4</td><td>2</td><td>2</td><td>4</td><td>21.145</td><td>16.193</td><td> $9.553×10^{-2}$ </td><td>30</td></tr><tr><td>15_4</td><td>S1</td><td>3</td><td>12</td><td>3</td><td>2</td><td>2</td><td>4</td><td>21.145</td><td>16.193</td><td> $9.553×10^{-2}$ </td><td>30</td></tr><tr><td>15_5</td><td>S1</td><td>3</td><td>12</td><td>4</td><td>2</td><td>2</td><td>4</td><td>21.145</td><td>16.193</td><td> $9.553×10^{-2}$ </td><td>30</td></tr><tr><td>15_6</td><td>S2</td><td>20</td><td>155</td><td>-20</td><td>12</td><td>12</td><td>24</td><td>275.606</td><td>12.360</td><td> $8.898×10^{-3}$ </td><td>100</td></tr><tr><td>16_1</td><td>S2</td><td>20</td><td>155</td><td>5</td><td>12</td><td>12</td><td>24</td><td>275.606</td><td>12.360</td><td> $8.898×10^{-3}$ </td><td>100</td></tr><tr><td>18_1</td><td>S3</td><td>40</td><td>400</td><td>100</td><td>48</td><td>48</td><td>60</td><td>577.537</td><td>14.253</td><td> $7.365×10^{-4}$ </td><td>440</td></tr><tr><td>21_1</td><td>S3</td><td>40</td><td>400</td><td>100</td><td>48</td><td>48</td><td>60</td><td>577.537</td><td>14.253</td><td> $7.365×10^{-4}$ </td><td>440</td></tr><tr><td>22_1</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>22_2</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>22_3</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>22_4</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>22_5</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>22_6</td><td>S2</td><td>10</td><td>76</td><td>-2</td><td>6</td><td>6</td><td>12</td><td>133.919</td><td>16.193</td><td> $1.508×10^{-2}$ </td><td>45</td></tr><tr><td>23_1</td><td>S2</td><td>20</td><td>155</td><td>5</td><td>12</td><td>12</td><td>24</td><td>275.606</td><td>12.360</td><td> $8.898×10^{-3}$ </td><td>100</td></tr><tr><td>23_2</td><td>S2</td><td>20</td><td>155</td><td>3</td><td>12</td><td>12</td><td>24</td><td>275.606</td><td>12.360</td><td> $8.898×10^{-3}$ </td><td>100</td></tr><tr><td>23_3</td><td>S2</td><td>35</td><td>350</td><td>11</td><td>24</td><td>24</td><td>36</td><td>517.669</td><td>11.892</td><td> $5.220×10^{-3}$ </td><td>250</td></tr></table>

<sup>a</sup>S1: Steam: fossil-oil; S2: Steam: fossil-coal; S3: Steam: nuclear; C: Combustion turbine.

## 4.1. IEEE test system

The first test problem is based on an IEEE test problem 7 . This test system contains 24 buses, 34<sup>w</sup> <sup>x</sup> transmission lines and 32 generating units. The parameters of the generating units are summarized in Table 1, in which the unit fuel costs are assume to be a quadratic function of power generation as:

$$
C _ {i} (p _ {i t}) = a _ {i 0} + a _ {i 1} p _ {i t} + a _ {i 2} p _ {i t} ^ {2},\tag{22}
$$

and the unit startup costs $S _ { i }$ are assumed to be constants. This test system contains steam units and combustion turbines as indicated in Table 1.

The transmission line parameters are given in Table 2. In Table 2 two sets of line capacities are presented. The capacities of the first set of transmission lines are generally larger than those of the second set. Therefore, the second set of transmission lines would yield more serious congestion than the first set. A 24-h planning horizon is adopted in the test problem, the system load information can be found in Table 3. The load taken here corresponds to the day with peak load in the year in the IEEE test problem. In this test, the spinning capacity

Table 2  
Transmission line parameters

<table><tr><td> $\ell$ </td><td>From bus</td><td>To bus</td><td>X (p.u.)</td><td>(i)  $F_{\ell}$  (MW)</td><td>(ii)  $F_{\ell}$  (MW)</td></tr><tr><td>1</td><td>1</td><td>2</td><td>0.0139</td><td>175</td><td>175</td></tr><tr><td>2</td><td>1</td><td>3</td><td>0.2112</td><td>175</td><td>175</td></tr><tr><td>3</td><td>1</td><td>5</td><td>0.0845</td><td>175</td><td>175</td></tr><tr><td>4</td><td>2</td><td>4</td><td>0.1267</td><td>175</td><td>175</td></tr><tr><td>5</td><td>2</td><td>6</td><td>0.1920</td><td>175</td><td>175</td></tr><tr><td>6</td><td>3</td><td>9</td><td>0.1190</td><td>175</td><td>175</td></tr><tr><td>7</td><td>3</td><td>24</td><td>0.0839</td><td>400</td><td>175</td></tr><tr><td>8</td><td>4</td><td>9</td><td>0.1037</td><td>175</td><td>175</td></tr><tr><td>9</td><td>5</td><td>10</td><td>0.0883</td><td>175</td><td>175</td></tr><tr><td>10</td><td>6</td><td>10</td><td>0.0605</td><td>175</td><td>175</td></tr><tr><td>11</td><td>7</td><td>8</td><td>0.0614</td><td>175</td><td>175</td></tr><tr><td>12</td><td>8</td><td>9</td><td>0.1651</td><td>175</td><td>175</td></tr><tr><td>13</td><td>8</td><td>10</td><td>0.1651</td><td>175</td><td>175</td></tr><tr><td>14</td><td>9</td><td>11</td><td>0.0839</td><td>400</td><td>175</td></tr><tr><td>15</td><td>9</td><td>12</td><td>0.0839</td><td>400</td><td>136</td></tr><tr><td>16</td><td>10</td><td>11</td><td>0.0839</td><td>400</td><td>200</td></tr><tr><td>17</td><td>10</td><td>12</td><td>0.0839</td><td>400</td><td>250</td></tr><tr><td>18</td><td>11</td><td>13</td><td>0.0476</td><td>400</td><td>198</td></tr><tr><td>19</td><td>11</td><td>14</td><td>0.0418</td><td>400</td><td>250</td></tr><tr><td>20</td><td>12</td><td>13</td><td>0.0476</td><td>400</td><td>150</td></tr><tr><td>21</td><td>12</td><td>23</td><td>0.0966</td><td>400</td><td>166</td></tr><tr><td>22</td><td>13</td><td>23</td><td>0.0865</td><td>400</td><td>250</td></tr><tr><td>23</td><td>14</td><td>16</td><td>0.0389</td><td>400</td><td>220</td></tr><tr><td>24</td><td>15</td><td>16</td><td>0.0173</td><td>400</td><td>250</td></tr><tr><td>25</td><td>15</td><td>21</td><td>0.0245</td><td>400</td><td>290</td></tr><tr><td>26</td><td>15</td><td>24</td><td>0.0519</td><td>400</td><td>270</td></tr><tr><td>27</td><td>16</td><td>17</td><td>0.0259</td><td>400</td><td>270</td></tr><tr><td>28</td><td>16</td><td>19</td><td>0.0231</td><td>400</td><td>270</td></tr><tr><td>29</td><td>17</td><td>18</td><td>0.0144</td><td>400</td><td>270</td></tr><tr><td>30</td><td>17</td><td>22</td><td>0.1053</td><td>400</td><td>270</td></tr><tr><td>31</td><td>18</td><td>21</td><td>0.0129</td><td>400</td><td>270</td></tr><tr><td>32</td><td>19</td><td>20</td><td>0.0198</td><td>400</td><td>198</td></tr><tr><td>33</td><td>20</td><td>23</td><td>0.0108</td><td>300</td><td>270</td></tr><tr><td>34</td><td>21</td><td>22</td><td>0.0678</td><td>400</td><td>270</td></tr></table>

Table 3  
Load information

<table><tr><td colspan="3">System load</td><td colspan="2">Bus load</td></tr><tr><td>Hour</td><td>Load (MW)</td><td>% of peak</td><td>Bus</td><td>% of peak</td></tr><tr><td>1</td><td>2223.0</td><td>78</td><td>1</td><td>3.8</td></tr><tr><td>2</td><td>2052.0</td><td>72</td><td>2</td><td>3.4</td></tr><tr><td>3</td><td>1938.0</td><td>68</td><td>3</td><td>6.3</td></tr><tr><td>4</td><td>1881.0</td><td>66</td><td>4</td><td>2.6</td></tr><tr><td>5</td><td>1824.0</td><td>64</td><td>5</td><td>2.5</td></tr><tr><td>6</td><td>1852.5</td><td>65</td><td>6</td><td>4.8</td></tr><tr><td>7</td><td>1881.0</td><td>66</td><td>7</td><td>4.4</td></tr><tr><td>8</td><td>1995.0</td><td>70</td><td>8</td><td>6.0</td></tr><tr><td>9</td><td>2280.0</td><td>80</td><td>9</td><td>6.1</td></tr><tr><td>10</td><td>2508.0</td><td>88</td><td>10</td><td>6.8</td></tr><tr><td>11</td><td>2565.0</td><td>90</td><td>11</td><td>0</td></tr><tr><td>12</td><td>2593.5</td><td>91</td><td>12</td><td>0</td></tr><tr><td>13</td><td>2565.0</td><td>90</td><td>13</td><td>9.3</td></tr><tr><td>14</td><td>2508.0</td><td>88</td><td>14</td><td>6.8</td></tr><tr><td>15</td><td>2479.5</td><td>87</td><td>15</td><td>11.1</td></tr><tr><td>16</td><td>2479.5</td><td>87</td><td>16</td><td>3.5</td></tr><tr><td>17</td><td>2593.5</td><td>91</td><td>17</td><td>0</td></tr><tr><td>18</td><td>2850.0</td><td>100</td><td>18</td><td>0</td></tr><tr><td>19</td><td>2821.5</td><td>99</td><td>19</td><td>6.4</td></tr><tr><td>20</td><td>2764.5</td><td>97</td><td>20</td><td>4.5</td></tr><tr><td>21</td><td>2679.0</td><td>94</td><td>21</td><td>0</td></tr><tr><td>22</td><td>2622.0</td><td>92</td><td>22</td><td>0</td></tr><tr><td>23</td><td>2479.5</td><td>87</td><td>23</td><td>0</td></tr><tr><td>24</td><td>2308.5</td><td>81</td><td>24</td><td>0</td></tr></table>

requirements are set to be $R _ { t } = 1 . 0 7 ~ D _ { t }$ for all t. The proposed algorithm is applied to solve this test problem. The test result is summarized in Table 4.

In case i of the transmission line capacityŽ . $F _ { \ell }$ , the test result shows that line 33 is always congested and line 11 becomes congested during peak hours. In this test case, it is noted that no combustion turbine is turned on during the planning horizon. The duality gap is 0.47% in this case. Compared with the total cost in the unconstrained case, the increased cost due to the transmission network is about 0.17% of the total cost of the unconstrained case. In the second case ii ofŽ . $F _ { \ell } ,$ , the congestion of the network involves seven lines. There are 12 h on the planning horizon in which there are 5 lines congested during the peak hours , 7 h with 4 lines, 4 h Ž . with 2 lines and 1 h with 1 line congested. The increased cost due to the transmission system constraints increases to 1.5% of the total cost of the unconstrained case. The congestion is much more serious than in the case i . It can be observed that when the transmission network gets more congested, the algorithm takes longerŽ . time to converge, specially in the dual optimization and in obtaining a feasible solution in the feasibility phase. Congestion of the transmission network also yields poorer larger duality gap. In this case, we also found thatŽ . the duality gap of 1.43% is primarily due to the poor dual objective value obtained. In another test run, tripling the CPU time spent on the dual optimization improves the dual value to 902 758 with the primal value reduced to 912 576 for the duality gap of 1.09%. Overall, our experience show that our feasibility phase is very robust in obtaining feasible solutions.

Test result of IEEE test problem direct approachŽ .

<table><tr><td>Case</td><td>Dual value</td><td>Primal value</td><td colspan="2">Duality gap</td></tr><tr><td>Unconstrained</td><td>US$898,619</td><td>US$898,683</td><td>0.00%</td><td></td></tr><tr><td>Constrained  $F_{\ell}$  (i)</td><td>US$895,980</td><td>US$900,206</td><td>0.47%</td><td></td></tr><tr><td>Constrained  $F_{\ell}$  (ii)</td><td>US$899,662</td><td>US$912,650</td><td>1.43%</td><td></td></tr><tr><td rowspan="2">Case</td><td colspan="4">CPU time (s)</td></tr><tr><td>Ph 1</td><td>Ph 2</td><td>Ph 3</td><td>Total</td></tr><tr><td>Unconstrained</td><td>3.72</td><td>0.37</td><td>2.32</td><td>6.41</td></tr><tr><td>Constrained  $F_{\ell}$  (i)</td><td>7.81</td><td>5.77</td><td>6.28</td><td>19.86</td></tr><tr><td>Constrained  $F_{\ell}$  (ii)</td><td>7.79</td><td>12.14</td><td>10.92</td><td>30.85</td></tr></table>

## 4.2. Direct and indirect approaches

In Ref. 12 , the direct and indirect methods are defined. Those methods which take transmission constraints<sup>w</sup> <sup>x</sup> into account in the dual optimization are called direct methods and those which do not are called indirect. Indirect methods ignore the transmission constraints in the dual optimization, but deal with them only in the feasibility phase. In this section, we shall compare two algorithms. Using the same naming convention as in Ref. <sup>w</sup> <sup>x</sup> 12 , we will call them the direct approach and the indirect approach. The direct approach is the three-phase algorithm proposed in this paper. The indirect approach is essentially the direct approach except that the multiplier $\alpha _ { t \ell } = \beta _ { t \ell } = 0 .$ , for $\forall t , \ell$ through out the algorithm, and the transmission constraints are enforced through Eq. 20d during the feasibility phase.Ž .

The major motivations for applying the indirect approach are to speed up the dual optimization, and to save memory space. Another reason for using the indirect approach may be to simulate a power market structure, like that of the British power pool, where an initial unit commitment does not consider transmission constraints, and transmission constraints are considered only in modifying this initial commitment. We also applied the indirect approach to solve the IEEE test problem given in the previous. The result is summarized in Table 5. It can be seen in Table 5 that the direct approach obtains a better solution and uses less CPU time. The indirect approach only uses less CPU time in the dual optimization phase Ph 1 , but spends more time to locate a feasibleŽ . solution. Also the quality of the solution obtained from the feasibility phase of the indirect approach tends to be worse than that from the direct approach, so that it might take longer for unit decommitment to improve the solution. Our comparison between the direct and indirect approaches agrees with what is observed in Ref. 12 .<sup>w</sup> <sup>x</sup>

## 4.3. A PG&E test problem

The proposed three-phase algorithm is also applied to a test problem based on PG&E’s system. The test problem with more than 2500 lines, 2200 buses and 79 dispatchable generating units is derived with necessary modifications to fit the scope discussed in this paper. The peak load is 3957 MW only the percentageŽ contributed by the thermal units . The test result is given in Table 6. We emphasize that these test results used a. program developed for research purpose with little effort spent in speeding up the algorithm performance. The motivation is to see how the algorithm performs on a large scale problem. We observe: 1 the convergence ofŽ . the dual optimization is not directly affected by the increased number of multipliers corresponding to the transmission constraints but by the increased number of nonzero multipliers. The more congested the network is, the more iterations are required to reach a near-optimal dual solution. We observe that the dual objective value tends to improve more slowly as the congestion of the network increases. 2 The CPU time required in this testŽ . problem, although high, scales approximate linearly with problem size. Algorithm performance can be improved by taking advantage of the sparsity of the matrix of the distribution factors and the multipliers associated with the transmission constraints. Along this direction, a large scale ‘bus-based’ model can be equivalent reduced to a small sized ‘area-based’ one without violating problem optimality, and the algorithm performance can be greatly accelerated 17 .<sup>w</sup> <sup>x</sup>

Table 5  
Test result of the indirect approach

<table><tr><td>Case</td><td>Dual value</td><td>Primal value</td><td>Duality gap</td><td></td></tr><tr><td>Constrained  $F_{\ell}$  (i)</td><td>US$895,840</td><td>US$901,289</td><td>0.60%</td><td></td></tr><tr><td>Constrained  $F_{\ell}$  (ii)</td><td>US$895,840</td><td>US$913,542</td><td>1.97%</td><td></td></tr><tr><td rowspan="2">Case</td><td colspan="4">CPU time (s)</td></tr><tr><td>Ph 1</td><td>Ph 2</td><td>Ph 3</td><td>Total</td></tr><tr><td>Constrained  $F_{\ell}$  (i)</td><td>5.69</td><td>21.74</td><td>10.45</td><td>37.88</td></tr><tr><td>Constrained  $F_{\ell}$  (ii)</td><td>5.80</td><td>18.72</td><td>9.52</td><td>34.04</td></tr></table>

Table 6  
Test result of a large scale problem

<table><tr><td>Total cost ($)</td><td>CPU time (s)</td></tr><tr><td>Dual optimal: 199,216.56</td><td>Ph. 1:1292.47</td></tr><tr><td>Primal optimal: 200,214.32</td><td>Ph. 2:116.60</td></tr><tr><td>Duality gap: 1.469%</td><td>Ph. 3:108.32</td></tr><tr><td></td><td>Total: 1512.39</td></tr></table>

## 5. Conclusions

In this paper we presented a transmission-constrained unit commitment algorithm using the Lagrangian relaxation approach. The transmission constraints are formulated as linear constraints under the DC power flow model. The Lagrangian relaxation approach relaxes the demand constraints, the spinning reserve constraints and the transmission constraints using multipliers. In this paper, we employ a three-phase algorithmic scheme. Phase 1, the subgradient method is used to maximize the dual function to determine a near-optimal dual solution. A feasibility phase follows to locate a feasible commitment. The feasibility phase is essentially an extension of that in the single area unit commitment case. Initially a reserve-feasible commitment is located, then by solving linear programs a dispatchable commitment is determined. Finally we devise a transmission-constrained unit decommitment method, which serves as a post-processing method of the algorithm.

In limited numerical tests, the proposed algorithm is found to be efficient and robust. A large scale problem based on PG&E system is also tested. The result suggests that the proposed algorithm can be used to deal with practical-sized transmission-constrained unit commitment problems.

## Acknowledgements

This work was partly supported by the National Science Foundation under Grant IRI-9120074 and PG&E’s R&D Department. Their support is greatly appreciated.

## References

<sup>w</sup> <sup>x</sup> 1 M.S. Bazaraa, C.M. Shetty, Nonlinear Programming—Theory and Algorithms, Wiley, New York, 1979.

<sup>w</sup> <sup>x</sup> 2 D.P. Bertsekas, G.S. Lauer, N.R. Sandell Jr., T.A. Posbergh, Optimal short-term scheduling of large-scale power systems, IEEE Transactions on Automatic Control AC 28 1 1983 1–11.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 W.G. Chandler, P.L. Dandeno, A.F. Gilmn, L.K. Kirchmayer, Short-Range Operation of a Combined Thermal and Hydroelectric Power System, AIEE, Transactions, Oct. 1953, pp. 53-326.

<sup>w</sup> <sup>x</sup> 4 A. Cohen, V. Sherkat, Optimization-based methods for operations scheduling, Proc. IEEE 75 12 1987 1574–1591. Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 L.A.F.M. Ferreira, T. Andersson, C.F. Imparato, T.E. Miller, C.K. Pang, A.J. Svoboda, A.F. Vojdani, Short-term resource scheduling in multi-area hydrothermal power systems, Electrical Power and Energy Systems 11 3 1989 200–212.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 X. Guan, P.B. Luh, H. Yan, An optimization-based method for unit commitment, Electrical Power and Energy Systems 14 1 1992Ž . Ž . 9–17.

<sup>w</sup> <sup>x</sup> 7 IEEE Reliability Test System, IEEE Transactions on Power Apparatus and Systems, Vol. PAS-98, No. 6, Nov.<sup>r</sup>Dec. 1979, pp. 2047–2054.

<sup>w</sup> <sup>x</sup> 8 F.N. Lee, Short-term thermal unit commitment—a new method, IEEE Transactions on Power Systems 3 2 1988 421–428.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 C. Murillo-Sanchez, R.J. Thomas, Thermal Unit Commitment Including Optimal AC Power Flow Constraints, Proceedings of the 31st´ Hawaii International Conference on System Sciences, Jan. 1998.

<sup>w</sup> <sup>x</sup> 10 C.K. Pang, H.C. Chen, Optimal short-term thermal unit commitment, IEEE Transactions on Power Apparatus and Systems PAS 95 4Ž . Ž .1976 1336–1342.

<sup>w</sup> <sup>x</sup>11 C.K. Pang, G.B. Sheble, F. Albuyeh, Evaluation of dynamic programming based methods and multiple area representation for therma unit commitments, IEEE Transactions on Power Apparatus and Systems PAS 100 3 1981 1212–1218.Ž . Ž .

<sup>w</sup> <sup>x</sup>12 J.J. Shaw, A direct method for security-constrained unit commitment, IEEE Transactions on Power Systems 10 3 1995 1329–1342Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 A.J. Svoboda, C.L. Tseng, C.A. Li, R.B. Johnson, Short term resource scheduling with ramp constraints, IEEE Transactions on Power Systems 12 1 1997 77–83.Ž . Ž .

<sup>w</sup> <sup>x</sup>14 C.L. Tseng, On Power System Generation Unit Commitment Problems, PhD Thesis, Department of Industry Engineering and Operations Research, Univ. of California at Berkeley, Dec. 1996.

<sup>w</sup> <sup>x</sup> 15 C.L. Tseng, S.S. Oren, A.J. Svoboda, R.B. Johnson, A unit decommitment method in power system scheduling, Electrical Power and Energy Systems 19 6 1997 357–365. Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 C.L. Tseng, S.S. Oren, C.S. Cheng, C.A. Li, A.J. Svoboda, R.B. Johnson, A Transmission-Constrained Unit Commitment Method, Proceedings of the 31st Hawaii International Conference on System Sciences, Jan. 1998.

<sup>w</sup> <sup>x</sup> 17 C.L. Tseng, X. Guan, A.J. Svoboda, Multi-area unit commitment for large-scale power systems, IEE Proceedings C, Generation, Transmission and Distribution 145 1998 415–422.Ž .

<sup>w</sup> <sup>x</sup> 18 A.J. Wood, B.F. Wollenberg, Power Generation, Operation and Control, Wiley, New York, 1984.

<sup>w</sup> <sup>x</sup> 19 F. Zhuang, F.D. Galiana, Towards a more rigorous and practical unit commitment by Lagrangian relaxation, IEEE Transactions on Power Systems PWRS 3 2 1988 763–770.Ž . Ž .

Chung-Li Tseng an Assistant Professor in Civil Engineering Department at the University of Maryland at College Park. He received a B.S. in Electrical Engineering from National Taiwan University in 1988, and a M.S. in Electrical and Computer Engineering from U.C. Davis in 1992 and a Ph.D. in Industrial Engineering and Operations Research from U.C. Berkeley in 1996. He has worked as an operational research consultant for PG&E from 1995 to 1996. Since 1997 he has been with Edison Enterprises as a senior risk management researcher. His research interests include financial engineering, optimization applied to industrial applications and neural network computation.

Shmuel S. Oren is Professor of Industrial Engineering and Operations Research at the University of California at Berkeley. He holds a B.S. and M.S. in Mechanical Engineering from the Technion in Israel and an M.S. and Ph.D. in Engineering Economic Systems from Stanford. Prior to his current position he was on the faculty of the Engineering Economic Systems Department at Stanford University and he worked for eight years as a research scientist at the Xerox Palo Alto Research Center. His research interests include Optimization theory, Modeling and analysis of economic systems, Coordination and decentralization through market mechanisms and Electric utility planning and operations.

Carol S. Cheng was born in Beijing China. She received B.S. in Electrical Engineering from Northern Jiaotong University in Beijing in 1982, M.S. in Mechanical Engineering from University of Cincinnati in 1986, and Ph.D. in Electrical Engineering from Georgia Institute of Technology in 1991. From 1982 to 1985, she joined the faculty of Northern Jiaotong University as a Teaching Assistant. From 1992 to 1995 she worked with the Energy Systems Automation group of PG&E where she developed several advanced applications for distribution systems. Currently she is a Systems Engineer in the Application Integration group responsible for the development of applications on resource scheduling and generation heat rate modeling.

Chao-an Li graduated from Electric Power System Department of Moscow Energetic Institute, Moscow, USSR. He has broad interests in power system optimization including hydrothermal coordination, economic dispatch, unit commitment, load forecasting, automatic generation control, power flow and power system state estimation problems. and network analysis. He is currently working on projects related to hydro-thermal optimization for PG&E.

Alva J. Svoboda received a B.A. in mathematics from U.C. Santa Barbara in 1980, and an M.S. and Ph.D. in Operations Research from U.C. Berkeley in 1984 and 1992. He has worked on contract as an operations research analyst for Pacific Gas and Electric since 1986. His current research interest is the extension of existing utility operations planning models to incorporate new operating constraints.

Raymond B. Johnson received his B.A. in 1976 in Electrical Sciences from Trinity College, Cambridge University, and a Ph.D. in Electrical Engineering from Imperial College, London University in 1985. His professional experience includes positions as a power system design engineer with Hawker Siddeley Power Engineering from 1976 to 1980 and an EMS applications developer with Ferranti International Controls from 1987 to 1989. Since 1989, has been with PG&E where he is currently a Systems Engineering Team Leader responsible for resource scheduling and energy trading applications.
