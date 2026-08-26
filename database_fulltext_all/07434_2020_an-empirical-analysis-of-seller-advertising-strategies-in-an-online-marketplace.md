---
otero_id: 7434
otero_key: "NB3BTX3R"
title: "An Empirical Analysis of Seller Advertising Strategies in an Online Marketplace"
authors: "Haoyan Sun; Ming Fan; Yong Tan"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0874"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/NB3BTX3R/fulltext/images/aab8df8f65f0c06ba4d0e8d2299c323388953fbb4668e0983762b0b85145febe.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## An Empirical Analysis of Seller Advertising Strategies in an Online Marketplace

Haoyan Sun, Ming Fan, Yong Tan

To cite this article: Haoyan Sun, Ming Fan, Yong Tan (2020) An Empirical Analysis of Seller Advertising Strategies in an Online Marketplace. Information Systems Research

Published online in Articles in Advance 26 Mar 2020

https://doi.org/10.1287/isre.2019.0874

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individua professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Empirical Analysis of Seller Advertising Strategies in an Online Marketplace

Haoyan Sun,<sup>a</sup> Ming Fan,<sup>b</sup> Yong Tan<sup>b</sup>

<sup>a</sup> Department of Decision and Technology Analytics, College of Business, Lehigh University, Bethlehem, Pennsylvania 18015; <sup>b</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195 Contact: has517@lehigh.edu (HS); mfan@uw.edu, https://orcid.org/0000-0002-4303-5313 (MF); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT)

Received: September 30, 2016 Revised: March 16, 2018; March 23, 2019 Accepted: May 24, 2019 Published Online in Articles in Advance: March 26, 2020

https://doi.org/10.1287/isre.2019.087

Copyright: © 2020 INFORMS

Abstract. Online marketplaces are increasingly adopting innovative business models such as paid advertising as a major revenue source. We study the effectiveness of two popular advertising tools, sponsored search and social media endorsement, in increasing traffic and sales for online sellers at a retail e-commerce platform. We find that, controlling for sellers self-selection behavior in choosing their strategies, both sponsored search and social media endorsement can significantly increase traffic for sellers, with sponsored search being more effective than social media endorsement. In contrast, only sponsored search has a positive and significant impact on sales. In examining the differential effects for sellers with low and high reputations, we find that sponsored search is more effective in increasing traffic for low-reputation sellers, but its effect on sales is larger for high-reputation sellers. Moreover, although social media endorsement increases traffic for sellers regardless of their repu tation, it is effective in increasing sales for only high-reputation sellers. Our study provides important managerial implications to sellers as well as e-commerce platforms.

History: Alessandro Acquisti, Senior Editor; Wenjing Duan, Associate Editor. Funding: Y. Tan acknowledges financial support from the National Natural Science Foundation of China (NSFC) [Grants 71729001 and 71490723]. M. Fan was supported by the Global Business Center at the University of Washington Foster School of Business. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0874.

Keywords: e-commerce platform • sponsored search • social media endorsement • online traf<sup>fi</sup>c • online sales • reputation

## 1. Introduction

In online e-commerce platforms, such as Amazon and eBay, sellers have to pay fees—usually a percentage of total transaction amount—to platform organizers in order to participate in the marketplace. Taobao, China’s largest online marketplace, owned by Alibaba Group, however, adopts a radically different business model, offering the basic platform service to sellers for free and generating revenues by monetizing traffic through advertising tools (Chen et al. 2016). Taobao’s business model, with little initial barriers to entry, naturally attracts a large number of participants to the platform. As of March 2015, Taobao had 350 million active buyers and over 10 million active sellers, generating a combined gross merchandise value of US\$394 billion (Alibaba Group 2015).

Although it is easy to become a seller at Taobao, surviving and prospering in this competitive market is difficult (Wong and Chu 2015). When hundreds of sellers are selling some similar products, attracting traffic to a store becomes critical. As a result, many sellers try to make their products more visible by investing in advertising (Osawa 2013), which in turn benefits the platform. Indeed, over 60% of Alibaba’s revenue comes from its online advertisement (iResearch 2014). The two primary advertising tools at Taobao are sponsored search advertising and social media endorsement. As one of Alibaba’s initial public offering investment advisory firms reported, sponsored search contributed 50%–60% of Taobao’s advertising revenue, while the rest was generated from seller advertising through different social media channels (Wu 2018).

Taobao started sponsored search advertising service in 2007. Similar to Google AdWords, sellers have to bid keywords to have their product advertisement appear along with relevant search results on Taobao’s website (Figure 1). Sellers only pay when a consumer actually clicks on the advertisement. Social media endorsement, another advertising tool offered by Taobao, was launched in 2009. It allows individual endorsers, who can receive commissions from the transactions, to post testimonials for different prod ucts so as to direct traffic to a seller’s store (Figure 2). Usually, sellers need to announce the products they want to promote at a crowdsourcing platform affiliated with Taobao. Then, the endorsers, who usually have sizable followers, can pick the products they want to endorse and then share their experiences at any social media platforms such as blogs, microblogs, or social networks.

Figure 1. (Color online) Illustration of Sponsored Search  
![](/api/attachments/NB3BTX3R/fulltext/images/c7aad5af545aafacac233d06ee4c1f2091c419c0cb2f044fa9370ac203949ead.jpg)

In this paper, we investigate the effectiveness of sponsored search and social media endorsement in increasing traffic and sales for sellers at Taobao and provide important implications to advertising on e-commerce platforms. First, previous literature on sponsored search (Yang and Ghose 2010b, Agarwal et al. 2015, Blake et al. 2015) focuses primarily on the context of search-engine advertising, such as Google and Bing. While advertising remains a key part of Taobao’s successful business model, e-commerce platforms such as Amazon and eBay, which have relied on transaction fees as their revenue model, are adopting sponsored product advertising as a growing revenue source, challenging Google and Facebook in online advertising (Mims 2018). Our study fills this gap by examining how sponsored search works on a retail e-commerce platform. Second, studies on paid social media endorsement are quite scant. Much less is known about the differential effects of sponsored search and social media endorsement when both strategies are used. The mechanisms of the two advertising models are quite different. As sponsored search can target consumers who already have purchase intentions and are actively searching for a certain product on a platform, social media endorsement relies on social influence and creates a positive attitude in online communities (Bakshy et al. 2012). Specifically, we aim to answer the following research questions: Are these two advertising strategies effective in increasing traffic and sales for online sellers? If yes, which strategy is more effective? Does the effectiveness of these strategies differ across heterogeneous sellers, and, if so, how?

Figure 2. (Color online) Illustration of Social Media Endorsement  
![](/api/attachments/NB3BTX3R/fulltext/images/0ee8f8720d834cfd4694f70dccb9f7b6bbd13505382072cef559a16d09833222.jpg)

Our study contributes to the literature in two important ways. First, we provide interesting results on how advertising tools work together in affecting individual sellers’ traffic and sales on a retail e-commerce platform. Although previous literature has studied the effectiveness of sponsored search and social media marketing, it remains unclear as to which advertising tool is generally more effective and whether these two tools increase traffic and sales independent of or in substitution with each other. Our model not only sheds light on the relative strengths of these tools in affecting traffic and sales, but also examines the interactive effects of these two tools, thus integrating the literature on these two important advertising approaches. Second, this paper advances the understanding of the two advertising tools by identifying a key contingency—seller reputation, which is an accessible index to customers that captures the accumulated customer feedbacks on transactions. Our findings are of great importance, as they provide additional insights into how these advertising tools can work more effectively in increasing traffic and sales for sellers with different reputation levels, thus providing important implications to guide the strategic choices for sellers as well as the platform.

The rest of the paper is structured as follows. Section 2 reviews the relevant literature and discusses our research motivation. Section 3 develops the theoretical background for the empirical model. Section 4 introduces the data set and provides model-free analysis. Section 5 illustrates the empirical model, as well as the specification and identification strategies for the analysis, and then presents results from the empirical analysis and an additional robustness check Section 6 discusses results and the related managerial implications. Section 7 concludes the study with limitations and suggestions for future research.

## 2. Prior Literature and Research Motivation 2.1. The Two Advertising Models

Our study builds on the growing literature of sponsored search and social media advertising in an online environment. There are quite a few studies that have looked at sponsored search (Athey and Ellison 2011; Chan et al. 2011a, b; Xu et al. 2012; Jeziorski and Sega 2015; Narayanan and Kalyanam 2015). Recent empirical work has examined sponsored search as a driver of click-through and conversion rates (Yang and Ghose 2010, Agarwal et al. 2015), as well as the effectiveness of different types of keywords (Blake et al. 2015). Specifically, Yang and Ghose (2010) used a retail chain store’s advertising data on Google and estimated the interrelationship between organic search listing and sponsored search listing. They found that the click-through rate on organic search listing has a positive interdependence with clickthroughs on paid ads. All the performance indicators in the presence of both paid and organic search listings are significantly higher than those in the ab sence of sponsored search advertisements. Agarwal et al. (2015) used data from an online retailer’s keyword advertising campaign and examined how competing organic results affect the performance of sponsored search advertisement. They found that competition among organic listings significantly decreases click-through rates on the sponsored search ads, but increases conversion rate on those sponsored search ads. Blake et al. (2015) conducted field experiments on eBay and found that the effectiveness of sponsored search advertisements differs for brand keyword search and nonbrand keyword search. The above studies, however, are all in the context of online search engine advertising, and our study examines sponsored search advertising in a different context.

Literature on social media endorsement has been scant. Although it is similar to social advertising, as the promotions are based on underlying social networks (Bakshy et al. 2012, Tucker 2016), social media endorsement allows advertisers to post their promotion tasks on a platform so that interested endorsers can take on the tasks to promote the products for monetary rewards (Peng et al. 2016). Two streams of research are related to social media endorsement. First, it is related to celebrity endorsement, which attaches the fame of a celebrity to a brand or product and influences consumer purchases. Celebrity endorsement has been shown to have positive effects on firm value (Agrawal and Kamakura 1995) and on book sales (Butler et al. 2005). Social media endorsement is different from celebrity endorsement in terms of the level of influences and the network size, but, similar to celebrity endorsement, the effectiveness of social media endorsement largely depends on the fan base and network connections of the endorser. Second, social media endorsement is also related to a growing body of literature that studied how word-ofmouth (WOM), especially online WOM, affects firm performance (Bickart and Schindler 2001, Godes and Mayzlin 2004, Clemons et al. 2006, Liu 2006, Dellarocas et al. 2007, Duan et al. 2008, Gu et al. 2012) and creates social influence (Trusov et al. 2010, Aral and Walker 2011, Iyengar et al. 2011, Aral and Walker 2012, Moe and Schweidel 2012, Oestreicher-Singer and Sundararajan 2012, Susarla et al. 2012, Fang et al. 2013). For example, Bickart and Schindler (2001) compared WOM generated from consumers and sellers, respectively, and found that consumergenerated information had a greater impact on consumer purchase decisions than seller-created information. Gu et al. (2012) compared internal WOM and external WOM on high-involvement products. Their results suggest that a retailer’s internal WOM has a limited influence on sales, whereas external WOM sources have a significant impact on sales. However, these studies on online WOM all focus on voluntary contributions from consumers, whereas in our context, endorsers clearly have a profit motivation.

## 2.2. Online Traf<sup>fi</sup>c and Sales

This paper also extends the literature that evaluates different driving forces of web traffic and sales. Online traffic has been one of the most important metrics in measuring the success of online businesses. One of the key measures of the effectiveness of a marketing strategy is the amount of traffic that it can attract. This is because a retailer’s financial performance closely relates to its ability to attract traffic (Perdikaki et al. 2011), and such traffic could potentially be converted into sales and revenue (Benbunan-Fich and Fich 2004). Luo and Zhang (2013) investigated the predictive power of web traffic and consumer buzz on firm value and found that buzz and traffic explain a substantial portion of the total variance of firm value. Extant research has also investigated the driving forces and the impact of online traffic (Dewan et al. 2002, Chatterjee et al. 2003, Wu et al. 2005, Rutz et al. 2011, Liaukonyte et al. 2015). For example, Chatterjee et al. (2003) examined the click proneness across consumers and studied the effects of exposure to repeated banner advertising and competing advertisements. Rutz et al. (2011) used search keyword-level data sets and found an indirect effect of sponsored search on future repeat traffic. We extend this body of literature and examine how the two advertising models concurrently influence traffic and sales.

## 2.3. Business Model for Online Platform

Moreover, our study is related to the growing literature that studies business models for online platforms and mechanisms of two-sided markets in engaging both buyers and sellers. Bhargava and Choudhary (2004) developed economic models of the marketplace as intermediaries to examine how their pricing and product-line design strategies provide value-added services to both sellers and buyers. Soh et al. (2006) compared online marketplaces on their strategy, price transparency, and performance, and they found that marketplaces should pursue strategies of differentiation in order to succeed. Specifically, marketplaces should provide compensatory benefits for sellers in the case of high price transparency and for buyers in the case of low price transparency. More recently, Chen et al. (2016) compared the two different revenue models adopted by eBay and Taobao and found that the advertising model creates more value for buyers and makes sellers better off in most scenarios.

In sum, our study contributes to the literature in the following ways. First, prior studies on sponsored search advertising focus on the context of online searchengine advertising, such as Google and Bing. Given the growing importance of advertising in e-commerce platforms such as Taobao and Amazon, this study fills the gap by examining the performance of sponsored search advertising on a retail e-commerce platform. Second, paid social media endorsement has not been well examined in previous literature. We study social media endorsement and compare its effectiveness to sponsored search advertising. Third, prior literature typically examines the isolated impact of a single advertising model and overlooks the interplay of different advertising strategies. Our study highlights the ben efits for sellers to employ different advertising strategies given their heterogeneous characteristics. To the best of our knowledge, our research is one of the first empirical studies to examine the economic impact of online advertising in a retail e-commerce platform that relies on advertising as its major revenue source. By showing the effectiveness of sponsored search and social media en dorsement, the study could help inspire other platforms such as Amazon and eBay to offer similar advertising services, which not only help platforms to expand their revenue sources, but also enable sellers to attract new buyers and grow their businesses.

## 3. Theory

Sponsored search advertising and social media endorsement are two types of advertising strategies that engage consumers in different ways. Although sponsored search advertising targets consumers who are already on an e-commerce platform and have specific purchase intentions reflected in their search terms, social media endorsement introduces products or brands based on underlying social networks and aims to cultivate a positive attitude through social influence (Bakshy et al. 2012, Tucker 2016). In this section, we develop hypotheses on how sponsored search and social media endorsement affect traffic and sales.

## 3.1. Sponsored Search Advertising

On e-commerce platforms, numerous sellers are selling similar products or even the same product. A customer’s purchase behavior in a platform often begins by putting in the keywords of the desired product in the search engine of the platform. The platform will then generate a list of products, which is often termed an organic search list, in the order based on the algorithms that potentially maximize product match in terms of relevance, product quality, seller characteristics, etc. Accumulated research on individual decision making has well established that, given the restriction of cognitive resource and time, individuals will rarely engage in rational decision making, where they should compile an exhaustive list of alternatives and compare to get the best decision. Instead, individual decision making is mostly guided by the principle of “satisficing,” where they go through the easily available choices and decide on one that they feel is “good enough” (Simon 1979). In the context of online purchase, consumers will likely go through a number of products listed in the front end of the organic search result and make the purchase when they find a good-enough product or seller. As a result, only a limited number of sellers can be exposed to the potential customer before the customer makes the purchase. Thus, for sellers, exposing themselves to potential buyers—when the search keywords are related to their products—is crucial in attracting traffic to their online store and convincing the buyers to purchase. Sponsored search represents an important approach to this end.

Sponsored search advertising on search engines, such as Google, can provide valuable information to consumers, not only to make their search more efficient in terms of finding their ideal result faster (Athey and Ellison 2011), but also to give potential vendors opportunities to expose themselves, especially when these vendors are listed far behind in the organic search results. Similarly, sponsored search on e-commerce platforms such as Taobao provides product information to potential buyers and also enables sellers with matching products to better expose themselves to customers in their satisficing decision-making process. The informative view of advertising theory (Nelson 1974, Bagwell 2007) argues that advertising provides information to consumers mainly through the matching effect. Advertising contains information on product attributes and prices, which can match potential buyers’ needs and their reservation prices (Anderson and Renault 2006). Based on consumers search terms, a seller can bid the search keywords and place the ads to consumers who are browsing through the products, thus increasing the chance that consumers will visit the store and check on the products (Chen et al. 2016, Mims 2018). Therefore, we expect that sponsored search can help attract consumers to visit the online seller’s store and effectively increase the traffic to the store, which leads to the following hypothesis:

Hypothesis 1. Sponsored search advertising has a positive effect in attracting traffic to an online store.

Increased traffic is vital for retailers seeking to increase sales. In studying physical retail stores, Perdikaki et al. (2012) find that traffic has a positive and significant effect on sales, although the relationship exhibits diminishing return, as the shortage of store sales representatives makes it difficult to convert increased traffic into sales. In online settings, web traffic is also positively related to brand awareness, customer acquisitions, and, in turn, firm value (Luo and Zhang 2013). Applying to the e-commerce context, we expect that the positive relationship between traffic and sales continues to hold. Although the strength of this positive relationship is subject to the capability of different sellers in converting incoming traffic into actual sales, we follow the previous literature and contend that increased traffic will, in general, lead to increased sales for online stores. Given that sponsored search can effectively increase traffic for sellers and that traffic has a robust, positive relationship with sales, we hypothesize that:

Hypothesis 2. Sponsored search advertising has a positive effect in increasing online sales.

## 3.2. Social Media Endorsement

Compared with sponsored search advertising, social media endorsement works differently, as it relies on social influence—via connections on social media platforms—to cultivate positive attitudes toward a seller’s products in consumers, who do not necessarily have a purchase intention to start with (Bakshy et al. 2012). Similar to other forms of social advertising, social media endorsement is based on linked social networks and existing fan base (Bakshy et al. 2012) and represents persuasion attempts designed to draw attention and influence recipients’ attitudes or decisions (Starr and MacMillan 1990, Friestad and Wright 1994). On social media platforms, people mostly follow (a) friends, families, or acquaintances to whom they have personal connections; and (b) public figures who they do not know at a personal level but find in terests and values in following because of new information or fresh insights that they can bring.

At its essence, social media endorsement represents a form of positive word-of-mouth that spreads positive information regarding a product or a seller. Accumulated research has shown that positive wordof-mouth has substantial effects on drawing traffic and increasing sales in a variety of online contexts (Godes and Mayzlin 2004, Chevalier and Mayzlin 2006, Lu et al. 2013). However, unlike regular online reviews, where the readers and the posters are most likely strangers to each other, when endorsers provide introduction and post positive comments about a product or a seller, they are spreading the positive word-ofmouth to those to whom the endorsers are personally connected or to those who share similar interests and values. Research on social psychology has long established that people are more likely to be influenced and persuaded by those who they like and with whom they share similarities (Cialdini 2001). In addition, given such connections between endorsers and information recipients, the potential buyers, motivated by an agreeable orientation (Lundgren and Prislin 1998, Wood 2000), will likely accept the endorsers’ views and check out the products. As such, we expect that social media endorsement will have an overall positive effect in attracting potential buyers to a store. Therefore, we hypothesize the following:

Hypothesis 3. Social media endorsement has a positive effect in increasing online traffic.

Similar to the reasoning of sponsored search advertising, as social media endorsement attracts more traffic, it can also have a positive effect on sales. Therefore, we have the following hypothesis:

Hypothesis 4. Social media endorsement has a positive effect in increasing online store sales.

## 3.3. Sponsored Search, Traf<sup>fi</sup>c, and Seller Reputation

In addition to the general positive effects that sponsored search and social media endorsement have on traffic and sales, we further expect that such effects will likely differ across heterogeneous sellers, given their different characteristics and resources. Specifically, we examine sellers based on their reputations, which measure a seller’s experiences and acquired status at the platform. Examining the interactions between the respective marketing strategy and seller reputation will help shed light upon the mechanisms through which sponsored advertising and social endorsement affect individual sellers.

At Taobao, reputation score reveals to consumers how many successful transactions a seller has made throughout her tenure at the platform. Previous literature suggests that the accumulated reputation score can be a proxy or a signal for a seller’s trustworthiness and quality (Rob and Fishman 2005, Jin and Kato 2006). A natural way to characterize a seller is through reputation. Although high-reputation sellers are usually mature sellers that have already established themselves on the platform by providing satisfactory products and services to a large number of customers, low-reputation sellers are usually relatively new to the platform and have not yet accumulated a large volume of positive feedbacks. For consumers who are visiting a seller’s store for the first time, they usually rely heavily on the reputation score to make the purchase decisions.

At the same time, reputation can also be a trafficgeneration mechanism. On e-commerce platforms such as Taobao and eBay, as well as at search engines such as Google, high-reputation sellers are more likely to appear in the front end of the organic search list. Researchers have found that on search engines, when an online retailer has higher quality, more consumers will click its link rather than the competitors’ in the same organic list (Baye et al. 2016).

The different functions of online reputation can lead to different interaction effects with sponsored search. As a signal for seller trustworthiness and quality, reputation can complement sponsored search. With a high reputation, a seller and its products are likely to be valued by more consumers, which sends a positive signal regarding the product quality as well as service (Elfenbein et al. 2012). Such positive signals from high-reputation sellers are extremely critical in the online context, where the potential buyers cannot view products in person and do not have personal interactions with the sellers. Therefore, when the potential buyers see a sponsored search advertisement from sellers with higher reputation and stronger name recognition, they are more likely to click the advertisement, thus generating more traffic to the store. Therefore, we expect that sponsored search is more effective when seller reputation is higher, which leads to the following hypothesis:

Hypothesis 5(a). Sponsored search is more effective for sellers with higher reputation in attracting traffic.

On the other hand, the logic that sponsored search works more effectively for lower-reputation sellers is also compelling. If we view reputation as a trafficgeneration mechanism, reputation can substitute for sponsored search. Although there is a net benefit that a product appears in both the organic search list and sponsored search list, the marginal effect of sponsored search ads could be lower for a high-reputation seller than for a low-reputation one. The high-reputation seller is more likely to appear on the top of the organic list, with a high number of clicks from consumers. In contrast, low-reputation sellers may end up at the bottom of the organic search result or not appear at all. Thus, traffic increase could be larger for low-reputation sellers when they use sponsored search. As a result, we propose the following alternative hypothesis:

Hypothesis 5(b). Sponsored search is more effective for sellers with lower reputation in attracting traffic.

## 3.4. Social Media Endorsement, Traf<sup>fi</sup>c, and Seller Reputation

Different from sponsored search advertising, social media endorsement typically attracts traffic from outside of the platform and does not directly compete with the traffic-generation function of seller reputation through organic search result. As we argued earlier, social media endorsement in general can effectively cultivate positive impressions and interests from the viewers toward the product. Nonetheless, depending on the contents provided in the posts, such positive effect could potentially differ. We argue that, by serving as a quality and trustworthiness signal, seller reputation could complement the social-influencing process. From the perspective of motivated reasoning, impression-oriented consumers are likely to select and pay more attention to the reputation information (Chen et al. 1996). For accuracy-oriented and defensiveoriented consumers, an objective signal such as reputation can make these customers respond more positively to the endorsements (Chen et al. 1996, Guo and Main 2012). In general, consumers are more likely to have a favorable impression toward a product or a seller when their reputation scores are higher (Elfenbein et al. 2012), assuming that the endorsers provide the high-reputation information on their posts. Therefore, we expect that, when seller reputation is higher, social media endorsement is more effective in influencing consumers and attracting customers to visit the store, which leads to the following hypothesis:

Hypothesis 6. Social media endorsement is more effective for sellers with higher reputation in attracting traffic.

## 3.5. Traf<sup>fi</sup>c Conversion and Sales

We further explore how seller reputation influences the effectiveness of advertising strategies in converting traffic into sales. Sales are a function of both traffic and conversion rate. With high reputation, advertising strategies can be more effective in generating sales. First, researchers have argued and found that highreputation sellers are, in general, associated with a high traffic conversion rate (Hui et al. 2016). Seller reputation reflects the general quality of their products, how fast they handle the shipment of product to customers, and how well they handle customers requests. These signals are important in consumers purchase decisions. In contrast, a lower reputation can be perceived as a negative signal of the product and service, or as a lack of credentials if a seller is relatively new and has not built up their reputation yet. Potential customers will be more cautious in making the purchase decisions. Second, as we discussed earlier, the relationship between sponsored search advertising and traffic depends on whether reputation serves as a complement for or substitute to sponsored search advertising in affecting traffic. In the former case, traffic could rise more quickly for high-reputation sellers when paid advertising is used. As a result, sales will naturally increase more quickly for high-reputation sellers, with more traffic and higher conversion rate. In the latter case, even traffic increase could be higher for low-reputation sellers than high-reputation sellers; as long as the effect of conversion rate dominates that of traffic, high-reputation sellers can still enjoy a higher sales increase compared with low-reputation sellers. Therefore, we hypothesize:

Hypothesis 7. Sponsored search is more effective for sellers with higher reputation in increasing sales.

Above, we argue that seller reputation significantly enhances the extent to which the sellers are able to convert the sponsored-search-induced traffic into actual sales. We suggest that seller reputation plays a salient role in converting traffic incurred from social media endorsement into actual sales. Unlike those attracted through sponsored search, the potential customers attracted through social media endorsement do not have a strong purchase intention to start with and will likely be making fast decisions on purchase or not (rather than comparing products from different sellers). According to the Elaboration Likelihood Mode of Persuasion (Petty and Cacioppo 1981, 1986), these potential customers do not have a strong motivation to scrutinize the product characteristics in comparison with other alternatives. In this case, they will be mostly influenced by the easily accessible cues that can help them quickly infer the quality of the product as well as the services (such as brand awareness and seller reputation). As such, a low reputation will very likely give these potential customers—attracted through social media endorsement—a stop in the purchase decision, without looking deeper into other desirable qualities of the product. Therefore, we expect that the conversion rate of traffic via social media endorsement will be significantly higher for high-reputation sellers. Together with the arguments that social media endorsement is more effective for high-reputation sellers in attracting traffic (Hypothesis 4), we propose the following hypothesis:

Hypothesis 8. Social media endorsement is more effective for sellers with higher reputation in increasing sales.

The conceptual model of our theoretical development is presented below in Figure 3.

Figure 3. Theoretical Model  
![](/api/attachments/NB3BTX3R/fulltext/images/12f8e06f0c4a98da245d2a91cdb2df922be7e36217bd731103f2c039cf6dcb4e.jpg)

## 4. Data and Model-Free Analysis 4.1. Data and Variables

We examine the effectiveness of sponsored search and social media endorsement based on a panel data from Taobao. The data set contains 3,620 randomly sampled sellers in the women’s fashion category, with monthly data across 10 months from May 2011 to February 2012. This is an unbalanced panel of data, as some sellers just entered the market during the period. In order to capture the effects of both strategies in a longer time horizon, we eliminate sellers with less than four-period activities in the data set, and we end up having 2,859 sellers in our sample. On the next subsection, we provide detailed descriptions on the variables in the data set. Table 1 presents the summary statistics of the variables.

Traffic is the dependent variable for our analysis, and it is the number of unique individual visitors that have visited any product pages of a particular seller in a given short period of time. Unique visitor is commonly used in both online and offline studies (Dreze\` and Zufryden 2004, Gallino and Moreno 2014), and it reflects the popularity of a platform/website/product page. Because a visitor can make multiple visits in a specified period before they make the final purchase, the number of visits may be greater than the number of unique visitors. Therefore, the number of unique visitors can better capture the popularity of a site/seller. Specifically, we use the monthly total of unique visitors in our analysis. Traffic is a count variable and is highly skewed, as the standard deviation is much higher than its mean.

Sales is another dependent variable for our analysis, and it is the number of transactions the seller has made in a given month. This variable captures the number of converted traffic, or, in other words, how many unique visitors actually made the purchase on the seller’s website.

Sponsored search is a dummy variable indicating whether a particular seller pays for the service of sponsored search advertisement in a given month. If a seller adopts the sponsored search advertising, the variable is coded 1; otherwise, it is coded as 0. The average of the variable is 0.59, suggesting that more than half of the sellers used the sponsored search during the whole data period.

Social media endorsement is a dummy variable indicating whether a particular seller utilizes social media endorsement service from Taobao in a given month. If a seller adopts the social media endorsement service, the variable is coded 1; otherwise, it is coded 0. The average of the variable, as shown in Table 1, is 0.47, suggesting that less than half of the sellers used the service during our study period.

Reputation is the accumulative feedback scores for a seller. It indicates how well and how long the sellers have established themselves on the marketplace A buyer can rate the seller positive, neutral, or negative after each transaction. Sellers receive 1 point if the feedback is positive, 0 if the feedback is neutral, and <sup>−</sup>1 if the feedback is negative. These scores accumulate over time for each seller, and the reputation score is the cumulative sum of each transaction feedback.

Tenure indicates the number of days the seller has been on the platform. The average tenure is 908 days, which is roughly 3 years. The maximum tenure is 3,188 days, which is about 8 years.

Repeat customer indicates the number of customers who have made purchases with a particular seller more than one time within the past 6 months. The average number of repeat customer is 146.97, and the standard deviation is 802.29, which is substantially higher than the mean, suggesting that the distribution of the variable is skewed.

Average price captures the price level of a seller in a given month. Different sellers have different business strategies to establish themselves on the marketplace. Average price is a good measurement of sellers’ product positioning, indicating whether a seller is a high-end luxury-brand seller or a budget-brand one.

Table 1. Summary Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Traffic</td><td>16,658.38</td><td>65,286.65</td><td>1</td><td>2,389,328</td></tr><tr><td>Sales</td><td>304.5992</td><td>1,454.556</td><td>0</td><td>58,442</td></tr><tr><td>Reputation</td><td>10,157.38</td><td>60,968.23</td><td>0</td><td>2,218,195</td></tr><tr><td>Tenure</td><td>908.15</td><td>643.28</td><td>1</td><td>3,188</td></tr><tr><td>Repeat Customer</td><td>157.96</td><td>885.33</td><td>0</td><td>30,182</td></tr><tr><td>Product Variety</td><td>307.90</td><td>543.75</td><td>1</td><td>20,778</td></tr><tr><td>Average Price</td><td>162.22</td><td>200.22</td><td>0.733</td><td>6,786.67</td></tr><tr><td>Social Media Endorsement</td><td>0.48</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>Sponsored Search</td><td>0.61</td><td>0.49</td><td>0</td><td>1</td></tr></table>

Note. Total number of observation N = 25,702.

Product variety indicates the breadth of product categories offered by a seller in a given month. Given different business models, sellers may want to focus on limited categories of products, or they would like to provide a large variety of products for customers to choose from. As shown in Table 1, the average number of product variety is 299.79, and the standard deviation is 719.81, suggesting that sellers on the platform have very different business models in terms of satisfying diverse consumer needs.

As indicated in the summary statistics in Table 1, the distributions for many of the above variables are highly skewed. Therefore, we log-transform the continuous independent variables in our empirical analyses.

## 4.2. Model-Free Analysis

We now present some model-free evidence of our data. First, for the sellers who have adopted advertising, a significant portion used the strategies dynamically, rather than using a strategy consistently throughout the whole period. Figure 4 shows the distribution of the adoptions of each advertising strategy by sellers. For example, 45.14% of sellers did not use sponsored search throughout the study period, whereas 27.68% of them always used sponsored search during the study period. Also, 49.89% of sellers did not use social media endorsement, whereas 18.76% of the sellers always used social media endorsement during the 10 months’ period.

Second, we examine whether there is a self-selection bias of adopting the strategies, such that more mature sellers are more willing to adopt advertising strategies. Figure 5 shows the distributions of two seller characteristics, seller tenure and average product price level, by the adoptions of different advertising strategies. The pattern suggests the existence of self-selection, such that sellers with longer tenure are more likely to use advertising (Figure 5(a)), whereas the average product price may or may not be the reason why sellers choose either or both strategies (Figure 5(b)).

![](/api/attachments/NB3BTX3R/fulltext/images/f46b8ad4b33aad3d313a7007ea9a854b9ebfb20bfe8e58d5afcdbff85090320e.jpg)  
Figure 4. (Color online) Distribution of Sellers with Strategy Adoption Frequency

Third, we examine the distribution of traffic and sales for the sellers. The distributions for traffic and sales are similar, with both highly skewed (Figure 6). Also, traffic and sales are highly correlated, with a correlation coefficient of 0.86. Figure 7 displays the scatterplot of log-transformed traffic and sales, which indicates that, at a lower traffic level, there is larger variance among sellers in converting traffic to sales, whereas, at a higher traffic level, sellers’ ability to convert traffic to sales is fairly consistent.

Finally, we examine the distribution of traffic and sales over different strategy sets. As shown in Figure 8(a), sellers using sponsored search advertising have more traffic than those using social media endorsement, and sellers using both strategies attract even more traffic. This result provides preliminary evidence that sponsored search has a higher impact on traffic than social media endorsement, but social media endorsement can increase traffic above and beyond sponsored search advertising. Figure 8(b) indicates that sellers who adopted sponsored search have higher average sales than those who adopted social media endorsement However, the level of sales for the sellers who adopted social media endorsement doesn’t seem to be significantly different from those that never used any strategies.

## 5. Empirical Model and Results

## 5.1. Panel Vector Autoregressive Model

To further study the dynamic relationship between seller strategies and online traffic, we employ a panel vector autoregressive (VAR) model to identify the reverse effect of past traffic on sellers’ selection of strategies.

![](/api/attachments/NB3BTX3R/fulltext/images/14f4a58998a510eba149d62ed341eccb40465a97da948329378c40c389027d01.jpg)

Figure 5. (Color online) Distribution of Seller Characteristics by Strategies  
(a)  
![](/api/attachments/NB3BTX3R/fulltext/images/9d48c53238c0cf47399a9168aaa1fe19c2d44be87dfca2c0578dd071d447c3e9.jpg)  
Notes. (a) Distribution of seller tenure. (b) Distribution of average price.

The panel VAR model has been widely used in the fields of economics (Fort et al. 2013), marketing (Steenkamp et al. 2005), and information system (Luo and Zhang 2013b, Chen et al. 2015, Thies et al. 2016, Moqri et al. 2018), and it is particularly useful to study panel data with a large number of observations and a small number of time periods. It allows us to control for unobserved individual heterogeneity, utilize lagged dependent variables as instruments within the Gaussian mixture model framework, and capture the motivations of adopting advertising strategies based on sellers’ past behavior and performance.

The specification of our model has the following form:

$$
\pmb {D} \pmb {V} _ {i, t} = A (L) \pmb {D} \pmb {V} _ {i, t} + \beta \pmb {\Delta} _ {i t} + \pmb {\kappa} _ {i} + \pmb {\nu} _ {t} + \varepsilon_ {i t}.
$$

Where DV is a vector of variables as follows:

$$
\boldsymbol {D} \boldsymbol {V} _ {i, t} = \left( \begin{array}{c} T r a f f i c \\ S p o n s e r e d S e a r c h \\ S o c i a l M e d i a E n d o r s e m e n t \end{array} \right) _ {i, t}.
$$

Figure 6. (Color online) Distributions of Traffic and Sales  
![](/api/attachments/NB3BTX3R/fulltext/images/a6216ffb3dba30ae08d1439257c5d0eae1310bfa64749a568f0ac083ce31ff59.jpg)

(b)  
![](/api/attachments/NB3BTX3R/fulltext/images/29f293ddc4b16c048c7fc596afca86c3eedcc5f03942d54a5daebdfc5cfd3323.jpg)

$\Delta _ { i t }$ is a vector of time-varying control variables, $\pmb { \kappa } _ { i }$ is the individual fixed effect, and $v _ { t }$ is the time dummy to control for seasonality. With the lagged operator A(L) defined as lag polynomial, $A ( L ) \bar { D } V _ { i , t }$ can be written as:

$$
A (L) \boldsymbol {D} \boldsymbol {V} _ {i, t} = \alpha_ {1} \boldsymbol {D} \boldsymbol {V} _ {i, t} + \dots + \alpha_ {p} \boldsymbol {D} \boldsymbol {V} _ {i, t - p}.
$$

In order to select the best lag for the model, we calculate the model-selection measure for first- to thirdorder panel VARs using the first four lags of $T r a f f i c ,$ Sponsored Search, and Social Media Endorsement as instruments. The selection criterial result show that the second-order panel VAR model is the preferred model (see Table A.1). The estimation results for our panel VAR model are shown in Table 2. Given that the number of lags picked is two, we are able to interpret the dynamic relationship between the two advertising strategies and their ability to attract online traffic in a relatively longer time horizon. From the equation of sponsored search, the negative and significant coefficient estimates on traffic at both lag 1 adoption of it at the current period, which suggests that sellers are more likely to keep using social media endorsement if they have used it in the last period, regardless of whether they have used sponsored search or not. Also, based on the traffic equation, the results show that past selection of advertising strategies, either sponsored search or social media endorsement, have no significant impact on current period traffic.

![](/api/attachments/NB3BTX3R/fulltext/images/c803dd0c8a11af67dcfbb2d859cd788cb67e7aff32c5775ce991717e5a6caeee.jpg)

Figure 7. (Color online) Scatterplot of Traffic and Sales  
![](/api/attachments/NB3BTX3R/fulltext/images/1baacde5dee932b7b9f4224fa0aab22a744a06791da45778eba67238b74fc2ba.jpg)  
$( \alpha = - 0 . 0 0 3 , p < 0 . 0 5 )$ and lag $2 \left( \alpha = - 0 . 0 0 2 , p < 0 . 1 0 \right)$ indicate that sellers are more likely to adopt sponsored search if they weren’t able to obtain enough traffic in the past periods. This effect also exists in terms of the adoption of social media endorsement. The coefficient estimates on traffic at lag 1 $( \alpha = - 0 . 0 1 4 , p < 0 . 0 5 )$ and lag $2 \left( \alpha = - 0 . 0 0 6 , p < 0 . 0 5 \right)$ ) are both negative and significant. Interestingly, the results also show that the adoption of the strategies also tend to be consistent over time. From the sponsored search equation, the significant and positive coefficient estimate of sponsored search adoption at lag 1 $( \alpha = 0 . 7 1 7 , p < 0 . 0 1 )$ ) and the significant and positive coefficient estimate of social media endorsement adoption at lag $1 ( \alpha = 0 . 0 3 2$ $p < 0 . 0 5 )$ indicates that sellers are likely to use sponsored search if they have used sponsored search in the last period or if they have used social media endorsement in the last period. However, based on the equation of social media endorsement, we only see that the adoption of social media endorsement at lag 1 has a significant and positive effect $( \alpha = 0 . 7 3 9 , p < 0 . 0 1 )$ on the

Figure 8. (Color online) Distribution of Traffic and Sales by Strategies  
![](/api/attachments/NB3BTX3R/fulltext/images/791d36f849118edc4ccfeaee51ac336e739c6ce87bdc68bad3df1763f1b60b5c.jpg)  
Notes. (a) Distribution of traffic by strategies. (b) Distribution of sales by strategies.

The results of Panel VAR suggest that there is no significant spillover effect on traffic from either sponsored search or social media endorsement. However, from a seller’s strategic perspective, there is some coordination between the two strategies over the long term.

## 5.2. Endogenous Treatment Model

Our model is estimated by using the endogenous treatment procedure developed by Rabe-Hesketh and Skrondal (2012). This technique is similar to the treatment effect approach developed by Heckman (1979), but in a more generalized and flexible form. Our model includes sellers’ advertising-strategy choice as an endogenous treatment variable, and we estimate the system equations simultaneously instead of following a two-stage estimation approach of sample selection and treatment model. In the following, we model the traffic equation and the selection equation of advertising strategies, respectively. Table 3 lists the notations in our empirical models.

We postulate that sellers’ advertising strategies affect web traffic and sales. The empirical model begins with the standard assumption that the sellers make choices about their strategies to increase store traffic, and store traffic is a function of advertising strategies employed and other seller characteristics. Specifically, we assess the impact on traffic based on seller price level, reputation, number of repeat customers, and product variety, all of which capture different aspects affecting online traffic. The number of unique visits $y _ { i t }$ is a count variable and can be assumed to follow a Poisson distribution. Because we find evidence of $y _ { i t }$ being overdispersed, we consider a negative binomial model as the traffic model, which is a generalization of a Poisson regression model that allows for overdispersion by incorporating an individual unobserved effect into the conditional mean (Hausman et al. 1984). We have the traffic model as follows:

![](/api/attachments/NB3BTX3R/fulltext/images/0560f5809310e2311fa869550d843c3d2131bd4e08a8e0407938bd443c9addd2.jpg)

Table 2. Estimation Result of Panel VAR Model

<table><tr><td>Variable</td><td>Traffic</td><td>Sponsored search</td><td>Social media endorsement</td></tr><tr><td> $Traffic_{t-1}$ </td><td>0.192***(0.034)</td><td>-0.003**(0.001)</td><td>-0.014**(0.005)</td></tr><tr><td> $Traffic_{t-2}$ </td><td>-0.177***(0.017)</td><td>-0.002**(0.001)</td><td>-0.006**(0.002)</td></tr><tr><td> $SponsoredSearch_{t-1}$ </td><td>0.063(0.421)</td><td>0.717***(0.043)</td><td>0.082(0.064)</td></tr><tr><td> $SponsoredSearch_{t-2}$ </td><td>-0.144(0.174)</td><td>0.001(0.003)</td><td>0.014(0.016)</td></tr><tr><td> $SocialMediaEndorsement_{t-1}$ </td><td>0.059(0.169)</td><td>0.032**(0.015)</td><td>0.739***(0.029)</td></tr><tr><td> $SocialMediaEndorsement_{t-2}$ </td><td>0.052(0.085)</td><td>0.009(0.006)</td><td>0.021(0.015)</td></tr><tr><td>Product Variety</td><td>0.271***(0.067)</td><td>0.002(0.004)</td><td>-0.010(0.010)</td></tr><tr><td>Price</td><td>0.454***(0.094)</td><td>0.002(0.004)</td><td>-0.045***(0.015)</td></tr><tr><td>Seller Average Tenure</td><td>-0.059(0.138)</td><td>0.001(0.007)</td><td>-0.032S(0.023)</td></tr></table>

$$
p (y _ {i t}) = \frac {\Gamma (\alpha + y _ {i t})}{\Gamma (\alpha) \Gamma (y _ {i t} + 1)} \left(\frac {\alpha}{\alpha + \lambda_ {i t}}\right) ^ {\alpha} \left(\frac {\lambda_ {i t}}{\alpha + \lambda_ {i t}}\right) ^ {y _ {i t}},
$$

where α represents the extent of overdispersion, and Γ(·) is a gamma function. Therefore, the negative binomial model is also a Poisson-gamma mixture model. The conditional expectation $\lambda _ { i t }$ is structured as:

$$
E \left(y _ {i t}\right) = \lambda_ {i t} = \exp \left(s p o n s o r e d _ {i t} \tau_ {1} + s o c i a l _ {i t} \tau_ {2} + X _ {i t} \beta + \vartheta_ {i}\right).
$$

The dependent variable $y _ { i t }$ is the number of unique visitors seller i receives at time $t . \ \vartheta _ { i } \sim N ( 0 , \ \sigma _ { \vartheta } )$ is the random effects capturing individual seller heterogeneity;

Table 3. Notations in Empirical Model

<table><tr><td> $y_{it}$ </td><td>Dependent variable (Traffic or Sales)</td></tr><tr><td> $X_{it}$ </td><td>Vector of control variables in the traffic equation</td></tr><tr><td> $\pi_i$ </td><td>Latent variable</td></tr><tr><td> $\delta$ </td><td>Factor loading of latent variable</td></tr><tr><td> $\vartheta_i$ </td><td>Random effect in the traffic equation</td></tr><tr><td> $\omega_{it}$ </td><td>Vector of control variables in the selection equation</td></tr><tr><td> $\ln(\alpha)$ </td><td>Log-transformed overdispersion parameter of negative binomial model</td></tr></table>

$\tau _ { 1 }$ and $\tau _ { 2 }$ capture the treatment effects of advertising strategies; $X _ { i t }$ is a vector of control variables including reputation, average price, the number of repeat customers, and product variety.

The challenge of analyzing the effectiveness of the strategies is that the choice of the advertising strategies could be endogenous, because the important determinants of sellers using those strategies may be unobserved and that these unobservable effects may be correlated with the random component of the traffic model. It is likely that there could be shared unobserved heterogeneity for adopting the strategies and attracting traffic. For example, mature sellers may be more likely to adopt the strategies with their financial capability. Meanwhile, they tend to attract more traffic than new sellers do. Our model accommodates the potential endogeneity of the self-selection by including the latent variable $\pi _ { i }$ in both specifications. It is different from the fixed-effects panel model, where individual specific unobservables depend on observed covariates in an unspecified way. Instead, we use a parametric approach, which models out the depen dence between individual specific effects and the covariates, leaving only the common unobservables. We assume $\pi _ { i } \sim N ( 0 , \psi )$ , which is a factor representing shared unobserved heterogeneity, and δ is the factor loading. For ease of computation, we restrict $\psi = 1$ Below, we establish the traffic model as:

$$
\begin{array}{l} y _ {i t} ^ {*} = \log (\lambda_ {i t}) \\ = \text { sponsored } _ {i t} \tau_ {1} + \text { social } _ {i t} \tau_ {2} + X _ {i t} \beta + \vartheta_ {i} + \pi_ {i} \delta + \varepsilon_ {i t} ^ {1}, \\ \left[ \begin{array}{c} \pi_ {i} \\ \varepsilon_ {i t} ^ {1} \end{array} \right] \sim \mathcal {N} \left(\left[ \begin{array}{c c} 0 \\ 0 \end{array} \right], \left[ \begin{array}{c c} 1 & 0 \\ 0 & \sigma^ {2} \end{array} \right]\right). \end{array} \tag {1}
$$

We model sellers’ choices of each strategy that is driven by sellers’ specific variables indicative of their inclinations to pursue advertising strategies. Because we have two binary choice variables, we therefore use the bivariate probit model, which allows more than one equation with correlated disturbances, in the same spirit as the seemingly unrelated regression model (Greene 2012). Equations for probability of selecting sponsored search and probability of selecting social media endorsement are estimated simultaneously. Below, we show the selection equation.

$$
\begin{array}{r l} & z _ {1 i t} = \omega_ {i t} \gamma_ {1} + \pi_ {i} + \varepsilon_ {i t} ^ {2}, s p o n s o r e d _ {i t} \\ & \quad = 1 \mathrm{if} z _ {1 i t} > 0, s p o n s o r e d _ {i t} = 0 \mathrm{otherwise}, \end{array}\tag{2}
$$

$$
\begin{array}{r l} z _ {2 i t} & = \omega_ {i t} \gamma_ {2} + \pi_ {i} + \varepsilon_ {i t} ^ {3}, \text {   social } _ {i t} = 1 \text {   if   } z _ {2 i t} > 0, \text {   social } _ {i t} \\ & = 0 \text {   otherwise }, \end{array} \tag {3}
$$

$$
\left[ \begin{array}{l} \varepsilon_ {i t} ^ {2} \\ \varepsilon_ {i t} ^ {3} \end{array} \right] \sim \mathcal {N} \biggl (\left[ \begin{array}{l} 0 \\ 0 \end{array} \right], \left[ \begin{array}{l l} 1 & \rho \\ \rho & 1 \end{array} \right] \biggr), - 1 <   \rho <   1.
$$

Individual observations on sponsored and $s o c i a l _ { i t }$ are available for all i and $t . \ \varepsilon _ { i t } ^ { 2 } \sim \dot { N ( 0 , 1 ) }$ and $\varepsilon _ { i t } ^ { 3 } \sim N ( 0 , 1 )$ are the error terms. We specify $\omega _ { i t }$ as a vector of control variables, including past selection of strategies, last traffic level, seller tenure, average price, and product variety. Basically, sellers’ endogenous choices of the strategy are closely related to their own characteristics and heterogeneity. Therefore, we choose these variables that are relevant to sellers’ experiences, active level, and price level. First, as indicated by the panel VAR model, sellers’ selection of strategies is related to their past adoption of strategies and past performance. Second, new sellers and mature sellers may have very different goals and behaviors on the marketplace. Third, sellers with different price levels or product variety may attract different types of customers; thus, the behavior of them may also be different. Although it is desirable to include all the variables that could possibly affect sellers’ selection of the strategy, we include those variables that we have information on and use the latent variable and error term to capture unobserved effects.

Putting the above Equations (1), (2), and (3) together, we have the full model as follows:

$$
y _ {i t} ^ {*} = s p o n s o r e d _ {i t} \tau_ {1} + s o c i a l _ {i t} \tau_ {2} + X _ {i t} \beta + \vartheta_ {i} + \pi_ {i} \delta + \varepsilon_ {i t} ^ {1},
$$

$$
\begin{array}{r l} & z _ {1 i t} = \omega_ {i t} \gamma_ {1} + \pi_ {i} + \varepsilon_ {i t} ^ {2}, s p o n s o r e d _ {i t} \\ & \quad = 1 \mathrm{if} z _ {1 i t} > 0, s p o n s o r e d _ {i t} = 0 \mathrm{otherwise}, \\ & z _ {2 i t} = \omega_ {i t} \gamma_ {2} + \pi_ {i} + \varepsilon_ {i t} ^ {3}, s o c i a l _ {i t} = 1 \mathrm{if} z _ {2 i t} > 0, s o c i a l _ {i t} \\ & \quad = 0 \mathrm{otherwise}, \end{array}
$$

where we assume that the latent variable and all the error terms follow a multivariate normal distribution:

$$
\left( \begin{array}{c} \pi_ {i} \\ \varepsilon_ {i t} ^ {1} \\ \varepsilon_ {i t} ^ {2} \\ \varepsilon_ {i t} ^ {3} \end{array} \right) \sim \mathcal {N} \left(\left( \begin{array}{c} 0 \\ 0 \\ 0 \\ 0 \end{array} \right), \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & \sigma^ {2} & 0 & 0 \\ 0 & 0 & 1 & \rho \\ 0 & 0 & \rho & 1 \end{array} \right]\right).
$$

Our full model framework is adopted from Rabe-Hesketh and Skrondal (2012). We use a maximum likelihood approach to maximize the log-likelihood function conditional on the sum $\scriptstyle \sum _ { t = 1 } ^ { T } y _ { i t }$ . This conditional likelihood function does not depend on the unobserved $\pi _ { i } ,$ as it is transformed out. Hence, the estimator is consistent for the coefficients on the timevarying covariates, and it is asymptotically normal. We apply the same model framework to conduct the analyses on sales. Table 3 lists all the notations used in the empirical model.

5.2.1. Analysis Results on Traf<sup>fi</sup>c. We control for selection bias in estimated store traffic, and the results of the selection model are presented in Table A.2. Table 4 shows the results of the traffic model. In the base model, the estimated coefficient for sponsored search is 0.328, and it is highly significant $( p < 0 . 0 1 )$ ). The estimated coefficient of social media endorsement is 0.144, and it is highly significant as well $( p < 0 . 0 1 )$ ). Thus, sponsored search and social media endorsement are both effective strategies in boosting online traffic. Hypothesis 1 and 3 are both supported. If we interpret the coefficients in terms of the incidence rate ratio, our model shows that, on average, by using sponsored search, a seller can have 39% higher traffic than not using sponsored search. Similarly, by adopting social media endorsement, sellers, on average, can have 15% higher traffic than not using this tool. We also conduct a Wald test to compare the effect size of the two strategies, which shows that sponsored search has a significantly larger effect on traffic than social media endorsement $( \chi ^ { 2 ^ { \vee } } = 1 5 5 . 2 6 , ~ p < 0 . 0 0 1 )$ ). Additionally, based on base model (II), the interaction term between sponsored search and social media endorsement is <sup>−</sup>0.142 and is highly significant $( p < 0 . 0 0 1 )$ ), indicating that the two strategies are partially substitutive to each other.

The interaction model in Table 4 presents how the two advertising strategies work contingent on seller reputation. First, the results show that sponsored search is a more effective tool in boosting traffic for sellers with lower reputation, with the coefficient estimation of $- 0 . 0 6 3 \ : \ : \overline { { ( p \mathrm { ~ < ~ } 0 . 0 1 ) } }$ for the interaction term of sponsored search and reputation. Therefore, Hypothesis 5(b) is supported, which suggests that, with the presence of sponsored search advertising, reputation is more of a traffic-generation mechanism as opposed to signaling. By generating traffic through an organic search list, reputation can to some extent substitute for sponsored search advertising. However, the interaction term between social media endorsement and seller reputation is not significant, suggesting that the effectiveness of social media endorsement in boosting traffic is not significantly different for highand low-reputation sellers. Therefore, Hypothesis 6 is not supported. We speculate that this interaction is not significant because social media endorsers may not post the reputation-related information in their endorsing posts, thus making seller reputation not relevant in how social media endorsement influences traffic. Our example of social media endorsement provided in Figure 2 does not contain the reputation information. However, we do not have data on the percentage of posts that mention seller reputation and the ones that don’t.

Table 4. Traffic Equation Estimates for Advertising Strategies

<table><tr><td>Variable</td><td>Base model (I)</td><td>Base model (II)</td><td>Interaction model</td></tr><tr><td>Reputation</td><td>0.185***(0.008)</td><td>0.183***(0.009)</td><td>0.186***(0.009)</td></tr><tr><td>Product Variety</td><td>0.256***(0.009)</td><td>0.256***(0.009)</td><td>0.250***(0.008)</td></tr><tr><td>Return Customer</td><td>0.486***(0.008)</td><td>0.486***(0.008)</td><td>0.485***(0.008)</td></tr><tr><td>Sponsored</td><td>0.328***(0.030)</td><td>0.381***(0.034)</td><td>0.784***(0.092)</td></tr><tr><td>Social</td><td>0.144***(0.026)</td><td>0.244***(0.041)</td><td>0.228***(0.084)</td></tr><tr><td>Sponsored × Social</td><td></td><td>-0.142***(0.044)</td><td></td></tr><tr><td>Sponsored × Reputation</td><td></td><td></td><td>-0.063***(0.012)</td></tr><tr><td>Social × Reputation</td><td></td><td></td><td>-0.0003(0.010)</td></tr><tr><td>Constant</td><td>3.674***(0.062)</td><td>3.666***(0.062)</td><td>3.699***(0.060)</td></tr><tr><td> $\sigma_{\delta}$ </td><td>0.024</td><td>0.024</td><td>0.813</td></tr><tr><td> $\delta$ </td><td>0.227</td><td>0.229</td><td>-0.250</td></tr><tr><td>ln( $\alpha$ )</td><td>-0.722</td><td>-0.723</td><td>-0.734</td></tr></table>

Notes. Total number of observations, N = 21,203. All the continuous variables are log-transformed. Standard errors are presented in parentheses \*\*\*p < 0.01.

5.2.2. Analysis Results on Sales. The results of analyses on sales are presented in Table 5. The base model results show that the coefficient estimate of sponsored search is 0.205 and is significant $( p < 0 . 0 1 )$ . However, the coefficient estimate of social media endorsement is not significant, suggesting that social media endorsement has no significant, direct impact on sales. Also, the coefficient of the interaction term between sponsored search and social media endorsement is 0.087 and is marginally significant $( p ~ < ~ 0 . 1 )$

The interaction model shows that the interaction coefficient between sponsored search and reputation is 0.037 and is highly significant $( p < 0 . 0 1 )$ , suggesting that sponsored search is more effective in boosting sales for high-reputation sellers than for low-reputation ones. Additionally, the interaction coefficient between social media endorsement and reputation is 0.029 and is also significant $( p < 0 . 0 1 )$ . Because the overall effect of social media endorsement on sales is not significant, the significant interaction effect indicates that only high-reputation sellers are able to boost sales by adopting social media endorsement.

## 5.3. Robustness Test

To further confirm the main effect of both strategies on increasing traffic, we use the matching techniques as robustness checks. We compute the probability of a seller adopting the strategy as a treatment based on their characteristics. Then, we match sellers who resemble each other in all relevant characteristics and compare the impact on traffic by using each strategy. Specifically, we match the sellers based on their previous level of traffic, the number of repeat customers, the number of product variety, the average number of new products launched, and average product price. Because we have two binary choice variables, we have to first match sellers that not only have similar characteristics, but also have the same decision on adopting one of the strategies, and then we treat the adoption of the other strategy as a treatment. We conduct matching based on a split sample, where we create two matching scenarios for sellers adopting either one of the strategies: (1) Matching sellers only adopt sponsored search with those that have not adopted any strategies; and (2) matching sellers who only adopt social media endorsement with those that have not adopted any strategies. We use the log-transformed traffic variable and sales variable as the outcome variable and calculate the aftertreatment effect for each strategy on the outcomes. For scenario (1), we are able to match 155 treated sellers with the same number of control-group sellers. For scenario (2), we are able to match 129 treated sellers with the same number of control-group sellers.

Table 5. Sales Equation Estimates for Advertising Strategies

<table><tr><td>Variable</td><td>Base model (I)</td><td>Base model (II)</td><td>Interaction model</td></tr><tr><td>Reputation</td><td>0.042***(0.008)</td><td>0.043***(0.008)</td><td>0.040***(0.008)</td></tr><tr><td>Product Variety</td><td>0.129***(0.009)</td><td>0.129***(0.009)</td><td>0.133***(0.009)</td></tr><tr><td>Return Customer</td><td>0.686***(0.008)</td><td>0.685***(0.008)</td><td>0.674***(0.008)</td></tr><tr><td>Sponsored</td><td>0.205***(0.034)</td><td>0.173***(0.032)</td><td>-0.108(0.090)</td></tr><tr><td>Social</td><td>0.002(0.026)</td><td>-0.058(0.040)</td><td>-0.347***(0.084)</td></tr><tr><td>Sponsored × Social</td><td></td><td>0.087*(0.044)</td><td></td></tr><tr><td>Sponsored × Reputation</td><td></td><td></td><td>0.037***(0.012)</td></tr><tr><td>Social × Reputation</td><td></td><td></td><td>0.029***(0.010)</td></tr><tr><td>Constant</td><td>0.846***(0.057)</td><td>0.851***(0.057)</td><td>0.924***(0.059)</td></tr><tr><td> $\sigma_{\vartheta}$ </td><td>0.042</td><td>0.042</td><td>0.441</td></tr><tr><td> $\delta$ </td><td>0.171</td><td>0.168</td><td>0.193</td></tr><tr><td>ln( $\alpha$ )</td><td>-0.452</td><td>-0.451</td><td>-0.457</td></tr></table>

Notes. Total number of observation, N = 21,203. All the continuous variables are log-transformed Standard errors are presented in parentheses.  
\*p < 0.10; \*\*\*p < 0.01.

Table 6 and Table 7 show the detailed propensity score matching results for the two scenarios. For scenario (1), the after-treatment effect of using sponsored search is highly significant when we have log-transformed traffic as the outcome variable (t-stat = 4.73) and is also highly significant when we have log-transformed sales as the outcome variable (t-stat = 4.78). For scenario (2), the after-treatment effect of using social media endorsement is highly significant on traffic (t-stat = 2.85), but not significant on sales (t-stat = 0.34). To further ensure the quality of the propensity-scorematching procedure, we check whether the covariates are balanced between the treatment and control groups in the prematching and postmatching conditions. We provide the covariate comparison before and after matching in Table A.4.

## 6. Discussions and Implications

The results of our analyses corroborate that both sponsored search and social media endorsement play important roles in increasing traffic, with sponsored search advertising being more effective than social media endorsement. We also find that the two advertising strategies, sponsored search and social media endorsement, are partially substitutive. Although sellers who employ both sponsored search and social media endorsement are able to attract more traffic than those who only use one tool, the marginal effect of sponsored search as well as social media endorsement is lower when the other advertising tool is also used. It is possible that some potential customers are exposed to both advertising mechanisms, which lowers the marginal effect of each tool. Additionally, we find that the effectiveness of the two strategies on increasing sales is different, as only sponsored search has a positive and significant impact on sales. We further examine the differential effects of these two advertising strategies for sellers with low and high reputation. Results show that sponsored search is more effective in increasing traffic for low-reputation sellers, but is more effective in increasing sales for high-reputation sellers. Moreover, social media endorsement increases traffic for sellers regardless of seller reputation, whereas social media endorsement is more effective in increasing sales for highreputation sellers. This result indicates that the main function of social media endorsement is to attract consumers to visit, or, in other words, consumers may use the social media channel to gather information, but may not consummate the purchase through that channel, which is consistent with the findings by Li and Kannan (2014).

Table 6. Propensity Score Matching: Sponsored Search Adoption vs. No Advertising

<table><tr><td>Outcome variable</td><td>Sample</td><td>Treated</td><td>Controls</td><td>Difference</td><td>Standard error</td><td>t-stat</td></tr><tr><td rowspan="2">Log(Traffic)</td><td>Unmatched</td><td>8.141</td><td>7.124</td><td>1.017</td><td>0.156</td><td>6.50</td></tr><tr><td>ATT</td><td>8.141</td><td>7.154</td><td>0.987</td><td>0.289</td><td>4.73</td></tr><tr><td rowspan="2">Log(Sales)</td><td>Unmatched</td><td>4.246</td><td>3.210</td><td>1.036</td><td>0.133</td><td>7.81</td></tr><tr><td>ATT</td><td>4.246</td><td>3.388</td><td>0.858</td><td>0.179</td><td>4.78</td></tr></table>

Note. ATT, average treatment effects of the treated.

Table 7. Propensity Score Matching: Social Media Endorsement Adoption vs. No Advertising

<table><tr><td>Outcome variable</td><td>Sample</td><td>Treated</td><td>Controls</td><td>Difference</td><td>Standard error</td><td>t-stat</td></tr><tr><td rowspan="2">Log(Traffic)</td><td>Unmatched</td><td>7.390</td><td>7.124</td><td>0.266</td><td>0.172</td><td>1.55</td></tr><tr><td>ATT</td><td>7.390</td><td>6.690</td><td>0.700</td><td>0.245</td><td>2.85</td></tr><tr><td rowspan="2">Log(Sales)</td><td>Unmatched</td><td>3.586</td><td>3.210</td><td>0.376</td><td>0.146</td><td>2.59</td></tr><tr><td>ATT</td><td>3.586</td><td>3.519</td><td>0.067</td><td>0.196</td><td>0.34</td></tr></table>

Note. ATT, average treatment effects of the treated

Our study provides important practical implications to sellers as well as to e-commerce platforms. First, our analysis suggests that, in general, sponsored search is a more effective way than social media endorsement in increasing traffic and, perhaps more importantly, sales for sellers. Therefore, sponsored search is generally preferred over social media endorsement if a seller is seeking ways to increase traffic and sales. In a way, this result validates the strength of the advertising business model for e-commerce platforms. If sponsored search advertising is effective, other e-commerce platforms could consider adopting sponsored search ads and potentially generate more revenues through this feature. As Amazon is increasingly incorporating sponsored product ads in its platform, rival platforms, such as eBay, should consider embracing it as well.

Second, although sponsored search is more effective in increasing traffic for sellers with lower reputation, it is more effective in increasing sales for higherreputation sellers. Such contrasting effects indicate that high-reputation sellers are more capable in turning incoming traffic into final sales, which is consistent with the existing literature. The implication is that new sellers should aim to increase their reputation scores in the long term. In the short run, they need to engage in more efforts—than high-reputation sellers—to send positive signals on their prices and product quality as well as their services, so that they can more effectively turn the incoming traffic into sales. For example, low-reputation sellers should consider offering a more competitive price than high-reputation sellers. Also, they should consider embracing the no-reason-needed return policy, which can increase the confidence and reduce the concerns the potential customers have in the lowreputation sellers. Finally, low-reputation sellers should also respond in a more timely and passionate manner to customers’ questions and requests, thus sending signals on their high-quality service despite their currently low reputation score. These efforts will lead to longterm benefits. If these sellers are able to convert traffic, they are more likely to increase their product rating and reputation, which are useful to attract organic, unpaid traffic, and increase conversion in the future.

Third, we suggest that low-reputation sellers should not, perhaps, expect substantial increase in sales from social media endorsement. Although social media endorsement can increase traffic, it does not significantly increase sales immediately, at least for low-reputation sellers, perhaps because the potential customers attracted through social media endorsement do not have a strong purchase intention to start with. According to the Elaboration Likelihood Model of Persuasion (Petty and Cacioppo 1981, 1986), these potential customers are likely to be making faster decisions and are mostly influenced by the easily accessible cues rather than looking deeper into the quality and other characteristics of the product and the seller. As such, the low reputation is more likely to give these potential customers— attracted through social media endorsement—a pause in the final purchase decision. In contrast, customers attracted through sponsored search have a specific purchase intention and have perhaps done some research on the important aspects of the product. Thus, they will be less swayed by the seller reputation, and the low-reputation sellers may still have a good chance in converting them into sales with other efforts in sending positive signals as described above.

Fourth, from the perspective of platforms, there are increasing competitions among them. In China, JD.com challenges Taobao. In the United States there are new entrants such as Etsy and Shopify. It is important for a platform to understand the roles of various players in the multisided market and come up with tailored strategies. For example, social endorsers are a new type of players in the marketplace that can perform an indispensable role. Social media endorsement can be a valuable tool for established sellers to attract new customers and increase their number of unique active users, which is an important index for their performance. These new customers, who are not triggered by specific purchase intentions, are exactly the new type of customer both the sellers and a platform should cultivate in the long run. Also, because high-reputation sellers have a stronger capability in turning the traffic from social media endorsement into sales, platforms should try to sell the social media endorsement advertising strategy to higher-reputation sellers. This is advisable because high-reputation sellers are more capable of turning these visitors into buyers and—perhaps more importantly—into returned and loyal customers to the platform. Moreover, for lowreputation sellers, platforms could help them develop an effective sponsored search advertising campaign so that they can better compete with established sellers. For instance, platforms can offer analytics tools to help new sellers improve the targeting of their ads by using the right keywords and right messages. Additionally, platforms could help advise lower-reputation sellers on how to increase their reputation, and, equally important, on how to send positive signals to convince customers of the quality of their products and services despite their currently low reputation.

## 7. Concluding Remarks and Future Research

Using data from the Taobao marketplace, we examine how the choices of two important advertising strategies provided by the platform affect online traffic and sales for heterogeneous sellers. Our findings unveil the relative effectiveness of the two strategies, the substitutive nature of the two strategies, and the differential effects of the two strategies on traffic and sales for sellers with higher or lower reputation. Accordingly, our findings provide important practical implications not only to sellers in e-commerce marketplaces, but also to e-commerce platform organizers.

Meanwhile, we believe there are several possible extensions of this study. First, although we discuss the general effect of seller reputation in the theory development, our empirics are bounded by the specific reputation mechanism used by Taobao. Taobao’s reputation score is an aggregate of feedback scores from every transaction and is thus heavily influenced by the accumulative volume of transactions a seller has. In contrast, eBay uses the “percentage of positive feedback” as the reputation index, which is less influenced by the number of the transactions a seller has. What’s more, Amazon does not provide an index on seller reputation but only the reviews (number of reviews and the average rating) on a specific product. Therefore, it is worth investigating whether different seller reputation indices (or product reviews, in Amazon’s case) might lead to different conclusions on the effect of seller reputation. Second, our sample is limited to one product category (i.e., women’s fashion) in the marketplace. Consumer and seller be haviors might be different when it comes to the sales of other product types. Therefore, checking for generalizability of results across different marketplaces or product categories would be interesting for future research. Also, it would be interesting to test whether there are differential effects of the two advertising tools for products that are experience goods and those that are search goods. Third, researchers can examine whether advertising models can complement other business models, such as transaction-fee-based ones Lastly, as our data set only provides information on seller behaviors on the marketplace, we are not able to see the dynamics of the seller–buyer interactions driven by the two different advertising tools. Thus, future research can consider studying how the two advertising tools work differently based on consumer behaviors.

## Acknowledgments

The authors thank Senior Editor Alessandro Acquisti, Associate Editor Wenjing Duan, and the two anonymous reviewers for their helpful and constructive suggestions throughout the review process. The authors thank participants at the 2014 INFORMS Conference on Information Systems and Technology and Information Systems Workshop at Arizona State University for their valuable comments.

Appendix

Table A.1. Panel VAR Model Selection

<table><tr><td>Lag</td><td>CD</td><td>J</td><td>J p-value</td><td>MBIC</td><td>MAIC</td><td>MQIC</td></tr><tr><td>1</td><td>0.99985</td><td>150.45800</td><td>0.00000</td><td>-95.21400</td><td>96.45797</td><td>31.21731</td></tr><tr><td>2</td><td>0.99987</td><td>24.14704</td><td>0.15027</td><td>-139.63430</td><td>-11.85296</td><td>-55.34673</td></tr><tr><td>3</td><td>0.99979</td><td>7.13878</td><td>0.62267</td><td>-74.75188</td><td>-10.86122</td><td>-32.60811</td></tr></table>

Notes. CD, coefficient of determination; J, Hansen’s J; MBIC, Bayesian information criterion; MAIC: Akalike information criterion; MQIC: Hannan–Quinn information criterion. Based on the three model selection criteria by Andrews and Lu (2001), we should pick the model with the smallest MBIC, MAIC, and MQIC.

Table A.2. Bivariate Probit Estimates for Traffic Selection Model

<table><tr><td>Variable</td><td>SponsoredSearch</td><td>SocialEndorsement</td></tr><tr><td>L.Traffic</td><td>0.049**(0.027)</td><td>-0.074***(0.020)</td></tr><tr><td>L.SponsoredSearch</td><td>13.323(24402.82)</td><td>0.545***(0.058)</td></tr><tr><td>L.SocialMediaEndorsment</td><td>0.531***(0.086)</td><td>5.082***(0.052)</td></tr><tr><td>Seller Tenure</td><td>-0.307***(0.045)</td><td>-0.066**(0.032)</td></tr><tr><td>Average Price</td><td>-0.031(0.044)</td><td>-0.158***(0.029)</td></tr><tr><td>Product Variety</td><td>-0.023(0.034)</td><td>0.088***(0.024)</td></tr><tr><td>Constant</td><td>-1.182***(0.298)</td><td>-1.492***(0.219)</td></tr></table>

Notes. Total number of observations, N = 21,203. All the continuous variables are log-transformed. Standard error is in parentheses.  
\*\*p < 0.05; \*\*\*p < 0.01.

Table A.3. Bivariate Probit Estimates for Sales Selection Model

<table><tr><td>Variable</td><td>SponsoredSearch</td><td>SocialEndorsement</td></tr><tr><td>L.Traffic</td><td>0.065**(0.025)</td><td>-0.064***(0.020)</td></tr><tr><td>L.SponsoredSearch</td><td>11.788(193.016)</td><td>0.491***(0.058)</td></tr><tr><td>L.SocialMediaEndorsment</td><td>0.541***(0.087)</td><td>5.133***(0.052)</td></tr><tr><td>Seller Tenure</td><td>-0.311***(0.046)</td><td>-0.054*(0.032)</td></tr><tr><td>Average Price</td><td>0.026(0.045)</td><td>-0.095***(0.029)</td></tr><tr><td>Product Variety</td><td>0.010(0.035)</td><td>0.083***(0.023)</td></tr><tr><td>Constant</td><td>-1.494***(0.305)</td><td>-1.918***(0.227)</td></tr></table>

Notes. Total number of observations, N = 21,203. All the continuous variables are log-transformed. Standard error is in parentheses.  
\*p < 0.10; \*\*p < 0.05; \*\*\*p < 0.01.

Table A.4. Covariate Comparison Before and After Matching

<table><tr><td rowspan="3">Variable</td><td rowspan="2">Treatment group</td><td colspan="8">Control group</td></tr><tr><td colspan="4">Before match</td><td colspan="4">After match</td></tr><tr><td>Mean</td><td>Mean</td><td>Mean difference</td><td>t-stat</td><td>Variance of ratio</td><td>Mean</td><td>Mean difference</td><td>t-stat</td><td>Variance of ratio</td></tr><tr><td colspan="10">Sponsored search adoption vs. no advertising</td></tr><tr><td>L.Traffic</td><td>7.2931</td><td>7.1152</td><td>0.1779</td><td>1.13</td><td>1.03</td><td>7.141</td><td>0.1521</td><td>0.67</td><td>0.92</td></tr><tr><td>Seller Tenure</td><td>5.5868</td><td>6.0182</td><td>-0.4314</td><td>-5.15</td><td>0.97</td><td>5.5812</td><td>0.0056</td><td>0.05</td><td>1.02</td></tr><tr><td>Product Variety</td><td>4.9747</td><td>5.0536</td><td>-0.0789</td><td>-0.79</td><td>0.72</td><td>5.0142</td><td>-0.0395</td><td>-0.28</td><td>0.57</td></tr><tr><td>New Product</td><td>1.1321</td><td>0.80565</td><td>0.32645</td><td>4.55</td><td>1.01</td><td>1.2041</td><td>-0.072</td><td>-0.67</td><td>0.79</td></tr><tr><td>Average Price</td><td>4.7489</td><td>4.8667</td><td>-0.1178</td><td>-1.55</td><td>0.75</td><td>4.8145</td><td>-0.0656</td><td>-0.68</td><td>0.82</td></tr><tr><td colspan="10">Social media endorsement adoption vs. no advertising</td></tr><tr><td>L.Traffic</td><td>6.5478</td><td>7.1152</td><td>-0.5674</td><td>-3.3</td><td>1.17</td><td>6.5437</td><td>0.0041</td><td>0.02</td><td>1.05</td></tr><tr><td>Seller Tenure</td><td>5.4292</td><td>6.0182</td><td>-0.589</td><td>-6.43</td><td>0.99</td><td>5.6252</td><td>-0.196</td><td>-1.49</td><td>0.89</td></tr><tr><td>Product Variety</td><td>5.3122</td><td>5.0536</td><td>0.2586</td><td>2.36</td><td>0.77</td><td>5.2174</td><td>0.0948</td><td>0.64</td><td>0.7</td></tr><tr><td>New Product</td><td>1.4094</td><td>0.80565</td><td>0.60375</td><td>7.67</td><td>1.26</td><td>1.3369</td><td>0.0725</td><td>0.56</td><td>0.83</td></tr><tr><td>Average Price</td><td>4.5575</td><td>4.8667</td><td>-0.3092</td><td>-3.73</td><td>0.53</td><td>4.5945</td><td>-0.037</td><td>-0.41</td><td>0.76</td></tr></table>

Note. All the continuous variables are log-transformed.

## References

Agarwal A, Hosanagar K, Smith MD (2015) Do organic results help or hurt sponsored search performance? Inform. Systems Res. 26(4): 695–713.

Agrawal J, Kamakura WA (1995) The economic worth of celebrity endorsers: An event study analysis. J. Marketing 59(3):56–62.

Alibaba Group (2015) 2015 annual report of the Alibaba Group. Accessed February 8, 2016, http://www.alibabagroup.com/en/ ir/secfilings.

Anderson SP, Renault R (2006) Advertising content. Amer. Econom. Rev. 96(1):93–113.

Andrews DWK, Lu B (2001) Consistent model and moment selection procedures for GMM estimation with application to dynamic panel data models. J. Econometrics 101(1):123–164.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Walker D (2012) Identifying influential and susceptible members of social networks. Science 337(6092):337–341.

Athey S, Ellison G (2011) Position auctions with consumer search. Quart. J. Econom. 126(3):1213–1270.

Bagwell K (2007) The economic analysis of advertising. Armstrong M, Porter R, eds. Handbook of Industrial Organization, vol. 3 (Elsevier, Amsterdam), 1701–1844.

Bakshy E, Eckles D, Yan R, Rosenn I (2012) Social influence in social advertising: Evidence from field experiments. Working paper, Facebook, Menlo Park, CA.

Baye MR, los Santos BD, Wildenbeest MR (2016) Search engine optimization: What drives organic traffic to retail sites? J. Econom. Management Strategy 25(1):6–31.

Benbunan-Fich R, Fich EM (2004) Effects of web traffic announce ments on firm value. Internat. J. Electronic Commerce 8(4):161–181.

Bhargava HK, Choudhary V (2004) Economics of an information intermediary with aggregation benefits. Inform. Systems Res. 15(1): 22–36.

Bickart B, Schindler RM (2001) Internet forums as influential sources of consumer information. J. Interactive Marketing 15(3):31–40.

Blake T, Nosko C, Tadelis S (2015) Consumer heterogeneity and paid search effectiveness: A large-scale field experiment. Econometrica 83(1):155–174.

Butler RJ, Cowan BW, Nilsson S (2005) From obscurity to bestseller: Examining the impact of Oprah’s Book Club selections. Public Res. Quart. 20(4):23–34.

Chan DX, Yuan Y, Koehler J, Kumar D (2011a) Incremental clicks: The impact of search advertising. J. Advertising Res. 51(4):643–647.

Chan TY, Wu C, Xie Y (2011b) Measuring the lifetime value of customers acquired from Google search advertising. Marketing Sci. 30(5):837–850.

Chatterjee P, Hoffman D, Novak T (2003) Modeling the clickstream: Implications for web-based advertising efforts. Marketing Sci. 22(4):520–541.

Chen H, De P, Hu YJ (2015) IT-enabled broadcasting in social media: An empirical study of artists’ activities and music sales. Inform. Systems Res. 26(3):513–531.

Chen J, Fan M, Li M (2016) Advertising versus brokerage model fo online trading platforms. MIS Quart. 40(3):575–596.

Chen S, Shechter D, Chaiken S (1996) Getting at the truth or getting along: Accuracy- vs. impression-motivated heuristic and sys tematic processing. J. Personality Soc. Psych. 71(2):262–275.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Cialdini RB (2001) Harnessing the science of persuasion. Harvard Bus. Rev. 79(9):72–79.

Clemons E, Gao G, Hitt L (2006) When online reviews meet hyper differentiation: A study of the craft beer industry. J. Management Inform. Systems 23(2):149–171.

Dellarocas C, Zhang XM, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Dewan RM, Freimer ML, Zhang J (2002) Management and valuation of advertisement-supported web sites. J. Management Inform. Systems 19(3):87–98.

Dreze X, Zufryden F (2004) Measurement of online visibility and its\` impact on Internet traffic. J. Interactive Marketing 18(1):20–37.

Duan W, Gu B, Whinston AB (2008) The dynamics of online wordof-mouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242

Elfenbein DW, Fisman R, Mcmanus B (2012) Charity as a substitute for reputation: Evidence from an online marketplace. Rev Econom. Stud. 79(4):1441–1468.

Fang X, Hu PJ-H, Li ZL, Tsai W (2013) Predicting adoption probabilities in social networks. Inform. Systems Res. 24(1):128–145.

Fort TC, Haltiwanger J, Jarmin RS, Miranda J (2013) How firms respond to business cycles: The role of firm age and firm size. IMF Econom. Rev. 61(3):520–559.

Friestad M, Wright P (1994) The persuasion knowledge model: How people cope with persuasion attempts. J. Consumer Res. 21(1):1–31.

Gallino S, Moreno A (2014) Integration of online and offline channels in retail: The impact of sharing reliable inventory availability information. Management Sci. 60(6):1434–1451.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Greene WH (2012) Econometric Analysis, 7th ed. (Prentice Hall, Boston).

Gu B, Park J, Konana P (2012) The impact of external word-of-mouth sources on retailer sales of high-involvement products. Inform. Systems Res. 23(1):182–196.

Guo W, Main KJ (2012) The vulnerability of defensiveness: The impact of persuasion attempts and processing motivations on trust. Marketing Lett. 23(4):959–971.

Hausman J, Hall BH, Griliches Z (1984) Econometric models for count data with an application to the patents-R&D relationship. Econometrica 52(4):909–938.

Heckman JJ (1979) Sample selection bias as a specification error. Econometrica 47(1):153–161.

Hui X, Saeedi M, Shen Z, Sundaresan N (2016) Reputation and reg ulations: Evidence from eBay. Management Sci. 62(12):3604–3616.

iResearch (2014) With revenue of \$7.5 billion in 2013, Alibaba restarts IPO. Accessed March 24, 2019, http://www.iresearchchina.com/ content/details7\_15533.html

Iyengar R, den Bulte CV, Valente TW (2011) Rejoinder—Further reflections on studying social influence in new product diffusion. Marketing Sci. 30(2):230–232.

Jeziorski P, Segal I (2015) What makes them click: Empirical analysis of consumer demand for search advertising. Amer. Econom. J. Microeconom. 7(3):24–53.

Jin GZ, Kato A (2006) Price, quality, and reputation: Evidence from an online field experiment. RAND J. Econom. 37(4):983–1005.

Li H, Kannan PK (2014) Attributing conversions in a multichannel online marketing environment: An empirical model and a field experiment. J. Marketing Res. 51(1):40–56.

Liaukonyte J, Teixeira T, Wilbur KC (2015) Television advertising and online shopping. Marketing Sci. 34(3):311–330.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Lu X, Ba S, Huang L, Feng Y (2013) Promotional marketing or wordof-mouth? Evidence from online restaurant reviews. Inform. Systems Res. 24(3):596–612.

Lundgren SR, Prislin R (1998) Motivated cognitive processing and attitude change. Personality Soc. Psych. Bull. 24(7):715–726.

Luo X, Zhang J (2013) How do consumer buzz and traffic in social media marketing predict the value of the firm? J. Management Inform. Systems 30(2):213–238.

Mims C (2018) How Amazon’s ad business could threaten Google and Facebook. Wall Street Journal (January 28), https://www.wsj .com/articles/how-amazons-ad-business-could-threaten-google -and-facebook-1517157327.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Moqri M, Mei X, Qiu L, Bandyopadhyay S (2018) Effect of “following” on contributions to open source communities. J. Management In form. Systems 35(4):1188–1217.

Narayanan S, Kalyanam K (2015) Position effects in search advertising and their moderators: A regression discontinuity approach. Marketing, Sci, 34(3):388–407.

Nelson P (1974) Advertising as information. J. Political Econom. 82(4):729–754

Oestreicher-Singer G, Sundararajan A (2012) Recommendation net works and the long tail of electronic commerce. MIS Quart. 36(1): 65–84.

Osawa J (2013) How does Alibaba make money? Wall Street Journal (September 9), http://blogs.wsj.com/digits/2013/09/09/how -does-alibaba-make-money/.

Peng J, Van den Bulte C (2016) Participation vs. effectiveness of paid endorsers in social advertising campaigns: A field experiment. Working paper, University of Connecticut, Storrs.

Perdikaki O, Kesavan S, Swaminathan J (2012) Effect of traffic on sales and conversion rates of retail stores. Manufacturing Ser vices Oper. Management 14(1):145–162.

Petty RE, Cacioppo JT (1981) Attitudes and Persuasion–Classic and Con temporary Approaches (W.C. Brown Co. Publishers, Dubuque, IA).

Petty RE, Cacioppo JT (1986) The elaboration likelihood model of persuasion. Petty RE, Cacioppo JT, eds. Communication and Persuasion: Central and Peripheral Routes to Attitude Change, Springer Series in Social Psychology (Springer, New York), 1–24.

Rabe-Hesketh S, Skrondal A (2012) Multilevel and Longitudinal Modeling Using Stata, 3rd ed. (Stata Press, College Station, TX)

Rob R, Fishman A (2005) Is bigger better? Customer base expansion through word-of-mouth reputation. J. Political Econom 113(5):1146–1162.

Rutz OJ, Trusov M, Bucklin RE (2011) Modeling indirect effects of paid search advertising: Which keywords lead to more future visits? Marketing Sci. 30(4):646–665.

Simon HA (1979) Rational decision making in business organizations. Amer. Econom. Rev. 69(4):493–513.

Soh C, Markus ML, Goh KH (2006) Electronic marketplaces and price transparency: Strategy, information technology, and success. MIS Quart. 30(3):705–723.

Starr JA, MacMillan IC (1990) Resource cooptation via social con tracting: Resource acquisition strategies for new ventures. Strategic Management J. 11(Special Issue: Corporate Entrepre neurship):79–92.

Steenkamp JBEM, Nijs VR, Hanssens DM, Dekimpe MG (2005) Competitive reactions to advertising and promotion attacks. Marketing Sci. 24(1):35–54

Susarla A, Oh J-H, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. System Res. 23(1):23–41.

Thies F, Wessel M, Benlian A (2016) Effects of social interaction dynamics on platforms. J. Management Inform. Systems 33(3): 843–873.

Trusov M, Bodapati AV, Bucklin RE (2010) Determining influential users in Internet social networks. J. Marketing Res. 47(4):643–658.

Tucker CE (2016) Social advertising: How advertising that explic itly promotes social influence can backfire. Working paper, Massachusetts Institute of Technology, Cambridge.

Wong G, Chu K (2015) The rat race to advertise on Alibaba’s market places. Wall Street Journal (March 3), http://www.wsj.com/articles the-race-to-advertise-on-alibabas-marketplaces-1425368909.

Wood W (2000) Attitude change: Persuasion and social influence. Annual Rev. Psych. 51(1):539–570.

Wu W (2018) Alibaba is an advertising company, more than an ecommerce one. The Low Down, Momentum Works (March 22), https://thelowdown.momentum.asia/alibaba-advertising-company -ecommerce-one/.

Wu J, Cook V, Strong E (2005) A two-stage model of the promotional performance of pure online firms. Inform. Systems Res. 16(4): 334–351.

Xu L, Chen J, Whinston A (2012) Effects of the presence of organic listing in search advertising. Inform. Systems Res. 23(4): 1284-1302.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.
