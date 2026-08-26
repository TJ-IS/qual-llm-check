---
otero_id: 9098
otero_key: "4G77YTNT"
title: "An Experimental Comparison of Linear and Nonlinear Price Combinatorial Auctions"
authors: "Tobias Scheffel; Alexander Pikovsky; Martin Bichler; Kemal Guler"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0267"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/4G77YTNT/fulltext/images/67e51a7518b46aa05dbe178d5adee462013991b843f361ab1b11a3ee10670e4b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# An Experimental Comparison of Linear and Nonlinear Price Combinatorial Auctions

Tobias Scheffel, Alexander Pikovsky, Martin Bichler, Kemal Guler,

## To cite this article:

Tobias Scheffel, Alexander Pikovsky, Martin Bichler, Kemal Guler, (2011) An Experimental Comparison of Linear and Nonlinear Price Combinatorial Auctions. Information Systems Research 22(2):346-368. http://dx.doi.org/10.1287/isre.1090.0267

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/4G77YTNT/fulltext/images/837e60685d5e36cf241f76a16002becdd71dc5310da807595f4e9d6b2252e8a6.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Experimental Comparison of Linear and Nonlinear Price Combinatorial Auctions

Tobias Scheffel, Alexander Pikovsky, Martin Bichler

Internet-Based Information Systems, Department of Informatics, Technische Universität München, 85478 München, Germany {scheffel@in.tum.de, pikovsky@in.tum.de, bichler@in.tum.de}

Kemal Guler Hewlett-Packard Laboratories, Palo Alto, California 94304, kemal.guler@hp.com

ombinatorial auctions are used for the efficient allocation of heterogeneous goods and services. They require appropriate software platforms that provide automated winner determination and decision support for bidders. Several promising ascending combinatorial auction formats have been developed throughout the past few years based on primal-dual algorithms and linear programming theory. The ascending proxy auction and iBundle result in Vickrey payoffs when the coalitional value function satisfies buyer submodularity conditions and bidders bid their best responses. These auction formats are based on nonlinear and personalized ask prices. In addition, there are a number of designs with linear prices that have performed well in experiments, the approximate linear prices auction, and the combinatorial clock auction. In this paper, we provide the results of lab experiments that tested these different auction formats in the same setting. We analyze aggregate metrics such as efficiency and auctioneer revenue for small- and medium-sized value models. In addition, we provide a detailed analysis not only of aggregate performance metrics but also of individual bidding behaviour under alternative combinatorial auction formats.

Key words: laboratory experiments; electronic markets and auctions; decision support systems History: Paulo Goes, Senior Editor; Yong Tan, Associate Editor. This paper was received on July 2, 2008, and was with the authors 2 <sup>1</sup> months for 2 revisions. Published online in Articles in Advance February 1, 2010.

## 1. Introduction

The design and analysis of online auction mechanisms, more specifically combinatorial auctions, has been an emerging strand in the decision support and information systems (IS) literature (Banker and Kauffman 2004). Literature in computer science, operations research, and economics provides valuable results regarding the computational complexity of winner determination problems, the communication complexity of combinatorial auctions, and the nonexistence of linear ask prices in such auctions. These results show that auctions that allow for package bids are challenging for the auctioneer and the bidders. The IS literature has been rich in proposals for practical auction designs, bidder decision support, new applications, and the analysis of bidder behavior in combinatorial auctions (see also Adomavicius and Gupta 2005; Bapna et al. 2000, 2001; Bichler et al. 2009; Fan et al. 2003; Kelly and Steinberg 2000; Xia et al. 2004). This paper is in line with previous IS research and focuses on the bidding behavior in combinatorial auctions. We report the results of our lab experiments and focus on some of the main combinatorial auction designs currently discussed in the literature.

Throughout the past few years, there have been multiple proposals on the design of efficient combinatorial auctions. The Vickrey-Clarke-Groves (VCG) auction is a unique auction with a dominant-strategy property that leads to efficient outcomes and takes only a zero payment from losing bidders (Ausubel et al. 2006, p. 93). Though the VCG auction assumes a central place in the mechanism design literature, the solutions can be outside the core<sup>1</sup> when goods are not substitutes. When the Vickrey payoff is not in the core, the seller’s Vickrey revenue is uncompetitively low. This opens up nonmonotonicity problems and possibilities for collusion and shill bidding (see Ausubel and Milgrom 2006b, Rothkopf 2007 for a more detailed discussion).

According to Porter et al. (2003), “experience in both the field and laboratory suggest that in complex economic environments iterative auctions, which enhance the ability of the participant to detect keen competition and learn when and how high to bid, produce better results than sealed bid auctions” (p. 11154). Several authors have tried to develop indirect auctions with strong incentive properties (even if they do not have a dominant strategy) to overcome these problems. In iterative combinatorial auctions, bidders do not have to reveal their true preferences on all possible bundles in one round as would be necessary in VCG mechanisms (Ausubel and Milgrom 2006b). Traditional English auctions are strategically simpler than “first-price sealed-bid” auction designs (Vickrey 1961). Finally, Milgrom and Weber (1982) have shown for single-item auctions that if there is affiliation in the bidders’ valuations, sealed-bid auctions are less efficient than iterative auctions. It is easy to see that the single-item English auction implements a Vickrey outcome under the assumptions of the independent private values model, but this is not true in general for iterative combinatorial auctions.

Much research on iterative combinatorial auctions (ICAs) is based on the linear programming theory and combinatorial optimization. Primal-dual algorithms and subgradient algorithms have been used as conceptual frameworks to design a number of iterative and ascending combinatorial auctions such as iBundle<sup>2</sup> (Parkes and Ungar 2000), dVSV (de Vries et al. 2007), and the ascending proxy auction (Ausubel and Milgrom 2006a). In these designs, prices are interpreted as feasible dual solutions. In the following, we will refer to these three auction designs as primal-dual auction designs 4PDAs5.

There are solid theoretical results on the efficiency of primal-dual auctions in the case of best-response bidding but hardly any empirical results. In contrast, there is no formal equilibrium analysis for linear price auctions, but there is some initial empirical evidence from lab experiments on selected auction formats with linear prices (Kwasnica et al. 2005, Porter et al. 2003). Linear price auction formats have also been analyzed in computational experiments for the purpose of sensitivity analysis with respect to different bidding stategies and value models (Bichler et al. 2009, Schneider et al. 2008). It is easy to construct examples in which linear price auctions are not 100% efficient. However, they performed well in the lab and in the case of different bidding strategies in computational experiments with realistic bidder valuations.

According to Roth (1988), “computer simulations are useful for creating and exploring theoretical models, while experiments are useful for observing behaviour” (p. 1000). Iterative combinatorial auctions are IT-based economic mechanisms and the decision support provided to bidders (such as the provision of certain types of ask prices in every round) can well impact the performance of these mechanisms in the field. Lab experiments are an excellent method to observe human bidding behavior and an important complement to theoretical and computational models. In this paper, we compare the results of a nonlinear discriminatory price auction (iBundle) to those of the VCG auction and those of combinatorial auction formats with linear prices, namely, “Approximate Linear PriceS” (ALPS)<sup>3</sup> (Bichler et al. 2009) and the combinatorial clock auction (Porter et al. 2003) in laboratory experiments. We analyzed valuations that satisfy buyer submodularity conditions, where theory predicts best-response bidding and Vickrey payoffs for iBundle, as well as more general valuations, where theory has little to say as of yet for all of the above auction formats. Allocative efficiency, revenue distribution, and speed of convergence were the main criteria in our analysis.

## 1.1. Previous Studies

A number of experimental studies have focused on combinatorial auctions and their comparison to simultaneous or sequential auctions. Banks et al. (1989) analyzed various mechanisms including the adaptive user selection mechanism (AUSM) and found Combinatorial auctions (CAs) to exhibit higher efficiency than traditional auctions in the presence of superadditivity. In line with this research, Ledyard et al. (1997) compared the simultaneous ascending auction (SAA), sequential ascending auctions, and AUSM and found that in the case of exposure problems, AUSM led to a significantly higher efficiency than the other two formats. Banks et al. (2003) did another analysis on the SAA and ascending auctions having package bidding and also found package bidding to achieve higher efficiency for valuations with complementarities.

Porter et al. (2003) compared the SAA against a design by Charles River and Associates and the combinatorial clock auction, and found that the clock design achieved the highest efficiency and was simple for bidders to use. Kwasnica et al. (2005) described the resource allocation design (RAD) and compared it to SAA. They found that in environments with complementarities, RAD significantly increased efficiency plus RAD had a lower number of auction rounds. In additive environments without complementarities, package bidding rarely occured and no significant differences in efficiency and seller revenue could be found.

Kazumori (2005) analyzed the SAA, the VCG mechanism, and the clock proxy auction. He conducted experiments with students and professional traders and confirmed the previous studies that when there are significant complementarities, bundle bidding leads to higher efficiency than the SAA. He also found, however, that when there are coordination problems, package bidding may be less powerful. The clock proxy auction outperformed both the SAA and the VCG auctions while the SAA outperformed the clock proxy auction for additive value structures. Kazumori (2005) also found professional traders to have higher payoffs than students on average. In another recent study, Chen and Takeuchi (2008) compared the VCG auction and iBEA in experiments in which humans competed against artificial bidders. Here, the sealed bid VCG auctions generated significantly higher efficiency and revenue than the iBEA auctions. Participants in the VCG auctions either underbid or bid their true values.

Goeree and Holt (2009) recently performed experiments for the U.S. Federal Communications Commission (FCC) in which they compared SAA and a modified version of RAD against hierarchical package bidding (HPB), a design for large combinatorial auctions where the auctioneer restricts bidders to bid on a few preselected bundles. The value model in these experiments included 18 items, which would allow for 262,143 possible bundle bids. The tested HPB design reduced this set to bids on the 18 individual licenses and only 4 bundle bids, which needed to be hierarchically structured. In these experiments, which were focused on the allocation problem of the FCC, HPB achieved the highest efficiency and revenue followed by RAD and then SAA. HPB is designed for large-scale combinatorial auctions in which it is possible for the auctioneer to suggest a hierarchical structuring of bundles that fits the bidders’ preferences. If this is not the case, the design can lead to exposure problems and low efficiency. Though the simplicity of HPB has a number of advantages for application domains such as the FCC spectrum auctions, in this paper we will focus on the efficiency of fully combinatorial auctions that allow bidding on all possible bundles. We did, however, include the value model VM5 in our experiments to analyze, whether some of the experimental results of the value models with up to nine items carry over to larger value models. VM5 is largely based on the experimental design in Goeree and Holt (2009), except from limitations of the bidders on the number of items they can win, which are specific to the FCC setting. This way, we could compare the results of VM5 to those of the plain combinatorial auctions with smaller value models, where no such limits existed. Additional results of related experiments for the FCC setting can be found in Brunner et al. (2009).

## 1.2. Contribution and Outline of the Paper

Let us briefly summarize the contributions of this paper. First, this is the first lab experiment that investigates a number of fundamentally different iterative auction designs with linear and nonlinear prices (combinatorial clock, ALPS, iBundle) and the VCG auction in the same setting, based on the same software platform with minimal differences in the user interface across auction formats. iBundle, a design with nonlinear personalized prices, has not been tested experimentally so far, although it has strong game theoretical properties.

Second, we analyze small- (3 and 6 items) to medium-sized (9 and 18 items) auctions and their impact on auction performance metrics. Though we do not want to generalize the results to large-scale auctions and all types of value models, the results provide helpful evidence on the efficiency of fully combinatorial auctions with a variety of different small- and medium-sized value models. We believe that it is important to understand simpler settings before we explore large value models.

Third, we provide a detailed analysis not only of aggregate performance metrics but also of individual bidding behavior in combinatorial auctions. This analysis reveals that bidders do not follow best-response strategies in any of the auction formats. Best-response bidding has been widely used as an assumption in theoretical work. Although it is not surprising that bidders do deviate from such behavior (rationally or irrationally), the relative incidence of such deviations under alternative formats is an important design issue. Though computational experiments establish the potential impact of deviations from best-response bidding, in a lab experiment we can account for the fact that best responding itself is a task difficulty that depends on the format. Until now, there was almost no literature on individual bidding behavior in combinatorial auctions, although realistic expectations about bidding behavior in complex auctions are vital for the development of practical auction designs.

It was interesting to see that bidders did not seem to follow pure best-response strategies in any of the auction formats, not even in iBundle where there are game-theoretical incentives to do so. This motivates the issue of robustness of combinatorial auction formats against nonbest-response bidding (Schneider et al. 2008). Also, the experiments confirm that the number of auction rounds in iBundle can be prohibitive in practical settings, even for auctions with only six items. As in previous studies (Bichler et al. 2009, Porter et al. 2003), linear price auctions achieved high levels of efficiency, which calls for more research in this area.

The rest of the paper is organized as follows. In §2, we describe the economic environment and the auction mechanisms, and review the theory on linear and nonlinear price auctions. Section 3 describes the experimental design. Section 4 describes the response variables and summarizes a number of hypotheses for our study. In $\ S 5 ,$ , we discuss the experimental results. Section $\check { 6 }$ provides conclusions and an outlook on future research in this area.

## 2. Economic Environment and

## Auction Mechanisms

For a discussion of the related theory to iterative combinatorial auctions, we refer the reader to Bichler et al. (2009).

## 2.1. Economic Environment and Notation

In the following, we will limit ourselves to describing the basic notation and concepts that are used in this paper. Let $\mathcal { K } = \{ 1 , \dots , m \}$ denote the set of items indexed by k and ${ \mathcal { I } } = \{ 1 , \ldots , n \}$ denote the set of bidders indexed by i with private valuations $v _ { i } ( S ) \geq 0$ for bundles $S \subseteq { \mathcal { K } }$ . This means that each bidder i has a valuation function $v _ { i } ( S ) \colon 2 ^ { \mathcal { K } } \to \mathbb { R } _ { 0 } ^ { + }$ that attaches a value $v _ { i } ( S )$ to any bundle $S \subseteq \mathcal { K }$ . In addition, we assume that values $v _ { i } ( S )$ are independent, private, and satisfy the free disposal $( { \mathrm { i f ~ } } S \subset T ,$ , then $v _ { i } ( S ) \leq$ $v _ { i } ( T ) )$ . Last, the bidders’ utility function $( \pi _ { i } )$ is quasilinear $( \pi _ { i } ( S , \mathcal { P } _ { \mathrm { p a y } } ) : = v _ { i } ( S ) - p _ { \mathrm { p a y } , i } ( S ) , \pi _ { i } ( \emptyset , \mathcal { P } _ { \mathrm { p a y } } ) : = 0 )$ where $\mathcal { P } _ { \mathrm { p a y } }$ denotes the price set.

Different pricing schemes have been discussed for combinatorial auctions in the literature, including linear, nonlinear, and nonlinear nonanonymous prices (see Xia et al. 2004 for a detailed discussion):

Definition 1. A set of prices $\mathcal { P } _ { \mathrm { a s k } } = \{ p _ { \mathrm { a s k } , i } ( S ) \}$ $i \in \mathcal { I } , S \subseteq \mathcal { K }$ is called

• linear (or additive) if

$$
\forall i, S \colon p _ {\mathrm{ask}, i} (S) = \sum_ {k \in S} p _ {\mathrm{ask}, i} (k)
$$

• anonymous if

$$
\forall i, j, S \colon p _ {\mathrm{ask}, i} (S) = p _ {\mathrm{ask}, i} (S)
$$

In other words, prices are linear if the price of a bundle is equal to the sum of the prices of its items, and prices are anonymous if prices of the same bundle are equal for every bidder. Nonanonymous ask prices are also called discriminatory prices.

Given an allocation $\ b X = ( S _ { 1 } , \ldots , S _ { n } )$ and price set $\mathcal { P } _ { \mathrm { p a y } } ,$ let $\pi _ { i } ( X , \mathcal { P } _ { \mathrm { p a y } } ) : = \pi _ { i } ( S _ { i } , \mathcal { P } _ { \mathrm { p a y } } )$ denote the payoff of bidder i for the bundle in the allocation $X ,$ and let $\pi _ { \mathrm { a l l } } ( X , { \mathcal P } _ { \mathrm { p a y } } ) : = \sum _ { i \in { \mathcal F } } \pi _ { i } ( X , { \mathcal P } _ { \mathrm { p a y } } )$ denote the total bidders’ payoff of all bidders. Furthermore, let $\begin{array} { r } { \Pi ( X , \mathcal { P } _ { \mathrm { p a y } } ) : = \dot { \sum } _ { S \subseteq \mathcal { K } , i \in \mathcal { I } } x _ { i } ( S ) p _ { \mathrm { p a y } , i } ( S ) } \end{array}$ denote the auctioneer’s revenue.

## 2.2. The Auction Designs

In the following, we will briefly introduce the combinatorial auction designs used in our lab experiments.

2.2.1. Vickrey-Clarke-Groves (Sealed Bid) Auction. The Vickrey-Clarke-Groves (VCG) auction, also called the generalized Vickrey auction, is a generalization of the classic Vickrey auction for multiple heterogeneous goods. Prior to the auction, bidders report their valuations $v _ { i } ( S )$ on all bundles $S \subseteq { \mathcal { K } }$ to the auctioneer who then determines the allocation and prices. This design assigns goods efficently and charges the bidders the opportunity costs of the items they win. Truthful bidding is a dominant strategy under the private values assumptions.

2.2.2. Nonlinear Price Auctions. iBundle uses nonanonymous and nonlinear prices. It calculates a provisional revenue maximizing allocation at the end of every round and increases the prices based on the bids of nonwinning (unhappy) bidders. Parkes and Ungar (2000) suggest different versions of iBundle called iBundle(2), iBundle(3), and iBundle(d). iBundle(3), which will be used in this paper, maintains personalized bundle prices throughout the auction. In every round, the prices for every unhappy $( \mathrm { i . e . , }$ , nonwinning) bidder are increased for every bundle on which he has submitted a bid.

2.2.3. Linear Price Auctions. The combinatorial clock auction 4CC auction5 described by Porter et al. (2003) utilizes anonymous linear prices called item clock prices. In each round, bidders express the quantities desired on the packages at the current prices. As long as demand exceeds supply for at least one item, the price clock “ticks” upward for those items (the item prices are increased by a fixed price increment) and the auction moves to the next round. If there is no excess demand and no excess supply, the items are allocated corresponding to the last round bids and the auction terminates. If there is no excess demand but there is excess supply (all active bidders on some item did not resubmit their bids in the last round), the auctioneer solves the winner auction run time. If the computed allocation does not displace any active last iteration bids, the auction terminates with this allocation; otherwise, the prices of the respective items are increased and the auction continues.

The resource allocation design 4RAD5 proposed by Kwasnica et al. (2005) also uses anonymous linear ask prices. However, instead of increasing the prices directly, the auction lets the bidders submit priced bids and calculates so-called pseudodual prices based on the linear programming (LP) relaxation of the combinatorial allocation problem (CAP) (Rassenti et al. 1982). Unless the LP relaxation is integral, RAD uses a restricted dual formulation to derive pseudodual prices after each auction round. In the next round, the losing bidders have to bid more than the sum of ask prices for a desired bundle plus a fixed minimum increment. However, RAD also faces a few design problems. Most importantly, the eligibility and termination rules can lead to premature termination and inefficiencies. Also, there are ways to further decrease the ask prices. ALPS is an ICA design that is based on pseudodual prices as in RAD but contains a number of additional rules (Bichler et al. 2009). The termination rule and the eligibility rules have been adapted. Additionally, the ask price calculation minimizes the pseudodual prices. In our lab experiments, we used the ALPSm version in which all bids submitted in one round remain active throughout the auction (Bichler et al. 2009).

## 3. Experimental Design

Our experimental design reflects the theoretical considerations described in the previous sections. We implement a 4 x 4 design. In the first dimension, we compare the four mechanisms: ALPS, the CC auction, iBundle, and the VCG auction. In addition to the auction design, the value model (i.e., bidder preferences) was the second factor in our experiments.

## 3.1. Value Models

We used 5 value models: 2 small models with only 3 items and 3 bigger ones with 6, 9, and 18 items. The small value models describe easy settings in which bidders have only one to three valuations. We want to contrast the bidding behavior in those settings with larger value models of up to 27 (VM4) or more bundles (VM5) of interest. Two of the value models (VM1 and VM3) that fulfill the bidders-are-substitutes and bidder submodularity conditions. We focus only on the bidder submodularity condition because, for ascending auctions, the bidders-are-substitutes condition is not sufficient to result in VCG prices. For all value models, we ran simulations with best-response bidding agents, as well as with heuristic bidding agents who randomly picked 3 out of their 5 best bundles or 3 out of their 10 best bundles in each round.<sup>4</sup> With a best-response bidding strategy, the value models VM1-4 would achieve the efficient allocation, which will serve as a benchmark for our laboratory experiments. VM5 is based on draws from a distribution so that the efficiency of a particular instance and best-response bidding also depends on this draw.

The first value model (VM1) follows an example by Dunford et al. (2007). Table 1 gives the individual valuations for each bidder. Note that we assume free disposal in the value models VM1 to VM4, i.e., if bidder

Table 1 Value Model VM1

<table><tr><td>Bundle</td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td></tr><tr><td>{A, B}</td><td>15.0</td><td>14.0</td><td>9.0</td><td>10.0</td></tr><tr><td>{C}</td><td></td><td>5.0</td><td></td><td>4.0</td></tr></table>

Table 2 Value Model VM2

<table><tr><td>Bundle</td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td></tr><tr><td>{A}</td><td>10.0</td><td>5.0</td><td>2.0</td><td></td></tr><tr><td>{B}</td><td>5.0</td><td>10.0</td><td>5.0</td><td></td></tr><tr><td>{C}</td><td>2.0</td><td>5.0</td><td>10.0</td><td></td></tr><tr><td>{A, B}</td><td></td><td></td><td></td><td>5.0</td></tr><tr><td>{B, C}</td><td></td><td></td><td></td><td>16.0</td></tr></table>

Table 3 Structure of the Value Model VM3

<table><tr><td></td><td colspan="2">Shoreline</td></tr><tr><td>A</td><td>B</td><td>C</td></tr><tr><td>D</td><td>E</td><td>F</td></tr></table>

1 wins bundle ABC in VM1, his value would be 15. Also, we assume that bidders can only consume one of these bundles. Thus, the valuation of bidder 4 on ABC would be 10, not 14.<sup>5</sup> In VM2 and VM4, we focus on the threshold problem with a different item count (3 and 9 items). The individual bidder valuations for VM2 are given in Table 2. They exhibit that bidders 1 and 3 have to coordinate their bids to outbid bidder 4.

VM3 fulfills the bidders-are-substitutes (BSC) and the bidder submodularity (BSM) conditions. It describes six pieces of land arranged in two rows on a shoreline (see Table 3). Bidders 1, 2, and 4 are interested in individual pieces or in bundles of two. All bundles of interest contain at least one lot at the shore. Bidder 3 is interested in larger bundles of size 2, 3, and 4. For bundles of size 3 and 4, he would also like to have two pieces of land at the shore. As you can see in the appendix, these valuations have both sub- and superadditivities.

In value model 4 (VM4), we have nine pieces of land and three bidders with a maximum bundle size of three. In addition, there is bidder 4 with bundles of size 4, 5, and 6. Each bidder has a different location (see Figure 1(a)) and, consequently, different bundles of interest that are close to his location (the valuations are given in the appendix).

This case exhibits a threshold problem for bidders 1, 2, and 3. In the efficient allocation (see Figure 1(b)) bidder 1 wins items A, D, and $G ;$ bidder 2 wins items

B, E, and H; and bidder 3 wins items C, F, and I. Bidder 4 has valuations on large bundles $( \mathrm { e . g . } , \mathrm { B } , \mathrm { C } ,$ E, F, H, and I) and bidders 1 to 3 have to coordinate their bids to outbid bidder 4.

We intentionally focused on smaller value models with up to nine items in our work. Without the understanding of bidding behavior in small auctions, problems of larger auctions are difficult to interpret. It is, however, interesting to see whether the results carry over to larger value models with more bidders. Therefore, we added another value model VM5 with 7 bidders and 18 items (licenses), modeled after an experiment that was used for the design of the spectrum auctions of the U.S. Federal Communications Commission (Goeree and Holt 2009). We have focused on comparisons of ALPS as an auction format with linear prices and the VCG for VM5 because we already had problems conducting iBundle with 6 or 9 items and we could not finish experiments with 18 items. In addition, we ran a set of experiments for the large value model VM5 without an automated payoff calculation to test for the impact of respective decision support.

In VM5, six regional bidders in an auction on spectrum licenses are each interested in four adjacent licenses of a national circle of licenses (A–L) and two licenses of a regional circle (M–R). For the national bidder, the 12 licenses of the national circle of licenses are relevant. This information is common knowledge, but it is not known which bidders were interested in a particular license. The smaller circle is useful to reduce earnings inequities among experimental subjects in cases where the national bidder wins all or a subset of licenses of the large circle. Bidders have zero values for the licenses that do not interest them. The values for the individual licenses are randomly determined based on draws from uniform distributions on the range indicated by Table 4.

The value distributions in this set of experiments (not the actual draws) are common knowledge among the experimental subjects. For both bidder types,

## Figure 1 Value Model VM4

(a) Structure of the value model including the location of each bidder

<table><tr><td>A Bidder 1</td><td>B Bidder 2</td><td>C Bidder 3,4</td></tr><tr><td>D</td><td>E</td><td>F</td></tr><tr><td>G</td><td>H</td><td>I</td></tr></table>

(b) The efficient allocation

<table><tr><td>A Bidder 1</td><td>B Bidder 2</td><td>C Bidder 3</td></tr><tr><td>D Bidder 1</td><td>E Bidder 2</td><td>F Bidder 3</td></tr><tr><td>G Bidder 1</td><td>H Bidder 2</td><td>I Bidder 3</td></tr></table>

Table 4 Range of Value Distributions for the Two Different Bidder Types in VM5

<table><tr><td>License</td><td>National bidder</td><td>Regional bidder</td></tr><tr><td>A–D</td><td>[0, 10]</td><td>[0, 20]</td></tr><tr><td>E–H</td><td>[0, 20]</td><td>[0, 40]</td></tr><tr><td>I–L</td><td>[0, 10]</td><td>[0, 20]</td></tr><tr><td>M–R</td><td>/</td><td>[0, 20]</td></tr></table>

the value of licenses in a bundle increases by 20% (with 2 licenses), 40% (with 3 licenses), 60% (with 4 licenses), and so on. The bundle containing 12 licenses increased by 220%. These complementarities occur among all licenses.

## 3.2. Bidder Decision Support

In our analysis, we use a simple decision support tool that relieves bidders of many simple payoff calculations they would otherwise have to do by hand. Subjects could enter their valuations on bundles of interest privately in this tool, and in each new auction round with a new vector of ask prices, their current payoff would be calculated automatically. This avoids calculation errors and allows bidders to focus on strategy rather than having to perform many calculations on paper. We believe that applications in the field will mostly provide this primitive decision support. In order to test for the impact of the tool, we have added an additional treatment for ALPS and VM5 (ALPS (without DSS)) without the automated payoff calculation. In our experiments with VM5, we have also provided bidders with a tool to privately calculate valuations for the potentially many bundles of interest.

## 3.3. Treatment Structure

In summary, the experiment had 19 possible treatments (see Table 5). For every treatment, four repeated experiments were conducted.

## 3.4. Experimental Procedures

All experiments with treatments 1 to 16 were conducted from June 2007 to August 2007; another set of experiments with treatments 17 to 19 was conducted in summer 2008 and winter 2008. The subjects were recruited using e-mail lists from the Technische Universitat (TU) München student population. Each auction in treatments 1 to 16 was conducted with 4 subjects while treatments 17 to 19 involved 7 subjects in each experiment. We have implemented the auction algorithms in a Web-based software system<sup>6</sup> and conducted the experiments in a computer lab at the Garching campus of the TU München.

Each session tested a single auction format but different value models. At the beginning of each session, each subject was given printed instructions. After the instructions were read aloud, subjects were encouraged to ask questions. The instruction period took 50 minutes on average. After receiving the instructions, we conducted one training auction in which the subjects could enhance their understanding of the auction mechanism. After the training, auction subjects took a quiz designed to test their understanding of the mechanism. At the end of the quiz, the experimenters went through the answers with the group of subjects. The quiz took 20 minutes on average. Subjects then randomly drew a PC terminal number and participated in another training auction to ensure that they were familiar with the market design and the user interface.

In each session of treatments 1 to 16, we conducted 4 auctions, each with a different value model. Each session was repeated four times with different subjects. The length of sessions varied from 3 to 4.5 hours depending on the auction format. In total, we ran 64 auctions with these treatments. The subjects were paid <sup>E</sup>5 as a show up fee and an additional <sup>E</sup>10 for successfully completing the quiz. The minimal payment per subject was <sup>E</sup>5 and the maximum payment was <sup>E</sup>80 depending on their payoff in the auctions. The average payment for bidders participating in the ALPS auctions was <sup>E</sup>40.17, <sup>E</sup>40.64 in the combinatorial clock auction, and <sup>E</sup>45.68 in the VCG auction. Because the iBundle auctions needed many auction rounds, we had to abort two of the auctions with VM3 and conducted only one auction with VM4. Therefore, the payments in iBundle were lower than in other auction formats (<sup>E</sup>34.57).

In each session of treatments 17 to 19, we conducted 6 auctions with a different draw of valuations for VM5. Each session was repeated four times with different subjects and a new wave of draws. In total, we ran 72 auctions in 12 sessions. The sessions took 3.5 to 5 hours depending on the auction format. The minimum payment was <sup>E</sup>10 and the maximum payment was <sup>E</sup>80 depending on the subjects’ payoff in the auctions. The average payment to subjects in VM5 was <sup>E</sup>43.90.

Table 5 Experimental Design

<table><tr><td>Treatment</td><td>Auction factor</td><td>Value factor</td></tr><tr><td>1</td><td>VCG</td><td>VM1</td></tr><tr><td>2</td><td>VCG</td><td>VM2</td></tr><tr><td>3</td><td>VCG</td><td>VM3</td></tr><tr><td>4</td><td>VCG</td><td>VM4</td></tr><tr><td>5</td><td>ALPS</td><td>VM1</td></tr><tr><td>6</td><td>ALPS</td><td>VM2</td></tr><tr><td>7</td><td>ALPS</td><td>VM3</td></tr><tr><td>8</td><td>ALPS</td><td>VM4</td></tr><tr><td>9</td><td>CC</td><td>VM1</td></tr><tr><td>10</td><td>CC</td><td>VM2</td></tr><tr><td>11</td><td>CC</td><td>VM3</td></tr><tr><td>12</td><td>CC</td><td>VM4</td></tr><tr><td>13</td><td>iBundle</td><td>VM1</td></tr><tr><td>14</td><td>iBundle</td><td>VM2</td></tr><tr><td>15</td><td>iBundle</td><td>VM3</td></tr><tr><td>16</td><td>iBundle</td><td>VM4</td></tr><tr><td>17</td><td>ALPS</td><td>VM5</td></tr><tr><td>18</td><td>ALPS (w/o DSS)</td><td>VM5</td></tr><tr><td>19</td><td>VCG</td><td>VM5</td></tr></table>

## 4. Hypotheses and Response Variables

## 4.1. Performance Measures

We use allocative efficiency (or simply efficiency) as a primary measure to benchmark auction designs. Allocative efficiency in CAs can be measured as the ratio of the total valuation of the resulting allocation X to the total valuation of an efficient allocation $X ^ { \ast }$ (Kwasnica et al. 2005):

$$
E (X) := \frac {\Pi (X , \mathcal {P} _ {\text { pay }}) + \pi_ {\text { all }} (X , \mathcal {P} _ {\text { pay }})}{\Pi (X ^ {*} , \mathcal {P} _ {\text { pay }}) + \pi_ {\text { all }} (X ^ {*} , \mathcal {P} _ {\text { pay }})} \in [ 0, 1 ]
$$

Another measure is the revenue distribution, which shows how the overall economic gain is distributed between the auctioneer and bidders. In cases where the auction is not 100% efficient, still another part of the overall utility is simply lost. Given the resulting allocation X and prices $\mathcal { P } _ { \mathrm { p a y } } ,$ the auctioneer’s revenue share is measured as the ratio of the auctioneer’s income to the total sum of valuations of an efficient allocation $X ^ { * }$

$$
\begin{array}{l} R (X) := \frac {\Pi (X , \mathcal {P} _ {\text {pay}})}{\Pi (X ^ {*} , \mathcal {P} _ {\text {pay}}) + \pi_ {\text {all}} (X ^ {*} , \mathcal {P} _ {\text {pay}})} \\ \in [ 0, E (X) ] \subset [ 0, 1 ]. \end{array}
$$

The cumulative bidders’ revenue share is $U ( X ) : =$ $E ( X ) - R ( X )$ . Note that efficiency depends only on the final allocation and not on the final prices $\dot { \mathcal { P } } _ { \mathrm { p a y } } . 7$ Therefore, it is possible for two auction outcomes with equal efficiency to have significantly different auctioneer revenues. In addition to efficiency and revenue distribution, we measure the speed of convergence in terms of auction rounds of the auction formats relative to each other.

## 4.2. Behavioral Assumptions and Bidding Strategies

For the VCG auction, there is a dominant strategy for bidders to bid the true valuation on all bundles. Provided that the valuations satisfy BSM, myopic best-response bidding is an ex post Nash equilibrium in iBundle and dVSV (de Vries et al. 2007). As already discussed, when the bidder submodularity condition does not hold, a myopic best-response strategy is likely to lead a bidder to pay more than the optimal price for the winning package (Dunford et al. 2007). Behavioral models of bidding in multiitem auctions are rare (see, for example, Plott and Salmon 2002). Schneider et al. (2008) analyzed the performance of primal-dual auctions and linear price ICAs in computational experiments. Provided there is best-response bidding, the simulations confirmed the theory. The efficiency of iBundle was at 100% in all auctions; however, the prices were above Vickrey prices on average because not all valuation models did satisfy BSM. Based on best-response bidding, both the combinatorial clock auction and ALPS performed significantly worse in terms of efficiency. Prices of these linear price auction formats were mostly higher, but sometimes they were also lower than the Vickrey prices. When bidders followed heuristic bidding strategies; however, linear price mechanisms showed to be fairly robust while primal-dual auctions often led to very low efficiency values.

Because in a private values experiment it is not known to the bidders whether bidder submodularity holds, one could expect bidders in iBundle to shade their bids in general. Also, one can often not expect bidders to follow pure best-response strategies due to cognitive barriers, but also due to risk aversion or some sort of strategizing of the bidders. In general, deviations from a best-response strategy can have multiple reasons:

• To follow best response strategies, bidders need to determine their demand sets from exponential numbers of possible bundle bids. This might be impossible due to cognitive restrictions, but it can also be due to strategic reasons. For example, in the early stages of the FCC spectrum auctions, bidders bid deliberately on bundles of lower interest to drive up the prices on those items while maintaining eligibility to bid on items of high interest later on (Cramton 1995, Cramton and Schwartz 2000).

• Such strategic reasons might not only be a reason for nonbest-response bundle selection but also for jump bidding, where bidders add more than the minimum bid increment to the ask prices when they determine bundle bid prices. Isaac et al. (2007) describe jump bidding to take place in a large proportion of FCC spectrum auctions (up to 44% of the bids with a 5% bid increment) as well as the 3G spectrum auctions in the United Kingdom.

• In situations closer to a common values model, bidders might also have biased estimates of their valuations v 4S5 at the start of the auction. The auction can then be seen as a way to help bidders elicit and learn about their true valuations throughout the auction. Researchers like Sargent (1993) among others have looked into respective theories of learning.

• Finally, it cannot be assumed that bidders will behave perfectly rationally in complex decision situations. They make mistakes and have different conceptual models of what strategies work best in given environments.

In §5, we will provide descriptive statistics on the level of jump bids and bundle selection in different auction formats. We will also use an ordinal logit model to analyze the discrete choice behavior of a bidder in each round that can be explained by covariates such as the value model or the auction format (Greene 2003, pp. 736–740).

## 4.3. Hypotheses

Based on the theoretical predictions, we identify the following hypotheses. The first two hypotheses are based on the dominant-strategy property of the VCG auction. In an independent private values model, a bidder’s dominant strategy is to bid truthfully on all packages.

<sup>Hypothesis</sup> <sup>1.</sup> In VCG auctions, bidders will bid on all packages (see §5, result 10).

<sup>Hypothesis</sup> <sup>2.</sup> In VCG auctions, bidders will bid truthfully (see §5, result 13).

Theory also suggests that best-response bidding is an ex post equilibrium in iBundle and that the auction will result in Vickrey payoffs when the bidder submodularity condition is satisfied. If it fails, a bidder can pay more than the VCG payment by following a best-response bidding strategy in an ascending proxy auction.

<sup>Hypothesis</sup> <sup>3.</sup> iBundle and the VCG auction will achieve full efficiency (see §5, result 1).

<sup>Hypothesis</sup> <sup>4.</sup> iBundle and the VCG auction will achieve the same auctioneer revenue if BSM is given (see §5, result 2).

<sup>Hypothesis</sup> <sup>5.</sup> Auctioneer revenue of iBundle will be higher than the revenue in a VCG auction when valuations do not satisfy BSM conditions (see §5, result 2).

Though there are strong incentives for bidders to follow best-response strategies if BSM is satisfied, there are fewer reasons to assume such strategies for general valuations or in linear price auction formats. Nevertheless, we postulate the following hypothesis on bidding behavior in ICAs.

<sup>Hypothesis</sup> <sup>6.</sup> In all auction formats, bidders follow best-response strategies (see §5, result 11).

<sup>Hypothesis</sup> <sup>7.</sup> Bidding behavior is homogeneous across individuals with the same treatment (see §5, result 13).

The performance of different analyzed auction formats depends on the bidders’ valuations and their bidding strategies. We ran simulations with different kinds of bidding agents and found that in value models VM1 to VM4, a best-response bidding strategy leads to the efficient solution.

<sup>Hypothesis</sup> <sup>8.</sup> With best-response bidding, the efficiency and results will follow the results of the simulations with best-response bidders. These simulations always result in efficient solutions (see §5, results 1 and 8).

In addition, we tested the following hypothesis on the number of auction rounds and the size of the auction. The best-response strategy in iBundle means that bidders only bid on their demand sets. This might cause many auction rounds because in each round often only one or a few bundles are elicited. We also assume no difference in efficiency for the smaller value models VM1-4 across all auction formats.

<sup>Hypothesis</sup> <sup>9.</sup> The number of auction rounds in ALPS is significantly lower than in iBundle (see §5, result 3).

<sup>Hypothesis</sup> <sup>10.</sup> There is no significant difference in the efficiency of combinatorial auctions for our small value models (VM1-4) of up to nine items (see §5, result 4).

We tested one larger value model (VM5) with 18 items and the ALPS auction format with and without decision support. This was done in order to see if the efficiency results extend also to selected larger value models, and to test the impact of bidder decision support, i.e., automated payoff calculation.

<sup>Hypothesis</sup> <sup>11.</sup> There is no difference in efficiency between small value models (VM1-4) and large value model (VM5) with seven bidders in ALPS and the VCG auction (see §5, result 6).

<sup>Hypothesis</sup> <sup>12.</sup> There is no difference between ALPS with and without bidder decision support (see §5, result 5).

Finally, in order to test for learning effects within a session, we used the six auctions in a single session in VM5.

<sup>Hypothesis</sup> <sup>13.</sup> There is no significant difference in efficiency and revenue among the six auctions with VM5 (see §5, result 9).

## 5. Experimental Results

In this section, we analyze the data from the experiments. We start with an overview of average efficiency and revenue distribution of the small value models VM1 to VM4. In addition, we look at the number of auction rounds in each auction. In a separate subsection, we analyze the larger value model VM5 and the VCG and the ALPS auction formats with and without decision support. Finally, in §5.3, we look at bidding behavior in the different auction formats.

## 5.1. Aggregate Performance Metrics of Small Value Models

In the first set of treatments (1 to 16), we used four different value models to compare ALPS, the CC auction, iBundle, and the VCG auction designs. The details of the auction setup and the results averaged over four sessions each are provided in Tables 6 and 7. The left-hand columns in Tables 6 and 7 describes the auction setup, i.e., the number of items and the value model. Note that three of the iBundle sessions on the value model VM4 had to be canceled because the auction converged very slowly. For example, session iB-52 was canceled after 4.5 hours, with one iBundle auction being at round 162. Also, session iB-102 was canceled after 4.5 hours, the last auction being at round 46. In contrast, the third auction in session iB-101 ended prematurely after 2 rounds, as one bidder did not submit any bid in the second round and every other bidder got a bundle in the provisional allocation. If the best-response bidding strategy is not guaranteed, the iBundle termination rule can lead to such inefficiencies.

We have added the results of the simulations using the same value models with best-response bidders as a benchmark in the columns suffixed by “-sim.”<sup>8</sup>

<sup>Result</sup> <sup>1.</sup> There is no significant difference in allocative efficiency across all four auction formats (Hypotheses 3 and 8).

All auctions in the small value models VM1–VM4 simulated with best-response bidders achieved 100% efficiency but varied in the auctioneer revenue. In the lab, the efficiency of all auction designs was also very high across all value models (see Figure 4). We did not find a significant difference in efficiency between different auction designs (see Table 8 and Figure 2). Although we found additional evidence for this result in VM5 with and without decision support for the bidders, we would not like to generalize the results to all large value models. We conjecture that bidders might face coordination problems in large value models and fully combinatorial auctions that allow bids on all possible bundles. The analysis of large combinatorial auctions is, however, beyond the scope of this paper.

<sup>Result</sup> <sup>2.</sup> Auctioneer revenue in the VCG auction is lower than in iBundle, the combinatorial clock auction, and ALPS (Hypotheses 4 and 5).

Table 6 Aggregate Measures of Auction Performance for ALPS and the Combinatorial Clock Auction Experiments

<table><tr><td colspan="2">Format</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value model</td><td></td><td>ALPS-sim</td><td>ALPS-21</td><td>ALPS-22</td><td>ALPS-31</td><td>ALPS-32</td><td>CC-sim</td><td>CC-41</td><td>CC-71</td><td>CC-72</td><td>CC-91</td></tr><tr><td>Value model 1</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.9</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.9</td><td>1.0</td></tr><tr><td>3 items</td><td>Auctioneer revenue</td><td>0.871</td><td>0.9</td><td>0.85</td><td>0.43</td><td>0.78</td><td>0.871</td><td>0.74</td><td>0.67</td><td>0.74</td><td>0.97</td></tr><tr><td>BSM</td><td>Rounds</td><td>16</td><td>4</td><td>14</td><td>4</td><td>6</td><td>15</td><td>8</td><td>7</td><td>9</td><td>11</td></tr><tr><td>Value model 2</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.7</td><td>1.0</td><td>1.0</td><td>0.87</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>3 items</td><td>Auctioneer revenue</td><td>0.63</td><td>0.7</td><td>0.8</td><td>0.58</td><td>0.66</td><td>0.77</td><td>0.67</td><td>0.53</td><td>0.73</td><td>0.7</td></tr><tr><td>not BSC</td><td>Rounds</td><td>10</td><td>6</td><td>3</td><td>8</td><td>6</td><td>10</td><td>15</td><td>6</td><td>8</td><td>8</td></tr><tr><td>Value model 3</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>0.62</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>6 items</td><td>Auctioneer revenue</td><td>0.7</td><td>0.78</td><td>0.83</td><td>0.57</td><td>0.82</td><td>0.79</td><td>0.8</td><td>0.8</td><td>0.85</td><td>0.85</td></tr><tr><td>not BSC</td><td>Rounds</td><td>24</td><td>7</td><td>9</td><td>10</td><td>9</td><td>14</td><td>10</td><td>10</td><td>12</td><td>12</td></tr><tr><td>Value model 4</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.83</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.92</td><td>1.0</td><td>1.0</td></tr><tr><td>9 items</td><td>Auctioneer revenue</td><td>0.74</td><td>0.81</td><td>0.93</td><td>0.77</td><td>0.9</td><td>0.89</td><td>0.78</td><td>0.85</td><td>0.89</td><td>0.89</td></tr><tr><td>not BSC</td><td>Rounds</td><td>21</td><td>6</td><td>5</td><td>13</td><td>5</td><td>11</td><td>9</td><td>13</td><td>11</td><td>15</td></tr></table>

Table 7 Aggregate Measures of Auction Performance for the VCG Mechanism and iBundle

<table><tr><td colspan="2">Format</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Value model</td><td></td><td>VCG-sim</td><td>VCG-61</td><td>VCG-62</td><td>VCG-81</td><td>VCG-82</td><td>iB-sim</td><td>iB-51</td><td>iB-52</td><td>iB-101</td><td>iB-102</td></tr><tr><td>Value model 1</td><td>Efficiency</td><td>1.0</td><td>0.95</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>3 items</td><td>Auctioneer revenue</td><td>0.850</td><td>1.0</td><td>0.88</td><td>0.59</td><td>0.68</td><td>0.850</td><td>0.85</td><td>0.79</td><td>0.9</td><td>0.9</td></tr><tr><td>BSM</td><td>Rounds</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>26</td><td>10</td><td>16</td><td>14</td><td>40</td></tr><tr><td>Value model 2</td><td>Efficiency</td><td>1.0</td><td>0.67</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td></tr><tr><td>3 items</td><td>Auctioneer revenue</td><td>0.43</td><td>0.99</td><td>0.31</td><td>0.37</td><td>0.49</td><td>0.60</td><td>0.84</td><td>0.63</td><td>0.74</td><td>0.9</td></tr><tr><td>not BSC</td><td>Rounds</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>26</td><td>12</td><td>20</td><td>23</td><td>40</td></tr><tr><td>Value model 3</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>1.0</td><td>0.69</td><td>1.0</td><td>1.0</td><td>1.0</td><td>—</td><td>0.76</td><td>0.22</td></tr><tr><td>6 items</td><td>Auctioneer revenue</td><td>0.600</td><td>0.67</td><td>0.61</td><td>0.62</td><td>0.62</td><td>0.600</td><td>0.8</td><td>—</td><td>0.3</td><td>0.91</td></tr><tr><td>not BSC</td><td>Rounds</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>47</td><td>14</td><td>162</td><td>2</td><td>37</td></tr><tr><td>Value model 4</td><td>Efficiency</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td>1.0</td><td></td><td></td><td>—</td></tr><tr><td>9 items</td><td>Auctioneer revenue</td><td>0.73</td><td>0.67</td><td>0.63</td><td>0.42</td><td>0.56</td><td>0.83</td><td>0.86</td><td></td><td></td><td>—</td></tr><tr><td>not BSC</td><td>Rounds</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>83</td><td>22</td><td></td><td></td><td>46</td></tr></table>

Table 8 Significance Tests for a Difference on All Pairs of Auction Formats

<table><tr><td>Comparison</td><td colspan="2">Efficiency</td><td colspan="2">Auctioneer revenue share</td><td colspan="2">Bidders&#x27; surplus</td><td colspan="2">Rounds</td></tr><tr><td>VCG vs. iBundle (Wilcoxon)</td><td>109</td><td>(0.8314)</td><td>60</td><td>(0.0539)</td><td>230</td><td>(0.0694)</td><td>0</td><td>(0.000)</td></tr><tr><td>VCG vs. iBundle (t-test)</td><td>0.71</td><td>(0.4868)</td><td>-1.94</td><td>(0.0633)</td><td>2.47</td><td>(0.0197)</td><td>-2.706</td><td>(0.01909)</td></tr><tr><td>VCG vs. ALPS (Wilcoxon)</td><td>136</td><td>(0.7405)</td><td>74</td><td>(0.0416)</td><td>243</td><td>(0.2534)</td><td>0</td><td>(0.000)</td></tr><tr><td>VCG vs. ALPS (t-test)</td><td>0.40</td><td>(0.6915)</td><td>-2.09</td><td>(0.0450)</td><td>1.58</td><td>(0.1239)</td><td>-7.868</td><td>(0.000)</td></tr><tr><td>VCG vs. CC (Wilcoxon)</td><td>126.5</td><td>(0.8962)</td><td>58</td><td>(0.0072)</td><td>231</td><td>(0.4096)</td><td>0</td><td>(0.000)</td></tr><tr><td>VCG vs. CC (t-test)</td><td>-0.81</td><td>(0.4263)</td><td>-2.63</td><td>(0.0134)</td><td>1.40</td><td>(0.1719)</td><td>-13.853</td><td>(0.000)</td></tr><tr><td>ALPS vs. iBundle (Wilcoxon)</td><td>103</td><td>(0.9619)</td><td>88</td><td>(0.4944)</td><td>200</td><td>(0.3730)</td><td>21.5</td><td>(0.000)</td></tr><tr><td>ALPS vs. iBundle (t-test)</td><td>0.46</td><td>(0.6509)</td><td>-0.18</td><td>(0.854)</td><td>1.24</td><td>(0.2238)</td><td>-2.399</td><td>(0.024)</td></tr><tr><td>ALPS vs. CC (Wilcoxon)</td><td>115.5</td><td>(0.4463)</td><td>124</td><td>(0.889)</td><td>176</td><td>(0.5246)</td><td>54.5</td><td>(0.004)</td></tr><tr><td>ALPS vs. CC (t-test)</td><td>-1.25</td><td>(0.2253)</td><td>-0.50</td><td>(0.6191)</td><td>-0.31</td><td>(0.7569)</td><td>-2.969</td><td>(0.006)</td></tr><tr><td>iBundle vs. CC (Wilcoxon)</td><td>95</td><td>(0.6)</td><td>119.5</td><td>(0.5083)</td><td>120</td><td>(0.1306)</td><td>176</td><td>(0.001)</td></tr><tr><td>iBundle vs. CC (t-test)</td><td>-1.15</td><td>(0.2717)</td><td>-0.20</td><td>(0.8373)</td><td>-1.62</td><td>(0.1136)</td><td>1.887</td><td>(0.083)</td></tr></table>

In simulations with best-response bidders, we found differences in the revenue distribution for different auction designs and value models. We observed similar results in the lab experiments, as shown in Figure 2. The median auctioneer’s revenue share across all value models produced by the simulations is shown as a benchmark by a dashed horizontal line. Note that though the auctioneer revenue in ALPS and the CC auction in the lab were close to the simulation results, the were results for iBundle were significantly higher and the lab results for the VCG auction were significantly lower than the simulation results. The iBundle results can be explained by jump bidding and the nonbest-response bidding that has been observed (see §5.3.3).

<sup>Result</sup> <sup>3.</sup> The number of rounds in iBundle is significantly higher than in ALPS and in the combinatorial clock auction (Hypothesis 9).

Figure 3 shows the number of auction rounds for every auction design and for every value model. The average number of rounds across all value models produced by the simulations is shown as a benchmark by a dashed horizontal line. The number of rounds in ALPS and the CC auction were lower than in the simulations for two reasons. First, eligibility rules encouraged the bidders to bid on more bundles than their demand sets. Second, jump bids have been used in ALPS. (The CC auction does not allow jump bidding.) In iBundle, we observed a significantly higher number of rounds even though the data does not contain the 3 sessions that had to be canceled after more than 100 rounds due to time reasons (see Figure 7 for detailed numbers). Nevertheless, the number of rounds was lower than in the simulations due to jump bidding, which is allowed in iBundle.

5.1.1. Pairwise Comparisons of Auction Formats. We now provide some statistical analyses with pairwise comparisons of selected metrics among treatment groups. A pairwise comparison entails less assumptions on the data-generating process than a linear model. We utilize the t-test for independent samples and the nonparametric Wilcoxon rank sum test to remove underlying distributional assumptions. The results are shown in Table 8. Though we did not find significant differences in efficiency, we found the auctioneer revenue share in the VCG auction to be significantly lower than in all other auction designs, which is consistent with the simulation results. The overall bidders’ surplus or net utility was not significantly different among the different auction formats, but there was a difference in the number of auction rounds, as can be seen in Figure 3.

## 5.1.2. Pairwise Comparisons of Value Models

<sup>Result</sup> <sup>4.</sup> There is no significant difference in efficiency across the different value models with three, six, and nine items (Hypothesis 10).

In our experimental setting, we have used auctions with three, six, and nine items. The bidders were interested in only 1 to 3 bundles in VM1 and VM2 (3 items), 11 to 15 bundles in VM3 (6 items), and 24 to 27 bundles in VM4 (9 items). We did not find any significant differences in efficiency between different value models (see Table 9 and Figure 4, which also includes VM5 where we only had experimental results for ALPS and the VCG auction as is described in §5.2). The small number of valuations in combination with the automated payoff calculation have made it fairly easy for the bidders to identify profitable bundles. Again, it is difficult to say whether the same holds for various large value models in which the preference elicitation on an exponentially large number of bundles might become a problem.

Figure 2 Efficiency and Revenue Distribution for Each Auction Format (a) Efficiency  
![](/api/attachments/4G77YTNT/fulltext/images/2fba01b30257292aac8aeb625ffedc8f54b917cc44b11bbd7b51e572f0d065f0.jpg)

(b) Auctioneer’s revenue share  
![](/api/attachments/4G77YTNT/fulltext/images/ed76115c1f551953c102e2329d3376530b9549e616091bfab51ee8dd5ff7a5f6.jpg)

5.1.3. ANOVA Analysis. In this section, we describe the results of the analysis of variance (ANOVA), which identifies the main impact factors and magnitude of interaction effects. The ANOVA statistical model for our case is given by

$$
Y _ {i j k} = \mu + \alpha_ {i} + \beta_ {j} + (\alpha \beta) _ {i j} + \epsilon_ {i j k},
$$

Figure 3 Number of Auction Rounds  
(a) Rounds per auction format  
![](/api/attachments/4G77YTNT/fulltext/images/762082c0cb26118083ed055cbbfe793bbdad9d3b6eeb3841b047eaf52ef81839.jpg)

(b) Rounds per value model  
![](/api/attachments/4G77YTNT/fulltext/images/05206a1680a302a3b30035f616942a625fffe1505d8c4ff825ec61595940af00.jpg)  
where $Y _ { i j k }$ stands for the dependent variable (either efficiency or revenue) and the differences are explained by the auction design $\alpha _ { i }$ and the value model $\beta _ { j }$ . The estimation error is denoted by $\epsilon _ { i j k }$ and the expected value is denoted by $\mu .$

First, the parameter estimation was performed with the allocative efficiency as the explanatory variable $Y _ { i j k }$ . The estimation results are given in Table 10. The results support the null hypothesis that the auction design and value model overall did not have a significant impact on efficiency in these experiments.

Table 9 Significance Tests for a Difference on the Four Value Models

<table><tr><td>Comparison</td><td colspan="2">Efficiency</td><td colspan="2">Revenue</td><td colspan="2">Rounds</td></tr><tr><td>VM1 vs. VM2 (Wilcoxon)</td><td>142</td><td>(1)</td><td>211</td><td>(0.0209)</td><td>147</td><td>(0.8472)</td></tr><tr><td>VM1 vs. VM2 (t-test)</td><td>0.87</td><td>(0.3923)</td><td>2.21</td><td>(0.03441)</td><td>-0.19</td><td>(0.8472)</td></tr><tr><td>VM1 vs. VM3 (Wilcoxon)</td><td>163</td><td>(0.4352)</td><td>177</td><td>(0.2620)</td><td>129.5</td><td>(0.6125)</td></tr><tr><td>VM1 vs. VM3 (t-test)</td><td>1.70</td><td>(0.1071)</td><td>1.30</td><td>(0.2027)</td><td>-0.9482</td><td>(0.3556)</td></tr><tr><td>VM1 vs. VM4 (Wilcoxon)</td><td>102.5</td><td>(0.6591)</td><td>119</td><td>(0.7333)</td><td>115</td><td>(0.5894)</td></tr><tr><td>VM1 vs. VM4 (t-test)</td><td>-0.08</td><td>(0.9348)</td><td>4,481</td><td>(0.6575)</td><td>0.4122</td><td>(0.6833)</td></tr><tr><td>VM2 vs. VM3 (Wilcoxon)</td><td>164</td><td>(0.3569)</td><td>115.5</td><td>(0.3259)</td><td>126</td><td>(0.5308)</td></tr><tr><td>VM2 vs. VM3 (t-test)</td><td>1.13</td><td>(0.2699)</td><td>-0.9395</td><td>(0.3545)</td><td>-0.8756</td><td>(0.3926)</td></tr><tr><td>VM2 vs. VM4 (Wilcoxon)</td><td>106</td><td>(0.7022)</td><td>70.5</td><td>(0.0964)</td><td>118</td><td>(0.762)</td></tr><tr><td>VM2 vs. VM4 (t-test)</td><td>-0.87</td><td>(0.3947)</td><td>-1.58</td><td>(0.1247)</td><td>0.5876</td><td>(0.5615)</td></tr><tr><td>VM3 vs. VM4 (Wilcoxon)</td><td>91</td><td>(0.2260)</td><td>89</td><td>(0.3787)</td><td>121.5</td><td>(0.6538)</td></tr><tr><td>VM3 vs. VM4 (t-test)</td><td>-1.696</td><td>(0.1069)</td><td>-0.7473</td><td>(0.4611)</td><td>1.09</td><td>(0.2904)</td></tr></table>

The same analysis was then performed with the auctioneer revenue share as the explanatory variable $Y _ { i j k } ,$ with similar results (see Table 11).

ANOVA assumes homoscedasticity of residuals as well as their normal distribution. The Levene test for homoscedasticity was significant, but the Shapiro-Wilk test for normality was not significant for both efficiency and revenue $( p < 0 . 0 5 )$ . However, a nonparametric Friedman rank sum test confirmed the ANOVA results that efficiency $( p = 0 . 1 8 7 )$ and revenue $( p = 0 . 3 0 8 )$ were not significantly different in each of the groups.

## 5.2. Aggregate Performance Metrics of the Large Value Model

Although the focus of this paper is on small value models, we ran an additional set of experiments with VM5 and the auction formats VCG and ALPS in order to see whether the results carry over to larger value models. We have also used this treatment to analyze the impact of automated payoff calculation. We conducted 4 sessions with 7 bidders and 6 auctions each for ALPS without DSS, for ALPS with decision support, and for the VCG auction, which resulted in $( 4 \times 6 \times 3 { = } )$ 72 auctions (see Table 12). Table 12 is composed of three tables for the three auction formats tested. Each subtable contains five columns for the unique session number, the auction number, efficiency, auctioneer’s revenue share, and the number of rounds.

<sup>Result</sup> <sup>5.</sup> There was no significant difference in both efficiency and revenue between ALPS with and without automated payoff calculation (Hypothesis 12).

Figure 4 Efficiency and Revenue Distribution for Different Value Models  
![](/api/attachments/4G77YTNT/fulltext/images/440d2d694a2bd018395de809db286ec39252a1b34ef07a16330fb78f21406573.jpg)

(b) Auctioneer’s revenue share  
![](/api/attachments/4G77YTNT/fulltext/images/7a0447e7baaa9a86818874638b7a9f72a61d0de2bd48394432cb500eeb3d402e.jpg)

The mean efficiency values of ALPS with decision support (0.95) and without decision support (0.9546) were not significantly different (t-test, $p = 0 . 4 2 4 2 )$ Also, the efficiency of simulations with best-response bidders was above 0.95 but varied depending on the draws from the value model. The same is true for the auctioneer’s revenue share, which on average was 0.769 for ALPS with and 0.782 for ALPS without decision support (t-test, $p = 0 . 6 6 5 )$ . Given the large variance in the number of auction rounds, we also did not find a significant difference in auction duration (t-test, $p = 0 . 0 8 1 )$ . Because we could not find a difference in these metrics for the large value model, such a difference is also unlikely for small value models where bidders only have three or six items.

Table 10 Impact of Value Model and Auction Format on Efficiency

<table><tr><td>Relative efficiency</td><td>DF</td><td>Sum of squares</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>Value model</td><td>1</td><td>0.00664</td><td>0.00664</td><td>0.3829</td><td>0.5384</td></tr><tr><td>Auction format</td><td>1</td><td>0.00535</td><td>0.00535</td><td>0.3085</td><td>0.5807</td></tr><tr><td>Value model</td><td>1</td><td>0.00003</td><td>0.00003</td><td>0.0018</td><td>0.9661</td></tr><tr><td colspan="6">* Auction format</td></tr><tr><td>Residuals</td><td>60</td><td>1.04066</td><td>0.01734</td><td></td><td></td></tr></table>

Table 11 Impact of Value Model and Auction Format on the Auctioneer Revenue Share

<table><tr><td>Auctioneer revenue share</td><td>DF</td><td>Sum of squares</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>Value model</td><td>1</td><td>0.00161</td><td>0.00161</td><td>0.0596</td><td>0.8079</td></tr><tr><td>Auction format</td><td>1</td><td>0.03931</td><td>0.03931</td><td>1.4592</td><td>0.2318</td></tr><tr><td>Value model * Auction format</td><td>1</td><td>0.00054</td><td>0.00054</td><td>0.0200</td><td>0.8879</td></tr><tr><td>Residuals</td><td>60</td><td>1.61634</td><td>0.02694</td><td></td><td></td></tr></table>

We did, however, find a significant difference in the number of bids submitted with decision support (t-test, $p = 0 . 0 2 6 )$ . On average, bidders submitted 107.29 bids with decision support but only 69.83 bids without decision support. This translated into an average number of 12.33 bids per round and bidder in ALPS with decision support and 10.09 bids per round and bidder in ALPS without decision support. The small bidders in this value model had positive valuations for $2 ^ { 6 } - 1 = 6 3$ bundles while the large bidder had valuations for $2 ^ { 1 2 } - 1 = 4 , 0 9 5$ bundles. It is interesting to note that there was no significant difference between the average number of bids per round that the small and large bidders submitted (t-test for a difference in ALPS with decision support, $p = 0 . 1 3 )$ . The fact that there was little difference in the efficiency in spite of the difference in the number of bids submitted supports the hypothesis that ALPS is rather robust against different bidding strategies. We tried iBundle with a large value model but had to cancel the experiment.

We have compared ALPS with decision support in the small value models (VM1-4) and VM5 with 18 items and did not find a significant difference in efficiency (t-test, $p = 0 . 7 7 3 )$ and revenue (t-test, $p = 0 . 7 4 5 )$

<sup>Result</sup> <sup>6.</sup> There was no significant difference in both efficiency and revenue between ALPS in VM5 and the results of ALPS in the small value models (Hypothesis 11).

Table 12 Aggregate Measures of Auction Performance for the VCG Auction and for ALPS With and Without Decision Support and VM5

<table><tr><td colspan="5">ALPS Without DSS</td><td colspan="5">ALPS</td><td colspan="5">VCG</td></tr><tr><td>Session</td><td>Auction</td><td>Efficiency</td><td>Revenue</td><td>Rounds</td><td>Session</td><td>Auction</td><td>Efficiency</td><td>Revenue</td><td>Rounds</td><td>Session</td><td>Auction</td><td>Efficiency</td><td>Revenue</td><td>Rounds</td></tr><tr><td>6</td><td>1</td><td>0.83</td><td>0.8</td><td>14</td><td>7</td><td>1</td><td>0.92</td><td>0.8</td><td>8</td><td>1</td><td>1</td><td>0.98</td><td>0.71</td><td>1</td></tr><tr><td>6</td><td>2</td><td>0.96</td><td>0.7</td><td>11</td><td>7</td><td>2</td><td>0.95</td><td>0.8</td><td>5</td><td>1</td><td>2</td><td>0.89</td><td>0.64</td><td>1</td></tr><tr><td>6</td><td>3</td><td>0.92</td><td>0.67</td><td>11</td><td>7</td><td>3</td><td>1</td><td>0.83</td><td>7</td><td>1</td><td>3</td><td>0.91</td><td>0.53</td><td>1</td></tr><tr><td>6</td><td>4</td><td>0.94</td><td>0.86</td><td>6</td><td>7</td><td>4</td><td>1</td><td>0.75</td><td>9</td><td>1</td><td>4</td><td>1</td><td>0.58</td><td>1</td></tr><tr><td>6</td><td>5</td><td>1</td><td>0.93</td><td>5</td><td>7</td><td>5</td><td>1</td><td>0.68</td><td>8</td><td>1</td><td>5</td><td>1</td><td>0.59</td><td>1</td></tr><tr><td>6</td><td>6</td><td>0.9</td><td>0.78</td><td>5</td><td>7</td><td>6</td><td>0.98</td><td>0.7</td><td>5</td><td>1</td><td>6</td><td>0.98</td><td>0.58</td><td>1</td></tr><tr><td>9</td><td>1</td><td>0.99</td><td>0.91</td><td>10</td><td>8</td><td>1</td><td>0.98</td><td>0.71</td><td>9</td><td>4</td><td>1</td><td>1</td><td>0.68</td><td>1</td></tr><tr><td>9</td><td>2</td><td>1</td><td>0.73</td><td>8</td><td>8</td><td>2</td><td>0.95</td><td>0.71</td><td>6</td><td>4</td><td>2</td><td>1</td><td>0.72</td><td>1</td></tr><tr><td>9</td><td>3</td><td>0.92</td><td>0.69</td><td>13</td><td>8</td><td>3</td><td>0.96</td><td>0.8</td><td>9</td><td>4</td><td>3</td><td>0.71</td><td>0.74</td><td>1</td></tr><tr><td>9</td><td>4</td><td>0.99</td><td>0.89</td><td>11</td><td>8</td><td>4</td><td>0.97</td><td>0.88</td><td>14</td><td>4</td><td>4</td><td>0.98</td><td>0.79</td><td>1</td></tr><tr><td>9</td><td>5</td><td>1</td><td>0.69</td><td>6</td><td>8</td><td>5</td><td>0.96</td><td>0.64</td><td>8</td><td>4</td><td>5</td><td>0.88</td><td>0.47</td><td>1</td></tr><tr><td>9</td><td>6</td><td>1</td><td>0.84</td><td>12</td><td>8</td><td>6</td><td>0.93</td><td>0.65</td><td>8</td><td>4</td><td>6</td><td>1</td><td>1</td><td>1</td></tr><tr><td>11</td><td>1</td><td>0.9</td><td>0.84</td><td>7</td><td>14</td><td>1</td><td>1</td><td>0.96</td><td>11</td><td>5</td><td>1</td><td>1</td><td>0.72</td><td>1</td></tr><tr><td>11</td><td>2</td><td>0.88</td><td>0.79</td><td>7</td><td>14</td><td>2</td><td>0.97</td><td>0.87</td><td>9</td><td>5</td><td>2</td><td>1</td><td>0.4</td><td>1</td></tr><tr><td>11</td><td>3</td><td>0.98</td><td>0.71</td><td>8</td><td>14</td><td>3</td><td>1</td><td>0.72</td><td>7</td><td>5</td><td>3</td><td>0.91</td><td>0.41</td><td>1</td></tr><tr><td>11</td><td>4</td><td>1</td><td>0.89</td><td>4</td><td>14</td><td>4</td><td>0.87</td><td>0.98</td><td>14</td><td>5</td><td>4</td><td>1</td><td>0.58</td><td>1</td></tr><tr><td>11</td><td>5</td><td>1</td><td>0.68</td><td>4</td><td>14</td><td>5</td><td>0.95</td><td>0.89</td><td>13</td><td>5</td><td>5</td><td>1</td><td>0.67</td><td>1</td></tr><tr><td>11</td><td>6</td><td>0.98</td><td>0.74</td><td>3</td><td>14</td><td>6</td><td>1</td><td>0.78</td><td>15</td><td>5</td><td>6</td><td>1</td><td>0.37</td><td>1</td></tr><tr><td>13</td><td>1</td><td>0.8</td><td>0.61</td><td>6</td><td>17</td><td>1</td><td>0.94</td><td>0.86</td><td>8</td><td>16</td><td>1</td><td>0.99</td><td>0.85</td><td>1</td></tr><tr><td>13</td><td>2</td><td>0.98</td><td>0.81</td><td>7</td><td>17</td><td>2</td><td>0.81</td><td>0.6</td><td>8</td><td>16</td><td>2</td><td>1</td><td>0.43</td><td>1</td></tr><tr><td>13</td><td>3</td><td>1</td><td>0.7</td><td>5</td><td>17</td><td>3</td><td>0.83</td><td>0.6</td><td>5</td><td>16</td><td>3</td><td>1</td><td>0.3</td><td>1</td></tr><tr><td>13</td><td>4</td><td>1</td><td>0.85</td><td>7</td><td>17</td><td>4</td><td>0.9</td><td>0.71</td><td>9</td><td>16</td><td>4</td><td>0.91</td><td>0.77</td><td>1</td></tr><tr><td>13</td><td>5</td><td>0.97</td><td>0.89</td><td>5</td><td>17</td><td>5</td><td>1</td><td>0.67</td><td>9</td><td>16</td><td>5</td><td>1</td><td>0.73</td><td>1</td></tr><tr><td>13</td><td>6</td><td>0.97</td><td>0.77</td><td>8</td><td>17</td><td>6</td><td>0.93</td><td>0.88</td><td>21</td><td>16</td><td>6</td><td>1</td><td>0.57</td><td>1</td></tr></table>

We do not claim that the results on larger value models beyond 10 items can be easily generalized. The results indicate that linear price auction formats can achieve high levels of efficiency on larger value models, but we need much more experimental work in this field with different types of value models to better understand large-scale combinatorial auctions.

We then compared the VCG auction using different value models. We did not find a significant difference for efficiency (t-test, p = 00795) and revenue (t-test, p = 00810) between the small value models (VM1-4) and VM5.

<sup>Result</sup> <sup>7.</sup> There was no significant difference in both efficiency and revenue between the VCG auction in VM5 and the result of the VCG auction in the small value models (Hypothesis 11).

We also found no differences in efficiency between ALPS with decision support and the VCG auction for VM5 (95.00% versus 96.16%; t-test, p = 00424) but we did find a significant difference in revenue (t-test, p = 0000052), which was 61.79% for the VCG auction and 76.96% for ALPS. These findings are similar to the results with small value models (VM1-4).

<sup>Result</sup> <sup>8.</sup> There was no significant difference in efficiency between ALPS with automated payoff calculation and the VCG auction in VM5. Revenue was, however, significantly lower in the VCG auction (Hypothesis 8).

In a single session, we conducted six auctions with the same subjects but with different valuations drawn and different bidder types assigned for each bidder in each auction. The differences in efficiency between the first and later auction rounds were not significant. Though this does not exclude learning effects, we could not find them on an aggregate level. For example, the t-test for zero difference between the first and the sixth round of ALPS auctions resulted in a p-value of 0.216. A bid-level analysis of payoffs throughout the auction for individual bidders in different auctions did not reveal a significant pattern either.

<sup>Result</sup> <sup>9.</sup> There was no signficant difference in efficiency in different auctions of a session in VM5 (see Hypothesis 13).

Overall, we do not make any statements regarding learning effects in combinatorial auctions, which would be beyond this study. The comparisons of auction formats are conditional on whatever learning may have occurred during the previous VMs under the same format. All statistical tests in this subsection were cross-checked with a Wilcoxon rank sum test.

## 5.3. Analysis of Bidding Behavior

In this section, we provide an individual-level analysis of the bidding behavior. In combinatorial auctions, bidding strategies can be much more complex than in traditional single-item auctions because bidders not only have to choose bid prices but also select the bundles to bid on in every round. In the VCG auction, we tested Hypotheses 1 and 2 and analyzed whether the bidders followed the strategies predicted by the theory. Because there is no equilibrium analysis of linear price designs, we did not conduct any structural analysis but we estimated a logit model with different covariates to possibly explain the bidding behavior. In iBundle, we compared the bidders’ strategies to bestresponse bidders in our simulations.

5.3.1. Bidding on Extended Bundles. For the following analysis, the extended bundles phenomenon that we observed in the experiments is of interest. The bidders sometimes submitted bids on extended bundles, i.e., supersets of the bundles for which they were given explicit valuations. For example, a bidder that received a positive valuation for AB would sometimes also bid on ABC with the same or higher bid price as for AB although he has not been given an explicit valuation for ABC. The awareness of free disposal might have led bidders to the conclusion that they could win more by bidding on extended bundles. On the other hand, bidding on extended bundles can be a strategy in ALPS and the CC auction to keep eligibility high but it has risk of winning a bundle at a lower payoff.

Altogether from the 6,340 bids over all auctions in the small value models VM1-4, there were 614 bids (9.6%) on extended bundles—84 in VM1, 151 in VM2, 233 in VM3, and 146 in VM4. From those bids, more than half were submitted in the VCG auction so that by excluding the VCG auction, the numbers are 59, 105, 89, and 14, respectively. Overall, only 5.1% of the 5,249 bids in iterative auctions (without the VCG) were on extended bundles. In contrast, 347 out of 1,091 bids (31.8%) were submitted on extended bundles in the VCG auctions in VM1-4.

In ALPS, almost all bids on extended bundles were submitted in the first three rounds. Also, 3.1% of the bids were submitted on bundles without any positive valuation in the first round. Both phenomena vanished in later rounds. At a price of zero or close to zero, bidders apparently wanted to maximize their eligibility. In the CC auction, there were almost no bids with no valuation, and a small proportion (4%) of the bids on extended bundles were mostly bid in the first five rounds of the auction. In iBundle, 4.6% were on extended bundles and most of them were submitted in the first 10 rounds. Bids on bundles without valuation were again negligible. We also found that, in all auction formats, only a small proportion of the bidders submitted bids on extended bundles. In all 3 iterative auction formats, only 25% of the 16 bidder submitted more than 10 bids on extended bundles while the others hardly used this possibility. In contrast, in the VCG auction, 56% of the bidders submitted bids on extended bundles.

For the large value model VM5 with ALPS, the bidders were told that there was no free disposal and that extended bundles had a value of zero to them. This did have an impact on the bidding behavior. Overall, only 211 out of 7,244 bids (2.91%) were submitted on extended bundles. In the VCG auction, this was only 1.14%. In ALPS, this was 7.8%, almost all of which was submitted in the first 5 rounds by only 10% to 20% of the subjects in each auction.

5.3.2. Bidding Behavior in the VCG Auction. Chen and Takeuchi (2008) found that most bidders either underbid or bid at their true value, i.e., the overbidding in single-unit Vickrey auctions did not carry over to combinatorial VCG auctions. In contrast, we identified both under- and overbidding in the VCG auction in our experiments (see Table 13).

<sup>Result</sup> <sup>10.</sup> On average, 15.2% of the bids of the bidders in a VCG auction revealed the true valuations: 48.3% can be classified as underbidders and 36.5% bid more than the true valuation for the bundle (Hypothesis 2).

Table 13 shows the relative number of bids that were above, below, close to, and exactly at the respective valuation in different value models. Overall, in all value models, the relative number of truthful bids was low. This is similar to what has been found for single-item Vickrey auctions. For example, Kagel and Levin (1985) report that in an experiment, 30% of all bids were at the dominant-strategy price, 62% of all bids were above the dominant-strategy price, and only 8% of all bids were below. Bidding above the dominant-strategy price in a Vickrey auction is mostly based on the illusion that it improves the probability of winning with little cost as the second-highest bid price is paid.

<sup>Result</sup> <sup>11.</sup> In VCG auctions, bidders did not bid on all bundles of value (Hypothesis 1).

The column “activity ratio 1” in Table 13 provides the number of bundles that were bid on throughout the auction divided by the number of positively valued bundles that were explicitly given to the bidders. The numbers are significantly higher than 1.0, which

Table 13 Nontruthful Bidding in the VCG Auction

<table><tr><td></td><td>Truthful bidding</td><td>Truthful bidding (+/-2.5%)</td><td>Overbidding</td><td>Underbidding</td><td>Activity ratio 1</td><td>Activity ratio 2</td></tr><tr><td>VM1</td><td>0.10</td><td>0.20</td><td>0.59</td><td>0.31</td><td>2.12</td><td>0.96</td></tr><tr><td>VM2</td><td>0.10</td><td>0.22</td><td>0.58</td><td>0.33</td><td>1.89</td><td>0.95</td></tr><tr><td>VM3</td><td>0.24</td><td>0.40</td><td>0.50</td><td>0.26</td><td>1.57</td><td>0.88</td></tr><tr><td>VM4</td><td>0.15</td><td>0.17</td><td>0.61</td><td>0.24</td><td>1.11</td><td>0.80</td></tr><tr><td>VM5</td><td>0.14</td><td>0.35</td><td>0.29</td><td>0.58</td><td>0.03</td><td>0.03</td></tr></table>

Figure 5 Scatter Plots of Bids for VM4 and VM5 in the VCG Auction  
(a) VM4  
![](/api/attachments/4G77YTNT/fulltext/images/d12a77ed4d17c601c989959a7ad6c7941d81b30054556133daf345604204db87.jpg)

(b) VM5  
![](/api/attachments/4G77YTNT/fulltext/images/e7a6cd4728f3588070b69849f1ba775549024789f1ac6eaa6b9952e9e27f583e.jpg)  
can be explained by the extended bundles phenomenon (see §5.3.1). Additionally, some bids were also placed on bundles without any positive valuation, which might have been simple mistakes. Interestingly, the bidders did not bid on all positively valued bundles that were explicitly provided to them. The column “activity ratio $2 ^ { \prime \prime }$ in Table 13 shows the ratio of the bids on bundles with explicitly specified positive valuations to the total number of these bundles. Actually, the longer the list of valuations, the smaller is this ratio. Especially in VM5, the activity ratios are very low because the big bidder has 4,095 bundles with positive valuation and bids on 18 bundles (median). The small bidders in VM5, with 63 bundles with positive valuation, had “activity ratio $1 ^ { \prime \prime }$ of 0.28 and “activity ratio $2 ^ { \prime \prime }$ of 0.27.

To further analyze Hypothesis $^ { 2 , }$ we used the OLS regression with the bundle value as the independent variable and the bid price as the dependent variable. The estimated regression coefficients for explicitly given and extended bundles are shown in Table 14. The row $V M _ { \mathrm { a l l } }$ contains the coefficients estimated for all auctions.

Isaac and James (2000) performed a similar regression and found a coefficient value of 0.95, which was not statistically different from 1.0. Chen and Takeuchi (2008) report a coefficient of 0.962, which is also close to truthful preference revelation. In Table 14, we found that the regression coefficient decreased with the value model from VM1 to VM4, which can be due to the increasing number of items. Figure 5 depicts the diagrams plotting the bundle valuation (or net payoff, respectively) against the actual bid price for VM4 and VM5 in all VCG auctions. In other words, it shows whether bidders followed their dominant strategies and revealed their valuations truthfully. Triangles denote bids on bundles with an explicitly given positive valuation while plus signs (+) denote extended bundles.

5.3.3. Best-Response Bidding Behavior in ICAs. In iterative combinatorial auctions, an interesting question is the bundle selection behavior, i.e., which bundles the bidders bid for in different rounds given their private valuations and the current ask prices. Deviations from best-response bidding might impact the efficiency of auction designs such as iBundle that are based on this assumption.

Table 14 Regression Coefficients for the Value of a Bundle

<table><tr><td>VM</td><td>All bundles</td><td>Given bundle</td><td>Extended bundle</td></tr><tr><td>VM1</td><td>0.9251</td><td>1.2707</td><td>1.3698</td></tr><tr><td>VM2</td><td>0.8457</td><td>1.1597</td><td>1.1714</td></tr><tr><td>VM3</td><td>1.0389</td><td>1.0296</td><td>1.0904</td></tr><tr><td>VM4</td><td>0.9683</td><td>0.9474</td><td>1.0406</td></tr><tr><td>VM5</td><td>0.9487</td><td>0.9833</td><td>—</td></tr><tr><td> $VM_{all}$ </td><td>0.9569</td><td>0.9803</td><td>1.0881</td></tr></table>

Table 15 Best-Response Bidding

<table><tr><td></td><td> $BB^{NJ}$ </td><td> $xBB^{NJ}$ </td><td> $xBB$ </td></tr><tr><td>ALPS</td><td>0.09</td><td>0.16</td><td>0.36</td></tr><tr><td>Clock</td><td>0.33</td><td>0.66</td><td>0.66</td></tr><tr><td>iBundle</td><td>0.13</td><td>0.23</td><td>0.69</td></tr><tr><td>VM1</td><td>0.32</td><td>0.54</td><td>1.00</td></tr><tr><td>VM2</td><td>0.29</td><td>0.51</td><td>1.00</td></tr><tr><td>VM3</td><td>0.16</td><td>0.28</td><td>0.62</td></tr><tr><td>VM4</td><td>0.09</td><td>0.24</td><td>0.47</td></tr><tr><td>VM5</td><td>0.05</td><td>0.08</td><td>0.21</td></tr><tr><td>VM1 + ALPS</td><td>0.15</td><td>0.35</td><td>1.00</td></tr><tr><td>VM1 + Clock</td><td>0.65</td><td>1.00</td><td>1.00</td></tr><tr><td>VM1 + iBundle</td><td>0.22</td><td>0.39</td><td>1.00</td></tr><tr><td>VM2 + ALPS</td><td>0.11</td><td>0.25</td><td>1.00</td></tr><tr><td>VM2 + Clock</td><td>0.57</td><td>1.00</td><td>1.00</td></tr><tr><td>VM2 + iBundle</td><td>0.26</td><td>0.39</td><td>1.00</td></tr><tr><td>VM3 + ALPS</td><td>0.05</td><td>0.10</td><td>0.49</td></tr><tr><td>VM3 + Clock</td><td>0.26</td><td>0.57</td><td>0.57</td></tr><tr><td>VM3 + iBundle</td><td>0.16</td><td>0.21</td><td>0.69</td></tr><tr><td>VM4 + ALPS</td><td>0.06</td><td>0.12</td><td>0.44</td></tr><tr><td>VM4 + Clock</td><td>0.24</td><td>0.55</td><td>0.55</td></tr><tr><td>VM4 + iBundle</td><td>0.03</td><td>0.18</td><td>0.52</td></tr><tr><td>VM5 + ALPS</td><td>0.09</td><td>0.16</td><td>0.29</td></tr></table>

To analyze the bundle selection behavior, we define four groups of bundles: BB, 2BB, 3BB, and all other bundles. For the bundles with explicitly provided valuations, we determine the best possible, the second-best possible, and the third-best possible payoffs $( u _ { 1 } , \ u _ { 2 } ,$ and $u _ { 3 } ,$ respectively) at the current ask prices. We then assign these bundles to the groups according to the rank of their possible payoffs. Because possible payoffs of extended bundles can fall in between, we assign extended bundles by the following rule: The extended bundles with payoffs equal to $u _ { 1 }$ are assigned to BB; those with payoffs in $[ u _ { 2 } ; u _ { 1 } ]$ to 2BB; those with payoffs in $[ u _ { 3 } ; u _ { 2 } ]$ to 3BB; and the remainder to other bundles. We further distinguish between jump bids and nonjump bids in each of the groups, denoted by J and $N J .$ , respectively. For example, $2 B \bar { B } ^ { N J }$ refers to the nonjump bids on the bundles from 2BB. Note that, in this notation, $B B ^ { N J }$ contains exactly the best-response bids.

Table 15 provides an overview of the proportions of bids submitted for the different kinds of bundles throughout the auctions. Column $x B B ^ { N J }$ refers to all bids from the groups $B B ^ { N J } , ~ 2 B B ^ { N J } .$ , and $3 B B ^ { N J }$ . Similarly, Column xBB refers to all bids from the groups BB, 2BB, and 3BB. The results are also visualized at a more detailed level $( B B , 2 B B , \ldots , n B B$ on the x-axis) in Figures 6 and 7.

We have discussed that, in the early round, bidders focused more on eligibility and they submitted bids on extended bundles. Therefore, we were interested in whether the numbers in Table 15 would change if we removed the first three rounds from the analysis. Actually, the proportion of best-response bids (xBB) increased to 0.43 for ALPS and to 0.73 for the clock auction (see Table 16). The proportion of pure bestresponse bids in iBundle stayed almost the same with 0.7, i.e., the phenomenon is stronger in auction formats with eligibility rules. When we removed the first 6 rounds from the analysis, xBB even increased to 0.47 in ALPS and 0.8 in the clock auction. With an increasing number of auction rounds, there are less bundles with positive payoff and bidders are better able to focus on their best bundles.

<sup>Result</sup> <sup>12.</sup> Bidders did not follow pure bestresponse strategies in any of the iterative combinatorial auction formats (Hypothesis 6).

In ALPS, 34% of bids (including jump bids) were submitted on bundles from the best 3 groups but only 9% were pure best-response bids. There are multiple reasons for nonbest-response bidding in

Figure 6 Detailed Distribution of Bids in VM3  
![](/api/attachments/4G77YTNT/fulltext/images/12d800409e8b3f07f654021baa085027d25e62b065a4228ee2c9f13ad23ec4a8.jpg)

![](/api/attachments/4G77YTNT/fulltext/images/841911d4072f297bf7d8d72c71ac28e6a56fadaaee20cb97463f1f7b79fe2277.jpg)

![](/api/attachments/4G77YTNT/fulltext/images/5e015827a91e6a5cb9fdad68a35e6ccc1cb1a0d99a9eab9dd0cc622d71efc215.jpg)

ALPS such as eligibility rules and nonmonotonicity in prices. Also, the fact that all bids remain active throughout the auction might have an impact on bidder behavior. In the CC auction, bidders cannot sub-

Figure 7 Detailed Distribution of Bids in VM5  
![](/api/attachments/4G77YTNT/fulltext/images/3eaf28f3426633e476657754e2d5ea51b5aaeb159160b321f919f805270539fa.jpg)

![](/api/attachments/4G77YTNT/fulltext/images/3820cc5801e988e4ec9c1b53fd9252cc51048a93b5401fa7c698af22b3951f9e.jpg)

![](/api/attachments/4G77YTNT/fulltext/images/f5f709d6d8fde46e7f0c654b8563a333ec6dea65be5eac7415ee51a3325132b1.jpg)

mit jump bids but the same eligibility rules apply. Here, the percentage of bids from the top 3 bundle groups was 66%. Eligibility rules induce bidders to submit many bids, which accounts for many bids on bundles with a lower payoff. In contrast, the iBundle eligibility rule does not hinder best-response bidding and theory predicts bidders to follow best-response strategies. Nevertheless, only 13% of bids were bestresponse bids in our iBundle experiments. Furthermore, 69% of bids (including jump bids) were submitted on bundles from the best 3 bundle groups but only 3% of the bids were pure best-response bids in iBundle and VM4 with 9 items. The reasons can be the inability of personalized bundle prices to reflect the current market competition and the large number of rounds, both of which might have induced the bidders to jump bidding. As the computational experiments have shown, the efficiency of iBundle can be significantly below 100% for realistic value models if bidders do not follow best response strategy but instead follow heuristic bidding strategies (Schneider et al. 2008).

Table 16 Best-Response Bidding in Later Rounds 4>35 of the Auction

<table><tr><td></td><td> $BB^{NJ}$ </td><td> $xBB^{NJ}$ </td><td> $xBB$ </td></tr><tr><td>ALPS</td><td>0.11</td><td>0.22</td><td>0.43</td></tr><tr><td>Clock</td><td>0.41</td><td>0.73</td><td>0.73</td></tr><tr><td>iBundle</td><td>0.14</td><td>0.24</td><td>0.70</td></tr><tr><td>VM1</td><td>0.43</td><td>0.66</td><td>1.00</td></tr><tr><td>VM2</td><td>0.47</td><td>0.63</td><td>1.00</td></tr><tr><td>VM3</td><td>0.21</td><td>0.33</td><td>0.69</td></tr><tr><td>VM4</td><td>0.11</td><td>0.35</td><td>0.60</td></tr><tr><td>VM5</td><td>0.12</td><td>0.23</td><td>0.38</td></tr></table>

<sup>Result</sup> <sup>13.</sup> We could not observe pure bestresponse bidding in iBundle; however, efficiency levels for iBundle on average were close to 100% in this experiment. Larger value models suffered from many auction rounds (Hypothesis 8).

The iBundle results need to be interpreted with care. The small value models all achieved 100% efficiency but here the decision problems faced by bidders are simple. Already, for value models with six or nine items, the number of auction rounds increased significantly and some auctions had to be canceled due to time reasons. This suggests that, in its original form, iBundle will only be suitable for very small combinatorial auctions. Higher price increments together with proxy agents that translate these high bid increments into many small rounds might be a remedy.

<sup>Result</sup> <sup>14.</sup> Bidder behavior was heterogeneous across individuals with the same treatment (Hypotheses 2 and 7).

The cognitive complexity of the decision environment is probably the best explanation for the fact that observed bidding behavior was different across individuals with the same treatments. This can be illustrated by a bidder-level analysis of particular auction

Figure 8 Distribution of Factors in ALPS and the Combinatorial Clock Auction  
![](/api/attachments/4G77YTNT/fulltext/images/7a5172468c4d7470285248addeb06b1268293a01d4280afb8ad3158a1aa612f7.jpg)

![](/api/attachments/4G77YTNT/fulltext/images/6b96b3fdcd2e04e3d9ad62156f56138aea61443c4f72f29d7f0336bddae7d96e.jpg)

designs as will also be discussed in subsequent sections. Figures 8 and 9 show the distribution of bids for individual bidders with the same valuations in VM3. Each bar describes the bidding behavior of a single bidder. The darkest shade of gray indicates the proportion of bids on the bundle with the highest payoff (BB); the second darkest shade of gray indicates the proportion of bids on the second-best bundle (2BB); the third darkest shade of gray describes the third-best bundle (3BB); and the lightest shade of gray indicates bids on all other bundles. Shaded areas describe the proportion of those bids that were jump bids. Furthermore, the relative number of submitted bids in relation to other bidders is indicated by the width of the corresponding bar. Figures 8 and 9 show that some bidders submitted many bids and others submitted only a few. There were bidders who concentrated on the best three bundles in terms of payoff and others who submitted more bids for bundles with lower payoff.

Figure 9 Distribution of Factors in iBundle  
![](/api/attachments/4G77YTNT/fulltext/images/e838c67604f51ee6ea6f359556e8f414adfbe272eae9ad13ae64871cacd0e5c7.jpg)

The results suggest that one cannot assume human bidders to act according to the same “best strategy” in a complex decision environment. Though there are rational explanations for ALPS such as eligibility rules, the reasons for this behavior are less obvious in iBundle. In light of these findings, the robustness of auction designs against nonoptimal bidding strategies emerges as an important design criterion for practical applications of combinatorial auctions.

5.3.4. Ordinal Choice Model. In this section, we model a bidder’s bundle selection decision in each round as a discrete choice problem, whereby the impact of covariates such as auction design and value model is estimated. In the ordinal logit model, the dependent variable y can take four different values: 0 means that the bidder submitted a bid on a bundle from BB, 1 describes a bid on a bundle from 2BB, 2 describes a bid on a bundle from 3BB, and 3 describes a bid on any other bundle. All values include jump bids. The independent variables $\mathbf { x } _ { i }$ include binary variables for the auction designs $( C C = C C$ auction, PD = iBundle) and value models (VM2, VM3, VM4). As a baseline for the categorical variables auction design and value model, we used ALPS and VM1, respectively. We also include the number of eligibility points (EP) and whether a bidder was a winner in the last round (WLAST R) as well as interaction effects between iBundle and VM4 (PDVM4) because they have shown to be highly significant. Clearly, bidding behavior changes throughout the auction and the number of alternative bundles with positive payoff decreases. Our exploratory data analysis revealed that bidding behavior was particularly different in the first three rounds, where bidders often submitted bids on extended bundles in order to keep their eligibility high. This was much less frequent in later rounds. Therefore, we have included covariates, describing bids in higher rounds (beyond round three) as LAT EROUN and interaction effects of this variable with the value models as LATEVM2, LATEVM3, and LATEVM4.

The ordinal logit model investigates how an ordinal variable Y taking value in $\{ 1 , \ldots , m \}$ depends on a vector of covariates z. We assume that Y is determined by the latent $Y ^ { * }$ and a set of additional parameters $\gamma _ { 1 } , \gamma _ { i } , \gamma _ { m - 1 }$ is defined as the threshold values. Under the additional assumption that $\epsilon _ { i }$ has a standard logistic distribution and z is exogeneous, it follows that

$$
P (Y \leq j \mid \mathbf {z}) = \frac {\exp (\gamma_ {j} - \alpha - \mathbf {z} ^ {\prime} \beta)}{1 + \exp (\gamma_ {j} - \alpha - \mathbf {z} ^ {\prime} \beta)}.
$$

For details on the estimation procedure, see Greene (2003). We omit VM5 because we only had results for ALPS on this value model.

The model led to an estimated error rate of 31% with four rank-ordered choices. Table 17 reports the coefficients of the estimated ordinal logit model. The marginal effects for the ordered probability model provide more detailed information on the individual choices and are given in Table 18. Each negative coefficient in the second column describes a negative impact on choosing the best bundle, the third column describes the marginal effect on the secondbest bundles, etc. There are a number of interesting observations. As compared to ALPS as the baseline, the covariate for the combinatorial clock auction (CC) did not have a significant impact while switching to iBundle (PD) did have a postive impact on choosing BB or 2BB. Larger value models had significant coefficients and a negative impact on selecting the best or second-best bundle. In particular, the interaction effect between iBundle and VM4 (PDVM4) was significant and negative on these two choices. The other interaction effects between auction formats and value models were not significant and we removed them from the model in order to get a more parsimonious description of the bidding behavior. In contrast, the indicator variable for late round bids beyond round three (LAT EROUN ) had a positive impact on the probability of selecting the best two bundles. This is no surprise because the number of alternative bundles shrinks. Looking at the interaction effect with value models, the interaction of this indicator with VM4 (LAT EVM4) had the highest significance, which suggests that in larger value models, bidders are more likely to select their best bundles in later rounds as compared to the baseline.

Table 17 Estimated Coefficients of the Ordinal Logit Model

<table><tr><td>Variable</td><td>Coefficient</td><td> $P\left\lbrack {\left| Z\right| > z}\right\rbrack$ </td><td>Mean of X</td></tr><tr><td>Constant</td><td>-0.5084848885</td><td>0.0000</td><td></td></tr><tr><td>EP</td><td>0.03214283580</td><td>0.0000</td><td>2.6099369</td></tr><tr><td>WLASTR</td><td>0.3674921936</td><td>0.0000</td><td>0.22365931</td></tr><tr><td>CC</td><td>0.02230806301</td><td>0.5950</td><td>0.29779180</td></tr><tr><td>PD</td><td>-0.1887835180</td><td>0.0003</td><td>0.39447950</td></tr><tr><td>VM2</td><td>0.2704704307</td><td>0.0026</td><td>0.10883281</td></tr><tr><td>VM3</td><td>1.260802637</td><td>0.0000</td><td>0.43249211</td></tr><tr><td>VM4</td><td>1.549391984</td><td>0.0000</td><td>0.37097792</td></tr><tr><td>PDVM4</td><td>0.6235001865</td><td>0.0000</td><td>0.12965300</td></tr><tr><td>LATEROUN</td><td>-0.2221204144</td><td>0.0367</td><td>0.49826498</td></tr><tr><td>LATEVM2</td><td>-0.1941968019</td><td>0.1611</td><td>0.047791798</td></tr><tr><td>LATEVM3</td><td>-0.2638853304</td><td>0.0198</td><td>0.23832808</td></tr><tr><td>LATEVM4</td><td>-0.5012348284</td><td>0.0000</td><td>0.17066246</td></tr></table>

Table 18 Marginal Effects for the Ordinal Logit Model

<table><tr><td>Estimates</td><td>Y = BB</td><td>Y = 2BB</td><td>Y = 3BB</td><td>Y = other</td></tr><tr><td>ONE</td><td>0.0000</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr><tr><td>EP</td><td>-0.0110</td><td>-0.0018</td><td>0.0012</td><td>0.0117</td></tr><tr><td>WLASTR</td><td>-0.1181</td><td>-0.0272</td><td>0.0074</td><td>0.1379</td></tr><tr><td>CC</td><td>-0.0076</td><td>-0.0013</td><td>0.0008</td><td>0.0081</td></tr><tr><td>PD</td><td>0.0653</td><td>0.0098</td><td>-0.0074</td><td>-0.0678</td></tr><tr><td>VM2</td><td>-0.0868</td><td>-0.0204</td><td>0.0053</td><td>0.1019</td></tr><tr><td>VM3</td><td>-0.3949</td><td>-0.0758</td><td>0.0240</td><td>0.4467</td></tr><tr><td>VM4</td><td>-0.4457</td><td>-0.1083</td><td>0.0053</td><td>0.5487</td></tr><tr><td>PDVM4</td><td>-0.1820</td><td>-0.0575</td><td>-0.0003</td><td>0.2398</td></tr><tr><td>LATEROUN</td><td>0.0760</td><td>0.0124</td><td>-0.0080</td><td>-0.0804</td></tr><tr><td>LATEVM2</td><td>0.0695</td><td>0.0074</td><td>-0.0095</td><td>-0.0674</td></tr><tr><td>LATEVM3</td><td>0.0935</td><td>0.0111</td><td>-0.0122</td><td>-0.0924</td></tr><tr><td>LATEVM4</td><td>0.1839</td><td>0.0107</td><td>-0.0290</td><td>-0.1657</td></tr></table>

## 6. Conclusions

In the past few years, we have seen fundamental advances in the theory of combinatorial auctions. Designs such as iBundle are based on strong theoretical foundations and even provide equilibrium analysis for a restricted set of value models that satisfy buyer submodularity conditions. In addition, a number of linear price auction formats have been suggested in the literature and also proposed for the design of the spectrum auctions by the U.S. Federal Communications Commission. We do not know of any other lab experiment that compares these different approaches using a uniform experimental environment that includes uniform software, a user interface, and experimental design.

In this paper, we provide experimental results comparing some of the main approaches for iterative combinatorial auctions that have been discussed in the literature, namely, iBundle, the combinatorial clock auction, and ALPS as a format with pseudodual linear prices. These formats are compared against the VCG mechanism.

We have compared the auction formats based on 5 different value models with $3 , 6 , 9 ,$ and 18 items. Although bidder behavior was heterogeneous and did not follow the pure best-response strategy in any of the auction formats, we did achieve high levels of efficiency in all auction formats. Actually, we did not find a significant difference in efficiency across all auction formats. With respect to auctioneer revenue, we did find the revenue in the VCG auction to be significantly lower than the one in iterative combinatorial auctions as predicted by the simulation results. Though these lab experiments suggest that all auction formats are robust against nonbest-response bidding, computational experiments have shown that this can actually lead to significant efficiency losses in iBundle (Schneider et al. 2008). We were, however, unable to finish iBundle with larger value models due to the large number of auction rounds. Our main contribution is the analysis of individual-level bidding behavior, which is largely missing in the literature but essential for understanding future auction designs. It reveals considerable bidder idiosyncracies and significant deviations from best-response bidding, even in iBundle where there are strong incentives to follow a respective strategy.

Theoretical contributions show what it would take to design an “ideal” auction, i.e., an auction with strong game-theoretical solution concepts and full efficiency. As we could show in our experiments, the assumptions in iBundle (Parkes and Ungar 2000), which are similar to those in the dVSV auction (de Vries et al. 2007), might not always be given in the lab or in the field. First, the number of auction rounds required in iBundle is too high already for small auctions with six or more items. Second, valuation models do not satisfy buyer submodularity conditions in most realistic settings. Third, bidders can often not be expected to strictly follow best-response strategies in difficult decision situations. The bidder has to choose one or more bundles from a set that is exponential in the number of items, plus he has to decide a bid price on any of these. This is not to diminish the significant contribution that respective designs made for the understanding of combinatorial auction designs.

If the assumptions for a game with strong solution concepts cannot be expected to hold in a particular market, one has to search for satisfying solutions. An important goal of this line of research is the development of auction formats that achieve high levels of efficiency in the lab and in the field. Consequently, robustness of these auction formats against different bidding strategies is an important design goal. Decision support in terms of ask prices, prepackaging, and automated payoff calculation can be important features in large combinatorial auctions. Though impossibility results show that exact linear prices are not always possible, there are various ways that auctioneers can provide feedback and bidders can be supported in selecting bundles and determining competititve bid prices (Adomavicius and Gupta 2005, Bichler et al. 2009, Porter et al. 2003). The empirical results in this paper provide insights for the development of new combinatorial auction designs that propose robust solutions to the problem of allocating multiple items in a combinatorial auction.

## 7. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

Financial support from the Deutsche Forschungsgemeinschaft (DFG) (BI 1057/3-1) is gratefully acknowledged. The authors thank Georg Ziegler for his help in organizing the laboratory experiments. The authors also thank Jacob Goeree, Richard Steinberg, David Parkes, and anonymous referees for their helpful comments and suggestions.

## Appendix. Bidder Valuations

The valuations for VM1 and VM2 are given in the Tables 1 and 2. VM3 contains the 6 items (A, B, C, D, E, and F) and, over all bidders, contains 26 valuated bundles. Figure A1(a) shows all given valuations for all bidders. VM4 comprises 9 items (A, B, C, D, E, F, G, H, and I) and, as shown in Figure A1(b), the bidders are interested in 51 different bundles.

Figure A1(a) Shows the Bidders’ Valuations in VM3

<table><tr><td>Bundle</td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td></tr><tr><td>{A}</td><td>9.0</td><td>6.0</td><td></td><td>9.0</td></tr><tr><td>{B}</td><td>6.0</td><td>6.0</td><td></td><td>12.0</td></tr><tr><td>{C}</td><td>6.0</td><td>9.0</td><td></td><td>9.0</td></tr><tr><td>{D}</td><td>6.0</td><td>3.0</td><td></td><td>8.0</td></tr><tr><td>{E}</td><td>3.0</td><td>3.0</td><td></td><td>11.0</td></tr><tr><td>{F}</td><td>3.0</td><td>6.0</td><td></td><td>8.0</td></tr><tr><td>{A,B}</td><td>17.0</td><td>14.0</td><td>14.0</td><td></td></tr><tr><td>{A,D}</td><td>17.0</td><td>11.0</td><td>16.0</td><td>9.0</td></tr><tr><td>{A,E}</td><td></td><td></td><td></td><td>11.0</td></tr><tr><td>{A,F}</td><td></td><td></td><td></td><td>12.0</td></tr><tr><td>{B,C}</td><td>14.0</td><td>17.0</td><td>11.0</td><td></td></tr><tr><td>{B,D}</td><td></td><td></td><td></td><td>12.0</td></tr><tr><td>{B,E}</td><td>11.0</td><td>11.0</td><td>10.0</td><td>12.0</td></tr><tr><td>{B,F}</td><td></td><td></td><td></td><td>12.0</td></tr><tr><td>{C,D}</td><td></td><td></td><td></td><td>12.0</td></tr><tr><td>{C,E}</td><td></td><td></td><td></td><td>11.0</td></tr><tr><td>{C,F}</td><td>11.0</td><td>17.0</td><td>10.0</td><td>9.0</td></tr><tr><td>{A,B,C}</td><td></td><td></td><td>25.0</td><td></td></tr><tr><td>{A,B,D}</td><td></td><td></td><td>27.0</td><td></td></tr><tr><td>{A,B,E}</td><td></td><td></td><td>24.0</td><td></td></tr><tr><td>{B,C,E}</td><td></td><td></td><td>21.0</td><td></td></tr><tr><td>{B,C,F}</td><td></td><td></td><td>21.0</td><td></td></tr><tr><td>{A,B,C,D}</td><td></td><td></td><td>32.0</td><td></td></tr><tr><td>{A,B,C,F}</td><td></td><td></td><td>29.0</td><td></td></tr><tr><td>{A,B,D,E}</td><td></td><td></td><td>31.0</td><td></td></tr><tr><td>{B,C,E,F}</td><td></td><td></td><td>25.0</td><td></td></tr></table>

Figure A1(b) Shows the Bidders’ Valuations in VM4

<table><tr><td>Bundle</td><td>Bidder 1</td><td>Bidder 2</td><td>Bidder 3</td><td>Bidder 4</td></tr><tr><td>{A}</td><td>10.0</td><td>5.0</td><td>2.0</td><td></td></tr><tr><td>{B}</td><td>5.0</td><td>10.0</td><td>5.0</td><td></td></tr><tr><td>{C}</td><td>2.0</td><td>5.0</td><td>10.0</td><td></td></tr><tr><td>{D}</td><td>5.0</td><td>2.0</td><td>1.0</td><td></td></tr><tr><td>{E}</td><td>2.0</td><td>5.0</td><td>2.0</td><td></td></tr><tr><td>{F}</td><td>1.0</td><td>2.0</td><td>5.0</td><td></td></tr><tr><td>{G}</td><td>2.0</td><td>1.0</td><td>0.0</td><td></td></tr><tr><td>{H}</td><td>1.0</td><td>2.0</td><td>1.0</td><td></td></tr><tr><td>{I}</td><td>0.0</td><td>1.0</td><td>2.0</td><td></td></tr><tr><td>{A,B}</td><td>16.0</td><td>16.0</td><td>8.0</td><td></td></tr><tr><td>{A,D}</td><td>16.0</td><td>8.0</td><td>4.0</td><td></td></tr><tr><td>{B,C}</td><td>8.0</td><td>16.0</td><td>16.0</td><td></td></tr><tr><td>{B,E}</td><td>8.0</td><td>16.0</td><td>8.0</td><td></td></tr><tr><td>{C,F}</td><td>4.0</td><td>8.0</td><td>16.0</td><td></td></tr><tr><td>{D,E}</td><td>8.0</td><td>8.0</td><td>4.0</td><td></td></tr><tr><td>{D,G}</td><td>8.0</td><td>4.0</td><td>2.0</td><td></td></tr><tr><td>{E,F}</td><td>4.0</td><td>8.0</td><td>8.0</td><td></td></tr><tr><td>{E,H}</td><td>4.0</td><td>8.0</td><td>4.0</td><td></td></tr><tr><td>{F,I}</td><td>2.0</td><td>4.0</td><td>8.0</td><td></td></tr><tr><td>{G,H}</td><td>4.0</td><td>4.0</td><td>2.0</td><td></td></tr><tr><td>{H,I}</td><td>2.0</td><td>4.0</td><td>4.0</td><td></td></tr><tr><td>{A,B,C}</td><td>22.0</td><td>30.0</td><td>28.0</td><td></td></tr><tr><td>{A,D,G}</td><td>22.0</td><td>19.0</td><td>15.0</td><td></td></tr><tr><td>{B,E,H}</td><td>13.0</td><td>28.0</td><td>19.0</td><td></td></tr><tr><td>{C,F,I}</td><td>9.0</td><td>19.0</td><td>28.0</td><td></td></tr><tr><td>{D,E,F}</td><td>13.0</td><td>20.0</td><td>19.0</td><td></td></tr><tr><td>{G,H,I}</td><td>9.0</td><td>15.0</td><td>15.0</td><td></td></tr><tr><td>{A,B,D,E}</td><td></td><td></td><td></td><td>14.0</td></tr><tr><td>{B,C,E,F}</td><td></td><td></td><td></td><td>32.0</td></tr><tr><td>{D,E,G,H}</td><td></td><td></td><td></td><td>9.0</td></tr><tr><td>{E,F,H,I}</td><td></td><td></td><td></td><td>14.0</td></tr><tr><td>{A,B,C,D,E}</td><td></td><td></td><td></td><td>36.0</td></tr><tr><td>{A,B,C,E,F}</td><td></td><td></td><td></td><td>40.0</td></tr><tr><td>{A,B,D,E,F}</td><td></td><td></td><td></td><td>25.0</td></tr><tr><td>{A,B,D,E,G}</td><td></td><td></td><td></td><td>21.0</td></tr><tr><td>{A,B,D,E,H}</td><td></td><td></td><td></td><td>21.0</td></tr><tr><td>{A,D,E,G,H}</td><td></td><td></td><td></td><td>17.0</td></tr><tr><td>{B,C,D,E,F}</td><td></td><td></td><td></td><td>39.0</td></tr><tr><td>{B,C,E,F,H}</td><td></td><td></td><td></td><td>39.0</td></tr><tr><td>{B,C,E,F,I}</td><td></td><td></td><td></td><td>40.0</td></tr><tr><td>{B,D,E,G,H}</td><td></td><td></td><td></td><td>20.0</td></tr><tr><td>{B,E,F,H,I}</td><td></td><td></td><td></td><td>25.0</td></tr><tr><td>{C,E,F,H,I}</td><td></td><td></td><td></td><td>36.0</td></tr><tr><td>{D,E,F,G,H}</td><td></td><td></td><td></td><td>20.0</td></tr><tr><td>{D,E,F,H,I}</td><td></td><td></td><td></td><td>21.0</td></tr><tr><td>{D,E,G,H,I}</td><td></td><td></td><td></td><td>17.0</td></tr><tr><td>{E,F,G,H,I}</td><td></td><td></td><td></td><td>21.0</td></tr><tr><td>{A,B,C,D,E,F}</td><td></td><td></td><td></td><td>50.0</td></tr><tr><td>{A,B,D,E,G,H}</td><td></td><td></td><td></td><td>31.0</td></tr><tr><td>{B,C,E,F,H,I}</td><td></td><td></td><td></td><td>50.0</td></tr><tr><td>{D,E,F,G,H,I}</td><td></td><td></td><td></td><td>31.0</td></tr></table>

## References

Adomavicius, D., A. Gupta. 2005. Toward comprehensive real-time bidder support in iterative combinatorial auctions. Inform. Systems Res. 16(2) 169–185.

Ausubel, L., P. Milgrom. 2006a. Ascending proxy auctions. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Ausubel, L., P. Milgrom. 2006b. The lovely but lonely Vickrey auction. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Ausubel, L., P. Cramton, P. Milgrom. 2006. The clock-proxy auction: A practical combinatorial auction design. P. Cramton, Y. Shoham, R. Steinberg, eds. Combinatorial Auctions. MIT Press, Cambridge, MA.

Banker, R. D., R. J. Kauffman. 2004. 50th anniversary article: The evolution of research on information systems: A fiftieth-year survey of the literature in management science. Management Sci. 50(3) 281–298.

Banks, J., J. Ledyard, D. Porter. 1989. Allocating uncertain and unresponsive resources: An experimental approach. RAND J. Econom. 20 1–25.

Banks, J., M. Olson, D. Porter, S. Rassenti, V. Smith. 2003. Theory, experiment and the FCC spectrum auctions. J. Econom. Behav. Organ. 51 303–350.

Bapna, R., P. Goes, A. Gupta. 2000. A theoretical and empirical investigation of multi-item on-line auctions. Inform. Tech. Management 1(1–2).

Bapna, R., P. Goes, A. Gupta. 2001. Insights and analyses of online auctions. Comm. ACM 44(11) 42–50.

Bichler, M., P. Shabalin, A. Pikovsky. 2009. A computational analysis of linear-price iterative combinatorial auctions. Inform. Systems Res. 20(1) 33–59.

Brunner, C., J. K. Goeree, C. A. Holt, J. Ledyard. 2009. An experimental test of flexible combinatorial spectrum auction formats. Amer. Econom. J.: Microeconom. Forthcoming.

Chen, Y., K. Takeuchi. 2008. Multi-Object Auctions with Package Bidding: An Experimental Comparison of Vickrey and iBEA. Games Econom. Behav. Forthcoming.

Cramton, P. 1995. Money out of thin air: The nationwide narrowband PCS auction. J. Econom. Management Strategy 4(2) 267–343.

Cramton, P., J. A. Schwartz. 2000. Collusive bidding in the FCC spectrum auctions. J. Regulatory Econom. 17(3) 229–252.

de Vries, S., J. Schummer, R. Vohra. 2007. On ascending Vickrey auctions for heterogeneous objects. J. Econom. Theory 132 95–118.

Dunford, M., K. Hoffman, D. Menon, R. Sultana, T. Wilson. 2007. Testing linear pricing algorithms for use in ascending combinatorial auctions. Technical report, George Mason University, Fairfax, VA.

Fan, M., J. Stallaert, A. Whinston. 2003. Decentralized mechanism design for supply chain organizations using auction market. Inform. Systems Res. 14(1) 1–22.

Goeree, J. K., C. A. Holt. 2009. Hierarchical package bidding: A paper and pencil combinatorial auction. Games Econom. Behav. Forthcoming.

Greene, W. H. 2003. Econometric Analysis. Prentice Hall, Upper Saddle River, NJ.

Isaac, R., D. James. 2000. Robustness of the incentive compatible combinatorial auction. Experiment. Econom. 3 31–53.

Isaac, M., T. Salmon, A. Zillante. 2007. A theory of jump bidding in ascending auctions. J. Econom. Behav. Organ. 62 144–164.

Kagel, J. H., D. Levin. 1985. Individual bidder behavior in first-price private value auctions. Econom. Lett. 19 125–128.

Kazumori, E. 2005. Auctions with package bidding: An experimental study. Technical report, The Center for Advanced Research in Finance, The University of Tokyo, Tokyo.

Kelly, F., R. Steinberg. 2000. A combinatorial auction with multiple winners for universal service. Management Sci. 46(4) 586–596.

Kwasnica, T., J. O. Ledyard, D. Porter, C. DeMartini. 2005. A new and improved design for multiobjective iterative auctions. Management Sci. 51(3) 419–434.

Ledyard, J., D. Porter, A. Rangel. 1997. Experiments testing multiobject allocation mechanisms. J. Econom., Management, Strategy 6 639–675.

Milgrom, P. R., R. J. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50(5) 1089–1122.

Parkes, D., L. H. Ungar. 2000. Iterative combinatorial auctions: Theory and practice. Proc. 17th National Conf. Artificial Intelligence (AAAI-17) and the 12th Conf. Innovative Applications Artificial Intelligence, AAAI Press/MIT Press, Menlo Park, CA.

Plott, C., T. Salmon. 2002. The simultaneous ascending auction: Dynamics of price adjustment in experiments and in the U.K. 3G spectrum auction. Social Science Working Paper 1155. California Institute of Technology, Pasadena, CA.

Porter, D., S. Rassenti, A. Roopnarine, V. Smith. 2003. Combinatorial auction design. Proc. National Acad. Sci. USA 100 11153–11157.

Rassenti, S., V. L. Smith, R. L. Bulfin. 1982. A combinatorial auction mechanism for airport time slot allocations. Bell J. Econom. 13 402–417.

Roth, A. 1988. Laboratory experimentation in economics: A methodological overview. Econom. J. 98 974–1031.

Rothkopf, M. H. 2007. Decision analysis: The right tool for auctions. Decision Anal. 4/3 167–172.

Sargent, T. J. 1993. Bounded Rationality and Macroeconomics. Oxford University Press, New York.

Schneider, S., P. Shabalin, M. Bichler. 2008. On the robustness of non-linear personalized price combinatorial auctions. Eur. J. Oper. Res. Forthcoming.

Vickrey, W. 1961. Counterspeculation, auctions, and competitive sealed tenders. J. Finance 1(3) 8–37.

Xia, M., G. J. Koehler, A. B. Whinston. 2004. Pricing combinatorial auctions. Eur. J. Oper. Res. 154(1) 251–270.
