---
otero_id: 28670
otero_key: "9PUDTDX5"
title: "When Is More Merrier? A Cloud-Based Architecture to Procure Impressions from Multiple Ad Exchanges"
authors: "Leila Hosseini; Shaojie Tang; Vijay Mookerjee"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.1221"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# When Is More Merrier? A Cloud-Based Architecture to Procure Impressions from Multiple Ad Exchanges

Leila Hosseini,<sup>a</sup> Shaojie Tang,<sup>b</sup> Vijay Mookerjee<sup>b,</sup>\*

<sup>a</sup> Department of Decision & Information Sciences, C.T. Bauer College of Business, University of Houston, Houston, Texas 77204; <sup>b</sup> Department of Information Systems, The University of Texas at Dallas, Richardson, Texas 75080

Contact: lhosseini@uh.edu (LH); shaojie.tang@utdallas.edu, https://orcid.org/0000-0001-9261-5210 (ST); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: October 4, 2021 Revised: September 20, 2022 Accepted: October 12, 2022 Published Online in Articles in Advance: June 13, 2023

https://doi.org/10.1287/isre.2023.1221

Copyright: © 2023 INFORMS

Abstract. We consider an ad firm that acts on behalf of advertisers to execute mobile, in-app, ad campaigns. The firm commits to provide an advertiser a specified number of ad placements (impressions) on mobile apps, usually in a specified location, and within a spe cified time horizon. The supply for ad space arrives, in real time, in the form of bid requests from one or more mobile ad exchanges. The ad firm needs to bid on each impression in such a way that the goals of several ongoing campaigns are met at minimum cost. The ad firm needs to execute multiple campaigns simultaneously and get its supply (for ad space, or impressions) from multiple mobile ad exchanges. By working with more than one ad exchange, the direct cost of procuring the necessary impressions can be lowered. However, this lower cost needs to be balanced with the cost of the additional computing resources needed to work with multiple mobile ad exchanges and the (possible) extra cost of meeting the minimum spend (or participation fee) imposed by each ad exchange. Here, there are two key decisions that the firm needs to make. First, it needs to select the set of mobile ad exchanges to obtain its supply; each mobile ad exchange is characterized by specific supply uncertainties, location dependent bid curves, and a participation fee. Second, for each ad exchange and location, the ad firm needs to determine its bidding policy, that is, how much to bid for each bid request. We show that the proposed near-optimal bidding strategy, the strategy to bid at each exchange-location combination, is state independent. We first solve a general problem of selecting among multiple nonidentical ad exchanges. We next analyze the special case with identical mobile ad exchanges and show that, depending on the particular parameter setting, the near-optimal number of ad exchanges and the near-optimal bid amount can be weak complements or substitutes. Finally, we propose a cloud-based architecture to procure impressions where the ad firm uses a selective bidding strategy that can further lower procurement costs. The ideas of this paper are applied to a real problem and the savings from our approach (about 33% lower cost) are demonstrated.

History: Giri Kumar Tayi, Senior Editor; Martin Bichler, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2023.1221.

Keywords: mobile advertising • mobile ad exchanges • procurement cost • capacity cost • cloud computing

## 1. Introduction

The penetration of the Internet and the increasing popularity of digital platforms have led to the growth in the use of advertising on the Internet. Furthermore, advertising on mobile devices such as smartphones, tablets, and other hand-held media devices is a fast-growing segment in digital advertising. The mobile advertising’s share of the digital advertising market has increased from 47% in 2015 to 72% in 2020 (Pew Research Center 2021). Worldwide mobile advertising spending has risen from \$227 billion in 2020 to \$288 billion in 2021, marking a 26.6% increase in year-over-year growth (Statista 2022). The focus of the current research is on mobile advertising. Particularly, we deal with ads that are displayed on mobile applications (apps), such as an app for news, games, or weather. In-app advertising is the fastest growing form of mobile advertising, and it is expected that a total of \$201 billion to be spent on in-app advertising in 2022 (Oliver 2021).

## 1.1. Mobile Ad Ecosystem

In the mobile in-app ad ecosystem, there are advertisers on the demand side who pay to advertise their products or services. On the supply side are the publishers; mobile app owners that sell the space needed for the display of ads. In between these two, are intermediaries: publisher (or supply-side) agents and advertiser (or demand-side) agents. Supply-side agents are mobile ad exchanges (e.g., DoubleClick, Nexage, AppNexus) that help the app owners to monetize their ad space. Demand-side agents are ad firms (e.g., Cidewalk, ExactDrive, Sitescout) that contract with advertisers to execute ad campaigns: display a specified number of ads, in a specified set of geographic locations, during a given time horizon. The focus of this study is on ad firms. An ad firm usually works with multiple advertisers at the same time and could obtain its supply from one or more ad exchanges.

In an ad exchange, each opportunity to display an ad (an impression) is auctioned on a real-time basis. To work together effectively, an ad exchange and an ad firm require closely integrated systems. This is to ensure a low turnaround time between ad-requests from the publisher and the supply of the winning ad by the ad firm. To ensure serious participation, ad exchanges impose a participation fee on bidders (usually, ad firms) that requires them to keep their average spend in each period above a specific amount (Choi et al. 2020). The participation fee results in market frictions on the supply side of the industry. It reduces the number of ad exchanges that an ad firm can work with, thereby lowering the supply-side competition among ad exchanges to sell ad space.

The operational details of real-time bidding are depicted in Figure 1 available in Online Appendix F. When an end user of a mobile app opens an app, the appropriate ad exchange is notified. This ad exchange then sends a bid request to the various bidders that have accounts with the ad exchange. Each bidder sends a response, and a firstprice auction is conducted in which the ad of the highest bidder is displayed. All bidders are required to send a bidresponse for every bid request; a zero bid-response is allowed. However, this response must be received within some time limit (typically any response received after 100 milliseconds (ms) is ignored; Downey 2012, Provost et al. 2015, Choi et al. 2020). An ad exchange has the option to disable bidders with high timeout levels. This response time constraint also creates supply side frictions: To earn the right to work with an ad exchange, the ad firm must possess sufficient computing capacity to be able to respond to every bid request within some acceptable delay. Because the arrival of bid requests is stochastic, it is common to see ad firms use a cloud-based architecture to meet their (elastic) computing capacity needs. Response time constraints not only reduce the competition for ad space, they also benefit cloud providers.<sup>1</sup>

## 1.2. Real-Time Bidding Architecture

Real-time bidding (RTB) is a complex environment because ad firms need to handle the bid requests and send responses to the requests within approximately 100 ms. Therefore, the ad firms are required to use advanced technologies (often cloud-based) to participate in these auctions (Choi et al. 2020, Google Architecture Center 2020). An illustrative (cloud-based) architecture is provided in Figure 2 available in Online Appendix F.<sup>2</sup> Two considerations about the architecture are significant from a modeling perspective. First, the architecture is distributed to ensure that it scales well and to avoid single point failures. From a modeling perspective, this implies that the bidding algorithm running on a particular server must act more or less independently of its peers. Second, as the load on the system increases, the capacity is automatically adjusted so that the ad firm can respond to each bid request within an acceptable time limit. That is, despite randomness in the arrivals (of bid requests), the sojourn time (waiting time plus service time) can be assumed to be almost deterministic, designed in a manner to meet the response time requirements of the ad exchange.<sup>3</sup> From a modeling perspective, this implies that the capacity planning decision (number of servers to rent) can be ignored. It also implies that the capacity cost in a period (e.g., a week) is stochastic and depends on the number of bid requests processed (and hence the number of servers rented over time) during the period.

## 1.3. Motivation of Problem

This study focuses on a problem where an ad firm commits to fulfill the demand for impressions (ad spaces) required by a set of advertisers. The ad firm identifies opportunities (in real time) across different ad exchanges to procure ad spaces at the lowest cost (Sharma 2019, Choi et al. 2020, Breus 2021). The ad firm needs to determine the set of ad exchanges to procure the supply and determine how much to bid on supply provided by each ad exchange such that the expected total cost is minimized. Based on a search of background literature, minimizing cost while acquiring enough ad spaces for advertisers is the top initiative for ad firms (Grigas et al. 2017, Wang et al. 2017, Cidewalk 2019). Moreover, industry experts state that the ad firms are confused in the market because of the presence of a large number of ad exchanges. As an ad firm, it is diffi cult to choose the correct set of ad exchanges to work with so that advertiser demand can be met at minimum cost.

The problem faced by the ad firm is a complicated operational problem (Choi et al. 2020). In general, it is easy to see that there could be many feasible solutions to the problem (we show later that the problem is NP-hard) so find ing the best solution using an enumeration approach is not likely to work for most real-world problems. Thus, the ad firms need efficient procedures to find the set of ad exchanges to obtain the supply of ad space from so that advertiser requirements are met at minimum expected total cost. Typically, the approach taken in practice is to acquire the supply of ad space from a single ad exchange to meet the demand (Graham 2015, Cidewalk 2019). In this paper, we show an ad firm can sometimes benefit from obtaining supply of ad space from multiple ad exchanges instead of single ad exchange.

## 1.4. Problem Description

Consider a situation where an ad firm commits to advertisers to display a specified number of ads, in a specified set of geographic locations, during a given time horizon.

Given a set of available ad exchanges, the ad firm wishes to select a subset of ad exchanges to obtain the supply of ad space from so that the advertisers demand is met at minimum expected total cost. The ad firm’s expected total cost is the sum of two costs: (1) the expected procurement cost and (2) the expected capacity cost.

The expected procurement cost is defined as the maximum of two cost components: expected bidding cost and participation fee. The expected bidding cost that is the direct cost of winning the impressions needed to meet the delivery constraints of the on-going ad campaigns being managed by the firm. The expected bidding cost depends on the number of opportunities that arrive (bid requests) and the bidding policy used to win impressions. If more bid requests arrive, the expected bidding cost to win the same number of impressions can be reduced. This is because, on average, the same bid amount will win a higher number of impressions if there are more bidding opportunities. Thus, everything else held the same, a firm should expect to reduce its expected bidding cost by working with more ad exchanges. The caveat here is the presence of a participation fee (minimum average spend in a period) imposed by each ad exchange. If the participation fee imposed by an ad exchange is relatively high, it requires the ad firm to spend more at this ad exchange to respect this constraint. In this case, the firm may be better off working without this ad exchange. Thus, adding a new ad exchange could increase or reduce the expected procurement cost, depending on the participation fee imposed by this ad exchange. On the other hand, the expected capacity cost always increases with each additional ad exchange because more bid requests need to be processed.

From above explanation, the ad firm faces a tradeoff between the expected bidding cost, participation fee, and capacity cost. Working with multiple ad exchanges is beneficial if the saving in expected bidding cost exceeds the extra participation cost and capacity cost; otherwise, it is better to work with a single ad exchange. Therefore, in practice, ad firms must balance the procurement cost and the capacity cost to minimize the expected total cost of acquiring the supply of the ad space: (1) the set of ad exchanges to obtain its supply from, and (2) the bidding policy used for each ad exchange at each location.

## 1.5. Contributions and Key Results

We first analyze the previous procurement model and propose a near-optimal bidding policy, the strategy to bid at each exchange-location combination, and provide a theoretical worst-case performance guarantee for our proposed bidding policy. An important feature of our proposed bidding policy is that it is state independent (Proposition 1). That is, the ad firm need not consider the states of the on-going campaigns (e.g., the number of impressions won so far, the time left in the horizon) in its bidding policy. This is a particularly useful property when the bidding architecture is distributed. The state independent property allows the servers to bid independently of one another, without exchanging state information.

Having obtained a characterization of the near-optimal bidding policy for the problem, we next solve the ad exchange selection problem. The following results are obtained.

• We start by analyzing the ad exchange selection problem for the case where the ad exchanges are nonidentical and propose a heuristic algorithm. The solution proposed is near optimal and efficient and can be found in a few seconds for realistic-sized problems. We also provide a theoretical worst-case performance guarantee for our proposed solution and numerically study its computational performance and cost. To demonstrate the cost savings of our proposed solution, we use the cost of the best single ad exchange solution as a benchmark. Our computational results show that our near-optimal solution can generate substantial savings (around 25%) over the best single ad exchange solution. Here, we also provide some managerial insights into the characteristics of ad exchanges that are most suitable for a particular ad firm to work with.

• We further analyze the nonidentical ad exchanges case and illustrate for a given number of ad exchanges in the market, a more heterogeneous market (one in which the participation costs of the ad exchanges are different) leads to a higher total cost for a big ad firm, but a lower total cost for a small ad firm. Thus, big ad firms can hurt from the heterogeneity of ad exchanges. However, the heterogeneity can be a friend for small ad firms.

• We then examine a special case with identical ad exchanges. We show that all impressions arriving from the same location should be procured in the same cost (Proposition 2). Next, we propose a near-optimal solution for number of ad exchanges that the ad firm should use to obtain its supply. A theoretical performance guarantee is presented for the near-optimal solution.

• The identical ad exchanges case is further analyzed. First, we show when a new ad exchange enters the market, the ad firm and cloud provider could benefit, but the total revenue earned from the ad firm by the ad exchange market stays the same or reduces (Proposition 3). Next, we provide guidelines for cost-aware promotion decisions. Using this analysis, the ad firm can choose specific locations to increase advertising demand, such that the impressions needed to meet the extra demand can be obtained at relatively low cost. We also show when the demand at a particular location increases, the nearoptimal number of ad exchanges and the near-optimal bid amount can be weak complements or substitutes (Proposition 4).

• We introduce a new bidding strategy that incorporates the idea of a selective bidding strategy. This feature allows the ad firm to further reduce expected total cost (expected procurement cost plus expected capacity cost). The impact of a selective bidding strategy on ad firms, ad exchanges and cloud providers is analyzed under the special case of identical ad exchanges (Propositions 5 and 6).

• From a practical perspective, we find that the model can be applied to real-world situations with significant benefits. Interestingly, only a small change in the operating policy can lead to significant savings. For example, in the Cidewalk case presented in Section 6, a 33% savings was obtained by procuring impressions from one additional ad exchange and by filtering out (i.e., not bidding on) 10% of the arriving impressions.

This research contributes by providing a formal representation of a real-world problem encountered by ad firms. Our proposed solution is easy to implement in practice and it potentially provides huge efficiency gains for ad firms by lowering the expected total cost of acquiring the supply of ad space. By analyzing the tradeoff between the expected bidding cost, participation fee, and expected capacity cost, we show that it is beneficial for an ad firm to acquire the supply of ad space from multiple ad exchanges if the saving in the expected bidding cost compensates for the extra participation fee and expected capacity cost; otherwise, it is better to procure the supply from only one ad exchange. Therefore, our proposed approach in this paper is useful not only for the ad firms that are currently working with a single ad exchange but also those ones that are working with multiple ad exchanges.

For those ad firms that are currently working with a single ad exchange, they could consider a potential set of ad exchanges to use to reduce expected total cost. Near the end of this paper, in Section 6, we show that in the absence of formal analysis to guide ad exchange selection, a real-world ad firm called Cidewalk works with only one ad exchange. However, our proposed approach demonstrates that it can be better for Cidewalk to work with multiple ad exchanges. Our proposed approach in the paper provides a 33% reduction in the firm’s expected total cost over the current option of obtaining all the required supply of ad space from a single ad exchange. Ad firms currently working with multiple ad exchanges might find it beneficial to work with a single ad exchange or even work with a different set of ad exchanges. Therefore, either way, our paper makes an important contribution to industry practice.

## 1.6. Differences from Past Research

The key feature distinguishing this study from traditional procurement problems is the presence of supply uncertainty (the uncertainty in the availability of ad space). Another important distinguishing feature is that the supply of ad space is exogenous to the demand for ad space. In the classical procurement literature, supply uncertainty is often caused by random yields (Yano and

Lee 1995, Wang and Gerchak 1996). However, unlike the advertising world where end users do not open mobile apps to create ad space, supply in traditional literature usually occurs in response to demand. Thus, our problem is fundamentally different from the traditional literature on delivery commitments that arise to manage supply/demand uncertainty (Bapna et al. 2011, Asdemir et al. 2012, Du et al. 2012, Yuan et al. 2018). Furthermore, in the advertising world, the ad firm cannot inventory the supply of ad space. Chen et al. (2013) study a procurement problem with uncertain demand and a spot market for supply. However, besides the inability to store ad space, the network structure in our problem is more complicated. Our procurement problem is studied from the perspective of an ad firm that needs to bid in multiple spot markets (ad exchanges) of its choice while considering the computing cost of participating in these markets.

A related stream of literature is the work on locationbased advertising (LBA) on mobile devices (Luo et al. 2013, Fang et al. 2015, Sun et al. 2017). Balseiro et al. (2014) study the problem from a publisher’s perspective to determine the optimal allocation of impressions between contracted advertisers and ad exchanges. Our problem is studied from ad firm’s perspective, and the goal of the ad firm is to optimize both ad exchange selection and bidding strategy to minimize the expected total cost. Recently, Aseri et al. (2017) study the problem of ad firms that contract with advertisers to deliver ad campaigns with the goal of finding a bidding strategy that minimizes procurement cost. The problem studied in Aseri et al. (2017) is different from ours in two respects. First, they assume the mobile-promotion platform procures impressions from a single ad exchange, with no participation fee. Second, the capacity cost associated with a bidding strategy is ignored in their work. Under our setting, the ad firm must choose a set of ad exchanges to work with and pay a rental cost that depends on the total number of bid requests received in a period from this set of ad exchanges. Because the number of bid requests is random, the capacity cost during a period is also random.

We next provide a brief review of the relevant research from the computer science area. The first category of studies deal with designing contracts between publishers and advertisers (Babaioff et al. 2009). For example, Constantin et al. (2008) study the problem of designing mechanisms with strong game-theoretic properties from the perspective of the publisher. They assume advertisers arrive sequentially and bid on which slots that are of interest to them. The publisher must decide, in real time, whether to allocate a slot to a specific advertiser (Yang et al. 2016). Another stream of work focuses on optimiz ing the bidding strategy from the perspective of the advertiser. For instance, Ghosh et al. (2009) study adaptive bidding for display advertising, where the goal is to acquire a given number of impressions subject to a budget constraint. For additional material in the area of bidding strategies, we refer readers to the recent comprehensive survey by Korula et al. (2015).

Another stream of literature uses a game-theoretic approach to study real-time bidding in targeted online advertising (Sayedi 2018, Sayedi et al. 2018) and position auctions (Lu et al. 2015). For example, Sayedi (2018) uses game theory to study the impacts of real-time bidding on advertisers’ and publishers’ strategies and their profits. They show that real-time bidding can benefit both advertisers benefit and publishers. Lu et al. (2015) examines the case with the two budget-constrained advertisers that compete for two ad positions sold by a publisher. Their model is a simultaneous-move static game of complete information played by two advertisers. The study sheds light on the impact of the advertisers’ budget on their profits and the revenue of the publisher.

We conclude this review of past work by providing a brief description of studies that adopt dynamic bidding strategies. Here, one common objective of a budget constrained advertiser is to acquire as many clicks as possible during a real-time advertising campaign (Perlich et al. 2012, Zhang et al. 2014, Wu et al. 2017). Assuming that the click through rate of each impression can be estimated with reasonable accuracy, the advertiser should assign a greater bidding price to an impression with a higher click through rate to achieve a higher number of clicks (Lin et al. 2020). In another study using dynamic bidding (Lee et al. 2013), the arrival probability of an impression is assumed to vary with time. The goal is to dynamically adjust the bidding price to spend the budget smoothly over the time. This helps to reach a wider range of audience and have a sustainable impact.

Our work is different from previous studies in several important ways. First, we study the problem from the point of view of an ad firm that, in turn, represents several advertisers. Thus, there are many on-going advertising campaigns be managed and the ad firm needs to bid for impressions and allocate the impressions that are won across these on-going campaigns. Second, we examine new aspects of the cost, namely, the capacity cost and the participation cost of working with an ad exchange. To the best of our knowledge, no previous research in RTB considers the participation cost component. Choi et al. (2020) emphasize the importance of participation cost in RTB and point out the need for considering it based on the grounds that it can considerably affect an ad firm’s bidding decision. Third, because we solve the problem from the perspective of the ad firm, there is no budget constraint in our study. Instead, we have a delivery constraint. Therefore, the focus of our study is entirely different from previous work. Finally, most existing studies assume that the ad firm procures the supply of ad space from a single ad exchange and ignores the ad exchange selection problem. In our study, we jointly optimize ad exchange selection and the bidding strategy. To our knowledge, this joint problem has not been studied earlier. We next present the model.

## 2. Model Preliminaries and Formulation The ad firm makes two decisions as described here.

• Ad exchange selection: The ad firm selects the set of ad exchanges to obtain its supply from to meet the requirements of various campaigns.

• Bidding policy: This is the strategy used to respond to bid requests. These requests arrive randomly from different ad exchanges and locations. The response to a request consists of a bid amount. This is equivalent to choosing a win probability; the bid amount and the win probability are related to one another via the bid-curve; and the bid amount needed to win an impression with the win probability.

Table 1 summarizes the main notation in this study. Before formulating the model, we discuss some basic definitions and assumptions.

1. Let $\mathcal { R } = \{ 1 , 2 , \ldots , R \}$ denote the set of all locations. The ad firm’s commitment is to procure, within a given time horizon (e.g., a week or a month), at least $\xi _ { r }$ impressions on mobile apps in location $r \in \mathcal { R }$ with a probability of $\beta$ or more (a typical value of $\beta$ could be 0.99, i.e., 99%). Clearly, $\xi _ { r } \geq 0 , r \in \mathcal { R }$ . It is notable that the ad firms such as Cidewalk, GroundTruth, Taboola, AdButler, and ExactDrive<sup>4</sup> implement the same type of commitment.<sup>5</sup>

2. Let $\Omega = \{ 1 , 2 , \dots , N \}$ denote the set of potential ad exchanges. Bid requests arrive from one or more ad exchanges for a location $r \in \mathcal { R }$ and must be responded to by the ad firm.

3. In practice, ad exchanges usually require the addelivery firms to commit for a minimum ad spend, referred to as a participation fee (Kreuger 2019). It is notable that ad exchanges such as Xandr, OpenX, MoPub, and Marine Ad Network impose this requirement.<sup>6</sup> We consider there is participation fee $C _ { i }$ for participating in the auction process held by ad exchange i.

4. For $r \in \mathcal { R } ,$ , let $p _ { i , r }$ denote the probability that an impression from location r arrives in a time slot via ad exchange i. The total number of impressions arriving via the subset of the nonidentical ad exchanges, $W \subseteq \Omega ,$ over the $T$ time-slots is a random variable, $K _ { W } ,$ following a binomial distribution with a trial success proba bility of $\begin{array} { r } { \sum _ { i \in W } \sum _ { r \in \mathcal { R } } p _ { i , r } \leq 1 } \end{array}$

5. The arriving impressions are auctioned in realtime on each ad exchange. The ad firms need to bid for the impressions. The ad firm with the highest bid wins the impression and needs to pay the amount that she bids to the ad exchange. Clearly, the higher the bid, the greater the probability of winning an impression. To model this, following previous literature (Gummadi et al. 2011, Iyer et al. 2014, Balseiro et al. 2015, Balseiro and Candogan 2017, Balseiro and Gur 2019), we consider that the ad firm can calculate the probability of winning an impression for a specified bid amount. Here, we model the probability of winning an impression for a specific bid using a win-curve, which is a function $q _ { i , r } ( \psi ) \hat { : } [ 0 , \psi _ { i , r } ^ { m a x } ] \longrightarrow [ \bar { 0 , } 1 ] , i \in \Omega$ and location $r \in \mathcal { R }$ The win-curve $q _ { i , r } ( \psi )$ determines the probability of winning an impression arriving from location r via ad exchange i by bidding an amount ψ. We define the bidcurve $\bar { \psi _ { i , r } } ( y ) : [ 0 , 1 ]  [ 0 , \psi _ { i , r } ^ { m a x } ] , i \in \Omega$ and $r \in \mathcal { R } ,$ , as the inverse of the function $q _ { i , r } ( . ) ;$ that is, $\psi _ { i , r } ( y ) = q _ { i , r } ^ { - 1 } ( y )$ Thus, $\psi _ { i , r } ( y )$ is the bid required to win impression arriving from location r via ad exchange i with probability of y. Figure 3(a) available in Online Appendix F illustrates the concept of win-curve visually. As shown in Figure 3(a) available in Online Appendix ${ \mathrm { F } } ,$ if the ad firm picks bid price \$0, it wins the impression arriving from location r via ad exchange i with probability of zero. If the ad firm increases the bid price, the winning probability of the impression increases as well till the bid price reaches to maximum bid amount which guarantees the win probability of one.

Table 1. Main Notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td>i</td><td>Ad exchange index</td></tr><tr><td>t</td><td>Time slot index</td></tr><tr><td>r</td><td>Location index</td></tr><tr><td>Ω</td><td>Set of potential ad exchanges</td></tr><tr><td>W</td><td>Subset of ad exchanges, W⊆Ω</td></tr><tr><td>R</td><td>Set of locations</td></tr><tr><td>T</td><td>Time duration of campaigns</td></tr><tr><td>pi,r</td><td>Arrival probability of an impression from location r via the ad exchange i; i∈Ω, r∈R</td></tr><tr><td>Ci</td><td>Participation fee of ad exchange i; i∈Ω</td></tr><tr><td>ξr</td><td>The demand at location r; r∈R</td></tr><tr><td>qi,r(ψ)</td><td>Win-curve—Probability of winning an impression arriving from location r via mobile ad exchange i by bidding an amount ψ; i∈Ω, r∈R</td></tr><tr><td>ψi,r(y)</td><td>Bid-curve—Inverse of the function qi,r(.), the bid amount needed to win an impression arriving from location r via ad exchange i with probability y; i∈Ω, r∈R</td></tr><tr><td>hi,r(y)</td><td>The expected cost associated with choosing a win probability of y for an impression arriving from location r via ad exchange i; i∈Ω, r∈R.</td></tr><tr><td>g(K)</td><td>The cost of renting VM instances to respond to K bid requests in a desired time limit.</td></tr></table>

6. We use T to denote the number of time slots in a planning horizon. By a time slot, we mean a sufficiently small interval of time in which the probability of more than one impression arriving from any locations via any of the ad exchanges is zero; for example, a time slot could be a few milliseconds or an even smaller unit of time, if necessary.

7. Let $g ( K _ { W } )$ denote the cost of the capacity needed to respond to the traffic $K _ { W }$ in an acceptable time limit. For example, it could correspond to the cost of renting capacity from a cloud provider such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud, and so on. The greater the traffic of impressions, the greater the need for computing resources to enable the ad firm to calculate bid amounts for the arriving traffic in an acceptable time limit. Previous studies have observed that the computing performance of a computing resource is increasing and concave in its characteristics (CPU, memory, storage, etc.; Dongarra 1992, Mao and Humphrey 2011, Juve et al. 2012). In addition, there is an increasing and linear relationship between the characteristics and unit-time rental cost of computing resources offered by cloud computing providers. Therefore, the unit-time rental cost of a resource is increasing and convex in its the computing performance. Hence, it is reasonable to assume that the function $g ( K _ { W } )$ is increasing and convex in $K _ { W }$ (Hosseini et al. 2020).

8. We define $h _ { i , r } ( y ) = y \psi _ { i , r } ( y )$ as the expected cost associated with choosing a win probability of y for an impression arriving from location r via ad exchange i. We assume function $h _ { i , r } ( y )$ is strictly increasing and convex in $y .$ This is a reasonable assumption and has been verified in prior research (Zhang et al. 2014, Aser et al. 2017). In Section $^ { 6 , }$ we also validate this assumption using data obtained from a real-world ad firm. Figure 3(b) available in Online Appendix F demonstrates the expected bidding cost visually. As illustrated in Figure 3(b) available in Online Appendix ${ \mathrm { F } } ,$ when the ad firm decides to win an impression with probability of zero, it needs to pay bid price of zero for the arriving impression, resulting in expected bidding cost $h _ { i , r } ( 0 ) \bar { = } 0$ . As the ad firm chooses the higher winning probability, it needs to bid a higher bid price, resulting in a higher expected bidding cost. If the ad firm decides to win the arriving impression with prob ability of one, it needs to choose the highest possible bid price, resulting in the maximum expected bidding cost $\mathsf { \bar { \boldsymbol { h } } } _ { i , r } ( 1 ) = 1 * \boldsymbol { \psi } _ { i , r } ( 1 ) = \boldsymbol { \psi } _ { i , r } ^ { m a x }$

We define $S _ { r , t }$ as a random variable representing the number of impressions won over the first t� 1 time slots from location $r \in \mathcal { R }$ . Let S be the matrix with ele ments $S _ { r , t } , r \in \mathcal { R } , t = 1 , 2 , . . . , T + 1$ . Let $\mathbf { S } _ { t }$ be the vector representing the tth column of the matrix S. Thus, if $\mathbf { S } _ { t }$ takes the value $\mathbf { s } _ { t } ,$ then $\left( t , \mathbf { s } _ { t } \right)$ represents the state of the ad firm’s procurement process. When the ad firm obtains its supply from subset of nonidentical ad exchanges, W, a bidding policy, π(W), for the ad firm is defined through the following function:

$$
\left\{ \begin{array}{l} y _ {t, i, r} ^ {\pi (W)} (t, \mathbf {s} _ {t} ^ {\pi (W)}) \text {: Probability of winning an impression} \\ \qquad \qquad \qquad \text { arriving from location } r \text { via the ad - } \\ \qquad \qquad \qquad \text { exchange } i \text { in time slot } t \text { under } \\ \qquad \qquad \qquad \text { state } (t, \mathbf {s} _ {t} ^ {\pi (W)}) \text { when the ad - firm obtains } \\ \qquad \qquad \qquad \text { its supply from subset of ad - exchanges } \\ \qquad \qquad \qquad W; 0 \leq y _ {t, i, r} ^ {\pi (W)} (t, \mathbf {s} _ {t} ^ {\pi (W)}) \leq 1. \end{array} \right.
$$

Under a given policy $\pi ( W )$ , the stochastic process $\{ \mathbf { S } _ { t } ^ { \pi ( W ) }$ $t \in \{ 1 , 2 , . . . , T + 1 \} \}$ evolves as follows: If an impression arrives from location r via the ad exchange i at time slot t, and the ad firm’s bid corresponding to the winning probability of $: y _ { t , i , r } ^ { \pi ( W ) } ( t , \mathbf { s } _ { t } ^ { \pi ( W ) } )$ wins that impression, then $s _ { r , t + 1 } =$ $s _ { r , t } + 1$ and $s _ { r ^ { \prime } , t + 1 } = s _ { r ^ { \prime } , t } , \ \forall r ^ { \prime } \neq r .$ . However, if no impression arrives or the ad firm’s bid does not win it, $s _ { r , t + 1 } = s _ { r , t } \forall r \in \mathcal { R }$

For the nonidentical ad exchanges case, we define set function $f ( \beta , W )$ that maps subsets of the finite ground set Ω to nonnegative real numbers, $f : 2 ^ { \Omega } \to \mathbb { R } _ { + }$ , as the expected total cost for given subset of the nonidentical ad exchanges, $W \subseteq \Omega$ . The aim of the ad firm is to find the subset of the nonidentical ad exchanges that minimizes the expected total cost while guaranteeing that the delivery constraint of the ongoing campaigns are satisfied with probability $\beta .$ Therefore, the ad firm’s problem is to find the subset $W \subseteq \Omega$ that minimizes $f ( \beta , W )$

Problem P(Ω):

$$
\min _ {W \subseteq \Omega} f (\beta , W),\tag{1}
$$

where the function $f ( \beta , W )$ is given by solving problem ${ \mathcal { P } } ( \beta , W )$

Problem ${ \mathcal { P } } ( \beta , W )$ :

$$
\begin{array}{l} f (\beta , W) := \min _ {\pi (W)} \sum_ {i \in W} m a x \Bigg \{\sum_ {t = 1} ^ {T} \sum_ {r \in \mathcal {R}} p _ {i, r} \\ \qquad \mathbb {E} _ {\mathbf {s} _ {t} ^ {\pi (W)}} \left[ h _ {i, r} \left(y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right)\right) \right], C _ {i} \Bigg \} + \mathbb {E} _ {K _ {W}} [ g (K _ {W}) ], \end{array}
$$

subject to

$$
\mathbb {P} [ S _ {r, T + 1} ^ {\pi (W)} \geq \xi_ {r} ] \geq \beta ,
$$

$$
\forall r,\tag{2}
$$

$$
y _ {t, i, r} ^ {\pi (W)} (t, \mathbf {s} _ {t} ^ {\pi (W)}) \in [ 0, 1 ],
$$

$$
\forall t, i, r, s _ {t} ^ {\pi (W)},\tag{3}
$$

where $\beta$ is defined as the desired confidence (probability) of satisfying the demand constraint at any location. Because the supply from an ad exchange is usually large, we assume that any single ad exchange can satisfy the ad firm’s demand, assuming it can win all the impressions it needs from the ad exchange.

## Theorem 1. Problem ${ \mathcal { P } } ( \Omega )$ is NP-hard.

We prove this theorem by showing that the set cover problem can be reduced to $\mathcal { P } ( \Omega )$ . A complete proof is provided in Online Appendix A.

In practice, it is possible that the ad firm may consider a set of similar ad exchanges to work with. Hence, in this paper, in addition to the nonidentical ad exchanges case, we also examine the identical ad exchanges case where all ad exchanges are identical and have the same participation fees, location arrival probabilities, and bid curves. We therefore omit the subscript i from these quantities, that is, $C _ { i } = C , p _ { i , r } = p _ { r }$ , and $\bar { \psi } _ { i , r } ( . ) = \psi _ { r } ( . )$ (.or $q _ { i , r } ( . ) = q _ { r } ( . ) )$ . With identical ad exchanges, instead of a set selection problem, the ad firm is faced with the problem of finding the optimal number of ad exchanges to use for procuring impressions and needs to solve the following problem.

Problem $\mathcal { P } ^ { \mathbb { Z } } ( \Omega )$ :

$$
\min _ {\omega \in \{1, 2, \dots , N \},} f ^ {\mathcal {I}} (\beta , \omega),\tag{4}
$$

where function $f ^ { \mathcal { T } } ( \beta , \omega )$ is given by solving problem $\mathcal { P } ^ { \mathcal { I } } ( \beta , \omega )$ ). It is notable that problem $\mathscr { P } ^ { \mathbb { Z } } ( \Omega )$ is a special case of problem ${ \mathcal { P } } ( \Omega )$ , where instead of finding a subset of ad exchanges which minimizes the expected total cost, a number of ad exchanges is obtained. For any given number of ad exchanges $\omega \in \{ 1 , 2 , \ldots , N \}$ , we formulate the following bidding problem called problem $\mathcal { P } ^ { \mathbb { Z } } ( \beta , \omega )$

Problem ${ \mathcal { P } } ^ { \mathbb { Z } } ( \beta , \omega ) \colon$

$$
\begin{array}{l} f ^ {\mathcal {I}} (\beta , \omega) := \min _ {\pi^ {\mathcal {I}} (\omega)} \sum_ {i = 1} ^ {\omega} m a x \Bigg \{\sum_ {t = 1} ^ {T} \sum_ {r \in \mathcal {R}} p _ {r} \\ \qquad \qquad \qquad \mathbb {E} _ {\mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}} \left[ h _ {i, r} \left(y _ {t, i, r} ^ {\pi^ {\mathcal {I}} (\omega)} \left(t, \mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}\right)\right) \right], C \Bigg \} + \mathbb {E} _ {K _ {\omega}} [ g (K _ {\omega}) ], \end{array}
$$

subject to

$$
\mathbb {P} \left[ \mathbf {S} _ {r, T + 1} ^ {\pi^ {\mathcal {I}} (\omega)} \geq \xi_ {r} \right] \geq \beta ,
$$

$$
\forall r,\tag{5}
$$

$$
y _ {t, i, r} ^ {\pi^ {\mathcal {I}} (\omega)} \left(t, \mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}\right) \in [ 0, 1 ],
$$

$$
\forall t, i, r, s _ {t} ^ {\pi^ {\mathcal {I}} (\omega)},\tag{6}
$$

where $\pi ^ { \mathcal { I } } ( \omega )$ is the bidding policy for a case where the ad exchanges are identical and the ad firm obtains its supply from ω number of ad exchanges.

## 3. Solution

In this section, we demonstrate how to solve the prob lem for the nonidentical ad exchanges and identical ad exchanges case. We begin with a high-level illustration of the solution procedure to better understand the following subsections. The high-level overview of the solution procedure is described in Figure 4 available in Online Appendix F. We use backward induction to solve the problem; in step 1, we solve the bidding problem, and we solve the ad exchange selection problem in step 2. A high-level overview of the solution procedure is described in Figure 4 available in Online Appendix F.

## Step 1. Bidding Policy

To solve the bidding problem for the nonidentical ad exchanges case, we take the following steps:

• In Section 3.1.1, first, for any given subset of the nonidentical ad exchanges $W \subseteq { \dot { \Omega } }$ , we define a relaxation of problem ${ \mathcal { P } } ( { \boldsymbol { \beta } } , W )$ , denoted by $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$ . This relaxation is obtained by replacing probabilistic Constraint (2) with an expectation constraint. Then, we obtain an optimal bidding policy for this relaxation which is a lower bound solution for problem ${ \mathcal { P } } ( \beta , W )$

• Next, we define problem $\mathcal { P } _ { \mathcal { R } } ( \bar { \pmb { \alpha } ^ { \prime } } , W )$ and show its optimal solution is a near-optimal bidding policy for problem ${ \mathcal { P } } ( \beta , W )$

• Because the near-optimal bidding policy obtained in Step 1 is used in Step $2 \ ( \mathrm { i . e . } ,$ ad exchange selection) and its performance affects the performance of the solution obtained in Step 2, then we propose a worstcase performance guarantee for the proposed nearoptimal bidding policy to problem ${ \mathcal { P } } ( { \boldsymbol { \beta } } , { \bar { W } } )$

To solve the bidding problem for the identical ad exchanges case, we take the following steps:

• In Section 3.1.2, first, for any given number of ad exchanges $\omega \in \{ 1 , 2 , \ldots , N \}$ , we formulate problem $\mathcal { P } _ { R } ^ { \mathcal { I } } \left( \pmb { \alpha } , \omega \right)$ and $\mathcal { P } _ { \mathcal { R } } ^ { \mathbb { Z } } ( \pmb { \alpha } ^ { \prime } , \omega )$ , which are the special cases of problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ and $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } ^ { \prime } , W )$

• Next, similar to the procedure used for the nonidentical ad exchanges case, we calculate the nearoptimal bidding policy for problem $\mathcal { P } ^ { \mathcal { I } } ( \beta , \omega )$ using the optimal bidding policy of problem $\mathcal { P } _ { R } ^ { \mathcal { I } } ( { \pmb { \alpha } } ^ { \prime } , \omega )$

## Step 2. Ad Exchange Selection

To solve the ad exchange selection problem for the nonidentical ad exchanges case, we take the following steps:

• In Section 3.2.1, we define problem $\mathcal { P } _ { E } ( \Omega )$ and propose an approximation algorithm to find a near-optimal subset of ad exchanges for this problem. We show that solution is a near-optimal solution for problem ${ \mathcal { P } } ( \Omega )$ We also provide a worst-case performance guarantee for the proposed near-optimal.

To solve the ad exchange selection problem for the identical ad exchanges case, we take the following steps:

• In Section 3.2.2, we define problem $\mathcal { P } _ { E } ^ { \breve { \tau } } ( \Omega )$ and find its optimal solution which is a near-optimal solution for problem ${ \mathcal { P } } ^ { \mathcal { I } } ( \Omega )$ . Then, we propose a worst-case performance guarantee for the proposed solution.

## 3.1. Bidding Policy

In this section, we solve the bidding problem for the nonidentical ad exchanges and identical ad exchanges cases, respectively.

3.1.1. Bidding Policy for Nonidentical Ad Exchanges Case. For any given subset of ad exchanges $W \subseteq \Omega$ , we calculate the set of bidding amounts or corresponding winning probabilities which the ad firm chooses for all impressions arriving from the set of specific locations during time. In the rest of this section, we explain how we solve this problem.

A relaxation of problem P(β, W): In the relaxed problem, we replace probabilistic Constraints (2) with expectation Constraints (7). In fact, the expectation constraints are to win a certain number of impressions, say $\alpha _ { r } ,$ in expectation at each location $r \in \mathcal { R }$ . Let be the vector with elements $\alpha _ { r } , \ \forall r \in \mathcal { R }$ . We define a new problem, denoted by $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$

Problem $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$ :

$$
\begin{array}{l} f _ {R} (\boldsymbol {\alpha}, W) := \min _ {\pi (W)} \sum_ {i \in W} m a x \Bigg \{\sum_ {t = 1} ^ {T} \sum_ {r \in \mathcal {R}} p _ {i, r} \\ \qquad \mathbb {E} _ {\mathbf {S} _ {t} ^ {\pi (W)}} \left[ h _ {i, r} \left(y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right)\right) \right], C _ {i} \Bigg \} + \mathbb {E} _ {K _ {W}} [ g (K _ {W}) ], \end{array}
$$

subject to,

$$
\sum_ {i \in W} \sum_ {t = 1} ^ {T} p _ {i, r} \mathbb {E} _ {\mathbf {s} _ {t} ^ {\pi (W)}} \left[ y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right) \right] \geq \alpha_ {r}, \forall r,\tag{7}
$$

$$
y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right) \in [ 0, 1 ],
$$

$$
\forall t, i, r, s _ {t} ^ {\pi (W)},\tag{8}
$$

and for each $r \in \mathcal { R }$ , the probabilistic guarantee (2) in problem ${ \mathcal { P } } ( \beta , W )$ implies the expectation guarantee (7) in problem $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$ , that is, the constraint $\mathbb { P } [ S _ { r , T + 1 } ^ { \pi ( W ) } \geq$ $\xi _ { r } \bar { ] } \ge \beta$ implies the inequality $\mathbb { E } [ S _ { r , T + 1 } ^ { \pi ( W ) } ] \geq \beta \xi _ { r }$ : This can be easily shown using the relationship between the expectation of a random variable and its cumulative distribution function: $\begin{array} { r } { \mathbb { E } [ S _ { r , T + 1 } ^ { \pi ( W ) } ] = \sum _ { s = 0 } ^ { \xi _ { r } } \mathbb { P } [ S _ { r , T + 1 } ^ { \pi ( W ) } \ge s ] } \end{array}$ : Then, we can say that $\begin{array} { r } { \sum _ { s = 0 } ^ { \xi _ { r } } \mathbb { P } [ S _ { r , T + 1 } ^ { \pi ( W ) } \geq s ] \geq \sum _ { s = 0 } ^ { \xi _ { r } } \beta = \beta \xi _ { r } } \end{array}$ : Hence, Constraint (2) implies (7). However, the reverse statement is not true. Thus, for the choice $\begin{array} { r } { \pmb { \alpha } = \beta \pmb { \xi } , } \end{array}$ problem $\mathcal { P } _ { R } ( \beta \pmb { \xi } , W )$ is a relaxation of problem ${ \mathcal { P } } ( \beta , W )$ , or any feasible solution of problem ${ \mathcal { P } } ( \beta , W )$ is also a feasible solution for problem $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$ ).

For any given subset of ad exchanges $W \subseteq \Omega ,$ , we introduce a deterministic problem, explained in Online Appendix B and then establish its equivalence to problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W ) .$ ; that is, we show that an optimal policy for problem $\mathcal { P } _ { R } ( \pmb { \alpha } , W )$ can be obtained from an optimal solution to the proposed deterministic problem.<sup>7</sup> To proceed, we first show that the optimal objective function value of the deterministic problem is a lower bound for the optimal objective function value of problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ . Then we show that there is a feasible solution for problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ whose objective function value is same as the optimal objective function value of the deterministic problem.

Proposition 1. The optimal policy of problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ is the state-independent policy $\pi _ { \alpha } ^ { * } ( W ) : = y _ { t , i , r } ^ { \pi _ { \alpha } ^ { * } ( W ) } ( t , \mathbf { s } _ { t } ^ { \pi _ { \alpha } ^ { * } ( W ) } ) =$ $y _ { i , r } ^ { * \mathcal { D } } , \ \forall t ,$ , where $y _ { i , r } ^ { * \mathcal { D } }$ is an optimal solution for the deterministic problem.

The proof is provided in Online Appendix A.

The optimal policy described in Proposition 1 is a state-independent policy. That is, the winning probability determined by the ad firm at a given time does not depend on the state of the system at that time, the number of impressions won from the individual location. The policy is easy to compute and is obtained by solving the deterministic problem whose objective function is a continuous and convex function on a closed, bounded, and convex set, and therefore it is a convex optimization problem and there exists an optimal solution for the problem. In practice, this property is useful when the bidding architecture is distributed, because the state independent property enables the servers in the computing cluster to bid independently of one another, without exchanging state information.

A near-optimal solution to problem ${ \mathcal { P } } ( \beta , W )$ : Until now, we have obtained an optimal policy for problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ . In particular, for the choice ${ \pmb { \alpha } } = \beta { \pmb { \xi } } ,$ , we have an optimal policy for our relaxation $\mathcal { P } _ { \mathcal { R } } ( \beta \pmb { \xi } , \mathbf { C } _ { W } )$ . As discussed earlier, the probabilistic constraint in problem ${ \mathcal { P } } ( \beta , W )$ implies the expectation constraint in problem $\mathcal { P } _ { \mathcal { R } } ( \beta \boldsymbol { \xi } , W )$ . Therefore, we need to formulate a new problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } ^ { \prime } , W )$ using a suitable parameter ${ \pmb { \alpha } } ^ { \prime } \geq \beta { \pmb { \xi } }$ such that the optimal solution of problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } ^ { \prime } , W )$ is feasible for problem ${ \mathcal { P } } ( \beta , W )$

We derive the value of $\pmb { \alpha } ^ { \prime }$ with elements $\alpha _ { r } ^ { \prime }$ such that $\mathbb { E } [ { \pmb S } _ { r , T + 1 } ^ { \pi ( W ) } ] = \alpha _ { r } ^ { \prime }$ implies $\mathbb { P } [ \mathbf { S } _ { r , T + 1 } ^ { \pi ( W ) } \geq \xi _ { r } ] = \beta$ . Under static policy $\pi ( W )$ , the random variable $\mathbf { S } _ { r , T + 1 } ^ { \pi ( W ) } ,$ , representing the number of impressions won over the $T$ time slots from location r is a binomially distributed random variable with a trial success probability of $\begin{array} { r } { \gamma _ { r } = \sum _ { i \in W } p _ { i , r } y _ { i , r } , } \end{array}$ $\forall r \in \mathcal { R }$ . We apply the central limit theorem to use a normal approximation for the distribution of the random variable $\mathbf { S } _ { r , T + 1 } ^ { \pi ( W ) }$ , which is appropriate here, since the sample size is adequate (Billingsley 2008). The sample size here is $T ,$ the time duration of campaigns, which is large in practice. According to Hogg and Tanis (2009), $T \geq 3 0$ can be considered as a large enough sample size for using the central limit theorem. Therefore, using central limit theorem, we calculate the normal approximation for $\mathrm { B i n } ( T , \gamma _ { r } )$ and we have

$$
\Phi_ {N} \left(\frac {T \gamma_ {r} - \xi_ {r}}{\sqrt {T \gamma_ {r} (1 - \gamma_ {r})}}\right) = \beta ,
$$

where $\Phi _ { N } ( . )$ is the cumulative distribution function of the standard normal distribution. Thus, we get

$$
(T \gamma_ {r} - \xi_ {r}) ^ {2} = z _ {\beta} ^ {2} T \gamma_ {r} (1 - \gamma_ {r}),
$$

where $z _ { \beta } = \Phi _ { N } ^ { - 1 } ( \beta )$ . The solution for the previous equation is

$$
\gamma_ {r} = \frac {(2 \xi_ {r} + z _ {\beta} ^ {2}) + \sqrt {(2 \xi_ {r} + z _ {\beta} ^ {2}) ^ {2} - 4 \left(1 + \frac {z _ {\beta} ^ {2}}{T}\right) \xi_ {r} ^ {2}}}{2 (T + z _ {\beta} ^ {2})}.
$$

In practice, $\beta$ is close to one, and the number of impressions $\xi _ { r }$ required at location r is in the order of thousands. Therefore, $\xi _ { r } \gg z _ { \beta }$ . Using this, we can approximate $q _ { r } .$

$$
\gamma_ {r} \approx \frac {\xi_ {r}}{T} + \frac {z _ {\beta} \sqrt {\xi_ {r}}}{T}.
$$

Thus, under the static policy $\pi ( W )$ , the expected numbe of impressions won from location r is

$$
\alpha_ {r} ^ {\prime} = T \gamma_ {r} \approx \xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}.
$$

The amount $z _ { \beta } \sqrt { \xi _ { r } }$ is the additional amount (or buffer) that the static policy needs to plan for to ensure that at least $\xi _ { r }$ impressions are won from location r with probability $\beta . ^ { 8 }$ The following theorem summarizes the results obtained from previous analysis. Let $\pmb { \xi } _ { o }$ denote the vector with elements $\sqrt { \xi _ { r } } , r \in \mathcal { R }$

Theorem 2. For the choice ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o }$ , the optimal policy of problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ is a feasible solution for problem ${ \dot { \mathcal { P } } } ( { \dot { \boldsymbol { \beta } } } , W )$

Performance guarantee of the near-optimal Solution to problem ${ \mathcal { P } } ( { \boldsymbol { \beta } } , W ) ;$ : Next, we illustrate that the static policy described in Theorem 2 is near optimal for problem ${ \mathcal { P } } ( \beta , W )$ . Let $\pi _ { \alpha } ^ { * } ( W )$ be the optimal policy for problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ for the choice ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o }$ and $C o s t ( \pmb { \xi } +$ $z _ { \beta } \pmb { \xi } _ { o } , W )$ . represents the cost incurred by static policy $\pi _ { \alpha } ^ { * } ( W )$ ) and be equal to $f _ { \mathcal { R } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , W )$ . Let $C o s t ( \beta , \bar { W } )$ be the optimal cost for problem ${ \mathcal { P } } ( \beta , W )$ . It is clear that $C o s t ( \bar { \beta } , W ) \ge f _ { \mathcal { R } } ( \beta \xi , W )$ , where $f _ { \mathcal { R } } ( \beta \boldsymbol { \xi } , W )$ is the optimal cost for problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , W )$ for the choice $\begin{array} { r } { \pmb { \alpha } = \beta \pmb { \xi } . } \end{array}$ . The following theorem illustrates the performance guarantee of the proposed near-optimal solution to problem ${ \mathcal { P } } ( \beta , W )$

Theorem 3. For the choice ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o }$ , the policy $\pi _ { \alpha } ^ { * } ( W )$ achieves the following performance guarantee for problem ${ \mathcal { P } } ( \beta , W )$

$$
\frac {\operatorname{Cost} \left(\boldsymbol {\xi} + z _ {\beta} \boldsymbol {\xi} _ {o} , W\right)}{\operatorname{Cost} (\beta , W)} \leq \frac {f _ {\mathcal {R}} \left(\boldsymbol {\xi} + z _ {\beta} \boldsymbol {\xi} _ {o} , W\right)}{f _ {\mathcal {R}} \left(\beta \boldsymbol {\xi} , W\right)}.\tag{9}
$$

3.1.2. Bidding Policy for Identical Ad Exchanges Case. From Theorem $^ { 2 , }$ for any given $\omega ,$ for the choice ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o }$ , the optimal solution of the following prob lem is a feasible solution for problem $\mathcal { P } ^ { \mathcal { I } } ( \beta , \omega )$

Problem $\mathcal { P } _ { R } ^ { \mathcal { L } } ( \pmb { \alpha } , \omega ) \mathrm { : }$

$$
\begin{array}{l} f _ {R} ^ {\mathcal {I}} (\boldsymbol {\xi} + z _ {\beta} \boldsymbol {\xi} _ {o}, \omega) := \min _ {\pi^ {\mathcal {I}} (\omega)} \sum_ {i = 1} ^ {\omega} m a x \Bigg \{\sum_ {t = 1} ^ {T} \sum_ {r \in \mathcal {R}} p _ {r} \\ \qquad \qquad \qquad \mathbb {E} _ {\mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}} \Big [ h _ {i, r} \Big (y _ {t, i, r} ^ {\pi^ {\mathcal {I}} (\omega)} \Big (t, \mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)} \Big) \Big) \Big ], C \Bigg \} \\ \qquad + \mathbb {E} _ {K _ {\omega}} [ g (K _ {\omega}) ], \end{array}
$$

subject to

$$
\sum_ {i = 1} ^ {\omega} \sum_ {t = 1} ^ {T} p _ {r} \mathbb {E} _ {\boldsymbol {S} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}} \left[ \mathcal {y} _ {t, i, r} ^ {\pi^ {\mathcal {I}} (\omega)} \left(t, \boldsymbol {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}\right) \right] \geq \xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}, \quad \forall r,\tag{10}
$$

$$
y _ {t, i, r} ^ {\pi^ {\mathcal {I}} (\omega)} (t, \mathbf {s} _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}) \in [ 0, 1 ], \qquad \forall t, i, r, s _ {t} ^ {\pi^ {\mathcal {I}} (\omega)}.\tag{11}
$$

From Proposition 1, we know that the optimal bidding policy for the above problem is a state-independent policy, that is, $\pi _ { \alpha } ^ { \underline { { T } } ^ { * } } ( \omega ) : = \tilde { y } _ { i , r } ^ { * }$ . We take the following steps to optimize the optimal number of ad exchanges.

• First, for any given number of ad exchanges $\omega \in [ 1 , N ]$ , using the results described in Proposition 1, we find a closed-form expression for the optimal bidding policy for problem $\mathbf { \widehat { \mathcal { P } } } _ { \mathcal { R } } ^ { \mathbb { Z } } ( \alpha , \omega )$ , where ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o } ,$ which is an approximate solution to problem $\mathcal { P } ^ { \mathcal { I } } ( \beta , \dot { \omega } )$

• Then, we obtain a near-optimal number of ad exchanges for problem ${ \mathcal { P } } ^ { \mathcal { I } } ( \Omega )$ and provide the performance guarantee for the proposed near-optimal solution.

The following proposition states that using identical winning probabilities for bid requests arriving from the same location via different ad exchanges is optimal for problem $\mathcal { P } _ { \mathcal { R } } ^ { \mathbb { Z } } ( \alpha , \omega )$ .

Proposition 2. There exists an optimal solution to problem $\mathcal { P } _ { \mathcal { R } } ^ { \mathcal { I } } ( \pmb { \alpha } , \omega )$ in which all impressions arriving from the same location are procured in the same cost with the following winning probability

$$
y _ {r} ^ {*} = \frac {\alpha_ {r}}{T p _ {r} \omega}.\tag{12}
$$

The proof is provided in Online Appendix A.

The previous result follows from the fact that the ad exchanges have the same bid curve for any given location, and this bid curve is strictly increasing and convex in the winning probability. Therefore, from Proposition 2 and Equation (12), the optimal solution to problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , \omega )$ for ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { \mathrm { { } } }$ is as follows.

Corollary 1. When the ad exchanges are identical, for any given number of ad exchanges $\omega \in \{ 1 , 2 , \ldots , N \}$ , the optimal winning probabilities to problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , \omega )$ , where $\begin{array} { r } { \pmb { \alpha } = \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , } \end{array}$ is

$$
y _ {r} ^ {*} = \frac {\xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}}{T p _ {r} \omega}, \quad \forall r \in \mathcal {R}.\tag{13}
$$

The optimal objective function value equals $f _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega )$ $= \mathrm { m a x } \{ f _ { 1 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ) , f _ { 2 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ) \}$ , where $f _ { 1 } ^ { \underline { { \tau } } } ( \pmb { \xi } + z _ { \beta }$ $\begin{array} { r } { \pmb { \xi } _ { o } , \omega ) = \sum _ { r \in \mathcal { R } } ( \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } ) \psi _ { r } \Big ( \frac { \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } } { T p _ { r } \omega } \Big ) + \mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ] } \end{array}$ and $f _ { 2 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ) = \omega C + \mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ] .$

It is notable that we define function $f _ { \mathcal R } ^ { \varPsi } ( . )$ as maximum of two functions $f _ { 1 } ^ { \mathcal { T } } ( . )$ and $f _ { 2 } ^ { \mathcal { I } } ( . )$ because the ad firm either pays the participation fee or it does not, and these are the two cases.

## 3.2. Ad Exchange Selection

3.2.1. Ad Exchange Selection for Nonidentical Ad Ex changes Case. In this section, we study a general problem with nonidentical ad exchanges. Here, the ad firm must select a subset of ad exchanges to obtain its supply from. To solve problem ${ \mathcal { P } } ( \Omega )$ , we first introduce problem $\mathcal { P } _ { E } ( \Omega )$ , although $\mathcal { P } _ { E } ( \Omega )$ is different from the original problem ${ \mathcal { P } } ( \Omega )$ , we show that an approximate solution to $\mathcal { P } _ { E } ( \Omega )$ is also an approximate solution to ${ \mathcal { P } } ( \Omega )$ . Then, We present an algorithm named EnhancedHillClimbing to provide an efficient, near-optimal policy for problem $\bar { \mathcal { P } } _ { E } ( \Omega )$ that is ultimately an approximation solution for problem $\mathcal { P } _ { E } ( \Omega )$ as well. The details of the proposed algorithm are available in Online Appendix D. We also propose a worst-case performance guarantee for our algorithm that is available in Online Appendix D.

Problem $\mathcal { P } _ { E } ( \Omega )$

$$
\min _ {W \subseteq \Omega} f _ {\mathcal {R}} (\boldsymbol {\xi} + z _ {\beta} \boldsymbol {\xi} _ {o}, W),
$$

Theorem 4. Problem $\mathcal { P } _ { E } ( \Omega )$ is NP-hard.

The proof of Theorem 4 is similar to that of Theorem 1. More details can be found in Online Appendix A.

## Theorem 5. The solution returned from EnhancedHill Climbing algorithm is a feasible solution for problem P(Ω).

The proof is provided in Online Appendix D.

Numerical experiments: We next evaluate the performance of Enhanced Hill Climbing for solving the ad exchange selection problem for the nonidentical ad exchanges case. The experimental design to generate the problem instances is as follows. We consider two loca tions and assume the demand at each location is generated randomly from U[5,000, 10,000]. The capacity cost function is defined as $g ( K ) = \lambda _ { 1 } ( e ^ { \lambda _ { 2 } K } - 1 )$ where the values of $\lambda _ { 1 }$ and $\lambda _ { 2 }$ are randomly chosen from U[25, 35] and $U [ 1 0 ^ { - 7 } , 5 \times 1 0 ^ { - 7 } ]$ , respectively. We randomly generate the value of the two parameters $T$ and $\beta$ from U[600,000, 650,000] and U[0.90, 0.999], respectively. The number of potential mobile ad exchanges is also generated randomly from U[1, 30]. The expected bidding cost for each exchange-location combination is defined as $\begin{array} { r } { h _ { i , r } ( y ) = \frac { y } { \kappa _ { 1 } ^ { i , r } } \mathrm { l n } \biggl ( \frac { y ( 1 - y _ { 0 } ^ { i , r } ) + y _ { 0 } ^ { i , r } } { 1 - y ( 1 - y _ { 0 } ^ { i , r } ) - y _ { 0 } ^ { i , r } } \biggr ) - \frac { y \kappa _ { 0 } ^ { i , r } } { \kappa _ { 1 } ^ { i , r } } . } \end{array}$ , ∀i, r, where $\kappa _ { 0 } ^ { i , r }$ and $\kappa _ { 1 } ^ { i , r }$ are randomly generated from U[�5, 1] and U[0, 6], respectively.<sup>9</sup> The arrival probability of an impression from a given exchange-location combination is generated randomly from U[0.001, 0.1]. The participation fee for an ad exchange is generated randomly from U[5,000, 10,000]. Based on the previous design, we generate 15 random problem instances with the parameters presented in Table 2.<sup>10</sup>

We used MATLAB to implement Enhanced Hill Climbing on an Intel Core i7 CPU running at 3.4GHz. For small-sized problems, we also obtained the optimal solution of problem $\mathcal { P } _ { E } ( \Omega )$ using an enumeration algorithm. In Table 2, for each small-sized problem instance, we compare the Enhance Hill Climbing solution with the benchmark solution (best single ad exchange solution), the solution obtained from enumeration, and the solution from a greedy heuristic algorithm. The greedy heuristic algorithm starts with an empty set, and then incrementally adds an ad exchange to the current solution that yields the largest cost reduction. This process iterates until the cost cannot be reduced. The greedy heuristic algorithm is possibly the most intuitive approach to solve our problem and is easy to implement. For large-sized problems, we compare the Enhance Hill Climbing solution with the benchmark solution and the greedy heuristic algorithm. Table 2 summarizes the computation results, including the expected total cost and the computation time (in seconds) for the benchmark solution, Enhance Hill Climbing solution, enumeration solution, and the solution from the greedy heuristic algorithm. For each problem instance, we measure the quality of the Enhance Hill Climbing solution by providing the worst case performance guarantee values and the savings of Enhance Hill Climbing over the benchmark solution as $S \mathbf { v } _ { e h } ^ { b e n c h } =$ (Benchmark� Enhance Hill Climbing)=Benchmark × 100.

We report the savings of Enumeration over Enhance Hill Climbing as $\mathrm { S v } _ { e h } ^ { e n u m } = \left( \mathrm { E n u m e r a t i o n } - \right.$ Enhance Hill Climbing)=Enumeration × 100. We also report the savings of Enhance Hill Climbing over the greedy heuristic as $\mathrm { \Delta } \mathrm { S v } _ { e h } ^ { g r e e d y } = \mathrm { ( G r e e d y }$ Heuristic � Enhance Hill Climbing) =Greedy Heuristic × 100. In Table 2, the acronyms TC, enum, eh, bench and P-G stand for the expected total cost, enumeration, EnhancedHillClimbing, benchmark, and the worst-case performance guarantee, respectively. The value of ε in Enhanced Hill Climbing approach was set to 0.5.

The computational study shows that for problem instances with the potential number of mobile ad exchanges greater than or equal to 14, the enumeration solution could not be obtained in two hours. For small problem instances, the gap between the expected total cost of Enhanced Hill Climbing solution and enumeration solution is zero. The average saving of the proposed Enhanced Hill Climbing approach over benchmark is 25.64% across 15 random problem instances. The average saving of the proposed Enhanced Hill Climbing approach over greedy heuristic is 18.13% across 15 random problem instances.

3.2.2. Ad Exchange Selection for Identical Ad Exchanges Case. Having obtained near-optimal win probabilities for different locations, we now need to obtain the near-optimal number of ad exchanges. Let us introduce the following problem.

Problem $\mathcal { P } _ { E } ^ { \mathcal { I } } ( \Omega )$

$$
\min _ {\omega \in \{1, 2, \ldots , N \},} f _ {\mathcal {R}} ^ {\mathcal {I}} (\pmb {\xi} + z _ {\beta} \pmb {\xi} _ {o}, \omega),\tag{14}
$$

where it is clear that the optimal solution of problem $\mathcal { P } _ { E } ^ { \mathcal { I } } ( \Omega )$ is a feasible solution to problem ${ \mathcal { P } } ^ { \mathcal { I } } ( \Omega )$ . Now, we need to find the optimal solution for problem ${ \mathcal { P } } _ { E } ^ { \mathcal { I } } ( \Omega )$

Table 2. Performance of Enhanced Hill Climbing Heuristic

<table><tr><td rowspan="2">No.</td><td rowspan="2">N</td><td rowspan="2"> $\beta$ </td><td rowspan="2">T</td><td rowspan="2">Benchmark</td><td rowspan="2">Greedy heuristic</td><td colspan="2">Enumeration</td><td colspan="6">Enhanced hill climbing</td></tr><tr><td>Time (s)</td><td>TC ($)</td><td>Time (s)</td><td>TC ($)</td><td>%  $Sv_{eh}^{enum}$ </td><td>%  $Sv_{eh}^{greedy}$ </td><td>%  $Sv_{eh}^{bench}$ </td><td>P-G</td></tr><tr><td>1</td><td>2</td><td>0.99</td><td>600,176</td><td>46,149</td><td>41,967</td><td>1.7092</td><td>34,820</td><td>0.154</td><td>34,820</td><td>0</td><td>17.03</td><td>24.55</td><td>1.53</td></tr><tr><td>2</td><td>3</td><td>0.95</td><td>634,505</td><td>53,223</td><td>47693</td><td>1.8731</td><td>40,477</td><td>0.4862</td><td>40,477</td><td>0</td><td>15.13</td><td>23.95</td><td>1.62</td></tr><tr><td>3</td><td>4</td><td>0.98</td><td>601,853</td><td>51,718</td><td>46,925</td><td>5.6720</td><td>38,509</td><td>0.9912</td><td>38,509</td><td>0</td><td>17.93</td><td>25.54</td><td>1.65</td></tr><tr><td>4</td><td>5</td><td>0.96</td><td>648,945</td><td>49,083</td><td>45,602</td><td>11.4182</td><td>36,649</td><td>1.0679</td><td>36,649</td><td>0</td><td>19.63</td><td>25.33</td><td>1.60</td></tr><tr><td>5</td><td>8</td><td>0.94</td><td>603,249</td><td>61,728</td><td>56,182</td><td>24.0742</td><td>44,618</td><td>2.8367</td><td>44,618</td><td>0</td><td>20.58</td><td>27.72</td><td>1.49</td></tr><tr><td>6</td><td>13</td><td>0.97</td><td>643,874</td><td>76,647</td><td>68,835</td><td>24,576</td><td>56,297</td><td>7.875</td><td>56,297</td><td>0</td><td>18.22</td><td>26.55</td><td>1.51</td></tr><tr><td>7</td><td>14</td><td>0.99</td><td>619,736</td><td>71,349</td><td>64,582</td><td>—</td><td>—</td><td>13.642</td><td>53,936</td><td>—</td><td>16.48</td><td>24.40</td><td>1.63</td></tr><tr><td>8</td><td>16</td><td>0.93</td><td>628,316</td><td>67,546</td><td>59,604</td><td>—</td><td>—</td><td>23.601</td><td>49,852</td><td>—</td><td>16.36</td><td>26.20</td><td>1.59</td></tr><tr><td>9</td><td>19</td><td>0.95</td><td>630,589</td><td>77,924</td><td>71,453</td><td>—</td><td>—</td><td>29.595</td><td>58,849</td><td>—</td><td>17.64</td><td>24.48</td><td>1.64</td></tr><tr><td>10</td><td>20</td><td>0.97</td><td>624,139</td><td>76,864</td><td>70,594</td><td>—</td><td>—</td><td>30.552</td><td>56,593</td><td>—</td><td>19.83</td><td>26.37</td><td>1.58</td></tr><tr><td>11</td><td>21</td><td>0.92</td><td>608,456</td><td>83,136</td><td>74,825</td><td>—</td><td>—</td><td>31.954</td><td>63,285</td><td>—</td><td>15.42</td><td>23.88</td><td>1.62</td></tr><tr><td>12</td><td>23</td><td>0.90</td><td>615,437</td><td>91,603</td><td>82,942</td><td>—</td><td>—</td><td>32.501</td><td>65,736</td><td>—</td><td>20.74</td><td>28.24</td><td>1.64</td></tr><tr><td>13</td><td>26</td><td>0.93</td><td>640,285</td><td>93,425</td><td>85,674</td><td>—</td><td>—</td><td>35.483</td><td>69,509</td><td>—</td><td>18.87</td><td>25.60</td><td>1.62</td></tr><tr><td>14</td><td>29</td><td>0.91</td><td>600,893</td><td>80,409</td><td>73,193</td><td>—</td><td>—</td><td>30.963</td><td>59,832</td><td>—</td><td>18.25</td><td>25.59</td><td>1.56</td></tr><tr><td>15</td><td>30</td><td>0.94</td><td>645,821</td><td>95,543</td><td>88,015</td><td>—</td><td>—</td><td>33.162</td><td>70,538</td><td>—</td><td>19.86</td><td>26.17</td><td>1.58</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>—</td><td>18.13</td><td>25.64</td><td>1.59</td></tr></table>

We first ignore the integrality constraint on ω and assume that $\omega \in [ 1 , N ]$ . Next, we introduce the following lemmas.

Lemma 1. Without the integrality constraint on $\omega ,$ the expected capacity cost (i.e., function $\mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ] )$ is strictly increasing and strictly convex in ω. The function $f _ { 1 } ^ { \underline { { \tau } } } ( { \pmb \xi } ^ { \underline { { \tau } } } +$ $z _ { \beta } \pmb { \xi } _ { o } , { \omega } )$ is strictly convex in $\omega ,$ and function $f _ { 2 } ^ { \scriptscriptstyle \mathscr { T } } ( \pmb { \xi } +$ $z _ { \beta } \pmb { \xi } _ { o } , { \omega } )$ is strictly increasing and strictly convex in ω.

## The proof is provided in Online Appendix A.

When the ad firm works with more ad exchanges, it receives more bid requests. However, to meet the response time constraint (e.g., 100 ms), the ad firm needs to deploy more computing resources. Therefore, the computing cost (capacity cost) increases.

For any given number of ad exchanges $\omega ,$ the function $f _ { 1 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \dot { \xi } } _ { o } , \omega )$ denotes the expected total cost including the bidding cost and the capacity cost. Hence, when the ad firm works one ad exchange, the bid amount (or equivalently the winning probability) is at its highest value, and it results to the highest possible expected bidding cost. However, the expected capacity cost in this situation is the smallest. As the number of ad exchanges increases, the expected bidding cost decreases but the expected capacity cost increases.

For any given number of ad exchanges, $\omega ,$ the function $f _ { 2 } ^ { \mathcal { T } } ( \pmb { \xi } + \bar { z } _ { \beta } \pmb { \xi } _ { o } , \omega )$ is defined as sum of participation fee charged by the ad exchanges and the expected capacity cost. By working with more ad exchanges, the sum of participation fees increases and expected capacity cost also increases. Therefore, $f _ { 2 } ^ { \mathcal { T } } \big ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega \big )$ always increases in ω.

Lemma 2. Without the integrality constraint on $\omega ,$ , there exists point - where the marginal procurement cost is equal to the marginal capacity cost, that is,

$$
\sum_ {r \in \mathcal {R}} (\xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}) \left[ \frac {\partial \psi_ {r} (y _ {r} ^ {*})}{\partial y _ {r} ^ {*}} \right. \left. \frac {\mathrm{d} y _ {r} ^ {*}}{\mathrm{d} \omega} \right] \bigg | _ {\omega = \varpi} = - \frac {\partial \mathbb {E} _ {K _ {\omega}} [ g (K _ {\omega}) ]}{\partial \omega} \bigg | _ {\omega = \varpi}.\tag{15}
$$

The result in Lemma 2 is from Lemma 1 and the fact that the function $\psi _ { r } ( y _ { r } ^ { * } )$ is decreasing in ω and function $\mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ]$ is increasing in ω. Let ϱ denote the smallest point where the two functions intersect, that is, $\varrho = \hat { \operatorname* { m i n } } \{ \omega | f _ { 1 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ) = f _ { 2 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ) \}$ . Theorem 6 characterizes a feasible solution to problem $\mathcal { P } ^ { \mathcal { I } } ( \Omega )$ .

Theorem 6. An optimal solution to problem $\mathcal { P } _ { F } ^ { \mathcal { I } } ( \Omega )$ (or equivalently, a feasible solution to problem $\mathcal { P } ^ { \tau } ( \Omega ) \big ) , \omega ^ { u p } ,$ , is

(i) equal to 1, $\begin{array} { r } { i f \sum _ { r \in \mathcal { R } } ( \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } ) \psi _ { r } \Big ( \frac { \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } } { T p _ { r } } \Big ) \leq C , } \end{array}$

(ii) min{arg m $\begin{array} { r } { \mathrm { n } _ { \omega } \{ f _ { \mathcal { R } } ^ { \mathcal { Z } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \lfloor \varpi \rfloor ) , f _ { \mathcal { R } } ^ { \mathcal { Z } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \lceil \varpi \rceil ) \} } \end{array}$

$$
N \}, i f \sum_ {r \in \mathcal {R}} (\xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}) \psi_ {r} \left(\frac {\xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}}{T p _ {r} N}\right) > C,
$$

(iii) min{arg min<sub>ω</sub> $\{ f _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \lfloor \operatorname* { m i n } \{ \varrho , \varpi \} \rfloor ) , f _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta }$ $\pmb { \xi } _ { o } , \lceil \operatorname* { m i n } \{ \varrho , \varpi \} \rceil ) \} , N \}$ , otherwise.

The proof is provided in Online Appendix A.

(i) The expected bidding cost decreases in the number of ad exchanges (ω). When $\omega = 1$ the expected bidding cost is at its highest. If, for this case, the expected bidding cost is smaller than the participation fee, then the ex pected bidding cost will remain smaller than the participation fee if the number of ad exchanges is increased. Adding more ad exchanges will only increase the pro curement cost (via an increase in participation cost). At the same time, the expected capacity cost will also in crease if more ad exchanges are added. Therefore, work ing with one ad exchange will be optimal.

(ii) On the other hand, if the ad firm works with the maximum available number of ad exchanges and the expected bidding cost is larger than the participation fee, then the participation fee constraint will never be binding. Under this case, the procurement cost is equal to the expected bidding cost for any given ω. Therefore, the best number of ad exchanges to work with is either ⌊-⌋, ⌈-⌉, or N. At point -, the marginal increment in the expected capacity cost is equal to marginal decrement in the expected bidding cost.

(iii) If neither case (i) nor (ii) holds, then the ad firm must work with either ⌊min $\{ \varrho , \varpi \} \rfloor$ , ⌈min $\{ \varrho , \varpi \} ]$ , or N.

Corollary 2. Given the feasible number of ad exchange $\omega ^ { u p }$ for problem $\mathcal { P } ^ { \mathbb { Z } } ( \Omega )$ , the near-optimal bidding policy for problem $\mathcal { P } ( \beta , \omega )$ is $\pi _ { \alpha } ^ { \mathcal { T } ^ { * } } ( \omega ^ { u p } ) : = y _ { r } ^ { * } \dot { ( } \omega ^ { u p } )$ calculated in $( 1 3 )$ with the expected total cost $\bar { f } _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ^ { u p } ) = \mathrm { m a x } \{ f _ { 1 } ^ { \mathcal { T } }$ $( { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o } , \omega ^ { u { \dot { p } } } ) , f _ { 2 } ^ { \mathcal { T } } ( { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } _ { o } , \omega ^ { u { \dot { p } } } ) { \} }$

Performance guarantee for the near-optimal solution to problem ${ \mathcal { P } } ^ { \mathcal { I } } ( \breve { \Omega } ) \colon$ Having obtained a feasible solution $\omega ^ { u \hat { p } }$ to problem ${ \mathcal { P } } ^ { \mathcal { I } } ( \Omega )$ , we next derive a lower bound solution to this problem to calculate a worst-case performance guarantee. Let us define the following problem.

Problem $\mathcal { P } _ { L } ^ { \mathcal { I } } ( \Omega )$

$$
\min _ {\omega \in \{1, 2, \dots , N \},} f _ {\mathcal {R}} ^ {\mathcal {I}} (\beta \boldsymbol {\xi}, \omega).\tag{16}
$$

As discussed in Section 3.1.2, for any given number of ad exchanges $\omega \in [ 1 , N ]$ , the optimal solution to problem $\mathcal { P } _ { \mathcal { R } } ( \pmb { \alpha } , \omega )$ , where ${ \pmb { \alpha } } = \beta { \pmb { \xi } } ,$ , is a lower bound solution for problem $\mathcal { P } ( \beta , \omega )$ . According to Proposition 2, for any given number of ad exchanges $\omega ,$ the optimal winning probabilities for problem $\mathcal { P } _ { \mathcal { R } } ( \beta \pmb { \xi } , \omega )$ are equal to $\frac { \beta \xi _ { r } ^ { \cup } } { T p _ { r } \omega }$ with the following objective function value:

$$
f _ {\mathcal {R}} ^ {\mathcal {I}} (\beta \pmb {\xi}, \omega) = \max \{f _ {1} ^ {\mathcal {I}} (\beta \pmb {\xi}, \omega), f _ {2} ^ {\mathcal {I}} (\beta \pmb {\xi}, \omega) \},\tag{17}
$$

where $f _ { 1 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega )$ and $f _ { 2 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega )$ are defined as $f _ { 1 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega ) =$ $\begin{array} { r } { \sum _ { r \in \mathcal { R } } ( \beta \xi _ { r } ) \psi _ { r } \left( \frac { \beta \xi _ { r } } { T p _ { r } \omega } \right) + \mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ] } \end{array}$ and $f _ { 2 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega ) = \omega C +$ $\mathbb { E } _ { K _ { \omega } } [ g ( K _ { \omega } ) ]$ . Similar to Theorem 6 and Corollary 2, we have the following result.

Lemma 3. Under the identical ad exchanges case, a lower bound solution to problem $\mathcal { P } ^ { \mathcal { I } } ( \Omega ) , \omega ^ { l b }$ is

(i) equal to $\begin{array} { r } { 1 , i f \sum _ { r \in \mathcal { R } } ( \beta \xi _ { r } ) \psi _ { r } \left( \frac { \beta \xi _ { r } } { T p _ { r } } \right) \leq C , } \end{array}$

(ii) min{arg m $\mathrm { i n } _ { \omega } \{ f _ { \mathcal { R } } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \lfloor \varpi ^ { l \hat { b } } \rfloor ^ { - } ) , f _ { \mathcal { R } } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \lceil \varpi ^ { l b } \rceil ) \} , N \} \mathrm { . ~ }$

$$
\sum_ {r \in \mathcal {R}} (\beta \xi_ {r}) \psi_ {r} \left(\frac {\beta \xi_ {r}}{T p _ {r} N}\right) > C,
$$

(iii) $\begin{array} { r } { \operatorname* { m i n } \{ \arg \operatorname* { m i n } _ { \omega } \{ f _ { \mathcal { R } } ^ { \mathcal { Z } } ( \beta \pm \xi , \lfloor \operatorname* { m i n } \{ \varrho ^ { l b } , \varpi ^ { l b } \} \rfloor ) , f _ { \mathcal { R } } ^ { \mathcal { Z } } ( \beta \pm \xi , } \end{array}$ ⌈min $\{ \varrho ^ { l b } , \varpi ^ { l b } \} ] ) \} , N \}$ , otherwise,

where $\varpi ^ { l b }$ solves the below equation when the integrality constraint on ω is relaxed:

$$
\sum_ {r \in \mathcal {R}} (\beta \xi_ {r}) \left[ \frac {\partial \psi_ {r} \left(\frac {\beta \xi_ {r}}{T p _ {r} \omega}\right)}{\partial \left(\frac {\beta \xi_ {r}}{T p _ {r} \omega}\right)} \frac {\mathrm{d} \left(\frac {\beta \xi_ {r}}{T p _ {r} \omega}\right)}{\mathrm{d} \omega} \right] \Bigg | _ {\omega = \varpi^ {l b}} = - \frac {\partial \mathbb {E} _ {K _ {\omega}} [ g (K _ {\omega}) ]}{\partial \omega} \Bigg | _ {\omega = \varpi^ {l b}},
$$

and $\varrho ^ { l b } = \operatorname* { m i n } \{ \omega | f _ { 1 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega ) = f _ { 2 } ^ { \mathcal { T } } ( \beta \pmb { \xi } , \omega ) \}$

From Corollary 2 and Lemma 3, we have the following result.

Theorem 7. The proposed solution $\omega ^ { u p }$ achieves the following performance guarantee for problem ${ \mathcal { P } } ^ { \mathbb { Z } } ( \Omega ) { \mathrm { : } }$

$$
\frac {f _ {\mathcal {R}} ^ {\mathcal {I}} (\pmb {\xi} + z _ {\beta} \pmb {\xi} _ {o} , \omega^ {u p})}{f _ {\mathcal {R}} ^ {\mathcal {I}} (\beta \pmb {\xi} , \omega^ {l b})}.
$$

## 4. Managerial Implications and Discussions

Based on the results obtained in the previous section, we provide and discuss some managerial insights for the nonidentical ad exchanges and identical ad exchanges cases. We first discuss the results relating to the bidding policy. Next, we illustrate the impact of the entry of a new ad exchange on different players in the market. For the nonidentical ad exchanges case, we examine and discuss the impact of heterogeneity among ad exchanges on different players in the market. Finally, for the identical ad exchanges case, we investigate the impact of increase in the demand at a specific location on the ad firm’s total cost.

## 4.1. State-Independent Bidding Policy

Proposition 1 suggests that there exists an optimal bidding policy for the nonidentical ad exchanges case that is state independent. Proposition 2 shows this property holds for the bidding problem under the identical ad exchanges case as well. This is a nice property for the bidding policy, because the ad firm does not need to change its policy for a specific exchange-location combination either with time or with the number of impressions won. This property is especially helpful for reducing the response time for the bid requests. As mentioned in Section 1.1, when an impression arrives, the ad firm must typically respond with a bid amount in less than 100 ms to participate in the real-time auction. The response time restriction requires the ad firm to adopt a distributed bidding architecture with “master-slave” format to ensure that a technical failure of one server does not interrupt the bidding process. For such a distributed architecture, the state independent property allows the slave servers to bid largely independent from each other, without exchanging state information, thus saving the response time.

## 4.2. Effect of the Entry of a New Ad Exchange

An interesting question for the identical ad exchanges case is how the entry of a new ad exchange could economically impact the ad firm, the cloud provider, and the ad exchange market. In the following proposition, we analyze this effect.

Proposition 3. The entry of a new ad exchange can affect various players in the market in different ways.

(i) The ad firm’s total cost stays the same or decreases.

(ii) The cloud provider’s revenue stays the same or increases.

(iii) The total revenue earned from this ad firm by the ad exchange market stays the same or reduces.

The proof is provided in Online Appendix A. In the preceding proposition, we make certain analytical predictions when a new ad exchange enters a market consisting of multiple incumbent ad exchanges. The entry of a new ad exchange can never decrease the number of the ad exchanges which the ad firm works with before the entry of the new ad exchange. If the demand for an ad firm is low, then it stays with the same number of ad exchanges which it works with before the entry. Thus, the ad firm spends the same amount for procuring impressions and computing capacity, resulting in no change in the total cost of the ad firm, the cloud provider’s revenue, and the total revenue earned from this ad firm by the ad exchange market. When a new entry joins the market, an ad firm with sufficiently high demand will also work with the new ad exchange. Hence, the supply of impressions will increase, resulting in a reduction in the bidding cost and procurement cost of the ad firm. However, revenue earned from this ad firm by the ad exchange market will decrease. On the other hand, the capacity cost of the ad firm will increase, implying that the cloud provider will earn more revenue. From the previous discussion, the entry of a new ad exchange is beneficial for an ad firm with sufficiently high demand. The previous discussion could also be applicable for the nonidentical ad exchanges case.

Table 3 numerically illustrates the impact of the entry of a new ad exchange on the ad firm’s total cost, the cloud provider’s revenue, and the revenue earned from this ad firm by the ad exchange market. Assume there are two identical ad exchanges (ad exchanges 1 and 2) originally exist in the market (before the entry), and one ad exchange identical with the incumbent ad exchanges (ad exchange 3) enters the market. There exists an ad firm in this market that needs to procure the impressions to satisfy a sufficiently high demand at a specific location. We consider demand is equal to $\xi = 9 , 0 0 0$ . To win an impression arriving from the location via an ad exchange with probability y, the ad firm incurs the bidding cost equal to $7 . 5 \dot { y } ^ { 2 } .$ . The arrival probability of an impression (from each ad exchange) is $p _ { 1 } = 0 . 0 0 4 $ . The participation fee for each ad exchange is \$1,000. Assuming a time slot of duration 10 ms, our problem consists of $T = 8 , 6 4 0 , 0 0 0$ time slots. The capacity cost function is assumed to be $g ( K ) =$ $0 . 0 0 0 0 0 \mathrm { \stackrel { \cdot } { 0 0 0 1 } } K ^ { 2 }$ and the ad firm’s probabilistic delivery guarantee is $\beta = 0 . 9 9 9$ . Thus, $z _ { \beta } = 3 . 0 9$

Table 3. Impact of Entry of a New Ad Exchange

<table><tr><td></td><td>Before entry</td><td>After entry</td></tr><tr><td>Selected ad exchanges</td><td>{1,2}</td><td>{1,2,3}</td></tr><tr><td>Revenue of ad exchange market</td><td>$9,371</td><td>$6,247</td></tr><tr><td>Cloud provider&#x27;s revenue</td><td>$478</td><td>$1,075</td></tr><tr><td>Ad firm&#x27;s total cost</td><td>$9,849</td><td>$7,322</td></tr></table>

Before the entry of the new ad exchange 3, the ad firm works with both incumbent ad exchanges 1 and 2 and spends \$9,371 as procurement cost, generating the revenue of \$9,371 by the ad exchange market. The ad firm spends \$478 for purchasing cloud computing capacity. Hence, the ad firm incurs total cost \$9,849. After the entry, the ad firm finds it beneficial to procure the required supply of impressions from all three ad exchanges (ad exchanges 1–3), resulting in reducing the procurement cost to \$6,247 and ultimately reducing the revenue earned from this ad firm by the ad exchange market. However, the capacity cost increases, that is, the cloud provider’s revenue increases to \$1,075, decreasing the ad firm’s total cost to \$7,322. Therefore, the entry of a new ad exchange can be good for the ad firm with sufficiently high demand (total cost decreases), good for the cloud provider (cloud provider revenue increases), and not good for the ad exchange market (revenue earned from this ad firm by the ad exchange market reduces).

## 4.3. Effect of Participation Cost Heterogeneity Among Ad Exchanges

An interesting question for the nonidentical ad exchanges case is how heterogeneity in participation costs of the ad exchanges can affect the ad firm’s total cost. To address this question, let us consider a market where there are N ad exchanges that have the same bid-curve and arrival probability of an impression. The heterogeneity among the ad exchanges can be created by choosing nonidentical participation fees. Starting with identical participation fees (C), some of the exchanges can be chosen with fees above C, whereas the others can be chosen to have participation fees below C. To isolate the impact of heterogeneity, we ensure that the mean participation fee is C.

Consider an ad firm whose demand is sufficiently high such that if the demand was equally distributed across all N ad exchanges, the spending on bidding (S) in each ad exchange would be greater than the participation fee C. For such an ad firm, heterogeneity among the ad exchanges can be harmful. We explain the reason for this as follows: Suppose that one of the ad exchanges increases its participation fee to $C ^ { \prime } > C . \mathrm { I f } \ S < C ^ { \prime } .$ , the ad firm might not work with this ad exchange. If the ad firm does not work with this ad exchange, then, the ad firm must divide the same demand across a smaller number of the ad exchanges, resulting in a higher bidding cost spent in each of the $N - 1$ ad exchanges. This will hurt the ad firm by way of a higher cost to procure the same number of impressions. If the ad firm works with this ad exchange, then the bidding cost increases by $C ^ { \prime } - S .$ . On the other hand, if $( S > C ^ { \prime } )$ , the ad firm can continue to work with all N ad exchanges and the heterogeneity will have no impact on the cost incurred by the ad firm.

Next, consider an ad firm whose demand is sufficiently low such that it only works with one ad exchange and its spending on bidding (S) at that exchange is less than C. Thus, the ad firm’s procurement cost will be $\mathrm { m a x } ( S , C ) = C$ . For such an ad firm, heterogeneity can be beneficial. After introducing heterogeneity, assume that one the ad exchanges has a participation fee $C ^ { \prime \prime } < C$ . The procurement cost spent by the ad firm at this ad exchange will be $\operatorname* { m a x } ( S , C ^ { \prime \prime } ) < C ,$ , implying that the ad firm’s total cost will reduce. If $S > { \bar { C } }$ and the ad firm works with only one exchange, then heterogeneity will have no impact on the procurement cost.

Table 4 numerically illustrates the impact of the heterogeneity in the participation fees of the ad exchanges on the ad firm’s total cost. Assume there are four identi cal ad exchanges (ad exchanges 1, 2, 3, and 4) and one ad firm that needs to procure the impressions to satisfy the demand at a specific location. To win an impression arriving from the location via an ad exchange with probability y, the ad firm incurs the bidding cost equal to

Table 4. Impact of Heterogeneity Across Ad Exchanges

<table><tr><td rowspan="2"></td><td colspan="2">Big ad firm</td><td colspan="2">Small ad firm</td></tr><tr><td>Identical</td><td>Nonidentical</td><td>Identical</td><td>Nonidentical</td></tr><tr><td>Selected ad exchanges</td><td>{1,2,3,4}</td><td>{1,2,3,4}</td><td>{4}</td><td>{4}</td></tr><tr><td>Ad firm’s procurement cost</td><td>$8,260</td><td>$9,111</td><td>$2,000</td><td>$700</td></tr><tr><td>Ad firm’s capacity cost</td><td>$1,910</td><td>$1,910</td><td>$120</td><td>$120</td></tr><tr><td>Ad firm’s total cost</td><td>$10,170</td><td>$11,021</td><td>$2,120</td><td>$820</td></tr></table>

$7 . 5 y ^ { 2 }$ . The arrival probability of an impression (from each ad exchange) is $p _ { 1 } = 0 . 0 0 4$ . The participation fee for each ad exchange is \$2,000. Assuming a time slot of duration 10ms, our problem consists of $T = 8 , 6 4 0 , 0 0 0$ time slots. The capacity cost function is assumed to be $g ( K ) = 0 . 0 0 0 0 0 0 \dot { 1 } K ^ { 2 } .$ , and the ad firm’s probabilistic delivery guarantee is $\beta = 0 . 9 9 9$ . Thus, $z _ { \beta } = 3 . 0 9$ . We consider two scenarios here: a big ad firm with sufficiently high demand $( \mathrm { i } . \mathrm { e } . , \xi = 1 2 , 0 0 0 )$ and a small ad firm with low demand $( \mathrm { i . e . , } \xi = 1 , 5 0 0 )$ . For creating heterogeneity across ad exchanges, we increase the participation fee of ad exchange 1 from \$2,000 to \$5,000 and reduce the participation fee of ad exchange 2, 3, and 4 (respectively) from \$2,000 to \$1,300, \$1,000, and \$700.

When the participation costs of the ad exchanges become heterogeneous, the big ad firm finds it optimal to continue to work with the same set of ad exchanges as before. However, the ad firm’s procurement cost increases from \$8,260 to \$9,111, and its total cost also increases from \$10,170 to \$11,021. Similar to the big ad firm, the small ad firm continues to works with the same set of ad exchanges as before. However, this ad firm’s procurement cost decreases from \$2,000 to \$700, and its total cost also reduces from \$2,120 to \$820. Thus, broadly speaking, a more heterogeneous market (one in which the participation costs of the ad exchanges are different) tends to favor small ad firms but could hurt big ad firms.

## 4.4. Effect of Increase in Demand at a Particular Location

For the identical ad exchanges case, another useful insight can be obtained by examining the impact of increase in the demand at location r on the (near-optimal) total expected cost. We use this analysis to guide the ad firm to shape the demand at different locations; some locations are cheaper than others for the ad firm to meet demand. We start by introducing the following lemmas.

Lemma 4. For any given number of ad exchanges $\omega \in$ [1, N], the function $\bar { f } _ { 1 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega )$ is strictly increasing in ξ and strictly convex in $\xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } ,$ , ∀r ∈ R.

The proof is Provided in Online Appendix A. Holding the number of ad exchanges at ω, an increase in the demand at location r will cause an increase in the expected bidding cost at location r as well as the expected bidding cost. This is because the supply is fixed so the ad firm will need to bid more to win more impressions. However, the expected capacity cost will not change since the number of ad exchanges has been fixed. Therefore, when demand at location r increases, the expected total cost also increases in a convex manner.

Lemma 5. The function $\frac { \partial f _ { 1 } ^ { T } ( \pmb { \xi } _ { + z _ { \beta } } \pmb { \xi } _ { o } , \omega ) } { \partial ( \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } ) }$ is strictly decreasing in ω.

The proof is provided in Online Appendix A. When the ad firm works with more ad exchanges and the demand at location r increases, this extra demand gets distributed among more suppliers. Hence, the increase in the winning probability is smaller. Therefore, the expected bidding cost at location r and the expected bidding cost increase less.

Let $\zeta _ { \omega } ^ { r }$ denote the level of demand at location r where the expected bidding cost is equal to the sum of the participation fees of the ad exchanges, that is, $\zeta _ { \omega } ^ { r }$ is the solution to the equation $\begin{array} { r } { \sum _ { r \in \mathcal { R } } ( \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } ) \psi _ { r } \left( \frac { \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } } { T p _ { r } \omega } \right) = \omega C } \end{array}$ Therefore, for any given ω, we have $f _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega )$ equal to $f _ { 1 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega )$ , if $\xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } \ge \zeta _ { \omega } ^ { r } ,$ , and it is equal to $f _ { 2 } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega )$ , otherwise.

Lemma 6. When ω increases, the value of $\zeta _ { \omega } ^ { r }$ also increases.

The proof is provided in Online Appendix A. Finally, it is insightful to study the overall impact of increasing the demand at a particular location. This result is sum marized in the following proposition.

Proposition 4. When the demand at location $\boldsymbol { r } \in \mathcal { R } , \ \boldsymbol { \xi } _ { \boldsymbol { r } } ,$ increases

(i) If the participation fee is relatively large, the nearoptimal number of mobile ad exchanges $\bar { \omega } ^ { u p }$ stays the same. Otherwise, it increases.

(ii) If the participation fee is relatively large, the nearoptimal winning probability $\begin{array} { r } { y _ { r } ^ { * D } ( \omega ^ { u p } ) = \frac { \xi _ { r } + z _ { \beta } \sqrt { \xi _ { r } } } { T p _ { r } \omega ^ { u p } } } \end{array}$ increases. Otherwise it decreases.

(iii) The near-optimal expected total cost $f _ { \mathcal { R } } ^ { \mathcal { T } } ( \pmb { \xi } + z _ { \beta } \pmb { \xi } _ { o } , \omega ^ { u p } )$ stays the same or increases.

The proof is provided in Online Appendix A. Let us assume that the near-optimal number of mobile ad exchanges which the ad firm works with is one. This case happens when the spending at all locations (or equivalently the expected bidding cost) is below participation fee of an ad exchange. When demand at location r increases, there will be a level of demand at location r where the total spending at all locations is equal to the participation fee of the ad exchanges. Before this point, an increase in the demand at location r does not change the near-optimal number of ad exchanges. After that point, the expected bidding cost goes above the participation fee but it is still optimal for the ad firm to work with one ad exchange until the demand hits a point where the expected total cost of working with one ad exchange is equal to that of working with two ad exchanges. After this level of demand, the ad firm should work with two ad exchanges until the demand increases to a point where working with three ad exchanges is cheaper, and so on. Put differently, when the demand at location r increases, the ad firm works with more ad exchanges if the participation fee is not large. Therefore, the supply increases, implying that the ad firm can decrease the bidding cost by bidding a lower amount. However, the expected capacity cost increases.

Figure 1. (Color online) Expected Total Cost  
![](/api/attachments/9PUDTDX5/fulltext/images/5269c8efff64370fc81824d84d4bdb1448e268ff1c02085938dc2b77d9042918.jpg)

Figure 1 illustrates the value of Proposition 3 for shaping demand. We could imagine a figure like this for every location and consider the effect (on expected total cost) of increasing demand at a particular location. As can be seen from this figure, there are intervals where extra demand can be served at zero marginal cost. Otherwise, the extra demand incurs a marginal cost equal to the slope of the increasing cost curves. The ad firm can shape its demand using Figure 1; that is, it can attract demand at locations where the marginal cost is the lowest.<sup>11</sup>

## 5. Extensions

We consider two extensions to our model: The ad firm can choose a fraction of the supply of impressions from an ad exchange, and the arrival probabilities of impressions and bid curves are time dependent.

## 5.1. Selective Bidding in Procurement

The implicit assumption thus far has been that the ad firm must calculate a bid amount for all the bid requests received from an ad exchange. This means that the ad firm cannot choose a fraction of the supply from an ad exchange for calculating bids. If such flexibility existed, the ad firm could save on computing costs, but at the same time, would need to increase its bids because a fewer number of bidding opportunities would be available to meet the same demand for impressions. This raises the following optimization problem: What fraction of the bid requests should the ad firm consider for bid calculation to minimize expected total cost? We next analyze the impact of selective bidding strategy for the case of identical ad exchanges.

It is useful to establish that flexibility of the kind referred to previously is possible in practice. Recall, that ad exchanges require that for every bid request, a bid response is received within a specified time limit. However, a zero bid is acceptable. If a fraction of the bid requests are responded with a zero bid (using negligible computing resources, because generating a zero needs very little processing), it would mimic the idea of a selective bidding strategy, and possibly, lead to a reduction in expected total cost.

5.1.1. Selective Bidding Strategy. Figure 6 available in Online Appendix F depicts a new architecture to incorporate selective bidding strategy. When a bid request arrives, a new module (EFlex) either diverts the bid request for regular processing of a nonzero bid amount, or it simply returns a zero bid. A fraction $\rho$ of the bid requests are queued and dealt with as before; the fraction (1 � ρ) incurs no processing cost and is immediately returned with a zero bid.<sup>12</sup> We next formulate the bidding strategy and ad exchange selection problem in the presence of a selective bidding strategy. The optimization problem using a selective bidding strategy is described in Online Appendix C. It should be clear that the entire problem needs to be resolved.

5.1.2. Discussions and Implications. Several interesting results emerge in the presence of a selective bidding strategy. At a high level, a selective bidding strategy reduces supply side frictions caused by response time constraints. It also avoids wasted CPU cycles; the need to process something that is inefficient for the ad firm. Under a selective bidding strategy, the ad firm (weakly) benefits (lower expected total cost) because using the full supply from an ad exchange is always a feasible option. However, the impact of the ad exchange(s) and the cloud provider is mixed.

The following proposition describes the effect of a selective bidding strategy on the number of ad exchanges that the ad firm should work with.

Proposition 5. Selective bidding does not change the number of ad exchanges which the ad firm works with if th participation fee is relatively large; otherwise, the number increases.

## The proof is provided in Online Appendix A.

The previous proposition states that the number of ad exchanges can never decrease as a result of a selective bidding strategy. Clearly, when the supply fraction is equal to one, the ad firm should work with the same number of ad exchanges as the number when the entire supply is considered for bid computation. However, when the supply fraction is less than one, the number of the ad exchanges might increase or stay the same. However, the optimal number cannot decrease. The intuition behind this result is described here.

Let $\omega ^ { u p }$ be the optimal number of exchanges under the case where the entire supply is considered for bid computation. Under the case where a fraction of supply $( \mathrm { i . e . , } \rho ^ { \ast } < 1 )$ is considered for bid calculation and the rest $( \mathrm { i . e . , } 1 - \rho ^ { \ast } )$ is responded with zero bid amount, assume that the ad firm works with a fewer number of the ad exchanges, say $\omega ^ { u p } - 1$ . Because the supply fraction is less than one, the supply has reduced to a level below $\omega ^ { u p } - 1$ under the case where entire supply is considered. However, under the case where entire supply is considered, it was not optimal to use $\omega ^ { u p } - 1$ ad exchanges; instead, $\omega ^ { u p }$ ad exchanges were found to be optimal. Hence, a level of supply even below $\omega ^ { u p } - 1$ should not be optimal under the case where a fraction of supply is considered. Therefore, when the supply fraction is strictly less than one, the number of ad exchanges is the same or higher than the number that was optimal when the entire supply is considered. The last part of Proposition 4 deals with the role of the participation fee: When this fee is large, it is not beneficial to increase the number of ad exchanges.

We next examine the economic impact of selective bidding on the mobile in-app ad ecosystem.

Proposition 6. If the supply fraction is equal to one, there is no impact of selective bidding on the mobile in-app ad ecosystem. Otherwise, (the supply fraction is strictly less than one), selective bidding affects the various players in different ways.

(i) The ad firm is better off.

(ii) If the participation fee is relatively large, the cloud provider is worse off (less capacity is rented) and the ad exchanges are better off (expected bidding cost increases). Otherwise, the cloud provider is better off, and the ad exchanges are worse off.

The proof is provided in Online Appendix A.

If the optimal fraction, $\rho ^ { * }$ , is equal to one, then the number of ad exchanges does not change. Hence, the ad firm spends the same amount for buying impressions as well as computing capacity.

If the optimal fraction, $\rho ^ { * }$ , is less than one, Part (i) is trivial. When the participation fee is relatively large, then the ad firm works with the same number of the ad exchanges, resulting in a decrement in the supply of impressions. Therefore, expected capacity cost reduces and the cloud provider is worse off. However, the expected bidding cost increases, implying that the ad exchanges are better off.

The ad firm works with more ad exchanges when the participation fee is not large. Therefore, the supply increases, implying that the bidding cost decreases and the ad exchanges earn less. However, the expected capacity cost increases (cloud provider earns more).

## 5.2. Time-Dependent Arrivals and Win Probabilities

The arrival probabilities of impressions and the bid curves could also depend on the time of the day, in addition to the ad exchange and geographical location. In business districts, for instance, the arrival probability of impressions is likely to be higher during regular office hours. To address this probability, we now consider timedependent arrival probabilities and win-probabilities. We impose this generalization on our basic model in Section 2 of our paper.

We divide time horizon into several time blocks of time slots such that the bid curves and arrival probabilities of impressions remain unchanged during a time block but allow both to vary across time blocks. A time block includes many small time slots, each time slot’s length is a few milliseconds. We show that the bid amount (or equivalently win probability) for an impression arriving from location r via ad exchange i remains unchanged during a time block, but it changes across time blocks. The following explains more details for this extension to our paper.

Consider an arbitrary partition of the time horizon into B contiguous blocks of time slots: $\Delta _ { 1 } = [ 0 , t _ { 1 } ] .$ $\Delta _ { 2 } = [ t _ { 1 } , t _ { 2 } ] , \ldots , \Delta _ { B } = [ t _ { B - 1 } , t _ { B } ] ;$ thus, jth time-block $\Delta _ { j }$ starts at $t = t _ { j - 1 }$ and ends at $t = t _ { j } , j \in \{ 1 , 2 , \ldots , B \}$ , with $t _ { 0 } = 0$ and $t _ { B } = T$ . We assume that the arrival probability of impressions and the platform’s probability of winning an impression remain unchanged during a time block but allow both to vary across time blocks. Accordingly for $t \in \Delta _ { j . }$ , let $p _ { i , j , r }$ denote the arrival probability of an impression from location $r \in \mathcal { R }$ via ad exchange $i \in \Omega$ in time block $j , j \in \{ 1 , 2 , \dots , B \} _ { \cdot }$ ; we assume these probabili ties are independent. Similarly, for $t \in \Delta _ { j } ,$ , let $q _ { i , j , r } ( . )$ be the bid-curve; ${ \mathrm { i . e . , ~ } } q _ { i , j , r } ( \psi )$ is the win-probability of an impression from location r via ad exchange i in time block j when bid $\psi$ is placed. Thus, during time block $\Delta _ { j } ,$ the bid curve is $\overset { \cdot } { \psi } _ { i , j , r } \overset { \cdot } { ( } y ) = q _ { i , j , r } ^ { - 1 } ( y )$ and $h _ { i , j , r } ( y ) = y \psi _ { i , j , r }$ $( y ) , y \in [ 0 , 1 ]$ , is the expected cost of ensuring a win probability of y at location r via ad exchange i.

Let $\mathcal { P } _ { \Delta } ( \beta , W )$ denote the bidding problem with these time-dependent arrival and win probabilities. Keeping the remainder of the notation the same as that in Section $^ { 2 , }$ we can formulate this problem as follows.

Problem $\mathcal { P } _ { \Delta } ( \beta , W )$

$$
\begin{array}{l} \min _ {\pi (W)} \sum_ {i \in W} m a x \Bigg \{\sum_ {j = 1} ^ {B} \sum_ {t \in \Delta_ {j}} \sum_ {r \in \mathcal {R}} p _ {i, j, r} \mathbb {E} _ {\mathbf {S} _ {t} ^ {\pi (W)}} \\ \left[ h _ {i, j, r} \left(y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right)\right) \right], C _ {i} \Bigg \} + \mathbb {E} _ {K _ {W}} [ g (K _ {W}) ], \end{array}
$$

subject to

$$
\mathbb {P} [ S _ {r, T + 1} ^ {\pi (W)} \geq \xi_ {r} ] \geq \beta , \quad \forall r,\tag{18}
$$

$$
y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right) \in [ 0, 1 ], \quad \forall i, r, s _ {t} ^ {\pi (W)}, t \in \Delta_ {j}, j = 1, 2, \dots , B.\tag{19}
$$

The analysis of this problem is similar to that in Section 2. Similarly, we first convert this probabilistic problem into a problem with expectation constraint, then we calculate the optimal solution of problem with expectation constraint and modified buffer such that the optimal solution is a feasible solution for our original problem with probabilistic constraint.

The following problem is relaxation of our original problem, where the probabilistic constraint is substitute with expectation constraint.

Problem $\mathcal { P } _ { \Delta _ { R } } ( \pmb { \alpha } , W )$

$$
\begin{array}{l} \min _ {\pi (W)} \sum_ {i \in W} m a x \Bigg \{\sum_ {j = 1} ^ {B} \sum_ {t \in \Delta_ {j}} \sum_ {r \in \mathcal {R}} p _ {i, j, r} \mathbb {E} _ {\mathbf {s} _ {t} ^ {\pi (W)}} \\ \left[ h _ {i, j, r} \left(y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right)\right) \right], C _ {i} \Bigg \} + \mathbb {E} _ {K _ {W}} [ g (K _ {W}) ], \end{array}
$$

subject to

$$
\sum_ {i \in W} \sum_ {j = 1} ^ {B} \sum_ {t \in \Delta_ {j}} p _ {i, j, r} \mathbb {E} _ {\mathbf {S} _ {t} ^ {\pi (W)}} \left[ y _ {t, i, r} ^ {\pi (W)} \left(t, \mathbf {s} _ {t} ^ {\pi (W)}\right) \right] \geq \alpha_ {r}, \quad \forall r,\tag{20}
$$

$$
y _ {t, i, r} ^ {\pi (W)} (t, \mathbf {s} _ {t} ^ {\pi (W)}) \in [ 0, 1 ], \quad \forall i, r, s _ {t} ^ {\pi (W)}, t \in \Delta_ {j}, j = 1, 2, \dots , B.\tag{21}
$$

To find the optimal solution for problem with expectation constraint (problem $\mathcal { P } _ { \Delta _ { R } } ( { \pmb { \alpha } } , { \bar { W } } ) )$ , we introduce a deterministic problem, explained in Online Appendix $\scriptstyle \mathrm { E , }$ that its equivalent to problem with expectation constraint (i.e., problem $\bar { \mathcal { P } } _ { \Delta _ { R } } ( \pmb { \alpha } , W ) )$ . This means that the optimal solution of the deterministic problem is also optimal solution for problem $\mathcal { P } _ { \Delta _ { R } } ( \pmb { \alpha } , W )$

A near-optimal solution to problem ${ \mathcal { P } } _ { \Delta } ( \beta , W )$ : Given that the arrival and winning probabilities change across time block and do not change during a time-block, it is natural to aim for a policy with the following structure: For a given combination of ad exchange and location (i, r), the ad firm maintains the same win-probability throughout a time-block but (possibly) changes this probability across time blocks. Formally, the structure of the desired policy, which we denote by $\pi _ { \Delta } ^ { \beta } ( W )$ , is as follows:

$$
\begin{array}{l} \pi_ {\Delta} ^ {\beta} (W) := y _ {t, i, r} ^ {\pi_ {\Delta} ^ {\beta} (W)} \left(t, \mathbf {s} _ {t} ^ {\pi_ {\Delta} ^ {\beta} (W)}\right) = y _ {i, j, r} ^ {* \mathcal {D}}, \\ \forall t \in \Delta_ {j}, j = \{1, 2, \ldots , B \}, i \in W, r \in \mathcal {R}, \end{array}\tag{22}
$$

such that $\mathbb { P } [ S _ { r , T + 1 } ^ { \pi ( W ) } \geq \xi _ { r } ] \geq \beta ,$ , ∀r.

Under the policy $\pi _ { \Delta } ^ { \beta } ( W )$ , the total number of impressions won during each time block $\Delta _ { j }$ from location r is a binomially distributed random variable with a trial success probability of $\begin{array} { r } { \gamma _ { j , r } = \sum _ { i \in W } p _ { i , j , r } y _ { i , j , r } , \forall r \in \mathcal { R } } \end{array}$ . Thus, the random variable $\mathbf { S } _ { r , T + 1 } ^ { \pi _ { \Delta } ^ { \beta } ( W ) }$ , which represents the number of impressions won over the T time slots from location r is the sum of B independent binomially distributed random variables that each represents the impressions won over the corresponding time block.

Assuming that each time block consists of a sufficiently large number of time slots, we can apply the central limit theorem to use a normal approximation of the binomial distribution for each time block. Thus, the ran dom variable $\mathbf { S } _ { r , T + 1 } ^ { \pi _ { \Delta } ^ { \beta } ( W ) }$ is approximately normally distributed with mean $\begin{array} { r } { \sum _ { j = 1 } ^ { B } | \Delta _ { j } | \gamma _ { j , 1 } } \end{array}$ r and variance $\sum _ { j = 1 } ^ { B } | \Delta _ { j } |$ $\gamma _ { j , r } ( 1 - \gamma _ { j , r } )$ . Because we want $\mathbb { P } [ S _ { r , T + 1 } ^ { \pi ( W ) } \geq \xi _ { r } ] \geq \beta ,$ , ∀r, we have

$$
\Phi_ {N} \left(\frac {\sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j , r} - \xi_ {r}}{\sqrt {\sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j , r} (1 - \gamma_ {j , r})}}\right) = \beta ,
$$

where $\Phi _ { N } ( . )$ is the cumulative distribution function of the standard normal distribution. Thus, we get

$$
\left(\sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j, r} - \xi_ {r}\right) ^ {2} = z _ {\beta} ^ {2} \left(\sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j, r} (1 - \gamma_ {j, r})\right),
$$

where $z _ { \beta } = \Phi _ { N } ^ { - 1 } ( \beta )$ . Using steps similar to those in Section 3.1.1, we obtain the following approximate of $\begin{array} { r } { \sum _ { j = 1 } ^ { B } | \Delta _ { j } | \gamma _ { j , r } ; } \end{array}$

$$
\sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j, r} \approx \xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}.
$$

Thus, under the policy $\pi _ { \Delta } ^ { \beta } ( W )$ , the expected number of impressions won from location r is

$$
\alpha_ {r} ^ {\prime} = \sum_ {j = 1} ^ {B} | \Delta_ {j} | \gamma_ {j, r} \approx \xi_ {r} + z _ {\beta} \sqrt {\xi_ {r}}.
$$

The amount $z _ { \beta } \sqrt { \xi _ { r } }$ is the additional amount (or buffer) that the static policy needs to plan for to ensure that at least $\xi _ { r }$ impressions are won from location r with probability $\beta .$ Therefore, for the choice ${ \pmb { \alpha } } = { \pmb { \xi } } + z _ { \beta } { \pmb { \xi } } ,$ , the optimal policy of problem $\mathcal { P } _ { \Delta _ { R } } ( \pmb { \alpha } , W )$ is a feasible solution for problem $\bar { \mathcal { P } } _ { \Delta } ( \beta , W )$ . In the proposed policy, all the ad space arriving from the same location and via the same ad exchange during a time block are procured at the same price but are procured at different prices across time blocks. Once the bidding strategy is found, we can study it as before within the larger, ad exchange selection problem as explained in Sections 3.2 and 3.2.1 and obtain the solution.

Example with time dependence: At this point, it is instructive to explain our proposed bidding policy using a simple and illustrative example. Let us consider the following example: There is one ad exchange and one location. The demand at the specified location can be a number in the following interval, that is, $\xi \in [ 2 , 0 0 0 , 1 4 , 0 0 0 ]$ . That is, the ad firm needs to win at least ξ impressions at the location with a probability of $\beta$ or more, within a time duration of 24hours. The ad delivery’s probabilistic guarantee is $\beta = 0 . 9 9 9$ . Thus, $z _ { \beta } = 3 . 0 9$ . The participation fee for the ad exchange is \$1, 500. We consider the total number of time slots equal to $T = 8 , 6 4 0 , 0 0 0$ . Each time slot is of duration 10 ms. We consider two time blocks: the first time block, that is, $\Delta _ { 1 } ,$ starts at 6:00 a.m. and ends at 6:00 p.m.; the second time block, that is, $\Delta _ { 2 } ,$ starts at 6:00 p.m. and ends at 6:00 a.m. Therefore, each time block includes 4,320,000 time slots. We consider three scenarios: under scenario 1, the probability that an impression arrives during the first and second time block is 0.002 and 0.004, respectively; under scenario 2, the probability that an impression arrives during the first and second time block is 0.004 and 0.002, respectively; and under scenario $^ { 3 , }$ the probability that an impression arrives during the first and second time block is 0.002 and 0.002, respectively. As shown in Figure 2(b), for scenarios 1 and $^ { 2 , }$ we define the expected bidding cost for winning an impression during the first time block as $\begin{array} { r } { h ( y ) = \left( \frac { y } { 2 . 7 8 6 } \right) \ln \left( \frac { 0 . 9 8 3 y + 0 . 0 1 7 } { 1 - \left( 0 . 9 8 3 y + 0 . 0 1 7 \right) } \right) + \frac { 4 . 0 4 1 y } { 2 . 7 8 6 } , } \end{array}$ , and the expected bidding cost for winning an impression during the second time block as $\begin{array} { r } { \bar { h } ( y ) = \left( \frac { \bar { y } } { 2 . 1 5 2 } \right) } \end{array}$ ln $\begin{array} { r } { \left( \frac { 0 . 8 8 y + 0 . 1 2 } { 1 - ( 0 . 8 8 y + 0 . 1 2 ) } \right) + \frac { 1 . 9 9 7 y } { 2 . 1 5 2 } . } \end{array}$ . As shown in Figure 2(b), for scenario $^ { 3 , }$ we consider the expected bidding cost during the first time block as $\begin{array} { r } { h ( y ) = \big ( \frac { y } { 2 . 9 3 9 } \big ) \ln \Big ( \frac { 0 . 9 7 7 y + 0 . 0 2 3 } { 1 - ( 0 . 9 7 7 y + 0 . 0 2 3 ) } \Big ) \ + } \end{array}$ + $\frac { 3 . 7 3 9 y } { 2 . 9 3 9 }$ and the expected bidding cost for the second time block as $\begin{array} { r } { h ( y ) = \left( \frac { y } { 1 . 4 8 9 } \right) \ln \left( \frac { 0 . 7 9 4 y + 0 . 2 1 } { 1 - \left( 0 . 7 9 4 y + 0 . 2 1 \right) } \right) + \frac { 1 . 3 5 y } { 1 . 4 8 9 } . } \end{array}$

Figure 2. (Color online) Expected Bidding Costs for Three Scenarios  
(a)  
![](/api/attachments/9PUDTDX5/fulltext/images/44fb143162a81bd8931b1d5ccc69df36148a0b7c8de04e405923209c9ee6a01f.jpg)  
Notes. (a) Scenario 1 and 2. (b) Scenario 3.

As shown in Figure 3(a), under scenario 1, the expected bidding cost during the first time block is always greater than the expected bidding cost during the second time block and more supply of impressions arrive during the second time block. When demand is low, that is, $\xi = 2 , 0 0 0$ , the ad firm buys no impressions during the more expensive, first time block. Hence, the ad firm chooses win probability zero, or equivalently bid amount zero during the first time block. Therefore, the ad firm needs to buy all the required number of impressions from the second, cheaper time block. However, as the demand increases, the arriving numbers of impressions during the cheaper time block are not enough anymore to satisfy the required demand. Hence, the ad firm needs to divide the required demand between both time blocks and procure some impressions from the more expensive, first time block. It is notable that the ad firm always procures more impressions from the cheaper time block and chooses a higher win probability, or equivalently, higher bid amount for the cheaper time block.

As shown in Figure 3(b), under scenario 2 where the expected bidding cost and supply of arriving impressions are always greater during the first time block, when demand is low, that is, $\xi = 2 , 0 0 0$ , despite scenario 1, the ad firm buys the required impressions from both time blocks and picks nonzero win probabilities. In this scenario, the arriving supply of impressions during the cheaper time block is not high enough to satisfy even the low level of demand. Similar to scenario 1, as the demand increases, the numbers of impressions that ad firm procures from the more expensive time block increases, but the ad firm always buys more impressions from the cheaper time block and chooses a higher win probability or equivalently higher bid amount for the cheaper time block.

(b)  
![](/api/attachments/9PUDTDX5/fulltext/images/fe07c02f69566c5e222b894d183c86d51e88e50a386a86a1f31b6dbd634b6418.jpg)

Figure 3. (Color online) Selected Win Probabilities for a Given Demand  
(a)  
![](/api/attachments/9PUDTDX5/fulltext/images/63d0fb802d8aa104bdfe6e3008b2e81aaae00364fb553da6de2e1329775f2ffd.jpg)  
Notes. (a) Scenario 1. (b) Scenario 2. (c) Scenario 3.

(b)  
![](/api/attachments/9PUDTDX5/fulltext/images/c1abee25555309b27f0f3a01affa997efdc596a4118227894424773cd7567760.jpg)

As shown in Figure $3 ( \mathrm { c } ) ,$ , under scenario $^ { 3 , }$ the expected bidding cost during the first time block can sometimes be cheaper than the expected bidding cost during the second time block. When demand is low, that is, $\xi =$ 2,000, similar to scenario 2, the ad firm buys the required impressions from both time blocks and picks nonzero win probabilities. As the demand increases, but stays below a specific level, the number of impressions that the ad firm procures from the more expensive, first time block, is less than the number of impressions procured from the second time block. However, as the demand increases beyond the specified level, the first time block becomes the cheaper one, and the ad firm buys more impressions from the first time block and chooses a higher win probability or equivalently higher bid amount for the first time block.

## 6. Case Study

To lend further credibility to our study, we obtained data from an ad firm (Cidewalk) and evaluated the benefits of using our approach for this firm. Cidewalk is in the business of running mobile in-app ad campaigns for small- to medium-sized firms. The firm currently procures impressions from ad exchange A but is evaluating the possibility of also using ad exchange B to procure its supply.<sup>13</sup> We demonstrate the use of our study to help Cidewalk evaluate the previous decision.

The parameters for Cidewalk’s problem are as follows: For a weekly planning horizon and a time slot of 10 ms, $T = 6 0 , 4 8 0 , 0 0 0 .$ Cidewalk’s probabilistic guarantee for satisfying a campaign is $\beta = \bar { 0 } . 9 9 9$ . The participation fees of ad exchanges A and B are \$5,000 and \$7,000, respectively. We consider six major locations where Cidewalk operates, $L = 6$ (locations are denoted as $1 - 6 )$ . The (weekly) demand (number of impressions needed) at each location is $( \xi _ { 1 } , \xi _ { 2 } , \xi _ { 3 } , \xi _ { 4 } , \xi _ { 5 } , \hat { \xi _ { 6 } } ) = ( 9 1 3 2 , 6 3 1 9 , 8 4 1 2 , $ 6621, 8101, 7507). An impression arrives from locations $1 - 6$ via ad exchange A with the following probabili ties: $( p _ { \mathcal { A } , 1 } , p _ { \mathcal { A } , 2 } , p _ { \mathcal { A } , 3 } , p _ { \mathcal { A } , 4 } , p _ { \mathcal { A } , 5 } , p _ { \mathcal { A } , 6 } ) = ( 0 . 0 4 1 , 0 . 0 2 9 , 0 . 0 3 6 ,$ 0:040, 0:027, 0:032). Similarly, for ad exchange $B ,$ the arrival probabilities are $( p _ { B , 1 } , p _ { B , 2 } , p _ { B , 3 } , p _ { B , 4 } , p _ { B , 5 } , p _ { B , 6 } ) =$ $( 0 . 0 2 1 , 0 . 0 3 2 , 0 . 0 2 3 , 0 . 0 2 5 , 0 . 0 2 4 , 0 . 0 1 8 )$ . We use logistic regression to estimate the expected bidding cost $h _ { i , r } ( y )$ (of ensuring a win probability of y at ad exchange i and location r) for two ad exchanges and six locations (12 combinations in all; see Online Appendix H for more details). Tables 5 and 6 available in Online Appendix H present the descriptive statistics for variables in all 12 models. We obtain the expected bidding cost function for exchangelocation $( i , r )$ using the relation $h _ { i , r } ( \psi ) = y _ { i , r } \psi _ { i , r } ( y )$ , where $\psi _ { i , r } ( y )$ , that ${ \mathrm { i } } s ,$ the bid curve, is the inverse function of $y _ { i , r } ( . )$ . This expected bidding cost function is of the form

(c)  
![](/api/attachments/9PUDTDX5/fulltext/images/3e5c262b9a30be50a70984ab516f4ace2ecffbbbcd1f0191090c727edf01dd4c.jpg)

$$
h _ {i, r} (y) = \frac {y}{\kappa_ {1} ^ {i , r}} \ln \left(\frac {y (1 - y _ {0} ^ {i , r}) + y _ {0} ^ {i , r}}{1 - y (1 - y _ {0} ^ {i , r}) - y _ {0} ^ {i , r}}\right) - \frac {y \kappa_ {0} ^ {i , r}}{\kappa_ {1} ^ {i , r}}, \quad \forall i, r,
$$

where $\kappa _ { 0 } ^ { i , r }$ and $\kappa _ { 1 } ^ { i , r }$ are presented in Tables 7 and 8 available in Online Appendix H, and $\begin{array} { r } { y _ { 0 } ^ { i , r } = \frac { e ^ { \kappa _ { 0 } ^ { i , r } } } { 1 + e ^ { \kappa _ { 0 } ^ { i , r } } } . } \end{array}$ . The data show that the expected bidding cost of each exchange location $( i , \ r ) ,$ , that is, $h _ { i , r } ( . )$ , is strictly increasing and convex, consistent with our assumption in Section 2. Figure 4 plots the expected bidding cost for winning an impression arriving from ad exchange A and location $r = 6$ with probability y. For exchange-location $( A , r )$ , ∀r $\in \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ , the expected bidding cost function is

$$
h _ {A, r} (y) = \frac {y}{\kappa_ {1} ^ {A , r}} \mathrm{ln} \left(\frac {y (1 - y _ {0} ^ {A , r}) + y _ {0} ^ {A , r}}{1 - y (1 - y _ {0} ^ {A , r}) - y _ {0} ^ {A , r}}\right) - \frac {y \kappa_ {0} ^ {A , r}}{\kappa_ {1} ^ {A , r}},
$$

where $( \kappa _ { 0 } ^ { A , 1 } , \kappa _ { 0 } ^ { A , 2 } , \kappa _ { 0 } ^ { A , 3 } , \kappa _ { 0 } ^ { A , 4 } , \kappa _ { 0 } ^ { A , 5 } , \kappa _ { 0 } ^ { A , 6 } ) = ( - 4 . 0 4 0 5 8 , - 3 . 7 3 9 3 ,$ $- 1 . 9 9 6 8 8 , \allowbreak - 1 . 3 5 0 4 4 , \allowbreak - 1 . 6 1 7 1 5 , \allowbreak - 0 . 7 5 7 6 5 )$ and $( \kappa _ { 1 } ^ { A , 1 } , \kappa _ { 1 } ^ { A , 2 } , \kappa _ { 1 } ^ { A , 3 } .$

Figure 4. (Color online) Expected Bidding Cost of Ensuring a Win Probability y at Ad Exchange A and Location 6  
![](/api/attachments/9PUDTDX5/fulltext/images/36c74a86769d3ad6903cc3bf8314ada25af5e6318b5344803cac17ae6270c0b2.jpg)  
$\kappa _ { 1 } ^ { A , 4 } , \kappa _ { 1 } ^ { A , 5 } , \kappa _ { 1 } ^ { A , 6 } ) = ( 2 . 7 8 5 8 ,$ 2:9393, 2:15227, 1:48896, 1:76308, 0:64176).

For exchange-location $( B , r ) , \forall r \in \{ 1 , 2 , 3 , 4 , 5 , 6 \}$ , the expected bidding cost function is

$$
h _ {B, r} (y) = \frac {y}{\kappa_ {1} ^ {B , r}} \ln \left(\frac {y (1 - y _ {0} ^ {B , r}) + y _ {0} ^ {B , r}}{1 - y (1 - y _ {0} ^ {B , r}) - y _ {0} ^ {B , r}}\right) - \frac {y \kappa_ {0} ^ {B , r}}{\kappa_ {1} ^ {B , r}},
$$

where $( \kappa _ { 0 } ^ { B , 1 } , \kappa _ { 0 } ^ { B , 2 } , \kappa _ { 0 } ^ { B , 3 } , \kappa _ { 0 } ^ { B , 4 } , \kappa _ { 0 } ^ { B , 5 } , \kappa _ { 0 } ^ { B , 6 } ) = ( - 0 . 8 9 4 4 1 , - 2 . 3 2 8 5 3 ,$ $0 . 6 6 1 3 2 , - 0 . 1 3 5 4 6 , 0 . 2 2 0 1 , - 0 . 4 8 8 )$ and $( \kappa _ { 1 } ^ { B , 1 } , \kappa _ { 1 } ^ { B , 2 } , \kappa _ { 1 } ^ { B , 3 } , \kappa _ { 1 } ^ { B , 4 } ,$ $\kappa _ { 1 } ^ { B , 5 } , \kappa _ { 1 } ^ { B , 6 } ) = ( 1 . 5 9 1 6 , 4 . 3 4 5 9 , 0 . 1 7 4 2 4 , 0 . 5 3 0 6 4 , \hat { 0 } . 7 1 0 \dot { 4 } , 1 . \dot { 1 } 7 4 3 5 ) .$

Using the data obtained from Cidewalk’s weekly bill for AWS services, the cost of renting the capacity needed to respond to K bid requests within an the acceptable time limit of 100 ms is $\dot { g ( K ) } = 2 9 . 7 8 ( e ^ { 3 \times 1 0 ^ { - 7 } K } - 1 )$ , which is strictly increasing and convex in the number of bid requests in a week; consistent with our assumption in Section 2. For estimating the capacity cost function, we tried to fit a linear, polynomial, or exponential curve on the data points, where the dependent variable is the capacity cost and independent variable is the volume of arriving bid requests. The results show that an exponential curve fits better with the data $( R ^ { 2 } = 0 . 8 9 )$ than a linear or polynomial form. For estimating the parameters in exponential form (exponential (i.e., $g ( K ) =$ $\alpha \mathrm { e x p } ^ { \beta K } + \gamma ) )$ , we first linearize it by taking the Log of both sides $( \mathrm { i . e . , } l o g ( g ( K ) - \gamma ) = l o g ( \dot { \alpha } ) + \beta K )$ and then fitting a linear model. We evaluate Cidewalk’s expected total cost (procurement cost + computing cost) under three different cases, corresponding to the set of ad exchanges used to procure impressions: (1) $\Omega = \{ { \mathcal A } \}$ , (2) $\Omega = \{ B \bar  \}$ , and $( 3 ) \bar { \Omega = } \{ \mathcal { A } , B \}$

The expected bidding cost, expected capacity cost, and expected total cost of each scenario are reported in Table 5, and the winning probabilities are reported in Table 6.

Table 5. Cidewalk’s Expected Costs for Different Sourcing Options

<table><tr><td></td><td> $\Omega = \{ \mathcal{A} \}$ </td><td> $\Omega = \{ \mathcal{B} \}$ </td><td> $\Omega = \{ \mathcal{A}, \mathcal{B} \}$ </td></tr><tr><td>Expected bidding cost ($)</td><td>43,456</td><td>46,604</td><td>16,453</td></tr><tr><td>Expected capacity cost ($)</td><td>1,199</td><td>370</td><td>16,418</td></tr><tr><td>Expected total cost ($)</td><td>44,655</td><td>46,974</td><td>32,871</td></tr></table>

The results show that if Cidewalk would like to use only one ad exchange, then it is better to use ad exchange A over ad exchange B. This choice results in an expected total cost of \$44,655 versus a cost of \$46,974 when ad exchange B is exclusively used. However, using both exchanges is the cheapest option (\$32,871, representing approximately a 26% reduction in expected total cost over the option of exclusively using A to procure impressions) among the three possibilities that were evaluated. As seen in Table 5, using both exchanges indeed increases computing cost, but this cost increase is more than offset by the substantial reduction in bidding cost. In summary, we recommend that Cidewalk will benefit substantially from working with both ad exchanges.

We now ask the following: Can Cidewalk further reduce costs using the idea of selective bidding that was discussed earlier? We study this question using ten levels of fractional supply, $\bar { \rho } = ( 0 . 1 , \bar { 0 } . 2 , 0 . 3 , 0 . 4 , 0 . \bar { 5 } , 0 . 6 ,$ $0 . 7 , 0 . 8 , 0 . 9 , 1 )$ . As shown in Figure 5, among the options evaluated, we see that cheapest option is to use 90% of the supply from ad exchanges A and B. The selective bidding strategy reduces the expected total cost to \$29,015 (the expected bidding cost incurred is \$20, 297 and the expected capacity cost is \$8, 718), representing an approximately 12% reduction in expected total cost over the option of using the full supply from both ad exchanges. As opposed to the full supply option $( \rho = 1 )$ under optimal selective bidding $( \rho = 0 . 9 )$ , Cidewalk spends more on bidding cost, but this increase is offset by a greater reduction in capacity cost. Selective bidding has a beneficial impact on both ad exchanges, but the cloud provider is worse off (earns less revenue). Overall, the combination of the ideas proposed in the paper (optimal set selection and optimal selective bidding), provides a 33% reduction in Cidewalk’s expected total cost over the current option of sourcing all its impressions from ad exchange A. Interestingly, only a small change in the operating policy can lead to significant savings: obtained by procuring impressions from one additional ad exchange and by filtering out $( \mathrm { i . e . , }$ not bidding on) 10% of the arriving impressions. The company is considering the possibility of implementing our approach.<sup>14</sup>

## 7. Conclusions

We study the procurement problem of a mobile ad firm that works with many advertisers over many different locations (e.g., zipcodes). The firm’s goal is to minimize the expected total cost of campaign execution: (1) the cost to win impressions (expected bidding cost) while respecting the spending (participation) constraint associated with each ad exchange and (2) the expected capacity cost: the information technology cost needed to run the bidding architecture. There are two key decision variables in the problem: (1) the bidding policy to use at each location-exchange and (2) the set of ad exchanges to use to procure impressions.

Table 6. Winning Probabilities for Different Sourcing Options

<table><tr><td rowspan="2">Location</td><td rowspan="2"> $\Omega = \{ \mathcal{A} \}$ Ad exchange  $\mathcal{A}$ </td><td rowspan="2"> $\Omega = \{ \mathcal{B} \}$ Ad exchange  $\mathcal{B}$ </td><td colspan="2"> $\Omega = \{ \mathcal{A},\mathcal{B} \}$ </td></tr><tr><td>Ad exchange  $\mathcal{A}$ </td><td>Ad exchange  $\mathcal{B}$ </td></tr><tr><td>1</td><td>0.0038</td><td>0.0074</td><td>0.0011</td><td>0.0053</td></tr><tr><td>2</td><td>0.0037</td><td>0.0034</td><td>0.0005</td><td>0.0030</td></tr><tr><td>3</td><td>0.0040</td><td>0.0063</td><td>0.0034</td><td>0.0009</td></tr><tr><td>4</td><td>0.0028</td><td>0.0045</td><td>0.0022</td><td>0.0011</td></tr><tr><td>5</td><td>0.0051</td><td>0.0058</td><td>0.0025</td><td>0.0030</td></tr><tr><td>6</td><td>0.0040</td><td>0.0071</td><td>0.0024</td><td>0.0029</td></tr></table>

Despite several complex features in the problem (random arrival of bid requests, time-constrained delivery commitments for each campaign, participation fees imposed by ad exchanges, etc.), we show that the bidding policy for any exchange-location combination is static; a constant bid for each exchange location is near optimal. This constant bid is easy to implement in a distributed bidding architecture, that is common to many bidding platforms. Next, the problem of ad exchange selection was solved using a near-optimal algorithm using an enhanced hill climbing policy. The algorithm starts with an empty set and then iteratively adds an ad exchange to the existing set. During each round, we pick the ad exchange that maximizes the ratio of the saved bidding cost and the increased participation fee and capacity cost. The algorithm is shown to have polynomial time complexity and a bounded approximation ratio. We also show for a given number of nonidentical ad exchanges in the market, a more heterogeneous market (one in which the participation costs of the ad exchanges are different) leads to a higher total cost for a big ad firm, but a lower total cost for a small ad firm. Thus, big ad firms can hurt from the heterogeneity of ad exchanges. However, the heterogeneity can be a friend for small ad firms.

We also focused on the special case of the problem where the ad exchanges were identical. The near-optimal solution to a special problem was found to be useful to develop the solution for the general problem. We could also provide some structural insights for the special case. (1) Depending on participation fee, the near-optimal bid and the near-optimal number of ad exchanges act as weak complements or as substitutes. (2) When a new ad exchange enters the market, the ad firm and cloud provider could benefit, but the total revenue earned from the ad firm by the ad exchange market stays the same or reduces. (3) The expected total cost structure exhibits a staircase-like pattern that can be exploited to shape the demand in a way that it can be stimulated more at cheaper locations.

Finally, a new procurement strategy was studied that allowed the ad firm to consider a fraction of the bid requests arriving from the ad exchanges. This “selective bidding strategy” avoided wasteful bid request processing by returning a zero bid without examining the contents of a bid request. In some cases, this reduced capacity cost, and despite the increase in the bidding cost, it reduced expected total cost. Overall, we found that relatively large participation fees protected ad exchanges in the presence of selective bidding. On the other hand, when these fees were low, the cloud providers benefited. Essentially, both participation fees and considering entire supply imposed by ad exchanges act as market frictions. We devised a method to reduce the friction from full supply consideration using a selective bidding strategy. The other friction, namely, the participation fee continues to act as a friend for the ad exchanges.

Figure 5. (Color online) Three Cost Components for Working with Both Ad Exchanges A and B  
![](/api/attachments/9PUDTDX5/fulltext/images/3265dc15208502fda0b9339ddb95d2432fefe009735f951737ff2fa4a4c54ce8.jpg)

![](/api/attachments/9PUDTDX5/fulltext/images/5f37467b8a0fa87a91d0273a687e826aa641629682ab666d4ac441fe75e74df2.jpg)

![](/api/attachments/9PUDTDX5/fulltext/images/002664a366578708eb928bcba63ca04b3d3c73f54dfcc06f1654dcd8399d3864.jpg)

Future research could study more complex revenue side arrangements between the ad firm and the advertisers. For example, the ad firm could offer a plan where the number of impressions delivered (for a fixed price) would be a function of the geographical concentration; fewer impressions would be delivered in a more concentrated area. This contract is being considered by ad firms in their attempt to offer geo-fencing services. Another idea that is being considered by ad firms is to offer costper-click plans in addition to cost-per-impression plans. A cost-per-click plan would influence the bidding strategy of the ad firm: presumably, the bid for an impression with a higher likelihood of a click would have to adjusted upward.

## Endnotes

<sup>1</sup> In Section 5.1, we present a selective bidding strategy that lowers the friction caused by response time constraints and analyze its impact on the ad firm, the ad exchange(s) and the cloud provider.

<sup>2</sup> More details of the architecture are available in Online Appendix G.

<sup>3</sup> The service time is itself deterministic, regardless of capacity adjustment. This is because all bid requests are identical. On the other hand, the randomness in the waiting time is absorbed by realtime adjustments to the capacity.

<sup>4</sup> Cidewalk (https://www.cidewalk.com/), GroundTruth (https:// www.groundtruth.com/), Taboola (https://www.taboola.com/), AdButler (https://www.adbutler.com/), and ExactDrive (https:// www.exactdrive.com/).

<sup>5</sup> Other types of contracts between an ad firm and advertisers exist in practice. For example, an advertiser can specify a budget to the ad firm and hope to receive as many impressions as possible such that the total cost does not exceed the budget. Under this type of contract, there is no commitment on how many impressions get delivered. However, this paper focuses on a contract, in which the ad firm commits to deliver a specified number of impressions. Such a contract is very popular in practice.

<sup>6</sup> Xandr (https://www.xandr.com/), OpenX (https://www.openx. com/), AppLovin (https://www.applovin.com/), and Marine Ad Network (https://marineadnetwork,net/)

<sup>7</sup> The formulation of the deterministic problem is described in Online Appendix B.

<sup>8</sup> Because we use the normal distribution to approximate the binomial distribution, it is possible that our proposed policy slightly violates the probabilistic guarantee. This infeasibility can be avoided by precisely computing the buffer (using the binomial distribution) such that our proposed policy satisfies the probabilistic guarantee that ξ<sub>r</sub> impressions are won from location r with probability β.

<sup>9</sup> The expected capacity cost and expected bidding cost functions are estimated based on real-world data explained in Section 6.

<sup>10</sup> The lower limits and upper limits of the parameters’ intervals are chosen based on the values observed from a real-world example explained in Section 6.

<sup>11</sup> Of course, the revenue at these locations can also be considered in shaping demand. However, most ad firms offer plans that charge the same price per impression, regardless of the location.

<sup>12</sup> Admittedly, EFLEX itself would require some computing resources, but it is reasonable to treat these as fixed and relatively insignificant.

<sup>13</sup> For this evaluation, Cidewalk worked with ad exchange B to get some data from this ad exchange to compare the options of working with ad exchange A or B (alone) or working with both add-exchanges A and B.

<sup>14</sup> A letter from Venkat Kolluri, CEO Cidewalk Inc., describing our interaction with the company, is provided in the online appendix.

## References

Asdemir K, Kumar N, Jacob VS (2012) Pricing models for online adver tising: Cpm vs. cpc. Inform. Systems Res. 23(3-part-1):804–822.

Aseri M, Dawande M, Janakiraman G, Mookerjee V (2017) Procurement policies for mobile-promotion platforms. Management Sci 64(10):4590–4607.

Babaioff M, Hartline JD, Kleinberg RD (2009) Selling ad campaigns: Online algorithms with cancellations. Proc. 10th ACM Conf. on Electronic Commerce (ACM, New York), 61–70.

Balseiro SR, Candogan O (2017) Optimal contracts for intermediaries in online advertising. Oper. Res. 65(4):878–896

Balseiro SR, Gur Y (2019) Learning in repeated auctions with bud gets: Regret minimization and equilibrium. Management Sci. 65(9):3952–3968.

Balseiro SR, Besbes O, Weintraub GY (2015) Repeated auctions with budgets in ad exchanges: Approximations and design. Management Sci. 61(4):864–884

Balseiro SR, Feldman J, Mirrokni V, Muthukrishnan S (2014) Yield optimization of display advertising with ad exchange. Management Sci. 60(12):2886–2907.

Bapna R, Das S, Day R, Garfinkel R, Stallaert J (2011) A clock-and-offer auction market for grid resources when bidders face stochastic computational needs. INFORMS J. Comput. 23(4):630–647.

Billingsley P (2008) Probability and Measure (John Wiley & Sons, Hoboken, NJ).

Breus D (2021) What is a demand side platform: The dsp role in media buying and how to choose the right platform. Accessed May 30, 2023, https://blog.admixer.com/what-is-demand-sideplatform/#must-haves-of-dsp-platforms.

Chen Y, Xue W, Yang J (2013) Optimal inventory policy in the presence of a long-term supplier and a spot market. Oper. Res. 61(1): 88–97.

Choi H, Mela CF, Balseiro SR, Leary A (2020) Online display advertising markets: A literature review and future directions. Inform Systems Res. 31(2):556–575.

Cidewalk (2019) Private communications.

Constantin F, Feldman J, Muthukrishnan S, Pal M (2008) Online ad slotting with cancellations. Preprint, submitted May 8, https:// arxiv.org/abs/0805.1213.

Dongarra JJ (1992) Performance of various computers using standard linear equations software. ACM SIGARCH Computer Architecture News 20(3):22–44

Downey M (2012) Real-time bidding is the next mobile ad breakthrough: Here’s how you can profit. Accessed May 30, 2023, https://venturebeat.com/2012/07/23/real-time-bidding-is-the next-mobile-ad-breakthrough-heres-how-you-can-profit/.

Du AY, Das S, Ramesh R (2012) Efficient risk hedging by dynamic forward pricing: A study in cloud computing. INFORMS J. Comput. 25(4):625–642.

Fang Z, Gu B, Luo X, Xu Y (2015) Contemporaneous and delayed sales impact of location-based mobile promotions. Inform. Systems Res.

Ghosh A, Rubinstein BI, Vassilvitskii S, Zinkevich M (2009) Adaptive bidding for display advertising. Proc. 18th Internat. Conf. on World Wide Web (ACM, New York), 251–260.

Google Architecture Center (2020) Infrastructure options for rtb bidders. Accessed May 30, 2023, https://cloud.google.com architecture/infrastructure-options-for-rtb-bidders.

Graham (2015) 6 challenges of mobile ad monetisation (and their solutions). Accessed May 30, 2023, https://thenextweb.com/ insider/2015/12/16/6-challenges-and-their-solutions-of-mobilead-monetization/

Grigas P, Lobos A, Wen Z, Lee KC (2017) Profit maximization for online advertising demand-side platforms. Proc. ADKDD (ACM, New York), 1–7.

Gummadi R, Key PB, Proutiere A (2011) Optimal bidding strategies in dynamic auctions with budget constraints. Proc. 49th Annual Allerton Conf. on Comm., Control, and Comput. (IEEE, Piscataway, NJ), 588–588.

Hogg RV, Tanis EA (2009) Probability and Statistical Inference (Pearson Educational International).

Hosseini L, Tang S, Mookerjee V, Sriskandarajah C (2020) A switch in time saves the dime: A model to reducerental cost in cloud computing. Inform. Systems Res. 31(3):753–775.

Iyer K, Johari R, Sundararajan M (2014) Mean field equilibria of dynamic auctions with learning. Management Sci. 60(12):2949–2970.

Juve G, Deelman E, Berriman GB, Berman BP, Maechling P (2012) An evaluation of the cost and performance of scientific work flows on amazon ec2. J. Grid Comput. 10(1):5–21.

Korula N, Mirrokni V, Nazerzadeh H (2015) Optimizing display advertising markets: Challenges and directions. IEEE Internet Comput. 20(1):28–35.

Kreuger M (2019) Match2one uses xandr invest to deliver easy, effective programmatic buying for smbs. Accessed May 30, 2023, https://dl.xandr.com/2019/12/Xandr-Match2One-Case-Study.pdf.

Lee KC, Jalali A, Dasdan A (2013) Real time bid optimization with smooth budget delivery in online advertising. Proc. 7th Internat. Workshop on Data Mining for Online Advertising (ACM, New York), 1–9.

Lin CC, Chuang KT, Wu WCH, Chen MS (2020) Budget-constrained real-time bidding optimization: Multiple predictors make it bet ter. ACM Trans. Knowledge Discovery Data 14(2):1–27.

Lu S, Zhu Y, Dukes A (2015) Position auctions with budget constraints: Implications for advertisers and publishers. Marketing Sci. 34(6):897–905.

Luo X, Andrews M, Fang Z, Phang CW (2013) Mobile targeting. Management Sci. 60(7):1738–1756.

Mao M, Humphrey M (2011) Auto-scaling to minimize cost and meet application deadlines in cloud workflows. Proc. Internat. Conf. for High Performance Comput., Networking, Storage and Anal ysis (IEEE, Piscataway, NJ), 1–12.

Oliver T (2021) In-app advertising to account 56% digital ad spend in 2026. Accessed May 30, 2023, https://theogm.com/2022/03 09/in-app-advertising-to-account-56-digital-ad-spend-in-2026/.

Perlich C, Dalessandro B, Hook R, Stitelman O, Raeder T, Provost F (2012) Bid optimizing and inventory scoring in targeted online advertising. Proc. 18th ACM SIGKDD Internat. Conf. on Knowledge Discovery and Data Mining (ACM, New York), 804–812.

Pew Research Center (2021) Digital advertising revenue on desktop and mobile. Accessed May 30, 2023, https://www.pewresearch org/journalism/chart/sotnm-digital-advertising-revenue-ondesktop-and-mobile/.

Provost F, Martens D, Murray A (2015) Finding similar mobile consumers with a privacy-friendly geosocial design. Inform. System Res. 26(2):243–265.

Sayedi A (2018) Real-time bidding in online display advertising. Marketing Sci. 37(4):553–568.

Sayedi A, Jerath K, Baghaie M (2018) Exclusive placement in onlin advertising. Marketing Sci. 37(6):970–986.

Sharma N (2019) What is a demand side platform and how does it work? Accessed May 30, 2023, https://www.outbrain.com/blog what-is-a-demand-side-platform/

Statista (2022) Mobile advertising spending worldwide from 2007 to 2024. Accessed May 30, 2023, https://www.statista.com/statistics/ 303817/mobile-internet-advertising-revenue-worldwide/.

Sun Z, Dawande M, Janakiraman G, Mookerjee V (2017) Not just a fad: Optimal sequencing in mobile in-app advertising. Inform. Systems Res. 28(3):511–528.

Wang J, Zhang W, Yuan S (2017) Display advertising with real-tim bidding (rtb) and behavioural targeting. Foundations Trends Inform. Retrieval 11(4–5):297–435.

Wang Y, Gerchak Y (1996) Periodic review production models with variable capacity, random yield, and uncertain demand. Management Sci. 42(1):130–137.

Wu Y, Pan S, Zhang Q, Xie J (2017) Dynamic bidding strategy based on probabilistic feedback in display advertising. Proc. Internat. Conf. on Neural Inform. Processing (Springer, Berlin), 845–853.

Yang S, Zhao R, Wu F, Tang S, Gao X, Chen G (2016) Revenue maximization and contract enforcement through representative bid ding in ad auctions. Proc. IEEE Global Comm. Conf. (IEEE, Piscataway, NJ), 1–6.

Yano CA, Lee HL (1995) Lot sizing with random yields: A review Oper. Res. 43(2):311–334.

Yuan S, Das S, Ramesh R, Qiao C (2018) Service agreement trifecta: Backup resources, price and penalty in the availability-aware cloud. Inform. Systems Res. 29(4):947–964.

Zhang W, Yuan S, Wang J (2014) Optimal real-time bidding for display advertising. Proc. 20th ACM SIGKDD Internat. Conf. on Knowledg Discovery and Data Mining (ACM, New York), 1077–1086.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
