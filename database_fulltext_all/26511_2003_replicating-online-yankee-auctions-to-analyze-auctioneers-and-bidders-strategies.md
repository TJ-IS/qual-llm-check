---
otero_id: 26511
otero_key: "5RP4U5HU"
title: "Replicating Online Yankee Auctions to Analyze Auctioneers' and Bidders' Strategies"
authors: "Ravi Bapna; Paulo Goes; Alok Gupta"
year: "2003"
journal: "Information Systems Research"
doi: "10.1287/isre.14.3.244.16562"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/5RP4U5HU/fulltext/images/ca0f8cada32546e9ade414f27f69bfee76a2f4a3b518d06b3f1ac386836d5966.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Replicating Online Yankee Auctions to Analyze Auctioneers' and Bidders' Strategies

Ravi Bapna, Paulo Goes, Alok Gupta,

To cite this article:

Ravi Bapna, Paulo Goes, Alok Gupta, (2003) Replicating Online Yankee Auctions to Analyze Auctioneers' and Bidders' Strategies. Information Systems Research 14(3):244-268. http://dx.doi.org/10.1287/isre.14.3.244.16562

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2003 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/5RP4U5HU/fulltext/images/fa0761e5caa9341d4b0332301c557233888fef227f597caa87d45ad53d6a385f.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Replicating Online Yankee Auctions to Analyze Auctioneers’ and Bidders’ Strategies

Ravi Bapna • Paulo Goes • Alok Gupta

Department of Operations and Information Management, U-41 IM, School of Business, University of Connecticut, Storrs, Connecticut 06269

Department of Operations and Information Management, U-41 IM, School of Business, University of Connecticut, Storrs, Connecticut 06269

Information and Decision Sciences Department, 3-365 Carlson School of Management, University of Minnesota, 321-19th Avenue South, Minneapolis, Minnesota 55455 ravi.bapna@business.uconn.edu • paulo.goes@business.uconn.edu • agupta@csom.umn.edu

environment to examine the decision space for both bid takers and bid makers in web-based dynamic price setting processes. The applicability of the simulation platform is demonstrated for Yankee auctions in particular. We focus on the optimization of bid takers’ revenue, as well as on examining the welfare implications of a range of consumer-bidding strategies—some observed, some hypothetical. While these progressive open discriminatory multiunit auctions with discrete bid increments are made feasible by Internet technologies, little is known about their structural characteristics, or their allocative efficiency. The multiunit and discrete nature of these mechanisms renders the traditional analytic framework of gametheory intractable (Nautz and Wolfstetter 1997). The simulation is based on theoretical revenue generating properties of these auctions. We use empirical data from real online auctions to instantiate the simulation’s parameters. For example, the bidding strategies of the bidders are specified based on three broad bidding strategies observed in real online auctions. The validity of the simulation model is established and subsequently the simulation model is configured to change the values of key control factors, such as the bid increment. Our analysis indicates that the auctioneers are, most of the time, far away from the optimal choice of bid increment, resulting in substantial losses in a market with already tight margins. The simulation tool provides a test bed for jointly exploring the combinatorial space of design choices made by the auctioneer’s and the bidding strategies adopted by the bidders. For instance, a multinomial logit model reveals that endogenous factors, such as the bid increment and the absolute magnitude of the auction have a statistically significant impact on consumer-bidding strategies. This endogeniety is subsequently modeled into the simulation to investigate whether the effects are significant enough to alter the optimal bid increments or auctioneer revenues. Additionally, we investigate hybrid-bidding strategies, derived as a combination of three broad strategies, such as jump bidding and strategic-at-margin (SAM) bidding. We find that hybrid strategies have the potential of significantly altering bidders’ likelihood of winning, as well as their surplus. (Dynamic Pricing; Online Auctions; Simulation)

## 1. Introduction and Background

Dynamic pricing mechanisms or processes, in which consumers become involved in the price-setting process, are now an integral part of the web economy. A myriad collection of price-setting processes such as auctions (e.g., eBay & uBid), reverse auctions, nameyour-price mechanisms (e.g., Priceline.com), quantity discounters (e.g., Mercata.com), and methods using derivative-based pricing for consumer goods (e.g., Iderive.com) emerged in the new economy. Some continue to flourish (e.g. eBay and uBid) while others have floundered (e.g., Mercata and Iderive). Despite the technological innovativeness of these market mechanisms and their expanded reach, little attention has been paid to the their economic efficiency, namely bid taker’s revenues and bidder’s surplus. We present a simulation approach that provides a relatively risk-free and cost-effective environment to examine the decision space of both bid takers and bid makers in web-based dynamic price-setting processes. We focus our attention on a specific dynamic pricing mechanism, namely, the online Yankee auction. However, the approach we develop is potentially useful in examining the microstructures of other e-market mechanisms as well.

Online auctions represent a model for the way the Internet is shaping the new economy. In the absence of spatial, temporal, and geographic constraints, these mechanisms provide many benefits to both buyers and sellers. However, significant research is still needed in designing new and better mechanisms, as well as examining the efficacy of existing ones in the contexts of the markets they serve. This study, and the tool developed in it, uses the observed insights obtained from tracking real-world online auctions to instantiate the parameters needed to simulate the real-world process. In a risk-free and cost-effective manner, it leverages the computational power of today’s desktops to provide direction to the online auctioneers.

Online auctions are a testimony to the increasing participation of consumers in the price-setting process. While auctions, negotiations, and posted-price mechanisms have all been around for a while (see

Lu and McAfee 1996 for a close look at the circumstances under which auctions are superior to bargaining and vice-versa), there is anecdotal evidence that suggests that auctions are increasingly getting a larger share of the mechanism-pie in consumer markets.<sup>1</sup> For example, eBay is now the largest auto dealer in the country, a product typically associated with negotiations.<sup>2</sup> In consumer-oriented markets, online auctions offer a dynamic-pricing alternative to the age-old posted pricing mechanism. Consumers can now experience the thrill of “winning” a product, potentially at a bargain, as opposed to the typically more tedious notion of “buying” it. The growing dynamic-pricing phenomenon on the web has led to researchers asking whether fixed prices are a thing of the past (Kauffman and Riggins 1998). For sellers, these mechanisms bring access to newer markets and help clear aging or perishable inventory.

Traditional auction design and bidding strategies have been extensively studied in the economics literature (Klemperer 1999, McAfee and McMillan 1987, Milgrom 1989, Milgrom and Weber 1982). However, the significant changes brought about by the Internet on this area are only now beginning to be studied. Researchers such as Van Heck and Vervset (1998) have called for examining the pervasive impact of advanced electronic communications on the wellestablished theory of auctions. Lucking-Reiley (2000) and Herschlag and Zwick (2000) provide an extended coverage of what is being auctioned online and where. In this paper, we concentrate on using theoretically motivated simulations, which use real-world empirical data, to study the drivers in one of the auction mechanisms prevalent in the online setting: the Yankee auction.

## 1.1. The Yankee Online Auction Mechanism

The Yankee auction is a special case of the multiunit English auction. Here, multiple units of the same product are sold to multiple bidders. The auction is progressive in nature; however, each new bid does not have to be strictly greater than the previous bid because there are multiple units available. The set of winning bids consists of the top N bids, where N is the number of units up for auction. A new bid either has to be equal to the minimum bid that is among the winning bids (if the set of winning bids has a cardinality of less than N ) or it has to be at least equal to the minimum winning bid plus a prespecified minimum bid increment. Bidders desiring more than one unit of an item are restricted to present nonunit demand in the form of lumpy bids (Tenorio 1999). In such a specification, several units are demanded at the same price. Bidders are not permitted to specify a demand schedule, detailing how many units they are willing to buy at a certain price. Thus, a hypothetical bidder desiring five units in a Yankee auction, which started at \$40 and had a \$20 bid increment, is not permitted to bid, say \$100 for three and \$80 for two items at the same instant!<sup>3</sup> Such a bidding scheme is infeasible according to the Yankee auction rules. Assuming that the “\$100-3, \$80-2” demand schedule reflected the bidder’s maximum willingness to pay, she could initially bid \$80 for five units, and if outbid could potentially bid \$100 for three units. Thus, the progressive nature of the Yankee auction allows an implicit partial demand schedule revelation, and reduces to an extent the lumpiness that would be evident if the auction was a sealed-bid one. To the best of our knowledge, this particular mechanism design choice of lumpy-bidding under a progressive discriminatory multiunit auction has not been studied in the literature.

Yankee auctions deploy a price-quantity-time precedence. Thereby, multiple-unit bids have a precedence over single-unit bids. The time priority in Yankee auctions is based on either a bidder’s first bid or a bidder’s current bid time depending on the auction site.<sup>4</sup> The former encourages entry into the early stages of the auction. The auction terminates on or after<sup>5</sup> a preannounced closing time and each of the winning bidders pays the amount they last bid to win the auction. Note that in multiunit settings this often leads to discriminatory pricing with consumers paying different amounts for the same item. The soft closing time provides a disincentive to last-minute bidding and is designed to attract participation in early stages of the auction. Such auctions are used on a variety of auction sites on the Web, such as Onsale.com and uBid.com. Before we present the approach and goals of this paper in detail, we present the classical and current set of research relevant to Yankee auctions.

## 1.2. General and Online Auction Research

While a complete literature review on auction theory is beyond the scope of this paper, we present some key and relevant findings. The classical approach to analyze auctions, perhaps unconsciously constrained by the physical limitations of traditional auctions, has been to use game-theoretic models (see, for example, McAfee and McMillan 1987, Milgrom and Weber 1982, and Milgrom 1989 for detailed literature review and analysis). These game-theoretic models are typically used for analyzing auctions of a single item, and are developed assuming an exogenously given number of bidders. The latter assumption implies a lack of substitutable mechanism choices that could attract bidders, a particularly shaky assumption in the “one click away” online environment. The presence of asymmetric information amongst the agents makes the Bayesian-Nash equilibrium the appropriate solution concept. However, the results for singleitem auctions do not apply to multiunit auctions (Rothkopf and Harstad 1994a). Further, the gametheoretic approach is notoriously difficult and, often, analytically intractable with a large number of bidders bidding for multiple units. The number of cases that need to be examined grows exponentially both with the number of items and the number of bidders.

Additionally, the traditional assumption has been to model bidders homogenously as being symmetric, risk neutral, and adopting Bayesian-Nash equilibrium strategies. This set of assumptions readily breaks down in the vast majority of multiunit online auctions, where it is well known that the computation of equilibrium-bidding strategies is intractable (Nautz and Wolfstetter 1997). Another significant barrier is that much of the empirical game theory literature (Paarsch 1992, Laffont et al. 1995) is constructed assuming continuous auction mechanisms that do not have discrete bid increments.

Perhaps because of the inability of applying game-theoretic approaches to such auctions, several researchers such as Lee and Mehta (1999), Vakrat and Seidmann (1999a), and Pavlou and Ba (2000) have taken an empirical approach in analyzing the effectiveness of online auctions. Vakrat and Seidmann (1999b) developed a stochastic model of the bidderarrival process to make lot-size decisions. Using purely empirical data, however, creates the limitation of not being able to test the data against a benchmark of what “should have happened,” i.e., no normative insights are created into the auction process itself.

In this paper, we describe an approach to analyze and optimize the auctioneer’s revenue by manipulating controllable factors. We present a simulation tool that is motivated by the theoretical results of Bapna et al. 2000, who develop an incomplete information model to analyze online bidding activity in Yankee auctions. The simulation uses the theoretical insights generated from the model by Bapna et al. and uses the data collected by monitoring real-world online auctions to demonstrate the validity of the tool. The simulation tool was developed to satisfy the following criteria:

• Given the data from an observed online auction, the simulation should replicate the auction with the winning-bid structure being statistically equivalent to that of the observed auction. Note that the winning-bid structure (and hence revenue) is affected by environmental parameters such as bidding strategies. Hence, if the parameters inferred from observed auctions are not specified with appropriate granularity, the winning-bid structures cannot be replicated.

• The parameters of the auctions can be individually changed to isolate and test the effects of changing the environment of a given auction.

The rest of this paper is organized as follows. In §2, we briefly review the theoretical results of Bapna et al. 2000 and explain the motivation behind this paper. In §3, we describe the data collection and discuss the various consumer-bidding strategies observed in such online auctions. In §4, we describe the characteristics of the multiagent-based simulation model. In §5, we present the results of the simulation study that show that our simulation model successfully replicates the online auction environment and that the simulation model can be used to improve the revenue of an auctioneer. In §6, we demonstrate the extended capabilities of the simulation platform, modeling endogenous impact on consumer-bidding strategy as well as exploring hypothetical hybridbidding strategies. Finally, we conclude in §7 by presenting directions for future work.

## 2. Theoretical Basis

Bapna et al. (2000, 2003) developed a stylized model of equilibrium-bid characteristics with a minimal set of assumptions. They assume that bidders follow the pedestrian bidding strategy, i.e., they always bid the lowest required bid. Rothkopf and Harstad (1994b) present a model in which this strategy is optimal for (single-item) English auctions with relatively small bid increments. Easley and Tenorio (1999) extend this result to Yankee auctions, conditioning it on the absence of any cost of preparing and submitting a bid. They claim that this might be the case in physical auctions, where after the sunk cost of physically reaching a place, the cost of making incremental bids is negligible.

The characterization of Bapna et al. (2000, 2003) is based on incomplete information and with no assumptions regarding the distribution of the bidder valuations. While this characterization did not produce a closed-form expression for the auctioneer’s revenue, it provided an upper and lower bound on the revenue based on the marginal bidder’s valuation. A marginal bidder is characterized as the losing bidder with the largest bid. The interesting aspect of this characterization is that while the marginal bidder’s valuation is not known (without making distributional assumptions), the marginal bid can be observed in practice. Further, the difference between upper and lower bound is purely based on the number of items on bid and the minimum bid increment. Let - denote the fraction of a bid increment k measuring the distance between the marginal consumer’s valuation V and the nearest lower feasible bid. N represents the total number of items for sale.

Proposition 1 below provides an expression for the lower and upper bound on revenue of an auctioneer in terms of the marginal bidder’s value V .

Proposition 1 (Bapna et al. 2003). Let V be the marginal consumer’s valuation, and - be a segment of the bid increment k that measures the distance between the marginal consumer’s valuation V and the nearest lower feasible bid. Then, the lower bound and the upper bound on the revenue of a seller selling multiple units under Yankee auctions are respectively N V <sub>−</sub> - and N V <sub>−</sub> - <sub>+</sub> k.

An interesting corollary of this proposition is that the range of revenue (upper bound–lower bound) is N <sub>∗</sub> k, which does not depend on V or -. A legitimate question to ask is: Given a prespecified Yankee auction with a given N , can the manipulation of the bid increment k yield a higher revenue for an auctioneer?

The following example illustrates, for the same valuations, how the temporal ordering of two separate bidding sequences can result in either the lower or the upper bound on the revenue. We also illustrate how these bounds are affected if the bid increments are changed.

Numerical Example 1. Consider the following hypothetical scenario. Let N <sub>=</sub> 3 and k <sub>=</sub> 5. Let there be four bidders, say A, B, C, D, with valuations of 56, 61, 62, 62, respectively. Let A be the marginal customer and let the opening bid be \$1.

• The lower bound occurs if we observe the following sequence of progressive bids: D(46)—C(46)— B(46) — A(51)—B(51)—C(51)—D(56)—C(56)—B(56) — STOP because A will have to, and will not, bid 61 to get in now. Revenue  \$168. The upper bound occurs if we observe the following sequence of progressive bids: B(51)—C(51)—D(51)—A(56)—D(56)—C(56)— B(61)—C(61)—D(61)—STOP because A will have to, and will not, as per observation 1, bid 61 to get in now. Revenue \$183.

• Now consider the case where we change the bid increment to three. Note that if both sequences above reach the level \$51 (by starting the bidding from a different point), then both lower and upper bound will move downwards to \$162 (\$54 paid by each winner) and \$177 (\$57 paid by each winner), respectively.

Anecdotal evidence suggests that auctioneers realize the importance of k, because we routinely observed online auctions of similar items with different k values at different times. In this paper, we investigate whether the seemingly randomly chosen values of k in the particular auctions were optimal or close to optimal. One approach to study this would be to auction the same or similar items with different k. However, this is a costly endeavor, and in the era of rapid obsolescence of computer products, it will still not answer the question whether the auctioneers used appropriate bid increments. We use the word appropriate, instead of optimal, because k affects the number of rounds of bidding required to reach the same levels of revenue and an auctioneer may choose a different level of k for a faster or slower convergence to the desired point. For example, a bid increment of 5 will take twice as many rounds of bidding as compared to a bid increment of 10 starting from the same opening bid. However, the implemented level of k should be such that it should not significantly affect the revenue because the margins in items sold through these auctions are quite small.

Alternatively, we investigate the optimality of k with the aid of a simulation model capable of replicating a given observed auction, once it has been provided the observed bidding activity. The simulation model then allows us to examine the impact of changing the values of k. This involves three steps: (1) observe a significant number of online auctions and collect a complete set of bidding data for each auction, (2) analyze the data to recognize consumerbidding strategies, and (3) develop the simulation model that uses the bid data and replicates consumer behavior in real auctions, such that the resulting revenue is statistically equivalent to the observed auction’s revenue.

It should be noted that manipulating the value of an endogenous parameter, such as the bid increment, might have implications on the bidding strategies adopted by the bidders also. From an experimental design perspective, we begin our exploration of determining the optimality of k by first controlling for this endogeniety, assuming that the bidding strategies are not impacted by the changing k. This represents a design choice we have made initially to isolate the combinatorial dynamics of the temporal sequencing of the bids. In §§5 and $^ { 6 , }$ we relax this restriction and question whether such endogeniety exists, and if so, is its effect significant.

In the next section, we describe the data-collection process and the simulation model.

## 3. Data Collection and Consumer Strategies

## 3.1. Data Collection

Data collection was carried out by an automatic agent that tracked a popular Yankee auction site (Onsale.com). The agent was programmed to download, at frequent intervals of 5–15 minutes, the html document containing a particular auction’s product description, minimum required bid, lot size, and current high bidders. Subsequently, the series of html files were parsed to condense all the information pertinent to a single auction, including all the submitted bids, as well as the time of each bid, into a single data file. Frequent sampling ensures that the agent is able to capture the time of every bid made by the bidder. This is more laborious than going to eBay at the end of the auction and downloading the final bid information, but is critical to explore the temporal dynamics of Yankee auctions.

We further screened the collected data to make sure that there was no data loss even during the transient periods of the auctions so that we have the complete bidding activity. Specifically, we were interested in the highest bid posted by each bidder, even if she did not “win” the auction. This information is necessary to replicate an auction via a discrete event simulation. These auctions were carefully selected with respect to the important parameters of lot size and bid increment so as to ensure a statistically sound sample.

While we collected equilibrium (final bids) data for over 150 auctions, after careful analysis we found that in a substantial number of cases we may have missed some bidding activity in the transient stages of the auction. This was caused by either a failure of the software agent to connect to the site at a given time, or a faster than expected bidding activity. We ended up with 85 auctions for which we are reasonably certain that we have complete bidding activity. While, at first, it may seem that bid information from individuals who did not win the auction is not important, we posit that even a single bidder can alter the revenue generating path, resulting in a different equilibrium than without a bid from that bidder. In the next section, we provide results from our simulations that validate the capability of the simulator in replicating real-world auctions and provide insights into the choice of optimal bid increment for a given auction.

We were also able to identify, in the data we collected, broad consumer-bidding strategies that we describe next.

## 3.2. Observed Consumer-Bidding Strategies

As identified by Bapna et al. (2000), the bidders in online Yankee auctions can be categorized in the following three broad categories according to their bidding strategies:

(1) Evaluators. Early one-time high bidders who have a clear idea of their valuation and execute a single bid, often during the early phases of the auctions. This bid is significantly greater than the minimum required bid at that time. In essence, the strategy here is to achieve the highest time priority (that is part of most Yankee auctions) for their personal maximum bid level. These consumers are willing to pay a potential premium for the higher priority at their bid level. From another perspective, they may be reasonably certain that the marginal bid will be close to their bid level and, thus, they want to be the first to enter at that level. Surely, such bidders would be rare in traditional auction settings, where the cost of physically getting to an auction site to make just a single bid would be a significant deterrent. They may be willing to pay a premium because they are unwilling to return to bid later or to trust a bidding agent.

(2) Participators. Consumers who derive some utility form the process of participating in the auction itself. They typically make a low initial bid equal to the minimum required bid and progressively monitor the progress of the auction and make ascending bids. These bidders follow the pedestrian approach described in §2.

(3) Opportunists. Consumers who by nature are looking out for bargains and who buy when they see one. They typically place minimum required bids just before the auction closes. Note that the maximum price penalty a bidder of this type pays is equal to the bid increment k of a particular auction (Bapna et al. 2001).

Roth and Ockenfels (2000) focus on the last-minute bidding behavior or “sniping,” and report that bidders strategically choose to bid at last minute to avoid price wars. They focus on single-unit auctions that have a hard closing time (eBay) versus similar auctions that have a going, going, gone period (Amazon). Sniping is found to be more prevalent on eBay, with its hard closing time. While they are related, it is important to differentiate “snipers” from the “opportunists” (Bapna et al. 2000, 2001) in Yankee auctions. Opportunists have been categorized in the multiunit auctions with a going, going, gone period. Such auctions have a larger strategic space in the form of multiple potential winning slots, and hence the notion of “last-minute” bidding is extended to “late bidding” (in the last 10th percentile of the duration).

In our data, we identified the number of each type of bidder for each auction. We then used this information in the simulation model as a set of parameters, with each bidding strategy being represented by a bidding agent that was coded to exhibit corresponding behavioral characteristics. The next section details the simulation model.

## 4. Simulation Model

The objective of developing the simulation model is to test the effect of changing controllable factors such as the bid increment and to examine whether the revenue generated through an auction can be improved. The results of the simulation can only be trusted if it replicates an online auction’s result with its original parameters. It also can be seen as a tool to verify whether the measurable parameters (including bidding strategies) have been measured in enough detail. For example, while we have identified three broad bidding strategies, the bidders certainly use many variations of these strategies such as jump bidding. The question, therefore, is whether the strategy space created by the identified strategies is enough to replicate a given auction. We designed the simulation such that it can be easily configured to run under any given set of inputs. We next describe the simulation model with some of its computational properties.

The first task we needed to accomplish was the creation of bidding agents that would behave as the three types of bidders identified in §3.2.

## 4.1. Creation of Bidding Agents to Represent Consumer-Bidding Strategies

To replicate an auction, we have to replicate the three broad strategies used by the bidders in the original auction. We achieve this by creating three classes of bidding agents, each embodying the behavioral characteristics of the bidding strategy they represent. These bidding agents fall within the conventional definition of software agents, which according to Nwana et al. (1998) are, “software entities that have been given sufficient autonomy and intelligence to enable them to carry out specified tasks with little or no human supervision.” To execute tasks on behalf of a business process, computer application, or an individual, agents are designed to be goal driven, which in our settings translates to maximizing their net worth by winning the object at lowest possible price. We next define the specific attributes that we associate with each of the three classes of bidding agents:

(a) Evaluatory Agents. These agents place just one bid that is equal to the highest feasible bid level below their valuation. Such agents do not participate in the auction on an ongoing basis and if there are enough bids above their bid, they are removed from the winners’ list.

(b) Participatory Agents. These agents arrive at an auction throughout the duration of an auction. The key characteristics of these agents is that they never place a bid higher than the minimum required bid to enter the winners’ list of an auction. In addition, they continue to participate in the auction until the minimum required bid exceeds their valuations.

(c) Opportunistic Agents. These agents enter into the bidding process only towards the end of the auction. We operationalize this feature in the simulation, by letting these agents bid only when the value of the lowest winning bid has reached 90% of the marginal bid level. Auctions terminate based on a going, going, gone rule.

Note that multiple-unit “lumpy” bids are split into a corresponding number of similar type bids giving the simulation process a finer granularity of bidding behavior information. This approximation is reasonable because the Yankee mechanism allows for partial fulfillment of a multiple-unit bid. If the number of units wanted were a hard constraint, then the splitting would not be able to capture the process dynamics. The results presented in §5 indicate that the splitting approximation works well.

The next section provides simulation details.

## 4.2. Simulation Yankee Auctions

The entire simulation process is illustrated in the flowcharts of Figure 1. Broadly, these steps can be summarized as follows:

(1) The observed final bid placed by each individual during a given auction is read from a file. The bids for each type of bidders are placed in separate files, so the input is read from three different files. The information is stored in a two-dimensional array containing bid value and the type of a bidder.

(2) The values of the original bid increment (k), simulated bid increment (k), starting bid level (r), and the number of units for sale (N ) are also provided as an input to the simulator.

(3) Based on the final bid of each bidder, a valuation is generated for that bidder, by adding a random number drawn from U0	 k. In online Yankee auctions, a bidder is not allowed to bid between two successive feasible bid levels. For example, suppose the starting bid for an auction was \$3 and the minimum bid increment was \$5. Then, the bidders are only allowed to bid at levels of \$3, \$8, \$13, \$18 . If a bidder bids \$11, the bid is automatically rounded to \$8. Therefore, a person who bid \$103 may actually have a true valuation of \$108 (at \$108, the person may or may not bid because she is indifferent) given that the minimum bid increment is \$5. Therefore, if the jth bidder’s highest bid was $B _ { j } ,$ then his true valuation is at least within the interval $\left[ { B } _ { j } , \left( { B } _ { j } + { k } \right) \right]$ . Note that this is a conservative approach to the estimation of the valuations. The simulation chooses bidders in a random order. Thus, for instance, participatory agents do not always bid at every single increment they can. It is highly likely that a bidder may bid a certain amount, be idle for several rounds, and when chosen to bid again will check to see if the minimum required bid is not greater than her valuation. If $\mathbf { S O } ,$ then she will bid the minimum required bid.

(4) The valuations array is then scrambled to remove the input bias because data is read from files that store bids in sorted order and the data for each type of bidder is bunched together in the valuations array. We use an innovative linear algorithm to perform this scrambling; the details of this procedure are presented in the next section. The original scrambled array forms the starting point for all the replications for a given auction.

(5) A copy of the scrambled value array is generated for each auction replication. Then, the auction process starts by choosing an eligible bidder from the valuation array. An eligible bidder is a bidder having a valuation higher than the current bid level; in addition, an eligible bidder cannot be among the winners’ list at that moment. We use a variation of our scrambling algorithm to ensure that at each bidding level we only have to draw exactly N random numbers (same as the number of items for sale) to find N eligible bidders at that level. The details of this approach are provided in §4.2.2 and, as shown there, it reduces the computational burden of the simulator significantly. In practice, a simulation run that would otherwise take 25–30 minutes on a Pentium 750 machine, takes less than a minute with our approach.

(6) While the evaluator and participator agents can arrive at any time during the auction, the opportunists can only arrive towards the end of an auction. Because there is no one-to-one correspondence between simulated time and actual time, we used a surrogate measure to detect the last few rounds of an auction. We allowed opportunistic agents to participate only after the 90% of the marginal bid level (lowest level to win the auction) has been reached in the simulated environment.

Figure 1 The Simulation Process  
![](/api/attachments/5RP4U5HU/fulltext/images/b18d568c7ef6f940b624730f90deea0421db8adf93dd3a288fd983bd78ae3172.jpg)

(7) Bidders are ranked using the bid amount and, by time within the bid amount. The winning list is maintained using an insertion sort algorithm.

(8) The simulation stops when there are no more eligible bidders in the valuation list. Note that by doing so we are modeling the automatic extension of the auction duration as implemented by many of the auction sites using Yankee auctions.

(9) When simulating an environment, it is recommended that independent replications of the simulations be done to provide statistically robust results (see, for example, Banks and Carson 1984). We can specify the number of replications in our simulation model, each starting with an independent random number stream. However, as mentioned earlier, we start with the same scrambled value array as created in the first replication. In addition, the other simulation parameters, i.e., the lot size, bid increments, and the starting bid values are kept the same. In other words, during different replications only the order in which bids from different bidders arrive is different.

The simulation model was developed using Visual Basic 6.0<sup>™</sup>. All the parameters of interest such as the starting bid, the lot size, and the original and simulated bid increments are the input to the simulation model. We created original and simulated bid increment as two separate inputs so that we can run the simulations with alternative values of bid increments. As noted above, original value of k is needed because the bidder valuations generated for an auction still need to be based on original data as described earlier in this section.

In the next two sections, we describe some of the details of the simulation model including some innovative techniques that we have developed and applied in the simulation program. In §4.2.1, we provide the details of an efficient linear OI procedure to scramble the valuations array to reduce input bias, where I is the size of the valuations array. In §4.2.2, we describe the process of selecting an eligible bidder by using an advanced version of the scrambling approach developed in §4.2.1. We will show both in terms of theoretical properties and through an analytical comparison with a purely random approach, that our approach increases the efficiency of the simulator by requiring it to draw a minimal number of random numbers during a given replication.

4.2.1. Randomizing the Sequence of the Bidders Valuations. Our objective is to create a mix of bidding agents representing the real-world consumers’ strategies and valuations. It is important from the perspective of the simulation that these bidders arrive in a random fashion and the likelihood of any type of bidder with any valuation at a given point in the simulation is truly random. As mentioned earlier, because the simulation program reads the bids from three distinct files in a sequential order and stores it in an array, the valuations of each type of bidder agents are bunched together in the array. Further, within each category of bidder agents the bids are in sorted order. This can be a potential source of bias in the simulation. For example, if all evaluators have relatively high index values (as compared to participators and opportunists) in the array, then, for an evaluator to be picked as a next eligible bidder a high random number has to be generated.

We developed a linear OI algorithm, referred to as Scramble, which randomizes the valuations array and, hence, reduces the potential source of bias.

Proposition 2. Procedure Scramble randomizes an array of size I in OI  time.

Proof. We present the pseudocode for the procedure that randomizes the array in linear time.

## Procedure Scramble

Begin

For l ranging from 1 to I

j <sub>=</sub> generate\_random\_number 1	 I <sub>−</sub> l

if not last element {

store the jth value-type pair as temporary value

copy the last available I <sub>−</sub> l <sub>+</sub> 1th slot’s value-type pair to the jth slot

replace the last available slot’s values with the temp values

loop l

End

In the next section, we describe an efficient mechanism created based on the procedure above to reduce the number of random numbers that need to be drawn during a simulation run.

4.2.2. Enhancing the Simulation Efficiency by Minimizing Random Number Generation. During a simulation run, the next eligible bidder is chosen by randomly drawing an integer between 1 and I, where I is the total number of eligible bidders. Let the integer drawn be j. The jth eligible bidder then places a bid according to the strategy they follow. Note that bidders who are already in the winners’ list or have a valuation less than the current bid level are not eligible bidders. In terms of implementation, if the array of individual valuations is used directly, then we may need to draw a random number several times before we find an eligible bidder because many in the array will be ineligible to bid. This creates inefficiency in the simulation process because of the need of drawing several random numbers to find a single eligible bidder. The problem accentuates towards the later parts of an auction where the majority of the bidders may have become ineligible. Random number generation is a costly operation and such wastage can result in unnecessarily long simulation runs.

Figure 2 Computational Efficiencies Through Iterative Minimization of the Consideration Set  
![](/api/attachments/5RP4U5HU/fulltext/images/d08ad56784ed9ebf6d1692fc22012016f965575e0de1f1d636b63e755e0c1751.jpg)

To maximize the computational efficiency of the simulation, we created an algorithm that is designed to utilize the minimum possible number of random numbers before convergence to equilibrium. Specifically, we need to draw exactly N numbers at each bid level and no more. Let the set I represent the set of all the bidders and let the set $C \subseteq I$ be the candidate set of bidders, those whose valuations exceed the minimum required bid, at any instance of the auction. We describe the process of finding the minimum eligible set and arranging their valuations in the array so that there is no need to draw multiple random numbers to find the next eligible bidder below. We describe the process from the perspective of an ongoing auction where the initial conditions (finding the first N eligible bidders) are already met because that part is algorithmically trivial.

Figure 2 represents our approach pictorially. Essentially, we divide our valuations array in three parts:

(1) The set of eligible bidders. The cardinality of this set after the initial N customers are in the winners’ list is $| C | \leq ( | I | - N )$ , where I is the cardinality of the whole set or the total number of bidders. In the array this set is arranged and maintained as the first C elements. The auction stops when C is equal to 0.

(2) The set of current winners. The cardinality of this set is always $N ,$ as long as $| I | > N .$ In the array this part is arranged as the elements ( C 1) to element $( | C | + N )$ . This part is arranged in such a way that an element can be inserted at any position from (<sub></sub>C<sub></sub> <sub>+</sub> 1) to (<sub></sub>C<sub></sub> <sub>+</sub> N ), but the element being pushed out is always the element ( C N ).

(3) The set of bidders whose valuations are less than the required current minimum bid. These customers cannot participate in the auction anymore. The cardinality of this set, $L \leq ( | I | - N )$ , increases as the auction progresses. In the array, these bidders are positioned in as elements $( | C | + N + 1 )$ to <sub></sub>I <sub></sub>.

Given this division, at any point in time the cardinality of the eligible set is given by the following expression:

$$
| C | = | I | - N - L.\tag{1}
$$

To choose a new bidder, we draw a random number between 1 and <sub></sub>C<sub></sub>. Let the chosen number be j. The jth eligible bidder is then simply chosen and places a bid based on their strategy. The bid is placed in the appropriate place in the winner stack. This pushes out the bidder who was in the $( | C | + N )$ th position. If the valuation of this bidder is greater than the current required bid, the bidder being pushed out is put in the jth position in the eligible bidder set, otherwise <sub></sub>C<sub></sub> is reduced by one by moving the elements in $( j + 1 ) \mathrm { t h }$ to <sub></sub>C<sub></sub>th position to jth to $( | C | - 1 )$ th position. Whenever the minimum bid requirement increases by k, we scan the eligible bid set and remove any bidders who may no longer be able to bid at the new level. Therefore, the eligible bidder set keeps on shrinking as the auction progresses and the auction stops when the eligible bidder set becomes a null set. By keeping the index of the eligible bidder set we only have to draw a single random number for finding an eligible bidder. If there are N items for sale then we need to draw, at the most, N random numbers at each bidding level.

To provide insight into the efficiency gained in this process versus a purely random approach of finding an eligible bidder, let us provide an analytical comparison of our approach to the purely random approach. First, we introduce some notation. Given that the set I represents the set of all the bidders and the set $C \subseteq I$ is the candidate set of bidders, define s as the likelihood of finding a bidder in the candidate set from amongst all the bidders. Observe that s <sub>=</sub> Prob(finding $i \in \mathsf { \bar { C } } ) = | C | / | I |$ . Recall that N represents the lot size. Let the bid increment $k = \alpha N ,$ , where $\alpha > 0 .$

Proposition 3. If the marginal bidder’s valuation V is from a uniform distribution such that $V \approx U [ 0 , x N ] .$ where $x \ge 1$ , then the expected total number of random variables drawn with purely random draws from a set of I bidders is

$$
\sum_ {i = 0} ^ {((x - 1) / \alpha) - 1} \frac {x N}{(x - 1) - i \alpha}.
$$

Our approach requires a maximum of $( x - 1 ) N / ( \alpha )$ random numbers to be drawn.

Proof. First, note that given our construction $k =$ N , the number of bidding cycles to convergence $( x N - N ) / ( \alpha N ) = ( x - 1 ) / \alpha$ , where the numerator accounts for top quintile with N bidders. Because our approach requires drawing a maximum of N random numbers in each bidding cycle, the maximum required number of random draws is $( x - 1 ) N / \alpha$

With purely random draws, the expected number of times we need to draw a bidder i belonging to the consideration set is binomially calculated as

Enumber of times to draw $i \in C )$

$$
= \sum_ {j = 1} ^ {\infty} j (1 - s) ^ {j - 1} s = s \sum_ {j = 1} ^ {\infty} - \frac {d}{d s} (1 - s) ^ {j}.
$$

Upon simplification, we obtain

Enumber of times to draw $i \in C ) = - s \frac { d } { d s } \frac { ( 1 - s ) } { s } = \frac { 1 } { s } .$

Extending to N winners,

$$
\mathrm{E} (\text { number   of   times   to   draw } N i ^ {\prime} s \in C) = \frac {N}{s}.
$$

At the jth bidding cycle, jN bidders will have valuations less than the minimum required bid. In addition, there will be N bidders who are already in the winners’ list and thus no longer belong to C. Thus, we can re-express the probability of finding a bidder belonging to the candidate set

$$
s = \frac {x N - j \alpha N - N}{x N} = \frac {x - j \alpha - 1}{x}.
$$

This implies that

$$
{\frac {1}{s}} = {\frac {x}{(x - 1) - j \alpha}}.
$$

Hence, summing over all the bidding rounds ranging from 0 through $( x - 1 ) / \alpha ,$ , we obtain: The expected total number of random variables drawn is

$$
\sum_ {i = 0} ^ {((x - 1) / \alpha) - 1} \frac {x N}{(x - 1) - i \alpha}.
$$

Numerical Example 2. Assume $x = 2 0 , \ \alpha = 0 . 5 ,$ $V _ { \operatorname* { m a x } } = \$ 200,k = 5 ,$ and $N = 1 0$ . Based on Proposition 3, the expected total number of random numbers drawn to reach convergence equals

$$
\begin{array}{c} 2 0 N \sum_ {j = 0} ^ {3 7} \frac {1}{1 9 - 0 . 5 j} = 2 0 N \left(\frac {1}{1 9} + \frac {1}{1 8 . 5} + \dots + \frac {1}{0 . 5}\right) \\ = \mathbf {1 6 9 . 1 2 N}. \end{array}
$$

Because in our approach we eliminate all the ineligible bids from the candidate set at every iteration, we are guaranteed to progress the auction at every iteration, hence, the expected number of random numbers drawn is simply equal to the number of bidding cycles to convergence, i.e., $( x - 1 ) / \alpha = 3 8 N$ . Thus, our approach results in an expected improvement in efficiency of approximately 345%.

## 5. Simulation Results

Our primary objective in building the simulator was to be able to replicate the 85 real-world auctions so that we can test the effect of theoretical, empirical, and heuristic rules on the auction process. This is a challenging task because the complex real-world strategies used by individual bidders in a given auction, which affect the revenue, cannot be coded in a general simulation tool. Even though we use the three broad bidding strategies we identified in §3.2, in reality, many bidders may use hybrid strategies. Hence, if the strategy space defined by our identified strategies is not rich enough we will not be able to replicate the auctions. The problem of establishing mechanism equivalence is further confounded by the fact that the observed data from actual auctions is a single point (a realization of a bidding sequence), which could be any of the multiple equilibrium points implied by Proposition 1. In addition, the revenues generated are discrete because of the discrete nature of bid levels. Therefore, instead of using mean revenue to establish equivalence, we establish equivalence by using either a chisquare goodness-of-fit test for the distribution of winning bids, or by using a binomial test depending upon whether there are more than two levels of bids among the bids. In the next section, we present the simulation results and the results of the equivalence tests.

## 5.1. Test of Bid Distribution Fit

We test the robustness of the simulator by using a goodness-of-fit procedure. Recall that a typical multiunit auction, with bidders employing the strategies described in §3.2, ends with winners at multiple bid levels. Given identical starting parameters, our test procedure examines whether the observed frequencies of the various bid levels in the real-world auctions matches, in a statistical sense, the expected frequencies of the same bid levels that are generated by the multiple replications of the simulation process.

Intuitively, we test whether there is a favorable likelihood that the real-world auction itself can be generated by the distribution of the winning-bid levels created by the simulation. Consider the following distribution of winning bid patterns for an auction we tracked and simulated.

Figure 3 shows an auction that terminated with winning bidders at four different bid levels. We then test the goodness of fit between the expected (simulated) and the observed distributions. Thus, our hypothesis of interest is:

Hypothesis H0. The observed real-world auction and its simulated replications belong to the same underlying distribution with regards to its revenue generating properties.

Against the alternative hypothesis:

Hypothesis Ha. The observed real-world auction and its simulated replications belong to the different underlying distributions with regards to their revenue generating properties.

Statistically, the chi-square test is ideally suited for this purpose. Particularly important to us is the fact that it is nonparametric, does not assume any prior distribution, and applies to nominal data, such as frequencies. Following are some of the reasons that dissuaded us from using a parametric statistical procedure:

(1) We only have a point estimate of the revenue of real auctions with no distributional information. Further, the observed revenue could be from any place in the distribution and there is no reason to believe that it indicates the central tendency of its underlying distribution. Testing an empirical distribution (generated by the simulation) with observed revenue as the indicator of central tendency (mean or median) is inappropriate.

Figure 3 Do the Simulated and Actual Distributions of the Bid Levels Fit?  
![](/api/attachments/5RP4U5HU/fulltext/images/0a5060ca68906abc12f151a7fecea7e7c907b4a4326422204ee0e222d82420ce.jpg)

(2) The empirical distributions did not seem to be bell shaped and were quite flat, making the parametric t-test inappropriate.

Another reason for not using a parametric test is, that given the restriction of bidders being able to only bid in multiples of the bid increment, the revenue of these auctions is a discrete variable. For example, suppose there are five items for sale and each winning bid is \$100 (for total revenue of \$500). If the minimum bid increment is \$10, then the next bid can only be \$110 and the revenue level \$510.

The chi-square test has certain minimum requirements with respect to frequency of every cell ( 5) and in those cases where this requirement is not satisfied there are two recourses. First, if the number of cells (possible bid levels in our case) is exactly two (and frequency <5), then the binomial signs test should be resorted to. Otherwise, if the number of possible outcomes is greater than two (and frequency <5) then either the multinomial signs test is recommended, or cells should be merged to get cell frequencies >5. For sake of completeness, in those cases when we had two bid levels and cell frequencies <5, we adopted the binomial signs test. For all other cases, we used the chi-square test, resorting to merging of cells in the case when there were more than two bid levels and the cell frequencies were <5.

The 85 auctions ranged in observed revenue from \$40 to \$24,790, in the number of items for sale from three to 100, and in the number of bidders from four to 437. The complete sets of results with detailed descriptions of the parameters of the auctions are listed in Tables 1a and 1b. The columns provide the masked auction number, the revenue that was observed in the real auction, the range of the simulated auctions, the test statistic, and the p-value, respectively. Each auction was replicated 31 times using independent random number seeds for the bidding sequence. However, during all these runs, the bidder valuations were kept constant, so the revenue variability is only the result of randomizing the sequence of bid arrivals.

Table 1a Chi-Square Test for Similarity of Bid Distribution

<table><tr><td>Auction Number</td><td>Observed Auction Revenue ($)</td><td>Simulated min ($)</td><td>Simulated max ($)</td><td>Chi Square</td><td>p-Value</td></tr><tr><td>1</td><td>16,190</td><td>16,210</td><td>16,270</td><td>10.21</td><td>0.176</td></tr><tr><td>2</td><td>24,790</td><td>24,670</td><td>24,990</td><td>0.78</td><td>0.376</td></tr><tr><td>3</td><td>10,915</td><td>10,775</td><td>10,975</td><td>9.53</td><td>0.121</td></tr><tr><td>4</td><td>10,770</td><td>10,850</td><td>10,990</td><td>2.21</td><td>0.33</td></tr><tr><td>5</td><td>19,836</td><td>19,436</td><td>19,616</td><td>4.34</td><td>0.114</td></tr><tr><td>6</td><td>16,068</td><td>16,168</td><td>16,628</td><td>0.78</td><td>0.376</td></tr><tr><td>7</td><td>11,633</td><td>11,653</td><td>11,813</td><td>9.53</td><td>0.121</td></tr><tr><td>8</td><td>14,093</td><td>14,033</td><td>14,113</td><td>0.76</td><td>0.69</td></tr><tr><td>9</td><td>11,610</td><td>11,340</td><td>11,600</td><td>4.34</td><td>0.114</td></tr><tr><td>11</td><td>10,694</td><td>10,754</td><td>11,194</td><td>0.81</td><td>0.938</td></tr><tr><td>12</td><td>15,190</td><td>15,050</td><td>15,150</td><td>0.52</td><td>0.771</td></tr><tr><td>13</td><td>16,922</td><td>16,662</td><td>16,762</td><td>0.17</td><td>0.919</td></tr><tr><td>14</td><td>13,660</td><td>13,430</td><td>13,690</td><td>2.86</td><td>0.239</td></tr><tr><td>15</td><td>14,968</td><td>14,908</td><td>14,988</td><td>0.62</td><td>0.989</td></tr><tr><td>16</td><td>18,308</td><td>18,168</td><td>18,408</td><td>5</td><td>0.172</td></tr><tr><td>17</td><td>12,515</td><td>11,055</td><td>11,195</td><td>84</td><td>0.000</td></tr><tr><td>18</td><td>23,473</td><td>23,273</td><td>23,533</td><td>0.67</td><td>0.716</td></tr><tr><td>19</td><td>3,486</td><td>3,426</td><td>3,506</td><td>0.26</td><td>0.879</td></tr><tr><td>20</td><td>11,043</td><td>10,823</td><td>11,043</td><td>2.99</td><td>0.225</td></tr><tr><td>23</td><td>5,233</td><td>5,113</td><td>5,313</td><td>1.89</td><td>0.389</td></tr><tr><td>30</td><td>3,496</td><td>3,496</td><td>3,536</td><td>0.75</td><td>0.687</td></tr><tr><td>35</td><td>13,610</td><td>13,090</td><td>13,290</td><td>43.52</td><td>0.000</td></tr><tr><td>36</td><td>1,833</td><td>1,853</td><td>1,903</td><td>2.17</td><td>0.338</td></tr><tr><td>38</td><td>8,340</td><td>8,290</td><td>8,410</td><td>0.24</td><td>0.887</td></tr><tr><td>40</td><td>3,449</td><td>3,379</td><td>3,439</td><td>0.01</td><td>0.997</td></tr><tr><td>41</td><td>3,779</td><td>3,729</td><td>3,829</td><td>3.11</td><td>0.211</td></tr><tr><td>42</td><td>2,869</td><td>2,819</td><td>2,949</td><td>0.5</td><td>0.78</td></tr><tr><td>43</td><td>2,509</td><td>2,447</td><td>2,519</td><td>0.35</td><td>0.839</td></tr><tr><td>44</td><td>2,007</td><td>1,987</td><td>2,077</td><td>1.12</td><td>0.57</td></tr><tr><td>47</td><td>703</td><td>663</td><td>713</td><td>1.19</td><td>0.552</td></tr><tr><td>49</td><td>1,012</td><td>1,012</td><td>1,052</td><td>1.23</td><td>0.542</td></tr><tr><td>54</td><td>1,553</td><td>1,543</td><td>1,593</td><td>0.5</td><td>0.779</td></tr><tr><td>55</td><td>647</td><td>627</td><td>667</td><td>1.84</td><td>0.398</td></tr><tr><td>56</td><td>557</td><td>527</td><td>547</td><td>0.11</td><td>0.949</td></tr><tr><td>57</td><td>1,147</td><td>1,137</td><td>1,157</td><td>1.67</td><td>0.435</td></tr><tr><td>60</td><td>590</td><td>590</td><td>630</td><td>0.03</td><td>0.857</td></tr><tr><td>63</td><td>1,313</td><td>1,193</td><td>1,273</td><td>0.52</td><td>0.771</td></tr><tr><td>65</td><td>813</td><td>813</td><td>853</td><td>0.22</td><td>0.894</td></tr><tr><td>66</td><td>1,104</td><td>1,104</td><td>1,134</td><td>1.4</td><td>0.496</td></tr><tr><td>67</td><td>10,960</td><td>11,162</td><td>11,244</td><td>1.60</td><td>0.45</td></tr><tr><td>68</td><td>2,800</td><td>2,785</td><td>2,850</td><td>5.77</td><td>0.575</td></tr><tr><td>69</td><td>3,970</td><td>3,945</td><td>3,995</td><td>1.62</td><td>0.654</td></tr><tr><td>70</td><td>1,347</td><td>1,367</td><td>1,402</td><td>1.29</td><td>0.526</td></tr><tr><td>71</td><td>1,950</td><td>1,905</td><td>1,985</td><td>3.24</td><td>0.198</td></tr><tr><td>72</td><td>2,592</td><td>2,532</td><td>2,582</td><td>1.93</td><td>0.412</td></tr><tr><td>73</td><td>2,645</td><td>2,740</td><td>2,820</td><td>13.49</td><td>0.002</td></tr><tr><td>74</td><td>982</td><td>962</td><td>1,012</td><td>3.43</td><td>0.180</td></tr><tr><td>75</td><td>947</td><td>977</td><td>1,002</td><td>81.11</td><td>0.000</td></tr><tr><td>76</td><td>1,546</td><td>1,536</td><td>1,556</td><td>0.94</td><td>0.623</td></tr><tr><td>77</td><td>1,811</td><td>1,806</td><td>1,826</td><td>0.25</td><td>0.884</td></tr><tr><td>78</td><td>586</td><td>591</td><td>626</td><td>2.71</td><td>0.258</td></tr><tr><td>79</td><td>1,536</td><td>1,506</td><td>1,541</td><td>3.68</td><td>0.159</td></tr><tr><td>80</td><td>609</td><td>589</td><td>634</td><td>0.47</td><td>0.925</td></tr><tr><td>81</td><td>142</td><td>117</td><td>147</td><td>0.47</td><td>0.925</td></tr><tr><td>85</td><td>499</td><td>465</td><td>514</td><td>1.77</td><td>0.412</td></tr><tr><td>86</td><td>738</td><td>738</td><td>773</td><td>4.10</td><td>0.129</td></tr></table>

Note. p-Value less than 0.05 indicates significant difference between the expected and actual frequencies of the bid levels.

Table 1b Binomial Signs Test for Data with Cell Frequencies <5 and Two Bid Levels

<table><tr><td>Auction Number</td><td>Observed Revenue ($)</td><td>Simulated min ($)</td><td>Simulated max ($)</td><td>p-Value</td><td>Significance [1]</td></tr><tr><td>10</td><td>17,792</td><td>17,452</td><td>17,952</td><td>0.999601</td><td>**</td></tr><tr><td>21</td><td>11,175</td><td>10,835</td><td>10,955</td><td>0.999998</td><td>**</td></tr><tr><td>22</td><td>1,977</td><td>1,797</td><td>1,857</td><td>0.254037</td><td>**</td></tr><tr><td>24</td><td>2,456</td><td>2,396</td><td>2,456</td><td>0.969859</td><td>**</td></tr><tr><td>25</td><td>1,525</td><td>1,485</td><td>1,525</td><td>0.954083</td><td>**</td></tr><tr><td>26</td><td>2,065</td><td>2,057</td><td>2,075</td><td>0.954083</td><td>**</td></tr><tr><td>27</td><td>1,397</td><td>1,377</td><td>1,417</td><td>0.663923</td><td>**</td></tr><tr><td>28</td><td>2,156</td><td>2,076</td><td>2,156</td><td>0.122549</td><td>**</td></tr><tr><td>29</td><td>2,256</td><td>2,236</td><td>2,316</td><td>0.695468</td><td>**</td></tr><tr><td>31</td><td>3,135</td><td>3,095</td><td>3,135</td><td>0.985681</td><td>**</td></tr><tr><td>32</td><td>2,377</td><td>2,337</td><td>2,377</td><td>0.8738</td><td>**</td></tr><tr><td>33</td><td>4,973</td><td>4,913</td><td>4,973</td><td>0.826703</td><td>**</td></tr><tr><td>34</td><td>3,584</td><td>3,524</td><td>3,564</td><td>0.912039</td><td>**</td></tr><tr><td>37</td><td>10,665</td><td>10,635</td><td>10,805</td><td>0.133456</td><td>**</td></tr><tr><td>39</td><td>788</td><td>748</td><td>818</td><td>0.608374</td><td>**</td></tr><tr><td>45</td><td>1,885</td><td>1,905</td><td>1,915</td><td>0.84408</td><td>**</td></tr><tr><td>46</td><td>2,117</td><td>2,003</td><td>2,083</td><td>0.968891</td><td>**</td></tr><tr><td>48</td><td>788</td><td>758</td><td>828</td><td>0.122059</td><td>**</td></tr><tr><td>51</td><td>675</td><td>665</td><td>675</td><td>0.418515</td><td>**</td></tr><tr><td>52</td><td>897</td><td>877</td><td>887</td><td>0.902318</td><td>**</td></tr><tr><td>53</td><td>387</td><td>367</td><td>397</td><td>0.181963</td><td>**</td></tr><tr><td>58</td><td>1,247</td><td>1,227</td><td>1,247</td><td>0.8738</td><td>**</td></tr><tr><td>59</td><td>2,645</td><td>2,615</td><td>2,635</td><td>0.990591</td><td>**</td></tr><tr><td>61</td><td>1,506</td><td>1,506</td><td>1,566</td><td>0.076501</td><td>**</td></tr><tr><td>64</td><td>2,774</td><td>2,674</td><td>2,794</td><td>0.297668</td><td>**</td></tr><tr><td>82</td><td>1,397</td><td>1,377</td><td>1,387</td><td>0.444137</td><td>**</td></tr><tr><td>83</td><td>40</td><td>20</td><td>20</td><td>0.885114</td><td>**</td></tr><tr><td>84</td><td>1,289</td><td>1,264</td><td>1,289</td><td>0.0625</td><td>**</td></tr><tr><td>87</td><td>1,780</td><td>1,794</td><td>1,794</td><td>0.890625</td><td>**</td></tr></table>

Note. [1] Fail to reject Hypothesis H0 at p > 0025 (a/2) for nondirectiona binomial signs test.

The results presented in Table 1a show the application of the chi-square test. We fail to reject our null hypothesis if we get a p-value > 0 05. Of the 56 auctions shown in this table, we fail to reject our null hypothesis in all but four (auctions 17, 35, 73, and 75) of the cases. Table 1b shows similar data for those 29 auctions that failed to meet the assumptions required to use the chi-square test. For these, we have resorted to using the binomial signs test.

In all the 29 cases in Table 1b, above we expect no significant difference between the observed and the expected distribution of the bid levels. Together with Table 1a’s success in 52 out of 56 auctions, this gives us great confidence in the ability of the simulator to replicate the bidding strategies, and by extension the revenue generation dynamics of the real-world auctions that we tracked.

Further robustness of the simulation can be deduced by examining the range of the simulated revenue. Observe that this is quite small with the maximum range being 9% of the observed revenue and the median of the revenue ranges being only 2% of the observed revenue. This is an important parameter to consider in simulations, because excess variability can reduce the implications generated from simulating a process.

While the replication results are within standard statistical limits, we examined each of the four cases where we were not able to replicate (auction numbers 17, 35, 73, and 75) the original auction to gain potential insights into the revenue generation process.

## 5.2. Auctions that Could Not Be Replicated

We believe that in auction numbers 17 and 35, all the winning bids are at the level that coincides with the upper bound case in Yankee auctions because all the winning bids are at the same level and the observed revenue is greater than the highest revenue generated by the simulator. The probability of actually realizing the upper bound is very small because it requires that the marginal bidder (the person with the highest losing bid) is the first one to bid at the previous level. In the case of auction 75, there was a total of 18 winning bidders out of which 15 followed the evaluatory strategy and the other three were opportunists. There were no participators, whose presence brings into play the temporal combinatorial dynamics of these multiunit auctions. Both the above kinds of occurrences require that bid sequences from the start follow an epsilon likelihood specific pattern. Therefore, we believe that the simulation model does generate a reasonable range of revenues. However, in the above special cases, the observed revenue is the upper bound of all possible revenues, and the bidder mix is nonstandard, respectively.

![](/api/attachments/5RP4U5HU/fulltext/images/9d41399c8f93efb4f0cf9d36bac6d85eaae989db6326c22eded0a940593ac741.jpg)  
Figure 4 Some Patterns of Average Revenue with Different Bid Increments

For auction 73, we have an unusual case when one of the bidders chose to bid for 61 out of the 85 items, eventually winning 42. As discussed in §4, multiple quantity lumpy bids are allowed in such auctions, and are modeled in the simulation as multiple single-unit bids of similar type, say participatory. The overall success of the simulator in replicating the original auctions gives us confidence that this is indeed a reasonable approximation of the real-world strategic behavior by the bidders. However, this modeling assumption begins to get tested as the quantity becomes unusually large, as in auction 73. This rare extremity, resulting in a significant informational shortage regarding the strategic space of the auction, exposes one of the limitations of the current tool. This was an unusually large quantity bid with respect to the auctions we tracked, and it was difficult for the simulator to capture the strategy space of the 60 other bidders who were independently modeled to behave as the large quantity bidder.

## 5.3. Investigating the Effect of Bid Increment on Auction Revenue

In the next section, we present results where we try to maximize the revenue by changing the bid increment and observing its impact on average revenue.

Because the auction numbers 17, 35, 73, and 75 were not adequately replicated, we did not use them in further analysis. For the rest of the auctions, we ran the simulation program with different minimum bid increments ranging from \$1–\$20. During these simulation runs, the valuations of the bidders remained the same as in the case with the original bid increment. Figure 4 depicts some representative patterns of average revenue generated from these simulation runs. Note that the revenue does not seem to be a monotonic function of the bid increment. In auction numbers 10 and 18 there are significant peaks and valleys, with several local optima. One common and interesting observation that can be made from these graphs is that the local optima seem to be at the multiples of a given number. For example, in auction number 10, the local optima seem to be occurring at bid increments of 3, 6, 9, 12, and 15; in auction number 24 it seems to be at 4, 8, and 12; and in auction number 21 at 6, 12, and 18. Intuitively, this happens because the different multiples of the same number generate an overlapping set of feasible bid levels. Together with a fixed marginal consumer’s valuation V , this leads to identical values of $B _ { \mathrm { m a x } } ,$ , the marginal consumer’s bid, leading to the regular patterns of local optima that we observe.

Table 2 presents the results of our investigation on the effect of bid increments on auction revenue. The second column displays the observed bid increment and the third column presents the optimal bid increment, i.e., the bid increment that yielded the highest average revenue. We also provide, in the fourth column, the largest recommended bid increment that had statistically equivalent average revenue at 5% significance. The motivation for providing this information is that a smaller bid increment implies more rounds of bidding activity to reach the similar equilibrium as achieved by a larger bid increment. Therefore, it may be appropriate to use the largest bid increment that provides the highest level of revenue. This is the appropriate bid increment that a modeler can recommend to the auctioneers, as it converges the auction quicker. The fifth column presents the actual auction revenue and the sixth presents the minimum revenue produced by the optimal bid increment. It should be noted that in 43 out of the 85 cases the range of revenues from the simulation is such that the lowest revenue attained using the optimal bid increment is higher than the revenue obtained with the real-world observed bid increment. In these cases, using the optimal bid increment is a dominant strategy and it virtually assures that the generated revenue will be higher than that with the bid increment used.

Table 2 Effect of Bid Increment on Auction Revenue

<table><tr><td rowspan="2">Auction Number</td><td colspan="4">Bid</td><td colspan="2">Minimum</td></tr><tr><td>Increment k</td><td>Optimal K*</td><td>Recommended K</td><td>Auction Revenue</td><td>Revenue Using k*</td><td>Optimal Dominant</td></tr><tr><td>1</td><td>20</td><td>4</td><td>15</td><td>16,190</td><td>16,218</td><td>*</td></tr><tr><td>2</td><td>20</td><td>13</td><td>13</td><td>24,790</td><td>24,990</td><td>*</td></tr><tr><td>3</td><td>20</td><td>3</td><td>12</td><td>10,915</td><td>10,979</td><td>*</td></tr><tr><td>4</td><td>20</td><td>1</td><td>1</td><td>10,770</td><td>11,151</td><td>*</td></tr><tr><td>5</td><td>20</td><td>6</td><td>11</td><td>19,836</td><td>19,576</td><td></td></tr><tr><td>6</td><td>20</td><td>1</td><td>9</td><td>16,068</td><td>16,460</td><td>*</td></tr><tr><td>7</td><td>20</td><td>1</td><td>14</td><td>11,633</td><td>11,869</td><td>*</td></tr><tr><td>8</td><td>20</td><td>7</td><td>7</td><td>14,093</td><td>14,117</td><td>*</td></tr><tr><td>9</td><td>20</td><td>4</td><td>11</td><td>11,610</td><td>11,564</td><td></td></tr><tr><td>10</td><td>20</td><td>20</td><td>20</td><td>17,792</td><td>17,428</td><td></td></tr><tr><td>11</td><td>20</td><td>1</td><td>4</td><td>10,694</td><td>11,129</td><td>*</td></tr><tr><td>12</td><td>20</td><td>1</td><td>1</td><td>15,190</td><td>15,201</td><td>*</td></tr><tr><td>13</td><td>20</td><td>3</td><td>9</td><td>16,922</td><td>16,741</td><td></td></tr><tr><td>14</td><td>20</td><td>4</td><td>6</td><td>13,660</td><td>13,702</td><td>*</td></tr><tr><td>15</td><td>20</td><td>2</td><td>2</td><td>14,968</td><td>15,178</td><td>*</td></tr><tr><td>16</td><td>20</td><td>1</td><td>15</td><td>18,308</td><td>18,320</td><td>*</td></tr><tr><td>18</td><td>20</td><td>8</td><td>14</td><td>23,473</td><td>23,369</td><td></td></tr><tr><td>19</td><td>20</td><td>3</td><td>3</td><td>3,486</td><td>3,510</td><td>*</td></tr><tr><td>20</td><td>20</td><td>1</td><td>10</td><td>11,043</td><td>11,032</td><td></td></tr><tr><td>21</td><td>20</td><td>5</td><td>11</td><td>11,175</td><td>10,895</td><td></td></tr><tr><td>22</td><td>20</td><td>8</td><td>15</td><td>1,977</td><td>1,833</td><td></td></tr><tr><td>23</td><td>20</td><td>1</td><td>11</td><td>5,233</td><td>5,213</td><td></td></tr><tr><td>24</td><td>20</td><td>20</td><td>20</td><td>2,456</td><td>2,396</td><td></td></tr><tr><td>25</td><td>20</td><td>2</td><td>13</td><td>1,525</td><td>1,531</td><td>*</td></tr><tr><td>26</td><td>20</td><td>1</td><td>3</td><td>2,065</td><td>2,080</td><td>*</td></tr><tr><td>27</td><td>20</td><td>20</td><td>20</td><td>1,397</td><td>1,377</td><td></td></tr><tr><td>28</td><td>20</td><td>15</td><td>20</td><td>2,156</td><td>2,116</td><td></td></tr><tr><td>29</td><td>20</td><td>2</td><td>12</td><td>2,256</td><td>2,266</td><td>*</td></tr><tr><td>30</td><td>20</td><td>5</td><td>11</td><td>3,496</td><td>3,521</td><td>*</td></tr><tr><td>31</td><td>20</td><td>9</td><td>14</td><td>3,135</td><td>3,110</td><td></td></tr><tr><td>32</td><td>20</td><td>15</td><td>20</td><td>2,377</td><td>2,352</td><td></td></tr><tr><td>33</td><td>20</td><td>9</td><td>9</td><td>4,973</td><td>4,939</td><td></td></tr><tr><td>34</td><td>20</td><td>5</td><td>15</td><td>3,684</td><td>3,544</td><td></td></tr></table>

Table 2 (cont’d.)

<table><tr><td rowspan="2">Auction Number</td><td colspan="3">Bid</td><td colspan="3">Minimum</td></tr><tr><td>Increment k</td><td>Optimal K*</td><td>Recommended K</td><td>Auction Revenue</td><td>Revenue Using k*</td><td>Optimal Dominant</td></tr><tr><td>36</td><td>10</td><td>1</td><td>1</td><td>1,833</td><td>1,884</td><td>*</td></tr><tr><td>37</td><td>10</td><td>3</td><td>9</td><td>10,665</td><td>10,751</td><td>*</td></tr><tr><td>38</td><td>10</td><td>5</td><td>5</td><td>8,340</td><td>8,305</td><td></td></tr><tr><td>39</td><td>10</td><td>4</td><td>7</td><td>788</td><td>792</td><td>*</td></tr><tr><td>40</td><td>10</td><td>5</td><td>15</td><td>3,449</td><td>3,394</td><td></td></tr><tr><td>41</td><td>10</td><td>5</td><td>6</td><td>3,779</td><td>3,769</td><td></td></tr><tr><td>42</td><td>10</td><td>1</td><td>3</td><td>2,869</td><td>2,913</td><td>*</td></tr><tr><td>43</td><td>10</td><td>1</td><td>11</td><td>2,509</td><td>2,498</td><td></td></tr><tr><td>44</td><td>10</td><td>3</td><td>10</td><td>2,007</td><td>2,016</td><td>*</td></tr><tr><td>45</td><td>10</td><td>5</td><td>5</td><td>1,885</td><td>1,905</td><td>*</td></tr><tr><td>46</td><td>10</td><td>12</td><td>12</td><td>2,117</td><td>2,017</td><td></td></tr><tr><td>47</td><td>10</td><td>9</td><td>15</td><td>703</td><td>693</td><td></td></tr><tr><td>48</td><td>10</td><td>4</td><td>14</td><td>788</td><td>800</td><td>*</td></tr><tr><td>49</td><td>10</td><td>5</td><td>5</td><td>1,012</td><td>1,017</td><td>*</td></tr><tr><td>51</td><td>10</td><td>1</td><td>1</td><td>675</td><td>689</td><td>*</td></tr><tr><td>52</td><td>10</td><td>3</td><td>3</td><td>897</td><td>882</td><td></td></tr><tr><td>53</td><td>10</td><td>2</td><td>15</td><td>387</td><td>375</td><td></td></tr><tr><td>54</td><td>10</td><td>1</td><td>2</td><td>1,563</td><td>1,572</td><td>*</td></tr><tr><td>55</td><td>10</td><td>5</td><td>11</td><td>647</td><td>632</td><td></td></tr><tr><td>56</td><td>10</td><td>10</td><td>10</td><td>557</td><td>537</td><td></td></tr><tr><td>57</td><td>10</td><td>3</td><td>12</td><td>1,147</td><td>1,143</td><td></td></tr><tr><td>58</td><td>10</td><td>13</td><td>13</td><td>1,247</td><td>1,236</td><td></td></tr><tr><td>59</td><td>10</td><td>1</td><td>5</td><td>2,645</td><td>2,624</td><td></td></tr><tr><td>60</td><td>10</td><td>4</td><td>13</td><td>590</td><td>614</td><td></td></tr><tr><td>61</td><td>10</td><td>4</td><td>15</td><td>1,506</td><td>1,508</td><td>*</td></tr><tr><td>63</td><td>10</td><td>9</td><td>10</td><td>1,313</td><td>1,206</td><td></td></tr><tr><td>64</td><td>10</td><td>1</td><td>7</td><td>2,774</td><td>2,700</td><td></td></tr><tr><td>65</td><td>10</td><td>3</td><td>5</td><td>813</td><td>822</td><td>*</td></tr><tr><td>66</td><td>10</td><td>1</td><td>4</td><td>1,104</td><td>1,123</td><td>*</td></tr><tr><td>67</td><td>5</td><td>1</td><td>1</td><td>10,960</td><td>11,113</td><td>*</td></tr><tr><td>68</td><td>5</td><td>1</td><td>2</td><td>2,800</td><td>2,872</td><td>*</td></tr><tr><td>69</td><td>5</td><td>1</td><td>1</td><td>3,970</td><td>4,019</td><td>*</td></tr><tr><td>70</td><td>5</td><td>1</td><td>1</td><td>1,347</td><td>1,422</td><td>*</td></tr><tr><td>71</td><td>5</td><td>1</td><td>3</td><td>1,950</td><td>1,969</td><td>*</td></tr><tr><td>72</td><td>5</td><td>1</td><td>1</td><td>2,592</td><td>2,594</td><td>*</td></tr><tr><td>74</td><td>5</td><td>1</td><td>1</td><td>982</td><td>991</td><td>*</td></tr><tr><td>76</td><td>5</td><td>1</td><td>2</td><td>1,546</td><td>1,563</td><td>*</td></tr><tr><td>77</td><td>5</td><td>5</td><td>5</td><td>1,811</td><td>1,806</td><td></td></tr><tr><td>78</td><td>5</td><td>1</td><td>1</td><td>586</td><td>630</td><td>*</td></tr><tr><td>79</td><td>5</td><td>1</td><td>4</td><td>1,536</td><td>1,529</td><td></td></tr><tr><td>80</td><td>5</td><td>1</td><td>4</td><td>609</td><td>605</td><td></td></tr><tr><td>81</td><td>5</td><td>5</td><td>15</td><td>142</td><td>142</td><td></td></tr><tr><td>82</td><td>5</td><td>5</td><td>7</td><td>1,397</td><td>1,377</td><td></td></tr><tr><td>83</td><td>5</td><td>1</td><td>1</td><td>40</td><td>24</td><td></td></tr><tr><td>84</td><td>5</td><td>1</td><td>1</td><td>1,289</td><td>1,287</td><td></td></tr><tr><td>85</td><td>5</td><td>1</td><td>1</td><td>499</td><td>509</td><td>*</td></tr><tr><td>86</td><td>5</td><td>1</td><td>1</td><td>738</td><td>764</td><td>*</td></tr><tr><td>87</td><td>5</td><td>1</td><td>1</td><td>1,780</td><td>1,794</td><td>*</td></tr></table>

## 5.4. Analysis—Bid Increments, Endogenous Entry, and Transaction Costs

Looking across the 85 auctions of Table 2, we observe an average 1.42% increase in revenue by adopting the optimal bid increment. In light of the fact that the items—typically aging computer hardware and consumer electronics, sold through these auctions are often sold at fractional margins—this represents a potentially significant gain in revenue. Only 12 out of the 85 cases have support for bid increments greater than the original bid increment k, with the original bid increment k being among the highest revenue generator for only four auctions. Thus, in aggregate, our results suggest that smaller bid increments on average yield higher expected revenue.

An auctioneer desiring to apply our findings could question whether changing the bid increment endogenously influences the number of bidders who enter the auction. Typically, the auction theory literature takes the number of bidders at an auction as exogenously given (Paarsch 1992, Laffont et al. 1995). Notable exceptions to this are Engelbrecht-Wiggans (1987), under the independent private values model and Harstad (1990) under the common values model. Engelbrecht-Wiggans (1987) found that the auctioneer realized higher expected revenue by choosing a reserve price that led to a larger number of bidders. In contrast, Harstad (1990) under the common value setting, points out that a seller often prefers an auction procedure because it generates fewer participants. The underlying logic is that given common values, a fewer number of participants will imply a higher chance of winning, and hence, in equilibrium, each bidder may settle for lower expected profit, thereby benefiting the seller. This is echoed in Levin and Smith (1994), who claim that the presence of too many bidders increases coordination costs that hurt welfare. More recently, Bajari and Hortascu (2001) have shown empirically, with single-unit data from eBay, that modifying the mechanism affects the entry decisions.

In our case, the number of bidders is held constant in the current simulation trials. A full-blown test to determine whether endogenous factors impact entry in multiunit auctions would also require a consideration of several market factors through a controlled field experiment, and is well beyond the scope of this study. Yet, a simple empirical test with our dataset indicates that the bid increment has no significant influence on the number of bidders who enter into an auction (see Appendix A for details of this model). We find that the lot size has significant positive influence on the number of bidders, and that lowering the opening bid also has a significant positive influence on attracting entry. As a next step, we regressed these two significant variables (N and R) on our simulation’s optimal bid increment (see Appendix B for details of this model).

The linear regression indicates that the optimal bid increment is negatively correlated with the lot size of the auction as well as the opening bid. In light of this fact, we recommend smaller increments as the lot size increases. Additionally, because the lot size positively influences the number of bidders, some of the revenue enhancements coming out of our simulation trials may be due to the benefits of having smaller increments in a larger pool of bidders. Intuitively, one needs several bidders making small jumps to compensate for one bidder making a large jump. From an allocative efficiency perspective, smaller increments are always preferred as they decrease the likelihood of inefficient allocations. For instance, a bidder with a value of \$20 cannot inefficiently outbid anyone with a k <sub>=</sub> 1, but could possibly outbid others with valuations in the interval 21–24 if k were 5 and she bid \$20.

The potential cost of using smaller increments is that it may take longer to converge. Given the opportunity costs of the auction participants, the recommended bid increments of Table 2 provide a useful alternative to the auctioneers.

In the next section, we show the versatility of the simulator by examining endogeniety at the level of bidding strategies adopted by the bidders.

## 6. The Simulator as a Risk-Free, Cost-Effective Decision Tool

One of the main advantages of having a reliable and robust simulator of a real-world process, such as an online auction market, is the potential of cost effectively testing a variety of scenarios that otherwise would be too risky to test in a real-world setting. We demonstrate this both from the auctioneer’s perspective and the bidder’s perspective. For the former, we examine a scenario in which the bidding strategy employed by bidders is endogenously influenced. For the latter, we consider the impact of some more sophisticated bidding strategies on the likelihood of winning and/or improving surplus. Both of these are elaborated in the sections below.

## 6.1. Endogenous Impact on Bidding Strategy

In general, if changing a parameter may endogenously impact another parameter, then we cannot look at the impact of changing the parameter in isolation. For example, if endogenous factors such as the lot size, the bid increment, the opening bid, and possibly the absolute magnitude of the auction influence the bidding strategies employed by the bidders, then we cannot change the bid increment alone and measure its effect on revenue.

As pointed out in §1.1, the literature also assumes homogeneity amongst bidders. In contrast, as discussed in §3.2, we observed at least three distinct bidder behaviors in online Yankee auctions. Here, we examine endogeniety at a finer granularity, by questioning whether endogenous changes that modify the mechanism, such as using a different bid increment, affects the bidding strategies adopted by those who chose to enter. For instance, one could hypothesize that, if transaction costs of placing a bid are significant, increasing the bid increment may induce a larger proportion of bidders to behave as participators. A natural followup research question is that if indeed bidding strategies are impacted by endogenous factors, then what are the implications of this on the optimal bid increments recommended in §5 3, as well as on the auctioneer’s revenue? The simulation platform is ideally suited to test this. If the situation warrants, the approach shown in this section can be extended to deal with other, perhaps more traditional, endogeniety questions that relate the design choices with the number of bidders that are drawn to the auction.

We address whether endogeniety is a factor by developing a multinomial logit regression model that considers the auctioneer’s control factors, namely, the bid increment k, the lot size N , and the opening bid R, as independent variables. In addition, Lucking-Reiley and List (2000) demonstrate that as far as bidding costs are concerned, stakes do indeed matter. In his field experiments, high-priced (\$70) cards produced more of the theoretically predicted strategic behavior than did lower-priced (\$3) cards. Thus, we also use as an independent variable, a stake variable MAG that captures the magnitude of the auction, and is computed as the average winning price of the multiunit auction. The dependent variables in the generic form $p r o b _ { s t r a t e g y }$ represent the probability that a bidder adopts a given strategy, and capture the relative likelihood of a bidder adopting one of the three bidding strategies described in §3.2. Our preliminary analysis indicated that both the lot size and the opening bid, as well as higher-order terms, failed to explain any of the variation in the bidder’s likelihood of adopting a given strategy. It is interesting to note that while the opening bid is significant in explaining entry (see §5.4), it does not have an influence on the bidder’s strategy, after they chose to enter. This leads us to the following MULTILOG model with two regression equations corresponding to the three response levels. The maximum likelihood parameter estimates were estimated in SAS using our entire data set of 1,546 bidders.

$$
\begin{array}{r l} & {\log (p r o b _ {p a r t i c i p a t o r} / p r o b _ {e v a l u a t o r})} \\ & {\qquad = - 1. 0 5 0 5 + 0. 0 4 7 4 k + 0. 0 0 1 8 1 \mathrm{MAG} + \varepsilon ,} \\ & {\log (p r o b _ {o p p o r t u n i s t} / p r o b _ {e v a l u a t o r})} \\ & {\qquad = - 1. 4 8 0 5 + 0. 0 3 1 8 k + 0. 0 0 1 9 7 \mathrm{MAG} + \varepsilon .} \end{array}
$$

Both the chi-square model and the six parameter estimates are significant at the $\alpha = 0 . 0 5$ level, indicating that the bid increment and magnitude of the auction have a significant impact on the likelihood of a bidder adopting a certain strategy. The positive coefficients reflect that as k increases and as MAG increases, bidders are less likely to use the evaluator strategy. This is an interesting empirical finding of our work and could potentially have significant implications on future mechanism design consideration of such auctions.

6.1.1. Impact of Endogeniety in Bidding Strategy on Optimal Bid Increments. To demonstrate the versatility of the simulation platform, we examine whether we would need to alter the recommendations of the optimal bid increment presented in §5.3 if we factored in the endogeniety of bidding strategies with respect to the changing bid increment. We are also interested in examining the impact, if any, on the auctioneer’s revenue. Recall that for each tracked auction, we have the percentage break-up of the adopted bidding strategies. Using a relative distance approach, we adjust the de facto observed bidding strategy mix as a function of the trial bid increments used in a particular simulation run, the auction’s magnitude, and the predicted bidding strategy mix from the MULTILOG model.

We repeated the entire set of experiments in §5.3, using the 81 auctions, and found that there was no significant difference in the optimal bid increment with endogenously determined bidder strategy mix. The optimal auction revenues at the endogenously determined optimal bid increments also showed no significant difference. These results indicate that, while bidders are more likely to adopt participatory strategies as the bid increments are higher (or bidding costs are lower) as well as if the stakes are higher, the magnitude of these effects is not significant enough to cause structural changes in the revenue generation process. One intuitive explanation is that the multiunit nature of such auctions dilutes the impact and as long as there exists a significant proportion of participators, who are primarily candidates for being the price-setting bidders, the endogeniety does not have an impact on the choice of optimal bid increments and the expected revenue. Next, we demonstrate the versatility of the simulation platform from the perspective of the bidder’s strategies.

## 6.2. Hybrid-Bidding Strategies

Much of the existing auction theory focuses on how the auctioneer’s (bid taker) expected revenue depends upon the bidding rules. There is ignorance of studying how bids are made, what bidding strategies are adopted, and what implications they might have. Only recently has this area begun to draw interest. Wilcox (2000) demonstrated empirically that most nonprofessional bidders do not bid in a manner following the game-theoretic predictions, whereas experienced bidders do. Bajari and Hortacsu (2001) find that costly entry is important to understanding bidding behavior in these auctions. Lucking-Reiley and List (2000) find that seller reputation, minimum bids, and auction duration all affect prices in significant ways.

One other relevant paper is Easley and Tenorio’s (2001) analysis of “jump bidding” behavior, a strategy that entails bidding more than the minimum increment. They focus on the questions: Do jump bidders place fewer bids overall and does increased early jump bidding in auctions reduce the total bids placed? To the best of our knowledge, no prior research has looked at whether such strategies improve the likelihood of winning for the bidder, as well as their impact on the surplus of the bidders. We consider two potential ways to operationalize what we call hybrid-bidding strategies. These are strategies that could be considered as combinations of the bidding strategies described in §3.2.

For demonstrative purposes, for each auction, we randomly chose one bidder, having a valuation within one bid increment away from the auction’s marginal bid, and following a participatory strategy in the original auction. We repeated this four times within an auction, choosing a different candidate bidder each time. For the entire set of 81 auctions, we tagged this bidder and imbibed her with the hybrid-bidding strategies described in the next two sections. To isolate the impact of the new bidding strategy, we compared the performance of the same bidder adopting the participatory strategy versus the hybrid strategy, keeping all other parameters the same. The metrics used for the comparison were (a) the percentage of times the bidder won the auction, and (b) the average price paid by the bidder over the 30 repetitions of the simulation, with lower being better.

6.2.1. Proportional Jump Bidding. Consider a participator who does not always bid at the required minimum bid level. Instead, under certain conditions, she jumps the bid by one bid increment, with the expectation that she will be able to exploit the time priority and be the early entry at the next bid level. The condition we utilize increases the likelihood of a jump bid in proportion to the number of bidders who are currently winning the auction with bids at the minimum required bid or higher. For instance, suppose in a six-item auction with a bid increment of \$10, the current minimum required bid is \$100. A hybrid participator stochastically chooses to bid \$110, with a probability of 2/6 if there are two winners at bid levels of \$100 or higher and with a probability of 4/6 if there are four bidders at bid levels of \$100 or higher. The results of this analysis are presented in Table 3.

Columns 1 and 2 display the number of times on average that the plain pedestrian participator and the proportional jump bidder win, respectively. The higher this value, the higher the likelihood of winning. Note that the maximum value here is 30, indicative of the number of replications of an auction, and for marginal valued bidders, both strategies yielding close to 22 wins is indicative of the robustness of the simulation process. Columns 3 and 4 report the average value of the winning bid. The lower this value, the higher the relative surplus extraction for that strategy. Table 3 indicates that participators have a significantly higher surplus than proportional jump bidders. Observe that proportional jump bidding, even though it utilizes more of the other bidder’s information, in contrast to a plain pedestrian approach, does not increase the likelihood of winning. There is no significant difference in the auctioneer’s revenue from either of the two strategies. In the next section, we consider an alternative bidding approach that, by design, should increase the likelihood of winning the auction.

6.2.2. Strategic-at-Margin (SAM) Bidding. Consider a participator who decides to jump bid only at the margin, with certainty. That is, if the current required bid is one increment away from her maximum feasible bid, then the bidder always jump bids, i.e., places her final bid. In all other bidding instances the bidder adopts a participatory strategy. We call such a strategy “strategic-at-margin” (SAM) bidding. Ex ante, such a strategy would be expected to significantly increase the likelihood of a bidder winning the auction, while the impact on surplus is not apparent. If we relax the common assumption that a bidder’s top bid is close to its valuation, as is the case with financially constrained capital-limited bidders (Che and Gale 1998), it is easy to see that the SAM strategy would be ideal for such bidders.<sup>6</sup> The simulator serves as an ideal test platform for such an approach. The results are presented in Table 4.

Table 3 Proportional Jump Bidding vs. Participatory Bidding Approaches (Winning Percentage and Surplus)

<table><tr><td rowspan="2">Proportional Jump Bidding</td><td colspan="2">(max 30)</td><td rowspan="2">Surplus Hybrid</td><td rowspan="2">Surplus Part</td></tr><tr><td>Hybrid Count</td><td>Part Count</td></tr><tr><td>Mean</td><td>22.29807692</td><td>22.43910256</td><td>7.842503029</td><td>8.796004104</td></tr><tr><td>Variance</td><td>29.3674561</td><td>30.16348215</td><td>51.81919686</td><td>50.44901638</td></tr><tr><td>Observations</td><td>312</td><td>312</td><td>312</td><td>312</td></tr><tr><td>Hypothesized Mean Difference</td><td>0</td><td></td><td>0</td><td></td></tr><tr><td>df</td><td>622</td><td></td><td>622</td><td></td></tr><tr><td>t Statistic</td><td>-0.322852397</td><td></td><td>-1.665436773</td><td></td></tr><tr><td>p(T ≤ t) One-Tail</td><td>0.373457764</td><td></td><td>0.048164594</td><td></td></tr></table>

Table 4 Strategic-at-Margin (SAM) Bidding vs. Participatory Bidding Approaches (Winning Percentage and Surplus)

<table><tr><td rowspan="2">SAM Bidding</td><td colspan="2">(max 30)</td><td rowspan="2">Surplus Hybrid</td><td rowspan="2">Surplus Part</td></tr><tr><td>Hybrid Count</td><td>Part Count</td></tr><tr><td>Mean</td><td>24.22327044</td><td>22.08805031</td><td>6.057965115</td><td>8.822553398</td></tr><tr><td>Variance</td><td>16.16765867</td><td>34.32029839</td><td>26.29290786</td><td>54.7026213</td></tr><tr><td>Observations</td><td>318</td><td>318</td><td>318</td><td>318</td></tr><tr><td>Hypothesized Mean Difference</td><td>0</td><td></td><td>0</td><td></td></tr><tr><td>df</td><td>561</td><td></td><td>565</td><td></td></tr><tr><td>t Statistic</td><td>5.358735426</td><td></td><td>-5.477892426</td><td></td></tr><tr><td>p(T ≤ t) One-Tail</td><td>6.1275E-08</td><td></td><td>3.24407E-08</td><td></td></tr></table>

Observe that the bidder’s likelihood of winning the auction is significantly ( <sub>=</sub> 1%) enhanced by adopting the SAM strategy. Given identical budget constraints, the SAM approach is likely to win 24 out of 30 times in contrast to the participatory approach which wins 22 out of 30 times. At the same time, this comes at a cost. The participatory strategy extracts a relatively higher surplus. There is no significant difference in the auctioneer’s revenue from either of the two strategies. It is easy to see that there exists a level of budget constraint, beyond which it is a dominant strategy for the capital-limited bidder to adopt SAM bidding. Consider the following numerical example that uses Table 4.

Numerical Example 3. For a bidder adopting SAM in an auction with k 20, note that

$$
\mathrm{total~surplus(SAM)} = 6. 0 6 * 3 0 = 1 8 1. 8.
$$

Let $x = 1 8 1 . 8 / 2 4 = 7 . 5 7$ denote the actual average surplus using SAM. If the bidder has a valuation V $B + S ,$ where B is the maximum feasible bid B and S is the surplus, then it is easy to compute the number of times a participator wins at B and infer the number of times she wins at $B - k ,$ one increment below.

Suppose, when using participatory strategy, the person wins n times at B and (22 n) times at (B k). Then,

$$
\begin{array}{c} n * 7. 5 7 + (2 2 - n) * (2 0 + 7. 5 7) = 8. 8 2 * 3 0 = 2 6 4. 6 8 \\ \Rightarrow 2 0 n = 3 4 1. 9 2 \Rightarrow n = 1 7. \end{array}
$$

For SAM to be optimal for our hypothetical bidder whose valuation is $B + S ,$ the following has to hold:

$$
\begin{array}{c} 2 4 * S > 5 * (2 0 + S) + 1 7 * S \\ \Rightarrow S > 5 0. \end{array}
$$

Therefore, as long as the budget-constrained bidder has valuation greater than \$50 above maximum feasible bid, it is optimal to bid using SAM.

The analyses presented in §§6.1 and 6.2 is by no means an exhaustive enumeration of the versatility of the simulation platform. However, they do test some of the insights provided by empirical and experimental models, by providing a benchmark of comparison when analytical or normative results are difficult to obtain. We expect this to be an interesting area of future research. Among the issues of interest will be the enumeration of the hybrid-strategy space that can be employed by the bidders resulting from a combination of the three core strategies we have identified. Subsequently, can we find dominant strategies that are either pure or contingent in nature?

## 7. Conclusions and Directions for Future Research

In this paper, we have presented a cost-effective tool in the form of a simulation model that replicates and subsequently improves the design of online

Yankee auctions. Tools such as these can be used ex ante in a dynamic marketplace, potentially avoiding many of the pitfalls that can emerge from costly entrepreneurial ventures that resemble uncontrolled field experiments.

More work is needed in considering the impact of progressive lumpy bidding in multiunit auctions. Prior work in analyzing the price-quantity choice issue in multiunit bidding has been done assuming a one-shot sealed bid environment, and has primarily focused on examining revenue equivalence between the discriminatory and uniform pricing multiunit auctions. Wilson (1979), assuming an exogenously given number of bidders, uses examples to show that the multiplicity of strategies resulting from demand-schedule bidding, could lead to bidders adopting strategies that are disadvantageous to the seller, as well as make winner determination nontrivial. Engelbrecht-Wiggans and Kahn (1998), while examining the case where bidders can win a variable number of units under demand-schedule specification, establish that the pay-your-bid mechanism (such as the Yankee) induces the highest bid to be shaded most signifi cantly. This leads to a tendency for “bunching” of bids at the same price even when the valuations of the goods is different. Tenorio (1999) draws a similar conclusion while analyzing revenue equivalence, indicating that with “lumpy” bid specification in a discriminatory setting, bidders have an incentive to understate their average valuations. Interestingly, this finding relates all the way back to Vickrey (1961). Indeed, more recent empirical and experimental work (Engelbrecht-Wiggans et al. 1999, Kagel and Levin 1997, respectively) has also found evidence of demand reduction in multiunit uniform auctions. Engelbrecht-Wiggans et al. (1999) demonstrate, through a field experiment that had endogenous entry, that in the case of two units being auctioned, demand reduction or bid shading for the second item exists, but reduces as the number of bidders increases.

Intuitively, the findings from the related literature suggest to us that the Yankee practitioners, by opting for the simpler and easier to understand lumpy bid specification in favor of the full demand schedule specification, are focusing on attracting entry to the auction. Naïve bidders on the Internet, as well as bidders for whom minimizing bid preparation costs is important, are likely to be deterred by a complex bid specification scheme. To what extent the progressive nature of the auction further dilutes any demand-reduction impact of the lumpy discriminatory mechanism, and how this impacts endogenous entry into the auction, remain promising areas of future research.

The simulation model uses the observed bids from real online auctions to instantiate the parameters and implements broad bidding strategies for replicating a given auction. Our results indicate that the simulation model works very well, with 81 out of the 85 auctions successfully being replicated.

The simulation model can be used to change the controllable parameters such as bid increment, starting bid amount, and other rules of auctions to investigate the impact on the auctioneers’ revenue. In addition, as shown, the effect of alternative strategies by the bidders and its impact on their surplus can also be studied.

This paper investigated the impact of changing the minimum required bid increment on the auctioneers’ revenue. Our result indicated that for the majority of the auctions, the auctioneers used a significantly higher value for the minimum bid increment than the optimal value. While the magnitude of the impact on revenue was small for the majority of the cases, in light of small margins on the items usually sold through these auctions, the impact on profit may be greater than 100%.

We further illustrate the versatility of our approach by considering a scenario where the policy recommendations, if adopted, could in turn influence the strategies adopted by the bidder. A multinomial logit model indicates that the likelihood of a bidder adopting a certain strategy is significantly impacted by the choice of the bid increment as well as the magnitude of the auction. Empirical results validate that lowering the bidding cost, by raising the bid increment, increases the likelihood of adopting a participatory strategy. Such endogeniety is then implemented into the simulation model and we test whether it is significant enough to alter the original optimal bid increment recommendations.

From the perspective of bidding strategies deployed by real-world bidders, our approach provides a fertile experimentation bed, as demonstrated by two potential hybrid-bidding strategies that could be used by the bidders. While proportional jump bidding appeals in theory, the SAM bidding approach, ideal for capital-limited bidders, significantly increases the likelihood of a bidder’s winning chances, albeit at a cost of surplus.

In summary, the simulation model developed in this paper is a tool, which can potentially be used by the auctioneers to investigate a variety of issues. These range from setting different control parameters and rules for a given auction to investigating the impact of bidding strategies on consumer surplus as well as the auctioneers’ revenue. We believe that using a calibrated model along the lines of this one, with subjective corrections for shortcomings of the model and the data, will be more powerful then either the purely subjective or the mechanically calibrated alternatives.

## Acknowledgments

This research was supported by NSF CAREER Grant #IIS-0301239, but does not necessarily reflect the views of the NSF. Partial support for this research was also provided by TECI—the Treibick Electronic Commerce Initiative, and the OPIM Department, School of Business, University of Connecticut. The authors thank an anonymous referee for several useful comments that helped improve the manuscript.

## Appendix A. Modeling Endogenous Entry

We use the number of auction participants (NUM) as our dependent variable. We test whether market factors such as the average price of the product (MAG), endogenous factors such as the lot size N , the opening bid R, and the bid increment k, have any impact on entry into the auction. Because we had three levels of the bid increment we used two dummy variables such that

<table><tr><td>DUM1</td><td>DUM2</td><td>k</td></tr><tr><td>0</td><td>0</td><td>5</td></tr><tr><td>1</td><td>0</td><td>10</td></tr><tr><td>0</td><td>1</td><td>20</td></tr></table>

Note that all auctions were of 24 hours duration, so that is not a factor. A thorough residual analysis and an examination of several higher-order effects lead us to the following regression model:

$$
\begin{array}{c} \operatorname{Ln} (\operatorname{NUM}) = 2. 8 1 + 0. 0 4 7 N + 0. 0 0 0 5 \operatorname{MAG} - 0. 0 9 8 R \\ + 0. 2 6 \operatorname{DUM1} + 0. 3 1 \operatorname{DUM2} + \varepsilon . \end{array}
$$

The overall model is significant at the  0 05 level and the R-square is 70.3%, high for empirical data. Thus, we believe that this is a reasonable model for explaining variation in the number of bidders who come into an auction. Amongst the individual coefficients for the independent variables, only the lot size and the opening bid are significant at the  <sub>=</sub> 0 05 level. The model indicates that entry is higher with higher lot sizes and decreasing the opening bid has a positive influence in attracting more bidders. This probably explains some of the large newspaper advertisements proclaiming “bidding starts at \$1!” Importantly, for the purpose of this study, the bid increment is not significant in explaining the variation in the number of bidders.

## Appendix B. Optimal Bid Increments Regressed with Significant Variables

Model <sub>→</sub> k∗ <sub>=</sub>  <sub>+</sub> #1N <sub>+</sub> #2R <sub>+</sub>

<table><tr><td colspan="2">Regression Statistics</td></tr><tr><td>Multiple R</td><td>0.393213203</td></tr><tr><td>R-Square</td><td>0.154616623</td></tr><tr><td>Adjusted R-Square</td><td>0.133482038</td></tr><tr><td>Standard Error</td><td>4.312413072</td></tr><tr><td>Observations</td><td>83</td></tr></table>

<table><tr><td>ANOVA</td><td>df</td><td>SS</td><td>MS</td><td>F</td><td>Significance F</td></tr><tr><td>Regression</td><td>2</td><td>272.1029016</td><td>136.0515</td><td>7.315811</td><td>0.001208226</td></tr><tr><td>Residual</td><td>80</td><td>1,487.75252</td><td>18.59691</td><td></td><td></td></tr><tr><td>Total</td><td>82</td><td>1,759.855422</td><td></td><td></td><td></td></tr><tr><td></td><td>Coefficients</td><td>Standard Error</td><td>t Statistic</td><td>p-Value</td><td></td></tr><tr><td>Intercept</td><td>7.06579426</td><td>0.881317709</td><td>8.017307</td><td>7.48E-12</td><td></td></tr><tr><td>N</td><td>-0.089429332</td><td>0.025726577</td><td>-3.47615</td><td>0.000825</td><td></td></tr><tr><td>R</td><td>-0.409295943</td><td>0.174208165</td><td>-2.34946</td><td>0.021267</td><td></td></tr></table>

## References

Bajari, P., A. Hortascu. 2001. Winner’s curse, reserve prices and endogenous entry: Empirical insights from eBay auctions. Working paper, Department of Economics, Stanford University, Stanford, CA.

Banks, J., J. S. Carson. 1984. Discrete-Event System Simulation. Prentice-Hall, Englewood Cliffs, NJ.

Bapna, R., P. Goes, A. Gupta. 2000. A theoretical and empirical investigation of multi-unit on-line auctions. Inform. Tech. Management 1(1) 1–23.

. 2001. Online auctions: Insights and analysis. Comm. ACM 44(11) 42–50.

. 2003. Analysis and design of business-toconsumer online auctions. Management Sci. 49(1) 85–101.

Che, Y. K., I. Gale. 1998. Standard auctions with financially constrained bidders. Rev. Econom. Stud. 65(1) 1–21.

Easley, R., R. Tenorio. 2001. Bidding strategies in Internet Yankee auctions. Working paper, Notre Dame University, South Bend, IN.

Engelbrecht-Wiggans, R. 1987. On optimal reserve price in auctions. Management Sci. 33 763–770.

, C. M. Kahn. 1998. Multi-unit pay-your-bid auctions with variable rewards. Games Econom. Behavior 23 25–42.

, J. A. List, D. Lucking-Reiley. 1999. Demand reduction in multi-unit auctions with varying numbers of bidders: Theory and field experiments. Working paper, Department of Economics, University of Arizona, Tuscon, AZ.

Harstad, R. M. 1990. Alternative common-value auction procedures: Revenue comparisons with free entry. J. Political Econom. 98(2) 421–429.

Herschlag, M., R. Zwick. 2000. Internet auctions—A popular and professional literature review. Quart. J. Electronic Commerce 1(2) 161–186.

Kagel, J. H., D. Levin. 1997. Independent private value multi-unit demand auctions: An experiment comparing uniform-price and dynamic Vickrey auctions. Working paper, University of Pittsburgh, Pittsburgh, PA.

Kauffman, R. J., F. J. Riggins. 1998. Information systems and economics. Comm. ACM 41(8) 32–34.

Klemperer, P. 1999. Auction theory: A guide to the literature. J. Econom. Surveys 13(3) 227–286.

Laffont, J. J., H. Ossard, Q. Vuong. 1995. Econometrics of first-price auctions. Econometrica 63(4) 953–980.

Lee, B., K. Mehta. 1999. Efficiency comparison in electronic market mechanisms: Posted price versus auction market. WISE Conf. 1999, Charlotte, NC.

Levin, D., J. L. Smith. 1994. Equilibrium in auctions with entry. Amer. Econom. Rev. 84(3) 585–599.

Lu, Xiaohua, P. R. McAfee. 1996. The evolutionary stability of auctions over bargaining. Games Econom. Behavior 15(2) 228–254.

Lucking-Reiley, D. 2000. Auctions on the Internet: What’s being auctioned, and how? J. Indust. Econom. 48(3) 227–252.

, J. A. List. 2000. Bidding behavior and decision costs in field experiments. Working paper, Department of Economics, University of Arizona, Tuscon, AZ.

McAfee, R. P., J. McMillan. 1987. Auctions and bidding. J. Econom. Literature 25 699–738.

Milgrom, P. 1989. Auctions and bidding: A primer. J. Econom. Perspectives 3 3–22.

, R. Weber. A theory of auctions and competitive bidding. Econometrica 50 1089–1122.

Nash, J. 1950. The bargaining problem. Econometrica 18 155–162.

Nautz, D., E. Wolfstetter. 1997. Bid shading and risk aversion in multi-unit auctions with many bidders. Econom. Lett. 56 195–200.

Nwana, H., J. Rosenschein. T. Sandholm, C. Sierra, P. Maes, R. Guttmann. 1998. Agent-mediated electronic commerce: Issues, challenges and some viewpoints. Proc. 2nd Internat. Conf. Autonomous Agents, Minneapolis, MN (May 9–13) 189–196.

Paarsch, H. J. 1992. Deciding between common values and private vale paradigms in empirical models of auctions. J. Econometrics 51 191–215.

Pavlou, P. A., S. Ba, 2000. Does online reputation matter?—An empirical investigation of reputation and trust in online auction markets. Proc. AMCIS 2000 Conf., Long Beach, CA.

Roth, A. E., A. Ockenfels. 2000. Last minute bidding and the rules for ending second-price auctions: Theory and evidence from a natural experiment on the Internet. Working paper, Department of Economics, Harvard University, Cambridge, MA.

Rothkopf, M. H., R. M. Harstad. 1994a. Modeling competitive bidding: A critical essay. Management Sci. 40(3) 364–384.

. 1994b. On the role of discrete bid levels in oral auctions. Eur. J. Oper. Res. 74 572–581.

Tenorio, R. 1999. Multiple unit auctions with strategic pricequantity decisions. Econom. Theory 13 247–260.

Vakrat, Y., A. Seidmann. 1999a. Analysis and design models for online auctions. Proc. INFORMS Conf. Inform. Systems Tech. (CIST), Cincinnati, OH, 64–78.

. 1999b. Can online auctions beat online catalogs?. P. De, J. DeGross, eds. Proc. 20th Internat. Conf. Inform. Systems (ICIS ’99), Charlotte, NC.

Van Heck, E., P. Vervest. 1998. How should CIO’s deal with webbased auctions? Comm. ACM 41(7) 99–100.

Vickrey, W. 1961. Counter speculation, auctions and competitive sealed tenders. J. Finance 41 8–47.

Wilcox, R. T. 2000. Experts and amateurs: The role of experience in Internet auctions. Marketing Lett. 11(4) 363–374.

Wilson, R. 1979. Auctions of shares. Quart. J. Econom. 93(4) 675–689.
