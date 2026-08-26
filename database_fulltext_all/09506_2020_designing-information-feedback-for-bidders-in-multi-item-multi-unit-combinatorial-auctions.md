---
otero_id: 9506
otero_key: "X32BVEY9"
title: "Designing information feedback for bidders in multi-item multi-unit combinatorial auctions"
authors: "Anup K. Sen; Amitava Bagchi; Soumyakanti Chakraborty"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113230"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing information feedback for bidders in multi-item multi-unit combinatorial auctions

![](/api/attachments/X32BVEY9/fulltext/images/6275f9b5a4ff05c6200d7f8f080c4e436e983856b049d143f2f46d69e9026680.jpg)

Anup K. Sen<sup>a</sup>, Amitava Bagchi<sup>b</sup>, Soumyakanti Chakraborty<sup>a,⁎</sup>

<sup>a</sup> Indian Institute of Management Calcutta, India

<sup>b</sup> Heritage Institute of Technology, Kolkata, India

## A R T I C L E I N F O

Keywords: Continuous combinatorial auctions Real-time bidder support Multi-unit auctions Electronic markets

## A B S T R A C T

Combinatorial auctions (CAs) promote allocative eficiency and are important market mechanisms for a wide variety of specialized domains where bidders are allowed to place bids on packages of items. However, the adoption of combinatorial auctions in real-life business scenarios has been fairly limited, perhaps because bidders find it dificult to construct their bids without extensive knowledge of the current state of the auction. In this paper, we develop decision support tools for bidders to provide information feedback at runtime for the general class of combinatorial auctions namely, online (continuous) multi-item multi-unit combinatorial auc tions (MUCAs). an area that has witnessed a rapid growth of interest in recent vears. In online MUCAs the number of packages may be large, and bidders need real time decision support to construct their bids, such as information on the ask prices of packages. The deadness level of a package serves as the ask price, and indicates the minimum bid on the package that keeps it in contention for inclusion in winning combinations in future. It has proved a challenge to find a satisfactory method for computing the deadness levels of packages in MUCAs. Here we present exact methods for determining package deadness levels in such auctions. Both the OR and the XOR formulations are considered. Experiments on simulated data as well as on live data show that the time and memory requirements are not excessive, so it appears possible to adopt the methods for the procurement and sale of commodities in B2B and B2C markets.

## 1. Introduction

Combinatorial auctions that allow bidders to bid on combinations (bundles or packages) of items make business sense when there are bundles of items that have a combined valuation to bidders higher than the sum of their individual valuations. Such items are said to be com plementary. CAs can be single round or iterative. Iterative CAs can be further divided into multi-round and continuous.<sup>1</sup> Examples of CAs abound in the business world: spectrum auctions (UK 2013, Australia 2013, Germany 2015, Switzerland 2012, Mexico 2016, Denmark 2016 and Netherlands 2012) [1], airport take-of and landing slots [2], bundling of routes for transportation [3,4], logistics services [5,6], raw material procurement in supply chain management [7], and travel package planning [8].

There are two major costs of allowing bids on combinations of items, and they have been a significant barrier to wide adoption of CAs [9–11]. First, the computation cost of solving the Winner Determination

Problem (WDP), i.e., of determining the winning allocation, is very high in principle, since the WDP is an NP-hard problem [12–14]. Secondly, the cognitive cost for bidders is also high, as the complexity of CAs makes it dificult for bidders to bid meaningfully [9,15]. In a single item single unit auction, such as an English auction, a bidder only needs to bid more than the current highest bid on the item to keep her bid in contention. But in CAs the problem of bid construction is complex. A bid on a package may not be winning currently and still be in conten tion for the winning allocation, as subsequent bids from other bidders may combine with it to form the winning combination. In the absence of information feedback from the auctioneer, it is dificult for a bidder to determine how much to bid. Both the above costs grow exponentially with the number of items.

WDP has received the attention of numerous researchers, and with the wide availability of high-end computing resources, solving the WDP within a reasonable time limit has become possible [12]. However, the problem of providing relevant information feedback to bidders so that they can bid meaningfully has not yet been completely resolved, par ticularly for continuous combinatorial auctions. It can be partially ad dressed in a multi-round combinatorial auction where the provisional winners of each round are announced along with the ask prices of the packages [16–18]. But there is no notion of a “round” in a continuous (or online) combinatorial auction, and bidders can join, leave or bid at any time. To make online combinatorial auctions possible it is necessary to provide information feedback to a bidder whenever it is needed and not just after a fixed time interval. For single-unit continuous combi natorial auctions with OR bids, Adomavicius et al. [19] proposed a mechanism based on two price levels, Deadness Level (or lower level) and Winning Level (or higher level) (see Example 1 below). The Winning Level (WL) of a package is the minimum amount a bidder has to bid on a package to make it a part of the winning allocation at the following instant, and the Deadness Level (DL) of a package is the minimum amount the bidder has to bid on it to ensure that the package remains in contention for inclusion in a winning allocation in future. Petrakis et al. [20] extended the scope of the single-unit problem by permitting XOR bids; in this formulation, no bidder can win more than one package. Recently, mechanisms have been proposed [21] for in formation feedback in auctions of single items with multiple indistinguishable copies; but there are no computational tools that provide information feedback to bidders in general multi-unit continuous combinatorial auctions of heterogeneous items.

Example 1. In a continuous combinatorial auction of one unit each of two items X and Y, the following bids were placed in time sequence: (XY, 20, 1); (X, 10, 2); (Y, 15, 3); (XY, 30, 4). The parameters within parentheses are the package, the bid amount, and the time instant at which the bid was placed. Assuming the objective is to maximize the seller's revenue, bid 4 is the current winning bid at instant 4, as the combination of bids at instants 2 and 3 add up only to 25 (< 30). The first bid of 20 on XY is no longer active, i.e., it is now a ‘dead’ bid as it can never be a part of any winning allocation. In other words, the minimum amount that a bidder must bid on XY in future in order to stay in contention for inclusion in a winning allocation is 30. Thus, the deadness level (DL) of package XY is 30. Let us now look at the DL and WL values of package X. The DL of X is 10, as any bid on X of 10 (plus a small increment) will keep it in contention. That is, if a bidder bids 11 on X (X, 11, 5) then a hypothetical bid of 20 on Y at a future instant can combine with the bid on X to dislodge the winning bid of (XY, 30, 4). However, the bid (X, 11, 5) has to wait for the hypothetical bid of 20 on Y. If the bidder is not keen to wait for such a hypothetical bid and instead wants to be a part of the winning allocation at the very next time instant, then she has to bid 15 (plus a small increment), i.e. (X, 16, 5), so that it can combine with the third bid (Y, 15, 3) to form a winning allocation. Thus, the winning level (WL) of package X is 15. □

Practical implementations of multi-unit combinatorial auctions are increasingly becoming a necessity in today's business world. The Mexico and Canada spectrum auctions in 2016 and 2015 respectively, the UK 4G spectrum auction in 2013, and many other such auctions in Europe were conducted as combinatorial auctions that had multiple units of spectrum bands [1,22]. Mars Inc. organizes two diferent mechanisms for procurement auctions for its buyers and suppliers [23]; the first allows bidders to place bids on bundles of items, and the other facilitates volume discounting where bidders can specify bids on multiple units of items. Auctions for procuring rights to truckload transportation lanes allow package bidding [24]. Multi-item multi-unit combinatorial auctions (MUCAs) are also becoming popular in natural resource management, in the areas of procurement of conservation services, water buybacks, climate change management schemes, fishing quota allocation, etc. [25].

Table 1 classifies combinatorial auctions based on the following two dimensions: Number of Units and Bid Type. Our interest is in the multiunit combinatorial auction (MUCA). In multi-item CAs, the number of packages is large and it is burdensome for a bidder to determine how much to bid on a package. In the absence of relevant information feedback, a bidder has to determine the next bid after evaluating the current bids on each package and its complementary package(s). In a combinatorial auction with a large number of items, this imposes a high cognitive load on bidders [9]. It becomes greater in the case of MUCAs, particularly for online MUCAs. Adomavicius et al. [9] have demonstrated experimentally that in single item CAs, information feedback on DLs and WLs of packages can help bidders place more meaningful bids, impacting positively on revenue generation. A similar conclusion will hold true for MUCAs as well. Our work focuses on developing a decision support system (DSS) for MUCAs to guide bidders in bid construction by providing real time information feedback. This DSS will allow a bidder to place queries on the multi-unit deadness level (MDL) and the multi-unit winning level (MWL) of a package at any time during an auction. The system will examine all the bids placed up to that time and return the relevant values.

Table 1  
The diferent categories of combinatorial auctions.<sup>a</sup>

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Number of units</td></tr><tr><td>Single-unit</td><td>Multi-unit</td></tr><tr><td rowspan="2">Bid type</td><td>OR</td><td>SU-OR</td><td>MU-OR</td></tr><tr><td>XOR</td><td>SU-XOR</td><td>MU-XOR</td></tr></table>

<sup>a</sup> Researchers have also used the terms ‘single-item’ and ‘multi-item’ when referring to CAs, to distinguish between homogeneous and heterogeneous items respectively [21]. Based on this nomenclature, our work can be termed as multi-item multi-unit CAs (MIMU CAs) instead of multi-unit CAs (MUCA).

## 1.1. Determining DL and WL values for multi-unit CAs

There is a major point of diference between single-unit and multi unit CAs. In the single-unit case, at most one bid on a package p is active at any time instant, namely the highest bid that has been placed on p by any bidder up to that instant. Other bids placed on p are dead and do not play any further role in the auction; there can be several bids that are active at any instant but each on a diferent package. In a MUCA, two diferent bids on a package p can both be active simultaneously, which can never happen in a single unit CA. This is because it might be possible to accommodate more than one copy of p in a winning combination. So, the ask price of p can be smaller than the highest current bid on p (see Example 2). This makes the determination of the MDL and MWL values of packages in a MUCA a more complex task.

Example 2. Consider a CA with two items, X and Y, and the following two bids (XY,15, 1) and (XY,20,2). In the single unit case, the deadness level (DL) of XY after the two bids is 20, as any bid < 20 can never be part of a winning allocation, implying that the first bid is a dead bid. In the multi-unit case with two units of X and Y available, and the same bid sequence as above, both bids are active, as the two bids together form a winning allocation. The deadness level of XY in this case is not 20 but 15; a fresh bid of value 17 on XY will dislodge the bid of value 15 from the winning allocation. □

A MUCA can be converted into a single unit combinatorial auction (SUCA) by creating dummy items and bidders: but this leads to an exponential increase in the number of bids [26]. For example, for a combinatorial auction of two items, X having two units and Y one, we have to create dummy items X1 and X2. If a bidder places bids on both X and XY, instead of [X OR XY] we have [(X1 XOR X2) OR (X1Y XOR X2Y)]. No algorithmic methods are currently available for processing such OR-XOR bids. So the transformed SUCA formulation becomes infeasible in practice. It should also be noted that the determination of deadness levels for XOR bids is even harder than NP-Complete [20].

Thus, it is important to devise methods to provide real time feedback on the WL and DL values of packages in MUCAs. In this paper, we propose exact schemes for computing the $M D L ( p , t )$ and $M W L ( p , t )$ values of a package p at time instant t. We do this separately for both the OR and the XOR formulations. In the XOR formulation, the deadness and winning levels are bidder dependent [20]. We also propose an incremental method for computing the MDL value of a package at an instant t + 1 given its value at instant t. Bidders will now be able to restrict a bid on p to the “safe” region between $M D L ( p , t )$ and $M W L ( p , t )$ , keeping the bid in contention for inclusion in winning combinations in future.

The paper makes several contributions. First, we present a real time information feedback mechanism for continuous MUCAs with OR type bids. Second, we consider MUCAs with XOR-type bids and provide a method for information feedback in this case also. Third, for both the OR and XOR formulations, we propose incremental implementations to speed up operations to encourage wider adoption of online MUCAs. Fourth, our work will make it possible to undertake experimental stu dies on bidder behavior in MUCAs, which could help in better design of MUCAs in future.

The work described here has several managerial implications. The inadequacy of information feedback mechanisms for MUCAs has compelled auction designers to persist with single-item multi-unit auctions. The adoption of the more eficient and user-friendly schemes proposed here will help managers to improve their sales and procurement strategies. The issue of bidder acceptance [9] will be better addressed, and governments will be able to provide transparent allocation policies for public resources such as: i) frequency spectrum; ii) geographical regions on land and sea for geological prospecting; iii) funding of public welfare schemes such as those for combating climate change; etc. Online auction websites that sell multiple units of complementary items, like samsclub.com and ubid.com, can now allow MUCA bids so that customer expectations are more fully satisfied.

The paper is organized as follows. In Section 2, we survey the extant literature on CAs. In Section 3, we discuss the properties of MU-OR CAs, and in Section 4 we present our scheme for calculating winner and deadness levels for MU-OR CAs. Theoretical and experiment results are provided in Sections 5 and 6. The methods developed for MU-OR CAs in Sections 4–6 are extended to MU-XOR CAs in Section 7. Section 8 dis cusses the impact of feedback on bidding behavior, and Section 9 concludes the paper. A table of notation is provided in the Appendix A.

## 2. Literature review

Interest in CAs was triggered when the FCC decided to experiment with package bidding in frequency spectrum auctions in 2004 [27,28]. In spite of the obvious advantages of CAs, the inherent cognitive complexity of the mechanism has discouraged wide-scale implementation. Bidders find it dificult to estimate the bid values of packages, as the number of packages increases exponentially with the number of items [9,11]. This is known as the valuation problem [29]. Single round CAs, such as the first price sealed bid CA and the VCG auction [30–32], sufer from certain limitations, in addition to the valuation problem, that render them unsuitable for use in practice. The first price sealed bid CA forces bidders to speculate about the bids placed by other bidders thereby encouraging underbidding [16]; the VCG auction on the other hand may at times result in very low revenue for the seller [33].

In multi-round CAs, bidders get an opportunity to revise their bids on packages before each round, and this addresses the valuation problem to a certain extent. An Ascending Proxy Auction [16] such as iBundle [17] allows multi-round package bidding using specific rules for fixing minimum prices of items at the start of each round. Porter et al. [34] proposed an alternative scheme called the Combinatorial Clock auction, which is simple and requires little computation, and can handle multiple units of items. The two-phase Clock Proxy auction [16,35] is an improvement on the Combinatorial Clock auction. In another scheme called Resource Allocation Design (RAD) [10], after bidders submit bids on packages, provisional allocations are determined and appropriate item prices are computed by solving a set of linear programs. The bidders then place fresh bids in the next round. However, allowing bid revision at the start of each round does not quite solve the problem of bid construction [10,21].

Adomavicius et al. [19] proposed the lower (DL) and upper (WL) bounds as real-time information feedback to bidders in single-unit online OR CAs. This work has been extended [20] to XOR CAs and to single item multi-unit CAs [21], but has remained unsolved for MUCAs. Research on multi-unit CAs has concentrated mostly on solving the WDP $[ 1 4 , 3 6 , 3 7 ]$ . The few implementations that are recorded in the literature are mostly from B2B procurement auctions. These are mainly discount auctions which allow suppliers to ofer discounts on quantities of items. These auctions try to make it possible to express complex multi-dimensional bids, and often impose restrictions on bidders. Implementation of multi-unit CAs can be traced back to the procurement auction that was designed by the Mars-IBM team [23]. This auction allowed bidders to place bids on packages as well as quantity-discount bids. Goosens et al. [38] have studied a procurement auction where suppliers can ofer independent discount rates on distinct products and price functions. MUCAs have also been implemented in the transportation domain. Remli and Rekik [24] studied a truckload transportation auction, where carriers (here bidders) are allowed to express preferences for serving transportation lanes. MUCAs are also becoming popular in the domain of natural resource management, for example, procurement of conservation services, water buybacks, climate change management schemes, fishing quota allocations, etc. [25]. To the best of our knowledge, no implementation is currently available for continuous multi-item multi-unit CAs.

Single item single-unit (SISU) online auctions, such as eBay auc tions, have been studied extensively in the literature. Lucking-Reilly [39] presented a comprehensive study of online auctions since 1993. The work suggests that one of the reasons for the popularity of online auctions is that these allow bidders to bid at any time during the auction. A number of researchers have worked on improving the design of online auctions to achieve higher economic eficiency $[ 1 0 , 1 5 , 4 0 , 4 1 ]$ Design of decision support systems for online auctions has also received attention. In one of the earlier works in this domain, Gregg and Walczak [42] developed an agent-based DSS called Auction Advisor to help bidders decide on which items to bid on, which websites to buy/sell items on, and how much to bid on an item. Hsieh [43] proposed an information revelation scheme for a buyer which can be used to guide sellers to generate winning bids in a reverse CA. Yang et al. [44] looked at decision support for multi-attribute auctions using the preference elicitation approach and designed an interactive agent to implement it. There are some studies on bidder support tools for multi-unit CAs [45,46]. These suggest probable bid combinations that can be a part of the winning allocation. However, these support tools do not ofer any suggestions on the amount to bid on a package.

Existing work on providing real-time information feedback to bidders in an online CA has considered either single units of multiple heterogeneous items or multiple units of a single item. Adomavicius et al. [19] addressed the problem for single unit CAs for the OR formulation, and Petrakis et al. [20] examined the XOR case. Recently, Adomavicius et al. [21] have proposed methods to determine the DL and WL values for multiple units of a single item in both the OR and XOR cases. However, no method is available for determining package DL and WL values in MUCAs. To bridge this research gap, we here propose a DSS for MUCAs that covers both the OR and XOR formulations.

## 3. MU-OR formulation: properties of MDL

Let S be a multi-set of items on auction containing, for each item i, η (S) identical units of the item; $\eta _ { i } ( S ) ~ > ~ { \cal 0 }$ for every item i present in S. We assume items are not substitutable. Any non-empty subset of S can be called a package. The auction starts at time instant 1 and ends at some time instant $T > 1 ,$ , the bids on packages (subsets of S) arriving in a strict chronological order. A bid $B = ( j , q , \nu , t )$ is a quadruple where j is the bidder, q is the package, v is the non-negative integer value of the bid placed by j on q, and t is the time instant at which the bid is placed. A package q contains $\eta _ { i } ( q )$ copies of each item i belonging to $s ,$ where $0 \leq \eta _ { i } ( q ) \leq \eta _ { i } ( S )$ . For example, given $\boldsymbol { S } = \lbrace \boldsymbol { X } ^ { 4 } \boldsymbol { Y } ^ { 4 } \rbrace$ containing 4 units of X and 4 units of $Y , \{ X \} , \{ X ^ { 2 } Y \} , \{ X ^ { 2 } Y ^ { 3 } \} , \{ X ^ { 3 } Y ^ { 3 } \} , \{ X ^ { 4 } Y ^ { 3 } \}$ are packages on which bids might be placed. We use j(B), q(B), v(B) and t(B) to refer to the bidder, the package, the value and the time instant of bid B respectively. Bids are placed by bidders on packages $q _ { 1 } , \ q _ { 2 } , \ . . . , \ q _ { T }$ at successive time instants $1 , 2 , . . . , T ,$ , where the packages are not necessarily distinct. Let us consider p to be a package on which bids may or may not have been placed, $0 \leq \eta _ { i } ( p ) \leq \eta _ { i } ( S )$ for every item i be longing to S. The packages of some of the bids might fit into $p .$ So, $p$ might be partly filled or fully filled by packages on which bids have been made. In the above example, suppose p is $X ^ { 3 } Y ^ { 3 }$ . While filling up p, we only consider the bids on $\{ { \bar { X } } \} , \{ X ^ { 2 } { \bar { Y } } \} , \{ X ^ { 2 } Y ^ { 3 } \} , \{ X ^ { 3 } Y ^ { 3 } \}$ and not the bid on $\{ X ^ { 4 } Y ^ { 3 } \}$ . The combinations $\{ X \} , \ \{ \{ X \} , \ \{ X ^ { 2 } Y \} \} , \ \{ \{ X ^ { 2 } Y \} \} , \ \{ X ^ { 2 } Y ^ { 3 } \} \} , \ \{ X ^ { 2 } Y \}$ $\{ X ^ { 2 } ~ Y ^ { 3 } \}$ and $\{ X ^ { 3 } ~ Y ^ { 3 } \}$ can be used to fill up p. The objective is to maximize the seller's revenue. This depends on how best the packages $q _ { k }$ of the bids can be packed into S. We assume that winning bidders pay their bid values at the end of the auction. In the OR formulation a bidder can win any number of packages, so the bidder's identity can be omitted from the bid [47].

Definition 1. MWDP(p,t): Let $p$ represent a package which is a non empty subset of S. Of the packages $q _ { k }$ on which bids have been placed, $1 \leq k \leq t ,$ we consider only the packages which satisfy $q _ { k } \subseteq p .$ . We fit the packages $q _ { k } , 1 \le k \le t ,$ into $p ,$ no ${ \bf q } _ { \bf k }$ being used more than once, ensuring for each item i that the number of units put into $p \mathrm { i } \mathbf { s } \le \mathsf { \eta } _ { \mathrm { i } } ( \mathsf { p } )$ There can be many combinations of packages that satisfy the constraints, each of which will belong to the set of feasible allocations $C _ { p , t } . \ M W D P ( p , t )$ is the maximum sum obtainable of the bid values of packages across all allocations, i.e., $\begin{array} { r l } { M W D P ( p , t ) } & { { } = } \end{array}$ $\begin{array} { r } { \mathbf { M a x } _ { \mathrm { C \in C _ { p , t } } } \sum _ { \mathrm { b i d } \mathrm { B } \in \mathrm { C } } \mathbf { v } ( \mathbf { B } ) } \end{array}$ . □

While no $q _ { k }$ is used more than once when filling up $p ,$ the same package (occurring as two diferent $q _ { k } { } ^ { \prime } s$ in the bid sequence) might get included more than once in $p ,$ which cannot happen in the single-unit case. So more than one bid on the same package can be simultaneously active at a time $t ,$ and these bids can be considered independently for inclusion in winning combinations.

Definition 2. a) $M W L ( p , t ) \mathrm { : }$ The Multi-unit Winning Level of a package p at time instant t is the smallest (non-negative) bid value v(B) that makes bid B on p at instant $t ~ + ~ 1$ a member of a provisional winning combination of packages at instant $\ t \ + \ 1$ . Formally, $M W L ( p , t ) \ =$ argmin : $B = ( j , p , \nu , t + 1 ) ,$ , B is a member of a provisional winning combination at instant $t ~ + ~ 1$ . In the OR case a bidder can win any number of packages so $M W L ( p , t )$ is not bidder dependent; this is also true for $M D L ( p , t )$ defined below.

b) MD $\mathbf { \nabla } \cdot ( p , t ) \mathbf { \{ } $ The Multi-unit Deadness Level of a package $p$ at time instant t is the smallest (non-negative) bid value v(B) that makes bid B on p at instant $t + 1$ a member of a provisional winning combination of packages at some instant $t _ { 1 } ~ \geq ~ t ~ + ~ 1$ . There might exist multiple hypothetical sequences of bids between $t + 1$ and $t _ { I }$ that put B in a provisional winning combination of packages at instant $t _ { 1 } .$ . Formally, MDL $( p , t ) \ = \ a r g m i n _ { \nu } \colon \exists \ t _ { 1 } \geq t \ + \ I \colon B \ = \ ( j , \ p , \ \nu , \ t + \ 1 )$ is a member of a provisional winning combination at instant $t _ { 1 } .$

These two definitions are similar in form to the corresponding ones for single-unit CAs in [19.20]. but the multi-unit versions have some: what diferent properties. A bid of value $\nu ( B ) = M W L ( p , t )$ on $p$ at instant $t + 1$ ensures that bid B is in a winning combination at instant $t + 1$ , while a bid of value $\nu ( B ) = M D L ( p , t )$ on p at instant $t + 1$ implies that there exists a possible continuation of the auction such that bid B is in a winning combination at a future instant (see Example 3). The time parameter t is sometimes suppressed below when no misunderstandings can arise, as also the symbol B in $\nu ( B ) , p ( B )$ and t(B). So, in the OR formulation, we can represent a bid as $( q , \nu )$ when the time instant is understood.

Table 2  
Values of MWL(p,t) and MDL(p,t) in Example 3.

<table><tr><td colspan="8"> $S = X^{8}Y^{8}, p = X^{2}Y^{2}, S \backslash p = X^{6}Y^{6}$ </td></tr><tr><td>Instant t</td><td>Package</td><td>Bid</td><td>MWDP(S)</td><td>MWDP(p)</td><td>MWDP(S\p)</td><td>MWL(p)</td><td>MDL(p)</td></tr><tr><td>3</td><td>X</td><td>30</td><td>75</td><td>30</td><td>75</td><td>0</td><td>0</td></tr><tr><td>4</td><td> $X^{3}Y^{5}$ </td><td>100</td><td>175</td><td>30</td><td>155</td><td>20</td><td>20</td></tr><tr><td>5</td><td> $XY^{2}$ </td><td>35</td><td>190</td><td>65</td><td>155</td><td>35</td><td>25</td></tr></table>

Example 3. Let the multi-set S of items consist of 8 units of X and 8 units of ${ \cal Y } ,$ and suppose that $T \ > \ 5 .$ For ease of notation we write $S \ = \ X ^ { 8 } Y ^ { 8 } .$ . Let the given sequence of bids (with the bidder's identity omitted) be $( X ^ { 2 } Y ^ { 2 } , 2 0 , 1 )$ , (X<sup>2</sup>Y,25,2), (X,30,3), $( X ^ { 3 } Y ^ { 5 } , 1 0 0 , 4 )$ and $( X Y ^ { 2 } , 3 5 , 5 ) ,$ , and let $p$ be the package $X ^ { 2 } Y ^ { 2 }$ .The values of $M W L ( p , t )$ and MDL(p,t) after each bid at instants 3, 4 and 5 are shown in Table 2. At instant 3, all the bids fit into S. A new bid of value 0 on p also fits into $S , s o M W L ( p , 3 )$ and $M D L ( p , 3 )$ are both 0. At instant $^ { 4 , }$ the bid of value 100 on $X ^ { 3 } Y ^ { 5 }$ increases MWDP(S,4) to $^ { 1 7 5 , }$ but MWDP(S\p,4) is only 155 because the four packages do not all fit into $S \backslash p$ . So $M W L ( p , 4 ) \ = \ 2 0$ since a bid of 20 on p now makes $( p , 2 0 , 4 + 1 )$ a part of the winning combination $\{ ( p , 2 0 , 4 \ + \ 1 ) , ( X ^ { 2 } Y , 2 5 , 2 ) , ( X , 3 0 , 3 ) , ( X ^ { 3 } Y ^ { 5 } , 1 0 0 , 4 ) \} ;$ MDL $( p , 4 )$ is also 20. At instant $^ { 5 , }$ the bid of 35 on the package $X Y ^ { 2 }$ changes MWDP(S,5) to 190. $M W L ( p , 5 )$ increases to 35, but $M D L ( p , 5 )$ is 25 because a bid of 25 on p at instant $5 + 1$ followed by (say) a bid of 100 on $X ^ { 4 } Y ^ { 4 }$ at $t \ > \ 6$ does not change MWDP(S) yielding the winning combination $\{ ( X ^ { 2 } Y ^ { 2 } , 2 5 , 5 + 1 ) , ( X , 3 0 , 3 ) , ( X Y ^ { 2 } , 3 5 , 5 ) , ( X ^ { 4 } Y ^ { 4 } , 1 0 0 , 6 ) \}$ and also the value of 65 for $M W D P ( X ^ { 2 } Y ^ { 2 } ) ;$ an exhaustive check shows that a smaller value of $M D L ( p , t )$ cannot be achieved. □

Multi-unit CAs difer in some ways from single-unit CAs. MWL has properties very similar to those of the single unit WL, but the properties of MDL listed below difer in some ways from those of $D L .$ . Properties 3 to 5 hold in the single unit case also, but Properties 1 and 2 do not. Properties 3 and 4 follow directly from the definitions. The proofs for Properties 1, 2 and 5 are given in the Appendix A.

Property 1. $\begin{array} { r } { { M D L } ( p , t ) \leq M { W D P } ( \mathrm { p , t } ) . } \end{array}$

Property 2. $M W D P ( p , t ) \ + \ M W D P ( S \setminus p , t ) \ \geq \ M W D P ( S , t ) .$

Property 3. $M D L ( p , t ) \leq M W L ( p , t ) = M W D P ( S , t ) \cdot M W D P ( S \setminus p , \mathrm { t } ) .$

Property 4. If a bid B of value less than $M D L ( p , t )$ is placed on p at instant $t + 1$ , then the bid B becomes dead (inactive) and plays no further role in the auction.

Property 5. For any package p, MDL(p,t) is non-decreasing in t.

The above results provide some interesting insights on multi-unit CAs and underline the diferences with respect to single-unit CAs. Property 1 implies that unlike single unit CAs where $D L ( p , t )$ is equal to $W D P ( p , t ) ,$ , in the multi-unit version the value of $M D L ( p , t )$ is sometimes less than $M W D P ( p , t )$ . The reason is that in multi-unit CAs each package may have multiple copies. ${ \bf { S 0 , } }$ while one copy of a package forms a part of the winning allocation, the other copies are still available to be included. Therefore. the $M D L ( p , t )$ will always be less than or equal to MWDP(p,t). For example, consider a combinatorial auction with two units of items $X$ and ${ \cal Y } ,$ and two bids on X: (X, 10, 1) and (X, 15, 2). In this case, the value of MWDP(X) is equal to 25 whereas MDL(X) is equal to 10. Therefore, for all cases where more than one bid on a package can be accommodated in $s ,$ the MDL of the package will be less than equal to the MWDP. Property 2 also brings out an important diference. For single unit $\mathbf { C A s } ,$ packages p and S\p are always disjoint, while it is not necessarily so for multi-unit CAs; a package can fit in both p and S

\p.

Property 3 states that the deadness level of a package for a multi unit CA will always be less than or equal to the winning level. This follows from the definitions of these levels. It also states that a bid equal to MWDP(S) - MWDP(S\p) at instant t, becomes the provisional winner in time instant $t + 1 .$ . Property 4 follows from the definition of MDL $( p , t ) ,$ and implies that a bid less than the deadness level is a dead bid. Property 5 implies that under the assumption that a bid cannot be withdrawn, the deadness level of a package cannot decrease during the course of the auction. This does not hold for the winning level which may decrease.

## 4. MU-OR CAs: computation of MDL

We now present a systematic method for determining package MDL values in MU-OR CAs. To compute MD $\mathbf { \Phi } _ { \cdot } ( p , t )$ for a package p the steps are as follows: At instant t, let $\Delta _ { t } = \{ q _ { k } , 1 \leq k \leq t \}$ be the multi-set of packages on which bids have been placed. (Some packages can appear more than once in Δ . Every element q in Δ has an associated bid value $\nu _ { k } . )$ We first use $\varDelta _ { t }$ to compute $M = M W D P ( S , t ) .$ , where M is a variable that stores the value of MWDP(S). We then create all subsets of $\varDelta _ { t }$ that fit into ${ \cal S } \backslash p ,$ view each of them as a package and put all of these in R along with the empty set; R is the set of all packages that fit into S\p and consist of a subset of packages from $\varDelta _ { t } , R _ { t }$ denotes the set R at time t. Let the elements of $R _ { t } \mathrm { b e } r _ { 1 } , r _ { 2 } . . . r _ { w } .$ . Every $r _ { k } , 1 \le k \le w _ { \mathrm { : } }$ , has a value μ(r ) which is the sum of the bid values of its constituent bids. Suppose we place a hypothetical bid $B ( s _ { k } )$ of value $M \cdot \mu ( r _ { k } )$ on package $s _ { k } = ( S \backslash p )$ $\setminus r _ { k }$ . Since p U $r _ { k } \mathrm { U } s _ { k } = S ( \mathrm { F i g }$ . 1), MDL(p,t) is the minimum over all k of the non-negative quantity $( B _ { k } + \mu ( r _ { k } ) + \nu ( s _ { k } ) - M )$ , where $B _ { k }$ is a subset of $( \varDelta _ { t } \backslash r _ { k } )$ of largest total value that fits into p.

The algorithm is summarized in Fig. 2 and illustrated in Example 4. Packages in (Δ \r ) get packed into p so that the total value $\mu ( p )$ is maximized. MDL(p,t) is obtained by varying $r _ { k }$ over all k to find the smallest value of μ(p) that satisfies all the above conditions.

Example 4. Suppose $S = X ^ { 9 } Y ^ { 9 } , p = X ^ { 3 } Y ^ { 3 }$ and $S \backslash p \ = \ X ^ { 6 } Y ^ { 6 } $ . Let the auction end at $T \ \geq \ 1 0 ,$ , and let $( X ^ { 3 } , 4 5 , 1 ) , \ ( Y ^ { 2 } , 5 0 , 2 ) , \ ( X ^ { 2 } Y ^ { 2 } , 7 5 , 3 )$ $( Y ^ { 3 } , 8 5 , 4 )$ be the first four bids. Table 3 shows the computation at instant 4 with values of $r _ { k } , s _ { k } , \mu ( r _ { k } ) , \nu ( s _ { k } ) _ { : }$ , M and newM-M. The algorithm considers a subset $r _ { k }$ that fits into S\p and places a hypothetical bid on $s _ { k } = ( ( S \backslash p ) \backslash r _ { k } )$ . By varying $r _ { k }$ it finds the bid on $s _ { k }$ that minimizes newM-M. Here this occurs when $r _ { k } = X ^ { 5 } Y ^ { 5 }$ . MDL(p,t) values at other instants are obtained in a similar way. □

We performed some additional experiments using illustrative data. Table 4 extends Example 4 and computes some more $M D L ( p , t )$ values, These, as can be seen, are non-decreasing in t. It also shows that MDL $^ { ( p , t ) }$ can change even when bids are placed on packages that do not fit into $p .$ No subset of existing bid values may add up to give $M D L ( p , t )$ (instant 6); the above two observations are not possible in the single unit case. In Table $^ { 5 , }$ the package q of Example 2 is kept fixed and its MDL value is computed as bids are placed on other packages at various instants of time.

## 4.1. Incremental implementation

Our objective is to speed up the Compute\_MDL() procedure by devising a way to determine MDL(p,t) incrementally. One way to achieve this is as follows. Let TABM be an array with two rows, one containing the package name and the other its current MWDP value. TABM initially contains all packages that fit into S that can be created from the given set of items (including the empty package); the MWDP values are initialized to zero. Assuming a is the number of items and m is the maximum number of copies of an item, $O ( ( m + 1 ) ^ { a } )$ memory is needed for TABM. The set $\varDelta _ { t }$ in Compute\_MDL() consists of packages on which bids have been placed at all instants $\leq t . \ \Delta _ { t }$ is a growing set; new packages get added to it at successive instants but no elements ever get deleted. The set $R _ { t }$ of packages also has the same property. When a new bid is placed, a package is added to $\varDelta _ { t }$ , and as a result, some packages might get added to $R _ { t } .$ Computations made at earlier instants do not get nullified, only some additional computations are needed for updating $M D L ( p , t )$ using the packages that have newly entered $R _ { t } .$ The incremental implementation below directly computes $M D L ( p , t ~ + ~ 1 )$ given the value of $M D L ( p , t )$ , the package $q _ { t + 1 }$ and the corresponding bid value v(B) of bid $B = ( j , q , \nu , t + 1 )$

<table><tr><td>p</td><td>$ r_{k} $</td><td>$ s_{k} = (S|p)|r_{k} $</td></tr></table>

Fig. 1. Partition of S into three parts

Step 1: MWDP values are initialized to zero. The leftmost entry in TABM is the empty package; the other packages are so ordered that if p, q are two packages with $p$ left of $q ,$ then q is not a subset of $p .$

Step 2: When a new bid $B = \left( q _ { b } \mathrm { ~ } \nu , t \right)$ is placed on a package $q _ { t }$ at instant t, the MWDP value of each package p in TABM must be updated in a right to left order using the recurrence

$$
M W D P (p, 0) = 0
$$

$$
M W D P (p, t) = M W D P (p, t - 1) \mathrm{if} q _ {t} \mathrm{isnotasubsetof} p, \mathrm{for} t > 0\tag{1}
$$

(2)

$$
M W D P (p, t) = \max \left\{M W D P (p, t - 1), M W D P (p \backslash q _ {t}, t) + \nu) \right\} \text {   if   } q _ {t} \text {   is   a   subset   of   } p\tag{3}
$$

Step 3: Once the MWDP values of all subsets of S have been updated, we compute $M D L ( p , t )$ making use of the function Compute\_MDL(). A new package q gets added to $\Delta _ { t - 1 }$ giving $\varDelta _ { t s }$ and one or more packages get added to $R _ { t - 1 }$ giving $R _ { t } .$ . (In some cases, $q _ { t }$ might be already present in $\Delta _ { t - 1 }$ so that $\Delta _ { t } = \Delta _ { t - 1 }$ and $R _ { t } = R _ { t - 1 } . )$ Since the value of $M D L ( p , t { - } 1 )$ is known, to get MDL(p,t) all we need to do is take each package r not present in $R _ { t - 1 }$ that has just entered $R _ { t s }$ compute the corresponding value of MWDP and update $M D L ( p )$ . The incremental computation can be further sped up by interleaving the computations of $M D L ( p , t )$ and $M W D P ( r , t ) . \ \bigsqcup$

## 5. Theoretical result

The objective of this section is to provide a proof of correctness for algorithm Compute\_MDL. We start by establishing a more basic result, namely, if package q is a subset of package r then $M D L ( q , t ) \leq M D L ( r , t )$ at every instant t. This proof does not depend on the computation procedure described above but makes use of a similar argument.

Result 1. Let q and r be packages where q is a subset of r. Then MDL $( q , t ) \le M D L ( r , t )$ at every instant t.

Proof: Suppose $M D L ( q , t ) = \gamma$ and $M D L ( r , t ) = \delta$ . We want to show that $\gamma \ \leq \ \delta .$ We divide S into three regions. The first region holds r exactly and the second region $r _ { 1 }$ contains a subset of Δ . Fig. 3 shows the packages and the corresponding bid values. Here, $\delta _ { 1 }$ is the sum of the bid values on the packages that constitute $r _ { 1 }$ . We choose the value of $\delta _ { 2 }$ in such a way that $\delta \ : + \ : \delta _ { 1 } \ : + \ : \delta _ { 2 } \ : = \ : M W D P ( S , t )$ where $M D L ( r , t ) = \delta .$ Some of the packages on which bids have been placed in the auction up to now have gone into the second region. Of the remaining ones, some will fit into $p ,$ but the total of their bid values cannot exceed δ.

To show that $\gamma \leq \delta ,$ , we now divide S into three parts, where the first part holds package q exactly, the second part $q _ { 1 }$ equals $r _ { 1 } ,$ and the third part $q _ { 2 } = ( S \backslash q ) \backslash q _ { 1 }$ as shown in the lower part of Fig. 3. The bids are the same as in the upper portion. Here too $\delta + \delta _ { 1 } + \delta _ { 2 } = M W D P ( S , t )$ . No dificulties arise since q is a subset of $r ,$ and it follows that $\gamma = M D L$ $\left( q , t \right) \leq \delta . \sqsupset$

We now present the second result. If $M D L ( p , t ) = \delta ,$ then a bid $( p , \delta ,$ $t + \mathbf { \nabla } \mathcal { 1 } )$ can combine with a hypothetical bid that ensures the bid $( p , \delta ,$ $t + \mathbf { \nabla } \mathcal { 1 } )$ is in the winning combination at a future instant $t + 2 .$

$$
\text {   Result   2.   Suppose   } (q _ {1}, \nu_ {1}, k _ {1}), (q _ {2}, \nu_ {2}, k _ {2}), (q _ {3}, \nu_ {3}, k _ {3}), \dots , (q _ {l}, \nu_ {l}, k _ {l}) \text {   is   the   }
$$

Table 3  
Table 4

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
function Compute_MDL(package p, instant t, set of bids  $\Delta_{t}$ )
{
    let MDL(p,t) = ∞; compute M = MWDP(S) from the set of bids  $\Delta_{t}$ ;
// the multiset  $\Delta_{t}$  contains all packages on which bids have been placed so far
    let R be the set of all packages that fit into Sp and consist of a subset of packages from  $\Delta_{t}$ ;
// R will also include the empty package that always fits into Sp;
for each package  $r_{k}$  in R //  $r_{k}$  can also be the empty package
    { let  $s_{k} = (S\backslash p)\backslash r_{k}$ ; // so p U  $r_{k}$  U  $s_{k} = S$ 
    let  $\mu(r_{k}) = \text{sum of the bid values of the packages in } r_{k}$ ;
    place a hypothetical bid  $B = M - \mu(r_{k})$  on  $s_{k}$ ;
    compute newM = MWDP(S) from the set  $\Delta_{t}$  U {  $s_{k}$ };
    compute MDL(p,t) = min { MDL(p,t), newM - M };
}
return MDL(p,t); }
</div>

Fig. 2. Computation of MDL(p,t) from the set of bid $\Delta _ { t } = \{ ( q _ { k } , \nu _ { k } , k ) , 1 \leq k \leq t \}$

Computation of MDL(p,4) for Example 2.

<table><tr><td colspan="6"> $S = {X}^{9}{Y}^{9},p = {X}^{3}{Y}^{3},S \backslash p = {X}^{6}{Y}^{6}$ </td></tr><tr><td colspan="6">Instant 4,  $M = {255},{\left( {X}^{3},{45},1\right) ,{\left( {Y}^{2},{50},2\right) ,{\left( {X}^{2}{Y}^{2},{75},3\right) ,{\left( {Y}^{3},{85},4\right) }}$ </td></tr><tr><td> ${r}_{k}$ </td><td> $\mu \left( {r}_{k}\right)$ </td><td> ${s}_{k} = \left( {S/p}\right) /{r}_{k}$ </td><td> ${bid}\left( {s}_{k}\right)$ </td><td>newM</td><td>newM-M</td></tr><tr><td> ${X}^{3}$ </td><td>45</td><td> ${X}^{3}{Y}^{6}$ </td><td>210</td><td>340</td><td>85</td></tr><tr><td> ${X}^{3}{Y}^{2}$ </td><td>95</td><td> ${X}^{3}{Y}^{4}$ </td><td>160</td><td>365</td><td>110</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> ${X}^{5}{Y}^{5}$ </td><td>205</td><td>XY</td><td>50</td><td>305</td><td>50</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr></table>

sequence of hypothetical bids at instants $k _ { 1 } , k _ { 2 } , . . . , k _ { l }$ needed to ensure that (p, MDL(p,t)) is in the winning allocation at some time instant ≥k . Here the k 's are greater than t + 1 and in increasing order. Then a bid $( p , M D L ( p , t ) , t ~ + ~ 1 )$ at time instant $\ t ~ + ~ 1$ followed by a bid on $( q _ { 1 } + q _ { 2 } + \ldots + q _ { l } )$ of value $( \nu _ { 1 } + \nu _ { 2 } + \ldots + \nu _ { l } )$ at time instant $t + 2$ ensures that (p, MDL(p,t)) is in the winning combination at time instant t + 2.

Proof: Immediate. □

Results 1 and 2 taken together imply that MDL(p,t) is in a certain sense well-behaved, since it is non-decreasing with time, and subsets of a package p have MDL values no larger than that of p. We now present the proof of correctness of the algorithm based on the previous two results.

Theorem. The procedure Compute\_MDL yields the correct value of MDL (p,t).

<table><tr><td rowspan="2">Instant t</td><td rowspan="2">Package q</td><td rowspan="2">Bid</td><td colspan="2">MDL(q)</td></tr><tr><td>Before bid</td><td>After bid</td></tr><tr><td>4</td><td> $Y^3$ </td><td>85</td><td>0</td><td>0</td></tr><tr><td>5</td><td> $X^4Y^3$ </td><td>125</td><td>50</td><td>95</td></tr><tr><td>6</td><td> $X^2Y^4$ </td><td>130</td><td>75</td><td>130</td></tr><tr><td>7</td><td>XY</td><td>55</td><td>0</td><td>10</td></tr><tr><td>8</td><td> $X^2$ </td><td>30</td><td>0</td><td>0</td></tr><tr><td>9</td><td> $X^2Y$ </td><td>85</td><td>20</td><td>30</td></tr><tr><td>10</td><td> $XY^2$ </td><td>100</td><td>25</td><td>50</td></tr></table>

<table><tr><td> $(r,\beta)$ </td><td> $(r_1,\beta_1)$ </td><td> $(r_2,\beta_2)$ </td></tr><tr><td> $(q,\beta)$ </td><td> $(q_1,\beta_1)$ </td><td> $(q_2,\beta_2)$ </td></tr></table>

Fig. 3. Proof of Result 1.

Proof. Suppose $M D L ( p , t ) = \delta .$ . Then by Result 2, at instant $t + 2$ there must exist packages (p, δ), (r, δ ), (s, δ ) as in Fig. 1 such that $p \ + \ r \ + \ s \ = \ S$ and $\delta \ : + \ : \delta _ { 1 } \ : + \ : \delta _ { 2 } \ : = \ : M \ : = \ : M W D P ( S , t )$ . Here r consists of packages from $\varDelta _ { t s }$ i.e., r is composed of packages on which bids have been placed at instants $\le t , \ \delta _ { 1 }$ is the sum of the corresponding bid values, and $\begin{array} { r } { \boldsymbol { s } = ( \boldsymbol { S } \backslash p ) \backslash \boldsymbol { r } . } \end{array}$ . By definition, δ must be the smallest bid value on p for which the above conditions are true. There are many possible choices for r. Compute\_MDL takes each such $( r , \delta _ { 1 } )$ pair and determines appropriate pairs (p, δ) and $( s , \delta _ { 2 } )$ . Since MWDP(S,t) has already been determined, given $\delta _ { 1 }$ we know the value of $\delta + \delta _ { 2 } ,$ but δ and $\delta _ { 2 }$ are not individually known to us. To overcome this problem, we place a hypothetical bid $( s , M \cdot \delta _ { 1 } )$ at instant $t \mathrm { ~ + ~ } 1$ and compute MWDP(S) afresh to get newM, which must be ≥M since an additional bid has been placed. We now work backwards. The quantity (newM – M) is subtracted from $M \cdot \delta _ { 1 }$ to give us $\delta _ { 2 } ,$ and a new bid (p, δ) is now placed, where $\delta \ = \ n e w M \ – \ M .$ The algorithm varies r and gets the minimum value of $\delta ;$ no combination of packages in $\Delta _ { t } \mathrm { \Delta } \ r _ { \mathrm { v } }$ have value that add up to a quantity greater than δ. □

Values of MDL(p,t) in Example 2.

<table><tr><td colspan="10"> $S = X^{9}Y^{9}p = X^{3}Y^{3}S\backslash p = X^{6}Y^{6}$ </td></tr><tr><td rowspan="2">Instant</td><td rowspan="2">Package</td><td rowspan="2">Bid</td><td colspan="2">MWDP</td><td rowspan="2">MWL(p,t)</td><td rowspan="2"> $r_{min}$  and  $\mu(r_{min})$ </td><td rowspan="2"> $s = ((S\backslash p)\backslash r_{min})$  hyp bid value on s</td><td rowspan="2">newM</td><td rowspan="2">MDL(p,t)</td></tr><tr><td>S</td><td>S\p</td></tr><tr><td>5</td><td> $X^{4}Y^{3}$ </td><td>125</td><td>330</td><td>210</td><td>120</td><td> $Y^{5} = (2) + (4) = 135$ </td><td> $X^{6}Y = 195$ </td><td>405</td><td>75</td></tr><tr><td>6</td><td> $X^{2}Y^{4}$ </td><td>130</td><td>350</td><td>225</td><td>125</td><td> $Y^{5} = (2) + (4) = 135$ </td><td> $X^{6}Y = 135$ </td><td>430</td><td>80</td></tr><tr><td>7</td><td>XY</td><td>55</td><td>360</td><td>260</td><td>100</td><td> $X^{4}Y = (1) + (7) = 100$ </td><td> $X^{2}Y^{5} = 175$ </td><td>445</td><td>85</td></tr><tr><td>8</td><td> $X^{2}$ </td><td>30</td><td>370</td><td>265</td><td>105</td><td> $X^{6}Y = (1) + (7) + (8) = 130$ </td><td> $Y^{5} = 145$ </td><td>465</td><td>95</td></tr><tr><td>9</td><td> $X^{2}Y$ </td><td>85</td><td>400</td><td>275</td><td>125</td><td> $X^{3}Y^{5} = (4) + (7) + (9) = 225$ </td><td> $X^{3}Y = 70$ </td><td>505</td><td>105</td></tr><tr><td>10</td><td> $XY^{2}$ </td><td>100</td><td>450</td><td>320</td><td>130</td><td> $X^{6}Y^{2} = (1) + (7) + (9) = 185$ </td><td> $Y^{4} = 135$ </td><td>580</td><td>130</td></tr></table>

Table 6  
![](/api/attachments/X32BVEY9/fulltext/images/04561f5b39b4123139c4c769c0318a690e2eafb7f0315008fe5892424dd8464c.jpg)  
Fig. 4. Variation of MDL, MWL and MWDP values of a package.

## 6. Experimental results

To test the Compute\_MDL algorithm, two sets of experiments were conducted. The first set was on simulated data and the second was on publicly available data.

## 6.1. Experiments on simulated data

100 auction instances of 10,000 bids each were generated. There were 7 items in each auction instance, and the number of units of an item ranged between 1 and 7. Out of 100 instances, we took 6 auction instances with a complexity score of < 100, and 6 where the complexity was very high (> 450). Close to 40% of the auctions instances had a complexity score between 200 and 300. For each auction instance the Compute\_MDL algorithm determined the MDL values of 10 randomly selected packages, and processed 10 million bids in all. All the experiments in this study were conducted on a 64-bit Windows PC having Intel core i5-4440 CPU @3.10 GHz and 4 GB memory. Fig. 4 shows how the MWDP, MWL and MDL values of a package in one of the 100 instances varied during the first 1000 bids.

The efect of an increase in the number of units of an item in S on the computation time of MDL values was also examined. The complexity score for an auction instance was computed using the formula $[ \sum _ { i } 2 ^ { \eta _ { i } }$ ] where $\eta _ { i }$ is the number of available units of item i. Table 6 shows the average time taken to process 10,000 bids for diferent levels of complexity. The scatter plot in Fig. 5 depicts the change in the runtime of Compute\_MDL with the complexity. It can be seen that the runtime increases exponentially with the complexity. However, the system could process 10,000 bids for fairly complex instances in < 2000 s, which is roughly equivalent to < 0.2 s per bid. This indicates that the system can meet the expected performance standards of a continuous (online) CA. Schefel et al. [48] reported that bidders generally bid on a fraction of the packages in a combinatorial auction. The same was confirmed later by Adomavicius [19]. Thus, it can be assumed that for an online multi-unit CA the complexity won't be much more than what we have tested it on; indeed, in the UK spectrum auction (discussed below) the complexity was much less than our experimental simulation tests.

Change in average runtime with complexity.

<table><tr><td>Complexity score</td><td>No. of auction instances</td><td>Average time (secs)</td></tr><tr><td>&lt; 100</td><td>6</td><td>29.74</td></tr><tr><td>101–150</td><td>9</td><td>48.84</td></tr><tr><td>151–200</td><td>13</td><td>146.08</td></tr><tr><td>201–250</td><td>20</td><td>149.75</td></tr><tr><td>251–300</td><td>18</td><td>237.81</td></tr><tr><td>301–350</td><td>13</td><td>246.87</td></tr><tr><td>351–400</td><td>11</td><td>448.78</td></tr><tr><td>401–450</td><td>6</td><td>718.52</td></tr><tr><td>&gt; 450</td><td>4</td><td>1650.58</td></tr></table>

![](/api/attachments/X32BVEY9/fulltext/images/8b7029f2f21efff7a807ecfc21b02006d766193f45f811588c756e8ea60dd66b.jpg)  
Fig. 5. Average time taken by Compute\_MDL vs complexity.

## 6.2. Experiments on real life data

As an additional test of the incremental procedure in Section 4, we ran the programs on publicly available bid data<sup>2</sup> obtained from a frequency spectrum auction held in the U.K. in January 2013 [22]. There were 6 items and 7 bidders. Five of the items had multiple units. A twophase Combinatorial Clock algorithm found the winners. A total of 615 bids were placed by the bidders. In the Clock (or price discovery) phase, the prices of individual items were varied by the auctioneer to match supply with demand. A total of 338 bids were placed in this phase. The Supplementary (i.e., second) phase involved a one-round sealed bid combinatorial auction, and 277 separate bids were placed in this phase.

To conform to our model of an online multi-unit CA, we interpreted the available bid data as a time sequence of 615 separate bids. A winning combination was found in the OR formulation, and the MWDP,

![](/api/attachments/X32BVEY9/fulltext/images/aa6ec8553d405a9df3da2e71fe26bffc7d8821814c59c4530bedeba7bc247766.jpg)  
Fig. 6. (a) Variation of MDL,MWL,MWDP and (b) Incremental Runtime for a package.

MWL and MDL values at diferent time instants were noted for a win ning package containing two units of Item 1 and four units of Item 3. The plots in Fig. 6(a) show the variations of the parameter values with time. The increase of the incremental run time with number of bids for the same package is also shown in Fig. 6(b). The absolute incremental time was of the order of a fraction of a second. As seen with simulated data, MDL and MWDP values are non-decreasing with time while the MWL values fluctuates with time. The experimental findings are con sistent with the theoretical results in the earlier sections.

## 7. The MU-XOR Problem

In this section we discuss multi-unit combinatorial auctions (MUCAs) with XOR bid type, or MU–XOR auctions. In this formulation, no bidder can win more than one package, i.e., packages in a winning combination come from bids by diferent bidders. Thus the bidder's identity must be included in a bid. This constraint on winning bids makes it harder to determine the MDL and MWL values of package [20,49]. We make the same general assumptions as in the OR case (Section 3). Bids and packages are defined as before. The objective is to maximize the seller's revenue. We assume that winning bidders pay their bid values at the end of the auction. When we need to distinguish a parameter or notation in MU-XOR from one in MU-OR, we add a superscript XOR on the name.

![](/api/attachments/X32BVEY9/fulltext/images/951a5e804f99ccf07a22e8dc5102bc007b19bca13f98bf8d28d452467f78754a.jpg)

Definition 3 $\therefore M W D P ^ { X O R } ( p , t ) :$ Let $p$ represent a package which is a non empty subset of S. Of the packages $q _ { k }$ on which bids have been placed, $1 \leq k \leq t ,$ we consider only the packages which satisfy $q _ { k } \subseteq p$ . We fit the packages $q _ { k } , 1 \le k \le t ,$ , into p, no $q _ { k }$ being used more than once and each $q _ { k }$ from a diferent bidder, ensuring for each item i that the number of units put into $p \ \mathrm { \ i } s \ \leq \eta _ { i } ( p )$ . There can be many combinations of packages that satisfy the constraints, each of which will belong to the set of feasible allocations, $C _ { p . t } ^ { \phantom { + } X O R }$ , no bidder appearing more than once. $M W D P ^ { X O R } ( p , t )$ is the maximum sum obtainable of the bid values of packages across all allocations, $\begin{array} { r l r l } { \mathrm { i . e . , } \ } & { { } M W D P ^ { X O R } ( p , t ) } & { } \end{array} \ =$ $\begin{array} { r } { \mathbf { M a x } _ { \mathrm { C } } \mathrm { x o r } _ { \in \mathrm { C } _ { \mathrm { p , t } } ^ { \mathrm { X O R } } } \sum _ { \mathrm { b i d } \ \mathbf { B } \in \mathrm { C } ^ { \mathrm { X O R } } } \mathbf { v } ( \mathbf { B } ) . } \end{array}$ . □

The $M W L ^ { X O R }$ and $M D L ^ { X O R }$ values of packages in MU-XOR, unlike those in MU-OR, depend not only on the time instant but also on the bidder. The definitions are given below.

Definition 4. a) $M W L ^ { X O R } ( p , j , t ) \colon$ The Multi-unit Winning Level of package p for bidder j at time instant t in the XOR case is the smallest (nonnegative) bid value v(B) that makes bid B on p by bidder j a time instant $t + 1$ a member of a provisional winning combination of packages at time instant $t + 1$ , each bidder contributing at most one bid. Formally,

MW $\begin{array} { r } { \boldsymbol { L } ^ { X O R } ( p , j , t ) = a r g m i n _ { \nu } \colon B = ( j , p , \nu , t + 1 ) } \end{array}$ such that B is a member of a provisional winning combination (with distinct bidders) at instant $t + 1 .$

b) $M D L ^ { X O R } ( p , j , t ) \colon$ The Multi-unit Deadness Level of package p for bidder j at time instant t in the XOR case is the smallest (non-negative) bid value $\nu ( B )$ that makes bid B by bidder j on p at instant $t \mathrm { ~ + ~ } 1$ a member of a provisional winning combination of packages at some instant $t _ { 1 } \geq t + 1$ . There might exist multiple hypothetical sequences of bids between $t + 1$ and t that put B in a provisional winning combination of packages at instant $t _ { 1 } .$ . Formally, ${ \cal M D L } ^ { X O R } ( p , j , t ) = a r g m i n _ { \nu } \mathrm { : }$ ∃ $t _ { l } \geq t + 1 \colon B = ( j , p , \nu , t + 1 )$ such that B is a member of a provisional winning combination (with distinct bidders) at instant $t _ { 1 } . \boxed { }$

Example 5. Suppose $S = \{ X ^ { 2 } \}$ and let there be two bids $( 1 , X , 1 0 , 1 )$ and (2, X, 15, 2). Here, under XOR formulation, bidders 1 and 2 cannot have more than one bid in the winning allocation. So, $M D L ^ { X O R } ( X , 1 , 2 )$ is 10 whereas $M D L ^ { X O R } ( X , 2 , 2 )$ is 15. In contrast, under OR formulation, MDL (X,2) is 10, independent of the bidders. □

Example 6. We use the notation of Section 4 with appropriate changes. Suppose there are two items X and Y on auction, and let $\scriptstyle { S } \ = \ X ^ { 9 } Y ^ { 9 }$ There are four bidders numbered 1 through 4 who place bids on packages that are subsets of S at time instants $1 , 2 , . . . , 1 0$ (see Table 7). The package of interest is $p \ = \ X ^ { 3 } Y ^ { 3 }$ . Values of $^ { ( p , t ) }$ are shown at diferent time instants, as well as the values of $\bar { M } W L ^ { X O R } ( p , j , t )$ and $M D L ^ { X O R } ( p , j , t )$ for the first two bidders. □

The table entries have been computed as follows. $M W D P ^ { X O R } ( S , t )$ and $M W D P ^ { X O R } ( p , t )$ can be obtained by identifying the bids, at most one per bidder, that fit in to $S = X ^ { 9 } Y ^ { 9 } \left( \mathrm { o r } p = X ^ { 3 } Y ^ { 3 } \right)$ and yield the largest total value. For example, when $t = 9 ,$ , the largest total of 355 for S is obtained by taking the bids 1, 4, 6 and 9. To compute $M W L ^ { X O R } ( p , 1 , 9 )$ , we have to determine the smallest bid that bidder 1 can place at instant $1 0 ~ = ~ 9 ~ + ~ 1$ on $p = X ^ { 3 } Y ^ { 3 }$ , which, together with the largest total obtainable within $X ^ { 6 } Y ^ { 6 }$ at instant 9 from at most one bid by each of the other bidders 2, 3 and 4, add up to $M W D P ^ { X O R } ( p , 9 )$ ). We find that the largest total of 255 within $X ^ { 6 } Y ^ { 6 }$ is the sum of the bids 6 by bidder $^ { 4 , }$ 8 by bidder 3 and 9 by bidder 2, which together with a bid by bidder 1 of 100 on $p$ gives a total of 355. The calculations for $M W L ^ { X O R } ( p , 2 , t )$ are similar.

To compute $M D L ^ { X O R } ( p , 1 , t )$ we make use of hypothetical bids. Suppose $t = 9 .$ It is clear that since bidder 1 has already placed a bid of 75 at instant 3 on the package $X ^ { 2 } Y ^ { 2 }$ that fits in to $p ~ = ~ X ^ { 3 } Y ^ { 3 } ,$ $M D L ^ { X O R } ( p , 1 , 9 )$ cannot be $< 7 5 ;$ we do not consider bid number $^ { 5 , }$ since the corresponding package does not fit into $p .$ We have already seen that $\begin{array} { r l r } { M W L ^ { X O R } ( p , 1 , 9 ) \quad } & { { } = } & { \quad 1 0 0 , \qquad s \mathbf { o } \qquad \mathrm { i t } } \end{array}$ follows that

Table 7  
Values of MU-XOR auction parameters $( { \cal S } = { \cal X } ^ { 9 } Y ^ { 9 } , p = { \cal X } ^ { 3 } Y ^ { 3 } ,$ 4 bidders).

<table><tr><td>Time</td><td>Bidder, package, bid value</td><td> $MWDP^{XOR}(S,t), MWDP^{XOR}(p,t)$ </td><td> $MWL^{XOR}(p,1,t)$ </td><td> $MDL^{XOR}(p,1,t)$ </td><td> $MWL^{XOR}(p,2,t)$ </td><td> $MDL^{XOR}(p,2,t)$ </td></tr><tr><td>1</td><td> $1, X^3, 45$ </td><td>45, 45</td><td>45</td><td>45</td><td>0</td><td>0</td></tr><tr><td>2</td><td> $2, Y^2, 50$ </td><td>95, 95</td><td>45</td><td>45</td><td>50</td><td>50</td></tr><tr><td>3</td><td> $1, X^2Y^2, 75$ </td><td>125, 95</td><td>75</td><td>75</td><td>50</td><td>50</td></tr><tr><td>4</td><td> $3, Y^3, 85$ </td><td>210, 130</td><td>75</td><td>75</td><td>50</td><td>50</td></tr><tr><td>5</td><td> $1, X^4Y^3, 125$ </td><td>260, 130</td><td>125</td><td>75</td><td>50</td><td>50</td></tr><tr><td>6</td><td> $4, X^2Y^4, 130$ </td><td>310, 130</td><td>130</td><td>75</td><td>100</td><td>50</td></tr><tr><td>7</td><td> $2, XY, 55$ </td><td>315, 130</td><td>130</td><td>75</td><td>105</td><td>55</td></tr><tr><td>8</td><td> $3, X^2, 30$ </td><td>340, 130</td><td>125</td><td>75</td><td>105</td><td>55</td></tr><tr><td>9</td><td> $2, X^2Y, 95$ </td><td>355, 130</td><td>100</td><td>75</td><td>120</td><td>95</td></tr><tr><td>10</td><td> $4, XY^2, 100$ </td><td>405, 195</td><td>125</td><td>75</td><td>170</td><td>95</td></tr></table>

$7 5 \le M D L ^ { X O R } ( p , 1 , 9 ) \le 1 0 0 . ~ \mathsf { A }$ hypothetical bid of 55 on the package $X ^ { 2 } Y$ at time instant 10 by bidder 3, together with bids 6 and $^ { 9 , }$ ensure that a total of 280 is achieved within ${ \bar { X } } ^ { 6 } Y ^ { 6 } ,$ which when added to the bid of 75 by bidder 1 on p yields the required value of 355. Similar arguments can be given in all the other cases. □

## 7.1. Computation of MWDP<sup>XOR</sup>

Fast computations of $M W D P ^ { X O R }$ values of packages become possible when an incremental dynamic programming scheme is employed. To keep track of bidders and their bids, we introduce the following notation. Let N be the set of all bidders, and let D be any subset of N. |N| ndicates the number of bidders in N. Let the bid at instant t be $( j , q , \nu , t )$ The packages p and q are subsets of S. $M W D P ^ { X O R } ( p , D , t )$ refers to the $M W \bar { D P } ^ { X O R }$ value for package p at instant t taking into account only the bids placed by bidders in set D. Therefore, $M W D P ^ { X O R } ( p , N , t ) ~ = ~ \bar { M } W D P ^ { X O R } ( S , ~ t ) .$ In Example $^ { 6 , }$ if $\begin{array} { r } { p \ = \ X ^ { 3 } Y ^ { 3 } } \end{array}$ $D = \{ 2 , 3 \}$ , and $t = 9 ,$ , we get M $U D P ^ { X O R } ( p , D , 9 ) = 9 5 .$

The $M W D P ^ { X O R }$ value of every package p for every choice of D is initialized to 0 at instant 0. The dynamic programming formulation given below holds for every p that is a subset of S (including S) and every D that is a subset of $\mathbf { \delta } _ { N , \bullet }$ when a new bid $B = ( j , q _ { t } , \nu , t )$ is placed on a package q at instant t,

$$
M W D P ^ {X O R} (p, D, 0) = 0\tag{4}
$$

$$
M W D P ^ {X O R} (p, D, t) = M W D P ^ {X O R} (p, D, t - 1)
$$

if $\dot { } q _ { t }$ >p j D tis not a subset of or is not in , for 0

$$
M W D P ^ {X O R} (p, D, t) = \max \{M W D P ^ {X O R} (p, D, t - 1), v + M W D P ^ {X O R} (p \backslash q _ {t}, D \backslash \{j \}, t - 1) \},\tag{5}
$$

$\operatorname { i f } q _ { t }$ >p j D tis a subset of and is in , for 0

(6)

Here, $p \backslash q _ { t }$ refers to the package that remains when $q _ { t }$ is subtracted from p. So $\left( 5 \right) - \left( 6 \right)$ states that when q is a subset of $p$ and j is in $D ,$ the $M W D \bar { P } ^ { X O R }$ value of p at instant t is the maximum of the $M W D P ^ { X O R }$ value of $p$ at instant t-1, and the $M W D P ^ { X O R }$ value of $p \backslash q _ { t }$ at instant t-1 taking into account bids by all bidders in D except j, augmented by an amount v. When we write $M W D P ^ { X O R } ( S , t )$ or $M W D P ^ { X O R } ( p , t )$ , we mean $D \ = \ N .$ From Example $^ { 6 , }$ since the bid at instant 9 is $( 2 , X ^ { 2 } Y , 9 5 , 9 )$ , the recurrence gives

$$
M W D P ^ {X O R} (S, 9) = \max (M W D P ^ {X O R} (S, \{1, 2, 3, 4 \}, 8), 9 5 +
$$

$$
M W D P ^ {X O R} (S \backslash X ^ {2} Y, \{1, 3, 4 \}, 8)
$$

$$
\begin{array}{l} = \max (3 4 0, 9 5 + M W D P ^ {X O R} (X ^ {7} Y ^ {8}, \{1, 3, 4 \}, 8) = \max (3 4 0, 9 5 + 2 6 0) \\ = 3 5 5 \end{array}
$$

Thus to determine the $M W D P ^ { X O R }$ value of $p$ at instant t we would need to know the MW $\mathcal { D P } ^ { X O R }$ values at instant t-1 of various subsets of p for various subsets of N.

7.2. Computation of $M D L ^ { X O R }$

We first present some important properties of $M W D P ^ { X O R } ,$ , MWL<sup>XOR</sup> and $M D L ^ { X O R }$ . For any subset p of S and any set D of bidders at any instant $t ,$ the following properties hold:

$$
\text { Property   6. } M W L ^ {X O R} (p, j, t) = M W D P ^ {X O R} (S, t) - M W D P ^ {X O R} (S p, N \backslash \{j \}, t);
$$

Property 7. $M D L ^ { X O R } ( p , j , t )$ is non-decreasing in t;

Property 8. $M D L ^ { X O R } ( p , j , t ) \ \leq \ M W L ^ { X O R } ( p , j , t ) .$

Property $\harpoonright . M W L ^ { X O R } ( p , j , t ) \ \leq \ M W D P ^ { X O R } ( p , N , t )$ at every instant t (see Table 7).

Property 10. For a bidde $^ { \dag , }$ it is possible that:

$$
\begin{array}{l} \text {a) MWL} ^ {X O R} (p, j, t) \geq M W D P ^ {X O R} (p, \{j \}, t); \\ \text {b) MDL} ^ {X O R} (p, j, t) \geq M W D P ^ {X O R} (p, \{j \}, t) \end{array}
$$

Properties 6–9, though there is a bidder dependence, have similarities with Properties 1–5 (OR case). Property 10 states that the winning level and deadness level of a package p for a bidder j can be greater than the $M W D P ^ { X O R }$ value computed with bids of bidder j at a time instant t. In Example 5, $M W D P ^ { X O R } ( X ^ { 2 } , 1 , 2 )$ is 10, whereas $M D L ^ { X O R } ( X ^ { 2 } , 1 , 2 )$ is 25.

To determine $M D L ^ { X O R } ( p , j , t )$ we split up S\p into atomic cells on each of which bidders can place bids (see [20]). Suppose, $\begin{array} { r } { s { \bf \Psi } = { \bf \Psi } X ^ { 9 } Y ^ { 9 } , } \end{array}$ $p = X ^ { 3 } Y ^ { 3 } , S \vee p = X ^ { 6 } Y ^ { 6 }$ . We split up S\p into 12 atomic cells, six of size X and six of size $\boldsymbol { Y } ,$ making it possible to accommodate up to 12 bidders in addition to j whose bid $M D L ^ { X O R } ( p , j , t )$ on p would make j a winner in future. Let there be r atomic cells in $S \backslash \boldsymbol { p } .$ . Two cases arise:

Case 1: |N| - 1 ≤ r.

We place hypothetical bids on behalf of each bidder, $k ,$ except j on atomic cells (like package X Y); for bidder k the bid is at least as large in value as the highest-valued bid placed by k on any package up to instant t. For j we take the highest-valued bid placed by j on a package that fits into $p .$ We ensure that the total of all the selected bids equals $M W D P ^ { X O R } ( S , t )$ and the total size adds up to S. This is the situation that arises in Example 7 and gives us the $M D L ^ { X O R }$ values shown.

Case $2 \colon | \mathbf { N } | \cdot 1 > r .$

When the number of bidders exceeds the number of atomic cells in S $\setminus ,$ there is a combinatorial explosion. Suppose the r atomic cells in $S \Psi$ to be allotted to s bidders (apart from j) where $s > r .$ Then hypothetical bids cannot be assigned to all the s bidders. If a bidder has a hypothetical bid assigned then the bidder is said to be blocked, otherwise she is free. Since a free bidder k might be able to squeeze in a bid into $p ,$ this imposes a lower bound on $M D L ^ { X O R } ( p , j , t )$ . The sum total of all bids from free bidders that fit into p might even equal $M W D P ^ { X O R } ( p , t )$ . Since $M D L ^ { X O R } ( p , j , t )$ should be kept as small as possible, an appropriate choice must be made of an r-subset of the s bidders when hypothetical bids are assigned so that the smallest possible amount is left over for inclusion in p and the lower bound imposed on $M D L ^ { X O R } ( p , j , t )$ is small. A similar scheme has been described in [20]

## 7.3. Incremental implementation

An incremental method for computing MWDP for OR bids has been described in Section 4.1. A similar method exists for $M W D P ^ { X O R } .$ . All packages that are subsets of S are represented in TABM, including the empty package, which forms the leftmost entry. When $\begin{array} { r } { s = X ^ { 9 } Y ^ { 9 } } \end{array}$ and there are four bidders numbered 1, 2, 3 and 4, the first row of TABM contains the entries ϕ (the empty set), $( X , \{ 1 \} ) , ( X , \{ 2 \} ) , . . . , ( X , \{ 1 , 2 \} )$ , $. . . , ( X , \{ 1 , 2 , 3 , 4 \} ) , ~ ( X ^ { 2 } , \{ 1 \} ) , ~ . . . , ~ ( X ^ { 9 } , \{ 1 \} ) , ~ . . . , ~ ( Y , \{ 1 \} ) , ~ . . . , ~ ( X Y , \{ 1 \} ) , ~ . . . , ~ ( X Y , \{ 1 \} ) , ~ . . . ,$ $( X ^ { 2 } Y , \{ 1 \} ) , ~ . . . . ( X ^ { 9 } Y , \{ 1 \} ) , ~ ( X ^ { 9 } Y ^ { 2 } , \{ 1 \} )$ , and so on. Thus if there are n bidders, and m items with r copies each, there will be $( r + 1 ) ^ { m } . ( 2 ^ { n } { - } 1 )$ entries in the first row. To ensure correct updating of $M W D P ^ { X O R }$ values, we require that $\mathrm { i f } p _ { 1 }$ and $q _ { 1 }$ are two subsets of S with $p _ { 1 }$ to the left of $q _ { 1 }$ in the first row of TABM, then $q _ { 1 }$ is not a subset o $\dot { p } _ { 1 }$ , though $p _ { 1 }$ can be a subset of $q _ { 1 } .$ . The time taken to arrange the $^ { ( p , D ) }$ pairs in TABM is a fixed cost and does not depend on the auction data. All cells in the second row of TABM are initialized to zero.

After t-1 instants the second row of TABM contains the $M W D P ^ { X O R }$ values of packages for each subset D of bidders at instant t-1. When the bid $( j , q , \nu , t )$ is placed, we scan TABM from right to left and update the $M W D P ^ { X O R }$ value of each package p that is a superset of q using the recurrences (5)–(6). If q is a subset of ${ \dot { p } } ,$ , then at instant t for package p\q we only need to examine those bidder sets D of which j is not a member at instant t-1. The MWDP value of package p\q cannot get updated before the MWDP value of package p because of the order in which the packages have been arranged in TABM. Packages in TABM are scanned from right to left to rule out the possibility of more than one update of the MWDP value of a package [50]. After this horizontal pass through TABM the second row contains the correctly updated $M W D P ^ { X O R }$ values of the packages at instant t for each subset of bidders. This scheme can be implemented more simply by viewing the bidders as additional items having one unit each, so that when there are m items and n bidders, we get $( m + n )$ items with the last n having one unit each. The MDL values can be determined from MWDP for cases 1 and 2.

## 7.4. Experimental results

We ran the Compute\_MDL() program, after modifying it for the XOR case, on the same publicly available bid data specified in Section 6.2. Table 8 shows the $M W D \bar { P } ^ { X O R }$ , MWL<sup>XOR</sup> and $M D L ^ { X O R }$ values for three diferent choices of package p after all bids were processed. The average runtime per bid did not change significantly with the package p, perhaps because most entries in TABM had to be examined after each bid. Interestingly, $M W L ^ { X O R } ( p , j )$ was found to exceed $M W D P ^ { X O R } ( p , \{ j \} )$ in each case.

## 8. Implications of MUCA DSS on bidder strategies

The bidder feedback mechanism proposed here has been designed with online (continuous) multi-unit CAs (MUCAs) in mind. These auctions are characterized by asynchronous bidding (i.e., bidders join, place bids and leave at any time during the auction), little or no in formation about the valuations of other bidders, and no incentive for bidders to deviate from truthful bidding [15,21]. It can thus be assumed that strategic behavior of bidders for online multi-unit CAs would be absent as the amount of information that a bidder must possess for such behavior is prohibitively high. Moreover, study of game-theoretic implications of single-unit CAs has been found to be extremely hard [11]; more so for multi-unit CAs. However, we can still try to infer the possible impact of our decision support system on bidding behavior by drawing parallels from prior research on single-unit CAs [9,15,35,48,51].

Schefel et al. [48] conducted an experiment to test the eficiency of three diferent formats of single unit CAs. It was found that irrespective of the number of packages available for bidding, bidders bid on only a fraction of the packages. The authors identified the most likely reason as the high cognitive load of evaluating and bidding on a large number of packages. Other experiments [35] also support the conclusion that cognitive limitations of bidders are the primary reason for ineficiencies in CAs. Ausubel et al. [52] have reported bid shading in multi-unit auctions of a homogeneous item; however, it was not a significant factor in experiments conducted for MUCAs [15]. Jump bids were ob served in [15] but those were mostly to signal interest and invite bids from fellow bidders on complementary packages. Adomavicius et al. [9] and Sanyal [51] have conducted experiments on single-unit CAs by providing DL and WL values as information feedback to bidders. The idea of straightforward bidding strategy which implies that a bidder would only bid at DL values to maximize her payof was found to hold for most of the cases studied. However, bidders bid at the WL level in quite a few cases. This is akin to the idea of jump bids, although this was identified as examples of impatience on the part of bidders [9,51].

Multi-unit CAs are more complex than single unit CAs and therefore, bids are likely to be placed on only a fraction of packages as observed for single unit CAs. Two important parameters will play a role in bidding behavior, namely the payment mechanism and the terminating condition. If we assume that the payment mechanism is pay-as-bid, and that the auction terminates in the absence of bids for more than a predetermined and pre-announced interval of time [19], three diferent cases may arise:

1. The bidder bids below the MDL. This bid does not play any role in future, and therefore, cannot be a part of the winning allocation. So, a dead bid cannot be a strategic bidding option for bidders who would like to win packages in the auction.

2. If we assume straightforward bidding, we can expect that bidders would bid only at the MDL values of packages. $\begin{array} { r } { \mathrm { A } s \ : M \mathrm { { } } D L ( p , t ) \geq 0 , } \end{array}$ and $M D L ( p , t )$ is non-decreasing in t (see Properties 5 and 7) for all $p ,$ we can claim that revenue from this auction will always be non-negative.

3. If we remove the assumption of straightforward bidding and look at the findings in [19], there could be some bids at the MWL level. As $M W L ( p , t ) \geq M D L ( p , t )$ (properties 4 and 8), we can again claim that the revenue from such bidding behavior will always be non-negative.

Based on the above we can state that implementing our decision support tool with a pay-as-bid payment scheme will lead to a weakly budget balanced mechanism as the auctioneer cannot lose money. However, as Pekec and Rothpokf [11] state, equilibrium analysis of CAs is dificult and CAs are best studied experimentally [19]. We are hopeful that the information feedback mechanism proposed by us will motivate further research on experimental studies of bidding behavior for multi-unit CAs.

Table 8  
XOR formulation: results on U.K. auction data (7 items, 615 bids, 7 bidders, $M W D P ^ { X O R } ( S ,$ end) = 6371244000).

<table><tr><td>Run no</td><td>Package p</td><td> $MWDP^{XOR}(p, end)$ </td><td> $MWL^{XOR}(p, bidder 1, end)$ </td><td> $MDL^{XOR}(p, bidder 1, end)$ </td><td>Average runtime (secs) per bid</td></tr><tr><td>1</td><td> $\{1,2,3^4,4^3,5^3,6^3\}$ </td><td>2603731000</td><td>2198363000</td><td>970478000</td><td>3.17</td></tr><tr><td>2</td><td> $\{1^2,2,3^7,4^5,5^5,6^5\}$ </td><td>3654134000</td><td>2909803000</td><td>1652000000</td><td>3.35</td></tr><tr><td>3</td><td> $\{1^3,2,3^{10},4^7,5^6,6^5\}$ </td><td>4561336000</td><td>4342347000</td><td>1652000000</td><td>3.30</td></tr></table>

## 9. Concluding remarks

In this paper we discuss multi-unit combinatorial auctions (MUCAs) where bidders can place bids on multiple items and multiple units of items. It is very dificult for the bidders to meaningfully participate in such auctions without relevant information feedback. Computational tools for providing such feedback in MUCAs have not been available so far. Perhaps, this is the reason why businesses have found it dificult to adopt MUCAs despite the obvious eficiency benefits of conducting such auctions. Here, we propose and develop computational tools for determining real time bidder feedback for MUCAs for both OR and XOR formulations. The information feedback is in the form of two bounds, multi-unit deadness level, MDL, and multi-unit winning level, MWL. MWL of a package is easy to determine, but MDL is far more dificult to obtain. In this paper we provide a systematic procedure for computing the MDL value of a package p at time t. The method can be made incremental, i.e., given $M D L ( p , t )$ and the next bid, $M D L ( p , t + 1 )$ can be determined. Supporting experimental results are provided on both simulated and real-life data, which show that average running time for a bid is less than a second even for quite complex auction instances. This supports our claim that the methods described here can be used to provide real time feedback for online multi-unit CAs.

We expect our work to facilitate the adoption of MUCAs in real life business domains such as industrial procurement and network capacity auctions. It has been observed that providing real time information feedback to bidders during a continuous combinatorial auction increases the perceived usefulness, ease of use and intention to use [9]. Also, our work opens up the possibility of conducting eBay like auctions in the domain of consumer goods. Furthermore, the availability of in formation feedback aids in decision making as bid construction becomes easier for bidders. The eficiency of MUCAs is also likely to improve because of the availability of our computational tools.

Our research paves the way for studying the strategic behavior of bidders during MUCAs. Any real-life implementation of an auction would demand a thorough understanding of how bidders are likely to behave strategically during an auction. It was not possible to engage in such studies in the absence of information feedback tools for bidders, and therefore our work further strengthens the possibility of practical implementations of MUCAs.

An interesting direction for future work is the study of the general ized MU-XOR auction. This is a generalization of the OR and XOR formulations in which we associate with each bidder j a number $k _ { j }$ which is either ∞ (infinity) or a non-negative integer. If $k _ { j } = \infty$ , no restrictions are imposed on how many packages can be won by j, but if $k _ { j }$ is a positive integer then j can win at most k<sub>j</sub> packages. When $k _ { j } = 0 ,$ , bidder j does not participate in the auction. Information feedback support tools for MU-GXOR auctions, when available, can be used for every type of CA, whether OR, XOR or generalized XOR.

## Author contributions

Anup K Sen: Conceptualization, Methodology, Writing – Review & Editing.

Amitava Bagchi: Conceptualization, Writing – Original Draft, Formal Analysis.

Soumyakanti Chakraborty: Software, Investigation, Visualization.

## Acknowledgements

The authors would like to thank the editor, and anonymous reviewers for their valuable suggestions that have led to significant improvements in the manuscript.

## Appendix A

Property 1. $\begin{array} { r } { \begin{array} { r } { M D L ( p , t ) \leq M W D P ( \mathrm { p , t } ) . } \end{array} } \end{array}$

Proof: In the single-unit case, $D L ( p , t ) = W D P ( p , t ) .$ , i.e., the value of $D L ( p , t )$ for a package p is equal to the value of $W D P ( p , t )$ at every instant t. In multi-unit CAs each package may have multiple copies. So, while one copy of a package forms a part of the winning allocation, the other copies are still available for incluaion. Therefore, MDL(p,t) will always be ≤MWDP(p,t). In Example 1, $M D L ( p , t ) \ < \ M W D P ( p , t )$ at all instants. □

Property 2. MWDP(p,t) + MWDP(S\p,t) ≥ MWDP(S,t).

Proof: In the single-unit case, $W D P ( S \backslash p , t ) \ + \ W D P ( p , t ) \ = \ W D P ( S , t )$ always. But in the multi-unit case, p and $S \Psi$ are not necessarily disjoint. The same package may get included in both p and ${ \cal S } \backslash p ,$ so the LHS can exceed the RHS. □

Property 5. For any package $p , M D L ( p , t )$ is non-decreasing in t.

Proof: Consider any instant k, and suppose that $M D L ( p , k ) = \gamma$ and $M D L ( p , k + 1 ) = \delta$ We have to show that $\gamma \leq \delta .$ We argue as follows. All the bids that have been placed at all instants ≤k remain in consideration at instant $k + 1 ;$ ; however, one additional bid $( q _ { k + 1 } , \nu , k + 1 )$ is placed at instant $k + 1$ . By definition, γ is the smallest bid on p at instant k + 1 for which there exists a sequence of bids that puts $( p , \ \gamma , k \ + \ 1 )$ in the (provisional) winning combination at a future instant. When computing γ, all possible future sequences of bids placed at instants $\geq k + 1$ are taken into consideration. The bid $( q _ { k + 1 } , \nu , k + 1 )$ that actually gets placed at instant k + 1 is only a particular case, and it imposes a constraint on the value of δ but not on that of $\gamma , s 0 \gamma \leq \delta . \square$

## A.1. List of important notations

<table><tr><td>Notation</td><td>Description</td><td>Notation</td><td>Description</td></tr><tr><td> $p$ </td><td>A package in a multi-unit combinatorial auction; bidders place queries for the deadness and winning levels of this package</td><td> $M$ </td><td>A variable to store the value of  $MWDP$  of the entire set of items (S) in auction</td></tr><tr><td> $q$ </td><td>A package in a multi-unit combinatorial auction on which a bid arrives at a time instant</td><td> $R_t$ </td><td> $R_t$  is the set of all packages at time  $t$  that fit into  $S\backslash p$  and consist of a subset of packages from  $\Delta_t$ .</td></tr><tr><td> $MDL(p,t)$ </td><td>Deadness level of a package,  $p$  at time instant  $t$  in a multi-unit combinatorial auction in OR formulation</td><td> $r_i$ </td><td>The elements of  $R$ </td></tr><tr><td> $MWL(p,t)$ </td><td>Winning level of a package,  $p$  at time instant  $t$  in a multi-unit combinatorial auction in OR formulation</td><td> $C_{p,t}^{XOR}$ </td><td>A feasible allocation for a package  $p$  at time  $t$  in XOR formulation</td></tr><tr><td> $S$ </td><td>Multi-set of available items in an auction</td><td> $MWDP^{XOR}(p,t)$ </td><td>Maximum sum obtainable of the bid values that fit into  $p$  across all the bids received till time  $t$ , in a multi-unit combinatorial auction in XOR formulation</td></tr><tr><td> $\eta_i(S)$ </td><td>Number of identical units of each item  $i$  present in  $S$ </td><td> $MDL^{XOR}(p,j,t)$ </td><td>Deadness level of a package  $p$  at time instant  $t$  in a multi-unit combinatorial auction in XOR formulation</td></tr><tr><td>MWDP(p,t)</td><td>Maximum sum obtainable of the bid values across all the bids received till time instant t that fit into package p, in a multi-unit combinatorial auction in the OR formulation</td><td> $MWL^{XOR}(p,j,t)$ </td><td>Winning level of a package p at time instant t in a multi-unit combinatorial auction in XOR formulation</td></tr><tr><td>MWDP(S,t)</td><td>The total revenue from the auction at time instant, t in OR formulation</td><td> $MWDP^{XOR}(S,t)$ </td><td>The total revenue from the auction at time instant, t in XOR formulation</td></tr><tr><td>B = (j, q, v, t)</td><td>A bid is a quadruple where j is the bidder, q is the package, v is the non-negative integer value of the bid placed by j on q, and t is the time instant at which the bid is placed.</td><td>N</td><td>Set of all bidders in an auction</td></tr><tr><td>Cp,t</td><td>A feasible allocation for a package p at time t in OR formulation</td><td>D</td><td>Any subset of N</td></tr><tr><td>Δt</td><td>The set of packages on which bids have been placed till t</td><td>|N|</td><td>The number of bidders in N</td></tr></table>

## References

[1] M. Bichler, J. Goeree, S. Mayer, P. Shabalin, Spectrum auction design: simple auctions fo complex sales, Telecommunications Policy 38 (7) (2014) 613–622.

[2] S.J. Rassenti, V.L. Smith, B. R.L., A combinatorial auction mechanism for airport time slot allocation, Bell Journal of Economics 13 (1982) 402–417.

[3] E. Cantillon, M. Pesendorfer, Auctioning bus routes: the London experience, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, The MIT Press, Cambridge, Massachusetts, USA, 2006, pp. 573–591.

[4] C. Caplice, Y. Shefi, Combinatorial auctions for truckload transportation, in: P. Cramton Y. Shoham, R. Steinberg (Eds.). Combinatorial Auctions, The MIT Press, Cambridge. Massachusetts. USA. 2006, pp. 539–571

[5] J.O. Ledvard. M. Olson, D. Porter, J.A. Swanson, D.P. Torma, The first use of a combined value auction for transportation services, Interfaces 32 (5) (2002) 2002

[6] S. Yossi, Combinatorial auctions in the procurement of transportation services. Interfaces 34 (4) (2004) 245–252

[7] M. Bichler. A. Davenport. G. Hohner, J. Kalagnanam. Industrial procurement auctions, in P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, The MIT Press, Cambridge. Massachusetts, USA. 2006, p. 594.

[8] A. Greewald, J. Boyan, Bidding algorithms for simultaneous auctions: a case study, ACM Conference on Electronic Commerce (EC-01), 2001.

[9] G. Adomavicius, S. Curley, A. Gupta, P. Sanval, Effect of information feedback on bidder behavior in continuous combinatorial auctions, Management Science 58 (4) (2012) 811–830.

[10] A.M. Kwasnica, J.O. Ledvard, D. Porter, C. Demartini, A new and improved design for multiobject iterative auctions, Management Science 51 (3) (2005) 419–434.

[11] A. Pekec, M.H. Rothkopf, Combinatorial auction design, Management Science 49 (11) (2003) 1485–1503.

[12] B. Brammert, U. Endriss, Comparing Winner Determination Algorithms for Mixed Multi unit Combinatorial Auctions, Proc AAMAS, Estoril, Portugal, 2008, pp. 1601–1604.

[13] T. Sandholm, Approaches to winner determination in combinatorial auctions, Decision Support Systems 28 (1–2) (2000) 165–176.

[14] T. Sandholm, Algorithms for optimal winner determination in combinatorial auctions, Artificial Intelligence 135 (1–2) (2002) 1–54.

[15] M. Bichler, H. Zhen, G. Adomavicius, Coalition-based pricing in ascending combinatoria auctions, Information Systems Research 28 (1) (2017) 159–179.

[16] L.M. Ausubel, P. Milgrom, Ascending proxy auctions, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, The MIT Press, Cambridge, Massachusetts, USA, 2006, pp. 79–98.

[17] D.C. Parkes, iBundle: an efficient ascending price bundle auction. 1st ACM Conference on Electronic Commerce, 1999, pp. 148–157 EC-99.

[18] M.H. Rothkopf, A. Pekec, R.M. Harstad, Computationally manageable combinatorial auctions, Management Science 44 (8) (1998) 1131–1147.

[19] G. Adomavicius, A. Gupta, Toward comprehensive real-time bidder support in iterative combinatorial auctions. Information Systems Research 16 (2) (2005) 169–185

[2o] I Petrakis G Ziegler M Bichler Ascending combinatorial auctions with allocation constraints: game-theoretical and computational properties of generic pricing rules Information Systems Research 24 (3) (2013) 768–786

[21] G. Adomavicius, A. Gupta, M. Yang, Designing real-time feedback for bidders in homogeneous-item continuous combinatorial auctions, MIS Quarterly 43 (3) (2019) 721–A11

[22] C. Kroemer, M. Bichler, A. Goetzendor, (Un)expected bidder behavior in spectrum auctions about inconsistent bidding and its impact on eficiency in the combinatorial clock auction, Group Decision and Negotiation 25 (1) (2015) 31–63

[23] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, J.R. Kalagnanam, H.S. Lee, C. An, Combinatorial and quantity-discount procurement auctions benefit Mars, incorporated and its suppliers INFORMS Journal on Applied Analytics 33 (1) (2003) 23–35

[24] N. Remli. M. Rekik. A robust winner determination problem for combinatorial trans: portation auctions under uncertain shipment volumes, Transportation Research Part C 35 (2012) 204–217.

[25] M. Iftekhar, S.A. Hailu, R.K. Lindner, Item price information feedback in multiple unit combinatorial auctions: design issues, IMA Journal of Management Mathematics 22 (3) (2011) 271–289.

[26] N. Nisan, Bidding and allocation in combinatorial auctions, Proceedings of the 2nd ACM Conference on Electronic Commerce (EC '00), ACM, New York, NY, USA, 2000, pp. 1–12.

[27] C. Brunner, J. Goeree, C. Holt, J. Ledyard, An experimental test of flexible combinatoria spectrum auction formats, American Economic Journal: Microeconomics 2 (1) (2010) 39-57.

[28] J. Goeree, A.C. Holt. J.O. Ledvard. An experimental comparison of the FCC's combinatorial and non-combinatorial simultaneous multiple round auctions, Report for Wireless Telecommunications Bureau of the Federal Communications Commission (FCC). 2006

[29] P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, The MIT Press Cambridge MA USA 2006

[30] W. Vickrey, Counter-speculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1) (1961) 8–37 1961.

[31] E.H. Clarke, Multipart pricing of public goods, Public Choice 11 (1971) 17–33.

[32] T. Groves, Incentives in teams, Econometrica 41 (4) (1973) 617–631

[33] L.M. Ausubel, P. Milgrom, The lovely but lonely Vickrey auction, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, The MIT Press, Cambridge, Massachusetts. USA. 2006. pp. 17–40

[34] D. Porter, S. Rassenti, A. Roopnarine, V. Smith, Combinatorial auction design, Proceedings of the National Academy of Sciences 100 (19) (2003) 11153–11157.

[35] M. Bichler, P. Shabalin, J. Wolf, Do core-selecting combinatorial clock auctions always lead to high eficiency? An experimental analysis of spectrum auction designs, Experimental Economics 16 (4) (2013) 511–545.

[36] R. Gonen, D. Lehmann, Optimal Solutions for Multi-unit Combinatorial Auctions, 2nd, ACM Conference on Electronic Commerce, Minnesota, 2000, pp. 13–20.

[37] K. Leyton-Brown, Y. Shoham, M. Tennenholtz, An algorithm for multi-unit combinatorial auctions, National Conference on Artificial Intelligence, 2000, pp. 55–61.

[38] D.R. Goossens, A.J.T. Maas, F.C.R. Spieksma, J.J. van de Klundert, Exact algorithms for procurement problems under a total quantity discount structure, European Journal of Operational Research 178 (2) (2007) 603–626.

[39] D. Lucking-Reiley, Auctions on the Internet: what’s being auctioned, and how? The Journal of Industrial Economics 48 (3) (2000) 227–252

[40] R. Bapna, P. Goes, A. Gupta, Analysis and design of business-to-consumer online auctions, Management Science 49 (1) (2003) 85–101.

[41] R. Bapna, W. Jank, G. Shmueli, Consumer surplus in online auctions, Information Systems Research 19 (4) (2008) 400–416.

[42] D.G. Gregg, S. Walczak, Auction Advisor: an agent-based online-auction decision support system, Decision Support Systems 41 (2) (2006) 449–471.

[43] F.S. Hsieh, Combinatorial reverse auction based on revelation of lagrangian multipliers, Decision Support Systems 48 (2) (2010) 323–330.

[44] N. Yang, X. Liao, W.W. Huang, Decision support for preference elicitation in multi-at tribute electronic procurement auctions through an agent-based intermediary, Decisior Support Systems 57 (2014) 127–138

[45] M. Köksalan, R.-L. Leskelä, H. Wallenius, J. Wallenius, Improving eficiency in multipleunit combinatorial auctions: bundling bids from multiple bidders, Decision Support Systems 48 (1) (2009) 103–111

[46] R.-L. Leskelä, J. Teich, H. Wallenius, J. Wallenius, Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2) (2007) 420–434

[47] Sen A K., Bagchi, A. How much to bid on a package in a multi-unit combinatorial auction, WITS-2014, 24th Workshop on Information Technology & Systems, Auckland, NZ.

[48] T. Scheffel, G. Ziegler, M. Bichler, On the impact of package selection in combinatorial auctions: an experimental study in the context of spectrum auction design, Experimental Economics 15 (4) (2012) 667–692

[49] A.K. Sen, A. Bagchi, Incremental solutions to online XOR multi-item multi-unit combinatorial auctions for information feedback. WITS-2017. 27th Workshop on Informatior Technology & Systems, 2017 (Seoul South Korea)

[50] Ramanathan S., Kasinathan A., Sen A.K., Incremental Solutions to Online Multi-Unit Combinatorial Auctions, 9, Paper, Beijing, China, n.d., pp. 882–889.

[51] P. Sanyal, Characteristics and economic consequences of jump bids in combinatorial auctions Information Systems Research 27 (2) (2016) 347–364

[52] L. Ausubel P Cramton M Pycia M Rostek M Weretka Demand reduction and ins eficiency in multi-unit auctions, The Review of Economic Studies 81 (4 (289)) (2014) 1366-1400.

Anup Kumar Sen is a Professor in the Management Information Group at the Indian Institute of Management Calcutta. Prof. Sen has received his doctorate in Computer Science from the University of Calcutta. His major areas of research interest are workflow modeling and verification. combinatorial auctions, theory and applications of heuristic search methods. constraint satisfaction problems and meta-heuristic techniques.

Amitava Bagchi is a Professor in the Department of Computer Science and Engineering at the Heritage Institute of Technology. Prof. Bagchi has received his doctorate from MIT USA, and he has teaching and research experience of more than forty five years. His areas of research interest include combinatorial auctions, workflows, analysis of algorithms, software engineering and software reliability.

Soumyakanti Chakraborty is an Associate Professor in the Management Information Systems Group at Indian Institute of Management Calcutta. Dr. Soumyakanti Chakraborty received his doctorate from the Indian Institute of Management Calcutta. His research interests are in platform economics, pricing of information goods and combinatoria auctions.
