---
otero_id: 5756
otero_key: "UJHA4VQD"
title: "On the supply function equilibrium and its applications in electricity markets"
authors: "Aleksandr Rudkevich"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.05.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the supply function equilibrium and its applications in electricity markets

Aleksandr Rudkevich<sup>\*</sup>

Tabors Caramanis and Associates, 50 Church Street, Cambridge MA, 02138, USA

Available online 22 July 2004

## Abstract

The paper deals with the Supply Function Equilibrium (SFE) as a model of competition in electricity markets. It introduces theoretical advancement through relaxing traditional assumptions of continuity of supply functions and provides a foundation for efficient computational algorithms. Two special examples are considered. One demonstrates that continuous equilibrium could be impossible while an infinite set of discontinuous equilibria exists. Another example proves the convergence to a linear equilibrium through learning in linear supply system. A possibility of a similar convergence for piece-wise linear system is being discussed.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Supply function equilibrium; Competition in electricity markets; Strategic behavior; Market power

## 1. Introduction

The concept of supply function equilibrium (SFE) was originally developed by Klemperer and Meyer [11] as a way of modeling how competitors could achieve profit-maximizing equilibria in the marketplace under conditions of uncertain demand. The SFE approach was then adopted by Green and Newbery [9] as a model for strategic bidding in a competitive spot market for electricity. That particular publication attracted a substantial interest to the SFE model both in the industry and in academia. The SFE concept offers a compelling model of competitive behavior of multiple suppliers of a single product in which the existence of the Nash equilibrium does not require the demand to be elastic. Instead, representation of the suppliers’ behavior by means of supply functions, rather than price-quantity pairs, creates elasticity of the residual demand faced by each player and could result in a sensible equilibrium outcome even if the demand is non-responsive to price. The on-going over the last decade deregulation of the electric industry in various countries of the world prompted industry analysts and consultants to study the SFE concept as means for modeling strategic behavior in electricity markets, creating tools for the direct analysis of market power, assessment of the impact of strategic behavior on electricity prices and on the market value of generating assets (see for example Ref. [14]).

Green and Newbery advanced the SFE theory by including capacity constraints [9] and by incorporating contracts for differences in the SFE framework, [7,8,12]. Rudkevich et al. [15] obtained a closedform solution to the Klemperer–Meyer equation in a special case of zero price elasticity of demand, generalized the model for the case of non-convex step-wise marginal cost curves representing discrete generating units operating in the market. Anderson and Xu [2], following Anderson and Philpott [1], considered a similar problem but relied on a an original technique for representing supply functions as parametrical two-dimensional curves. This approach allowed them to obtain optimality conditions in a very general form allowing for a discontinuous relationship between price and quantity and to prove the existence of the optimal response of an individual player. Rudkevich [13] analyzed the ability of players to adapt their behavior through market observations and learning by means of the Cournot adjustment process and proved that players characterized with linear marginal costs and unconstrained capacities are capable of converging to the linear SFE. Baldick et al. [4] explored the applicability of this approach to piece-wise linear systems. Baldick and Hogan [3] attempted a substantial analytical and numerical explorations of SFEs in piece-wise linear systems.

Yet a wide spectrum of theoretical and applied problems remains unresolved. The original paper [11] was dealing with systems with uncertain demand and a single market clearing during the game period. Moreover, suppliers were assumed to be identical (symmetrical system). In light of these two assumptions, it is not surprising that the resulting equilibria are insensitive to the shape of the demand distribution (e.g., demand duration). Attempts to integrate Klemperer–Meyer equations in non-symmetrical cases could yield supply functions that were not always monotonically increasing or even always monotonically declining supply functions. In was not clear whether equilibrium conditions could be discontinuous and if so, what rules should be guiding their discontinuity. Finally, equilibrium conditions were explored only for the case of the so-called one-price payment rule.

In this paper, we offer a general formulation of the SFE game, consider a spectrum of payment rules ranging from the one-price to the pay-bid market design and derive necessary conditions of equilibria in those general settings. In all other parts we focus entirely on the system with one-price payment rule. We use these optimality conditions to explore equilibria in systems with zero marginal costs, analyze the adaptive learning process and its convergence to the equilibrium in linear systems, and outline an efficient algorithms for solving the problem of optimal response for piece-wise linear systems which could be used as a first step in adaptive learning in such systems. Finally, we briefly discuss the application of this algorithm to finding the equilibrium in supply functions for power systems.

## 2. Description of the SFE game

We consider a one-shot non-cooperative game of n+1 players—n competing generating firms and one market administrator (MA) such as an Independent System Operator (ISO) typically administering markets for electricity.

We assume that consumers’ demand for the product is given in a form of a demand duration function $D ( t , p ) . ~ D ( t , p )$ depends on time and price such that $D _ { t } ^ { \prime } ( t , p ) { > } 0 , D _ { p } ^ { \prime } ( t , p ) { \leq } 0$ . Time is continuous and $0 { \le } t { \le } \bar { T }$ . We further assume that firms are characterized by cost functions $C _ { j } ( q _ { j } )$ that are continuous and piece-wise differentiable functions of production capacities $q _ { j }$ . Production capacities are bounded from below by zeros and from above by totalP capacity available to each firm: $0 { \le } q _ { j } { \le } W _ { j } ; \ j = \overline { { 1 , n } }$

Prior to the beginning of the game period, each firm submits to the MA a supply function $q _ { j } ( p )$ which is a piece-wise differentiable, monotonically non-descending function of price. The MA develops a market-wide supply function

$$
Q (p) = \sum_ {j = 1} ^ {n} q _ {j} (p)
$$

and in each moment of time $0 { \le } t { \le } \bar { T }$ solves equation $Q ( p ) { = } D ( t , p )$ for price. Solutions to this equation at each instantaneous moment $P ( t )$ form a monotonically ascending function of time, known as a price duration function. Let us compute

$$
p _ {0} = P (0); p _ {1} = P (\bar {T}); p _ {0} <   p _ {1}
$$

and define function $T ( p )$ inverse to the price duration function:

$$
P (T (p)) \equiv p; T (p _ {0}) = 0; T (p _ {1}) = \bar {T}.
$$

The results of the MA’s actions are: the price limits $p _ { 0 }$ and $p _ { 1 }$ and the Inverse Price Duration Function (IPDF) $T ( p )$

In general, we assume that in each instant moment of time, for each infinitesimal increment of capacity $\mathrm { d } q _ { j } ( \boldsymbol { p } )$ offered to the market at prices ranging between $p$ and $p { \mathrm { + d } } p ,$ the firm is paid the bid price $p$ and an incentive proportional to the difference between the market clearing price and the bid price. The infinitesimal revenue flow for this capacity increment will be equal to

$$
\mathrm{d} r (t, p) = [ p + \beta (P (t) - p) ] \mathrm{d} q _ {j} (p)
$$

where $\beta$ is a parameter of market design ranging between zero and unity. $\beta { = } 1$ corresponds to the oneprice market, $\beta { = } 0$ corresponds to the pay-bid market.

The integrated flow of revenues for firm j in time moment t could be expressed in the following way:

$$
\begin{array}{l} r _ {j} (t) = q _ {j} \left(p _ {0}\right) \left[ p _ {0} + \beta (P (t) - p _ {0}) \right] \\ \quad + \int_ {p _ {0}} ^ {P (t)} [ x + \beta (P (t) - x) ] \mathrm{d} q _ {j} (x) \\ = q _ {j} \left(p _ {0}\right) \left[ p _ {0} + \beta (P (t) - p _ {0}) \right] \\ \quad + \int_ {p _ {0}} ^ {P (t)} [ x + \beta (P (t) - x) ] q _ {j} ^ {\prime} (x) \mathrm{d} x \end{array}
$$

Total revenues the firm j will receive during the game period $0 { \le } t { \le } \bar { T }$ will equal to

$$
R _ {j} = \int_ {0} ^ {\bar {T}} \mathrm{d} t \int_ {p _ {0}} ^ {P (t)} [ x + \beta (P (t)) - x ] q _ {j} ^ {\prime} (x) \mathrm{d} x + \bar {T} p _ {0} q _ {j} (p _ {0})
$$

Firm’s total variable costs over the game period are equal to

$$
V _ {j} = \int_ {0} ^ {\bar {T}} C _ {j} [ q _ {j} (P (t)) ] \mathrm{d} t,
$$

resulting in profit margin $\pi _ { j } { = } R _ { j } { - } V _ { j }$ . It is easy to derive that

$$
\begin{array}{l} \pi_ {j} = \int_ {p _ {0}} ^ {p _ {1}} \left[ p q _ {j} (p) - C _ {j} \bigl (q _ {j} (p) \bigr) \right] T ^ {\prime} (p) \mathrm{d} p \\ - (1 - \beta) \int_ {p _ {0}} ^ {p _ {1}} (\bar {T} - T (p)) q _ {j} (p) \mathrm{d} p \end{array}\tag{1}
$$

Let us denote the profit functional in (Eq. (1)) as $\begin{array} { l } { \displaystyle { \pi _ { j } ( q _ { j } , ~ T , ~ p _ { 0 } , ~ p _ { 1 } ) } } \end{array}$ . This notation reflects key factors influencing the value of the profit margin of each firm.

Formula (1) shows that the supply function a firm submits to the MA influences its payoff in two ways—directly and indirectly. The latter is through influencing MA’s actions, namely the price limits and IPDF which also appear in that formula.

## 3. Definition of the Nash Equilibrium

We assume that firms choose their supply functions in order to maximize the total profit $\pi _ { j }$ for the entire game period $0 { \le } t { \le } \bar { T }$ . Once supply functions $q _ { j } ( p ) , \ j = 1 , 2 , . . . n ,$ are chosen, the MA responds with price limits $p _ { 0 }$ and $p _ { 1 }$ and the IPDF $T ( p )$ . As stated earlier, firms’ profit margins are denoted as $\scriptstyle \pi _ { j } = \pi _ { j } ( q _ { j } , T , p _ { 0 } , p _ { 1 } )$

If the firm number k unilaterally changes its supply function, i.e. it submits supply function $\tilde { q } _ { k } ( p )$ that is different from the supply function $q _ { k } ( p )$ while all other firms adhere to supply functions $q _ { j } ( p ) , j \not = k$ , then the MA by solving equation

$$
\sum_ {j \neq k} q _ {j} (p) + \tilde {\boldsymbol {q}} _ {k} (p) = D (t, p)
$$

will respond with a new set of $\tilde { p } _ { 0 }$ and $\tilde { p } _ { 1 }$ and the IPDF $\tilde { T } ( p )$ . This response could change profit margins of all firms to $\tilde { \pi } _ { j } { = } \Pi _ { j } ( q _ { j } , \tilde { T } , \tilde { p } _ { 0 } , \tilde { p } _ { 1 } )$ if jpk and $\tilde { \pi } _ { k } { = } \Pi _ { k } ( \tilde { q } _ { k } , \tilde { T } , \tilde { p } _ { 0 } , \tilde { p } _ { 1 } )$

Definition 1. We will say that the set of supply functions $q _ { j } ( p ) _ { \mathcal { J } } { = } 1 , 2 , . . . , n$ , the price limits $p _ { 0 }$ and $p _ { 1 }$ and the IPDF $T ( p )$ form a Nash equilibrium in the above described game if

(1) All supply functions are defined in the interval $\left[ p _ { 0 } , p _ { 1 } \right]$ and on that interval they satisfy the following feasibility conditions:

$$
0 \leq q _ {j} (p) \leq W _ {j}; j = 1, 2, \dots , n\tag{2}
$$

$$
\frac {\mathrm{d} q _ {j} (p)}{\mathrm{d} p} \geq 0; j = 1, 2, \dots , n\tag{3}
$$

(2) No unilateral change of the supply function by any firm k from $q _ { k } ( p )$ to a function $\widetilde { q } _ { k } ( \boldsymbol { p } )$ satisfying feasibility conditions (2) and $( 3 )$ and resulting in a change in price limits to $\tilde { p } _ { 0 }$ and $\tilde { p } _ { 1 }$ and in the IPDF to $\tilde { T } ( p )$ could increase this firm’s payoff:

$$
\Pi_ {k} \big (\tilde {\boldsymbol {q}} _ {k}, \tilde {T}, \tilde {\boldsymbol {p}} _ {0}, \tilde {\boldsymbol {p}} _ {1} \big) \leq \Pi_ {k} (q _ {k}, T, p _ {0}, p _ {1}).\tag{4}
$$

## 4. Nash Equilibrium in supply functions

Theorem 1. If supply functions $q _ { j } ( p ) , \ j = I , 2 , . . . . , n ,$ price limits $p _ { \theta }$ and p<sub>1</sub> and the IPDF T(p) form a Nash equilibrium, then there exists a set of continuous and differentiable almost everywhere on $[ p _ { 0 } , p _ { I } ]$ adjoint functions w<sub>j</sub>(p), $j { = } I , 2 , . . . . , n$ such that each of the following is true:

(1) $\psi _ { j } ( p ) { \leq } 0 , j { = } I , 2 , . . . , n$ and satisfy adjoint differential equations

$$
\begin{array}{l} \frac {d \psi_ {j}}{d p} = (1 - \beta) (\bar {T} - T) \\ + \frac {\beta q _ {j} - [ p - C _ {j} ^ {\prime} (q _ {j}) ] [ q _ {- j} ^ {\prime} - D _ {p} ^ {\prime} (T , p) ]}{D _ {t} ^ {\prime} (T , p)} \end{array}\tag{5}
$$

(2) If a supply function $q _ { j } ( p )$ is growing at price $p ,$ $q _ { j } ^ { \prime } ( p ) { > } 0 $ , then $\psi _ { j } ( p ) { = } 0$ and

$$
\begin{array}{c} \frac {d q _ {- j}}{d p} = \frac {\beta q _ {j} + (1 - \beta) D _ {t} ^ {\prime} (T , p) [ \bar {T} - T ]}{p - C _ {j} ^ {\prime} (q _ {j})} \\ + D _ {p} ^ {\prime} (T, p) \end{array}\tag{6}
$$

where $q _ { - j } ( p )$ denotes the aggregate supply function of all competitors of the firm j:

$$
q _ {- j} (p) = \sum_ {k \neq j} q _ {k} (p)\tag{7}
$$

(3) If $\psi _ { j } ( p ) { < } 0$ on some interval of prices, then the supply function $q _ { j } ( p )$ must remain constant on that interval, $q _ { j } ^ { \prime } ( p ) { = } 0$

(4) Supply meets demand at all prices:

$$
\sum_ {j = 1} ^ {n} q _ {j} (p) = D (T (p), p)\tag{8}
$$

(5) The price limits and boundary values of supply and adjoint functions satisfy the following transversality conditions:

$$
\psi_ {j} (p _ {0}) q _ {j} (p _ {0}) = 0; \psi_ {j} (p _ {0}) \leq 0; q _ {j} (p _ {0}) \geq 0\tag{9}
$$

$$
T \left(p _ {0}\right) = 0\tag{10}
$$

$$
\psi_ {j} \left(p _ {1}\right) \left[ q _ {j} \left(p _ {1}\right) - W _ {j} \right] = 0; \psi_ {j} \left(p _ {1}\right) \leq 0; q _ {j} \left(p _ {1}\right) \leq W _ {j}\tag{11}
$$

$$
T (p _ {1}) = \bar {T}\tag{12}
$$

(6) Supply function $q _ { j }$ may have a vertical jump at price p from q<sub></sub> to $q _ { + } ,$ where $q _ { + } { > } q$ <sub></sub> only if $q _ { - j } ^ { \prime } \left( p \right)$ also jumps at that price and the following condition holds

$$
\begin{array}{c} \frac {q _ {- j} ^ {\prime} (p +) - D _ {p} ^ {\prime}}{q _ {- j} ^ {\prime} (p -) - D _ {p} ^ {\prime}} - \frac {p - C _ {j} ^ {\prime} (q _ {-})}{p - C _ {j} ^ {\prime} (q _ {+})} \\ > 0 (\text {   if   } \beta > 0) \geq 0 (\text {   if   } \beta = 0) \end{array}\tag{13}
$$

The proof of this theorem appears in Appendix A. The problem (5)–(13) is a two-point boundary problem. However, it does not have enough boundary conditions to ensure unique equilibrium if such exists. Therefore, as a two-point boundary problem the latter is under-defined and could have an infinite set solution as discussed in next two sections.

## 5. Differential equations for supply functions

Differential equations (Eq. (6)) seem to make the search for the equilibrium very promising. It is easy to notice that if $\beta { = } 1$ , it becomes a familiar Klemperer– Meyer equation

$$
\frac {\mathrm{d} q _ {- j} (p)}{\mathrm{d} p} = \frac {q _ {j} (p)}{p - C _ {j} ^ {\prime} (q _ {j} (p))} + D _ {p} ^ {\prime} (T (p), p)\tag{14}
$$

Klemperer and Meyer derived their equation assuming zero cross-elasticity of demand, $D _ { p t } ^ { \prime \prime } { = } 0$ . Eq. (14) is a generalization accounting for an arbitrary crosselasticity. It is important to note that not all supply functions must obey Eq. (14) at the same price. Indeed, as indicated by condition (3), supply functions could stay flat over some interval of prices, e.g., not offering any incremental supply until <sup>b</sup>the price is right.<sup>Q</sup> In a system comprised of suppliers with different capacities and cost characteristics, the appearance of such flat segments over some price intervals should be more of a rule than an exception. Therefore, it should be expected that in a given price interval, only a subset of functions would obey Eq. (14). Let us assume that firms with the set of indices $A { = } \{ j _ { 1 } , . . . . j _ { k } \}$ and only those firms obey differential equations (Eq. (14)) over the same interval of prices. Define $\begin{array} { r } { Q _ { A } ( p ) = \sum _ { r \in A } q _ { r } } \end{array}$ Since all other supply functions are flat over that interval of prices, $q _ { - j } ^ { \prime } = { Q } _ { A } ^ { \prime } - q _ { j } ^ { \prime }$ Observing that $\begin{array} { r } { ( k - 1 ) Q _ { \cal A } ^ { \prime } = \sum _ { r \in { \cal A } } q _ { - r } ^ { \prime } , } \end{array}$ , Eq. (14) could be reduced to the normal form:

$$
q _ {m} ^ {\prime} = \frac {1}{k - 1} \sum_ {r \in A} \frac {q _ {r}}{p - C _ {r} ^ {\prime} (q _ {r})} - \frac {q _ {m}}{p - C _ {m} ^ {\prime} (q _ {m})} + \frac {D _ {p} ^ {\prime}}{k - 1}\tag{15}
$$

where $m \in A .$

This system of simultaneous equations yields feasible solutions (monotonically increasing supply functions) as long as all right hand sides stay positive. Thus, for a subset of firms $A { = } \{ j _ { 1 } , . . . . j _ { k } \}$ and price $p ,$ , we can define a feasible subset in the phase space as a set of all such $q _ { i _ { 1 } } , . . . , q _ { i _ { k } }$ that

$$
\begin{array}{l} \frac {1}{k - 1} \sum_ {r \in A} \frac {q _ {r}}{p - C _ {r} ^ {\prime} (q _ {r})} - \frac {q _ {m}}{p - C _ {m} ^ {\prime} (q _ {m})} \\ + \frac {D _ {p} ^ {\prime} (T , p)}{k - 1} \geq 0 \end{array}
$$

where m<sup>a</sup>A

$$
0 \leq q _ {j} \leq W _ {j}; j = \overline {{1 , n}}
$$

$$
D (T, p) = \sum_ {j = 1} ^ {n} q _ {j}
$$

With the total of n suppliers, there are $2 ^ { n } - ( n + 1 )$ different subsets containing two or more suppliers. Thus, for any price $p$ there potentially could be that many feasible subsets and therefore that many different systems of differential equations defining supply functions. Thus, unlike the symmetrical case considered by Klemperer and Meyer and the case of asymmetrical duopoly explored by Green and Newbery [9], the variety of potential equilibria could be decided not only by the set of boundary conditions, but also by the variety of differential equations that should be considered at every price $p .$ Thus, if a trajectory at a price $p$ is passing through a point in the phase space (let us say in the direction of increasing prices) the behavior of this trajectory could potentially switch into any subset of differential equations whose feasibility set contains that point in the phase space at that price. The switch between differential equations, however, cannot be arbitrary, given the conditions on adjoint functions specified in Theorem 1. Indeed, a switch corresponds to at least one supply function becoming flat and/or at least one supply function initiating a growth segment. Again, assuming that integration of the entire system occurs in order of increasing prices, a condition for the supply function to initiate growth will be determined by the adjoint differential equation through finding the price at which the corresponding adjoint function vanishes. However, it is not obvious at which point and which particular supply function must become flat. That determination could only be verified upon reaching the final point of integration by checking transversality conditions. Thus, we are dealing with a two-point boundary problem with added complexity when not only the boundary conditions on one end must be chosen to satisfy conditions on the other end, but also at every point a decision has to be made whether and how the composition of differential equations to integrate further should be changed. With up to $2 ^ { n } - ( n + 1 )$ possibilities to consider at each point, the complexity of this problem appears overbearing.

## 6. Example 1. Asymmetrical system with zero marginal costs

In this section, we consider a special example of the SFE game with zero marginal costs of all players. Games of this kind appear in selling capacity in the Installed Capability Market (ICAP) or in markets for firm transmission rights on a particular path. In the first case, players are generating firms selling installed capacity of their plants to Load Serving Entities obligated to procure such capacity to ensure system reliability. In the second case, players are typically Load Serving Entities procuring firm transmission right to hedge their exposure to price spikes caused by transmission congestion. Although in the latter case the bidders submit monotonically declining demand curves, the game still could be reduced to the same SFE framework.

In this example, we demonstrate that it may be impossible for all players to be simultaneously active, i.e. to have growing supply functions. We also demonstrate that all equilibria in such a game could be discontinuous.

We assume that players face an uncertain demand range $[ D _ { 0 } \mathbf { \cal D } _ { 1 } ]$ and that demand is inelastic.

If there are n active players in this game, Klemperer–Meyer equations for those players are relatively simple:

$$
q _ {- j} ^ {\prime} = \frac {q _ {j}}{p} \quad j = 1, \dots , n\tag{16}
$$

The aggregate supply curve of active players $Q ( p ) =$ $\scriptstyle \sum _ { j = 1 } ^ { n } q _ { j } ( p )$ satisfies differential equation

$$
Q ^ {\prime} = \frac {Q}{(n - 1) p}\tag{17}
$$

and therefore is equal to

$$
Q (p) = Q _ {\max} \left(p / p _ {\max}\right) ^ {1 / (n - 1)}\tag{18}
$$

where $p _ { \mathrm { m a x } }$ is the highest price at which the market is assumed to clear (generally this price could be unknown); $\mathcal { Q } _ { \mathrm { m a x } }$ is the aggregate supply of all active players at that price. A general solution to system (16) can easily be found and is given by the following expression:

$$
q _ {j} (p) = q _ {j} ^ {\max} \left[ \frac {1}{n \varepsilon_ {j}} \left(\frac {p}{p _ {\max}}\right) ^ {1 / (n - 1)} - \frac {p _ {\max}}{p} \left(\frac {1}{n \varepsilon_ {j}} - 1\right) \right]\tag{19}
$$

where $q _ { j } ^ { \operatorname* { m a x } } { \leq } W _ { j }$ is the capacity offered by j-th player at maximum price and $\scriptstyle { \varepsilon _ { j } = q _ { j } ^ { \mathrm { m a x } } } / Q _ { \mathrm { m a x } }$ is its market share at maximum price. Eq. (19) gives a feasible solution only if the resulting supply function is nonnegative and monotonically increasing.

It is easy to verify that for a larger player with $\varepsilon _ { j } { > } 1 /$ n the supply function defined by Eq. (19) is nonnegative for all prices within the range $[ 0 , p _ { \mathrm { m a x } } ]$ whereas for a <sup>b</sup>small<sup>Q</sup> player with $\varepsilon _ { j } { < } 1 / n$ the solution could be positive only on a subinterval of prices $[ P _ { j } ^ { + } , { p } _ { \operatorname* { m a x } } ]$ where

$$
P _ {j} ^ {+} = p _ {\max} \left[ 1 - n \varepsilon_ {j} \right] ^ {(n - 1) / n} \text {   if   } \varepsilon_ {j} <   1 / n,\tag{20}
$$

The smaller is the player, the narrower will be interval in which its supply function could be positive.

It is also easy to verify that for smaller players with $\varepsilon _ { j } { < } 1 / n$ its supply function is always monotonically increasing at any price. However, for <sup>b</sup>intermediate<sup>Q</sup> players with $1 / n { < } \varepsilon _ { j } { < } 1 / ( n { - } 1 )$ the solution would be monotonically increasing only within the interval of prices $[ \hat { P _ { j } } , \bar { p } _ { \mathrm { m a x } } ]$ where

$$
\begin{array}{l} \hat {P} _ {j} = p _ {\max} \left[ n (n - 1) \left(\varepsilon_ {j} - 1 / n\right) \right] ^ {(n - 1) / n} \\ \text { if } 1 / n <   \varepsilon_ {j} <   1 / (n - 1) \end{array}\tag{21}
$$

The solution will be monotonically decreasing on the entire price interval for a <sup>b</sup>very large<sup>Q</sup> player with $\displaystyle \varepsilon _ { j } { > } 1 / ( n { - } 1 )$

The above stated conditions of monotonicity indicate that it maybe impossible for supply functions of all players to be simultaneously growing. Indeed, if some active players appear <sup>b</sup>very large,<sup>Q</sup> their supply functions defined by Klepmperer–Meyer equations are simply infeasible at any price. It will be simply impossible to find an equilibrium with all supply functions simultaneously growing at all prices. Thus, in order to construct an equilibrium, supply functions of some small players have to be flat at high prices. That would exclude those players from the active set and reduce the market share of larger players among active players. The obvious rule is that at any price interval active players either have to be small or intermediate, i.e., among n active participants no player should have market share exceeding $1 / ( n { - } 1 )$

Consider now the case of two players with $\varepsilon _ { 1 } { > } 1 / 2$ and $\scriptstyle \varepsilon _ { 2 } = 1 - \varepsilon _ { 1 } < 1 / 2$ . Their supply functions are:

$$
\begin{array}{l} q _ {j} (p) = q _ {j} ^ {\max} \left[ \frac {1}{2 \varepsilon_ {j}} \left(\frac {p}{p _ {\max}}\right) - \frac {p _ {\max}}{p} \left(\frac {1}{2 \varepsilon_ {j}} - 1\right) \right]; \\ j = 1, 2. \end{array}\tag{22}
$$

In the duopoly case one player is small and another is intermediate and their supply functions are <sup>b</sup>synchronized,<sup>Q</sup> because the supply function of the small player becomes positive at the same price at which the supply function of the intermediate player becomes monotonically increasing:

$$
\hat {P} _ {1} = p _ {\max} [ 2 \varepsilon_ {1} - 1 ] ^ {1 / 2} = P _ {2} ^ {+} = p _ {\max} [ 1 - 2 \varepsilon_ {2} ] ^ {1 / 2}
$$

If both supply function are continuous on the price interval $[ \hat { P _ { 2 } } , \hat { P _ { \mathrm { m a x } } } ]$ , the aggregate supply function is linear on that interval:

$$
Q (p) = Q _ {\max} \left(p / p _ {\max}\right)
$$

However, for the market to always clear, it is necessary that

$$
Q _ {\max} \geq D _ {1} \text { and } Q _ {\max} (\hat {P} _ {1} / p _ {\max}) = Q _ {\max} [ 2 \varepsilon_ {1} - 1 ] ^ {1 / 2} \leq D _ {0}
$$

the latter is possible if and only if

$$
\varepsilon_ {1} \leq \frac {1}{2} \left[ 1 + \left(\frac {D _ {0}}{D _ {1}}\right) ^ {2} \right]\tag{23}
$$

and sets limitation on the market share of the dominant player. Assume now that at the highest demand the market is tight, $W _ { 1 } { + } W _ { 2 } { = } D _ { 1 }$ resulting in $\scriptstyle \varepsilon _ { 1 } = W _ { 1 } / ( W _ { 1 } + W _ { 2 } )$ , because in order for the market to clear, bidders have to offer their entire capacity to the market at maximum price. Therefore, continuous equilibrium ensuring that the market clears over the entire price range would be possible only if

$$
\frac {W _ {1}}{W _ {1} + W _ {2}} \leq \frac {1}{2} \left[ 1 + \left(\frac {D _ {0}}{D _ {1}}\right) ^ {2} \right]\tag{24}
$$

Thus, should the composition of supply be too asymmetric with Player 1 having too much of a market share, no continuous equilibrium could be found. We can express condition (23) slightly differently. Define the demand uncertainty coefficient $\gamma { = } D _ { 1 } / D _ { 0 }$ and supply asymmetry coefficient as $\scriptstyle \rho = 2 \varepsilon _ { 1 } - 1$ Obviously, $\gamma { \geq } 1$ and $0 { \le } \rho { \le } 1$ . Higher values of $\gamma$ correspond to more uncertain demand. Higher values of $\rho$ correspond to a more asymmetrical supply. Condition (23) can now be rewritten as

$$
\rho \gamma^ {2} \leq 1
$$

In other words, for the continuous equilibrium to exist, more uncertain demand requires more symmetrical supply.

Nonexistence of continuous equilibrium does not mean that no equilibrium could be found. There is an infinite set of discontinuous equilibria. Indeed, assume that players’ supply functions satisfy Eq. (23) on an interval $( \tilde { p } , p _ { \mathrm { m a x } } ]$ and that condition (24) is not satisfied. It is easy to verify that if Player 1 has a higher market share at maximum price, it will have higher market share at any price within interval $( \tilde { p } , p _ { \mathrm { m a x } } ]$ . Theorem 1 permits the supply function of Player 1 to change in a jump at price ${ \tilde { p } } .$ Indeed, that would be consistent with condition (6) which in this case could be restated in the following form:

$$
\frac {q _ {2} ^ {\prime} (\tilde {p} +)}{q _ {2} ^ {\prime} (\tilde {p} -)} = \frac {q _ {1} (\tilde {p} +)}{q _ {1} (\tilde {p} -)} > 1
$$

That condition is obviously satisfied. As follows from Eqs. (8) (9), the size of the jump should be chosen in such a way that

$$
\frac {q _ {1} (\tilde {\boldsymbol {p}} -)}{q _ {1} (\tilde {\boldsymbol {p}} -) + q _ {2} (\tilde {\boldsymbol {p}})} \leq \frac {1}{2} \left[ 1 + \left(\frac {D _ {0}}{q _ {1} (\tilde {\boldsymbol {p}} -) + q _ {2} (\tilde {\boldsymbol {p}})}\right) ^ {2} \right]
$$

which is equivalent to

$$
q _ {1} ^ {2} (\tilde {\boldsymbol {p}} -) \leq q _ {2} ^ {2} (\tilde {\boldsymbol {p}}) + D _ {0} ^ {2}\tag{25}
$$

Choosing the size of the jump according to Eq. (25) would guarantee that the market can clear. However, the choice of discontinuity price $\tilde { p }$ is arbitrary and essentially there exists at least one equilibrium for any such discontinuity price.

Based on this example, several observations could be made. First, an attempt to solve a simultaneous system of Klemperer–Meyer equations will not necessarily lead to finding an equilibrium. This system could hold simultaneously only for a subset of players, but not necessarily for all players. Second, even in the simplest case of duopoly there could be no equilibrium with both supply functions being continuous. Thus, the discontinuity in the SFE framework has to be carefully addressed. It could be very common, especially in a set of diverse (in this example very asymmetric) players. Third, the SFE game could allow for an infinite set of discontinuous equilibria.

## 7. Example 2. Cournot adjustment process in linear systems

A relatively simple SFE game considered in the previous example leads to a rather disturbing conclusion that an attempt to construct an equilibrium by trying to solve the two-point boundary problem formulated in Theorem 1 is not only difficult but also ambiguous, because the problem underdefined and an infinite set of equilibria might exist. This poses another methodological problem well known in Game Theory and discussed for example by Fudenberg and Levine [6]: if there are multiple equilibria, there is no guarantee that players would coordinate their moves toward the same equilibrium or any equilibrium at all.

Therefore, it is useful to model the process in which players may evolve in the game over time. For example, players could start with a trial bidding strategy and then adjust it based on market observations. The next move of each player could conceivably be an attempt to maximize its payoff assuming that competitors would continue to behave as observed. This process is known as Cournot adjustment [6].

In this example we analyze this learning process assuming that all players have unlimited supply and linear marginal cost functions. First we prove that in linear systems there exists a unique linear SFE. Next, we demonstrate that the learning process converges to that linear SFE.

We assume that each firm controls a continuous set of infinitesimal generation capacities and is characterized by a quadratic cost function:

$$
C _ {j} (q _ {j}) = \frac {1}{2} c _ {j} q _ {j} ^ {2}
$$

where $C _ { j } ( q _ { j } )$ is the total cost that firm j would incur at any instant moment of time in which it generates quantity $q _ { j }$ . Firm j’s marginal cost function is equal to

$$
C _ {j} ^ {\prime} (q _ {j}) = c _ {j} q _ {j}\tag{26}
$$

which is a linear function of its outputs.

Two important facts are stated below for models with linear marginal cost functions.

The market-wide marginal cost function $C _ { \mathrm { M } } ^ { \prime } ( Q ) =$ $c _ { \mathrm { M } } Q$ is also linear. Here $\mathcal { Q }$ denotes the total supply of all generators and

$$
c _ {\mathrm{M}} = \left(\sum_ {i = 1} ^ {n} \frac {1}{c _ {i}}\right) ^ {- 1}\tag{27}
$$

Under perfect competition (defined here as a least-cost dispatch), market shares of all firms are independent of the level of the demand served and are inversely proportional to firms’ marginal cost coefficients.

$$
\varepsilon_ {j} = \frac {c _ {\mathrm{M}}}{c _ {j}} \text { where } \sum_ {j = 1} ^ {n} \varepsilon_ {j} = 1\tag{28}
$$

We assume that the total demand $D ( t , p )$ linearly depends on price. For example, it could be presented in the following form:

$$
\begin{array}{c} D (t, p) = D _ {0} (t) - \delta (p - c _ {\mathrm{M}} D _ {0} (t)) \\ = D _ {0} (t) [ 1 + \delta c _ {\mathrm{M}} ] - \delta p \end{array}
$$

where $D _ { 0 } ( t )$ is the level of demand in hour t assuming that the price in that hour equals system-wide marginal cost of serving that demand; $\delta$ is the slope of the demand responsiveness to price. In this case, the price elasticity of demand at the point of marginal cost equals<sup>1</sup>

$$
- \omega = - \delta c _ {\mathrm{M}}
$$

We also assume in this example that not all of the dispatched capacity will be necessarily sold at spot prices. Bidding companies may enter bilateral contracts with buyers at prices that are not instantly related to spot prices. To reflect this reality in the stylized model, following Green [7,8], we assume that each firm j has a total contractual obligation to sell $Y _ { j }$ MW each hour at price $f _ { j }$ In this case, firm’s revenues are equal to

$$
R _ {j} = p \big [ q _ {j} (p) - Y _ {j} \big ] + f _ {j} Y _ {j}
$$

resulting in the profit margin

$$
\pi_ {j} = R _ {j} - C _ {j} = p \left[ q _ {j} (p) - Y _ {j} \right] + f _ {j} Y _ {j} - \frac {1}{2} c _ {j} q _ {j} ^ {2} (p)
$$

Although equilibrium conditions specified in Theorem 1 were derived in absence of contracts, Klemperer–Meyer equations reflecting contracts are well known (see for example Ref. [8]):

$$
\frac {\mathrm{d} q _ {- j}}{\mathrm{d} p} = \frac {q _ {j} - Y _ {j}}{p - c _ {j} q _ {j}} - \delta ; j = 1, 2, \dots , n\tag{29}
$$

In Ref. [7,8] Green discovered that Eq. (29) allows for a special linear solution in the form

$$
q _ {j} (p) = a _ {j} p + b _ {j}\tag{30}
$$

where slopes of supply functions $a _ { j }$ must satisfy the following simultaneous algebraic equations:

$$
a _ {- j} = \sum_ {i \neq j} a _ {i}
$$

$$
a _ {- j} = \frac {a _ {j}}{1 - c _ {j} a _ {j}} - \delta\tag{31}
$$

and with known slopes, intercepts $b _ { j }$ could be calculated as

$$
b _ {j} = Y _ {j} \left(1 - c _ {j} a _ {j}\right)\tag{32}
$$

Lemma 1. $H n { > } I ,$ system $( 3 l )$ has a unique positive solution ${ \hat { a } } _ { I } , { \hat { a } } _ { 2 } , . . . . , { \hat { a } } _ { n }$ such that

$$
\hat {a} _ {j} = \frac {1}{c _ {M}} \left[ \varepsilon_ {j} + \frac {(\hat {U} + \omega)}{2} - \sqrt {\varepsilon_ {j} ^ {2} + \frac {(\hat {U} + \omega) ^ {2}}{4}} \right]\tag{33}
$$

where

$$
\hat {U} = c _ {M} \sum_ {j = 1} ^ {n} \hat {a} _ {j}; \quad \hat {a} _ {j} c _ {j} <   1
$$

and $\hat { U }$ could be found from the following algebraic equation

$$
U = 1 + n \frac {U + \omega}{2} - \sum_ {j = 1} ^ {n} \sqrt {\varepsilon_ {j} ^ {2} + \frac {(U + \omega) ^ {2}}{4}}\tag{34}
$$

which has a unique positive solution $\hat { U }$ and

$$
0 <   \hat {U} <   1\tag{35}
$$

Intercepts of equilibrium supply functions $\hat { b _ { j } } ^ { \hat { } }$ are equal to

$$
\hat {\boldsymbol {b}} _ {j} = Y _ {j} (1 - c _ {j} \hat {\boldsymbol {a}} _ {j})
$$

and are nonnegative.

Eq. (29) could be rewritten in the following form

$$
q _ {j} (p) = \frac {Y _ {j} + p \left(q _ {- j} ^ {\prime} (p) + \delta\right)}{1 + c _ {j} \left(q _ {- j} ^ {\prime} (p) + \delta\right)}\tag{36}
$$

Eq. (36) could be interpreted as an optimal response of firm j to the aggregate supply function of its rivals $q _ { - j } ( p )$ if the latter is known, provided that the resulting supply function will be monotonically nondescending.

An important observation could be made from Eq. (36). If the aggregate supply function of rivals is linear, the responsive supply function of firm j will also be linear.

It is possible now to formulate the learning process as based on the following steps:

1. On day 1 each firm submits a trial supply function to the MA.

2. At the end of day 1, firms analyze the publicly available market statistics for each hour in that day: market clearing prices and total demand quantities. Using this information as well as their own supply functions, firms estimate aggregate supply functions of their competitors.

3. After these aggregate supply functions have been identified, firms use Eq. (36) to compute new supply functions to be used as their bids on the next day. These supply functions are optimal profit maximizing responses to supply functions of their competitors observed during day 1.

4. Firms submit these new adjusted supply functions to the coordinating entity for day 2. The process is repeated from Step 2.

Throughout this section, index k denotes the day number.

$$
7. 1. D a y 1 (k = 1)
$$

On day 1 all firms submit <sup>b</sup>perfectly competitive<sup>Q</sup> bids based on their marginal costs:

$$
\begin{array}{l} q _ {j} [ p, 1 ] = \frac {p}{c _ {j}}; \quad a _ {j} [ 1 ] = \frac {1}{c _ {j}}; \quad b _ {j} [ 1 ] = 0; \\ j = 1, 2, \ldots , n \end{array}\tag{37}
$$

As a result, during that day the MA will operate with the perfectly competitive supply function

$$
Q [ p, 1 ] = p \sum_ {j = 1} ^ {n} \frac {1}{c _ {j}} = A [ 1 ] p = \frac {p}{c _ {\mathrm{M}}}\tag{38}
$$

At the end of the day, each firm would be able to analyze market statistics—market clearing prices by hour and demand served by hour.<sup>2</sup> A simple regression analysis should easily reveal that the system-wide supply function on day 1 was linear with the slope of

$1 / { c _ { \mathrm { M } } } . ^ { 3 }$ That would allow each firm to compute the aggregate supply function of its competitors on day 1.

$$
q _ {- j} ^ {\prime} [ p, 1 ] = v _ {j} [ 1 ]
$$

$$
v _ {j} [ 1 ] = A [ 1 ] - a _ {j} [ 1 ] = \frac {1}{c _ {\mathrm{M}}} - \frac {1}{c _ {j}}
$$

$$
j = 1, 2, \dots , n
$$

## 7.2. Arbitrary day (k<sup>N</sup>1)

On any arbitrary day k, solving Eq. (36) leads to a new linear supply function of each player:

$$
q _ {- j} ^ {\prime} [ p, k - 1 ] = v _ {- j} [ k - 1 ]
$$

$$
v _ {- j} [ k - 1 ] = \frac {a _ {j} [ k ] - Y _ {j}}{1 - c _ {j} a _ {j} [ k ]} - \delta
$$

which yields slopes

$$
a _ {j} [ k ] = \frac {v _ {- j} [ k - 1 ] + \delta}{1 + c _ {j} \left\{v _ {- j} [ k - 1 ] + \delta \right\}}\tag{39}
$$

and intercepts

$$
b _ {j} [ k ] = Y _ {j} \left[ 1 - c _ {j} a _ {j} [ k ] \right]\tag{40}
$$

Slopes of competitors’ aggregated supply functions are equal to

$$
v _ {- j} [ k - 1 ] = \sum_ {j \neq i} a _ {j} [ k - 1 ]\tag{41}
$$

As discussed earlier, although Eq. (41) holds, firms do not need to use it in order to calculate aggregated slopes $\nu _ { - j } [ k - 1 ]$ . Instead, they estimate these coefficients through market observations.<sup>4</sup> However, in order to study the convergence of the learning process, Eq. (41) must be considered.

Lemma 2. A sequence of supply function coefficients defined by Eqs. (39)–(41) with initial conditions (Eq. (37)) converges to the linear SFE:

$$
\lim _ {k \to \infty} a _ {j} [ k ] = \hat {\boldsymbol {a}} _ {j}; \quad \lim _ {k \to \infty} b _ {j} [ k ] = \hat {\boldsymbol {b}} _ {j} = Y _ {j} [ 1 - c _ {j} \hat {\boldsymbol {a}} _ {j} ]
$$

where $\hat { a } _ { j }$ are defined by Eqs. (33) and (34).

Proof of this Lemma can be found in Appendix A. This lemma states in the mathematical form that firms could achieve an equilibrium bidding strategy by following a four-step procedure described above. The equilibrium could be reached without relying on information on production costs of competitors. Moreover, firms need no information regarding contractual commitments of their competitors. Indeed, on each step of the learning process, each firm relies entirely on the information regarding its own costs, its own contractual commitments, and results of the regression analysis of market-wide data. Finally, given that the learning process converges to a particular SFE (linear SFE), this resolves the ambiguity of the gametheoretical analysis relying on the SFE model of market interactions. An analysis of the speed of convergence could be found in the TCA Technical Paper [13].

## 8. Cournot adjustment process in piece-wise linear systems

The results presented in Example 2 appear encouraging enough to try to use the Cournot adjustment process in more general systems. In linear systems it was easy to identify the optimal response of each player and as long as all players operated with linear supply functions, optimal response on the next step of the Cournot adjustment process was again linear.

In this section we will demonstrate that a similar property would hold for piece-wise linear systems, and sketch the algorithm for construction an optimal supply function of a player responding to piece-wise linear aggregate supply function of competitors.

We assume that the cost function of the responding firm is monotonically increasing, continuous piecewise linear function of supply and, therefore, marginal cost function is step-wise. This assumption reasonably well reflects the economics of power generation with firms operating discreet generating units.

$$
C ^ {\prime} (q) = z _ {k} \text {   if   } Y _ {k - 1} <   q \leq Y _ {k}; k = \overline {{1 , u}}
$$

$$
Y _ {0} = 0; Y _ {m} = W\tag{42}
$$

where monotonically increasing quantities $Y _ { 1 } , . . . ,$ $Y _ { u - 1 } , W$ are cumulative capacities of u generating units and monotonically increasing values $z _ { 1 } , . . . , z _ { u }$ are their running costs.

Let us assume that the rival’s supply function $S ( p )$ is also a piece-wise linear function of price and therefore its derivative which exists at all prices except $P _ { 1 } , \ldots , P _ { N }$ is also a step-wise function:

$$
S ^ {\prime} (p) = s _ {k} \text {   if   } P _ {k - 1} <   p \leq P _ {k}; k = \overline {{2 , N}}\tag{43}
$$

We can also assume that demand is a piece-wise linear function of time and a linear function of price with zero cross-elasticity:

$$
\begin{array}{l} D (t, p) = \bar {D} (t) + \delta \bar {M} (t) - \delta p = D _ {\delta} (t) - \delta p \\ \bar {D} (t) = \bar {D} (t _ {k - 1}) + d _ {k} (t - t _ {k - 1}) \text { if } t _ {k - 1} \leq t \leq t _ {k} \\ \bar {M} (t) = \bar {M} (t _ {k - 1}) + m _ {k} (t - t _ {k - 1}) \text { if } t _ {k - 1} \leq t \leq t _ {k} \\ k = \overline {{1 , F}}; t _ {0} = 0, t _ {F} = \bar {T} \end{array}\tag{44}
$$

where $\bar { D } ( t )$ is system demand measured at reference prices $\bar { M } ( t )$ and d is the slope of demand responsiveness to price.

If we substitute Eqs. (42) and (43) into Eq. (6), the latter would yield the following bidding rule:

$$
B _ {j k} = z _ {j} + \frac {Y _ {j - 1} + x}{s _ {k} + \delta}\tag{45}
$$

suggesting the price at which the quantity x of the unit j should be offered to compete with the k-th segment of competitors’ supply function. Thus, in order to construct an optimal response supply function we can visualize an $N { \times } u$ grid on the $p \times q$ plane with formula (45) directing the potential growing segment of the supply functions within each rectangle in that grid. Vertical gridlines are defined by price points $P _ { 1 } , . . . , P _ { N } . \mathrm { ~ A ~ }$ part of the plane between two vertical gridlines defined by prices $P _ { k - 1 } , P _ { k }$ , we will call rivals’ segment k. Horizontal gridlines are at levels $Y _ { 1 } , . . . , Y _ { u - 1 } , W$ and a part of the plane between horizontal gridlines $Y _ { j - 1 } , Y _ { j }$ corresponds to unit $j .$ Thus, every rectangle on this grid corresponds to a combination of unit j and rivals’ segment k. The algorithm of forming the optimal response must yield a monotonically non-descending supply function such that if it is strictly monotonic within a particular rectangle it obeys the Eq. (45) bidding rule. The supply function could move vertically (quantity could increase in a jump) and/or horizontally (flat segment). At each end, the flat segment could be of a different kind: (1) connecting with a growth segment inside a rectangle; (2) connecting with a vertical jump along the gridline; (3) connecting with the problem boundary (left or right). With three possibilities at each end, there are overall nine types of flat segments. Lemma 1 below establishes additional rules and formulas allowing for an efficient search algorithm. In order to state it properly, we need to make several definitions.

Definition 2. Using formula (45), we can define the upper and lower bid limits for the unit within each rectangle:

$$
B _ {j k} ^ {-} = z _ {j} + \frac {Y _ {j - 1}}{s _ {k} + \delta}; B _ {j k} ^ {+} = z _ {j} + \frac {Y _ {j}}{s _ {k} + \delta}\tag{46}
$$

We will say that the rival’s segment k excites the unit j if $\cdot [ B _ { j k } ^ { - } , B _ { j k } ^ { + } ] \cap [ P _ { k - 1 } , P _ { k } ] \neq \emptyset .$

Definition 3. We will say that rival’s segment k initializes units up to j if each of the following is true:

$$
P _ {k - 1} <   z _ {j} <   P _ {k};
$$

$$
\begin{array}{c} \left[ Y _ {j - 1}, Y _ {j} \right] \cap [ D _ {\delta} (0) - S (P _ {k - 1}) - \delta P _ {k - 1}, D _ {\delta} (0) \\ - S (P _ {k}) - \delta P _ {k} ] \neq \emptyset ; \end{array}
$$

either $z _ { j + 1 } { > } P _ { k } \mathrm { o r } D _ { \delta } ( 0 ) - S ( z _ { j + 1 } ) - \delta z _ { j + 1 } { < } Y _ { k } .$

Definition 4. Let $P ^ { * } ( q )$ be a peak price in the system in the event of withholding all capacity above the level q : $S ( P ^ { * } ( q ) ) + q { = } D _ { \delta } ( T ^ { - } ) { - } \delta p$ and therefore $P ^ { * } ( q )$ is a monotonically non-descending function of q. We will say that rival’s segment k is in agreement with withholding all units above unit j if

$\exists q \in [ Y _ { j - 1 } , Y _ { j } ]$ such that $P _ { k - 1 } \bot P ^ { * } ( q ) \bot P _ { k }$

and 8x<sup>N</sup>0 $P ^ { * } \big ( Y _ { j } + x \big ) { > } P _ { j }$

Lemma 3. Let q(p) be the optimal response supply function

a) If $Y _ { j - I } { < } q ( p _ { 0 } ) { \leq } Y _ { j }$ and $P _ { k - I } { < } p _ { 0 } { \leq } P _ { k }$ , then rivals’ segment k initializes units up to j;

b) If $Y _ { j - I } { < } q ( p _ { I } ) { \leq } Y _ { j }$ and $P _ { k - I } { < } p _ { I } { \leq } P _ { k }$ , then rival’s segment k is in agreement with withholding all units above unit j;

c) q(p) is growing within a rectangle k,j if and only if rival’s segment k excites unit j and in this case

$$
q (p) = \left(p - z _ {j}\right) \left(s _ {k} + \delta\right)\tag{47}
$$

d) If rival’s segment k excites unit j but does not excite unit j+1, then it excites no units above j+1;

e) If rival’s segment k excites unit j but does not excite unit $j - l ,$ , then it does not excite units below $j - l ;$

f) Vertical jumps are possible only along a vertical gridline;

g) if q(p) jumps from level A corresponding to unit j to level B corresponding to (possibly a different) unit f along the vertical gridline separating rivals’ segments k and $k { + } l ,$ then

$$
\frac {s _ {k + 1} + \delta}{s _ {k} + \delta} > \frac {P _ {k} - z _ {j}}{P _ {k} - z _ {f}}
$$

and

$$
A \geq (s _ {k} + \delta) (P _ {k} - z _ {j})
$$

$$
B \leq (s _ {k + 1} + \delta) (P _ {k} - z _ {f})
$$

h) if q(p) has a flat segment at level A corresponding to unit j that stretches from price $p _ { - ; }$ , corresponding to rivals’ segment k to $p _ { + }$ , corresponding to rivals’ segment r, then

$$
\int_ {p _ {-}} ^ {p _ {+}} \frac {A - (S ^ {\prime} (p) + \delta) (p - z _ {j})}{D _ {t} ^ {\prime} (T (p))} d p = 0\tag{48}
$$

if q(p) has no vertical jumps at p<sub></sub> and $p _ { + }$ , then the unit j is excited by both segments k and r and $s _ { r } { < } s _ { k } ;$

i) if the flat segment terminates at the end-price, i.e. ${ p / + \overline { { \ l } } \ l } ^ { { = } } { p / \ l }$ and $A { = } W$ (no capacity withheld), then

$$
\int_ {p _ {-}} ^ {p _ {1}} \frac {W - (S ^ {\prime} (p) + \delta) (p - z _ {j})}{D _ {t} ^ {\prime} (T (p))} d p \leq 0\tag{49}
$$

This lemma is a direct interpretation of Theorem 1 applied to the case of piece-wise linear functions.

## 8.1. Sketch of the algorithm

The rules outlined in the lemma set the foundation for the efficient algorithm of inspecting the grid in search of the optimal supply function. It is important to note that in formulas (48) and (49) one has to integrate a piece-wise linear function of price which can be accomplished in closed form. The algorithm itself could be interpreted as a search of a feasible path connecting a rectangle initializing one or more units with a rectangle consistent with withholding of one or more units or ending at the highest vertical gridline. If no path is found, the optimal response is to offer no supply. Feasible path may obey Eq. (47) only if the unit corresponding to this rectangle is excited by the corresponding rivals’ segment. If feasible path does not obey Eq. (47), it can only be flat or jumps vertically upward along a vertical gridline. If the flat segment connects two growing segments, Eq. (47) relates prices at each end with the quantity level of the flat segment and Eq. (48) then has to be solved for that level only. If the flat segment merges with the vertical jump, it is again not difficult to solve Eq. (48), because one of the integration bounds is fixed at the price determining the jump gridline.

## 8.2. Numerical experiments and applications

We conducted two sets of numerical experiments using this algorithm for the Cournot adjustment process. In the first set we assumed that players observe the entire aggregate supply function of competitors. Under this assumption the process typically was not converging.

The second set of numerical experiments was based on the analytical representation of what each player assumes with respect to the behavior of its competitors, rather than merely expecting the overall system to be at equilibrium. This is a realistic assumption, because players in the electricity market have no exact information with respect to running costs of their rivals’ generating units. Therefore, even if they were capable of computing the exact equilibrium, information required to perform such computations is not readily available. On the other hand, players can rely upon market observation. In particular, each player can observe hourly prices in the market (locational and/or regional) as well as total and/or regional quantity of electricity consumed. Each player also knows hourly quantity it produced and can compute the total quantity produced by its rivals at any point in time. Thus, a player j observes p(t)and estimates $S _ { j } ( t )$ and therefore can develop an estimate of $S _ { j } ( p )$ using these data. It is only logical to approximate $S _ { j } ( p )$ with a piece-wise linear function. Next, each player can solve a problem of optimal response given that estimated rivals’ supply function generates a new market outcome prompting for the next iteration. Apparently, using thus estimated rivals’ supply function instead of a directly computed one makes the process converge. We were not able to obtain a formal proof of convergence.

We implemented a first version of this algorithm as the basis for the TCA COMPEL-21 Model. We use COMPEL-21 in conjunction with GE ${ \mathrm { M A P S } } ^ { 5 }$ in the following manner. First, we make a standard GE MAPS run assuming that all generators are dispatched based on short-run marginal costs. We use the results of this run for an initial calibration of competitors’ supply functions. Next, COMPEL-21 simulates a Cournot adjustment process using the algorithm described above. The results of COMPEL-21 are then used to adjust generators’ bids on a unit-by-unit basis. Adjusted bids are then used as an input for a new GE MAPS run. We apply this logic to modeling the Northeastern power system combining New England, New York, PJM, Ontario and New Brunswick.

## Appendix A

Proof of Theorem 1. Consider the optimal control problem arising from the problem of optimal response of one player, i.e. assume that the aggregate supply function $q _ { - j } ( p )$ of all competitors to firm j is known; it is price-wise differentiable and monotonically nondescending. We formulate the optimal response of firm j in the following way:

$$
\begin{array}{l} \min \left(- \pi_ {j}\right) = - \int_ {p _ {0}} ^ {p _ {1}} \left[ p q _ {j} (p) - C _ {j} \big (q _ {j} (p) \big) \right] T ^ {\prime} (p) \mathrm{d} p \\ + (1 - \beta) \int_ {p _ {0}} ^ {p _ {1}} (\bar {T} - T (p)) q _ {j} (p) \mathrm{d} p \end{array}
$$

$$
\begin{array}{l} \text { s.t. } ^ {6} \\ \frac {\mathrm{d} q _ {j} (p)}{\mathrm{d} p} = u _ {j} (p); \\ u _ {j} (p) \geq 0; \\ q _ {j} (p) + q _ {- j} (p) = D (T (p), p) \\ T (p _ {0}) = 0; \\ - q _ {j} (p _ {0}) \leq 0; \\ q _ {j} (p _ {1}) \leq W _ {j}; \end{array}
$$

$$
T (p _ {1}) = \bar {T};\tag{OR}
$$

We will use the Lagrangian form of optimality conditions [10]. First, we define the Lagrangian of problem (OR) which is equal to

$$
\begin{array}{l} L \big (q _ {j}, q _ {j} ^ {\prime}, T, T ^ {\prime}, u _ {j}, p \big) = T ^ {\prime} \left[ C _ {j} \big (q _ {j} \big) - p q _ {j} \right] \\ \qquad + (1 - \beta) \big [ \bar {T} - T \big ] q _ {j} \\ \qquad + \psi_ {j} \big [ q _ {j} ^ {\prime} - u _ {j} \big ] \\ \qquad + \lambda \big [ q _ {j} + q _ {- j} (p) - D (T, p) \big ] \end{array}
$$

where $\psi _ { j } , \lambda$ are Lagrange multipliers. Next, we define the terminal function

$$
l (q _ {j} (p _ {0}), q _ {j} (p _ {1})) = - \mu q _ {j} (p _ {0}) + \eta [ q _ {j} (p _ {1}) - W _ {j} ]
$$

The optimality conditions are then could be expressed in the following way: Lagrange–Euler Equations

$$
\frac {\mathrm{d}}{\mathrm{d} p} \frac {\partial L}{\partial q _ {j} ^ {\prime}} - \frac {\partial L}{\partial q _ {j}} = 0;
$$

$$
\frac {\mathrm{d}}{\mathrm{d} p} \frac {\partial L}{\partial T ^ {\prime}} - \frac {\partial L}{\partial T} = 0;\tag{LE}
$$

Pontryagin optimality principle (POP): at each point of the optimal trajectory the Lagrangian must reach its minimum as a function of control variables:

$$
\begin{array}{l} L \big (q _ {j} (p), q _ {j} ^ {\prime} (p), T (p), T ^ {\prime} (p), u _ {j} (p), p \big) \\ = \min _ {u _ {j} \geq 0} L \big (q _ {j} (p), q _ {j} ^ {\prime} (p), T (p), T ^ {\prime} (p), u _ {j}, p \big) \end{array}\tag{POP}
$$

Transversality conditions

$$
\left. \frac {\partial L}{\partial q _ {j} ^ {\prime}} \right| _ {p = p _ {0}} = \frac {\partial l}{\partial q _ {j} (p _ {0})}; \left. \frac {\partial L}{\partial q _ {j} ^ {\prime}} \right| _ {p = p _ {1}} = - \frac {\partial l}{\partial q _ {j} (p _ {1})}.\tag{TC}
$$

Complimentarity conditions

$$
\mu q _ {j} (p _ {0}) = 0;
$$

$$
\mu \geq 0;
$$

$$
\eta \left[ q _ {j} (p _ {1}) - W _ {j} \right] = 0;
$$

$$
\eta \geq 0.\tag{CC}
$$

Eq. (LE) are:

$$
\begin{array}{l} \frac {\mathrm{d} \psi_ {j}}{\mathrm{d} p} = \lambda + (1 - \beta) [ \bar {T} - T ] + T ^ {\prime} [ C _ {j} ^ {\prime} - p ]; \\ q _ {j} ^ {\prime} [ p - C _ {j} ^ {\prime} ] + \beta q _ {j} = \lambda D _ {t} ^ {\prime}. \end{array}\tag{A-1}
$$

The POP could be reduced to the consideration of the only term in the Lagrangian that depends on the control function $u _ { j } { \mathrm { : } }$

$$
\min _ {u _ {j} \geq 0} \left[ - u _ {j} \psi_ {j} \right] = - \max _ {u _ {j} \geq 0} \left[ u _ {j} \psi_ {j} \right]\tag{A-2}
$$

Eq. (A-2) indicates that if the adjoint function is positive, $\psi _ { j } { > } 0$ , then there exists no optimal value of the control function $u _ { j } ,$ hence the optimality requires $\psi _ { j } { \le } 0$ . The control function could be positive if only the adjoint function is equal to zero. Finally, if the adjoint function is negative, the optimal control function must be at zero. In other words, if the supply function $q _ { j }$ is growing on some interval of prices, the adjoint function must remain equal to zero on that interval. If the adjoint function is negative on some interval of prices, the supply function must remain constant on that interval.

Consider the case of the growing supply function. Since the adjoint function is zero on the interval of growth, its derivative must also be zero on that interval. Combining that with Eq. (A-1), we get

$$
\begin{array}{c} D _ {t} ^ {\prime} \lambda = T ^ {\prime} D _ {t} ^ {\prime} \left[ p - C _ {j} ^ {\prime} \right] - (1 - \beta) D _ {t} ^ {\prime} \left[ \bar {T} - T \right] \\ = q _ {j} ^ {\prime} \left[ p - C _ {j} ^ {\prime} \right] + \beta q _ {j}. \end{array}\tag{A-3}
$$

On the other hand, by differentiating the <sup>b</sup>supply equals demand<sup>Q</sup> equation, we derive that

$$
T ^ {\prime} D _ {t} ^ {\prime} = q _ {j} ^ {\prime} + q _ {- j} ^ {\prime} - D _ {p} ^ {\prime}.\tag{A-4}
$$

Substitution of Eq. (A-4) into Eq. (A-3) yields the following equation:

$$
q _ {- j} ^ {\prime} = \frac {\beta q _ {j} + (1 - \beta) (\bar {T} - T) D _ {t} ^ {\prime}}{p - C _ {j} ^ {\prime}} + D _ {p} ^ {\prime}\tag{A-5}
$$

which proves statement (2) of the theorem.

By combining Eq. (A-1) with Eq. (A-4) and eliminating k, we obtain the following differential equation for the adjoint function which, as one can see, holds regardless of whether the supply function is growing or flat:

$$
\begin{array}{l} \frac {\mathrm{d} \psi_ {j}}{\mathrm{d} p} = (1 - \beta) (\bar {T} - T) \\ + \frac {\beta q _ {j} - [ p - C _ {j} ^ {\prime} (q _ {j}) ] [ q _ {- j} ^ {\prime} - D _ {t} ^ {\prime} (T , p) ]}{D _ {t} ^ {\prime} (T , p)} \end{array}\tag{A-6}
$$

If $q _ { j } ( p )$ is growing, the right hand side in Eq. (A-6) is equal to zero due to Eq. (A-5). $\operatorname { I f } q _ { j } ( p )$ stays constant, the adjoint Eq. (A-6) takes the following form:

$$
\begin{array}{l} \frac {\mathrm{d} \psi_ {j}}{\mathrm{d} p} = (1 - \beta) [ \bar {T} - T ] \\ \qquad + \left[ p - C _ {j} ^ {\prime} \left(q _ {j} ^ {*}\right) + \frac {\beta q _ {j} ^ {*}}{q _ {- j} ^ {\prime} (p) - D _ {p} ^ {\prime}} \right] T ^ {\prime} \end{array}\tag{A-7}
$$

where $q _ { J } ^ { * }$ is the level at which the supply function remains flat.

This proves statement (3) of the theorem.

Statement (4) is obvious; it could be interpreted as the formula to compute the IPDF given all supply functions.

Finally, the transversality conditions (TC) result in the following:

$$
\mu = - \psi_ {j} (p _ {0}); \eta = - \psi_ {j} (p _ {1}).\tag{A-8}
$$

By combining Eq. (A-8) with the complimentarity conditions (CC), we get

$$
\begin{array}{l} \psi_ {j} (p _ {0}) q _ {j} (p _ {0}) = 0; \psi_ {j} (p _ {0}) \leq 0; q _ {j} (p _ {0}) \geq 0; \\ \psi_ {j} (p _ {1}) \big [ q _ {j} (p _ {1}) - W _ {j} \big ] = 0; \psi_ {j} (p _ {1}) \leq 0; q _ {j} (p _ {1}) \leq W _ {j}. \end{array}\tag{A-9}
$$

That proves statement (5) of the Theorem.

Let us assume that the supply function has a vertical jump from q<sub></sub> to $q _ { + }$ at price p. This jump could be optimal only if $\psi _ { j } ( p ) { = } 0$ . Given that the adjoint function cannot be positive, the latter is possible only if $\psi _ { j } ^ { \prime } ( p - ) { \geq } 0$ and $\psi _ { j } ^ { \prime } ( p \mathrm { + } ) \mathrm { { \le } } 0$ . Using Eq. (A-6), we get that

$$
\begin{array}{c} \beta q _ {-} \geq \left[ p - C _ {j} ^ {\prime} (q _ {-}) \right] \left[ q _ {- j} ^ {\prime} (p -) - D _ {p} ^ {\prime} \right] \\ - (1 - \beta) (\bar {T} - T) D _ {t} ^ {\prime} \end{array}
$$

$$
\begin{array}{l} \beta q _ {+} \leq \left[ p - C _ {j} ^ {\prime} (q _ {+}) \right] \left[ q _ {- j} ^ {\prime} (p +) - D _ {p} ^ {\prime} \right] \\ - (1 - \beta) (\bar {T} - T) D _ {t} ^ {\prime} \end{array}
$$

Since $q _ { + } { > } q _ { - }$ and $\beta { > } 0 ,$ , the above two inequalities imply that the $q _ { - j } ^ { \prime } ( p + ) > q _ { - j } ^ { \prime } ( p - )$ , and moreover

$$
\frac {q _ {- j} ^ {\prime} (p +) - D _ {p} ^ {\prime}}{q _ {- j} ^ {\prime} (p -) - D _ {p} ^ {\prime}} > \frac {p - C _ {j} ^ {\prime} (q _ {-})}{p - C _ {j} ^ {\prime} (q _ {+})}.\tag{A-10}
$$

If b=0, the same inequality will hold if $C _ { j } ^ { \prime } ( q _ { - } ) ^ { < }$ $C _ { j } ^ { \prime } ( q _ { + } )$ . Otherwise, the inequality (A-10) would have to be restated as a non-strict (with a <sub>z</sub> sign). 5

Proof of Lemma 1. Consider Eq. (31), and rewrite it in the following form

$$
A - a _ {j} = \frac {a _ {j}}{1 - c _ {j} a _ {j}} - \delta ; \quad A = \sum_ {j = 1} ^ {n} a _ {j}\tag{A-11}
$$

The first equation could be easily represented as the following quadratic equation for $a _ { j }$

$$
c _ {j} a _ {j} ^ {2} - \left[ c _ {j} (A + \delta) + 2 \right] a _ {j} + (A + \delta) = 0
$$

Two solutions to this equation are

$$
a _ {j} ^ {1, 2} = \frac {1}{c _ {j}} + \frac {A + \delta}{2} \pm \frac {1}{2 c _ {j}} \sqrt {\frac {1}{c _ {j} ^ {2}} + \frac {(A + \delta) ^ {2}}{4}}
$$

One can easily verify that the <sup>b</sup>plus<sup>Q</sup> branch of this solution is meaningless; it leads to the equation for A with no positive roots. This leaves us with the <sup>b</sup>minus<sup>Q</sup> branch.

$$
\begin{array}{l} a _ {j} = \frac {1}{c _ {j}} + \frac {A + \delta}{2} - \frac {1}{2 c _ {j}} \sqrt {\frac {1}{c _ {j} ^ {2}} + \frac {(A + \delta) ^ {2}}{4}} \\ = \frac {1}{c _ {\mathrm{M}}} \left[ \varepsilon_ {j} + \frac {(U + \omega)}{2} - \sqrt {\varepsilon_ {j} ^ {2} + \frac {(U + \omega) ^ {2}}{4}} \right] \end{array}
$$

where

$$
U = c _ {\mathrm{M}} A; \qquad \omega = c _ {\mathrm{M}} \delta\tag{A-12}
$$

This proves formula (33).

Recall now the definition of A in formula (A-11) and substitute Eq. (A-12) into that definition

$$
\begin{array}{l} \frac {U}{c _ {\mathrm{M}}} = A = \sum_ {j = 1} ^ {n} a _ {j} \\ = \frac {1}{c _ {\mathrm{M}}} \sum_ {j = 1} ^ {n} \left[ \varepsilon_ {j} + \frac {(U + \omega)}{2} - \sqrt {\varepsilon_ {j} ^ {2} + \frac {(U + \omega) ^ {2}}{4}} \right] \\ = \frac {1}{c _ {\mathrm{M}}} \left[ 1 + n \frac {(U + \omega)}{2} - \sum_ {j = 1} ^ {n} \sqrt {\varepsilon_ {j} ^ {2} + \frac {(U + \omega) ^ {2}}{4}} \right] \end{array}
$$

We now receive an algebraic equation for U

$$
U = 1 + n \frac {(U + \omega)}{2} - \sum_ {j = 1} ^ {n} \sqrt {\varepsilon_ {j} ^ {2} + \frac {(U + \omega) ^ {2}}{4}}
$$

which coincides with Eq. (34).

The left-hand side (LHS) in this equation is a linear function of U. After differentiating the right-hand side (RHS) twice, one can find that the second derivative is negative, hence RHS is a concave function of U. Moreover, a simple check indicates that at $U { = } 0 ,$ , the RHS is positive while the LHS is zero. The concave curve defined by the RHS starts at $U { = } 0$ above the straight line defined by the LHS and it can intersect the straight line at some U<sup>N</sup>0 only once. Therefore, Eq. (34) has a unique positive solution.

Finally, a simple check shows that if $U { = } 1$ the LHS equals 1 and the RHS is less than 1. Therefore, the root is inside the interval $0 { < } U { < } 1$ 5

Proof of Lemma 2. Consider the equations of the learning process

$$
a _ {j} [ k ] = \frac {v _ {- j} [ k - 1 ] + \delta}{1 + c _ {j} \left\{v _ {- j} [ k - 1 ] + \delta \right\}}\tag{A-13}
$$

$$
v _ {- j} [ k - 1 ] = \sum_ {m \neq j} a _ {m} [ k - 1 ]\tag{A-14}
$$

$$
k = 2, 3, \dots ;
$$

$$
a _ {j} [ 1 ] = \frac {1}{c _ {j}}; j = 1, 2, \dots , n
$$

Compare a[1] and a[2]:

$$
\begin{array}{l} a _ {j} [ 2 ] = \frac {\frac {1}{c _ {\mathrm{M}}} - \frac {1}{c _ {j}} + \delta}{1 + c _ {j} \left[ \frac {1}{c _ {\mathrm{M}}} - \frac {1}{c _ {j}} + \delta \right]} = \frac {\frac {1}{c _ {\mathrm{M}}} - \frac {1}{c _ {j}} + \delta}{\frac {c _ {j}}{c _ {\mathrm{M}}} + c _ {j} \delta} \\ c _ {j} a _ {j} [ 2 ] = 1 - \frac {1}{\frac {c _ {j}}{c _ {\mathrm{M}}} + c _ {j} \delta} <   1 \\ a _ {j} [ 2 ] <   \frac {1}{c _ {j}} = a _ {j} [ 1 ] \end{array}
$$

Thus, all supply function slopes for day 2 are lower than corresponding slopes for day 1. This and Eq. (A-14) imply that v ${ \bf \Phi } _ { - j } [ 2 ] { < } \nu _ { - j } [ 1 ]$ . A simple differentiation of the RHS of $( \mathrm { A } \cdot 1 3 )$ by $\dot { \nu } _ { - j } [ k - 1 ]$ indicates that it is a monotonically growing function of this variable. Therefore, inequality $\nu _ { - j } [ 2 ] { < } \nu _ { - j } [ 1 ]$ implies

$$
\begin{array}{l} a _ {j} [ 3 ] = \frac {v _ {- j} [ 2 ] + \delta}{1 + c _ {j} \left\{v _ {- j} [ 2 ] + \delta \right\}} <   \frac {v _ {- j} [ 1 ] + \delta}{1 + c _ {j} \left\{v _ {- j} [ 1 ] + \delta \right\}} \\ = a _ {j} [ 2 ] \end{array}
$$

The latter means that $a _ { j } [ 3 ] { < } a _ { j } [ 2 ]$ . Similarly, one can prove by induction that for each firm, $a _ { j } [ k ]$ is a monotonically descending with $k$ sequence. Moreover, on each day k, slopes $a _ { j } [ k ]$ are positive because the RHS in $\mathrm { E q . ~ } ( \mathrm { A } \mathrm { - } 1 3 )$ is always positive. Therefore, for each firm $j ,$ the sequence $a _ { j } [ k ]$ is bounded from below. A positive monotonically descending and bounded from below sequence converges to a nonnegative value. Therefore, for any j there exist a nonnegative number $\hat { a } _ { j }$ such that $\begin{array} { r } { \operatorname* { l i m } _ { k \to \infty } a _ { j } [ k ] = \hat { a } _ { j } } \end{array}$ Finally, let us prove that $\hat { a } _ { j }$ are equilibrium slopes. To do so, let us introduce for each j a residual sequence $e _ { j } [ k ]$ such that

$$
a _ {j} [ k ] = \hat {a} _ {j} + e _ {j} [ k ];
$$

where

$$
e _ {j} [ k ] \rightarrow 0 \text {   as   } k \rightarrow_ {\infty}
$$

and substitute this expression into Eq. (A-13):

$$
\hat {a} _ {j} + e _ {j} [ k ] = \frac {\sum_ {m \neq j} [ \hat {a} _ {m} + e _ {m} [ k - 1 ] ] + \delta}{1 + c _ {j} \left\{\sum_ {m \neq j} [ \hat {a} _ {m} + e _ {m} [ k - 1 ] ] + \delta \right\}}.
$$

When k tends to infinity, the latter equation converges to

$$
\hat {a} _ {j} = \frac {\sum_ {m \neq j} \hat {a} _ {m} + \delta}{1 + c _ {j} \left\{\sum_ {m \neq j} \hat {a} _ {m} + \delta \right\}}
$$

which is equivalent to

$$
\sum_ {m \neq j} \hat {a} _ {m} = \frac {\hat {a} _ {j}}{1 - c _ {j} \hat {a} _ {j}} - \delta .
$$

The last equation represents equilibrium conditions for slopes in the form of Eq. (31). Since Eq. (31) has a unique solution given by Eqs. (33) and (34)), this solution is the limit to which the slopes converge in the learning process. 5

## References

[1] E.J. Anderson, A.B. Philpott, Optimal offer construction in electricity markets, Mathematics of Operations Research 27 (2001) 82–100.

[2] E.J. Anderson, H. Xu, Necessary and sufficient conditions for optimal offers in electricity markets, SIAM Journal of Control and Optimization 41 (4) (2002) 1212 – 1228.

[3] R. Baldick, W. Hogan, Capacity Constrained Supply Function Equilibrium Models of Electricity Markets: Stability, Nondecreasing constraints, and Function Space Iterations. POWER Working Paper PWP-089, University of California Energy Institute, Berkeley, CA, December 2001.

[4] R. Baldick, R. Grant, E. Kahn, Linear Supply Function Equilibrium: Generalizations, Application, and Limitations, POWER Working Paper PWP-078, University of California Energy Institute, Berkeley, CA, August 2000.

[5] C.J. Day, B.F. Hobbs, J.-S. Pang, Oligopolistic competition in power networks: a conjectured supply function approach, IEEE Transactions on Power Systems 17 (3) (2002) 597– 606.

[6] D. Fudenberg, D.K. Levine, The Theory of Learning in Games, The MIT Press, Cambridge, MA, 2002.

[7] R.J. Green, Increasing competition in the British electricity spot market, Journal of Industrial Economics 44 (1996) 205–216.

[8] R.J. Green, The electricity contract market in England and Wales, Journal of Industrial Economics 47 (1) (1997) 107– 123.

[9] R.J. Green, D.M. Newbery, Competition in the British electric spot market, Journal of Political Economy 100 (1992) 929–953.

[10] A.D. Ioffe, V.M. Tihomirov, Theory of Extremal Problems, Elsevier, North Holland, 1979.

[11] P.D. Klemperer, M.A. Meyer, Supply function equilibria, Econometrica 57 (1989) 1243 – 1277.

[12] D.M. Newbery, Competition, contracts and entry in the electricity spot market, Rand Journal of Economics 29 (1998) 726– 749.

[13] A. Rudkevich, Supply Function Equilibrium in Power Markets: Learning All the Way, 1999, TCA Technical Paper 1299-1702, available at www.tca-us.com.

[14] A. Rudkevich, M. Duckworth, R. Rosen, Modeling electricity pricing in a deregulated generation industry: the potential for oligopoly pricing in a Poolco, The Energy Journal 19 (3) (1998) 19– 48.

[15] A. Rudkevich, P. Capozzoli, J. Cardell, E. Hausman, R. Hornby, A. Zobian, Horizontal Market Power in Wisconsin. A Report to the Public Commission of Wisconsin Submitted by Tabors Caramanis and Associates, November 2000, available at www.tca-us.com.

## 9. Further reading

[5]

Dr. Rudkevich, is a Director of the Modeling Group at Tabors Caramanis and Associates. He has over 20 years of experience in energy economics, regulatory policy and strategic planning. At TCA, Dr. Rudkevich manages projects and directs analyses of economic, policy and technical issues related to the electric and natural gas industry deregulation; market design; simulation and theoretical analysis of markets for electric energy, capacity, ancillary services, financial transmission rights and marginal losses; market power and mitigation measures; valuation of generation and transmission assets; and fuel price forecasting. He received PhD in Energy Economics and Technology from the Siberian Energy Institute of Academy of Sciences in Irkutsk, Russia and MS in Applied Mathematics from the Moscow Institute of Oil and Gas.
