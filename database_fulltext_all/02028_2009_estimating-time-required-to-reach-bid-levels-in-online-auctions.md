---
otero_id: 2028
otero_key: "BCFQPMPU"
title: "Estimating Time Required to Reach Bid Levels in Online Auctions"
authors: "Subhajyoti Bandyopadhyay; Seema Bandyopadhyay"
year: "2009"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222260309"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/BCFQPMPU/fulltext/images/cc77213706408b1bd735c3a199a8bfe045efd315150cbe9a2a263afc58b4087b.jpg)

# Estimating Time Required to Reach Bid Levels in Online Auctions

## Subhajyoti Bandyopadhyay & Seema Bandyopadhyay

To cite this article: Subhajyoti Bandyopadhyay & Seema Bandyopadhyay (2009) Estimating Time Required to Reach Bid Levels in Online Auctions, Journal of Management Information Systems, 26:3, 275-301

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222260309

![](/api/attachments/BCFQPMPU/fulltext/images/4be80f51cc8cd9d9e9dae4e325bd4b71ffa86fbb126dc6cd4fd6b0541ae3d9fd.jpg)

Published online: 08 Dec 2014.

![](/api/attachments/BCFQPMPU/fulltext/images/cc060898cffbde2f3b27eff8f700910718d9e2b99995867930d8b29c3b6e1b4d.jpg)

Submit your article to this journal

Article views: 9

![](/api/attachments/BCFQPMPU/fulltext/images/6cc056c478eb4fea45050e58cea806ad1c678e206e93054068ea4daddc12a737.jpg)

View related articles

# Estimating Time Required to Reach Bid Levels in Online Auctions

Subhajyo ti Band yo pad hyay and Sem a Band yo pad hyay

Subhajyoti Bandyopadhyay is an Assistant Professor in the Department of Information Systems and Operations Management at the University of Florida, Gainesville. He received his Ph.D. in MIS from Purdue University in 2002. His current research interests include economics of information systems, and information systems policy issues, especially in the area of net neutrality and health informatics. His work has been published in several journals in the areas of information systems and operations management.

Seema Bandyopadhyay is a faculty member in the Department of Computer and Information Science and Engineering, University of Florida, Gainesville. Before joining the University of Florida, she was a Visiting Assistant Professor in the School of Electrical Engineering and Computer Science, University of Central Florida, Orlando. She received her Ph.D. from the School of Electrical and Computer Engineering at Purdue University in 2004. Her research interests include the design and performance analysis of wireless sensor networks, optimization of computer networks, and game theory applied to the design of computer networks. Her work has been published in leading engineering journals, mainly in the area of computer networks.

Abs tract: Sellers in eBay are often small-business owners whose livelihood depends on fast turnaround of their cash flows. Unlike in traditional auctions, these sellers are content to sell as soon as some target price is reached. While a wealth of literature exists on the final rent of the various stakeholders in a traditional auction setting, what is of interest here is to estimate the time required to reach a certain bid level in ongoing auctions. This paper introduces an analytical model to estimate the time it takes an online auction to reach a prespecified price threshold. The motivation for the research is to avoid unnecessary delays in conducting the transaction. Specifying the right duration would benefit small sellers who would realize the revenue proceeds from the sale faster. To this end, we model the bidding process as an infinite quasibirth-death process, characterized by bursts of rapid bidding and subsequent lulls. We obtain closed-form solutions for the transient probability distribution in the frequency domain of the bid prices in an ongoing auction, which are then used to compute the transient probability distributions in the time domain. Experienced auctioneers can use these results to estimate expected ending times for their auctions. Sample observations from online auctions indicate that there may be potential room for improvement for sellers in setting their auction ending times. Simulations of the quasi-birth-death processes back up the theoretical observations.

Key words and phras es : auction bid price, auction cash turnaround time, auctions, “buy it now” price, correlated random walk, electronic auctions, quasi-birth-death process, small business, transient analysis.

Thanks mainly to the online auctioneer eBay, thousands of sellers depend almost entirely on the Internet auctioneer platform to sell their goods. eBay estimates more than 100,000 merchants belong to its “power seller” group [44]. Many sellers often have hundreds of different products being auctioned simultaneously, with the auctions ending at different times. Unlike traditional auctioneers, sellers on eBay are mostly small-business owners whose livelihood depends on fast turnaround of their cash flows [25]. This is so because overruns in start-up costs, lower than anticipated profit margins, and sales that grow slower than expected are among the most common cash drains on small businesses that therefore need all the cash they can get, as fast as they can [1]. The Financial Times estimated the number of eBay sellers who considered online selling as their primary source of income to be around 750,000 in 2006 [12]. Rather than waiting for the possibility of extracting the highest possible surplus from a bidder in a distant future, these sellers are often looking to sell their goods as soon as they reach some target price. In fact, eBay has a mechanism of a “buy it now” price, which is the price at which a bidder can circumvent the ongoing bidding process and buy a product immediately.<sup>1</sup> eBay’s marketing guide states that the advantage of “buy it now” is to “sell your item for the price you want.”<sup>2</sup> Without any guidance as to when this target price might be reached, however, it is not uncommon to find different units of the same product (that are likely sold by different sellers) to have widely varying ending times.

While a wealth of literature exists in analyzing traditional auctions, the motivation of the sellers like those described above in an online platform such as eBay are markedly different, and, as we explain later, so is the mechanism by which interested bidders participate in these auctions. Instead of trying to extract the maximum possible surplus from the sale, which has been the focus in traditional auctions and the associated literature, these sellers who depend on their livelihood on eBay are more interested in a rapid turnaround of their capital than holding out for an extended period of time in the hope of capturing a higher surplus.<sup>3</sup> In fact, the presence of a “buy it now” price in an auction signals the willingness of the seller to forego the possible extra rent that can be obtained through bidding wars in exchange for a quick cash flow. In such an environment, it would be helpful to have some sense of what future prices would be in an ongoing auction. Specifically, when an eBay auctioneer lists a product, it would be valuable to have reasonable estimates of future bids and the likely end time of the auction. That is, he or she would like to know what the probability is that the highest bid is b at time t. A better estimation of this distribution can often lead to significantly faster turnaround times for cash flows and enable better forecasting, which could be invaluable to these small-business owners. Online auctioneer platforms such as eBay can provide such estimates to their sellers as value-added services.

The purpose of this paper is to develop an analytical model to satisfy these ends. As our analysis indicates, in many of the auctions that we observed, sellers often significantly overestimate the time to keep an auction open. If the bidders are assumed to be rational, and have a significant disutility for waiting over this extra time (i.e., the difference between the time the auction is actually kept open and the time that is indicated by our analysis), the sellers would end up keeping the auction open for a greater time than necessary. At the other extreme, overestimating bidder interest for a niche product might result in the auction remaining open for too small an amount of time, and thereby risk not selling the product. Hence, the results should be of interest to academics in the area of auction theory and to auction houses who want to develop value-added services for their sellers.

We should emphasize here that our contribution at this point is more from a theoretical standpoint. As we explain in the third section, the types of products that we monitored in live auctions on eBay typically do not attract huge amounts of traffic, and therefore the very act of observing these auctions amounted to a majority of the traffic for those particular auctions. Thus, even though we calculated reasonable estimates of the various parameters that are required for our analysis, we cannot be completely sure whether our very act of monitoring could have affected the system that we were trying to monitor. The best way to arrive at the estimates of the requisite parameters would have been through analysis of the server data, but unfortunately we could not get access to this data. We would therefore think of our contribution as a theoretical one, with some empirical evidence from our monitoring of the live auctions that indicates that our results have promise from a practical standpoint.

The amount of literature on auctions is vast, and hence we limit our references to a representative collection, considering especially the recent literature on online auctions. The extant literature has looked extensively at the rents of the winning bidders or the auctioneer. Milgrom [33] lays out the basic theory behind single-object auctions, and McAfee and McMillan [30] point out several extensions to this theory. Wilson [47] offers a range of examples where the equilibrium bidding strategies can be computed in closed form. Work has also been done for the case of an uncertain number of bidders (e.g., [31]), and extended to empirical studies of auction prices (e.g., [20, 24]).

The proliferation of online auctions has spawned a wealth of literature in recent years. Stafford and Stern [40] have investigated the reasons consumers use auction sites. Lucking-Reiley [27] studied the effect of auction formats, following up with an overview of what is being auctioned on the Internet and the mechanisms that are being employed [28]. Bajari and Hortacsu provide an overview of research on eBay [5], and the extent of the winner’s curse [4] on eBay. Melnik and Alm [32] considered the seller’s perspective—the effect of seller reputation—again using empirical data from eBay auctions. Other papers that look into reputation and trust issues in online auctions include Utz et al. [42], who look at the effect of feedback comments and reactions on building (and rebuilding) trust in online auctions; Clemons [14], who investigates a third-party seller rating system on eBay; Gregg and Scott [19], who investigate whether online reputation systems are a useful mechanism for potential buyers to avoid fraudulent auctions; and MacInnes et al. [29], who present a conceptual framework for determining what factors affect the likelihood of disputes in eBay transactions. Liu et al. [26] study auction design for selling sponsored links on a search engine results page (often called key word auctions): they consider how to incorporate advertisers past performance information into auction design and find that optimally weighted unit price auctions can generate more revenue than generalized first-price auctions, and that optimal minimum bids generally differ from those prescribed in the mechanism design literature. Other papers on the seller’s perspective include classifying bidding strategies in multiunit Yankee auctions [9] and determining optimal bid increments [6]. Bapna et al. [7] simulate an auction environment to analyze both buyer and seller strategies. From the perspective of revenue realization in online auctions, we mention Ward and Clark [46], who conducted an empirical study to determine the effects of bidding strategy on revenue realized in eBay auctions.

Roth and Ockenfels [37] studied the practice of “sniping” in online auctions in which some bidders try to outbid others just before the auction is scheduled to end in order to prevent further activity. Several other papers have looked at buyer behavior in online auctions—the influence of value signals such as minimum bid, seller reputation, and so on [3]; evidence of herd behavior [15]; and the effect of minimum bid on final auction price [22]. Angst et al. [2] examine the behavioral aspects of bidder conduct in online auctions. Recently, Park and Bradlow [36] developed a general parametric modeling framework for bidding behavior in online auctions, while Gneezy [16] considered a step-level reasoning model to approximate bidding behavior in auctions. Bapna et al. [8] use field-level experiments to estimate the total consumer surplus in online auctions.

Bapna et al. [6] found that there are three types of bidders in online auctions— evaluators, participators, and opportunists. Evaluators are bidders who place a single early bid, opportunists are last-minute bidders, and participators are bidders who continue to participate throughout the auction. Shmueli et al. [39] hypothesize that bid arrivals in online auctions might show characteristics of self-similar processes and model them as a nonhomogeneous Poisson process, and finally try to fit it to empirical data. Bapna et al. [10] employ a real-time estimation approach to predict bidders’ maximum willingness to pay in a multiunit ascending uniform-price and Yankee online auction.

Our model estimates bids over time in an ongoing auction. In contrast to the extant literature that has generally focused on estimating the maximum rent of the various stakeholders at the end of an auction, this model looks at the progression of bid levels during an ongoing auction, and estimates when an acceptable bid level will be reached. As compared to much of the literature that takes a normative approach in analyzing auctions, our analysis concentrates on unique characteristics of online auctions. The result is a “bottom-up” analysis of an online auction through the estimation of two observable parameters of the auction. Two papers that have taken a somewhat similar approach include Jank and Shmueli [21], who illustrate the use of functional data analysis in electronic commerce research, and Wang et al. [45], where the series of bids in an auction is represented by a distribution. In a related setting, stochastic modeling has also been used in marketing literature (e.g., [38]).

Note that not all online auctions can be satisfactorily modeled in the fashion of our research—specifically, we assume that the candidates for using this analysis are for auctions of products whose valuation is generally understood, and can often be readily found elsewhere. Examples of such products include computers and computing products, consumer electronics such as personal digital assistants and mobile phones, and so on.

To the best of our knowledge, none of the existing literature has analytically modeled the process of the transient behavior of how the bid prices evolve as the auction progresses, something that the aforementioned sellers would be interested in. We initially considered an options pricing approach to estimate future prices, but as pointed out in Gopal et al. [17], the fundamental principles of options pricing models do not hold within online auction markets.

## Model

Ongoing bidding in auctions is often characterized by intermittent periods of activity (when prices are bid up) and lulls (i.e., when prices remain static). For example, the very act of bidding may create a momentum in itself, in the sense that an aggressive bid can trigger a flurry of interest and bids from other bidders. At other times, bidders may bide their time waiting for a fresh round of activity.

Online bidding characteristics differ significantly from closed-room, open outcry bidding. The former often span several days, as opposed to a few hours in the more traditional form. The number of bidders changes over the course of the auction, as interested parties search within eBay for a particular product. Even after entering a bidding process, a bidder’s attention is not undivided over the course of the auction. A typical bidder might suddenly recall the ongoing auction and decide to check on the current bids even as he or she goes on with other activities. This type of a bidding behavior closely matches that of those bidders who Bapna et al. [6] categorize as “participators.”<sup>4</sup> We approximate this bidding behavior as follows. Every time a bidder logs into eBay to observe an ongoing auction, he or she might decide to make a higher bid or not. We call this event of visiting eBay and observing the current bid for a product an “interested observation.” In other words, an interested observation occurs when a bidder (either new or existing) turns his or her attention to the auction and visits eBay to check the current bid. Note that this is a different process from the bid arrival process that is empirically observed in Shmueli et al. [39], because this interested observation might or might not result in an increased bid.<sup>5</sup> However, we carried out simulations of this process and found that the emergent bid arrival process shows self-similar behavior, something that has been empirically observed in Shmueli et al. [39].

A bidder will have no idea of when other bidders might decide to check into the auction, so the interarrival times of the interested observations can be assumed to be independent. Further, except at the very end of the auction, we can also reasonably assume that the number of times interested observations occur in two different nonoverlapping time intervals are independent of each other. The arrival of the interested observations of the auction by the bidders is therefore estimated as a Poisson arrival process with arrival rate l. Note that the Poisson assumption is inappropriate at the final stages of the auction because, as can be seen in Roth and Ockenfels [37], there is a heightened bidding activity at that time. For the current analysis, however, we do not need to consider those final few minutes. The results of our model indicate the expected bid price after a certain amount of time, and so a prudent seller would in all likelihood add a buffer time for variance to make sure that the target price is indeed met. Therefore, the price escalation from the bidding war in the final few minutes can be thought to be lagniappe for the seller, and is not germane for our model.<sup>6</sup> The estimates of our analysis thus might well be a little conservative.

To model the momentum of activity,<sup>7</sup> we posit that if an interested observation arrives after a bid resulting in a price increase, the probability is $p _ { 1 }$ that the bidder will make an elevated bid, and the probability that there will not be an increased offer is $q _ { 1 } = 1 - p _ { 1 }$ . If the interested observation occurs after no increase in the bid price, the probability of making an increased offer is $\boldsymbol { q } _ { 2 } = 1 - \boldsymbol { p } _ { 2 }$ , and the probability that there will not be an increased offer is $p _ { 2 } .$ . Generally, due to the momentum effect discussed at the start of this section, we would expect $p _ { 1 } > q _ { 1 }$ and $\begin{array} { r } { p _ { 2 } > q _ { 2 } . } \end{array}$ 8

The bidding process can be modeled as a quasi-birth-death (QB D) process; that is, a continuous-parameter, time-homogeneous Markov chain with an infinitesimal generator that is tridiagonal [35]. The state transition diagram of the QB D process is shown in Figure 1. The number of previously placed bids is the level of the QB D process. Each level n has two states—n and $n _ { + }$ . The state $n _ { _ o }$ represents the state at which the number of bids so far is n and the bid was not increased by the last interested observation. The state $n _ { + }$ is reached when the number of bids so far is n and the bid was increased by the last interested observation. Let the difference between the ith and the (i – 1)th bid be denoted by the independent and identically distributed (i.i.d.) random variables $X _ { i }$ with the probability density function $( \mathrm { p d f } ) f _ { X } ( x )$ . Given the nature of bids in auctions, we assume that the random variables $X _ { i }$ have a bounded support, with the minimum possible value of the random variable being strictly positive. The bid at any time t then depends on the number of bids n made by time t and the increments in the bid values $X _ { 1 } , X _ { 2 } , . . . , X _ { n }$ . Hence, to find the probability distribution of bid values at time t, we need to find (1) the probability the QB D process is in state $n _ { + }$ or $n _ { \mathrm { o } } , n = 1 , 2 , \dots$ . at time t and (2) the distribution of $S _ { _ n } = X _ { _ 1 } + X _ { _ 2 } + \ldots + X _ { _ n }$

In the next section, we first derive the probability distribution that the QB D process is in a given state $( n _ { + } \mathrm { o r } n _ { o } )$ at any time t, and then use these results to derive the probability density and distribution of the bid value at any time t.

## Transient Probability Distributions

The generator matrix $Q$ of the QB D process [23] shown in Figure 1 is given by

$$
Q = \left[ \begin{array}{c c c c c c c c} p _ {2} \lambda - \lambda & 0 & 0 & q _ {2} \lambda & 0 & 0 & 0 & \dots \\ q _ {1} \lambda & - \lambda & 0 & p _ {1} \lambda & 0 & 0 & 0 & \dots \\ 0 & 0 & p _ {2} \lambda - \lambda & 0 & 0 & q _ {2} \lambda & 0 & \dots \\ 0 & 0 & q _ {1} \lambda & - \lambda & 0 & p _ {1} \lambda & 0 & \dots \\ 0 & 0 & 0 & 0 & p _ {2} \lambda - \lambda & 0 & 0 & \dots \\ 0 & 0 & 0 & 0 & q _ {1} \lambda & - \lambda & 0 & \dots \\ 0 & 0 & 0 & 0 & 0 & 0 & p _ {2} \lambda - \lambda & \dots \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots \end{array} \right].\tag{1}
$$

![](/api/attachments/BCFQPMPU/fulltext/images/92eca2680fd0b55afb1a4b22888308fa7cdf9d428f4b634a8d8783b3678c421a.jpg)  
Figure 1. State Transition Diagram of the QB D Process

Let the vector $\pi ( t ) = [ \pi _ { _ { 0 o } } ( t ) , \pi _ { _ { 0 + } } ( t ) , \pi _ { _ { 1 o } } ( t ) , \pi _ { _ { 1 + } } ( t ) , \pi _ { _ { 2 o } } ( t ) , . . . , \pi _ { _ { n o } } ( t ) , \pi _ { _ { n + } } ( t ) , . . . ]$ denote the probability distribution at time t for the QB D process. Here, $\pi _ { n o } ( t )$ represents the probability that the process is in state $n _ { 0 }$ at time t, and $\pi _ { n + } ( t )$ represents the probability that the process is in state $n _ { + }$ in time t. If the time-homogeneous QB D process is regular, its probability distribution $\pi ( t )$ exists and is the solution of the differential equation [13]:

$$
\frac {d}{d t} \pi (t) = \pi (t) Q, \quad \left. \pi (0) = \pi (t) \right| _ {t = 0}.\tag{2}
$$

One sufficient condition for regularity is that the magnitude of each of the diagonal elements of $Q$ is bounded by a common positive number [13]. This condition is satisfied by the generator Q given in matrix (1), and hence a solution for p(t) can be found through Equation (2).

Finding the solution of Equation (2), however, is not straightforward. When Q is finite-dimensional, several techniques exist to obtain the solution of Equation (2) [34]. The solution, however, gets much more complicated when $Q$ is infinite-dimensional. Even in the simplest cases, the solution is hard to evaluate. Several numerical techniques have been developed to solve Equation (2) for Markov processes with infinite dimensional generators [18]. In this paper, we build on the results of Beuerman and Coyle [11] and Zhang and Coyle [48], which provide a way to obtain closed-form solutions for the transient probability distribution of QB D processes in the frequency domain.

Let the vector $\Pi ( s ) = \int _ { 0 } ^ { + \infty } \pi ( t ) e ^ { - s t } d t$ denote the Laplace transform of $\pi ( t )$ , where s is a complex variable. We first use matrix-geometric techniques to obtain the solution for the Laplace transform P(s) and then obtain $\pi ( t )$ by inverting P(s). In Beuerman and Coyle [11] and Zhang and Coyle [48], it is proved that the Laplace transform P(s) of the transient probabilities p(t) satisfies the equations:

$$
\Pi (s) \bigl (Q (s) - s I \bigr) = - \pi (0), \quad \pi (0) = \pi (t) \big | _ {t = 0}.\tag{3}
$$

Theorem 1: If the bidding process was in state $0 _ { + }$ at time $t = 0 ,$ , that $i s ,$ $\pi ( 0 ) = l 0 , l , 0 , 0 , 0 , \ldots J ,$ , then, for $n \geq O ,$ the Laplace transforms $\Pi _ { n + } ( s )$ and $\Pi _ { n o } ( s )$ of the transient probabilities $\pi _ { n + } ( t )$ and $\pi _ { n o } ( t )$ , respectively, are given by

$$
\begin{array}{c} \Pi_ {n +} (s) = \frac {1}{\lambda + s} \Bigg [ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s)}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \Bigg ] ^ {n} \\ \Pi_ {n o} (s) = \frac {q _ {1} \lambda}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \Bigg [ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s)}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \Bigg ] ^ {n}. \end{array}\tag{4}
$$

Proof: See the Appendix.

Before proceeding further, we define some variables that are required for further analysis. Let the random variable $B _ { { _ t } }$ denote the highest bid by time t and let $f _ { B _ { t } } ( b )$ be the probability density function of $B _ { { } _ { t } }$ . Also define $\Phi _ { B _ { t } } ( s _ { 1 } , s _ { 2 } )$ , the two-dimensional Laplace transform of $f _ { B _ { t } } ( b )$ , as

$$
\Phi_ {B _ {t}} \left(s _ {1}, s _ {2}\right) = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} e ^ {- s _ {1} b - s _ {2} t} f _ {B _ {t}} (b) d b d t.\tag{5}
$$

Theorem 2:

$$
\Phi_ {B _ {t}} \left(s _ {1}, s _ {2}\right) = \frac {\gamma (\lambda + s _ {2} - p _ {2} \lambda + q _ {1} \lambda)}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda) (1 - \gamma)},
$$

where

$$
\gamma = \Phi_ {X} (s _ {1}) \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right].\tag{6}
$$

Proof: See the Appendix.

The two-dimensional Laplace transform $\Phi _ { B _ { t } } ( s _ { 1 } , s _ { 2 } )$ of the probability density function of the highest bid at time t obtained in Theorem 2 can now be inverted to get the transient probability density of the highest bid at time t in time-domain.

Now, let us define $\Phi _ { B t } ( B )$ as the probability that the bid by time t is less than or equal to b—that is, $\begin{array} { r } { \Phi _ { { B } _ { t } } ( b ) = \int _ { 0 } ^ { b } f _ { B _ { t } } ( x ) d x } \end{array}$ . If $\Phi _ { B _ { t } } ^ { \prime } ( s _ { 1 } )$ denotes the Laplace transform of $\Phi _ { B _ { t } } ( b )$ , then, by the properties of Laplace transforms, we get

$$
\Phi_ {B _ {t}} ^ {\prime} (s _ {1}) = \frac {\Phi_ {B _ {t}} (s _ {1} , s _ {2})}{s _ {1}}.\tag{7}
$$

Inverting Equation (7) will give us the probability distribution of the bid value at time t.

The above results hold for any distribution of increments in bid values $X _ { i ^ { \ast } }$ . However, for the purposes of illustration, we now proceed to analyze the specific functional forms when $X _ { _ i }$ is uniformly distributed.

Transient Probability Distribution of Bids When Bid Increments Are Uniformly Distributed

When the bid increments are uniformly distributed, $X _ { i } \sim U [ \alpha , \beta ]$ , we get

$$
\Phi_ {X} (x) = E \left[ \exp (- s X _ {i}) \right] = \int_ {\alpha} ^ {\beta} e ^ {- s x} \left(\frac {1}{\beta - \alpha}\right) d x = \frac {e ^ {- s \alpha} - e ^ {- s \beta}}{s (\beta - \alpha)}.\tag{8}
$$

Substituting (8) in (6), we get

$$
\Phi_ {B _ {t}} \left(s _ {1}, s _ {2}\right) = \frac {\gamma (\lambda + s - p _ {2} \lambda + q _ {1} \lambda)}{(\lambda + s) (\lambda + s - p _ {2} \lambda) (1 - \gamma)},\tag{9}
$$

where

$$
\gamma = \frac {e ^ {- s _ {1} \alpha} - e ^ {- s _ {1} \beta}}{s _ {1} (\beta - \alpha)} \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right].\tag{10}
$$

The Laplace transform given by Equation (9) cannot be inverted analytically. Hence, we invert it using algorithms that numerically invert two-dimensional Laplace transforms [43]. Figures 2 and 3 provide the transient-probability density for various values of highest bid and l when $p _ { _ { 1 } } { = } p _ { _ { 2 } } { = } 0 . 8$ , and $X _ { _ i } \sim U [ 1 , 5 ]$ . As is to be expected, the time taken to reach the maximum value of the probability density function increases as the bid value increases (Figure 2); and for a given bid value, as the arrival rate $\lambda$ increases, the probability density function reaches its peak earlier (Figure 3). Note that $f _ { B _ { t } } ( b )$ is the joint probability density function of the bid value b and the time t. Hence, for a given value of $^ { b , }$ the area under the curves shown in Figures 2 and 3 is the marginal density function of the bid value.

Charts such as these could be precomputed for different arrival rates and bidincrement distribution parameters to estimate the probabilities of reaching a particular bid value after a given interval of time.<sup>9</sup> To do that, experienced practitioners can arrive at educated estimates for the arrival rates of interested observations for different products—and these estimates can change depending on the time of the year, expected demand or availability of the product, the seller reputation, and so forth. Such practitioners can also make estimates on the two probabilities $p _ { 1 }$ and $p _ { 2 }$ that are required for the model, while the interval of bid increments can be gauged from historical data. These estimates can be revised and fine-tuned at regular intervals with updated auction data. As we mention in the introduction, having such precomputed charts as guidelines should be highly beneficial to a vast number of small-business owners who conduct their business primarily on eBay in streamlining their cash flows.

Finally, sellers would be interested in knowing the expected time to reach a particular bid price. The probability distributions we obtained in Figures 2 and 3 may or may not yield a ready-made functional form, but they could nonetheless be computed easily from the computed data. For example, with the same values of the parameters as described above, the expected time to reach the bid value of 10 is computed to be 7.5894 time units, while a bid value of 20 is expected after 12.0833 time units.

![](/api/attachments/BCFQPMPU/fulltext/images/4c1b1d6ea4e09fabeffcb9b89e376db8f1a01aceec5d603f725686ab52db8d70.jpg)  
Figure 2. Transient Probability Density of the Highest Bid by Time t (in days) Note: The increments in bids are uniformly distributed in (1, 5) and $p _ { 1 } = p _ { 2 } = 0 . 8 .$

![](/api/attachments/BCFQPMPU/fulltext/images/64633188ff4bd72d70203c71c657f676773d515d3a5cb2f8658abf7fef3aa505.jpg)  
Figure 3. Transient Probability Density, the Highest Bid Being Equal to 40 by Time t (in days) for Different Values of l  
Note: The increments in bids are uniformly distributed in (1, 5) and $p _ { _ { 1 } } = p _ { _ { 2 } } = 0 . 8$

## Application in Real-Life Scenarios

We applied the res ults of our analys is to sample data from live auctions on eBay. It should be emphasized that the estimates of the parameters—for reasons outlined later—are probably approximate, and serve best as showing how the analysis can be possibly useful. The best way to estimate the parameters would be to measure them from the records of the Web server software (which, in our case, would be eBay’s server records), but we were unable to obtain access to such records.

Our method for estimating the parameters from live auction was as follows: for each of the auctions we followed, we monitored the auction page using Screen Scraper software (basic edition), from ekiwi LLC, which allowed us to poll the Web page at a regular interval and gather the data we needed at those points in time. Because Web pages on eBay do not update by themselves,<sup>10</sup> we had to program the Screen Scraper software to refresh the screen every time it had to gather the required data. This data included the number of page views at that point in time (this is something that is not produced by eBay but sellers can augment their auction page by including the page view information using code provided by many independent third parties), as well as the current highest bid. The type of merchandise that we were tracking tended to have page views in the range of 10–20 per day: in other words, just the very act of polling the Web site for gathering the requisite information would constitute (perhaps overwhelmingly) the bulk of activity on that auction page. We are therefore somewhat hesitant to place complete faith in the data that we gathered, for it is possible that the system would have acted differently had it not been polled regularly by the screenscraping software. The best way to gather the data would have been from eBay’s server records, which unfortunately were not available to us.

With this caveat in place, we decided to poll the auction pages once every five minutes for the necessary information. We started to poll the auction page about half an hour after the auction had started, and continued the monitoring for over the next two to four days (depending on the length of the auction), and we always stopped monitoring some time before the auction was scheduled to end. This was to ensure that the data recorded was from the “steady-state” part of the auction. From the auctions’ expected number of page views, it is apparent that our monitoring resulted in the overwhelming majority of the observations of the page views. Because an auction page on eBay does not refresh automatically, an “interested observation” can take place only when a new page view is registered—either through a new visit by a bidder or by a page refresh (by either a potential bidder or through our software). If the data recorded only one incremental page view between our polling, it meant that there were no new interested observations within the interval (the one page view was a result of the software’s polling). If the data recorded two (or rarely, more) incremental page views, it meant that there was an interested observation within the polling interval. By recording the bid price at that point in time, we then get to know (1) if the interested observation resulted in an increase in the bid and (2) how much was the increment in the bid. Since we maintain the history of all the interested observations, we were able to observe whether a bid price increase from one interested observation resulted in a bid price increase in the next interested observation (the cumulative statistics would thereby give us an estimate of the parameter $p _ { 1 } ) ;$ and in a similar vein, if an interested observation that did not result in an increased bid would result in the next interested observation also not making an increased bid (the cumulative statistics would thereby give us an estimate of the parameter $p _ { 2 } )$ . If more than two incremental page views occurred within the interval (a rare occurrence), it meant that there was more than one interested observation in that interval, and we recorded it as one observation (otherwise we would run into the issue of trying to guess the state of the system—we do note that this was a rare occurrence). The algorithm for estimating the parameter values is laid out in Figure 4.

The final estimate that had to be made was with regard to the distribution of the bid increments. We felt that due to the paucity of data, we could not make sufficient judgment regarding the distribution of the bid increment, and for purposes of illustration, we assumed that the distribution was uniform (the expressions would be more complicated for other distributions, but can nonetheless be handled by the numerical Laplace transform algorithms).

Electronic merchandise is a common type of item sold on eBay. Price cutting in electronic items among online retailers is usually quite severe, leading us to believe that sellers on eBay cannot expect to hold out for a long time on such items with the hope of extracting the maximum possible rent, and would therefore be possible beneficiaries of our results. We observed several such live auctions as they evolved; Table 1 summarizes our findings by comparing the actual time the auction was open to the time computed from our results. eBay now allows sellers to sell in various ways—bidding with no minimum, bidding with minimum reserve price, “buy it now” with bidding, “buy it now” or “best offer,” and so on—and so we chose only those auctions for new electronic items that had bidding with a minimum reserve price and also had a “buy it now” option.<sup>11</sup> This “buy it now” price was chosen as the proxy for the price that the seller would be content to reach as soon as possible instead of waiting the entire length of the auction (this seemed reasonable, as eBay’s marketing guide states that the advantage of “buy it now” is to “sell your item for the price you want”).<sup>12</sup> As an interesting aside, we mention the findings of Standifird et al. [41], who found that eBay buyers did not use the “buy it now” option even when “buy it now” prices were set below prevailing market prices: the authors think that the entertainment benefit associated with eBay auctions may explain this somewhat counterintuitive finding. If this finding is generally true, it would validate our choice of the “buy it now” price as the target, since the bidders’ behavior would not be influenced by it.

We illustrate the process with two of these auctions in greater detail, and then comment on some of the other auctions of interest. Since the model requires estimation of three parameters—the arrival rate (l) and the “momentum” probabilities $( \boldsymbol { p } _ { 1 }$ and $p _ { 2 } )$ —and different sellers might have different estimates of them, we simulated moderate perturbations to our estimates to find their effect on the final expected time. The simulation results confirmed that the final numerical values change only slightly, which indicates that different estimates of the parameters, as long as they are close to each other, will not materially affect the final result. In any case, the numerical examples provide a nice illustration of the capabilities of the model, and in many examples, back up the empirical observations to show its utility.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input:
PV: Sequence of values indicating the number of page views reported by the scraping software
BV: Sequence of corresponding bid values reported by the scraping software
N: number of values in the sequence PV
Duration: the time duration for which the scraping software was run

Output:
Estimate of  $\lambda$ ,  $p_{1}$ ,  $p_{2}$ ,  $\beta$ 

Procedure Estimate Parameters (PV, BV, N, Duration)
{
    Lambda = (PV(n) - PV(1))/Duration;
    //Sequence Action will record a value (1 or 0) per interested observation to indicate
    //if the bid value was increased or not in that observation
    //Initialize Beta, j, Action(j) to 0, 1, and 0 resp.
    Beta = 0; j = 1; Action(j) = 0;
    For i = 2 to N
    {
    If((PV(i) - PV(i-1)) &gt;= 1)
    {
    j = j + 1;
    BidIncrement = BV(i) - BV(i-1);
    If (BidIncrement &gt; 0)
    {
    Action(j) = 1;
    If (BidIncrement &gt; Beta)
    {
    Beta = BidIncrement;
    }
    Else
    {
    Action(j) = 0;
    } //EndIf
    } //EndIf
    } //EndFor

    //Initialize TotP1, TotP2, NumP1, NumP2 to 0
    TotP1 = 0; TotP2 = 0; NumP1 = 0; NumP2 = 0;
    For i = 1 to (j-1)
    {
    If(Action(i) = 1)
    {
    TotP1 = TotP1 + 1;
    }
    Else
    {
    TotP2 = TotP2 + 1;
    }
    If(Action(i) = Action(i+1))
    {
    If (Action(i) = 1)
    {
    numP1 = numP1 + 1;
    }
    Else
    {
    numP2 = numP2 + 1;
    } //endif
    } //endif
    } //endFor
    p1 = numP1/totP1;
    p2 = numP2/totP2;
} //End
</div>

Figure 4. Algorithm for Estimating l, $p _ { 1 } , p _ { 2 } , \beta$

<table><tr><td colspan="8">Table 1. Sample Computations for Estimated Times to Reach a Certain Price for Various Auctions on eBay Compared to the Actual Auction Open Time</td></tr><tr><td>Product</td><td>α (dollars)</td><td>β (dollars)</td><td>λ (day)</td><td>“BIN” price (dollars)</td><td>Auction open time (days)</td><td>Initial price (dollars)</td><td>Computed expected time*</td></tr><tr><td>Sony PS2</td><td>2.50</td><td>10.00</td><td>9</td><td>125.00</td><td>5</td><td>15.00</td><td>4 days, 1 hour</td></tr><tr><td>Canon Powershot SD300</td><td>1.00</td><td>15.00</td><td>9</td><td>205.00</td><td>5</td><td>45.00</td><td>4 days, 14 hours</td></tr><tr><td>Casio Exilim EX-750</td><td>1.00</td><td>15.00</td><td>11</td><td>250.00</td><td>7</td><td>70.00</td><td>4 days 9 hours</td></tr><tr><td>Toshiba M55-S331 laptop</td><td>5.00</td><td>50.00</td><td>8</td><td>850.00</td><td>5</td><td>350.00</td><td>4 days, 17 hours</td></tr><tr><td>HP dv1000 laptop</td><td>5.00</td><td>50.00</td><td>10</td><td>730.00</td><td>7</td><td>200.00</td><td>3 days, 20 hours</td></tr><tr><td>HP dv5000 laptop</td><td>5.00</td><td>50.00</td><td>9</td><td>900.00</td><td>7</td><td>350.00</td><td>4 days, 13 hours</td></tr><tr><td>Sony PS2</td><td>2.50</td><td>10.00</td><td>12</td><td>130.00</td><td>7</td><td>10.00</td><td>3 days, 12 hours</td></tr><tr><td>Lenovo Thinkpad X41 laptop</td><td>5.00</td><td>50.00</td><td>5</td><td>1,559.00</td><td>7</td><td>600.00</td><td>14 days, 5 hours</td></tr><tr><td>Microsoft Xbox 360 Premium bundle</td><td>10.00</td><td>50.00</td><td>10</td><td>500.00</td><td>4</td><td>300.00</td><td>1 day, 11 hours</td></tr><tr><td>Palm Lifedrive</td><td>5.00</td><td>20.00</td><td>8</td><td>315.00</td><td>3</td><td>175.00</td><td>2 days, 23 hours</td></tr><tr><td>HP iPAQ RX3715 Pocket PC</td><td>5.00</td><td>20.00</td><td>10</td><td>330.00</td><td>4</td><td>150.00</td><td>3 days</td></tr><tr><td>Toshiba Protégé R200-S234 laptop</td><td>10.00</td><td>50.00</td><td>6</td><td>1,195.00</td><td>5</td><td>750.00</td><td>5 days, 3 hours</td></tr><tr><td colspan="8">* The times are rounded to the nearest hour.</td></tr></table>

The first product was a popular model of a laptop, the HP  avilion dv1000 notebook from Hewlett-Packard. The retail price of the laptop comparably equipped on Hewlett-Packard’s online store was approximately \$820.00 (excluding taxes, but with free shipping). For this particular auction, the seller had decided to keep the auction open for seven days, and had kept the “buy it now” price at \$730.00, excluding shipping cost, which was \$35.00. On eBay, a prospective buyer can readily observe the history of bids and when they were placed. From this data, we estimated l to be around 10 per day. The lowest price increment for the auction was \$5.00 (i.e., a = 5), and we estimated the highest bid increment, b, to be \$50.00. The starting price for the laptop was \$200.00.

Another auction that we observed was for the popular electronic game console the Sony P laystation P S2. Here, the initial price was \$10.00, and the “buy it now” price was set at \$130.00. The auction interval was once again set to one week. By observing the various bids, we estimated $\lambda { = } 1 2 / \mathrm { d a y }$ , and the lowest price increment was observed to be \$2.50. We estimated that the highest bid increment was \$10.00.

The parameters above were entered into the analytical results of the prior section. Figures 5 and 6 show the probability distributions of the bid reaching a certain value (which for a seller would be the “buy it now” price) for the above-mentioned auctions in a certain amount of time—for the laptop, the required bid price was set to \$730.00, and for the PS2, that price was set at \$130.00. If we numerically invert $\Phi _ { B _ { t } } ^ { \prime } ( s _ { 1 } )$ given by Equation (7), and subtract that value from 1, we get the cumulative probability distribution of the price being greater than or equal to the “buy it now” price after a certain interval of time. These are shown in Figures 7 and 8 for auctions of the abovementioned laptop and PS2, respectively. We also calculated the expected time required to reach the “buy it now” prices—for the laptop, the “buy it now” price could be expected to be reached in about 3 days and 20 hours, whereas for the PS2, the expected time was calculated to be around 3 days and 12 hours. Thus, in each case, both sellers were keeping the auction open unnecessarily for a significantly larger amount of time than was necessary, the cumulative effect of which across all of a seller’s auctions could have a significant detrimental effect on the seller’s cash flows.

As the computed expected times for the other auctions show, the sellers often significantly overestimate (and sometimes underestimate) the time to keep the auctions open for many of the auctions. Specifically, some of the auction activities proved to be very interesting. Consider, for example, the auction for the Lenovo Thinkpad X41 laptop that was kept open for one week with a “buy it now” price of \$1,559.00. The expected time as per our analysis for the auction to reach the “buy it now” price was a little over two weeks. The auction actually ended without the seller managing to find a buyer. In fact, the highest bid for the laptop was \$1,090.00 about half an hour before the time ran out on the auction. This compares favorably with the expected price (as per our analytical results) of \$1,115.97 at the end of seven days. The seller thus overestimated the interest for the laptop by a wide margin. Similarly, the Toshiba Protégé R200-S234 laptop auction also ended without a buyer (the auction remained open for five days, and the calculated expected time was five days and three hours). At the other end of the spectrum was the Microsoft Xbox Premium bundle that reached the “buy it now” price in about one day and seven hours, four hours less than the expected time as per the analytical results. We think that the results have to do with the type of product being auctioned. The Lenovo Thinkpad X41 is an “ultraportable” tablet notebook, a very niche product with limited demand. Combined with a high “buy it now” price, the product remained unsold in the limited time the auction was kept open. Similarly, the Toshiba Protégé R200 is also an ultraportable laptop with a limited market. Conversely, the Microsoft Xbox Premium bundle (which included the game console with a “special” collection of games) was in high demand, and the “buy it now” price could arguably be considered to be a relative bargain.

![](/api/attachments/BCFQPMPU/fulltext/images/214937c8aaeb562d80488896981e19bde8508750b507e3cc08b7a94cd6546f17.jpg)  
Figure 5. Probability That Bid Price Will Reach \$730.00 at Time t (in days) with the Auction Starting at \$200.00 (a = 5, b = 50, l = 10/day)

![](/api/attachments/BCFQPMPU/fulltext/images/f04c2e0a46110eba1ee6608a9e44351049501d8ad14046802f29f38579ff8d8b.jpg)  
Figure 6. Probability That Bid Price Will Reach \$130.00 at Time t (in days) with the Auction Starting at \$10.00 (a = 2.5, b = 10, l = 12/day)

![](/api/attachments/BCFQPMPU/fulltext/images/36f494c84be13c0bc1496c786c1aad2c45139f8c7e83c39901a139dd248acde8.jpg)  
Figure 7. Probability That Bid Price Exceeds \$730.00 at Time t (in days) with the Auction Starting at \$200.00 (a = 5, b = 50, l = 10/day)

![](/api/attachments/BCFQPMPU/fulltext/images/f3b2b88a44debdbd54c4583153e8bb801e785abe0078f8ad71a6dbc37d941970.jpg)  
Figure 8. Probability That Bid Price Exceeds \$130.00 at Time t (in days) with the Auction Starting at \$10.00 (a = 2.5, b = 10, l = 12/day)

Finally, another interesting auction was for the HP iPAQ RX3715 Pocket P C, with a “buy it now” price of \$330. The auction ended in about three days and two hours, comparing favorably with the computed expected time of three days.

Because it was difficult to get a vast amount of live data from eBay’s Web site, we decided to further validate our model through the use of simulation.<sup>13</sup> To ensure that we can do meaningful comparisons if necessary with the actual empirical observations, we decided to simulate the behavior of the QB D process using “products” that had the same characteristics as the ones we observed. We chose seven different “products,” such that they represented different price levels as well as different time periods for which their auctions remained open. These virtual products, which corresponded exactly with their real-life counterparts, are listed in Table 2; that is, for each of these “products,” we assumed the same initial bid prices, momentum probabilities, minimum and maximum bid increments (with the values distributed uniformly within the interval), and the Poisson arrival rate of interested observations, which in turn gave us the same theoretically computed expected times of reaching their respective “buy it now” prices. We then computed the actual time required to reach each of these “buy it now” prices by simulating these QB D processes in 1,000 different observations for each one of these seven different “products”—for a total of 7,000 observations.

The simulation procedure is as follows:

1. Record initial starting price. Record the time when the auction starts.

2. Simulate interested observations as a Poisson process with an arrival rate λ .

3. With each new interested observation, simulate the bid price to either stay the same or go up, with probabilities as determined by the momentum probabilities $p _ { 1 } , q _ { 1 } , p _ { 2 } ,$ and $q _ { 2 }$ .

4. T he bid price increment is determined by simulating a uniform random variable with its support defined by the minimum and maximum bid increment (i.e., α and β ).

5. Record the simulated time taken for the bid price to reach or cross the “BIN” price.

The process is repeated 1,000 times for each of the seven “products.” The results of the simulations are provided in Table 2.

The final two columns show the mean of the simulated times taken to reach the “BIN” price and the standard deviation of these observations for respective virtual “products.” As the results indicate, the different averages of the times taken to reach the “BIN” price show remarkable consistency with the theoretically computed expected times (the maximum deviation happens for just two “products” and that too by just one hour in each case—the times being rounded to the nearest hour). This is perhaps to be expected, given that we average over 1,000 simulation runs in each case, so that the mean of the random variable from a sample of the 1,000 observations (in each of the simulated auctions) tended toward the theoretical mean. Significantly, the standard deviations of the time taken to reach the “BIN” price in the various observations are very small, from a minimum of 0.2857 percent of the mean (with the simulated Microsoft Xbox 360 Premium bundle) to a maximum of 0.3881 percent of the mean (HP iPAQ RX3715 Pocket P C).

<sub>Theoretical</sub> <sub>Expected</sub> <sub>Times</sub> <sub>with</sub> <sub>Actu</sub>a<sup>l</sup> <sup>Simulated</sup> <sup>Times</sup> <sup>for</sup> <sup>Different</sup> <sup>Virtua</sup>

<table><tr><td>Product</td><td>α (dollars)</td><td>β (dollars)</td><td>λ (day)</td><td>“BIN” price (dollars)</td><td>Initial price (dollars)</td><td>Computed expected time*</td><td>Average simulated time (1,000 observations)*</td><td>Standard deviation</td></tr><tr><td>Sony PS2</td><td>2.50</td><td>10.00</td><td>9</td><td>125.00</td><td>15.00</td><td>4 d, 1 h</td><td>4 d, 1 h</td><td>21 m</td></tr><tr><td>Casio Exilim EX-750</td><td>1.00</td><td>15.00</td><td>11</td><td>250.00</td><td>70.00</td><td>4 d, 9 h</td><td>4 d, 9 h</td><td>24 m</td></tr><tr><td>HP iPAQ RX3715 Pocket PC</td><td>5.00</td><td>20.00</td><td>10</td><td>330.00</td><td>150.00</td><td>3 d</td><td>3 d</td><td>17 m</td></tr><tr><td>Microsoft Xbox 360 Premium bundle</td><td>10.00</td><td>50.00</td><td>10</td><td>500.00</td><td>300.00</td><td>1 d, 11 h</td><td>1 d, 11 h</td><td>6 m</td></tr><tr><td>Toshiba M55-S331 laptop</td><td>5.00</td><td>50.00</td><td>8</td><td>850.00</td><td>350.00</td><td>4 d, 17 h</td><td>4 d, 18 h</td><td>24 m</td></tr><tr><td>Toshiba Protégé R200-S234 laptop</td><td>10.00</td><td>50.00</td><td>6</td><td>1,195.00</td><td>750.00</td><td>5 d, 3 h</td><td>5 d, 3 h</td><td>27 m</td></tr><tr><td>Lenovo Thinkpad X41 laptop</td><td>5.00</td><td>50.00</td><td>5</td><td>1,559.00</td><td>600.00</td><td>14 d, 5 h</td><td>14 d, 4 h</td><td>63 m</td></tr><tr><td colspan="9">Notes: d = days, h = hours, m = minutes. * Times are rounded to the nearest hour.</td></tr></table>

Given the significant closeness of the simulations with the theoretical results, we feel that we can conclude that the simulations of the QB D processes back up our theoretical results extremely well.

## Concluding Remarks and Future Extensions

The res ults of our res earch complement the rich lis t of empirical phenomena that have been expounded in recent literature. For example, it is likely that many of the variables that affect the final bid level of online auctions, such as seller reputation, will affect the two parameters $p _ { 1 }$ and $q _ { 2 }$ of our model. One advantage of our model is that it bypasses the need for such hypothesis by estimating these parameters accurately from page visit data. In fact, an online auctioneer such as eBay can progressively fine-tune these estimates for different types of sellers, products, times of year, and so forth, and can provide estimates of ending times to the sellers when they (the sellers) start designing a particular auction. Experienced sellers can combine this estimate with the results of other extant literature on phenomena like the effect of ending time for an auction or sniping on the final bid price. For purposes of illustration, say a seller observes that bidding in the final few minutes is greater during the lunch hours for a particular type of product (e.g., a high-end personal digital assistant), and that an algorithm based on our analysis suggests that the bidding can be ended with a reasonably degree of certainty of reaching the seller’s target price at 9 a.m. The seller can then decide to close the auction at 4 p.m. (to account for all different time zones) to take advantage of the last-minute biddings. Similar observations can be made about the sniping phenomenon—once the seller is comfortable of reaching his or her desired minimum target price through the results of our analysis, it is up to the seller to extend that time by a few hours to extract the surplus due to bidders who want to snipe.

Note that while our estimate might suggest a precise ending time calculated to the last minute, sites such as eBay have discrete ending times. The results of our analysis are still useful in such contexts; if the analysis suggests that an auction end in 4 days and 13 hours (from the HP dv5000 notebook auction example shown in Table 1) and the degree of granularity of the auction ending times on the auctioneer site is a day, the seller can then decide to end the auction in 5 days, which in any event would be a much more informed decision than deciding to end the auction in, say, 10 or 14 days.

Depending on how the model fares with empirical data, it can be extended in some ways. For example, some modifications to the results might be driven by the significant presence of bidders who have been termed “evaluators” by Bapna et al. [6]—bidders who bid early and once in the auction. Such bidders might make our analysis results conservative, since they might drive up the bids higher in the initial moments of the auction than what the “participators” would. Another extension would be in the lines suggested by Shmueli et al. [39], who contend that online auctions might be characterized by three phases—the early moments, the final moments, and the time in between—which differ in their bid arrival intensities. Implementation of this idea in our model will essentially involve estimating three sets of parameters—the arrival rates and the momentum probabilities in each of the phases—but otherwise the analysis should be similar.

To conclude, the emergence of eBay has had a transforming effect on the lives of millions of online sellers who depend exclusively on this Internet platform to sell their products. Unlike traditional auctions, most of these sellers are not looking for extracting the maximum possible rent for a particular product, but are rather content to sell it as soon as a target price is reached. The existing literature has not looked into the phenomenon of how prices evolve in these auctions, which we model in this paper. We take a different approach to some of the existing research in auction literature in that we take advantage of the wealth of data that exists among online auctioneers such as eBay. It allows us to not presuppose motivations by which prices are bid up in online auctions, but simply estimate two observable parameters (albeit currently privately to the auctioneer platform) that are a result of the process. Our analysis takes a bottom-up approach to modeling the process, and takes advantage of the data that are available only now thanks to the online auctions. We present an analytical model of the dynamics of geographically distributed, independent bidders as they observe the auction and bid up prices throughout its life cycle. The results should contribute to the existing literature, and should also be of interest to practitioners who develop online tools for the Internet auctions community.

## Notes

1. As a related point, unlike traditional auctions, many of the products sold in online auctions are readily available with several retailers (and their prices can be easily compiled from price comparison search engines), and therefore the sellers cannot hold out for long periods of time in expectation of high rents.

2. Learn about “buy it now,” available at http://pages.ebay.com/services/buyandsell/buyitnow.html.

3. See also note 1.

4. Specifically, in Bapna et al., participators are defined as those bidders who “progressively monitor the progress of the auction and make ascending bids” [6, p. 92].

5. It is also different from bidder arrivals (which counts each bidder only once).

6. However, as we remark in the concluding section, an experienced seller can use the knowledge of the sniping behavior in conjunction with the results of our analysis to arrive at more “intelligent” ending times.

7. We note that this phenomenon of momentum is not incompatible with the independence of the Poisson arrival process described earlier.

8. The results of the analysis do not depend on these inequalities, however.

9. Another alternative would be to create an application that simulates the distributions in real time.

10. This turned out to be a blessing in disguise. As one anonymous reviewer pointed out, there could be some bidders who keep the Web page open for the entire length of the auction. However, as the Web pages did not refresh automatically, any new interested observation would necessitate a refresh of the Web page, and this would get recorded as a new page view.

11. They also reveal one of the author’s preferences in electronics items.

12. See note 2.

13. We thank an anonymous reviewer for the suggestion.

## References

1. Adams, B. Adams Streetwise Small Business Start-Up: Your Comprehensive Guide to Starting and Managing a Business. Cincinnati, OH: Adams Media, 2002.

2. Angst, C.M.; Agarwal, R.; and Kuruzovich, J. Bid or buy? Individual shopping traits as predictors of strategic exit in on-line auctions. International Journal of Electronic Commerce, 13, 1 (2008), 59–84.

3. Ariely, D., and Simonson, I. Buying, bidding, playing or competing? Value assessment and decision dynamics in online auctions. Journal of Consumer Psychology, 13, 1 (2003), 113–123.

4. Bajari, P., and Hortacsu, A. The winner’s curse, reserve prices, and endogenous entry: Empirical insights from eBay auctions. RAND Journal of Economics, 34, 2 (2003), 329–355.

5. Bajari, P., and Hortacsu, A. Economic insights from Internet auctions. Journal of Economic Literature, 42 (June 2004), 457–486.

6. Bapna, R.; Goes, P.; and Gupta, A. Analysis and design of business-to-consumer online auctions. Management Science, 49, 1 (2003), 85–101.

7. Bapna, R.; Goes, P.; and Gupta, A. Replicating online Yankee auctions to analyze auctioneers’ and bidders’ strategies. Information Systems Research, 14, 3 (2003), 244–268.

8. Bapna, R.; Jank, W.; and Shmueli, G. Consumer surplus in online auctions. Information Systems Research, 19, 4 (2008), 400–416.

9. Bapna, R.; Goes, P.; Gupta, A.; and Jin, Y. User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quarterly, 28, 1 (2004), 21–43.

10. Bapna, R.; Goes, P.; Gupta, A.; and Karuga, G. Predicting bidders’ willingness to pay in online multiunit ascending auctions: Analytical and empirical insights. INFORMS Journal on Computing, 20, 3 (2008), 345–355.

11. Beuerman, S.L., and Coyle, E.J. State space expansions and the limiting behavior of quasi-birth and death processes. Advances in Applied Probability, 21, 2 (1989), 284–314.

12. Byrne, F. Matters of faith, hope and charity. Financial Times (March 26, 2006), W3.

13. Cinlar, E. Introduction to Stochastic Processes. Englewood Cliffs, NJ: Prentice Hall, 1967.

14. Clemons, E.K. An empirical investigation of third-party seller rating systems in e-commerce: The case of buySAFE. Journal of Management Information Systems, 24, 2 (Fall 2007), 43–71.

15. Dholakia, U.M., and Soltysinski, K. Coveted or overlooked? The psychology of bidding for comparable listings in digital auctions. Marketing Letters, 12, 3 (2001), 225–237.

16. Gneezy, U. Step-level reasoning and bidding in auctions. Management Science, 51, 11 (2005), 1633–1642.

17. Gopal, R.; Thompson, S.; Tung, Y.A.; and Whinston, A.B. Managing risks in multiple online auctions: An options approach. Decision Sciences, 36, 3 (2005), 397–425.

18. Grassman, W. Transient solution in Markovian queues. European Journal of Operations Research, 1 (1977), 396–402.

19. Gregg, D.G., and Scott, J.E. The role of reputation systems in reducing on-line auction fraud. International Journal of Electronic Commerce, 10, 3 (2006), 95–120.

20. Hendricks, K., and Paarsch, H. A survey of recent empirical work concerning auctions. Canadian Journal of Economics, 28, 2 (1995), 403–426.

21. Jank, W., and Shmueli, G. Functional data analysis in electronic commerce research. Statistical Science, 21, 2 (2006), 155–166.

22. Kamins, M.A.; Dreze, X.; and Folkes, V.S. A field study of the effects of minimum and reserve prices on Internet auction. Journal of Consumer Research, 30, 4 (2004), 622–628.

23. Kleinrock, L. Queueing Systems, Volume 1: Theory. New York: John Wiley & Sons, 1975.

24. Laffont, J.-J.; Ossard, H.; and Vuong, Q. Econometrics of first-price auctions. Econometrica, 63, 4 (1995), 953–980.

25. Lewis, N. IBM offers quick-turnaround credit program for VARs. IT Channel News, November 29, 2006 (available at http://searchitchannel.techtarget.com/news/article/0,289142, sid96\_gci1232031,00.html).

26. Liu, D.; Chen, J.‑Q .; and Whinston, A.B. Ex-ante information and design of keyword auctions. Information Systems Research, forthcoming.

27. Lucking-Reiley, D. Using field experiments to test equivalence between auction formats: Magic on the Internet. American Economic Review, 89, 5 (1999), 1063–1080.

28. Lucking-Reiley, D. Auctions on the Internet: What’s being auctioned, and how? Journal of Industrial Economics, 48, 3 (2000), 227–252.

29. MacInnes, I.; Li, Y.; and Yurcik, W. Reputation and dispute in eBay transactions. International Journal of Electronic Commerce, 10, 1 (2005), 27–54.

30. McAfee, P., and McMillan, J. Auctions and bidding. Journal of Economic Literature, 25, 2 (1987), 699–738.

31. McAfee, P., and McMillan, J. Auctions with a stochastic number of bidders. Journal of Economic Theory, 43, 1 (1987), 1–19.

32. Melnik, M.I., and Alm, J. Does a seller’s e-commerce reputation matter? Evidence from eBay auctions. Journal of Industrial Economics, 50, 3 (2002), 337–350.

33. Milgrom, P. The economics of competitive bidding: A selective survey. In L. Hurwicz, D. Svhmeidler, and H. Sonneschein (eds.), Social Goals and Social Organization: Essays in Memory of Elisha Pazner. New York: Cambridge University Press, 1985, pp. 261–292.

34. Moler, C., and Van Loan, C. Nineteen dubious ways to compute the exponential of a matrix. SIAM Review, 20, 4 (1978), 801–836.

35. Neuts, M.F. Matrix-Geometric Solutions in Stochastic Model. Baltimore: Johns Hopkins University Press, 1981.

36. Park, Y.‑H ., and Bradlow, E.T. An integrated model for bidding behavior in Internet auctions: Whether, who, when, and how much. Journal of Marketing Research, 42, 4 (2005), 470–482.

37. Roth, A.E., and Ockenfels, A. Last-minute bidding and the rules for ending second-price auctions: Evidence from eBay and Amazon auctions on the Internet. American Economic Review, 92, 4 (2002), 1093–1103.

38. Schmittlein, D.C.; Morrison, D.G.; and Colombo, R. Counting your customers: Who are they and what will they do next? Management Science, 33, 1 (1987), 1–24.

39. Shmueli, G.; Russo, R.P.; and Jank, W. The BA RISTA : Modeling bid arrivals in online auctions. Annals of Applied Statistics, 1, 2 (2007), 412–441.

40. Stafford, M.R., and Stern, B. Consumer bidding behavior on Internet auction sites. International Journal of Electronic Commerce, 7, 1 (2002), 135–135.

41. Standifird, S.S.; Roelofs, M.R.; and Durham, Y. The impact of eBay’s buy-it-now function on bidder behavior. International Journal of Electronic Commerce, 9, 2 (2004), 167–176.

42. Utz, S.; Matzat, U.; and Snijders, C. On-line reputation systems: The effects of feedback comments and reactions on building and rebuilding trust in on-line auctions. International Journal of Electronic Commerce, 13, 3 (2009), 95–118.

43. Valkó, P.P., and Abate, J. Numerical inversion of 2-D Laplace transforms applied to fractional diffusion equations. Applied Numerical Mathematics, 53, 1 (2005), 53–88.

44. Walker, L. EBay sellers fell into careers that fill their lives. Washington Post (June 30, 2005) (available at www.washingtonpost.com/wp-dyn/content/article/2005/06/29/AR2005062902935. html).

45. Wang, S.; Jank, W.; and Shmueli, G. Explaining and forecasting online auction prices and their dynamics using functional data analysis. Journal of Business and Economic Statistics, 26, 2 (2006), 144–160.

46. Ward, S.G., and Clark, J.M. Bidding behavior in on-line auctions: An examination of the eBay Pokemon card market. International Journal of Electronic Commerce, 6, 4 (2002), 139–139.

47. Wilson, R. Strategic analysis of auctions. In R. Aumann and S. Hart (eds.), Handbook of Game Theory, vol. 1. Amsterdam: North-Holland, 1993, pp. 227–279.

48. Zhang, J., and Coyle, E.J. Transient analysis of quasi-birth-death processes. Communications in Statistics: Stochastic Models, 5, 3 (1989), 459–496.

## Appendix

## Proof of Theorem 1

When $\pi ( 0 ) = [ 0 , 1 , 0 , 0 , 0 , . . . ]$ and Q given by matrix (1) is substituted into Equation (3), the following set of equations results:

$$
\Pi_ {0 o} (s) \bigl (p _ {2} \lambda - \lambda - s \bigr) + \Pi_ {0 +} (s) q _ {1} \lambda = 0\tag{A1}
$$

$$
- \Pi_ {0 +} (s) (\lambda + s) = - 1\tag{A2}
$$

$$
\Pi_ {n} (s) B (s) + \Pi_ {n + 1} (s) C (s) = 0, \quad n \geq 0,\tag{A3}
$$

where

$$
\Pi_ {n} (s) = \left[ \Pi_ {n o} (s), \Pi_ {n +} (s) \right], B (s) = \left[ \begin{array}{c c} 0 & q _ {2} \lambda \\ 0 & p _ {1} \lambda \end{array} \right]
$$

and

$$
C (s) = \left[ \begin{array}{c c} p _ {2} \lambda - \lambda - s & 0 \\ q _ {1} \lambda & - \lambda - s \end{array} \right].
$$

From Equation (6), we get the recursive relation:

$$
\Pi_ {n + 1} (s) = \Pi_ {n} (s) W (s),\tag{A4}
$$

where

$$
W (s) = - B (s) \big [ C (s) \big ] ^ {- 1} = \left[ \begin{array}{c c} \frac {q _ {1} q _ {2} \lambda^ {2}}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} & \frac {q _ {2} \lambda}{\lambda + s} \\ \frac {p _ {1} q _ {1} \lambda^ {2}}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} & \frac {p _ {1} \lambda}{\lambda + s} \end{array} \right].
$$

Solving Equations (A1), (A2), and (A4), it may be verified that

$$
\Pi_ {n +} (s) = \frac {1}{\lambda + s} \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s)}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \right] ^ {n}, \quad n \geq 0\tag{A5}
$$

$$
\Pi_ {n o} (s) = \frac {q _ {1} \lambda}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s)}{(\lambda + s) (\lambda + s - p _ {2} \lambda)} \right] ^ {n}, \quad n \geq 0.\tag{A6}
$$

Q.E.D.

## Proof of Theorem 2

Recall that the difference between the ith and the (i – 1)th bid is denoted by the i.i.d. random variables $X _ { _ i }$ with the pdf $f _ { X } ( x )$ . Let us now define $\Phi _ { x } ( x ) = E [ \exp ( - s X _ { i } ) ]$ . If the QB D process is in states $n _ { + }$ or $n _ { o } ,$ , then the highest bid is a random variable

$$
S _ {n} = \sum_ {i = 1} ^ {n} X _ {i}.
$$

As the variables $X _ { i } , i > 0$ are i.i.d., we get

$$
\Phi_ {S _ {n}} (s) = E \left[ \exp (- s S _ {n}) \right] = \left[ \Phi_ {X} (s) \right] ^ {n}.\tag{A7}
$$

At any time $t ,$ the QB D process can be in any of the states $n _ { + }$ or $n _ { _ { o } } , n > 0$ . Note that the increment in the bid is independent of the state of the process. Hence, the probability density function of the highest bid at time $t , f _ { B _ { t } } ( b ) , b > 0$ , is given by

$$
\begin{array}{c} f _ {B _ {t}} (b) = \sum_ {n = 1} ^ {\infty} f _ {B _ {t}} \big (b | p r o c e s s i s i n s t a t e n _ {+} \text {or} n _ {o} \big) \big (\pi_ {n +} (t) + \pi_ {n o} (t) \big) \\ = \sum_ {n = 1} ^ {\infty} f _ {S _ {n}} (b) \big (\pi_ {n +} (t) + \pi_ {n o} (t) \big). \end{array}\tag{A8}
$$

Note that the limits on the summation in Equation (A8) are from $n = 1$ and not from $n = 0$ because we are assuming that b is greater than the minimum bid level at which the auction started, and hence the probability that the bid level of b can be reached in either state $0 _ { \ i }$ or $0 _ { + }$ is zero.

Taking the Laplace transform on both sides of Equation (A8), we get

$$
\begin{array}{c} \Phi_ {B _ {t}} (s _ {1}, s _ {2}) = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} \mathrm{e} ^ {- s _ {1} b - s _ {2} t} f _ {B _ {t}} (b) d b d t \\ = \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} e ^ {- s _ {1} b - s _ {2} t} \left(\sum_ {n = 1} ^ {\infty} f _ {S _ {n}} (b) (\pi_ {n +} (t) + \pi_ {n o} (t))\right) d b d t \\ = \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {\infty} \int_ {0} ^ {\infty} e ^ {- s _ {1} b - s _ {2} t} f _ {S _ {n}} (b) (\pi_ {n +} (t) + \pi_ {n o} (t)) d b d t \\ = \sum_ {n = 1} ^ {\infty} \int_ {0} ^ {\infty} e ^ {- s _ {1} b} f _ {S _ {n}} (b) d S _ {n} \int_ {0} ^ {\infty} \mathrm{e} ^ {- s _ {2} t} (\pi_ {n +} (t) + \pi_ {n o} (t)) d t \end{array}\tag{A9}
$$

(A10)

$$
\begin{array}{c} = \sum_ {n = 1} ^ {\infty} \Phi_ {S _ {n}} (s _ {1}) (\Pi_ {n +} (s _ {2}) + \Pi_ {n o} (s _ {2})) \\ = \sum_ {n = 1} ^ {\infty} [ \Phi_ {X} (s _ {1}) ] ^ {n} (\Pi_ {n +} (s _ {2}) + \Pi_ {n o} (s _ {2})) \\ = \sum_ {n = 1} ^ {\infty} [ \Phi_ {X} (s _ {1}) ] ^ {n} \left[ \frac {\lambda + s _ {2} - p _ {2} \lambda + q _ {1} \lambda}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right] \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right] ^ {n} \\ = \gamma \left[ \frac {\lambda + s _ {2} - p _ {2} \lambda + q _ {1} \lambda}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right] \sum_ {n = 0} ^ {\infty} [ \Phi_ {X} (s _ {1}) ] ^ {n} \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right] ^ {n}. \end{array}\tag{A11}
$$

The random variables $X _ { i } ( \mathrm { i . e . }$ , the increments in the bids) are strictly positive and have a bounded support. Thus, the integral and summation signs can be switched while going from Equations (A9) and (A10), as a consequence of the Lebesgue dominated convergence theorem.

It can be proved that the absolute values of both the arguments inside the summations in Equation (A11) are less than one, and therefore we can get a closed-form solution for (A11); the details of the proof are provided next.

Using the results (A12) and (A13) below in Equation (A11), we get

$$
\Phi_ {B _ {t}} \left(s _ {1}, s _ {2}\right) = \frac {\gamma (\lambda + s _ {2} - p _ {2} \lambda + q _ {1} \lambda)}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda) (1 - \gamma)},
$$

where

$$
\gamma = \Phi_ {X} (s _ {1}) \left[ \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right].
$$

Proof that the absolute values of both the arguments inside the summations in Equation (A11) are less than one:

As the increments in bids $X _ { i }$ can only be positive,

$$
\begin{array}{c} \left| \Phi_ {X} (s _ {1}) \right| = \left| \int_ {0} ^ {\infty} e ^ {- s _ {1} x} f _ {X} (x) d x \right| = \int_ {0} ^ {\infty} \left| e ^ {- s _ {1} x} f _ {X} (x) \right| d x \\ = \int_ {0} ^ {\infty} \left| e ^ {- s _ {1} x} \right| \left| f _ {X} (x) \right| d x \leq \int_ {0} ^ {\infty} 1 \cdot f _ {X} (x) d x = 1. \end{array}\tag{A12}
$$

Further, for any complex variable $s _ { 2 } = x + i y$ with $x > 0$

$$
\begin{array}{c} \left| \frac {\lambda (\lambda - p _ {2} \lambda + p _ {1} s _ {2})}{(\lambda + s _ {2}) (\lambda + s _ {2} - p _ {2} \lambda)} \right| = \frac {| \lambda | | \lambda - p _ {2} \lambda + p _ {1} s _ {2} |}{| \lambda + s _ {2} | | \lambda - p _ {2} \lambda + s _ {2} |} \\ = \frac {\lambda \sqrt {(\lambda - p _ {2} \lambda + p _ {1} x) ^ {2} + (p _ {1} y) ^ {2}}}{\sqrt {(\lambda + x) ^ {2} + y ^ {2}} \sqrt {(\lambda - p _ {2} \lambda + x) ^ {2} + y ^ {2}}} \\ = \sqrt {\frac {\lambda^ {2}}{(\lambda + x) ^ {2} + y ^ {2}}} \sqrt {\frac {(\lambda - p _ {2} \lambda + p _ {1} x) ^ {2} + (p _ {1} y) ^ {2}}{(\lambda - p _ {2} \lambda + x) ^ {2} + y ^ {2}}} <   1. \end{array}\tag{A13}
$$

Q.E.D.
