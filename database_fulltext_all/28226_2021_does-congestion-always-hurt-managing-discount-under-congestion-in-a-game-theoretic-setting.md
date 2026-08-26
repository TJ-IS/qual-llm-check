---
otero_id: 28226
otero_key: "NWPWWW67"
title: "Does Congestion Always Hurt? Managing Discount Under Congestion in a Game-Theoretic Setting"
authors: "Rajib L. Saha; Sumanta Singha; Subodha Kumar"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1040"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Does Congestion Always Hurt? Managing Discount Under Congestion in a Game-Theoretic Setting

Rajib L. Saha,<sup>a</sup> Sumanta Singha,<sup>a</sup> Subodha Kumar<sup>b</sup>

<sup>a</sup> Indian School of Business, Telangana 500111, India; <sup>b</sup> Temple University, Philadelphia, Pennsylvania 19122 Contact: rajib\_saha@isb.edu, https://orcid.org/0000-0002-9132-0151 (RLS); sumanta\_singha@isb.edu, https://orcid.org/0000-0003-3794-127X (SS); subodha@temple.edu, https://orcid.org/0000-0002-4401-7950 (SK)

Received: December 19, 2019 Revised: October 6, 2020; March 23, 2021; April 28, 2021 Accepted: May 3, 2021 Published Online in Articles in Advance: September 21, 2021

https://doi.org/10.1287/isre.2021.1040

Copyright: © 2021 INFORMS

Abstract. We study a scenario in which a buyer (e.g., Uber) buys cloud capacity from a seller (e.g., Amazon Web services) to run its business. One of the key factors that affects the quality of cloud services is congestion, and it has drawn considerable attention in recent years. Congestion leads to a potential loss of end users (e.g., riders and drivers of Uber), thereby adversely affecting the demand for cloud services. Discount has been a useful mean to stimulate demand and reward customer loyalty. However, in the presence of congestion, the effect of discount on demand is ambiguous. On the one hand, a higher discount leads to higher demand; on the other hand, higher demand can lead to higher congestion, thereby lowering the demand. Given that end users are both price and conges tion sensitive, the choice of optimal discount under congestion is, therefore, not straightforward. Using a game-theoretic model, we study the dynamics between congestion and discount and explore how congestion moderates both the buyer’s and seller’s optimal decisions. Our results show that the buyer is not necessarily worse off even when the end user are more intolerant to congestion. In fact, we <sup>fi</sup>nd that when end users are more congestion sensitive, the demand of cloud services can actually sometimes increase, and the discount offered by the seller can decrease. These <sup>fi</sup>ndings have important managerial implications on the seller’s pricing and capacity decisions. We also observe that a lower cost of technology can sometimes hurt the buyer, and the buyer can pass on lower bene<sup>fi</sup>ts to end users. Moreover, given that the cloud services are prone to disruptions, a buyer sources from multiple cloud vendors, which further complicates the matter. We draw useful insight about the buyer’s procurement decisions under congestion in a multicloud setup.

History: Yong Tan, Senior Editor; Juan Feng, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1040.

Keywords: cloud computing quantity discount congestion pricing game theory

## 1. Introduction

Cloud computing has been one of the most disruptive digital innovations since Web 2.0. As Larry Ellison, the CTO of Oracle, comments, “Cloud computing is not only the future of computing, but the present and entire past of computing” (Gelles 2019). From start-ups to global corporations, cloud computing has impacted almost every possible business. Several companies, such as Net<sup>fl</sup>ix, Uber, Twitch, Dropbox, Adobe, Twitter, Facebook, LinkedIn, Salesforce, Oracle, and BBC, rely heavily on cloud services. According to an estimate, more than 94% of enterprises already use a cloud service (Galov 2020). Gartner (2019) predicts that the cloud market will grow in excess of \$330 billion by 2022. Given such impressive prospects, cloud computing has attracted a lot of attention in recent years.

Despite its tremendous success, congestion has remained a major concern for cloud services (Anselmi et al. 2017). Congestion occurs when the demand for cloud services exceeds the cloud capacity, resulting in slowdown, data loss, or frequent disconnections (Tchernykh et al. 2019). For example, research shows that 53% of internet users abandon a web page if the loading time exceeds three seconds (Stringam and Gerdes 2019). Amid such concerns, both buyers and sellers of cloud services make important strategic decisions. How much of a discount should a cloud vendor offer when services suffer from congestion? Most importantly, does congestion necessarily hurt the buyer? Despite a growing academic interest in cloud computing (Yuan et al. 2018), some of these questions have remained largely unanswered. Answering these questions is necessary to determine how best to effectively implement cloud contracts. In this pa per, we attempt to answer these important questions.

## 1.1. Motivation

We motivate this paper in a business-to-business (B2B) setting in which a <sup>fi</sup>rm (the buyer) buys cloud services from another <sup>fi</sup>rm (the seller) to run its businesses. As with many B2B contracts, a quantity discount is fairly common for cloud services. For instance, Amazon Web Services (AWS) follows a tiered pricing model for S3 storage, meaning the higher the usage, the lower the cost per GB.<sup>1</sup> Such pricing incentivizes buyers to procure larger quantities of cloud capacity to avail lower prices.<sup>2</sup> However, unlike other B2B contracts, the nature of cloud services poses unique challenges. One such challenge is congestion. Congestion can lead to signi<sup>fi</sup>cant disruption and a potential loss of end users<sup>3</sup> for the business. For example, 81% of Internet users abandon a page or video if it does not play immediately (Rivenes 2016).

Congestion plays a crucial role in the choice of discounts for cloud service contracts. On the one hand, a higher discount leads to an increase in demand for cloud services; on the other hand, higher demand creates more congestion, which, in turn, decreases demand and hurts pro<sup>fi</sup>tability. Thus, the discount has two opposite effects on demand in the presence of congestion, and it is unclear which effect is stronger and under which circumstances. A suboptimal discount offer can damage the product’s brand image and force the seller into a vicious cycle of congestion and further price cuts (Dass et al. 2013). In this paper, we study this dynamic between congestion and discount in the context of cloud services.

Another factor that affects the demand for cloud services is the growing adoption of a multicloud strategy. Although it may be cheaper and more effortless to source everything from a single vendor, the buyer can go completely out of business if the seller fails to supply, commonly referred to as sourcing risk in the literature (Tomlin and Wang 2005). To minimize such costly disruption and increase ef<sup>fi</sup>ciency, business houses increasingly rely on multiple clouds. For example, Adobe relies on both AWS and Microsoft Azure to ful<sup>fi</sup>ll similar computational needs. As Melissa Webster, an International Data Corporation analyst, comments, “Adobe isn’t looking at Azure as a replacement for what it has now. Rather, it sees a multi-cloud environment in the future” (Richman 2016). Research by Virtustream and Forrester Consulting reveals that these multicloud businesses are on the rise with nearly 86% of enterprises adopting a multicloud strategy as the risk of congestion increases (Help Net Security 2018).

The multicloud strategy presents additional challenges and opportunities for cloud contracts. From a buyer’s perspective, one key strategic decision is how to source from multiple cloud service providers given that they are differently priced, have different costs of technology, and have different levels of risk exposure (Hong and Pavlou 2017). From a seller’s perspective, the challenge is to choose the discount more carefully as the buyer can choose to mix and match services from multiple vendors. In this paper, we study the decision problem of both the buyer and seller of cloud services under congestion in a multicloud setup. The following section elaborates on these research questions.

## 1.2. Research Questions and Contributions

The slowdown of e-commerce websites during peak usage has been a growing concern for many years. A 2017 study <sup>fi</sup>nds that a delay as small as 100 milliseconds can decrease conversion rates by 7% (Akamai 2017). In 2015, Target’s website crashed on Cyber Monday because of surging online traf<sup>fi</sup>c (Howland 2015), and the websites for Wal-Mart Stores Inc., Pay-Pal, and others also saw signi<sup>fi</sup>cant slowdown. Nasr (2015) reports, “The outage angered some would-be shoppers, and shares of Target were down more than 1% in Monday afternoon trading.” Even during a normal period, a customer can send a series of requests per session that are sometimes too many for the website to handle concurrently. Congestion leading to customer switching is prevalent in many competitive environments, such as mobile networks, app-based services, and online payment systems, especially when switching cost is low (De Ruyter et al. 1998). This raises an important managerial question: do more congestion-sensitive end users hurt the buyer?

Based on these examples, one would expect the answer to the question to be “yes” because congestion usually leads to reduced service quality (i.e., slowdown, buffering, or jitters) resulting in loss of customers for the buyer. In the Cyber Monday example, congestion-sensitive shoppers left Target’s website, thereby adversely affecting demand for its products and, hence, pro<sup>fi</sup>tability. However, our results show that pro<sup>fi</sup>tability may not always be negatively affected. We <sup>fi</sup>nd that, under certain conditions, the surplus can actually be higher even when its end users are more intolerant to congestion. This question has important implications for buyers of cloud services. In the preceding example, Target may indulge in building costly IT infrastructure in order to improve the shopping performance for its customers and reduce dropouts. However, our results suggest that this is not necessarily the best strategy. In Proposition 1, we attempt to shed light on this important question.

Another important attribute of cloud services that affects buyer surplus is its cost. In the recent past, cloud cost has fallen dramatically because of rapid innovation and a relentless drop in the cost of storage and computing engines. Thanks to massive data centers with high utilization, the entry-level cloud cost has shrunk by more than 66% since 2013 and continues to drop (Donnelly 2016). For instance, Google’s BigQuery has seen the largest price drop at 85% in

2014 following large-scale capacity optimization (Babcock 2014). Following suit, AWS slashed the S3 storage price by a massive 80% since its inception in 2006 (Barr 2016). One can store data as cheaply as one cent per GB per month. Speculation is ripe that the storage cost can fall to zero. This sharp decline in technology costs can inspire many small-to-medium-size enterprises to move their businesses to the cloud. In light of the more recent large-scale adoption of the cloud and cloud-enabled services, one may be curious to know whether a lower cost of technology bene<sup>fi</sup>ts the buyer.

As cloud services become cheaper, <sup>fi</sup>rms stand to gain from lower technology costs and increased productivity (Hosseini et al. 2020). As a result of instant scalability, there has been a signi<sup>fi</sup>cant decrease in the “capacity hoarding” cost for the <sup>fi</sup>rm. Given that a typical IT organization spends more than 30% of the annual IT budget on infrastructures, the cloud can save <sup>fi</sup>rms anywhere between 10% and 20% of the IT budget (Bishop et al. 2015). Hence, one may expect the answer to the preceding question to be “yes.” However, we <sup>fi</sup>nd that this is not necessarily true. Proposition 2 sheds light on when a lower cost of technology can actually hurt the buyer.

Our third research question investigates the impact of the cost of technology on a buyer’s pricing decision. As cloud technology becomes cheaper, end users have become wary about whether the buyer of cloud services would pass on the bene<sup>fi</sup>t of cheaper technology to end users. For example, Amazon has now lowered selling fees by as much as 70% for small- and medium-sized businesses using Amazon’s distribution channel (Khatri 2018). This drop comes in the wake of cheaper platform costs and the pressure to engage more sellers in the marketplace. In view of this, one may be curious to know whether the buyer increases the portion of the bene<sup>fi</sup>ts it passes to end users when the technology becomes cheaper for the seller? Anecdotal evidence suggests that this is indeed the case for many areas, such as computer hardware and software, broadband, medical equipment, satellite TV, VoIPs, and radio (Lyons and Coyne 2017). However, our results suggest that, sometimes, the buyer can actually pass lesser bene<sup>fi</sup>t to the end users when the cost of technology declines for the seller.

Finally, we address the fourth and <sup>fi</sup>nal research question, which deals with the impact of congestion sensitivity on the seller’s discount decision and total demand. As the end users become less tolerant of congestion, any drop in service quality may lower the demand for cloud services and may adversely affect both the buyer and the seller. Unhappy customers are more likely to abandon the buyer and switch to other <sup>fi</sup>rms in search of better quality. Buell et al. (2016) show that a congestion-sensitive customer values quality more over price and eventually gravitates toward <sup>fi</sup>rms with a high relative service quality/ price position. As a result, the seller tends to offer a higher discount to compensate for the loss in quality. For example, AWS offers a 90% discount on spot instances when end users are ready to adjust with frequent service disruption. Many e-commerce companies, such as Amazon, offer deep discounts on electronic products when they dispose of old or damaged stock to attract customers. Based on this evidence, one may want to know if the focal vendor provides a high er discount when end users are more sensitive to congestion.

One would expect the answer to be “yes” because sellers tend to believe that a discount boosts sales by enhancing the product’s perceived utility to the customers (Heda et al. 2017). However, we <sup>fi</sup>nd that this is not always the case. Our results suggest that both total demand and price can sometimes increase as end users’ congestion sensitivity becomes higher. This has important managerial implications on sellers undertaking aggressive pricing to beat market competition.

The rest of the paper is organized as follows. In Section 2, we brie<sup>fl</sup>y discuss the relevant literature and contrast our work. In Section 3, we describe the model setup, the pro<sup>fi</sup>t and the utility maximization problem for both the buyer and the seller, the game sequence, and the equilibrium solution. In Section 4, we present the results of our analysis and discuss their managerial insights. This is followed by Section 5, in which we discuss the robustness of the results to our modeling choice with regard to risks in cloud services. In Section 6, we discuss the market share contract and its underlying mechanism and present results. Finally, we conclude in Section 7 and present some future research directions.

## 2. Literature Review

Our work is broadly related to two streams of literature: (i) cloud pricing and capacity decisions and (ii) revenue management under congestion. In the following sections, we brie<sup>fl</sup>y discuss the related work in these two streams and compare and contrast our work with the extant literature to highlight our contributions.

## 2.1. Cloud Pricing and Capacity Decisions

The literature on cloud pricing is enormous, and given the different types of resources available (storage and bandwidth), different application types (server and batch), different service types (infrastructure as a service or software as a service), an exhaustive review of this literature is virtually impossible. We, therefore, present a limited review of the literature that is directly related to this study and highlight our contributions. The challenges associated with cloud pricing are multifaceted, and different studies explore different aspects of cloud pricing and capacity decisions (i.e., server sizing). For instance, Gera and Xia (2011) present quantitative modeling and optimization approaches for assisting pricing and capacity decisions in cloud computing services. They show that learning curve models can be useful to model the providers cost reduction with the economies of scale. Shen and Li (2015) propose a pricing model that sets different unit prices for different levels of congestion.

Although some researchers focus on either the cloud pricing or capacity problem, many studies examine the joint pricing and capacity right-sizing problem in the cloud market. For instance, Jain and Hazra (2019) analyze the trade-off of a business’ decision on allocating on-premise capacity and procuring excess demand from cloud vendors at a pay-as-you-go (PAYG) price. Further, Chen et al. (2019) examine two variations of a pricing scheme—the reservation- and utilization-based schemes in a duopoly setup—and look at the bene<sup>fi</sup>t of such schemes from both user’s and cloud vendor’s perspectives. Ma and Seidmann (2015) use a game-theoretic model to study the competitive dynamics between price and quality decisions. Chan et al. (2019) also do a similar study in the context of hospitals. Passacantando et al. (2016) examine the allocation of virtual machine capacity to minimize service disruption.

As mentioned, the cloud computing literature is vast and varied. Researchers examine cloud computing from a wide range of perspectives, ranging from technology to <sup>fi</sup>rm strategy to entry risks to security. We brie<sup>fl</sup>y summarize some of these works here. Guerin et al. (2019) demonstrate that sharing infrastructure can produce complex interactions between services, and the resulting diseconomies of scope can more than offset any of the bene<sup>fi</sup>ts it affords. August et al. (2014) examine cloud implications on software network structure and security risks. Chen and Wu (2013) look at their implications on market structure, <sup>fi</sup>rm pro<sup>fi</sup>tability, and consumer welfare. Fazli et al. (2018) examine the effect of auto-scaling in cloud computing on web-based <sup>fi</sup>rms’ market entry and pricing decisions. In a related study, Li and Kumar (2018) study strategies for an incumbent cloud services provider under competition and entry risks.

Much of the literature in this <sup>fi</sup>eld is related to cloud pricing and capacity allocation with or without competition. However, many of them do not model congestion and its impact on demand explicitly in their works. In this study, we model not only congestion, but also the risk of failures explicitly in a setup in which the demand is uncertain and customers are quality and price sensitive. In a related study, Cheng et al. (2016) examine cloud computing and spot pricing dynamics and the in<sup>fl</sup>uence of latency on those pricing dynamics. However, their focus is different, and they study the spatial dispersion of price and arbitrage opportunities.

The key contributions of this study with respect to the cloud pricing literature are as follows. (i) Unlike earlier research, such as Welzl (2005) that examines negative impacts of congestion or Wang et al. (2018) that <sup>fi</sup>nds no impact of delay-sensitive customers on <sup>fi</sup>rm pro<sup>fi</sup>t, our results show that the pro<sup>fi</sup>t of cloud service providers can actually sometimes increase even when the customers are more intolerant to congestion. (ii) Consistent with the literature (Wang and Zhang 2017, Wang and Wu 2018), we also <sup>fi</sup>nd the seller of cloud services determines the discount in response to the buyer’s congestion sensitivity. However, unlike past <sup>fi</sup>ndings, we show that it is possible that cloud service providers can actually lower the discount (i.e., increase the price) when the buyer is more intolerant to congestion.

## 2.2. Revenue Management Under Congestion

In this section, we brie<sup>fl</sup>y examine the related literature in revenue management (RM), especially devoted to price-based RM. Price-based RM has been the subject of operation researchers for ages (Smith et al. 1992) and extended more recently (Talluri and Van Ryzin 2006). Quantity discount is one of the common strategies in price-based revenue management. Although studying RM started with the airlines and hotel industries, it soon expanded to many other <sup>fi</sup>elds, such as automobile rental and hospitality, among others. In the early 2000s, it became popular in internet-based services as well. For instance, Nair and Bapna (2001) study the problem of internet network utilization in which customers queue up randomly, and the internet service provider allocates the available modems to the customers. However, unlike our model, they do not consider the impact of congestion, which implies that the allocation decision at any stage does not affect the service quality for subsequent buyers.

Li et al. (2009) study the optimal usage-based pricing problem in a resource-constrained network with a single service provider and multiple buyers but do not model congestion explicitly. In a related study, Pa schalidis and Tsitsiklis (2000) examine the congestiondependent pricing for network services. In their work, customers do not in<sup>fl</sup>uence the pricing decision of the service provider, unlike our model, in which customers’ tolerance to congestion drives pricing and capacity decisions. This is a key difference with our work.

In most of the earlier works, the common presumption is that all <sup>fi</sup>rms have an economic interest in low er input prices (Thatcher and Oliver 2001). However, we show that, under certain conditions, low technology prices can actually hurt when congestion is present and provide necessary conditions for the same. This is one of the contributions of the paper. Another key <sup>fi</sup>nding of our study is that <sup>fi</sup>rms can sometimes lower the percentage of the bene<sup>fi</sup>ts they pass to the end users. This contrasts with the <sup>fi</sup>ndings of Koopman et al. (2015), who show that, in a competitive economy, <sup>fi</sup>rms can <sup>fi</sup>nd innovative ways to minimize their costs, passing on some of the savings to customers. Kate and Niels (2005) study a somewhat similar problem as ours in which they examine whether a pro<sup>fi</sup>tmaximizing <sup>fi</sup>rm would share such bene<sup>fi</sup>ts. However, they do not analytically obtain the optimal sharing percentage as we do.

## 3. Model Setup with Quantity Discount Contract

In this section, we introduce our model and summarize key notations in Table 1. We consider a single-period setting, in which a <sup>fi</sup>rm (the client, that is, the buyer of the cloud services) procures cloud services from other <sup>fi</sup>rms (the cloud vendors, that is, the sellers of the cloud services) to run its business. For example, Dropbox buys cloud services from AWS to offer <sup>fi</sup>le sharing and data storage facilities to millions of its users across the world. Although Dropbox decided to move 90% of its data from AWS to its in-house server in 2017, it still relies on AWS for its European and Asian market for performance and reliability (Miller 2017). Spotify, a music streaming and media service provider, relies on both Google cloud for core infrastructure and AWS for peripheral services to provide online music streaming services to its customers. This practice of procuring cloud services from multiple <sup>fi</sup>rms, otherwise known as the multicloud strategy, is common across the industry. According to a survey, 86% of enterprises have adopted a multicloud strategy to minimize costly disruptions (Help Net Security 2018).

Table 1. Key Notations and Decision Variables

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td> $i$ </td><td>Index of vendor,  $i = \{ f : \text{focal vendor}, s : \text{spot vendor} \}$ </td></tr><tr><td colspan="2">Parameters</td></tr><tr><td> $Q_0$ </td><td>Stable component of the base demand</td></tr><tr><td> $\varepsilon$ </td><td>Random component of the base demand</td></tr><tr><td> $\alpha$ </td><td>Congestion sensitivity</td></tr><tr><td> $\beta$ </td><td>Discount sensitivity</td></tr><tr><td> $k$ </td><td>Capacity cost coefficient</td></tr><tr><td> $v$ </td><td>Value per unit of cloud services to the buyer</td></tr><tr><td> $p_i$ </td><td>PAYG price from Vendor  $i$ </td></tr><tr><td colspan="2">Decisions</td></tr><tr><td> $d$ </td><td>Discount coefficient</td></tr><tr><td> $s$ </td><td>Capacity under discount contract</td></tr><tr><td> $q$ </td><td>Quantity procured under discount contract</td></tr><tr><td> $\lambda$ </td><td>Proportion of total discount passed to end users</td></tr><tr><td> $b$ </td><td>Focal vendor&#x27;s share of demand at PAYG price</td></tr><tr><td colspan="2">Equilibrium outcome</td></tr><tr><td> $Q$ </td><td>Total demand for cloud services</td></tr><tr><td> $p$ </td><td>Unit price under discount contract</td></tr><tr><td> $q_i$ </td><td>Quantity fulfilled from Vendor  $i$  at PAYG price</td></tr><tr><td> $\pi_i$ </td><td>Profit of Vendor  $i$ </td></tr><tr><td> $\pi_b$ </td><td>Buyer surplus or net utility of the buyer</td></tr></table>

In this paper, we study the strategic interactions of the buyer and sellers of cloud services using an analytical model. Before we provide additional details about the utility functions of different players in the game and the decisions they make, we provide, in this paragraph, a brief overview of the players in our game setup. To capture the dynamics of the market for cloud services, we consider two cloud vendors: a strategic <sup>fi</sup>rm, hereafter, called the focal vendor, whose decisions we model, and a nonstrategic <sup>fi</sup>rm that represents the spot market, hereafter, called the spot vendor. The demand for cloud services is generated from the service the buyer offers to its end users. The buyer allocates the total demand between the focal and the spot vendors based on the relative risks and prices offered by these two vendors.

Here, we brie<sup>fl</sup>y explain the quality levels of the services offered by the cloud vendors. Consequently, we elaborate on these aspects and their implications on the players’ decision making in further detail in the following sections. We consider that the buyer signs a discount-based contract only with the focal vendor— hence, termed the “focal” vendor. The focal vendor al lots a certain capacity as part of the contract. The product bought under this contract can lead to congestion as it is ful<sup>fi</sup>lled using a limited capacity that comes with the contract. The focal vendor also offers, on the go, cloud services that are not susceptible to congestion, however, at a higher price. Going by the industry practice, we term this price the PAYG price. This PAYG price is analogous to Amazon’s “on-demand” price or Google’s “pay-as-you-go” pricing, with which customers pay for what they use without any up-front commitment.

Essentially, we capture a scenario in which the focal vendor offers both low- and high-quality services: congestion-prone services at a discounted price and congestion-free services at a PAYG price. The buyer considers the spot vendor only for procuring high quality, congestion-free services on the go, as and when demand is realized—hence, termed the “spot” vendor. As demand is realized, the buyer ful<sup>fi</sup>lls a part of its demand for cloud services using the discount contract from the focal vendor. Thereafter, it allocates the rest of the demand between the focal and the spot vendors at PAYG prices. Next, we elaborate on the nature of the discount-based contract that the buyer signs with the cloud vendor.

## 3.1. The Nature of Discount-Based B2B Contract

Both the buyer and the focal vendor have strategic incentives to collaborate (Venkatesan 1992). Some common incentives offered by sellers to buyers include attractive discounts, longer payment terms, improved operational ef<sup>fi</sup>ciency, shared innovation, speed to market, and quality control (Tevelson et al. 2013). Of them, a discount is the most popular way to stimulate demand and reward customer loyalty. For example, Google offers a discount up to 57% compared with the on-demand rate when customers buy a long-term contract of up to three years (Google 2020). According to a survey, 97% of the respondents consider discount as the top pricing strategy for retailers across the sectors (Guinn 2015). In this study, we model the discount offered by the focal vendor as the discount per unit benchmarked against the PAYG price. For example, AWS and Google offer attractive discounts on subscription-based plans but bill retail demand at the highest on-demand rate (similar to the PAYG price).

We analyze the equilibrium outcome under a speci<sup>fi</sup>c form of discount-based contract, known as a quantity discount contract (Wilson 1993). Under this contract, the seller offers a discount that depends on the absolute number of units the buyer procures from the focal vendor. For instance, AWS charges \$0.023 per gigabyte (GB) up to 50 TB storage, \$0.022 per GB for 51–100 TB storage, and \$0.021 per GB for 100<sup>+</sup> TB storage (Amazon 2020). Similar to Chen and Wu (2013), we model a quantity discount contract in which the discount increases linearly with the quantity purchased. Given that the buyer procures q units of cloud services from the focal vendor under this contract, we formulate the discounted price per unit p as follows:

$$
p = p _ {f} - d q,\tag{1}
$$

where $p _ { f }$ is the PAYG price from the focal vendor and d is the discount coef<sup>fi</sup>cient that captures the steepness of the discount. The price implies the price per unit of cloud capacity in which capacity can be in any form, from storage to memory to computing power (Soni and Hasan 2017). The focal vendor’s decision is to choose an appropriate d that maximizes its pro<sup>fi</sup>t. Next, we discuss how we model the demand for cloud services and how such discount-based contracts further impacts it.

## 3.2. Characterization of Demand for Cloud-Based Services

The demand for cloud services originates from the end users of the buyer’s <sup>fi</sup>rm. This demand can be random, referred to as “surge” in the literature (Arbabian et al. 2020). Consistent with the literature (Petruzz and Dada 1999, Kansal et al. 2020), we de<sup>fi</sup>ne the base demand for cloud services as the sum of a stable and a random component as $Q _ { 0 } + \epsilon ,$ , where $Q _ { 0 } > 0$ is the stable part and E is the random part with mean zero and standard deviation $\sigma > 0$ . However, as we elabo rate, there exist other factors that can further impact the demand for cloud services.

One such factor that lowers the demand is congestion. In June 2019, Google reported “high levels of network congestion in the eastern USA, affecting multiple services in Google Cloud, G-Suite and YouTube” (PTI 2019). Congestion occurs when the cloud service provider has capacity constraints (i.e., bandwidth limitation, storage scalability, or network latency). Congestion leads to reduced quality of service (i.e., performance, reliability, and availability)<sup>4</sup> and a potential loss of customers. For instance, an angry Dropbox user wrote “I received an angry email from client saying the picture quality was not going to <sup>fl</sup>y with them. Does Dropbox reduce the quality of pictures?” (Stone 2015). Despite many technological advances, congestion remains a key concern for businesses.

What leads to congestion? Usually, when a B2B contract is established, the vendor makes certain investments on building capacity taking into account the needs of the buyer. We capture this aspect by considering that, when the cloud vendor offers a discountbased contract, it also builds a capacity, s, associated with the contract. An overutilization of that capacity can lead to congestion, leading to a delay in services. We model congestion as a threshold-based phenomenon (Chung et al. 2018), meaning congestion triggers when the demand ful<sup>fi</sup>lled by the buyer under the discount contract exceeds the allotted capacity. This congestion slows down the availability of services that the buyer provides to the end users.

An immediate consequence of delay in the availability of services is loss of demand. As Stringam and Gerdes (2019) note, internet users abandon a web page if the loading time exceeds three seconds. Following the literature (Koo et al. 2012), we consider that the demand drops at an increasing rate once the demand exceeds the network capacity. This conceptualization is consistent with standard queuing theory, in which service time is considered exponentially distributed (Vilaplana et al. 2014). In order to capture this phenomenon, we consider that the decrease in demand equals $\alpha ( [ q - s ] ^ { + } ) ^ { 2 }$ , where s is the allotted capacity by the focal vendor and $q$ is the demand allocated by the buyer under the discount contract. The parameter $\alpha \geq 0$ is a scaling factor and captures the strength of the negative impact; the higher the $\alpha ,$ the higher the loss in demand because of congestion. We denote this parameter α as the congestion sensitivity of the end users.

Another factor that increases the demand for cloud service is the bene<sup>fi</sup>t that the buyer of cloud service offers to its end users. For example, Net<sup>fl</sup>ix, a leading internet television network, occasionally offers reduced subscription fees or promotions (e.g., “10% discount on a 3-month subscription,” “free watching of a popular series,” “one-month free subscription”).<sup>5</sup> Such options are common in practice and can enhance the utility of the end users. In fact, there exists a variety of nonmonetary bene<sup>fi</sup>ts, such as attractive payment terms, lower processing fees, extended warranty, auto-renewal facility, etc., that can boost the demand from end users.

How such nonmonetary bene<sup>fi</sup>ts positively in<sup>fl</sup>uence the demand, in turn, depends on the total discount the buyer (for instance, Net<sup>fl</sup>ix) receives from the cloud vendor (for instance, AWS) and also the proportion of that discount the buyer passes on to its end users. The total discount that the buyer receives from the focal vendor is given by $d q ^ { 2 } .$ , where d times q is the discount per unit and $q$ is the quantity procured at this discount. We denote the proportion of the total discount the buyer passes on to its end users through nonmonetary means as $\lambda \in [ 0 , 1 ]$ . Thus, the total amount of bene<sup>fi</sup>t that the buyer passes on to end users is λ dq q. We consider that the increase in demand is concave in this quantity (Huang et al. 2013). Therefore, we model the increase in demand as $\beta \sqrt { \lambda ( d q ) q }$

We now model the cumulative effect of congestion and discount on <sup>fi</sup>nal demand. A linear demand function is used in many areas of service operations, including cloud services (Kansal et al. 2020). In a linear demand model, demand elasticity is always decreasing and concave in price, unlike the multiplicative (iso-elastic) demand model, in which demand elasticity is always negative and constant. Consistent with the literature (Petruzzi and Dada 1999), we de<sup>fi</sup>ne the net total demand for cloud services faced by the buyer (Q) by considering the impact of congestion and discount to be additive as follows:

$$
Q = (Q _ {0} + \epsilon) - \alpha ([ q - s ] ^ {+}) ^ {2} + \beta \sqrt {\lambda (d q) q},\tag{2}
$$

where the <sup>fi</sup>rst term captures the base demand, the second term the negative impact of congestion, and the third term the positive impact of discount.

## 3.3. Net Utility of the Buyer of Cloud Services

The buyer buys cloud services to run its business and, in turn, generates positive utility by selling its products or services to the end users. For example, Uber purchases cloud capacity from AWS to deliver peerto-peer riding and taxi services. We represent this value that the buyer realizes from consuming each unit of cloud service as $v \geq 0$ in our model. Therefore, vQ represents the total value the buyer earns from consuming Q units of cloud services. Although vQ represents the income for the buyer, the buyer also incurs certain costs to run its business. The buyer’s cost comes from the payment it makes to cloud service providers in order to buy cloud capacity and the bene-<sup>fi</sup>t it passes on to the end users to stimulate the demand. As mentioned, the total amount of bene<sup>fi</sup>t the buyer passes to the end users is given by λ dq q. Next, we discuss the payments the buyer makes to the cloud vendors for purchasing cloud capacity.

Because the buyer buys q quantity from the focal vendor at a discounted price p, it pays pq to the focal vendor under the discount contract. The choice of q is critical for the buyer. As a cloud service bought under the discount contract is prone to congestion, a larger quantity bought under the discount contract leads to a higher congestion, resulting in loss of demand (Rivenes 2016). Therefore, in order to maintain a healthy level of demand, the buyer also buys cloud services using a PAYG contract, which is more expensive but does not suffer from congestion. At this juncture, the buyer has the option to buy the quantity over and above q from the focal vendor or from multiple vendors. The practice of procuring identical products or services (i.e., perfect substitutes) from multiple ven dors is known as the multicloud strategy. Multicloud has become increasingly common among businesses to minimize costly disruption as well as to ful<sup>fi</sup>ll unplanned demand. For example, Adobe relies on both AWS and Microsoft Azure to ful<sup>fi</sup>ll similar computational needs (Richman 2016). According to a survey from IBM, 85% of organizations are now using multiple clouds in their business, and by 2021, 98% of companies plan to adopt a multicloud strategy (Wilson 2018).

One of the main reasons behind adopting a multicloud strategy is to avoid the risk of failures. Hong et al. (2019) state that <sup>fi</sup>rms utilize numerous cloud networks and services simultaneously to ensure high availability and provide backups during disasters. Examples of failures include <sup>fl</sup>awed security, hacking, power outage, poor design, networking issues, maintenance, and others. Of these, although a few types of failures, such as load balancing or disc failure, can be quickly <sup>fi</sup>xed, some others, such as power outage, poor design, hacking, and natural disasters, take a long duration for recovery (Yuan et al. 2018). According to the International Working Group on Cloud Computing Resiliency, the average unavailability of cloud services is 7.7 hours per year or more (Cerin´ et al. 2013). This explains why, despite the rapid scalability of cloud services, disruptions or failures remain a concern for most businesses.

However, the risk of failure has very little or no impact on the quantity purchased under the discount contract. For such contracts, cloud service providers maintain adequate backup capacity so that the committed capacity can be made available even if there is a disruption. Yuan et al. (2018) state that a cloud service provider typically allocates a set of k additional virtual machines (VMs) as backup(s) to the client as best-effort sustenance of the uptime guarantee. Hence, downtime results only when all $( k + 1 )$ VMs concurrently fail. This is not necessarily the case with PAYG services because the cloud vendor, in this category, allocates capacity as and when needed in the absence of any prior commitment on capacity. Therefore, we consider that the quantity bought at PAYG prices alone is exposed to this risk and not the quantity bought under the discount contract.<sup>6</sup>

Thus, consistent with industry practice, we consider a setting in which the buyer ful<sup>fi</sup>lls its excess demand from two PAYG vendors—the focal and spot vendors—who are perfect substitutes in terms of quality but differ in prices and relative risks of failures. Following the literature on secondary markets (Lee and Whang 2002), we model the spot vendor as a nonstrategic substitute that provides only tactical sourcing opportunities. Let $p _ { f }$ and $p _ { s }$ denote the PAYG prices offered by the focal and spot vendors, respectively. In order to realistically capture the buyer’s trade-off between congestion and price and also to minimize the risk of failure, we break the buyer’s allocation decision into two stages. First, the buyer decides the quantity q to procure under the discount contract from the focal vendor. Next, the buyer decides the proportion b of the remaining demand $( Q - q )$ to procure from the focal vendor at a PAYG price. The leftover quantity is procured from the spot vendor at the PAYG price. We denote the quantity bought at the respective PAYG prices from the focal and spot vendors as $q _ { f }$ and $q _ { s } ,$ respectively; essentially, $q _ { f } = b ( Q - q )$ and $q _ { s } = ( 1 - b )$ $( { \bar { Q } } - q )$ . The buyer’s allocation decisions are pictorially depicted in Figure 1. Given a choice of $b ,$ the buyer’s utility maximization problem is written as

$$
\max _ {q \geq 0, \lambda \in [ 0, 1 ]} E [ \pi_ {b} ] = \max _ {q \geq 0, \lambda \in [ 0, 1 ]} E \Big [ v Q - \lambda d q ^ {2} - p q - p _ {f} q _ {f} - p _ {s} q _ {s} \Big ].\tag{3}
$$

The <sup>fi</sup>rst term of the utility function of the buyer in Equation (3) represents the total value generated for the buyer, the second term represents the bene<sup>fi</sup>t the buyers passes on to the end users, the third term represents the buyer’s payment to the focal vendor under the discount contract, and the fourth and <sup>fi</sup>fth terms represent the buyer’s payments to the focal and spot vendors, respectively, for the amount of services it procures at the respective PAYG prices; the expectation is taken over the distribution of E.

The choice of b depends not only on the PAYG prices offered by these vendors, but also on their respective risks of disruption or service failure that is different from the risk of demand uncertainty. Because procuring a large quantity from a single vendor increases the risk of failure (Blome and Henke 2009), we de<sup>fi</sup>ne risk exposure as rx, where x is the proportion of demand that is allocated to the vendor and r is the risk pro<sup>fi</sup>le of that vendor. We denote the risk pro-<sup>fi</sup>le of the focal and spot vendors as $r _ { f } \geq 0$ and $r _ { s } \ge 0 ,$ respectively. Therefore, the buyer decides b in such a way that minimizes not only its total payment for the quantity at PAYG prices, but also the total risk exposure of that quantity. Thus, the buyer’s risk-adjusted cost $r _ { b }$ is given as the sum of the risk exposure and payment at PAYG prices. The buyer’s risk minimization problem can be stated as

$$
\min _ {b \in [ 0, 1 ]} E [ r _ {b} ] = \min _ {b \in [ 0, 1 ]} E \bigl [ (p _ {f} q _ {f} + p _ {s} q _ {s}) + (b r _ {f} q _ {f} + (1 - b) r _ {s} q _ {s}) \bigr ],
$$

(4)

where the <sup>fi</sup>rst term represents the total payment and the second term represents the total risk exposure of the quantity bought under the PAYG category; the expectation is taken over the distribution of E.

## 3.4. Profit of the Focal Vendor

The focal vendor is strategic in its pricing decision and chooses a discount schedule that maximizes its pro<sup>fi</sup>t. It does so by choosing an appropriate discount coef<sup>fi</sup>cient, $d ,$ that we mention earlier in Section 3.1 when describing the form of the quantity discount contract. It also chooses a capacity level, s. A convex cost function is well justi<sup>fi</sup>ed in both literature and practice (Zhang et al. 2020). Therefore, consistent with the literature, we take the cost of developing cloud capacity as convex to the level of capacity. In particular, we take the cost of developing the capacity level s as $k s ^ { 2 }$ , where $k > 0$ . Following past studies, we consider that the cloud vendor incurs no marginal costs while providing cloud services (Weinman 2011). Therefore, the focal vendor’s pro<sup>fi</sup>t maximization problem is given as

Figure 1. The Buyer’s Allocation Decisions  
![](/api/attachments/NWPWWW67/fulltext/images/7f6e7a918172eba026e9b0d716f33e4bfcacda86d1c333ecba8480a63cecf0b4.jpg)

$$
\max _ {d \geq 0, s \geq 0} E [ \pi_ {f} ] = \max _ {d \geq 0, s \geq 0} E \Big [ p q + p _ {f} q _ {f} - k s ^ {2} \Big ].\tag{5}
$$

The <sup>fi</sup>rst term in the focal vendor’s pro<sup>fi</sup>t function represents the pro<sup>fi</sup>t earned through the discount contract, the second term represents the pro<sup>fi</sup>t earned from the sale of the high-quality service at a PAYG price, and the third term represents the cost of capacity; the expectation is taken over the distribution of E.

## 3.5. Game Sequence

AWS and other leading cloud service providers offer a host of subscription plans specifying the maximum possible discount allowed under those plans (Amazon 2020). The actual amount of discount, however, depends on the type of instances used and the size and tenure of the contract, which are usually privately negotiated with the buyer (Du et al. 2013). Generally, cloud service providers know the buyer’s purchase requirements in advance (for large enterprise customers and repeat buyers) or can <sup>fi</sup>nd them with minimal effort. As a result, cloud service providers can choose the discount schedule accordingly and also make customer-speci<sup>fi</sup>c investment. Therefore, the game begins with the focal vendor offering a contract to the buyer with full knowledge of the buyer’s demand function. This is Stage 1 of the game. In our context, in Stage 1, the focal vendor decides the steepness of the discount, that is, the discount coef<sup>fi</sup>cient d for the quantity discount contract. At this stage, it also decides the capacity level s that it builds for the buyer. The focal vendor’s optimization problem in Stage 1 is given in Equation (5).

In Stage 2, based on the discount schedule and capacity offered, the buyer decides $q ,$ that is, how much to source from the focal vendor using the discount contract, knowing full well that the service under the discount contract is cheaper but congestion prone. As mentioned earlier, Spotify used Google cloud for core infrastructure while relying on AWS for peripheral service. Although, in some instances, the demand allocation is driven by technical constraints (e.g., having an OEM) or the modularity of the job, this is not so in many instances. Nonetheless, the buyer can procure a certain deterministic quantity from the focal vendo using the contract. At this stage, the buyer also decides λ, that is, the proportion of the total discount it passes on to the end users. The buyer’s optimization problem in Stage 2 is given in Equation (3).

Once the demand is realized and the buyer has procured the predecided quantity using the discount contract, it allocates the rest of the demand between the two vendors while paying the respective PAYG prices. Essentially, it decides $b ,$ the proportion of the rest of the demand it allocates to the focal vendor. This is Stage 3 of the game. The buyer’s optimization problem in Stage 3 is given in Equation (4). Based on this game sequence, there exist several possibilities. With respect to the decision variables b and $q ,$ we enumerate these possibilities in Figure 2. Of these possibilities, Case II $( Q = q )$ and Case IC $( Q > q$ and $b = 1 )$ ) degenerate into a monopoly setup. However, in this paper, we are focusing on a scenario in which two cloud service providers coexist. Therefore, we do not study these cases. Furthermore, $q = 0$ or $d = 0$ makes our study of a quantity discount contract irrelevant, and they are, therefore, omitted. In addition, $\lambda = 0$ or 1 and $s = 0$ do not re<sup>fl</sup>ect reality. It is unlikely that a buyer passes either everything or nothing to end users. Similarly, $s = 0$ is unrealistic as a B2B contract without any customer-speci<sup>fi</sup>c investment is rare. Therefore, we exclude these possibilities as well. In the following section, we only focus on the solutions in which $0 \le b < 1 , q > 0 , d > 0 , 0 < \lambda < 1$ , and $s > 0 .$ The game sequence is depicted in Figure 3.

## 3.6. Equilibrium Outcome

In this section, we derive the optimal choices of the buyer and the focal vendor, the focal vendor’s pro<sup>fi</sup>t, and the buyer’s net utility or surplus. Using backward induction, we <sup>fi</sup>rst determine the buyer’s optimal allocation strategy: First, we work out the buyer’s optimal choice of $b ;$ thereafter, we solve for the buyer’s optimal choice for $q$ and λ. At the next step, given the buyer’s allocation choices, we estimate the focal vendor’s optimal discount and capacity investment strategy; that is, we work out the focal vendor’s optimal choice for d and s. As far as the exogenous parameters in our model are concerned, the parameter space that we consider in our analysis is

Figure 2. Possible Allocations  
![](/api/attachments/NWPWWW67/fulltext/images/46ed243eb3092ad9e6606a2d6c902b70fb1ec02c7a3f62b1ee7f4646b3dce6ca.jpg)

Figure 3. Game Sequence  
![](/api/attachments/NWPWWW67/fulltext/images/c49a2630bde4dbb4d29ec2df617df755c39881cdfe05dba81670919282edbb12.jpg)

$$
\begin{array}{c} \chi = (Q _ {0} \geq 0) \text { and } (\sigma \geq 0) \text { and } (\alpha \geq 0) \text { and } (\beta \geq 0) \\ \text { and } (k \geq 0) \text { and } (v \geq 0) \text { and } (p _ {f} \geq 0) \\ \text { and } (p _ {s} \geq 0) \text { and } (r _ {f} \geq 0) \text { and } (r _ {s} \geq 0). \end{array}\tag{6}
$$

Lemma EC.1 presents the equilibrium outcome under the quantity discount contract. Both the lemma and its proof are included in the online appendix.

## 4. Results and Managerial Insights

In this section, we discuss key results and manageria insights. We explore the impact of congestion and discount on the buyer’s and seller’s decisions and the equilibrium outcomes. As expected, we <sup>fi</sup>nd that the buyer buys less using basic services when end users are more congestion sensitive and more when end users are more discount sensitive. In other words, $q$ is decreasing in α and increasing in $\beta .$ The same is true for the pro<sup>fi</sup>t of the focal vendor as well. The reason is that a higher value of α lowers the allocation of demand to the focal vendor. In order to make up for the loss in demand, the focal vendor increases its discount coef<sup>fi</sup>cient $d ,$ which hurts its pro<sup>fi</sup>tability. In contrast, a higher value of $\beta$ increases the allocation of demand to the focal vendor that leads to a higher pro<sup>fi</sup>t. From the buyer’s perspective, the impact of $\beta$ is straightforward as well. $\operatorname { A s } \beta$ increases, it increases the demand, resulting in higher surplus for the buyer. Although these observations are somewhat intuitive, the impact of α on the buyer’s surplus is not so straightforward. It is not obvious whether the buyer is worse off when the end users are more intolerant to congestion. In Section 4.1, we address this ambiguity.

## 4.1. Do More Congestion-Sensitive End Users Hurt the Buyer?

Cloud service providers offer services at different levels of quality. Although some services are fast and expensive, others are cheap but have high latency. High latency (i.e., long delay) can cause serious frustration to internet users or even permanent loss of customers. For example, in 2011, Vodafone in Australia lost 375,000 end users and \$155 million in revenue to Sprint because of massive congestion in its 4G network. Stringam and Gerdes (2019) <sup>fi</sup>nd that internet users abandon a web page if the loading time exceeds three seconds. The problem becomes particularly acute when end users are highly congestion sensitive or running applications, such as video streaming or VoIPS, which require low latency. This leads us to our <sup>fi</sup>rst research question: does congestion always hurt the buyer of cloud services? In the following proposition, we attempt to answer this question.

Proposition 1. Under a quantity discount contract, the buyer’s surplus can sometimes increase even when the end users are more intolerant to congestion (i.e., α is higher). Specifically, $\begin{array} { r } { \frac { d E [ \pi _ { b } ] } { d \alpha } > 0 } \end{array}$ when $\alpha <$ $\frac { 3 2 A _ { 2 } k ^ { 3 } Z _ { 1 } ^ { 2 } + 4 A _ { 1 } ^ { 2 } k ( A _ { 1 } ^ { 2 } A _ { 2 } - 4 ( 1 - b ^ { * } ) ( b ^ { * } ) ^ { 2 } p _ { f } ^ { 3 } - A _ { 1 } b ^ { * } p _ { f } W _ { 1 } ) \alpha ^ { 2 } + A _ { 1 } ^ { 4 } \big ( 4 b ^ { * } p _ { f } Y _ { 1 } + A _ { 1 } X _ { 1 } \big ) \alpha ^ { 3 } } { 2 4 A _ { 1 } ^ { 2 } A _ { 2 } k ^ { 2 } Z _ { 1 } } .$ The expressions of $X _ { 1 } , Y _ { 1 } , Z _ { 1 } , W _ { 1 } , A _ { 1 } ,$ , and $A _ { 2 }$ are included in the proof.

As described earlier, congestion can lead to severe performance drop, network jitters, or buffering. Users may see delay or intermittent errors, forcing unhappy users to leave the platform or even switch to an alternate service provider. Krishnan and Sitaraman (2013) show that more than half the audience leave when the start-up delay exceeds 10 seconds. Mueller (2015) shows that when video quality is poor, 33% of viewers abandon the video immediately and 84% leave after a minute. According to OnBlastBlog (2016), an e-commerce <sup>fi</sup>rm making \$50,000 a day could potentially lose \$1.25 million in sales per year from a one-second page delay.

Therefore, users’ tolerance to congestion plays a critical role in cloud services. This tolerance to congestion α can vary across services for a variety of reasons. For example, in the case of e-commerce and video streaming services, with which switching to a competing platform is less costly, users can be even less tolerant to congestion. In contrast, tolerance can be high when switching is costlier as in the case of Dropbox. Therefore, one would expect that, when users are more intolerant to congestion, it would hurt the buyer more.

However, our results suggest that this is not always the case. In fact, we <sup>fi</sup>nd that buyer surplus is nonmonotonic in $\alpha ,$ and it can sometimes increase even when end users are more congestion intolerant. This occurs because the congestion sensitivity of end users affects buyer surplus in two ways. On the one hand, with a higher level of $\alpha ,$ the buyer procures less under the discount contract and more under the PAYG service to avoid congestion. As a result, the buyer receives a lower per-unit discount from the focal vendor $( \mathrm { i . e . , }$ $\begin{array} { r } { \frac { d ( d q ) } { d \alpha } < 0 ) } \end{array}$ , which hurts buyer surplus. On the other hand, as the PAYG service is congestion-free, the total demand increases. Consequently, the revenue as well as the total procurement costs both increase. In effect, buyer surplus can sometimes increase in α as the revenue increases at a faster rate dominating the negative effect of congestion.

This result has important managerial implications for business as competitive pressure is paramount on every <sup>fi</sup>rm to retain market share. When users are more congestion sensitive, business managers may rush to mitigate the effects of congestion. This arises out of the fear that a loss in service quality may force dissatis<sup>fi</sup>ed end users to leave, thereby hurting the buyer. However, our result shows that this is not always the case, and practicing managers must assess end users’ congestion sensitivity critically before adopting any measures.

Congestion is a negative externality that adds to the network costs (Welzl 2005). However, literature on congestion and service capacity allocation reports con-<sup>fl</sup>icting <sup>fi</sup>ndings on the impact of delay-sensitive customers on the <sup>fi</sup>rm’s pro<sup>fi</sup>t. For instance, Wang et al. (2018) <sup>fi</sup>nd that delay-sensitive customers can hurt <sup>fi</sup>rm pro<sup>fi</sup>t under asymmetric competition, whereas it has no impact on <sup>fi</sup>rm pro<sup>fi</sup>t when the <sup>fi</sup>rms and consumers are symmetric. Sunar et al. (2021) show that, when customers are delay sensitive and decide to join or balk based on queue length, it can lower the <sup>fi</sup>rm’s pro<sup>fi</sup>t. Hassin and Haviv (2003) provide an excellent review on this research stream. Our results show that, under certain conditions, the high congestion sensitivity of end users does not hurt the buyer of cloud services in a B2B setting. In fact, the <sup>fi</sup>rm’s pro<sup>fi</sup>t can actually sometimes increase. Our study contributes to the existing literature by providing conditions in which having more delay-sensitive customers is not necessarily bad for congestion-prone services.

## 4.2. Does a Lower Cost of Technology Benefit the Buyer?

In recent years, cloud prices have dramatically fallen because of innovation and competition in the cloud market (Rosenthal et al. 2012). The entry-level cloud cost has shrunk by more than 66% since 2013 and con tinues to slide further (Donnelly 2016). Research indicates that the price-performance of computing has almost doubled in every 1.4 years, translating to a 39% annual price decrease in processing costs (Nordhaus et al. 2001). Data can be stored for as little as one cent per GB per month. Such a downward spiral has led to phenomenal growth in the usage of cloud and cloudenabled services. For instance, an average of 60 mil lion photos get uploaded daily by Instagram users, and more than 500 million tweets are sent per day globally (Robertson 2018). This heightened enthusiasm raises a very important question: does a lower cost of technology always bene<sup>fi</sup>t the buyer of cloud service?

As the cloud becomes cheaper, <sup>fi</sup>rms potentially bene<sup>fi</sup>t from huge ef<sup>fi</sup>ciency gains, lower licensing and infrastructure costs, and increased workplace productivity (Hosseini et al. 2020). In a B2B setting, this implies a greater market penetration for the buyer, securing more end users and higher growth. A lower cost cloud can enhance buyer surplus in two ways. First, with typical IT organizations spending more than 30% of their annual IT budget on infrastructure, the cloud can save <sup>fi</sup>rms between 10% and 20% of their IT budget. Second, with improved utilization and instant scalability, there is a signi<sup>fi</sup>cant drop in capacity hoarding, resulting in the lower unit cost of usage (Bishop et al. 2015). For the aforementioned reasons, one may expect the answer to the question to be $\mathrm { ^ { \prime \prime } y e s . ^ { \prime \prime } }$ However, we <sup>fi</sup>nd that this is not necessarily true. Proposition 2 sheds light on this very important question.

Proposition 2. Under a quantity discount contract, the buyer surplus can decrease even when the technology gets cheaper for the seller $( i . e . ,$ , k is lower). Specifically, $\begin{array} { r } { \frac { d E [ \pi _ { b } ] } { d k } > 0 } \end{array}$ when $( k Y _ { 2 } - Z _ { 2 } ) > 0$ . The expressions of $Y _ { 2 }$ and $Z _ { 2 }$ are included in the proof.

As this technology becomes cheaper $( \mathrm { i . e . , }$ k decreases), the focal vendor allocates a higher capacity $( \mathrm { i . e . } , s$ increases) under the discount contract. This has two opposite effects on buyer surplus. On the one hand, it lowers congestion and increases the total demand resulting in higher revenue for the buyer $( \mathrm { i . e . , }$ $\begin{array} { r } { \frac { d Q } { d k } < 0 ) } \end{array}$ ). On the other hand, because of higher capacity $s ,$ the buyer procures more under the discount contract, and consequently, the focal vendor <sup>fi</sup>nds it optimal to lower the discount coef<sup>fi</sup>cient d. In effect, the discounted price increases as $k$ decreases $( \mathrm { i . e . , }$ $\begin{array} { r } { \frac { d p } { d k } < 0 ) } \end{array}$ , leading to an increase in the cost of procurement. We <sup>fi</sup>nd that, under the given condition, the cost of procurement increases at a faster rate than the revenue, making the buyer surplus $( \mathrm { i . e . , }$ revenue – cost) go down as the technology becomes cheaper.

This result has important managerial implications because, historically, cost has been the key driver for technology adoption (Zhu and Weyant 2003). However, contrary to common belief (Thatcher and Oliver 2001), Proposition 2 shows that the pro<sup>fi</sup>t of the technology buyer can sometimes decrease even when the technology becomes cheaper. Our work contributes to the extant literature by providing conditions when migrating to cloud services for cost reasons does not make good business sense. Note that, although cloud computing offers a variety of advantages, in this proposition, we show how the falling cost of technology can also adversely affect <sup>fi</sup>rm pro<sup>fi</sup>tability.

## 4.3. Does the Firm Pass on More Benefits to End Users When the Technology Becomes Cheaper?

As mentioned earlier, the cost of technology, particularly storage and computing costs, has fallen drastically in recent years (Rosoff 2015). This has translated into lower prices from the cloud service providers. For instance, Google’s BigQuery has seen the largest price drop at 85% in 2014 (Babcock 2014), and AWS has slashed the S3 storage price by a massive 80% since inception (Barr 2016). Such examples abound in practice across a wide range of applications. In a B2B setting, this means that a technology <sup>fi</sup>rm, such as Uber, now has more disposable savings to share with its end users (e.g., through lower price or promotion). An important managerial question, thus, arises: should the buyer of cloud service pass on a larger portion of the total discount it receives from the seller to its end users when the technology becomes cheaper for the seller? Given that there is a relentless drop in the price of components and technology, this question becomes paramount for many businesses in order to retain their market share. In the following proposition, we attempt to answer this important question.

Proposition 3. Under the quantity discount contract, the buyer can sometimes decrease $\lambda ,$ that is, the proportion of the total discount it passes on to its end users, even when the technology gets cheaper for the seller (i.e., k is lower). Specifically, $\begin{array} { r } { \frac { d \Breve { \lambda } } { d k } > 0 } \end{array}$ when $( k \dot { X _ { 3 } } - Y _ { 3 } ) > 0$ . The expressions of $X _ { 3 }$ and $Y _ { 3 }$ are included in the proof.

In practice, passing on bene<sup>fi</sup>ts to consumers in the form of lower prices or promotion is common in many areas, such as fast fashion, groceries, pharmaceuticals, retail, ride-sharing, <sup>fi</sup>nancial services, and even <sup>fi</sup>ne dining. For example, Nissan cars recently got 3% cheaper as the automaker passed on the bene<sup>fi</sup>ts of lower taxation to the end consumers (Business Standard 2017). Similar observations can also be made fo technology products and services, such as computer hardware and software, broadband, medical equipment, satellite TV, VoIPs, and radio (Lyons and Coyne 2017). Therefore, one may expect the answer to the question to be “yes.” However, the proposition shows that this is not always the case. In fact, the buyer sometimes passes on a lower percentage of the total discount to its end users as the cost of technology falls.

As the technology becomes cheaper (i.e., k decreases), the focal vendor allocates a higher capacity (i.e., s increases). Consequently, the buyer procures a greater quantity under the discount contract (i.e., q increases). In response, the focal vendor <sup>fi</sup>nds it optimal to lower the discount coef<sup>fi</sup>cient d. These two forces have opposing effects on the total discount the buyer receives from the focal vendor. Under the given condition, the former effect dominates the latter resulting in a net increase in the total discount as k decreases. As a result, the buyer <sup>fi</sup>nds it optimal to pass on a smaller fraction of the total discount (i.e., λ decreases) and yet maintain a healthy level of demand.

The topic of passing on the bene<sup>fi</sup>ts of cost savings to end users has existed in practice for a while (Connor et al. 1998). This proposition has important managerial implication as managers are often unaware of whether the cost savings from technology innovations should be transferred to the end users, and if so, how much? Such questions are generally perplexing as, on the one hand, sharing savings can boost demand and improve customer loyalty, but on the other hand, it may hurt the <sup>fi</sup>rm’s pro<sup>fi</sup>tability because of greater cash out<sup>fl</sup>ow. Thus, what is an optimal pro<sup>fi</sup>t-sharing arrangement remains an unsolved question, especially when congestion plays a key role. The preceding proposition sheds light on this important question.

Competition policy, which ensures consumer wellbeing in a competitive market, often asks whether a “fair share” of the bene<sup>fi</sup>ts from cost savings should be shared with the end users (Weatherill 2018). Sharing of bene<sup>fi</sup>ts with end consumers has drawn consid erable attention in the past. Koopman et al. (2015) study a sharing economy and consumer protection regulation and <sup>fi</sup>nd that, in a competitive economy, <sup>fi</sup>rms can <sup>fi</sup>nd innovative ways to minimize their costs, passing on some of the savings to customers. Our results show that it is not always so, and in fact, <sup>fi</sup>rms can sometimes lower the percentage of the bene-<sup>fi</sup>ts they pass to end users. Kate and Niels (2005) study a somewhat similar problem as ours in which they examine whether a pro<sup>fi</sup>t-maximizing <sup>fi</sup>rm would share such bene<sup>fi</sup>ts. However, they do not analytically obtain the optimal sharing percentage. In this paper, we present the optimal portion of bene<sup>fi</sup>ts that a <sup>fi</sup>rm passes on to its end users, characterized by different discount and congestion sensitivities.

## 4.4. Should the Focal Vendor Provide a Higher Discount When End Users Are More Sensitive to Congestion?

The practice of offering deep discounts in the face of congestion is widely prevalent in the industry. Examples include cloud services, airlines, e-commerce, hospitality, apparel, and many others. As end users become more intolerant to poor service quality, congestion can shift business to competitors in no time. Kocak (2017) <sup>fi</sup>nds that an average online shopper visits at least three websites before making purchases. Thus, in a consumer-driven market, retaining end users is challenging when quality is unstable. One common way to build loyalty in end users is to offer attractive discounts. For example, AWS offers a 90% discount on spot instances when buyers are ready to adjust with frequent service disruption. This practice, although not new, is hardly sustainable. This leads to our fourth and <sup>fi</sup>nal research question: should the focal vendor offer a higher discount when buyers are more intolerant to congestion? Another related question follows: does the demand always go down when buyers are more intolerant to congestion? In the following proposition, we attempt to answer these questions.

## Proposition 4. Under a quantity discount contract,

1. The focal vendor actually provides a lower discount even when end users are more intolerant to congestion, that $\begin{array} { r } { i s , \frac { d ( d q ) } { d \alpha } < 0 } \end{array}$

2. The total demand can be higher under certain conditions even when end users are more intolerant to congestion. More specifically, ${ \frac { d E [ Q ] } { d \alpha } } > 0$ when $\begin{array} { r l } { ( A _ { 1 } \alpha - 2 k ) } & { { } \big ( \Breve { 8 k } ^ { 2 } ( A _ { 1 } + b ^ { * } p _ { f } ) } \end{array}$ $- 2 \dot { A _ { 1 } } k ( A _ { 1 } - 2 \ddot { b ^ { * } } p _ { f } ) \alpha + A _ { 1 } ^ { 3 } \alpha ^ { 2 } ) < 0 .$ , where $\overset { \cdot } { A _ { 1 } } = v - A$ and $A = b p _ { f } ^ { \cdot } + ( 1 - b ) \dot { p } _ { s }$

These results reveal interesting facts about the relationship between congestion and discount. Lee and Chen-Yu (2018) study the effect of price discounts on the consumer’s perception of quality. They <sup>fi</sup>nd that, when a price discount serves as a mediator, it can lead to a positive perception of product quality. Because congestion leads to poor quality, it may imply that the focal vendor is likely to offer a higher discount to compensate for the loss in service quality. Such pricing decisions are not uncommon in practice. Takeuchi and Quelch (1983) observe that many U.S. companies have experimented with a variety of promotional tactics to improve their quality image. Therefore, one may expect the answer to the question to be “yes.” However, we <sup>fi</sup>nd that this is not the case. In fact, our results suggest that both total demand and price can increase as end users’ congestion sensitivity becomes higher.

As the congestion sensitivity α increases, the buyer tends to procure less under the discount contract $( \mathrm { i . e . , } q$ decreases) and more from the PAYG service to ward off the negative effect of congestion. This demand shifting helps to improve the overall quality of services. As a result, the total demand Q can be higher when the end users are more congestion sensitive. Further, although the focal vendor can increase d to counter the negative effect of congestion, q decreases at a much faster rate, offsetting the effect of d. Consequently, the discount per unit <sub>(</sub>dq<sub>)</sub> decreases as α increases.

This <sup>fi</sup>nding has important managerial implications because business managers often get tempted to offer higher discounts when service quality degrades as a result of congestion. This is a common phenomenon in airlines, e-commerce, and many other market segments in which congestion is high and the price is an impor tant determinant (Heda et al. 2017). Our results show that this tendency may lead to a lower pro<sup>fi</sup>t for the focal vendor if the end users’ congestion sensitivity is not carefully assessed. If the congestion sensitivity is high, the positive effect of a discount is dominated by the negative effect of congestion sensitivity, thus forcing the focal vendor to offer a lower discount per unit.

Chen and Frank (2001) show that, contrary to the common assumption, <sup>fi</sup>rms do actually adjust their prices based on queue length (analogous to degree of congestion in our model). Wang and Zhang (2017) extend this research to <sup>fi</sup>nd the optimal price at which a <sup>fi</sup>rm sells its services in a service-inventory system with delay-sensitive customers and lost sales. Wang and Wu (2018) later study price competition between two servers with differentiated exogenous processing rates and <sup>fi</sup>nd that servers set their prices according to the delay sensitivity of customers and the symmetry of the competition. Our results are consistent with earlier research in that we also <sup>fi</sup>nd the seller of cloud services determines the discount in response to the buyer’s congestion sensitivity. We contribute to the literature by showing that the businesses can actually lower the discount when the buyer is more intolerant to congestion. Ma (2014) studies generic congestionprone network services, including cloud services, and <sup>fi</sup>nds how users’ value on usage and sensitivity to congestion in<sup>fl</sup>uence pricing, revenue, and social welfare. Although they study a similar setting, they do not consider a multicloud strategy as we do. Therefore, our results regarding buyer’s and seller’s decisions are different from those given in Ma (2014).

## 5. Robustness to Risk Specification

In this section, we demonstrate that the key insights of the propositions hold even if the quantity q purchased by the buyer under the discount contract is exposed to the same risk of failure to which the PAYG services are exposed as discussed in Section 3.3. When such risk affects $q ,$ the buyer chooses to procure a lower fraction of $( Q - q )$ from the focal vendor at the PAYG price. That is, the optimal choice of b is now lower than b∗ in our main model $( b ^ { * } )$ , as presented in Lemma EC.1, is the optimal choice of b when $q$ is not exposed to risk of failure). In order to establish that our results are robust, we show that the key insights of each proposition continue to hold even if the value of b is less than b∗. In the discussion that follows, we demonstrate the robustness of results of each of our four propositions.

Proposition 1 shows the nonmonotonicity of buyer surplus with respect to congestion sensitivity α. Figure 4 numerically demonstrates this nonmonotonicity in a parameter space in which the equilibrium is feasible. It further shows that the nonmonotonicity of buyer surplus with respect to α continues to hold even for values of $b < b ^ { * }$ . Proposition 2 shows the nonmonotonicity of buyer surplus with respect to capacity cost coef<sup>fi</sup>cient k. Figure 5(a) numerically demonstrates this nonmonotonicity in a parameter space in which the equilibrium is feasible. It further shows that the nonmonotonicity of buyer surplus with respect to k continues to hold even for values of $b < b ^ { * }$ Proposition 3 shows the nonmonotonicity of λ with respect to capacity cost coef<sup>fi</sup>cient k. Figure 5(b) numerically demonstrates this nonmonotonicity in a parameter space in which the equilibrium is feasible. It further shows that the nonmonotonicity of λ with respect to k continues to hold even for values of $b < b ^ { * }$

The <sup>fi</sup>rst part of Proposition 4 shows that the discount per unit under the discount contract with the focal vendor is decreasing in congestion sensitivity α . Figure 6(a) numerically demonstrates this relationship in a parameter space in which the equilibrium is feasible. It further shows that the discount per unit continues to decrease in α even for values of $b < b ^ { * }$ . The second part of Proposition 4 follows from showing that total demand is increasing in congestion sensitivity α . Figure 6(b) numerically demonstrates this relationship in a parameter space in which the equilibrium is feasible. It further shows that total demand continues to be increasing in α even for values of $b < b ^ { * }$

Figure 4. (Color online) E π vs. α at $\{ p _ { f } = 0 . 7 , p _ { s } = 0 . 6 , r _ { f } =$ $0 . 5 , r _ { s } = 0 . 5 , Q _ { 0 } = 2 0 , \beta = 0 . 1 , k = 1 , v = 1 \}$  
![](/api/attachments/NWPWWW67/fulltext/images/c60a983dc59c3cd43f258f44c72210b6c508d33c1df0c7ee23d62f931624df7e.jpg)

## 6. Market Share Contract as a Potentia Contract Mechanism

The adoption of a multicloud strategy brings new challenges and opportunities to <sup>fi</sup>rms that operate in the market for the cloud. As we discuss earlier, buyers must make a key strategic decision regarding whether and how to source from multiple providers (Hong and Pavlou 2017). Although it may be cheaper for a buyer to source all its needs from a single vendor, the negative effect of congestion and risk motivates a buyer to ful<sup>fi</sup>ll a part of its demand from a competing seller. This requires sellers to be more competitive and innovative in designing contracts. One such contract that stimulates demand through inducing loyalty is a market share or share-of-wallet contract (Calzolari and Denicolo\` 2018). Although, under the quantity discount contract, the discount depends on the “absolute purchase quantity,” in a market share contract, the discount is linked to the “share of the total purchase” of the buyer with the seller. As the existing literature suggests, the motivations for using a market share contract include using it as a rent-shifting device (Marx and Shaffer 2004), mitigating risk (Akgun and¨ Chioveanu 2013), or facilitating price discrimination (Majumdar and Shaffer 2009).

Subscription-based contracts, such as Amazon’s Reserved Instances (RI) or Google’s committed use plan, are ideal grounds for market share contracts. Most subscription plans offer attractive discounts based on the size and tenure of the contract. For example, Amazon’s RI provides discounts up to 75% compared with the on-demand pricing for a tenure up to three years. However, the exact form of such discounts is not publicly announced; instead, they are privately negotiated, opaque, and can involve price discrimination. Given the limited number of cloud vendors and thei market power, this provides an opportunity for the seller to engage in a market share contract with an incumbent buyer. Furthermore, although the quantity discount and the market share contracts are identical when the expected demand is known (Vassallo 2012), situations might arise when the buyer and the seller are uncertain about the demand. In the presence of congestion, too, the realized total demand can vary based on the choice of contract and the demand allocation that follows. As the market share contract does not depend on absolute purchase quantity, it is independent of the buyer sizes and more <sup>fl</sup>exible when the demand is uncertain. Because the buyers’ needs in the cloud market are varied and demand is uncertain, market share contracts are a potential mechanism in this market. Therefore, we also look at congestion in the context of market share contracts.

Figure 5. (Color online) Sensitivity of E<sub>[</sub>π<sub>b]</sub> and λ with Respect to k at $\{ p _ { f } = 0 . 5 , p _ { s } = 0 . 5 , r _ { f } = 0 . 5 , r _ { s } = 0 . 5 , Q _ { 0 } = 1 , \alpha = 1 , \beta = 1 , v = 0 . 7 5 \}$ (a) (b)  
![](/api/attachments/NWPWWW67/fulltext/images/b972ed97778c56d5dbac26a15708036ec9ace1499b698df8b71ebc5cc9c21edd.jpg)  
Notes. (a) E π versus k. (b) λ versus k.

![](/api/attachments/NWPWWW67/fulltext/images/23fb818d14582ddfc57df0586224a128e61bf32d5dbe9daa1a856ac4f00da857.jpg)

One of the major concerns that makes market share contracts relatively dif<sup>fi</sup>cult to implement is their monitoring requirement. Under a market share contract, buyers are incentivized to misreport to hide purchases from outside vendors and avail a higher discount from the focal vendor. Prior literature contends that such contracts are practiced by having a clause binding the buyer to disclose its same-category purchase from another vendor. Such contracts come under the umbrella of contracts that reference rivals (Morton 2012). However, enforcing such a contract is not necessarily costless for the vendor. The prior literature acknowledges such a cost (Chen and Shaffer 2016) but does not explicitly model it.

There are two factors to consider when enforcing such a contract: (1) whether it is technologically possible to monitor and (2) how the cost of monitoring would impact the equilibrium outcome in our setup. There are multiple cloud management platforms (CMPs) that enable organizations to manage multicloud services and resources. “These include provisioning and orchestration; service request management; inventory and classi<sup>fi</sup>cation; monitoring and analytics; cost management and resource optimization; cloud migration, backup and disaster recovery; and identity, security and compliance” (Smith et al. 2019). Notably, even Google, despite being one of the largest public cloud vendors itself, has a platform known as Anthos that also lets enterprises manage workloads running on third-party clouds such as AWS and Azure (Google 2019). Essentially, these CMPs, while pursuing a multicloud strategy, are also able to implement contracts that require monitoring purchases from rivals. Even if one considers that there is a <sup>fi</sup>xed cost of monitoring, it does not change our results qualitatively.

Figure 6. (Color online) Sensitivity of dq and E<sub>[</sub>Q<sub>]</sub> with Respect to α at $\{ p _ { f } = 0 . 5 , p _ { s } = 0 . 5 , r _ { f } = 0 . 5 , r _ { s } = 0 . 5 , Q _ { 0 } = 1 , \beta = 1 , k = 1 , v = 0 . 7 5 \}$  
![](/api/attachments/NWPWWW67/fulltext/images/55a794fc392177b1abcc7fe65869d13f2d64c68ee36599ff77956b38a97f05a6.jpg)  
Notes. (a) dq versus α. (b) E Q versus α.

![](/api/attachments/NWPWWW67/fulltext/images/5c0bafddb5265baa22f74359ffda14037e4c111dae6dd8aa9bd476c2b106c099.jpg)

## 6.1. Model Setup, Game Sequence, and Solution Approach

We keep our model setup and notations the same as in Section 3 and discuss only those aspects that are different when a market share contract is adopted instead of a quantity discount contract. In our context, we consider the implementation of a market share contract as follows: when the buyer procures q units of cloud services from the focal vendor using the market share contract and it buys $q _ { f }$ units from the focal vendor and $q _ { s }$ units from the spot vendor at the respective PAYG prices, although the discount is applied to quantity $q ,$ the discount depends on the buyer’s share of the total purchase with the focal vendor measured as $\textstyle \frac { q + q _ { f } } { Q } .$ . The discounted price per unit, $p ,$ is expressed as

$$
p = p _ {f} - d \left(\frac {q + q _ {f}}{Q}\right).\tag{7}
$$

The formulation of the total demand remains the same except the last term, in which the amount of discount is calculated as per the market share contract. The total demand is given as

$$
Q = (Q _ {0} + \epsilon) - \alpha \Big ([ q - s ] ^ {+} \Big) ^ {2} + \beta \sqrt {\lambda d \bigg (\frac {q + q _ {f}}{Q} \bigg) q}.\tag{8}
$$

Because the buyer’s utility depends on the amount of discount it passes on to its end users, the formulation of the buyer’s net utility is also updated to incorporate how the discount is computed under this contract. The buyer’s utility is given as

$$
\pi_ {b} = v Q - \lambda d \biggl (\frac {q + q _ {f}}{Q} \biggr) q - p q - p _ {f} q _ {f} - p _ {s} q _ {s},\tag{9}
$$

where $p$ and $Q$ are de<sup>fi</sup>ned in Equations (7) and (8). The pro<sup>fi</sup>t of the focal vendor is given as

$$
\pi_ {f} = p q + p _ {f} q _ {f} - k s ^ {2}.\tag{10}
$$

Although the discount under the market share contract is based on the fraction of the total demand the buyer procures from the focal vendor, this fraction is not known to the buyer or the seller until the demand is realized. Therefore, we solve the game using the concept of ful<sup>fi</sup>lled Nash equilibrium (Mantena and Saha 2012). Following this solution approach in the context of our model setup, we consider that the players in the game—the focal vendor and the buyer— make their decision ex ante based on what they expect to be the total allocated demand to the focal vendor (i.e., E q  q<sub>f</sub> ) as a proportion of the expected total demand (i.e., E Q ). In equilibrium, this expectation is ful<sup>fi</sup>lled. We denote the expected fraction as $\hat { f } .$ . The game sequence is the same as before except that the players make decisions with the knowledge of $\hat { f } .$ . In equilibrium $\cdot \hat { f }$ equals $\frac { q ^ { * } + q _ { f } ^ { * } } { Q ^ { * } }$

The players in the game, make the decision with the knowledge o $\hat { f }$ . Consequently, p and $Q$ are expressed as

$$
p = p _ {f} - d \hat {f},\tag{11}
$$

$$
Q = (Q _ {0} + \epsilon) - \alpha ([ q - s ] ^ {+}) ^ {2} + \beta \sqrt {\lambda d \hat {f} q}.\tag{12}
$$

The buyer’s and the cloud vendor’s objectives are also updated accordingly as follows. The buyer’s utility maximization problem is given as

$$
\max _ {q \geq 0, \lambda \in [ 0, 1 ]} E [ \pi_ {b} ] = \max _ {q \geq 0, \lambda \in [ 0, 1 ]} E \Big [ v Q - \lambda d \hat {f} q - p q - p _ {f} q _ {f} - p _ {s} q _ {s} \Big ].\tag{13}
$$

The buyer’s risk minimization problem is given as

$$
\min _ {b \in [ 0, 1 ]} E [ r _ {b} ] = \min _ {b \in [ 0, 1 ]} E \bigl [ (p _ {f} q _ {f} + p _ {s} q _ {s}) + (b r _ {f} q _ {f} + (1 - b) r _ {s} q _ {s}) \bigr ].\tag{14}
$$

The focal vendor’s pro<sup>fi</sup>t maximization problem is

$$
\max _ {d \geq 0, s \geq 0} E [ \pi_ {f} ] = \max _ {d \geq 0, s \geq 0} E \Big [ p q + p _ {f} q _ {f} - k s ^ {2} \Big ].\tag{15}
$$

Lemma EC.2 presents the equilibrium outcome under the market share contract. Both the lemma and its proof are included in the online appendix.

## 6.2. Does a Market Share Contract Hurt the Buyer?

Although a market share contract is not exactly the same as the exclusivity contract, it still suffers from the criticism that it can hurt competition and put the buyer at a disadvantage. For example, Ordover and Shaffer (2013) show that a dominant <sup>fi</sup>rm’s use of market share contracts can be exclusionary. Therefore, whether a market share contract hurts buyer surplus is an interesting question. On the one hand, the buyer is worried about overcommitting to a single vendor. On the other hand, the buyer enjoys superior bargaining power if a higher market share is committed. Therefore, in this section, we verify if buyer surplus is always lower under a market share contract compared with that under a quantity discount contract.

The answer follows from comparing the equilibrium outcome under the quantity discount contract (as presented in Lemma EC.1) and market share contract (as presented in Lemma EC.2). In Figure $^ { 7 , }$ we plot buyer surplus $( \pi _ { b } )$ under both quantity discount and market share contracts with respect to the end users congestion sensitivity (α). The plot corresponds to the parameter space $\dot { \{ p _ { f } = 0 . 5 , p _ { s } = 0 . 5 , r _ { f } = 0 . 5 , r _ { s } = 0 . 5 , }$

Figure 7. (Color online) Buyer Surplus (π<sub>b</sub>) vs. Congestion Sensitivity (α)  
![](/api/attachments/NWPWWW67/fulltext/images/631fe26a42aa0673cc8ebc76e4d40a51e0f8de6070f69f22d3ea8269e37239c0.jpg)

$Q _ { 0 } = 1 0 , 1 \le \alpha \le 4 , \beta = 0 . 4 , k = 1 , v = 0 . 7 5 \}$ in which both market share and quantity discount contracts are feasible. We <sup>fi</sup>nd that the buyer surplus under the market share contract is higher compared with that under the quantity discount contract when the end users’ congestion sensitivity $( \mathrm { i } . \mathrm { e } . , \ \alpha )$ is low. The following observation formally states this result.

Observation 1. Buyer surplus under a market share contract can sometimes be higher compared with that under a quantity discount contract, especially when the end users congestion sensitivity (α) is low.

This observation has important managerial implications as it is not intuitive whether buyers bene<sup>fi</sup>t when a market share contract is offered by a seller. If the market share contract is a contract mechanism that only facilitates a seller, we would observe that, when such a contract is implemented, it is the seller whose pro<sup>fi</sup>t would increase resulting from a higher payment transfer from the buyer to the seller. However, we interestingly <sup>fi</sup>nd that, under such a contract, the buyer surplus can also be higher when the end users’ congestion sensitivity is low. Therefore, although a market share contract may look like an overcommitment from the buyer’s perspective, it is not necessarily always bad for the buyer.

## 7. Discussion and Conclusion

\- Market Share Contract - - - -- Quantity Discount Contract

Although the discount is an effective tool to stimulate demand and reward customer loyalty, a seller needs to take into account certain nuances in its pricing decision that are unique to the nature of products or services it offers. In this study, we focus on one such nuance, called congestion, in the pricing for cloud services. Discount-based contracts are common in cloud services. One common form of the discountbased B2B contract is a quantity discount contract, wherein a buyer receives a discount proportional to the volume it procures from the vendor. However, the nature of cloud-based services poses an additional challenge in the seller’s pricing decision. Cloud-based services are prone to congestion as the demand gets higher, resulting in lower service quality, eventually leading to loss of revenue and customer base. On the one hand, a higher discount can increase the demand; on the other hand, it can create more congestion, which, in turn, lowers the demand and impacts pro<sup>fi</sup>tability. Therefore, a seller should be careful when balancing these two opposing forces optimally when making its pricing decision.

We build an analytical model to understand the equilibrium outcome under a quantity discount contract. We consider a single-period setting in which a <sup>fi</sup>rm (the buyer or the client) buys cloud services from other <sup>fi</sup>rms (the seller or the vendor) to run its business. We consider two vendors that provide cloud services. We consider the focal vendor to be strategic and the other as a spot vendor that represents the outside options for the buyer. The focal vendor offers both low- and high-quality services, whereas the spot ven dor offers only high-quality services. We characterize the nature of the demand for cloud services using a demand function that incorporates the positive impact of the discount as well as the negative impact of congestion on demand. The buyer allocates the demand between the two vendors in such a way that it minimizes the impact of congestion and risks.

## 7.1. Managerial Implications

In this study, we particularly attempt to answer some important questions that have signi<sup>fi</sup>cant managerial implications on both the buyer and seller of cloud service. Our <sup>fi</sup>rst question is, do more congestionsensitive end users hurt the buyer? We <sup>fi</sup>nd that this is not necessarily true. In fact, the buyer surplus can sometimes increase even when the end users are more intolerant to congestion. This result has important managerial implication as offering deep discounts has become an increasingly common phenomenon in recent times. Unnecessary discounts may hurt the buyer’s pro<sup>fi</sup>tability and damage the buyer’s brand image in the long run. Our result suggests that managers do not always have to do that.

In the second research question, we study the following: does a lower cost of technology always bene<sup>fi</sup> the buyer of cloud services? Contrary to popular belief, our results suggest that the buyer can actually be worse off even when the technology becomes cheaper for the seller. This is an interesting <sup>fi</sup>nding and has considerable implications for managers, who must assess the effect of technology costs carefully. Notably, the buyer does not necessarily bene<sup>fi</sup>t as the technology becomes cheaper for the cloud vendor.

A related question that follows concerns what happens to the end users when the technology becomes cheaper for the cloud service provider. More formally, does the buyer increase the portion of the bene<sup>fi</sup>ts it passes to the end users when the technology becomes cheaper for the seller? Anecdotal examples suggest that the buyer usually increases the portion of bene<sup>fi</sup>ts it passes on to its end users (typically in the form of lower prices or promotions) as technology costs decline. However, our results suggest that this price reduction is not always the optimal strategy. Under certain conditions, the buyer can actually decrease the portion of bene<sup>fi</sup>ts it passes on to the end users. This result sheds light on the optimal pro<sup>fi</sup>t-sharing arrangement between the buyer and the end users and provides useful insights for the buyer.

Finally, we study our last research question: should the focal vendor offer a higher discount when buyers are more intolerant to congestion? We <sup>fi</sup>nd that, when end users are more congestion sensitive, sellers can increase the price for the buyer instead of lowering it. This result is somewhat counterintuitive as the examples suggest managers tend to offer higher discounts when service quality degrades because of congestion. Simultaneously, we also note that the total demand for cloud services can go up when end users are more congestion sensitive. In the next section, we discuss the limitations of our model and some future research directions.

## 7.2. Limitations and Future Research Directions

Although our model captures the effect of congestion on the strategic choices of the buyer and seller quite realistically, it has some limitations and, therefore, can pave the way for new research questions. For example, <sup>fi</sup>rst, we have not modeled the decisions of the spot vendor; we modeled only the strategic interactions of the buyer and the focal vendor. Although this setup is not unrealistic as it captures the buyer’s outside option quite reasonably, one can explicitly model a duopoly competition in which the buyer can have the option to sign a discount contract with both vendors. Doing so can further shed light on how the nature of contracts differs across the two vendors if vendors are differentiated based on their technological capabilities or how they <sup>fi</sup>t the preference of the buyer under consideration.

Second, we consider the PAYG prices from the two vendors to be exogenous in our model. One can endogenize the PAYG prices from the two vendors and see how the nature of the discount contract is linked with these choices. Consequently, one can explore how these choices of PAYG price vary between the focal and the spot vendor. However, considering the PAYG price to be exogenous in our model is reasonable enough, at least, in the short term as we observe that PAYG prices (or on-demand rates, etc.) are usually stable over time. It is the nature of the discount with reference to the PAYG price that gets decided at the individual contract level.

Third, we model the demand at the macro level. Although it captures the effect of congestion and discount sensitivity for end users on the total demand reasonably, one can model the mechanism of demand generation at the user level, taking into the account the heterogeneity of end users with respect to these two dimensions. Although doing so is not expected to contradict our results, it may further enable the buye to make more granular decisions while interacting with end users; it could be along the line of to whom to pass on more versus less discount, whom to serve with low- versus high-quality cloud services, etc. Being able to make these granular decisions more optimally at the end-user level, the buyer can further <sup>fi</sup>ne-tune its demand allocation strategy in the presence of congestion.

## Endnotes

<sup>1</sup> AWS charges \$0.023 per GB up to 50 TB storage, \$0.022 per GB for 51–100 TB storage, and \$0.021 per GB for 100<sup>+</sup> TB storage (Amazon 2020).

<sup>2</sup> The price implies the price per unit of cloud capacity, and capacity can be in any form from storage to memory to computing power.

<sup>3</sup> We use end users and customers interchangeably to represent the final users of the service provided by the buyer.

<sup>4</sup> Quality of web-based services is formalized between the buyer and seller through service-level agreements.

<sup>5</sup> See https://www.grabon.in/netflix-coupons (last accessed October 4, 2020).

<sup>6</sup> In Section 5, we numerically demonstrate that our key insights hold even if the quantity purchased under the discount contract is exposed to the risk of failure.

## References

Akamai (2017) Akamai online retail performance report: Milliseconds are critical. Accessed October 5, 2020, https://tinyurl com/y4jrompg.

Akgun U, Chioveanu I (2013) Loyalty discounts.¨ B.E. J. Econom. Anal. Policy 13(2):655–685.

Amazon (2020) AWS pricing—How does AWS pricing work? Accessed October 4, 2020, https://aws.amazon.com/pricing/.

Anselmi J, Ardagna D, Lui JC, Wierman A, Xu Y, Yang Z (2017) The economics of the cloud. ACM Trans. Model. Performance Evaluation Comput. Systems 2(4):1–23.

Arbabian ME, Chen S, Moinzadeh K (2020) Capacity expansions with bundled supplies of attributes: An application to server procurement in cloud computing. Manufacturing Service Oper. Management 23(1):191–209.

August T, Niculescu MF, Shin H (2014) Cloud implications on soft ware network structure and security risks. Inform. Systems Res. 25(3):489–510.

Babcock C (2014) Amazon counters Google Cloud price cuts. Accessed October 4, 2020, https://tinyurl.com/yyqxdp43.

Barr J (2016) AWS storage update—S3 & Glacier price reductions additional retrieval options for Glacier. Accessed October 4, 2020, https://preview.tinyurl.com/zhgx8ck.

Bishop M, Snyder ME, Okin H (2015) Cloud economics: Making the business case for cloud. Technical report, KPMG.

Blome C, Henke M (2009) Single vs. multiple sourcing: A supply risk management perspective. Zsidisin GA, Ritchie B, eds. Sup ply Chain Risk, International Series in Operations Research & Management Science, vol. 124 (Springer, Boston), 125–135.

Buell RW, Campbell D, Frei FX (2016) How do customers respond to increased service quality competition? Manufacturing Service Oper. Management 18(4):585–607.

Business Standard (2017) Nissan India cars get 3% cheaper as <sup>fi</sup>rm passes on GST bene<sup>fi</sup>ts to buyers. Accessed October 4, 2020, https://tinyurl.com/55px7ftp.

Calzolari G, Denicolo V (2018) Price-cost tests and loyalty discounts.\` Technical report, CEPR Discussion Paper No. DP12924, London.

Cerin C, Coti C, Delort P, Diaz F, Gagnaire M, Gaumer Q, Guil-´ laume N, et al. (2013) Downtime statistics of current cloud solu tions. Technical report, International Working Group on Cloud Computing Resiliency, Paris.

Chan CW, Green LV, Lekwijit S, Lu L, Escobar G (2019) Assessing the impact of service level when customer needs are uncertain: An empirical investigation of hospital step-down units. Management Sci. 65(2):751–775.

Chen H, Frank MZ (2001) State dependent pricing with a queue. IIE Trans. 33(10):847–860.

Chen Z, Shaffer G (2016) Are market-share contracts a poor man’s exclusive dealing? Technical report, Monash University, Department of Economics, Melbourne, London.

Chen PY, Wu SY (2013) The impact and implications of on-demand services on market structure. Inform. Systems Res. 24(3):750–767.

Chen S, Lee H, Moinzadeh K (2019) Pricing schemes in cloud computing: Utilization-based vs. reservation-based. Production Oper. Management 28(1):82–102.

Cheng HK, Li Z, Naranjo A (2016) Research note—Cloud comput ing spot pricing dynamics: Latency and limits to arbitrage. Inform. Systems Res. 27(1):145–165.

Chung SP, Lu YJ, Lai YC (2018) Cloud computing with single server threshold and double congestion thresholds. ICT Express 4(3): 119–123.

Connor RA, Feldman RD, Dowd BE (1998) The effects of market concentration and horizontal mergers on hospital costs and pri ces. Internat. J. Econom. Bus. 5(2):159–180.

Dass M, Kumar P, Peev PP (2013) Brand vulnerability to product assortments and prices. J. Marketing Management 29(7–8):735–754.

De Ruyter K, Wetzels M, Bloemer J (1998) On the relationship between perceived service quality, service loyalty and switching costs. Internat. J. Service Indust. Management 9(5):436–453.

Donnelly C (2016) Public cloud competition prompts 66% drop in prices since 2013, research reveals. Accessed October 4, 2020, https://tinyurl.com/y5j3dhzt.

Du AY, Das S, Ramesh R (2013) Ef<sup>fi</sup>cient risk hedging by dynamic forward pricing: A study in cloud computing. INFORMS J. Comput. 25(4):625–642.

Fazli A, Sayedi A, Shulman JD (2018) The effects of autoscaling in cloud computing. Management Sci. 64(11):5149–5163.

Galov N (2020) Cloud adoption statistics for 2020. Accessed December 20, 2020, https://hostingtribunal.com/blog/cloud-adoptionstatistics/#gref.

Gartner (2019) Gartner forecasts worldwide public cloud revenue to grow 17.5 percent in 2019. Accessed October 5, 2020, https:// tinyurl.com/y5rtefd2.

Gelles D (2019) Larry Ellison on the economy, the cloud, and sailing. Accessed October 2, 2020, https://tinyurl.com/wqzkspy.

Gera A, Xia CH (2011) Learning curves and stochastic models for pricing and provisioning cloud computing services. Service Sci. 3(1):99–109.

Google (2019) Introducing Anthos: An entirely new platform fo managing applications in today’s multi-cloud world. Accessed October 4, 2020, https://tinyurl.com/y3afjjlq.

Google (2020) Committed use discounts. Accessed October 4, 2020, https://cloud.google.com/compute/docs/instances/signing up-committed-use-discounts/.

Guerin R, Hosanagar K, Li X, Sen S (2019) Shared or dedicated infrastructures: On the impact of reprovisioning ability. Management Inform. Systems Quart. 43(4):1059–1079.

Guinn J (2015) The top retail pricing strategy for your business. Ac cessed October 5, 2020, https://tinyurl.com/wl2qsw9.

Hassin R, Haviv M (2003) To Queue or Not to Queue: Equilibrium Behavior in Queueing Systems, International Series in Operation Research & Management Science, vol. 59 (Springer, US).

Heda S, Mewborn S, Caine S (2017) How customers perceive a price is as important as the price itself. Harvard Business Review Online. Accessed July 25, 2021, https://tinyurl.com/hyt7uns.

Help Net Security (2018) 86% of enterprises have adopted a multi cloud strategy. Accessed October 5, 2020, https://tinyurl.com u97l7eu.

Hong Y, Pavlou PA (2017) On buyer selection of service providers in online outsourcing platforms for it services. Inform. Systems. Res. 28(3):547–562.

Hong J, Dreibholz T, Schenkel JA, Hu JA (2019) An overview of multi-cloud computing. Xhafa F, Barolli L, Takizawa M, Enokido T, eds. Workshops Internat. Conf. Adv. Inform. Network ing Appl. (Springer Cham, Switzerland), 1055–1068.

Hosseini L, Tang S, Mookerjee V, Sriskandarajah C (2020) A switch in time saves the dime: A model to reduce rental cost in cloud computing. Inform. Systems Res. 31(3):753–775.

Howland D (2015) Target site crashes Cyber Monday, while slow Wal-Mart site impedes some Black Friday doorbusters. Ac cessed January 23, 2021, https://tinyurl.com/yjl2y86r.

Huang J, Leng M, Parlar M (2013) Demand functions in decision modeling: A comprehensive survey and research directions. Decision Sci. 44(3):557–609.

Jain T, Hazra J (2019) “On-demand” pricing and capacity management in cloud computing. J. Revenue Pricing Management 18(3): 228–246.

Kansal S, Kumar H, Kaushal S, Sangaiah AK (2020) Genetic algorithmbased cost minimization pricing model for on-demand IaaS cloud service. J. Supercomputing 76(3):1536–1561.

Kate AT, Niels G (2005) To what extent are cost savings passed on to consumers? An oligopoly approach. Eur. J. Law Econom. 20(3): 323–337.

Khatri B (2018) Ecommerce behemoth Amazon India modi<sup>fi</sup>es seller fees to engage more sellers. Accessed October 4, 2020, https:// tinyurl.com/yxplaqwm.

Kocak Y (2017) Pricing facts: Infographic striking data from Prisync. Accessed October 5, 2020, https://tinyurl.com/y6nl55yb.

Koo J, Ahn S, Chung J (2012) A comparative study of queue, delay, and loss characteristics of AQM schemes in QoS-enabled net works. Comput. Inform. 23(4):317–335.

Koopman C, Mitchell MD, Thierer AD (2015) The sharing economy and consumer protection regulation: The case for policy change. J. Bus. Entrepreneurship Law 8(2):529.

Krishnan SS, Sitaraman RK (2013) Video stream quality impacts viewer behavior: Inferring causality using quasi-experimental designs. IEEE/ACM Trans. Networking 21(6):2001–2014.

Lee JE, Chen-Yu JH (2018) Effects of price discount on consumers perceptions of savings, quality, and value for apparel products: Mediating effect of price discount affect. Fashion Textiles 5(1):13.

Lee H, Whang S (2002) The impact of the secondary market on the supply chain. Management Sci. 48(6):719–731.

Li B, Kumar S (2018) Should you kill or embrace your competitor: Cloud service and competition strategy. Production Oper. Man agement 27(5):822–838.

Li S, Huang J, Li SR (2009) Revenue maximization for communication networks with usage-based pricing. Ulema M, ed. Proc. Global Comm. Conf. (IEEE, Honolulu), 4889–4894.

Lyons S, Coyne B (2017) The price of broadband quality: Tracking the changing valuation of service characteristics. Econom. Innovation New Tech. 26(6):516–532.

Ma RTB (2014) Pay-as-you-go pricing and competition in congested network service markets. IEEE 22nd Internat. Conf. Network Pro tocols (IEEE, Raleigh, NC), 257–268.

Ma D, Seidmann A (2015) Analyzing software as a service with pertransaction charges. Inform. Systems Res. 26(2):360–378.

Majumdar A, Shaffer G (2009) Market-share contracts with asymmetric information. J. Econom. Management Strategy 18(2):393–421.

Mantena R, Saha RL (2012) Co-opetition between differentiated plat forms in two-sided markets. J. Management Inform. Systems 29(2): 109–140.

Marx LM, Shaffer G (2004) Rent shifting, exclusion and marketshare discounts. Working paper, Duke University, Raleigh, NC.

Miller R (2017) Why Dropbox decided to drop AWS and build its own infrastructure and network. Accessed October 5, 2020, https://tinyurl.com/uqapj8w.

Morton FMS (2012) Contracts that reference rivals. Antitrust 27(3):72.

Mueller C (2015) The video problem: 3 reasons why users leave a website with badly implemented video. Accessed October 5, 2020, https://tinyurl.com/yhlcevky.

Nair SK, Bapna R (2001) An application of yield management for in ternet service providers. Naval Res. Logist. 48(5):348–362.

Nasr R (2015) Target site back after Cyber Monday TKO. Accessed January 23, 2021, https://www.cnbc.com/2015/11/30/paypalappears-to-be-down-on-cyber-monday.html.

Nordhaus WD (2001) The progress of computing. Yale Cowles Foundation Discussion Paper No. 1324, Yale University, New Haven, CT.

OnBlastBlog (2016) How to increase WordPress speed. Accessed February 5, 2021, https://www.onblastblog.com/speedwordpress/.

Ordover JA, Shaffer G (2013) Exclusionary discounts. Internat. J. Indust. Organ. 31(5):569–586.

Paschalidis IC, Tsitsiklis JN (2000) Congestion-dependent pricing of network services. IEEE/ACM Trans. Networking 8(2):171–184.

Passacantando M, Ardagna D, Savi A (2016) Service provisioning problem in cloud and multi-cloud systems. INFORMS J. Comput. 28(2):265–277.

Petruzzi NC, Dada M (1999) Pricing and the newsvendor problem: A review with extensions. Oper. Res. 47(2):183–194.

PTI (2019) YouTube, Snapchat network congestion issues in eastern United States now <sup>fi</sup>xed. Business Today, Accessed October 5, 2020, https://tinyurl.com/rd8uc3p.

Richman D (2016) Adobe’s use of Microsoft Azure will complement, not replace, AWS and its own cloud. Accessed February 20, 2021, https://tinyurl.com/yhlkogjv.

Rivenes L (2016) The negative effects of your network congestion problem. Accessed October 5, 2020, https://tinyurl.com/ uushlxo.

Robertson M (2018) Instagram Marketing: How to Grow Your Instagram Page and Gain Millions of Followers Quickly with Step-by-Step

Social Media Marketing Strategies (Createspace Independent Publishing Platform, California).

Rosenthal DS, Rosenthal D, Miller EL, Adams I, Storer MW, Zadok E (2012) The economics of long-term digital storage. Duranti L, Shaffer E, eds. The Memory of the World in the Digital Age: Digitization and Preservation. (UNESCO, Vancouver), 513–528.

Rosoff M (2015) Why is tech getting cheaper? Accessed October 4, 2020, https://www.weforum.org/agenda/2015/10/why-is-tech -getting-cheaper/.

Shen H, Li Z (2015) New bandwidth sharing and pricing policies to achieve a win-win situation for cloud provider and tenants. IEEE Trans. Parallel Distribution Systems 27(9):2682–2697.

Smith BC, Leimkuhler JF, Darrow RM (1992) Yield management at American Airlines. Interfaces 22(1):8–31.

Smith D, Cheung M, Fletcher C, Byrne P (2019) Gartner magic quadrant for cloud management platforms. Accessed October 5, 2020, https://tinyurl.com/y4pa96yh.

Soni A, Hasan M (2017) Pricing schemes in cloud computing: A review. Internat. J. Adv. Comput. Res. 7(29):60–70.

Stone C (2015) Losing image quality when uploading to Dropbox. Accessed October 5, 2020, https://tinyurl.com/qu79wew.

Stringam B, Gerdes J (2019) Service gap in hotel website load performance. Internat. Hospitality Rev. 33(1):16–29.

Sunar N, Tu Y, Ziya S (2021) Pooled vs. dedicated queues when customers are delay-sensitive. Management Sci. 67(6):3785–3802.

Takeuchi H, Quelch J (1983) Quality is more than making a good product. Harvard Bus. Rev. 61(4):139–145.

Talluri KT, Van Ryzin GJ (2006) The Theory and Practice of Revenue Management, vol. 68 (Springer Science & Business Media).

Tchernykh A, Schwiegelsohn U, Talbi EG, Babenko M (2019) Toward understanding uncertainty in cloud computing with risks of con<sup>fi</sup>dentiality, integrity, and availability. J. Comput. Sci. 36: 100581.

Tevelson R, Zygelman J, Farrell P, Benett S, Rosenfeld P, Alsen A´ (2013) Buyer-supplier collaboration: A roadmap for success. Ac cessed October 5, 2020, https://tinyurl.com/qvywuxu.

Thatcher ME, Oliver JR (2001) The impact of technology investments on a <sup>fi</sup>rm’s production ef<sup>fi</sup>ciency, product quality, and productivity. J. Management Inform. Systems 18(2):17–45.

Tomlin B, Wang Y (2005) On the value of mix <sup>fl</sup>exibility and dual sourcing in unreliable newsvendor networks. Manufacturin Service Oper. Management 7(1):37–57

Vassallo A (2012) Market share discounts. Working paper, Rutgers University, New Brunswick, NJ.

Venkatesan R (1992) Strategic sourcing: To make or not to make. Harvard Bus. Rev. 70(6):98–107.

Vilaplana J, Solsona F, Teixido I, Mateo J, Abella F, Rius J (2014) A´ queuing theory model for cloud computing. J. Supercomputing 69(1):492–507.

Wang N, Wu J (2018) Optimal cloud instance acquisition via IaaS cloud brokerage with volume discount. IEEE/ACM 26th Internat. Sympos. Quality Service (IEEE, Banff, AB), 1–10.

Wang J, Zhang X (2017) Optimal pricing in a service-inventory system with delay-sensitive customers and lost sales. Internat. J. Production Res. 55(22):6883–6902.

Wang H, Olsen TL, Liu G (2018) Service capacity competition with peak arrivals and delay sensitive customers. Omega 77:80–95.

Weatherill S (2018) The links between competition policy and con sumer protection. Yearbook Consumer Law 2007:187–209.

Weinman J (2011) The future of cloud computing. IEEE Tech. Time Machine Sympos. Tech Beyond 2020 (IEEE Hong Kong), 7–8.

Welzl M (2005) Network Congestion Control: Managing Internet Traffi (John Wiley & Sons)

Wilson RB (1993) Nonlinear Pricing (Oxford University Press on Demand).

Wilson M (2018) Survey: Most companies use multicloud, but far less have tools for management. Accessed February 20, 2021, https://tinyurl.com/ydr6n9nf.

Yuan S, Das S, Ramesh R, Qiao C (2018) Service agreement trifecta: Backup resources, price and penalty in the availability-aware cloud. Inform. Systems Res. 29(4):947–964.

Zhang H, Chao X, Shi C (2020) Closing the gap: A learning algorithm for lost-sales inventory systems with lead times. Management Sci. 66(5):1962–1980.

Zhu K, Weyant JP (2003) Strategic decisions of new technology adoption under asymmetric information: A game-theoretic model. Decision Sci. 34(4):643–675.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
