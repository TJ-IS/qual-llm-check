---
otero_id: 7970
otero_key: "H6SYGDDT"
title: "Ex Ante Information and the Design of Keyword Auctions"
authors: "De Liu; Jianqing Chen; Andrew B. Whinston"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0225"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [128.122.253.212] On: 01 July 2015, At: 17:19 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## 6SR

![](/api/attachments/H6SYGDDT/fulltext/images/474e77dbb7c6ff6dd44bd107c7966ee1eae9e3ca53db7e4b2982aa715b85b3cc.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Ex Ante Information and the Design of Keyword Auctions

De Liu, Jianqing Chen, Andrew B. Whinston,

To cite this article:

De Liu, Jianqing Chen, Andrew B. Whinston, (2010) Ex Ante Information and the Design of Keyword Auctions. Information Systems Research 21(1):133-153. http://dx.doi.org/10.1287/isre.1080.0225

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/H6SYGDDT/fulltext/images/e6208f228beac58fce90e69c23f3ca7d861935b5a2b2642eec3c5e9eea5d57fa.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Ex Ante Information and the Design of Keyword Auctions

De Liu

Gatton College of Business and Economics, University of Kentucky, Lexington, Kentucky 40506, de.liu@uky.edu

Jianqing Chen

University of Calgary, Haskayne School of Business, Calgary, Alberta T2N 1N4, Canada, jiachen@ucalgary.ca

Andrew B. Whinston

Red McCombs School of Business, The University of Texas at Austin, Austin, Texas 78712, abw@uts.cc.utexas.edu

eyword advertising, including sponsored links and contextual advertising, powers many of today’s online information services such as search engines and Internet-based emails. This paper examines the design of keyword auctions, a novel mechanism that keyword advertising providers such as Google and Yahoo! use to allocate advertising slots. In our keyword auction model, advertisers bid their willingness-to-pay per click on their advertisements, and the advertising provider can weight advertisers’ bids differently and require differ ent minimum bids based on advertisers’ click-generating potential. We study the impact and design of such weighting schemes and minimum-bid policies. We find that weighting scheme determines how advertisers with different click-generating potential match in equilibrium. Minimum bids exclude low-valuation advertisers and at the same time may distort the equilibrium matching. The efficient design of keyword auctions requires weighting advertisers’ bids by their expected click-through-rates, and requires the same minimum weighted bids. The revenue-maximizing weighting scheme may or may not favor advertisers with low click-generating potential. The revenue-maximizing minimum-bid policy differs from those prescribed in the standard auction design literature. Keyword auctions that employ the revenue-maximizing weighting scheme and differentiated minimum bid policy can generate higher revenue than standard fixed-payment auctions. We draw managerial implications for pay-per-click and other pay-for-performance auctions and discuss potential applications to other areas.

Key words: keyword auctions; keyword advertising; sponsored links; weighted unit-price auctions; weighting scheme; Google; Yahoo!; minimum bid

History: Sumit Sarkar, Senior Editor; Arun Sundararajan, Associate Editor. This paper was received on October 31, 2006, and was with the authors 5 months for 4 revisions. Published online in Articles in Advance November 13, 2009.

## 1. Introduction

Advances in information technology have created radically new business models, most notably the integration of advertising with keyword-based targeting, or “keyword advertising.” A growing number of online services, including search engines, news websites, and Internet-based emails, are powered by keyword advertising, which reached a total revenue of \$8.5 billion in 2007 (Interactive Advertising Bureau and PricewaterhouseCoopers 2008). Keyword advertising has two main variations: advertising based on keywords employed by users in search engines, often known as “sponsored links,” and advertising based on keywords embedded in the content users view, often known as “contextual advertising.” Keyword advertising is distinguished from offline advertising and other online advertising because it delivers the most relevant advertisement to Internet users, yet in less intrusive ways. The effectiveness of this type of advertising has been demonstrated in its acceptance among marketers. The leading provider of keyword advertising, Google, increased its total revenue 39-fold between 2002 and 2007 to \$16.6 billion, mostly from keyword advertising. Keyword advertising has consistently accounted for about 40% of the total online advertising revenue in the last few years and will remain the biggest form of online advertising for years to come. It is expected to reach about \$16.8 billion by 2011 (eMarketer 2007).

Keyword advertising is undoubtedly enabled by new information technologies. One of the key differences between keyword advertising and traditional forms of advertising such as radio and television is that keyword advertising providers, with the help of information technology, can better track outcomes of advertisements including how many Internet users click on them and the number that end up making a purchase. The ability to track such outcomes not only allows marketers to better account for their advertising campaigns, but also shapes the design of keyword auctions—a novel mechanism that keyword advertising providers such as Google, Yahoo!, and MSN use to allocate advertising slots. First, it enables outcomebased pricing (or pay-for-performance), including the now standard “pay-per-click,” in which advertisers pay only when Internet users click on their advertisements, and new variants such as “pay-per-call” (advertisers pay each time an Internet user contacts the advertiser) and “pay-per-purchase” (advertisers pay each time an Internet user follows the advertisement to make a purchase). Second, it allows advertising providers to gather information on advertisers’ potential to generate outcomes. For example, in pay-per-click advertising, advertising providers typically accumulate information on advertisers’ clickthrough rates (CTRs)—the number of clicks on an advertisement divided by the number of times displayed—which can be used to infer advertisers’ click-generating potential. This paper examines how such information—the ex ante information on advertisers’ potential to generate outcomes—should be integrated into the design of keyword auctions that use outcome-based pricing.

The ex ante information on advertisers’ outcomegenerating potential has been gradually integrated into keyword auction designs in terms of ranking rules and minimum-bid policies. The initial keyword auctions, as introduced by Overture (now a subsidiary of Yahoo!), rank advertisers solely by their willingnessto-pay per click (henceforth unit price), thus making no use of information on advertisers’ click-generating potential. In 2002, Google used such information for the first time by ranking advertisers by the product of unit prices they bid and their historical CTRs so that, everything else being equal, an advertiser with a higher CTR will get a better slot. Later, Google extended the ranking factor from CTRs to a more comprehensive “quality score” that also takes into account the quality of the advertisement text and other unannounced relevance factors. Yahoo! adopted a similar ranking rule in its new advertising platform. Recently, advertising providers have begun to make minimum bids depend on advertisers’ click-generating potential. For example, Google recently switched from a onesize-fits-all minimum-bid policy to one that requires higher minimum bids for advertisers with low CTRs. These novel designs raise many questions. For example, what is the impact of the weighted ranking rules and differentiated minimum-bid policies on advertisers’ equilibrium bidding behavior? How should advertising providers rank advertisers with different CTRs and set minimum bids for them? The goal of this paper is to address these issues.

We address the issues by studying a model of keyword auctions. In this model, advertisers bid unit prices; the advertising provider not only receives unitprice bids from advertisers but also takes into account the information on the advertisers’ click-generating potential. Such information allows the advertising provider to differentiate advertisers with high expected CTRs (h type) from those with low expected CTRs (l type). Advertisers, on the other hand, cannot tell another advertiser’s CTR-type or valuation-perclick. The advertising provider can assign different weighting factors and impose different minimum bids for advertisers with high and low expected CTRs. Using such a framework, we study how weighting schemes and differentiated minimum-bid policies affect advertisers’ equilibrium bidding and how to design such keyword auctions in terms of choosing weighting factors and minimum bids for advertisers with different expected CTRs. Such design issues depart from those in standard auctions where no similar information exists. Our focus on design issues also differentiates our study from studies that focus on equilibrium analysis under given auction rules, such as Edelman et al. (2007) and Varian (2007). More importantly, how to best design weighting schemes and minimum-bid policies is important to the performance of keyword advertising platforms used by search engines.

We study the design of weighting schemes and minimum-bid policies from two perspectives: one that maximizes total expected valuation created (the efficient design) and one that maximizes the auctioneer’s expected revenue (the revenue-maximizing design). The efficient design maximizes the “total pie.” Such a design is most relevant at the developing stage of the keyword advertising market in which advertising providers are likely to attract advertisers by passing much of the valuation created to them. As the keyword advertising market becomes mature and market shares stabilize, advertising providers will more likely focus on profitability, thereby adopting a revenuemaximizing design.

Our study generates several important insights. We demonstrate that weighting schemes and differentiated minimum bid policies have a significant impact on equilibrium bidding. The weighting scheme determines how advertisers with different expected CTRs match in equilibrium—an advertiser with a low weighting factor compensates by bidding higher (than one with the same valuation-per-click but a higher weighting factor). Minimum bids exclude low-valuation advertisers and, when not equally constraining, can distort the equilibrium matching: some of the less-constrained advertisers will choose not to compete with their more-constrained competitors by bidding low. Despite these nontrivial equilibrium features, the efficient keyword auction design is remarkably simple: it weights advertisers’ unit-price bids with their expected CTRs and requires the same minimum weighted bid. This implies that one should rank advertisers as if they bid their true valuation, and set higher minimum bids for advertisers with lower expected CTRs. The revenue-maximizing design may generate higher revenue than standard fixed-payment auctions, but requires fine balancing between low- and high-CTR advertisers based on their expected CTRs and valuation-per-click distributions. Relative to the efficient weighting scheme, the revenue-maximizing weighting scheme may favor low- or high-CTR advertisers. In choosing revenuemaximizing minimum bids, advertising providers should consider the effect of excluding low-valuation advertisers as well as that of distorted allocations among advertisers with different expected CTRs.

The rest of the paper is organized as follows. In §2 we discuss the related literature. In §3 we lay out our research model. We examine weighting scheme design and differentiated minimum bids design in §4 and §5, respectively. We compare keyword auctions to standard fixed-payment auctions in §6. Section 7 discusses some extensions, and §8 concludes the paper.

## 2. Related Literature

How auctioneers should use available information has been an important area of investigation in the auction literature. The early literature focuses on ex post information. Riley (1988) finds that in common-value auctions, such as drilling-right auctions, auctioneers can increase their revenue by tying winners’ payment with the ex post information on the item’s value. McAfee and McMillan (1986) demonstrate that in procurement auctions, making contractors’ (bidders’) payment partially depend on their ex post realized costs can reduce the buyer’s procurement costs. This paper focuses on how auctioneers can use ex ante information on bidders’ outcome-generating potential.

This research is most related to research on “scoring auctions,” or auctions in which bidders are ranked by a score that summarizes multiple underlying attributes. Che (1993) and Asker and Cantillon (2008) study a form of scoring auction used in procurement settings, in which the score is a function of suppliers’ nonprice attributes (e.g., quality and time-tocompletion) minus the price they ask. Ewerhart and Fieseler (2003) study another form of scoring auction, in which a score is a weighted sum of unit-price bids for each input factor (e.g., labor and materials). All three papers show that scoring auctions, though inefficient, can generate higher revenues than efficient mechanisms such as fixed-payment first-price auctions. Keyword auctions in this paper are different from the above scoring auctions in auction rules, equilibrium bidding behavior, and application settings. For example, we study a multiplicative scoring rule that is different from other scoring auctions. The difference in scoring rules also leads to different equilibrium features (e.g., kinks and jumps in our setting). Another important difference is that equilibrium bidding in other scoring auctions is determined by a single parameter, whereas in our paper, equilibrium bidding is determined both by advertisers’ valuation-per-click and by their CTR signals. Besides scoring rules, we study differentiated minimum bid policies, which are not discussed in the aforementioned literature.

This paper is closely related to previous studies on ranking rules in keyword auctions. Recall that one approach ranks advertisers only by their unit prices, whereas the other approach ranks advertisers using the product of their unit prices and historical CTRs. Liu and Chen (2006) and Lahaie (2006) study the equilibrium bidding under the two approaches and show that the latter approach is efficient and that the revenues generated by the two approaches are ambiguously ranked. Liu and Chen (2006) study the revenue-maximizing design under a more general class of ranking rules with ranking-by-price and ranking-by-price <sub>×</sub> CTR as two special cases. They show that neither ranking-by-price nor ranking-byprice <sub>×</sub> CTR is revenue-maximizing. We extend Liu and Chen (2006) in several ways. First, this paper considers a general multislot setting, whereas Liu and Chen (2006) assume a single slot. Second, this paper allows valuation-per-click to be correlated with CTR signals. Third, for the first time in the literature, this paper studies the use of differentiated minimum bids, together with the weighted ranking rule, as a way of exploiting ex ante information on advertisers.

Several authors have looked at keyword auctions from different perspectives. Following the “auction of contracts” literature (McAfee and McMillan 1986, Samuelson 1986), a few authors (e.g., Sundararajan 2006) study whether advertisers should pay a fixed payment, a contingent payment, or a combination of the two. Weber and Zheng (2007) study a model of paid referrals in which firms can offer a “bribe” to the search engine in exchange for a higher position. They show that the revenue-maximizing design is a weighted average of the “bribe” and the quality of the product offered by each firm. Feng (2007) studies the optimal allocation of multiple slots when buyers’ valuation of slots decreases at different speeds. Edelman et al. (2007) and Varian (2007) examine equilibria of auctions with a “generalized second price” (GSP) payment rule, that is, that winners pay only the lowest price that keeps their positions. They study GSP auctions under a complete-information setting (that is, advertisers know each others’ valuation for slots).<sup>1</sup> Edelman et al. (2007) show that GSP auctions under a complete-information setting do not have a dominant-strategy equilibrium, and advertisers will not bid their true valuation. Both Edelman et al. (2007) and Varian (2007) show that GSP auctions admit a range of stable equilibria, and the auctioneer’s equilibrium revenue under the GSP rule is at least as high as that under the Vickrey-Clarke-Groves mechanism. Although their characterization of the equilibria under the GSP rule applies to both the rank-by-price case and the rank-by-price <sub>×</sub> CTR case, they do not study what ranking rules advertising providers should choose, nor do they study optimal minimum-bid policies. This paper complements theirs by examining how ranking rules and minimum-bid policies affect equilibrium bidding and how advertising providers should design such auction dimensions. Also, different from Edelman el al. (2007) and Varian (2007), we model keyword auctions as an incomplete-information game $( \mathrm { i . e . , }$ advertisers only know a distribution of other advertisers’ valuation and click-generating abilities). The real-world keyword auctions may lie between complete information and incomplete information. For example, Google does not publish advertisers’ bids whereas Yahoo! does with measures that prevent large-scale automatic harvesting of such information. In either case, advertisers may not know at every minute how much other advertisers value the slots.

## 3. Model Setup

We consider a problem of assigning m advertising slots associated with a keyword to $n \ ( n \geq m )$ riskneutral advertisers. Each advertiser has one advertisement for the keyword and can use only one slot. The number of clicks an advertisement can attract depends both on the quality of the advertisement and on the prominence of the slot the advertisement is assigned to. The quality of an advertisement is considered an attribute of the advertisement and may be determined by the relevance of the advertisement to the keyword, the attractiveness of the advertised product or service, and how well the advertisement is written. For example, for the keyword “refinance,” an advertisement from a more reputable lender may generate more clicks than one from a less reputable lender. The prominence of a slot is considered a slotspecific factor and may be determined by the position, size, shape, or media format (text, image, or video) of the slot. For example, an advertisement may attract more clicks when placed on the top of a page than when placed at the bottom of the page. In this light, we assume the number of clicks generated by an advertiser at slot j is $\delta _ { j } q . \delta _ { j }$ is a deterministic factor that we use to capture the prominence of slot $j .$ We assume $\delta _ { 1 } \geq \delta _ { 2 } \cdot \cdot \cdot \geq \delta _ { m } > 0$ and normalize $\delta _ { 1 } = 1$ q is a stochastic number that we use to capture the quality of the advertisement. We interpret q as the advertiser’s CTR in the sense that the higher the quality of the advertisement, the more likely a Web user will click on it. It is important to note that, in general, CTRs are subject to both the advertisement effect and the slot effect. In this paper, an advertiser’s CTR refers exclusively to the attractiveness of an advertisement, regardless of any slot effect.

Though an advertiser’s CTR is realized only after the auction, the advertiser and the auctioneer may have ex ante information about the advertiser’s future CTRs. This is because e-commerce technologies make it easy for advertising providers to track advertisers’ past CTRs and to make predictions about their future CTRs. We assume that the auctioneer can observe a signal about each advertiser’s future CTR; the same signal is observed by the advertiser but not by other advertisers. For simplicity, we assume that such signal allows the auctioneer to distinguish between two types of advertisers, those with high expected CTRs (h type) and those with low expected CTRs (l type). We will extend our model to a multiple CTR-type case in §7. Denote $Q _ { h }$ and $Q _ { l } \ ( Q _ { h } > Q _ { l } > 0 )$ as the expected CTRs for l- and h-type advertisers, respectively. We assume the probabilities for advertisers being h type and l type are  and $1 - \alpha ,$ respectively. These probabilities are common knowledge.

Each advertiser has a valuation v for each click, termed the advertiser’s valuation-per-click. Advertisers may differ in valuation-per-click. For example, for the keyword “refinance,” bankone.com may have a higher valuation-per-click than aggregate lender lendingtree.com. The distribution of the valuation-perclick may be correlated with the advertiser’s CTR signal such that l- and h-type advertisers may have different valuation-per-click distributions. For example, aggregate lenders (e.g., lendingtree.com) may have higher CTRs but lower valuation-per-click than banks (e.g., bankone.com) for the keyword “refinance.” Let $F _ { l } ( v )$ and $F _ { h } ( v )$ denote the cumulative distribution of valuation-per-click for l- and h-type advertisers, respectively. The realization of an advertiser’s valuation-per-click is not known by the auctioneer or other advertisers. But the distributions $F _ { h } ( v )$ and $F _ { l } ( v )$ are common knowledge.

We assume $F _ { l } ( v )$ and $F _ { h } ( v )$ have a fixed support 0 1, and the density functions, $f _ { l } ( v )$ and $f _ { h } ( v )$ , are positive and differentiable everywhere within the support. This assumption can be generalized to $[ \underline { { v } } _ { l } , \bar { v } _ { l } ]$ and $[ \underline { { v } } _ { h } , \bar { v } _ { h } ]$ for l- and h-type advertisers, respectively. We also assume that one advertiser’s valuationper-click and expected-CTR type are independent of another advertiser $\mathrm { ' s } . { } ^ { 2 }$

We assume advertisers’ payoff functions are additive in their total valuation and the payment. In particular, conditional on winning slot j, an advertiser’s payoff is

$$
v q \delta_ {j} - \text { payment }.\tag{1}
$$

Advertising slots are sold through a weighted unitprice auction, which we describe below. Each advertiser is asked to submit a b that is the advertiser’s willingness-to-pay per click, or unit price. The auctioneer assigns each advertiser a score based on the advertiser’s unit-price bid and CTR signal. The score for an advertiser is

$$
s = \left\{ \begin{array}{l l} b, & \text { if   the   advertiser   is   h   type }, \\ w b, & \text { if   the   advertiser   is   l   type }, \end{array} \right.\tag{2}
$$

where w is the weighting factor for l-type advertisers, and the weighting factor for h-type advertisers is normalized to one. The auctioneer allocates the first slot to the advertiser with the highest score, the second slot to the advertiser with the second highest score, and so on. Winners pay for their realized clicks at unit prices they bid.<sup>3</sup> We call such an auction format a weighted unit-price auction.

By allowing w to take different values, we can accommodate the following stylized auction formats. When w equals one, the winners are determined solely by the prices they bid. One example is Overture’s auction format. When w is less than one, bid prices from l-type advertisers are weighted less than those from h-type advertisers. Google’s auction fits in this category because under Google’s ranking policy, bids from advertisers with high click-generating potential are weighted more.

We also allow the auctioneer to set different minimum bids (or reserve prices) for advertisers with different CTR signals. In particular, we let $\underline b _ { l }$ and $\underline { { b } } _ { h }$ be the minimum bids for l- and h-type advertisers, respectively.

The auction proceeds as follows. First, the auctioneer announces weighting factors and minimum bids. All advertisers receive signals about their future CTRs and learn their valuation-per-click before the auction. Then, each advertiser submits a unit-price bid, and the auctioneer assigns advertisers to slots based on their unit-price bids and CTR signals according to the announced weighting scheme. Finally, the number of clicks is realized, and advertisers pay the realized clicks at the unit prices they bid.

## 4. Designing Weighting Scheme

We start by assuming no minimum bids so that we can focus on the design of the weighting scheme. We will first consider how weighting factors affect advertisers’ equilibrium bidding. Then, we will examine the efficient and revenue-maximizing weighting schemes.

4.1. Weighting Scheme and Equilibrium Bidding Throughout this paper, we consider a symmetric, pure-strategy Bayesian-Nash equilibrium. By “symmetric,” we mean that advertisers with the same valuation-per-click and CTR signal will bid the same.

Let $b _ { h } ( v )$ denote the equilibrium bidding function for h-type advertisers, and $b _ { l } ( v )$ for l-type advertisers. A bidding function in our setting is a function that associates advertisers’ unit-price bids with their valuation-per-click. Because advertisers differ both in valuation-per-click and in expected CTRs, we need a pair of bidding functions to describe our equilibrium. The condition for the pair to be an equilibrium is that an advertiser finds it is optimal to bid according to this pair if all other advertisers bid according to this pair. We conjecture that both bidding functions are strictly increasing (we verify this in the appendix). The following result is key to our analysis.

<sup>Lemma</sup> <sup>1.</sup> An l-type advertiser with valuation-per-click v matches an h-type advertiser with valuation-per-click wv in equilibrium. Formally,

$$
b _ {h} (w v) = w b _ {l} (v), \quad \forall v, w v \in [ 0, 1 ].\tag{3}
$$

<sup>Proof.</sup> All proofs are in the appendix. <sup></sup>

The intuition for Lemma 1 is as follows. Consider an h-type advertiser with valuation-per-click wv and an l-type advertiser with valuation-per-click v. If the former bids wb and the latter bids $b ,$ the two advertisers tie, and therefore their chances of winning each slot are the same. Meanwhile, conditional on winning the same slot, the l-type advertiser’s payoff $( Q _ { l } \delta _ { i } ( w v - w b ) )$ differs from the h-type advertiser’s $( Q _ { h } \dot { \delta } _ { j } ( v - b ) )$ ) only by a scalar. So their total expected payoffs differ only by a scalar, too. Because multiplying the objective of an optimization problem by a scalar does not change the solution to the problem, we conclude that if bidding b is optimal for the l-type advertiser then bidding wb must also be optimal for the h-type advertiser, and vice versa.

We call two advertisers comparable if they tie or match (in scores) in equilibrium without minimum bids. Lemma 1 greatly simplifies the derivation of advertisers’ equilibrium winning probabilities. Let us first consider an l-type advertiser’s winning probability against any advertiser, or the advertiser’s one-on-one winning probability, denoted as $G _ { l } ( v )$ . Lemma 1 suggests that an l-type advertiser with valuation-per-click v can beat another advertiser, say B, if and only if B is l type and has valuation-per-click less than $v ,$ or B is h type and has valuation-per-click less than wv. Hence,

$$
G _ {l} (v) = \alpha F _ {h} (w v) + (1 - \alpha) F _ {l} (v).\tag{4}
$$

Similarly, an h-type advertiser’s winning probability against any advertiser, $G _ { h } ( v )$ , is

$$
G _ {h} (v) = \alpha F _ {h} (v) + (1 - \alpha) F _ {l} (v / w).\tag{5}
$$

We denote $P _ { l } ^ { j } ( v )$ and $P _ { h } ^ { j } ( v )$ as l- and h-type advertisers’ probabilities of winning the jth slot, respectively. We can write $P _ { l } ^ { j } ( v )$ and $P _ { h } ^ { j } ( v )$ as

$$
P _ {\theta} ^ {j} (v) = \binom{n - 1}{n - j} G _ {\theta} (v) ^ {n - j} [ 1 - G _ {\theta} (v) ] ^ {j - 1}, \quad \theta \in \{l, h \}.\tag{6}
$$

Proposition 1. <sub>Given w</sub> $( w > 0 )$ , equilibrium bidding functions are given by

$$
\left\{ \begin{array}{l l} b _ {l} (v) = v - \frac {\int_ {0} ^ {v} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (t)   d t}{\sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (v)}, & \forall   v \in [ 0, 1 ], \\ b _ {h} (v) = v - \frac {\int_ {0} ^ {v} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (t)   d t}{\sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (v)}, & \forall   v \in [ 0, 1 ]. \end{array} \right.\tag{7}
$$

Proposition 1 characterizes the equilibrium for a weighted unit-price auction. In Figure 1, we plot advertisers’ equilibrium scores when l-type advertisers’ weighting factor is 0.5 and the valuation distributions are uniform. Recall that score is bid times weighting factor. We plot scores instead of unit-price bids because the former better illustrates the equilibrium matching between l- and h-type advertisers. Clearly, an l type with valuation-per-click 1 ties with an h type with valuation-per-click 05, and h-type advertisers with higher valuation have no comparable l-type advertisers.

Figure 1 Equilibrium Bidding Functions  
![](/api/attachments/H6SYGDDT/fulltext/images/1ea39931251b74f54371cefb3a54dd95836cd290cdc1ad084f4d8f9ba117994f.jpg)

Interestingly, the figure shows a kink in h-type advertisers’ equilibrium bidding function. Intuitively, this is because h-type advertisers with valuationper-click less than 05 compete with both l- and h-type advertisers, whereas h-type advertisers with valuation-per-click higher than 0.5 complete only with h-type advertisers. The sudden change in the number of competitors causes h-type advertisers with valuation-per-click higher than 0.5 to bid considerably less aggressively than h-type advertisers with valuation-per-click lower than 0.5, thus the kink. Generally speaking, when the weighting factor w for l-type advertisers is less than one, the h-type advertisers’ equilibrium bidding function has a kink at w. When w is greater than one, the l-type advertisers’ equilibrium bidding function has a kink at $1 / w . ^ { 4 }$ These kinks reflect the impact of weighting scheme on the equilibrium matching between l- and h-type advertisers.

Proposition 1 has the following implications. Advertisers who receive a high weighting factor are favored in equilibrium allocation, and can win more often with the same unit price. Some advertisers who receive a high weighting factor may out-compete all advertisers who receive a low weighting factor, and thus can benefit from such a situation by bidding less aggressively. Increasing l-type advertisers’ weighting factor causes the following effects. It increases l-type advertisers one-on-one winning probability and decreases h-type advertisers’ one-on-one winning probability (see (4) and (5)). Consequently, l-type advertisers are selected more often into high-ranked slots and have a larger total expected winning (defined as the expected value of the slot an advertiser may win, i.e., $\begin{array} { r } { \sum _ { j = 1 } ^ { m } \delta _ { j } P _ { \theta } ^ { j } ( v ) ) } \end{array}$ Meanwhile, it causes more h-type advertisers to bid aggressively because there are more h-type advertisers with valuation-per-click below w who face competition from both CTR-types.

## 4.2. Efficient Weighting Scheme

We measure the efficiency by the total value created. The efficiency criterion, therefore, emphasizes the “total pie,” which is important if the auctioneer’s objective is to transfer much of the value to advertisers in return for their participation. This is especially true when the keyword advertising market is still nascent, and online advertising providers are still trying to steal market share from the traditional advertising providers. The efficiency criterion may become the criterion of choice for advertising providers who aim at long-term development rather than short-term profits, regardless of their market positions.

We define the efficient weighting factor, $w _ { \mathrm { e f f } } ,$ as one that maximizes the total expected valuation. We focus on expected valuation (thus ex ante efficiency) because advertisers’ valuation for slots is also determined by the realized CTRs after the auction. The assignment of an advertiser with valuation-per-click v and CTR-signal  to slot j will generate an expected valuation of $v \delta _ { j } Q _ { \theta } , \theta \in \{ l , h \}$ . Given that the probability of assigning an advertiser to slot j is $P _ { \theta } ^ { j } ( v )$ , the total expected valuation generated by all advertisers is

$$
\begin{array}{c} W = n (1 - \alpha) Q _ {l} \int_ {0} ^ {1} v \sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (v) f _ {l} (v) d v \\ + n \alpha Q _ {h} \int_ {0} ^ {1} v \sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (v) f _ {h} (v) d v. \end{array}\tag{8}
$$

<sup>Proposition</sup> <sup>2.</sup> The efficient weighting factor ( for l-type advertisers) is $Q _ { l } / Q _ { h }$ .

Proposition 2 suggests that it is efficient to weight advertisers’ bids by their expected CTRs (note that the weighting factor pair $( Q _ { l } / Q _ { h } , 1 )$ is equivalent to the pair $( Q _ { l } , Q _ { h } ) )$ . Such a weighting scheme is also efficient if advertisers were to bid their true valuation. In other words, the auctioneer can achieve efficiency by weighting unit-price bids by expected CTRs as if advertisers are bidding their true valuation, despite that in our model advertisers generally do not bid their true valuation-per-click. The reason for this lies in the way l- and h-type advertisers are matched in equilibrium. According to Lemma 1, an l-type advertiser with valuation-per-click v is comparable with an h-type advertiser with valuation-per-click wv. The efficiency criterion requires comparable advertisers to generate the same expected valuation. Hence, the efficient weighting factor must be $Q _ { l } / Q _ { h }$

It is worth noting that the efficient weighting factor is independent of the distribution of valuationper-click and that of CTR types. This feature makes it straightforward to implement an efficient weighting scheme: the auctioneer only needs to estimate the expected CTR for each advertiser-keyword combination and use it to weight the advertiser’s unit-price bid. Given that keyword auctions have already been set up to accumulate CTR information for all advertisers and all keywords, it is possible to estimate an advertiser’s CTR on a particular keyword and that estimation can be perfected over time.

## 4.3. Revenue-Maximizing Weighting Scheme

Another useful design criterion is revenue-maximization. As the industry matures and the competition for market shares settles, an efficient design toward future growth becomes less appealing, and the auctioneer’s objective is likely to transform from maximizing the “total pie” to maximizing the total revenue from existing advertisers. Next, we examine how an auctioneer should choose the weighting factor to maximize the expected revenue.

We define the revenue-maximizing weighting factor, $w ^ { \ast } .$ , as one that maximizes the total expected revenue of the auctioneer. We can explicitly derive the auctioneer’s expected revenue (") as (see the appendix for details)

$$
\begin{array}{l} \pi = n (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (v) \left(v - \frac {1 - F _ {l} (v)}{f _ {l} (v)}\right) f _ {l} (v) d v \\ + n \alpha Q _ {h} \int_ {0} ^ {1} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (v) \left(v - \frac {1 - F _ {h} (v)}{f _ {h} (v)}\right) f _ {h} (v) d v. \end{array}\tag{9}
$$

In the above, the total expected revenue consists of the expected revenue from l-type advertisers (the first term) and the expected revenue from h-type advertisers (the second term). Recall that $P _ { l } ^ { j } ( v )$ is an l-type advertiser’s probability of winning the jth slot, and

$P _ { h } ^ { j } ( v )$ is an h-type advertiser’s probability. We interpret the terms

$$
Q _ {l} \left[ v - \frac {1 - F _ {l} (v)}{f _ {l} (v)} \right] \quad \text { and } \quad Q _ {h} \left[ v - \frac {1 - F _ {h} (v)}{f _ {h} (v)} \right]\tag{10}
$$

as l type’s and h type’s “revenue contribution” to the auctioneer if they are assigned to a standard slot $( \delta = 1 )$ , respectively. Revenue contribution refers to the revenue captured by the auctioneer, which is usually less than the total valuation created. The difference between advertisers’ revenue contribution and their valuation for slots is considered to be the informational rent kept by the advertisers. According to this interpretation, the total expected revenue can be viewed as the total expected revenue contribution of the winners at all slots. The concept of revenue contribution is closely related to the concept of “virtual valuation” introduced by Myerson (1981) in the optimal auction setting. One difference is that we consider revenue contribution across multiple slots, whereas Myerson (1981) studies a single object.

The revenue-maximizing weighting factor can be characterized by the first-order condition of the total expected revenue with respect to the weighting factor. Except in some special cases, the revenue-maximizing weighting factor cannot be expressed in an explicit form. Next, we focus on two issues regarding the revenue-maximizing weighting factor. First, how is it different from the efficient weighting factor? Second, how is it affected by the underlying model primitives, especially valuation-per-click distributions? We first consider a setting in which the valuation-per-click is independent of the CTR signal, so that the valuationper-click distributions for l- and h-type advertisers are the same (commonly denoted as $F ( v ) )$ ).

We say a distribution function F v is an increasinghazard-rate (IHR) distribution if its hazard rate $f ( v ) / ( 1 - F ( v ) )$ increases in v throughout the support. Many distributions, including uniform, normal, and exponential, are IHR.

<sup>Proposition</sup> <sup>3.</sup> If the valuation-per-click and CTR signals are independent, and $F ( v )$ is IHR, then the revenuemaximizing weighting factor $w ^ { * }$ must be higher than the efficient weighting factor $w _ { \mathrm { e f f } }$

Proposition 3 implies that when the distributions of valuation-per-click are the same across l- and h-type advertisers, the revenue-maximizing weighting factor is generally inefficient and discriminates against h-type advertisers relative to the efficient design. The intuition is as follows. For any weighting factor less than $w _ { \mathrm { e f f } } ,$ , if the valuation-per-click distribution is IHR,

$$
Q _ {l} \bigg [ v - \frac {1 - F (v)}{f (v)} \bigg ] > Q _ {h} \bigg [ w v - \frac {1 - F (w v)}{f (w v)} \bigg ],
$$

for all v

(11)

In other words, for any weighting factor less than $w _ { \mathrm { e f f } } ,$ the revenue contribution of an l-type advertiser is always higher than that of a comparable h-type advertiser. Thus, the auctioneer can always earn a higher revenue by raising w to allocate the slots more often to l-type advertisers.

When l- and h-type advertisers have different valuation-per-click distributions, however, the revenue-maximizing weighting factor may or may not be higher than the efficient weighting factor, as illustrated by the following example.

<sup>Example</sup> <sup>1.</sup> Assume there is only one slot and the valuation-per-click of l- and h-type advertisers are uniformly distributed on 0 z and 0 1, respectively. Let $\alpha = 0 . 5 , Q _ { l } = 0 . 5 , Q _ { h } = 1$ , and $n = 5$ . We can explicitly solve the revenue-maximizing weighting factor as $w ^ { * } = 1 / ( 0 . 6 z + 0 . 8 )$ , which is lower than $w _ { \mathrm { e f f } } = 0 . 5$ when $z > 2$ and higher than $w _ { \mathrm { e f f } }$ when $z < 2$

In the above example, when z increases, the valuation-per-click distribution of the l-type advertisers becomes less “tight.” As a result, they can claim more informational rent and contribute less to the total revenue. So the auctioneer should allocate the slots less often to them by lowering the weighting factor for l-type advertisers. When l-type advertisers valuation distribution is loose enough, the revenuemaximizing weighting factor can be less than the efficient weighting factor.

Example 1 highlights that it is not always best to discriminate against advertisers with high expected CTRs. This is fundamentally because advertisers’ revenue contribution is determined both by expected CTRs and valuation distributions. h-type advertisers do not necessarily contribute less to the total revenue than l-type advertisers who have the same total valuation for slots, especially when the former have “tighter” valuation distributions.

## 5. Designing Differentiated Minimum Bids

The optimal auction literature suggests that an optimal design often involves imposing minimum bids to exclude advertisers whose participation reduces the auctioneer’s revenue. In our setting, the auctioneer can impose differentiated minimum bids for l- and h-type advertisers because of the information on advertisers’ future CTRs.

We say a minimum bid for h-type advertisers is more constraining than that for l-type advertisers if the comparable h-type advertiser for the lowest participating l-type advertiser is excluded by the minimum bids. We similarly define the case of a more constraining minimum bid for l-type advertisers. A pair of minimum bids is equally constraining if neither bid is more constraining.

Next we will focus on the scenario in which the weighting factor for l-type advertisers is no higher than that for h-type advertisers (Assumption 1) and the minimum bid for h-type advertisers is equally or more constraining (Assumption 2). Analyses of other scenarios—where the weighting factor for l type is higher, the minimum bid for l type is more constraining, or both—are analogous. We also assume that the minimum bid for h-type advertisers is low enough such that at least some l-type advertisers have comparable participating h-type advertisers (Assumption 3). This assumption excludes a trivial case in which ltype advertisers and h-type advertisers each compete with advertisers of their own type. Formally, these assumptions are:

Assumption 1. $w \leq 1 .$

Assumption 2. <sub>w</sub> $\underline { { b } } _ { l } \le \underline { { b } } _ { h }$

Assumption 3. $\underline { { b } } _ { h } < w .$

As in $\ S 4 ,$ we first examine the impact of differentiated minimum bids on equilibrium bidding and then study the efficient and revenue-maximizing minimum bid design.

## 5.1. Minimum Bids and Equilibrium Bidding

We conjecture that a pure-strategy equilibrium exists. l-type advertisers’ equilibrium bidding function must satisfy two criteria: (a) the lowest participating l-type advertiser must have a valuation-per-click of $\underline b l$ and bid his or her true valuation-per-click, (b) the equilibrium bidding function must be strictly increasing. The criterion (a) is simply the consequence of minimum bids, and the criterion (b) is required by the incentive compatibility condition (see the online supplement for a proof<sup>5</sup>). The criteria for h-type advertisers are symmetric.

Because the minimum bid for h-type advertisers is more constraining, some low-valuation l-type advertisers cannot match any participating h-type advertiser in the equilibrium score. But l-type advertisers with high enough valuation-per-click can. We call the lowest valuation-per-click for l-type advertisers to match a participating h-type advertiser the matching point for l-type advertisers, denoted as $v _ { 0 } .$

If the matching point equals one, no l-type advertiser can match an h-type advertiser in equilibrium. We will focus on the more interesting case of the matching point less than one and assume the condition for that is satisfied (see Proposition 4 for such a condition).

Will l-type advertisers with valuation-per-click above the matching point match with their comparable h-type advertisers as in the case of no minimum bids? Lemma 2 shows that they do.

<sup>Lemma</sup> <sup>2.</sup> Under Assumptions 1–3, an l-type advertiser with valuation-per-click v above the matching point matches an h-type advertiser with valuation-per-click wv in equilibrium. Formally,

$$
b _ {h} (w v) = w b _ {l} (v), \quad \forall v > v _ {0}.\tag{12}
$$

The question remains: where is the matching point? One may conjecture that the matching point will be the valuation-per-click of the l-type advertiser who is comparable with the lowest participating h-type advertiser. However, we show that this may be not the case.

Remark 1 (Postponed Matching). <sub>If the mini-</sub> mum bid for h-type advertisers is more constraining, at least some low-valuation l-type advertisers will bid lower scores than their comparable h-type advertisers.

Suppose the opposite, that is, every l-type advertiser will match the comparable h-type advertiser in equilibrium whenever the latter is not excluded by minimum bids. The first l-type advertiser to have a comparable h-type advertiser is ${ \underline { { b } } _ { h } } / w .$ By definition, ${ \underline { { b } } _ { h } } / w$ is also the matching point. Because the h-type advertiser with valuation-per-click $\underline { { b } } _ { h }$ must bid the true valuation (by criterion (a)) and earn zero payoff, the l-type advertiser must also bid his or her true value (by Lemma 2) and earn zero payoff. However, this cannot be an equilibrium because the l-type advertiser can always earn a positive payoff by bidding less. This contradiction leads us to conclude that the matching point must be higher than ${ \underline { { b } } _ { h } } / w$ . In other words, l-type advertisers avoid matching their comparable h-type ones in equilibrium until their valuation-per-click is high enough.

Given that the minimum bids are not equally constraining, the two bidding functions cannot both be continuous. If both bidding functions were continuous, by the definition of the matching point, the l-type advertiser with valuation-per-click $v _ { 0 }$ must match the h-type advertiser with valuation-per-click $\underline { { b } } _ { h }$ in equilibrium scores and both must earn zero payoff. Our previous argument shows that this cannot be an equilibrium. The following proposition establishes the equilibrium bidding with minimum bids.

<sup>Proposition</sup> <sup>4.</sup> Under Assumptions 1–3, the equilibrium bidding functions are given by

$$
\begin{array}{c} b _ {\theta} (v) = v - \frac {\int_ {\underline {{b}} _ {\theta}} ^ {v} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {\theta} ^ {j} (t)   d t}{\sum_ {j = 1} ^ {m} \delta_ {j} P _ {\theta} ^ {j} (v)}, \\ \forall   v \in [ \underline {{b}} _ {\theta}, 1 ],   \theta \in \{l, h \}, \end{array}\tag{13}
$$

where $P _ { l } ^ { j } ( v )$ and $P _ { h } ^ { j } ( v )$ are defined in (6) and the one-onone winning probabilities for l- and h-type advertisers are now

$$
G _ {l} (v) = \left\{ \begin{array}{l l} \alpha F _ {h} (\underline {{b}} _ {h}) + (1 - \alpha) F _ {l} (v) & f o r v \in [ \underline {{b}} _ {l}, v _ {0}) \\ \alpha F _ {h} (w v) + (1 - \alpha) F _ {l} (v) & f o r v \in [ v _ {0}, 1 ], \end{array} \right.\tag{14}
$$

$$
G _ {h} (v) = \left\{ \begin{array}{l l} \alpha F _ {h} (v) + (1 - \alpha) F _ {l} (v _ {0}) & \text {for v\in[ b _{h} ,w v_{0})} \\ \alpha F _ {h} (v) + (1 - \alpha) F _ {l} \bigg (\frac {v}{w} \bigg) & \text {for v\in[ w v_{0} ,1]}. \end{array} \right.\tag{15}
$$

The matching point $v _ { 0 }$ is determined by

$$
w \int_ {\underline {{b}} _ {l}} ^ {v _ {0}} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (t) d t = \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (t) d t,\tag{16}
$$

Figure 2 Equilibrium Bidding Functions with Minimum Bids  
![](/api/attachments/H6SYGDDT/fulltext/images/8e26bb6ffdd7decf74254d5a81754bf6f4c11f59d6dd30466fc6bc6690d03dee.jpg)

when w $\begin{array} { r } { \int _ { \underline { { b } } _ { l } } ^ { 1 } \sum _ { j = 1 } ^ { m } \delta _ { j } P _ { l } ^ { j } ( t ) d t < \int _ { \underline { { b } } _ { h } } ^ { w } \sum _ { j = 1 } ^ { m } \delta _ { j } P _ { h } ^ { j } ( t ) d t , } \end{array}$ and is 1 otherwise.

Proposition 4 characterizes the equilibrium under a weighted unit-price auction with differentiated minimum bids. In Figure $^ { 2 , }$ we show an example of h-type advertisers facing a more constraining minimum bid. In this example, we let $m = 1 , n = 5 , \alpha = 0 . 5 , F _ { l } ( v ) =$ $F _ { h } ( v ) = v , w = 0 . 5 , \underline { { b } } _ { l } = 0 ,$ , and $\underline { { b } } _ { h } = 0 . 1$ . Figure 2 shows the equilibrium scores for l- and h-type advertisers.

From Figure 2, l-type advertisers with valuationper-click lower than the matching point (026) bid lower scores than any h-type advertisers. l-type advertisers with valuation-per-click above the matching point match with their comparable h-type advertisers (with valuation-per-click between 013 and 05). h-type advertisers with valuation-per-click higher than 05 beat any l-type advertisers. h-type advertisers with valuation-per-click lower than 013 bid higher scores than l-type advertisers below the matching point but bid lower than l-type advertisers above the matching point. As in §4, the kinks are explained by an abrupt increase/decrease in the number of competing advertisers: the first kink in h-type advertisers equilibrium bidding function is because l-type advertisers start matching h-type advertisers; the second is because l-type advertisers can no longer match h-type advertisers.

The example in Figure 2 confirms the “postponed matching” effect outlined in Remark 1. In this example, l-type advertisers with valuation-per-click between 0.2 and 0.26 are comparable with h-type advertisers with valuation-per-click between 0.1 and 0.13, but choose not to match the latter. Intuitively, the minimum bid forces h-type advertisers with low valuation-per-click to bid close to their true valuation. Their comparable l-type advertisers, who do not face such a constraint, have the option of bidding significantly lower than their true valuation, which leads to low winning probabilities but high per-click payoffs. Bidding low (and not matching their comparable h-type advertisers) is a dominant strategy for l-type advertisers until their valuation-per-click reaches the matching point.

The jump in l-type advertisers’ bidding function at the matching point confirms our earlier argument about discontinuity.<sup>6</sup> At the matching point, l-type advertisers’ bidding strategy changes from not matching h-type advertisers to matching them. The fact the two strategies require quite different unit-price bids explains the jump in the equilibrium bids.

Proposition 4 has several implications. First, minimum bids exclude low-valuation advertisers and force the participating ones, especially those whose valuation is close to the minimum bids, to bid aggressively. In the example, h-type advertisers between 01 and 013 bid higher than they would in the absence of minimum bids (dashed lines indicate their equilibrium scores without minimum bids). Second, if the minimum scores for two CTR-types are the same (in other words, the minimum bid for h-type advertisers is w times of that for l-type advertisers), two advertisers who would tie without minimum bids remain tying. This is also the reason we call such minimum bids equally constraining. Third, when minimum bids are not equally constraining, advertisers who face a less constraining minimum bid may be better off by choosing not to match their comparable advertisers who face a more constraining minimum bid, a strategy leading to lower winning odds but a higher perclick payoff. However, advertisers whose valuation is far above minimum bids will choose to match their comparable advertisers, even if the minimum bids are not equally constraining. This later finding is consistent with Google’s claim that their differentiated minimum-bids policy only affects a small percentage of advertisers.<sup>7</sup>

As we have mentioned earlier, the intuition in Proposition 4 carries over to other scenarios (h-type advertisers receive a lower weighting factor, the minimum bid for l-type advertisers is more constraining, or both). For example, when the minimum bid for l-type advertisers is more constraining, h-type advertisers will postpone matching their comparable l-type advertisers, and the jump will occur in h-type’s equilibrium bidding function.

## 5.2. Efficient Minimum Bids

We now consider the impact of minimum bids on allocation efficiency. We call a pair of equally constraining minimum bids a uniform minimum score policy because they result in identical minimum scores for l- and h-type advertisers. We say a keyword auction is weakly efficient if it allocates assets in a way that maximizes the total expected valuation of all participating advertisers. The notion of weak efficiency we use is similar to the one discussed by Mark Armstrong (2000). Weak efficiency is different from “strong” efficiency in that weak efficiency concerns the total valuation of participating bidders, whereas strong efficiency concerns the total valuation of all bidders and the auctioneer. Weak efficiency is a necessary condition for strong efficiency.

If the auctioneer uses a uniform minimum score policy, all participating l-type advertisers match their comparable h-type advertisers in equilibrium. Hence, if the weighting factor is $Q _ { l } / Q _ { h } ,$ the auction is still efficient according to the same argument in Proposition 2. In fact, such designs are also necessary for the auction to be weakly efficient.

<sup>Proposition</sup> <sup>5.</sup> A weighted unit-price auction is weakly efficient if and only if the auctioneer uses the efficient weighting factor and a uniform minimum score.

Proposition 5 provides a theoretical justification for using differentiated minimum bids. A uniform minimum-score rule implies that auctioneers should set high minimum unit prices for advertisers with low expected CTRs. This is consistent in principle with Google’s recently adopted differentiated minimumbid practices.

Once again, a uniform minimum-score policy is easy to implement because it does not require knowing the distribution of advertisers’ valuation-per-click. Proposition 5 shows that weighting advertisers’ unitprice bids by their expected CTRs, together with a simple uniform minimum-score rule, allows the auctioneer to achieve efficiency among participating advertisers.

## 5.3. Revenue-Maximizing Minimum Bids

In a manner similar to the one used in the derivation of (9), we can explicitly evaluate the expected revenue of the auctioneer with minimum bids:

$$
\pi = n (1 - \alpha) Q _ {l} \int_ {\underline {{b}} _ {l}} ^ {1} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {l} ^ {j} (v) \left(v - \frac {1 - F _ {l} (v)}{f _ {l} (v)}\right) f _ {l} (v) d v
$$

$$
+ n \alpha Q _ {h} \int_ {\underline {{b}} _ {h}} ^ {1} \sum_ {j = 1} ^ {m} \delta_ {j} P _ {h} ^ {j} (v) \left(v - \frac {1 - F _ {h} (v)}{f _ {h} (v)}\right) f _ {h} (v) d v.\tag{17}
$$

A pair of minimum bids is revenue-maximizing if this pair is chosen to maximize (17). In the appendix we characterize the revenue-maximizing minimum bid policy, using a set of first-order conditions. The revenue-maximizing minimum bid policy can be computed numerically. In general, when choosing the revenue-maximizing minimum bids, the auctioneer needs to consider both the exclusion effect and the distortion effect. The exclusion effect is well-known in the auction design literature. A minimum bid excludes advertisers whose valuation-per-click is lower than the minimum bid, and forces the remaining advertisers to bid higher than they would in the absence of such a minimum bid. The distortion effect is new, however. We have shown earlier that when the minimum bid for h-type advertisers is more constraining, some l-type advertisers will bid lower scores than their comparable h-type advertisers.

The condition for revenue-maximizing minimum bids in our setting is generally different from the “exclusion principle” in standard auctions. The exclusion principle requires that the revenue-maximizing minimum bid should be chosen to admit only the advertisers with positive revenue contribution. In our setting, this would require the revenue-maximizing minimum bids to satisfy, respectively,

$$
\underline {{{b}}} _ {l} - \frac {1 - F _ {l} (\underline {{{b}}} _ {l})}{f _ {l} (\underline {{{b}}} _ {l})} = 0 \quad \text { and } \quad \underline {{{b}}} _ {h} - \frac {1 - F _ {h} (\underline {{{b}}} _ {h})}{f _ {h} (\underline {{{b}}} _ {h})} = 0.\tag{18}
$$

The conditions in (18) are not revenue-maximizing in our setting, however. They ignore the fact that in our setting, minimum bids also cause a distortion effect that has revenue consequences.

The revenue-maximizing minimum bids generally do not have a uniform score either. Intuitively, when we restrict to a uniform minimum-score policy, the distortion effect does not exist. As a result, the revenue-maximizing minimum bid policy should simply exclude advertisers with a negative revenue contribution, that is, one that satisfies (18). However, the minimum bid pair determined by (18) seldom has a uniform minimum score. For example, if the valuation-per-click distributions for l- and h-type advertisers are the same, conditions in (18) lead to the same minimum bid for l- and h-type advertisers, implying different minimum scores for l- and h-type advertisers.

We summarize the previous observations in the following remark.

<sup>Remark</sup> <sup>2.</sup> The revenue-maximizing minimum bid policy is generally not a uniform minimum-score policy or one resulting from a traditional exclusion principle (as determined by (18)).

We conclude the aforementioned discussion with an example that illustrates how the revenue-maximizing minimum bids in our setting differ from a uniform minimum-score policy and from those recommended by the auction design literature. The following example also shows that the auctioneer can achieve a higher revenue with a revenue-maximizing minimum bid policy.

<sup>Example 2.</sup> Assume there are five advertisers and one slot. Let $\alpha = 0 . 5 , ~ Q _ { l } = 0 . 8 , ~ Q _ { h } = 1 , ~ w = 0 . 8 ,$ $F _ { h } ( v ) = v ,$ and $F _ { l } ( v ) = 2 v - v ^ { 2 }$ . We calculate the minimum bids and expected revenues under three policies: a revenue-maximizing uniform-score policy, a policy using the exclusion principle, and a revenuemaximizing policy (see Table 1).

Table 1 Comparison Between Different Minimum Bid Policies

<table><tr><td>Minimum bid policy</td><td> $(\underline{b}_l, \underline{b}_h)$ </td><td>Total expected revenue</td></tr><tr><td>Revenue-maximizing uniform score</td><td>(0.481, 0.385)</td><td>0.5211</td></tr><tr><td>Traditional exclusion principle</td><td>(0.333, 0.500)</td><td>0.5213</td></tr><tr><td>Revenue-maximizing</td><td>(0.334, 0.615)</td><td>0.5309</td></tr></table>

## 6. Comparison with Fixed-Payment Auctions

Given the results on the efficient and revenue-maximizing designs, we are now able to compare weighted unit-price auctions with traditional auction formats where bidders bid fixed payments. Note that in fixed-payment auctions, winners pay a fixed payment upfront, whereas in unit-price auctions, winners pay ex post based on realized outcomes. In this sense, advertisers bear less risk in unit-price auctions than in fixed-payment auctions. The risk-sharing feature of unit-price auctions is considered advantageous, for example, by McAfee and McMillan (1986) in the study of procurement auctions. Here we move beyond risksharing advantage and focus on comparing weighted unit-price auctions with fixed-payment auctions on allocation efficiency and revenue.

To make a fair comparison, we extend the standard fixed-payment auction to a multiobject setting. We define the generalized first-price auction as one satisfying the following conditions: (1) Advertisers bid their total willingness-to-pay b for the first slot. (2) Slots are assigned based on the ranking of bids. (3) If an advertiser wins the jth slot, he/she will pay $\delta _ { j } b$

Given our model setting, the probability of an advertiser’s expected total valuation for the first slot being less than x is

$$
\alpha F _ {h} \left(\frac {x}{Q _ {h}}\right) + (1 - \alpha) F _ {l} \left(\frac {x}{Q _ {l}}\right).\tag{19}
$$

When there is only one slot, the generalized firstprice auction reduces to a standard first-price auction in which advertisers’ valuation for the slot is distributed according to (19). Such a standard auction is known to be efficient. In fact, the generalized firstprice auction is also efficient. This is because, as in standard auctions, advertisers’ bids are monotonically increasing in their valuation (for the first slot) such that slots are allocated efficiently.

Recall that in efficient weighted unit-price auctions, an advertiser is assigned a slot if and only if the advertiser has the highest total valuation for the slot among those who have not been assigned a slot (Proposition 2). This implies that efficient weighted unit-price auctions allocate the same way as generalized first-price auctions and thus generate the same expected revenue to auctioneers. Thus, see the following proposition.

<sup>Proposition</sup> <sup>6.</sup> The efficient weighted unit-price auction achieves the same efficiency and expected revenue as a generalized first-price auction.

Because the efficient weighted unit-price auction generates the same expected revenue as the generalized first-price auctions (Proposition 6) and the revenue-maximizing weighted unit-price auction can generate more revenue than the efficient weighted unit-price auction (Proposition 3), we immediately have the following corollary.

<sup>Corollary</sup> <sup>1.</sup> Revenue-maximizing weighted unitprice auctions generate more revenue than generalized firstprice auctions.

According to the optimal mechanism design literature, the standard auctions (with an appropriately set reserve price) can achieve the highest revenue among all mechanisms in assigning a single-object setting. The Corollary 1 indicates, however, that weighted unit-price auctions can achieve even higher revenue. The reason lies in that weighted unit-price auctions allow the auctioneer to discriminate advertisers based on information about their expected CTRs, which is not considered in the standard mechanism design setting. Therefore, this corollary illustrates that ex ante information on bidders’ outcome-generating potential can be exploited to enhance the auctioneer’s revenue.

We shall note that Proposition 6 and Corollary 1 are obtained with the assumption that the auctioneer has the same information on advertisers future CTRs as advertisers themselves do. In keyword auctions, because advertising providers have full access to advertisers’ CTR history, we expect advertisers’ information advantage on future CTRs to be small, especially after advertisers have had a long enough history with the advertising provider. However, in other settings where auctioneers have substantially less information on bidders’ future outcomes than bidders themselves, fixed-payment auctions may achieve higher allocation efficiency and revenue than weighted unit-price auctions.

## 7. Discussion

In this section, we consider relaxing some of the model assumptions.

## 7.1. Quality of CTR Information

Given the importance of the information on advertisers’ future CTRs, a natural question is how the quality of such information affects our results, which we attempt to address here by perturbing the information quality. One way to do this is to assume that under perfect information, advertisers with high and low expected CTRs can be correctly categorized into h-type and l-type, whereas under imperfect information some of the advertisers may be miscategorized. Such miscategorization maintains the same overall expected CTR but causes the (unbiased) expected CTR for the h-type group to be lower and for the l-type group to be higher; more so as the information quality worsens. By this notion of information quality, we can say one information set (\$) is less informative than another (\$ ) if

$$
Q _ {l} ^ {\prime} \geq Q _ {l} \quad \text { and } \quad Q _ {h} ^ {\prime} \leq Q _ {h},\tag{20}
$$

where superscripts denote parameters under information set $\tau ^ { \prime } .$ . In the extreme case, when the CTR signal is completely uninformative, there is no difference between the expected CTRs of the h-type group and those of the l-type group.

Obviously, our results on equilibrium bidding hold under different information quality in the aforementioned sense. The efficient weighting factor for l-type advertisers is higher under lower quality information because of a smaller difference between h type’s and l type’s expected CTRs. The miscategorization may cause the advertising provider to allocate advertising slots to low valuation advertisers even though higher valuation ones are available, and thus there is a loss of efficiency. The total expected revenue is generally lower because of the decrease in the total valuation created. In sum, deterioration in the quality of information on advertisers’ future CTRs generally reduces the efficiency and the expected revenue of weighted unit-price auctions. The following example illustrates such results.

Table 2 Impact of Information Quality

<table><tr><td></td><td> $w_{\text{eff}}$ </td><td>Total expected valuation</td><td> $w^{*}$ </td><td>Total expected revenue</td></tr><tr><td>Perfect info</td><td>0.50</td><td>0.68</td><td>0.80</td><td>0.44</td></tr><tr><td>Imperfect info</td><td>0.63</td><td>0.63</td><td>0.85</td><td>0.43</td></tr></table>

<sup>Example</sup> <sup>3.</sup> Assume there is one slot, $n = 5 ,$ and $F _ { l } ( v ) = F _ { h } ( v ) = v$ (uniform distribution). Let $\alpha = 0 . 5 ,$ $Q _ { l } = 0 . 5 ,$ and $Q _ { h } = 1$ under perfect information, and $\alpha = 0 . 4 5 , ~ Q _ { l } = 0 . 5 9 1$ , and $Q _ { h } = 0 . 9 4 4$ under imperfect information (corresponding to 10% of low-CTR advertisers and 20% of high-CTR advertisers being mis-categorized). Table 2 summarizes the changes in efficiency and total expected revenue.

## 7.2. Multiple CTR-Types

The basic intuition of our main results holds for multiple signal types (see the online supplement for a formal analysis). Suppose there are k CTR-types, indexed by $\theta = 1 , 2 , \ldots , k ,$ and the weighting factor for a CTR-type  is $w _ { \theta } .$ . We can show, as in Lemma 1, that an advertiser with a CTR-type $\theta _ { 1 }$ and valuation-per-click v ties with an advertiser with a CTR-type $\theta _ { 2 }$ and valuation-per-click ${ w _ { \theta _ { 1 } } v / w _ { \theta _ { 2 } } }$ in equilibrium. We can obtain k equilibrium bidding functions in the same way as in Proposition 1, one for each type. Analogous to the two-type case, it is still efficient to weight advertisers’ bids by their expected CTRs and to impose a uniform score across different CTR-types. The revenue-maximizing weighting scheme and minimum bid policy are more complex in the multiple CTR-type case because of additional undetermined design parameters; but the basic intuition follows through. For example, the minimum bid policy remains different from a uniform-score policy and from a policy implied by the traditional exclusion principle.

## 8. Conclusion

Information technology gives us the ability to track online behaviors in unprecedented detail. For online advertising, this means that advertisers can monitor how many customers click on their advertisements and how many end up making a purchase. This ability not only enables new outcome-based pricing (also known as “pay-for-performance”) models but also allows advertising providers to accumulate information on advertisers’ outcome-generating potential. Within this context, we examine how information on advertisers’ CTRs can be used in the design of keyword auctions. We evaluate two ways of incorporating advertisers’ CTR information into the keyword auction design: by assigning different weighting factors for advertisers with different expected CTRs and by imposing different minimum bids for them. Edelman et al. (2007) and Varian (2007) note that equilibria under rank-by-price and rank-by-price <sub>×</sub> CTR rules would be different, but do not address the impact of different ranking rules on equilibrium outcome. This paper addresses this question, and also a more general question of how to choose ranking rules and minimum bid policies to best utilize the ex ante information on advertisers’ future CTRs. We study the impact of weighting schemes and differentiated minimum bid policies and how they should be configured to maximize allocation efficiency or total expected revenue.

Although we use pay-per-click keyword auctions as a specific context for our discussion, our model framework and implications can be applied to other outcome-based pricing settings such as pay-per-call and pay-per-purchase advertising auctions. The success of pay-per-click advertising on search engines has inspired innovations in other areas. For example, Google introduced keyword-auction-like mechanisms to television, online video, and mobile phone advertising. The intuition obtained in this paper can potentially apply to these application areas as well.

## 8.1. Managerial Implications

Our analysis has several implications. First, we gain insight on how weighting schemes and differentiated minimum bids affect equilibrium bidding. We demonstrate that the weighting scheme determines how advertisers with different expected CTRs match in equilibrium: a low-CTR advertiser ties in equilibrium with a high-CTR advertiser when the two have the same weighted valuation-per-click—that is, valuationper-click times the weighting factor. For example, if low-CTR advertisers receive a weighting factor of w, a low-CTR advertiser with valuation-per-click one matches a high-CTR advertiser with valuation-perclick w in equilibrium.

As in classic auctions, minimum bids exclude lowvaluation advertisers and force others, especially those whose valuation is near minimum bids, to bid closer to their true valuation. Minimum bids in our setting have other effects: When minimum bids are not equally constraining, they distort equilibrium matching between low- and high-CTR advertisers and cause a jump in the less-constrained type’s equilibrium bidding. Intuitively, the less-constrained type avoids competing with the more-constrained type, who bids ultra-aggressively because of minimum bids. But for advertisers with valuation wellabove the minimum bids, the less-constrained type matches the more-constrained type the same way as the no-minimum-bids case. The jump reflects a transition from avoiding matching to matching among the less-constrained advertisers. These insights, together with ones on the weighting schemes, help advertising providers understand the impact of their auction rules on advertisers. They also provide guidelines for advertisers on how to bid optimally.

Second, the efficient keyword auction design is remarkably simple. It involves weighting advertisers’ pay-per-click bids with their expected CTRs, and requires the same minimum score for all advertisers. The former implies lower weighting factors for advertisers with lower expected CTRs. The latter implies higher minimum bids for advertisers with lower expected CTRs. These appear to be consistent with designs used in practice. For example, Google has been using historical CTRs as weighting factors and requiring higher minimum bids for advertisers with low historical CTRs. As we have argued in §7, the quality of such estimation affects the level of efficiency that keyword auctions can achieve, thus, our results draw attention to the importance of estimating advertisers’ future CTRs. Keyword advertising providers may improve the quality of such estimation by acquiring additional information on advertisers future CTRs and refining their estimation techniques.

Third, we characterize the revenue-maximizing weighting scheme and minimum-bid policy. The revenue-maximizing weighting scheme may favor or disfavor low-CTR advertisers relative to the efficient weighting scheme. If low- and high-CTR advertisers have the same valuation-per-click distribution, advertising providers obtain the highest expected revenue by favoring low-CTR advertisers—the disadvantaged type. But if low-CTR advertisers have a less tight valuation distribution than high-CTR ones, the revenuemaximizing weighting scheme may favor low-CTR advertisers less, possibly even disfavoring them. Such results suggest that we cannot automatically assume that low-CTR advertisers should be favored in a revenue-maximizing design.

## 8.2. Relation to Other Research

This research may have implications for online procurement auctions, which have gained some acceptance in recent years (Snir and Hitt 2003). One of the challenges for online procurement auction designers is to incorporate non-price dimensions such as quality, delivery, and services into auction mechanisms (Beall et al. 2003). Weighted unit-price auctions may provide a framework to do that. Of course, further research is needed to account for special features in procurement settings, such as the cost associated with switching suppliers and the fact that suppliers may misrepresent their nonprice attributes.

Our research may also have implications for posted-schedule pricing of information goods and services. A variety of information goods and services such as radio spectrum, network bandwidth, and Internet cache are resources allocated for exclusive use, the use of which may generate trackable outcomes (e.g., number of packets transmitted). Information system researchers have proposed several ways to price these resources (Bapna et al. 2005, Hosanager et al. 2005, Sundararajan 2004). For example, Sundararajan (2004) suggests a nonlinear price schedule that includes a fixed fee and a usage-based fee. Our results may add a new direction for pricing these goods and services, that is, to charge buyers by realized outcomes (such as usage) and differentiate pricing schedules for buyers with different outcomegenerating potential (such as usage rates). It will be interesting to compare such an approach to existing ones in the optimal pricing literature.

## 8.3. Limitations and Future Research

This research has certain limitations. We consider CTRs as endowed attributes, whereas in reality, advertisers may manipulate their CTRs to gain favorable weighting factors. If the manipulation permanently improves an advertiser’s CTR (such as by improving the presentation of the advertisement), then our results apply to the postmanipulation periods. Advertising providers may want to encourage such “manipulation.” On the other hand, manipulation that temporarily inflates an advertiser’s CTR may be discouraged by a carefully structured CTRestimation method. For example, manipulation that lasts one period does not have much impact on the weighting factor in a weighting system that emphasizes long-term CTR history. However, coping with various forms of manipulation remains an open issue in keyword auction designs.

Several other issues may be interesting for future research. First, it is not entirely clear whether keyword auctions perform better than alterative mechanisms such as posted-price. A commonly accepted argument holds that auctions are more suitable than posted-price when bidders’ valuation for goods and services is more uncertain (Pinker et al. 2003). This appears to be a plausible explanation for the popularity of auctions in selling keyword advertising slots, given sellers’ lack of knowledge on the potential value of keyword advertising slots. Second, an important issue related to this study is how to estimate advertisers’ future CTRs. Third, it would be interesting to examine how competition from other keyword advertising providers affects the efficient and revenue-maximizing designs.

## Acknowledgments

The authors thank Thomas Wiseman, Ajay Mehra, Mark Liu, the anonymous referees, the associate editor, and the senior editor for their generous input to this manuscript. The authors also thank participants at the Second Workshop on Sponsored Search Auctions (2006) and the Workshop on Information Systems and Economics (2006), as well as seminar participants at Google, Purdue University, Hong Kong University of Science and Technology, National University of Singapore, Carnegie Mellon University, University of Calgary, University of Maryland Baltimore County, University of Texas at Austin, and University of Kentucky. Jianqing Chen is the corresponding author.

## Appendix

Throughout the appendix, we denote

$$
\rho_ {\theta} (v) \equiv \sum_ {j = 1} ^ {m} P _ {\theta} ^ {j} (v) \delta_ {j}.\tag{21}
$$

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>1.</sup> Consider an h-type advertiser with valuation-per-click wv who bids wb and an l-type advertiser with v who bids b. Both advertisers get a score wb, and their payoff functions are

$$
U _ {l} (v, b) = Q _ {l} (v - b) \sum_ {j = 1} ^ {m} \delta_ {j} \operatorname * {P r} (w b \text {   ranks   } j \text { th }),\tag{22}
$$

$$
U _ {h} (w v, w b) = Q _ {h} (w v - w b) \sum_ {j = 1} ^ {m} \delta_ {j} \operatorname * {P r} (w b \text {   ranks   } j \text { th }).\tag{23}
$$

It is easy to establish that

$$
U _ {h} (w v, w b) = \frac {w Q _ {h}}{Q _ {l}} U _ {l} (v, b).\tag{24}
$$

For $b _ { l } ( v )$ and $b _ { h } ( v )$ to be equilibrium bidding functions, at any $v , b _ { l } ( v )$ must maximize $U _ { l } ( v , b )$ and $b _ { h } ( v )$ must maximize $U _ { h } ( v , b ) . { \sf S o } , ( 2 4 )$ suggests that if bidding b is the best for an l-type advertiser with valuation-per-click $v ,$ bidding wb must be the best for an h-type advertiser with valuationper-click wv, which implies $b _ { h } \vert$ wv equals $w b _ { l } ( v )$

Proof of the Revenue Equivalence Between First- and Second-Score Weighted Unit-Price Auctions. First, we show that the same relationship as in (3) holds between land h-type advertisers’ bidding functions under the secondscore setting. To see, we denote $s _ { j : n - 1 }$ as the random variable for jth highest score among $n - 1$ advertisers in equilibrium. Consider an h-type advertiser with valuation-per-click wv bidding wb and an l-type advertiser with valuation-perclick v bidding b. So both advertisers get a score $s = w b$

$$
\begin{array}{l} U _ {h} (w v, w b) \\ = Q _ {h} \left[ \sum_ {j = 1} ^ {m} \delta_ {j} \operatorname * {P r} (w b \text {   ranks   } j \text {th}) (w v - E [ s _ {j: n - 1} | s _ {j: n - 1} \leq s <   s _ {j - 1: n - 1} ]) \right] \end{array}
$$

and

$$
\begin{array}{l} U _ {l} (v, b) \\ = Q _ {l} \bigg [ \sum_ {j = 1} ^ {m} \delta_ {j} \operatorname * {P r} (w b \text {   ranks   } j \text { th }) \bigg (v - \frac {1}{w} E [ s _ {j: n - 1} | s _ {j: n - 1} \leq s <   s _ {j - 1: n - 1} ] \bigg) \bigg ]. \end{array}
$$

Similar to the proof of Lemma $^ { 1 , }$ we have $U _ { h } ( w v , w b ) =$ $( w Q _ { h } / Q _ { l } ) U _ { l } ( v , \bar { b } )$ and $b _ { h } ( w v ) = w b _ { l } ( v ) . b _ { h } ( w v ) = w b _ { l } ( v )$ implies the l-type advertiser with valuation-per-click v and the h-type advertiser with wv will tie in both first- and second-score weighted unit-price auctions. Therefore, firstand second-score weighted unit-price auctions allocate the slots in the same way. By the revenue equivalence theorem (e.g., Proposition 14.1 in Krishna 2002), the two formats must generate the same amount of revenue.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>1.</sup> Denote the inverse bidding functions as $b _ { l } ^ { - 1 } ( b )$ and $b _ { h } ^ { - 1 } ( b )$ , respectively, which are strictly increasing given the monotonicity of the bidding functions. Lemma 1 implies that $b _ { h } ^ { - 1 } \bar { ( } w b ) = w b _ { l } ^ { - 1 } ( b )$ for $\bar { b } \in [ 0 , b _ { l } ( 1 ) ]$ . Substituting this into (22) and (23), we can uniformly write the payoff functions as $U _ { \theta } ( v , b ) =$

$Q _ { \theta } ( v \mathbin { - } b ) \rho _ { \theta } ( b _ { \theta } ^ { - 1 } ( b ) )$ , where $\rho _ { \theta } ( v )$ is defined in (21). We denote

$$
V _ {\theta} (v) \equiv U _ {\theta} (v, b _ {\theta} (v)) = Q _ {\theta} (v - b _ {\theta} (v)) \rho_ {\theta} (b _ {\theta} ^ {- 1} (b _ {\theta} (v)))\tag{25}
$$

as the equilibrium payoff of an advertiser with valuationper-click v.

$$
\begin{array}{c} \frac {d V _ {\theta} (v)}{d v} = \frac {\partial U _ {\theta} (v , b _ {\theta} (v))}{\partial v} + \frac {\partial U _ {\theta} (v , b _ {\theta} (v))}{\partial b} \frac {d b _ {\theta} (v)}{d v} \\ = \frac {\partial U _ {\theta} (v , b _ {\theta} (v))}{\partial v} = Q _ {\theta} \rho_ {\theta} (v), \end{array}
$$

where the second equality is due to $\partial U _ { \theta } ( v , b _ { \theta } ( v ) ) / \partial b = 0$ (the first-order condition). Applying the boundary condition $V _ { \theta } ( 0 ) = 0$ , we get

$$
V _ {\theta} (v) = Q _ {\theta} \int_ {0} ^ {v} \rho_ {\theta} (t) d t.\tag{26}
$$

Combining (25) (note $b _ { \theta } ^ { - 1 } ( b _ { \theta } ( v ) ) = v )$ and (26), we can solve the equilibrium bidding function as $b _ { \theta } ( v ) = v \ -$ $\textstyle \int _ { 0 } ^ { v } \rho _ { \theta } ( t ) d t / \rho _ { \theta } { \overline { { \left( v \right) } } }$

Now we show that $d b _ { \theta } ( v ) / d v > 0$ . Note that $d b _ { \theta } ( v ) / d v =$ $\begin{array} { r l r } { \rho _ { \theta } ^ { \prime } ( v ) \int _ { 0 } ^ { v } \rho _ { \theta } ( t ) d t / \rho _ { \theta } ^ { 2 } ( v ) } \end{array}$ . The sign of $d b _ { \theta } ( v ) / d v$ is solely determined by that of $\rho _ { \theta } ^ { \prime } ( v )$ . It is sufficient to show $\rho _ { \theta } ^ { \prime } ( v ) > 0 ,$ , or $\begin{array} { r } { \sum _ { j = 1 } ^ { m } \delta _ { j } P _ { \theta } ^ { \ j \prime } ( v ) > 0 . } \end{array}$

$$
\begin{array}{c} P _ {\theta} ^ {j \prime} (v) = \binom {n - 1} {n - j} G _ {\theta} (v) ^ {n - j - 1} (1 - G _ {\theta} (v)) ^ {j - 2} \\ \cdot [ (n - j) - (n - 1) G _ {\theta} (v) ] G _ {\theta} ^ {\prime} (v). \end{array}\tag{27}
$$

Notice that $P _ { \theta } ^ { 1 \prime } ( v ) \geq 0$ and $P _ { \theta } ^ { n \prime } ( v ) \leq 0$ for all v $; P _ { \theta } ^ { j \prime } ( v ) \ ( 1 <$ $j < n )$ crosses 0 only once from positive to negative on $( 0 , 1 )$ . The crossing point, $v _ { j } ^ { c } ,$ , is the solution to $G _ { \theta } ( v _ { i } ^ { c } ) =$ $( n - j ) / ( n - 1 )$ . It is clear that $0 < v _ { n - 1 } ^ { c } < \cdots < v _ { 3 } ^ { c } < v _ { 2 } ^ { c } < 1$ Thus, for a given $v \in ( 0 , 1 )$ , there exists $j _ { v } \in \{ 1 , 2 , \dotsc , n - 1 \}$ such that

$$
\begin{array}{l l} P _ {\theta} ^ {j \prime} (v) > 0, & \text {for j = 1,\ldots,j_{v} , and} \\ P _ {\theta} ^ {j \prime} (v) \leq 0, & \text {for j = j_{v} +1,\ldots,n.} \end{array}\tag{28}
$$

Let $\delta _ { m + 1 } = \delta _ { m + 2 } = \cdot \cdot \cdot = \delta _ { n } = 0$ . We have $\begin{array} { r l } { \sum _ { j = 1 } ^ { m } \delta _ { j } P _ { \theta } ^ { j \prime } ( v ) = } & { { } } \end{array}$ $\begin{array} { r } { \sum _ { i = 1 } ^ { n } \delta _ { j } P _ { \theta } ^ { j \prime } ( v ) > \delta _ { j _ { v } } \sum _ { i = 1 } ^ { n } P _ { \theta } ^ { j \prime } ( v ) = 0 , } \end{array}$ , where the inequality is due to $\delta _ { 1 } \geq \delta _ { 2 } \geq \cdots \geq \delta _ { n }$ and (28), and the last equality is due to the fact that $\begin{array} { r } { \sum _ { i = 1 } ^ { n } P _ { \theta } ^ { j } ( v ) = ( G _ { \theta } ( v ) + 1 - G _ { \theta } ( v ) ) ^ { n - 1 } = 1 } \end{array}$

Proof of Proposition 2. <sub>First note that</sub> $G _ { h } ( w v ) =$ $G _ { l } ( v )$ and $d G _ { h } ( v ) / d w | _ { w v } = - ( ( 1 - \alpha ) / \alpha w ) ( f _ { l } ( v ) / f _ { h } ( w v ) )$ $( d G _ { l } ( v ) / d w )$ . We can establish

$$
\left. \frac {d \rho_ {h} (v)}{d w} \right| _ {w v} = - \frac {1 - \alpha}{\alpha w} \frac {f _ {l} (v)}{f _ {h} (w v)} \frac {d \rho_ {l} (v)}{d w}.\tag{29}
$$

Using the same technique in Proof of Proposition 1, we can show $d \rho _ { l } ( v ) / d w > 0$ . Taking the first-order derivative of (8) with respect to w yields

$$
(1 - \alpha) Q _ {l} \int_ {0} ^ {1} v \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) d v + \alpha Q _ {h} \int_ {0} ^ {1} v \frac {d \rho_ {h} (v)}{d w} f _ {h} (v) d v.\tag{30}
$$

If $w \leq 1$ , noting $d \rho _ { h } ( v ) / d w = 0$ for $v > w ,$ we can reorganize (30) as

$$
\begin{array}{l} (1 - \alpha) Q _ {l} \int_ {0} ^ {1} v \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) d v + \alpha Q _ {h} \int_ {0} ^ {w} v \frac {d \rho_ {h} (v)}{d w} f _ {h} (v) d v \\ = (1 - \alpha) Q _ {l} \int_ {0} ^ {1} v \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) d v \\ - (1 - \alpha) w Q _ {h} \int_ {0} ^ {1} v \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) d v \\ = (1 - \alpha) (Q _ {l} - w Q _ {h}) \int_ {0} ^ {1} v \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) d v, \end{array} \tag {31}\tag{31}
$$

where the second equality is due to integration by substitution and (29). Because $d \rho _ { l } ( v ) / d w > 0 ,$ , the above firstorder derivative is positive if $w < Q _ { l } / Q _ { h }$ and negative if $w > Q _ { l } / Q _ { h }$ . So $w = Q _ { l } / Q _ { h }$ maximizes the social welfare among all $v \in [ 0 , 1 ]$

By a similar logic, we can verify $w > 1$ cannot maximize the social welfare. So, $w _ { \mathrm { e f f } } = Q _ { l } / Q _ { h }$ .

Derivation of Expected Revenue. The expected payment from an advertiser is equal to the advertiser’s total expected valuation upon winning minus the advertiser’s expected payoff:

$$
Q _ {\theta} v \rho_ {\theta} (v) - V _ {\theta} (v) = Q _ {\theta} \left[ v \rho_ {\theta} (v) - \int_ {0} ^ {v} \rho_ {\theta} (t) d t \right],\tag{32}
$$

where the equality is due to (26).

The expected payment from one advertiser (with probability  being h-type and with probability $( 1 - \alpha )$ being $\scriptstyle l - { \mathrm { t y p e } } )$ is

$$
\begin{array}{l} \alpha E [ Q _ {h} v \rho_ {h} (v) - V _ {h} (v) ] + (1 - \alpha) E [ Q _ {l} v \rho_ {l} (v) - V _ {l} (v) ] \\ = \alpha Q _ {h} \int_ {0} ^ {1} \bigg [ v \rho_ {h} (v) - \int_ {0} ^ {v} \rho_ {h} (t) d t \bigg ] f _ {h} (v) d v \\ \qquad + (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \bigg [ v \rho_ {l} (v) - \int_ {0} ^ {v} \rho_ {l} (t) d t \bigg ] f _ {l} (v) d v \\ = \alpha Q _ {h} \int_ {0} ^ {1} \rho_ {h} (v) \bigg [ v - \frac {1 - F _ {h} (v)}{f _ {h} (v)} \bigg ] f _ {h} (v) d v \\ \qquad + (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \rho_ {l} (v) \bigg [ v - \frac {1 - F _ {l} (v)}{f _ {l} (v)} \bigg ] f _ {l} (v) d v. \end{array}
$$

The total expected revenue from all advertisers is n times the aforementioned.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>3.</sup> Taking the first order derivative of the expected revenue (9) with respect to w yields

$$
\begin{array}{l} \frac {d \pi}{d w} = (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} \bigg (v - \frac {1 - F _ {l} (v)}{f _ {l} (v)} \bigg) f _ {l} (v) d v \\ \qquad + \alpha Q _ {h} \int_ {0} ^ {1} \frac {d \rho_ {h} (v)}{d w} \bigg (v - \frac {1 - F _ {h} (v)}{f _ {h} (v)} \bigg) f _ {h} (v) d v. \end{array}
$$

We only need to check the sign of d"/dw for $0 < w \leq$ $Q _ { l } / Q _ { h }$ . For $0 < w \leq Q _ { l } / Q _ { h }$

$$
\begin{array}{l} \frac {d \pi}{d w} = (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} \left(v - \frac {1 - F _ {l} (v)}{f _ {l} (v)}\right) f _ {l} (v) d v \\ \quad + \alpha Q _ {h} \int_ {0} ^ {w} \frac {d \rho_ {h} (v)}{d w} \left(v - \frac {1 - F _ {h} (v)}{f _ {h} (v)}\right) f _ {h} (v) d v \\ = (1 - \alpha) Q _ {l} \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} \left(v - \frac {1 - F _ {l} (v)}{f _ {l} (v)}\right) f _ {l} (v) d v \\ \quad - (1 - \alpha) Q _ {h} \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} \left(w v - \frac {1 - F _ {h} (w v)}{f _ {h} (w v)}\right) f _ {l} (v) d v \\ = (1 - \alpha) \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) \left[ Q _ {l} \left(v - \frac {1 - F _ {l} (v)}{f _ {l} (v)}\right) - Q _ {h} \left(w v - \frac {1 - F _ {h} (w v)}{f _ {h} (w v)}\right) \right] d v \\ = (1 - \alpha) \int_ {0} ^ {1} \frac {d \rho_ {l} (v)}{d w} f _ {l} (v) \left[ v (Q _ {l} - Q _ {h} w) + Q _ {h} \frac {1 - F _ {h} (w v)}{f _ {h} (w v)} - Q _ {l} \frac {1 - F _ {l} (v)}{f _ {l} (v)} \right] d v, \end{array}\tag{33}
$$

(34)

where the first equality is because for $v > w , d \rho _ { h } ( v ) / d w = 0$ and the second equality is due to (29).

Note that $d \rho _ { l } ( v ) / d w > 0$ by the proof of Proposition 2. Clearly, for $0 ~ < ~ w ~ \leq ~ Q _ { l } / Q _ { h }$ $v ( Q _ { l } \ - \ Q _ { h } w ) \ \geq \ 0 .$ . By the IHR property (note that $F _ { l } ( \cdot ) ~ = ~ F _ { h } ( \cdot ) ~ = ~ F ( \cdot ) ) .$ $Q _ { h } ( ( 1 - F _ { h } ( w v ) ) / f _ { h } ( w v ) ) - Q _ { l } ( ( 1 - F _ { l } ( v ) ) / f _ { l } ( v ) ) > 0 . \mathrm { ~ S o } ,$ , (34) is greater than 0, which implies $w ^ { * } > Q _ { l } / Q _ { h }$

<sup>Proof</sup> <sup>for</sup> <sup>Lemma</sup> <sup>2.</sup> We suppose there exists a mapping $\Lambda \colon ( v _ { 0 } , 1 ] \to [ \underline { { b } } _ { h } , 1 ]$ such that $w b _ { l } ( v ) = b _ { h } ( \Lambda ( v ) )$ . That is, an l-type advertiser with v will tie with an h-type advertiser $\Lambda ( v )$ in equilibrium. Similarly, we define $P _ { \theta } ^ { j } ( v ) \equiv$ ${ \binom { n - 1 } { n - j } } [ G _ { \theta } ( v ) ] ^ { n - j } [ 1 - G _ { \theta } ( v ) ] ^ { j - 1 }$ and $\begin{array} { r } { \rho _ { \theta } ( v ) \equiv \sum _ { j = 1 } ^ { m } P _ { \theta } ^ { j } ( v ) \delta _ { j } , \theta \in } \end{array}$ $\{ l , \dot { h } \}$ , where

$$
\begin{array}{c} G _ {l} (v) = [ (1 - \alpha) F _ {l} (v) + \alpha F _ {h} (\Lambda (v)) ], \quad \text {for all} 1 \geq v > v _ {0}, \\ G _ {h} (v) = [ (1 - \alpha) F _ {l} (\Lambda^ {- 1} (v)) + \alpha F _ {h} (v) ], \quad \text {for all} \Lambda (1) \geq v > \Lambda (v _ {0}). \end{array}
$$

We can then solve the equilibrium bidding for each advertiser type as

$$
\begin{array}{c} b _ {l} (v) = v - \frac {U _ {l} ^ {0} / Q _ {l} + \int_ {v _ {0}} ^ {v} \rho_ {l} (t) d t}{\rho_ {l} (v)}, \\ b _ {h} (v) = v - \frac {U _ {h} ^ {0} / Q _ {h} + \int_ {\Lambda (v _ {0})} ^ {v} \rho_ {h} (t) d t}{\rho_ {h} (v)}, \end{array}\tag{35}
$$

(36)

where $U _ { l } ^ { 0 }$ and $U _ { h } ^ { 0 }$ are equilibrium payoff of an l-type advertiser with valuation-per-click $v _ { 0 }$ and equilibrium payoff of an h-type advertiser with valuation-per-click $\Lambda ( v _ { 0 } ) .$ , respectively. By $w b _ { l } ( v ) = b _ { h } ( \Lambda ( v ) )$ ,

$$
\begin{array}{l} w \bigg [ v - \frac {U _ {l} ^ {0} / Q _ {l} + \int_ {v _ {0}} ^ {v} \rho_ {l} (t) d t}{\rho_ {l} (v)} \bigg ] \\ = \Lambda (v) - \frac {U _ {h} ^ {0} / Q _ {h} + \int_ {\Lambda (v _ {0})} ^ {\Lambda (v)} \rho_ {h} (t) d t}{\rho_ {h} (\Lambda (v))} \\ = \Lambda (v) - \frac {U _ {h} ^ {0} / Q _ {h} + \int_ {v _ {0}} ^ {v} \rho_ {l} (t) \Lambda^ {\prime} (t) d t}{\rho_ {l} (v)}, \end{array}\tag{37}
$$

where the second step is due to $\rho _ { l } ( v ) = \rho _ { h } ( \Lambda ( v ) )$ . Multiplying both sides of $( 3 7 )$ by $\rho _ { l } ( v )$ and taking the first-order derivative with respect to $v ,$ we have w $\begin{array} { r l r } { \mathrm { \nabla } \eta \boldsymbol { \rho } _ { l } ^ { \prime } + \boldsymbol { \rho } _ { l } - \boldsymbol { \rho } _ { l } \big ] = } \end{array}$ $\Lambda ^ { \prime } \rho _ { l } + \rho _ { l } ^ { \prime } \Lambda - \rho _ { l } \Lambda ^ { \prime } ,$ which implies $\Lambda ( v ) = w v .$

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>4.</sup> Our analysis in §5.1 implies that an l-type advertiser with $v \in [ \underline { { b } } _ { h } , v _ { 0 } )$ participates but cannot compete with any participating h-type advertisers. The probability for such an l-type advertiser to beat any other advertiser is $G _ { l } ( v ) = \alpha F _ { h } \dot { ( } \bar { b } _ { h } ) + ( 1 - \alpha ) F _ { l } ( v )$ For an l-type advertiser with $\boldsymbol { v } \in \left[ v _ { 0 } , 1 \right]$ (who competes with both l-type advertisers and h-type advertisers), $G _ { l } ( v ) = \alpha F _ { h } ( w v ) + ( 1 - \alpha ) F _ { l } ( v )$ . Similarly, we can obtain the probability of beating any other advertiser for h-type advertisers with valuation-per-click in $\left[ \underline { { b } } _ { h } , w v _ { 0 } \right]$ (who beat any l-type advertisers in $[ \underline { { \bar { b } } } _ { h } , v _ { 0 } )$ but none of the l-type advertisers in $[ v _ { 0 } , 1 ] )$ , in $[ w v _ { 0 } , w ]$ (who compete both with h-type advertisers and l-type advertisers), and in $( w , 1 ]$ (who beat any l-type advertisers). The equilibrium winning and the equilibrium bidding functions follow naturally. The only undetermined variable is $v _ { 0 } .$ Notice that Lemma 2 implies for any $v \in \left[ v _ { 0 } , 1 \right]$

$$
\begin{array}{c} V _ {h} (w v) = Q _ {h} (w v - b _ {h} (w v)) \rho_ {h} (w v) \\ = Q _ {h} w (v - b _ {l} (v)) \rho_ {l} (v) = \frac {w Q _ {h}}{Q _ {l}} V _ {l} (v). \end{array}\tag{38}
$$

Meanwhile, we have (by a similar process in the proof of Proposition 1)

$$
\begin{array}{l} V _ {l} (v _ {0}) = Q _ {l} \int_ {\underline {{b}} _ {l}} ^ {v _ {0}} \rho_ {l} (t)   d t \quad \text { and } \\ V _ {h} (w v _ {0}) = Q _ {h} \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \rho_ {h} (t)   d t. \end{array}\tag{39}
$$

Evaluating (38) at $v = v _ { 0 }$ and substituting (39) into (38), we immediately have w $\begin{array} { r } { \int _ { b _ { I } } ^ { v _ { 0 } } \rho _ { l } ( t ) d t = \int _ { b _ { h } } ^ { w \tilde { v _ { 0 } } } \rho _ { h } ( t ) d t , } \end{array}$ , which determines $v _ { 0 } .$ We can verify that the bidding strategies obtained in the aforementioned process constitute an equilibrium.

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>5.</sup> In the following proof, we only consider the nontrivial case in which at least some participating l-type advertisers can match h-type ones in valuation; i.e., $\underline { { b } } _ { h } < Q _ { l } / Q _ { h }$ .

(Only-if part): We first show that a weighted unit-price auction with unequally constraining minimum bids is inefficient. When the minimum bid for h-type advertisers is more constraining, any weighting factor that results in a matching point being one for l-type advertisers is not efficient, because an l-type advertiser with valuation-per-click one would lose to an h-type advertiser with valuation-per-click $\underline { { b } } _ { h }$ despite having higher expected valuation. If the matching point is less than one, by Lemma 2, an l-type advertiser with valuation-per-click $v > v _ { 0 }$ will tie with an h-type advertiser with valuation-per-click wv (provided that $w v < 1 )$ . By the same argument in Proposition 2, the allocation among these advertisers is efficient only if the weighting factor is $Q _ { l } / Q _ { h }$ . However, if the weighting factor is $Q _ { l } / Q _ { k }$ and the minimum bid for h-type advertisers is more constraining, by Proposition 4, h-type advertisers with valuation-per-click between $\underline { { b } } _ { h }$ and wv $w v _ { 0 }$ are unmatched by any l-type advertisers, implying that the h-type advertisers are inefficiently favored under the current minimum bids. So, it is not possible to achieve allocation efficiency with a more constraining minimum bid for h-type advertisers. By a similar argument, we can show that nor is it possible with a less constraining minimum bid for h-type advertisers.

One cannot achieve efficiency with equally constraining minimum bids but an inefficient weighting factor either. If minimum bids are equally constraining, an l-type advertiser with valuation-per-click v always ties with an h-type advertiser with valuation-per-click wv. By the argument in Proposition 2, one can achieve efficiency only by setting the weighting factor to $Q _ { l } / Q _ { h } .$ . In sum, a weighted unit-price auction is weakly efficient only if the weighting factor is efficient and minimum bids are equally constraining.

Derivation of Revenue-Maximizing Minimum Bids. Define $J _ { \theta } ( v ) { = } v - ( 1 { - } F _ { \theta } ( v ) ) / f _ { \theta } ( v )$ and $\rho _ { l } ( v _ { 0 } ^ { - } ) { \equiv } \operatorname* { l i m } _ { v \to v _ { 0 } ^ { - } } \rho _ { l } ( v )$ $\mathop { = } \rho _ { h } ( \underline { { b } } _ { h } )$ . Taking the partial derivative of (17) with respect to $\underline { { b } } _ { h }$ and $\underline { { b } } _ { l } ,$ respectively, we obtain the first-order conditions (note that $v _ { 0 }$ is a function of $\underline { { b } } _ { h }$ and b )

$$
\begin{array}{l} (1 - \alpha) Q _ {l} \rho_ {l} (v _ {0} ^ {-}) J _ {l} (v _ {0}) f _ {l} (v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} \\ + (1 - \alpha) Q _ {l} \int_ {\underline {{b}} _ {l}} ^ {v _ {0}} \frac {d \rho_ {l} (v)}{d \underline {{b}} _ {h}} J _ {l} (v) f _ {l} (v) d v \\ - (1 - \alpha) Q _ {l} \rho_ {l} (v _ {0}) J _ {l} (v _ {0}) f _ {l} (v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} - \alpha Q _ {h} \rho_ {h} (\underline {{b}} _ {h}) J _ {h} (\underline {{b}} _ {h}) f _ {h} (\underline {{b}} _ {h}) \\ + \alpha Q _ {h} \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \frac {d \rho_ {h} (v)}{d v _ {0}} \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} J _ {h} (v) f _ {h} (v) d v = 0 \\ - (1 - \alpha) Q _ {l} \rho_ {l} (\underline {{b}} _ {l}) J _ {l} (\underline {{b}} _ {l}) f _ {l} (\underline {{b}} _ {l}) + (1 - \alpha) Q _ {l} \rho_ {l} (v _ {0} ^ {-}) J _ {l} (v _ {0}) f _ {l} (v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} \\ - (1 - \alpha) Q _ {l} \rho_ {l} (v _ {0}) J _ {l} (v _ {0}) f _ {l} (v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} \\ + \alpha Q _ {h} \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \frac {d \rho_ {h} (v)}{d v _ {0}} J _ {h} (v) f _ {h} (v) d v = 0, \end{array} \tag {41}
$$

in which $\partial v _ { 0 } / \partial { b _ { h } }$ and $\partial v _ { 0 } / \partial { \underline { { b } } } _ { l }$ can be derived from the partial derivatives of both sides of Equation (16) with respect

to $\underline { { b } } _ { h }$ and $\underline { { b } } _ { l } ,$ respectively:

$$
\begin{array}{l} w \rho_ {l} (v _ {0} ^ {-}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} + w \int_ {\underline {{b}} _ {l}} ^ {v _ {0}} \frac {d \rho_ {l} (t)}{d \underline {{b}} _ {h}} d t \\ = w \rho_ {h} (w v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} - \rho_ {h} (\underline {{b}} _ {h}) + \frac {\partial v _ {0}}{\partial \underline {{b}} _ {h}} \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \frac {d \rho_ {h} (t)}{d v _ {0}} d t \\ - w \rho_ {l} (\underline {{b}} _ {l}) + w \rho_ {l} (v _ {0} ^ {-}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} \\ = w \rho_ {h} (w v _ {0}) \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} + \frac {\partial v _ {0}}{\partial \underline {{b}} _ {l}} \int_ {\underline {{b}} _ {h}} ^ {w v _ {0}} \frac {d \rho_ {h} (v)}{d v _ {0}} d v. \end{array}\tag{42}
$$

(43)

The system of equations above allows us to solve the revenue-maximizing minimum bids for l-type advertisers $\left( \underline { { b } } _ { l } ^ { * } \right)$ and $h \mathrm { - t y p e }$ advertisers $\left( \underline { { b } } _ { h } ^ { * } \right)$ . For example, solving (40) we can get $\underline { { b } } _ { h } = \underline { { b } } _ { h } ^ { * } ( \underline { { b } } _ { l } )$ . Substituting $\underline { { b } } _ { h } ^ { * } ( \underline { { b } } _ { l } )$ into (41), we can derive $\underline { { b } } _ { l } ^ { * }$

Proof of Proposition 6. <sub>Denote</sub> $H ( x ) \equiv \alpha F _ { h } ( x / Q _ { h } ) +$ $( 1 - \alpha ) F _ { l } ( x / Q _ { l } )$ . Using the similar approach as in Proof for Proposition 1, we can derive the equilibrium bidding function for the generalized first-price auction as

$$
b (x) = x - \frac {\sum_ {j = 1} ^ {m} \delta_ {j} \int_ {0} ^ {x} \binom {n - 1} {n - j} H (t) ^ {n - j} [ 1 - H (t) ] ^ {j - 1} d t}{\sum_ {j = 1} ^ {m} \delta_ {j} \binom {n - 1} {n - j} H (x) ^ {n - j} [ 1 - H (x) ] ^ {j - 1}}.
$$

If this bid is from an l-type advertiser, let $v = x / Q _ { i }$ <sub>l</sub>. Noting that $H ( Q _ { l } v ) = \alpha F _ { h } ( ( Q _ { l } / Q _ { h } ) v ) + ( 1 - \alpha ) F _ { l } ( v ) = \alpha F _ { h } ( w _ { \mathrm { e f f } } v ) + $ $( 1 - \alpha ) F _ { l } ( v ) = G _ { l } ( v )$ , we have

$$
\begin{array}{c} b (x) = Q _ {l} v - \frac {\sum_ {j = 1} ^ {m} \delta_ {j} \int_ {0} ^ {Q _ {l} v} (_ {n - j} ^ {n - 1}) H (t) ^ {n - j} [ 1 - H (t) ] ^ {j - 1} d t}{\sum_ {j = 1} ^ {m} \delta_ {j} (_ {n - j} ^ {(n - 1)}) H (Q _ {l} v) ^ {n - j} [ 1 - H (Q _ {l} v) ] ^ {j - 1}} \\ = Q _ {l} v - Q _ {l} \frac {\int_ {0} ^ {v} \rho_ {l} (t) d t}{\rho_ {l} (v)} = Q _ {l} b _ {l} (v), \end{array}
$$

which means the total payment the advertiser bids is exactly the unit price he/she would bid under efficient weighted unit-price auctions times his/her expected CTR. Similar argument holds if the bid is from an h-type advertiser. Therefore, efficient weighted unit-price auctions are revenue-equivalent to generalized first-price auctions.

## References

Armstrong, M. 2000. Optimal multi-object auctions. Rev. Econom. Stud. 67(3) 455–481.

Asker, J. W., E. Cantillon. 2008. Properties of scoring auctions. RAND J. Econom. 39(1) 69–85.

Bapna, R., P. Goes, A. Gupta. 2005. Pricing and allocation for quality differentiated online services. Management Sci. 51(7) 1141–1150.

Beall, S., C. Carter, P. L. Carter, T. Germer, T. Hendrick, S. Jap, L. Kaufmann, et al. 2003. The role of reverse auctions in strategic sourcing. CAPS Research Report, Tempe, AZ.

Che, Y.-K. 1993. Design competition through multidimensional auctions. RAND J. Econom. 24(4) 668–680.

Edelman, B., M. Ostrovsky, M. Schwarz. 2007. Internet advertising and the generalized second price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1) 242–259.

eMarketer. 2007. Online advertising on a rocket ride. eMarketer Reports (November 7) 1–2.

Ewerhart, C., K. Fieseler. 2003. Procurement auctions and unit-price contracts. RAND J. Econom. 34(3) 569–581.

Feng, J. 2007. Optimal allocation mechanisms when bidders ranking for the objects is common. Marketing Sci. Forthcoming.

Google. 2006. Accessed September 26, 2009, http://adwords. blogspot.com/2006/11/landing-page-quality-update.html.

Hosanagar, K., R. Krishnan, J. Chuang, et al. 2005. Pricing and resource allocation in caching services with multiple levels of quality of service. Management Sci. 51(12) 1844–1859.

Interactive Advertising Bureau and PricewaterhouseCoopers. 2008. Internet advertising revenues again reach new highs, estimated to pass \$21 billion in 2007 and hit nearly \$6 billion in Q4 2007. Report, Interactive Advertising Bureau and PricewaterhouseCoopers, New York.

Krishna, V. 2002. Auction Theory. Academic Press, San Diego.

Lahaie, S. 2006. An analysis of alternative slot auction designs for sponsored search. Proc. 7th ACM Conf. Electronic Commerce, ACM Press, Ann Arbor, MI, 218–227.

Liu, D., J. Chen. 2006. Designing online auctions with performance information. Decision Support Systems 42(3) 1307–1320.

McAfee, R. P., J. McMillan. 1986. Bidding for contracts—A principal-agent analysis. RAND J. Econom. 17(3) 326–338.

McAfee, R. P., J. McMillan. 1987. Auctions and bidding. J. Econom. Literature 25(2) 699–738.

Myerson, R. B. 1981. Optimal auction design. Math. Oper. Res. 6(1) 58–73.

Pinker, E. J., A. Seidmann, Y. Vakrat. 2003. Managing online auctions: Current business and research issues. Management Sci. 49(11) 1457–1484.

Riley, J. G. 1988. Ex post information in auctions. Rev. Econom. Stud. 55(3) 409–429.

Samuelson, W. 1986. Bidding for contracts. Management Sci. 32(12) 1533–1550.

Snir, E. M., L. M. Hitt. 2003. Costly bidding in online markets for IT services. Management Sci. 49(11) 1504–1520.

Sundararajan, A. 2004. Nonlinear pricing of information goods. Management Sci. 50(12) 1660–1673.

Sundararajan, A. 2006. Pricing digital marketing: Information, risk sharing and performance. Working paper, New York University, New York.

Varian, H. R. 2007. Position auctions. Internat. J. Indust. Organ. 25(6) 1163–1178.

Weber, T. A., Z. Zheng. 2007. A model of search intermediaries and paid referrals. Inform. Systems Res. 18(4) 414–436.
