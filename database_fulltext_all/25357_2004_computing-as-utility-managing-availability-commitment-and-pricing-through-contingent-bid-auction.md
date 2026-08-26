---
otero_id: 25357
otero_key: "CJQTU7CQ"
title: "Computing as Utility: Managing Availability, Commitment, and Pricing Through Contingent Bid Auctions"
authors: "HEMANT K. BHARGAVA; SHANKAR SUNDARESAN"
year: "2004"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2004.11045806"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computing as Utility: Managing Availability, Commitment, and Pricing Through Contingent Bid Auctions

HEMANT K. BHARGAVA AND SHANKAR SUNDARESAN

HEMANT K. BHARGAVA is a Professor at the Graduate School of Management at the University of California, Davis. Dr. Bhargava’s current research is in economics of information systems and information technology industry, covering pricing, product variety, operations, and competition. Specific topics include preferential placement in Internet search engines, product versioning, quality-contingent pricing under quality uncertainty, and synergies between inventory management and stockout discount pricing in electronic retailing. Dr. Bhargava’s past work studied management decision technologies, Web-based decision computation, and logic modeling. He has published on these topics in several academic journals. He is on the Editorial Boards of Operations Research, Management Science, and Decision Support Systems.

SHANKAR SUNDARESAN is an Assistant Professor in the Supply Chain and Information Systems Department of the Smeal College of Business at Pennsylvania State University. He studies information goods and services and their pricing strategies. His research on the management of information resources includes the analysis of corporate IT standards and knowledge management systems. Dr. Sundaresan’s research interests also include economics of information systems, pricing, IT-intensive commerce, automated database design, and the impact of information technology trends on supply chains. He was awarded the Winmill Software Faculty Fellowship in 1999. His work won research awards in 1995, 1996, 1997, and 2002 at premier IS conferences. Dr. Sundaresan’s research has appeared in the International Journal of Electronic Commerce, Information Systems Frontiers, ACM Transactions on Database Systems, Data & Knowledge Engineering, and other journals.

ABSTRACT: Enabled by advances in grid and network computing architectures for the delivery of on-demand computing services, the vision of an e-services economy in which computing will be as ubiquitous as a utility is becoming a possibility in business computing. Major firms in the computing industry such as IBM, Hewlett-Packard, and Sun Microsystems are focusing on agility and flexibility of computing resources and gearing up for their own versions of on-demand computing and information technology (IT) outsourcing solutions. The successful introduction of these new computing models requires the development of appropriate pricing mechanisms that are consistent with the enabling technologies. Our paper introduces the notion of contingent auctions to address this lacuna. In contingent auctions, users bid for computing resources in an auction, but are relieved from the contract (paying a penalty) if demand is not realized. We study different mechanisms—ranging from an advance commitment (capacity reservation) to no commitment (pay-as-you-go)—under demand uncertainty. We consider markets in which the demand for computing is uncertain and, moreover, users’ value of computing and demand realization may be related.

We show how the different levels of commitment affect prices, revenues, and resource utilization under different market conditions. Our results reiterate the need to address the availability-commitment dichotomy in the design of business models for on-demand computing and IT outsourcing.

KEY WORDS AND PHRASES: computing marketplace, electronic auctions, grid computing, on-demand computing, utility computing.

## The Future of Information Technology: Computing as Utility?

BUSINESS COMPUTING HAS TRAVERSED several different architectures for deploying information technology (IT) applications, as exponential increases in capabilities and drastic reductions in cost have redefined the scope and efficacy of architectures. Starting with centralized mainframe computing, IT architectures progressed to decentralized islands of computing as desktop computers became highly affordable and powerful, and then—responding to the need for information sharing—to networked applications using client-server, n-tier, and Web computing architectures. Recently, communication speeds have become faster and bandwidth cheaper, so that a distributed grid computing architecture combines the benefits of centralization with the advantages of anywhere, anytime access. In the past two years, the IT industry has been abuzz with the idea that in the near future, IT computing will gravitate toward a “computing as utility” model, where, as indicated in a recent issue of the Economist (“The Future of Computing,” January 15, 2004, echoing similar arguments in June 2001 and May 2003):

Some day, firms will indeed stop maintaining huge, complex and expensive computer systems that often sit idle and cannot communicate with the computers of suppliers and customers. Instead, they will outsource their computing to specialists (IBM, HP, etc.) and pay for it as they use it, just as they now pay for their electricity, gas and water.

Management of ITs has become highly complex today. Consider one of the simplest areas, data storage. Firms today gather and maintain massive amounts of data, often measured in terabytes and petabytes. These are stored in various generations of storage media and may have to be maintained for several years due to legal, organizational, or other requirements. Access to data must be provided over a network, but it must be done securely and in a way that maintains data privacy and confidentiality. Data must be protected from failures, and recoverable in the event they do happen. For many firms, these data management requirements are highly complex and prohibitively expensive to satisfy. Such firms turn to specialist providers of data storage services, giving rise to an industry of storage providers that manage firms’ data and make the data accessible to the firm over a network [25]. This phenomenon and its underlying causes are consistent with the “computing as utility” idea [39].

The increasing maturity of network computing technologies enables the idea of “business computing as utility,” discussed variously under the concepts of on-demand computing, pay-per-use, and software as service [29]. The vision is that computing needs of business applications and corporate data centers would be addressed by drawing computational resources supplied by a combination of specialist service providers, enterprise resources, and small-scale opportunistic suppliers [36, 43]. Vendor firms in various sectors of the computing industry—IBM, Hewlett-Packard, Sun Microsystems, Computer Associates, EDS, EMC, Microsoft, and Oracle—have made significant research and development investments in utility computing and applications [19, 20]. See Appendix A for a discussion of the enabling technologies and application areas that motivate and are consistent with the utility computing idea. We discuss developments in areas that are widely predicted to be important to the future of business computing—grid computing technologies, the distribution of computational resources as utilities, and IT outsourcing.

Although the technological underpinnings of computing as utility appear to be well developed and have already been proven in both research and the real world, little work has been done with regard to the business and pricing models that would underlie this architecture. Widespread business application of the “business computing as utility” vision requires a pricing mechanism that is consistent with the business computing environment [8, 22, 35]. The industry press has largely suggested a “pay-asyou-go” model, where firms pay for just the capacity they use [18]. From the provider’s perspective, this is essentially a capacity reservation mechanism, where the provider must guarantee the desired capacity but where the client firm makes no commitment toward actual use. Hence this scheme assumes that unlimited computing power is always available, which would impose a significant cost on the resource providers. This may work in a managed hosting scenario with long-term contracts, where a resource provider would provide sufficient capacity to meet peak demand in the hopes of recovering costs over a long period. However, an element of risk-sharing may be required in many other business applications that involve opportunistic computing, are nonrecurring, and therefore are less predictable [5].

The “business computing as utility” scenario appears to be one with substantial demand uncertainty. Variance in computing needs is a key factor in the suggested move toward utility computing, and may occur due to internal variables such as sales, customer service queries, orders, and so on. Illustrative settings include advanced business applications, such as optimization problems; data mining; text or multimedia search and retrieval; and nonrecurring business computation, such as large database manipulations and queries for record matching over multiple databases. In such applications, both the timing and the quantity of computing resources required cannot be predicted with certainty. Hence the client firm’s computing demand is stochastic, involving uncertainty either about the quantity of resources required or whether these resources are needed (e.g., whether a computing project is on or off).

Given the high degree of uncertainty in demand for computing, it is unreasonable to assume that vast amounts of computational resources will be guaranteed, unless the client firm makes an advance reservation for capacity. Availability and commitment are thus dichotomous. Such applications cannot be addressed via a real-time spot market for computational resources due to setup requirements, such as data formats, security, and connectivity. Hence the framework we study for computing as utility is one where potential users make short-term capacity reservations as they become aware of possible demand.

In addition to uncertain demand, user firms may place different value on the computing resource, depending upon the intended application. Multiple firms may expect to draw on the same computational resources [19], and these firms differ in their valuations. We assume that prices of computational resources are discovered via an auction mechanism. This offers a superior way to balance supply and demand, compared with a posted price offered on a take-it-or-leave-it basis, especially given the heterogeneity in valuations and the uncertainty in demand realization. Industry experts predict that auctions will play an important role as a pricing and resource allocation mechanism in the computing as utility arena.

The two dimensions of demand—valuation and demand probability—are orthogonal to each other. Moreover, different utility computing markets may be characterized by different relatedness of valuation and demand probability. For instance, routine computing users may have low values and low demand uncertainty, whereas unpredictable critical applications have high values but incur high uncertainty. It is necessary for the provider to consider not only the extent of user firms’ demand uncertainty but also their valuations of the computing resource and the relationship between them. Specifically, this highlights the need to consider whether the performance of an allocation and pricing mechanism depends on high-value or low-value applications having greater uncertainty. For ease of reference, we present the definitions of some key terms in Table 1.

This paper investigates the dichotomous issues of availability and commitment in utility computing, and studies how pricing mechanisms relate to the availability-commitment tradeoff. We ask whether the computing resource provider is always better off requiring commitment from the user firm, or whether it might benefit by making sufficient resources available while giving the user flexibility in using and paying for these resources. We argue that the pricing scheme must specifically take into account the client firm’s demand uncertainties and examine the applicability and performance of alternative pricing models. We consider a setting where pay-per-use prices are discovered via competitive bidding in an auction, and propose and analyze a new form of auction—a contingent bid auction. In this format, the auctioneer (resource provider) announces a mechanism that includes a refund policy under which firms that win the auction, but realize a level of demand that is lower than the reserved quantity, are given a partial refund for unutilized capacity. We formally model the no-show option in the strategic bidding behavior of participants and analyze its implication on market outcomes. We consider markets in which buyers are heterogeneous on both their valuation and probability of demand. We model three different contingent bid auctions—the general case where a winning bidder is refunded a percentage of the winning price on being a no-show, and the two special cases where this percentage is 100 percent (we call this NC—a “no commitment” mechanism) or 0 percent (AC—an “advance commitment” mechanism). Using analytical models and computational study, we study the changes in prices, revenues, and utilizations under different mechanisms with different degrees of correlation between demand realization and valuation. After establishing some fundamental properties of optimal bidding strategies under the three mechanisms, we concentrate on discovering comparative properties of these three mechanisms under different market characterizations via computational experiments owing to the complexity of the resulting analytical formulation.

Table 1. Definitions of Key Terms

<table><tr><td>Term</td><td>Definition</td></tr><tr><td>Advance commitment (AC)</td><td>No-shows lose the full price; also called capacity reservation; refund rate is zero.</td></tr><tr><td>Availability</td><td>Measures whether the provider has enough computing resource to satisfy all user firms that demand it.</td></tr><tr><td>Commitment</td><td>Measures what the user firm loses when it does not use the prebooked computing resource.</td></tr><tr><td>Contingent bid auction</td><td>Auction in which user firms that win the auction and pay the winning price may choose not to consume the computing resource but still get a (partial) refund.</td></tr><tr><td>Demand realization</td><td>Probability that the user firm will use the computing resource.</td></tr><tr><td>No-show</td><td>Refers to user firms that win the auction but do not consume the computing resource.</td></tr><tr><td>No commitment (NC)</td><td>No-shows do not lose anything; also referred as pay-as-you-go (zero commitment; refund rate of one).</td></tr><tr><td>Partial commitment (PC)</td><td>No-shows lose a part of the price paid; receive a partial refund.</td></tr><tr><td>Value demand correlation</td><td>The relationship between user firms&#x27; value for the computing resource and demand realization.</td></tr><tr><td>Refund rate</td><td>The percentage of price refunded to no-shows.</td></tr></table>

## Pricing Models and Demand Uncertainty

AN IMPORTANT FACTOR IN THE IDEA of on-demand computing is the presence of substantial demand uncertainties when client firms reserve computational resources. As explained in the first section, advance reservations may be required to guarantee capacity and to deal with setup requirements, such as data formats, interoperability, access privileges, and security. Many forms of uncertainty have been analyzed in the literature. Uncertainty can occur in the quantity available or demanded, and mechanisms to deal with such uncertainty include quantity-flexible contracts [24, 27] and options. Uncertainty can also occur regarding the likelihood of arrival of a buyer or seller, or the likelihood of a “no-show” after a reservation—mechanisms for dealing with such uncertainty include revenue management [30] and contingent sales [9].

Finally, uncertainty may be about product or service quality—this is quite common for many digitizable information goods as well as traditional physical products. Quality uncertainty prior to purchase can have negative consequences, including an unwillingness to trade as well as inefficient prices and outcomes. Many mechanisms have been proposed, and some are in use, to deal with such uncertainty: money-back guarantees [21] and warranties [10] in the case of physical goods, and trial periods [40] and quality-contingent pricing [6] in the case of information goods.

The problems and mechanisms discussed above are studied in posted price settings, where the seller (firm) moves first in choosing and posting a price, and buyers follow with their purchase decision [33]. In many markets, however, prices are discovered via mechanisms such as auctions. The use of auctions has grown dramatically in the past several years along with the privatization and growth of the Internet [3]. For standard (noncontingent) auctions, the literature discusses various types of auction formats, including open versus sealed-bid auctions and single versus multiunit auctions (see Krishna [26] for an excellent introduction to auction theory). Important considerations in choosing an auction format are: efficiency (allocation of items to highest-value bidders); sellers’ revenue; and truth revelation (bidders bid true values). If the bidders’ valuation of the goods is private and is not affected by the process of bidding, then these auctions produce the same revenue and are also efficient [37, 46]. For the case of multiunit auctions, the major open-format auctions include the ascending price English auction, the descending price Dutch auction, and the Ausubel auction [2]. The sealed-bid multiunit auction formats include: discriminatory auctions, where every winner pays its bid amount; uniform price auctions, where every winner pays the highest losing bid; and the generalized Vickrey auction [45], where every winner, on winning k items, pays the highest k losing bids as the price for the k items. For multiunit auctions in which each bidder has unit demand (the case we consider in this paper), then uniform price and Vickrey auctions are identical. Specifically, if there are Q items to sell, every winner pays the (Q + 1)th highest bid (the highest losing bid). In Vickrey auctions, it is optimal for the bidders to bid their true values [45]. The auction is efficient and revenue maximizing as well.

The quality and quantity uncertainty problems prevalent in many posted-price settings also appear in many cases where prices are set via an auction. However, literature on the theory and practice of auctions does not offer systematic ways to incorporate such uncertainty in the price discovery process, beyond the bidders adjusting their bids for uncertainty and bearing the quality risk on winning the auction. The theories of options and real options contain features that are common with contingent bid auctions (see Dixit and Pindyck [13] for a systematic expositions of options theory, and Amram and Kulatilaka [1] for real options). The strike price bears resemblance to the winning price of the contingent bid auction, and the price of the option is the amount not refunded. However, there are some key differences. First, in contingent bid auctions, we have a limited capacity and finite number of bidders. Hence, the winning price in the auction is influenced by the individual bids and cannot be treated as the extraneous price movements of an underlying asset. Moreover, the contingency discussed in options literature is on the price of the underlying asset, whereas in our model, it is on the demand-realization, not on the winning price of the auction.

In this paper, we examine whether the essential principle behind contingency pricing—pay according to actual realization of quality, as agreed in a predefined contract—can be extended to the case where prices are discovered via auction. Specifically, we propose a setting where multiple buyers are contracting to reserve capacity offered by a single seller, when the buyers are uncertain about the quantity they will need. We study the special case where each bidder has unit demand, but at the time of bidding for capacity the buyer is uncertain about whether this demand will occur. Bidders have private information about the probability that demand will occur, and the actual realization is unobservable by the seller. This private information raises the need for a mechanism where bidders can be provided some incentive to reveal such information. Accordingly, we analyze the case where the seller chooses a contingent auction format for selling capacity, where bidders make contingent bids covering the two scenarios (demand realized or not). A buyer who wins in the auction and has a demand realization pays the winning price. But if a winning buyer becomes a “noshow,” he or she pays only a percentage of the winning price, as specified in the contingent auction mechanism.

## Modeling Contingent Bid Auctions

THE GENERAL PRICE DISCOVERY STRUCTURE we employ is a contingent bid auction. The “contingent bid” aspect of the auction means that the promise of payment, implied in a bid placement, is contingent on some factor. In the present analysis, the contingency is about the user firm’s demand realization. Specifically, if a winning bidder “reneges” (determines that he or she no longer needs the computational resource) he or she is partially relieved from the obligation to consume and pay for the resource. Provisions for “reneging” are evolving in some consumer Internet auctions, such as eBay.com; however, these are not systematically incorporated into the design and analysis of the auction. Our work formally introduces the possibility of reneging into the analysis of bidder behavior and auction design.

Formally, suppose that a seller has Q units of capacity to sell to N buyers $( N > Q )$ who have uncertain unit demand. Buyers bid to reserve a unit of capacity (computing resource) for use at a later time t. Buyer i has a probability $\theta _ { i }$ that he or she will in fact need this capacity at time t, and this probability is his or her private information. Whether or not the capacity is needed at time t is unobservable to the seller. The seller announces rules for computing winners and prices, as well as a refund rate m that establishes the extent of relief given to auction winners who fail to realize their demand. We analyze the role of refund rate by considering three special cases—two extreme cases with m = 1 and $m = 0 ,$ , and one with $m = { ^ { 1 } / 2 }$ . Table 2 summarizes the notation.

## Different Levels of Commitment

We consider two extremes with no commitment and full advance commitment, and a more general case of partial commitment.

Table 2: Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $i$ </td><td>index for firm  $i$ .</td></tr><tr><td> $m$ </td><td>Refund rate; also indexes the NC, AC, and PC mechanisms with  $m = 1$ , $m = 0$ ,  $m = 1/2$ , respectively.</td></tr><tr><td> $N$ </td><td>Total number of buyer firms.</td></tr><tr><td> $Q$ </td><td>Available units of computing capacity.</td></tr><tr><td> $\rho$ </td><td>Degree of correlation between valuation and demand realization probability.</td></tr><tr><td> $\hat{\rho}$ </td><td>Threshold value of correlation.</td></tr><tr><td> $B_{im}$ </td><td>The bid of user firm  $i$  under mechanism  $m$ .</td></tr><tr><td> $\theta_i$ </td><td>Demand realization probability for firm  $i$ .</td></tr><tr><td> $\hat{\theta}_i$ </td><td>Actual demand realization of firm  $i$  in the computational study.</td></tr><tr><td> $v_i$ </td><td>Valuation of firm  $i$  for the computational resource.</td></tr><tr><td> $P_m$ </td><td>Winning price under mechanism  $m$ .</td></tr><tr><td> $\pi_m$ </td><td>Profit under mechanism  $m$ .</td></tr><tr><td> $W_m$ </td><td>Set of winners under mechanism  $m$ .</td></tr></table>

• AC—Advance commitment mechanism $( m = 0 )$ : The winning price $P _ { 0 }$ is paid by all winners regardless of their actual demand realization. There is no refund for no-shows. This is the standard auction format studied in the literature and widely used in practice. Since buyers precommit, they bear all the risk of demand uncertainty, whereas the provider incurs no loss from no-shows.

• NC—No commitment mechanism $( m = 1 )$ : Auction winners pay a price $P _ { 1 } . \mathrm { A }$ winning buyer who reneges is given a full refund. This is the type of contract that seems to underlie nearly all discussions of computing as utility [5, 18]. Buyers bear no risk from demand uncertainty, whereas the provider incurs all the risk of no-shows.

• PC—Partial commitment mechanism $( m = 1 / 2 )$ : No-shows receive a partial refund $^ 1 / 2 P _ { _ { 1 / 2 } } .$ Here, the risk of demand uncertainty is shared between the buyer and the provider. If demand is not realized, buyers stand to lose the partial price $( 1 - 1 / 2 ) ^ { 1 } / 2 \mathrm { P } _ { 1 / 2 }$ that the provider retains.

## Winner and Price Determination

Since we wish to focus on comparing the three mechanisms (AC, NC, PC)—rather than study the underlying auctions themselves—we focus on the Vickrey auction with its desirable properties (discussed in the second section.). The sequence of events in our auction format is shown in Figure 1. First, the seller chooses a contingent bid mechanism (NC, AC, or PC with $m = 1 , 0 , 1 / 2$ , respectively) and announces quantity $Q .$ , mechanism m, and the winner and price determination rules. Winner determination is straightforward: the Q highest bidders win. The highest losing bid determines the price, hence each winner pays the (Q + 1)th highest bid. Let $P _ { m }$ denote the price under mechanism m. Buyer i places a bid $B _ { i m }$ under mechanism $m ,$ knowing that his or her likelihood of demand realization is θ. The seller announces the winners and price based on the auction rules. Winners then learn their actual demand realization (not observable to the seller) and inform the seller whether they wish to consume the reserved capacity or not. The seller refunds no-shows an amount $m P _ { m }$ . Hence, the buyer’s expected payment is $( 1 - m ( 1 - \theta ) ) P _ { { m } } ,$ , where $m = ( 1 , 0 , 1 / 2 )$ for NC, AC, and PC.

![](/api/attachments/CJQTU7CQ/fulltext/images/459e8ac677c262808ee140fdf0baaf7fddd1ae912a20861e66b510ef4a7b252f.jpg)  
Figure 1. Contingent Bid Auction Mechanism

## Bidder Behavior

There are N buyers, who are heterogeneous in both their valuation of the resource and the probability that they will need the resource. We characterize buyer i with a pair $( \nu _ { i } ,$ $\theta _ { i } )$ of random variables, where $\nu _ { i }$ denotes valuation and $\theta _ { i }$ is a probability.<sup>1</sup> The interpretation of bids and the equilibrium bidding strategy under each mechanism are stated below.

1. AC: Buyer i places a bid $B _ { i 0 } ,$ and pays $P _ { 0 }$ if she wins, independent of her actual utilization. Each bidder places a bid equal to her expected value, hence

$B _ { _ { i 0 } } = \theta _ { _ { i } } \nu _ { _ { i } }$ . This mechanism is closest in format to a traditional auction setting where the best bidding strategy is to bid the true value—true expected value in this scenario.

2. NC: Buyer i places a bid $B _ { i 1 }$ but pays the winning price $P _ { 1 }$ only if she chooses to consume. Because of this escape clause regarding payment, buyers bid their true value in equilibrium, $B _ { { } _ { i 1 } } = \nu _ { { } _ { i } }$ . This strategy is the same as in the standard Vickrey auction with no demand uncertainty.

3. PC: Buyer i bids $\mathbf { B } _ { i 1 / 2 } ,$ , and gets a refund $^ 1 / 2 \mathrm { P } _ { 1 / 2 }$ if she does not arrive. Following the reasoning in the above two cases, the optimal strategy is to bid expected value, $( \theta _ { \mathrm { i } } / ( 1 - ( 1 / 2 ) ( 1 - \theta _ { i } ) ) ) \nu _ { i }$

See Appendix B for a formal proof. Equation (B1) offers a generalized form of the bidding strategy across the three mechanisms.

## Seller’s Profit Under Different Mechanisms

The seller sorts the received bids and chooses the Q highest bidders as winners, with a price equal to the (Q + 1)th highest bid. Let $W _ { m }$ denote the set of winners under mechanism m. The actual profit is calculated by aggregating the revenues from all winners and subtracting the refund rate percent of the price from no-shows. The ex post actual profit expressions are developed in Appendix B. While these equations represent the actual profit, the seller, of course, must choose the mechanism ex ante. Hence the seller’s problem is to choose the mechanism that maximizes expected profits. We discuss the seller’s choice and the relative performance of different mechanisms in the next section.

## Analysis

THE SELLER’S EXPECTED PROFIT UNDER EACH MECHANISM is a function of the expected winning price, the expected demand realization among the winning bidders, and the level of commitment imposed under that mechanism. Given the demand uncertainty, it might seem that the seller should overbook capacity—and the overbooking levels might vary across the mechanisms—however, we do not consider this aspect because it is not consistent with a deterministic guarantee of resource availability. A related aspect is the salvage value of unused capacity, which we also ignore in the current analysis. These issues would be worthy of investigation in a more detailed study.

Returning to the computation of expected profits, the expected winning price $P _ { 1 }$ in the NC mechanism is simply the (Q + 1)th order statistic on the distribution of v. However, for the advanced and partial commitment cases, the winning price is an order statistic over a function that involves two random variables. Given the difficulty in analytically determining the winning price and expected demand realization for these cases, our analysis primarily focuses on discovering comparative properties across the three mechanisms via computational experiments.

## Research Questions

We recall that the bidder’s valuation and the probability of utilizing the resource are considered as joint random variates. The degree of correlation between the two is a characteristic of the particular market and may be unknown to the resource provider. In practice, markets for utility computing may have positive or negative correlation. For example, some applications may have high valuations and high variability (the SARS example discussed in Appendix A fits this case), while other routine applications may have low valuations and low variability. A market that combines these two applications will have an unknown degree of correlation. The resource provider must decide the auction format under such uncertainty. Hence our computational analysis seeks to understand the impact of correlation on the relative performance of different mechanisms.

We characterize the relation between user valuations and demand realization probabilities by the parameter ρ (a measure of correlation). Among the three mechanisms discussed in the third section, we are interested in understanding:

1. Which mechanism performs better? Intuitively, when the highest-valued consumers are the least likely to have a positive demand realization, the no commitment (pay-as-you-go) contract is likely to perform poorly, since the winner determination rule will select bidders with lowest probability of demand realization, resulting in low actual revenues. In order to analyze this relation systematically, we repeat our trials for various levels o $\dot { \boldsymbol { \rho } }$ (see the next subsection).

2. How does the price in the advance commit mechanism $( P _ { 0 } )$ change with the level of correlation between valuation and demand realization?

3. How do bidding strategy and ordering of bids change with varying levels of ρ?

4. How do prices and profits vary under different mechanisms, as customers tend to be clustered around high valuations versus being distributed in a wider (lower) range? This may represent different types of markets for computing—routine processing versus critical applications.

## Computational Study

Figure 2 depicts the design of the computational experiment. We start the simulation process with N bidders. To systematically study the effect of $\cdot _ { \rho , \cdot }$ we vary the degree of correlation from –1 to 1. For each correlation value, we conduct K trials. In each trial, the bidder valuations (v ) are drawn from a uniform distribution whose supports can vary between experiments. We compute the probability of demand realization $\theta _ { i }$ as $\theta _ { i } \equiv \theta ( \nu _ { i } ) = 1 / 2 - \rho ( 1 / 2 - \nu _ { i } )$ . The N bidders then place bids under each mechanism as given in Equation (B1) in Appendix B. The winning price is determined as the (Q + 1)th bid under each mechanism. We then draw M realizations of the demand for the N bidders. For each realization, we compute ex post the actual demand realizations, utilization, revenues, consumer surplus, and social welfare under each mechanism. In Appendix B, we provide the formulas for these calculations. We aggregate these outcomes over all realizations and over all trials. To minimize the variance in the outcomes and to help us study the factors of interest for each correlation value, we repeat the experiment with the same 200 trials of the same random draw of N bidder valuations.

![](/api/attachments/CJQTU7CQ/fulltext/images/3fcbaf5e178dfbdf791238c0fde908df5b4389dc66fc2df73540b0fc086e616b.jpg)  
Figure 2. Simulation Computational Design

We first compare the bids under the three different mechanisms. Equation (B1) and the definition of the $\theta _ { i }$ function lead to the following properties (see Appendix B for all proofs):

Proposition 1: Each player’s NC bid is highest, and AC bid is lowest, and the PC bid lies between the two.

Since the buyer bears the least risk in the NC mechanism, he or she bids the highest under it. Under AC, since the buyer bears all the risk, the bid is the lowest. We next study how the bids vary with users’ valuations under the different mechanisms. The outcomes for the NC mechanism are straightforward: since users bid their true valuations, the highest-value bidders bid higher than lower-value bidders. Under AC, since a player’s bid depends not only on valuation but also on the probability of demand realization, we are no longer guaranteed that high-value players will make higher bids under each mechanism. We prove that

Proposition 2:

1. Under the NC mechanism, high-value players bid higher than low-value players (formally, $\nu _ { j } > \nu _ { i } \Leftrightarrow B _ { j l } > B _ { i l } )$

![](/api/attachments/CJQTU7CQ/fulltext/images/6b9e8322a603cf3aba725d8569bdadd283aecbc4a9282a5556dbdc9e14d77004.jpg)

![](/api/attachments/CJQTU7CQ/fulltext/images/3ffa1b137fe4b85b25e8e934a15ea8d2b31cf1d87cc0fe65427c3fde8d23ea12.jpg)  
Figure 3. Bids Versus Valuation Under Positive and Negative Correlation Notes: Under positive value-demand correlation $( \rho = 0 . 6 )$ , bids increase monotonically with valuation. For high negative correlation $( \rho = - 0 . 6 )$ , under PC and AC, high-value users do not necessarily bid higher than low-value users, making it difficult to determine winners.

2. Under the AC mechanism, there exists a threshold $\hat { \rho } < 0$ such that high-value players bid higher than low-value players (formally, $\rho > \hat { \rho }  ( \nu _ { j } > \nu _ { i } \Leftrightarrow B _ { j l } >$ $B _ { i l } ) )$

3. Under the distributional specifications mentioned earlier in this section, the threshold occurs at a correlation value of one-third $( \hat { \rho } = - { I } / { 3 } )$

Figure 3 illustrates how the bids of users change with valuations under positive and negative correlation. When $\rho < \hat { \rho }$ [, then high-value players need not necessarily bid higher than low-value players, making it difficult to determine the winners.

For $\rho > \hat { \rho }$ , since the bids are monotonically increasing in valuations, Proposition 2 leads to the following interesting and important property.

Corollary 1: For al $| \rho > \hat { \rho } ,$ the winners under $N C , A C ,$ and PC mechanisms are identical. Hence the system utilization is also identical under the three mechanisms $f o r \rho > \hat { \rho } .$

Utilization rates under the different mechanisms will be identical when the winners are identical. Since the choice of winners is governed by their likelihood of demand realization, it is easy to understand the identical utilization result under positive correlation. However, this result also holds for negative $\rho \left( \rho \in \left[ - 1 / 3 , 0 \right] \right.$ in our specific setting), because the bids are monotonic in valuation in this range. As we show later, our computational study covers an interesting effect: the winners and utilization can be identical even when the bids are nonmonotonic in valuation, which happens for certain $\rho < \hat { \rho }$ . Note that even when the winners are identical, the revenues under the mechanisms may differ.

## Results

We begin our analysis of results with the prices achieved under different mechanisms when correlation levels vary. Figure 4 illustrates the price variations under the three different mechanisms. Under NC, prices remain unchanged. This is essentially because, when consumers do not have to commit to reserving capacity, it is optimal for them to bid their valuation quite independent of the demand realization probability. They pay no penalty for a no-show. Since the bidding strategy of users is independent of the demand realization distribution, the winning price remains the same. The AC mechanism yields the lowest prices, since the users incur all the risk and are not willing to bid high prices. They bid their expected values. Moreover, the expected values increase with correlation, so the resulting price also increases monotonically with correlation. As expected, PC prices remain between AC and NC prices, since the risk is shared between the users and provider. Hence,

![](/api/attachments/CJQTU7CQ/fulltext/images/7b3b080c3c04c6d68051763911a3a1dd1106e98683b173a68cf9406a5b887fca.jpg)  
Figure 4. Price Versus Correlation Under NC, AC, and PC Mechanisms Notes: Under NC, prices remain unchanged. The AC mechanism yields the lowest prices, since the users incur all the risk and are not willing to bid high prices. Prices under PC lie between AC and NC prices. Prices increase with correlation under AC and PC.

Finding 1: The AC mechanism yields the lowest prices, which increase monotonically with the degree of correlation between valuation and demand realization. Prices under the NC mechanism remain the highest and constant independent of correlation. Prices under PC lie in between AC and NC prices, and increase monotonically with correlation. Formally, $P _ { I }$ is constant over all , while $P _ { o }$ and $P _ { I / 2 }$ are increasing in . For all , $P _ { o } < P _ { I / 2 } < P _ { I } $

We next study the profits achieved under various mechanisms for different degrees of correlation, as illustrated in Figure 5. When valuations and demand realization are positively related—that is, higher-value consumers have a higher chance of realizing demand—the NC mechanism performs the best. This follows from two reasons: first, as we saw earlier, the prices are highest under NC, since users bid their true valuations; second, under positive correlation, the high-value bidders who win are more likely to realize demand, and hence the provider gets the higher revenues resulting from high prices and high utilization. The AC mechanism performs the poorest under positive correlation. The reasoning is similar to the NC case: high-value users who also have high expected values win; but the prices are lower, since users bid only expected valuations rather than true valuations. Hence revenues are lower for the provider than under NC. The PC mechanism, as expected, lies between the AC and NC cases. Hence,

![](/api/attachments/CJQTU7CQ/fulltext/images/400ab86dd93eabeaacd77410f35c654bae04ef9c449644856bca9a64d3f821dc.jpg)  
Figure 5. Revenue Versus Correlation Under NC, AC, and PC Mechanisms  
Notes: Under positive correlation, the NC mechanism yields the highest revenues, and AC yields the lowest revenues, vice versa under negative correlation. The revenues under all mechanisms monotonically increase with correlation.

Finding 2: Under positive (negative) correlation between valuation and demand realization, the NC mechanism yields the highest (lowest) revenues, and AC yields the lowest (highest) revenues. Revenues under the PC mechanism lie between the AC and NC revenues. $A t \rho = 0 ,$ , all the mechanisms yield the same revenue. The revenues under all mechanisms monotonically increase with correlation. Formally, $\pi _ { I } > \pi _ { O }$ when $\rho > 0 ,$ and $\pi _ { o } > \pi _ { I }$ when $\rho < 0 . \pi _ { 0 } , \pi _ { I } ,$ and $\pi _ { I / 2 }$ increase with $\rho .$

How does the choice of winners and system utilization differ between the mechanisms, and vary with correlation? Corollary 1 proved that the three mechanisms are identical with respect to winners and utilization for $\rho > \hat { \rho } = - 1 / 3$ . However, our computational analysis uncovered an interesting finding that this result holds even for certain $\rho < \hat { \rho }$ . It is puzzling that the winners are identical under the three mechanisms in spite of an important difference between them: high-value players make lower bids than low-value players in the AC and PC mechanisms. Figure 6 explains the result. Consider a shift in ρ from –0.6 to –0.4: we see that even though the ranking of bidders changes, the set of winning bidders is identical, hence utilization remains the same.

Figure 7 indicates that for very large negative correlations $( \rho < \hat { \rho } )$ , the NC mechanism delivers the lowest utilization, because the chosen winners—high-value users—have the lowest demand realizations. The AC mechanism performs better, since it chooses users with moderate valuations, hence better demand realizations. The difference in utilization between the mechanisms is largest at the maximum negative correlation value and gradually diminishes until all the three mechanisms look identical.

![](/api/attachments/CJQTU7CQ/fulltext/images/aa98e5fe6674c8eea231de5ebfbe0f01b65b5cb8d0514bb9c4452986e93c5e6a.jpg)  
Figure 6. Bids Versus Valuation Under Different Correlations  
Notes: The thicker parts of curves for $\rho = - 0 . 4$ and $\rho = - 0 . 6$ indicate identical winners, even though the rankings of the winners are different.  
Utilization vs. Correlation

![](/api/attachments/CJQTU7CQ/fulltext/images/dd7e129c1ea6781d9b7b48c3ad916e0b706f9f819fa2dd23ae2d52f2c6babc9c.jpg)  
Figure 7. Utilization Versus Correlation Under NC, AC, and PC Mechanisms Notes: Utilizations for the three mechanisms remain identical beyond a negative threshold value of correlation, indicating that the winners are identical.

We study consumer surplus and social welfare next (please refer to Figures 8 and 9, respectively). Under negative correlation, NC delivers the highest consumer surplus, as consumers do not incur any of the risk of demand realization, and AC delivers the least consumer surplus, as the users bear all the risk. Under positive correlation, the effect is reversed, because under NC, prices are higher, and hence consumer surplus

Consumer Surplus vs. Correlation  
![](/api/attachments/CJQTU7CQ/fulltext/images/8c43fe610813654d84e6c4546af0ed0045435473425f52d9992e2ca66389a4d8.jpg)  
Figure 8. Consumer Surplus Versus Correlation Under NC, AC, and PC Mechanisms Notes: Under negative correlation, NC delivers the highest consumer surplus, as consumers do not incur any of the risk of demand realization, and AC delivers the least consumer surplus, as the users bear all the risk. Results reverse under positive correlation.

## Social Welfare vs. Correlation

![](/api/attachments/CJQTU7CQ/fulltext/images/9b4943b79ec8e94e7a96a59f68f9bf03e7e2caebf4812ee6b350ef3f7eac330e.jpg)  
Figure 9. Social Welfare Versus Correlation Under NC, AC, and PC Mechanisms Notes: The three mechanisms perform similarly from a social welfare perspective beyond the threshold value of correlation.

remains the lowest. Recalling Finding 2, it is clear that consumer surplus trends are the opposite of revenue trends. It is unclear which of these effects will dominate in determining social welfare. It turns out that

Finding 3: The three mechanisms perform similarly from a social welfare perspective for all  > [. When  < [, NC delivers the lowest social welfare while AC delivers the highest social welfare.

![](/api/attachments/CJQTU7CQ/fulltext/images/faffc23ff688e180589153ba38c5d0ade4857e1b465499b79674c2dbe99d9bcc.jpg)  
Figure 10. Revenue with Low Customer Valuations Under High Negative Correlation Notes: As users are clustered more around higher valuations, but demand realizations are highly negatively correlated, revenues fall under the NC mechanism.

Beyond $\hat { \rho } ,$ , the winners and utilization are identical for all mechanisms as stated in Corollary 1, hence social welfare also remains the same.

Now we consider how revenues change when the customer valuations become more concentrated. We accomplish this by changing the lower support of the uniform distribution of customer valuations. Figure 10 displays the changes in revenues as the support is varied from 0 to 0.6 for $\rho = - 0 . 9$ . The higher end of the support for valuations is maintained at 1.

Finding 4: Despite the clustering of users around higher valuations, revenues fall under the NC mechanism when valuations and demand realizations are highly negatively correlated.

As users are clustered more around higher valuations, but demand realizations are negatively correlated, two effects determine how the NC mechanism performs. It is true that, on average, the bids are higher and prices are higher, and we should expect higher revenues. But, lower demand realizations tend to drive down the revenues. Hence, under high enough negative correlations, the total revenue falls, with increasing clustering of users toward higher values. The AC and PC mechanisms do not exhibit this effect. Beyond a threshold value of correlation, all the mechanisms show increased profits as users’ valuations increase.

## Discussion and Managerial Implications

THE SUCCESSFUL INTRODUCTION OF THESE new computing models requires development of appropriate pricing mechanisms and an understanding of the critical economic issues. Our research raises many important implications for practicing managers.

First, the use of auctions, especially contingent bid auctions, is well suited for addressing the challenges of computing as utility paradigm. Second, our framework provides a means of understanding the tradeoffs between availability, commitment, and pricing in the context of different markets for computing as utility—a clear understanding of this is essential for successfully managing IT resources in the future both as a provider and as a user of these resources. Third, our model also helps to understand the current evolution and future trajectory of business models of computing as utility. We discuss these issues in more detail below.

Computing as utility is expected to become widely prevalent in the future, and many types of pricing models will also emerge, including long-term contracts. But many applications of computing as utility cannot be addressed via a real-time spot market for computational resources due to setup requirements such as data formats, security, and connectivity. As we have argued, uncertainty about the future requirements of computing characterizes many of these applications. Hence, users will make short-term capacity reservations as they become aware of possible demand. Valuations of the computing resource will also vary across different user firms. Since unlimited computing capacity cannot be assumed, the auction mechanisms efficiently allocate the limited computing resources efficiently in an environment of private information to the users who value the resource highly. Under demand uncertainty, contingent bid auctions, used appropriately, increase the efficiency of allocation.

Providers of computing resources need to carefully weigh the availability, commitment, and pricing tradeoffs. Understanding how much capacity to make available, how much commitment to demand from user firms, and how profits change for different market conditions are crucial to good management of utility computing resources. We show how different mechanisms, ranging from full advance commitment to no commitment, provide different levels of utilization and availability of computing resources and resulting prices and profits. With a good understanding of the market in terms of valuation, demand uncertainty, and their correlation, and the salvage value of unused capacity, managers can use our framework to tune the refund rate m and understand its impact in achieving the desired level of capacity, utilization, and profits.

Our pricing framework can also be used to understand the trajectory of business computing pricing models. For instance, we relate “pay-as-you-go” pricing to a “no commitment” mechanism and demonstrate that it does not always work well. Why, then, are many providers, such as IBM and Hewlett-Packard, proposing these pricing models? To understand this, we consider the typical diffusion curve for new technology as illustrated in Figure 11. In the introductory period of a new technology, when adoption rates are low and early innovators try out the product, providers need to convince the users of the value of the new technology. So the providers extend the pay-as-you-go model and offer to absorb all the risk themselves to induce users to try the technology risk free. When utility computing technology really matures, when users better understand the value of the technology and uncertainty about demand, the “capacity reservation” model corresponding to the “advance commitment” mechanism in which users bear all the risk is preferred both by users and providers and may become the dominant pricing model. In the intermediate maturing years of utility computing, the “partial commitment” mechanism that shares the risk between providers and users emerges as the suitable pricing model.

![](/api/attachments/CJQTU7CQ/fulltext/images/89c1b03e9fb6e476537cdbe08e9a53a85570719a9fcfc4fe25c34ab9b4a9297a.jpg)  
Figure 11. Pricing Mechanism as Utility Computing Technology Matures

The emergence of new intermediaries for computing resource, such as Entropia, and increased intensity of IT outsourcing highlight the importance of research that carefully captures the intricacies of pricing under demand uncertainty.

## Conclusion and Future Work

THE IT INDUSTRY HAS MADE SUBSTANTIAL FINANCIAL investments in the belief that a “computing as utility” paradigm will exist in the future of business computing. Advances in grid and network computing architectures enable IT services such as ondemand computing and IT outsourcing. The successful introduction of these new computing models requires development of appropriate pricing mechanisms and an understanding of the critical economic issues. In this paper, we argue that the pay-asyou-go model for pricing utility computing raises dichotomous issues of availability and demand commitment. We introduce the notion of contingent auctions as a way to discover prices for utility computing, and examine the economic outcomes that are generated by various contingent auction mechanisms. It is useful for practicing managers to understand the markets—specifically, the relation between valuations and demand realization—under which these pricing schemes can be profitably employed.

We propose to address some limitations of our current model and continue our investigations in different directions. Our analysis is carried out under the assumption of risk-neutral participants. The PC mechanism, although never the best in terms of revenues or utilizations, performs consistently under all ranges of correlations and exhibits lower variance in the outcomes. If the provider does not have sufficient information about the market, and is betting on the NC or AC mechanism, a mismatched mechanism may produce considerable variance in the profits. Hence, under risk aversion, the performance of the PC mechanism may exceed both the NC and AC mechanisms. We propose to extend our analysis by characterizing the risk associated with the mechanisms in a systematic fashion. A related line of investigation studies the value of information in understanding the customer segments. For example, the provider may wish to sample the user population to understand the joint distribution of valuations and demand realizations.

We are currently analyzing the case where the provider gives the option to the users to bid using any of the mechanisms. It is clear that different customers, depending upon their valuations, will prefer different mechanisms under different degrees of correlation. While the auction literature discusses information revelation about valuations, and marketing literature examines segmentation based on customer valuations, we expect to show that a well-designed menu of contingent auction mechanisms can induce customers to reveal information not only about their valuations but also about their demand realization probabilities. We are also studying the impact of spot markets on contingent auctions by varying the reservation price of the provider via the salvage value of unutilized computing capacity. This also opens up the inquiry toward overbooking of capacity by the provider.

Acknowledgments: The authors thank the guest editors and referees for the JMIS special issue—their comments and suggestions have substantially strengthened the paper. Shankar Sundaresan gratefully acknowledges the eBusiness Research Center at Pennsylvania State University and the IBM Faculty Fellowship for research support.

## NOTE

1. In the general case not modeled here, θ would be the mean of a probability distribution.

## REFERENCES

1. Amram, M., and Kulatilaka, N. Real Options: Managing Strategic Investment in an Uncertain World. Boston: Harvard Business School Press, 1999.

2. Ausubel, L.M. An efficient ascending-bid auction for multiple objects. Working Paper 97–06, University of Maryland, College Park, June 1997.

3. Bapna, R.; Goes, P.; and Gupta, A. Insights and analysis of online auctions. Communications of the ACM, 44, 11 (2001), 42–50.

4. Baratloo, A.; Dasgupta, P.; Karamcheti, V.; and Kedem, Z.M. Metacomputing with MILAN. In V. Prasanna (ed.), Proceedings of the Eighth Heterogeneous Computing Workshop. Los Alamitos, CA: IEEE Computer Society Press, April 1999, pp. 169–183 (available at csdl.computer.org/comp/proceedings/hcw/1999/0107/00/0107toc.htm).

5. Bednarz, A. IBM touts on-demand computing. Network World, 19, 44 (November 4, 2002), 8.

6. Bhargava, H.K., and Sundaresan, S. Contingency pricing for information goods and services under industry-wide performance standard. Journal of Management Information Systems, 20, 2 (Fall 2003), 113–136.

7. Bhargava, H.K.; Krishnan, R.; and Müller, R. Decision support on demand: Emerging electronic markets for decision technologies. Decision Support Systems, 19, 3 (1997), 193–214.

8. Bichler, M.; Kalagnanam, J.; Katircioglu, K.; King, A.J.; Lawrence, R.D.; Lee, H.S.; Lin, G.Y.; and Lu, Y. Applications of flexible pricing in business-to-business electronic commerce. IBM Systems Journal, 41, 2 (2002), 287–302.

9. Biyalogorsky, E., and Gerstner, E. Contingent pricing to reduce price risks. Marketing Science, 23, 1 (2004), 146–155.

10. Boom, A. Product risk sharing by warranties in a monopoly market with risk-averse consumers. Journal of Economic Behavior & Organization, 33, 2 (January 1998), 241–258.

11. Czyzyk, J.; Owen, J.; and Wright, S.J. Optimization on the Internet. OR/MS Today, 24, 5 (1997), 48–51.

12. Deelman, E.; Kesselman, C.; Mehta, G.; Meshkat, L.; Pearlman, L.; Blackburn, K.; Ehrens, P.; Lazzarini, A.; Williams, R.; and Koranda, S. GriPhyN and LIGO, building a virtual data grid for gravitational wave scientists. In Proceedings of the Eleventh IEEE International Symposium on High Performance Distributed Computing. Los Alamitos, CA: IEEE Computer Society Press, 2002, pp. 225–234.

13. Dixit, A.K., and Pindyck, R.S. Investments Under Uncertainty. Princeton: Princeton University Press, 1994.

14. Foster, I. The grid: A new infrastructure for 21st century science. Physics Today, 55, 2 (2002), 42–47.

15. Foster, I., and Kesselman, C. Globus: A metacomputing infrastructure toolkit. International Journal of Supercomputer Applications and High Performance Computing, 11, 2 (Summer 1997), 115–128.

16. Foster, I., and Kesselman, C. The Globus project: A status report. Future Generation Computer Systems, 15, 5–6 (1999), 607–621.

17. Foster, I.; Kesselman, C.; and Tuecke, S. The anatomy of the grid: Enabling scalable virtual organizations. International Journal of Supercomputer Applications, 15, 3 (2001), 200–222.

18. Greenemeier, L. Pay as you go. InformationWeek, 878 (March 4, 2002), 22–25.

19. Greenemeier, L. Plugged in. InformationWeek, 899 (July 29, 2002), 30–36.

20. Gwynne, P. IBM girds for the grid. IEEE Spectrum, 38, 12 (December 2001), 24.

21. Heiman, A.; McWilliams, B.; and Zilberman, D. Demonstrations and money-back guarantees: Market mechanisms to reduce uncertainty. Journal of Business Research, 54, 1 (2001), 71–84.

22. Hoffman, T. HP takes new pricing path for utility-based computing. Computer World, 37, 21 (May 27, 2003), 1.

23. Hoschek, W.; Jaen-Martinez, J.; Samar, A.; Stockinger, H.; and Stockinger, K. Data management in an international data grid project. In R. Buyya and M. Baker (eds.), Proceedings of the First IEEE/ACM International Workshop on Grid Computing. New York: Springer-Verlag, 2000, 77–90.

24. Jeuland, A.P., and Shugan, S.M. Managing channel profits. Marketing Science, 2, 3 (1983), 239–272.

25. Kaplan, J.M. Outsourcing trends—A matter of perspective? Business Communications Review, 33, 8 (2003), 46–50.

26. Krishna, V. Auction Theory. New York: Academic Press, 2002.

27. Lee, H.L., and Rosenblatt, M.J. A generalized quantity discounting pricing model to increase supplier’s profits. Management Science, 32, 9 (1986), 1179–1187.

28. Litzkow, M.J.; Livny, M.; and Mutka, M.W. Condor—A hunter of idle workstations. Paper presented at the Eighth International Conference on Distributed Computing Systems conference, San Jose, CA, June 1988.

29. Marsan, C.D. Gauging the network effect of grids. Network World, 20, 17 (April 28, 2003), 21–22.

30. McGill, J.I., and Van Ryzin, G.J. Revenue management: Research overview and prospects. Transportation Science, 23, 2 (1999), 233–256.

31. Network World. Gateway to offer grid computing service with store PCs. Southborough, MA, December 10, 2002 (available at www.nwfusion.com/news/2002/1210gateway.html).

32. Network World. Grid technology helps fight SARS. Southborough, MA, May 26, 2003 (available at www.www.nwfusion.com/news/2003/0526sargrid.html).

33. Paleologo, G.A. Price-at-risk: A methodology for pricing utility computing services. IBM Systems Journal, 43, 1 (2004), 20–31.

34. Phillips, B. Have storage area networks come of age? IEEE Computer, 31, 7 (July 1998), 10–12.

35. Probst, M. Utility computing: Determining when the price is right. IT Journal, 1st quarter (April 28, 2002), 66–73.

36. Rappa, M.A. The utility business model and the future of computing services. IBM Systems Journal, 43, 1 (2004), 32–42.

37. Riley, J., and Samuelson, W. Optimal auctions. American Economic Review, 71, 3 (1981), 381–392.

38. Romberg, M. The UNICORE grid infrastructure. Scientific Programming, 10, 2 (2002), 149–157.

39. Ross, J.W., and Westerman, G. Preparing for utility computing: The role of IT architecture and relationship management. IBM Systems Journal, 43, 1 (2004), 5–19.

40. Shapiro, C., and Varian, H. Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business School Press, 1999.

41. Smarr, L., and Catlett, C.E. Metacomputing. Communications of the ACM, 35, 6 (June 1992), 44–52.

42. Survey: Computing power on tap. Economist, 359, 8227 (June 23 2001), 16–20.

43. Survey: Moving up the stack. Economist, 367, 8323 (May 10 2003), 6–9.

44. Tao, L. Shifting paradigms with the application service provider model. IEEE Computer, 34, 10 (October 2002), 32–39.

45. Vickrey, W. Counterspeculation, auctions and competitive sealed tenders. Journal of Finance, 16 (1961), 8–37.

46. Vickrey, W. Auctions and Bidding Games in Recent Advances in Game Theory. Princeton: Princeton University Press, 1962.

## Appendix A. Computing as Utility: Enabling Technologies and Applications

FOR MANY YEARS, RESEARCHERS IN SCIENTIFIC COMPUTING have pursued the idea of a distributed collection of advanced computational resources that would be available for sharing across a heterogeneous collection of access platforms (see, e.g., [41]). Advances in grid computing technologies have helped overcome technical challenges in achieving this vision, which involve providing acceptable performance on quality of service (QoS) metrics such as “common security semantics, distributed resource management performance, coordinated fail-over, [and] problem determination services” to a diverse set of applications and access platforms [17, p. 37; also see 14]. Several research initiatives have produced middleware solutions—such as the Globus Toolkit [15, 16], Computing Communities [4], and DataGrid [23]—which enable multiple processors and storage devices to compute in concert in a way that is seamless and transparent to users and application programs.

The earliest applications of grid computing technologies occurred in scientific computing. The GriPhyN project involves a computation grid for a consortium of physics projects [12]. The Earth System Grid enables climate simulation and analysis covering large time periods. The Unicore project, and its extension E-Grid, link various European supercomputing facilities to enable solving massive computational problems [38]. Similar initiatives are underway in other areas, such as earthquake simulation, which require massive computing power and data analysis [42].

Distributed computing technologies are being applied to business and societal applications as well. Several researchers have studied the use of distributed computing for providing access to management decision models and algorithms. These include the Condor project [28], the network-enabled optimization server NEOS [11], and the DecisionNet electronic market for decision computing technologies [7]. An intriguing example is the strategy by a leading personal computer reseller to make its thousands of computers, which sit idle in computer showrooms across the country, become part of a nationwide computational grid [31]. Similarly, individual households or office workers participating in a peer-to-peer model of computation can make idle computing power available to a computer grid that can run business applications, such as large data mining problems, for which the client firms need not make the large investments needed to provide dedicated computing power at peak demand. Existing projects include searching for extraterrestrial life (SETI@home), discovery of new drugs, and computations of population growth [42].

Several categories of business computing applications seem to fit the paradigm of computing as utility, especially under a “price discovery via auction” setting. This includes IT outsourcing settings such as application outsourcing [44], data storage outsourcing [34], and managed hosting [39]. Data storage seems especially suitable, owing to a high degree of standardization in storage specifications, high volatility in data requirements, and the fact that massive data sets can be partitioned into smaller units. For instance, EMC Corporation’s OpenScale service offers clients a capacityon-demand feature for storage capacity, SAN switch ports, NAS servers, and storage software. Another candidate class is business applications that generate sporadic or episodic demand for massive computation, such as data mining, managing major promotions and Internet-based advertising blitzes, and Web events that draw flash crowds. A notable recent example of opportunistic use of on-demand computing is the response to the SARS outbreak in Asia. In May 2003, researchers in Taiwan put together, over a few days, an “access grid” for storing massive amounts of x-ray data (3,000 patients, one x-ray per day for 30 days, at up to 20Mb per x-ray) and making these files available to doctors for remote viewing, diagnosis, and analysis [32]. Over time, we expect that the computing as utility paradigm would also involve more routine and predictable business computing applications.

## Bidding Strategy

LEMMA 1: THE EQUILIBRIUM BIDDING STRATEGY IS GENERALIZED AS

$$
B _ {i m} = \frac {\theta_ {i}}{1 - m (1 - \theta_ {i})} v _ {i}.\tag{B1}
$$

Proof:

1. AC: The mechanism is equivalent to the traditional Vickrey auction where, given the likelihood of demand realization, firm i’s valuation of the resource is its expected value $\theta _ { i } \nu _ { i } .$ . Hence firm i bids $B _ { i 0 } = \theta _ { i } \nu _ { i }$

2. NC: How do firms bid when they have no penalty for reneging? Given the standard Vickrey result, we know that all bidders will bid at least their true valuation. The concern is that bids will exceed valuation, in order to win, since actual realization is private information. One scenario is that all bidders bid very high, some win, and then no one emerges with their demand, leading in zero utilization, profit, and consumer surplus. We ignore this case of market failure, which can be prevented by imposing a small bidding cost. Then, assuming that other bidders do not overbid, consider the choices of bidder i. There are two scenarios:

a. Bidder i is not in the top Q but bids high enough to win. Then there are at least Q other bidders who will bid greater than or equal to $\nu _ { _ { ( Q ) } } ,$ the qth highest-order statistic, so the winning price is necessarily greater than $\nu _ { i }$ . Hence if bidder i wins, he or she will have to announce “no demand” regardless of $\widehat { \theta } _ { { } _ { i } }$ . This presents a lost opportunity.

b. Bidder i is in the top $Q$ valuations; then bidder i will win, and at a price below $\nu _ { i } ,$ whether or not he or she bids $\nu _ { i }$ or higher.

Since bidder i does not know in advance whether $\hat { \theta } _ { i }$ will be 0 or 1, bidding $\nu _ { i }$ is strictly superior to bidding higher than $\nu _ { i } ,$ which can result in a lost opportunity to realize a surplus.

3. PC: Since this mechanism combines the two extreme cases, the firms bid their expected value, $( \theta _ { i } / ( 1 - 1 / 2 ( 1 - \theta _ { i } ) ) ) \nu _ { i } \cdot \mathrm { Q . E . D }$

## Profit Under Different Mechanisms

The seller sorts the received bids and chooses the Q highest bidders as winners, with a price equal to the $( Q + 1$ )th highest bid. Let $W _ { m }$ denote the set of winners under mechanism m. The ex post actual profit

$$
\begin{array}{c} \pi_ {m} = P _ {m} Q - m P _ {m} \sum_ {i \in W _ {m}} (1 - \hat {\theta} _ {i}) \\ = P _ {m} \sum_ {i \in W _ {1}} (1 - m (1 - \hat {\theta} _ {i})), \end{array}
$$

where $\hat { \theta } _ { i } = 1$ if the winner i arrives, otherwise it is 0. Specifically, the profit under the three mechanisms can be written as

$$
\pi_ {1} = P _ {1} \sum_ {i \in W _ {1}} \hat {\theta} _ {i}\tag{B2}
$$

$$
\pi_ {0} = P _ {0} Q\tag{B3}
$$

$$
\pi_ {\frac {1}{2}} = P _ {\frac {1}{2}} \sum_ {i \in W \frac {1}{2}} \left(1 - \frac {1}{2} \left(1 - \hat {\theta} _ {i}\right)\right).\tag{B4}
$$

## Computational Study

For each realization, we compute ex post the actual demand realizations (the ${ \hat { \theta } } _ { i } \mathrm { s } )$ utilization $\boldsymbol { \mathbf { \hat { \theta } } } = ( \sum _ { W _ { m } } \hat { \theta } _ { i } )$ , revenues $\mathbf { \pi } = \left( \pi _ { m } \right)$ , consumer surplus $= ( \Sigma _ { W _ { m } } ( \nu _ { i } \hat { \theta } _ { i } - P _ { m } + m P _ { m } ( 1 -$ $\hat { \theta } _ { i } ) ) )$ , and social welfare = (profit + consumer surplus) under each mechanism. We aggregate these outcomes over all realizations and over all trials.

## Proof of Proposition 2

Proof: Combining the $\theta _ { \mathrm { i } }$ function with the bidding rule (Equation (B1))

$$
\theta (v) = \frac {1}{2} - \rho \left(\frac {1}{2} - v\right).
$$

Under AC, the bid function is $B = \theta \nu$ . Taking derivatives with v, we get

$$
B ^ {\prime} (v) = \theta + v \rho = \frac {1}{2} (1 - \rho) + 2 \rho v.
$$

This proves our claim: $B ^ { \prime } ( \nu ) > 0$ when $\rho > 0 .$

To show that this result holds true for certain $\rho { : \mathrm { A C } }$ bids are nonmonotonic when $\rho$ is negative, so it is sufficient to show that $\exists \nu _ { 0 }$ such that $B ^ { \prime } ( \nu ) < 0$ for $\nu < \nu _ { 0 }$ and $B ^ { \prime } ( \nu ) >$ 0 for $\nu > \nu _ { 0 } .$ . We see that $B ^ { \prime } ( \nu ) = 0$ for $\nu _ { 0 } = ( 1 - \rho ) / ( - 4 \rho )$ . Solving for the value of $\rho$ at which $\nu _ { 0 } = 1$ , we get $\hat { \rho } = ( - 1 / 3 ) . \mathrm { Q . E . D }$
