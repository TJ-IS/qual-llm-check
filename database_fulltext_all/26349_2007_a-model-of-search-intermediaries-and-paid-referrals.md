---
otero_id: 26349
otero_key: "DZZ45VXE"
title: "A Model of Search Intermediaries and Paid Referrals"
authors: "Thomas A. Weber; Zhiqiang (Eric) Zheng"
year: "2007"
journal: "Information Systems Research"
doi: "10.1287/isre.1070.0139"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.63.180.147] On: 16 September 2016, At: 05:31 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## Information Systems Research

## 6SR

![](/api/attachments/DZZ45VXE/fulltext/images/51ea0e79a678a75b4b82c81b0e949ac14f6baa3cb68adca5d8a5de70d3f41ee7.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## A Model of Search Intermediaries and Paid Referrals

Thomas A. Weber, Zhiqiang (Eric) Zheng,

## To cite this article:

Thomas A. Weber, Zhiqiang (Eric) Zheng, (2007) A Model of Search Intermediaries and Paid Referrals. Information Systems Research 18(4):414-436. http://dx.doi.org/10.1287/isre.1070.0139

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2007, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/DZZ45VXE/fulltext/images/1724703f107d8c4be789da811b341edcec981830a90a414aad9e93f6251e1531.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Model of Search Intermediaries and Paid Referrals

Thomas A. Weber

Department of Management Science and Engineering, Terman Engineering Center, Stanford University, Stanford, California 94305, webert@stanford.edu

Zhiqiang (Eric) Zheng School of Management, University of Texas at Dallas, Richardson, Texas 75083, ericz@utdallas.edu

n this paper we pursue three main objectives: (1) to develop a model of an intermediated search market in Iwhich matching between consumers and firms takes place primarily via paid referrals; (2) to address the question of designing a suitable mechanism for selling referrals to firms; and (3) to characterize and analyze the firms’ bidding strategies given consumers’ equilibrium search behavior. To achieve these objectives we develop a two-stage model of search intermediaries in a vertically differentiated product market. In the first stage an intermediary chooses a search engine design that specifies to which extent a firm’s search rank is determined by its bid and to which extent it is determined by the product offering’s performance. In the second stage, based on the search engine design, competing firms place their open bids to be paid for each referral by the search engine. We find that the revenue-maximizing search engine design bases rankings on a weighted average of product performance and bid amount. Nonzero pure-strategy equilibria of the underlying discontinuous bidding game generally exist but are not robust with respect to noisy clicks in the system. We determine a unique nondegenerate mixed-strategy Nash equilibrium that is robust to noisy clicks. In this equilibrium firms of low product performance fully dissipate their rents, which are appropriated by the search intermediary and the firm with the better product. The firms’ expected bid amounts are generally nonmonotonic in product performance and depend on the search engine design parameter. The intermediary’s profit-maximizing design choice, by attributing a positive weight to the firms’ bids, tends to obfuscate search results and reduce overal consumer surplus compared to the socially optimal design of fully transparent results ranked purely on produc performance.

Key words: markets and auctions; paid referrals; search intermediary

History: Sanjeev Dewan, Senior Editor; Arun Sundararajan, Associate Editor. This paper was received on October 5, 2005, and was with the authors 3 <sup>1</sup> months for 2 revisions.

Truly, to tell lies is not honorable; But when the truth entails tremendous ruin, To speak dishonorably is pardonable.

Sophocles (495 b.c.–406 b.c.), Creusa

## 1. Introduction

Even in a time when electronic commerce and Internet presence of many firms seem to increase transparency in product markets, residual and—as we argue—partially intended imperfections may lead to significant price dispersion, especially when goods are differentiated along one or more dimensions (Clemons et al. 2002, Smith and Brynjolfsson 2001, Clay et al. 2001). The difficulties consumers have in finding and comparing goods have led to the flourishing of search intermediaries. The intermediaries’ information aggregation capacity enables marketing to a captive advertising audience (Bhargava and Choudhary 2004). Direct benefits from exercising control over the order in which search results appear can be derived from the firms’ willingness to pay for referrals to their websites. Thus, the ranking of firms produced by a search engine as a response to a consumer’s search request is likely to be influenced by payments from the industry. Google, for example, currently places “sponsor results” above “website matches” for common generic search terms such as “books.” This suggests that there exists a burgeoning market for paid referrals (Edelman et al. 2007), even in an environment that per se is characterized by relatively low cost of information aggregation and dissemination. Naturally, the result may be a partial “obfuscation” of information leading to decreased transparency (Ellison and Ellison 2004). The search intermediary itself may act as a profit-maximizing agent selling, or more precisely auctioning off, the order in which information is made accessible.<sup>1</sup> The rationale is that consumers with a high opportunity cost of time will tend to limit their search in the form of comparison shopping to the first few hits from a “trusted” search intermediary.<sup>2</sup>

In this paper we pursue three main objectives: (1) to develop a model of an intermediated search market in which matching between consumers and firms takes place primarily via paid referrals; (2) to address the important managerial question (for a search intermediary) of finding a suitable mechanism for selling referrals to firms; and (3) to characterize the firms’ equilibrium bidding strategies as well as consumers’ equilibrium search behavior.

In our model we assume that there are two rival firms offering products of possibly many different attributes in the same market. Consumers, who are initially uninformed, can either directly inspect the different products at local retailers or—often at a smaller cost—follow referrals (or links) provided by a search intermediary. In order to maximize their revenues in this search market, firms therefore have an incentive to compete actively for referrals which are followed by a larger number of consumers. In contesting the higher-ranking referrals firms thus engage in rent seeking (Tullock 1980), i.e., behavior destined to appropriate potential excess returns in the market. As a consequence, the value of top referrals has to be equal to the extra rents that firms can obtain by being referred to more consumers. We find that in a market with firms of different product performances it is, perhaps surprisingly, the low-performance firms that tend to expend most of their expected surplus from being ranked high; in other words, they are likely to squander their expected supranormal rents completely in their quest for advantage (in accordance with Posner’s 1975 “rent dissipation postulate”). Contrary to what is common practice at leading search intermediaries such as Yahoo! and Nextag, we find that for the sale of paid referrals it is generally not optimal to base the ranking of firms purely on bid amounts.<sup>3</sup> Taking the consumers’ search behavior into account, it is often beneficial to rank a firm according to a weighted average of its product performance (e.g., reputation as evaluated by consumer feedback or based on other metrics, cf. Footnote 3) and its bid, which can increase the intermediary’s revenue noticeably. There is another important interpretation of our results. Given the difficulty, or near impossibility, of an intermediary being able to commit to a mechanism that is not transparent, in the sense that the produced allocations are not verifiable by the participating agents (e.g., the mechanism employed by Google for ranking sponsored search results), our results shed light on the equilibrium information disclosure that can be expected in such situations.

In our auction setting (further detailed below) it turns out that, quite independent of the weight placed by the intermediary’s ranking mechanism on product performance versus bid amount, the underlying open bidding game for search terms implies discontinuous best-response functions for each vertically differentiated firm and is without pure-strategy Nash equilibria that are robust with respect to even the smallest amount of “noisy clicks” in the system. Exceptions are those special cases of large interfirm performance differences that may provoke zero-bid “shutdown” solutions where no firm bids a positive amount. More specifically, we show that there exists an equilibrium of the bidding game consisting of either nonrobust pure strategies or mixed bidding strategies with positive expected bid amounts by both parties. Clearly it is in the intermediary’s best interest to avoid zerobid equilibria, which implies a degree of obfuscation in the search results, i.e., the weight the intermediary can place on firm performance without inducing a zero-bid equilibrium is bounded from above. In Appendix B we discuss some empirical support for the results of our model, in particular for firms using mixed bidding strategies.

## 1.1. Literature Review

As a consequence of imperfections in product markets, in particular consumer search costs, matching between buyers and sellers is often difficult. Advertising and more recently intermediation can reduce buyers’ search costs and thus facilitate the matching process. Indeed, advertising in a search market has been recognized by Stigler (1961) as “the obvious modern method to identify buyers and sellers” (p. 216). He continues to point out that “[t]he identification of buyers and sellers reduces drastically the cost of search” (ibid.), which has given rise to a rich literature on how much firms should spend on advertising (Butters 1977, Stegeman 1991) and how informative advertising should be (Shapiro 1982, Grossman and Shapiro 1984). Stiglitz (1989) provides an excellent overview of the classical literature on search in product markets with imperfect information. One important characteristic of search markets is that, due to consumer heterogeneities, it is natural for price dispersion to arise in equilibrium (Pratt et al. 1979, Varian 1980, Rob 1985, Stahl 1989). Such price dispersion has been empirically found to be persistent, even in markets with relatively low search costs, such as online books (Clay et al. 2001), online travel (Clemons et al. 2002), or Internet car retailing (Morton et al. 2001). The presence of search intermediaries such as shopbots has not been found to alter significantly consumers’ reliance on brand to make purchase decisions and thus to effectively reduce their search costs (Smith and Brynjolfsson 2001).

The potential role of intermediaries as welfareimproving agents in markets with asymmetrically distributed information is clear since Akerlof (1970) showed that gains from trade may not be realized as a result of an excess in private product information on the part of the seller. Biglaiser (1993) demonstrates that middlemen can be welfare-improving in a relatively general bargaining model with adverse selection. Chen et al. (2002) examine the role of such middlemen as an instrument for price discrimination between offline and online product offerings (the latter, as they find, typically at a lower price), and thus indirectly confirm the welfare-improving role that intermediaries can play in facilitating bi- or multilateral trade. Most of the extant literature on intermediaries has not particularly stressed the consequences of their self-interested behavior as profit-maximizing agents, which can be expected to counterbalance some of the welfare created for the trading parties. A notable exception is Lizzeri (1999), who examines a situation where one seller uses an intermediary to communicate private information to two buyers by an endogenous “certification” procedure. He finds that it is revenue maximizing for the intermediary to disclose the achievement of minimum quality standards to the buyers. Generally, including the intermediary’s interests into the analysis implies that monetary transfers between trading partners and intermediary are per se welfare neutral. Instead of being interpreted as a sink for firms engaging in rent-seeking behavior dissipating their monopoly (or oligopoly) rents (Baumol et al. 1982), the intermediary appropriates and at least partially conserves these rents. Fudenberg and Tirole (1987) stress that a careful use of game theory can reverse some of the consequences of Posner’s (1975) “dissipation” and “wastefulness” postulates, which predict that monopoly rents are completely wasted by firms trying to attain and conserve monopoly power.

In this paper, we focus on a search intermediary that collects payments from firms in return for consumer referrals. In our setting the intermediary, by reducing consumer search costs, enables trade by matching supply and demand for a heterogeneous good. Bhargava and Feng (2004), similar to Baye and Morgan (2001), examine a situation in which such a profit-maximizing search intermediary derives rents from displaying firms’ paid advertisements instead of an unbiased set of search results that users value. The intermediary then needs to trade off an increase in revenues from fixed-fee paid placements against a loss of user-based subscription revenues due to a bias in the search results. Our setting is quite different in that we focus on paid referrals, the priority of which is auctioned off by a search intermediary to competing firms. In this auction, firms bid an amount to be paid for each referral (in the form of a “clickthrough”) generated by the search intermediary. The auction is “all-pay” in the sense that the bid amounts need to be paid for any referrals, independent of the achieved search rank. All-pay auctions arise sometimes in nonmarket situations where decisions about effort or investment are made before the winner of a contest is announced, such as in lobbying activities (Baye et al. 1993). The intermediary can base the ranking of the firms partly on their bids and partly on product quality (and/or firm reputation). Multicomponent scoring rules which incorporate other dimensions of an agreement in addition to monetary bids are sometimes used in procurement auctions and unit price contracts (Ewerhart and Fieseler 2003). Anticipating the firms’ equilibrium bidding behavior, the intermediary determines a revenue-maximizing search engine design in the form of an optimal weight in the ranking function (cf. also Liu and Chen 2006). If the firms have an incentive to bid positive amounts for being ranked first, we show that the bidding equilibrium is generally in mixed strategies, which makes it difficult for consumers to take the open bids as signals for the firms’ respective product performance. In our setting it is the low type that fully dissipates expected profits on bidding for referrals, until a balance is reached between the expected conversion rate and payments for (possibly unsuccessful) referrals, in contrast to the standard signaling models.<sup>4</sup> Our paper is the first to address strategic interdependencies between bidders, which arise naturally in the context of paid referrals as firms are trying to sell their products to the same heterogeneous consumer base.

## 1.2. Outline

In §2 we develop our basic analytical model and describe the main underlying assumptions. In §3 we derive the firms’ equilibrium bidding strategies and the consumers’ equilibrium search behavior, given a certain search engine design. We show that for any search engine design that yields nonzero intermediary revenues, there is a unique Nash bidding equilibrium in mixed strategies, for which we determine the firms expected second-period profit. In §4 we derive the intermediary’s optimal search engine design, that—in contrast to a welfare-maximizing design—will always put a positive weight on the firms’ bids to avoid a zero-bid equilibrium. We also compute the optimal design explicitly for a concrete example. Section 5 concludes the paper with directions for further research.

## 2. The Model

Consider two firms, 1 and 2, that offer differentiated substitute goods in a common market. These goods may have a number of different attributes including price and quality. The exact nature of these attributes matters for our model only insofar as each bundle of attributes can be expected to generate a certain utility u for a given consumer (Lancaster 1966). Ex ante, when selecting these attributes, both firms are confronted with uncertainty about the market and about the other firm’s technological possibilities. In this regard both firms find themselves in an identical decision situation. We assume that at a certain pre-play stage (which remains unmodelled here) there exists an equilibrium (e.g., a perfect Bayesian equilibrium) in which firms choose product offerings, the resulting performance of which will need to be evaluated by consumers and is thus subject to a significant uncertainty from the firms’ point of view. Consumers, on the other hand, are unable to simulate the firms decision processes and form beliefs about the net utility (surplus) of a product offering obtained from one of the firms at random. This utility is realized when purchasing the product (i.e., accepting the product offering with all its attributes including price), so that consumers inspecting both firms’ product offerings can be rationally expected to select the utilitymaximizing one. It is the consumers’ beliefs about the net utilities that we take as primitives of our model.<sup>5</sup>

In what follows we will refer to the net utility of a product also as product performance. Accordingly, by inspecting a firm’s offering a consumer evaluates its product performance.

Consumers can search for suitable products in two ways: with or without the help of an intermediary. The nonintermediated search cost incurred by consumers visiting local retailers directly (corresponding to the “shopping $\mathrm { c o s t ^ { \prime \prime } }$ in Chen et al. 2002, p. 428) is assumed to be substantial. Not only does it contain expenses for transportation but also—and maybe more importantly—the opportunity cost of not getting the most favorable deal. For example, regarding the latter portion of the shopping cost, Chen et al. (2002) indicate that in the market for automobiles the average price obtained through an online intermediary is about two percent less than that paid at a local retailer. Without loss of generality, we set any consumer’s ex ante expected utility $\overline { { u } } _ { 0 }$ from using the outside option of visiting a retailer directly or using another channel (and not using the search intermediary) to zero.

We assume that there is a search intermediary capable of reducing consumers’ shopping cost significantly, at least in expectation (Diehl et al. 2003). Furthermore, inspecting (or “sampling”) each search result is costly as it involves following the provided referrals and evaluating product performance to reach a purchase decision. The sampling cost for transactions such as visiting and inspecting a firm’s site has empirically been found to be considerable. As an example, for a name-your-own-price retailer Hann and Terwiesch (2003) find a “frictional” cost of about \$5 per e-business transaction. This is consistent with observed search behavior of consumers who tend to inspect very few sites prior to a purchase (cf. Footnote 2). In our model we allow consumers to be heterogeneous with respect to their sampling cost $c ,$ which is assumed to be distributed on a compact support $\mathcal { C } \subset \mathbb { R } _ { + }$ . The corresponding cumulative distribution function (cdf) F is taken to be increasing and continuously differentiable, but otherwise is completely arbitrary. We further suppose, at least initially, that every consumer inspects the results in the order they are obtained from the search intermediary. Thus, depending on the prospects of having found the best product offering, a portion $\alpha _ { k }$ of the total number of consumers $C = | \mathcal { C } | > 0$ (per unit time interval)

Table 1 Summary of Notation

<table><tr><td>Symbol</td><td>Explanation</td></tr><tr><td> $\alpha = \alpha_{1}/(\alpha_{1} + \alpha_{2})$ </td><td>(Maximum) value of a rank-one referral</td></tr><tr><td> $\alpha_{k}$ </td><td>Number of consumers that search  $k$  times ( $k \in \{0, 1, 2\}$ )</td></tr><tr><td> $f: \mathcal{C} \to \mathbb{R}_{+}$ </td><td>Density of consumers’ search costs on  $\mathcal{C} \subset \mathbb{R}_{+}$ </td></tr><tr><td> $g: \mathcal{U} \to \mathbb{R}_{+}$ </td><td>Density of consumer surplus on  $\mathcal{U} \subset \mathbb{R}_{+}^{2}$ </td></tr><tr><td> $\theta \in \Theta$ </td><td>Intermediary’s design parameter in the type space  $\Theta = [0, 1]$ </td></tr><tr><td> $b_{H}, b_{L}$ </td><td>Respective bid of high- and low-type firm</td></tr><tr><td> $\delta_{u} = u_{H} - u_{L}$ </td><td>Difference between the firms’ product performances  $u_{H}$  and  $u_{L}$ </td></tr><tr><td> $\Delta = \frac{\theta}{1 - \theta} \delta_{u}$ </td><td>Intermediated utility difference</td></tr><tr><td> $h: \Theta \to \Theta$ </td><td>Design homotopy (probability of high-type firm being ranked first)</td></tr><tr><td> $\mu_{u}^{(k)}$ </td><td>Expected surplus after  $k$  searches ( $k \in \{1, 2\}$ )</td></tr><tr><td> $\hat{\mu}_{u}^{(1)}(\theta)$ </td><td>Expected surplus after one search given  $\theta$  ( $\hat{\mu}_{u}^{(1)}(0) = \mu_{u}^{(1)}$ )</td></tr><tr><td> $\pi_{F}, \pi_{I}$ </td><td>Firm  $F$ &#x27;s ( $F \in \{L, H\}$ ) and intermediary  $I$ &#x27;s payoff</td></tr></table>

evaluate the first k hits $( k \in \{ 0 , 1 , 2 \} )$ by the search intermediary. We argue later (in our remarks before Lemma 3) that this assumption of seemingly nonstrategic consumer behavior is in fact superfluous. As a natural consequence of the model, we obtain that in equilibrium consumers never have an incentive to reverse their search order. Without any loss of generality we can normalize the total number of consumers to one, i.e., C 1. The main notation in our model is summarized in Table 1.

Timing. The model consists of two periods: In the first period, the search intermediary chooses a “search engine design” parameter $\theta \in [ 0 , 1 ] = \Theta$ , which specifies the weight that the intermediary’s ranking function r assigns to the firms’ respective bids versus their true performance level $( \theta = 0 ;$ no weight on product performance/full weight on bids; $\theta = 1 \colon$ : full weight on product performance/none on bids). We assume that the intermediary can gain knowledge about the firms’ true performance level either by consulting third-party information (such as consumer reports) or through its own due diligence (e.g., expert directory ranking produced by Yahoo!).<sup>6</sup> For simplicity we assume that after the design parameter  has been <sup>7</sup> For example, even though an intermediary may have chosen to communicate, say,  0 (i.e., no weight on product performance) to firms, our results indicate that the intermediary may have an incentive to actually use a different $\theta \neq 0$ for ranking purposes, and in the absence of a credible commitment this would be rationally anticipated by the firms when submitting their bids and by consumers when performing their searches.

Figure 1 Timing of Events  
![](/api/attachments/DZZ45VXE/fulltext/images/6bbd6ce96a5f4cb89515b8c73431b9549c455711b69de9448b2cdca7af665838.jpg)  
chosen, the intermediary does credibly communicate this parameter to firms and consumers. Alternately, one may suppose that based on prior experience, both firms and consumers have gained common knowledge about  on which their further decisions can be based. In some situations the intermediary may be unable to either credibly communicate or commit to a particular value of its design parameter . This is the case, for example, when the allocation produced by the intermediary’s mechanism cannot be immediately verified by the participating firms.<sup>7</sup> Under such circumstances firms would rationally assume that the intermediary’s  corresponds to the one maximizing its profits, an interpretation which exactly corresponds to the equilibrium outcome we find. We therefore, for the purposes of our discussion, adhere to the first interpretation of  as a deliberately chosen design parameter which is credibly communicated to all other players.

After observing  firms and consumers decide— at the end of period one—whether to use the search engine or not (in the latter case they obtain the outside option’s payoff of zero). In the second period, the firms’ product performances realize publicly and they enter their respective open bids for each referral by the search intermediary. Naturally these bids may be shaded by strategic considerations, and we will show in the next section that the only equilibrium with nonzero bids is actually in mixed strategies, as is often the case in rent-seeking games, e.g., in the war of attrition (Maynard Smith 1974; Tirole 1988, pp. 311–312) or in complete-information all-pay auctions (Baye et al. 1996). Based on the firms’ bids, their respective product performance and the ranking function, the intermediary then provides ranked search results to consumers, who then decide about their purchases. Figure 1 provides an overview of the timeline in our model. Next we discuss the strategic decision problems of the different parties in our model: consumers, search intermediary, and firms.

Consumers. It is common knowledge among all consumers that there are two competing companies in the market that offer products of different net utilities $u _ { 1 }$ and $u _ { 2 }$ . In order to bound consumers expected surplus (as a function of their searches) from below, let us first consider the case where the search intermediary (such as Yahoo!) puts full weight on the firms’ bids $( \theta = 0 )$ , which ex ante are unknown to the consumers.<sup>8</sup> Note that the joint surplus distribution allows for correlation in the consumers’ beliefs about the two firms; its symmetry expresses the fact that the firms are ex ante indistinguishable. The consumers’ common prior beliefs about the net utilities of the available product offerings are jointly distributed over the convex compact support $\mathcal { U } \subset \mathbb { R } _ { + } ^ { 2 }$ with symmetric measurable probability density $g$ (where $g ( u _ { 1 } , u _ { 2 } ) =$ $g ( u _ { 2 } , u _ { 1 } )$ for almost all $( u _ { 1 } , u _ { 2 } ) \in \mathcal { U } )$ . The resulting net expected utility ${ \overline { { u } } } ( k ; c )$ for any consumer of type $c \in \mathcal { C }$ after $k \in \mathcal { K } = \{ 0 , 1 , 2 \}$ searches is given by

$$
\bar {u} (k; c) = \left\{ \begin{array}{l l} \mu_ {u} ^ {(k)} - k c, & \text { if } k \in \{1, 2 \}, \\ 0, & \text { if } k = 0, \end{array} \right.\tag{1}
$$

where $\mu _ { u } ^ { ( k ) }$ is the expected highest surplus after inspecting k products,<sup>9</sup>

$$
\begin{array}{r} \mu_ {u} ^ {(1)} = \int_ {\mathcal {U}} u _ {1} g (u _ {1}, u _ {2}) d (u _ {1}, u _ {2}), \\ \mu_ {u} ^ {(2)} = \int_ {\mathcal {U}} \max \{u _ {1}, u _ {2} \} g (u _ {1}, u _ {2}) d (u _ {1}, u _ {2}). \end{array}\tag{2}
$$

The optimal number of searches $k ^ { * } ( c )$ for a consumer of type c is such that each additional search (including the first one) promises an expected incremental payoff that outweighs the positive search cost $c . ^ { 1 0 }$ While all consumers strategically perform searches conditional on past observations (cf. Footnote 10), the expected number of searches for any given consumer type c depends only on the order statistics in (2). More specifically, let $\alpha _ { k } \in [ 0 , 1 ]$ be the number of consumers that are expected to search $k \in \mathcal { K }$ times. The following lemma clarifies how the $\alpha _ { k } ^ { \prime } \mathbf { s }$ depend on a composition of consumers’ sampling costs and their beliefs about the net utilities. We will refer to a segment of consumers who all search k times as “consumer search class $k . ^ { \prime \prime }$

Lemma 1 (Consumer Search Classes). <sub>The</sub> <sub>parti-</sub> tion of the consumer base  into search classes is given by $\overset { \cdot } { \alpha _ { 2 } } = F ( \mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) } ) , \alpha _ { 1 } = F ( \mu _ { u } ^ { ( 1 ) } ) - \alpha _ { 2 } ,$ , and $\alpha _ { 0 } =$ $1 - F ( \mu _ { u } ^ { ( 1 ) } )$

The above partitioning $( \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } ;$ cf. Figure 3) of the consumer base  depends on the distribution of the consumer sampling costs as well as on the consumers’ prior beliefs about product performance. In general it also depends on the design parameter $\theta ,$ which had been fixed up to now to $\theta = 0$ . For higher , consumers are less likely to inspect more than the first search result, since the likelihood of finding the best firm by following the “rank-one referral” increases.

Search Intermediary. The search intermediary bases an internal rank score $r ,$ with which it displays the search results, on the $\mathrm { \Delta } ^ { \prime \prime } \mathrm { b i d } ^ { \prime \prime }$ b received by a firm and on this firm’s product performance, measured in consumer surplus u. We define the “search engine design” $\theta \in [ 0 , 1 ] = \Theta$ as the relative weight between the two,<sup>11</sup>

$$
r (b, u; \theta) = \theta u + (1 - \theta) b.\tag{3}
$$

The bid amount b is thereby payable for every referral, irrespective of actual consumer purchase (conversion). This firm’s total payment for referrals is therefore dependent on the number of inspections by consumers, and it is clear that for a given firm this generally results in a tradeoff between being highly ranked and having to pay for a large number of “irrelevant” hits from consumers.

Clearly, for $\theta = 1$ (full ranking weight on product performance) all consumers simply inspect at most the first search result and thus $\alpha _ { 2 } | _ { \theta = 1 }$ must be zero. All consumers who find it incentive compatible to search once can expect a surplus of $\mu _ { u } ^ { ( 2 ) }$ . Since all underlying functions are smooth, it is reasonable to expect that for a general search engine design the partition $( \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } ) ( \theta )$ of the consumer base depends smoothly on the parameter $\theta \in \Theta$ . More specifically, we assume that there exists a continuously differentiable function<sup>12</sup> h $\Theta \to \Theta$ such that h is nondecreasing in $\theta , h ( 0 ) = 1 - h ( 1 ) = 0 .$ , and

$$
\hat {\mu} _ {u} ^ {(1)} (\theta) = (1 - h (\theta)) \mu_ {u} ^ {(1)} + h (\theta) \mu_ {u} ^ {(2)}\tag{4}
$$

is the consumers’ expected surplus from searching once, given a search engine of design . We demonstrate below (cf. Proposition 3) that h corresponds to the equilibrium probability and also the consumers beliefs that the firm with the higher product performance is listed first. In expectation, a type-c consumer searches a second time, if given  the cost c of inspecting an additional product does not exceed the expected gain $\mu _ { u } ^ { ( 2 ) } - \hat { \mu } _ { u } ^ { ( 1 ) }$ of an additional search (cf. Figure 2). As a direct consequence from Lemma 1 we obtain the following more general “intermediated” partition of the consumer base.<sup>13</sup>

Lemmma 2 (Intermediated Consumer Search <sup>Classes).</sup> For a given search engine design $\theta \in \Theta$ and appropriate continuous mapping h in (4), the segmentation of the consumer base  into search classes is given by $\alpha _ { 2 } ( \theta ) = F ( \mu _ { u } ^ { ( 2 ) } - \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) ) , \alpha _ { 1 } ( \theta ) = F ( \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) ) - \alpha _ { 2 } ( \theta )$ and $\alpha _ { 0 } ( \theta ) = 1 - F ( \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) )$

Lemma 2 states that consumers who are expected to search twice have a search cost c that does not exceed the expected incremental benefit $\mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) }$ of searching twice instead of once, times the probability $1 - h ( \theta )$ that the firm with the lower-performing product is listed first. Similarly, consumers who are expected to search at least once have a search cost that does not exceed the expected value $\hat { \mu } _ { u } ^ { ( 1 ) } ( \theta )$ of searching once in equilibrium.

Figure 2 Consumers Trade Off Sampling Cost Against an Increase in Expected Utility  
![](/api/attachments/DZZ45VXE/fulltext/images/026625c5e5c8dd47726a70b8a6839d6c59ac049cfe5da484b93df775b56c914b.jpg)

The search intermediary’s first-period optimal design problem is to find a design parameter  that maximizes expected revenues given the resulting consumer behavior and firms’ optimal bidding policies. We can see that the total number of consumers using the search engine, $( \alpha _ { 1 } + \alpha _ { 2 } )$ , increases in , whereas the expected total number of referrals, $( \alpha _ { 1 } + 2 \alpha _ { 2 } )$ , does not have to be monotonic in $\theta . ^ { 1 4 }$ Naturally the number of consumers in the system influences the “stakes” for the companies, tending to increase the bids if the magnitude of search class one is large compared to the magnitude of search class two, i.e., if $\alpha _ { 1 } \gg \alpha _ { 2 }$ On the other hand, as  increases, the firm with the lower performance level needs to outbid the highperformance firm by a larger amount to secure rankone referrals despite its lack in product performance. However, if  is close enough to 1, the lower firm will stop bidding altogether as the bids needed to win a rank-one referral exceed its expected value, which in turn reduces the incentives of the high-performance firm to bid, reducing overall intermediary revenues. From this it is clear that generally the intermediary will seek an intermediary search engine design $\theta ^ { * }$ in the interior of  to maximize revenues.

Figure 3 Intermediated Consumer Search Classes  
![](/api/attachments/DZZ45VXE/fulltext/images/6834448d6c9fe86524438d88b0e359c0c6887ce4d675ac8751a9b25274c8a66a.jpg)

The Firms’ Bidding Problem. At the beginning of the second period the (hitherto unknown) random net utilities, $u _ { 1 } , u _ { 2 } \in \mathcal { U } ,$ of the firms’ product offerings realize. A net utility $u _ { i }$ corresponds to firm i’s performance type. The firms simultaneously submit bids to the intermediary for referrals. It turns out that a firm’s bidding strategy depends only on whether or not its performance type is higher or lower than that of the other firm. Hence, we say that firm i is of “high” performance type (or simply of high type), abbreviated by H , if

$$
u _ {i} = \max \{u _ {1}, u _ {2} \} \equiv u _ {H}.\tag{5}
$$

Similarly, firm j is of low type, if

$$
u _ {j} = \min \{u _ {1}, u _ {2} \} \equiv u _ {L}.\tag{6}
$$

Note that the probability that $u _ { H } = u _ { L }$ is zero, because $u _ { 1 } , \ u _ { 2 }$ are two independent draws of the net consumer surplus. For simplicity, once the net utilities have realized we refer to the firms by their type $j \in \{ L , H \}$ rather than their index $i \in \{ 1 , 2 \}$ . Firm $j ^ { \prime } \mathbf { s }$ profit $\pi _ { j }$ depends on the search rank $r ( b _ { j } , u _ { j } ; \theta )$ achieved through its bid, the other firm’s search rank (which determines $\mathrm { i f } j$ wins the auction or not), and its margin, which we normalize for both firms to one.<sup>15</sup> If both firms achieve the same rank, then the search intermediary will adopt the tiebreaking rule of displaying firm H with the better performing product first (note that Prob $( u _ { H } = u _ { L } ) = 0 )$

## 3. Equilibrium Strategies

At the end of the second period consumers form their beliefs h about the probability that the high-type firm is ranked first. Based on Lemma 2 this determines the intermediated consumer search classes, i.e., the partition $( \alpha _ { 0 } , \alpha _ { 1 } , \alpha _ { 2 } ) ( \theta )$ of the consumer base . At the beginning of this period each of the two competing firms learns its type $j \in \{ L , H \}$ (from the realizations of $u _ { 1 } , u _ { 2 } \in \mathcal { U } )$ and the corresponding expected payoffs as a function of its bids (relative to the consumers beliefs). The firms’ respective payoffs are given by

$$
\begin{array}{l} \pi_ {H} (b _ {L}, b _ {H}) \\ = \left\{ \begin{array}{l l} (\alpha_ {1} + \alpha_ {2}) (1 - b _ {H}), & \text { if } r (b _ {H}, u _ {H}) \geq r (b _ {L}, u _ {L}), \\ \alpha_ {2} (1 - b _ {H}), & \text { if } r (b _ {H}, u _ {H}) <   r (b _ {L}, u _ {L}), \end{array} \right. \end{array}\tag{7}
$$

and

$$
\begin{array}{l} \pi_ {L} (b _ {L}, b _ {H}) \\ = \left\{ \begin{array}{l l} - \alpha_ {2} b _ {L}, & \text { if } r (b _ {H}, u _ {H}) \geq r (b _ {L}, u _ {L}), \\ - \alpha_ {2} b _ {L} + \alpha_ {1} (1 - b _ {L}), & \text { if } r (b _ {H}, u _ {H}) <   r (b _ {L}, u _ {L}), \end{array} \right. \end{array}\tag{8}
$$

where as before $r ( b _ { j } , u _ { j } ) = r ( b _ { j } , u _ { j } ; \theta )$ for $j \in \{ L , H \}$ . To simplify the exposition we have dropped the explicit dependence on . Firm H is thereby ranked first by the intermediary, if and only if the condition

$$
r (b _ {H}, u _ {H}) \geq r (b _ {L}, u _ {L}) \Leftrightarrow b _ {H} \geq b _ {L} - \frac {\theta}{1 - \theta} (u _ {H} - u _ {L})\tag{9}
$$

is satisfied. Maximizing firm $j ^ { \prime } \mathbf { s }$ profit function with respect to $b _ { j }$ in $( 7 )  { - } ( 8 )$ we obtain the best-response correspondences<sup>16</sup>

$$
\begin{array}{l} b _ {H} ^ {*} (b _ {L}) = \underset {b _ {H} \geq 0} {\arg \max} \pi_ {H} (b _ {L}, b _ {H}) \\ = \left\{ \begin{array}{l l} [ b _ {L} - \Delta ] _ {+}, & \text { if } b _ {L} \leq \alpha + \Delta , \\ 0, & \text { if } b _ {L} \geq \alpha + \Delta , \end{array} \right. \end{array}\tag{10}
$$

obtains at least the same margin as the firm of type $L .$ In the event where $m _ { L } > m _ { H }$ one can show that the notion of highperforming versus low-performing may be reversed if firms’ performance differences are small. In addition, this distinction wil then also depend on the design parameter . The model can then still be solved if one allows the surplus distributions to depend on θ; however, to keep our model simple and analytically tractable we exclude this somewhat implausible situation.

and

$$
\begin{array}{l} b _ {L} ^ {*} (b _ {H}) = \underset {b _ {L} \geq 0} {\arg \max} \pi_ {L} (b _ {L}, b _ {H}) \\ = \left\{ \begin{array}{l l} b _ {H} + \Delta + \varepsilon , & \text { if } b _ {H} \leq \alpha - \Delta - \varepsilon , \\ 0, & \text { if } b _ {H} \geq \alpha - \Delta - \varepsilon , \end{array} \right. \end{array}\tag{11}
$$

where we define $\alpha ( \theta )$ as “(maximum) value of a rankone referral,” i.e., unit margin times the fraction of searching consumers who sample only the first search result,

$$
\alpha = \alpha_ {1} / (\alpha_ {1} + \alpha_ {2}) \in [ 0, 1 ],\tag{12}
$$

and " as the “intermediated utility difference,”

$$
\Delta = \frac {\theta}{1 - \theta} (u _ {H} - u _ {L}) \geq 0.\tag{13}
$$

It represents the cash equivalent (excluding the additional increment #) by which the low-type firm has to overbid the high-type firm to win a rank-one referral. We now examine the second-period bidding game $\Gamma ( \theta ) . ^ { 1 7 }$ The value of a rank-one referral corresponds to the value (on a per-referral basis) of winning the intermediary’s auction. As a consequence, no bid can rationally exceed . The constant $\varepsilon > 0$ corresponds to the smallest monetary bid increment accepted by the search intermediary.<sup>18</sup> A purestrategy equilibrium of this auction can exist only if the corresponding consumer beliefs $h ( \theta ) \in \{ 0 , 1 \}$ about the probability of the high type’s winning reflect the firms’ equilibrium bidding strategies. Let us first examine the case where $h ( \theta ) = 0 , { \mathrm { ~ i . e . } }$ , when the low-type firm is sure to be listed first in equilibrium. Then, consistent with their beliefs, all consumers would start their search with the second rank, so that the value of a rank-one referral becomes zero. As a result, both firms would bid zero, which implies that the high-type firm would win with probability one, inconsistent with the consumers’ beliefs. We now consider the case when $h ( \theta ) = 1 , { \mathrm { i . e . } }$ , the consumers believe that the high-type firm is sure to win the auction, and therefore $r ( b _ { H } , u _ { H } ; \theta ) \ge r ( b _ { L } , u _ { L } ; \theta )$ has to hold in equilibrium. Then all consumers search exactly once, so that $\alpha _ { 1 } = \alpha = 1$ . From (7) and (8) we can see that Firm L would prefer to lose the auction if any only if $b _ { L } \geq 1$ while firm H would agree to win the auction (at a bid of $b _ { H } = b _ { L } - \Delta )$ if $b _ { H } \leq 1$ . Thus, there exists a continuum of pure-strategy equilibria. However, it turns out that these pure-strategy equilibria vanish if there is an arbitrarily small number of “noisy clicks” in the system, which could be the result of small deviations from full rationality by consumers, causing them to make a mistake from time to time when following the online referrals.

Proposition 1 (Pure-Strategy Nash Equilibria). Let $\theta \in \Theta . \ ( \mathrm { i } )$ The bidding-strategy profile $( b _ { L } ^ { * } , b _ { H } ^ { * } ) = ( 1 +$ $\lambda , 1 + \lambda - \Delta )$ constitutes a pure-strategy equilibrium of the bidding game \$  for all $\lambda \in [ 0 , \Delta ( \theta ) ]$ . (ii) If, as a result of noisy clicks, $\alpha _ { 2 } > 0 $ , then a pure-strategy equilibrium of \$  does not exist.

Part (i) of Proposition 1 states that similar to a separating equilibrium in the Spence signaling game (cf. Footnote 4) there exists a continuum of purestrategy equilibria for which the consumers are able to distinguish the firms by their ranking (with firm H being ranked first). Most of these equilibria are (Kaldor-Hicks) “inefficient” in the sense that firm L’s equilibrium bid critically depends on the assumption that it never wins the auction (all consumers search only once), increasing the minimum bid required for firm H . The latter would be willing to avoid the high bids by a side payment to firm L. Note in particular that all pure-strategy equilibria are such that firm L is never required to actually pay and that the ranking function produces the same value for firm L and firm H, i.e., $r ( b _ { L } , u _ { L } ; \theta ) \equiv$ $r ( b _ { H } , u _ { H } ; \theta )$ . Part (ii) of Proposition 1 notes that if firm L can expect a nonzero number of clicks, then all of the pure-strategy equilibria must vanish, as firm L is never able to offset the associated cost. From part (ii) we conclude that the pure-strategy equilibria are not robust, and therefore examine the possibility of mixed-strategy equilibria, which turn out to be unique and robust with respect to noisy clicks.

For a given rank-one-referral value  and an intermediated utility difference " Figure 4 depicts the firms’ best-response correspondences in the bidding game \$ . It can readily be verified that their intersection is empty. For example, starting with a bid amount $b _ { L } \in [ \Delta , \alpha ] .$ , we see by tracing the firms’ best responses successively that both firms will tend to bid until one of them drops out, upon which the firms start bidding up again.<sup>19</sup> It is crucial that $\alpha ( \theta ) \leq \Delta ( \theta )$ or equivalently that

Figure 4 Best-Response Correspondences for $\theta \in [ 0 , \bar { \theta } )$  
![](/api/attachments/DZZ45VXE/fulltext/images/11874cd0f853931206695429b5656afc52968d0f3b077ce23631dc31c1b4f42a.jpg)

$$
\theta <   \bar {\theta} = \frac {\alpha (\bar {\theta})}{\alpha (\bar {\theta}) + (u _ {H} - u _ {L})},\tag{14}
$$

since otherwise firm L would need to (with positive probability) bid more than the rank-one referral value $\alpha ( \theta )$ to ever be able to win the auction, which is a dominated strategy. The search intermediary therefore has a natural incentive to keep the design parameter  below a critical value ¯. This makes plain the search intermediary’s desire to limit the transparency of the provided search results, a pervasive managerial insight in intermediated search markets. If the search engine design is such that the weight on product performance is high with $\theta \geq \bar { \theta } ,$ then a mixed-strategy bid equilibrium does not exist. The intermediated utility difference in (13) is too large for the low-type firm to be able to win the auction at a gain. The cash equivalent of this difference exceeds the value of a rank-one referral, i.e., $\Delta \ge \alpha$

Proposition 2 (Mixed-Strategy Nash Equilibrium). <sub>Let</sub> $\theta \in [ 0 , \bar { \theta } )$ . Then there is a unique mixedstrategy Nash equilibrium of $\Gamma ( \theta )$ , which is given by the following probability distributions of bids:

$$
P _ {H} ^ {*} (z; \theta) = \operatorname{Prob} (b _ {H} \leq z | \theta) = \frac {(1 - \alpha (\theta)) (z + \Delta (\theta))}{\alpha (\theta) (1 - z - \Delta (\theta))}\tag{15}
$$

for firm H, and

$$
\begin{array}{l} Q _ {L} ^ {*} (y; \theta) = \operatorname{Prob} (b _ {L} \leq y \mid \theta) \\ = \left\{ \begin{array}{l l} \frac {y - \alpha (\theta) (y - \Delta (\theta))}{\alpha (\theta) (1 - y + \Delta (\theta))}, & y \geq \Delta (\theta), \\ \Delta (\theta) / \alpha (\theta), & y \leq \Delta (\theta), \end{array} \right. \end{array}\tag{16}
$$

for firm $L . ^ { 2 0 }$

In the case where the search engine design allows firm L to in principle win a rank-one referral at a gain $( \mathrm { i . e . , ~ } \alpha > \Delta )$ , then the only Nash equilibrium of the open-bidding game $\Gamma ( \theta )$ is in mixed strategies, where both firms L and H randomize over their bids.<sup>21</sup> The mixed-strategy equilibrium found in this search market implies a bid dispersion that is somewhat related to equilibrium price dispersions noted earlier in search markets (Varian 1980). Figure 5

<sup>20</sup> The corresponding densities $p _ { H } ^ { * } ( z \vert \theta )$ and $q _ { L } ^ { * } ( y \mid \theta )$ can be obtained via (generalized) differentiation,

$$
p _ {H} ^ {*} (z \mid \theta) \stackrel {\text { a.e. }} {=} \frac {1 - \alpha}{\alpha (1 - \Delta - z) ^ {2}} \operatorname{rect} \left(\frac {z}{\alpha - \Delta}\right) + \frac {(1 - \alpha) \Delta}{\alpha (1 - \Delta)} \delta (z),
$$

for firm $H ,$ and

$$
q _ {L} ^ {*} (y \mid \theta) \stackrel {{\text { a.e. }}} {{=}} \frac {1 + \Delta - \alpha}{\alpha (1 + \Delta - y) ^ {2}} \operatorname{rect} \left(\frac {y - \Delta}{\alpha - \Delta}\right) + \frac {\Delta}{\alpha} \delta (y),
$$

for firm L, where we have omitted the dependence on  on the right-hand sides, for simplicity. The Dirac distribution $\delta ( \cdot )$ is such that $\delta ( y ) = 0$ for all $y \neq 0$ and $\begin{array} { r } { \int _ { - \varepsilon } ^ { \varepsilon } \delta ( y ) d y = 1 } \end{array}$ for any $\varepsilon > 0 .$ The rectangular function rect· is defined by recty = 1 for $y \in [ 0 , 1 ]$ and rec $\operatorname { t } ( y ) = 0$ otherwise. Note that when $\Delta > 0$ there is a positive probability of either firm bidding zero.

<sup>21</sup> The mixed-strategy equilibrium specified in Proposition 2 supposes uncorrelated strategy profiles. In addition there may be correlated equilibria (Aumann 1974) if firms can coordinate on an appropriate interbid correlation (e.g., by using a public randomizing device). Naturally in the realistic (and empirically observed) setting of a dynamic bidding game, bids are typically correlated (cf. Appendix B, Figure B.1). Our theory is limited to the firm’s one-shot (or repeated myopic) equilibrium behavior, which natu rally also constitutes a subgame-perfect Nash equilibrium of the infinitely repeated game.

Figure 5 Mixed-Strategy Nash Equilibrium of   (10,000 Simulated Bids) for $\theta = 1 / 5$  
![](/api/attachments/DZZ45VXE/fulltext/images/438fffa1958b94468a1961d3830898382b532af1a3ec25779fc7b023c348603f.jpg)

![](/api/attachments/DZZ45VXE/fulltext/images/115e76af5e31465522b902391af4f7f70be3a2cec4273c9c28cfc50ebf56fb46.jpg)

![](/api/attachments/DZZ45VXE/fulltext/images/4db5011dbc72d9c340626695360796612bbd31f12b098c6b0c7640e032b2ff2a.jpg)

depicts the mixed-strategy equilibrium. In order to achieve mutual indifference (the defining condition for a mixed-strategy equilibrium), both firms when randomizing need to make higher bid amounts progressively more likely. Note that these mixed-strategy profiles contain generally nonzero atoms, in particular whenever $\Delta > 0$ and $\alpha < 1 . ^ { 2 2 }$

As a consequence of Proposition 2 we can determine both firms’ expected bids,

$$
\bar {b} _ {H} ^ {*} = \int_ {0} ^ {\alpha - \Delta} z d P _ {H} ^ {*} (z) = \frac {1}{\alpha} \left(\alpha - \Delta + (1 - \alpha) \ln \frac {1 - \alpha}{1 - \Delta}\right),\tag{17}
$$

and

$$
\begin{array}{r l} & {\bar {b} _ {L} ^ {*} = \int_ {\Delta} ^ {\alpha} y d Q _ {L} ^ {*} (y)} \\ & {\quad = \frac {1}{\alpha} ((1 + \Delta) (\alpha - \Delta) + (1 + \Delta - \alpha) \ln (1 + \Delta - \alpha)),} \end{array}\tag{18}
$$

<sup>22</sup> The existence of the mixed strategy profiles also follows from Simon (1987), as the firms’ payoffs $( 7 )  { - } ( 8 )$ satisfy the “complementary discontinuity property.” The well-known earlier existence result for mixed-strategy equilibria in games with discontinuous payoffs by Dasgupta and Maskin (1986) does not allow for such atoms.

where $\Delta \in [ 0 , \alpha ]$ . For not too high values of $\alpha$ it is $\bar { b } _ { H } ^ { * } < \bar { b } _ { L } ^ { * } ,$ , which stresses the importance the presence of the low-type firm has for the intermediary. However, there are cases (for large  and small ") in which $\bar { b } _ { H } ^ { * } > \bar { b } _ { L } ^ { * } ,$ in those situations the value of a rankone referral  is very high and the bid-advantage through better product performance relatively low, so that the high-type firm ends up bidding higher on average. Note also that the bids are generally not visible to consumers, and as a consequence bids cannot act as a signal separating the firms’ types in expectation. In addition, even if firm L bids higher than firm H, its probability of winning the auction can never reach a value above 05, the critical value above which consumers would find it beneficial to inspect the second referral first. However, the latter switch in consumer behavior cannot occur, because firm H by mimicking firm L could always preempt it through a simple bid increase. Lastly, we remark that, in contrast to the pure-strategy equilibria in Proposition 1, the mixed-strategy equilibrium is robust with respect to noisy clicks in the sense that the cost of additional random consumers that search twice can be offset (in expectation) by a small random number of additional consumers that only search once. Because firm H can (for $\theta > 0 )$ expect a positive profit, its participation is not sensitive to noisy clicks.

Lemma 3 (Expected Firm Profits in Equilibrium). i Let $u _ { H } > u _ { L }$ and $\theta \in [ 0 , \bar { \theta } )$ . At the beginning of the second period, the expected firm profits in equilibrium are $\bar { \pi } _ { H } ^ { * } = \alpha _ { 2 } + ( \alpha _ { 1 } + \alpha _ { 2 } ) \Delta$ and $\bar { \pi } _ { I . } ^ { * } = 0 .$ (ii) Each firm’s ex ante expected profits $\overline { { \overline { { \pi } } } } _ { F } ^ { * }$ at the beginning of the first period are

$$
\begin{array}{c} \overline {{\overline {{\pi}}}} _ {F} ^ {*} = \frac {\alpha_ {2}}{2} + \frac {1}{2} \big (\alpha_ {1} \text {Prob} (\Delta \geq \alpha) + (\alpha_ {1} + \alpha_ {2}) \\ \cdot E (\Delta   |   \Delta <   \alpha) \text {Prob} (\Delta <   \alpha) \big), \end{array}\tag{19}
$$

where $\Delta = ( \theta / ( 1 - \theta ) ) \delta _ { u }$ with $\delta _ { u } = u _ { H } - u _ { L }$ the surplus difference between the two firms.

In a mixed-strategy Nash equilibrium, at $t = 2$ firm L expects zero profits, even though in many cases it is firm L that expects to bid more than firm H. Even conditional on having realized $u _ { L } ,$ it is (according to (18)) still incentive compatible for firm L to expect to bid a positive amount leading to zero expected profits.<sup>23</sup> However, ex ante (at t 1) both firms have symmetric expectations about their types, and thus both generally expect a positive profit of $\overline { { \overline { { \pi } } } } _ { F } ^ { * }$ according to part (ii) of Lemma 3. From expression (19) it is clear that both firms would prefer ex ante full transparency, i.e., a search engine design $\theta _ { F } ^ { * } = 1$ with full weight on product performance. It is clear that $\overline { { \overline { { \pi } } } } _ { F } ^ { * }$ cannot exceed $\textstyle ( \alpha _ { 1 } + \alpha _ { 2 } ) / 2$ , i.e., half of the total surplus to be shared between firms and intermediary. Setting $\theta = 1$ implies that Prob $( \Delta \ge \alpha ) = 1$ , so that this upper bound is achieved. We note, however, that given a certain design $\theta < 1 .$ it may be the case that the firms would locally prefer less transparency, i.e., the intermediary’s placing a higher weight on the firms bids. In other words, $\overline { { \overline { { \pi } } } } _ { F } ^ { * } ( \theta )$ may be nonmonotonic with respect to $\theta . ^ { 2 4 }$ Because $\alpha ( \theta )$ is nondecreasing in  (cf. Lemma 2) one obtains—in view of relation (14)—that as long as  does not exceed some critical value $\overline { { \overline { { \theta } } } } \in \Theta$ (which is a lower bound for ¯ in (14)),

$$
\theta \leq \frac {\alpha (0)}{\alpha (0) + \max _ {(u _ {1} , u _ {2}) \in \mathcal {U}} | u _ {1} - u _ {2} |} \equiv \overline {{\overline {{\theta}}}} (\leq \bar {\theta}),\tag{20}
$$

expression (19) for ex ante expected firm profits simplifies to

$$
\bar {\overline {{\pi}}} _ {F} ^ {*} = \frac {1}{2} (\alpha_ {2} + (\alpha_ {1} + \alpha_ {2}) \bar {\Delta}),\tag{21}
$$

where $\bar { \Delta } = ( \theta / ( 1 - \theta ) ) \bar { \delta } _ { u }$ is the expected intermediated utility difference and $\bar { \delta } _ { u } = E ( \delta _ { u } )$ is the expected product-performance difference. Relation (20) ensures that (14) is satisfied for any possible surplus realizations.

Proposition 3 (Equilibrium Search Behavior). For any $\theta \in [ 0 , \bar { \theta } )$ the consumers’ equilibrium search behavior is determined by the following system of equations:

$$
\left\{ \begin{array}{l} \alpha (\theta) = 1 - (F (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)) / F (\hat {\mu} _ {u} ^ {(1)} (\theta))), \\ \hat {\mu} _ {u} ^ {(1)} (\theta) = \int_ {\mathcal {U}} (\varphi (u _ {2} - u _ {1}, \theta) u _ {2} + (1 - \varphi (u _ {2} - u _ {1}, \theta)) u _ {1}) \\ \qquad \cdot g (u _ {1}, u _ {2}) d (u _ {1}, u _ {2}), \\ \varphi (u _ {2} - u _ {1}, \theta) = \frac {\Delta}{\alpha (\theta)} + \frac {1 - \alpha + \Delta}{\alpha^ {2} \Delta^ {2}} \bigg ((\alpha - \Delta) \Delta + (1 - \alpha) \\ \qquad \cdot \ln \frac {1 - \alpha}{(1 - \Delta) (1 - \alpha + \Delta)} \bigg) \bigg | _ {\Delta = (\theta | u _ {2} - u _ {1} |) / (1 - \theta)}, \end{array} \right.\tag{22}
$$

where $\mu _ { u } ^ { ( 2 ) }$ is given by (2), and / denotes the probability density that the high-type firm wins the rank-one referral. In a pure-strategy equilibrium, all consumers inspect only the first link, so that $\alpha ( \theta ) \equiv 1$ and $\hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) \equiv \dot { \mu } _ { u } ^ { ( 2 ) }$ where $\mu _ { u } ^ { ( \tilde { 2 } ) }$ is given by (2).

In the interesting case where $\theta \in [ 0 , \bar { \theta } )$ , the equilibrium system in Proposition 3 determines the consumers’ search behavior in the sense that the sizes of the intermediated consumer search classes, $\alpha _ { 1 }$ and $\alpha _ { 2 } ,$ as well as the function h in (4), which was used to construct the equilibrium, are obtained from a solution $( \alpha , \hat { \mu } _ { u } ^ { ( 1 ) } , \varphi )$ to (22) as follows:

$$
\left\{ \begin{array}{l} \alpha_ {1} (\theta) = F (\hat {\mu} _ {u} ^ {(1)} (\theta)) - F (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)), \\ \alpha_ {2} (\theta) = F (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)), \\ h (\theta) = 1 - (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) ^ {- 1} (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)). \end{array} \right.\tag{23}
$$

The dependence of the consumers’ search behavior in a mixed-strategy equilibrium becomes apparent by inspecting (22) and (23): as $\theta \in [ 0 , \bar { \theta } )$ increases, $\hat { \mu } _ { u } ^ { ( 1 ) } ( \dot { \theta } )$ increases, so that $\alpha _ { 1 } ( \theta )$ also increases while $\alpha _ { 2 } ( \theta )$ decreases. The value h corresponds to the consumers’ beliefs about the probability that firm H is listed first, which are correct in equilibrium. We note that h is continuous and increases in equilibrium (with $h ( 0 ) = 1 - h ( 1 ) = 0 )$ , as posited in $\ S 2$

## 4. Search Engine Design

We now solve the intermediary’s first-stage problem of finding an optimal (public) weighting parameter that trades off between product performance and bids in the ranking function. The intermediary’s secondperiod profits $\pi _ { I }$ as a function of the firms’ bids $( b _ { L } , b _ { H } )$ are given by

$$
\begin{array}{l} \pi_ {I} (b _ {L}, b _ {H}) \\ = \alpha_ {2} (b _ {L} + b _ {H}) + \left\{ \begin{array}{l l} \alpha_ {1} b _ {H}, & \text { if } r (b _ {H}, u _ {H}) \geq r (b _ {L}, u _ {L}), \\ \alpha_ {1} b _ {L}, & \text { if } r (b _ {H}, u _ {H}) <   r (b _ {L}, u _ {L}). \end{array} \right. \end{array}\tag{24}
$$

Using the results in Proposition 2 we can determine the intermediary’s expected profits in the mixedstrategy bidding equilibrium.

Lemma 4 (Expected Intermediary Profits in <sup>Equilibrium).</sup> The search intermediary’s ex ante expected equilibrium profits are given by

$$
\overline {{\bar {\pi}}} _ {I} ^ {*} (\theta) = \left(\alpha_ {1} - \left(\alpha_ {1} + \alpha_ {2}\right) E (\Delta | \Delta <   \alpha)\right) \operatorname{Prob} (\Delta <   \alpha),\tag{25}
$$

where " is given as in Lemma 3.

Analogous to our remark after Lemma 3, as long as (20) holds, expression (25) simplifies to

$$
\overline {{\overline {{\pi}}}} _ {I} ^ {*} = \alpha_ {1} \bigg (1 - \frac {\bar {\Delta}}{\alpha} \bigg) = \alpha_ {1} - (\alpha_ {1} + \alpha_ {2}) \bar {\Delta}.\tag{26}
$$

In the first period (at t = 1), i.e., at the time when the mechanism is designed, the intermediary does not know the product performance of the respective firms. Because in equilibrium the intermediary’s prior beliefs are distributed in the same way as those of the consumers, the search engine design itself does not depend on the product performance of the firms present in the market. At the beginning of period 2, the intermediary obtains information about the firms respective product performance levels, before consumers start their search. It becomes clear below that the intermediary generally has a strict incentive to obtain such information, e.g., as a result of its own product testing, or using third-party data. The ranking thus occurs under complete information, whereas the search engine design is chosen under incomplete information: the intermediary expects a surplus dispersion of $\bar { \delta } _ { u } = E ( u _ { H } - u _ { L } )$

Proposition 4 (Optimal Search Engine Design). Assume that at an optimal search engine design ∗ condition (20) holds. Then the intermediary’s optimal first-period search engine needs to satisfy

$$
\begin{array}{l} \frac {d \hat {\mu} _ {u} ^ {(1)} (\theta)}{d \theta} \Big | _ {\theta = \theta^ {*}} \\ \leq \frac {F (\hat {\mu} _ {u} ^ {(1)} (\theta^ {*}))}{(1 - \frac {\theta^ {*}}{1 - \theta^ {*}} \bar {\delta} _ {u}) f (\hat {\mu} _ {u} ^ {(1)} (\theta^ {*})) + f (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta^ {*}))} \frac {\bar {\delta} _ {u}}{(1 - \theta^ {*}) ^ {2}}, \end{array}\tag{27}
$$

whereby equality in (27) holds whenever the optimum is interior, so that $\theta ^ { * } > 0$

Provided that an optimal search engine design $\theta ^ { * }$ satisfies condition (20), this design must be such that the increase of consumers in the system is balanced against the tendency of firms to reduce their bids when the weight on product performance is very large. The left-hand side of (27) is equal to $h ^ { \prime } ( \breve { \theta ^ { * } } ) ( \mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) } )$ and corresponds to the change of the probability that firm H wins the auction, times the expected (nonintermediated) gain from searching twice over searching once. The first term on the right-hand side is akin to a hazard rate, while second term is the expected utility difference, weighted by the design parameter.

Note that relation (27) provides a necessary condition for the optimal search engine design $\theta ^ { * } \colon$ due to nonconvexities in the input distributions, condition (27) may allow for several solutions corresponding to local extrema of the intermediary’s ex ante expected profits. As long as $h ^ { \prime \prime } > 0$ (implying a fast increase of the consumers’ expected payoff in ), condition (27) implies that the optimal weight on product performance decreases as the expected difference in product performance increases, which indicates the intermediary’s desire to maintain incentives for the low-type firm to participate with nonzero bids. In case the simplifying condition (20) is not satisfied, the optimal search engine design $\theta ^ { * }$ maximizes the intermediary’s profit (25) in which one needs to substitute the equilibrium quantities $\alpha _ { 1 } ( \theta ) , \alpha _ { 2 } ( \theta ) , \alpha ( \theta )$ , and $\Delta ( \theta )$ that can be obtained by solving the equilibrium system (22). The corresponding one-dimensional maximization problem can then be solved numerically.

We now contrast the intermediary-optimal design to a design that maximizes overall welfare. Because in equilibrium consumers of search classes 1 and 2 eventually purchase a product, the total ex ante expected consumer surplus is

$$
\begin{array}{l} \text {CS} = \int_ {0} ^ {c _ {2}} (\mu_ {u} ^ {(2)} - 2 c) f (c) d c + \int_ {c _ {2}} ^ {c _ {1}} (\hat {\mu} _ {u} ^ {(1)} - c) f (c) d c \\ \qquad = \alpha_ {1} \hat {\mu} _ {u} ^ {(1)} + \alpha_ {2} \mu_ {u} ^ {(2)} - \int_ {0} ^ {c _ {1}} c f (c) d c - \int_ {0} ^ {c _ {2}} c f (c) d c. \end{array}\tag{28}
$$

Overall (ex ante) social welfare W in the system is then defined as the sum of ex ante expected firm profits, intermediary profits and consumer surplus, so that $W = \alpha _ { 1 } + \alpha _ { 2 } + { \mathrm C S }$ . The following proposition provides a necessary optimality condition for a welfare-maximizing search engine design, provided that condition (20) holds at the optimum.

Proposition 5 (Consumer-Surplus and Welfare-<sup>Maximizing</sup> <sup>Design).</sup> (i) Consumer surplus is nondecreasing in the design parameter . (ii) The unique ex ante social-welfare maximizing search engine design is to rank based exclusively on product performance by setting $\theta _ { W } ^ { * } = 1$

Unlike the firms (as seen in the previous section, cf. Footnote 24), consumers always prefer a maximum of transparency, which is then also socially optimal as the pie $( \alpha _ { 1 } + \alpha _ { 2 } )$ to be shared between firms and intermediary increases in the weight  on product performance. As a result obfuscation is socially wasteful: the intermediary’s self-interested behavior of choosing a revenue-maximizing design introduces systematic obfuscation into the market place, which—even though anticipated by the consumers— limits the transparency of the resulting intermediated search market. From a public policy perspective a larger degree of transparency may be desirable. It may be achieved through private and/or publicsector organizations such as SearchEngineWatch.com (which reveals the performances of various search engines and thus indirectly enforces market discipline) or the Federal Trade Commission (which may act upon receiving consumer complaints).

![](/api/attachments/DZZ45VXE/fulltext/images/9e58dd21875d35b5fd26da657f70df1f12ee8a4da5319fb0ed6badaae3bed13c.jpg)

<sup>Example.</sup> As a practical illustration of our results (cf. Figure 6), we now consider the concrete case in which the probability densities f and g are constant on ${ \mathcal { C } } = [ 0 , 1 ]$ and $\mathcal { U } = [ 0 , 1 ] ^ { 2 }$ respectively. Under this specification, we find that (for $\theta = 0 )$ the consumer’s expected surplus after one search is $\mu _ { u } ^ { ( 1 ) } = 1 / 2$ and after two searches it is $\mu _ { u } ^ { ( 2 ) } = 2 / 3$ . Hence, by Lemma 2 and (23) the intermediated consumer search classes are given by $\alpha _ { 1 } ( \theta ) = 2 \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) - ( 2 / 3 )$ and $\alpha _ { 2 } ( \theta ) =$ $( 2 / 3 ) - \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta )$ . On the other hand, from (22) we obtain that the consumers’ expected benefit from searching once using the search intermediary is

$$
\hat {\mu} _ {u} ^ {(1)} (\theta) = \frac {1}{3} + 2 \int_ {0} ^ {1} \varphi (s, \theta) (1 - s) s d s,
$$

where the probability / that the high-type firm wins a rank-one referral in a mixed-strategy bidding equilibrium is given by the last relation in (23) with $\alpha ( \theta ) =$ $( 1 / 3 ) + \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta )$ . By (20) we know that for $\theta \leq { \overline { { \overline { { \theta } } } } } =$ $\alpha ( 0 ) / ( \alpha ( 0 ) + 1 ) = 2 / 5$ the intermediary is guaranteed a nontrivial mixed-strategy equilibrium. Maximizing the intermediary’s expected profits $\alpha _ { 1 } ( \theta ) - ( \alpha _ { 1 } ( \theta ) +$ $\alpha _ { 2 } ( \theta ) ) \bar { \Delta } ( \theta ) = ( 2 - ( \theta / 3 ( 1 - \theta ) ) ) \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) - 2 / 3$ with respect to the design parameter , we find $\theta ^ { * } \approx 0 . 3 4$ , leading to an optimal expected equilibrium profit of $\equiv _ { \ast } _ { \ast } \approx 0 . 3 9 ,$ a 17% improvement over its expected equilibrium profits of $1 / 3$ at $\theta = 0$ . Taking the socially optimal solution $\theta _ { W } ^ { * } = \theta _ { F } ^ { * } = 1$ as a benchmark, the intermediary reduces ex ante consumer surplus ${ \mathrm { C S } } =$ $( 2 / 9 ) - ( ( 2 / 3 ) - \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) ) \hat { \mu } _ { u } ^ { ( 1 ) } ( \theta )$ by 23% from ${ \mathrm { C S } } ( \theta _ { W } ^ { * } ) =$ $2 / 9 \approx 0 . 2 2 2 2$ to $\mathrm { C S } ( \theta ^ { * } ) \approx 0 . 1 7 1 2$ . Similarly, the number of consumers using the engine is reduced by 13%, from $2 / 3$ to about 05786. We should note, however, that in the absence of the intermediary consumers would expect ${ \overline { { u } } } _ { 0 } ,$ i.e., only zero surplus. <sup></sup>

## 5. Conclusion

In this section we discuss managerial implications of our results and theoretical contributions of this research, including its current limitations. We then provide some directions for further research.

Managerial Implications. Let us first consider our important conclusions regarding the design of a mechanism for selling paid referrals. If consumers observe bids and the weight on product performance in the ranking function is greater than zero, then consumers could rationally infer that in expectation bids from the lower-performance firm would be (weakly) higher and adjust their search order accordingly, starting their inspections with the firm bidding less. However, this would in turn (by a process of “unraveling”) remove the incentive for the lower-performance firm to bid at all and thus result in a zero-bid equilibrium unfavorable for the intermediary. On the other hand, if the intermediary places no weight on product performance in its ranking function, then by Proposition 2 (for $\Delta = 0 )$ we obtain a symmetric bidding equilibrium in mixed strategies and consumers cannot infer anything (even in expectation) from the observed bid amounts; they thus do not have any incentive to change their order of inspection to anything different from the order the intermediary provides to them. Naturally, market transparency would be minimal in that case, to the detriment of consumers, by Lemma 2 resulting in a minimum number of consumers $( \alpha _ { 1 } + \alpha _ { 2 } )$ using the intermediary’s site. We can thus conclude that if the firms’ bid amounts are known to the consumers, then it is optimal for the intermediary to base the ranking purely on the bid amounts, which is the current choice of leading search intermediaries such as Yahoo! or Nextag. However, when the firms’ bid amounts are not known to the consumers, as is the case with 95 percent of

Overture’s click-throughs (which take place at affiliates’ sites), then we argue that it is possible for the intermediary to increase revenues by choosing an optimal search engine design parameter $\theta ^ { * } \in [ 0 , 1 )$ in accordance with Proposition 4. If it turns out to be profitable to use the firms’ product performance (or a correlated indicator such as consumer feedback) in the ranking $( \mathrm { i . e . , } \theta ^ { \ast } > 0 )$ , then the intermediary would rationally spend an amount, which at most equals its expected gains of $\overline { { \overline { { \pi } } } } _ { I } ( \theta ^ { * } ) - \overline { { \overline { { \pi } } } } _ { I } ( 0 )$ , to obtain this product performance information (from third parties or own research; cf. also Footnote 3). We note that in order to optimize the search engine design, the intermediary needs to have some beliefs about the consumers’ search cost and the surplus of the firms’ products (in terms of the cfd’s F and G).

Given a search engine design $\theta > 0 ,$ the firms’ equilibrium bidding strategies in Proposition 2 are such that often (but not always!) it is best for a low-type firm to bid higher in expectation than the high-type firm, in order to take advantage of $\alpha _ { 1 } { \mathrm { - c o n s u m e r s } }$ with high sampling cost. In fact, it is the presence of a low-type firm and the externality it exerts on a high-type firm that generates revenue for the search intermediary (cf. also Bandyopadhyay et al. 2005). The low-type firm, in trying to obtain rents from $\alpha _ { 1 } { \mathrm { - c o n s u m e r s } } ,$ spends all its expected surplus on bidding, whereas the high-type firm which obtains rents from both $\alpha _ { 1 } \cdot$ and $\alpha _ { 2 } \cdot$ -consumers, spends as much on bidding so as to make the low-type firm in equilibrium indifferent between staying in and dropping out. The more the low-type firm sees its chances in using a high search-ranking to sell to consumers with a high opportunity cost of time, the more rent a search intermediary is able to appropriate, thereby naturally limiting the transparency of the market. As a perhaps surprising conclusion, we have seen at the end of §3 (cf. Footnote 24) that it may be sometimes (at least locally) not only in the intermediary’s but also in the firms’ best interest to limit transparency, $\mathrm { i . e . , }$ to decrease the search engine design parameter . In contrast to this, consumers always prefer higher transparency, as it increases their expected utility from inspecting the most promising (rank-one) referral. The presence of the search intermediary in our model is generally welfare improving (though naturally not welfare maximizing), in contrast to Posner’s (1975) “dissipation” and “wastefulness” postulates alluded to in §1. We have shown that the intermediary manages to appropriate all of the expected rents of the low-performance firm, which tends to bid higher expected amounts for rank-one referrals than its highperformance competitor to compensate for this performance difference. As a result, given the weighted average that a revenue-maximizing search intermediary is likely to choose in its ranking function, consumers should be concerned about the endogenous obfuscation in the search results provided by an information intermediary, and adapt their behavior, which in turn will tend to moderate the intermediary’s opportunistic course of action.

Contributions and Limitations. Our paper is among the first attempts to address mechanism design issues for search intermediaries. We provide a model of an intermediated search market, whereby the intermediary adopts a bidding model for selling referrals to competing firms, as is the current practice of many leading search intermediaries. The resulting auction with interdependent valuations is in reality complicated by the fact that actual payments occur stochastically, only when consumers actually click through on the referrals provided by the intermediary. To make the model tractable we assumed a single bidding round, so that some of the dynamic traits found in the data, such as end-of-day effects, weekend dropouts, or interbid correlation, cannot be replicated in our single-period model. Our empirical observations (cf. Appendix B) can thus serve only as anecdotal evidence (as is the case with most data when trying to confirm game-theoretical conclusions), and we hope that further research can shed more light on the intertemporal bidding behavior of firms, which interestingly is (in light of the firms’ often very significant total expenditures on paid referrals) sometimes aided by “bidding agents.” We believe that the mixing of bids that can be found in the data corroborates our rent-seeking interpretation and that the results of our model can be widely applied where referrals are common practice, such as in real estate, the law, accounting, and medicine. Our results can also be applied to brokerages, where referral payments are generally not observable by the end consumer. The generic lack of transparency in equilibrium can also be interpreted as a consequence of an intermediary’s inability to commit to a specific ranking function, if allocations are not fully verifiable by the participating firms. Such a lack of commitment ability can naturally be expected in at least some of the aforementioned industries.

Directions for Future Research. As The Economist (2002, pp. 23 and 24) noted, “the Internet is being transformed, from a vast repository of mostly free content into a commercial cauldron in which almost everything is available ... [e]ven Internet search terms.” In this paper, which is part of a larger research program on search efficiency, we attempt to shed some light on this phenomenon of decreasing transparency on the Internet by constructing an empirically validated model of paid referrals in this intermediated search environment. Future research could proceed along the following three axes: (1) formulate the referral auction as a dynamic game and examine the resulting intertemporal bidding strategies, which can then be directly compared to the available timeseries bidding data; (2) find and examine more general revenue-maximizing mechanisms for providing intermediary supply-demand matching services; and (3) allow for competition among multiple heterogeneous intermediaries using differentiated mechanisms for allocating referrals (cf. Bhargava et al. 2007 for a first step in this direction).

## Acknowledgments

Research was supported in part by a David Morgenthaler II Faculty Scholar Award at Stanford University. The authors thank Krishnan Anand, Hemant Bhargava, Erik Brynjolfsson, Eric Clemons, David Croson, Rachel Croson, Sanjeev Dewan, Lorin Hitt, Paul Kleindorfer, Howard Kunreuther, Edieal Pinker, Roy Radner, Jagmohan Raju, Arun Sundararajan, Christian Terwiesch, John Zhang, two anonymous referees, as well as participants of seminars at the University of Michigan, New York University, University of Rochester, Stanford University, the Wharton School, and colleagues at the 2002 Workshop on Information Systems and Economics (WISE) and the 2006 INFORMS Annual Meeting for helpful comments. The authors are also grateful to Overture Services Inc. (now Yahoo! Search Marketing), who graciously agreed to share a portion of their bidding data with them.

## Appendix A. Proofs

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>1.</sup> Note first that always $\mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) } \leq$ $\mu _ { u } ^ { ( 1 ) }$ , i.e., the expected gain in utility by one additional search cannot exceed the expected utility from a single search. Using (2) the expected ex ante benefit from searching twice is

$$
\begin{array}{r l} & {\mu_ {u} ^ {(2)} = \int_ {\mathcal {U}} \max \{u _ {1}, u _ {2} \} g (u _ {1}, u _ {2}) d (u _ {1}, u _ {2})} \\ & {\quad \leq \int_ {\mathcal {U}} (u _ {1} + u _ {2}) g (u _ {1}, u _ {2}) d (u _ {1}, u _ {2}) = 2 \mu_ {u} ^ {(1)},} \end{array}
$$

since $\mathcal { U } \subset \mathbb { R } _ { + } ^ { 2 }$ by assumption. Naturally, the partition of the consumer base $\mathcal { C } ,$ , outlined in Lemma 1, is free of overlaps, so that $\alpha _ { 0 } + \alpha _ { 1 } + \alpha _ { 2 } = 1$ . Let $\mathcal { A } _ { k }$ be the set of consumers for whom searching k times is individually rational (cf. Footnote 10). For $k \geq 1$ searches it is $\mathcal { A } _ { k } \overset { \cdot } { = } [ 0 , F ( \pmb { \mu } _ { u } ^ { ( k ) } ) ] \cap \mathcal { C } ,$ , so that $\mathcal { A } _ { 2 } \subset \mathcal { A } _ { 1 }$ and $\mathcal { A } _ { 0 } = \mathcal { C } \backslash \mathcal { A } _ { 1 }$ . In other words, consumers in $\mathcal { A } _ { 1 }$ who search at least once might also search twice, and those that do not search at all are in the complement of $\mathcal { A } _ { 1 }$ with respect to $\mathcal { C } .$ . The marginal consumers are determined by the distribution function F evaluated at the expected benefit $\mu _ { k } ^ { ( k ) }$ of searching k times. It is ex ante incentivecompatible for a consumer $c \in \mathcal { A } _ { 1 }$ to perform $k ^ { * } ( c ) = 2$ instead of just one search if and only if $\begin{array} { r } { \dot { \mu } _ { u } ^ { ( 2 ) } - 2 c \geq \mu _ { u } ^ { ( 1 ) } - c , } \end{array}$ or, equivalently, if and only if $c \in [ 0 , F ( \mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) } ) ] \cap \mathcal { C } \subset \mathcal { A } _ { 2 }$ This yields the proposed segmentation of the consumer base  into search classes with $\alpha _ { 2 } = | { \mathcal { A } } _ { 2 } | , \alpha _ { 1 } = | { \mathcal { A } } _ { 1 } \backslash { \mathcal { A } } _ { 2 } |$ , and $\alpha _ { 0 } = 1 - \alpha _ { 1 } - \alpha _ { 2 } ,$ which concludes our proof. <sup></sup>

Proof of Proposition 1. <sub>(i)</sub> <sub>For</sub> <sub>any</sub> <sub>given</sub> $\theta \in [ 0 , 1 ]$ let $\lambda \in [ 0 , \Delta ( \theta ) ]$ be an arbitrary constant. If firm L bids $b _ { L } ^ { * } = 1 + \lambda$ , then firm H’s lowest winning bid is $b _ { H } ^ { * } = b _ { L } ^ { * } - \Delta =$ $1 + \lambda - \Delta$ . Its payoffs at that bid are $\pi _ { H } ^ { * } = ( 1 - b _ { H } ^ { * } ) h ( \theta ) =$ $\Delta - \lambda \geq 0 ,$ , where $\dot { h } ( \theta ) \equiv 1$ is firm H’s probability of winning the auction. Hence, there is no reason for firm H to deviate from this equilibrium strategy. Firm L also has no reason to deviate, because its profits cannot increase beyond zero by increasing (or decreasing) its bid. (ii) If firm L expects a random number of clicks, then in a pure-strategy equilibrium firm L can never recoup its cost, implying nonparticipation by the low-type firm. <sup></sup>

Proof of Proposition 2. <sub>Because</sub> $\theta \in [ 0 , \bar { \theta } )$ , it is $\alpha > \Delta$ . If the firm of performance-type H randomizes over bids with probability distribution $P _ { H }$ and the firm of performancetype L randomizes over bids with probability distribution $Q _ { L }$ , then the firms’ respective expected payoffs are

$$
\bar {\pi} _ {H} (P _ {H}, Q _ {L}) = \int_ {0} ^ {\alpha - \Delta} (1 - z) (\alpha_ {1} Q _ {L} (z + \Delta) + \alpha_ {2}) d P _ {H} (z)\tag{A1}
$$

for firm H, and

$$
\bar {\pi} _ {L} (P _ {H}, Q _ {L}) = \int_ {\Delta} ^ {\alpha} (\alpha_ {1} (1 - y) P _ {H} (y - \Delta) - \alpha_ {2} y) d Q _ {L} (y)\tag{A2}
$$

for firm L. Note that in equilibrium the support of firm $H ^ { \prime } \mathbf { s }$ bids is contained in $[ 0 , \bar { \alpha } - \Delta ]$ whereas the support of firm L’s nonzero bids is contained in $[ \Delta , \alpha ]$ (bidding less than " results in a sure loss of the auction for firm L so that bidding zero is better). Because by part (ii) of Proposition 1 a pure-strategy equilibrium does not exist, we look for a mixed-strategy equilibrium. Firm H is willing to randomize on the support $[ 0 , \alpha - \Delta ]$ if and only if the integrand in (A1) is equal to a constant $c _ { H } , \mathrm { i . e . } ,$

$$
(1 - z) (\alpha_ {1} Q _ {L} (z + \Delta) + \alpha_ {2}) = c _ {H}\tag{A3}
$$

for all $z \in [ 0 , \alpha - \Delta ]$ . By setting $z = \alpha - \Delta$ we find that $c _ { H } =$ $( \alpha _ { 1 } + \alpha _ { 2 } ) ( 1 - \alpha + \Delta )$ . Thus, by substituting $y = z + \Delta$ and the expression for $c _ { H }$ in (A3), firm $L ^ { \prime } \mathrm { s }$ bid distribution can be written in the form (16) for all $y \in [ 0 , \alpha ]$ . Similarly, setting the integrand in (A2) equal to a constant $c _ { L } ,$ , i.e.,

$$
\alpha_ {1} (1 - y) P _ {H} (y - \Delta) - \alpha_ {2} y = c _ {L}
$$

for all $y \in [ \Delta , \alpha ]$ , we obtain $c _ { L } = \alpha _ { 1 } ( 1 - \alpha ) - \alpha _ { 2 } \alpha$ (by setting $y = \alpha )$ , and thus (with $z = y - \Delta )$ relation (15). By construction, the distributions $P _ { H }$ and $Q _ { L }$ in (15) and (16) constitute a mixed-strategy equilibrium of the bidding game.

We now show that this mixed-strategy equilibrium is unique. Suppose that there is another mixed-strategy equilibrium with respective bid distributions $\hat { Q } _ { L }$ for firm $L ,$ and $\hat { P } _ { H }$ for firm H. By the same argument as above the respective supports for these distributions must be contained in $[ 0 , \alpha ]$ and $[ 0 , \alpha - \Delta ]$ respectively. It is also clear that $Q _ { L }$ is constant on the interval $( 0 , \Delta )$ because such positive bids lead to a sure loss for firm L. Thus, the only way the equilibrium described by $\hat { Q } _ { L } , \hat { P } _ { H }$ can differ from the one described by $Q _ { L } , P _ { H }$ is if the support of the new mixedstrategy equilibrium differs by a set of nonzero measure. In other words, there exists a bid amount so that a firm does not submit any bid in the neighborhood of that bid amount. But then the other firm can ensure winning the all-pay auction for sure by bidding that amount (plus or minus ") for sure, resulting in a pure-strategy equilibrium. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>3.</sup> (i) We assume that both firms L and H follow the mixed equilibrium strategies according to $q _ { L } ^ { * } ( \cdot )$ and $p _ { H } ^ { * } ( \cdot )$ specified in (15)–(16). Then, based on (7) and using (17), firm H expects to net the profits

$$
\begin{array}{l} \bar {\pi} _ {H} ^ {*} = \int_ {\mathbb {R} _ {+} ^ {2}} \pi_ {H} (y, z) q _ {L} ^ {*} (y) p _ {H} ^ {*} (z)   d (y, z) \\ \qquad = \alpha_ {1} \bigg (\frac {1 - \alpha}{1 - \Delta} \bigg (\frac {\Delta}{\alpha} \bigg) ^ {2} + \frac {\Delta}{\alpha} \bigg (\frac {\alpha - \Delta}{\alpha (1 - \Delta)} - \bar {b} _ {H} ^ {*} \bigg) + B _ {H} ^ {*} \bigg) \\ \qquad + \alpha_ {2} (1 - \bar {b} _ {H} ^ {*}), \end{array}\tag{A4}
$$

where using (15)

$$
\begin{array}{l} B _ {H} ^ {*} = \int_ {0 +} ^ {\alpha - \Delta} (1 - z) p _ {H} ^ {*} (z) \bigg [ \int_ {\Delta} ^ {z + \Delta} q _ {L} ^ {*} (y) d y \bigg ] d z \\ = \frac {1 - (\alpha - \Delta)}{\alpha} \bar {b} _ {H} ^ {*}. \end{array}\tag{A5}
$$

By substituting the expressions (17) and (A5) into (A4), one obtains that $\bar { \pi } _ { H } ^ { * } = \alpha _ { 2 } + ( \alpha _ { 1 } + \alpha _ { 2 } ) \Delta$ . Let us now turn to the expected equilibrium profits for firm $L ,$ which using (8) as well as (18) can be written as

$$
\begin{array}{r l} & {\bar {\pi} _ {L} ^ {*} = \int_ {\mathbb {R} _ {+} ^ {2}} \pi_ {L} (y, z) q _ {L} ^ {*} (y) p _ {H} ^ {*} (z) d (y, z)} \\ & {\quad = \alpha_ {1} \bigg (\frac {(1 - \alpha) \Delta}{\alpha (1 - \Delta)} \bigg (\frac {\alpha - \Delta}{\alpha} - \bar {b} _ {L} ^ {*} \bigg) + B _ {L} ^ {*} \bigg) - \alpha_ {2} \bar {b} _ {L} ^ {*},} \end{array}\tag{A6}
$$

where with (16) and (18):

$$
\begin{array}{r} B _ {L} ^ {*} = \int_ {\Delta} ^ {\alpha} q _ {L} ^ {*} (y) (1 - y) \biggl [ \int_ {0 +} ^ {y - \Delta} p _ {H} ^ {*} (z) d z \biggr ] d y \\ = \frac {(1 - \alpha) \Delta}{\alpha (1 - \Delta)} \biggl (\bar {b} _ {L} ^ {*} - \frac {\alpha - \Delta}{\alpha} \biggr) + \frac {1 - \alpha}{\alpha} \bar {b} _ {L} ^ {*}. \end{array}\tag{A7}
$$

Substituting expressions (18) and (A7) into (A6) yields that $\bar { \pi } _ { L } ^ { * } = 0 . \mathrm { ~ ( i i ) }$ In period one, both firms expect the same equilibrium profits $\bar { \bar { \pi } } _ { F } ^ { * }$ . With probability $\mathrm { P r o b } ( \Delta \geq \alpha )$ a zero-bid equilibrium occurs in which $\bar { \overline { { \pi } } } _ { F } ^ { * } \vert _ { \Delta \geq \alpha } = ( \alpha _ { 1 } + \alpha _ { 2 } ) / 2$ In the event that this is not the case, both firms expect to bid the positive amount $( \bar { b } _ { L } ^ { * } + \bar { b } _ { H } ^ { * } ) / 2 ,$ so that with probability $\bar { \mathrm { P r o b } } ( \Delta \sim \alpha )$ we obtain using part (i) that $\bar { \overline { { { \pi } } } } _ { F } ^ { * } | _ { \Delta < \alpha } = \bar { E } ( \bar { \pi } _ { H } ^ { * } | \Delta < \alpha ) / 2$ . This implies expression (19), which completes our proof. <sup></sup>

Proof of Proposition 3. <sub>Let</sub> $( u _ { 1 } , u _ { 2 } ) \in \mathcal { U } ,$ and $u _ { H } , \ u _ { L }$ be defined by $( 5 ) \AA { - } \left( 6 \right)$ . We first consider the case where $\theta \in [ 0 , \bar { \theta } )$ , where ¯ is implied by (14). Thus, there is a nonzero-bid equilibrium with the firms’ choosing equilibrium bid distributions $p _ { H } ^ { * }$ and $q _ { L } ^ { * }$ according to $ ^ { - } ( 1 5 ) \bar { - } ( 1 6 )$ Then the probability that the firm of performance-type H wins the auction is given by

$$
\varphi (u _ {2} - u _ {1}, \theta) = \int_ {[ 0, \alpha ] ^ {2}} \mathbf {1} _ {\{z \geq y + \theta | u _ {2} - u _ {1} | / (1 - \theta) \}} p _ {H} ^ {*} (z; \alpha) q _ {L} ^ {*} (y; \alpha) d (y, z)
$$

where $p _ { H } ^ { * }$ and $q _ { L } ^ { * }$ depend on $\alpha = \alpha ( \theta )$ , which we have explicitly noted. The integration (which is similar to the one carried out in the proof of Lemma 3) yields the explicit expression for $\varphi$ in (22). The (maximum) value of a rankone referral  is in turn determined by Lemma 2 and thus is a function of $\hat { \mu } _ { u } ^ { ( 1 ) }$ . The three equations in (22) therefore determine the tuple $( \alpha , \hat { \mu } _ { u } ^ { ( 1 ) } , \varphi )$ for any given $\theta \in [ 0 , \bar { \theta } )$ . We now consider the situation when $\theta \in [ \bar { \theta } , 1 ]$ which implies a zero-bid equilibrium. In that case, firms do not bid and—as a consequence of our tiebreaking rule which weakly favors the high-performance type—no consumers will search twice, so that $\alpha ( \theta ) \equiv 1$ and correspondingly $\hat { \mu } _ { u } ^ { ( 1 ) } ( \theta ) \equiv \mu _ { u } ^ { ( 2 ) }$ , which completes our argument. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Lemma</sup> <sup>4.</sup> In equilibrium all products will get sold at a unit margin. Thus, $W = \alpha _ { 1 } + \alpha _ { 2 }$ is the sum of the welfare allocated to the search intermediary and both firms $L , H$ . Using Lemma 3 we have that $\equiv _ { \overline { { \pi } } _ { I } ^ { * } } = \mathbf { \bar { ( } } \alpha _ { 1 } + \alpha _ { 2 } ) -$ $2 \overline { { \overline { { \pi } } } } _ { F } ^ { \ast } ,$ which using (12) implies (25). <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>4.</sup> By differentiating (26) with respect to  we obtain:

$$
\frac {\partial \bar {\pi} _ {I} ^ {*}}{\partial \theta} (\theta) = \alpha_ {1} ^ {\prime} - (\alpha_ {1} + \alpha_ {2}) ^ {\prime} \bar {\Delta} - (\alpha_ {1} + \alpha_ {2}) \bar {\Delta} ^ {\prime},\tag{A8}
$$

with

$$
\alpha_ {1} ^ {\prime} (\theta) = [ f (\hat {\mu} _ {u} ^ {(1)} (\theta)) + f (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)) ] (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) h ^ {\prime} (\theta) > 0,\tag{A9}
$$

$$
\alpha_ {2} ^ {\prime} (\theta) = - f (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)) (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) h ^ {\prime} (\theta) <   0,\tag{A10}
$$

$$
\bar {\Delta} ^ {\prime} (\theta) = \bar {\delta} _ {u} / (1 - \theta) ^ {2} > 0.
$$

Substituting the last expressions into (A8) and rearranging yields the equality in (27). If $\theta ^ { * } = 0$ is a strict maximizer of the intermediary’s expected equilibrium profits, then the slope of $\bar { \pi } _ { I } ^ { * } ( \theta )$ must be negative in a right-neighborhood of $\theta ^ { * } = 0 ,$ which implies the inequality in (27). This concludes the proof. <sup></sup>

<sup>Proof</sup> <sup>of</sup> <sup>Proposition</sup> <sup>5.</sup> Differentiating the social welfare W with respect to  yields

$$
\begin{array}{r l} & W ^ {\prime} (\theta) = (\alpha_ {1} ^ {\prime} + \alpha_ {2} ^ {\prime}) (\theta) + \mathrm{CS} ^ {\prime} (\theta) \\ & \qquad = f (\hat {\mu} _ {u} ^ {(1)} (\theta)) (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) h ^ {\prime} (\theta) + \mathrm{CS} ^ {\prime} (\theta), \end{array}\tag{A11}
$$

where CS is given by (28),

$$
C S = \alpha_ {1} \hat {\mu} _ {u} ^ {(1)} + \alpha_ {2} \mu_ {u} ^ {(2)} - \int_ {0} ^ {c _ {1}} c f (c) d c - \int_ {0} ^ {c _ {2}} c f (c) d c.
$$

Using the definition of $c _ { k }$ for $k = 1 , 2$ in Footnote 13 as wel as relation (4), we obtain

$$
\frac {\partial}{\partial \theta} \int_ {0} ^ {c _ {1}} c f (c) d c = c _ {1} f (c _ {1}) c _ {1} ^ {\prime} = \hat {\mu} _ {u} ^ {(1)} f (c _ {1}) f (\hat {\mu} _ {u} ^ {(1)}) (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) h ^ {\prime},
$$

and

$$
\begin{array}{c} \frac {\partial}{\partial \theta} \int_ {0} ^ {c _ {2}} c f (c) d c = c _ {2} f (c _ {2}) c _ {2} ^ {\prime} \\ = - (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)}) f (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)}) (\mu_ {u} ^ {(2)} - \mu_ {u} ^ {(1)}) h ^ {\prime}. \end{array}
$$

As a direct consequence we obtain

$$
C S ^ {\prime} (\theta) = \alpha_ {1} (\theta) (\mu_ {u} ^ {(2)} - \hat {\mu} _ {u} ^ {(1)} (\theta)) h ^ {\prime} (\theta) > 0,
$$

for all $\theta \in \Theta$ . This proves part (i). Part (ii) then follows directly from (A11) after noting that $( \alpha _ { 1 } + \alpha _ { 2 } ) ^ { \prime } ( \theta ) =$ $f ( \hat { \mu } _ { u } ^ { ( 1 ) } ( \boldsymbol { \theta } ) ) ( \mu _ { u } ^ { ( 2 ) } - \mu _ { u } ^ { ( 1 ) } ) \dot { h } ^ { \prime } ( \boldsymbol { \theta } ) > 0$ for all $\theta \in \Theta _ { \varepsilon }$ , which completes the proof. <sup></sup>

## Appendix B. Some Empirical Observations

In this section we provide some empirical observations on firms’ actual referral bidding behavior, which is far from conclusive evidence. Nevertheless, we believe that they can contribute some at least anecdotal justification for our results, which were derived from a one-shot bidding model. In reality firms bid in multiple rounds, and we do hope that further theoretical and empirical research can shed more light on firms’ (behavioral) dynamic strategies when bidding for paid referrals. Our bidding data were obtained from Overture Services, a market leader in the paid search market (taken over by Yahoo! in 2003 for US\$1.63B, and Yahoo! Search Marketing, as of May 2007).

The data stem from the U.S. flower market spanning about 18 months, from January 2001 to August 2002. They contain four variables: firm ID, the search term on which bids are placed, a time stamp for each bid, and the respective bid amounts. In total, 384 firms bid 282,480 times across 12 search terms, with an average bid of \$1.45 per referral (or “click-through”). As a reference, we also report the number of searches (corresponding to $\alpha _ { 1 } + \alpha _ { 2 }$ in our model) incurred in the month of September 2002 with respect to each search term. Bids for paid referrals in the U.S. flower market are substantial: the average bid is above \$1 for eight out of twelve search terms, and some firms are willing to pay as high as \$8.86 for each consumer referral by Overture, whose ranking is entirely based on bid amount (corresponding to $\theta = 0$ in our model). Search terms are auctioned off in a continuous open-bid auction. The firm that bids the most is displayed first; in the case of tied bids the intermediary displays the corresponding firms randomly on their achieved rank.<sup>25</sup>

To examine the firms’ bidding behavior, we focus our analysis on the “flower” search term and we restrict our attention to those 33 firms that bid at least 100 times. Examining individual firms’ bidding histories shows that there is high relative bid dispersion, which can be characterized by the coefficient of variation (corresponding to sample standard deviation divided by sample mean). The coefficient of variation measures the degree of deviation from the mean as a percentage. The average of this coefficient over 33 firms is 35.5%, which implies that firms’ bids fluctuate 35.5% around the mean. We find that relative bid dispersion is high, as 27 out of 33 firms exhibit bids with a coefficient of variation above 30%.

We assume here that firm bidding occurs within “strategic groups” (Caves and Porter 1977, McGee and Thomas 1986) of the flower industry. For simplicity, and to be able to relate our observations to the model, we restrict attention in this paper to strategic groups consisting of two firms. Using as a criterion for competitive bidding a “small” relative difference of not more than 20% in bid averages, we identified six strategic groups among the 33 firms that bid at least 100 times for the search term “flower.” To maximize the signal-to-noise ratio we concentrated on strategic groups with frequent bidding activity and high average bids, which led us to the strategic group consisting of Firms 352 and 356 for closer examination.<sup>26</sup> From July 28, 2002 to August 31, 2002, Firm 352 bid 452 times with average amount \$3.42, and Firm 356 placed 477 bids averaging \$3.02.

Figure B.1 plots the two firms’ bids over a time interval from July 28 through August 31, 2002. In §3 we showed that

Figure B.1 Firms 352 and 356’s Bidding Behavior (July 28–August 31, 2002)  
![](/api/attachments/DZZ45VXE/fulltext/images/e492911494e0a1f0f967417d612db82e3eda2bc7efa9b6e6682ef8cf996aec03.jpg)  
a pure-strategy Nash equilibrium does not exist for $\theta = 0 ,$ as is the case for Overture. However, according to Proposition 2 there is a unique mixed-strategy Nash equilibrium, with bid densities specified by (15)–(16). Note that $p _ { H } = q _ { L } ,$ if $\Delta = 0 .$ The latter condition is satisfied, because Overture’s engine design is such that  0 (full ranking weight on bid). We test the goodness-of-fit of our derived mixed strategy with respect to the bidding data collected for Firms 352 and 356. For this purpose we use the quantile-quantile (Q-Q) plot technique (Chambers et al. 1983, Johnson and Wichern 1998), a graphical technique for determining if two data sets come from populations with a common distribution. For identical distributions (up to scaling and translation) the Q-Q plot naturally degenerates to a straight line. Using linear regression it is then possible to test the goodness-of-fit between each firm’s sample bid distribution and the theoretical distribution. Our hypotheses are therefore

$H _ { 3 5 2 } / H _ { 3 5 6 } \colon$ Firm’s 352/356 bidding data is consistent with (15)–(16) and $\theta = 0 ,$

We first generated 1,000 bids according to the theoretical equilibrium densities in Proposition 2. Overture, for example, originally based its rankings purely on the bid amount, so that  is zero in this case (so that $\Delta = 0$ as a consequence). The precise value of $\alpha \in ( 0 , 1 )$ is immaterial to the Q-Q analysis. Using this simulated data, we then plotted two Q-Q charts as shown in Figure B.2, with the theoretical data at the x-coordinate and the observed data at the y-coordinate. The distance of the curve to the reference line (the straight line in the plots) reflects the closeness of the theoretical distribution to the empirical distribution. The straight line in the Q-Q plot connects the first and the third quartile to provide—as commonly practiced—some visual indication of fit. A correlation-coefficient test is often used to measure the straightness of the Q-Q plot (Johnson and Wichern 1998, p. 193) and thus the fit between the two sample distributions. Computing the correlation coefficients based on 50 data points sampled from the Q-Q plot, we obtain 0.972 and 0.982 for Firms 352 and 356 respectively. Since the firms’ bids are not independent, we need to test the two hypotheses $H _ { 3 5 2 }$ and $H _ { 3 5 6 }$ simultaneously. For this we use the standard Bonferroni correction for multiple comparisons. The corrected critical values (using a oneway test) are $R _ { 5 0 , 0 . 0 5 } ^ { * } = 0 . 9 7 7$ at the 0.05-significance level and $R _ { 5 0 , 0 . 1 0 } ^ { * } = 0 . 9 6 7$ at the 0.10-significance level. This indicates that at the 0.05-level, there is no significant difference between the distributions governing the simulated data and Firm 356’s bidding data. Similarly, there is no significant difference between the simulated data and Firm $3 \bar { 5 } 2 ^ { \prime } \mathrm { s }$ bidding data at a 0.10-level. Thus, neither $H _ { 3 5 2 }$ nor $H _ { 3 5 6 }$ can be rejected by our sample data.

Figure B.2 Q-Q Plots Comparing Firms 352 and 356’s Bidding Behavior to the Theoretical Mixed-Strategy Equilibrium Distribution  
![](/api/attachments/DZZ45VXE/fulltext/images/febd47d01d1798c19d13c92b490b4ab3f734eea976ec27887cb27e1f7a8fdbab.jpg)

The observed bidding data of Firms 352 and 356 indicate that their intertemporal bidding behavior is distributionally consistent with our theoretical mixed-strategy equilibrium specified in Proposition 2. However, as can easily be seen by inspecting the firms’ time-series bidding behavior as well as Figure B.1, those intertemporal bidding strategies are correlated (the corresponding cross-correlation coefficient is 0.65), which is not consistent with the theoretical one-shot mixed-strategy equilibrium (cf. Footnote 21). This suggests that those firms that engage in intertemporal correlated bidding are not myopic when determining their bid amounts. A high bid is more likely to be trumped by an even higher bid. The firms thus seem to iterate through their best-response correspondences yielding a noticeably cyclical behavior.

## Appendix C. General Ranking Functions

We now discuss the generality of the intermediary’s search engine design based on the ranking function r in (3), in which the relative weight placed on consumer surplus versus bids is a convex combination determined by the design parameter $\theta \in \left[ 0 , 1 \right]$ . For this, let us consider an alternative, more general, smooth ranking function $\rho ( b , u ; \vartheta )$ which depends on a design parameter $\vartheta \in [ 0 , 1 ]$ . In order not to

![](/api/attachments/DZZ45VXE/fulltext/images/3c7266310540a118cced653b94c1c05930ce3e36f455843cf827ebdaa80353ac.jpg)  
induce perverse bidding behavior, it is clear that for each feasible value of ; the ranking function $\rho$ needs to be increasing in both b and $u .$ As a result, given the surplus realizations $u _ { H }$ and $u _ { L }$ and firm $j ^ { \prime } \mathbf { s }$ bid $\breve { b } _ { j }$ with $j \in \{ L , H \}$ firm $i \neq j$ (with $i \in \{ L , H \} )$ needs to bid such that

$$
\rho (b _ {i}, u _ {i}; \vartheta) \geq \rho (b _ {j}, u _ {j}; \vartheta)\tag{C.1}
$$

in order to win the auction (with the inequality being strict in case $i = L )$ . Using the implicit function theorem (Rudin 1976, pp. 224–225), there is a smooth function $\beta ( u _ { i } , \rho ( b _ { j } , u _ { j } ; \vartheta ) ; \vartheta )$ such that the inequality (C.1) can be rewritten in the form

$$
b _ {i} \geq \beta (u _ {i}, \rho (b _ {j}, u _ {j}; \vartheta); \vartheta)\tag{C.2}
$$

for any $\vartheta \in [ 0$ 1 . To address the question about the relative importance of bids versus surplus in the ranking of firms we assume that the intermediary’s mechanism parametrization is chosen such that the ratio

$$
\eta (b, u; \vartheta) \equiv \left(\frac {\partial \rho (b , u ; \vartheta)}{\partial b}\right) ^ {- 1} \left(\frac {\partial \rho (b , u ; \vartheta)}{\partial u}\right)\tag{C.3}
$$

is increasing in ; for any fixed b	 u and $\eta ( \cdot , \cdot ; 0 ) = 0 ,$ $\eta ( \cdot , \cdot ; 1 ) = \infty$ . The last two relations express the natural boundary conditions for the search engine designer which are such that for $\vartheta = 0$ the ranking function does not depend on the firms’ product performance while for $\vartheta = 1$ the ranking function does not depend on the firms’ bids. This in turn implies the firms’ expected payoffs as a function of their bids,

$$
\begin{array}{l} \pi_ {H} (b _ {L}, b _ {H}; \vartheta) \\ = \left\{ \begin{array}{l l} (\alpha_ {1} + \alpha_ {2}) (1 - b _ {H}), & \text { if } b _ {H} \geq \beta (u _ {H}, \rho (b _ {L}, u _ {H}; \vartheta); \vartheta), \\ \alpha_ {2} (1 - b _ {H}), & \text { if } b _ {H} <   \beta (u _ {H}, \rho (b _ {L}, u _ {H}; \vartheta); \vartheta), \end{array} \right. \end{array}\tag{C.4}
$$

and

$$
\begin{array}{l} \pi_ {L} (b _ {L}, b _ {H}; \vartheta) \\ = \left\{ \begin{array}{l l} - \alpha_ {2} b _ {L}, & \text { if } b _ {L} > \beta (u _ {L}, \rho (b _ {H}, u _ {H}; \vartheta); \vartheta), \\ - \alpha_ {2} b _ {L} + \alpha_ {1} (1 - b _ {L}), & \text { if } b _ {L} \leq \beta (u _ {L}, \rho (b _ {H}, u _ {H}; \vartheta); \vartheta), \end{array} \right. \end{array}\tag{C.5}
$$

as well as their response correspondences,

$$
\begin{array}{c} b _ {H} ^ {*} (b _ {L}; \vartheta) = \underset {b _ {H} \geq 0} {\arg \max} \pi_ {H} (b _ {L}, b _ {H}; \vartheta) \\ = \left\{ \begin{array}{l l} [ b _ {L} - \Delta_ {H} ] _ {+}, & \text { if } b _ {L} \leq \alpha + \Delta_ {H}, \\ 0, & \text { if } b _ {L} > \alpha + \Delta_ {H}, \end{array} \right. \end{array}\tag{C.6}
$$

and

$$
\begin{array}{c} b _ {L} ^ {*} (b _ {H}; \vartheta) = \underset {b _ {L} \geq 0} {\arg \max} \pi_ {L} (b _ {L}, b _ {H}; \vartheta) \\ = \left\{ \begin{array}{l l} b _ {H} + \Delta_ {L} + \varepsilon , & \text { if } b _ {H} <   \alpha - \Delta_ {L} - \varepsilon , \\ 0, & \text { if } b _ {H} \geq \alpha - \Delta_ {L} - \varepsilon , \end{array} \right. \end{array}\tag{C.7}
$$

where for any $\alpha \in [ 0$ 1 the function $\Delta _ { i } = \Delta _ { i } ( u _ { i } , u _ { j } , \vartheta , \alpha )$ is implicitly defined by

$$
\beta (u _ {j}, \rho (\Delta_ {j} + \alpha , u _ {i}; \vartheta); \vartheta) = \alpha .\tag{C.8}
$$

Note that in the case where $\vartheta = \theta$ and $\rho = r$ as in (3) we obtain that $\Delta _ { H } = \Delta _ { L } = \Delta$ as in (13). Thus, the analysis in the main portion of the paper remains essentially unchanged except for the fact that the bid difference $\Delta _ { i }$ required for winning (as a result of the intermediary’s consideration of surplus when determining the winning bidder) as perceived by firm $i \in \{ L , H \}$ becomes firm-specific. We now show that $\Delta _ { i }$ is nonnegative, which implies that all the results in the main paper remain qualitatively unchanged. Indeed, for $\vartheta = 0$ relation (C.8), combined with the definition of $\beta$ as the inverse of the ranking function $\rho$ with respect to bids, becomes

$$
\rho (\alpha , u _ {i}; 0) = \rho (\Delta_ {i} + \alpha , u _ {j}; 0),
$$

so that necessarily $\Delta _ { i } = 0$ (given that, by virtue of $\eta ( \cdot , \cdot ; 0 )$ $= 0 ,$ the ranking function $\rho$ is independent of a firm’s product performance and, by assumption, increasing in its bid). From (C.1) and (C.2) we obtain that $\beta$ is—all else equal— decreasing in $\vartheta ,$ for (given any nonzero product performance) as the relative weight of bids decreases the bid necessary to attain a given fixed ranking-function value decreases. Using the assumed monotonicity of $\rho$ we therefore find, by differentiating (C.8) with respect to ;, that

$$
\frac {\partial \Delta_ {i}}{\partial \vartheta} = - \left(\frac {\partial \beta}{\partial \rho} \frac {\partial \rho}{\partial b}\right) ^ {- 1} \left(\frac {\partial \beta}{\partial \vartheta}\right) - \left(\frac {\partial \rho}{\partial b}\right) ^ {- 1} \left(\frac {\partial \rho}{\partial \vartheta}\right) \geq 0,
$$

which thus together with $\Delta _ { i } | _ { \vartheta = 0 } = 0$ implies that $\Delta _ { i }$ is nonnegative for any $\vartheta \in [ 0 , 1 ]$

## References

Akerlof, G. A. 1970. The market for “lemons”: Quality uncertainty and the market mechanism. Quart. J. Econom. 84(3) 488–500.

Aumann, R. J. 1974. Subjectivity and correlation in randomized strategies J. Math. Econom. 1(1) 67–96.

Bandyopadhyay, S., J. M. Barron, A. R. Chaturvedi. 2005. Competition among sellers in online exchanges. Inform. Systems Res. 16(1) 47–60.

Baumol, W., J. Panzar, R. D. Willig. 1982. Contestable Markets and the Theory of Industry Structure. Harcourt Brace Jovanovich, New York.

Baye, M., J. Morgan. 2001. Information gatekeepers on the internet and the competitiveness of homogeneous product markets. Amer. Econom. Rev. 91(3) 454–474.

Baye, M., D. Kovenock, C. de Vries. 1993. Rigging the lobbying process: An application of the all-pay auction. Amer. Econom. Rev. 83(1) 289–294.

Baye, M. R., D. Kovenock, C. G. de Vries. 1996. The all-pay auction with complete information. Econom. Theory 8(2) 291–305.

Bhargava, H. K., J. Feng. 2004. Preferential placement bias in information gatekeepers. Working paper, Pennsylvania State University, University Park, PA.

Bhargava, H. K., V. Choudhary. 2004. Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1) 22–36.

Bhargava, H. K., J. Feng, D. M. Pennock. 2007. Implementing sponsored search in web search engines: Computational evaluation of alternative mechanisms. INFORMS J. Comput. 19(1) 137–148.

Biglaiser, G. 1993. Middlemen as experts. RAND J. Econom. 24(2) 212–223.

Bradlow, E. T., D. C. Schmittlein. 2000. The little engines that could: Modeling the performance of world wide web search engines. Marketing Sci. 19(1) 43–62.

Butters, G. 1977. Equilibrium distributions of sales and advertising prices. Rev. Econom. Stud. 44(3) 465–491.

Caves, R., M. E. Porter. 1977. From entry barriers to mobility barriers. Quart. J. Econom. 91(2) 241–262.

Chambers, J. M., W. S. Cleveland, B. Kleiner, P. A. Tukey. 1983. Graphical Methods for Data Analysis. Duxbury Press, Boston, MA.

Chen, Y., G. Iyer, V. Padmanabhan. 2002. Referral infomediaries. Marketing Sci. 21(4) 412–434.

Clay, K., R. Krishnan, E. Wolff. 2001. Prices and price dispersion on the web: Evidence from the online book industry. J. Indust. Econom. 49

Clemons, E. K., I.-H. Hann, L. M. Hitt. 2002. Price dispersion and differentiation in online travel: An empirical investigation. Management Sci. 48(1) 534–549.

Dasgupta, P., E. Maskin. 1986. The existence of equilibrium in discontinuous economic games, I: Theory. Rev. Econom. Stud. 53(1) 1–26.

Diehl, K., L. Kornish, J. Lynch. 2003. Smart agents: When lower search costs for quality information increase price sensitivity. J. Consumer Res. 30(1) 56–72.

Economist, The. 2002. The Internet sells its soul. Economist (April 20) 23–24.

Edelman, B., M. Ostrovsky, M. Schwarz. 2007. Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1) 242–259.

Ellison, G., S. F. Ellison. 2004. Search, obfuscation, and price elasticities on the internet. Working Paper 10570, National Bureau of Economic Research, Cambridge, MA.

Ewerhart, C., K. Fieseler. 2003. Procurement auctions and unit-price contracts. RAND J. Econom. 34(3) 569–581.

Fudenberg, D., J. Tirole. 1987. Understanding rent dissipation: On the use of game theory in industrial organization. Amer. Econom. Rev. 77(2) 176–183.

Gandal, N. 2001. The dynamics of competition in the internet search engine market. Internat. J. Indust. Organ. 19(7) 1103–1117.

Grossman, G. M., C. Shapiro. 1984. Informative advertising with differentiated goods. Rev. Econom. Stud. 51(1) 63–81.

Guillemin, V., A. Pollack. 1974. Differential Topology. Prentice-Hall, Englewood Cliffs, NJ.

Hann, I.-H., C. Terwiesch. 2003. Measuring the frictional costs of online transactions: The case of a name-your-own-price channel. Management Sci. 49(11) 1563–1579.

Johnson, R., D. Wichern. 1998. Applied Multivariate Statistical Analysis. Prentice Hall, Upper Saddle River, NJ.

Johnson, E. J., W. Moe, P. Fader, S. Bellman, J. Lohse. 2004. On the depth and dynamics of online search behavior. Management Sci. 50(3) 299–308.

Lancaster, K. 1966. A new approach to consumer theory. J. Political Econom. 74(2) 132–157.

Liu, D., J. Chen. 2006. Designing online auctions with past performance information. Decision Support Systems 42(3) 1307–1320.

Lizzeri, A. 1999. Information revelation and certification intermediaries. RAND J. Econom. 30(2) 214–231.

Maynard Smith, J. 1974. The theory of games and the evolution of animal conflicts. J. Theoret. Biol. 47 209–221.

McGee, J., H. Thomas. 1986. Strategic groups: Theory, research and taxonomy. Strategic Management J. 7 141–160.

Morton, F. S., F. Zettelmeyer, J. Silva-Risso. 2001. Internet car retailing. J. Indust. Econom. 49(4) 501–519.

Posner, R. A. 1975. The social costs of monopoly and regulation. J. Political Econom. 83(4) 807–828.

Pratt, J. W., D. A. Wise, R. Zeckhauser. 1979. Price differences in almost competitive markets. Quart. J. Econom. 93(2) 189–211.

Rob, R. 1985. Equilibrium price distributions. Rev. Econom. Stud. 52(3) 487–504.

Rudin, W. 1976. Principles of Mathematical Analysis. McGraw-Hill, New York.

Shapiro, C. 1982. Consumer information, product quality, and seller reputation. Bell J. Econom. 13(1) 20–35.

Simon, L. K. 1987. Games with discontinuous payoffs. Rev. Econom. Stud. 54(4) 569–597.

Smith, M., E. Brynjolfsson. 2001. Consumer decision-making at an internet shopbot: Brand still matters. J. Indust. Econom. 49(4) 541–558.

Spence, M. 1973. Job market signaling. Quart. J. Econom. 87(3) 355–374.

Stahl, D. O. 1989. Oligopolistic pricing with sequential consumer search. Amer. Econom. Rev. 79(4) 700–712.

Stegeman, M. 1991. Advertising in competitive markets. Amer. Econom. Rev. 81(1) 210–223.

Stigler, G. 1961. The economics of information. J. Political Econom. 69(3) 213–225.

Stiglitz, J. E. 1989. Imperfect information in the product market. R. Schmalensee, R. D. Willig, eds. Handbook of Industrial Organization. North-Holland, Amsterdam, The Netherlands, 769–847.

Tirole, J. 1988. The Theory of Industrial Organization. MIT Press, Cambridge, MA.

Tullock, G. 1980. Efficient rent-seeking. J. M. Buchanan, R. D. Tollison, G. Tullock, eds. Toward a Theory of the Rent-Seeking Society. Texas A&M University Press, College Station, TX, 97–112.

Varian, H. R. 1980. A model of sales. Amer. Econom. Rev. 70(4) 651–659.

Weber, T. A., Z. Zheng. 2002. A model of search intermediaries and paid referrals. Working Paper 02-12-01, Department of Operations and Information Management, Wharton School, University of Pennsylvania, Philadelphia, PA.

Zhang, X., J. Feng. 2005. Price cycles in online advertising auctions. Proc. 26th Internat. Conf. Inform. Systems. Association of Information Systems, Las Vegas, NV.

Zwick, R., A. Rapoport, A. Lo, A. Muthukrishnan. 2003. Consumer sequential search: Not enough or too much? Marketing Sci. 22(4) 503–519.
