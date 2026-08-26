---
otero_id: 12646
otero_key: "7RYTPRZN"
title: "An incentive-based mechanism for transmission asset investment"
authors: "Javier Contreras; George Gross; José Manuel Arroyo; José Ignacio Muñoz"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An incentive-based mechanism for transmission asset investment ☆

Javier Contreras <sup>a,</sup>⁎, George Gross <sup>b</sup>, José Manuel Arroyo <sup>a</sup>, José Ignacio Muñoz <sup>a</sup>

<sup>a</sup> Escuela Técnica Superior de Ingenieros Industriales, Universidad de Castilla — La Mancha, 13071 Ciudad Real, Spain

<sup>b</sup> Department of Electrical and Computer Engineering, University of Illinois at Urbana — Champaign, Urbana, IL 61801, USA

## a r t i c l e i n f o

Article history: Received 3 January 2008 Received in revised form 19 December 2008 Accepted 26 December 2008 Available online 8 January 2009

Keywords: Transmission planning Social welfare Investment incentives Cooperative game theory Shapley value

## a b s t r a c t

This paper presents an incentive scheme to encourage investment in the improvement and expansion of the transmission in the competitive electricity market environment. To create these incentives, a decentralized transmission asset investment model is proposed, where the new assets are built by the investors. The incentives are based on the value added to the social welfare through each asset investment. By viewing each potential investor as a player in a cooperative game the Shapley value is used to reward investors according to the added value that they create. The proposed methodology is applied to the Garver 6-bus system and the IEEE 24-bus Reliability Test System to illustrate the capability and <sup>fl</sup>exibility of the decision support system presented.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

The restructuring of the electricity industry has resulted in the advent of many new players, brokers, marketers, independent power producers and the creation of new structures, most notably the Independent System Operator (ISO) and the Regional Transmission Operator (RTO). The latter is also known with the generic term of Independent Grid Operator (IGO). The IGO is emblematic of the changes resulting from the separation of the ownership from the control and operation of the transmission network.

In the planning of new transmission asset additions, the objectives of market ef<sup>fi</sup>ciency improvement and social welfare maximization compete with those of pro<sup>fi</sup>t maximization of the individual players and investors. Typical situations requiring transmission asset investments stem from the need to ef<sup>fi</sup>ciently address congestion relief requirements by making the necessary improvements to the transmission network. Such investments impact each market player differently, some faring better and some worse as a result of the provided congestion relief.

Network expansion is by nature a very complex multi-period and multi-objective optimization problem [36]. Its nonlinear nature, the lumpiness of transmission resources and the inherent uncertainty of future developments constitute major complicating factors. Its solution is very dif<sup>fi</sup>cult, even under central decision making. In the vertically integrated structure, the construction of new transmission facilities is typically associated with the addition of new generating resources to facilitate their integration into the existing network. Given the strong control exerted by the state regulators over virtually every aspect of the regulated utility's activities, transmission planning must meet the requirements for regulatory approval. For transmission asset investments, the planning objectives are typically simpli<sup>fi</sup>ed to the minimization of total costs involved.

A wide range of techniques has been applied to investigate transmission planning. They include mathematical optimization methods such as linear programming [15,40], mixed-integer linear programming [1,34], Benders decomposition [2], and dynamic programming [13]; intelligent systems, such as genetic algorithms [14], simulated annealing [35]; and others, such as game theory models [8,9,41,42]. In the competitive electricity market environment, the solution of the transmission improvement/expansion problem requires some important modi<sup>fi</sup>cations, such as the introduction of a new objective function, e.g., social welfare maximization [10,38]. In addition, the problem requires the consideration of Financial Transmission Rights (FTR), market power, the analysis of merchant transmission investment, and the effect of lumpiness and imperfect competition. Such issues are investigated in [5,6,11,16,19,20,23,27,30,31,37].

The changes introduced and the consideration of the aforementioned issues are necessitated by the major changes emanating from the restructuring of the electricity industry. The open access regime entailed the breakup of the well entrenched vertically integrated structure in the electricity industry. As a result, centralized decision making has been replaced by decentralized decisions and the setting up of the new IGO structure has resulted in the separation of ownership from operational control. While the IGO has wide responsibilities for regional planning, including transmission, the implementation of the plans are in the hands of current transmission owners or new transmission investors. In this widely modi<sup>fi</sup>ed planning paradigm the transmission investments have, however, failed to keep up with the steadily increasing load demands and the ever more intense utilization of the grid by an increasing number of transmission customers [17]. One way to overcome this sorry picture in transmission investment is through the provision of appropriate incentives for expansion/improvement of the grid. Such schemes must take into account the physical constraints such as loop <sup>fl</sup>ow and lumpiness issues. Moreover, there are the additional complications arising from the competing objectives of the IGO to maximize societal bene<sup>fi</sup>ts with those of individual investors to maximize their expected pro<sup>fi</sup>ts.

Other than the lumpiness of transmission investments, lack of clarity in regulatory policy, lack of regional institutions and need for state approval are among the key reasons of transmission underinvestment. The sluggishness of transmission construction is because mismatches between those bene<sup>fi</sup>ting from the new facilities and those paying for them are often such as to ensure the new facilities do not get built. Effective procedures must be set up to ensure the timely recovery of transmission investments so that the expansion costs will be paid by those who bene<sup>fi</sup>t – the so-called participant funding approach – in order to have suf<sup>fi</sup>cient incentives to site new facilities.

Incentives formulated as reimbursement schemes are well known in the economics literature given to the seminal work of Vickrey [39] and the extensions to other economic problems [7,18]. These schemes are based on the notion that the remuneration should be a function of the difference in the social welfare with and without the added investment. In transmission planning, the formulation of investment incentives needs to pay careful attention to the network effects of the existing transmission grid and the extensive interactions among individual investments. As such, incentive mechanisms which reward those investors whose investments lead to increased total social welfare are appropriate under these schemes. The thrust of this paper is to explore the development of such incentive mechanisms for transmission asset investment.

New transmission assets can produce improvements in the network, such as congestion relief, that are bene<sup>fi</sup>cial to some or, even, all transmission customers. Cooperative game theory allows participants to jointly create added value and to receive a compensation based upon their contribution to the welfare of the system. There are several cooperative value allocation methods, such as the core [3,21], the nucleolus [21], and the Shapley value [21]. The latter entails the attractive attribute of uniqueness, which serves as a basis for sharing bene<sup>fi</sup>ts among all the investors.

This paper proposes an incentive mechanism design for transmission network investment where the problem is modeled as a cooperative game in order to allocate the new value created in the network expansion. In this game the players are investors in transmission assets and the Transmission Planner (TP) reimburses these investors by offering them all or part of the social welfare increase due to them. The investors receive these incentive offers and send their rate of return requirements to the TP. If their requirements are lower than the incentives, then they are invited to invest. The whole process is iterative until there are no more investors willing to build transmission assets.

The paper is structured as follows. Section 2 describes two formulations of the transmission investment problem: a centralized model and a decentralized model. In Section 3 an incentive scheme that rewards the investors in the decentralized model based on the expected increase in social welfare that they can provide is proposed. To calculate the amount of reward a cooperative transmission expansion game is de<sup>fi</sup>ned to allocate the gains obtained by the expansion among the investors using the Shapley value allocation method. Section 4 illustrates the application of the proposed incentive scheme to the Garver 6-bus system and the IEEE 24-bus Reliability Test System. The results provide a good example of effective incentive formulation for these systems. Conclusions with suggestions for future work are shown in Section 5. Appendix A compares the centralized and decentralized formulations showing their equivalence under several assumptions. Finally, Appendix B presents the necessary background on cooperative game theory.

## 2. Centralized and decentralized transmission investment formulations

The market-based transmission planning models presented in this section are related to the control level over the new investments that the TP has. The market is modeled as a pool-based system. The double auction pool-based market mechanism has the objective of maximizing the social welfare, so as to determine the maximum net bene<sup>fi</sup>ts for society, measuring the overall impacts of both sellers and buyers.

In the <sup>fi</sup>rst model presented, the TP invests in new transmission assets whose costs are publicly available. Although the generators and demands bid in the market, the investment in transmission is centrally planned.

The second model allows investors to build new transmission assets, provided that they want to recover their investments with a certain rate of return. In this case, the TP decides the amount of money given to the investors based on some measure of the overall improvement of the market: the social welfare.

The description of both models for transmission investment follows.

## 2.1. Transmission planning model with centralized transmission investment

Without loss of generality, a single seller and a single buyer at each node $n = 0 , 1 , \cdots , N$ of the network is assumed, where ${ \mathcal { L } } = \{ { \boldsymbol { \ell } } _ { 1 } , { \boldsymbol { \ell } } _ { 2 } , { \boldsymbol { \cdots } } _ { n }$ $\ell _ { L } \}$ <sup>L</sup>is the set of lines and transformers that connect the buses of the network and $\mathcal { L } ^ { \mathcal { C } } = \{ \ell _ { 1 } ^ { c } , \ell _ { 2 } ^ { c } , \dots , \ell _ { L ^ { c } } ^ { c } \}$ is the set of candidate lines and <sup>L</sup>transformers. The binary variable m<sup>c</sup> $( j = 1 , \cdots , L ^ { c } )$ models the presence of new transmission assets: it takes the value of 1 if the investment in transmission asset $\mathscr { l } _ { j } ^ { c } ( j = 1 , \cdots , L ^ { c } )$ is made, and 0 otherwise. The set $\boldsymbol { \kappa } ^ { c } = \{ k _ { 1 } ^ { c } , k _ { 2 } ^ { c } , \cdots , k _ { L } ^ { c } \}$ of investment costs in new transmission assets is de<sup>fi</sup>ned, where each individual cost of a new transmission asset $\ell _ { j } ^ { c }$ is expressed as $k _ { j } ^ { c } .$ . The node n selling entity's marginal offer in period t is integrated and denoted by $\beta _ { n , t } ^ { s } ( p _ { n , t } ^ { s } )$ , where $p _ { n , t } ^ { s }$ is the power injected at node n in period t. Similarly, the node n buying entity's marginal bid in period t is integrated and denoted by $\beta _ { n , t } ^ { b } ( p _ { n , t } ^ { b } )$ , where $p _ { n , t } ^ { b }$ is the power withdrawn at node n in period t. The $T P$ has a budget constraint, $B _ { c }$ , that takes into account the amount of monetary resources that can be used to construct new transmission assets.

The process to determine the successful bids/offers of the pool players per period is based on the maximization of the social welfare, as shown in [24,25]. The TP needs the information per period to maximize the aggregate social welfare (SW) minus the investment costs (IC) subject to the network constraints over a prede<sup>fi</sup>ned planning horizon $\mathcal { T } = \{ t { : } 1 , 2 , ~ \stackrel { . . . } { \ }  , ~ T \}$ , where t represents one period of the planning horizon. This optimization problem can be expressed as:

$$
\max (S W - I C) = \sum_ {t \in \mathcal {T}} \sum_ {n = 0} ^ {N} \left[ \beta_ {n, t} ^ {b} \left(p _ {n, t} ^ {b}\right) - \beta_ {n, t} ^ {s} \left(p _ {n, t} ^ {s}\right) \right] - \sum_ {j = 1} ^ {L ^ {c}} m _ {j} ^ {c} k _ {j} ^ {c}
$$

s:t:

1

$$
g _ {n, t} \left(p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {c}, \dots , m _ {L ^ {c}} ^ {c}\right)\tag{2}
$$

$$
= 0 \leftrightarrow \lambda_ {n, t}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}
$$

$$
\begin{array}{l} - f _ {i} ^ {m a x} \leq h _ {i, t} \left(p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {c}, \dots , m _ {L ^ {c}} ^ {c}\right) \\ \leq f _ {i} ^ {m a x} \leftrightarrow \left(\mu_ {i, t} ^ {m i n}, \mu_ {i, t} ^ {m a x}\right); \forall i = 1, 2, \dots , L; \forall t \in \mathcal {T} \end{array}\tag{3}
$$

$$
\begin{array}{l} - f _ {j} ^ {m a x} \leq h _ {j, t} \left(p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {c}, \dots , m _ {L ^ {c}} ^ {c}\right) \\ \leq f _ {j} ^ {m a x} \leftrightarrow \left(\mu_ {j, t} ^ {m i n}, \mu_ {j, t} ^ {m a x}\right); \forall j = 1, \dots , L ^ {c}; \forall t \in \mathcal {T} \end{array}\tag{4}
$$

$$
\sum_ {j = 1} ^ {L ^ {c}} m _ {j} ^ {c} k _ {j} ^ {c} \leq B _ {C}\tag{5}
$$

$$
m _ {j} ^ {c} \in \{0, 1 \}; \forall j = 1, \dots , L ^ {c}\tag{6}
$$

$$
0 \leq p _ {n, t} ^ {s} \leq p _ {n} ^ {s, m a x}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}\tag{7}
$$

$$
0 \leq p _ {n, t} ^ {b} \leq p _ {n} ^ {b, m a x}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}\tag{8}
$$

where $g _ { n , t } ( \bullet )$ is the nodal real power <sup>fl</sup>ow balance equation at node n in period $t , h _ { i , t } ( \bullet )$ is the expression of the real power <sup>fl</sup>ow in asset $\ell _ { i }$ in period t, and $h _ { j , t } ( \bullet )$ is the expression of the real power <sup>fl</sup>ow in candidate asset $\ell _ { j } ^ { c }$ in period t. Power <sup>fl</sup>ows are bounded by the capacities $f _ { i } ^ { \mathrm { m a x } }$ and $f _ { j } ^ { \mathrm { m a x } }$ . Likewise, the powers injected and withdrawn at node n in period t are limited by their maximum respective values $p _ { n } ^ { s , m a x }$ and $p _ { n } ^ { b , m a x } .$ . For every constraint set there is a corresponding set of dual variables: $\{ \lambda _ { n , t } \colon$ $\forall n = 0 , 1 , \cdots , N ; \forall t \in \mathcal { T } \}$ for the power <sup>fl</sup>ow balance equations, $\{ ( \mu _ { i , t } ^ { \mathrm { m i n } } ,$ $\mu _ { i , t } ^ { \operatorname* { m a x } } ) ; \forall i = 1 , 2 , \cdots , L ; \forall t \in T \} \mathrm { a n d } \{ ( \mu _ { j , t } ^ { \operatorname* { m i n } } , \mu _ { j , t } ^ { \operatorname* { m a x } } ) ; \forall j = 1 , 2 , \cdots , L ^ { c } ; \forall t \in T \}$ for <sup>T T</sup>the real power <sup>fl</sup>ows in existing and candidate assets, respectively. Note that if the assumption of having a dc power <sup>fl</sup>ow is made, expression (2)

![](/api/attachments/7RYTPRZN/fulltext/images/fc9c35219dadbea16e77762812db956f2ce84ac4ef2b0471d68aef9746a6435e.jpg)  
Fig. 1. Garver 6-bus system topology.

Garver 6-bus system: line data.

<table><tr><td>From</td><td>To</td><td>X (pu)</td><td>Line flow limit (MW)</td><td>Annualized cost (M$)</td><td>Already built</td></tr><tr><td>1</td><td>2</td><td>0.40</td><td>100</td><td>4.0</td><td>1</td></tr><tr><td>1</td><td>3</td><td>0.38</td><td>100</td><td>3.8</td><td>0</td></tr><tr><td>1</td><td>4</td><td>0.60</td><td>80</td><td>6.0</td><td>1</td></tr><tr><td>1</td><td>5</td><td>0.20</td><td>100</td><td>2.0</td><td>1</td></tr><tr><td>1</td><td>6</td><td>0.68</td><td>70</td><td>6.8</td><td>0</td></tr><tr><td>2</td><td>3</td><td>0.20</td><td>100</td><td>2.0</td><td>1</td></tr><tr><td>2</td><td>4</td><td>0.40</td><td>100</td><td>4.0</td><td>1</td></tr><tr><td>2</td><td>5</td><td>0.31</td><td>100</td><td>3.1</td><td>0</td></tr><tr><td>2</td><td>6</td><td>0.30</td><td>100</td><td>3.0</td><td>0</td></tr><tr><td>3</td><td>4</td><td>0.59</td><td>82</td><td>5.9</td><td>0</td></tr><tr><td>3</td><td>5</td><td>0.20</td><td>100</td><td>2.0</td><td>1</td></tr><tr><td>3</td><td>6</td><td>0.48</td><td>100</td><td>4.8</td><td>0</td></tr><tr><td>4</td><td>5</td><td>0.63</td><td>75</td><td>6.3</td><td>0</td></tr><tr><td>4</td><td>6</td><td>0.30</td><td>100</td><td>3.0</td><td>0</td></tr><tr><td>5</td><td>6</td><td>0.61</td><td>78</td><td>6.1</td><td>0</td></tr></table>

results in: $\begin{array} { r } { \begin{array} { r } { p _ { n , t } ^ { s } - p _ { n , t } ^ { b } = \sum , \quad B _ { n m } \Big ( \delta _ { n , t } - \delta _ { m , t } \Big ) L _ { n m } ; \forall n = 0 , 1 , \cdot \cdot \cdot , N ; } \end{array} } \end{array}$ $\forall t \in \mathcal T$ ; where $B _ { n m } { = } 1 / X _ { n m } ^ { n } , \bar { \bar { X } } _ { n m } ^ { m }$ is the reactance of the transmis-<sup>8 T</sup>sion asset connecting nodes n and m, $\left( \delta _ { n , t } - \delta _ { m , t } \right)$ is the difference between the angles of nodes n and m in period t, and $L _ { n m }$ is the number of both existing and new transmission assets connecting nodes n and m, assuming that all the assets connected in parallel between the nodes are identical. In addition, Eqs. (3) and (4) can be set as $| F _ { n m , t } | = | B _ { n m } ( \delta _ { n , t } - \delta _ { m , t } ) | \leq F _ { n m } ^ { \operatorname* { m a x } }$ , where $F _ { n m , t }$ is the active power <sup>fl</sup>ow in the transmission asset connecting nodes n and m in period t and $F _ { n m } ^ { \mathrm { I n n a x } }$ corresponds to the maximum limit of the active power <sup>fl</sup>ow in the asset connecting nodes n and m.

The optimal solution of problem (1)–(8) determines the amount of power sold and bought by the pool players. In addition, the dual variables $\lambda _ { n , t } , ~ ( \mu _ { i , t } ^ { \mathrm { m i n } } , \mu _ { i , t } ^ { \mathrm { m a x } } )$ and $( \mu _ { j , t } ^ { \operatorname* { m i n } } , \mu _ { i , t } ^ { \operatorname* { m a x } } )$ provide the locational marginal prices at each node n in period t, and the marginal values of a change in the capacity for each existing asset $\ell _ { i }$ and candidate asset $\ell _ { j } ^ { c }$ in period t, respectively.

2.2. Transmission planning model with decentralized transmission investment

A single seller and a single buyer at each node $n { = } 0 , 1 , \cdots ,$ N of the network are assumed, where ${ \mathcal { L } } = \{ { \boldsymbol { \ell } } _ { 1 } , { \boldsymbol { \ell } } _ { 2 } , { \boldsymbol { \cdot } } , { \boldsymbol { \ell } } _ { L } \}$ is the set of lines <sup>L</sup>and transformers that connect the buses of the network. This model has three distinctive features: i) transmission asset costs are not publicly available, ii) investment is possible, and iii) the TP has a budget constraint that takes into account the amount of monetary resources that can be used to reward investors. To account for these new features of the problem a set of investors $\mathcal { V } = \{ y _ { 1 } , y _ { 2 } , \cdots , y _ { Y } \}$ } is de<sup>fi</sup>ned, where each <sup>Y</sup>of them can build a set of new assets $\mathcal { L } _ { \mathcal { V } } ^ { \mathcal { C } } = \{ a _ { j } ^ { k } ; \forall j = 1 , 2 , \cdots , Y ; \forall k = 1 , 2 , \cdots ,$ K }, and a set of payments $Q _ { y } ^ { \mathcal { C } } = \{ q _ { j } ^ { k } ; \forall j = 1 , 2 , \therefore , Y ; \forall k = 1 , 2 , \cdots , K _ { j } \}$ that the

Garver 6-bus system: offer and bid function coef<sup>fi</sup>cients.

<table><tr><td rowspan="2">Node</td><td colspan="3">Generators</td><td colspan="3">Demands</td></tr><tr><td>Name</td><td> $a_i$  ($/MWh)</td><td> $b_i$  ($/MW2h)</td><td>Name</td><td> $c_j$  ($/MWh)</td><td> $d_j$  ($/MW2h)</td></tr><tr><td>1</td><td> $G_1$ </td><td>10</td><td>0.001</td><td> $D_1$ </td><td>28</td><td>0.002</td></tr><tr><td>2</td><td>-</td><td>-</td><td>-</td><td> $D_2$ </td><td>32</td><td>0.001</td></tr><tr><td>3</td><td> $G_2$ </td><td>20</td><td>0.002</td><td> $D_3$ </td><td>16</td><td>0.002</td></tr><tr><td></td><td> $G_3$ </td><td>22</td><td>0.003</td><td></td><td></td><td></td></tr><tr><td></td><td> $G_4$ </td><td>25</td><td>0.003</td><td></td><td></td><td></td></tr><tr><td>4</td><td>-</td><td>-</td><td>-</td><td> $D_4$ </td><td>27</td><td>0.002</td></tr><tr><td>5</td><td>-</td><td>-</td><td>-</td><td> $D_5$ </td><td>30</td><td>0.001</td></tr><tr><td>6</td><td> $G_5$ </td><td>8</td><td>0.001</td><td>-</td><td>-</td><td>-</td></tr><tr><td></td><td> $G_6$ </td><td>12</td><td>0.001</td><td></td><td></td><td></td></tr><tr><td></td><td> $G_7$ </td><td>15</td><td>0.002</td><td></td><td></td><td></td></tr><tr><td></td><td> $G_8$ </td><td>17</td><td>0.002</td><td></td><td></td><td></td></tr><tr><td></td><td> $G_9$ </td><td>19</td><td>0.002</td><td></td><td></td><td></td></tr><tr><td></td><td> $G_{10}$ </td><td>21</td><td>0.003</td><td></td><td></td><td></td></tr></table>

TP can initially offer to each individual investor. The binary variable m<sup>k</sup> is used to model the presence of new investors: it takes the value of 1 if the investor $y _ { j }$ is paid for the new transmission asset $a _ { j } ^ { k } ,$ and 0 otherwise. The value $B _ { D }$ represents the budget constraint of the TP, where the $T P$ initially estimates the payments to the investors based on transmission asset costs. The decentralized planning model can be formulated as the following social welfare maximization problem:

$$
\max S W = \sum_ {t \in \mathcal {T}} \sum_ {n = 0} ^ {N} \left[ \beta_ {n, t} ^ {b} \left(p _ {n, t} ^ {b}\right) - \beta_ {n, t} ^ {s} \left(p _ {n, t} ^ {s}\right) \right]
$$

s:t:

9

$$
g _ {n, t} \left(p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {1}, \dots , m _ {Y} ^ {K _ {Y}}\right)\tag{10}
$$

$$
= 0 \leftrightarrow \lambda_ {n, t}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}
$$

$$
\begin{array}{l} - f _ {i} ^ {m a x} \leq h _ {i, t} \Big (p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {1}, \dots , m _ {Y} ^ {K _ {Y}} \Big) \\ \leq f _ {i} ^ {m a x} \leftrightarrow \Big (\mu_ {i, t} ^ {m i n}, \mu_ {i, t} ^ {m a x} \Big); \forall i = 1, 2, \dots , L; \forall t \in \mathcal {T} \end{array}\tag{11}
$$

$$
\begin{array}{l} - f _ {j} ^ {k, m a x} \leq h _ {j, t} ^ {k} \left(p _ {0, t} ^ {s}, p _ {1, t} ^ {s}, \dots , p _ {N, t} ^ {s}; p _ {0, t} ^ {b}, p _ {1, t} ^ {b}, \dots , p _ {N, t} ^ {b}; m _ {1} ^ {1}, \dots , m _ {Y} ^ {K _ {Y}}\right) \\ \leq f _ {j} ^ {k, m a x} \leftrightarrow \left(\mu_ {j, t} ^ {k, m i n}, \mu_ {j, t} ^ {k, m a x}\right); \forall j = 1, \dots , L ^ {c}; \forall k = 1, \dots , K _ {j}; \forall t \in \mathcal {T} \end{array}\tag{12}
$$

$$
\sum_ {j = 1} ^ {Y} \sum_ {k = 1} ^ {K _ {j}} m _ {j} ^ {k} q _ {j} ^ {k} \leq B _ {D}\tag{13}
$$

$$
m _ {j} ^ {k} \in \{0, 1 \}; \forall j = 1, \dots , Y; \forall k = 1, \dots , K _ {Y}\tag{14}
$$

$$
0 \leq p _ {n, t} ^ {s} \leq p _ {n} ^ {s, m a x}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}\tag{15}
$$

$$
0 \leq p _ {n, t} ^ {b} \leq p _ {n} ^ {b, m a x}; \forall n = 0, 1, \dots , N; \forall t \in \mathcal {T}\tag{16}
$$

where $g _ { n , t } ( \bullet )$ is the nodal real power <sup>fl</sup>ow balance equation at node n in period $t , h _ { i , t } ( \bullet )$ is the expression of the real power <sup>fl</sup>ow in asset $\ell _ { i }$ in period t, and $h _ { j , t } ^ { k } ( \bullet )$ is the expression of the real power <sup>fl</sup>ow in candidate asset $a _ { j } ^ { k }$ of investor $y _ { j }$ in period t. For every constraint set there is a corresponding set of dual variables: $\{ \lambda _ { n , t } \colon \forall n { = } 0 , 1 , \ \cdots , N ; \ \forall t \in \mathcal { T } \}$ for the power <sup>fl</sup>ow balance equations, $\{ ( \mu _ { i , t } ^ { \operatorname* { m i n } } , \mu _ { i , t } ^ { \operatorname* { m a x } } ) { : \forall } i = 1 , { \cdots } , L ; \forall t \in T \}$ and $\{ ( \mu _ { j , t } ^ { k , m i n } , \mu _ { j , t } ^ { k , m a x } ) \colon \forall j = 1 , \cdots , \bar { Y } ; \forall k = 1 , \cdots , K _ { j } ; \forall t \in \mathcal { T } \}$ <sup>T</sup>for the real power <sup>fl</sup>ows <sup>T</sup>in existing transmission assets and investors' candidate assets, respectively. Note that both objective functions in Eqs. (1) and (9) do not incorporate the time value of money over the planning horizon for simplicity, but it should be added in a more realistic setting. Note also that transmission asset costs are not included in the formulation, since it is not public information in the decentralized model. Instead, it is assumed that the investors want to obtain an adequate rate of return expressed as a percentage over their actual construction costs. The centralized and decentralized formulations are compared in Appendix A, showing the conditions that make them equivalent. Note that there are two conditions for the decentralized optimal solution to be equivalent to the centralized optimal solution: i) the overall payments by all investors are bounded by the optimal investment cost of the centralized model, and ii) the individual payment requests by the investors are at actual costs.

Garver 6-bus system: upper generation limits.

<table><tr><td>Generator</td><td> $PG^{\max}$  (MW)</td></tr><tr><td> $G_1$ </td><td>150</td></tr><tr><td> $G_2$ </td><td>120</td></tr><tr><td> $G_3$ </td><td>120</td></tr><tr><td> $G_4$ </td><td>120</td></tr><tr><td> $G_5$ </td><td>100</td></tr><tr><td> $G_6$ </td><td>100</td></tr><tr><td> $G_7$ </td><td>100</td></tr><tr><td> $G_8$ </td><td>100</td></tr><tr><td> $G_9$ </td><td>100</td></tr><tr><td> $G_{10}$ </td><td>100</td></tr></table>

Garver 6-bus system: upper demand limits per season.

<table><tr><td rowspan="2">Demand</td><td colspan="4"> $PD^{max} (MW)$ </td></tr><tr><td>Season 1</td><td>Season 2</td><td>Season 3</td><td>Season 4</td></tr><tr><td> $D_1$ </td><td>80</td><td>120</td><td>130</td><td>90</td></tr><tr><td> $D_2$ </td><td>240</td><td>260</td><td>250</td><td>200</td></tr><tr><td> $D_3$ </td><td>40</td><td>60</td><td>60</td><td>60</td></tr><tr><td> $D_4$ </td><td>160</td><td>200</td><td>180</td><td>160</td></tr><tr><td> $D_5$ </td><td>240</td><td>260</td><td>260</td><td>210</td></tr></table>

The next section describes the bargaining process that coordinates both the investors' payment requirements and the TP offers to the investors that are initially selected in problem (9)–(16). In this case, the TP simply optimizes the social welfare and then receives the payment requirements of the investors, comparing these values with the Shapley value allocation. Since this is an iterative procedure, the results are not necessarily the same as in the centralized method. The budget constraint imposes a further restriction over the money paid to the investors, but cannot be directly used to compare the results with the ones from the centralized method, since the information set is different.

Note that both problem formulations, centralized and decentralized, allow sequential decomposition of the investment problem. The formulations also lend themselves nicely for scenario analysis, thereby providing a consistent basis to compare the impacts of different investments.

## 3. Investment incentives in decentralized planning: the investment game

The centralized transmission investment model presented in the previous section provides the set of investments which result in the maximum increase in bene<sup>fi</sup>ts to a network without an explicit formulation of the incentives. Since the costs of the new assets are known in advance and no investors are allowed, the $T P$ can solve the planning problem in a centralized fashion. However, in the second model, a decentralized transmission investment needs to create incentives to the investors whose assets improve the network. Therefore, in order to make both the TP and the investors decide to build new assets, a simple and fair criterion must exist, based on the value that a new asset brings to the system.

Garver 6-bus system: <sup>fi</sup>nal centralized and decentralized solutions without a budget constraint.

<table><tr><td rowspan="2">Corridor</td><td rowspan="2">Pre-expansion</td><td colspan="2">New lines</td></tr><tr><td>Centralized model</td><td>Decentralized model</td></tr><tr><td>1-2</td><td>1</td><td>-</td><td>-</td></tr><tr><td>1-3</td><td>0</td><td>-</td><td>-</td></tr><tr><td>1-4</td><td>1</td><td>-</td><td>-</td></tr><tr><td>1-5</td><td>1</td><td>-</td><td>-</td></tr><tr><td>1-6</td><td>0</td><td>-</td><td>-</td></tr><tr><td>2-3</td><td>1</td><td>-</td><td>-</td></tr><tr><td>2-4</td><td>1</td><td>-</td><td>-</td></tr><tr><td>2-5</td><td>0</td><td>-</td><td>-</td></tr><tr><td>2-6</td><td>0</td><td>2</td><td>3</td></tr><tr><td>3-4</td><td>0</td><td>-</td><td>-</td></tr><tr><td>3-5</td><td>1</td><td>1</td><td>-</td></tr><tr><td>3-6</td><td>0</td><td>-</td><td>-</td></tr><tr><td>4-5</td><td>0</td><td>-</td><td>-</td></tr><tr><td>4-6</td><td>0</td><td>2</td><td>2</td></tr><tr><td>5-6</td><td>0</td><td>-</td><td>1</td></tr><tr><td># of lines</td><td>-</td><td>5</td><td>6</td></tr><tr><td>Annualized cost (1000$/year)</td><td>-</td><td>14,000</td><td>-</td></tr><tr><td>Required payment (1000$/year)</td><td>-</td><td>-</td><td>22,155</td></tr><tr><td>SW (1000$/year)</td><td>44,654</td><td>97,144</td><td>100,083</td></tr><tr><td>SW increase (%)</td><td>-</td><td>217.55</td><td>224.13</td></tr></table>

Table 8  
Table 6  
Garver 6-bus system: decentralized model iterations without a budget constraint

<table><tr><td>Iteration</td><td>Investor</td><td>Lines per investor</td><td>Required payments (1000$/year)</td><td>Shapley values (1000$/year)</td></tr><tr><td rowspan="3">1</td><td>2-6</td><td>3</td><td>9450</td><td>27,271</td></tr><tr><td>4-6</td><td>2</td><td>6300</td><td>17,700</td></tr><tr><td>5-6</td><td>2</td><td>12,810</td><td>11,527</td></tr><tr><td rowspan="3">2</td><td>2-6</td><td>3</td><td>9450</td><td>29,511</td></tr><tr><td>4-6</td><td>2</td><td>6300</td><td>18,653</td></tr><tr><td>5-6</td><td>1</td><td>6405</td><td>7265</td></tr></table>

The value of a transmission asset is de<sup>fi</sup>ned as the increase in social welfare that this new asset (or combination of assets) brings to the network over the planning horizon, as compared to the preinvestment scenario, where no new assets are considered.

Rewarding the investors based on the improvement that their new assets bring to the social welfare can be done in several ways. The simplest choice is to reward each individual investor with the increase in social welfare that its new assets produce alone. This approach, although simple, has the disadvantage of not considering the combined effects of multiple separate transmission investments in the network. For that reason, a method based on cooperative game theory is used: the Shapley value, which incorporates the ef<sup>fi</sup>ciency and fairness principles [21]<sup>1</sup>. By using the Shapley value we can analyze the combined effects of simultaneous investments and also remunerate only the investors that truly improve the social welfare.

The investment problem is treated as a cooperative game, where the players are investors in transmission assets and the TP reimburses these investors by offering them all or part of the social welfare increase that they produce when they are selected. This can be seen as a cooperative value allocation game, where the players are rewarded as a function of the improvement that they can bring to the system. Using cooperative game theory standard notation, the proposed transmission investment game is de<sup>fi</sup>ned by a pair ( , ΔSW), where $\mathcal { V } = \{ y _ { 1 } , y _ { 2 } , \cdots , y _ { Y } \}$ <sup>Y</sup>is the set of investors and ΔSW is the increase in <sup>Y</sup>social welfare of the network with respect to the pre-investment scenario; in game theoretic terminology it is called the characteristic function (see Appendix B).

Using the notation from above, the Shapley value allocation per investor is given by:

$$
\phi_ {j} = \sum_ {S \subseteq \mathcal {Y}} \frac {(Y - s) ! (s - 1) !}{Y !} \left[ \Delta S W (\mathcal {S}) - \Delta S W \left(\mathcal {S} - \left\{y _ {j} \right\}\right) \right]; \forall j = 1, \dots , Y\tag{17}
$$

where

$$
\begin{array}{l l} \phi_ {j}: & \text {Shapley value allocation to investor y_{j}}, \\ Y: & \text {total number of investors,} \\ S: & \text {coalition of investors,} \\ s = | S |: & \text {number of investors in coalition S}, \\ \Delta S W (S): & \text {increase in social welfare brought by coalition S}. \end{array}
$$

Thus, the Shapley value of a player in a game can be interpreted as the increase in the coalition surplus brought by the player to a coalition.

The <sup>fi</sup>nal values assigned to each investor as a result of the game can be expressed by a vector of payments $\overline { { { \phi } } } _ { Y } = \{ \Phi _ { 1 } , \Phi _ { 2 } , \cdots , \Phi _ { Y } \} ,$ , where $\phi _ { j }$ is the payoff to investor $y _ { j } .$ The sum of all these values is equal to the increase in social welfare due to all the investors, as shown in Shapley value's axiom 1 of Appendix B. Note that investors do not really engage in actual coalitions. This is just an artifact used by the TP to account for all possible combinations of investors and their joint effect in the social welfare increase. In real-life transmission investment cases, where the number of coalitions is not too high, the proposed method can be applied without reaching an explosion of combinations of possible investors. Additionally, note that an investor that is asking for a high return on investment may be in risk of being dropped off if the competitors' payment requests are not publicly available or he is unable to calculate the social welfare increase in all scenarios as performed by the TP.

Table 7  
Garver 6-bus system: investors' rate of return effect on investments.

<table><tr><td rowspan="2">Iteration</td><td rowspan="2">Investor</td><td rowspan="2">Lines</td><td colspan="3">Required payments (1000$/year)</td><td rowspan="2">Shapley values (1000$/year)</td></tr><tr><td>20%</td><td>25%</td><td>30%</td></tr><tr><td rowspan="3">1</td><td>2-6</td><td>3</td><td>10,800</td><td>11,250</td><td>11,700</td><td>27,271</td></tr><tr><td>4-6</td><td>2</td><td>7200</td><td>7500</td><td>7800</td><td>17,700</td></tr><tr><td>5-6</td><td>2</td><td>14,640</td><td>15,250</td><td>15,860</td><td>11,527</td></tr><tr><td rowspan="3">2</td><td>2-6</td><td>3</td><td>10,800</td><td>11,250</td><td>11,700</td><td>29,511</td></tr><tr><td>4-6</td><td>2</td><td>7200</td><td>7500</td><td>7800</td><td>18,653</td></tr><tr><td>5-6</td><td>1</td><td>7320</td><td>7625</td><td>7930</td><td>7265</td></tr><tr><td rowspan="3">3</td><td>2-6</td><td>3</td><td>10,800</td><td>11,250</td><td>11,700</td><td>30,363</td></tr><tr><td>4-6</td><td>2</td><td>7200</td><td>7500</td><td>7800</td><td>19,882</td></tr><tr><td>5-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

The following algorithm is proposed to represent the interactions between the TP and the investors for the decentralized investment model using the Shapley value allocation scheme:

Step 1: The TP selects the initial set of investors from those who have declared interest in building transmission assets. To that end, the TP runs the decentralized investment model subject to budget constraints (9)–(16) with $q _ { j } ^ { k }$ equal to the respective investor's requirements.

Step 2: The TP calculates the increase in social welfare with respect to the pre-investment scenario for all the combinations of selected investors resulting from the decentralized investment model. Based on that, the TP calculates the Shapley values (Eq. (17)) and compares them to the investors' requirements. For a single asset investor, if the Shapley value is higher than the payment requested, the TP noti<sup>fi</sup>es the investor that he can build the transmission asset and that he will be paid what he requests. Otherwise, the TP tells the investor that he is not selected. In case of a non-selected investor with more than one transmission asset, the TP requests the investor to withdraw at least one of his transmission assets in the next iteration. If two investors propose to build identical lines and they ask for identical payments they are limited by the number of lines per investor per right-of-way bound that can be imposed by the planner. This bound can be added to the budget constraint to avoid redundant investments.

Garver 6-bus system: decentralized model initial line proposals subject to budge constraints

<table><tr><td rowspan="2"></td><td rowspan="2">Corridor</td><td colspan="8">Budget (M$/year)</td></tr><tr><td>0</td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td><td>60</td></tr><tr><td rowspan="15">Lines to install</td><td>1-2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td></tr><tr><td>2-3</td><td>-</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td></tr><tr><td>2-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-6</td><td>-</td><td>-</td><td>1</td><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>3-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3-5</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4-6</td><td>-</td><td>1</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td></tr><tr><td>5-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>2</td><td>2</td></tr><tr><td># of proposed lines</td><td></td><td>0</td><td>2</td><td>3</td><td>5</td><td>7</td><td>7</td><td>7</td><td>7</td></tr></table>

Table 9  
Garver 6–bus system: centralized (C) and decentralized (D) solutions subject to budget constraints.

<table><tr><td rowspan="3"></td><td rowspan="3">Corridor</td><td colspan="15">Budget (M$/year)</td><td></td></tr><tr><td colspan="2">0</td><td colspan="2">5</td><td colspan="2">10</td><td colspan="2">15</td><td colspan="2">20</td><td colspan="2">25</td><td colspan="2">30</td><td colspan="2">60</td></tr><tr><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td><td>C</td><td>D</td></tr><tr><td rowspan="15">Lines to install</td><td>1-2</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>1-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-3</td><td>-</td><td>-</td><td>1</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>2-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>3</td><td>2</td><td>3</td><td>2</td><td>3</td></tr><tr><td>3-4</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>3-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td><td>1</td><td>-</td><td>1</td><td>-</td></tr><tr><td>3-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4-5</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>4-6</td><td>-</td><td>-</td><td>1</td><td>1</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>5-6</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>1</td><td>-</td><td>1</td></tr><tr><td colspan="2">Total number of new lines</td><td>0</td><td>0</td><td>2</td><td>2</td><td>3</td><td>3</td><td>5</td><td>5</td><td>5</td><td>7</td><td>5</td><td>6</td><td>5</td><td>6</td><td>5</td><td>6</td></tr></table>

Step 3: The TP veri<sup>fi</sup>es how many investors have decided to build the assets and goes to step 2.

Step 4: The game ends when there are no more investors willing to build more transmission assets.

## 4. Case studies

The proposed decentralized incentive scheme is applied to the Garver 6-bus system [15] and the IEEE 24-bus case from the Reliability Test System (RTS) [33]. Both case studies are simulation-based, meaning that they have been done faithfully reproducing the centralized and decentralized algorithms described in the two previous sections. The following assumptions are made:

1. Marginal offers and marginal bids by generators and demands are linear and remain unchanged for all the periods of study, such that $p _ { i } = a _ { i } + b _ { i } P G _ { i }$ and $p _ { j } = c _ { j } - d _ { j } P D _ { j }$ , where p is the price offer of generator i that produces $P G _ { i } \mathrm { M W } , p _ { j }$ is the price bid of demand j that consumes PD MW, and $a _ { i } , b _ { i } , c _ { j } , d _ { j }$ are the price intercepts and slope coef<sup>fi</sup>cients of the linear functions of the generators and demands, respectively. Offers are at marginal cost, bids re<sup>fl</sup>ect actual demand utility functions, and therefore the cost function of generator i can be expressed as $C _ { i } ( P G _ { i } ) = a _ { i } P G _ { i } + 0 . 5 b _ { i } P G _ { i } ^ { 2 }$ and the bene<sup>fi</sup>t function of demand j is de<sup>fi</sup>ned as $B _ { j } ( P D _ { j } ) = c _ { j } P D _ { j } - 0 . 5 d _ { j } P D _ { j } ^ { 2 } .$ Note that the fact that generators offer at their marginal costs is a good strategy when considering perfect competition.

2. The time horizon is one year, that is, a “target year”. For this “target year” the demand, the generation offers and the demand bids are estimated. Therefore, this model represents a “Static Transmission

![](/api/attachments/7RYTPRZN/fulltext/images/dd1bf91c6685362e74f95d9f6cbf317e03e9a1c153598e43c92f72c1ebc17cbe.jpg)  
Fig. 2. IEEE 24-bus system topology.

Table 10 Table 10  
IEEE 24-bus RTS: line data.

<table><tr><td>From</td><td>To</td><td>X (pu)</td><td>Line flow limit (MW)</td><td>Annualized cost (M$)</td><td>Already built</td></tr><tr><td>1</td><td>2</td><td>0.0139</td><td>87.5</td><td>0.704</td><td>1</td></tr><tr><td>1</td><td>3</td><td>0.2120</td><td>87.5</td><td>10.692</td><td>1</td></tr><tr><td>1</td><td>5</td><td>0.0845</td><td>87.5</td><td>4.278</td><td>1</td></tr><tr><td>2</td><td>4</td><td>0.1267</td><td>87.5</td><td>6.414</td><td>1</td></tr><tr><td>2</td><td>6</td><td>0.1920</td><td>87.5</td><td>9.720</td><td>1</td></tr><tr><td>3</td><td>9</td><td>0.1190</td><td>87.5</td><td>6.024</td><td>1</td></tr><tr><td>3</td><td>24</td><td>0.0839</td><td>200.0</td><td>4.247</td><td>1</td></tr><tr><td>4</td><td>9</td><td>0.1037</td><td>87.5</td><td>5.250</td><td>1</td></tr><tr><td>5</td><td>10</td><td>0.0883</td><td>87.5</td><td>4.470</td><td>1</td></tr><tr><td>6</td><td>10</td><td>0.0605</td><td>87.5</td><td>3.063</td><td>1</td></tr><tr><td>7</td><td>8</td><td>0.0614</td><td>87.5</td><td>3.108</td><td>1</td></tr><tr><td>8</td><td>9</td><td>0.1651</td><td>87.5</td><td>8.358</td><td>1</td></tr><tr><td>8</td><td>10</td><td>0.1651</td><td>87.5</td><td>8.358</td><td>1</td></tr><tr><td>9</td><td>11</td><td>0.0839</td><td>200.0</td><td>4.247</td><td>1</td></tr><tr><td>9</td><td>12</td><td>0.0839</td><td>200.0</td><td>4.247</td><td>1</td></tr><tr><td>10</td><td>11</td><td>0.0839</td><td>200.0</td><td>4.247</td><td>1</td></tr><tr><td>10</td><td>12</td><td>0.0839</td><td>200.0</td><td>4.247</td><td>1</td></tr><tr><td>11</td><td>13</td><td>0.0476</td><td>250.0</td><td>2.410</td><td>1</td></tr><tr><td>11</td><td>14</td><td>0.0418</td><td>250.0</td><td>2.116</td><td>1</td></tr><tr><td>12</td><td>13</td><td>0.0476</td><td>250.0</td><td>2.410</td><td>1</td></tr><tr><td>12</td><td>23</td><td>0.0966</td><td>250.0</td><td>4.890</td><td>1</td></tr><tr><td>13</td><td>23</td><td>0.0865</td><td>250.0</td><td>4.379</td><td>1</td></tr><tr><td>14</td><td>16</td><td>0.0389</td><td>250.0</td><td>1.970</td><td>1</td></tr><tr><td>15</td><td>16</td><td>0.0173</td><td>250.0</td><td>0.876</td><td>1</td></tr><tr><td>15</td><td>21</td><td>0.0490</td><td>250.0</td><td>2.481</td><td>1</td></tr><tr><td>15</td><td>24</td><td>0.0519</td><td>250.0</td><td>2.627</td><td>1</td></tr><tr><td>16</td><td>17</td><td>0.0259</td><td>250.0</td><td>1.311</td><td>1</td></tr><tr><td>16</td><td>19</td><td>0.0231</td><td>250.0</td><td>1.170</td><td>1</td></tr><tr><td>17</td><td>18</td><td>0.0144</td><td>250.0</td><td>0.729</td><td>1</td></tr><tr><td>17</td><td>22</td><td>0.1053</td><td>250.0</td><td>5.331</td><td>1</td></tr><tr><td>18</td><td>21</td><td>0.0259</td><td>250.0</td><td>1.311</td><td>1</td></tr><tr><td>19</td><td>20</td><td>0.0396</td><td>250.0</td><td>2.005</td><td>1</td></tr><tr><td>20</td><td>23</td><td>0.0216</td><td>250.0</td><td>1.093</td><td>1</td></tr><tr><td>21</td><td>22</td><td>0.6780</td><td>250.0</td><td>3.432</td><td>1</td></tr></table>

Expansion Planning” problem, since it considers a “target year” for which the net social welfare is maximized.<sup>2</sup>

3. It is assumed that the new assets will be operative for at least 25 years, thus a 25-year investment return period has been considered. A 10% interest discount rate is assumed as the cost of capital. Bearing these values in mind, the value of the capital recovery factor can be calculated so that, for the next 25 years, the investment cost in new transmission assets is yearly repaid at a rate of 11.02% of the total initial investment. This is also known as the annualized cost.

4. A dc model of the network is used and losses are not considered in the formulation.

## 4.1. Garver 6-bus system

The system considered comprises 5 nodes and 6 lines connecting them; moreover, a sixth node is considered, at which some generation is placed. This node is not connected to the other <sup>fi</sup>ve nodes, but lines to connect it to the system could be built if necessary. Fig. 1 shows this system where dashed lines indicate some possible lines. Table 1 lists the line data of the system. The <sup>fi</sup>rst two columns provide the nodes of origin and destination of the lines, the third column shows the reactance of the lines in pu (with a 100 MVA base value), the fourth column shows the capacity that the lines can transmit, and the annualized line costs, proportional to the line reactances, are shown in the <sup>fi</sup>fth column. Up to three parallel lines are accepted for every possible connection between the nodes. The last column shows the number of lines already built for every possible corridor.

Table 2 presents the location of generators and demands in the network and the offer and bid function coef<sup>fi</sup>cients. The time span of the study is one year and it is split into four seasons of equal duration (2190 h per season out of 8760 h per year). Table 3 shows the maximum generation limits and Table 4 lists the demand limits for each season of the year. The rate of return required by the investors is 5% over actual costs and the budget constraint is \$60 M (a high value equivalent to no budget constraint).

Table 11  
IEEE 24-bus RTS: offer and bid function coef<sup>fi</sup>cients.

<table><tr><td rowspan="2">Node</td><td colspan="3">Generators</td><td colspan="3">Demands</td></tr><tr><td>Name</td><td> $a_i$  ($/MWh)</td><td> $b_i$  ($/MW2h)</td><td>Name</td><td> $c_j$  ($/MWh)</td><td> $d_j$  ($/MW2h)</td></tr><tr><td rowspan="2">1</td><td> $G_1$ </td><td>71</td><td>0.046</td><td> $D_1$ </td><td>58</td><td>0.054</td></tr><tr><td> $G_2$ </td><td>24</td><td>0.043</td><td></td><td></td><td></td></tr><tr><td rowspan="2">2</td><td> $G_3$ </td><td>71</td><td>0.031</td><td> $D_2$ </td><td>30</td><td>0.013</td></tr><tr><td> $G_4$ </td><td>24</td><td>0.074</td><td></td><td></td><td></td></tr><tr><td>3</td><td>-</td><td>-</td><td>-</td><td> $D_3$ </td><td>44</td><td>0.031</td></tr><tr><td>4</td><td>-</td><td>-</td><td>-</td><td> $D_4$ </td><td>10</td><td>0.052</td></tr><tr><td>5</td><td>-</td><td>-</td><td>-</td><td> $D_5$ </td><td>32</td><td>0.034</td></tr><tr><td>6</td><td>-</td><td>-</td><td>-</td><td> $D_6$ </td><td>19</td><td>0.037</td></tr><tr><td>7</td><td> $G_5$ </td><td>34</td><td>0.064</td><td> $D_7$ </td><td>29</td><td>0.041</td></tr><tr><td>8</td><td>-</td><td>-</td><td>-</td><td> $D_8$ </td><td>34</td><td>0.026</td></tr><tr><td>9</td><td>-</td><td>-</td><td>-</td><td> $D_9$ </td><td>68</td><td>0.073</td></tr><tr><td>10</td><td>-</td><td>-</td><td>-</td><td> $D_{10}$ </td><td>69</td><td>0.055</td></tr><tr><td>11</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>13</td><td> $G_6$ </td><td>33</td><td>0.062</td><td> $D_{11}$ </td><td>43</td><td>0.059</td></tr><tr><td>14</td><td>-</td><td>-</td><td>-</td><td> $D_{12}$ </td><td>45</td><td>0.015</td></tr><tr><td rowspan="2">15</td><td> $G_7$ </td><td>41</td><td>0.067</td><td> $D_{13}$ </td><td>20</td><td>0.061</td></tr><tr><td> $G_9$ </td><td>20</td><td>0.070</td><td></td><td></td><td></td></tr><tr><td>16</td><td> $G_8$ </td><td>20</td><td>0.051</td><td> $D_{14}$ </td><td>63</td><td>0.057</td></tr><tr><td>17</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>18</td><td> $G_{10}$ </td><td>10</td><td>0.073</td><td> $D_{15}$ </td><td>27</td><td>0.071</td></tr><tr><td>19</td><td>-</td><td>-</td><td>-</td><td> $D_{16}$ </td><td>32</td><td>0.025</td></tr><tr><td>20</td><td>-</td><td>-</td><td>-</td><td> $D_{17}$ </td><td>19</td><td>0.040</td></tr><tr><td>21</td><td> $G_{11}$ </td><td>10</td><td>0.057</td><td>-</td><td>-</td><td>-</td></tr><tr><td>22</td><td> $G_{12}$ </td><td>24</td><td>0.013</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">23</td><td> $G_{13}$ </td><td>20</td><td>0.044</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $G_{14}$ </td><td>19</td><td>0.056</td><td></td><td></td><td></td></tr><tr><td>24</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

The expansion plans and the values of the social welfare achieved without expansion, with a centralized solution, and with a decentralized solution are shown in Table 5.

Table 12  
IEEE 24-bus RTS: generation and demand limits.

<table><tr><td rowspan="2">Node</td><td colspan="2">Generators</td><td colspan="3">Demands</td></tr><tr><td>Name</td><td> $PG^{max} (MW)$ </td><td>Name</td><td> $PD^{min} (MW)$ </td><td> $PD^{max} (MW)$ </td></tr><tr><td rowspan="2">1</td><td> $G_1$ </td><td>40</td><td> $D_1$ </td><td>50</td><td>110</td></tr><tr><td> $G_2$ </td><td>152</td><td></td><td></td><td></td></tr><tr><td rowspan="2">2</td><td> $G_3$ </td><td>40</td><td> $D_2$ </td><td>50</td><td>100</td></tr><tr><td> $G_4$ </td><td>152</td><td></td><td></td><td></td></tr><tr><td>3</td><td>-</td><td>-</td><td> $D_3$ </td><td>125</td><td>180</td></tr><tr><td>4</td><td>-</td><td>-</td><td> $D_4$ </td><td>40</td><td>75</td></tr><tr><td>5</td><td>-</td><td>-</td><td> $D_5$ </td><td>40</td><td>75</td></tr><tr><td>6</td><td>-</td><td>-</td><td> $D_6$ </td><td>60</td><td>140</td></tr><tr><td>7</td><td> $G_5$ </td><td>300</td><td> $D_7$ </td><td>60</td><td>125</td></tr><tr><td>8</td><td>-</td><td>-</td><td> $D_8$ </td><td>90</td><td>175</td></tr><tr><td>9</td><td>-</td><td>-</td><td> $D_9$ </td><td>90</td><td>175</td></tr><tr><td>10</td><td>-</td><td>-</td><td> $D_{10}$ </td><td>90</td><td>195</td></tr><tr><td>11</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>12</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>13</td><td> $G_6$ </td><td>591</td><td> $D_{11}$ </td><td>125</td><td>265</td></tr><tr><td>14</td><td>-</td><td>-</td><td> $D_{12}$ </td><td>90</td><td>195</td></tr><tr><td rowspan="2">15</td><td> $G_7$ </td><td>60</td><td> $D_{13}$ </td><td>155</td><td>320</td></tr><tr><td> $G_9$ </td><td>155</td><td></td><td></td><td></td></tr><tr><td>16</td><td> $G_8$ </td><td>155</td><td> $D_{14}$ </td><td>50</td><td>100</td></tr><tr><td>17</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>18</td><td> $G_{10}$ </td><td>400</td><td> $D_{15}$ </td><td>160</td><td>330</td></tr><tr><td>19</td><td>-</td><td>-</td><td> $D_{16}$ </td><td>100</td><td>180</td></tr><tr><td>20</td><td>-</td><td>-</td><td> $D_{17}$ </td><td>60</td><td>130</td></tr><tr><td>21</td><td> $G_{11}$ </td><td>400</td><td>-</td><td>-</td><td>-</td></tr><tr><td>22</td><td> $G_{12}$ </td><td>300</td><td>-</td><td>-</td><td>-</td></tr><tr><td rowspan="2">23</td><td> $G_{13}$ </td><td>310</td><td>-</td><td>-</td><td>-</td></tr><tr><td> $G_{14}$ </td><td>350</td><td></td><td></td><td></td></tr><tr><td>24</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

Table 16  
Table 14  
Table 13  
IEEE 24-bus RTS: load level percentages per period.

<table><tr><td>Period</td><td>Season</td><td>Day type</td><td>Duration (hours)</td><td>% of load</td></tr><tr><td>1</td><td>Spring</td><td>Weekday</td><td>1512</td><td>43.0</td></tr><tr><td>2</td><td>Spring</td><td>Weekend</td><td>720</td><td>40.0</td></tr><tr><td>3</td><td>Summer</td><td>Weekday</td><td>1560</td><td>100.0</td></tr><tr><td>4</td><td>Summer</td><td>Weekend</td><td>672</td><td>81.3</td></tr><tr><td>5</td><td>Fall</td><td>Weekday</td><td>1416</td><td>60.0</td></tr><tr><td>6</td><td>Fall</td><td>Weekend</td><td>720</td><td>50.0</td></tr><tr><td>7</td><td>Winter</td><td>Weekday</td><td>1464</td><td>74.0</td></tr><tr><td>8</td><td>Winter</td><td>Weekend</td><td>696</td><td>65.0</td></tr></table>

Table 6 shows the evolution of the decentralized model. In the <sup>fi</sup>rst iteration, the TP selects three investors and seven candidate lines by running the decentralized model (Eqs. (9)–(16). Investors in corridors 2-6 and 4-6 are accepted, since their required payments (based on a 5% rate of return over actual line costs) are smaller than the Shapley value allocations, but investor in corridor 5-6 is asked to withdraw one of his lines from the game, since the Shapley value allocation is not enough to reward his two lines. Note that only the investor in corridor 2-6 is allowed to build the maximum number of lines per corridor. In the second iteration, the investor in corridor 5-6 builds just one line and his payment request is accepted. Thus, the game ends in the second iteration and 6 lines are built.

It is also possible that the investors can ask for a higher rate of return to increase their pro<sup>fi</sup>ts. Table 7 shows the effect of a gradual increase in the required rate of return of all the investors. It can be observed that with a rate of return of 20% or higher for all investors, the investor in corridor 5-6 is no longer accepted and therefore, the <sup>fi</sup>nal solution only has 3 lines from investor 2-6 and 2 lines from investor 4-6, as expected.

Table 8 shows the initial line proposals of the decentralized model when a range of budget constraints is imposed. Table 9 shows the corresponding centralized and decentralized solutions. It can be observed that the centralized and decentralized <sup>fi</sup>nal solutions in Table 9 are not the same when the budget limit exceeds \$15 M. Note that this budget limit is suf<sup>fi</sup>ciently close to \$14 M, the optimal investment cost of the centralized problem in Table 5, for which the <sup>fi</sup>nal solutions of both models are approximately the same if the rates of return are also suf<sup>fi</sup>ciently small, i.e., payments and costs are similar (see Appendix A).

## 4.2. IEEE 24-bus RTS case study

The IEEE 24-bus RTS [33] is shown in Fig. 2 and line data are provided in Table 10. Line <sup>fl</sup>ow limits in Table 10 are half of their original values in [33] to allow for future expansion. Total line costs are taken from [1] and their annualized values are also shown in Table 10. A maximum of three lines per corridor is allowed for the network expansion. The time span of the study is 1 year and it is split into eight periods. Each period corresponds to a weekday or a weekend of each season. Bidding and offer data are taken from [38] and presented in Table 11. Table 12 shows the maximum generation limits and the minimum and maximum demand limits. Table 13 lists the duration of each period and its load level percentage. The minimum and maximum demands per period are obtained by multiplying the minimum and maximum values from Table 12 by the load level percentages in Table 13. Two case studies are analyzed below to illustrate the model and the effect of budget limits.

IEEE 24-bus RTS: centralized and decentralized solutions without a budget limit.

<table><tr><td rowspan="2">Corridor</td><td rowspan="2">Pre-expansion</td><td colspan="2">New lines</td></tr><tr><td>Centralized model</td><td>Decentralized model</td></tr><tr><td>14–16</td><td>1</td><td>1</td><td>1</td></tr><tr><td>16–17</td><td>1</td><td>1</td><td>-</td></tr><tr><td># of lines</td><td>34</td><td>2</td><td>1</td></tr><tr><td>Annualized cost (1000$/year)</td><td>-</td><td>3281</td><td>-</td></tr><tr><td>Required payment (1000$/year)</td><td>-</td><td>-</td><td>2068</td></tr><tr><td>SW (1000$/year)</td><td>204,297</td><td>213,091</td><td>208,785</td></tr><tr><td>SW increase (%)</td><td>-</td><td>4.30</td><td>2.20</td></tr></table>

Table 15  
IEEE 24-bus RTS: decentralized model iterations without a budget limit.

<table><tr><td>Iteration</td><td>Investor</td><td>Lines per investor</td><td>Required payments (1000$/year)</td><td>Shapley values (1000$/year)</td></tr><tr><td rowspan="6">1</td><td>1-2</td><td>2</td><td>1478</td><td>233</td></tr><tr><td>2-6</td><td>1</td><td>10,206</td><td>-316</td></tr><tr><td>3-24</td><td>1</td><td>4459</td><td>2623</td></tr><tr><td>14-16</td><td>1</td><td>2068</td><td>4186</td></tr><tr><td>15-21</td><td>1</td><td>2605</td><td>1798</td></tr><tr><td>16-17</td><td>1</td><td>1377</td><td>1323</td></tr><tr><td rowspan="2">2</td><td>1-2</td><td>1</td><td>739</td><td>0</td></tr><tr><td>14-16</td><td>1</td><td>2068</td><td>4465</td></tr><tr><td>3</td><td>14-16</td><td>1</td><td>2068</td><td>4465</td></tr></table>

IEEE 24-bus RTS: centralized and decentralized solutions with a \$5 M-budget limit.

<table><tr><td rowspan="2">Corridor</td><td colspan="2">New lines</td></tr><tr><td>Centralized model</td><td>Decentralized model</td></tr><tr><td>14–16</td><td>1</td><td>1</td></tr><tr><td>16–17</td><td>1</td><td>1</td></tr><tr><td># of lines</td><td>2</td><td>2</td></tr><tr><td>Annualized cost (1000$/year)</td><td>3281</td><td>-</td></tr><tr><td>Required payment (1000$/year)</td><td>-</td><td>3694</td></tr><tr><td>SW (1000$/year)</td><td>213,091</td><td>213,091</td></tr><tr><td>SW increase (%)</td><td>4.30</td><td>4.30</td></tr></table>

## 4.2.1. IEEE 24-bus RTS case study without a budget limit

The rate of return required by the investors is 5% and the budget is \$55 M (a high value equivalent to no budget constraint). The values of the social welfare achieved without expansion, with a centralized solution, and with the proposed decentralized approach are shown in Table 14.

Table 15 shows the evolution of the decentralized model, which stops after three iterations. In the <sup>fi</sup>rst iteration, the TP selects six investors and seven lines by running the decentralized model (Eqs. (9)–(16)). Note that in this iteration the Shapley value corresponding to investor 2-6 is negative. It means that there are some coalitions of investors in which the increase in social welfare is higher than the one obtained when investor 2-6 belongs to them.<sup>3</sup> In addition, investor 1-2 has a zero Shapley value in the second iteration, which means that this investor does not add anything to his coalition with investor 14-16. The game ends after three iterations and only one line is built. Note that the number of candidate lines is high but the real contribution to the social welfare comes only from a few of them.

## 4.2.2. IEEE 24-bus RTS case study with a budget limit

Now, it is assumed that the TP imposes a budget constraint of \$5 M and investors in corridors 14-16, 16-17 and 16-19 require a rate of return of 15, 9, and 6%, respectively. Table 16 presents the results of the centralized and decentralized models. Table 17 lists the evolution of the decentralized algorithm. Note that the <sup>fi</sup>nal centralized and decentralized solutions are the same because the budget limit is equal to \$5 M, which is suf<sup>fi</sup>ciently close to the optimal investment cost of the centralized problem, \$3.281 M (see Table 16), and the rates of return are also suf<sup>fi</sup>ciently small, i.e., payments and costs are similar.

Table 17  
IEEE 24-bus RTS: decentralized model iterations with a \$5 M-budget limit.

<table><tr><td>Iteration</td><td>Investor</td><td>Lines per investor</td><td>Required payments (1000$/year)</td><td>Shapley values (1000$/year)</td></tr><tr><td rowspan="3">1</td><td>14–16</td><td>1</td><td>2265</td><td>6442</td></tr><tr><td>16–17</td><td>1</td><td>1429</td><td>2102</td></tr><tr><td>16–19</td><td>1</td><td>1240</td><td>187</td></tr><tr><td rowspan="2">2</td><td>14–16</td><td>1</td><td>2265</td><td>6578</td></tr><tr><td>16–17</td><td>1</td><td>1429</td><td>2192</td></tr></table>

The software used to solve all the optimization models is the SBB solver under GAMS [4] through the web-based NEOS server [28]. The Shapley value allocations are obtained using the Cooperative Game Toolbox [12] in MATLAB [26] on an Intel Pentium 4 PC with 256 Mb of RAM at 2.8 GHz. Running times of GAMS and MATLAB models for all case studies are below 10 s.

## 5. Conclusions

Two different models for transmission planning and investment in electricity markets are presented. The <sup>fi</sup>rst model is a centralized model, where the costs of expansion are publicly known and the investment is performed by the TP. The second model allows for a decentralized expansion of the network. In this model, the investors build new transmission assets according to the incentives provided by the TP. These incentives are calculated using the Shapley value formula and are based on the increase in social welfare produced by the combined effect of new transmission assets. To make this decentralized decision model a <sup>fl</sup>exible tool, both a budget limit and a payment requirement are imposed by the TP and the investors, respectively. Further research will consider the combined effect of generation and transmission investments in more realistic scenarios and the development of a multi-year investment model.

## Acknowledgment

Professor Jean Derks is kindly acknowledged for the use of his Cooperative Game Toolbox [12].

Appendix A: Equivalence between the centralized and decentralized formulations

This Appendix presents the proof that the decentralized formulation of the investment problem $\left( \mathrm { E q s . } \left( 9 \right) \mathrm { - } ( 1 6 ) \right) ,$ ) yields the same results as the centralized one $( \mathsf { E q s . } ( 1 ) \ – ( 8 ) )$ under the following assumptions:

1. Payments are made at the actual costs.

2. The overall decentralized investment payment offered by the TP is less than or equal to the optimal investment cost of the centralized problem.

The above conditions can be mathematically formulated as:

$$
I P (x _ {d}) = I C (x _ {d}) \leq I C (x _ {c} ^ {*})\tag{18}
$$

where $I P ( x _ { d } )$ is the decentralized investment payment by the TP, IC $\left( x _ { d } \right)$ is the actual decentralized investment cost, $I C ( x _ { c } ^ { * } )$ is the optimal centralized investment cost, and $x _ { d }$ and x are the decision vectors of the decentralized and centralized models, respectively. In other words, both models are equivalent when payments are equal to the actual costs and the decentralized budget limit, $B _ { D } ,$ is equal to the optimal investment cost of the centralized problem.

Proof. The above claim will be proved by reductio ad absurdum. Let the optimal solution to the decentralized problem, x ⁎, yield a level of social welfare different from that obtained by the optimal solution to the centralized problem, x<sub>c</sub>⁎, i.e., $S W ( x _ { d } ^ { * } ) \neq S W ( x _ { c } ^ { * } )$ . Then, four cases must be analyzed:

1) $S W ( x _ { d } ^ { * } ) { > } S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) = I C ( x _ { c } ^ { * } ) .$

In this $\mathrm { c a s e } \ S W ( x _ { d } ^ { * } ) - I C ( x _ { d } ^ { * } ) = S W ( x _ { d } ^ { * } ) - I C ( x _ { c } ^ { * } ) > S W ( x _ { c } ^ { * } ) - I C ( x _ { c } ^ { * } ) .$ The maximum attainable value of $S W ( x _ { d } ) - I C ( x _ { d } )$ is equal to $S W ( x _ { c } ^ { * } ) -$ $I C ( x _ { c } ^ { * } )$ as per the optimization of problem $( 1 )  { - } ( 8 )$ . Therefore, there exists a contradiction.

$2 ) S W ( x _ { d } ^ { * } ) { > } S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) { < } I C ( x _ { c } ^ { * } )$

Similarly to case $1 , S W ( x _ { d } ^ { * } ) - I C ( x _ { d } ^ { * } ) { > } S W ( x _ { c } ^ { * } ) - I C ( x _ { c } ^ { * } )$ , and, therefore, the same contradiction is found.

3) $S W ( x _ { d } ^ { * } ) { < } S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) = I C ( x _ { c } ^ { * } ) .$

In this case the optimal solution to the decentralized problem $x _ { d } ^ { * } ,$ is assumed to yield a level of social welfare lower than that corresponding to the optimal solution to the centralized problem. In addition, constraint (18) is binding at the optimal solution of the decentralized problem (Eqs. (9)–(16)).

Under these assumptions:

a) SW(x ⁎)−IC(x ⁎)= SW(x ⁎)−IC(x ⁎), and

b) $S W ( x _ { c } ^ { * } ) - I C ( x _ { c } ^ { * } ) { < } S W ( x _ { c } ^ { * } ) - I C ( x _ { c } ^ { * } )$ , which is the optimal value of the objective function of problem (1)–(8).

Since problem (9)–(16) maximizes the social welfare, $x _ { d } ^ { * }$ cannot be its optimal solution because a higher value of social welfare with the same level of investment cost is achieved by x⁎.

4) $S W ( x _ { d } ^ { * } ) { < } S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) { < } I C ( x _ { c } ^ { * } )$

In this case the constraint on investment payment (Eq. (18)) is not binding and consequently it can be removed from the optimization. Thus, $S W ( x _ { d } ^ { * } )$ is an upper bound for the solution to problem (9)–(16) with constraint (18) binding (case 3). Since the optimal solution to case 3 yields a level of social welfare equal to $S W ( x _ { c } ^ { * } )$ , then, SW(x ⁎) has to be greater than or equal to SW(x<sub>c</sub>⁎), which contradicts the initial assumption.

As a conclusion the four above situations are infeasible. The only feasible optimal solution is: $S W ( x _ { d } ^ { * } ) = S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) =$ $I C ( x _ { c } ^ { * } )$ . It should also be noted that this proof holds when the budget constraint (5) is binding. In this case the only feasible optimal solution is: $S W ( x _ { d } ^ { * } ) = S W ( x _ { c } ^ { * } )$ and $I P ( x _ { d } ^ { * } ) = I C ( x _ { d } ^ { * } ) = I C ( x _ { c } ^ { * } ) = B _ { C }$

## Appendix B: Cooperative game theory background

A cooperative game is de<sup>fi</sup>ned by a real-valued function u called the characteristic function [21]. The function u assigns to each subset C of $\mathcal { P }$ (the set of all players) the maximum value of a game played <sup>P</sup>between C and $\mathcal { P } - C , \mathrm { i . e . , } u ( C )$ is the best total utility that the coalition C can obtain under the worst scenario induced by the actions of the remaining players. The players can form coalitions in many different ways; the way in which players can group in m mutually exclusive and excluding coalitions S is given by $\delta = \{ S _ { 1 } , \ S _ { 2 } , \ \cdots , \ S _ { m } \} ,$ , where δ is a partition of P that satis<sup>fi</sup>es these three conditions:

$$
\begin{array}{l l} S _ {j} \neq \varnothing ; & \forall j = 1, 2, \dots , m \\ S _ {i} \cap S _ {j} = \varnothing ; & \forall i \neq j \\ \cup S _ {j} = P, \end{array}\tag{19}
$$

where $\emptyset$ is the empty set.

The Shapley value of a game u for player $i , \phi _ { i } ,$ is given by Eq. (17), and is the unique value vector that satis<sup>fi</sup>es these four axioms:

Axiom 1: the set of players receives all the resources available, i.e., $\smash { \sum _ { j = 1 } \phi _ { i } [ u ] = u ( \mathcal { P } ) }$

Axiom 2: if S is a dummy, i.e., $u ( C ) - u ( C - \{ i \} ) = u ( \{ i \} )$ for each coalition C in , then $\Phi _ { i } [ u ] = u ( \{ i \} )$

Axiom 3: the value assigned to player i does not depend on the position of the player in the set of players.

Axiom 4: if u and v are the characteristic functions of two games, then $\phi _ { i } [ u + \nu ] = \phi _ { i } [ u ] + \phi _ { i } [ \nu ] .$

## References

[1] N. Alguacil, A.L. Motto, A.J. Conejo, Transmission expansion planning: a mixedinteger LP approach, IEEE Transactions on Power Systems 18 (3) (August 2003) 1070–1077.

[2] S. Binato, M.V.F. Pereira, S. Granville, A new Benders decomposition approach to solve power transmission network design problems, IEEE Transactions on Power Systems 16 (2) (May 2001) 235–240.

[3] E. Bjørndal, G.C. Stamtsis, I. Erlich, Finding core solutions for power system <sup>fi</sup>xed cost allocation, IEE Proceedings – Generation, Transmission & Distribution 152 (2) (March 2005) 173–179

[4] A. Brooke, D. Kendrick, A. Meeraus, R. Raman, GAMS – A User's Guide, GAMS Development Corporation, Washington DC, USA, 1998.

[5] J.B. Bushnell, S.E. Stoft, Electric grid investment under a contract network regime, Journal of Regulatory Economics 10 (1) (July 1996) 61–79.

[6] H.–P. Chao, S. Peck, A market mechanism for electric power transmission, Journal of Regulatory Economics 10 (1) (July 1996) 25–59.

[7] E.H. Clarke, Multipart pricing of public goods, Public Choice 11 (1) (1971) 17–33.

[8] J. Contreras, F.F. Wu, Coalition formation in transmission expansion planning, IEEE Transactions on Power Systems 14 (3) (August 1999) 1144–1152.

[9] J. Contreras, F.F. Wu, A kernel-oriented algorithm for transmission expansion planning, IEEE Transactions on Power Systems 15 (4) (November 2000) 1434–1440.

[10] J. Contreras, V. Bósquez, G. Gross, A framework for the analysis of transmission planning in the market environment, Proceedings of the 15th Power Systems Computation Conference, Liège, Belgium, August 22–26, 2005.

[11] M.J. Denton, S.J. Rassenti, V.L. Smith, S.R. Backerman, Market power in a deregulated electrical industry, Decision Support Systems 30 (3) (January 2001) 357–381.

[12] J. Derks, Cooperative Game Toolbox, http://www.math.unimaas.nl/PERSONAL/ jeand/downlds/CGinMatlab20050731.zip

[13] Y.P. Dusonchet, A. El-Abiad, Transmission planning using discrete dynamic optimizing, IEEE Transactions on Power Apparatus and Systems 92 (4) (July 1973) 1358-1371.

[14] R.A. Gallego, A. Monticelli, R. Romero, Transmission system expansion planning by an extended genetic algorithm, IEE Proceedings – Generation, Transmission & Distribution 145 (3) (May 1998) 329–335.

[15] L.L. Garver, Transmission network estimation using linear programming, IEEE Transactions on Power Apparatus and Systems 89 (7) (September–October 1970) 1688–1697.

[16] P.R. Gribik, D. Shirmohammadi, J.S. Graves, J.G. Kritikson, Transmission rights and transmission expansions, IEEE Transactions on Power Systems 20 (4) (November 2005) 1728–1737.

[18] T. Groves, Incentives in teams, Econometrica 41 (4) (1973) 617–631.

[17] G. Gross, Challenges and opportunities in the new transmission business, Proceedings of the 2004 Australasian Universities Power Engineering Conference, University of Oueensland. Brisbane, Australia, September 26–29. 2004.

[19] W.W. Hogan, Contract networks for electric power transmission, Journal of Regulatory Economics 4 (3) (September 1992) 211–242.

[20] P. Joskow, J. Tirole, Merchant transmission investment, Journal of Industrial Economics 53 (2) (June 2005) 233–264.

[21] J. Kahan, A. Rapoport, Theories of Coalition Formation, Lawrence Erlbaum, London, UK, 1984.

[22] G. Latorre, R.D. Cruz, J.M. Areiza, A. Villegas, Classi<sup>fi</sup>cation of publications and models on transmission expansion planning, IEEE Transactions on Power Systems 18 (2) (May 2003) 938–946.

[23] T.–O. Léautier, Transmission constraints and imperfect markets for power, Journal of Regulatory Economics 19 (1) (January 2001) 27–54.

[24] M. Liu, G. Gross, Framework for the design and analysis of congestion revenue rights, IEEE Transactions on Power Systems 19 (1) (February 2004) 243–251.

[25] M. Liu, A framework for transmission congestion management analysis, PhD Thesis, Department of Electrical and Computer Engineering, University of Illinois at Urbana–Champaign, USA, 2005.

[26] MATLAB® Reference Guide, The MathWorks Inc., Natick, MA, USA, 2006

[27] T. Mount, Market power and price volatility in restructured markets for electricity Decision Support Systems 30 (3) (January 2001) 311–325.

[28] NEOS Solvers, http://neos.mcs.anl.gov/neos/solvers.

[29] G.C. Oliveira, A.P.C. Costa, S. Binato, Large scale transmission network planning using optimization and heuristic techniques, IEEE Transactions on Power Systems 10 (4) (November 1995) 1828–1834.

[30] S. Oren P Spiller P Varaiva EE Wu Nodal prices and transmission rights: a critical appraisal, The Electricity Journal 8 (3) (April 1995) 24–35.

[31] G. Pritchard, A. Philpott, On <sup>fi</sup>nancial transmission rights and market power, Decision Support Systems 40 (3–4) (October 2005) 507–515.

[32] I.J. Ramírez-Rosado, T. Gönen, Pseudodynamic planning for expansion of power distribution systems, IEEE Transactions on Power Systems 6 (1) (February 1991) 245-254.

[33] Reliability Test System Task Force, The IEEE reliability test system—1996, IEEE Transactions on Power Systems 14 (3) (August 1999) 1010–1020.

[34] R. Romero, A. Monticelli, A hierarchical decomposition approach for transmission network expansion planning, IEEE Transactions on Power Systems 9 (1) (February 1994) 373–380.

[35] R. Romero, R.A. Gallego, A. Monticelli, Transmission system expansion planning by simulated annealing, IEEE Transactions on Power Systems 11 (1) (February 1996) 364-369.

[36] J. Rosellón, Different approaches towards electricity transmission expansion, Review of Network Economics 2 (3) (September 2003) 238–269.

[37] R.E. Schuler, Analytic and experimentally derived estimates of market power in deregulated electricity systems: policy implications for the management and institutional evolution of the industry, Decision Support Systems 30 (3) (January 2001) 341–355.

[38] G.B. Shrestha, P.A.J. Fonseka, Congestion-driven transmission expansion in competitive power markets, IEEE Transactions on Power Systems 19 (3) (August 2004) 1658–1665.

[39] W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1) (March 1961) 8–37.

[40] R. Villasana, L.L. Garver, S.J. Salon, Transmission network planning using linear programming, IEEE Transactions on Power Apparatus and Systems 104 (2) (February 1985) 349–356.

[41] J. Yen, Y. Yan, J. Contreras, P.–C. Ma, F.F. Wu, Multi-agent approach to the planning of power transmission expansion, Decision Support Systems 28 (3) (May 2000) 279–290.

[42] J.M. Zolezzi, H. Rudnick, Transmission cost allocation by cooperative games and coalition formation, IEEE Transactions on Power Systems 17 (4) (November 2002) 1008–1015.

![](/api/attachments/7RYTPRZN/fulltext/images/c49bedc05b3f1bbd1e63b2e59aa1a15c2b61604eec92dd0a7c1ba21b31b378d6.jpg)  
Javier Contreras received his BS in Electrical Engineering from the University of Zaragoza, Spain, his MSc from the University of Southern California, and his PhD from the University of California, Berkeley, in 1989, 1992, and 1997, respectively. His research interests include power systems planning, operations and economics, and electricity markets. He is currently Associate Professor at the University of Castilla — La Mancha, Ciudad Real, Spain.

![](/api/attachments/7RYTPRZN/fulltext/images/390b35141a4f9ef7fae13a496b1fbb2294903497db5497ac750720ca960ca20a.jpg)

George Gross is Professor of Electrical and Computer Engineering and Professor, Institute of Government and Public Affairs, at the University of Illinois at Urbana– Champaign. His current research and teaching activities are in the areas of power system analysis, planning, economics and operations and utility regulatory policy and industry restructuring His undergraduate work was completed at McGill University, and he earned his graduate degrees from the University of California, Berkeley. He was previously employed by Paci<sup>fi</sup>c Gas and Electric Company in various technical, policy and management positions.

![](/api/attachments/7RYTPRZN/fulltext/images/65ef05748de61e89d45c130c1eced8f585cf6d6da55bf814c40a322769025703.jpg)

José Manuel Arroyo received the Ingeniero Industrial degree from the Universidad de Málaga, Málaga, Spain, in 1995, and the Ph.D. degree in power systems operations planning from the Universidad de Castilla — La Mancha, Ciudad Real, Spain, in 2000. From June 2003 through July 2004 he held a Richard H. Tomlinson Postdoctoral Fellowship at the Department of Electrical and Computer Engineering of McGill University, Montreal, OC, Canada. He is currently an Associate Professor of Electrical Engineering at the Universidad de Castilla — La Mancha. His research interests include operations, planning and economics of power systems, as well as optimization and parallel computation.

![](/api/attachments/7RYTPRZN/fulltext/images/77360623c640dbd892c693bd9c86fa44822f2d8a64bc2c23d984467441209ffe.jpg)

José Ignacio Muñoz received his BS in Industrial Engineering from the University of Navarra, Spain, in 1998 and his MSc from the University of País Vasco, Spain, in 2003. He is currently working towards his PhD at this University. His research interests include power systems forecasting, operations and economics, and project management. He has been working as Project Manager in several engineering <sup>fi</sup>rms and is, currently, Assistant Professor at the University of Castilla — La Mancha, Ciudad Real, Spain.
