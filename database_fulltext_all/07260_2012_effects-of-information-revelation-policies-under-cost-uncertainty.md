---
otero_id: 7260
otero_key: "G4FMD74V"
title: "Effects of Information Revelation Policies Under Cost Uncertainty"
authors: "Karthik N. Kannan"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0292"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/G4FMD74V/fulltext/images/187cfeadaca01ae5fc909517a5531ec87c18e834da929ca59eab0b087d64000f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Effects of Information Revelation Policies Under Cost Uncertainty

Karthik N. Kannan,

## To cite this article:

Karthik N. Kannan, (2012) Effects of Information Revelation Policies Under Cost Uncertainty. Information Systems Research 23(1):75-92. http://dx.doi.org/10.1287/isre.1100.0292

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/G4FMD74V/fulltext/images/d245bb9807d5523043d334e2606d8dd8ae190808e6aa2c24ba5d28416935521e.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Effects of Information Revelation Policies Under Cost Uncertainty

Karthik N. Kannan

Krannert School of Management, Purdue University, West Lafayette, Indiana 47907, kkarthik@purdue.edu

he paper presents insights regarding the key learning-related factors a buyer should consider when deciding the extent to which information about bids is revealed in a procurement auction context. It offers the insights by analyzing the following two first-price sealed-bid policies in a private-value sequential auction with no winner dropouts: (i) <sup>iis</sup>, where only the winner’s bid is revealed, and (ii) <sup>cis</sup>, where all bids are revealed. Our analysis identifies two important learning effects—the extraction and the deception effects—as having significant welfare implications. Both these effects arise because of a bidder’s desire to gain an informational advantage relative to his competitors, but their manifestations are different. The extraction effect occurs because of a bidder’s incentive to learn about his competitors, and the deception effect is a consequence of the incentive to prevent an opponent from gaining the information. Both effects lead to higher bid prices, and either may be dominant from a procurer surplus standpoint. With the deception effect, social welfare can decrease even when the number of suppliers increases, a result that is counterintuitive. The paper also discusses how insights regarding the learning effects might apply to other policies.

Key words: information revelation; electronic markets; economics of information systems; perfect Bayesian Nash equilibrium; auctions

History: Paulo Goes, Senior Editor; Vijay Mookerjee, Associate Editor. This paper was received August 30, 2008, and was with the authors for $7 \frac { 3 } { 4 }$ months for 1 revision. Published online in Articles in Advance June 14, 2010.

## 1. Introduction and Problem Motivation

The research problem in this paper is motivated by conversations with Freemarkets (now Ariba), a firm that executes electronic reverse auctions (or market sessions) at the request of procurers. Each procurer initiating a market session has to choose an information policy, i.e., the nature of information—bids submitted, rank of the bidder, etc.—that is revealed to suppliers at the beginning, during, and/or at the end of a market session. In Freemarkets, a procurer can choose from among a wide range of information policies to accept sealed bids with minimal feedback to the suppliers; provide rank information as feedback; or conduct an open-cry auction. In fact, different information policies have been adopted in various electronic (Jap 2002, 2003) and traditional procurement markets (McAfee and McMillan 1988, Hausch 1986). Even with electronic procurement auction systems installed at individual firms, the information policy is an important design element (for example, see Elmaghraby and Keskinocak 2000). This paper will provide insights for guiding the choice of information policy in a procurement auction.

In procurement scenarios, the nature of competition is known to be similar across market sessions, with the same set of suppliers repeatedly competing (Milgrom and Weber 1982, as well as anecdotal evidence from Freemarkets). With the repeated competition, depending on the information revealed, suppliers alter their behaviors to learn private information about their opponents, such as costs. Thus, the information policy choice affects market outcomes. It can be extrapolated from other contexts that market outcomes, including procurer surplus, do not always vary monotonically with the information revealed. However, that extrapolation in itself is insufficient to guide the choice of information policy. Moreover, to the best of our knowledge, no generic analysis of information policies applicable to this setting is available. This paper provides insights regarding some of the key bidding-related factors a buyer should consider when choosing an information policy.

We study a first-price, sealed-bid, private-value sequential auction with no winner dropout under the following two policies:

• Complete Information Policy (<sup>cis</sup>): All bids are revealed at the end of the market session. This policy is similar to the one adopted for municipal construction contracts (Hausch 1986).

• Incomplete Information Policy (<sup>iis</sup>): Only the winner’s bid is revealed at the end of the market session. Some government procurement auctions are required by statute to adhere to this policy (McAfee and McMillan 1988).

<sup>cis</sup> and <sup>iis</sup> are two of the many policies available to a procurer initiating marketing sessions at Freemarkets (Arora et al. 2007). Not only are they commonly adopted in electronic and traditional markets, but they have also been analyzed in prior work (although in different contexts). For example, Arora et al. (2007) and Greenwald et al. (2009) compare <sup>cis</sup> and <sup>iis</sup>; Ortega-Reichert (1968) and Hausch (1986) investigate <sup>cis</sup>.

Our analysis of the two policies identifies two learning-related effects—the extraction and the deception effects—as being key factors having significant welfare implications. Both effects are consequences of a bidder’s desire to gain an informational advantage relative to his competitors, but their manifestations are quite different. The extraction effect, which occurs under <sup>iis</sup>, is a consequence of a bidder’s interest in learning about his opponent; but the deception effect, which is observed under <sup>cis</sup>, is an outcome of the bidder’s interest to prevent an opponent from learning about him. Each of these effects leads to a higher bid price and is significant enough to dominate the other from a supplier profit standpoint. In our setting, loosely speaking, the supplier profit comparisons are the opposite of the procurer surplus comparisons. Thus, our analysis also provides insights for a procurer choosing an information policy. It is not just the managerial insights that are interesting, but also the manner in which we demonstrate them. Corresponding to the condition when both the effects occur, neither <sup>cis</sup> nor <sup>iis</sup> has a generic closed-form expression for the equilibrium strategies; yet we prove the comparison results.

We also evaluate the social welfare generated under the policies. When analyzing its sensitivity to the exogenous parameters, we find that the learning effects lead to a counterintuitive observation. One would expect that, as the number of competitors increases, the market becomes more competitive and hence more efficient. However, we find that the social welfare can also decrease with an increase in the number of competitors. This result has implications for a social planner.

The research problem investigated in this paper overlaps many domains that appeal to the information systems (IS) research audience. First, several papers by IS researchers (e.g., Koppius 2002, Arora et al. 2007, Mithas and Jones 2007, Adomavicius et al. 2008, Greenwald et al. 2009) have analyzed the impact of the information revealed in procurement contexts (the focus has been different). This paper contributes to that growing body of knowledge. Second, we investigate the dynamics arising because of varying information levels. Specifically, our paper focuses on the learning-related dynamics. The topic of informational dynamics and information transparencies is also of interest to the IS community (e.g., Granados et al. 2005, Goes et al. 2009). Third, the paper offers insights regarding electronic markets, which is also a research theme of interest to many in the IS area (e.g., Yoo et al. 2007, Kumar et al. 2007, Adomavicius et al. 2009).

The rest of the paper is organized as follows. In §2, we review the related literature. Following that, we present our model in §3 and solve for equilibria in §4. The policies are compared in §5. Section 6 presents some generalization results. Finally, we discuss the results in §7 and conclude in §8.

## 2. Literature Review

In this section, we survey the literature in the following streams of research: literature studying the impact of information on auction markets, sequential auctions in economics, and information policies in procurement contexts.<sup>1</sup>

## 2.1. Impact of Information in Auctions

Several studies have considered the information impact on auction performances. To be brief, in this section we only survey a few of the key ones. Wilson (1977) has one of the first papers to study the information impact in auctions. He considers a single-period auction where the bidders are unaware of their valuation. He shows that when bidders base their bids only on the private sample information they get, the maximum bid is almost surely equal to the true value. Winkler and Brooks (1980) investigated the impact of uncertainty in a common value auction. They demonstrate how the valuation dependence is related to “winner’s curse.” The seminal work from Milgrom and Weber (1982) also studies the information impact in one of the subsections. In that, they recommend that the auctioneer reveal all bidder-related valuation to maximize surplus based on their analysis of a single-period auction setting where the bidder valuations are affiliated. This result is often extended to our setup to claim that, because bids are surrogates for valuation information, it is optimal for the procurer to reveal all the information. As we show later, such a result is not applicable to our context.

## 2.2. Sequential Auctions Literature

There is a large body of literature on sequential auctions. Within that, there are two main streams. In one, the winning bidder drops out of the future periods; in the other, the winner continues to participate. Because the reverse auction contexts we study, involve repeated competition among the same set of sellers (Milgrom and Weber 1982, as well as anecdotal evidence from Freemarkets), they relate to the latter stream. However, as Klemperer (2004) notes, much of the literature has focused on the former. Krishna (2009, p. 221) observes the main problem affecting analysis of the “no dropout” scenario is that “even if bidders are symmetric ex ante, multiunit demands [or simply, the no drop out scenario] introduce asymmetries in later auctions.” Thus, as Laffont (1997) concludes, “The theory is more complex.” Also because of the differences between the two sequential auction streams, one cannot extrapolate results from one to the other. For example, the revenue equivalence between the first- and the second-price auctions holds when the winner drops out (Krishna 2009) but not with “no dropout” (Hausch 1988).

Among the articles that model the winner not dropping out, Ortega-Reichert (1968) and Hausch (1986) have considered problems related to ours. Ortega-Reichert (1968) is the first study to focus on sequential auctions with no dropouts. He analyzes a first-price, sealed-bid, common-value auction with two people and two market sessions (each of which corresponds to a period) under <sup>cis</sup>-like policy. He discovers that there exists a symmetric pure strategy equilibrium that reveals the bidder’s information in the first period. Hausch (1986) builds on the setting and compares <sup>cis</sup> against a simultaneous auction scenario. He shows that, under different conditions, either policy may be better from a bidder standpoint. Our private-value auction framework is different from the common-value auction studied in both papers. We also study <sup>iis</sup>.

More recently, Tu (2005) in his thesis also considers the same problem even though the results are different. Note that his work at best can be considered parallel to ours (an earlier version of our paper can be easily shown to precede Tu 2005). He models a two-player game and characterizes the equilibrium by making a critical assumption. Specifically, he explicitly assumes that pooling of bids is not permitted (i.e., players do not fake their types), an assumption that we believe is unrealistic in this context. With such an assumption, Tu shows that <sup>cis</sup> always generates higher procurer surplus than <sup>iis</sup>. However, we believe that one of the key reasons our results are different is that we do not make the same assumption. We demonstrate that <sup>iis</sup> can generate a higher procurer surplus. We also demonstrate the robustness of our result for any arbitrary number of suppliers, not just for two. Extending the proofs beyond two suppliers involves additional complications.

There is also some overlap with the literature on mergers. Thomas (1996) analyzes how the vertical mergers may be different to horizontal mergers. With a two-player game, where the player type (either high or low) is equally likely, he concludes that merged entities with complete information flow between them are better for the procurer than unmerged ones. Contrary to his conclusion, our analysis shows that a policy that does not completely reveal information may be dominant. Moreover, the stochastic dominance results and the social welfare results we later prove are not even present there. Furthermore, we demonstrate our results for any arbitrary number of suppliers.<sup>2</sup>

2.3. Information Policies in Procurement Settings Our paper best fits this stream of research. There is an increasing interest in the IS community in studying information policies. The most closely related work is Arora et al. (2007), which compares <sup>cis</sup> and <sup>iis</sup> in a setting with homogeneous bidders facing uncertainty about the number of their competitors. Thus, theirs is a common-value setup. They prove that the procurer surplus varies non-monotonically with the information revealed and recommend <sup>cis</sup> from a procurer standpoint. First, note that ours is a private value setup. Second, one of their key assumptions— which is the non-zero probability of a bidder being a monopolist in the market—does not always hold in real life. This assumption is violated when requirements regarding the minimum number of suppliers is imposed (e.g., OMB 1993, United-Nations 2007). Third, our results are different because, in our setting, the procurer surplus under <sup>iis</sup> can also be higher.

Another related paper is Greenwald et al. (2009); that paper primarily develops a computational test bed to enable comparisons of policies by building on a previous version of our paper. That paper also demonstrates the usefulness of the test bed by comparing <sup>cis</sup> and <sup>iis</sup> policies in an analytically intractable setup, where both types of uncertainties— uncertainty about the number of competitors as well as about their costs—are jointly present. The development of the test bed treats bidder behavior as a black box and considers the procurer surplus as the only metric of analysis. In fact, no equilibrium bid distribution is specified in the paper. Bid distributions are relevant only to demonstrate the performance of the proposed algorithm. Even to do that, the paper primarily considers a single-period game. However, for such a game, the deception and extraction effects never arise. In short, that paper neither establishes the presence of the learning effects nor demonstrates the dominance of the effects. To the contrary, our paper identifies the learning effects and also studies their welfare implications.

Koppius (2002) has experimentally analyzed the impact of revelation policies on bidder behavior in a multidimensional procurement auction. He infers that, when the suppliers have the least level of uncertainty about the weights a procurer places on the multiple dimensions, the supplier profits are maximized. Our focus is quite different in that we do not analyze the impact of information-processing capacities of the suppliers but consider the strategic behavior that suppliers exhibit along with the nature of the information revealed.

Mithas and Jones (2007) present an empirical analysis based on data from a real-life electronic marketplace. The paper does not specifically consider the policies considered here. Their analysis shows that there is no monotonicity in the procurer surplus with the information revealed to the bidders. The analysis is, however, limited in its ability to explicate the strategies adopted by the suppliers. This is so because they do not have the data to track how suppliers bid across market sessions. The focus of this paper is quite different from theirs in that we are not only compare the procurer surplus but also develop an understanding of the bidding behavior in response to information policies. Moreover, the methodology adopted is different.

In a recent study, Adomavicius et al. (2008) use a laboratory experiment to study the role of information in a combinatorial procurement auction setting, where each market session involves multiple rounds. They study three policies that differ in the information revealed: (i) the provisional allocation (e.g., the current rank) is revealed; (ii) task-related information (e.g., the price or level of quality needed to win the auction) specific to each bidder is provided; and (iii) a menu of prices along with the possible ranks and the profits generated—again, specific to the bidder—is provided. Based on the experimental data, Adomavicius et al. infer that the procurer generates the maximum surplus with the second policy. The paper also empirically investigates the changes in bidder behaviors observed with the varying levels of feedback.

Table 1 provides a summary of how this paper compares to related prior analytical works on information policies.

## 3. Model

Our model is closely related to those in Hausch (1986) and Arora et al. (2007). We treat the procurement context as an independent private value auction. Such a treatment is generally accepted (e.g., Maskin and Riley 2000b, Bajari 2001, Brosig and Reiss 2007,

Table 1 Comparison of Related Analytical Works on Information Policies

<table><tr><td>Paper</td><td>Setting</td><td>Relationship between procurer surplus and the information revealed</td></tr><tr><td>Hausch (1986)</td><td>Common value setting</td><td>cis or simultaneous auction; it varies depending on the priors.</td></tr><tr><td>Arora et al. (2007)</td><td>Common value setting but with numbers uncertainty</td><td>cis preferred from a procurer standpoint.</td></tr><tr><td>Thomas (1996)</td><td>Private value setting with 2 bidders and equally likely cost types</td><td>cis preferred from a procurer standpoint.</td></tr><tr><td>Tu (2005)</td><td>Private value setting with 2 bidders, and no pooling strategy allowed</td><td>cis preferred from a procurer standpoint.</td></tr><tr><td>This paper</td><td>Private value setting with an arbitrary number of bidders and an arbitrary probability of a bidder being low-cost type</td><td>Either cis or iis preferred from a procurer standpoint, depending on the probability of an opponent being low-cost type</td></tr></table>

Kostamis et al. 2009).<sup>3</sup> Our model employs a firstprice sealed bid auction, although we also briefly discuss the second-price mechanism in §7. Because we focus on the learning effects across market sessions, we consider two sequentially occurring market sessions or periods, each initiated by a different procurer. We assume that in each period the suppliers submit bids without any knowledge of their opponents’ bids for that period. Thus, ours is a simultaneous move game in each period.

We assume that there are n + 1 suppliers in the marketplace, where n is common knowledge. (Table 6 in the Online Appendix A shows the notations used in the paper.<sup>4</sup>) Hausch (1986) considers n = 1, i.e., a two-player game. Each supplier can be one of two types, depending on its marginal cost of production: a low- or a high-cost type. We assume that the marginal cost is c<sub>l</sub> for a low-cost type and $c _ { h }$ for a high-cost type, with $c _ { l } < c _ { h } . ^ { 5 }$ (In §6.1, we also discuss the result when the model involves three cost types.) Each supplier is aware of his own type, but uncertainty persists for him regarding his opponents’ types. Let the probability of a supplier being a low-cost type be , which is common knowledge.<sup>6</sup> Once a supplier’s cost is determined from the random draw, we assume that it remains the same across both periods.<sup>7</sup> Thus, the only difference between the two periods is the information set.

Bids submitted by the suppliers are often multidimensional in reality. The procurer may place weights over the different attributes and use a single metric to compare the bids. In certain markets, for example in the coal marketplace,<sup>8</sup> bidders may even be aware of the weights that the procurer places on each attribute. In such cases, a multidimensional bid may be collapsed into a single dimensional bid without loss of generality. This logic motivates the assumption of a single dimensional bid in electronic reverse markets in prior works (e.g., Carr 2003). We also assume that the bid submitted is a single dimensional price p, which is required to be nonnegative.

Next, we define the sequence of moves in our game. In the first period, all n + 1 suppliers submit the bid prices simultaneously. The supplier with the lowest price is picked as the winner; a tie is broken randomly. At the end of the period, information is revealed according to the revelation policy. At this stage, under both <sup>cis</sup> and <sup>iis</sup>, the winning supplier is awarded the contract and paid the bid amount; the supplier manufactures the product and incurs the marginal cost associated with his type. Table 2 captures the information that is revealed under the different information policies without the details regarding the awarding of the contracts. The second period is repeated in the same manner as the first.

Table 2 Information Revealed Under Each Policy

<table><tr><td>Instant</td><td>Complete information policy (cis)</td><td>Incomplete information policy (iis)</td></tr><tr><td>Beginning of the first period</td><td>Uncertain</td><td>Uncertain</td></tr><tr><td>End of the first period</td><td>All bids revealed</td><td>Only winner&#x27;s bid revealed</td></tr><tr><td>Beginning of the second period</td><td>All suppliers aware of all bids</td><td>Each loser is aware of the the winner&#x27;s bid.Winner from the first market session continues to be uncertain.</td></tr></table>

## 4. Equilibrium Analysis

Since our multiperiod game is a “game with incomplete information,” we use the perfect Bayesian Nash solution concept to determine the equilibrium. Such a concept allows us to account for the interdependencies among the first-period strategies, the updated belief for the second-period, and the second-period strategies. The following points are relevant before we solve for the equilibrium:

• We use the backward induction technique by first solving the second-period game. Our secondperiod game turns out to be a single-period game where the beliefs of the suppliers regarding the others may or may not be asymmetric. Games similar to the ones we encounter in the second period have already been analyzed in Maskin and Riley (1985), and it is well known that they do not always have an equilibrium. To overcome the problem, we employ the same technique as Maskin and Riley (1985). Actually, their Footnote 2 becomes directly applicable to our context: “As our model is formulated, an equilibrium in the sealed-bid auction may not exist. The nonexistence problem, however, is an artifact of our allowing literally a continuum of possible bids. In fact, we can restore existence even with a continuum by allowing the possibility of positive but infinitesimal bids, which we implicitly assume in our analysis.” For the sake of readability, we also make the same implicit assumption in the main manuscript and in the corresponding content in the appendix. The key difference is that, while they employ it for their single period game, we extend it to our two period game.<sup>9</sup>

• A high-cost supplier always bids a price of $c _ { h }$ (equal to his marginal cost), and it is quite easy to demonstrate $\mathbf { s o . } ^ { \mathrm { ~ i 0 } }$ Compared to it, computing the equilibrium of a low-cost type is fairly involved. ${ \mathrm { S o } } ,$ the rest of the analysis focuses on the low-cost suppliers’ bidding behavior.

## 4.1. Single-Period Game

In this section, we develop equilibrium results for a game that generalizes most of the single-period games that arise in our model context. This helps us avoid repeating the same intuitions. Consider the following game, which we will later refer to as the SPG (Single-Period Game). An instance of the game, for example, occurs in the second periods of <sup>iis</sup> and <sup>cis</sup>. The players in the game can be categorized into two sets. In the first set, there is only one low-cost supplier, $R _ { 1 }$ (the subscript refers to the only player), and the other n suppliers, each referred to as $R _ { o }$ (the subscript refers to the other players), are in the second set. For example, under <sup>iis</sup> in the second period, the firstperiod winner corresponds to $R _ { 1 }$ and each loser is $R _ { o } .$ The game is such that $R _ { 1 }$ believes that each of his n opponents $( R _ { o } )$ is a low-cost type with a probability of . Each $R _ { o }$ believes that $R _ { 1 }$ is a low-cost type with probability $\beta$ and that each of the other $R _ { o }$ suppliers is a low-cost type with probability of $\alpha .$ We always find that $\beta \ge \alpha$ and that both $\beta$ and  are common knowledge.

As mentioned earlier, an auction game similar to SPG has already been analyzed by Maskin and Riley (1985, §3). Adhering to their procedure, we solve for the equilibrium, which is unique (see Appendix B). The equilibrium is obtained by solving the following profit function expressions for $R _ { 1 }$ and a low-cost $R _ { o }$ from bidding any price $p { \mathrm { : } }$

$$
\begin{array}{l} \Pi_ {R _ {1}} (p) \\ = \left(\overbrace {\underbrace {(1 - \alpha)} ^ {\text {   That   supplier   is   a   high - cost   type   }} + \underbrace {\overbrace {\alpha (1 - F _ {R _ {o}} (p))} ^ {\text {   Consider   each   of   the   } R _ {o} s}} ^ {\text {   that   supplier   is   a   low - cost   type   and   is   outbid   }}} ^ {n}\right) ^ {n} \\ \cdot (p - c _ {l}), \quad \text { and } \\ \Pi_ {R _ {o}} (p) \\ = \underbrace {((1 - \beta) + \beta (1 - F _ {R _ {1}} (p)))} _ {\text { For   } R _ {1}} \underbrace {((1 - \alpha) + \alpha (1 - F _ {R _ {o}} (p)))} _ {\text { For   each   of   the   other   } R _ {o} s} ^ {n - 1} \\ \cdot (p - c _ {l}). \end{array} \tag {2}
$$

Here, $F _ { R _ { 1 } } ( p )$ is the cumulative density function (cdf) of the bid distribution for $R _ { 1 }$ and $F _ { R _ { o } } ( p )$ for $R _ { o } .$ There are only two key results from this game we carry along for the rest of the paper: (i) a lowcost type always bids $< c _ { h }$ and never bids like a high-cost type, i.e., it is a separating equilibrium, and (ii) $\Pi _ { R _ { 1 } } = \dot { \Pi _ { R _ { o } } } = ( 1 - \alpha ) ^ { n } ( c _ { h } - \dot { c } _ { l } )$ . Some may find the result surprising but it has been observed before for certain special cases of asymmetric auctions, including by Maskin and Riley (1985, §3) and Arora et al. (2007, Lemma 2). It can also be seen from the equilibrium calculations that, when $\alpha = \beta ,$ , i.e., bidders are symmetric, their bid distributions are identical.

Note that the values of  and $\beta$ vary across the policies, and they depend on how, in the first period of each policy, the suppliers bid. Our analysis will take into account these variations to derive the firstperiod strategies.

## 4.2. Two-Period Games

The steps involved in determining the perfect Bayesian Nash equilibrium (Fudenberg and Tirole 1994) are as follows. Under each policy, we first derive the second-period equilibrium when the firstperiod game has a separating equilibrium, i.e., a lowcost type bid $p < c _ { h } .$ . Following that, we obtain the first-period separating equilibrium and the conditions when such an equilibrium is valid in the first period. Eventually, for those conditions when a separating equilibrium does not exist in the first period, we determine the equilibrium for both periods.

4.2.1. <sup>iis</sup>. Under this policy, only the winner’s bid is revealed at the end of the first period. Let us represent the revealed bid with $p _ { w }$ . Suppose a separating equilibrium exists in the first period. If $p _ { w } = c _ { h } ,$ , it indicates that all participating suppliers are high-cost types. They continue to be bid $c _ { h }$ in the second period. Hence, analyzing that case is uninteresting.

If at least one of the suppliers is a low-cost type, then $p _ { w } \prec c _ { h } .$ In that case, let us map the second period game to SPG. Set $R _ { 1 }$ to be the winner, and $R _ { o }$ to represent every loser. Because the winner’s bid is announced and all the other suppliers observe the winning bid $p _ { w } < c _ { h } ,$ they learn that the winner is a low-cost type, i.e., $\beta = 1$ . However, the first-period winner continues to be uncertain about the cost types of other suppliers. Let the winner’s belief about each of the other suppliers being a high-cost type be $x ( p _ { w } )$ and let it be updated in a Bayesian manner:

$$
x (p _ {w}) = \underbrace {\frac {\overbrace {(1 - \theta)} ^ {\text { Prob.   of   a   supplier   being   a   high - cost   type }}}{1 - \theta + \theta (1 - F _ {1 , \text { ins }} (p _ {w}))}} _ {\text { Prob.   of   outbidding   the   supplier   with   a   bid   } p _ {w}},\tag{3}
$$

where $F _ { 1 , \mathrm { { m s } } } ( p )$ is the cdf of the first-period bid distribution at equilibrium. Hence, the common knowledge of $p _ { w }$ translates into the common knowledge of $x ( p _ { w } ) _ { \scriptscriptstyle { \it \ / w } }$ because bidders know the first-period bid distribution. So $\alpha = 1 - x ( p _ { w } )$ . With those values for  and $\beta ,$ our SPG analysis shows that the expected profits for any low-cost supplier is $( x ( p _ { w } ) ) ^ { n } ( c _ { h } - c _ { l } )$ in the second period.

Next, we compute the first-period equilibrium. If the supplier wins with a bid $p _ { 1 }$ in the first period, the conditional and unconditional second-period profits are straightforward to compute, because $p _ { w } = p _ { 1 }$ . If the supplier loses with a bid $p _ { 1 } ,$ the expected secondperiod profit has to consider all possible $p _ { w } s < p _ { 1 }$ and the probability of the winning bid being $p _ { w } .$ Thus, the expected profit across both periods from bidding $p _ { 1 }$ in the first period is:

$$
\begin{array}{l} \Pi_ {\mathrm{IIS}} (p _ {1}) \\ = \overbrace {(1 - \theta + \theta (1 - F _ {1 , \mathrm{IIS}} (p _ {1}))) ^ {n} (p _ {1} - c _ {l})} ^ {\text { First - period profits from bidding p } _ {1}} \\ + \overbrace {(1 - \theta + \theta (1 - F _ {1 , \mathrm{IIS}} (p _ {1}))) ^ {n} (x (p _ {1})) ^ {n} (c _ {h} - c _ {l})} ^ {\text { Second - period profits when he wins the first period with p } _ {1}} \\ + \underbrace \int_ {p _ {l} ^ {\mathrm{IIS}}} ^ {p _ {1}} (x (p)) ^ {n} (c _ {h} - c _ {l}) \sum_ {k = 1} ^ {n} \underbrace {\binom {n} {k} (1 - \theta) ^ {(n - k)} \theta^ {k}} _ {\text { Prob.   of   k   low - cost   rivals }} \underbrace {k f _ {1 , \mathrm{IIS}} (p) (1 - F _ {1 , \mathrm{IIS}} (p)) ^ {k - 1}} _ {\text { Prob.   that   one   of   them   wins   with   p }} d p, \end{array}\tag{4}
$$

where $f _ { 1 , \mathrm { I I S } } ( p )$ is the probability density function (pdf) of the first period bid distribution and $p _ { l } ^ { \mathrm { { m s } } }$ is the infimum of the first-period strategy set.

Using the above expressions, we compute (in Appendix C.1) the first-period equilibrium bid distribution, $F _ { 1 , \mathrm { { m s } } } ( p )$ , to be a solution to the following nonlinear equation:

$$
\begin{array}{l} (1 - \theta) ^ {n} \big (1 - n \log {(1 - \theta)} \big) (c _ {h} - c _ {l}) \\ = \big (1 - \theta + \theta (1 - F _ {1, \text {ns}} (p)) \big) ^ {n} (p - c _ {l}) \\ \qquad - (1 - \theta) ^ {n} n (c _ {h} - c _ {l}) \log {\big (1 - \theta + \theta (1 - F _ {1, \text {ns}} (p)) \big)}. \end{array}\tag{5}
$$

Although $F _ { 1 , \mathrm { { I I S } } } ( p )$ cannot be expressed in closed form, the distribution can be computed numerically. However, from Equation (5), one can analytically derive comparative results, such as $\partial F _ { 1 , \mathrm { I I S } } ( p ) \dot { / } \partial n \geq \dot { 0 }$ or $\partial { \cal F } _ { 1 , \mathrm { { n s } } } ( p ) / \partial \theta \geq 0 .$ , validating our intuition that, as the intensity of competition increases, bids tend to be lower. Among the sensitivity results, the most interesting one is:

<sup>Lemma</sup> <sup>1.</sup> Consider two settings that may have a different  and/or n. If the winning bid is the same in both settings, the winner’s second belief that none of the suppliers is a low-cost type across the two settings is the same, and independent of both  and n.

Under <sup>iis</sup>, bidders do not have an incentive to deviate from the separating equilibrium in the first period. We next present an informal argument to explain why a pooling strategy, which is to bid $c _ { h } ,$ , is not sustained. Suppose a low-cost supplier deviates in the first period and bids $p = c _ { h }$ . He is worse off now than before when none of his opponents is a low-cost type. Even if at least one low-cost supplier is present, he loses the first period. Because no other bid apart from the winner’s is observed anyway, the pooled bid does not serve to alter the second period beliefs of the winner. In that words, he is not better off in the latter case either. Therefore, by pooling, the bidder is actually worse-off. The interesting aspect of our result is that even though suppliers have an opportunity to signal their types differently, they have no incentive to do so. Because suppliers do not signal their types differently, our result under <sup>iis</sup> is mathematically similar to that from Arora et al. (2007). Note that suppliers in Arora et al. (2007) do not even have the opportunity to signal their types differently in that context.

As a consequence of the equilibrium, the total expected profits for a low-cost supplier across both the periods in <sup>iis</sup> is:

$$
\Pi_ {\mathrm{ns}} = (1 - \theta) ^ {n} (2 - n \log {(1 - \theta)}) (c _ {h} - c _ {l}).\tag{6}
$$

Compared to a single-period version of the same, the bid distributions in the first period are skewed to the right. This is because, under <sup>iis</sup>, suppliers are willing to lose in the first period in order to gain the informational advantage over the winner. This effect, which we refer to as the extraction effect, accounts for the supplier’s action to increase his bid in order to extract information or improve his information endowment about his opponents’ types for the future periods.

4.2.2. <sup>cis</sup>. Under this policy, recall that all bids are revealed. For the equilibrium analysis, we initially consider the case when only a separating equilibrium exists in the first period. The separating equilibrium is valid only under a certain condition. Eventually, we compute the alternate equilibrium.

Separating Equilibrium. Suppose a separating equilibrium exists in the first period. Then, because all bids are revealed under this policy, the second period is a Bertrand game. The expected second-period profit low-cost supplier is $\Pi _ { 2 , \mathrm { c I S } } ^ { \mathrm { s e p } } \dot { = } ( 1 - \theta ) ^ { n } ( c _ { h } - \dot { c } _ { l } )$

We next consider the first-period equilibrium. For a low-cost bidder, the total profit across both periods, if $F _ { 1 , \mathrm { c r s } } ^ { \mathrm { s e p } } ( p _ { 1 } )$ represents the cdf of the first period bid distribution for $p _ { 1 } < c _ { h } ,$ , is

$$
\begin{array}{c} \text {First - period profits from bidding p_{1}} \\ \Pi_ {\text {cis}} ^ {\text {sep}} (p _ {1}) = \overbrace {(1 - \theta + \theta (1 - F _ {1 , \text {cis}} ^ {\text {sep}} (p _ {1}))) ^ {n} (p _ {1} - c _ {l})} ^ {\text {Second - period profits when}} \\ + \overbrace {(1 - \theta) ^ {n} (c _ {h} - c _ {l})}. \end{array}\tag{7}
$$

The second-period payoff is a constant independent of $p _ { 1 }$ and can be ignored for equilibrium calculations. Without the term, the expected profit expressions are identical to SPG with $\alpha = \beta = \theta$ and hence, the equilibrium bid distributions are also the same.

The total expected profits across both periods in this case is

$$
\Pi_ {\mathrm{cis}} ^ {\mathrm{sep}} = 2 (1 - \theta) ^ {n} (c _ {h} - c _ {l}).\tag{8}
$$

We verify whether the separating equilibrium is always valid in the first period. By comparing the expected profits between the separating equilibrium and the faking strategies, we find in Appendix D.1 that a separating equilibrium in the first period only exists for $\theta \leq \theta _ { n } ^ { \mathrm { f a k e } } = 1 / ( 2 + n )$ . In the same appendix, we show that only a semipooling strategy exists for $\theta > \theta _ { n } ^ { \mathrm { f a k e } }$ . A semipooling equilibrium is one where a low-cost supplier mixes with bids $\boldsymbol { p } < \boldsymbol { c } _ { h }$ and also $p = c _ { h }$ (which is to fake).

The existence of a semipooling equilibrium implies that a supplier has an incentive to fake to inhibit his opponent from gaining information regarding the faking supplier’s type. By faking and deceiving his opponent, the supplier gains an opportunity to “low-ball” his opponents in the second period and gain. The resulting profit is higher than if the low-cost supplier reveals his type in the first period (so long as $\theta > \theta _ { n } ^ { \mathrm { f a k e } } )$ We refer to this faking as the deception effect.<sup>11</sup>

Table 3 The Second-Period Game Under <sup>cis</sup>

<table><tr><td>Case</td><td>Possibilities for the first-period game</td><td>Relationship to SPG</td><td>Second-period profits for a low-cost type</td></tr><tr><td>1.</td><td>All suppliers bid  $p = c_h$ . No one bids  $p < c_h$ .</td><td>Symmetric game; set  $\alpha = 1 - y$  and  $\beta = 1 - y$ .</td><td> $y^n(c_h - c_l)$ </td></tr><tr><td>2.</td><td>Only one of the suppliers bids  $p < c_h$ . All others bid  $p = c_h$ . (The low-cost types may even be faking.)</td><td>Asymmetric game; set  $\alpha = 1 - y$  for the winner.  $\beta = 1$  for the other low-cost types.</td><td> $y^n(c_h - c_l)$ </td></tr><tr><td>3.</td><td>At least two suppliers bid  $p < c_h$ .</td><td>None. In equilibrium, the low-cost suppliers bid  $p = c_i$ .</td><td>0</td></tr></table>

Semipooling Equilibrium. In this subsection, we characterize the semipooling equilibrium. For a given  and $n ,$ let $\gamma _ { \theta , n }$ represent the probability with which suppliers fake, i.e., the probability with which a lowcost supplier bids $p = c _ { h }$ in the first period. Because a pooling equilibrium does not exist, $\gamma _ { \theta , n } < 1$ . The firstperiod equilibrium computation involves characterizing $\gamma _ { \theta , n }$ in addition to characterizing the expression for how a low-cost supplier bids $p < c _ { h } .$ , the cdf of which we denote by $F _ { 1 , \mathrm { c r s } } ^ { \mathrm { s e m i } } ( p )$

The first-period equilibrium is driven by the second-period equilibria, which are computed as follows. If a low-cost supplier does not observe any price $p < c _ { h }$ bid in the first period, he updates his second period belief that each of its opponents is a high-cost type to

$$
y = \frac {(1 - \theta)}{1 - \theta + \theta \gamma_ {\theta , n}}
$$

in a Bayesian manner. If he instead, observes a price $p \textless c _ { h }$ in the first period, the second-period belief about having low-cost supplier is 1.

Depending on whether in the first period all suppliers faked, only one supplier reveals to be a lowcost type, or more than one supplier reveals low-cost structures, the outcome of the second period game is different. Table 3 shows the three possible games in the second column. Corresponding to each game, the third column matches the beliefs from each of the cases in SPG. In the last column, we show the expected supplier profits for each case. These secondperiod profits are taken into account while characterizing the first period equilibrium.

The total expected profit across both periods is expressed as follows. The profit for supplier i from bidding $p _ { 1 } < c _ { h }$ is

$$
\begin{array}{l} \Pi_ {\text { CIS }} ^ {\text { semi }} (p _ {1} \mid p _ {1} <   c _ {h}) = \overbrace {(1 - \theta + \theta (1 - F _ {1 , \text { CIS }} ^ {\text { semi }} (p _ {1}))) ^ {n} (p _ {1} - c _ {l})} ^ {\text { First - period profits from bidding } p _ {1} <   c _ {h}} \\ \quad + \underbrace {(1 - \theta + \theta \gamma_ {\theta , n}) ^ {n} y ^ {n} (c _ {h} - c _ {l})} _ {\text { Second - period profits: case 2 in Table 3 }; i \text { is the only supplier bidding } p _ {1} <   c _ {h}}. \end{array} \tag {9}
$$

The profit for supplier i from bidding $p _ { 1 } = c _ { h }$ is ç<sup>semi</sup><sub>cis</sub> 4c<sub>h</sub>5

$$
\begin{array}{c} \overbrace {(1 - \theta + \theta \gamma_ {\theta ,   n}) ^ {n} \frac {(c _ {h} - c _ {l})}{n + 1}} ^ {\text {First - period profits}} + \overbrace {[ 1 - \theta + \theta \gamma_ {\theta ,   n} ] ^ {n} y ^ {n} (c _ {h} - c _ {l})} ^ {\text {Second - period profits: Case 1 in Table 3}} \\ + y ^ {n} (c _ {h} - c _ {l}) \underbrace {\sum_ {k = 1} ^ {n}} _ {\text {At least one opponent exists}} \underbrace {\left(\binom {n} {k} (1 - \theta) ^ {n - k} \theta^ {k} \right.} _ {\text {Prob. of having k low - cost opponents}} \\ \cdot \underbrace {(k (1 - \gamma_ {\theta ,   n}) \gamma_ {\theta ,   n} ^ {k - 1})} _ {\text {Only one of them does not fake}}. \end{array}
$$

Second-period profits: Case 2 in Table 3 when some supplier j 6= i is the only supplier bidding p < c

(10)

Using the above two expressions, we compute the first-period equilibrium (see Appendix D.2). The semipooling equilibrium includes a bid distribution $F _ { 1 , \mathrm { c r s } } ^ { \mathrm { s e m i } } \hat { ( } p )$ according to which a supplier bids a price $p < c _ { h }$ and the probability $\gamma _ { \theta , n }$ with which he fakes. The two terms are solutions to the following two equations:

$$
\begin{array}{r l} & {(1 - \theta + \theta \gamma_ {\theta , n}) ^ {n} (c _ {h} - c _ {l})} \\ & {\quad = (1 - \theta + \theta (1 - F _ {1, \mathrm{cis}} ^ {\mathrm{semi}} (p))) ^ {n} (p - c _ {l}),} \end{array}\tag{11}
$$

$$
(1 - \theta + \theta \gamma_ {\theta , n}) ^ {n + 1} = (n + 1) (1 - \gamma_ {\theta , n}) (1 - \theta) ^ {n} \theta .\tag{12}
$$

Based on the equilibrium analysis, the total expected profit for a low-cost supplier under <sup>cis</sup> when only a semipooling equilibrium exists is

$$
\Pi_ {\mathrm{CIS}} ^ {\mathrm{semi}} = ((1 - \theta + \theta \gamma_ {\theta , n}) ^ {n} + (1 - \theta) ^ {n}) (c _ {h} - c _ {l}).\tag{13}
$$

Note that, from Equation (12), we cannot solve $\gamma _ { \theta , n }$ for an arbitrary n. This is because of the Abel–Ruffini impossibility theorem, which states that no general solution exist in radicals for a polynomial equation of order five or more. The limitation perhaps might be the reason that prior papers have only considered $n = 1$ when a quadratic equation can be solved in radicals. Despite the limitation, we compare the policies using the properties of Equation (12) presented next.

All the suppliers bid $p = c _ { h }$  
![](/api/attachments/G4FMD74V/fulltext/images/3fb67bc7d1d938137dd66934ac908749a926d020bd906be1075b175ad439f158.jpg)

In general, the variation of $\gamma _ { \theta , n }$ with respect to  is similar to the one in Figure 1. The function is zero and increasing at $\theta _ { n } ^ { \mathrm { f a k e } }$ (recall that it is the value of  beyond which the semipooling equilibrium is valid), attains a maxima, and again reaches zero at $\theta = 1$ . Let $\gamma _ { n } ^ { \mathrm { m a x } }$ be the maximum value attained for a given n and $\theta _ { n } ^ { \operatorname* { m a x } \gamma }$ be the  at which the maxima is attained.

<sup>Proposition</sup> <sup>1.</sup> For any arbitrary n, the following properties of Equation (12) are observed:

1. $\gamma _ { \theta , n } > 0 \forall \theta \in ( \theta _ { n } ^ { \mathrm { f a k e } } , 1 )$ . There is only one point of inflection, which occurs at $\theta _ { n } ^ { \operatorname* { m a x } \gamma } = \overset { \smile } { 1 } / 1 + \overset { \cdot } { n } ^ { 1 + n } /$ $( n ^ { n } + ( 1 + n ) ^ { n } )$

$$
\begin{array}{l} 2. \partial \theta_ {n} ^ {\mathrm{fake}} / \partial n <   0. \\ 3. F o r \theta > \theta_ {1} ^ {\max \gamma}, \gamma_ {\theta , 1} \geq \gamma_ {\theta , n} f o r a n y n > 1. \end{array}
$$

(See Appendix D.3 for the proof.) We will use these properties when comparing the policies in the following section.

Compared to the single period, the bid distribution is skewed to the right here again. In fact, the bid distributions under <sup>cis</sup> can be shown to be stochastically dominant over that for the single period game. The skew is because of the deception effect we identified earlier.

## 5. Comparisons

In this section, we compare the policies on the procurer surplus, the expected supplier profits, and the social welfare generated. In doing so, we are implicitly comparing the welfare implication of the two learning effects. As we will show, the procurer surplus and the supplier profit comparisons are quite related. So we first deal with them. Following that, we compare the social welfare generated. Note that—independent of the policies—the metrics are identical across the policies for $\theta = 1 _ { . }$ , so we ignore this uninteresting case in our results.

If $\mathrm { S P } _ { \phi }$ represents the unconditional supplier profits across both periods under policy $\phi ,$ where $\phi \in$ 8<sup>iis</sup>, <sup>cis</sup>9, then

$$
\mathrm{SP} _ {\phi} = \theta \Pi_ {\phi} + (1 - \theta) 0,
$$

where $\Pi _ { \phi }$ is the expected supplier profits conditional on a supplier being a low-cost type and is characterized by Equations (6), (8), and (13) under the respective policies. From the above expression, it is sufficient to compare $\Pi _ { \phi }$ for comparing the expected supplier profits.

Based on the expression for the unconditional profits for each bidder, we compute the total expected payment by the procurer across both periods, $\operatorname { E P } _ { \phi } .$ Under the three cases, they are

$$
\mathrm{EP} _ {\mathrm{IIIS}} = 2 c _ {l} + (n + 1) \theta \Pi_ {\mathrm{IIIS}} + 2 (1 - \theta) ^ {n + 1} (c _ {h} - c _ {l}),
$$

$$
\mathrm{EP} _ {\mathrm{cis}} ^ {\mathrm{sep}} = 2 c _ {l} + (n + 1) \theta \Pi_ {\mathrm{cis}} ^ {\mathrm{sep}} + 2 (1 - \theta) ^ {n + 1} (c _ {h} - c _ {l}),
$$

$$
\mathrm{EP} _ {\mathrm{CIS}} ^ {\mathrm{semi}} = 2 c _ {l} + (n + 1) \theta \Pi_ {\mathrm{CIS}} ^ {\mathrm{semi}} + (2 (1 - \theta) ^ {n + 1} + \Delta) (c _ {h} - c _ {l}),
$$

where $\Delta \ge 0$ is the probability that a high-cost type wins in the first period of <sup>cis</sup> when at least one low supplier is present. From these expressions, we see that comparing the procurer surplus between <sup>cis</sup>-separating equilibrium and <sup>iis</sup> is the opposite of comparing their respective expected supplier profits. It should also be obvious from the expressions that, whenever a <sup>cis</sup>-separating equilibrium generates higher supplier profits than IIS, the expected payment for the buyer is also higher. Therefore, comparing $\Pi _ { \phi }$ is also relevant to the procurer surplus comparisons.

## 5.1. Comparing $\Pi _ { \phi }$

The result from comparing <sup>cis</sup> under the separating equilibrium and <sup>iis</sup> is straightforward.

Theorem 1. $\Pi _ { \mathrm { { I I S } } } > \Pi _ { \mathrm { { C I S } } } ^ { \mathrm { s e p } }$ and $\mathrm { E P } _ { \mathrm { _ { I I S } } } > \mathrm { E P } _ { \mathrm { c I S } } ^ { \mathrm { s e p } }$ for $\theta \in$ $[ 0 , \theta _ { n } ^ { \mathrm { f a k e } } )$

(Proofs for all the results in $\ S 5$ are available in the Online Appendix E.) Recall that the extraction effect exists under <sup>iis</sup>, but no such effect plays a role under <sup>cis</sup> when separating equilibrium is valid. As a result, the bids tend to be higher under <sup>iis</sup>. Thus, the extraction effect is the primary cause for the theorem. Note that the comparison in the above theorem has been executed for any n, but the result under the semipooling equilibrium case is not as straightforward.

Let us introduce a variable $\theta _ { n } ^ { \mathrm { e q u a l } }$ to represent, for a given n, the value of  when $\Pi _ { \mathrm { c I S } } ^ { \mathrm { s e m i } } = \hat { \Pi _ { \mathrm { I I S } } } ^ { } ,$ . (Table 4 shows the different representations of $\theta$ used during the comparisons.) Let us first execute the comparison for the case when $n = 1$

Proposition 2. <sub>For</sub> $n = 1 .$ , there exists a $\theta _ { 1 } ^ { \mathrm { e q u a l } } < 0 . 8 7$ such that $\Pi _ { \mathrm { c I S } } ^ { \mathrm { s e m i } } > \Pi _ { \mathrm { m s } }$ and $\mathrm { E P _ { c r s } ^ { s e m i } } > \mathrm { E P _ { \ m s } } \ f o { \bar { r } } \ \theta > \theta _ { 1 } ^ { \mathrm { e q u a l } }$ and $\Pi _ { \mathrm { c I S } } ^ { \mathrm { s e m i } } < \Pi _ { \mathrm { \scriptscriptstyle I I S } } f o r \theta _ { 1 } ^ { \mathrm { f a k e } } < \theta < \theta _ { 1 } ^ { \mathrm { e q u a l } }$

Table 4 Different Representations of  That We Employ When Comparing the Policies

<table><tr><td>Variation</td><td>Explanation</td></tr><tr><td> $\theta$ </td><td>Probability of a supplier being a low-cost type</td></tr><tr><td> $\theta_{n}^{\text{fake}}$ </td><td>For a given  $n$ , faking occurs in cis for  $\theta > \theta_{n}^{\text{fake}}$ </td></tr><tr><td> $\theta_{n}^{\text{max } \gamma}$ </td><td>For a given  $n$ ,  $\theta$  when the  $\gamma$  attains the maximum</td></tr><tr><td> $\theta_{n}^{\text{equal}}$ </td><td>For a given  $n$ , the  $\theta$  value when profits from cis under the semipooling equilibrium case equals that under IIS</td></tr></table>

Note that the proof analytically establishes that there can be only one value of  when $\Pi _ { \mathrm { c I S } } ^ { \mathrm { s e m i } } = \Pi _ { \mathrm { m s } }$ . Numerical calculations are only needed to establish the directionality of the difference.

Combining the proposition with the last theorem, notice that there are three regions depending on the nature of the equilibrium under <sup>cis</sup> and the policy comparison outcomes: (i) $\theta \in [ 0 , \theta _ { 1 } ^ { \mathrm { f a k e } } )$ , where the separating equilibrium exists and <sup>iis</sup> generates higher supplier profits; (ii) $\theta \in [ \theta _ { 1 } ^ { \mathrm { f a k e } } , \theta _ { 1 } ^ { \mathrm { e q u a l } } )$ , where the semipooling equilibrium exists but <sup>iis</sup> continues to generate higher supplier profits; and (iii) $\theta \in [ \theta _ { 1 } ^ { \mathrm { e q u a l } } , 1 )$ where the semipooling equilibrium exists and <sup>cis</sup> generates higher supplier profits. When $n = 1$ , we can compute $\begin{array} { r } { \theta _ { 1 } ^ { \mathrm { f a k e } } = \frac { 1 } { 3 } } \end{array}$ and $\dot { \theta } _ { 1 } ^ { \mathrm { e q u a l } } \approx 0 . 8 6 8 8$ . As we discuss below, $\theta _ { n } ^ { \mathrm { e q u a l } }$ can even be less than 005.

Unlike in Theorem 1, here, either policy may be dominant. Hence, recommending one policy over the other is not quite correct. Actually, the choice should depend on the value that the probability of observing a low-cost opponent takes. Notice that the outcome of the comparison is driven by the learning effects we demonstrated earlier. The observation can be explained as follows. When the probability of a low-cost type is high, the motive for a player to learn about its opponent is not as strong. However, the incentive to fake is still dominant. In contrast, for lower values of $\theta ,$ the deception effect is not dominant enough to decrease the procurer surplus.

The next question that arises is whether this result is robust for any arbitrary n. Such a question is especially valid because even the nature of the equilibrium (separating or semipooling) changes depending on n. Moreover, even the probability of faking for a given  is not monotonic in n. This leads to additional difficulties in proving the results. The trick to overcoming the difficulty is to focus on the sensitivity of the difference with respect to n by building on the result established in the previous proposition for $n = 1$

Theorem 2. <sub>Suppose</sub> $n > 0 .$ . There always exists a $\theta _ { n } ^ { \mathrm { e q u a l } } < 0 . 8 7$ such that $\Pi _ { _ { \mathrm { I I S } } } < \Pi _ { _ { \mathrm { C I S } } } ^ { \mathrm { s e m i } }$ and $\mathrm { E P } _ { \mathrm { I I S } } < \mathrm { E P } _ { \mathrm { c I S } } ^ { \mathrm { s e m i } }$ for any $\theta \in [ \operatorname* { m a x } \{ \theta _ { 1 } ^ { \operatorname* { m a x } \gamma } , \theta _ { n } ^ { \mathrm { e q u a l } } \} , 1 )$

Thus, the results from the previous proposition qualitatively hold even for any $\stackrel { \bullet } { n } . { } ^ { 1 2 }$

The above analysis does not show how low $\theta _ { n } ^ { \mathrm { e q u a l } }$ can be. It is reasonable to consider that, if the range $( \theta _ { n } ^ { \mathrm { e q u a l } } , 1 ]$ is quite small, nothing much is lost from a procurer standpoint if we always choose <sup>cis</sup>. To assess how small $\dot { \theta } _ { n } ^ { \mathrm { e q u a l } }$ can be, we did some numerical experiments.<sup>13</sup> These experiments demonstrate that $\theta _ { n } ^ { \mathrm { e q u a l } }$ decreases with n. We found that $\theta _ { n } ^ { \mathrm { e q u a l } }$ is even less than 005 when $n > 1 6 ,$ . This means that, even if the probability of a low-cost type is a simple coin toss, the procurer should consider revealing all the bids if the market involves 17 or more suppliers. This is not a large number. In Freemarkets, when a procurer initiates a market session seeking suppliers to die cast, 30 or more participate. This example illustrates the importance of considering either policy. Next, suppose the procurer is unaware of our recommendation and chooses to always adhere to one policy. How serious will the impact be? In some regards, the answer to this question explains the contribution of this paper. Again, through the same numerical experiments, for $n = 1$ , we found that the expected payments for the procurer can be as large as 68% if <sup>cis</sup> is always chosen and 25% if <sup>iis</sup> is always chosen. These numerical analyses show the value of considering the trade-off between the extraction and the deception effects. We are not aware of any prior work that has shown the existence of such a trade-off. These examples also illustrate the problem with concluding that one policy is always better than another.

Next, we investigate how the two effects drive the bidding behaviors of the suppliers. The following theorems provide some insights in that regard:

Theorem 3. <sub>For</sub> $\theta > \theta _ { n } ^ { \mathrm { e q u a l } }$ , the first-period bid distribution under <sup>cis</sup> first order stochastically dominates that under <sup>iis</sup>.

Theorem 4. <sub>For</sub> $\theta < \theta _ { n } ^ { \mathrm { f a k e } } .$ , the first-period bid distributions under <sup>iis</sup> first order stochastically dominate that under <sup>cis</sup>.

Figure 2 provides a visual idea how the bid distributions compare under the case corresponding to Theorem 3. In the figure, under both the policies, as  increases, the bid distributions tend to be lower, consistent with our expectation. If one considers the firstperiod bid distribution under <sup>iis</sup>, notice that the mass of the cdf in the first period tends to be on lower bids when $\theta > \theta _ { n } ^ { \mathrm { e q u a l } }$ . Thus, the first-order stochastic dominance results proved in the theorem can be seen. The stochastic dominance result also affects the secondperiod profit comparisons. For $\theta > \theta _ { n } ^ { \mathrm { e q u a l } }$ <sup>l</sup>, because of the stochastic dominance result, the beliefs held by the winner tend to be lower under <sup>iis</sup>. This also leads to lower second-period profits under <sup>iis</sup> than under <sup>cis</sup>. Therefore, we observe the expected profit comparison in Theorem 2. A similar explanation is valid for $\theta < \theta _ { n } ^ { \mathrm { f a k e } }$

Figure 2 Bid Distribution Under Both <sup>iis</sup> and <sup>cis</sup> for Two Different Values of $\theta = \{ 0 . 9 , 0 . 9 7 9 \} , n = 1 , c _ { h } = 1$ 1 and $c _ { I } = 0$  
![](/api/attachments/G4FMD74V/fulltext/images/e841cf03508972b6fd67668242870ff793549c9286904babbc9f6bea1899dbbc.jpg)

## 5.2. Comparing the Social Welfare

In this subsection, we are interested in comparing the efficiencies of the policies. Let $\mathsf { S W } _ { \phi }$ represent the social welfare generated under a specific policy $\phi \in \{ \mathrm { I I S } , \mathrm { C I S } \}$ . It actually represents the total welfare of the procurers and the sellers. Note that the procurer utilities are identical across the policies, prices are simply transfer of rents, and only the costs of the winning suppliers matter. So the focus of social welfare comparison is the probability of a high-cost supplier winning. Formally:

Theorem $5 . \ S W _ { \scriptscriptstyle \mathrm { I I S } } = S W _ { \scriptscriptstyle \mathrm { C I S } } ^ { \mathrm { s e p } } \ f o r \ \theta \in [ 0 , \theta _ { n } ^ { \mathrm { f a k e } } ] . \ S W _ { \scriptscriptstyle \mathrm { I I S } } >$ $\mathrm { S W } _ { \mathrm { C I S } } ^ { \mathrm { s e m i } } f o r \ \theta \in ( \theta _ { n } ^ { \mathrm { f a k e } } , 1 )$

It is clear that <sup>cis</sup> generates less social welfare than <sup>iis</sup>. This is so because suppliers in <sup>cis</sup> have an incentive to fake. When faking occurs, the probability of a high-cost type winning is nonzero, which in turn leads to a lower social welfare. It is important to distinguish here the impact of the extraction effect as opposed to the faking effect. Note that, although bids are higher under <sup>iis</sup> because of the extraction effect, they are never equal to $c _ { h } .$ This is the reason that <sup>cis</sup> is not socially optimal. These insights may be useful to a policy maker. Note that the government, which is typically considered a social welfare maximizer, often conducts auctions that are similar to <sup>cis</sup>.

One example is municipal auctions, described earlier. Another example is the auctioning of sulfur dioxide emission permits by the U.S. Environmental Protection Agency. Here, the emission rights are packaged into smaller sets and sequentially auctioned using a first-price sealed bid mechanism. At the end of each auction, all of the sealed bids are revealed, consistent with the complete information policy analyzed in our paper (Culligan 2008). Our results demonstrate that such a complete revelation of bids can lead to decreasing social welfare even if the number of competitors increases.

When studying the sensitivity of the social welfare to different parameters, we observed the following counterintuitive result:

Theorem 6. <sub>For</sub> <sub>every</sub> $\theta ~ \in ~ [ 0 , \theta _ { 1 } ^ { \mathrm { f a k e } } ] ,$ , there exist $n _ { 1 }$ and n , such that $n _ { 2 } ,$ $\partial S W _ { \mathrm { c I s } } / \partial n < 0 f o r n _ { 1 } \leq n < n _ { 2 }$

One would expect that as the number of competitors increases, the efficiency also increases. With respect to that, the above theorem may be surprising. The key point to note is that the deception effect under <sup>cis</sup> blunts the ferocity of competition and enables suppliers to submit high bids, resulting in decreased social welfare. From a technical standpoint, the result is a consequence of $\theta _ { n } ^ { \mathrm { f a k e } }$ decreasing with n (also shown as Property 2 in Proposition 1). Fix the number of suppliers to be n. For an arbitrary $\theta ^ { \prime } \in ( \theta _ { n + 1 } ^ { \mathrm { f a k e } } , \theta _ { n } ^ { \mathrm { f a k e } } )$ , the faking probability is zero. For the same $\theta ^ { \prime }$ , increase the number of suppliers to $( n + 1 )$ . Then the suppliers start to fake. Thus, the increased competition can be seen to decrease social welfare.

## 6. Generalization

This section demonstrates that the results we have already established hold in more generic settings. In the first subsection, we consider the scenario where there are three cost types. In the second subsection, we consider a stylized model to study the sensitivity of the faking effect to the direct benefit from faking.

## 6.1. Three-Cost Type

Consider the original model specification in §3 with some modifications. Instead of the two-cost type model, we assume that each supplier can be one of three $\mathrm { t y p e s } { \mathrm { - } } c _ { l } , ~ c _ { m } , ~ \mathrm { o r } ~ c _ { h }$ . We will focus on the special case of $n = 1 ~ { \mathrm { ( i . e . , } }$ a two-bidder game) and normalized costs. Let $c _ { l }$ type incur $c _ { l } = 0$ cost; $c _ { h }$ incur $c _ { h } = 1 ;$ and $c _ { m }$ type incur $c _ { m } = c$ with $0 < c < 1$ . The probability that a supplier’s cost type is $c _ { l }$ is $\{ l \ | \ 0 \leq$ $l \leq 1 \} ; c _ { m }$ is $\{ m \mid 0 < { \bar { m } } \leq 1 \} .$ ; and $c _ { h }$ is $\{ 1 - l - m \mid l +$ $m \leq 1 \}$ . The mathematical details turn out to be such that the results in the original model can be retrieved by setting l = 0. As in the original model, we implicitly assume throughout the discussion that discontinuities exist in the strategy space to avoid the equilibrium nonexistence problem. All of the newly introduced variables are assumed to be common knowledge. In this game, at equilibrium, a supplier of cost type $c _ { h }$ always bids 1. We are focused on the bidding behavior of the other two types. (See Appendix F for additional details.)

6.1.1. Second-Period Game. There are four scenarios in the second-period game that are relevant to our analysis. In all the four scenarios, whenever there is uncertainty about the opponent’s type, let l<sup>0</sup> and m<sup>0</sup> be the beliefs that a supplier has about the opponent being of type $c _ { l }$ and $c _ { m } ,$ respectively.

In Scenario 1, suppliers know each other’s cost type and the scenario resembles a Bertrand game. In Scenario 2, the uncertainty that each supplier has about his opponent is identical. At equilibrium, suppliers of type $c _ { l }$ and $c _ { m } ,$ respectively, generate profits of

$$
\begin{array}{c} \Pi_ {c _ {l}} ^ {\mathrm{Sc}: 2} = c (1 - l ^ {\prime}) + (1 - l ^ {\prime} - m ^ {\prime}) (1 - c) \quad \text { and } \\ \Pi_ {c _ {m}} ^ {\mathrm{Sc}: 2} = (1 - l ^ {\prime} - m ^ {\prime}) (1 - c). \end{array}
$$

The subscripts indicate the cost type, and the superscript shows the scenario. In Scenario 3, only one supplier has his type revealed to the other; let the revealed type be $c _ { m }$ . At equilibrium, the profits for the different players are

$$
\begin{array}{c} \Pi_ {c _ {m}} ^ {\mathrm{Sc:3;} R} = (1 - l ^ {\prime} - m ^ {\prime}) (1 - c), \\ \Pi_ {c _ {m}} ^ {\mathrm{Sc:3;} H} = \frac {(1 - l ^ {\prime} - m ^ {\prime})}{1 - l ^ {\prime}} (1 - c), \quad \text { and } \\ \Pi_ {c _ {l}} ^ {\mathrm{Sc:3;} H} = c + \frac {(1 - l ^ {\prime} - m ^ {\prime})}{1 - l ^ {\prime}} (1 - c). \end{array}
$$

The additional term R or H in the superscript indicates whether the supplier’s type is revealed. In Scenario 4, only one supplier has his type revealed; let the type revealed be $c _ { l }$ . Two different equilibria are feasible depending on whether $( 1 - l ^ { \prime } - m ^ { \prime } ) > ( 1 - l ^ { \prime } ) c .$ If the condition is valid, the equilibrium profits are as follows:

$$
\begin{array}{c} \Pi_ {c _ {l}} ^ {\mathrm{Sc:4-(1);R}} = (1 - l ^ {\prime} - m ^ {\prime}), \\ \Pi_ {c _ {m}} ^ {\mathrm{Sc:4-(1);H}} = \frac {(1 - l ^ {\prime} - m ^ {\prime})}{1 - l ^ {\prime}} - c, \quad \text { and } \\ \Pi_ {c _ {l}} ^ {\mathrm{Sc:4-(1);H}} = \frac {(1 - l ^ {\prime} - m ^ {\prime})}{1 - l ^ {\prime}}. \end{array}
$$

Otherwise, the following are the equilibrium profits: $\Pi _ { c _ { l } } ^ { \mathrm { S c } : 4 - ( 2 ) ; R } = \Pi _ { c _ { l } } ^ { \mathrm { S c } : 4 - ( 2 ) ; H } = ( 1 - l ^ { \prime } ) c ,$ , and $\begin{array} { r } { \Pi _ { c _ { m } } ^ { \mathrm { S c : 4 - } ( 1 ) ; H } = \stackrel { \bullet } { 0 } } \end{array}$

6.1.2. First-Period Game: <sup>iis</sup>. It turns out that only a separating equilibrium exists in the first period here. The profit expressions for the equilibrium computations are

$$
\begin{array}{l} \pi_ {\text { IIS }, c _ {m}} (p) = \overbrace {(1 - l - m) (p - c + \Pi_ {c _ {m}} ^ {\text { Sc:3; } R})} ^ {\text { Opponent   is   type   } c _ {h}} \\ \qquad + \overbrace {m (1 - F _ {m} (p)) (p - c + \Pi_ {c _ {m}} ^ {\text { Sc:3; } R})} ^ {\text { Opponent   is   type   } c _ {m} \text {   but   he   lost   first   period }} \\ \qquad + \underbrace {m F _ {m} (p) (0 + \Pi_ {c _ {m}} ^ {\text { Sc:3; } H})} _ {\text { Opponent   is   type   } c _ {m} \text {   but   he   won   first   period }} + \underbrace {l \Pi_ {c _ {m}} ^ {\text { Sc:4; } H}} _ {\text { Opponent   is   type   } c _ {l}} \end{array}
$$

$$
\begin{array}{c} \pi_ {\text {IIS}, c _ {l}} (p) = \Big (\overbrace {(1 - l) (p + \Pi_ {c _ {l}} ^ {\text {Sc:4;R}})} ^ {\text {Opponent is not type c_{l}}} \\ + \overbrace {l (1 - F _ {l} (p)) (p + \Pi_ {c _ {l}} ^ {\text {Sc:4;R}})} ^ {\text {Opponent is type c_{l}}   \text {but he lost first period}} \\ + \overbrace {l F _ {l} (p) (0 + \Pi_ {c _ {l}} ^ {\text {Sc:4;H}})} ^ {\text {Opponent is type c_{l}}   \text {but he won}} \Big). \end{array}
$$

Assuming a Bayesian update for the beliefs, the equilibrium for $F _ { m } ( p )$ can be computed. The infimum of the strategy set is

$$
p _ {l, m} ^ {\mathrm{IIS}} = c + (1 - c) \frac {(1 - l - m)}{1 - l} \left(1 - \log \left(\frac {1 - l - m}{1 - l}\right)\right).
$$

The total profit for type $c _ { m }$ is

$$
(1 - l - m) (1 - c) \left(2 - \log \left(\frac {1 - l - m}{1 - l}\right)\right) + x \Pi_ {c _ {m}} ^ {\mathrm{Sc}: 4; H}.
$$

We discuss the expansion on $\Pi _ { c } ^ { \mathsf { S c } : 4 ; H }$ next.

In Scenario $4 , m ^ { \prime } = m$ and $l ^ { \prime } { \overset { \cdot \cdot } { = } } l ( 1 - F _ { l } ( q ) ) / 1 - l F _ { l } ( q )$ Let $p _ { l , l } ^ { \mathrm { m s } }$ be such that $F _ { l } ( p _ { l , l } ^ { \mathrm { \tiny { I I S } } } ) = 0$ . Computing the profit expressions for that scenario has to consider different conditions.

1. If $( 1 - l - m ) > ( 1 - l ) c , \mathrm { t h e n } ( 1 - l ^ { \prime } - m ^ { \prime } ) > ( 1 - l ^ { \prime } ) c .$ So

$$
\Pi_ {c _ {l}} ^ {\mathrm{Sc:4;R}} = \frac {1 - l}{1 - l F _ {l} (p)} - m,
$$

$$
\Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; H} = \frac {1}{F _ {l} (p)} \int_ {p _ {l, l} ^ {\mathrm{ns}}} ^ {p} \left(\frac {1 - l - m (1 - l F _ {l} (q))}{1 - l}\right) f _ {l} (q)   d q,
$$

and

$$
\Pi_ {c _ {m}} ^ {\mathrm{Sc:4}; H} = \frac {1}{F _ {l} (p)} \int_ {p _ {l, l} ^ {\mathrm{is}}} ^ {p} \biggl (\frac {1 - l - m (1 - l F _ {l} (q))}{1 - l} - c \biggr) f _ {l} (q)   d q.
$$

2. If $( 1 - c ) < m ,$ , then 41 − l<sup>0</sup> − m<sup>0</sup>5 < 41 − l<sup>0</sup>5c. So

$$
\Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; R} = \frac {(1 - l) c}{1 - l F _ {l} (p)}, \quad \Pi_ {c _ {m}} ^ {\mathrm{Sc:4}; H} = 0 \quad \text { and }
$$

$$
\Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; H} = \frac {c}{F _ {l} (p)} \int_ {p _ {l, l} ^ {\mathrm{ns}}} ^ {p} \biggl (\frac {1 - l}{(1 - l F _ {l} (q))} \biggr) f _ {l} (q) d q.
$$

3. Otherwise, two subcases arise. Let $p _ { e }$ be such that

$$
F _ {l} (p _ {e}) = \frac {1}{l} \left(1 - \frac {(1 - l) (1 - c)}{m}\right).
$$

• If

$$
p \leq p _ {e}, \quad \Pi_ {c _ {m}} ^ {\mathrm{Sc:4}; H} = 0, \quad \Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; R} = \frac {(1 - l) c}{1 - l F _ {l} (p)}, \quad \text { and }
$$

$$
\Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; H} = \frac {c}{F _ {l} (p)} \int_ {p _ {l, l} ^ {\mathrm{ns}}} ^ {p} \biggl (\frac {1 - l}{(1 - l F _ {l} (q))} \biggr) f _ {l} (q) d q.
$$

• For

$$
\begin{array}{r} p > p _ {e}, \quad \Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; R} = \frac {1 - l}{1 - l F _ {l} (p)} - m, \\ \Pi_ {c _ {m}} ^ {\mathrm{Sc:4}; H} = \frac {1}{F _ {l} (p)} \int_ {p _ {e}} ^ {p} \biggl (\frac {1 - l - m (1 - l F _ {l} (q))}{1 - l} - c \biggr) f _ {l} (q) d q, \end{array}
$$

and

$$
\begin{array}{r l} & {\Pi_ {c _ {l}} ^ {\mathrm{Sc:4}; H} = \frac {c}{F _ {l} (p)} \int_ {p _ {l, l} ^ {\mathrm{us}}} ^ {p _ {e}} \biggl (\frac {1 - l}{(1 - l F _ {l} (q))} \biggr) f _ {l} (q) d q} \\ & {\qquad + \frac {1}{F _ {l} (p)} \int_ {p _ {e}} ^ {p} \biggl (\frac {1 - l - m (1 - l F _ {l} (q))}{1 - l} \biggr) f _ {l} (q) d q.} \end{array}
$$

To compute the bid distribution in each case, we invoke the property that the strategies in the mixed equilibrium yield the same profit and that $p _ { l , m } ^ { \mathrm { m s } }$ is the supremum of the strategy space for type $c _ { l } .$ The explicit expressions for the different cases have not been shown, for the sake of simplicity. We use the expression to compare against the bid distribution of a single-period game. The single-period game has the same bid distribution as Scenario 2 except for ${ l } ^ { \prime } = l$ and $m ^ { \prime } = m$ . One can show the stochastic dominance of <sup>iis</sup> bid distribution in each case, validating the existence of the extraction effect. One can also prove deviations are not more profitable.

6.1.3. First-Period Game: <sup>cis</sup> Separating Equilibrium. Recall that all bids are revealed under <sup>cis</sup>. If the separating equilibrium is valid in the first period, then the second period is a Bertrand game. The expected payoff for both cost types are

$$
\begin{array}{c} \pi_ {\mathrm{CIS}, c _ {m}} ^ {\mathrm{sep}} (p) = (1 - l - m) (p - c + 1 - c) + m (1 - F _ {m} (p)) (p - c), \\ \pi_ {\mathrm{CIS}, c _ {l}} ^ {\mathrm{sep}} (p) = (1 - l - m) (p + 1) + m (p + c) + l (1 - F _ {l} (p)) p \end{array}
$$

The equilibrium bid distributions in this case are similar to Scenario 2 except for $l ^ { \prime } = l$ and $m ^ { \prime } = m$ . The expected profits are $\pi _ { \mathrm { c I s } , c _ { l } } ^ { \dot { \mathrm { s e p } } } = 2 ( 1 - l - m + m c )$ and $\pi _ { \mathrm { c r s } , c _ { m } } ^ { \mathrm { s e p } } = 2 \dot { ( } 1 - l - m ) ( 1 - c )$

Next, we show why the separating equilibrium does not always exist. Fixing the opponent’s action, a bidder of $c _ { m }$ type generates a profit of $( 1 - l - m )$ $( ( 1 - c ) / 2 + ( 1 - \bar { c } ) \bar { ) } + \bar { m } ( 1 - c ) + l ( 1 - \bar { c } ) .$ , which is greater than $2 ( 1 - l - m ) ( 1 - c ) { \mathrm { ~ i f ~ } } 3 l + 3 m > 1$ . Similarly, fixing the opponent’s action, $c _ { l }$ type fakes as $c _ { h }$ if $3 l + ( 3 +$ $4 c ) m > 1$ . Both these conditions are feasible in the valid range of l and $m ,$ proving the existence of the faking effect. The exact conditions when a separating equilibrium exists have to be considered when one or both opponent types fake, and one can obtain that from the analysis of the semipooling equilibrium case. One can easily rule out a pooling equilibrium.

6.1.4. First-Period Game: <sup>cis</sup> Semipooling Equilibrium. Suppose $\gamma _ { l }$ and $\gamma _ { m }$ are the respective probabilities that each of type $c _ { l }$ and $c _ { m }$ bid like a $c _ { h }$ type. Let $F _ { c _ { l } } ^ { \mathrm { s e m i } } ( p )$ and $F _ { c _ { m } } ^ { \mathrm { s e m i } } ( \bar { p } )$ be the cdfs of the bid distributions for $c _ { l }$ and $c _ { m }$ types, respectively. It can be shown that the lower support for type $c _ { l }$ is lower than that for type $c _ { m } .$ . Assume for now that $p _ { m } ^ { \mathrm { c r s } }$ is the lower end of the bid distribution for type $c _ { m } .$ In this case, the expected profits for the different types and different bids are

$$
\Pi_ {c _ {m}} ^ {\mathrm{semi}} (p \mid p <   1) = (1 - l - m + l \gamma_ {l} + m \gamma_ {m}) \big (p - c + \Pi_ {c _ {m}} ^ {\mathrm{Sc:3;R}} \big)\tag{14}
$$

$$
\begin{array}{r l} & {\Pi_ {c _ {m}} ^ {\mathrm{semi}} (p = 1)} \\ & {\qquad = \big (1 - l - m + l \gamma_ {l} + m \gamma_ {m} \big) \bigg (\frac {1 - c}{2} + \Pi_ {c _ {m}} ^ {\mathrm{Sc:2}} \bigg)} \\ & {\qquad + m (1 - \gamma_ {m}) \Pi_ {c _ {m}} ^ {\mathrm{Sc:3;H}} + l (1 - \gamma_ {l}) \Pi_ {c _ {m}} ^ {\mathrm{Sc:4;H}}} \end{array}\tag{15}
$$

$$
\begin{array}{c} \Pi_ {c _ {l}} ^ {\text {semi}} (p \mid p <   p _ {m} ^ {\text {cis}}) = (1 - l - m + l \gamma_ {l} + m \gamma_ {m}) \big (p + \Pi_ {c _ {l}} ^ {\text {Sc:4; R}} \big) \\ + m (1 - F _ {c _ {m}} ^ {\text {semi}} (p) - \gamma_ {m}) (p + c) \end{array}
$$

$$
\Pi_ {c _ {l}} ^ {\text {semi}} (p = 1) + l (1 - F _ {c _ {l}} ^ {\text {semi}} (p) - \gamma_ {l}) p\tag{16}
$$

$$
\begin{array}{l} \Pi_ {c _ {l}} ^ {\mathrm{semin}} (p = 1) \\ \qquad = (1 - l - m + l \gamma_ {l} + m \gamma_ {m}) \bigg (\frac {1}{2} + \Pi_ {c _ {l}} ^ {\mathrm{Sc:2}} \bigg) \\ \qquad + m (1 - \gamma_ {m}) \Pi_ {c _ {l}} ^ {\mathrm{Sc:3;H}} + l (1 - \gamma_ {l}) \Pi_ {c _ {l}} ^ {\mathrm{Sc:4;H}}. \end{array}\tag{17}
$$

Equations (15) and (17) are the profit expressions when faking. We note that $F _ { c _ { I } } ^ { \mathrm { s e m i } } ( \approx 1 ) \ = 1 \ - \ \gamma _ { l } ,$ $F _ { c _ { m } } ^ { \mathrm { s e m i } } ( \approx 1 ) = 1 - \gamma _ { m } , F _ { c _ { l } } ^ { \mathrm { s e m i } } ( p _ { m } ^ { \mathrm { c u s } } ) = 1 - \gamma _ { l } ,$ , and $F _ { c _ { m } } ^ { \mathrm { s e m i } } ( p _ { m } ^ { \mathrm { c I s } } ) =$ 0; and that the expected profits are the same across all prices in the strategy space, to compute the expected profits. In this case, the beliefs l<sup>0</sup> and m<sup>0</sup> are the beliefs held by the opponent of a non-revealing bidder (the opponent can be non-revealing also). Unlike in the previous policy, the second period beliefs are the same independent of the cost type holding it and it is so because all bids are revealed. Using Bayesian update,

$$
\begin{array}{c} (1 - l ^ {\prime} - m ^ {\prime}) = \frac {(1 - l - m)}{1 - l (1 - \gamma_ {l}) - m (1 - \gamma_ {m})} \text { and } \\ (1 - l ^ {\prime}) = \frac {1 - l - m (1 - \gamma_ {m})}{1 - l (1 - \gamma_ {l}) - m (1 - \gamma_ {m})}. \end{array}
$$

Table 5 Numerical Comparison

<table><tr><td>c</td><td>l</td><td>m</td><td> $\gamma_l$ </td><td> $\gamma_m$ </td><td> $\Pi^{CIS}$ </td><td> $\Pi^{IIS}$ </td></tr><tr><td rowspan="6">0.5</td><td rowspan="3">0</td><td>0.10</td><td>0</td><td>0</td><td>0.090</td><td>0.095</td></tr><tr><td>0.50</td><td>0</td><td>0.236</td><td>0.280</td><td>0.337</td></tr><tr><td>0.90</td><td>0</td><td>0.287</td><td>0.206</td><td>0.193</td></tr><tr><td rowspan="2">0.20</td><td>0.20</td><td>0</td><td>0.211</td><td>0.404</td><td>0.455</td></tr><tr><td>0.75</td><td>0</td><td>0.250</td><td>0.291</td><td>0.216</td></tr><tr><td>0.75</td><td>0.20</td><td>0.431</td><td>0.156</td><td>0.516</td><td>0.489</td></tr><tr><td>0.75</td><td>0.55</td><td>0.25</td><td>0.04</td><td>0.263</td><td>0.451</td><td>0.528</td></tr></table>

One has to solve the four equations subject to the constraints that $1 \ge \gamma _ { l } \ge 0$ and $1 \geq \gamma _ { m } \geq 0$ and the updated beliefs should be considered for the appropriate Scenario 4. If a solution does not exist, then the equilibrium is a separating one.

6.1.5. Numerical Comparison. In this subsection, we show using numerical simulations that one effect dominates the other. Under each policy, we have already characterized the payoff for the bidder conditional on his type. We use that to compare the unconditional payoff for each bidder under either policy. We use $\Pi ^ { \mathrm { c r s } }$ to represent the unconditional bidder profit under <sup>cis</sup> and $\Pi ^ { \mathrm { I I I S } }$ as that under <sup>iis</sup>. We continue to impose the restriction that $l + m < 1$ . Table 5 shows the results from the numerical comparisons. The first three rows show the comparisons that are similar to the original model. Rows four and five show that either effect may dominate for nonzero l. The last two rows show examples of $\gamma _ { l }$ being nonzero and how one effect may dominate the other.

## 6.2. Robustness of the Faking Effect

In the original model, the maximum feasible number of low-cost types is the same as the number of suppliers in the market. When the total number of suppliers in the market increases, faking may become less attractive and the original results may not be sustained. The question we address in this section is; How strong are the results if the direct benefit from faking decreases? Using a stylized model, we show below that our original results qualitatively continue to hold.

Suppose there are $n _ { l }$ low-cost suppliers in the world and all others are high-cost types. Let  be the probability with which a low-cost type participates in the auction. Assume that there are M participating suppliers and the value of M is common knowledge. Everything else from the original model is assumed to hold, including the same bidder characteristics across both periods.

If $\begin{array} { r } { \bar { M } \leq n _ { l } , } \end{array}$ the original equilibrium results are applicable except that n in all the equations will be replaced with M. The reason the results are similar is that the question considered by each of the suppliers is also similar: Which of the M (instead of n in the earlier formulation) suppliers are low-cost types? Under this case, therefore, the extraction and the deception effects become relevant. Note that the deception effect occurs only when $\theta \geq 1 / ( 2 + M )$

When $M > n _ { l } ,$ the equilibrium results are slightly different: (i) n in all the other equilibrium equations except Equations (10) and (12) are replaced with $n _ { l } .$ (ii) Equations (10) and (12) are respectively changed to the following:

$$
\begin{array}{l} \Pi_ {\mathrm{CIS}} ^ {\text {semi}} (c _ {h}) = \left[ 1 - \theta + \theta \gamma_ {\theta , n _ {l}} \right] ^ {n _ {l}} \overbrace {\frac {(c _ {h} - c _ {l})}{M + 1}} ^ {\text {Note the change}} \\ \quad + [ 1 - \theta + \theta \gamma_ {\theta , n _ {l}} ] ^ {n _ {l}} y ^ {n _ {l}} (c _ {h} - c _ {l}) \\ \quad + \sum_ {k = 1} ^ {n _ {l}} \binom {n _ {l}} {k} (1 - \theta) ^ {n _ {l} - k} \theta^ {k} \\ \cdot [ k (1 - \gamma_ {\theta , n _ {l}}) \gamma_ {\theta , n _ {l}} ^ {k - 1} ] y ^ {n _ {l}} (c _ {h} - c _ {l}) \\ (1 - \theta + \theta \gamma_ {\theta , n _ {l}}) ^ {n _ {l} + 1} = n _ {l} (1 - \gamma_ {\theta , n _ {l}}) (1 - \theta) ^ {n _ {l}} \theta \underbrace {\frac {(M + 1)}{M}} _ {\text {Note the change}}. \end{array} \tag {18}\tag{18}
$$

The question considered is the same as the one in the original model: Which of the $n _ { l }$ suppliers are low-cost types? However, the difference is that the suppliers have to consider M other suppliers when faking. From these equilibrium expressions, it is obvious that the deception and the extraction effects become relevant even in this case. From Equation (18), we can identify that the deception effect occurs for $\theta >$ $M / n _ { l } ( M + \bar { 1 } ) + M _ { ☉ }$ , which we refer to as $\theta _ { n , M } ^ { \mathrm { f a k e } }$ . We also introduce another notation $\theta _ { n , M } ^ { \mathrm { e q u a l } }$ to refer to the  when the supplier profits under <sup>cis</sup> and <sup>iis</sup> are equal.

Based on the equilibrium analysis, we find the following sensitivity results. First, as M increases, the incentive to fake decreases. Second, as M increases, $\theta _ { n _ { l } , M } ^ { \mathrm { f a k e } }$ decreases. In fact, lim $_ { M  \infty } M / ( n _ { l } ( M + 1 ) + M ) =$ $1 / ( n _ { l } + 1 )$ 0 This shows that even if the direct benefit from faking is zero, faking occurs for $\theta > 1 / ( n _ { l } + 1 )$ . Even more surprising is the result that $\theta _ { n , \infty } ^ { \mathrm { e q u a l } } \approx 0 . 9 5$ It means that for  larger than that the supplier profits under <sup>cis</sup> are higher than under <sup>iis</sup>. Qualitatively, the results we had established in the base model hold even under this special case. Combining the results from these two cases, we can establish that, independent of M, the expected bidder profits are higher under <sup>iis</sup> for $\theta < 1 / ( n _ { l } + 2 )$ and, for $\theta > 0 . 9 5$ , they are higher under <sup>cis</sup>.

## 7. Discussion

We first discuss the implication of replacing the firstprice auction in our model setup with a second-price auction. With the second-price auction, the equilibrium strategies are as follows. Each supplier has an incentive to truthfully bid his valuation independent of the policy, and it is procurer surplus maximizing in our context. However, in general, the second-price auction is not always procurer surplus maximizing (Maskin and Riley 2000a). Even if one considers the first-price auction in those scenarios where the second price sealed bid is not optimal, the learning/signaling effects that we identify in this paper become relevant. So our analysis becomes relevant even in such a scenario. Furthermore, the approach of employing a model with a first-price sealed bid so that the analysis can expose the key insights useful to a procurement manager is consistent with other prior works, $\mathrm { e . g . , }$ Arora et al. (2007), Bajari (2001), and Brosig and Reiss (2007). In each of the examples, the second-price auction is the procurer surplus maximizing mechanism.

Our consideration of the first-price auction is also a matter of relevance. The examples mentioned earlier—the municipal construction auctions as well as the government procurement auctions—are often conducted as first-price sealed bid auctions. Even in the electronic marketplaces we interacted with, the second-price auction or its equivalent, the open-cry auction, is not commonly adopted. In fact, the secondprice auction is not available as an information policy to the procurers. We learned from Freemarkets that the open-cry policy is often not adopted in practice either. Similarly, during a discussion with AT Kearney, we learned that the software provided by AT Kearney’s procurement group (which competes with Freemarkets) does not even enable an open-cry auction. It may be that the procurers do not find the second-price auction surplus maximizing, a result that, as we mentioned earlier, has already been shown theoretically. For these reasons, the model we studied is also reasonable.

The main driver behind our results is how the beliefs held by the suppliers (about the presence of each of the others) evolve across the periods. Under <sup>iis</sup>, the belief terms change because of the extraction effect, whereas, under <sup>cis</sup>, it is because of the faking effect. In <sup>iis</sup>, a supplier alters his bid to affect his own belief and improve his information endowment about the presence of any other low-cost opponent. In contrast, the key reason for a supplier to fake in <sup>cis</sup> is to influence his opponent’s belief and, specifically, to inhibit the competitor’s information endowment about himself. It should be clear that these two effects have different objectives.

The belief updates occur in our setup only because the supplier cost types are identical in both periods. If the cost types were randomly drawn in each period, there would be no benefit from making the belief changes. Then, independent of the information policy, the equilibrium strategies under the two-period game would coincide with those under two singleperiod games. Thus, the procurer surplus generated under the policies policies would be identical, making the policy comparisons uninteresting. In reality, from a supplier’s perspective, the cost types drawn for every opponent are not independent across the periods. Often, they are consistent across periods. As mentioned earlier, anecdotal evidence from Freemarkets supports this claim (see also Arora et al. 2007). So long as the draws are not completely independent, suppliers have an incentive to alter the beliefs; but the degree to which they are altered depends on the consistency of draws across periods and, of course, the information policy. The suppliers under <sup>iis</sup> continue to have an incentive to bid in a manner that creates an information advantage over the winner. Similarly, the suppliers in <sup>cis</sup> also continue to have an incentive to fake. So qualitatively the results should hold.

## 8. Conclusion

In conclusion, we study an important problem that was motivated by a real-world marketplace. Procurers in third-party marketplaces have to choose an information policy for the market sessions they initiate. Suppliers who face uncertainty regarding their opponents’ costs respond by altering their bidding behaviors according to the policy. Thus, the choice of the policy affects the procurer surplus. Given this, our paper focuses on providing managerial insights to procurers in choosing an appropriate policy. Specifically, our objective is to offer insights regarding the key effects affecting revelation policies a procurer needs to consider when choosing the policy.

We accomplish our objective by analytically comparing the policies referred to as <sup>cis</sup> and <sup>iis</sup>. Our analysis reveals two important effects, the extraction and the deception effects, that a procurer has to consider. The extraction effect impacts the bidding behavior under <sup>iis</sup>, and the deception effect under <sup>cis</sup>. When we compare the policies and the effects, we use the following metrics: the expected supplier profits, the expected procurer surplus, and the social welfare generated. Loosely speaking, in our setup, the procurer surplus comparisons turn out to be the opposite of the supplier profit comparisons. From a procurer standpoint, we show that either effect may dominate the other, depending on the probability of observing a low-cost opponent. Specifically, we find that the procurer surplus is higher under <sup>iis</sup> when the probability of observing a low-cost opponent is high, and vice versa. We also demonstrate through analytical models and numerical experiments the importance of understanding the trade-offs between the two effects and when they occur.

From a social welfare standpoint, we find that <sup>iis</sup> is better than <sup>cis</sup>. This observation is also a consequence of the faking effect. When low-cost suppliers fake, the probability of a high-cost type winning the contract is nonzero. However, under <sup>iis</sup>, the probability of a high-cost type winning is zero when at least one lowcost type is present. We also analyzed the sensitivity of the social welfare results. We find it surprising that the social welfare under <sup>cis</sup> may decrease as the number of opponents increases.

Let us briefly contrast our results with those in related prior papers. When the uncertainty about the number of competitors is considered, Arora et al. (2007) demonstrate that the <sup>iis</sup> always generates higher supplier profits than <sup>cis</sup>. As we show in this paper, that result does not hold when the uncertainty about the opponents’ cost is considered. Compared to Tu (2005), a work that was simultaneously pursued, our paper highlights how his assumption disallowing pooling equilibrium affects the policy comparison. We also show that, counter to the simple extension of the revelation principle, <sup>iis</sup> can generate higher procurer surplus.

In our opinion, in addition to the insights, the methodologies adopted in this paper are also interesting. We determine the perfect Bayesian Nash equilibrium of two policies. In general, both <sup>cis</sup> and <sup>iis</sup> did not have closed-form expressions for the bid distribution. Even the expected supplier profits under <sup>cis</sup> could not be expressed in a closed form for any arbitrary number of players. In this paper, we overcome the issues related to the lack of closed-form expression and still execute the comparisons. Note that prior works, which have dealt with similar issues, have avoided this problem by only considering a twoplayer game.

The insights offered in the paper also appear to shed some light on the implications of policies other than those analyzed here. Recall that, under <sup>iis</sup>, suppliers attempt to learn about the nature of the competition, i.e., the presence of the other low-cost competitors, by bidding high prices (the extraction effect). When this result was presented to Freemarkets, they mentioned that they had observed a similar phenomenon when only the bidder rank was provided as feedback. Apparently, in those cases, bidders submitted higher bids initially to learn about the total of competitors, another aspect related to the nature of competition. Perhaps the extraction effect may also explain the lower procurer surplus observed by Koppius (2002) when rank was provided as feedback. It would be interesting to validate if the extraction effect is relevant to other policies as well.

Regarding future research, our paper can be extended in many ways. We have already highlighted some of the questions. Apart from those, one can also consider extending the model to incorporate procurers’ ability to learn across auctions. It would also be interesting to analyze other policies adopted in the marketplaces. Another interesting way to extend our paper would be to relax the common prior assumption on . Such an analysis will shed light on how the policy comparison results alter with different priors.

## Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http://isr.journal .informs.org/.

## Acknowledgments

The author thanks Ashish Arora, Paul Heidhues, Vijay Krishna, Ramayya Krishnan, and the audiences at the University of Rochester and the University of Texas at Dallas for comments on the paper. The author specifically thanks Krishnan Anand for his detailed feedback. The author benefited a lot from discussions with Mohit Tawarmalani. The paper has motivated from conversations with Tony Bernhard, who was the director at Freemarkets Inc., and the author wishes to thank him as well. The author also thanks the GSCMi at Purdue University for the support it offered in writing this paper. The author thanks Ralph Siebert, who has helped tremendously with discussions and in naming the effects identified in the paper.

## References

Adomavicius, G., A. Gupta, P. Sanyal. 2008. Design and evaluation of feedback schemes for multi-attribute procurement auctions. Proc. 29th Internat. Conf. Inform. Systems, Paris. http://aisel .aisnet.org/icis2008/32.

Adomavicius, G., A. Gupta, D. Zhdanov. 2009. Designing intelligent software agents for auctions with limited information feedback. Inform. Systems Res. 20(4) 484–506.

Arora, A., A. Greenwald, K. N. Kannan, R. Krishnan. 2007. Effects of information-revelation policies under market-structure uncertainty. Management Sci. 53(8) 1234–1248.

Aumann, R. 1987. Correlated equilibrium as an expression of Bayesian rationality. Econometrica 55(1) 1–18.

Bajari, P. 2001. Comparing competition and collusion in procurement auctions: A numerical approach. Econom. Theory 18 187–205.

Brosig, J., J. P. Reiss. 2007. Entry decisions and bidding behavior in sequentialfirst-price procurement auctions: An experimental study. Games Econom. Behav. 58(1) 50–74.

Carr, S. 2003. Note on online auctions with costly bid evaluations. Management Sci. 49(11) 1521–1528.

Culligan, K. 2008. SO2 allowance in the US. Proc. 2nd Global Carbon Market Forum: Auctioning Carbon Allowances—Towards Robust Auction Design and Implementation, Washington, DC.

Daughety, A., J. Reinganum. 1994. Asymmetric information acquisition and behavior in role choice models: An endogenously generated signaling game. Internat. Econom. Rev. 35(4) 795–819.

Elmaghraby, W., P. Keskinocak. 2000. Technology for transportation bidding at the Home Depot. http://www2.isye.gatech.edu/ people/faculty/Pinar\_Keskinocak/home-depot-case.zip.

Fudenberg, D., J. Tirole. 1994. Game Theory. MIT Press, Cambridge, MA.

Goes, P., G. Karuga, A. Tripathi. 2009. Understanding willingnessto-pay formation of repeat bidders in sequential online auctions. Inform. Systems Res., epub ahead of print May 12, 2009, http://isr.journal.informs.org/.

Granados, N., A. Gupta, R. J. Kauffman. 2005. Transparency strategy in Internet-based selling. K. Tomak, ed. Advances in the Economics of Information Systems. Idea Group Publishing, Harrisburg, PA, 80–112.

Greenwald, A., K. Kannan, R. Krishnan. 2010. On evaluating information revelation policies in procurement auctions: A Markov decision process approach. Inform. Systems Res. 21(1) 15–36.

Harsanyi, J. 1967. Games with incomplete information played by “Bayesian” players, Part I. The basic model. Management Sci. 14(3) 159–182.

Harsanyi, J. 1968a. Games with incomplete information played by “Bayesian” players, Part II. Bayesian equilibrium points. Management Sci. 14(5) 320–334.

Harsanyi, J. 1968b. Games with incomplete information played by “Bayesian” players, Part III. The basic probability distribution of the game. Management Sci. 14(7) 486–502.

Hausch, D. 1986. Multi-object auctions: Sequential vs. simultaneous sales. Management Sci. 32(12) 1599–1610.

Hausch, D. 1988. A model of sequential auctions. Econom. Lett. 26(3) 227–233.

Jap, S. D. 2002. Online reverse auctions: Issues, themes, and prospects for the future. J. Acad. Marketing Sci. 30(4) 506–525.

Jap, S. D. 2003. An exploratory study of the introduction of online reverse auctions. J. Marketing 67(July) 96–107.

Klemperer, P. 2004. Auctions: Theory and Practice. Princeton University Press, Princeton, NJ.

Koppius, O. R. 2002. Information architecture and electronic market performance. Unpublished doctoral thesis, Erasmus University, Rotterdam, The Netherland.

Krishna, V. 2009. Auction Theory. Academic Press, San Diego.

Kostamis, D., D. Beil, I. Duenyas. 2009. Total-cost procurement auctions: Should the buyer reveal suppliers’ quality? Management Sci. 55(12) 1985–1999.

Kumar, S., M. Dawande, V. S. Mookerjee. 2007. Optimal scheduling and placement of Internet banner advertisements. IEEE Trans. Knowledge Data Engrg. 19(11) 1571–1584.

Laffont, J. 1997. Game theory and empirical economics: The case of auction data. Eur. Econom. Rev. 41(1) 1–35.

Laffont, J., D. Martimort. 2002. The theory of incentives. The Principal Agent Model. Princeton University Press, Princeton, NJ.

Maskin, E., J. Riley. 1985. Auction theory in private values. Amer. Econom. Rev. 75(2) 150–155.

Maskin, E., J. Riley. 2000a. Asymmetric auctions. Rev. Econom. Stud. 67(3) 413–438.

Maskin, E., J. Riley. 2000b. Equilibrium in sealed high bid auctions. Rev. Econom. Stud. 67(3) 439–454.

McAfee, P., J. McMillan. 1988. Incentives in Government Procurements. University of Toronto Press, Toronto.

Milgrom, P. R., J. Roberts. 1982. Limit pricing and entry under incomplete information: An equilibrium analysis. Econometrica 50(2) 443–459.

Milgrom, P. R., R. J. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50(5) 1089–1122.

Mithas, S., J. Jones. 2007. Do auction parameters affect buyer surplus in e-auctions for procurement? Production Oper. Management 16(4) 455–470.

Narasimhan, C. 1988. Competitive promotional strategies. J. Bus. 61(4) 427–449.

OMB. 1993. CIRCULAR A-110: Uniform Administrative Requirements for Grants and Agreements with Institutions of Higher Education, Hospitals, and Other Non-Profit Organizations. Revised on 11/19/93 and further amended on 9/30/99.

Ortega-Reichert, A. 1968. Models for competitive bidding under uncertainty. Unpublished doctoral thesis, Department of Operations Research, Stanford University, Stanford, CA.

Salanie, J. 2000. The Economics of Contracts. MIT Press, Cambridge, UK.

Spence, M. 1973. Job market signaling. Quart. J. Econom. 87(3) 355–374.

Thomas, C. 1996. Market structure and the flow of information in repeated auctions. Working paper, Federal Trade Commission, Washington, DC.

Thomas, C. 2010. Information revelation and buyer profits in repeated procurement competition. J. Indust. Econom. 58(1) 79–105.

Tu, Z. 2005. Why do we use Dutch auction to sell flowers? Information disclosure in sequential auctions. Working paper, Department of Economics, University of Pittsburgh, Pittsburgh, PA.

United-Nations. 2007. United Nations Procurement Manual. Revision 6. http://www.un.org/Depts/ptd/manual.htm.

Wilson, R. 1977. A bidding model of perfect competition. Rev. Econom. Stud. 44(3) 511–518.

Winkler, R., D. Brooks. 1980. Competitive bidding with dependent value estimates. Oper. Res. 28(3, Part I) 603–613.

Yoo, B., V. Choudhary, T. Mukhopadhyay. 2007. Electronic B2B marketplaces with different ownership structures. Management Sci. 53(6) 952–961.
