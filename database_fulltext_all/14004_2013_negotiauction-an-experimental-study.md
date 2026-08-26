---
otero_id: 14004
otero_key: "YBUCG6CU"
title: "NegotiAuction: An experimental study"
authors: "Long Pham; Alexander Zaitsev; Robert Steiner; Jeffrey E. Teich"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.06.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Long Pham <sup>a,b,</sup>⁎, Alexander Zaitsev <sup>c,1</sup>, Robert Steiner <sup>d,2</sup>, Jeffrey E. Teich <sup>e,3</sup>

<sup>a</sup> Department of Business Administration, College of Business, Minot State University, 500 University Ave W, Minot, ND 58707, United States

<sup>b</sup> School of Banking and Finance, National Economics University, Hanoi, Vietnam

<sup>c</sup> Moscow State University, Russia

<sup>d</sup> Department of Applied Statistics, College of Business, New Mexico State University, MSC 3CQ, P.O. Box 30001, Las Cruces, NM 88003-8001, United States

<sup>e</sup> Department of Management, College of Business, New Mexico State University, MSC 3DJ, P.O. Box 30001, Las Cruces, NM 88003-8001, United States

## a r t i c l e i n f o

Article history: Received 8 May 2012 Received in revised form 18 June 2013 Accepted 26 June 2013 Available online 10 July 2013

Keywords: Negotiation Auction NegotiAuction Hybrid

## a b s t r a c t

We investigated and compared economic performance of auction, negotiation and hybrid mechanisms of the NegotiAuction software. With the auction mechanism, bidders are required to submit bids consisting of quantity needed and other relevant non-price attributes, then they are returned with suggested prices to make them active. With the negotiation mechanism, the requested price button is turned off and the auction owner and the bidder are free to negotiate on one-on-one basis with other issues besides price and quantity. With the hybrid mechanism, characteristics of both negotiation and auction are combined. Twelve hypotheses involving economic performance measures were tested. On many measures, the hybrid mechanism was best for the auction owners.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Negotiation is viewed as a rich and ill-de<sup>fi</sup>ned family of exchange mechanisms. Negotiation can be utilized for exchanging goods/services among buyers and sellers and solving inter-personal and interorganizational con<sup>fl</sup>icts [31]. In other words, negotiation is considered as a decision making process based on continuous communication between two or more participants whose objectives cannot be obtained via unilateral actions [6].

Negotiations are different in terms of degree of their structuredness, possibility of modi<sup>fi</sup>cation, and participation rules [6,39]. The interaction process in negotiations may not be established in advance and the negotiation rules may be elicited in an implicit manner (based on tradition), especially for many face-to-face negotiations [36].

Recently, the Internet has been emerging as an important channel for business transactions including e-negotiations [41]. As a matter of fact, many negotiations have been carried out electronically in e-commerce and e-business. Furthermore, many applications of computer and information technologies have been applied in attempts to make favorable conditions for negotiations, aid human negotiators, and facilitate software agent collaboration as well, such as MIT Deep Ocean Mining model and IIASA RAINS model (for further information, see [21]). In today's business arena, characterized by interdependence and constant changes, negotiations are indispensable for businesses with respect to time and effort spent for them [26]. Thus, systems based on computer power have an important role in upgrading negotiation ef<sup>fi</sup>ciency and effectiveness that are likely to have keen effects on negotiation outcomes of organizations and individuals (see [21] and cybersettle.com for further information on negotiation support and e-negotiation systems).

Besides negotiations, auctions are a market mechanism initially introduced in the ancient world. The word auction has its root in the Latin language that can be understood as “go up” [30]. Under the traditional perspective, auctions are viewed as economic mechanisms to <sup>fi</sup>nd prices for assets that are not placed on traditional markets for transactions and that have very unique and/or rare characteristics that are very dif<sup>fi</sup>cult in determining the suitable prices on traditional markets. An auction brings about a forum that can be considered a marketplace where potential bidders can gather.

McAfee and McMillan [30] classi<sup>fi</sup>ed various types of auctions into four distinct groups: The English auction, the Dutch auction, the <sup>fi</sup>rst price sealed bid auction, and the second price sealed bid auction.

English auctions or forward auctions are described as economic mechanisms where bidders can attend to openly compete with each other to have opportunities to buy an asset. The bidder who values the asset the most will become the winner. It should be noted that when the auction comes into the end, the <sup>fi</sup>nal price is not necessarily the true market price but the <sup>fi</sup>nal valuation for the asset auctioned that is expected to be close to the true market value [30].

Dutch auctions are viewed as descending auctions where bidders compete in a downward direction until the auction comes into the end. The asset is sold to the bidder who is <sup>fi</sup>rst to stop the clock at the close of the auction. It should be noted that the <sup>fi</sup>nal price is not necessarily the true market price but the <sup>fi</sup>nal valuation of the item auctioned that is expected to be close to the true market price [30].

In a <sup>fi</sup>rst price sealed bid auction, bidders submit their best bids only one time to the seller in a sealed envelope. All of these bids will be opened at the same time. In ascending auctions, the highest bidder is awarded the asset while in reverse auctions the lowest bidder is awarded the contract. First price sealed bid auctions do not provide bidders any opportunity to see bids of their competitors, make changes in their reserve prices, or resubmit new bids. The winning bidder is required to pay the amount submitted in his or her bid to the seller. First price sealed bid auctions are often utilized in governmental procurements [30].

The second price sealed bid auction is known as the Vickrey auction (named after its developer in economics). Vickrey [46] discussed this kind of auction that share many common characteristics with the <sup>fi</sup>rst price sealed bid auction except for one distinct aspect. Depending on the situations (forward or reverse), the winning bidder is the one who has the highest or lowest bid, he or she has to pay or receive the amount listed on the bid of the second highest bidder.

Online reverse auctions have been used by a number of Fortune 1000 companies as a tool to drive down the price of purchased products and services [13]. Emiliani [12] simply de<sup>fi</sup>nes that business-to-business online auctions are downward pricing and hence reversed. Smeltzer and Carr [37] argue that the reverse auction is a price-decreasing format. Jap [19] de<sup>fi</sup>nes reverse auctions as declining price auctions where sellers bid instead of the buyer (forward) auctions. Parente et al. [32] suggest that the difference lies in the number of buyers and sellers, whereas reverse auctions have one buyer and many sellers.

Online reverse auctions can bring about bene<sup>fi</sup>ts for not only buyers but also suppliers. Via online reverse auctions, suppliers can gain market information, create new markets for better excess capacity management, and attract new customers from their competitors.

Besides these above-mentioned bene<sup>fi</sup>ts that online reverse auctions can bring about, concerns relating to online reverse auction adoption and usage have been pointed out [43]. One of the major concerns is that online reverse auctions only concentrate on the interests of the buyer while ignoring that of the suppliers. It is likely that long-term relationships between buyer and supplier can be destroyed if the <sup>fi</sup>nal price is the only priority of the buyer and if winner determination procedures through the auctions are biased towards the buyer [20].

Although both negotiations and auctions are viewed as two primary market mechanisms to sell and/or buy goods/services, theories on them have limitations and they are often investigated in isolation [40]. In negotiations, the main source of competitive pressure comes from the across-the-table dynamics. In contrast, in auctions, the competitive pressure comes primarily from the same-side-of-the-table dynamics. The point here is that most real world situations include aspects of both the same-side-of-the-table competition and the across-the-table competition [40].

In addition, a comparison between auctions and negotiations based on multi-attributes besides the price has not yet been undertaken (except for [9]). It is obvious that ignoring other attributes besides price is very likely to erase the applicability of economics in the <sup>fi</sup>eld of procurement and other settings in which the product/service speci<sup>fi</sup>cations are not made at the outset. In spite of the fact that advancements and improvements have been made in the area of multi-attribute auctions, comprehensive comparisons between negotiations and auctions based on multi-attributes besides price are still missing.

Studies and practical evidence seem to support the superiority of hybrid mechanisms over only negotiation mechanisms or only auction mechanisms in the context of selling goods/services. One of the reasons for the growing interest in these hybrid environments is their increasing utilization by successful internet auction sites like eBay (www. ebay.com), Yahoo (www.yahoo.com), and QXL (www.qxl.com)

[11,29]. These sites provide sellers with an opportunity to sell their products at a <sup>fi</sup>xed price right before or during the auction [35].

Hybrid mechanisms can be conducted in the forms of negotiation– auction sequences or auction–negotiation sequences [1,18,48], or even by following the form speci<sup>fi</sup>ed by Teich et al. [42] that the auction owner can participate in negotiations at any time she wants during the auction process, or stated another way there are no <sup>fi</sup>xed sequences of negotiation–auction or auction–negotiation.

The objectives of this study under the setting of multi-attribute online reverse auctions/negotiations are as follows:

1. To compare allocational ef<sup>fi</sup>ciency among three different exchange mechanisms — negotiation, auction, and the hybrid mechanism.

2. To compare Pareto ef<sup>fi</sup>ciency among the three different mechanisms.

3. To compare cost savings earned by buyer and pro<sup>fi</sup>ts earned by suppliers among the three different mechanisms.

In Section 2, we provide the research hypotheses. Section 3 provides the methodology for this research. Section 4 presents the results while Section 5 presents implications, limitations and directions for future research.

## 2. Research hypotheses

Auctions are considered a class of market mechanism with an explicit set of rules for determining the goods/services allocation between sellers and buyers [30,33,34]. Auctions can be constructed in the form of either single-sided (one seller auctions off goods to a number of bidders or one buyer can buy goods from a number of suppliers) or double-sided (competition takes place from both sides of a market). Recently, auctions with various designs have been commonly utilized to allocate a variety of products/services such as securities, offshore mineral rights, and emission certi<sup>fi</sup>cates [28,47].

Research conducted by economists on negotiation and auction mechanisms can be found in several theoretical studies on single and multi-attribute negotiations and auctions. Interestingly, the empirical research provides no clear answer as to the superiority of one mechanism over the other.

With respect to theoretical comparisons, Bulow and Klemperer [8] have shown that a simple English auction with N + 1 bidders always generated higher revenue than a negotiation with N participants. This implication is only valid if a number of assumptions are not violated (for example, attribute preference independence).

Kirkegaard [22] argued that seller–offer bargaining is more advantageous than an English auction when demand is discrete (<sup>fi</sup>nite space or the seller releases only partial information such that each buyer will learn only that his valuation is in one of a <sup>fi</sup>nite set of intervals) and the buyers are patient. In such situations, sellers prefer a bargaining protocol over an English auction. In addition, Kirkegaard [22] proved that when demand is continuous (the seller releases all his information to a given buyer), an English auction could be improved by some kind of pre-negotiation.

Thomas and Wilson [44,45] implemented two experimental studies where online reverse auctions were compared with multi-bilateral negotiations. Based on their laboratory experiments, they showed that the superiority of auctions argued by Bulow and Klemperer [8] was not supported by the empirical data. In multi-bilateral negotiations, a buyer solicited price offers from multiple sellers and then requested more favorable offers from the sellers who needed to compete against each other. In their <sup>fi</sup>rst experiment, Thomas and Wilson [44] realized that multi-bilateral negotiations with two sellers generated higher prices than <sup>fi</sup>rst-price sealed bid auctions for inexperienced buyers and sellers. However, both mechanisms proved to be outcome-equivalent in the experiment with four sellers. In addition, Thomas and Wilson [45] recognized that the prices in second price sealed bid auctions were higher than the prices created in multi-bilateral negotiations. Such <sup>fi</sup>ndings indicated that this auction mechanism was inef<sup>fi</sup>cient in the given experimental setting. Note that the two aforementioned studies compared auctions and negotiations only based on price.

Bajari, McMillan and Tadelis [3] empirically analyzed auctions and negotiations that had taken place in the construction industry. They observed that 43% building contracts in Northern California were procured via utilizing negotiations, while 18% were procured via utilizing auctions, and the rest could be in the form of contract procurement at a <sup>fi</sup>xed price or some other kinds of mechanism. They went further to argue that the selection of the exchange mechanism depended on the knowledge and complexity of the context and task (product). In their opinion, advantages could be realized by utilizing negotiations if the product speci<sup>fi</sup>cations traded were not well-de<sup>fi</sup>ned a priori, which was often the case in this industry. Unlike auctions, negotiations made favorable conditions for buyers and sellers to discuss and clarify the product speci<sup>fi</sup>cations. Their <sup>fi</sup>ndings showed that auctions performed poorly in terms of ef<sup>fi</sup>ciency if changes in the product design occurred after the transaction took place. In the same vein, Lef<sup>fl</sup>er et al. [25] gathered data from private sales of timber tracts in North Carolina. They observed that about half of the 360 contracts they analyzed were auctioned and the other half were negotiated. They also refer to the Goldberg [15] and to the Bajari and Tadelis [2] predictions on the effects of complexity and showed a positive relationship between their measures of complexity and the use of negotiated contracts. Bonaccorsi et al. [7] offered an empirical analysis of auctions versus bargaining as alternative procurement mechanisms using data on the procurement of medical devices by Italian hospitals. In their study, a hypothesis that quality concerns would in<sup>fl</sup>uence the choice of award mechanisms was tested by considering variations in which part of the hospital was directly in charge of procuring the devices, administrators, who were more concerned with costs, or medical personnel, who were more concerned with quality. Finally, they con<sup>fi</sup>rmed this hypothesis.

All of the above research only refers to single issue auction/negotiation mechanisms with the inconsistent results in terms of which mechanism (auction or negotiation) is better than the other. A comparison between auctions and negotiations based on multiattributes besides price has not yet been undertaken (except for [9]), although there have been some studies conducted to compare multi-attribute auctions under different information revelations (e.g., [4,5,10,16,23,38]).

It should be noted that complex (multi-attribute) negotiation tasks require substantial cognitive efforts and is very likely to result in suboptimal outcomes due to people's cognitive limitations, their lack of interest in highly complex transactions, and their involvement with many competitive activities [17]. Furthermore, Chen et al. [9] conclude from an experimental study that multi-attribute negotiations are no better than Multiple Attribute Online Reverse Auctions (MAORAs), and MAORAs require less effort than multi-attribute negotiations. Thus, in this study, we hypothesize that

H1. Allocational ef<sup>fi</sup>ciency is better in auctions than in negotiations.

H2. Pareto ef<sup>fi</sup>ciency is better in auctions than in negotiations.

H3. Cost savings earned by buyers are higher in auctions than in negotiations.

H4. Pro<sup>fi</sup>ts earned by suppliers are higher in auctions than in negotiations.

Allocational ef<sup>fi</sup>ciency measures the extent to which the goods/ services are allocated to a set of bidders who, in combination, maximize the social welfare. Pareto ef<sup>fi</sup>ciency can be interpreted from the perspective of the auction owner/bidder dyads or from the group as a whole. The approach used to represent buyer's preferences over multiple issues will determine whether the result is Pareto optimal for the dyads. If all dyads are Pareto optimal, it should follow that the group as a whole is also Pareto optimal, although this conjecture has yet to be proven.

A hybrid mechanism is a mechanism combining characteristics of both auctions and negotiations [42]. Ivanova-Stenzel and Kroger [18] examined behavior in a hybrid mechanism where a seller <sup>fi</sup>rst negotiated with one potential buyer about the price of a good. If the negotiation failed to produce a sale, a second-price sealed-bid auction with an additional buyer was conducted. The theoretical model predicted that with risk neutral agents, all sales took place in the auction rendering the negotiation prior to the auction as obsolete. An experimental test of the model provided evidence that average prices and pro<sup>fi</sup>ts were quite precisely predicted by the theoretical benchmark. However, a signi<sup>fi</sup>- cant number of sales occurred already during the negotiation stage. The authors showed that allowing for individual heterogeneity in risk preferences could theoretically account for the existence of sales during the negotiation stage and improve the <sup>fi</sup>t for buyers' behavior, but was not suf<sup>fi</sup>cient to explain sellers' decisions.

Ye [48] contended that in auctions with costly entry, the entry process matters. The author compared expected revenues generated by different entry processes. It was shown that an auction with deterministic entry (exactly n potential bidders entered the auction and exactly (N − n) potential bidders stayed out) usually generated more expected revenue than that with stochastic entry (potential bidders were randomized). Thus in<sup>fl</sup>uencing the entry process by reducing the randomness of participation was to the seller's bene<sup>fi</sup>t. Based on this insight, the author analyzed a hybrid mechanism combining both auction and negotiation elements, in which a sole buyer was selected from a forward auction process, followed by a negotiation stage. The author showed that such a hybrid mechanism generated higher expected revenue than the one-stage standard auction, as long as the number of potential buyers was suf<sup>fi</sup>ciently large. In addition, Levin and Ye [27] examined a generalized hybrid auction in a simple model with af<sup>fi</sup>liated private values and risk averse bidders. The authors showed that the hybrid auctions generated higher expected revenue than the standard English ascending auction, and the optimal hybrid auction was characterized by an optimal number of ascending-bid stages. The results suggested that the revenue-maximizing auctions should optimally balance the bene<sup>fi</sup>t of information extraction in the ascending-bid phase with the cost of reduced competition in the sealed-bid phase.

According to Aktas, Bodl and Roll [1], observable (ex-post) competition in the merger and acquisition (M&A) markets seemed to be very low. In their study, they focused on the role of ex-ante competition and showed that, when this was taken into account, the M&A market was more competitive than it seemed at <sup>fi</sup>rst sight. The authors <sup>fi</sup>rst provided a theoretical analysis where they modeled takeovers as a two-stage process. The initial stage corresponded to a one-to-one negotiation with the target. If the negotiation failed, there was a second stage in which either a takeover battle among rivals occurred, or the target <sup>fi</sup>rm organized a competitive auction. One of the main empirical predictions was that the higher the anticipated competition in the second stage, the higher the bid offered in the <sup>fi</sup>rst stage. The authors then provided an empirical test of this prediction using a dataset of friendly deals for which, by construction, no ex-post competition was observable. The authors used the deal frequency in a given industry as a proxy for ex-ante competition, and showed that this variable was negatively related to the share of the value creation kept by the acquirer. This result was signi<sup>fi</sup>cant even taking into account evidence of a decreasing investment opportunity. The main conclusion that the authors could draw from the analysis was that the M&A market was fairly competitive and that anticipated competition allowed target shareholders to receive a reasonable premium even in friendly deals.

Studies and practical evidence seem to support the superiority of hybrid mechanisms over only negotiation mechanisms or only auction mechanisms in the context of selling goods/services. Thus, the following hypotheses are also to be tested in the procurement setting:

H5. Allocational ef<sup>fi</sup>ciency is better in hybrid mechanisms than in auctions.

H6. Pareto ef<sup>fi</sup>ciency is better in hybrid mechanisms than in auctions.

H7. Cost savings earned by buyers are higher in hybrid mechanisms than in auctions.

H8. Pro<sup>fi</sup>ts earned by suppliers are higher in hybrid mechanisms than in auctions.

H9. Allocational ef<sup>fi</sup>ciency is better in hybrid mechanisms than in negotiations.

H10. Pareto ef<sup>fi</sup>ciency is better in hybrid mechanisms than in negotiations.

H11. Cost savings earned by buyers are higher in hybrid mechanisms than in negotiations.

H12. Pro<sup>fi</sup>ts earned by suppliers are higher in hybrid mechanisms than in negotiations.

## 3. Methodology

## 3.1. The NegotiAuction system

The NegotiAuction system has been devised by Teich et al. [42] which serves as a setting where the research hypotheses are tested. The main characteristics of the NegotiAuction system are as follows (for further information, and screenshots of the system, read Teich et al. [42]).

1. Negotiable Bid Issues (NBIs) and Bidder Attributes (BAs) are used to take multiple issues into consideration with the purpose of differentiating among bidders:

a. Negotiable Bid Issues: These are issues other than price and quantity included in the actual bid. Discounts/bonuses can be used for different levels of such issues. For example, a warranty level of 3 years with a bonus of \$0 and a warranty level of 4 years with a bonus of \$5 per unit, and so on.

b. Bidder attributes: Information on bidders (characteristics of bidders). For example, bidders are ISO certi<sup>fi</sup>ed or not.

2. Scoring, rating and ranking of bidders. Bid premiums (or penalties) can be used to discriminate among bidders, without their knowledge.

3. A variety of constraints can be set up such as limits on quantity for each bidder or a group of bidders, limits on Negotiable Bid Issues, and so on. The simplex algorithm is used so that all the constraints are met and cost minimization for the auction owner is achieved. The algorithm enables the system to make suggested bids to the suppliers to make their bid active in real time.

4. Three modes of the system are:

a. Auto Mode (the auction mechanism): Prices are suggested by the system to the bidders to make them active.

b. Manual Mode (the negotiation mechanism): By using this mode, negotiations between the auction owner and the bidder can be carried out one-on-one during the event.

c. Hybrid Mode: Some bidders are in Auto Mode at the same time that other bidders are in Manual Mode.

It should be noted that the system also has Pause Mode where bidders can be put on a hold state during the event. However, in this paper, we are not interested in this mode but Auto Mode, Manual Mode and Hybrid Mode.

With Auto Mode, prices are suggested by the system to the bidders based on the reserve price and previous bids, NBI discounts/bonuses, bid premiums, and the bid increment, subject to the constraints [42,43]. Thus, Auto Mode is considered the auction mechanism where the suggested prices make bidders active. If the auction comes to the end while a bidder has an active bid, she will be awarded the full quantity speci<sup>fi</sup>ed in her bid. If her bid state is semi-active at the end of the auction, she will be awarded a partial quantity. If her bid state is inactive, she will not be awarded anything. In Auto Mode (the auction mechanism), bidders' bid status is always explicitly shown after the bids have been submitted. This can be considered an advantage to the bidder over a traditional negotiation due to the fact that she always knows where she stands, and what bid she should make to become active. Another advantage is that bids, as an optimal default feature, are semi-sealed (only the auction owner can see all the bids from all bidders), so there is no need for the bidders to be concerned about the fact that their rivals exploit too much information on their proprietary pricing information. That is why Auto Mode can be considered an absolutely full information revelation policy in the eyes of bidders since the bidders are only required to submit bids consisting of quantity needed and other relevant non-price attributes, then they are returned with suggested prices to make them active.

However, in contrast to Auto Mode, in Manual Mode (the negotiation mechanism), the explicit constraints, NBI discounts and bid premiums are not necessarily utilized. The request price button is turned off and the auction owner and the bidder are free to negotiate on a one-on-one basis. The advantage to the bidder is that she can engage the Auction Owner (AO) in a discussion to make her bid look attractive, perhaps by including new issues. She also bene<sup>fi</sup>ts from the possibility that the AO can be encouraged to lock in the bid. The disadvantage to the bidder is that she has even less information regarding her bid than in Auto Mode. The auction owner may de<sup>fl</sup>ate the price to make the bidder active.

The advantage to the AO is that she has complete freedom to negotiate and include new issues. A disadvantage to the AO is that it takes more time to negotiate, especially with many bidders at the same time as compared to simply leaving them in Auto Mode. It should be noted that complex (multi-attribute) negotiation tasks require substantial cognitive efforts and is very likely to result in suboptimal outcomes due to people's cognitive limitations, their lack of interest in highly complex transactions, and their involvement with many competitive activities [17].

The third mode in the NegotiAuction system is Hybrid Mode (hybrid mechanism) that consists of characteristics of both Auto Mode (the auction mechanism) and Manual Mode (the negotiation mechanism). Negotiations can bring about much <sup>fl</sup>exibility for discriminating among the suppliers while auctions treat the suppliers equally (although they are subject to price discrimination using penalties called “bid premiums” which are based on the bidder attributes and/or the ranking of bidders) and create more competition among them.

## 3.2. Experimental design

A buyer (bid-taker, auctioneer) wants to buy a given quantity of an item (a kind of laptop) from exactly six potential suppliers (bidders), ${ \mathrm { i } } \in { \mathrm { I } } = ( 1 , . . . , \ 6 )$ . This situation refers to multiple sourcing (meaning that a set of suppliers can be selected as winning suppliers) and occurs frequently in the corporate e-procurement setting. Specifically, we are presenting an experiment where the buyer makes an announcement that she would like to acquire a given quantity (100 units) of the item and asks invited suppliers to submit their bids based on three negotiable attributes of the item: the price p, the quantity q, and the warranty w. The non-price attribute is the warranty (the lowest and highest levels of this attribute are set up to make sure that they are in the range of acceptable levels). This non-price attribute can take on a discrete level from a set of ten levels: $\mathsf { w } \in \mathsf { W } = ( 1 , 2 , 3 , . . . , 1 0 )$ . Such attribute levels have discrete values in order to make the bidding process manageable. The price p is a nonnegative integer: $\mathsf { p } \in \mathsf { P } . { \mathsf { A } }$ bid b consists of three dimensions including a price suggested to make a bidder active: b = (p, q, $\mathsf { w } ) \in \mathsf { P } * \mathrm { Q } * \mathsf { W }$ . In the view of the buyer, if other things are kept constant, the buyer prefers better levels in the non-price attribute. That is why the buyer is very likely to set up good levels of the non-price attribute, but does not absolutely require the perfect level. In the experiment, the buyer's value function v: W → R is increasing with respect to w. Moreover, the buyer trades off price for levels of the non-price attribute. The buyer demands a lower price for a lower level and is willing to pay a higher price for a better level. In the experiment, the buyer's value function is given as $\mathsf { s } ( \mathsf { w } , \mathsf { p } ) = \mathsf { v } ( \mathsf { w } ) - \mathsf { p } .$

Each supplier (bidder) has an initial technology, knowledge and commodity endowment adequate to produce any technical speci<sup>fi</sup>cation in the set of feasible technical speci<sup>fi</sup>cations. The suppliers' initial endowments are <sup>fi</sup>xed throughout the bidding process. A supplier i's production cost function ${ \mathfrak { c } } _ { \mathrm { i } } \colon { \mathsf { W } } \to { \mathsf { R } } , { \mathrm { i } } = 1 , . . . , 6$ is increasing with respect to w. The better the level of the non-price attribute, the more additional costs each supplier incurs. This presents production settings in which costs of providing better levels of the non-price attribute increase proportionally with the better levels. In the experiment, supplier i's pro<sup>fi</sup>t is given as $\mathtt { U } _ { \mathrm { i } } ( \mathtt { W } , \mathtt { p } ) = \mathtt { p } _ { \mathrm { i } } - \mathtt { c } _ { \mathrm { i } } ( \mathtt { W } )$ if supplier i sells a given quantity of the item; or 0, otherwise.

In the experiment, a multi-attribute online reverse auction is examined. Such an auction allows an iterative bidding procedure where each bidder is eligible to submit subsequent bids. Each submitted bid b is assessed and validated based on the buyer's scoring rule. All the bidders who submit their bids with suggested prices (provided by the system) that make them active at the end of the auction will produce and deliver their respective amount of the item with its technical speci<sup>fi</sup>cation in accordance with their winning bids. The unit payoff of a winning bidder is the difference between the price received and the cost to produce a unit of the item depending on the technical speci<sup>fi</sup>cation. If a bidder does not belong to a group of winners, he or she does not produce and sell thus receives a zero payoff.

## 3.3. Performance measures and operationalization of constructs

## 3.3.1. Allocational efficiency

Allocational and Pareto ef<sup>fi</sup>ciency in this study were adapted from that of Strecker [38] by extending his procurement situation to a multiple<sup>e e</sup> sourcing situation where more than one winning supplier is possible.<sup>e e</sup>

The suppliers selected by the buyer to supply a given quantity of the item are denoted by a set $\tilde { i } _ { \mathrm { m } } , 1 \le \mathrm { m } \le \mathrm { n } ( \mathrm { n } = 6 )$ , and the transaction<sup>e e e e</sup> price and the delivered technical speci<sup>fi</sup>cation byp and $\widetilde { w } _ { \mathrm { m } } ,$ respectively. Hence, an outcome ☺is a set of winners: $\begin{array} { r } { \Theta = ( \widetilde { i } _ { \mathrm { m } } , \widetilde { w } _ { \mathrm { m } } , \widetilde { p } _ { \mathrm { m } } ) \in \mathrm { I } \times \mathbb { W } \times \mathbb { P } . } \end{array}$ The social welfare of an outcome ☺ is de<sup>fi</sup>ned as the sum of buyer's and the selected suppliers' surplus: s $\begin{array} { r } { { \mathsf { v } } ( \Theta ) = \sum _ { i = 1 } ^ { m } S ( \widetilde { i } _ { \mathrm { i } } , \widetilde { w } _ { \mathrm { i } } , \widetilde { p } _ { \mathrm { i } } ) + { \mathrm { u } } _ { \mathrm { i } } ( \widetilde { i } _ { \mathrm { i } } , \widetilde { w } _ { \mathrm { i } } , \widetilde { p } _ { \mathrm { i } } ) } \end{array}$ . The relative performance of an auction is measured by the allocational ef<sup>fi</sup>- ciency of an auction outcome ☺. An outcome ☺is called allocationally ef-<sup>fi</sup>cient if and only if the auction outcome ☺maximizes the social welfare. Speci<sup>fi</sup>cally, each winning supplier follows that $( \widetilde { i } _ { \mathrm { m } } , \ \widetilde { w } _ { \mathrm { m } } ) \in \mathrm { M A X } _ { ( \mathrm { i } , \mathrm { w } ) }$ $\{ \mathsf { v } ( \mathsf { w } ) - \mathsf { c } _ { \mathrm { i } } ( \mathsf { w } ) \}$ among all six suppliers. Allocational ef<sup>fi</sup>ciency is measured in terms of the sum of deviations of actual outcomes (<sup>fi</sup>nal allocations) from maximum achievable social welfare with misallocations representing foregone gains from trade. The relative ef<sup>fi</sup>ciency (RE) of<sup>e e e</sup> an outcome is de<sup>fi</sup>ned as the sum of relative ef<sup>fi</sup>ciencies of winning suppliers. Each winning supplier's relative ef<sup>fi</sup>ciency is de<sup>fi</sup>ned as the actual realized social welfare as a ratio of the potential maximum social welfare $( \mathtt { R E } _ { \mathrm { i } } = \mathsf { w } ( \widetilde { w } _ { \mathrm { m } } ) \widetilde { i } ( \bar { i } , \overline { { w } } )$ where $\mathrm { i } = 1 , \ldots$ m and w(i,w) is the potential maximum social welfare). Thus, relative ef<sup>fi</sup>ciency of an outcome can be written as $\begin{array} { r } { \mathbb { R E } = \sum _ { 1 } ^ { m } \mathbb { R E } _ { i } } \end{array}$ . Larger values of RE indicate a higher ef<sup>fi</sup>ciency $( 0 < = \mathrm { R E } < = 6 , \mathrm { R E } = 6$ when all the six suppliers are selected as the winning suppliers and all $\mathsf { R E } _ { \mathrm { i } } s = 1 )$ .

Consider one simple example. Assume that 3 suppliers are preparing to participate in a multi-attribute online reverse auction organized by a buyer. This auction concentrates not only on price and quantity, but also on non-price attribute-warranty. The following are cost schedules for the three suppliers of providing 1-year– 10-year warranties and the valuation schedule of the buyer:

Supplier 1: 1 year: 609; 2 years: 610; 3 years: 611; 4 years: 614; 5 years: 618; 6 years: 623; 7 years: 626; 8 years: 628; 9 years: 629; and 10 years: 632.

Supplier 2: 1 year: 597; 2 years: 602; 3 years: 607; 4 years: 613; 5 years: 622; 6 years: 626; 7 years: 630; 8 years: 635; 9 years: 638; and 10 years: 643.

Supplier 3: 1 year: 606; 2 years: 610; 3 years: 614; 4 years: 618; 5 years: 623; 6 years: 635; 7 years: 656; 8 years: 680; 9 years: 694; and 10 years: 717.

Buyer: 1 year: 645; 2 years: 654; 3 years: 662; 4 years: 669; 5 years: 676; 6 years: 755; 7 years: 763; 8 years: 771; 9 years: 777; and 10 years: 784.

From such above numbers, we can compute the differences between the buyer valuation and each supplier's costs as follows.

Differences between the buyer valuation and Supplier 1's costs: 1 year: 36; 2 years: 44; 3 years: 51; 4 years: 55; 5 years: 58; 6 years: 132; 7 years: 137; 8 years: 143; 9 years: 148; and 10 years: 152.

Differences between the buyer valuation and Supplier 2's costs: 1 year: 48; 2 years: 52; 3 years: 55; 4 years: 56; 5 years: 54; 6 years: 129; 7 years: 133; 8 years: 136; 9 years: 139; and 10 years: 141.

Differences between the buyer valuation and Supplier 3's costs: 1 year: 39; 2 years: 44; 3 years: 48; 4 years: 51; 5 years: 53; 6 years: 120; 7 years: 107; 8 years: 91; 9 years: 83; and 10 years: 67.

Based on the values of the differences computed, we rank them as (152; 148; 143; 141; 139; 137; 136; 133; 132; 129; 120; 107; 91; 83; 67; 58; 56; 55; 54; 53; 52; 51; 48; 44; 39; 36) with the maximum value of 152 and the minimum value of 36. Furthermore, suppose that in the end, Supplier 1 and Supplier 2 are selected as the winners with market prices as 720 and 700 respectively and quantities as 70 and 30 respectively (such quantities completely meet the buyer's demand) supplier 1 will sell the product with warranty of 10 years and Supplier 2 will sell the product with warranty of 9 years. Total social welfare for the two suppliers and the buyer equals $1 5 2 + 1 3 9 = 2 9 1$ . Supplier 1 approaches the maximum value (152) of differences between the buyer valuation and his costs. Supplier 2 approaches the <sup>fi</sup>fth maximum value of 139. As a result, RE (relative allocational ef<sup>fi</sup>ciency) is computed as $( 1 5 2 / 1 5 2 ) + ( 1 3 9 / 1 5 2 ) = 1 . 9 1$ (very near 2) or 95.5%. Thus, we can conclude that the allocational ef<sup>fi</sup>ciency in this example is very high.<sup>e</sup>

## 3.3.2. Pareto efficiency<sup>e e</sup>

An outcome ☺ is called Pareto ef<sup>fi</sup>cient if the technical speci<sup>fi</sup>cation $( \widetilde { w } _ { \mathrm { m } } )$ supplied by winning suppliers maximizes the social welfare given the buyer's value function and the selected suppliers' production cost schedules: $( \widetilde { i } _ { \mathrm { m } } , \widetilde { w } _ { \mathrm { m } } ) \in \mathrm { M A X } _ { ( \mathrm { i } , \mathrm { ~ w } ) } \left\{ \mathsf { v } ( \mathbf { w } ) - C _ { i m } \left( \mathbf { w } \right) \right\}$ }. In addition, if each supplier among the winning suppliers is Pareto ef<sup>fi</sup>cient, then the group of winning suppliers should also be Pareto ef<sup>fi</sup>cient, as discussed earlier.

Still based on the above example, we now analyze Pareto ef<sup>fi</sup>ciency for each pair of buyer and supplier. Since Supplier 1 approaches the maximum value of 152 meaning that Pareto ef<sup>fi</sup>ciency for this supplier is perfect (100%). In a same vein, Supplier 2 approaches the value of 139 (very near to the maximum difference (141)) between the buyer valuation and Supplier 2's costs, meaning that Pareto ef<sup>fi</sup>ciency for Supplier 2 is 98.6%. As a consequence, we can conclude that the group of winning suppliers (Supplier 1 and Supplier 2) are highly Pareto ef<sup>fi</sup>cient with value of $( 1 0 0 \% + 9 8 . 6 \% ) / 2 = 9 9 . 3 \%$

It should be noted that the minimum allocational and Pareto ef<sup>fi</sup>- ciency is 0 while the maximum is 1.

## 3.3.3. Cost savings for buyer

This variable is de<sup>fi</sup>ned as the difference between the buyer valuation and the actual prices. With the example mentioned above, cost savings for the buyer equal $7 8 4 - 7 2 0 = 6 4 $ for one unit purchased from Supplier 1 and $7 7 7 - 7 0 0 = 7 7$ for one unit purchased from Supplier 3. Thus, the total cost savings equal 64 ∗ $7 0 + 7 7 * 3 0 =$ \$6790

## 3.3.4. Profits for suppliers

This variable is de<sup>fi</sup>ned as the difference between the actual price and the costs incurred by the suppliers. With the example mentioned above, pro<sup>fi</sup>t for Supplier 1 equals $7 2 0 - 6 3 2 = 8 8$ for each unit sold to the buyer and pro<sup>fi</sup>t for Supplier 2 equals $7 0 0 - 6 3 8 = 6 2$ for each unit sold to the buyer. Thus, the total pro<sup>fi</sup>ts for Supplier 1 and Supplier 2 equal 88 ∗ 70 + 62 ∗ 30 = \$8020

Cost savings for the buyer and pro<sup>fi</sup>ts for the suppliers can be normalized so that the maximum is 1 and the minimum is 0. To make it clearer, let's consider an example where pro<sup>fi</sup>ts for the winning suppliers are 35, 44, 53, and 60, respectively. In this case, the maximum value is 60 and the minimum value is 35. We utilize the formula (x − min) / (max − min) such that the above values are converted into 0, 0.36, 0.72, and 1.

## 3.4. Data collection

The three treatments (Auto Mode — auction mechanism; Manual Mode — negotiation mechanism; and Hybrid Mode — hybrid mechanism) were investigated under six sequences. Such sequences were set up based on systematically switching the three modes. Speci<sup>fi</sup>cally, sequence 1 is M (Manual Mode), A (Auto Mode), and H (Hybrid Mode); sequence 2: M, H, and A; sequence 3: A, M, and H; sequence 4: A, H, and M; sequence 5: H, A, and M; and sequence 6: H, M, and A. In each sequence, six subjects participated in all the three treatments, and their roles were changed in Hybrid Mode (they were placed on Manual Mode or Auto Mode).

In addition, in each sequence (each experiment), six rounds of auctions/negotiations/hybrid were conducted by the same six subjects after two practice rounds for training in Auto and Manual Modes. The experiments repeatedly ran through sequences 1 to 6. Thus, in total, there were 22 experiments with 132 rounds of auctions/negotiations/ hybrid and 132 subjects attending.

The subjects were noti<sup>fi</sup>ed that the buyer (AO) worked with them through the software. In the experiment, the buyer's value function and the suppliers' technical speci<sup>fi</sup>cations were carefully constructed considering advantages of each supplier regarding the non-price attribute. Each supplier did only know his or her cost schedule, but not that of the other suppliers. All the suppliers did not know the value function of the buyer. Both the buyer's valuations and suppliers' cost schedules were constructed to guarantee a unique equilibrium outcome and adequate variation between auction rounds. The subjects were only provided with printout of tabulated discrete values. In each of the six rounds of each sequence, the buyer had a different valuation for technical speci<sup>fi</sup>cation and each supplier was assigned a different production cost schedule. The supplier's production cost schedules and the buyer's valuation functions were randomized a priori and varied between auctions.

The number of competing suppliers and the number of consecutive auctions/negotiations/hybrid were public information. The bidders did also know that in each auction/negotiation/hybrid, it was likely that a set of suppliers could be selected as winners (multiple sourcing) and that only these winning bidders made pro<sup>fi</sup>ts or losses.

ANOVA for AE.  
Table 1

<table><tr><td>Source</td><td>DF</td><td>Type III SS</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>G</td><td>21</td><td>0.37700549</td><td>0.01795264</td><td>1.08</td><td>0.3893</td></tr><tr><td>M</td><td>2</td><td>0.72446856</td><td>0.36223428</td><td>21.81</td><td>&lt;.0001</td></tr><tr><td>M * G</td><td>42</td><td>0.59110644</td><td>0.01407396</td><td>0.85</td><td>0.7141</td></tr></table>

Table 2  
ANOVA for PE.

<table><tr><td>Source</td><td>DF</td><td>Type III SS</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>G</td><td>21</td><td>0.36564924</td><td>0.01741187</td><td>0.71</td><td>0.8116</td></tr><tr><td>M</td><td>2</td><td>0.50705909</td><td>0.25352955</td><td>10.28</td><td>0.0001</td></tr><tr><td>M * G</td><td>42</td><td>0.61240758</td><td>0.01458113</td><td>0.59</td><td>0.9646</td></tr></table>

Throughout the experiment, the production cost schedules remained private information to the respective supplier and suppliers were not provided with information about their competitors' production costs. The subjects remained anonymous during the experiment and communication among subjects was not permitted.

The experiments were conducted at the College of Business laboratory at a large state university in the southwestern United States. The subjects were selected from a pool of undergraduate and graduate students. Before participating in the experiments, the subjects were given written instructions which were read aloud by a research assistant prior to the bidding.

In addition, YouTube videos were utilized so that the students were trained by watching samples of conducting the NegotiAuction system experiment. Also, at the beginning of the experiment, there were two events set up for the subjects so that they became familiar with using the system under all the three treatments. In order to motivate the subjects to really and actively participate in the experiment, every subject had a chance of receiving a prize of \$200. However, chances were different for each subject depending on how well they did in the experiment. Speci<sup>fi</sup>cally, outcomes of the experiment for each subject were classi<sup>fi</sup>ed into six levels such as: (A) excellent; (B) very good; (C) good; (D) average; (E) not very good; and (F) poor. Thus, if a subject was ranked A, she or he would be given 6 lottery tickets; B with 5; C with 4; D with 3; E with 2 ticket; and F with 1 ticket. There was only one winning ticket. All the tickets were put in a jar and after the experiment and the department administrative assistant randomly selected the winning ticket from the jar. In addition, all the subjects participating in the experiment were given extra credit by their professors in the course they took.

## 3.5. Statistical method

In order to compare the outcomes of the three treatments (Auto Mode — auction mechanism; Hybrid Mode — hybrid mechanism; and Manual Mode — negotiation mechanism), we utilized the analysis of variance technique. By utilizing this technique, we tested the null hypothesis that there are no differences among the three treatments with respect to allocational ef<sup>fi</sup>ciency, Pareto ef<sup>fi</sup>ciency, cost savings for buyer, and pro<sup>fi</sup>ts for suppliers. If such a null hypothesis is statistically rejected, we go further to conduct pair wise comparison of all the treatments. The parameters of interest are all pairwise differences among the treatment means, $\mu _ { \mathrm { i } } - \mu _ { \mathrm { j } } \ : \mathrm { f o r } \ : \mathrm { i } \neq \mathrm { j } ,$ , resulting in t(t − 1) / 2 comparisons. Most frequently, applications of these methods have an objective to detect signi<sup>fi</sup>cant inequalities, μ ≠ μ for all i ≠ j. Since, the Tukey method provides the best protection against decision errors, along with the strong inference about magnitude and direction of differences among the treatments [24], thus, we use the Tukey method in case the null hypothesis $\mu _ { \mathrm { M } } \neq \mu _ { \mathrm { A } } \neq \mu _ { \mathrm { H } }$ is rejected.

Table 3  
ANOVA for CS.

<table><tr><td>Source</td><td>DF</td><td>Type III SS</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>G</td><td>21</td><td>0.68392228</td><td>0.03256773</td><td>3.12</td><td>0.0002</td></tr><tr><td>M</td><td>2</td><td>1.22298337</td><td>0.61149169</td><td>58.64</td><td>&lt;.0001</td></tr><tr><td>M * G</td><td>42</td><td>1.05032268</td><td>0.02500768</td><td>2.40</td><td>0.0007</td></tr></table>

Table 6  
Table 4 ANOVA for P.

<table><tr><td>Source</td><td>DF</td><td>Type III SS</td><td>Mean square</td><td>F value</td><td>Pr &gt; F</td></tr><tr><td>G</td><td>21</td><td>0.94639845</td><td>0.04506659</td><td>3.77</td><td>&lt;.0001</td></tr><tr><td>M</td><td>2</td><td>0.97647104</td><td>0.48823552</td><td>40.85</td><td>&lt;.0001</td></tr><tr><td>M * G</td><td>42</td><td>1.09819323</td><td>0.02614746</td><td>2.19</td><td>0.0021</td></tr></table>

## 4. Results

In this study, there are four outcome variables — allocational ef<sup>fi</sup>- ciency (AE), Pareto ef<sup>fi</sup>ciency (PE), cost savings for buyer (CS), and pro<sup>fi</sup>ts for suppliers (P). These variables were standardized so that their values were within 0 and 1. In total, there were 22 experiments and each experiment is viewed as one “experimental” unit. There are two factors investigated in the study, namely, Mode (M) and Group (G). Mode consists of three levels — Auto Mode (auction mechanism), Hybrid Mode (hybrid mechanism), and Manual Mode (negotiation mechanism) while Group consists of 22 levels corresponding to 22 experiments.

Our analyses are based on parametric tests, it is very important that certain assumptions are met. Since groups were independent from each other, the independence assumption is validated. In addition, the measures for AE, PE, CS, and P were standardized so that their values were within [0, 1] leading to the validity of the internal data assumption for AE, PE, CS, and P. As for the normal data assumption, both statistical tests and visual checking were implemented. We did not <sup>fi</sup>nd any serious violations based on examining Q–Q plot and Box plot for AE. Moreover, the p-value of Shapiro–Wilk test was 0.0843 indicating that AE is normally distributed. Neither did we <sup>fi</sup>nd any serious violations from the residual plot for AE, although the plot looked a little bit skewed (but surprisingly, the skewness coef<sup>fi</sup>cient was 0 and the kurtosis coef-<sup>fi</sup>cient was 0.157).

Having looked at the Q–Q plot, residual plot, and Box plot for PE, no serious violations were found. The skewness coef<sup>fi</sup>cient and kurtosis coef<sup>fi</sup>cient were 0 and −0.129, respectively. As for CS and P, although residual plots and Box plots looked acceptable, Q–Q plots indicated some outliers. Thus, it was concluded that AE and PE are suitable for the ANOVA technique. There was uncertainty if CS and P were suitable for the ANOVA technique, so we conducted both the ANOVA technique and skewed distribution technique for CS and P, and their results were compared to one another.

![](/api/attachments/YBUCG6CU/fulltext/images/007f525f73003a971e8de8f8243c3557454338dd969ec56f7c1fad3e110317e7.jpg)

![](/api/attachments/YBUCG6CU/fulltext/images/1690cb8ebb5bde7a3d1d916caac94bf3d9638fd29ae86d699e26f8f8d34e2a8c.jpg)

![](/api/attachments/YBUCG6CU/fulltext/images/21c6074e1872da7b00f11386928988427c0e06cf8afd195855ccd0dc0521b17a.jpg)

P  
![](/api/attachments/YBUCG6CU/fulltext/images/53507f0fa900aaa894eea8d675e602e0f054e6800ea050121b7db1cbc0892cf9.jpg)  
Fig. 1. Means for AE, PE, CS, and P.

Table 5  
Tukey treatment comparison for AE (means with the same letter are not signi<sup>fi</sup>cantly different).

<table><tr><td>Tukey grouping</td><td>Mean</td><td>N</td><td>Mode</td></tr><tr><td>A</td><td>0.79568</td><td>44</td><td>H</td></tr><tr><td>A</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.78284</td><td>44</td><td>A</td></tr><tr><td>B</td><td>0.63250</td><td>44</td><td>M</td></tr></table>

Alpha: 0.05.  
Error degrees of freedom: 42.  
Error mean square: 0.014074.  
Critical value of studentized range: 3.43582.  
Minimum signi<sup>fi</sup>cant difference: 0.0614.

Table 1 illustrates the outputs resulting from testing main and interaction effects for AE. The table shows that there are signi<sup>fi</sup>cant differences in M effects for AE but there are no signi<sup>fi</sup>cant differences in G and M ∗ G effects.

Table 2 illustrates the outputs resulting from testing main and interaction effects for PE. The table shows that there are signi<sup>fi</sup>cant differences in M effects for PE but there are no signi<sup>fi</sup>cant differences in G and M \* G effects.

Table 3 illustrates the outputs resulting from testing main and interaction effects for CS. The table shows that there are signi<sup>fi</sup>cant differences in M effects for CS and there are signi<sup>fi</sup>cant differences in G and M G effects

Table 4 illustrates the outputs resulting from testing main and interaction effects for P. The table shows that there are signi<sup>fi</sup>cant differences in M effects for P and there are signi<sup>fi</sup>cant differences in G and M G effects. In a word, there are signi<sup>fi</sup>cant differences in M effects for all the outcome variables — AE, PE, CS, and P. However, as for AE and PE, there are no signi<sup>fi</sup>cant differences in G and M ∗ G effects. For CS and P, there are signi<sup>fi</sup>cant differences in both G and M ∗ G. Our major interest is to know which treatment (Mode) is better than the others.

In addition to testing the main and interaction effects, calculations for means of AE, PE, CS, and P were also made. Fig. 1 illustrates the means for AE, PE, CS, and P.

Fig. 1a seems to indicate that Hybrid Mode N Auto Mode N Manual Mode for AE (N means better). However, based on the Tukey technique, it can be concluded that there are no signi<sup>fi</sup>cant differences between Auto Mode and Hybrid Mode, but both Auto Mode and Hybrid Mode are better than Manual Mode. Such results are illustrated in Table 5.

Fig. 1b seems to indicate that Auto Mode N Hybrid Mode N Manual Mode for PE. It should be noted that the symbol N means “better”. To put it another way, based on such mean values, Auto Mode seems to be better than Hybrid Mode with respect to PE and Hybrid Mode seems to be better than Manual Mode with respect to PE. However, based on the Tukey technique, it can be concluded that there are no signi<sup>fi</sup>cant differences between Auto Mode and Hybrid Mode, but both Auto Mode and Hybrid Mode are better than Manual Mode.

Tukey treatment comparison for PE (means with the same letter are not signi<sup>fi</sup>cantly different).

<table><tr><td>Tukey grouping</td><td>Mean</td><td>N</td><td>Mode</td></tr><tr><td>A</td><td>0.87909</td><td>44</td><td>A</td></tr><tr><td>A</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.86500</td><td>44</td><td>H</td></tr><tr><td>B</td><td>0.74114</td><td>44</td><td>M</td></tr></table>

Alpha: 0.05.  
Error degrees of freedom: 42.  
Error mean square: 0.014581.  
Critical value of studentized range: 3.43582.  
Minimum signi<sup>fi</sup>cant difference: 0.0625.

Table 7  
Tukey treatment comparison for CS (means with the same letter are not signi<sup>fi</sup>cantly different).

<table><tr><td>Tukey grouping</td><td>Mean</td><td>N</td><td>Mode</td></tr><tr><td>A</td><td>0.49407</td><td>44</td><td>H</td></tr><tr><td>A</td><td></td><td></td><td></td></tr><tr><td>A</td><td>0.44847</td><td>44</td><td>M</td></tr><tr><td>B</td><td>0.27093</td><td>44</td><td>A</td></tr></table>

Alpha: 0.05.  
Error degrees of freedom: 42.  
Error mean square: 0.025008.  
Critical value of studentized range: 3.43582.  
Minimum signi<sup>fi</sup>cant difference: 0.0819.

Such results are illustrated in Table 6.

Fig. 1c seems to indicate that Hybrid Mode N Manual Mode N Auto Mode for CS.

However, based on the Tukey technique, it can be concluded that there are no signi<sup>fi</sup>cant differences between Hybrid Mode and Manual Mode, but both Hybrid Mode and Manual Mode are better than Auto Mode. Such results are illustrated in Table 7.

Fig. 1d seems to indicate that Auto Mode N Hybrid Mode N Manual Mode for P.

However, based on the Tukey technique, it can be concluded that there are no signi<sup>fi</sup>cant differences between Hybrid Mode and Manual Mode, but Auto Mode is better than both Hybrid Mode and Manual Mode. Such results are illustrated in Table 8.

It should be noted that the assumptions under which ANOVA is reliable are the same as for all parametric tests based on the normal distribution. That is, data should be from a normally distributed population, the variances in each experiment condition are “fairly” similar, observations should be independent and the dependent variable should be measured on at least an interval scale.

Although we much focus on how important assumptions are, they are not completely in<sup>fl</sup>exible. In terms of violations of the assumption of homogeneity of variance, ANOVA is fairly robust when sample sizes are equal. However, when sample sizes are unequal ANOVA is not robust to violations of homogeneity of variance. When groups with larger sample sizes have larger variances than the groups with smaller sample sizes, the resulting F-ratio tends to be conservative. That is, it's more likely to produce a non-signi<sup>fi</sup>cant result when a genuine difference does exist in the population. Conversely, when the groups with larger sample sizes have smaller variances than the groups with smaller sample sizes, the resulting F-ratio tends to be liberal. That is, it is more likely to produce a signi<sup>fi</sup>cant result when there is no difference between groups in the population [14].

As a remedy to the violation of equal variances and normal distribution, Proc Glimmix in SAS 9.2 with the gamma distribution is utilized for detecting any differences among Auto Mode, Manual Mode, and Hybrid Mode for both CS and P. Proc Glimmix <sup>fi</sup>ts statistical models to data with correlations or non-constant variability and where the response is not necessarily normally distributed. These models are considered as generalized linear mixed models (GLMM). With this remedy, it was found that there are signi<sup>fi</sup>cant differences among modes (treatments) for both CS and P. The following tables show more speci<sup>fi</sup>c results regarding treatment means and treatment pair-wise comparisons.

Tukey treatment comparison for P (means with the same letter are not signi<sup>fi</sup>cantly different).

<table><tr><td>Tukey grouping</td><td>Mean</td><td>N</td><td>Mode</td></tr><tr><td>A</td><td>0.68019</td><td>44</td><td>A</td></tr><tr><td>B</td><td></td><td></td><td></td></tr><tr><td>B</td><td>0.52174</td><td>44</td><td>M</td></tr><tr><td>B</td><td>0.48072</td><td>44</td><td>H</td></tr></table>

Alpha: 0.05.  
Error degrees of freedom: 42.  
Error mean square: 0.026147.  
Critical value of studentized range: 3.43582.  
Minimum signi<sup>fi</sup>cant difference: 0.0838.

Table 9  
Means for Auto, Manual, and Hybrid Modes based on the Glimmix procedure (CS).

<table><tr><td>Mode</td><td>Estimate</td><td>Standard error</td><td>DF</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>A</td><td>-1.3502</td><td>0.07051</td><td>104</td><td>-19.15</td><td>&lt;.0001</td></tr><tr><td>H</td><td>-0.7068</td><td>0.06985</td><td>104</td><td>-10.12</td><td>&lt;.0001</td></tr><tr><td>M</td><td>-0.8014</td><td>0.06985</td><td>104</td><td>-11.47</td><td>&lt;.0001</td></tr></table>

Table 9 presents the outputs from Proc Glimmix for CS.

Table 10 presents the comparisons for CS based on Proc Glimmix. Table 11 presents the outputs from Proc Glimmix for P.

Table 12 presents the comparisons for P based on Proc Glimmix.

The numbers in estimate columns of Tables 9, 10, 11, and 12 are in the form of Ln values. As for CS, there are no signi<sup>fi</sup>cant differences between Hybrid Mode and Manual Mode, but there are signi<sup>fi</sup>cant differences between Auto Mode and Hybrid Mode and between Auto Mode and Manual Mode. As for P, the same results were shown. In order to specify the directions and magnitudes among the three modes, it is necessary to convert the Ln values into the original values. Such a process is illustrated in Table 13.

The numbers in column 2 and column 4 of Table 13 indicate that for CS, Hybrid Mode is signi<sup>fi</sup>cantly better than Auto Mode and Manual Mode is signi<sup>fi</sup>cantly better than Auto Mode. For P, Auto Mode is signi<sup>fi</sup>cantly better than Hybrid Mode and Manual Mode. Such results show that there are no differences between using Proc GLM and Proc Glimmix, or to put it another way, using Proc GLM or Proc Glimmix result in the same results.

From the aforementioned statistical analyses, results of the <sup>fi</sup>rst 12 hypotheses testing are summarized in Table 14. As seen in this table, six hypotheses are statistically supported by the data.

## 5. Implications, limitations and directions for future research

## 5.1. Implications

## 5.1.1. Allocational and Pareto efficiency

For allocational ef<sup>fi</sup>ciency, the mean of Hybrid Mode (hybrid mechanism) was 0.79568, Auto Mode (auction mechanism) 0.78284, and Manual Mode (negotiation mechanism) 0.63250. Based on these numbers, it appears that Hybrid Mode is the best followed by Auto Mode and Manual Mode. However, from the Tukey treatment comparison technique, there were no signi<sup>fi</sup>cant differences between Hybrid Mode and Auto Mode, but both Hybrid Mode and Auto Mode were better than Manual Mode. As for Pareto ef<sup>fi</sup>ciency, the mean of Hybrid Mode was 0.86500 while the means for Auto Mode and Manual Mode were 0.87909 and 0.74114, respectively. In a similar vein as allocational ef<sup>fi</sup>- ciency, there were no signi<sup>fi</sup>cant differences between Hybrid Mode and Auto Mode, but both Hybrid Mode and Auto Mode were better than Manual.

Table 10  
Pair-wise comparisons for CS based on the Glimmix procedure.

<table><tr><td>Mode</td><td>- Mode</td><td>Estimate</td><td>Standard error</td><td>DF</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>A</td><td>H</td><td>-0.6433</td><td>0.08465</td><td>104</td><td>-7.60</td><td>&lt;.0001</td></tr><tr><td>A</td><td>M</td><td>-0.5488</td><td>0.08465</td><td>104</td><td>-6.48</td><td>&lt;.0001</td></tr><tr><td>H</td><td>M</td><td>0.09454</td><td>0.08410</td><td>104</td><td>1.12</td><td>0.2636</td></tr></table>

Table 11  
Means for Auto, Manual, and Hybrid Modes based on the Glimmix procedure (P).

<table><tr><td>Mode</td><td>Estimate</td><td>Standard error</td><td>DF</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>A</td><td>-0.4057</td><td>0.04121</td><td>104</td><td>-9.85</td><td>&lt;.0001</td></tr><tr><td>H</td><td>-0.7151</td><td>0.04154</td><td>104</td><td>-17.22</td><td>&lt;.0001</td></tr><tr><td>M</td><td>-0.6510</td><td>0.04121</td><td>104</td><td>-15.80</td><td>&lt;.0001</td></tr></table>

The results in this paper showed that both Hybrid Mode and Auto Mode were better than Manual Mode. The results are in line with the reasoning of [23,38] that the full disclosure mechanism is better than the non-disclose mechanism (or unrestricted information architecture is better than restricted information architecture), although these researchers only compared among multi-attribute auctions, not among multi-attribute auctions, multi-attribute negotiations, and hybrid mechanisms. The results are also supported by [17]: negotiation tasks require substantial cognitive efforts and are very likely to result in suboptimal outcomes due to people's cognitive limitations, their lack of interest in highly complex transactions, and their involvement with many competitive activities. By the same token, Chen et al. [9] conclude from an experimental study that multi-attribute negotiations are no better than MAORAs, and MAORAs require less effort than multiattribute negotiations.

Thus, if management (both buyers and suppliers) from companies and/or governments are considering which Modes (mechanisms) to use, they'd better utilize either Hybrid Mode or Auto Mode, because both Hybrid Mode and Auto Mode are better than Manual Mode with respect to allocational ef<sup>fi</sup>ciency and Pareto ef<sup>fi</sup>ciency. Nevertheless, the question of which Mode – Hybrid Mode or Auto Mode – is better than the other is still unanswered because the data in this paper indicated that there were not signi<sup>fi</sup>cant differences between Hybrid Mode and Auto Mode.

## 5.1.2. Cost savings and profits

As for cost savings, the mean of Hybrid Mode was 0.49407 while the means for Auto Mode and Manual Mode were 0.27093 and 0.44847, respectively. These numbers seems to indicate that Hybrid Mode N Manual Mode N Auto Mode (N is better); however, based on the Tukey treatment comparison technique, there were no signi<sup>fi</sup>cant differences between Hybrid Mode and Manual Mode, but both Hybrid Mode and Manual Mode were better than Auto Mode. As for pro<sup>fi</sup>ts earned by suppliers, the mean of Auto Mode was 0.68019 while that of Manual Mode and Hybrid Mode were 0.52174 and 0.48072, respectively. Such numbers appear to indicate that Auto Mode N Manual Mode N Hybrid Mode; however, based on the Tukey treatment comparison technique, there were no signi<sup>fi</sup>cant differences between Hybrid Mode and Manual Mode, but Auto Mode was better than both Hybrid Mode and Manual Mode.

At this point, one dif<sup>fi</sup>cult question for management in both companies and governments arises that which Mode is the best to use? It is certain that we cannot have a concrete answer due to the fact that the answer should be based on whose perspective — the buyer perspective or the supplier perspective? The buyer might select Hybrid Mode or Manual Mode because both Hybrid Mode and Manual Mode are better than Auto Mode with respect to cost savings. However, the supplier might want to select Auto Mode due to the fact that Auto Mode is better than Manual Mode and Hybrid Mode with respect to pro<sup>fi</sup>ts earned by the supplier. It is also worth noting that the <sup>fi</sup>nal decision under the buyer perspective or the supplier perspective should be based on allocational ef<sup>fi</sup>ciency and Pareto ef<sup>fi</sup>ciency as well. Speci<sup>fi</sup>cally, in the e-procurement process, if suppliers have more power than the buyer, they might want to utilize Auto Mode since perhaps utilizing Auto Mode is expected to bring about more pro<sup>fi</sup>ts for them. Also, in this paper, the data supported that Auto Mode is better than Manual Mode with respect to allocational and Pareto ef<sup>fi</sup>ciency (although there is no signi<sup>fi</sup>cant difference between Auto Mode and Hybrid Mode). Contrary, if the buyer has more power than suppliers, it is very likely that the buyer will utilize Hybrid Mode or Manual Mode since perhaps utilizing Hybrid Mode or Manual Mode might bring about more cost savings for the buyer. But it should be noted that if allocational and Pareto ef<sup>fi</sup>ciency are taken into account, the buyer is more likely to select Hybrid Mode instead of utilizing Manual Mode since Hybrid Mode is better than Manual Mode with respect to allocational ef<sup>fi</sup>ciency and Pareto ef<sup>fi</sup>ciency. In a word, choosing an appropriate Mode among three Modes — Hybrid Mode (hybrid mechanism), Auto Mode (auction mechanism), and Manual Mode (negotiation mechanism) should be based on carefully considering their characteristics regarding allocational ef<sup>fi</sup>ciency, Pareto ef<sup>fi</sup>ciency, cost savings, and pro<sup>fi</sup>ts. In addition, power asymmetry between the buyer and suppliers should also be taken into consideration in the e-procurement process (multi-attribute online reverse auction).

Table 12  
Pair-wise comparisons for P based on the Glimmix procedure.

<table><tr><td>Mode</td><td>- Mode</td><td>Estimate</td><td>Standard error</td><td>DF</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>A</td><td>H</td><td>0.3094</td><td>0.04538</td><td>104</td><td>6.82</td><td>&lt;.0001</td></tr><tr><td>A</td><td>M</td><td>0.2453</td><td>0.04508</td><td>104</td><td>5.44</td><td>&lt;.0001</td></tr><tr><td>H</td><td>M</td><td>-0.06410</td><td>0.04538</td><td>104</td><td>-1.41</td><td>0.1607</td></tr></table>

Table 13  
Conversion of Ln values into original values.

<table><tr><td>Ln values for CS</td><td>Original values for CS</td><td>Ln values for P</td><td>Original values for P</td></tr><tr><td>A: -1.3502</td><td>A: 0.2592</td><td>A: -0.4057</td><td>A: 0.6665</td></tr><tr><td>H: -0.7068</td><td>H: 0.4932</td><td>H: -0.7151</td><td>H: 0.4891</td></tr><tr><td>M: -0.8014</td><td>M: 0.4487</td><td>M: -0.6510</td><td>M: 0.5215</td></tr></table>

## 5.2. Limitations and directions for future research

There are some limitations in this study that future research needs to address. First, Hybrid Mode, Auto Mode, and Manual Mode may be fully differentiated in speci<sup>fi</sup>c situations; for example, a different number of bidders may have impacts on each Mode's economic performance. Thus, future research needs to be conducted to investigate how number of bidders affects the economic performance of Hybrid Mode, Auto Mode, and Manual Mode.

Another limitation is that this study is an experimental one with the participation of under-graduate and graduate students, and there might not be enough <sup>fi</sup>nancial incentives for these subjects to seriously pursue multiple rounds of auctions and negotiations [40].

## Table 14

Results of the <sup>fi</sup>rst 12 hypotheses testing

<table><tr><td>Hypotheses</td><td>Hypothesis supported</td></tr><tr><td>H1. Allocational efficiency is better in Auto Mode than in Manual Mode.</td><td>Yes</td></tr><tr><td>H2. Pareto efficiency is better in Auto Mode than in Manual Mode.</td><td>Yes</td></tr><tr><td>H3. Cost savings earned by buyers are higher in Auto Mode than in Manual Mode.</td><td>No</td></tr><tr><td>H4. Profits earned by suppliers are higher in Auto Mode than in Manual Mode.</td><td>Yes</td></tr><tr><td>H5. Allocational efficiency is better in Hybrid Mode than in Auto Mode.</td><td>No</td></tr><tr><td>H6. Pareto efficiency is better in Hybrid Mode than in Auto Mode.</td><td>No</td></tr><tr><td>H7. Cost savings earned by buyers are higher in Hybrid Mode than in Auto Mode.</td><td>Yes</td></tr><tr><td>H8. Profits earned by suppliers are higher in Hybrid Mode than in Auto Mode.</td><td>No</td></tr><tr><td>H9. Allocational efficiency is better in Hybrid Mode than in Manual Mode.</td><td>Yes</td></tr><tr><td>H10. Pareto efficiency is better in Hybrid Mode than in Manual Mode.</td><td>Yes</td></tr><tr><td>H11. Cost savings earned by buyers are higher in Hybrid Mode than in Manual Mode.</td><td>No</td></tr><tr><td>H12. Profits earned by suppliers are higher in Hybrid Mode than in Manual Mode.</td><td>No</td></tr></table>

However, we have seen that in our experiment, the subjects had very high motivations to attend the experiment since they had opportunities to gain a \$200 lottery award and bonus grade for the courses they were taking. Nevertheless, it would be better if future research mobilizes real dealmakers to actually use the NegotiAuction system to further validate the results.

## References

[1] N. Aktas, D. Bodl, R. Roll, Negotiation under the threat of an auction, Journal of Financial Economics 98 (2) (2010) 241–255.

[2] P. Bajari, S. Tadelis, Incentives versus transaction costs: a theory of procurement contracts, Journal of Economics 32 (2001) 387–407.

[3] P. Bajari, R. McMillan, S. Tadelis, Auctions versus negotiations in procurement: an empirical analysis, The Journal of Law, Economics, & Organization 25 (2) (2009) 372–399.

[4] D. Beil, L. Wein, An inverse-optimization-based auction for multiattribute RFQs, Management Science 49 (11) (2003) 1529–1545.

[5] M. Bichler, An experimental analysis of multi-attribute auctions, Decision Support Systems 29 (3) (2000) 249–268.

[6] M. Bichler, G. Kersten, S. Strecker, Towards a structured design of electronic negotiations, Group Decision and Negotiation 12 (4) (2003) 311–335.

[7] A. Bonaccorsi, T. Lyon, F. Pammolli, G. Turchetti, Auctions vs. bargaining: an empirical analysis of medical device procurement, Working Paper, Department of Economics, University of Washington, 2000.

[8] J. Bulow, P. Klemperer, Auctions versus negotiations, The American Economic Review 86 (1) (1996) 180–195

[9] E. Chen, G. Kersten, D. Neumann, R. Vahidov, E-market framework: the assessment and comparison of auction, negotiation and decision support, InterNeg Research Papers INR02, 2009. 1–20.

[10] E. David, S. Azoulay-Schwartz, S. Kraus, Bidding in sealed-bid and English multi-attribute auctions, Decision Support Systems 42 (2) (2006) 527–556.

[11] eBay Inc., Financial Results: Fourth Quarter 2001 First and Second Quarter 2004, Technical Report, eBay Inc., 2004

[12] M.L. Emiliani, Business-to-business online auctions: key issues for purchasing process improvement, Supply Chain Management: An International Journal 5 (4) (2000) 176–186.

[13] M.L. Emiliani, D. Stec, Aerospace parts suppliers' reaction to online reverse auctions, Supply Chain Management: An international Journal 9 (2) (2004) 139–153.

[14] G.V. Glass, P.D. Peckham, J.R. Sanders, Consequences of failure to meet assumptions underlving analysis of variance and covariance Educational Research 42 (1972) 237–288.

[15] P. Goldberg, Competitive bidding and the production of pre-contract information Journal of Economics 8 (1977) 250–261.

[16] L. Gwebu, Decision support in multi-attribute reverse auctions, Journal of Electronic Commerce Research 10 (4) (2009) 252–264.

[17] B. Hyder, J. Prietula, J. Michael, R. Weingart, Getting to best: ef<sup>fi</sup>ciency vs. optimality in negotiation, Cognitive Science 24 (2) (2000) 169–204.

[18] R. Ivanova-Stenzel, S. Kroger, Behavior on combined mechanisms: auctions with a pre-negotiation state — an experimental investigation, Working Paper, Institute of Economic Theory I, School of Business and Economics, Humboldt University of Berlin, 2004.

[19] S. Jap, An exploratory study of the introduction of online reverse auctions, Journal of Marketing 67 (7) (2003) 96–107.

[20] S. Jap, The impact of online reverse auction design on buyer-supplier relationships, Journal of Marketing 71 (1) (2007) 146–159.

[21] G. Kersten, H. Lai, Negotiation support and e-negotiation systems: an overview, Group Decision Negotiation 16 (2007) 553-586

[22] R. Kirkegaard, Auctions Versus Negotiations Revisited, Working Paper, Department of Economics, University of Aarhus, 2004.

[23] O. Koppius, E. Van Heck, Information architecture and electronic market performance in multi-dimensional auctions, Erasmus Research Institute of Management, Rotterdam School of Management, Erasmus University, Rotterdam, The Netherlands, 2002, p. 38.

[24] O.R. Kuehl, Design of Experiments: Statistical Principles of Research Design and Analysis, Duxbury, Thomson Learning, 2000. (Paci<sup>fi</sup>c Grove, CA, USA).

[25] B. Lef<sup>fl</sup>er, R. Rucker, I. Munn, The choice among sales procedures: auction vs. negotiated sales of private timber. Unpublished Manuscript, Department of Agricultural Economics and Economics, Montana State University, Bozeman, MT, January 2007.

[26] R. Leskela, J. Teich, H. Wallenius, J. Wallenius, Decision support for multi-unit combinatorial bundle auctions, Decision Support Systems 43 (2) (2007) 420–434.

[27] D. Levin, L. Ye, Hybrid auctions revisited, Economics Letters 99 (2008) 591–594

[28] D. Lucking-Reiley, Auctions on the Internet: what's being auctioned, and how? The Journal of Industrial Economics 48 (3) (2000) 227–252.

[29] T. Mathews, The impact of discounting on an auction with a buyout option: a theoretical analysis motivated by eBays buy-it-now feature, Journal of Economics 81 (2004) 25–52.

[30] P. McAfee, J. McMillan, Auctions and bidding, Journal of Economic Literature 25 (2) (1987) 699–738.

[31] K. Mount, S. Reiter, The informational size of message spaces, Journal of Economic Theory 8 (1) (1974) 161–192.

[32] D. Parente, R. Venkataraman, Millet, A conceptual research framework for analyzing online auctions in a B2B environment, Supply Chain Management: An International Journal 9 (4) (2004) 287–294.

[33] C. Parkes, H. Ungar, P. Foster, Accounting for cognitive costs in online auction design, in: P. Noriega, C. Sierra (Eds.), Agent Mediated Electronic Commerce, Lecture Note in Arti<sup>fi</sup>cial Intelligence, vol. 1571, Springer, Berlin, 1999, pp. 25–40

[34] S. Reiter, Information and performance in the new welfare economics, American Economic Review 67 (1)(1977) 226–234.

[35] S. Reynolds, J. Wooders, Auctions with a buy price, Economic Theory 38 (1) (2009) 9–39.

[36] A. Ruane, Real men and diplomats: Intercultural diplomatic negotiation and masculinities in China and the United States, International Studies Perspectives 7 (4) (2006) 342–359.

[37] L. Smeltzer, A. Carr, Electronic reverse auctions: promises, risks, and conditions for success, Industrial Marketing Management 23 (6) (2003) 481–488.

[38] S. Strecker, Information revelation in multiattribute English auctions: a laboratory study, Decision Support Systems 49 (3) (2010) 272–280.

[39] M. Strobel, C. Weinhardt, The Montreal taxonomy for electronic negotiations, Group Decision and Negotiation 12 (2) (2003) 143–164.

[40] G. Subramanian, Negotiauction: New Dealmaking Strategies for a competitive Marketplace, W. W. Norton & Company, MA, 2010.

[41] J. Teich, H. Wallenius, J. Wallenius, Multiple-issue auction and market algorithms for the world wide web, Decision Support Systems 26 (1) (1999) 49–66.

[42] J. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, Designing electronic auctions: an internet-based hybrid procedure combining aspects of negotiations and auctions, Electronic Commerce Research 1 (2001) 301–314.

[43] J. Teich, H. Wallenius, J. Wallenius, A. Zaitsev, A multi-attribute e-auction mechanism for procurement: theoretical foundations, European Journal of Operational Research 175 (1) (2006) 90–100.

[44] J. Thomas, J. Wilson, A comparison of auctions and multilateral negotiations, The RAND Journal of Economics 33 (1) (2002) 140–155.

[45] J. Thomas, J. Wilson, Veri<sup>fi</sup>able offers and the relationship between auctions and multilateral negotiations, The Economic Journal 115 (506) (2005) 1016–1031.

[46] W. Vickrey, Counterspeculation, auctions, and competitive sealed tenders, Journal of Finance 16 (1) (1961) 8–37

[47] E. Wolfstetter, Auctions: an introduction, Journal of Economic Surveys 10 (4) (1995) 367–420.

[48] L. Ye, Deterministic vs, stochastic entry: a bene<sup>fi</sup>t of running an auction-negotiation hybrid mechanism, Working Paper. Department of Economics. The Ohio State University, 2007.

Long Pham is an Assistant Professor at Minot State University, USA and National Economics University, Vietnam. His research interests and publications are in the areas of e-commerce, negotiation, auction, NegotiAuction, and decision support.

Alexander Zaitsev is a M.Sc. in Mathematics and Systems Programming graduate from Moscow State University. His research interests include systems analysis, multiple criteria decision making, non-linear approximation, electronic commerce implementations and online advertising optimization.

Robert Steiner is a Professor at New Mexico State University. His interests and publications are in the areas of applied statistics.

Jeffrey E. Teich is a Professor at New Mexico State University. His research interests and publications are in the areas of e-commerce, negotiation, auction, NegotiAuction, and decision support.
