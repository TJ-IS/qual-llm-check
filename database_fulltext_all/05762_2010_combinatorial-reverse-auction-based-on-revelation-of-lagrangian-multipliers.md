---
otero_id: 5762
otero_key: "CEPQ3TVB"
title: "Combinatorial reverse auction based on revelation of Lagrangian multipliers"
authors: "Fu-Shiung Hsieh"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.08.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combinatorial reverse auction based on revelation of Lagrangian multipliers

Fu-Shiung Hsieh

Department of Computer Science and Information Engineering, Chaoyang University of Technology, Taiwan

a r t i c l e i n f o

Article history: Received 8 January 2009 Received in revised form 3 August 2009 Accepted 30 August 2009 Available online 13 September 2009

Keywords: Auction e-Commerce Integer programming Optimization Bid

## a b s t r a c t

Recently, researchers have proposed decision support tool for generating suggestions for bids in combinatorial reverse auction based on disclosure of bids. An interesting issue is to design an effective mechanism to guide the bidders to collectively minimize the overall cost without explicitly disclosing the bids. We consider a winner determination problem for combinatorial reverse auction and study how to support the bidders' decisions without explicitly disclosing the bids of others. We propose an information revelation scheme for a buyer to guide the sellers to generate potential winning bids to minimize the overall cost. The main results include: (1) a problem formulation for the combinatorial reverse auction problem; (2) a solution methodology based on Lagrangian relaxation; (3) a scheme to guide the sellers to generate potential winning bids for the bidders in multi-round combinatorial reverse auctions based on revelation of Lagrangian multipliers; (4) a heuristic algorithm for <sup>fi</sup>nding a near-optimal feasible solution and (5) results and analysis of our solution algorithms.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Auctions are popular, distributed and autonomy preserving ways of allocating items or tasks among multiple agents to maximize revenue or minimize cost. In economics, different types of auctions have been proposed and extensively studied, including English Auction (open ascending price auction), Dutch auction (open descending price auction), sealed <sup>fi</sup>rst-price auction, etc. Single item auctions are by far the most common auction format, but they are not always ef<sup>fi</sup>cient. Combinatorial auctions [4,16,22,26] enable several bidders to bid on different combination of goods according to personal preferences. Allowing bids for bundles of items is the foundation of combinatorial auctions. Bidders can select multiple items at one time and offer those items a price. It enables bidders to decide combinations of auction according to personal preferences of bidders. Combinatorial auctions are bene<sup>fi</sup>cial if complementarities exist between the items to be auctioned. Well-known examples are the auctioning of Federal Communications Commission's radio spectrum licenses, the sales of airport time slots, and allocation of delivery routes. Applying combinatorial auctions in corporations' procurement processes can lead to signi<sup>fi</sup>cant savings [17,18]. Reverse auction is a business auction model that can be applied to corporations' procurement. Combinatorial reverse auction enables buyers to simultaneously purchase multiple goods with the lowest prices from the sellers.

Combinatorial auctions have attracted considerable attention in the existing literature. An excellent survey on combinatorial auctions can be found in [3,19]. Combinatorial auctions have been notoriously dif<sup>fi</sup>cult to solve from a computational point of view [21] due to the exponential growth of the number of combinations [25]. The combinatorial auction problem can be modeled as a set packing problems (SPP) [2,5,10,24] Sandholm et al. mentioned that determining the winners so as to maximize revenue in combinatorial auction is NP-complete [22,23]. Many algorithms have been developed for combinatorial auction problems. Exact algorithms have been developed for the SPP problem, including iterative deepening A\* search [23] and the direct application of available CPLEX IP solver [2]. Gonen and Lehmann proposed branch and bound heuristics for <sup>fi</sup>nding optimal solutions for multi-unit combinatorial auctions [7]. Jones and Koehler studied combinatorial auctions using rule-based bids [13]. In [8]; [11,12] the authors proposed a Lagrangian heuristic and a Lagrangian relaxation approach for combinatorial reverse auction problems, respectively. Although combinatorial reverse auctions have been extensively studied, most studies focus on the development of ef<sup>fi</sup>cient solution algorithms to determine winners. From the viewpoint of a bidder, how to <sup>fi</sup>nd a potential winning bid that maximizes the pro<sup>fi</sup>t is a key issue. In practice, each seller has no idea about the bids placed by other sellers at the beginning of a combinatorial reverse auction. Therefore, each seller is “blind” in creating his bids. The bid placed by a seller is usually a pro<sup>fi</sup>t maximizing bid that does not take into account the bids placed by other sellers. However, a pro<sup>fi</sup>t maximizing bid may not be a winning bid. An interesting question is to design an information revelation mechanism to assist a seller to <sup>fi</sup>nd pro<sup>fi</sup>t maximizing winning bids while minimizing the cost of the buyer.

Recently, decision support in auctions and combinatorial auctions has received signi<sup>fi</sup>cant attention. Adomavicius and Gupta presented several metrics that bidders can use to evaluate the current auction situation and the potential of each bid being among the winners [1]. The weakness of solving the winner determination problem (WDP) of combinatorial auctions in one shot is the black box nature of integer programming. Another stream of literature in combinatorial auctions is on ascending auctions, in which bidders, instead of bidding one price for the bundles, engage in multiple rounds of auctions of different bundles. Adomavicius and Gupta [1], among other proponents of the approach, argued that one advantage over the seal-bid one-shot format is that bidders can get pricing feedback from the process. Our approach may open up the black box slightly to the bidders by offering the values of Lagrangian multipliers to them.

Kwasnica et al. provided the bidders with a vector of prices (one for each commodity) that new bids must beat in order to be accepted [14]. Gallien and Wein presented a system and the underlying theory for an optimization-based multi-item auction mechanism that relies on the solution of a linear program for minimizing the buyer's cost under the suppliers' known capacity constraints [6]. They assist suppliers in <sup>fi</sup>nding a winning bid price. The underlying assumption is that the suppliers are willing to disclose their cost functions to a supposedly neutral third party auction organizer. Hohner et al. provided feedback to nonwinning bidders regarding clearing prices, at which supply for each item equals demand [9]. Leskelä et al. [15] proposed a decision support tool for generating suggestions for bids that would be among the current winners of the auction. Their results indicate that the quantity support tool is useful as it decreases the total cost to the buyer and improves the ef<sup>fi</sup>ciency of the auction. The support tool of Leskelä et al. requires the information of the bids placed by other bidders. To apply the support tool of Leskelä et al. requires disclosing the bids of other bidders. An interesting question is how to develop an effective method to support bidders' decision without disclosing the bids while minimizing buyer's total cost. The goal of this paper is to design an effective mechanism to guide the bidders to collectively minimize the overall cost in combinatorial reverse auction. We consider a winner determination problem for combinatorial reverse auction in which a buyer wants to acquire items from a set of sellers and each seller can provide a set of items. We propose an information revelation scheme for a buyer to guide the bidders to generate potential winning bids to minimize the overall cost without disclosing the bids to all the bidders.

One way to reduce the computational complexity in solving the winner determination problem (WDP) for combinatorial reverse auction is to set up a <sup>fi</sup>ctitious market to determine an allocation and prices in a decentralized way to adapt to dynamic environments where bidders and items may change from time to time. In this paper, we apply Lagrangian relaxation technique to develop a solution algorithm for WDP. We propose a multi-round combinatorial reverse auction algorithm to ef<sup>fi</sup>ciently <sup>fi</sup>nd a solution based on revelation of Lagrangian multipliers for each type of item at the end of each round. In our multi-round combinatorial reverse auction algorithm, Lagrangian relaxation is applied to obtain a solution at the end of each round. To take advantage of Lagrangian multipliers to ef<sup>fi</sup>ciently guide the bidders in the bidding processes, the Lagrangian multipliers are revealed to all the bidders. We propose a combinatorial reverse auction information revelation scheme based on Lagrangian multipliers. A seller may generate a new bid according to the most recently revealed Lagrangian multipliers.

Lagrangian relaxation provides a systematic approach to determine an allocation and prices based on the introduction of Lagrangian multipliers, which set prices for each item to be purchased by the buyer. If two or more sellers compete for the same item, the price will be adjusted. This saves bidders from specifying their bids for every possible combination and the buyer from having to process each bid function. Based on the price for the individual items, bidders submit bids. The bundle associated with a bid is tentatively assigned to that bidder only if the price of the bid is the lowest. Based on the iterative price adjustment mechanism, a solution will be obtained. It should be emphasized that Lagrangian relaxation is not guaranteed to <sup>fi</sup>nd the optimal solution to the underlying problem. Furthermore, it is not guaranteed to produce a feasible solution by applying Lagrangian relaxation technique. In case the resulting solution is not feasible, a heuristic algorithm must be applied to adjust the infeasible solution to a feasible one. We develop a heuristic algorithm for <sup>fi</sup>nding a nearoptimal, feasible solution based on the solution of the relaxed problem. We also demonstrate the advantage of multi-round combinatorial reverse auction algorithm (with revelation of Lagrangian multipliers) by comparing it with the single-round combinatorial reverse auction algorithm (without information revelation). Our results indicate that signi<sup>fi</sup>cant improvement in costs can be achieved by applying our method at the price of more but acceptable CPU time.

In summary, the main results presented in this paper include: (1) a problem formulation for the combinatorial reverse auction problem; (2) a solution methodology based on Lagrangian relaxation; (3) a price information revelation scheme to facilitate auction based on an economic interpretation of Lagrangian multipliers and (4) results and analysis of our solution algorithms.

The remainder of this paper is organized as follows. In Section 2, we present the problem formulation. In Section 3, we propose the solution algorithms for the dual problem and give an economic interpretation for our solution approach. In Section 4, we propose a combinatorial reverse auction information revelation scheme based on Lagrangian multipliers. In Section 5, we concentrate on the heuristic algorithm for <sup>fi</sup>nding a feasible solution. Finally, we demonstrate the effectiveness of the proposed algorithms by analyzing the results of many numerical examples. We conclude this paper in Section 7.

## 2. Combinatorial reverse auction problem formulation

In this paper, we <sup>fi</sup>rst formulate the combinatorial reverse auction problem as an integer programming problem. We then develop solution algorithms based on Lagrangian relaxation. Fig. 1 illustrates an application scenario in which Buyer requests to purchase at least a bundle of items 2A, 3B, 2C and 1D from the market. There are three bidders, Seller 1, Seller 2 and Seller 3 who place bids in the system. Suppose Seller 1 places two bids: (1A, 2B, p11) and (1C, 1D, p12), where p11 and p12 denote the prices of the bids. Seller 2 places two bids: (1B, 2C, p21) and (2C, 1D, p22). Seller 3 places two bids: (1C, 1D, p31) and (1A,1B, p32). We assume that all the bids entered the auction are recorded. A bid is said to be active if it is in the solution. We assume that there is only one bid active for all the bids placed by the same bidder. For this example, the solution for this combinatorial reverse auction problem is Seller1: (1A, 2B, p11), Seller 2: (2C, 1D, p22) and Seller 3: (1A,1B, p32).

![](/api/attachments/CEPQ3TVB/fulltext/images/44759abfcc9b1181d6f6b67ca8d9b3c14b9b689eb5567de0539739fa0cd521a2.jpg)  
Fig. 1. Combinatorial reverse auction.

Consider a buyer who requests a set of items to be purchased. Let K denote the number of items requested. Let $d _ { k }$ denote the desired units of the k-th item, where $k { \in } \{ 1 , 2 , 3 , \ldots K \}$ . In a combinatorial reverse auction, there are many bidders. Let I denote the number of bidders in the combinatorial reverse auction. Each $i { \in } \{ 1 , 2 , 3 , { \ldots } , I \}$ represents a bidder. To model the combinatorial reverse auction problem, the bid must be represented mathematically. We use a vector $\pmb { b } _ { i j } = ( q _ { i j 1 } , q _ { i j 2 } ,$ $q _ { i j 3 } , . . . , q _ { i j K } , p _ { i j } )$ to represent the j-th bid submitted by bidder i, where $q _ { i j k }$ is a nonnegative integer that denotes the quantity of the k-th items and $p _ { i j }$ is a real positive number that denotes the price of the bundle. As the quantity of the k-th items cannot exceed the quantity $d _ { k } ,$ it follows that the constraint $0 \leq q _ { i j k } \leq d _ { k }$ must be satis<sup>fi</sup>ed. The j-th bid ${ \pmb { b } } _ { i j }$ is actually an offer to deliver $q _ { i j k }$ units of items for each $k { \in } \{ 1 , 2 , 3 , { \ldots } _ { 1 }$ K} a total price of $\dot { p } _ { i j } .$ Let n denote the number of bids placed by bidder $i { \in } \{ 1 , 2 , 3 , { \ldots } , I \} .$ . Let J denote the maximum number of bids that a bidder can place in each round of combinatorial reverse auction. That is, $J = \operatorname* { m a x } _ { i \in \{ 1 . 2 . . . . . I \} } n _ { i }$ . To formulate the problem, we use the variable $x _ { i j }$ to <sup>f g</sup>indicate that the j-th bid placed by bidder i is active $( x _ { i j } = 1 )$ or inactive $( x _ { i j } = 0 )$ . The winner determination problem can be formulated as an integer programming problem as follows.

Winner determination problem (WDP):

$$
\min \sum_ {i = 1} ^ {1} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j}
$$

$$
\mathrm{s.t.} \sum_ {i = 1} ^ {1} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} \geq d _ {k} \forall k = 1, 2, \dots , K\tag{2 - 1}
$$

$$
\sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \forall i = 1, \dots , I\tag{2 - 2}
$$

$$
x _ {i j} \in \{0, 1 \}.\tag{2 - 3}
$$

Condition (2-1) in WDP assumes “free disposal” as the total quantity offered by the winners must be greater than or equal to the desired quantity of the buyer. If there are more quantities provided than needed, we can dispose of the surplus with no additional cost. One way to reduce the computational burden in solving the WDP is to adopt Lagrangian relaxation approach to set up a <sup>fi</sup>ctitious market to determine an allocation and prices in a decentralized way to adapt to dynamic environments where bidders and items may change from time to time. The buyer announces which sets of items and sets prices for them. If two or more agents compete for the same item, the buyer adjusts the price vector. This saves bidders from specifying their bids for every possible combination and the buyer from having to process each bid function. The bundle associated with the bid is tentatively assigned to that bidder only if the price of the bid is the lowest.

## 3. Solution algorithms for dual problem

The basic idea of Lagrangian relaxation is to relax some of the constraints of the original problem by moving them to the objective function with a penalty term. That is, infeasible solutions to the original problem are allowed, but they are penalized in the objective function in proportion to the amount of infeasibility. The constraints that are chosen to be relaxed are selected so that the optimization problem over the remaining set of constraints is in some sense easy. In WDP, we observe that the coupling among different operations is caused by the minimal requirement constraints (2-1). Let λ denotes the vector with λ(k) representing the Lagrangian multiplier for the k-th items. We de<sup>fi</sup>ne

$$
\begin{array}{l} L (\boldsymbol {\lambda}) = \min \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} P _ {i j} + \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) \bigg (d _ {k} - \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} \bigg) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1   \forall i = 1,..., I \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

For a given Lagrangian multiplier λ, the relaxation of constraints $( 2 \ – 1 )$ decomposes the original problem into a number of bidders' subproblems (BS). These subproblems can be solved independently. That is, the Lagrangian relaxation results in subproblems with a highly decentralized decision making structure. Interactions among subproblems are re<sup>fl</sup>ected through Lanrange multipliers, which are determined by solving the following dual problem.

max $L ( \lambda )$ , where λ≥0

$$
\begin{array}{l} L (\boldsymbol {\lambda}) = \min \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) d _ {k} + \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \left(P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j k}\right) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1   \forall i = 1,..., I \\ x _ {i j} \in \{0, 1 \} \\ = \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) d _ {k} + \sum_ {i = 1} ^ {I} L _ {i} (\boldsymbol {\lambda}), \text {with} \\ L _ {i} (\boldsymbol {\lambda}) = \min \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \left(P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j k}\right) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

$L _ { i } ( \boldsymbol { \lambda } )$ de<sup>fi</sup>nes a bidder's subproblem (BS). Our methodology for <sup>fi</sup>nding a near-optimal solution of WDP is developed based on the result of Lagrangian relaxation and decomposition. It consists of three parts: (1) an algorithm for solving subproblems, (2) a subgradient method for solving the dual problem and (3) a heuristic algorithm for <sup>fi</sup>nding a near-optimal feasible solution. In this section, we focus on part (1) and part (2). Part (3) will be detailed in Section 5.

(1) An algorithm for solving subproblems

Given λ, the optimal solution to BS subproblem $L _ { i } ( \boldsymbol { \lambda } )$ can be solved

$\begin{array} { r l } {  { \mathrm { ~ \stackrel { d S \ I O I I O W S . } { L e t \ j ^ { * } } = \mathrm { \ a r g \operatorname* { m i n } } _ { j \in \{ 1 , 2 , \ldots , n _ { i } \} } ( P _ { i j } - \sum _ { k = 1 } ^ { K } \mathrm { \ a } ( k ) q _ { i j k } ) } } } \\ & { L _ { i } ( \lambda ) \ \mathrm { i s \ a s \ f o l l o W S . } } \end{array}$ . The optimal solution to

$$
x _ {i j} = \left\{ \begin{array}{l l} 0 & \forall j \in \{1, 2,..., n _ {i} \} \setminus \{j ^ {*} \} \\ 1 & \text { if } P _ {i j ^ {*}} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j ^ {*} k} <   0 \\ 0 & \text { if } P _ {i j ^ {*}} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j ^ {*} k} \geq 0. \end{array} \right.
$$

Since evaluating $L _ { i } ( \boldsymbol { \lambda } )$ for each λ is a snap, if we can <sup>fi</sup>nd a fast way to determine the λthat solves, max $L ( \lambda )$ we would have a fast procedure λ>0 to <sup>fi</sup>nd a solution. Although the resulting solution (values of the x variables) need not be feasible, it could be adjusted to a feasible solution without a great increase in objective function value. Finding λ that solves max L λ can be accomplished using the subgradient algorithm. λ>0

(2) A subgradient method for solving the dual problem max L λ

Let $x ^ { l }$ be the optimal solution to the subproblems for given Lagrangian multipliers $\lambda ^ { l }$ of iteration l. We de<sup>fi</sup>ne the subgradient of $L ( \lambda )$ as

$$
g ^ {l} (k) = d _ {k} - \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} ^ {l} q _ {i j k}, \text {   where   } k \in \{1, 2,..., K \}.
$$

The subgradient method proposed by Polyak [20] is adopted to update λ as follows

$$
\lambda^ {l + 1} (k) = \left\{ \begin{array}{l} \boldsymbol {\lambda} ^ {l} (k) + \alpha^ {l} g ^ {l} (k) \text {   if   } \boldsymbol {\lambda} ^ {l} (k) + \alpha^ {l} \boldsymbol {\lambda} ^ {l} (k) \geq 0; \\ 0 \text {   otherwise.   } \end{array} \right.
$$

where $\begin{array} { r } { \alpha ^ { l } = c \frac { \bar { L } - L ( \lambda ) } { \underset { \ast } { \Sigma } ( g ^ { l } ( k ) ) ^ { 2 } } , 0 \leq c \leq 2 } \end{array}$ and L is an estimate of the optimal dual cost. The iteration step terminates if $\alpha ^ { l }$ is smaller than a threshold. Polyak proved that this method has a linear convergence rate. The structure of our algorithms is depicted in Fig. 2.

Iterative application of the algorithms in (1) and (2) may converge to an optimal dual solution $( x ^ { * } , \lambda ^ { * } )$ . It should be emphasized that Lagrangian relaxation is not guaranteed to <sup>fi</sup>nd the optimal solution to the underlying problem. Rather, it <sup>fi</sup>nds an optimal solution to a relaxation of it. While Lagrangian relaxation will yield the optimal objective function value for the linear relaxation of the underlying integer program, it is not guaranteed to produce a feasible solution. Thus the solution generated may not satisfy the complementary slackness conditions. In case the solution is not feasible, we must develop a heuristic algorithm to <sup>fi</sup>nd a feasible solution. Development of a heuristic algorithm to <sup>fi</sup>nd a feasible solution is detailed in Section 5.

## 4. Revelation of Lagrangian multipliers

Decomposition of the original problem into BS subproblems provides us a different viewpoint of the original problem. Decision making of the original problem is composed of those of BSs. BS can be regarded as the decision making problem to acquire the required resources and bene<sup>fi</sup>ts from utilizing the acquired resources. The decision processes of each entity are just like the ones made by sellers in a real business environment. That is, a seller is willing to sell a good only when its utility is at least equal to its market price. The buyer will raise the market price in case of resource shortage. Such processes occur in the decision making of the BS. Lagrangian multipliers can often be given the economic interpretation as marginal costs for using the items when they are used to relax demand constraints. In our relaxation procedure above, the Lagrangian multipliers λ(k) are used to relax the demand constraints of item k. Lagrangian multipliers λ(k) can be interpreted as the marginal bene<sup>fi</sup>t of using an additional unit of item k. Suppose the constraint $d _ { k } - \sum _ { i = 1 } ^ { I } \ \sum _ { j \ = \ 1 } ^ { n _ { i } } x _ { i j } q _ { i j k } { \le } 0$ is violated. That is, $d _ { k } - \sum _ { i = 1 } ^ { I } \ \sum _ { j } ^ { n _ { i } } x _ { i j } q _ { i j k } > 0$ . In this case, adding an additional unit of item k reduces the total cost by $\pmb { \lambda } ( k )$ . On the other hand, if the constraint $d _ { k } - \sum _ { i = 1 } ^ { I } \ \sum _ { j \ = \ 1 } ^ { n _ { i } } x _ { i j } q _ { i j k } { \le } 0$ holds, adding an additional unit of item increases the total cost by $\pmb { \lambda } ( k )$

To take advantage of the Lagrangian multipliers to ef<sup>fi</sup>ciently guide the bidders in a combinatorial reverse auction, we propose an information revelation scheme. In this section, we propose an information revelation scheme to guide the bidders without revealing the details of all the bids submitted. The information revealed in our scheme is based on Lagrangian multipliers obtained at the end of each round of the combinatorial reverse auction. Let $\lambda ^ { * }$ denote the Lagrangian multipliers obtained at the end of the m-th round. Lagrangian multipliers $\lambda ^ { * } ( k )$ for each item k of the m-th round are revealed. By revealing $\lambda ^ { * } ( k )$ for each item k, each bidder will know the marginal bene<sup>fi</sup>t of adding a unit of item k. Thus, each bidder may place a new bid based on $\lambda ^ { * } ( k )$ for each k. To determine whether a new bid should be placed, consider the following BS for bidder $i \in { I } { : }$

Suppose

$$
\begin{array}{l} L _ {i} (\boldsymbol {\lambda}) = \min \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \Bigg (P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} ^ {*} (k) q _ {i j k} \Bigg) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

Suppose a new bid $\pmb { b } _ { i j ^ { \prime } } = ( q _ { i j ^ { \prime } 1 } , q _ { i j ^ { \prime } 2 } , q _ { i j ^ { \prime } 3 } , . . . , q _ { i j ^ { \prime } K } , p _ { i j ^ { \prime } } )$ is placed by bidder i. Then

$$
\begin{array}{l} L _ {i} ^ {\prime} (\boldsymbol {\lambda}) = \min \left(\sum_ {j = 1} ^ {n _ {i}} x _ {i j} \left(P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} ^ {*} (k) q _ {i j k}\right) + x _ {i j ^ {\prime}} \left(P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} ^ {*} (k) q _ {i j ^ {\prime} k}\right)\right) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

Suppose

$$
P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j ^ {\prime} k} \leq P _ {i j} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j k} \forall j \in \{1, 2,..., n _ {i} \}.\tag{4 - 1}
$$

In this case, $\pmb { b } _ { i j ^ { \prime } }$ is the better than all the existing bids placed by bidder i. It will be the bid selected by the algorithm. Therefore, $\mathrm { i f } \lambda ^ { * } ( k )$ is revealed for each item k, inequality $( 4 - 1 )$ imposes a condition for bidder i to place a new bid that will be selected by the Lagrangian relaxation solution algorithm.

To be a winner in the next round of combinatorial reverse auction, a bidder may draw up a new bid under the constraint that the minimal pro<sup>fi</sup>t must be satis<sup>fi</sup>ed. A bidder determines whether he should submit a new bid $\pmb { b } _ { i j ^ { \prime } }$ to maximize the pro<sup>fi</sup>t while satisfying constraints $( 4 - 1 )$ . To achieve this objective, the following optimization problem is formulated, where $c _ { i } ^ { * }$ denotes the minimal pro<sup>fi</sup>ts bidder i expects to take from the combinatorial reverse auction.

![](/api/attachments/CEPQ3TVB/fulltext/images/b8e60006c1fe881559d742718eaacfaf9a3522cfaaf4566c8ec9b75f348baa3b.jpg)  
Fig. 2. Structure of solution algorithms.

Pro<sup>fi</sup>t Maximization for Bidder (PMB)

$$
\begin{array}{l} \max P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} c _ {i j ^ {\prime} k} q _ {i j ^ {\prime} k} \\ \text { s.t. } P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} c _ {i j ^ {\prime} k} q _ {i j ^ {\prime} k} \geq c _ {i} ^ {*} \\ P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j ^ {\prime} k} \leq P _ {i j} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j k} \forall j \in \{1, 2,..., n _ {i} \} \\ P _ {i j ^ {\prime}} \geq 0 \\ q _ {i j ^ {\prime} k} \geq 0 \text { and } q _ {i j ^ {\prime} k} \in Z ^ {+} \cup \{0 \} \forall k \in \{1, 2,..., K \}. \end{array}
$$

A problem obtained by relaxing the constraints $q _ { i j ^ { \prime } k } { \in } Z ^ { + } \cup \{ 0 \} \forall k { \in } \{ 1 $ $2 , . . . , K \}$ in PMB is formulated as follows.

Linear Programming for PMB (LPPMB)

$$
\begin{array}{l} \max P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} c _ {i j ^ {\prime} k} q _ {i j ^ {\prime} k} \\ \text { s.t. } P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} c _ {i j ^ {\prime} k} q _ {i j ^ {\prime} k} \geq c _ {i} ^ {*} \\ P _ {i j ^ {\prime}} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j ^ {\prime} k} \leq P _ {i j} - \sum_ {k = 1} ^ {K} \lambda^ {*} (k) q _ {i j k} \forall j \in \{1, 2,..., n _ {i} \} \\ P _ {i j ^ {\prime}} \geq 0 \\ q _ {i j ^ {\prime} k} \geq 0   \forall k \in \{1, 2,..., K \}. \end{array}
$$

Bidder i determines whether to submit a new bid by solving LPPMB. If there exists a solution for LPPMB, a new bid will be submitted based on the solution. Otherwise, no new bid will be submitted.

Suppose the combinatorial reverse auction is conducted M rounds. Our information revelation scheme is applied at the end of each round. Each bidder may submit J bids in each round. Therefore, in the M-th round, a bidder may submit at most MJ bids.

## 5. A heuristic algorithm for <sup>fi</sup>nding a feasible solution

Although revelation of Lagrangian multipliers may improve the ef<sup>fi</sup>ciency as well as reduce the costs, it is still possible that the outcome of the multi-round combinatorial reverse auction is still not a feasible solution. In this case, we develop a heuristic algorithm to <sup>fi</sup>nd a feasible solution based on the solution $x ^ { * }$ and the Lagrangian multipliers $\lambda ^ { * }$ obtained at the end of the m-th round. The heuristic algorithm for <sup>fi</sup>nding a near-optimal feasible solution x ̅ based on the solution $( x ^ { * } , \lambda ^ { * } )$ of the relaxed problem is proposed in this section.

The solution obtained by applying the subgradient method may not be a feasible. If it is not feasible, it could be adjusted to a feasible solution without a great increase in objective function value. To adjust the solution of the dual problem to a feasible one, one must identify the set of demand constraints violated $K ^ { 0 }$ and the set of bidders $\hat { I ^ { 0 } }$ that is not a winner in the solution of the dual problem. Then we pick the bidders from the set $I ^ { 0 }$ according to the rule of minimal cost <sup>fi</sup>rst to ful<sup>fi</sup>ll the insuf<sup>fi</sup>cient quantity required by the set of violated demand constraints $K ^ { 0 }$

The solution $( x ^ { * } , \lambda ^ { * } )$ may result in one type of constraint violation due to relaxation: assignment of the quantity of items less than the demand of the items. Our heuristic scheme <sup>fi</sup>rst checks all the demand constraints $\begin{array} { c } { { \displaystyle \sum _ { i = 1 } ^ { I } \sum _ { j } ^ { n _ { i } } = { } _ { 1 } x _ { i j } ^ { * } q _ { i j k } \ge d _ { k } \forall k = 1 , 2 , . . . , K } } \end{array}$ that have not been satisfied. Let $\begin{array} { r } { \overset { ^ { 1 } } { K } \overset { ^ { 1 } } { \underset { ^ { 1 } = } { \longrightarrow } } \{ k | k \in \{ 1 , 2 , 3 , . . . , K \} , \overset { ^ { 1 } } { \underset { ^ { 1 } = - 1 } { \sum } } \ \sum _ { j = 1 } ^ { n _ { i } } x _ { i j } ^ { * } q _ { i j k } < d _ { k } \} } \end{array}$ $K ^ { 0 }$ denotes the set of demand constraints violated. Let $I ^ { 0 } = \{ i | i \in \{ 1 , 2 , 3$ $. . . , I \} , x _ { i j } ^ { * } = 0 \} . \ I ^ { 0 }$ denotes the set of bidders that is not a winner in solution x\*. To make the set of constraints $K ^ { 0 }$ satis<sup>fi</sup>ed, we <sup>fi</sup>rst pick $k { \in } K ^ { 0 } \operatorname { w i t h } k = \arg \operatorname* { m i n } _ { k \in K ^ { 0 } } d _ { k } { - } \sum _ { i = 1 } ^ { I } \sum _ { j = 1 } ^ { n _ { i } } { _ 1 } x _ { i j } ^ { * } q _ { i j k } .$ . The heuristic algorithm proceeds as follows to make constraint k satis<sup>fi</sup>ed. Select $i \in { I ^ { 0 } }$ and $j \in \{ 1$ $2 , . . . , n _ { i } \}$ with $j = \arg \operatorname* { m i n } _ { j \in \{ 1 , 2 , . . . n _ { i } \} , q _ { i j k } > 0 } p _ { i j }$ and se $\begin{array} { r } { { \bf \nabla } \cdot \overline { { \bf X } } _ { i j } = 1 . } \end{array}$ . After performing the above operation, we set $I ^ { 0 }  I ^ { 0 } \backslash \{ i \}$ . If the violation of the k-th constraint cannot be completely resolved, the same procedure repeats. Eventually, all the constraints will be satis<sup>fi</sup>ed.

Heuristic algorithm for <sup>fi</sup>nding a feasible solution

Step $0 . { \overline { { \mathrm { ~ X ~ } } } } \gets \mathbf { X } ^ { * } .$

Step 1. Find the set of demand constraints violated.

$$
\text { Find } K ^ {0} = \{k | k \in \{1, 2, 3,..., K \}, \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} ^ {*} q _ {i j k} <   d _ {k} \}.
$$

Step 2. Find the set of bidders that is not a winner in solution $x ^ { * } .$

$$
\text { Find } I ^ {0} = \{i | i \in \{1, 2, 3,..., I \}, x _ {i j} ^ {*} = 0 \}.
$$

Step 3. While $K ^ { 0 } \neq \boldsymbol { \phi } .$

$$
\begin{array}{l} \text {Select k = arg \min _ {k\in K^{0}} d_{k} - \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n_{i}} x_{ij} ^{*} q_{ijk} from K^{0}.} \\ \text {Select i\in I^{0} and j\in\{1,2,\ldots,n_{i}\} with j = arg \min _ {j\in\{1,2,\ldots n_{i}\},q_{ijk} >0} p_{ij}.} \\ \text {Set \overline {{x}} _{ij} = 1.} \\ I ^ {0} \leftarrow I ^ {0} \setminus \{i \}. \end{array}
$$

End while

The effectiveness of the solution algorithms can be evaluated based on the duality gap, which is the ratio of the difference between primal and dual objective values divided by the primal objective value. That is, duality gap is de<sup>fi</sup>ned $\mathsf { b y } \frac { f ( \overline { { \boldsymbol { x } } } ) - \mathsf { \bar { L } } ( \boldsymbol { \mathsf { X } } ^ { * } ) } { f ( \overline { { \boldsymbol { x } } } ) }$

$$
f (\overline {{x}}) = \sum_ {i = 1} ^ {I} \sum_ {j = 1} ^ {n _ {i}} \overline {{x}} _ {i j} p _ {i j}.
$$

## 6. Experimental results and analysis

Based on the proposed algorithms for combinatorial reverse auction, we conduct several examples to illustrate the effectiveness of our method.

Example 1. Consider a buyer who will purchase a set of <sup>fi</sup>ve items. The desired units of each type of items are one. Suppose there are two sellers. Suppose each seller only places two bids. For this example, we have

$$
\begin{array}{l} I = 2, J = 2, K = 5 \\ d _ {k} = 1 (d _ {1} = 1, d _ {2} = 1, d _ {3} = 1, d _ {4} = 1, d _ {5} = 1). \end{array}
$$

Suppose the four bids submitted by the two bidders are as follows:

$$
\begin{array}{l} q _ {1 1 1} = 1, q _ {1 1 2} = 0, q _ {1 1 3} = 1, q _ {1 1 4} = 0, q _ {1 1 5} = 1 \\ q _ {1 2 1} = 0, q _ {1 2 2} = 1, q _ {1 2 3} = 0, q _ {1 2 4} = 1, q _ {1 2 5} = 0 \\ q _ {2 1 1} = 1, q _ {2 1 2} = 0, q _ {2 1 3} = 1, q _ {2 1 4} = 0, q _ {2 1 5} = 1 \\ q _ {2 2 1} = 0, q _ {2 2 2} = 1, q _ {2 2 3} = 0, q _ {2 2 4} = 1, q _ {2 2 5} = 0. \\ P _ {1 1} = 1 0 0, P _ {1 2} = 6 0, P _ {2 1} = 9 0, P _ {2 2} = 4 0. \end{array}
$$

Suppose we initialize the Lagrangian multipliers as follows: $\lambda ( 1 ) =$ 10.0, $\lambda ( 2 ) = 1 0 . 0 , \lambda ( 3 ) = 1 0 . 0 , \lambda ( 4 ) = 1 0 . 0 , \lambda ( 5 ) = 1 0 . 0$ Our subgradient algorithm converges to the following solution:

$$
x _ {1 1} ^ {*} = 1, x _ {1 2} ^ {*} = 0, x _ {2 1} ^ {*} = 0, x _ {2 2} ^ {*} = 1.
$$

As the above solution is a feasible one, the heuristic algorithm needs not be applied. Therefore, $\overline { { \mathbf { x } } } _ { 1 1 } = 1 , \ \overline { { \mathbf { x } } } _ { 1 2 } = 0 , \ \overline { { \mathbf { x } } } _ { 2 1 } = 0 ,$ , and $\overline { { \mathbf { X } } } _ { 2 2 } = 1 .$ Indeed, the solution $x ^ { * }$ is also an optimal solution. The duality gap of the solution is as follows:

Duality $\mathrm { g a p } = 0 \%$

Example 2. Consider a buyer who will purchase a set of four items. The desired units of each type of items are

$$
d _ {1} = 2, d _ {2} = 1, d _ {3} = 2, d _ {4} = 1.
$$

Suppose there are three sellers. Suppose each bidder only places two bids. For this example, we have

$$
\begin{array}{l} {I = 3, J = 2, K = 4,} \\ {d _ {1} = 2, d _ {2} = 1, d _ {3} = 2, d _ {4} = 1.} \end{array}
$$

Suppose the four bids submitted by the two bidders are as follows:

$$
\begin{array}{l} q _ {1 1 1} = 1, q _ {1 1 2} = 0, q _ {1 1 3} = 1, q _ {1 1 4} = 0 \\ q _ {1 2 1} = 1, q _ {1 2 2} = 1, q _ {1 2 3} = 0, q _ {1 2 4} = 0 \\ q _ {2 1 1} = 0, q _ {2 1 2} = 0, q _ {2 1 3} = 1, q _ {2 1 4} = 0 \\ q _ {2 2 1} = 0, q _ {2 2 2} = 1, q _ {2 2 3} = 0, q _ {2 2 4} = 1 \\ q _ {3 1 1} = 0, q _ {3 1 2} = 0, q _ {3 1 3} = 1, q _ {3 1 4} = 0 \\ q _ {3 2 1} = 0, q _ {3 2 2} = 0, q _ {3 2 3} = 0, q _ {3 2 4} = 1. \\ P _ {1 1} = 7 0, P _ {1 2} = 7 5, P _ {2 1} = 4 0, P _ {2 2} = 8 0, P _ {3 1} = 4 5, P _ {3 2} = 5 0. \end{array}
$$

Suppose we initialize the Lagrangian multipliers as follows.

$$
\lambda (1) = 3 0. 0, \lambda (2) = 4 0. 0, \lambda (3) = 3 5. 0, \lambda (4) = 5 0. 0.
$$

Our subgradient algorithm converges to the following solution:

$$
x _ {1 2} ^ {*} = 1, x _ {2 2} ^ {*} = 1, x _ {3 2} ^ {*} = 1.
$$

As the above solution is not a feasible one, the heuristic algorithm needs to be applied. Our heuristic algorithm leads to the following feasible solution

$$
\bar {x} _ {1 1} = 1, \bar {x} _ {2 1} = 1, \bar {x} _ {2 2} = 1, \bar {x} _ {3 2} = 1.
$$

The duality gap of the solution is as follows:

Duality gap= 2.448%.

Despite the duality gap is not zero, the solution x̄ is an optimal solution for this example.

In addition to Example 1 and Example 2, Table 1 illustrates the duality gap of several cases based on the problem size (I, J, K). According the results, the duality gaps are within 3%. This means the solution methodology generates near-optimal solution.

In addition to the two examples above, we also conduct several experiments to study the computational ef<sup>fi</sup>ciency of our proposed algorithms. These experiments show the growth of CPU time with respect to I, J and K, respectively.

Fig. 3 shows the CPU time for a number of problems in which parameters J and K are <sup>fi</sup>xed while parameter I is changed. The increase in the CPU time is not signi<sup>fi</sup>cant as parameter I is increased. According to the following equation:

Table 1  
Duality gap of several cases.

<table><tr><td>I</td><td>J</td><td>K</td><td>Duality gap</td></tr><tr><td>5</td><td>10</td><td>5</td><td>2.8%</td></tr><tr><td>10</td><td>5</td><td>10</td><td>2.2%</td></tr><tr><td>30</td><td>10</td><td>20</td><td>2.4%</td></tr></table>

![](/api/attachments/CEPQ3TVB/fulltext/images/57b936b315fd667d3abd97a9b8c1c1cb1c67461aa184233fd86dff03e01a6feb.jpg)  
Fig. 3. CPU time (in millisecond) respect to I.

$$
L (\pmb {\lambda}) = \sum_ {k = 1} ^ {K} \pmb {\lambda} (k) d _ {k} + \sum_ {i = 1} ^ {I} L _ {i} (\pmb {\lambda}).
$$

This result justi<sup>fi</sup>es the fact that the CPU time to compute $L ( \lambda )$ Lλ for a given λ grows approximately linearly with respect to I.

The CPU time for a number of problems in which parameters I and K are <sup>fi</sup>xed while parameter J is changed is shown in Fig. 4. As J=max n<sub>i</sub>, it only in<sup>fl</sup>uences the computation of

$$
\begin{array}{l} L _ {i} (\boldsymbol {\lambda}) = \min \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \left(P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j k}\right) \\ \text {s.t.} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

Therefore, the CPU time to compute $L ( \lambda )$ for a given λ grows approximately linearly with J.

We also study the growth of the CPU time with respect to parameter K.

$$
\begin{array}{l} \text { As   } L (\boldsymbol {\lambda}) = \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) d _ {k} + \sum_ {i = 1} ^ {I} L _ {i} (\boldsymbol {\lambda}) \text {   with } \\ L _ {i} (\boldsymbol {\lambda}) = \min \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \left(P _ {i j} - \sum_ {k = 1} ^ {K} \boldsymbol {\lambda} (k) q _ {i j k}\right) \\ \text { s.t.   } \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \\ x _ {i j} \in \{0, 1 \}. \end{array}
$$

The CPU time to calculate $\sum _ { k = 1 } ^ { K } \lambda ( k ) q _ { i j k }$ will increase approximately proportionally with K. Note that the Lagrangian multiplier is updated as follows:

$$
\boldsymbol {\lambda} ^ {l + 1} (k) = \left\{ \begin{array}{l} \boldsymbol {\lambda} ^ {l} (k) + \alpha^ {l} g ^ {l} (k) \text {   if   } \boldsymbol {\lambda} ^ {l} (k) + \alpha^ {l} \boldsymbol {\lambda} ^ {l} (k) \geq 0; \\ 0 \text {   otherwise.   } \end{array} \right.
$$

![](/api/attachments/CEPQ3TVB/fulltext/images/88df535ad9a659bf38fbe53f85ead94b3b11cfb94510ac65af09b27568b57f52.jpg)  
Fig. 4. CPU time (in millisecond) respect to J.

As the number of Lagrangian multipliers is proportional to $K ,$ the CPU time computation involved in updating λ will increase approximately proportionally with $K ^ { 2 } .$

Fig. 5 shows the growth of CPU time with respect to K.

Fig. 6 shows the reduction on the cost for the combinatorial reverse auction Example 2 with <sup>fi</sup>ve rounds and

$$
\begin{array}{l} c _ {1 j ^ {\prime} 1} = 1, c _ {1 j ^ {\prime} 2} = 2, c _ {1 j ^ {\prime} 3} = 1, c _ {1 j ^ {\prime} 4} = 3 \\ c _ {2 j ^ {\prime} 1} = 2, c _ {2 j ^ {\prime} 2} = 2, c _ {2 j ^ {\prime} 3} = 1, c _ {2 j ^ {\prime} 4} = 1 \\ c _ {3 j ^ {\prime} 1} = 1, c _ {3 j ^ {\prime} 2} = 1, c _ {3 j ^ {\prime} 3} = 3, c _ {3 j ^ {\prime} 4} = 1. \end{array}
$$

Note that signi<sup>fi</sup>cant cost reduction can be achieved in the second round and the third round. The cost reduction diminishes at the fourth round and the <sup>fi</sup>fth round. This implies that the cost reduction can be expected in the <sup>fi</sup>rst few rounds.

Before concluding this paper, we compare the difference between the method proposed in this paper and the existing literature on combinatorial auctions. This paper is differentiated from the method proposed in [23] to <sup>fi</sup>nd the optimal solution in that we adopt the Lagrangian relaxation approach to <sup>fi</sup>nd approximate solutions. The advantage of our Lagrangian relaxation approach is to <sup>fi</sup>nd approximate solutions ef<sup>fi</sup>ciently. Numerical examples indicate that our algorithm generates near-optimal solution within acceptable CPU time. Our proposed algorithm is different from the one [8] based on Lagrangian heuristic in existing literature as our algorithm is based on the subgradient algorithm to adjust Lagrangian multipliers in multiround combinatorial reverse auctions. We propose an effective mechanism to guide the bidders to collectively minimize the overall cost without explicitly disclosing the bids. Our multi-round combinatorial reverse auction algorithm to guide sellers to generate potentially winning bids only relies on revelation of Lagrangian multipliers. It is different from the methods proposed in [6] and [15], which require revelation of all bids to generate suggestions for bids.

## 7. Conclusion

Combinatorial auctions enable several bidders to bid on different combination of goods according to personal preferences. Bidders can select multiple items at one time and offer those items a price. It enables bidders to decide combinations of auction according to personal preferences and more effectively arranges bid winners. Combinatorial auctions have been notoriously dif<sup>fi</sup>cult to solve from a computational point of view due to the exponential growth of the number of combinations. Although combinatorial reverse auctions have attracted a lot of attention recently, most studies focus on development of ef<sup>fi</sup>cient solution algorithms to determine winners. From the viewpoint of a buyer, an important issue is to design an effective mechanism to guide the bidders to collectively minimize the overall cost. On the other hand, from the viewpoint of a bidder, how to <sup>fi</sup>nd a potential winning bid that maximizes the pro<sup>fi</sup>t is a key issue. In practice, each seller has no idea about the bids placed by other sellers at the beginning of a combinatorial reverse auction. Therefore, each seller is “blind” in creating his bids. The bid placed by a seller is usually a pro<sup>fi</sup>t maximizing bid that does not take into account the bids placed by other sellers. However, a pro<sup>fi</sup>t maximizing bid may not be a winning bid. An interesting issue is to design an information revelation mechanism to assist a seller to <sup>fi</sup>nd pro<sup>fi</sup>t maximizing winning bid while minimizing the cost of the buyer.

![](/api/attachments/CEPQ3TVB/fulltext/images/627ceb9250c100646499676da8e869796283553735871e8118122fe83690038d.jpg)  
Fig. 5. CPU time (in millisecond) with respect to K.

![](/api/attachments/CEPQ3TVB/fulltext/images/6fd2268acb6f0563a197f4ee98c9a73bc0915e77530743e7bbb083d047f050c6.jpg)  
Fig. 6. Cost for each round m=1, 2, 3, 4, 5.

Motivated by the de<sup>fi</sup>ciency of existing results, we consider a winner determination problem for combinatorial reverse auction in which a buyer wants to acquire items from a set of sellers and each seller can provide a set of items. We propose an information revelation scheme for a buyer to guide the sellers to generate potential winning bids to minimize the overall cost ultimately. This paper is different from the one presented in [8] as we adopt the subgradient method to <sup>fi</sup>nd Lagrangian multipliers. Our multi-round combinatorial reverse auction algorithm to guide sellers to generate potentially winning bids only relies on revelation of Lagrangian multipliers. It is different from the methods proposed in [6] and [15], which require revelation of all bids to generate suggestions for bids.

We formulate a winner determination optimization problem for combinatorial auction. The demands of the buyer impose additional constraints on determination of the winners. By applying Lagrangian relaxation technique, the original optimization can be decomposed into a number of bidders' subproblems. Our methodology consists of <sup>fi</sup>ve parts: (1) an algorithm for solving bidders' subproblems by exploiting their individual structures; (2) a subgradient method for solving the non-differentiable dual problem; (3) an information revelation scheme to facilitate auction based on an economic interpretation of Lagrangian multipliers; (4) a heuristic algorithm for <sup>fi</sup>nding a near-optimal, feasible solution and (5) results and analysis of our solution algorithms. The information revealed is based on the Lagrangian multipliers that are iteratively updated in our algorithm. A bidder may submit a new bid based on the price information revealed. Although the price information revelation scheme may improve the performance of combinatorial reverse auctions, it does not guarantee a feasible solution. In case the resulting solution is not feasible, a heuristic algorithm must be applied to adjust the infeasible solution to a feasible one. We develop a heuristic algorithm for <sup>fi</sup>nding a nearoptimal, feasible solution based on the solution of the relaxed problem. Numerical results indicate that our proposed algorithms yield nearoptimal solutions. We also demonstrate the advantage of multi-round combinatorial reverse auction algorithm (with revelation of Lagrangian multipliers) by comparing it with the single-round combinatorial reverse auction algorithm (without information revelation). Our results indicate signi<sup>fi</sup>cant improvement in costs can be achieved by applying our method with acceptable CPU time.

Although we concentrate on combinatorial reverse auction, the solution method proposed in this paper can be applied to regular auctions in which there are multiple buyers bidding for a set of goods offered by one seller. The WDP of combinatorial auctions is similar to the winner determination problem (WDP) of combinatorial reverse auctions. By changing the objective function to maximize the revenue, changing sellers to buyers and changing buyer to seller in the WDP of combinatorial reverse auctions, we can formulate the WDP of combinatorial auctions. Lagrangian relaxation approach can also be applied to solve the WDP of combinatorial auctions by following a procedure similar to the one proposed in this paper.

## Acknowledgement

This paper is supported in part by National Science Council of Taiwan, R.O.C. under grant NSC97-2410-H-324-017-MY3.

## References

[1] G. Adomavicius, A. Gupta, Toward comprehensive real-time bidder support in iterative combinatorial auctions, Information Systems Research 16 (2005) 169–185.

[2] A. Andersson, M. Tenhunen, F. Ygge, Integer programming for combinatorial auction winner determination. Proceedings of the Seventeenth National Conference on Arti<sup>fi</sup>cial Intelligence, 2000, pp 39–46.

[3] Sven de Vries, R.V. Vohra, Combinatorial auctions: a survey, INFORMS, Journal on Computing 3 (2003) 284–309.

[4] Don Perugini, Dale Lambert, Leon Sterling, Adrian Pearce, From Single Static to Multiple Dynamic Combinatorial Auctions, Intelligent Agent Technology, IEEE WIC/ACM International Conference on 19–22 Sept, 2005, pp. 443–446

[5] Y. Fujishima, K. Leyton-Brown, Y. Shoham, Taming the computational complexity of combinatorial auctions: Optimal and approximate approaches. In Sixteenth International Joint Conference on Arti<sup>fi</sup>cial Intelligence, 1999, pp. 548–553.

[6] J. Gallien, L.M. Wein, A smart market for industrial procurement with capacity constraints, Management Science 51 (2005) 76–91.

[7] R. Gonen, D. Lehmann, Optimal solutions for multi-unit combinatorial auctions: branch and bound heuristics, The Proceedings of the Second ACM Conference on Electronic Commerce (EC'00), 2000, pp. 13–20.

[8] Y. Guo, A. Lim, B. Rodrigues, J. Tang, Using a Lagrangian heuristic for a combinatorial auction problem, Proceedings of the 17th IEEE International Conference on Tools with Arti<sup>fi</sup>cial Intelligence, 2005, pp. 103–107.

[9] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, J.R. Kalaganam, H.S. Lee, C. An, Combinatorial and quantity-discount procurement auctions bene<sup>fi</sup>t Mars, Incorporated and its suppliers, Interfaces 33 (2003) 23–35.

[10] H.H. Hoos, Craig Boutilier, Solving combinatorial auctions using stochastic local search. Proceedings of the Seventeenth National Conference on Arti<sup>fi</sup>cial Intelligence, 2000, pp. 22–29.

[11] Fu-Shiung Hsieh, Combinatorial auction with minimal resource requirements Lecture Notes in Arti<sup>fi</sup>cial Intelligence 4570 (2007) 1072–1077.

[12] Hsieh, Fu-Shiung, Shih-Min Tsai, Combinatorial Reverse Auction based on Lagrangian Relaxation, Proceedings of 2008 IEEE Asia-Paci<sup>fi</sup>c Services Computing Conference, 2008, pp. 329–334.

[13] J.L. Jones, G.J. Koehler, Combinatorial auctions using rule-based bids, Decision Support Systems 34 (2002) 59–74.

[14] A.M. Kwasnica, J.O. Ledyard, D. Porter, C. DeMartini, A new and improved design for multiobjective iterative auctions, Management Science 51 (2005) 419–434.

[15] R. Leskelä, Jeffrey Teich, Hannele Wallenius, Jyrki Wallenius , Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2007) 420–434.

[16] L. Meeus, Karolien Verhaegen, Ronnie Belmans, Block order restrictions in combinatorial electric energy auctions, European Journal of Operational Research 196 (3) (2009) 1202–1206.

[17] T. Metty, R. Harlan, Q. Samelson, T. Moore, T. Morris, R. Sorensen, A. Schneur, O. Raskina, R. Schneur, J. Kanner, K. Potts, J. Robbins, Reinventing the supplier negotiation process at Motorola, Interfaces 35 (2005) 7–23.

[18] J.D. Murray, R.W. White, Economies of scale and economies of scope in multiproduct <sup>fi</sup>nancial institutions: a study of British Columbia Credit Unions, The Journal of Finance 38 (1983) 887–902.

[19] A. Pekeč, M.H. Rothkopf, Combinatorial auction design, Management Science 49 (2003) 1485–1503.

[20] B.T. Polyak, Minimization of unsmooth functionals, USSR Computational Math and Math. Physics 9 (1969) 14–29.

[21] M. Rothkopf, A. Pekeč, R. Harstad, Computationally manageable combinational auctions, Management Science 44 (1998) 1131–1147.

[22] T. Sandholm, Approaches to winner determination in combinatorial auctions, Decision Support Systems 28 (2000) 165–176.

[23] T. Sandholm, Algorithm for optimal winner determination in combinatorial auctions, Arti<sup>fi</sup>cial Intelligence 135 (1–2) (2002) 1–54.

[24] R.R. Vemuganti, Applications of Set Covering, Set Packing and Set Partitioning Models: A Survey, in: D.-Z. Du (Ed.), Handbook of Combinatorial Optimization, vol 1, Kluwer Academic Publishers, Netherlands, 1998, pp. 573–746.

[25] M. Xia, Jan Stallaert, Andrew B. Whinston, Solving the combinatorial double auction problem, European Journal of Operational Research 164 (2005) 239–251.

[26] S. Yanga, Segrea Alberto Maria, Codenottib Bruno, An optimal multiprocessor combinatorial auction solver, Computers & Operations Research 36 (2007) 149–166.

Fu-Shiung Hsieh received his B.S. and M.S. degrees in control engineering from the National Chiao-Tung University, Taiwan, Republic of China in 1987 and 1989, respectively. He received his Ph.D. degree from the National Taiwan University in 1994. He served as a researcher in Industrial Technology Research Institute (ITRI), Taiwan, from 1994 to 1999. He was an Assistant Professor and Associate Professor with The Overseas Chinese Institute of Technology (OCIT) from 1999 to July 2004 and August 2004 to July 2005, respectively. He was the Director of the International Electronic Commerce Center of OCIT from August 2001 to July 2002. Since August 2005, he has been with Chaoyang University of Technology, where he is currently an Associate Professor at the Department of Computer Science and Information Engineering. He has over <sup>fi</sup>fty publications, including international journal and conference papers. He is listed in Who's Who in the World 2006, 2007, and 2009 and Who's Who in Asia 2007. His research interests are in electronic commerce, work<sup>fl</sup>ows, multi-agent systems and manufacturing systems.
