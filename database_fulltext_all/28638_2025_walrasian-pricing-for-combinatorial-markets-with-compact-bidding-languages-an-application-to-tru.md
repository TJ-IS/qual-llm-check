---
otero_id: 28638
otero_key: "KJDKDQ33"
title: "Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation"
authors: "Mohsen Emadikhiav; Robert Day"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0676"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Walrasian Pricing for Combinatorial Markets with Compact-Bidding Languages: An Application to Truckload Transportation

Mohsen Emadikhiav,<sup>a,</sup>\* Robert Day<sup>b</sup>

<sup>a</sup> Department of Information Technology and Operations Management, College of Business, Florida Atlantic University, Boca Raton, Florida 33431; <sup>b</sup> Department of Operations and Information Management, School of Business, University of Connecticut, Storrs, Connecticut 06269

\*Corresponding author

Contact: memadikhiav@fau.edu, https://orcid.org/0000-0003-2114-3353 (ME); robert.day@uconn.edu, https://orcid.org/0000-0002-9705-4130 (RD)

Received: November 7, 2023 Revised: July 4, 2024; December 4, 2024 Accepted: December 23, 2024 Published Online in Articles in Advance: January 30, 2025

https://doi.org/10.1287/isre.2023.0676

Copyright: © 2025 INFORMS

Abstract. Combinatorial auctions offer several economic advantages but also face multiple technical challenges, including bid generation, the need to solve a combinatorial allocation problem, and determining reasonable prices. These challenges are even more pronounced in a combinatorial exchange, where bidders can simultaneously buy and sell combinations of goods. Motivated by truckload transportation markets, we explore new mechanisms for finding linear and anonymous Walrasian equilibrium prices in combinatorial auctions and exchanges where bidders can use a compact-bidding language to express their potentially complex preferences. With the goal of improving economic efficiency and reducing the environmental impact of the trucking industry, we identify significant potential gains by developing a method for integrated allocation and price determination based on an industry-specific bidding language. We also demonstrate our proposed mechanism’s adaptability and flexibility by considering a number of practical constraints.

History: Martin Bichler, Senior Editor; Pallab Sanyal, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0676.

Keywords: combinatorial auctions • exchange • Walrasian equilibrium • compact-bidding languages • transportation

## 1. Introduction

A combinatorial auction (CA) is a form of multiunit auction that allows bidders to bid on packages of items (Cramton et al. 2006). CAs offer protection against the “exposure problem” present in multiunit simultaneous auctions, in which a bidder is exposed to winning too many substitute items or too few complementary items given her preferences (Bykowsky et al. 2000, Milgrom 2004). CAs have been adopted in practice in procurement auctions (Bichler et al. 2011, Sandholm 2013), spectrum auctions (Bichler and Goeree 2017), the allocation of fishing rights (Bichler et al. 2018), and truckload transportation contracts (Sheffi 2004) among others, and they have been proposed for other practical applications, such as airport-slot allocation (Ball et al. 2018) and advertisement-slot allocation (Goetzendorff et al. 2015). A combinatorial exchange (CE) is a generalization of a CA with multiple buyers, multiple sellers, and even traders, whose bids include combinations of items that they want to sell along with items that they want to buy (Parkes et al. 2001).

Despite their promise of better outcomes through expressivity, the implementation of CAs and CEs in practice faces multiple design challenges. First, bidders potentially need to evaluate an exponential number of package bids. Hence, when the number of objects being auctioned grows large, bidders might only bid on a small subset of all possible packages, which could result in significant efficiency losses, sometimes known as the “missing bids” problem (Bichler et al. 2013). Compactbidding languages have been proposed for specific markets as a remedy, reducing the burden of bidding by providing a means to express preferences on (poten tially) all packages of interest while using only a poly nomial number of parameters. Second, the auctionee needs to compute an allocation and payments that satisfy one or more desirable economic properties based on these bids, such as individual rationality (IR), Walrasian equilibrium (WE), incentive compatibility, budget balance (BB), and core stability among others. Studies have proposed various pricing mechanisms for CAs/ CEs, including the Vickrey–Clarke–Groves (VCG) mech anism (Vickrey 1961, Clarke 1971, Groves 1973), linear dual prices (Bikhchandani and Mamer 1997), and coreselecting payment determination (Day and Raghavan 2007), which we will describe in further detail in Section 2.

Here, we introduce a general pricing framework for CAs and CEs to find linear and anonymous prices.

A linear pricing structure, where the payment for a package is equal to the sum of the prices of the items in that package, makes the identified prices simple to understand and explain to participants. Moreover, linear prices are computationally tractable in combinatorial markets as they obviate the need to compute prices for an exponential number of packages individually. The anonymity makes the identified prices fair as all bidders, regardless of their identity, pay the same price for the items they win (Lubin et al. 2008, Bichler et al. 2018). To extend the usefulness of linear prices beyond their well-known nonexistence for CAs in general (Bikhchandani and Mamer 1997), we show how to augment a CA with cuts to the winner-determination problem (WDP), and the dual prices of these new constraints will behave exactly as linear and anonymous prices when the cuts are treated as items themselves. (Note that each item listed in a market enters the optimization formulation as a single constraint so that an added constraint is functionally identical to an original item as long as all bidders are offered the same price for the item and the winner of the item pays the item price.) Our pricing mechanism also satisfies (i) individual rationality (i.e., all players are better off through their participation), (ii) ɛ-Walrasian equilibrium (i.e., the market clears while ensuring that participants (approximately) prefer their allocated packages); and (iii) strong budget balance (i.e., total payments of participants equal zero so that no money needs to be injected from an external entity to balance the payments). (It is known that VCG violates BB in CEs (Lubin et al. 2008). We benchmark our proposed pricing mechanism against VCG and highlight that the extent of these violations makes VCG impractical.)

We also highlight our approach’s adaptability and flexibility by considering a number of practical constraints. Although it has been shown that a WE with linear prices may not exist (Bikhchandani and Mamer 1997), through our experiments, we show that in many instances, we are able to find linear WE prices satisfying IR and BB. For those cases where WE prices cannot be found, we show that the deviation from equilibrium is relatively negligible (i.e., we have ɛ-Walrasian equilibrium prices). In such cases, we propose a cuttingplane method to further reduce deviation from WE, also known as residual envy, often reducing it to zero (i.e., to an exact WE when cuts are treated as items). The cuts that we employ here are clique cuts; stated in words, this is a group of bundle bids that mutually exclude each other (forming a clique in a bid independence graph). We will sell and price a license to be the sole winning bid from this particular set and thus, (at least partially) resolve the deviation from WE. We highlight the effectiveness and practical interpretability of the cuts used for a truckload transportation market, which can be generalized to other domains. Moreover, to our knowledge, no previous study has explored the use of our general computational framework to balance the benefits of a domain-specific compact-bidding language with the explanatory power of an enumerative “exclusive or” (XOR) primal-dual formulation, utilizing dynamic cut generation to find ɛ-WE and budgetbalanced linear prices for CAs/CEs. Our paper aims to fill this gap by presenting an algorithmic framework for finding IR, ɛ-WE, and BB prices that can be adapted to a broad class of CAs or CEs based on compact-bidding languages.

Through our experiments in a truckload transportation market, we benchmark our proposed approach against some of the existing mechanisms from the literature. To compare the efficiency of different mechanisms, we calculate total savings, defined as the reduction in total transportation costs for the participants when they join the market compared with their total transportation costs when they operate individually. Specifically, in a pure procurement auction setting (where carriers do not exchange lanes), we highlight that a mechanism that allocates efficiently based on bids (such as ours or the VCG mechanism) generates significantly higher savings (on average, 37% higher savings) compared with straightforward bidding in a benchmark simultaneous multiround auction (SMRA). (In the latter, inefficiencies occur because of the nonexistence of a linear-price equi librium (i.e., because market efficiency does not benefit from the additional price information captured by our newly generated cuts or from nonlinear lump-sum payments in the case of VCG).) Moreover, we show that incorporating lane exchange can significantly boost the savings (on average, 151% more savings), bringing substantial additional benefits for the carriers in the market and justifying the additional complexity of allocation and price computation for the CE setting.

In summary, our research has important theoretical and practical contributions. We outline a novel general framework for either a CA or a CE with many items, including bidding, winner, and price determination, using large truckload-transportation markets as a leading example.

1. We incorporate domain-specific compact-bidding languages into the calculation of ɛ-Walrasian equilibrium prices. To do so, we map the solution of a polynomial winner-determination problem, which utilizes compact bids, onto a standard combinatorial winnerdetermination problem, which has interpretable dual prices. We then use an iterative cut-generation procedure to find linear and anonymous prices that satisfy ɛ-Walrasian equilibrium, IR, and BB.

2. We extend dual pricing in CEs pioneered by Bikhchandani and Mamer (1997) by incorporating a cutting-plane procedure based on cliques to find new linear and interpretable price components in a WE. We show that adding such cuts significantly reduces residual envy.

3. We evaluate our approach with a series of simulations of a transportation lane exchange, showing financial and environmental benefits relative to benchmarks from the literature.

To our knowledge, we are the first to present a mechanism with the above-mentioned properties, providing a practical direction for easier-to-implement efficient carrier collaborations and an overall framework for general CAs or CEs with compact-bidding languages to find meaningful ɛ-WE prices.

## 2. Related Work

The information systems literature has made significant contributions to the theory and applications of CAs and CEs in recent decades (e.g., Adomavicius and Gupta 2005; Bichler et al. 2009, 2017, 2018; Ray et al. 2021; Adomavicius et al. 2022; Bu¨ nz et al. 2022; Kittsteiner et al. 2022). Advances in information technology and the design of effective computational methods have made the implementation of CAs and CEs possible. However, there are still significant research opportunities in the design of bidding languages and pricing schemes (Bichler et al. 2018).

Compact-bidding languages have been proposed as a remedy to the missing bids problem, where instead of evaluating an exponential number of packages, a bidder submits her bids with a polynomial number of parameters. Goetzendorff et al. (2015) study combinatorial auction markets with compact-bidding languages and present methods to compute Vickrey–Clarke–Groves or bidder-optimal, core-selecting payment rules. They motivate their study using applications in TV advertising and volume-discount procurement auctions. Bichler et al. (2018) propose a compact-bidding language for allocation of fishing rights to compute and analyze linear prices in a combinatorial exchange. Chen et al. (2009) present an compact-bidding language for a truckload procurement auction. The focus of Chen et al. (2009) is primarily on solving the combinatorial winnerdetermination problem, and the economics of the market prices are essentially not considered.

When bids are submitted, the auctioneer solves the “winner-determination problem” to determine an optimal allocation of items to bidders, typically an NP-hard problem (Garey and Johnson 2002, Bichler 2018). Many researchers have presented exact and heuristic methods to solve various forms of WDPs (Sandholm 2002, Gu¨ nlu¨ k et al. 2005, Boughaci et al. 2010, Wu and Hao 2015). From a theoretical standpoint, the nonoptimality of WDP can impact the calculation of prices. For example, Goetzendorff et al. (2015) propose core-selecting payment calculations when the optimality of the allocation problem cannot be guaranteed. We instead follow much of the CA literature by focusing on an exactly optimal allocation followed by the calculation of meaningful payments to support that allocation.

Under the VCG mechanism (Vickrey 1961, Clarke 1971, Groves 1973), the winner of each package gets a discount on her winning bid equivalent to the difference between the value of the WDP with and without her participation in the auction, resulting in the unique efficient and IR mechanism that is incentive compatible (i.e., each bidder’s weakly dominant strategy is to bid truthfully). However, VCG payments may not be in the core (Ausubel and Milgrom 2006, Day and Raghavan 2007), meaning that profitable renegotiations may be available. Further, in exchange environments, VCG payments are often not budget balanced, meaning that an external entity (e.g., the government) would need to inject money into the market in order to balance the prescribed payments of all of the players (Day 2013).

To address these shortcomings of VCG, researchers have explored alternative payment methods in both CAs and CEs that may or may not prioritize incentive compatibility. For instance, Cavallo (2006) presents a mechanism that is incentive compatible and individually rational but approximates budget balance. Other studies investigate payment mechanisms that prioritize other economic properties while approximating VCG. For instance, Parkes (2001) presents a mechanism that maintains budget balance while minimizing the maximum deviation from VCG payments; core-selecting payment mechanisms have been proposed in CAs (Day and Raghavan 2007, Day and Cramton 2012) and CEs (Hoffman and Menon 2010, Day 2013).

Our proposed pricing mechanism follows in the spirit of others for CEs (Bikhchandani and Mamer 1997, Parkes 2001, Lubin et al. 2008, Hoffman and Menon 2010, Day 2013). In particular, we introduce a mechanism that aims to simultaneously satisfy IR, BB, and ɛ-WE. Although linear prices—for which the payment for a package is equal to the sum of the prices of the items in that package—are desirable in practice (Lubin et al. 2008, Bichler et al. 2018), in markets with indivisibilities, it has been shown that a WE with linea prices may not exist (Bikhchandani and Mamer 1997). Our work extends the literature on finding ɛ-WE prices by integrating a cutting-plane approach to reduce residual envy in the computation of fair and desirable linear prices. These cuts can be interpreted as virtual items that are priced to determine payments. Among the only other work related to automated price term generation, Lahaie and Lubin (2019) propose an adap tive pricing scheme that adds price terms for collections of items interpreted in a polynomial framework. Although they work in an environment with a single copy of each unique item being offered (unlike the current multi-item setting), their monomial price terms can also be interpreted in our framework as a subset of the clique cuts that we search over for additional price richness. Additionally, their focus is on payment determination in iterative (multiround) combinatorial auctions unlike our framework, which finds WE prices in single-shot (sealed-bid) CAs or CEs.

Sandholm (2013) describes the deployment of cuttingedge CA technology in real-world procurement auctions run by CombineNet, with similar applications to those described here. As in that work, we work within the general notion of “expressive commerce,” in which integer programming techniques allow for ad hoc user (bidder) constraints in CAs, offering higher efficiency and relief from the exposure problem through succinct communication of practical conditions and preferences. They cite real-world avoidance of the VCG mechanism in practice, and our simulation results provide further support for this perspective. For practical simplicity (it would seem), they default to pay-as-bid pricing. Here, we explore extensions of the CombineNet perspective but look at the middle ground (between VCG and pay as bid) of WE prices. WE prices have a long history as a solution paradigm in economics that is suitable for markets that typically have many bidders, such as in the markets that we explore, where the aggregate of U.S. markets, for example, is composed of hundreds of thousands of independent carriers (Harris and Nguyen 2025). Advanced variations of WE pricing mechanisms continue to be explored for markets with nonconvexities, where simple WEs do not exist: for example, in Milgrom and Watt (2022). As in that work, we add new pricing dimensions as cuts (here, explicitly and there, implicitly) but differ in the type of pricing terms used; Milgrom and Watt (2022) use monetary markups to rescale prices, whereas we use clique cuts to price naturally occurring exclusions among bids, adding an additional dimension of pricing feedback. Also, here we hope to extend the trail blazed by CombineNet, showing that if the markets for trucking were to go a step further into shipping-contract exchange, greater market-wide efficiency may be obtained. Our simulations show the potential to unlock substantial benefits by providing a mechanism with enhanced opportunities for resource pooling and competitive equilibrium price feedback.

Milgrom and Watt (2022) also provide theoretical support for bidder-optimal approximate-WE prices, noting that with price-taking agents, such mechanisms will have “good incentives and small deadweight losses.” Informally, computing prices close to WE in a direct-report mechanism will result in incentives and efficiency that are similarly close to the properties of WE in general. This idea underpins other recent uses of the WE paradigm. For example, Budish (2011) uses approximate-WE prices in an economy with fictional money to allocate scarce, highly demanded seats in business schools, introducing a notion of “incentive compatibility in large markets” in which WE prices perform well as markets grow and bidders become price takers. These concepts were more recently explored and refined by Nguyen and Vohra (2022), who give both approximation techniques and preference restrictions that result in provable bounds on the relaxation error. This literature stream provides several methods for approximating WE along various dimensions when they are not guaranteed to exist, such as in the current work. The incentive-compatible VCG mechanism is often not usable in practice (Ausubel and Milgrom 2006), and therefore, approximate WE mechanisms emerge as a heuristic method for practical market design. We, therefore, defer from a direct discussion of bidder incentives in the current work, supported by this literature.

Our framework is unique in using a clique-cut generation procedure that is highly effective and interpretable for the domain of our problem yet can be generalized to other contexts. We show that in the majority of our experiments, we can find linear and anonymous WE prices satisfying IR and BB. In the minority cases where WE prices cannot be found, we show that the deviation from equilibrium is relatively negligible.

## 2.1. Truckload Transportation Markets

The trucking industry generated over \$875.7 billion in revenue in the United States during 2021, which accounted for approximately 81% of the nation’s freight bill (from the American Trucking Association<sup>1</sup>). Over 90% of trucking shipment operations are performed on a full-truckload basis, where buyers (shippers) hire suppliers (carriers) to move full trailers of goods through their supply chains (Scott 2019). Shippers and carriers in the U.S. truckload markets engage in two forms of transactions: long-term contracts and spot-market agreements. Studies estimate that roughly 80% of the for-hire truckload market is covered by long-term contract prices<sup>2</sup> (Harris and Nguyen 2022), which are usually established via annual procurement auctions (Caplice and Sheffi 2006). The objects traded through these procurement auctions are “transportation lanes,” typically specified by an origin, a destination, and the number of truckloads that need to be shipped between the origin and the destination. Although long-term contracts help carriers and shippers to create a reliable relationship and establish long-term prices, spot-market transactions involve ad hoc searches and price negotiations to address uncertainties in real time (Emadikhiav et al. 2024). Our focus is on addressing the long-term allocation and price determination through an auction/exchange-based truckload market, where shippers and carriers look for highly predictable and repeatable lanes.

In a transportation market, package bidding is particularly advantageous as carriers are able to bid on and potentially win a collection of shippers’ lanes that are well suited to their existing network (Chen et al. 2009). However, as typically hundreds of lanes need to be traded through a truckload procurement auction, bid generation and price determination are challenging tasks for the bidders and the auctioneer. Hence, bidders in practice tend to bid only on individual lanes, and simpler pricing schemes, such as pay-as-bid prices, are used to determine payments (Caplice and Sheffi 2006). Here, we propose a combined compact bidding language and ɛ-WE price format to unlock the efficiency gains left on the table, overcoming these previously observed difficulties with new simplicity in both the bidding format and the interpretation of meaningful prices.

We use a compact-bidding language similar to the one proposed by Chen et al. (2009) for our CE setting. The resulting WDP formulation is of manageable size, connecting it to the literature on carrier collaboration problems, which have been extensively studied in the transportation science literature (for instance, Ergun et al. 2007a, b; Liu et al. 2010; Ferna´ndez et al. 2016; and Kuyzu 2017). Specifically, we consider a formulation similar to the multicarrier lane-covering problem (MCLCP) presented in Chen et al. (2009) and O<sup>¨</sup> zener et al. (2011), which aims to minimize transportation costs by finding a set of tours to cover a set of given lanes from multiple carriers. Although MCLCP was shown to be NP hard for certain cost structures of the carriers (O<sup>¨</sup> zener et al. 2011), we find that the optimization model can still be solved quickly using standard commercial solvers for most randomly generated instances based on real-world parameters. Among the trucking transportation literature (for instance, Huang and Xu 2013, Chen 2016, Cheng et al. 2016, and Xu et al. 2017), only a few studies consider CAs or CEs, and we provide the first study incorporating a compact-bidding language for a transportation CE coupled with BB and ɛ-WE prices.

An important assumption in the study of expressive commerce via CAs or CEs is that bidders (carriers) would be willing to share their private information (preferences) with the auctioneer, despite the risk of information leakage to their competitors (Chen et al. 2009). Although the trade-off between the risks of sharing private information and the benefits of collaboration remains an important question, as highlighted in our results (Section 4.3.1), we show significant gains from expressive collaboration given a trustworthy auctioneer. Private third-party logistics providers, such as CombineNet and Manhattan Associates, stake their reputations on their ability to mitigate the risk of information leakage, and in recent years, we have indeed witnessed shippers and carriers sharing critical private information with the U.S. Government in order to untangle congested supply chains.<sup>3</sup> Further, the need for a trusted third-party auctioneer may eventually be eliminated in some contexts given the advancements in cryptography and secured systems through multiparty computation, in which a set of untrusting participants in a sealed-bid auction can compute any function of their private inputs while revealing nothing but the result of the function (Ben-David et al. 2008, Evans et al. 2018, Wang et al. 2021).

## 3. Problem Description

Consider a transportation market with multiple carriers and one shipper (or a collection of shippers acting as a single conglomerate). The carriers are primarily the suppliers in the market, having an available supply of trucks that can ship full truckloads for the shipper. Each carrier is also exogenously endowed with existing contracts $( \mathrm { i . e . , }$ for each, we have a set of previously contracted lanes that she has committed to cover). The shipper, on the other hand, has truckloads that need to be moved but does not have any trucks to transport these loads. (The shipper is like a carrier in coming to the market with needs or contracts to transport across lanes but unlike them in having no supply of trucks.) A lane is specified by an origin, a destination, and a required number of shipments between the origin and the destination for its owner. We denote the set of car riers by C. We index carriers by c and denote the shipper with zero to distinguish her from carriers. The set of all lanes is denoted by ${ \mathcal { L } } ,$ with $\mathcal { L } _ { c }$ specifying the set of lanes for carrier $c \in { \mathcal { C } }$ (i.e., the existing contracts to cover lanes brought to the market by c) and $\mathcal { L } _ { 0 }$ representing the set of shipper’s lanes (needs). We use O(l) to denote the owner of lane $l \in \mathcal { L }$ . The beginning and end of lane l are denoted by $B ( l ) \in \mathcal { N }$ and $\mathcal { E } ( l ) \in \mathcal { N } ,$ respectively. Parameter $d _ { l }$ specifies the number of shipments to be transferred across lane l for O(l).

In this transportation market, carriers submit bids on lanes. We consider two general market settings: (i) procurement auction for lanes (PAL) and (ii) procurement exchange for lanes (PEL). In PAL, each carrier bids only on the shipper’s lanes. Each carrier must cover her own previously contracted lanes $( \mathcal { L } _ { c } )$ and potentially cover some additional shipper’s lanes (from $\mathcal { L } _ { 0 } )$ if she bids on them and wins. In PEL, on the other hand, a carrier may bid on the shipper’s lanes as well as some other carrier’s lanes that have been made available for exchange. In other words, in PEL, whereas the shipper remains a net procurer, lanes brought by carriers may be traded among the carriers so that after the close of the market, a carrier may fulfill some of her own previously contracted lanes, some of the shipper lanes, and some lanes of other carriers. This, of course, implies that a carrier under PEL may end up with another carrier fulfilling some lanes that were originally her lanes, which cannot happen under the more simple setting of PAL. In both PAL and PEL, all lanes are feasibly covered at the close of the market, with some possibly being relegated to the (more expensive) spot market. Note that PAL is closer to common practice, in which trucking service contracts are typically procured by a single shipper (or collection of shippers) via auction without endogenous trade among the bidding carriers. We explore PEL here to show new opportunities for potentially better market performance when carriers can also trade existing contracts within the market. We first explore the PAL case before turning to PEL in Section 3.6.

## 3.1. PAL Winner Determination

In a reverse auction or procurement auction, an auctioneer solves the WDP to find an allocation of items consistent with a given set of bids so as to minimize total costs. The set of package bids is represented by ${ \mathcal { S } } ,$ with the bids submitted by carrier c denoted by $\dot { \mathcal { S } _ { c } } .$ . A bid $s \in \mathcal S$ is a 3-tuple $\langle \mathsf { C } _ { s } , \Psi _ { s } , b _ { s } \rangle$ , where ${ \mathrm { C } } _ { s }$ is the carrier that submitted s and $\Psi _ { s }$ is a vector of $\vert \mathcal { L } _ { 0 } \vert$ | nonnegative integers with each component $\psi _ { l } ^ { s }$ indicating the number of truckloads on lane l that would be covered by package bid s. The monetary bid value $b _ { s }$ of each package is the lump-sum cost calculated by c considering her operational constraints and network structure (Caplice 2007, Chen et al. 2009). This XOR approach (listing exclusive bids on any package) fully describes any CA setting for our theoretical presentation, but as we show below, we only implement such package bids dynamically in any computation, never fully enumerating all such bids within computer memory.

As an example, consider a simple network shown in Figure 1 with a carrier and a shipper. The carrier has two lanes (her existing contracts), each with two shipments (shown by solid arrows in in Figure 1). In her current network, the carrier is frequently moving empty between C and A locations. The shipper also has two lanes, each with demand of two (shown by dashed arrows in Figure 1). We assume that the carrier pays \$1.5 to cover a shipment on her own lane, and considering the additional operational costs, it costs her \$2 to cover a shipment on a shipper lane. The cost of moving empty on any arc is also \$1 for the carrier. So, in her current network, the carrier is paying $2 \times \$ 1.5$ \$8 in total. We assume that the carrier is not interested in the shipper’s lane 2 (between D and E locations) as she does not operate in that region. The carrier can submit two package bids as follows: $b i d _ { 1 } = \langle c a r r i e r _ { 1 } , [ 2 , 0 ] , \$ 9 2 \rangle$ and $b i d _ { 2 } = \langle c a r r i e r _ { 1 } , [ 1 , 0 ] , \$ 1 \rangle$ 〉. Here, the first bid expresses that she is willing to cover two shipments of the shipper’s lane between C and $\scriptstyle \mathrm { A , }$ cover no shipments on the shipper’s lane between D and E, and receive \$2 from the shipper. The bid value of \$2 is the difference in costs between covering two shipments of the shipper’s lane between C and A (i.e., $2 \times  { \hat { \mathbb { g } } } 1 . 5 + 2 \times  { \mathbb { g } } 1 . 5 +  { \hat { 2 } } \times  { \mathbb { g } } 2 =  { \mathbb { g } } 1 0 )$ and the carrier’s current cost of \$8. Similarly, the second bid indicates that the carrier is willing to cover only one shipment between C and A and receive \$1 from the shipper.

Figure 1. A Simple Example (All Lanes Include Two Shipments)  
![](/api/attachments/KJDKDQ33/fulltext/images/459d103304da55e45dc0738073b021beb2af5cbf2d15b2b0d177fc8cd539df35.jpg)

![](/api/attachments/KJDKDQ33/fulltext/images/f5c284d60f136ac3cfffd52c0d19636238ddc658f27a504334dfcbabdba042d7.jpg)

We first present the WDP for PAL using the generic (fully expressive) XOR bidding language (i.e., as an exclusive disjunction of package bids with each carrier in principle listing every possible integer allocation and corresponding price). The number of packages (columns) grows exponentially with the number of the shipper’s lanes. Later, we introduce a compact-bidding language to soften this computational burden, but this XOR version provides a theoretical benchmark and basis for pricing. The exponentially sized winner-determination problem (henceforth denoted by Ex-WDPR) for this combinatorial reverse auction is

$$
\min \sum_ {s \in \mathcal {S}} b _ {s} \chi_ {s} + \sum_ {l \in \mathcal {L} _ {0}} \gamma_ {l} r _ {l},\tag{1a}
$$

s:t:

$$
(p _ {l}) \quad \sum_ {s \in \mathcal {S}} \psi_ {l} ^ {s} \chi_ {s} + r _ {l} = d _ {l}, \qquad \forall l \in \mathcal {L} _ {0},\tag{1b}
$$

$$
(\pi_ {c}) \sum_ {s \in \mathcal {S} _ {c}} \chi_ {s} = 1,
$$

$$
\forall c \in \mathcal {C},\tag{1c}
$$

$$
\chi_ {s} \in \{0, 1 \},
$$

$$
r _ {l} \in \mathbb {Z} _ {\geq 0},
$$

$$
\forall s \in \mathcal {S},\tag{1d}
$$

$$
\forall l \in \mathcal {L} _ {0}.\tag{1e}
$$

Binary decision variable $\chi _ { s }$ equals one if package $s \in \mathcal S$ of carrier ${ \mathrm { C } } _ { s }$ is a winning bid, whereas integer decision variable $r _ { l }$ determines the number of times that lane $l \in \mathcal { L } _ { 0 }$ is covered externally via the spot market. The objective is to minimize total lane-covering costs based on the submitted bids. Equations (1b) ensure that all shipper’s lanes are covered either by a carrier or through the spot market. Equations (1c) ensure that each bidder (carrier) wins exactly one of her submitted packages as per the explicitly enumerative XOR language. (Note that the null bid, where a carrier does not win any shipper’s lanes, is implicitly included in S for each carrier.) Dual variables $p _ { l }$ for Constraints (1b) and $\pi _ { c }$ for Constraints (1c) are shown here for reference and are described later.

## 3.2. Price Determination Using Dual Values

After solving the winner-determination problem, prices should be calculated to determine the payments (and therefore, surpluses) of the shipper and the carriers. We consider a quasilinear setting where the surplus of each carrier is calculated as the difference between the payments given to her and her bid. For the shipper, the payoff is the difference between her payments in the spot market and our auction-based market.

The dual values of Ex-WDPR (i.e., Equations (1a)–(1e)) can be interpreted as linear prices and bidders’ surpluses (Bikhchandani and Mamer 1997). Consider the dual of the linear relaxation of Ex-WDPR as follows:

$$
\max \sum_ {l \in \mathcal {L} _ {0}} d _ {l} p _ {l} - \sum_ {c \in \mathcal {C}} \pi_ {c},\tag{2a}
$$

$$
\text { s.t. } \quad \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s}   p _ {l} - \pi_ {C _ {s}} \leq b _ {s}, \qquad \forall s \in \mathcal {S},\tag{2b}
$$

$$
p _ {l} \leq \gamma_ {l},
$$

$$
\forall l \in \mathcal {L} _ {0},\tag{2b}
$$

$$
\pi_ {c} \in \mathbb {R},
$$

$$
\forall c \in \mathcal {C}.\tag{2c}
$$

Here, $p _ { l }$ is the price of lane $l \in \mathcal { L } _ { 0 } ,$ , and $\pi _ { c }$ represents the surplus of carrier $c \in { \mathcal { C } } .$ Bikhchandani and Mamer (1997) showed that when the relaxation of the primal problem (here, Ex-WDPR) produces integer solutions, $\mathrm { i . e . } ,$ , no integer programming (IP) relaxation gap, the prices from the dual problem support a Walrasian equilibrium. Bikhchandani and Mamer (1997) formulated the WDP primal for a forward auction/exchange. The following proposition shows that similar properties hold in our reverse auction setting.

Proposition 1. When there is no IP relaxation gap in the primal, the resulting dual prices satisfy individual rationality and Walrasian equilibrium.

All proofs are presented in Online Appendix B. It is also straightforward to see that when there is no IP gap, the dual linear prices are strongly budget balanced as after prices are identified for each lane, the shipper makes those exact payments to the carriers based on their allocations.

The standard dual model, Equations (2a)–(2c), indeed finds a WE, but in general, many WEs are possible, including both “pay-as-bid” outcomes and bidder (-Pareto)-optimal outcomes, the latter of which can provide better incentive properties. Following the proof of Proposition 1 in Online Appendix $\mathrm { B , }$ by removing the $\pi _ { c }$ variables and taking the information from the optimal allocation of the primal model, we propose the following winner-aware dual formulation (henceforth denoted by WAD) for determining bidder-optimal prices:

max $\sum _ { l \in \mathcal { L } _ { 0 } } d _ { l } \ p _ { l } ,$

$$
\text { s.t. } \quad \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*}} p _ {l} - b _ {s ^ {*}} \geq \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s} p _ {l} - b _ {s},\tag{3a}
$$

$$
\forall s ^ {*} \in \mathcal {S} ^ {*}, s \in \mathcal {S} \backslash \mathcal {S} ^ {*}, C _ {s ^ {*}} = C _ {s},\tag{3b}
$$

$$
p _ {l} \leq \gamma_ {l},
$$

$$
\forall l \in \mathcal {L} _ {0}.\tag{3c}
$$

Equations (3b) are Walrasian equilibrium constraints. The modified objective function (3a) adjusts the prices in the direction of increasing payments to the winning carriers and maximizes their surplus $( \mathrm { i . e . , }$ selecting bidder-optimal prices). Intuitively, the best prices for the carriers (limited only by competition captured in the constraints) deliver the best incentives for bidding over the available (linear) payment space.

3.2.1. Compact Bidding and a Polynomially Sized WDP. We next study the market under the assumption that carriers express their preferences using a polynomial number of parameters in $| { \mathcal { L } } |$ (as opposed to an expo nential in the number of lanes under an XOR language that lists a value for each lane combination), similar to the bidding language presented in Chen et al. (2009). In our baseline model, each carrier $c \in { \mathcal { C } }$ submits all information about her network to a trusted auctioneer, including her existing contracts, $\mathcal { L } _ { c } ,$ , and the cost of covering each origin-destination pair of nodes within the network of all carriers and the shipper. Specifically, each compact bid of carrier c is a 3-tuple $\langle \mathcal { L } _ { c } , [ \delta _ { l } ^ { c } ] , [ \theta _ { i j } ^ { c } ] \rangle$ where $[ \delta _ { l } ^ { \dot { c } } ]$ is the cost matrix specified to cover each lane $l \in \mathcal L$ and $[ \theta _ { i j } ^ { c } ]$ is the cost matrix specified for each arc in the whole network to travel empty from node i ∈ $\mathcal { N }$ and $j \in \mathcal N$ . We study this full disclosure case to emphasize the potential efficiency benefits of this natural benchmark. Later, in the experiments of Section $^ { 4 , }$ we relax the assumption of full disclosure and explore the impact of bidding carriers sharing only partial information about their private networks while maintaining a polynomial structure for direct (lane-by-lane) cost revelation.

In the baseline case, the compact-bidding WDP becomes a variant of the multicarrier lane-covering problem introduced by O<sup>¨</sup> zener et al. (2011), and we will have similar parameters. The cost of covering lane l by carrier c is denoted by $\delta _ { l } ^ { c }$ . The cost of traveling empty on arc $( i , j ) \in { \mathcal { A } }$ for carrier c is denoted by $\theta _ { i j } ^ { c } .$ Integer variable $x _ { l } ^ { c }$ specifies the number of times that carrier c covers lane l. Integer variable $y _ { i j } ^ { c }$ determines the number of times that carrier c travels empty on arc $( i , \ j )$ . For carrier $c$ and each lane $l \in \mathcal { L } _ { c }$ we have a required number of shipments (existing contracts) $d _ { l } ,$ which are constant terms in this formulation that could later be eligible for exchange when we extend to the PEL scenario.

The polynomially sized winner-determination problem (henceforth referred as Poly-WDPR) is

$$
\min \sum_ {c \in \mathcal {C}} \left[ \sum_ {l \in \mathcal {L} _ {c}} \delta_ {l} ^ {c} d _ {l} + \sum_ {l \in \mathcal {L} _ {0}} \delta_ {l} ^ {c} x _ {l} ^ {c} + \sum_ {(i, j) \in \mathcal {A}} \theta_ {i j} ^ {c} y _ {i j} ^ {c} - L C P _ {c} ^ {*} \right] + \sum_ {l \in \mathcal {L} _ {0}} \gamma_ {l} r _ {l},\tag{4a}
$$

$$
\mathrm{s.t.} \sum_ {c \in \mathcal {C}} x _ {l} ^ {c} + r _ {l} = d _ {l},
$$

$$
\forall l \in \mathcal {L} _ {0},\tag{4b}
$$

$$
\begin{array}{l} \sum_ {l \in \mathcal {L} _ {c}, \mathcal {E} (l) = i} d _ {l} + \sum_ {l \in \mathcal {L} _ {0}, \mathcal {E} (l) = i} x _ {l} ^ {c} + \sum_ {j \in \mathcal {N}} y _ {j i} ^ {c} \\ = \sum_ {l \in \mathcal {L} _ {c}, \mathcal {B} (l) = i} d _ {l} + \sum_ {l \in \mathcal {L} _ {0}, \mathcal {B} (l) = i} x _ {l} ^ {c} + \sum_ {j \in \mathcal {N}} y _ {i j} ^ {c}, \qquad \forall i \in \mathcal {N}, c \in \mathcal {C}, \end{array}\tag{4c}
$$

$$
r _ {l}, x _ {l} ^ {c} \in \mathbb {Z} _ {\geq 0},
$$

$$
\forall c \in \mathcal {C}, l \in \mathcal {L} _ {0},\tag{4d}
$$

$$
y _ {i j} ^ {c} \in \mathbb {Z} _ {\geq 0},
$$

$$
\forall c \in \mathcal {C}, (i, j) \in \mathcal {A}.\tag{4e}
$$

Objective function (4a) minimizes the total costs of covering shippers’ lanes while incorporating carriers existing networks $( \mathrm { i . e . } ,$ , the socially efficient outcome). The constant term $L C P _ { c } ^ { * }$ is the fixed optimal solution value of solving a lane-covering problem for a single carrier c over its own network (similar to Ergun et al. 2007b). See Online Appendix A for more details of the lane-covering problem formulation. In other words, through objective function (4a), costs of the added obligations for each carrier (compared with their status quo $\hat { L } C P _ { c } ^ { * }$ for all $c \in { \mathcal { C } } )$ are determined. As in existing MCLCP formulations from the literature, we have demand satisfaction Constraints (4b) and node flow balance Constraints (4c), differing only in the inclusion of outside spot options $r _ { l }$ and existing carrier contracts $d _ { l } .$

Let $\overline { { y } } _ { i j } ^ { c }$ be the optimal solution values for empty movements in the lane-covering problem solved for just the single carrier $c \in { \mathcal { C } }$ (Online Appendix A). Objective function (4a) can be rewritten as

$$
\min \sum_ {c \in \mathcal {C}} \left[ \sum_ {l \in \mathcal {L} _ {0}} \delta_ {l} ^ {c} x _ {l} ^ {c} + \sum_ {(i, j) \in \mathcal {A}} \theta_ {i j} ^ {c} (y _ {i j} ^ {c} - \overline {{y}} _ {i j} ^ {c}) \right] + \sum_ {l \in \mathcal {L} _ {0}} \gamma_ {l} r _ {l}.\tag{4f}
$$

In Ex-WDPR (Equations (1a)–(1e)), parameters $b _ { s }$ and $\Psi _ { s }$ are calculated with respect to added obligations for each carrier and the status quo of the carrier. Each package bid expresses the cost difference between a specific auction outcome and the status quo outcome of nonparticipation. Therefore, when carriers can enumerate all packages for Ex-WDPR, the optimal objective values of Ex-WDPR and Poly-WDPR (Equations (4a)–(4e)) are equivalent. Proposition 2 indicates that if Poly-WDPR has no IP relaxation gap, Ex-WDPR has no IP relaxation gap as well.

Proposition 2. The objective value of the linear relaxation of Ex-WDPR is greater than or equal to the objective value of the linear relaxation of Poly-WDPR.

## 3.3. Dynamically Generated Dual Prices

With the compact-bidding language used in Poly-WDPR (Equations (4a)–(4e)), a carrier needs to evaluate only $\vert \mathcal { L } _ { 0 } \vert$ lanes; however, with the XOR bidding language in Ex-WDPR (Equations (1a)–(1e)), in the worst case, the carrier may need to evaluate $\textstyle \prod _ { l \in { \mathcal { L } } _ { 0 } } ( d _ { l } + 1 ) \geq$ $O ( 2 ^ { | \mathcal { L } _ { 0 } | } )$ packages. Despite the manageable communication size of Poly-WDPR, its dual values do not provide the same economic meaning as the dual values of Ex-WDPR, which will form a WE when there is no IP gap. Thus, we proceed by first solving Poly-WDPR, and then, we transform its optimal solution (a set of assigned lanes and empty movements for each carrier) into a set of winning package bids.

Mapping the solution of the Poly-WDPR to $E x -$ WDPR is straightforward. From Poly-WDPR, let $\hat { x } _ { l } ^ { c }$ denote the value of decision variable $x _ { l } ^ { c }$ for carrier $c \in { \mathcal { C } }$ and lane $l \in \mathcal { L } _ { 0 } .$ . Similarly, let $\hat { y } _ { i j } ^ { c }$ be the value of decision variable $y _ { i j } ^ { c }$ for carrier c and arc $( i , j ) \in \mathcal { A }$ . For the winning bid of carrier $c ,$ denoted by $s ^ { * } ( c ) .$ , we set $\psi _ { l } ^ { s ^ { * } ( c ) } = \hat { x } _ { l } ^ { c }$ for lane $l \in \mathcal { L } _ { 0 }$ and $\dot { \psi } _ { l } ^ { s ^ { * } ( c ) } = 0$ for $\dot { l } \in \mathcal { L } \backslash \mathcal { L } _ { 0 }$ . The monetary winning bid value for carrier c is calculated as the cost to cover her own lanes $( \mathcal { L } _ { c } )$ and additional assigned shipper’s lanes $( \hat { \boldsymbol { x } } _ { l } ^ { c } , \ \forall l \in \mathcal { L } _ { 0 } )$ minus the lane-covering problem to satisfy only her existing contracts. More specifically, we have $\begin{array} { r } { b _ { s ^ { * } ( c ) } = \sum _ { l \in \mathcal { L } _ { c } } \breve { \delta } _ { l } ^ { c } d _ { l } + \sum _ { l \in \mathcal { L } _ { 0 } } \delta _ { l } ^ { c } \hat { { \mathbf { x } _ { l } ^ { c } } } + } \end{array}$ $\begin{array} { r } { \sum _ { ( i , j ) \in \mathcal { A } } \theta _ { i j } ^ { c } \hat { y } _ { i j } ^ { c } - L C P _ { c } ^ { * } = \sum _ { l \in \mathcal { L } _ { 0 } } \delta _ { l } ^ { c } \hat { x } _ { l } ^ { c } + \sum _ { ( i , j ) \in \mathcal { A } } \theta _ { i j } ^ { c } ( \hat { y } _ { i j } ^ { c } - \overline { { y } } _ { i j } ^ { c } ) } \end{array}$ Let us consider the example from Section 3.1 with a shipper and a carrier (Figure 1). We index the carrier as one in this example for consistency. The lane-covering cost, LCP<sup>∗</sup> , for the carrier is $2 \times { \dot { \mathfrak { G } } } 1 . 5 + 2 \times { \mathfrak { G } } 1 . 5 + 2 \times$ $\$ 123$ . In this individual lane-covering solution, the carrier has two empty movements on arc $( C , A ) \ ( \mathrm { i . e . , }$ $\overline { { y } } _ { C A } ^ { 1 } = 2 )$ . After solving Poly-WDP, the carrier will be assigned both trips on shipper lane 1 $( \mathrm { i . e . , } \hat { x } _ { 1 } ^ { 1 } = 2 )$ and none of the trips on shipper lane $2 \ ( \mathrm { i . e . } , \hat { x } _ { 2 } ^ { 1 } = 0 )$ . In this solution, the carrier has no empty movements on $( C , A )$ that is, $\hat { y } _ { C A } ^ { 1 } = 0 .$ . The lane-covering cost for the carrier in Poly-WDPR is $2 \times \$ 1.5$ . We generate a package bid for the carrier where we have $\breve { \Psi } _ { s ^ { * } ( 1 ) } = [ 2 , \hat { 0 } ]$ with a monetary bid value of $b _ { s ^ { * } ( 1 ) } = 2 \times$ $\ S 2 + \ S 1 \times ( 0 - 2 ) = \ S 2 ( { \mathrm { o r } } \ S 1 0 - \bar { \Phi } 8 = \ S 2 )$

However, this mapping does not provide the set of carriers’ nonwinning packages, which are needed for WE constraints in the pricing problem (Equations (3a)–(3c)). We thus generate those packages dynamically through a procedure that we name iterative dual pricing (IDP) or the IDP algorithm. Let $s ^ { * } ( c )$ specify the winning package bid for carrier c. We next generate (dynamically, as needed) the relevant WE pricesetting nonwinning bids (as shown in the framework of Section 3.2), a small subset of the full set of all possible package bids. Given a fixed price vector of iteration t denoted by $p ^ { t } ,$ with $p _ { l } ^ { t }$ elements denoting the price of lane l on iteration $t ,$ the following separation problem for carrier $c \in { \mathcal { C } }$ (henceforth referred as $\hat { \boldsymbol { S } } E P ( \boldsymbol { c } , p ^ { t } ) )$ identifies a nonwinning package in which the WE constraint (i.e., Equation (3b)) is maximally

violated at $p ^ { t }$ :

max

$$
\sum_ {l \in \mathcal {L} _ {0}} (p _ {l} ^ {t} - \delta_ {l} ^ {c})   x _ {l} ^ {c} - \sum_ {(i, j) \in \mathcal {A}} \theta_ {i j} ^ {c} (y _ {i j} ^ {c} - \overline {{y}} _ {i j} ^ {c}),\tag{5a}
$$

$$
\text { s.t. } \sum_ {l \in \mathcal {L} _ {c}, \mathcal {E} (l) = i} d _ {l} + \sum_ {l \in \mathcal {L} _ {0}, \mathcal {E} (l) = i} x _ {l} ^ {c} + \sum_ {j \in \mathcal {N}} y _ {j i} ^ {c}
$$

$$
= \sum_ {l \in \mathcal {L} _ {c}, \mathcal {B} (l) = i} d _ {l} + \sum_ {l \in \mathcal {L} _ {0}, \mathcal {B} (l) = i} x _ {l} ^ {c} + \sum_ {j \in \mathcal {N}} y _ {i j} ^ {c}, \quad \forall i \in \mathcal {N},\tag{5b}
$$

$$
x _ {l} ^ {c} \leq d _ {l},
$$

$$
\forall l \in \mathcal {L} _ {0},\tag{5c}
$$

$$
x _ {l} ^ {c} \in \mathbb {Z} _ {\geq 0},
$$

$$
\forall l \in \mathcal {L} _ {0},\tag{5d}
$$

$$
y _ {i j} ^ {c} \in \mathbb {Z} _ {\geq 0},
$$

$$
\forall (i, j) \in \mathcal {A}.\tag{5e}
$$

A solution where the objective function value is greater than the carrier’s surplus from her winning bid $( \mathrm { i . e . , }$ where $\begin{array} { r } { S E P ^ { * } ( c , p ^ { t } ) > \sum _ { l \in \mathcal { L } _ { 0 } } ^ { } \psi _ { l } ^ { s ^ { * } ( c ) } p _ { l } ^ { t } - b _ { s ^ { * } ( c ) } ) } \end{array}$ indicates that the carrier finds a preferred package at $p ^ { t } ,$ , and hence, the associated WE constraint is added to WAD (Equations (3a)–(3c)). The procedure stops when the objective is less than or equal to the current surplus (after checking for all carriers), and thus, there is no new WE constraint to be added to WAD. One of the desirable properties of the base version of the separation problem (i.e., Equations (5a)–(5e)) is that it can be solved quickly:

Proposition 3. The base version of the separation problem can be solved in polynomial time.

With these iterative steps in place, IDP can be initialized with spot-market rates because WAD starts with an empty constraint set (3b) and thus, no other provisional WE prices at $t = 0$

Proposition 4. IDP terminates in finite number of steps.

Payments and surpluses of the shipper and the carriers are calculated linearly. The payment to carrier $c \in { \mathcal { C } } ,$ denoted by ${ \mathcal P _ { c \prime } }$ is

$$
\mathcal {P} _ {c} = \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*} (c)} p _ {l} ^ {*},
$$

where $p _ { l } ^ { * }$ is the final anonymous price of lane l from WAD. The shipper’s payment is $\textstyle \sum _ { c \in { \mathcal { C } } } { \mathcal { P } } _ { c } ,$ implying strong budget balance.

Proposition 5. If Poly-WDPR has no $I P$ gap, upon termination IDP finds prices that satisfy individual rationality, strong budget balance, and Walrasian equilibrium.

## 3.4. Additional Practical Constraints

In practice, additional practical constraints might be needed. We consider the following sets of practical constraints to demonstrate how the ideas presented can be adapted to such extensions.

• Winner-per-lane constraints. The shipper may enforce lower and upper bounds on the number of winners for each lane $l \in \mathcal { L } _ { 0 }$ denoted by $\underline { n } _ { l }$ and ${ \overline { { n } } } _ { l } ,$ respectively. In practice, upper bounds might be desired to reduce the management complexity of working with many suppli ers. Lower bounds allow the shipper to have backup options in case of carrier failure or load rejections in real time. The following linear constraints would be added to Ex-WDPR (Equations (1a)–(1e)):

$$
(\alpha_ {l} ^ {L B}) \qquad \sum_ {s \in \mathcal {S}} \phi_ {l} ^ {s} \chi_ {s} \geq \underline {{n}} _ {l}, \qquad \forall l \in \mathcal {L} _ {0},\tag{1f}
$$

$$
(\alpha_ {l} ^ {U B}) \qquad \sum_ {s \in \mathcal {S}} \phi_ {l} ^ {s} \chi_ {s} \leq \overline {{n}} _ {l}, \qquad \forall l \in \mathcal {L} _ {0}.\tag{1g}
$$

For bid $s \in \mathcal S$ and lane $l \in \mathcal { L } _ { 0 } ,$ , binary parameter $\phi _ { l } ^ { s }$ equals one if $\psi _ { l } ^ { s } > 0 .$ . Corresponding dual values are presented in parentheses on the left side of each constraint set. Dual variable $\alpha _ { l } ^ { L B }$ can be interpreted as a discount on lane $l \in \mathcal { L } _ { 0 }$ offered by the shipper to have at least $\underline { n } _ { l }$ winners on l. On the other hand, $\alpha _ { l } ^ { U B }$ can be interpreted as an additional license fee that a winning carrier of lane $l \in \mathcal { L } _ { 0 }$ should pay to operate on l. A similar constraint set can be added to Poly-WDPR (Equations (4a)–(4e)). Let binary decision variable $z _ { l } ^ { c }$ equal one if carrier $c \in { \mathcal { C } }$ covers at least one shipment on lane $l \in { \mathcal { L } } _ { 0 } \colon$

$$
z _ {l} ^ {c} \leq x _ {l} ^ {c} \leq d _ {l} z _ {l} ^ {c}, \quad \forall c \in \mathcal {C}, l \in \mathcal {L} _ {0},\tag{4g}
$$

$$
\underline {{n}} _ {l} \leq \sum_ {c \in \mathcal {C}} z _ {l} ^ {c} \leq \overline {{n}} _ {l},
$$

$$
\forall l \in \mathcal {L} _ {0},\tag{4h}
$$

$$
z _ {l} ^ {c} \in \{0, 1 \},
$$

$$
\forall c \in \mathcal {C}, l \in \mathcal {L} _ {0}.\tag{4i}
$$

• Lane-bound constraints. A carrier may enforce lower bounds and upper limit (capacity) on the number of times that she covers lane l denoted by Let $\underline { { \omega } } _ { l }$ and $\overline { { \omega } } _ { l } ,$ respectively. These constraints do not impact Ex-WDPR (Equations (1a)–(1e)) as the carriers can incorporate them while generating their bid sets through the separation problem. For Poly-WDPR (Equations (4a)–(4e)) using $z _ { l } ^ { c }$ binary decision variables, we can formulate the following linear constraints:

$$
\underline {{\omega}} _ {l} z _ {l} ^ {c} \leq x _ {l} ^ {c} \leq \overline {{\omega}} _ {l} z _ {l} ^ {c}, \quad \forall c \in \mathcal {C}, l \in \mathcal {L} _ {0},\tag{4j}
$$

$$
z _ {l} ^ {c} \in \{0, 1 \}, \quad \forall c \in \mathcal {C}, l \in \mathcal {L} _ {0}.\tag{4k}
$$

• Strategic-partner constraints. The shipper may enforce lower and upper bounds on the number of her strategic partners (winners of lane contracts) denoted by m and ${ \overline { { m } } } ,$ respectively. Again, these bounds would be used to reduce the management complexity of dealing with multiple partner companies but here, in the aggregate as opposed to the lane-by-lane level used above. The following linear constraints can be added to Ex-WDPR (Equations (1a)–(1e)):

$$
(\beta^ {L B}) \qquad \sum_ {s \in \mathcal {S}} \lambda_ {s} \chi_ {s} \geq \underline {{m}},\tag{1h}
$$

$$
(\beta^ {U B}) \qquad \sum_ {s \in \mathcal {S}} \lambda_ {s} \chi_ {s} \leq \overline {{m}}.\tag{1i}
$$

For bid $s \in S ,$ , binary parameter $\lambda _ { s }$ equals one if bid s has at least a lane $l \in \mathcal { L } _ { 0 }$ such that $\psi _ { l } ^ { s } > 0$ . Corresponding dual values are presented in parentheses on the left side of each constraint. Dual value $\beta ^ { L B }$ is also interpreted as a lump-sum discount offered by the shipper to the winning carriers to be among her strategic partners. On the other hand, $\beta ^ { U B }$ is interpreted as a license fee that the winning carriers should pay so that they become strategic partners of the shipper. To define the same constraint set for Poly-WDPR (Equations (4a)–(4e)), let binary decision variable $z _ { c }$ equal one if carrier $c \in { \mathcal { C } }$ wins any of the shipper’s lanes:

$$
z _ {l} ^ {c} \leq z _ {c}, \quad \forall c \in \mathcal {C}, l \in \mathcal {L} _ {0},\tag{41}
$$

$$
z _ {c} \leq \sum_ {l \in \mathcal {L} _ {0}} z _ {l} ^ {c},
$$

$$
\forall c \in \mathcal {C},\tag{4m}
$$

$$
\underline {{m}} \leq \sum_ {c \in \mathcal {C}} z _ {c} \leq \overline {{m}},\tag{4n}
$$

$$
\mathsf {z} _ {c} \in \{0, 1 \},
$$

$$
\forall c \in \mathcal {C}.\tag{40}
$$

Constraints (4l) ensure that if a carrier wins any shipper’s lane, she is counted as a winner. Similarly, Constraints (4m) ensure that a carrier is not counted as a winner if she does not win any of the shipper’s lanes.

Incorporating additional constraints impacts the dual models and the separation problem. See Online Appendix C for the details of these changes. The payment received by carrier $c \in { \mathcal { C } }$ when the additional practical constraints of this subsection are included is given by

$$
\mathcal {P} _ {c} = \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*} (c)} p _ {l} + \sum_ {l \in \mathcal {L} _ {0}} \phi_ {l} ^ {s ^ {*} (c)} (\alpha_ {l} ^ {L B} - \alpha_ {l} ^ {U B}) + \lambda_ {c} ^ {s ^ {*} (c)} (\beta^ {L B} - \beta^ {U B}).\tag{6}
$$

With the additional α and $\beta$ price components, the payment structure is now linear in an extended pricing space, using the interpretability of the dual values for these practical constraints to form explainable payments beyond simple lane-only pricing. The shipper pays $\sum _ { c \in { \mathcal { C } } } { \mathcal { P } } _ { c }$ , which implies strong budget balance. It is straightforward to show that with no IP gap in constrained Ex-WDPR, IDP prices satisfy individual rationality and Walrasian equilibrium.

## 3.5. Ex-WDPR with IP Gap

Thus far, we have shown the nice properties that occur under an assumption that Ex-WDPR (Equations (1a)–(1e)) and Poly-WDPR (Equations (4a)–(4e)) have no IP gap. However, this is not always the case (see Online Appendix D for an example), with IP gaps becoming more common when additional practical constraints are considered.

As IDP progresses, with the new packages dynamically generated through the separation problem, it could be that Ex-WDPR starts to show an IP relaxation gap, which means that WAD (Equations (3a)–(3c)) reports infeasibility. This indicates that given the optimal allocation determined by Ex-WDPR, we cannot find linear prices that can satisfy WE constraints. To handle such cases, we add a relaxation term $\epsilon _ { c }$ specified for each carrier $c \in { \mathcal { C } }$ to WE cuts and modify the WAD model to find prices that minimize the deviation from WE. To do so, we consider a large coefficient M for $\epsilon _ { c }$ in the objective function. The modified winner-aware dual ɛ-WAD is formulated as follows:

$$
\max \sum_ {l \in \mathcal {L} _ {0}} d _ {l} p _ {l} - \sum_ {c \in \mathcal {C}} M \epsilon_ {c}\tag{7a}
$$

$$
\mathrm{s.t.} \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*}} p _ {l} - b _ {s ^ {*}} \geq 0,
$$

$$
\forall s ^ {*} \in \mathcal {S} ^ {*},\tag{7b}
$$

$$
\sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*}} p _ {l} - b _ {s ^ {*}} \geq \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s} p _ {l} - b _ {s} - \epsilon_ {\mathrm{C} _ {s}},
$$

$$
\forall s ^ {*} \in \mathcal {S} ^ {*}, s \in \mathcal {S} \backslash \mathcal {S} ^ {*}, C _ {s ^ {*}} = C _ {s},\tag{7c}
$$

$$
p _ {l} \leq \gamma_ {l},
$$

$$
\forall l \in \mathcal {L} _ {0}.\tag{7d}
$$

Here, by separating IR and WE constraints, we do not include any $\epsilon _ { c }$ term in Constraints (7b) to enforce individual rationality while allowing for deviation from WE through Constraints (7c). Similar to the no $\mathrm { I P }$ gap scenario, IDP continues until no nonwinning packages are found at the fixed prices. At the final prices, we might have some carriers with positive $\epsilon _ { c } ^ { * } ,$ , which is interpreted as the carrier’s residual envy (or deviation from WE). This approach is consistent with recent work on ɛ-equilibria: for example, in Lahaie and Lubin (2019). Although other norms are possible to measure closeness to WE, here we minimize the linear $\| \epsilon _ { c } \| _ { 1 }$ norm for ease of computation and interpretation.

Although the ɛ-relaxation approach is one way to handle IP gaps (which we will show is often reasonable in our numerical experiments where ɛ values are small), an alternative is to generate additional cutting planes and price the resulting cuts as meaningful nonlinear price terms that can reduce or ideally close the $\mathrm { I P }$ gap (i.e., reduce ɛ values or drive them to zero) and set payments such that both IR and WE constraints are satisfied. Incorporating these new constraints into the primal problem (i.e., Ex-WDPR in Equations (1a)–(1e)) requires updates to the WAD (i.e., Equations (7a)–(7d)) and separation problems, so there is a natural trade-off; if model complexity and nonlinear price interpretation are not desired, one option is to simply deal with ɛ-relaxations of WE as presented thus far. But, for some environments, the additional computational effort of generating and pricing cutting planes may be justified as we show that it can be effective in eliminating residual envy in many instances (see Section 4.3.3).

3.5.1. The Cutting-Plane Procedure. In the operations research literature, various cutting-plane methods have been used to strengthen IP formulations, but here, we are among the first to propose the use of cutting planes, where cuts are interpreted as artificial items that will be paid for (linearly), thus incrementally closing the IP gap while adjusting total payments toward a WE. For CA/CE applications, interpretability of prices is of primary concern, so although many cutting methods are available, we focus here on perhaps the most natural to interpret, clique cuts, in which there is a set of package bids for which at most one could be accepted in any scenario. (If we were to draw a conflict graph with nodes as package bids and edges between any two that cannot both be accepted feasibly, such a set is a complete subgraph or clique.) Package bids in $E x -$ WDPR (i.e., Equations (1a)–(1e)) that mutually exclude one another in this way may be part of a fractional solution to its linear-programming relaxation, and thus, a cut that says at most one of these bids can be accepted will improve the relaxation.

Given a fractional solution to Ex-WDPR, we generate conflict cliques that include exactly one winning bid, ensuring that exactly one bidder pays the newly generated dual price associated with the cut. This dual price may, therefore, be interpreted as a penalty imposed on that winning package to be the single winner from the set of competing bids, only one of which could actually win in any feasible outcome. This dual penalty term can thus be seen as the cost of “exclusivity rights” or a “local monopoly penalty,” where “local” indicates that the collection of mutually exclusive bids must overlap on some set of actual lanes. (Such monopoly effects can occur in different local regions of the transportation network.) Online Appendix E presents our clique-cut generation procedure.

We denote the set of generated clique cuts by K. Each cut $k \in K$ is then added to the winner-determination problem as follows:

$$
\left(q _ {k}\right) \quad \sum_ {s \in \mathcal {S} _ {k}} \chi_ {s} \leq 1,\tag{1j}
$$

where $\boldsymbol { S _ { k } }$ denotes the set of bids that are included in cut $k \in K .$ . The new price term $q _ { k }$ (corresponding dual value of cut k) is paid by the single winning bid in $S _ { k } .$ Note that in a procurement auction or exchange, the sign of these priced items is the reverse of lane prices $p _ { l }$ so that a winning bidder is paid the corresponding lane prices minus any local monopoly penalties. As shown in Online Appendix F, the modified ɛ-WAD that incorporates the new price terms enforces IR for the bidding carriers as well. Assuming no additional practical constraints and given the complete set of cuts, $K ,$ each carrier c (whose winning bid is denoted by $s ^ { * } ( c ) )$ is paid:

$$
\mathcal {P} _ {c} = \sum_ {l \in \mathcal {L} _ {0}} \psi_ {l} ^ {s ^ {*} (c)} p _ {l} ^ {*} - \sum_ {k \in K: s ^ {*} (c) \in \mathcal {S} _ {k}} q _ {k} ^ {*}.
$$

To enforce strong budget balance, the shipper’s payment remains the sum of all payments to the carriers. We should note that the clique cuts that we employ are not guaranteed to close the IP gap (a counterexample is given in Online Appendix D), but we show that they can be quite effective in closing the IP gap in most instances (see Section 4.3.3), leaving only small gaps otherwise, and are among the most naturally interpretable of cuts to price.

Algorithm 1 (The Iterative Dual-Pricing Procedure) Outputs: Price vector p; vector q, and $\epsilon _ { c }$ for all $c \in { \mathcal { C } } ;$ Input: Set of compact bids;

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Phase 1:
Generate WE
Constraints
    Solve Poly-WDPR;
    Map Poly-WDPR solution on Ex-WDPR;
    $p \leftarrow p^{0}$ (i.e., initialize with spot-market prices);
    $t \leftarrow 0$;
    $newCons \leftarrow True$;
    While $newCons == True$ do :
    $newCons \leftarrow False$;
    Solve $\epsilon$-WAD;
    $p^{t} \leftarrow p^{*}$ and $\epsilon^{t} \leftarrow \epsilon_{c}^{*} \quad \forall c \in \mathcal{C}$;
    For $c \in \mathcal{C}$ do :
    Solve $SEP(c, p^{t})$;
    If $SEP^{*}(c, p^{t}) &gt; \sum_{l \in \mathcal{L}_{0}} \psi_{l}^{s^{*}(c)} p_{l}^{t} - b_{s^{*}(c)} + \epsilon_{c}^{t}$ do :
    Generate new nonwinning bid s from $SEP^{*}(c, p^{t})$;
    $S \leftarrow s$;
    $newCons \leftarrow True$;
    $t \leftarrow t + 1$;
    $p \leftarrow p^{t}$;
    $\epsilon_{c} \leftarrow \epsilon_{c}^{t} \quad \forall c \in \mathcal{C}$.

Phase 2:
Generate Clique Cuts and Update Prices
    If $\exists c \in \mathcal{C}: \epsilon_{c} &gt; 0$ do :
    Clique Generation ($G'$) from Algorithm 2 (Online Appendix E);
    Solve modified $\epsilon$-WAD with $q$ (i.e., clique-cut dual values);
    $p \leftarrow p^{*}$ and $q \leftarrow q^{*}$;
    $\epsilon_{c} \leftarrow \epsilon_{c}^{*} \quad \forall c \in \mathcal{C}$.
</div>

The pseudocode of our proposed two-phase mechanism is presented in Algorithm 1. The mechanism starts with carriers submitting bids using the compactbidding language. The first phase begins with solving the Poly-WDPR (Equations (4a)–(4e)) to determine the winners. The solution of Poly-WDPR is mapped onto Ex-WDPR (Equations (1a)–(1e)). Then, using the optimal allocation, we solve ɛ-WAD (Equations (7a)–(7d)), fix prices and carriers’ residual envy to the optimal solutions of ɛ-WAD $( \mathrm { i . e . , } p ^ { \ast }$ and $\epsilon _ { c } ^ { * }$ values), and solve the separation problem to determine nonwinning bids for each carrier to generate new WE constraints for ɛ-WAD. We iterate between ɛ-WAD and the separation problem until no new WE constraint is generated $( \mathrm { i . e . , }$ newCons is false). We then check if we have no residual envy and satisfy Walrasian equilibrium. If yes, we stop.

If not, we move to the second phase of the mechanism and generate clique cuts using (Algorithm 2, Online Appendix E). We then solve the modified ɛ-WAD that incorporates clique-cut dual variables (see Online Appendix F for the formulation), and we recalculate prices and residual envy for the carriers.

## 3.6. Procurement Exchange for Lanes

In common practice, procurement auctions for lanes only take lane-by-lane bids, sometimes augmented with a small set of individual package bids. Our description thus far of PAL adds the expressive polynomial-sized communication of an entire network (thus considering all network effects in implicit package bids) and enhances pricing with WE computation and cut prices $q .$ Here, we also investigate the possibility of lane exchange in the procurement of lane contracts, which we refer to as PEL. In PEL, we allow a carrier to benefit by picking up lanes of other carriers or allowing some of its lanes to be outsourced to others, with the following minor modifications to the framework as described so far.

Each carrier $c \in { \mathcal { C } }$ has $d _ { l } - f _ { l }$ shipments available for exchange on lane $l \in \mathcal { L } _ { c } ,$ where $f _ { l }$ denotes the number of shipments that carrier c must operate by herself on lane $l \in \bar { \mathcal { L } } _ { c }$ . The package bid $s \in \mathcal S$ is similarly denoted by $\langle \mathrm { C } _ { s } , \Psi _ { s } , b _ { s } \rangle$ , where $\Psi _ { s }$ is a vector of $| { \mathcal { L } } |$ integers with each component $\psi _ { l } ^ { s }$ indicating the number of times lane l ∈ $\mathcal { L } \backslash \mathcal { L } _ { \mathrm { C } _ { s } }$ is covered (indicated by a positive integer) or hired out for $l \in \mathcal { L } _ { \mathrm { C } _ { s } }$ (indicated by a negative integer) in package s ∈ S. The monetary value of bid s ∈ $s$ is denoted by $b _ { s \prime }$ which can be positive or negative depending on the net value of lanes added and removed. Here, to make the formulations more compact, we denote the shipper as any other carrier, just one whose bids only include hiring lanes out and that is willing to pay spot-market rates otherwise. The Ex-WDPR, formulated in Equations (1a)–(1e), is modified for PEL as follows:

$$
\min \sum_ {s \in \mathcal {S}} b _ {s} \chi_ {s} + \sum_ {l \in \mathcal {L}} \gamma_ {l} r _ {l},\tag{8a}
$$

$$
\mathrm{s.t.} \sum_ {s \in \mathcal {S}} \psi_ {l} ^ {s} \chi_ {s} + r _ {l} = 0, \quad \forall l \in \mathcal {L},\tag{8b}
$$

$$
\sum_ {s \in \mathcal {S} _ {c}} \chi_ {s} = 1, \quad \forall c \in \mathcal {C},\tag{8c}
$$

$$
\chi_ {s} \in \{0, 1 \}, \quad \forall s \in \mathcal {S},\tag{8d}
$$

$$
r _ {l} \in \mathbb {Z} _ {\geq 0}, \quad \forall l \in \mathcal {L}.\tag{8e}
$$

Further details of the PEL dual models, Poly-WDPR, and cut separation can be found in Online Appendix G. Note that the practical constraints presented in Section 3.4 extend to PEL as well. The IDP algorithm remains similar under PEL. It is straightforward to show that if there is no IP gap in Ex-WDPR (Equations (8a)–(8e)), the prices calculated through IDP satisfy individual rationality and WE. Similar results hold if practical constraints are considered in the winnerdetermination problem.

When clique cuts are not needed to establish WE, linear prices associated with lanes and practical constraints clearly satisfy strong budget balance. (See Online Appendix H for details.) Because dual values associated with cli que cuts are paid by carriers as fees (negative payments), it is not uniquely determined who should collect these additional payments under PEL when the shipper is not the only net procurer. In our numerical results, we allo cate this additional surplus to the auctioneer (shipper) as one natural approach, but a proportional division of surplus similar to Milgrom and Watt (2022) could also be considered. Additional details and a numerical example are given in Online Appendix H. Further discussions of payment division in combinatorial exchanges can be found in Day (2013).

## 4. Experiments and Discussions

For PAL, we benchmark our proposed procurement market design using IDP against VCG and a standard simultaneous multiround auction tailored for the truckload transportation market (see Online Appendix I for details). SMRA has been frequently used in practice (for example, in many spectrum license auctions) because it is straightforward to describe and implement. The format is known to work well when goods are substitutes but may not perform well otherwise, a motivation for CA techniques in general (Bedard et al. 2020). Its use here is similar to a comparison with a greedy algorithm, and it helps show the value of sealed-bid efficient CA techniques in the current simulated context (i.e., that complementarities are significant here). See Online Appendix J for details on the VCG setup for the current truckload procurement process.

## 4.1. Evaluation Criteria

To evaluate the market outcomes in different settings and using different pricing schemes, we utilize the following metrics.

• Total savings. We compute the difference between the total costs in the status quo (i.e., when carriers and the shipper do not participate in a market) and the total costs after participation in a PAL or PEL market as proposed here:

$$
\begin{array}{l} S a v i n g s = \sum_ {c \in \mathcal {C}} L C P _ {c} ^ {*} + \sum_ {l \in \mathcal {L} _ {0}} \gamma_ {l} \\ \qquad - \left(Z ^ {*} (E x \text {-WDPR}) + \sum_ {c \in \mathcal {C}} L C P _ {c} ^ {*}\right) \\ \qquad = \sum_ {l \in \mathcal {L} _ {0}} \gamma_ {l} - Z ^ {*} (E x \text {-WDPR}), \end{array}
$$

where $Z ^ { * } ( E x { - } W D P R )$ is the optimal value of Ex-WDPR (Equations (1a)–(1e)) plus additional practical constraints where indicated. Because VCG and IDP are both efficient mechanisms, this metric will be the same. For SMRA, on the other hand, this comparison with efficient mechanisms will measure efficiency loss. Although VCG and IDP can incorporate a wide variety of side constraints (as with any IP-based method), SMRA cannot readily handle every practical constraint type described so far. Thus, in our numerical comparisons of total savings, we consider only the simpler lane-bound constraints (Equations (4j) and (4k)) for the PAL setting because adapting SMRA to handle more complex constraints is often not straightforward. Similarly, we define relative savings, which is the ratio of savings to total costs in the status quo.

• Shipper and carriers’ surplus. To evaluate market outcomes for the participants, we measure their surplus using different pricing schemes.

• Residual envy. We report $\epsilon _ { c \prime }$ the maximum relaxation of a carrier’s WE Constraint (7c), equal to the maximum amount of additional profit that a carrier would receive from another package as compared with her optimal package at the reported prices.

## 4.2. Data Generation

Our data-generation process is based on Chen et al. (2009) with modifications tailored to our problem setting. To generate instances, we consider 100 large cities in the contiguous United States divided into five regions: the Northeast (8 cities), the Southeast (13 cities), the Midwest (23 cities), the Southwest (23 cities), and the West (33 cities). In each region, we consider one shipper and five carriers. Within each region, we randomly generate U{50, 100} lanes for the shipper<sup>4</sup> and U{40, 70} existing lanes for each carrier. The demand for each lane is generated using U{20, 40}.

We also consider three network structures for the shipper’s network: (1) a uniform network, where the lanes are selected uniformly at random from a complete graph with cities as vertices; (2) a unidirectional hub-and-spoke network, where a few hubs are selected and for each carrier, all of the generated lanes have either inbound or outbound trips to each of these hubs; and (3) a bidirectional hub-and-spoke network, which is similar to that unidirectional hub-and-spoke network but includes a combination of inbound and outbound trips.

We consider uniform networks for all carriers. From above, we generate 3 different shipper networks in each region (15 networks in total). For each network, we consider the following treatments.

• Exchange level. Knowing that carriers may be reluctant to share all of their private information about existing lanes and put those contracts up for trade, we simulate carriers that may choose to make only some and potentially none of their lanes available for exchange. We consider three scenarios for the fraction of lanes that are available for exchange from each carrier: Exchange Level $\in \{ 0 \% , 5 0 \% , 1 0 0 \% \}$

• Practical constraints’ parameters. For the winnerper-lane constraints, we consider ${ \underline { { n } } } _ { l } = \{ 1 , 2 \}$ and ${ \overline { { n } } } _ { l } = \{ { n } _ { l }$ $+ 2 , \ldots , | { \mathcal { C } } | \}$ for all $l \in \mathcal { L } _ { 0 }$ . For the strategic-partner constraints for the shipper, we set $\underline { { m } } = \{ 1 , 2 \}$ and $\overline { { m } } =$ $\{ \underline { { m } } + 2 , \ldots , | \mathcal { C } | \}$ }. For the lane-bound constraints, we con sider $\begin{array} { r } { w _ { l } = \lfloor \frac { d _ { l } } { 3 } \rfloor } \end{array}$ and ${ \overline { { w } } } _ { l } = d _ { l }$ for all $l \in \mathcal { L } _ { 0 }$ in all instances. We do not impose winner-per-lane and lane-bound constraints on any carrier’s exchangeable lanes.

Based on these configurations, we run 630 instances. For each carrier, the cost per mile (dollars) to travel loaded on a lane is drawn randomly between \$1 and \$2 in increments of \$0.1 (i.e., from U{10, 20}=10). For each carrier, we consider equal cost per mile across each region. The cost to cover a lane is the Euclidean distance times the cost per mile. For each carrier, empty travel on any arc is 75% of the cost per mile for traveling loaded. The spot-market rate is set at \$3 per mile (except in the robustness checks of Online Appendix K).

## 4.3. Results and Discussions

All instances were run on a standard personal computer (Intel Core i7-6700 CPU at 3.40 GHz, RAM 32 GB) with a four-hour time limit to run Phase 1 for each instance and a one-hour time limit to run Phase 2 fo those instances where we find positive residual envy from Phase 1. We used Gurobi 10.0 (Gurobi Optimization and LLC 2023) for all optimization calls across all models and pricing schemes.

4.3.1. Benefits of a Centralized Market Approach. We first present the results for PAL with only lane-bound constraints, where we benchmark VCG and IDP savings against SMRA. Note that incorporating strategicpartner and winner-per-lane constraints in an SMRA is not straightforward.

The results are summarized in Figure 2, showing the benefits of a one-shot combinatorial auction compared with SMRA’s tatonnement heuristic for optimization; relative savings are significantly higher in VCG/IDP (13.4% versus 9.4%). This also highlights the value of a compact-bidding language that allows carriers to submit their complex preferences effectively given a trusted platform with which to share data.

Next, we highlight significantly improved results (using IDP/VCG) as carriers become more willing to exchange lanes as shown in Table 1 and Figure 3. In Table 1, “status quo” refers to the total transportation costs when carriers satisfy only their own contracts and the shipper relies on spot-market rates, whereas the “market” column shows total costs when instead using an auction or exchange. The market outcome’s average relative savings is 14.24% (\$1.24 million average saving),<sup>5</sup> even without lane exchange among carriers.

Figure 2. (Color online) Relative Savings  
![](/api/attachments/KJDKDQ33/fulltext/images/b2eb9003f70ece91e14b11a055e0759d572e237b9fdd629fdce2f57b6b99790c.jpg)  
Note. Boxes indicate interquartile ranges and medians, with means as red dots.

Relative savings increase to 39.72% as the level of exchange among carriers increases from zero (no exchange among carriers) to 100%.

4.3.2. Shipper and Carrier Benefits. Although total savings remain the same for any efficient mechanism, here we discern the difference between the efficient mechanisms by showing the surplus of the shipper and the participating carriers under the two pricing schemes, reporting the average shipper’s surplus and the average total carriers’ surplus over our generated instances. Recall that surplus here is relative to the status quo of nonparticipation in the market, and note for comparison that the average size of the shipper’s business, measured as the total costs to cover her lanes through the spot market, is \$1.81 million. Similarly, the average size of the carriers’ business, measured as the total cost to cover their existing lanes if they were to operate individually, is \$6.9 million. Similar to IDP, in order to establish BB under VCG, the shipper’s payment equals the sum of all carriers’ payments, and the shipper’s surplus is calculated as her total costs to cover her lanes through the spot market minus her payment. A carrier’s surplus under VCG equals her VCG discount as explained in Online Appendix J. The results are summarized in Table 2 and Figures 4 and 5.

Figure 3. (Color online) Summary of the Results with Efficient Allocations and Different Exchange Levels  
![](/api/attachments/KJDKDQ33/fulltext/images/1c2b700317c42232b0f828c21b177d79a0e0c5094eb5f04dccdec7645bdd8846.jpg)

Not surprisingly, we find that with both VCG and IDP, as the exchange-level willingness among carriers increases, their total surplus increases significantly. This effect is more pronounced under VCG, where carriers’ surplus grows more than 15 times (from \$0.25 million to \$4.06 million) when going from zero to 100% exchange; carriers’ total surplus rises 16 times (from \$0.15 million to \$2.55 million) under IDP. Here, \$4.06 million represents 59% of their \$6.9 million status quo business costs (under VCG), and \$2.55 million represents 37% of their existing business costs (under IDP). Clearly, these payoff differences provide huge motivation for carriers to participate in a lane-exchange format that also benefits the entire system as a whole, reducing costs, fuel consumption, and vehicles on the road. Intuitively and as discussed in Day (2013), VCG rewards both exchange partners for the cost reduction that their participation unlocks, in essence forcing the mechanism to “double pay” for the overall rewards. So, although both mechanisms provide great benefits to carriers for their willingness to exchange lanes, there are theoretical reasons for thinking that VCG benefits them too much, and our experiments both confirm this intuition and provide a sense of the scale of this difference.

Further, the shipper’s surplus shows a very different trend with VCG versus IDP mechanisms. From Figure 5(a), we find that as exchange level among carriers increases, the shipper’s surplus goes down significantly. There are instances with 50% and 100% exchange levels where the shipper’s surplus is negative, implying that when carriers exchange lanes, the market is not attractive for the shipper relative to simply opting for the spot market (her status quo outcome). In other words, with VCG pricing, the payments required to induce the carriers to bid truthfully are so high that the shipper would rather not participate at all. On the other hand, from Figure 5(b), we see that under IDP, the shipper’s surplus remains fairly stable (with only a slight decrease) and positive as the carriers increase their willingness to exchange among themselves.

Table 1. Efficiency Improvements Under Exchange-Level Scenarios

<table><tr><td rowspan="2">Exchange level, %</td><td colspan="2">Total costs, $ million</td><td rowspan="2">Savings, $ million</td><td rowspan="2">Relative savings, %</td></tr><tr><td>Status quo</td><td>Market</td></tr><tr><td>0</td><td>8.71</td><td>7.47</td><td>1.24</td><td>14.24</td></tr><tr><td>50</td><td>8.71</td><td>6.33</td><td>2.38</td><td>27.32</td></tr><tr><td>100</td><td>8.71</td><td>5.25</td><td>3.46</td><td>39.72</td></tr></table>

Table 2. Shipper’s and Carriers’ Average Savings Under VCG vs. IDP

<table><tr><td></td><td colspan="2">Shipper, $ million</td><td colspan="2">Carriers, $ million</td></tr><tr><td>Exchange level, %</td><td>VCG</td><td>IDP</td><td>VCG</td><td>IDP</td></tr><tr><td>0</td><td>1.00</td><td>1.09</td><td>0.25</td><td>0.15</td></tr><tr><td>50</td><td>0.19</td><td>1.04</td><td>2.14</td><td>1.29</td></tr><tr><td>100</td><td>-0.60</td><td>0.91</td><td>4.06</td><td>2.55</td></tr></table>

Overall, we see that both the shipper and the carriers maintain large positive net surpluses for participating in IDP, which cannot be said for VCG. Although the carriers’ surplus is lower with IDP (compared with VCG), they still benefit greatly, particularly when they exchange lanes. Although they might prefer the VCG outcome, it would not be chosen by a shipper given the option of IDP. We also perform sensitivity analyses in Online Appendix K to show that our results still hold if the spot-market rate changes. The overall results also highlight the value of information sharing among the carriers, which not only reduces the bidding complexity for them significantly (simply share all network information) but also helps them collect additional benefits while producing linear and explainable prices that can guide future bidding and long-term business investment.

Figure 4. (Color online) Total Carriers’ Surplus  
![](/api/attachments/KJDKDQ33/fulltext/images/0bc1edfad1a08dd6c1fce63279954ee40909ddd23526c9119304162b41b4ef2b.jpg)  
Notes. (a) VCG. (b) IDP.

Finally, although we propose WE prices for this environment based on their understandable price feedback and good incentive properties cited in the literature, we remind the reader that the resulting mechanism is not incentive compatible (strategy proof), like VCG. As noted by Parkes et al. (2001), any bidder will see the dif ference between her final payment and the VCG payment as the maximum possible benefit of shading her bid (i.e., inflating her costs) to attempt to extract the VCG surplus. Yet, this individual deviation from truth telling does not represent an obvious or risk-free manipulation as the inflation of cost toward the VCG outcome is only safe if undertaken unilaterally; if other complementary bidders also inflate costs, participants risk missing preferred bundles and thus, lowering their surpluses. Bu¨ nz et al. (2022) show that in competitive envir onments, auctioneer and bidder surpluses will converge at equilibrium to an intermediary point between the VCG point and the truth-telling outcome under a bidder-optimal core-selecting rule, a perspective shared by Schneider et al. (2015) under risk or loss aversion and by Ausubel and Baranov (2020) under bidder-value correlation. Thus, although we forgo a direct Bayes–Nash equilibrium analysis as in those papers (which was only technically feasible in markets that were very small in comparison with the current setting), the literature supports the notion that actual performance with strategic players will converge somewhere in between the two extremes presented in our results (VCG and WE under truth telling), approaching closer to the latter as competition, risk or loss aversion, or value-correlation increase. Because all of our results show substantial improvements over the status quo (except for the shipper that is worse off under a full exchange and VCG), our computational results, therefore, support the following characterizations.

![](/api/attachments/KJDKDQ33/fulltext/images/5c2df43be28f03268466d65479eb2e753f87c83655e37cdb40d5bca8c5d35b80.jpg)

Figure 5. (Color online) Shipper’s Surplus  
![](/api/attachments/KJDKDQ33/fulltext/images/3dd7da4915887683cfc6749352c4c23595df94af522c1a9b14b2b5099cac1a19.jpg)

![](/api/attachments/KJDKDQ33/fulltext/images/b49001f1e22ada30db1f7d79258fd2c5ae203b0f3e16261c75b606756d5f221b.jpg)  
Notes. (a) VCG. (b) IDP.

• All players prefer participation over the status quo under IDP.

• Carriers are close to indifferent between VCG and IDP when there is no exchange, but they can benefit from manipulation under IDP more as the level of exchange increases.

• The use of an exchange unlocks significant efficiency gains, putting additional “money on the table” that encourages carriers to participate in exchanging lanes.

• The shipper is closer to indifferent to the amount of exchange chosen by carriers under IDP compared with VCG. Thus, although a shipper/auctioneer would not want to unlock the gains from exchange under VCG, she would be much more willing under IDP.

4.3.3. Residual Envy and the Impact of Clique Cuts. The first phase of our mechanism (Algorithm 1) generates packages to support equilibrium prices and reports residual envy, $\epsilon _ { c \prime }$ for each carrier. We then calculate total residual envy as $\textstyle \sum _ { c \in { \mathcal { C } } } \epsilon _ { c }$ . We also find that the algorithm run times are significantly shorter when no exchange is allowed (less than two minutes). As the number of lanes available to be exchanged increases, we find slower convergence; Phase 1’s average run times for 50% and 100% exchange levels are 30 and 103 minutes, respectively. Adding exchange possibilities opens new symmetries among the potential packages, resulting in more difficult proofs of IP optimality even when solutions are high quality. This is particularly more challenging when the shipper considers lowerbound requirements for winners per lane and strategic partners because in these cases, carriers receive additional payments from the shipper that wants to secure multiple partners (see Equation (6)). These additional payments improve the potential surplus of relevant packages, requiring more nonwinning packages to be generated in Phase 1.

For instances with positive total residual envy, we move to the second phase of the mechanism to generate clique cuts in order to reduce or ideally, eliminate residual envy. The average number of clique cuts gen erated per instance in the second phase is 40, ranging from 10 to 133 cuts.

Table 3 summarizes our results. The columns under “envy free, no.” in Table 3 report the numbers of instances where IDP reported no residual envy from Phase 1 (i.e., those for which $\textstyle \sum _ { c \in { \mathcal { C } } } \epsilon _ { c } = 0 )$ before and after adding clique cuts (of 210 instances for each exchange level). The columns under “residual envy (dollars)” in Table 3 report the residual envy averages (in dollars) over only those instances with positive residual envy before adding the clique cuts. Note that total costs for each market are millions of dollars, so these deviations are consistently represent fractions of a percentage of total market value.

Table 3. Summary of the Results (Averaged on 210 Instances for Each Exchange Level)

<table><tr><td rowspan="2">Exchange level, %</td><td colspan="2">Envy free, no.</td><td colspan="2">Residual envy, dollars</td></tr><tr><td>Without cuts</td><td>With cuts</td><td>Without cuts</td><td>With cuts</td></tr><tr><td>0</td><td>41</td><td>209</td><td>1,212</td><td>6</td></tr><tr><td>50</td><td>122</td><td>199</td><td>116</td><td>32</td></tr><tr><td>100</td><td>205</td><td>210</td><td>23</td><td>0</td></tr></table>

Figure 6. (Color online) Scatterplot of Residual Envy Before and After Adding Clique Cuts in Linear Scale (Left Panel) and Logarithmic Scale (Right Panel)  
![](/api/attachments/KJDKDQ33/fulltext/images/adbd56981d9de5b19ee1f7066f4d58fe6d16958fd2de193b03b69e0d229f71ae.jpg)

Table 3 shows that under PEL, Phase 1 is sufficient to find WE prices in most instances, with 122 of 210 instances resulting in envy-free prices after just Phase 1 under 50% exchange and 205 of 210 instances resulting in envy-free prices after just Phase 1 under 100% exchange. For nonenvy-free instances, residual envy is negligible (\$116 and \$23, respectively) relative to the size of the market. For PAL, on the other hand (i.e., zero cases), Phase 1 results in only 41 envy-free instances, although the amount of envy is still small relative to the size of the market.

Table 3 also shows that clique cuts significantly increase the number of envy-free instances and reduce residual envy. When no exchange is considered, residual envy is completely eliminated by clique cuts in all but one instance. Similarly, under 100% exchange, all instances generate envy-free prices after cuts. For those few instances under 50% exchange where Phase 1 did not result in WE prices, we still find significant improvements in residual envy, eliminating residual envy for an additional 77 instances (122 versus 199) and drastically reducing average residual envy (\$116 versus \$32) in the remaining instances. Figure 6 presents a scatterplot highlighting the magnitude of residual envy before and after adding clique cuts in both linear and logarithmic (base 10) scales. As can be seen, after completing Phase 1, residual envy is relatively negligible under PEL. However, Phase 2 is still able to reduce (and in many cases, eliminate) residual envy for these instances. On the other hand, under PAL, we observe relatively larger residual envy after completing Phase 1, which is eliminated after incorporating the clique-cut generation procedure. In Online Appendix

![](/api/attachments/KJDKDQ33/fulltext/images/a725c2a914e084bc8aef1d200adc459b6f0d9b3ceaac4fa5fc74e5d2ebb0bd33.jpg)  
L, we more closely examine run times and the structure of the clique cuts.

## 5. Concluding Remarks

Designing effective electronic markets is an important field and has gained attention in the management science and information systems research literature over the past few decades. The advancement of commercial mixed-integer programming solvers has made the implementation of combinatorial auctions/exchanges possible, but the design of pricing mechanisms and compactbidding languages remains open to fruitful research for specific real-world applications. Motivated by an application in truckload transportation markets, we propose a novel framework, IDP, that incorporates a compactbidding language to calculate linear anonymous prices that are ɛ-Walrasian equilibrium. Our mechanism is fully efficient for this market, and our numerical experiments highlight that the relative deviation from WE is negligible compared with the benefits collected by the shipper and carriers. To implement such pricing computationally, we demonstrate a dynamic iterative algorithm using an interplay between polynomial and enumerative formulations, an approach that can be tailored to other auction/exchange markets with similar benefits or be extended with additional practical constraints. Our research also highlights how coordination among carriers and shippers can be facilitated by an appropriately designed auction/exchange, unlocking significant efficiency gains that can be seen as money left on the table to be divided fairly among the participants.

Our analyses highlight significant efficiency gains of a centralized system (i.e., using one-shot combinatoria auctions that utilize VCG or IDP pricing) compared with a multiround auction. Our experiments also highlight the well-known shortcomings of VCG prices (Ausubel and Milgrom 2006), particularly in exchange settings, and provide IDP as a more reliable alternative. We show that residual envy can be relatively small for large truckload transportation markets and initiate the use of a straightforward and effective cutting-plane approach blended within our pricing to further reduce such deviations. We believe that our research provides a direction for the optimization community to investigate standardized and computationally efficient cutting-plane methods to calculate ɛ-WE prices while maintaining high levels of interpretability for item prices.

Moreover, although we focus on designing a mechanism to determine prices for a long-term truckload procurement market, our approach could also be adapted for short-term truckload transportation markets (e.g., mini bids) (Caplice 2021). Such short-term markets are proposed to reduce the “load rejection” issue observed in real-time trucking operations when spot-market rates dip below contractual rates. In such cases, the shipper typically finds another carrier through the spot market (Scott et al. 2017). As in the long-term market, mechanisms using expressive bidding (like PAL or PEL) have the potential to mitigate spot-market pressures by allowing combinatorial efficiencies to price them out. Further, our overall approach is flexible enough to be easily combined with other methods, such as a price-index adjustment (Caplice 2021), which adjusts contract prices based on market conditions in real time.

Another possible direction is to tailor our proposed approach for a short-term truckload matching setting. To do so, bids would need to incorporate shipment times, which can be formulated using a time-space network.<sup>6</sup> By mapping the polynomial allocation problem to a time-space network, we expect that our framework could be implemented with only minor modifications.

More broadly, our pricing format could also be tailored to other procurement markets or forward auctions. Exploring stronger cuts blended into iterative pricing is an interesting research direction, especially where the IP relaxation gap in the winner-determination problem may be larger. An important consideration in exploring such cutting-plane approaches is to maintain high levels of interpretability of the identified prices. There are also opportunities to improve the computational efficiency of our proposed mechanism, particularly when the separation problem is more challenging to solve. Heuristic algorithms may be tailored for various procurement settings to make the algorithm faster for larger markets.

Given the extreme computational effort required to compute Bayes–Nash equilibria for the much smaller markets considered by Schneider et al. (2015), Ausubel and Baranov (2020), and Bu¨ nz et al. (2022), a similar exploration of equilibria (both theoretical and experimental) for markets of the current size and structure would be quite challenging but a natural direction for future work. Similarly, a comparison of the manipulability (or mitigation of manipulability) afforded by various bid languages is also a compelling open topic. These remain just a few of many possible open directions in which combinatorial market perspectives might continue to benefit from advanced information systems research.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their constructive comments throughout the review process.

## Endnotes

<sup>1</sup> See https://www.trucking.org/.

<sup>2</sup> See https://www.freightwaves.com/news/what-is-the-differencebetween-trucking-contract-and-spot-rates.

3 <sup>3</sup> See https://www.freightwaves.com/news/freight-companiesbegin-sharing-capacity-data-with-feds.

<sup>4</sup> U{a, b} represents the discrete uniform distribution over integers from a to b.

<sup>5</sup> Note that the reported average relative savings here are slightly different from what is presented in Figure 2 as these results also incor porate instances with strategic-partner and winner-per-lane constraints.

<sup>6</sup> In a time-space network, each node represents a location and a time interval, and solutions represent dispatch time intervals for trucks and shipments (Boland et al. 2017).

## References

Adomavicius G, Gupta A (2005) Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2):169–185.

Adomavicius G, Gupta A, Yang M (2022) Bidder support in multiitem multi-unit continuous combinatorial auctions: A unifying theoretical framework. Inform. Systems Res. 33(4):1174–1195.

Ausubel LM, Baranov O (2020) Core-selecting auctions with incom plete information. Internat. J. Game Theory 49(1):251–273.

Ausubel LM, Milgrom P (2006) The lovely but lonely Vickrey auc tion. Combinatorial Auctions 17:22–26.

Ball MO, Berardino F, Hansen M (2018) The use of auctions for allocating airport access rights. Transportation Res. Part A Policy Practice 114:186–202.

Bedard NC, Goeree JK, Louis P, Zhang J (2020) The favored but flawed simultaneous multiple-round auction. Working Paper Series 2020/03, Economics Discipline Group, UTS Business School, University of Technology, Sydney, Australia.

Ben-David A, Nisan N, Pinkas B (2008) FairplayMP: A system for secure multi-party computation. Proc. 15th ACM Conf. Comput Comm. Security (Association for Computing Machinery, New York), 257–266.

Bichler M (2018) Market Design: A Linear Programming Approach to Auctions and Matching (Cambridge University Press, Cam bridge, UK).

Bichler M, Goeree JK (2017) Handbook of Spectrum Auction Design (Cambridge University Press, Cambridge, UK).

Bichler M, Fux V, Goeree J (2018) A matter of equality: Linear pricing in combinatorial exchanges. Inform. Systems Res. 29(4):1024–1043.

Bichler M, Hao Z, Adomavicius G (2017) Coalition-based pricing in ascending combinatorial auctions. Inform. Systems Res. 28(1): 159–179.

Bichler M, Shabalin P, Pikovsky A (2009) A computational analysis of linear price iterative combinatorial auction formats. Inform. Systems Res. 20(1):33–59.

Bichler M, Shabalin P, Wolf J (2013) Do core-selecting combinatorial clock auctions always lead to high efficiency? An experimental analysis of spectrum auction designs. Experiment. Econom. 16(4):511–545.

Bichler M, Schneider S, Guler K, Sayal M (2011) Compact bidding languages and supplier selection for markets with economies of scale and scope. Eur. J. Oper. Res. 214(1):67–77.

Bikhchandani S, Mamer JW (1997) Competitive equilibrium in an exchange economy with indivisibilities. J. Econom. Theory 74(2): 385–413.

Boland N, Hewitt M, Marshall L, Savelsbergh M (2017) The continuous-time service network design problem. Oper. Res. 65(5):1303–1321.

Boughaci D, Benhamou B, Drias H (2010) Local search methods for the optimal winner determination problem in combinatoria auctions. J. Math. Model. Algorithms 9(2):165–180.

Budish E (2011) The combinatorial assignment problem: Approximate competitive equilibrium from equal incomes. J. Political Econom. 119(6):1061–1103.

Bu¨ nz B, Lubin B, Seuken S (2022) Designing core-selecting payment rules: A computational search approach. Inform. Systems Res. 33(4):1157–1173.

Bykowsky MM, Cull RJ, Ledyard JO (2000) Mutually destructive bidding: The FCC auction design problem. J. Regulatory Econom. 17(3):205–228.

Caplice C (2007) Electronic markets for truckload transportation. Production Oper. Management 16(4):423–436.

Caplice C (2021) Reducing uncertainty in freight transportation procurement. J. Supply Chain Management 4(2):137–155.

Caplice C, Sheffi Y (2006) Combinatorial auctions for truckload transportation. Combinatorial Auctions 21:539–572.

Cavallo R (2006) Optimal decision-making with minimal waste: Strategyproof redistribution of VCG payments. Proc. Fifth Internat. Joint Conf. Autonomous Agents Multiagent Systems (Associa tion for Computing Machinery, New York), 882–889.

Chen H (2016) Combinatorial clock-proxy exchange for carrier collaboration in less than truck load transportation. Transportation Res. Part E Logist. Transportation Rev. 91:152–172.

Chen RLY, AhmadBeygi S, Cohn A, Beil DR, Sinha A (2009) Solving truckload procurement auctions over an exponential number of bundles. Transportation Sci. 43(4):493–510.

Cheng M, Xu SX, Huang GQ (2016) Truthful multi-unit multi attribute double auctions for perishable supply chain trading. Transportation Res. Part E Logist. Transportation Rev. 93:21–37.

Clarke EH (1971) Multipart pricing of public goods. Public Choice 11(1):17–33.

Cramton P, Shoham Y, Steinberg R (2006) Combinatorial Auctions (MIT Press, Cambridge, MA).

Day R (2013) The division of surplus in efficient combinatorial exchanges. Preprint, submitted February 26, https://dx.doi.org/ 10.2139/ssrn.2207067.

Day RW, Cramton P (2012) Quadratic core-selecting payment rules for combinatorial auctions. Oper. Res. 60(3):588–603.

Day RW, Raghavan S (2007) Fair payments for efficient allocations in public sector combinatorial auctions. Management Sci. 53(9): 1389–1406.

Emadikhiav M, Bhattacharjee S, Day R, Bergman D (2024) A decision support framework for integrated lane identification and long-term backhaul collaboration using spatial analytics and optimization. Decision Support Systems 180:114186.

Ergun O, Kuyzu G, Savelsbergh M (2007a) Reducing truckload transportation costs through collaboration. Transportation Sci. 41(2):206–221.

Ergun O<sup>¨</sup> , Kuyzu G, Savelsbergh M (2007b) Shipper collaboration. Comput. Oper. Res. 34(6):1551–1560.

Evans D, Kolesnikov V, Rosulek M (2018) A pragmatic introduction to secure multi-party computation. Foundations Trends Privacy Security 2(2–3):70–246.

Ferna´ndez E, Fontana D, Speranza MG (2016) On the collaboration uncapacitated arc routing problem. Comput. Oper. Res. 67: 120–131.

Garey MR, Johnson DS (2002) Computers and Intractability, vol. 29 (W. H. Freeman, New York).

Goetzendorff A, Bichler M, Shabalin P, Day RW (2015) Compact bid languages and core pricing in large multi-item auctions. Management Sci. 61(7):1684–1703.

Groves T (1973) Incentives in teams. Econometrica 41(4):617–631.

Gu¨ nlu¨ k O, Lada´nyi L, De Vries S (2005) A branch-and-price algorithm and new test problems for spectrum auctions. Management Sci. 51(3):391–406

Gurobi Optimization, LLC (2023) Gurobi Optimizer Gurobi 12.0. Accessed December 1, 2024, https://www.gurobi.com.

Harris A, Nguyen TMA (2022) Long-term relationships and the spot market: Evidence from US trucking. Working paper, Department of Economics, Massachusetts Institute of Technology, Boston.

Harris A, Nguyen TMA (2025) Long-term relationships in the US truckload freight industry. Amer. Econom. J. Microeconom. Forthcoming.

Hoffman K, Menon D (2010) A practical combinatorial clock exchange for spectrum licenses. Decision Anal. 7(1):58–77.

Huang GQ, Xu SX (2013) Truthful multi-unit transportation procurement auctions for logistics e-marketplaces. Transportation Res. Part B Methodological 47:127–148.

Kittsteiner T, Ott M, Steinberg R (2022) Competing combinatorial auctions. Inform. Systems Res. 33(4):1130–1137.

Kuyzu G (2017) Lane covering with partner bounds in collaborative truckload transportation procurement. Comput. Oper. Res. 77: 32–43.

Lahaie S, Lubin B (2019) Adaptive-price combinatorial auctions. EC’19 Proc. 2019 ACM Conf. Econom. Comput. (Association fo Computing Machinery, New York), 749–750.

Liu R, Jiang Z, Fung RY, Chen F, Liu X (2010) Two-phase heuristi algorithms for full truckloads multi-depot capacitated vehicle routing problem in carrier collaboration. Comput. Oper. Res. 37(5):950–959.

Lubin B, Juda AI, Cavallo R, Lahaie S, Shneidman J, Parkes DC (2008) ICE: An expressive iterative combinatorial exchange. J. Artificial Intelligence Res. 33:33–77.

Milgrom PR (2004) Putting Auction Theory to Work (Cambridge Uni versity Press, Cambridge, UK).

Milgrom P, Watt M (2022) Walrasian mechanisms for non-convex economies and the bound-form first welfare theorem. Proc. ACM Conf. Econom. Comput. (Association for Computing Machinery, New York), 300.

Nguyen T, Vohra R (2022) (Near) substitute preferences and equilibria with indivisibilities. Technical Report No. 22-010, Penn Institute for Economic Research, Department of Economics, University of Pennsylvania, Philadelphia.

O<sup>¨</sup> zener OO<sup>¨</sup> , Ergun O<sup>¨</sup> , Savelsbergh M (2011) Lane-exchange mechanisms for truckload carrier collaboration. Transportation Sci. 45(1):1–17.

Parkes DC (2001) Iterative Combinatorial Auctions: Achieving Eco nomic and Computational Efficiency (University of Pennsylvania, Philadelphia).

Parkes DC, Kalagnanam J, Eso M (2001) Achieving budget-balance with Vickrey-based payment schemes in exchanges. Proc. 17th Internat. Joint Conf. Artificial Intelligence—Volume 2 (Morgan Kaufmann Publishers Inc., San Francisco), 1161–1168.

Ray A, Ventresca M, Kannan K (2021) A graph-based ant algorithm for the winner determination problem in combinatorial auctions. Inform. Systems Res. 32(4):1099–1114.

Sandholm T (2002) Algorithm for optimal winner determination in combinatorial auctions. Artificial Intelligence 135(1–2):1–54

Sandholm T (2013) Very-large-scale generalized combinatorial multiattribute auctions. Vulkan N, Roth AE, Neeman Z, eds. The Handbook of Market Design (Oxford University Press, Oxford, UK), 379–412.

Schneider M, Day R, Garfinkel R (2015) Risk aversion and loss aversion in core-selecting auctions. Decision Support Systems 79:161–170.

Scott A (2019) Concurrent business and buyer–supplier behavior in B2B auctions: Evidence from truckload transportation. Production Oper. Management 28(10):2609–2628.

Scott A, Parker C, Craighead CW (2017) Service refusals in supply chains: Drivers and deterrents of freight rejection. Transportation Sci. 51(4):1086–1101.

Sheffi Y (2004) Combinatorial auctions in the procurement of transportation services. Interfaces 34(4):245–252.

Vickrey W (1961) Counterspeculation, auctions, and competitive sealed tenders. J. Finance 16(1):8–37.

Wang J, Shen Y, Wang B (2021) Sealed-bid auction scheme based on blockchain and secure multi-party computation. 2021 IEEE 5th Inform. Tech. Networking Electronic Automation Control Conf. (ITNEC), vol. 5 (IEEE, Piscataway, NJ), 407–412.

Wu Q, Hao JK (2015) Solving the winner determination problem vi a weighted maximum clique heuristic. Expert Systems Appl. 42(1):355–365.

Xu SX, Huang GQ, Cheng M (2017) Truthful, budget-balanced bun dle double auctions for carrier collaboration. Transportation Sci 51(4):1365–1386.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
