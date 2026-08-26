---
otero_id: 21810
otero_key: "FEARYTFT"
title: "Approaches to winner determination in combinatorial auctions"
authors: "Tuomas Sandholm"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00066-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Approaches to winner determination in combinatorial auctions

Tuomas Sandholm )

Department of Computer Science, Washington UniÕersity, One Brookings DriÕe, St. Louis, MO 63130-4899, USA

## Abstract

Combinatorial auctions, i.e., auctions where bidders can bid on combinations of items, tend to lead to more efficient allocations than traditional auctions in multi-item auctions where the agents’ valuations of the items are not additive. However, determining the winners so as to maximize revenue is <sub>N P</sub>-complete.

First, existing approaches for tackling this problem are reviewed: exhaustive enumeration, dynamic programming, approximation algorithms, and restricting the allowable combinations. Then, we overview our new search algorithm for optimal anytime winner determination. By capitalizing on the fact that the space of bids is necessarily sparsely populated in practice, it enlarges the envelope of input sizes for which combinatorial auctions are computationally feasible. Finally, we discuss eMediator, our electronic commerce server that implements several techniques for automatically facilitating commerce, including an auction house with generalized combinatorial auctions. To our knowledge, our implementation is the first Internet auction to support combinatorial auctions, bidding via graphically drawn price–quantity graphs, and by mobile agents. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Combinatorial auction; Winner determination; Matching algorithms; Multi-agent system; Electronic commerce server

## 1. Introduction

Auctions are popular, distributed and autonomypreserving ways of allocating items among multiple agents. They are relatively efficient both in terms of process and outcome. They are extensively used among human bidders and among software agents in a variety of task and resource allocation problems. <sup>1</sup> Auctions can be used among cooperative agents, but they also work in open systems consisting of self-interested agents. An auction can be analyzed using noncooperative game theory: what strategies are self-interested agents best off using in the auction

Ž .and, therefore, will use , and will a desirable social outcome — e.g., efficient allocation — still follow. The goal is to design the protocols mechanisms ofŽ . the interaction so that desirable social outcomes follow even though each agent acts based on self-interest. This paper focuses on multi-item auctions, i.e., auctions where there is more than one item to be allocated.

## 1.1. Sequential auctions

In a sequential auction, the items are auctioned one at a time. Determining the winners in such protocols is easy because that can be done by picking the highest bidder for each item separately. However, if a bidder has preferences over bundles Ž . combinations of items , then bidding in such auctions is difficult. To determine her valuation for an item, the bidder needs to guess what items she will receive in later auctions. This requires speculation of what the others will bid in the future because that affects what items she will receive. Furthermore, what the others bid in the future depends on what they believe of others, etc. This counterspeculation introduces computational cost and other wasteful overhead. Moreover, in auctions with a reasonable number of items, such look-ahead in the game tree is intractable, and then there is no known way to bid rationally. Bidding rationally would involve optimally trading off the cost of look-ahead against the gains it provides, but that would again depend on how others strike that tradeoff. Furthermore, even if look-ahead were computationally manageable, usually some uncertainty remains about the others’ bids because agents do not have exact information about each other. This can lead to inefficient allocations where bidders do not get the combinations that they want and do get combinations that they do not want.

## 1.2. Parallel auctions

An alternative to a sequential auction is a parallel auction, in which the items are opened for auction in parallel. This has the advantage that the others’ bids partially signal to the bidder about what the others bids will end up being for the different items, so the uncertainty and the need for look-ahead is not as drastic as in a sequential auction. However, the same problems prevail, albeit in a mitigated form. For example, when bidding for an item, the bidder does not know her valuation because it depends on which other items she wins, which in turn depends on how others will bid. Even in open-cry auctions, this may only become known later to the bidder.<sup>2</sup>

In parallel auctions, an additional difficulty arises: each bidder would like to wait until the end to see what the going prices will be, and to optimize her bids so as to maximize payoff given the final prices. Because every bidder would want to wait, no bidding would commence. As a patch to this problem, activity rules have been used 12 . Each bidder has to bid<sup>w</sup> <sup>x</sup> at least a certain volume by predefined time points in the auction, otherwise, the bidder’s future rights are reduced in some prespecified manner. Unfortunately, the equilibrium bidding strategies in such auctions are not game-theoretically known. It follows that the outcomes of such auctions are unknown for rational bidders.

## 1.3. Methods for fixing inefficient allocations in sequential and parallel auctions

In sequential and parallel auctions, the computational cost of look-ahead and counterspeculation cannot be recovered, but one can attempt to fix the inefficient allocations that stem from the uncertainties discussed above.

One such approach is to set up an after market where the bidders can exchange items among themselves after the auction has closed. While this approach can undo some inefficiencies, it may not lead to a Pareto efficient allocation in general, and even if it does, that may take an impractically large number of exchanges 20 .<sup>w</sup> <sup>x</sup>

Another approach is to allow bidders to retract their bids if they do not get the combinations that they want. For example, in the Federal Communications Commission’s bandwidth auction, the bidders were allowed to retract their bids. In case of a retraction, the item was opened for re-auction 12 . If<sup>w</sup> <sup>x</sup> the new winning price was lower than the old one, the bidder that retracted the bid had to pay the difference. This guarantees that retractions do not decrease the auctioneer’s payoff. However, it exposes the retracting bidder to considerable risk.

This risk can be eliminated by what we call a leÕeled commitment protocol 24,25 , where the de- <sup>w</sup> <sup>x</sup> committing penalties are set up front, possibly on a per item basis. This protocol allows the bidders to decommit but it also allows the auctioneer to decommit. A bidder may want to decommit for example if she did not get the combination that she wanted but only a subset of it. The auctioneer may want to decommit for example if he believes that he can get a higher price for the item later on. The leveled commitment protocol has interesting gaming aspects: the agents do not decommit truthfully because there is a chance that the other agent will decommit, in which case the former agent is freed from the contract obligations, does not have to pay the decommitment penalty, and will collect a penalty from the latter agent. We have shown that despite this gaming, in Nash equilibrium, the protocol can increase the expected payoff of both parties, and enable contracts that would not be individually rational to both parties via any full commitment contract 1,2,19,25 .<sup>w</sup> <sup>x</sup>

Yet another approach would be to sell options for decommitting, where the price of the option would be paid up front regardless of whether it is actually exercised.

Each one of the methods above can be used to implement bid retraction before and<sup>r</sup>or after the winning bids have been determined.

While these methods can be used to try to fix inefficient allocations, it would clearly be desirable to get efficient allocations right away in the auction itself, so no fixing would be required. Combinatorial auctions hold significant promise toward that goal.

## 1.4. Combinatorial auctions

One approach to overcome the need for look-ahead and to overcome the inefficiencies that stem from related uncertainties is to use combinatorial auctions <sup>w</sup> <sup>x</sup> 13,14,17,18 . In a combinatorial auction, bidders may place bids on combinations of items. This allows the bidders to express complementarities between items instead of having to speculate into an item’s valuation the impact of possibly getting other, complementary items.

This paper focuses on combinatorial auctions where a bidder can bid on combinations of items, and her bids are joined with non-exclusive OR, meaning that any number of the bids may get accepted. We will also restrict our attention to settings where there is only one indivisible unit of each item. While these restrictions are common in the literature on combinatorial auctions 16 , winner determination<sup>w</sup> <sup>x</sup> methods have also been developed for cases where these assumptions are relaxed 14 . Such more gen- <sup>w</sup> <sup>x</sup> eral auctions are discussed in Section 9.

While combinatorial auctions have the desirable feature that they can avoid the need for look-ahead by the bidders, they do impose significant complexity on the auctioneer because he needs to determine the winners. This nontrivial task is the focus of the rest of the paper.

## 2. Winner determination in combinatorial auctions

The determination of winners — i.e., determining what items each bidder gets — is easy in non-combinatorial auctions. It can be done by picking the highest bidder for each item separately. This takes O amŽ . time where a is the number of bidders, and m is the number of items. In such auctions, determining the Vickrey price of each item is equally easy: it can be done in O am Ž . time by simply finding the second highest bid for each item.

Winner determination in combinatorial auctions is more difficult. Let M be the set of items to be auctioned. Then any agent, i, could place any bid $b _ { i } ( S )$ for any combination $S \subseteq M$

As a first preprocessing step to tackle winner determination, we observe that only the highest bid

Level

![](/api/attachments/FEARYTFT/fulltext/images/8c93429cf42c134502170c396e7ae95598ef4332f5021c964d29ba94e3445f79.jpg)

(1)

Fig. 1. Space of allocations in a four-item example. Each node represents one possible allocation $\mathcal { X } .$

for each combination needs to be considered. Formally, let <sup>3</sup>

$$
\overline {{b}} (S) = \max _ {i \in \text { bidders }} b _ {i} (S)\tag{1}
$$

The other bids for each combination can be deleted, as can bids of non-positive price. From now on when we talk about bids, we refer to the bids that remain after these straightforward deletions. Let n be the number of such remaining bids.

Now, winner determination in a combinatorial auction is the following problem, where the goal is to maximize the auctioneer’s revenue:

$$
\max _ {\mathscr {X} \in \mathscr {A}} \sum_ {S \in \mathscr {X}} \bar {b} (S)\tag{2}
$$

where $\mathcal { X }$ is a valid outcome, i.e., an outcome where each item is allocated to at most one bidder. Formally, let $S = \{ S \subseteq M \}$ . Then, the set of valid outcomes is $\mathcal { A } = \left\{ \mathcal { W } \subseteq \mathcal { S } | S , S ^ { \prime } \in \mathcal { W } \Rightarrow S \cap S ^ { \prime } = \emptyset \right\}$

## 3. Exhaustive enumeration

If each combination of items has received at least one bid of positive price, the search space of allocations will look like the graph in Fig. 1.

The number of allocations grows rapidly as the number of agents increases. The exact number of allocations is

$$
\sum_ {q = 1} ^ {m} Z (m, q)\tag{3}
$$

where $Z ( m , q )$ is the number of allocations with $q$ accepted bids, i.e., the number of allocations on level $q$ of the graph. The quantity $Z ( m , q )$ — also known as the Stirling number of the second kind — is captured by the following recurrence:

$$
Z (m, q) = q Z (m - 1, q) + Z (m - 1, q - 1),\tag{4}
$$

where $Z ( m , m ) = Z ( m , 1 ) = 1$ . This recurrence can be understood by considering the addition of a new item to a setting with $m - 1$ items. The first term, $q Z ( m$ $- \operatorname { 1 } , q )$ , counts the number of allocations formed by adding the new item to one of the existing allocations. There are $q$ choices because the existing allocations have q accepted bids. The second term, $Z ( m - 1 , q - 1 )$ , considers using the new item in a bid of its own, and, therefore, existing allocations with only $m - 1$ previously accepted bids are counted.

The following proposition characterizes the asymptotic complexity in closed form we give the Ž proof in Ref. 23 : <sup>w</sup> <sup>x</sup>.

Proposition 1. The number of allocations is $O ( m ^ { m } )$ and $\omega ( m ^ { m / 2 } )$ .

The number of such allocations is so large that not all allocations can be enumerated unless the number of items is extremely small — below a dozen or so in practice. Therefore, exhaustive enumeration is not a viable method for searching for the optimal allocation in most settings.

## 4. <sub>N</sub> <sub>P</sub>-completeness

Some combinations of items may not have received any bids, so some of the allocations in the graph need not be considered. Therefore, the relevant question is not how many allocations there might be if the space of bids were completely populated, but instead, can the optimal allocation be found quickly, e.g., in time that is polynomial in the actual input.

The winner determination problem is the same problem as the abstract problem called weighted set packing once we view each bid as a set and the price, b SŽ ., as the weight of the set S. The fact that weighted set packing is <sub>N</sub> <sub>P</sub>-complete 10 means <sup>w</sup> <sup>x</sup> that, unless $\mathcal { P } = \mathcal { N P }$ , no algorithm can find a revenue maximizing allocation in combinatorial auctions in polynomial time.

For example, in the airwave bandwidth auctions, the FCC recognized that the bidders’ valuations of the items will be non-additive, and that this fact could be capitalized on by using combinatorial auctions where the bidders can express complementarities by bidding on combinations of items instead of only on individual items. However, the FCC did not use a combinatorial auction protocol because they realized that they might not be able to determine the winners.

Sections 5–8 discuss different approaches to tackling the winner determination problem.

## 5. Dynamic programming

One approach to optimal winner determination is to use dynamic programming instead of exhaustive enumeration in the graph of Fig. 1. This has been discussed by Rothkopf et al. 16 . Based on the<sup>w</sup> <sup>x</sup> ${ \overline { { b } } } ( S )$ function, the dynamic programming algorithm determines for each set S of items the highest possible revenue that can be acquired using only the items in S. The algorithm proceeds systematically from the smallest sets to the largest. The needed optimal substructure property comes from the fact that for each set S, the maximal revenue comes either from a single bid b SŽ ., or from the sum of the maximal revenues of two disjoint exhaustive subsets of S. For each S, all possible subsets together with that sub-Ž set’s complement in S. are tried.

The savings compared to exhaustive search come from the fact that the revenue maximizing solutions for the subsets need not be computed over and over again, but only once. The dynamic programming algorithm takes $\Omega ( 2 ^ { m } )$ and $O ( 3 ^ { m } )$ steps 16 , which<sup>w</sup> <sup>x</sup> is a considerable saving over exhaustive enumeration, but still too complex to scale to large numbers of items above about 20–30 .Ž .

A key observation here is that the dynamic programming algorithm takes the same number of steps independent of the number of actual bids. This is because the algorithm generates each combination S even if no bids have been placed on S. Interpreted positively, this means that the auctioneer can determine ex ante how long winner determination will take regardless of the number of bids that will be received. Interpreted negatively, this means that the algorithm will scale only to a small number of items even if the number of bids is relatively small. In Section 8, we will present a search algorithm that avoids the generation of combinations for which bids have not been placed. That algorithm scales well to large numbers of items if the number of bids is relatively small.

## 6. Polynomial time approximation algorithms

Another way to achieve tractability is to try to find a reasonably good outcome $\mathcal { X }$ instead of an optimal one. One would then like to trade off the expected cost of additional computation cost of theŽ computational resources and cost associated with delaying the result against the expected improve-. ment in $\mathcal { X }$ . Instead of using expectations, one could try to devise an algorithm that will establish a worst case bound, i.e., guarantee that the value of the best allocation $\mathcal { X }$ is no more than some constant say Ž . k times the value of the best $\mathcal { X }$ found by the algorithm. A considerable amount of research has focused on generating such approximation algorithms that execute in polynomial time in the size of the input.

## 6.1. General case

Unfortunately, a recent inapproximability result of Hastad for the maximum clique problem 8 can be˚ <sup>w</sup> <sup>x</sup> used to show that no polynomial time algorithm can guarantee a bound $k \leq n ^ { 1 - \epsilon }$ for any $\epsilon > 0$ for the winner determination problem unlessŽ $\mathcal { N P }$ equals probabilistic polynomial time 21 . Therefore, the . <sup>w</sup> <sup>x</sup> approach of constructing polynomial time approximation algorithms with worst case guarantees is a futile effort in the winner determination problem. Even a bound $k = 2$ would mean that the algorithm might only capture 50% of the available revenue, and usually $k \gg 2$ so the guarantee would be even weaker.

One could also ask whether randomized algorithms would help in the winner determination problem. It is conceivable that randomization could provide some improvement over deterministic algorithms. However, the inapproximability result applies to randomized algorithms as well.

## 6.2. Special cases

While the general winner determination problem is inapproximable, one can do somewhat better in special cases where the bids have special structure. For example, there might be some cap on the number of items per bid, or there might be some cap on the number of bids with which a bid can share items.

The desired special structure could be enforced on the bidders by restricting the allowable bids al-Ž though this can lead to some of the same inefficiencies as non-combinatorial auctions because bidders may not be allowed to bid on the combinations they want or the auctioneer can allow general bids and . use these algorithms if the bids happen to exhibit the desired structure.

Several novel approximation algorithms 3,6,7,9<sup>w</sup> <sup>x</sup> have been developed for special cases of the weighted independent set problem and the weighted set packing problem, and they could be directly used for the corresponding special cases of the winner determination problem. Unfortunately, even these algorithms give bounds that are so weak that they are irrelevant for the winner determination problem in practice.

Approximation algorithms for the known special cases have been improved repeatedly. There is also the possibility that probabilistic algorithms could improve upon the deterministic ones. In addition, it is possible that additional special cases with desirable approximability properties will be found. For example, while the current approximation algorithms are based on restrictions on the structure of bids and items, a new family of restrictions that will very likely lend itself to approximation stems from limitations on the prices. For example, if the function b SŽ . is close to additive, approximation should be easy. Unfortunately, it does not seem reasonable for the auctioneer to restrict the bid prices or to eliminate outlier bids after the bids have been submitted. Setting an upper bound could reduce the auctioneer’s revenue because higher bids would not occur. Setting a lower bound above zero would possibly disable bidders with lower valuations from bidding, and it might happen that no bids on the respective items would be placed. Again, that would reduce the auctioneer’s revenue. However, the auctioneer could capitalize on special price structure if such structure happens to be present in the bids.

## 7. Restricting the combinations to guarantee optimal winner determination in polynomial time

If even more severe restrictions apply to the bids, winner determination can be carried out optimally in polynomial time. To capitalize on this idea in practice, the restrictions would have to be imposed by the auctioneer since they at least the currently knownŽ ones 16 are so severe that it is very unlikely that<sup>w</sup> <sup>x</sup>. they would hold by chance.

Imposing restrictions on the bids introduces some of the same inefficiencies that are present in noncombinatorial auctions because the bidders may be barred from bidding on the combinations that they want. There is an inherent tradeoff here between computational complexity and economic efficiency. Imposing certain restrictions on bids achieves provably tractable winner determination but gives rise to economic inefficiencies.

## 8. Our optimal anytime search algorithm

We recently generated another approach for optimal winner determination. We briefly review that approach here. The technical details of the highly optimized algorithm<sup>4</sup> are beyond the scope of this article. They can be found in Ref. 21 together with <sup>w</sup> <sup>x</sup> experimental results.

The motivations behind our approach are the following.

– To allow all combinations to be bid on unlike the approach of Rothkopf et al. This is in order not to introduce any of the inefficiencies that occur in non-combinatorial auctions.

– To strive for the optimal solution instead of an approximation. This maximizes the seller’s revenue. If this optimal winner determination takes more time than is available, the algorithm can be prematurely terminated with a feasible monotonically improving suboptimal solution in hand.

– To completely avoid loops and redundant generation of vertices when searching the graph of allocations Fig. 1 .Ž .

– To capitalize heavily on the sparseness of bids–unlike dynamic programming which uses the same amount of time irrespective of the number of bids. In practice the space of bids is necessarily extremely sparsely populated. For example, even if there are only 100 items to be auctioned, there are

$2 ^ { 1 0 0 } - 1$ combinations, and it would take longer than the life of the universe to bid on all of them even if every person in the world submitted a bid per second. Sparseness of bids implies sparseness of the allocations $\mathcal { X }$ that need to be checked. Our algorithm constructively checks each allocation $\mathcal { X }$ that has positive value exactly once, and does not construct the other allocations. Therefore, unlike dynamic programming, the algorithm only generates those parts of the search space that are actually populated by bids.

To achieve these goals, we use a search algorithm that generates a tree. Each path consists of a sequence of bids, and each path terminates when all items have been used on that path. At that point, the path corresponds to a feasible allocation, and the revenue from that allocation can be compared to the best one found so far. Fig. 2 demonstrates the kind of search tree that our algorithm generates.

The resulting search generates each allocation that has positive revenue exactly once, and searches through no other allocations, i.e. it eliminates redundant search. The fact that each allocation of positive value is checked guarantees that the algorithm finds the optimal solution.

The algorithm was implemented as depth-first search, which executes in linear space. The depth-first strategy causes feasible allocations to be found quickly, and the solution improves monotonically since the algorithm keeps track of the best solution found so far. This implements the anytime feature: if the algorithm does not complete in the desired amount of time, it can be terminated prematurely, and it guarantees a feasible solution that improves monotonically in time.

![](/api/attachments/FEARYTFT/fulltext/images/cf85fd997a318d6f437658c49940dede655541aee7440da8d506d6c213a56d12.jpg)  
Fig. 2. A small example search tree generated by our algorithm.

Not surprisingly, the worst case complexity is ${ \mathrm { O } } ( { \mathrm { n } } ^ { \mathrm { m } } )$ . However, we reemphasize the fact that n is the number of bids actually received, not the number of allowable combination of items. The depth-first version was experimentally tested on a general-purpose uniprocessor workstation. For easy bid distributions, it handles 400 items and 400 bids optimally in minutes, while for difficult distributions it can determine the optimal allocations up to about 80 items and 80 bids in that time. When testing the anytime feature, it turned out that in practice most of the revenue was generated early on as desired, and there were diminishing returns to computation.

The same search tree can be searched more efficiently without compromising optimality by using an iterative deepening $\mathbf { A } ^ { * }$ search strategy 11 with a<sup>w</sup> <sup>x</sup> Ž heuristic that we developed specifically for the winner determination application instead of depth-first. search 21 . Furthermore, before the main search we<sup>w</sup> <sup>x</sup> run a preprocessing search that removes all the bids that are provably noncompetitive. This makes the main search faster without compromising optimality. A bid prunee is noncompetitive if there is someŽ . disjoint collection of subsets of that bid such that the sum of the bid prices of the subsets exceeds or equals the price of the prunee bid. For example, a US\$10 bid for items 1, 2, 3, and 4 would be pruned by a US\$6 bid for item 1 and a US\$7 bid for items 2 and 4. The preprocessing is done by conducting a search analogous to the main search for each bidŽ . Ž . potential prunee separately, but now restricting the search to those bids that only include items that the prunee bid includes. We also use several additional preprocessing methods 21 . The preprocessors could<sup>w</sup> <sup>x</sup> as well be used in conjunction with other approaches to winner determination than our main search algorithm.

## 9. eMediator and generalized combinatorial auctions

During the last year and a half, we built a next generation electronic commerce server called eMediator <sup>w</sup> <sup>x</sup> 22 . One of the services it provides is a free-touse third party auction house. Several commercial and academic 15,26 auction houses have recently <sup>w</sup> <sup>x</sup> appeared on the Internet, but to our knowledge, ours is the first — and, currently, the only — Internet auction that supports combinatorial auctions.

The methods of conquering the intractability of winner determination, discussed above, are based on the common assumption that the bids are super-additive: $\mathbf { \bar { b } } ( S \cup S ^ { \prime } ) \geq \mathbf { \bar { b } } ( S ) + \mathbf { \bar { b } } ( S ^ { \prime } )$ . But what would happen if agent 1 bid $b _ { 1 } ( \{ 1 \} ) = 5 , \ b _ { 1 } ( \{ 2 \} ) = 4 ,$ and $b _ { 1 } ( \{ 1 , 2 \} ) = 7$ , and there were no other bidders? The auctioneer could allocate items 1 and 2 to agent 1 separately, and that agent’s bid for the combination would value at $5 + 4 = 9$ instead of 7. So, the current techniques focus on situations where combinational bids are introduced to capture synergies posi- Ž tive complementarities among items. On the other. hand, in many real world settings local subadditivities substitutability can occur as well. For example, Ž . when bidding for a landing slot for a plane, the bidder is willing to take any one of a host of slots, but does not want more than one.

To address this, eMediator allows the bidders to submit XOR-bids, i.e., bids on combinations such that only one of the combinations can get accepted. This allows the bidders to express general preferences with both positive and negative complementarities.

To allow an efficient allocation to be reached, it would be desirable to extract truthful valuation revelations as the bids to the auctioneer. Bidding truthfully can be made incentive compatible a dominantŽ strategy by using the Groves–Clarke pricing mecha-. nism 4,5 together with XOR-bids. This motivates<sup>w</sup> <sup>x</sup> each bidder to bid truthfully irrespective of what the others bid. That renders counterspeculation unnecessary. The auction house of eMediator support the Groves–Clarke mechanism in a way that applies to XOR-bids. The winning bids are determined to be those that together maximize the auctioneer’s rev-Ž . enue while respecting the exclusiveness of XOR,Ž and while allocating each item to at most one bidder .. The amount that an agent needs to pay is computed as the sum of the others’ winning bids had that agent not submitted any bids, minus the sum of the others’ winning bids in the actual optimal allocation. Therefore, the winner determination problem has to be solved once overall, and once per winning agent without any of that agent’s bids. This makes fast winner determination even more crucial. Note that, for example, just removing one winning bid at a time would not constitute an incentive-compatible mechanism. Incentive compatibility can also be lost if either winner determination or price determination is done only approximately. eMediator supports multiple different pricing schemes including the Groves– Clarke mechanism and a scheme where each winning bidder pays the prices of her winning bids.

Our current work focuses on developing faster optimal winner determination algorithms for XORbids. Naturally, this problem is even harder than the basic winner determination problem because the latter is a special case of the former. Therefore, the negative results, <sub>N</sub> <sub>P</sub>-completeness and inapproximability, apply to this setting as well.

We are also developing optimal matching algorithms for other generalizations such as double auctions instead of just single-sided auctions. Allowing combinatorial bidding in continuous double auctions is particularly important in illiquid or highly volatile markets where it is unsure whether one can acquire the items of the desired bundle one at a time. During the time when we are developing optimal matching algorithms for this type of combinatorial auctions, we use approximate matching algorithms for this setting in eMediator.

eMediator also supports the generalization of combinatorial auctions where the auction allows the agents to bid for multiple units of each item of a combination. This splits into two cases depending on whether the matches of units have to be exact or whether partial matches are allowed. Both singlesided and double auctions with multiple units are supported. In single-sided auctions, the auctioneer who sets up the auction can choose between using the Groves–Clarke pricing scheme and the scheme where each winning bidder pays the prices of her winning bids.

The convenience of using combinatorial auctions is an important issue. While XOR-bids allow the bidder to express general preferences, in the worst case this would involve placing a bid for each of the 2 <sup>m y</sup>1 possible combinations. A shorter representation of preferences without loss of expressive power could be possible by allowing a richer input language. One idea toward this direction was presented early on by Rassenti et al. 14 . They allowed the bidder to place combinational bids and to state the maximal number of combinations that could be accepted. An XOR-bid is a special case of this where that number is one. eMediator follows another approach. It allows the user to submit multiple XORbids. These multiple bids are combined together with a non-exclusive OR. This maintains full expressive power and tends to lead to significantly shorter inputs from the users than XOR-bids only at leastŽ the input that is required to express particular preferences cannot be longer than with XOR-bids since this method is a strict generalization of XOR-bids .. Due to full expressiveness of the language, the Groves–Clarke pricing scheme can be used to motivate bidders to bid truthfully here as well. eMediator supports that pricing scheme in this context also.

Fig. 3 shows the interface that eMediator provides for XOR-bidding when there are potentially multiple units of each item. The table in the figure is one XOR-bid, i.e., the rows are combined with exclusive OR. To submit multiple non-exclusively joined XOR-bids, the user can submit multiple tables. The example is from an electricity market scenario where the agents can bid for combinations of electricity for different hours of the day, and for multiple megawatt hours for each hour of the day.

Other enrichments to the input language are also possible. Since even basic XOR-bids have full expressive power, expressiveness should be viewed as a necessary but not sufficient condition. Between fully expressive input languages, the appropriate comparison criterion is the convenience of their use in the particular application domain in question. This could be measured via questionnaires in field trials, but it could also be addressed formally, for example, by defining convenience as the average- or worst-case length of the preference representation that the bidder needs to provide.

In addition to pioneering combinatorial auctions on the Internet, our auction server is, to our knowledge, the first Internet auction house that supports bidding via graphically drawn price–quantity graphs and by mobile agents. Price–quantity graphs are supported so that bidders can express continuous preferences. For example, when a bidder buys a larger quantity, she might only accept a lower unit price. Mobile agents are supported so that a user can have her agent actively participating in the auction

![](/api/attachments/FEARYTFT/fulltext/images/2b12849cba868d9bd56b93cf72ee85d3fe70b46e93bf10f2f785549c931415f7.jpg)  
Fig. 3. A combinatorial XOR-bid in our auction server. In this example, a refinery operator needs three consecutive hours of electricity for her plant. She prefers to start at 8 AM first row in the input form because that is a more suitable time and running that plant at that timeŽ . requires less electricity. However, starting at 6 AM second row or 7 AM third row is also feasible. The fourth row of the input formŽ . Ž . represents yet another alternative where the refinery operators does not operate the refinery at all, but speculates by buying and selling electricity at different times. Note that the same row combinatorial bid can include both buying and selling.Ž .

while she is disconnected. For example, the user can launch her agent over the phone from an airplane using a laptop, and then disconnect. Mobile agents that execute on the agent dock, which is on or nearŽ . the host machine of the auction server, also reduce the network latency — an issue of key importance in time-critical bidding. The Michigan Internet AuctionBot 26 provides a TCP<sup>w</sup> <sup>x</sup> <sup>r</sup>IP-level message protocol via which agents could participate in their auction. Their auction server differs from ours in that they do not provide support for mobile agents. Our auction server uses the commercial Concordia agent dock from Mitsubishi to provide mobile agents a safe execution platform from where they can observe what is transpiring in the auctions, bid, set up auctions, move to other hosts, etc. We also provide an easy-to-use HTML interface where the user can specify what she wants her agent to do, and our system automatically generates the Java code for the corresponding mobile agent, and launches it.

Yet another advantage of agents in this context comes from precompiled expertise. In certain auction settings, the optimal bidding strategies can be gametheoretically determined. eMediator provides such agents for the users 22 . Given that the user knows<sup>w</sup> <sup>x</sup> that the agent will bid optimally on her behalf, the user is motivated to reveal her preferences truthfully to the agent, and need not engage in counter-speculation and strategic bidding. Furthermore, agents that optimally bid on the user’s behalf put novices and expert bidders on an equal playing field for e-commerce.

## 10. Conclusions

Combinatorial auctions, i.e., auctions where bidders can bid on combinations of items, tend to lead to more efficient allocations than traditional auctions in multi-item auctions where the agents’ valuations of the items are not additive. This is because the users can express complementarities in their bids, and the winner determination algorithm will take these into account. Unfortunately, determining the winners so as to maximize revenue is <sub>N P</sub>-complete.

The space of allocations was first explicated, and asymptotic bounds on the number of allocations were shown. The number of allocations is so large that exhaustive enumeration will only work with a very small number of items. Dynamic programming avoids some of the redundancy of exhaustive enu meration, but it does not scale beyond auctions with a small number of items because it generates the entire search space independent of what bids have actually been placed.

The approach of compromising optimality to get polynomial time winner determination is futile if one is interested in worst-case approximation guarantees: a strong inapproximability result for the maximum clique problem applies to the winner determination problem. If the combinations are restricted, somewhat better guarantees can be established by known approximation algorithms for the weighted independent set problem and the weighted set packing problem, but the guarantees remain so weak that they are irrelevant in the domain of auctions in practice. The main hope for practical approximations for special cases lies in new forms of special structure espe- Ž cially on bid prices , and possibly in better algo- . rithms such as probabilistic ones.

By imposing severe restrictions on the allowable combinations, optimal winner determination can be guaranteed in polynomial time. However, these restrictions introduce some of the same economic inefficiencies that are present in non-combinatorial auctions.

To tackle the limitations of the existing approaches to winner determination, we developed a search algorithm for optimal anytime winner determination. It significantly enlarges the envelope of input sizes for which combinatorial auctions with optimal winner determination are computationally feasible. The highly optimized algorithm achieves this mainly by capitalizing on the fact that the space of bids is necessarily sparsely populated in practice. Unlike dynamic programming, it generates only the populated parts of the search space. It follows that the disadvantage of our algorithm is that the run time depends on the number of bids received, while in dynamic programming it does not. We addressed this problem by making our algorithm into an anytime algorithm: it can be terminated at any time before completion with a feasible monotonically improving solution in hand.

Finally, we discussed eMediator, our electronic commerce server that implements several techniques for automatically facilitating commerce, including an auction house with generalized combinatorial auctions. In addition to allowing combinations to be joined nonexclusively, it allows the user to join combinations exclusively in a bid. This input representation gives the user the power to express general preferences including both positive and negative complementarities. To shorten the input representation, we allow the user to also nonexclusively string together bids where the combinations are exclusive. To our knowledge, our implementation is the first Internet auction to support combinatorial auctions, bidding via graphically drawn price–quantity graphs, and mobile agents.

## Acknowledgements

Qianbo Huai programmed the auction server except for the winner determination algorithm described in this paper. Christina Fong proofread several drafts of this article. I received good comments on this work from the audience at the First International Conference on Information and Computation Economies ICE-98 . I present my kind thanks. Of Ž . course, any possible errors are solely mine.

## References

<sup>w</sup> <sup>x</sup> 1 M.R. Andersson, T.W. Sandholm, Leveled commitment contracting among myopic individually rational agents, in: Proceedings of the Third International Conference on Multi-Agent Systems ICMAS , Paris, France, July 1998, pp. 26– Ž . 33.

<sup>w</sup> <sup>x</sup> 2 M.R. Andersson, T.W. Sandholm, Leveled commitment contracts with myopic and strategic agents, in: Proceedings of the National Conference on Artificial Intelligence AAAI ,Ž . Madison, WI, July 1998, pp. 38–45.

<sup>w</sup> <sup>x</sup> 3 B. Chandra, M.M. Halldorsson, Greedy local search and ´ weighted set packing approximation, in: 10th Annual SIAM-ACM Sympossium on Discrete Algorithms SODA , JanuaryŽ . 1999.

<sup>w</sup> <sup>x</sup> 4 E.H. Clarke, Multipart pricing of public goods, Public Choice 11 1971 17–33.Ž .

<sup>w</sup> <sup>x</sup> 5 T. Groves, Incentives in teams, Econometrica 41 1973Ž . 617–631.

<sup>w</sup> <sup>x</sup> 6 M.M. Halldorsson, Approximations of independent sets in´ graphs, in: K. Jansen, J. Rolim Eds. , The First InternationalŽ . Workshop on Approximation Algorithms for Combinatorial Optimization Problems APPROX , Aalborg, Denmark, July Ž . 1998, pp. 1–14, Springer LNCS 1444.

<sup>w</sup> <sup>x</sup> 7 M.M. Halldorsson, H.C. Lau, Low-degree graph partitioning´ via local search with applications to constraint satisfaction, max cut, and 3-coloring, Journal of Graph Algo. Application 1 3 1997 1–13.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 J. Hastad, Clique is hard to approximate within ˚ $n ^ { 1 - \epsilon }$ , Acta Mathematica 1999 627–636, To appear. Draft: Royal Insti- Ž . tute of Technology, Sweden, 8<sup>r</sup>11<sup>r</sup>98. Early version: Proc. 37th IEEE Symposium on Foundations of Computer Science, 1996.

<sup>w</sup> <sup>x</sup> 9 D.S. Hochbaum, Efficient bounds for the stable set, vertex cover and set packing problems, Discrete Applied Mathematics 6 1983 243–254.Ž .

<sup>w</sup> <sup>x</sup> 10 R.M. Karp, Reducibility among combinatorial problems, in: R.E. Miller, J.W. Thatcher Eds. , Complexity of Computer Ž . Computations, Plenum, New York, 1972, pp. 85–103.

<sup>w</sup> <sup>x</sup> 11 R.E. Korf, Depth-first iterative-deepening: an optimal admissible tree search, Artificial Intelligence 27 1 1985 97–109.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 R.P. McAfee, J. McMillan, Analyzing the airwaves auction, Journal of Economic Perspectives 10 1 1996 159–175.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 J. McMillan, Selling spectrum rights, Journal of Economic Perspectives 8 3 1994 145–162.Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 S.J. Rassenti, V.L. Smith, R.L. Bulfin, A combinatorial auction mechanism for airport time slot allocation, Bell Journal of Economics 13 1982 402–417.Ž .

<sup>w</sup> <sup>x</sup> 15 J.A. Rodriguez-Aguilar, P. Noriega, C. Sierra, J. Padget, FM96.5: a Java-based electronic auction house, in: Proceedings of the Second International Conference on the Practica Application of Intelligent Agents and Multi-Agent Technology PAAM’97 , 1997.Ž .

<sup>w</sup> <sup>x</sup>16 M.H. Rothkopf, A. Pekec, R.M. Harstad, Computationallyˇ manageable combinatorial auctions, Management Science 44 Ž . Ž . 8 1998 1131–1147.

<sup>w</sup> <sup>x</sup>17 T.W. Sandholm, A strategy for decreasing the total transportation costs among area-distributed transportation centers, in: Nordic Operations Analysis in Cooperation NOAS : ORŽ . in Business, Turku School of Economics, Finland, 1991.

<sup>w</sup> <sup>x</sup> 18 T.W. Sandholm, An implementation of the contract net protocol based on marginal cost calculations, in: Proceedings

of the National Conference on Artificial Intelligence AAAI , Ž . Washington, D.C., July 1993, pp. 256–262.

<sup>w</sup> <sup>x</sup> 19 T.W. Sandholm. Negotiation among self-interested computationally limited agents. PhD thesis, University of Massachusetts, Amherst, 1996. Available at http:<sup>rr</sup>www.cs. wustl.edu<sup>r ;</sup>sandholm<sup>r</sup>dissertation.ps.

<sup>w</sup> <sup>x</sup> 20 T.W. Sandholm, Contract types for satisficing task allocation: I. Theoretical results, in: AAAI Spring Symposium Series: Satisficing Models, Stanford University, CA, 1998, pp. 68–75.

<sup>w</sup> <sup>x</sup> 21 T.W. Sandholm, An algorithm for optimal winner determination in combinatorial auctions, in: Proceedings of the Sixteenth International Joint Conference on Artificial Intelligence IJCAI , Stockholm, Sweden, 1999, pp. 542–547,Ž . Extended version: Washington University, Department of Computer Science technical report WUCS-99-01, January.

<sup>w</sup> <sup>x</sup> 22 T.W. Sandholm, eMediator: a next generation electronic commerce server, in: AAAI-99 Workshop on AI in Electronic Commerce, Orlando, FL, July 1999, pp. 46–55, Extended version: Washington University, Department of Computer Science technical report WUCS-99-02, January.

<sup>w</sup> <sup>x</sup> 23 T.W. Sandholm, K.S. Larson, M.R. Andersson, O. Shehory, F. Tohme, Coalition structure generation with worst case´ guarantees, Artificial Intelligence 111 1–2 1999 209–238,Ž . Ž . Early version appeared at the National Conference on Artificial Intelligence AAAI , 1998, p. 4653.Ž .

<sup>w</sup> <sup>x</sup> 24 T.W. Sandholm, V.R. Lesser, Issues in automated negotiation and electronic commerce: extending the contract net framework, in: Proceedings of the First International Conference on Multi-Agent Systems ICMAS , San Francisco, CA,Ž . June,1995, pp. 328–335, Reprinted in Huhns and Singh Ž . Eds. , Readings in Agents, 1997, pp. 66–73.

<sup>w</sup> <sup>x</sup> 25 T.W. Sandholm, V.R. Lesser, Advantages of a leveled commitment contracting protocol, in: Proceedings of the National Conference on Artificial Intelligence AAAI , Portland, OR,Ž . August, 1996, pp. 126–133.

<sup>w</sup> <sup>x</sup> 26 P.R. Wurman, M.P. Wellman, W.E. Walsh, The Michigan Internet AuctionBot: a configurable auction server for human and software agents, in: Proceedings of the Second International Conference on Autonomous Agents AGENTS , Min-Ž . neapolis<sup>r</sup>St. Paul, MN, May 1998, pp. 301–308

Tuomas Sandholm is assistant professor of computer science at Washington University in St. Louis. He received his PhD and MS degrees in computer science from the University of Massachusetts at Amherst in 1996 and 1994. He earned an MS BS includedŽ . with distinction in Industrial Engineering and Management Science from the Helsinki University of Technology, Finland in 1991. He has published over 100 technical papers on ecommerce, AI, game theory, multiagent systems, rational resource-bounded reasoning, auctions, automated negotiation and contracting, coalition formation, machine learning, constraint satisfaction, and combinatorial optimization. He has 10 years of experience building multiagent systems for e-commerce, co-developed two fielded AI systems, and founded two e-commerce startup companies.
