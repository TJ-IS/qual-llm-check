---
otero_id: 14660
otero_key: "Y2VC9CFY"
title: "Selling or Leasing? Pricing Information Goods with Depreciation of Consumer Valuation"
authors: "Yifan Dou; Yu Jeffrey Hu; D. J. Wu"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0698"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

## H4R

![](/api/attachments/Y2VC9CFY/fulltext/images/2c261793cbac1d2f263b3e3ef98d64138af82d959e7b4adf5184305c30c6911b.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Selling or Leasing? Pricing Information Goods with Depreciation of Consumer Valuation

http://orcid.org/0000-0002-0516-3250Yifan Dou, http://orcid.org/0000-0001-8482-4899Yu Jeffrey Hu, http://orcid.org/0000-0002-7991-1127D. J. Wu

To cite this article: To cite this article:

http://orcid.org/0000-0002-0516-3250Yifan Dou, http://orcid.org/0000-0001-8482-4899Yu Jeffrey Hu, http:// orcid.org/0000-0002-7991-1127D. J. Wu (2017) Selling or Leasing? Pricing Information Goods with Depreciation of Consumer Valuation. Information Systems Research

Published online in Articles in Advance 21 Jul 2017

https://doi.org/10.1287/isre.2017.0698

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/Y2VC9CFY/fulltext/images/54d2e7774947cf453fe3b82d6259f7fd11f010207b60578242f902a77b6a7705.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Selling or Leasing? Pricing Information Goods with Depreciation of Consumer Valuation

Yifan Dou,<sup>a</sup> Yu Jefrey Hu,<sup>b</sup> D. J. Wu<sup>b</sup>

<sup>a</sup> School of Management, Fudan University, 200433 Shanghai, China; <sup>b</sup> Scheller College of Business, Georgia Institute of Technology, Atlanta, Georgia 30308

Contact: yfdou@fudan.edu.cn, http://orcid.org/0000-0002-0516-3250 (YD); jefrey.hu@scheller.gatech.edu, http://orcid.org/0000-0001-8482-4899 (YJH); dj.wu@scheller.gatech.edu, http://orcid.org/0000-0002-7991-1127 (DJW)

Received: December 12, 2013 Revised: May 3, 2015; August 18, 2016 Accepted: January 11, 2017 Published Online in Articles in Advance: July 21, 2017

https://doi.org/10.1287/isre.2017.0698

Copyright: © 2017 INFORMS

Abstract. Should a monopolistic vendor adopt the selling model or the leasing model for information goods or services? We study this question in the context of consumer valuation depreciation. Using a two-period game-theoretic model, we consider two types of consumer valuation depreciation for information goods or services: vintage depreciation and individual depreciation. Vintage depreciation assumes that a good or service loses some of its appeal to consumers as it becomes dated, and this efect persists independent of usage. Individual depreciation instead assumes that valuation depreciation happens only for consumers who have consumed or experienced the good or service. We identify conditions under which each pricing model is preferred. For vintage depreciation information goods, the leasing model dominates the selling model in vendor profit. For individual depreciation information goods, the selling model dominates the leasing model as long as the magnitude of individual depreciation exceeds a certain threshold; otherwise, leasing dominates selling. We consider several model extensions such as when network efects are present. Furthermore, we show a negative interaction efect between vintage depreciation and network efects in vendor profit. By contrast, the interaction efect between individual depreciation and network efects can be either negative or positive, depending on the magnitude of individual depreciation. Managerial implications are also discussed.

History: Sanjeev Dewan, Senior Editor; Bin Gu, Associate Editor. Funding: Yifan Dou acknowledges financial support from the National Natural Science Foundation of China (NSFC) [Grants 71302002 and 71531006].

Keywords: pricing strategies • selling • leasing • vintage depreciation • individual depreciation • network efects • information goods or services

## 1. Introduction

To sell or to lease? Practitioners and academic researchers have been engaged in this debate for decades. With the rapid advancement of information technologies, especially the Internet, vendors of information goods and services are increasingly embracing the leasing model (hereafter, “leasing” for short), as exemplified by video streaming services (e.g., Netflix, Apple iTunes), online storage services (e.g., Dropbox), and software as a service (e.g., Microsoft Ofice 365). Rather than taking the perpetual ownership, under the leasing model, users rent information goods or services from the vendor and pay a periodic leasing fee. By contrast, under the selling model (hereafter, “selling” for short), users pay a lump-sum price for the perpetual use of information goods or services, such as boxed software (e.g., Microsoft Windows, Adobe, Autodesk, SAP), DVDs, hosted solutions (e.g., Rackspace), and mobile applications (e.g., paid apps in Google Play and Apple App Store). The extant literature documents that leasing is more eficient for extracting consumer surplus over time. The pioneering work by Coase (1972) suggests that selling is suboptimal for a monopolistic vendor because consumers expect price markdowns and delay their purchases. Leasing is favored over selling because it can eliminate such strategic waiting behaviors.

We reinvestigate this trade-of by incorporating another important issue over the timeline, namely, the depreciation of consumer valuation. While the extant literature has focused on the quality decay on the product side, we examine the valuation depreciation on the consumer side. Consumer valuation depreciation is ubiquitous in markets for information goods, such as books, CDs, DVDs, video games, etc. They share the common feature that their physical attributes hardly depreciate, but their consumption value to consumers diminishes as consumers become satiated (Ishihara and Ching 2012). In the market for video games, Shiller (2013) reports empirical evidence that consumers may tire quickly of playing. For the average game, highvaluation consumers reduce their valuation from \$80 in the first month of use to just a couple of dollars by the sixth month. Consumer valuation depreciation is prevalent among information goods, which are often intangible (i.e., with no physical features), and their consumption value is sensitive to consumer’s experience over time (Shapiro and Varian 1999). To our knowledge, analytical modeling research on consumer valuation depreciation is largely missing.

To fill this gap, we employ a two-period game-theoretic model to examine two types of consumer valuation depreciation: vintage depreciation and individual depreciation. Vintage depreciation assumes that a good or service loses some of its appeal to consumers as it becomes dated, and this efect persists independent of usage. For example, a dated version of Microsoft Ofice software is valued much less than a new release. By contrast, individual depreciation assumes that valuation depreciation occurs only when a consumer has already consumed (or experienced) the good or service (Hu 2005). We reexamine vintage depreciation in the context of information goods where we focus on the consumer side (Hu 2005), rather than on the product side studied in the literature of durable physical goods (e.g., Desai and Purohit 1998). We use the case of vintage depreciation as a benchmark for the case of individual depreciation, the main focus of our paper.

In an extension to our baseline model, we also include network efects, which are a unique feature of information goods (e.g., Katz and Shapiro 1985, Farrell and Saloner 1986). Many information goods, such as online games and chatting tools, are built on user networks or communities in which the user’s willingness to pay depends on peer adoptions. Following prior literature (e.g., Conner 1995), we model such network efects by using an additive utility function. This functional form allows us to capture both a standalone utility the user gains from consumption and the additional utility the user obtains by interacting with other users of the information good. For example, in video games, the standalone utility can come from singleplayer game playing and media streaming. A player can also obtain the additional utility by playing with peers over the network.

We identify optimal conditions for each pricing model. First and as a benchmark, for vintage depreciation information goods, leasing dominates selling. This finding extends the extant literature on durable physical goods with vintage depreciation, to our context of information goods. Furthermore, we extend this finding to consider network efects, which is new. Second, for individual depreciation information goods, which have largely been missing from the literature but are the main focus of this paper, we show that selling dominates leasing when the magnitude of individual depreciation exceeds a certain threshold; otherwise, leasing dominates selling. These findings are new, and they are also obtained in the presence of network efects. Furthermore, we show a negative interaction efect between vintage depreciation and network efects in vendor profit. By contrast, the interaction efect between individual depreciation and network efects can be either negative or positive, depending on the magnitude of individual depreciation. Strategic implications of the above findings for practitioners are discussed throughout this paper.

The rest of this paper is organized as follows: Section 2 reviews related literature. In Section 3, we first introduce our model assumptions, and then construct a very simple two-consumer example to illustrate the key ideas and insights of our analytical model. We then establish the baseline case of vintage depreciation in Section 4 and the case of individual depreciation in Section 5. Several model extensions, including network efects, are discussed in Section 6. Section 7 outlines the managerial implications and concludes. Proofs of the major results are included in the appendix.

## 2. Literature Review

The rich academic debate about whether to sell or lease durable goods can be traced back at least to Coase (1972). The key idea, as summarized by Bond and Samuelson (1984), is that a monopoly seller of a durable good is efectively unable to exercise its monopoly power. Once an initial stock of the good has been produced and sold, the monopolist still faces the residual demand. Exploiting the residual demand by selling some additional quantity of the good, presumably at a lower price, allows the seller to earn additional profit. Therefore, the monopoly seller’s optimal stock level will converge to the competitive stock level at which the market price is equal to the marginal production cost. Rational consumers, on the other hand, will anticipate the price markdown and accordingly value the good only at the competitive price. As a result, the monopolist can earn no more profit than that of a competitive seller—a prediction known as the Coase conjecture. Coase (1972) also suggests that leasing, rather than selling, can improve vendor profit because leasing limits the market supply to the monopoly level, which helps maintain the monopoly price.

Most analytical models in the literature related to the Coase conjecture use two main approaches. The first approach directly formalizes the stock-level decision Coase (1972) considers. In particular, the vendor of durable goods chooses the amount of available stock at the beginning of each period (Swan 1970, Bulow 1982, Bond and Samuelson 1984, Gul et al. 1986, Suslow 1986, Bhaskaran and Gilbert 2009).<sup>1</sup> In the stock-level decision models, the Coase conjecture is equivalent to the notion that the monopoly seller’s optimal stock level will converge to the competitive stock level. The (inverse) demand functions in these papers are aggregated measures of consumptions at the market level, rather than at the individual level. Because this traditional approach does not model individual consumer behaviors, it cannot diferentiate existing adopters from potential new consumers. In sum, the stock-level decision models cannot capture consumer valuation depreciation, which is the focus of this paper.

The second approach to examining the Coase conjecture models individual consumer behaviors. In this literature, the optimal prices are obtained from the distribution of consumer utilities. Such a model setting allows analysis of consumers’ choices at the individual level. In this stream of research, Stokey (1979) investigates the durable goods pricing problem in a continuous time model with a wide range of utility functions. Similar to Coase’s criticism to the selling model, Stokey (1979) finds that price discrimination over time is not optimal for the seller because of consumer waiting behaviors. Conlisk et al. (1984) revisit Stokey’s (1979) utility-based model by considering new consumer arrivals in each period. They find that the selling model may still be optimal with new consumer arrivals in each period. Unfortunately, these two studies do not analytically solve the case of leasing. Bagnoli et al. (1989) discover that selling is better than leasing when the consumer valuation is discrete. The utility-based model is also popular in the literature of marketing (e.g., Desai and Purohit 1998, Bhaskaran and Gilbert 2005), industrial organization $( \mathrm { e . g . }$ , Bensaid 1996), and information systems economics $( \mathrm { e . g . }$ , Chien and Chu 2008, Zhang and Seidmann 2010). Our work follows this stream, and in our utility-based model, we use a standard two-period setting, similar to Conlisk et al. (1984), Desai and Purohit (1998), and Bhaskaran and Gilbert (2009). We contribute to this literature stream by considering individual depreciation associated with the sale or lease of information goods, which is novel. Additionally, we also ofer new insights by extending the literature on product-side vintage depreciation (for physical durable goods such as cars, e.g., Desai and Purohit 1998) to the consumer side in the context of information goods, with and without network efects.

Our work also relates closely to the burgeoning literature on software pricing. For example, Jain and Kannan (2002) examine the server cost structure and compare pricing schemes of information goods. In an auction setting with demand uncertainty, Bhargava and Sundaresan (2004) show that a pay-as-you-go model is optimal when consumer valuation and demand realization correlate negatively. Huang and Sundararajan (2005) compare on-demand and in-house computing from a cost perspective and discuss the optimal transition path from in-house to on-demand computing. Choudhary (2007) endogenizes the software upgrading decision and shows that the subscription model is always optimal. In our paper, the leasing (selling) model is a simplified form of the subscription (perpetual licensing) pricing model in the software industry. Therefore, our results can also provide novel insights to vendors of software products that exhibit characteristics of individual depreciation.

## 3. Model Assumptions and An Illustrative Two-Consumer Example

In this section, we first introduce our model assumptions. We then construct a simple example to illustrate the impact of two types of consumer valuation depreciation: vintage depreciation and individual depreciation.

## 3.1. Model Assumptions

A monopolistic vendor ofers an information good or service with a life cycle of two periods. The vendor wishes to maximize his total profit over both periods. We assume the marginal production cost of the information good or service is zero $( \mathrm { e . g . } ,$ , Shapiro and Varian 1999). We examine and compare two representative pricing models: selling and leasing. Under selling, the vendor announces prices $p _ { i }$ at the beginning of period $i \in \{ 1 , 2 \}$ , and consumers pay $p _ { i }$ for the perpetual ownership and use of the information good. Under leasing, the vendor announces the periodic leasing fee $r _ { i }$ at the beginning of each period $i \in \{ 1 , 2 \}$ and consumers pay $r _ { i }$ for the single-period use for that particular period i. We follow the literature to assume that the vendor is unable to commit to a future price path (e.g., Coase 1972, Bulow 1982, Katz and Shapiro 1985). For simplicity, following the durable goods pricing literature (e.g., Conlisk et al. 1984), we assume that no consumer buys more than one unit, and there are no resales. There are no disposal or switching costs if period 1 adopters stop the adoption in period 2.

We assume a unit mass of heterogeneous consumers with their type v uniformly distributed on $[ - K , 1 ]$ where $K \geq 0 .$ Therefore, the density of consumer distribution is $1 / ( 1 + K )$ everywhere. Specifically, for consumers with $v \in [ 0 , 1 ]$ , their type v represents period 1 valuation of the information good, which is subject to depreciation in period 2. By contrast, consumers distributed on $[ - K , 0 )$ are “not interested” in the information good or service. Thus, their valuation is equal to 0 in both periods. In our baseline model without network efects, we need to consider only consumers with $v \in$ <sup>[</sup>0, 1<sup>]</sup>. In Section 6.1, we will extend this baseline model to incorporate network efects, under which those consumers with type $v < 0$ may become “interested” if they expect benefits generated by network efects (e.g., Conner 1995, Jing 2007).

Next we introduce the mechanisms of valuation depreciation specifically for consumers with nonnegative valuation. For vintage depreciation information goods, any consumer $v ^ { \prime } \mathbf { s }$ valuation will depreciate from v to θv in period 2. By contrast, for individual depreciation information goods, consumer v’s valuation will depreciate to θv only when she is a period 1 adopter. Otherwise, consumer v will maintain the same initial valuation in period 2 (Hu 2005). We denote $N _ { i }$ as the number of paying consumers (either under leasing or selling) in equilibrium in period i. We summarize our key notation in Table 1. For both vintage depreciation information goods and individual depreciation information goods, we compare and contrast the selling model with the leasing model.

Table 1. Summary of Key Notation

<table><tr><td> $v$ </td><td>Consumer type,  $v \sim U[-K,1]$ , we set  $K = 0$  in the case of no network effects</td></tr><tr><td> $1 - \theta$ </td><td>Magnitude of depreciation  $\theta \in [0,1]$ </td></tr><tr><td> $v_i$ </td><td>Marginal consumer type in period  $i \in \{1,2\}$ </td></tr><tr><td> $p_i$ </td><td>Selling price in period  $i \in \{1,2\}$ </td></tr><tr><td> $r_i$ </td><td>Leasing fee in period  $i \in \{1,2\}$ </td></tr><tr><td> $N_i$ </td><td>Number of paying (under either selling or leasing) consumers in equilibrium in period  $i \in \{1,2\}$ </td></tr><tr><td> $S(L)$ </td><td>Indicator of the selling (leasing) model</td></tr><tr><td> $A(B)$ </td><td>Indicator of vintage depreciation (individual depreciation) information goods</td></tr><tr><td> $s$ </td><td>Strength of network effects,  $s \in [0,1]$ </td></tr><tr><td> $\pi(\tilde{\pi})$ </td><td>The vendor&#x27;s overall profit without (with) network effects</td></tr><tr><td> $\pi_2(\tilde{\pi}_2)$ </td><td>The vendor&#x27;s single-period profit in period 2 without (with) network effects</td></tr><tr><td> $U(\tilde{U})$ </td><td>Consumer utility without (with) network effects</td></tr><tr><td> $\Omega$ </td><td>Consumer&#x27;s adoption status over two periods, $\Omega \in \{DD,OD,DO,OO\}$ , where  $D$  stands for “adopting” and  $O$  for “not adopting”</td></tr></table>

## 3.2. An Illustrative Two-Consumer Example

Consider a market with two consumers, denoted by $V _ { 1 }$ and $V _ { 2 } ,$ with initial single-period valuations of 10 and 4 at the beginning of period 1, respectively. The information good has a two-period life cycle. In period 2, consumer valuation will drop by 75% (i.e., θ <sup></sup> 0.25) when depreciation applies.

In the scenario of vintage depreciation, both consumers’ valuations are subject to depreciation in period $^ { 2 , }$ unconditionally. Thus, consumers’ period 2 valuations are $1 0 \times 0 . 2 5 = 2 . 5$ and $4 \times 0 . 2 5 = 1$ , respectively.

Under selling and vintage depreciation, if consumer $V _ { 1 }$ purchases in period 1, then only consumer $V _ { 2 }$ is left in period 2 and the optimal period 2 selling price is 1. While consumer $V _ { 1 }$ has an overall valuation of $1 0 + 2 . 5 = 1 2 . 5$ over two periods, the vendor is unable to charge a price at 12.5. Why? Because consumer $V _ { 1 }$ would delay her adoption to period 2 when the selling price is 1 to enjoy a greater surplus of $2 . 5 - 1 = 1 . 5 ,$ rather than purchasing in period 1 with a zero surplus $( 1 2 . 5 - \overset { \cdot } { 1 } 2 . 5 = 0 )$ . Thus, the incentive compatibility constraint leads to the optimal period 1 price at $1 \dot { 2 } . 5 - 1 . 5 = 1 1$ . The total profit for a selling vendor is then $1 1 + 1 = 1 2$

Under leasing and vintage depreciation, in period $^ { 2 , }$ the optimal leasing fee is 2.5, and period 2 profit is 2.5 because only consumer $V _ { 1 }$ rents. In period 1, the optimal leasing fee is 10, and again only consumer $V _ { 1 }$ rents. The total profit for a leasing vendor is $1 0 + 2 . 5 = 1 2 . 5$ Thus, under vintage depreciation, leasing dominates selling in vendor profit $( \hat { 1 } 2 . 5 > 1 2 )$

In the scenario of individual depreciation, only the valuation of the period 1 adopter depreciates. For example, if we assume that only consumer $V _ { 1 }$ adopts in period 1, then her valuation drops to $1 0 \times 0 . 2 5 = 2 . 5$ in period 2, while consumer $V _ { 2 }$ maintains the period 1 valuation of 4. Intuitively, one would expect that the vendor’s profit should be at least equal to that under vintage depreciation because depreciation occurs only for existing adopters, rather than for all consumers. However, we show that the vendor becomes worse of in this scenario.

Under selling and individual depreciation, if consumer $V _ { 1 }$ adopts in period 1, then only consumer $V _ { 2 }$ is left at the beginning of period 2. The optimal selling price in period 2 is 4. Therefore, the optimal selling price in period 1 is 6.5 after considering the incentive compatibility constraint. Otherwise, consumer $V _ { 1 }$ would delay her adoption until period 2 for a greater surplus. The total profit for a selling vendor is $6 . 5 + 4 = 1 0 . { \overset { \cdot } { 5 } }$

Under leasing and individual depreciation, in period 2, if we assume that only consumer $V _ { 1 }$ adopts in period 1, then her valuation drops to 2.5 in period $^ { 2 , }$ while consumer $V _ { 2 }$ maintains the valuation of 4. Can the vendor increase the period 2 leasing fee to 4? Unfortunately not, because consumer $V _ { 1 }$ would then delay her adoption to period 2 and receive a surplus of $1 0 - 4 = 6 ,$ instead of adopting early in period 1 (in which case her surplus would be $0 < 6 )$ . As a result, the optimal period 2 leasing fee is 10. No consumers rent in period 1, and only consumer $V _ { 1 }$ rents in period 2. The total profit for a leasing vendor is 10. Thus, under individual depreciation, leasing can generate less profit than selling $( \mathrm { i } . \mathrm { e } . , 1 0 < 1 0 . 5 )$

Table 2 summarizes vendor profit under our $2 \times 2$ design between depreciation types and pricing models. Our simple two-consumer example illustrates the following key insights of our paper: Benchmarked with vintage depreciation, in the presence of individual depreciation, consumers have incentives to wait, both under selling and under leasing. This, in turn, hurts vendor profit. Surprisingly, selling can mitigate such customer waiting behaviors better than leasing can, particularly when the magnitude of individual depreciation is large. We formalize these insights in our analytical models below.

Table 2. Summary of Profits in Two-Consumer Example

<table><tr><td></td><td>Selling</td><td>Leasing</td></tr><tr><td>Vintage depreciation</td><td>12</td><td>12.5</td></tr><tr><td>Individual depreciation</td><td>10.5</td><td>10</td></tr></table>

## 4. Vintage Depreciation

As a benchmark, we start our analysis by studying vintage depreciation information goods, where all consumers, including those who do not adopt in period 1, depreciate their valuation in period 2. As a result, in period 2, consumer valuation is uniformly distributed on $[ 0 , \theta ]$ (with a greater density). The update to the distribution of consumer valuation, exemplified with $\theta = 0 . 5 ,$ , is illustrated in Figure 1.

## 4.1. The Selling Model

Under selling, the vendor announces prices $p _ { i }$ at the beginning of period $i \in \{ 1 , 2 \}$ . Denote the marginal consumer type in period i by $v _ { i } \ ( i \in \{ 1 , 2 \} )$ ). Consumers with the marginal type are indiferent between adopting and not adopting in each period. We solve the vendor’s problem using backward induction.

At the beginning of period $^ { 2 , }$ the vendor needs to consider only potential consumers with type distributed on $[ 0 , \dot { v _ { 1 } } ] .$ , because period 1 adopters have purchased the information good with perpetual license. For any consumer $v \in [ 0 , \bar { v } _ { 1 } ] ,$ , period 2 valuation depreciates to θv. She will become a period 2 adopter if $p _ { 2 }$ satisfies $\theta v \geq p _ { 2 }$ . The population of paying consumers in period 2 is given by $\mathbf { \bar { \Phi } } _ { } - \mathbf { \Phi } _ { 2 } ,$ , in which $v _ { 2 }$ can be determined by solving $\theta v _ { 2 } - p _ { 2 } = 0$ . The vendor’s period 2 problem is

$$
\max _ {v _ {2} \in [ 0, v _ {1} ]} \pi_ {2} ^ {S, A} (v _ {2} \mid v _ {1}) = (v _ {1} - v _ {2}) \theta v _ {2},
$$

where the superscripts S and A stand for selling and vintage depreciation information goods, respectively.

Figure 1. The Distribution Density Function of Consumers Single-Period Valuation $( \theta = 0 . 5 , \dot { K } = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/6caeece2f517afddee67ac54f737454a35a20d75946401c02b85b992fae591bc.jpg)

Solving, we have $v _ { 2 } ^ { * } = v _ { 1 } / 2 , p _ { 2 } ^ { * } = \theta v _ { 1 } / 2$ , and the vendor’s optimal period 2 profit is $( \pi _ { 2 } ^ { S , A } ) ^ { * } = \theta v _ { 1 } ^ { 2 } / 4$

Next, we move to period 1. A type v consumer’s utility function is denoted by $U _ { v } ( \Omega )$ , where $\Omega \in \{ D D , O D$ $\dot { D O } , O O \}$ stands for consumer v’s adoption status in each period (D for “adopting” and O for “not adopt-$\mathrm { i n g ^ { \prime \prime } } )$ . In period 1, all consumers have three options: buying in period 1 (i.e., adopting in both periods, denoted by $\Omega = D D ) ,$ , delaying adoption to period 2 $( \mathrm { i . e . , ~ } \Omega = { \mathrm { { \bar { O } } } } D )$ , or never adopting $( \mathrm { i . e . , ~ } \bar { \Omega ^ { \mathrm { ~ } } } = O O )$ The corresponding utility function $U _ { v } ( \Omega )$ is given in Equation (1)

$$
\begin{array}{r l} & U _ {v} ^ {S, A} (D D) = (1 + \theta) v - p _ {1}; \\ & U _ {v} ^ {S, A} (O D) = \theta v - p _ {2}; \\ & U _ {v} ^ {S, A} (O O) = 0. \end{array}\tag{1}
$$

Following the literature (e.g., Fudenberg and Tirole 1991), we assume that at the beginning of period 1, consumers can correctly expect the vendor’s period 2 optimal pricing strategy in rational expectations equilibrium (REE). Marginal consumers (with type $v _ { 1 } )$ are indiferent between adopting in period 1 and delaying adoption until period 2. Therefore, $v _ { 1 }$ can be obtained by solving $U _ { v _ { 1 } } ^ { S , A } ( D D ) = U _ { v _ { 1 } } ^ { S , A } ( O D )$ , which yields, $p _ { 1 } =$ $( \dot { 1 } + \theta / 2 ) \dot { v _ { 1 } }$ . The number of period 1 paying consumers is $N _ { 1 } = 1 - v _ { 1 }$ . The vendor’s period 1 problem is

$$
\begin{array}{r l} \max _ {v _ {1} \in [ 0, 1 ]} & \pi^ {S, A} (v _ {1}) = p _ {1} N _ {1} + (\pi_ {2} ^ {S, A}) ^ {*} (v _ {1}) \\ \text {s.t.} & p _ {1} = (1 + \theta / 2) v _ {1}, \\ & N _ {1} = 1 - v _ {1}. \end{array}
$$

Solving, we have

$$
p _ {1} ^ {*} = \frac {(2 + \theta) ^ {2}}{2 (4 + \theta)}, \quad p _ {2} ^ {*} = \frac {\theta (2 + \theta)}{2 (4 + \theta)}, \quad (\pi^ {S, A}) ^ {*} = \frac {(2 + \theta) ^ {2}}{4 (4 + \theta)}.\tag{2}
$$

The numbers of paying consumers are

$$
N _ {1} ^ {*} = \frac {2}{4 + \theta}, N _ {2} ^ {*} = \frac {2 + \theta}{2 (4 + \theta)}.\tag{3}
$$

We depict consumer adoptions under the optimal selling strategy in Figure 2. Consumers who “buy in period $1 ^ { \prime \prime }$ have a higher valuation than those who “buy in period $2 , \prime \prime$ because the total benefit of buying in period 1 is $( 1 + \theta ) v$ , which is always greater than the benefit of buying in period 2, θv. In period 2, a rational vendor lowers the price $( p _ { 2 } ^ { * } < p _ { 1 } ^ { * } )$ to induce more purchases. Expecting this future price markdown, a group of consumers (denoted by region W) choose to delay their adoptions until period 2 even if they can aford $p _ { 1 }$ $( \mathrm { i . e . , ~ } ( 1 + \mathsf { \bar { \theta } } ) v \ge p _ { 1 } )$ . The vendor, in turn, has to lower the period 1 price $( \mathbf { i . e . } , p _ { 1 } ^ { * } < ( 1 + \theta ) v _ { 1 } )$ to alleviate such waiting behavior. If consumers do not wait, i.e., they adopt in period 1 as long as $U ^ { S , A } ( D D ) \geq 0 .$ , then the vendor’s optimal profit is $( 1 + \theta ) ^ { 2 } / ( 4 + 3 \theta )$ . We denote the profit loss due to such consumer waiting behaviors by $\underline { { \dot { L } o s s } } ^ { S , A }$ . Then, we have

Figure 2. Consumers’ Valuation and Adoptions Under Selling and Vintage Depreciation $( \theta = 0 . 5 , K = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/90022a2eab9908612771f8458786cef32f5af85b0bef02eb1d4a3f956f1bef5c.jpg)

$$
\begin{array}{c} L o s s ^ {S, A} = \frac {(1 + \theta) ^ {2}}{4 + 3 \theta} - (\pi^ {S, A}) ^ {*} = \frac {(1 + \theta) ^ {2}}{4 + 3 \theta} - \frac {(2 + \theta) ^ {2}}{4 (4 + \theta)} \\ = \frac {\theta [ 8 + \theta (8 + \theta) ]}{4 (4 + \theta) (4 + 3 \theta)}. \end{array}
$$

## 4.2. The Leasing Model

Under leasing, the vendor announces the leasing fee $r _ { i }$ at the beginning of each period $i \in \{ 1 , 2 \}$ . All consumers, including existing adopters in period 1, must pay the leasing fee in period 2 if they opt to use the information good. Again we solve the vendor’s problem using backward induction.

Consider period 2 first. Unlike a selling vendor, a leasing vendor needs to take all consumers into consideration. The number of paying consumers in period 2 is $N _ { 2 } = 1 - v _ { 2 } ,$ where $v _ { 2 }$ satisfies $\theta v _ { 2 } - r _ { 2 } = 0$ . The vendor’s period 2 profit is $\pi _ { 2 } ^ { L , A } ( v _ { 2 } ) = N _ { 2 } \times r _ { 2 } = ( 1 - v _ { 2 } ) \theta v _ { 2 } ,$ The superscript L represents the leasing model. Solving, we have $\begin{array} { r } { \bar { v _ { 2 } ^ { * } } = \frac { 1 } { 2 } , \bar { r _ { 2 } ^ { * } } = \theta / 2 } \end{array}$ , and $( \pi _ { 2 } ^ { L , A } ) ^ { * } = \theta / 4$

At the beginning of period 1, under leasing consumers have the freedom to rent only in period 1. Therefore, there are four candidate strategies

$$
\begin{array}{r l} & U _ {v} ^ {L, A} (D D) = (1 + \theta) v - r _ {1} - r _ {2}; \\ & U _ {v} ^ {L, A} (D O) = v - r _ {1}; \\ & U _ {v} ^ {L, A} (O D) = \theta v - r _ {2}; \\ & U _ {v} ^ {L, A} (O O) = 0. \end{array}
$$

In REE, the marginal consumer type $v _ { 1 }$ satisfies either $U _ { v _ { 1 } } ^ { \dot { L } , A } ( D D ) = \bigcup _ { v _ { 1 } } ^ { L , A } ( O D )$ (when there are new adopters in period 2) or $U _ { v _ { 1 } } ^ { L , A } ( D O ) = 0$ (when some consumers only rent in period 1), both resulting $r _ { 1 } = v _ { 1 }$ after simplification. Thus, the vendor’s problem becomes

Figure 3. Consumers’ Valuation and Adoptions Under Leasing and Vintage Depreciation $( \theta = 0 . { \overset { \circ } { 5 } } , K = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/a94d11564aeb5d1468afcc0ac3847059f5be87d805fb0bfe9a99a0c04acbba38.jpg)

$$
\begin{array}{l} \max _ {v _ {1} \in [ 0, 1 ]} \pi^ {L, A} (v _ {1}) = r _ {1} N _ {1} + (\pi_ {2} ^ {L, A}) ^ {*} (v _ {1}) \\ \text {s.t.} r _ {1} = v _ {1}, \\ N _ {1} = 1 - v _ {1}. \end{array}
$$

The optimal solution is $\begin{array} { r } { v _ { 1 } ^ { * } = \frac { 1 } { 2 } } \end{array}$ , which gives $\begin{array} { r } { r _ { 1 } ^ { * } = \frac { 1 } { 2 } } \end{array}$ and $( \pi ^ { L , A } ) ^ { * } \dot { = } ( 1 + \theta ) / 4$ . The numbers of paying consumers in each period are $\begin{array} { r } { N _ { 1 } ^ { * } = N _ { 2 } ^ { * } = \frac { 1 } { 2 } } \end{array}$ . Figure 3 illustrates consumers’ valuation and adoption under leasing and vintage depreciation.

In each period, the marginal consumers’ adoption decisions depend on only single-period valuation and the leasing fee $( { \mathrm { i . e . , } } v _ { 1 } = r _ { 1 } , \theta v _ { 2 } = r _ { 2 } )$ ; that is, consumers do not wait under leasing because they do not take the future price into consideration, i.e., $\check { L } o s s ^ { L , A } = 0 .$ . Thus, leasing efectively eliminates consumer waiting behavior. Comparing the vendor’s profit under leasing and selling, we have

$$
(\pi^ {L, A}) ^ {*} - (\pi^ {S, A}) ^ {*} = \frac {1 + \theta}{4} - \frac {(2 + \theta) ^ {2}}{4 (4 + \theta)} = \frac {\theta}{4 (4 + \theta)} \geq 0,
$$

which leads to the following proposition.

Proposition 1. For vintage depreciation information goods, leasing dominates selling in vendor profit.

Note that

$$
\frac {L o s s ^ {S , A}}{(\pi^ {L , A}) ^ {*} - (\pi^ {S , A}) ^ {*}} = \frac {8 + \theta (8 + \theta)}{4 + 3 \theta} \geq 1, \quad f o r \theta \in [ 0, 1 ],
$$

which implies that selling would dominate leasing if consumers did not wait. Proposition 1 formalizes the idea in Coase (1972) that leasing can efectively eliminate consumer waiting behaviors, but extends it to the context of vintage depreciation information goods.

Interestingly, compared to leasing, selling ofers higher social welfare. This can be shown by computing the area below the valuation curves in Figures 2 and 3 among those adopting consumers. We have the following proposition.

Proposition 2. For vintage depreciation information goods, selling dominates leasing in social welfare.

Intuitively, selling covers a larger market than leasing, leading to a higher social welfare. However, leasing dominates selling in vendor profit by focusing on consumers with higher valuations. Taken together, these findings extend the extant literature of vintage depreciation durable goods to the new context of durable information goods. In particular, we focus on the consumer valuation depreciation, rather than on the product side $( \mathrm { e . g . } ,$ quality decay or physical wear and tear over time; see Desai and Purohit 1998) as in the prior literature.

Proposition 1 provides a useful benchmark for the case of individual depreciation of information goods, which is our key focus. It is a new type of consumer valuation depreciation in practice, yet it has not been formally treated in the academic literature. We analyze this case in Section 5.

## 5. Individual Depreciation

For an individual depreciation information good, in period 2, only period 1 adopters depreciate their valuations. As a comparison to Figure 1, we depict the density function of consumer valuation distribution in period 2 in Figure 4. In sharp contrast with Figure 1, the consumer type distribution is no longer uniform in period 2. Specifically, consumers with type $v \in$ $[ v _ { 1 } , 1 ]$ (i.e., period 1 adopters) depreciate their valuation, while consumers with type $\bar { v ^ { } \in [ 0 , v _ { 1 } ) }$ do not. This leads to two cases: (a) $v _ { 1 } < \theta$ (see Figure 4(a)), and (b) $v _ { 1 } \geq \theta$ (see Figure 4(b)). Under case (a), the distribution of period 2 valuation is further segmented into three intervals: (a.1) the interval $[ 0 , \theta v _ { 1 } ) ]$ , which consists of only period 1 nonadopters with a density of 1; (a.2) the interval $[ \theta v _ { 1 } , v _ { 1 } )$ , which consists of both period 1 adopters and nonadopters, with a density of $ { \bar { 1 } } + 1 / \theta ;$ and (a.3) the interval $[ v _ { 1 } , \theta ]$ , which consists of only period 1 adopters with a density of $1 / \theta .$ . Similarly, in case (b), the distribution of period 2 valuation is segmented into three intervals: (b.1) intervals $[ 0 , \theta v _ { 1 } )$ and $[ \theta , v _ { 1 } ]$ , which consist of only period 1 nonadopters with a density of 1, and (b.2) the interval $[ \theta v _ { 1 } , \theta )$ , which consists of both period 1 adopters and nonadopters with a density of $1 + 1 / \theta$

Note that, although θ is exogenous, $v _ { 1 }$ is determined by the vendor’s pricing strategy, which implies that the distribution density of consumers’ period 2 valuation can be manipulated by the vendor’s period 1 pricing strategy. This insight connects our work with the literature on endogenous demand functions $( \mathrm { e . g . }$ Johnson and Myatt 2003, 2006; Bhargava and Chen 2012). For individual depreciation information goods, upon observing θ, the vendor can strategically manipulate consumer valuation toward a certain distribution in period 2. For example, if the vendor charges a smaller period 1 leasing fee to induce more adoptions in period 1 (which leads to a smaller $v _ { 1 } ) .$ , then period 2 distribution converges to a pattern, as illustrated in

Figure 4. The Distribution Density Functions of Consumers’ Single-Period Valuation $( \theta = 0 . 5 , K = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/232ee342b68f71196996d9ea751f8bf5765a10de760c849f9819f1f4a4e40d20.jpg)

![](/api/attachments/Y2VC9CFY/fulltext/images/83db79b53ba458f132a7c067882cc34c5c95174740576fce97c759924781fbee.jpg)

Figure 4(a), where consumers are segmented into three intervals with diferent densities. If in period 1 the vendor maintains a relatively small number of adopters by charging a higher period 1 leasing fee, then the period 2 distribution converges to a pattern as illustrated in Figure 4(b), with a single bump in the center.

## 5.1. The Selling Model

Under selling, we denote the selling prices as $p _ { i }$ $( i \in \{ 1 , 2 \} )$ for period i and solve the vendor’s problem using backward induction. At the beginning of period $^ { 2 , }$ the selling vendor needs to consider consumers only in the interval $[ 0 , v _ { 1 } ]$ . The number of paying consumers in period 2 is $N _ { 2 } = v _ { 1 } - v _ { 2 } ,$ where $v _ { 2 }$ satisfies $v _ { 2 } - p _ { 2 } = 0$ . Note that $v _ { 2 }$ is not afected by individual depreciation, because new adopters in period 2 have not adopted in period 1. The vendor’s period 2 problem is

$$
\max _ {v _ {2} \in [ 0, v _ {1} ]} \pi_ {2} ^ {S, B} (v _ {2} \mid v _ {1}) = (v _ {1} - v _ {2}) \times v _ {2},
$$

where the superscript B represents the case of individual depreciation information goods. Solving, we have $v _ { 2 } ^ { * } = v _ { 1 } / 2 , p _ { 2 } ^ { * } = v _ { 1 } / 2$ , and $( \pi _ { 2 } ^ { S , B } ) ^ { * } = v _ { 1 } ^ { 2 } / 4$ . At the beginning of period $^ { 1 , }$ consumer v faces three options with the following utility function:

$$
\begin{array}{l} U _ {v} ^ {S, B} (D D) = (1 + \theta) v - p _ {1}; \\ U _ {v} ^ {S, B} (O D) = v - p _ {2}; \\ U _ {v} ^ {S, B} (O O) = 0. \end{array}
$$

Note that existing adopters need not pay $p _ { 2 }$ for their period 2 adoptions. The marginal consumer type $v _ { 1 }$ can be obtained by solving $U _ { v _ { 1 } } ^ { S , B } ( D D ) = U _ { v _ { 1 } } ^ { S , B } ( O \bar { D } )$ , which yields $v _ { 1 } = ( p _ { 1 } - p _ { 2 } ^ { * } ) / \theta$ or, equivalently, $p _ { 1 } = \theta v _ { 1 } + p _ { 2 } ^ { * } =$ $( \theta + { \textstyle \frac { 1 } { 2 } } ) v _ { 1 }$ . The number of period 1 paying consumers is $N _ { 1 } = \overline { { 1 } } - v _ { 1 }$ . Therefore, the vendor’s problem is

$$
\begin{array}{r l} \max _ {v _ {1} \in [ 0, 1 ]} & \pi^ {S, B} (v _ {1}) = p _ {1} N _ {1} + (\pi_ {2} ^ {S, B}) ^ {*} (v _ {1}) \\ \text {s.t.} & p _ {1} = (\theta + 1 / 2) v _ {1}, \\ & N _ {1} = 1 - v _ {1}. \end{array}
$$

Solving the vendor’s problem, we obtain the following lemma.

Lemma 1. For individual depreciation information goods and under the selling model, the optimal pricing strategies $( p _ { 1 } ^ { * } , p _ { 2 } ^ { * } )$ are

$$
p _ {1} ^ {*} = \frac {(1 + 2 \theta) ^ {2}}{2 (1 + 4 \theta)}, \quad p _ {2} ^ {*} = \frac {1 + 2 \theta}{2 (1 + 4 \theta)}.
$$

The optimal profit is

$$
(\pi^ {S, B}) ^ {*} = \frac {(1 + 2 \theta) ^ {2}}{4 (1 + 4 \theta)}.
$$

The numbers of paying consumers in each period are

$$
N _ {1} ^ {*} = \frac {2 \theta}{(1 + 4 \theta)}, N _ {2} ^ {*} = \frac {1 + 2 \theta}{2 (1 + 4 \theta)}.
$$

Figure 5. Consumers’ Valuation and Adoptions Under Selling and Individual Depreciation $( \theta = \bar { 0 } . 5 , K = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/849b83b4ec1801e3f1ecbe72d4d13184be7c1370be9d5fcee2e8625fb28062b7.jpg)  
We illustrate consumer valuation and adoptions in Figure 5. The parameter setting is the same as in Figure 2. Note that there exists a fraction of strategic consumers (denoted by W) who will delay adoption to period 2. It can be shown that the selling profit without consumer waiting is $( 1 + \theta ) ^ { 2 } / ( 3 + 4 \breve { \theta } ) \breve $ (i.e., assuming consumer v adopts in period 1 as long as $U _ { v } ^ { S , B } ( D D ) > 0 )$ , thus the vendor’s profit loss due to consumer waiting is ${ \cal L } o s s ^ { S , B } = ( 1 + \hat { \theta ) ^ { 2 } } / ( 3 + 4 \theta ) - ( \pi ^ { S , B } ) ^ { * } =$ $( 1 + 8 \theta + 8 { \theta } ^ { 2 } ) / ( 4 ( 3 + 1 6 \theta + 1 6 { \theta } ^ { 2 } ) )$ <sup>)</sup>. Note that this loss is even greater than that under vintage depreciation, because $L o s s ^ { S , B } \ge L o s s ^ { S , A }$ for all $\theta \in [ \breve { 0 } , 1 ]$ . Thus, consumers have stronger incentives to wait until period 2 in the case of individual depreciation than in the case of vintage depreciation.

## 5.2. The Leasing Model

Finally, we examine the leasing model under individual depreciation. The vendor announces a singleperiod leasing fee $r _ { i }$ at the beginning of each period $\hat { i } = \{ 1 , 2 \}$ <sup>}</sup>. We use $v _ { i }$ to denote the marginal consumer type in period i $( i \in \{ 1 , 2 \} )$ . As illustrated in Figure $^ { 4 , }$ there are two cases to consider here: (a) $v _ { 1 } < \theta$ and (b) $v _ { 1 } \geq \theta$ . The distribution of consumer valuation in period 2 is no longer a single uniform continuum, but features intervals of diferent densities (see Figure 4). Consequently, the vendor’s period 2 problem becomes nontrivial, because the marginal consumer type $v _ { 2 }$ can be located in any interval, as illustrated in Figure 4.

For case (a) in Figure 4, the number of period 2 paying consumers $N _ { 2 }$ depends on the location of marginal consumer type $v _ { 2 }$

$$
N _ {2} (r _ {2} \mid v _ {1} <   \theta) = \left\{ \begin{array}{l l} 1 - r _ {2}, & r _ {2} \in [ 0, \theta v _ {1}); \\ v _ {1} - r _ {2} + 1 - r _ {2} / \theta , & r _ {2} \in [ \theta v _ {1}, v _ {1}); \\ 1 - r _ {2} / \theta , & r _ {2} \in [ v _ {1}, \theta ]. \end{array} \right.\tag{4}
$$

Similarly, for case (b) in Figure $4 , N _ { 2 }$ is given as

$$
N _ {2} (r _ {2} \mid v _ {1} \geq \theta) = \left\{ \begin{array}{l l} 1 - r _ {2}, & r _ {2} \in [ 0, \theta v _ {1}); \\ v _ {1} - r _ {2} + 1 - r _ {2} / \theta , & r _ {2} \in [ \theta v _ {1}, \theta); \\ v _ {1} - r _ {2}, & r _ {2} \in [ \theta , v _ {1} ]. \end{array} \right.\tag{5}
$$

The vendor’s period 2 problem is

$$
\begin{array}{l} \max _ {v _ {2} \in [ 0, 1 ]} \pi_ {2} ^ {L, B} (v _ {2} \mid v _ {1}) = r _ {2} N _ {2} (r _ {2} \mid v _ {1}) \\ \text {s.t.} r _ {2} = \left\{ \begin{array}{l l} \theta v _ {2}, & v _ {2} \geq v _ {1}; \\ v _ {2}, & v _ {2} <   v _ {1}. \end{array} \right. \end{array}
$$

At the beginning of period 1, the type v consumer’s utility function is

$$
\begin{array}{l} U _ {v} ^ {L, B} (D D) = (1 + \theta) v - r _ {1} - r _ {2}; \\ U _ {v} ^ {L, B} (D O) = v - r _ {1}; \\ U _ {v} ^ {L, B} (O D) = v - r _ {2}; \\ U _ {v} ^ {L, B} (O O) = 0. \end{array}
$$

The vendor’s period 1 problem is

$$
\begin{array}{l} \underset {v _ {1} \in [ 0, 1 ]} {\max} \pi^ {L, B} (v _ {1}) = r _ {1} N _ {1} + (\pi_ {2} ^ {L, B}) ^ {*} (v _ {1}) \\ \text {s.t.} r _ {1} = \left\{ \begin{array}{l l} \theta v _ {1}, & v _ {1} \geq v _ {2} ^ {*}; \\ v _ {1}, & v _ {1} <   v _ {2} ^ {*}; \end{array} \right. \\ N _ {1} = 1 - v _ {1}. \end{array}
$$

Solving, we have the following lemma.

Lemma 2. For individual depreciation information goods and under the leasing model, the optimal leasing fees $( r _ { 1 } ^ { * } , r _ { 2 } ^ { * } )$ are

$$
(r _ {1} ^ {*}, r _ {2} ^ {*}) = \left\{ \begin{array}{l l} (1 / 2 + \epsilon , 1 / 2), & \theta \in [ 0, 1 / 3); \\ (\theta / (1 + \theta), \theta / (1 + \theta)), & \theta \in [ 1 / 3, 1 ]. \end{array} \right.\tag{6}
$$

The optimal profit $( \pi ^ { L , B } ) ^ { * }$ is

$$
(\pi^ {L, B}) ^ {*} = \left\{ \begin{array}{l l} 1 / 4, & \theta \in [ 0, 1 / 3); \\ \theta / (1 + \theta), & \theta \in [ 1 / 3, 1 ]. \end{array} \right.\tag{7}
$$

The numbers of paying consumers in each period $( N _ { 1 } ^ { * } , N _ { 2 } ^ { * } )$ are

$$
(N _ {1} ^ {*}, N _ {2} ^ {*}) = \left\{ \begin{array}{l l} (0, 1 / 2), & \theta \in [ 0, 1 / 3); \\ (\theta / (1 + \theta), 1 / (1 + \theta)), & \theta \in [ 1 / 3, 1 ]. \end{array} \right.\tag{8}
$$

Lemma 2 states that when individuals heavily depreciate the valuation, i.e., when $\theta < { \frac { 1 } { 3 } } ,$ , in REE, consumers opt to wait until period 2 even if they can aford the leasing fee in period 1. For example, suppose $\begin{array} { r } { \epsilon = \frac { 1 } { 4 } } \end{array}$ Then consumers with type $v \in [ \textstyle { \frac { 3 } { 4 } } , 1 ]$ will still choose to delay adoption even if they can aford the period 1 leasing fee. Otherwise when $\begin{array} { r } { \mathbf { \dot { \theta } } \geq \frac { 1 } { 3 } , } \end{array}$ , it is optimal to charge the same rental fee at each period $( \bar { r _ { 1 } ^ { * } } = r _ { 2 } ^ { * } )$ . Proposition 3 follows immediately from Lemmas 1 and 2.

Figure 6. Consumers’ Valuation and Adoptions Under Leasing and Individual Depreciation $( \theta = \stackrel { \cdot } { 0 . 5 } , K = 0 )$  
![](/api/attachments/Y2VC9CFY/fulltext/images/f71572c2c9b77e94176eb165f242e4fbc82461cda1c6909aa47bb65ee6292ae3.jpg)  
Proposition 3. For individual depreciation information goods, selling dominates leasing in vendor profit when $\theta \in$ $[ 0 , { \frac { 1 } { 2 } } ) ;$ ; otherwise, when $\theta \in \left[ { \textstyle { \frac { 1 } { 2 } } , \bar { 1 } } \right]$ , leasing dominates selling.

The insight from Proposition 3 is that, for information goods with individual depreciation, selling dominates leasing when the magnitude $( \mathrm { i . e . , } 1 - \theta )$ of individual depreciation is large. The driving factor behind this is also consumer waiting behaviors. In REE, we show that consumers might as well choose to wait under leasing (see region W in Figure 6). If consumers adopt as long as $U _ { v } ^ { L , \mathcal { B } } ( D O ) \geq 0 ,$ then the leasing vendor’s optimal profit is <sup>1</sup> for $\theta \in [ 0 , \frac { 1 } { 6 } ) , 1 - 3 / ( 4 + \bar { 3 \theta } )$ <sup>)</sup> for $\theta \in [ \textstyle { \frac { 1 } { 6 } } , \textstyle { \frac { 1 } { 3 } } ) .$ , and $( 1 + \theta ) ^ { 2 } \big / ( 4 ( 1 + \theta ^ { 2 } ) )$ for $\theta \in \left[ { \textstyle { \frac { 1 } { 3 } } } , 1 \right]$ . Thus, we can show that the leasing vendor’s profit loss due to such consumer waiting behavior, $L o s s ^ { { \hat { L } } , B }$ , satisfies that

$$
\frac {L o s s ^ {L , B}}{L o s s ^ {S , B}} \geq 1, \quad \mathrm{for} \theta \in [ \underline {{\theta}}, 1 / 2 ],\tag{9}
$$

where θ is the unique root to the equation $2 \theta [ \theta ( 1 1 +$ $1 5 \underline { { \theta } } ) - 1 ] = 1$ in the interval $\begin{array} { r } { \big [ \frac { 1 } { 6 } , \frac { 1 } { 3 } \big ) \ ( \underline { { \theta } } ^ { * } \approx 0 . 2 3 ) } \end{array}$ . Equation <sup>¯ ¯</sup>(9) implies that the loss due to consumer waiting under leasing is larger than that under selling when individual depreciation is large. In this case, selling is favored over leasing because selling can better mitigate consumer waiting behaviors.

Interestingly, as we show in Proposition $^ { 4 , }$ selling also provides higher social welfare than leasing in the context of individual depreciation information goods.

Proposition 4. For individual depreciation information goods, selling dominates leasing in social welfare.

We next consider several model extensions and compare them with our baseline model.

## 6. Extensions

We extend our baseline model along three dimensions: Section 6.1 incorporates network efects; Section 6.2 considers conditional pricing whereby the vendor commits to having a discount in period 2 for period 1 adopters; and Section 6.3 discusses the hybrid pricing model in our two-period setting when the vendor is able to ofer both selling and leasing simultaneously.

## 6.1. Network Efects

Network efects are ubiquitous in markets for information goods (e.g., Katz and Shapiro 1986, 1992; Shapiro and Varian 1999). A natural extension of our baseline model, therefore, is to examine optimal selling and leasing strategies under network efects. For example, consumers of video games can either play the singleplayer game alone or join a game with friends on the player network. This also applies to many information goods that share the feature of online communities, where adopters may benefit from collaborative adoptions with peers. Examples include cloud storage services (e.g., Dropbox) and product discussion forums (e.g., Microsoft Community).

Following the literature on network efects, we consider a group of potential consumers with their type v distributed on $v \in [ - K , 0 )$ , where K is large enough that the vendor can never fully cover the entire market. We denote the utility functions with network efects by U<sup>˜</sup> . In the presence of network efects, it may become possible that $\tilde { U } _ { v } > 0$ , even when $v < 0 ,$ , in which case the consumer’s adoption is driven solely by peer adoptions. This setup is standard in the literature (e.g., Katz and Shapiro 1985, Conner 1995, Jing 2007). For vintage depreciation information goods studied in Section 4.1, we rewrite Equation (1) as

$$
\begin{array}{r l} & {\tilde {U} _ {v} ^ {S, A} (D D) = v + s N _ {1} + \theta [ v + s (N _ {1} + N _ {2}) ] ^ {+} - p _ {1},} \\ & {\tilde {U} _ {v} ^ {S, A} (O D) = \theta [ v + s (N _ {1} + N _ {2}) ] ^ {+} - p _ {2},} \\ & {\tilde {U} _ {v} ^ {S, A} (O O) = 0,} \end{array}\tag{10}
$$

where s denotes the strength of network efects, and $[ v + s ( N _ { 1 } + N _ { 2 } ) ] ^ { + } = \mathrm { m a x } \{ v + \stackrel { \smile } { s } ( N _ { 1 } + N _ { 2 } ) , 0 \}$ . The interpretation of this formulation is that depreciation occurs only when consumers have nonnegative utility. The utility function in Equation (10) generalizes that in Equation (1), as it is straightforward to see that they are identical when $s = 0$ . We assume $s \in [ 0 , 1 ]$ to maintain a reasonable strength of network efects.<sup>2</sup>

Proposition 5. For vintage depreciation information goods with network efects, leasing dominates selling in vendor profit.

According to Proposition 5, the presence of network efects does not change the dominance of leasing over selling for vintage depreciation information goods. The vendor’s profit under both selling and leasing models is influenced by network efects, but in diferent ways. Under selling, as the strength of network efects increases, consumers have smaller incentives to delay adoption until period 2, because waiting becomes less attractive. Under leasing and in contrast, the optimal leasing fees are not influenced by network efects, but the number of adopters increases as the strength of network efects increases.

In addition to contributing to the literature on vintage depreciation by considering the consumer valuation depreciation over time, our extensions to consider network efects appear new in the literature. We are able to obtain closed-form solutions for both the selling model and the leasing model in the presence of network efects. This in turn allows us to explicitly compare selling and leasing, which is largely missing in the literature.<sup>3</sup> Next, we examine the case of individual depreciation with network efects, and Proposition 6 summarizes our results.

Proposition 6. For individual depreciation information goods with network efects, in terms of vendor profit,

(i) when $\theta \in [ 0 , s / ( 2 + 2 K - s ) ]$ , selling and leasing are equivalent;

(ii) when $\theta \in ( s / ( 2 + 2 K - s ) , ( 1 + K - s ) / ( 2 + 2 K - s ) ] .$ selling dominates leasing;

(iii) when $\theta \in ( ( 1 + K - s ) / ( 2 + 2 K - s ) , 1 ]$ , leasing dominates selling.

We illustrate Proposition 6 in Figure 7. Consistent with our analysis in Section 5.2, leasing induces waiting under individual depreciation. Consequently, when θ is relatively small (i.e., the magnitude of individual depreciation, $1 - \theta _ { \ast }$ , is large), selling dominates leasing. Note that when network efects do not exist, that is, when $s = 0$ , Proposition 6 reduces to Proposition 3.

Figure 7. Optimal Pricing Strategies Under Individual Depreciation with Network Efects (K <sup></sup> 7)  
![](/api/attachments/Y2VC9CFY/fulltext/images/a576ba63c54c2f06242e4eea56c74887af523f74e62ca5fd8daa57ce6c79bd08.jpg)

Comparing Proposition 6 to Proposition 5 thus ofers insights for pricing information goods with depreciation and network efects. For vintage depreciation information goods, leasing dominates selling. By contrast, the optimal pricing scheme for individual depreciation information goods largely depends on the magnitude of the depreciation, and selling dominates leasing when the magnitude of the depreciation is large.

It is also interesting to note the region in Figure 7 where selling and leasing are equivalent in generating vendor profit. This is so because in this region, individual depreciation is so strong that, in REE, all consumers will wait (under either leasing or selling) until period $^ { 2 , }$ making the selling model and the leasing model identical in our two-period setting. Consequently, they generate the same vendor profit.

Next we examine the interaction efects between the strength of network efects and the magnitude of valuation depreciation in vendor profit. We obtain the following results.

Proposition 7. For vintage depreciation information goods with network efects,

(i) the vendor’s profit is increasing and convex in the strength of network efects $( i . e . , \partial \tilde { \pi } ^ { * } / \bar { \partial } s > 0$ and ${ \partial ^ { 2 } } \tilde { \pi } ^ { * } / { \partial s ^ { 2 } }$ $> 0 ) .$ ;

(ii) the interaction efect between vintage depreciation and the strength of network efects in vendor profit is negative $( i . e . , \partial ^ { 2 } \tilde { \pi ^ { * } } / \partial ( \bar { 1 } - \theta ) \partial s < \ddot { 0 } )$

Proposition 8. For individual depreciation information goods with network efects,

(i) the vendor’s profit is increasing and convex in the strength of network efects $( i . e . , \partial \tilde { \pi } ^ { * } / \breve { \partial } s > 0$ and ${ \partial ^ { 2 } } \tilde { \pi } ^ { * } / { \partial s ^ { 2 } }$ $> 0 ) .$ ;

(ii) there exists a threshold $\hat { \theta } \in ( s / ( 2 + 2 K - s ) , ( 1 +$ $K - s ) / ( 2 + 2 K - s ) ]$ , when $\theta \in [ 0 , \hat { \theta } ]$ , the interaction efect between individual depreciation and the strength of network efects is positive $( i . e . , \stackrel { . } { \partial ^ { 2 } \pi ^ { * } } / \partial ( 1 - \theta ) \partial s \geq 0 )$ ;

(iii) when $\theta \in ( { \hat { \theta } } , 1 ] .$ , the interaction efect between individual depreciation and the strength of network efects is negative $\left( i . e . , \partial ^ { 2 } \tilde { \pi } ^ { * } / \partial ( 1 - \theta ) \partial s < \tilde { 0 } \right)$

While it is not surprising to find that the vendor’s marginal profit increases in the strength of network efects under both vintage depreciation and individual depreciation, we note several new and interesting findings. First, when leasing dominates selling (under both types of consumer valuation depreciation), the vendor’s profit loss due to stronger valuation depreciation can be remedied by network efects. Theoretically, this means that in the case when leasing dominates selling, network efects mitigate consumer valuation depreciation. Practically, this suggests that stronger network efects not only help a leasing vendor attract more consumers but also help him alleviate consumer valuation depreciation. Second, we identify a region under

Figure 8. Interaction Efects Between Individual Valuation Depreciation and Network Efects in Vendor Profit (K <sup></sup> 7)  
![](/api/attachments/Y2VC9CFY/fulltext/images/c0fee4b46528aa58010c335939bbe35bee82bda628383fd3a294104fc3ac2f6b.jpg)  
which a vendor of individual depreciation information goods favors the selling model over the leasing model. Here we uncover nontrivial dynamics in the interplay between individual valuation depreciation and network efects. The interaction efects between the two factors can be negative or positive, depending on a threshold $\hat { \theta }$ (defined in the appendix). As we illustrate in Figure 8, as the strength of network efects increases from $s = 0$ to $s = 0 . 8$ , when $\theta > \hat { \theta } _ { \ast }$ , the interaction efect between individual depreciation and network efects is negative; however, when $\theta \leq { \hat { \theta } } .$ , the interaction efect becomes positive. In this region, as we show in Proposition $^ { 6 , }$ the vendor favors selling over leasing. Here both network efects and individual depreciation induce consumer waiting behaviors, because consumers expect to benefit from a larger network as well as a lower period 2 selling price. Consequently, the vendor is able to charge a higher selling price $p _ { 2 }$ . (Indeed, it is straightforward to show that $\dot { \partial } ( p _ { 2 } ^ { * } ) ^ { 2 } \dot { / } \partial ( 1 - \theta ) \partial s \geq 0$ when $\mathsf { \bar { \theta } } \in [ 0 , \hat { \theta } ) . )$ ) This, in turn, drives the positive interaction efect.

## 6.2. Conditional Pricing

In this section, we consider conditional pricing whereby the vendor commits to having a discount in period 2 for period 1 adopters and compare this strategy with the selling model and the leasing model. We define conditional pricing as the following. At the beginning of period 1, the vendor commits that the period 2 leasing fee $( r _ { d } )$ for period 1 adopters will be lower than the period 2 leasing fee for new adopters $( r _ { 2 } )$ , i.e., $r _ { d } < r _ { 2 }$ We have the following results.

Proposition 9. For vintage depreciation information goods, conditional pricing is dominated by leasing.

Proposition 10. For individual depreciation information goods, when $\theta \in [ 0 , \frac { 1 } { 2 } )$ , conditional pricing is weakly dominated by selling; otherwise, when $\not \in [ { \frac { 1 } { 2 } } , 1 ]$ , conditional pricing is dominated by leasing.

The intuition behind Proposition 9 is as follows. For vintage depreciation information goods and under leasing, the vendor does not incur any profit loss due to waiting; therefore, conditional pricing cannot further improve vendor profit.

For individual depreciation information goods, when $\theta \in \left[ { \textstyle { \frac { 1 } { 2 } } } , 1 \right]$ , the existing adopters are willing to pay a period 2 leasing fee that is almost the same as the period 1 leasing fee. Thus, conditional pricing (which ofers a discounted price to existing adopters) is not needed. When $\theta \in [ 0 , \frac { 1 } { 2 } )$ , while conditional pricing does improve profit, such an improvement does not cause conditional pricing to dominate selling. Here is the intuition. Even at the discounted leasing fee $\boldsymbol { r } _ { d } ,$ not all existing adopters continue to lease in period 2 because of heavy individual depreciation. This, coupled with the high period 2 leasing fee $r _ { 2 } ,$ cap the vendor’s profit.

The above insight can be illustrated using the twoconsumer example in Section 3.2. Under leasing and individual depreciation, the optimal profit is 10 (see the bottom-right corner in Table 2). Now consider conditional pricing. Suppose $r _ { 1 } = 1 0 , r _ { 2 } = 4 ,$ , and $r _ { d } = 2 . 5$ In this case, consumer $V _ { 1 }$ has zero surplus if renting in both periods. However, consumer $V _ { 1 }$ has a surplus of 6 $( \mathrm { i . e . , ~ } 1 0 - 4 = 6 )$ if renting only in period 2. Therefore, the vendor must lower $r _ { 1 }$ to 4 to attract consumer $V _ { 1 } ^ { ' \mathrm { s } }$ adoption in period 1. In REE, the optimal conditional pricing strategies are $r _ { 1 } = r _ { 2 } = 4$ and $r _ { d } = 2 . 5 $ , and vendor profit is $4 + 4 + 2 . 5 = 1 0 . 5$ . This example illustrates the case when conditional pricing dominates leasing, but is weakly dominated by selling.

As a remark, we stress here that such conditional pricing requires vendor commitment at the beginning of period 1. This is a fundamental departure from our baseline model assumption where we do not require such a price commitment. It is well known in the literature that vendor price commitment is not desirable because of the vendor’s inability to do so (e.g., Coase 1972, Bulow 1982, Katz and Shapiro 1986). This issue is central to the time-inconsistency problem we discussed in Sections 1 and 2.

## 6.3. The Hybrid Model

Finally, we briefly discuss the hybrid model, where consumers have the freedom to choose between buying and renting. We have the following proposition.

Proposition 11. For both vintage and individual depreciation information goods, in a two-period setting, the hybrid model cannot further increase the vendor’s profit.

We illustrate this somewhat surprising finding using our previous two-consumer example in Section 3.2. For brevity, we illustrate only with the case of individual depreciation. Similar examples can be constructed for the case of vintage depreciation. We first note that for the hybrid model to be optimal, it needs to be used by consumers. This in turn imposes the following structure in a two-period setting: one consumer will buy and the other will rent in period 1. Without loss of generality, let us assume that in period 1, consumer $V _ { 1 }$ chooses to buy and consumer $\bar { V } _ { 2 }$ chooses to rent. In period 2, only consumer $V _ { 2 }$ is left, with a depreciated valuation of $\dot { 4 } \times 0 . 2 5 = 1$ . Therefore, the optimal period 2 leasing fee is 1 $. \left( r _ { 2 } ^ { * } = 1 \right)$ . Then the optimal period 1 leasing fee is 1 $( r _ { 1 } ^ { * } = 1 )$ ; otherwise, consumer $V _ { 2 }$ would delay her adoption. If the leasing fee is 1 in both periods, then the optimal selling price is $2 \ ( p _ { 1 } ^ { * } = 2 )$ . Otherwise, consumer $V _ { 1 }$ would choose to rent in both periods, rather than buy in period 1. Thus, the optimal total profit is 4 under the hybrid model, which is suboptimal because the vendor would make more profit using either a pure selling strategy (10.5) or a pure leasing strategy (10).

The key intuition behind Proposition 11 is that ofering the hybrid model does not further segment the market (thus resulting in higher profit). Rather, what it does is ofer additional incentives for consumers to wait, which, in turn, does not improve profit. For both types of consumer value depreciation, in REE, it is suboptimal to have both buying and renting consumers coexist in either period. In a two-period setting such as ours, selling and leasing models are profit equivalent in period 2. Then, both selling and leasing adopters must coexist in period 1 for the hybrid model to be optimal. This structure imposes an additional constraint on the selling price, $p _ { 1 } = r _ { 1 } + r _ { 2 }$ . Otherwise, if $p _ { 1 } > r _ { 1 } + r _ { 2 } ,$ no consumers would choose to purchase in period 1 (all in favor of renting); if $p _ { 1 } < r _ { 1 } + r _ { 2 } ,$ no consumers would choose to rent in period 1 or in period 2 (all in favor of buying). Given this constraint, $p _ { 1 } = r _ { 1 } + r _ { 2 } ,$ , we see the hybrid model cannot further increase vendor profit, as it will never be chosen by any consumers. Note that Proposition 11 is obtained in a two-period setting assuming no further price commitment by the vendor ex ante.<sup>4</sup> We leave it for future research to study whether or not Proposition 11 can be extended to a T-period setting $( T > 2 )$ or to a continuous-time setting.

## 7. Conclusion

We examine the selling versus leasing debate for information goods in the context of valuation depreciation, using a two-period game-theoretic model. Our model considers two types of consumer valuation depreciation for information goods: vintage depreciation and individual depreciation. We are among the first to study individual depreciation information goods. While vintage depreciation has been studied in the durable goods literature for physical goods on the product side, we examine it in the context of information goods where we focus on the consumerside valuation depreciation over time. Our extensions to consider network efects appear new in the literature, and we ofer several new insights. We find that, for vintage depreciation information goods, leasing dominates selling, with and without the presence of network efects. This seems to be consistent with some of the best business practices. For example, vendors of cloud storage services (e.g., Dropbox) and cloud computing services (e.g., Rackspace) often favor the leasing model. We would expect the network efects of the former to be significant because of the nature of user collaboration, while the latter would have limited or no network efects. We then use the case of vintage depreciation as a benchmark for the case of individual depreciation, the main focus of our paper.

We find that leasing dominates selling when the magnitude of individual depreciation is small, which is consistent with real-world observations, such as Microsoft Ofice 365.<sup>5</sup> As yet another example, Wolfram Alpha, which is well known for its computing software solution Wolfram Mathematica, started to ofer software on a subscription basis, starting with its version 8.<sup>6</sup>

Interestingly, we also find that selling dominates leasing when individual adopters heavily depreciate their valuation of information goods, and this finding holds true in the presence of network efects as well. Furthermore, the interaction efect between individual depreciation and network efects can be either negative or positive. Our findings have immediate practical implications. For example, many mobile app games, such as Angry Birds or Draw Something receive a lot of attention because of their novelty, but then their novelty wears of, and users quickly get bored or distracted by similar products. In this case, selling could be more profitable than leasing. Amazon recently announced rental services for its Kindle digital book oferings (i.e., Kindle Unlimited). Our analytical results are not in favor of this pricing model migration, which is echoed by Amazon’s limited oferings in Kindle Unlimited, especially in certain categories with strong individual depreciation.<sup>7</sup>

Our model results also suggest an interesting strategic interaction between individual depreciation $( \mathrm { i . e . , } \theta )$ and network efects (i.e., s). For vendors of information goods, the optimal pricing scheme can be obtained by locating themselves in Figure 7 with their parameter pair of θ and s. For example, sales of individual mp3 music titles rely on the selling model only, because of significant individual depreciation $( \mathrm { e . g . } ,$ iTunes). However, the leading music streaming service website Spotify has been very successful in using the periodic subscription pricing model. It ofers more than 20 million songs produced by multiple publishers, with weekly updates. Linking this observation to our model, we posit that Spotify’s ofering of a package of songs, rather than a single song, is relatively less sensitive to individual depreciation, making the leasing model more favorable. Spotify’s ofering of a music collection and Amazon’s Kindle Unlimited represent examples of how vendors of information goods can mitigate the efect of individual depreciation through bundling. In addition, vendors of similar products may choose diferent pricing schemes depending on the strength of network efects. Take computer games as an example. The leasing model is popular among the network-based versions of games (e.g., Blizzard’s World of Warcraft) when network efects are strong; on the other hand, selling becomes more favorable when network efects are weak (e.g., the single-player game Warcraft III).

For future research, it would be interesting to extend our model to the multiple-period or continuous-time setting. Another fruitful avenue of future research would be to test our model predictions empirically.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous reviewers for their constructive feedback throughout the review process. The authors also thank Hemant Bhargava, Andrew Ching, seminar participants at Southern Methodist University, Temple University, University of California at Davis, University of Florida, University of Electronic Science and Technology of China, and University of North Carolina at Charlotte as well as participants at the Workshop on Information Systems and Economics (WISE 2013), POMS 25th Annual Conference (2014), and the Theory in Economics of Information Systems Workshop (TEIS 2015) for their helpful comments and discussions.

## Appendix. Proofs

Proof of Proposition 2. Denote by $S W ^ { S , A }$ the social welfare for vintage depreciation information goods (A) under the selling model (S). We have

$$
S W ^ {S, A} = \int_ {v _ {1}} ^ {1} (1 + \theta) v d v + \int_ {v _ {2}} ^ {v _ {1}} \theta v d v.
$$

Since $v _ { 1 } = 1 - N _ { 1 } ^ { * }$ and $v _ { 2 } = 1 - N _ { 1 } ^ { * } - N _ { 2 } ^ { * } ,$ and $N _ { 1 } ^ { * }$ and N<sup>∗</sup> are given by Equation (3), solving, we have $v _ { 1 } = ( \dot { 2 } + \theta ) / ( 4 \bar { + } \theta )$ and $v _ { 2 } = ( 2 + \theta ) / ( 2 ( 4 + \theta ) )$ . Inserting $v _ { 1 }$ and $v _ { 2 }$ into $S W ^ { S , A }$ gives

$$
\begin{array}{l} S W ^ {S, A} = \int_ {(2 + \theta) / (4 + \theta)} ^ {1} (1 + \theta) v   \mathrm{d} v + \int_ {(2 + \theta) / (2 (4 + \theta))} ^ {(2 + \theta) / (4 + \theta)} \theta v   \mathrm{d} v \\ = \frac {4 + 3 \theta}{8} - \frac {1}{2 (4 + \theta)}. \end{array}
$$

Similarly, the social welfare for vintage depreciation information goods (A) under the leasing model (L), denoted as $S W ^ { L , A }$ , by

$$
S W ^ {L, A} = \int_ {v _ {1}} ^ {1} v \mathrm{d} v + \int_ {v _ {2}} ^ {1} \theta v \mathrm{d} v = \int_ {1 / 2} ^ {1} v \mathrm{d} v + \int_ {1 / 2} ^ {1} \theta v \mathrm{d} v = \frac {3 (1 + \theta)}{8}.
$$

Proposition 2 holds because $S W ^ { S , A } - S W ^ { L , A } = \theta / ( 8 ( 4 + \theta ) )$ $\geq 0 .$ 

Proof of Lemma 1. This is the case for individual depreciation information goods (B) under the selling model (S). We prove the lemma via backward induction. At the beginning of period 2, potential adopter types are located in interval $[ 0 , v _ { 1 } ]$ . The marginal consumer type in period $2 , v _ { 2 } ,$ , satisfies $v _ { 2 } = p _ { 2 }$ . The selling vendor’s period 2 profit is $p _ { 2 } ( v _ { 1 } - v _ { 2 } )$ Optimizing the vendor’s profit gives $p _ { 2 } ^ { * } = v _ { 1 } / 2$ and $\pi _ { > } ^ { * } = v _ { 1 } ^ { 2 } / 4$

Next, consider the vendor’s problem in period 1. The marginal consumer type in period $1 , v _ { 1 } ,$ , satisfies the following equation:

$$
U _ {v _ {1}} ^ {S, B} (D D) = U _ {v _ {1}} ^ {S, B} (O D) \Rightarrow v _ {1} + \theta v _ {1} - p _ {1} = v _ {1} - p _ {2} ^ {*}.\tag{A.1}
$$

Inserting $p _ { 2 } ^ { * } = v _ { 1 } / 2$ into Equation (A.1) results in $p _ { 1 } =$ $( 1 + 2 \theta ) v _ { 1 } / 2 .$

At the beginning of period 1, the vendor’s profit is $\pi ^ { S , B } =$ $p _ { 1 } ( 1 - v _ { 1 } ) + \stackrel { \smile } { \pi } _ { 2 } ^ { * } ( v _ { 1 } ) = v _ { 1 } [ \bar { 2 } ( 1 + 2 \theta ) - ( 1 + 4 \theta ) v _ { 1 } ] / \bar { 4 } ,$ which is concave in $v _ { 1 } . { \mathrm { S o l v i n g } } ,$ , we have $v _ { 1 } ^ { * } = ( 1 + 2 \theta ) / ( 1 + 4 \theta )$ <sup>)</sup>. Lemma 1 follows immediately. <sup></sup>

Proof of Lemma 2. Consider period 2. At the beginning of period 2, period 1 adopters are distributed in the interval $( v _ { 1 } , 1 ]$ . Under individual depreciation, all consumers are potential adopters in period 2. There are three scenarios to consider in period 2:

Scenario 1: $v _ { 1 } = 1$

Scenario 2: $v _ { 1 } < 1 , v _ { 1 } < \theta .$

Scenario 3 $: v _ { 1 } < 1 , v _ { 1 } \geq \theta .$

Scenario 1 implies that there are no adopters in period 1. In this case, period 2 marginal consumer type v satisfies $\boldsymbol { v } _ { 2 } = \boldsymbol { r } _ { 2 } ,$ , and period 2 profit is $r _ { 2 } ( 1 - v _ { 2 } )$ . Solving the vendor’s period 2 profit optimization problem gives $\begin{array} { r } { v _ { 2 } ^ { * } = \frac { 1 } { \lambda } } \end{array}$ and $\begin{array} { r } { \pi _ { 2 } ^ { * } = \frac { 1 } { 4 } } \end{array}$

Under scenario 2, there are three pricing regions in period $2 \colon ( 1 ) \ v _ { 2 } \leq \theta v _ { 1 } , ( 2 ) \ v _ { 2 } \in ( \theta v _ { 1 } , v _ { 1 } )$ , and $( 3 ) \ v _ { 2 } \in [ v _ { 1 } , \theta ]$ We first rule out the second price region, which is infeasible according to Lemma $_ { \mathrm { A . 1 } }$

Lemma A.1. For individual depreciation information goods and under the leasing model, given any rental price pair $( r _ { 1 } , r _ { 2 } ) .$ , if there are simultaneous period 1 only and period 2 only adopters, then $( r _ { 1 } , r _ { 2 } )$ does not constitute a REE.

We prove Lemma A.1 by contradiction. Assume that consumers correctly anticipate the rental price pair $( r _ { 1 } , r _ { 2 } )$ , and period 1 only and period 2 only adopters coexist in the market. The surplus for a type v period 1 only adopter is $v - r _ { 1 } .$ Similarly, the surplus for a type v period 2 only adopter is $v - r _ { 2 }$ . Rational consumers will rent only in the period with the smaller rental price, unless $r _ { 1 } = r _ { 2 }$ (in which case there is no decision for the vendor to make in period 2), a contradiction.

Lemma A.1 thus implies that only the first and third price regions are feasible for scenario 2. In price region (1), the optimal period 2 rental price is obtained by maximizing period 2 profit $r _ { 2 } ( 1 - v _ { 2 } )$ , subject to $r _ { 2 } < \theta v _ { 1 }$ and $r _ { 2 } = v _ { 2 }$ . The optimal solutions and profit are

$$
r _ {2} ^ {*} = \left\{ \begin{array}{l l} \frac {1}{2}, & v _ {1} \geq \frac {1}{2 \theta}, \\ \theta v _ {1}, & v _ {1} <   \frac {1}{2 \theta}; \end{array} \right. \quad \pi_ {2} ^ {*} = \left\{ \begin{array}{l l} \frac {1}{4}, & v _ {1} \geq \frac {1}{2 \theta}, \\ \theta v _ {1} (1 - \theta v _ {1}), & v _ {1} <   \frac {1}{2 \theta}. \end{array} \right.\tag{A.2}
$$

Similarly, the optimal rental fee $r _ { 2 } ^ { * }$ and the corresponding profit $\pi _ { 2 } ^ { * }$ in price region (3) are

$$
r _ {2} ^ {*} = \left\{ \begin{array}{l l} v _ {1}, & v _ {1} \geq \frac {\theta}{2}, \\ \frac {\theta}{2}, & v _ {1} <   \frac {\theta}{2}; \end{array} \right. \quad \pi_ {2} ^ {*} = \left\{ \begin{array}{l l} v _ {1} \bigg (1 - \frac {v _ {1}}{\theta} \bigg), & v _ {1} \geq \frac {\theta}{2}, \\ \frac {\theta}{4}, & v _ {1} <   \frac {\theta}{2}. \end{array} \right.
$$

In scenario 3, there is only one feasible price region, $v _ { 2 } \leq$ $\theta v _ { 1 }$ . Therefore, the solution is identical to Equation $( \mathrm { A } . 2 )$ , and we have a total of five candidate strategies for period 1. We must combine them for the optimal period 2 strategies under all possible values of $v _ { 1 } { : }$

Period 2, Candidate Strategy 1: $\begin{array} { r } { v _ { 1 } = 1 , r _ { 2 } = \frac { 1 } { \gamma } . } \end{array}$ , and $\begin{array} { r } { \pi _ { 2 } = \frac { 1 } { 4 } } \end{array}$

Period 2, Candidate Strategy $\textstyle 2 \colon v _ { 1 } \in [ 1 / ( 2 \theta ) , 1 ) , r _ { 2 } = { \frac { 1 } { 2 } }$ , and $\begin{array} { r } { \pi _ { 2 } = \frac { 1 } { 4 } } \end{array}$

Period 2, Candidate Strategy 3 $: v _ { 1 } < 1 / ( 2 \theta ) , r _ { 2 } = \theta v _ { 1 } ,$ and $\pi _ { 2 } = \theta v _ { 1 } ( 1 - \theta v _ { 1 } )$

Period 2, Candidate Strategy 4: $v _ { 1 } < \theta / 2 , ~ r _ { 2 } = \theta / 2 ,$ , and $\pi _ { 2 } = \theta / 4 .$

Period 2, Candidate Strategy 5: $v _ { 1 } \in [ \theta / 2 , \theta ] , r _ { 2 } = v _ { 1 } ,$ and $\pi _ { 2 } = v _ { 1 } ( 1 - v _ { 1 } / \theta )$

Combining all five candidate strategies leads to the following period 2 optimal strategies for diferent regions of $v _ { 1 }$ and θ:

Region 1: $\begin{array} { r } { v _ { 1 } = 1 , r _ { 2 } = \frac { 1 } { 2 } , } \end{array}$ , and $\begin{array} { r } { \pi _ { 2 } = \frac { 1 } { 4 } } \end{array}$

Region 2: $v _ { 1 } \in [ 1 / ( 2 \theta ) , \hat { 1 } )$ and $\begin{array} { r } { \theta \in [ \frac { 1 } { 2 } , 1 ] , r _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , and $\begin{array} { r } { \pi _ { 2 } = \frac { 1 } { 4 } } \end{array}$

Region 3: $v _ { 1 } \in [ \theta / ( 1 + \theta + \theta ^ { 2 } ) , 1 )$ and $\theta \in [ \bar { 0 } , \frac { 1 } { 2 } ) , r _ { 2 } = \theta \bar { v _ { 1 } }$ and $\pi _ { 2 } = \theta v _ { 1 } ( 1 - \theta v _ { 1 } )$

Region $4 \colon \ v _ { 1 } \ \in \ [ \theta / ( 1 \ + \ \theta \ + \ \theta ^ { 2 } ) , 1 / ( 2 \theta ) )$ and $\theta \ \in \ [ \frac { 1 } { 2 }$ $( \sqrt { 5 } - 1 ) / 2 ) , r _ { 2 } = \theta v _ { 1 } , \mathrm { a n d } \pi _ { 2 } = \theta v _ { 1 } ( 1 - \theta v _ { 1 } ) .$

Region√ $5 \colon \ v _ { 1 } \ \in \ [ ( 1 \ - \ \sqrt { 1 - \theta } ) / ( 2 \theta ) , 1 / ( 2 \theta ) )$ and $\theta \in$ $[ ( \sqrt { 5 } - 1 ) / 2 , 1 ] , r _ { 2 } = \theta v _ { 1 } , \mathrm { a n d } \pi _ { 2 } = \theta v _ { 1 } ( \underline { { { 1 - \theta v _ { 1 } } } } ) .$

Region 6: v <sup>∈</sup> <sup>[</sup>0, θ<sup>/</sup>2<sup>)</sup> and $\theta \in [ 0 , ( \sqrt { 5 } - 1 ) / 2 ) , r _ { 2 } = \theta / 2 ,$ and $\pi _ { 2 } = \theta / 4$

$$
\text {   Region   } 7 \colon v _ {1} \in [ (1 - \sqrt {1 - \theta}) / (2 \theta), 1 / (2 \theta))
$$

$$
[ (\sqrt {5} - 1) / 2, 1 ], r _ {2} = \theta / 2, \text {   and   } \pi_ {2} = \theta / 4.
$$

$$
\theta \in
$$

Region 8: $v _ { 1 } \in [ \theta / 2 , \theta / ( 1 + \theta + \theta ^ { 2 } ) )$ and $\theta \in [ 0 , ( \sqrt { 5 } - 1 ) / 2 )$ $r _ { 2 } = v _ { 1 } , \mathrm { a n d } \pi _ { 2 } = v _ { 1 } ( 1 - v _ { 1 } / \theta ) .$

In period 1, we move through Regions 1 to 8 to solve for $v _ { 1 } ^ { * }$ . There are a total of six candidate strategies in period 1:

Period 1, Candidate Strategy $1 \colon v _ { 1 } = 1 { \mathrm { ~ a n d ~ } } \pi = { \frac { \bar { 1 } } { 4 } }$

Period 1, Candidate Strategy 2: $\begin{array} { r } { \theta \in [ \frac { 1 } { 2 } , 1 ] , v _ { 1 } = \dot { 1 } / ( 2 \theta ) } \end{array}$ , and $\pi = { \textstyle { \frac { 3 } { 4 } } } - 1 / ( 4 \theta )$

Period 1, Candidate Strategy $3 \colon v _ { 1 } = 1 / ( 1 + \theta )$ and $\pi =$ $\theta / ( 1 + \theta )$

Period 1, Candidate Strategy 4: $\theta \in [ 0 , ( \sqrt { 5 } - 1 ) / 2 ) , v _ { 1 } = \theta / 2 ,$ and $\pi = \theta ( 3 - \theta ) / 4$

Period 1, Candidate Strategy $5 \colon \theta \in [ ( \sqrt { 5 } - 1 ) / 2 , 1 ] , v _ { 1 } = ( 1 -$ ${ \sqrt { 1 - \theta } } ) / ( 2 \theta )$ , and $\pi = ( \theta ^ { 3 } + 2 [ ( 1 - \theta ) \sqrt { 1 - \theta } - 1 ] + 3 \theta ) / ( 4 \theta ^ { 2 } )$ Period 1, Candidate Strategy 6: $\theta \in [ 0 , ( \sqrt { 5 } - 1 ) / 2 ) , v _ { 1 } =$ $\theta / ( 1 + \theta + \theta ^ { 2 } )$ , and $\pi = \theta ( 1 + \bar { \theta ^ { + } } 2 \theta ^ { 2 } ) / ( 1 + \theta + \theta ^ { 2 } ) ^ { 2 } .$

The optimal solution in Lemma 2 can be obtained by comparing all candidate strategies in period 1. <sup></sup>

Proof of Proposition 4. Denote by $S W ^ { S , B }$ the social welfare for individual depreciation information goods (B) under the selling model (S). From Lemma 1, we have

$$
S W ^ {S, B} = \int_ {v _ {1}} ^ {1} (1 + \theta) v d v + \int_ {v _ {2}} ^ {v _ {1}} v d v = \frac {3 + 4 \theta [ 9 + \theta (1 9 + 1 2 \theta) ]}{8 (1 + 4 \theta) ^ {2}}.
$$

Denote by $S W ^ { L , B }$ the social welfare for individual depreciation information goods (B) under the leasing model (L). From Lemma $^ { 2 , }$ , we have the following two cases:

Case 1. $\textstyle \theta < { \frac { 1 } { 3 } }$ . Then there are only period 2 adopters and $\begin{array} { r } { v _ { 2 } = \frac { 1 } { 2 } } \end{array}$ , which gives that $\begin{array} { r } { S W ^ { L , B } = \int _ { 1 / 2 } ^ { 1 } v \mathrm { d } v = \frac { 3 } { 8 } < S W ^ { S , B } } \end{array}$

Case 2. $\textstyle . \theta \geq { \frac { 1 } { 3 } } . v _ { 1 } = 1 / ( 1 + \theta )$ and $\dot { v } _ { 2 } = \theta / ( 1 + \theta )$ . All period 1 adopters continue adopting in period 2. Then

$$
S W ^ {L, B} = \int_ {v _ {1}} ^ {1} (1 + \theta) v d v + \int_ {v _ {2}} ^ {v _ {1}} v d v = \frac {1}{2} + \frac {\theta^ {2}}{2 (1 + \theta)} <   S W ^ {S, B}.
$$

Thus, in either case, $S W ^ { L , B } < S W ^ { S , B }$ 

Proof of Proposition 5. We first derive a selling vendor’s profit.

First, consider period 2. The marginal consumer type $v _ { 2 }$ satisfies $p _ { 2 } = \bar { \theta ( v _ { 2 } + s ( ( 1 - v _ { 2 } ) / ( 1 + \bar { K } ) ) ) }$ <sup>)</sup>. Period 2 profit is $p _ { 2 } ( v _ { 1 } - v _ { 2 } ) / ( 1 + K ) = \theta ( v _ { 1 } - v _ { 2 } ) ( s + ( 1 + K - s ) v _ { 2 } ) / ( 1 + K ) ^ { 2 } \jmath _ { 1 }$ which is always concave in $v _ { 2 } .$ . The interior optimal solution is $v _ { 2 } ^ { * } = \bar { \frac { 1 } { 2 } } \bar { [ } v _ { 1 } - s / ( 1 + K \bar { - } s ) ]$ , and $p _ { 2 } ^ { * }$ is nonnegative when $v _ { 1 } \geq - s \bar { / } ( 1 + K - s ) .$ . Therefore, for ${ \bar { v _ { 1 } } } ^ { \bar { > } } \bar { > } - s / ( 1 + \bar { K } - s )$ $p _ { \gamma } ^ { \ast } = \theta ( s + ( 1 + K - s ) v _ { 1 } ) / ( 2 ( 1 + K ) )$ , and $( { \bar { \tilde { \pi } } _ { 2 } } ^ { S , A } ) ^ { * } = \theta ( s + ( 1 +$ $\bar { K ^ { - } } s ) v _ { 1 } ) ^ { 2 } / ( 4 ( 1 + K ) ^ { 2 } ( 1 + K - s ) )$ . Otherwise $v _ { 2 } ^ { * } = v _ { 1 }$

Next, consider period 1. The marginal consumer $v _ { 1 }$ is indiferent between buying in period 1 and buying in period $^ { 2 , }$ which implies

$$
v _ {1} + s N _ {1} - p _ {1} + \theta (v _ {1} + s (N _ {1} + N _ {2})) ^ {+} = \theta (v _ {1} + s (N _ {1} + N _ {2})) ^ {+} - p _ {2}.
$$

This leads to $p _ { 1 } = ( 2 + \theta ) [ s + ( 1 + K - s ) v _ { 1 } ] / ( 2 ( 1 + K ) )$ . Inserting $p _ { 1 }$ back into the profit function $p _ { 1 } ( 1 - v _ { 1 } ) + ( \tilde { \pi } _ { 2 } ^ { S , A } ) ^ { * }$ <sup>∗</sup> gives

$$
\begin{array}{l} \tilde {\pi} ^ {S, A} = \frac {2 s (2 + \theta) (1 + 2 K) - s ^ {2} (4 + \theta)}{4 (1 + K) ^ {2} (1 + K - s)} \\ \qquad - \frac {2 (1 + K - s) v _ {1} (2 s (4 + \theta) - 2 (1 + K) (2 + \theta))}{4 (1 + K) ^ {2} (1 + K - s)} \\ \qquad - \frac {(1 + K - s) (4 + \theta) v _ {1} ^ {2}}{4 (1 + K) ^ {2}}, \end{array}
$$

which is concave in $v _ { 1 }$ . The interior solution is

$$
v _ {1} ^ {*} = 1 - \frac {2 (1 + K)}{(1 + K - s) (4 + \theta)}.
$$

This interior solution is obtainable because $v _ { 1 } ^ { * } > - s /$ $( 1 + K - s )$ always holds. The optimal profit is $( 2 + \theta ) ^ { 2 } / ( 4 ( 1 +$ $K - s ) ( 4 + \theta ) )$

We now derive a leasing vendor’s profit.

The marginal consumer type $v _ { 2 }$ satisfies $r _ { 2 } = \theta ( v _ { 2 } \ +$ $s ( 1 - v _ { 2 } ) / ( 1 \bar { + } K ) )$ . Inserting this back into the profit function $r _ { 2 } ( 1 - v _ { 2 } ) / ( 1 + K )$ gives

$$
\tilde {\pi} _ {2} ^ {L, A} = \frac {\theta (1 - v _ {2}) [ s + (1 + K - s) v _ {2} ]}{(1 + K) ^ {2}},
$$

which is concave in $v _ { 2 } .$ . The interior solution is $v _ { \scriptscriptstyle 2 } ^ { \ast } = ( 1 +$ $K - 2 s ) / ( 2 ( 1 + K - s ) )$ , and the optimal period 2 profit is $( \tilde { \pi } _ { \gamma } ^ { L , A } ) ^ { * } = \theta / ( 4 ( 1 + K - s ) )$ .

In period 1, the marginal consumer type $v _ { 1 }$ satisfies $v _ { 1 } +$ $s N _ { 1 } - r _ { 1 } = 0$ , which implies that consumers are purely myopic. Using an argument similar to that in period $^ { 2 , }$ we can obtain that $v _ { 1 } ^ { * } = v _ { ? } ^ { * } = ( 1 + K - 2 s ) / ( 2 ( 1 + K - s ) )$ . The profit is $( 1 + \theta ) /$ $( 4 ( 1 + \mathbf { \bar { K } } - \mathbf { \bar { s } } ) )$

Leasing dominates selling in vendor profit, because <sup>(</sup>1 <sup>+</sup> $\theta ) / ( 4 ( 1 + \stackrel { \smile } { K } - s ) ) > ( 2 + \theta ) ^ { 2 } / \stackrel { \smile } { ( 4 } ( 1 + K - s ) \stackrel { \cdot } { ( 4 } + \theta ) )$ holds for all $\theta \in [ 0 , 1 ]$ . 

Proof of Proposition 6. This proof is similar to the proofs of Lemmas 1 and 2. For brevity, we provide only a sketch of the proof here. A detailed proof is available upon request.

Individual Depreciation: Selling. Under the selling model, in period 2, when $v _ { 1 } \geq - s / ( 1 + K - s )$ , there exists a unique interior solution such that $v _ { 2 } = { \textstyle { \frac { 1 } { 7 } } } ( v _ { 1 } - s / ( 1 + K - s ) )$ and the optimal period 2 profit is $[ s + ( \bar { 1 } + K - s ) v _ { 1 } ] ^ { 2 } / ( 4 ( 1 + K ) ^ { 2 } ( 1 +$ $\bar { K } - s ) )$ .

In period 1, the marginal consumer type $v _ { 1 }$ satisfies

$$
v _ {1} + s N _ {1} - p _ {1} + \theta (v _ {1} + s (N _ {1} + N _ {2})) = v _ {1} + s (N _ {1} + N _ {2}) - p _ {2}.
$$

Inserting $N _ { 2 } ^ { * }$ and $p _ { 2 } ^ { * }$ into this equation and rearranging, we obtain

$$
p _ {1} = \frac {(s (1 - v _ {1}) + v _ {1} (1 + K)) (1 + K - s \theta - 2 (s - (1 + K) \theta))}{2 (1 + K) (1 + K - s)}.
$$

We now have two cases to consider:

Case 1. $s \geq ( 1 + K ) ( 1 + 4 \theta ) / ( 3 + 2 \theta )$ , the profit function is convex in $v _ { 1 } , v _ { 1 } ^ { * } = 1$ , and $( \tilde { \pi } ^ { S , B } ) ^ { * } = 1 / ( 4 ( 1 + \bar { K ^ { - } } s ) )$

Case $2 . s < ( \bar { 1 + } K ) ( 1 + 4 \theta ) / ( 3 + 2 \theta ) .$ , the profit function is concave in $v _ { 1 } ,$ and the interior solution is $v _ { 1 } ^ { * } = 1 - ( 1 + K ) / 2 ( 1 / ( 1 +$ $K - s ) - 1 / ( 1 + K - 3 s + 4 \theta + 4 K \theta - 2 s \theta ) )$ , which is obtainable when $s \leq 2 \theta ( 1 + K ) / ( 1 + \theta )$

Combining Cases 1 and 2, we have the following: when $s \leq 2 \theta ( 1 + K ) / ( 1 + \theta ) , v _ { 1 } ^ { * } = 1 - ( ( 1 + K ) / 2 ) ( 1 / ( 1 + K - s ) - 1 / ( 1 + K ) / 2 ) ,$ $K - 3 s + 4 \theta + 4 K \theta - \bar { 2 s } \theta ) )$ and $( \tilde { \pi } ^ { S , B } ) ^ { * } = ( ( 1 + K ) ( 1 + 2 \theta ) -$ $s ( 2 + \theta ) ) ^ { 2 } / ( 4 ( 1 + K - s ) ^ { 2 } ( ( 1 + K ) ( 1 + 4 \theta ) - s ( 3 + 2 \theta ) ) ) ; \mathrm { o t h e r w i s e } ,$ when $s > 2 \theta ( 1 + K ) / ( 1 + \theta ) , v _ { 1 } ^ { * } = 1$ and $( \tilde { \pi } ^ { S , B } ) ^ { * } = 1 / ( 4 ( 1 + K - s ) )$

Individual Depreciation: Leasing. Under the leasing model, similar to the proof of Lemma 2, we consider multiple scenarios for period 2 and obtain the following candidate strategies:

Candidate Strategy $1 { : } v _ { 1 } = 1 , v _ { 2 } = ( 1 + K - 2 s ) / ( 2 ( 1 + K - s ) )$ and $( \tilde { \pi } _ { \gamma } ^ { L , B } ) ^ { * } = 1 / ( 4 ( 1 + K - s ) )$

Candidate Strategy $2 \colon v _ { 1 } \geq ( 1 + K - s ( 1 + \theta ) ) / ( 2 ( 1 + K - s ) \theta ) ,$ $v _ { 2 } = ( 1 + K - 2 s ) / ( 2 ( 1 + K - s ) )$ , and $( \tilde { \pi } _ { \gamma } ^ { L , B } ) ^ { * } = 1 / ( 4 ( 1 + K - s ) )$

Candidate Strategy 3 $: v _ { 1 } < ( 1 + K - \bar { s ( 1 + \theta ) ) } / ( 2 ( 1 + K - s ) \theta ) ,$ $v _ { 2 } = ( ( 1 + K ) \theta v _ { 1 } - s ( 1 - \theta ) ) / ( 1 + K - s ( 1 - \theta ) ) ,$ , and $( \tilde { \pi } _ { 2 } ^ { L , B } ) ^ { * } =$ $\theta [ s + ( 1 + K - s ) v _ { 1 } ] ( 1 - \theta v _ { 1 } ) / ( 1 + K - s ( 1 - \theta ) ) ^ { 2 } .$

Candidate Strategy 4: $v _ { 1 } \geq \theta / 2 - s / ( 2 ( 1 + K - s ) ) , v _ { 2 } = ( s ( 1 -$ $\theta ) + v _ { 1 } ( 1 + K ) ) / ( s ( 1 - \theta ) + \theta ( 1 + K ) )$ , and $( \tilde { \pi } _ { 2 } ^ { L , B } ) ^ { * } = \theta [ s + ( 1 +$ $K - s ) v _ { 1 } ] ( 1 - \theta v _ { 1 } ) / ( 1 + K - s ( 1 - \theta ) ) ^ { 2 }$

Candidate Strategy 5: $v _ { 1 } < \theta / 2 - s / ( 2 ( 1 + K - s ) ) , v _ { 2 } = ( 1 +$ $K - 2 s ) / ( 2 ( 1 + K - s ) )$ , and $( \tilde { \pi } _ { 2 } ^ { L , B } ) ^ { * } = \theta / ( 4 ( 1 + K - s ) )$

Combining all of these candidate strategies produces the optimal period 2 solution, which contains seven regions. In period 1, we search through all seven regions for an optimal solution that satisfies the REE criteria. The optimal period 1 solution contains at most four candidate solutions, each of which covers a certain parameter space (subregions) of $( \theta , s )$

In region $s \geq ( 1 + K ) ( 1 - 2 \theta ) / ( 1 - \theta )$ , leasing dominates selling. In region $s \geq 2 \theta ( 1 + K ) / ( 1 + \theta )$ , these two pricing models converge, with $v _ { 1 } = 1$ and $( \tilde { \pi } ^ { L , B } ) ^ { * } = 1 ( 4 ( 1 + K - s ) )$ <sup>)</sup>. In all other regions, selling dominates leasing. <sup></sup>

Proof of Proposition 7. $\tilde { \pi } ^ { \ast } = ( 1 + \theta ) / ( 4 ( 1 + K - s ) ) . \partial \tilde { \pi } ^ { \ast } / \partial s =$ $( 1 + \theta ) / ( 4 ( 1 + K - s ) ^ { 2 } ) > 0 .$ , and $\partial ^ { 2 } \tilde { \pi } ^ { * } / \partial s ^ { 2 } = ( 1 + \theta ) / ( 4 ( 1 +$ $K - s ) ^ { 3 } ) > 0 .$ We have $\partial ^ { 2 } \tilde { \pi } ^ { * } / \partial \theta \partial s = 1 / ( 4 ( 1 + K - s ) ^ { 2 } ) > 0 .$ , which means $\partial ^ { 2 } \tilde { \pi } ^ { \ast } / \partial ( 1 - \theta ) \partial s < 0 .$ 

Proof of Proposition 8. There are three regions to consider:

Region 1: $\theta \in [ 0 , s / ( 2 + 2 K - s ) ) ; \tilde { \pi } ^ { * } = 1 / ( 4 ( 1 + K - s ) ) ;$ ; and $\partial \tilde { \pi } ^ { * } / \bar { \partial } s = 1 / ( 4 ( 1 + K - s ) ^ { 2 } ) > 0 , \partial ^ { 2 } \tilde { \pi } ^ { * } / \partial s ^ { 2 } = 1 / ( 4 ( 1 + K - s ) ^ { 3 } ) > 0 ,$ and $\partial ^ { 2 } \tilde { \pi } ^ { \ast } / ( \partial \theta \partial s ) = 0 .$

Region $2 \colon \theta \in [ s / ( 2 + 2 K - s ) , ( 1 + K - s ) / ( 2 + 2 K - s ) )$ , and $\tilde { \pi } ^ { * } = ( ( 1 + 2 \theta ) ( 1 + K ) - ( \theta + 2 ) s ) ^ { 2 } / ( 4 ( K - s + 1 ) ^ { 2 } ( ( 1 + 4 \theta ) ( 1 + K ) - ( \theta + 2 ) s ) ^ { 2 } ) ^ { 2 }$ $( 2 \theta + 3 ) s ) )$

$$
\begin{array}{r l} & {\frac {\partial \tilde {\pi} ^ {*}}{\partial s} = [ 1 + K + 2 \theta + 2 K \theta - s (2 + \theta) ] \times [ (1 + K) (1 + K - 3 s)} \\ & {\qquad + 6 s ^ {2} + (2 (1 + K) ^ {2} - 1 7 (1 + K) s + 7 s ^ {2}) \theta} \\ & {\qquad + 2 \theta^ {2} (1 + K - 2 s) (1 + K - 3 s) ]} \\ & {\qquad \cdot [ 4 (1 + K - s) ^ {3} ((1 + K) (1 + 4 \theta) - s (3 + 2 \theta)) ^ {2} ] ^ {- 1},} \end{array}
$$

which is positive.

$$
\begin{array}{r l} \frac {\partial^ {2} \tilde {\pi} ^ {*}}{\partial s ^ {2}} = \frac {1}{8} \Bigg (- \frac {1 + K + 5 s}{(1 + K - s) ^ {4}} + \frac {2 (4 + 4 K - s) \theta}{(1 + K - s) ^ {4}} & \\ + \frac {2 5 (1 + K) ^ {2}}{(- 2 - 2 K + s) ^ {2} (1 + K + 4 \theta + 4 K \theta - s (3 + 2 \theta)) ^ {3}} \Bigg) & \\ + \frac {1 0 (1 + K)}{8 (2 + 2 K - s) ^ {2} (1 + K + 4 \theta + 4 K \theta - s (3 + 2 \theta)) ^ {2}} & \\ + \frac {1}{8 (2 + 2 K - s) ^ {2} (1 + K + 4 \theta + 4 K \theta - s (3 + 2 \theta))}, \end{array}
$$

which is positive.

$$
\begin{array}{r} \frac {\partial^ {2} \tilde {\pi} ^ {*}}{\partial s \partial \theta} = \frac {1}{8} \Bigg (\frac {3 + 3 K - s}{(1 + K - s) ^ {3}} - \frac {1}{(1 + K - 3 s + 4 \theta + 4 K \theta - 2 s \theta) ^ {2}} \\ - \frac {1 0 (1 + K)}{(1 + K + 4 \theta + 4 K \theta - s (3 + 2 \theta)) ^ {3}} \Bigg), \end{array}
$$

which is not always positive. However, we can show that $\partial ^ { 2 } \tilde { \pi } ^ { * } / \partial s \partial \theta$ is increasing in θ, which implies that there exists a unique $\hat { \theta }$ such that the cross-derivative is negative for $\theta \in$ $[ s / ( 2 \bar { + } 2 K - s ) , \hat { \theta } )$ and nonnegative for $\theta \in [ \tilde { \hat { \theta } } , ( 1 + K - s ) /$ $( 2 + 2 K - s ) ) .$

Region $3 \colon \theta \in [ ( 1 + K - s ) / ( 2 + 2 K - s ) , 1 ]$ , and $\tilde { \pi } ^ { * } = ( 2 ( 1 + K )$ $\theta - s ( 1 - \theta ) ) ^ { 2 } / ( 4 ( 1 + K - s ) ( s ^ { 2 } ( 1 - \theta ) ^ { 2 } + ( 1 + K ) ^ { 2 } \theta ( 1 + \theta ) -$ $( 1 + K ) s ( 1 - \theta ^ { 2 } ) ) )$

$$
\begin{array}{r l} \frac {\partial \tilde {\pi} ^ {*}}{\partial s} = & ((2 \theta (K + 1) + (\theta - 1) s) (2 \theta^ {2} (\theta + 1) (K + 1) ^ {3} \\ & + 6 (\theta - 1) ^ {2} \theta (K + 1) s ^ {2} + (\theta - 1) (7 \theta - 1) (K + 1) ^ {2} s \\ & + (\theta - 1) ^ {3} s ^ {3})) \cdot (4 (K - s + 1) ^ {2} (\theta (\theta + 1) (K + 1) ^ {2} \\ & + (\theta^ {2} - 1) (K + 1) s + (\theta - 1) ^ {2} s ^ {2}) ^ {2}) ^ {- 1}, \end{array}
$$

which is positive for $\theta \in [ ( 1 + K - s ) / ( 2 + 2 K - s ) , 1 ]$

$$
\begin{array}{l} \frac {\partial^ {2} \tilde {\pi} ^ {*}}{\partial s ^ {2}} \\ = \frac {1}{2 (K - s + 1) ^ {3} (\theta (\theta + 1) (K + 1) ^ {2} + (\theta^ {2} - 1) (K + 1) s + (\theta - 1) ^ {2} s ^ {2}) ^ {3}} \\ \times \left( \begin{array}{c} 1 2 \theta (\theta - 1) ^ {5} (K + 1) s ^ {5} + 1 2 \theta^ {3} (\theta + 1) ^ {2} (\theta - 1) (K + 1) ^ {5} s \\ + (\theta - 1) ^ {6} s ^ {6} + \theta^ {2} (\theta + 1) (\theta (\theta (\theta + 1 1) - 5) + 1) (K + 1) ^ {6} \\ + 3 (\theta - 1) ^ {4} (\theta + 1) (8 \theta - 1) (K + 1) ^ {2} s ^ {4} \\ + (\theta - 1) ^ {3} (\theta (\theta (7 \theta + 6 0) + 3) - 2) (K + 1) ^ {3} s ^ {3} \\ + 6 (\theta - 1) ^ {2} \theta (\theta (\theta (4 \theta + 3) + 6) - 1) (K + 1) ^ {4} s ^ {2} \end{array} \right), \end{array}
$$

which is positive.

$$
\begin{array}{c} \frac {\partial^ {2} \tilde {\pi} ^ {*}}{\partial s \partial \theta} = (1 + K) \cdot (4 (K - s + 1) ^ {2} (\theta (\theta + 1) (K + 1) ^ {2} \\ \qquad \qquad \qquad + (\theta^ {2} - 1) (K + 1) s + (\theta - 1) ^ {2} s ^ {2}) ^ {3}) ^ {- 1} \\ \qquad \qquad \times \left( \begin{array}{c} 4 \theta^ {3} (\theta + 1) (K + 1) ^ {5} - (\theta - 1) ^ {3} (\theta + 1 1) (K + 1) s ^ {4} \\ + 7 (\theta - 1) ^ {3} (5 \theta + 1) (K + 1) ^ {2} s ^ {3} - 4 (\theta - 1) ^ {4} s ^ {5} \\ + (\theta - 1) \theta (\theta (7 \theta + 3 2) - 3 1) (K + 1) ^ {3} s ^ {2} \\ - 2 \theta (\theta (\theta (7 \theta - 1 7) + 9) + 1) (K + 1) ^ {4} s \end{array} \right), \end{array}
$$

which is positive. <sup></sup>

Proof of Proposition 9. For vintage depreciation information goods and under leasing, as illustrated by Figure 3, the vendor does not sufer from consumers’ waiting behaviors because consumers do not need to take the future price $r _ { 2 }$ into consideration. Consequently, conditional pricing does not impact period 1 adoption, and committing $r _ { d } < r _ { 2 }$ can only decreases vendor profit. <sup></sup>

Proof of Proposition 10. This proof is similar to the proof of Lemma 2. We provide only a sketch here. Period 2 optimal solutions include five diferent regions:√

Region 1: $\theta < \frac { 1 } { 2 } , v _ { 1 } \in [ 0 , ( 2 \theta - \sqrt { \theta } ) / ( 4 \theta - 1 ) )$ , and $\pi _ { 2 } ^ { * } = \theta / 4$ Region $\begin{array} { r } { 2 : \ \theta < \frac { 1 } { 2 } , \ v _ { 1 } \in [ ( 2 \theta - \sqrt { \theta } ) / ( 4 \theta - 1 ) , 1 ] . } \end{array}$ , and $\pi _ { 2 } ^ { * } =$ $\theta v _ { 1 } ( \bar { 1 - v _ { 1 } } ) + v _ { 1 } ^ { 2 } / 4 .$

Region $\begin{array} { r } { 3 \colon \theta \geq \frac { 1 } { 2 } , v _ { 1 } \in [ 0 , ( 1 - \sqrt { 1 - \theta } ) / ( 2 \theta ) ) . } \end{array}$ , and $\pi _ { 2 } ^ { * } = \theta / 4$ Region 4: $\theta \geq \frac { 1 } { 2 } , v _ { 1 } \in [ ( 1 - \sqrt { 1 - \theta } ) / ( 2 \theta ) , 1 / ( 2 \theta ) )$ , and $\pi _ { 2 } ^ { * } =$ $\theta v _ { 1 } ( 1 - \theta v _ { 1 } )$

Region $\begin{array} { r } { \bar { \mathfrak { d } } \colon \theta \geq \frac { 1 } { 2 } , v _ { 1 } \in [ 1 / ( 2 \theta ) , 1 ] , } \end{array}$ and $\pi _ { 2 } ^ { * } = 1 / 4$

In each region, we solve for $v _ { 1 } ^ { * }$ that satisfies the REE criteria.

When $\theta \in [ 0 , \frac { 1 } { \upsilon } )$ , the optimal pricing strategies are $r _ { 1 } ^ { * } =$ $r _ { \gamma } ^ { * } = ( 1 + 2 \theta ) / ( 2 ( \bar { 1 ^ { \cdot } } + 4 \theta ) )$ and $r _ { d } ^ { * } = \theta / 2$ . The optimal profit is $( \bar { 1 } + 2 \theta ) ^ { 2 } / ( 4 ( 1 + 4 \theta ) )$ , which is the same as the selling vendor’s profit. Thus, conditional pricing is weakly dominated by selling. When $\theta \in [ { \textstyle { \frac { 1 } { 2 } } } , 1 ] .$ , the optimal pricing strategies are $r _ { 1 } ^ { * } =$ $r _ { 2 } ^ { * } = \theta / ( 1 + \theta )$ and $r _ { d } ^ { * } \to r _ { 2 } ^ { * }$ . Thus, conditional pricing (committing $r _ { d } < r _ { 2 } )$ is suboptimal and is dominated by leasing. <sup></sup>

Proof of Proposition 11. We start by proving Lemma A.2.

Lemma A.2. In a two-period setting, under either vintage or individual depreciation, period 1 only consumers and period 2 only consumers can never coexist.

We prove Lemma $\mathrm { A } . 2$ by contradiction. Assume period 1 only consumers and period 2 only consumers can coexist.

Case 1: Individual depreciation. Without loss of generality, assume that there exists a type v consumer who chooses the leasing model only in period 1, i.e., $U _ { v } ^ { L , B } ( D O ) > U _ { v } ^ { L , B } ( O D )$ This leads to $v - r _ { 1 } > v - r _ { 2 } \Rightarrow r _ { 2 } > r _ { 1 }$ . By assumption, there exists another type $v ^ { \prime }$ consumer, who also chooses the leasing model but adopts only in period 2, i.e., $U _ { v ^ { \prime } } ^ { L , B } ( O D ) >$ $U _ { \tau ^ { \prime } } ^ { \breve { L } , B } ( D O )$ . This leads to $v ^ { \prime } - r _ { 1 } < v ^ { \prime } - r _ { 2 } \Rightarrow r _ { 2 } < r _ { 1 } ,$ a contradiction.

Case 2: Vintage depreciation. Without loss of generality, assume that there exists a type v consumer who chooses leasing and adopts only in period 1. This gives

$$
\begin{array}{l} U _ {v} ^ {L, A} (D O) > U _ {v} ^ {L, A} (O D) \\ \quad \Rightarrow v - r _ {1} > \theta v - r _ {2} \Rightarrow r _ {1} - r _ {2} <   (1 - \theta) v; \\ U _ {v} ^ {L, A} (D O) > U _ {v} ^ {L, A} (D D) \\ \quad \Rightarrow v - r _ {1} > v - r _ {1} + \theta v - r _ {2} \Rightarrow r _ {2} > \theta v. \end{array}
$$

By assumption there exists another type v consumer who chooses leasing and adopts only in period 2. This gives

$$
\begin{array}{r l} & U _ {v ^ {\prime}} ^ {L, A} (O D) > U _ {v ^ {\prime}} ^ {L, A} (D O) \\ & \quad \Rightarrow \theta v ^ {\prime} - r _ {2} > v ^ {\prime} - r _ {1} \Rightarrow r _ {1} - r _ {2} > (1 - \theta) v; \\ & U _ {v ^ {\prime}} ^ {L, A} (O D) > U _ {v ^ {\prime}} ^ {L, A} (O O) \Rightarrow \theta v ^ {\prime} - r _ {2} > 0 \Rightarrow r _ {2} <   \theta v ^ {\prime}. \end{array}
$$

Combining the above four conditions, we have

$$
\begin{array}{r l} (1 - \theta) v ^ {\prime} <   r _ {1} - r _ {2} <   (1 - \theta) v & \Rightarrow v > v ^ {\prime}; \\ \theta v <   r _ {2} <   \theta v ^ {\prime} & \Rightarrow v ^ {\prime} > v, \end{array}
$$

a contradiction.

We now prove Proposition 11 by contradiction. Assume that the hybrid model is optimal. This requires that both the selling model and the leasing model are adopted simultaneously, by diferent market segments.

In a two-period setting, selling and leasing are identical for new adopters in period 2. This means that if selling and leasing are adopted simultaneously, there must be period 1 adopters who choose the leasing model. Otherwise, the hybrid model is replaced by the selling model, which is not optimal. This in turn gives rise to the following two cases:

Case 1. All period 1 adopters who choose the leasing model continue to lease in period 2, which implies that leasing in both periods is favored over buying in period 1, i.e., $r _ { 1 } + r _ { 2 } < p _ { 1 }$ . In turn, this means that no consumer will buy in period 1. Then the hybrid model can be fully replaced by the leasing model, which is not optimal, a contradiction.

Case 2. Not all period 1 adopters who choose the leasing model will continue to lease in period 2; i.e., there are some consumers who adopt only in period 1 via leasing. According to Lemma A.2, this means that there are no consumers who will adopt only in period 2. Again, the hybrid model is replaced by the leasing model, which is not optimal, a contradiction. <sup></sup>

## Endnotes

<sup>1</sup> In this literature, a few papers address quality decay of physical products, such as Bond and Samuelson (1984) and Suslow (1986). However, as pointed out by Desai and Purohit (1998), they do not diferentiate existing adopters from potential new adopters.

<sup>2</sup> This assumption ensures that network efects will not be so strong that they dominate all other factors. We thank the review team for this suggestion.

<sup>3</sup> For example, Desai and Purohit (1998) do not study network efects, as they focus on product-side vintage depreciation for physical goods rather than consumer valuation depreciation for information goods as we do. While Bensaid and Lesne (1996) and Mason (2000) consider network efects, neither studies leasing, therefore, their papers are unable to compare selling versus leasing, one key focus of this paper.

<sup>4</sup> If we assume a comparable setup of a two-period model, a fixed leasing fee over time, and no production versioning (e.g., no product upgrading over time), our findings in Proposition 11 are consistent with prior literature (i.e., Zhang and Seidmann 2010).

<sup>5</sup> See https://products.ofice.com/en-US/?omkt<sup></sup>en-US.

<sup>6</sup> See http://www.wolfram.com/mathematica-home-edition/.

<sup>7</sup> As of August 2016, 29.2% of e-book titles in the Amazon Kindle Store (1,372,503 out of 4,703,075 titles) are eligible for Kindle Unlimited. Some categories with strong individual depreciation, such as nonfiction novels, are not included in the Kindle Unlimited program.

## References

Bagnoli M, Salant SW, Swierzbinski JE (1989) Durable-goods monopoly with discrete demand. J. Political Econom. 97(6): 1459–1478.

Bensaid B (1996) Dynamic monopoly pricing with network externalities. Internat. J. Indust. Organ. 14(6):837–855.

Bensaid B, Lesne JP (1996) Dynamic monopoly pricing with network externalities. Internat. J. Indust. Organ. 14(6):837–855.

Bhargava HK, Chen RR (2012) The benefit of information asymmetry: When to sell to informed customers? Decision Support Systems 53(3):345–356.

Bhargava HK, Sundaresan S (2004) Computing as utility: Managing availability, commitment, and pricing through contingent bid auctions. J. Management Inform. Systems 21(2):201–227.

Bhaskaran SR, Gilbert SM (2005) Selling and leasing strategies for durable goods with complementary products. Management Sci. 51(8):1278–1290.

Bhaskaran SR, Gilbert SM (2009) Implications of channel structure for leasing or selling durable goods. Marketing Sci. 28(5): 918–934.

Bond EW, Samuelson L (1984) Durable good monopolies with rational expectations and replacement sales. RAND J. Econom. 15(3):336–345.

Bulow JI (1982) Durable goods monopolists. J. Political Econom. 90(2):314–332.

Chien HK, Chu CYC (2008) Sale or lease? Durable-goods monopoly with network efects. Marketing Sci. 27(6):1012–1019.

Choudhary V (2007) Software as a service: Implications for investment in software development. Sprague RH Jr, ed. Proc. 40th Hawaii Internat. Conf. System Sci. (IEEE Computer Society, Washington, DC).

Coase RH (1972) Durability and monopoly. J. Law Econom. 15(1): 143–149.

Conlisk JE, Gerstner E, Sobel J (1984) Cyclic pricing by a durable goods monopolist. Quart. J. Econom. 99(3):489–505.

Conner KR (1995) Obtaining strategic advantage from being imitated: When can encouraging “clones” pay? Management Sci. 41(2):209–225.

Desai P, Purohit D (1998) Leasing and selling: Optimal marketing strategies for a durable goods firm. Management Sci. 44(11): S19–S34.

Farrell J, Saloner G (1986) Installed base and compatibility: Innovation, product preannouncements, and predation. Amer. Econom. Rev. 76(5):940–955.

Fudenberg D, Tirole J (1991) Game Theory (MIT Press, Cambridge, MA).

Gul F, Sonnenschein HF, Wilson R (1986) Foundations of dynamic monopoly and the Coase conjecture. J. Econom. Theory 39(1): 155–190.

Hu JY (2005) Essays on Internet markets and information goods. Unpublished doctoral thesis, Massachusetts Institute of Technology, Cambridge.

Huang KW, Sundararajan A (2005) Pricing models for on-demand computing. Working paper, Stern School of Business, New York University, New York.

Ishihara M, Ching A (2012) Dynamic demand for new and used durable goods without physical depreciation: The case of Japanese video games. Working paper, Rotman School of Management, University of Toronto, Toronto.

Jain S, Kannan PK (2002) Pricing of information products on online servers: issues, models, and analysis. Management Sci. 48(9):1123–1142.

Jing B (2007) Network externalities and market segmentation in a monopoly. Econom. Lett. 95(1):7–13.

Johnson JP, Myatt DP (2003) Multiproduct quality competition: Fighting brands and product line pruning. Amer. Econom. Rev. 93(3):748–774.

Johnson JP, Myatt DP (2006) On the simple economics of advertising, marketing, and product design. Amer. Econom. Rev. 96(3): 756–784.

Katz ML, Shapiro C (1985) Network externalities, competition, and compatibility. Amer. Econom. Rev. 75(3):424–440.

Katz ML, Shapiro C (1986) Technology adoption in the presence of network externalities. J. Political Econom. 94(4):822–841.

Katz ML, Shapiro C (1992) Product introduction with network externalities. J. Indust. Econom. 40(1):55–83.

Mason R (2000) Network externalities and the Coase conjecture. Eur. Econom. Rev. 44(10):1981–1992.

Shapiro C, Varian HR (1999) Information Rules: A Strategic Guide to the Network Economy (Harvard Business Press, Boston).

Shiller BR (2013) Digital distribution and the prohibition of resale markets for information goods. Quant. Marketing Econom. 11(4): 403–435.

Stokey NL (1979) Intertemporal price discrimination. Quart. J. Econom. 93(3):355–371.

Suslow VY (1986) Commitment and monopoly pricing in durable goods models. Internat. J. Indust. Organ. 4(4):451–460.

Swan PL (1970) Durability of consumption goods. Amer. Econom. Rev. 60(5):884–894.

Zhang J, Seidmann A (2010) Perpetual versus subscription licensing under quality uncertainty and network externality efects. J. Management Inform. Systems 27(1):39–68.
