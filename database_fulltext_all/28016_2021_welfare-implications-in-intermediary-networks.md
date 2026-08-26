---
otero_id: 28016
otero_key: "QTU59NBD"
title: "Welfare Implications in Intermediary Networks"
authors: "Thành Nguyen; Karthik Kannan"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0970"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Welfare Implications in Intermediary Networks

Thanh Nguyen,\` <sup>a</sup> Karthik Kannan<sup>a</sup>

<sup>a</sup> Krannert School of Management, Purdue University, West Lafayette, Indiana 47907

Contact: nguye161@purdue.edu (TN); kkarthik@purdue.edu, https://orcid.org/0000-0002-9861-0717 (KK)

Received: April 29, 2017<sub>Revised:</sub> 2020 Accepted: Published Online in Articles in Advance: March 11. 2021

https://doi.org/10.1287/isre.2020.0970

Copyright:

Abstract. We study the welfare implications of competing middlemen in a two-sided market, where goods are intermediated between providers and purchasers. In our model, each intermediary sets the quantities it intermediates, and the prices are a consequence of a Cournot competition. Our analysis shows that, unlike traditional markets, increasing competition is not always beneficial for market efficiency and that mergers can have an ambiguous effect on efficiency. We also analyze how the underlying network influences social welfare. We define a parameter called the intermediary capacity of the network and show how the price of anarchy depends on this parameter. These results suggest an intuitive and simple measure for the level of competitiveness in a networked market involving intermediaries.

History: Kai-Lung Hui, Senior Editor; Marius Niculescu, Associate Editor. Funding: T. Nguyen is partly supported by National Science Foundation [Grant 1728165]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2020.0970

Keywords: network economics • ad-exchange • ride-sharing • market competition in networks

## 1. Introduction

Because of digital technologies, platform markets— where an intermediary enables connections between providers and purchasers of services—are becoming popular. In addition to the new-age companies (such as Uber, Google, and Facebook), many leading “traditional” companies, including Cummins, Kaiser Permanente, and GE, are developing their digital platform strategies. They perceive the push toward a platform business model as being critical to their survival (Accenture 2016). So, an extensive and growing literature is now focused on developing platform strategies from a single firm’s perspective. However, very few prior works study the implications of platforms in a competitive environment. Understanding the ecosystems of competing and heterogeneous platforms is important because it provides insights for not only individual companies but also the policymakers. For example, when discussing the platform markets, Assistant Attorney General Makan Delrahim said, “[W]e, as antitrust enforcers, need to pay close attention to competitive constraints, to first make sure we don’t enforce away pro-competitive business models, but also to be vigilant that conduct does not unreasonably constrain the ability of new competitors to compete on the merits” (Delrahim 2019). The nature of competition in the platform markets is evolving. We first started to think about this research question because of the following anecdote.

In 2008, Google and Yahoo proposed a joint partnership that would have allowed Yahoo to use Google’s ad service to intermediate and deliver ads for Yahoo as well as its partners’ sites in the United States and Canada. The benefits of this agreement were mentioned in Drummond (2008):

We feel that the agreement would have been good for publishers, advertisers, and users—as well, of course, for Yahoo! and Google. Why? Because it would have allowed Yahoo! (and its existing publisher partners) to show more relevant ads for queries that currently generate few or no advertisements. Better ads are more useful for users, more efficient for advertisers, and more valuable for publishers.

However, the agreement never materialized because of antitrust concerns:

After four months of review, including discussions of various possible changes to the agreement, it’s clear that government regulators and some advertisers continue to have concerns about the agreement. Pressing ahead risked not only a protracted legal battle but also damage to relationships with valued partners. . . . [S]o, we have decided to end the agreement. (Drummond 2008)

Since then, this market has undergone significant changes. Mergers are quite commonplace: Microsoft bought aQuantitative in 2012, and Yahoo purchased Interclick in 2011. Such mergers are not limited to advertising markets. The ride-sharing market is also undergoing a significant transformation. In that sector, Lyft and Didi Chuxing were initially in a partnership to thwart Uber. Eventually, Uber merged its operation with Didi Chuxing. Yet another example is in the e-commerce space, where online market-makers are intermediaries connecting sellers and buyers. Amazon and Walmart competed fiercely to buy the Indian online retailer Flipkart, which Walmart eventually won. The issues we study in our paper are not just specific to the new age markets but also are relevant to other markets with similar intermediated structures. The network services segment is evolving with “intermediaries” such as AT&T acquiring other intermediaries such as DirectTV. Similarly, retailers may be viewed as simply intermediating between manufacturers and consumers. Our analysis provides insights into such cases also. For example, in such an intermediated ecosystem, we show that there are sources of inefficiency raised by intermediaries and networks that do not exist in traditional models. Given our generic focus, our model is set up to be agnostic to contexts. The examples provided throughout the paper are meant to help a reader connect different entities in our model to reality.

An oft-cited rationale against this kind of proposed agreement has been that mergers and coalitions among firms increase the monopoly power and harm both consumer surplus and social welfare. While this rationale may be appropriate in traditional markets involving only one type of customer, such an analysis does not always extend to two-sided markets. Even the Supreme Court is open to considering such alternatives: “We have therefore felt relatively free to revise our legal analysis as economic understanding evolves and. . .to reverse antitrust precedents that misperceived a practice’s competitive consequences” (Wilson and US Comissioner 2019). Such mergers or even agreements may allow participants (say, buyers, advertisers, or passengers) on one side to access participants on the other (correspondingly, sellers, publishers, or drivers). By opening up access to the other market, the coalition may facilitate more transactions between the two sides, improving social welfare as a whole. To illustrate the complexity of the intermediary networks, consider the highly stylized network structure in the two scenarios shown in Figure 1.

In scenario I, three intermediaries A, B, and C are competing to deliver a service for purchasers 3 and 4 by providers 1 and 2. In scenario II, A and B merge. Trade-offs need to be considered because of the mergers. Notice that, in scenario I, A and B compete to deliver service by 1 to 4; but C is the only intermediary between 2 and 3. On the other hand, when A and B merge, the merged firm AB becomes a monopoly when serving 1 and 4; however, the merged entity now competes with C to deliver service for purchaser 3 by provider 2. Thus, unlike the traditional seller-buyer models, the merging of intermediaries can even increase competition. As a result, the overall efficiency of such an economy depends critically on the underlying network structure. This means that, in large and complex networks, understanding the implications of antitrust policies becomes difficult. In this paper, we present this idea more formally. In addition, we ask the following question. Can we use a simple but intuitive set of network parameters to estimate the level of efficiency? The answers to this question not only give insights into the nature of competition among the intermediaries in a networked market but also provide guidelines for conducting policy analysis when comparing alternate network structures. As platform-based markets continue to grow, one can anticipate more partnerships, mergers, and acquisitions. Hence, understanding the welfare implications of these markets is becoming increasingly important.

We investigate the welfare implications of a marketplace involving multiple intermediaries. An intermediary may serve multiple providers (e.g., web publishers with ad-slots, ride-sharing drivers) and purchasers (e.g., advertisers, ride-sharing passengers, respectively). A provider or a purchaser may connect with multiple intermediaries. The dependencies create a networked market structure. We study how the nature of the networked structure has welfare implications.

For the study, we formulate the problem initially as a three-partite graph with the edges corresponding to the networked structure. This structure is reduced to a bipartite graph by making assumptions. In the real markets, the price-clearing mechanisms generally vary—for example, generalized second price (GSP) is used in the ad auctions or dynamic “surge prices” for ride-shares. We employ a Cournot competition model as the price-clearing mechanism. As we will expand later, Cournot has been used in prior works to effectively capture competition—the competition among the providers themselves and purchasers themselves. Such a model was also used extensively when studying welfare implications in traditional markets. With that pricing mechanism, when the intermediaries act optimally, the problem can be reduced to a single convex program, the solution of which corresponds to the decisions of the individual intermediaries at equilibrium. A key feature of the resulting quadratic program is that it allows us to identify a unique equilibrium. Thus, the problem is amenable to some robust comparative static analysis.

Figure 1. Two Different Networks: Before and After Merging of A and B  
![](/api/attachments/QTU59NBD/fulltext/images/6bb2c06d247a611acd9bcffb429afaa4cd763bc3e2fbb0fdfe4e398fee017f75.jpg)  
I: Three intermediarv network

![](/api/attachments/QTU59NBD/fulltext/images/e60a6e61aa3cf078db2492eede0294068351d8161dc33775d0c35cb03878d679.jpg)  
II: Merging of A and B

With the convex program, we provide several comparative analyses. We show that competition in an unbalanced market can reduce social welfare. Mergers in sparse markets, however, can create competition and improve market efficiency. This is a seemingly counterintuitive result different from the results in traditional markets. We also study how well the best social welfare obtained using the networked structure in equilibrium compares with the maximum social welfare by using the price of anarchy. The price of anarchy is dependent on the intensity of competition, which we capture through a measure we call the intermediary capacity of the network. Specifically, we find that the larger the intermediary capacity of the network, the more efficient the equilibrium.

The rest of the paper is organized as follows. In the following section, we survey the related literature. Section 3 formally defines the model, which is analyzed in Section 4. Section 5 provides new insights about how competition and mergers influence welfare. Section 6 studies the impact of the network structure on the level of efficiency. Section 8 concludes the paper.

## 2. Literature Review

Our work relates to several streams of research. The first stream is the well-established literature on platform-based markets. The second stream is the literature on networked markets that is nascent but growing extensively. We provide a brief survey of the first stream and a somewhat more extended one of the second. Since there is some related work in individual contexts (ad markets, ride-sharing, etc.) we also provide a brief survey of the related work as the third subsection.

## 2.1. Platform Economics

Our paper studies intermediaries that connect different sides of a market as found in the literature on network-effect-based platforms. This domain has been extensively researched. The early focus on this literature was on single-sided networks (e.g., the seminal work by Katz and Shapiro (1985)) but has expanded in recent years to include multisided platforms (e.g., Parker and Van-Alstyne (2005) study two-sided networks). Many papers have analyzed the strategic aspects of managing these network-based platforms. For example, they analyze what the pricing strategies should be and how to launch a networkeffect-based market.

A few recent papers have also studied welfare implications. Lee (2014) has studied the problems involving single-sided networks. Others (Weyl 2010, Evans and Schmalensee 2013) have studied it with respect to the two-sided markets. To the best of our knowledge, these papers have not considered the welfare implications of mergers across the intermediaries. Moreover, the “network” effects studied in these papers are very different from ours. In particular, most papers in the platform economic literature model symmetric environments and focus on the externality/ complementarity effect that a platform creates for its members. This is, for example, integrated directly into a member’s utility that depends on how many others are using the same platform. Our paper, on the other hand, moves away from such effects to focus on the impact of heterogeneity in the connection struc ture. This other type of “network effect” is actively investigated by a relatively new but fast-growing literature on network markets that we survey next.

## 2.2. Network Markets

Most of the early literature on network markets focuses on seller-buyer networks. Kranton and Minehart (2001), Corominas-Bosch (2004), Polanski (2007) Manea (2011), Abreu and Manea (2012), and Elliott (2015) are a few examples. By assumption, all these papers rule out intermediaries and focus only on the trade between buyers and sellers.

Blume et al. (2009) was among the first to investigate a mediated market in a network setting. The network structure in our paper is similar to that of Blume et al. (2009). However, Blume et al. (2009) consider Bertrand competition among intermediaries and assume buyers have unit demand. In twosided markets, such as ad-networks, considering multiunit demand and supply with heterogeneity among the players is more relevant. In the context of adintermediaries, agents target different amounts of impressions, and trades are executed by market-clearing auctions. It is natural, therefore, to study such a network using a Cournot model, which we do in this paper Such a characterization is a unique feature of our model. Because of the differences in the model characterizations, the equilibrium outcomes are also different. All equilibria in Blume et al. (2009) are efficient, whereas, that is not the case in our model. Hence, our main aim of measuring the level of efficiency based on the structure of the underlying network is relevant.

Our paper is closely related to recent models of Cournot competition in networks by Bimpikis et al. (2019b) and Perakis and Sun (2014). However, unlike us, they do not consider intermediaries. On the contrary, we show in Section 5 new insights on how competition and mergers of intermediaries influence welfare. These effects are absent in models without intermediaries such as Bimpikis et al. (2019b) and Perakis and Sun (2014). For example, Bimpikis et al. (2019b) study mergers of firms in a two-sided market. The effect on welfare for that type of merger is different from that in our paper. The mathematics behind them are also different. Our paper shows that the unique equilibrium can be characterized by a convex program.<sup>1</sup> Note that with network games, for a general class of utilities, it is quite hard to prove the existence of equilibrium, let alone prove uniqueness. For example, in Bimpikis et al. (2019b), they need additional assumptions such as positive trade occurring in all links for the comparative analysis.

Our model formulation employs a model of Cournot competition. Bose et al. (2014) also studies intermediaries and market-makers in a Cournot game. The main question that Bose et al. (2014) addresses is how to modify the objective of market-makers to maximize social welfare. Here, we focus on how the network structure influences efficiency.

Several recent papers have studied intermediaries, including Nguyen (2015, 2017) and Manea (2018). The settings in these papers, however, are quite different from ours. In particular, they study the incentive of noncooperative bargaining and assume unit-demand agents. Even though, in the advertising industry, bargaining is part of the contracts, automated auctions control the majority of the interactions among the agents in those studies. Feldman et al. (2010) study the equilibrium properties in a model where buyers buy ad slots from a central buyer via a set of competing intermediaries. They demonstrate how the interaction between the auction design and double marginalization affects outcomes. Our paper differs from this work in that intermediaries in our model connect between multiple buyers and sellers and in that the prices are determined by the Cournot (sub)markets.

## 2.3. Context-Speci<sup>fi</sup>c Literature

Digital and search ads have received significant attention from various disciplines, including computer science, marketing, information systems, and economics. A seminal piece in this regard is by Edelman et al. (2007), who analyzes the equilibrium of the GSP auction. Variants of GSP have been implemented and also studied. Feng et al. (2007) using simulations and Balachander et al. (2009) using game theory compare alternative GSP auction policies. More generally, papers have also evaluated the welfare implications of the search ads market. Usually, they are executed in the context of a single ad intermediary. For example, Chen and He (2011) evaluated the efficiency of ads on the consumer search process. Similarly, welfare implications are also studied when considering policy changes for the auctions. As another example, Shin (2015) study the subject of search engines requiring budget constraints for advertisers in GSP auctions. More generally, computer science has extensively studied mechanism design problems in the ad-network context. One stream within this literature employs matching algorithms—specifically, how to match ads to positions (Mehta et al. 2007, Caragiannis et al. 2015). Note that we focus on multiple search ad intermediaries.

The literature on ride-sharing has been expanding rapidly in recent years (Banerjee et al. 2017, Cachon et al. 2017, Fang et al. 2017, Bimpikis et al. 2019a). The focus of this literature, however, has been on the optimal design of a monopoly’s matching and pricing mechanisms. Our paper, on the other hand, considers the problem from an industry-level perspective. Given that there are many competing platforms and the connections of these platforms with the two sides of the markets are heterogeneous, our paper analyzes the impact of such an underlying network structure on the efficiency of the whole ecosystem.

## 3. The Model

Many intermediated markets are highly dynamic, and the demand and supply of quantities are often ephemeral. It is often quite hard to capture the changing aspects of a model. Given our focus on studying welfare implications, for the sake of trac tability, we study a single-period game using a stylized static competitive model. Let G be an exogenous tripartite network involving I intermediaries, J providers, and K purchasers, where the set of edges connect the J providers with the I intermediaries and also the I intermediaries with the K purchasers. The producers and purchasers cannot transact without an intermediary. Figure 2 shows a possible structure for decentralized competition among intermediaries that we study. Note that it is not a fully connected graph. If an edge does not exist, it indicates that trade cannot be facilitated by the corresponding intermediary with the purchaser/producer. Using this structure, we analyze the welfare implication as the number of intermediaries or when the connections to the purchasers/ producers endogenously change while retaining the J producers and K purchasers.

Figure 2. (Color online) An Example Structure of Networked Competition  
![](/api/attachments/QTU59NBD/fulltext/images/f0bce97d1f8eb31155f65890d4f90909a7274669e47867a7760e33151eb50d7f.jpg)

The providers and purchasers in our model are heterogeneous. A provider j faces an increasing convex cost $C _ { j } ( \chi )$ with respect to the amount of goods/ service produced, $\chi . ^ { \bar { 2 } }$ For simplicity, we assume $\begin{array} { r } { C _ { j } ( \chi ) = \theta _ { j } \chi + \frac { \alpha _ { j } } { 2 } \chi ^ { 2 } } \end{array}$ , where $\alpha _ { j }$ and $\theta _ { j }$ are nonnegative coefficients exogenous to our model. (It is normalized so that $C _ { j } ( \chi = 0 ) = 0 . ) ^ { 3 }$ In the advertising market, $\chi$ corresponds to the number of ads shown, and a convex cost is consistent with the dissatisfaction that ads impose on web page viewers. In the ride-sharing context, the convex cost captures the inconvenience the drivers face from driving for long hours.

The utility of the purchaser k for the goods/services sold by provider j is $U _ { j k } ( Y )$ , which is concave in the quantity Y for all $j , k . ^ { 4 }$ Specifically, we assume that $\begin{array} { r } { U _ { j k } ( Y ) = \mu _ { j k } Y - \frac { \beta _ { j k } } { 2 } Y ^ { 2 } } \end{array}$ , where $\beta _ { j k }$ and $\mu _ { j k }$ are nonnegative coefficients exogenous to our model. (It is also normalized such that $U _ { i k } ( Y = 0 ) = 0 . )$ For the initial set of insights, we assume that the payoff for purchaser k is separable as follows: $\begin{array} { r } { \sum _ { j } U _ { j k } \big ( \bar { \cdot } \big ) } \end{array}$ —that ${ \mathrm { i } } \mathbf { s } ,$ , the utilities generated from different providers can be added. We later extend the basic model in Section 7 to capture the substitutability of goods.

Notice that we assume cost C to be independent of the purchaser while the utilities U depend on the suppliers. In the ad exchange, for example, the cost depends on the space that ad slots take and it is independent of the specific ad; whereas for the advertisers, ads on different websites bring different values.

Let $y _ { j k } ^ { i }$ be the amount of goods/service intermediated by i between j and k. The network structure constrains the pairs of providers and purchasers that intermediary i cannot facilitate trade between. Specifically, $y _ { j k } ^ { i } = 0$ if $j$ and k are not connected via i. Let $\begin{array} { r } { Y _ { j k } = \sum _ { i } ^ { } y _ { j k } ^ { i } } \end{array}$ be the total amount of goods provided by j to k, let $\begin{array} { r } { x _ { j } ^ { i } = \sum _ { k \in K } y _ { j k } ^ { i } } \end{array}$ be the amount from provider j intermediated by $i ,$ and let $\begin{array} { r } { X _ { j } = \sum _ { i } x _ { j } ^ { i } } \end{array}$ be the amount requested from all the intermediaries for provider j.

## 3.1 Decision-Making and Competition

Whether prices or quantities should be the decision variable has long been debated (Bertrand versus Cournot models). Early papers on welfare implication in traditional markets have used Cournot model (Farrell and Shapiro 1990). Given our interest in studying the welfare implications of networked markets, we also employ a model where quantities are strategically chosen.

In our model, the intermediaries strategically choose the quantities, and the purchasers/producers respond to them. This assumption that the interme diary is the lead player is consistent with reality where the intermediaries generally have had the power to set policies.<sup>5</sup> For example, in many markets, the intermediaries choose the market-clearing (or price-determining) mechanisms: be it GSP for ad auctions or surge prices for ride-sharing contexts. Another way to note the power position is to compare the number of providers or purchasers versus the intermediaries. Since typically a fewer number of intermediaries (e.g., Google, Uber, Lyft) exist, it is reasonable to assume the intermediaries hold power.<sup>6</sup> Next, we describe how our setup is framed as a Cournot model.

Before we describe our model, note the following key features about a standard Cournot model:

• The demand curve assumed in the standard Cournot model is nothing more than the marginal benefit curve of the entire set of customers. The marginal benefit curve is simply the aggregation of the marginal utility curves of individual consumers with no assumption on how many consumers generate the aggregate utility. Therefore, independent on whether it is single or multiple consumers, the de mand function is the marginal benefit curve.

• Given an aggregate x chosen by the firm and the aggregate utility $U ( \cdot ) _ { \cdot }$ , the market clearing price is the price that maximizes $U ( x ) - p \cdot x$ when the aggregate consumption of all the customers is $x .$ . This explains why the market-clearing price is equal to the marginal benefit curve and also that demand equals supply.

• In a standard Cournot model, the marketclearing price is obtained from a multiunit uniformprice auction when the number of units auctioned equals the aggregate quantities set by the firms. The market-clearing price as the inverse demand function can be implemented with minimal requirements on the knowledge of private information. ${ \mathrm { S o } } ,$ , we assume that the firm(s) are aware of the market-clearing price. Prior work has used this approach for various economic environments. For example, Milgrom (2004) argues that, in a model with positive supply elasticity, the “auction outcomes resemble a Cournot competition among buyers” when modeling the Federal Communications Commission (FCC) spectrum auctions. Vasin and Kartunova (2016) studies the electricity markets using a similar structure. Even in ad-auctions, Nava (2015), Ashlagi et al. (2018), and Bimpikis et al. (2019b) use Cournot models for their analyses. Daughtery (2008) provides a survey of such works that have used Cournot models. A work cited in their survey is Klemperer (1986), who shows the conditions when their modeling of a competition resembles Cournot outcomes.

• The Cournot model is laid out in a purchasing or procuring setting. (1) The firms may supply a quantity of goods to sell to purchasers/consumers; or (2) the firms may procure a certain quantity from providers/ sellers. The bullet points so far have focused on the latter setting.

Our model combines both the producer- and purchasermarkets, with intermediaries as the lead player in both and also intermediating between the two. Our information structure is no different from the standard Cournot structure: the intermediaries are aware of the market-clearing price, which corresponds to the marginal benefit (equivalently, supply) function that is independent of the number of purchasers (equivalently, producers) generating the aggregate utility (equivalently, supply). In this regard, as Endnotes 4 and 6 mention, the purchasers and producers could themselves correspond to multiple agents. We additionally assume that, in our network, the intermediaries do not even need to know the network structure but only their connections.

The equilibrium of our Cournot model may be viewed as the convergence of a tatonnement process. The intermediaries can adjust their quantities if they can improve their payoff. At each step of this adjustment process, they do so by changing these quantities by a small amount to test price elasticity and to observe if these are indeed profit improving. Each step of this process requires little private information and thus naturally reflects the dynamic of a real market.

For all these reasons, the Cournot approach models the essential elements of a complex market. To be tractable, it necessarily abstracts away from details, such as bargaining and optimal contract design. Our paper, therefore, uses this approach as a natural model to study the effects of network structure on competition and welfare of the market.

## 3.2. Inverse Demand/Supply Functions

Recall that the aggregate quantity requested from a provider j is $\begin{array} { r } { X _ { j } = \sum _ { i , k } y _ { j k } ^ { i } } \end{array}$ and the aggregate quantity offered to a purchaser k is $\begin{array} { r } { Y _ { j k } = \sum _ { i } y _ { j k } ^ { i } } \end{array}$ . The “inverse supply function” for producer j is adapted to our model as follows: given any aggregate quantity χ from all the intermediaries, what should be the price paid to incentivize the provider j to offer that same quantity (i.e., incentive compatibility (IC) condition)

$$
\chi = \arg \max _ {x} P _ {j} \cdot x - C _ {j} (x).
$$

By taking the first-order differentiation, the price $P _ { j }$ is the marginal cost at $\chi .$ . Because $\begin{array} { r } { C _ { j } ( x ) = \theta _ { j } \chi + \frac { \alpha _ { j } } { 2 } x ^ { 2 } . } \end{array}$ , we obtain the following inverse supply function:

$$
P _ {j} = \theta_ {j} + \alpha_ {j} \cdot \chi .\tag{1}
$$

Similarly, the “inverse demand function” for the purchaser can be interpreted similarly. The price willing to be paid must equal the marginal benefit realized by the purchaser from delivering Y goods from j to k:

$$
R _ {j k} = \mu_ {j k} - \beta_ {j k} \cdot Y.\tag{2}
$$

Note that our model can be adapted to fit certain real situations.<sup>7</sup> There are often many other idiosyncratic features of every market also. Our objective is not focused on capturing every possible feature. Using a parsimonious model, we intend to provide the first set of first-order insights. So long as the tensions associated with those insights exist, the welfare outcomes will be similar. With this mind, we provide in the following subsection interpretations of the model and “inverse supply/demand functions” in two settings: ad-exchange networks and ride-sharing platforms.

3.2.1. Ad-Exchange. An ad-exchange may be a large market, and we can view each provider j as a group of publishers having similar types of ad positions— for example, possible ad positions across the sports sections of various online magazines. We call this a buying submarket j. Similarly, each purchaser k can be thought of as a group of advertisers with similar characteristics—sellers of sneakers and gym equipment. We call this a selling submarket k. Intermediaries buy ad quantities from publishers and sell them to advertisers. Then, $y _ { j k } ^ { i }$ is the amount of trade transacted between j and k via intermediary i.

Next, we describe the market mechanisms that give rise to the inverse supply and demand functions. At the buying submarket j, all the intermediaries together are interested in buying $\begin{array} { r } { X _ { j } = \sum _ { i } x _ { j } ^ { i } } \end{array}$ number of ad positions. To determine the unit price to be charged, a uniform-price ascending auction is run until the supply reaches the demand X . In particular, for every publisher in this submarket, an additional ad position has a marginal cost that is increasing in the number of ad positions already allocated to it. This is to capture the increasing constraints and costs as the number of advertising positions increases for the seller.

If p is the unit price in the auction and $c ( x )$ is the cost for one publisher, then the publisher chooses the optimal x that maximizes $p \cdot x - c ( x )$ —the optimal x is such that the marginal cost for the seller is $c ^ { \prime } ( x ) = p$ . The cost functions may be different across the publishers. Suppose we are able to aggregate the marginal cost across all the publishers in this submarket as follows: $f ( X ) = \theta _ { j } + \alpha _ { j } \bar { X }$ . That is, if we sort the ad slots in increasing order of marginal cost across the individual publishers, the marginal cost of the Xth slot is assumed to be f X . Then, given $X _ { j } ,$ the ascending auction stops when $P _ { j } = \theta _ { j } \overset { \cdot } { + } \alpha _ { j } X _ { j }$

Similarly, consider the selling submarket k. This is similar to the provider case. Suppose, for any $k ,$ the aggregate marginal utility of all the advertisers at submarket k for ad position from publisher $j$ is $g ( Y ) = \mu _ { j k } - \beta _ { j k } \cdot Y$ . That is, if the marginal utility of each advertiser is sorted in decreasing order, then the marginal utility of the Yth unit ad is $g ( Y )$ . For each type of ad position ${ } _ { j , \ l }$ intermediaries sell $\begin{array} { r } { Y _ { j k } = \sum _ { i } y _ { j k } ^ { i } } \end{array}$ ad slots in this submarket, and the market-clearing price given by an auction will be $R _ { j k } = \mu _ { j k } - \beta _ { j k } \cdot Y _ { j k }$

The uniform-price ascending auction in these submarkets has a natural interpretation in practice. This is because ad exchange in each of the submarkets is often managed by aggregators, who use auctions to clear the market.

3.2.2 Ride Sharing. Now, consider a different interpretation. A provider node j represents a group of drivers of similar characteristics (location and the type of cars); we call them a type of providers. A purchaser node k represents a group of riders requesting a ride in a specific region: call it a demand region. An intermediary (Uber or Lyft) manages the matching between supply and demand.

One unit of trade in this economy is one unit of riding service (measured by either time or distance). The price paid to providers can be seen as the average payment to drivers per riding unit. The price paid by purchasers corresponds to the average payment from the riders per unit of service. The quantities decided by the intermediaries are the average market shares for certain levels of service at certain locations.

Given the supply and demand curve, each platform decides the quantities. At the market equilibrium, the average price paid to the same type of driver should be the same across platforms; otherwise, drivers will exclusively choose the platform with the best price. Furthermore, at this price, the amount of service offered by the drivers should be the same as the total market share across platforms. The same logic holds for the riders. The Cournot competition exactly captures this aspect of competition. Namely, depending on the number of rides enabled, the market price will be endogenously determined depending on the demand and supply curves of the providers and purchasers. Specif ically, we assume each provider in j has an increasing marginal cost for providing service. It gives rise to the supply curve increasing in $P _ { j } ,$ , which we assume is:

$$
X _ {j} = \max \bigl \{0, a \cdot P _ {j} - b \bigr \}.
$$

Similarly, the demand curve at a demand region k for a specific type of provider j decreases in the price $R _ { j k }$ and is assumed to be:

$$
Y _ {j k} = \max \{0, b ^ {\prime} - a ^ {\prime} \cdot R _ {j k} \}.
$$

By changing notation $a , b , a ^ { \prime } , b ^ { \prime } .$ , we obtain equiva lently Equations (1) and (2).

3.3. Summary of Characterizations and De<sup>fi</sup>nitions In summary, we consider a networked market involving intermediaries and heterogeneous purchasers and providers. Even though such markets tend to be highly dynamic markets in reality, we study their equilibrium in a “steady” state. This can be modeled as a single-period game involving multiple intermediaries, each of which chooses $y _ { j k } ^ { i } .$ . Recall that these choices determine $X _ { j } ,$ which affect the inverse supply function, and $Y _ { j k } ,$ , which affect the inverse demand function on the purchaser sides. They in turn determine the prices to be paid to the producers and the revenues from the purchasers.

So, each intermediary i’s payoff is the difference between the money paid by the purchasers and the amount paid to the providers:

$$
\Pi_ {i} (\vec {y}) = \sum_ {j k} R _ {j k} y _ {j k} ^ {i} - \sum_ {j} P _ {j} \sum_ {k} y _ {j k} ^ {i},\tag{3}
$$

where $\vec { y }$ correspond to the vector of quantities chosen by the intermediaries, that is, $\vec { y } = \{ \vec { y ^ { 1 } } , \vec { y ^ { 2 } } , \dots , \vec { y ^ { I } } \}$ , where each $\vec { y ^ { i } }$ is a matrix corresponding to $y _ { j k } ^ { i } .$ . The game described above is denoted as $\Gamma ( \bar { \mathcal { N } } , \theta , \mu , \alpha , \beta )$ . Then, we have the following definition of an equilibrium for the game:

De<sup>fi</sup>nition 1. A vector $\vec { y }$ is an equilibrium if no intermediary i can change his strategy $\vec { y ^ { i } }$ to $y ^ { \vec { i ^ { \prime } } }$ to obtain a better payoff given by (3). That is,

$$
\Pi_ {i} \left(y ^ {\vec {1}}, \dots , y ^ {\vec {i ^ {\prime}}}, \dots , y ^ {\vec {I}}\right) > \Pi_ {i} \left(y ^ {\vec {1}}, \dots , y ^ {\vec {i}}, \dots , y ^ {\vec {I}}\right).
$$

The game can be characterized as a bipartite graph involving purchasers and producers, with the edges having $Y _ { j k }$ as the weights. This bipartite graph is useful when studying social welfare. The total social welfare is a measure of how efficient the allocation of providers to purchasers is. We compute it by adding the total surplus of providers, purchasers, and intermediaries:

De<sup>fi</sup>nition 2. Given a strategy profile ${ \vec { y , } }$ social welfare is

$$
\begin{array}{c} S W (\vec {y}) = \sum_ {j k} U _ {j k} (Y _ {j k}) - \sum_ {j} C _ {j} (X _ {j}) \\ = \sum_ {j k} \bigg (\mu_ {j k} Y _ {j k} - \frac {1}{2} \beta_ {j k} Y _ {j k} ^ {2} \bigg) - \sum_ {j} \bigg (\theta_ {j} X _ {j} + \frac {1}{2} \alpha_ {j} X _ {j} ^ {2} \bigg). \end{array}\tag{4}
$$

## 4. Equilibrium Characterization

We illustrate the equilibrium with an example for two reasons. The first is to show how the variables we defined earlier correspond to supply and demand functions. The second is to provide a figurative perspective on social welfare.

Example 1. Consider the example with one provider, one purchaser, and one intermediary. The intermediary’s decision variable is the amount, $y ,$ to buy from the provider and to deliver for the purchaser. We assume that the marginal cost for the provider is $1 + y$ and the marginal gain for the purchaser in the market is $2 - y$ . Then, the intermediary pays the provider $P =$ 1 y and charges the purchaser $\begin{array} { r } { R = 2 - y . } \end{array}$ So, the intermediary maximizes

$$
\max _ {y} \{R \cdot y - P \cdot y = (2 - y) y - (1 + y) y \mid y \geq 0 \}.
$$

It is straightforward to see that the optimal solution is $y = 1 / 4$ . Figure 3 shows the equilibrium obtained as a consequence of plotting the marginal utilities and marginal costs. The intermediary surplus is represented as the shaded rectangle in the same figure. Note that only 1/4 units of goods are transferred from the provider to the purchaser. The picture also shows the consumer surplus generated by the purchaser and the provider separately. The total social welfare obtained is the sum of all these components and is shaped like parallelogram ADEC.

Figure 3. (Color online) Illustrating the Welfare Metrics Associated with Example 1  
![](/api/attachments/QTU59NBD/fulltext/images/7f641f2a64f5de69d13912ebfe369f58da09feb6e6e37c8305d1e352afa8c004.jpg)

From an efficiency standpoint, we can see that, when supply meets demand, that is, $2 - y = 1 + y ,$ , we have the maximum welfare obtained when $y = 1 / 2$ This maximum welfare corresponds to the area of the triangle ABC in the same figure. That corresponds to when the intermediary makes zero profit. In this scenario involving only one provider and one purchaser, increasing the number of intermediaries will always improve social welfare. However, that may not be the case when the market structure and net works are different, as will be shown later.<sup>9</sup>

In general, equilibria are hard to characterize in games with complex network structure but equilibrium always exists in our model. Furthermore, the equilibrium is unique and can be characterized by a convex program. Hence, we can study the sensitivity of the network structure on various metrics. This section characterizes the nature of the equilibrium.

Because $\begin{array} { r } { x _ { j } ^ { i } = \sum _ { k } y _ { j k } ^ { i } , } \end{array}$ , the payoff of intermediary i expressed in (3) can be written as

$$
\begin{array}{r l} & {\sum_ {j, k} (\mu_ {j k} - \beta_ {j k} Y _ {j k}) y _ {j k} ^ {i} - \sum_ {j} (\theta_ {j} + \alpha_ {j} X _ {j}) x _ {j} ^ {i}} \\ & {\qquad = \sum_ {i, j, k} (\mu_ {j k} - \theta_ {j}) y _ {j k} ^ {i} - \sum_ {j, k} \beta_ {j k} Y _ {j k} y _ {j k} ^ {i} - \sum_ {j, k} \alpha_ {j} X _ {j} y _ {j k} ^ {i}.} \end{array}
$$

Observe that, for every $i \in I ,$ , the utility function above can be seen as a concave function o ${ \vec { y } } .$ . Furthermore, notice also a constant Z exists such that i $\dot { y } _ { j k } ^ { i } > Z ,$ , then the payoff above is negative. Therefore, the game we consider is a bounded, concave game. Because of Rosen (1965), such a game has a pure equilibrium.

Given the specific payoff structure in our game, we can provide additional insights. For example, the equilibrium is unique and can be characterized as follows.

Theorem 1. $I f \alpha _ { j } > 0$ and $\beta _ { j k } > 0 ,$ , y is an equilibrium if and only if it is the unique solution of the following convex program with the unknowns ${ \vec { y } } , { \vec { x } } , \mathbf { \check { X } } ,$ , and ${ \vec { Y } } ;$

$$
\begin{array}{l} \min: \sum_ {j} \frac {\alpha_ {j}}{2} (X _ {j}) ^ {2} + \sum_ {i j} \frac {\alpha_ {j}}{2} (x _ {j} ^ {i}) ^ {2} + \sum_ {j, k} \frac {\beta_ {j k}}{2} (Y _ {j k}) ^ {2} + \sum_ {i, j, k} \frac {\beta_ {j k}}{2} (y _ {j k} ^ {i}) ^ {2} \\ \text {s.t.:} \alpha_ {j} X _ {j} + \alpha_ {j} x _ {j} ^ {i} + \beta_ {j k} Y _ {j k} + \beta_ {j k} y _ {j k} ^ {i} \geq \mu_ {j k} - \theta_ {j}. \end{array}\tag{5}
$$

The formal proof is given in the online appendix.

Remark 1. To gain some further intuition of the game, consider a centralized agent who on behalf of all the intermediaries facilitates trade between providers and purchasers to maximize welfare. The agent’s problem reduces to an optimization problem on the variables $\{ Y _ { j k } \}$ of the bipartite network for the pairs $\left( j , k \right)$ that are connected by at least one intermediary. The objective of that optimization problem is to maximize the total utility of the purchasers minus the total cost of the providers. Assume $Y _ { j k } ^ { * }$ is the welfare-maximizing solution.

In the equilibrium, each intermediary i individually decides on a set of $\{ y _ { j k } ^ { i } \}$ , where $( j , k )$ are connected via i. First, compared with the hypothetical centralized agent, the set of trade $( j , k )$ that the intermediary i can control is smaller. Second, multiple intermediaries can decide different amounts of trade on a pair of $( j , k )$ . The total trade resulting in equilibrium between $j , k$ k is $\begin{array} { r } { Y _ { j k } = \sum _ { i } y _ { j k } ^ { i } } \end{array}$ . Third, the intermediaries are payoff maximizers. Our paper studies how far away the equilibrium outcome $Y _ { j k }$ is from the welfare-maximizing solution $Y _ { j k } ^ { * }$

Hence, from a welfare perspective, the tripartite graph reduces to a bipartite structure. We exploit this feature in Section 6. However, to understand the equilibrium behavior, the structure of the original tripartite graph is important because it captures the set of possible trades between providers and purchasers that a particular intermediary can transact.

## 5. Insights from Networks: Increasing Competition and Merging Intermediaries

Having established the equilibrium, we can now identify insights about the effect of network structures on market efficiency. In particular, we provide two illustrative examples. The first shows that increasing competition is not always beneficial for market efficiency. The second shows that mergers have an ambiguous effect on efficiency. These examples highlight two insights into market inefficiency caused by intermediaries that are absent in standard Cournot models.

## 5.1. The Impact of Increasing Competition on Welfare

To demonstrate the effect of competition among intermediaries on market efficiency, consider the network shown in Figure 4. In this example, intermediary #1 solely serves purchaser $b ,$ but purchaser a is served by all $I + 1$ intermediaries, including #1. Such a scenario can happen when intermediary #1 is a large incumbent intermediary that has an exclusive connection to a specific market b while the other intermediaries are new, small firms competing on a smaller market segment, a. Analyzing such a network structure is useful for gaining insights. It is also convenient because the merger of any two intermediaries not involving #1 will again result in a network structure that can be studied with our generic formulation.

We simplify certain definitions and make additional assumptions for ease of exposition. Because there is only one provider, we simply denote $\alpha = \alpha _ { s } ,$ , Assuming $\mu _ { s a } = \mu _ { a } ,$ , and $\mu _ { s b } = \mu _ { b } .$ . The additional assumptions we make are as follows: $\theta _ { s } = 0$ for the providers, and $\beta =$ $\beta _ { s a } = \beta _ { s b }$ for the purchasers. Because intermediaries $2 , 3 , \ldots , I + 1$ are symmetric, $y _ { s a } ^ { \# j } = y _ { s a } ^ { \# 2 }$ and $x _ { s a } ^ { \# j } = x _ { s a } ^ { \# 2 }$ for any $1 < j \le I + \bar { 1 } . ^ { 1 0 }$ The equilibrium is therefore the optimal solution to the following program:

Figure 4. I 1 Intermediaries  
![](/api/attachments/QTU59NBD/fulltext/images/0883dd9af34e7389ea7524584ca8359d7f9392f0e4fb623ee920d0dfa9132b8c.jpg)

$$
\begin{array}{l} \min: \alpha \Big ((X _ {s}) ^ {2} + I \big (x _ {s} ^ {\# 2} \big) ^ {2} + \big (x _ {s} ^ {\# 1} \big) ^ {2} \Big) \\ \qquad + \beta \Big ((Y _ {s a}) ^ {2} + I \big (y _ {s a} ^ {\# 2} \big) ^ {2} + \big (y _ {s a} ^ {\# 1} \big) ^ {2} \Big) \\ \qquad + \beta \Big ((Y _ {s b}) ^ {2} + \big (y _ {s b} ^ {\# 1} \big) ^ {2} \Big) \end{array}
$$

$$
\begin{array}{r} \mathrm{s.t.:} \alpha X _ {s} + \alpha x _ {s} ^ {\# 2} + \beta Y _ {s a} + \beta y _ {s a} ^ {\# 2} \geq \mu_ {a}, \\ \alpha X _ {s} + \alpha x _ {s} ^ {\# 1} + \beta Y _ {s a} + \beta y _ {s a} ^ {\# 1} \geq \mu_ {a}, \\ \alpha X _ {s} + \alpha x _ {s} ^ {\# 1} + \beta Y _ {s b} + \beta y _ {s b} ^ {\# 1} \geq \mu_ {b}. \end{array}
$$

Notice that α and $\beta$ capture the market sensitivity of the provider (seller) and the purchasers (buyers), respectively. We next consider two extreme cases in order to gain intuition about this network structure. The first has $\alpha = 1 , \beta = 0 .$ , and the second has $\alpha = 0$ $\beta = 1$ . The main insight continues to hold for a wider range of $\alpha , \beta$ (see the online appendix).

Case 1: $\alpha = 1 , \beta = 0 .$

This scenario corresponds to the case where the marginal utility of the purchasers is much less sensitive to the amount of goods traded compared with the marginal cost of the supply side. With this, we obtain the following result.

Corollary 1. Take $\alpha = 1 , \beta = 0$

• For $\begin{array} { r } { \mu _ { a } < \mu _ { b } < \frac { 5 } { 4 } \mu _ { a } , } \end{array}$ , as I increases, the welfare will first increase and then decrease

• For $\begin{array} { r } { \frac { 5 } { 4 } \mu _ { a } \leq \mu _ { b } < 2 \mu _ { a } , } \end{array}$ , as I increases, the welfare will decrease.

• For $2 \mu _ { a } \leq \mu _ { b }$ the welfare is independent of I.

Corollary 1 is quite striking because it shows that competition among intermediaries can harm the market efficiency. In the online appendix, we provide the proof and use several numerical examples to show that the analysis is robust for a much wider parameter range.

Figure 5 provides two numerical examples to illustrate Corollary 1.

The intuition for the result is as follows. Imagine intermediary #1 as an incumbent monopolist serving market segments a and b that are quite different. When $\mu _ { a } < \mu _ { b } ,$ purchasers at b value the goods more than purchasers at a. Hence, an efficient allocation would allocate more goods to submarket b than to a. The monopolistic intermediary #1 can internalize this and trade in a reasonably efficient way. Suppose entrants $\# 2 , \ldots , \# I + 1$ arrive and they only trade in the smaller market. In that case, one can compute the equilibrium $y _ { j k } ^ { i } . ^ { 1 1 }$ Consider what happens when $\mu _ { a } < \mu _ { b } < 2 \mu _ { a }$ . As the competition for purchaser a increases, it increases the goods sold to the market— that is, $\begin{array} { r } { Y _ { s a } = y _ { s a } ^ { \# 1 } + I y _ { s a } ^ { \# 2 } = \frac { I } { I + 2 } ( 2 \mu _ { a } - \mu _ { b } ) } \end{array}$ increases with I. It also increases the price at s. However, this increase lowers the amount of goods that intermediary #1 sells to $\begin{array} { r } { b , Y _ { s b } = ( \mu _ { b } - \mu _ { a } ) + \frac { 2 \mu _ { a } - \mu _ { b } } { I + 2 } } \end{array}$ . When $\begin{array} { r } { \frac { 5 } { 4 } \mu _ { a } \leq \mu _ { b } < 2 \mu _ { a } , } \end{array}$ delivering goods to b is preferred from a social standpoint. When I increases in that case, the competition in market a only distorts the trade further away from the efficient allocation.

Next, consider the impact of competing intermediaries on the share of the surplus. When $\mu _ { b } > 2 \mu _ { a } ,$ intermediaries $\# 2 , \ldots , I + 1$ do not participate, and the equilibrium is independent of I. So, we focus on the more interesting case $\mu _ { a } \leq \mu _ { b } \leq 2 \mu _ { a } ,$ , in which we obtain the following result.

Corollary 2. Take $\alpha = 1 , \beta = 0 ,$ , and $\mu _ { a } \leq \mu _ { b } \leq 2 \mu _ { a }$

• As I increases, provider s’s and purchaser a’s payoff increase; but b’s utility decreases.

• The payoff of all the intermediaries decreases as I increases.

See the online appendix for the proof.

Case 2: $\alpha = 0 , \beta = 1$

The negative effect of competition on welfare described above is driven partly by the fact that the price at the providers is more sensitive to the amount of goods traded than the price at the purchasers. As we see from the calculation above, because of this, when the number of intermediaries increases, the competition pushes down the selling price at the provider. We will show next that this effect disappears when the price at the providers is not sensitive to the amount of goods traded.

Corollary 3. For $\alpha = 0 , \beta = 1$ , increasing the number of intermediaries will make the market more competitive and improve social welfare. However, intermediary #1 remains as the monopoly for purchaser b.

To see this, observe that the value of goods allocated to purchasers is a diminishing marginal function. Thus, the most efficient way to allocate goods is when these marginals are 0, that is, allocate $\mu _ { a }$ and $\mu _ { b }$ amounts of goods to purchaser a and $b ,$ , respectively. The convex program above defines the equilibrium for this game as:

$$
y _ {s b} ^ {\# 1} = \frac {\mu_ {b}}{2}; y _ {s a} ^ {\# 1} = y _ {s a} ^ {\# 2} = \frac {\mu_ {a}}{I + 2}.
$$

From this, we can calculate the amount of goods allocated to purchaser a to be $\textstyle { \frac { I + 1 } { I + 2 } } \mu _ { a }$ and to purchaser b to be ${ \frac { \mu _ { b } } { 2 } } .$

## 5.2 The Impact of Mergers on Welfare

Next, we demonstrate another counterintuitive effect on welfare caused by merging intermediaries. For this, we consider the same network and the two scenarios shown in Figure 1. In scenario I, three intermediaries A, B, and C compete to deliver goods between purchasers 3 and 4 and providers 1 and 2. In scenario II, A and B merge. Notice that, in scenario I, A and B compete to deliver goods from 1 to 4, but C is the only intermediary between 2 and 3. However, when A and B merge, the merged firm AB becomes the monopoly between 1 and 4, but a competitor for C between 2 and 3.

Figure 5. (Color online) Social Welfare as Function of $I , \mu _ { a } = 1 ; \mu _ { b } = 1 . 1 5$ on Left and $\mu _ { a } = 1 ; \mu _ { b } = 1 . 3$ on Right  
![](/api/attachments/QTU59NBD/fulltext/images/f02f479c6ca4cc695f3f53fd528fb6c789736e3624ccede0b992ac5aed3366ec.jpg)

![](/api/attachments/QTU59NBD/fulltext/images/610ed7efc8ac5c3d88ee13039017d750208e01032acf17c392bba340b0cc001a.jpg)

Depending on how purchaser 3 values the goods from provider 2 relative to the valuations for the other purchaser-provider pairs, the merging of A and B may or may not improve social welfare. Interestingly, for a wide range of parameter values, merging A and B improves consumer welfare. A more specific analysis is given in the following result.

Corollary 4. Consider the network in Figure 1 and the set of parameters $\alpha _ { j } = 1 , \mu _ { 2 3 } = V ; \beta _ { 2 3 } = 1 , \mu _ { 1 3 } = \mu _ { 2 4 } = 0 ; \beta _ { 1 3 } =$ $\beta _ { 2 4 } = 0 ; \mu _ { 1 4 } = 1 ; \beta _ { 1 4 } = 1 ; \theta _ { j } = 0 .$

If V > 1, then the revenue of AB after the merger is larger than the combined revenue of A and B before the merger; furthermore, both the social welfare and the consumer surplus in scenario II are also larger than those in scenario I.

$I f 3 / 7 < V < 1$ , then the revenue of AB after the merger is less than the combined revenue of A and B before the merger; furthermore, the social welfare in scenario II is also less than that in scenario I, but not the consumer surplus.

Proof. The proof involves a straightforward calculation that we omit. Also see Figure 6 for a plot of the welfare, consumer surplus, and revenue as V changes for the two scenarios. □

The proof is based on the convex program characterization given in Theorem 1, which gives us an easy way to compute these equilibria. We omit the details of this calculation and provide only the intuition for the results. Notice that, in scenario I, the path 2-3 is intermediated by C in a monopolistic fashion. In scenario II, the 2-3 connection is no longer monopolistically intermediated. This merger also has a cost. In particular, it leads to decreased competition between the intermediaries connecting 1 and 4. For large values of $V ,$ the value from increasing the competition in the 2-3 connection dominates the decreasing competition in the 1-4 connection.

We use this example to show how the implications of our model differ from those in the prior literature. Bimpikis et al. (2019b) model no intermediaries. So, the mergers of two firms can only lead to indirect impacts. Compared with Bimpikis et al. (2019b), our model impacts social welfare and consumer surplus differently. In our model, the providers and purchasers connected to the merged firms are directly impacted because of the merger. These direct impacts occur in addition to the indirect ones. Therefore, unlike theirs, we can study the implications of mergers of intermediaries. In conclusion, this section demonstrates that social welfare implications critically depend on the network structure. Comparing two arbitrary networks is, in general, a difficult task, and mergers can have both positive and negative welfare implications. While we have studied interesting policy questions thus far, we are also interested in studying how close we can get to the social optima. Specifically, we are interested in bounding the efficiency loss. Additionally, we are interested in analyzing how the parameters of our model may affect the efficiency-loss bounds.

## 6. Bounding Inef<sup>fi</sup>ciency

This section builds further on the previous section to show how network structure influences efficiency.

Figure 6. (Color online) Different Welfare Measures as Functions of V.  
![](/api/attachments/QTU59NBD/fulltext/images/0647cae1d1299eab120f3ad0ef5e69c961d458b5aa2e472e94318e11017e0d56.jpg)  
Notes. Dotted lines represent scenario 2. Solid lines represent scenario 1.

Our intent is to act as a guide for market designers or policymakers to evaluate alternative network structures from an efficiency standpoint. We specifically study how the network structures lead to the social welfare obtained in the decentralized context compared with the optimal one (without any such constraint). For this purpose, we use the measure called price of anarchy, which is the ratio between the welfare of a Nash equilibrium and the optimal social welfare without incentive constraints. This measure is studied in Dubey (1986) and has been extensively used in computer science starting with Koutsoupias and Papadimitriou (1999). If this ratio is close to 1, then it means that the system is almost optimal.

## 6.1. Price of Anarchy: Lower Bound

De<sup>fi</sup>nition 3. Let $E \subset J \times K$ be the set of node pairs $j \in J ; k \in K$ . Define OPT E as the optimal social welfare obtainable through the links in $E ,$ that is,

$$
\begin{array}{l} O P T (E) := \max _ {X, Y} \sum_ {j, k} \mu_ {j k} Y _ {j k} - \sum_ {j} \theta_ {j} X _ {j} \\ \qquad \qquad \qquad \qquad - \sum_ {j k \in E} \beta_ {j k} \frac {Y _ {j k} ^ {2}}{2} - \sum_ {j \in J} \alpha_ {j} \frac {X _ {j} ^ {2}}{2} \\ \text {s.t:} X, Y \geq 0, \\ \qquad \qquad \qquad Y _ {j k} = 0, \forall j k \notin E, \\ \qquad \qquad \qquad X _ {j} = \sum_ {k} Y _ {j k}. \end{array}\tag{6}
$$

If the set of connections (or links) in E constrain the trades to occur only between the connected (or linked) agents, OPT E is the maximum level of welfare the system can achieve. In our environment, a trade between $j \in J$ and $k \in K$ is possible only if they are connected to at least a common intermediary. Let $E _ { 1 } \subset$ $J \times K$ be the set of such pairs. Namely,

$$
\begin{array}{c} E _ {1} := \big \{(j, k) \in J \times K | \text { there exists } i \in I \text { where both } \\ j i \text { and } i k \text { are connected} \big \}. \end{array}
$$

Thus, at the equilibrium, the welfare is at most $O P T ( E _ { 1 } )$ . Our first price of anarchy result provides a lower bound on the welfare of the equilibrium compared with $O P T ( E _ { 1 } )$ .

Theorem 2. The social welfare at the Nash equilibrium of the game $\Gamma ( \mathcal { N } , \theta , \mu , \alpha , \beta )$ (defined in Definition 3.1) is at least $2 / 3$ times the optimal social welfare, $O P T ( E _ { 1 } )$

The proof of this theorem is provided in the online appendix. There, we establish the equilibrium to be a series of inequalities. Using those inequalities, we determine the lower bound on the efficiency of the system. This lower bound of $\frac { 2 } { 3 }$ is called the price of anarchy. It measures the extent to which selfish behavior affects efficiency. Note that this result differs from that of the Bertrand competition model among intermediaries in Blume et al. (2009). In their model, all equilibria are efficient, and so the merging of intermediaries would not change the price of anarchy.

## 6.2. Price of Anarchy: Re<sup>fi</sup>ned Lower Bound

Although it is a general result, Theorem 2 does not provide information about the role of the underlying network structure on welfare. For example, in Figure 1, it may be interesting to obtain a more detailed efficiency comparison of the two networks. To obtain more general bounds that reveal the structure of networks, the following notions of network connec tivity are important.

De<sup>fi</sup>nition 4. Given a network G whose nodes are partitioned into three disjoint classes $J , I , K ,$ , we define the edges of G to be those that connect nodes between ${ \dot { J } } , I$ and between $I , K ,$ while $J , K$ are disconnected. We define the ωth layer of G, denoted as $E _ { \omega } ( G ) o r E _ { \omega } f o r s h o r t ,$ , to be the set of node pairs $j k : j \in J ; k \in K$ that are connected by at least ω nodes $i \in I$ (i.e., both ji and ik are edges in G).

For example, for each of the networks in Figure 1, the first layer of $G , \omega = 1$ , contains the pairs 13, 14, 23, 24 . The second layer of the network, $\omega = 2$ , in scenario I (on the left-hand side) is the pair 14, and in scenario II it is the pair 23. Given this definition, our next result refines the price of anarchy for these layers of the network.

Theorem 3. Given a network G over the set of providers, purchasers, and intermediaries, the social welfare at the Nash equilibrium is at least $\begin{array} { r } { ( 1 - \frac { 1 } { 2 \omega + 1 } ) O P T ( E _ { \omega } ) } \end{array}$

The proof of Theorem 3 is given in the online appendix. Relative to Theorem 2, Theorem 3 is informative about the level of efficiency in a more refined way. In particular, Theorem 3 suggests more details on the influence of the underlying network structure on the level of efficiency. To illustrate, continue with the example network in Figure 1. With $\omega = 2 ,$ Theorem 3 implies that the welfare at equilibrium in the network on the left-hand side is at least $4 / 5$ times the total trade surplus of the submarket between 1 and 4, and for the network on the right-hand side, its equilibrium welfare is at least $4 / 5$ times the total trade surplus of the submarket between 2 and 3. This means that merging A and B is beneficial under a Nash model if the submarket between 2 and 3 has high trade value.

This theorem can be insightful for a network designer when analyzing policies having substantial changes in the network structure. The designer should consider policy impacts on different layers of the network. In particular, there is a trade-off in the bound $\begin{array} { r } { ( 1 - \frac { 1 } { 2 \omega + 1 } ) { O P T } ( E _ { \omega } ) \colon { O P T } ( E _ { \omega } ) } \end{array}$ is decreasing, while $( 1 -$ $\scriptstyle { \frac { 1 } { 2 \omega + 1 } } )$ is increasing in ω. Hence, the layer of the network that closest captures the efficiency of the equilibrium is the one that has both high connectivity ω and high trade maximum value ${ \ O } \bar { P T } ( E _ { \omega } )$ . Significant changes in this network layer will likely have a large impact on the efficiency of the market. In the remainder of this section, we further discuss the implications of this result. Here, we will consider the price of anarchy as the proxy for the efficiency of the market and study the impact of the “intermediary capacity” on this measure of efficiency.

## 6.3. Impact of Intermediary Capacity on Price of Anarchy

We start by defining a parameter, which we call the intermediary capacity of the network.

De<sup>fi</sup>nition 5. For a node pair $j \in J ; k \in K$ in the network $G ,$ which is connected by at least one middleman, let $w _ { j k } \ge 1$ be the number of middlemen that connect j and k. Then, $w _ { G } ,$ called the intermediary capacity of $G ,$ is defined as the minimum value among all such $w _ { j k }$

The intermediary capacity of the network, w<sub>G</sub>, is a measure of the competitiveness of the network market. For any provider and purchaser that can potentially trade through the network, they can trade by at least w intermediaries. Further, as a corollary of Theorem 3, we obtain the following result.

Corollary 5. The price of anarchy is at least $\begin{array} { r } { 1 - \frac { 1 } { 2 w _ { G } + 1 } . } \end{array}$

Because $w _ { G } \geq 1$ for any network G, Corollary 5 is a generalization of Theorem 2. Note that the intermediary capacity of the network intuitively captures the degree of competition among the intermediaries. As the intermediary capacity of the network increases—that is, as the economy becomes more competitive—the system approaches full efficiency. Note that, while mergers can lower the intermediary capacity, it is not always the case, as illustrated by the example in Figure 1. So, Corollary 5 does not contradict our earlier result that mergers can have ambiguous implications for welfare.

## 7. Extension for Substitute Goods

Previously, we assumed that the utility of k is additive across $j ,$ that is, $\Sigma _ { j } U _ { j k } ( Y _ { j k } )$ . In this section, we consider the case where the goods are a substitute. We show that a similar characterization of equilibrium based on a convex program applies but is even simpler. Recall that $y _ { j k } ^ { i }$ is the amount of goods that intermediaries i provided by j to k; the total amount of goods that i sells to k is $\begin{array} { r } { Y _ { k } ^ { i } = \sum _ { j } y _ { j k } ^ { i } ; } \end{array}$ the total amount of goods that i buys from $\begin{array} { r } { j \mathrm { i s } x _ { j } ^ { i } = \sum _ { k } y _ { j k } ^ { i } ; } \end{array}$ ; and $\begin{array} { r } { Y _ { k } = \sum _ { j } Y _ { j k } } \end{array}$ is the total amount of goods that a purchaser k obtains. We assume the utility of a purchaser k is $\begin{array} { r } { U _ { k } ( Y _ { k } ) = \mu _ { k } Y _ { k } - \frac { 1 } { 2 } \beta _ { k } Y _ { k } ^ { 2 } } \end{array}$ . Thus, the marginal price at the purchaser k is

$$
\frac {\partial U _ {k} (Y _ {k})}{\partial Y _ {k}} = \mu_ {k} - \beta_ {k} Y _ {k}.
$$

We further assume a unit cost of $c _ { j k } \ge 0$ that the intermediary needs to pay i for delivering goods from j to $k . ^ { 1 2 }$ Then, intermediary $i ^ { \prime } \mathrm { s }$ payoff function is

$$
\begin{array}{c} \Phi (y) = \sum_ {k} (\mu_ {k} - \beta_ {k} Y _ {k}) Y _ {k} ^ {i} - \sum_ {j k} c _ {j k} y _ {j k} ^ {i} \\ - \sum_ {j} (\theta_ {j} + \alpha_ {j} X _ {j}) x _ {j} ^ {i}. \end{array}
$$

Given an index $j ^ { * }$ and $k ^ { * }$ , taking the derivative according $y _ { j ^ { * } k ^ { * } } ^ { i }$ we obtain

$$
\begin{array}{c} \sum_ {k} (\mu_ {k} - \beta_ {k} Y _ {k}) \frac {\partial Y _ {k} ^ {i}}{\partial y _ {j ^ {*} k ^ {*}} ^ {i}} + \sum_ {k} \frac {\partial (\mu_ {k} - \beta_ {k} Y _ {k})}{\partial y _ {j ^ {*} k ^ {*}} ^ {i}} Y _ {k} ^ {i} - c _ {j ^ {*} k ^ {*}} \\ - \sum_ {j} (\theta_ {j} + \alpha_ {j} X _ {j}) \frac {\partial x _ {j} ^ {i}}{\partial y _ {j ^ {*} k ^ {*}} ^ {i}} - \sum_ {j} \frac {\partial (\theta_ {j} + \alpha_ {j} X _ {j})}{\partial y _ {j ^ {*} k ^ {*}} ^ {i}} x _ {j} ^ {i}. \end{array}
$$

Notice that if $k \neq k ^ { * }$ , then $\begin{array} { r } { \frac { \partial Y _ { k } ^ { i } } { \partial y _ { j ^ { * } k ^ { * } } ^ { i } } = 0 . } \end{array}$ , and $\operatorname { i f } j \neq j ^ { * }$ , then $\begin{array} { r } { \frac { \partial x _ { j } ^ { i } } { \partial y _ { j ^ { * } k ^ { * } } ^ { i } } = 0 } \end{array}$ . Thus,

$$
\begin{array}{c} \frac {\partial \Phi (y)}{\partial y _ {j ^ {*} k ^ {*}} ^ {i}} = (\mu_ {k ^ {*}} - \beta_ {k ^ {*}} Y _ {k ^ {*}}) - \beta_ {k ^ {*}} Y _ {k ^ {*}} ^ {i} - c _ {j ^ {*} k ^ {*}} \\ - (\theta_ {j ^ {*}} + \alpha_ {j ^ {*}} X _ {j ^ {*}}) - \alpha_ {j ^ {*}} x _ {j ^ {*}} ^ {i}. \end{array}
$$

Observe that Φ is a concave function, thus, we have the following first-order condition for an equilibrium for all providers $j ^ { * }$ , purchasers $k ^ { * }$ , and intermediaries i who are connected in the network:

$$
\alpha_ {j ^ {*}} X _ {j ^ {*}} + \alpha_ {j ^ {*}} x _ {j ^ {*}} ^ {i} + \beta_ {k ^ {*}} Y _ {k ^ {*}} + \beta_ {k ^ {*}} Y _ {k ^ {*}} ^ {i} \geq \mu_ {k ^ {*}} - \theta_ {j ^ {*}} - c _ {j ^ {*} k ^ {*}},
$$

if strict inequality holds then $y _ { j ^ { * } k ^ { * } } ^ { i } = 0$

Given this equilibrium condition, using a similar argument as in Theorem 1, we obtain the following characterization of equilibria. The proof of this result is provided in the online appendix.

Theorem 4. The equilibrium is unique and is the solution of the following convex program

$$
\min \sum_ {j} \alpha_ {j} (X _ {j}) ^ {2} + \sum_ {j, i} \alpha_ {j} (x _ {j} ^ {i}) ^ {2} + \sum_ {k} \beta_ {k} (Y _ {k}) ^ {2} + \sum_ {i, k} \beta_ {k} (Y _ {k} ^ {i}) ^ {2}\tag{7}
$$

$$
\mathbf {s . t .}: \alpha_ {j} X _ {j} + \alpha_ {j} x _ {j} ^ {i} + \beta_ {k} Y _ {k} + \beta_ {k} Y _ {k} ^ {i} \geq \mu_ {k} - \theta_ {j} - c _ {j k}
$$

j, k, i where i connects j and k.

(<sup>8</sup>)

This theorem suggests that, even when the purchasers consider goods from different providers substitutes, the equilibrium is unique and characterized by a convex program. Hence, the results in the previous section extend to this case as well.

## 8. Conclusions and Future Work

Sharing economies facilitated by multisided platforms are becoming increasingly popular in many contexts (Uber, Airbnb being some of the well-known ones). Therefore, understanding the welfare implications of these platforms is important to guide policy proposals for improving social welfare. For example, as the sharing economy matures, mergers and acquisitions among platforms are likely to occur. Yet, there is little guidance from the prior literature to analyze the welfare implications of such mergers. This is because the majority of the current literature focuses on monopoly pricing problems. Our paper fills this void by developing a tractable model that provides insights into the role of network structure in affecting welfare.

The contributions of our paper are twofold. First, we show that, in the presence of intermediaries and networks, mergers and competition have an ambiguous effect on welfare. These effects are absent in models of prior literature that are without networks/ intermediaries. Second, we introduce a measure of intermediary capacity that gives an upper bound on the loss of efficiency. As the intermediary capacity gets bigger, the loss of efficiency approaches zero. These nontrivial and robust structural results potentially have policy implications on evaluating mergers of intermediaries.

Even though we presented the analysis in a stylized context, the underlying structure is relevant more broadly. For example, the analysis is also relevant to a physical retail chain context. Visualize the retailers as the platform companies. On one side of the network are manufacturers (e.g., Reebok, Under Armour). On the other side of the network are geographic locations where the retailers compete against one another. The edges between the first side and the platform now correspond to whether the retailer carries the products from the manufacturers. The edges between the platform and the second side correspond to whether the retailer has a presence in the geographic location. In such a context, our insights become relevant when studying the impact of retail chain mergers.

Additionally, the insights continue to be valid in some variations of our model. For example, in the adauction context, a provider can correspond to supply aggregator firms such as ValueClick, AdBrite, or Burst Media. So, the network may involve an additional layer, say, a four-partite graph with advertisers connecting to the ad aggregators connecting to the intermediaries. If we assume that the value perceived at those adaggregator nodes does not change because of the mergers of intermediaries, then the current analysis is not affected by extending the graph. This implies that analyzing the three-layer network structure is informative enough for the efficiency of the market.

However, if the valuations at the provider nodes change because of changes to the market structure, then the multipartite graph would be needed, which we leave for future work. In essence, we have considered a parsimonious structure for analysis which is robust to some generalizations.

In conclusion, we have provided a tractable model of competition among intermediaries. Our key results show that the traditional antitrust analysis does not apply to a platform context because of the nature of the underlying network. As mentioned earlier, it would be of interest to study more deeply in the future the welfare implications when characterizing a multipartite graph involving aggregators on the publisherand/or the provider-side or when purchasers can easily substitute among the offerings. Furthermore, for future work, it would also be of interest to model more general utility functions, uncertainty, asymmetric information, and network formation questions. Moreover, we used the Cournot model as the basis for the information structure in our model and this allowed us to not focus on price + quantity contracts. Another possible extension is to study a detailed model involving such contracts.

## Endnotes

<sup>1</sup> Characterizing equilibria with convex programming techniques is not new, for example, in bargaining network games (Nguyen 2015) and in combinatorial auctions (Bikhchandani and Ostroy 2002). However, we are not aware of the same technique being used in this specific context, and such a formulation allows us to conduct com parative analysis easily.

<sup>2</sup> In the applications in Sections 3.2.1 and 3.2.2, each provider corresponds to a group of anonymous agents and C χ corresponds to the aggregate cost function.

<sup>3</sup> Note that the approach can be generalized to concave utilities and convex costs. Our paper, like many in the literature, focuses on quadratic functions because of tractability.

<sup>4</sup> In our applications in Sections 3.2.1 and 3.2.2, each purchaser represents to a group of anonymous agents and U Y corresponds to the aggregate utility function.

<sup>5</sup> In some situations, the advertisers may own the power and the entities may be involved in negotiations. Our model and insights do not cover these cases.

<sup>6</sup> These companies do not have limitless power. In some cases, governments have intervened to limit the surge prices. For ou analysis, as we mentioned earlier, we construct a stylized parsimo nious model for our analysis.

<sup>7</sup> Certain characterizations of search auctions may only be perceived, for example, as involving advertisers and the intermediaries, in which case our formulation may not work.

<sup>8</sup> In this perspective, one can also view our model as a reduced form characterization of a more complex ad network—possibly involving five layers with additional layers representing the aggregators between publishers and intermediaries as well as between advertisers and intermediaries. Note that here we abstract away the costs and the fee that advertisers and publishers need to pay to the aggregator. However, assuming constant marginal cost, one can encode these costs in the constant term of the supply and demand functions f X and g Y .

<sup>9</sup> Note that, in this example, outside the Cournot competition framework, it is possible for the intermediary to offer contracts involving both price and quantity, and the monopolist would obtain al the trade surplus. However, as in our applications, if each provider and purchaser represents a group of anonymous sellers and buyers, the intermediary will not be able to extract all the surplus.

<sup>10</sup> The argument to prove is as follows. Suppose that is not the case and one of those values is not equal at equilibrium. Then, because the constraints are identical for other intermediaries, the different solutions should have been optimal for every other intermediary as well. We also know from Theorem 1 that the equilibrium is unique.

<sup>11</sup> We have

$$
\begin{array}{r l} y _ {s a} ^ {\# 1} = 0; y _ {s b} ^ {\# 1} = \frac {(I + 1) \mu_ {b} - I \mu_ {a}}{I + 2}; y _ {s a} ^ {\# 2} = \frac {2 \mu_ {a} - \mu_ {b}}{I + 2} \\ & \text {if} \mu_ {a} <   \mu_ {b} <   2 \mu_ {a}, \\ y _ {s a} ^ {\# 1} = 0; y _ {s b} ^ {\# 1} = \frac {\mu_ {b}}{2}; y _ {s a} ^ {\# 2} = 0 \quad \text {if} 2 \mu_ {a} <   \mu_ {b}. \end{array}
$$

<sup>12</sup> The analysis extends to the case in which each intermediary i has a different cost $c _ { j k } ^ { i } .$

## References

Abreu D, Manea M (2012) Bargaining and efficiency in networks. J. Econom. Theory 147(1):43–70.

Accenture (2016) Platform economy: Technology-driven business model innovation from the outside in. Accessed August 21, 2020, https://www.accenture.com/fr-fr/\_acnmedia/PDF-2/Accenture -Platform-Economy-Technology-Vision-2016-france.pdf.

Ashlagi I, Edelmanb B, Leec HS (2018) Competing ad auctions. Working paper, Stanford University, Palo Alto, CA.

Balachander S, Kannan K, Schwartz DG (2009) A theoretical and empirical analysis of alternate auction policies for search ad vertisements. Rev. Marketing Sci. 7(1):1–51.

Banerjee S, Freund D, Lykouris T (2017) Pricing and optimization in shared vehicle systems: An approximation framework. Babaioff M, Moulin H, eds. Proc. 2017 ACM Conf. Econom. Comput. (ACM, New York), 517.

Bikhchandani S, Ostroy JM (2002) The package assignment model. J. Econom. Theory 107(2):377–406.

Bimpikis K, Candogan O, Daniela S (2019a) Spatial pricing in ride sharing networks. Oper. Res. 67(3):744–769.

Bimpikis K, Ehsani S, Ilkilic R (2019b) Cournot competition in net worked markets. Management Sci. 65(6):2467–2481.

Blume LE, Easley D, Kleinberg J, Tardos E (2009) Trading networks with price-setting agents. Games Econom. Behav. 67(1):36–50.

Bose S, Cai DW, Low S, Wierman A (2014) The role of a market maker in networked cournot competition. 2014 IEEE 53rd Annual Conf. Decision Control (CDC) (IEEE, Los Angeles), 4479–4484.

Cachon GP, Daniels KM, Lobel R (2017) The role of surge pricing on a service platform with self-scheduling capacity. Manufacturing Service Oper. Management 19(3):368–384.

Caragiannis I, Kaklamanis C, Kanellopoulos P, Kyropoulou M, Lucier B, Paes Leme R, Tardos E (2015) Bounding the inefficiency of outcomes in generalized second price auctions. J. Econom. Theory 156(C):343–388.

Chen Y, He C (2011) Paid placement: Advertising and search on the Internet. Econom. J. (London) 121(556):F309–F328.

Corominas-Bosch M (2004) Bargaining in a network of buyers and sellers. J. Econom. Theory 115(1):36–77.

Daughtery A (2008) Cournot competition. Durlauf S, Blume L, eds. The New Palgrave Dictionary of Economics, 2nd ed. (Palgrave Macmillan, Basingstoke, New York), 1197–1203.

Delrahim M (2019) Keynote address at Silicon Flatirons Annual Technology Policy Conference. Accessed February 10, 2021. https://www.justice.gov/opa/speech/assistant-attorney-genera -makan-delrahim-delivers-keynote-address-silicon-flatirons.

Drummond D (2008) Ending our agreement with Yahoo! Accessed February 5, 2021, http://googleblog.blogspot.com/2008/11 ending-our-agreement-with-yahoo.html.

Dubey P (1986) Inefficiency of nash equilibria. Math. Oper. Res 11(1):1–8.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1):242–259.

Elliott M (2015) Inefficiencies in networked markets. Amer. Econom. J. Microeconom. 7(4):43–82.

Evans DS, Schmalensee R (2013) The antitrust analysis of multi sided platform businesses. NBER Working Paper No. w18783, National Bureau of Economic Research, Cambridge, MA

Fang Z, Huang L, Wierman A (2017) Prices and subsidies in the sharing economy. Proc. 26th Internat. Conf. World Wide Web (International World Wide Web Conferences Steering Com mittee, Geneva, Switzerland), 53–62.

Farrell J, Shapiro C (1990) Horizontal mergers: An equilibrium analysis. Amer. Econom. Rev. 80(1):107–126.

Feldman J, Mirrokni V, Muthukrishnan S, Pai M (2010). Auctions with intermediaries. Proc. ACM Conf. Electronic Commerce. 23–32.

Feng J, Bhargava HK, Pennock DM (2007) Implementing sponsored search in web search engines: Computational evaluation of al ternative mechanisms. INFORMS J. Comput. 19(1):137–148

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Klemperer P (1986) Price competition vs. quantity competition: The role of uncertainty. RAND J. Econom. 17(4):618–638.

Koutsoupias E, Papadimitriou C (1999) Worst-case equilibria. Annual Sympos. Theoret. Aspects Comput. Sci. 99 (Springer, Berlin, Hei delberg), 404–413.

Kranton R, Minehart D (2001) A theory of buyer-seller networks Amer. Econom. Rev. 91(3):485–508.

Lee R (2014) Competing platforms. J. Econom. Management Strategy. 23(3):507–526.

Manea M (2011) Bargaining on stationary networks. Amer. Econom Rev. 101(5).

Manea M (2018) Intermediation and resale in networks. J. Political Econom. 126(3):1250–1301.

Mehta A, Saberi A, Vazirani U, Vazirani V (2007) Adwords and generalized online matching. J. ACM 54(5):22.

Milgrom P (2004) Uniform price auctions. Putting Auction Theory to Work (Cambridge University Press, Cambridge, UK), 295–296.

Nava F (2015) Efficiency in decentralized oligopolistic markets. J. Econom. Theory 157(1):315–348.

Nguyen T (2015) Coalitional bargaining in networks. Oper. Res 63(3):501–511.

Nguyen T (2017) Local bargaining and supply chain instability. Oper Res. 65(6):1535–1545

Parker G, Van-Alstyne M (2005) Two-sided network effects: A the ory of information product design. Management Sci. 51(10): 1494–1504.

Perakis G, Sun W (2014) Efficiency analysis of Cournot competition in service industries with congestion. Management Sci. 60(11):2684–2700.

Polanski A (2007) Bilateral bargaining in networks. J. Econom. Theory 134(1):557–565.

Rosen JB (1965) Existence and uniqueness of equilibrium points fo concave n-person games. Econometrica 33(3):520–534.

Shin W (2015) Keyword search advertising and limited budgets. Marketing Sci. 34(6):882–896.

Vasin A, Kartunova P (2016) Cournot oligopoly theory for simple electricity markets. von Mouche P, Quartieri F, eds. Contributions to Equilibrium Theory for Cournot Oligopolies and Related Games: Essays in Honour of Koji Okuguchi (Springer), 155–178

Weyl EG (2010) A price theory of multi-sided platforms. Amer Econom. Rev. 100(4):1642–1672

Wilson CS, US Commissioner (2019) Welfare Standards Underlying Antitrust Enforcement: What You Measure is What You Get. Keynote address, George Mason Law Review 22nd Annua Antitrust Symposium, Arlington, VA.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
