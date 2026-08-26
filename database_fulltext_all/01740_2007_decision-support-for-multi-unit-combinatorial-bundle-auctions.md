---
otero_id: 1740
otero_key: "HSRVCKPZ"
title: "Decision support for multi-unit combinatorial bundle auctions"
authors: "Riikka-Leena Leskelä; Jeffrey Teich; Hannele Wallenius; Jyrki Wallenius"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.10.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Decision support for multi-unit combinatorial bundle auctions

Riikka-Leena Leskelä <sup>a,⁎</sup>, Jeffrey Teich <sup>b</sup>, Hannele Wallenius <sup>a</sup>, Jyrki Wallenius <sup>c</sup>

<sup>a</sup> Department of Industrial Engineering and Management, Helsinki University of Technology, POB 5500, 02015 HUT, Finland <sup>b</sup> Management Department, New Mexico State University, Las Cruces, NM 88003, USA <sup>c</sup> Helsinki School of Economics, POB 1210, 00101 Helsinki, Finland

Received 7 June 2005; received in revised form 23 August 2006; accepted 30 October 2006 Available online 26 December 2006

## Abstract

Single item auctions are by far the most common auction format, but they are not always efficient. Combinatorial auctions are beneficial, when complementarities exist between the items to be auctioned. There are, however, several problems with the implementation of combinatorial auctions. Firstly, they are computationally challenging. Secondly, in combinatorial auctions it is difficult for bidders to know what kind of bids to place, since the winning bids complement each other. We consider a progressive electronic procurement situation with a monopsonistic buyer. We propose a decision support tool for iterative e-auctions generating suggestions for bids that would be among the current winners of the auction. We have tested the mechanism and report on the results.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Combinatorial multi-item auctions; Decision support; e-auctions; Multi-attribute auctions; B2B E-procurement

## 1. Introduction

There are circumstances when it is not efficient to hold only single item auctions. Complementarities may exist between different items in both forward and reverse (procurement) auctions. Well-known examples are the auctioning of Federal Communications Commission's radio spectrum licenses, the sales of airport time slots, and allocation of delivery routes. Several studies indicate that using combinatorial auctions in firms' procurement processes can result in significant savings [11,21]. Combinatorial auctions can be beneficial even in the sales or procurement of furniture. De Vries and Vohra [7] illustrate such complementarities with a simple example, where a person wants to auction off a dining room set consisting of four chairs and a table. Given that the bidders are interested in the dining room set (which is a reasonable assumption), it is much better to auction the entire set rather than the individual pieces separately. In such a situation, a bidder desires to bid on a bundle of items. Allowing bids for bundles of items is the foundation of combinatorial auctions, which have attracted considerable attention in the auction literature. For a recent survey of combinatorial auctions, see [7] and [29]. Sheffi [33] demonstrates how issues related to the procurement of transportation services, a popular application of combinatorial auctions, can be incorporated into the combinatorial auction framework. Also see Xia, Koehler, and Whinston [39], who examine different combinatorial auction models and their relationships and properties.

Combinatorial auctions have been notoriously difficult to solve from a computational point of view. Rothkopf, Pekec and Harstad [30] discuss the computational complexity of solving different types of combinatorial (or rather combinational<sup>1</sup>) auctions. In fact much of the combinatorial auction literature, with ties to the set packing/knapsack problem in Operations Research (see, for example, [36]), has dealt with computational aspects and heuristics for solving what is known as the Winner Determination Problem of an auction [10,13,14,25,31]. Interesting recent research has focused on preference elicitation mechanisms for combinatorial auctions. For a review see Sandholm and Boutilier [32]. The purpose of the preference elicitation is to find out the bidders' valuation functions over various (all) possible bundles, in order to determine an optimal allocation. As acknowledged by Sandholm and Boutilier and others, this task is enormous in practice and several approaches have been proposed addressing this issue. A special case is ascending combinatorial auctions, where prices for different (all) bundles are posted asking bidders to reveal their demands at the respective prices (for example, Parkes [26], and Wurman and Wellman [38]). An interesting approach has been proposed by Conen and Sandholm [6], who ask bidders for limited, ideally relevant information to partially elicit the bidders' valuation functions — to determine an optimal allocation. Furthermore, we would like to mention the recent interest in optimal mechanism design issues in combinatorial auctions [18,28,29]. In general, some nice theoretical properties can be shown to hold, but one can question how realistic the underlying assumptions are (for example, requiring the bidders to announce their bids for each conceivable combination).

However, it is not only the solution of the Winner Determination Problem, the elicitation of the bidders preferences, or the actual mechanism design that becomes difficult in combinatorial auctions. Also, the task of placing bids becomes difficult. At least two kinds of problems arise. First of all, in combinatorial auctions, a successful bid complements existing bids, placing all of them among the winners (unless the winning bid is for the entire bundle). However, most procurement auctions use a sealed-bid format<sup>2</sup>, which means that the bids placed in the auction are known only to the bid taker. Thus it is impossible for bidders to place complementing bids, since they are unaware of previous bids placed by other bidders. It can easily happen that a bidder with a low cost structure loses, because she did not bid for the ‘right’ combination. Secondly, bids placed in combinatorial auctions are multidimensional vectors. When placing a bid on a set of commodities<sup>3</sup>, the bidder needs to know what the combination is worth to her. In reverse auctions this requires that the bidders have knowledge of their cost structure and of the complementarities and substitutabilities in production. In many cases such tradeoff information is not available; hence the task of selecting the combination to bid for and attaching a price to that combination can be difficult. The preference elicitation procedures try to help bidders attach appropriate prices to their bids. However, they do not help in finding complementary quantities.

In combinatorial auctions bidders could benefit from decision support tools that help them attach prices to bids and find bids that bring them among the winners of the auction and which are still profitable for them. However, if the bidders feel that the bidding process is too laborious and time-consuming, or that they do not understand how the bids are evaluated and winners chosen, they will choose not to participate in the auction. Providing support for the bidders is also in the interest of the bid taker, because it leads to a better result (i.e. a lower final price in a reverse auction) when more bidders participate in the auction and they are able to place ‘efficient’ bids. Fortunately, the Internet enables the use of such computerized decision support tools.

In the literature there are only a few publications that discuss decision support in auctions, and combinatorial auctions in particular. Adomavicius and Gupta [1] and Kwasnica, Ledyard, Porter and DeMartini [19], Hohner et al. [11] and Gallien and Wein [9] are some exceptions. Adomavicius and Gupta present several metrics that bidders can use to evaluate the current auction situation and the potential of each bid being among the winners. They assume that bidders do not often even know the status of their own bids, and therefore cannot know whether to improve upon their bids or not. Kwasnica et al. take bidder support a little further. They provide the bidders with a vector of prices (one for each commodity) that new bids must beat in order to be accepted. Gallien and Wein [9] present a system and the underlying theory for an optimization-based multi-item auction mechanism that relies on the solution of a linear program minimizing the buyer's cost under the suppliers (known) capacity constraints. They assist suppliers in finding a winning bid price. The underlying assumption is that the suppliers are willing to disclose their cost functions to a supposedly neutral third party auction organizer. Hohner et al. [11] in a very interesting paper provide feedback to nonwinning bidders regarding clearing prices, at which supply for each item equals demand. Despite the four cited papers, we feel that the decision support aspect of combinatorial auctions has been neglected, opening up interesting research questions.

In this paper we develop a support tool that helps bidders decide what kind of bids (price–quantity combinations) to place in a progressive multi-unit combinatorial reverse auction. The future goal is to extend our single item multi-attribute progressive hybrid negotiation and E-procurement system (NegotiAuction: see [34,35]) to combinatorial (bundle) auctions. Naturally, the extension will allow auction owners to hold multi-item auctions even if there are no synergies between the items, or if only some of the bidders have synergies. Our decision support tool is generic and can be integrated to NegotiAuction and other auction systems as well. It is not a stand-alone complete auction mechanism. We will address important issues related to mechanism design at the end of this paper. This will be done in the context of NegotiAuction.

In our discussions with procurement managers, it has become evident that this extension is important from a practical point of view. NegotiAuction already has a bidder support tool called ‘suggested price’, which gives the bidder the best price that will make her bid active (i.e. among the current winners of the auction) for a given quantity. For a complete description of the original NegotiAuction system we refer to [34] and [35].<sup>4</sup> We extend the ‘suggested price’ tool to a multiitem (combinatorial) setting. However, we feel that giving such price support is not enough in combinatorial auctions. In order to use the suggested price tool, the bidder has to know the quantities for all items for which she wants to place a bid. In combinatorial auctions it is possible that two bids complement each other making a winning combination, but either bid alone might not be among the winners. Hence, bidders would need some kind of quantity support to be able to find the combinations that ‘team-up’ with existing bids. This paper presents and tests a quantity support tool designed to aid bidders in combinatorial auctions.

This paper is organized as follows. The next section presents the relevant mathematical formulations in combinatorial auctions. The third section provides an example of a combinatorial reverse auction. The fourth section describes the experiment design used to test the quantity support mechanism. The fifth section presents the main results of the tests, and the sixth section discusses implementation issues. The last section concludes the paper and indicates some areas for further research.

## 2. Mathematical formulations

Bids entering the auction are recorded to the bid stream. In a combinatorial auction it makes sense to keep all the inactive bids in the bid stream as well, because the concept of outbidding a bid is not straightforward anymore. It is possible that an inactive bid can become active again, if an entering bid teams up with it. An exception is dominated bids, which are deleted from the bid stream. However, the concept of a dominated bid in combinatorial auctions is not trivial. In our auction, where only one bid per bidder can be active, a bid with the same quantities, but with a higher price than the same bidder's latter bid, is clearly dominated: it cannot become active anymore. However, if two bidders have identical bids otherwise, but one bid has a higher price than the other, it is not necessarily the case that the one with the higher price could never become active. It can, but only if the other bid (with the ‘better’ price) is also among the winners. It is very rare that something like this would happen, but it is not impossible. Thus, a bid becomes dominated only when there are so many identical bids with better prices that they can fulfill the whole demand.

For simplicity, we formulate the combinatorial auction as a price-only auction. However, multiple attributes can be taken into consideration through ‘pricing out’ (see [16] for theory and [34] for the application to auctions). When the non-price attributes are ‘priced out’, the last element of the bid vector depicts the normalized ‘working’ price rather than the actual monetary price of the bundle. Thus, the following formulations can be extended to multi-attribute settings in a straightforward manner.

## 2.1. Winner Determination Problem

We consider K items and assume that $d _ { k } \left( k { =                    } 1 , \ldots , K \right)$ units (nonnegative integers) of each of K items are requested by the buyer, defining demand. Now each bid j by bidder i is a $( K + 1 )$ -dimensional vector: $( q _ { i j 1 } , q _ { i j 2 } , \dots ,$ $q _ { i j K } , ~ p _ { i j } )$ , where $0 \leq q _ { i j k } \leq d _ { k }$ are nonnegative integers (quantities of item k) and $p _ { i j }$ (price of the bundle) is also a real positive number. In other words, bidder $i ^ { \circ } \mathrm { s } j \mathrm { t h }$ bid is an offer to deliver (in a reverse auction) $q _ { i j k }$ units of each item k for a total price of $p _ { i j } .$

The Winner Determination Problem (WDP) determining the status of each bid by each bidder at any given moment in the auction is formulated as an Integer Programming problem as follows:

$$
\begin{array}{l l} \min & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j} \\ \text { s.t. } & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} \geq d _ {k} \quad \forall k = 1, \dots , K \\ & \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \quad \forall i = 1, \dots , N \\ & x _ {i j} \in \{0, 1 \} \end{array}\tag{1}
$$

The variable $x _ { i j }$ indicates whether bidder $i ^ { \circ } \mathrm { s } j \mathrm { t h }$ bid is active $( x _ { i j } = 1 )$ or inactive $( x _ { i j } = 0 ) , n _ { i }$ is the number of bids placed by bidder i, where $i = 1 , \ldots , N .$ The auction owner can choose to add other constraints (so called side constraints) as well (e.g. that no more than half of the items can be bought from one seller), but they have been left out from the formulation.

The above problem may not have a feasible solution. Some of the quantity constraints or other constraints may be violated. A reservation price can also be incorporated in the formulation, and it is possible that the reservation price is not met. In such situations, the bidders could be informed, which constraints (and by how much) are violated, and encouraged to submit additional bids. Alternatively, the buyer, based on the solution of the above problem, may decide to relax some of the constraints. Otherwise the auction does not have a solution.

## 2.2. Calculating ‘suggested price’ for a new bid

In an iterative auction we seek to decrease total cost to buyer from the current round (denoted C\*) to the next. In the beginning of the auction when there are no bids, the buyer's reservation price can be used instead of total cost. We acknowledge that the concept of a reservation price is complex. First of all, it is not easy to define a reservation price for a combinatorial auction. Another issue is whether it is optimal to announce the reservation price truthfully. Also, the reservation price could change as more information about bidders' cost structures is obtained during the auction. However, in most cases it is not acceptable to change the announced reservation price during an auction. Thereby, the dynamic nature of the reservation price can much better be taken into consideration in one-on-one negotiations, where the reservation prices are usually kept a secret. Thus, if the buyer cannot or does not want to indicate a reservation price, the suggested price will become available only after the first bid has been entered.

Assume that bidder s (who can be an old or a new bidder) wants to use the suggested price tool. To obtain the ‘suggested price’ $p$ for a new bid $[ s _ { 1 } , s _ { 2 } , \ldots , s _ { K } ]$ to make it active, formulate the following optimization problem:

$$
\begin{array}{l l} \text { max } & \frac {p}{N} \\ \text { s.t. } & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j} + p <   C ^ {*} \\ & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} + s _ {k} \geq d _ {k} \forall k = 1, \dots , K \\ & x _ {s j} = 0 \quad \forall j = 1, \dots , n _ {s} \\ & \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \quad \forall i = 1, \dots , N \\ & x _ {i j} \in \{0, 1 \} \end{array}\tag{2}
$$

where $x _ { i j } \in \{ 0 , 1 \}$ and $p$ are treated as variables and $p _ { i j }$ are known (old) bid prices for bundles (again incorporating the ‘priced $\mathrm { o u t } ^ { \star }$ attributes in the case of a multiattribute auction). The above problem cannot be solved directly, since its first constraint contains an open set. There are, however, several ways this problem could be circumvented. (This does not guarantee that the problem has a feasible solution.) One simple and common way is to ask the buyer in the beginning of an auction to specify a desired δ bid decrement $( \delta > 0 )$ in total cost $C ^ { ^ { * } }$ from one iteration (bid) to the next, and formulate the first constraint as follows:

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j} + p \leq C ^ {*} - \delta\tag{3}
$$

Obviously the size of δ is important. There is evidence [2,3] that it may very well affect total cost to buyer in addition to the speed of convergence of an auction. Choosing an appropriate $\delta$ can be a difficult optimization problem. In fact, the size of $\delta$ does not necessarily have to be fixed for the duration of an entire auction. It might be a decreasing function of the number of submitted bids or a percentage of the price. With the help of experimentation, some useful guidelines for the size of an appropriate δ may be determined.

Interestingly, it may be worthwhile for bidders to submit bids whose price exceeds the ‘suggested price’. Such bids will not be active immediately, but it is possible that they become active when new bids enter the system. This is also a reason, why we would like to keep old (inactive) bids in the bid stream, unless bidders specifically tell us not to. Some of them may become active in the future. This problem is referred to as the threshold problem in the combinatorial auction literature [29,30].

## 2.3. Providing ‘quantity decision support’ to bidders

The starting point for the above discussion on ‘suggested price’ has been the assumption that the bidder fixes the quantity vector and requests the best price that would make her bid active. However, the bidders would often benefit from decision support regarding what quantities to bid. We are assuming that bidders are not informed of the bids in the bid stream. The question is then how to find such bid quantities that could ‘team-up’ with inactive and active bids in the bid stream in the ‘best’ possible way. If we knew the bidder's cost function and she would be willing to disclose it (to the auction owner or, if it could be arranged, to a neutral third party), the problem would reduce to a standard optimization problem<sup>5</sup>. The quantity support problem for bidder s would be formulated as a profit maximization problem as follows:

max $p - C _ { s } ( Q _ { 1 } , \dots , Q _ { k } )$

$$
\begin{array}{l l} \text { s.t. } & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} p _ {i j} + p \leq C ^ {*} - \delta \\ & \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {n _ {i}} x _ {i j} q _ {i j k} + Q _ {k} \geq d _ {k} \quad \forall k = 1, \dots , K \\ & x _ {s j} = 0 \forall j = 1, \dots , n _ {s} \\ & \sum_ {j = 1} ^ {n _ {i}} x _ {i j} \leq 1 \forall i = 1, \dots , N \\ & Q _ {k} \leq c _ {s k} \quad \forall k = 1, \dots , K \\ & x _ {i j} \in \{0, 1 \} \end{array}\tag{4}
$$

where $C _ { s } ( . )$ represents the bidder's cost function, $Q _ { k }$ the suggested quantity for item k in the new bid, and $c _ { s k }$ the (optional) capacity constraint upper bound<sup>6</sup> for item k expressed by bidder s.

We believe that it is not very likely that the bidders would be able to express their costs in a functional form. It is also unlikely that they would be willing to disclose their cost functions to the auction owner or even a neutral third party, even if they could specify the costs. The quantity support tool can be designed so that it enables the bidder to insert a cost function, allowing us to use the formulation in Eq. (4), but for the time being we are assuming that the bidder has not disclosed cost information. Hence, we need to resort to other ideas. We briefly summarize our thoughts.

We present three alternative suggestions for the formulation of the quantity support tool. The first two are very simple; the third is a bit more sophisticated. First, the bidder could be asked to give bid quantities and the system would then explore partial (percentage) quantities. This way the ratio of the quantities of different items in the bundle would remain the same. A good reference for situations in which partial quantities are appropriate is [8]. Exploring partial quantities, however, is only marginally better than merely using ‘suggested price’. A more interesting approach would be to fix all quantities but one and then play with it. This would allow for changes in the quantity ratios between items. This approach, however, is very tedious, especially, if the number of items is large, and somewhat rigid as it allows for only one change at a time.

The most interesting idea is to generate a shortlist of item bid vectors that ‘team-up’ with active and inactive bids. This is done by solving the bidder's profit maximization problem presented in Eq. (4) using a proxy to estimate the underlying unknown true cost function(s). The proxy used in this study is the vector of the dual prices associated with the quantity constraints of the linear relaxation of the WDP. The dual prices can be interpreted as market prices for the items [7]. Because in the Integer Programming case there are no dual prices, we use the dual prices of the equivalent linear problem. It is possible that the linear approximation of the cost function is poor and that the quantity support does not give acceptable suggestions to the bidders. Therefore a shortlist of alternative solutions is generated. This is done by going through the neighboring pivots of the original quantity support problem. Pivoting in the integer case is interpreted as forcing each status variable with a zero value to assume the value ‘one’ in turn. Hence, the number of pivots depends on the number of bids in the bid stream (as there is one status variable for each bid), and the number of bids in the optimal combination (those have already assumed the value ‘one’).

The quantity support tool formulated in this manner is very easy to use. The cost function $C _ { s } ( . )$ in Eq. (4) is replaced with the linear cost function

$$
C _ {s} (Q _ {1}, \dots , Q _ {K}) = \sum_ {k = 1} ^ {K} \mu_ {k} Q _ {k},\tag{5}
$$

where $\mu _ { k }$ is the dual price of the kth quantity constraint in the linear relaxation of the WDP (Eq. (1)). According to economic theory, firms have two kinds of costs: variable and fixed. We have considered only the variable costs in our linear approximation. A fixed cost term could easily be added, but as it is a constant, it would not affect the solution of the maximization problem. The lack of the fixed cost element affects the value of the objective function, but in this problem the approximated profit indicated by the objective function is not interesting — only the allocation and bundle price are.

The use of the tool does not require any prior input from the bidder, and our problem returns the same solution (shortlist) independent of the bidder. The bidder is asked to choose among the shortlist solutions (if any).

## 3. An example of a combinatorial reverse auction

Consider a procurement situation, where a single buyer desires to buy a bundle of items: 100 units of item A, 100 units of item B, and 200 units of item C. Her reservation price for the entire package is \$100,000. All prices are assumed to be ‘working prices’, i.e. all other attributes have been ‘priced out’. Let us further assume that there are three bidders: X, Y, and Z. Finally, assume that the desired price decrement $\delta$ is equal to \$3000 from one bid to the next.

Assume bidder X makes her first bid of 50 units of item A and 100 units of item B (but no units of C) for a total bid price of \$25,000. In vector notation, this bid is (50; 100; 0; \$25,000). Naturally, since this was the first and only bid so far, it is inactive, but it is entered into the bid stream. Next, assume that bidder Y enters the following bid (100; 50; 200; \$79,000). The bidder is informed that her bid does not become active. Considered jointly with the inactive bid of bidder X, they would meet the quantity demand of the buyer. In fact they would exceed the demand for items A and B, since bid $X _ { 1 } \cdot$ + bid $Y _ { 1 } = ( 1 5 0 ; 1 5 0 ; 2 0 0 ; \mathbb { { S 1 0 4 } } , 0 0 0 )$ . That would be acceptable, except that the buyer's reservation price (\$100,000) is exceeded, making the combination of bid $X _ { 1 }$ and $Y _ { 1 }$ not feasible. However, as previously, we retain bid $Y _ { 1 }$ in the database. Next, bidder Z enters the following bid (100; 100; 0, \$32,000). This bid is also inactive. Bidder Z is informed. The other two earlier bids remain in the database with inactive status.

Assume that bidder X wants to know what bundle price p would make her bid (50; 100; 0; p) active (as a full lot bid). We formulate and solve the following Integer Programming problem:

$$
\begin{array}{l l} \text { max } & p \\ \text { s.t. } & 7 9, 0 0 0 y _ {1} + 3 2, 0 0 0 z _ {1} + p \leq 1 0 0, 0 0 0 \\ & 5 0 x _ {1} + 1 0 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 1 0 0 x _ {1} + 5 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 2 0 0 y _ {1} \geq 2 0 0 \\ & x _ {1} = 1 \\ & y _ {1}, z _ {1} \in \{0, 1 \} \end{array}\tag{6}
$$

In other words, we seek to find the highest possible bid price for this new bid so that the reservation price is met. The previously inactive bids by Z and Y are included in the formulation.

The solution of the above problem is $y _ { 1 } = 1 , z _ { 1 } = 0$ max $p { = } 2 1 , 0 0 0$ (and of course $x _ { 1 } = 1 )$ . In other words, were X to accept this ‘suggested price’ for her bid, it would make her and $\mathrm { Y } { \mathrm { } } { \mathrm { } } { \mathrm { } } { \mathrm { } } \mathrm { s }$ previous bid active, but $Z \mathrm { { ' } s }$ bid would still be inactive. Assume that the ‘suggested price’ is good enough for bidder X, so she accepts it and bidder Y is informed about her changed status. Note that the new bid $X _ { 2 }$ contains the same quantities but for a lower price. Thus we can drop $X _ { 1 }$ from the bid stream because each bidder can have only one bid active simultaneously.

Now bidder Z wants to find a ‘suggested price $\dot { } p$ that would make her bid (100; 100; 0; $p )$ active. The formulation of the problem is as follows:

$$
\begin{array}{l l} \text { max } & p \\ \text { s.t. } & 7 9, 0 0 0 y _ {1} + 2 1, 0 0 0 z _ {2} + p \leq 9 7, 0 0 0 \\ & 5 0 x _ {2} + 1 0 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 1 0 0 x _ {2} + 5 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 2 0 0 y _ {1} \geq 2 0 0 \\ & z _ {1} = 1 \\ & x _ {2}, y _ {1} \in \{0, 1 \} \end{array}\tag{7}
$$

Note that we require that the total cost to the buyer declines by the bid decrement (\$3000). The ‘suggested price’ is \$18,000, which we assume is too low for bidder $Z ,$ so she declines the bid. Instead, she decides to use the quantity support tool to find an active bid.

First, in order to obtain the dual prices for the quantity constraints, we formulate and solve the LP relaxation of the WDP:

$$
\begin{array}{l l} \min & 2 1, 0 0 0 x _ {2} + 7 9, 0 0 0 y _ {1} + 3 2, 0 0 0 z _ {1} \\ \text {s.t.} & 5 0 x _ {2} + 1 0 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 1 0 0 x _ {2} + 5 0 y _ {1} + 1 0 0 z _ {1} \geq 1 0 0 \\ & 2 0 0 y _ {1} \geq 2 0 0 \\ & 0 \leq x _ {2} \leq 1 \\ & 0 \leq y _ {1} \leq 1 \\ & 0 \leq z _ {1} \leq 1 \end{array}\tag{8}
$$

The solution of the problem is $x _ { 2 } { = } 0 . 5 , y _ { 1 } { = } 1 , z _ { 1 } { = } 0$ The dual prices are 0, 210, and 342.5 for the three quantity constraints. Using these dual prices as the coefficients for the linear cost function we can formulate the following quantity support problem.

Denote the unknown price by $p$ and the unknown quantities by $Q _ { \mathrm { A } } , Q _ { \mathrm { B } }$ and $\varrho _ { \mathrm { C } }$ . Here we assume that any bidder can have only one active bid, so $Z _ { 1 }$ is deleted from the quantity support formulation.

$$
\begin{array}{l l} \max & p - 2 1 0 Q _ {\mathrm{B}} - 3 4 2. 5 Q _ {\mathrm{C}} \\ \text { s   .   t   . } & 2 1, 0 0 0 x _ {2} + 7 9, 0 0 0 y _ {1} + p \leq 9 7, 0 0 0 \\ & 5 0 x _ {2} + 1 0 0 y _ {1} + Q _ {\mathrm{A}} \geq 1 0 0 \\ & 1 0 0 x _ {2} + 5 0 y _ {1} + Q _ {\mathrm{B}} \geq 1 0 0 \\ & 2 0 0 y _ {1} + Q _ {\mathrm{C}} \geq 2 0 0 \\ & x _ {2}, y _ {1} \in \{0, 1 \} \end{array}\tag{9}
$$

The suggested bid is (100; 100; 200; \$97,000) with $x _ { 2 } = 0$ and $y _ { 1 } = 0$ . The shortlist is generated by solving problem (9) twice, first with the additional constraint $x _ { 2 } = 1$ , and then with y = 1. The shortlist consists of the following three bids: (100; 100; 200; \$97,000), (50; 0; 200; \$76,000), (0; 50; 0; \$18,000).

Bidder Z decides to accept the second bid from the shortlist, which is added to the bid stream. The new bid $Z _ { 2 }$ becomes active together with $X _ { 2 } ; ~ Y _ { 1 }$ becomes inactive. The bidders X and Y are informed.

Next bidder Y requests a suggested bid. The linear relaxation of the WDP (similar to Eq. (8)) is solved to obtain the dual prices. They are: 0, 210, and 380. The quantity support problem is formulated as in Eq. (9), but this time $Y _ { 1 }$ is left out (one bidder can have only one active bid), and $X _ { 2 } , Z _ { 1 } ,$ , and $Z _ { 2 }$ are included. The total cost to the buyer cannot exceed \$94,000. The suggested bid is $( 5 0 ; 0 ;$ 200; \$73,000) with $x _ { 2 } = 1$ and $z _ { 1 } { = } z _ { 2 } { = } 0$ . The following shortlist is generated by forcing each of the nonzero variables to assume the value of one in turn: (50; 0; 200; \$73,000), (0; 0; 200; \$62,000), (50; 100; 0; \$18,000).

Bidder Y decides to accept bid $Y _ { 2 } { = } ( 0 ; ~ 0 ; ~ 2 0 0 ;$ \$62,000), which is then added to the bid stream. The bidders are informed about their new status. The auction continues along these lines until no bidder is willing to place a new bid.

## 4. Testing the quantity support tool

The idea in testing the quantity support tool is to find out whether the dual-price heuristic produces acceptable suggestions for the bidders. In other words, can it find good bids to ‘team-up’ with, and is the linear approximation of the cost function with the dual prices a reasonable starting point for the shortlist.

We have tested the above-formulated quantity support tool in a reverse auction setting by generating random auctions and solving the WDP and the quantity support problem for each auction<sup>7</sup>. Its performance was compared to the case where cost parameters were chosen randomly (from a certain range), as well as the hypothetical case of perfect information of the true underlying cost functions. The case of perfect information provides an upper bound for the potential profits to be generated and is therefore a good benchmark. The random parameters represent the ‘no information’ case, and we expect the dual prices to perform better. The performance measure for the quantity support tool was profits generated for the bidders.

## 4.1. Choosing the form of the cost function

Combinatorial auctions have an advantage over traditional auctions in situations in which there are synergies between the different items to be auctioned. They are thought to produce higher payoffs for both the auction owner and the bidders. This study was conducted from the viewpoint of reverse auctions, in which the bidders are the sellers and the auctioneer is the buyer. Synergies in reverse auctions arise from the nature of the production process. Economists use the term ‘economies of scope’<sup>8</sup> when talking about complementarities in production. Hence, also the cost function used in the experiments should depict economies of scope. The simplest form for a cost function exhibiting economies of scope is a linear function with a fixed cost element:

$$
C (q _ {i}) = F ^ {i} + c _ {i} q _ {i},\tag{10}
$$

where $F ^ { i }$ is the fixed cost, $c _ { i }$ the per-unit cost of producing item i alone, and $q _ { i }$ the quantity of item i. For the two-item case the cost function would take the form

$$
C (q _ {1}, q _ {2}) = F ^ {1 2} + c _ {1} q _ {1} + c _ {2} q _ {2},\tag{11}
$$

The existence of economies of scope in this framework simply implies that the following inequality holds [23]:

$$
F ^ {1 2} <   F ^ {1} + F ^ {2}\tag{12}
$$

The extension to situations with more than two products is conceptually straightforward. The above presented multi-product cost function (Eq. (11)) is very simplistic. It is theoretically restrictive, as it implies constant marginal costs and monotonically decreasing average costs. Also, the function is discontinuous at points when the level of one or more outputs is zero. The function is also applicable only to situations with relatively few products. It can easily be seen that the number of different fixed cost parameters increases rapidly as the number of products increases. In the case of two products, there are only three parameters ${ \boldsymbol { F } } ^ { 1 } , { \boldsymbol { F } } ^ { 2 }$ and $F ^ { 1 \dot { 2 } }$ . With three products there are seven parameters: $F ^ { 1 } , F ^ { 2 } , F ^ { 3 } , F ^ { 1 2 } , F ^ { 1 3 } , F ^ { 2 3 }$ , and $F ^ { 1 2 3 }$ , where $\bar { F } ^ { \bar { i } j k }$ indicates the fixed cost of producing items $i , \ j ,$ and k simultaneously. When the number of products is increased to five, there are already 31 fixed cost parameters, with six products there are 63, and with seven products 127 parameters. However, the simplicity of the function makes it intuitive and thereby very appealing in an experiment like this<sup>9</sup>.

## 4.2. Experimental design

We initially conducted a series of four different experiments with five replications of each experiment using dual prices as proxies to cost coefficients. The number of items in the auction was either three or five and the number of bidders ten. The number of items had to be kept relatively small due to the exponentially increasing number of fixed cost parameters that had to be generated. The demand for each item was fixed at 1000. The bid quantities were drawn from a continuous uniform distribution between 100 and 500 and rounded to the closest fifty. Some of the bid quantities, however, were chosen to be zero in order to create 20% sparsity in the bid matrix. It is realistic to assume that all bidders would not place bids for all products but a subset of them. The constraint $\mathcal { Q } _ { k } \le 5 0 0$ was added to the quantity support problem to simulate the capacity constraints of the sellers.

A bid for bidder i was generated so that the quantities were chosen randomly, but the bid price was the cost of producing that specific bundle, to which an initial markup of 30% was added. The quantity support tool can naturally be used only when there are some bids already in the bid stream. The initial bid stream was created by entering one bid from each bidder. This tactic was chosen to avoid one bidder having multiple active bids in the optimal solution. The WDP was solved for the initial bid pool, and the quantity support problem was solved using the dual prices of the quantity constraints in the corresponding linear relaxation of the WDP. The price decrement was set at 5% in every experiment. The shortlist was created through solving the quantity support problem over and over again with the added constraint $x _ { i } = 1$ for each original nonbasic variable in turn.

As cost functions<sup>10</sup> we used the linear functions with a fixed cost element as explained in Section 4.1. The intervals for the fixed cost parameters were chosen so that it was very likely that economies of scope would exist. This meant that the lower bound of $F ^ { 1 2 }$ was less than or equal to the sum of the lower bounds of $F ^ { 1 }$ and $F ^ { 2 }$ . A similar logic was applied to the upper bounds. Furthermore, total fixed cost should not decrease due to the addition of a new product. Thus the lower bound of $F ^ { 1 2 }$ was set higher than the upper bounds of $F ^ { 1 }$ and $F ^ { 2 }$

In the first two experiments the fixed costs were quite small relative to the total cost of producing the bundle of items. In the three-item case the lower bounds for the fixed costs ranged from 700 (for $\boldsymbol { F } ^ { 3 } )$ to 2300 $( F ^ { 1 2 3 } )$ and the upper bounds from 1000 $( \boldsymbol { F } ^ { 3 } )$ to 3200 $( F ^ { 1 2 3 } )$ . The variable costs varied within the range [30, 50] for $c _ { 1 } .$ [40, 60] for $c _ { 2 }$ and within [60, 70] for $c _ { 3 }$ . Two new items were added to the three existing ones to create the fiveitem case by keeping the cost parameters for the three first items unchanged. The lower bounds for the fixed costs ranged from 700 (for $F ^ { 3 } )$ to 5500 $( F ^ { 1 2 3 4 5 } )$ and the upper bounds from 1000 $( \boldsymbol { F } ^ { 3 } )$ to 7500 $( F ^ { 1 2 3 4 5 } )$ . The variable costs for $c _ { 4 }$ and $c _ { 5 }$ were within the ranges of [15, 45] and [20, 55]. The exact ranges for all fixed cost parameters can be received from the authors upon request.

In the last two experiments the ranges for the fixed cost parameters were increased so that the function became more nonlinear. In the first two experiments the proportion of the fixed costs was 10% or less of the total cost, which made the cost function relatively linear. Nonlinearity was accentuated by increasing the size of the fixed cost components approximately tenfold while the variable costs stayed the same in all experiments. The lower bounds for the fixed costs in Experiment III and IV ranged from 5000 $( \boldsymbol { F } ^ { 3 } )$ to 42,000 $( F ^ { 1 2 3 4 5 } )$ and upper bounds from 7000 $( \boldsymbol { F } ^ { 3 } )$ to 50,000 $( F ^ { 1 2 3 4 5 } )$ . This increased the proportion of fixed costs to almost 30%. The complete experiment design is presented in Table 1.

The quantity support problem and the shortlist items return the maximal profit for the bidder as the optimal value of the objective function. This figure, however, is based on the linear approximation of the cost function using the dual prices from the linear relaxation of the WDP as proxies for the per-unit costs. A test for the goodness of the quantity support solution is to calculate the ‘true’ profit for the bidders from the combination suggested by the solution. Also, the ‘true’ profit varies from bidder to bidder due to differences in the cost function parameters, whereas the quantity support problem produces only one value for the profit. The underlying thought in calculating the profits for bidders was to find out whether any currently inactive bidder wishing to become active would actually find the suggestion of the quantity support tool worth bidding for.

Table 1 Experiment design

<table><tr><td>Experiment</td><td>Items</td><td>Bids</td><td>Fixed cost</td></tr><tr><td>I</td><td>3</td><td>10</td><td>Low (~10%)</td></tr><tr><td>II</td><td>5</td><td>10</td><td>Low (~10%)</td></tr><tr><td>III</td><td>3</td><td>10</td><td>High (~30%)</td></tr><tr><td>IV</td><td>5</td><td>10</td><td>High (~30%)</td></tr></table>

The results from the experiments were difficult to evaluate as such, creating the need for the use of benchmarks. In our experiment, the natural benchmarks were on the one hand the case of perfect cost information, and on the other hand the case of no cost information. To create the case of perfect information the whole approximated cost function was replaced by each bidder's true cost function in turn. The IP formulation of the profit maximizing problem is not trivial due to the discontinuous cost function. However, in order to save journal space, this formulation is not reproduced in this paper. It can be obtained, upon request, from the authors. Note that there is no shortlist to be created in the perfect information case, because the optimum is found directly for each bidder. It is not obvious how one should interpret the case of no cost information. We decided to test the dual heuristic against randomly chosen cost coefficients. The range for the parameters was suitably chosen.<sup>11</sup> The shortlist was created for the random case in the same way as for the dual-price heuristic. To enable comparisons, the same simulated auctions were used to solve the quantity support problem in all the cases. Everything else remained the same (bidders' cost functions and bid quantities in the initial bid stream), except the cost function used in the quantity support problem.

The experiment was designed so that one bidder could have at most one active bid. This restriction can be added as an additional constraint in the winner determination and quantity support problems. In the simulated auctions of this study there was only one bid from each bidder in the bid stream, so no such constraints were necessary. However, when evaluating the goodness of the quantity support feature we considered it only for those bidders who would be inactive otherwise. If some bidder, whose initial bid already is active, wanted to enter the bid suggested by the quantity support problem, the solution would not be feasible anymore since this bidder would have two active bids. Thus, to simplify the analysis we have only considered providing quantity support for inactive bidders. Also, it is reasonable to assume that bidders who are currently among the winners of the auction would not want to try to improve upon their bids.

Table 2  
Results of Experiment I: profits generated by the dual and random heuristics as percentage of the perfect information case

<table><tr><td>Replication</td><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td rowspan="2">1</td><td>D</td><td>0.86</td><td>0.87</td><td>0.76</td><td>0.14</td><td>1.00</td><td>0.95</td><td>0.87</td><td>0.95</td><td>0.76</td><td>0.00</td></tr><tr><td>R</td><td>0.59</td><td>0.57</td><td>0.39</td><td>0.33</td><td>0.72</td><td>0.62</td><td>0.66</td><td>0.36</td><td>0.61</td><td>0.33</td></tr><tr><td rowspan="2">2</td><td>D</td><td>0.88</td><td>1.00</td><td>0.87</td><td>0.88</td><td>0.92</td><td>1.00</td><td>0.86</td><td>0.00</td><td>0.90</td><td>0.91</td></tr><tr><td>R</td><td>0.27</td><td>0.55</td><td>0.68</td><td>0.59</td><td>0.60</td><td>0.58</td><td>0.66</td><td>0.67</td><td>0.07</td><td>0.55</td></tr><tr><td rowspan="2">3</td><td>D</td><td>0.00</td><td>0.60</td><td>0.73</td><td>0.83</td><td>0.74</td><td>0.79</td><td>0.00</td><td>0.84</td><td>0.82</td><td>0.75</td></tr><tr><td>R</td><td>0.82</td><td>0.72</td><td>0.74</td><td>0.73</td><td>0.75</td><td>0.74</td><td>0.93</td><td>0.77</td><td>0.73</td><td>0.75</td></tr><tr><td rowspan="2">4</td><td>D</td><td>0.92</td><td>0.88</td><td>0.00</td><td>0.79</td><td>0.91</td><td>0.86</td><td>0.42</td><td>0.88</td><td>0.95</td><td>0.91</td></tr><tr><td>R</td><td>0.42</td><td>0.41</td><td>0.12</td><td>0.40</td><td>0.44</td><td>0.38</td><td>0.41</td><td>0.43</td><td>0.41</td><td>0.26</td></tr><tr><td rowspan="2">5</td><td>D</td><td>0.76</td><td>0.83</td><td>0.92</td><td>0.00</td><td>0.87</td><td>0.83</td><td>0.66</td><td>0.87</td><td>0.86</td><td>0.00</td></tr><tr><td>R</td><td>0.65</td><td>0.76</td><td>0.82</td><td>0.85</td><td>0.75</td><td>0.16</td><td>0.72</td><td>0.80</td><td>0.83</td><td>0.00</td></tr><tr><td colspan="2"># cases where D≥R</td><td>4</td><td>4</td><td>3</td><td>3</td><td>4</td><td>5</td><td>3</td><td>4</td><td>5</td><td>4</td></tr></table>

D = dual heuristic, R = random heuristic.

## 5. Results

After the shortlists were created using both dual prices and random parameters in the cost function approximation, the highest profit for each inactive bidder was recorded. The optimal solution varied from one shortlist item to another, so also the combination of inactive bidders varied. Thus, in most cases we were able to obtain a profit for each of the 10 bidders. The profits obtained from the dual price experiments and those obtained from the random parameter experiments were then compared to the maximum obtainable profits from the perfect information case. This comparison could be made because the bidders' true cost functions and the initial bids in the bid stream were kept the same from the dual price case to the random parameter and the perfect information cases. The comparison was done by calculating what percentage of the maximum profit was obtained by the dual price and random cost approaches.

The results of the first three experiments are presented in Tables 2, 3, and 4. The results in general were very promising. The quantity support tool using dual prices categorically found profits that were above 70% of the maximum, as can be seen from the tables. The profits obtained with the random approach were often lower, and varied more. In pairwise comparisons, the dual price approach (D) outperformed the random cost approach (R) 83% of the time. We also tested the statistical significance of the results presented in Tables 2, 3, and 4 using a pairwise t-test. The p-values (twotailed) for the three respective tables were highly significant (0.007, 0.0000, 0.0001).

The mark-up percentage in the original bids was set at 30%. One would assume that the mark-ups would have to decrease in order for the new bids to become active. Interestingly, the profits generated by the dual price quantity support tool resulted in higher than 30% mark-ups about 80% of the time.

In the fourth experiment (5 products, 10 bids and higher fixed costs), the quantity support tool using dual prices did not perform as well as the one with random cost parameters (p-value 0.003). However, as can be seen from Table 5, the dual price approach is still oftentimes reasonably good generating profits well above 60% of the maximum. The random parameters simply worked even better.

Table 3  
Results of Experiment II: profits generated by the dual and random heuristics as percentage of the perfect information case

<table><tr><td>Replication</td><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td rowspan="2">1</td><td>D</td><td>0.78</td><td>0.73</td><td>0.78</td><td>0.49</td><td>0.56</td><td>0.72</td><td>1.00</td><td>0.79</td><td>0.73</td><td>0.75</td></tr><tr><td>R</td><td>0.38</td><td>0.26</td><td>0.15</td><td>0.00</td><td>0.33</td><td>0.21</td><td>0.22</td><td>0.24</td><td>0.40</td><td>0.29</td></tr><tr><td rowspan="2">2</td><td>D</td><td>0.90</td><td>0.74</td><td>0.80</td><td>0.78</td><td>0.74</td><td>0.00</td><td>0.77</td><td>0.80</td><td>0.82</td><td>0.80</td></tr><tr><td>R</td><td>0.73</td><td>0.62</td><td>0.57</td><td>0.00</td><td>0.67</td><td>0.00</td><td>0.69</td><td>0.60</td><td>0.00</td><td>0.58</td></tr><tr><td rowspan="2">3</td><td>D</td><td>0.85</td><td>0.65</td><td>0.80</td><td>0.00</td><td>0.85</td><td>0.78</td><td>0.76</td><td>0.00</td><td>0.84</td><td>0.86</td></tr><tr><td>R</td><td>0.24</td><td>0.20</td><td>0.26</td><td>0.00</td><td>0.00</td><td>0.23</td><td>0.30</td><td>0.00</td><td>0.38</td><td>0.35</td></tr><tr><td rowspan="2">4</td><td>D</td><td>1.00</td><td>0.86</td><td>1.00</td><td>1.00</td><td>1.00</td><td>0.00</td><td>0.94</td><td>1.00</td><td>1.00</td><td>0.00</td></tr><tr><td>R</td><td>0.34</td><td>0.28</td><td>0.29</td><td>0.05</td><td>0.30</td><td>0.00</td><td>0.31</td><td>0.39</td><td>0.39</td><td>0.44</td></tr><tr><td rowspan="2">5</td><td>D</td><td>0.98</td><td>0.76</td><td>0.84</td><td>0.76</td><td>0.00</td><td>1.00</td><td>0.91</td><td>1.00</td><td>0.47</td><td>0.00</td></tr><tr><td>R</td><td>0.34</td><td>0.34</td><td>0.42</td><td>0.00</td><td>0.37</td><td>0.17</td><td>0.36</td><td>0.37</td><td>0.33</td><td>0.11</td></tr><tr><td colspan="2"># cases where D≥R</td><td>5</td><td>5</td><td>5</td><td>5</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3</td></tr></table>

D = dual heuristic, R = random heuristic.

Results of Experiment III: profits generated by the dual and random heuristics as percentage of the perfect information case

<table><tr><td>Replication</td><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td rowspan="2">1</td><td>D</td><td>0.50</td><td>0.55</td><td>0.47</td><td>0.45</td><td>0.48</td><td>0.00</td><td>0.44</td><td>0.46</td><td>0.48</td><td>0.51</td></tr><tr><td>R</td><td>0.26</td><td>0.23</td><td>0.23</td><td>0.24</td><td>0.25</td><td>0.00</td><td>0.31</td><td>0.30</td><td>0.32</td><td>0.51</td></tr><tr><td rowspan="2">2</td><td>D</td><td>0.98</td><td>0.53</td><td>0.68</td><td>0.55</td><td>0.00</td><td>0.73</td><td>0.62</td><td>0.65</td><td>0.66</td><td>0.73</td></tr><tr><td>R</td><td>0.98</td><td>0.50</td><td>0.68</td><td>0.55</td><td>0.31</td><td>0.73</td><td>0.62</td><td>0.65</td><td>0.66</td><td>0.73</td></tr><tr><td rowspan="2">3</td><td>D</td><td>0.52</td><td>1.00</td><td>0.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td>R</td><td>0.06</td><td>0.22</td><td>0.28</td><td>0.17</td><td>0.24</td><td>0.25</td><td>0.19</td><td>0.28</td><td>0.18</td><td>0.28</td></tr><tr><td rowspan="2">4</td><td>D</td><td>0.63</td><td>0.57</td><td>0.59</td><td>0.54</td><td>0.59</td><td>0.62</td><td>0.57</td><td>0.31</td><td>0.64</td><td>0.53</td></tr><tr><td>R</td><td>0.67</td><td>0.55</td><td>0.66</td><td>0.61</td><td>0.40</td><td>0.58</td><td>0.49</td><td>0.65</td><td>0.57</td><td>0.64</td></tr><tr><td rowspan="2">5</td><td>D</td><td>0.83</td><td>0.84</td><td>0.73</td><td>0.89</td><td>0.85</td><td>0.86</td><td>0.68</td><td>1.00</td><td>0.87</td><td>0.83</td></tr><tr><td>R</td><td>0.68</td><td>0.76</td><td>0.58</td><td>0.73</td><td>0.61</td><td>0.00</td><td>0.68</td><td>0.79</td><td>0.81</td><td>0.71</td></tr><tr><td colspan="2"># cases where D≥R</td><td>3</td><td>5</td><td>2</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>4</td></tr></table>

D = dual heuristic, R = random heuristic.

One must keep in mind here, though, that the random parameters were chosen from the interval within which the dual prices varied. In reality, only one or the other approach would be used. So, if we were using random parameters alone, we would not know the range within which the dual prices varied. We reproduced Experiment IV with random cost parameters, but this time chosen from the range [0, 2000]. The random parameters worked poorly producing very small profits categorically. The performance of the random parameters approach understandably seems to depend on the chosen range of the cost parameters. The approach of generating random parameters is beautiful in its simplicity, but their use is complicated by the fact that an unsuitable range can significantly deteriorate the results. Thereby, we feel that using dual prices is a better and more robust approach. It is also fairly simple, even though an additional (linear) optimization problem has to be solved each time someone wishes to use the quantity support tool.

## 6. Implementation considerations

Desirable properties of an auction design are allocative efficiency, maximum revenue/minimum cost, incentive compatibility, high speed, low transaction costs, and fairness [4,11,29]. Allocative efficiency means that the lowest cost producer(s) are the auction winners. Allocative efficiency can lead to revenue maximization or cost minimization, but not necessarily. Incentive compatibility refers to the bidders' incentives to bid truthfully, i.e. according to their underlying valuations. Thus incentive compatibility affects efficiency and revenues. Fairness refers, among others, to methods of resolving ties (see [29] for suggestions), and the transparency of the system. Furthermore, fairness implies that approximate solutions to the

Results of Experiment IV: profits generated by the dual and random heuristics as percentage of the perfect information case

<table><tr><td>Replication</td><td></td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td><td>Bidder 5</td><td>Bidder 6</td><td>Bidder 7</td><td>Bidder 8</td><td>Bidder 9</td><td>Bidder 10</td></tr><tr><td rowspan="2">1</td><td>D</td><td>0.70</td><td>0.50</td><td>0.67</td><td>0.69</td><td>0.69</td><td>0.69</td><td>0.60</td><td>0.70</td><td>0.74</td><td>0.67</td></tr><tr><td>R</td><td>0.97</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>1.00</td><td>0.39</td><td>0.82</td></tr><tr><td rowspan="2">2</td><td>D</td><td>0.47</td><td>0.00</td><td>0.72</td><td>0.77</td><td>0.76</td><td>0.79</td><td>0.69</td><td>0.87</td><td>0.70</td><td>0.69</td></tr><tr><td>R</td><td>0.90</td><td>0.74</td><td>0.81</td><td>0.88</td><td>0.88</td><td>0.84</td><td>0.65</td><td>0.00</td><td>0.81</td><td>0.74</td></tr><tr><td rowspan="2">3</td><td>D</td><td>0.00</td><td>1.00</td><td>0.85</td><td>0.00</td><td>1.00</td><td>0.91</td><td>*</td><td>1.00</td><td>0.92</td><td>0.72</td></tr><tr><td>R</td><td>0.46</td><td>0.57</td><td>0.33</td><td>0.52</td><td>0.65</td><td>0.58</td><td>*</td><td>0.55</td><td>0.61</td><td>0.61</td></tr><tr><td rowspan="2">4</td><td>D</td><td>0.87</td><td>0.86</td><td>0.70</td><td>0.00</td><td>0.87</td><td>0.84</td><td>0.90</td><td>0.00</td><td>0.87</td><td>0.87</td></tr><tr><td>R</td><td>0.81</td><td>0.96</td><td>0.89</td><td>1.00</td><td>0.95</td><td>0.88</td><td>0.98</td><td>0.00</td><td>0.99</td><td>0.96</td></tr><tr><td rowspan="2">5</td><td>D</td><td>0.33</td><td>0.14</td><td>0.00</td><td>0.34</td><td>0.34</td><td>0.47</td><td>0.08</td><td>0.34</td><td>0.00</td><td>0.32</td></tr><tr><td>R</td><td>0.71</td><td>0.87</td><td>0.67</td><td>0.68</td><td>0.29</td><td>0.82</td><td>0.66</td><td>0.68</td><td>0.70</td><td>0.72</td></tr><tr><td colspan="2"># cases where D≥R</td><td>1</td><td>1</td><td>1</td><td>0</td><td>2</td><td>1</td><td>1</td><td>3</td><td>2</td><td>1</td></tr></table>

\*Lindo could not find a solution.  
D = dual heuristic, R = Random heuristic.

WDP are unacceptable, because the set of winning bidders could change from the optimal [11,29]. Also, suppliers may perceive it as more fair, if there are constraints requiring that several bidders win some business (which helps small firms especially). Fairness issues are deemed critical in maintaining long-term supplier relations [11].

The desirable properties are achieved by careful design of auction procedures and rules, the details depend on the particular market the auction is going to be held in. Each auction owner will want to customize the auction to fit its purposes. Thus we only discuss the more general design issues. The following discussion is from the perspective of the NegotiAuction system. NegotiAuction is a progressive, first-price, semi-sealed bid auction. Bids enter continuously, and the WDP is solved after every incoming bid. In case the next bid comes in before the problem is solved, the solution algorithm is terminated, and restarted with the new bid added into the bid stream. The quantity support mechanism works best in a continuous auction. However, in larger auctions the solution of the WDP takes time and it might not be feasible to solve it after every bid, especially if bids are entering at a fast pace. Also, the bidders' monitoring and participation costs increase [27].

In NegotiAuction, each time the WDP is solved, the bidders are notified about the status of all of their own bids, but they are not given any information on the currently winning bids or bids placed by other bidders. However, it is also possible to hold an open-cry auction in the NegotiAuction system. In that case, bidders would receive full information on all bids placed in the auction, but not necessarily the identity of the bidders. Then bidders could potentially solve the quantity support problem independently. Even so, we believe that bidders would like to use a readily available quantity support tool, because it would be time-consuming to formulate and solve the WDP and the quantity support problem. Also, as the number of bids in the bid stream increases, it becomes more and more difficult to decide on quantities and a price without the help of computer-aided calculations.

All bids are retained in the bid stream, until they become dominated. The bidder is notified, when her bid is permanently removed. Bidders are not allowed to withdraw bids, because combinatorial bidding allows them to avoid the exposure problem even without the possibility of withdrawals. If winning bidders default on their bid, they may be subject to a penalty as defined by the auction owner. Bids are indicated as price–quantity vectors. Each bidder is allowed to have only one bid active at a time, so formal XOR bidding, which slows down the computations, is not needed.

Bidding rules should state the required improvements on bids, and also contain the activity rules and closing rules of the auction. Activity rules state how often and what kind of bids a bidder must enter in order to be eligible to continue bidding. Closing rules indicate when the auction ends. The auction owner can also specify the improvements that are required from new bids before they are allowed to enter the auction. These rules are all intertwined, so a choice of a particular closing rule and requirements for bid improvements affects the activity rules. Activity rules are crucial in auction design, because they expedite the convergence. Also, if the closing time is announced, bidders may wait for the last minute to bid in the absence of activity rules. To avoid designing very complicated activity rules, the closing rule in NegotiAuction is tied to bidding activity. After the announced time the auction actually closes only after there is a period of no bidding. This way, the only task for the activity rules is to expedite convergence. The use of the quantity support mechanism should speed up the auction process. It will also automatically suggest bids that decrease the cost to the buyer by a predetermined decrement. However, some improvement requirements should also apply to bids made without the use of quantity support; otherwise it would be easy to fulfill activity rules by placing noncompetitive bids.

The buyer can also specify constraints on the auction outcome. She can set a reservation price, which the total cost must meet or beat. She can also set constraints on market share, for example she might want to specify that the number of suppliers must be large enough (not to be too dependent on a few suppliers), but not too large (to avoid extra costs from administering many suppliers). These constraints can also improve the perceived fairness of the auction.

What do the auction rules in NegotiAuction imply for the properties of the mechanism? Is it incentive compatible? Does it lead to allocative efficiency or maximal cost savings for the buyer? Is it fair? Progressive auctions such as NegotiAuction are usually incentive compatible. If the bidder does not bid up to her valuation (or the valuation of the second highest bidder), she risks losing the item. Also bidding below costs (to drive down the price) is not wise when bid withdrawals are not allowed. However, in combinatorial auctions incentive compatibility problems can arise as the result of the threshold problem. A bidder does not have an incentive to improve upon her bid, if she cannot improve it enough to become a winner, unless someone else also improves on her bid.<sup>12</sup> Allocative efficiency is difficult to reach in a multi-item, multi-unit combinatorial auction. The problems with allocative efficiency are related to the threshold problem. If an efficient bidder is to be among the winners, other efficient bidders must have made suitable bids to team-up with. Thus efficiency becomes relative. Sometimes a bidder can win by placing a bid, which is not optimal with respect to her production possibilities, if it is what best complements the other low cost producers. Our quantity support tool cannot guarantee allocative efficiency, but it improves the efficiency of the auction and lowers the cost to the buyer. Regarding fairness, we argue that our system is transparent, does not use approximate solutions to the WDP, and seeks to support both parties.

## 7. Conclusions

Combinatorial auctions are an efficient market mechanism in a situation in which there are synergies between the items to be auctioned. In the context of reverse auctions this translates into economies of scope in the production process of multiple items. Combinatorial auctions are known to be computationally difficult to manage, but also the task of the bidders becomes highly complicated. Computational aspects have been extensively studied, but not the decision support aspects of auctions. In combinatorial auctions the winning bids complement each other. However, in sealed-bid auctions it is impossible for bidders to find such combinations. Thus the winners are those who happen to guess a good combination rather than those who would have had the lowest production costs, providing a case for progressive auctions.

We feel that it is important to provide decision support for the bidders in combinatorial auctions. We have developed a ‘quantity support tool’, which generates a shortlist of price–quantity combinations that team-up with existing bids in such a way that they would be among the current winners. We are not aware of other similar support tools. The problem of evaluating each combination in the shortlist and choosing the best one is left to the bidder. Extending the tool to help the bidders choose their most preferred combinations from the shortlist is well worth looking into in the future, particularly for cases where the shortlist is not so short and the number of items is relatively large.

The quantity support problem is formulated as a profit maximization problem for the bidder subject to the constraints that the total cost to the buyer must decrease from one bid to the next and demand must be met. In the absence of information on the bidders' cost structures we approximate them with a linear cost function. We use the dual prices from the LP relaxation of the WDP as proxies for the true variable costs for each item. Because we do not have information on the bidders' true cost structures, we generate a shortlist of ‘good’ combinations. Results of the tests indicate that the quantity support tool is useful. When bidders use it, the total cost to the buyer decreases and the efficiency of the auction improves.

Future research includes implementing the quantity support tool as a part of an auction system, and testing it with real people. We will also investigate the convergence properties of our progressive combinatorial auction scheme over time.

## Acknowledgment

The authors wish to thank Professors Matthew Carlyle (Naval Postgraduate School) and Murat Köksalan (Middle East Technical University) for valuable comments, and the Foundation for Economic Education (Finland), the Kemira Foundation (Finland), the Foundation of the Helsinki School of Economics, Wihuri Foundation (Finland), and the Academy of Finland (grants # 212767 and 200935) for financial support.

## References

[1] G. Adomavicius, A. Gupta, Toward comprehensive real-time bidder support in iterative combinatorial auctions, Information Systems Research 16 (2005) 169–185.

[2] R. Bapna, P. Goes, A. Gupta, A theoretical and empirical investigation of multi-item on-line auctions, Information Technology and Management 1 (2000) 1–23.

[3] R. Bapna, P. Goes, A. Gupta, Insights and analyses of on-line auctions, Communications of the ACM 44 (2001) 43–50.

[4] M. Bichler, A. Davenport, G. Hohner, J. Kalagnanam, Industrial procurement auctions, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2006.

[5] Y. Cho, Economic efficiency of multi-product structure: the evidence from Korean housebuilding firms, Journal of Housing Economics 12 (2003) 337–355.

[6] W. Conen, T. Sandholm, Minimal Preference Elicitation in Combinatorial Auctions, Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI), Workshop on Economic Agents, Models and Mechanisms, Seattle, WA, 2001.

[7] S. De Vries, R. Vohra, Combinatorial auctions: a survey, INFORMS Journal on Computing 15 (2003) 284–309.

[8] M. Fan, J. Stallaert, A.B. Whinston, Decentralized mechanism design for supply chain organizations using a market auction, Information Systems Research 14 (2003) 1–22.

[9] J. Gallien, L.M. Wein, A smart market for industrial procurement with capacity constraints, Management Science 51 (2005) 76–91.

[10] R. Gonen, D. Lehmann, Optimal solutions for multi-unit combinatorial auctions: branch and bound heuristics, The Proceedings of the Second ACM Conference on Electronic Commerce (EC'00), 2000, pp. 13–20.

[11] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, J.R. Kalaganam, H.S. Lee, C. An, Combinatorial and quantitydiscount procurement auctions benefit Mars, Incorporated and its suppliers, Interfaces 33 (2003) 23–35.

[12] S.D. Jap, An exploratory study of the introduction of online reverse auctions, Journal of Marketing 67 (2003) 96–107.

[13] M. Jin, S.D. Wu, M. Erkoc, Multiple unit auctions with economies and diseconomies of scale, European Journal of Operational Research 174 (2006) 816–834.

[14] J.L. Jones, G.J. Koehler, Combinatorial auctions using rule-based bids, Decision Support Systems 34 (2002) 59–74.

[15] P.G. Keat, P.K. Young, Managerial Economics: Economic Tools for Today's Decision Maker, Prentice Hall, New Jersey, 2000.

[16] R. Keeney, H. Raiffa, Decisions with Multiple Objectives: Preferences and Value Tradeoffs, Wiley, New York, 1976.

[17] O. Koppius, E. Van Heck, Information architecture and electronic market performance in multidimensional auctions, http://hdl. handle.net/1765/921/%D, 2002.

[18] V. Krishna, Auction Theory, Academic Press, San Diego, 2002.

[19] A.M. Kwasnica, J.O. Ledyard, D. Porter, C. DeMartini, A new and improved design for multiobjective iterative auctions, Management Science 51 (2005) 419–434.

[20] R.-L. Leskelä, Electronic multi-attribute auctions: a support mechanism for a combinatorial setting, Master's Thesis, Department of Industrial Engineering and Management, Helsinki University of Technology (2004).

[21] T. Metty, R. Harlan, Q. Samelson, T. Moore, T. Morris, R. Sorensen, A. Schneur, O. Raskina, R. Schneur, J. Kanner, K. Potts, J. Robbins, Reinventing the supplier negotiation process at Motorola, Interfaces 35 (2005) 7–23.

[22] J.D. Murray, R.W. White, Economies of scale and economies of scope in multiproduct financial institutions: a study of British Columbia Credit Unions, The Journal of Finance 38 (1983) 887–902.

[23] J.C. Panzar, Technological determinants of firm and industry structure, in: R. Schmalensee, R.D. Willig (Eds.), Handbook of Industrial Organization, Vol I, North-Holland, 1989.

[24] J.C. Panzar, R.D. Willig, Economies of scope. The American Economic Review 71 (2), Papers and Proceedings of the 93rd Annual Meeting of the American Economic Association (May, 1981), 1981.

[25] S. Park, M. Rothkopf, Auctions with bidder-determined allowable combinations, European Journal of Operational Research 161 (2005) 399–415.

[26] D. Parkes, iBundle: an efficient ascending price bundle auction, ACM Conference on Electronic Commerce, 1999, pp. 148–157, Denver, Colorado.

[27] D. Parkes, Iterative combinatorial auctions, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2006 (Chapter 2).

[28] D. Parkes, L.H. Ungar, Iterative combinatorial auctions: theory and practice, Proceedings of the 17th National Conference on Artificial Intelligence (AAAI-00), 2000, pp. 74–81.

[29] A. Pekeč, M.H. Rothkopf, Combinatorial auction design, Management Science 49 (2003) 1485–1503.

[30] M. Rothkopf, A. Pekeč, R. Harstad, Computationally manageable combinational auctions, Management Science 44 (1998) 1131–1147.

[31] T. Sandholm, Approaches to winner determination in combinatorial auctions, Decision Support Systems 28 (2000) 165–176.

[32] T. Sandholm, C. Boutilier, Preference elicitation in combinatorial auctions, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, 2006, Chapter 10.

[33] Y. Sheffi, Combinatorial auctions in the procurement of transportation services, Interfaces 34 (2004) 245–252.

[34] J. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, Designing electronic auctions: an internet-based hybrid procedure combining aspects of negotiations and auctions, Electronic Commerce Research 1 (2001) 301–314.

[35] J. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A Multi-Attribute e-Auction Mechanism for Procurement: Theoretical Foundations, European Journal of Operational Research 175 (2006) 90–100.

[36] R.R. Vemuganti, Applications of set covering, set packing and set partitioning models: a survey, in: D.-Z. Du (Ed.), Handbook of Combinatorial Optimization, Vol. 1, Kluwer Academic Publishers, Netherlands, 1998, pp. 573–746.

[37] R. Vohra, R.J. Weber, A “bids and offers” approach to package bidding, An official filing with the FCC, 2000, http://wireless. fcc.gov/auctions/31.

[38] P. Wurman, M. Wellman, AkBA: A Progressive, Anonymous-Price Combinatorial Auction, in ACM Conference on Electronic Commerce, 2000, pp. 21–29, Minneapolis, Minnesota.

[39] M. Xia, G.J. Koehler, A.B. Whinston, Pricing combinatorial auctions, European Journal of Operational Research 154 (2004) 251–270.

Riikka-Leena Leskelä is a Ph.D. candidate at the Helsinki University of Technology. She received her M.Sc. (Tech) from Helsinki University of Technology 2004. Her research interests are in the area of multiattribute and combinatorial auctions.

Dr. Jeffrey Teich is an Associate Professor at New Mexico State University. His research interests and publications are in the areas of negotiation modeling, electronic commerce, and decision support. He has served as a Visiting Professor at the Helsinki School of Economics, teaching in its international programs, and at Erasmus University, Rotterdam. He has also been awarded a Fulbright Scholarship to lecture and conduct research in the Republic of the Maldives.

Hannele Wallenius holds a Ph.D. from the University of Jyväskylä, Finland. She has been faculty at the Helsinki University of Technology since 1995 where she is currently Professor of Industrial Economics at the Department of Industrial Engineering and Management. Her research has dealt with such diverse areas as Multiple Criteria Decision Making, public sector operations research, negotiation analysis and more recently electronic auctions and market mechanisms. Hannele Wallenius has spent numerous sabbaticals in the US, notably at Purdue University, Texas A&M University and Arizona State University. In addition, she has taught in the international programs of the Helsink School of Economics.

Jyrki Wallenius holds a Ph.D. from the Helsinki School of Economics, where he is professor since 1990. He has served ten years as the Director of the Helsinki School of Economics Information Technology Program and seven years as the MBA Director. His research encompasses Multiple Criteria Decision Making, negotiation analysis, decision support, behavioral decision making, and more recently electronic auctions and market mechanisms. Jyrki Wallenius has been a visiting professor at Purdue University, Texas A&M University and Arizona State University on several occasions. He is past editor of the European Journal of Operational Research and the President Elect of the International Society of Multiple Criteria Decision Making. He is the recipient of numerous awards, both domestic and international.
