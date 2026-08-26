---
otero_id: 8490
otero_key: "K5RAAHJ8"
title: "Cooperation and profit allocation in distribution chains"
authors: "Luis A. Guardiola; Ana Meca; Judith Timmer"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.12.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cooperation and profit allocation in distribution chains<sup>☆</sup>

Luis A. Guardiola <sup>a,⁎</sup>, Ana Meca <sup>a</sup>, Judith Timmer <sup>b</sup>

<sup>a</sup> Operations Research Center, Universidad Miguel Hernández, Edificio Torretamarit, Avda. de la Universidad s.n, 03202 Elche (Alicante), Spain <sup>b</sup> Stochastic Operations Research Group, Department of Applied Mathematics, University of Twente, Enschede, The Netherlands

Received 13 September 2005; received in revised form 21 December 2006; accepted 27 December 2006 Available online 23 January 2007

## Abstract

We study the coordination of actions and the allocation of profit in supply chains under decentralized control in which a single supplier supplies several retailers with goods for replenishment of stocks. The goal of the supplier and the retailers is to maximize their individual profits. Since the outcome under decentralized control is inefficient, cooperation among firms by means of coordination of actions may improve the individual profits. Cooperation is studied by means of cooperative game theory. Among others we show that the corresponding games are balanced and we propose a stable solution concept for these games. © 2007 Elsevier B.V. All rights reserved.

PACS: 91A12; 90B99 Keywords: Distribution chain; Cooperative game; Balancedness; Mgpc-solution

## 1. Introduction

The study of the coordination of actions and the allocation of profits in distribution chains are becoming popular topics nowadays. In the literature on distribution channel coordination both cooperative and noncooperative game theory are used quite often to investigate these topics. There are some differences between the use of noncooperative and cooperative game theory. When applying noncooperative game theory it is assumed that each company in the supply chain is an independent decision-maker that acts in accordance with its objective. One of the main points of concern is whether some proposed coordination mechanism coordinates the supply chain, that is maximizes the total profit of the supply chain, under a competitive framework.

In contrast, cooperative game theory assumes that companies can make binding agreements. One of the main questions here is whether the cooperation is stable, that is, whether there are allocations of the total profit among the companies such that no group of companies would like to cooperate on its own.

Channel coordination is an issue that has been investigated under several perspectives. Its main goal is to improve total profits and welfare. In this paper, we focus on the analysis of supply chains by means of cooperative games. In particular, we consider single period distribution chains with a single product. In such a supply chain, retailers place one-time orders for the product at the supplier. After production, the supplier delivers the goods to the retailers via a warehouse. This warehouse acts as an intermediary without costs or revenues. When the goods arrive, the noncompeting retailers sell these on their own separate markets. The larger the quantity that is put on the market, the lower the expected revenue per unit for the retailer. Each retailer chooses its order quantity such that its profit is maximized.

The retailer pays the supplier a wholesale price per unit product ordered and delivered. This price is a decreasing function of the quantity ordered. Hence, incentives for cooperation among retailers exist. If the retailers combine their orders into one large order then they enjoy a lower wholesale price per unit. They can do so because the warehouse only informs the supplier about the quantities ordered and not about which retailer orders how much. Besides, retailers may want to cooperate with the supplier which implies a further reduction in cost inefficiency due to the absence of the intermediate wholesale prices. Obviously, the total profit under full cooperation is larger than the sum of the individual profits.

Because of the incentives for cooperation, we use cooperative game theory to study these distribution chains. For each chain we define a corresponding cooperative game in which the supplier and the retailers are the players. The value of a coalition of players equals the optimal joint profit they can achieve. We show that the core of such a game is never empty, that is, all companies in the chain are willing to cooperate because there exist stable distributions of the total profit among the companies upon which no coalition can improve. Any distribution of profits that belongs to the core has a nice interpretation in terms of the underlying distribution chain. Further, we introduce a specific allocation of the total profit for distribution chains, the so-called minimalgain-per-capita (mgpc) solution. This solution is a stable distribution of the profits, that is, it always belongs to the core of the game, and it possess several nice properties. In particular, it takes into account the importance of the supplier to achieve full cooperation. Finally, a characterization of the mgpc-solution is provided.

Our paper contributes to the emerging literature on the analysis of problems in Operations Research by means of cooperative game theory. Some recent papers in this area are [7,12,8,9,23], and for a survey we refer to [4]. Closely related to our work are papers that focus on cooperation in supply chains by means of cooperative games. Perhaps one of the first to do so is [15], who uses cooperative game theory to study the allocation of joint inventory control costs among multiple retailers. The author shows that the Shapley value [16] of the corresponding cooperative game belongs to the core, and as such is a fair and suitable allocation for sharing the costs. In [25] a three-player news-vendor game is analyzed by means of both noncooperative and cooperative game theory. Among others, conditions are given such that the core of related cooperative games is nonempty and the authors conclude that full cooperation cannot always be obtained. [19] studies joint ordering by multiple retailers. The authors study a related cooperative game in which the retailers are the players. Their main result is that this game has a nonempty core. This result is extended in subsequent studies [14,20]. Noncooperative game theory is also used to study problems in supply chains namely, among others, to study coordination mechanisms, like contracts, under horizontal and vertical competition. We refer to [1,2,5,6,11,21,22,24] for reviews on analyses of contracts. Finally, [13] analyses collaboration for the economic order quantity model by using bargaining concepts from noncooperative and cooperative game theory.

The contribution of our paper to the literature is twofold. First, we include the supplier in our analysis and study cooperation among retailers and the supplier. Second, we introduce a tailor-made allocation of the joint profit that always belongs to the core of the game. The above-mentioned literature only considers cooperation among retailers and hardly pays attention to suitable allocations of the joint benefits.

The contents of this paper are as follows. In the next section we introduce the necessary concepts of cooperative game theory. Our model of a single period distribution chain is introduced and studied in Section 3. A related cooperative game, the RS-game, is studied in Section 4. Thereafter, in Section 5, we show that RSgames always have a nonempty core. Any allocation in the core is shown to have a nice interpretation in terms of its underlying distribution chain. In Section 6 we introduce and study the mgpc-solution for RS-games. We show that it belongs to the core and characterize it. Section 7 concludes.

## 2. Preliminaries cooperative game theory

A cooperative (benefit) game with transferable utility (TU game) is a pair (N, v) where $N = \{ 1 , 2 , . . . , n \}$ is the finite player set. Let P(N) be the set containing all subsets of N then v : $P ( N ) \longrightarrow$ R is the characteristic function of the <sup>ð Þ</sup>game satisfying v(t) = 0. A coalition is a nonempty subset of N. The subgame $\nu _ { S }$ related to coalition S is the restriction of the mapping v to the subcoalitions of S. We denote by s the cardinality of the set $S \subseteq N ,$ i.e. $\operatorname { c a r d } ( S ) = s .$ A benefit vector, or allocation, is denoted by $x \in \mathbb { R } ^ { n }$ . The core of the game $( N , \nu )$ consists of those allocations of $\nu ( N )$ in which each coalition receives at least its benefit as prescribed by the characteristic function: Core $( N , \nu ) =$ $\textstyle \left\{ x \in \mathbb { R } ^ { n } / \sum _ { i \in N } x _ { i } = \nu ( N ) \right.$ and $\textstyle \sum _ { i \in S } x _ { i } \geq \nu ( S )$ <sup>Þ ¼</sup>for all $S \subset N \}$ <sup>¼ ð Þ</sup>. A core-allocation $x { \in } \mathbf { C } \operatorname { o r e } ( N , \ \nu )$ <sup>Þ</sup>is both <sup>g</sup>efficient, that is $\begin{array} { r } { \sum _ { i \in N } x _ { i } = \nu ( N ) } \end{array}$ , and it satisfies the <sup>¼ ð Þ</sup>coalitional stability property, that is $\textstyle \sum _ { i \in S } x _ { i } \geq \nu ( S )$ for all $S \subset N . \mathrm { ~ A ~ }$ <sup>ð Þ</sup>game (N, v) is balanced if and only if it has a nonempty core [3,17]. It is a totally balanced game if all its subgames are balanced.

A game $( N , \nu )$ is strict monotone increasing if $\nu ( S ) <$ $\nu ( T )$ for all $S \subset T .$ It is superadditive $\mathrm { i f } \nu ( S \cup T ) \geq \nu ( S ) +$ $\nu ( T )$ holds for all disjoint coalitions S and T. In a superadditive game, it is always beneficial for two disjoint coalitions to cooperate and form a larger coalition. A well-known class of balanced and superadditive games is the class of convex games [18]. A game $( N , \nu )$ is convex if $\nu ( S \cup \{ i \} ) - \nu ( S ) \leq \nu ( T \cup \{ i \} ) - \nu ( T )$ for all $i \in N$ and for all $S \subseteq T \subseteq N \setminus \{ i \}$

A single-valued solution $\varphi$ for TU games $( N , \nu )$ is a map $\varphi : \bar { { \cal I } ^ { N } } { \longrightarrow } \mathbb { R } ^ { N }$ where $T ^ { N }$ is the class of TU-games with player set N. The payoff to player $i \in N$ in game $\nu \in T ^ { \bar { N } }$ according to this solution is denoted by $\varphi _ { i } ( \nu )$ and $\varphi ( \nu ) { = } ( \varphi _ { i } ( \nu ) ) _ { i \in N }$

We denote by $\mathbb { R } _ { + } ^ { n }$ the set of n-dimensional real <sup>þ</sup>vectors whose components are nonnegative. For $a , \ b \in \mathbb { R } , a < b , [ a , b ]$ is a closed interval and $( a , b )$ an <sup>½</sup>open interval in R.

## 3. Retailer–supplier problems

In this paper we study single period models of distribution chains involving a single product. In these chains, a supplier replenishes his goods to several retailers via a warehouse. One can think, for example, of a car manufacturer (supplier) who is about to produce a car with special features that will only be temporarily available. This is a single period model in which the local car dealers (retailers) have one opportunity to place their orders for this special car at the national importer (warehouse), who passes the national orders to the car manufacturer. In this section we first concentrate on a chain with a single retailer. Chains with multiple retailers are considered in the next section.

The retailer places a one-time order, say of size q units, for the good at the warehouse, who passes this information to the supplier. The costs of this order are $w ( q )$ per unit for the retailer, where the wholesale price function $w : \mathbb { R } _ { + } { \longrightarrow } ( c , + \infty ) ( \mathrm { i . e . ~ } w ( q ) { > } c$ for all $q { \geq } 0 )$ is a de-<sup>þ ð þ Þð ð Þ Þ</sup>creasing and continuous function. Its decreasing nature represents quantity discounts provided by the supplier: the more the retailer orders, the lower the price per unit he has to pay. The ordered goods are produced by the supplier at a cost of c per unit. After production the goods are shipped to the warehouse, who acts as an intermediate party with no costs or benefits. The warehouse sends the goods to the retailer, who in turn sells the goods on the market. The expected revenue of the retailer is $p ( q )$ per unit of the good, given the supply of q units on the consumer market. The expected price function $p : \mathbb { R } _ { + } { \longrightarrow } \mathbb { R }$ is decreasing and continuous in $q ,$ satisfies $p ( 0 ) { > } w ( 0 )$ and there exists a quantity $q { > } 0$ such that $p ( q ) { = } c .$ . Notice that the latter condition makes sense from an economic point of view since $\mathrm { i f } p ( q ) > c$ for all $q$ then the parties in the chain can obtain arbitrary large profits.

A retailer–supplier problem (henceforth: RS-problem) is denoted by the tuple $( c , \ w , p )$ . Given such a problem let $\mathbb { Q } = \left\{ q \in \mathbb { R } _ { + } | p ( q ) { \ge } w ( q ) \right\}$ be the set of <sup>¼ f þj ð Þ ð Þg</sup>feasible order sizes, that is, those order sizes that result in a nonnegative profit margin for the retailer. Notice that $\mathbb { Q } \neq \emptyset$ because $p ( 0 ) { > } w ( 0 )$

The retailer determines his order quantity $q$ such that his (expected) profit is maximized:

$$
\begin{array}{l l} \max & \Pi^ {r e t} (q; w (q)) = (p (q) - w (q)) q \\ \text { s.t. } & q \in \mathbb {Q}. \end{array}
$$

This optimization problem always has an optimal solution/ order size $q$ since $\mathbb { Q }$ is a compact set and $\Pi ^ { \mathrm { r e t } } \left( q ; w \left( q \right) \right)$ is continuous on $\mathbb { Q } .$ Given the retailer's order size $q ,$ , the supplier's profit equals

$$
\Pi^ {\sup} (q; w (q)) = (w (q) - c) q.
$$

The two $\mathrm { e x a m p l e s } ^ { 1 }$ below show that the retailer may have one or more optimal order sizes.

Example 3.1. Let $( c , ~ w , ~ p )$ be an RS-problem with $c { = } 2 , p ( q ) { = } 7 { - } q$ and

$$
w (q) = \left\{ \begin{array}{l l} 5, & 0 \leq q \leq 1, \\ 2 + 3 / q, & q > 1. \end{array} \right.
$$

The retailer solves

$$
\begin{array}{l l} \max & \Pi^ {\text { ret }} (q; w (q)) \\ \text { s.t. } & q \in \mathbb {Q} = \left[ 0, \frac {5 + \sqrt {1 3}}{2} \right] \end{array}
$$

where

$$
\Pi^ {\mathrm{ret}} (q; w (q)) = \left\{ \begin{array}{l l} 2 q - q ^ {2}, & 0 \leq q \leq 1, \\ - q ^ {2} + 5 q - 3, & q > 1. \end{array} \right.
$$

The unique optimal order size is $\boldsymbol { q } ^ { * } = 2 \frac { 1 } { \tau ^ { * } } ,$ , leading to a profit of $\hat { \Pi } ^ { \mathrm { \tiny { r e t } } } ( q ^ { * } ; w ( q ^ { * } ) ) = 3 \frac { 1 } { \cal A }$ <sup>¼</sup>for the retailer and $\Pi ^ { \mathrm { s u p } } ( q ^ { * } ; \ w \ ( q ^ { * } ) ) { = } 3$ <sup>ð ÞÞ ¼</sup> for the supplier.

Example 3.2. Let $( c , w , p )$ be an RS-problem with $c = 1$ 4

$$
p (q) = \left\{ \begin{array}{l l} 5, & 0 \leq q \leq 1, \\ 6 - q, & 1 <   q \leq 2, \\ 5 - \frac {q}{2}, & q > 2, \end{array} \right.
$$

and

$$
w (q) = \left\{ \begin{array}{l l} 4, & 0 \leq q \leq 1, \\ 3 + \frac {1}{q}, & 1 <   q \leq 2, \\ 2 \frac {1}{4} + \frac {5}{2 q}, & 2 <   q \leq 2 \frac {1}{2}, \\ 3 \frac {1}{4}, & q > 2 \frac {1}{2}. \end{array} \right.
$$

Now the retailer solves

max $\Pi ^ { \mathrm { r e t } } ( q ; w ( q ) )$

s:t: $q \in \mathbb { Q } = \left[ 0 , 3 \frac { 1 } { 2 } \right]$

where

$$
\Pi^ {\text { ret }} (q; w (q)) = \left\{ \begin{array}{l l} q, & 0 \leq q \leq 1, \\ - q ^ {2} + 3 q - 1, & 1 <   q \leq 2, \\ - \frac {1}{2} q ^ {2} + 2 \frac {3}{4} q - 2 \frac {1}{2}, & 2 <   q \leq 2 \frac {1}{2}, \\ - \frac {1}{2} q ^ {2} + 1 \frac {3}{4} q, & q > 2 \frac {1}{2}. \end{array} \right.
$$

This leads to two optimal order sizes, namely $q _ { a } ^ { * } = 1 \frac { 1 } { 2 }$ and $q _ { b } ^ { * } = 2 _ { \tau } ^ { 1 }$ . In either case the optimal benefit <sup>¼</sup> for the retailer is $1 { \frac { 1 } { x } } .$ . The profit for the supplier is either $\Pi ^ { \mathrm { s u p } } ( q _ { a } ^ { * } ; w ( q _ { a } ^ { * } ) ) { = } ^ { 4 }$ or $\begin{array} { r } { \hat { \Pi } ^ { \mathrm { s u p } } ( q _ { b } ^ { * } ; w ( q _ { b } ^ { * } ) ) = 5 _ { \mathrm { s } } ^ { 5 } . } \end{array}$ The read-<sup>ð ð ÞÞ ¼ ð ð ÞÞ¼</sup>er may notice that the supplier prefers q<sup>⁎</sup> over $\stackrel { \cup } { q _ { a } ^ { * } }$ because it results in larger profits. However, he has no means to induce it. The only way the supplier would be able to influence the retailer's decision is by changing the wholesale price $w ( q )$ , but that is outside the scope of this paper.

## 4. Retailers–supplier games

In this section we address a natural extension of the RS-problem, namely, we consider single period models of distribution chains with a supplier, a warehouse and multiple retailers. Each of the retailers places its order at the warehouse, who passes the order sizes to the supplier. The retailers have the possibility to cooperate among each other and place a joint order, which results in a lower wholesale price per unit. The supplier will not know about the cooperation since he only receives the order sizes and does not know which order size belongs to which retailer(s). Hence the presence of the warehouse allows the retailers to save money by cooperation. Furthermore, a group of retailers may cooperate with the supplier via the warehouse. In this case, the warehouse provides all parties with the necessary information to achieve cooperation. After delivery of the goods from the supplier via the warehouse to the retailers, each retailer sells its goods on its local consumer market. These markets are independent from one another, implying that the retailers do not compete for customers.

Let $N { = \{ 1 , . . . , n \} }$ be the set of retailers and denote the supplier by 0. Then $N _ { 0 } { = } N \cup \left\{ 0 \right\}$ is the set of all com-<sup>[</sup>panies in the chain. Similarly, we define $S _ { 0 } { = } S \cup \{ 0 \}$ for all $S \subseteq N . \mathrm { A }$ retailers–supplier situation (RS-situation) is a tuple $( N _ { 0 } , c , w , P )$ with $P { = } ( p _ { 1 } , . . . , p _ { n } ) , p _ { i }$ is the expected price function of retailer $i ,$ and the tuple $( c , w , p _ { i } )$ is an RS-problem for any retailer i.

In such an RS-situation two types of cooperation among the companies may occur, namely cooperation excluding or including the supplier. First, cooperation among retailers is profitable since the firms may place one large joint order for the good and thus enjoy a quantity discount provided by the supplier. If $q _ { S } =$ $\bar { \sum _ { i \in S } q _ { i } }$ denotes the total order size by a coalition $S \subseteq N$ of retailers then the joint benefit of this coalition equals

$$
\begin{array}{l l} \max & \sum_ {i \in S} (p _ {i} (q _ {i}) - w (q _ {s})) q _ {i} \\ \text { s.t. } & q \in \mathbb {Q} ^ {S} := \{q \in \mathbb {R} _ {+} ^ {s} | p _ {i} (q _ {i}) \geq w (q _ {S}) \text {   for   all   } i \in S \}. \end{array}
$$

The reader may notice that $\mathbb { Q } ^ { S }$ is a nonempty set since $( q _ { i } ^ { \{ i \} } ) _ { i \in S } \in \mathbb { Q } ^ { S }$ , where $q ^ { \{ i \} }$ is an optimal solution for retail-<sup>ð</sup>er $i \mathbf { \ ' } _ { \mathbf { S } }$ RS-problem $( c , w , p _ { i } )$ . Besides, $\mathbb { Q } ^ { S } \subset \Pi _ { i \in S } [ 0 , q _ { i } ^ { * } ]$ 9 where the order size $q _ { i } ^ { * }$ satisfies $p _ { i } ( q _ { i } ^ { * } ) { = } c ,$ , and $\mathbb { Q } ^ { S }$ <sup>-</sup>is closed. Hence, there exists an optimal solution for this optimization problem. Let $q _ { i } ^ { S }$ denote the optimal order size for retailer i when cooperating in coalition S.

A second type of cooperation is cooperation among a group of retailers $S$ and the supplier. The joint benefit of this coalition $S _ { 0 }$ is

$$
\begin{array}{l} \sum_ {i \in S} \Pi_ {i} ^ {r e t} (q _ {i}; w (q _ {S})) + \sum_ {i \in S} \Pi_ {i} ^ {\sup} (q _ {i}; w (q _ {S})) \\ = \sum_ {i \in S} (p _ {i} (q _ {i}) - c) q _ {i}, \end{array}
$$

which shows a reduction in cost inefficiency for the companies due to the absence of the intermediate wholesale prices. Under cooperation this coalition optimizes

$$
\begin{array}{l l} \max & \sum_ {i \in S} (p _ {i} (q _ {i}) - c) q _ {i} \\ \text { s.t. } & q \in \mathbb {Q} _ {c} ^ {S} := \{q \in \mathbb {R} _ {+} ^ {s} | p _ {i} (q _ {i}) \geq c \text {   for   all   } i \in S \}, \end{array}
$$

which is equivalent to

$$
\text { for   all } i \in S: \begin{array}{l l} \max & (p _ {i} (q _ {i}) - c) q _ {i} \\ \text { s.t. } & p _ {i} (q _ {i}) \geq c \end{array}\tag{1}
$$

Similar arguments as above assure the existence of optimal solutions for these optimization problems. Let $q _ { i } ^ { c }$ denote the optimal order size for retailer i in this situation. Notice that this quantity does not depend on S or $S _ { 0 } ,$ since the optimization problem (1) for i only depends on individual parameters. Also, in general $\stackrel { \cdot } { q _ { i } ^ { c } } \neq \stackrel { \cdot } { q _ { i } ^ { S } }$ for all coalitions S with $i \in S$

The profit functions arising from cooperation have nice properties, as stated in the lemma below.

Lemma 4.1. Let $( N _ { O } , c , w , P )$ be an RS-situation, and $i \in S \subseteq N$ then

(P1) $\Pi _ { i } ^ { r e t } ( q _ { i } ^ { S } ; \ c ) = \Pi _ { i } ^ { r e t } ~ ( q _ { i } ^ { S } ; \ w ( q _ { S } ^ { S } ) ) + \Pi _ { i } ^ { s u p } ~ ( q _ { i } ^ { S } ; \ w ( q _ { S } ^ { S } ) ) ;$ (P2) $\Pi _ { i } ^ { r e t } ( q _ { i } ^ { c } ; c ) \geq I I _ { i } ^ { r e t } ( q _ { i } ^ { S } ; c ) ;$ (P3) $\begin{array} { l } { { \Pi _ { i } ^ { r e t } ( q _ { i } ^ { c } ; c ) > \cal { I } _ { i } ^ { r e t } ( q _ { i } ^ { S } ; w ( q _ { S } ^ { S } ) ) } } \\ { { \pi _ { i } ^ { s u p } ( q _ { i } ^ { S } ; w ( q _ { S } ^ { S } ) ) . } } \end{array}$ and $H _ { i } ^ { r e t } ~ ( q _ { i } ^ { c } ; c ) ^ { > }$

Proof. (P1) follows immediately from the definitions of $\Pi _ { i } ^ { \mathrm { r e t } }$ and $\overline { { \Pi _ { i } ^ { \mathrm { s u p } } } }$ . (P2) follows from $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; c ) { = } \operatorname* { m a x } _ { q _ { i } } ( p _ { i } ( q _ { i } ) -$ $c ) \ : q _ { i } \ge p _ { i } ( q _ { i } ^ { S } ) - c ) \ : q _ { i } ^ { S } \qquad $ . Finally, (P3) follows from (P1), (P2), $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { S } ; w ( q _ { S } ^ { S } ) ) { > } 0$ and $\Pi _ { i } ^ { \mathrm { s u p } } ( q _ { i } ^ { S } ; w ( q _ { S } ^ { S } ) ) { > } 0$ □

Next we define the cooperative game corresponding to an RS-situation. Its characteristic function is based on the maximum profit that each coalition can reach.

Definition 4.2. Let $( N _ { 0 } , c , w , P )$ be an RS-situation. The corresponding RS-game $( N _ { 0 } , \nu )$ is defined by

$$
v (S) = \sum_ {i \in S} \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S}))
$$

and

$$
v (S _ {0}) = \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; c)
$$

for all coalitions $S \subseteq N ,$ , and $\nu ( \emptyset ) { = } 0$

The definition of RS-situations and their corresponding games focuses on retailer revenues arising from selling goods to consumers. As a consequence one may interpret the game value $\nu ( T )$ of a coalition $T$ as being ‘zero-normalised’ with respect to the supplier. This explains why $\nu ( \{ 0 \} ) { = } 0$

The definition above shows that a coalition of retailers benefits from a lower wholesale price per unit while a coalition including the supplier increases its profit due to the absence of the intermediate wholesale prices. This provides the companies in the chain with sufficient incentives for cooperation. Also, cooperation with the supplier is attractive for retailers since $\nu ( S _ { 0 } ) { > } \nu ( S )$ by property (P3). The reader may notice that the supplier does not contribute with a fixed quantity of gain but rather he reduces the cost inefficiency by suppressing the intermediate wholesale prices. To be more precise, if the supplier joins a coalition S of retailers then this leads to an increase of

$$
v (S _ {0}) - v (S) = \sum_ {i \in S} (p _ {i} (q _ {i} ^ {c}) - c) q _ {i} ^ {c} - \sum_ {i \in S} (p _ {i} (q _ {i} ^ {S}) - w (q _ {S} ^ {S})) q _ {i} ^ {S}.
$$

Besides the optimal quantity for each retailer does depend upon the presence of the supplier in the coalition. Namely, if the supplier is present then the optimal quantity for referee i is $q _ { i } ^ { c }$ and if the supplier is not present then it is $q _ { i } ^ { S } .$ . See for instance Example $5 . 7$ in which $\stackrel { S } { q _ { i } ^ { s } } = 4 9$ (the supplier is not present) and $q _ { i } ^ { c } = 4 8 \frac { 1 } { 5 }$ (the supplier is present) for $i { = } 1 , 2$ and $S { \subseteq } N .$ Hence, the difference among $\nu ( S _ { 0 } )$ and v(S) does not just depend upon the gain of the supplier. The increase is also due to the retailers: cooperation increases the gain of the retailers since for all $i \in S$

$$
(p _ {i} (q _ {i} ^ {c}) - c) q _ {i} ^ {c} > (p _ {i} (q _ {i} ^ {S}) - w (q _ {S} ^ {S})) q _ {i} ^ {S}.
$$

Therefore, the supplier has reasons to share the gain from cooperation with the retailers. The example below shows an RS-situation and its corresponding RS-game.

Example 4.3. Let $( N _ { 0 } , c , w , P )$ be an RS-situation with $N _ { 0 } = \{ 0 , 1 , 2 \} , c = 2 , p _ { 1 } ( q ) = 7 - q , p _ { 2 } ( q ) = 8 - q$ and

$$
w (q) = \left\{ \begin{array}{l l} 5, & \frac {1}{4} \leq q \leq 1, \\ 2 + 3 / q, & q > 1. \end{array} \right.
$$

The optimal order sizes are $q _ { 1 } ^ { S } = q _ { 1 } ^ { c } = 2 { \frac { 1 } { \gamma } }$ and $q _ { 2 } ^ { S } =$ $q _ { 2 } ^ { c } = 3$ for all $S \subseteq N$ <sup>¼ ¼</sup> <sup>¼</sup>. This implies the RS-game as <sup>¼</sup>given in the table below.

<table><tr><td>T</td><td>{0}</td><td>{1}</td><td>{2}</td><td>{0, 1}</td><td>{0, 2}</td><td>{1, 2}</td><td>{0, 1, 2}</td></tr><tr><td>v(T)</td><td>0</td><td> $3\frac{1}{4}$ </td><td>6</td><td> $6\frac{1}{4}$ </td><td>9</td><td> $12\frac{1}{4}$ </td><td> $15\frac{1}{4}$ </td></tr></table>

This game has positive values for coalitions $T \neq \{ 0 \}$ is superadditive and monotone increasing. In addition, $\nu ( N _ { 0 } ) { = } \nu ( \{ 0 , 1 \} ) { + } \nu ( \{ 0 , 2 \} )$ .

The properties that are observed in this example hold in general, as the next lemma shows.

Lemma 4.4. Let $( N _ { O } ,$ v) be an RS-game. Then

(i) $\nu ( T ) > 0$ for all coalitions $T \neq \{ 0 \}$

(ii) v is superadditive;

(iii) v is strict monotone increasing;

(iv) $\textstyle \nu ( S _ { 0 } ) = \sum _ { i \in S } \nu ( \{ 0 , i \} )$ and $\nu ( S _ { 0 } ) – \nu ( S _ { 0 } \setminus \{ i \} ) =$ $\nu ( \{ 0 , 1 \} )$ <sup>ð Þ ¼</sup>for all $S \subseteq N$ <sup>g</sup>and $i \in S$

Proof. (i) The definition of the game $( N _ { 0 } , \nu )$ and the positive profit margins for the retailers $( p _ { i } ( q ) { > } w ( q ) )$ imply that $\nu ( T ) { > } 0$ for any coalition $T \neq \{ 0 \}$

(ii) Let $S , T \subseteq N$ be two disjoint coalitions of retailers. By definition of the RS-game

$$
\begin{array}{l} v (S) + v (T) = \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) \\ \quad + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {T}; w (q _ {T} ^ {T})). \end{array}
$$

Define the specific order quantity $\hat { q } _ { i }$ for retailer i in coalition S⋃T by $\hat { q } _ { i } { = } q _ { i } ^ { S }$ if $i \in S$ and $\quad { \hat { q } } _ { i } = q _ { i } ^ { T } \operatorname { i f } i \in T .$ Now

$$
\begin{array}{l} \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {T}; w (q _ {T} ^ {T})) \\ \leq \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (\hat {q} _ {i}; w (\hat {q} _ {S \cup T})) + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (\hat {q} _ {i}; w (\hat {q} _ {S \cup T})) \end{array}
$$

because this larger coalition enjoys a lower wholesale price than before: $w ( \hat { q } _ { S } \cup _ { T } ) = w ( q _ { S } ^ { S } + q _ { T } ^ { T } ) \leq \operatorname* { m i n } \left\{ w ( q _ { S } ^ { S } ) \right.$ 4 $\bar { \ l } _ { w } ( q _ { T } ^ { T } ) \}$ . Finally,

$$
\begin{array}{l} \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (\hat {q} _ {i}; w (\hat {q} _ {S \cup T})) + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (\hat {q} _ {i}; w (\hat {q} _ {S \cup T})) \\ = \sum_ {i \in S \cup T} \Pi_ {i} ^ {\text {ret}} (\hat {q} _ {i}; w (\hat {q} _ {S \cup T})) \leq \sum_ {i \in S \cup T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {S \cup T}; w (q _ {S \cup T} ^ {S \cup T})) \\ = v (S \cup T), \end{array}
$$

since the quantities $\hat { q } _ { i }$ need not be optimal for coalition $S \cup T .$

<sup>[</sup>Furthermore,

$$
\begin{array}{l} v (S _ {0}) + v (T) = \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {T}; w (q _ {T} ^ {T})) \\ <   \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) + \sum_ {i \in T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) \\ = \sum_ {i \in S \cup T} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) = v (S _ {0} \cup T), \end{array}
$$

where the second inequality is due to property (P3).

(iii) This follows immediately from (i), (ii) and (P3).

(iv) These results follow directly from the definition of the game. □

The fourth property in this lemma shows that each optimal profit of a large coalition including the supplier is composed of optimal profits for pairs of the supplier and a retailer. This is due to the fact that the retailers do not compete for customers but rather serve their own market.

## 5. The core of RS-games

The core is an important set-solution for cooperative games. In this section we show that every RS-game is balanced, that is, its core is nonempty. But first we present the core structure for RS-games.

Theorem 5.1. Let $( N _ { 0 } , c , w , P )$ be an RS-situation and $( N _ { O } ,$ v) the corresponding RS-game. The core of this game equals

$$
\begin{array}{l} \text {Core} (N _ {0}, v) \\ = \left\{x \in \mathbb {R} ^ {n _ {0}} \middle | \frac {\sum_ {i \in N _ {0}} x _ {i} = v (N _ {0}) ; x _ {i} \leq v (\{0 , i \}) , i \in N ;}{\sum_ {i \in S} x _ {i} \geq v (S) , S \subseteq N} \right\}. \end{array}
$$

Proof. Let $i \in N$ and $x { \in } \mathrm { C o r e } ( N _ { 0 } , \nu )$ . The core conditions $\begin{array} { r } { \sum _ { i \in N _ { 0 } } x _ { i } = \nu ( N _ { 0 } ) } \end{array}$ and $\begin{array} { r } { \sum _ { j \in N _ { 0 } \setminus \{ i \} } x _ { j } \ge \nu ( N _ { 0 } \setminus \{ i \} ) } \end{array}$ imply $x _ { i } \le \overset { \sim } { \nu } ( N _ { 0 } ) { - } \nu ( N _ { 0 } \setminus \{ i \} )$ <sup>f g</sup>, which leads to

$$
\begin{array}{l} x _ {i} \leq v (N _ {0}) - v (N _ {0} \setminus \{i \}) = v (N _ {0}) - (v (N _ {0}) - v (\{0, i \})) \\ = v (\{0, i \}), \end{array}
$$

in which the first equality follows from property (iv) in lemma 4.4.

We proceed by showing that the core conditions $\begin{array} { r } { x _ { 0 } + \sum _ { i \in S } x _ { i } { \ge } \nu ( S _ { 0 } ) , S \subseteq N _ {  } } \end{array}$ , are superfluous. We obtain subsequently

$$
\begin{array}{l} x _ {0} + \sum_ {i \in S} x _ {i} = \sum_ {i \in N _ {0}} x _ {i} - \sum_ {j \in N \setminus S} x _ {j} \geq v (N _ {0}) - \sum_ {j \in N \setminus S} v (\{0, j \}) \\ = \sum_ {j \in S} v (\{0, j \}) = v (S _ {0}), \end{array}
$$

by using respectively $\textstyle \sum _ { i \in N _ { 0 } } x _ { i } = \nu ( N _ { 0 } ) , x _ { j } \leq \nu ( \{ 0 , j \} )$ and property (iv) in lemma 4.4. gÞ<sub>□</sub>

This theorem says that the stability conditions for coalitions including the supplier $\begin{array} { r } { ( \mathrm { i . e . } \sum _ { i \in S _ { 0 } } x _ { i } \mathrm { \sum } \nu ( S _ { 0 } ) ) } \end{array}$ can be replaced by the conditions $x _ { i } \le \nu ( \{ 0 , i \} )$ <sup>ð Þ</sup>for all retailers i. This allows for an easier expression of the core of RS-games.

Using the above theorem, the core of Example 4.3 can be expressed as

$$
\operatorname{Core} (N _ {0, \nu}) = \left\{(x _ {0}, x _ {1}, x _ {2}) \left| \begin{array}{l} 3 \frac {1}{4} \leq x _ {1} \leq 6 \frac {1}{4}, 6 \leq x _ {2} \leq 9, \\ x _ {1} + x _ {2} \geq 1 2 \frac {1}{4}, x _ {0} + x _ {1} + x _ {2} = 1 5 \frac {1}{4} \end{array} \right. \right\}.
$$

One immediately sees that this core is nonempty since $( 0 , 6 { \frac { 1 } { 4 } } , 9 ) { \in } \thinspace \mathrm { C o r e } ( N _ { 0 } , \nu )$ . Nonemptiness of the <sup>ð Þ</sup>core of RS-games in general is shown in the theorem below.

Theorem 5.2. Let $( N _ { O } , c , w , P )$ be an RS-situation and $( N _ { O } , \nu )$ the corresponding RS-game. Then $( N _ { O } , \nu )$ is balanced.

Proof. Define the allocation $x ^ { a } ( \nu )$ by $x _ { 0 } ^ { a } ( \nu ) { = } 0$ and $x _ { i } ^ { a } ( \nu ) =$ $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; \ c ) = \nu ( \{ 0 , \ i \} ) , \ i \in N .$ . In this allocation the retailer receives all the benefit from cooperation with the supplier, while the supplier receives nothing. First notice that

$$
\sum_ {i \in N _ {0}} x _ {i} ^ {a} (v) = \sum_ {i \in N} \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; c) = v (N _ {0}).
$$

Hence, $x ^ { a } ( \nu )$ is an efficient allocation. Next, consider a coalition $S \subseteq N .$ Then

$$
\begin{array}{l} \sum_ {i \in S} x _ {i} ^ {a} (v) = \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) > \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) \\ = v (S), \end{array}
$$

where the inequality follows from property (P3). Finally, by definition $x _ { i } ^ { a } ( \nu ) \leq \nu ( \{ 0 , i \} )$ . We conclude that $x ^ { a } ( \nu ) { \in } \mathrm { C o r e } ( N _ { 0 } , \nu )$ , thus, the game is balanced. □

The proof of this theorem shows that the allocation ${ x ^ { a } } ( \nu ) { = } ( 0 , \nu ( \{ 0 , i \} ) _ { i \in N } )$ always belongs to the core of an RSgame. This allocation will be called the altruistic allocation since it is the worst possible core-allocation for the supplier, namely the only one in which he receives nothing.

As a corollary of this theorem we obtain balancedness of subgames including the supplier in the player set.

Corollary 5.3. Let $( N _ { 0 } , c , w ,$ P) be an RS-situation and S a coalition of retailers. Let $P _ { S }$ denote the restriction of the vector of consumer price functions P to coalition S. Then the game $( S _ { O } , \nu _ { S _ { O } } )$ corresponding to the RSsituation $( S _ { 0 } , c , w , P _ { S } )$ is balanced.

This corollary and its preceding theorem show that cooperation is profitable for all companies in the distribution chain because (a) it results in higher profits, and (b) there exists a core-allocation of the joint optimal profit, that is, an allocation upon which no coalition can improve.

The core of RS-games has a nice alternative interpretation in terms of the underlying distribution chain, as we will see shortly. For this, we need the following lemma and its corollary.

Lemma 5.4. Let $( N _ { 0 } , c , w , P )$ be an RS-situation. Then there exist prices $w _ { i } ^ { \ast } \in / c , p _ { i } ( q _ { i } ^ { c } ) \jmath , i \in N ,$ such that

$$
\Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}) \geq \max _ {S \subseteq N: i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {S}; w (q _ {S} ^ {S})).
$$

Proof. Consider a coalition S of retailers and let $i \in S$ be one of them. Then by property (P3)

$$
\Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; c) > \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) > 0.
$$

This implies that there exists a number $\beta ^ { S } , 0 { < } \beta ^ { S } { < }$ $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; c )$ , such that $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { S } ; ~ w ( q _ { S } ^ { S } ) ) { = } \Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; c ) { \ - } ^ { + } \beta ^ { S }$ Furthermore, there is a wholesale price $w _ { i } ^ { S } { \in } [ c , p _ { i } ( q _ { i } ^ { c } ) ]$ such that $\Pi _ { i } ^ { \mathrm { s u p } } ( q _ { i } ^ { c } ; w _ { i } ^ { S } ) { = } ( w _ { i } ^ { S } { - } c ) q _ { i } ^ { c } { \le } \beta ^ { S } ,$ . Thus

$$
\begin{array}{l} \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) = \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; c) - \beta^ {S} \\ \leq \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; c) - \Pi_ {i} ^ {\sup} (q _ {i} ^ {c}; w _ {i} ^ {S}) \\ = \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; w _ {i} ^ {S}), \end{array}
$$

where property (P1) is used in the last equality. Let ${ \scriptstyle w _ { i } ^ { * } = \operatorname* { m i n } _ { { \cal S } \ni i } w _ { i } ^ { { \cal S } } }$ be the lowest wholesale price for retailer i. Then

$$
\Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; w _ {i} ^ {*}) \geq \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {c}; w _ {i} ^ {S}) \geq \Pi_ {i} ^ {\mathrm{ret}} (q _ {i} ^ {S}; w (q _ {S} ^ {S}))
$$

for all $S \subseteq N$ with $i \in S ,$ which concludes the proof. □

Notice that this lemma generates upper bounds lower than $p _ { i } ( q _ { i } ^ { c } )$ for the values w<sup>⁎</sup>. Lower bounds for $w _ { i } ^ { * }$ are given by c. As a corollary we obtain the following weaker result.

Corollary 5.5. Let $( N _ { 0 } , \ c , \ w , \ P )$ be an RS-situation. Then there exist prices $w _ { i } ^ { * } \geq c , i \in N ,$ such that

$$
\sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}) \geq \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) = v (S),
$$

or equivalently,

$$
\sum_ {i \in S} q _ {i} ^ {c} w _ {i} ^ {*} \leq \sum_ {i \in S} p _ {i} (q _ {i} ^ {c}) q _ {i} ^ {c} - v (S),
$$

for all coalitions S of retailers.

Using this corollary we provide an alternative formulation of the core of an RS-game.

Theorem 5.6. Let $( N _ { O } , c ,$ w, P) be an RS-situation and $( N _ { O } ,$ v) the corresponding RS-game. Then $x \in C o r e ( N _ { O } ,$ v) if and only if

$$
x _ {0} = \sum_ {i \in N} \Pi_ {i} ^ {\sup} (q _ {i} ^ {c}; w _ {i} ^ {*}) a n d x _ {i} = \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}), i \in N,
$$

for some $w ^ { * } { \in } \mathbb { R } ^ { n }$ that satisfies corollary 5.5.

Proof. First, according to theorem $5 . 2 \ \mathrm { C o r e } ( N _ { 0 } , \nu ) { \neq } 0$ All elements $x { \in } \mathrm { C o r e } ( N _ { 0 } , \nu )$ satisfy

$$
v (\{i \}) \leq x _ {i} \leq v (N _ {0}) - v (N _ {0} \setminus \{i \})
$$

for all $i \in N _ { 0 }$ . Using the definition of the RS-game this condition is equivalent to

$$
x _ {i} ^ {L} = \Pi_ {i} ^ {\text { ret }} \left(q _ {i} ^ {i}; w (q _ {i} ^ {\{i \}})\right) \leq x _ {i} \leq \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; c) = x _ {i} ^ {H}
$$

for all retailers $i \in N .$ Now, let $x ^ { * } { = } ( x _ { 0 } ^ { * } , ~ x _ { 1 } ^ { * } , ~ . . . , ~ x _ { n } ^ { * } ) \in$ $\mathrm { C o r e } ( N _ { 0 } , \nu )$ . Notice that $\Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; p _ { i } ( q _ { i } ^ { c } ) ) { = } 0$ and so x<sup>⁎</sup>; x<sup>⁎L</sup>; yx<sup>⁎H</sup> o C<sup>ret</sup> q<sup>c</sup>; p<sub>i</sub> q<sup>c</sup> ; C<sup>ret</sup> q<sup>c</sup>; c

for all $i \in N .$ . Because of this, there exists $w _ { i } ^ { * } { \in } [ c , p _ { i } ( q _ { i } ^ { c } ) ]$ such that ${ x _ { i } ^ { * } } { = } \Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; ~ w _ { i } ^ { * } )$ . The efficiency of coreelements implies $\begin{array} { r } { x _ { 0 } ^ { * } = \sum _ { i \in N } \Pi _ { i } ^ { \operatorname { s u p } } ( q _ { i } ^ { c } ; w _ { i } ^ { * } ) } \end{array}$ . For any coalition $S \subseteq N$ of retailers

$$
v (S) \leq \sum_ {i \in S} x _ {i} ^ {*} \Leftrightarrow \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) \leq \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}).
$$

Hence, the $w _ { i } ^ { * }$ satisfy corollary 5.5. This concludes the first part of the proof.

Second, let $w ^ { * } \in \mathbb { R } ^ { n }$ satisfy corollary 5.5. Define the allocation $x ^ { * }$ by

$$
x _ {i} ^ {*} = \left\{ \begin{array}{l l} \sum_ {j \in N} \Pi_ {j} ^ {\sup} (q _ {j} ^ {c}; w _ {j} ^ {*}), & i = 0, \\ \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}), & i \in N. \end{array} \right.
$$

Notice first that

$$
\sum_ {i \in N _ {0}} x _ {i} ^ {*} = \sum_ {i \in N} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}) + \sum_ {j \in N} \Pi_ {j} ^ {\sup} (q _ {j} ^ {c}; w _ {j} ^ {*}) = v (N _ {0})
$$

where the last equality is due to property (P1). Hence, $x ^ { * }$ is an efficient allocation. Next, consider a coalition $S \subseteq N .$ . Then

$$
\sum_ {i \in S} x _ {i} ^ {*} = \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {c}; w _ {i} ^ {*}) \geq \sum_ {i \in S} \Pi_ {i} ^ {\text { ret }} (q _ {i} ^ {S}; w (q _ {S} ^ {S})) = v (S),
$$

where the inequality follows from corollary 5.5. Further,

$$
\begin{array}{l} \sum_ {i \in S _ {0}} x _ {i} ^ {*} = \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; w _ {i} ^ {*}) + \sum_ {i \in N} \Pi_ {i} ^ {\sup} (q _ {i} ^ {c}; w _ {i} ^ {*}) \\ = \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) + \sum_ {i \in N \setminus S} \Pi_ {i} ^ {\sup} (q _ {i} ^ {c}; w _ {i} ^ {*}) \\ \geq \sum_ {i \in S} \Pi_ {i} ^ {\text {ret}} (q _ {i} ^ {c}; c) = v (S _ {0}), \end{array}
$$

where the second equality is due to property (P1). We conclude that $x ^ { * } \in \mathbf { C } \mathrm { o r e } ( N _ { 0 } , \nu )$ □

This theorem shows that for each core-allocation x there exist fixed wholesale prices $w ^ { * }$ such that the retailer's share $x _ { i }$ corresponds to its optimal profit under cooperation with the supplier given the wholesale price $w _ { i } ^ { * } , \bar { x } _ { i } { = } \Pi _ { i } ^ { \mathrm { r e t } } ( q _ { i } ^ { c } ; ~ w _ { i } ^ { * } )$ , and the supplier's share equals $\begin{array} { r } { x _ { 0 } = \sum _ { i \in N } \Pi _ { i } ^ { \mathrm { s u p } } ( q _ { i } ^ { c } ; w _ { i } ^ { * } ) } \end{array}$ . Hence, each core-allocation <sup>¼ ð Þ</sup>has a natural interpretation in terms of the underlying distribution chain.

Further, this theorem shows that the structure of the core is determined by the values $w _ { i } ^ { * }$ . Corollary 5.5 generates for each coalition S of retailers an upper bound for $\{ w _ { i } ^ { * } \} _ { i \in S } ,$ which is related to the corecondition of this coalition. The lower bound $w _ { i } ^ { * } { = } c$ corresponds to the upper bound $\nu ( \{ 0 , i \} )$ for $x _ { i } .$ . This corresponds with the formulation of the core in theorem 5.1. The example below illustrates these observations.

Example 5.7. Let $( N _ { 0 } , c , w , P )$ be the RS-situation with $\begin{array} { r } { N _ { 0 } = \{ 0 , 1 , 2 \} , c = 1 \frac { 4 } { 5 } , p _ { 1 } ( q ) = p _ { 2 } ( q ) = 5 0 - \frac { q } { 2 } , } \end{array}$ , and

$$
w (q) = \left\{ \begin{array}{l l} 1 1, & 0 \leq q \leq 1 0, \\ 1 + \frac {1 0 0}{q}, & 1 0 <   q \leq 1 0 0, \\ 2, & q > 1 0 0. \end{array} \right.
$$

The optimal order sizes are $q _ { i } ^ { S } { = } 4 9$ and $q _ { i } ^ { c } = 4 8 \frac { 1 } { 5 }$ for $i = 1 , 2$ and $S \subseteq N .$ . The coalitional values in the corresponding game are

<table><tr><td>T</td><td>{0}</td><td>{1}</td><td>{2}</td><td>{0, 1}</td><td>{0, 2}</td><td>{1, 2}</td><td>{0, 1, 2}</td></tr><tr><td>v(T)</td><td>0</td><td> $1100 \frac{1}{2}$ </td><td> $1100 \frac{1}{2}$ </td><td> $1161 \frac{31}{50}$ </td><td> $1161 \frac{31}{50}$ </td><td>2301</td><td> $2323 \frac{6}{25}$ </td></tr></table>

The core of this game equals

$$
\begin{array}{l} \operatorname{Core} (N _ {0}, v) = \left\{\left(x _ {0}, x _ {1}, x _ {2}\right) \left| \begin{array}{l l} 1 1 0 0 \frac {1}{2} \leq x _ {i} \leq 1 1 6 1 \frac {3 1}{5 0}, & i = 1, 2; \\ x _ {1} + x _ {2} \geq 2 3 0 1; x _ {0} + x _ {1} + x _ {2} = 2 3 2 3 \frac {6}{2 5} \end{array} \right. \right\} \\ = \left\{\left( \begin{array}{l} 4 8 \frac {1}{5} (w _ {1} ^ {*} + w _ {2} ^ {*}) - 1 7 3 \frac {1 3}{2 5}, \\ 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} w _ {1} ^ {*}, \\ 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} w _ {2} ^ {*} \end{array} \right) \left| \begin{array}{l l} 1 \frac {4}{5} \leq w _ {i} ^ {*} \leq 3 \frac {8 2}{1 2 0 5}, & i = 1, 2; \\ w _ {1} ^ {*} + w _ {2} ^ {*} \leq 4 \frac {7 4}{1 2 0 5}. \end{array} \right. \right\}. \end{array}
$$

The correspondence between the two formulations is clear:

$$
1 \frac {4}{5} \leq w _ {i} ^ {*} \Leftrightarrow x _ {i} \leq 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} \cdot 1 \frac {4}{5} = 1 1 6 1 \frac {3 1}{5 0}
$$

and

$$
w _ {i} ^ {*} \leq 3 \frac {8 2}{1 2 0 5} \Leftrightarrow x _ {i} \geq 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} \cdot 3 \frac {8 2}{1 2 0 5} = 1 1 0 0 \frac {1}{2}
$$

for i = 1, 2. Also,

$$
w _ {1} ^ {*} + w _ {2} ^ {*} \leq 4 \frac {7 4}{1 2 0 5} \Leftrightarrow x _ {1} + x _ {2} \geq 2 4 9 6 \frac {1 9}{2 5} - 4 8 \frac {1}{5} \cdot 4 \frac {7 4}{1 2 0 5} = 2 3 0 1.
$$

Finally, the equality

$$
\begin{array}{l} 4 8 \frac {1}{5} (w _ {1} ^ {*} + w _ {2} ^ {*}) - 1 7 3 \frac {1 3}{2 5} + 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} w _ {1} ^ {*} \\ + 1 2 4 8 \frac {1 9}{5 0} - 4 8 \frac {1}{5} w _ {2} ^ {*} = 2 3 2 3 \frac {6}{2 5} \end{array}
$$

implies that the allocations are efficient.

This example shows that there is a one-to-one relation between the conditions of the core of RSgames in both the reduced formulation in theorem 5.1 and the alternative formulation in theorem 5.6.

## 6. A solution for RS-games

In the previous section one single-valued solution for RS-games was already discussed briefly, namely the altruistic allocation $x ^ { a } ( \nu )$ This allocation always belongs to the core but it is not fair because it assigns a zero payoff to the supplier although this company is needed to obtain the largest total profits. Instead, a suitable solution for RS-games should assign a positive payoff to the supplier and it should belong to the core of the game. Four desirable properties for a single-valued solution $\varphi$ for RS-games $( N _ { 0 } , \nu )$ are:

(EF) Efficiency. $\begin{array} { r } { \sum _ { i \in N _ { 0 } } \varphi _ { i } (  { \boldsymbol \nu } ) =  { \boldsymbol \nu } ( N _ { 0 } ) } \end{array}$ (SR) Stability for retailers. $\textstyle \sum _ { i \in S } \varphi _ { i } ( \nu ) \geq \nu ( S )$ for all coalitions $S \subseteq N .$

(RR) $\begin{array} { l } { { \mathrm { R e t a 1 l e r ~ r e d u c t i o n . } } _ { \dot { \nu } ( S _ { 0 } ^ { i } ) - \nu ( S ^ { i } ) } } \\ { { \varphi _ { i } ( \nu ) = \nu ( \{ 0 , i \} ) - \frac { \dot { \nu } ( S _ { 0 } ^ { i } ) - \nu ( S ^ { i } ) } { s ^ { i } } } } \\ { { S ^ { i } \subseteq N , \mathrm { f o r ~ a l l } i \in N . } } \end{array}$ for some coalition

(PD) Preservation of differences for retailers. $\varphi _ { i } ( \nu ) -$ $\varphi _ { j } ( \nu ) { = } \nu ( \{ 0 , i \} ) { - } \nu ( \{ 0 , j \} )$ for all $i , j \in N$ with $i \neq j$

Efficiency implies that the total benefit is divided among the players, while stability for retailers ensures coalitional stability for all coalitions of retailers. The retailer reduction property says that a retailer receives an amount smaller than his joint profit with the supplier $\nu ( \{ 0 , i \} )$ . The reduction equals the gain per capita for coalition $S ^ { i }$ from cooperation with the supplier, $( \nu ( S _ { 0 } ^ { i } ) - \nu ( S ^ { i } ) ) / s ^ { i }$ , for some coalition of retailers $S ^ { i } .$ . Finally, the preservation of differences for retailers property is a modification of the preservation of differences property by [10]. The (PD) property states that the difference in payoffs for two retailers should equal the difference in their joint profits with the supplier.

The main result in this section states that there exists a unique solution for RS-games satisfying the properties (EF), (SR), (RR) and (PD).

Theorem 6.1. Let $( N _ { O } , c , w ,$ P) be an RS-situation and $( N _ { O } ,$ v) the corresponding RS-game. The unique solution $\xi$ on the class of RS-games, $R \bar { S } ^ { N _ { o } }$ , satisfying (EF), (SR), (RR) and (PD) is $\xi ( \nu ) = ( \xi _ { i } ( \nu ) ) _ { i \in N _ { 0 } }$ defined by

$$
\xi_ {i} (v) = \left\{ \begin{array}{l l} n \beta , & i = 0, \\ v (\{0, i \}) - \beta , & i \in N, \end{array} \right.
$$

where $\begin{array} { r } { \beta = \operatorname* { m i n } _ { S \subseteq N , S \not = \emptyset } \left\{ \frac { \nu ( S _ { 0 } ) - \nu ( S ) } { s } \right\} } \end{array}$

Proof. It is clear that ξ(v) satisfies (EF), (SR), (RR) and (PD).

To show the converse, take a solution φ on the class of RS-games that satisfies (EF), (SR), (RR) and (PD). By (RR), $\varphi _ { i } ( \nu ) { = } \nu ( \{ 0 , i \} ) { - } \alpha _ { i }$ with $\alpha _ { i } { = } ( \nu ( S _ { 0 } ^ { i } ) { - } \nu ( S ^ { i } ) ) / s ^ { i }$ for some coalition $S ^ { i } \subseteq N .$ , for all retailers i. By (PD), ${ \alpha _ { i } } \mathrm { { = } } { \alpha _ { j } }$ for all $i , j { \in } N$ with $i \neq j$ . This implies ${ \alpha } _ { i } { = } { \alpha } _ { \ast }$ for all $i \in N$

According to (SR) $\begin{array} { r } { \sum _ { i \in S } \varphi _ { i } ( \nu ) = \nu ( S _ { 0 } )  – s \alpha _ { * } \ge \nu ( S ) } \end{array}$ or equivalently $\alpha _ { \ast } \leq ( \nu ( S _ { 0 } ) - \nu ( S ) ) / s$ <sup>ð Þ ð Þ</sup>for all coalitions $S \subseteq N .$ . But then $\begin{array} { r } { \alpha _ { * } = \operatorname* { m i n } _ { S \subseteq N , S \neq \emptyset } \left\{ ( \nu ( S _ { 0 } ) - \nu ( S ) ) / s \right\} } \end{array}$ . Finally, by (EF) we conclude $\varphi = \xi .$ □

This unique solution $\xi$ is called the minimal-gainper-capita solution (in short: mgpc-solution) because each retailer pays the minimal gain per capita $\beta$ to the supplier. Two properties of mgpc-solutions follow.

Lemma 6.2. For all RS-games $( N _ { O } , \mathbf { \Lambda } _ { \nu } )$ the mgpcsolution is a core allocation, $\xi ( \nu ) \in C o r e ( N _ { O } , \nu )$ , and it assures a positive payoff to the supplier, $\xi _ { { \scriptscriptstyle O } } ( \nu ) > 0 .$

Proof. By property (iii) in lemma 4.4 $\nu ( S _ { 0 } ) { > } \nu ( S )$ which implies $\beta { > } 0$ . Hence,

$$
\xi_ {i} (v) = v (\{0, i \}) - \beta <   v (\{0, i \})
$$

for all retailers i. Together with (EF) and (SR) we conclude $\xi ( \nu ) \in \mathrm { C o r e } ( N _ { 0 } , \nu )$ . Second, the positive value of $\beta$ immediately implies $\xi _ { 0 } ( \nu ) > 0$ □

This lemma shows that the mgpc-solution $\xi ( \nu )$ is a stable allocation since it belongs to the core. Further, the supplier prefers this allocation to the altruistic allocation $x ^ { a } ( \nu )$ because it assigns a larger payoff to him.

Upon comparison of the mgpc-solution with the Shapley value Sh(v) [16], we observe the following. In the table below the solutions are mentioned for example 4.3.

<table><tr><td> $\xi(v)$ </td><td> $x^{a}(v)$ </td><td> $Sh(v)$ </td></tr><tr><td> $\begin{pmatrix} 3 \\ 4\frac{3}{4} \\ 7\frac{1}{2} \end{pmatrix}$ </td><td> $\begin{pmatrix} 0 \\ 6\frac{1}{4} \\ 9 \end{pmatrix}$ </td><td> $\begin{pmatrix} 2 \\ 5\frac{1}{4} \\ 8 \end{pmatrix}$ </td></tr></table>

In this example the Shapley value belongs to the core since the game is convex. The supplier prefers the mgpc-solution to the Shapley value since it results in a larger payoff 3 instead of 2. If in this example the wholesale price function w is changed to $w ( q ) { = } 5$ if $0 \leq q \leq 1$ and $w ( q ) { = } 9 / 2 + 1 / ( 2 q )$ if $q > 1$ then the solutions change as follows.

<table><tr><td> $\xi(v)$ </td><td> $x^{a}(v)$ </td><td> $Sh(v)$ </td></tr><tr><td> $\begin{pmatrix} 10\frac{3}{8} \\ 1\frac{1}{16} \\ 3\frac{13}{16} \end{pmatrix}$ </td><td> $\begin{pmatrix} 0 \\ 6\frac{1}{4} \\ 9 \end{pmatrix}$ </td><td> $\begin{pmatrix} 5\frac{31}{48} \\ 3\frac{71}{96} \\ 5\frac{83}{96} \end{pmatrix}$ </td></tr></table>

Again, all three solutions belong to the core and the supplier prefers the mgpc-solution. In example 5.7 the solutions are as follows.

<table><tr><td>ξ(v)</td><td>xa(v)</td><td>Sh(v)</td></tr><tr><td>(22 6/25)</td><td>0</td><td>(27 59/75)</td></tr><tr><td>1150 1/2</td><td>1161 31/50</td><td>1147 109/150</td></tr><tr><td>1150 1/2</td><td>1161 31/50</td><td>1147 109/150</td></tr></table>

Here, the Shapley value is not a core-allocation. Obviously, the supplier prefers the mgpc-solution to the altruistic allocation. From these observations we conclude that the mgpc-solution $\xi$ is suitable for RS-games because (a) it recognizes the importance of the supplier in achieving full cooperation and (b) it always belongs to the core of the RS-game, as opposed to the Shapley value.

Finally, to conclude this section, the four examples below show that the properties (EF), (SR), (RR) and (PD) are logically independent.

Example 6.3. Consider the solution $\varphi$ on $\mathsf { R S } ^ { N _ { 0 } }$ defined by

$$
\varphi_ {i} (v) = \left\{ \begin{array}{l l} 0, & i = 0, \\ v (\{0, 1 \}) - \beta , & i \in N. \end{array} \right.
$$

$\varphi$ satisfies (SR), (RR) and (PD) but not (EF).

Example 6.4. Consider $\varphi$ on $\mathsf { R S } ^ { N _ { 0 } }$ defined by

$$
\varphi_ {i} (v) = \left\{ \begin{array}{l l} n \beta^ {*}, & i = 0, \\ v (\{0, 1 \}) - \beta^ {*}, & i \in N, \end{array} \right.
$$

where $\beta ^ { * } { \operatorname { : = m a x } _ { S \subseteq N , S \neq \emptyset } \ \left\{ ( \nu ( S _ { 0 } ) - \nu ( S ) ) / s \right\} }$ . φ satisfies (EF), (RR) and (PD) but not (SR).

Example 6.5. Consider $\varphi$ on $\mathsf { R S } ^ { N _ { 0 } }$ defined by

$$
\varphi_ {i} (v) = \left\{ \begin{array}{l l} n (\beta - 1), & i = 0, \\ v (\{0, 1 \}) - (\beta - 1), & i \in N, \end{array} \right.
$$

φ satisfies (EF), (SR) and (PD) but not (RR).

Example 6.6. Consider $\varphi$ on $\mathsf { R S } ^ { N _ { 0 } }$ defined by

$$
\varphi_ {i} (v) = \left\{ \begin{array}{l l} \sum_ {j \in N} \beta_ {j}, & i = 0, \\ v (\{0, 1 \}) - \beta_ {i}, & i \in N, \end{array} \right.
$$

where $\begin{array} { r } { \beta _ { i } { : = } \operatorname* { m i n } _ { S _ { \mathrm { c } } N , i \in { S } } \{ ( \nu ( S _ { 0 } ) - \nu ( S ) ) / s \} , \ i \in N . } \end{array}$ . φ satisfies (EF), (SR) and (RR) but not (PD).

## 7. Concluding remarks

In this paper we studied single-period distribution chains consisting of a supplier and multiple noncompeting retailers from a game-theoretic viewpoint. All companies have incentives to cooperate since this results in reduced costs and consequently in increased profits. Therefore, these chains are analyzed by means of their corresponding cooperative games, the RSgames. Among others it is shown that any RS-game has a nonempty core. Further, any core-allocation has a natural interpretation in terms of its underlying distribution chain. One such a core-allocation is the mgpcsolution for RS-games, whose characterization is included. This solution is fit for RS-games since it recognizes the importance of the supplier in achieving full cooperation. These results imply that the companies in a distribution chain are willing to cooperate because there exist stable distributions of the joint profit, namely the core-allocations. Further, the mgpc-solution is a suitable allocation since it is designed especially for this kind of distribution chains.

Topics for further research are: (1) examine other core-allocations like e.g. the nucleolus, and the τ-value; (2) investigate how the results change if the wholesale price function is endogenous; (3) analyze what happens if the unit production cost depends on the total quantity to be produced; (4) study the new model and game that arise when considering the warehouse as a decisionmaker/player.

## References

[1] F. Bernstein, A. Federgruen, Pricing and replenishment strategies in a distribution system with competing retailers, Operations Research 51 (3) (2003) 409–426.

[2] F. Bernstein, A. Federgruen, Decentralized supply chains with competing retailers under demand uncertainty, Management Science 51 (1) (2005) 18–29.

[3] O.N. Bondareva, Some applications of linear programming methods to the theory of cooperative games (in Russian), Problemy Kibernety 10 (1963) 119–139.

[4] P. Borm, H. Hamers, R. Hendrickx, Operations research games: a survey, TOP 9 (2001) 139–199.

[5] G.P. Cachon, M.A. Lariviere, Turning the supply chain into a revenue chain, Harvard Business Review (2001) 20–21.

[6] G.P. Cachon, M.A. Lariviere, Supply chain coordination with revenue-sharing contracts: strengths and limitations, Management Science 51 (2005) 30–44.

[7] L.A. Guardiola, A. Meca, J. Puerto, On the core and Owen point of production-inventory games, CIO paper I-2004-27, Miguel Hernandez University, Elche, Spain, 2004.

[8] L.A. Guardiola, A. Meca, J. Puerto, Coordination in periodic review inventory situations, CIO paper I-2006-13, Miguel Hernandez University, Elche, Spain, 2006.

[9] L.A. Guardiola, A. Meca, J. Puerto, Production-Inventory Games: A New Class of Totally Balanced Combinatorial Optimization Games, Forthcoming in Games and Economic Behavior, 2007.

[10] S. Hart, A. Mas-Colell, Potential, value, and consistency, Econometrica 57 (1989) 589–614.

[11] H. Krishnan, R. Kapuscinski, D. Butz, Coordinating contracts for decentralized supply chains with retailer promotional effort, Management Science 50 (1) (2001) 48–63.

[12] E. Markakis, A. Saberi, On the core of the multicommodity flow game, Decision Support Systems 39 (2005) 3–10.

[13] S. Minner, Bargaining for cooperative economic ordering, Decision Support Systems 43 (2) (2007) 569–583.

[14] U. Özen, J. Fransoo, H.W. Norde, M. Slikker, Cooperation between Multiple Newsvendors with Warehouses, CentER DP 2004-34, Tilburg University, Tilburg, The Netherlands, 2004.

[15] L.W. Robinson, A comment on Gerchak and Gupta's ‘On Apportioning Costs to Customers in Centralized Continuous Review Inventory Systems’, Journal of Operations Management 11 (1993) 99–102.

[16] L.S. Shapley, A Value for n-Person Games, in: H. Kuhn, A.W. Tucker (Eds.), Contributions to the Theory of Games II, Princeton University Press, Princeton, 1953, pp. 307–317.

[17] L.S. Shapley, On balanced sets and cores, Naval Research Logististics 14 (1967) 453–460.

[18] L.S. Shapley, Cores of convex games, International Journal of Game Theory 1 (1971) 11–26.

[19] M. Slikker, J. Fransoo, M. Wouters, Joint Ordering in Multiple News-Vendor Situations: A Game Theoretical Approach, working paper, Eindhoven University of Technology, Eindhoven, The Netherlands, 2001.

[20] M. Slikker, J. Fransoo, M. Wouters, Cooperation between multiple news-vendors with transshipments, European Journal of Operational Research 167 (2005) 370–380.

[21] T. Taylor, Supply chain coordination under channel rebates with sales effort effects, Management Science 45 (1992) 1339–1385.

[22] A. Tsay, S. Nahmias, N. Agrawal (Eds.), Modeling Supply Chain Contracts: A Review, Quantitative Models for Supply Chain Management, Kluwer, Boston, MA, 1998.

[23] W. van den Heuvel, P. Borm, H. Hamers, Economic Lot-sizing Games, European Journal of Operational Research 176 (2007) 1117–1130.

[24] G. van Ryzin, S. Mahajan, Supply Chain Coordination under Horizontal Competition, Working paper, Columbia University, New York, 2000.

[25] Q. Wang, M. Parlar, A three-person game theory model arising in stochastic inventory control, European Journal of Operational Research 76 (1994) 83–97.

![](/api/attachments/K5RAAHJ8/fulltext/images/d1236663ef31563b4156083d94d629d03cf54f22eac101e4e4c2e6b9082ff7f5.jpg)  
perative game theory  
Ana Meca is Associated Professor in the Game Theory Research (GATHER) Group at the Operations Research Center, University Miguel Hernández of Elche in Alicante, Spain. She received her Mathematics degree from the University of Granada (Spain) and her PhD from the University Miguel Hernández of Elche. Her areas of specialization and publications are in Operation Research Gamesinventory games, cooperation and coordination within supply chains, allocation of joint profit in supply chains-and noncoo-

![](/api/attachments/K5RAAHJ8/fulltext/images/6f3eee5306f1cc767bd7cd03f779f2a241be1ec828ac73fd4d7d7dc1ce0a8faa.jpg)  
Judith Timmer is Assistant Professor in the Stochastic Operations Research group at the University of Twente in Enschede, The Netherlands. Her research interests include cooperation and coordination within supply chains, allocation of joint profit in supply chains, inventory management and game theory.

![](/api/attachments/K5RAAHJ8/fulltext/images/1926ae5efaa59a01110b014d3eaf33bf2a3eecc99a7062709aa36c70e8348e89.jpg)

Luis A. Guardiola is a PhD student in the Game Theory Research (GATHER) Group at the Operations Research Center, University Miguel Hernández of Elche in Alicante, Spain. He received his Mathematics degree from the University of Alicante in 2002. His major research interests are in Operation Research Games: inventory games, cooperation and coordination within supply chains, allocation of joint profit in supply chains.
