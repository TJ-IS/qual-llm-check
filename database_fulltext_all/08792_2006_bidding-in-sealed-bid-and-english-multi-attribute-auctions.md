---
otero_id: 8792
otero_key: "4FAW8XUH"
title: "Bidding in sealed-bid and English multi-attribute auctions"
authors: "Esther David; Rina Azoulay-Schwartz; Sarit Kraus"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Bidding in sealed-bid and English multi-attribute auctions B

Esther David <sup>a,\*</sup>, Rina Azoulay-Schwartz <sup>b</sup>, Sarit Krau s <sup>b,c</sup>

Intelligence, Agents, Multimedia Group, Electronics and Computer Science, University of Southampton, Southampton SO17 1BJ, UK <sup>b</sup> Department of Computer Science, Bar-Ilan University, Ramat-Gan 52900, Israel <sup>c</sup> Institute for Advanced Computer Studies, University of Maryland, College Park, MD 20742, USA

Available online 13 June 2005

## Abstract

In this paper we consider an extension of the traditional auction mechanism, the multi-attribute auction, which enables negotiation on several attributes in addition to the price of the item. In particular, we consider a procurement auction in which the buyer is the auctioneer and the sellers are the bidders. Such domains include auctions on task allocation, services, etc. We focus on three auction protocols for the case of multi-attribute items; a variation of the first-price sealed-bid protocol termed first-score sealed-bid, a variation of the second-price sealed-bid protocol termed second-score sealed-bid, and a variation of the English auction protocol termed sequential full information revelation. We analyze a specific model for these protocols and we provide optimal and stable strategies for the auctioneer agent and for the bidder agents participating in multi-attribute auctions. In addition, we analyze the auctioneer’s/buyer’s expected payoff and suggest an optimal scoring rule to be announced according to the protocol. Finally, we reveal that the buyer’s expected payoff in all three protocols, the first-score-sealed-bid auction, the second-score sealed-bid auction and the English auction, differ only by a predefined constant. We prove that the optimal scoring rule is equal in all three protocols. This result can be interpreted as the extension of the equivalence theory of the single attribute for the case of multi-attribute items.

Keywords: Multi-attribute auctions; Automated agents; Electronic commerce

## 1. Introduction

Auction mechanisms have become very popular within electronic commerce and have been implemented in many domains with assorted environments (e.g., one-to-many, many-to-one, many-to-many, seller-to-buyers and buyer- to-sellers auctions). To date, most of the research on automated auctions considers models where the price is the unique strategic dimension [7,14,23,24,30]. However, in many real world situations, competition and negotiation involve many quality dimensions in addition to the price. Such auctions are termed multi-attribute auctions and a consequence of these additional dimensions, is that the traditional bidding strategies and auction design mechanisms should be reconsidered and adjusted.

A multi-attribute item is defined as an item characterized by several negotiable dimensions. For example, in the supply chain management domain, contracts are typically composed of multiple negotiable attributes, such as the supply time, the number of items delivered, the duration of the product’s warranty and the price. In a task or resource allocation scenario, a task might be defined by its size, starting time, deadline and accuracy level. Finally, in the case of an Internet portal or video-on-demand supplier, storage capacity may be negotiated depending on capacity, the access rates to the data, the availability time and the level of security. Currently, complex contracts such as these are usually finalized using human negotiation or the non-price dimensions are fixed, and the auction relates only to the price. In this paper we suggest an automatic tool based on agent technology to assist the human user confronting complicated tasks on a daily basis.

In contrast to the single-attribute auction, where each side of the auction knows the preferences of the other side regarding the price (the seller prefers a higher price and the buyer a lower one), in reverse multi-attribute auctions, the bidders (sellers) do not necessarily have any information about the auctioneer’s (buyer’s) preferences regarding these additional attributes. To overcome this problem, the auctioneer can either use a scoring function or explicitly guide the auction by revealing if a given bid is better than the best bid yet offered. The scoring function enables the auctioneer to articulate its preferences regarding the various attributes which are made public to all bidders at the beginning of the auction. Sellers use this scoring function to value specific configurations and thus can understand how changes to the various attributes will affect the overall desirability of the bid.

Given a scoring function, one may think that the multi-attribute auction can be mapped into a simple price only auction. However, this is not the case. The scoring function announced by the auctioneer, is not necessarily its real utility function (i.e. the one that reflects the auctioneer’s actual preferences). The announced scoring function, is chosen by the auctioneer, in order to maximize its expected pay-off. Thus, the scoring function may have a different structure from the auctioneer’s utility function or a similar structure but with different weights associated with the various attributes. Moreover, even when given the scoring function, it is still non-trivial for the bidders to identify its optimal bid (as we will show in Section 4.3).

Several interesting questions emerge when attempting to analyze the new concept of the multiattribute auction, for example,

(1) How can the auctioneer choose the auction protocol that maximizes its expected payoff?

(2) What should the buyer (auctioneer) reveal at the start of an auction? Should it include all its preferences, only part of them, or should different modified preferences be revealed?

(3) How should a seller (bidder) formulate its bid considering the various attributes? What should the optimal bid of each seller be, given the protocol, and its beliefs?

(4) Assuming that an English protocol is used, how can a seller (bidder) suggest a better bid than the current best bid, if it does not completely know the buyer’s preferences?

In this paper, we address these issues and propose ways to handle auctions using automated agents. In particular we analyze three auction protocols for the case of multi-attribute items; a variation of the firstprice sealed-bid protocol termed first-score sealedbid, a variation of the second-price sealed-bid protocol termed first-score sealed-bid, and a variation of the English auction protocol termed sequential full information revelation. Another possible protocol is to have a two-stage protocol. In the first stage the bidders offer bids using a sealed protocol, then a set of the best bidders get a second opportunity to compete in an open cry auction. There might be several such protocols which differ in the reservation price/initial bid allowed in the second stage. For example, if this reservation price is set to the price offered by the lowest bidder in the winning bidders set then the strategy in the first stage will be equivalent to the second-price auction. On the other hand, if the bidders are allowed to offer bids in the second stage which are higher than the one they proposed in the first stage then the bidding strategy of the first stage will be strategically equivalent to the first price. In any case by analyzing the three protocols we have suggested we have been able to cover a wide range of protocols.

The auction design goal we consider is to maximize the expected pay-off of the buyer (auctioneer). In the context of economics or market design, it is more common to maximize the overall market efficiency [1,31], however, in the domains that we are interested in, the buyers (auctioneers) are selfish and seek to maximize their profit. Given the auction protocols, we provide the bidder agents with the optimal bidding strategy, and we also provide the auctioneer agent with a mechanism to calculate the optimal scoring function that should be announced, in order to maximize its expected payoff.

Given this background, this work advances the state of the art of the auction in the following ways:

<sup>!</sup> It provides the bidders with the dominant bidding strategy and the auctioneer with the optimal auction design for the three auction protocols; the firstscore sealed-bid, the second-score sealed-bid and the multi-attribute English auctions with an arbitrary number of attributes.

<sup>!</sup> It proves that the buyer’s expected payoff from the multi-attribute English auction and the secondscore sealed-bid auction are equal with the difference of a predefined constant.

<sup>!</sup> It proves that the expected payoff of the auctioneer from the multi-attribute English and first-score sealed-bid auctions are equal with the difference of a predefined constant.

The outline of the paper is as follows. In Section 2 we discuss related work and describe the state of the art in the area of multi-attribute auctions. In Section 3 we describe in detail the model we assume for the auctions. In Section 4 we describe and analyze a sealed-bid auction for multi-attribute items. Using similar methods we analyze a multi-attribute English auction in Section 5. In Section 6 we first analyze the second-score sealed bid auction and then we prove the equivalence between the second score sealed bid and the English auction for the case of multi-attribute items. In addition, we prove that the buyer’s expected payoff in the English auction is equal to the buyer’s expected payoff from the first-score sealed-bid auction with the difference of the predefined constant D that represents the minimal bid increment allowed in the English protocol. Finally, we discuss the optimal value for the minimal increment which should be defined in the multi-attribute English auction. We present our conclusions and discuss future work in Section 7.

## 2. Related work

There are two main maximization goals that are commonly used for auction mechanism designs [9,33]: (1) efficiency in terms of the general welfare of the system (covering both the buyer and the sellers) and (2) the auctioneer’s expected payoff. The former captures the case where there is no other solution that is better for both the auctioneer and the bidders [17]. In terms of efficiency maximization in reverse multiattribute auctions, it has been shown that it is optimal for the auctioneer to announce its true preferences [9,17]. However in the latter case we prove that this is not the case with respect to the multi-attribute English and the sealed-bid auctions. Specifically, we prove that in some cases lying about the utility function may result in a better outcome for the auctioneer. Thus, in order to maximize the auctioneer’s expected payoff, the auction designer has to choose the optimal scoring function (as depicted in Sections 4 and 5).

To date, comparatively little theoretical work has focused on multi-attribute auctions especially in the case of maximizing the auctioneer’s expected payoff. In particular, there are two main pieces of related work and we deal with each of them in turn.

First, Che [8] considered a two-dimensional auctions where a bid is composed of a price and a quality (i.e. ( p, q)). In doing this Che defined three auction protocols; the <sup>b</sup>first-score<sup>Q</sup>, <sup>b</sup>second-score<sup>Q</sup>, and the <sup>b</sup>second-preferred-offer<sup>Q</sup>. The first-score is a simple generalization of the first-price sealed-bid auction, where each bidder submits a sealed bid, and the winner is the bidder who achieves the highest score. The winner is then obliged to produce the goods with the preffered quality at the offered price. The second score is a generalization of the second-price sealed-bid auction where the winner is the bidder who achieves the highest score but is only required to provide goods with a combination of attributes (quality, price) that yields the score of the second highest bid. Another variation of the second-price auction defined by Che is the second preferred-offer in which the winner is required to exactly match the quality-price combination of the second highest bid. Given these auction protocols, Che proposed an optimal design for the auction protocols, based on an announced scoring rule.

In this paper, we extend Che’s model for more realistic electronic commerce applications, where the reverse auction considers multiple non-price attributes. For this case we analyze the first-score, the second-score and the English auctions. We do not consider the second-preferred-offer auction, as we believe that in such procurement (reverse) auction environments, the requirement to match the exact values proposed by another bidder is neither fair nor realistic and thus it is not appropriate for the scenarios that we examine.

One of the interesting issues analyzed by Che is the problem of finding the optimal scoring function, within the auction protocols that he considered. He showed that if the scoring function under-rewards quality compared to the buyer’s utility function, the first-score and second-score auctions implement an optimal mechanism for the auctioneer (i.e. maximizing the auctioneer’s expected payoff). In this paper we extend its result in several ways. First, we consider an arbitrary number of non-price attributes, while Che considers only one such attribute. Second, Che proposes an additive distortion such that the announced scoring function is generated by adding a constant to the real utility function, $S { = } \mathrm { U t i l i t y } { + } r ,$ where r is the value that obtains an optimal outcome for the auctioneer. In contrast, we consider a distortion in the announced weights. That is, given the additive utility function, $\textstyle { \mathrm { U t i l i t y } } : = \sum _ { i } W _ { i } \cdot q _ { i } ,$ where $W _ { i } \mathbf { s }$ are the real weights that the auctioneer associates with each of the corresponding quality value $q _ { i } ,$ , the scoring function we propose will have the form $S { : = } \textstyle \sum _ { i } w _ { i } \cdot q _ { i }$ , where $w _ { i }$ are the optimal calculated weights to be announced in order to maximize the auctioneer’s payoff. We believe that our distortion is more intuitive for the bidders and the auctioneer, because the same structure of the weighted function is kept. The advantages of the additive utility function method in a real electronic commerce domain are clear: functions can be easily estimated and easily reported, and they reflect the real buyer’s preferences in many domains.

Moreover, while Che proved that in cases in which the scoring function equals the buyer’s utility function, first-score and second score protocols yield the same expected payoff for the buyer, we prove that for any given scoring function (even different than the buyer’s utility function) this equivalence holds and also applies to the English protocol in addition to the first-score and second-score protocols.

The second work conducted by Vulkan and Jennings [35] discusses a reverse multi-attribute English auction (within the business process management domain). According to their assumptions, the winning bid relates to the real utility function of the buyer, whereas in our protocol the winning bid relates to the scoring function. Consequently, in Vulkan and Jennings’ work the auctioneer’s optimal strategy is to announce its real utility function. However, as a consequence of our assumptions about the winning bid, the auctioneer is motivated to calculate the scoring function that will yield the best result (as we show in Sections 4.3 and 5.3). In some cases the scoring function may be similar to the real utility function of the auctioneer, but in other cases it may not. Moreover, Vulkan and Jennings refer to the bidding strategy only in a general way; simply to offer a bid that is better than the previous selected bid. In contrast, in our work we precisely indicate the method of choosing the qualities that are optimal for the bidder and that refer specifically to the auctioneer’s preferences. In addition, we prove that only the price should be recalculated in each step (as opposed to Vulkan and Jennings who assumed the bidder calculates the bid from scratch each time), which significantly reduces the computational burden from the bidder’s perspective.

More generally speaking, a number of researches have dealt with multi-attribute auctions, but from the design goal of efficiency maximization. Branco [6] extended Che’s work by assuming that the costs of the bidders are correlated in the sense that their cost model combines elements of private and common values. Specifically, Branco considered a governmental procurement auction in which the main goal is to maximize the general welfare, which takes into account the private rents that will be given to the firms. However in our work, we assume that the costs of bidders are independent as is commonly assumed in auction theory. Parkes and Kalagnanam have also worked in this area and they applied a linear programming based methodology to develop a family of iterative auctions that end with the outcome of a modified

Vickrey–Clarke–Groves (VCG) mechanism for the multi-attribute allocation problem [22]. Since they considered iterative scenarios, because they were concerned with long term relationships, they chose the efficiency maximization goal as their guiding principle. However, they stated that the auctioneer payoff maximization problem is more appropriate for one-shot procurement problems (such as ours).

In addition to the above theoretic work, there has also been some experimental work on multi-attribute auctions. This work shows that multi-attribute auctions can produce higher gains<sup>1</sup> for participants because of the bidding flexibility it offers [5]. Specifically, Bichler [4] found that the utility scores achieved in multi-attribute auctions were significantly higher than those of corresponding single attribute auctions. Similar work was performed by Chen-Ritzo et al. [9] who also experimentally compared the multi-attribute auction with the price-only auction (for multi-attribute items). In order to give the priceonly auction the best chance of success, they calculated the optimal reserve levels of the non-price attributes to be announced. This calculation is based on full information about the bidders’ profit functions in order to provide the most difficult test for the multiattribute auction to compete with. In spite of this handicap, they found that the multi-attribute auction is still more effective in terms of the buyer utility and the bidders’ profits. In an additional work [29] a laboratory experiment was performed to investigate whether a multi-attribute reverse English and a multiattribute reverse Vickrey auction lead to identical outcomes with respect to the buyer’s (auctioneer’s) utility, the suppliers’ profits and allocation efficiency. The benchmarking of this experiment is the theoretical observation that both protocols are equivalent for the single attribute case, which is extended to the multi-attribute case (Section 6.1) in this paper. The results show no significant difference in the suppliers’ profits. However, regarding the buyer’s utility, the English auction leads to both higher allocatable effi ciency and buyer’s utility. These results are explained by the observation that bidders deviated from the dominant bidding strategy. With time they learned and updated their strategies. At that stage the results were more similar in both auctions. This phenomena, of bidders not considering the bidding-strategies derived in game-theory while deciding about their bid has been observed for the single attribute as well [26].

Finally, there are a number of similarities between combinatorial and multi-attribute auctions. In the former case [10,15,16,20,27] a set of available goods is given and each bidder specifies bundles of goods and the prices it is willing to pay for each specified bundle. Given the set of bids, the auctioneer’s problem is then to determine which agents will obtain the bundles they ask for (since the number of available goods is limited). Although the instantiation of the bids can be mapped from the multi-attribute auction to the combinatorial auction (e.g. by considering the various attributes as various goods and the attributes values as the goods’ quantities), the decision problem the auctioneer faces in each case is significantly different. In the combinatorial case, the winner determination is to choose a set of bids that maximizes the prices (or minimizing the price in a reverse auction) while ensuring that the quantities of items meet the supply (or demand in reverse auction). That is, there will be a set of winners. In contrast, in the multiattribute case the auctioneer tries to identify the solitary winner that maximizes its utility.

## 3. The model

The auction model consists of one buyer agent, who is the auctioneer, and a fixed number of n seller agents, who are the bidders. The buyer agent that needs a particular item (service or product) starts the auction process. At the beginning of the auction, the buyer announces its item request (which consists of the item’s desired characteristics), the auction protocol, and a scoring rule describing its preferences concerning the item properties. A seller agent that decides to send a bid has to specify the full configuration it offers. In addition we assume the agents to be rational in a sense that they are trying to maximize their utility and that they will not do an action that yields them a negative utility.

The scoring function associates a score with each proposed offer and the auction protocol dictates that the winner and the winning bid are based on the offers’ scores. The scoring function is used by the auctioneer as a tool for choosing from a set of offers, and is used by the bidders to calculate the optimal bid (as we will show in Section 4.2). Because the scoring function influences the proposed bid, the buyer agent tries to derive a scoring function that maximizes its own expected utility in a given auction protocol. We assume that each participant knows its utility function, and time and bidding are not costly.

In particular, we consider auctions in which the auctioned item is defined by multiple attributes which are utility independent. Namely, the utility of one attribute does not depend on the value of any other attributes [34]. For example, consider the utility of attributes such as the delivery time and the warranty duration, taken from the supply chain management domain. The manufacturer has preferences regarding the delivery time (e.g. <sup>b</sup>the faster the better<sup>Q</sup>) which are independent of the preference for the warranty (e.g. <sup>b</sup>the longer the better<sup>Q</sup>). This assumption is quite common in describing scoring and utility functions in multi-attribute auctions [5]. Another example may be the international Trading Agent Competition (TAC) which is also designed in a way that the multi-criteria decision-making [32] is based on an additive weighting utility function. Given this assumption, we propose to use the additive weighting utility function to combine the different attributes into a decision $\mathrm { r u l e } . ^ { 2 }$ In practice, it is not a trivial task to draw an additive utility function, however there are numerical methods [19] and software available that guide users to construct and design additive utility functions based on their past experience.

Given this background, the seller agents are characterized by an additive utility function that describes their private preferences [36]. Specifically, each seller agent has private information about the costs of improving the quality of the product it sells. Its performance is thus articulated in its cost parameter, $\theta _ { i } .$ . As this parameter increases, the cost to the seller offering an item of a higher quality also increases, i.e., the seller is <sup>b</sup>weaker<sup>Q</sup>. The buyer (auctioneer) only knows the distribution function of the sellers’ cost parameters, and has no information about the particular value of $\theta _ { i }$ of each seller.

Similar to the model described by Che [8], we assume that $\theta _ { i }$ is independently and identically distributed over $[ \underline { { { \theta } } } ; ~ \bar { \theta } ] ~ ( 0 { < } \underline { { { \theta } } } { < } \bar { \theta } { < } \infty )$ according to a distribution function F for which a positive, continuously differentiable density function, $f ,$ exists (in particular, we used the uniform distribution). Because of complete symmetry among agents, the subscript i is omitted in the rest of the paper.

We analyze a case of a multi-attribute auction in which there is an arbitrary number of attributes $( m + 1 )$ , which are predefined and known to all the participants. One of the attributes is the price, $p ,$ and the others are quality attributes for which the preferences of the buyer and the sellers are opposed $( { q } _ { i }$ where $i { \in } [ 1 . . m ] )$ . We assume that as $q _ { i }$ increases, the quality of the item increases. That is, as $q _ { i }$ increases the cost to the seller providing it increases (i.e. it is harder to provide higher quality items). In addition, the buyer’s utility for a higher quality item increases.

For example, a multi-attribute service providing a machine tool, could be characterized by four attributes: the price $p ,$ the speed of the machine $q _ { 1 } ,$ , the accuracy of the machine $q _ { 2 }$ and the warranty period for the machine $q _ { 3 } .$ . As the provided qualities increase, the seller’s cost increases but the buyer’s utility increases.

There are also cases where the quality increases as the quality-attribute values decrease. For example, in the international logistics supply chain domain a service is defined as the transportation of a cargo from one location to another. Some of the attributes that can characterize such a service are the availability time, the path length and the price. As the availability time of the item decreases, and the path length decreases, the service quality increases. In such domains, we can denote $q _ { 1 }$ to be 1 / (AvailabilityTime) and $q _ { 2 }$ to be $1 /$ (PathLength) in order to obtain a positive relation between the quality attributes $q _ { 1 } , \ q _ { 2 }$ and the quality of the item.

Consider the cost functions of the sellers. We assume that there are fixed coefficients for each of the quality dimensions which are identical for all the sellers. Namely, $a _ { 1 }$ is the coefficient of $q _ { 1 }$ , and $a _ { 2 }$ is the coefficient of $q _ { 2 }$ and similarly $a _ { i }$ is the coefficient of quality attribute $q _ { i } .$ . The extension, in the sense of having a vector of cost parameters per bidder that indicates the cost parameter for each quality attribute, is possible as we showed in Ref. [13] for a particular protocol. However, this assumption complicates the calculations and limits us from deriving advanced results. Consequently, in this paper we assume that each bidder is characterized by one cost parameter.

The seller’s cost function is:

$$
C _ {\mathrm{s}} \left(q _ {1}, \dots , q _ {m}, \theta\right) = \theta \left(\sum_ {i = 0} ^ {m} a _ {i} \cdot q _ {i}\right)\tag{1}
$$

where $a _ { i } > 0$

Based on the cost function, the quasi-linear seller’s utility function is:

$$
U _ {\mathrm{s}} (p, q _ {1}, \dots , q _ {m}, \theta) = p - \theta \cdot \left(\sum_ {i = 0} ^ {m} a _ {i} \cdot q _ {i}\right)\tag{2}
$$

Notice that the utility function of the seller is the difference between the price it obtains and the cost of producing the proposed qualities’ values. Consequently, as the payment it obtains increases, the utility also increases.

The influence of $q _ { i }$ is assumed to be independent and linear; as $q _ { i }$ increases by one unit, the cost of the seller will increase by $\theta \cdot a _ { i }$

We assume that the utility function of the buyer agent (the auctioneer) for an item or service is as follows:

$$
U _ {\text { buyer }} (p, q _ {1}, \dots , q _ {m}) = - p + \sum_ {i = 1} ^ {m} W _ {i} \cdot \sqrt {q _ {i}}\tag{3}
$$

where $W _ { i }$ are the weights the buyer associated with $q _ { i } ,$ respectively (i.e. a quasi-linear utility function). In fact as the price decreases, the buyer’s utility increases. It is clear that as $q _ { i }$ increases, the utility of the buyer increases. We assume that $q _ { i }$ where $i { \in } [ 1 . . m ]$ are independent but not linear; as $q _ { i }$ increases, the influence of one additional unit of $q _ { i }$ becomes smaller. This assumption is valid in many domains. For example, enlarging the speed of a processor from 100 to 200 Mhz will have a stronger influence than enlarging the speed from 200 to 300 Mhz. The affect of $q _ { i }$ is weighted by $W _ { i } ,$ respectively, where $W _ { i }$ can be smaller or larger than 1. As $W _ { i }$ increases, the importance of attribute $q _ { i }$ to the buyer increases with respect to the price and other attributes.

Given the buyer’s utility function, the buyer will announce a scoring function, which is used for choosing among bids. The scoring function of the buyer may be different from its real utility function in the sense that the announced weights $w _ { i }$ may be different than the actual weights $W _ { i }$ . In particular, the scoring function is of the form:

$$
S (p, q _ {1}, \dots , q _ {m}) = - p + \sum_ {i = 1} ^ {m} w _ {i} \cdot \sqrt {q _ {i}}\tag{4}
$$

where $w _ { i }$ are the weights that the buyer assigns to $q _ { i } .$ From the scoring function we infer that the announced bid’s value for the buyer is:

$$
V (q _ {1}, \dots , q _ {m}) = \sum_ {i = 1} ^ {m} w _ {i} \cdot \sqrt {q _ {i}}\tag{5}
$$

The announced values of the weights $w _ { i }$ can be equal to or different from the real values of the weights $W _ { i } .$ . For example, if $w _ { 1 } < W _ { 1 }$ , then for some reason the buyer declares a lower utility derived from each unit of $q _ { 1 }$ than its actual utility from $q _ { 1 } .$ . In Sections 4.3 and 5.3 we will show how optimal announced weights can be determined.

## 4. First-score sealed-bid auction

In this section, we study an extension of the firstprice sealed-bid auction, which considers a multiattribute auction. This protocol which was developed by Che [8], is called the first-score sealed-bid auction protocol. This type of protocol for the singleattribute case is widely used in commercial and governmental auctions because of its simplicity. It does not require a long process such as the English protocol, and it does not oblige the auctioneer to reveal the bids it obtained, as in the second price sealed bid auction.

According to the first-price sealed-bid auction protocol for one attribute of one seller and several buyers, the bid with the highest price wins and the buyer is committed to its bid.

We assume that the auctioneer is committed to its scoring function and the winner agent is required to provide an item with the exact values of the bid it offered (e.g., the exact price, quality, delivery date, etc.).We analyze the auction protocol where our main goal is to maximize the auctioneer expected payoff given that the each bidder also bids in a way that maximizes its (of the bidder) utility assuming the model described in Section 3.

## 4.1. Protocol’s description

According to the first-score sealed-bid auction protocol, at the beginning of the auction the buyer (auctioneer) announces the requirement of the desired item including the scoring function. At the next step, each seller (bidder) submits a sealed bid that includes the details of the product it suggests to supply. Finally, the winner agent is the seller (bidder) that receives the highest score for his bid, according to the pre-announced scoring rule. And the winner should provide the bid it offered.

## 4.2. Bidder agents’ strategies

In the single attribute auction protocol, in which the price is the only bidding strategy, the bidder should decide only about the price to bid considering its beliefs about the other competitors. However, in the case of the multi-attribute auction the bidder has to decide about the values of all the quality attributes in addition to the price. One may think that the decision about these values should also be influenced by the bidder’s beliefs about the other competitors. But, as we will see in the following lemma, the values of the qualities’ attributes are determined by the bidder, independent of its beliefs about the other competitors. Thus, the only components that influence this decision are the bidder’s cost parameter and the announced scoring rule. In the following lemma, we specify how each seller will choose the values of $q _ { i } ,$ given its type, and given a particular scoring rule. Che [8] proved a similar lemma for the case of one quality dimension and we show that it holds also for the case of multiple dimensions.

Lemma 1. Given the scoring rule and the seller’s utility function, the optimal quality attributes $q _ { i }$ that maximize the seller’s utility in a multi-attribute auction protocol, are chosen independently of the price and the seller’s beliefs about the other participants, at $q _ { i } ^ { * } ( \theta )$ for all $\theta { \in } [ \underline { { \theta } } , \bar { \bar { \theta } } ]$ , where,

$$
q _ {i} ^ {*} (\theta) = \underset {q _ {1}} {\operatorname{argmax}} \left\{V (q _ {1},..., q _ {m}) - C _ {\mathrm{s}} (q _ {1},..., q _ {m}, \theta) \right\}.\tag{6}
$$

Proof. Suppose on the contrary, that for one seller with a cost parameter h where $\theta \ \leq \bar { \theta } ,$ , the seller’s utility is higher from another bid $( p , q _ { 1 } , . . . , q _ { m } )$ in which $q _ { i } \neq q _ { i } ^ { * }$ for at least one quality dimension. A contradiction is derived by showing that the bid $( p , \ q _ { 1 } , \ldots , \ q _ { m } )$ is dominated by an alternative bid $( p ^ { \prime } , q ^ { \prime } { } _ { 1 } , \ldots , q ^ { \prime } { } _ { m } )$ where $q _ { i } { = } q _ { i } ^ { * }$ , and $p ^ { \prime } = p - V$ $( q _ { 1 } , . . . , q _ { m } ) + V ( q \prime _ { 1 } , . . . , q \prime _ { m } )$

Notice that $S ( p , \ q _ { I } , . . . , q _ { m } ) = S ( p ^ { \prime } , \ q _ { 1 } ^ { \prime } , . . . , \ q _ { m } ^ { \prime } )$ using the scoring rule

$$
S (p, q _ {1}, \dots , q _ {m}) = - p + V (q _ {1}, \dots , q _ {m}).
$$

Now, we will show that

$$
\begin{array}{l} U _ {\mathrm{s}} (p, q _ {1}, \dots , q _ {m}, \theta) \leq U _ {\mathrm{s}} (p ^ {\prime}, q _ {1} ^ {\prime}, \dots , q _ {m} ^ {\prime}, \theta). \\ U _ {\mathrm{s}} (p ^ {\prime}, q _ {1} ^ {\prime}, \dots , q _ {m} ^ {\prime}, \theta) = p ^ {\prime} - C _ {\mathrm{s}} (q _ {1} ^ {\prime}, \dots , q _ {m} ^ {\prime}, \theta) \\ \quad = p - V (q _ {1}, \dots , q _ {m}) + V (q _ {1} ^ {\prime}, \dots , q _ {m} ^ {\prime}) \\ \quad - C _ {\mathrm{s}} (q _ {1} ^ {\prime}, \dots , q _ {m} ^ {\prime}, \theta) \geq p - V (q _ {1}, \dots , q _ {m}) \\ \quad + V (q _ {1}, \dots , q _ {m}) - C _ {\mathrm{s}} (q _ {1}, \dots , q _ {m}, \theta) \\ \quad = p - C _ {\mathrm{s}} (q _ {1}, \dots , q _ {m}, \theta) = U _ {\mathrm{s}} (p, q _ {1}, \dots , q _ {m}, \theta) \end{array}
$$

Lemma 1 describes how each bidder will decide about the quality dimensions of a bid, given the announced scoring rule, and given the bidder’s beliefs about its cost parameter. The proof is similar to that of Che [8], but it considers the additional dimensions of $q _ { i } .$ . Notice that this proof holds for any multi-attribute auction protocol.

From Lemma 1, we can infer that there is no loss of generality in restricting attention to $( q _ { I } ^ { * } ( \theta ) , \dots , q _ { m } ^ { * } ( \theta ) )$ when searching for an equilibrium. The following lemma explicitly finds the values of the price and the qualities dimensions, $b i d \mathbf { = } ( p , q _ { I } ^ { \ast } ( \theta ) , \dots , q _ { m } ^ { \ast } ( \theta ) )$ , in a proposed bid, assuming participation in an auction that follows the first score sealed-bid protocol, given the announced scoring rule and the model described in Section 3. We used the general equation developed by Che for optimal price to be offered by a bidder in the first-score sealed bid auction with one quality dimension and we adjusted it to fit our model of multiple quality dimensions.

Lemma 2. Considering a first-score sealed-bid-auction protocol of one buyer and n sellers with types independently and identically distributed over $[ \underline { { \theta } } , \bar { \theta } ]$ and assuming the model described in Section 3, the dominant strategy for a seller is to bid:

$$
q _ {i} ^ {*} (\theta) = \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2}\tag{7}
$$

where i<sup>a</sup>[1..m] and

$$
\begin{array}{l} p ^ {*} (\theta) = \sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{4 \cdot a _ {i}} \\ \cdot \left(\frac {1}{\theta} + \frac {1}{(\bar {\theta} - \theta) ^ {n - 1}} \cdot \int_ {\theta} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t ^ {2}} \mathrm{d} t\right) \end{array}\tag{8}
$$

Proof. The values of $q _ { 1 } ^ { * } ( \theta )$ can be immediately derived from Lemma 1. The price $p ^ { * }$ is calculated by following Che’s method [8]. Assume $\begin{array} { r } { \frac { \partial C _ { \mathrm { s } } ( q _ { 1 } , \ldots , \check { q _ { m } } , \theta ) } { \partial ( \theta ) } = C _ { \mathrm { s } } ^ { \prime } ( \check { \theta } ) } \end{array}$ , then according to Che:

$$
\begin{array}{l} p ^ {*} (\theta) = C _ {\mathrm{s}} (q _ {1} ^ {*} (\theta), \dots , q _ {m} ^ {*} (\theta), \theta) \\ \quad + \int_ {\theta} ^ {\bar {\theta}} \left(C _ {\mathrm{s}} ^ {\prime} (\theta) (q _ {1} ^ {*} (t), \dots , q _ {m} ^ {*} (t), \theta) \right. \\ \quad \cdot \left(\frac {1 - F (t)}{1 - F (\theta)}\right) ^ {n - 1} \Bigg) \mathrm{d} t \end{array}
$$

where

$$
F (x) = \frac {x - \underline {{\theta}}}{\bar {\theta} - \underline {{\theta}}}
$$

The first component of the integral is the differential of the seller’s cost function by h where the optimal values of $q _ { i } \ ( q _ { i } ^ { * } )$ are assigned. That is:

$$
\begin{array}{l} \Rightarrow p ^ {*} (\theta) = \theta \cdot \sum_ {i = 1} ^ {m} a _ {i} \cdot \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2} \\ \qquad + \int_ {\theta} ^ {\bar {\theta}} \left(\sum_ {i = 1} ^ {m} a _ {i} \cdot \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2}\right) \\ \qquad \cdot \left[ \frac {1 - \frac {t - \underline {{\theta}}}{\bar {\theta} - \underline {{\theta}}}}{1 - \frac {\theta - \underline {{\theta}}}{\bar {\theta} - \underline {{\theta}}}} \right] ^ {[ n - 1 ]} d t \end{array}
$$

Resulting with:

$$
\begin{array}{l} p ^ {*} (\theta) = \left(\sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{4 \cdot a _ {i}}\right) \\ \cdot \left(\frac {1}{\theta} + \frac {1}{(\bar {\theta} - \theta) ^ {n - 1}} \cdot \int_ {\theta} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t ^ {2}} \mathrm{d} t\right) \end{array}\tag{□}
$$

The seller agent will decide about its bid according to its private cost parameter, the scoring rule, and its beliefs about the other sellers. We can see from Lemma 2 that its beliefs about other agents will only influence the price it will suggest. For example, as there are more bidders its price will decrease since the competition increases among the sellers/bidders. Therefore the price that each seller demands decreases following the principle of supply and demand. As the supply increases and the demand is constant the prices decrease.

As the announced weights $w _ { i }$ where $i { \in } [ 1 . . m ]$ increase, the quality of the proposed item, concerning $q _ { i } ,$ increases, and the price $p ^ { * }$ of the bid will increase too. As the private cost parameter h increases, that is, the seller’s efficiency decreases, it will suggest lower quality items. This can be inferred from the formulas of $q _ { i } ^ { * }$ and $p ^ { * } \colon$ as $\theta$ increases (less efficient seller), the denominators of $q _ { i } ^ { * }$ increase, so the values of $q _ { i } ^ { * }$ decrease. However, since a given seller has to compete with other sellers, it will also suggest lower prices (lower value of $p ^ { * } )$ when the quality of its item is lower.

To illustrate the proposed bidding strategy we use the following three-sellers and one buyer example bellow.

Example 1. Consider a situation where a big company (e.g., a supermarket or a university) is trying to build a homepage. To do so, this company needs to have a certain data storage space which will have an adequate level of response speed. Consequently, this company may conduct a reverse auction against the potential web hosting (e.g., StreamlineNet [28], netfirms [21]). Assume we have one company that needs a service from a web host who becomes the auctioneer (buyer) and assume there are three competing web hosts who play as the bidders $( s _ { 1 } , \ s _ { 2 } , $ and $s _ { 3 } )$ . The attributes which the auction considers are the data storage space $q _ { 1 } ,$ , and respond speed $q _ { 2 } .$

Assume the utility functions of the participants are as follow:

$$
\begin{array}{l} U _ {\text { buyer }} (p, q _ {1}, q _ {2}) = - p + 3 \cdot \sqrt {q _ {1}} + 5 \cdot \sqrt {q _ {2}} \\ U _ {s _ {1}} (q _ {1}, q _ {2}) = p - 0. 2 \cdot q _ {1} - 0. 4 \cdot q _ {2} \\ U _ {s _ {2}} (q _ {1}, q _ {2}) = p - 0. 4 \cdot q _ {1} - 0. 8 \cdot q _ {2} \\ U _ {s _ {3}} (q _ {1}, q _ {2}) = p - 0. 6 \cdot q _ {1} - 1. 2 \cdot q _ {2} \end{array}
$$

Since we prove that the bidders decide about their bids based on the scoring function let us assume the following scoring function:

$$
S (p, q _ {1}, q _ {2}) = - p + 2 \cdot \sqrt {q _ {1}} + 4 \cdot \sqrt {q _ {2}}
$$

Notice that the weights in the scoring function $^ { ( 2 , 4 ) }$ are different than the real weights appearing in the buyer utility function (3,5). Given this information, based on Lemma 2 the three sellers will propose the following bids in the first-score sealed-bid auction.

$$
\mathrm{BID} _ {1} = (p = 2 2. 5, q _ {1} = 2 5, q _ {2} = 2 5)
$$

$$
\mathrm{BID} _ {2} = (p = 9. 7 2 8 5, q _ {1} = 6. 2 5, q _ {2} = 6. 2 5)
$$

$$
\mathrm{BID} _ {3} = (p = 5. 8 4 4 0, q _ {1} = 2. 7 7 7 8, q _ {2} = 2. 7 7 7 8)
$$

So we can see that there are bidders that will offer high qualities but will require high prices and other sellers propose lower quality values for much lower prices. The winner in this case will be seller $s _ { 1 }$ who obtains a score equal to 7.5.

## 4.3. Optimal buyer’s strategy and the auction result

The main goal of the following analysis is to find the optimal scoring rule that yields the best results for the buyer agent. The motivation to search for an optimal scoring rule evolves from the fact that there are situations in which the competition among the seller agents is not strong enough and therefore some sellers can utilize these situations and offer bids which yield a high profit for them. In these cases the buyer can increase its gains by manipulating its scoring rule.

In order to find the optimal scoring rule we should first calculate the buyer’s expected payoff as a function of the environment parameters, and then find the value of the announced weights of the scoring rule that maximizes the buyer’s expected payoff.

Given the optimal bid to be placed by each bidder, and given the buyer’s beliefs about the range of the bidders’ types, the expected payoff of the buyer can be evaluated. In Definition 1, we define the method of calculating the buyer’s expected payoff of the firstscore sealed-bid auction, $\mathrm { E } \dot { \mathrm { P } } ^ { 1 }$ in the general case with no restriction to a specific model.

Definition 1. Given the scoring rule, the utility functions of the buyer and the sellers, the number of sellers (n) and the distribution of the sellers’ types, the buyer’s expected payoff in a first-score sealed-bid auction $\mathrm { E P } ^ { \hat { 1 } }$ is as follows:

$$
\begin{array}{c} \mathrm{EP} ^ {1} \big (\underline {{\theta}}, \bar {\theta} \big) = \int_ {\theta} ^ {\bar {\theta}} U _ {\text { buyer }} (p ^ {*} (t), q _ {1} ^ {*} (t),..., q _ {m} ^ {*} (t)) \\ \cdot (1 - F (t)) ^ {n - 1} \cdot n \cdot f (t) \mathrm{d} t. \end{array}\tag{9}
$$

The buyer’s expected payoff $\mathrm { E P ^ { 1 } }$ is the actual expected payoff (utility) value of the highest possible bid among the n participating sellers. This can be found by calculating the average utility of the buyer from each possible winning bid which is based on the bidders’ private cost parameters, $\theta { \in } [ \underline { { \theta } } , \bar { \theta } ]$ weighted by the probability of each bidder’s cost parameter.

Suppose that the winning bidder is of type t. In this case, the winning bid will be $( p ^ { * } ( t ) , q _ { 1 } ^ { * } ( t ) , . . . , q _ { \mathrm { m } } ^ { * } ( t ) )$ 2 and the utility of the buyer from this bid will be

$$
U _ {\text { buyer }} (p ^ {*} (t), q _ {1} ^ {*} (t), \dots , q _ {m} ^ {*} (t))
$$

The probability of a particular bidder to be of type t is $f ( t )$ , while the probability of this bidder to win is $\left( 1 - F ( t ) \right) ^ { n - 1 }$ , which is the probability for the other bidders to have lower types (and thus, to suggest bids with lower scoring values). Since each of the n bidders may be of type t and therefore be the winner, we multiply the probability of the winner bidder to be of type t by n. Thus, the probability of the winning bid to be $( p ^ { * } ( t ) , q _ { 1 } ^ { * } ( t ) , . . . , q _ { m } ^ { * } ( t ) ) { \mathrm { ~ i s ~ } } ( 1 - F ( t ) ) ^ { n - 1 } \cdot n \cdot f ( t ) .$ Considering all possible values of t, from $\underline { { \theta } }$ to ${ \bar { \theta } } ,$ we obtain the expression $\mathrm { E P ^ { 1 } }$

Based on the above definition, we will proceed to define $\mathrm { E P } ^ { 1 }$ as a function of the buyer’s utility function, the scoring function, and the beliefs about the bidders distribution. Using the explicit formulation of $\mathrm { E P ^ { 1 } }$ , we will be able to proceed and find its behavior and the optimal strategy for the auctioneer.

Definition 2. Given the scoring rule (including the announced weights $w _ { i } ,$ where $i { \in } [ 1 . . m ] )$ , the utility functions of the buyer (including the actual weights $W _ { i } ,$ , where $i { \in } [ 1 . . m ] )$ , the number of sellers (n) and that the cost parameters of the sellers are independently and identically distributed over $( \theta { \in } [ \underline { { { \theta } } } , \bar { \theta } ] ;$ ; the buyer’s expected payoff in a first-score sealed-bid auction $\mathrm { E P ^ { 1 } }$ is:

$$
\begin{array}{l} \mathrm{EP} ^ {1} \left(\underline {{\theta}}, \bar {\theta}\right) = \frac {- n}{\left(\bar {\theta} - \underline {{\theta}}\right) ^ {n}} \cdot \left(\sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{4 \cdot a _ {i}}\right) \\ \quad \cdot \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - t\right) ^ {n - 1}}{t} \mathrm{d} t \right. \\ \quad + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - z\right) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t \\ \quad + \frac {n}{\left(\bar {\theta} - \underline {{\theta}}\right) ^ {n}} \cdot \left(\sum_ {i = 1} ^ {m} \frac {W _ {i} \cdot w _ {i}}{2 \cdot a _ {i}}\right) \\ \quad \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - t\right) ^ {n - 1}}{t} \mathrm{d} t \end{array}\tag{10}
$$

Eq. (10) is induced from Eq. (9) by substituting $( p ^ { * } ( t ) , \ q _ { 1 } ^ { * } ( t ) , \ . . . , \ q _ { m } ^ { * } ( t ) )$ with the explicit bid of a bidder with a cost parameter $t ,$ as stated in Lemma 2. Next, the values of $f ( t )$ and $F ( t )$ are substituted, where $\begin{array} { r } { F ( t ) = \frac { t - \theta } { \theta - \theta } } \end{array}$ and $\begin{array} { r } { f ( t ) = \frac { 1 } { \theta - \theta } . } \end{array}$

After the assignment of the full function in $\mathrm { E P ^ { 1 } }$ , the buyer’s expected payoff in the first-score sealed-bid auction in our model results in:

$$
\begin{array}{l} \mathrm{EP} ^ {1} \left(\underline {{\theta}}, \bar {\theta}\right) = \frac {- n}{\left(\bar {\theta} - \underline {{\theta}}\right) ^ {n}} \cdot \left(\sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{4 \cdot a _ {i}}\right) \\ \qquad \cdot \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - t\right) ^ {n - 1}}{t} \mathrm{d} t \right. \\ \qquad + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - z\right) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t \Bigg) \\ \qquad + \frac {n}{\left(\bar {\theta} - \underline {{\theta}}\right) ^ {n}} \cdot \left(\sum_ {i = 1} ^ {m} \frac {W _ {i} \cdot w _ {i}}{2 \cdot a _ {i}}\right) \\ \qquad \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\left(\bar {\theta} - t\right) ^ {n - 1}}{t} \mathrm{d} t \end{array}
$$

The values of $a _ { i }$ where $i { \in } [ 1 . . m ]$ influence the $\mathrm { E P } ^ { 1 }$ such that when $a _ { i }$ increases, the expected payoff of the buyer decreases. Intuitively, the reason stems from the fact that as the costs of the sellers increase, they will suggest worse bids, and the utility of the buyer from the winning bid will decrease.

By observing Eq. (10) of the $\mathrm { E P ^ { 1 } }$ one can infer that the influence of the announced weights $w _ { i }$ has mixed directions. Thus, the optimal values of $w _ { i }$ where $i { \in } [ 1 . . m ]$ can be calculated as a function of the other parameters. Consider Example 1, which we presented in Section 4.2 to illustrate the effect of different weights (i.e., different scoring functions) on the resulting expected payoff.

Example 2. Consider the following scoring functions:

(1) A scoring function which is equal to the buyer’s utility function (no lying):

$$
S _ {1} = U _ {\text { buyer }} (p, q _ {1}, q _ {2}) = - p + 3 \cdot \sqrt {q _ {1}} + 5 \cdot \sqrt {q _ {2}}
$$

(2) A scoring function with modified weights (defined in Example 1 in Section 4.2):

$$
S _ {2} (p, q _ {1}, q _ {2}) = - p + 2 \cdot \sqrt {q _ {1}} + 4 \cdot \sqrt {q _ {2}}
$$

(3) A scoring function with the optimal weights (i.e., the ones that maximize the buyer’s expected-payoff):

$$
\begin{array}{r l} S _ {3} (p, q _ {1}, q _ {2}) = & - p + 2. 0 4 1 9 \cdot \sqrt {q _ {1}} + 3. 4 0 3 2 \\ & \cdot \sqrt {q _ {2}} \end{array}
$$

For each of these scoring functions we derived the buyer’s expected payoff using Eq. (10) of Definition 2:

$$
\begin{array}{l} \text {(1)} S _ {1} \Rightarrow \mathrm{EP} ^ {1} = 1 1. 7 1 1 8 \\ \text {(2)} S _ {2} \Rightarrow \mathrm{EP} ^ {1} = 1 4. 7 4 7 4 \\ \text {(3)} S _ {3} \Rightarrow \mathrm{EP} ^ {1} = 1 5. 0 1 8 6 \end{array}
$$

From these results one can realize, that not telling the truth about the buyer’s preferences may yield better outcomes for the buyer (the results of $S _ { 2 }$ and $S _ { 3 }$ are better than the results yielded by $S _ { 1 } ,$ the real utility function). Consequently, we conclude that the auctioneer should be interested in manipulating the scoring function since it is one of its control factors as it has a significant effect on the results. In the following theorem we specify a method for calculating the optimal scoring function by the auctioneer given the bidder’s cost parameters’ distribution range and the number of participating bidders.

Theorem 1. Given the model described in Section 3, the optimal values of the announced weights, $w _ { i }$ where i<sup>a</sup>[1..m], for the buyer in a first-score sealed-bid auction are:

$$
\begin{array}{l} w _ {i} (\bar {\theta}, \underline {{\theta}}) \\ = W _ {i} \cdot \frac { \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t}{\left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right)}. \end{array}\tag{11}
$$

Proof. In order to find the optimal weights of the scoring rule that maximize the buyer’s expected payoff, we first find the differential of $\mathrm { E P ^ { 1 } }$ with respect to the weights (notice that the weights are symmetric and independent, therefore the calculation of the optimal weights are identical):

$$
\begin{array}{l} \frac {\partial \mathrm{EP} ^ {1} (\underline {{\theta}} , \bar {\theta})}{\partial w _ {i}} = \frac {- n \cdot}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \frac {w _ {i}}{2 \cdot a _ {i}} \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t \right. \\ \qquad + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t \Bigg) \\ \qquad + \frac {n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \frac {W _ {i}}{2 \cdot a _ {i}} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t. \end{array}
$$

By comparing the differential of $\mathrm { E P ^ { 1 } }$ to zero the maximum value of $w _ { i }$ is identified

$$
\begin{array}{l} \frac {\partial \mathrm{EP} ^ {1} (\underline {{\theta}} , \bar {\theta})}{\partial w _ {i}} = \frac {- n \cdot}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \frac {w _ {i}}{2 \cdot a _ {i}} \\ \times \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) \\ + \frac {n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \frac {W _ {i}}{2 \cdot a _ {i}} \\ \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t = 0 \end{array}
$$

$$
\begin{array}{l} \Rightarrow w _ {i} \cdot \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) \\ = W _ {i} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t. \\ \Rightarrow w _ {i} (\bar {\theta}, \underline {{\theta}}) \\ = W _ {i} \cdot \frac {\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t}{\left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{dz} \mathrm{d} t\right)}. \end{array}
$$

5

Based on the above results, if the number of sellers, the distribution of h, and the sellers’ optimal strategies are known to the buyer, the buyer can announce the optimal scoring function that will optimize its expected payoff from the auction. Given all the parameters’ values the auctioneer can immediately find the optimal values by solving the equation or by using a mathematical tool such as Mapel or Matlab.

Notice that the ratio between $w _ { i }$ and $w _ { j }$ remains the same as the ratio between $W _ { i }$ and $W _ { j } .$ . Due to this property, for each bid, the ratio of $q _ { i }$ and $q _ { j }$ remains equal to their ratio given the actual weights (according to Lemma 2). The only difference is in the prices with regard to the qualities. If $w _ { i } < W _ { i } ,$ , the price will be lower than the price given the actual weights. Similarly, the qualities will be lower and vice versa.

Fig. 1 demonstrates the influence of n on $w _ { i } ,$ , where $W _ { i } { = } 1$ , and the values of h are between 0.5 and 1. It can be shown that as n increases, the ratio $w _ { i } / W _ { i }$ increases, and it approaches 1 for higher values of n, i.e., as the number of bidders increases, the buyer is more motivated to announce a scoring function closer to its real utility function.

The relation between $\underline { { \theta } } / \bar { \theta }$ also influences the announced weights. As the relation increases the rate in which the scoring function converges to the real utility function decreases. That is, when the weights $w _ { i }$ start with lower values, the convergence to $W _ { i }$ is slower.

![](/api/attachments/4FAW8XUH/fulltext/images/eea2ce46c29f5d9e1255b4eaeb5de2d32a53c3bff252f923ac64aa50d50aeca2.jpg)  
Fig. 1. $w _ { i } / W _ { i }$ as a function of the number of bidders when the sellers’ cost parameters are in the range of (0.5, 1).

For example, in Fig. 1, the relation between ${ \bar { \theta } } / \underline { { \theta } }$ ([0.5, 1]) is 2 while in Fig. 2 the relation between ${ \bar { \theta } } / { \underline { { \theta } } }$ ([0.1, 0.5]) is 5. Notice that the values of $w _ { i }$ in Fig. 1 are closer to 1, i.e. to the value of $W _ { i } ,$ than the values in Fig. 2. In Fig. 3 we demonstrate the influence of the relation between ${ \bar { \theta } } / { \underline { { \theta } } }$ , on $w _ { i } .$ . The parameters were set to $n { = } 4 , \underline { { \theta } } { = } 1 , W _ { i } { = } 1$ , while the value of $\bar { \theta }$ varied from 2 to 20.

The relation between ${ \bar { \theta } } / { \underline { { \theta } } }$ is actually a measurement of the relative distribution of the sellers’ types. That is, if the value of the relative distribution is low the sellers are homogenous which means that the competition is very high and there is no need to manipulate the utility function. Thus, the buyer is motivated to tell the truth (the relation between $w _ { i }$ and $W _ { i }$ approaches

![](/api/attachments/4FAW8XUH/fulltext/images/bbc38f4ac0b67a3c929fb755241b9764f6e5c6712e1b46b9ef3b5cc0bb9358e6.jpg)  
Fig. 2. $w _ { i } / W _ { i }$ as a function of the number of bidders when the sellers’ cost parameters are in the range of (0.2, 1).

![](/api/attachments/4FAW8XUH/fulltext/images/3a359dea8ab3e158fedaa50e9f0abe3f659546b4adc3f785fdb20d8bf5c6baf5.jpg)  
Fig. 3. The influence of the relation $\bar { \theta } / \underline { { \theta } }$ on $w _ { i } / W _ { i }$

1) (see Fig. 3). However, when the relative distribution is high the sellers are heterogeneous. In this case the strong seller/s can utilize this situation and increase its/their profit. Consequently, the buyer is motivated to modify the real weights. Notice that the specific values of $\bar { \theta }$ and h have no affect on the expected value and the scoring rule. Only the relation between $\bar { \theta }$ and $\underline { { \theta } }$ affects the auction design.

## 5. Multi-attribute English auction

Recently, the English auction has become a very popular mechanism for purchasing items on the Internet. The most substantial reason that makes this auction so popular is the fact that users feel comfortable participating in it since they do not have to speculate nor estimate the bids of the other competitors. Additional advantages of the English auction protocol over other existing protocols (e.g. first price sealed bid auction, Dutch auction), are: (a) It is an incentive compatible protocol, i.e., the bidders will have no motivation to manipulate and change bids according to their beliefs about the other agents. (b) The English auction is the best-preferred protocol if the valuation problems of the agent are difficult [11]. In the rest of this section, we analyze the model given in Section 3 for the English protocol. We first show the optimal bids to be suggested by each bidder, and then we prove which bidder and which of its bids will win. We proceed by analyzing the expected payoff of the auctioneer and its optimal scoring rule, and finally, we compare the buyer’s expected payoff from the first score sealed-bid auction and the English auction.

## 5.1. Protocol’s description

We consider one of the variations of a multi-attribute English auction protocol discussed in [12]. In particular, we consider the Sequential Full-Information-Revelation protocol. According to this protocol, the buyer agent announces (1) a scoring-rule function that describes the required item, (2) the closing interval, which is the length of the time interval, where if no new bid is made the auction is closed, and (3) the minimal increment allowed, D. We assume that the bids must be in increments of D, otherwise, the auction can theoretically proceed to infinity since the score and the qualities’ values are continuous dimensions.

In the Sequential Full-Information-Revelation protocol each participating seller agent receives a serial number that defines the order of the bidding among the agents. In contrast to the traditional English protocol we allow bidders to place a bid which is equal to the current best bid. Specifically, in each step that a bid is proposed any seller agent that wants to place a bid, which yields the same score, can do so at a predefined interval of time. In general, in each step, the seller whose turn it is to bid may place a bid (it does not have to submit a bid), which should be better than or equal to the previous proposed bid by at least the minimal increment of D with regard to the scoring rule function.

We allow this feature in order to restrict the effect of the bidding order. The buyer chooses one of the bids that yields the same score randomly. Note that this option of bidding equal bids does not appear in the classic auction protocols. However it was also introduced in the Yankee protocol (English auction for multi-unit cases) to which we refer in more detail in Section 6.2.

## 5.2. Bidder agent’s strategies in the English auction

We start by considering the optimal bid to be offered by each bidder in each step. First, as shown in Lemma 1 and Lemma 2, the optimal qualities’ values are chosen independently of the auction protocol. Also, the price to be chosen and the beliefs about the other participants are also independent of the current selected bid. Therefore, we begin by directly finding the optimal price to be offered in each step of the auction, given the bidder’s properties and given the current selected bid.

In Lemma 3 we specifically define the bid’s exact value, given the seller’s type, the seller’s utility function, the scoring rule, the minimal increment of D and the score of the current best bid which is termed the selected bid.

Lemma 3. Given the model described inSection 3, in a sequential full-information revelation English auction, and given the last selected bid that was placed by another seller, the seller’s dominant strategy is:

(1) Bid a higher score bid (S(selected)  D) while the seller’s utility is positive or zero, that is:

$$
p ^ {*} (\theta , \text { selected }) = \sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \cdot \theta} - S (\text { selected }) - D\tag{12}
$$

$$
q _ {i} ^ {*} (\theta) = \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2}\tag{13}
$$

where $i \in [ I . . m ] .$

(2) Otherwise, bid an equal score bid S(selected) while the seller’s utility is positive or zero, that is:

$$
p ^ {*} (\theta , \text { selected }) = \sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \cdot \theta} - S (\text { selected })\tag{14}
$$

$$
q _ {i} ^ {*} (\theta) = \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2}\tag{15}
$$

## (3) Otherwise, quit the auction.

Proof. If the selected bid was offered by the seller we consider then the dominant strategy is not to bid (trivial) since this seller may unnecessarily reduce its utility by any other legal action. However, if the selected bid does not belong to the seller we consider, then the seller should try (while its utility is positive or equal to zero) to place the minimum bid which will maximize its probability to win. That is targeting the score of the bid to be higher than the score of the current selected bid plus the minimal increment D. If the seller can allow himself to bid accordingly then by offering an equal bid it reduces its probability of winning by at least 50%. Specifically, the seller will propose the optimal qualities’ values as specified in Lemma 2 and determine the price that will achieve the total bid of the desired score (S(selected) + D):

$$
\begin{array}{l} S (p ^ {*}, q _ {1} ^ {*},..., q _ {m} ^ {*}) = S (\text { selected }) + D \\ \Rightarrow - p ^ {*} + \sum_ {i = 1} ^ {m} w _ {i} \cdot \sqrt {\left(\frac {w _ {i}}{2 \cdot a _ {i} \cdot \theta}\right) ^ {2}} = S (\text { selected }) + D \\ \Rightarrow p ^ {*} = \sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \cdot \theta} - S (\text { selected }) - D \end{array}
$$

However, if by using the above option the seller yields a negative utility, the second option is to bid an equal bid that still yields a non-negative utility, which increases its winning probability (from zero to a positive value). In this case the qualities again are the optimal ones, as derived in Lemma 2, and the price is set to meet the current score of the selected bid:

$$
p ^ {*} = \sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \cdot \theta} - S (\text { selected })
$$

If the second option also yields a negative utility, then according to the protocol no other action that yields a non-negative utility can be made. Therefore the seller is advised to quit the auction. 5

In Lemma 3 we specify the bidding strategy in the sequential full-information-revelation English auction. Notice that in the sequential full-informationrevelation auction the strategy of choosing the price to offer does not require any beliefs about the cost parameters nor the number of other participating agents. In contrast, in the first-score sealed-bid auction the beliefs about the other seller’s cost parameters are considered in the process of determining the bid’s price value.

To demonstrate the sequential multi-attribute English auction’s process lets review the three sellers’ example that we first describe in Example 1 in Section 4.2:

Example 3. Given the utility functions of the participants and the announced scoring function:

$$
\begin{array}{l} U _ {\text { buyer }} (p, q _ {1}, q _ {2}) = - p + 3 \cdot \sqrt {q _ {1}} + 5 \cdot \sqrt {q _ {2}} \\ U _ {s _ {1}} (q _ {1}, q _ {2}) = p - 0. 2 \cdot q _ {1} - 0. 4 \cdot q _ {2} \end{array}
$$

$$
\begin{array}{l} U _ {s _ {2}} (q _ {1}, q _ {2}) = p - 0. 4 \cdot q _ {1} - 0. 8 \cdot q _ {2} \\ U _ {s _ {3}} (q _ {1}, q _ {2}) = p - 0. 6 \cdot q _ {1} - 1. 2 \cdot q _ {2} \\ S (p, q _ {1}, q _ {2}) = - p + 2 \cdot \sqrt {q} _ {1} + 4 \cdot \sqrt {q} _ {2} \end{array}
$$

Assume that seller $s _ { 1 }$ is given serial number 1, seller $s _ { 2 }$ is given serial number 2, and seller $s _ { 3 }$ is given serial number 3. Moreover, assume that the minimal bid increment allowed is D = 0.5.

Before beginning the auction simulation process, first we have to calculate the limitation of the bidders in the sense of the best bid they can offer, (a successive bid with a higher score will result in a negative utility for the bidder). Namely, we calculate the best bid that yields a zero utility for the seller where the optimal qualities are assumed (as specified in Eq. (13)). In other words we will calculate the minimum price a seller can bid without causing a loss for himself:

$$
\begin{array}{r l} U _ {\mathrm{s}} (p, q _ {1} ^ {*},..., q _ {m} ^ {*}, \theta) & = p - \theta \cdot \left(\sum_ {i = 0} ^ {m} a _ {i} \cdot \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta}\right) ^ {2}\right) \\ & = 0 \Rightarrow p _ {\text {ZeroUtility}} = \left(\frac {w _ {i} ^ {2}}{4 \cdot a _ {i} \theta}\right) \end{array} \tag {1}\tag{16}
$$

Given the optimal qualities and the minimum price we can calculate the highest score termed the MaxScore(s<sub>i</sub>) that a seller is able to receive in the auction (assuming that an agent is rational and does not bid something that yields him a negative utility).

$$
\begin{array}{l} \text { MaxScore } (s _ {i} (\theta)) = - \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{4 \cdot a _ {i} \theta}\right) + \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \theta}\right) \\ \Rightarrow \text { MaxScore } (s _ {i} (p _ {\text { ZeroUtility }}, q _ {1} ^ {*},..., q _ {m} ^ {*}, \theta)) \\ = \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{4 \cdot a _ {i} \theta}\right) \end{array} \tag {17}
$$

Given this background, we calculate the MaxScor-$\operatorname { e } ( s _ { i } )$ for each of the sellers:

$$
\begin{array}{l} \text { MaxScore } (s _ {1}) = 1 5 \\ \text { MaxScore } (s _ {2}) = 7. 5 \\ \text { MaxScore } (s _ {3}) = 5 \end{array}
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
:
Stage 15:
Seller $s_1$ proposes ($p=23, q_1=25, q_2=25$) (which yields score=7).
Stage 16:
Seller $s_2$ proposes ($p=7:5, q_1=6:25, q_2=6:25$) (which yields score=7:5).
Stage 17:
Seller $s_1$ proposes ($p=22; q_1=25; q_2=25$) (which yields score=8).
Stage 18:
At this stage it is seller $s_2$'s turn to bid. The current score is 8 but MaxScore($s_2$)=7:5. Therefore, at this point seller $s_2$ quits the auction. Consequently, the auction terminates with seller $s_1$ providing the winning bid.
END
</div>

At this point we are ready to start the auction where the reservation price of the buyer (auctioneer) is assumed to be zero.

Stage 1: Seller s<sub>1</sub> proposes $( p = 2 9 . 5 , q _ { 1 } = 2 5 , q _ { 2 } = 2 5 )$ (which yields score = 0.5).

Stage 2: Seller $s _ { 2 }$ proposes $( p = 1 4 ; q _ { 1 } = 6 . 2 5 , q _ { 2 } = 6 . 2 5 )$ (which yields score = 1).

Seller $s _ { 3 }$ proposes $( p = 8 . 5 , \ q _ { 1 } = 2 . 7 7 7 8 , \ q _ { 2 } = 2 . 7 7 7 8 )$ (which yields score = 1.5).

It is seller $s _ { 3 } \mathrm { ^ { * } s }$ turn to bid, but the current score of the last proposed bid is 5.5, whereas Max-Score(s<sub>3</sub>) = 5. Therefore, at this point seller $s _ { 3 }$ quits the auction.

This example shows that the bid increment is one of the factors the auctioneer can control. In Section 6.2 we discuss this issue in more details.

The next question is, given the utility functions form of the auction participants, the range of the sellers types (i.e. [h,h<sup>¯</sup>]), the announced scoring rule and the sellers optimal bidding strategy, (1) can the buyer agent estimate which of the sellers will win and (2) can it estimate its expected payoff?

We will start by answering the first question. In Lemma 4 we will show that the winning seller is the seller with the lowest cost parameter h. The intuition of this property (Lemma 4) is that for any bid offered by another seller, the seller with the lowest cost parameter can offer a better bid with regard to the scoring rule. That is, the seller with the lowest cost parameter can overcome any of the other sellers throughout the English auction process. In the firstscore sealed-bid auction, the stronger bidder does not necessarily win since the result will depend on the beliefs that the bidders have about their competitors. If all the bidders have exactly the same belief (distribution function and range) then the strongest bidder will win the auction also in the first-score sealedbid auction.

## 5.3. Optimal buyer’s strategy and auction results

The assumption in an English auction is that a seller bids while its profit is non-negative. Suppose that seller $s _ { i }$ is the seller with the lowest cost parameter $\theta _ { i } ,$ and seller $s _ { j }$ is the seller with cost parameter $\theta _ { j }$ that is the second lowest cost parameter among the set of bidders. Then, seller $s _ { i }$ actually competes with seller $s _ { j } ,$ which is its strongest competitor. Therefore, the prices that seller $s _ { i }$ will offer will decrease until seller $s _ { j }$ quits the auction and this happens when its utility becomes non-positive. From this point on, seller $s _ { i }$ has to reduce the price in such a way that will increase its score in D which is the minimal increment allowed in the auction protocol we discuss. In Lemma 4 we define the winning bid considering these assumptions.

Lemma 4. Denote by $s _ { i }$ the seller with the lowest value of h, and by $s _ { j }$ the seller with the second lowest h. In the sequential full-information revelation English auction protocol, seller $s _ { i }$ is the winner of the auction whenever $\begin{array} { r } { D \le \frac { 1 } { 4 } \cdot \left( \frac { 1 } { \theta _ { i } } - \frac { 1 } { \theta _ { j } } \right) \cdot \sum _ { t = 1 } ^ { m } \frac { w _ { t } ^ { 2 } } { a _ { t } } } \end{array}$ is:

$$
\begin{array}{l} \left\{p = \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right) - D; q _ {t} \right. \\ \qquad \qquad \qquad \qquad \qquad \qquad = \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) ^ {2}, \text {   where,   } t \in [ 1.. m ] \Bigg \}. \end{array}\tag{18}
$$

Proof. See Appendix.

The qualities of the winning bid are defined in Lemma 4. However, the price depends implicitly on the cost function of the second best seller, denoted by $j .$ In particular, as the expenses of the second best seller increase, i.e., $\theta _ { j }$ increases, (that is the second best seller is less efficient) the winning price offered by seller $s _ { i }$ (the strongest seller) increases. Intuitively, the reason for this result is that as $\theta _ { i }$ increases (the seller becomes less efficient) and the qualities $q _ { t } ( \theta _ { i } )$ where $t { \in } [ 1 . . m ]$ decrease. Therefore, the seller must compensate this by suggesting a lower price in order to compete with the other bidders. In addition, as $\theta _ { j }$ decreases, the second best bidder is stronger, so seller $s _ { i }$ must suggest a more competitive price in order to win against agent $j ,$ and thus, the winning price decreases.

Given the information about the auction, we can try to analyze it from the auctioneer’s (buyer’s) point of view. That is, to calculate the buyer’s expected payoff given the environment details. In order to estimate the buyer’s expected payoff, we actually have to estimate the best bid and with which probability the buyer may receive it. This brings us to the following lemma that explicitly calculates the buyer’s expected payoff $\mathrm { E P ^ { E } }$ (Expected Payoff for the version of an English auction).

Lemma 5. In a sequential full-information revelation auction protocol of one buyer and n sellers with types independently and identically distributed over $[ \underline { { \theta } } , \bar { \theta } ] ,$ given the minimal increment of D defined inLemma $^ { 4 , }$ and given the real weights $W _ { t }$ where t<sup>a</sup>[1..m] of the buyer’s utility and the announced weights wt where t<sup>a</sup>[1..m] of the scoring rule, the buyer’s expected payoff $\bar { E P } ^ { \bar { E } }$ is:

$$
\begin{array}{l}\mathrm{EP} ^ {\mathrm{E}} (\underline {{\theta}}, \bar {\theta}) = \frac {1}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot n \cdot (n - 1) \cdot \left(\sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{4 \cdot a _ {t}}\right) \right.\\\cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {i}} ^ {\bar {\theta}} \frac {(\bar {\theta} - \theta_ {j}) ^ {n - 2}}{\theta_ {j}} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}\\+ \left(- \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{2 \cdot a _ {t}}\right) + \sum_ {t = 1} ^ {m} \left(\frac {W _ {t} \cdot w _ {t}}{2 \cdot a _ {t}}\right)\right)\\\cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {i}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i} + D\\\cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {i}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}\left. \right)\end{array}\tag {19}
$$

Proof. The expected payoff is calculated by:

$$
\begin{array}{l} \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \left[ \int_ {\theta_ {i}} ^ {\bar {\theta}} \left(U _ {\text { buyer }} (\text { winning   bid }) \cdot (1 - F (\theta_ {j})) ^ {n - 2} \right. \right. \\ \left. \cdot f (\theta_ {j}) \cdot f (\theta_ {i}) \cdot n \cdot (n - 1)) \mathrm{d} \theta_ {j} \right] \mathrm{d} \theta_ {i} \end{array}
$$

The expected payoff actually calculates the average utility of the buyer from each possible winning bid weighted by the probability of this winning bid, where the winning bid is the bid calculated in Lemma 4. In this double integral we cover all the probabilities of the lowest cost parameter $\theta _ { i } ,$ , and all the probabilities of the second lowest cost parameter $\theta _ { j } ,$ multiplied by the buyer’s utility from the best bid of the given cost parameters. The probability of a certain lowest cost parameter $\theta _ { i }$ and of a certain second lowest cost parameter $\theta _ { j }$ is actually the probability that all the other $n - 2$ sellers have higher cost parameters than $\theta _ { j } ,$ multiplied by the probability of having one seller of cost parameter $\theta _ { j }$ and multiplied by the probability of having another seller with cost parameter $\theta _ { i } .$ This multiplication is multiplied by $n ( n - 1 )$ which is the number of possibilities (n) for the specific seller to be of cost parameter $\theta _ { i }$ multiplied by (n  1) the number of possibilities for a seller to be of cost parameter $\theta _ { j } .$

By substituting all the explicit functions we receive:

$$
\begin{array}{l} \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {i}} ^ {\bar {\theta}} \left(\sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{2 \cdot \theta_ {j}} - \frac {1}{\theta_ {i}}\right) \right. \\ \left. + \sum_ {t = 1} ^ {m} \left(W _ {t} \cdot \sqrt {\left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) ^ {2}}\right) + D\right) \cdot \left(\frac {\bar {\theta} - \theta_ {j}}{\bar {\theta} - \underline {{\theta}}}\right) ^ {n - 2} \\ \cdot \frac {1}{\bar {\theta} - \underline {{\theta}}} \cdot \frac {1}{\bar {\theta} - \underline {{\theta}}} \cdot n \cdot (n - 1) d \theta_ {j} d \theta_ {i} \end{array}
$$

By opening the parenthesis and simplifying the equation we obtain the buyer’s expected payoff. 5

Notice that the only information that the buyer should obtain is the range of the sellers cost parameters’, the forms of the sellers’ utility functions, and the number of sellers, in order to estimate its expected payoff. It is interesting to note that if we multiply h and h<sup>¯</sup> by a given value, and we divide at where t<sup>a</sup>[1..m] by the same value, the result of $\mathrm { E P ^ { E } }$ remains the same. This means that the buyer’s expected payoff does not depend on the exact values of the parameters, but only on the relations between them.

The ability of predicting the buyer’s expected payoff leads to the most interesting phase of the auction design, which is searching for the optimal scoring rule that will maximize the buyer’s expected payoff. In other words, this leads to finding the optimal weights $w _ { t }$ where $t { \in } [ 1 . . m ]$ to be announced. These optimal values of the scoring function can be found by differentiating the buyer’s expected payoff function each time by one of the weights $w _ { t }$ where $t { \in } [ 1 . . m ]$ since they are independent.

Let us consider the example we use throughout the paper and calculate the $\mathrm { E P } ^ { \mathrm { \check { E } } }$ regarding the three different scoring functions we defined in Example 2 in Section 4.3:

Example 4. Consider the following scoring functions:

$$
\begin{array}{l} \text {(1) S_{1}} (p, q _ {1}, q _ {2}) = - p + 3 \cdot \sqrt {q _ {1}} + 5 \cdot \sqrt {q _ {2}} \\ \text {(2) S_{2}} (p, q _ {1}, q _ {2}) = - p + 2 \cdot \sqrt {q _ {1}} + 4 \cdot \sqrt {q _ {2}} \\ \text {(3) S_{3}} (p, q _ {1}, q _ {2}) = - p + 2. 0 4 1 9 \cdot \sqrt {q _ {1}} + 3. 4 0 3 2 \cdot \\ \sqrt {q _ {2}} \end{array}
$$

For each of these scoring functions we derive the buyer’s expected payoff using Eq. (10) of Definition 2:

$$
\begin{array}{l} (1) S _ {1} \Rightarrow \mathrm{EP} ^ {1} = 1 2. 2 1 1 8 \\ (2) S _ {2} \Rightarrow \mathrm{EP} ^ {1} = 1 5. 2 4 7 4 \\ (3) S _ {3} \Rightarrow \mathrm{EP} ^ {1} = 1 5. 5 1 8 6 \end{array}
$$

The results demonstrate again (Example 2 in Section 4.3) that some optimal weights to be announced in the scoring function exist, as we specify in the following theorem.

Theorem 2. Given a sequential full-information revelation auction protocol of one buyer and n sellers with types independently and identically distributed over [h,h<sup>¯</sup>] and given the real weights, $W _ { t }$ where $t { \in } / I . . m ]$ , of the buyer utility function, the optimal values of the announced weights, $w _ { t }$ where $t { \in } / I . . m ]$ , of the scoring rule are: w ¼ W

$$
\cdot \frac {\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {t}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}}{2 \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {t}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i} - \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {t}} ^ {\bar {\theta}} \frac {(\bar {\theta} - \theta_ {j}) ^ {n - 2}}{\theta_ {j}} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}}\tag{20}
$$

where $i \in [ 1 . . m ]$

Proof. In order to find the announced weights, $w _ { t }$ where $t { \in } [ 1 . . m ]$ , of the scoring rule that maximize the buyer’s expected payoff $\bar { \mathrm { E P } } ^ { \mathrm { E } }$ , we differentiate the function $\mathrm { E \bar { P } ^ { E } }$ by $w _ { t }$ where $t { \in } [ 1 . . m ]$ . That is:

$$
\begin{array}{l}\frac {\partial E P ^ {E} (\underline {{\theta}} , \bar {\theta})}{\partial w _ {t}} = \frac {1}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot (n - 1) \cdot n \cdot \left(\left[ - \frac {2 \cdot w _ {t}}{2 \cdot a _ {t}} + \right. \right.\\\left. \cdot \frac {W _ {t}}{2 \cdot a _ {t}} \right] \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \left(\frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {i}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} d \theta_ {j}\right) d \theta_ {i}\\+ \frac {2 \cdot w _ {t}}{4 \cdot a _ {t}} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \left(\int_ {\theta_ {i}} ^ {\bar {\theta}} \frac {(\bar {\theta} - \theta_ {j}) ^ {n - 2}}{\theta_ {j}} d \theta_ {j}\right) d \theta_ {i}\left. \right)\end{array}
$$

By comparing the differentiation of $\mathrm { E P ^ { E } }$ to zero the maximum value of $w _ { t }$ is identifed.

$$
\begin{array}{l} \Rightarrow w _ {t} = W _ {t} \\ \cdot \frac {\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {i}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}}{2 \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \cdot \int_ {\theta_ {i}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i} - \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {t}} ^ {\bar {\theta}} \frac {(\bar {\theta} - \theta_ {j}) ^ {n - 2}}{\theta_ {j}} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}} \end{array}\tag{□}
$$

In conclusion for both auction protocols we consider (the first-score sealed bid auction and the English auction), we provide the auctioneer agent with a function that calculates the optimal weights to be announced in the scoring function, given the number of participating sellers (bidders) and the range of sellers’ cost parameters $[ \underline { { \theta } } , \bar { \theta } ]$ in the model we consider. Given all the parameters values the auctioneer can immediately find the optimal values by calculating the equation or by using a mathematical tool such as Mapel or Matlab.

By observing the behavior of the values of the optimal weights as a function of different parameters, one can observe that even though the formulas of the optimal weights in both cases, the first-score sealed bid auction and the English auction, seem different, they behave in the same manner. This observation motivated us to analyze the relation between the results of the two protocols. By applying this result on our on-going example the optimal weights for the multi-attribute English auction are:

$$
\langle w _ {1} = 2. 0 4 1 9, w _ {2} = 3. 4 0 3 2 \rangle
$$

which are exactly the optimal weights that where calculated for the first-score sealed-bid auction based on Theorem 1.

And indeed, in the following section we provide the most interesting result of our research in the area of multi-attribute auctions. We prove that the expected payoff for the auctioneer in the first score sealed bid auction $\mathrm { E P ^ { 1 } }$ is equal (with the difference of a minor constant) to the expected payoff of the multi-attribute English auction $\bar { \mathrm { E P } } ^ { \mathrm { E } }$ . This means that the equivalence theorem holds in our model: the buyer will be indifferent to using both auction protocols, whenever $D$ is small enough, and the assumptions of our model hold. That is, this result is actually an extension of the payoff equivalence of the single attribute case [18].

Che [8] proved that the first-score sealed-bid auction is equal to the second-score sealed-bid auction (which is strategically equal to the English protocol) for the case the auctioneer announces its true utility function as the scoring rule. However, we prove that for each given scoring rule both protocols yield the same expected payoff for the auctioneer (the buyer). In addition we build an optimal scoring function that keeps the form of the real utility function which is an SAW function. Che, on the other hand, discussed the optimal scoring function for the general case of a utility function and considered the optimal scoring function to be the real utility function plus a certain increment.

## 6. Payoff equivalence theory

In Section 6.1 the second-score sealed-bid auction is defined and analyzed. The analysis results show that, similar to the case of single attribute, the second-score sealed-bid and the multi-attribute English are equivalent with the difference of a constant D, in the sense that the outcomes of both protocols are equal with the difference of a constant D (the minimal increment). Moreover, in Section 6.2 we prove that the expected payoff from the firstscore sealed-bid and the multi-attribute English auctions are equal with the difference of the constant D. In other words, we provide an extension of the equivalence theory of the single attribute to the case of the multi-attribute items. As a consequence of the above results, one can observe that the minimal bid increment is one of the manipulating factors that the auctioneer can adjust to yield the optimal results. A discussion on this optimal bid increment for the multi-attribute case is provided in Section 6.3.

## 6.1. Equivalence of the second-score sealed-bid and the multi-attribute English auctions

The second-score auction is a variation of the second price auction which begins with the auctioneer announcing a scoring function, then the bidders send sealed bids (including the quality values and the price). The winner is the bidder that achieves the highest score regarding the scoring function, and he is committed to offer a bid that achieves a score that is equal to the second highest scored bid. The dominant bidding strategy is provided next:

Lemma 6. Given the model described in Section 3, the dominant bidding strategy in a second-score sealed-bid auction is to bid the optimal qualities as described in Lemma 1 and to set the price such that yields the bidder zero utility. That is, seller $s _ { i } { } ^ { \ ' } \mathbf { S }$ bid is:

$$
\left\{p = \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{4 \cdot a _ {t} \cdot \theta_ {i}}; \quad q _ {t} = \left(\frac {w _ {t}}{2 \cdot a _ {t} \theta_ {i}}\right) ^ {2}, \quad \text { where }, t \in [ 1.. m ] \right\}\tag{21}
$$

Proof. We need to prove only that the offered price will achieve the dominant strategy since the optimality of the quality values was proved in Lemma 1 independently of the auction protocol. In order to prove that the strategy for choosing the price in the second-score is dominant, suppose that the agent seller does not use the proposed strategy. Then we will attempt to derive a contradiction. That is, supposes the seller agent $s _ { i }$ chooses a price using one of the following complementary strategies:

(1) Choosing a price that yields (with regard to the optimal qualities) the seller a utility value less than zero. (2) Choosing a price that yields (with regard to the optimal qualities) the seller a utility value greater than zero.

Consider the first option where seller $s _ { i }$ offers a price that yields him a negative utility, Since we assume the sellers agents are rational (Section 3), a contradiction is derived. On the other hand, when considering the second option of choosing the price in a way that yields a positive (greater than zero) utility for the seller, then the seller offers a higher price. Since we consider a reverse auction it means that the auction decreases its probability to win with regard to the price suggested in the lemma. However, since the winner’s determination is not included in the winning bid criteria, the seller decreases his probability to win. Nonetheless, the bid he will have to provide in case he wins remains the same as in the case he proposes the price in the lemma. In conclusion, offering the price that yields a zero utility for the seller is better for the seller than choosing the price according to option 2.

The price satisfying the condition of yielding a zero utility using the optimal qualities is:

$$
U _ {\mathrm{s}} \left(p, q _ {1} ^ {*},..., q _ {m} ^ {*}, \theta_ {i}\right) = p - \theta_ {i} \cdot \left(\sum_ {i = 0} ^ {m} a _ {i} \cdot \left(\frac {w _ {i}}{2 \cdot a _ {i} \theta_ {i}}\right) ^ {2}\right) = 0 \Rightarrow p = \left(\frac {w _ {i} ^ {2}}{4 \cdot a _ {i} \theta_ {i}}\right)
$$

Lemma 7. Given the model described in Section 3 and given that the highest score bidder is $s _ { i }$ and the second highest score is $s _ { j } ,$ the winning bid in a second-score sealed-bid auction is:

$$
\left\{p = \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right); \quad q _ {t} = \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) ^ {2}, \quad \text { where }, t \in [ 1.. m ] \right\}\tag{22}
$$

Proof. The quality attributes’ values are determined based on Eq. (13). Regarding the price, in Lemma 6 we proved that the dominant strategy in the second-score auction is to bid the optimal qualities and to choose the price that achieves a zero utility for the seller (see Eq. (16)). That is seller $s _ { j }$ will propose

$$
\left\{\left(\frac {w _ {t} ^ {2}}{4 \cdot a _ {t} \theta_ {j}}\right), \quad q _ {t} = \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {j}}\right) ^ {2}, \quad \text { where }, t \in [ 1.. m ] \right\}
$$

According to the second-score auction the seller that achieves the highest score (defined by the lowest cost parameter) $s _ { i }$ will have to offer a bid that achieves a score equal to the score achieved by the bid of seller $s _ { j } .$ . Since the qualities being offered are determined by Eq. (13), the value of the price will have to be calculated as follows:

$$
- p + \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \theta_ {i}}\right) = - \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{4 \cdot a _ {i} \theta_ {j}}\right) + \sum_ {i = 1} ^ {m} \left(\frac {w _ {i} ^ {2}}{2 \cdot a _ {i} \theta_ {j}}\right)
$$

$$
p = \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right)
$$

Corollary 1. The winning bid in a second-score sealed-bid is equal to the winning bid in a multi-attribute English auction with the difference of a constant D (bid increment).

## Proof. Can be derived directly from Lemmas 4 and 7.

Corollary 1 actually proves that both auction protocols, the second-score and the multi-attribute are equivalent from the outcome point of view. This result extends the equivalence that exists between the second-price and the English auctions in the single-attribute case. Moreover, we can derive from this result that the expected payoff from the second-score and the multi-attribute English are equal and consequently the optimal weights to be announced by the auctioneer in both protocols are equal.

Table 1  
A comparison of the expected payoff in the first-score and the English auctions of the on-going example

<table><tr><td></td><td> $EP^1$ </td><td> $EP^E$ </td><td> $EP^1 - EP^E$ </td></tr><tr><td> $S_1$ </td><td>11.7118</td><td>12.2118</td><td>0.5</td></tr><tr><td> $S_2$ </td><td>14.7474</td><td>15.2474</td><td>0.5</td></tr><tr><td> $S_3$ </td><td>15.0186</td><td>15.5186</td><td>0.5</td></tr></table>

## 6.2. Equivalence payoff between the first-score sealed-bid and the multi-attribute English auctions

By observing the expected payoff of the first-score sealed-bid and the multi-attribute English auctions in our ongoing example (Table 1), one may notice that they are equal with the difference of the bid increment which was set to 0.5. This observation inspired us to prove the following theorem about the equivalence between the first-score and the multi-attribute auctions.

Theorem 3. For each set of parameters for the model described in Section 3, $\begin{array} { r } { i f ~ D { \le } \frac { 1 } { 4 } \cdot \left( \frac { 1 } { \theta _ { i } } - \frac { 1 } { \theta _ { j } } \right) \cdot \sum _ { t = 1 } ^ { m } \frac { w _ { t } ^ { 2 } } { a _ { t } } , } \end{array}$ , then the difference between $E P ^ { E }$ and $E P ^ { I }$ is equal to $D .$

Proof. Recall that

$$
\begin{array}{l} \mathrm{EP} ^ {1} (\underline {{\theta}}, \bar {\theta}) = \frac {- n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \left(\sum_ {i = 1} ^ {m} \frac {w _ {i} ^ {2}}{4 \cdot a _ {i}}\right) \cdot \left(\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t + \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {n - 1}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) + \frac {n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \\ \cdot \left(\sum_ {i = 1} ^ {m} \frac {W _ {i} \cdot w _ {i}}{2 \cdot a _ {i}}\right) \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {n - 1}}{t} \mathrm{d} t. \end{array}
$$

and

$$
\begin{array}{l}\mathrm{EP} ^ {\mathrm{E}} (\underline {{\theta}}, \bar {\theta}) = \frac {1}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot n \cdot (n - 1) \cdot \left(\sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{4 \cdot a _ {t}}\right) \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta_ {i}} ^ {\bar {\theta}} \frac {(\bar {\theta} - \theta_ {j}) ^ {n - 2}}{\theta_ {j}} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i} + \left(- \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{2 \cdot a _ {t}}\right) \right. \right.\\\left. + \sum_ {t = 1} ^ {m} \left(\frac {W _ {t} \cdot w _ {t}}{2 \cdot a _ {t}}\right)\right) \cdot \int_ {\theta_ {i}} ^ {\bar {\theta}} \frac {1}{\theta_ {i}} \int_ {\underline {{\theta}}} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i} + D \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {\theta i} ^ {\bar {\theta}} (\bar {\theta} - \theta_ {j}) ^ {n - 2} \mathrm{d} \theta_ {j} \mathrm{d} \theta_ {i}\left. \right)\end{array}
$$

From Proposition 1 (in the Appendix)

If

$$
A := \int_ {\bar {\theta}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {(n - 1)}}{t} \mathrm{d} t,
$$

and

$$
B := (n - 1) \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2) _ {\mathrm{d} z}}}{t} \mathrm{d} t,
$$

then $A = B ,$

Denote G to be:

$$
G := n \cdot (n - 1) \cdot \frac {\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z \mathrm{d} t}{(\bar {\theta} - \underline {{\theta}}) ^ {n}}
$$

So by substituting the expressions of $A , B ,$ , and G in $\mathrm { E P ^ { E } }$ and $\mathrm { E P ^ { 1 } }$ we attain:

$$
\mathrm{EP} ^ {1} = \frac {\left(\sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{4 \cdot a _ {t}}\right) \cdot \left(- A - \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 1)}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) + \sum_ {t = 1} ^ {m} \left(\frac {W _ {t} \cdot w _ {t}}{2 \cdot a _ {t}}\right) \cdot A\right) \cdot n}{(\underline {{\theta}} - \bar {\theta}) ^ {n}}
$$

and

$$
\mathrm{EP} ^ {\mathrm{E}} = \frac {\left(\sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{a _ {t}}\right) \cdot \left(- \frac {B}{2} + \frac {(n - 1)}{4} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z} \mathrm{d} z \mathrm{d} t\right) + \sum_ {t = 1} ^ {m} \left(\frac {W _ {t} \cdot w _ {t}}{2 \cdot a _ {t}}\right) \cdot B\right) \cdot n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} + D \cdot G
$$

We would like to show that ${ \mathrm { E P } } ^ { { \mathrm { E } } } { = } { \mathrm { E P } } ^ { 1 } { + } D$ . From Proposition 2 (Appendix), G=1. Thus, it is sufficient to show that $\mathrm { E P } ^ { \mathrm { E } } - D { = } \mathrm { E P } ^ { 1 }$

Since we found that $A = B .$ , we only have to show that:

$$
\begin{array}{l} \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{4 \cdot a _ {t}}\right) \cdot \left(- A - \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 1)}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) = \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{a _ {t}}\right) \\ \cdot \left(- \frac {B}{2} + \frac {(n - 1)}{4} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z} \mathrm{d} z \mathrm{d} t\right) \end{array}
$$

By dividing both sides of the equation by

$$
\sum_ {t = 1} ^ {m} \left(\frac {w _ {t ^ {2}}}{a _ {t}}\right)
$$

We only have to show that

$$
\frac {1}{4} \left(- A - \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 1)}}{z ^ {2}} \mathrm{d} z \mathrm{d} t\right) = \left(- \frac {B}{2} + \frac {(n - 1)}{4} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z} \mathrm{d} z \mathrm{d} t\right)
$$

Substituting B with A and changing sides we only have to prove that

$$
\begin{array}{r l} \frac {1}{4} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 1)}}{z ^ {2}} \mathrm{d} z \mathrm{d} t + \frac {(n - 1)}{4} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z} \mathrm{d} z \mathrm{d} t & = \frac {A}{4} \Rightarrow \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 1)}}{z ^ {2}} \mathrm{d} z \mathrm{d} t + (n - 1) \\ & \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z} \mathrm{d} z \mathrm{d} t = A \end{array}
$$

This can also be written as

$$
\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} d z d t = A
$$

The left side of the equation is the exact expression denoted by F in Proposition $3 \ : ( \mathrm { A p p e n d i x } )$ and there we prove that $F { = } A$ . Thus, both sides of the equation are actually equal, so the original values of $\mathrm { E P ^ { 1 } }$ and $\mathrm { E P } ^ { \mathrm { E } } - D$ are also equal. 5

In Theorem 3 we prove that the expected payoff in the first-score sealed-bid protocol auction and the English auction are equal with the difference of the constant D. Accordingly, the optimal scoring rule is also equal in these two auction protocols since the optimal scoring rule is derived by solving a maximization problem of the expected payoff with regards to the announced weights $w _ { i } .$

At the end of an English auction the bidders and the auctioneer have information about the bidders cost parameters, which is based on the order in which the bidders quit the auction. That is, the bidders and the auctioneer assume that the first bidder that quit is the weakest bidder and that the winner is actually the strongest bidder. However in a first-score sealed bid auction the bidders cannot reveal any information about the other participants except to the winner since the bids are not a part of public information. Only the auctioneer in the firstscore sealed-bid auction can learn about the bidders’ private information. As a consequence, given the equivalence between the first-score and the English protocols for multi-attribute items, strong bidders are motivated to participate in an English auction in order to reveal their power and to deter the weaker bidders from participating in other auctions in the future, in which they will take part. Another observation is that weak sellers will be more comfortable participating in sealed auctions in order to keep their private information hidden. Therefore, it seems that from the auctioneer’s (buyer) point of view using an English protocol encourages strong bidders’ participation and therefore it may increase its payoff. There are more aspects which should be discussed and perhaps a more indepth research is required to learn about the long-term influence of participation in a certain auction. In the following subsection we discuss the method for determining the value of the minimal increment allowed D.

## 6.3. Determining the Optimal Bid Increment

From the above subsections the importance of D’s value is realized as it directly influences the auctioneer’s expected payoff. In Theorem 3 we prove that the difference of the first-score sealed-bid and the multi-attribute English auctions’ expected payoff is equal to D, which is the minimal bid increment allowed in the English auction. That is, the greater the bid increment set by the auctioneer in the multi-attribute English auction, the greater the expected payoff. However, the assumptions of Theorem 3 bound D by:

$$
0 \leq D \leq \frac {1}{4} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{\theta_ {j}}\right) \cdot \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{a _ {t}}.\tag{23}
$$

Consequently, the optimal value of D should have been the upper bound.

Notice that the upper limit set for the minimal increment is to allow the best bidder (with the lowest cost parameter) to win. Otherwise, the determination of the winner depends on the bidding order which is an undesired feature, since it causes the bidders to speculate on the bids of the other bidders in order to bid a winning bid, and hence making the protocol non-incentive compatible.

The above discussion provides the optimal value of D where the cost parameters of the best sellers are known. Since this assumption is unrealistic in the real world (the auctioneer knowing the cost parameters of the best bidders at the beginning of the auction) this result does not provide the auctioneer with a tool to calculate the optimal value of the bid increment. Further research should be conducted on this open question.

Our conclusion with regards to the optimal bid increment, which is recommended to be higher than zero, contradicts the traditional assumption that the continuous bid (i.e., allowing the minimal unit possible, theoretically it is some small e) is optimal for the auctioneer in the single-attribute English auction [25].

Next we explain the correlation of concepts used in the single and the multi-attribute auctions. In the single attribute auction each bidder is characterized by its <sup>b</sup>valuation<sup>Q</sup> which is the bidder’s monetary value of the item. According to the classic auction theory a bidder will never propose a price higher than its valuation in an auction (or a lower price in a reverse auction). The corresponding concept for the multi-attribute case is the bidder’s MaxScore(s ) (defined in Eq. (17)). The MaxScore is actually the maximum score for any bid the seller will offer that yields a non-negative utility value for the seller. In other words in order to achieve a higher score than that the agent will propose an offer that yields him a negative utility. But since the agents are assumed to be rational, such an action is unfeasible. Consequently, the maximum score is the bidding limit similar to the way the valuation is the bidder’s limit in the single attribute case.

![](/api/attachments/4FAW8XUH/fulltext/images/51ab836962a07a05ba77804cb68482a88ebae6ced9d18154e3f7f14ae1ea002c.jpg)  
Fig. 4. The histogram of h in the range (0.1, 1) where the number of attributes is set to 2, w<sub>1</sub> = 2, w<sub>2</sub> = 4, a<sub>1</sub> = 1, $\scriptstyle a _ { 2 } = 2 .$

Looking more closely at the multi-attribute English auction defined in this paper, to understand the contradiction with the single attribute auction, notice that in our protocol bidders are allowed to submit equal bids.<sup>3</sup> However according to the traditional single-attribute English auction each proposed bid should be higher than the previously placed bid and equal bids are therefore unacceptable. As a consequence in the single traditional English auction the winning bid depends on the bidding order and the auctioneer cannot control the auction in the sense that it cannot ensure the winning of the highest bidder. In contrast, in the multi-attribute auction where equal bids are allowed, by defining the increment D to be lower than the upper bound specified in Eq. (23), the auctioneer ensures the winning of the highest bidder. If we would have allowed equal bids in the traditional English auction then we would have been able to calculate (using a method similar to the one presented in this paper) the optimal discrete value which will ensure that the highest bidder wins and pays his valuation.

In addition, in the single attribute case it is assumed that the continuous bid (very small increment) is the optimal strategy given that the valuations of the bidders are distributed uniformly [25]. However this result does not apply to the multi-attribute settings of this paper. Even though the bidders’ cost parameters are uniformly distributed, since the bidders’ MaxScores are not uniformly distributed, the results of the single case cannot be easily applied to the multi-attribute case. To understand the reason that the MaxScore is not uniformly distributed recall from Eq. (17) that MaxScore $\begin{array} { r } { \left( s _ { i } ( \theta ) \right) = \sum _ { i = 1 } ^ { m } \left( \frac { w _ { i } ^ { 2 } } { 4 \cdot a _ { i } \theta } \right) } \end{array}$ . In Fig. 4 we illustrate the histogram of h which is uniformly distributed in the range (0.1, 1) and the histogram of the corresponding MaxScores is presented in Fig.

## 5. As we can see there are many sellers with low MaxScores and very few sellers with high MaxScores.

Alternatively, where only the distribution of the sellers’ cost parameters is available, the optimal bid may be estimated using the distributions of the cost the parameters of the two highest sellers’ cost parameters and the upper bound defined in Eq. (23). We leave this task for future work.

However we are not the first to demonstrate that a discrete bid increment is better than the continuous one in a given setting. There are several cases where the discrete bid increment is better [2,3]. For instance in the Yankee auction considered in Bapna et al. [3] multiple identical units of an item are sold to multiple buyers using an ascending and open auction mechanism. Similar to our work they analyzed the auction from the auctioneer’s point of view and attempted to identify the control factors that the auctioneer can manipulate in order to maximize its expected payoff. In the Yankee auction equal bids are allowed since there are multiple items. Bapna et al. [3] obtained the optimal bid increment as a function of the number of items $N ,$ and the uniform distribution range of the highest N bidders. They concluded that the optimal bid increment decreases as the number of items increases. That is, for a small number of items for sale a discrete bid increment is better than the continuous one. However this result cannot be applied to our case since again they assume a uniform distribution of the bidders’ valuations.

![](/api/attachments/4FAW8XUH/fulltext/images/5b5a35857b956c5a4b3a35da132eb1c8e2b7b8cac93868ae110c9a9eaf1d413d.jpg)  
Fig. 5. The histogram of MaxScore where h is uniformly distributed in the range (0.1, 1) where the number of attributes is set to 2, $w _ { 1 } = 2 ,$ $w _ { 2 } = 4 , a _ { 1 } = 1 , a _ { 2 } = 2$

Another interesting work conducted by Bapna et al. [2] considers the multi-unit English auction. They faced the problem of auction design without making any distributional assumption regarding the bidders’ valuations. They concluded that the auctioneer can control the bounds of its payoff by manipulating the bid increment, since the range between the upper and the lower bounds of the auctioneer’s payoff is the number of items for sale, multiplied by the bid increment. So, for the case where there is only one item for sale the range will be equal to the bid increment. Thus, as the auctioneer is risk seeking, it will increase this value. In contrast, as the auctioneer’s risk averseness increases the bid increment decreases.

## 7. Conclusion and future work

In this paper, we consider multi-attribute auction protocols in which the auctioned item is characterized by several negotiable dimensions. Specifically, we analyze the first-score sealed-bid, the second-score sealed-bid and a variation of a multi-attribute English protocol, termed sequential full information revelation considering the perspectives of both the bidders and the auctioneer. For each protocol, we provide the bidder agent with the optimal bidding strategy, and the auctioneer with the optimal auction design. The optimal auction design in our context involves composing the optimal scoring function that will yield the optimal payoff to the auctioneer. We prove and demonstrate the result, that under the assumptions of the model, the three protocols yield identical results with the exception of a small constant, D.

Moreover, we show that as the number of bidders increases the expected pay-off for the auctioneer increases. Accordingly the auctioneer is motivated to encourage the bidder to participate in the auction. In addition, as the number of bidders increases the need for modification of the real preferences to be announced decreases. That is, if the number of bidders is large enough, the auctioneer can announce its true preferences (i.e. its actual utility function) and still expect the optimal payoff.

In future work we intend to identify more properties regarding the bid increment in multi-attribute auctions. Furthermore it will be interesting to analyze the effect of multi-attribute bidding strategy in more complex auction protocols such as multi-sourcing multi-attribute (allowing more than one winner) [5], combinatorial, double and simultaneous-multiple auctions. Currently, all these strategies mainly deal with the case of a single attribute. However as we have outlined in this paper there is an increasing need to handle multi-attribute contracts.

## Appendix A

Lemma 4. Denote by $s _ { i }$ the seller with the lowest value of h, and by $s _ { j }$ the seller with the second lowest $\theta .$ In the sequential full-information revelation English auction protocol, seller $s _ { i }$ is the winner of the auction whenever $\begin{array} { r } { D \le \frac { 1 } { 4 } \cdot \left( \frac { 1 } { \theta _ { i } } - \overset { \cdot } { \theta _ { j } } \right) \cdot \sum _ { t = 1 } ^ { m } \frac { w _ { t ^ { 2 } } } { a _ { t } } \mathrm { ~ } i s . } \end{array}$

$$
\left\{p = \sum_ {t = 1} ^ {m} \frac {w _ {t ^ {2}}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right) - D; q _ {t} = \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) ^ {2},   \text { where, } t \in [ 1.. m ] \right\}
$$

Proof. Suppose that $s _ { i }$ is the seller with the lowest cost parameter $\theta _ { i } .$ . Suppose on the contrary that another seller $s _ { j }$ with a higher cost parameter $\theta _ { j }$ wins. Suppose that seller $s _ { j }$ offers a bid $( p ( \theta _ { j } ) , q _ { 1 } ( \theta _ { j } )$ $q _ { m } ( \theta _ { j } ) )$ in a given step of the auction. If seller ${ \bf { \sigma } } _ { { \bf { { i } } } }$ wants to improve this bid its new bid $( p ( \theta _ { i } ) , q _ { 1 } ( \theta _ { i } ) .$ $q _ { m } ( \theta _ { i } ) )$ must satisfy:

$$
\begin{array}{l} S (p (\theta_ {i}), q _ {1} (\theta_ {i}),..., q _ {m} (\theta_ {i})) \\ = S \big (p (\theta_ {j}), q _ {1} (\theta_ {j}),..., q _ {m} (\theta_ {j}) \big) + D. \end{array}
$$

By using the announced scoring rule we obtain:

$$
\begin{array}{l} - p (\theta_ {i}) + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \sqrt {q} _ {t} (\theta_ {i})\right) \\ = - p (\theta_ {j}) + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \sqrt {q} _ {t} (\theta_ {j})\right) + D \end{array}
$$

Substituting the values of the optimal offered qualities:

$$
\begin{array}{l} \left\{q _ {1} (\theta_ {i}),..., q _ {m} (\theta_ {i}), q _ {1} (\theta_ {j}),..., q _ {m} (\theta_ {j}) \right\} \\ \text { according   to   Lemma   3   results   in: } \\ - p (\theta_ {i}) + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) \\ = - p (\theta_ {j}) + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {j}}\right) + D \end{array}
$$

The best bid that seller $s _ { j }$ can offer is a bid which will yield for $s _ { j }$ a utility equal to zero:

$$
\begin{array}{l} p \big (\theta_ {j} \big) - \theta_ {j} \cdot \sum_ {t = 1} ^ {m} \big (a _ {t} \cdot q _ {t} \big (\theta_ {j} \big) \big) = 0 \\ \Rightarrow \\ p \big (\theta_ {j} \big) - \theta_ {j} \cdot \sum_ {t = 0} ^ {m} \left(a _ {t} \cdot \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {j}}\right) ^ {2}\right) = 0 \\ \Rightarrow \\ p \big (\theta_ {j} \big) = \frac {1}{4 \cdot \theta_ {j}} \cdot \sum_ {t = 1} ^ {m} \left(\frac {w _ {t ^ {2}}}{a _ {t}}\right) \end{array}\tag{1}
$$

This value of the price is the best price that seller $s _ { j }$ can offer without a loss. We will term it $p ^ { * } ( \theta _ { j } )$ . That is, by bidding a lowest price seller $s _ { j }$ loses. So assuming that seller $s _ { j }$ offers its best bid including the lowest price then it can bid $p ^ { * } ( \theta _ { j } )$ . We will see if seller $s _ { i }$ can compete with him. By substituting $p ( \theta _ { j } )$ with $p ^ { * } ( \theta _ { j } )$ we attain:

$$
\begin{array}{l} - p \left(\theta_ {i}\right) + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) = - \frac {1}{4 \cdot \theta_ {j}} \cdot \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{a _ {t}} \\ + \sum_ {t = 1} ^ {m} \left(w _ {t} \cdot \frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {j}}\right) + D \Rightarrow p \left(\theta_ {i}\right) \\ = \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right) \cdot \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{2 \cdot a _ {t}}\right) - D \end{array} \tag {2}\tag{2}
$$

This means that by offering the price as specified in Eq. (2) seller $s _ { i }$ beats seller $s _ { j }$ . However, this price is valid and possible from seller $s _ { i } { } ^ { \ ' } \mathbf { S }$ point of view only if it fulfills the condition that this price is higher than or equal to the minimum price that seller $s _ { i }$ can allow itself to offer similar to Eq. (1).

$$
\begin{array}{l} \text {MinPrices} _ {i} = \min p (\theta_ {i}) = \frac {1}{4 \cdot \theta_ {j}} \cdot \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{a _ {t}}\right) \\ \qquad \leq \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right) \cdot \sum_ {t = 1} ^ {m} \left(\frac {w _ {t} ^ {2}}{2 \cdot a _ {t}}\right) - D \\ \qquad \Rightarrow D \leq \frac {1}{4} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{\theta_ {j}}\right) \cdot \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{a _ {t}} \end{array}
$$

This condition actually defines the higher bound of the incremental value of $\mathbf { \delta } _ { D _ { \delta } }$ in which the seller with the lowest cost parameter can win. Otherwise, the determination of the winner depends on the bidding order which is an undesired feature, since it causes the bidders to speculate on the bids of the other bidders in order to bid a winning bid.

Accordingly the winning bid of the winning seller $s _ { i } ,$ based on Lemma 3 and Eq. (25), is:

$$
\left\{p = \sum_ {t = 1} ^ {m} \frac {w _ {t} ^ {2}}{2 \cdot a _ {t}} \cdot \left(\frac {1}{\theta_ {i}} - \frac {1}{2 \cdot \theta_ {j}}\right) - D; q _ {t} = \left(\frac {w _ {t}}{2 \cdot a _ {t} \cdot \theta_ {i}}\right) ^ {2} \text {   where,   } t \in [ 1.. m ] \right\}
$$

Next we prove three auxiliary propositions (for the proof of Theorem 3).

Proposition 1.

$$
\begin{array}{l} A = \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {(n - 1)}}{t} \mathrm{d}, B = (n - 1) \\ \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {\int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z}{t} \mathrm{d} t \Rightarrow A = B \end{array}
$$

Proof. Consider the internal integral of B:

$$
\int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z
$$

By substitution of:

$$
\begin{array}{l} x = \bar {\theta} - z \\ \mathrm{d} x = - \mathrm{d} z \\ \int (\bar {\theta} - z) ^ {(n - 2)} = - \int (x) ^ {(n - 2)} \end{array}
$$

However, the integral on the right side of the equation can be easily solved and the solution is:

$$
- \int x ^ {(n - 2)} \mathrm{d} x = - \frac {x ^ {(n - 1)}}{(n - 1)}
$$

$$
\begin{array}{l} x = \bar {\theta} - z \Rightarrow = - \frac {x ^ {(n - 1)}}{(n - 1)} = - \frac {(\bar {\theta} - z) ^ {(n - 1)}}{(n - 1)} \\ \Rightarrow \int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z = - \frac {(\bar {\theta} - z) ^ {(n - 1)}}{(n - 1)} \Bigg | \\ (z = t.. \bar {\theta}) = - \frac {(\bar {\theta} - \bar {\theta}) ^ {(n - 1)}}{(n - 1)} + \frac {(\bar {\theta} - t) ^ {(n - 1)}}{(n - 1)} \\ = \frac {(\bar {\theta} - t) ^ {(n - 1)}}{(n - 1)} \Rightarrow \int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z \\ = \frac {(\bar {\theta} - t) ^ {(n - 1)}}{(n - 1)} \Rightarrow B = (n - 1) \\ \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {(n - 1)}}{(n - 1)} \mathrm{d} t = \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \frac {(\bar {\theta} - t) ^ {(n - 1)}}{t} \mathrm{d} t \\ = A \end{array}
$$

Proposition 2. Denote G to be:

$$
G = n \cdot (n - 1) \cdot \frac {\int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z \mathrm{d} t}{(\bar {\theta} - \underline {{\theta}}) ^ {n}}
$$

Then G=1.

Proof. First we will consider the internal integral of G which is: $\begin{array} { r } { \int _ { t } ^ { \bar { \theta } } \big ( \bar { \theta } - z \big ) ^ { ( n - 2 ) } } \end{array}$ dz. According to Proposition 1 this equals:

$$
\int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 2)} \mathrm{d} z = \frac {(\bar {\theta} - t) ^ {(n - 1)}}{(n - 1)}
$$

$$
\begin{array}{r l} G & = \frac {n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \int_ {\underline {{\theta}}} ^ {\bar {\theta}} (\bar {\theta} - t) ^ {(n - 1)} \mathrm{d} t \\ & = \frac {n}{(\bar {\theta} - \underline {{\theta}}) ^ {n}} \cdot \frac {(\bar {\theta} - \underline {{\theta}}) ^ {n}}{n} = 1 \end{array}
$$

By substituting the solution of the integral in $G$ we receive: So we proved that G=1. 5

Proposition 3. Denote F to be:

$$
F = \int_ {\underline {{\theta}}} ^ {\bar {\theta}} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} d z d t
$$

Then $F { = } A .$

Proof. Consider first the internal integral of F which can be written as a sum of two sub-integrals:

$$
\begin{array}{l} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} \mathrm{d} z \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2)}{z} \mathrm{d} z \\ + \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot \bar {\theta}}{z ^ {2}} \mathrm{d} z \end{array}
$$

First we will solve the second sub-integral by integration of parts: $\begin{array} { r } { \int \textbf {  { u } } \cdot \textbf {  { d } } \nu = \ b { u } \cdot \textbf {  { v } } - \int \mathrm { ~ d } \nu \ \cdot \textbf {  { u } } . } \end{array}$ Denote u and v to be:

$$
\begin{array}{r l} u = (\bar {\theta} - z) ^ {(n - 2)}, & \mathrm{d} v = \frac {1}{(z) ^ {2}} \Rightarrow \mathrm{d} u = - (n - 2) \\ \cdot (\bar {\theta} - z) ^ {(n - 3)}, & v = - \frac {1}{z} \end{array}
$$

By using the above rule we obtain:

$$
\begin{array}{r l} \int u \cdot \mathrm{d} v & = u \cdot v - \int \mathrm{d} u \cdot v \Rightarrow \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)}}{z ^ {2}} \mathrm{d} z \\ & = (\bar {\theta} - z) ^ {(n - 2)} \cdot \left(- \frac {1}{z}\right) \\ & - \int_ {t} ^ {\bar {\theta}} \frac {(n - 2) \cdot (\bar {\theta} - z) ^ {(n - 3)}}{z} \mathrm{d} z \end{array}
$$

Now we will substitute the second internal integral of F with the above equation:

$$
\begin{array}{l} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} \mathrm{d} z \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2)}{z} \mathrm{d} z \end{array}
$$

$$
\begin{array}{l} + \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot \bar {\theta}}{z ^ {2}} \mathrm{d} z \\ \Rightarrow \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} \mathrm{d} z \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2)}{z} \mathrm{d} z + \bar {\theta} \\ \cdot \left((\bar {\theta} - z) ^ {(n - 2)} \cdot (- \frac {1}{z}) \right. \\ - \int_ {t} ^ {\bar {\theta}} \frac {(n - 2) \cdot (\bar {\theta} - z) ^ {(n - 3)}}{z} \mathrm{d} z) \end{array}
$$

and

$$
\begin{array}{l} \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} \mathrm{d} z = \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2)}{z} \mathrm{d} z + \bar {\theta} \\ \cdot \left(\left[ (\bar {\theta} - z) ^ {(n - 2)} \cdot \left(- \frac {1}{z}\right) \right] _ {z = t.. \bar {\theta}} \right. \\ \left. - \int_ {t} ^ {\bar {\theta}} \frac {(n - 2) \cdot (\bar {\theta} - z) ^ {(n - 3)}}{z} \mathrm{d} z\right) \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2)}{z} \mathrm{d} z - \bar {\theta} \\ \cdot \int_ {t} ^ {\bar {\theta}} \frac {(n - 2) (\bar {\theta} - z) ^ {(n - 3)}}{z} \mathrm{d} z + \bar {\theta} \\ \times \left[ (\bar {\theta} - z) ^ {(n - 2)} \cdot \left(- \frac {1}{z}\right) \right] _ {z = t.. \bar {\theta}} \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 3)} \cdot [ (\bar {\theta} - z) \cdot (n - 2) - \bar {\theta} \cdot (n - 2) ]}{z} \\ \times \mathrm{d} z + \bar {\theta} \left[ (\bar {\theta} - z) ^ {(n - 2)} \cdot \left(- \frac {1}{z}\right) \right] _ {z = t.. \bar {\theta}} \\ = \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 3)} \cdot [ (- z) \cdot (n - 2) ]}{z} \mathrm{d} z + \bar {\theta} \\ \times \left[ (\bar {\theta} - z) ^ {(n - 2)} \cdot \left(- \frac {1}{z}\right) \right] _ {z = t.. \bar {\theta}} \end{array}
$$

$$
\begin{array}{l} = - (n - 2) \int_ {t} ^ {\bar {\theta}} (\bar {\theta} - z) ^ {(n - 3)} \mathrm{d} z + \bar {\theta} \left[ (\bar {\theta} - z) ^ {(n - 2)} \right. \\ \cdot \left(- \frac {1}{z}\right) \Bigg ] _ {z = t.. \bar {\theta}} \\ = - (n - 2) \cdot \frac {(\bar {\theta} - t) ^ {(n - 2)}}{(n - 2)} + \bar {\theta} \cdot (\bar {\theta} - t) ^ {(n - 2)} \cdot \left(\frac {1}{t}\right) \\ = (\bar {\theta} - t) ^ {(n - 2)} \cdot \left(- 1 + \frac {\bar {\theta}}{t}\right) \\ \int_ {t} ^ {\bar {\theta}} \frac {(\bar {\theta} - z) ^ {(n - 2)} \cdot (n - 2 + \frac {\bar {\theta}}{z})}{z} \mathrm{d} z \\ = (\bar {\theta} - t) ^ {(n - 2)} \cdot \left(- 1 + \frac {\bar {\theta}}{t}\right) = \frac {(\bar {\theta} - t) ^ {(n - 1)}}{t} \end{array}
$$

Until now we only considered the internal integral of F and we simplified it. Now we will add the main integral to this expression and terminate the proof by showing that F is equal to A. 5

## References

[1] M. Babaioff, N. Nisan, Concurrent auctions across the supply chain, EC 2001, Florida, USA, 2001, pp. 1 – 10.

[2] R. Bapna, A.A.G.P. Goes, Analysis and design of business-toconsumer online auctions, Management Science 49 (1) (2003) 85– 101.

[3] R. Bapna, P. Goes, A. Gupta, A. Karuga, Optimal design on the online auction channel: analytical, empirical and computational insights, Decision Science 33 (4) (2002) 557 – 577.

[4] M. Bichler, An experimental analysis of multi-attribute auction, Decision Support Systems 29 (2000) 249 – 268.

[5] M. Bichler, J. Kalagnanam, Configurable offers and winner determination in multi-attribute auctions, European Journal of Operational Research 160 (2) (2005) 380 – 394.

[6] F. Branco, The design of multidimensional auctions, Rand Journal of Economics 28 (1) (1997) 63 – 81.

[7] A. Byde, A comparison among bidding algorithms for multiple auctions, Proc. of the 4th Int. Workshop on Agent-Mediated Electronic Commerce, Bologna, Italy, 2002, pp. 613–620.

[8] Y.K. Che, Design competition through multidimensional auctions, RAND Journal of Economics 24 (1993) 668–680.

[9] C. Chen-Ritzo, T. Harrison, M. K. Wasnica, D. Thomas, Better, faster, cheaper: a multi-attribute supply chain auction mechanism, in: Penn State University ISBM report 10-2003, 2003.

[10] G.J. Collins, G. Demir, M. Gini, Bidtree ordering in ida\* combinatorial auction winner determination with side con-

straints, Proc. of the 4th Int. Workshop on Agent-Mediated Electronic Commerce, Bologna, Italy, 2002.

[11] P. Cramton, Ascending auctions, European Economic Review 42 (3–5) (1988) 745 – 756.

[12] E. David, R. Azoulay-Schwartz, S. Kraus, Protocols and strategies for automated multi-attributes auctions, Proc. of the 1st Conference on Autonomous Agents and Multi-Agent Systems, Bologna, Italy, 2002, pp. 77 – 85.

[13] E. David, R. Azoulay-Schwartz, S. Kraus, An english auction protocol for multi-attributes items, in: J. Padget, D. Parkes, N. Sadeh, O. Shehory, W. Walsh (Eds.), Agent Mediated Electronic Commerce: IV. Designing Mechanisms and Systems, vol. 2531, LNAI, 2002, pp. 52– 68.

[14] S.S. Fatima, M.J. Wooldrige, N.R. Jennings, The influence of information on negotiation equilibrium, Proc. 4th Int. Workshop on Agent-Mediated Electronic Commerce, Bologna, Italy, 2002, pp. 180 – 193.

[15] B. Hudson, T. Sandholm, Effectiveness of preference elicitation in combinatorial auctions, Proceedings of AMEC-IV LNCS, vol. 2531, 2002, pp. 180 – 193.

[16] F. Kelly, R. Steinberg, A combinatorial auction with multiple winners for universal service, Management Science 46 (4) (2000) 586– 596.

[17] P. Milgrom, An economist’s vision of the b-tob marketplace, An Executive White Paper October 2000.

[18] P. Milgrom, R. Weber, A theory of auction and competitive bidding, Econometria 50 (1982) 1089 – 1122.

[19] I. Miller, J. Freund, Probability and Statistics for Engineers, Prentice-Hall, Inc., 1985.

[20] N. Nisan, Bidding and allocation in combinatorial auctions, Proc. of the ACM Conference on Electronic Commerce (ACM-EC), Minneapolis, MN, 2000, pp. 1– 12.

[21] netfirms, http://www.netfirms.com/.

[22] D.C. Parkes, J. Kalagnanam, Iterative multi-attribute vickrey auctions, Management Science, 2004, (http://www.eecs. harvard.edu/econcs/pubs/map.pdf).

[23] P.S.A. Reitsma, P. Stone, J.A. Csirik, M.L. Littman, Self enforcing strategic demand reduction, Proc. 4th Int. Workshop on Agent-Mediated Electronic Commerce Bologna, Italy, 2002.

[24] J.G. Riley, W.F. Samuelson, Optimal auctions, American Economic Review 71 (1981) 381 – 392.

[25] M.H. Rothkopf, R. Harstad, On the role of discrete bid levels in oral auctions, European Journal of Operations Research 74 (1994) 572– 581.

[26] M.H. Rothkopf, R. Harstad, Modeling competitive bidding: a critical essay, Management Science 40 (3) (1994) 364 – 384.

[27] T. Sandholm, S. Suri, Improved algorithms for optimal winner determination in combinatorial auctions and generalizations, Proceedings of the Seventeenth National Conference on Artificial Intelligence and Twelfth Conference on Innovative Applications of Artificial Intelligence, 2003, pp. 90 – 97.

[28] Streamlinenet, http://www.streamlinenet.co.uk/.

[29] S. Strecker, S. Seifert, Electronic sourcing with multi-attribute auctions, Proceedings of the 37th Hawaii International Conferenceon System Science, 2004.

[30] P. Stone, R.E. Schapire, J.A. Csirik, L. Littman, D. McAllester, ATTac-2001: a learning autonomous bidding agent, Agent

mediated electronic commerce: IV. Designing mechanisms and systems of lecture notes in artificial intelligence, 2531, 2002, pp. 143–160.

[31] A.V. Sunderam, D.C. Parkes, Preference elicitation in proxied multiattribute auctions, Fourth ACM Conf. on Electronic Commerce (EC’03), 2003.

[32] Tac2004, http://www.sics.se/tac/page.php?id-3{#}custutil.

[33] J. E. Teich, H. Wallenius, J. Wallenius, O. R. Koppius, Emerging multiple issue e-auctions (invited review), European Jour nal of Operational Research 159 (1) 1–16.

[34] G. Vignaux, Multi-attribute decision problems, Technical Report (2004) Victorya University of Wellington New Zealand.

[35] N. Vulkan, N.R. Jennings, Efficient mechanisms for the supply of services in multi-agent environments, Decision Support Systems 28 (2000) 5 – 19.

[36] K. Yoon, C. Hwang, Multiple Attribute Decision-Making: An Introduction, Sage, Thousand Oaks, 1995.

Esther David received the BSc (hons.) degree in mathematics and computer science (1995), the MSc degree in computer science (1998) and the PhD degree in computer science (2003) from Bar Ilan University, Ramat-Gan, Israel. She is currently a Senior Re search Fellow of computer science in the School of Electronics and Computer Science, University of Southampton, Southampton, UK. Her current research interests include auctions and electronic commerce, multi-agents systems, game theory, and decentralized algorithm to control open agent-based systems.

Rina Azoulay-Schwartz is Lecturer of Computer Science at Jerusalem College of Technology (JCT), Ramat Gan branch. Rina Azoulay-Schwartz graduated summa cum laude from Bar Ilan University in 1995. In 1995, she began working under the direction of Professor Sarit Kraus at Bar Ilan University, and received the MSc degree in computer Science in 1997 and a PhD degree in Computer Science from Bar Ilan University in 2001. Area of research interests and teaching includes but not limited to the following: multi-agent systems, auctions, distributed learning, reinforcement learning, probabilistic models, algorithms, and game theory.

Sarit Kraus is a Professor of Computer Science at Bar-Ilan University and an adjunct Professor at the Institute for Advanced Computer Studies at the University of Maryland, College Park. She graduated from the Hebrew University of Jerusalem with a PhD in computer science in 1989. Subsequently, she spent 2 years at the University of Maryland, College Park, as a postdoctoral fellow, before joining Bar-Ilan University. She has worked extensively in the following areas: cooperation among agents, automated negotiation, information agents, large-scale systems, decision support systems, autonomous computing, optimization of complex systems, learning, auctions and electronic commerce, security of databases and agents.

Prof. Kraus was awarded the 1995 IJCAI Computers and Thought Award, an award given every 2 years at the major international Artificial Intelligence conference to an <sup>b</sup>outstanding young scientist.<sup>Q</sup> In 2001 she was awarded the IBM Faculty Partnership Award and in 2002 she was elected as AAAI Fellow. She has published over 160 papers in leading journals and major conferences and has received substantial grants from a variety of agencies and companies, including ISF, GIF, MAFAT, NSF, GM, IBM and NDS. She is an author of the book Strategic Negotiation in Multiagent Environments (2001) and a co-author of a book on Heterogeneous Active Agents (2000), both published in MIT Press.

In addition, she has served on numerous program committees of major conferences and workshops and she was a program co-chair of the ICMAS 2000 and a general co-chair of AAMAS 2005. She is a member of the board of directors of the International Foundation for Multi-agent Systems (IFMAS). She is an associate editor of the Annals of Mathematics and Artificial Intelligence Journal, and on the editorial board of the Artificial Intelligence Journal and the Journal of Autonomous Agents and Multi-Agent Systems. She has joint projects with researchers from the University of Maryland at College Park, Harvard University, SRI, and USC.
