---
otero_id: 5406
otero_key: "DM4CWEBJ"
title: "Bidding strategies in dynamic electricity markets"
authors: "Ashkan R. Kian; Jose B. Cruz"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bidding strategies in dynamic electricity markets

Ashkan R. Kian<sup>a,\*</sup>, Jose B. Cruz Jr.<sup>b</sup>

<sup>a</sup>Dept. of ECE, Faculty of Engineering, University of Tehran, Iran <sup>b</sup>205 Dreese Lab., Electrical Engineering Dept., Ohio State University, Columbus, Ohio 43210, United States

## Abstract

In this paper the problem of developing bidding strategies for the participants of dynamic oligopolistic electricity markets is studied. Attention is given to strategic bidding of load serving entities (LSE) in these markets. We model oligopolistic electricity markets as non-linear dynamical systems and use discrete-time Nash bidding strategies. We assume a Cournot model for our game, where the LSEs decide on demand quantities and the market price is the marginal cost of producing electricity.

Attention is given to a problem, where the objective functions are quadratic in the deviations of trajectories from desired trajectories and quadratic in the control deviations from the nominal controls. It is assumed that each power marketer can estimate his/her competitors’ benefit function coefficients.

The optimal bidding strategies are developed mathematically using dynamic game theory. We deal with games that are nonlinear in the state equations. We linearize these equations for complex non-linear oligopolistic electricity multi-markets and use discrete-time Nash strategies. We show that the actual dynamic excursions from the operating point where we linearize are small so that the linearization is valid. The developed algorithm is applied to an IEEE 14-bus power system. We show that the LSEs’ expected profits are higher for our method than those for other methods in the literature (F. Wen, A.K. David, Optimal bidding strategies and modeling of imperfect information among competitive generators. IEEE Transactions on Power Systems, Vol. 16, No. 1, pp.15–21, Feb. 2001.

Keywords: Bidding strategies; Oligopolistic electricity markets; Nash tracking games; Desired load trajectories

## 1. Introduction

A percentage of the electricity markets in the United States are based on auctions mechanisms. An auction is a market institution with an explicit set of rules determining resource allocation and prices on the basis of bids from the market participants. The auction mechanism has been a preferred choice of setting prices for electricity markets. It is an economically efficient mechanism to allocate demand to suppliers. For example, California market participants submits supply and demand bid curves for the dayahead and hour-ahead energy markets in sealed bid format. Then, aggregated hourly supply and demand bid curves are constructed to determine market clearing prices as well as the corresponding supply and demand schedules. A marginal clearing price is set at the intersection point between the aggregated demand and supply curves for each of the 24 scheduling hours. All generators winning the auction are paid at the uniform clearing.

In this paper the problem of developing bidding strategies for the participants of dynamic oligopolistic electricity markets is studied. Attention is given to strategic bidding of load serving entities (LSE) in these markets. We model oligopolistic electricity markets as non-linear dynamical systems and use discrete-time Nash bidding strategies. We assume a Cournot model for our game, where the LSEs decide on demand quantities and the market clearing-price is the marginal cost of producing electricity. Dynamic non-cooperative games and Nash strategies are introduced and discussed about in [1], [2] and [8].

The rest of the paper is organized as follows: Section 2 covers the literature review. In Section 3, we formulate the problem mathematically. In Section 4, a numerical example of the proposed method is presented. Section 5 concludes the paper.

## 2. Literature review

Researchers [3–7,11–13] have shown that demandelasticity, market share and strategic behavior have the major effects on price volatilities in electricity multimarkets. One of the ways of controlling price volatility is to design demand management programs for consumers of electricity. Fahrioglu and Alvarado [4,5] consider and describe a variety of voluntary demand management programs, including full interruption, equipment specific partial interruptions and programs that guarantee a certain <sup>b</sup>relief performance<sup>Q</sup>. The authors define, consider and compare three types of demand management programs:

<sup>!</sup> Firm Power Level Program, which defines a maximum power level (FPL) for each customer. During an interruption request the customers in this program are required to reduce their demand to their pre-agreed FPL or below.

<sup>!</sup> Agreed Relief Program, which has some similarities with the FPL program. When customers receive a relief request, they shed a predetermined amount of load from their demand level at the time of the curtailment request and have a sloping upper limit to their demand pickup during the requested curtailment period. After the curtailment ends they may resume their typical demand.

<sup>!</sup> Equipment Specific Interruption Program is different in a sense that there are no parameters to decide upon. However, the customer can decide what equipment to shut off upon request. Air conditioners and heaters would be among the best candidates since they put a big burden on the utility.

The authors use a concept from Game Theory called <sup>b</sup>mechanism design<sup>Q</sup> to develop demand management contracts for the power utilities based on their customer willingness to shed load. Their demand management contracts are largely governed by customer type (willingness to shed load) and customer location. Locational value of each customer is calculated using sensitivity method (sensitivity of line flows to individual loads). Some customers are at more critical locations than the others that make them more important for the power utilities to sign interruptible load contracts with them.

Visudhiphan and Illic [12] have introduced dynamic bidding models for representing possible behavior of rational profit-maximizing generators responding to the electricity price variation in a simplified poolco-type electricity market. The emphasis of their work is to address mechanisms and critical factors that enable generators (Gencos) to exert market power during the bidding process. They have shown that in electricity markets with price-inelastic loads, generators will attempt to game the market extensively. With the aid of a dynamic bidding model, they have analyzed the effect of generators bidding strategies on the market-clearing price. Two types of generator supply functions are considered in this research work: (1) Single-step Supply Function (SSF) and (2) Linear Supply Function (LSF). The authors have studied two possible strategies for power generators:

(1) Estimated Profit Maximization (EPM): In this strategy the generator will increase its offer price in his next bid if the expected (estimated) profit of the next period is larger than the profit of the current period.

(2) Competition to be a Base-Load Generator (CBG): In this strategy the base-load generator offering the lowest bid is scheduled at each hour for power generation by the ISO.

Based on their simulation results, the marketclearing price will be lower when the generators adopt the CBG strategy rather than EPM strategy.

Skantze and Chapman [11] have shown some of the complexity related to the bidding of electric power in a deregulated market. They use California system to examine the price dynamics of electric power. They define a new index to measure the existence of market power. This index is derived specifically for electric power markets, taking into account the nature of generators operating costs. The first challenge of understanding price dynamics in electric power markets is to identify the forces driving up the cumulative supply curves. The second is to quantify and estimate them. The authors consider three possible causes for shifts in supply curve:

(1) Generator Outages: If a generator is off line due to faults or service requirements, its bid curve is withheld from the market, shifting the cumulative supply curve to the left.

(2) Market entry or exit: A new generator entering the market, either from a competing power exchange or a terminated bilateral contract will shift the supply curve to the right. Similarly generators exiting the Power Exchange (PX) markets will shift the supply curve to the left.

(3) Gaming and strategic bidding: Generators with significant market share may attempt to increase profits by shifting their bid curves to the left, thus driving up the market clearing price.

Wen and David [13] have presented a method to build optimal bidding strategies for competitive power suppliers in an electricity market. They assume that power suppliers are required to bid a linear supply function. If the market operator selects their bids they will be paid the market-clearing price. They have developed a stochastic optimization model to compute the optimal bidding strategies for power suppliers. They also model the imperfect information about rivals as random variables with known probability distributions and known minimum–maximum values.

Their simulation results show that market-clearing price can be higher than the competitive level if the suppliers bid strategically. But, the suppliers’ market power will be reduced if the demand elasticity increases.

Schuler [10] introduced the importance of the speed of customer responses in gauging the competitiveness of oligopolistic markets. He develops economic rationale for a lagged response by customers buying from spatial markets. His emphasis is on two lag mechanisms: (1) possible delays in the digestion of information about changes in product prices; (2) delay in action by consumers after the information is received. He formulated a two-player non-cooperative game with concave adjustment process (CAP) and logistic adjustment process (LAP). The simulation results showed that as market shares become more nearly equal in a world of rapid feasible consumer changes in suppliers, the possibility of unstable market conditions might increase.

Maiorano, Song and Trovata [9] proposed a dynamic oligopolistic market model to analyze the new competitive electricity environment. Their model was developed on the basis of the well-known Cournot model for the analysis of a non-collusive oligopolistic market. Their first objective was to evaluate the reaction functions of the suppliers who share the market. A reaction function evaluated the expected profit-maximizing level of the power output for each generating firm (Genco), given the expected values of its rivals’ power outputs. They claimed their market model is dynamic but they solve a series of static optimization (profit-maximizing) problems for three competing Gencos over ten bidding periods. They showed how the behavior of Gencos affected their rivals’ profit maximization.

Given the above background about strategic bidding and demand management in new electricity market environment, the aim of this paper is to develop bidding strategies for load serving entities (power utilities) in dynamic oligopolistic electricity multi-markets. Dynamic modeling of the oligopolistic electricity markets could provide additional insights to the behavior and stability of these markets. The above task is a novel approach for developing bidding strategies for power utilities (LSEs) in new emerged oligopolistic electricity multi-markets and cannot be found in the literature.

## 3. Problem formulation

The focus of this paper is to develop bidding strategies for LSEs in oligopolistic electricity markets. We will use demand-elasticity as the control variable to achieve optimal demand bids for the LSEs. Attention is given to a problem where the objective functions are quadratic in the deviations of trajectories from desired trajectories and quadratic in the control deviations from the nominal controls. This is called a tracking problem. In this paper we deal with discrete-time dynamic games that are nonlinear in the state equations. Therefore, we extend the existing theory for linear-quadratic tracking games to discrete-time non-linear-quadratic tracking games. Our approach is to linearize the non-linear state equations with respect to the state variables and controls of all players at each desired operating point. We expect that the actual dynamic excursions from the operating point where we linearize will be small so that the linearization is valid. In our simulations, we compare the desired trajectories with the optimal linearized-state trajectories to show the validity of linearization process (refer to Fig. 5). Consider the following discrete-time non-linearquadratic tracking game:

$$
\begin{array}{l} J _ {k} ^ {i} (x _ {k}) = \big (x _ {N} - x _ {N} ^ {d} \big) ^ {\prime} Q _ {N} ^ {i} \big (x _ {N} - x _ {N} ^ {d} \big) \\ \qquad + \sum_ {j = k} ^ {N - 1} \Big \{\Big (x _ {j} - x _ {j} ^ {d} \Big) ^ {\prime} Q _ {j} ^ {i} \Big (x _ {j} - x _ {j} ^ {d} \Big) \\ \qquad + \Big (u _ {j} ^ {i} - u _ {j} ^ {i d} \Big) ^ {\prime} R _ {j} ^ {i} \Big (u _ {j} ^ {i} - u _ {j} ^ {i d} \Big) \Big \} \end{array}\tag{1}
$$

for $i { = } 1 , \ldots$ np

$$
x _ {k + 1} = f _ {k} \left(x _ {k}, u _ {k} ^ {1}, \dots , u _ {k} ^ {n p}\right)\tag{2}
$$

where $J _ { k } ^ { i } ( x _ { k } )$ is the additive quadratic objective function of player $i { \bf \ ( } i { = } 1 , \ldots , n p )$ , matrices $\mathcal { Q } _ { j } ^ { i } , \ R _ { j } ^ { i }$ are symmetric and positive definite for all $j { \in } [ 0 \small J ]$ $x _ { j } ^ { d }$ are the desired state values for $j { \in } [ 0 , N ] , u _ { j } ^ { d } { = } [ u _ { j } ^ { 1 d } ,$ $\lambda _ { j } ^ { ' 2 d } , . . . , u _ { j } ^ { n p d } ]$ are the desired control values for $j { \in } [ 0 ,$ $\dot { N } { - } 1 ]$ (which can be calculated algebraically if the desired state values are known), and $f _ { k } ~ ( x _ { k } , ~ u _ { k } ^ { 1 } , . . . ,$ $u _ { k } ^ { n p } )$ are the set of non-linear dynamic state equations of the states $( x _ { k } )$ and players’ controls $( u _ { k } ^ { i } , \ i { = } 1 , \ldots ,$ np). The optimal Nash-Cournot strategies $( u _ { k } ^ { * } { = } [ u _ { k } ^ { 1 * }$ $u _ { k } ^ { 2 } { * } _ { , \cdot \cdot \cdot } , u _ { k } ^ { n p } { * } _ { ] ) }$ of the above discrete-time non-linearquadratic tracking game should satisfy the following inequalities:

$$
\begin{array}{l} J _ {k} ^ {i} \left(x _ {k}, u _ {k} ^ {1 *}, \dots , u _ {k} ^ {i *}, \dots , u _ {k} ^ {n p *}\right) \leq J _ {k} ^ {i} \left(x _ {k}, u _ {k} ^ {1 *}, \dots , u _ {k} ^ {i}, \dots , u _ {k} ^ {n p *}\right), \\ \forall u _ {k} ^ {i} \in U ^ {i} \end{array} \tag {3}
$$

for $i { = } 1 , . . . , n p ;$ where, $U ^ { i }$ is the set of all admissible controls (strategies) for player i.

The linearized state equations are as follows:

$$
\delta x _ {k + 1} = A _ {k} \delta x _ {k} + B _ {k} ^ {1} \delta u _ {k} ^ {1} + \dots + B _ {k} ^ {n p} \delta u _ {k} ^ {n p}
$$

$$
A _ {k} = \frac {\partial f _ {k}}{\partial x _ {k}} \bigg | _ {x _ {k} = x _ {k} ^ {d}, u _ {k} = u _ {k} ^ {d}}\tag{4a}
$$

ð4bÞ

$$
B _ {k} ^ {i} = \frac {\partial f _ {k}}{\partial u _ {k} ^ {i}} \Bigg | _ {x _ {k} = x _ {k} ^ {d}, u _ {k} = u _ {k} ^ {d}}, \text {   for   } i = 1, \dots , n p\tag{4c}
$$

By applying the linearization process, the tracking problem becomes a regulator problem (driving the state deviations from the desired state values to zero by optimally calculating the control deviations from the desired controls) as follows:

$$
\begin{array}{l} J _ {k} ^ {i} (\delta x _ {k}) = \delta x _ {N} ^ {\prime} Q _ {N} ^ {i} \delta x _ {N} \\ \qquad + \sum_ {j = k} ^ {N - 1} \left\{\delta x _ {j} ^ {\prime} Q _ {j} ^ {i} \delta x _ {j} + \delta u _ {j} ^ {i ^ {\prime}} R _ {j} ^ {i} \delta u _ {j} ^ {i} \right\} \end{array}\tag{5}
$$

The optimal Nash strategies for the tracking problem are determined by the following equations:

$$
u _ {k} ^ {*} = L _ {k} \delta x _ {k} + u _ {k} ^ {d} = \delta u _ {k} ^ {*} + u _ {k} ^ {d}\tag{6a}
$$

$$
L _ {k} = - \psi_ {k} ^ {- 1} \zeta_ {k}\tag{6b}
$$

where,

$$
\psi_ {k} = \left[ \begin{array}{c c c c} R _ {k} ^ {1} + B _ {k} ^ {1 ^ {\prime}} K _ {k + 1} ^ {1} B _ {k} ^ {1} & B _ {k} ^ {1 ^ {\prime}} K _ {k + 1} ^ {1} B _ {k} ^ {2} & \ldots & B _ {k} ^ {1 ^ {\prime}} K _ {k + 1} ^ {1} B _ {k} ^ {n p} \\ B _ {k} ^ {2 ^ {\prime}} K _ {k + 1} ^ {2} B _ {k} ^ {1} & R _ {k} ^ {2} + B _ {k} ^ {2 ^ {\prime}} K _ {k + 1} ^ {2} B _ {k} ^ {2} & \ldots & B _ {k} ^ {2 ^ {\prime}} K _ {k + 1} ^ {2} B _ {k} ^ {n p} \\ . & . & \ldots & . \\ . & . & \ldots & . \\ . & . & \ldots & . \\ B _ {k} ^ {n p ^ {\prime}} K _ {k + 1} ^ {n p} B _ {k} ^ {1} & B _ {k} ^ {n p ^ {\prime}} K _ {k + 1} ^ {n p} B _ {k} ^ {2} & \ldots & R _ {k} ^ {n p} + B _ {k} ^ {n p ^ {\prime}} K _ {k + 1} ^ {n p} B _ {k} ^ {n p} \end{array} \right]\tag{7}
$$

$$
\zeta_ {k} = \left[ \begin{array}{c} B _ {k} ^ {1 ^ {\prime}} K _ {k + 1} ^ {1} \\ B _ {k} ^ {2 ^ {\prime}} K _ {k + 1} ^ {2} \\ \vdots \\ B _ {k} ^ {n p ^ {\prime}} K _ {k + 1} ^ {n p} \end{array} \right] A _ {k}\tag{8}
$$

and matrices $K _ { k } ^ { i } ( i { = } 1 , . . . , n p )$ are computed by the following Riccati-like equations:

$$
K _ {N} ^ {i} = Q _ {N} ^ {i}\tag{9a}
$$

$$
\begin{array}{l} K _ {k} ^ {i} = Q _ {k} ^ {i} + L _ {k} ^ {i ^ {\prime}} R _ {k} ^ {i} L _ {k} ^ {i} \\ \quad + \left(A _ {k} + \sum_ {j = 1} ^ {n p} B _ {k} ^ {j} L _ {k} ^ {j}\right) ^ {\prime} K _ {k + 1} ^ {i} \left(A _ {k} + \sum_ {j = 1} ^ {n p} B _ {k} ^ {j} L _ {k} ^ {j}\right) \end{array}\tag{9b}
$$

for $k { = } 1 , . . . , N { - } 1$

The optimal costs-to-go at time step k (for the regulator problem) can be computed by the following equation:

$$
J _ {k} ^ {i ^ {*}} (\delta x _ {k}) = \delta x _ {k} ^ {\prime} K _ {k} ^ {i} \delta x _ {k}, \qquad i = 1, \ldots , n p\tag{10}
$$

The dimensions of $x _ { k } , x _ { k } ^ { d } , u _ { k } , u _ { k } ^ { d }$ are $n \times 1 , \ n \times 1$ $1 \times p , ~ 1 \times p$ , respectively. Matrices $A _ { k } , \ B _ { k } ^ { i } , \ Q _ { k } ^ { i } , \ R _ { k } ^ { i }$ $( i { = } 1 , . . . . , n p )$ have proper dimensions.

## 4. Numerical example

In this section, the developed algorithm of Section 3 is used to compute optimal bidding strategies for three competing LSEs in four interconnected zonal oligopolistic electricity markets (IEEE14-bus power system) as shown in Fig. 1. It is assumed that each LSE has market share at each zone (price area). The LSEs play a Nash game (non-cooperative game) among each other to buy electricity from the zonalmarkets. In order to conserve energy (and basically hedge against price volatility), LSEs sign loadleveling contracts with their customers at each zone based on pre-agreed incentive discounts for each kW h of load curtailment [4,5]. Therefore, each LSE starts the game knowing its desired load profile (over a 24-h period) to track. We assume that each LSE has a linear demand function defined as following:

$$
d _ {k} ^ {i} = D _ {0} ^ {i} - \alpha_ {k} ^ {i} \lambda_ {k}, \qquad i = 1, 2, 3\tag{11}
$$

where, $d _ { k } ^ { i }$ is the hourly demand (MW), $D _ { 0 } ^ { i }$ is the intercept of the linear demand function (MW), $\boldsymbol { \alpha } _ { k } ^ { i }$ is the slope of the demand function of LSE $_ { ( i = 1 , 2 , 3 ) }$ and $\lambda _ { k }$ is the spot price of electricity. The objective functions and dynamic state equations of the Nash tracking game among LSEs are defined as follows:

![](/api/attachments/DM4CWEBJ/fulltext/images/9db84ba7a79fa5a928a4d270199e0932680c602e8d43d2f941c816ef36e833ac.jpg)  
Fig. 1. IEEE 14-bus power system (interconnected zonal electricity markets).

$$
\begin{array}{l} J _ {k} ^ {i} \left(d _ {k} ^ {i}\right) = \left(d _ {N} ^ {i} - d _ {N} ^ {i d}\right) ^ {\prime} Q _ {N} ^ {i} \left(d _ {N} ^ {i} - d _ {N} ^ {i d}\right) \\ \quad + \sum_ {j = k} ^ {N - 1} \left\{\left(d _ {j} ^ {i} - d _ {j} ^ {i d}\right) ^ {\prime} Q _ {j} ^ {i} \left(d _ {j} ^ {i} - d _ {j} ^ {i d}\right) \right. \\ \quad + \left(\alpha_ {j} ^ {i} - \alpha_ {j} ^ {i d}\right) ^ {\prime} R _ {j} ^ {i} \left(\alpha_ {j} ^ {i} - \alpha_ {j} ^ {i d}\right) \Bigg \} \end{array}\tag{12}
$$

$$
\begin{array}{l} d _ {k + 1} ^ {i} = d _ {k} ^ {i} - \alpha_ {k} ^ {i} \left(\frac {\sum_ {j = 1} ^ {3} \left(D _ {0} ^ {j} - d _ {k} ^ {j}\right)}{\sum_ {j = 1} ^ {3} \alpha_ {k} ^ {j}} + w _ {k}\right) \\ = f _ {k} ^ {i} \left(d _ {k} ^ {i}, \alpha_ {k} ^ {1}, \alpha_ {k} ^ {2}, \alpha_ {k} ^ {3}\right) \end{array}\tag{13}
$$

for i=1,2,3; $k { = } 0 , . . . ,$ N1; N=24.

Eq. (13) consists of a set of non-linear dynamic equations that show each LSE’s zonal demand is directly proportional to its own elasticity and inversely proportional to the zonal price of electricity (which is inversely proportional to all LSEs’ elasticity). In Eq. (13), $w _ { k }$ is the stochastic price volatility at time step k (which is assumed to have a normal distribution with zero mean). In this example, we consider LSEs who bid into day-ahead multi-zone electricity markets. As it can be seen from Eq. (13), the dynamic state equations are nonlinear in the players’ controls $( \bar { \alpha } _ { k } { = } [ \alpha _ { k } ^ { 1 } \alpha _ { k } ^ { 2 } \alpha _ { k } ^ { 3 } ] )$ Knowing the desired load values $( d _ { k } ^ { d } , \ k { = } 1 , . \ . \ . , 2 4 )$ the desired control values $( d _ { k } ^ { d } , \ k { = } 1 , . \ . \ . , 2 4 )$ can be computed using Eq. (11). Before the computation of optimal Nash strategies, the dynamic state equations must be linearized with respects to the states and players’ controls at the desired operating points: $( d _ { k } ^ { d } , \ \alpha _ { k } ^ { d } )$ ,

Probability distribution data of the players’ private information

<table><tr><td>Parameter</td><td>Mean</td><td>Variance</td></tr><tr><td> $D_0^j$ , j=1,2,3</td><td>{450,400,420}</td><td>{10,6,8}</td></tr><tr><td> $Q_k^j$ , j=1,2,3</td><td>{100,95,90}</td><td>{10,10,10}</td></tr><tr><td> $R_k^j$ , j=1,2,3</td><td>{14,12,10}</td><td>{2.5,2,1}</td></tr></table>

![](/api/attachments/DM4CWEBJ/fulltext/images/64925f07bc59ac63d8120970eeda77a910b2b253702bfe52c845e07ab687b3b4.jpg)  
Fig. 2. Predicted market clearing-prices (MCP) of electricity [\$/MW h] vs. time step k. MCP at: zone 1 (solid line), zone 2 (dash line), zone 3 (dash dot line), and zone 4 (dot line).

$$
d _ {k + 1} = A _ {k} d _ {k} + B _ {k} ^ {1} \alpha_ {k} ^ {1} + B _ {k} ^ {2} \alpha_ {k} ^ {2} + B _ {k} ^ {3} \alpha_ {k} ^ {3}\tag{14a}
$$

We assume that the players’ linear demand function intercepts $( D _ { 0 } ^ { i } ~ ( i { = } 1 , ~ 2 , ~ 3 ) )$ and objective function coefficients, $Q _ { k } ^ { i } , R _ { k } ^ { i } ( i { = } 1 , 2 , 3 )$ , have normal distributions with known means and variances to all players in electricity markets.

$$
A _ {k} = \left[ \begin{array}{c c c} \frac {\partial f _ {k} ^ {1}}{\partial d _ {k} ^ {1}} & \frac {\partial f _ {k} ^ {1}}{\partial d _ {k} ^ {2}} & \frac {\partial f _ {k} ^ {1}}{\partial d _ {k} ^ {3}} \\ \frac {\partial f _ {k} ^ {2}}{\partial d _ {k} ^ {1}} & \frac {\partial f _ {k} ^ {2}}{\partial d _ {k} ^ {2}} & \frac {\partial f _ {k} ^ {2}}{\partial d _ {k} ^ {3}} \\ \frac {\partial f _ {k} ^ {3}}{\partial d _ {k} ^ {1}} & \frac {\partial f _ {k} ^ {3}}{\partial d _ {k} ^ {2}} & \frac {\partial f _ {k} ^ {3}}{\partial d _ {k} ^ {3}} \end{array} \right]\tag{14b}
$$

$$
B _ {k} ^ {i} = \left[ \begin{array}{l} \frac {\partial f _ {k} ^ {1}}{\partial \alpha_ {k} ^ {i}} \\ \frac {\partial f _ {k} ^ {2}}{\partial \alpha_ {k} ^ {i}} \\ \frac {\partial f _ {k} ^ {3}}{\partial \alpha_ {k} ^ {i}} \end{array} \right] \text {   for   } i = 1, 2, 3\tag{14c}
$$

For our numerical example these values are given in Table 1. The simulation results are shown

![](/api/attachments/DM4CWEBJ/fulltext/images/b965ce40cae2ac42aef265bf53a8b7b2cea064dd78958ddfa6a038bf1ef733b0.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/a41d62780b528d8f9e31e90020afe10d77c24ed97646f4fb2b307f97824bab9a.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/ae2ac3ef90d390b870f2d2716455368de34d24ec568e4660eb96f586ee013a3d.jpg)  
Fig. 3. Optimal load trajectories $( d _ { k } )$ in MW h: (1) $\mathrm { L S E _ { A } }$ load at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); (2) $\mathrm { L S E _ { B } }$ load at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); (3) $\mathrm { L S E _ { C } }$ load at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line).

in Figs. 3 and 4. As we can see from these results, the optimal Nash-Cournot strategies (optimal controls) for all three players at all four zones are those that force the demand trajectories to follow the desired load values at all trading hours. The predicted zonal market clearing-prices (MCP) of electricity are shown in Fig. 2. The optimal demand trajectories are shown in Fig. 3, and the optimal Nash-Cournot strategies (optimal controls) are shown in Fig. 4.

![](/api/attachments/DM4CWEBJ/fulltext/images/ff083e32e247fe301d7d56bdf86ad85513a2b03ad7b5ce52defa10bd385556b4.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/0e91f7135bbc3173fec281ad891ae1ed188064fc2bef3c2625059e167cbb491e.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/b499ce62d5862f86ab13aff1ba41a1c0c75eee14a5ee86f84e38e2ffba8c5525.jpg)  
Fig. 4. Optimal Nash strategies of players $( \alpha _ { k } ) \colon$ (1) $\mathrm { L S E _ { A } }$ elasticity at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); $( 2 ) \mathrm { L S E _ { B } }$ elasticity at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); (3) $\mathrm { L S E } _ { \mathrm { C } }$ elasticity at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line).

![](/api/attachments/DM4CWEBJ/fulltext/images/e13acb0e5d1e13b84359c32604ab350b11d835e43277fea76d216c89efb9800d.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/e8f905f784dbe6e60c451bec0030947a0929ba8081d9129437d7843aefcece8b.jpg)

![](/api/attachments/DM4CWEBJ/fulltext/images/60314bcf069f522717555f7f9df1baaa4a85219bdb8b3a2573e5dd07d66c9154.jpg)  
Fig. 5. Optimum load deviations $( \delta d _ { k } )$ in MW h: (1) $\mathrm { L S E _ { A } }$ dev. at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); (2) $\mathrm { L S E _ { B } }$ dev. at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line); (3) $\mathrm { L S E _ { C } }$ dev. at zone 1 (solid line), zone 2 (dash line), zone 3 (dash-dot line), and zone 4 (dot line).

The simulation results of Fig. 4 shows that in competitive electricity markets, demand varies as a function of price (hedging against price volatility). In other words, energy double-sided auctions are more competitive and efficient than energy supplier-only auctions. The optimum load deviations $( \delta d _ { k } \mathrm { = } d _ { k } \mathrm { - } d _ { k } ^ { d } )$ from the desired load values for all four zones are shown in Fig. 5. Their values converge to zero after five bidding periods.

The expected profits of the LSEs in dynamic oligopolistic electricity markets based on the algorithm developed in this paper are given in Table 2. These values are compared with the expected profits of the LSEs computed based on the algorithm developed by Wen et al. [13] (using static model for oligopolistic electricity markets ) in Table 2.

Table 2  
LSEs’ expected profits in dynamic electricity multi-markets

<table><tr><td>Player</td><td>Expected profit (in $) “Our method”</td><td>Expected profit (in $) “Wen et al. method”</td></tr><tr><td>LSE_1</td><td>3.5837e6</td><td>5.3239e5</td></tr><tr><td>LSE_2</td><td>4.7549e6</td><td>1.6464e6</td></tr><tr><td>LSE_3</td><td>4.6383e6</td><td>1.5776e6</td></tr></table>

It can be seen from Table 2 that the LSEs’ expected profits for our method are higher than those for Wen et al. method. This shows the advantage of dynamic modeling of oligopolistic electricity markets over existing static models.

## 5. Conclusions

In this paper the problem of developing bidding strategies for the participants of dynamic oligopolistic electricity markets was studied. Attention was given to strategic bidding of load serving entities (LSE) in these markets. We modeled oligopolistic electricity markets as non-linear dynamical systems and used discrete-time Nash bidding strategies. We assumed a Cournot model for our game, where the LSEs decide on demand quantities and the market clearing-price is the marginal cost of producing electricity.

Attention was given to a problem, where the objective functions are quadratic in the deviations of trajectories from desired trajectories and quadratic in the control deviations from the nominal controls. This is called a tracking game. In this paper we dealt with discrete-time dynamic games that were nonlinear in the state equations. We linearized the nonlinear state equations with respect to the state variables and controls of all players at each desired operating point. The simulation results of Fig. 5 showed that the optimum load deviations $( \delta d _ { k } )$ from the desired load values converge to zero after five bidding periods. The developed bidding strategies were used to compute optimal demand quantities for three competing LSEs who bid to buy electricity from four interconnected zonal energy multi-market (IEEE14-bus power system). The LSEs play a Nash-Cournot game (non-cooperative game) among themselves. We assumed that the LSEs sign load-leveling contracts with their customers at each zone based on pre-agreed incentive discounts for each kWh of load curtailment. Our market simulation results showed that the optimal Nash-Cournot strategies (optimal controls) for all three players at all four zones were those that forced the demand trajectories to follow the desired load values at all trading hours. Our simulation results also showed that in competitive electricity markets demand varies as a function of price (hedging against price volatility). In other words, energy double-sided auctions are more competitive and efficient than energy supplier-only auctions. We also showed the advantage of applying dynamic game theory to power trading systems over existing methods (static game theory). This is demonstrated by comparing the LSEs’ expected profits in oligopolistic electricity markets based on the method developed in this paper and that developed by Wen et al. [13].

## References

[1] T. Basar, G.J. Olsder, Dynamic Non-Cooperative Game Theory, second edition, Academic Press, London, 1995.

[2] J.B. Cruz Jr., Leader-follower strategies for multilevel systems, IEEE Transactions on Automatic Control AC-23 (1978) 244–255.

[3] E. Elia, A. Maiorano, Y.H. Song, M. Trovato, Novel methodology for simulation studies of strategic behavior of electricity producers, Proceedings IEEE-PES Summer Meeting 2000, Seattle, 2000 July, pp. 2235 – 2241.

[4] M. Fahrioglu, F. Alvarado, The design of optimal demand management programs, Bulk Power System Dynamics and Control IV-Restructuring Proceedings, Santorini, Greece, 1998 (Aug.).

[5] M. Fahrioglu, F. Alvarado, Using utility information to calibrate customer demand management behavior models, IEEE Transactions on Power Systems 16 (2) (2001 May) 317– 322.

[6] R.W. Ferrero, J.F. Rivera, S.M. Shahidehpour, Application of games with incomplete information for pricing electricity in deregulated power pools, IEEE Transactions on Power Systems 13 (1) (1998 Feb.) 184– 189.

[7] Ali Keyhani, Ashkan Kian, Jose Cruz Jr., Marwan A. Simaan, Market monitoring and control of ancillary services, Journal of Financial Economics, Decision Support Systems 30 (3) (2001 Jan.) 255 – 267.

[8] A.R. Kian, J.B. Cruz Jr., M.A. Simaan, Stochastic discretetime Nash games with constrained state estimators, Journal of Optimization Theory and Applications 114 (1) (2002 July) 171– 188.

[9] A. Maiorano, Y.H. Song, M. Trovato, Dynamics of noncollusive oligopolistic electricity markets, Proceedings IEEE-PES winter meeting 2000, Singapore, 2000 Jan., pp. 838–844.

[10] Richard E. Schuler, Benjamin F. Hobbs, Price adjustments in oligopolistic markets: the impact of lags in customer response, Market Strategy and Structure, Harverster-Sheatsheaf, 1992, pp. 125 – 142.

[11] P. Skantze, J. Chapman, Price dynamics in the deregulated California energy market, IEEE-PES Annual Conference Proceedings, NY, NY, 1999 February.

[12] P. Visudhiphan, M.D. Ilic, Dynamic games-based modeling of electricity markets, IEEE-PES Annual Conference Proceedings, NY, NY, 1999 February.

[13] F. Wen, A.K. David, Optimal bidding strategies and modeling of imperfect information among competitive generators, IEEE Transactions on Power Systems 16 (1) (2001 Feb.) 15 – 21.

![](/api/attachments/DM4CWEBJ/fulltext/images/970cc94a10ef10dd9152de9c486aab4d37766549bba802e790ed886d369beea3.jpg)

Ashkan R. Kian was borne in May 1970 in Tehran, Iran. He received his B.Sc. (with honors) in 1992 from Tehran University; M.S. and Ph.D. degrees in 1997 and 2001 respectively from Ohio State University all in Electrical Engineering. He was the Vice President of Engineering and Development at Genscape, Inc., Louisville, KY from September 2001 to October 2002; Research Associate at the school of ECE, Cornell

University from November 2002 to December 2003. Dr. Kian is currently an assistant professor in electrical engineering (Control & Intelligent Processing Center of Excellence) at University of Tehran, Tehran, Iran. His research interests are: bidding strategies in dynamic energy markets, game theory, stochastic optimal control, market monitoring, power systems operation and control.

![](/api/attachments/DM4CWEBJ/fulltext/images/806f6516d9bf84087254bbfbb22ef910cc28798dc05ea22c4c79ee9e535160bd.jpg)

Jose B. Cruz, Jr. is the Howard D. Winbigler Chair in Engineering, and Professor of Electrical Engineering at the Ohio State University OSU. He received his BS summa cum laude from the University of the Philippines in 1953, SM from the Massachusetts Institute of Technology in 1956 and the PhD from the University of Illinois in 1959, all in electrical engineering. He served as Dean of the College of Engineering at OSU from 1992 to 1997,

Professor of Electrical and Computer Engineering at the University of California in Irvine UCI from 1986 to 1992, and at the University of Illinois from 1965 to 1986. Dr Cruz was elected as a member of the National Academy of Engineering in 1980. He is also a life Fellow of the Institute of Electrical and Electronics Engineers; recipient, Curtis W. McGraw Research Award of the American Society for Engineering Education 1972; recipient, Halliburton Engineering Education Leadership Award, 1981; distinguished member, IEEE Control Systems Society, designated in 1983; recipient, IEEE Centennial Medal, 1984; recipient, IEEE Richard M. Emberson Award, 1989; Fellow, American Association for the Advancement of Science elected 1989; recipient, ASEE Centennial Medal, 1993; and recipient, Richard E. Bellman Control Heritage Award, American Automatic Control Council in 1994; member, National Academy of Engineering, elected 1980; corresponding member, National Academy of Science and Technology (Philippines), elected 2003.
