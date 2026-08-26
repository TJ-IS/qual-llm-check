---
otero_id: 4162
otero_key: "3DQQYFTD"
title: "A Computational Analysis of Linear Price Iterative Combinatorial Auction Formats"
authors: "Martin Bichler; Pasha Shabalin; Alexander Pikovsky"
year: "2009"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0151"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/3DQQYFTD/fulltext/images/a92cd88fe3f679ac284e714684e6577dd5910726747ac2640b926c2a554f0287.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Computational Analysis of Linear Price Iterative Combinatorial Auction Formats

Martin Bichler, Pasha Shabalin, Alexander Pikovsky,

To cite this article:

Martin Bichler, Pasha Shabalin, Alexander Pikovsky, (2009) A Computational Analysis of Linear Price Iterative Combinatoria Auction Formats. Information Systems Research 20(1):33-59. http://dx.doi.org/10.1287/isre.1070.0151

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2009, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/3DQQYFTD/fulltext/images/c314ea8968ea02cf6fa5a807207683ebcf484636d439a668831d348aa8697387.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Computational Analysis of Linear Price Iterative Combinatorial Auction Formats

Martin Bichler, Pasha Shabalin, Alexander Pikovsky Department of Informatics, Technische Universität München, 85748 Garching, Germany {bichler@in.tum.de, shabalin@in.tum.de, pikovsky@mytum.de}

terative combinatorial auctions (ICAs) are IT-based economic mechanisms where bidders submit bundle bids Iin a sequence and an auctioneer computes allocations and ask prices in each auction round. The literature in this field provides equilibrium analysis for ICAs with nonlinear personalized prices under strong assumptions on bidders’ strategies. Linear pricing has performed very well in the lab and in the field. In this paper, we com pare three selected linear price ICA formats based on allocative efficiency and revenue distribution using different bidding strategies and bidder valuations. The goal of this research is to benchmark different ICA formats and design and analyze new auction rules for auctions with pseudodual linear prices. The multi-item and discrete nature of linear price iterative combinatorial auctions and the complex price calculation schemes defy much of the traditional game theoretical analysis in this field. Computational methods can be of great help in exploring potential auction designs and analyzing the virtues of various design options. In our simulations, we found that ICA designs with linear prices performed very well for different valuation models even in cases of high synergies among the valuations. There were, however, significant differences in efficiency and in the revenue distributions of the three ICA formats. Heuristic bidding strategies using only a few of the best bundles also led to high levels of efficiency. We have also identified a number of auction rules for ask price calculation and auction termination that have shown to perform very well in the simulations.

Key words: iterative combinatorial auction; pseudodual prices; allocative efficiency; computational experiment History: Paulo Goes, Senior Editor; Alok Gupta, Associate Editor. This paper was received on June 13, 2006, and was with the authors 5 <sup>1</sup><sub>2</sub> months for 2 revisions. Published online in Articles in Advance June 5, 2008.

## 1. Introduction

Multi-item auctions are common in industrial procurement and logistics, where suppliers are able to satisfy the buyer’s demand for several items or lanes. Purchasing managers often package these items into predefined bundles that the suppliers can bid on Schoenherr and Mabert (2006). Throughout the past few years, the study of combinatorial auctions (CAs) has received much academic attention (Anandalingam et al. 2005, Cramton et al. 2006). CAs are multi-item auctions, where bidders can define their own combinations of items called “packages” or “bundles,” and place bids on them rather than just on individual items or bundles that are predefined by the auctioneer. This allows the bidders to better express their valuations and ultimately increases economic efficiency in the presence of synergistic values, often called economies of scope. CAs have already found application in various domains ranging from transportation to industrial procurement and allocation of spectrum licenses for wireless communication services (Cramton et al. 2006).

## 1.1. Information Systems for Iterative Combinatorial Auctions

In comparison to single-round, sealed-bid designs, multiround or iterative CAs (ICAs) have been selected in a number of industrial applications, because they help bidders to express their preferences by providing feedback such as provisional pricing and allocation information in each round (Cramton 1998, Bichler et al. 2006). ICAs have several advantages over sealed-bid auctions. First, bidders do not have to reveal their true preferences on all possible bundles in one round as would be necessary in Vickrey-Clarke-Groves (VCG) mechanisms (Ausubel and Milgrom 2006b). Second, prices and other feedback received by bidders in ICAs help to reduce the amount of potentially interesting bundles. Third, Milgrom and Weber (1982) have shown for single-item auctions that if there is affiliation in the values of bidders, then sealed-bid auctions are less efficient than iterative auctions. Even in cases where sealed-bid CAs have been used, people have decided to run after-market negotiations to overcome inefficiencies (Elmaghraby and Keskinocak 2002).

Iterative combinatorial auctions would not be possible without IT-based auction platforms solving hard computational problems in each auction round, most notably the winner determination problem and the calculation of feedback prices. This is also a reason why combinatorial auctions have been a topic in much recent Information Systems research (see, for example, Adomavicius and Gupta 2005, Jones and Koehler 2005, Xia et al. 2004, Fan et al. 2003, Kelly and Steinberg 2000).

Much research on ICAs is based on so-called primal-dual auction algorithms. In their seminal paper, Bikhchandani and Ostroy (2002) use dual information based on results of a winner determination integer program as ask prices in an ICA. The solution to the LP relaxation of the winner determination problem (WDP) suggested in their paper is integral and the ask prices will lead to competitive equilibrium, maximizing allocative efficiency. Unfortunately, they need to introduce a variable for every feasible integer solution so that the number of variables needed for the WDP is exponential in the number of bids. The formulation then results in discriminatory nonlinear ask prices and is not a feasible approach for larger combinatorial auctions (see Bikhchandani and Ostroy 2002, §2.1). Nevertheless, the paper provided very useful insights for practical auction designs. There have been multiple proposals on how to design ICAs including approximate linear, nonlinear, and discriminatory nonlinear prices (Kelly and Steinberg 2000, Wurman and Wellman 2000, Parkes and Ungar 2000, Porter et al. 2003, Day 2004, Ausubel and Milgrom 2002, Kwasnica et al. 2005, Kwon et al. 2005, Drexl et al. 2005). As of now, there is no general consensus on a single “best” design, and it seems that several auction formats will prove useful for different applications and different types of valuations.

We focus on the ICA designs with linear ask prices, where each item in the auction is assigned an individual ask price and the price of a package of items is simply the sum of the single-item prices. Although it can be shown that exact linear prices are only possible in restricted cases (Kelso and Crawford 1982), several authors approximate these prices with so-called pseudodual linear prices (Rassenti et al. 1982, Kwasnica et al. 2005, Kwon et al. 2005). Such prices are easy to understand for bidders in comparison to the nonlinear ask prices, where the number of prices to communicate in each round is exponential in the number of items (Xia et al. 2004). Linear prices give good guidance to the bid formation for new entrants and for losing bidders, who can use them to compute the price of any bundle even if no bids were submitted for it so far. Pseudodual prices have been shown to perform surprisingly well in laboratory experiments, and even the U.S. Federal Communications Commission (FCC) has examined their use (FCC 2002). Unfortunately, as of now, there is little theory about the economic properties of ICAs using pseudodual linear ask prices, and initial evidence is restricted to a few laboratory experiments testing selected auction designs and treatment variables.

## 1.2. Research Goals and Methodology

In this paper, we use computational experiments as a tool to compare the relative performance of three selected auction designs primarily based on allocative efficiency and revenue distribution, and several other characteristics including price monotonicity and speed of convergence. The main goal of our research is to evaluate ICA designs and elicit auction rules that work well with a wide range of bidder valuations and bidding strategies. Ultimately, we expect to see the evolution of standard software components and standard designs for combinatorial auctions that work well in a wide variety of bidder valuations and bidding strategies.

Traditionally, laboratory experiments and game theory have been used to analyze bidding in single-item auctions. Equilibrium analysis has been performed for so-called primal-dual auctions with nonlinear prices (see §2.1), but not for ICAs with pseudodual linear prices. Computing equilibria of combinatorial auctions is hard because the space of bidding strategies can be very large (Anandalingam et al. 2005, Sureka and Wurman 2005). Various ask price calculation schemes, bidder decision support tools, eligibility, and bid increment rules make it extremely complex to admit much theoretical analysis at a greater level of detail. On the other hand, laboratory experiments are costly and are typically restricted to relatively few treatment variables. Computational experiments can be of great help in exploring potential auction designs and analyzing the virtues of various design options.

We focus on three promising auction designs— the combinatorial clock (CC) auction, the resource allocation design (RAD), and the approximate linear prices (ALPS) with its modified version ALPSm, which extends RAD—and analyze their performance in discrete event simulations. In the first set of simulations, we do not try to emulate real-world bidding behavior but use myopic bestResponse bidders and simple powerSet bidders (see §3.2). This enables us to compare different ICA designs and estimate the efficiency loss that can be attributed to different auction rules and not to the bidding strategies.

In the second set of simulations, we analyze the impact of different bidding strategies on the auction outcome. This analysis is relevant because real-world bidders typically do not follow powerSet or myopic best response bidding strategies, but use different types of bundling heuristics. Due to the $2 ^ { k } - 1$ packages a bidder must decide on, it may simply be impractical for bidders to consider or even know valuations for the full range of relevant packages on which to bid. Our analysis is based on different bundling strategies and bidder valuation models in order to achieve more general results.

The paper is organized as follows. In §2 we provide an overview of ICAs and describe the relevant terms and concepts. Section 3 describes the simulation framework, the model parameters, and the performance measures. In §4 we discuss the numerical results of simulations with myopic best response bidders. Section 5 analyzes the impact of different bidding strategies. Finally, in §6 we draw conclusions and provide an outlook on future research.

Appendices A, B, and C provide a detailed description of the ALPS and ALPSm auction formats. The accompanying website (http://ibis.in.tum.de/ marketdesigner/ISR/) contains all simulation results, including those omitted from the print version for space reasons.

## 2. Iterative Combinatorial Auctions

In this section, we provide an overview of iterative or, more precisely, “ascending” combinatorial auctions and describe the relevant concepts and terms. We refer the reader to Parkes (2006) for a detailed introduction to iterative combinatorial auctions (ICAs). We first introduce some necessary notation. Let $\mathcal { K } =$ $\{ 1 , \ldots , m \}$ denote the set of items indexed by $k ,$ and ${ \mathcal { I } } = \left\{ 1 , \ldots , n \right\}$ denote the set of bidders indexed by i with private valuations $v _ { i } ( S ) \geq 0$ for bundles $S \subseteq { \mathcal { K } }$ This means, each bidder i has a valuation function v<sub>i</sub> $2 ^ { \mathcal { K } }  \mathbb { R } _ { 0 } ^ { + }$ that attaches a value $v _ { i } ( S )$ to any bundle $S \subseteq { \mathcal { K } }$ . In addition, we assume values $v _ { i } ( S )$ to be independent and private, and the bidders’ utility function to be quasilinear $( \pi _ { i } ( S ) = v _ { i } ( S ) - p )$ with free disposal, i.e., if $S \subset T ,$ , then $v _ { i } ( S ) \leq v _ { i } ( T )$ . A typical auction design goal is to obtain an efficient allocation $X ^ { * } = ( S _ { 1 } ^ { * } , \ldots , S _ { n } ^ { * } )$ , where $S _ { i } ^ { * }$ is bidder $i ^ { \prime } \mathrm { s }$ optimal bundle. Given the private bidder valuations for all possible bundles, the efficient allocation can be found by solving the combinatorial allocation problem (CAP) (also called the winner determination problem (WDP)). It is well-known that CAP can be interpreted as a weighted set packing problem (SPP) (Lehmann et al. 2006). CAP has a straightforward integer programming formulation using the binary decision variables $x _ { i } ( S )$ which indicate whether the bid of the bidder i for the bundle S belongs to the allocation:

$$
\begin{array}{l} \max _ {x _ {i} (S)} \sum_ {S \subseteq \mathcal {K}} \sum_ {i \in \mathcal {I}} x _ {i} (S) v _ {i} (S) \\ \text {s.t.} \sum_ {S \subseteq \mathcal {K}} x _ {i} (S) \leq 1 \quad \forall   i \in \mathcal {I} \\ \sum_ {S: k \in S} \sum_ {i \in \mathcal {I}} x _ {i} (S) \leq 1 \quad \forall   k \in \mathcal {K} \\ x _ {i} (S) \in \{0, 1 \} \quad \forall   i, S. \end{array}\tag{CAP}
$$

The formulation CAP is NP-hard if bidders are limited to submitting a number of bundle bids that is less than some polynomial function of m. When bids are submitted on all bundles, Rothkopf et al. (1998) provide a polynomial algorithm for CAP with an OR language. The solution $X ^ { \ast }$ is a combination of bundles which maximizes the total valuation. The first set of constraints guarantees that any bidder can win at most one bundle, which is only relevant for XOR bidding. Without these constraints, the auctioneer would allow additive-OR bids. The second set of constraints ensures that each item is only allocated once. The CAP has been attracting intense research efforts. For example, polynomial-time algorithms for restricted cases of CAP have been suggested in Rothkopf et al.

(1998) and Carlsson and Andersson (2007). However, the package bidding nature of CAs also leads to a number of additional problems in the auction design.

Bidding in combinatorial auctions is complex. The preference elicitation problem (PEP) includes the valuation problem, i.e., the selection and valuation of bundles to bid on from an exponential set of possible bundles. In addition, the strategy problem of determining optimal bid prices in various auction designs has been a main focus in the classic game-theoretic auction research but turns out to be an even more difficult problem in ICAs. For example, it is possible that a losing bid in an ICA becomes a winning bid in a subsequent round without changing the bid. The bidder faces the problem of choosing appropriate bundles to bid on $( \mathrm { i . e . , }$ bundle selection) and, if the format allows, determining a bid price. Communication complexity is related to PEP and deals with the question of how many valuations need to be transferred to the auctioneer in order for him to calculate an efficient allocation. Nisan (2000) shows that an exponential communication is required. This problem might be addressed by designing careful bidding languages that allow for compact representation of the bidder’s preferences. In addition, there is much recent research on preference elicitation in combinatorial auctions through querying, which can provide an alternative to ICAs that are discussed in this paper (Sandholm and Boutilier 2006).

PEP “has emerged as perhaps the key bottleneck in the real-world application of combinatorial auctions. Advanced clearing algorithms are worthless if one cannot simplify the bidding problem facing bidders” (Parkes 2006). ICAs are (to date) the most promising way of addressing the PEP. “Experience in both the field and laboratory suggest that in complex economic environments iterative auctions, which enhance the ability of the participant to detect keen competition and learn when and how high to bid, produce better results than sealed bid auctions” (Porter et al. 2003). In contrast, sealed-bid auctions require bidders to determine and report their valuations up-front.

## 2.1. Pricing in ICAs

The typical bidding process in an ICA consists of the steps of bid submission and bid evaluation (a.k.a. winner determination, market clearing, or resource allocation) followed by some feedback to the bidders (see Figure 1). The feedback is typically given in the form of ask prices for the next round and some information on the provisionally winning allocation. These prices are used not only to provide valuation information to bidders but also to set a minimum bid amount for the next round. Because of computational requirements, ICA designs are usually round based rather than continuous. The auctions close either at a fixed point in time or after a certain stopping condition is satisfied (e.g., no new bids were submitted). The competitive process of auctions serves to aggregate the dispersed information about bidders’ valuations and to dynamically set the prices of a trade.

Figure 1 Process of an Iterative Combinatorial Auction  
![](/api/attachments/3DQQYFTD/fulltext/images/ae91c225eb0912a767156d5b62c6dac81305f34743cfecb75d1aaf2188f69d8b.jpg)

Let $t = 1 , 2 , 3 , \ldots$  denote the current auction round and B<sup>t</sup> be the set of all bids submitted in the round t with $b \in B ^ { t }$ denoting a single bid. A bid $b = b _ { i } ( S )$ represents the bid price submitted by the bidder i on the bundle S. Furthermore, for the current provisional allocation $X ^ { t } .$ , let $W ^ { t } \subseteq B ^ { t }$ and $L ^ { t } \subset B ^ { t }$ be the currently provisionally winning bids and the provisionally losing bids, respectively, with $W ^ { t } \cap L ^ { t } = \emptyset ,$ $W ^ { t } \cup L ^ { t } = B ^ { t }$ . In other words, $b = b _ { i } ( S ) \in W ^ { t } \Leftrightarrow$ $x _ { i } ( S ) = 1$ . In the following, we will omit the round index t with $B , W , L , X$ indicating the provisional allocation in the current round t and with  the prices to be calculated for the next round t 1.

Different pricing schemes have been discussed in the literature including linear, nonlinear, and nonlinear, nonanonymous prices (see Xia et al. 2004 for a detailed discussion):

Definition 1. A set of prices $p _ { i } ( S ) , i \in \mathcal { I } , S \subseteq \mathcal { K }$ is called:

• linear (or additive), if

$$
\forall i, \quad S \colon p _ {i} (S) = \sum_ {k \in S} p _ {i} (k)
$$

• anonymous, if

$$
\forall i \neq j, S \colon p _ {i} (S) = p _ {j} (S).
$$

In other words, prices are linear if the price of a bundle is equal to the sum of prices of its items, and prices are anonymous if prices of the same bundle are equal for every bidder. Nonanonymous ask prices are also called discriminatory prices. By combining these notions, the following four sets of ask prices can be discussed:

1. a set of linear anonymous prices $\mathcal { P } = \{ p ( k ) \}$

2. a set of linear discriminatory prices ${ \mathcal { P } } = \{ p _ { i } ( k ) \}$

3. a set of nonlinear anonymous prices ${ \mathcal { P } } = \{ p ( S ) \}$ 

4. a set of nonlinear discriminatory prices ${ \mathcal { P } } =$ $\{ p _ { i } ( S ) \}$

For a bidder i, a set of prices ${ \mathcal { P } } ,$ and a bundle $S ,$ let $\pi _ { i } ( S , { \mathcal { P } } ) = v _ { i } ( S ) - p _ { i } ( S )$ denote the bidder’s payoff and $\begin{array} { r } { \Pi ( S , { \mathcal P } ) = \sum _ { k \in S } p _ { i } ( S ) } \end{array}$ denote the auctioneer’s revenue on the bundle S at the prices . In addition, let  denote the set of all possible allocations with allocation $X = ( S _ { 1 } , \ldots , S _ { n } ) , X \in \Gamma ,$ , and the optimal allocation $X ^ { \ast } \in \Gamma$ . Equilibrium theory is often used as a guideline for constructing efficient price-based auction designs.

Definition 2 (Competitive Equilibrium (CE)). Prices $\mathcal { P }$ and allocation $X ^ { * } = ( S _ { 1 } ^ { * } , \ldots , S _ { n } ^ { * } )$ are in competitive equilibrium if:

$$
\begin{array}{c} \pi_ {i} (S _ {i} ^ {*}, \mathcal {P}) = \max _ {S \subseteq \mathcal {K}} [ v _ {i} (S) - p _ {i} (S), 0 ] \quad \forall   i \in \mathcal {I} \\ \Pi (X ^ {*}, \mathcal {P}) = \max _ {X \in \Gamma} \sum_ {i \in \mathcal {I}} p _ {i} (S _ {i}). \end{array}
$$

In CE, the payoff of every bidder (and the auctioneer) is maximized at the given prices and the auction will effectively end because bidders will not want to change the allocation by submitting any further bids.

In their seminal paper, Bikhchandani and Ostroy (2006) show that $X ^ { \ast }$ is supported in CE by some set of prices  if and only if $X ^ { \ast }$ is an efficient allocation. This allows for construction of ICAs that update prices in the direction of CE prices until there are no new bids. Such an ICA will converge to a minimal CE price set. Generating minimal CE prices is a desirable property because it usually imposes incentive compatibility of the auction design. Termination with CE prices that support VCG payments brings straightforward bidding into an ex post equilibrium (Parkes 2006).

Definition 3 (Minimal CE Prices). Minimal CE prices minimize the auctioneer revenue $\Pi _ { S } ( X ^ { * } , { \mathcal { P } } )$ on the efficient allocation $X ^ { \ast }$ across all CE prices.

Given the LP relaxation of the CAP, we can derive minimal CE prices by solving the dual problem:

$$
\begin{array}{l l} \underset {p (i), p (k)} {\min} & \sum_ {i} p (i) + \sum_ {k} p (k) \\ \text {s.t.} & p (i) + \sum_ {k \in S} p (k) \geq v _ {i} (S) \quad \forall   i, S \\ & p (i), p (k) \geq 0 \quad \forall   i, k. \end{array}\tag{CAP-DLP}
$$

The values of the dual variables quantify the monetary cost of not awarding the item to whom it has been provisionally assigned. This means that the dual variables $p ( k )$ can be interpreted as anonymous linear prices; the term $\textstyle \sum _ { k \in S } p ( k )$ is then the price of the bundle S and $p ( i ) : = \operatorname* { m a x } _ { S } \{ v _ { i } ( S ) - \textstyle \sum _ { k \in S } p ( k ) \}$ is the maximal utility of the bidder i at the prices $p ( k )$

A Walrasian equilibrium is described as a vector of such item prices for which all the items are sold, when each bidder receives a bundle in his demand set. Unfortunately, CAP is a binary program, i.e., a nonconvex optimization problem, where the dual prices will overestimate the true item values. Simple examples illustrate that linear anonymous CE prices do not exist for a general CA where goods are indivisible; in other words, for certain types of bidder valuations it is impossible to find linear prices which support the efficient allocation X∗ (Pikovsky and Bichler 2005). Kelso and Crawford (1982) show that the goods are substitutes property (also named gross substitutes property) is a sufficient and an almost necessary condition for the existence of the exact linear CE prices. Intuitively, the property implies that the bidder will continue to demand the items which do not change in price, even if the prices on other items increase. However, the goods are substitutes condition is very restrictive as most known practical applications of combinatorial auctions deal rather with complementary goods.

By adding additional constraints for each set partition of items and each bidder to CAP, the formulation can be strengthened so that nonlinear and nonanonymous prices can be derived from the respective dual problem. Such a formulation describes every feasible solution to an integer problem and is solvable with linear programming resulting in discriminatory nonlinear CE prices (Bikhchandani and Ostroy

2002). Although such prices do always exist, such an approach is not practical for larger CAs.

Several ICA designs attempt to result in VCG payments. Minimal CE prices and VCG payments typically differ. Bikhchandani and Ostroy (2002) show that the bidders are substitutes condition (BSC) is necessary and sufficient to support VCG payments in competitive equilibrium.

Definition 4 (Bidders are Substitutes Condition). Let $w ( \mathcal { I } )$ represent the value of CAP. For any subset of bidders $L \subseteq { \mathcal { I } } ,$ let $w ( L )$ denote the coalitional value for $L ,$ equal to the value of the efficient allocation for $\mathrm { C A P } ( L )$ . This amount would be the social surplus if only the bidders in L were present. The bidders are substitutes condition requires:

$$
w (\mathcal {I}) - w (\mathcal {I} \setminus L) \geq \sum_ {i \in L} [ w (\mathcal {I}) - w (\mathcal {I} \setminus i) ], \quad \forall L \subseteq \mathcal {I}.
$$

If BSC fails, the VCG payments are not supported in any price equilibrium and truthful bidding is not an equilibrium strategy. A bidder’s payment in the VCG mechanism is always less than or equal to the payment by a bidder at any CE price. Also, BSC is not sufficient for an ascending auction to terminate with VCG prices and Ausubel and Milgrom (2006a) show that it requires the slightly stronger bidder submodularity condition (BSM) for an ascending proxy auction to implement VCG payments.

Definition 5 (Bidder Submodularity Condition). BSM requires that for all $L \subseteq L ^ { \prime } \subseteq \mathcal { F }$ and all $i \in { \mathcal { I } } ,$ there is

$$
w (L \cup \{i \}) - w (L) \geq w (L ^ {\prime} \cup \{i \}) - w (L ^ {\prime}).
$$

Also, de Vries et al. (2007) show that under BSM their primal-dual auction yields VCG payments. When the BSM condition does not hold, the property breaks down and a myopic best-response strategy is likely to lead a bidder to pay more than the optimal price for the winning package (Dunford et al. 2007). Some recent ICA designs extend the notion of ascending auctions to achieve VCG payments for general valuations (see §2.2).

Although the arguments for primal-dual auctions are compelling, there are also a number of problems: Primal-dual auctions elicit all valuations of all losing bidders. This can result in an enormous number of auction rounds, as our own and other experiments have shown (Dunford et al. 2007). Also, BSC can often fail in realistic settings for CAs (Parkes 2001, Chapter 7). de Vries et al. (2007) show that when at least one bidder has a nonsubstitutes valuation, an ascending CA cannot implement the VCG outcome. In these cases, VCG payments are not supported in any price equilibrium and truthful bidding is not an equilibrium strategy (Parkes 2006). The performance of primal-dual auction designs for general valuations and nonmyopic bidding strategies is unknown. Our own experiments have shown that with heuristic bidding behavior (e.g., bidders randomly selecting 3 out of the 10 best bundles in each round) the efficiency of primal-dual auctions can be very low, while linear price auctions are robust against these and other bundle bidding strategies.

Both the large number of auction rounds and the need for a best-response bidding strategy require a proxy agent. All valuations need to be provided to the proxy agent up front or throughout the auction, which needs to be hosted by a trusted third party, something that can be a considerable disadvantage in many settings. Also, the use of discriminatory prices might be perceived as unfair by bidders.

Although the existence of exact linear CE prices is limited, there are several proposals for auction designs with linear prices. Currently, no formal equilibrium analysis for such prices exists, but they exhibit a number of very useful properties and have performed well in the lab:

• Linear prices are easy to understand for the bidders. Simplicity of the feedback given to bidders is very important in many practical application domains.

• Only a linear number of prices has to be communicated in each round.

• One can use linear prices to compute the value of any other bundle, even if no bid was submitted for this bundle in previous rounds (Kwon et al. 2005). This gives bidders an indication of which items and bundles will be expensive and where there is little competition.

• Overall, dual prices in linear programming are only valid within bounds under ceteris paribus conditions, when no new bids are submitted. A single new bid can completely change the allocation, and previously losing bids may become winning bids. Therefore, such pricing information is best viewed as a guideline for bidders, informing them about what it would take for a bid to have some possibility of winning in the next round.

• Problems of approximate linear prices occur when ask prices are below the last bid price of a bidder. While this can be confusing, if ask prices are viewed as a guideline and minimum bid, this does not necessarily have to impact efficiency of the auction.

These arguments motivate further analysis of auction designs with pseudodual prices.

## 2.2. ICA Designs

In the following, we briefly introduce a few of the iterative combinatorial auction designs.

The combinatorial clock auction (CC auction) proposed in Porter et al. (2003) utilizes anonymous linear prices called item clock prices. In each round, bidders express the quantities desired on the packages at the current prices. As long as demand exceeds supply for at least one item (each item is counted only once for each bidder), the price clock “ticks” upward for those items (the item prices are increased by a fixed price increment) and the auction moves on to the next round. If there is no excess demand and no excess supply, the items are allocated corresponding to the last round’s bids and the auction terminates. If there is no excess demand but there is excess supply (all active bidders on an item did not resubmit their bids in the last round), the auctioneer solves the winner determination problem while considering all bids submitted during the auction run time. If the computed allocation does not displace any active last iteration bids, the auction terminates with this allocation; otherwise, the prices of the respective items are increased and the auction continues.

The resource allocation design (RAD) proposed in Kwasnica et al. (2005) also uses anonymous linear ask prices. However, instead of increasing the prices directly, the auction lets the bidders submit priced bids and calculates so-called pseudodual prices based on the LP relaxation of the CAP (Rassenti et al. 1982). The dual price of each item measures the cost of not awarding the item to whom it has been allocated in the last round. Unless the LP relaxation is integral, RAD uses a restricted dual formulation to derive approximate or pseudodual prices after each auction round. In the next round, the losing bidders have to bid more than the sum of ask prices for a desired bundle plus a fixed minimum increment.

RAD suggests OR bidding language and winning bids remain in the auction in its original design. In our work, we have enforced all the original RAD rules but used an XOR bidding language (see §2) in order to be able to use the same bidding agents in all auction formats and thus be able to better compare the results. Furthermore, OR bid language makes the bidding strategy more complex because of the exposure problem when a bidder wins several bids and receives items with subadditive valuations. In an XOR bidding language, only one of the bidder’s bids can be a winning bid.

Because prices may sometimes fall, the auction termination relies on additional eligibility rules as defined in the simultaneous multiround auction (SMR) (Cramton et al. 1998). Most notably, a bidder is not allowed to bid on an increasing number of items in subsequent rounds. Some of the newer FCC auction designs are based in part on RAD (FCC 2002).

In addition to ascending combinatorial auctions based on linear ask prices, several authors have proposed designs based on nonlinear, nonanonymous prices. The ascending proxy auction has been proposed in the context of the FCC spectrum auction design (Ausubel and Milgrom 2006a). The ascending proxy auction uses nonanonymous and nonlinear prices and is similar to the iBundle design by Parkes (Parkes 2001), although Ausubel and Milgrom (2006a) emphasize proxy agents which essentially lead to a sealedbid auction format. Both designs achieve an efficient outcome with minimal CE prices and VCG payments when the BSM condition is satisfied. The dVSV auction design by de Vries et al. (2007) is also similar to iBundle but differs in the price update rule, which only increases prices on the set of minimally undersupplied bidders.

de Vries et al. (2007) also show that there cannot be an ascending combinatorial auction with VCG outcomes for private valuation models without restrictions. Newer approaches such as the one by Mishra and Parkes (2007) try to overcome this negative result by extending the definition of ascending price auctions, e.g., by multiple price paths or discounts on the quoted bid prices upon termination. Most problems discussed in the previous section on primal-dual auctions, however, remain. In addition, VCG outcomes are not in the core for general valuations.

An interesting auction design that combines a linear price ICA and a nonlinear price ICA is the clockproxy auction (Ausubel et al. 2006). It extends the CC auction by a last and final ascending proxy auction round. The approach combines the simple and transparent price discovery mechanism of the CC auction with the efficiency of the ascending proxy auction. Linear pricing is used during the clock phase for price discovery but is then abandoned in the last proxy round to improve the auction efficiency. In the proxy round, bidders specify their final valuations for all packages they still want to purchase, whereas the valuations must be higher than the final prices of the clock phase. We did not specifically consider this auction format in our analysis because it uses nonlinear prices in the second phase, and bidding strategies of bidders in such an auction are theoretically less understood. However, the comparison of linear price formats might propose alternatives to the CC auction in the first phase of the clock-proxy auction.

## 2.3. Approximate Linear PriceS (ALPS)

In our analysis, we focus on auctions with linear prices. In this section, we introduce ALPS with its modification ALPSm, an ICA design that is largely based on, but extends, the original RAD design. Detailed descriptions of the ALPS and ALPSm auction formats can be found in Appendices A, B, and C.

The strength of RAD lies in its simplicity and flexibility for bidders. The ask prices serve as a guideline for bidders to discover new and interesting bundles and allow submission of bid prices. Linear prices are straightforward to use and intuitive, even for novice bidders. However, RAD also faces a few design problems. Most importantly, the eligibility and termination rules can lead to premature termination and inefficiencies. Also, there are ways to further decrease the ask prices. ALPS is an ICA design that is based on pseudodual prices such as RAD, but contains a number of modifications:

Calculation of Linear Ask Prices. ALPS calculates pseudodual prices but modifies the rules specified in RAD to better minimize and balance prices and slack variables. We found this to have a modest but positive impact on efficiency.

Termination Rule. The termination rule has been adapted because it is a potential cause of inefficiency in RAD. An auction terminates if there are no new bids submitted in the last round. To ensure auction progress, the ALPS design increases prices if the provisional allocation does not change in two consecutive rounds. In ALPSm, every bidder has to outbid his old bids in previous rounds on the same bundle.

Surplus Eligibility. Many auction scenarios suffer from the problem that the RAD eligibility rule does not allow for an increase in the number of distinct items on which a bidder is bidding. In particular, in transportation it can become beneficial to bid on a longer route during the course of an auction. We have modified RAD’s eligibility rule to allow active bidders to also increase the number of items to bid on.

A detailed description of the ask price calculation, the termination rule, and the surplus eligibility rule in ALPS can be found in the Appendices A, B, and C. ALPS is based on an XOR bidding language, which we have also used in the RAD and the CC auction implementations in our simulation. In addition to the above rule, we found the “active bid rule” to have a significant effect on the auction outcome.

Active Bid Rule. Typically, only the winning bids W <sup>t</sup> of the last auction round remain active in the subsequent round. In a modified version of ALPS, called ALPSm, all bids submitted in an auction remain active even if they are losing bids, which has shown to provide a significant positive effect on efficiency.

We have also experimented with the last and final bid rule as described by Parkes (2001) and with a minimum bid increment on bundles, but could not find a positive impact on efficiency in the experiments.

## 3. Setup of the Computational Experiments

We developed a software framework for the simulation of ICAs which consists of three main components. A value model defines valuations of all bundles for each bidder. A bidding agent implements a bidding strategy adhering to the given value model and to the restrictions of the specific auction design. An auction processor implements the auction logic, enforces auction protocol rules, and calculates allocations and ask prices. At the same time, these software components implement different treatment variables in our numerical simulations. Different implementations of value models, bidding agents $( \mathrm { i . e . , }$ strategies), and auction processors can be combined which allows performing sensitivity analysis by running a set of simulations while changing only one component and preserving all other parameters. For the comparison of auction formats, we use a set of performance measures, specifically, allocative efficiency, revenue distribution, price monotonicity, and speed of convergence measured by number of auction rounds.

## 3.1. Value Model

The type of bidder valuations is an important treatment variable for the analysis of different auction formats (see §2.1). Performance of an auction format can significantly depend on properties of the valuations, particularly on the BSC and BSM condition, which often do not hold in practical settings. Because there are hardly any real-world combinational auctions data sets available, we have adopted the combinatorial auctions test suite (CATS) value models that have been widely used for the evaluation of winner determination algorithms (Leyton-Brown et al. 2000).

In the following, we will describe a value model as a function that generates realistic, economically motivated combinatorial valuations on all possible bundles for all bidders. For example, a transportation network, real estate lots, or airport slot occupancy timetable provide the underlying rationale. In addition to CATS value models, we have used the pairwise synergy value model from An et al. (2005). In all models, we assume free disposal, i.e., bidders can discard additional items at a price of zero.

The transportation value model uses the paths in space model from the CATS in Leyton-Brown et al. (2000). It models a nearly planar transportation graph in Cartesian coordinates, where each bidder is interested in securing a path between two randomly selected vertices (cities). The items traded are edges (routes) of the graph. Parameters for the transportation value model are the number of items (edges) m and graph density $\rho ,$ which defines an average number of edges per city, and is used to calculate the number of vertices as $( m * 2 ) / \rho .$ . The bidder’s valuation for a path is defined by the Euclidean distance between two nodes multiplied by a random number, drawn from a uniform distribution. Consequently, only a limited number of bundles, which represent paths between both selected cities, are valuable for the bidder. This allows us to consider even larger transportation networks in a reasonable time.

The pairwise synergy value model in An et al. (2005) is defined by a set of valuations of individual items $\{ v _ { k } \}$ with $k \in \mathcal { K }$ and a matrix of pairwise item synergies $\{ s y n _ { k , l } \colon k , l \in \mathcal { K } , s y n _ { k , l } = s y n _ { l , k } , s y n _ { k , k } = 0 \}$ The valuation of a bundle S is then calculated as:

$$
v (S) = \sum_ {k = 1} ^ {| S |} v _ {k} + \frac {1}{| S | - 1} \sum_ {k = 1} ^ {| S |} \sum_ {l = k + 1} ^ {| S |} s y n _ {k, l} (v _ {k} + v _ {l}).
$$

A synergy value of zero corresponds to completely independent items, and the synergy value of one means that the bundle valuation is twice as high as the sum of the individual item valuations. The relevant parameters for the pairwise synergy value model are the interval for the randomly generated item valuations and the interval for the randomly generated synergy values.

The matching value model is an implementation of the matching scenario in CATS. It models the four largest U.S. airports, each having a predefined number of departure and arrival time slots. For simplicity, there is only one slot for each time unit available. Each bidder is interested in obtaining one departure and one arrival slot (i.e., item) in two randomly selected airports. His valuation is proportional to the distance between the airports and reaches maximum when the arrival time matches a certain randomly selected value. The valuation is reduced if the arrival time deviates from this ideal value, or if the time between departure and arrival slots is longer than necessary.

The real estate value model is based on the proximity in space model from the CATS in Leyton-Brown et al. (2000). Items sold in the auction are the real estate lots $k ,$ which have valuations $v _ { k }$ drawn from the same normal distribution for each bidder. Adjacency relationships between two pieces of land l and m $( e _ { l m } )$ are created randomly for all bidders. Edge weights $w _ { l m } \in$ 0 1 are then generated randomly for each bidder, and they are used to determine bundle valuations of adjacent pieces of land:

$$
v (S) = \left(1 + \sum_ {e _ {l m}: l, m \in S} w _ {l m}\right) \sum_ {k \in S} v _ {k}.
$$

## 3.2. Bidding Agents

A bidding agent implements a bidding strategy adhering to the given value model and to the restrictions of the specific auction design. In these simulations, we consider six different agent behaviors. Some of them represent extreme cases of a completely bundleunaware (naïve) bidder and intelligent bidders who evaluate all possible bundles (bestResponse and power-Set). Other agents implement some bundle selection heuristics which might more closely resemble real bidders.

The naïve bidder is the first extreme case and represents a bidder who does not use bundle bids at all. A naïve bidder submits in each round singleton bids only for those items that would provide positive utility, given current prices. In contrast to all other bidder types, this bidder uses an OR bidding language.

The (myopic) bestResponse or straightforward bidder is often assumed in game-theoretical analysis (Parkes and Ungar 2000). This bidder bids for all bundles that would maximize his surplus if it were to win any of them at current prices, and only for these bundles (i.e., his demand set $D _ { i } ( p ) )$ . Determining the demand set requires advanced computational skills:

$$
D _ {i} (p) := \{S \subseteq \mathcal {K} \colon v _ {i} (S) - p _ {i} (S) \geq v _ {i} (T) - p _ {i} (T), \forall T \subseteq \mathcal {K} \}.
$$

The powerSet bidder evaluates all possible bundles in each round and submits bids for all bundles which are profitable given his valuation on a bundle and the current ask prices. In our ICA simulations, we modeled this bidder to bid on his 10 most profitable bundles given current ask prices in each round. In contrast to the bestResponse bidder, the powerSet bidder selects not only those bundle(s) in his demand set providing the maximum profit, but less profitable ones as well.

The heuristic bidder is close to the powerSet bidder, but randomly selects 3 out of the 10 most profitable bundles (3 of 10) he can bid on. Another version bids a random 5 out of his 20 most profitable bundles (5 of 20).

The bestChain bidder is similar to the INT bidder in An et al. (2005). It implements the following algorithm:

for each $k \in \mathcal { K }$

(1) Create a single-item bundle $B _ { k } = \{ k \}$

(2) Define $\alpha = \arg \operatorname* { m a x } _ { \boldsymbol { l } \in \mathcal { K } \setminus B _ { \iota } } A U ( B _ { k } \cup \{ \boldsymbol { l } \} )$

(3) if $A U ( B _ { k } \cup \{ \alpha \} ) > A U ( \dot { B _ { k } } ) ,$

then $B _ { k } = B _ { k } \cup \{ \alpha \} , \mathrm { g o t o } ( 2 ) .$

Starting from each individual item $k \in \mathcal { K } ,$ the algorithm finds another item which provides a maximum increase in average unit utility (AU) of the bundle given current prices. If the new average utility exceeds the previous value, the new item is added to the bundle and the process is continued until the average unit utility cannot be increased further.

## 3.3. Auction Processor

The auction processor implements the auction logic, enforces auction protocol rules, calculates ask prices and the provisional allocation for the current round, and selects winning bids. We used five auction processors in our numerical experiments: the CC auction processor, the RAD processor, the ALPS and the ALPSm processors, and the sealed bid auction processor. The sealed bid auction processor was used to determine the revenue-maximizing allocation in combination with modified powerSet bidders which always submitted their true valuations for all bundles (instead of bidding minimal possible prices on the top ten bundles).

## 3.4. Performance Measures

We use allocative efficiency (or simply efficiency) as a primary measure to benchmark auction designs. Allocative efficiency in CAs can be measured as the ratio of the total valuation of the resulting allocation X to the total valuation of an efficient allocation $X ^ { \ast }$ (Kwasnica et al. 2005):

$$
E (X) = \frac {\sum_ {i \in \mathcal {I}} v _ {i} (\bigcup_ {S \subseteq \mathcal {K} : x _ {i} (S) = 1} S)}{\sum_ {i \in \mathcal {I}} v _ {i} (\bigcup_ {S \subseteq \mathcal {K} : x _ {i} ^ {*} (S) = 1} S)}.
$$

The term $\textstyle \sum _ { i \in { \mathcal { I } } } v _ { i } ( \bigcup _ { S \subseteq { \mathcal { K } } : x _ { i } ( S ) = 1 } S )$ can be simplified to $\begin{array} { r } { \sum _ { i \in \mathcal { I } } \sum _ { S \subseteq \mathcal { K } } x _ { i } ( S ) v _ { i } ( S ) } \end{array}$ in case of a pure XOR auction, because at most one bundle per bidder can be allocated.

Another measure is the revenue distribution which shows how the overall economic gain is distributed between the auctioneer and bidders. In cases where the auction is not 100% efficient, yet another part of the overall utility is simply lost. Given the resulting allocation X and the bid prices $\{ b _ { i } ( S ) \}$ , the auctioneer’s revenue share is measured as the ratio of the auctioneer’s income to the total sum of valuations of an efficient allocation $X ^ { \ast }$ :

$$
R (X) = \frac {\sum_ {S \subseteq \mathcal {K}} \sum_ {i \in \mathcal {I}} x _ {i} (S) b _ {i} (S)}{\sum_ {i \in \mathcal {I}} v _ {i} (\bigcup_ {S \subseteq \mathcal {K} : x _ {i} ^ {*} (S) = 1} S)}.
$$

The cumulative bidders’ revenue share is $E ( X ) -$ R X. Note that efficiency depends only on the final allocation and not on the final bid prices $b _ { i } ( S )$ Therefore, it is possible for two auction outcomes with equal efficiency to have significantly different auctioneer revenues.

## 4. Experimental Results

In the first set of simulations, our goal was to compare the performance of various ICA designs based on different value models. We were interested in efficiency and revenue figures of various auction designs using only myopic bestResponse bidders and a small static minimum bid increment. The results provide an estimate of the efficiency loss that can be attributed to the auction design and, in particular, to linear ask prices.

## 4.1. Efficiency of Different ICA Designs

We used seven different value models to compare the CC auction, RAD, RAD without eligibility (RADne), ALPS, and ALPSm designs. For each value model, we created 40 auction instances with different valuations and ran each of them in all five auction formats, preserving bidder valuations. All auctions used a bid increment of 0.1. Details on the auction setup and the mean results of 40 auction rounds are provided in Table 1. The left-hand column indicates the auction setup, i.e., the number of items, valuations, number of bidders, and the number of auctions where the valuations fulfill BSC. As can be seen, in most cases BSC was not fulfilled.

Real estate 3 3 describes a real-estate model with nine lots for sale and five bidders. Individual item valuations have normal distribution with a mean of 10 and a variance of 2. There is a 90% probability of a vertical or horizontal edge and an 80% probability of a diagonal edge. Edge weights have a mean of 0.5 and a variance of 0.3. Sixteen instances of the valuations generated for these 40 auctions fulfilled BSC. Lot valuations in the real estate $4 \times 4$ model with 16 lots and

10 bidders have a mean of 6 and a variance of 1.1; all other parameters are equal to the real estate $3 \times 3$ model. Only one of the auctions in this model followed BSC. The pairwise synergy low model describes a value model with seven items, where valuations were drawn for each auction based on a uniform distribution between the upper and lower bounds stated in Table 1. The synergy values used were between 0 and 0.5 in the pairwise synergy low model and between 1.5 and 2.0 in the pairwise synergy high model, each having five bestResponse bidders. In the Real estate and pairwise synergy value models, bidders were interested in a maximum bundle size of three because in these value models large bundles have advantages over small ones. In other value models, bidders were not restricted in bundle size. For the transportation and matching value models, the number of bidders was higher to have sufficient competition. The matching value model had 84 items, i.e., 21 time slots per airport. None of these auctions fulfilled BSC. Finally, transportation large modelled a transportation network with 50 items (edges) of the graph and 34 cities (vertices). In transportation large, we used 30 bestResponse bidders while in transportation small, we had 25 edges, 15 vertices, and only 15 bidders. None of the transportation auctions fulfilled BSC. All value model parameters were selected so that the efficient allocation of each auction had the same order of magnitude (200 to 250).

Overall, efficiency in all value models using bestResponse bidders was very high and showed the same pattern. The simulation resulted in the highest efficiency levels for the ALPSm auction design, due to the higher number of bids available for winner determination in late rounds. In the pairwise synergy high value model, there was no significant difference between the efficiency values of the CC auction and ALPSm (t-test, p-value <sub>=</sub> 079). The RAD design suffered from premature termination. Also, omitting the eligibility rules (RADne) did not show a significant improvement. In all but two value models (real estate $4 \times 4 ,$ transportation small), the CC auction achieved higher efficiency values than ALPS.

Figures 2, 3, and 4 show the box plots for the efficiency of selected value models using bestResponse bidders. We found a similar pattern for simulations with powerSet bidders that were restricted to submit their best 10 bids (see Figure 5).

Table 1 Efficiency of Different ICA Formats—Average Results of 40 Auctions with bestResponse Bidders

<table><tr><td rowspan="2">Value model</td><td></td><td colspan="6">ICA format</td></tr><tr><td></td><td>ALPS</td><td>ALPSm</td><td>CC</td><td>RAD</td><td>RADne</td><td>VCG</td></tr><tr><td>Real estate 3 × 3</td><td>∅ Efficiency in %</td><td>96.5</td><td>98.81</td><td>97.13</td><td>69.9</td><td>71.21</td><td>100</td></tr><tr><td>9 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>67.75</td><td>82.5</td><td>86.56</td><td>10.11</td><td>10.37</td><td>84.2</td></tr><tr><td>5 bestResponse bidders</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>28.75</td><td>16.31</td><td>10.57</td><td>59.79</td><td>60.84</td><td>15.8</td></tr><tr><td>16 auctions BSC</td><td>∅ Rounds</td><td>532.98</td><td>760.83</td><td>400</td><td>46.95</td><td>47.15</td><td>1</td></tr><tr><td>Real estate 4 × 4</td><td>∅ Efficiency in %</td><td>96.84</td><td>99.82</td><td>96.24</td><td>76.13</td><td>76.09</td><td>100</td></tr><tr><td>16 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>75.51</td><td>90.72</td><td>90.56</td><td>9.16</td><td>9.75</td><td>90.3</td></tr><tr><td>10 bestResponse bidders</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>21.34</td><td>9.1</td><td>5.69</td><td>66.97</td><td>66.34</td><td>9.7</td></tr><tr><td>1 auction BSC</td><td>∅ Rounds</td><td>440.73</td><td>641.7</td><td>247.7</td><td>28.95</td><td>30.65</td><td>1</td></tr><tr><td>Pairwise synergy low</td><td>∅ Efficiency in %</td><td>94.82</td><td>99.73</td><td>98.56</td><td>69.98</td><td>69.17</td><td>100</td></tr><tr><td>7 items, valued 0 to 195</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>72.41</td><td>87.53</td><td>88.29</td><td>8.84</td><td>8.63</td><td>87.08</td></tr><tr><td>Synergy 0 to 0.5</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>22.42</td><td>12.19</td><td>10.27</td><td>61.14</td><td>60.54</td><td>12.92</td></tr><tr><td>5 bestResponse bidders</td><td>∅ Rounds</td><td>369.3</td><td>816</td><td>412.82</td><td>44.42</td><td>44.4</td><td>1</td></tr><tr><td>20 auctions BSC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pairwise synergy high</td><td>∅ Efficiency in %</td><td>92.8</td><td>99.64</td><td>99.87</td><td>72.66</td><td>71.99</td><td>100</td></tr><tr><td>7 items, valued 0 to 88</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>76.28</td><td>87.97</td><td>89.18</td><td>9.82</td><td>9.6</td><td>87.5</td></tr><tr><td>Synergy 1.5 to 2.0</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>16.52</td><td>11.68</td><td>10.69</td><td>62.84</td><td>62.4</td><td>12.5</td></tr><tr><td>5 bestResponse bidders</td><td>∅ Rounds</td><td>354.65</td><td>656.38</td><td>338.48</td><td>41.8</td><td>41.67</td><td>1</td></tr><tr><td>15 auctions BSC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Matching</td><td>∅ Efficiency in %</td><td>97.27</td><td>99.81</td><td>97.95</td><td>90.09</td><td>90.56</td><td>100</td></tr><tr><td>84 items (21 slots/airport)</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>52.01</td><td>53.81</td><td>67.9</td><td>28.26</td><td>30.45</td><td>42.33</td></tr><tr><td>40 bestResponse bidders</td><td>∅ Sum of bidders&#x27; revenue in %</td><td>45.26</td><td>46.01</td><td>30.04</td><td>61.83</td><td>60.11</td><td>57.67</td></tr><tr><td>0 auctions BSC</td><td>∅ Rounds</td><td>671.55</td><td>186.47</td><td>93.47</td><td>23.3</td><td>27.5</td><td>1</td></tr><tr><td>Transportation large</td><td>∅ Efficiency in %</td><td>93.97</td><td>99.52</td><td>96.78</td><td>82.48</td><td>83.73</td><td>100</td></tr><tr><td>50 items, density ρ = 2.9</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>62.33</td><td>76.61</td><td>80.92</td><td>38.97</td><td>34.9</td><td>64.21</td></tr><tr><td>34 cities (vertices)</td><td>∅ Sum of bidders&#x27; revenue in %</td><td>31.65</td><td>22.91</td><td>15.86</td><td>43.5</td><td>48.83</td><td>35.79</td></tr><tr><td>30 bestResponse bidders</td><td>∅ Rounds</td><td>193.4</td><td>161.8</td><td>180.05</td><td>31.38</td><td>28.3</td><td>1</td></tr><tr><td>0 auctions BSC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Transportation small</td><td>∅ Efficiency in %</td><td>98.26</td><td>99.78</td><td>97.73</td><td>82.98</td><td>81.31</td><td>100</td></tr><tr><td>25 items, density ρ = 3.2</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>54.79</td><td>59.54</td><td>65</td><td>21.96</td><td>17.93</td><td>48.32</td></tr><tr><td>15 cities (vertices)</td><td>∅ Sum of bidders&#x27; revenue in %</td><td>43.48</td><td>40.23</td><td>32.74</td><td>61.02</td><td>63.38</td><td>51.68</td></tr><tr><td>15 bestResponse bidders</td><td>∅ Rounds</td><td>409.32</td><td>327</td><td>314.62</td><td>66.17</td><td>51.1</td><td>1</td></tr><tr><td>0 auctions BSC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

In these simulations, we wanted to avoid inefficiencies due to high bid increments and set the minimum bid increment to 0.1. Therefore, the average number of auction rounds was quite high in general. A minimum bid increment of 1 reduced the auction rounds in our simulations by a factor of 10. Note that the number of auction rounds is influenced by the valuation model, the number of bidders, and their bundle selection strategy. So the figures in Table 1 cannot easily be generalized but only compared relative to the same setting with a different auction format. ALPSm had the highest number of auction rounds except for the matching and the transportation value models.

RAD often terminated prematurely, leading to a much lower average number of auction rounds, but at the cost of lower efficiency. We have also tested a dynamic version of bid increments that decreases with increasing competition and could reduce the number of auction rounds in ALPS considerably with little or no effect of efficiency.

## 4.2. Auctioneer Revenue in Different ICAs

Another performance characteristic of auction formats is the revenue distribution, or which part of the overall utility goes to the auctioneer and which part is distributed to the bidders. In cases where the auction is not 100% efficient, part of the overall utility is lost. In theory, only minimal CE prices encourage myopic bestResponse bidding and lead to an efficient auction outcome, minimizing auctioneer revenue of an efficient allocation (Parkes 2006). Knowledge of the revenue distribution of a particular ICA design can affect bidding strategies of the participants. Our simulation results indicate significant differences in revenue distributions between different auction designs. Again, we found similar patterns across different value models (Figure 6). An important observation is that the CC design resulted in the highest average auctioneer revenue, followed by ALPSm. The dashed line in Figure 6 shows the average auctioneer revenue in case of a VCG auction. The VCG outcomes can serve as one indicator for competition in the auction, which was generally high. We have also run the experiments

Figure 2 Box Plot of Allocative Efficiency for the Real Estate Value Models with bestResponse Bidders  
![](/api/attachments/3DQQYFTD/fulltext/images/4fce376a63ec92b8997461fd2cc8bcde1f3b1a8ffbbb9467863051b413e3e5ee.jpg)

(b) Real estate 4× 4  
![](/api/attachments/3DQQYFTD/fulltext/images/2fb8972c71e4835498d2a478670e35573d2b4e0711e2306855db5777f1634f30.jpg)

Figure 3  
Box Plot of Allocative Efficiency for the Transportation Value Models with bestResponse Bidders  
![](/api/attachments/3DQQYFTD/fulltext/images/7dfb4dfe516679e98541f3b41921a5eeaa5fe081f1b74debd5e031b3dd092d1f.jpg)

(b) 50 edges  
![](/api/attachments/3DQQYFTD/fulltext/images/3c408e30112f9c5d2c7e76bdc73056e2ad40fe65a0b5e0abc3789b6f9bd790ed.jpg)  
with little competition (for example, the pairwise synergy low model with only three bidders), and found the final ALPS ask prices to be higher than the average VCG prices compared to auction instances with higher competition (real estate 3 <sub>×</sub> 3 with five or seven bidders).

## 4.3. Price Monotonicity

Reducing item prices in the course of the auction may be necessary to reflect the competitive situation but can also be confusing for bidders. Price fluctuations are a phenomenon in RAD and in ALPS. The literature does not describe a measure for price monotonicity. Prices in a linear price ICA can be described as a discrete function $f \colon  { \mathbb { N } } \to  { \mathbb { R } } _ { 0 } ^ { + }$ for a single item (see Figure 7).

Figure 4 Box Plot of Allocative Efficiency for the Matching and Pairwise Synergy Value Models with bestResponse Bidders  
![](/api/attachments/3DQQYFTD/fulltext/images/32cc5ec480011b62ffd755bbec4394c84907b09aa73338aded66c8271fc6c4f9.jpg)

(b) Pairwise synergy high  
![](/api/attachments/3DQQYFTD/fulltext/images/e51b0f8c0d6be1f6fd214a8168dd6f643dff0043815a760efd15fb2db019718b.jpg)

We measure price nonmonotonicity in auctions as the sum of price decreases $\Delta e _ { t , k }$ divided by the sum of price increases $\Delta p _ { t , k }$ for all items k in all auction rounds t. This results in the price nonmonotonicity $m \in [ 0 , 1 ]$ , where $m = 0$ describes a fully monotonic function as in the CC auction:

$$
m = \frac {\sum_ {t = 1} ^ {T} \sum_ {k \in \mathcal {K}} \Delta e _ {t , k}}{\sum_ {t = 1} ^ {T} \sum_ {k \in \mathcal {K}} \Delta p _ {t , k}}.\tag{1}
$$

Figure 8 provides a box plot for the m values of ALPS, ALPSm, RAD, and RADne (without eligibility) in the real estate and the transportation value models with bestResponse bidders. Higher values for m in ALPS can be attributed to the fact that auctions take more rounds than in RAD and do not terminate prematurely.

Figure 5  
Box Plot of Allocative Efficiency for a Real Estate and Transportation Value Model with powerSet Bidders  
![](/api/attachments/3DQQYFTD/fulltext/images/cd8d18287f90cfb6dfd55e06e54004e3515fdb2e1092bd516241b6800d08d722.jpg)

(b) Transportation 25 edges  
![](/api/attachments/3DQQYFTD/fulltext/images/8d2bd9aec798d50adba1a9fd22659e75cd0fec5c0103240b19212bd137f0da68.jpg)

There is a long tradition in economics of Walrasian taˆtonnement, which allows prices both to ascend and descend (Ausubel 2006, p. 604), as is the case with ALPS and RAD. In applications where price fluctuations become an issue for bidders, alternative ways of calculating the pseudodual ask prices can help reduce or even eliminate this phenomenon. We have experimented with a simple rule that forces prices not to decrease across rounds (Shabalin et al. 2007). This rule ensures monotonic prices but also causes minor efficiency losses. Dunford et al. (2007) discuss an alternative approach that uses a quadratic program to smooth

Figure 6 Revenue Distribution of the Real Estate and Transportation Model with bestResponse Bidders  
![](/api/attachments/3DQQYFTD/fulltext/images/efdd9b2ac79c2570b6659a0030c29432d547d8e6594be61b4b3465af8cd7b4fb.jpg)

(b) Transportation 25 edges  
![](/api/attachments/3DQQYFTD/fulltext/images/c35ce1390ccfffe33eb314296123a6e877b2d2d3c48dbddba5f77ddcb4145f75.jpg)  
price fluctuations in RAD across rounds. Nonmonotonicity certainly deserves a more in-depth discussion. Laboratory experiments will be helpful to shed more light on the effect of price fluctuations on human bidders.

Figure 7 Calculation of a Single Item’s Price Nonmonotonicity  
![](/api/attachments/3DQQYFTD/fulltext/images/5fbd41648087b0b632645e2e009c6c13d36fe1c371783daf99d17e5398ae8db5.jpg)

Figure 8 Average Price Nonmonotonicity m in the Real Estate and Transportation Value Models  
![](/api/attachments/3DQQYFTD/fulltext/images/0c421dee2766ef57f9f726a70f7ebfb21fb30cd6d0eae31868df983338433662.jpg)  
(b) Transportation 25 edges

![](/api/attachments/3DQQYFTD/fulltext/images/21d73d7307b26602df4443cf6c8cc8f9456a184ff46d46e0804865d288746dd5.jpg)

## 4.4. Inefficiencies in Linear Price ICAs

While efficiency of linear price ICAs in our experiments was generally high, it is important to understand those cases where the final allocation is not optimal. We have analyzed all instances of auctions in the real estate and pairwise synergy value models, where efficiency was particularly low (90% and below). We have focused on the ALPSm and CC designs when the eligibility rules were disabled to isolate the negative impact of linear prices from inefficiencies due to eligibility rules. Here, only bestResponse bidders were used.

In all situations with an efficiency of less than 90%, the auctioneer did not sell all items, as compared to the efficient allocation. These situations happen rarely in the real estate value models, and even less so in the pairwise synergy value models, as can be seen in Figures 2 and 4. Whenever all items were sold, the allocative efficiency was always higher than 98%. The following two small examples in Tables 2 and 3 illustrate structural characteristics of valuations which can lead to inefficiencies in ICAs with linear prices and best-response bidding.

The example in Table 2 illustrates a scenario with three items $\hat { { \sf A } } , { \sf B } , { \sf C }$ and the valuations of four bidders. Each bidder has a valuation for one bundle only and the efficient allocation is marked with a star. In Table 2, the ALPSm design selects the bid of bidder 4 on bundle BC and leaves the item A unsold. The particular property of these valuations is the set of mutually exclusive bundle valuations AB and BC, none of which belongs to the efficient allocation. During the auction, bidders 3 and 4 drive up the prices, which blocks other bidders from submitting their true valuations. Interestingly, the auction outcome in this case is sensitive to start prices. The efficient allocation was found for item start prices of 1.3 and 1.9, but was inefficient for all other values from 0 to 2.0 with a 0.1 minimum bid increment. The CC design was generally efficient in this example.

Table 2 Example for Inefficiencies in ALPSm

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td><td>AB</td><td>AC</td><td>BC</td><td>ABC</td></tr><tr><td>Bidder1</td><td></td><td></td><td></td><td></td><td>9*</td><td></td><td></td></tr><tr><td>Bidder2</td><td></td><td>2*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bidder3</td><td></td><td></td><td></td><td>10</td><td></td><td></td><td></td></tr><tr><td>Bidder4</td><td></td><td></td><td></td><td></td><td></td><td>10</td><td></td></tr></table>

Table 3 Example for Inefficiencies in CC

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td><td>AB</td><td>AC</td><td>BC</td><td>ABC</td></tr><tr><td>Bidder1</td><td></td><td></td><td></td><td></td><td></td><td>20*</td><td>60</td></tr><tr><td>Bidder2</td><td>61*</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Bidder3</td><td></td><td></td><td></td><td>50</td><td>50</td><td></td><td></td></tr></table>

The second example in Table 3 illustrates a set of valuations where the CC design leads to an inefficient allocation. It allocates the item A to the bidder 2 and both items B and C remain unsold. Note that bidder 1’s high valuation on the bundle ABC dominates the bundle BC. At the time where bidder 2 overbids him, the prices are already too high on all items, which prevents the bidder 1 from submitting bids on the bundle BC. Again, all bidders follow a bestResponse strategy. The ALPSm design terminates with an efficient allocation in this example.

One possibility to mitigate the remaining inefficiencies in the ALPS and CC designs is to auction off the goods that have been unsold in an after market (sell the rest of the goods), but this still does not guarantee 100% efficiency and there might be no demand for these individual items, as in our first example in Table 2.

An alternative is the addition of a second phase with an ascending proxy auction, as suggested in the clock-proxy auction (Ausubel et al. 2006), with suitable eligibility rules. Without eligibility rules, the ALPS end prices as start prices for the ascending proxy auction, and with truthful bidders this will always lead to an efficient allocation. However, both minimum bid prices and eligibility rules are necessary to encourage active bidding during the first linear-price auction phase. The impact of different eligibility rules on the allocative efficiency in a two-stage auction as well as optimal bidding strategies in these auction designs are a topic for further research.

## 4.5. Price Deviations

It is impossible to calculate exact linear prices except from special types of valuations where goods are substitutes. In other words, in both ALPS and RAD, there will be cases where the ask prices in a new round are below some of the bid prices of losing bidders in the previous round. We will call this a price deviation. It can be confusing for losing bidders because their bids may have bid prices above current ask prices and still do not win in the provisional allocation. We have measured the average percentage of individual ask prices with price deviations in each round (see Figure 9). Overall, price deviations happened only in a very small percentage (<2%) of the ask prices in an auction. The auction rule that all old bids are active in each round led to a higher percentage of price deviations in ALPSm.

Figure 9 Percentage of Linear Ask Prices with Price Deviations in the Real Estate and Transportation Value Models  
![](/api/attachments/3DQQYFTD/fulltext/images/526ff3237133b307df06038ff6c5e9710a4cc33d730f680df473ed072819f3df.jpg)

(b) Transportation 25 edges  
![](/api/attachments/3DQQYFTD/fulltext/images/67a52801213e7382df9f0ffc35a72c2b1697a670942b006f266ac6817603177a.jpg)

In addition to price deviations, we have also analyzed efficiency with respect to increasing levels of synergy among items. The pairwise synergy value model allows synergy values to be increased from zero to three and the results to be analyzed (see Figure 10). Interestingly, auction efficiency remains high for all auction designs even in the case of high syn-

Figure 10 Changes in Efficiency Based on Different Synergy Values  
![](/api/attachments/3DQQYFTD/fulltext/images/5c2927cc1ae4c0fcd2f8678cdef07581de44361139b007606f0d72c84f9c6bd2.jpg)  
ergy values. Note that with a synergy value of 2.5, a bundle of items already has 3.5 times the value of its individual items.

## 5. Analysis of Bidding Strategies

In the previous section, we primarily used myopic bestResponse agents. We also performed the same simulations with powerSet bidders limited to their best 10 bids and found the results to be very similar. While it is useful to estimate the efficiency loss attributed to the use of specific auction formats, real-world bundling and bidding strategies are often much simpler than powerSet or bestResponse bidding strategies, because evaluating and submitting all possible bundles is typically not practical for bidders (An et al. 2005).

According to a study in transportation CAs by Plummer (2003), out of the 644 carriers only about 30 percent submitted package bids. This group of carriers submitted between two and seven lane combinations and the vast majority of the packages were small, containing between two and four lanes. The discounts carriers gave to packaged lanes were around five percent. Apart from the novelty of CAs and the complexity of knowing their valuations over all possible bundles, the bidders face the bundle selection problem from an exponential number of possible bundles. To overcome some of these problems, bidder decision support tools have been suggested (Song and Regan 2002, Hoffman et al. 2005), which are however currently rarely used in practice. It is therefore interesting to see how robust the above ICA formats are with respect to other, simpler bundling strategies.

In this analysis, we focused on bundle selection in iterative auctions and assumed that bidders bid the minimum price only (neglecting jump bids or similar phenomena). We used six types of bidding agents and the ALPS auction format because it has performed well on allocative efficiency, while at the same time it calculates minimal pseudodual ask prices for bidders. All bidders used the XOR bidding language with the notable exception of the naïve bidder, who used an OR language bidding only on individual items. We analyzed the real estate and pairwise synergy value models where naïve bidding makes sense, but did not consider the matching and transportation value models for this reason.

## 5.1. Efficiency of Pure Strategies

In a first set of simulations, we ran the same auction with all bidders of the same type and repeated it for different value models (see Table 4). The naïve bidder only bids up to his item valuations and ignores synergistic valuations. In our simulations, a naïve strategy was suboptimal and led to low efficiency scores and low auctioneer revenue. The powerSet bidder came out best, while the bestChain and heuristic bidders also achieved high levels of efficiency because they focused on the best bundles. The heuristic bidders (3 of 10, 5 of 20) showed efficiency and revenue values close to the powerSet and bestChain bidders. For example, there was no significant difference between the bestChain and the heuristic 3 of 10 bidder in ALPS (t-test, p-value of 0.65) in the real estate 3 3 value model. Auctions with bestResponse bidders did have high efficiency values but the auctioneer revenue was significantly lower than the revenue in all other auctions except with naïve bidders. We could find the same pattern in ALPSm, the CC auction, and in the other three value models analyzed. Figure 11 illustrates the revenue distributions for the real estate 4 4 value model with ALPSm and the CC auction.

## 5.2. Sensitivity Analysis with Respect to the Bidder Type

In a next set of simulations, we measured efficiency and revenue for auctions with nine (for the real estate 4 4 value model) or four (for all other value models) bestResponse bidders and a last bidder with a simpler bundle selection strategy (e.g., naïve, bestChain, heuristic) in ALPS. For the last bidder, the mean revenue over all 40 auctions was calculated. The results are shown in Table 5. Overall, efficiency was not much lower because 9 out of 10 and 4 of 5 bidders, respectively, were bestResponse bidders, keeping efficiency high. In Table 5, row “<sub></sub> Last bidder’s revenue in %” shows the difference in revenue for the last bidder. Clearly, the naïve bidding strategy came out worst.

Table 4 Pure Bidding Strategies in ICAs—Setup and Results

<table><tr><td rowspan="2">Setup</td><td colspan="7">Bidder type</td></tr><tr><td></td><td>naïve</td><td>bestChain</td><td>powerSet</td><td>3 of 10</td><td>5 of 20</td><td>bestResponse</td></tr><tr><td>Real estate  $3 \times 3$ </td><td>∅ Efficiency in %</td><td>54.84</td><td>96.31</td><td>98.63</td><td>96.95</td><td>95.95</td><td>96.18</td></tr><tr><td>9 items</td><td>∅ Auctioneer revenue in %</td><td>47.97</td><td>74.12</td><td>78.83</td><td>78.72</td><td>81</td><td>67.8</td></tr><tr><td>5 bidders</td><td>∅ Bidders&#x27; revenue in %</td><td>6.86</td><td>22.19</td><td>19.8</td><td>18.22</td><td>14.96</td><td>28.38</td></tr><tr><td></td><td>∅ Rounds</td><td>198.95</td><td>471</td><td>364.5</td><td>403.25</td><td>369.95</td><td>532.98</td></tr><tr><td>Real estate  $4 \times 4$ </td><td>∅ Efficiency in %</td><td>52.86</td><td>97.96</td><td>98.19</td><td>96.56</td><td>96.73</td><td>96.68</td></tr><tr><td>16 items</td><td>∅ Auctioneer revenue in %</td><td>48.43</td><td>84.61</td><td>86.65</td><td>85.03</td><td>87.29</td><td>75.56</td></tr><tr><td>10 bidders</td><td>∅ Bidders&#x27; revenue in %</td><td>4.43</td><td>13.35</td><td>11.54</td><td>11.53</td><td>9.44</td><td>21.13</td></tr><tr><td></td><td>∅ Rounds</td><td>108.55</td><td>230.43</td><td>247.5</td><td>367.23</td><td>289.7</td><td>671.95</td></tr><tr><td>Pairwise synergy low</td><td>∅ Efficiency in %</td><td>77.21</td><td>96.25</td><td>98.09</td><td>96.99</td><td>97.7</td><td>95.64</td></tr><tr><td>7 items, valuations 0 to 195</td><td>∅ Auctioneer revenue in %</td><td>66.63</td><td>75.68</td><td>81.83</td><td>81.56</td><td>85.3</td><td>74.07</td></tr><tr><td>Synergy 0 to 0.5, 5 bidders</td><td>∅ Bidders&#x27; revenue in %</td><td>10.59</td><td>20.57</td><td>16.25</td><td>15.43</td><td>12.4</td><td>21.57</td></tr><tr><td></td><td>∅ Rounds</td><td>259.65</td><td>461.2</td><td>369.88</td><td>395.45</td><td>382.88</td><td>541.77</td></tr><tr><td>Pairwise synergy high</td><td>∅ Efficiency in %</td><td>36.53</td><td>96.61</td><td>98.61</td><td>96.55</td><td>97.98</td><td>93.6</td></tr><tr><td>7 items, valuations 0 to 88</td><td>∅ Auctioneer revenue in %</td><td>31.53</td><td>78.62</td><td>83.25</td><td>82.19</td><td>85.91</td><td>76.47</td></tr><tr><td>Synergy 1.5 to 2.0, 5 bidders</td><td>∅ Bidders&#x27; revenue in %</td><td>5</td><td>17.99</td><td>15.36</td><td>14.36</td><td>12.06</td><td>17.14</td></tr><tr><td></td><td>∅ Rounds</td><td>116.35</td><td>380.32</td><td>335.8</td><td>351</td><td>342.05</td><td>466.18</td></tr></table>

Figure 11 Revenue Distribution for Pure Bidding Strategies in the Real Estate 4 <sub>×</sub> 4 Value Model  
![](/api/attachments/3DQQYFTD/fulltext/images/271c9a86d13a29353b6617a1bcd7e41f5c94b54b0effcd1c9dc7251fc6916503.jpg)

![](/api/attachments/3DQQYFTD/fulltext/images/9c598afd31e1c4ac034d9a4b97b0a895528ac7b76d742fed5b4a1914fbc261ef.jpg)

Interestingly, either a powerSet, bestChain, or heuristic strategy always performed better than the bestResponse strategy. One reason for this is the eligibility rules, which might prevent a bidder from submitting a winning bundle. The same type of sensitivity analysis was repeated with respect to powerSet bidders in Table 6, where we could see a similar pattern.

In another set of simulations, we tested how much better bundle bidders performed if they only compete with naïve bidders. We ran 40 auctions with 10 (or 5, respectively) naïve bidders only and then repeated them with the last bidder playing a bestSet, a bestChain, or a powerSet strategy. Results are shown in Table 7. Overall, the efficiency of these auctions decreased significantly compared to previous setups. This happened because the single smart bidder could mostly win his preferred bundle, while other bidders were restricted to bids on individual items often leading to inefficient allocations.

Table 5 Sensitivity with Respect to bestResponse Bidders

<table><tr><td rowspan="2">Setup</td><td colspan="7">Last bidder type</td></tr><tr><td></td><td>bestResponse</td><td>powerSet</td><td>3 of 10</td><td>5 of 20</td><td>bestChain</td><td>naïve</td></tr><tr><td>Real estate  $3 \times 3$ </td><td>∅ Efficiency in %</td><td>96.18</td><td>96.65</td><td>96.33</td><td>96.52</td><td>96.26</td><td>94.96</td></tr><tr><td rowspan="2">9 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>67.88</td><td>70.99</td><td>71.67</td><td>67.82</td><td>69.41</td><td>61.87</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>28.30</td><td>25.67</td><td>24.66</td><td>28.7</td><td>26.84</td><td>33.09</td></tr><tr><td>4 bestResponse plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>3.785</td><td>4.844</td><td>4.708</td><td>6.041</td><td>5.392</td><td>0.5227</td></tr><tr><td>Real estate  $4 \times 4$ </td><td>∅ Efficiency in %</td><td>96.24</td><td>97.13</td><td>96.58</td><td>96.29</td><td>96.95</td><td>96.08</td></tr><tr><td rowspan="2">16 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>74.39</td><td>75.77</td><td>74.54</td><td>76.38</td><td>75.41</td><td>71.83</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>21.85</td><td>21.36</td><td>22.05</td><td>19.91</td><td>21.54</td><td>24.25</td></tr><tr><td>9 bestResponse plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>1.314</td><td>2.558</td><td>2.562</td><td>2.187</td><td>2.269</td><td>0.2110</td></tr><tr><td>Pairwise synergy low</td><td>∅ Efficiency in %</td><td>95.35</td><td>97.78</td><td>96.98</td><td>97.09</td><td>96.96</td><td>92.86</td></tr><tr><td>7 items, valued 0 to 195</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>71.87</td><td>73.91</td><td>76.81</td><td>73.83</td><td>73.94</td><td>69.35</td></tr><tr><td>Synergy 0 to 0.5</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>23.48</td><td>23.87</td><td>20.17</td><td>23.26</td><td>23.02</td><td>23.51</td></tr><tr><td>4 bestResponse plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>4.826</td><td>7.928</td><td>5.679</td><td>6.908</td><td>5.487</td><td>1.533</td></tr><tr><td>Pairwise synergy high</td><td>∅ Efficiency in %</td><td>92.04</td><td>94.17</td><td>92.9</td><td>93.88</td><td>93.98</td><td>86.37</td></tr><tr><td>7 items, valued 0 to 88</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>73.33</td><td>76.37</td><td>77.15</td><td>76.24</td><td>74.74</td><td>65.05</td></tr><tr><td>Synergy 1.5 to 2.0</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>18.71</td><td>17.8</td><td>15.75</td><td>17.64</td><td>19.24</td><td>21.32</td></tr><tr><td>4 bestResponse plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>3.191</td><td>5.076</td><td>4.569</td><td>5.577</td><td>5.487</td><td>0</td></tr></table>

Table 6 Sensitivity with Respect to powerSet Bidders

<table><tr><td rowspan="2">Setup</td><td colspan="7">Last bidder type</td></tr><tr><td></td><td>bestResponse</td><td>powerSet</td><td>3 of 10</td><td>5 of 20</td><td>bestChain</td><td>naïve</td></tr><tr><td>Real estate  $3 \times 3$ </td><td>∅ Efficiency in %</td><td>98.13</td><td>98.9</td><td>98.34</td><td>98.2</td><td>98.08</td><td>96.05</td></tr><tr><td rowspan="2">9 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>79.34</td><td>79.67</td><td>79.87</td><td>80.14</td><td>79.67</td><td>66.76</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>18.79</td><td>19.23</td><td>18.47</td><td>18.06</td><td>18.41</td><td>29.29</td></tr><tr><td>4 powerSet plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>1.522</td><td>3.237</td><td>3.263</td><td>2.809</td><td>2.341</td><td>0.05379</td></tr><tr><td>Real estate  $4 \times 4$ </td><td>∅ Efficiency in %</td><td>98.68</td><td>98.83</td><td>98.53</td><td>98.4</td><td>98.6</td><td>97.4</td></tr><tr><td rowspan="2">16 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>85.67</td><td>86.88</td><td>86.57</td><td>86.53</td><td>86.76</td><td>85</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>13.01</td><td>11.95</td><td>11.95</td><td>11.88</td><td>11.83</td><td>12.40</td></tr><tr><td>9 powerSet plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>0.4362</td><td>0.8017</td><td>0.6333</td><td>1.009</td><td>1.123</td><td>0.002506</td></tr><tr><td>Pairwise synergy low</td><td>∅ Efficiency in %</td><td>98.42</td><td>99.6</td><td>98.3</td><td>98.84</td><td>99.25</td><td>96.33</td></tr><tr><td>7 items, valued 0 to 195</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>80.57</td><td>83.78</td><td>83.85</td><td>84.06</td><td>84.62</td><td>78.41</td></tr><tr><td>Synergy 0 to 0.5</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>17.84</td><td>15.81</td><td>14.45</td><td>14.79</td><td>14.63</td><td>17.92</td></tr><tr><td>4 powerSet plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>2.502</td><td>4.171</td><td>4.104</td><td>3.899</td><td>3.883</td><td>0.2604</td></tr><tr><td>Pairwise synergy high</td><td>∅ Efficiency in %</td><td>98.17</td><td>99.06</td><td>98.55</td><td>99.01</td><td>98.36</td><td>95.88</td></tr><tr><td>7 items, valued 0 to 88</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>82.2</td><td>86.41</td><td>86.25</td><td>86.47</td><td>85.56</td><td>74.6</td></tr><tr><td>Synergy 1.5 to 2.0</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>15.97</td><td>12.65</td><td>12.29</td><td>12.54</td><td>12.80</td><td>21.27</td></tr><tr><td>4 powerSet plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>1.949</td><td>3.336</td><td>2.876</td><td>3.106</td><td>2.757</td><td>0</td></tr></table>

In comparison to four naïve bidders, a bestResponse strategy of the fifth bidder performed slightly better than other bundling strategies (see Table 7). This may be attributed to the fact that bidding on more bundles drives up ask prices on individual items.

In summary, from the perspective of a bidder who is interested in maximizing his own revenue, it is favorable to use bundle bidding. If all other bidders in the auction use a bestResponse or a powerSet strategy, the bidder is better off using a powerSet strategy. In contrast, if all other bidders bid naïvely, the best-Response strategy is slightly better than the powerSet strategy. Overall, the more bidders who use bundle bids, the better it is for the auctioneer.

Table 7 Sensitivity with Respect to Naïve Bidders

<table><tr><td rowspan="2">Setup</td><td colspan="7">Last bidder type</td></tr><tr><td></td><td>bestResponse</td><td>powerSet</td><td>3 of 10</td><td>5 of 20</td><td>bestChain</td><td>naïve</td></tr><tr><td>Real estate  $3 \times 3$ </td><td>∅ Efficiency in %</td><td>69.96</td><td>69.95</td><td>69.78</td><td>69.46</td><td>69.18</td><td>54.84</td></tr><tr><td rowspan="2">9 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>48.19</td><td>48.68</td><td>48.68</td><td>48.89</td><td>48.48</td><td>47.97</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>21.77</td><td>21.27</td><td>21.1</td><td>20.57</td><td>20.71</td><td>6.863</td></tr><tr><td>4 naïve plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>17.12</td><td>16.92</td><td>16.81</td><td>16.18</td><td>16.26</td><td>1.199</td></tr><tr><td>Real estate  $4 \times 4$ </td><td>∅ Efficiency in %</td><td>62.07</td><td>61.99</td><td>61.76</td><td>61.74</td><td>61.66</td><td>52.86</td></tr><tr><td rowspan="2">16 items</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>48.6</td><td>48.72</td><td>48.93</td><td>48.85</td><td>48.87</td><td>48.43</td></tr><tr><td>∅ Sum of bidder&#x27;s revenue in %</td><td>13.47</td><td>13.27</td><td>12.83</td><td>12.89</td><td>12.78</td><td>4.431</td></tr><tr><td>9 naïve plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>9.939</td><td>9.809</td><td>9.471</td><td>9.452</td><td>9.295</td><td>0.4877</td></tr><tr><td>Pairwise synergy low</td><td>∅ Efficiency in %</td><td>85.13</td><td>85.1</td><td>85.08</td><td>85.08</td><td>84.66</td><td>77.15</td></tr><tr><td>7 items, valued 0 to 195</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>67.63</td><td>68.34</td><td>68.46</td><td>68.46</td><td>68.28</td><td>67.62</td></tr><tr><td>Synergy 0 to 0.5</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>17.5</td><td>16.76</td><td>16.61</td><td>16.62</td><td>16.38</td><td>9.535</td></tr><tr><td>4 naïve plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>10.96</td><td>10.55</td><td>10.57</td><td>10.61</td><td>9.984</td><td>1.827</td></tr><tr><td>Pairwise synergy high</td><td>∅ Efficiency in %</td><td>61.96</td><td>61.97</td><td>61.97</td><td>61.87</td><td>60.5</td><td>36.50</td></tr><tr><td>7 items, valued 0 to 88</td><td>∅ Auctioneer&#x27;s revenue share in %</td><td>31.76</td><td>32.32</td><td>32.28</td><td>32.4</td><td>32.32</td><td>32.01</td></tr><tr><td>Synergy 1.5 to 2.0</td><td>∅ Sum of bidder&#x27;s revenue in %</td><td>30.19</td><td>29.66</td><td>29.69</td><td>29.47</td><td>28.18</td><td>4.49</td></tr><tr><td>4 naïve plus one bidder</td><td>∅ Last bidder&#x27;s revenue in %</td><td>27.01</td><td>26.72</td><td>26.74</td><td>26.59</td><td>25.37</td><td>0.8595</td></tr></table>

The computational complexity of CAP and the ask price calculation and the time to solve realistic problem sizes is particularly important in iterative CAs, where bidders submit bids in an interactive mode. For example, we could solve practically relevant problem sizes with up to 2,659 bids (196 items, 230 bidders) in the airport value model, and for 659 bids (62 items, 40 bidders) in the transportation model in less than 2 minutes on an Intel M processor (2.13 GHz) running Windows XP and the open source IP solver “lp\_solve.” The literature provides much useful work on solving large instances of CAP which is outside the scope of this paper (Lehmann et al. 2006, Leyton-Brown et al. 2006).

## 6. Conclusion

Iterative combinatorial auctions using linear ask prices are promising mechanisms for complex negotiation problems including multiple heterogeneous items. While game theoretical modelling is essential for the understanding of the basic economic laws governing the bidding process, the discrete nature of ICAs, the effects of eligibility rules, and finegrained ask price calculations in these auction formats defy much formal analysis. Economic experiments, on the other hand, are costly and the number of treatment variables that can be analyzed in laboratory experiments is limited. In recent years, computation has become another research method, complementing theory and experiment (a.k.a. computational sciences). Computer simulations make it possible to investigate scenarios and study phenomena that have been shown to be difficult to analyze analytically. Combinatorial auctions are still a new phenomenon and after a number of seminal contributions describing the underlying economic theory, much can be gained by testing new auction rules and different types of information feedback using computational methods and laboratory experiments.

In this paper, we have used computational experiments to compare characteristics of four linear price ICA designs—two established (CC auction, RAD) and two new ones (ALPS, ALPSm)—based on different value models and bundling strategies.

In contrast to primaldual auction formats, linearprice combinatorial auctions follow a more heuristic approach to update ask prices and find the efficient solution. While it is easy to construct examples where linear prices lead to inefficiencies, the allocative efficiency in ALPS, ALPSm, and the CC auction was surprisingly high for very realistic value models in our large-scale experiments. Just as exact combinatorial optimization algorithms find a feasible optimal solution at the cost of high computational cost, primal-dual auction mechanisms provide an efficient solution at the cost of many auction rounds and nonlinear personalized prices. Also, best-response bidding is required to achieve allocative efficiency. In analogy, similar to approximation schemes or heuristics, linear-price auctions can find very good allocations in a much lower number of auction rounds at the cost of minor inefficiencies.

ALPSm typically achieves higher efficiency and lower ask prices than the CC auction. In comparison to the CC auction, nonmonotonicity and price deviations can be disturbing for bidders in RAD and ALPS. Only a small percentage of ask prices showed price deviations in our experiments, but price monotonicity was low. Interestingly, even in cases with high synergy values in the pairwise synergy value model, efficiency levels in ALPS, ALPSm, and the CC auction were very high. For the remaining inefficiencies in linear price auctions, there are a few remedies such as the proxy phase in the clock-proxy auction (Ausubel et al. 2006) that address these inefficiencies, but these designs have not yet been thoroughly analyzed. In summary, linear price designs bear a number of advantages:

• Only a linear number of prices needs to be communicated.

• Linear prices, if perceived as a guideline, help bidders to easily find items with high competition and allow for endogenous bidding (Kwon et al. 2005).

• The perceived lack of fairness of nonanonymous prices may be an issue in some applications. Anonymous linear prices do not suffer from this drawback.

• The number of auction rounds is much lower at the expense of inefficiencies at the end of the auction compared to primaldual auction formats.

• ALPSm showed to be robust against different non-best-response bidding strategies. This robustness is important because human bidders might not be able to follow a pure best-response strategy.

The results provide an estimator for the efficiency of linear price ICAs and a starting point for further theoretical research and laboratory experiments. Laboratory experiments are an important complement to our analysis because important aspects of human cognition can only be observed in the laboratory and help to fine-tune simulation and analytical models.

## Acknowledgments

Financial support from the Deutsche Forschungsgemeinschaft (DFG) (BI 1057/1-1) is gratefully acknowledged. The authors also thank Kemal Guler, Ramayya Krishnan, David Parkes, Richard Steinberg, Sven de Vries, and three anonymous referees for valuable feedback on this paper. Errors are, of course, the authors’ responsibility.

## Appendix A. ALPS Ask Prices

A central ALPS auction rule focuses on the calculation of ask prices. There are a number of ways that pseudodual prices can be calculated. The following three properties can serve as guidelines:

1. The ask prices for the next round should be compatible with the current provisional allocation and submitted bids, i.e., all winning bids are higher than or equal to the ask prices and all losing bids are lower than the ask prices. If such prices do not exist, they should be approximated as closely as possible.

2. The ask prices should be balanced across items to be perceived as fair and to mitigate the threshold problem. The threshold problem describes the problem multiple small bidders face when they try to outbid one big bidder bidding on many items.

3. The ask prices should be minimal, enabling bidders to submit bids as long as they can.

RAD describes a procedure to satisfy the first two properties by solving a series of linear programs (LPs), minimizing the sum of slack variables. The idea of pseudodual prices has been introduced already in Rassenti et al. (1982). In ALPS, we propose an extension to RAD which fulfills all three properties and addresses some pitfalls in RAD. The overall approach can be schematically described as follows:

$$
\begin{array}{l l} \min _ {p (k),   \delta_ {b}} & \{\max \{\delta_ {b} \}, \max \{p (k) \} \} \\ \text { subject   to: } & \sum_ {k \in S} p (k) = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in W \\ & \sum_ {k \in S} p (k) + \delta_ {b} \geq b _ {i} (S) \quad \forall   b = b _ {i} (S) \in L \\ & \delta_ {b} \geq 0 \quad \forall   b \in L \\ & p (k) \geq 0 \quad \forall   k \in \mathscr {K}. \end{array}\tag{A1}
$$

The first condition sets the bid prices of the winning bids equal to the ask prices, which satisfies the first compatibility requirement. The second condition tries to satisfy the second compatibility requirement as closely as possible, whereby the distortions $\delta _ { b }$ represent the deviations from the ideal. Losing bids of a winning bidder are not included in the second condition. The reason for this is the XOR bidding language. Because bidders can only win one bundle at maximum, their losing bids might keep up prices on other items unnecessarily, which conflicts with the third requirement.

Note that RAD and ALPS describe only two ways to calculate pseudodual ask prices in each round. There are various possibilities in choosing an objective function and constraints that satisfy different criteria. For example, one might also try to minimize nonmonotonicity across rounds. Dunford et al. (2007) have explored this subject further and found high monotonicity with alternative formulations. In this paper, we have focused on a method that satisfies the above three constraints. The schematically defined objective function min-max-.  max-p k should describe a balanced minimization of all distortions $\delta _ { b }$ and then a balanced minimization of the ask prices. This price calculation procedure is now described in detail.

In a first step, we sequentially lower all slack variables while trying to keep them balanced. We first minimize the maximum of all slack variables, then fix those slack variables that cannot be further improved and repeat. Let $\hat { L }$ denote the set of all bids b for which $\delta _ { b }$ cannot be improved any more, and initialize it with $\hat { L } = \varnothing$ . Then, solve the following linear program (A2):

$$
\begin{array}{l l} \min _ {p (k), Z, \delta_ {b}} & Z \\ \text { subject   to: } & \sum_ {k \in S} p (k) = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in W \\ & \sum_ {k \in S} p (k) + \hat {\delta} _ {b} = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in \hat {L} \\ & \sum_ {k \in S} p (k) + \delta_ {b} \geq b _ {i} (S) \quad \forall   b = b _ {i} (S) \in L \setminus \hat {L} \\ & 0 \leq \delta_ {b} \leq Z \quad \forall   b \in L \setminus \hat {L} \\ & p (k) \geq 0 \quad \forall   k \in \mathscr {K}. \end{array}\tag{A2}
$$

Let $Z ^ { \ast } , \delta ^ { \ast } , \mathcal { P } ^ { \ast }$ be the solution of (A2) and let $L ^ { * } : =$ -b $\delta _ { b } ^ { * } = Z ^ { * } \} . \mathrm { I f } \ Z ^ { * } = 0 .$ , we are done. Otherwise, RAD would fix the slack variables for all bids in $L ^ { * }$ and proceed. However, if $L ^ { * }$ contains more than one element, some of these slack variables may still be possible to improve. Moreover, if the simplex optimization algorithm (Nemhauser and Wolsey 1988) is used, we will very likely get some $\delta _ { b } ^ { * } = Z ^ { * }$ because it always finds some vertex of the feasible polytope. This requires additional steps. Therefore, ALPS restricts the slack variables by $Z ^ { * }$ and minimizes the sum of all slack variables in $L ^ { * }$ as follows:

$$
\begin{array}{l l} \min _ {p (k), \delta_ {b}} & \sum_ {b \in L ^ {*}} \delta_ {b} \\ \text {subject to:} & \sum_ {k \in S} p (k) = b _ {i} (S) \quad \forall b = b _ {i} (S) \in W \\ & \sum_ {k \in S} p (k) + \hat {\delta} _ {b} = b _ {i} (S) \quad \forall b = b _ {i} (S) \in \hat {L} \\ & \sum_ {k \in S} p (k) + \delta_ {b} \geq b _ {i} (S) \quad \forall b = b _ {i} (S) \in L \setminus \hat {L} \\ & 0 \leq \delta_ {b} \leq Z ^ {*} \quad \forall b \in L \setminus \hat {L} \\ & p (k) \geq 0 \quad \forall k \in \mathscr {K}. \end{array}\tag{A3}
$$

If at least one of the slack variables in $L ^ { * }$ can be improved, this will be done by (A3). We now remove all bids with improved slack variables from $L ^ { * }$ and repeat (A3) until no more slack variables can be improved. At this point, we set $\hat { L } : = \hat { L } \cup L ^ { * } .$ , fix all nonimprovable slack variables $( \forall b \in L ^ { * }$ set $\hat { \delta } _ { b } : = \delta _ { b } ^ { * } )$ and continue with (A2).

After the set of all positive slack variables $\hat { L }$ is identified and all those slack variables are minimized and fixed to $\bigl \{ \hat { \delta } _ { b } \bigr \} .$ , the prices may still not be unique. For example, in the ideal case, we get $\hat { L } = \varnothing$ and we still have a lot of freedom in setting prices. We now balance prices similar to minimizing slack variables in the previous step. We first minimize the maximum of all prices, then fix those prices that cannot be further lowered and repeat. Let $\widehat { \mathcal { K } }$ denote the set of all items for which prices cannot be lowered any more, and initialize it with $\widehat { \mathcal { K } } = \alpha$ . Then, solve the following linear program (A4):

$$
\begin{array}{l} \min _ {p (k), Y} Y \\ \text { subject   to: } \sum_ {k \in S} p (k) = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in W \end{array}
$$

$$
\begin{array}{l} \sum_ {k \in S} p (k) + \hat {\delta} _ {b} = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in \hat {L} \\ \sum_ {k \in S} p (k) \geq b _ {i} (S) \quad \forall   b = b _ {i} (S) \in L \setminus \hat {L} \\ p (k) = \hat {p} (k) \quad \forall   k \in \widehat {\mathcal {K}} \\ 0 \leq p (k) \leq Y \quad \forall   k \in \mathcal {K} \setminus \widehat {\mathcal {K}}. \end{array}\tag{A4}
$$

Let $Y ^ { * } , \mathcal { P } ^ { * }$ be the solution of (A4) and let $\mathcal { K } ^ { \ast } : = $ -k $p ^ { * } ( k ) = Y ^ { * } \}$ . Now, RAD would fix the prices for all bids in $\mathcal { K } ^ { * }$ and proceed. Again, if $\mathcal { K } ^ { \ast }$ contains more than one element, some of these prices may still be lowered and this is very likely to happen when using a simplex-based LP solver. This can be illustrated by the following examples.

Consider an auction with three items A, B, and C and four currently active bids from different bidders $b _ { 1 } ( \mathrm { A } ) = 5 5 , \ b _ { 2 } ( \mathrm { C } ) = 5 5 , \ b _ { 3 } ( \mathrm { A B } ) = 4 0 ,$ and $b _ { 4 } ( \mathrm { B C } ) = 4 0$ Obviously, the provisional winners are 1 and 2 and $\hat { L } = \varnothing$ . After removing redundant inequalities, the linear program (A4) looks like:

$$
\begin{array}{c} \min _ {p (B), Y} Y \\ \text { subject   to: } p (A) = 5 5 \\ p (C) = 5 5 \\ 5 5 \leq Y \\ 0 \leq p (B) \leq Y. \end{array}
$$

We can get two possible solutions of this problem when using a simplex-based LP solver: $\{ p ^ { * } ( \mathtt { B } ) =$ $5 5 , Y ^ { * } = 5 5 \}$ or $\{ p ^ { * } ( \mathtt { B } ) = 0 , Y ^ { * } = 5 5 \}$ . In the first case, RAD would fix all prices to 55, which would distort the bidder’s understanding of the current demand for the item B.

Another important point is the balancing method used. RAD proposes maximizing minimal price instead of minimizing maximum price. However, if the solver finds the second solution, RAD would fix $\hat { p } ( \mathrm { A } ) = 5 5$ and $\hat { p } ( \mathrm { C } ) = 5 5$ and then yield $p ^ { * } ( \mathtt { B } ) = \infty$ in the next iteration.

Now, consider another auction with three items $\scriptstyle \mathbf { A } ,$ $\mathrm { { B } , C }$ and two currently active bids $b _ { 1 } ( \mathrm { A B C } ) = 1 6 0$ and $b _ { 2 } ( \mathrm { A } ) = 7 0$ , where the provisional winner is 1 and again $\hat { L } = \varnothing$ . The linear program (A4) looks like:

$$
\begin{array}{l} \min _ {p (\mathrm{A}),   (\mathrm{B}),   p (\mathrm{C}),   Y} Y \\ \text { subject   to: } p (\mathrm{A}) + P (\mathrm{B}) + P (\mathrm{C}) = 1 6 0 \end{array}
$$

$$
\begin{array}{l} p (\mathrm{A}) \geq 7 0 \\ 0 \leq p (\mathrm{A}), p (\mathrm{B}), P (\mathrm{C}) \leq Y. \end{array}
$$

With a simplex-based solver, this would yield one of two possible solutions: $\{ p ^ { * } ( \mathrm { A } ) = 7 0 , \ p ^ { * } ( \mathrm { B } ) = 2 0$ $p ^ { * } ( \mathsf C ) = 7 0 , \ Y ^ { * } = 7 0 \}$ or $\{ p ^ { * } ( \mathrm { A } ) = 7 0 , p ^ { * } ( \mathrm { B } ) = 7 0 .$ $p ^ { * } ( \mathrm { C } ) = 2 0 , \ Y ^ { * } = 7 0 \}$ . In both cases, RAD would stop with this solution. There are no reasons why the prices for the items B and C are different.

To avoid the pitfalls illustrated in the above examples, ALPS continues by bounding the prices to $Y ^ { * }$ and minimizes the sum of all prices in $\mathcal { K } ^ { * }$ as follows:

$$
\begin{array}{l} \min _ {p (k)} \sum_ {k \in \mathcal {K} ^ {*}} p (k) \\ \text { subject   to: } \sum_ {k \in S} p (k) = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in W \\ \sum_ {k \in S} p (k) + \hat {\delta} _ {b} = b _ {i} (S) \quad \forall   b = b _ {i} (S) \in \hat {L} (\mathrm{A5}) \\ \sum_ {k \in S} p (k) \geq b _ {i} (S) \quad \forall   b = b _ {i} (S) \in L \setminus \hat {L} \\ p (k) = \hat {p} (k) \quad \forall   k \in \widehat {\mathcal {K}} \\ 0 \leq p (k) \leq Y ^ {*} \quad \forall   k \in \mathcal {K} \setminus \widehat {\mathcal {R}}. \end{array}
$$

If at least one of the prices in $\mathcal { K } ^ { \ast }$ can be lowered, this will be done by (A5). We now remove all items with lowered prices from $\mathcal { K } ^ { \ast }$ and repeat with (A5) until no more prices can be improved. At this point, we set $\widehat { \mathcal { K } } : = \widehat { \mathcal { K } } \dot { \cup } \mathcal { K } ^ { * }$ , fix all nonimprovable prices $( \forall k \in$ $\mathcal { K } ^ { * }$ set ${ \hat { p } } ( k ) : = p ^ { * } ( k ) )$ , and continue with (A4) unless $\mathcal { K } \backslash \widehat { \mathcal { K } } = \emptyset$ . In our example, the algorithm terminates after one iteration with prices $\{ p ^ { * } ( \mathrm { A } ) = 7 0 , p ^ { * } ( \mathrm { B } ) =$ $4 5 , p ^ { * } ( \mathsf C ) = 4 5 \}$ , which better describes the competitive situation.

## Appendix B. ALPS Surplus Eligibility

ALPS is also based on the RAD eligibility rules. A bidder’s eligibility $e _ { i } ^ { t }$ is the number of distinct objects he is allowed to bid on in a round. In the simultaneous multiround auction and RAD, a collection of bids is eligible if the new bids plus last round’s winning bids are placed on no more items than the eligibility $e _ { i } ^ { t - 1 }$ These rules, however, can also lead to inefficiencies. For example, when items in the auction vary significantly in price, bidders may want to replace a single expensive item by a set of cheaper items. This is typically the case in transportation, when bidders give up bidding on the shortest route and start bidding on a detour. In ALPS, we extend the RAD eligibility rules with the surplus eligibility in order to account for these cases.

Surplus eligibility s<sup>t</sup> gives each bidder i a chance to increase his round t eligibility $e _ { i } ^ { t } .$ . To retain the original purpose of enforcing activity in the auction, size of the surplus eligibility is directly bound to the bidder’s market activity in the auction so far. The surplus eligibility $s _ { i } ^ { t }$ for each bidder is calculated in each round and is communicated to the bidders along with prices and the provisional allocation. In round $t , \mathsf { a }$ bidder is allowed to bid maximally on as many distinct items as he bid in the last round plus surplus eligibility:

$$
e _ {i} ^ {t} \leq e _ {i} ^ {t - 1} + s _ {i} ^ {t}.
$$

To determine the value $u _ { i } ^ { t } ,$ we propose a measure for a bidder’s market activity, where we want to avoid situations in which bidders can pretend activity by submitting deliberately losing bids. For this purpose, we introduce the notion of bid volume of bidder i in round t:

$$
\begin{array}{l l} r _ {i} ^ {t} = \sum_ {k \in \mathcal {K}} m _ {i} ^ {t} (k) & (\text { round   bid   volume }) \\ u _ {i} = \sum_ {t = 1} ^ {T} r _ {i} ^ {t} & (\text { total   bid   volume }). \end{array}
$$

Function $m _ { i } ^ { t } ( k )$ determines an optimistic estimator for the bid price of a bidder for the single item k based on bidder $i ^ { \prime } \mathrm { s }$ package bids in round t. For each bid $b _ { i } ^ { t } ( S ) .$ , the bid price for all $k \in S$ is determined by splitting the bundle bid price to individual items proportionally to item ask prices. For each item, the maximum over all bids is taken. In other words, $m _ { i } ^ { t } ( k )$ describes how much item k is worth to bidder i in round t.

A simple example illustrates this. Consider an auction with three items $\begin{array} { r } { \mathsf { A } , \mathsf { B } , } \end{array}$ and C and linear prices in round t, respectively, 10, 10, and 20. If bidder i submits a bid on the bundle $( \mathrm { A } , \mathrm { B } , \mathrm { C } )$ for 50, the bid price is split proportionally to ask prices, resulting in values 12.5, 12.5, and 25 for $\begin{array} { r } { \operatorname { A } , \ \operatorname { B } , } \end{array}$ and $C ,$ respectively. Let his second (and last) bid in the round t be 30 on the bundle $( \mathtt { B } , \mathsf { C } ) .$ , which splits proportionally to ask prices as 10 for B and 20 for C. In this case, we obtain:

$$
\begin{array}{c} {m _ {i} ^ {t} (\mathrm{A}) = 1 2. 5} \\ {m _ {i} ^ {t} (\mathrm{B}) = \max (1 0, 1 2. 5) = 1 2. 5} \\ {m _ {i} ^ {t} (\mathrm{C}) = \max (2 0, 2 5) = 2 5.} \end{array}
$$

The total bid volume $u _ { i }$ equals the sum of $r _ { i } ^ { t }$ over all auction rounds and represents the overall bid volume that bidder i generated in the auction so far. Further bidders are ranked by their $u _ { i }$ in ascending order. The rank for bidder $i ,$ denoted by $u _ { i } ,$ is the index of the position in the ordered sequence of this bidder’s $u _ { i }$ minus one. The surplus eligibility is then calculated as:

$$
s _ {i} ^ {t} = \text { round } \left(\left(\frac {w _ {i}}{| \mathscr {I} | - 1}\right) \cdot s _ {\max}\right).
$$

The value $w _ { i } / ( | \mathcal { I } | - 1 )$ is scaled between 0 1 and serves as an indicator for market activity. $s _ { \mathrm { m a x } }$ is the maximal surplus eligibility defined by the auctioneer. The fact that bidders’ activity can be accumulated throughout the auction sets incentives for bidders to bid actively right from the start. We found surplus eligibility to have a significant positive effect on efficiency in the transportation value model.

## Appendix C. ALPS Termination Rules

The termination rule is central to an auction design. The RAD design (Kwasnica et al. 2005) has an eligibility-based stopping rule and enforces minimum bid increments. As illustrated below, this is not always sufficient to ensure auction termination. One of the other stopping rules, defined in the RAD auction design, is an identical provisional allocation in two consecutive rounds. However, the approximative nature of linear ask prices in RAD in combination with this termination rule can result in inefficient allocations. Consider an example auction with valuations $v _ { i } ( S )$ in Table C.1 and minimum increment of two monetary units (MU). The efficient outcome would be to sell A to Bidder1 and -B C to Bidder2. Let two bids (Table C.2) be active at some point during the auction. Table C.3 shows the resulting ask prices.

Bidder2 does not win in the provisional allocation so he must submit another bid. He now has to choose between 27 [115 115 2 2] for -A B and 23 [116 $7 . 5 + 2 + 2 ]$ for -B C. As he has equal valuations for both combinations, the second alternative is selected. The next round bids are depicted in Table C.4.

Table C.1

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td><td>AB</td><td>AC</td><td>BC</td><td>ABC</td></tr><tr><td>Bidder1</td><td>10</td><td></td><td></td><td></td><td></td><td></td><td>35</td></tr><tr><td>Bidder2</td><td></td><td></td><td></td><td>32</td><td></td><td>32</td><td></td></tr></table>

Table C.2

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td><td>AB</td><td>AC</td><td>BC</td><td>ABC</td></tr><tr><td>Bidder1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>30.5</td></tr><tr><td>Bidder2</td><td></td><td></td><td></td><td>23</td><td></td><td></td><td></td></tr></table>

Table C.3

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Price</td><td>11.5</td><td>11.5</td><td>7.5</td></tr></table>

Table C.4

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td><td>AB</td><td>AC</td><td>BC</td><td>ABC</td></tr><tr><td>Bidder1</td><td></td><td></td><td></td><td></td><td></td><td></td><td>30.5</td></tr><tr><td>Bidder2</td><td></td><td></td><td></td><td></td><td></td><td>23</td><td></td></tr></table>

This is the second round with the same provisional allocation and, consequently, the auction will be terminated with Bidder1 receiving all three items. Obviously, this is not an efficient outcome. For Bidder2, the auction termination comes as a surprise; from his point of view, he was still ready to submit higher bids.

A naïve approach of removing this termination rule and relying only on the eligibility-based principle (Kwasnica et al. 2005) causes other problems. Continuing the above example, ask prices in the new round will change to the values in Table C.5.

At this point, the Bidder2 can again bid 23 MU on the package -A B and the auction might iterate without stopping at all. The reason for this infinite loop is the possibility of ask prices falling (nonmonotonicity).

In order to avoid these problems, we suggest omitting the auction stopping rule based on two successive identical allocations and introduce alternative rules to prevent auctions from looping:

• Increase the minimum increment with each equal allocation but reset the minimum increment to the original value if the allocation changes (ALPS).

• Request every bidder to outbid own bids, which were submitted previously on the same bundle (ALPSm).

Table C.5

<table><tr><td>Item</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Price</td><td>7.5</td><td>11.5</td><td>11.5</td></tr></table>

If the losing bidder’s valuation is high enough, both rules will eventually cause the allocation to change. Otherwise, the losing bidder will eventually stop bidding and the auction will end.

## References

Adomavicius, D., A. Gupta. 2005. Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2) 169–185.

An, N., W. Elmaghraby, P. Keskinocak. 2005. Bidding strategies and their impact on revenues in combinatorial auctions. J. Revenue Pricing Management. 3(4) 337–357.

Anandalingam, G., R. W. Day, S. Raghavan. 2005. The landscape of electronic market design. Management Sci. 51(3) 316–327.

Ausubel, L. 2006. An efficient dynamic auction for heterogeneous commodities. Amer. Econom. Rev. 96(3) 602–629.

Ausubel, L., P. Milgrom. 2002. Ascending auctions with package bidding. Frontiers Theoret. Econom. 1 1–42.

Ausubel, L., P. Milgrom. 2006a. Ascending proxy auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Ausubel, L., P. Milgrom. 2006b. The lovely but lonely Vickrey auction. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Ausubel, L., P. Crampton, P. Milgrom. 2006. The clock-proxy auction: A practical combinatorial auction design. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Bichler, M., A. Davenport, G. Hohner, J. Kalagnanam. 2006. Industrial procurement auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Bikhchandani, S., J. M. Ostroy. 2002. The package assignment model. J. Econom. Theory 107(2) 377–406.

Bikhchandani, S., J. M. Ostroy. 2006. From the assignment model to combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Carlsson, P., A. Andersson. 2007. A flexible model for treestructured multi-commodity markets. J. Electronic Commerce Res. 7(1) 337–357.

Cramton, P. 1998. Ascending auctions. Eur. Econom. Rev. 42(3–5) 745–756.

Cramton, P., R. McMillan, P. Milgrom, B. Miller, B. Mitchell, D. Vincent, R. Wilson. 1998. Simultaneous ascending auctions with package bidding. Report to the Federal Communications Commission, Charles River and Associates.

Cramton, P., Y. Shoham, R. Steinberg, eds. 2006. Combinatorial Auctions. MIT Press, Cambridge, MA.

Day, R. 2004. Expressing preferences with price-vector agents in combinatorial auctions. Ph.D. thesis, University of Maryland, College Park, MD.

de Vries, S., J. Schummer, R. Vohra. 2007. On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132(1) 95–118.

Drexl, A., K. Jornsten, D. Knof. 2005. Non-linear anonymous pricing in combinatorial auctions. Working paper, Christian-Albrechts-Universität, Kiel, Germany.

Dunford, M., K. Hoffman, D. Menon, R. Sultana, T. Wilson. 2007. Testing linear pricing algorithms for use in ascending combinatorial auctions. Technical report, George Mason University, Fairfax, VA.

Elmaghraby, W., P. Keskinocak. 2002. Technology for transportation bidding at the Home Depot. Kluwer’s Internatioal Series in Operations Research and Management Science. Kluwer Academic Publishers, Dordrecht, The Netherlands.

Fan, M., J. Stallaert, A. Whinston. 2003. Decentralized mechanism design for supply chain organizations using auction market. Inform. Systems Res. 14(1) 1–22.

Federal Communications Commission. 2002. Auction of licenses in the 747–762 and 777–792 MHz bands scheduled for June 19, 2002. Technical report, Federal Communications Commission, Public Notice (DA 02-260), Washington, D.C.

Hoffman, K., D. Menon, A. Heever. 2005. A bidder aid tool for dynamic package creation in the FCC spectrum auctions. Working paper, George Mason University, Fairfax, VA.

Jones, J., G. Koehler. 2005. A heuristic for winner determination in rule-based combinatorial auctions. INFORMS J. Comput. 17(4) 475–489.

Kelly, F., R. Steinberg. 2000. A combinatorial auction with multiple winners for universal service. Management Sci. 46(4) 586–596.

Kelso, A. S., V. P. Crawford. 1982. Job matching, coalition formation, and gross substitute. Econometrica 50 1483–1504.

Kwasnica, T., J. O. Ledyard, D. Porter, C. DeMartini. 2005. A new and improved design for multiobjective iterative auctions. Management Sci. 51(3) 419–434.

Kwon, R. H., G. Anandalingam, L. H. Ungar. 2005. Iterative combinatorial auctions with bidder-determined combinations. Management Sci. 51(3) 407–418.

Lehmann, D., R. Mueller, T. Sandholm. 2006. The winner determination problem. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA, 297–317.

Leyton-Brown, K., E. Nudelman, Y. Shoham. 2006. Empirical hardness models for combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA, 478–504.

Leyton-Brown, K., M. Pearson, Y. Shoham. 2000. Towards a universal test suite for combinatorial auction algorithms. ACM Conf. Electronic Commerce EC-2000. ACM SIGecom, New York, 66–76.

Milgrom, P. R., R. J. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50(5) 1089–1122.

Mishra, D., D. Parkes. 2007. Ascending price Vickrey auctions for general valuations. J. Econom. Theory 132(1) 335–366.

Nemhauser, G. L., L. A. Wolsey. 1988. Integer and Combinatorial Optimization. Wiley-Interscience Series in Discrete Mathematics and Optimization, John Wiley and Sons, Inc., New York.

Nisan, N. 2000. Bidding and allocations in combinatorial auctions. ACM Conf. Electronic Commerce EC-2000. ACM SIGecom, New York, 1–12.

Parkes, D. 2001. Iterative combinatorial auctions: Achieving economic and computational efficiency. Ph.D. thesis, University of Pennsylvania, Philadelphia.

Parkes, D. 2006. Iterative combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Parkes, D., L. H. Ungar. 2000. Iterative combinatorial auctions: Theory and practice. 17th National Conf. Artificial Intelligence AAAI-00. AAAI Press, Menlo Park, CA, 74–81.

Pikovsky, A., M. Bichler. 2005. Information feedback and decision support in interative combinatorial auctions. Wirtschaftsinformatik. Springer, Bamberg, Germany, 329–348. [Also available at http://ibis.in.tum.de/staff/pikovsky/index.htm.]

Plummer, C. L. 2003. Bidder response to combinatorial auctions in truckload procurement. Master’s thesis, Massachusetts, Institute of Technology, Cambridge, MA.

Porter, D., S. Rassenti, A. Roopnarine, V. Smith. 2003. Combinatorial auction design. Proc. National Acad. Sci. PNAS 100 11153–11157.

Rassenti, S., V. L. Smith, R. L. Bulfin. 1982. A combinatorial auction mechanism for airport time slot allocations. Bell J. Econom. 13 402–417.

Rothkopf, M. H., A. Pekeˇc, R. M. Harstad. 1998. Computationally manageable combinatorial auctions. Management Sci. 44(8) 1131–1147.

Sandholm, T., C. Boutilier. 2006. Preference elicitation in combinatorial auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA, 233–263.

Schoenherr, T., V. A. Mabert. 2006. Bundling for B2B procurement auctions: Current state and best practices. Internat. J. Integrated Supply Management 2(3) 189–213.

Shabalin, P., B. Laqua, A. Pikovsky. 2007. Improved rules for the resource allocation design. Proc. 9th IEEE Internat. Conf. E-Commerce Tech. IEEE, Washington, D.C., 232–330.

Song, J., A. C. Regan. 2002. Combinatorial auctions for transportation service procurement: The carrier perspective. Transportation Res. Record 1833 40–46.

Sureka, A., P. Wurman. 2005. Applying metaheuristic techniques to search the space of bidding strategies in combinatorial auctions. Genetic Evolutionary Comput. Conf. ACM, New York, 2097–2103.

Wurman, P., M. Wellman. 2000. Akba: A progressive, anonymousprice combinatorial auction. ACM Conf. Electronic Commerce. ACM, New York, 21–29.

Xia, Mu, G. J. Koehler, A. B. Whinston. 2004. Pricing combinatorial auctions. Eur. J. Oper. Res. 154(1) 251–270.
