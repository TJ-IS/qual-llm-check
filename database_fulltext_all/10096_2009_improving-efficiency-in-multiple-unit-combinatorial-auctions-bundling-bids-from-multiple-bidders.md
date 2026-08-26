---
otero_id: 10096
otero_key: "4UYJVK5W"
title: "Improving efficiency in multiple-unit combinatorial auctions: Bundling bids from multiple bidders"
authors: "Murat Köksalan; Riikka-Leena Leskelä; Hannele Wallenius; Jyrki Wallenius"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.07.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving ef<sup>fi</sup>ciency in multiple-unit combinatorial auctions: Bundling bids from multiple bidders

Murat Köksalan <sup>a</sup>, Riikka-Leena Leskelä <sup>b,</sup>⁎, Hannele Wallenius <sup>b</sup>, Jyrki Wallenius <sup>c</sup>

<sup>a</sup> Middle-East Technical University, Dept. of Industrial Engineering, 06531, Ankara, Turkey

<sup>b</sup> Helsinki University of Technology, Dept. of Industrial Engineering and Management, P.O. Box 5500, 02015 TKK, Finland

<sup>c</sup> Helsinki School of Economics, P.O. Box 1210, 00101 Helsinki, Finland

## a r t i c l e i n f o

Article history: Received 27 May 2008 Received in revised form 25 February 2009 Accepted 7 July 2009 Available online 14 July 2009

Keywords: Auctions/bidding Iterative combinatorial auctions Decision support systems Multiple units

## a b s t r a c t

In multiple-unit combinatorial auctions both bidders and bid takers can bene<sup>fi</sup>t from support mechanisms that suggest new bids for the bidders. We present a support tool called Group Support Mechanism, which suggests bundles of bids to several bidders not among the provisional winners. It improves upon the Quantity Support Mechanism we developed earlier. The ef<sup>fi</sup>ciency of the <sup>fi</sup>nal allocation is better when the Group Support Mechanism is used instead of the Quantity Support Mechanism, especially in cases when the ef<sup>fi</sup>cient allocation consists of three or more bids.

© 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

Combinatorial auctions are pricing mechanisms in which a bundle of different goods or services (items) is sold/bought in one auction. Bids are vectors $( q _ { 1 } , \dots , q _ { K } , p )$ , where q indicates the quantity of item i (in singleunit auctions the inclusion of item i in the bid), and p the price for the bundle. The bids are assumed indivisible. Combinatorial auctions are best suited for selling/buying items that are complements or substitutes. When the items are substitutes, the bidder only wants one of the items (not more). When items are complements, the value of the whole bundle is larger than the sum of the values of its components separately. In reverse auctions, complementarities translate into economies of scope in the sellers’ production process. Allowing combinatorial bidding allows the bidders to fully express their synergies, and thereby avoid the exposure problem. The exposure problem occurs when items with synergies are sold in separate auctions. In such cases, the value of one item depends on the combination of items the bidder wins. However, the bidders have to bid on single items without knowing what other items they will win. Thus, theycan end up with a combination they did not want, or pay too much for the items they do get. Also the auction owner bene<sup>fi</sup>ts, as bidders can offer lower prices in reverse auctions, and conversely higher prices in forward auctions. Thus, combinatorial auctions provide a viable market mechanism, for example, for business-to-business (B2B) transactions.

Combinatorial auctions are becoming increasingly popular. The possibility of complementarities is recognized by many companies and organizations holding auctions and tenders. For example, the procurement of trucking services is well suited for a combinatorial auction [16,30]. A trucking company can offer a much lower price for transporting a truck load from point A to point B, if it can make sure that the truck is full also on the return trip. Combinatorial auctions have been used in the auctioning of bus routes [2], as well as in the general procurement processes of several multinational companies, such as Mars, Motorola and Procter & Gamble [10,18,28]. In the beginning of 2008, in the USA, the Federal Communications Commission (FCC) allowed combinatorial bidding in Auction #73 of the 700 MHz band. Combinatorial bidding was allowed in one license block containing 12 licenses [6]. However, the allowed combinations were restricted to three packages: “50 states” (licenses 1–8), “Atlantic” (licenses 10 and 12) and “Paci<sup>fi</sup>c” (licenses 9 and 11). At the end of the auction, only the bid on the “Paci<sup>fi</sup>c” package was among the winners; all other licenses were sold individually [7].

Combinatorial auctions are computationally too complex to be held without the support of computers. The Winner Determination Problem (WDP) is NP-complete [25], which means that as the size of the auction grows, the time required to solve the WDP increases beyond practical limits. In many cases the practical applications of auctions are quite large. E.g. the procurement auctions at Motorola [18] may include thousands of items with different quantity and delivery considerations. A big part of the combinatorial auction literature is devoted to computational issues. One branch of research focuses on developing more ef<sup>fi</sup>cient algorithms [26,29], whereas other researchers have developed heuristics [19,12] or studied situations in which the computational manageability can be guaranteed [21,25].

It is not only the solving of the WDP that becomes dif<sup>fi</sup>cult in combinatorial auctions. Also, the task of placing bids becomes dif<sup>fi</sup>cult. The dif<sup>fi</sup>culties in bidding are of two types: 1) the dif<sup>fi</sup>culty of expressing preferences over the items, and 2) the dif<sup>fi</sup>culty in bidding due to the fact that whenever the winning allocation consists of at least two bids, the winning bids always complement each other. These dif<sup>fi</sup>culties open up opportunities for developing support mechanisms to help alleviate them. Expressing preferences over items resembles closely the problem of expressing preferences over multiple attributes, which has been studied quite extensively within the <sup>fi</sup>eld of multiple criteria decision making. Preference elicitation in combinatorial auctions in particular has been directly addressed by several authors (e.g. [4,9,11,27]).

The problems arising from the fact that winning bids complement each other, however, have not been broadly addressed in literature. This phenomenon, which we call the “puzzle problem”, is related to the threshold problem, which is commonly identi<sup>fi</sup>ed as a problem in combinatorial auctions (see, for example, [24]). The threshold problem refers to the situation in which a number of “local” bidders interested in only a fraction of the whole bundle need to improve upon their bid prices together in order to beat the “global” bidder (who has a provisionally winning bid on the whole combination). This price coordination is dif<sup>fi</sup>cult, because it should be done without communication, as communication is usually forbidden to prevent collusion — hence the threshold problem. However, in general, in combinatorial auctions it is not enough to only coordinate the bid prices. Successful bids need to complement each other also with respect to the item combinations, and the number of units of each item. We call this broader problem of placing complementing bids the “puzzle problem”. In a sense, a combinatorial auction resembles a puzzle: the missing piece has to be of a certain form in order to complete the puzzle and a bid has to contain the right quantities of the right items to complete the bundle. The puzzle problem is not tied to the speci<sup>fi</sup>c setting of global vs. local bidders, but recognizes the existence of what we call “glocal” bidders (bidders who bid for any size of package between single items and the whole demand). The issues related to the puzzle problem have not been raised in literature.

Many auctions use a sealed-bid format, which means that the bids placed in the auction are known only to the bid taker (the buyer in reverse auctions). It is impossible for bidders to place complementing bids to team up with other bids – to <sup>fi</sup>nd the missing piece to the puzzle – if they are unaware of previous bids placed by other bidders. Many procurement auctions and government tenders are sealed-bid auctions, so this concern about teaming-up is justi<sup>fi</sup>ed. The puzzle problem is accentuated in the multiple-unit case, where the bidders need to decide item quantities in addition to choosing the combination of items. It can easily happen that a bidder with a low cost structure loses, because she did not bid for the “right” combination or right quantities. Some iterative combinatorial auction mechanisms offer price vectors that incoming bids must beat (see for example [13,14,23,32]). However, price information only helps choose which items to bid on, and it does not help with choosing the quantities of each item. The bene<sup>fi</sup>ts of quantity support in multiple-unit combinatorial auctions have been neglected in literature.

## 2. Providing quantity support for bidders

Leskelä et al. [15] and Ervasti and Leskelä [5] discuss a bidder support tool called the Quantity Support Mechanism (QSM) for iterative combinatorial auctions. The QSM is presented in a reverse auction setting, but it is applicable to forward auctions as well. The core of the QSM, the quantity support problem (QSP) is designed to solve for a price-quantity combination that would become a provisional winner<sup>1</sup> in the auction, and would also be pro<sup>fi</sup>table for the bidder (although the bidders’ cost functions are unknown). In other words, the QSM helps the bidders overcome the puzzle problem through solving for the missing piece in the puzzle.

The formulation of the QSP as presented in [5,15] is the following. Consider K items and assume that the demand of the buyer is $d _ { k }$ $( k = 1 , \ldots , K )$ units of each of the K items. There are N bidders in the auction, and bidder i has placed $n _ { i }$ bids. Now each bid j by bidder i is a (K+1)-dimensional vector: $( q _ { i j 1 } , q _ { i j 2 } , \dots , q _ { i j K } , p _ { i j } )$ , where $0 \leq q _ { i j k } \leq d _ { k }$ are quantities of item k and $p _ { i j } { \ge } 0$ is the price of the bundle. In other words, bidder I's jth bid is an offer to deliver $q _ { i j k }$ units of each item k for a total price of $p _ { i j } .$ . The QSP for bidder m takes the form of a mixed integer programming problem $\left( \mathsf { Q S P } _ { m } \right)$ . The objective $\left( \operatorname { E q . } \left( 1 \right) \right)$ is to maximize the pro<sup>fi</sup>t of bidder m by solving for the new price p<sub>m,new</sub>, the vector $Q _ { m , n e w }$ of item quantities $q _ { m , n e w , k }$ and the values for the bid status variables $x _ { i j } .$ The total cost to the buyer is required to decrease by a predetermined decrement δ as a result of the new bid (Eq. (2)), and the demand for each item must be ful<sup>fi</sup>lled (Eq. (3)). The item quantities q should not exceed the bidder's corresponding capacities $a _ { m k } \left( \mathrm { E q . ~ } ( 6 ) \right)$ ). It is also assumed that at most one bid per bidder can be active at a time to simplify the bidding language. The formulation is thus:

$$
(\mathrm{QSP} _ {m}) \colon m a x p _ {m, n e w} - \tilde {c} _ {m} \Big (Q _ {m, n e w} \Big)\tag{1}
$$

$$
s. t. \quad \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j} + p _ {m, n e w} \leq C ^ {*} - \delta\tag{2}
$$

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} + q _ {m, n e w, k} \geq d _ {k} \quad \forall k = 1,..., K\tag{3}
$$

$$
x _ {m j} = 0 \quad \forall j = 1, \dots , n _ {m}\tag{4}
$$

$$
\sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \quad \forall i = 1, \dots , N\tag{5}
$$

$$
\begin{array}{l l} q _ {m, \text { new }, k} \leq a _ {m k} & \forall   k = 1,..., K \\ x _ {i j} \in \{0, 1 \} & \forall   i, j \\ p _ {m, \text { new }}, q _ {m, \text { new }, k} \geq 0 \forall   k = 1,..., K \end{array}\tag{6}
$$

where $\tilde { c } _ { m } ( Q _ { m , \mathrm { n e w } } ) \mathrm { i }$ is the cost function of bidder $m , x _ { i j } { ' } s$ indicate which existing bids are among the provisional winners, and $C ^ { * }$ is the current lowest cost to the buyer (which is required to decrease by δ each round).

Leskelä et al. [15] use the dual prices of the linear relaxation of the WDP as proxies for the cost coef<sup>fi</sup>cients in a linear approximation of the cost function, which would take the form

$$
\tilde {c} _ {m} \left(Q _ {m, \text {new}}\right) = \sum_ {k = 1} ^ {K} \mu_ {k} q _ {m, \text {new}, k},\tag{7}
$$

where $\mu _ { k } { ' } s$ are the dual prices of the corresponding demand constraints. The dual prices corresponding to each demand constraint can be interpreted as market prices for the items [14]. The corresponding integer program of the WDP does not have dual prices when the linear programming relaxation has a solution with nonintegral values. However, the dual prices of the linearized program (which are easily obtainable) may be suf<sup>fi</sup>cient for the QSM.

Leskelä et al. [15] conclude that the QSM manages to <sup>fi</sup>nd pro<sup>fi</sup>table bid suggestions quite well. However, when studying the <sup>fi</sup>nal allocations of simulated auctions, Ervasti and Leskelä [5] discovered that the QSM does not necessarily help to reach an ef<sup>fi</sup>cient allocation. The ef<sup>fi</sup>cient allocation is de<sup>fi</sup>ned as the allocation that minimizes the sum of the bidders' production cost for the bundle of items. Depending on the design, the average production cost of the <sup>fi</sup>nal allocations could be as much as 5% higher than the production cost of the ef<sup>fi</sup>cient allocation. Especially, the larger the number of bids in the ef<sup>fi</sup>cient allocation, the less likely it was that the ef<sup>fi</sup>cient allocation was found. Ervasti and Leskelä [5] identify an extended puzzle problem: it is not enough to solve for the shape of the last missing bid, but rather a larger number of missing bids, if one wants to reach the ef<sup>fi</sup>cient allocation.

Allocative ef<sup>fi</sup>ciency is a desirable property of an auction mechanism. It means that the winners of the auction value the items the most, or, in the reverse setting, have the lowest production costs. Due to the dif<sup>fi</sup>culties in formulating bids, allocative ef<sup>fi</sup>ciency is more dif<sup>fi</sup>cult to reach in combinatorial auctions than in single-item auctions. The Vickrey–Clark–Groves (VCG) mechanism developed by [3,8,31] guarantees allocative ef<sup>fi</sup>ciency [17], but requires that the bidders announce their valuations for every conceivable combination. When the number of items increases – especially in multiple-unit auctions – the number of combinations grows very quickly too large to be manageable. Iterative auction mechanisms alleviate this problem, as the bidders can choose to place only a few bids at a time, and then place more bids later. The problems of expressing preferences over bundle items and placing complementing bids still remain, though.

Our argument is that bidders and bid takers could bene<sup>fi</sup>t from a decision support tool that helps form bids that complement existing bids. Such a tool would be especially useful for the local bidders trying to outbid the global bidder. The tool would be equally bene<sup>fi</sup>cial for “glocal” bidders. The global bidders do not bene<sup>fi</sup>t from quantity support, as they only want the whole bundle, but they can use price support, which is a special case of quantity support with <sup>fi</sup>xed quantities.

Providing support is also in the interest of the bid taker, because if bidding is simpler, the auction may attract more participants resulting in more competition, and improve the allocative ef<sup>fi</sup>ciency of the auction. Particularly, we are interested in improving on the ideas presented in [5] and [15], and design a support mechanism that would guide the auction to the ef<sup>fi</sup>cient allocation — or at least close to it. Our approach is to extend the QSM to suggest bundles of bids for multiple bidders simultaneously, where the bundled bids would become active together. Following the example of [5] and [15], we focus on continuous, iterative combinatorial auctions, and present our ideas in the reverse auction setting. Continuous, iterative auctions seem to be the most popular ones in practice (see [10,18]), and hence it makes sense to focus on this particular auction type.

The following section presents the extension of the QSM, the Group Support Mechanism (GSM). In the third section we present an example of the GSM. The fourth section concludes.

## 3. The group support mechanism

The dif<sup>fi</sup>culties the Quantity Support Mechanism of Leskelä et al. [15] experiences in <sup>fi</sup>nding the ef<sup>fi</sup>cient allocation are mostly due to the fact that the formulation of the QSP only looks for one optimal incoming bid to complement the existing bids. Because of this, the suggested bids are to a large extent determined by the existing bids. It also implies that the QSM most likely will not suggest bids from the ef<sup>fi</sup>cient allocation, unless the complementing bids are already in the bid stream; this was apparent in the simulation results of Ervasti and Leskelä [5]. This is a fundamental problem inherent in the formulation. Also, the QSM does not remove the threshold problem the local bidders face, since by de<sup>fi</sup>nition, the threshold problem arises when more than one bidder is required to improve upon her bid in order for them to beat the global bidder. Thus, we are proposing a different way of providing quantity support, which would directly address the problem of the “single incoming bid”.

Our idea is a Group Support Mechanism (GSM) that would suggest a combination of bids that either together satisfy the entire demand, or team up with one or more of the existing bids in the bid stream, and become active as a group. This should improve the ef<sup>fi</sup>ciency of the <sup>fi</sup>nal allocation, because the GSM also chooses how many new bids it suggests, and is therefore not as dependent on the existing bids as the QSM. The QSM is in a way a special case of the GSM, because the GSM will also support only a single bidder when <sup>fi</sup>nding it the optimal course of action. However, the GSM is free to suggest any number of incoming bids at a time, and the added <sup>fl</sup>exibility should result in more ef<sup>fi</sup>cient outcomes than the QSM.

The formulation of the GSM is related to the formulation of the QSM presented in Leskelä et al. [15], and the main idea of suggesting bids that would maximize the bidders’ pro<sup>fi</sup>ts is retained. This principle is important for practical applications, and hence we wanted to retain it. Firms are worried about auctions undermining their longterm supplier relationships if the suppliers feel unfairly treated (see e.g. [10,18]). However, there are signi<sup>fi</sup>cant differences in the formulations as well. The GSM maximizes the combined pro<sup>fi</sup>t of the provisional winners, that is, the pro<sup>fi</sup>ts of the new bids and existing bids to be included in the provisionally winning combination. The QSM maximized only the pro<sup>fi</sup>t of the single incoming bid. The inclusion of the pro<sup>fi</sup>t of existing bids in the GSM may appear somewhat counterintuitive, because the purpose of the QSM is to serve the incoming bidders and <sup>fi</sup>nd new, pro<sup>fi</sup>table bids for them. However, not including the pro<sup>fi</sup>t of the existing bids would create a bias towards <sup>fi</sup>lling the set of provisional winners with new bids. The existing bids would not be teamed-up with, even if they were good matches.

Another signi<sup>fi</sup>cant difference in the formulations of the GSM and QSM is the approximation of the bidders’ cost functions. The QSM uses the same linear cost function estimate for all bidders, and thereby the bid suggestions of QSM are anonymous (i.e. it gives the same suggested bids regardless of the bidder). However, it does not make sense for the GSM to be anonymous. If each bidder did not have a unique approximation of the cost function, the optimization algorithm would assign the bid suggestions randomly to some bidders, and it would pool the quantities into one large bid or few large bids (as allowed by the capacity constraints). Also, it is quite realistic to assume that bidders differ from each other. We hold on to the assumption that bidders do not want to disclose any cost information, and thus the only information we have on the bidders’ costs is information from the bidders' bids in the bid stream. We use the bid information to customize the cost function approximations for each bidder.

## 3.1. Group support problem

The core of the GSM is an optimization problem similar to the QSP in many ways. We use similar notation as in the formulation of the QSP: there are K items, $d _ { k } \left( k = 1 , \ldots , K \right)$ units of each item requested by the buyer, N bidders, and n bids from each bidder i. At any point in time the bidders can be divided into two sets: active bidders, who are among the provisional winners, and inactive bidders who are not. Let I denote the set of inactive bidders. The GSM solves for a combination of new bids for the inactive bidders which, as a group (and possibly together with some of the existing bids in the bid stream), become active. The objective is to maximize the combined (approximated) pro<sup>fi</sup>t of all the bidders by choosing the statuses of the old bids (x ), and the quantities $\left( q _ { i , \mathrm { n e w } , k } \right)$ and prices $\left( p _ { i , \mathrm { n e w } } \right)$ in the new bids (i.e. sum of new pro<sup>fi</sup>ts e ) suggested for the inactive bidders (Eq. (8)). The constraints (9), (10), (14), (15) and (16) are the same as in the QSP. Because the new bids in the combination suggested by the GSM will become active only if all the bids are accepted by the bidders, combinations in which one bidder makes a big pro<sup>fi</sup>t and another bidder makes a loss (which may happen since the GSP is only maximizing the sum of pro<sup>fi</sup>ts) are not desirable. However, we acknowledge that the pro<sup>fi</sup>ts we use in the formulations are approximations, and if we require that all pro<sup>fi</sup>ts be at least zero, we might not get a feasible solution even if one existed (that is, if we have overestimated the bidders' costs). Thus, we allow losses, but add a penalty for losses into the objective function and formulate corresponding constraints (11). Constraints (12) and (13) ensure that a price in a new bid can be positive only if at least one item assumes a positive value and that the status variable for the new bid, $x _ { i , \mathrm { n e w } } = 1$ , when the bid is not empty. The formulation is the following:

$$
(G S P): \max - \sum_ {i \in I} S _ {i} + \varepsilon \left(\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} \left(p _ {i j} - \tilde {c} _ {i} \left(Q _ {i j}\right) x _ {i j}\right) + \varepsilon \left(\sum_ {i \in I} e _ {i}\right) \right.\tag{8}
$$

$$
s. t. \quad \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} p _ {i j} x _ {i j} + \sum_ {i \in I} p _ {i, \text { new }} \leq (1 - \delta) C ^ {*}\tag{9}
$$

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} q _ {i j k} x _ {i j} + \sum_ {i \in I} q _ {i, \mathrm{new}, k} \geq d _ {k} \forall k = 1,..., K\tag{10}
$$

$$
p _ {i, \text { new }} - \tilde {c} _ {i} \left(Q _ {i, \text { new }}\right) - e _ {i} + s _ {i} = 0 \forall i \in I\tag{11}
$$

$$
\sum_ {k = 1} ^ {K} q _ {i, \text { new }, k} - x _ {i, \text { new }} \geq 0 \forall i \in I\tag{12}
$$

$$
M x _ {i, \text { new }} - p _ {i, \text { new }} \geq 0 \forall i \in I q\tag{13}
$$

$$
\sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \forall i \notin I\tag{14}
$$

$$
\sum_ {j = 1} ^ {n _ {i}} x _ {i j} + x _ {i, \text { new }} \leq 1 \forall i \in I\tag{15}
$$

$$
q _ {i, \text { new }, k} \leq a _ {i k} k = 1,..., K, \forall i \in I\tag{16}
$$

$$
x _ {i j}, x _ {i, \text { new }} \in \{0, 1 \} \forall i, j
$$

$$
s _ {i}, e _ {i}, p _ {i, \text { new }}, q _ {i, \text { new }, k} \geq 0
$$

where $C ^ { * }$ is the current lowest total cost to the buyer, d the percentage by which the total cost is required to decrease, $\tilde { c } _ { i } ( Q _ { i , \mathrm { n e w } } )$ the approximated cost for bidder i from producing the suggested set of item quantities $Q _ { i , \mathrm { n e w } } , \ s _ { i }$ is the approximated loss and $e _ { i }$ the approximated pro<sup>fi</sup>t in bidder i’s suggested new bid. The bidders' capacities are denoted by $a _ { i k } .$ . M is a positive constant larger than any conceivable bid price, and ε is a very small positive constant. Allowing for different capacities recognizes the fact that companies of various sizes may participate in the auction. Naturally, other constraints can easily be added to the problem, for example, limitations on the number of suppliers or volumes per supplier, which were important for Mars Inc. [10]. The addition of ε in the objective function implies that the primary objective is to avoid losses and pro<sup>fi</sup>t maximization is secondary. Essentially, the GSP chooses the most pro<sup>fi</sup>table combination of bids from combinations that do not result in losses for any bidder, if possible. If losses cannot be avoided, they will still be minimized.

## 3.2. Approximating cost functions

A crucial element of the QSM is the approximation of bidders' cost functions $\tilde { c } _ { i } ( Q _ { i } )$ . The better we can approximate them, the more accurate are the bid suggestions. First of all, we need to choose the form of the function. We would like the bidders' cost functions to exhibit economies of scope, which complicates matters somewhat. A conceptually simple function that exhibits economies of scope for bidder i is of the form $\tilde { c } _ { i } ( q _ { i j 1 } , q _ { i j 2 } ) = F _ { i , 1 2 } + c _ { i 1 } q _ { i j 1 } + c _ { i 2 } q _ { i j 2 }$ consisting of a <sup>fi</sup>xed cost element for combination L, $F _ { i , L } ,$ , and per-unit costs $c _ { i k } ,$ where $F _ { i , 1 2 } { < } F _ { i , 1 } + F _ { i , 2 } \left[ 2 0 \right]$ . The downside of this functional form is that the number of parameters to be estimated increases exponentially with the number of items. In the case of K items, the number of <sup>fi</sup>xed cost parameters is $2 ^ { K } - 1$ (and the number of variable cost parameters is K). However, as a starting point we will use this functional form and test its performance.

To approximate the bidders' cost functions we design an inverse optimization problem (in the spirit of [1]; see also [33]), which utilizes the information we get in the form of bids in the bid stream. We assume that bidders do not place bids in which costs exceed the price. Thus, the task of the inverse optimization problem is to <sup>fi</sup>nd a set of cost function parameters, which are consistent with a bidder's bidding behavior. The constraints formulated from the bidder's bids (18) form the feasible set. The objective function then determines which ones of the feasible cost parameters are chosen. Especially in the beginning of the auction when there are only few bids from each bidder, the feasible set is large and relatively unconstrained. For example, the <sup>fi</sup>xed cost parameters corresponding to combinations that have not been bid on can be chosen quite freely. The only things constraining them are the assumption of economies of scope (Eq. (22)), and the assumption that producing additional items can never lower total <sup>fi</sup>xed cost (Eq. (21)). To constrain the feasible set a little more, we assume that upper and lower limits for all the cost parameters can be derived for any particular industry (Eqs. (19) and (20)). However, these limits still leave a vast range of feasible options to choose from. Therefore, the choice of the objective function to a large extent determines the values for the cost parameters. Thus, the question becomes how to choose the objective function.

The use of any objective function will lead the Cost Estimate Problem (CEP) to choose one of the points in the feasible set. Without any further information on the bidders' cost functions besides the constraints that make up the feasible set, we have no way of knowing, which point would be better than some other point. In other words, it is impossible to say which objective function would provide a good approximation. Thus, we have designed a following iterative scheme to approximate the bidders' cost function parameters and to narrow down the feasible set as the auction progresses.

First, lower and upper bound estimates for the cost function parameters are set. At the beginning of the auction the bounds coincide with “industry estimates”, or in our experiments, the ranges of the distributions. The objective is simply to maximize the sum of the cost function parameters (Eq. (17)), which will drive all the parameters to their upper bounds in the absence of any bid information to provide contradicting evidence. This may naturally be an over estimate of the cost functions, but it will not prohibit the GSP from <sup>fi</sup>nding bid suggestions, since losses are allowed in the formulation. Thus, we can still suggest the bids to the bidders even though the cost function approximations suggest that the bids would result in losses, and it is possible that the bidders will actually <sup>fi</sup>nd them pro<sup>fi</sup>table. This has the added bene<sup>fi</sup>t that now we get contradicting information and can update the estimates for the cost function parameters. The updated estimates are then set as the new upper bounds for the parameters, and the auction continues. If we started from a lower bound estimate for the cost parameters, and the GSP suggests bids in which all the estimated pro<sup>fi</sup>ts are positive, the acceptance of the bids is expected and would not give us any new information on the cost function parameters (the old estimates are still consistent with the new evidence). Naturally, in this case, if the bidders declined the bid suggestions we would get new information. However, it is desirable that the bidders accept the bid suggestions because that way the auction progresses. In order to maximize the information obtained from new bids and to speed up the auction process it makes more sense to start from the upper bound estimates.

The general formulation of the CEP for bidder i would be

$$
(\text { CEP }): \max \sum_ {L \subseteq \Gamma} F _ {i L} + \sum_ {k = 1} ^ {K} c _ {i k}\tag{17}
$$

$$
s. t. p _ {i j} - \tilde {c} _ {i} (Q _ {i j}) \geq \varepsilon \quad \forall j = 1, \dots , n _ {i}\tag{18}
$$

$$
l _ {i L} \leq F _ {i L} \leq u _ {i L} \quad \forall L \subseteq \Gamma\tag{19}
$$

$$
l _ {i k} \leq c _ {i k} \leq u _ {i k} \quad \forall k = 1, \dots , K\tag{20}
$$

$$
F _ {i L ^ {\prime}} \leq F _ {i L} \quad \forall L ^ {\prime} \subset L, \forall L \subseteq \Gamma\tag{21}
$$

$$
F _ {i L} \leq \sum_ {L _ {t} \in P a r [ L ]} F _ {i L _ {t}} \quad \forall L \subset \Gamma\tag{22}
$$

where ε is a small positive scalar, Γ is the set of all possible item combinations, and $L , L ^ { \prime }$ are subsets of Γ, Par[L] refers to all possible partitions of L, and $L _ { t }$ is an element of Par[L]. A partition of set L is the group of disjoint sets, which together form L. The set of constraints (22) only states that the sum of the <sup>fi</sup>xed costs of all subsets forming any item combination L should exceed the <sup>fi</sup>xed cost $F _ { L }$ due to economies of scope between items.

It is worth noting that the GSP will not offer bid suggestions to all inactive bidders unless there is room for everybody in the set of provisional winners, which is more unlikely the more there are participants in the auction. Thus, some bidders are not suggested a bid by the GSP, and without any bid information the cost function estimate would not be lowered, which decreases the probability that the bidder would be offered a bid suggestion the next time. Some bidders could get stuck in this loop, and never be suggested anything. We could consider adding a constraint requiring that the bidder requesting support would be guaranteed a bid suggestion (not to upset the bidder), but so far we have not added any such constraints. Instead, recognizing that the estimates are above the true parameters, we decided to decrease the estimates by 1% for each bidder who is not suggested anything to improve their chances to receive a suggestion in the next round. We chose the decrement to be 1% in order to make only small adjustments in the estimates. Increasing the decrement could reduce the number of iterations needed to get the GSM to suggest a bid for the bidder, but a smaller decrement allows us to get closer to the true estimates. If, in the next round, the bidder receives a bid suggestion and accepts it, the upper bounds are replaced by the 1% lower estimates. If it turns out that the new estimate was too optimistic (the GSM offers a bid it thinks is pro<sup>fi</sup>table, but the bidder declines), we solve the cost function estimation problem again with the rejected bid added to the constraints, and receive an updated estimate of the parameters.

## 4. An example

In this example auction there are three items, 600 units of each item demanded by the buyer, and 10 bidders. Three items are enough to demonstrate the complexities of the auction, and typically used in literature to illustrate combinatorial auction mechanisms (see e.g. [13,22]). The number of bidders is usually less than 10 in auction examples and even in more rigorous simulation studies. The number of items demanded by the bidder is not important as long as it is more than one, but the ratio of the demand to bidders' capacities matters. All bidders are assumed to be “glocal” meaning that they have production capacity for all three items but they are willing to settle for any item and unit combination as long as it is pro<sup>fi</sup>table. The bidders are assigned capacities, and cost functions. The capacities of each bidder are chosen randomly as 150, 225 or 300 for each item. The capacity levels were chosen to be such that, given the demand, at least two bidders would always be among the winners. Assigning speci<sup>fi</sup>c cost functions allows for the evaluation of the pro<sup>fi</sup>tability of the bid suggestions, and for the solution of the ef<sup>fi</sup>cient allocation, against which the auction outcome can be evaluated. The cost functions are designed to exhibit economies of scope, and they are of the form presented in Section 3.2. The parameters are chosen randomly from uniform distributions, but for the sake of simplicity no difference is made between the items: variable costs $c _ { i k }$ vary from [53.3, 66.7], <sup>fi</sup>xed costs $F _ { i L }$ for single items from [1777.8, 2222.2], for pairs of items from [2666.7, 3333.3], and for combinations of three items from [3555.6, 4444.4].

Because the GSM cannot be used unless there is already a feasible solution to the WDP (and thereby a total cost to the buyer), we assume that at the beginning each bidder places one bid. The bidders place a bid on the combination for which their <sup>fi</sup>xed cost is lowest with respect to the expected value of the cost. The item quantities are set at the upper bounds of the capacity constraints. The WDP is then solved for the initial bid stream. Approximate solutions of the WDP are not accepted, because the set of winning bidders could be different, which would cause fairness issues. The initial bid stream is reproduced in Table 1.

The next step is to estimate the cost functions of the bidders. The CEP is unique for each bidder. However, the constraints resulting from the economies of scope assumption are the same for each bidder. Also initially, the upper and lower bounds for the parameters (which are set to be the upper and lower bounds of the uniform distributions from which the bidders' true cost function parameters were drawn) are identical to the bidders. The objective function, which was chosen to be the sum of the parameters, is the same across bidders. For example, for bidder B1 the CEP assumes the following form:

$$
\begin{array}{l l} \text {max} & F _ {1} + F _ {2} + F _ {3} + F _ {1 2} + F _ {1 3} + F _ {2 3} + F _ {1 2 3} + c _ {1} + c _ {2} + c _ {3} \\ \text {s.t.} \end{array}
$$

$$
2 7 1 9 9 - F _ {2 3} - 2 2 5 c _ {2} - 1 5 0 c _ {3} \geq \varepsilon
$$

$$
1 7 7 7. 8 \leq F _ {i} \leq 2 2 2 2. 2 \quad i = 1, 2, 3
$$

$$
2 6 6 6. 7 \leq F _ {1 j} \leq 3 3 3 3. 3 \quad j = 2, 3
$$

$$
2 6 6 6. 7 \leq F _ {2 3} ^ {\prime} \leq 3 3 3 3. 3
$$

$$
3 5 5 5. 6 \leq F _ {1 2 3} \leq 4 4 4 4. 4
$$

$$
5 3. 3 \leq c _ {i} \leq 6 6. 7 \quad \forall i = 1, \dots , 3\tag{23}
$$

$$
F _ {1 2} \geq F _ {1}, F _ {1 2} \geq F _ {2}
$$

$$
F _ {1 3} \geq F _ {1}, F _ {1 3} \geq F _ {3}
$$

$$
F _ {2 3} \geq F _ {2}, F _ {2 3} \geq F _ {3}
$$

$$
F _ {1 2 3} ^ {2 3} \geq F _ {1 2}, F _ {1 2 3} \geq F _ {1 3}, F _ {1 2 3} \geq F _ {2 3}
$$

$$
\begin{array}{l} F _ {1} + F _ {2} \geq F _ {1 2}, F _ {1} + F _ {3} \geq F _ {1 3}, F _ {2} + F _ {3} \geq F _ {2 3} \\ F _ {1 2} + F _ {3} \geq F _ {1 2 3}, F _ {1 3} + F _ {2} \geq F _ {1 2 3}, F _ {2 3} + F _ {1} \geq F _ {1 2 3} \end{array}
$$

where ε is a small positive constant. For the sake of simplifying the notation, the index for the bidder has been left out. Once the CEP has been solved for each bidder, we have the following initial estimates for the cost function parameters (Table 2):

Table 1  
The initial bids and provisional winners.

<table><tr><td>Bid</td><td>Item 1</td><td>Item 2</td><td>Item 3</td><td>Price (€)</td><td>Status $^{a}$ </td></tr><tr><td> $x_{11}$ </td><td>0</td><td>225</td><td>150</td><td>27,199</td><td>0</td></tr><tr><td> $x_{21}$ </td><td>150</td><td>0</td><td>150</td><td>22,954</td><td>1</td></tr><tr><td> $x_{31}$ </td><td>225</td><td>225</td><td>150</td><td>45,990</td><td>0</td></tr><tr><td> $x_{41}$ </td><td>0</td><td>225</td><td>0</td><td>17,613</td><td>0</td></tr><tr><td> $x_{51}$ </td><td>0</td><td>225</td><td>150</td><td>25,594</td><td>0</td></tr><tr><td> $x_{61}$ </td><td>225</td><td>150</td><td>300</td><td>49,356</td><td>0</td></tr><tr><td> $x_{71}$ </td><td>300</td><td>0</td><td>0</td><td>22,007</td><td>0</td></tr><tr><td> $x_{81}$ </td><td>0</td><td>225</td><td>225</td><td>33,210</td><td>1</td></tr><tr><td> $x_{91}$ </td><td>225</td><td>150</td><td>0</td><td>27,831</td><td>1</td></tr><tr><td> $x_{10,1}$ </td><td>225</td><td>225</td><td>225</td><td>50,076</td><td>1</td></tr></table>

<sup>a</sup> 1=active, 0=inactive; total cost to buyer=134,071€.

Table 3  
Table 2  
Initial cost function estimates.

<table><tr><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td> $F_i$ </td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td></tr><tr><td> $F_{ij}$ </td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td></tr><tr><td> $F_{123}$ </td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td></tr><tr><td> $c_1$ </td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.7</td><td>65.9</td><td>66.7</td><td>64.4</td><td>66.7</td></tr><tr><td> $c_2$ </td><td>61.6</td><td>66.7</td><td>66.7</td><td>66.7</td><td>54.5</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.7</td></tr><tr><td> $c_3$ </td><td>66.7</td><td>64.1</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.4</td><td>66.7</td><td>66.1</td><td>66.7</td><td>66.7</td></tr></table>

The auction is a continuous auction, that is, the WDP is solved after each incoming bid. However, since in the example bids only enter based on the suggestions of the GSM, it is easier to present the example “round by round”, in which one round continues as long as there is a change in the solution of the WDP (i.e., the set of active bidders changes).

## 4.1. Round 1

It is now time to use the GSM for the <sup>fi</sup>rst time. The decrement δ by which the total cost to the buyer is required to decrease from round to round is set at 2%. A larger δ could speed the convergence of the auction, but the larger the decrement the further away from the lowest possible total cost the auction can end. The cost function parameters in Table 2 are inserted in the cost function in the GSP presented in Section 3.1. However, because the cost function is discontinuous (the <sup>fi</sup>xed cost term depends on the combination of items in the bid), the formulation becomes somewhat more complex. A set of auxiliary variables $y _ { i , j k l }$ is de<sup>fi</sup>ned to construct constraints that guarantee that the correct <sup>fi</sup>xed cost is taken into consideration in the objective function $( y _ { i , j k l } = 1$ if the items in combination j,k and l all have a non-zero value, $y _ { i , j k l } = 0$ otherwise). Also, for the same reason we need to create new variables for the item quantities in the incoming bids: one variable per item per combination it is in. If there are K items in the auction, each item is in $2 ^ { K - 1 }$ combinations, so in this case each item is in four combinations.

The cost function c̃(Q) for bidder i takes the form

$$
\begin{array}{l} \tilde {c} _ {i} (Q _ {i, \text { new }}) = c _ {i, 1} \sum_ {s = 1} ^ {4} q _ {i, \text { new }, 1, s} + c _ {i, 2} \sum_ {s = 1} ^ {4} q _ {i, \text { new }, 2, s} + c _ {i, 3} \sum_ {s = 1} ^ {4} q _ {i, \text { new }, 3, s} \\ \quad + F _ {i, 1} y _ {i, 1} + F _ {i, 2} y _ {i, 2} + F _ {i, 3} y _ {i, 3} + F _ {i, 1 2} y _ {i, 1 2} + F _ {i, 1 3} y _ {i, 1 3} + F _ {i, 2 3} y _ {i, 2 3} \\ \quad + F _ {i, 1 2 3} y _ {i, 1 2 3} \end{array} \tag {24}\tag{24}
$$

To ensure that the correct <sup>fi</sup>xed cost is taken into consideration in the cost function and that at most one combination is chosen per bidder, the following constraints are added to the GSP for each inactive bidder i I.

$$
\begin{array}{l} M y _ {i, k} - q _ {i, \text {new}, k, 1} \geq 0 \quad k = 1, 2, 3 \\ M y _ {i, 1 2} - q _ {i, \text {new}, 1, 2} - q _ {i, \text {new}, 2, 2} \geq 0 \\ M y _ {i, 1 3} - q _ {i, \text {new}, 1, 3} - q _ {i, \text {new}, 3, 2} \geq 0 \\ M y _ {i, 2 3} - q _ {i, \text {new}, 2, 3} - q _ {i, \text {new}, 3 3} \geq 0 \\ M y _ {i, 1 2 3} - q _ {i, \text {new}, 1, 4} - q _ {i, \text {new}, 2, 4} - q _ {i, \text {new}, 3, 4} \geq 0 \\ y _ {i, 1} + y _ {i, 2} + y _ {i, 3} + y _ {i, 1 2} + y _ {i, 1 3} + y _ {i, 2 3} + y _ {i, 1 2 3} \leq 1 \\ y _ {i, 1}, y _ {i, 2}, y _ {i, 3}, y _ {i, 1 2}, y _ {i, 1 3}, y _ {i, 2 3}, y _ {i, 1 2 3} \in \{0, 1 \} \end{array}\tag{25}
$$

where M is a constant larger than any conceivable item quantity. In this example, M=1000 was used. Note that these constraints leave open the possibility that $y _ { i , j k l }$ assumes the value of one, even though one or more of the items in the combination are zero. For example, when items one and two assume a nonzero value for bidder i, either $y _ { i , 1 2 } = 1 \ \mathrm { o r } \ y _ { i , 1 2 3 } = 1$ . However, since the <sup>fi</sup>xed cost for a bundle including more items is always larger than for a bundle with less items, the objective function will ensure that the $y _ { i , j k l } ,$ , which coincides exactly with the combination of nonzero item quantities, assumes the value one.

Bids suggested by the GSM.

<table><tr><td>Bid</td><td>Item 1</td><td>Item 2</td><td>Item 3</td><td>Price (€)</td></tr><tr><td> $x_{1,new}$ </td><td>0</td><td>225</td><td>0</td><td>16,658</td></tr><tr><td> $x_{5,new}$ </td><td>75</td><td>225</td><td>0</td><td>21,426</td></tr><tr><td> $x_{7,new}$ </td><td>300</td><td>0</td><td>300</td><td>43,950</td></tr></table>

The bundle of bids suggested by the GSM in the <sup>fi</sup>rst round is presented in Table 3. There are always multiple solutions, because the pro<sup>fi</sup>t or loss in the bids (e or s ) can be divided in an in<sup>fi</sup>nite number of ways between the bidders who are offered a bid suggestion. We chose the solution where the estimated pro<sup>fi</sup>t/loss is divided equally among the bidders. Of course the true pro<sup>fi</sup>ts/losses of the bidders are not equal; we are dividing the pro<sup>fi</sup>t/loss calculated with the cost function estimates equally among the bidders. Another approach would be to divide the pro<sup>fi</sup>t proportionately to the size of the bid. The main effect that the choice of solution has in the auction, is that in some cases it can cause the bidder to accept or reject a bid suggestion. E.g. if our cost estimate is a bit too low, offering a bid suggestion in which the GSP thinks the bidder will just break even, will not be good enough for the bidder and she will reject. However, if some of the surplus in the auction is allocated to this bidder, it may increase the bid price high enough so that she will accept the bid suggestion. Because we assume we do not know the bidders' true costs, it is dif<sup>fi</sup>cult to know which cost estimates are underestimated, and which way of dividing the surplus would be best.

Thus, bidders B1, B5 and B7 are suggested a bid, and their bids would team up with bidder B6's initial bid (225, 150, 300, 49356). The bidders all accept the new suggestions, so the set of provisional winners is now B1, B5, B6 and B7, and the total cost to the buyer is reduced to 131,390 €.

## 4.2. Round 2

Next the cost functions are updated. The cost estimates for bidders B3 and B4, who were inactive but still not offered a new bid, are now lowered by 1%. The cost estimates of the active bidders remain the same. The accepted bids offer no new information on the bidders' cost functions, because the bid prices are high enough to cover current estimated costs. The reason for the decrease in B3's and B4's estimates is that it is possible that we have overestimated their cost and hence they were not offered a bid. B2, B8, B9 and B10 were active so they could not have received bid suggestions regardless of their cost function estimates, and thus nothing is done to the estimates of their cost functions.

The GSP with the updated cost information is solved for the new set of inactive bidders. The solution is presented in Table 4.

This time the GSP suggests bids to B4 and B8 to team up with the initial bids of B5 $( x _ { 5 1 } = 1 )$ and B7 $( x _ { 7 1 } = 1 )$ . The GSP thinks the bids will result in a loss of 474 € for both bidders. However, both bidders accept the suggested bids. The GSP has overestimated their costs, so the true cost of producing the proposed bundles is below the bid prices. Now we have new information on the costs of bidders B4 and B8, and their cost estimates are updated. The cost estimates for inactive bidders who did not receive a bid suggestion (B2, B3, B9 and B10) are lowered by 1%, and the estimates for bidders who previously were active (B1, B5, B6 and B7), out of which B5 and B7 are still active, remain untouched. The new cost function parameters are depicted in Table 5.

Table 4  
Bids suggested by the GSM in the second round.

<table><tr><td>Bid</td><td>Item 1</td><td>Item 2</td><td>Item 3</td><td>Price (€)</td></tr><tr><td> $x_{4,\text{new}}$ </td><td>300</td><td>225</td><td>225</td><td>53,426</td></tr><tr><td> $x_{8,\text{new}}$ </td><td>0</td><td>150</td><td>225</td><td>27,736</td></tr></table>

Table 5  
Cost function parameters after Round 2.

<table><tr><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td> $F_i$ </td><td>2222.2</td><td>2200.0</td><td>2178.0</td><td>2200.0</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2222.2</td><td>2200.0</td><td>2200.0</td></tr><tr><td> $F_{ij}$ </td><td>3333.3</td><td>3300.0</td><td>3267.0</td><td>3300.0</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3333.3</td><td>3300.0</td><td>3300.0</td></tr><tr><td> $F_{123}$ </td><td>4444.4</td><td>4400.0</td><td>4356.0</td><td>4400.0</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4444.4</td><td>4400.0</td><td>4400.0</td></tr><tr><td> $c_1$ </td><td>66.7</td><td>66.0</td><td>65.3</td><td>64.4</td><td>66.7</td><td>66.7</td><td>65.9</td><td>66.7</td><td>63.8</td><td>66.0</td></tr><tr><td> $c_2$ </td><td>61.6</td><td>66.0</td><td>65.3</td><td>66.0</td><td>54.5</td><td>66.7</td><td>66.7</td><td>66.7</td><td>66.0</td><td>66.0</td></tr><tr><td> $c_3$ </td><td>66.7</td><td>63.5</td><td>65.3</td><td>66.0</td><td>66.7</td><td>66.4</td><td>66.7</td><td>59.1</td><td>66.0</td><td>66.0</td></tr></table>

## 4.3. Round 3

First the GSP suggests a bid for bidder B10 only, and that bid (0, 150, 225, 25,160) is not acceptable to her. Also according to the estimated cost the bid is not pro<sup>fi</sup>table, and therefore we do not receive more information on B10's cost function. The cost estimates of all the other inactive bidders (B1, B2, B3, B6 and B9) are lowered by 1% and the GSP is solved again. This time the GSP suggests bids for bidders B1: (150, 225, 0, 26,139), B6: (225, 0, 300, 37,075) and B9: (225, 150, 150, 37,379), which would team up with bidder B5's initial bid resulting in a total cost to the buyer of 126,187 €. All the three bidders <sup>fi</sup>nd the suggestions pro<sup>fi</sup>table, even though the GSP again thinks the bids would result in losses. The cost estimates are updated for all bidders, except the ones who are active.

## 4.4. Round 4

The <sup>fi</sup>rst solution of the GSP provides only a suggestion for bidder B3 (225,150,150, 34,855), which is not accepted. Thereafter, the GSP is solved seven times, and each time at least one bidder who is suggested a bid declines the suggestion, vetoing the “group” bid. The accepted bids are added to the bid stream, but the total cost to the buyer does not decline by the required 2% because the complementary bid(s) was not accepted. After each GSP solution the cost functions are updated. Finally, the ninth iteration produces bid suggestions to bidders B4: (300, 0, 150, 30,515) and B7: (300, 150, 300, 50,897), which are both pro<sup>fi</sup>table for the bidders. After this round, the GSP does not <sup>fi</sup>nd bid combinations that would be pro<sup>fi</sup>table for all bidders. The auction ends. Going back to the bidders' cost functions we can conclude that the inactive bidders have such high costs that they could not afford to decrease the total cost to the buyer by the required 2%. The active bidders could have afforded $\mathrm { t o } ,$ but they did not have an incentive to do so, as they were already among the provisional winners. The <sup>fi</sup>nal bid stream and the winning bids are presented in Table 6.

Bid stream and solution of the WDP after Round 4.

<table><tr><td>Bid</td><td>Item 1</td><td>Item 2</td><td>Item 3</td><td>Price (€)</td><td>Status</td></tr><tr><td> $x_{11}$ </td><td>0</td><td>225</td><td>150</td><td>27,199</td><td>1</td></tr><tr><td> $x_{21}$ </td><td>150</td><td>0</td><td>150</td><td>22,954</td><td>0</td></tr><tr><td> $x_{31}$ </td><td>225</td><td>225</td><td>150</td><td>45,990</td><td>0</td></tr><tr><td> $x_{41}$ </td><td>0</td><td>225</td><td>0</td><td>17,613</td><td>0</td></tr><tr><td> $x_{51}$ </td><td>0</td><td>225</td><td>150</td><td>25,594</td><td>1</td></tr><tr><td> $x_{61}$ </td><td>225</td><td>150</td><td>300</td><td>49,356</td><td>0</td></tr><tr><td> $x_{71}$ </td><td>300</td><td>0</td><td>0</td><td>22,007</td><td>0</td></tr><tr><td> $x_{81}$ </td><td>0</td><td>225</td><td>225</td><td>33,210</td><td>0</td></tr><tr><td> $x_{91}$ </td><td>225</td><td>150</td><td>0</td><td>27,831</td><td>0</td></tr><tr><td> $x_{10,1}$ </td><td>225</td><td>225</td><td>225</td><td>50,076</td><td>0</td></tr><tr><td> $x_{12}$ </td><td>0</td><td>225</td><td>0</td><td>16,658</td><td>0</td></tr><tr><td> $x_{52}$ </td><td>75</td><td>225</td><td>0</td><td>21,426</td><td>0</td></tr><tr><td> $x_{72}$ </td><td>300</td><td>0</td><td>300</td><td>43,950</td><td>0</td></tr><tr><td> $x_{42}$ </td><td>300</td><td>225</td><td>225</td><td>53,426</td><td>0</td></tr><tr><td> $x_{82}$ </td><td>0</td><td>150</td><td>225</td><td>27,736</td><td>0</td></tr><tr><td> $x_{13}$ </td><td>150</td><td>225</td><td>0</td><td>26,139</td><td>0</td></tr><tr><td> $x_{62}$ </td><td>225</td><td>0</td><td>300</td><td>37,075</td><td>0</td></tr><tr><td> $x_{92}$ </td><td>225</td><td>150</td><td>150</td><td>37,379</td><td>0</td></tr><tr><td> $x_{43}$ </td><td>300</td><td>150</td><td>225</td><td>46,781</td><td>0</td></tr><tr><td> $x_{44}$ </td><td>300</td><td>225</td><td>225</td><td>50,969</td><td>0</td></tr><tr><td> $x_{73}$ </td><td>300</td><td>150</td><td>0</td><td>31,938</td><td>0</td></tr><tr><td> $x_{45}$ </td><td>300</td><td>0</td><td>0</td><td>19,666</td><td>1</td></tr><tr><td> $x_{74}$ </td><td>300</td><td>150</td><td>300</td><td>52,385</td><td>0</td></tr><tr><td> $x_{46}$ </td><td>300</td><td>150</td><td>0</td><td>30,561</td><td>0</td></tr><tr><td> $x_{10,2}$ </td><td>225</td><td>225</td><td>225</td><td>46,199</td><td>0</td></tr><tr><td> $x_{47}$ </td><td>300</td><td>0</td><td>0</td><td>19,778</td><td>0</td></tr><tr><td> $x_{48}$ </td><td>300</td><td>0</td><td>0</td><td>19,824</td><td>0</td></tr><tr><td> $x_{49}$ </td><td>300</td><td>0</td><td>150</td><td>30,515</td><td>0</td></tr><tr><td> $x_{75}$ </td><td>300</td><td>150</td><td>300</td><td>50,897</td><td>1</td></tr></table>

The total cost to the buyer is 123,356 €. In fact, the total cost decreased by more than 2%. The previously inactive bid $\boldsymbol { \chi } _ { 4 5 }$ made by B4 was more advantageous to the buyer now that a good match entered $\left( x _ { 7 5 } \right)$ the auction. The estimated pro<sup>fi</sup>t for bidder B4 was larger from the newest bid $\left( x _ { 4 9 } \right)$ and that is why the GSP favored that one (it looks at the auction from the bidders' perspective), but it is the WDP that determines the set of winners. In fact, the mark-up in bidder B4’s bid $x _ { 4 5 }$ is higher than in bid $x _ { 4 9 } .$ Hence, the bidder may be happier with this outcome.

## 4.5. Comparison with the efficient allocation

The ef<sup>fi</sup>cient allocation can be solved, because we know the bidders' cost functions. It is presented in Table 7.

Comparing the ef<sup>fi</sup>cient allocation with the actual auction outcome (in Table 6) it is evident that the auction came close to the ef<sup>fi</sup>cient allocation. All the bidders are the same, as are the items they bid on. The only differences are in two item quantities. If we compare the production costs of the ef<sup>fi</sup>cient allocation (113,666 €) and the winning allocation (114,057 €), the difference is small.

## 4.6. Comparison with the outcome of the QSM auction

The auction presented in the example above was also run through using the QSM to support the bidders instead of the GSM. All the auction parameters (demand, number of bidders, bidders' cost functions and initial bids) were kept the same, but instead of using the GSM, the inactive bidders used the QSM, and placed bids based on the bid suggestions made by the QSM. The <sup>fi</sup>nal allocation of the QSM auction is presented in Table 8.

The combined production cost of the winning bidders is 121,385€, which is 6.8% higher than the ef<sup>fi</sup>cient production cost, and 6.4% higher than the production cost of the winning allocation of the GSM auction. There are some bidders among the winners, who are not

## Table 7

The ef<sup>fi</sup>cient allocation of the auction.

<table><tr><td>Bidder</td><td>Item 1</td><td>Item 2</td><td>Item 3</td></tr><tr><td>B1</td><td>0</td><td>75</td><td>150</td></tr><tr><td>B4</td><td>300</td><td>0</td><td>0</td></tr><tr><td>B5</td><td>0</td><td>225</td><td>150</td></tr><tr><td>B7</td><td>300</td><td>300</td><td>300</td></tr></table>

Table 8  
The <sup>fi</sup>nal allocation of the auction with QSM.

<table><tr><td>Bidder</td><td>Item 1</td><td>Item 2</td><td>Item 3</td></tr><tr><td>B4</td><td>225</td><td>150</td><td>0</td></tr><tr><td>B5</td><td>0</td><td>150</td><td>150</td></tr><tr><td>B7</td><td>0</td><td>225</td><td>150</td></tr><tr><td>B8</td><td>150</td><td>0</td><td>150</td></tr><tr><td>B9</td><td>225</td><td>75</td><td>150</td></tr></table>

ef<sup>fi</sup>cient and should not be there (B8 and B9), and one ef<sup>fi</sup>cient bidder (B1) is not among the winners. Also, the number of winning bids in the <sup>fi</sup>nal allocation exceeds that of the ef<sup>fi</sup>cient allocation, which causes the bidders to incur unnecessary <sup>fi</sup>xed costs. The difference between the GSM and the QSM is very clear, even though the ef<sup>fi</sup>cient allocation consisted of only four bids. When the number of bids increases, we expect the difference in the ef<sup>fi</sup>ciency of the QSM auction and the GSM auction to increase.

## 5. Conclusions

As allocative ef<sup>fi</sup>ciency is a desirable property of any auction mechanism, we have studied ways to improve the ef<sup>fi</sup>ciency of the Quantity Support Mechanism of Leskelä et al. [15]. Based on the results of Ervasti and Leskelä [5], the original form of the QSM helps guide the auction to an ef<sup>fi</sup>cient allocation (or very close to it) only if the ef<sup>fi</sup>cient allocation consists of two bids. However, when the ef<sup>fi</sup>cient allocation consists of three or more bids, the QSM often fails to <sup>fi</sup>nd the ef<sup>fi</sup>cient bids.

We introduce an improved support tool called the Group Support Mechanism (GSM). It is based on the notion that a major handicap in the QSM is that it looks for only one new bid to enter the auction and to team up with the existing bids. Thus, the content of the new bid is highly dependent on the existing bids. And, if there are no good complements for the ef<sup>fi</sup>cient allocation bids in the bid stream, the QSM most likely will not suggest them. The GSM is based on a similar logic as the QSM: it suggests bids to bidders in order to maximize the bidders' pro<sup>fi</sup>ts while making the bidders provisional winners. The biggest difference is that instead of suggesting just one bid, the GSM suggests a bundle of bids for a set of inactive bidders. Suggesting a collection of bids diminishes the signi<sup>fi</sup>cance of the initial bid stream. However, it simultaneously increases the importance of the cost function estimates. The more information we have on the costs, i.e., the more bids there are from the bidders in the bid stream, the more accurate the estimate. Thus, we can expect the estimates to become more accurate as the auction progresses. Our example already indicated to this direction: for those bidders from whom we had more information (more accepted or rejected bid suggestions), the cost function parameter estimates changed more during the auction.

In a way, GSM can be considered as a generalization of the QSM. As a special case, the GSM will support a single bidder when it <sup>fi</sup>nds the optimal course of action, but it also provides the possibility of supporting any combination of bidders in each iteration. Hence, it has a substantially higher <sup>fl</sup>exibility to improve the allocations. The bene<sup>fi</sup>ts that can be obtained from this <sup>fl</sup>exibility are, naturally, expected to increase as the number of bids in the ef<sup>fi</sup>cient allocation increases. Also, the GSM alleviates the threshold problem and the extended puzzle problem, since it can offer bid suggestions to a group of “local” or “glocal” bidders to help them outbid a “global” bidder. Thus, the GSM should improve the allocative ef<sup>fi</sup>ciency of the <sup>fi</sup>nal allocation compared to the QSM in cases in which the ef<sup>fi</sup>cient allocation consists of three bids or more.

Further research involves the <sup>fi</sup>ne-tuning of the GSM and the Cost Estimation Problem (CEP), which is an important part of the GSM. One idea would be to <sup>fi</sup>nd a functional form for the cost function which has fewer parameters than the one we are currently using, but which would still be suf<sup>fi</sup>ciently accurate. Also, as the example presented in this paper demonstrates, the number of iterations per “round” increases as the auction nears the end and most bidders reject the bid suggestions made by the GSM. It would be worthwhile to improve the algorithm so that the number of iterations would be smaller. Also, currently the GSM suggests only one bundle of bids to a certain subset of the inactive bidders. Perhaps it would make sense to <sup>fi</sup>nd a way to compile several bundles to offer the bidders.

## Acknowledgments

The authors wish to thank the Emil Aaltonen Foundation (Finland) and the Academy of Finland (grant #121980) for <sup>fi</sup>nancial support. This study was initiated when the <sup>fi</sup>rst author was a visiting professor at Helsinki University of Technology.

## References

[1] D.R. Beil, L.M. Wein, An inverse-optimization-based auction mechanism to support multiattribute RFQs, Management Science 49 (2003) 1529–1545.

[2] E. Cantillon, M. Pesendorfer, Auctioning bus routes: the London experience, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, vol. 22, MIT Press, Cambridge, 2006.

[3] E.H. Clarke, Multipart pricing of public goods, Public Choice 11 (1971) 17–33.

[4] W. Conen, T. Sandholm, Minimal preference elicitation in combinatorial auctions Proceedings of the International Joint Conference on Arti<sup>fi</sup>cial Intelligence (IJCAI) Workshop on Economic Agents, Models, and Mechanisms, 2001, Seattle, Washington

[5] V. Ervasti and R.-L. Leskelä, Allocative Ef<sup>fi</sup>ciency in Simulated Combinatorial Auctions with Quantity Support, Unpublished manuscript, Helsinki University of Technology (2008).

[6] FCC, The Federal Communications Commission public notice DA-4171, http:// fjallfoss.fcc.gov/edocs\_public/attachmatch/DA-07-4171A1.pdf, accessed Oct. 17, 2007.

[7] FCC, The Federal Communications Commission public notice DA 08-595, Attachment A pp. 62-63. http://hraunfoss.fcc.gov/edocs\_public/attachmatch/DA-08-595A2.pdf, accessed Oct. 1, 2008.

[8] T. Groves, Incentives in teams, Econometrica 41 (1973) 617–631

[9] K. Hoffman, D. Menon, S. van den Heever, A bidder aid tool for dynamic package creation in the FCC spectrum auction, Working paper, Dept. of Systems Engineering and Operations Research, George Mason University, 2004.

[10] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, J.R. Kalaganam, H.S. Lee, C. An, Combinatorial and quantity-discount procurement auctions bene<sup>fi</sup>t mars, incorporated and its suppliers Interfaces 33 (2003) 23–35

[11] J.L. Jones, G.J. Koehler, Combinatorial auctions using rule-based bids, Decision Support Systems 34 (2002) 59–74.

[12] J.L. Jones, G.J. Koehler, A heuristic for winner determination in rule-based combinatorial auctions, INFORMS Journal on Computing 17 (2005) 475–489.

[13] A.M. Kwasnica, J.O. Ledyard, D. Porter, C. DeMartini, A new and improved design for multiobiective iterative auctions. Management Science 51 (2005) 419–434.

[14] R.H. Kwon, G. Anandalingam, L.H. Ungar, Iterative combinatorial auctions with bidder-determined combinations, Management Science 51 (3) (2005) 407–418.

[15] R.-L. Leskelä, J. Teich, H. Wallenius, J. Wallenius, Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2007) 420–434.

[16] J.O. Ledyard, M. Olson, D. Porter, J.A. Swanson, D.P. Torma, The <sup>fi</sup>rst use of a combined-value auction for transportation services, Interfaces 32 (5) (2002) 4–12.

[17] E. Maasland, S. Onderstal, Going, going, gone! A swift tour of auction theory and its applications, De Economist 154 (2006) 197–249.

[18] T. Metty, R. Harlan, Q. Samelson, T. Moore, T. Morris, R. Sorensen, A. Schneur, O. Raskina, R. Schneur, J. Kanner, K. Potts, J. Robbins, Reinventing the supplier negotiation process at Motorola, Interfaces 35 (2005) 7–23.

[19] M. Mito, S. Fujita, On heuristics for solving winner determination problem in combinatorial auctions, Journal of Heuristics 10 (2004) 507–523.

[20] J.C. Panzar, Technological determinants of <sup>fi</sup>rm and industry structure, in: R. Schmalensee, R.D. Willig (Eds.), Handbook of Industrial Organization, vol. I, North-Holland, 1989.

[21] S. Park, M. Rothkopf, Auctions with bidder-determined allowable combinations, European Journal of Operational Research 161 (2) (2005) 399–415.

[22] D.C. Parkes, iBundle: an ef<sup>fi</sup>cient ascending price bundle auction, Proceedings of First ACM Conference on Electronic Commerce (EC-99), 1999, pp. 148–157.

[23] D.C. Parkes, L.H. Ungar, Iterative combinatorial auctions: theory and practice, Proceedings of the 17th National Conference on Arti<sup>fi</sup>cial Intelligence (AAAI-00), 2000, pp. 74–81.

[24] A. Pekeč, M. Rothkopf, Combinatorial auction design, Management Science 49 (2003) 1485-1503

[25] M. Rothkopf, A. Pekeč, R. Harstad, Computationally manageable combinational auctions, Management Science 44 (1998) 1131–1147.

[26] T. Sandholm, Approaches to winner determination in combinatorial auctions, Decision Support Systems 28 (2000) 165–176.

[27] T. Sandholm, C. Boutlier, Preference elicitation in combinatorial auctions, in: P. Cramton Y Shoham R. Steinberg (Eds.) Combinatorial Auctions vol, 10 MIT Press, Cambridge, 2006.

[28] T. Sandholm, D. Levine, M. Concordia, P. Martyn, R. Hughes, J. Jacobs, D. Begg, Changing the game in strategic sourcing at Procter & Gamble: expressive competition enabled by optimization, Interfaces 36 (2006) 55–68.

[29] T. Sandholm, S. Suri, A. Gilpin, D. Levine, CABOB: a fast optimal algorithm for winner determination in combinatorial auctions, Management Science 51 (3) (2005) 374–390 special issue on Electronic Markets.

[30] Y. Shef<sup>fi</sup>, Combinatorial auctions in the procurement of transportation services, Interfaces 34 (2004) 245–252.

[31] W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, The Journal of Finance 16 (1) (1961) 8–37.

[32] P. Wurman, M. Wellman, AkBA: a progressive, anonymous-price combinatorial auction, Proceedings of Second ACM Conference on Electronic Commerce (EC-00), 2000, pp. 21–29, Minneapolis, Minnesota.

[33] S. Zionts, J. Wallenius, An interactive programming method for solving the multiple criteria problem, Management Science 22 (6) (1976) 652–663.

Riikka-Leena Leskelä is a PhD candidate at the Helsinki University of Technology. She received her M.Sc. (Tech) in 2004, and Lic.Sc (Tech) in 2007, both from Helsinki University of Technology. Her research interests are in the area of multiattribute and combinatorial auctions.

Hannele Wallenius holds a PhD from University of Jyväskylä, Finland. She has been faculty at the Helsinki University of Technology since 1995 where she is currently Professor of Industrial Economics and head of the Department of Industrial Engineering and Management. Her research has dealt with such diverse areas as Multiple Criteria Decision Making, public sector operations research, negotiation analysis and more recently electronic auctions and market mechanisms. Hannele Wallenius has spent numerous sabbaticals in the US, notably at Purdue University, Texas A&M University and Arizona State University. In addition, she has taught in the international programs of Helsinki School of Economics.

Jyrki Wallenius holds a PhD from the Helsinki School of Economics, where he is professor since 1990. He is serving as department head of the Department of Business Technology. His research encompasses Multiple Criteria Decision Making, negotiation analysis, decision support, behavioral decision making, and more recently electronic auctions and market mechanisms. Jyrki Wallenius has been a visiting professor at Purdue University, Texas A&M University and Arizona State University on several occasions. He is past editor of the European Journal of Operational Research and the President of the International Society of Multiple Criteria Decision Making. He is the recipient of numerous awards, both domestic and international.

Murat Köksalan is a professor in the Department of Industrial Engineering, Middle East Technical University. He has been a visiting professor at SUNY Buffalo, Purdue University, Helsinki University of Technology, and Helsinki School of Economics on various occasions. He is the recipient of the young researcher award of the Scienti<sup>fi</sup>c and Technological Research Council of Turkey and The MCDM Gold Medal of the International Society on Multiple Criteria Decision Making. He won the <sup>fi</sup>rst prize at the INFORMS Case Competition with various co-authors three times. His academic interests include multiple criteria decision making, combinatorial optimization, heuristic search, combinatorial auctions, and preparing teaching cases.
