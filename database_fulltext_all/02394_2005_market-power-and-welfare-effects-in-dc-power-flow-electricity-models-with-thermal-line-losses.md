---
otero_id: 2394
otero_key: "5DE9QRWJ"
title: "Market power and welfare effects in DC power flow electricity models with thermal line losses"
authors: "Rastislav Ivanic; Paul V. Preckel; Zuwei Yu"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Market power and welfare effects in DC power flow electricity models with thermal line losses

Rastislav Ivanic<sup>a</sup>, Paul V. Preckel<sup>a,\*</sup>, Zuwei Yu<sup>b</sup>

<sup>a</sup>Department of Agricultural Economics, 1145 Krannert Building, Purdue University, West Lafayette, IN 47907-1145, United States <sup>b</sup>State Utility Forecasting Group, Purdue University, West Lafayette, IN, United States

Available online 22 October 2004

## Abstract

A nodal electric power network with Cournot–Nash interaction among power generators is formulated as a mixed complementarity problem. The model incorporates a direct current (DC) power flow approximation with thermal line losses to model real-time flows. We include constant wheeling rate and variable congestion charges for transmission of electricity. Market power and welfare effects are measured in an aggregated Indiana electric grid model. We find that imposing DC power flow constraints in a model results in significant changes in social welfare estimates. Line losses are also an important factor affecting market power and welfare of market participants in the case study. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Electricity markets; Imperfect competition; Welfare measurement; Thermal line losses

## 1. Introduction

Much attention in the literature has been paid to the study of deregulation of electricity markets. Issues such as transmission pricing and deregulated market structure have been the most prominent. A comprehensive survey of recent literature is presented in Ref. [5]. Here, we focus on studying market power and social welfare—major issues in deregulated markets. The central issue in this paper is the effect of physical properties of electric power networks on market power and consumers’ welfare in the real-time dispatch problem. The physical properties discussed in this paper are a direct current (DC) power flow approximation, thermal line limits, and thermal line losses.

Current transmission pricing in the U.S. deregulated electricity markets consists of fixed wheeling charges and congestion charges. The fixed wheeling charges are used to recover transmission capital costs while congestion charges provide funds for future expansion of transmission capacity. Fixed wheeling charges have been posted on various OASIS (Open Access Same Time Information Systems) systems as requested by the FERC. Our paper is the first to consider both charges in a noncooperative gaming model.

Our model is a real-time model with explicit thermal line limits and congestion charges, and thus is inherently different from similar models, where electric power can concurrently flow both ways on a line. Simultaneous bidirectional flows are impossible in real time because electrons can flow only one way on the line at any instant. Removing counter flows from the model by imposing DC power flow constraints adds another constraint to the dispatch problem and can have an effect on the competitiveness electricity markets. Here we explore the effects of this physical phenomenon on the market power within the system. The model presented is an alternative formulation to those of Refs. [1,2], which also includes DC power flow approximation in the real-time markets. Our formulation of the problem is simple and still captures the physical properties of the network while it reflects the Cournot assumptions.

The major difference between our model and those in Refs. [1,2] is that we assume that our Transmission Agent (TA) is regulated (i.e., the TA does not maximize profit). Although in deregulated electricity markets, some system operators maximize the total (pseudo) welfare (PJM, California, NYISO, etc.), other transmission operators only dispatch bids to ensure that transmission capacity limits are not violated. This is the case with the Midwest ISO or in Texas, which are examples where contracts are predominantly bilateral. Our formulation of the TA’s problem reflects the latter case.

In the United States, a transmission agent (or operator) is to enforce open access and conduct nondiscriminative transactions for market participants. The current transmission pricing policy consists of fixed wheeling and variable congestion charges. Our paper captures all theses aspects of the deregulated electricity markets in the U.S. This paper also correctly evaluates the fixed charges for transmission use. They are assessed along the real flow paths rather than along the contractual paths.

Another important physical phenomenon in modeling electricity markets is thermal losses. As electricity is transmitted via a line, part of the transmitted energy transforms into heat and is wasted. From the market power point of view, thermal losses make power transmission less efficient and create a barrier to competition for more distant generation facilities. Most literature acknowledges line losses as a factor in market function; however, we are not aware of any formulation that formally incorporates lines losses in a noncooperative gaming model with the exception of the price leadership model in Ref. [3]. Thus, one goal of this paper is to assess the importance of line losses in electricity market models.

This paper is organized as follows. We first introduce our model in the framework of the DC power flow approximation with line losses. Then we introduce a simplified Indiana power network with real-world data on generation, demand, and transmission. Finally, we use the model to discern the effects of DC power flow constraints and line losses on market power within the system. Uniqueness of solution and our formulation of TA’s problem are discussed in Appendices.

## 2. Model description

We formulate our model as a linear complementarity problem. This is an extension to the seminal work in Refs. [1,2]. In our model, we recognize three types of agents: consumers, Cournot–Nash oligopolistic producers, and a transmission agent. Consumers are assumed to maximize their surplus, producers act as profit maximizers who recognize limited market power, and the TA operates the transmission system reliably and efficiently. The TA is regulated and is entrusted to operate the electric network and charge transmission fees to other market participants. This is different from other models that consider the TA as a revenue maximizer.

Other differences between our model and others are: we compute the DC power distribution factors, which used for approximating the DC power flow, inside of the model, while others take them as given outside the model. We also omit the generation variable as it can be computed directly from the sales variables. For example, Ref. [2] uses a transmission service variable to balance the market, whereas we use a demand quantity variable to balance demand and supply of energy at each node in the network rather than transmission. Finally, we set our model up in a way to make it easy to account appropriately for line losses.

Our approach to determining load factors is consistent with the framework employed in Ref. [4], which enables a fixed set of injections and loads to be decomposed into flows on individual lines and attributes real flows on individual connections to financial transactions. These flows are calculated using the standard DC-Load model approximations [4]. Under these assumptions, the distribution factors over individual lines are constant. In other words, if we know how individual power flows are distributed for injection and consumption of 1 unit of power, then individual real power flows for a multiple of this amount will increase them by the same multiple if there is no congestion. If there is congestion, some load/injection pairs are impossible to accommodate. This formulation allows us to also combine injection/load pairs with each other (e.g., if we would like to know the factors resulting from injection/load pair (1,3), we can do it by combining the factors resulting from pairs (1,4) and (4,3)).

## 2.1. Notation

The sets used in the model are listed below:

<table><tr><td>i,j,m</td><td>Zone or node indices (=1, ..., N)</td></tr><tr><td>s,k</td><td>Producer/supplier indices (=1, ..., S)</td></tr><tr><td>l</td><td>Connection index (=1, ..., L)</td></tr><tr><td>n,v</td><td>Line indices for positive and negative flows across connections (=1, ..., 2L)</td></tr></table>

There are N nodes in the model, which are connected by $l { = } ( l , . . . . , L )$ connections (transmission lines). Each connection is assigned an a priori direction of flow (i.e., it is assigned a positive or negative sign). However, given that real flows are not restricted in direction, the sign is only an aid to applying Kirchhoff’s laws and has no bearing on the rest of the model. Because our goal is to model the line losses in the system, we further divide each connection indexed by $l { = } ( l , . . . . , L )$ into two virtual lines indexed by $\scriptstyle n = ( I , \ . . . , \ 2 L )$ where the index n separately keeps track of flows in one direction (positive direction as it is the same as the assigned direction of connection l) and the other represents the flows in the opposite direction (negative flows). This approach makes modeling line losses transparent and intuitive. When n is odd, it indexes the positive flow (with respect to preassigned direction) on connection $\begin{array} { r } { l = \frac { ( n + 1 ) } { 2 } } \end{array}$ , and when n is even, it indexes the negative flow on the connection $\begin{array} { r } { l = \frac { n } { 2 } . } \end{array}$ . Thus, for example, line 1 is assigned for real power flows along the first connection, and line 2 represents real flows in the opposite direction of the first line. Lines 3 and 4 are associated with connection 2, etc.

The parameters are summarized below:

<table><tr><td> $T_{\text{max}_n}$ </td><td>Flow upper limit along line n (MW)</td></tr><tr><td> $a_I$ </td><td>Intercept for the inverse demand function at node i</td></tr><tr><td> $b_I$ </td><td>Slope for the inverse demand function at node i</td></tr><tr><td> $d_{is}$ </td><td>Linear cost coefficient for generator in node i owned by firm s</td></tr><tr><td> $P_{\text{max}_is}$ </td><td>Generation capacity at node i by producer s</td></tr><tr><td> $\alpha_n$ </td><td>Line loss factor on line n in percent of flow</td></tr><tr><td> $\text{Kirmatrix}_{vn}$ </td><td>Matrix of Kirchhoff&#x27;s relations</td></tr><tr><td> $\text{Lossmatrix}_{vn}$ </td><td>Matrix of line loss incidence throughout the network</td></tr><tr><td> $B_{\text{matrix}_{vij}}$ </td><td>Matrix of solutions to the system of Kirchhnoff&#x27;s relations</td></tr><tr><td> $B_{\text{lossmatrix}_{vij}}$ </td><td>Matrix of line loss incidence in the solution B matrix</td></tr><tr><td> $\text{Odd}_n$ </td><td>Switch matrix with 1 for positive flow elements of line index l,0 otherwise</td></tr><tr><td> $\text{Even}_n$ </td><td>Switch matrix with 1 for negative flow elements of line index l,0 otherwise</td></tr><tr><td> $w_n$ </td><td>Capital recovery charge applied to flow on a line</td></tr></table>

We construct the matrix of Kirchhoff’s relations using Ref. [4] as a guide:

$$
\left(\operatorname{Kirmatrix} _ {v n} - \operatorname{Lossmatrix} _ {v n}\right) \times \operatorname{fac} _ {n i j} = \left(\operatorname{Bmatrix} _ {v i j} - \operatorname{Blossmatrix} _ {v i j}\right)
$$

where Kirmatrix is a matrix based on Kirchhoff’s current and voltage laws, from which line loss constants are $_ { \cdot _ { \nu n } }$ subtracted. The role of line losses and their incorporation into our problem is discussed in Appendix B.

Model variables and Lagrange multipliers:

<table><tr><td> $\rho_{is}$ </td><td>Shadow price on production capacity</td></tr><tr><td> $f_{ijs}$ </td><td>Sales of power or Financial flow from i to j by firm s</td></tr><tr><td> $q_I$ </td><td>Demand at node i</td></tr><tr><td> $\theta_n^+$ </td><td>Congestion charge for constraining/decongesting line n</td></tr><tr><td> $\theta_n^-$ </td><td>Congestion charge for constraining/decongesting line n</td></tr><tr><td> $\delta_{lij}$ </td><td>Lagrange multiplier on factor (fac $_{nij}$ ) equations</td></tr><tr><td> $\lambda_I$ </td><td>Price of electricity at node i</td></tr><tr><td>fac $_{nij}$ </td><td>Load factors on line n caused by sales from i to j</td></tr></table>

There are three classes of optimization problems embedded in the model representing the three classes of agents as discussed earlier. The TA optimizes the delivery of the power, which can be regarded as a <sup>b</sup>pseudo TA problem<sup>Q</sup> because in real terms, all flows are determined by net injections into the system. That is, once the market participants determine financial transactions, which are based on supply and demand conditions and on transmission charges, the individual real flows are determined as well. What the TA does is calculate wheeling charges, and compute congestion fees by enforcing the network’s physical laws (represented by Kirchhoff’s laws) and consequently either penalizing market participants for creating congestion or rewarding those transactions that relieve congestion. Thus, the TA does not direct flows per se, but creates incentives for market participants to use the network efficiently.

The TA problem determines the power load factors as described in Ref. [4], which in turn determine how much each transaction is charged or credited for congestion created or relieved. Our model computes congestion charges on each line and any point-to-point transmission wheeling rate is implicit in the model. That is, point-to-point transmission rates can be computed by multiplying individual congestion charges by the power factors.

## 2.2. The consumer’s problem

Consumers maximize their surplus from consuming electricity defined as a difference between the price of energy actually paid to the electricity sellers and consumers’ maximum willingness to pay for that amount of energy. Consumers’ demand functions are assumed to be affine and strictly decreasing with respect to the price of energy consumed. Hence, consumer surplus maximization at node i can be formulated as:

$$
\underset {q _ {i}} {\text { minimize }} \quad Z _ {c i} = \left[ - a _ {i} - \frac {1}{2} b _ {i} q _ {i} \right] q _ {i} + \lambda_ {i} q = \int_ {0} ^ {q _ {i}} [ a _ {i} - b _ {i} q ] d q - \lambda_ {i} q _ {i}
$$

subject to:

$$
q _ {i} \geq 0.\tag{1}
$$

In the equilibrium, the consumers’ willingness to pay for the extra unit of energy is equal to the price paid to the generator and/or TA agent. This is described by the following first-order optimality conditions (FOCs):

$$
\frac {\partial (Z _ {c})}{\partial q _ {i}} = - a _ {i} - b _ {i} q _ {i} + \lambda_ {i} \geq 0 \text {   and   } \frac {\partial Z _ {c i}}{\partial q _ {i}} q _ {i} = (- a _ {i} - b _ {i} q _ {i} + \lambda_ {i}) q _ {i} = 0\tag{2}
$$

Note that the second equation is a complementarity condition.

## 2.3. The producer’s problem

Producers choose the levels of electricity sales to individual consumers to maximize their profit (minimize the negative profit). The producers are assumed to behave as Cournot–Nash oligopolists recognizing that their behavior will have an effect on nodal prices. They, however, treat the strategies of their competitors as fixed.

$$
\begin{array}{l} \underset {f _ {i j s}} {\text { minimize }} Z _ {p s} = \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left\{- \lambda_ {j} \left(f _ {i j s} \left[ 1 - \sum_ {n = 1} ^ {2 L} \alpha_ {n} \operatorname{fac} _ {n i j} \right]\right) + d _ {i s} f _ {i j s} + \sum_ {n = 1} ^ {2 L} w _ {n} \operatorname{fac} _ {n i j} f _ {i j s} \right. \\ \quad \left. + \left(\sum_ {n \in \text { odd }} \operatorname{fac} _ {n i j} \theta_ {n} ^ {+} + \sum_ {n \in \text { even }} \operatorname{fac} _ {n i j} \theta_ {n} ^ {-} - \sum_ {n \in \text { odd }} \operatorname{fac} _ {(n + 1) i j} \theta_ {n} ^ {+} - \sum_ {n \in \text { even }} \operatorname{fac} _ {(n - 1) i j} \theta_ {n} ^ {-}\right) f _ {i j s} \right\} \end{array}
$$

subject to:

$$
P \max _ {i s} - \sum_ {j = 1} ^ {N} f _ {i j s} \geq 0; \quad : \rho_ {i s}\tag{3}
$$

The first term in the objective function is the revenue from sales of energy to node $j ,$ where we recognize that $\begin{array} { r } { \lambda _ { i } = a _ { i } + b _ { i } \sum _ { i = 1 } ^ { N } \sum _ { s = 1 } ^ { S } f _ { i j s } } \end{array}$ in the equilibrium. We note that the producers are getting paid for the energy delivered to the consumer (i.e., electricity shipped out less the thermal line losses). The second term is the cost of production of energy. The cost function of energy production is assumed to be linear and strictly increasing. The third term is the wheeling charge, and the last term is the charge for creating or credit for relieving congestion on the network. The proportion of the congestion fee charged to a particular sale of power is determined by the actual flow on the congested line caused by that sale. For example, if selling 1 MW to consumer A creates a 0.50-MW real flow on congested connection l with resulting congestion charge rate of \$10/MW, the producer will be charged $0 . 5 0 \times \mathbb { S } 1 0 { = } \mathbb { S } 5$ congestion charge. If, on the other hand, another producer is selling 1 MW to consumer B, which causes the 0.3 MW of power pressure on connection l in the other direction (i.e., what would be counter flow), that producer will be credited \$3 for relieving congestion.

Congestion charges themselves are the shadow prices on the thermal constraints of the transmission system, which state that the flow of real power on each line is limited to some level that cannot be exceeded. We have two sets of constraints, one set for odd (positive) and one for even (negative) numbered lines each resulting in two kinds of congestion charges.

The sales of electricity from a given node are constrained by the generator capacity $P \ \mathrm { m a x } _ { i s }$ . Producers are also constrained by the market clearing condition requiring that the amount of energy sold to each node is at least as much as the consumers’ demand at the node. The resulting Lagrange multiplier is the equilibrium market price for each node of the network.

The FOCs are:

$$
\begin{array}{l} \frac {\partial (Z _ {p})}{\partial f _ {i j s}} = \left[ - \lambda_ {j} - f _ {i j s} b _ {j} \left(1 - \sum_ {n = 1} ^ {2 L} \alpha_ {n} \operatorname{fac} _ {n i j}\right) \right] \left(1 - \sum_ {n = 1} ^ {2 L} \alpha_ {n} \operatorname{fac} _ {n i j}\right) + d _ {i s} + \rho_ {i s} + \sum_ {n \in \text { odd }} \operatorname{fac} _ {n i j} \theta_ {n} ^ {+} + \sum_ {n \in \text { even }} \operatorname{fac} _ {n i j} \theta_ {n} ^ {-} \\ - \sum_ {n \in \text { odd }} \operatorname{fac} _ {(n + 1) i j} \theta_ {n} ^ {+} - \sum_ {n \in \text { even }} \operatorname{fac} _ {(n - 1) i j} \theta_ {n} ^ {-} + \sum_ {n = 1} ^ {2 L} w _ {n} \operatorname{fac} _ {n i j} \geq 0 \text { and } \frac {\partial Z _ {p s}}{\partial f _ {i j s}} f _ {i j s} = 0; f _ {i j s} \geq 0 \quad \forall i, j, s \end{array}\tag{4}
$$

Because we model the producers to be Cournot competitors, we assume that $\begin{array} { r } { \frac { \partial f _ { i j t } } { \partial f _ { i j s } } = 0 } \end{array}$ for all $t \neq s$ . We also note that although we do not allow physical counter flows in our model, the financial counter flows can occur as we allow all producers to compete in all markets.

## 2.4. The TA problem

In order to achieve a unique solution (uniqueness is discussed further in Appendix C), we require a third agent in our model. The concept of a transmission agent can be found in many models (for example, Ref. [2]). Because the previous optimization problems can solve only for unique net flows in the network, and we require a unique solution for flows in each direction, we need to use another optimization to ensure that all the flows in the system are unique. In other words, the <sup>b</sup>net<sup>Q</sup> load factors, as a solution to the system of equations, are unrestricted in sign. If the matrix of the Kirchhoff’s relations is nonsingular, we can be assured of the uniqueness of the solution to the load factor problem. However, when we divide the net load factors into the even and odd factors, the system of equations determining the net load factors is undetermined because we have twice as many variables as equations. Hence, we need to produce an optimization problem to assign the positive part of th net load factor to $\operatorname { f a c } _ { n }$ where n is odd and the negative part of the net load factor to $\operatorname { f a c } _ { n }$ where n is even.

We formulate the TA problem so as to determine the net, directed load factors per unit of energy sold. Moreover, because we recognize that the load factors of real flows resulting from an injection/load pair remain the same for any volume of transactions (barring congestion), we do not need to compute the actual flows in the system or the transmission service levels, rather, knowing the set of factors will be sufficient. The $\mathrm { T A }$ <sup>b</sup>chooses<sup>Q</sup> the factors associated with each financial transaction, so that the resulting set of factors satisfies Kirchhoff’s current and voltage laws.

$$
\underset {f a c _ {n i j}} {\text { Minimize }} Z _ {\mathrm{TA}} = \sum_ {n = 1} ^ {2 L} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \operatorname{fac} _ {n i j}
$$

Subject to:

$$
\sum_ {n = 1} ^ {2 L} \left(\operatorname{kirmatrix} _ {v n} - \alpha_ {n} \text { lossmatrix } _ {v n}\right) \operatorname{fac} _ {n i j} - \operatorname{bmatrix} _ {v i j} + \text { lossmatrix } _ {v i j} \sum_ {n = 1} ^ {2 L} \alpha_ {n} \operatorname{fac} _ {n i j} = 0: \delta_ {v i j} \operatorname{fac} _ {n i j} \geq 0\tag{5}
$$

The FOCs are:

$$
\frac {\partial \left(Z _ {\mathrm{TA}}\right)}{\partial \operatorname{fac} _ {n i j}} = 1 - \sum_ {v - 1} ^ {2 L} \delta_ {v i j} \left[ \operatorname{kirmatrix} _ {v n} + \alpha_ {n} \left(\text { b   l   o   s   s   m   a   t   r   i   x } _ {v i j} - \text { l   o   s   s   m   a   t   r   i   x } _ {v n}\right) \right] \geq 0 \text { and } \frac {\partial Z _ {\mathrm{TA}}}{\partial \operatorname{fac} _ {n i j}} \operatorname{fac} _ {n i j} = 0.\tag{6}
$$

For better understanding of the above relations, we provide a $4 { \times } 4$ system example in Appendix B.

In a case study of a three-node system, the model in Ref. [2] and our model produce the same equilibrium despite our differences in the TA problem formulation. We believe that if the TA is mandated to only relieve congestion on the network via assessing appropriate congestion charges, our TA’s problem formulations as a dispatcher or a revenue maximizer are equivalent. In either case, congestion charges are driven only by the physical properties of the network and thus whether the TA acts as a profit maximizer or a social planner, the same solution results as long as the TA is required to satisfy all trades requested by consumers and producers (subject to physical constraints). In addition to agent-specific constraints, system-wide constraints are presented below:

$$
\begin{array}{l} T \max _ {n} - \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left[ \left(\operatorname{fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\operatorname{fac} _ {(n + 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \geq 0: \theta_ {n \in \text {odd}} ^ {+} \\ T \max _ {n} - \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left[ \left(\operatorname{fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\operatorname{fac} _ {(n - 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \geq 0: \theta_ {n \in \text {even}} ^ {-} \\ \sum_ {s = 1} ^ {S} \sum_ {j = 1} ^ {N} \left[ f _ {i j s} \left(1 - \sum_ {n = 1} ^ {2 L} \alpha_ {n} \operatorname{fac} _ {n i j}\right) \right] \geq q _ {i}: \lambda_ {i} \end{array}\tag{7}
$$

$$
T \max _ {n} = T \max _ {n + 1} \text {   if   } n \text {   is   odd   }
$$

The first two constraints set the transmission limits on every line and the third constraint is the market balance condition.

## 3. An illustrative example and the results

In this example, we use a simplified (aggregated) model of the Indiana power grid. Service areas corresponding to major energy producers are modeled as nodes of the system with respective demand functions, supply functions, and equivalent transmission lines connecting the nodes. Fig. 1 displays the structure of the network.

First, we want to examine the impact of enforcing the DC power flow constraints on the market power and social welfare in the system. Models that do not decompose flows between nodes of the network into flows on individual lines ignore the interactions among various injections and load pairs that may create congestion on lines that has a pattern far different from their contractual path. That is, if we have injection and load at two neighboring nodes of the network, the load factor decomposition will show that real flow occurs not only between the two nodes, but also in other parts of the network. As a result, prices and regional consumption predicted on the same network via the load factor method and the more simple method can be significantly different (Table 1).

The model used to generate the results in the last two columns in Table 1 without load factor constraints is equivalent to the one used by Ref. [6]. We contrast it with a model that includes DC power flow constraints. It is apparent that despite using the same network, the two models produce significantly different results. Namely, if we do not account for physical flow constraints we exaggerate the competitiveness and the social welfare within the system. In the example presented here, adding the DC power flow constraints results in an increase in average price by 5.1% over the average price without the DC flow constraints. We also observe a greater variation in price with the DC flow constraints. In addition, the total consumption with the power flow constraints is about 2.6% lower than in the case where these physical constraints are excluded. Finally, we note that total consumer welfare is 5.1% lower when the DC power flow constraints are present in the model, and the producers’ profits are about 20% greater. Moreover, we see that, using DC power flow constraints changes, the consumer surplus differentially across the regions. In one region, the consumer surplus increased by 6.2% while at other nodes it decreased by more than 11%. Thus, from a policy evaluation and planning perspective, incorporation of the DC power flow constraint appears to be important.

In Table 2, we compare two models including DC power flow constraint but, with and without line losses. Whereas line losses ranged between 1.6% and 9.5% and averaged 4.9%, the prices in the model with line losses were from 4.4% to 13.5% higher than in the model with no line losses. In the example

![](/api/attachments/5DE9QRWJ/fulltext/images/397a992fe18ab2e4e36c393cc6aeb94b2f087741c5836a5750d5413fb685791c.jpg)  
Fig. 1. Model of Indiana’s electrical network, marginal cost of production in parentheses, size of nodes corresponds to generation capacity. PSI, Public Service of Indiana (generation capacity 5235 MW); SIG, Southern Indiana Gas and Electric (1181 MW); IPL, Indianapolis Power and Light (2578 MW); NIP, Northern Indiana Public Service (2938 MW); HER, Hoosier Energy Rural Electric Cooperative (1081 MW); IME, Indiana/Michigan Electric Power (5792 MW); MAIN, Mid-America Interconnected Networks (Demand only); ECAR, East Central Area Reliability Coordination Agreement (Demand Only). Indiana exports power to both ECAR and MAIN. Source: State Utility Forecasting Group, Purdue University, West Lafayette, IN.

presented above, the inclusion of line losses results in a general increase in regional electricity prices with an average price increase of 6.5%. In addition, the total consumption with line losses is 3.2% lower than in the case where they are omitted. Finally, the total consumer welfare is 6.4% lower when line losses are included in the model while the producers profits are 3% greater.

Table 1  
Regional electricity pricing with and without DC power flow constraints

<table><tr><td rowspan="2">Node</td><td colspan="2">With DC flow constraints</td><td colspan="2">Without DC flow constraints</td><td rowspan="2">Change in consumer surplus by node (%)</td></tr><tr><td>Price ($/MWh)</td><td>Consumption (MWh)</td><td>Price ($/MWh)</td><td>Consumption (MWh)</td></tr><tr><td>PSI</td><td>34.37</td><td>4343.41</td><td>33.76</td><td>4383.86</td><td>-1.84</td></tr><tr><td>SIG</td><td>31.15</td><td>753.08</td><td>33.19</td><td>730.78</td><td>6.20</td></tr><tr><td>IPL</td><td>35.65</td><td>2092.38</td><td>33.95</td><td>2147.62</td><td>-5.08</td></tr><tr><td>NIP</td><td>36.93</td><td>2095.68</td><td>32.93</td><td>2228.81</td><td>-11.59</td></tr><tr><td>HER</td><td>34.99</td><td>733.62</td><td>33.03</td><td>755.68</td><td>-5.75</td></tr><tr><td>IME</td><td>34.98</td><td>2824.60</td><td>33.54</td><td>2887.16</td><td>-4.29</td></tr><tr><td>ECR</td><td>36.79</td><td>2074.67</td><td>35.13</td><td>2129.00</td><td>-5.04</td></tr><tr><td>MAN</td><td>37.03</td><td>1515.17</td><td>32.99</td><td>1612.19</td><td>-11.67</td></tr><tr><td>Producer&#x27;s profits</td><td>331,859</td><td></td><td>275,588</td><td></td><td>20.42</td></tr><tr><td>Consumer welfare</td><td>530,821</td><td></td><td>559,594</td><td></td><td>-5.14</td></tr></table>

Table 2  
Regional electricity pricing with and without line losses

<table><tr><td rowspan="2">Node</td><td colspan="2">With line losses</td><td colspan="2">With no line losses</td><td rowspan="2">Change in consumer surplus by node (%)</td></tr><tr><td>Price ($/MWh)</td><td>Consumption (MWh)</td><td>Price ($/MWh)</td><td>Consumption (MWh)</td></tr><tr><td>PSI</td><td>34.37</td><td>4343.41</td><td>32.92</td><td>4439.14</td><td>-4.27</td></tr><tr><td>SIG</td><td>31.15</td><td>753.08</td><td>27.43</td><td>793.73</td><td>-9.98</td></tr><tr><td>IPL</td><td>35.65</td><td>2092.38</td><td>33.39</td><td>2165.77</td><td>-6.66</td></tr><tr><td>NIP</td><td>36.93</td><td>2095.68</td><td>34.25</td><td>2184.93</td><td>-8.00</td></tr><tr><td>HER</td><td>34.99</td><td>733.62</td><td>33.22</td><td>753.52</td><td>-5.21</td></tr><tr><td>IME</td><td>34.98</td><td>2824.60</td><td>33.11</td><td>2905.67</td><td>-5.50</td></tr><tr><td>ECR</td><td>36.79</td><td>2074.67</td><td>34.26</td><td>2157.74</td><td>-7.55</td></tr><tr><td>MAN</td><td>37.03</td><td>1515.17</td><td>34.25</td><td>1581.92</td><td>-8.26</td></tr><tr><td>Producer&#x27;s profits</td><td>331,859</td><td></td><td>322,024</td><td></td><td>3.05</td></tr><tr><td>Consumer welfare</td><td>530,821</td><td></td><td>566,911</td><td></td><td>-6.37</td></tr></table>

## 4. Conclusions

We formulate a model of real-time electricity markets that takes into account certain basic physical properties of electrical networks as well as government regulations in transmission pricing. By employing a Cournot–Nash framework, we have explored the market power and welfare effects of the physical properties of electrical networks. We have found in our example that both physical DC flow constraints and line losses are important in modeling electricity markets as noncooperative games. For example, if we are concerned about capacity expansion, then line losses are very important. If we are interested in mitigating market power, then power flow constraints are important. Line losses create a barrier to competition in the spatial electrical network thus enhancing market power of the producers. In our case study, DC power constraints also affected consumers’ welfare in a negative way. However, it would be useful to explore whether there are conditions under which DC power flow approximation can diminish market power and enhance consumers’ welfare.

With these results in mind, we can suggest several useful extensions of our work. Imposing AC power constraints or introducing quadratic thermal line losses over their linear approximation would most likely result in different (more realistic) market power effects. It would also be interesting to explore the effects of physical network constraints beyond the real-time framework into longer-term planning periods. Contract markets are a fundamental part of electricity market deregulation, so modeling them in a realistic physical framework would be beneficial to our understanding of market power issues in deregulated systems.

## Acknowledgements

Partial support for this research was provided by National Science Foundation Grant No. 0122207-DMI.

## Appendix A. Equivalence of TA profit maximizing and transmission operating efficiency objectives

The following argument is constructed using the model in Ref. [1], although it can be extended also to the model in Ref. [2]. The contrast is based on the assumption that there are no fixed wheeling charges. The TA objective is stated as: (1) $\begin{array} { r } { \mathrm { M a x i m i z e } _ { y _ { i j } } \sum _ { i j } w _ { i j } y _ { i j } } \end{array}$ subject to Kirchhoff’s laws, where $y _ { i j }$ is the paper flow (transmission service) controlled by the TA agent and $w _ { i j }$ is the congestion charge assessed to the paper flow from i to j (note this congestion charge is contract path specific). Furthermore, the market balancing conditions for the transmission services is (2) $\begin{array} { r } { \sum _ { s } ^ { \bar { S } } x _ { i j s } = y _ { i j } } \end{array}$ stating that the financial flows (sales) controlled by producers from i to j must equal the transmission services provided by the TA. Furthermore, because we know that the congestion charges (or the price differential) between two points can be rewritten as the sum of congestion charges on each line resulting from the particular financial/paper flow, we can rewrite the objective function as: (3) $\mathrm { m a x i m i z e } _ { \mathrm { f a c } _ { n i j } }$ $\begin{array} { r } { \sum _ { i j } \sum _ { n } \left( \mathrm { f a c } _ { i j n } \theta _ { n } \sum _ { s } x _ { i j s } \right) } \end{array}$ subject to Kirchoff’s laws where $\theta _ { n }$ is a congestion charge on line n and $\mathrm { f a c } _ { i j n }$ is the portion of sale $x _ { i j }$ actually flowing on line n. Note that the decision variable has changed from $y _ { i j }$ to $\mathrm { f a c } _ { i j n }$ because TA cannot control the sales of the power producers.

Kirchhoff’s laws can be approximated as a system of linear equations, whose solution is unique after a reference bus is chosen. Whether we state the TA agent’s objective function as (1), (3), or $\begin{array} { r } { \mathrm { M i n i m i z e } _ { \mathrm { f a c } _ { n i j } } \sum _ { n } ^ { 2 L } \dot { \sum _ { i } ^ { N } } \sum _ { j } ^ { N } \mathrm { f a c } _ { n i j } . } \end{array}$ , as we do in our model, the objective function is constrained by a system of equations with a unique solution. Thus, whether the decision variable is $y _ { i j }$ (paper flows) or fac (load factors), there is only one feasible solution for a given physical network. Thus, whether the TA is a maximizer of revenue, or minimizes total transportation is irrelevant as long as laws of physics are enforced.

## Appendix B. A four-node example of load factor calculations

We use the methodology of Ref. [4] to compute the DC load factors. To get the set of load factors, we have to solve a system of linear equations. These equations reflect the physics laws of electric power transmission. They are the current law and the voltage law, and linear line losses are incorporated in these equations. The solution to this system is unique if we can show that the Kirchoff’s equation matrix is nonsingular after a reference is chosen. After we defined the power grid properly, we can be assured of its uniqueness.<sup>2</sup> The following is the system of relations that solves load factors for a simple four-node system.

Fig. B1 shows a simple four-node system with two defined loops. We will need five relationships to define the Kirchhoff relationships: two-loop (voltage law) equations and three-node (current law) equations. We only need three current law equations to achieve unique

solution; thus, we arbitrarily drop the current law equation referring to the D node. Following is the matrix (kirmatrix) defining the appropriate Kirchhoff’s relations:

<table><tr><td> $Kirmatrix_{vn}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td> $bmatrix_{vAB}$ </td></tr><tr><td> $CurrentA$ </td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>-1</td><td>0</td><td>0</td><td>-1</td></tr><tr><td> $CurrentB$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>-1</td><td>1</td><td>+1</td></tr><tr><td> $CurrentC$ </td><td>0</td><td>0</td><td>1</td><td>-1</td><td>-1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $Loop1$ </td><td> $-x_1$ </td><td> $x_1$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td> $-x_4$ </td><td> $x_4$ </td><td> $x_5$ </td><td> $-x_5$ </td><td>0</td></tr><tr><td> $Loop2$ </td><td>0</td><td>0</td><td> $x_2$ </td><td> $-x_2$ </td><td> $x_3$ </td><td> $-x_3$ </td><td>0</td><td>0</td><td> $x_5$ </td><td> $-x_5$ </td><td>0</td></tr></table>

(B1)

The bmatrix in the above example is the one used to determine load factors for sales from node A to node B (we withdraw one unit from node A 1) and ship it to node B (+1)). We solve the above system for all pairs of nodes. Following is the rest of the bmatrix for sales from node A for the fournode example. The index x denotes reactances on connections 1 through 5 used to compute the solutions for the voltage law equations. The rest of the matrix for sales from B, C, and D is constructed similarly:

<table><tr><td>Bmatrix</td><td> $A \rightarrow A$ </td><td> $A \rightarrow B$ </td><td> $A \rightarrow C$ </td><td> $A \rightarrow D$ </td></tr><tr><td>CurrentA</td><td>0</td><td>-1</td><td>-1</td><td>-1</td></tr><tr><td>CurrentB</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>CurrentC</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Loop1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Loop2</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

(B2)

To add line losses, we create a lossmatrix, which indicates where line losses are to be applied:

<table><tr><td> $Lossmatrix_{vn}$ </td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td> $blossmatrix_{vAB}$ </td></tr><tr><td>CurrentA</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>CurrentB</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>CurrentC</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Loop1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Loop2</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr></table>

(B3)

![](/api/attachments/5DE9QRWJ/fulltext/images/009f5b5aad812832efbf8867be4ee33b71122872a0930d5350f9c58777dfc697.jpg)  
Fig. B1. An illustrative example.

The blossmatrix is the same as the bmatrix except for all the negative entries are replaced with zeros. To solve for the load factors, we thus have the following constraint:

$$
\begin{array}{l} \sum_ {n = 1} ^ {2 L} (\text { kirmatrix } _ {v n} - \alpha_ {n} \text { lossmatrix } _ {v n}) \text { fac } _ {n i j} \\ = \text { bmatrix } _ {v i j} - \text { glossmatrix } _ {v i j} \sum_ {n = 1} ^ {2 L} \alpha_ {n} \text { fac } _ {n i j} \end{array}\tag{B4}
$$

On the left side of the system, we apply the line losses to both the current and voltage law equations to reflect that the volume electricity exiting the line is reduced by an The right side recognizes that the total electricity delivered from point A to B is reduced by the sum of thermal line losses, weighted by the load factors, on each line where the sale creates real flows.

The resulting set of factors will satisfy all the physical conditions of the network. An extension to this approach would be to model quadratic line losses, which would result in different factors depending on the level of sales in the system. The challenge for this task is not modeling the nonlinear physical line losses in the system, but the accounting for line losses in the financial flows. For now, although, we assume that linear line losses are a good approximation.

## Appendix C. Discussion of the uniqueness of the solution

We have argued that the TA problem has a unique solution after a reference node is chosen (discussion is provided later in this appendix). Thus, to show that the full model has a unique solution means to show that the solutions to the producers’ and consumers’ problems are unique. We can prove uniqueness of the solutions to the consumer’s and producer’s problem by showing that the Jacobian of the MCP problem at hand is identical to the first-order conditions of the following QP:

$$
\underset {q _ {i}, f _ {i j s}} {\text { MIN }} \sum_ {i = 1} ^ {N} \left(\left[ - a _ {i} - \frac {1}{2} b _ {i} q _ {i} \right] q _ {i}\right) + \sum_ {s = 1} ^ {S} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left\{- \frac {1}{2} b _ {j} \left(f _ {i j s}\right) ^ {2} + d _ {i s} f _ {i j s} + \sum_ {n = 1} ^ {2 L} w _ {n} \operatorname{fac} _ {n i j} f _ {i j s} \right\}
$$

Subject to:

$$
\begin{array}{l l} P \max _ {i s} - \sum_ {j = 1} ^ {N} f _ {i j s} \geq 0 & (\rho_ {i s}) \forall i, s \\ T \max _ {n} - \sum_ {i} ^ {N} \sum_ {j} ^ {N} \left[ \left(\operatorname{fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\operatorname{fac} _ {(n + 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \geq 0 & (\theta_ {n} ^ {+}) \forall n \\ T \max _ {n} - \sum_ {i} ^ {N} \sum_ {j} ^ {N} \left[ \left(\operatorname{fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\operatorname{fac} _ {(n - 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \geq 0 & (\theta_ {n} ^ {-}) \forall n \\ \sum_ {s = 1} ^ {S} \sum_ {j = 1} ^ {N} f _ {j i s} \geq q _ {i} (\lambda_ {i}) \forall i \end{array}\tag{C1}
$$

Note that this QP is not necessarily addressing a specific economic problem. It is used as a mathematical tool to prove uniqueness of the gaming model. We can rewrite the QP in the complete Lagrangian form as:

$$
\begin{array}{l} L = \sum_ {i = 1} ^ {N} \left(\left[ - a _ {i} - \frac {1}{2} b _ {i} q _ {i} \right] q _ {i}\right) + \sum_ {s = 1} ^ {S} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left\{- \frac {1}{2} b _ {j} (f _ {i j s}) ^ {2} + d _ {i s} f _ {i j s} + \sum_ {n = 1} ^ {2 L} w _ {n} \text {fac} _ {n i j} f _ {i j s} \right\} \\ - \sum_ {i = 1} ^ {N} \lambda_ {i} \left(\sum_ {s = 1} ^ {S} \sum_ {j = 1} ^ {N} f _ {j i s} - q _ {i}\right) - \sum_ {n = 1} ^ {2 L} \theta_ {n} ^ {+} \left\{T \max _ {n} - \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left[ \left(\text {fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\text {fac} _ {(n + 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \right\} \\ - \sum_ {n = 1} ^ {2 L} \theta_ {n} ^ {-} \left\{T \max _ {n} - \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} \left[ \left(\text {fac} _ {n i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) - \left(\text {fac} _ {(n - 1) i j} \sum_ {s = 1} ^ {S} f _ {i j s}\right) \right] \right\} \\ - \sum_ {s = 1} ^ {S} \sum_ {i = 1} ^ {N} \rho_ {i s} \left(P \max _ {i s} - \sum_ {j = 1} ^ {N} f _ {i j s}\right) \end{array} \tag {C2}
$$

Recognizing that in the equilibrium $\begin{array} { r } { \lambda _ { i } = a _ { i } + \frac { 1 } { 2 } b _ { i } q _ { i } } \end{array}$ and that $\begin{array} { r } { \sum _ { j = 1 } ^ { N } \sum _ { s = 1 } ^ { S } f _ { j i s } = q _ { i } } \end{array}$ , we next show that the firstorder conditions for this QP problem are identical to the first-order conditions of the consumer’s and the producer’s problem. It is straightforward to show that the partial derivative of L with respect to $q _ { i }$ will result in the FOCs of the consumers. Likewise, the partial derivative of L with respect to $f _ { i j s }$ results in the FOCs of the producers.

From the properties of QP, we know that, if a QP problem is a strictly convex programming, then the solutions for sales and quantity demanded variables are unique. Looking at the Jacobian matrix (the one that excludes the factor load and pseudo TA equations and their associated variables), we see that this problem is indeed convex programming in $q _ { i }$ and $f _ { i j s }$ values if the solution space is nonempty. Furthermore, also the $\lambda _ { i }$ values are unique because the consumers’ demand functions are continuous and strictly decreasing.

We have shown that our reduced problem without the TA subproblem has a unique solution and now will assert that this also means that the full problem has a unique solution. We have excluded the TA problem from the rest of the model because we claim that TA’s decision variables (the load factors) are uniquely determined by the physics of the network as shown previously and thus are mere parameters in the full problem. We can strengthen our assertion of uniqueness of the solution to the TA’s problem (solving for $\mathrm { f a c } _ { n i j } )$ because we realize that the two sets of variables $\operatorname { f a c } _ { n i j }$ and $\delta _ { l i j }$ are not really variables in the gaming model. We can therefore pull the entire problem of determining factor loads out of the system because we observe that both $\operatorname { f a c } _ { n i j }$ and $\delta _ { l i j }$ are determined by the physical properties of the network and are independent of all decision variables.<sup>3</sup>

We can verify that by looking at the set of Kirchhoff’s equalities along with the pseudo TA problem’s first-order conditions: $\begin{array} { r } { \sum _ { n } ^ { 2 L } \left( \mathrm { k i r m a t r i x } _ { \nu n } \right) \tilde { \mathrm { f a c } } _ { n i j } - \mathrm { b m a t r i x } _ { \nu i j } = 0 \mathrm { a n d } \tilde { \mathsf { \Gamma } } _ { 0 } ^ { \mathsf { a } } ( . ) } \\ { \sum _ { n } ^ { 2 L } \left( \mathrm { k i r m a t r i x } _ { \nu n } \right) \tilde { \mathrm { f a c } } _ { n i j } - \mathrm { b m a t r i x } _ { \nu n } ] } \end{array}$ with the restriction that fa $_ { \mathrm { { n } i j } } { \geq } 0$ . The Kirchoff’s equalities give a unique solution to the net load factors; that is, they can be either positive or negative. Because we want the factors to be only positive (in order to model line losses), we created a <sup>d</sup>double<sup>T</sup> for each line. Thus, a line between some nodes A and B is virtually divided between line 1 for all the flows in one direction and line 2 for the flows in the opposite direction. When we are computing the load factors for a given connection, we want the factor on one virtual line of the connection to be positive and the other to be zero. If we do not force this relationship, then we cannot achieve uniqueness in load factors because there is an infinite number of combinations of load factors that would add up to the unique net factor: $\mathrm { f a c } _ { n i j } - \mathrm { f a c } _ { ( n + I ) i j } \mathrm { : }$ =netfacto $\mathrm { \Delta } \mathrm { r } _ { l i j }$ where l is the connection described by both n and n+1. A trick is necessary to furnish this relationship: We want to ask the TA to minimize the total value of factors in the system subject to constraints. By doing so, there is only one combination of load factors on a given connection that equals the unique net load factor on the connection and that is also of lowest value of the sum of the absolute values of both load factors. Hence, if we accept that the net load flows on every line are unique, so there must be the individual load flows associated with it.

Table C1 The Jacobian of the mixed complementarity problem

<table><tr><td>Jacobian matrix</td><td> $q_{i}$ </td><td> $f_{ijs}$ </td><td> $\theta_{n\in odd}^{+}$ </td><td> $\theta_{n\in evev}^{-}$ </td><td> $\lambda_{i}$ </td><td> $\rho_{is}$ </td><td> $fac_{nij}$ </td><td> $\delta_{lij}$ </td></tr><tr><td> $\partial q_{I}$ </td><td> $-b_{i}$ </td><td></td><td></td><td></td><td>1</td><td></td><td></td><td></td></tr><tr><td> $\partial f_{ijs}$ </td><td></td><td> $-b_{j}$ </td><td> $fac_{nij}-fac_{(n+1)ij}$ </td><td> $fac_{nij}-fac_{(n-1)ij}$ </td><td>-1</td><td>1</td><td></td><td></td></tr><tr><td> $T\max_{n}^{+}$ </td><td></td><td> $-(fac_{nij}-fac_{(n+1)ij})$ </td><td></td><td></td><td></td><td></td><td> $\sum_{i}\sum_{j}\sum_{s}f_{ijs}$ </td><td></td></tr><tr><td> $T\max_{n}^{-}$ </td><td></td><td> $-(fac_{nij}-fac_{(n-1)ij})$ </td><td></td><td></td><td></td><td></td><td> $\sum_{i}\sum_{j}\sum_{s}f_{ijs}$ </td><td></td></tr><tr><td> $SD_{I}$ </td><td>-1</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $P\max_{is}$ </td><td></td><td>-1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\partial fac_{nij}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td> $-\sum_{v}kirmatrix_{vn}$ </td></tr><tr><td> $Kir_{lij}$ </td><td></td><td></td><td></td><td></td><td></td><td> $kirmatrix_{vn}$ </td><td></td><td></td></tr></table>

Table C2 The Jacobian of MCP after presolving for load factors

<table><tr><td>Jacobian matrix</td><td> $q_I$ </td><td> $f_{ijs}$ </td><td> $\theta_{n\in odd}^{+}$ </td><td> $\theta_{n\in\text{evev}}^{-}$ </td><td> $\lambda_i$ </td><td> $\rho_{is}$ </td></tr><tr><td> $\partial q_i$ </td><td> $-b_I$ </td><td></td><td></td><td></td><td>1</td><td></td></tr><tr><td> $\partial f_{ijs}$ </td><td></td><td> $-b_j$ </td><td> $fac_{nij}-fac_{(n+1)ij}$ </td><td> $fac_{nij}-fac_{(n-1)ij}$ </td><td>-1</td><td>1</td></tr><tr><td> $T\max_n^+$ </td><td></td><td> $-(fac_{nij}-fac_{(n+1)ij})$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $T\max_n^-$ </td><td></td><td> $-(fac_{nij}-fac_{(n-1)ij})$ </td><td></td><td></td><td></td><td></td></tr><tr><td> $SD_i$ </td><td>-1</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td> $P\max_{is}$ </td><td></td><td>-1</td><td></td><td></td><td></td><td></td></tr></table>

## References

[1] B.F. Hobbs, LCP models of Nash–Cournot competition in bilateral and POOLCO-based power markets, Proceedings of IEEE Power Engineering Society, 1999 (Winter).

[2] B.F. Hobbs, Linear complementarity models of Nash–Cournot competition in bilateral and POOLCO power markets, IEEE Transactions on Power Systems 16 (2) (2001) 194 – 202.

[3] W.W. Hogan, A market power model with strategic interaction in electricity networks, The Energy Journal 18 (4) (1997) 107 – 141.

[4] W.W. Hogan, Flowgate rights and wrongs, MEET Conference, Stanford, CA, 2000, pp. 102 – 112 (August 19).

[5] R. Kamat, S.S. Oren, Two Settlement Systems for Electricity Markets: Zonal Aggregation Under Network Uncertainty and Market Power, POWER Working Paper, University of California Energy Institute (2002).

[6] J. Wei, Y. Smeers, Spatial oligopolistic electricity models with Cournot generators and regulated transmission prices, Operations Research 47 (1) (1999)

![](/api/attachments/5DE9QRWJ/fulltext/images/fd24fe9500a3f4fb02e6d2b068e279e55e020b5e1b7c01ff38265f4054fe5c2e.jpg)  
Rastislav Ivanic is currently a graduate student in the Department of Agricultural Economics at Purdue University. His research interest is in electricity markets design. He holds a B.A. in economics from Furman University and an M.S. in economics and an M.B.A. from Purdue University.

![](/api/attachments/5DE9QRWJ/fulltext/images/f3d9a523d6d611962c7da26b3857e9e8ce2d5b00863d53282bd1090c586a5f73.jpg)

Dr. P. Preckel holds a B.S. in Mathematical Sciences from Ohio State University, and an M.S. and Ph.D. in Operations Research from Stanford University. He is currently Professor and Associate Department Head of Agricultural Economics at Purdue University. He researches and teaches in the areas of decision analysis and mathematical modeling. He has had extensive experience in developing applications and methods over a wide range of

subject matter areas. His current areas of interest are focused on assessment of the effects of policy across an economy’s income spectrum, modeling imperfectly competitive markets, supply chain management, and applications and methods for optimization and numerical integration.

Dr. Zuwei Yu received his Ph.D. in Electrical Engineering in 1995 from the University of Oklahoma, with a minor in Operations ResearchMathML:/mathematical Programming. He is an associate professor of courtesy appointment at Purdue University and a senior analyst with the Indiana State Utility Forecasting Group. His current research interests include mathematical programming, economics, decision analysis and gaming modeling with applications to energy industry, and other areas as well.
