---
otero_id: 1772
otero_key: "G2KKMGJR"
title: "The role of market pricing mechanism under imperfect competition"
authors: "Hossein Haghighat; Hossein Seifi; Ashkan Rahimi Kian"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.12.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# The role of market pricing mechanism under imperfect competition

Hossein Haghighat <sup>a,⁎</sup>, Hossein Seifi <sup>b</sup>, Ashkan Rahimi Kian <sup>c</sup>

<sup>a</sup> Department of ECE, University of Waterloo, Waterloo, Canada

<sup>b</sup> Department of Electrical Engineering, Tarbiat Modares University (TMU), Tehran, Iran

<sup>c</sup> CIPCE, School of ECE, College of Engineering, University of Tehran, Tehran, Iran

Received 16 May 2007; received in revised form 17 December 2007; accepted 19 December 2007 Available online 31 December 2007

## Abstract

This paper illustrates how a supplier profit may be affected by the market pricing mechanism under imperfect competition. A parameterized Supply Function Equilibrium (SFE) model involving manipulation of the sole intercept is used to represent the strategic behavior of each supplier. Through utilizing a bilevel optimization technique and a Mathematical Program with Equilibrium Constraints (MPECs) approach, market equilibria are calculated and compared under pay-as-bid pricing (PABP) and marginal pricing (MP) mechanisms. For an unconstrained case, analytically it is demonstrated that the optimal bidding strategy and the maximum profit of each supplier, as well as the market clearing price are the same under PABP and MP. The effects of the transmission limits and the supplier capacity constraints are discussed through numerical results. © 2007 Elsevier B.V. All rights reserved.

Keywords: Bidding strategy; Electricity market; Marginal pricing; Nash equilibrium; Pay-as-bid pricing; Risk profile

## 1. Introduction

The most common approaches for auctioning electricity markets are sealed-bid mechanisms. Suppliers offer supply schedules and supply curve which exhibits price versus cumulative quantity is formed. The intersection of the supply and demand curves determines the market clearing price. All bids submitted at a price lower than or equal to the market clearing price are accepted and paid according to either pay-as-bid pricing (PABP) or marginal pricing (MP) mechanism. Under PABP scheme, suppliers are paid their own bids that have offered to the independent system operator (ISO), whereas under MP scheme, accepted suppliers are paid the market marginal price (either the last accepted priceoffer, or the first rejected price-offer). PABP mechanism may force suppliers to bid higher than their marginal costs in order to make profit while under MP suppliers gain profits even if they bid their marginal costs.

The choice between MP and PABP mechanisms for electricity markets and the arguments for and against them have been the subject of recent studies [17,20,9,30,16]. Although revenue equivalence result [17] suggests that the expected payment in a uniform pricing scheme will be identical with that in a PABP mechanism, some papers argue in favor of MP (see e.g., [30,16]) because of other considerations such as fairness and efficiency. MP is recognized efficient since bidders have an incentive to reveal their true costs and the resulting dispatch will be efficient [20]. MP is also known to be fair because all winners receive (or pay) the same price and nonwinners fail to win as they refuse to offer at or less than the market clearing price [9]. A potential problem with MP is that whenever a supplier can influence the price, MP mechanism gives the supplier an opportunity to exercise market power by bidding above its marginal cost. PABP is recommended as a way to prevent the exercise of market power. In contrast to MP, under PABP there is no incentive to increase the offer curve above marginal cost in an effort to increase the price received on all quantity offered below the market clearing price [9]. Reduced price volatility is one of the arguments used in support of PABP because it is based on an average price rather than on a marginal price which is volatile to gaming [31]. Another advantage with the PABP is that the risk for tacit collusion is lower in this mechanism compared to MP [11]. A drawback of pay-as-bid pricing is that market price does not reflect a surplus or deficit of the generation capacity and in the long-run it can deprive potential investors of receiving correct economic signals [21].

A number of recent studies have focused on the bidding behavior in the electricity markets and have compared the market performances under PABP and MP [30,12,11,21,22,27,15]. Wolfram [30] illustrated a simple electricity auction to examine the differences between discriminatory and uniform pricing auctions [30]. It is shown that for a typical case there are equal revenues from the discriminatory and the uniform pricing cases. Federico and Rahman [2003] compared uniform price and discriminatory auctions for perfect competition and monopoly. They demonstrated that the expected output decreases and the expected consumer surplus increases after a switch to PABP. Analysis in [11] concentrates on developing Nash equilibria for a duopoly model with constant marginal costs. It is shown that if the demand is inelastic and certainly known, the average prices will be lower under PABP. Ren and Gailana compared the quantitative behavior of a perfectly competitive market under PABP and MP structures [21,22]. For an uncertain demand, they demonstrated that although MP and PABP yield equal expected generator profits and consumer payments, the risk of not meeting the expected values is greater under MP. Game theory and auction theory are employed in [27] to analyze the strategic behavior of a two-player auction game under discriminatory and uniform pricing mechanisms. It is shown that the revenue equivalence theorem does not hold in a simple multiunit auction model in the presence of market power. Reference [15] develops an SFE model for a discriminatory auction and proves that SFE always exists if the system demand follows an inverse polynomial probability distribution. Given this probability distribution and compared to the uniform price auction, the demand-weighted average price is shown to be equal or lower in the discriminatory auction. Theoretical explorations of SFE have been attempted in [24] through relaxing assumptions of continuity of supply functions with focus on one-price payment rule. Reference [19] shows that discriminatory price auctions are preferable to the current practice of using uniform price auctions to determine spot prices. It demonstrates that under a discriminatory auction the supply curve is relatively elastic which reduces the price volatility caused by errors in forecasting total system demand.

In recent studies (e.g. [18,7,4,26]), the problem of strategic bidding is formulated as a bilevel optimization problem using SFE model, and an MPEC approach, introduced in [14], is used to solve the problem. For instance, reference [18] employs this technique to develop an optimum transmission expansion plan for a given power system when the gaming behavior of the power producers is taken into account. Reference [4] adopts the same framework to evaluate the performances of a typical power market with network constraints under strategic interactions amongst suppliers.

This paper characterizes the supply function equilibrium under PABP and MP mechanisms under imperfect competition with and without transmission limits. Strategic behavior of suppliers is represented via a parameterized SFE model involving manipulation of the sole intercept. The game problem is formulated as a bilevel optimization problem where each supplier solves an MPEC with the ISO's Karush-Kuhn-Tucker (KKT) conditions as constraints. For an unconstrained case, it is demonstrated that the optimal bidding strategy and the maximum profit of each strategic supplier, as well as the market clearing price are the same under PABP and MP mechanisms. However, this conclusion may not hold when transmission constraints and supply capacity limits are observed. Taking generators' random outages into account, the risk profile for each supplier is created through market simulation under PABP and MP mechanisms.

The remainder of this paper is organized as follows. Notations are introduced in Section II. Section III provides the mathematical problem formulation including the ISO and the supplier problems. The game solution technique and a methodology for constructing risk profiles are also presented in section III. Section IV is devoted to the simulation results of several case studies. Concluding remarks are presented in section V.

## 2. Notation

The notations used in this paper are introduced as follows. For a generic variable x, the notation $x _ { i }$ (for $i { = } 1 \ldots n )$ is used to refer to each element of vector x. The upper bound on the value of $x _ { i }$ is represented by ${ \overline { { x } } } _ { i \cdot }$ Notation $q$ is used for quantity and $p$ for price. Subscripts e and $d$ stand for energy and demand, respectively. Notation “diag(w)” indicates a diagonal matrix whose entries are the components of the vector w. Notation $u \perp \nu$ is used for expressing the complimentary conditions which means the two vectors are perpendicular.

The electrical network composed of n nodes, indexed by i. Each demand at node i is represented by $q _ { d , i } . ~ G _ { i , f }$ denotes supplier f at node $\therefore N _ { G }$ refers to the total number of generators. The set of arcs is denoted by A and, if $i j \in { \cal A }$ there is an arc between i and $j .$ The power flow between nodes i and j is represented by $F _ { \mathrm { i j } } .$ . Notation $\overline { { F } } _ { \mathrm { i j } }$ is used for capacity limit of the line connecting nodes i and $j . ~ L$ is the set of Kirchhoff loops in the network indexed by m such that $L _ { m }$ is the ordered set of arcs associated with kirchhoff loop $m , z _ { \mathrm { i j } }$ is the reactance on arc $i j \in L$ and $s _ { i j m } = \pm 1$ , depending on the orientation of arc ij in loop m. R denotes the (arc, loop) incidence matrix which is equal to $s _ { i j m } z _ { i j }$ if $i j \in L$ and is zero otherwise. Δ denotes the (node, arc) incidence matrix of the electrical network whose entries $\varDelta _ { i l }$ are +1 if $l { = } i j ,$ and $- 1 \mathrm { i f } l = j i ,$ , and are zero otherwise $( i j \in$ set of arcs and $j \in$ set of network nodes). $x ^ { t }$ represents a generic variable x in time period t. Ramp up rate and ramp down rate limits are denoted by ru and rd, respectively. $\delta ^ { t }$ is defined as: $\delta ^ { t } = 0$ for $t = T$ and $\delta ^ { t } = 1$ for $t < T .$

The marginal cost function of each supplier is assumed affine in the form $p ( q _ { e , i , f } ^ { t } ) = a _ { e , i , f } + b _ { e , i , f } q _ { e , i , f } ^ { t }$ where $a _ { e , i , f }$ and $b _ { e , i , f }$ are positive coefficients (linear bids are assumed here to simplify the analysis presented in the following sections. The exact bidding behavior can be different in realistic power markets). For every supplier (player) in the game, $\boldsymbol { \mathfrak { a } } _ { e , i , f } ^ { t }$ (or, for short $\alpha _ { i , f } ^ { t } )$ represents the bidding strategy of supplier f and $\alpha _ { i , - f } ^ { \quad t }$ indicates the bidding strategies of suppliers other than supplier f. The payoff function of supplier f is denoted by $\pi _ { i , f } ( \alpha _ { i , f } ^ { t } \alpha _ { i , - f } ^ { t } )$ To model the strategic behaviors, $\boldsymbol { \alpha } _ { e , i , f } ^ { t }$ supersedes true intercept $a _ { e , i , f }$ in the marginal cost function. The failure probability of $G _ { i , f }$ is denoted by $f p _ { i , f } \ E ( x )$ indicates the expected value of x. Symbol $\therefore \angle C = 9 0 ^ { \circ }$ indicates the values in the equilibrium state.

## 3. Mathematical modeling

## 3.1. Market assumptions

In this paper, an affine nondecreasing supply function is considered for each supplier as it allows representing more realistically the bidding procedure via strategic variation of the supply bid. When an SFE model is adopted, there exist different ways that the supply function could be manipulated [1]. As found in [14,3,4] a preferable choice for bidding, a parameterized SFE model with a one-degree-of-freedom parameterization is utilized in this study. It is assumed that each supplier manipulates the intercept of its supply function and keeps the slope equal to its true value. Therefore, $\alpha _ { e , \ - }$ $i , f ^ { t }$ is the decision variable for each supplier through which it can strategically act. Other parameterization methods were undertaken in literature, as in [18], where manipulation of the slope is considered, or as in [28], where the slope is manipulated in proportion with the intercept.

## 3.2. Market-clearing rule

The market-clearing rule is the maximization of the social welfare, or equivalently, the minimization of the aggregated supply function minus the aggregated demand function, subject to power flow balance conditions as described below (DC load flow formulation)

$$
q _ {d, i} ^ {t} - q _ {e, i, f} ^ {t} + \sum_ {j; i j \in A} F _ {i j} ^ {t} - \sum_ {j; j i \in A} F _ {j i} ^ {t} = 0, q _ {d, i} ^ {t} \geq 0\tag{1}
$$

where $q _ { d , i } ^ { t }$ and $q _ { e , i , f } ^ { t }$ are nodal withdraw and injection, respectively. $\boldsymbol { F } _ { i j } ^ { t }$ represents line flow.

Including other relevant constraints, the resulting market-clearing problem can be formulated as a convex quadratic programming problem as

$$
\operatorname * {M i n} _ {q _ {e} ^ {t}, F ^ {t}} \sum_ {t} \sum_ {i, f} \alpha_ {e, i, f} ^ {t} q _ {e, i, f} ^ {t} + \frac {1}{2} b _ {e, i, f} \left(q _ {e, i, f} ^ {t}\right) ^ {2}\tag{2}
$$

subject to

$$
0 \leq q _ {e, i, f} ^ {t} \leq \overline {{q}} _ {e, i, f} \quad \forall i, f, t\tag{3}
$$

$$
q _ {e, i, f} ^ {t} - q _ {e, i, f} ^ {t - 1} \leq r u _ {i, f} \quad \forall i, f, t\tag{4}
$$

$$
q _ {e, i, f} ^ {t - 1} - q _ {e, i, f} ^ {t} \leq r d _ {i, f} \quad \forall i, f, t\tag{5}
$$

$$
0 \leq F _ {i j} ^ {t} \leq \overline {{F}} _ {i j} \quad \forall i, j, t\tag{6}
$$

$$
\sum_ {i j \in L} s _ {i j m} z _ {i j} F _ {i j} ^ {t} = 0 \quad \forall m, t\tag{7}
$$

and constraint 1

8

where (2) represents the total cost of producing energy which depends on the bids submitted by the participants.

Eq. (3) specifies the maximum capacity limit of the supplier. Eqs.(4) and (5) are ramp up and ramp down rate limits of each generator, representing physical limitations for increasing and decreasing the output level. Eq. (6) imposes restrictions over the line flows to comply with line limits. Eq. (7) states the Kirchhoff voltage law. The constraint in (8) was introduced before.

Forming the KKT conditions for the primal problem (2)–(8), and using dual variables $\mu ^ { t } , \tau ^ { t } , \hat { \sigma _ { \hphantom { t } } ^ { t } } , \lambda _ { e } ^ { t } , \nu ^ { \hat { t } } ,$ and $\eta ^ { t } ,$ the following linear complementary formulation of the primal problem is obtained [14]

$$
0 \leq \overline {{q}} _ {e} - q _ {e} ^ {t} \quad \perp \quad \mu^ {t} \geq 0\tag{9}
$$

$$
0 \leq r u - q _ {e} ^ {t} + q _ {e} ^ {t - 1} \quad \perp \quad \tau^ {t} \geq 0\tag{10}
$$

$$
0 \leq r d - q _ {e} ^ {t - 1} + q _ {e} ^ {t} \quad \perp \quad \sigma^ {t} \geq 0\tag{11}
$$

$$
0 \leq q _ {e} ^ {t} \perp \mu^ {t} - \lambda_ {e} ^ {t} + \alpha_ {e} ^ {t} + \mathrm{diag} (b _ {e}) q _ {e} ^ {t}
$$

$$
+ \tau^ {t} - \sigma^ {t} - \delta^ {t} (\tau^ {t + 1} - \sigma^ {t + 1}) \geq 0\tag{12}
$$

$$
0 \leq v ^ {t} \quad \perp \quad \overline {{F}} - F ^ {t} \geq 0\tag{13}
$$

$$
0 \leq F ^ {t} \quad \perp \quad \Delta^ {\prime} \lambda_ {e} ^ {t} + v ^ {t} + R ^ {\prime} \eta^ {t} \geq 0\tag{14}
$$

$$
\lambda_ {e} ^ {t} \text { free } \quad q _ {d} ^ {t} - q _ {e} ^ {t} + \Delta F ^ {t} = 0\tag{15}
$$

$$
\eta^ {t} \text { free } R F ^ {t} = 0\tag{16}
$$

where matrices Δ and R were introduced in section II (apex “′” has the meaning of transpose).

## 3.3. Supplier problem

The problem faced by each supplier (holding a single generator) is the maximization of profit; the difference between the revenue and the production cost. The cost of producing energy is estimated by

$$
\left(\operatorname{cost}\right) _ {e, i, f} = \sum_ {t} a _ {e, i, f} q _ {e, i, f} ^ {t} + \frac {1}{2} b _ {e, i, f} \left(q _ {e, i, f} ^ {t}\right) ^ {2}.\tag{17}
$$

The supplier revenue comes from the sale of energy in the market. Under PABP and MP mechanisms, it is calculated as

$$
(\text { revenue }) _ {e, i, f} ^ {\text { PABP }} = \sum_ {t} \alpha_ {e, i, f} ^ {t} q _ {e, i, f} ^ {t} + b _ {e, i, f} \left(q _ {e, i, f} ^ {t}\right) ^ {2}\tag{18}
$$

$$
\left(\text { revenue }\right) _ {e, i, f} ^ {\mathrm{MP}} = \sum_ {t} \lambda_ {e, i} ^ {t} q _ {e, i, f} ^ {t}\tag{19}
$$

where $\lambda _ { e , i } ^ { t }$ in Eq. (19) is the marginal nodal price. Hence, the supplier profit under each pricing scheme becomes

$$
\begin{array}{r l} \Pi_ {i, f} ^ {\mathrm{PABP}} & = \sum_ {t} \Pi_ {i, f} ^ {t} ^ {\mathrm{PABP}} \\ & = \sum_ {t} \left(\alpha_ {e, i, f} ^ {t} - a _ {e, i, f} + \frac {1}{2} b _ {e, i, f} q _ {e, i, f} ^ {t}\right) \times q _ {e, i, f} ^ {t} \end{array}\tag{20}
$$

$$
\begin{array}{l} \Pi_ {i, f} ^ {\mathrm{MP}} = \sum_ {t} \Pi_ {i, f} ^ {t} ^ {\mathrm{MP}} \\ = \sum_ {t} \left(\lambda_ {e, i} ^ {t} - a _ {e, i, f} - \frac {1}{2} b _ {e, i, f} q _ {e, i, f} ^ {t}\right) \times q _ {e, i, f} ^ {t} \end{array}\tag{21}
$$

Making use of the results of the market-clearing problem (2)–(8), the supplier problem can be represented as a mathematical program with equilibrium constraints [14]

$$
\text { Max } \quad \Pi_ {i, f}\tag{22}
$$

subject to

$$
\text { constraints } [ (9) - (1 6) ]\tag{23}
$$

where $\varPi _ { i , f }$ in (22) is given either by (20) or (21). The impacts of the ISO's and the rivals' actions are observed through constraints in (23).

## 3.4. Complete information gaming

In a complete information game, the payoff of each player is commonly known to all players. To compute NE through utilizing game theory concept, it is useful to state the above problem as an n player game: There are n players in the game that simultaneously play with their own bidding strategies. Each player knows its opponents' payoff functions and attempts to maximize its own payoff by acknowledging the opponents' bidding strategies. A Nash equilibrium will occur when no player has the incentive to unilaterally change its bidding strategy. More formally, a strategy profile $( { \alpha _ { i , f } ^ { t } } ^ { * } , { \alpha _ { i , - f } ^ { t } } ^ { * } )$ such that $\Pi _ { i , f } ( { \alpha ^ { t } } _ { i , f } { ^ * } , { \alpha ^ { t } } _ { i , - f } { ^ * } ) \geq \Pi _ { i , f } ( \bar { \alpha } _ { i , f } ^ { t } , { \alpha ^ { t } } _ { i , - f } ) \ \forall { \alpha ^ { t } } _ { i , f } { ^ * } \neq \alpha _ { i , f } ^ { t } .$

A common approach, used in power market context (see, e.g., [28,6,25]), for solving game problems is to presume a set of initial strategies and then iteratively calculate each player's reaction assuming the opponents' reactions remain fixed. An equilibrium state is found when no player can increase its payoff, given its opponents' reactions. In this paper, the following procedure is used to find a NE:

Step 1) Choose an initial guess for the vector of bidding strategy $\boldsymbol { \alpha } _ { i , - f } ^ { t }$ Marginal bids would be an appropriate choice at initialization.

Step 2) Solve the supplier problem (22)–(23), taking the rivals' bidding strategies as given.

Step 3) Use the results of step 2 to update the bidding strategy of supplier f, $\alpha _ { e , i , f } ^ { t }$

Step 4) Reiterate steps 1–3 to find the optimal bidding strategy of each supplier.

Step 5) Stop if Max $\smash { \{ \vert T _ { i , f } ^ { \mathrm { { n e w } } } - T _ { i , f } ^ { \mathrm { { o l d } } } \vert _ { G i , f } \} }$ is below some tolerance or a maximum number of iterations has been reached; otherwise go back to step 2.

Using this procedure, each supplier can determine its optimal bidding strategy, knowing the strategies of the rest of the suppliers and assuming they remain unchanged. This process is reiterated until suppliers stop changing their bidding strategies or a maximum number of iterations has been reached.

As pointed out in literature, in a game there can be none, single, or multiple equilibria [13]. The iterative procedure above will not converge if there is no Nash point. Whenever, the found NE of the game problem can be proved to be unique, the corresponding bidding strategies are indeed optimal. The existence and uniqueness properties of NE have been examined in [29] with supply capacity limits. References [28,4,8,31] explore the role of the transmission constrains in the outcome of the oligopolistic competition. A method for finding multiple market equilibria is proposed in [8] which can reduce the number of search regions to be tested for equilibria.

Given a NE for the game problem above, the payoff of supplier f is calculated by

$$
\Pi_ {i, f} ^ {*} = \Pi_ {i, f} \left(\alpha_ {e, i, f} ^ {t} ^ {*}, q _ {e, i, f} ^ {t} ^ {*}\right)\tag{24}
$$

where $\varPi _ { i , f }$ is given by (20) and (21) in each pricing scheme.

## 3.5. Unconstrained game analysis under PABP and MP

To facilitate finding an analytic solution in closedform expression, let us consider a transmission-unconstrained case and further assume that no supplier is restricted by its capacity limit. Under common loading scenarios, the optimal bidding strategy of individual suppliers can be obtained under PABP and MP mechanisms. Under these conditions, constraints (9)–(11) and (13) are not binding and from (12) and (15) it follows that

$$
- \lambda_ {e, i} ^ {t} + \alpha_ {e, i, f} ^ {t} + b _ {e, i, f} q _ {e, i, f} ^ {t} = 0 \quad \forall i, f\tag{25}
$$

$$
\sum_ {i, f} q _ {e, i, f} ^ {t} = \sum_ {i} q _ {d, i} ^ {t} = Q _ {D} ^ {t} \quad \forall i, f\tag{26}
$$

where $\mathcal { Q } _ { D } ^ { t }$ in $\operatorname { E q . }$ (26) represents total demand. Solving (25)–(26) for $\lambda _ { e , i } ^ { t }$ and $q _ { e , i , f } ^ { t }$ and rearranging yields

$$
\lambda_ {e, i} ^ {t} = \frac {1}{\sum_ {i , h} \frac {1}{b _ {e , i , h}}} \left(Q _ {D} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t}}{b _ {e , i , h}}\right)\tag{27}
$$

$$
q _ {e, i, f} ^ {t} = \frac {1}{b _ {e , i , f} \sum_ {i , h} \frac {1}{b _ {e , i , h}}} \left(Q _ {D} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} - \alpha_ {e , i , f} ^ {t}}{b _ {e , i , h}}\right).\tag{28}
$$

At Nash equilibrium, all suppliers are playing their optimum strategies. Given the bids of the rest of the suppliers, the optimum bidding strategy of supplier f that maximizes the profit can be expressed as (see Appendix for details)

$$
\alpha_ {e, i, f} ^ {t} \text {PABP} = \frac {Q _ {D} ^ {t} + \sum_ {i , h \neq f} \frac {\alpha_ {e , i , h} ^ {t}}{b _ {e , i , h}} + a _ {e , i , f} b _ {e , i , f} \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}} \sum_ {i , h} \frac {1}{b _ {e , i , h}}}{\left(1 + b _ {e , i , f} \sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}}}\tag{29}
$$

$$
\alpha_ {e, i, f} ^ {t} \text {MP} = \frac {Q _ {D} ^ {t} + \sum_ {i , h \neq f} \frac {\alpha_ {e , i , h} ^ {t}}{b _ {e , i , h}} ^ {\mathrm{MP}} + a _ {e , i , f} b _ {e , i , f} \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}} \sum_ {i , h} \frac {1}{b _ {e , i , h}}}{\left(1 + b _ {e , i , f} \sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}}}\tag{30}
$$

where (29) and (30) represent the expressions under PABP and MP mechanisms, respectively. The maximum profit can be obtained using Eqs. (27)–(30). Substituting $\dot { \alpha } _ { e , i , f } ^ { t } \ / { } ^ { P A B P }$ and $q _ { e , i , f } ^ { t }$ in payoff function (20), gives the maximum profit of supplier f under PABP as

$$
\begin{array}{l} \Pi_ {i, f} ^ {t} ^ {\text {Max - PABP}} = \frac {1}{2 b _ {e , i , f} \left(\sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) ^ {2}} \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} ^ {\text {PABP}} - \alpha_ {e , i , f} ^ {t} ^ {\text {PABP}}}{b _ {e , i , h}}\right) \\ \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} ^ {\text {PABP}} + \alpha_ {e , i , f} ^ {t} ^ {\text {PABP}}}{b _ {e , i , h}} - 2 a _ {e, i, f} \sum_ {i, h} \frac {1}{b _ {e , i , h}}\right). \end{array}\tag{31}
$$

Likewise, substituting $\alpha _ { e , i , f } ^ { t } , \lambda _ { e , i } ^ { t }$ , and $q _ { e , i , f } ^ { t }$ in payoff function (21), yields the maximum profit of supplier f under MP as

$$
\begin{array}{l} \Pi_ {i, f} ^ {t} ^ {\text { Max - MP }} = \frac {1}{2 b _ {e , i , f} \left(\sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) ^ {2}} \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\mathrm{MP}} - \alpha_ {e , i , f} ^ {t} {} ^ {\mathrm{MP}}}{b _ {e , i , h}}\right) \\ \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\mathrm{MP}} + \alpha_ {e , i , f} ^ {t} {} ^ {\mathrm{MP}}}{b _ {e , i , h}} - 2 a _ {e, i, f} \sum_ {i, h} \frac {1}{b _ {e , i , h}}\right) \end{array}\tag{32}
$$

Since the total demand is inelastic and known with certainty to all suppliers, total suppliers' production is the same under PABP and MP. Furthermore, as the same market clearing rule (namely, an OPF program) is used under both pricing mechanisms, the differences between PABP and MP can be characterized through comparing the market results as described next.

Lemma 1. In a single generator game, the optimal bidding strategies of any individual supplier holding a single generator are the same under PABP and MP mechanisms.

Proof. Assuming an initial set of bidding strategies for all suppliers other than supplier $f ,$ we can state the following expression by means of (30) and (31)

$$
\alpha_ {e, i, f} ^ {t} \text {PABP} - \alpha_ {e, i, f} ^ {t} \text {MP} = \frac {\sum_ {i , h \neq f} \frac {\alpha_ {e , i , f} ^ {t} \text {PABP} - \alpha_ {e , i , f} ^ {t} \text {MP}}{b _ {e , i , h}}}{\left(1 + b _ {e , i , f} \sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}}} = 0\tag{33}
$$

where the right hand side of Eq. (33) is obtained by observing that $\alpha _ { e , i , h } ^ { t } \mathrm { { ^ { \tiny ~ M P } = } } \alpha _ { e , i , h } ^ { t } \mathrm { { ^ { \tiny ~ P A B P } } }$ , h ≠f. Hence, Eqs. (30) and (31) represent identical optimal bidding strategies under PABP and MP schemes and the lemma is proved. □

Lemma 2. In a single generator game, the maximum profits of any individual supplier holding a single generator are the same under PABP and MP mechanisms.

Proof. Lemma 1 implies that $\alpha _ { e , i , f } ^ { t } { } ^ { P A B P } = \alpha _ { e , i , f } ^ { t } { } ^ { M P } .$ It is also seen from Eq. (28) that under MP scheme $q _ { e , i , f } ^ { t }$ is identical with that under PABP scheme. Consequently, it follows from Eqs. (31) and (32) that the maximum profit of supplier f under PABP is equal to the profit under MP and the lemma is proved. □

Lemma 3. In a single generator game and under common loading conditions, the market clearing price under PABP mechanism is equal to the market clearing price under MP mechanism.

Proof. This Lemma comes as a result of Lemma 1 since it is evident from Lemma 1 that $\alpha _ { e , i , f } ^ { t } { } ^ { P A B P } = \alpha _ { e , i , f } ^ { t } { } ^ { M P } .$ It is also seen from Eq. (27) that PABP and MP mechanisms lead to the same market clearing price $\lambda _ { e , i } ^ { t }$ and the lemma is proved. □

The above discussion was confined to a single generator game. If a supplier owns more than one generator, the conclusions presented for a single generator game can be generalized to a multigenerator game as follows.

Let us denote by $K _ { P }$ the number of the generators that are under the control of supplier P. It is shown in

Appendix that the optimal bidding strategy of generator f (regulated by supplier P) under PABP becomes

$$
\begin{array}{l} \alpha_ {e, i, f} ^ {t} ^ {\text {PABP - Mg}} = \frac {1}{\sum_ {i , h} \frac {1}{b _ {e , i , h}} \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}} + \sum_ {i , k \notin \{1 , . . . , K _ {P} \}} \frac {1}{b _ {e , i , f} b _ {e , i , k}}} \\ \times \left[ \left(Q _ {D} ^ {t} + \sum_ {i, h \neq f} \frac {\alpha_ {e , i , h} ^ {t} ^ {\text {PABP - Mg}}}{b _ {e , i , h}}\right) \right. \\ \times \sum_ {i, k \in \{1,.., K _ {P} \}} \frac {1}{b _ {e , i , k}} + \left(\sum_ {i, h \neq f} \frac {a _ {e , i , f}}{b _ {e , i , h}} \right. \\ \left. - \sum_ {i, k \in \{1,.., K _ {P} \}, k \neq i} \frac {a _ {e , i , k}}{b _ {e , i , k}}\right) \sum_ {i, h} \frac {1}{b _ {e , i , h}} \Bigg ] \end{array}\tag{34}
$$

Similarly, we can state the following expression for the optimal bidding strategy of generator f under MP

$$
\begin{array}{l} \alpha_ {e, i, f} ^ {t} ^ {\mathrm{MP-Mg}} = \frac {1}{\sum_ {i , h} \frac {1}{b _ {e , i , h}} \sum_ {i , h \neq f} \frac {1}{b _ {e , i , h}} + \sum_ {i , k \notin \{1 , . . . , K _ {P} \}} \frac {1}{b _ {e , i , f} b _ {e , i , k}}} \\ \times \left[ \left(Q _ {D} ^ {t} + \sum_ {i, h \neq f} \frac {\alpha_ {e , i , h} ^ {t} ^ {\mathrm{MP-Mg}}}{b _ {e , i , h}}\right) \right. \\ \times \sum_ {i, k \in \{1,.., K _ {P} \}} \frac {1}{b _ {e , i , k}} + \left(\sum_ {i, h \neq f} \frac {a _ {e , i , f}}{b _ {e , i , h}} \right. \\ - \left. \sum_ {i, k \in \{1,.., K _ {P} \}, k \neq i} \frac {a _ {e , i , k}}{b _ {e , i , k}}\right) \sum_ {i, h} \frac {1}{b _ {e , i , h}} \Bigg ] \end{array}\tag{35}
$$

The maximum profit of generator f can be obtained by substituting $\boldsymbol { \alpha } _ { e , i , f } ^ { t }$ (Eqs. (34), (35)), $\lambda _ { e , i } ^ { t }$ (Eq. (27)), and $q _ { e , i , f } ^ { t } ( \mathrm { E q . } ( 2 8 ) )$ into the corresponding payoff function under each pricing mechanism (see Appendix for details). In the following lemmas, comparative statements are made between PABP and MP for a multigenerator game.

Lemma 4. In a multigenerator game, the optimal bidding strategies of each individual generator (player) belonging to a given supplier are the same under PABP and MP mechanisms.

Proof. This lemma can be proved in the same way outlined in Lemma 1. □

Lemma 5. In a multigenerator game, the maximum profits of each individual generator (player) belonging to a given supplier are the same under PABP and MP mechanisms.

Proof. To prove this lemma, it should be noticed that the profit of a given supplier holding more than one generator is the sum of the individual profits made by each. Lemma 5 implies that $\alpha _ { e , i , f } ^ { t } { } ^ { P A B P - M g } = \stackrel { \cdot } { \alpha } _ { e , i , f } ^ { t } M P - M g$ . Hence, this lemma is proved in the same way as lemma 2. □

Lemma 6. In a multigenerator game and under similar loading conditions, the market clearing price under PABP mechanism is equal to the market clearing price under MP mechanism.

Proof. Lemmas 4 and 5 imply that the optimal bidding strategies are the same under PABP and MP. Therefore, for common loading conditions the market clearing price, given by Eq. (27), is the same under PABP and MP and the lemma is proved. □

Lemmas above imply that the market settlement rule does not affect the optimal bidding strategy and the maximum payoff of a strategic supplier, as long as the supplier chooses to manipulate the sole intercept of the supply function and furthermore, the problem constraints are ignored. In addition, the market clearing price remains unchanged if the pricing mechanism changes. The results obtained in this section hold for both single generator and multigenerator game scenarios under imperfect competition. References [21,22] analyze the market performance under perfect competition and demonstrate that the expected profits of the suppliers are equal under PABP and MP mechanisms.

The analysis presented in this section was restricted to a transmission-unconstrained case excluding supply capacity limits. Since comparative statements between PABP and MP under constrained situations can not be made without extensive market simulations, in the following section the impact of transmission and supply capacity limits on the market results are explored. Moreover, through the methodology introduced in [10], the suppliers' risk profiles are created and compared under both pricing mechanisms.

## 3.6. Loss and profit calculation

Let us consider a multiperiod market consisting of a day-ahead hourly market and a real-time (spot) market. Suppliers offer profit-maximizing bids to the day-ahead market according to the method outlined in the preceding section. Given the equilibrium state of the dayahead market, the individual profits can be calculated based on the market pricing scheme. After all offers are made and the winning suppliers are identified in the dayahead market, a supplier may confront financial losses if it faces random outages in real-time. If this happens, the supplier must purchase the replacement energy from the real-time market to fulfill its commitment. Whenever, the real-time price is higher than the day-ahead price, the supplier incures a loss. Expected value of this loss (or, profit if the opposite occurs) can be calculated by simulating the market over a given time horizon. This provides a cumulative probability distribution of the expected loss/profit known as risk profile [10].

The abovementioned risk profile can be created under each pricing mechanism. Under PABP mechanism, the expected loss of supplier f whenever it experiences a random outage at time period t is calculated as

$$
E \left(\text { loss } _ {i, f} ^ {t} \text { PABP }\right) = \left(\alpha_ {e, i, f} ^ {t} + b _ {e, i, f} q _ {e, i, f} ^ {t} - \lambda_ {e, i} ^ {t} \text { sp }\right) \times q _ {e, i, f} ^ {t} \times f p _ {i, f}\tag{36}
$$

where $\lambda _ { e , i } ^ { t } \mathrm { } ^ { s p }$ is the nodal energy price in the spot market. Likewise, the expected loss under MP mechanism becomes

$$
E \Big (\mathrm{loss} _ {i, f} ^ {t} \mathrm{^MP} \Big) = \Big (\lambda_ {e, i} ^ {t} - \lambda_ {e, i} ^ {t} \mathrm{^sp} \Big) \times q _ {e, i, f} ^ {t} \times f p _ {i, f}.\tag{37}
$$

The expected profit during commitment hours is given by

$$
E \left(\Pi_ {i, f} ^ {t}\right) = \Pi_ {i, f} ^ {t} \times \left(1 - f p _ {i, f}\right)\tag{38}
$$

where $\smash { \prod _ { i , f } ^ { t } }$ was defined in section III-C for each pricing scheme. The hourly expected loss/profit calculation is carried out for each supplier over the time horizon. To identify whether a supplier fails at a given hour or not, a uniformly distributed random number on range (0,1) is generated. The supplier fails if $1 - f p _ { i , f }$ is less than the random number and the expected loss is computed either by (36) or (37). Otherwise, (38) is used to calculate the expected profit at that hour [10].

![](/api/attachments/G2KKMGJR/fulltext/images/3c0cfe00e6d557d1dbf8c0752d91770b739a4f69e2b10194a482426420c9cbcd.jpg)  
Fig. 1. Six-bus test system.

Table 1  
Generator and demand data

<table><tr><td>Node $i$ </td><td>Supplier $F$ </td><td> $b_{e,i,f}$  $(\$/MW^{2}h)$ </td><td> $a_{e,i,f}$  $(\$/MWh)$ </td><td> $\overline{q}_{e,i,f}$ (MW)</td><td> $ru_{i,f}$ (MW/h)</td><td> $rd_{i,f}$ (MW/h)</td><td> $fp_{i,f}$ (%)</td><td> $q_{d,i}$ (MW)</td></tr><tr><td>1</td><td>1</td><td>0.08</td><td>10</td><td>700</td><td>100</td><td>100</td><td>10</td><td>155</td></tr><tr><td>2</td><td>2</td><td>0.10</td><td>15</td><td>600</td><td>100</td><td>100</td><td>15</td><td>258</td></tr><tr><td>3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>104</td></tr><tr><td>4</td><td>3</td><td>0.12</td><td>20</td><td>600</td><td>100</td><td>100</td><td>10</td><td>153</td></tr><tr><td>5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>361</td></tr><tr><td>6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>255</td></tr></table>

To simulate the spot price, $\lambda _ { e , i } ^ { t } \overset { s p }  $ is supposed to reside within range $[ 1 - \varepsilon , 1 + \varepsilon ] \times \lambda _ { e , i } ^ { t }$ in off-peak periods and within $[ 1 , 1 + \kappa ] \times \lambda _ { e , i } ^ { t }$ during peak periods. This ensures $\lambda _ { e , i } ^ { t } \mathrm { } ^ { s p }$ to be greater than $\lambda _ { e , i } ^ { t }$ in peak periods while can be less than $\lambda _ { e , i } ^ { t }$ in off-peak periods. ε and κ are two random numbers exhibiting equiprobable values over (0,0.10) and (0,0.50), respectively. To represent the spot price more realistically, several price spikes are generated and accounted for in $\lambda _ { e , i } ^ { t } \lambda _ { } ^ { s p }$ by making the use of the Frechet distribution [5].

A multiperiod market based on a six-bus test system is used to illustrate the effects of physical constraints on the market outcomes under PABP and MP. The time horizon is assumed to be composed of 365 days with each day of 10 hours. Nodal demands follow a common yearly loadprofile comprising daily, weekly, and seasonal variations [23]. The market is then solved for each day of the year using the method outlined in section III. Given a NE of the game, the supplier risk profiles are then created under PABP and MP based on the procedure introduced in III-F.

![](/api/attachments/G2KKMGJR/fulltext/images/dc0bcc01170c53d445c064defb30bd83e6c37c7bb4f1ae67d7ab937d92322097.jpg)  
Fig. 2. Risk profile of generator 3: single generator game.

## 4. Simulations

The test system depicted in Fig. 1 has been adopted from [2] with some modifications. In Fig. 1, generation and demand are denoted by $G _ { i , f }$ and $q _ { d , i } ,$ respectively. The relevant system data is tabulated in Table 1. All transmission lines have zero resistances and equal reactances. Transmission limits for lines connecting nodes 1 and 6 (referred to as line 1) as well as nodes 2 and 5 (referred to as line 2) are both set to 220 MW. Other lines have large enough transmission capacities. Nodal demand variations comply with the yearly loadprofile presented in [31]. The yearly peak demand occurs in week 51 with the nodal values shown in Table 1.

Two cases, termed as A and B, are studied and analyzed. In Case A, a single generator game is simulated where individual suppliers derive optimal profit-maximizing bidding strategies using the method introduced in section III. A multigenerator game is considered in Case B where some players join together and form a single player. Suppliers' risk profiles are created and compared in cases A and B as described next.

Case A. Single generator Game Including Constraints: Each supplier acts individually in this case and submits profit-maximizing bids to the energy market. A flow limit of 220 MW is imposed on Line 1 and Line 2. Ramp rate limits are set to 100 MW/h for each supplier together with the capacity limits as tabulated in Table 1. Typical results for $G _ { 4 , 3 }$ are shown in Fig. 2. This figure illustrates the cumulative probability distribution versus the expected value of loss and profit (referred to as risk profile) under PABP and MP. It is seen from Fig. 2 that beyond a given probability, PABP mechanism gives greater expected profits than MP, however, in the vertical part of the curve, the expected profits are almost equal under PABP and MP. This is due to the fact that in light load conditions, no transmission constraints are violated and suppliers operate within their capacity limits. As implied by lemmas 1–3, the supplier profit and hence, the risk profiles, as well as the market price will be the same under PABP and MP mechanisms.

![](/api/attachments/G2KKMGJR/fulltext/images/da48090f319a1eb3093b642e5b3d9cc99f7edb3aa27818b9746c637a2db6c276.jpg)  
Fig. 3. Risk profile of generator 3: multigenerator game.

Case B. Multigenerator Game Including Constraints: A multigenerator game is considered in this case study. Let us suppose that player 2 (owner of $G _ { 2 , 2 } )$ and player 3 (owner of $G _ { 4 , 3 } )$ have joined together and constituted a single player. A two-player game is thus formed where $G _ { I , I }$ is regulated by player 1 and the remaining two generators remain under the control of player 2. Player 2 attempts to maximize the sum of the individual profits made by $G _ { 2 , 2 }$ and $G _ { 4 , 3 } .$ . Other assumptions are the same as in Case A. Typical results are shown in Fig. 3 for $G _ { 4 , 3 }$ Compared to Case A, for some probability levels, the expected profit is higher under MP. This happens because the price increase under MP (in the multigenerator case) can dominate the bid increase in high loading conditions leading to greater profits in these periods.

Further insights can be gained through comparing the market results in Case B with those in Case A. Comparable results for single generator and multigenerator games are shown in Figs. 4 and 5 for $G _ { 2 , 2 }$ . It can be observed from these plots that the multigenerator game provides higher expected loss and profits under both pricing mechanisms (this result remains valid for the remaining two suppliers not shown here). This conclusion is supported by intuition since higher prices and profits are expected as the market moves towards an oligopoly.

![](/api/attachments/G2KKMGJR/fulltext/images/aaaf8a3c2823e4451c49267f0255a8843b7dfbee81176882745f67f082da2dd9.jpg)  
Fig. 4. Risk profile of generator 2 under PABP: single generator game vs. multigenerator game.

![](/api/attachments/G2KKMGJR/fulltext/images/154a59199c264f3994995bb6c31ee6ddbeb5f47a94b467dd8fd202345d8d4053.jpg)  
Fig. 5. Risk profile of generator 2 under MP: single generator game vs. multigenerator game.

## 5. Conclusion

Supply Function Equilibria under PABP and MP mechanisms were analyzed theoretically and through numerical results. Using a parameterized SFE approach which involves manipulation of the sole intercept, it was demonstrated that the optimal bidding strategy and the maximum profit of a strategic supplier, as well as the marker clearing price are the same under PABP and MP mechanisms provided the constraints are ignored. Through market simulations, the effects of transmission constraints as well as the supply capacity limits on the market outcomes were examined. It was shown that when the constraints are introduced, the profit a supplier can achieve is contingent not only upon its location in the system but also on the market settlement rule.

Comparable results for multigenerator and single generator games were provided as well illustrating that the multigenerator game yields higher nodal price and supplier's profit under both PABP and MP mechanisms.

## Appendix A

## A.1. Optimal bidding strategy derivations

Chouchman et al. [7] consider a pay-as-bid pricing scheme and develop profit-maximizing bids for a strategic player under unconstrained situations. In the following, we will derive somewhat different expressions for optimal bidding strategy under both PABP and MP.

Let us consider the unconstrained game outlined in section III-E. Under PABP, the supplier problem (22)– (23) is simplified to

$$
\underset {\alpha_ {e, i, f} ^ {t}} {\text { Max }} \Pi_ {i, f} ^ {t} ^ {\text { PABP }} = \left(\alpha_ {e, i, f} ^ {t} - a _ {e, i, f} + \frac {1}{2} b _ {e, i, f} q _ {e, i, f} ^ {t}\right) \times q _ {e, i, f} ^ {t}\tag{39}
$$

subject to

$$
- \lambda_ {e, i} ^ {t} + \alpha_ {e, i, f} ^ {t} + b _ {e, i, f} q _ {e, i, f} ^ {t} = 0 \quad i = 1... n, f = 1... N _ {G}\tag{40}
$$

$$
\sum_ {i, f} q _ {e, i, f} ^ {t} = \sum_ {i} q _ {d, i} ^ {t} = Q _ {D} ^ {t} \quad i = 1... n, f = 1... N _ {G}.\tag{41}
$$

Eqs. (40) and (41) were used in section III-E to derive Eq. (28)) for the dispatched quantity $q _ { e , i , f } ^ { t }$ Substituting $q _ { e , i , f } ^ { t }$ in (39) and rearranging yields

$$
\begin{array}{l} \text {Max} _ {\alpha_ {e, i, f} ^ {t}} \Pi_ {i, f} ^ {t} ^ {\text {PABP}} = \frac {1}{2 b _ {e , i , f} \left(\sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) ^ {2}} \\ \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\text {PABP}} - \alpha_ {e , i , f} ^ {t} {} ^ {\text {PABP}}}{b _ {e , i , h}}\right) \\ \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\text {PABP}} + \alpha_ {e , i , f} ^ {t} {} ^ {\text {PABP}}}{b _ {e , i , h}} \right. \\ \left. - 2 a _ {e, i, f} \sum_ {i, h} \frac {1}{b _ {e , i , h}}\right) \end{array}\tag{42}
$$

Similarly, using payoff function (21) and substituting for $\lambda _ { e , i } ^ { t }$ and $q _ { e , i , f } ^ { t }$ (given respectively by (27) and (28)), the optimization problem (39)–(41) under MP becomes

$$
\begin{array}{l} \underset {\alpha_ {e, i, f} ^ {t}} {\text {Max}} \Pi_ {i, f} ^ {t} ^ {\text {MP}} = \frac {1}{2 b _ {e , i , f} \left(\sum_ {i , h} \frac {1}{b _ {e , i , h}}\right) ^ {2}} \\ \qquad \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\text {MP}} - \alpha_ {e , i , f} ^ {t} {} ^ {\text {MP}}}{b _ {e , i , h}}\right) \\ \qquad \times \left(\sum_ {i} q _ {d, i} ^ {t} + \sum_ {i, h} \frac {\alpha_ {e , i , h} ^ {t} {} ^ {\text {MP}} + \alpha_ {e , i , f} ^ {t} {} ^ {\text {MP}}}{b _ {e , i , h}} \right. \\ \qquad \left. - 2 a _ {e, i, f} \sum_ {i, h} \frac {1}{b _ {e , i , h}}\right) \end{array}\tag{43}
$$

The first partial derivatives with respect to $\boldsymbol { \alpha } _ { e , i , f } ^ { t }$ give Eqs. (29) and (30) under PABP and MP, respectively (see section III-E). Since payoff functions (41) and (42) are concave and quadratic w.r.t $\boldsymbol { \alpha } _ { e , i , f } ^ { t }$ the sufficiency conditions for maximum are satisfied and (29)–(30) represent the optimal bidding strategies.

The expressions obtained above can be extended to a multigenerator game where a supplier can hold more than one generator. Let us denote by $K _ { P }$ the number of the generators that player Ρ controls. The profit of this player is the sum of the individual profits made by each generator. Under PABP mechanism, the optimization problem (39)–(41) can be expressed as

$$
\underset {\alpha_ {e, i, h} ^ {t}} {\text { Max }} \Pi_ {P} ^ {t} ^ {\text { PABP }} = \sum_ {i, h} \Pi_ {i, h} ^ {t} ^ {\text { PABP }}, \quad h = 1, 2, \dots , K _ {P}\tag{44}
$$

subject to

constraints 40   41

45

where $\boldsymbol { \Pi } _ { i , h } ^ { t _ { 1 } , \mathrm { \tiny ~ { P A B P } } }$ represents the profit of generator h at node i, given by Eq. (20) (see section III-C).

Likewise, under MP mechanism we get

$$
\underset {\alpha_ {e, i, h} ^ {t}} {\text { Max }} \Pi_ {P} ^ {t \text { MP }} = \sum_ {i, h} \Pi_ {i, h} ^ {t \text { MP }}, \quad h = 1, 2,... K _ {P}\tag{46}
$$

subject to

constraints 40     41

47

where $\boldsymbol { \mathit { I I } } _ { i , h } ^ { t } \mathrm { { ^ M P } }$ represents the profit of generator h at node i, given by Eq. (21) (see section III-C). Following the same procedure as in the single generator case (i.e., substituting for $\alpha _ { e , i , f } ^ { t } \lambda _ { e , i } ^ { t }$ and $q _ { e , i , f } ^ { t }$ in (44) and (46), and applying the first-order optimality conditions), we get the optimal bidding strategies (34) and (35) under PABP and MP, respectively. Since payoff functions (44) and (46) are concave, the sufficiency conditions for maximum hold and (34) and (35) give the optimal bidding strategies for player f.

## References

[1] R. Baldick, Electricity market equilibrium models: the effects of parameterization, IEEE Transactions on Power Systems 17 (4) (Feb. 2002) 1170–1176.

[2] G. Bautista, V.H. Quintana, J.A. Aguado, An oligopolistic model of an integrated market for energy and spinning reserve, IEEE Transactions on Power Systems 21 (1) (Feb. 2006) 132–142.

[3] C.A. Berry, B.F. Hobbs, W.A. Meroney, Understanding how market power can arise in market competition: a game theoretic approach, Utilities Policy 8 (1999) 139–158.

[4] E. Bompard, W. Lu, R. Napoli, Network constraint impacts on the competitive electricity markets under supply-side strategic bidding, IEEE Transactions on Power Systems 21 (7) (Feb. 2006) 160–170.

[5] K. Bury, Statistical Distributions in Engineering, Cambridge University press, 1999.

[6] J. Cardel, C.C. Hitt, W.W. Hogan, Market power and strategic interaction in electricity networks, Research and Energy Economics 19 (1-2) (1997) 109–137.

[7] P. Chouchman, B. Kouvaritakis, M. Cannon, F. Prashad, Gaming strategy for electric power with random demand, IEEE Transactions on Power Systems 20 (3) (Aug. 2005) 1283–1292.

[8] P.F. Correia, T.J. Overbye, I.A. Hiskens, Searching for noncooperative equilibria in centralized electricity markets, IEEE Transactions on Power Systems 18 (4) (Nov. 2003) 1417–1424.

[9] P. Cramton, Alternative pricing rules, Proceeding of Power System Conference and Exposition, New York, Oct. 2004.

[10] D. Das, F. Wollenberg, Risk assessment of generators bidding in day-ahead markets, IEEE Transactions on Power Systems 20 (1) (Feb. 2005) 416–424.

[11] N. Fabra, Tacit collusion in repeated auctions: uniform versus discriminatory, Journal of Industrial Economics 51 (3) (2003) 271–293.

[12] G. Federico, D. Rahman, Bidding in an electricity pay-as-bid auction, Journal of Regulatory Economics 24 (2) (2003) 157–211.

[13] D. Fundenburg, J. Tirol, Game Theory, 5th ed, Cambridge, MA: MIT Press, 1996.

[14] B.F. Hobbs, C.B. Metzler, J.-S. Pang, Strategic gaming analysis for electric power systems: an MPEC Approach, IEEE Transactions on Power Systems 15 (2) (May 2000) 638–645.

[15] P. Holmberg, Comparing Supply Function Equilibria of Pay-as-Bid and Uniform-Price Auctions, vol. 17, Uppsala University, May 2005, Working Paper.

[16] A. Kahn, P.C. Cramton, R.H. Porter, R.D. Tabors, Uniform pricing or pay-as-bid pricing: a dilemma for California and beyond, The Electricity Journal 14 (6) (2001) 70–79.

[17] P. Klemperer, Auction theory: a guide to the literature, Journal of Economic Surveys 13 (3) (July 1999) 227–286.

[18] A. Minoia, D. Ernst, M. Dicorato, M. Trovato, M. Ilic, Reference transmission network: a game theory approach, IEEE Transactions on Power Systems 21 (1) (Feb. 2006) 249–259.

[19] T. Mount, Market power and price volatility in restructured markets for electricity, Decision Support Systems 30 (2001) 311–325.

[20] S. Oren, When is a pay-as bid preferable to uniform price in electricity markets, Proceeding of Power System Conference and Exposition, New York, Oct. 2004.

[21] Y. Ren, F. Galiana, Pay-as-bid versus marginal pricing-part I: strategic generator offers, IEEE Transactions on Power Systems 19 (4) (Nov. 2004) 1771–1776.

[22] Y. Ren, F. Galiana, Pay-as-bid versus marginal pricing-part II: market behavior under strategic generator offers, IEEE Transactions on Power Systems 19 (4) (Nov. 2004) 1777–1783.

[23] Reliability Test System (RTS) Load Data, Version 1996, [Online]. Available: http://www.ee.washington.edu/research/ pstca/rts.

[24] A. Rudkevich, On the supply function equilibrium and its applications in electricity markets? Decision Support Systems 40 (2005) 409–425.

[25] S.D-L. Torre, A.J. Conejo, J. Contreras, Oligopolistic pool-based electricity markets: a multiperiod approach, IEEE Transactions on Power Systems 18 (4) (Nov. 2003) 1547–1555.

[26] S.D-L. Torre, J. Contreras, A.J. Conejo, Finding multiperiod nash equilibria in pool-based electricity markets, IEEE Transactions on Power Systems 19 (1) (Feb. 2004) 643–651.

[27] Y.S. Son, R. Baldick, K.H. Lee, S. Siddiqi, Short-term electricity market auction game analysis: uniform and pay-as-bid pricing, IEEE Transactions on Power Systems 19 (4) (Nov. 2004) 1990–1998.

[28] J.D. Weber, T.J. Overbye, A two-level optimization problem for analysis of market bidding strategies, Proc. IEEE PES Summer Meeting, vol. 2, Jul. 1999, pp. 682–687.

[29] J.D. Weber, T.J. Overbye, An individual welfare maximization algorithm for electricity markets, IEEE Transactions on Power Systems 17 (3) (Aug. 2002) 590–596.

[30] C. Wolfram, Electricity markets: should the rest of the world adopt the UK reforms? Regulation 22 (1999) 48–83.

[31] Z. Younes, M. Ilic, Generation strategies for gaming transmission constraints: will the deregulated electric power market be an oligopoly? Decision Support Systems 24 (1999) 207–222.

Hossein Haghighat received the B.Sc. degree in electrical engineering from Shiraz University, Shiraz, Iran, in 1999 and the M.Sc. and PhD degrees from Tarbiat Modares University, Tehran, in 2001 and 2007, respectively. He is currently a post doctoral fellow in the Department of ECE at the University of Waterloo, Waterloo, Canada. His research interests include power system operation and deregulation.

Hossein Seifi was born in Shiraz, Iran in 1957. He received his B.Sc. degree from Shiraz University in 1980, and his M.Sc. degree and Ph.D. both from UMIST (U.K.) in 1987 and 1989, respectively. From 1989, he is with Tarbiat Modares University, Tehran, Iran where he is currently a full professor. In 1995 he was with ABB Network Partner in Switzerland during sabbatical leave. He also acts as the chief advisor to the Iranian Ministry of Energy (Tavanir Co.) and the head of IPSERC. His research interests are de-regulation, operation and dynamics of power systems.

Ashkan R. Kian was born in Tehran, Iran, in 1970. He received his B.Sc. (with honors) in 1992 from Tehran University; M.S. and Ph.D. degrees in 1997 and 2001 respectively from Ohio State University all in Electrical Engineering. He was the Vice President of Engineering and Development at Genscape, Inc., Louisville, KY, from September 2001 to October 2002 and then a Research Associate at the School of Electrical and Computer Engineering, Cornell University, Ithaca, NY, from November 2002 to December 2003. Dr. Kian is currently an Assistant Professor of Electrical Engineering in the Control and Intelligent Processing Center of Excellence, University of Tehran. His research interests include bidding strategies in dynamic energy markets, game theory, stochastic optimal control, market monitoring, power systems operation, and control.
