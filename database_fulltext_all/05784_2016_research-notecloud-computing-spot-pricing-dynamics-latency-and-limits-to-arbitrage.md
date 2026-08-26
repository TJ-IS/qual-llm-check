---
otero_id: 5784
otero_key: "BBJB2KE8"
title: "Research Note—Cloud Computing Spot Pricing Dynamics: Latency and Limits to Arbitrage"
authors: "Hsing Kenneth Cheng; Zhi Li; Andy Naranjo"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0608"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [132.239.1.231] On: 14 March 2016, At: 04:44 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/BBJB2KE8/fulltext/images/e5c3e3f84b33f3a919da61654090e4d5e0275c1237bb527c1691d9f345d46d67.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Cloud Computing Spot Pricing Dynamics: Latency and Limits to Arbitrage

Hsing Kenneth Cheng, Zhi Li, Andy Naranjo

To cite this article:

Hsing Kenneth Cheng, Zhi Li, Andy Naranjo (2016) Research Note—Cloud Computing Spot Pricing Dynamics: Latency and Limits to Arbitrage. Information Systems Research

Published online in Articles in Advance 18 Feb 2016

http://dx.doi.org/10.1287/isre.2015.0608

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/BBJB2KE8/fulltext/images/ceb37d1454df567a791855167adafcf21e43d4d9d6741666be5aba3ae06bf632.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Cloud Computing Spot Pricing Dynamics: Latency and Limits to Arbitrage

Hsing Kenneth Cheng

Hough Graduate School of Business, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611, hkcheng@ufl.edu

Zhi Li

Technology, Operation and Information Management Division, Babson College, Babson Park, Massachusetts 02457, zli@babson.edu

Andy Naranjo

Hough Graduate School of Business, Warrington College of Business Administration, University of Florida, Gainesville, Florida 32611, andy.naranjo@warrington.ufl.edu

his study examines cloud computing spot pricing dynamics and the influence of latency on those pricing Tdynamics. Using the Amazon Elastic Compute Cloud U.S. East and West market spot instance pricing and latency intraday data from April 9, 2010, to May 22, 2011, we find considerable time variation in spot instance prices, and prices are often persistently higher in the West. Bivariate vector autoregressive model results show that within-market autoregressive pricing effects are larger than across-market effects. We also document that over 70% of the relative price discovery occurs in the East market. Our regression results further show that East–West latency differentials have a significantly positive effect on East–West pricing differentials. Latency creates a dynamic pricing wedge that widens or narrows conditional on the latency differentials. Using an error correction model, the speed of adjustment from long-run pricing convergence errors causes the short-run price differential to narrow, but the adjustment does not completely offset the price differential.

Keywords: cloud computing; spot pricing; pricing dynamics; latency; arbitrage

History: Rahul Telang, Senior Editor; Subodha Kumar, Associate Editor. This paper was received on October 13, 2013, and was with the authors 9 months for 3 revisions. Published online in Articles in Advance.

## 1. Introduction

Cloud computing has garnered significant attention as an increasingly important computing environment that will continue to grow over time. According to conservative estimates by Ried and Kisker (2011), the global cloud computing market will grow from \$40.7 billion in 2011 to \$241 billion in 2020. The cloud has various forms, including SaaS (software as a service), PaaS (platform as a service), and IaaS (infrastructure as a service). It has succinctly been defined as an information technology (IT) service model where computing services (both hardware and software) are delivered on demand to customers over a network in a self-service fashion, independent of device and location (Cheshire 1996).<sup>1</sup> A majority of firms now use some form of cloud computing for IT (Cohen 2013).

Cloud computing providers offer basic computing and storage resources at relatively low prices. Amazon’s Elastic Compute Cloud (Amazon EC2) is the major cloud service provider; in fact, it has been called the Coke of cloud computing in terms of market share and “there isn’t yet a Pepsi.”<sup>2</sup> The price of an EC2 instance is based on the service center where the instance is running. Customers can purchase EC2 instances through on-demand instances, reserved instances, and spot instances.<sup>3</sup> Spot instances are a relatively new method as of December 2009 to both purchase and consume Amazon EC2 instances. They allow customers to bid on unused Amazon EC2 capacity and run those instances for as long as their bid exceeds the current spot price. Customers whose bids exceed the current spot price gain access to the available spot instances. Historically, customers using spot instances have received significant price discounts beyond ondemand prices for no commitments past one hour. The Amazon EC2 spot market uses the Vickrey-style auction, where customers submit sealed bids, and the provider computes a market clearing price (Mazzucco and Dumas 2011). All winning customers pay the same price, which is the value of the lowest winning bid. Research indicates that this mechanism is a truthful auction given that the supply level can be adjusted ex post (Zhang et al. 2011).<sup>4</sup>

However, a conundrum arises when one examines Amazon EC2 spot prices, because a visual inspection of the spot prices reveals that Amazon western EC2 center spot prices are consistently and significantly higher than those of the eastern center across Amazon’s computing platforms. Since cloud computing services from the West and East centers for the same computing platform are identical goods, the consistently positive price differentials between the West and East centers presents a seemingly clear arbitrage opportunity for cloud computing customers and raises a fundamental question about the market efficiency of cloud computing.

The consistently positive spot price differentials cannot be systematically attributed to either the supply or demand of Amazon EC2 cloud computing services; that is, if the sources for the observed pricing differentials were in greater supply (lower supply) in the eastern (western) center or greater demand (lower demand) in the western (eastern) center, Amazon EC2 customers could easily alter their spot bids from a dropdown menu to select the center with the cheaper persistent pricing. Knowing that the cloud computing service is cheaper at the Amazon eastern center, customers could easily switch their bids to the eastern center. This, in turn, would create more demand at the eastern center, which then would drive up the spot prices on the eastern center to reach the same level as the western center over time. This equivalent pricing equilibrium, however, has not materialized as the price differentials are persistent.

A fundamental research question concerning cloud computing market efficiency is, therefore, what is the source of the pricing differentials, and does it manifest itself as a pricing wedge that limits arbitrage? Furthermore, given that Amazon EC2 customers only observe spot price information and do not know the supply nor the demand of the spot market, what can they glean from the pricing dynamics of the cloud computing spot market, and how might they better react to that information?

We use various econometric modeling approaches to carefully address the aforementioned fundamental questions. We employ vector autoregressive (VAR) models to measure and test spot instance pricing dynamics both within and across the Amazon EC2 East and West regions. To measure the price discovery for Amazon EC2 cloud computing spot instances across the East and West regions, we employ the two most widely accepted price discovery measures developed by Hasbrouck (1995) and Gonzalo and Granger (1995). Finally, we use both regression procedures and an error correction model (ECM) to measure and test the effect of latency on the documented East and West pricing differential dynamics.

For the most fundamental question on cloud computing market efficiency, we show that network latency, defined as the total elapsed time from the time a request is sent via the Internet to the time a response is received (O3b Networks 2008), is the key factor contributing to the persistent positive spot price differentials between the Amazon EC2 West and East regions. Our study is the first to provide convincing evidence to explain this intriguing and perplexing cloud computing market efficiency issue. Brynjolfsson and Smith (2000) find that branding, awareness, and trust are important sources of heterogeneity in pricing among Internet retailers, whereas Brynjolfsson et al. (2009) document the importance of geography on the competition between the Internet channel and local stores.<sup>5</sup> We further show that even with the same cloud computing provider and computing platform (i.e., same provider and same good), price heterogeneity still exists due to latency differentials across markets.

Arguably, why should seconds of delay created by network latency matter? In one of the earliest studies on the response time effect on user behavior, Miller (1968) showed that 10 seconds is the threshold for user attention. However, this user attention threshold has reduced to 2 seconds in today’s e-commerce environment because consumers have become impatient when Web pages take longer than 2 seconds to load (Forrester Consulting 2009).<sup>6</sup> These user attention thresholds are important because a subpar Web experience results in lost revenue and unfavorable customer perceptions of the company. For example, an increase of 100 ms in response time can result in a 1% drop of sales at Amazon (Mazzucco 2010), and Google’s traffic will drop by 20% for a half-second increase in returning search results (Mayer 2009).

Latency is a key issue not only for firms offering products and services to consumers over the Internet but also for corporations considering the adoption of cloud computing. In fact, it has been dubbed the “Achilles heel of cloud computing” (Minnear 2011). As a further example of the management relevancy and larger contribution of our study, the chief cloud architect for Netflix, Adrian Cockcroft, recently stated in an interview (Babcock 2013) that “[m]astering these business tradeoffs of weighing the cost and latency penalties, when they exist, against your business goals is one of the fundamental challenges of cloud computing.” Cockcroft used a rough equation to formulate the trade-off: “How many dollars should you spend to reduce customer latencies by 50% if that increases your conversion rate by 10%?” However, there is a scarcity of research examining the impact of latency on various aspects of cloud computing implementation, including no research that we are aware of that examines the effects of latency on pricing dynamics both within and across markets.

We find that across operating system (OS) platforms and spot instance types, there is a considerable time variation in the pricing dynamics. We also find that prices in the West are often persistently greater than prices in the East over our sample period. Our bivariate VAR model results suggest that there are significant dynamic pricing relations both within and across the East and West markets. The within-market effect is larger than the across-market effect, but there are also significantly pronounced across-market pricing effects. Using both Hasbrouck’s (1995) and Gonzalo and Granger’s (1995) price discovery methodologies, we find that over 70% of the relative price discovery occurs in the East market.

What explains these pricing dynamic differentials across the East and West markets? We find that both the East and West latency differentials have a significantly positive effect on the pricing differential, suggesting that larger (smaller) latency effects result in larger (smaller) pricing differentials; that is, latency creates a dynamic pricing wedge, similar to a varying transaction cost, that widens or narrows conditional on the latency differentials. From the ECM results, we also find that the speed of adjustment from long-run pricing convergence errors causes the short-run price differential to narrow, but the adjustment is only partial.

The rest of this paper is organized as follows. Section 2 provides our hypothesis development and empirical testing framework, whereas $\ S \hat { 3 }$ provides information on our data and some descriptive statistics. Section 4 provides the core of our results starting with a VAR model of the dynamic within- and across-market pricing effects, to measuring where price discovery is occurring and ending with using both regression procedures and an error correction model to explain pricing differential effects. Section 5 provides a discussion of the managerial implications of our study, whereas §6 provides some concluding remarks.

## 2. Hypothesis Development and Empirical Testing Framework

## 2.1. Hypothesis Development

Underlying our theoretical and empirical motivation is the well-established economic proposition regarding the law of one price (LOP). In a nutshell, the LOP states that identical goods or securities should sell for identical prices, accounting for consumer’s transport (transaction) costs. The LOP is the basic building block of most economic theorizing. The logic of why it should hold is simple: if the same good or asset is selling for two different prices simultaneously, then consumers will simply buy in the cheaper market, resulting in the price rising in the cheaper market or, alternatively, in the higher-priced market closing. Price differences are both the necessary and sufficient statistic to test the LOP. The LOP is either violated or not violated, and if so, the follow-on question is, what explains the violation? It is a very important question that addresses market efficiency and the efficient allocation of goods, capital, and resources. In many ways, this fundamental question lies at the heart of a market-based economy.

Consider a company selling the same product in two markets, W and E. Suppose that the price for this product in W $( P _ { w } )$ is more than its price in E $( P _ { e } )$ such that $P _ { w } > P _ { e }$

Given $P _ { w } > P _ { e } ,$ a profit-seeking individual (an arbitrager) in a competitive market setting could buy in

E and sell in W, buying in the low price market and reselling profitably in the higher priced market without sharing profits with the original firm. This strategy is profitable as long as $P _ { w } - P _ { e } - T > 0 .$ , where T is the total transaction cost that includes transportation costs. This two-sided arbitrage scenario is common for physical goods such as commodities as well as for financial assets, where arbitragers buy low and sell high until prices equilibrate across markets after accounting for total transaction costs. In an integrated and efficient competitive market, the price convergence will occur rapidly. Note that arbitrage stops becoming a significant price equating force once $P _ { w } - P _ { e } - T \leq 0 \ \mathrm { ( i . e . } ,$ , the no arbitrage condition). If $T = 0 , P _ { w } = P _ { e }$ is a sufficient no arbitrage condition. This price equilibrating condition could also occur through consumer implementation of only one-side of the arbitrage condition (i.e., buying in the low priced market without also selling in the high priced market); that is, all else equal, if consumers simply purchased in the cheaper priced market instead of the higher priced market, prices would rise in the cheaper market or, alternatively, the prices would fall in the higher priced market—resulting in the prices being equilibrated but for total transactions costs.

Consider instead digital goods such as cloud computing. Could a user take advantage of price differentials between, for instance, Amazon’s EC2 West and East regions? A common assumption is that moving data over the Internet is virtually costless $( \mathrm { i . e . , } T = \bar { 0 } )$ . We argue that this virtually costless assumption is incorrect, and instead $T \neq 0$ due to latency; that is, there are latency effects in data traveling from W and E such that $\dot { T } > 0$ . Since firms and other customers bid on their pricing conditional on their firm’s exposure to latency effects, this latency allows $P _ { w } - P _ { e } > 0 ,$ , and yet ${ \cal P } _ { w } ^ { \mathrm { ~ ~ } } - { \cal P } _ { e } - { \cal T } \le 0$ . We formally test the following hypothesis:

Hypothesis 1. $\delta ( P _ { w } - P _ { e } ) / \delta T > 0 .$ . The pricing differential between Amazon’s EC2 West and East spot pricing widens as West–East latency-related transaction costs rise.

We hypothesize that $T > 0$ due to latency and test this hypothesis in a conditional framework to show that $E [ ( \bar { P } _ { w } - P _ { e } ) | T , \Theta ] \neq 0 .$ , where ä represents a vector of explicit and implicit controls such as within and between market differences, server and platform types, and event indicators.

Consistent with the adage “time is money,” we also provide evidence on the following corollary C : Firms respond to latency effects through their willingness to pay higher spot prices and locating facilities near Internet and exchange hubs to reduce their latency related transactions costs. From a managerial perspective, bidding on the relatively lower priced cloud computing location is optimal if latency is not an important customer concern. However, if latency exposure is an important concern, then the firm’s optimal cloud computing location selection should factor in pricing-latency effects—in terms of both cloud bidding location and potentially longer-term firm operational computing location choices.

## 2.2. Basic Empirical Testing Framework

We employ a two-part empirical framework to test our hypothesis that latency affects cloud computing pricing across markets. In the first part, we establish and test the relation between Amazon EC2 East and West spot instance pricing dynamics and price discovery across these markets. In the second part, we measure and test the extent to which latency and other factors affect our documented pricing differential dynamics from the first part. Although figures and descriptive statistics are useful in providing some preliminary evidence on pricing dynamics within and across Amazon EC2 spot instance markets, they are incomplete because they are unable to directly measure and test the pricing dynamics and do not control for other factors that influence those pricing dynamics. In our analysis, we use several standard time series econometric procedures to both examine the pricing dynamics and test for the effect of latency on the pricing dynamics.

## 3. Data and Descriptive Statistics

## 3.1. Amazon EC2 Spot Instance Pricing Data

We use Amazon EC2 East and West spot instance intraday pricing data over the April 9, 2010, to May 22, 2011, sample period. The begin and end dates of our sample period correspond to the availability of the latency data for our analysis. We collect these incurred transaction interval pricing data from Amazon’s application programming interface (API), which provides these data for five regions, six instance types, six computing capacities, and two OS platforms.<sup>7</sup> In our primary analysis, we use standard m1.xlarge spot instance prices across the East and West U.S. regions for both Windows and Linux/Unix operating platforms.<sup>8</sup> Our results are robust to alternative instance types.<sup>9</sup> The East and West U.S. regions are chosen to keep the pricing analysis within one country, and the time-stamped price data across the two regions are synchronized to a unified Greenwich mean time (GMT). For our analysis, we also convert the incurred transaction interval data (both price and latency) to an hourly frequency by interpolating them in between incurred transaction prices with the most recent incurred transaction price. This allows us to time match both our price series as well as our latency time series. Our results are robust to alternative timing frequencies.

## 3.2. Latency Data

The latency data measured in seconds are collected from CloudSleuth.com over the April 9, 2010, to May 22, 2011, sample period. CloudSleuth records and compares the performance of PaaS and IaaS providers from around the world. The latency data we collected from CloudSleuth.com measure the total elapsed time of a standard benchmark test of downloading two Web pages developed by Gomez Performance Network from each of the 18 Internet backbone nodes in the United States to Amazon’s EC2 East and West centers. The same benchmark test, termed “identical sample application,” commonly used in the industry, is used to measure and collect the latency data to ensure that the latency data will not be impacted by the types of jobs running at the Amazon EC2 centers (e.g., running a long time-consuming job versus running a short job, or different types of jobs from different industry sectors).

Throughout each day at approximately 30 minute to 1 hour intervals, CloudSleuth monitors latency from many backbone nodes. The latency data that we obtain correspond to the measured latency between 18 backbone nodes from cities throughout the United States to Amazon EC2 US-west and US-east. Similar to the spot pricing data, the time-stamped latency data are synchronized to a unified GMT, and we also convert the measured latency interval data to an hourly frequency by interpolating the in-between latency measures with the most recent measured latency. This again enables us to time match both our price series as well as our latency time series.

In our analysis, we use city-level (i.e., 18 nodes) latency data. We also aggregate the city-level latency data into three regions as follows:

$$
\begin{array}{c} \text {East = average(Newark + Atlanta + Boston + NY} \\ \quad + \text {Philadelphia + DC + Reston);} \end{array}
$$

$$
\begin{array}{c} \text {West = average(San Jose + Mesa + Denver + LA} \\ \quad + \text {San Diego + Seattle);} \end{array}
$$

$$
\begin{array}{c} \text { Central } = \text { average } (\text { Dallas } + \text { Houston } + \text { Kansas   City } \\ \quad + \text { St.   Louis } + \text { Chicago }). \end{array}
$$

Since we hypothesize that the spot instance pricing differentials across the East and West markets are affected by the latency differentials across these markets, we create the following latency difference variables (defined at each time t):

DL\_City<sub>it</sub>: Average latency to Amazon West EC2 center at city i minus average latency to Amazon East EC2 center at city i

L<sup>EastToEast</sup><sub>t</sub> : Average latency from East region backbone nodes to Amazon East EC2 center

L<sup>EastToWest</sup>: Average latency from East region backbone nodes to Amazon West EC2 center

L<sup>WestToEast</sup><sub>t</sub> : Average latency from West region backbone nodes to Amazon East EC2 center

L<sup>WestToWest</sup><sub>t</sub> : Average latency from West region backbone nodes to Amazon West EC2 center

$L _ { t } ^ { C e n t r a l T o E a s t } \colon$ Average latency from Central region backbone nodes to Amazon East EC2 center

L<sup>CentralToWest</sup>: Average latency from Central region backbone nodes to Amazon West EC2 center

DL<sup>East</sup>: L<sup>EastToWest</sup> − L<sup>EastToEast</sup>

DL<sup>West</sup>: L<sup>WestToEast</sup> − L<sup>WestToWest</sup>

DL<sup>Central</sup>: L<sup>CentralToWest</sup> − L<sup>CentralToEast</sup>

## 3.3. Control Indicator Variables

As additional control variables, we create a series of indicator variables corresponding to a series of Amazon

Table 1 Summary Statistics

<table><tr><td rowspan="2"></td><td colspan="2">Windows</td><td colspan="2">Linux/Unix</td></tr><tr><td> $P_{East}$ </td><td> $P_{West}$ </td><td> $P_{East}$ </td><td> $P_{West}$ </td></tr><tr><td colspan="5">Panel A: Spot prices: m1.xlarge at incurred transaction interval</td></tr><tr><td>Obs.</td><td>6,407</td><td>5,440</td><td>6,384</td><td>5,343</td></tr><tr><td>Mean</td><td>0.400</td><td>0.532</td><td>0.246</td><td>0.319</td></tr><tr><td>Median</td><td>0.402</td><td>0.529</td><td>0.242</td><td>0.318</td></tr><tr><td>Std. dev.</td><td>0.016</td><td>0.017</td><td>0.056</td><td>0.010</td></tr><tr><td>Max</td><td>0.960</td><td>0.560</td><td>1.000</td><td>0.336</td></tr><tr><td>Min</td><td>0.380</td><td>0.506</td><td>0.228</td><td>0.304</td></tr><tr><td colspan="5">Panel B: Spot prices for m1.xlarge at 60 minute intervals</td></tr><tr><td>Obs.</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td></tr><tr><td>Mean</td><td>0.400</td><td>0.532</td><td>0.245</td><td>0.320</td></tr><tr><td>Median</td><td>0.401</td><td>0.530</td><td>0.241</td><td>0.319</td></tr><tr><td>Std. dev.</td><td>0.014</td><td>0.016</td><td>0.045</td><td>0.010</td></tr><tr><td>Max</td><td>0.960</td><td>0.560</td><td>1.000</td><td>0.336</td></tr><tr><td>Min</td><td>0.380</td><td>0.506</td><td>0.228</td><td>0.304</td></tr><tr><td>Correlation( $P_{East}$ )</td><td>1.00000</td><td>0.00279(0.7826)</td><td>1.00000</td><td>-0.00492(0.6263)</td></tr><tr><td>Correlation( $P_{West}$ )</td><td>0.00279(0.7826)</td><td>1.00000</td><td>-0.00492(0.6263)</td><td>1.00000</td></tr></table>

Notes. This table provides summary statistics for the Amazon EC2 (standard) m1.xlarge intraday spot instance price data on Windows and Linux/Unix platforms from April 9, 2010, to May 22, 2011. P <sup>East</sup> corresponds to the intraday spot prices at the US-east region, whereas P <sup>West</sup> corresponds to the spot prices at the US-west region. Both price series are measured in dollars per hour and are winsorized at the 1% level to address potential outlier issues. The mean, median, standard deviation, max, min, and correlation matrix are given for each series. Panel A provides descriptive statistics on the prices at their incurred transactions, whereas Panel B provides descriptive statistics on spot prices at 60 minute intervals.

EC2 events that might influence the spot instance pricing dynamics. In particular, we create the following indicator variables that take on a value of one at their begin event dates and zero otherwise:

Micro: Micro instances (announced September 9, 2010)

Singapore: Asia Pacific Region (Singapore; announced April 29, 2010)<sup>10</sup>

CC: Cluster compute instances (Linux only; announced July 13, 2010)

Free: Amazon Web Services (AWS) Free Usage Tier (introduced October 21, 2010)

CG: Cluster GPU instances (announced November 15, 2010)

Reduced: m2.2xlarge and m2.4xlarge on-demand reserved price (reduced September 1, 2010)

Tokyo: Asia Pacific Region (Tokyo; announced March 2, 2011)

## 3.4. Descriptive Statistics

Table 1 provides summary statistics for the Amazon EC2 standard xlarge intraday spot instance price data on Windows and Linux/Unix platforms from April 9, 2010, to May 22, 2011. The term $\setminus P ^ { E a s t }$ corresponds to the intraday spot prices at the US-east region, whereas P <sup>West</sup> corresponds to the spot prices at the US-west region. Both are measured in dollars per hour. The mean, median, standard deviation, max, min, and correlation matrix are given for each series. Panel A provides descriptive statistics on the prices at their incurred transactions, whereas Panel B provides descriptive statistics on spot prices at 60 minute intervals.<sup>11</sup>

In Panel A of Table 1, we show that the average and median prices at their incurred transaction intervals across both the Windows and Linux/Unix platforms are higher in the West relative to the East over our sample period. The average price differences are \$0.132 per hour for the Windows platform and \$0.073 per hour for the Linux/Unix platform. Looking across the OS platforms, we also find that the Linux/Unix prices are lower than the Windows platform prices. For the Windows platform, the standard deviation is higher for the West relative to the East at 0.017 versus 0.016. However, there is substantially more price variation using the Linux/Unix platform, and especially so for East prices, where we document standard deviations of 0.056 and 0.010 for the East and West, respectively.

In Panel B of Table 1 we report the spot instance prices for standard xlarge at 60 minute intervals. The

Panel A

Figure 1 (Color online) (Panel A) Weekly Price Differential of m1.xlarge.windows, $P D = P ^ { W e s t } - P ^ { E a s t }$ , and (Panel B) Weekly Price Differential of m1.xlarge.unix $P D = P ^ { \ ' { W e s t } } - P ^ { \ ' { E a s t } }$  
![](/api/attachments/BBJB2KE8/fulltext/images/075a5399da458fea192dda24112b24fec6261fefce757f21b36899119b6e6127.jpg)

Panel B  
![](/api/attachments/BBJB2KE8/fulltext/images/4523dd380c6e370f630fca47389caa5f26fe4805899ab27a21fc6af953c1b0d9.jpg)

mean, median, and standard deviations of the 60 minute interval prices are nearly identical to the incurred level prices, indicating that the distribution of the incurred and 60 minute interval prices are very similar. The 60 minute interval prices also allow us to examine the correlation of the aligned prices. Interestingly, the contemporaneous intraday East and West price correlations across both OS platforms are not different from zero.<sup>12</sup> Our documented East and West pricing differences coupled with their insignificant correlations provides some preliminary unconditional evidence suggesting that there may be some persistence in the pricing differentials across these markets.

To examine the time-varying characteristics of the pricing differentials, we provide a time series plot of the West minus East pricing differentials for the Windows platform in Panel A of Figure 1 and for the Linux/Unix platform in Panel B. Given the high frequency of the data, we plot the pricing differentials at the average weekly level (using daily averages based on the intraday 60 minute interval prices) for depiction purposes. In both panels of Figure 1, we can see that there is indeed persistence in the pricing differential whereby West prices are consistently higher than East prices over time across both OS platforms. Furthermore, the plots show that there is significant time variation in the pricing differentials. These results suggest that there is a dynamic relation in the pricing differentials, which we address in our conditional analysis.

## 4. Results

## 4.1. Measuring and Testing the Dynamic Relations Between Amazon EC2 Spot Instance East and West Prices Using a Bivariate VAR Model

The descriptive statistics and price differential figures suggest that East and West prices vary over time, but this unconditional analysis is incomplete because it is unable to directly measure and test the pricing dynamics and does not control for other factors that influence those pricing dynamics. To examine these pricing dynamics in an appropriate conditional framework, we use a bivariate VAR model to test the price relations within and across the East and West Amazon EC2 spot instance pricing markets.

The VAR framework provides a systematic modeling approach to capture rich conditional dynamics in multiple time series, and these models are among the most widely used to measure and test interdependencies among multiple time series such as our Amazon EC2 spot instance pricing across markets (e.g., Hamilton 1994). VAR models have proven to be especially useful in describing the dynamic behavior of economic and financial time series as well as the prices of assets, commodities, and other goods, often providing superior forecasts to those from elaborate theory-based simultaneous equations models.

In its simplest form, a VAR model is composed of a system of regressions where two or more dependent variables are expressed as linear functions of their own and each other’s lagged values, as well as other potential exogenous control variables. In more technical terms, a vector autoregressive model is the unconstrained reduced form of a dynamic simultaneous equations model. An unrestricted pth-order Gaussian VAR model can be represented as

$$
Y _ {t} = \mu + \Phi_ {1} Y _ {t - 1} + \Phi_ {2} Y _ {t - 2} + \dots + \Phi_ {p} Y _ {t - p} + e _ {t},\tag{1}
$$

where $Y _ { t }$ is a vector of variables; $\mu$ is a $p \times 1$ vector of intercepts; $\Phi _ { 1 } , \Phi _ { 2 } , \ldots , \Phi _ { p }$ are $p \times p$ matrices of parameters with all eigenvalues of ê having moduli less than one so that the VAR model is stationary; and $e _ { t }$ is a vector of uncorrelated structural shocks 6∼ NID401 ì57. A problem arises with the VAR framework if the variables in the system are nonstationary, which we test. To further capture both long- and short-run dynamics and address nonstationarity problems, we also employ error correction models as discussed in §4.2. We obtain maximum likelihood estimates of ê and ì using iterated least squares. The number of lags is chosen based on examination of the Akaike information criteria (AIC), Schwarz Bayesian information criteria (SBIC), and the likelihood ratio selection criteria for various choices of $p .$

In a two-equation framework consisting of only East and West pricing as endogenous variables, the diagonal coefficients of ê represent conditional momentum in East and West pricing (lagged prices affecting current prices, controlling for other within- and across-market lagged pricing effects), whereas the off-diagonal coefficients of ê represent conditional positive feedback and anticipation effects (changes in West prices following changes in East prices and vice versa, controlling for other within- and across-market lagged pricing effects).

Table 2 provides results from the estimation of the bivariate VAR model using the 60 minute interval data and five lags as suggested by the AIC, the SBIC, and the likelihood ratio selection criteria for various lag choices. We report p-values in parentheses for individual coefficient significance. To examine the cumulative effects, we also report the sum of the estimated lagged coefficients and p-values associated with Wald tests of joint significance.

The results in Table 2 show that the autoregressive component within each market is highly significant, but the cross-market effects are largely muted. These results are consistent with our reported low contemporaneous correlations of the East and West prices. In particular, looking at the Windows platform results, we find that prices in the East are significantly related to prior East prices at a largely decreasing rate for up to four hours. At the same time, the East prices are weakly related to West prices—except at the five hour lag where we find a significant effect at the 3% level. Turning to the West prices with the Windows platform, we again find a significant diminishing autoregressive effect of lagged West prices influencing current West prices. However, we do not find evidence of a significant relation between lagged East prices influencing West prices using the Windows platform. Both the individual East and West within- and across-market price effects are also confirmed when we look at their joint significance in the bottom panel. In the joint significance panel, we find strong within-market effects and insignificant across-market effects.

In the right panel of Table 2, we report the bivariate VAR model results between East and West prices using the Linux/Unix OS platform. We again find a significant relation between current and lagged East prices for up to four hours at a largely diminishing rate over time.

Table 2 The Dynamic Relations Between East and West Prices Using a Bivariate VAR Model

<table><tr><td rowspan="2"></td><td colspan="2">Windows</td><td colspan="2">Linux/Unix</td></tr><tr><td> $P_{East}$ </td><td> $P_{West}$ </td><td> $P_{East}$ </td><td> $P_{West}$ </td></tr><tr><td>Constant</td><td>0.319(0.0001)</td><td>0.358(0.0001)</td><td>0.027(0.1093)</td><td>0.211(0.0001)</td></tr><tr><td> $P_{t-1}^{East}$ </td><td>0.110(0.0001)</td><td>-0.004(0.7354)</td><td>0.471(0.0001)</td><td>-0.003(0.264)</td></tr><tr><td> $P_{t-2}^{East}$ </td><td>0.030(0.0028)</td><td>0.004(0.7025)</td><td>0.085(0.0001)</td><td>-0.006(0.0787)</td></tr><tr><td> $P_{t-3}^{East}$ </td><td>0.071(0.0001)</td><td>0.008(0.4685)</td><td>0.180(0.0001)</td><td>0.004(0.2776)</td></tr><tr><td> $P_{t-4}^{East}$ </td><td>-0.023(0.0229)</td><td>-0.010(0.3879)</td><td>0.107(0.0001)</td><td>0.005(0.1288)</td></tr><tr><td> $P_{t-5}^{East}$ </td><td>-0.002(0.8383)</td><td>-0.007(0.5178)</td><td>0.016(0.1195)</td><td>0.001(0.6477)</td></tr><tr><td> $P_{t-1}^{West}$ </td><td>0.001(0.9339)</td><td>0.305(0.0001)</td><td>-0.088(0.0072)</td><td>0.329(0.0001)</td></tr><tr><td> $P_{t-2}^{West}$ </td><td>0.015(0.1254)</td><td>-0.002(0.8861)</td><td>0.036(0.2966)</td><td>-0.009(0.4184)</td></tr><tr><td> $P_{t-3}^{West}$ </td><td>-0.013(0.1868)</td><td>0.042(0.0001)</td><td>-0.044(0.2011)</td><td>0.032(0.0024)</td></tr><tr><td> $P_{t-4}^{West}$ </td><td>-0.012(0.2161)</td><td>-0.028(0.0073)</td><td>0.082(0.0177)</td><td>-0.014(0.1836)</td></tr><tr><td> $P_{t-5}^{West}$ </td><td>0.020(0.0265)</td><td>0.015(0.1349)</td><td>0.036(0.2725)</td><td>0.000(0.9695)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.020</td><td>0.096</td><td>0.109</td><td>0.581</td></tr><tr><td>Obs.</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td></tr></table>

<table><tr><td rowspan="2">Variables</td><td colspan="2">Windows</td><td colspan="2">Linux/Unix</td></tr><tr><td> $P_{East}$ </td><td> $P_{West}$ </td><td> $P_{East}$ </td><td> $P_{West}$ </td></tr><tr><td> $P_{t-1\ to\ t-5}^{East}$ </td><td>0.186(0.000)</td><td>-0.009(0.907)</td><td>0.859(0.000)</td><td>0.001(0.190)</td></tr><tr><td> $P_{t-1\ to\ t-5}^{West}$ </td><td>0.011(0.205)</td><td>0.332(0.000)</td><td>0.022(0.011)</td><td>0.338(0.000)</td></tr></table>

Notes. This table presents results obtained from estimating unrestricted VAR models using Amazon EC2 m1.xlarge spot prices at 60 minute intervals over the April 9, 2010, to May 22, 2011, sample period $( N = 9 , 8 1 6 )$ . An unrestricted pth-order Gaussian VAR model can be represented as  
Y<sub>t</sub> =  + ê<sub>1</sub>Y<sub>t−1</sub> + ê<sub>2</sub>Y<sub>t−2</sub> + · · · + ê<sub>p</sub>Y<sub>t−p</sub> + e<sub>t</sub> 0  
We estimate a bivariate model where the lag length of the vector autoregression is chosen by the AIC, SBIC, and likelihood ratio criterion for various choices of p. We find that five periodic 60 minute lags provide the best fit. To examine the cumulative effects, we also report the sum of the estimated lagged coefficients and p-values associated with Wald tests of joint significance. The p-values are reported in parentheses.

However, unlike the Windows platform results, we find that lagged West prices have a significant influence on East prices within one hour and also at higherlevel lags. The positive and significant joint effect of lagged West prices on East prices in the bottom of the panel suggests an overall positive dynamic relation between West prices and East prices. Similarly, for the West prices under the Linux/Unix platform, we find a significant effect of lagged West prices on current West prices. However, in contrast to the Windows platform results, we find that lagged East prices have a significant influence on West prices, as shown by the two hour lag effect of East prices on current West prices, but their joint effect is insignificant. The fit of the West price market as measured by the adjusted $R ^ { 2 }$ is also significantly higher relative to the other price fits.

Taken together, our bivariate VAR model results suggest that there are significant dynamic pricing relations both within and across the East and West markets. The within-market effect is larger than the across-market effect, but there are also significantly pronounced across-market pricing effects.<sup>13</sup>

## 4.2. Price Discovery in East and West Markets Using Information Shares

The bivariate VAR analysis provides a formal test on the pricing relation dynamics between East and West markets, but those tests do not measure where price discovery occurs across these markets. An important function of markets is price discovery, which is the process through which closely related markets for a good attempt to reach an equilibrium price for that good. Although price discovery may be assumed to be immediate in perfectly competitive markets and frictionless Walrasian models of trading behavior, such assumptions are far from realistic in most markets. Prices of assets and goods evolve in markets, and price discovery involves the incorporation of new information into those prices. When homogeneous or closely linked goods trade in multiple markets, determining where the incorporation of new information (price discovery) occurs is important for market participants in determining market efficiency, pricing of the good or asset, and effective bidding and investment strategies. Measuring the price discovery process across Amazon EC2 East and West spot instance pricing markets is therefore important to understanding the pricing dynamics across these markets.

There are two standard approaches, developed by Hasbrouck (1995) and Gonzalo and Granger (1995), used to examine the relative rates of price discovery for the same good traded across markets.<sup>14</sup> Both approaches assume that an underlying good trading in multiple markets has a common implicit efficient price, and the approaches build on the idea that prices for the same good converge to this common efficient price in the long run, but deviate in the short run because of various market frictions. The market with the largest information shares leads the other markets by reacting to new information first. If the innovations in a market drive the reaction of the other markets, this market is informationally dominant in the price discovery process. Importantly, the results from using Hasbrouck’s (1995) versus Gonzalo and Granger’s (1995) approach differ at times, and we therefore apply both methodologies in our analysis to determine the information shares generated by East and West Amazon EC2 spot instance pricing markets.

In its simplest form, one can think of the information shares as capturing the extent to which pricing relevant information on a good traded in different markets is incorporated into the price; that is, it measures in simple terms the market (location) where the pricing relevant information is being incorporated—which is subsequently incorporated in other markets for that same good. As an illustrating example, a Canadian stock may be cross-listed on both the Toronto Stock Exchange (TSE) and the New York Stock Exchange (NYSE). The new earning information of the stock may affect the stock price on the domestic market (TSE) more than the foreign market (NYSE), whereas the greater competition on the NYSE may lead to a greater contribution of NYSE to the price discovery. The basic idea is that observed prices impound an efficient implicit price that is common to the markets where the good trades. Sources of variation in this price can be attributed to different markets. Therefore, the proportion of the price innovation that can be attributed to each market is that market’s information share—its contribution to price discovery. The information shares provide a useful summary measure of each market’s contribution to the price discovery of the same good traded in different markets.

Both Hasbrouck’s (1995) information share model and Gonzalo and Granger’s (1995) common factor model are based on the following vector error correction (VEC) model:

$$
\Delta P _ {t} = \alpha \beta^ {\prime} P _ {t - 1} + \sum_ {j = 1} ^ {k} \Phi_ {j} \Delta P _ {t - j} + e _ {t},\tag{2}
$$

where  is the error correction term. The error term $e _ { t }$ is a zero-mean vector of serially uncorrelated innovations with a covariance matrix

$$
\Omega = \left( \begin{array}{c c} \sigma_ {1} ^ {2} & \rho \sigma_ {1} \sigma_ {2} \\ \rho \sigma_ {1} \sigma_ {2} & \sigma_ {2} ^ {2} \end{array} \right);
$$

$\sigma _ { 1 } ^ { 2 }$ and $\sigma _ { 2 } ^ { 2 }$ are the variances of $e _ { 1 t }$ and $e _ { 2 t } ,$ and $\rho$ is the correlation coefficient. The first term on the right-hand side of (2), $\alpha \beta ^ { \prime } P _ { t - 1 } ,$ represents the long-run equilibrium of two price time series, whereas the second term on the right-hand side of $\begin{array} { r } { ( 2 ) , \sum _ { j = 1 } ^ { k } \Phi _ { j } \Delta P _ { t - j } , } \end{array}$ describes short-run deviations due to imperfect market conditions.

Hasbrouck (1995) converts the VEC model to obtain a vector moving average representation, which is $\Delta P _ { t } =$ $\Psi ( L ) e _ { t }$ and $\begin{array} { r } { P _ { t } = \Psi ( 1 ) \breve { \sum _ { s = 1 } ^ { t } } \tilde { e _ { s } } + \Psi ^ { * } ( L ) e _ { t } } \end{array}$ . As discussed by Hasbrouck (1995), the long-run impact of a disturbance on each of the prices is intuitively given by ë 415. The row differences of this coefficient matrix are then checked. If the differences are all less than 0.001, we consider the rows of ë 415 to be identical and use only the first row of the coefficient matrix. We use  to denote the first row vector in ë 415, $\psi = ( \psi _ { 1 } , \psi _ { 2 } )$ . Thus, $\begin{array} { r } { P _ { t } = l \psi \sum _ { s = 1 } ^ { t } e _ { s } + \Psi ^ { * } ( L ) e _ { t } } \end{array}$ , where $l = ( 1 , 1 )$ . Hasbrouck (1995) defines $\psi e _ { t }$ as the common factor component of two market prices with variance $\psi \Omega \psi ^ { \prime }$ . When $e _ { 1 t }$ and $e _ { 2 t }$ are uncorrelated, the information share of the jth market is $I S _ { i } = \psi _ { i } ^ { 2 } \sigma _ { i } ^ { 2 } / ( \psi \Omega \psi ^ { \prime } ) , j = 1 , 2$ . When $e _ { 1 t }$ and $e _ { 2 t }$ are correlated, Cholesky factorization is used to remove the error caused by the correlation. In this case, the information share of the jth market is $I S _ { j } = ( [ \psi M ] _ { j } ) ^ { 2 } / ( \psi \Omega \psi ^ { \prime } )$ , where

$$
M = \left( \begin{array}{c c} m _ {1 1}, & 0 \\ m _ {1 2}, & m _ {2 2} \end{array} \right) = \left( \begin{array}{c c} \sigma_ {1}, & 0 \\ \rho \sigma_ {2}, & \sigma_ {2} (1 - \rho^ {2}) ^ {1 / 2} \end{array} \right).
$$

Since the Cholesky factorization ì is sensitive to ordering of the variables, we estimate the upper and lower bounds for each of the markets using both possible order permutations of the East and West Amazon EC2 prices. We use intraday five minute intervals to estimate daily information shares. Our reported results are robust to alternative intraday frequencies.

The first several steps of the Gonzalo and Granger (1995) information model are similar to Hasbrouck’s (1995) information shares approach. We again use intraday five minute intervals to estimate daily market price discovery shares. The East and West prices, $p _ { 1 }$ and $\displaystyle p _ { 2 } ,$ , are then “shocked” (perturbed) with a unit impulse. We estimate a VEC model using 20 lags

$$
\Delta p _ {t} = \alpha \beta^ {\prime} p _ {t - 1} + A _ {1} \Delta p _ {t - 1} + A _ {1} \Delta p _ {t - 1} + \dots + A _ {2 0} \Delta p _ {t - 2 0} + e _ {t},\tag{3}
$$

where $\alpha = ( \alpha _ { 1 } , \alpha _ { 2 } )$ is the speed of price correction when the price in one market deviates from that in the other market. The Gonzalo and Granger (1995) price discovery measures for $p _ { 1 }$ and $p _ { 2 }$ are defined as $\mathrm { \bar { \it G } } G _ { 1 } = - \alpha _ { 2 } / ( \alpha _ { 1 } - \alpha _ { 2 } )$ , and $G G _ { 2 } = \alpha _ { 1 } / ( \alpha _ { 1 } - \alpha _ { 2 } )$

In Table 3, we provide descriptive statistics on the relative price discovery across the East and West markets for both OS platforms. Panel A provides the means, medians, and standard deviations of daily Hasbrouck (1995) information shares over our sample period, whereas Panel B provides the same descriptive statistics for our estimated daily Gonzalo and Granger (1995) information shares.

Looking first at the Hasbrouck (1995) information share results in Panel A of Table 3, we find that a large portion of the relative price discovery occurs in the eastern market relative to the western market. The average daily information shares using the Windows platform prices are 78.8% in the East and 21.2% in the West. By comparison, the Linux/Unix platform results in the right panel also indicate that a significant portion of the information processing occurs in the East market at an average of 72.3% and in the West market at an average of 27.7%. The median results further confirm that price discovery predominantly occurs in the East market relative to the West.

In Panel B of Table $^ { 3 , }$ we provide descriptive statistics on the daily information shares using the Gonzalo and Granger (1995) methodology. Consistent with the Hasbrouck (1995) information share results, we again find that the East market has greater price information processing relative to the West. The average daily price information shares are 70.9% in the East and 29.1% in the West for the Windows OS, and 78.9% and 21.1% for the East and West price information shares, respectively, using the Linux/Unix OS. The median price information share results also suggest that the East price information processing is larger than the West across both OS platforms.

Overall, the information share results using both Hasbrouck (1995) and Gonzalo and Granger (1995) and across both OS platforms suggest that a large portion of the relative price discovery across markets occurs in the East market—it leads the West market by reacting to new information first and is informationally dominant in the price discovery process for Amazon EC2 cloud computing spot instances.

## 4.3. Latency and East vs. West Price Differences

4.3.1. Price Difference Regressions. The earlier reported descriptive statistics and price differential figures suggest that Amazon EC2 East and West spot price instances vary over time, whereas our VAR model results suggest that there are significant within- and across-market pricing dynamic relations. The information shares further suggest that the East market is informationally dominant in the price discovery process relative to the West market. In our hypothesis development, we hypothesize that latency is a key determinant of the pricing differentials over time. To test this hypothesis, we use regression procedures whereby we regress latency differences and various event indicator controls on the differences in prices between the West and East markets.

We first use various ordinary least squares (OLS) regression specifications to test for the influence of latency and other factors on the pricing differentials across East and West Amazon EC2 spot instance pricing over time.<sup>15</sup> In particular, we employ the following

Table 3 Price Discovery in East and West Markets Using Information Shares

<table><tr><td rowspan="2"></td><td colspan="2">Windows</td><td colspan="2">Linux/Unix</td></tr><tr><td> $P_{East}$ </td><td> $P_{West}$ </td><td> $P_{East}$ </td><td> $P_{West}$ </td></tr><tr><td colspan="5">Panel A. Hasbrouck&#x27;s (1995) information shares</td></tr><tr><td>Obs.</td><td>409</td><td>409</td><td>409</td><td>409</td></tr><tr><td>Mean</td><td>0.788</td><td>0.212</td><td>0.723</td><td>0.277</td></tr><tr><td>Median</td><td>0.866</td><td>0.134</td><td>0.838</td><td>0.162</td></tr><tr><td>Std. dev.</td><td>0.222</td><td>0.222</td><td>0.298</td><td>0.298</td></tr><tr><td colspan="5">Panel B. Gonzalo and Granger&#x27;s (1995) information shares</td></tr><tr><td>Obs.</td><td>409</td><td>409</td><td>409</td><td>409</td></tr><tr><td>Mean</td><td>0.709</td><td>0.291</td><td>0.789</td><td>0.211</td></tr><tr><td>Median</td><td>0.597</td><td>0.403</td><td>0.576</td><td>0.424</td></tr><tr><td>Std. dev.</td><td>2.901</td><td>2.901</td><td>4.341</td><td>4.341</td></tr></table>

Notes. This table provides descriptive statistics for daily information shares using intraday five minute pricing time intervals. Panel A provides the means, medians, and standard deviations of Hasbrouck’s (1995) daily information shares

$$
I S _ {j} = \frac {\psi_ {j} ^ {2} \sigma_ {j} ^ {2}}{\psi \Omega \psi^ {\prime}}, \quad \text { when } e _ {1 t} \text { and } e _ {2 t} \text { are   correlated; }
$$

$$
I S _ {j} = \frac {\left([ \psi M ] _ {j}\right) ^ {2}}{\psi \Omega \psi^ {\prime}}, \quad \text { when } e _ {1 t} \text { and } e _ {2 t} \text { are   uncorrelated   and   where }
$$

$$
M = \left( \begin{array}{c c} m _ {1 1}, & 0 \\ m _ {1 2}, & m _ {2 2} \end{array} \right) = \left( \begin{array}{c c} \sigma_ {1}, & 0 \\ \rho \sigma_ {2}, & \sigma_ {2} (1 - \rho^ {2}) ^ {1 / 2} \end{array} \right).
$$

Since the Cholesky factorization ì is sensitive to ordering of the variables, we estimate the upper and lower bounds for each of the markets using both possible order permutations of the East and West Amazon EC2 prices. For each market, we calculate the daily midrange of the upper and lower bounds, and we provide descriptive statistics on these daily Hasbrouck (1995) information shares over our sample.

Panel B provides the means, medians, and standard deviations of the daily information shares using the Gonzalo and Granger (1995 model 

$$
G G _ {1} = \frac {- \alpha_ {2}}{\alpha_ {1} - \alpha_ {2}} \quad \mathrm{and} \quad G G _ {2} = \frac {\alpha_ {1}}{\alpha_ {1} - \alpha_ {2}}.
$$

For each region, we report the statistics for information shares: P <sup>East</sup> corresponds to the information share for the region US-east, whereas $P ^ { W e s t }$ corresponds to the information share for the region US-west. The sample period is from April 9, 2010, to May 22, 2011.

four intraday pricing differential regression models:

$$
P D _ {t} = \alpha_ {0} + \beta_ {1} D L _ {t} ^ {E a s t} + \beta_ {2} D L _ {t} ^ {W e s t} + \beta_ {3} D L _ {t} ^ {C e n t r a l} + \varepsilon_ {t},\tag{4}
$$

$$
P D _ {t} = \alpha_ {0} + \beta_ {1} D L _ {t} ^ {E a s t} + \beta_ {2} D L _ {t} ^ {W e s t} + \beta_ {3} D L _ {t} ^ {C e n t r a l}
$$

$$
+ \sum_ {i = 1} ^ {7} \beta_ {d i} D _ {i} + \varepsilon_ {t},\tag{5}
$$

$$
P D _ {t} = \alpha_ {0} + \sum_ {i = 1} ^ {1 8} \beta_ {i} D L \_ C i t y _ {i t} + \varepsilon_ {t},\tag{6}
$$

$$
P D _ {t} = \alpha_ {0} + \sum_ {i = 1} ^ {1 8} \beta_ {i} D L _ {-} C i t y _ {i t} + \sum_ {i = 1} ^ {7} \beta_ {d i} D _ {i} + \varepsilon_ {t},\tag{7}
$$

where $P D _ { t } = P _ { t } ^ { W e s t } - P _ { t } ^ { E a s t }$ is the pricing differential between West and East Amazon EC2 spot instance pricing at time $t ; D L _ { t } ^ { E a s t } , D L _ { t } ^ { W e s t }$ , and $D L _ { t } ^ { C e n t r a l }$ are corresponding average regional latency differences at time t; $D L \_ C i t y _ { i t }$ are corresponding average city-level latency differences at time $t ;$ and $D _ { i }$ are various event indicator variables $( \mathrm { i . e . , }$ introductions of new Amazon computing instances, locations, and reserved pricing changes). We include all three regions or all 18 cities of the Internet backbone in our base regression estimates and therefore suppress the constant, $\alpha _ { 0 } ,$ to avoid singularity problems—particularly those associated with event indicator variables that span a large portion of the sample period. We also perform reverse causality tests to confirm that latency is driving the pricing differential, and not vice versa, as well as use an instrumental variable (IV) approach to further confirm and identify that latency is causal in affecting the price differentials.

Table 4 provides a description of the variables that we use in the regression analysis. We use both citylevel latency differential measures and regional latency differential measures derived from the city measures. We also include a series of Amazon event indicator explanatory variables. The intraday summary statistics associated with the regional latency differential variables are shown in Table 5 at 60 minute intervals.<sup>16</sup> We find that the East latency differential is on average smaller than the West latency differential. The median results further confirm that the East latency differentials are smaller than the West latency differentials. Both the standard deviations and range suggest that there is some substantial variability in the latency differentials over time. The central latency differentials are the smallest of the regional latency differentials by design in that they are more centrally located between the East and West markets, and hence the latency differential results in a smaller latency difference. Also, as expected, based on the formulation of the East–West latency variables, there is a negative correlation between the East and West latency differentials.

Table 4 Description of Regression Variables Used to Explain the Price Differential

<table><tr><td>PD</td><td> $P^{West} - P^{East}$ </td></tr><tr><td> $DL\_City_{it}$ </td><td>Average latency to Amazon West EC2 center at city i minus average latency to Amazon East EC2 center at city i</td></tr><tr><td> $L_{t}^{EastToEast}$ </td><td>Average latency from East region backbone nodes to Amazon East EC2 center</td></tr><tr><td> $L_{t}^{EastToWest}$ </td><td>Average latency from East region backbone nodes to Amazon West EC2 center</td></tr><tr><td> $L_{t}^{WestToEast}$ </td><td>Average latency from West region backbone nodes to Amazon East EC2 center</td></tr><tr><td> $L_{t}^{WestToWest}$ </td><td>Average latency from West region backbone nodes to Amazon West EC2 center</td></tr><tr><td> $L_{t}^{CentralToEast}$ </td><td>Average latency from Central region backbone nodes to Amazon East EC2 center</td></tr><tr><td> $L_{t}^{CentralToWest}$ </td><td>Average latency from Central region backbone nodes to Amazon West EC2 center</td></tr><tr><td> $DL_{t}^{East}$ </td><td> $L^{EastToWest} - L^{EastToEast}$ </td></tr><tr><td> $DL_{t}^{West}$ </td><td> $L^{WestToEast} - L^{WestToWest}$ </td></tr><tr><td> $DL_{t}^{Central}$ </td><td> $L^{CentralToWest} - L^{CentralToEast}$ </td></tr><tr><td>Micro</td><td>Micro instances announced (September 9, 2010)</td></tr><tr><td>Singapore</td><td>Asia Pacific Region (Singapore) announced (April 29, 2010)</td></tr><tr><td>CC</td><td>Cluster compute instances (Linux/Unix Only) announced (July 13, 2010)</td></tr><tr><td>Free</td><td>AWS Free Usage Tier introduced (October 21, 2010)</td></tr><tr><td>CG</td><td>Cluster GPU instances announced (November 15, 2010)</td></tr><tr><td>Reduced</td><td>m2.2xlarge and m2.4xlarge on-demand reserved price reduced (September 1, 2010)</td></tr><tr><td>Tokyo</td><td>Asia Pacific Region (Tokyo) announced (March 2, 2011)</td></tr></table>

Notes. In our analysis, we use city-level (i.e., 18 node) latency data measured in seconds. We also aggregate the city-level latency data into three regions as follows:  
East = average4Newark + Atlanta + Boston + NY + Philadelphia + DC + Reston53  
West = average4San Jose + Mesa + Denver + LA + San Diego + Seattle5  
Central = average4Dallas + Houston + Kansas City + St. Louis + Chicago50  
This table provides a description of the variables used in the regressions with price differential as the dependent variable.

Table 5 Latency Summary Statistics

<table><tr><td></td><td> $DL^{East}$ </td><td> $DL^{West}$ </td><td> $DL^{Central}$ </td></tr><tr><td>Obs.</td><td>9,816</td><td>9,816</td><td>9,816</td></tr><tr><td>Mean</td><td>4.908</td><td>6.082</td><td>0.765</td></tr><tr><td>Median</td><td>4.796</td><td>5.925</td><td>0.445</td></tr><tr><td>Std. dev.</td><td>2.286</td><td>2.675</td><td>2.970</td></tr><tr><td>Max</td><td>94.739</td><td>47.773</td><td>118.104</td></tr><tr><td>Min</td><td>-21.664</td><td>-66.279</td><td>-23.651</td></tr><tr><td>Correlation $(DL^{East})$ </td><td>1.000</td><td>-0.512(&lt;0.0001)</td><td>0.586(&lt;0.0001)</td></tr><tr><td>Correlation $(DL^{West})$ </td><td>-0.512(&lt;0.0001)</td><td>1.000</td><td>-0.457(0.6263)</td></tr><tr><td>Correlation $(DL^{Central})$ </td><td>0.586(&lt;0.0001)</td><td>-0.457(&lt;0.0001)</td><td>1.000</td></tr></table>

Notes. Intraday latency data were measured at 60 minute intervals and winsorized at the 1% level to address potential outlier issues. Latency data are in seconds.

As some additional visual motivation, we plot in Figure 2, Panels A and B, the pricing differentials along with the East and West latency differentials aggregated at the weekly level. In Panel A we report the Windows platform pricing differentials, whereas in Panel B we report the Linux/Unix platform pricing differentials. From both panels in Figure 2, one can see that there is significant time variation in the latency differentials and that the pattern of the latency differentials and pricing differentials is similar over time. In many cases, the pricing differentials are also bounded by the latency differentials. Although the visual evidence is helpful in understanding the relation between latency and pricing over time, it is not a formal test of that relation. To formally measure and test the relation between the pricing and latency differentials, we use regression procedures with various model specifications to insure that our results are robust.

Table 6 provides the results from estimating our four different regression specifications across the Windows and Linux/Unix platforms. These two panels show the results of regressing the price differentials on latency differentials and various event indicator variables. The left panel of the table contains the regression results using the Windows platform, whereas the right panel contains the results using the Linux/Unix platform. For Model 1, we include the regional latency differentials in the regression specification, whereas for Model 2 we augment the regional latency differentials with the event indicator variables. Model 3 uses city-level latency differentials, whereas Model 4 augments the city-level latency differentials with the event indicator variables.

Figure 2 (Color online) (Panel A) Weekly Price Differential of m1.xlarge.windows and Latency Differential and (Panel B) Weekly Price Differential of m1.xlarge.linuxunix and Latency Differential  
![](/api/attachments/BBJB2KE8/fulltext/images/1e26ccfcab983a8db671fa2cebb5ff390c3a83cec88de729767e939fe5f66d85.jpg)

![](/api/attachments/BBJB2KE8/fulltext/images/0d4aeeca2e3042719774988c8cd2cb1b0334e73714974b0c4b078a81ceead9eb.jpg)

The results in Table 6 show that latency differentials have a significant effect on the pricing differential. For Model 1, we find that both the East and West latency differentials have a significantly positive effect on the pricing differential, suggesting that larger (smaller) latency effects result in larger (smaller) pricing differentials; that is, latency creates a dynamic pricing wedge, similar to a varying transaction cost, that widens or narrows conditional on the latency differentials as discussed in §2. Although significant, the central latency differential has a much more muted effect (less than one-tenth the size) on the pricing differential as expected given the relative distances and consequent latencies, though it has an unexpected negative effect.

Table 6 Price Differential Regressions

<table><tr><td rowspan="2"></td><td colspan="4">Windows</td><td colspan="4">Linux/Unix</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td> $DL^{East}$ </td><td>12.770(0.0001)</td><td>6.420(0.0001)</td><td></td><td></td><td>7.480(0.0001)</td><td>4.000(0.0001)</td><td></td><td></td></tr><tr><td> $DL^{West}$ </td><td>10.400(0.0001)</td><td>5.550(0.0001)</td><td></td><td></td><td>5.780(0.0001)</td><td>3.310(0.0001)</td><td></td><td></td></tr><tr><td> $DL^{Central}$ </td><td>-0.841(0.0001)</td><td>-0.273(0.0639)</td><td></td><td></td><td>-1.120(0.0001)</td><td>-0.227(0.2995)</td><td></td><td></td></tr><tr><td colspan="9">East</td></tr><tr><td>DL_Atlanta</td><td></td><td></td><td>0.356(0.0001)</td><td>0.038(0.7153)</td><td></td><td></td><td>-0.520(0.0001)</td><td>-0.623(0.0001)</td></tr><tr><td>DL_Boston</td><td></td><td></td><td>0.799(0.0001)</td><td>0.466(0.0001)</td><td></td><td></td><td>0.775(0.0001)</td><td>0.515(0.0001)</td></tr><tr><td>DL_DC</td><td></td><td></td><td>1.250(0.0001)</td><td>0.586(0.0001)</td><td></td><td></td><td>0.687(0.0001)</td><td>0.355(0.0051)</td></tr><tr><td>DL_Newark</td><td></td><td></td><td>2.590(0.0001)</td><td>1.580(0.0001)</td><td></td><td></td><td>1.930(0.0001)</td><td>1.450(0.0001)</td></tr><tr><td>DL_NY</td><td></td><td></td><td>0.744(0.0001)</td><td>0.379(0.0001)</td><td></td><td></td><td>0.434(0.0001)</td><td>0.238(0.0001)</td></tr><tr><td>DL_Philly</td><td></td><td></td><td>2.830(0.0001)</td><td>1.710(0.0001)</td><td></td><td></td><td>1.660(0.0001)</td><td>1.150(0.0001)</td></tr><tr><td>DL_Reston</td><td></td><td></td><td>3.040(0.0001)</td><td>2.060(0.0001)</td><td></td><td></td><td>1.830(0.0001)</td><td>1.290(0.0001)</td></tr><tr><td colspan="9">West</td></tr><tr><td>DL_Denver</td><td></td><td></td><td>-0.372(0.0001)</td><td>-0.222(0.0001)</td><td></td><td></td><td>-0.192(0.0054)</td><td>-0.134(0.0506)</td></tr><tr><td>DL_LA</td><td></td><td></td><td>-1.910(0.0001)</td><td>-1.460(0.0001)</td><td></td><td></td><td>-0.933(0.0001)</td><td>-0.642(0.0001)</td></tr><tr><td>DL_Mesa</td><td></td><td></td><td>-1.300(0.0001)</td><td>-0.713(0.0001)</td><td></td><td></td><td>-0.869(0.0001)</td><td>-0.603(0.0001)</td></tr><tr><td>DL_SD</td><td></td><td></td><td>-3.650(0.0001)</td><td>-2.160(0.0001)</td><td></td><td></td><td>-1.980(0.0001)</td><td>-1.260(0.0001)</td></tr><tr><td>DL_SJ</td><td></td><td></td><td>-1.660(0.0001)</td><td>-0.878(0.0001)</td><td></td><td></td><td>-1.060(0.0001)</td><td>-0.684(0.0001)</td></tr><tr><td>DL_Seattle</td><td></td><td></td><td>-1.670(0.0001)</td><td>-0.924(0.0001)</td><td></td><td></td><td>-0.878(0.0001)</td><td>-0.508(0.0001)</td></tr><tr><td colspan="9">Central</td></tr><tr><td>DL_Chicago</td><td></td><td></td><td>0.509(0.0001)</td><td>0.545(0.0001)</td><td></td><td></td><td>0.063(0.4049)</td><td>0.361(0.0001)</td></tr><tr><td>DL_Dallas</td><td></td><td></td><td>-0.017(0.8200)</td><td>-0.080(0.3015)</td><td></td><td></td><td>0.037(0.7459)</td><td>-0.012(0.9315)</td></tr><tr><td>DL_Houston</td><td></td><td></td><td>0.064(0.1940)</td><td>-0.069(0.1836)</td><td></td><td></td><td>-0.287(0.0001)</td><td>-0.164(0.0375)</td></tr><tr><td>DL_KC</td><td></td><td></td><td>-0.155(0.0132)</td><td>-0.255(0.0001)</td><td></td><td></td><td>0.108(0.2592)</td><td>-0.092(0.3369)</td></tr><tr><td>DL_St.Louis</td><td></td><td></td><td>0.623(0.0001)</td><td>0.441(0.0001)</td><td></td><td></td><td>0.366(0.0029)</td><td>0.447(0.0003)</td></tr></table>

In Model 2 under the Windows platform, where we now include the event indicator variables, we again find that the East and West latency differentials have a significantly positive effect on the pricing differential. The central latency differential is again also much more muted in its impact, but it is now only marginally significant at the 10% level. Interestingly, the introduction of a reduction in the m2.2xlarge and m2.4xlarge on demand reserved prices has a negative effect on the pricing differentials, as does the later introduction of the Tokyo Asia Pacific region. By contrast, the earlier introduction of the Singapore Asia Pacific region has a positive effect on the pricing differential. As additional robustness checks, we include various additional variables in our specifications. Our results are robust to their inclusion. In particular, including Amazon EC2 East center’s failure on April 21, 2011, does not alter our results—the event is not statistically significant in our estimates. If we include a lagged dependent variable in our specifications, we again obtain similar results.

Table 6 (Continued)

<table><tr><td rowspan="2"></td><td colspan="4">Windows</td><td colspan="4">Linux/Unix</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td colspan="9">Indicators</td></tr><tr><td>Micro</td><td></td><td>0.777(0.7351)</td><td></td><td>0.892(0.6664)</td><td></td><td>9.030(0.0158)</td><td></td><td>8.320(0.0255)</td></tr><tr><td>Singapore</td><td></td><td>70.560(0.0001)</td><td></td><td>54.840(0.0001)</td><td></td><td>26.610(0.0001)</td><td></td><td>15.910(0.0001)</td></tr><tr><td>CC</td><td></td><td>-1.450(0.2108)</td><td></td><td>0.304(0.7488)</td><td></td><td>7.680(0.0001)</td><td></td><td>8.020(0.0001)</td></tr><tr><td>Free</td><td></td><td>-0.789(0.6040)</td><td></td><td>-0.315(0.8126)</td><td></td><td>-0.578(0.8114)</td><td></td><td>-0.251(0.9153)</td></tr><tr><td>CG</td><td></td><td>2.060(0.7726)</td><td></td><td>0.260(0.3071)</td><td></td><td>-1.830(0.2818)</td><td></td><td>-3.050(0.1035)</td></tr><tr><td>Reduced</td><td></td><td>-4.820(0.0373)</td><td></td><td>-2.670(0.2151)</td><td></td><td>-4.280(0.2458)</td><td></td><td>-1.830(0.6182)</td></tr><tr><td>Tokyo</td><td></td><td>-3.840(0.0001)</td><td></td><td>-3.390(0.0001)</td><td></td><td>-0.813(0.5688)</td><td></td><td>-0.566(0.6886)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.928</td><td>0.950</td><td>0.946</td><td>0.957</td><td>0.692</td><td>0.706</td><td>0.707</td><td>0.714</td></tr><tr><td>Obs.</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td></tr></table>

Notes. This table provides regression results of the price differentials $( P ^ { W e s t } - P ^ { E a s t } )$ on the latency differentials and various event indicator variables. The variable definitions are provided in Table 4. The regressions use intraday data measured at 60 minute intervals, and the sample period runs from April 9, 2010, to May 22, 2011. All estimates are multiplied by 1,000.

Models 3 and 4 provide the results using the citylevel latency differentials and augmented model with event indicator variables. Recall that the city-level latency differentials are measured as the average latency to Amazon West EC2 center at city i minus the average latency to Amazon East center at city i. As expected, across both Models 3 and 4, we find that the city-level latency differentials have a significant effect on the pricing differentials. The positive signs on the eastern city differentials are as expected, as are the negative signs on the western city differentials, given how we define the city-level latency differentials; that is, the western cities will have lower latencies to the west by design given their location, resulting in a negative latency differential given the larger latency to the east. The interpretation of the negative latency differential on the price differential defined as $P ^ { W e s t } - P ^ { E a s t }$ in this case would result in an inverse relation. As expected, several of the central city latency differentials do not have a significant effect on the pricing differential given that their latencies are often similar to the West and East markets. In Model 4, augmented with the event indicator variables, we again find that the introduction of Tokyo and Singapore results in negative and positive price differential effects, respectively. However, the reduced indicator event is no longer significant when the city-level latency differentials are used.

The Linux/Unix platform results are reported in the right columns of Table 6. Similar to the Windows platform results, we again find that latency differentials (except central latency differential) have a significant effect on the pricing differentials for both the differential latencies measured at the regional or city level. The indicator event effects are also very similar to those discussed for the Windows platform results, with the exception that the Tokyo introduction and reduced indicator event do not have a significant effect across any of our model specifications with the Linux/Unix platform.

We have shown that both the East and West latency differentials have a significant effect on the pricing differentials. However, some may argue that there might be differences in the prevalent industry sectors in the two coasts, and these industry differences (or other factors), rather than the latency, drive the price differential. This “other factors” question can be best answered both conceptually and empirically. Conceptually, no other factors can reasonably explain the persistent price differentials but for latency, by envisioning the counterfactual of a world without latency. Suppose there is no latency (the counterfactual part) and there are persistent price differentials between the spot prices of the Amazon EC2 West and East centers (the West prices are always 30% higher). In the absence of latency, the prevalent industry sectors in the two coasts cannot explain the persistent price differentials. Since any company in any industry sector can effortlessly bid in either Amazon’s East or West center, no industry sector will bid for spot instances in the persistently higher West market. As a result, the persistently higher-priced spot market in the West center will cease to exist without latency.

Empirically, to insure that our results are robust, we performed numerous additional tests, as discussed throughout this paper and are available in the online appendix (available as supplemental material at http:// dx.doi.org/10.1287/isre.2015.0608). Our reported results are robust to numerous additional tests, including varying specifications, nonlinear specifications, outlier tests, additional control variables, additional latency lags, and alternative instance samples and frequencies. We also ran reverse causality regressions and found no evidence of a simultaneity or endogeneity issue of pricing dynamics influencing latency. In §4.3.2, we further use two-stage least squares (2SLS) instrumental variable procedures to address potential omitted variable bias issues.

4.3.2. Additional Identification Tests and Shortand Long-Run Price Differential Dynamics: 2SLS Regressions and Error Correction Models. As an additional strong identification test, we used 2SLS IV procedures. Although employing IV procedures can often be challenging because of the limited availability of ideal exogenous instruments, we have an ideal instrument in this setting that is clearly correlated with latency and cannot be affected by price or an omitted variable—physical distances (the straight line distances between the center of city i and Amazon EC2’s data center locations); that is, distance is clearly exogenous to price or any other possible latent factor. Physical distances cannot be affected by any of these variables.

In this set of tests, we use 2SLS IV procedures whereby we regress distances at the city level against the corresponding latencies and take the fitted values (predicted values) as an instrument for latency in our second stage pricing regressions. In the first stage, we run regression models where we regress Distance\_ $C i t y _ { i - } t o .$ \_East (or West or Central) against Latency \_City \_to\_East (or West or Central) for each hour and every city within each region. From these regressions, we obtain predicted hourly city-level latencies based on distance as an IV. This dynamic estimation approach allows for hourly variation in the associated coefficient estimates on distance and time-varying citylevel latency estimates.<sup>17</sup> With the predicted city-level latencies from the first stage regressions, we calculate average regional-level latencies and take these variables into the original model to perform the second stage regression—price difference with IVs.

Table 7 provides the results from our 2SLS regression procedures. In the first stage, we report the regression statistics for the median estimate results from the time-varying estimates. For clarity of fit purposes, we chose to report the results at their medians, but presenting the results for the averages also yields similar inferences. The specifications for second stage results are exactly the same as in Table $6 ,$ except we use instrumented latency (predicted latency with distance as the instrument) from the first stage estimates in place of latency.

Looking at the first stage results in Table $^ { 7 , }$ we see that distance is a strong instrument for latency, with significant coefficient estimates, F -tests, and high $R ^ { 2 }$ values in the first stage regressions. The weaker fit for the central estimates are not surprising since there is significantly less variation in both latency and distance among central cities to Amazon East and West centers. In our second stage regressions, we obtain results that are very similar to the results reported in Table 6. These results further strongly confirm and identify that latency causally affects the price differentials.

To capture both long-run and short-run pricing dynamics, we also employ an ECM. The ECM model is appropriate if the series are nonstationary and cointegrated. Unit root test results suggest that the Windows East and West prices are nonstationary at the 10% significance level and are cointegrated $( P ^ { W e s t }$ , ADF P-value = 0.08; $P ^ { E a s t }$ , ADF P-value = 0.04; ADF is the augmented Dickey–Fuller unit root test). The ECM framework allows us to model the East and West pricing relations as an adjustment process around their long-run equilibrium price convergence. Error correction models are based on the idea that two or more time series exhibit a long-run time-varying equilibrium to which the system tends to converge. This long-term convergence in pricing is a reasonable assumption given that long-run pricing in both the East and West should be similar or users would shift their computing to the lower priced market through negative feedback and error correction, with the latency differential playing an important role in the potential pricing convergence.

Following the Engle and Granger (1987) two-step method, a long-run price model is specified in levels. The second stage, short-run adjustment model is specified in first differences and includes a long-run error correction term from the estimation of the long-run, equilibrium model (the residuals from the first stage model as an error correction term). In the first stage, theory and econometric evidence are used to determine whether the East and West Amazon EC2 spot instance price series contain unit roots and are cointegrated. If the pricing series are cointegrated, a long-run equilibrium relation $( \mathrm { i . e . , }$ a cointegrating regression) can be specified in levels as

$$
P _ {t} ^ {W e s t} = \beta_ {0} + \beta_ {1} P _ {t} ^ {E a s t} + \pmb {v} _ {t},\tag{8}
$$

where $P _ { t } ^ { W e s t }$ and $P _ { t } ^ { E a s t }$ are the Amazon EC2 spot instance price levels in the West and East, respectively. From this regression, we can estimate residuals as the differences between the actual and estimated equilibrium values of the price levels. If the residuals from Equation (8) are stationary, they may be used as error correction terms in the short-run price difference model as follows:

Table 7 Additional Identification Test: 2SLS Instrumental Variables Approach

<table><tr><td colspan="4">First stage regression statistics at median: Latency</td></tr><tr><td></td><td>Median coefficient (p-value)</td><td>Median F-statistic (p-value)</td><td>Median  $R^2$ </td></tr><tr><td colspan="4">To East</td></tr><tr><td>Distance East</td><td>0.0030(0.0575)</td><td>15.2113(0.0114)</td><td>0.75</td></tr><tr><td>Distance West</td><td>0.0048(0.0768)</td><td>5.6135(0.0640)</td><td>0.58</td></tr><tr><td>Distance Central</td><td>0.0023(0.4153)</td><td>0.8887(0.3891)</td><td>0.23</td></tr><tr><td colspan="4">To West</td></tr><tr><td>Distance East</td><td>0.0032(0.1036)</td><td>3.6927(0.1127)</td><td>0.43</td></tr><tr><td>Distance West</td><td>0.0015(0.0483)</td><td>6.6844(0.0491)</td><td>0.66</td></tr><tr><td>Distance Central</td><td>0.0032(0.3880)</td><td>1.0142(0.3601)</td><td>0.25</td></tr></table>

Second stage regression: Price difference with latency IV

<table><tr><td rowspan="2"></td><td colspan="2">Windows</td><td colspan="2">Linux/Unix</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td></tr><tr><td>East_IV_Latency</td><td>15.59(&lt;0.0001)</td><td>11.980(&lt;0.0001)</td><td>8.930(&lt;0.0001)</td><td>7.190(&lt;0.0001)</td></tr><tr><td>West_IV_Latency</td><td>8.080(&lt;0.0001)</td><td>6.330(&lt;0.0001)</td><td>4.800(&lt;0.0001)</td><td>3.910(&lt;0.0001)</td></tr><tr><td>Central_IV_Latency</td><td>0.671(0.0001)</td><td>0.442(0.0019)</td><td>-0.524(0.0150)</td><td>0.505(0.0344)</td></tr><tr><td>Micro</td><td></td><td>2.020(0.3137)</td><td></td><td>10.010(0.0028)</td></tr><tr><td>Singapore</td><td></td><td>34.750(&lt;0.0001)</td><td></td><td>4.180(0.0380)</td></tr><tr><td>CC</td><td></td><td>-2.530(0.0096)</td><td></td><td>9.000(0.0022)</td></tr><tr><td>Free</td><td></td><td>-0.672(0.6032)</td><td></td><td>-0.498(0.8183)</td></tr><tr><td>CG</td><td></td><td>5.480(&lt;0.0001)</td><td></td><td>0.308(0.8716)</td></tr><tr><td>Reduced</td><td></td><td>-594(0.0026)</td><td></td><td>-6.560(0.0470)</td></tr><tr><td>Tokyo</td><td></td><td>-4.420(&lt;0.0001)</td><td></td><td>-0.969(0.4493)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.9601</td><td>0.9637</td><td>0.7508</td><td>0.7540</td></tr><tr><td>Obs.</td><td>9,816</td><td>9,816</td><td>9,816</td><td>9,816</td></tr></table>

Notes. In this additional identification test, we employ 2SLS procedures. In the first stage, we run regression models where we regress Distance\_City \_to\_East (or West or Central) against Latency \_City \_to\_East (or West or Central) for each hour and every city within each region. From these regressions, we obtain predicted hourly city-level latencies based on distance as an instrumental variable. This dynamic estimation approach allows for hourly variation in the associated coefficient estimates on distance and time varying city-level latency estimates. With the predicted city-level latencies from the first stage regressions, we calculate average regional-level latencies and take these variables into the original model to perform the second stage regression—price difference with IV. Below we report the results from our 2SLS instrumental variables procedures. In the first stage, we report the regression statistics for the median estimate results from the time-varying estimates. The specification for second stage results are exactly the same as Table 6, except we use instrumented latency (predicted latency with distance as the instrument) from the first stage estimates in place of latency.

$$
P D _ {t} = \alpha_ {0} + \sum_ {i = 1} ^ {n} \alpha_ {i} \Delta X _ {i t} - \gamma \hat {\pmb {v}} _ {t - 1} + \varepsilon_ {t},\tag{9}
$$

where $P D _ { t } = P _ { t } ^ { W e s t } - P _ { t } ^ { E a s t }$ is the pricing differential between West and East Amazon EC2 spot instance pricing in time $t , \Delta X _ { i t }$ are first differences of the explanatory variables $( \mathrm { i . e . , }$ differences in latency in time t), $\hat { \nu } _ { t } .$ −1 is the error correction term (i.e., the lagged residuals from the long-run cointegrating regression), and all of the difference terms are stationary. Estimation of Equation (9) provides evidence on short-run pricing dynamics related to latency differentials (the $\alpha _ { i } ^ { \prime } \mathbf { s } )$ and adjustments to the previous disequilibrium in the longrun relation,  (the speed of adjustment parameter).

Table 8 Short- and Long-Run Price Differential Dynamics Using an Error Correction Model

<table><tr><td>Variable</td><td>Parameter estimate</td><td>Pr &gt; |t|</td></tr><tr><td colspan="3">Panel A: Stage 1,  $P_{t}^{West} = \beta_{0} + \beta_{1}P_{t}^{East} + v_{t}$ </td></tr><tr><td>Intercept</td><td>0.531</td><td>&lt;0.0001</td></tr><tr><td> $P_{East}$ </td><td>3.200</td><td>0.7826</td></tr><tr><td colspan="3">Panel B: Stage 2,  $PD_{t} = \alpha_{0} + \sum_{i=1}^{n} \alpha_{i} \Delta X_{it} - \gamma \hat{v}_{t-1} + \varepsilon_{t}$ ,</td></tr><tr><td>lagpd</td><td>0.849</td><td>&lt;0.0001</td></tr><tr><td> $DL_{East}$ </td><td>1.590</td><td>&lt;0.0001</td></tr><tr><td> $DL_{West}$ </td><td>1.860</td><td>&lt;0.0001</td></tr><tr><td> $DL_{Central}$ </td><td>-0.085</td><td>0.3901</td></tr><tr><td>lagres</td><td>-0.544</td><td>&lt;0.0001</td></tr></table>

Notes. This table provides ECM estimates using the Windows platform prices. Unit root tests suggest that the Windows East and West prices are nonstationary at the 10% significance level and are cointegrated $( P ^ { W e s t } , \mathsf { A D F } P \mathsf { - v a l u e } = 0 . 0 8 ;$ $P ^ { E a s t } , A D F \ P \Join$ is the augmented Dickey–Fuller unit root test). Following the Engle–Granger two-step method, we specify a long-run price model in levels. In the short-run second stage adjustment model, the variables are specified as first differences and include the residuals from the first stage model as an error correction term. The variable definitions are provided in Table 4. The term $\Delta X _ { i t }$ are first differences of the explanatory variables (i.e., differences in latency in time $t ) , \hat { v } _ { t - 1 }$ is the error correction term (i.e., the lagged residuals from the long-run cointegrating regression, lagres), and all of the difference terms are stationary. The regressions use intraday data measured at 60 minute intervals, and the sample period runs from April 9, 2010, to May 22, 2011. Price and latency differential estimated coefficients are multiplied by 1,000.

Consistent with our prior empirical specifications, the variable of interest is the cross-market price dynamic. We chose to be more conservative in our approach by using both price difference regressions and a modified ECM model to further show the robustness of our results if one was concerned with potential nonstationarity problems. However, our fundamental results in this paper do not hinge on the ECM model results, and the ECM model results are robust to alternative ECM model specifications.

Table 8 reports the results from estimating the ECM model using the Windows platform instance prices. In Panel $\scriptstyle \mathbf { A } ,$ we find that East prices have a positive long-run relation on West prices, though the standard errors of the equilibrium estimate are large. In Panel B, we find that lagged price differentials have a positive and significant influence on current price differentials, suggesting some persistence in the pricing differentials. We also find that the East and West latency differentials continue to have a positive and significant influence on the pricing differentials. This suggests that latency plays an important role in the short-run pricing dynamics across the East and West markets, consistent with our proposed hypothesis. Looking at the error correction term, lagres, we find that the speed of adjustment parameter is both significant and negative, suggesting that a wider disequilibrium $( \mathrm { i . e . , }$ larger errors) from the long-run price convergence causes the short-run price differential to narrow, but the adjustment is only partial at −00544.

## 5. Managerial Implications

The key takeaway from our study is that companies should factor in their latency tolerance in deciding how much to bid for cloud computing spot instances. The apparent arbitrage opportunity for Amazon EC2 cloud computing spot instances no longer exists after taking latency effects into account; that is, for latencysensitive firms, the total cost, including the price of the spot instance and latency, for a company on the West Coast using the Amazon West EC2 center is comparable to that of the Amazon East EC2 center. In the short term, companies should take into account their latency tolerance in their spot instance bidding strategies. In the long term, corporations currently using or those considering the adoption of cloud computing should collect baseline latency metrics and their latency tolerance and determine how much they want to pay for reducing latency—which undoubtedly depends on the cost and benefit trade-offs of doing so. The statement by the chief cloud architect for Netflix, Adrian Cockcroft, in a recent interview, “How many dollars should you spend to reduce customer latencies by 50% if that increases your conversion rate by 10%?,” exemplifies a good rough equation to formulate the trade-off (Babcock 2013). For industries sensitive to latency, such as finance (e.g., investment banking and financial services firms), entertainment (e.g., Netflix), and multiplayer online games (e.g., Blizzard Entertainment, publisher of World of Warcraft), it is often imperative to reduce latency by strategically locating their facilities. Stibel (2013), for example, argues that traders have gone to great lengths to improve their speeds: “some have gone so far as to move their computer networks to be in close physical proximity to the data centers of the stock exchange and news outlets, paying hundreds of millions of dollars for direct access.” A recent real estate transaction further illustrates how much reducing latency by colocation can be worth, where One Wilshire, an office building in downtown Los Angeles, sold for a record \$437.5 million since it is one of the three leading telecommunications interconnect hubs in the world (Vincent 2013).

## 6. Conclusion

Our research is the first to examine the effects of latency on pricing dynamics both within and across different spot markets and provides convincing evidence that even with the same cloud computing provider and computing platform, price heterogeneity still exists because of latency differentials across markets. We further address other key questions in this paper. First, what are the stylized pricing dynamics for Amazon EC2 spot instance pricing both within and across East and West market regions? Second, what explains the observed pricing dynamics and pricing differentials across the East and West markets? Third, what effect does latency have on the across-market pricing differentials? In addressing the first question, we document that across Windows and Linux/Unix OS platforms as well as spot instance types, there is considerable time variation in spot prices. We also find that prices in the West are often persistently greater than prices in the East over our sample period. Results from using a bivariate VAR model of East and West spot instance prices suggests that there are significant dynamic pricing relations both within and across the East and West markets. We find that the within-market autoregressive pricing effect is larger than the across-market effect, but there are also significantly pronounced across-market pricing effects. Using both Hasbrouck’s (1995) and Gonzalo and Granger’s (1995) price discovery methodologies, we also find that over 70% of the relative price discovery occurs in the East market relative to the West market.

To explain the observed time-varying pricing differentials across the East and West markets (i.e., addressing our second and third questions), we use both regression procedures and an error correction model. We find that both the East and West latency differentials have a significantly positive effect on the pricing differentials. These results suggest that larger (smaller) latency effects result in larger (smaller) pricing differentials. Similar to a time-varying transaction cost band, latency creates a dynamic pricing wedge that widens or narrows conditional on the latency differentials, consistent with our proposed hypothesis. From the ECM results, we also find that the speed of adjustment from longrun pricing convergence errors causes the short-run price differential to narrow, but the adjustment is only partial.

Interestingly, our results suggest that data in some ways behaves similar to physical goods in that longer latencies from the cloud result in larger total transaction costs (transportation costs in physical goods). From a managerial perspective, bidding on the relatively lower priced cloud computing location is optimal if latency is not an important customer concern. However, if latency exposure is an important concern, then the firm’s optimal cloud computing location selection should factor in pricing-latency effects, both in terms of cloud bidding location as well as potentially longer-term firm operational computing location choices.

The results from our paper can also be viewed in a broader context and provide a framework for some additional follow-on research questions. From a broader context, our research provides some further evidence and insights into market-based pricing dynamics and market efficiency issues in a burgeoning new market with unique characteristics, including latency effects. Although markets have become increasingly integrated due to technological innovations and reductions in barriers across markets, several studies show that geographical distance still matters in behavioral, economic, and financial outcomes. These studies establish the relevance of geographical proximity to consumer’s costs of acquiring information, which in turn influences the behavior of both consumers and firms.

The effects of distance manifest themselves through higher search costs often related to information acquisition problems (e.g., degree of information asymmetry and uncertainty as well as other information and market impediments) and behavioral biases (e.g., anchoring and loss aversion). Both higher search costs and behavioral biases may lead to the payment of higher prices for a given good. In this regard, our research on latency effects provides some evidence consistent with the role of market impediments playing a fundamental role in the cloud pricing dynamics. At the same time, consumers may suffer from behavioral biases, which may cause them to “anchor” their expectations on local or personal circumstances and prior decisions. Further research on understanding the nature of these potential factors in the pricing dynamics of cloud computing could yield some additional interesting insights.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0608.

## Acknowledgments

The authors thank Lloyd Bloom, Sanjukta Das Smith, Dick Elnicki, Anuj Kumar, Mahendrarajah Nimalendran, Liangfei Qiu, Suprateek Sarker, three anonymous reviewers, the associate editor, the senior editor, and seminar and conference participants at Babson College, Florida International University, University of Florida, University of Illinois, University of Maryland, University of Notre Dame, the 2013 Taiwan Summer Workshop on Information Management, and the 2014 Information Systems and International Management Forum. The authors also thank Compuware for providing data for this project. The first author gratefully acknowledges the support of John B. Higdon Eminent Scholar Chair of the University of Florida and the Distinguished Overseas Professorship of the School of Information Management and Engineering, Shanghai University of Finance and Economics.

## References

Ba S, Stallaert J, Zhang Z (2012) Research note—Online price dispersion: A game-theoretic perspective and empirical evidence. Inform. Systems Res. 23(2):575–592.

Babcock C (2013) Netflix’s 5 secrets for maximizing Amazon cloud value. InformationWeek (April 8), www.informationweek.com/ cloud/infrastructure-as-a-service/netflixs-5-secrets-for-maximizing -amazon-cloud-value/d/d-id/1109453.

Baillie RT, Geoffrey Booth G, Tse Y, Zabotina T (2002) Price discovery and common factor models. J. Financial Markets 5(3):309–321.

Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Brynjolfsson E, Hu YJ, Rahman MS (2009) Battle of the retail channels: How product selection and geography drive cross-channel competition. Management Sci. 55(11):1755–1765.

Cheshire S (1996) It’s the latency, stupid. Report, Stanford University, Stanford, CA.

Clayton N (2011) Meet the rainmakers. Wall Street Journal (February 14), http://www.wsj.com/articles/SB10001424052748704 739504576067580949404062.

Cohen R (2013) The cloud hits the mainstream: More than half of U.S. businesses now use cloud computing. Forbes (April 16), http://www.forbes.com/sites/reuvencohen/2013/04/16/the -cloud-hits-the-mainstream-more-than-half-of-u-s-businesses -now-use-cloud-computing/#1262226467c2.

Das S, Du AY, Gopal R, Ramesh R (2011) Risk management and optimal pricing in online storage grids. Inform. Systems Res. 22(4):756–773.

De Jong F (2002) Measures of contributions to price discovery: A comparison. J. Financial Markets 5(3):323–327.

Du AY, Das S, Ramesh R (2012) Efficient risk hedging by dynamic forward pricing: A study in cloud computing. INFORMS J. Comput. 25(4):625–642.

Engle RF, Granger CW (1987) Co-integration and error correction: Representation, estimation, and testing. Econometrica 55(2): 251–276.

Forrester Consulting (2009) eCommerce Web site performance today: An updated look at consumer reaction to a poor online shopping experience. White paper, Akamai Technologies Inc., Cambridge, MA.

Gonzalo J, Granger C (1995) Estimation of common long-memory components in cointegrated systems. J. Bus. Econom. Statist. 13(1):27–35.

Hamilton JD (1994) Time Series Analysis (Princeton University Press, Princeton, NJ).

Hasbrouck J (1995) One security, many markets: Determining the contributions to price discovery. J. Finance 50(4):1175–1199.

Lehmann BN (2002) Some desiderata for the measurement of price discovery across markets. J. Financial Markets 5(3):259–276.

Mayer M (2009) In search of a better, faster, stronger Web. Proc. Velocity.

Mazzucco M (2010) Towards autonomic service provisioning systems. Proc. 10th IEEE/ACM Internat. Conf. Cluster, Cloud Grid Comput. (IEEE Computing Society, Washington, DC), 273–282.

Mazzucco M, Dumas M (2011) Achieving performance and availability guarantees with spot instances. IEEE 13th Internat. Conf. High Performance Comput. Comm. Proc. (IEEE, Piscataway, NJ), 296–303.

Miller RB (1968) Response time in man-computer conversational transactions. ACM AFIPS Proc. Fall Joint Comput. Conf. (ACM, New York), 267–277.

Minnear R (2011) Latency: The Achilles heel of cloud computing. Accessed January 29, 2016, http://cloudcomputing.sys-con.com/ node/1745523.

O3b Networks (2008) What is network latency and why does it matter? White paper, O3b Networks, Ltd., St. John, Jersey.

Plummer DC, Cearley DW, Smith DM (2008a) Cloud computing confusion leads to opportunity. Report, Gartner, Stamford, CT.

Plummer DC, Bittman TJ, Austin T, Cearley DW, Smith DM (2008b) Cloud computing: Defining and describing an emerging phenomenon. Report, Gartner, Stamford, CT.

Ried S, Kisker H (2011) Sizing the cloud—A BT futures report. Report, Forrester Research, Inc., Cambridge, MA.

Stibel J (2013) Will the Internet destroy the stock market? Harvard Business Rev. Accessed January 29, 2016, https://hbr.org/2013/ 08/will-the-internet-destroy-the/.

Vincent R (2013) One Wilshire sells for record \$437.5 million. Los Angeles Times (July 18), http://articles.latimes.com/2013/jul/18/ business/la-fi-0718-property-report-20130718.

Zhang Q, Zhu Q, Boutaba R (2011) Dynamic resource allocation for spot markets in cloud computing environments. Proc. Fourth IEEE Internat. Conf. Utility Cloud Comput., Victoria, NSW, Australia, 178–185.
