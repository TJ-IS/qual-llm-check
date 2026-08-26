---
otero_id: 14386
otero_key: "4D52JBT3"
title: "A public procurement combinatorial auction mechanism with quality assignment"
authors: "Jian Chen; He Huang; Robert J. Kauffman"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.02.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A public procurement combinatorial auction mechanism with quality assignment Jian Chen <sup>a</sup>, He Huang <sup>b,c</sup>, Robert J. Kauffman <sup>d,e,</sup>⁎

<sup>a</sup> Research Center for Contemporary Management, Tsinghua University, Beijing 100084, China

<sup>b</sup> School of Economics Business Administration, Chongqing University, Chongqing 400044, China

<sup>c</sup> Graduate School of Business, Columbia University, New York, NY 10027, USA

<sup>d</sup> School of Information Systems, and Lee Kong Chian School of Business, Singapore Management University, 178902, Singapore

<sup>e</sup> Glassmeyer-McNamee Center for Digital Strategies, Tuck School of Business, Dartmouth College, Hanover, NH 03755, USA

## a r t i c l e i n f o

Article history: Received 9 July 2010 Received in revised form 1 December 2010 Accepted 6 February 2011 Available online 10 February 2011

Keywords: Combinatorial auctions Economic analysis Government procurement Mechanism design Quality assignment Social welfare

## a b s t r a c t

This article focuses on mechanism design for quality assignment combinatorial procurement auctions. We model how the participants can maximize social surplus, the difference between gross utility and total cost in electronic procurement, while selecting appropriate quality standards for the procured items. In typical forward combinatorial auctions, the goal is to maximize the sum of all buyers' valuations. In our setting, however, to achieve high buyer utility with low supplier cost, the selected quality levels for the procured items from the suppliers must exceed some predetermined minimum threshold. So the identi<sup>fi</sup>cation of capable suppliers and the corresponding quality assignments are crucial, since buyer utility and supplier cost will be affected by the buyer's quality choice. We develop a novel mechanism to balance the interests of buyers and sellers. Our proposed quality assignment Vickrey–Groves– Clarke (QA-VCG) mechanism is incentive-compatible, provides constraints on partial participation, and is ef<sup>fi</sup>cient in quasi-linear preferences. In consideration of the perspective of the buyer as a government auctioneer, we also propose a revised mechanism to implement the goal of achieving minimal procurement costs, and appropriate bene<sup>fi</sup>ts for participating suppliers. We provide a numerical illustration of our QA-VCG mechanism, and an extension that addresses an iterative combinatorial auction mechanism design in our context.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Electronic combinatorial auctions have been applied in a variety of environments involving economic transactions. They have the potential to play an important role in electronic transactions for supply chain management procurement [33] and other contexts [45,46]. For example, Logistics.com (www.logistics.com) in the transportation and shipping industry has conducted industry-speci<sup>fi</sup>c B2B procurement combinatorial auctions, and Net Exchange (www.nex.com) has procured transportation services for Sears Logistics [50]. Home Depot regularly uses combinatorial auctions to procure trucking services [27]. Lee et al. [51] also have reported on an algorithm for optimal combinatorial auction bidding in truck route selection in support of such applications. IBM, which has signi<sup>fi</sup>cant ongoing research at its R&D centers around the world [12–16,57,58], also has been doing procurement through combinatorial auctions on behalf of Mars Incorporated and many other organizations [34].

In many other application settings though, the buyer in an electronic combinatorial auction for supply procurement is not a business enterprise. Municipal, county, provincial, state and central governments, and other public sector organizations are likely to bene<sup>fi</sup>t as well [30,46].

Combinatorial auctions can be used to procure services and project help, as well as goods, re<sup>fl</sup>ecting the needs of public procurement. We focus on the reverse auction version of combinatorial auctions for public procurement, where the emphasis is on social welfare. Our purpose especially matches the requirements for government auctions that can be held via the Internet in China, where state and private enterprises are involved in procurement, and where this research originated. Recently, for example, Catalan et al. [19] have studied the practical application of Internet-based combinatorial procurement auctions in the context of the procurement activities for food supplies by the Government of Chile, which provides more than 1.8 million meals daily to public school children at an annual cost of US\$360 million.

Combinatorial auctions have several features that affect the ef<sup>fi</sup>cacy of their design: their computational feasibility [55], their efficiency for winner determination [18], and the economic efficiency of their mechanism [37,45].<sup>1</sup> The computational ef<sup>fi</sup>ciency of winner determination algorithms has been explored in many research articles to date on combinatorial auctions [5,17,63]. Combinatorial auctions are challenging mechanisms to implement effectively. It is hard to solve for exact solutions when the number of suppliers is relatively large [65], and when there are information asymmetries between the buyer and suppliers [11]. In addition, there are often problems with free riding [24] on the part of bidders.

From the perspective of economics and management science, the central issues that exist in the optimal design of combinatorial auctions are allocation ef<sup>fi</sup>ciency and revenue maximization (or cost minimization) [37]. Allocation efficiency occurs when both the total value for the winners and the buyer's valuation are maximized, and is a primary goal in auctions involving a government auctioneer, such as the United States Federal Communications Commission for broadcast spectrum and transmission rights in radio networks [53]. Another application area is the procurement auctions of airport commissions for landing and takeoff slots at regional airports [40].

We view allocation ef<sup>fi</sup>ciency in terms of social surplus maximization from the procurement, from the point of view of both the government and suppliers. Revenue maximization is also important from the perspective of a government, which typically wishes to minimize its total cost of procurement [6,7,60]. However, these goals may contradict each other in different economic settings. For example, this can occur when there is a reserve price that does not permit the auction allocation priority ranking to be in synch with the ordered values of the bids that are made [54]. Krishna and Perry [47] suggest that a tradeoff is probably necessary in most auction mechanism design cases. Mechanism design is intended to solve the problem of effective auction implementation [9]. It views the marketplace as having self-interested rational agents with private information who act as participating suppliers in an auction. Their private information characterizes the suppliers' cost structure and auction bidder's demeanor. Some typical supplier type descriptors include supplier preferences, the schedule of supplier values for different quantities and qualities, the time in the auction (e.g., early or late or both) when the supplier makes a bid, and so on.

The purpose of this paper is to design a mechanism for combinatorial reverse auction-based procurement to achieve maximum social welfare, which has the utilitarian social goal of optimizing total surplus for both the auctioneer and the winning supply bidders. We emphasize that the role of the auctioneer that we wish to model in this work is a government or public entity procurement agent. For clarity related to the procurement in supply chain management, we will refer to bidders as suppliers throughout. The speci<sup>fi</sup>c characteristics of combinatorial auctions that we will treat in the procurement context involve heterogeneous goods and different quality standards. The property of heterogeneous goods is the same property that we see in normal combinatorial auctions [20]. However, the second property — quality standards assignment — is somewhat unique in procurement auctions.

The remainder of this article is organized as follows. Section 2 discusses the background literature and theory on the Vickrey– Clarke–Groves (VCG) mechanism for combinatorial auctions, as a departure point for the remainder of the article. Section 3 presents our proposed variant, a VCG mechanism for combinatorial auctions with the possibility of quality choices to be made by the auction bidders, and with suppliers who have the <sup>fl</sup>exibility to provide different bundles of procurement goods with differing degrees of quality. Section 4 discusses incentive compatibility, and presents our <sup>fi</sup>rst analytical results to show that the social choice function in our quality assignment VCG mechanism (QA-VCG) can be truthfully-implemented based on identi<sup>fi</sup>able dominant strategies. Section 5 deepens our analysis of the QA-VCG mechanism, by analyzing individual rationality and permitting bidders to decide whether they wish to participate in the auction. Next is Section 6, which discusses the QA-VCG mechanism's performance from the point of view of the auction operator. In Section 7, we present a numerical illustration of the operation of the QA-VCG mechanism. Section 8 extends the results of our QA-VCG mechanism to the case of multi-round auctions, where truth-telling round-by-round is no longer an essential goal. Section 9 concludes with contributions and limitations that can be addressed in future research.

## 2. The Vickrey–Clark–Groves mechanism

Discussions about the application of the Vickrey–Clark–Groves (VCG) mechanism [21,31,71,72] in normal combinatorial auctions can be found in the works of Ausubel [1–3], Ausubel and Milgrom [4,5], Bikhchandani and Ostroy [17], Parkes [57], Rothkopf et al. [64], and elsewhere. Sun and Yang [68,69] focused on combinatorial auctions for substitute goods or complementary goods to achieve allocation ef<sup>fi</sup>ciency, by a new Walrasian tâtonnement process called a doubletrack procedure. The VCG mechanism family provides a useful basis for our efforts to design a mechanism for combinatorial procurement auctions that addresses the key issues in social welfare maximization from a public procurement perspective.

The VCG mechanism family has several well-known virtues. The <sup>fi</sup>rst is that it creates incentives for truthful reporting as the dominant strategy of any bidder. In addition, its outcomes are always ef<sup>fi</sup>cient. Another virtue is its scope of application: the fundamental rules of VCG can adapted to suit other settings based on the addition of some extra constraints. Finally, the revenue equivalence theorem tells us that the auctioneer's revenue under the VCG mechanism will not be less than that from any other ef<sup>fi</sup>cient mechanism. Despite these attractive properties, however, the VCG mechanism has not often been applied in real-world settings. The main reasons relate to weaknesses in the VCG mechanism that include: the winner determination problem, bid preparation and communication costs, the failure of truthful reporting with budget constraints, the information revelation problem, the auction's vulnerability to shill bids, and decreased revenues or cost savings in the presence of a larger number of bidders [23,48,62].

Hidvégi et al. [32] introduced a binary Vickrey auction (BVA) mechanism to address the problem of computational complexity related to the winner determination problem. Their mechanism allocates goods in bundles based on sequentially-decreasing powerof-two items over multiple rounds. Their mechanism is able to handle auctions for speci<sup>fi</sup>c bidding quantities of multiple identical items. In public procurement auctions, the above concerns may not be controlling though. For example, as auctioneers governments tend to pay the most attention to social welfare and allocation ef<sup>fi</sup>ciency, rather than revenues. Shilling, or pseudonym use, and non-monotonic revenues for the auctioneer are not critical issues in government procurement. When procurement costs are going to be large, government procurement specialists will scrutinize the identities of all potential suppliers, and prequalify them for bidding. Also, they can make it a criminal act for a supplier to use a pseudonym — and enforce that prohibition. Further, knowing that the participation of additional potential supplier enhances the probability of achieving higher social welfare, the non-monotonicity of the government's revenue in terms of the number of suppliers will not be critical either.

To handle the quality-related combinatorial assignment, we will extend the classical VCG mechanism by incorporating suppliers' cost functions, and by capturing the quality assignment nature of procurement combinatorial auctions in an analytical model. This is our quality assignment Vickrey–Clark–Groves (QA-VCG) mechanism. In the QA-VCG mechanism, the supplier's cost function can be used to characterize the auction bids, and the level of willingness-to-pay or valuation for providing supplies in a given combinatorial auction that involves not-for-pro<sup>fi</sup>t operations. We will show the basis for allocation ef<sup>fi</sup>ciency, the incentive compatibility that makes dominant equilibrium strategies possible, and the individual rationality of the suppliers that obtains in their use of the mechanism. We also show that the proposed mechanism offers a means for the auctioneer to achieve lower costs with the process. To do this, we will propose and evaluate a related social choice function by revising the underlying payment function. Finally, we will show that the maximal expected revenue property holds for the revised mechanism by applying the revenue equivalence theorem [47,61,71,72].

There is a key difference between the standard VCG mechanism and our proposed combinatorial procurement QA-VCG mechanism. First, in terms of allocation ef<sup>fi</sup>ciency, the traditional VCG mechanism for reverse combinatorial auctions, without quality consideration, focuses on all the winning suppliers' total surplus only. Since ef<sup>fi</sup>ciency comes from giving suppliers who most highly value the opportunity to supply the combinations of item that are demanded, or equivalently, suppliers who are able to supply the items of a given quality at minimum cost, allocation ef<sup>fi</sup>ciency has nothing to do with the auctioneer, in this case, the buyer in such auctions, since without any quality assignment the auctioneer's total valuation of all items available for purchase is <sup>fi</sup>xed. Instead, allocation ef<sup>fi</sup>ciency in our proposed QA-VCG relates to the two-party surplus, which includes the both suppliers' and buyer's surplus. The allocations associated with the quality standard assignment not only will affect the suppliers' cost but they also will change the buyer's utility, which in turn will change the total social surplus of both parties.

Second, in terms of how the design works, the VCG mechanism includes the allocation of procurement supplies and a payment function, while the QA-VCG mechanism consists of these and quality assignments too. Our proposal for a QA-VCG mechanism is an extension of the VCG mechanism for the quality assignment combinatorial auctions setting. And we will show that our proposed mechanism achieves the maximum social surplus, based on the buyers' utility and suppliers' revenue.

## 3. A model of the VCG mechanism with quality assignment

Suppose there are n suppliers who make bids in an electronic auction. Each supplier is able to supply just one combination of goods in an auction to one buyer. We will refer to this buyer as the auctioneer, since public entities commonly act on their own behalf by soliciting quotes and conducting reverse auctions for supplies and services that they wish to procure. Bidding in the auction occurs around the prices at which the suppliers are willing to sell a bundle of procurement goods to the auctioneer.

Suppose that the auctioneer wants to procure one unit for each of m different goods from suppliers. Let X be the set of all m individual goods in a procurement auction that are to be delivered by the suppliers. We denote B as the set of possible bidding combinations, with $B \subset X ,$ representing a combination of goods in the procurement supplies set. The bidding language of supplier j is given by $B _ { j } =$ $\{ c _ { j k } ( \bullet ) \} \forall k \in B .$ . Here $c _ { j k } ( \bullet )$ is supplier j's cost function of supply for item k, an element of B, the set of possible bidding combinations. (See Table 1 for our modeling notation.)

Based on the revelation principle for dominant strategies [52], we will design a direct revelation mechanism for the quality assignment combinatorial procurement auction. Direct revelation in QA-VCG means that the bids of any supplier will contain only two kinds of information: the bidding combination and the supplier's cost function. Our QA-VCG mechanism can be represented in terms of three elements as the set QA-VCG: {A,Θ,P}. A is the set of all feasible allocations for the goods procured by the auctioneer from its suppliers with no assignment overlaps or omissions and no contract ful<sup>fi</sup>llment failures. Θ denotes the feasible quality standards for all goods. And, <sup>fi</sup>nally, P is the payment function that identi<sup>fi</sup>es what winning suppliers will be paid. Under the QA-VCG mechanism, the suppliers are the bidders, and their types correspond to the different cost functions that they face. In one speci<sup>fi</sup>c allocation outcome, the suppliers obtain different quality assignments, which determine by whom and at what quality levels the relevant procurement goods are supplied.

De<sup>fi</sup>nitions for key modeling notation in the main model

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td>A</td><td>The set of all feasible supply allocations made by the auctioneer to the suppliers</td></tr><tr><td> $a(a^{*})$ </td><td>A specific (optimal) supply allocation in the feasible set</td></tr><tr><td> $a^{-1}(j)$ </td><td>The allocation of supply goods for supplier  $j$ </td></tr><tr><td> $B; B_{j} = \{c_{jk}(.)\}, \forall k \in B$ </td><td>Set of possible bidding combinations by all suppliers; and by one specific supplier  $j$ </td></tr><tr><td> $\hat{c}_{j}(\cdot); \hat{c}_{jk}(\cdot)$ </td><td>Supplier  $j$ &#x27;s bidding cost function for her bidding combination; and for one element of the combination, goods  $k$ </td></tr><tr><td> $c_{j}(\cdot); c_{jk}(\cdot)$ </td><td>Supplier  $j$ &#x27;s real cost function for her bidding combination; and for goods  $k$ </td></tr><tr><td> $p_{j}\left(c_{j}\left(\overline{\theta}_{a^{-1}(j)}\right)\right)$ </td><td>Probability supplier  $j$  is assigned her bidding combination with quality requirements vector  $\overline{\theta}_{a^{-1}(j)}$ </td></tr><tr><td> $P_{j}(\hat{c}_{j})(P_{j}(\hat{c}_{j}|\bar{c}_{j}))$ </td><td>Payment function to winning supplier  $j$ , with cost report  $\hat{c}_{j}(.)$ , in original (revised) mechanism</td></tr><tr><td> $t_{j}(c_{j})$ </td><td>Expected payment value to supplier  $j$  with cost function  $c_{j}(.)$  in equilibrium state in any incentive-compatible, participation-constrained and efficient mechanism</td></tr><tr><td> $t_{j}(c_{j}|\bar{c}_{j})$ </td><td>Expected payment to supplier  $j$  with cost function  $c_{j}(.)$  in equilibrium state of the revised mechanism</td></tr><tr><td> $\theta_{k}$ </td><td>Quality requirements for a bundle of goods,  $k$ </td></tr><tr><td> $\overline{\theta}_{a^{-1}(j)}$ </td><td>Quality (Optimal quality) requirements for supply goods allocated to supplier  $j$ </td></tr><tr><td> $\Theta$ </td><td>the quality standards assignment feasible set</td></tr><tr><td> $\Theta^{*}$ </td><td>An optimal quality standards assignment scheme (Satisfy Eq. (1))</td></tr><tr><td> $u_{j}(\Theta^{*},P_{j})$ </td><td>Supplier  $j$ &#x27;s utility function expressed in terms of the quality requirements of the procurement goods and the payment function</td></tr><tr><td> $u_{j}(c_{j}|\bar{c}_{j})$ </td><td>Ex post utility of supplier  $j$  in the revised mechanism</td></tr><tr><td> $U_{j}(c_{j})$ </td><td>Expected utility of supplier  $j$  with cost function  $c_{j}(.)$  in any incentive-compatible, participation-constrained and efficient mechanism</td></tr><tr><td> $U_{j}(c_{j}|\bar{c}_{j})$ </td><td>Expected utility of supplier  $j$  with cost function  $c_{j}(.)$  in the revised mechanism</td></tr><tr><td> $v_{k}(\theta_{k})$ </td><td>Utility function of the auctioneer for goods  $k$  with quality  $\theta_{k}$ </td></tr><tr><td> $V(.)$ </td><td>Maximal social surplus for all procured goods</td></tr><tr><td> $V(J)$ </td><td>Maximal social surplus based on all suppliers&#x27; participation</td></tr><tr><td> $V(J|j)$ </td><td>Maximal social surplus with supplier  $j$  not participating</td></tr><tr><td> $V(J_{-j},\bar{c}_{j})$ </td><td>Maximal social surplus for supplier  $j$ &#x27;s participation with cost function  $\bar{c}_{j}(.)$ </td></tr></table>

The problem to be solved involves the goal of maximizing social surplus, which means maximizing the difference of the auctioneer's utility and the suppliers' costs, as follows:

$$
\underset {\overrightarrow {\theta} _ {a ^ {- 1} (j)} \in \Theta , a \in A} {M a x} \sum_ {j = 1} ^ {n} \left[ v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - \hat {c} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) \right]\tag{1}
$$

where

$$
v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) = \sum_ {k \in a ^ {- 1} (j)} v _ {k} (\theta_ {k})\tag{2}
$$

$$
\hat {c} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) = \sum_ {k \in a ^ {- 1} (j)} c _ {j k} \left(\theta_ {k}\right)\tag{3}
$$

In the above expressions, the notation, a, represents a speci<sup>fi</sup>c optimal allocation. This is an element of A which is the set of all feasible allocations by the auctioneer. In addition, Θ is the quality standards assignment feasible set, according to allocation a, for all goods or items that are procured, and $a ^ { - 1 } ( j )$ is the allocation for supplier j. The expression $\Theta _ { a ^ { - 1 } ( j ) }$ stands for the quality requirements <sup>ð Þ</sup>for the n items allocated to supplier $j ,$ and it is a vector in $R ^ { n } .$ Meanwhile, $\theta _ { k }$ is the quality standard for procurement item k. Here, $\boldsymbol { v _ { k } }$ (θ<sub>k</sub>) represents the utility function for the buyer related to item k with quality $\theta _ { k } ,$ and supplier j's bidding cost function, $\hat { c } _ { j k } ( \cdot )$ , for item k.

The QA-VCG mechanism optimizes the allocation of supplies to suppliers on the basis of Pareto efficiency, so that no supplier will be better off with any adjustment that is made to the allocation without another supplier being worse off. A related goal is maximizing the social surplus within the constraints of the applicable budget balance, an assumption that does not permit external subsidies. If the QA-VCG mechanism provides Pareto ef<sup>fi</sup>ciency, then the allocation of supplies to suppliers must satisfy Eq. (1)'s allocation function.

Any given supplier j who becomes one of the winners of the combinatorial auction will have an associated payment function, P, as follows:

$$
P _ {j} \left(\hat {c} _ {j}\right) = V (J) + \hat {c} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - V (J \backslash j)\tag{4}
$$

where

$$
V (J) = \underset {\overrightarrow {\theta} _ {a ^ {- 1} (j)} \in \Theta , a \in A} {M a x} \sum_ {j = 1} ^ {n} \left[ v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - \hat {c} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) \right]\tag{5}
$$

$$
V (J \backslash j) = \underset {\overrightarrow {\theta} _ {a ^ {- 1} (i)} \in \Theta , a \in A} {M a x} \sum_ {i \in [ J \backslash j ]} ^ {n} \left[ v _ {i} \Bigl (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Bigr) - \hat {c} _ {i} \Bigl (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Bigr) \right]\tag{6}
$$

Consider the individual terms in Eq. (4). The <sup>fi</sup>rst term, $V ( J )$ de<sup>fi</sup>ned in Eq. (5) in its full form, is the maximum social surplus based on the aggregation of all individual-level supplier utilities, $\nu _ { j } ,$ that can be achieved with all bidding suppliers' participation in the auction. The second term, as before, is the supplier's reported cost associated with providing a winning set of goods with corresponding optimum quality standards to the auctioneer. The third term, de<sup>fi</sup>ned in Eq. (6), is the maximum social surplus that can be achieved in the auction without supplier j's participation. So supplier j's payment includes the difference between the maximum achievable social surplus with or without her participation, plus the reported cost of her delivery of a winning combination of goods to the auctioneer that meet the quality requirement. Another way to interpret the payment function is to regard this payment as a transfer in value between auction agents. The transfer in our model is measured by the externality of supplier j plus the utility of the combination of goods she supplies to auctioneer.

The surplus maximization problem in Eq. (1) and the payment function in Eq. (4) together represent the social choice function for our QA-VCG mechanism. A social choice function is a correspondence between the supplier types to the allocation outcomes of an auction, which must satisfy some social goals [52]. The implicit constraints embedded in Eqs. (5) and (6) for the optimization problems are all of the feasible allocations, which are partitions of all the procured goods. In the winner determination problem for combinatorial auctions, the feasibility and complexity of these allocations are important [4,63]. However, it is common to assume that there is a mechanism that can solve the optimization problem to select the best outcome for the suppliers and the auctioneer. We assume enough suppliers to participate in the procurement auction, so a feasible allocation solution for the subsets of goods that are procured will always exist.

The Gibbard–Satterthwaite impossibility theorem [29,66] tells us that, for a general class of problems, there is no hope of implementing ef<sup>fi</sup>cient social choice functions in dominant strategies. Given this “negative” theorem, if we are to have any hope of implementing a desirable social choice function based on the allocation function and the payment function in our model, then we have to weaken the demands of our implementation or we must focus on more restricted environments. We will follow the latter course in the present work, by implementing desirable social choice functions in dominant strategies when preferences take on a speci<sup>fi</sup>c functional form. We will assume that the utility $u _ { j }$ of any supplier j has a quasi-linear form:

$$
u _ {j} = P _ {j} \left(\hat {c} _ {j}\right) - \sum_ {k \in a ^ {- 1} (j)} c _ {j k} \left(\theta_ {k}\right)\tag{7}
$$

where $c _ { j k } ( \bullet )$ once again is supplier j's true cost function of item k.

## 4. Incentive compatibility

Next, we will show that the social choice function in our QA-VCG mechanism can be truthfully-implemented based on dominant strategies in electronic combinatorial auctions. For the purpose of maximizing her own utility, supplier j will report her true cost function to the auctioneer as $\hat { c } _ { j k } ( \cdot ) = c _ { j k } ( \cdot ) , \forall k \in a ^ { - 1 } ( j )$

Proposition 1 (The supplier's truth-telling strategy). In QA-VCG combinatorial procurement auctions, truth-telling is a dominant strategy for any supplier.

Proof. Let $\boldsymbol { \Theta } ^ { * }$ denote the optimal quality requirements for all goods that satisfy the allocation ef<sup>fi</sup>ciency in Eq. (1). If supplier j is one of the winners, then her utility function can be expressed in terms of the quality requirements and the payment function in Eq. (4) as:

$$
\begin{array}{l} u _ {j} \Big (\Theta^ {*}, P _ {j} \Big) = u _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)}, P _ {j} \Big) \\ \qquad = - \sum_ {k \in a ^ {- 1} (j)} c _ {j k} (\theta_ {k}) + V (J) + \sum_ {k \in a ^ {- 1} (j)} \hat {c} _ {j k} (\theta_ {k}) - V (J \backslash j) \\ \qquad = \sum_ {i = 1, i \neq j} ^ {n} \Big [ v _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) - \hat {c} _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) \Big ] + \Big [ v _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) - c _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) \Big ] - V (J \backslash j) \end{array}\tag{8}
$$

In Eq. (8), the last term, $V ( J \backslash j )$ , is not in<sup>fl</sup>uenced by supplier j's revelation of her cost function information. However, revelation of the true cost function indirectly affects the <sup>fi</sup>rst two terms. Supplier j's bid, $\hat { c } _ { j k } ( \cdot ) , k { \in } a ^ { - 1 } ( j )$ , will affect her utility in Eq. (8) based on the effect of <sup>ð Þ ð Þ</sup>the quality standard assignment for the supplies, Θ\*, that is chosen based on the goal of allocation ef<sup>fi</sup>ciency, as in Eq. (1). The requirement is that supplier j must report her real cost function, so that $\hat { c } _ { j } \biggl ( \overrightarrow { \boldsymbol { \Theta } } _ { a ^ { - 1 } ( j ) } \biggr ) = c _ { j } \biggl ( \overrightarrow { \boldsymbol { \Theta } } _ { a ^ { - 1 } ( j ) } \biggr )$ , in order to achieve her maximal utility through the optimization choice of a and $\boldsymbol { \Theta } ^ { * }$ □

It is routine to verify that truth-telling is an equilibrium strategy in any ef<sup>fi</sup>cient mechanism [47,52]. In our case, we know that the QA-VCG mechanism implements the social choice function in Eqs. (1) and (4) as a dominant equilibrium strategy. Comparing this equilibrium strategy with how implementation is viewed in the context of the Bayesian–Nash equilibrium concept, the dominant equilibrium implementation is strong and robust. A rational agent who has a weakly dominant strategy will want to use it. But, unlike the equilibrium strategies in a Bayesian–Nash equilibrium, a supplier does not need to correctly forecast the opposing supplier's bids or types to justify his dominant strategy approach to bidding. The QA-VCG mechanism will be robust even if the suppliers have incorrect, and perhaps even contradictory beliefs about the distribution of other suppliers' cost functions. One advantage of the dominant equilibrium strategy is that if the mechanism designer is an outsider — for example, the auctioneer or a government procurement agent in our model — then the designer will not need to know the probability density over realizations of the suppliers' costs to successfully implement the social choice function via the allocation and payment functions.

## 5. Individual rationality

Until now, we have assumed that each supplier has no choice but to participate in the auction. We limited the supplier's judgment to choosing optimal actions within those allowed by the mechanism. However, in many cases, suppliers can voluntarily participate in combinational procurement auctions. As a result, the social choice function that is to be implemented by a mechanism must not only be incentive-compatible. It must also satisfy the appropriate individual rationality or participation constraints to be successful.

We note three stages in which participation constraints may be relevant under different assumptions. The <sup>fi</sup>rst of these stages occurs when we assume that suppliers may be able to withdraw from the auction and is called the ex post stage [52]. This stage arises when all suppliers have announced their cost functions and an allocation (including the combinatorial assignment and quality requirements) has been announced publicly by the auctioneer. A related assumption is that suppliers cannot receive any positive utility by withdrawing from the auction. The second stage is the interim stage, which is de<sup>fi</sup>ned as the time when all suppliers know their own cost functions for supply but have no precise information about the cost functions of other suppliers [35]. The third stage is the ex ante stage, in which all suppliers do not know their own and other bidders' cost functions exactly, but just distributional information about them [52]. We will next show that the QA-VCG mechanism is able to satisfy individual rationality in the ex post stage.

Proposition 2 (Ex post individual rationality proposition). In QA-VCG, a supplier's ex post individual rationality is assured.

Proof. Incentive compatibility in QA-VCG shows that the reported costs of a supplier in delivering goods of a required quality are truthful costs, that is, $c _ { j } \Big ( \overrightarrow { \theta } _ { a ^ { - 1 } ( j ) } \Big ) = \hat { c } _ { j } \Big ( \overrightarrow { \theta } _ { a ^ { - 1 } ( j ) } \Big )$ , based on payment function $P _ { j } = V ( J ) - V ( J \backslash j ) + \sum _ { \iota , \ldots \mid \colon } \hat { c } \quad ( \theta _ { k } ) ,$ . Here $u _ { j } = V ( J ) - V ( J \backslash j )$ , which k∈a<sup>−1</sup> j <sub>jk</sub> is non-negative, can be used as an expression for the ex post utility of supplier j. □

We now will discuss the individual rationality of the auctioneer relative to the revenue that is produced. This can be expressed as follows in terms of the utility of a successful bidding combination, $u ^ { B } ,$ when some suppliers win the opportunity to provide supplies:

$$
u ^ {B} = \sum_ {j \in \{\text { winners } \}} v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - \sum_ {j \in \{\text { winners } \}} P _ {j}\tag{9}
$$

In this expression, the <sup>fi</sup>rst term describes the value of all procured goods to the auctioneer associated with the corresponding optimal quality requirements, reduced by the relevant payments to suppliers in the second term. Note that using Eqs. (4)–(6), we can rewrite Eq. (9):

$$
\begin{array}{l} u ^ {B} = \sum_ {j \in \{\text { winners } \}} v _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) - \sum_ {j \in \{\text { winners } \}} \left[ V (J) - V (J \setminus j) + \sum_ {k \in a ^ {- 1} (j)} c _ {j k} (\theta_ {k}) \right] \\ = V (J) - \sum_ {j \in \{\text { winners } \}} [ V (J) - V (J / j) ] \end{array}\tag{10}
$$

The term $\begin{array} { r } { \sum _ { j \in \{ w i n n e r s \} } [ V ( J ) - V ( J \backslash j ) ] } \end{array}$ represents the total surplus of <sup>f g½ -ð Þ ð Þ</sup>all of the winning suppliers, while V(J) is the social surplus. However, we cannot be certain that the value of the utility, $u ^ { B } ,$ , is greater than or equal to zero. In some extreme cases, V(J) can be negative, but the social surplus optimization that we speci<sup>fi</sup>ed in Eqs. (1) and (4) will still work. For example, a government auctioneer may wish to procure something or launch some projects, such as equipment for swimming stadium for the Olympic Games in Beijing, China or a land reclamation project for low-income housing in Baltimore, Maryland. When the visible utility of these projects is less than the cost, the government's procurement approach typically is to minimize the extent of the negative bene<sup>fi</sup>t–cost difference. In addition, it may be appropriate to think of Eq. (10) as a non-negativity condition for the auctioneer's individual rationality, if break-even or better is required. When the aggregate social surplus is greater than the total winners' surplus, the auctioneer will bene<sup>fi</sup>t from the difference.

Whenever gains from auction-based trade are possible, but not certain, there is no ex post ef<sup>fi</sup>cient social choice function that is Bayesian incentive-compatible and will satisfy the participation constraints [54]. Under the conditions of the theorem, the presence of both private information and voluntary participation makes it impossible to achieve ex post ef<sup>fi</sup>ciency. In other words, no ex post ef<sup>fi</sup>cient social choice function will be implementable via the dominant strategies with participation constraints.

In government procurement auctions, the auctioneer typically emphasizes fairness, transparency, bidding incentives and social welfare to a greater extent than we typically observe in the private sector. Visible pro<sup>fi</sup>t may not be as critical a factor in the social planning context. Thus, it may be inappropriate to over-emphasize the assumption of individual rationality, when there is a quasi-participation constraint that permits participation with negative utility.

## 6. The payment function and auctioneer's cost

We have seen that the social choice function that we speci<sup>fi</sup>ed is truthfully implementable via dominant strategies for bidding participation in a combinatorial procurement auction. But are these the only ef<sup>fi</sup>cient social choice functions that satisfy Eqs. (1) and (4) and will they be truthfully implementable? And what can the auctioneer do to minimize cost? We now examine these issues more closely.

Our next proposition considers the functional form of the payment function, which is a revised version of truthful implementation condition in Groves–Clarke mechanisms [52].

Proposition 3 (Payment functional form proposition). The social choice function is truthfully implementable in dominant strategies only if the payment is specified according to the functional form of Eq. (4).

A proof is provided in Appendix A.

## 6.1. Minimizing the auctioneer's cost with supplier participation

If some truthfully implementable ef<sup>fi</sup>ciency mechanism can enhance the pro<sup>fi</sup>t that the auctioneer can earn in settings with maximum social welfare, then the auctioneer likely will choose the mechanism that enables the greatest utility or <sup>fi</sup>nancial advantage. We next explore the construction of an alternate social choice function with a revised payment function advantageous to the auctioneer, in the presence of the same social goals, as in the allocation function in Eq. (1). We de<sup>fi</sup>ne the following revised payment function:

$$
P _ {j} \left(\hat {c} _ {j} | \bar {c} _ {j}\right) = V (J) + \hat {c} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - V \left(J _ {- j}, \bar {c} _ {j}\right)\tag{11}
$$

where

$$
V \left(J _ {- j}, \overline {{c}} _ {j}\right) = \sum_ {i \neq j} \left[ v _ {i} \left(\overrightarrow {\theta} _ {a ^ {- 1} (i)}\right) - \hat {c} _ {i} \left(\overrightarrow {\theta} _ {a ^ {- 1} (i)}\right) \right] + \left[ v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (\bar {j})}\right) - \overline {{c}} _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (\bar {j})}\right) \right]\tag{12}
$$

$V \left( J _ { - j } , \overline { { c } } _ { j } \right)$ is the social surplus (including suppliers' and auctioneer's pro<sup>fi</sup>t) when supplier $j ^ { \prime } s$ cost function is $\overline { { c } } _ { j } ( . )$ , and she submits a bid of $\overline { { c } } _ { j } ( \cdot )$ to the auctioneer, while the other supply bid $\hat { c } _ { i } ( \cdot ) . a ^ { - 1 } \left( \bar { j } \right)$ denotes <sup>ð Þ ð Þ</sup>the allocation that the auctioneer makes (for the combination of goods supplied and quality standard met) to supplier j.

If she wins, the ex post utility of supplier j is given by:

$$
\begin{array}{l} u _ {j} \Big (c _ {j} | \overline {{c}} _ {j} \Big) = V (J) + \hat {c} _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) - V \Big (J _ {- j}, \overline {{c}} _ {j} \Big) - c _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) \\ = \sum_ {i \neq j} ^ {n} \left[ v _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) - \hat {c} _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) \right] + \left[ v _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) - c _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) \right] - V \Big (J _ {- j}, \overline {{c}} _ {j} \Big) \end{array}\tag{13}
$$

By implementing a similar analysis of the original mechanism's incentive compatibility, we can show that supplier j must bid her real cost function, $\overline { { c } } _ { j } ( \cdot )$ , in the revised mechanism to maximize the value of <sup>ð Þ</sup>her ex post utility in Eq. (13). It is evident from the form of the equation that her revelation of her cost function is unaffected by $V ( J _ { - j } , \overline { { c } } _ { j } )$ . In the improved mechanism, suppliers will have an incentive to submit bids that re<sup>fl</sup>ect their true underlying cost functions.

Next, following Krishna and Perry [47], we de<sup>fi</sup>ne the value of the supplier's critical participation cost, $\overline { { c } } _ { j } ( \cdot )$ , in terms of the auctioneer's revenue:

$$
\overline {{c}} _ {j} (\cdot) = \underset {c _ {j} (\cdot) \in C _ {j} (\cdot)} {\text { argmin }} V \left(J _ {- j}, c _ {j}\right)\tag{14}
$$

$c _ { j } ( \cdot )$ re<sup>fl</sup>ects the range of possible bids (and underlying costs) of the supplier. Think of $\overline { { c } } _ { j } ( \cdot )$ as the cost type for providing a package of <sup>ð Þ</sup>supplies that is associated with indifference on the part of supplier j. In another words, if supplier j has true cost, $\overline { { c } } _ { j } ( \cdot )$ , then she will obtain <sup>ð Þ</sup>utility 0 from our revised QA-VCG mechanism. We assume that the auctioneer knows the range of cost functions for all of the potential suppliers, but only will come to know their real cost functions after the bidding is done. Because the revised mechanism is incentivecompatible, our assumption about the auctioneer's knowledge of the true cost functions of all of the suppliers is reasonable. We de<sup>fi</sup>ne the equilibrium state as the state in which suppliers bid their true cost functions. Equilibrium can be achieved in the incentive-compatible revised mechanism. So, in the equilibrium state of the revised mechanism, we can rewrite Eq. (13) as:

$$
u _ {j} \left(c _ {j} \mid \bar {c} _ {j}\right) = V (J) - V \left(J _ {- j}, \bar {c} _ {j}\right)\tag{15}
$$

This expression is non-negative because the suppliers' ex post participation constraint is satis<sup>fi</sup>ed. $V ( J _ { - j } , \overline { { c } } _ { j } )$ is the social surplus for a speci<sup>fi</sup>c supplier j that has cost function $\overline { { c } } _ { j } ( \cdot )$ . Considering the de<sup>fi</sup>nition of $\overline { { c } } _ { j } ( \cdot ) , V \bigl ( J _ { - j } , \overline { { c } } _ { j } \bigr )$ <sup>ð Þ</sup>is the least maximal social surplus with supplier $j ^ { \prime } s$ <sup>ð Þ</sup>participation, given the other suppliers' bids. For this reason, Eq. (15) is non-negative.

## 6.2. Winning suppliers' utility and payments

We argued earlier that the ex post utility of supplier $j ,$ $u _ { j } ( c _ { j } | \overline { { c } } _ { j } ) = V ( J ) { - } V ( J _ { - j } , \overline { { c } } _ { j } )$ , is positive. To show this more formally, we <sup>j ð Þfi</sup>rst need to examine two cases in which supplier j is selected as one of the winners by the auctioneer in a procurement combinatorial auction.

## Case 1. Supplier's true cost is better than expected

If the supplier $j ^ { \prime } s$ true cost function, $c _ { j } ( \cdot )$ , is better than what the auctioneer thinks, as represented by the indifference level $\overline { { c } } _ { j } ( \cdot )$ then $V ( J _ { - j } , c _ { j } ) = V ( J ) > V ( J _ { - j } , \overline { { c } } _ { j } )$ <sup>ð Þ</sup>. That is a restatement of our prior <sup>ð Þ</sup>assertion: that the ex post utility of supplier j is positive in Eq. (15).

## Case 2. Supplier's true cost matches the auctioneer's expectation

If Supplier $j ^ { \prime } s$ true cost function $c _ { j } ( \cdot )$ is the same as $\overline { { c } } _ { j } ( \cdot ) ,$ then the <sup>ð Þ</sup>utility associated with combinatorial-based procurement will be zero for the supplier. Based on the de<sup>fi</sup>nition $\mathrm { o f } \overline { { c } } _ { j } ( \cdot )$ , it is impossible that $c _ { j } ( \cdot )$ is worse than $\overline { { c } } _ { j } ( \cdot )$

If supplier j is not selected as one of the winners, then the utility will also be zero. So the utility that obtains from the supplier's participation in the auction, as indicated in Eq. (15), will be nonnegative, which means that ex post individual rationality will hold.

We also know that $V ( J _ { - j } , \overline { { { c } } } _ { j } ) { \ge } V ( J \backslash j ) \forall j$ will be true. That is because <sup>ð Þ</sup>the level of social welfare that obtains with the participation of suppliers whose bids are made at the indifference level (yielding a zero utility) — including bidder j's bid — will be greater than or equal to the social welfare that accrues without her participation. By comparing the payment function for the original payment scheme in Eq. (4) with the revised payment function in Eq. (11), we can see that the payment to be made to any supplier j will be less for the latter. This means that the auctioneer can obtain the same quality products or services for less money.

Now we should not view the revised mechanism as being better than in the original mechanism in terms of social welfare terms, however. What is happening is that the same amount of surplus from suppliers is ending up in the hands of the auctioneer, with the result that there is no increase in total social welfare. Only the auctioneer's cost is decreased by the revised payment scheme, and this makes the suppliers get less value from the process in terms of the monetary payments for the items they supply.

In the spirit of payment maximization theorem of Krishna and Perry [47], to choose another optimal $\overline { { c } } _ { j } ( \cdot )$ based on the conditional <sup>ð Þ</sup>expectation, we will show that our proposed mechanism maximizes expected utility for all incentive-compatible mechanisms in our combinatorial procurement auction setting. The purpose of applying the conditional expectation is to depict settings in which a supplier who knows her own cost function may not know the cost functions of the other suppliers, as in the interim stage in mechanism design theory that we discussed earlier. So the only effective way for a supplier to forecast her revenue is to evaluate other suppliers' cost functions based on what she knows about her own cost function.

To illustrate these ideas, we <sup>fi</sup>rst de<sup>fi</sup>ne the expected utility of supplier j with cost function $c _ { j } ( \cdot )$ in any incentive-compatible, participation-constrained and ef<sup>fi</sup>cient mechanism:

$$
U _ {j} \left(c _ {j}\right) = E _ {c _ {- j}} \left[ u \left(c _ {j}\right) \right] = t _ {j} \left(c _ {j}\right) - p _ {j} \left(c _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right)\right) \cdot c _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right)\tag{16}
$$

Here, $t _ { j } ( c _ { j } )$ is the expected payment value with supplier $j ^ { \prime } s$ cost function $c _ { j } ( \cdot )$ . But supplier $j$ is not aware of other suppliers' cost functions. Thus, the payment value will not be deterministic in the interim stage for supplier $j .$ Further, her revenue from the combinatorial auction must be evaluated in expected value terms, as $p _ { j } \biggl ( c _ { j } \biggl ( \overrightarrow { \boldsymbol { \theta } } _ { a ^ { - 1 } ( j ) } \biggr ) \biggr )$ . This is the probability with which supplier $j$ is assigned an allocation based on her bidding combination that meets the standard that the auctioneer sets for the quality vector of the supply goods, $\overline { { { \Theta } } } _ { a ^ { - 1 } ( j ) }$ . Since the amount the supplier is willing to pay <sup>ð Þ</sup>via her cost function also re<sup>fl</sup>ects her expected utility, we can employ the supplier j's cost function $c _ { j } \left( \cdot \right)$ in the revised mechanism, to obtain the optimal value of supplier utility, $U _ { j } ( \cdot )$ , as follows:

$$
U _ {j} \left(c _ {j} \mid \bar {c} _ {j}\right) = E _ {c _ {- j}} \left[ u \left(c _ {j} \mid \bar {c} _ {j}\right) \right] = t _ {j} \left(c _ {j} \mid \bar {c} _ {j}\right) - p _ {j} \left(c _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right)\right) \cdot c _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) \tag {17}
$$

$t _ { j } ( c _ { j } | \overline { { c } } _ { j } )$ is the expected payment to supplier j established on the basis <sup>j</sup>of true cost function, $c _ { j } ( \cdot )$ , in the equilibrium state of the application of the revised combinatorial auction mechanism. The conditionallyexpected optimal value of $\overline { { c } } _ { j } ( \cdot )$ is based on:

$$
\overline {{c}} _ {j} (\cdot) = \underset {c _ {j} (\cdot) \in C _ {j} (\cdot)} {\operatorname{argmin}} E _ {c _ {- j}} \left[ V \left(J _ {- j}, c _ {j}\right) \right]\tag{18}
$$

Applying Krishna and Perry's [47] expected utility equivalence theorem, for any incentive-compatible, participation-constrained and ef<sup>fi</sup>cient mechanism that has the same social goal, we obtain the following equality, which is known as the revenue equivalence theorem:

$$
U _ {j} \left(\bar {c} _ {j} | \bar {c} _ {j}\right) - U _ {j} \left(c _ {j} | \bar {c} _ {j}\right) = U _ {j} \left(\bar {c} _ {j}\right) - U _ {j} \left(c _ {j}\right)\tag{19}
$$

This theorem states that all incentive-compatible, participationconstrained and ef<sup>fi</sup>cient mechanisms with the same social goal will generate the same difference in expected utility corresponding to different cost functions for the suppliers [36]. The left side of Eq. (19) is the difference in expected utility of supplier j based on different cost functions, $c _ { j } ( \cdot )$ and $\overline { { c } } _ { j } ( \cdot )$ , in the revised mechanism. The right hand side is the difference in expected utility of supplier j based on $c _ { j } ( \cdot )$ and $\overline { { c } } _ { j } ( \cdot )$ , which applies to any other speci<sup>fi</sup>c incentive mechanism with the same social goal as in our model (based on Eqs. (1) and (4).

Rearranging terms in Eq. (19), we obtain:

$$
U _ {j} \left(c _ {j}\right) - U _ {j} \left(c _ {j} \mid \bar {c} _ {j}\right) = U _ {j} \left(\bar {c} _ {j}\right) - U _ {j} \left(\bar {c} _ {j} \mid \bar {c} _ {j}\right)\tag{20}
$$

Individual rationality requires that $U _ { j } ( \overline { { c } } _ { j } ) { \geq } U _ { j } ( \overline { { c } } _ { j } | \overline { { c } } _ { j } ) = 0 \ \forall j .$ Consequently, it must also be the case that $U _ { j } ( c _ { j } ) { \geq } U _ { j } ( c _ { j } | \bar { c } _ { j } ) \forall c _ { j } ,$ which, in turn, means that $t _ { j } ( c _ { j } | \overline { { c } } _ { j } ) { \leq } t _ { j } ( c _ { j } ) \forall c _ { j } .$ <sup>j</sup>. Thus, we conclude that the revised mechanism, with its optimal conditionally-expected value of $\begin{array} { r } { \overline { { c } } _ { j } ( \cdot ) , } \end{array}$ , will <sup>ð Þ</sup>minimize the expected cost of the auctioneer by minimizing all of the suppliers' expected payments with the same allocation rules and the same allocation outcome. This is the same combinatorial assignment of goods at the criterion level of quality demanded by the auctioneer.

## 7. A numerical illustration of the QA-VCG mechanism's operation

We next illustrate the QA-VCG mechanism based on e-procurement of a bundle of goods. The procedure has several steps leading to what mix of quality and trade items in a bundle maximize value in procurement. First, we specify the cost function for the quality level of the trade items as they would be delivered by the suppliers who make bids. We specify the utility for quality from the point of view of the buyer — in this case, the auctioneer. Then, associated with the supply bids and the auctioneer's utility function, we show the search space for the optimal allocation of supplies by the auctioneer to the suppliers.

## 7.1. Assumptions and search procedure for the optimal allocation of suppliers

The auctioneer wishes to procure three trade items, A, B and C. There are three suppliers. Supplier 1 can supply all three items, however, Suppliers 2 and 3 cannot supply all three individually. Together, Suppliers 2 and 3 are able to provide the auctioneer with the full bundle, but not without cooperating. To represent the search space, we assume two levels of quality for all of the trade items to be procured, high and low. The low quality standard L has a quality score x of 3, and the high quality standard H has a quality score of 4. The auctioneer wants to maximize the value of quality less procurement cost. (See Tables 2 and 3.)

The search procedure involves the enumeration of all of the different combinations of quality bundles, which re<sup>fl</sup>ect acceptable combinations of high and low quality trade items, to determine the social surplus or highest net value based on total utility less total cost. (See Table 4.)

Based on the information presented in Table 4, we can see that there are two potentially optimal allocations to suppliers, Allocations 9 and 13, each with a net value or social surplus of 24. The auctioneer will be indifferent between these two allocations in value terms, but also sure to recognize that the quality of the Allocation 9 dominates the quality of Allocation 13 due to the higher quality level for Item A in Allocation 9.

The suppliers' cost function for quality.

<table><tr><td rowspan="2">Suppliers (bidders)</td><td colspan="3">Trade items&#x27; supply bundles with costs assigned</td></tr><tr><td>ABC</td><td>AB</td><td>C</td></tr><tr><td>1</td><td>{3x,3x,4x}</td><td>#</td><td>#</td></tr><tr><td>2</td><td>#</td><td>{4x,2x}</td><td>#</td></tr><tr><td>3</td><td>#</td><td>#</td><td>{3x}</td></tr></table>

Note: # denotes available information for auctioneer/buyer (i.e., the “report”) doesn't include the corresponding bundles. x is quality score: 3 = low quality; 4 = high quality.

## 7.2. Payments to winning suppliers

We now consider the payment function for transfers from the auctioneer to the suppliers. According to our base case QA-VCG mechanism, we need to examine Allocations 9 and 13 separately to determine what Suppliers 2 and 3 earn. The payment to a winning supplier is $P _ { j } ( \hat { c } _ { j } ) = \bar { V } ( J ) + \hat { c } _ { j } \big ( \vec { \theta } _ { a ^ { - 1 } ( j ) } \big ) - V ( J j ) .$ . The <sup>fi</sup>rst term, $V ( J )$ , is <sup>ð Þ ð Þ ð Þ</sup>the maximum social surplus that can be achieved by having all suppliers' participate in the auction. The second term, $\hat { c } _ { j } \left( \overrightarrow { \boldsymbol { \theta } } _ { a ^ { - 1 } ( j ) } \right)$ , is the cost for the supplier associated with providing the corresponding goods to the auctioneer. The third term, $V ( J \backslash j )$ , is the maximum social surplus that can be achieved in the auction without supplier j's participation. So supplier j's payment includes the difference between the maximum achievable social surplus with or without her participation, plus the cost of her supply of the winning goods to the auctioneer that meets the quality requirements. If the auctioneer chooses Allocation 9, {H, H, H}, then the payments to the suppliers will be: (i) Supplier 2: $2 4 + 2 4 - 2 0 = 2 8$ , and (ii) Supplier $3 \colon 1 2 + 2 4 -$ $2 0 = 1 6 .$ . If the auctioneer chooses Allocation 13, {L, H, H}, then the payments to suppliers will be: (iii) Suppler $2 \colon 2 0 + 4 = 2 4$ , and (iv) Supplier $3 \colon 1 2 + 4 = 1 6$

The overall surplus of the auctioneer according in QA-VCG is determined based on the two optimal allocations. It is computed based on the corresponding utility of the bundle to the auctioneer, less the sum of payments to Suppliers 2 and 3. Thus, the auctioneer's revenue for Allocation 9 is given by $6 0 - 2 8 - 1 6 = 1 6$ , while that for Allocation 13 is given by $5 6 - 2 4 - 1 6 = 1 6 .$

## 7.3. The revised mechanism and its payment function

In the revised QA-VCG mechanism, the allocation and corresponding quality standard are the same as in the original base version of the mechanism. However, the payment to the winners in revised mechanism is now $P _ { j } ( \hat { c } _ { j } | \bar { c } _ { j } ) \stackrel { \left. \right)} { = } V ( J ) + \hat { c } _ { j } \left( \stackrel { \right. } { \theta } _ { a ^ { - 1 } ( j ) }  - V \left( J _ { - j } , \bar { c } _ { j } \right)$ . The reader should speci<sup>fi</sup>cally note that the third term is different, and supplier j has been assumed to have cost function $\overline { { c } } _ { j } ( \cdot )$ . Then $V ( J _ { - j } , \overline { { c } } _ { j } )$ is the least maximal social surplus with supplier j's participation, given the other suppliers' bids. We also know that $V ( J _ { - j } , \overline { { c } } _ { j } ) { \ge } V ( J \backslash j )$ j is true. Fo this example, we further assume a minimal decrease of one unit for the value of social surplus and in the payment scheme. We apply the cost function {4x, 2.75x} for Items AB as $\overline { { c } } _ { j } ( \cdot )$ for Supplier 2, and the cost function {3.75x} for Item C as c · for Supplier 3. In this way, we derived the revised payments for the winning suppliers in this auction as follows for Allocations 9 and 13. If the auctioneer chooses Allocation 9, {H, H, H}, then the revised payments are: (i) Supplier $2 \colon 2 4 + 2 4 - 2 1 = 2 7$ and (ii) Supplier $3 ; 2 4 + 1 2 - 2 1 = 1 5$ If the auctioneer chooses Allocation 13, {L, H, H}, then the revised payments are (iii) Suppler $2 : 2 0 + 3 = 2 3$ and (iv) Supplier $3 \colon 1 2 + 4 = 1 5$

The auctioneer's utility function for quality.

<table><tr><td rowspan="2"></td><td colspan="3">Trade items</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>Utility</td><td>4x</td><td>6x</td><td>5x</td></tr></table>

Note: x is the quality score, which is 3 for low quality and 4 for high quality.

Table 4  
Evaluation of the procurement combinatorial auction allocations.

<table><tr><td>Allocation</td><td>Quality</td><td>Utility</td><td>Cost</td><td>Net value</td></tr><tr><td colspan="5">Supplier 1 selected for procurement</td></tr><tr><td>1</td><td>{H,H,H}</td><td>60</td><td>40</td><td>20**</td></tr><tr><td>2</td><td>{H,H,L}</td><td>55</td><td>36</td><td>19</td></tr><tr><td>3</td><td>{H,L,H}</td><td>54</td><td>37</td><td>17</td></tr><tr><td>4</td><td>{H,L,L}</td><td>49</td><td>33</td><td>16</td></tr><tr><td>5</td><td>{L,H,H}</td><td>56</td><td>37</td><td>19</td></tr><tr><td>6</td><td>{L,H,L}</td><td>51</td><td>33</td><td>18</td></tr><tr><td>7</td><td>{L,L,H}</td><td>50</td><td>34</td><td>16</td></tr><tr><td>8</td><td>{L,L,L}</td><td>45</td><td>30</td><td>15</td></tr><tr><td colspan="5">Suppliers 2 and 3 selected for procurement</td></tr><tr><td>9</td><td>{H,H,H}</td><td>60</td><td>36</td><td>24***</td></tr><tr><td>10</td><td>{H,H,L}</td><td>55</td><td>33</td><td>22</td></tr><tr><td>11</td><td>{H,L,H}</td><td>54</td><td>34</td><td>20</td></tr><tr><td>12</td><td>{H,L,L}</td><td>49</td><td>31</td><td>18</td></tr><tr><td>13</td><td>{L,H,H}</td><td>56</td><td>32</td><td>24***</td></tr><tr><td>14</td><td>{L,H,L}</td><td>51</td><td>29</td><td>22</td></tr><tr><td>15</td><td>{L,L,H}</td><td>50</td><td>30</td><td>20</td></tr><tr><td>16</td><td>{L,L,L}</td><td>45</td><td>27</td><td>18</td></tr></table>

Note: The allocation algorithm is: (i) for supplier combinations that match the auctioneer's requirements, compute total utility, total cost and net value. (ii) Identify the highest net value allocation for each supplier combination. (iii) Select supplier allocation to maximize net value. (iv) If ties exist, apply other preferences to break ties. The asterisks are: \*\* = Supplier 1 can meet auctioneer's requirements alone, with maximum net value is 20; and \*\*\* = Suppliers 2 and 3 can jointly meet requirements, and maximum net value is 24

The revenue of the auctioneer according to the revised QA-VCG mechanism is again determined based on the two optimal allocations. It is computed via the utility of the bundle to the auctioneer, less the sum of payments to Suppliers 2 and 3. Thus, the auctioneer's surplus for Allocation 9 is given by $6 0 - 2 7 - 1 5 = 1 8$ , while that for Allocation 13 is given by $5 6 - 2 3 - 1 5 = 1 8$ . In both cases, the auctioneer's revenue is higher for the QA-VCG with the revised than for the base payment scheme, whose surpluses for the auctioneer were 16 for Allocations 9 and 13.

## 8. Extension: an iterative procurement cominatorial auction approach

We now extend our prior model to the case where truthful reporting of the suppliers' cost functions does not need to occur. (See Appendix B for additional details.) This is normally the case when the auction bidding process goes multiple rounds, as opposed to just being carried out in one shot. Truthful reporting is of limited interest in auctions that have multiple rounds of bidding. The reason is that if the bidders are truthful in what they bid in each round, their bids will be the same. This will lead, as a result, to an unchanged auction allocation outcome in every round. However, iterative auctions are known to dominate one-shot auctions in other ways, since they may help the suppliers to identify their preferences better. One piece of the problem is communication complexity, a measurement of the amount of information that bidders must provide to an auctioneer. In this respect, it is sometimes possible to use bidding language design to balance expressiveness and compactness. In addition, it is necessary to determine the valuations that the various auction participants place on outcomes at beginning of any transaction. Classic economic theory assumes that agents already know their preferences across different states of the world. This is a relatively strict assumption, which is not an appropriate model for many situations in which combinatorial auctions are relevant. Iterative combinatorial auctions relieve the valuation problem to some extent, because they allow bidders to adapt and focus on their valuation during an auction in response to feedback they receive, such as about the auction prices that are established in light of other suppliers' bids and the provisional allocations that are associated with them. In contrast, any ef<sup>fi</sup>cient one-shot auction requires bidders to report and determine their exact and complete valuations over all feasible outcomes.

Iterative auctions perform well in the laboratory and real world [49,57]. They proceed in a series of rounds, which last a speci<sup>fi</sup>ed period of time. During an auction round, the bidders have the chance to bid before the auctioneer determines the provisional winner of the round through the application of a winner determination algorithm. Then, the auctioneer will provide information about the outcome to the bidders, including the bid prices, the provisional allocation scheme and the quality standards supplied under the round's provisional outcome. This process repeats until the termination rules of the auction are satis<sup>fi</sup>ed. We next brie<sup>fl</sup>y explore an iterative assignment model to extend the combinatorial mechanism that we have been analyzing for public procurement.

The auctioneer, who is the buyer in the procurement case, will determine a winner and a provisional allocation that minimize her cost in each round. The auctioneer must respect the suppliers' bidding constraints though, and cannot allocate any single item to more than one supplier. The provisional allocation becomes the <sup>fi</sup>nal allocation when the auction terminates. The main differences between the winner determination process in procurement combinatorial auctions versus forward combinatorial auctions, in the quality assignment context we are considering, are that every item must be supplied, and competition in procurement relates not only to prices but also to quality standards bidding. Thus, there must be an optimization process for winner determination that involves a tradeoff between price and quality. With bidding strategies in iterative combinatorial auctions, a common assumption is that the bidders always make a myopic best response to the price and quality information that is made available following the provisional allocation that occurs in all of the auction rounds. The suppliers are myopic in the sense that they only consider currently allocated price and quality levels, and expect to maximize the pro<sup>fi</sup>ts through the consecutive bidding actions they make.

If one can design a set of auction rules with appropriate economic properties that cover supplier bidding, bundle assignment and evaluation, winner determination, and auction termination rules, the combinatorial auction will terminate with outcomes that satisfy allocation ef<sup>fi</sup>ciency. Combinatorial auction winner determination algorithms are often based on a general formulation for an integer programming combinatorial assignment problem [17]. We have developed an integer program for the iterative QA-VCG that uses an indicator variable to identify whether the auctioneer (or buyer in this case) receives a combinatorial bundle of goods with an attractive price that meets the quality standard. The objective function of the integer program that we specify is to compute the allocation scheme that maximizes value over all winning suppliers and the buyer, without allocating more than one bundle to any agent (via the <sup>fi</sup>rst constraint) and without allocating any item more than once (via the second constraint). We also offer additional results that suggest the ef<sup>fi</sup>cacy of a primal–dual problem formulation for winner determination for our iterative QA-VCG setting.

## 9. Conclusion

The most important issues in combinatorial auction design are obtaining ef<sup>fi</sup>cient allocations, achieving revenue maximization and encouraging truthfulness in bidding. Constraints on individual rationality and a balanced budget are of second-order importance. In quality assignment combinatorial procurement auctions, the auctioneer hopes to use the market mechanism to effectively procure goods or services at an attractive price, with reasonable costs and acceptable (if not optimal) quality. The special characteristics we have considered are the evaluation of choice of the quality standard levels for the suppliers' procurement items that the auctioneer wants to purchase. By combining the bene<sup>fi</sup>ts of the VCG mechanism [21,31,71,72] with quality assignment evaluation, our proposed QA-VCG mechanism provides a useful theoretical extension to prior research, and treats practical issues that arise in public sector combinatorial procurement auctions.

## 9.1. Contributions

To what kinds of settings will the proposed QA-VCG mechanism be most well suited? The key thing to keep in mind is that the mechanism is designed to maximize the total utility of the system as a whole, which we have described as the social surplus. This perspective takes into account the point of view of the auctioneer, who may represent government procurement interests, and the trade goods and services bundle suppliers, who may be either public or private entities. This consideration makes what we are proposing relevant in many different kinds of procurement settings, across a number of different countries. Our model formulates this in terms of the total utility of the system as the sum of the differences of the valuations of all the procured items based on the speci<sup>fi</sup>c quality requirements and corresponding costs. This formulation considers the aggregate value adjusted by the total costs. Compared with the optimization goal of the traditional VCG mechanism — which only adds the valuations of all the winning bidders together — our QA-VCG mechanism achieves a procurement solution that balances the government auctioneer's utility and the winning suppliers' costs. The incentive compatibility and the ex post participation constraint properties of QA-VCG further imply that this mechanism can preserve the advantageous properties of VCG in quality-related combinatorial procurement auctions. In other words, the goal of optimizing all winning bidders' utilities in the VCG mechanism becomes broader under our proposed QA-VCG mechanism. The goal shifts to including the optimization of joint utility, so that both the auctioneer and the winning suppliers are considered. In our view, the main difference that drives the necessity of this shift in optimization perspective is that quality-related combinatorial bidding and evaluation are bound up with both the suppliers' cost functions and the auctioneer's value function. Moreover, the original optimization goal of the VCG mechanism fails to effectively take into account aggregate social welfare.

Our QA-VCG mechanism, as we have shown in this article, is also incentive-compatible, quasi-participation constrained and ef<sup>fi</sup>cient in a setting that assumes quasi-linear preferences on the part of the suppliers. We modeled a setting in which the auctioneer has no private information. This setup meets the criteria required for ex post ef<sup>fi</sup>ciency for a dominant strategy incentive-compatible mechanism. Although the ex post participation constraint for the auctioneer is not satis<sup>fi</sup>ed in our QA-VCG mechanism, however, all suppliers still are individually rational in their bids, with valuations up to the limit of their costs. We also explored the theoretical reasons and practical background for why our QA-VCG mechanism works the way that it does. And we showed that the payment function must have a unique form, like the payment function in a Groves–Clarke mechanism, so that it is able to satisfy the dual criteria of ef<sup>fi</sup>ciency and incentive compatibility.

To minimize the procurement cost for the auctioneer, we proposed a new payment function that achieves lower cost for the buyer and is based on the original mechanism. The reader should recognize that the change we made to the payment function cannot increase the total social surplus. However, it shifts some value from the winning suppliers to the auctioneer, who is procuring supplies. For each winning supplier, we found that the decrease in the amount of pro<sup>fi</sup>t, compared with the original mechanism, is deterministic. For the interim stage of our QA-VCG mechanism, we applied Krishna's [46] version of the revenue equivalence theorem, and showed the maximal auctioneer's expected revenue property of the revised mechanism.

## 9.2. Limitations

There are three primary limitations of the current work. First, the winner determination problem in combinatorial auctions suggests that with considerable suppliers and corresponding possible bidding combinations, the feasibility and complexity of these allocations will be critical limiting factors for the viability of many mechanisms. We assumed enough suppliers to participate in the procurement auction, so that an allocation outcome, in terms of the subsets of all goods that are procured, will always exist. This may not always be true, of course. This permitted our QA-VCG mechanism to provide a theoretical solution for the optimization problem to ensure the best allocation outcome for the suppliers and auctioneer, in view of the applicable payment rules. The tensions between game theory solutions and computational solutions become critical when we consider applying QA-VCG to practical managerial problems, such as real-world supply chain procurement and forward combinatorial auctions. Fortunately, any feasible computation method, including heuristic or optimal algorithms for our pre-de<sup>fi</sup>ned auction structure, can be applied to our proposed mechanism. In other words, QA-VCG is suitable for general procurement combinatorial auctions and also speci<sup>fi</sup>c ones, but only if the chosen algorithm is able to <sup>fi</sup>nd solutions for Eq. (1). Computational problems in combinatorial assignments are a well-known practical problem, and they are not unique to the VCG mechanism family.

A second limitation is that we formulated our model as a one-shot auction. This required a strong assumption about the preferences of the suppliers: the suppliers need to know their preferences well enough from the start to be able to bid effectively, ignoring the need for a process to elicit their preferences and values. In contrast, iterative combinatorial auctions allow suppliers to submit different bids at different times. This makes sense because some bidding combinations may have package-contingent value. Consider the example of airline landing and takeoff rights. The airlines' valuation for different combinations of landing and takeoff slots will depend on the different feasible outcomes. Too many morning slots in a package, for example, may diminish the value of any individual morning slot. In contrast, in a package with slots over the full day, a few morning slots will be of higher value. We offered a plausible scheme for iterative procurement combinatorial auction based on this kind of underlying setting, and included the related assignment model in Appendix B.

Third, another controversial assumption in our model is that the suppliers supply just one speci<sup>fi</sup>c combination of goods via the QA-VCG mechanism. Thus, our thinking has been that each supplier is an all-or-nothing supplier who hopes to win with one supply combination only. Otherwise the supplier will not be able to make an auction transaction. This assumption eases the complexity of valuation for the auctioneer to solve its social choice problem and to make an ef<sup>fi</sup>cient and incentive-compatible procurement supply allocation. Complexity will determine how much computation will be needed to represent the complete preferences of the suppliers, so that the auctioneer is able to determine the appropriate allocations. This brings up another related and <sup>fi</sup>nal issue: the extent of communication (e.g., revelation of the suppliers' cost functions) that is required between the suppliers and the auctioneer to yield an optimal outcome with the mechanism. The idea of an all-or-nothing supplier is more reasonable in supply chain procurement settings, where the auctioneer or buyer is subject to other considerations about the transaction costs and risks inherent in spreading orders across multiple suppliers [22], and the possibility of supply and demand shocks that may require subsequent procurement renegotiation [39].

## Acknowledgments

We are grateful to the Associate Editor and the referees for their valuable comments. Jian Chen is partly supported by the National Natural Science Foundation of China (NSFC) under grant 70890082, the MOE, PR China, through the Project of the Key Research Institute of Humanities and Social Sciences in Universities under Grant 08JJD630001, and Tsinghua University Initiative Scienti<sup>fi</sup>c Research Program under grant 20101081741. Huang He is supported by National Natural Science Foundation of China under grants 71071171 and 70701040, and the Fundamental Research Funds for the Central Universities of China (Project No. CDJSK100200). Rob Kauffman also thanks the Research Center for Contemporary Management at Tsinghua University for generous support.

Appendix A. Proof of Proposition 3 (the payment functional form proposition)

The payment function in our model is as follows:

$$
\begin{array}{l} P _ {j} \Big (\hat {c} _ {j}, \hat {c} _ {- j} \Big) = V (J) + \sum_ {k \in a ^ {- 1} (j)} \hat {c} _ {j k} (\theta_ {k}) - V (J \setminus j) \\ = \sum_ {i \neq j} ^ {n} \left[ v _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) - \hat {c} _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) \right] + v _ {j} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (j)} \Big) - V (J \setminus j) \end{array}\tag{A1}
$$

The <sup>fi</sup>rst and third terms in Eq. (A1) do not include $\hat { c } _ { j } ( \cdot )$ . So we can rewrite Eq. (A1) as:

$$
P _ {j} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right) = \sum_ {i \neq j} ^ {n} \left[ v _ {i} \left(\overrightarrow {\theta} _ {a ^ {- 1} (i)}\right) - \hat {c} _ {i} \left(\overrightarrow {\theta} _ {a ^ {- 1} (i)}\right) \right] + v _ {j} \left(\overrightarrow {\theta} _ {a ^ {- 1} (j)}\right) - h _ {j} \left(\hat {c} _ {- j}\right)\tag{A2}
$$

where $h _ { j } ( \hat { c } _ { - j } )$ which is an arbitrary function that similarly excludes $\hat { c } _ { j } ( \cdot ) .$

<sup>Þ</sup>Next, suppose there is another form of the payment function $P _ { j } ^ { \prime } ( \hat { c } _ { j } , \hat { c } _ { - j } )$ in which the <sup>fi</sup>rst two terms are same as in Eq. (A2), but the last term is no longer independent of $\hat { c } _ { j } ( \cdot )$

$$
P _ {j} ^ {\prime} \big (\hat {c} _ {j}, \hat {c} _ {- j} \big) = V (J) + \sum_ {k \in a ^ {- 1} (j)} \hat {c} _ {j k} (\theta_ {k}) + h _ {j} \big (\hat {c} _ {j}, \hat {c} _ {- j} \big)\tag{A3}
$$

In this expression, $\hat { c } _ { - j }$ denotes the cost functions of other suppliers than supplier j.

We wish to show that $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } )$ must be independent of $\mathrm { \ddot { c } } _ { j } ( \cdot )$ if the <sup>ð Þ</sup>social choice function is truthfully-implemented by dominant strategies. We begin by assuming this is not so. So let the social choice function be truthfully implementable in dominant strategies, but for some $c _ { j } ( \cdot ) , \hat { c } _ { j } ( \cdot )$ and $\hat { c } _ { - j } ( \cdot )$ , we have

$$
h _ {j} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right) \neq h _ {j} \left(c _ {j}, \hat {c} _ {- j}\right)\tag{A4}
$$

We consider two cases as follows.

Case ${ \bf 1 . } \ \theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = \theta ^ { * } ( c _ { j } , \hat { c } _ { - j } )$ and $a ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = a ^ { * } ( c _ { j } , \hat { c } _ { - j } )$ , where $\theta ^ { * } \Big ( \hat { c } _ { j } , \hat { c } _ { - j } \Big )$ denotes the optimal quality assignment when supplier $j ^ { \prime } s$ reported cost is $\hat { c } _ { j } ( \cdot )$ , while the other suppliers' reports are $\hat { c } _ { - j } .$ $a ^ { \ast } \left( \hat { c } _ { j } , \hat { c } _ { - j } \right)$ denotes the optimal combinatorial allocation under the same reporting costs. Because the mechanism is incentive-compatible in the sense of the dominant strategy, the suppliers will report their cost functions truthfully. This leads to:

$$
P _ {j} ^ {\prime} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right) - \hat {c} _ {j} \left(a ^ {*} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right), \Theta^ {*} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right)\right) \geq P _ {j} ^ {\prime} \left(c _ {j}, \hat {c} _ {- j}\right) - \hat {c} _ {j} \left(a ^ {*} \left(c _ {j}, \hat {c} _ {- j}\right), \Theta^ {*} \left(c _ {j}, \hat {c} _ {- j}\right)\right)\tag{A5}
$$

$$
P _ {j} ^ {\prime} \left(c _ {j}, \hat {c} _ {- j}\right) - c _ {j} \left(a ^ {*} \left(c _ {j}, \hat {c} _ {- j}\right), \Theta^ {*} \left(c _ {j}, \hat {c} _ {- j}\right)\right) \geq P _ {j} ^ {\prime} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right) - c _ {j} \left(a ^ {*} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right), \Theta^ {*} \left(\hat {c} _ {j}, \hat {c} _ {- j}\right)\right)\tag{A6}
$$

Since, $\theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = \theta ^ { * } ( c _ { j } , \hat { c } _ { - j } )$ and a $( \hat { c } _ { j } , \hat { c } _ { - j } ) = a ^ { * } ( c _ { j } , \hat { c } _ { - j } )$ , Eqs. (A5) and (A6) together imply that $P _ { j } ^ { \prime } ( c _ { j } , \hat { c } _ { - j } ) = P _ { j } ^ { \prime } ( \hat { c } _ { j } , \hat { c } _ { - j } )$ . Also, based on Eq. (A3), we have $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = h _ { j } ( c _ { j } , \hat { c } _ { - j } )$ , which is a contradiction of Eq. (A4).

Case 2. Θ $\mathfrak { p } ^ { * } \left( \hat { c } _ { j } , \hat { c } _ { - j } \right) { \neq \theta } ^ { * } \left( c _ { j } , \hat { c } _ { - j } \right)$ and $a ^ { * } \left( \hat { c } _ { j } , \hat { c } _ { - j } \right) \neq a ^ { * } \left( c _ { j } , \hat { c } _ { - j } \right)$ , or one of these holds. Without loss of generality, suppose that $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } ) <$ $h _ { j } ( c _ { j } , \hat { c } _ { - j } )$ . Consider a speci<sup>fi</sup>c real cost function:

$$
c _ {j} ^ {\varepsilon} (a, \Theta) = \left\{ \begin{array}{l l} \sum_ {i \neq j} \left[ v _ {i} \Big (\vec {\theta} _ {a ^ {- 1} (i)} ^ {*} \Big) - \hat {c} _ {i} \Big (\vec {\theta} _ {a ^ {- 1} (i)} ^ {*} \Big) \right] + \sum_ {k \in a ^ {- 1} (j)} v _ {j k} (\theta_ {k} ^ {*}) - \varepsilon & \text { if } a = a ^ {*} \big (\hat {c} _ {j}, \hat {c} _ {- j} \big), \Theta = \Theta^ {*} \big (\hat {c} _ {j}, \hat {c} _ {- j} \big) \\ \sum_ {i \neq j} \left[ v _ {i} \Big (\vec {\theta} _ {a ^ {- 1} (i)} ^ {*} \Big) - \hat {c} _ {i} \Big (\vec {\theta} _ {a ^ {- 1} (i)} ^ {*} \Big) \right] + \sum_ {k \in a ^ {- 1} (j)} v _ {j k '} (\theta_ {k} ^ {*}) & \text { if } a = a ^ {*} \big (c _ {j}, \hat {c} _ {- j} \big), \Theta = \Theta^ {*} \big (c _ {j}, \hat {c} _ {- j} \big) \\ \infty & \text { if   others } \end{array} \right.\tag{A7}
$$

For a suf<sup>fi</sup>ciently small value of εN0, supplier j with cost function type $c _ { j } ^ { \varepsilon } ( \cdot )$ will prefer to falsely report her type when others' cost function types are $\hat { c } _ { - j } ( \cdot )$ . To see this, we note that due to Eq. (A7), $a ^ { \ast } \left( \hat { c } _ { j } , \hat { c } _ { - j } \right)$ and $\theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } )$ <sup>Þ</sup>will maximize the following:

$$
\sum_ {i \neq j} \left[ v \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) - \hat {c} _ {i} \Big (\overrightarrow {\theta} _ {a ^ {- 1} (i)} \Big) - \right] + \sum_ {k \in a ^ {- 1} (j)} v _ {j k} \pi (\theta_ {k}) - c _ {j} ^ {\varepsilon} (a, \Theta)\tag{A8}
$$

Note the social choice goal of social surplus maximization also is re<sup>fl</sup>ected in Eq. (A8). When other suppliers' reports are $\hat { c } _ { - j } ( \cdot )$ , the <sup>ð</sup>optimal allocations will be the same, whether supplier j reports $c _ { j } ^ { \varepsilon } ( \cdot )$ or $\hat { c } _ { j } ( \cdot )$ , so that $\Theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = \Theta ^ { * } \left( c _ { i } ^ { \varepsilon } , \hat { c } _ { - j } \right)$ and $a ^ { * } ( \bar { \hat { c } } _ { j } , \hat { c } _ { - j } ) \bar { = } \bar { a } ^ { * } \big ( c _ { i } ^ { \varepsilon } , \bar { \hat { c } } _ { - j } \big )$ <sup>ð Þ</sup>will be true. Thus, for truth-telling by suppler j with type $c _ { j } ^ { \varepsilon } ( \cdot )$ ) to be a dominant strategy, we require the following condition to be true:

$$
\begin{array}{l} P _ {j} ^ {\prime} \left(c _ {j} ^ {\varepsilon}, \hat {c} _ {- j}\right) - c _ {j} ^ {\varepsilon} \left(a ^ {*} \left(c _ {j} ^ {\varepsilon}, \hat {c} _ {- j}\right), \Theta^ {*} \left(c _ {j} ^ {\varepsilon}, \hat {c} _ {- j}\right)\right) \\ \geq P _ {j} ^ {\prime} \left(c _ {j}, \hat {c} _ {- j}\right) - c _ {j} ^ {\varepsilon} \left(a ^ {*} \left(c _ {j}, \hat {c} _ {- j}\right), \Theta^ {*} \left(c _ {j}, \hat {c} _ {- j}\right)\right) \end{array}\tag{A9}
$$

Substituting $\boldsymbol { l } ^ { * } \big ( \hat { c } _ { j } , \hat { c } _ { - j } \big )$ for $a ^ { * } \left( c _ { j } ^ { \varepsilon } , \hat { c } _ { - j } \right)$ , and $\theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } )$ for $\theta ^ { * } \left( c _ { j } ^ { \mathrm { { c } } } , \hat { c } _ { - j } \right)$ in Eq. (A9) yields:

$$
\begin{array}{l} P _ {j} ^ {\prime} \Big (c _ {j} ^ {\varepsilon}, \hat {c} _ {- j} \Big) - c _ {j} ^ {\varepsilon} \Big (a ^ {*} \Big (\hat {c} _ {j}, \hat {c} _ {- j} \Big), \Theta^ {*} \Big (\hat {c} _ {j}, \hat {c} _ {- j} \Big) \Big) \\ \geq P _ {j} ^ {\prime} \Big (c _ {j}, \hat {c} _ {- j} \Big) - c _ {j} ^ {\varepsilon} \Big (a ^ {*} \Big (c _ {j}, \hat {c} _ {- j} \Big), \Theta^ {*} \Big (c _ {j}, \hat {c} _ {- j} \Big) \Big) \end{array}\tag{A10}
$$

Further substitution of Eqs. (A3) and (A7) into Eq. (A10) gives:

$$
h _ {j} \left(c _ {j} ^ {\varepsilon}, \hat {c} _ {- j}\right) + \varepsilon \geq h _ {j} \left(c _ {j}, \hat {c} _ {- j}\right)\tag{A11}
$$

However by the result we obtained in Case 1, and by $\Theta ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = \Theta ^ { * } \mathbf { \check { ( } } c _ { j } ^ { \varepsilon } , \hat { c } _ { - j } )$ and $a ^ { * } ( \hat { c } _ { j } , \hat { c } _ { - j } ) = a ^ { * } \big ( c _ { j } ^ { \varepsilon } , \hat { c } _ { - j } \big )$ , we know that this gives $h _ { j } \Bigl ( c _ { j } ^ { \varepsilon } , \dot { c } _ { - j } \Bigr ) = \dot { h } _ { j } \bigl ( \hat { c } _ { j } , \hat { c } _ { - j } \bigr )$ . As a result, Eq. (A11) can be rewritten as $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } ) ^ { \top } + \varepsilon \geq h _ { j } ( c _ { j } , \hat { c } _ { - j } )$ . But, we know that $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } ) { < } h _ { j } ( c _ { j } , \hat { c } _ { - j } )$

∀j

∀a

So it must be the case that $h _ { j } ( \hat { c } _ { j } , \hat { c } _ { - j } ) + \varepsilon { \geq } h _ { j } ( c _ { j } , \hat { c } _ { - j } )$ will be violated for a small enough value of $\varepsilon > 0$ □

Appendix B. Integer program for iterative combinatorial procurement with quality assignment

The results we reported in Section 8 are based on the following integer program to solve an assignment model for multi-attribute combinatorial auctions.

$$
\underset {x _ {j} (q (s) ^ {*})} {\text { Max }} \sum_ {s} \sum_ {j} \left[ v (q (s)) ^ {*} - c _ {j} (q (s) ^ {*}) \right] \cdot x _ {j} (q (s) ^ {*})\tag{IP}
$$

$$
s. t. \sum_ {s} x _ {j} (q (s) ^ {*}) \leq 1,\tag{\((IP - 1)\}
$$

B1

$$
\sum_ {s (i)} \sum_ {j} x _ {j} \bigl (q (s (i)) ^ {*} \bigr) = 1,\tag{\((IP - 2)\}
$$

$$
x _ {j} (q (s) ^ {*}) \in \{0, 1 \},
$$

$$
\forall j, s
$$

In this model, the variables are as follows: j denotes a speci<sup>fi</sup>c supplier; i is an item; s is a goods bundle; $s ( i )$ is bundle s which contains item i; q(s) is a quality bid for bundle $s ; \nu ( q ( s ) ^ { * } )$ is the buyer's utility of bundle s with quality $q ( s ) ^ { * } ;$ and c<sub>j</sub> $\left( q ( s ) ^ { * } \right)$ is supplier j's cost of supplying s with $q ( s ) ^ { * }$ . Finally, $q ( s ) ^ { * } \in a r g$ max $[ v ( q ( s ) ) - c _ { j } ( q ( s ) ) ]$ q s <sup>ð Þ</sup>represents the most ef<sup>fi</sup>cient quality in terms of the transaction of bundle s between the buyer and supplier $j , x _ { j } ( q ( s ) ^ { * } )$ , and also $x _ { j } ( q ( s ( i ) ) ^ { * } )$ denotes whether supplier j wins the bundle s which contains item i. The optimization involves computing the winners' selection allocation and quality assignment that maximizes value over all winning suppliers, while minimizing the buyer's cost of procurement (which also re<sup>fl</sup>ects the maximization of buyer's value). The <sup>fi</sup>rst constraint ensures that no more than one bundle is supplied by supplier j to the buyer. The second constraint ensures that no item that is already allocated can be allocated another time.

In our further exploration of this integer program, we were able to achieve some useful results by transforming this problem to a linear program, well-known technique that has been used in numerous contexts (e.g., software project portfolio management [10], dynamic macroeconomic policy-making [12,41]). This permitted us to exploit the structure of the primal and dual optimization problems $[ 3 3 , 7 0 ] \textrm { -- }$ especially the complementary slackness conditions [26] — to make effective bundle allocations in the auction rounds. The mathematical translation from the primal to the dual problem involves the mapping of a maximization problem to a minimization problem in our case through the inversion of the constraint matrix. In addition, the coef<sup>fi</sup>cients of the objective function in the primal problem become the right hand side of the new constraints, while the inequality signs are reversed and the newly-speci<sup>fi</sup>ed variables continue to be required to be greater than or equal to zero. The procedure is generalizable to accommodate the kinds of constraints that are shown in the Primal Problem below. The quality and price bundle assignment models are presented as primal and dual linear programs in Eqs. (B2) and (B3). The <sup>fi</sup>rst is:

$$
\underset {x _ {j} (q (s ^ {*}), y (a)} {\text { Max }} \sum_ {s} \sum_ {j} \left[ v (q (s) ^ {*}) - c _ {j} (q (s) ^ {*}) \right] \cdot x _ {j} (q (s) ^ {*})\tag{LP}
$$

$$
s. t. \quad \sum_ {s} x _ {j} (q (s) ^ {*}) \leq 1, \quad \forall j\tag{LP-1}
$$

$$
\sum_ {j} x _ {j} \big (q (s) ^ {*} \big) \leq \sum_ {a \in A} y (a), \quad \forall s\tag{LP-2) Primal Problem}
$$

$$
\sum_ {s (i)} \sum_ {j} x _ {j} \bigl (q (s (i)) ^ {*} \bigr) \leq 1, \quad \forall i\tag{LP-3}
$$

$$
\sum_ {a} y (a) \leq 1\tag{LP-4}
$$

$$
x _ {j} \big (q (s) ^ {*} \big), y (a) \geq 0, \forall j, s, a\tag{B2}
$$

where a represents a speci<sup>fi</sup>c allocation including quality assignment; and y(a) is an indicator which denotes whether allocation a is chosen.

The second is:

$$
\underset {p (s) ^ {*}, \pi_ {j}, \Pi_ {A}} {\text { Min }} \sum_ {j} \pi_ {j} + \Pi_ {A}\tag{DP}
$$

$$
s. t. \quad \pi_ {j} (q (s) ^ {*}) \geq p (s) ^ {*} - c _ {j} (q (s) ^ {*}),
$$

$$
\forall j, s
$$

$$
\Pi_ {A} - \sum_ {s \in a} S ^ {e} (s) \geq 0,\tag{DP-1}
$$

Dual Problem

$$
\sum_ {s (i)} \pi_ {j} \bigl (q (s (i)) ^ {*} \bigr) \geq 0,\tag{DP-2}
$$

$$
\pi_ {j} \big (q (s) ^ {*} \big), S ^ {e} (s), \Pi_ {A} \geq 0,\tag{B3}
$$

where $p ( s ) ^ { * }$ is the price associated with bundle s; $\pi _ { j } , ( \pi _ { j } ( q ( s ) ^ { * } ) )$ $\pi _ { j } ( q ( s ) ^ { * } ) )$ is supplier j's maximal utility by supplying bundle s , with

$$
\begin{array}{l} \pi_ {j} = \underset {p (s) ^ {*}, q (s) ^ {*}} {\text { Max }} \Big [ p (s) ^ {*} - c _ {j} (q (s) ^ {*}) \Big ]; \\ \Pi_ {A} = \underset {a \in A} {\text { Max }} \sum_ {s \in a} \big [ v (q (s) ^ {*}) - p (s) ^ {*} \big ]; S ^ {e} (s) = v (q (s) ^ {*}) - p (s) ^ {*}. \end{array}
$$

The optimization objectives of the primal and dual math programs are similar: to maximize aggregate surplus or allocation ef<sup>fi</sup>ciency within the iterative QA-VCG. The programs optimize the sum of the all item utilities for the auctioneer / buyer, less the sum of the corresponding costs for the suppliers. This is the same thing, in essence, as what the earlier one-round QA-VCG was intended to accomplish, albeit with a somewhat different emphasis. Actually, primal–dual formulations like what we propose here are representative of a design paradigm for winner determination that is often used to solve combinatorial optimization problems in real-time [17]. Through the design of auction rules for speci<sup>fi</sup>c settings under a set of appropriate assumptions, we see that a quality assignment multiattribute iterative combinatorial procurement auction that implements a primal–dual winner determination algorithm permits us to develop bundle allocations that maximize allocation ef<sup>fi</sup>ciency.

## References

[1] L.M. Ausubel, Auction theory for the new economy, in: D. Jones (Ed.), New Economy Handbook, Academic Press/Elsevier, San Diego, CA, 2003, pp. 123–162.

[2] L.M. Ausubel, An ef<sup>fi</sup>cient ascending-bid auction for multiple objects, American Economic Review 94 (3) (2004) 1452-1475

[3] L.M. Ausubel, An ef<sup>fi</sup>cient dynamic auction for heterogeneous commodities, American Economic Review 96 (3) (2006) 602–629.

[4] L.M. Ausubel, P. Milgrom, Ascending auctions with package bidding, Frontiers of Theoretical Economics 1 (1) (2002) 1–42.

[5] L.M. Ausubel, P. Milgrom, The lovely but lonely Vickrey auction, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, Cambridge, MA, 2005, pp. 17–40.

[6] T. Baker, N.N. Murthy, A framework for estimating bene<sup>fi</sup>ts of using auctions in revenue management, Decision Science 33 (3) (2002) 385–413.

[7] T. Baker, N.N. Murthy, Viability of auction-based revenue management in sequential markets, Decision Science 36 (2) (2005) 259–286.

[8] J.S. Banks, J.O. Ledyard, D. Porter, Allocating uncertain and unresponsive resources: an experimental approach, Rand Journal of Economics 20 (1) (1989) 1–25.

[9] R. Bapna, P. Goes, A. Gupta, G. Karuga, Optimal design of the online auction channel: analytical, empirical, and computational insights, Decision Science 33 (4) (2002) 557–577.

[10] I. Bardhan, R.J. Kauffman, S. Naranpanawe, IT project portfolio optimization: a risk management approach to software development governance, IBM Journal of Research and Development 54 (2) (2010).1-18

[11] D.R. Beil, L.M. Wein, An inverse optimization-based auction mechanism to support a multiattribute RFQ process, Management Science 49 (11) (2003) 1529-1545.

[12] P. Benigno, M. Woodford, Optimal taxation in an RBC model: a linear–quadratic approach, Journal of Economic Dynamics and Control 30 (2006) 1445–1489.

[13] M. Bichler, J. Kalagnanam, Industrial procurement auctions, in: P. Cramton, Y. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, Cambridge, MA, 2006.

[14] M. Bichler, J. Kalagnanam, Software frameworks for advanced procurement auction markets, Communications of the ACM 49 (12) (2006) 104–108.

[15] M. Bichler L Kalagnanam K. Katircioglu A.I King R.D. Lawrence H.S. Lee G.Y. Lin Y. Lu, Applications of <sup>fl</sup>exible pricing in business-to-business electronic commerce IBM Systems Journal 41 (2) (2002) 287–302

[16] M. Bichler, J. Kalagnanam, H.S. Lee, Software frameworks for automated winner determination in electronic auctions, in: K. Bauknecht, A.M. Tjoa, G. Quirchmayr (Eds.), Lecture Notes in Computer Science, 2455, Springer Verlag, Berlin Germany, 2002, pp. 37–46.

[17] S. Bikhchandani, J. Ostroy, The package assignment model, Journal of Economic Theory 107 (2) (2002) 377–406.

[18] J.I. Bulow, J. Roberts, The simple economics of optimal auctions, Journal of Political Economy 97 (5) (1989) 1060–1090.

[19] J. Catalan, R. Epstein, M. Guajardo, D. Yung, C. Martinez, Solving multiple scenarios in a combinatorial auction, Computers and Operations Research 36 (10) (2009) 2752–2758.

[20] Y.K. Che, Design competition through multidimensional auctions, Rand Journal of Economics 24 (4) (1993) 668–681.

[21] E. Clarke, H. Fall, Multipart pricing of public goods, Public Choice 11 (1971) 17–33.

[22] E.K. Clemons, S.P. Reddi, M.C. Row, The impact of information technology on the organization of economic activity: the “move to the middle” hypothesis, Journal of Management Information Systems 10 (2) (1993) 9–36.

[23] P. Cramton, Y.T. Shoham, R. Steinberg (Eds.), Combinatorial Auctions, MIT Press, Cambridge, MA, 2005.

[24] R.W. Day, S. Raghavan, A combinatorial procurement auction featuring bundle price revelation without free-riding, Decision Support Systems 44 (3) (2008) 621–640.

[25] S. deVries, R. Vohra, Combinatorial auctions: a survey, INFORMS Journal of Computing 15 (3) (2003) 284–309.

[26] A.K. Dixit, Optimization in Economic Theory, 2nd Edition, Oxford University Press New York, NY, 1990.

[27] W. Elmaghraby, P. Keskinocak, Technology for transportation bidding at the Home Depot, in: C. Billington, T. Harrison, H. Lee, J. Neale (Eds.), The Practice of Supply Chain Management: Where Theory and Applications Converge, Kluwer, Amsterdam, Netherlands, 2003, pp. 245–258.

[28] R. Englebrecht-Wiggans, M. Shubik, R.M. Stark (Eds.), Auctions, Bidding, and Contracting: Uses and Theory, New York University Press, New York, NY, 1983.

[29] A. Gibbard, Manipulation of voting schemes, Econometrica 41 (4) (1973) 587–602.

[30] J. Green, J.J. Laffont, Characterization of a satisfactory mechanism for the revelation of preferences for public goods, Econometrica 45 (2) (1979) 427–438.

[31] T. Groves, Incentives in teams, Econometrica 41 (4) (1973) 617–631.

[32] Z. Hidvégi, W. Wang, A.B. Whinston, Binary Vickrey auction: a robust and ef<sup>fi</sup>cient multi-unit sealed-bid online auction protocol against buyer multi-identity bidding, Decision Support Systems 43 (2) (2007) 301–312.

[33] F.S. Hillier, G.L. Lieberman, Introduction to Operations Research, 8th Edition, Mc Graw Hill New York NY 2005

[34] G. Hohner, J. Rich, E. Ng, G. Reid, A.J. Davenport, R.K. Kalagnanam, H.S. Lee, C. An, Combinatorial and quality-discount procurement auctions with mutual bene<sup>fi</sup>ts at Mars Incorporated, Interfaces 33 (1) (2003) 23–35.

[35] B. Holmstrom, R.B. Myerson, Ef<sup>fi</sup>cient and durable decision rules with incomplete information, Econometrica 51 (6) (1983) 1799–1819.

[36] T. Hossain, J. Morgan, A test of revenue equivalence theory using <sup>fi</sup>eld experiments on eBay, working paper, Department of Economics, Princeton University, Princeton, NJ, 2003.

[37] P. Jehiel, B. Moldovanu, An economic perspective on auctions, Economic Policy 18 (36)(2003)271–308.

[38] J.H. Kagel, Auctions: a survey of experimental research, in: J.H. Kagel, A.E. Roth (Eds.), The Handbook of Experimental Economics, Princeton University Press, Princeton, NJ, 1995, pp. 501–585.

[39] R.J. Kauffman, H. Mohtadi, Proprietary and open systems adoption: a riskaugmented transactions cost perspective, Journal of Management Information Systems 21 (1) (2004) 137–166.

[40] F. Kelly, R. Steinberg, A combinatorial auction with multiple winners for universal service, Management Science 46 (4) (2000) 586–597.

[41] J. Kim, S.H. Kim, Two pitfalls of linearization models, Finance and Economics Discussion Series 2007–64, Divisions of Research & Statistics and Monetary Affairs, Federal Reserve Board, Washington, DC, 2007.

[42] P.D. Klemperer, Auction theory: a guide to the literature, Journal of Economic Surveys 13 (3) (1999) 227–286.

[43] P.D. Klemperer, What really matters in auction design, Journal of Economic Perspectives 16 (1) (2002) 169–189.

[44] P.D. Klemperer, Why every economist should learn some auction theory, in: M. Dewatripont, L. Hansen, S. Turnovsky (Eds.), Advanced in Economics and Econometrics: Invited Lectures to the 8th World Congress of the Econometric Society, 201, Cambridge University Press, Oxford, UK, 2003, pp. 25–55.

[45] P.D. Klemperer, Auctions: Theory and Practice, Princeton University Press, Princeton, NJ, 2004.

[46] V. Krishna, Auction Theory, Academic Press, New York, NY, 2002.

[47] V. Krishna, M. Perry, Ef<sup>fi</sup>cient mechanism design, working paper, Pennsylvania State University, State College, PA, and the Hebrew University of Jerusalem, Israel, 1998.

[48] V. Krishna, R.W. Rosenthal, Simultaneous auctions with synergies, Games and Economic Behavior 17 (1) (1996) 1–31.

[49] A.M. Kwasnica, J.O. Ledyard, D. Porter, C. DeMartini, A new and improved design for multiobjective iterative auctions, Management Science 51 (3) (2005) 419-434.

[50] J.O. Ledyard, M. Olson, D. Porter, J.A. Swanson, D.P. Torma, The <sup>fi</sup>rst use of a combined value auction for transportation services, Interfaces 32 (5) (2002) 4–12.

[51] C.G. Lee, R.H. Kwon, Z. Ma, A carrier's optimal bid generation problem in combinatorial auctions for transportation procurement, Transportation Research, Part E: Logistics and Transportation Review 43 (2) (2007) 173–191.

[52] A. Mas-Colell, M.D. Whinston, J.R. Green, Microeconomic Theory, Oxford University Press, Oxford, UK, 1995

[53] P. Milgrom, Putting Auction Theory to Work, Cambridge University Press, Cambridge, UK, 2004.

[54] R. Myerson, M. Satterthwaite, Ef<sup>fi</sup>cient mechanisms for bilateral trading, Journal of Economic Theory 29 (2) (1983) 265–281.

[55] N. Nisan, A. Ronen, Computationally feasible VCG mechanisms, working paper, Hebrew University of Jerusalem, Israel, 2001.

[56] N. Nisan, I. Segal, The communication complexity of ef<sup>fi</sup>cient allocation problems, working paper, Hebrew University of Jerusalem, Israel and Stanford University, Stanford, CA, 2002.

[57] D. Parkes, Iterative combinatorial auctions: achieving economic and computational ef<sup>fi</sup>ciency, doctoral thesis, Computer Science Department, University of Pennsylvania, Philadelphia, PA, 2001.

[58] D. Parkes, J.R. Kalagnanam, M. Eso, Achieving budget balance with Vickrey-based payment schemes in combinatorial exchanges, Proceedings of the 17th International Joint Conference on Arti<sup>fi</sup>cial Intelligence, Seattle, WA, August 4– 10, Morgan Kauffman, San Francisco, CA, 2001, pp. 1161–1168.

[59] A. Pekec, M.H. Rothkopf, Making the FCC's <sup>fi</sup>rst combinatorial auction work well, working paper, Federal Communications Commission, Washington, DC, 2000.

[60] A. Pekec, M.H. Rothkopf, Combinatorial auction design, Management Science 49 (11) (2003) 1485–1503.

[61] J.G. Riley, W.F. Samuelson, Optimal auctions, American Economic Review 71 (3) (1981) 381–392.

[62] M.H. Rothkopf, Thirteen reasons why the Vickrey–Clarke–Groves process is not practical, Operations Research 55 (2) (2007) 191–197.

[63] M.H. Rothkopf, A. Pekec, R.M. Harstad, Computationally manageable combina tional auctions, Management Science 44 (8) (1998) 1131–1146

[64] M.H. Rothkopf, T.J. Teisberg, E.P. Kahn, Why are Vickrey auctions rare? Journal of Political Economy 98 (1) (1990) 94–109.

[65] T.W. Sandholm, Approaches to winner determination in combinatorial auctions, Decision Support Systems 28 (1–2) (2000) 165–176.

[66] M.A. Satterthwaite, Strategy-proofness and Arrow's conditions: existence and correspondence theorems for voting procedures and social welfare functions, Journal of Economic Theory 10 (2) (1975) 187–217.

[67] D.F. Spulber, Market Microstructure: Intermediaries and the Theory of the Firm, Cambridge University Press, New York, NY, 1999.

[68] N. Sun, Z. Yang, Equilibria and indivisibilities: gross substitutes and complements, Econometrica 74 (4) (2006) 1385–1402.

[69] N. Sun, Z. Yang, A double-track adjustment process for discrete markets with substitutes and complements, Econometrica 77 (3) (2009) 933–952.

[70] H.R. Varian, Microeconomic Analysis, 3rd Edition, W.W. Norton, New York, NY, 2007.

[71] W.W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1) (1961) 8–36.

[72] W.W. Vickrey, Auction and bidding games, in: M. Maschler (Ed.), Recent Advances in Game Theory, Ivy Curtis Press, Philadelphia, PA, 1962, pp. 15–27.

[73] R.B. Wilson, Strategic analysis of auctions, in: R. Aumann, S. Hart (Eds.), Handbook of Game Theory, 1, North-Holland/Elsevier, Amsterdam, Netherlands, 1992, pp. 227–279.

![](/api/attachments/4D52JBT3/fulltext/images/2c14c011e0b2fda3b87fcefa7f406265193a8e1e8da48cf3cf8f3346360f18ad.jpg)

Chen Jian (jchen@tsinghua.edu.cn) received the B.Sc. degree in Electrical Engineering from Tsinghua University, Beijing, China, in 1983, and the M.Sc. and the Ph.D. degree both in Systems Engineering from Tsinghua University in 1986 and 1989. He is the Lenovo Chair Professor and Chairman of the Management Science Department, and Director of the Research Center for Contemporary Management, Tsinghua University. His main research interests include supply chain management, e-commerce, and decision support systems. Dr. Chen has published over 150 papers in refereed journals and has been a principal investigator for over 30 grants and research contracts with the National Science Foundation of China governmental

organizations and companies. He has been invited to present several plenary lectures. He is a past recipient of multiple awards and recognitions, including a Ministry of Education Changjiang Scholar Award, an IBM Faculty Award, and an Outstanding Contribution Award from the IEEE Systems, Man and Cybernetics Society. He has also been elected as an IEEE Fellow. He is the editor of Journal of Systems Science and Systems Engineering, an area editor of Electronic Commerce Research and Applications, an associate editor of IEEE Transactions on Systems, Man and Cybernetics: Part A, IEEE Transactions on Systems, Man and Cybernetics: Part C, and the Asia Pacific Journal of Operational Research. He also serves on multiple editorial boards of leading journals, including Flexible Services and Manufacturing, the International Journal of Electronic Business, International Journal of Information Technology and Decision Making, and Systems Research and Behavioral Science.

![](/api/attachments/4D52JBT3/fulltext/images/3bf13eda722b9a28bd970928e2d2b62c13084812c5717bb4e6a02f8153cd4a89.jpg)

Huang He is a Professor of Management Science in the School of Economics and Business Administration, Chongqing University, China. He received his Ph.D. degree in Management Science from the School of Economics and Management at Tsinghua University, Beijing, China in 2006. He was a visiting scholar in the Graduate School of Business, Columbia University in 2008 and 2009, and was a visiting faculty member at Hong Kong Polytechnic University in 2011. His publications appear in many different conferences and journals, including Electronic Commerce Research and Applications, the Journal of Systems Science and Systems Engineering, Lecture Notes on Computer Science, the Journal of Management Sciences in China, and Systems

Engineering — Theory & Practice. His current research interests focus on mechanism design, and the economic analysis of bargaining, contracts and procurement auctions.

![](/api/attachments/4D52JBT3/fulltext/images/34a1346b6f2296f4dc9a26804e176bb7a2d7ba8f9f1dd0e2d474c1c84b9172ed.jpg)

Robert J. Kauffman is a Visiting Professor of IS and Strategy at the School of Information and the Lee Kong Chian School of Business at Singapore University. He is also a Distinguished Visiting Fellow at the Glassmeyer–McNamee Center for Digital Strategies, Tuck School of Business, Dartmouth College. Previously, he served on the faculty at New York University, the University of Minnesota and Arizona State University. He also visited the University of Rochester and the Federal Reserve Bank of Philadelphia, and worked in international banking and <sup>fi</sup>nance in New York City prior to beginning his academic career. His graduate degrees are from Cornell University and Carnegie Mellon University, and his undergraduate degree is from the University of Colorado

Boulder. His research interests span the economics of IS, pricing and mechanism design on the Internet, competitive strategy, and theory development, modeling and empirical methods for IS and e-commerce research, all in contexts that emphasize senior management issues. His publications have appeared in Management Science, Information Systems Research, MIS Quarterly, the Journal of Management Information Systems Organization Science, the Review of Economics and Statistics, Decision Sciences, and other journals.
