---
otero_id: 874
otero_key: "UK8ZZACN"
title: "The Impact of Information Diffusion on Bidding Behavior in Secret Reserve Price Auctions"
authors: "Oliver Hinz; Martin Spann"
year: "2008"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0190"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## 6SR

![](/api/attachments/UK8ZZACN/fulltext/images/2aa684ad830a6b34d39945fe570b969bd53f438cbdfa30fe7d521cdb51ee2d87.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Impact of Information Diffusion on Bidding Behavior in Secret Reserve Price Auctions

Oliver Hinz, Martin Spann,

## To cite this article:

Oliver Hinz, Martin Spann, (2008) The Impact of Information Diffusion on Bidding Behavior in Secret Reserve Price Auctions. Information Systems Research 19(3):351-368. http://dx.doi.org/10.1287/isre.1080.0190

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2008, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/UK8ZZACN/fulltext/images/5f3cc8795c9a2c20b4618e35ab22487e36add0c0c9f1d8f94afd4c5078e40b57.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Impact of Information Diffusion on Bidding Behavior in Secret Reserve Price Auctions

Oliver Hinz

Johann Wolfgang Goethe-University, 60054 Frankfurt am Main, Germany, ohinz@wiwi.uni-frankfurt.de

Martin Spann

University of Passau, 94032 Passau, Germany, spann@spann.de

he interactive nature of the Internet promotes collaborative business models (e.g., auctions) and facilitates Tinformation-sharing via social networks. In Internet auctions, an important design option for sellers is the setting of a secret reserve price that has to be met by a buyer’s bid for a successful purchase. Bidders have strong incentives to learn more about the secret reserve price in these auctions, thereby relying on their own network of friends or digital networks of users with similar interests and information needs. Information-sharing and flow in digital networks, both person-to-person and via communities, can change bidding behavior and thus can have important implications for buyers and sellers in secret reserve price auctions. This paper uses a multiparadigm approach to analyze the impact of information diffusion in social networks on bidding behavior in secret reserve price auctions. We first develop an analytical model for the effect of shared information on individual bidding behavior in a secret reserve price auction with a single buyer facing a single seller similar to eBay’s Best Offer and some variants of NYOP. Next, we combine the implications from our analytical model with relational data that describe the individual’s position in social networks. We empirically test the implications of our analytical model in a laboratory experiment, and examine the impact of information diffusion in social networks on bidding behavior in a field study with real purchases where we use a virtual world as proxy for the real world. We find that the amount and dispersion of information in the individualized context, and betweenness centrality in the social network context, have a significant impact on bidding behavior. Finally, we discuss the implications of our results for buyers and sellers.

Key words: information diffusion; social networks; secret reserve price auctions; name-your-own-price; eBay best offer; virtual worlds

History: Ritu Agarwal, Senior Editor. This paper was received on July 14, 2006, and was with the authors 7 months for 3 revisions.

## 1. Introduction

The interactive nature of the Internet—enabled by the low transaction costs of this digital medium— has been a core driver of many web-related business models: The success of virtual communities and opinion marketplaces (e.g., LinkedIn.com or epinions.com) relies on the frequent message exchange of their members. Peer-to-peer concepts (e.g., Skype.com or Napster.com) are based on the direct or indirect exchange of messages or media content, and marketplaces provide interaction possibilities for buyers and sellers. In addition, interaction between buyers and sellers to determine the price of a transaction is a common feature of the web economy. Buyers and sellers interact in auctions (e.g., ebay.com), reverse auctions, and other forms of interactive, negotiation-type pricing mechanisms to increase welfare by means of price discrimination (e.g., Kannan and Kopalle 2001).

In Internet auctions, an important design option for sellers is the setting of a secret reserve price that has to be met by a buyer’s bid for a successful purchase (Bajari and Hortaçsu 2004). Such secret reserve prices can be found in various Internet auction formats such as open eBay auctions, eBay’s Best Offer auctions, and a number of variants of the Name-Your-Own-Price (NYOP) auctions. Sellers can decide to set a secret reserve price on eBay’s open-bid auctions, where buyers are informed about the existence of such a secret reserve price. A transaction occurs only if the winning bid meets the secret reserve price. In eBay’s

Best Offer auction, the seller can permit buyers to submit an offer that the seller can automatically accept if it is at least equal to a secret reserve price set by the seller (http://pages.ebay.com/help/sell/ best-offer.html). NYOP auctions, pioneered by Priceline.com in 1998, have developed into several variants. While Priceline combines the auction aspect of NYOP with opaque selling, other applications at European low-cost airlines (e.g., Germanwings.com), and software sellers like Ashampoo.com, use the NYOP auction to sell products under their own brand name. All variants of NYOP share a common feature in that prospective buyers bid for a product which is on sale at an unrevealed (i.e., secret) reserve price set by the seller and only if a bid amount is at least equal to the seller’s secret reserve price is the transaction initiated at the price denoted by the buyer’s bid.

In eBay’s Best Offer auction and most of the NYOP variants, a prospective buyer can usually participate in one of multiple parallel auctions for one unit of the product. Thus, a single buyer faces only a single seller in one auction. There is no price competition among buyers because a prospective buyer has solely to meet the secret reserve price set by the seller to win the auction. By the seller’s response to their bids, prospective buyers learn about the seller’s secret reserve price. They may share their knowledge with other prospective buyers, who can exploit this information in their bids in unfinished auctions for the same product, if the seller keeps the secret reserve price constant.

Bidders have therefore the opportunity and strong incentives to learn more about the secret reserve price in these auction types to bid close to secret reserve prices and possibly not overbid these at all or only marginally. Besides the information networks existing between friends, family members and colleagues, the Internet provides a digital platform for social networks to spread and gather information (e.g., online communities like BiddingForTravel.com and Better-Bidding.com list bids on flights and hotel rooms offered by Priceline).

Information that bidders receive via their social networks alters their beliefs about the secret reserve price and thus has an impact on bidding behavior. Information diffusion can lead to more homogeneous beliefs about the secret reserve price among bidders who receive similar information and result in a lower degree of price discrimination, potentially diminishing seller profit. Because the Internet promotes information-sharing by facilitating personto-person communication (e.g., via e-mail or instant messaging), as well as creating new social networks (e.g., social networking websites like Facebook or Myspace), we expect a considerable impact of information diffusion on bidding behavior and potentially on seller profit.

Previous research on secret reserve price auctions has not examined the impact of information diffusion via digital and social networks on bidding behavior. This is surprising, given the inherent incentives for consumers to obtain and exchange such information mentioned above. Furthermore, Avery et al. (1999) and Dellarocas (2003) discuss the impact of information diffusion on welfare and profit of web-based business models but do not quantify their effects or discuss secret reserve price auctions. Sellers need to understand the effects of this information diffusion on bidders’ strategies and their profit to be able to enhance the application and design of markets in general (Bapna et al. 2004) and auctions with secret reserve prices in particular.

The goal of this paper is to analyze the impact of information diffusion in social networks on bidding behavior in secret reserve price auctions. We first develop an analytical model for the effect of shared information on individual bidding behavior in a secret reserve price auction with a single buyer facing a single seller similar to eBay’s Best Offer and some variants of NYOP. Next, we combine our analytical model with relational data describing the individual’s position in a social network and analyze the impact of the social position on bidding behavior in such secret reserve price auctions. We empirically test the implications of our analytical model in a laboratory experiment with induced valuations. Using these insights, we then examine the impact of information diffusion in social networks on bidding behavior in a field study with real purchases, where we use a virtual world as proxy for the real world. Finally, we discuss the implications of our results for buyers and sellers.

## 2. Previous Research

Previous research on secret reserve price auctions is predominantly concerned with whether to use secret reserve prices (with respect to auction design) and the revenue effects for sellers (Bajari and Hortaçsu 2004, Pinker et al. 2003, Reiley 2006). Bichler and Kalagnanam (2006) estimate secret reserve prices in procurement auctions based on observed drop-out bids. The partial revelation of the secret reserve price owing to information diffusion has not, however, been examined in academic literature. Klemperer (2002) pinpoints the danger posed by the thinness of the auction-theoretic literature on auction fraud and we did not find any discussion on buyers’ collusion in a related setting in auction theory. Studies in experimental economics look at collusive behavior in bidding rings in repeated English auctions (Phillips et al. 2003), cooperative agreements in sealed-bid auctions (Isaac and Walker 1985) and how bidders collude in multiple, simultaneous sealed-bid auctions (Kwasnica 2000). Models in economics, however, routinely assume that cooperation among bidders only takes place in the presence of incentives to share information. In contrast, insights from other disciplines such as Information Systems teach us that individuals share information and help others, including strangers whom they will never meet in person (e.g., Constant et al. 1994).

Previous research on the NYOP auction has had two different goals: First, to analyze bidding behavior in NYOP auctions and, second, to determine the optimal auction design. Several studies develop analytical models for individual bidding behavior to measure bidders’ frictional costs (Hann and Terwiesch 2003), to measure bidders’ willingness-to-pay (Spann et al. 2004) and to derive implications on the optimal auction design (Terwiesch et al. 2005). Fay (2004) studies optimal design of a NYOP auction in an analytical model where a single buyer may use multiple identities and can thus learn more about the secret reserve price. Fay (2004) does not, however, incorporate information diffusion among buyers.

Behavioral aspects of bidding behavior in NYOP auctions are analyzed by augmenting analytical models to account for behavioral aspects (Ding et al. 2005) or by studying the extent to which bidding behavior in NYOP auctions is rational, as would be expected of an economic model (Spann and Tellis 2006). Additionally, consumers’ preferences for different design specifications of NYOP auctions are analyzed by Chernev (2003).

While all these studies offer interesting and valid insights about bidding behavior and auction design, they account for individuals as atomized, i.e., not interacting with others. The social dimension of communication among bidders can, however, be important for web business models such as secret reserve price auctions. We expect information diffusion to have a significant impact on bidding behavior and the success of these business models (Avery et al. 1999, Dellarocas 2003, Butler 2001).

Information is a key determinant of consumer and firm behavior as well as market performance. Information diffusion can be accomplished via the price mechanism of markets (Hayek 1945), corporate communication (e.g., advertising) or interaction in social networks (e.g., word-of-mouth). Whereas the former have been well analyzed in economics and business research over the past decades, research on information diffusion via digital social networks is an emerging field in information systems, marketing and economics.

Godes and Mayzlin (2004) and Chevalier and Mayzlin (2006) show in different settings that word-ofmouth can affect product sales. A study by Chatterjee and Eliashberg (1990) reveals that consumers use externally-obtained information like word-of-mouth to update personal beliefs and thereby change actions. Furthermore, Putsis et al. (1997) show that the structure of the network has an important influence on the spread of word-of-mouth.

As outlined by Granovetter (1985), economic life is embedded in social relations. Thus, individual-level models have to incorporate these social relations to be able to derive valid predictions for individual behavior and seller profit. We therefore combine two approaches, economics and social network analysis, to determine the impact of information diffusion on secret reserve price auctions.

## 3. Methodology

To address our central research question, the analysis of the impact of information diffusion in a social network on bidding behavior in secret reserve price auctions, we have to analyze (i) the individual response (i.e., the impact on bidding behavior) to information on previous bid amounts and (ii) the impact of social position on bidding behavior, and thus the impact of the information flow through a social network on auction outcomes. We first develop an analytical model of bidding behavior, which captures the impact of shared information on individual bidding behavior and is thus an explanation of individual-level behavior. We distinguish between two types of information, amount and dispersion, and derive implications for the effect of such information on individual bidding behavior. We validate these implications in a laboratory study while controlling for individual characteristics like willingness-to-pay (WTP) and prior beliefs about the secret reserve price (see upper part of Figure 1).

Figure 1 Overview of Methodological Approach  
![](/api/attachments/UK8ZZACN/fulltext/images/804a9e0527e4d453172eb2b895a16bb0d7fc1539f177d2ec5e5a3709494c6013.jpg)

Second, on the basis of the individual-level response predictions for the impact of information on bidding behavior, we use insights from social network analysis to hypothesize about the type of information an individual is likely to obtain based on his or her position in social networks (dashed arrow in Figure 1). We derive three hypotheses on the impact of social position on bidding behavior owing to the type of information that flows through the network which we test by conducting a field study where we combine data on real purchases with social network data. Figure 1 illustrates our approach.

Data in social sciences can be distinguished between two principal types: Attribute data and relational data (Scott 2000). Attribute data describe the properties, qualities and characteristics that belong to agents as individuals. Relational data are the contacts, connection and ties which relate one agent to another. Relations are not the characteristics of individuals but of the system to which the agents belong (Scott 2000). In our approach, we make use of both attribute and relational data to analyze the bidding behavior in secret reserve price auctions, thereby embedding economic behavior into social context.

## 3.1. Impact of Shared Information on Bidding Behavior

We begin with an economic model as a theoretical basis explaining bidding behavior and assessing the effects of exogenously-given information by means of word-of-mouth or messages circulating in Internet communities, also called “word-on-line” (Granitz and Ward 1996). We develop propositions for the impact of various types, amount, and dispersion of shared information on bidding behavior that form the basis for our empirical tests.

3.1.1. Analytical Model for Bidding Behavior. We model bidding behavior for the special case of a secret reserve price auction similar to eBay’s Best Offer auction and some versions of the NYOP auction. In this model, the seller sets a secret reserve price and offers similar products using multiple parallel secret reserve price auctions over a period of time (without changing the secret reserve price). In each auction, only one buyer enters the market and the buyer can place only one bid. This model is similar to models of bidding behavior in NYOP auctions (e.g., Hann and Terwiesch 2003 and Spann et al. 2004), but extends these models to account for the impact of external information. We assume that bidders correctly expect an exogenous and constant secret reserve price of the seller. Bidders are considered to be riskneutral.

3.1.2. Base Model (No Shared Information). The decision rule for the no-communication model (i.e., without additional shared information) is that the jth bidder submits a bid $b _ { j }$ for a product if the expected consumer surplus ECS of the bid (accounting for frictional costs $c _ { j }$ which are incurred by submission of the bid) is not negative. The bidder optimizes the expected consumer surplus ECS of the bid over the bid amount (see Equation (1)). The bid amount influences both the surplus and the success probability. The success probability depends on the jth bidder’s assumption regarding the probability distribution $g _ { j } ( p _ { T } )$ of the secret reserve price $p _ { T }$ . The bidder increases her success probability by increasing the amount of the bid. At the same time, a higher bid decreases consumer surplus in the case of a successful bid. Bidders have a reservation price $r _ { j }$ for the product sold by the seller. This reservation price is determined by bidders’ willingness-to-pay WTP . If, however, a bidder expects a highest possible value (e.g., an upper truncation point of the probability distribution) for the secret reserve price that is below her WTP, she will use this highest expected secret reserve price value as her reservation price.

$$
\begin{array}{l} \underset {b _ {j}} {\max} E C S _ {j} = E (r _ {j} - b _ {j}) - c _ {j} \\ \qquad \qquad \qquad = \int_ {0} ^ {b _ {j}} (r _ {j} - b _ {j}) \cdot g _ {j} (p _ {T})   d p _ {T} - c _ {j} \\ \text { s.t. } E C S _ {j} \geq 0; \quad b _ {j} \leq r _ {j}; \quad (j \in J). \end{array}\tag{1}
$$

The bidder’s assumption regarding the probability distribution $g _ { j } ( p _ { T } )$ of the secret reserve price can have different functional forms, including a normal distribution or a uniform distribution. We can derive a closed-form solution for the bidder’s optimal bid in case of a uniform distribution of the expected secret reserve price on the interval $[ L B _ { j } , U B _ { j } ]$ . This assumption is in line with Stigler (1961), Ding et al. (2005), and Hann and Terwiesch (2003). Results also hold for all other common distributional assumptions because only the strength of the effect may vary (a solution assuming a normal distribution is more complex, because the standard normal distribution function cannot be expressed in terms of elementary functions, and is available from the authors on request). On the assumption of a uniform distribution, we can then easily derive the optimal bid for our base model:

$$
E C S _ {j} = \int_ {L B _ {j}} ^ {b _ {j}} (r _ {j} - b _ {j}) \cdot \frac {1}{U B _ {j} - L B _ {j}} d p _ {T} - c _ {j}\tag{2}
$$

$$
\begin{array}{r l} \Rightarrow \max E C S _ {j} & = \frac {d E C S _ {j}}{d b _ {j}} \\ & = \frac {1}{U B _ {j} - L B _ {j}} [ (- 1) \cdot (b _ {j}) + L B _ {j} + (r _ {j} - b _ {j}) \cdot 1 ] \stackrel {!} {=} 0 \end{array}
$$

$$
\Leftrightarrow b _ {j} ^ {*} = \frac {r _ {j} + L B _ {j}}{2} \quad \text { with } r _ {j} = \min \{W T P _ {j}, U B _ {j} \}.\tag{3}
$$

The bidder will submit the bid if $E C S _ { j }$ is not negative and the optimal bid does not exceed the bidder’s reservation price $r _ { j } .$ As can be seen, the bidder’s belief about the distribution of the secret reserve price directly influences the optimal bid amount (3). A bidder thus has an incentive to learn more about accepted and rejected bids to update her beliefs about the distribution of the secret reserve price.

3.1.3. Impact of Shared Information. The impact of shared information obtained by bidders $( \mathrm { i . e . , }$ information about accepted or rejected bids) can be modeled as updating of the beliefs using Bayes’ rule. Information about a rejected bid leads to a lefttruncation of the distribution if the amount of the rejected bid is higher than the lower truncation point LB of the prior. Vice versa, a message about accepted bids leads to a right-truncation of the distribution if the amount of the accepted bid is lower than the (prior) upper truncation point UB. This setting is similar to an affiliated value setting of a first-price auction where the seller is another bidder whose reservation price distribution is being partially revealed by providing information about winning or losing bids in this auction (Milgrom and Weber 1982).

The lower truncation point $L B ^ { \prime }$ can easily be determined as the $\operatorname* { m a x } ( \{ B _ { R } \} , L B )$ where $\{ B _ { R } \}$ is the set of all rejected bids and LB the prior lower truncation point. $U B ^ { \prime }$ is the min $( \{ B _ { A } \}$  UB where $\{ B _ { A } \}$ is the set of all accepted bids and UB is the prior upper truncation point. Note that we do not account for information overload (see e.g., Jones et al. 2004) because we assume unrestricted rational behavior and hence bidders always pick the most valuable information.

The effect of shared information is then straightforward: On the one hand bidders who overestimate the secret reserve price are corrected downwards and on the other hand bidders who underestimate the secret reserve price are corrected upwards. This can lead to higher or lower bid amounts depending on the prior relationship between bidders’ WTP and bidders’ beliefs.

We outline the following corollaries for the impact of shared information on bidding behavior from our analytical model: If a bidder receives information that a bid amount of $B _ { R }$ was rejected, she updates her belief according to Bayes’ rule. The new truncation point is $L B ^ { \prime } = B _ { R } { \mathrm { ~ i f ~ } } B _ { R } > L B _ { \prime }$ , otherwise $L B ^ { \prime } = L B$ . Thus, if $L B ^ { \prime } \geq L B$ , her new bid amount is $b i d ^ { \prime } = ( r + L B ^ { \prime } ) / 2 \geq$ $b i d = ( r + L B ) / 2$ . Note that this function is monotonically but not strictly monotonically increasing since $L B ^ { \prime } = L B$ does not bring new insights and hence no change of bidding behavior. We thus state Corollary 1:

<sup>Corollary</sup> <sup>1</sup> <sup>(C1).</sup> Information about rejected bids leads to strictly monotonically increasing bids -in increasing

LB if the information about the rejected bid is above bidder’s lower bound of the prior $( B _ { R } > L B )$

Analogously, information about an accepted bid $B _ { A }$ leads to lower bids if $B _ { A } < W T P$ and $B _ { A } < U B$ . We state Corollary 2 as follows:

<sup>Corollary</sup> <sup>2</sup> <sup>(C2).</sup> Information about accepted bids leads to strictly monotonically decreasing bids -in decreasing UB if the information about the accepted bid is below bidder’s willingness-to-pay $( B _ { A } < W T P )$ and the upper bound of the prior $\left( B _ { A } < U B \right)$

From these two corollaries, we can conclude that additional information decreases the absolute difference between bid and secret reserve price. We define the standardized absolute deviation $S A D _ { j }$ between the jth bidder’s bid and the secret reserve price for a product relative to the jth bidder’s WTP as

$$
S A D _ {j} = \frac {\left| b _ {j} - p _ {T} \right|}{W T P _ {j}}.\tag{4}
$$

If $B _ { R }$ and $B _ { A }$ represent valid information and C1 and C2 hold, $S A D _ { j }$ is monotonically decreasing with additional information. The bid amounts asymptotically approach the secret reserve price until the secret reserve price is completely revealed. The more information is available, the closer bidders bid to the secret reserve price. Our model leads hence to Implication I1.

<sup>Implication</sup> <sup>I1.</sup> Additional information monotonically decreases the difference between bid amounts and the secret reserve price.

Burt (1992) distinguishes between the amount of information available and the dispersion of information. While the amount of information is incorporated in Implication I1, the dispersion in the set of received information can also affect bidding behavior. Dispersion of information was first discussed by Stigler (1961, 1962) as part of the economics of information and was first solved mathematically by McCall (1970). McCall’s model for the economics of searching for jobs reveals that greater variance of information may make the searcher better off, and prolong optimal search, even if the searcher is risk-averse. Given a fixed mean, more variation in wage offers may make the searcher want to search longer, expecting to receive an exceptionally high wage offer. The possibility of receiving some exceptionally low offers has less impact on the optimal search because bad offers can be ignored. In our context, this means that information about the acceptance or rejection of bids should be more valuable for the searcher if the dispersion in bid amounts is high. In other words, if n pieces of information are similar, i.e., they contain a similar bid amount, it is likely that this set of information is less valuable when compared with a set containing dispersed information. We thus state Implication I2.

<sup>Implication</sup> <sup>I2.</sup> More dispersed information decreases the difference between bid amounts and the secret reserve price.

3.2. Information Diffusion in Social Networks The analytical model allows us to describe the impact of shared information on bidding behavior but assumes that the information flow to the agents is exogenously given. We can thus not analyze the impact of information diffusion within the network. We therefore use insights from social network analysis to link the implications on the impact of shared information on individual bidding behavior to the amount and type of shared information bidders are likely to obtain in a social network. This allows us to examine the effect of information diffusion on the success of secret reserve price auctions for different social network structures.

Granovetter (1974) pinpoints how the acquisition of information heavily depends on the strategic location of an agent’s contact in the overall information flow. Figure 2 depicts an exemplary network for illustration purposes in which, for example, agent B can obtain direct information from agents A and C only. The position of B, however, is not necessarily disadvantageous, because B has access to very different parts of the overall network. In this example, B is acting as a bridge between the subnetwork around A and the subnetwork around C.

Figure 2 Undirected Network  
![](/api/attachments/UK8ZZACN/fulltext/images/e859d6d5a9abde457460dfb5861ceaad36c32807baf54384cc5d889f86fed2c2.jpg)

Freeman (1977) developed a set of measures of centrality which were elaborated in numerous follow-up papers. With these different concepts from social network analysis it is possible to quantify the social position of nodes and determine then the effect of social position on some dependent variable.

On the basis of social network theory, we therefore introduce different measures that are likely to have an influence on the type and amount of information that bidders who participate in a network will receive. These measures are related to a bidder’s position in a social network and are (1) the number of links to other bidders (“degree centrality”), (2) a bidder’s connection to dispersed parts of the network (“betweenness centrality”) and (3) the structure of a bidder’s circle of friends, i.e., “clique” (“clustering”).

The number of links a bidder (“node”) has with other network members is measured by the degree centrality which is defined for undirected networks as number of links which interconnect with the node. The degree of a node is a numerical measure of the size of its neighborhood. In an undirected network, the degree of a node equals the count of the number of ties to other agents in the network. Figure 2 illustrates such an undirected network, where e.g., node B has a degree of 2 because he is only linked to node A and node C. In a directed network, the number of incoming ties from other agents defines the indegree and the number of ties towards other agents defines the outdegree of a node.

It is well known in social network analysis that agents with high degree centrality, i.e., with more links to other bidders, can potentially receive more information (e.g., Burt 1992). Because more information will decrease the difference between bid amounts and secret reserve price (based on Implication I1), we expect that bidders with high degree centrality should be able to bid more closely to the secret reserve price than bidders with lower degree centrality. We thus state Hypothesis 1:

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> The difference between bid amounts and the secret reserve price decreases with increasing degree centrality of bidders.

In social network analysis “betweenness centrality” measures the degree to which an agent lies between dispersed parts of the network (Freeman 1979). It measures the extent to which a node is directly connected only to those other agents that are not directly connected to each other. For a network with a set of V nodes, let $\sigma _ { s t }$ be the number of shortest paths from s to t and $\sigma _ { s t } ( i )$ the number of shortest paths from s to t that go through node i. The betweenness centrality $C _ { B } ( i )$ of node i is defined as the proportion of shortest paths from s to t that pass through i

$$
C _ {B} (i) = \sum_ {s \neq v \neq t \in V} \frac {\sigma_ {s t} (i)}{\sigma_ {s t}}.\tag{5}
$$

Scott (2000) calls agents with high betweenness centrality “intermediaries” or “brokers” because they can access and pass information from different parts of the network. In a diffusion process, a node with high betweenness centrality can bridge dispersed parts of the network and control the flow of information. A common example used in social network analysis is the position of an executive secretary, who can obtain valuable information owing to this social position. A node with high betweenness centrality can act as a bridge between disparate regions of the network where different ideas may evolve.

Hence, bidders with a high level of betweenness are likely to receive dispersed information, yielding a decreasing difference between bid amounts and secret reserve prices (based on Implication I2). Therefore, we propose Hypothesis 2.

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> The difference between bid amounts and the secret reserve price decreases with increasing betweenness centrality.

Social networks often encompass subnetworks, so-called “cliques,” which are groups of very well interconnected individuals. The interconnections within a clique can be measured by the clustering coefficient (Watts and Strogatz 1998), which accounts for the relation between existing and possible connections. If a node has z neighbors, a maximum of $z ( z - 1 ) / 2$ links is possible between them. The clustering coefficient $C _ { i }$ for a node i is then defined as the ratio of existing links w to the maximum number of possible links between the neighbors of the node i

$$
C _ {i} = \frac {2 \cdot w}{z \cdot (z - 1)}.\tag{6}
$$

A clustering coefficient of 1 describes a situation in which all neighbors are directly connected. Highly connected cliques that can be identified by a high clustering coefficient tend to have better local cooperation (Chwe 2000) and should thus be better informed about the secret reserve price. Thus, we hypothesize:

<sup>Hypothesis 3 (H3).</sup> The difference between bid amounts and the secret reserve price decreases with increasing clustering coefficient.

## 4. Empirical Studies

We test the implications and hypotheses derived in the previous section with two different approaches, experimental microeconomics, as well as the analysis of field data with real purchases augmented with the relational data of the underlying social network structure. As a first step, we test the results from our analytical model in a laboratory experiment with induced valuations (Smith 1976) and systematically manipulate the stimuli which allows for maximum control (study 1). Given the validity of our Implications I1 and I2, we expect that bidders with high centrality in social networks benefit most from information diffusion. To test the corresponding Hypotheses 1–3, we set up a field study in a virtual world that allows us to use data from a “friend’s list” as proxy measure for possible communication links (study 2).

## 4.1. Study 1: Laboratory Test of Analytical Model of Bidding Behavior

Method. We conducted a computer-assisted laboratory experiment to test our implications derived in §3.1 for the effect of exogenous (i.e., shared) information on individual bidding behavior. We experimentally manipulated information presented to subjects via a controlled web-based information board. The subjects were systematically confronted with different stimuli which we derived from the following factorial design (1) amount of information and (2) dispersion of information (high/low). The number of available messages is displayed in Table 1. “A bid of x EUR has been accepted” indicated an accepted bid, while “A bid of y EUR has been rejected” indicated that a bid of y did not meet the secret reserve price.

We generated the dispersion in bid amounts as follows and illustrate the procedure using the case of three messages about rejected bids: For the high dispersion case, we drew three random numbers from the uniformly-distributed interval between the lower bound and the secret reserve price. For the case of low dispersion in contrast, we divided the interval between the lower bound and the secret reserve price into five intervals of equal size and then drew all three messages from the same subinterval. Figure 3 illustrates the procedure. We applied the same procedure to generate dispersion of messages about accepted bids.

Table 1 Experimental Treatment Factors in Laboratory Study

<table><tr><td>Factor dispersion of information</td><td>Factor amount of information provided to subjects</td></tr><tr><td>-/-</td><td>T1: No information</td></tr><tr><td>-/-</td><td>T2: One message about an accepted bid</td></tr><tr><td>-/-</td><td>T3: One message about a rejected bid</td></tr><tr><td>Low/high</td><td>T4: One message about a rejected bid, two messages about accepted bids</td></tr><tr><td>Low/high</td><td>T5: One message about an accepted bid, two messages about rejected bids</td></tr><tr><td>Low/high</td><td>T6: Two messages about a rejected bid, three messages about accepted bids</td></tr><tr><td>Low/high</td><td>T7: Three messages about a rejected bid, two messages about accepted bids</td></tr></table>

In the case of low dispersion all messages about accepted or rejected bids came thus from a similar subdistribution resulting in e.g., “A bid of 100 EUR has been accepted. A bid of 105 EUR has been accepted. A bid of 98.54 EUR has been accepted.” In the high-dispersion case the amount was drawn from the entire interval. Note that this dispersion stimulus only influenced the difference between messages of the same direction (i.e., information about accepted or rejected bids).

Figure 3 Procedure for Factor Dispersion of Information  
![](/api/attachments/UK8ZZACN/fulltext/images/17e19739cf71a21a0dc5008e933e9d981c9cae6e0f023c05b12c13637266d737.jpg)

The information given in the experimental treatments was predetermined as part of our experimental manipulation and did not depend on actual behavior of subjects. The information in the messages presented was always true, i.e., consistent with actual secret reserve prices applied (e.g., “A bid of 100 EUR has been rejected” and “A bid of 160 EUR has been accepted” indicate a secret reserve price between 100 EUR and 160 EUR). Secret reserve prices were systematically varied and set such that we expected about an even split between accepted and rejected bids if the bidder bid as predicted by our analytical model.

Further, we controlled for bidders’ product valuation using an induced-values paradigm (Smith 1976) by informing them about the resale value of the given product. Each product had a resale value inducing the subject’s WTP. The difference between the induced valuation and a successful bid thus represents surplus for subjects. The induced valuation for the different products ranged from 60 EUR to 755 EUR. The subjects were also informed about the lower and upper bound of the interval for the secret reserve price. The lower bounds were set between 26.6% and 72.7% of the induced valuation for the product while the upper bounds were between 115.8% and 146.1% of the induced valuations for the product. In the information treatments, messages about rejected bid amounts were always higher than the initial lower bound LB and messages about accepted bid amounts were always lower than the initial upper bound UB: $\forall B _ { R } \in \{ B _ { R } \} \colon B _ { R } > L B$ and $\forall B _ { A } \in \{ B _ { A } \} \colon B _ { A } < U B$

We used a within-subject design in which every subject had the option to place bids on one hypothetical, generic product in each of 14 different experimental treatments. We created the 14 experimental treatments to account for all factor level combinations of both experimental factors (see Table 1): Subjects could bid on two products in each of the 7 levels of the factor amount of information: In the case of factor levels with at least 2 messages about rejected or accepted bids (factor levels T4–T7), we systematically combined each factor level of the amount of information with each of the two levels of the second factor dispersion of information (high or low:

see Table 1). In the case of factor levels with no or only one message for the amount of information (factor levels T1–T3), we cannot not vary dispersion and subjects were assigned to the same factor level for the amount of information twice to have a balanced design (see Table 1). The 14 treatments were randomly combined with 14 different generic products.

The within-subject design used in this experiment allowed us to control for order effects by systematic variation of scenarios and random assignment of participants to different scenarios. The subjects’ success was measured by their generated consumer surplus and subjects were remunerated accordingly (see appendix for experimental instructions). We paid a basic reward of 6 EUR for participation plus their accumulated surplus for all 14 products divided by 80. All subjects were informed about this rule. Average remuneration per participant was 9.68 EUR ( 14 USD).

The experiment was conducted in a lab equipped with PCs and separators between subjects to limit visual and verbal communication. Participants were randomly assigned to different sessions of 15–20 subjects each. For each product, subjects were presented with different sets of messages about rejected and accepted bids according to the specific treatment and could submit a bid for this generic product. All treatments were systematically varied and combined with the hypothetical products by means of induced valuations in random order to control for product and order effects. After the completion of bidding rounds, subjects had to answer an additional questionnaire where we elicited demographics and additional information.

Results. 121 subjects participated in the laboratory experiment. The subjects were mainly recruited from MBA students (117 students, 4 nonstudents) and the majority of subjects were male (29 female, 92 male). In total, 1,694 bids were placed, 728 were rejected, and 966 accepted. Using numeric simulations we actually expected a fraction of 50% for both groups. This means that the subjects bid rather closely to their induced WTP, which lead to more accepted bids but a relatively small realized consumer surplus.

To test our corollaries and implications, we standardize variables by dividing through the induced $W T P _ { j }$ for each product to attain comparability across products (standardized bid $S b i d _ { j } = b _ { j } / W T P _ { j }$ and standardized absolute deviation $\dot { S A } D _ { j } \stackrel { \cdot } { = } | b _ { j } - \stackrel { \cdot } { }$ $p _ { T } | / W T P _ { j }$ between a bidder’s bid and the secret reserve price). To test C1, we compare the standardized bids of the amount of information factor level T1 (no information) with standardized bids of level T3 where subjects received a message that a bid with a certain amount $B _ { R }$ was rejected. We expect that this information influences the beliefs about the lower truncation point LB (lower bound for uniform distribution), because all messages about rejected bids were by design always higher than the initial lower bound LB. Table 2 depicts a significant increase in the standardized bid in case of information about a rejected bid (repeated-measures ANOVA, $p < 0 . 0 5 )$ which is consistent with C1.

Table 2 Influence of Rejected Bids on Bidding Behavior

<table><tr><td>Amount of information</td><td>Mean  $Sbid_j$ </td><td>N</td><td>SD</td></tr><tr><td>No information (T1)</td><td>0.832</td><td>242</td><td>0.1061</td></tr><tr><td>Message about a rejected bid (T3)</td><td>0.852</td><td>242</td><td>0.0814</td></tr><tr><td>Percentage change (p-value)</td><td colspan="3">+2.37% (0.022)</td></tr></table>

Testing C2 has to account for the fact that information about accepted bids $B _ { A }$ influences bidding behavior only if the upper bound of the belief about the secret reserve price serves as the reservation price $( \mathrm { i . e . , } U B < W T P )$ and is below the upper bound of the prior $( B _ { A } < U B )$ . In the amount of information factor level with one message about an accepted bid (T2), all messages about accepted bids were by design always lower than the initial upper bound UB. We hence separate the cases in T2 where the information about the accepted bid $B _ { A }$ is below subjects’ willingnessto-pay $( B _ { A } < W T P )$ . For cases with $B _ { A } < W T P$ , standardized bids are significantly lower than in cases where $B _ { A }$ is above or equal to subjects’ WTP $( p <$ 005; see Table 3). Comparing the mean standardized bid for the case $B _ { A } < W T P ( S b i d _ { j } = 0 . 8 4 4 )$ with the case where no information is provided (no information (T1): mean $S b i d _ { i } = 0 . 8 3 2 )$ , we find no significant difference $( p > 0 . 5 3 )$

Table 3 Influence of Accepted Bids on Bidding Behavior

<table><tr><td>Information (T2)</td><td>Mean  $Sbid_j$ </td><td>N</td><td>SD</td></tr><tr><td> $B_A \geq WTP$ </td><td>0.888</td><td>212</td><td>0.1173</td></tr><tr><td> $B_A < WTP$ </td><td>0.844</td><td>30</td><td>0.0533</td></tr><tr><td>Percentage change (p-value)</td><td colspan="3">-5.00% (0.042)</td></tr></table>

Table 4 Influence of Number of Messages on Bidding Behavior

<table><tr><td>No. of messages</td><td>Mean of  $SAD_{j}$ </td><td>N</td><td>SD</td></tr><tr><td>0</td><td>0.173</td><td>242</td><td>0.1353</td></tr><tr><td>1</td><td>0.152</td><td>484</td><td>0.1318</td></tr><tr><td>3</td><td>0.103</td><td>484</td><td>0.0963</td></tr><tr><td>5</td><td>0.098</td><td>484</td><td>0.1003</td></tr></table>

Implication I1 predicts that bids get closer to the secret reserve price with additional information. To test Implication I1 we compare $S A D _ { j }$ for treatments with different numbers of presented messages (see Table 4). More information significantly diminishes the difference between bid amounts and secret reserve prices (repeated-measures ANOVA, $p < 0 . 0 1 )$ which is consistent with Implication I1.

Implication I2 predicts that bids get closer to the secret reserve price with more dispersed information. To test Implication I2, we analyze the impact of our experimental treatments on the $S A D _ { j }$ for the factor levels of the amount of information with at least two messages about rejected or accepted bids (factor levels T4–T7). Here we can systematically combine each factor level of the amount of information with each of the two levels of the dispersion of information factor (high or low: see Table 1) and test the effect of both factors (i.e., Implications I1 and I2), as well as for an interaction effect, via a repeated-measures analysis of variance (ANOVA) for this subsample.

We find that more dispersed information significantly decreases the standardized absolute deviation $S A D _ { j }$ between a bidder’s bid and the secret reserve price (repeated-measures ANOVA, $p < 0 . 0 1 )$ , which is consistent with Implication I2 (see Table 5).

Table 5 Influence of Information Dispersion on Bidding Behavior

<table><tr><td rowspan="2">Amount of information</td><td colspan="2">Low dispersion</td><td colspan="2">High dispersion</td><td rowspan="2">N</td></tr><tr><td>Mean of  $SAD_j$ </td><td>SD</td><td>Mean of  $SAD_j$ </td><td>SD</td></tr><tr><td>T4</td><td>0.120</td><td>0.1041</td><td>0.078</td><td>0.0909</td><td>242</td></tr><tr><td>T5</td><td>0.127</td><td>0.1018</td><td>0.086</td><td>0.0780</td><td>242</td></tr><tr><td>T6</td><td>0.133</td><td>0.1168</td><td>0.065</td><td>0.0791</td><td>242</td></tr><tr><td>T7</td><td>0.119</td><td>0.1068</td><td>0.074</td><td>0.0765</td><td>242</td></tr></table>

More information, however, i.e., going from 3 messages (amount of information factor levels T4 and T5) to 5 messages (amount of information factor levels T6 and T7) has no significant effect on the difference between bid amounts and secret reserve prices in this subsample (repeated-measures ANOVA, p > 064). Therefore, the interaction effect between dispersion and the number messages is also not significant (repeated-measures ANOVA, p > 029).

Hence, the results of study 1 support both Implications I1 and I2. We can thus conclude that dispersion of information and the number of messages influence the impact of information diffusion on bidding behavior in secret reserve price auctions. The benefit of additional messages diminishes, however, with an increasing number of messages, which may be explained by diminishing returns of extra information.

## 4.2. Study 2: Field Test with Real Purchases

Method. The results from the previous sections indicate the applicability of our analytical model to explain individual bidding behavior. Because we support for Implications I1 and I2, we expect that individuals’ position in a social network has an impact on their bidding behavior. We hypothesize that the obtained information is determined by the individual social network position. Therefore, we now focus on the impact of contact, ties, connections and group attachments which relate one bidder to another and can thus not be reduced to the properties of the individual bidders themselves (Scott 2000). Data collection for social networks is a very complex task (Marsden 1990) because the entire social network cannot be completely observed. For our purposes we apply a novel approach: We conduct a field study with real purchases in a virtual environment called HabboHotel (e.g., http://www.habbo.com/). This is a virtual world without monthly fees for a regular membership. Additionally, HabboHotel offers premium memberships (HabboClub) for approximately 5 EUR/month (approx. 7 USD/month) which allows members to have special looks, have access to special moves and allows for a higher number of connected friends. Revenues are mainly generated by the sales of virtual products. These products are usually sold through applying a posted price and can then be used by the buyer to personalize her chat-room.

To test our hypotheses, we conducted a field study with the German version of HabboHotel and sold bundles of three virtual products applying a secret reserve price auction with a single buyer facing a seller similar to eBay’s Best Offer and some variants of NYOP. The auction was promoted in a subcategory called “Events” on the HabboHotel.de-website and it was communicated that this is a short-time event while the exact end of the auction was not communicated. Two of the three products in the auctioned bundle were already available in previous promotion campaigns, a Habbo record player and a piece of Chinese-style furniture, and the third product, a virtual white rubber chair, had not been sold before and was especially created for this study. There were no comparable substitutes for the white rubber chair (e.g., no red rubber chair) at the time of the experiment, making this item particularly rare. In a previous campaign, the record player was sold for approximately 2 EUR and the Chinese-style furniture for approx. 3.50 EUR but both products were not offered for sale any longer by the operator of the HabboHotel. Virtual items can, however, be traded and sold within the HabboHotel to other players and such market prices heavily depend on the individual bargaining abilities.

In our secret reserve price auction, bidders had the option to place one bid for a single bundle of these three items. We explained the mechanism on the website and pointed out that bidders should think carefully before placing a bid because we provide only one opportunity to bid. We also stated on the website that the secret reserve price for the bundle was definitely between 0 EUR and 20 EUR. Bidders had to provide their email address, to which a confirmation mail was sent after the placement of their bid. Bidders had to confirm their bid by clicking on a link in this email for their bid to be processed. Additionally, bidders had to state the alias of their Habbo-character which would then receive the bundle of items in case of a successful bid. The email address as well as the alias of the Habbo-character had to be unique, making it indeed not impossible but rather inconvenient to create different identities to bid again. Nevertheless, we cannot rule out such behavior, which has already been discussed by Fay (2004) for bids at Priceline. After 15 minutes we sent out an email with information about the bid’s acceptance or rejection. The secret reserve price was set to 9.43 EUR (approx. 14 USD) and winning bidders received the items in the game after receipt of payment was confirmed. Figure 4 shows Habbo-characters and the rare white rubber chair.

Figure 4 Screenshot of HabboHotel with White Rubber Chair Tested by a Player  
![](/api/attachments/UK8ZZACN/fulltext/images/2f692d09f65465e2d11189e7b11b9b59136ceb468b32786bfbed71af14fae140.jpg)

HabboHotel.de does not provide a forum itself because the management wants the participants to be online in the virtual environment as often as possible. This gives us the unique opportunity to observe the information diffusion in a relatively closed system. We use the “friend’s list” (similar to a contact list in Skype or ICQ) as proxy for likely communication links and description of the social network. These data were provided by the operator of HabboHotel two days after the end of the secret reserve price auction. We were able to match bidding data and the friend’s list by the bidder’s alias. Additionally, we asked bidders to participate in a post-experimental questionnaire and provided incentives for filling out the questionnaire in the form of the virtual currency used by HabboHotel (worth 100 EUR) drawn from a lottery for the bidders who completed the questionnaire in full. Thus, we were able to match bidding data, social network data and questionnaire data.

The friendship network of HabboHotel consisted at the time of the experiment of 196,748 participants, demonstrating the popularity of this virtual world among German teenagers. Following the common notation, nodes symbolize participants and links denote the friendship relationships in this network. The number of links between participants is 5,206,784, resulting in a mean degree of 26, whereas the median degree is 10 (Minimum: 0, Maximum: 500). Figure 5 shows that this network meets the requirement for scale-free networks (Barabasi and Bonabeau 2003), having many nodes with very few links and very few nodes with a very high number of links. Apparently, there is a structural break at the size of 100 links. This is the maximum number of possible friendships for regular members, whereas paying premium members can increase this maximum number to 500. This limitation also explains why we do not see a perfect linear correlation between the log-scale of nodes and nodes degrees.

Figure 5 Log Scale Number of Nodes to Degree of Nodes  
![](/api/attachments/UK8ZZACN/fulltext/images/96d3510a2f28bb83a006b2517e5268973cee901478acaa0db6e927c813767009.jpg)

Results. In the five days of the offering (2006-12-04 to 2006-12-08), we received 314 bids of which 228 were confirmed. 122 (53.5%) of these bids were accepted as they surpassed the secret reserve price, generating overall revenues of 1,845.76 EUR for the seller. See Table 6 for the distribution of bid amounts and bid amounts by day of the experiment. Surprisingly, more than 30% of bidders overbid the secret reserve price by more than 50%. 27 participants bid 19.99 or 20.00 EUR, presumably because they wanted to have the products under any circumstances. We had a response rate of 43.5% for our post-experimental questionnaire.

To relate bidding behavior to an individual bidder’s position in the social network, we apply an eventbased approach as boundary specification strategy (Laumann et al. 1989) and examine partial networks: We remove all nodes and connecting edges symbolizing agents who did not participate in this secret reserve price auction. Thereby, we obtain an undirected network with 200 nodes (i.e., bidders that could be identified in the network data). We then use the bid dates to generate a directed information flow network (labeled “Network D”: see Figure 6): If A is a friend of B and A places a bid first, then first-hand information about the secret reserve price auction can only flow from A to B and not vice versa. B can then exploit this information for her bid whereas A is not allowed to bid again. Therefore, we have a directed information flow from A to B which we model by replacing the undirected link with a direct link from A to B in the network data. Bidding late thus leads to more access to information but the unknown end of the auction boosted the start of bidding.

Table 6 Descriptive Statistics of Bids

<table><tr><td colspan="2">Distribution of bid amounts</td><td colspan="3">Bid amounts by day</td></tr><tr><td>Bid amount (EUR)</td><td>No. of bids</td><td>Day</td><td>Mean bid amount (EUR)</td><td>No. of bids</td></tr><tr><td>0.00–4.99</td><td>50</td><td>2006-12-04</td><td>10.03</td><td>115</td></tr><tr><td>5.00–9.99</td><td>57</td><td>2006-12-05</td><td>9.27</td><td>37</td></tr><tr><td>10.00–14.99</td><td>55</td><td>2006-12-06</td><td>9.96</td><td>32</td></tr><tr><td>15.00–19.99</td><td>46</td><td>2006-12-07</td><td>10.98</td><td>32</td></tr><tr><td>20.00</td><td>20</td><td>2006-12-08</td><td>11.72</td><td>12</td></tr><tr><td>All</td><td>228</td><td>All</td><td>10.12</td><td>228</td></tr></table>

For the directed network D we assume that all nodes were willing to share and receive information. Even though this assumption is only a proxy, nodes with higher indegree (i.e., the number of incoming ties from other agents) should always have a higher probability to receive information and nodes with higher outdegree (i.e., the number of ties towards other agents) should have more possibilities to share their experience. Hence, our results should be stable, based on this assumption.

To test H1–H3, we calculate the degree centrality, betweenness centrality and clustering coefficient for all bidders of the directed network D and regress the absolute difference between their bid and the secret reserve price on these measures of their network position. Because the position in the network rather determines the bid’s deviation from the secret reserve price and bidding is very unlikely to influence the agent’s position in the network, we can assume a direct causality in this case.

Table 7 shows the regression results. The overall fit is significant and R-square is low but acceptable for such cross-sectional data. For all independent variables, variance inflation factors (VIFs) are well below 2, indicating that multicollinearity is not a problem. According to H1, we expect that the higher the degree centrality, i.e., the more contacts are involved in secret reserve price auctions, the better an agent can determine the secret reserve price owing to

Figure 6 Directed Network D Visualized with Pajek

![](/api/attachments/UK8ZZACN/fulltext/images/aa70265f4b6e0065cbd24de7a767e8ac910370223b13fc4d97caba9ad9c32dae.jpg)

the information flow. The degree centrality of a node has, however, no significant influence on the deviation of the bid from the secret reserve price, thus we find no support for H1. Hypothesis 2 posits that if an individual is connected to different parts of the network and, therefore, an intermediary or bridge with access to dispersed information (i.e., has a high betweenness centrality), he or she can better predict the secret reserve price than individuals with a low betweenness centrality. This result is highly significant for the directed network that incorporates the direction of information flow and therefore we find support for H2. The strength of weak ties, which are more likely to bridge different parts of the networks, has already been demonstrated by Granovetter (1973). The negative influence of betweenness centrality supports this stylized fact.

The clustering coefficient has a surprisingly significant positive influence on the bid’s deviation from the secret reserve price and hence contradicts our H3 (see Table 7). As already outlined by Granovetter (1974), cliques have many overlapping contacts. They all tend to know and interact with one another and so there is a tendency for them to possess the same information and knowledge. The information received is likely to be “stale” (Scott 2000). Our results indicate that information from the same cluster is not only stale, but even leads to a greater deviation of individual bids from the secret reserve price.

On the other hand, the clustering coefficient, which is especially high for bidders that are connected to a strong clique, significantly increases the deviation between bids and the secret reserve price, although it is an indicator of improved local cooperation.

Table 7 Influence of Social Position on Absolute Deviation from Secret Reserve Price

<table><tr><td>Regression</td><td>Parameter (standard error)</td></tr><tr><td>Constant</td><td>5.337 (0.307)**</td></tr><tr><td>Degree centrality</td><td>8.864 (16.100)</td></tr><tr><td>Betweenness centrality</td><td>-257.634 (129.264)*</td></tr><tr><td>Clustering coefficient</td><td>3.988 (1.989)*</td></tr><tr><td>R-square</td><td>0.047</td></tr><tr><td>F-test (p-value)</td><td>3.225 (0.024)</td></tr><tr><td>No. of obs.</td><td>200</td></tr></table>

Notes. Dependent variable: absolute difference between bid and the secret reserve price. Network measures based on information flow through directed network D. VIFs of independent variables <2.  
∗p < 0-05, $^ { * * } p < 0 . 0 1 .$

Interestingly, the clustering coefficient and betweenness centrality are not significantly correlated. There are several possible explanations for the influence of clustering on bidding behavior: We conjecture that many bids with the same amount within a clique may set an anchor or reference point, thus preventing bidders from adjusting away from this anchor (Tversky and Kahneman 1974). Another explanation is potentially isomorphic pressure in the cluster. Isomorphic pressure can be put into three distinct types—coercive, mimetic, and normative pressure (DiMaggio and Powell 1983). While coercive pressure is more important in organizational settings (see DiMaggio and Powell 1983), mimetic and normative pressure might influence individuals’ bidding behavior.

Mimetic pressure may cause agents to become more like other agents in the same position. Thus mimetic pressures act through structural equivalence (DiMaggio and Powell 1983). Normative pressures normally operate through interconnected relations. According to social contagion literature, agents with direct or indirect ties to other agents are likely to behave similarly (Burt 1987) and thus might have a homogeneous WTP that might lead to this effect. The counterintuitive effect of clustering on bidding behavior, however, opens avenues for future research because we cannot distinguish the ultimate reason for this effect with the available data.

Overall, the information diffusion in case of Habbo-Hotel was mainly limited to person-to-person communication because there were only very few threads on external message boards dealing with the secret reserve price auction at HabboHotel. The centrality measures also confirm a predominant personto-person communication, and, as long as subjects reading forums were randomly distributed, we might actually observe even stronger results in the absence of such message boards. The postexperimental questionnaire also showed that 18.2% of the bidders had knowledge about previously rejected and accepted bids and 23.5% of the bidders stated that they actively shared their experience in terms of bidding information. This closed system helped us, however, to isolate the effect of person-to-person communication and find a significant impact of an agent’s position in a social network on bidding behavior.

Taking into account that this offering at HabboHotel lasted fewer than five days, and that this was the first time that such a secret reserve price auction was applied there, the fraction of shared information is rather high. Especially at the beginning, information may be rather sparse in such a person-to-person network. For mature bidder communities the effect of information diffusion should thus be much stronger.

## 5. Discussion

We analyzed the impact of information diffusion on secret reserve price auctions. We developed an analytical model for the effect of shared information on bidding behavior and empirically tested the validity of the model in a laboratory experiment with induced valuations. We find that the value of information is influenced by two dimensions: amount of information and dispersion of information. We link these properties to positions in social networks by embedding economic behavior in social relationships: Bidders with many contacts are more likely to have access to a large amount of information, whereas bidders who are intermediaries between different parts of the network have access to dispersed information (“strength of weak ties”). We also find that bidders within a wellconnected clique and a high clustering coefficient suffer from the stale information that is available within the clique (“weakness of strong ties”). This is quite surprising and may result from anchoring effects or isomorphic pressures. A behavioral approach might offer additional explanation and is hence an opportunity for further research. Overall, our field study with real purchases is the first study that finds a significant impact of social position on bidding behavior and is consistent with Granovetter’s primacy of structure over motivation that has been found in sociology.

Our study has several limiting assumptions that can be used as avenues for future research. First, our methodological approach is normative. Behavioral aspects, however, such as information overload with regard to the received number of messages may influence bidding behavior. The latter can be one explanation why only a limited percentage of bidders use bulletin boards or communities for their information search. Additionally, bidders may exert free-riding behavior with regard to information they obtain but not spread, and bidders with high search cost may provide less information, which may reduce the overall value of information provided in bulletin boards or via person-to-person communication. Future research can analyze bidders’ incentives and motives to spread information. Furthermore, future studies can test seller strategies in laboratory or field experiments as well as agent-based simulation studies (as an example of such an approach see Bapna et al. 2003). Additionally, they may provide suggestion tools for bidders with regard to acceptable bids. In the case of suggestion tools, however, additional uncertainty with regard to the truth of the suggestions, similar to the provision of false information, may arise for bidders.

Our results have important implications for sellers and buyers in secret reserve price auctions. First, information diffusion in markets with secret reserve price auctions will enable potential buyers better to estimate sellers’ secret reserve prices, thus reducing bid dispersion and hence sellers’ ability to yield price discrimination amongst buyers. Second, on the basis of our findings, sellers may quantify the effect of information diffusion for different network structures amongst buyers. We found support for our hypothesis that information diffusion significantly depends on social structure amongst prospective buyers in such secret reserve price auctions. The effect of information diffusion differs between dense and not-so-well connected buyer networks. The case of communities like BetterBidding.com or BiddingForTravel.com with around 90,000 registered members (last visited 2008- 01-05 compared with 77,000 registered members in

March 2007) shows the imperative need to incorporate the impact of information diffusion in the optimal auction design.

Sellers conducting secret reserve price auctions might consider different strategies to encounter or accelerate information diffusion: First, the optimal setting of the secret reserve price can depend on the magnitude of information diffusion. Second, the provision of a forum can be beneficial for the seller when the bidders systematically underestimate the costs of the product and thus the secret reserve price. The additional communication can help to correct this false estimation and therefore increase sales, thus positively influencing seller profit and consumer surplus. Third, a seller might influence the usefulness of forums like BetterBidding.com by the provision of false information. This creates some uncertainty about the truthfulness of the available information and may reduce the effect of information diffusion. Such behavior has been reported in several other studies (Harmon 2004, Dellarocas 2006, Mayzlin 2006). The provision of false information is not, however, a valid option in more or less pure person-to-person communication as in our case of the HabboHotel.

Although the context of our study is information diffusion about secret reserve price auctions in a social network, our methodology and study design might provide beneficial insights and implications for the spread of product information (word-of-mouth and buzz) through social networks within and outside virtual worlds. Data on social networks are available in many Web2.0-communities (e.g., Facebook, LinkedIn) or in companies, and might help decision-makers to identify suitable multipliers. Our results indicate that bridging agents in social networks especially foster information diffusion.

## 6. Conclusion

Digital networks have enabled new business models and new pricing mechanisms owing to lower transaction and menu costs. On the other hand, consumers’ social networks have on average expanded, by using digital technology to facilitate communication and to participate in additional social networks such as online communities. Both developments have very interesting and countervailing effects on consumers’ use of new pricing mechanisms and the performance of the related business models as shown in our study. The magnitude of these effects indicates that online sellers have to account for the social interaction among their consumers to sustain their business models. Furthermore, insights into the structure of social networks can help to create new models of consumer behavior and improve predictions of market performance.

Virtual worlds such as HabboHotel or SecondLife offer a unique setting for controlled experiments because researchers can control for information diffusion to a certain degree, and the real purchases in these experiments offer high external validity. While laboratory experiments offer maximum control where effects can easily be attributed to the manipulation treatments, external validity may be low. Field data, in contrast, offer high external validity but it may be hard to isolate effects. Experiments in virtual worlds can therefore close this gap and stimulate research in many domains. While experiments in virtual worlds, where subjects’ decisions have economic consequences for them, appear to be incentive-aligned, it remains an open question if actors make different decisions (for their avatars) in a virtual world than (for themselves) in the real world. Many more interesting studies in these virtual worlds remain to be conducted.

## Acknowledgments

The authors gratefully acknowledge the support from Sulake Germany and Torsten Jüngling as well as many helpful comments from Bernd Skiera, Ju-Young Kim, Christophe van den Bulte, Kristin Diehl, Arina Soukhoroukova, Martin Bernhardt, and Eva Gerstmeier. In addition, the special issue senior editors, the three referees, and the participants in the ISR special issue workshop provided the authors with many helpful suggestions. This research is supported by the German Federal Ministry of Education and Research under Grant No. 01AK706A.

## Appendix. Experimental Instructions (Study 1)

## Information Given to Participants

First, you receive a code that can be used to log in. Do not close the browser during the experiment and do not use the back button. Furthermore, it is prohibited to use any other program during the experiment.

You have the opportunity to hypothetically buy a total number of 14 products. You do not compete with the other bidders because the product is sold using a secret reserve price auction with you as the only bidder. In such a mechanism the seller sets a secret reserve price. As a prospective buyer you get the product for your bid amount stated when the bid hits or surpasses this secret reserve price but you can only bid once per product.

During the bidding process, you can receive information about previous bids for the same product you currently can bid for. These messages can provide clues for your bidding decision. Additionally, you see a lower and an upper bound for the secret reserve price that can help you with your bidding decision.

Bidding in any round is independent from the result of the preceding rounds.

How can you earn money? At the beginning of each round you receive information about the resale value of the product. If you manage to buy the product for less, you can keep the remainder multiplied with a payoff factor as personal bargain. You can collect your personal bargain in cash in two weeks and will be notified via email.

## References

Avery, C., P. Resnick, R. Zeckhauser. 1999. The market for evalua tions. Amer. Econom. Rev. 89(3) 564–584.

Bajari, P., A. Hortaçsu. 2004. Economic insights from Internet auctions. J. Econom. Literature 42(2) 457–486.

Bapna, R., P. Goes, A. Gupta. 2003. Replicating online Yankee auctions to analyze auctioneers’ and bidders’ strategies. Inform. Systems Res. 14(3) 244–268.

Bapna, R., P. Goes, A. Gupta, Y. Jin. 2004. User heterogeneity and its impact on electronic auction market design: An empirical exploration. MIS Quart. 28(1) 21–43.

Barabasi, A.-L., E. Bonabeau. 2003. Scale-free networks. Sci. Amer. 288(5) 50–59.

Bichler, M., J. Kalagnanam. 2006. A non-parametric estimator for reserve prices in procurement auctions. Inform. Tech. Management 7(3) 157–169.

Burt, R. 1987. Social contagion and innovation: Cohesion versus structural equivalence. Amer. J. Sociol. 92(6) 1257–1335.

Burt, R. 1992. Social structure of competition. N. Nohria, R. Eccles, eds. Networks and Organizations: Structure Form, and Action. Harvard Business School Press, Boston, 57–91.

Butler, B. 2001. Membership size, communication activity, and sustainability: A resource-based model of online social structures. Inform. Systems Res. 13(4) 346–365.

Chatterjee, R., J. Eliashberg. 1990. The innovation diffusion process in a heterogeneous population: A micromodeling approach. Management Sci. 36(9) 1057–1079.

Chernev, A. 2003. Reverse pricing and online price elicitation strategies in consumer choice. J. Consumer Psych. 13(1/2) 51–62.

Chevalier, J., D. Mayzlin. 2006. The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3) 345–354.

Chwe, M. S.-Y. 2000. Communication and coordination in social networks. Rev. Econom. Stud. 67(230) 1–16.

Constant, D., S. Kiesler, L. Sproull. 1994. What’s mine is ours, or is it? A study of attitudes about information sharing. Inform. Systems Res. 5(4) 400–421.

Dellarocas, C. 2003. The digitization of word-of-mouth: Promise and challenges of online reputation systems. Management Sci. 49(10) 1407–1424.

Dellarocas, C. 2006. Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10) 1577–1593.

DiMaggio, P., W. Powell. 1983. The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. Amer. Sociol. Rev. 48(2) 147–160.

Ding, M., J, Eliashberg, J. Huber, R. Saini. 2005. Emotional bidders— An analytical and experimental examination of consumers behavior in a priceline-like reverse auction. Management Sci. 51(3) 352–364.

Fay, S. 2004. Partial repeat bidding in the name-your-own-price channel. Marketing Sci. 23(3) 407–418.

Freeman, L. C. 1977. A set of measures of centrality based on betweenness. Sociometry 40(1) 35–41.

Freeman, L. C. 1979. Centrality in social networks: I. Conceptual clarification. Soc. Networks 1(3) 215–239.

Godes, D., D. Mayzlin. 2004. Using online conversations to study word of mouth communication. Marketing Sci. 23(4) 545–560.

Granitz, N., J. Ward. 1996. Virtual community: A sociocognitive analysis. Adv. Consumer Res. 23(1) 161–166.

Granovetter, M. 1973. The strength of weak ties. Amer. J. Sociol. 78(6) 1360–1380.

Granovetter, M. 1974. Getting a Job. Harvard University Press, Cambridge, MA.

Granovetter, M. 1985. Economic action and social structure: The problem of embeddedness. Amer. J. Sociol. 91(3) 481–510.

Hann, I.-H., C. Terwiesch. 2003. Measuring the frictional costs of online transactions: The case of a name-your-own-price channel. Management Sci. 49(11) 1563–1579.

Harmon, A. 2004. Amazon glitch unmasks war of reviewers. The New York Times (February 14), New York.

Hayek, F. A. v. 1945. The use of knowledge in society. Amer. Econom. Rev. 35(4) 519–530.

Isaac, R. M., J. M. Walker. 1985. Information and conspiracy in sealed bid auctions. J. Econom. Behav. Organ. 6(2) 139–159.

Jones, Q., G. Ravid, S. Rafaeli. 2004. Information overload and the message dynamics of online interaction spaces: A theoretical model and empirical exploration. Inform. Systems Res. 15(2) 194–210.

Kannan, P. K., P. K. Kopalle. 2001. Dynamic pricing on the Internet: Importance and implications for consumer behavior. Internat. J. Electronic Commerce 5(3) 63–83.

Klemperer, P. 2002. What really matters in auction design. J. Econom. Perspectives 16(1) 169–189.

Kwasnica, A. M. 2000. The choice of cooperative strategies in sealed bid auctions. J. Econom. Behav. Organ. 42(3) 323–346.

Laumann, E. O., P. V. Marsden, D. Prensky. 1989. The boundary specification problem in network analysis. L. C. Freeman, D. R. White, A. K. Rommey, eds. Research Methods in Social Network Analysis. Mason University Press, Fairfax, VA, 61–87.

Marsden, P. V. 1990. Network data and measurement. Annual Rev. Sociol. 16 435–463.

Mayzlin, D. 2006. Promotional chat on the Internet. Marketing Sci. 25(2) 155–163.

McCall, J. J. 1970. Economics of information and job search. Quart. J. Econom. 84(1) 113–126.

Milgrom, P. R., R. J. Weber. 1982. A theory of auctions and competitive bidding. Econometrica 50(5) 1089–1122.

Phillips, O. R., D. J. Menkhaus, K. T. Coatney. 2003. Collusive practices in repeated english auctions: Experimental evidence on bidding rings. Amer. Econom. Rev. 93(3) 965–979.

Pinker, E. J., A. Seidmann, A. Y. Vakrakt. 2003. Managing online auctions: Current business and research issues. Management Sci. 49(11) 1457–1484.

Putsis, W., S. Balasubramanian, E. Kaplan, S. Sen. 1997. Mixing behavior in cross-country diffusion. Marketing Sci. 16(4) 354–369.

Reiley, D. H. 2006. Field experiments on the effects of reserve prices in auctions: More magic on the Internet. RAND J. Econom. 37(1) 195–211.

Scott, J. 2000. Social Network Analysis: A Handbook, 2nd ed. Sage Publications, London.

Smith, V. L. 1976. Experimental economics: Induced value theory. Amer. Econom. Rev. 66(2) 274–279.

Spann, M., G. J. Tellis. 2006. Does the Internet promote better consumer decisions? The case of name-your-own-price auctions. J. Marketing 70(1) 65–78.

Spann, M., B. Skiera, B. Schäfers. 2004. Measuring individual frictional costs and willingness-to-pay via name-your-own-price mechanisms. J. Interactive Marketing 18(4) 22–36.

Stigler, G. J. 1961. The economics of information. J. Political Econom. 69(3) 213–225.

Stigler, G. J. 1962. Information in the labor market. J. Political Econom. 70(5) 94–105.

Terwiesch, C., S. Savin, I.-H. Hann. 2005. Online haggling and price-discrimination in a name-your-own-price channel. Management Sci. 51(3) 339–351.

Tversky, A., D. Kahneman. 1974. Judgment and uncertainty: Heuristics and biases. Science 185(4157) 1124–1131.

Watts, D. J., S. H. Strogartz. 1998. Collective dynamics of smallworld networks. Nature 393(6684) 440–442.
