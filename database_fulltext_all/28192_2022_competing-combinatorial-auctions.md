---
otero_id: 28192
otero_key: "KGZEMY3R"
title: "Competing Combinatorial Auctions"
authors: "Thomas Kittsteiner; Marion Ott; Richard Steinberg"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1018"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Competing Combinatorial Auctions

Thomas Kittsteiner,<sup>a</sup> Marion Ott,<sup>b</sup> Richard Steinberg<sup>c</sup>

<sup>a</sup> School of Business and Economics, RWTH Aachen University, 52056 Aachen, Germany; <sup>b</sup> ZEW – Leibniz Centre for European Economic Research, 68161 Mannheim, Germany; <sup>c</sup> Department of Management, London School of Economics and Political Science, London WC2A 2AE, United Kingdom

https://orcid.org/0000-0001-5199-4664 (MO); r.steinberg@lse.ac.uk, https://orcid.org/0000-0001-9636-472X (RS)

Received: January 8, 2020 Revised: September 28, 2020; February 12, 2021 Accepted: February 18, 2021 Published Online in Articles in Advance: September 7, 2021

https://doi.org/10.1287/isre.2021.1018

Copyright: © 2021 INFORMS

Abstract. We investigate whether revenue-maximizing auctioneers selling heterogeneous items will allow for combinatorial bidding in the presence of auctioneer competition. We compare the choice of auction format by two competing auctioneers with that of a single auctioneer. Bidders are heterogeneous in their demands, with some having synergies for items. We <sup>fi</sup>nd that, even if a single auctioneer offers a combinatorial auction, competing auctioneers in a comparable setting will not. Instead, the competing auctioneers will segment the market by restricting allowable package bids in order to increase competition between bidders. This shows that it might not be advantageous for an online market platform to offer combinatorial auctions as a design option to competing auctioneers.

History: This paper has been accepted for the Information Systems Research Special Section on Market Design and Analytics. Funding: Financial support from the Deutsche Forschungsgemeinschaft [Grants KI 1915/1-1 and OT 487/2-1] is gratefully acknowledged by T. Kittsteiner and M. Ott. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1018.

Keywords: competing auctioneers combinatorial auction electronic marketplace VCG mechanism

## 1. Introduction

In recent years, we have seen the advent of combinatorial auctions as well as the emergence of online market platforms with competing auctioneers.<sup>1</sup> However, “the combinatorial auction mechanism has yet to become popular in the electronic market place” (Adomavicius et al. 2012, p. 811). These observations raise two questions: First, why have combinatorial auctions yet to become popular on online auction platforms with competing auctioneers? Second, should combinatorial auctions be offered as a design choice to competing auctioneers on online auction platforms? This paper is, to our knowledge, the <sup>fi</sup>rst to address these fundamental questions about electronic marketplaces hosting competing auctioneers.

Combinatorial auctions are those auctions that allow bids on packages, that ${ \mathrm { i } } \mathbf { s } ,$ subsets of items, thus enabling bidders to express their synergies for items. Consequently, combinatorial auctions avoid the well-known exposure problem and the converse problem, which we refer to as the bundle problem, which is when a bidder needs to bid on a superset of that bidder’s desired items in order to obtain them. Both problems can have an adverse effect on auctioneer revenue. Although combinatorial auctions eliminate these problems, there might exist a concomitant attenuating effect on auction revenue. To explain, consider a bidder $\beta _ { 1 }$ whose bid is complemented by bids of bidders $\beta _ { 2 } , \beta _ { 3 } , \ldots , \beta _ { k }$ such that together the bids of $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { k }$ cover a set of items desired by some competing bidder, γ. Then, bidder $\beta _ { 1 }$ might bene<sup>fi</sup>t from the complementing bidders, because $\beta _ { 1 } \mathrm { ' s }$ probability of winning against $\gamma$ is increasing in each of the bids of $\beta _ { 2 } , \beta _ { 3 } , \ldots , \beta _ { k }$ . Thus, combinatorial auctions create a free-rider problem, which is associated with low-revenue noncore outcomes.<sup>2</sup>

Our main <sup>fi</sup>nding shows that, even if a single auctioneer permits bids on all packages of items, competing auctioneers might not. To gain some intuition, <sup>fi</sup>rst note that it can be bene<sup>fi</sup>cial for competing auctioneers to segment bidders. Consider the example from the previous paragraph. If bidders $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { k }$ were to bid with a different auctioneer than bidder $\gamma ,$ this segmentation would mitigate the free-rider problem. Second, note that if competing auctioneers restrict package bidding, segmentation of bidders can become self-enforcing. Speci<sup>fi</sup>cally, in order to avoid the bundle problem, bidders $\beta _ { 1 } , \beta _ { 2 } , \ldots , \beta _ { k }$ would avoid auctioneers who allow bids only on the package desired by bidder $\gamma ;$ whereas, in order to avoid the exposure problem, bidder γ would avoid auctioneers who allow bids only on subsets of the desired package.

To show this and derive our main <sup>fi</sup>nding, we adopt the widely used local-local-global (LLG) framework,<sup>3</sup> which is just rich enough to incorporate the free-rider, exposure, and bundle problems. In our benchmark model—the single-auctioneer model—a single auctioneer offers two nonidentical items, A and B, to three heterogeneous bidders. One bidder desires only item A and one only item B; these bidders are referred to as local bidders. The third bidder, referred to as a global bidder, desires only the package of both items. In the main model—the competing-auctioneers model—two competing auctioneers each offer the two items, A and B, and compete for six bidders; speci<sup>fi</sup>cally, for two copies of the three heterogeneous bidders. Thus, our model of competing auctioneers is a duplication and then merger of our single-auctioneer model. The timing in our game-theoretic model is as follows: <sup>fi</sup>rst, the auctioneers announce the packages on which they will accept bids; second, the bidders decide in which auction they will participate; third, bidders submit bids.

We make the following modeling assumptions. First, we concentrate on the most prominent combinatorial auction: the Vickrey-Clarke-Groves (VCG) mechanism (see Ausubel and Milgrom 2002, 2006; Day and Milgrom 2008). This assures that, in most continuation games following the bidders’ participation decisions, each bidder will have a weakly dominant strategy, which is to bid its own valuation. The free-rider problem manifests itself indirectly in the VCG mechanism, whereas it may manifest itself directly through low bids, for example, in pay-as-bid or core-selecting 4 combinatorial auctions.

Second, we parameterize the global bidders’ valuation distribution function in terms of their strength. We employ the uniform distribution, which ful<sup>fi</sup>lls many of the technical assumptions often made to obtain tractable models, such as monotonicity of virtual valuations, or to obtain closed-form solutions. From the analysis it follows that, due to continuity and because all inequalities restricting equilibrium behavior hold with slackness, our results remain valid for distribution functions suf<sup>fi</sup>ciently close to the uniform.

Third, we assume that the item or package in which a bidder is interested, which we call the bidder’s kind, is common knowledge. However, a bidder’s valuation is private information and independent of the other bidders’ valuations. These are standard assumptions in LLG models. (See the references in endnote 3.) A bidder’s kind is more apparent and requires less detailed knowledge about the bidder than knowing the bidder’s valuation. In repeated interactions, knowing the kind of a bidder can be the result of observation and learning. In procurement contexts, production costs are typically private information, whereas information about a <sup>fi</sup>rm’s products is not.

Fourth, we allow each bidder to bid with only one auctioneer. This simpli<sup>fi</sup>cation, which is standard and required in models of competing auctioneers of single items to derive closed-form solutions (e.g., Bapna et al. 2010, Kim and Kircher 2015), can be justi<sup>fi</sup>ed by suf<sup>fi</sup>- ciently high costs of participation, or simply by bidders’ physical inability to interact with more than one auctioneer at a time. Furthermore, in an experiment that allowed for bidding in multiple auctions, most bidders indeed decided to bid with only one auctioneer (Bapna et al. 2010).

Fifth, we restrict attention to equilibria in which bidders’ participation decisions are valuation independent. This implies that, on the equilibrium path, inferences about other bidders’ valuations from their participation decisions are neither necessary nor possible. For this nonempty class of equilibria we provide a full characterization for the relevant parameter range.

The rest of the paper provides a literature review (Section 2), develops our single-auctioneer and competing-auctioneer models (Section 3), presents our results (Section 4), provides additional discussion (Section 5), and concludes (Section 6). An online appendix provides detailed proofs.

## 2. Literature Review

To the best of our knowledge, the restriction of package bidding in combinatorial auctions in a competingauctioneers setting has not been previously addressed in the literature. This paper is related to four different research streams.

First, there exists a literature on competing singleitem auctioneers where each auctioneer offers a single item and bidders are ex ante symmetric. Consequently, the type of horizontal market segmentation that we <sup>fi</sup>nd is not possible in these models. These models vary with regard to the assumed market size (e.g., large <sup>fi</sup>- nite markets, in<sup>fi</sup>nite markets, or two-auctioneer markets), bidder information regarding valuations when choosing an auctioneer, the available auction formats, and whether items are sold in sequential, overlapping, or simultaneous auctions (see McAfee 1993; Peters 1997; Peters and Severinov 1997; Burguet and Sakovics 1999; Parlane 2008; Bapna et al. 2009, 2010; Virag´ 2010; Albrecht et al. 2012, 2014; Kim and Kircher 2015; Truong et al. 2017). For a survey of work in this literature up until 2010, see Pai (2010).

Second, we draw on auction models with bidders facing an exposure problem (see Krishna and Rosenthal 1996, Rosenthal and Wang 1996, Bikhchandani 1999, Szentes and Rosenthal 2003, Szentes 2007, Goeree and Lien 2014). In our framework, we <sup>fi</sup>nd that bidders respond to the exposure problem by submitting either very low or very high bids and may react to increased bidder competition by reducing their bids (for similar results, see Krishna and Rosenthal 1996).

Third, a single auctioneer’s decision regarding the packages on which to allow bids has been investigated for symmetric bidders with additive valuations by Palfrey (1983), Chakraborty (1999), Armstrong (2000), and Jehiel et al. (2007); for symmetric bidders who consider two items complements or substitutes by Subramaniam and Venkatesh (2009); and for asymmetric bidders with single-item or additive-value multi-item demand for two items by Avery and Hendershott (2000). Allowing bids on all packages can be optimal for a single auctioneer facing symmetric bidders with either additive valuations, substitutes valuations, or strong complements valuations (Jehiel et al. 2007, Subramaniam and Venkatesh 2009). Our benchmark scenario with a single auctioneer has not been addressed in these studies. Furthermore, there exist studies that acknowledge the bene<sup>fi</sup>t of reducing complexity for both the bidders and the auctioneer by disallowing bids on some packages (see Rothkopf et al. 1998, Lehmann et al. 2006, Nisan 2006). Our results identify an additional motive for the designer to restrict package bidding or even entirely avoid offering a combinatorial design: the presence of competing auctioneers.

Fourth, the spirit of our result is similar to a central idea from the industrial organization and strategic management literature on the value of product differentiation for competing <sup>fi</sup>rms. In order to mitigate competition, <sup>fi</sup>rms deliberately differentiate their products from those of other <sup>fi</sup>rms. This involves creating a more attractive product for a subset of customers, while at the same time rendering it less attractive for other potential customers. The seminal paper in this large literature is d’Aspremont et al. (1979); Belle<sup>fl</sup>amme and Peitz (2010) provide an introduction to the topic. In contrast to this literature, our paper considers offering different auction formats rather than offering different items for sale.

## 3. The Two Models

## 3.1. The Single-Auctioneer Model

Consider an auctioneer who offers for sale two nonidentical items, A and B, to three bidders.

We use an LLG model, in which bidders are interested in either the one-item package A, the one-item package B, or the two-item package AB. We refer to these three kinds of bidders, respectively, as A-bidders, Bbidders, and AB-bidders. We assume that there is one bidder of each kind. The A- and B-bidders are collectively referred to as local bidders, the AB-bidder is referred to as a global bidder.

Bidder $j ^ { \prime } \mathbf { s }$ valuation for any package that contains this bidder’s preferred package A, B, or AB is given by $v _ { j } \in \mathbb { R } _ { \geq 0 }$ , where $v _ { j }$ is private information.<sup>5</sup> Valuations for packages that do not contain a bidder’s preferred package are commonly known to be zero. The valuations $v _ { j }$ are drawn independently from the commonly known distribution functions $\begin{array} { r } { \dot { v _ { j } } \sim U [ 0 , 1 ] } \end{array}$ for a local bidder, and $v _ { j } \sim U [ 0 , k ] , k > 1$ , for a global bidder. The parameter k measures the strength of the global bidder vis-a-vis the local bidders.\`

Suppose a bidder’s valuation for the package the bidder wins is v, where $\boldsymbol { v } \ = \ \boldsymbol { v } _ { j }$ or $v = 0$ . Then the bidder’s payoff is given by $v - p ,$ , where $p \in \mathbb { R } _ { \geq 0 }$ is the price the bidder pays in the auction. If the bidder wins no package, the payoff to the bidder is zero. Each bidder maximizes its own expected payoff.

The auctions are VCG mechanisms restricted by the allowable bids.<sup>6</sup> The auctioneer’s options can be delineated in terms of three possible auction formats: (i) allowing exclusive bids on A, B, and AB, by offering a VCG mechanism for the two items, denote this option by [A,B]; (ii) allowing nonexclusive bids on A and on B, by offering two separate simultaneous second-price auctions, denote this option by [A][B]; and (iii) allowing bids on AB only, corresponding to a single secondprice auction on the package AB, denote this option by [AB]. These three are the only options that need to be considered, because an auctioneer would never want to restrict bids to only on A or only on B, and because options to allow exclusive bids on A and AB, or on B and AB, are equivalent to offering [AB]. (See the proofs in Online Appendix B.2.4 and B.3.) The auctioneer maximizes expected revenue. We assume that an auctioneer prefers the combinatorial auction [A,B] over both [AB] and [A][B] only if the combinatorial auction generates a strictly larger expected revenue.<sup>7</sup>

The game consists of the following two stages:

Stage 1: The auctioneer chooses an auction format among [A,B], [A][B], and [AB]. The chosen auction format becomes common knowledge. Thus, each decision by the auctioneer de<sup>fi</sup>nes a subgame.

Stage 2: The bidders observe their private valuations and then simultaneously and independently submit bids. Items are allocated and payments are made. Ties are broken randomly.

A bidder’s strategy consists of a bidding strategy for each auction format. A bidder can submit bids on all permissible packages but has the option not to submit a bid on some or all packages.

## 3.2. The Competing-Auctioneers Model

This setup is a duplication and merger of the singleauctioneer setting. Two auctioneers, each offering items A and B, compete for six bidders: two A-bidders, two B-bidders, and two AB-bidders.

The game consists of the following three stages:

Stage 1: The two auctioneers simultaneously and independently choose an auction format among [A,B], [A][B], and [AB]. The chosen auction formats become common knowledge. Thus, each combination of decisions by the auctioneers de<sup>fi</sup>nes a subgame.

Stage 2: The bidders observe their private valuations and then simultaneously and independently make their participation decisions; each bidder can participate in the auction of only one auctioneer.

Stage 3: The bidders observe all participation decisions and then simultaneously and independently submit bids. Items are allocated and payments are made.

Ties are broken randomly, with exceptions where this would not preserve value.<sup>8</sup>

A bidder’s strategy consists of a participation decision for each feasible pair of offered auction formats by the auctioneers together with the bidder’s bidding strategies for each observed bidder partition.

## 3.3. Equilibrium Concept

We consider perfect Bayesian equilibria in pure strategies with the following three properties:

P1: A bidder’s participation decisions are independent of the bidder’s valuation.

P2: A bidder submits only undominated bids.

P3: If a global bidder participates in [A][B], then bidders play according to an ef<sup>fi</sup>cient ex post equilibrium, if it exists.<sup>9</sup>

Formal speci<sup>fi</sup>cations of these properties are provided in Online Appendix B.1. It should be emphasized that these properties constitute an equilibrium selection criterion and not a restriction on the strategies available to players. If an equilibrium with these properties exists, then it is selected. In Theorem 2, we show existence for a range of parameter values of k.

Property P1 can be thought of as a simplicity criterion. If an equilibrium can include pooling participation strategies, then these strategies should be selected, because they imply simpler beliefs for the bidders than nonpooling strategies. Property P1 implies that a bidder does not reveal any private information with the participation decision. Thus no bidder has an incentive to switch auctions after observing the participation decisions of other bidders. In this sense, participation decision are stable, and we do not need to assume that, once executed, participation decisions cannot be revoked. Also, for any equilibrium with property P1, there is a payoff-equivalent equilibrium in a modi<sup>fi</sup>ed game in which bidders learn their valuation only after the participation decision. Properties P2 and P3 are common re<sup>fi</sup>nements.

## 4. Results

In order to identify and evaluate the relevance of competition for the choice of auction format, we start by analyzing the cases of a single auctioneer and of competing auctioneers separately, and then compare the two cases to derive our main result. The single auctioneer’s optimal decision is given in the following theorem.

Theorem 1. Consider the single-auctioneer model. There exists a unique <sup>ˆ</sup>k such that in any equilibrium in pure strategies with properties P1 and P2:

For all $k > \hat { k } .$ , the auctioneer offers the combinatorial auction $I A , B J .$

For all $k \leq \hat { k } ,$ , the auctioneer offers [AB].

The single auctioneer never offers [A][B] because for all k the auctioneer is better off by offering $[ \mathrm { A } , \mathrm { B } ] ,$ which shields the global bidder from the exposure problem. Whether the auctioneer prefers [A,B] or [AB] depends on the strength of the global bidder. With a strong global bidder, generating competition for the global bidder is more important; with a weak global bidder, generating competition between local bidders is more important. In $[ \bar { \bf A } , \bar { \bf B } ]$ , local bidders complement each other against the global bidder, whereas [AB] creates competition between local bidders.

In contrast to the single-auctioneer case, the competing auctioneers’ auction format choices determine revenue by affecting the number and kind of participating bidders. The following theorem describes the equilibria of the competing-auctioneers model.

Theorem 2. Consider the competing-auctioneers model. There exists a unique k∗ such that an equilibrium in pure strategies with properties P1, P2, and P3 exists if and only $i f k \le k ^ { * }$ . For every $k \leq k ^ { * }$ , the following hold:

a. There exists an equilibrium in which one auctioneer offers [A][B] and one auctioneer offers [AB]. There does not exist an equilibrium in which both auctioneers offer a combinatorial auction.

b. In every equilibrium, all local bidders bid for the items of the same auctioneer and all global bidders bid for the items of the other auctioneer.

If global bidders are weak, speci<sup>fi</sup>cally if $k \leq \hat { k }$ (as determined in Theorem 1), there may be additional equilibria to the one mentioned in Theorem 2, part (a). These are: (i) both auctioneers offer [A][B] and one attracts the local bidders and the other attracts the global bidders; and (ii) one auctioneer offers [A,B] and attracts the local bidders, and the other auctioneer offers [A][B] or [AB] and attracts the global bidders.

Remarkably, even if the combinatorial auction [A,B] is offered in equilibrium, only local bidders will enter that auction, and thus the auctioneer with the combinatorial auction allows bids on more packages than are necessary to accommodate the heterogeneity of the participating bidders. We discuss this counterintuitive result in Section 5.

In all equilibria, one auctioneer is better off than the other auctioneer (unless k 2). The auctioneer who attracts the local bidders receives an expected revenue of $2 / 3 ,$ and the auctioneer who attracts the global bidders receives an expected revenue of $k / 3 .$ . (See Proposition 1 in Online Appendix B.2.)

If global bidders are signi<sup>fi</sup>cantly stronger than local bidders, $k > k ^ { * }$ , then equilibria with properties P1, P2, and P3 fail to exist in the competing-auctioneers setting, because some subgames fail to have equilibria with these properties.

Our main <sup>fi</sup>nding, Theorem $^ { 3 , }$ shows that competing auctioneers might not choose a combinatorial auction, even if a single auctioneer would do so.

Theorem 3. Let <sup>ˆ</sup>k be as in Theorem 1 and k∗ as in Theorem 2. It holds that $\hat { k } < k ^ { * }$ . For every $\hat { k } < k \le k ^ { * }$ , in every equilibrium in pure strategies with properties P1, P2, and P3 of the competing-auctioneers model, one auctioneer offers [A][B] and one offers [AB], whereas a single auctioneer offers [A,B].

Thus, for levels of k for which the single auctioneer offers the combinatorial auction, neither of the competing auctioneers offers a combinatorial auction. This is because a single auctioneer, by choosing an auction format, needs to trade off the negative effects on revenue caused by the exposure problem (in [A][B]) or the bundle problem (in [AB]) with that of the free-rider problem (in [A,B]). Competing auctioneers share the market. They have the option to segment the market, which can be achieved by offering noncombinatorial auctions, thereby eliminating the free-rider, exposure, and bundle problems. In order to achieve segmentation, the auctioneers can offer different noncombinatorial auction formats. One auctioneer offers [A][B] and attracts all local bidders; the other auctioneer offers [AB], attracts all global bidders, and has the higher expected revenue.

## Example to Illustrate the Auctioneers’ Choices

Let $k = 7 / 3 \in ( \hat { k } , k ^ { * } ]$ . (This value of k is in the relevant range for Theorem 3 because, as shown in the online appendix, $\hat { k } = 2$ and $k ^ { * } = 8 / 3 . )$ ) A single auctioneer’s revenue from offering [A][B], [AB], or [A,B] is 0.57, 0.60, or 0.64, respectively. Competing auctioneers’ revenues in Stage 1 are depicted in Table 1 for the nine subgames. (Complete tables for any $k \leq k ^ { * }$ are derived in Online Appendix B.2.) Auctioneers’ equilibrium revenues are in bold.

A single auctioneer would offer a combinatorial auction and receive an expected revenue of 0.64. This is also the expected revenue of a competing auctioneer if both auctioneers offer [A,B] and attract the same kinds of bidders. However, for every auction format offered by the competitor, an auctioneer has an incentive to offer a different auction format targeted at local ([A][B]) or global ([AB]) bidders, thereby inducing bidder segmentation and a higher expected revenue of 0.67 or 0.78, respectively. Only if one auctioneer offers [A][B] and the other auctioneer offers [AB] does neither auctioneer have an incentive to deviate.

Table 1. Expected Auctioneer Revenue for $k = 7 / 3$

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Auctioneer 2</td></tr><tr><td>[A][B]</td><td>[AB]</td><td>[A,B]</td></tr><tr><td rowspan="3">Auctioneer 1</td><td>[A][B]</td><td>(0.57,0.57)</td><td>(0.67,0.78)</td><td>(0.67,0.78)</td></tr><tr><td>[AB]</td><td>(0.78,0.67)</td><td>(0.60,0.60)</td><td>(0.78,0.67)</td></tr><tr><td>[A,B]</td><td>(0.78,0.67)</td><td>(0.67,0.78)</td><td>(0.64,0.64)</td></tr></table>

Note. Auctioneers’ equilibrium revenues are in bold.

## Idea of Proof of Theorem 2

We focus on the main drivers of the players’ equilibrium decisions. First we describe bidding behavior in the various possible auctions, then we discuss what drives bidders’ participation decisions, and <sup>fi</sup>nally we explain why this makes auctioneers prefer to differentiate.

With the exception of global bidders in [A][B], all bidders—regardless of the auction in which they chose to participate—bid their valuation. A global bidder’s bidding strategy in [A][B] depends on the bidder’s information about the other bidders in the auction, consisting of the number and kind of the other bidders. In particular, if there is at least one A-bidder and at least one B-bidder, global bidders in [A][B] face an exposure problem. To avoid this problem, global bidders either submit a bid of zero on each item if their valuation for the package is suf<sup>fi</sup>ciently small, or otherwise bid in a way that ensures that they win against any local bidder.

Bidders’ participation decisions are driven by four considerations. First, global bidders tend to avoid [A][B] with local bidders due to the exposure problem. Second, global bidders tend to avoid the combinatorial auction [A,B] with local bidders, because local bidders who want different items complement each other, which effectively makes them jointly compete against global bidders. Third, local bidders avoid [AB] with other local (and global) bidders because of a bundle problem, that is, because they will need to compete against all of the bidders.<sup>10</sup> Fourth, bidders tend to avoid an auctioneer who attracts more or stronger bidders, and thus there is a tendency toward an equal distribution of bidders. Bidder segmentation is mainly a consequence of the <sup>fi</sup>rst three considerations if auctioneers offer different auction formats.

In general, for $k \leq k ^ { * } .$ , auctioneers collectively bene<sup>fi</sup>t from a segmented market and the resulting bidder homogeneity; that is, they bene<sup>fi</sup>t from attracting only local or only global bidders. This is because, in each auction of a segmented market, local and global bidders do not compete against each other, and each bidder can bid on its desired package. Therefore, the free-rider, exposure, and bundle problems vanish and low-revenue (noncore) outcomes do not occur. Which market segment—that of the local bidders or that of the global bidders—is more remunerative for an auctioneer depends on the relative strengths of these subsets of bidders, as determined by the value of k. Being able to attract the more remunerative market segment provides the auctioneer with an additional incentive for segmentation.

If global bidders are weak, speci<sup>fi</sup>cally if $k \leq \hat { k } ,$ the highest expected revenue a competing auctioneer can obtain is that from the market segment of the local bidders. If one auctioneer offers [A][B] and the other offers [AB], then bidders will segment and the auctioneers will have no incentive to deviate from their choices. The auctioneer offering [A][B] already has the highest possible expected revenue. The auctioneer offering [AB], by deviating to [A,B], will still attract the global bidders, and by deviating to [A][B] expects a lower revenue due to the exposure problem (as then bidders do not segment). There cannot be an equilibrium where both auctioneers offer the combinatorial auction [A,B], because at least one of them would prefer to attract all global bidders by offering [AB].

If global bidders are stronger, speci<sup>fi</sup>cally if $\hat { k } < k \leq$ k∗ (as in the previous example with $k = 7 / 3 )$ , the highest expected revenue a competing auctioneer can obtain is that from the market segment of the global bidders. Also, attracting all local bidders is more remunerative than attracting one bidder of each kind, which creates a free-rider, exposure, or bundle problem. If only one auctioneer offers [AB], this auctioneer will necessarily (i.e., in any equilibrium of a subgame following such a choice) attract the global bidders, and thus cannot do better. If one auctioneer offers [AB] and the other offers [A][B], the auctioneer offering [A][B] cannot, by deviating to a different auction, attract the global bidders.

If global bidders are signi<sup>fi</sup>cantly stronger than local bidders, $k > k ^ { * }$ , then only in the three subgames starting at the auctioneers’ choices of ([A][B], [A][B]), ([AB], [AB]), or ([A,B], [A,B]) do equilibria with properties P1, P2, and P3 exist. No competing auctioneer will be able to attract both global bidders, because a global bidder with a high valuation $( v \in ( k ^ { * } , k ] )$ wants to avoid the other global bidder even if that requires the global bidder to compete against all local bidders. In subgames, only equilibria in which bidders split into two symmetric groups are possible. As for $k \leq \bar { k } ^ { * }$ , these can occur only if both auctioneers offer the same format.

## 5. Discussion

Bidders segment in all equilibria satisfying P1, P2, and P3 (Theorem 2, part (b)). This segmentation naturally occurs in equilibria where the auctioneers offer auction formats [AB] and [A][B] tailored to the respective segments. However, we can have additional, less intuitive equilibria if global bidders are suf<sup>fi</sup>ciently weak, but each will have a more intuitive counterpart with the same revenues for auctioneers and payoffs for bidders. If $k < \hat { k } ,$ we can have one auctioneer offering the combinatorial auction [A,B] and attracting the local bidders, and the other offering [A][B] and attracting the global bidders. Notably, one auctioneer allows bids on more packages than is necessary to accommodate the participating bidders’ heterogeneity, whereas the other auctioneer does not allow the participating global bidders to bid on the package. To understand why these counterintuitive equilibria exist, note that the auctioneer who offers the combinatorial auction [A,B] attracts the more remunerative segment, viz., the local bidders. This is possible because, conditional on segmentation, these two auction formats, [A,B] and [A][B], are payoff-equivalent for all bidders (due to the lack of an exposure problem in [A][B] without local bidders). The auctioneer offering [A,B] would attract a strictly less remunerative set of bidders if the auctioneer offered a different auction format. If the auctioneer offered the same format as the competitor, then the market would not be segmented, and if the auctioneer offered [AB], then this would attract the global bidders. The auctioneer who offers [A][B] would attract the same (global) bidders and receive the same expected revenues if the auctioneer deviated to [AB], or would attract one bidder of each kind if the auctioneer offered [A,B], which would be less remunerative due to the low-revenue (free-rider) problem of [A,B]. We cannot have that one auctioneer offers [A,B] and the other offers [AB], unless global bidders are almost as weak as local bidders. (For this exceptional case, k 1, see Section B.2.3 in the online appendix.) In contrast, if $k \geq \hat { k } ,$ there is no equilibrium in which an auctioneer offers the combinatorial auction [A,B]. This is because, given the choice between [AB] and [A,B], global bidders will necessarily participate in [AB]. Thus the auctioneer offering [A,B] will get the local bidders and will want to deviate to [A][B].

A comparison of revenues in the competing-auctioneer and single-auctioneer models reveals that auctioneers bene<sup>fi</sup>t from competition if market size, in terms of the number and kind of buyers, increases proportionally. More precisely, the sum of the competing auctioneers’ expected revenues is larger than twice the expected revenue in the single-auctioneer model. If market segments do not differ too much in their attractiveness to auctioneers, viz., if k is neither too small nor too large, then each auctioneer is better off under competition than in the single-auctioneer setup. This suggests that allowing for or intensifying competition in an electronic marketplace can help attract auctioneers, if the average number of bidders per auctioneer does not decrease.

We have discussed the free-rider problem in the VCG mechanism. This problem is not speci<sup>fi</sup>c to this auction. For example, for k  2 in our LLG setting, the expected revenue from [A,B] is 0.583, and the expected revenue from the combinatorial pay-as-bid auction and from various bidder-optimal core-selecting auctions has been calculated to values between 0.500 and 0.596 (Baranov 2010, Beck and Ott 2013, Ausubel and Baranov 2020). Speci<sup>fi</sup>cally, these expected revenues are below the expected total valuations of the losing bidders (0.708), which implies the occurrence of noncore outcomes in these auctions (see, e.g., Ausubel and Milgrom 2006, Day and Milgrom 2008, for the low-revenue problem and the core).

## 6. Conclusion

Although a single auctioneer may offer a combinatorial auction, competing auctioneers in a comparable setting will not. Instead, the competing auctioneers will segment the market by restricting the packages on which they accept bids, attracting more homogeneous sets of bidders, resulting in increased bidder competition. The advantage to an auctioneer of accommodating bidder heterogeneity via a combinatorial auction is dominated in a competing-auctioneer setting by the greater advantage from attracting homogeneous sets of bidders who will compete more <sup>fi</sup>ercely with each other.

The intuition for our results rests upon the presence of the free-rider problem and the associated low revenues. The intuition does not extend to scenarios without a free-rider problem, for example, if all items are substitutes for all bidders. Our model is rich enough to incorporate the free-rider problem while still maintaining tractability. This allows us to identify the free-rider, exposure, and bundle problems as suf<sup>fi</sup>cient drivers for bene<sup>fi</sup>cial market segmentation. The effect of additional auction design features (e.g., payment rules, reserve prices) on these drivers, and therefore on the auctioneers’ incentives to segment the market, remain unaddressed. We leave this for future research.

According to Adomavicius et al. (2012, p. 811), the explanation for the scarcity of online combinatorial auctions is “the computational complexity of determining winners in such auctions and the cognitive complexity of formulating combinatorial bids.” In this paper, we examined combinatorial auctions in online markets where both types of complexity become insigni<sup>fi</sup>cant, revealing an additional explanation for the scarcity of competitive combinatorial auctions in the electronic marketplace.

Our <sup>fi</sup>ndings may help to explain why, despite the increased use of combinatorial auctions in markets with a single auctioneer, combinatorial auction formats have largely been absent from online market platforms. These <sup>fi</sup>ndings have implications for market design and, in particular, show that it might not be advantageous for an online market platform on which different sellers and buyers interact to offer combinatorial auctions as a design option to competing auctioneers.

## Acknowledgments

The authors thank the associate editor and two anonymous reviewers for their especially helpful comments.

## Endnotes

<sup>1</sup> For combinatorial auctions of a single auctioneer, see Bichler et al. (2006), Cantillon and Pesendorfer (2006), Caplice and Sheffi (2006), Olivares et al. (2012), Ausubel and Baranov (2014), Goossens et al. (2014), Mastropietroa et al. (2014). For competing auctioneers, see Bapna et al. (2010), Andersson et al. (2012), Han et al. (2018).

<sup>2</sup> An auction outcome is a noncore outcome if there is a group of bidders who, together with the auctioneer, can generate a higher payoff

for each of them by trading among themselves. The free-rider problem in this context is often referred to as the threshold problem.

<sup>3</sup> The use of LLG models goes back at least to Krishna and Rosenthal (1996). Other papers employing an LLG model include Erdil and Klemperer (2010), Beck and Ott (2013), Goeree and Lien (2016), Baisa and Burkett (2018), Ausubel and Baranov (2020), Bosshard et al. (2020), Finster (2020).

<sup>4</sup> For combinatorial pay-as-bid auctions, see Baranov (2010), Bosshard et al. (2020); for combinatorial core-selecting auctions, see Sano (2012), Goeree and Lien (2016), Ausubel and Baranov (2020). For the magnitude of the free-rider problem in various auctions, see Section 5. An empirical counterfactual analysis for a large-scale VCG mechanism found that it performed similarly to the analyzed pay-as-bid combinatorial auction (Kim et al. 2014).

<sup>5</sup> This implies free disposal.

<sup>6</sup> For a definition of the VCG mechanism, see, for example, Krishna (2010, chapter 16), or Ausubel and Milgrom (2006).

<sup>7</sup> That is, we break an auctioneer’s indifference between [A,B] and [A][B], or between [A,B] and [AB], in favor of the less complex auction format. In the single-auctioneer model, this rule will be applied only for one value of k. In the competing-auctioneers model, we will need to apply this tie-breaking rule only in cases where the auctions’ sets of participants are equal and consist only of local or only of global bidders.

8 Specifically, in [A][B], ties among global bidders are broken such that both items are allocated to the same global bidder. If global bidders in [A][B] submit the same bid on one package but not on the other, this tie is broken in favor of the bidder with the higher bid on the other package; if global bidders in [A][B] tie with their bids on both packages, both ties are broken in favor of the same global bidder, which is chosen randomly.

<sup>9</sup> Existence of such an equilibrium in the continuation game is guaranteed if, in addition to the global bidder, another global bidder and/or local bidders of only one kind participate. See Lemma 2 in Online Appendix B.2.1. As this cannot happen in the single-auctioneer case, property P3 will not appear in Theorem 1.

<sup>10</sup> Note that in [A][B] and [A,B] local bidders compete only with local bidders of the same kind (and global bidders) and, in addition, local bidders can free-ride on bids of local bidders of the other kind.

## References

Adomavicius G, Curley SP, Gupta A, Sanyal P (2012) Effect of information feedback on bidder behavior in continuous combinatorial auctions. Management Sci. 58(4):811–830.

Albrecht J, Gautier P, Vroman S (2012) A note on Peters and Severinov, “Competition among sellers who offer auctions instead of prices. J. Econom. Theory 147(1):389–392.

Albrecht J, Gautier P, Vroman S (2014) Ef<sup>fi</sup>cient entry in competing auctions. Amer. Econom. Rev. 104(10):3288–3296.

Andersson T, Andersson C, Andersson F (2012) An empirical investigation of ef<sup>fi</sup>ciency and price uniformity in competing auc-Econom. Lett. –

Armstrong M (2000) Optimal multi-object auctions. Rev. Econom. Stud. 67(3):455–481.

Ausubel LM, Baranov OV (2014) Market design and the evolution of the combinatorial clock auction. Amer. Econom. Rev. 104(5): 446–451.

Ausubel LM, Baranov OV (2020) Core-selecting auctions with incomplete information. Internat. J. Game Theory 49(1):251–273.

Ausubel LM, Milgrom PR (2002) Ascending auctions with package bidding. B. E. J. Theoret. Econom. 1(1):1–44.

Ausubel LM, Milgrom P (2006) The lovely but lonely Vickrey auction. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 17–40.

Avery C, Hendershott T (2000) Bundling and optimal auctions of multiple products. Rev. Econom. Stud. 67(3):483–497.

Baisa B, Burkett J (2018) Large multi-unit auctions with a large bidder. J. Econom. Theory 174:1–15.

Bapna R, Dellarocas C, Rice S (2010) Vertically differentiated simultaneous Vickrey auctions: Theory and experimental evidence. Management Sci. 56(7):1074–1092.

Bapna R, Chang SA, Goes P, Gupta A (2009) Overlapping online auctions: Empirical characterization of bidder strategies and auction prices. Management Inform. Systems Quart. 33(4):763–783.

Baranov O (2010) Exposure vs. free-riding in auctions with incomplete information. Working paper, University of Maryland, College Park, MD.

Beck M, Ott M (2013) Incentives for overbidding in minimum-revenue core-selecting auctions. Accessed June 9, 2021, http://hdl.handle .net/10419/79946.

Belle<sup>fl</sup>amme P, Peitz M (2010) Industrial Organization: Markets and Strategies (Cambridge University Press, Cambridge, UK).

Bichler M, Davenport A, Hohner G, Kalagnanam J (2006) Industrial procurement auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 593–612.

Bikhchandani S (1999) Auctions of heterogeneous objects. Games Econom. Behav. 26(2):193–220.

Bosshard V, Bunz B, Lubin B, Seuken S (2020) Computing Bayes-¨ Nash equilibria in combinatorial auctions with veri<sup>fi</sup>cation. J. Artificial Intelligence Res. 69:531–570.

Burguet R, Sakovics J (1999) Imperfect competition in auction designs. Internat. Econom. Rev. 40(1):231–247.

Cantillon E, Pesendorfer M (2006) Auctioning bus routes: The London experience. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 573–591.

Caplice C, Shef<sup>fi</sup> Y (2006) Combinatorial auctions for truckload transportation. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 539–571.

Chakraborty I (1999) Bundling decisions for selling multiple objects. Econom. Theory 13(3):723–733.

d’Aspremont C, Gabszewicz JJ, Thisse J-F (1979) On Hotelling’s “Stability in competition.” Econometrica 47(5):1145–1150.

Day R, Milgrom PR (2008) Core-selecting package auctions. Internat. J. Game Theory 36(3):393–407.

Erdil A, Klemperer P (2010) A new payment rule for core-selecting package auctions. J. Eur. Econom. Assoc. 8(2–3):537–547.

Finster S (2020) Strategic bidding in product-mix, sequential, and simultaneous auctions. Economics Papers 2020-W03, Economics Group, Nuf<sup>fi</sup>eld College, University of Oxford, Oxford, UK.

Goeree JK, Lien Y (2014) An equilibrium analysis of the simultaneous ascending auction. J. Econom. Theory 153(1):506–533.

Goeree JK, Lien Y (2016) On the impossibility of core-selecting auctions. Theoret. Econom. 11(1):41–52.

Goossens DR, Onderstal S, Pijnacker J, Spieksma FCR (2014) Solids: A combinatorial auction design for real estate. Interfaces 44(4):351–363.

Han J, Qiu C, Popkowski Leszczyc P (2018) The effects of competitive reserve prices in online auctions. Eur. J. Marketing 52(7/8): 1439–1456.

Jehiel P, Meyer-ter-Vehn M, Moldovanu B (2007) Mixed bundling auctions. J. Econom. Theory 134(1):494–512.

Kim K, Kircher P (2015) Ef<sup>fi</sup>cient comeptition through cheap talk: The case of competing auctions. Econometrica 83(5):1849–1875.

Kim SW, Olivares M, Weintraub GY (2014) Measuring the performance of large-scale combinatorial auctions: A structural estimation approach. Management Sci. 60(5):1180–1201.

Krishna V (2010) Auction Theory, 2nd ed. (Academic Press, San Diego, CA).

Krishna V, Rosenthal RW (1996) Simultaneous auctions with synergies. Games Econom. Behav. 17(1):1–31.

Lehmann D, Muller R, Sandholm T (2006) The winner determina-¨ tion problem. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 297–317.

Mastropietroa P, Batlle C, Barroso LA, Rodilla P (2014) Electricity auctions in South America: Toward convergence of system adequacy and RES-E support. Renewable Sustainable Energy Rev. 40:375–385.

McAfee RP (1993) Mechanism design by competing sellers. Econometrica 61(6):1281–1312.

Nisan N (2006) Bidding languages for combinatorial auctions. Cramton P, Shoham Y, Steinberg R, eds. Combinatorial Auctions (MIT Press, Cambridge, MA), 215–232.

Olivares M, Weintraub GY, Epstein R, Yung D (2012) Combinatorial auctions for procurement: An empirical study of the Chilean school meals auction. Management Sci. 58(8):1458–1481.

Pai MM (2010) Competition in mechanisms. ACM SIGecom Exchanges 9(1):1–5.

Palfrey TR (1983) Bundling decisions by a multiproduct monopolist with incomplete information. Econometrica 51(2):463–483.

Parlane S (2008) Auctioning horizontally differentiated items. Rev. Indust. Organ. 33(2):113–128.

Peters M (1997) A competitive distribution of auctions. Rev. Econom. Stud. 64(1):97–123.

Peters M, Severinov S (1997) Competition among sellers who offer auctions instead of prices. J. Econom. Theory 75(1):141–179.

Rosenthal RW, Wang R (1996) Simultaneous auctions with synergies and common values. Games Econom. Behav. 17(1):32–55.

Rothkopf MH, Pekec A, Harstad RM (1998) Computationally manage- ˇ able combinational auctions. Management Sci. 44(8):1131–1147.

Sano R (2012) Non-bidding equilibrium in an ascending core-selecting auction. Games Econom. Behav. 74(2):637–650.

Subramaniam R, Venkatesh R (2009) Optimal bundling strategies in multiobject auctions of complements or substitutes. Marketing Sci. 28(2):264–273.

Szentes B (2007) Two-object two-bidder simultaneous auctions. Internat. Game Theory Rev. 9(3):483–493.

Szentes B, Rosenthal RW (2003) Three-object two-bidder simultaneous auctions: Chopsticks and tetrahedra. Games Econom. Behav. 44(1):114–133.

Truong HM, Gupta A, Ketter W, van Heck E (2017) Effects of presales posted price channel on sequential B2B Dutch <sup>fl</sup>ower auctions. 38th Internat. Conf. Inform. Systems: Transforming Soc. Digital Innovation, ICIS 2017, vol. 14, Seoul

Virag G (2010) Competing auctions: Finite markets and conver-´ gence. Theoret. Econom. 5(2):241–274.

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
