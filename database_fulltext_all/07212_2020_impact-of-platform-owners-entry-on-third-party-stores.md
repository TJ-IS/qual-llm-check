---
otero_id: 7212
otero_key: "WUUK8BPE"
title: "Impact of Platform Owner’s Entry on Third-Party Stores"
authors: "Shu He; Jing Peng; Jianbin Li; Liping Xu"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0957"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.209.6.61] On: 30 October 2020, At: 18:44 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/WUUK8BPE/fulltext/images/b73307bfb5cac30e5c9faf562f05f9006e2f6a71baac6df4563f3c9dbfc908a4.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Impact of Platform Owner’s Entry on Third-Party Stores

Shu He, Jing Peng, Jianbin Li, Liping Xu

To cite this article:

Shu He, Jing Peng, Jianbin Li, Liping Xu (2020) Impact of Platform Owner’s Entry on Third-Party Stores. Information Systems Research

Published online in Articles in Advance 30 Oct 2020

https://doi.org/10.1287/isre.2020.0957

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Impact of Platform Owner’s Entry on Third-Party Stores

Shu He,<sup>a</sup> Jing Peng,<sup>a</sup> Jianbin Li,<sup>b</sup> Liping Xu<sup>b</sup>

<sup>a</sup> Department of Operations and Information Management, University of Connecticut, Storrs, Connecticut 06269; <sup>b</sup> School of Management, Huazhong University of Science and Technology, Wuhan 430074, China

Contact: shu.he@uconn.edu, https://orcid.org/0000-0001-5899-5299 (SH); jing.peng@uconn.edu, https://orcid.org/0000-0001-5490-6228 (JP); jbli@hust.edu.cn (JL); 15927073712@163.com (LX)

Received: August 11, 2018<sub>Revised:</sub> Jun Accepted: Published Online in Articles in Advance: October 30. 2020

https://doi.org/10.1287/isre.2020.095

Copyright:

Abstract. Online marketplaces thrive by offering products from a wide array of thirdparty stores. One major decision faced by the owners of online marketplaces is whether they should enter into the market and sell products directly to customers. Although a few game-theoretical models have addressed this issue, there is still no empirical research to guide the decisions of managers. To fill this gap, this paper empirically investigates the impact of a platform owner’s entry on the demand of third-party stores, as well as their potential reactions, using data from a Chinese e-commerce platform that supports both online and offline transactions. We establish several important findings. First, we find that the offline demand of competing third-party stores decreases with the entry of the platform, whereas their online demand does not change significantly. Second, we systematically investigate three potential mechanisms underlying the effects of platform entry in the online and offline channels: the competition effect, the spillover effect, and the disintermediation effect. We show that the decreased offline demand results from third-party stores’ defensive strategy to divert their offline customers away from the platform (i.e., disintermediation) rather than from the defection of customers under competition. Third, in contrast to the prior finding from mobile app platforms, we find that the demand of larger third-party stores decreases more with the entry of the platform, suggesting that the effect of platform entry is context dependent. Our study suggests that, while making entry decisions, platform owners should consider the nature of their marketplaces (i.e., whether the competition among sellers is exclusive) and the potential reactions from third-party sellers.

History: D. J. Wu, Senior Editor; Pei-Yu Chen, Associate Editor. Funding: This research was partially supported by the Natural Science Foundation of China [Grants 71831007 and 71821001]. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2020.0957.

Keywords: platform entry • <sup>fi</sup>rst-party • third-party • online • of<sup>fl</sup>ine • disintermediation

## 1. Introduction

E-commerce platforms (e.g., Amazon, JD, and Taobao) often have both platform-owned (first-party) and third-party stores, although initially they may only focus on one type of stores. For example, Amazon had no third-party stores until it launched its marketplace in 2000. On the other hand, Taobao, which had served as a marketplace for third-party retailers since its inception, opened a first-party store that sells products directly to customers (i.e., good.- tmall.com) in 2017. By entering into certain product categories, the platform not only appropriates value from third-party stores (Zhu and Liu 2018), but also increases the general awareness of these products on the platform. However, the direct competition of the platform with third-party stores can crowd thirdparty stores out of the platform and drive away customers (Jiang et al. 2011, Ryan et al. 2012).

For platform managers, it is critical to understand the impact of the platform owner’s entry on the demand of competing third-party sellers and thirdparty sellers’ potential reactions to the entry. However, research on this issue is still nascent. In the context of e-commerce, prior studies primarily use game-theoretical models to identify the equilibrium strategies of the platform and third-party retailers when the platform has the option to enter the market (Jiang et al. 2011, Ryan et al. 2012, Chen and Guo 2018). In the context of mobile apps, empirical studies have shown that the platform entry has a positive spillover effect on third-party apps, especially for large ones (Li and Agarwal 2017, Foerderer et al. 2018). However, this finding may not be generalizable to e-commerce platforms because, unlike mobile apps that are typically free,<sup>1</sup> products are rarely free on e-commerce platforms. Therefore, how the platform entry affects the demand of the complementors (i.e., third-party stores) remain unclear in the e-commerce context. More importantly, to our best knowledge, no study has yet empirically investigated how third-party sellers respond to the entry of the platform in a complementary market.

This paper seeks to fill in these research gaps using a proprietary data set from a large online marketplace platform in China. The platform primarily focuses on business-to-business transactions among wholesalers (henceforth sellers) and retailers (henceforth customers), although it also supports business-to-customer transactions. The platform did not have first-party stores initially but gradually opened multiple first-party stores in different cities. One unique feature of this platform is that every store on this online platform, first-party or third-party, is backed by a physical store. In addition to ordering online, customers may also order directly from the store through offline communications (e.g., order in person, by phone, or via text message). We therefore have sales data from both online customers and offline customers (if they choose to pay through the platform), which allows us to separately investigate the effects of platform entry on the online and offline demand of thirdparty stores and the underlying mechanisms for each channel. Taking advantage of this rich data set, we aim to address the following questions:

1. How does platform owner’s entry affect the online and offline demand of third-party stores, respectively?

2. What are the plausible mechanisms for the changes in the online and offline demand of third-party stores after platform owner’s entry?

3. Does platform owner’s entry have differential effects on large and small third-party stores?

To answer these questions, we analyze our data with the widely used difference-in-differences (DID) model. We find that, after the entry of a first-party store, the demand of third-party stores in the same category and city as the first-party store decreases significantly. Interestingly, the decrease is only significant for the offline demand, but not for the online demand. Moreover, in contrast to previous findings from mobile app platforms, we find that the offline demand of larger third-party stores decreases more with the platform owner’s entry. To explain the observed phenomena, our additional analyses demonstrate that the decrease in third-party stores’ offline demand is not driven by the defection of customers under competition but, rather, by third-party stores defensive strategy to divert their offline customers away from the platform. The offline demand of larger third-party stores decreases more because they have more offline customers to protect.

We make the following contributions to the literature. First, to our best knowledge, this paper is the first empirical study to investigate the impact of platform entry on third-party sellers in the e-commerce context, providing data-driven insights for both researchers and practitioners. Second, this paper documents the differential effects of platform entry in the online and offline channels. Third, this paper sheds light on the mechanisms behind the decrease in the demand of third-party sellers and demonstrates that, in response to platform entry, third-party sellers proactively protect their customer bases by encouraging their offline customers to transact outside the platform. Finally, our work complements prior studies on mobile app platforms by highlighting the contextual dependence of the impact of platform entry.

## 2. Literature

Although it is common for a platform to enter into a complementary market, the consequences of this decision are not well understood yet. Earlier research in this area primarily focuses on how the entry decision affects complementors’ innovation (Farrell and Katz 2000, Gawer and Henderson 2007, Wen and Zhu 2019). Researchers have recently started to investigate how platform owner’s entry affects complementors’ demand.

In the context of e-commerce, the research on platform owner’s entry is limited to game-theoretical models. Ryan et al. (2012) consider a marketplace setting in which both the platform and a third-party retailer can sell products to customers, but the thirdparty retailer has an option to sell through its own website. The authors show that whether the platform chooses to coordinate or to compete with the third party retailer depends on whether the retailer is a strong competitor. Jiang et al. (2011) find that the platform can become worse off by retaining the option of entry, because retailers can be incentivized to mask their high-demand products to prevent the platform from strategically entering into their product space More recently, Kwark et al. (2017) demonstrate that the availability of third-party information such as product reviews may affect the decision of an online retailer to operate as a platform or a wholesaler. Chen and Guo (2018) further show that a platform tends to embrace third-party sellers when the advertising cost is low enough (e.g., advertising on social media). Song et al. (2020) discuss the impact of spillover effect on third-party sellers’ selling strategies and retailer’s platform-openness decision.

Despite the significant modeling interest in the impact of platform entry in the context of e-commerce, empirical research in this area is scant. In the only empirical study we are aware of, Zhu and Liu (2018) demonstrate that Amazon is more likely to target successful complementors than poorly performing ones. In other words, Amazon focuses more on appropriating value from the innovations of thirdparty retailers than on improving the overall quality of goods on its platform. Nevertheless, this paper does not answer the question of how the entry of the platform affects the demand of third-party sellers.

One probable reason for the limited empirical research on e-commerce platforms is that the necessary data are often not available to researchers. With the increasingly available data about mobile apps, recent studies have investigated the impact of platform entry on the demand of third-party apps. Specifically, Li and Agarwal (2017) find that Facebook’s integration of Instagram has a negative spillover effect on small third-party apps, whereas a positive spillover effect on large third-party apps. Using a natural experiment (i.e., Google’s release of the Google Photos app), Foerderer et al. (2018) also demonstrate that larger third-party apps benefit more from the attention spillover effect of platform entry. However, this finding from mobile app platforms might not extend to e-commerce platforms because, unlike mobile apps, the products typically are not free on e-commerce platforms. Therefore, the impact of platform entry on the demand of third-party sellers on e-commerce platforms warrants a separate study.

## 3. Theoretical Background

The launch of first-party stores may affect the demand of competing third-party stores in multiple ways. Here, we discuss three mechanisms through which the entry of first-party stores can influence the demand of competing third-party stores: the competition effect (Zhu and Liu 2018), the spillover effect (Li and Agarwal 2017, Foerderer et al. 2018), and the disintermediation effect (Gu and Zhu 2020). Given that online and offline customers have different ordering processes and are subject to different constraints (e.g., information asymmetry and geographical proximity), the roles of these three mechanisms are likely to be different in the online and offline channels. As such, we also elaborate on which mechanism is plausible in each channel.

## 3.1. Competition Effect

It has been shown that a platform may enter into a complementary market to appropriate value from complementors (Zhu and Liu 2018). By launching first-party stores, the platform could steal customers from competing third-party stores selling similar products, because of its reputation and awareness advantages (Chen and Guo 2018). Therefore, the demand of third-party stores could decrease because of the direct competition with the platform (Jiang et al. 2011, Ryan et al. 2012).

The competition effect is more likely to influence third-party stores’ online demand than their offline demand for three reasons. First, the search cost of online customers is generally much lower than that of offline customers. Unlike offline customers who often need to travel to explore potential alternative stores, exploring alternatives is very convenient for online customers. As a result, online customers are more likely to become aware of first-party stores and hence have a higher probability to switch to first-party stores. Second, compared with offline customers who may communicate with the sellers in person, over phone, or via text message, online customers may rely more on the reputation of stores, because they often have less outlets to obtain information about the stores and their products. In this sense, online customers are more likely to switch to the platform-backed first-party stores to alleviate their concerns about the sellers’ credibility. Third, because the third-party stores were in operation offline before they joined the platform, they have already established an offline customer base with whom they may maintain an offline relationship. Compared with online customers, the switching cost (Klemperer 1987, Chen and Hitt 2002, Li and Agarwal 2017) of offline customers is expected to be higher because switching to first-party stores may undermine their established offline relationships with the third-party sellers, not to mention that it may also result in extra communication cost and/or transportation cost for offline customers.<sup>2</sup> Therefore, the competition effect is more plausible in the online channel than in the offline channel.

## 3.2. Spillover Effect

The entry of the platform could increase the exposure or awareness of the products sold at first-party stores, driving up their demand. The increased demand for these products could spill over to third-party stores selling similar products. Thus, the demand of thirdparty stores could increase as the overall demand increases. This is known as the attention spillover effect (Li and Agarwal 2017, Foerderer et al. 2018). Nevertheless, it should be noted that the spillover effect on the e-commerce platform may not be as pronounced as that on the mobile app platforms. On mobile app platforms, it is very common for customers to install multiple similar free apps (e.g., Google Voice and Skype). However, on e-commerce platforms, it is highly unlikely for a customer to buy multiple similar products from different stores at the same time. Simply put, unlike the mobile app platforms, the competition on e-commerce platform is largely exclusive. Therefore, the spillover effect, if present, is expected to be weaker on e-commerce platforms than on mobile app platforms.

Similar to the competition effect, the spillover effect is also more likely to play a role in the online channel than in the offline channel. On the one hand, because of the lower search cost, online customers of firstparty stores are more likely to find third-party stores selling similar products. On the other hand, unlike offline customers, the switching of online customers from first-party stores to third-party stores does not incur extra communication cost or transportation cost.

## 3.3. Disintermediation Effect

Third-party stores often join an online marketplace platform at a certain cost, including paying membership and/or commission fees and sharing their customers’ information with the platform (Jiang et al. 2011, Ryan et al. 2012, Kwark et al. 2017, Chen and Guo 2018). Under the threat that the first-party stores can steal their customers, third-party stores may encourage their customers to transact outside the platform to retain their customers. This defensive strategy, also known as disintermediation, is common on platforms that operate as intermediaries (Gu and Zhu 2020).

Contrary to the competition and spillover effects, the disintermediation effect is more likely to affect offline demand than online demand because offline orders are placed through offline communications, meaning that the third-party stores have a chance to persuade offline customers to transact outside the platform during the ordering process. On the other hand, disintermediating online customers requires the sellers to first reach out to the customers and then persuade them to cancel existing orders and to transact outside the platform, which incurs additional communication and transaction costs for both the sellers and the customers, not to mention the risk of sellers being caught and punished by the platform. In contrast, diverting offline customers only requires customers to pay directly (e.g., through WeChat or Alipay) instead of through the platform, which actually simplifies the payment process. Moreover, offline customers are likely to be more cooperative than online customers, because they might have established an offline relationship with the sellers. Therefore, the disintermediation effect is very plausible in the offline channel, but not likely in the online channel.

Table 1 summarizes the three mechanisms discussed previously and the channel(s) in which they may play a role. To facilitate interpretation, we explain the three mechanisms from the perspective of customer flow in the second column. The spillover effect refers to the phenomenon of new customers acquired by first-party stores later purchase from competing third-party stores. Here, new customers acquired by first-party stores are broadly defined as those who become aware of a product category through a first-party store. Because of the competition effect, third-party stores may lose both existing and prospective customers to the competing first-party stores. The disintermediation effect can lead to the exodus of customers from the platform. It should be noted that the primary focus of this paper is to figure out which mechanism is in play for which channel rather than comparing the effect sizes of each mechanism across the online and offline channels.

## 3.4. Heterogeneous Effects on Large vs. Small Third-Party Stores

The entry of the platform could have heterogeneous treatment effects on different third-party stores. In the online channel, because of information asymmetry, the reputation of online sellers plays an important role in customers’ decision process (Weiss et al. 1999, Chevalier and Mayzlin 2006). The reputation of small third-party stores is generally lower than that of large ones, as the performance of stores serves as a social cue for reputation (Pavlou and Gefen 2004, Zhu and Zhang 2010). Consequently, the online demand of large third-party stores may rely more heavily on reputation than that of small ones. With the entry of first-party stores, online customers who are concerned about reputation may purchase from firstparty stores instead of large third-party stores. On the other hand, if the attention spillover effect is in play in the online channel, larger third-party stores who are more representative of the product category (Li and Agarwal 2017) may capture a larger share of the attention spilled over from first-party stores. In this sense, larger third-party stores may also benefit more from the entry of first-party stores. Therefore, whether larger third-party stores suffer or benefit more from the platform entry depends on which of these two mechanisms (i.e., competition and spillover) plays a more important role in the online channel.

Table 1. Summary of Potential Mechanisms for Online and Offline Demand

<table><tr><td>Mechanism</td><td>Description</td><td>Impact on online vs. offline demand</td></tr><tr><td>Spillover effect (Li and Agarwal 2017, Foerderer et al. 2018)</td><td>New customers acquired by first-party stores later purchase from third-party stores</td><td>Spillover effect is more likely to influence online demand than offline demand:a. Lower search cost for online customersb. Lower switching cost for online customers</td></tr><tr><td>Competition effect (Jiang et al. 2011, Ryan et al. 2012, Zhu and Liu 2018)</td><td>1. Existing customers of third-party stores switch to first-party stores2. Potential new customers of third-party stores captured by first-party stores</td><td>Competition effect is more likely to influence online demand than offline demand:a. Lower search cost for online customersb. Lower switching cost for online customersc. Online customers rely more heavily on reputation and first-party stores have a reputation advantage</td></tr><tr><td>Disintermediation effect (Gu and Zhu 2020)</td><td>Third-party stores encourage customers to transact outside the platform</td><td>Disintermediation effect is more likely to influence offline demand than online demand:a. Offline orders are placed through offline communications, offering a chance to disintermediate in the ordering processb. Disintermediating online orders is both costly and riskyc. Potential offline relationships with offline customers</td></tr></table>

Compared with the online channel, the competition and spillover effects are less likely to be in play in the offline channel because of the high search and switching costs. However, as explained in Table 1, the disintermediation effect is expected to play a prominent role in the offline channel. Because larger thirdparty stores have to share the information of more offline customers for access to the same pool of customers on the platform, they have more offline customers to lose when they are forced to compete with the platform. In this sense, large third-party stores have stronger incentives to divert their offline customers away from the platform than small ones do (Gu and Zhu 2020). Consequently, in the offline channel, the demand of larger third-party stores may decrease more after the platform entry.

## 4. Empirical Analysis 4.1. Data

We investigate how the entry of first-party stores influences third-party stores’ demand using transactionlevel data from a large e-commerce platform in China. The platform was launched in November 2015 and primarily focuses on business-to-business transactions between wholesale stores and retailers, although they also support business-to-customers transactions (we do not distinguish business and individual customers in this study). Before the launch of the platform, the transactions between these wholesale stores and their customers typically took place offline. The mission of this platform is to provide an online marketplace to facilitate these transactions. Accordingly, every store on this online platform is backed by a physical wholesale store. Many of the stores were in operation offline long before they joined the platform and hence had already established their offline customer base. Joining the platform allows the stores to reach new customers nationwide. As of June 2019, the total value of transactions on this platform exceeded USD 85 billion.

One unique feature of this e-commerce platform is that it supports both online and offline orders for each store. Online orders are placed through the platform’s website or mobile app and must be paid before shipping, similar to other e-commerce platforms. Meanwhile, since there is a large demand for pay on delivery and some products sold in the physical stores are hard to be listed on the platform (e.g., products that do not fall into any predefined categories or products with nonstandard specifications), the platform also allows customers to order directly from the stores though offline interactions. Specifically, customers may order from a seller in person, over phone, or via text message and then pay through the platform upon delivery. Note that, to reduce the risk of not getting paid, a seller may decline phone or text message orders from unknown customers.

When customers order offline but pay through the platform, they are still eligible for any coupons offered by the store or the platform (all the coupons on the platform are based on order values, such as 20 off 100, are not attached to any specific products, and can be used by both online and offline customers). In addition, because the platform also offers financial services (e.g., loans) to sellers based on their sales data, sellers are incentivized to process offline orders through the platform, although they are not obligated to do so. For offline orders, the platform is only involved in the payment process and has no information about exactly what are ordered. Despite the support for offline orders, the platform has strict policies in place to prevent sellers from not fulfilling online orders or disintermediating online orders (i.e. persuading customers to cancel online orders and transact outside the platform).

Starting from August 12, 2016, the platform gradually opened first-party stores in several major cities in mainland China. Table 2 summarizes the information of eight first-party stores. Although the platform covers a wide range of products from more than 20 categories, such as home improvement, food, clothing, hotel supplies, baby products, beauty, outdoors and sports, and food and daily necessities, all but one first party stores sell products that fall into the general category of fast-moving consumer goods (FMCGs), such as purified water, soda, facial tissues, and biscuits. Because the FMCGs sold on the platform are typically from common brands, we do not expect the product quality of first-party stores to be any higher than that of competing third-party stores, although first-party stores generally offer richer choices. We also do not observe noticeable price difference between first-party and third-party stores for the same product. The platform strategically chose FMCGs because they can be sold quickly, and the platform has cost advantages because of the economy of scale. The entry decisions of the platform were not negotiated with the third-party stores.

Table 2. Details of First-Party Stores

<table><tr><td>Store ID</td><td>Launch date</td><td>Category</td><td>City</td></tr><tr><td>1</td><td>September 7, 2016</td><td>Clothing</td><td>Guangzhou</td></tr><tr><td>2</td><td>November 29, 2016</td><td>Food</td><td>Tianjin</td></tr><tr><td>3</td><td>August 12, 2016</td><td>Food and daily necessities</td><td>Zhengzhou</td></tr><tr><td>4</td><td>September 13, 2016</td><td>Food and daily necessities</td><td>Chengdu</td></tr><tr><td>5</td><td>September 6, 2016</td><td>Food and daily necessities</td><td>Kunming</td></tr><tr><td>6</td><td>December 15, 2016</td><td>Food and daily necessities</td><td>Changsha</td></tr><tr><td>7</td><td>August 26, 2016</td><td>Food and daily necessities</td><td>Yiwu</td></tr><tr><td>8</td><td>August 25, 2016</td><td>Food and daily necessities</td><td>Wuhan</td></tr></table>

Note. Except for the first store, all the other first-party stores focus on products that are FMCG.

Our data include all orders on the platform from February 25, 2016, through November 30, 2017. The information pertaining to each order includes the seller’s ID, the customer’s ID, the order creation time, the order value, the discount (if any), and so forth. In addition, we observe the joining date of each thirdparty store and the entry date of each first-party store. The data discussed previously allow us to compare the sales of third-party stores and the purchase behaviors of individual customers before and after entry.

Because the focal platform primarily focuses on business-to-business transactions, customers tend to purchase from local stores with which they may have offline connections.<sup>3</sup> Consequently, stores in different cities could face completely different business environments. Upon the platform owner’s entry in each city, we consider third-party stores located in the same city and selling products in the same category with the first-party store as the treated stores, because they are the ones most likely to be affected. At the same time, other stores located in the same city but selling products in other categories are considered as control stores. We identify the control and treated stores separately for the entry of each first-party store. We include a store in the treatment or control group only if the store has had at least one order before and after the entry date. We thus obtain 78 treated stores and 198 control stores.

To evaluate third-party stores’ demand before and after the first-party stores’ entries, we consider two dependent variables: the number of orders and the number of unique customers for each store in each month. Because the platform entry may have differential effects in the online and offline channels, we further split these numbers based on the transaction channel, online or offline. Given that the distributions of our dependent variables are highly skewed, we use the natural logarithms of the dependent variables in our analysis. Similar to a standard DID analysis, our key independent variables are the two dummy variables Treatment (whether a store is in the treatment group) and After (whether the current month is after the entry date). To investigate the potential heterogenous treatment effects on large versus small thirdparty stores, we use the pre-entry cumulative number of orders for each store as a moderating factor. In addition to the store and month level fixed effects, we also control for the age of each store (in months). The summary statistics of all the variables are reported in Table 3, and the correlations among these variables are provided in Table 4.

Table 3. Variable Descriptions and Summary Statistics

<table><tr><td>Variables</td><td>Descriptions</td><td>Observations</td><td>Mean</td><td>Standard deviation</td><td>Maximum</td><td>Minimum</td></tr><tr><td>Orders</td><td>Monthly number of orders</td><td>1,544</td><td>58.27</td><td>193.38</td><td>5,162</td><td>0</td></tr><tr><td>Online_Orders</td><td>Monthly number of online orders</td><td>1,544</td><td>22.44</td><td>168.17</td><td>5,161</td><td>0</td></tr><tr><td>Offline Orders</td><td>Monthly number of offline orders</td><td>1,544</td><td>35.83</td><td>101.45</td><td>1,722</td><td>0</td></tr><tr><td>Users</td><td>Monthly number of unique customers</td><td>1,544</td><td>17.33</td><td>78.18</td><td>2,618</td><td>0</td></tr><tr><td>Online_Users</td><td>Monthly number of unique online customers</td><td>1,544</td><td>8.08</td><td>72.87</td><td>2,618</td><td>0</td></tr><tr><td>Offline_Users</td><td>Monthly number of unique offline customers</td><td>1,544</td><td>9.48</td><td>30.25</td><td>612</td><td>0</td></tr><tr><td>Treatment</td><td>Whether a store is in the treatment group</td><td>276</td><td>0.28</td><td>0.45</td><td>1</td><td>0</td></tr><tr><td>After</td><td>Whether the month is after the entry date</td><td>1,544</td><td>0.51</td><td>0.50</td><td>1</td><td>0</td></tr><tr><td>Store_Age</td><td>Number of months since the store joined the platform</td><td>1,544</td><td>3.70</td><td>3.05</td><td>12</td><td>0</td></tr><tr><td>Cum Orders</td><td>Cumulative number of orders of a store pre-entry</td><td>276</td><td>133.72</td><td>239.07</td><td>1,427</td><td>1</td></tr></table>

Note. The statistics for Treatment and Cum\_Orders are summarized at the store level instead of the store-month level.

Table 4. Correlations among the Variables

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td></tr><tr><td>(1) Orders</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Online_Orders</td><td>0.85</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Offline_Orders</td><td>0.49</td><td>-0.03</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Users</td><td>0.84</td><td>0.83</td><td>0.22</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Online_Users</td><td>0.78</td><td>0.91</td><td>-0.03</td><td>0.92</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) Offline_Users</td><td>0.32</td><td>-0.03</td><td>0.65</td><td>0.37</td><td>-0.03</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(7) Treatment</td><td>0.05</td><td>0.12</td><td>-0.10</td><td>0.10</td><td>0.12</td><td>-0.04</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(8) After</td><td>0.05</td><td>0.07</td><td>-0.02</td><td>0.01</td><td>0.04</td><td>-0.08</td><td>-0.03</td><td>1.00</td><td></td><td></td></tr><tr><td>(9) Store_Age</td><td>0.01</td><td>-0.01</td><td>0.03</td><td>-0.04</td><td>-0.03</td><td>-0.03</td><td>-0.07</td><td>0.74</td><td>1.00</td><td></td></tr><tr><td>(10) Cum_Orders</td><td>0.30</td><td>0.13</td><td>0.35</td><td>0.25</td><td>0.11</td><td>0.38</td><td>0.05</td><td>-0.06</td><td>0.13</td><td>1.00</td></tr></table>

To provide intuition regarding the effect of platform entry on the demand of third-party stores, we aggregate the demand of the treated and control stores before and after platform’s entry. The results are illustrated in Figure 1. The demand of third-party stores drops substantially after entry, in terms of both the number of orders and the number of unique customers, whereas the demand of the control stores does not change significantly. Next, we analyze the impact of platform owner’s entry, using econometric models.

Figure 1. (Color online) Model-Free Analysis of the Effect of Platform Owner’s Entry  
(a)  
![](/api/attachments/WUUK8BPE/fulltext/images/1c016ce1ef48eef7024cc59f5e23ebffce4b4a014279fcc0b7e7b5580f13a96d.jpg)

(b)  
![](/api/attachments/WUUK8BPE/fulltext/images/37781084598cba982595e63268020f0ab8829c7cb77d4b35effbe0fbeb508d3a.jpg)

## 4.2. Empirical Model

Taking advantage of the sequential entries of the platform in different cities, we use a staggered DID model (Besley and Burgess 2004, Zhang and Zhu 2011, Greenwood and Wattal 2017) to estimate the effect of platform entry on the demand of competing third-party stores. We use sales data six months before and after the entry date of each first-party store for our empirical analysis. To obtain a clean treatment effect, we drop the sales of each store in the month when the corresponding first-party store was launched. The DID model for the store-level analysis is as follows:

$$
\begin{array}{c} y _ {i t} = \alpha_ {0} + \alpha_ {1} \times T r e a t m e n t _ {i} \times A f t e r _ {t} + \alpha_ {2} \times X _ {i t} + \delta_ {i} + \theta_ {t} \\ + \epsilon_ {i t}, \end{array}\tag{1}
$$

where $y _ { i t }$ represents the logarithm of the number of orders (or the number of unique customers) of store i in month t in the online and/or offline channel; Treatment indicates whether store i is in the treatment group (i.e., whether the store is in the same category and city as the first-party store); $A f t e r _ { t }$ indicates whether the platform has entered into the market by month $t ; X _ { i t }$ represents the time-varying variables of store $i ,$ such as its age; $\delta _ { i }$ and $\theta _ { t }$ represent store and month level fixed effects, respectively, which control for the effects of the observable and unobservabl time-invariant characteristics of stores and potential temporal shocks; and $\alpha _ { 1 }$ is the coefficient of interest in this model. We allow the error terms for the same store to be arbitrarily correlated (i.e., we use robust standard errors clustered by store), which accounts for potential serial correlations (Bertrand et al. 2004).

To explore the potential heterogeneous treatment effects of platform entry on stores of different sizes, we also consider a difference-in-difference-in-differences (DDD) model (Bertrand et al. 2004, Greenwood and Wattal 2017)

that includes a three-way interaction on the store’s cumulative orders before the platform’s entry, which is a time-invariant proxy for store size. The DDD model is

$$
\begin{array}{r l} & y _ {i t} = \alpha_ {0} + \alpha_ {1} \times T r e a t m e n t _ {i} \times A f t e r _ {t} \\ & \quad + \alpha_ {2} \times C u m \_ O r d e r s _ {i} \times A f t e r _ {t} \\ & \quad + \alpha_ {3} \times T r e a t m e n t _ {i} \times C u m \_ O r d e r s _ {i} \times A f t e r _ {t} \\ & \quad + \alpha_ {4} \times X _ {i t} + \delta_ {i} + \theta_ {t} + \epsilon_ {i t}, \end{array}\tag{2}
$$

where α is the coefficient of interest. Because Cum Orders and Treatment are both time invariant, their interaction is not identified in this equation with storelevel fixed effects.

## 4.3. Main Results

The effects of platform entry on the overall demand of treated third-party stores, in terms of the number of orders and the number of unique customers, estimated using the DID model are reported in columns 1 and 2 of Table 5. Compared with control stores, the number of orders and the number of unique customers both decrease significantly after the platform entry. The substantial decrease in the demand of treated stores lends support to the existence of the competition/disintermediation effect but not the existence of the spillover effect. Put differently, our finding suggests that the spillover effect, if any, is dominated by the competition and/or disintermediation effect.

Although prior studies in the context of mobile app platform have found that the entry of the platform can boost the demand of competing third-party apps (Li and Agarwal 2017, Foerderer et al. 2018), the effect of platform entry is negative in our context. This finding demonstrates that the impact of platform entry is context dependent. In mobile app platforms, the apps are typically free, making it possible for customers to install multiple apps with similar functionalities. However, the products sold on e-commerce platforms are rarely free, indicating that customers are unlikely to purchase multiple similar products from different stores. The exclusive nature of purchasing behavior on e-commerce platform implies that the competition effect may well outweigh the spillover effect.

As we discussed in Section 3, the mechanisms at work for the online and offline channels are likely to be different. Specifically, the competition effect is more likely to influence online demand, whereas the disintermediation effect is more likely to influence offline demand. Consequently, the platform entry may have differential effects on online and offline demand. To investigate this possibility, we also estimate the effect of platform entry on the online and offline demand of treated third-party stores separately. The results are summarized in columns 3–6 of Table 5. We find that the offline demand of treated stores decreases significantly after the entry of the platform, whereas the online demand of treated stores does not change significantly.

Because the dependent variables are transformed logarithmically and the interaction term Treatment × After is a binary variable, the predicted demand of a treated store after the platform entry will be the counterfactual demand in the absence of the entry multiplied by a scalar $e ^ { \alpha _ { 1 } }$ , where $\alpha _ { 1 }$ is the coefficient of Treatment $\times \ A f t e r$ . Therefore, the proportional decrease in demand due to platform entry can be computed as $( 1 - e ^ { \alpha _ { 1 } } ) ^ { * } 1 0 0 \%$ . Based on the coefficients of Treatment × After in columns 3 and $^ { 4 , }$ the numbers of offline orders and customers for treated third-party stores decrease by 49% and 50%, respectively, because of the platform entry. This finding suggests that about one half of the offline demand for treated third-party stores diminishes because of the platform entry, which might severely undermine the ecosystem of the platform.

Table 5. Impact of Platform Owner’s Entry on Different Types of Transactions

<table><tr><td rowspan="2"></td><td colspan="2">All</td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td><td>(5) Orders</td><td>(6) Users</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.722**(0.319)</td><td>-0.790***(0.274)</td><td>-0.673**(0.316)</td><td>-0.684***(0.241)</td><td>-0.303(0.212)</td><td>-0.281*(0.170)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-0.338(0.233)</td><td>-0.180(0.176)</td><td>-0.529**(0.242)</td><td>-0.406**(0.162)</td><td>0.148(0.144)</td><td>0.024(0.111)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.072</td><td>0.078</td><td>0.107</td><td>0.122</td><td>0.056</td><td>0.041</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level. In Online Appendix A, we show that the findings hold even after controlling for the promotion activity and service quality of third-party stores, which third-party stores might change in response to platform entry. The coefficient of store age is significantly negative for the offline demand but not significant for the online demand. This finding will be explained in the note of Table 10 \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

The significant decrease in offline demand can be well explained by the disintermediation effect, given that our discussion in Section 3 suggests that thirdparty stores are incentivized to divert their offline customers away from the platform. With that being said, the previous results are not sufficient to rule out the possibility that the decrease is driven by the competition effect, although the competition effect is unlikely in the offline channel because of the high search and switching costs. The insignificant change in online demand suggests that the competition effect is weak, or strong but cancelled out by the spillover effect. To better understand the mechanisms underlying our findings, next we run a series of additional analyses to identify the most plausible explanations for our findings.

## 4.4. Mechanisms

As we discussed in Section 3, the entry of first-party stores may affect the demand of third-party stores through three mechanisms: the competition effect, the spillover effect, and the disintermediation effect. In this section, we conduct a series of analyses from different perspectives to figure out which mechanism(s) are likely to be in effect in the online and offline channels, respectively.

4.4.1. Competition Effect. To investigate whether the competition effect is at work, we analyze the origins of first-party stores’ customers and see how many of them are switched from treated third-party stores. To minimize the possibility of false rejection for the competition effect, we loosely define any former customer of third-party stores who later makes at least one purchase from the competing first-party stores as switched, even though she may keep purchasing from the third-party stores. Apparently, the number of switched customers will be overestimated under this definition, but it allows us to provide an upper bound estimate about the level of switching. Table 6 summarizes the numbers (percentages) of first-party stores’ online and offline customers who are former customers of the competing (treated) thirdparty stores and the numbers (percentages) of orders contributed by these customers.

Even under our loose definition of switching, only 76 former offline customers of treated third-party stores switched to first-party stores, which only accounts for 2.8% of all the 2,763 customers (online and offline) of first-party stores. The number of orders made by these customers (i.e., 660) only amounts to about 2.3% of all the 28,440 orders on the first-party stores. This finding suggests that the percentage of first-party stores’ offline customers coming from treated third-party stores is negligible. From the perspective of treated third-party stores, only 76 of their 1,987 (3.8%) offline customers (pre-entry) switched to first-party stores after the platform entry, which cannot explain the 50% decline in treated stores’ offline customers. These statistics rule out the possibility that the decrease in offline demand is driven by the defection of existing customers.

In contrast, 783 (28.3%) of first-party stores’ 2,763 customers (online and offline) used to be online customers of treated third-party stores, which is consistent with our earlier argument that the competition effect is more likely to be effective in the online channel because of the lower search cost, the lower switching cost, and the stronger reliance on reputation (Table 1). Nevertheless, it should be noted that 28.3% is an upper bound estimate of the proportion of switched customers. In sum, the analysis on customer origins suggests that the role of the competition effect is weak in the offline channel but seems to be noticeable in the online channel.

4.4.2. Spillover Effect. The launch of first-party stores may attract new customers for the products sold at first-party stores, and these new customers may spil over to third-party stores selling similar products. As opposite to the competition effect that captures the flow of customers from treated third-party stores to first-party stores, the spillover effect refers to the flow of customers from first-party stores to treated thirdparty stores. If the spillover effect is in play, the numbers of new customers for treated third-party stores are expected to increase after the platform entry, in the absence of the competition and disintermediation effects. In an endeavor to test the potential spillover effect, we estimate how the numbers of new and old customers of third-party stores change with platform entry using the DID model, respectively, for the online and offline channels. The results are reported in Table 7.

Table 6. Breakdown of First-Party Stores’ Customers and Orders

<table><tr><td rowspan="2"></td><td colspan="3">No. customers</td><td colspan="3">No. orders</td></tr><tr><td>All</td><td>Offline</td><td>Online</td><td>All</td><td>Offline</td><td>Online</td></tr><tr><td>All customers of first-party stores</td><td>2,763</td><td>379</td><td>2,526</td><td>28,440</td><td>8,400</td><td>20,040</td></tr><tr><td>Former offline customers of treated third-party stores</td><td>76 (2.8%)</td><td>7 (1.8%)</td><td>75 (3.0%)</td><td>660 (2.3%)</td><td>8 (0.1%)</td><td>652 (3.3%)</td></tr><tr><td>Former online customers of treated third-party stores</td><td>783 (28.3%)</td><td>14 (3.7%)</td><td>782 (31.0%)</td><td>5,756 (20.2%)</td><td>43 (0.5%)</td><td>5,713 (28.5%)</td></tr></table>

Notes. The percentages of treated third-party stores’ former customers are reported in parentheses. A former customer of a third-party store means customer who had purchased from the third-party store before the entry. A customer can be an online and offline customer at the same time.

The results in Table 7 suggest that the number of new customers of treated third-party stores decreases after the launch of first-party stores, both online (significant) and offline (marginally significant). This finding demonstrates that the spillover effect, if any, is dominated by the competition and/or the disintermediation effect. In the online channel, the spillover effect is more likely to be dominated by the competition effect than by the disintermediation effect, because it is costly for stores to persuade new online customers to transact outside of the platform (doing so requires reaching out to the customers and persuading them to cancel the placed online orders, not to mention the risk of getting caught by the platform). In the offline channel, the decrease in the number of new customers is very likely to be driven by the disintermediation effect, given that the extent of competition in the offline channel is expected to be weak because of geographical constraints (the analysis in Section 4.4.1 provides evidence for this by showing that no more than 3.8% of treated third-party stores offline customers switched to first-party stores).

Moving on to old customers, we find that the number of old customers of treated stores in the offline channel decrease significantly after the platform entry and the effect size is larger than that of new customers in the offline channel. This finding is not that surprising as it is easier to divert old offline customers, with whom the stores have prior offline interactions, than to divert new offline customers. Conversely, in the online channel, we find that the decrease in the number of old customers is insignif icant and also much smaller in magnitude than the decrease in the number of new customers. One plausible explanation is that old customers who have purchased from third-party stores may have established trust in them and hence less likely to switch to first-party stores given that the prices of the products at first-party and third-party stores are comparable.

Table 7. Impact of Platform Owner’s Entry on Numbers of New and Old Customers

<table><tr><td rowspan="2"></td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) New</td><td>(2) Old</td><td>(3) New</td><td>(4) Old</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.355*(0.191)</td><td>-0.591***(0.210)</td><td>-0.308**(0.154)</td><td>-0.082(0.154)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-0.548***(0.126)</td><td>-0.122(0.155)</td><td>-0.136(0.097)</td><td>0.193*(0.100)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.167</td><td>0.094</td><td>0.050</td><td>0.042</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level. The results using the numbers of orders from new and old customers are highly consistent and are available from the authors on request.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

4.4.3. Disintermediation Effect. Because of the competition from first-party stores, third-party stores may adopt the disintermediation strategy to protect their customer base. Specifically, they may divert their customers away from the platform by encouraging them to transact outside the platform. A direct consequence of disintermediation is that the demand from those diverted customers will vanish from the platform, in opposition to the competition and spillover effects that only redistribute the demand within the platform. Had treated third-party stores taken the disintermediation strategy, the purchase activities of their past customers on the platform would decrease. To test whether the disintermediation strategy is used, we further analyze customers’ purchase activities before and after entry in an alternative DID setting at the customer level.

In this DID analysis, we focus on customers who had placed at least one order from a treated or control third-party store prior to the entry of the respective first-party store. We view customers who placed at least one order in any treated third-party store as treated customers and all the rest as control cus tomers. The treatment time of a customer is the entry time of the respective first-party store. If a customer purchased from multiple treated third-party stores, we use the earliest entry time as the treatment time Because the customers’ activities are sparse on a monthly basis, we aggregate their orders into two periods (i.e., before and after entry). Such an aggregation could also mitigate the issues of serial correlation and grouped error terms (Bertrand et al. 2004, Manchanda et al. 2015). Because the characteristics of treated and control customers differ substantially, the comparison between the two groups may not be particularly meaningful. To obtain comparable statistics on relevant observable covariates, we use propensity score matching to find a comparable control customer for each treated customer, using pretreatment data (Stuart 2010). The demographics and consumption patterns between the customers in the treatment and control groups are not significantly different after the matching. See Online Appendix B for details on the matching process.

Other than the aggregation and the matching processes, our customer-level DID analysis is largely the same as the store-level DID analysis. The dependent variable is the total number of orders made by each customer before the entry and six months after the entry, which include orders in both first-party and third-party stores. To investigate the potential differential effects of platform entry on a customer’s online and offline purchases, we also divide the orders by transaction channel. The results of all the customer-level analyses are provided in Table 8.

The result in first column of Table 8 suggests that the overall purchase activities of treated customers decrease significantly after the platform entry, for which the only plausible explanation is the disintermediation effect, as neither the competition effect nor the spillover effect can lead to a decrease in a customer’s overall demand. Therefore, the customer level DID analysis provides strong support for the existence of the disintermediation effect, indicating that third-party stores have indeed diverted their customers away from the platform. Examining the results of the second and third columns, we find that treated customers’ offline purchase activities decrease substantially, whereas their online purchase activities remain basically the same. This finding suggests that the decrease in overall purchase activities is driven by the disintermediation in the offline channel, which is not surprising as disintermediation is both costly and risky in the online channel.

4.4.4. Summary of Analyses on Mechanisms. Table 9 summarizes the findings from the empirical analyses in Section 4.4, as well as what they inform us about the underlying mechanisms. To sum up, we rule out the competition effect in the offline channel and provide convincing evidence that the decrease in the offline demand is driven by the disintermediation effect.

In addition, the competition effect is at work in the online channel, at least for new customers. Moreover, there is no direct evidence to support the existence of the spillover effect. The spillover effect, if any, is either dominated by the competition effect or the disintermediation effect.

## 4.5. Heterogeneous Treatment Effects

To investigate the potential heterogeneous effects of platform entry on treated third-party stores of different sizes, we estimate the DDD model as discussed in Section 4.2, where we use each third-party store’s pre-entry cumulative number of orders as a proxy of its size. The advantage of using pre-entry sales is that it cannot be affected by the entry of the platform.<sup>4</sup> The results are summarized in the Table 10.

In columns 1 and 2, the negative coefficients of the three-way interaction suggest that the overall demand of larger third-party stores decreases more with the platform entry, in terms of both the number of orders and the number of unique customers. Breaking down the demand into online and offline demand, we find that the three-way interaction is (marginally) significant for offline demand, but small and insignificant for online demand. This heterogeneity can be well explained by the disintermediation effect. That is, larger third-party stores are more incentivized to disintermediate when forced to compete with the platform, and the resulting demand decrease is limited to the offline channel because disintermediation is difficult in the online channel.

The heterogeneity, if driven by the competition effect, is expected to be more pronounced in the online channel than in the offline channel, because our theoretical discussions (Section 3) and empirical analyses (Section 4.4) both suggest that the competition effect is more likely to be in play in the online channel. Apparently, the heterogeneity is not driven by the positive spillover effect either. Prior studies in the literature suggest that, when the spillover effect is at work, the demand of larger third-party stores increase (rather than decrease) more after the platform entry (Li and Agarwal 2017, Foerderer et al. 2018).

Table 8. Impact of Platform Owner’s Entry on Customer Purchase Activities

<table><tr><td></td><td>(1) Orders</td><td>(2) Offline orders</td><td>(3) Online orders</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.179**(0.035)</td><td>-0.249***(0.026)</td><td>0.006(0.028)</td></tr><tr><td> $After_{t}$ </td><td>-0.762***(0.027)</td><td>-0.462***(0.022)</td><td>-0.310***(0.021)</td></tr><tr><td>User-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.234</td><td>0.190</td><td>0.053</td></tr><tr><td>Number of users</td><td>4,044</td><td>4,044</td><td>4,044</td></tr><tr><td>Number of observations</td><td>8,088</td><td>8,088</td><td>8,088</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level. The effect of After is identified, because we use a two-period DID model with no month-level fixed effects. The negative coefficient of After is likely driven by the attrition of customers over time. In Online Appendix C, we show that the results are similar when the control customers are matched more loosely with the treated customers  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 9. Empirical Findings and Plausible Mechanisms

<table><tr><td>Analysis</td><td>Focus</td><td>Finding</td><td>Discussion on Mechanisms</td></tr><tr><td>Table 6</td><td>Competition</td><td>2.8% (28.3%) of first-party stores&#x27; customers are former offline (online) customers of third-party stores</td><td>1. The competition effect is negligible for third-party stores&#x27; existing customers in the offline channel2. The competition effect is plausible for third-party stores&#x27; existing customers in the online channel</td></tr><tr><td>Table 7</td><td>Spillover</td><td>Both online and offline orders from new customers decrease significantly after platform entry</td><td>3. The spillover effect, if any, is dominated by the competition effect or disintermediation effect3.1. In the online channel, the spillover effect is likely to be dominated by the competition effect as disintermediating new online customers is costly and risky3.2. In the offline channel, the spillover effect is likely to be dominated by the disintermediation effect, because the competition effect is less plausible in the offline channel due to geographical constraints (evident by point #1 above)</td></tr><tr><td>Table 8</td><td>Disintermediation</td><td>Treated customers&#x27; total demand and offline demand decrease significantly after platform entry</td><td>4. The decrease in the overall demand of treated customers lends support to the disintermediation effect, as neither the spillover effect nor the competition effect can lead to a reduction in customers&#x27; overall demand</td></tr></table>

If the heterogeneous treatment effects indeed result from the disintermediation of offline customers, one would expect the offline demand of third-party stores with more offline demand to decrease more, but not for those with more online demand. To verify this possibility, we divide the pre-entry cumulative number of orders of each third-party store into two parts: cumulative offline orders and cumulative online orders. We then investigate how the treatment effect varies with the cumula tive offline orders and cumulative online orders in the two channels, respectively. The results are reported in Table 11.

Table 10. Heterogeneous Treatment Effects on Stores of Different Sizes

<table><tr><td rowspan="2"></td><td colspan="2">Overall</td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td><td>(5) Orders</td><td>(6) Users</td></tr><tr><td> $Treatment_{i} \times After_{t} \times Cum\_Orders_{i}$ </td><td>-0.267**(0.126)</td><td>-0.339***(0.101)</td><td>-0.267*(0.140)</td><td>-0.285***(0.105)</td><td>-0.081(0.116)</td><td>-0.097(0.084)</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>0.410(0.367)</td><td>0.598*(0.323)</td><td>0.463(0.376)</td><td>0.485*(0.281)</td><td>0.027(0.358)</td><td>0.119(0.278)</td></tr><tr><td> $After_{t} \times Cum\_Orders_{i}$ </td><td>-0.247***(0.077)</td><td>-0.159***(0.059)</td><td>-0.253***(0.077)</td><td>-0.141**(0.057)</td><td>-0.040(0.041)</td><td>-0.047(0.032)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-0.684***(0.223)</td><td>-0.451***(0.163)</td><td>-0.881***(0.231)</td><td>-0.641***(0.155)</td><td>0.081(0.145)</td><td>-0.056(0.114)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.120</td><td>0.139</td><td>0.156</td><td>0.180</td><td>0.060</td><td>0.052</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables and the independent variable $C u m \_ O r d e r s _ { i t }$ are transformed logarithmically. Standard errors are clustered at the store level. In line with Table 5, the coefficient of store age is significantly negative for the offline demand but not significant for the online demand. This finding can be explained by the natural disintermediation of third-party stores in the offline channel. That is, over time, some unsuccessful third-party stores become less motivated to process their offline orders through the platform, leading to a decline in the average offline demand of all third-party stores. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

Table 11. Heterogeneous Treatment Effects on Stores Relying on Offline vs. Online Orders

<table><tr><td rowspan="2"></td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.106(0.348)</td><td>0.100(0.303)</td><td>-0.080(0.301)</td><td>0.150(0.304)</td></tr><tr><td> $Treatment_{i} \times After_{t} \times Cum\_Offline\_Orders_{i}$ </td><td>-0.301**(0.116)</td><td>-0.288***(0.087)</td><td>0.049(0.073)</td><td>0.013(0.066)</td></tr><tr><td> $Treatment_{i} \times After_{t} \times Cum\_Online\_Orders_{i}$ </td><td>0.203(0.123)</td><td>0.096(0.104)</td><td>-0.106(0.142)</td><td>-0.110(0.099)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-1.185***(0.221)</td><td>-0.516***(0.176)</td><td>0.079(0.151)</td><td>0.138(0.148)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.190</td><td>0.212</td><td>0.080</td><td>0.096</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables and online, offline cumulative number of orders are transformed logarithmically. Standard errors are clustered at the store level.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

The results in Table 11 are exactly consistent with our reasoning. Specifically, in the offline channel, the three-way interaction on cumulative offline orders is significant and negative, whereas the three-way interaction on cumulative online orders is not significant. In addition, neither three-way interaction is significant in the online channel. These findings demonstrate that third-party stores respond to the platform entry based on the size of their offline demand, rather than the size of their online demand, and their response is limited to the offline channel, lending support to the disintermediation mechanism that concentrates on offline customers.

Although prior studies on the mobile app platforms show that the platform entry has a larger demand spillover effect on larger complementors (Li and Agarwal 2017, Foerderer et al. 2018), we find exactly the opposite in our context. This finding suggests that the positive spillover effect may result from the special nature of the mobile app platform, namely, the products (i.e., apps) are typically free. Our study using data from an e-commerce platform provides empirical evidence that the platform entry may instead lead to disintermediation when products are not free.

## 5. Robustness Checks

## 5.1. Parallel Trend Assumption

One fundamental assumption underlying the DID analysis is that, in the absence of treatment, the difference between the control group and the treatment group is constant over time, which is also known as the parallel trend assumption (Abadie 2005, Angrist and Pischke 2008). Violation of this assumption can lead to biased estimates. This assumption is generally not testable because the counterfactual posttreatment outcome of the treatment group is not observed. However, it is still possible to test whether this assumption holds pretreatment, using the DID model with leads and lags (Autor 2003, Lu et al. 2019). In doing so, we interact the Treatment dummy with the leads and lags of the After dummy. If the parallel trend assumption is valid, the interaction with the leads should be insignificant. Figure 2 illustrates the estimated coefficients of these interactions for both of our dependent variables (i.e., monthly numbers of orders and users).<sup>5</sup> In either case, none of the pretreatment interactions is significant, which is consistent with the parallel trend assumption. In addition to the test on the overall demand, we further test the parallel trends for the online and offline demand separately and do not find significant differences between the treated and control third-party stores’ pre-entry trends in either case.

## 5.2. Synthetic Control Method

Another issue that could undermine the validity of our findings is that the effect of confounders can change over time. To alleviate this concern, we use a data-driven procedure to construct a comparable control store for each treated store by weighting all available control stores, namely, the synthetic control method (Abadie et al. 2010). This method can account for potential time-varying confounders by allowing the individual level fixed effects to change over time. Here, we employ a generalized synthetic control method that can handle unbalanced panel data and multiple treatments at different time points (Xu 2017). However, one limitation of the generalized synthetic control method is that it requires a relatively long series before the treatment to construct synthetic controls, which results in very limited observations in the treatment group. Table 12 summarizes the results from the generalized synthetic control method.

Figure 2. (Color online) Test of the Parallel Trend Assumption  
(a)  
![](/api/attachments/WUUK8BPE/fulltext/images/87304ce809cfe8f5b971ce09ac6687cc173d69c2824410ce5ebe100ae743b009.jpg)

(b)  
![](/api/attachments/WUUK8BPE/fulltext/images/8d648759e9cc99952f5e3b3f94852eae1add238ef78bbf69e4a6e4f970be8cc0.jpg)

The results in Table 12 are consistent with those in Table 5, which mitigates the concern that our results could be driven by time-varying confounders. To provide a more intuitive understanding of the treatment effect, we illustrate the actual and counterfactual demand of treated stores over time in Figure 3. The red solid line represents the average actual demand and the blue dashed line represents the average predicted demand in the absence of platform entry (i.e., counterfactual demand). The actual demand of the treated stores is clearly lower than their counterfactual demand.

## 5.3. Alternative Measure for Demand

In our main analysis, we use the number of orders and the number of unique customers per month to measure demand. In addition to these two variables, sales revenue is also a common measure for demand Table 13 reports the results of the DID analysis using the logarithmically transformed monthly sales revenue as the dependent variable. In line with our earlier findings, the results suggest that the total and offline sales revenue of treated third-party stores decrease (marginally) significantly after the platform entry. Therefore, our findings are robust to alternative measures for demand.

Table 12. Impact of Platform Owner’s Entry Using the Generalized Synthetic Control Method

<table><tr><td></td><td>(1) Orders</td><td>(2) Users</td></tr><tr><td> $Treatment_i \times After_t$ </td><td>-1.128***(0.354)</td><td>-1.296***(0.248)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of treated stores</td><td>10</td><td>10</td></tr><tr><td>Number of control stores</td><td>194</td><td>194</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are produced by 1,000 bootstraps blocked at the store level.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

## 5.4. Alternative Measure of Platform Entry

If the observed reduction in treated third-party stores total (offline) sales is caused by the entry of first-party stores, we would expect a larger reduction in sales for treated third-party stores competing with a larger first-party store. To test this possibility, we construct a continuous variable to measure the treatment.<sup>6</sup> Specifically, we use the log-transformed cumulative orders of the first-party store before each month as the

Table 13. Impact of Platform Owner’s Entry on Sales Revenue

<table><tr><td></td><td>(1) All</td><td>(2) Offline</td><td>(3) Online</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-1.167*(0.686)</td><td>-1.442*(0.809)</td><td>-0.507(0.457)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-1.954***(0.542)</td><td>-2.383***(0.647)</td><td>0.0686(0.350)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.084</td><td>0.113</td><td>0.084</td></tr><tr><td>Number of stores</td><td>255</td><td>255</td><td>255</td></tr><tr><td>Number of observations</td><td>1,418</td><td>1,418</td><td>1,418</td></tr></table>

Notes. To mitigate the influence of outliers, we remove the top 5% stores whose average transaction values are more than 15 times higher than the median average transaction value of all stores. The results are similar when we remove the top 10% stores instead. The results of customer-level analysis also remain consistent when we use sales revenue as the dependent variable

$$
^ {*} p <   0. 1; ^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

(a)

Figure 3. (Color online) Actual vs. Counterfactual Demand: (a) Number of Orders (Log Scale) and (b) Number of Unique Customers (Log Scale)  
![](/api/attachments/WUUK8BPE/fulltext/images/81e567aeff970984775c9d7b9d1515bb2ab2961e599bcc27f0cfff92eb56f94b.jpg)

(b)  
![](/api/attachments/WUUK8BPE/fulltext/images/9a0243040d20fd7a24bcbaeaa281946456fc70097c3131a9a09705ef0d4c5012.jpg)

treatment variable. Since this continuous treatment variable is zero before the platform entry, there is no need to interact it with the After dummy. The results using the continuous treatment variable are provided in Table 14. The significantly negative coefficient of this alternative treatment measure confirms that the total (offline) sales of treated third-party stores decrease with the sales of the competing first-party stores. Therefore, our findings are robust to this alternative measure of treatment.

## 5.5. Alternative Measure of Store Size

In Table 10, we use a third-party store’s cumulative number of orders before the platform entry to measure its size. The results using this continuous measure seem to imply that platform entry could have a positive effect on small third-party stores whose sales are close to zero. To test whether this is true, we use a binary variable Large<sub>i</sub> to indicate whether store i is large or not. Specifically, Large equals one if the thirdparty store’s cumulative number of orders before the entry of the respective first-party store is among the top 25% of all third-party stores and zero otherwise.<sup>7</sup> The results using this binary measure for store size are reported in Table 15. The results demonstrate that the offline demand of large third-party stores decrease significantly after the platform entry, whereas the offline demand of small third-party stores does not change significantly. Therefore, small treated thirdparty stores do not benefit from the platform entry.

## 5.6. Permutation Tests

A potential caveat of our analysis is that the treated stores are limited to a few categories. Specifically, seven of the eight first-party stores focus on FMCGs (Table 2). It is possible that the demand for products in this category decreases over time, leading to decreased sales of the treated stores. If the treatment effect is indeed driven by a declining trend in this category, we should obtain similar results when we shift the entry time of the platform. Table 16 summarizes the results when we shift the entry time to three months before and after the actual entry time for each first-party store. The coefficient of the interaction term is not significant in either analysis. Therefore, our findings are unlikely to be driven by a trend in certain product categories.

Table 14. Results Using a Continuous Measure of Platform Entry

<table><tr><td rowspan="2"></td><td colspan="2">Overall</td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td><td>(5) Orders</td><td>(6) Users</td></tr><tr><td> $log(Cum\_First\_Party\_Orders)_{it}$ </td><td>-0.137**(0.064)</td><td>-0.161***(0.061)</td><td>-0.141**(0.062)</td><td>-0.135***(0.051)</td><td>-0.082(0.058)</td><td>-0.090*(0.048)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.071</td><td>0.077</td><td>0.107</td><td>0.119</td><td>0.059</td><td>0.050</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

In addition to shifting the entry time, an alternative way to test the robustness of our findings is to shuffle the treatment status of stores (Bertrand et al. 2004, Greenwood and Wattal 2017). This permutation test allows us to assess if the treatment effect is observed by chance. We randomly label 78 of the stores as treated stores (and consider the rest control ones) and re-estimate the DID model at the store level. We repeat this process 1,000 times and find that the average treatment effect is not statistically different from zero

## 5.7. Additional Analyses

In addition to the robustness checks discussed previously, we also conducted several additional analyses to further illustrate the robustness of our findings.

5.7.1. Seemingly Unrelated Regression. There are mul tiple dependent variables in our analyses and their error terms could be correlated. Ignoring correlations in error terms can lead to inefficient estimates (Zellner 1962). To incorporate the potential correlations among the error terms, we re-estimate our models using seemingly unrelated regression and the point estimates remain the same, whereas the standard errors become slightly smaller. This finding suggests that the correlations between the error terms of different dependent variables, if any, will only make the findings in our main model more conservative.

Table 15. Heterogeneous Treatment Effects on Large and Small Stores

<table><tr><td rowspan="2"></td><td colspan="2">Overall</td><td colspan="2">Offline</td><td colspan="2">Online</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td><td>(5) Orders</td><td>(6) Users</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.103(0.242)</td><td>-0.179(0.228)</td><td>-0.115(0.223)</td><td>-0.219(0.174)</td><td>-0.120(0.191)</td><td>-0.085(0.165)</td></tr><tr><td> $Treatment_{i} \times After_{t} \times Large_{i}$ </td><td>-1.538***(0.592)</td><td>-1.571***(0.493)</td><td>-1.344**(0.639)</td><td>-1.165**(0.497)</td><td>-0.508(0.505)</td><td>-0.524(0.381)</td></tr><tr><td> $Large_{i} \times After_{t}$ </td><td>-0.789**(0.343)</td><td>-0.502*(0.270)</td><td>-0.930***(0.342)</td><td>-0.540**(0.252)</td><td>0.050(0.197)</td><td>-0.049(0.144)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-0.618***(0.220)</td><td>-0.389**(0.168)</td><td>-0.834***(0.223)</td><td>-0.603***(0.153)</td><td>0.134(0.148)</td><td>-0.016(0.117)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.118</td><td>0.132</td><td>0.156</td><td>0.173</td><td>0.059</td><td>0.049</td></tr><tr><td>Number of stores</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td><td>276</td></tr><tr><td>Number of observations</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td><td>1,544</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table 16. Permutation Test by Shifting the Treatment Time

<table><tr><td rowspan="2"></td><td colspan="2">Three Months Earlier</td><td colspan="2">Three Months Later</td></tr><tr><td>(1) Orders</td><td>(2) Users</td><td>(3) Orders</td><td>(4) Users</td></tr><tr><td> $Treatment_{i} \times After_{t}$ </td><td>-0.231(0.305)</td><td>-0.285(0.255)</td><td>-0.130(0.221)</td><td>-0.268(0.233)</td></tr><tr><td> $Store\_Age_{it}$ </td><td>-1.258**(0.631)</td><td>-0.239(0.435)</td><td>-0.007(0.165)</td><td>-0.060(0.154)</td></tr><tr><td>Store-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-level fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^{2}$ </td><td>0.103</td><td>0.079</td><td>0.083</td><td>0.063</td></tr><tr><td>Number of stores</td><td>102</td><td>102</td><td>285</td><td>285</td></tr><tr><td>Number of observations</td><td>582</td><td>582</td><td>2,089</td><td>2,089</td></tr></table>

Notes. The dependent variables are transformed logarithmically. Standard errors are clustered at the store level. Many stores drop out of the data set when we move the treatment time three months ahead because they were not open yet at that time.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

5.7.2. Observation Window. In the main analysis, we use the data six months before and after each entry. Other than the platform entries, there could be other unobserved events during this one-year window. To alleviate this concern, we reduce the pretreatment period and/or the posttreatment period to three months and re-estimate the DID model. The results are very similar to those of our main analysis (see Online Appendix D). Therefore, our results are unlikely to be an artifact of unobserved events.

5.7.3. Information Leakage. Finally, to account for the potential information leakage (i.e., third-party stores may anticipate the later entry events based on prior entry events and respond to later entries in advance), we run an additional analysis in which we use the entry date of the first first-party store as the entry time for all first-party stores and the results remain consistent (see Online Appendix E).

## 6. Conclusions

Platform owners often enter into complementary markets to appropriate value from complementors or to improve the quality of products on the platforms (Zhu and Liu 2018). However, the entry is a doubleedged sword that could end up hurting the platforms by crowding out complementors. This paper makes a first attempt to empirically evaluate the impact of platform entry on the demand of third-party stores on an e-commerce platform. Contrary to previous studies on mobile app platforms, we show that, after the entry of first-party stores, the demand of competing third-party stores decreases. In addition, we find that the decrease in the overall demand of third-party stores results from the decrease in offline demand, instead of the decrease in online demand. Our furthe analyses suggest that the decreased offline demand is driven by third-party stores’ defensive strategy to divert their offline customers away from the platform (i.e., disintermediation), rather than the defection of customers (i.e., competition). Finally, we find that the offline demand declines more for third-party stores who have more offline sales pre-entry, because they have more offline customers to lose had they not used the disintermediation strategy.

Our findings have important implications for both platform managers and third-party sellers. Platforms should carefully evaluate the nature of their markets before entering into the market to compete with complementors. When the competition between firstparty and third-party sellers are nonexclusive (e.g., mobile app platforms), the entry of the platform can be beneficial because of the spillover effect. However, when the competition is exclusive (e.g., e-commerce platforms), the platform entry can lead third-party sellers to disintermediate. In such a case, the platform entry is particularly risky because our results show that it may drive out large third-party sellers first. From the perspective of third-party sellers, the platform entry is not necessarily a threat. In our analysis, we find that the online demand of third-party sellers is not significantly affected by platform entry, suggesting that the disintermediation strategy could be an overreaction.

This work has its limitations. One limitation is that we have no information on offline orders that were paid outside the platform, which cannot be tracked by the platform. Therefore, we cannot directly verify whether the reduced offline orders of third-party stores become offline orders paid outside the platform. However, even without such information, we rule out the alternative explanation of customer switching by showing that less than 4% of third-party stores offline customers defected. Moreover, because we do not observe the detailed information of each offline order (e.g., the ID, price, and quantity of each product in the order), even though it was paid through the platform, we cannot pinpoint the specific tactics (e.g., price promotion) used by third-party stores to persuade offline customers to transact outside the platform. This can be an interesting future study when related data are available.

## Acknowledgments

The authors thank the senior editor, the associate editor, and anonymous reviewers for valuable suggestions and guidance. This work also benefited from feedback from the participants at the Fourteenth Symposium on Statistical Challenges in Electronic Commerce Research 2018, the 12th China Summer Workshop on Information Management 2018, and the 2019 Conference on Information Systems and Technology.

## Endnotes

<sup>1</sup> More than 90% of apps in the Apple App Store and the Google Play app store are free as of December 2019. See https://www.statista .com/statistics/263797/number-of-applications-for-mobile-phones/ for details (last access: June 30, 2020).

<sup>2</sup> Given that all the first-party stores are located in major cities spanning hundreds of square miles in China, for most offline customers in each city, the location of the first-party store is expected to be much further than those of the third-party stores they originally purchase from.

<sup>3</sup> In our data set, about 95% of orders are made by local customers (i.e., customers residing in the same cities as sellers).

<sup>4</sup> We thank the anonymous reviewers for this suggestion.

<sup>5</sup> The confidence intervals at period <sup>−</sup>6 are relatively large because of limited observations in that period.

<sup>6</sup> We thank an anonymous reviewer for this suggestion.

<sup>7</sup> The top 25% stores account for 86.7% of orders on the platform before the platform entry. Moreover, the top 33% stores account for 92.5% of orders. Our results are robust to the choice of the threshold for large stores.

## References

Abadie A (2005) Semiparametric difference-in-differences estimators. Rev. Econom. Stud. 72(1):1–19.

Abadie A, Diamond A, Hainmueller J (2010) Synthetic control methods for comparative case studies: Estimating the effect of California’s tobacco control program. J. Amer. Statist. Assoc. 105(490):493–505.

Angrist DJ, Pischke J (2008) Mostly Harmless Econometrics: An Em piricist’s Companion (Princeton University Press, Princeton, NJ)

Autor DH (2003) Outsourcing at will: The contribution of unjust dismissal doctrine to the growth of employment outsourcing. J. Labor Econom. 21(1):1–42.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1): 249–275.

Besley T, Burgess R (2004) Can labor regulation hinder economic performance? Evidence from India. Quart. J. Econom. 119(1): 91–134.

Chen J, Guo Z (2018) New media advertising and retail platform openness. Working paper, University of Texas at Dallas, Richardson.

Chen P-Y, Hitt LM (2002) Measuring switching costs and the determinants of customer retention in Internet-enabled businesses: A study of the online brokerage industry. Inform. Systems Res 13(3):255–274.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Farrell J, Katz ML (2000) Innovation, rent extraction, and integration in systems markets. J. Industrial Econom. 48(4):413–432.

Foerderer J, Kude T, Mithas S, Heinzl A (2018) Does platform owner’s entry crowd out innovation? Evidence from Google photos. Inform. Systems Res. 29(2):444–460.

Gawer A, Henderson R (2007) Platform owner entry and innovation in complementary markets: Evidence from Intel. J. Econom. Management Strategy 16(1):1–34.

Greenwood BN, Wattal S (2017) Show me the way to go home: An empirical investigation of ride-sharing and alcohol related motor vehicle fatalities. MIS Quart. 41(1):163–187.

Gu G, Zhu F (2020) Trust and disintermediation: Evidence from an online freelance marketplace. Management Sci. Forthcoming.

Jiang B, Jerath K, Srinivasan K (2011) Firm strategies in the mid tail of platform-based retailing. Marketing Sci. 30(5):757–775.

Klemperer P (1987) Markets with consumer switching costs. Quart. J. Econom. 102(2):375–394.

Kwark Y, Chen J, Raghunathan S (2017) Platform or wholesale? A strategic tool for online retailers to benefit from third-party in formation. MIS Quart. 41(3):763–785.

Li Z, Agarwal A (2017) Platform integration and demand spillovers in complementary markets: Evidence from Facebook’s integration of Instagram. Management Sci. 63(10):3438–3458.

Lu Y, Gupta A, Ketter W, van Heck E (2019) Information transparency in business-to-business auction markets: The role of winne identity disclosure. Management Sci. 65(9):4261–4279.

Manchanda P, Packard G, Pattabhiramaiah A (2015) Social dollars: The economic impact of customer participation in a firmsponsored online customer community. Marketing Sci. 34(3): 367–387.

Pavlou PA, Gefen D (2004) Building effective online marketplaces with institution-based trust. Inform. Systems Res. 15(1):667–675.

Ryan JK, Sun D, Zhao X (2012) Competition and coordination in online marketplaces. Production Oper. Management 21(6): 997-1014.

Song W, Chen J, Li W (2020) Spillover effect of consumer awareness on third parties’ selling strategies and retailers’ platform open ness. Inform. Systems Res. Forthcoming

Stuart EA (2010) Matching methods for causal inference: A review and a look forward. Statist. Sci. 25(1):1–21.

Weiss AM, Anderson E, MacInnis DJ (1999) Reputation management as a motivation for sales structure decisions. J. Marketing 68(4):74–89.

Wen W, Zhu F (2019) Threat of platform-owner entry and com plementor responses: Evidence from the mobile app market. Strategic Management J. 40(9):1336–1367.

Xu Y (2017) Generalized synthetic control method: Causal infer-Political Anal. 25(1):57–76.

Zellner A (1962) An efficient method of estimating seemingly unrelated regressions and tests for aggregation bias. J. Amer. Statist. Assoc. 57(298):348–368

Zhang XM, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev. 101(4):1601–1615.

Zhu F, Liu Q (2018) Competing with complementors: An empirical look at Amazon.com. Strategic Management J. 39(10): 2618–2642.

Zhu F, Zhang XM (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
