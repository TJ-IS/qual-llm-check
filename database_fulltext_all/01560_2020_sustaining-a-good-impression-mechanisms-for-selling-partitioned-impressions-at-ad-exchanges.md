---
otero_id: 1560
otero_key: "9S5WHDE3"
title: "Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges"
authors: "Sameer Mehta; Milind Dawande; Ganesh Janakiraman; Vijay Mookerjee"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0878"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/9S5WHDE3/fulltext/images/e1968ba3beee658019ea2551ed54a603bdaa1c4b13c82ecffef87ea945985a37.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges

Sameer Mehta, Milind Dawande, Ganesh Janakiraman, Vijay Mookerjee

To cite this article: Sameer Mehta, Milind Dawande, Ganesh Janakiraman, Vijay Mookerjee (2020) Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges. Information Systems Research

Published online in Articles in Advance 17 Mar 2020

https://doi.org/10.1287/isre.2019.0878

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Sustaining a Good Impression: Mechanisms for Selling Partitioned Impressions at Ad Exchanges

Sameer Mehta,<sup>a</sup> Milind Dawande,<sup>a</sup> Ganesh Janakiraman,<sup>a</sup> Vijay Mookerjee<sup>a</sup>

<sup>a</sup> The University of Texas at Dallas, Richardson, Texas 75080

Contact: sameer.mehta@utdallas.edu, https://orcid.org/0000-0002-0410-3248 (SM); milind@utdallas.edu (MD); ganesh@utdallas.edu (GJ); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: November 18, 2017 Revised: October 11, 2018; March 18, 2019 Accepted: May 17, 2019 Published Online in Articles in Advance: March 17, 2020

https://doi.org/10.1287/isre.2019.0878

Copyright: © 2020 INFORMS

Abstract. In the mobile advertising ecosystem, the role of ad exchanges to match advertisers and publishers has grown significantly over the past few years. At a mobile ad exchange, impressions (i.e., opportunities to display ads) are sold to advertisers in real time through an auction mechanism. The traditional mechanism selects a single advertiser whose ad is displayed over the entire duration of an impression, that is, throughout the user’s visit. We argue that such a mechanism leads to an allocative inefficiency, as displaying only the winning ad throughout the lifetime of an impression precludes the exchange from exploiting the opportunity to obtain additional revenue from advertisers whose willingness to pay becomes higher during the lifetime of that impression. Our goal in this paper is to address this efficiency loss by offering mechanisms in which multiple ads can be displayed sequentially over the lifetime of the impression. We consider two plausible settings—one where each auction is individually rational for the advertisers and one where advertisers are better off relative to the traditional mechanism over the long run—and derive an optimal (i.e., revenue-maximizing for the ad exchange) mechanism for each setting. To efficiently compute the payment rule, the optimal mechanism for the former setting uses randomized payments. Under this mechanism, whereas the ad exchange always benefits relative to the traditional mechanism, the advertisers could either gain or lose—we demonstrate both these possibilities. The optimal mechanism for the latter setting is a “mutually beneficial” mechanism in that it guarantees a win–win for both the parties relative to the traditional mechanism, over the long run. Happily, for both the mechanisms, the allocation of ads and the payments from the advertisers are efficiently computable, thereby making them amenable to real-time bidding.

History: Xiaoquan (Michael) Zhang, Senior Editor; Bin Gu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0878.

Keywords: mobile advertising • ad exchanges • optimal mechanisms • mutually-bene<sup>fi</sup>cial mechanisms

## 1. Introduction

Many mobile publishers, that is, owners of mobile applications, or apps, earn revenue via advertisements on their apps. This revenue stream has been sustained primarily by the tremendous growth in mobile advertising over the past few years. In fiscal year 2017, mobile advertising accounted for 56.7% (\$49.9 billion) of the total advertising revenue (Interactive Advertising Bureau 2017). One of the key drivers of this growth is the emergence of multiple channels to sell digital ads. Until recently, publishers would sell most of their impressions through ad networks<sup>1</sup> via long-term contracts. These contracts are usually drawn on a revenue-sharing basis, where the ad network shares a proportion of the revenue it earns with the publishers.

A now-popular way to buy and sell digital ads is via an ad exchange—an online, automated marketplace that connects advertisers and publishers to buy and sell ads through auctions in real time;<sup>2</sup> examples include DoubleClick, RightMedia, AppNexus, and OpenX. Ad exchanges are attractive to publishers, as they provide liquidity in selling impressions, offer better transparency than ad networks, and help elicit better prices from advertisers. Also, advertisers get access to a large inventory of impressions and are able to better target their audiences. With benefits to both publishers and advertisers, the growth of ad exchanges to trade digital ads has surged over recent years. Present-day ad exchanges are closely aligned with publisher goals—higher revenue for the ad exchange translates to higher revenue for the publishers.

The focus of our study is on display advertising on mobile devices, for example, smartphones or tablets. At a mobile ad exchange, advertisers—or, equivalently, ad agencies who manage ad campaigns on behalf of advertisers—bid for impressions originating from mobile devices; DoubleClick, PubMatic, Smaato, and Nexage, are some prominent present-day mobile ad exchanges. As will become clear soon, mobile inapp advertising can especially benefit from the kind of inefficiency we seek to eliminate, as app sessions typically last much longer than user visits on web pages—4.2 minutes on average, compared with just under 1 minute, according to a recent study (iAd 2014). The traditional auction for click ads that has been used in these exchanges solicits a bid from each advertiser (for the value he derives from the user clicking on that ad) in a real-time auction; the winner’s ad is displayed on the impression over the entire lifetime of that impression, that is, throughout the user’s visit. We highlight an allocative inefficiency in the traditional auction via a simple but illustrative example.

## 1.1. Inef<sup>fi</sup>ciency in Traditional Allocation

Consider the traditional auction with two advertisers (1 and 2), competing to display their ads, say, A and B, respectively, on a mobile impression. Suppose advertiser 2 wins the auction, as a result of which ad B is displayed on the user’s app. As the app session progresses, the click probability of ad B varies due to a variety of factors. Because the value of displaying an ad to its advertiser is tied to its click probability, the (instantaneous) value of ad B to its advertiser also varies with the passage of time. This notion of the varying value of ad B is represented by the dotted curve in Figure 1.

Figure 1. Allocative Inefficiency in the Traditional Auction at Ad Exchanges: An Illustrative Example  
![](/api/attachments/9S5WHDE3/fulltext/images/a9a672e9b69dc89494a8f6274a3c647835d84f00b2573fce96f7a6770183442a.jpg)

Now, consider ad A that lost to ad B in the auction and is, therefore, not displayed on the user’s app. Had advertiser 1 won the auction and ad A were displayed to the user, its (instantaneous) value would also vary with the passage of time but possibly at a different rate than that of ad B. This is represented by the solid curve in Figure 1. Notice that in time interval <sub>[</sub> <sub>]</sub> t<sub>1</sub>, t<sub>2</sub> , the (instantaneous) value of displaying ad A is higher than that of displaying ad B; thus, during this interval, advertiser 1 would be willing to pay more to display ad A to the user than would advertiser 2 to display ad B. However, because advertiser 2 won the auction, ad B is displayed to the user throughout the lifetime of the impression. Thus, the shaded region in Figure 1 represents, from the ad exchange’s perspective, an allocative inefficiency<sup>3</sup> from the use of the traditional auction.

This brings us to the idea of allocating (possibly) multiple ads to an impression when it is auctioned, with each allocated ad being scheduled for display in specific “slots” of time; of course, the ad scheduled for display at a certain time can actually be shown only if the impression lasts until that time. For instance, in the above example, the mechanism used by the ad exchange could choose to allocate ad A to the interval 0, t and ad B to the interval $[ t _ { 1 } , t _ { 2 } ]$ . Allocating multiple ads to an impression potentially gives the ad exchange an opportunity to obtain more surplus from the trade. Furthermore, there is no technological hurdle in implementing this idea—for example, the DoubleClick and OpenX exchanges allow publishers to dynamically reload ads on an impression.<sup>4</sup> Thus, a natural goal is an effective mechanism for the exchange to sell such “partitioned” impressions.

Given the discussion above, a mechanism that immediately suggests itself is one that considers each slot separately and allocates the best ad in that time slot. However, such a mechanism will yield subopti mal revenue to the ad exchange as it does not take into account the impact of the ad placed in the current time slot on the (potential) time slots in the future. We will analyze this mechanism and show that the revenue from this “myopic” mechanism can be significantly lower than that from the optimal mechanism, and it is therefore not an attractive prospect for the ad exchange.

A related issue is the welfare implication of such a mechanism on the advertisers. Whereas the ad exchange will clearly benefit relative to the traditional mechanism, it is not immediately clear whether the advertisers will too. If the advertisers could be worse off in some situations, then one could also consider alternate mechanisms under which the ad exchange ensures that the advertisers are at least as well off as they are under the traditional mechanism.

Given that a predominant volume of impressions are being sold today via adexchanges, the removal of this allocative inefficiency by designing attractive mechanisms has significant implications for the advertising ecosystem. Moreover, such a mechanism should be suited for real-time bidding; that is, the allocation of ads and the payment from the advertisers should be efficiently computable. For wider acceptability, it would also help if the mechanism is simple in its structure. We address all these goals in this study.

Before proceeding further, we briefly discuss our main contributions.

## 1.2. Our Contributions

We propose an approach to address the allocative inefficiency in present-day mobile ad exchanges that arises from the sale of an impression to a single advertiser—as discussed above, the allocation rule of the traditional mechanism fails to exploit advertisers willingness to pay over the lifetime of the impression. To this end, we develop a framework that addresses this efficiency loss, namely, the partitioning of an impression into time slots and allocating (possibly) multiple ads sequentially to these time slots when the impression is auctioned.

We obtain optimal mechanisms for selling partitioned impressions under two plausible settings that differ in terms of the utility guarantee they offer to the advertisers: The first (Setting 1) considers mechanisms in which each auction is individually rational (IR) for the advertisers. Given that advertisers typically participate in tens of thousands of such auctions each day, the long-term utility of each advertiser is also a reasonable metric. Accordingly, our second setting (Setting 2) considers mechanisms in which advertisers obtain at least as much utility as in the traditional mechanism, over the long term. We obtain optimal mechanisms under each of these settings— the one for Setting 1 is referred to as OPT-IR (optimal individually rational) and the one for Setting 2 as OPT-MB (optimal mutually beneficial). We note that the traditional mechanism is feasible under both the settings.

The OPT-IR and OPT-MB mechanisms are well suited for real-time bidding. The mechanisms consist of an allocation rule (assignment of ads to time slots) and a payment rule (amounts charged to the advertisers for displaying their respective ads). An ad exchange needs to process several activities from the time it receives an impression to the time it delivers the ad to the publisher’s app. This includes packaging information about the impression (user demographics, operating system platform type, publisher app type, etc.) into several categories, revealing all or part of this information to advertisers, obtaining bids from advertisers, conducting an auction, and finally displaying the winning advertiser’s ad on the impression.

The entire process must be completed fast enough (usually within 150 milliseconds) so that the app user does not experience any perceptible delay in the rendering of the ad. The allocation rules of both the optima mechanisms can be efficiently obtained by solving a deterministic dynamic program of complexity 2<sub>(</sub>AN<sub>)</sub>, where A is the number of advertisers in the auction, and N is the maximum number of time slots that the impression is partitioned into. Thus, the allocation rules can be incorporated into the ad-delivery process without causing a significant delay. Furthermore, the allocation rule of the OPT-MB mechanism is the first best; that is, generates the maximum possible social welfare through the trade.

The payment rule of the OPT-IR mechanism, however, is difficult to compute “as is” for the following reason. This mechanism needs to compute the information rent to each advertiser, which, in turn, is obtained from the allocation rule of the mechanism. For our problem, the allocation rule consists of a sequence of ads (i.e., an assignment of ads to time slots) With the increase in the bid of an ad, both the sequence of ads displayed in the time slots as well as the subset of slots assigned to that ad can change several times. Furthermore, there is no characterization of when the sequence of ads changes. This makes the payment rule of the OPT-IR mechanism difficult to compute and thus poses an implementation challenge. As a remedy, we develop a randomized payment rule that is both optimal and easy to implement. Furthermore, the payment can be implemented in either of the two most popular formats in use today—cost per click (CPC) and cost per mille (CPM). The payment rule of the OPT-MB mechanism can be easily computed. This simplification stems from the fact that the OPT-MB mechanism is not required to compute the information rent; it provides each advertiser exactly his expected utility from the traditional mechanism, which can be precomputed. Therefore, in the OPT-MB mechanism, each advertiser pays his value obtained from the allocation less his expected utility from the traditional mechanism.

We also analyze the welfare implications of the OPT-IR and OPT-MB mechanisms on the ad exchange and the advertisers. Because the mechanism-design problem in each of the two settings is formulated from the perspective of the ad exchange and the traditional mechanism is feasible for this problem, it is clear that the ad exchange benefits from the optimal mechanism relative to the traditional mechanism. However, advertisers may be worse off under the OPT-IR mechanism relative to the traditional mechanism. We demonstrate both the possibilities—that is, the OPT-IR mechanism benefiting (win–win) and hurting (win–lose) the advertisers—analytically. On the other hand, each advertiser’s utility under the OPT-MB mechanism is, by construction, at least that under the traditional mechanism, in the long run.

Finally, we examine the performance of the OPT-IR and the OPT-MB mechanisms on an illustrative suite of instances and contrast their relative strengths. The main message from this numerical study is that both the mechanisms can effectively address the allocative inefficiency in the traditional mechanism—the ad exchange can gain handsomely (ranging from 7% to 33% in our study) under either mechanism, and this gain further improves as the ads become more heterogeneous in terms of their click probabilities over time. Moreover, both the mechanisms are attractive in terms of the social welfare they generate—the OPT-IR mechanism achieves a near-first-best social welfare, and the OPT-MB mechanism achieves the first-best social welfare.

## 1.3. Organization of This Paper

We review the relevant literature in Section 2. In Section 3, we first discuss preliminaries that are common to both Setting 1 and Setting 2, and then formulate the mechanism-design problem for Setting 1. In Section 4, we derive an optimal mechanism (OPT-IR) for Setting 1 and address a variety of issues related to its implementation. Section 5 analyzes a myopic mechanism that conducts an auction in each time slot, and Section 6 compares its performance with the OPT-IR mechanism. Next, Section 7 analyzes the traditional mechanism that is currently used by mobile ad exchanges. Section 8 compares the OPT-IR mechanism with the traditional mechanism by evaluating its impact on advertisers; here we show analytically that advertisers can either gain or lose under the OPT-IR mechanism. In Section 9, we obtain an optimal mechanism (OPT-MB) for Setting 2; this mechanism guarantees a higher revenue to the ad exchange and a higher surplus to the advertisers, relative to the traditional mechanism. Section 10 investigates the OPT-IR and OPT-MB mechanisms numerically and quantifies their benefit over the traditional mechanism. Section 11 concludes.

## 2. Literature Review

The design of advertising auctions in the digital ecosystem has been studied extensively in the literature. For example, Edelman et al. (2007), Varian (2007), Liu et al. (2010), and Abhishek and Hosanagar (2013) design mechanisms for slots/positions in sponsored-search auctions (for an excellent discussion on sponsoredsearch auctions, see Nisan et al. 2007, chapter 28). Kim et al. (2012) study the design problem of determining the optimal number of slots in these auctions. This stream of papers focuses on allocating (search) ads to spatial slots on a web page simultaneously, whereas we study a setting where an impression is partitioned into several time slots and (display) ads are shown sequentially. This differentiation has several bearings on the dynamics of ad allocation and payment of our mechanisms:

• Because of the sequential display of ads, the allocation rules of our mechanisms are obtained by solving a dynamic program.

• The display of an ad in a particular time slot is contingent on the user not leaving the app session earlier and not clicking on an ad displayed earlier in the sequence.

• In a sponsored-search auction, a single ad is allocated to at most one physical slot on the web page, whereas in our mechanism, an ad can be allocated to multiple time slots.

Aumann et al. (2016) consider the problem of auctioning the timed consumption of a resource by multiple agents, where each agent has different valuations for different time intervals. For this multidimensional private-information setting, the social planner has to decide which agent should be allocated the resource, and for how long, to maximize total surplus (i.e., to maximize efficiency) instead of revenue. Another difference with respect to our work is that they allow allocation of only contiguous time intervals to the agents. As agents have different valuations for different time intervals, they show that the associated allocation problem is NP-complete and therefore seek computationally efficient mechanisms. In contrast, our problem deals with optimal mechanisms that allocate time slots of predetermined length to advertisers with single-dimensional private information.

McAfee and Vassilvitskii (2012) describe a broad set of practical issues—efficiency, expressiveness, strategic simplicity, and neutrality toward participants—in designing exchanges. The mechanisms that we derive in our study are guided by these principles. Specifically, we develop revenue-maximizing mechanisms for the ad exchange that are (i) easy to implement in a real-time environment, (ii) incentive compatible (IC) for the advertisers, and (iii) simple for advertisers to communicate, in that they only need to report their valuation per click. Our mechanisms also take into consideration the welfare implication on both the ad exchange and the advertisers.

Our work is also related to the literature on scheduling display ads. The paper closest to our work is that by Sun et al. (2017), which analyzes the following setting. A supply-side ad network has acquired an impression. The ad network has a set of ads (of the advertisers that the ad network has contracted with) that it wants to possibly display on that impression. For this purpose, the ad network wants to determine a sequence of ads to display on that impression during its lifetime. If an ad is clicked, the ad network charges an ad-specific amount (valuation per click)

to the corresponding advertiser. The advertisers sign a contract with the ad network that specifies the amount that they have to pay to the ad network when their respective ads are clicked. Therefore, in this setting, the ad network has full information about the value that a particular ad sequence can yield. The objective of the ad network is to determine an ad sequence that maximizes expected revenue. The authors obtain near-optimal algorithms (optimal under some special cases) for the ad-sequencing problem above.

The context of our paper is fundamentally different from that considered by Sun et al. (2017). In our setting, an ad exchange is faced with the challenge of selling partitioned impressions to the advertisers. Unlike ad networks, the ad exchange does not know the per-click valuations of the advertisers, which naturally gives rise to information asymmetry between the ad exchange and the advertisers. Consequently, the ad exchange has to design a mechanism (an auction) to sell the partitioned impressions. The design of an optimal mechanism involves obtaining an allocation rule as well as a payment rule. By announcing these two rules of a mechanism to the advertisers, the ad exchange offers appropriate incentives to the advertisers to participate in the mechanism and report their valuations truthfully in equilibrium. The optimal ad-scheduling problem studied by Sun et al. (2017) focuses only on obtaining the best schedule of ads to display on the impression and completely ignores modeling advertisers’ incentives.

Whereas the allocation rule of our optimal mechanism can be computed efficiently, the payment rule of that mechanism is not amenable to real-time implementation as is. We address this challenge by developing the randomized payment rule that yields the same expected revenue as the payment rule of the OPT-IR mechanism. To the best of our knowledge, this idea of randomized payment is novel in the context of the digital advertising literature and is appropriate for real-time implementation in both the CPM and CPC formats.

Another important difference is that the problem considered by Sun et al. (2017) is solely from the context of an ad network and completely ignores the welfare of the advertisers. In contrast, we consider the welfares of the supply-side (ad exchange) and demand-side (advertisers) players in our problem. This gives rise to interesting questions such as how a mechanism affects the two parties. As will be shown later, a mechanism that benefits the ad exchange may prove harmful to the advertisers. This possibility drives the subsequent discussion in our paper, leading to the proposal of a mutually beneficial mechanism, which is another important contribution of our paper aimed at improving current practice.

Hojjat et al. (2017) consider advertisers’ constraints— reach and frequency of ads—for ad planning and delivering sequenced ads. A case study on Facebook ads (Adaptly 2014) experimentally demonstrates that creatively sequencing ads at a personalized level increases view-through and subscription rates. Mohan et al. (2013) focus on the challenges and feasibility of prefetching multiple ads in the existing advertising architecture. Bharadwaj et al. (2012) develop an efficient algorithm to allocate ads in guaranteed contracts. Turner et al. (2011) model the scheduling of ads in video games and develop a dynamic scheduling algorithm.

Several studies investigate other challenges that arise in display advertising, such as (i) targeting strategies (Goldfarb and Tucker 2011), including mobile targeting (Andrews et al. 2015, Chen et al. 2017); (ii) ad positioning (Agarwal et al. 2011); (iii) click behavior (Chatterjee et al. 2003); (iv) wearout of ads (Braun and Moe 2013); and (v) preference between the CPC and CPM pricing formats (Asdemir et al. 2012, Najafi-Asadolahi and Fridgeirsdottir 2014), among others. Goldstein et al. (2015) discuss the effectiveness of sell ing time-based display ads by analyzing the duration of the ads through an online behavioral experiment. Muthukrishnan (2009) and Korula et al. (2016) discuss some of the broader issues and research opportunities in the digital advertising ecosystem. Yuan et al. (2014) provide a comprehensive survey on realtime-bidding advertising.

We also note a related stream of literature that investigates supply- and demand-side issues that arise in the digital advertising ecosystem. The supply side consists of publishers and ad networks. Balseiro et al. (2014) model the trade-off faced by publishers in selling their impressions via an ad exchange for shortterm revenue against the long-term benefits obtained by contracting with an ad network. Roels and Fridgeirsdottir (2009) consider the problem of maximizing publisher revenue in the presence of advertising requests and web traffic. Balseiro et al. (2015) study various design decisions (e.g., reserve prices) in the presence of dynamic interactions among budgetconstrained advertisers. Yang et al. (2010) study a publisher’s problem of allocating ad space between guaranteed delivery from an ad network and nonguaranteed delivery from an ad exchange, under multiple objectives for the publisher and the advertisers. The demand side of the ecosystem primarily includes advertisers and demand-side platforms. Several papers focus on campaign-management issues from the demand side; see, for example, Aseri et al. (2017) and Balseiro et al. (2017). Zhang et al. (2014) derive optimal real-time bidding strategies for display advertising based on advertiser’s budget, campaign objective, and impression details.

Allouah and Besbes (2017) show that under a wide range of market settings, multibidding by a demand-side platform—that is, the platform submitting multiple bids to the ad exchange instead of one—benefits both demand-side and supply-side players.

## 3. Preliminaries and Formulation of Setting 1

We begin by describing the key elements used in Setting 1 and Setting 2:

• Impression. An opportunity to display an ad on an app is referred to as an impression. We assume that time is divided into slots of equal length that is determined by industry practice as the minimum length of exposure for an ad; for instance, mobile ads sold through the DoubleClick ad exchange are shown for a minimum of 30 seconds. Let N be a sufficiently large integer such that the length of an app session (i.e., the time the user stays on the app until he either leaves the app or clicks on an ad) can be reasonably assumed<sup>5</sup> to be at most N time slots. We index the time slots by n; $n = 1 , 2 , \ldots , N .$ . Slots of varying length can be easily accounted for by adjusting the click probabilities of the ads in the different time slots.

• Mobile ad exchange. For each impression that is generated on an app, the ad exchange solicits valuation per click bids from advertisers for their respective ads and chooses a sequence of ads to display in the time slots of that impression. The objective of the ad exchange is to maximize its expected revenue over the lifetime of the impression.

• Advertisers. We use the term advertiser to reference an entity that is interested in purchasing the impression. Advertisers compete to display their respective ads on the impression. We denote the set of advertisers by $\scriptstyle { \mathcal { A } } ;$ let $| { \overset { \cdot } { \lrcorner } } { \mathcal { A } } | = A$ . We assume that each advertiser bids for the display of only one ad and, therefore, use the subscript a for both of them interchangeably. Let the private valuation per click for advertiser a be denoted by $r _ { a } ,$ which is a random variable independently distributed with publicly known cumulative distribution function $\left( \mathrm { c . d . f . } \right)$ $F _ { a } ( \cdot )$ and probability density function $( \mathrm { p . d . f . } ) f _ { a } ( \cdot )$ over the interval $\mathcal { B } _ { a } = [ \dot { 0 } , \omega _ { a } ]$ . Let $\mathcal { B } = \times _ { a = 1 } ^ { A } \mathbf { \hat { \mathcal { B } } } _ { a }$ denote the Cartesian product of the valuation intervals of the advertisers, and for all $^ { a , }$ let $\mathcal { B } _ { - a } = \mathsf { X } _ { j \neq a } \mathcal { B } _ { j }$ . Let $\mathbf { r } =$ $\left[ r _ { 1 } , r _ { 2 } , \ldots , r _ { A } \right]$ denote the vector of the true valuations, and let $\mathbf { r } _ { - a } = \left[ r _ { 1 } , \ldots , r _ { a - 1 } , r _ { a + 1 } , \ldots r _ { A } \right]$ . The bid submitted by advertiser a is denoted by $b _ { a } ,$ and $\mathbf { b } = [ b _ { 1 } , b _ { 2 } , \ldots , b _ { A } ]$ . Let $\begin{array} { r } { f ( \mathbf { r } ) = \prod _ { a = 1 } ^ { A } f _ { a } ( r _ { a } ) } \end{array}$ denote the joint density at r, and let $f _ { - a } ( \mathbf { r } _ { - a } )$ denote the joint density at $\mathbf { r } _ { - a } .$ . Let $F ( \mathbf { r } )$ denote the joint distribution at r.

• Click probabilities. The click probability of an ad $a ,$ when shown in time slot n of the impression, is denoted by $p _ { a , n } .$ . In our analysis, we assume that the click probabilities of the advertisers are common knowledge.

This is a widely used assumption in the literature (see, e.g., Edelman et al. 2007, Garg and Narahari 2009, Thompson and Leyton-Brown 2013), with the argument that the bidders are likely to learn all relevant information about each other’s ads through repeated interactions. This assumption is not too restrictive for our context, in the following sense: ${ \mathrm { I f } } ,$ instead, the click probabilities of an ad are private to its advertiser and the ad exchange, and other adver tisers have only distributional knowledge of these probabilities, then all our mechanisms remain incentive compatible for the advertisers. Thus, the assumption that click probabilities are common knowledge is not needed for the advertisers to determine their bids; the assumption is needed only to establish the optimality of our mechanisms in their respective settings. For tractability, we assume that the click probability of an ad in a slot depends only on the time elapsed thus far in the user’s session. In general, the click probability of an ad in a particular slot might depend on several other characteristics, for example, the ads previously shown to the user in that session and the se quence in which they were shown. All the optimization problems we encounter in our analysis can also be formulated using a general click-probability structure that allows this click probability to depend on an arbitrary set of characteristics; however, then, the optimization problems are no longer efficiently solvable. Let the conditional probability that the user stays on the app until the end of a time slot, given that she enters that time slot and does not click on the ad, be denoted by λ.

We now formulate the mechanism-design problem for Setting 1.

## 3.1. Setting 1: Problem Formulation

Our analysis makes the following regularity assumption: For each $l \in \mathcal { A } ,$ , the distribution $F _ { a } ( \cdot )$ with density $f _ { a } ( \cdot )$ is regular, that is, the hazard rate $\big ( \frac { f _ { a } ( r _ { a } ) } { 1 - F _ { a } ( r _ { a } ) } \big )$ is nondecreasing and bounded. This assumption is common in the mechanism-design literature (see, e.g., Krishna 2009) and guarantees that the virtual valuation, $\begin{array} { r } { \psi _ { a } ( r _ { a } ) : = r _ { a } - \frac { 1 - F _ { a } ( r _ { a } ) } { f _ { a } ( r _ { a } ) } , } \end{array}$ , is nondecreasing in $r _ { a }$ over the support of $F _ { a }$ . Distributions that satisfy this assumption include, among others, uniform, exponential, truncated normal, log-normal and Weibull. Let $\mathcal { A } ^ { + } : =$ $\{ a \vert \psi _ { a } ( r _ { a } ) \ge 0 \} \subseteq \mathcal { A }$ denote the set of advertisers that have nonnegative virtual valuations.

Using the revelation principle (Myerson 1981), we restrict our attention, without loss of generality, to incentive compatible and individually rational direct mechanisms, that is, mechanisms in which (i) ad vertisers reporting their per-click valuations truthfully to the ad exchange is a Bayesian Nash equilibrium (BNE) and (ii) advertisers obtain a nonnegative expected payoff from participating in the mechanism and are therefore willing to do so.

A direct mechanism µ consists of a pair of functions Π<sup>µ</sup>, M<sup>µ</sup> , where $\Pi ^ { \mu } : \dot { \mathcal { B } }  \{ \mathcal { A } \cup \phi \} ^ { N }$ is the allocation rule that specifies the ad sequence, and $\mathbf { M } ^ { \mu } : \mathcal { B }  \mathbb { R } ^ { A }$ is the payment rule that specifies the expected payment by the advertisers to the ad exchange. These two rules are defined as follows:

$\bullet \ \Pi ^ { \mu } ( { \boldsymbol { \mathbf { b } } } ) = \{ \pi _ { n } ^ { \mu } ( { \boldsymbol { \mathbf { b } } } ) : 1 \leq n \leq N , { \boldsymbol { \mathbf { b } } } \in { \mathcal { B } } \}$ , where $\pi _ { n } ^ { \mu } ( \mathbf { b } )$ ∈ ! φ denotes the ad in time slot n for bid vector b. We allow for a null allocation in each time slot; thus, if no ad is allocated to slot $n ,$ then $\pi _ { n } ^ { \mu } ( \mathbf { b } ) = \phi$ (see Remark 1 in Section 4 for an alternate formulation of the allocation function).

$\mathbf { M } ^ { \mu } ( \mathbf { b } ) = \{ M _ { a } ^ { \mu } ( \mathbf { b } ) : a \in \mathcal { A } , \mathbf { b } \in \mathcal { B } \}$ , where $M _ { a } ^ { \mu } ( \mathbf { b } )$ denotes the expected payment made by advertiser a to the ad exchange under the bid vector b.

The objective of the ad exchange is to find a mechanism $\mu$ that maximizes its expected revenue over the N time slots of an impression. Table 1 summarizes our notation.

As is common in the mechanism-design literature, we assume that the advertisers have a quasi-linear utility function. The expected payoff to each advertiser from participating in an auction is equal to his expected value from the slots he wins minus the payment he makes to the ad exchange. Let $\Theta _ { a } ^ { \mu } ( \mathbf { b } )$ denote the likelihood of a click on ad a over all the time slots, under the mechanism $\mu ,$ when the advertisers bid b. Then,

$$
\begin{array}{r l r} & & {\Theta_ {a} ^ {\mu} (\mathbf {b}) = \sum_ {n = 1} ^ {N} p _ {a, n} \mathbb {1} \Bigl \{\pi_ {n} ^ {\mu} (\mathbf {b}) = a \Bigr \} \lambda^ {n - 1} \prod_ {t = 1} ^ {n - 1} \Bigl (1 - p _ {\pi_ {t} ^ {\mu} (\mathbf {b}), t} \Bigr)} \\ & & {\forall a \in \mathcal {A},} \end{array}\tag{1}
$$

where $\mathbb { I } \{ \cdot \}$ denotes the indicator function of its argument. For the sequence $\Pi ^ { \mu } ( \mathbf { b } )$ and time slot $n ,$ the term $\begin{array} { r } { \lambda ^ { n - 1 } \prod _ { t = 1 } ^ { n - 1 } ( 1 - \dot { p } _ { \pi _ { t } ^ { \mu } ( \mathbf { b } ) , t } ) } \end{array}$ denotes the probability that in the previous n 1 slots, the user neither exited the app $( \lambda ^ { n - 1 } )$ nor clicked on any ad $\begin{array} { r } { ( \prod _ { t = 1 } ^ { n - 1 } ( 1 - p _ { \pi _ { * } ^ { \mu } ( \mathbf { b } ) , t } ) ) } \end{array}$ The term $p _ { a , n } \mathbb { 1 } \{ \pi _ { n } ^ { \mu } ( \mathbf { b } ) = a \}$ denotes the click probability of ad a in time slot n. Thus, $\begin{array} { r } { \sum _ { n = 1 } ^ { N } p _ { a , n } \mathbb { I } \{ \pi _ { n } ^ { \mu } ( \mathbf { \bar { b } } ) = a \} \lambda ^ { n - 1 } } \end{array}$ $\begin{array} { r } { \prod _ { t = 1 } ^ { n - 1 } ( 1 - p _ { \pi _ { * } ^ { \mu } ( \mathbf b ) , t } ) } \end{array}$ denotes the probability that ad a is clicked when the sequence $\Pi ^ { \bar { \mu } } ( { \mathbf { \bar { b } } } )$ is chosen. Let $\theta _ { a } ^ { \mu } ( b _ { a } )$ denote the expected click probability of ad a across all the slots when advertiser a bids $b _ { a }$ and all the other advertisers bid their true valuations. Thus, $\theta _ { a } ^ { \mu } ( b _ { a } ) = \mathbb { E } _ { \mathbf { r } _ { a } } [ \Theta _ { a } ^ { \mu } ( b _ { a } , \mathbf { r } _ { - a } ) ]$ for all $a \in { \mathcal { A } }$

Let $m _ { a } ^ { \mu } ( b _ { a } )$ denote the expected payment by advertiser a to the ad exchange when he bids $b _ { a }$ and all the other advertisers report their true valuations. Thus, $m _ { a } ^ { \mu } ( b _ { a } ) = \mathbb { E } _ { { \mathbf { r } } _ { a } } [ M _ { a } ^ { \mu } \mathbf { \bar { ( } } b _ { a } , { \mathbf { r } } _ { - a } ) ]$ . Then, the net expected utility that advertiser a obtains from bidding $b _ { a }$ when all the other advertisers bid their true valuations is equal to $r _ { a } \theta _ { a } ^ { \mu } ( b _ { a } ) - m _ { a } ^ { \mu } ( b _ { a } )$ . The IC and the IR constraints can now be stated as follows:

$$
r _ {a} \theta_ {a} ^ {\mu} (r _ {a}) - m _ {a} ^ {\mu} (r _ {a}) \geq r _ {a} \theta_ {a} ^ {\mu} (b _ {a}) - m _ {a} ^ {\mu} (b _ {a}) \forall a \in \mathcal {A}, \forall r _ {a},\tag{IC}
$$

$$
r _ {a} \theta_ {a} ^ {\mu} (r _ {a}) - m _ {a} ^ {\mu} (r _ {a}) \geq 0 \forall a \in \mathcal {A}, \forall r _ {a}, b _ {a} \in \mathcal {B} _ {a}.\tag{IR}
$$

Let $U _ { a } ^ { \mu } ( r _ { a } ) = r _ { a } \theta _ { a } ^ { \mu } ( r _ { a } ) - m _ { a } ^ { \mu } ( r _ { a } )$ denote the expected utility to advertiser a under mechanism $\mu ,$ , in equilibrium. The constraints (IC) state that it is optimal for the advertisers to reveal their private valuation per click truthfully, given that all the other advertisers do so. In other words, truth telling is a BNE. The constraints (IR) state that the expected payoff of each advertiser in a BNE is nonnegative.

## 3.2. Setting 1: The Optimal Mechanism Design Problem

The ad exchange solicits valuation per click bids from the advertisers, based on which it determines (i) the optimal sequence (i.e., the allocation of ads to time slots) through the allocation function $\Pi ^ { \mu }$ and (ii) the expected payment from each advertiser through the payment function $\mathbf { M } ^ { \mu } .$ . The optimization problem for the ad exchange is

Table 1. Our Main Notation

<table><tr><td>Notation</td><td>Parameter description</td></tr><tr><td> $\mathcal{A}$ </td><td>The set of all ads;  $|\mathcal{A}| = A$ </td></tr><tr><td> $N$ </td><td>The number of time slots that the impression is partitioned into</td></tr><tr><td> $r_a$ </td><td>True (private) valuation per click for advertiser  $a$ ;  $a \in \mathcal{A}$ </td></tr><tr><td> $\mathbf{r} = [r_1, r_2, \ldots, r_A]$ </td><td>The valuation-per-click vector</td></tr><tr><td> $f_a(\cdot), F_a(\cdot)$ </td><td>The p.d.f. and c.d.f., respectively, of the valuation per click of advertiser  $a$ </td></tr><tr><td> $f(\mathbf{r}) = \prod_{a=1}^{A} f_i(r_a)$ </td><td>The joint density of vector  $\mathbf{r}$ </td></tr><tr><td> $f_{-a}(\mathbf{r}_{-a}) = \prod_{i=1}^{a-1} f_i(r_i) \prod_{j=a+1}^{A} f_j(r_j)$ </td><td>The joint density of vector  $\mathbf{r}_{-a}$ </td></tr><tr><td> $b_a$ </td><td>The valuation per click (bid) reported by advertiser  $a$ </td></tr><tr><td> $\psi_a(r_a) = r_a - \frac{1 - F_a(r_a)}{f_a(r_a)}$ </td><td>The virtual valuation of advertiser  $a$ </td></tr><tr><td> $\mathcal{A}^+$ </td><td>The set of advertisers with nonnegative virtual valuations</td></tr><tr><td> $p_{a,n}$ </td><td>Click probability of ad  $a$  when displayed in time slot  $n$ </td></tr><tr><td> $\lambda$ </td><td>Conditional probability of the user staying on the app at the end of a time slot, given that she enters that time slot and does not click on the ad</td></tr></table>

$$
\max _ {\mu} \left\{\sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \left[ m _ {a} ^ {\mu} (r _ {a}) \right] \right\}, \quad \text { s   .   t   . } (\mathrm{IC}), (\mathrm{IR});\tag{\((P^{IR})\}
$$

that ${ \mathrm { i } } \mathbf { s } ,$ the ad exchange maximizes the sum of the expected payments it obtains by allocating the ads to the impression, subject to the constraints (IC) and (IR) of the advertisers.

In Section 4, we derive several solutions (i.e., optimal mechanisms) to Problem (P<sup>IR</sup>) that differ in their implementation. Before proceeding further, we find it convenient to discuss the related problem of identifying efficient mechanisms—this will be helpful in Sections 4.1 and 9 in the discussions related to our optimal mechanisms.

## 3.3. Vickrey–Clarke–Groves (VCG) Mechanism

Consider the problem of designing an IC and IR mechanism that maximizes the social welfare, defined as the sum of the utilities to all the advertisers and the ad exchange. Because payments from the advertisers to the ad exchange are “internal transfers,” the social welfare for any valuation-per-click vector r under an arbitrary IC mechanism $\mu$ is

$$
\mathrm{sw} ^ {\mu} (\mathbf {r}) := \sum_ {a = 1} ^ {A} r _ {a} \Theta_ {a} ^ {\mu} (\mathbf {r}).\tag{2}
$$

Define <sup>sw</sup> $\mathbf { \Pi } _ { - i } ^ { \mu } ( \mathbf { r } ) : = \Sigma _ { a \neq i } r _ { a } \Theta _ { a } ^ { \mu } ( \mathbf { r } )$ . Using the expression of $\Theta _ { a } ^ { \mu } ( \mathbf { r } )$ from (1), the social welfare under mechanism $\mu$ can be written as

$$
\begin{array}{c} \mathrm{sw} ^ {\mu} (\mathbf {r}) = \sum_ {a = 1} ^ {A} r _ {a} \cdot \sum_ {n = 1} ^ {N} p _ {a, n} \mathbb {I} \Bigl \{\pi_ {n} ^ {\mu} (\mathbf {r}) = a \Bigr \} \\ \cdot \lambda^ {n - 1} \prod_ {t = 1} ^ {n - 1} \Bigl (1 - p _ {\pi_ {t} ^ {\mu} (\mathbf {r}), t} \Bigr). \end{array}\tag{3}
$$

An efficient IC and IR mechanism is one that maximizes (3) subject to (IC) and (IR). It is well known that the class of VCG mechanisms is efficient (Krishna and Perry 1998). Specific to our setting, the VCG mechanism is described by the allocation rule $\mathbf { I I } ^ { \mathrm { v c G } }$ and the payment rule $\mathbf { M } ^ { \mathrm { v c G } }$ defined below:

$$
\begin{array}{l} \Pi^ {\mathrm{vCG}} (\mathbf {r}) = \underset {\mu} {\arg \max} \left\{\operatorname{sw} ^ {\mu} (\mathbf {r}) \right\} \\ = \underset {\mu} {\arg \max} \left\{\sum_ {a = 1} ^ {A} r _ {a} \cdot \sum_ {n = 1} ^ {N} p _ {a, n} \mathbb {I} \left\{\pi_ {n} ^ {\mu} (\mathbf {r}) = a \right\} \lambda^ {n - 1} \right. \\ \quad \cdot \prod_ {t = 1} ^ {n - 1} \left(1 - p _ {\pi_ {t} ^ {\mu} (\mathbf {r}), t}\right) \Bigg \}, \end{array}\tag{\((P^{EFF})\}
$$

$$
M _ {a} ^ {\mathrm{VCG}} (\mathbf {r}) = \mathrm{sw} ^ {\mathrm{VCG}} (0, \mathbf {r} _ {- a}) - \mathrm{sw} _ {- a} ^ {\mathrm{VCG}} (\mathbf {r}) \forall a \in \mathcal {A}.\tag{4}
$$

We note that Problem $( \mathrm { P } ^ { \mathrm { E F F } } )$ is identical to a problem recently studied by Sun et al. (2017) in the context of an ad network optimizing the sequence of ads (that the network has already purchased) displayed during the lifetime of an impression. This problem can be solved using backward, dynamic programming recursion—the allocation rule, $\Pi ^ { \mathrm { v c G } } ( \mathbf { r } ) .$ , is

$$
\begin{array}{c} \pi_ {n} ^ {\mathrm{vCG}} (\mathbf {r}) = \underset {a \in \mathcal {A}} {\arg \max} \bigl \{r _ {a} p _ {a, n} + \lambda \bigl (1 - p _ {a, n} \bigr) R (n + 1; \mathbf {r}) \bigr \}; \\ 1 \leq n \leq N, \quad \text {where} \\ R (n; \mathbf {r}) = \underset {a \in \mathcal {A}} {\max} \bigl \{r _ {a} p _ {a, n} + \lambda \bigl (1 - p _ {a, n} \bigr) R (n + 1; \mathbf {r}) \bigr \}; \\ 1 \leq n \leq N, \text {and} R (N + 1; \mathbf {r}) = 0. \end{array}\tag{5}
$$

Next, we use this result and derive an optimal mecha nism for Problem $( { \mathrm { P } } ^ { ^ { \mathrm { I R } } } )$ ).

## 4. Setting 1: An Optimal Mechanism

We begin by specifying an optimal mechanism for Problem $( \mathbf { P } ^ { \mathrm { I R } } )$ in Theorem 1. Then, Sections 4.1 and 4.2 discuss the challenges associated with implementing this mechanism. We address these by obtaining an optimal mechanism that uses randomized payments. We also show how these payments can be adapted to the CPC and the CPM formats. We end this section with brief remarks on an alternate allocation rule and infinite-horizon mechanisms.

Consider the following mechanism $( \mathbf { I I } ^ { \mathrm { o p r - I R } } , \mathbf { M } ^ { \mathrm { o p T - I R } } )$

$$
\begin{array}{c} \Pi^ {\mathrm{OPT-IR}} (\mathbf {r}) = \arg \max _ {\mu} \Biggl \{\sum_ {a = 1} ^ {A} \psi_ {a} (r _ {a}) \Theta_ {a} ^ {\mu} (\mathbf {r}) \Biggr \}, \\ M _ {a} ^ {\mathrm{OPT-IR}} (\mathbf {r}) = r _ {a} \Theta_ {a} ^ {\mathrm{OPT-IR}} (\mathbf {r}) - \int_ {0} ^ {r _ {a}} \Theta_ {a} ^ {\mathrm{OPT-IR}} (t _ {a}, \mathbf {r} _ {- a}) d t _ {a} \\ \forall a \in \mathcal {A}. \end{array}\tag{6}
$$

(7)

Theorem 1. The mechanism $( \mathbf { I I } ^ { \mathrm { o p r - I R } } , \mathbf { M } ^ { \mathrm { o p r - I R } } )$ is an optima solution to Problem (P<sup>IR</sup>).

Proof. To show that $( \mathbf { I I } ^ { \mathrm { o p r - I R } } , \mathbf { M } ^ { \mathrm { o p r - I R } } )$ is an optimal solution to Problem $( \mathrm { P ^ { \mathrm { I R } } } )$ ), it is sufficient to show that for every a $\in \mathcal { A } , \Theta _ { a } ^ { \mathrm { o p T - I R } } ( \cdot , \mathbf { r } _ { - a } )$ is a nondecreasing function of its argument. A detailed proof of this claim is provided in Online Appendix A. Thus, we need to establish only that this sufficient condition holds. To this end, fix an advertiser $a \in { \mathcal { A } } .$ . Consider any two values of $r _ { a } , \mathrm { \ s a y } ,$ $r _ { a } ^ { 1 } , r _ { a } ^ { 2 } \in \mathcal { B } _ { a } ,$ , such that $r _ { a } ^ { 1 } \leq r _ { a } ^ { 2 }$ . Because $\psi _ { a } ( \cdot )$ is an increasing function of its argument, we have $\psi _ { a } ( r _ { a } ^ { 1 } ) \leq$ $\psi _ { a } ( r _ { a } ^ { 2 } )$ . From (6), we have

$$
\begin{array}{l} \psi_ {a} (r _ {a} ^ {2}) \Theta_ {a} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {2}, \mathbf {r} _ {- a}) + \sum_ {j \neq a} \psi_ {j} (r _ {j}) \Theta_ {j} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {2}, \mathbf {r} _ {- a}) \\ \qquad \geq \psi_ {a} (r _ {a} ^ {2}) \Theta_ {a} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {1}, \mathbf {r} _ {- a}) + \sum_ {j \neq a} \psi_ {j} (r _ {j}) \Theta_ {j} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {1}, \mathbf {r} _ {- a}), \\ \psi_ {a} (r _ {a} ^ {1}) \Theta_ {a} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {1}, \mathbf {r} _ {- a}) + \sum_ {j \neq a} \psi_ {j} (r _ {j}) \Theta_ {j} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {1}, \mathbf {r} _ {- a}) \\ \qquad \geq \psi_ {a} (r _ {a} ^ {1}) \Theta_ {a} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {2}, \mathbf {r} _ {- a}) + \sum_ {j \neq a} \psi_ {j} (r _ {j}) \Theta_ {j} ^ {\mathrm{OPT-IR}} (r _ {a} ^ {2}, \mathbf {r} _ {- a}). \end{array}
$$

Adding the two inequalities above, we get

$$
\big (\psi_ {a} \big (r _ {a} ^ {2} \big) - \psi_ {a} \big (r _ {a} ^ {1} \big) \big) \big (\Theta_ {a} ^ {\mathrm{OPT-IR}} \big (r _ {a} ^ {2}, \mathbf {r} _ {- a} \big) - \Theta_ {a} ^ {\mathrm{OPT-IR}} \big (r _ {a} ^ {1}, \mathbf {r} _ {- a} \big) \big) \geq 0.
$$

Because $\psi _ { a } ( r _ { a } ^ { 1 } ) \leq \psi _ { a } ( r _ { a } ^ { 2 } ) .$ , we get $\Theta _ { a } ^ { \mathrm { o p T - I R } } ( r _ { a } ^ { 1 } , \mathbf { r } _ { - a } ) \leq \Theta _ { a } ^ { \mathrm { o p T - I R } }$ $( r _ { a } ^ { 2 } , { \bf r } _ { - a } )$ . Therefore, $\Theta _ { a } ^ { \mathrm { o p T - I R } } ( \cdot , \mathbf { r } _ { - a } )$ is a nondecreasing function of its argument for all a. <sup>□</sup>

Although Theorem 1 presents an optimal mechanism, our application context also requires us to implement the mechanism in real time. We now turn our attention to implementation issues.

## 4.1. Implementing the Optimal Allocation

Notice that the optimization problem that appears in the definition of $\hat { \mathbf { I I } } ^ { \mathrm { o p r - I R } } ( \mathbf { r } )$ is identical to problem $( \mathrm { P } ^ { \mathrm { E F F } } )$ with the change that $r _ { a }$ is replaced by $\psi _ { a } ( \boldsymbol { r } _ { a } )$ for all $a \in { \mathcal { A } }$ . Consequently, using the VCG allocation specified in (5), $\Pi ^ { \mathrm { o { \hat { P } } T ^ { - } I R } } ( \mathbf { r } )$ can be computed as follows:

$$
\pi_ {n} ^ {\mathrm{OPT-IR}} (\mathbf {r}) = \underset {a \in \mathcal {A} ^ {+}} {\arg \max} \bigl \{\psi_ {a} (r _ {a}) p _ {a, n} + \lambda \bigl (1 - p _ {a, n} \bigr) \hat {R} (n + 1; \mathbf {r}) \bigr \};
$$

$$
1 \leq n \leq N, \mathrm{where}\tag{8}
$$

$$
\hat {R} (n; \mathbf {r}) := \max _ {a \in \mathscr {A} ^ {+}} \left\{\psi_ {a} \left(r _ {a}\right) p _ {a, n} + \lambda \left(1 - p _ {a, n}\right) \hat {R} (n + 1; \mathbf {r}) \right\};
$$

$$
1 \leq n \leq N, \hat {R} (N + 1; \mathbf {r}) := 0.\tag{9}
$$

The dynamic program (8) can be efficiently solved (specifically, in time $ { \mathbb { O } } ( A N ) )$ , thus making the optimal mechanism amenable to real-time bidding. Note that, unlike sponsored-search auctions, it is possible for an ad to appear in multiple (time) slots in the sequence decided by the mechanism.

Whereas the optimal allocation rule $\Pi ^ { \mathrm { O P T - I R } } ( \mathbf { r } )$ can be easily computed, the optimal payment rule $\mathbf { M } ^ { \mathrm { o P T - I R } } ( \mathbf { r } )$ is difficult to evaluate. We explain and address this challenge below, and also discuss CPC and CPM implementations.

## 4.2. Implementing the Optimal Payment

Recall from (1) that $\Theta _ { a } ^ { \mathrm { o p r - I R } } ( \mathbf { r } )$ denotes the click probability of ad a across all slots when all advertisers bid truthfully, under the optimal mechanism. Therefore, the first term in the optimal payment rule $( r _ { a } \Theta _ { a } ^ { \mathrm { o p r - I R } } ( \mathbf { r } ) )$ can be easily computed by using the optimal ad sequence obtained from (8) in the expression for $\Theta _ { a } ^ { \mathrm { o p r - I R } } ( \mathbf { r } )$

in (1). However, the second term in the payment rule $( \int _ { 0 } ^ { \dot { r _ { a } } } \dot { \Theta } _ { a } ^ { \mathrm { o p r - I R } } ( t _ { a } , { \bf r } _ { - a } ) d t _ { a } )$ involves computing $\mathbf { \Theta } \Theta _ { a } ^ { \mathrm { { o p T - I R } } } ( t _ { a } , \mathbf { r } _ { - a } )$ for all possible bids $t _ { a }$ (ranging from 0 to $r _ { a } )$ of a. We now discuss the difficulty in computing this term.

For advertiser $a \in \mathcal A$ , as the bid $t _ { a }$ changes from $0 \mathrm { t o } r _ { a } ,$ both the sequence of ads displayed in the N slots as well as the subset of slots assigned to advertiser a can change several times. Furthermore, there is no characterization of when the sequence of ads changes. Thus, the only way to (approximately) evaluate this integral is to discretize the range $[ 0 , \dot { r } _ { a } ]$ using a sufficiently small step size, say, $\Delta > 0 ,$ , and recompute the optimal sequence $r _ { a } / \Delta$ times, each time using the dynamic program (8). Clearly, this is computationally expensive because the step size Δ needs to be sufficiently small to ensure a reasonably close approximation. Furthermore, such a calculation is needed fo each advertiser $a \in { \mathcal { A } } .$ . We now use a simple example to illustrate the change in the sequence of ads as the bid $t _ { a }$ of advertiser a changes from 0 to $r _ { a } .$

Consider two ads, X and Y, and three time slots $( N = 3 )$ . The valuation per click of the two ads along with their click probabilities in the three time slots are as shown in Table 2 below. Let $\lambda = 0 . 9$

To compute the payment for advertiser $X ,$ we need to evaluate $( \int _ { 0 } ^ { 0 . 7 0 } \bar { \Theta } _ { X } ^ { \mathrm { o p r - I R } } ( t _ { X } , 0 . 6 0 ) d t _ { X } )$ . Table 3 shows the bid values for which the optimal sequence of ads changes (and, therefore, the value of the integrand $\Theta _ { X } ^ { \mathrm { o p r - i R } } ( t _ { X } , 0 . 6 0 )$ also changes).

To address this challenge, we introduce a novel idea of a randomized payment rule that yields the same expected revenue as the payment rule of the - mechanism.

4.2.1. Real-Time Implementation via Randomization. Typically, advertisers bid on tens of thousands of impressions per day and thus interact with an ad exchange on a repeated basis (Mansour et al. 2012). This motivates us to develop a randomized payment rule that can be efficiently implemented. For advertiser $a ,$ notice that

$$
\begin{array}{r} \int_ {0} ^ {r _ {a}} \Theta_ {a} ^ {\mathrm{OPT-IR}} (t _ {a}, \mathbf {r} _ {- a}) d t _ {a} = r _ {a} \int_ {0} ^ {r _ {a}} \Theta_ {a} ^ {\mathrm{OPT-IR}} (t _ {a}, \mathbf {r} _ {- a}) \frac {1}{r _ {a}} d t _ {a} \\ = r _ {a} \mathbb {E} _ {u _ {a}} \big [ \Theta_ {a} ^ {\mathrm{OPT-IR}} (u _ {a}, \mathbf {r} _ {- a}) \big ], \end{array}
$$

wher $\underline { { \boldsymbol { \mathsf { \Pi } } } } ^ { 6 } \ u _ { a } \sim U ( 0 , r _ { a } )$

Table 2. Parameter Values for Ads X and Y

<table><tr><td></td><td>Valuation per click</td><td>Click probability in time slot 1</td><td>Click probability in time slot 2</td><td>Click probability in time slot 3</td></tr><tr><td>Ad X</td><td>0.70</td><td>0.05</td><td>0.0169</td><td>0.0057</td></tr><tr><td>Ad Y</td><td>0.60</td><td>0.01</td><td>0.0092</td><td>0.0085</td></tr></table>

Let

$$
\begin{array}{c} M _ {a} ^ {\text {RAND}} (\mathbf {r}) = r _ {a} \Theta_ {a} ^ {\text {OPT - IR}} (\mathbf {r}) - r _ {a} \Theta_ {a} ^ {\text {OPT - IR}} (u _ {a}, \mathbf {r} _ {- a}), \\ \text {where} \quad u _ {a} \sim U (0, r _ {a}) \forall a \in \mathcal {A}. \end{array}
$$

Then, $\mathbb { E } _ { u _ { a } } \big [ M _ { a } ^ { \scriptscriptstyle \mathrm { R A N D } } ( { \bf r } ) \big ] = M _ { a } ^ { \scriptscriptstyle \mathrm { O P T } - \scriptscriptstyle \mathrm { I R } } ( { \bf r } )$ . This and the fact that the mechanism $( \bar { \mathbf { I I } ^ { \mathrm { O P T - I R } } } , \mathbf { M } ^ { \mathrm { o P T - I R } } )$ is IC implies that the mechanism $( \mathbf { I I } ^ { \mathrm { o p T - I R } } , \mathbf { M } ^ { \mathrm { R A N D } } )$ is IC too. Furthermore, because the optimal allocation function is monotone and $u _ { a } \leq r _ { a } ,$ we have $r _ { a } \Theta _ { a } ^ { \mathrm { o p T - I R } } ( \mathbf { r } ) \geq r _ { a } \Theta _ { a } ^ { \mathrm { o p T - I R } } ( u _ { a } , \mathbf { r } _ { - a } ) .$ , which implies that the mechanism $( \mathbf { I I } ^ { \mathrm { o p T - I R } } , \mathbf { M } ^ { \mathrm { R A N D } } )$ is IR. Thus, the mechanism $( \mathbf { I I } ^ { \mathrm { o p T - I R } } , \mathbf { M } ^ { \mathrm { R A N D } } )$ is also optimal.

We now discuss the implemention of the optimal payment rule ${ \bf M } ^ { \mathrm { R A N D } }$ in a manner that is consistent with the two dominant payment paradigms in digital advertising—CPM and CPC. For a traditional digitaladvertising auction, where a single impression is sold to a single advertiser, the CPM model requires the winning advertiser to pay for the impression regardless of whether it is clicked on or not. The CPC model, on the other hand, requires the winning advertiser to pay for the impression only if it is clicked on. The CPM model accounts for 35% of the ad revenue in display ads, whereas CPC accounts for 64% (Interactive Advertising Bureau 2017).

4.2.2. A CPC Implementation. The randomized payment rule ${ \bf M } ^ { \mathrm { R A N D } }$ can be implemented in a CPC-like manner by requiring an advertiser to pay only if the user clicks on that advertiser’s ad. Specifically, if the user clicks on ad a, then advertiser a is required to pay $\frac { M _ { a } ^ { \mathrm { R A N D } } ( \mathbf { r } ) } { \Theta _ { a } ^ { \mathrm { o p T } ^ { - _ { \mathrm { I R } } } } ( \mathbf { r } ) } .$ . This guarantees that the expected payment from any advertiser a (where the expectation is taken with respect to the randomness in whether the user clicks on the ad) is exactly $M _ { a } ^ { \mathrm { R A N D } } ( \mathbf { r } )$ . Thus, the allocation rule $\Pi ^ { \mathrm { o P T - I R } }$ along with this CPC payment rule also forms an optimal mechanism that is implementable in real time.

4.2.3. A CPM Implementation. A CPM-style implementation of the randomized payment scheme is to require an advertiser to pay for the display of his ad, regardless of whether the user clicks on the ad; the advertiser is not charged if his ad is not displayed. Here, it is important to highlight the difference with respect to CPM payments in the traditional auction. In the latter, only one advertiser wins the entire impression; thus, the winning advertiser is guaranteed that his ad will be displayed for the entire duration of the impression. In contrast, in our context, multiple advertisers might be required to pay the ad exchange, and, with the exception of the advertiser whose ad is displayed in the first slot, the advertisers receive no guarantee that their ads will be shown to the user; this is because the impression might end before an advertiser’s turn (i.e., slot) to have his ad displayed arrives.

This motivates the following slot-by-slot CPM-style implementation of the randomized payment rule $\mathbf { M } ^ { \mathrm { R A N D } }$ . Let $\{ a  n \}$ denote the event that ad a is displayed in slot n. Consider the payment scheme in which, if slot n materializes (that is, the impression survives until slot n), then advertiser a is required to pay $\frac { M _ { a } ^ { \mathrm { R A N D } } ( \mathbf { r } ) \cdot \mathbb { I } \{ a \to n \} } { \sum _ { t } \mathrm { P r o b } \{ a \to t \} }$ for that slot, where $\operatorname { P r o b } \{ a  t \}$ is the probability that ad a is displayed in slot t. This probability can be easily obtained from (1). Thus, the expected payment from any advertiser a over all slots (where the expectation is taken with respect to the randomness in whether the slot(s) assigned to this advertiser materialize) is exactly $M _ { a } ^ { \mathrm { R A N D } } ( \mathbf { r } )$ . Thus, the allocation rule $\Pi ^ { \mathrm { O P T - I R } } ( \mathbf { r } )$ along with this CPM payment rule forms an optimal mechanism.

Remark 1 (Alternate Allocation Rule). <sub>The allocation rule</sub> we formulated in Section 3.1 can be alternatively viewed as a mapping from the bid space to a probability simplex over the set of all possible sequences. Mathematically, $\Pi ^ { \mathrm { A L T } } : { \mathcal { B } }  [ 0 , 1 ] ^ { S } ,$ , where $S = { \overset { \cdot } { (} } A + 1 ) ^ { N }$ is the number of possible ad sequences (including null allocations). It can be shown using standard arguments that this alternate formulation yields the same optimal solution as that in Theorem 1.

<sub>Remark 2</sub> (Infinite-Horizon Mechanisms)<sub>. While formu-</sub> lating our mechanism-design problem in Section 3.1, we assumed that the number of time slots, N (which denotes the time the user stays on the app until he either leaves the app or clicks on an ad), is a sufficiently large integer. Technically, if the user neither leaves the app nor clicks on an ad, then our context requires us to consider infinite-horizon mechanisms. To show that it is sufficient to restrict attention to finite-horizon mechanisms, we establish that the loss in revenue to the ad exchange by restricting attention to finite-horizon mechanisms instead of infinite-horizon mechanisms can be made arbitrarily small. A proof of this claim is provided in Online Appendix B.

Table 3. Optimal Sequence of Ads for Different Bids of Ad X

<table><tr><td>Bid of ad  $X$  ( $t_X$ )</td><td>Ad in time slot 1</td><td>Ad in time slot 2</td><td>Ad in time slot 3</td></tr><tr><td>0.00</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>0.53</td><td>X</td><td>Y</td><td>Y</td></tr><tr><td>0.56</td><td>X</td><td>X</td><td>Y</td></tr><tr><td>0.65</td><td>X</td><td>X</td><td>X</td></tr></table>

## 5. A Sequential Mechanism

As discussed in Section 1, the allocative inefficiency in the traditional mechanism results from the difference in the way the expected valuations of ads change with time during an app session—ads that are more attractive for display in the initial time slots might become less attractive in the later time slots. A natural mechanism that comes to mind for addressing this allocative inefficiency is one that conducts an auction in each time slot, that is, a mechanism that treats an impression with N potential time slots as N potential impressions and sequentially auctions each time slot independently to the advertisers. We will refer to such a mechanism as an SEQ mechanism. For a given slot $n , n \in \{ 1 , 2 , \ldots , N \}$ , the optimal SEQ mechanism in that slot is defined by its allocation rule $\pi _ { n } ^ { \mathrm { s e } }$ (ad served in time slot n) and payment rule $M _ { a , n } ^ { \mathrm { s e q } }$ (amount paid by advertiser a to the ad exchange in time slot n). We further discuss this mechanism below.

Consider time slot 1. The expected value of the partitioned impression in time slot 1 to advertiser $a , a \in { \mathcal { A } } ,$ is $r _ { a } p _ { a , 1 } ,$ where $p _ { a , 1 }$ denotes the click probability of ad a in time slot 1. Recall that the click probabilities of the ads in this time slot are known to the ad exchange and only the valuation per click of each advertiser is private to the respective advertiser. Therefore, instead of soliciting bids for the advertisers’ expected valuations $\boldsymbol { r } _ { a } p _ { a , 1 } , a \in \mathcal { A } _ { \cdot }$ , it suffices for the ad exchange to solicit their valuations per click, $\boldsymbol { r } _ { a } , a \in \mathcal { A }$ . From the theory of the classical single-unit auction (Myerson 1981), we know that there exists an optimal mechanism that is incentive compatible and individually rational, and, furthermore, this mechanism will serve ad arg $\mathfrak { m a x } _ { a \in \mathcal { A } ^ { + } } \{ \psi _ { a } ( r _ { a } ) p _ { a , 1 } \}$ in time slot 1, where $\psi _ { a } ( \boldsymbol { r } _ { a } )$ denotes the virtual bid of advertiser a. The winning advertiser in this slot will be charged the minimum amount necessary to outbid all the other advertisers.

The session progresses to time slot 2 only if the app user does not click on the ad shown in time slot 1 and decides not to leave the app session. Conditional on the existence of time slot 2, the optimal SEQ mechanism then selects the best ad for this slot, which is ad arg $\mathrm { m a x } _ { a \in \mathcal { A } ^ { + } } \{ \psi _ { a } ( r _ { a } ) p _ { a , 2 } \}$ . The winning advertiser in slot 2 pays the minimum amount necessary to outbid all the other advertisers. Repeating this argument for the N time slots, the (optimal) SEQ mechanism is defined as follows:

$$
\pi_ {n} ^ {\mathrm{SEQ}} (\mathbf {r}) = \underset {a \in \mathcal {A} ^ {+}} {\arg \max} \bigl \{\psi_ {a} (r _ {a}) p _ {a, n} \bigr \}, n = 1, 2, \ldots , N,\tag{10}
$$

$$
M _ {a, n} ^ {\mathrm{SEQ}} (\mathbf {r}) = r _ {a} p _ {a, n} \mathbb {1} \left\{\pi_ {n} ^ {\mathrm{SEQ}} (\mathbf {r}) = a \right\}
$$

$$
- \int_ {0} ^ {r _ {a}} p _ {a, n} \mathbb {1} \left\{\pi_ {n} ^ {\text { SEQ }} \left(t _ {a}, \mathbf {r} _ {- a}\right) = a \right\} d t _ {a}.\tag{11}
$$

The SEQ mechanism defined by (10) and (11) is derived using the same steps we used to derive the OPT-IR mechanism in Online Appendix A. Notice that when $N = 1$ , the OPT-IR mechanism and the SEQ mechanism solve the same single-slot revenue-maximization problem of allocating the ad that maximizes the expected revenue. It is then straightforward to see that the allocation rule (10) and the payment rule (11) of the SEQ mechanism in a particular time slot $n , n \in$ $1 , 2 , \ldots , N ,$ , can be obtained, respectively, from the allocation rule (6) and the payment rule (7) of the OPT-IR mechanism.

Although the SEQ mechanism conducts multiple auctions, one for each time slot, and selects an ad in each time slot, each of these auctions is structurally similar to the traditional mechanism (used by present-day ad exchanges) that selects an ad for the entire session. Thus, the SEQ mechanism does not require any changes to the current technology infrastructure of the ad exchange and is, consequently, easy to implement. Furthermore, because the allocation and payment rules of the SEQ mechanism are also structurally similar to those of the traditional mechanism, it would also be easy for advertisers to accommodate these rules into their bidding strategy However, the expected revenue of the ad exchange under the SEQ mechanism can be significantly lower than that under the optimal (i.e., OPT-IR) mechanism The basic reason behind this drawback is as follows: Although this mechanism myopically selects the “best” ad for display in the current time slot, it disregards the impact (on the ad exchange’s expected revenue) from the ads that could be shown in future time slots. Nevertheless, the SEQ mechanism is attractive to practitioners because of its simplicity. Thus, it would be useful to delve deeper into the comparison of the performance of the SEQ mechanism with that of the - mechanism. We do this next.

## 6. SEQ Mechanism vs. OPT-IR Mechanism

We begin our discussion by illustrating the inferior performance of the SEQ mechanism via a simple example consisting of two ads and two time slots. Throughout this section, for expositional simplicity, we consider the special case where the distribution of the valuation per click of the ads is a point distribution; thus, the valuation per click of each ad is known to the ad exchange.

Example 1. $\operatorname { L e t } \mathcal { A } = \{ X , Y \}$ be the set of advertisers and $N = 2$ (the number of time slots). Let $r _ { X }$ and $r _ { Y }$ denote the valuation per click of advertisers X and $\boldsymbol { Y } ,$ respectively. Let $\begin{array} { r } { r _ { X } = r _ { Y } \epsilon + \gamma _ { \mathrm { . } } } \end{array}$ , where $\epsilon , \gamma > 0 , \epsilon ^ { 2 } \approx 0 .$ , and $\gamma \approx 0$ . The click probabilities of the two ads in the two time slots are as follows: $p _ { X , 1 } = 1 , p _ { X , 2 } = 0$ and $p _ { Y , 1 } = p _ { Y , 2 } = \epsilon .$ Finally, let $\lambda = 1$ . In time slot 1, $r _ { X } \cdot 1 = r _ { Y } \epsilon + \gamma > r _ { Y } \epsilon .$

Therefore, the SEQ mechanism selects ad X for display in that slot. Once ad X is displayed in slot 1, the user clicks on that ad (because $p _ { X , 1 } = 1 )$ and the app session ends. Thus, the revenue to the ad exchange under the SEQ mechanism is simply $r _ { X } \cdot 1 = r _ { Y } \epsilon + \gamma \approx r _ { Y } \epsilon .$ Using (6), it is straightforward to see that the OPT-IR mechanism selects ad Y for display in both the time slots. Thus, the revenue to the ad exchange under the OPT-IR mechanism is $r _ { Y } \epsilon + ( 1 - \epsilon ) r _ { Y } \epsilon \approx 2 r _ { Y } \epsilon$ . Thus, the ratio of the ad exchange’s revenue under the OPT-IR mechanism to that under the SEQ mechanism can be made arbitrarily close to 2.

In Example 1, we observe that the valuation per click of ad Y is higher than that of ad X, whereas the click probability of ad Y in the first time slot is lower than that of ad X in the first time slot. This observation suggests that the ordering of the valuation per click of advertisers and the click probability of their ads might be associated with the inferior performance of the SEQ mechanism. Before we examine this line of inquiry, it is convenient, for expositional simplicity, to define the following notion of negative correlation: When we say that the valuation per click of the advertisers and the click probability of their ads in the first time slot are negatively correlated, we mean that the advertisers and their ads can be indexed such that

$$
\begin{array}{c} r _ {1} \geq r _ {2} \geq \ldots \geq r _ {A}, \\ p _ {1, 1} \leq p _ {2, 1} \leq \ldots \leq p _ {A, 1}. \end{array}
$$

We begin by providing an illustrative example in which we observe that the notion of negative correlation by itself is not sufficient to guarantee the suboptimality of the SEQ mechanism; that is, it is possible for the SEQ mechanism to be optimal when the valuation per click of the advertisers and the click probability of their ads in the first time slot are negatively correlated.

## 6.1. Illustrative Example 2

Example 2. Let ${ \mathcal { A } } = \{ X , Y \}$ be the set of advertisers and $N = 2 .$ Let $r _ { X }$ (respectively, r ) denote the valuation per click of advertiser X (respectively, Y). Let $\lambda = 1$ . The valuation per click and the click probabilities of each ad are shown in Table 4. Note that $r _ { X } > r _ { Y }$ and $p _ { X , 1 } < p _ { Y , 1 }$ Thus, the valuation per click of the advertisers and the click probability of their ads in the first time slot are negatively correlated.

For the above choice of parameters, the SEQ mechanism as well as the optimal (i.e., OPT-IR) mechanism selects ad X in time slot 1 and ad Y in time slot 2. Consequently, both the mechanisms yield a revenue of \$0.282 to the ad exchange.

Next, we obtain conditions that guarantee the suboptimality of the SEQ mechanism.

## 6.2. Suboptimality of the SEQ Mechanism

Let $\mathcal { A } = \{ X , Y \}$ denote the set of advertisers. Let the click probability of each ad decay at a constant rate δ with the passage of time, that is, $p _ { a , n + 1 } = \delta p _ { a , n }$ for all $a \in { \mathcal { A } }$ and $n \geq 1 .$ . Thus, under this constant decay-rate structure, the click probability of an ad in any time slot is determined by its click probability in the first slot and the decay rate. Let $\hat { \lambda } = 1$ . Let $\begin{array} { r } { \dot { \Delta } ( \mathbf { r } ) : = \frac { r _ { X } p _ { X , 1 } - r _ { Y } p _ { Y , 1 } } { p _ { X , 1 } - p _ { Y , 1 } } , } \end{array}$ and define a “value function ${ \bf \Omega } ^ { \prime \prime } \ : \ : W ( n ; { \bf r } )$ recursively as follows:

$$
\begin{array}{c} W (n; \mathbf {r}) := r _ {X} \cdot p _ {X, n} + \left(1 - p _ {X, n}\right) \cdot W (n + 1; \mathbf {r}); \\ 1 \leq n \leq N, W (N + 1; \mathbf {r}) = 0. \end{array}
$$

That is, $W ( n ; { \mathbf { r } } )$ denotes the revenue obtained from period n onward by displaying ad X in each time slot. Then, we have the following theorem.

Theorem 2. If $r _ { Y } > r _ { X } , \ p _ { X , 1 } > p _ { Y , 1 } , \ r _ { X } p _ { X , 1 } > r _ { Y } p _ { Y , 1 } $ , and $W ( K ; { \mathbf { r } } ) > \Delta ( { \mathbf { r } } ) \ge W ( K + 1 ; { \mathbf { r } } )$ for some $K \in \{ 2 , 3 , . . . , N - 1 \}$ }, then the revenue to the ad exchange under the OPT-IR mechanism is strictly greater than that under the SEQ mechanism

A proof of Theorem 2 is provided in Online $\mathrm { A p \cdot }$ pendix C. This result states that along with the negative correlation between the valuation per click of the advertisers and the click probability of their ads in the first time slot, certain additional conditions on the problem parameters are required to guarantee the suboptimality of the SEQ mechanism. Broadly speaking, under these conditions, the SEQ mechanism selects a single ad for display in all the time slots, whereas the OPT-IR mechanism selects two ads and displays the first ad for a certain number of initial time slots and the second ad for the remaining time slots.

We now supplement Theorem 2 by providing a numerical example to demonstrate that the conditions in that result can indeed be achieved by the problem parameters. Consider the values of the parameters in Table 5. For these parameters, we have $\Delta ( { \bf r } ) = 0 . 0 7 5 .$ The values of $W ( \cdot ; { \bar { \mathbf { r } } } )$ are shown in Table 6. Thus, we have $W ( 3 ; { \bf r } ) > \Delta ( { \bf r } ) > W ( 4 ; { \bf r } )$ and, consequently, $K = 3$ in the statement of Theorem 2. The SEQ mechanism shows ad X in each time slot and yields a revenue of \$0.260 to the ad exchange. On the other hand, the OPT-IR mechanism shows ad Y in the first two time slots and ad X in each of the remaining eight slots, and yields a revenue of \$0.298 to the ad exchange.

The conditions in Theorem 2 that guarantee the suboptimality of the SEQ mechanism is only sufficient and not necessary. We now demonstrate this via an illustrative example in which, although the valuation per click of two advertisers and the click probability of their ads in the first time slot are not negatively correlated, the SEQ mechanism is suboptimal.

Table 4. Parameter Values for Example 2

<table><tr><td rowspan="2">Ad</td><td rowspan="2">Valuation per click</td><td colspan="2">Click probabilities</td></tr><tr><td>1</td><td>2</td></tr><tr><td>X</td><td>0.551</td><td>0.354</td><td>0.185</td></tr><tr><td>Y</td><td>0.212</td><td>0.708</td><td>0.636</td></tr></table>

Table 5. Parameter Values for the Illustrative Example used to Demonstrate that the Result in Theorem 2 can be achieved by the Problem Parameters

<table><tr><td>N</td><td>$ r_{X} $</td><td>$ r_{Y} $</td><td>$ p_{X,1} $</td><td>$ p_{Y,1} $</td><td>$ \delta $</td></tr><tr><td>10</td><td>0.3</td><td>0.6</td><td>0.7</td><td>0.3</td><td>0.5</td></tr></table>

## 6.3. Illustrative Example 3

Example 3. Consider two ads X and Y and 10 time slots $( N = 1 0 )$ . The click probabilities of the ads follow a constant decay-rate structure; that $\mathbf { i s } , p _ { a , n + 1 } = \delta _ { a } p _ { a , n } , a$ ∈ $\{ X , Y \}$ and $n \geq 1$ . The valuation per click, the click probability in the first time slot, and the decay rate of each ad are shown in Table 7. Let $\lambda = 1$ . Note that, we have $r _ { X } > r _ { Y }$ and $p _ { X , 1 } > p _ { Y , 1 }$

For the above choice of parameter values, the OPT-IR mechanism allocates ad X in the first four time slots and ad Y in the remaining six slots, and yields a revenue of \$0.884. On the other hand, the SEQ mechanism allocates ad X in the first time slot and ad Y in the remaining nine slots and yields a revenue of \$0.839, which is about 5% below the optimal revenue.

Although negative correlation, along with certain additional conditions, guarantees the suboptimality of the SEQ mechanism, a natural question arises: When is the SEQ mechanism optimal? The following result establishes a sufficient condition.

## 6.4. Optimality of the SEQ Mechanism

Theorem 3. If $r _ { 1 } \ge r _ { 2 } \ge . . . \ge r _ { A }$ and $p _ { 1 , n } \ge p _ { 2 , n } \ge . . . p _ { A , n }$ for all $n \in \{ 1 , 2 , \ldots , N \}$ , then the SEQ mechanism is an optimal mechanism (i.e., an optimal solution to Problem $( \mathrm { P } ^ { \mathrm { I R } } ) )$

Theorem 3 states that if ads with a higher valuation per click have a higher click probability in each time slot, then the SEQ mechanism is optimal. A proof is provided in Online Appendix D.

Given these developments, it should be clear that a complete characterization of the conditions under which the SEQ mechanism is optimal (or suboptimal) is difficult to obtain. In light of this, we now conduct a focused numerical experiment to assess the impact of the extent of negative correlation on the performance of the SEQ mechanism relative to that of the OPT-IR mechanism. The main message here is that as the extent of negative correlation between the valuation per click of the advertisers and the click probability of their ads in the first time slot decreases, the impact of the myopia of the SEQ mechanism decreases, and its performance moves closer to optimality.

Table 6. Value of $W ( \cdots \mathbf { r } )$ for Different Time Slots

<table><tr><td>W(1;r)</td><td>W(2;r)</td><td>W(3;r)</td><td>W(4;r)</td><td>...</td><td>W(10;r)</td></tr><tr><td>0.260</td><td>0.165</td><td>0.093</td><td>0.049</td><td>...</td><td>0.001</td></tr></table>

Table 7. Parameter Values for Example 3

<table><tr><td>Ad</td><td>Valuation per click</td><td>Click probability in slot 1</td><td>Decay rate</td></tr><tr><td>X</td><td>0.976</td><td>0.488</td><td>0.545</td></tr><tr><td>Y</td><td>0.724</td><td>0.362</td><td>0.991</td></tr></table>

## 6.5. Numerical Analysis

Our setting is as follows: Let $\mathcal { A } = \{ 1 , 2 , \ldots , 1 0 \}$ denote the set of advertisers, and let N, the number of time slots, be equal to 10. For $a \in \mathcal A _ { \varepsilon }$ , the valuation $r _ { a }$ of ad a is given by $r _ { a } = 0 . 5 - \alpha ( 5 - a ) _ { . }$ , where the parameter α 0, 0.1 is the relative difference between the valuation per clicks of two consecutively indexed advertisers (see Figure 2(a)). Notice that a higher-indexed ad has a higher valuation per click than a lower-indexed ad. Let the click probability of ad a ! decay at adspecific rate $\delta _ { a }$ with the passage of time; that is, $p _ { a , n + 1 } =$ $\delta _ { a } p _ { a , n }$ for all a ! and $n \geq 1 .$ . Let the click probability of ad $a , a \in \mathcal { A } ,$ in time slot $1 , p _ { a , 1 } .$ , be $p _ { a , 1 } = 0 . 5 - \beta ( 6 - a ) .$ where the parameter $\beta \in \left[ - 0 . 1 , 0 \right]$ is the relative difference between the click probabilities of two consecutively indexed ads in the first time slot (see Figure 2(b)). Thus, lower-indexed ads have a higher click probability in the first time slot compared with higher-indexed ads. Let $\lambda = 1$ . The decay rate $\delta _ { a }$ of ad a is chosen randomly from a uniform distribution $U ( 0 , 1 )$ . For this choice of parameters, we compute the ratio of the expected revenue to the ad exchange under the SEQ mechanism to the expected revenue to the ad exchange under the OPT-IR mechanism, using the sample average over 1,000,000 instances.

Table 8 shows the performance of the SEQ mechanism relative to the OPT-IR mechanism for different values of the parameters α and $\beta .$ When $\alpha = \beta = 0 ,$ , all the ads have the same valuation per click and click probability in the first time slot. In this case, it is easy to verify that the SEQ mechanism is optimal and, hence, the ratio of the expected revenue of the SEQ mechanism to that of the OPT-IR mechanism is 1. As α increases and $\beta$ decreases, the lower-indexed ads have increasingly lower valuation per click and increasingly higher click probability in the first time slot compared with the higher-indexed ads; that is, the extent of negative correlation among the ads increases, and consequently, the performance of the SEQ mechanism deteriorates.

We now move our attention to current practice.

Figure 2. (Color online) The Relative Ordering of (a) the Valuation per Click of the Ads for Different Values of the Parameter α and (b) the Click Probability of the Ads in Time Slot 1 for Different Values of the Parameter $\beta$

(a)  
![](/api/attachments/9S5WHDE3/fulltext/images/80233d86e4a3e7e564b4acc8b57f9ca1f335a76b099230168444db4a54315245.jpg)  
(b)

## 7. The Traditional (BASE) Mechanism

As mentioned earlier, the major mobile ad exchanges of today use the following mechanism to sell an impression: valuation-per-click bids are solicited from the advertisers in a real-time auction, and the winner gets the impression; that is, the winner’s ad is served on the impression throughout its lifetime. We will refer to this traditional mechanism as the BASE mechanism.

The problem of obtaining an optimal (i.e., revenuemaximizing) BASE mechanism for the ad exchange can be viewed as a constrained version of the problem we formulated in Section 3.1, with the additional constraint that the same ad be displayed in all the time slots. Thus, the optimization problem can be formulated as follows:

$$
\begin{array}{r l} & {\underset {\mu} {\max} \left\{\sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \Big [ m _ {a} ^ {\mu} (r _ {a}) \Big ] \right\}} \\ & {\quad \mathrm{s.t.} (\mathrm{IC}), (\mathrm{IR}),} \\ & {\qquad \pi_ {1} ^ {\mu} (\mathbf {r}) = \pi_ {2} ^ {\mu} (\mathbf {r}) = \ldots = \pi_ {N} ^ {\mu} (\mathbf {r}).} \end{array}
$$

(<sup>P</sup> )

(12)

Using steps similar to those in Section 4 to solve Problem $( \bar { \mathrm { P } } ^ { \mathrm { I R } } )$ , the solution to Problem $( \mathrm { P ^ { \mathrm { B A S E } } } )$ is as follows:

$$
\begin{array}{l} \Pi^ {\text { BASE }} (\mathbf {r}) = \arg \max _ {\mu} \left\{\sum_ {a = 1} ^ {A} \psi_ {a} (r _ {a}) \Theta_ {a} ^ {\mu} (\mathbf {r}) \right\} \text {   s.t.   (12) }, \\ M _ {a} ^ {\text { BASE }} (\mathbf {r}) = r _ {a} \Theta_ {a} ^ {\text { BASE }} (\mathbf {r}) - \int_ {0} ^ {r _ {a}} \Theta_ {a} ^ {\text { BASE }} (t _ {a}, \mathbf {r} _ {- a}) d t _ {a} \forall a \in \mathscr {A}. \end{array}
$$

This mechanism can be simplified, using steps presented in Online Appendix ${ \bar { \mathrm { E } } } ,$ to yield

$$
\begin{array}{c} \pi_ {n} ^ {\text { BASE}} (\mathbf {r}) = \underset {a \in \mathcal {A} ^ {+}} {\arg \max} \left\{\psi_ {a} (r _ {a}) \sum_ {n = 1} ^ {N} p _ {a, n} \lambda^ {n - 1} \prod_ {t = 1} ^ {n - 1} (1 - p _ {a, t}) \right\}, \\ n = 1, 2, \ldots , N, \\ M _ {a} ^ {\text { BASE}} (\mathbf {r}) = \Theta_ {a} ^ {\text { BASE}} (\mathbf {r}) \cdot y _ {a} ^ {\text { BASE}} (\mathbf {r} _ {- a})   \forall a \in \mathcal {A}, \end{array}
$$

![](/api/attachments/9S5WHDE3/fulltext/images/33f47b17670fab6483afffbeaaa5607c0d3344dc327c316ab0d39f6023d09547.jpg)  
Click probability in time slot 1

where $y _ { a } ^ { \scriptscriptstyle \mathrm { B A S E } } ( { \bf r } _ { - a } ) = \operatorname* { i n f } \{ t _ { a } : \psi _ { a } ( t _ { a } ) \geq 0$ and for all $j$ not equal to $\bar { a } , \psi _ { a } ( t _ { a } ) \cdot \Theta _ { a } ^ { \scriptscriptstyle \mathrm { B A S E } } ( t _ { a } , { \bf r } _ { - a } ) \geq \psi _ { j } ( r _ { j } ) \Theta _ { j } ^ { \scriptscriptstyle \mathrm { B A S E } } ( t _ { a } , { \bf r } _ { - a } ) \}$ . In words, $y _ { a } ^ { \scriptscriptstyle \mathrm { B A S E } } ( { \bf r } _ { - a } )$ denotes the smallest bid that advertiser a has to make to win against the bid vector $\mathbf { r } _ { - a } .$ Thus, we have the following theorem.

Theorem 4. The mechanism $\left( \mathbf { I I ^ { \mathrm { B A S E } } } , \mathbf { M ^ { \mathrm { B A S E } } } \right)$ is an optimal solution to Problem $( \mathrm { P ^ { \mathrm { B A S E } } } )$

The optimal BASE mechanism allocates the impression to the highest bidder contingent on his virtual bid being nonnegative, and charges the winner the minimum amount necessary to outbid all the other advertisers.

Our next task is to compare the OPT-IR mechanism with the BASE mechanism.

## 8. - Mechanism vs. Mechanism: Impact on Stakeholders

Because the BASE mechanism is a feasible solution to the mechanism-design problem formulated in Section 3.1,

Table 8. Impact of the Parameters α and $\beta$ on the Performance of the Mechanism Relative to the - Mechanism

<table><tr><td>α</td><td>β</td><td>REVENUE(SEQ) REVENUE(OPT-IR) (%)</td></tr><tr><td>0</td><td>0</td><td>100.0</td></tr><tr><td>0.01</td><td>-0.01</td><td>94.1</td></tr><tr><td>0.02</td><td>-0.02</td><td>89.0</td></tr><tr><td>0.03</td><td>-0.03</td><td>84.9</td></tr><tr><td>0.04</td><td>-0.04</td><td>81.6</td></tr><tr><td>0.05</td><td>-0.05</td><td>79.1</td></tr><tr><td>0.06</td><td>-0.06</td><td>77.4</td></tr><tr><td>0.07</td><td>-0.07</td><td>76.3</td></tr><tr><td>0.08</td><td>-0.08</td><td>75.7</td></tr><tr><td>0.09</td><td>-0.09</td><td>75.6</td></tr><tr><td>0.1</td><td>-0.1</td><td>75.5</td></tr></table>

Note. As the magnitudes of the parameters α and $\beta$ increase, the negative correlation between the valuation per click of the advertisers and the click probability of the ads in the first time slot increases. This increases the extent of negative correlation among the ads, and, in turn, the performance of the SEQ mechanism deteriorates.

it follows that the ad exchange always obtains a higher expected revenue from the OPT-IR mechanism than that from the BASE mechanism. However, the surplus of an advertiser can be either lower or higher under the OPT-IR mechanism compared with that under the BASE mechanism. We define a win–win scenario (signifying that both the exchange and the advertisers benefit) as one where each of the participating advertisers obtains a (weakly) higher expected utility than that under the BASE mechanism. Similarly, we define a win–lose scenario as one where at least one advertiser obtains a (strictly) lower expected utility than that under the BASE mechanism. We now demonstrate these two possibilities analytically.

## 8.1. Illustration of a Win–Win Scenario

Let ! X, Y be the set of advertisers and $N = 2$ (the number of time slots). Let $v _ { X }$ and $v _ { Y }$ denote the virtual bids of advertisers X and $\boldsymbol { Y } ,$ respectively. Without loss of generality, we assume that the valuation-per-click bids are independently drawn from U 0.5, 1 . Thus, $v _ { X } = 2 r _ { X } - 1 \sim U ( 0 , 1 )$ and $v _ { Y } = 2 r _ { Y } - 1 \sim U ( 0 , 1 )$ , where $r _ { X }$ and $r _ { Y }$ denote, respectively, the valuation-per-click bids of X and Y. Notice that the virtual bids are always nonnegative; thus, the impression is always assigned one ad in the base mechanism and at least one ad in the optimal mechanism. Recall that $p _ { a , n }$ denotes the click probability of ad a in time slot n. Let $p _ { X , 1 } = 2 p , p _ { X , 2 } = 0 ,$ and $p _ { Y , 1 } = p _ { Y , 2 } = p ,$ where $p$ is a parameter satisfying $0 < p \leq 0 . 5$ and $\dot { p } ^ { 2 } \approx 0$ . Thus, ad X represents an impulse ad (the likelihood of a click on ad X diminishes quickly), and ad Y represents a steady ad (the likelihood of click on ad Y is the same in both the time slots). For expositional simplicity, assume that the conditional probability, λ, that the user stays in a particular time slot, given that she enters that time slot, is equal to 1.

For the setting described above, we evaluate the expected utility of advertisers X and Y, the expected revenue to the ad exchange, and the expected social welfare under the BASE and the OPT-IR mechanisms. These values are succinctly summarized in Table 9; for a derivation of these results, we refer the reader to Online Appendix F. The important observation here is that both the advertisers are better off in the OPT-IR mechanism, relative to the BASE mechanism.

## 8.2. Illustration of a Win–Lose Scenario

Again, let ${ \mathcal { A } } = \{ X , Y \}$ and $N = 2$ . The valuation-perclick bid of $X , r _ { X } ,$ is drawn from U 0.75, 1 , whereas the valuation-per-click bid of $Y , \ r _ { Y } ,$ is deterministically equal to 1.5. Consequently, we have $v _ { X } = 2 r _ { X } - 1 \sim$ $U ( 0 . 5 , 1 )$ and $v _ { Y } = r _ { Y } = 1 . 5$ . Notice that, in this scenario too, the virtual bids of both the advertisers are always nonnegative. The click probabilities of the ads in the two slots are as follows: $p _ { X , 1 } = p _ { X , 2 } = 1$ and $p _ { Y , 1 } = p _ { Y , 2 } = q ,$ where q is a parameter such that $\begin{array} { r } { 0 < q \le \frac { 3 - \sqrt { 6 } } { 3 } . } \end{array}$ . Finally, $\lambda \approx 1$ . Like Table 9 for the win–win scenario, Table 10 compares the BASE and OPT-IR mechanisms for the win–lose scenario. The derivations are in Online Appendix G. Here, advertiser X is worse off in the OPT-IR mechanism.

In summary, we have identified two scenarios, one in which shifting to the OPT-IR mechanism results in a win–win for the ad exchange and the advertisers, relative to the BASE mechanism, and another in which one advertiser is worse off. The existence of these scenarios motivates us to consider mechanisms in which the benefit to both parties is guaranteed, that is, the ad exchange and the advertisers obtain, respectively, at least as much revenue and utility as in the BASE mechanism (in expectation). We refer to such mechanisms as mutually beneficial mechanisms and now examine the problem of obtaining an optimal mechanism in this class.

## 9. Setting 2: An Optimal Mutually Bene<sup>fi</sup>cial Mechanism

By definition, the BASE mechanism is mutually beneficial. Because advertisers typically bid on thousands of impressions that arrive at an ad exchange, it is reasonable to consider mechanisms in which advertisers obtain, over the long run, at least their respective utilities in the BASE mechanism (which we refer to as the BASE utility). The corresponding optimal mechanism-design problem is as follows:

$$
\begin{array}{l} \max _ {\mu} \left\{\sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \Big [ m _ {a} ^ {\mu} (r _ {a}) \Big ] \right\} \\ \text {s.t. (IC),} \end{array}\tag{\((P^{MB})\}
$$

$$
\mathbb {E} _ {r _ {a}} \left[ U _ {a} ^ {\mu} (r _ {a}) \right] \geq \mathbb {E} _ {r _ {a}} \left[ U _ {a} ^ {\text { BASE }} (r _ {a}) \right] \forall a \in \mathscr {A}.\tag{13}
$$

Table 9. Summary of the Win–Win Scenario

<table><tr><td></td><td>BASE</td><td>OPT-IR</td><td>Gain in OPT-IR (w.r.t. BASE) (%)</td></tr><tr><td>Expected utility of X</td><td> $\frac{p}{6}$ </td><td> $\frac{7p}{24}$ </td><td>+75</td></tr><tr><td>Expected utility of Y</td><td> $\frac{p}{6}$ </td><td> $\frac{7p}{24}$ </td><td>+75</td></tr><tr><td>Expected revenue of ad exchange</td><td> $\frac{4p}{3}$ </td><td> $\frac{19p}{12}$ </td><td>+18.75</td></tr><tr><td>Social welfare</td><td> $\frac{5p}{3}$ </td><td> $\frac{13p}{6}$ </td><td>+30</td></tr></table>

Note. w.r.t., With respect to.

The constraints in (13) ensure that, in the long run, each advertiser obtains at least his expected utility in the BASE mechanism. Note that Problem $( \mathrm { P ^ { M B } } )$ relaxes the constraints (IR) in Problem $( \mathrm { P ^ { \mathrm { I R } } } )$ , and instead imposes the BASE utility constraints (13). Thus, Problem $( \mathrm { P ^ { M B } } )$ is not a relaxation of Problem (P<sup>IR</sup>). Consequently, the ad exchange’s revenue under a mutually beneficial mechanism could be higher or lower than that under the OPT-IR mechanism. Before proceeding further, we remark on our formulation of Problem $( \mathrm { P ^ { M B } } )$

<sub>Remark 3</sub> (Individual Rationality for Individual Auctions)<sub>.</sub> The mechanism-design Problem $( \mathrm { P ^ { M B } } )$ that we formulated above guarantees at least the BASE utility in the long run. One could also conceive of a more constrained setting where advertisers obtain at least the BASE utility in the long run and each individual auction satisfies the individual rationality constraints (i.e., the constraints (IR) for each auction, viz., $U _ { a } ^ { \mu } ( r _ { a } ) { \dot { \geq 0 } }$ for all $a \in \mathcal A )$ for the advertisers. The mechanism-design problem for this setting can be formulated as follows:

$$
\begin{array}{l} \max _ {\mu} \left\{\sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \Big [ m _ {a} ^ {\mu} (r _ {a}) \Big ] \right\} \\ \text { s.t. } (\mathrm{IC}), (\mathrm{IR}), \\ \mathbb {E} _ {r _ {a}} \Big [ U _ {a} ^ {\mu} (r _ {a}) \Big ] \geq \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\mathrm{BASE}} (r _ {a}) \big ] \forall a \in \mathcal {A}. \end{array}\tag{\((P^{\mathrm{SIM}})\}
$$

Using the classical approach, Problem $( \mathrm { P } ^ { \mathrm { S I M } } )$ reduces to the following optimization problem:

$$
\begin{array}{l} \max _ {\mu} \left\{\mathbb {E} _ {\mathbf {r}} \bigg [ \sum_ {a = 1} ^ {A} \min \Big \{r _ {a} \Theta_ {a} ^ {\mu} (\mathbf {r}), U _ {a} ^ {\text { BASE}} (r _ {a}) \right. \\ \left. + \psi_ {a} (r _ {a}) \Theta_ {a} ^ {\mu} (\mathbf {r}) \Big \} \right] \Bigg \} - \sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\text { BASE}} (r _ {a}) \big ]. \end{array}
$$

In the optimization problem above, the first argument inside the $\operatorname* { m i n } \{ \cdot , \cdot \}$ expression can be analyzed in isolation through pointwise maximization of a dynamic program. However, the second argument is nonlinear for a given bid vector and, when combined with the first argument, renders the optimization problem difficult to solve. The study of optimal and/or approximate mechanisms for this problem can be a useful direction for future work.

We now obtain a mechanism—characterized by a pair of functions $( { \bf { I I } } ^ { \mathrm { { M B } } } , { \bf { M } } ^ { \mathrm { { M B } } } )$ —that is an optimal solution to Problem $( \mathrm { P } ^ { \mathrm { M B } } )$ . An upper bound on the objective function of Problem $( \hat { \mathrm { P } } ^ { \mathrm { M B } } )$ is easy to obtain: Because $U _ { a } ^ { \mu } ( r _ { a } ) = r _ { a } \theta _ { a } ^ { \mu } ( r _ { a } ) - m _ { a } ^ { \mu } ( r _ { a } )$ , the constraints in (13) are the same as

$$
\mathbb {E} _ {r _ {a}} \left[ m _ {a} ^ {\mu} (r _ {a}) \right] \leq \mathbb {E} _ {r _ {a}} \left[ r _ {a} \theta_ {a} ^ {\mu} (r _ {a}) \right] - \mathbb {E} _ {r _ {a}} \left[ U _ {a} ^ {\text { BASE }} (r _ {a}) \right] \quad \forall a \in \mathscr {A}.
$$

Summing these inequalities over all $a \in \mathcal A ,$ , we have

$$
\begin{array}{r l} & {\sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \Big [ m _ {a} ^ {\mu} (r _ {a}) \Big ] \leq \sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \Big [ r _ {a} \theta_ {a} ^ {\mu} (r _ {a}) \Big ] - \sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\mathrm{BASE}} (r _ {a}) \big ]} \\ & {\qquad \leq \sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \big [ r _ {a} \theta_ {a} ^ {\mathrm{VCG}} (r _ {a}) \big ] - \sum_ {a = 1} ^ {A} \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\mathrm{BASE}} (r _ {a}) \big ].} \end{array}
$$

The last inequality follows from the fact that the VCG allocation maximizes the social surplus. We now propose a mechanism that is feasible for Problem $( \mathrm { P ^ { M B } } )$ and achieves this upper bound, and is therefore optimal for that problem. Consider the following mechanism:

$$
\begin{array}{l} \Pi^ {\mathrm{OPT-MB}} (\mathbf {r}) = \Pi^ {\mathrm{VCG}} (\mathbf {r}), \\ M _ {a} ^ {\mathrm{OPT-MB}} (\mathbf {r}) = M _ {a} ^ {\mathrm{VCG}} (\mathbf {r}) + \mathbb {E} _ {r _ {a}} \left[ U _ {a} ^ {\mathrm{VCG}} (r _ {a}) \right] - \mathbb {E} _ {r _ {a}} \left[ U _ {a} ^ {\mathrm{BASE}} (r _ {a}) \right]. \end{array} \tag {14}\tag{15}
$$

From (15), we have

$$
\begin{array}{c} \mathbb {E} _ {\mathbf {r}} \big [ M _ {a} ^ {\mathrm{OPT-MB}} (\mathbf {r}) \big ] = \underbrace {\mathbb {E} _ {\mathbf {r}} \big [ M _ {a} ^ {\mathrm{VCG}} (\mathbf {r}) \big ] + \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\mathrm{VCG}} (r _ {a}) \big ]} _ {= \mathbb {E} _ {r _ {a}} \big [ r _ {a} \theta_ {a} ^ {\mathrm{VCG}} (r _ {a}) \big ]} \\ - \mathbb {E} _ {r _ {a}} \big [ U _ {a} ^ {\mathrm{BASE}} (r _ {a}) \big ]   \forall a \in \mathcal {A}. \end{array}
$$

Thus, the constraints in (13) are satisfied at equality, thereby achieving the upper bound above. Moreover, because the allocation and payments are as per VCG (up to a constant), the mechanism $( \mathbf { I I } ^ { \mathrm { o P T - M B } } , \hat { \mathbf { M } } ^ { \mathrm { o P T - M B } } )$ satisfies the constraints (IC). Thus, we have the following theorem.

Theorem 5. The mechanism $( \mathbf { I I } ^ { \mathrm { o P T - M B } } , \mathbf { M } ^ { \mathrm { o P T - M B } } )$ is an optimal solution to Problem (P<sup>MB</sup>).

Table 10. Summary of Win–Lose Scenario

<table><tr><td></td><td>BASE</td><td>OPT-IR</td><td>Gain in OPT-IR (w.r.t. BASE) (%)</td></tr><tr><td>Expected utility of X</td><td> $\frac{1}{8}$ </td><td> $\frac{(1-q)}{8}$ </td><td>-100q</td></tr><tr><td>Expected utility of Y</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Expected revenue of ad exchange</td><td> $\frac{3}{4}$ </td><td> $\frac{3(1+q)}{4}$ </td><td>+100q</td></tr><tr><td>Social welfare</td><td> $\frac{7}{8}$ </td><td> $\frac{7+5q}{8}$ </td><td>+71.43q</td></tr></table>

Note. w.r.t., With respect to.

We briefly note some salient features of the OPT-MB mechanism:

The allocation rule, being VCG, is first best and achieves the maximum social welfare from the sale of an impression. As discussed earlier (see (5), Section 3.3), the allocations can be computed efficiently (specifically, in time 2<sub>(</sub>AN<sub>)</sub>) by solving a dynamic program, thus making them amenable to real-time bidding.

The payment from an advertiser is equal to the value he obtains from the allocation less his expected BASE utility. Consequently, the total expected utility of advertiser a in the long run is equal to E<sub>r</sub> $\lceil U _ { a } ^ { \mathrm { B A S E } } ( \dot { r } _ { a } ) \rceil$ Thus, the ad exchange ensures that each advertiser obtains exactly his expected BASE utility and keeps the remainder of the social surplus.

## 9.1. Applying the OPT-MB Mechanism to the Win–Win and Win–Lose Scenarios

We revisit the win–win and win–lose scenarios discussed in Section 8.1 and 8.2, respectively, and contrast the performance of the OPT-MB mechanism with that of the OPT-IR mechanism. Tables 11 and 12 provide the details of this comparison.

In the win–win scenario, recall from Section 8.1 that the advertisers and the ad exchange are better off under the OPT-IR mechanism compared with the BASE mechanism: both the advertisers enjoy a 75% increase in their expected utility and the ad exchange’s expected revenue increases by 18.75%. Under the OPT-MB mechanism, the ad exchange’s expected revenue increases by 159.38% relative to the BASE mechanism. Thus, the ad exchange benefits more under the OPT-MB mechanism as compared with the OPT-IR mechanism. This is driven by the fact that the OPT-MB mechanism only needs to provide the expected BASE utility to the advertisers.

In the win–lose scenario, advertiser X takes a hit 100q% in his expected utility in the OPT-IR mechanism relative to the BASE mechanism, whereas the OPT-MB mechanism prevents this by giving advertiser X his expected BASE utility. This guarantee that the OPT-MB mechanism provides to the advertisers comes at the expense of a reduced gain in the expected revenue (83.33q% compared with 100q%) of the ad exchange.

To summarize, the advertisers pay a price— foregoing the gain (in their respective expected utilities) they could have received in win–win scenarios—to insure themselves against any loss in the gain (relative to the base mechanism) that can arise in win–lose scenarios. Thus, neither the OPT-IR nor the OPT-MB mechanism dominates the other in the sense that the advertisers and the exchange prefer different mechanisms under different conditions.

It is encouraging to see that, despite guaranteeing the BASE utility to advertisers, the OPT-MB mechanism benefits the ad exchange handsomely relative to the BASE mechanism. Whereas our purpose above was to analytically establish the trade-off between the OPT-IR and OPT-MB mechanisms vis-a-vis the win\` –win and win–lose scenarios, we now inspect the performance of these mechanisms on a more realistic test bed.

## 10. Numerical Investigation

Let the gain in the expected revenue of the ad exchange under mechanism $\mu ,$ relative to the BASE mechanism, be defined as follows:

$$
\rho^ {\mu} := \frac {\text { Expected   revenue   to   the   ad   exchange   under   mechanism } \mu}{\text { Expected   revenue   to   the   ad   exchange   under   the   BASE   mechanism }} - 1.
$$

Similarly, let the gain in the total expected utility over all the advertisers under mechanism $\mu ,$ relative to the BASE mechanism, be defined as follows:

$$
\eta^ {\mu} := \frac {\text { Total   expected   utility   of   the   advertisers }}{\text { under   mechanism } \mu} - 1.
$$

In our discussion below, we will refer to ρ<sup>μ</sup> and $\eta ^ { \mu }$ as, respectively, the revenue gain (of the ad exchange) and the utility gain (of the advertisers) under mechanism μ. Informed by current practice, we now describe a realistic test bed for our study.

## 10.1. Test Bed

We set the number of advertisers (who are typically demand-side networks), A, to 10. Given that (i) for a majority of ads on mobile apps, an impression lasts for a maximum of 300 seconds (Waber 2014), and (ii) the minimum duration for the display of an ad is 30 seconds at major ad exchanges such as Double-Click and OpenX, we set the number of time slots, N, to 10. The valuation-per-click bids of the advertisers are independently drawn from U 0, 1 . The conditional probability, λ, that a user stays on the app at the end of a time slot, given she enters that time slot and does not click on the ad, is assumed to be 0.9.

Table 11. Comparison of Expected Utilities of the Advertisers and Expected Revenue of the Ad Exchange Under the OPT-IR and OPT-MB Mechanisms Under the Win–Win Scenario (Discussed in Section 8.1)

<table><tr><td></td><td>BASE</td><td>OPT-IR</td><td>OPT-MB</td><td>Gain in OPT-IR (w.r.t. BASE) (%)</td><td>Gain in OPT-MB (w.r.t. BASE) (%)</td></tr><tr><td>Expected utility of X</td><td> $\frac{p}{6}$ </td><td> $\frac{7p}{24}$ </td><td> $\frac{p}{6}$ </td><td>+75</td><td>0</td></tr><tr><td>Expected utility of Y</td><td> $\frac{p}{6}$ </td><td> $\frac{7p}{24}$ </td><td> $\frac{p}{6}$ </td><td>+75</td><td>0</td></tr><tr><td>Expected revenue of ad exchange</td><td> $\frac{4p}{3}$ </td><td> $\frac{19p}{12}$ </td><td> $\frac{83p}{12}$ </td><td>+18.75</td><td>+159.38</td></tr></table>

Note. w.r.t., With respect to.

Table 12. Comparison of Expected Utilities of the Advertisers and Expected Revenue of the Ad Exchange Under the OPT-IR and - Mechanisms Under the Win–Lose Scenario (Discussed in Section 8.2)

<table><tr><td></td><td>BASE</td><td>OPT-IR</td><td>OPT-MB</td><td>Gain in OPT-IR (w.r.t. BASE) (%)</td><td>Gain in OPT-MB (w.r.t. BASE) (%)</td></tr><tr><td>Expected utility of X</td><td> $\frac{1}{8}$ </td><td> $\frac{1-q}{8}$ </td><td> $\frac{1}{8}$ </td><td>-100q</td><td>0</td></tr><tr><td>Expected utility of Y</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Expected revenue of ad exchange</td><td> $\frac{3}{4}$ </td><td> $\frac{3(1+q)}{4}$ </td><td> $\frac{6+5q}{8}$ </td><td>+100q</td><td>+83.33q</td></tr></table>

Note. w.r.t., With respect to.

We assume that the click probability of each ad decays at a constant (ad-specific) rate with the passage of time, that is, $p _ { a , n + 1 } = \delta _ { a } p _ { a , n }$ for all a ! and n 1. We refer to $\delta _ { a }$ as the decay $\mathrm { r a t e } ^ { 7 }$ of ad a. Thus, under this constant decay-rate structure, the click probability of an ad in any time slot is determined by its click probability in the first slot and its decay rate. Recall from Section 1.1 that the allocative inefficiency that we seek to eliminate is primarily driven by the variation in the click probability of the ads over time. To examine the effect of this variation on the revenue gain (of the ad exchange) and the utility gain (of the advertisers) under the OPT-IR and OPT-MB mechanisms, we consider the following two scenarios:

<sub>•</sub> Homogeneous ads. In this scenario, for each ad, the click probability in the first time slot is chosen from a common distribution. Similarly, the respective decay rates of the ads are chosen from a common distribution. Using these values, the click probabilities of the ads in the other slots are computed. The clickthrough rate for mobile display ads across different formats is about 0.05% on average (Chaffey 2018). Accordingly, the click probabilities of the ads in the first time slot are independently drawn from U 0, 0.001 . The decay rate of each ad is independently drawn from U 0, 1 .

Heterogeneous ads. In this scenario, we draw 10 random variables from U 0, 0.001 and sort them in ascending order—these are the click probabilities in the first time slot of ads 1 through 10, in that order. The decay rates in the click probabilities of the ads are drawn from U 0, 1 and then sorted in descending order. Thus, ads with a higher index experience a relatively sharper decay than those with a lower index. In this sense, ads with a higher index can be viewed as impulse ads, whereas those with a lower index can be viewed as steady ads.

We compute the percentage gain in the ad exchange’s revenue and the advertisers’ total utility under the OPT-IR and OPT-MB mechanisms (relative to the BASE mechanism) using the sample averages, over 1,000,000 instances. Table 13 summarizes this performance under the homogeneous ad and heterogeneous ad scenarios. We discuss the observations below:

Under both the scenarios, the ad exchange benefits handsomely under the OPT-IR as well as the OPT-MB mechanism, relative to the BASE mechanism. Thus, the partitioned selling of an impression is a promising idea to reduce the allocative inefficiency that we discussed earlier.

In the homogeneous ad scenario, both the ad exchange and the advertisers are better off under the OPT-IR mechanism (by, respectively, 7.01% and 13.72%). Under the OPT-MB mechanism, the revenue gain of the ad exchange significantly improves (from 7.01% to 23.02%). This improvement results from the fact that under the OPT-MB mechanism, the advertisers receive only their respective BASE utilities (thus, η<sup>opt mb</sup> 0%), and the remainder of the total welfare generated goes to the ad exchange. The same phenomenon is observed in the heterogeneous ad scenario, with the difference being that both the revenue gain of the ad exchange (under the OPT-IR and OPT-MB mechanisms) and the utility gain of the advertisers (under the OPT-IR mechanism) are more pronounced. When the ads are heterogeneous, the click probabilities of impulse ads decay more sharply than those of steady ads, resulting in a higher allocative inefficiency as compared with the homogeneous ad scenario. Both the mechanisms exploit this opportunity and offer higher benefits.

In this numerical study, it turned out that under the OPT-IR mechanism, both the ad exchange and the advertisers benefit relative to the BASE mechanism; that is, we are under the win–win scenario (Section 8.1). Note, however, that there is no guarantee offered to the advertisers in the OPT-IR mechanism. As we demonstrated in Section 8.2, it is also possible for some or all the advertisers to be worse off under the OPT-IR mechanism relative to the BASE mechanism. On the other hand, the use of the OPT-MB mechanism allows the ad exchange to guarantee advertisers at least their BASE utility. Despite offering this guarantee, in our numerical study, the ad exchange is better off using the OPT-MB mechanism over the OPT-IR mechanism. Indeed, this is always the case in a win–win scenario. Thus, with the OPT-MB mechanism, the ad exchange can achieve two goals simultaneously under a win–win scenario: assure advertisers of their welfare and obtain a higher revenue. However, in general, it is possible that in adopting the OPT-MB mechanism, the ad exchange has to sacrifice some of its benefit to guarantee the BASE utility to advertisers. Ultimately, the choice between the OPT-IR and the OPT-MB mechanisms will depend on the environment in which the ad exchange operates and whether the exchange wants to assure advertisers of their long-term welfare over the BASE mechanism.

Table 13. Revenue Gain and Utility Gain Under the OPT-IR and OPT-MB Mechanisms for the Homogeneous Ad and Heterogeneous Ad Scenarios

<table><tr><td rowspan="2"></td><td colspan="2">Homogeneous ads</td><td colspan="2">Heterogeneous ads</td></tr><tr><td>OPT-IR</td><td>OPT-MB</td><td>OPT-IR</td><td>OPT-MB</td></tr><tr><td>Revenue gain ( $\rho^{\mu}$ ) (%)</td><td>7.01</td><td>23.02</td><td>18.22</td><td>33.60</td></tr><tr><td>Utility gain ( $\eta^{\mu}$ ) (%)</td><td>13.72</td><td> $\approx 0$ </td><td>55.61</td><td> $\approx 0$ </td></tr></table>

We further investigate the impact of the heterogeneity in the click probabilities of the ads and the number of advertisers on the revenue gain of the ad exchange. To this end, we consider (i) six different distributions of the decay rate by systematically varying its support (see Table 14) and (ii) three values of A: 10, 20, 30. The values of all the other parameters are the same as before.

Figure 3, (a) and (b), illustrates the impact of the variation in the decay rates of the ads on the revenue gain of the ad exchange under, respectively, the OPT-IR and OPT-MB mechanisms. Also shown is the change in this impact as the number of advertisers varies. The revenue gain under both the mechanisms increases with a higher variation in the decay rate. The intuition behind this is as follows. Under a small coefficient of variation of the decay rate, the click probabilities of the ads decay at nearly the same rate. Thus, to begin with, there is little allocative inefficiency to exploit in the BASE mechanism. As the coefficient of variation of the decay rate increases, the contrast between steady and impulse ads becomes prominent, leading to an increase in the allocative inefficiency in the BASE mechanism, which the OPT-IR and OPT-MB mechanisms duly harness. For a fixed coefficient of variation of the decay rate, an increase in the number of advertisers naturally leads to higher competition and, hence, higher revenue gains under both the mechanisms. Furthermore, the marginal revenue gain from an additional advertiser increases with the variation in the decay rate. In summary, the benefit offered by these two mechanisms (over the BASE mechanism) increases as the ads become more diverse (in their click-probability decay) and as competition for the impression increases.

Table 14. Distributions of the Decay Rates of the Click Probabilities of the Ads and the Corresponding Coefficients of Variation

<table><tr><td>Distribution of decay rate of ads ( $\delta_a$ )</td><td>Coefficient of variation of  $\delta_a$ </td></tr><tr><td> $Prob(\delta_a = 0.5) = 1 \forall a$ </td><td>0</td></tr><tr><td> $U(0.4, 0.9)$ </td><td>0.12</td></tr><tr><td> $U(0.3, 0.9)$ </td><td>0.23</td></tr><tr><td> $U(0.2, 0.9)$ </td><td>0.35</td></tr><tr><td> $U(0.1, 0.9)$ </td><td>0.46</td></tr><tr><td> $U(0, 1)$ </td><td>0.58</td></tr></table>

We end this section by commenting on the social welfare achieved by the OPT-IR and OPT-MB mechanisms. Although these mechanisms are designed from the perspective of the ad exchange, they also significantly improve the social welfare relative to the BASE mechanism; Table 15 compares the social welfare under the three mechanisms. The BASE mechanism suffers from two distinct sources of inefficiency:<sup>8</sup> one, the ad exchange retains the impression if the highest virtual valuation is negative, and two, contingent on the highest virtual valuation being nonnegative, a single ad is allocated to all the time slots. The BASE mechanism achieves 84.48% (respectively, 77.45%) of the first-best social welfare under the homoge neous ad (respectively, heterogeneous ad) scenario. The OPT-IR mechanism removes the inefficiency that arises from allocating a single ad to the impression, thereby improving social welfare. Furthermore, because this inefficiency is more pronounced in the heterogeneous ad scenario, the improvement in social welfare is higher in that scenario. The OPT-MB mechanism removes both the inefficiencies, thereby achieving the first-best social welfare.

## 11. Concluding Remarks

With the rapid evolution of technology in the online advertising ecosystem, it has become imperative for stakeholders to come up with solutions that improve their margins as well as the efficiency of the supply chain. The process of delivering digital ads suffers from several inefficiencies due to a fragmented supply chain. In this paper, we analyzed one such inefficiency, namely, the one associated with selling an impression at once to a single advertiser, and obtained mechanisms that are amenable to the real-time bidding protocol. We hope that these mechanisms receive significant attention from the industry as they better match advertisers and publishers, and possess attractive revenue implications for ad exchanges.

Figure 3. (Color online) Revenue Gain of the Ad Exchange for Varying Distributions of the Decay Rate of Ads and Differen Numbers of Advertisers Under the (a) - Mechanism and (b) - Mechanism  
(a)  
![](/api/attachments/9S5WHDE3/fulltext/images/fe68ce567c121ff15a42cf9dd3bd55b215911c40b165c051066fd0524ac1d37c.jpg)

(b)  
![](/api/attachments/9S5WHDE3/fulltext/images/0a113f253f3e6f740d356347de66a02e68c2330f4284aab33dd5c4d936c3c846.jpg)

In our analysis, we have assumed that the private information (valuation per click $r _ { a }$ of advertiser $a ;$ $a \in \mathcal A )$ of the advertisers remains unchanged during the current session. In general, the valuation per click of the advertisers can evolve with the passage of time in the following sense: Given that a user has not clicked on an ad displayed in the sequence thus far, the valuation per click of the advertisers can change in the current time slot to reflect this fact. The modeling framework that incorporates such a feature is that of dynamic mechanism design, in which the private information itself changes over time. The design of dynamic mechanisms specific to our context that accommodate the changes in the private information of the advertisers is a complex problem and is worthy of future investigation.

A natural design question that arises in selling a partitioned impression is the determination of the lengths of the time slots. As of now, ad exchanges such as OpenX and DoubleClick allow publishers to control the refresh rate of ads and offer broad guidelines for better performance. A separate study is required to understand the ad exchange’s problem of dynamically determining the lengths of time slots and estimating the click probabilities of ads in these slots.

Our analysis in this paper can potentially be applied to a variety of other settings. Stated in more general terms, our problem of selling partitioned impressions has the following features: (i) the good that the principle allocates to the agents is “divisible” and there are “dependencies” among the divided subgoods (i.e.,the divided subgoods are “connected” to each other), and (ii) the valuations of the divided subgoods are heterogeneous (i.e., the agents value them differently). Similarly, our objective in more general terms is to obtain a win–win solution for both the principal and the agents, vis-a-vis the current \` practice. Two examples of other potential applications are as follows:

Table 15. Percentage of the First-Best Social Welfare Achieved by the BASE, OPT-IR, and OPT-MB Mechanisms Under the Homogeneous Ad and Heterogeneous Ad Scenarios

<table><tr><td>Mechanism</td><td>Homogeneous ads (%)</td><td>Heterogeneous ads (%)</td></tr><tr><td>BASE</td><td>84.48</td><td>77.45</td></tr><tr><td>OPT-IR</td><td>91.54</td><td>95.46</td></tr><tr><td>OPT-MB</td><td>100</td><td>100</td></tr></table>

The use of shared resources (such as computing capacity) by multiple agents. Here, the division of the good is represented by the allocation of time for which the resources are assigned to different agents. Such a setting offers several interesting constraints on the allocation of the resources. For example, some agents may be endowed with nonpreemptive jobs, which may necessitate the designer to allocate only adjacent slots to these agents. Furthermore, there may be different tiers/ qualities of the resources (e.g., high-, medium-, lowcomputing capacity), and agents may require specific proportions of each of these resources.

The use of a shared space by multiple agents. An example of such a setting is the allocation of real estate to multiple retail outlets in a shopping mall. Here, the division of the good (real estate) is represented by the percentage allocation of the shared space to different retail outlets. In this case, the physical space (area as well as location) allocated to one outlet might affect customer demand at other outlets.

Given the competitive nature of the online advertising landscape, it is natural for the industry to continually look for better ways to monetize the addelivery process. For instance, to overcome the inefficiency in discovering the best price available for an impression across different ad networks and ad exchanges, the industry has started adopting header-bidding technology to enable publishers to consolidate bids across different ad networks and exchanges, and essentially run a simultaneous auction locally on the user’s app/website (for more details, see Levine 2015). The header-bidding mechanism and the mechanisms that we discussed in this paper help improve, respectively, the demand-side and supply-side market thickness. In future research, it would be interesting to analyze the interplay of these two mechanisms and the improvement they offer to the ecosystem in conjunction.

## Endnotes

<sup>1</sup> Ad networks (or supply-side networks) aggregate impressions from different publishers and sell them to advertisers.

<sup>2</sup> See https://developers.google.com/ad-exchange/rtb/start for more details on real-time bidding at Google’s DoubleClick Ad Exchange.

<sup>3</sup> The mechanism-design literature studies several sources of inefficiencies that arise in the design of auctions, for example, no trade as a consequence of reserve prices set by the principal or the resource not being allocated to the highest bidder when the bidders are asymmetric. However, the focus of our work is on the allocative inefficiency that arises from the principal allocating the entire resource at once to a single bidder.

<sup>4</sup> See https://support.google.com/adxseller/answer/6286179 for more details.

<sup>5</sup> See Remark 2 for a mathematically precise justification.

<sup>6</sup> The uniform distribution is used here for ease of exposition. Any other distribution with support 0, r can also be used to construct such a randomized payment rule.

<sup>7</sup> The OPT-IR and the OPT-MB mechanisms do not require a specific structure on the click probabilities of the ads in different slots. We assume a constant decay-rate structure only for our numerical investigation; see Sun et al. (2017) for the mathematical microfoundation of the diminishing click probability of display ads with time and Waber (2014) for empirical evidence.

<sup>8</sup> Another source of inefficiency that could arise in a revenuemaximizing mechanism is when the impression is allocated to the advertiser with the highest virtual valuation instead of the advertiser with the highest valuation. However, in our numerical experiments, the advertisers’ valuations are symmetric and regular, and thus our mechanisms do not suffer from this type of inefficiency.

## References

Abhishek V, Hosanagar K (2013) Optimal bidding in multi-item multislot sponsored search auctions. Oper. Res. 61(4):855–873.

Adaptly (2014) A research study on sequenced for call to action vs. sustained call to action. Accessed September 1, 2019, http:// adaptly.com/wp-content/uploads/2014/11/Adaptly-Refinery29 -White-Paper-2014.pdf.

Agarwal A, Hosanagar K, Smith MD (2011) Location, location, location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Allouah A, Besbes O (2017) Auctions in the online display advertising chain: A case for independent campaign management. Working paper, Columbia Business School Research Paper No. 17-60, Columbia University, New York.

Andrews M, Luo X, Fang Z, Ghose A (2015) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Asdemir K, Kumar N, Jacob VS (2012) Pricing models for online advertising: CPM vs. CPC. Inform. Systems Res. 23 (3-part-1):804–822.

Aseri M, Dawande M, Janakiraman G, Mookerjee V (2017) Procurement policies for mobile-promotion platforms. Manage ment Sci. 64(10):4590–4607.

Aumann Y, Dombb Y, Hassidim A (2016) Auctioning time: Truthful auctions of heterogeneous divisible goods. ACM Trans. Econom. Comput. 4(1):3.

Balseiro S, Kim A, Mahdian M, Mirrokni V (2017) Budget management strategies in repeated auctions. Proc. 26th Internat. Conf. World Wide Web (International World Wide Web Con ferences Steering Committee, Geneva), 15–23.

Balseiro SR, Besbes O, Weintraub GY (2015) Repeated auctions with budgets in ad exchanges: Approximations and design. Management Sci. 61(4):864–884.

Balseiro SR, Feldman J, Mirrokni V, Muthukrishnan S (2014) Yield optimization of display advertising with ad exchange. Man agement Sci. 60(12):2886–2907.

Bharadwaj V, Chen P, Ma W, Nagarajan C, Tomlin J, Vassilvitskii S, Vee E, Yang J (2012) SHALE: An efficient algorithm for allocation of guaranteed display advertising. Proc. 18th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 1195–1203.

Braun M, Moe WW (2013) Online display advertising: Modeling the effects of multiple creatives and individual impression histories. Marketing Sci. 32(5):753–767.

Chaffey D (2018) Average display advertising clickthrough rates. Smart Insights (April 10), https://www.smartinsights.com/internet -advertising/internet-advertising-analytics/display-advertising -clickthrough-rates/.

Chatterjee P, Hoffman DL, Novak TP (2003) Modeling the clickstream: Implications for web-based advertising efforts. Market ing Sci. 22(4):520–541.

Chen Y, Li X, Sun M (2017) Competitive mobile geo targeting Marketing Sci. 36(5):666–682.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1):242–259.

Garg D, Narahari Y (2009) An optimal mechanism for sponsored search auctions on the web and comparison with other mech anisms. IEEE Trans. Automation Sci. Engrg. 6(4):641–657.

Goldfarb A, Tucker C (2011) Online display advertising: Targeting and obtrusiveness. Marketing Sci. 30(3):389–404.

Goldstein DG, McAfee RP, Suri S (2015) Improving the effectiveness of time-based display advertising. ACM Trans. Econom. Comput. 3(2):Article 7.

Hojjat A, Turner J, Cetintas S, Yang J (2017) A unified framework for the scheduling of guaranteed targeted display advertising under reach and frequency requirements. Oper. Res. 65(2): 289–313.

iAd (2014) Inside mobile advertising: Top 5 trends and insights. Accessed September 1, 2019, http://www.callmemobi.com/wp -content/uploads/2013/04/MCSAATCHIMOBILEv15.pdf

Interactive Advertising Bureau (2017) IAB internet advertising revenue report. Accessed September 1, 2019, https://www.iab .com/wp-content/uploads/2018/05/IAB-2017-Full-Year-Internet -Advertising-Revenue-Webinar-Presentation.pdf.

Kim A, Balachander S, Kannan K (2012) On the optimal number of advertising slots in a generalized second-price auction. Markeing Lett. 23(3):851–868.

Korula N, Mirrokni V, Nazerzadeh H (2016) Optimizing display advertising markets: Challenges and directions. IEEE Internet Comput. 20(1):28–35.

Krishna V (2009) Auction Theory (Academic Press, Cambridge, MA).

Krishna V, Perry M (1998) Efficient mechanism design. Working paper, Penn Sate University, State College, PA.

Levine B (2015) MarTech landscape: What is header bidding—And why should publishers care? MarTech Today (December 21), https:///martechtoday.com/martech-landscape-what-is-header -bidding-and-why-should-publishers-care-157065.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1): 133–153.

Mansour Y, Muthukrishnan S, Nisan N (2012) Doubleclick ad exchange auction. Working paper, Tel Aviv University, Tel Aviv, Israel.

McAfee RP, Vassilvitskii S (2012) An overview of practical exchange design. Current Sci. 103(9):1056–1063.

Mohan P, Nath S, Riva O (2013) Prefetching mobile ads: Can ad vertising systems afford it? Proc. 8th ACM Eur. Conf. Comput. Systems (ACM, New York), 267–280.

Muthukrishnan S (2009) Ad exchanges: Research issues. Leonardi S, ed. Internet and Network Economics, Lecture Notes in Computer Science, vol. 5929 (Springer, Berlin), 1–12.

Myerson RB (1981) Optimal auction design. Math. Oper. Res. 6(1): 58–73.

Najafi-Asadolahi S, Fridgeirsdottir K (2014) Cost-per-click pricing for display advertising. Manufacturing Service Oper. Management 16(4):482–497.

Nisan N, Roughgarden T, Tardos E, Vazirani VV (2007) Algorithmi Game Theory, vol. 1 (Cambridge University Press, Cambridge, UK).

Roels G, Fridgeirsdottir K (2009) Dynamic revenue management for online display advertising. J. Revenue Pricing Management 8(5): 452–466.

Sun Z, Dawande M, Janakiraman G, Mookerjee V (2017) Not just a fad: Optimal sequencing in mobile in-app advertising. Inform. Systems Res. 28(3):511–528

Thompson DR, Leyton-Brown K (2013) Revenue optimization in the generalized second-price auction. Proc. 14th ACM Conf. Electronic Commerce (ACM, New York), 837–852.

Turner J, Scheller-Wolf A, Tayur S (2011) OR PRACTICE—Scheduling of dynamic in-game advertising. Oper. Res. 59(1):1–16.

Varian HR (2007) Position auctions. Internat. J. Indust. Organ. 25(6): 1163–1178.

Waber A (2014) The shelf life of a mobile ad: Shorter than you may think. Marketing Land (July 23), http://marketingland.com shelf-life-mobile-ad-shorter-may-think-91495.

Yang J, Vee E, Vassilvitskii S, Tomlin J, Shanmugasundaram J, Anastasakos T, Kennedy O (2010) Inventory allocation for online graphical display advertising. Preprint, submitted August 20, https://arxiv.org/abs/1008.3551.

Yuan Y, Wang F, Li J, Qin R (2014) A survey on real time bidding advertising. IEEE Internat. Conf. Service Oper. Logist. Informatic (IEEE, Piscataway, NJ), 418–423.

Zhang W, Yuan S, Wang J (2014) Optimal real-time bidding for displa advertising. Proc. 20th ACM SIGKDD Internat. Conf. Knowledg Discovery Data Mining (ACM, New York), 1077–1086.
