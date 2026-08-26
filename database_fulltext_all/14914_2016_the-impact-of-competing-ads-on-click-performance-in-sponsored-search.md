---
otero_id: 14914
otero_key: "YQESEA6A"
title: "The Impact of Competing Ads on Click Performance in Sponsored Search"
authors: "Ashish Agarwal; Tridas Mukhopadhyay"
year: "2016"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0637"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [147.8.31.43] On: 28 August 2016, At: 03:27 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/YQESEA6A/fulltext/images/4d6bc1e066104257485d6ecf80176b3af850d63c152f1e54c252aafc7b1f1d8e.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Impact of Competing Ads on Click Performance in Sponsored Search

Ashish Agarwal, Tridas Mukhopadhyay

To cite this article:

Ashish Agarwal, Tridas Mukhopadhyay (2016) The Impact of Competing Ads on Click Performance in Sponsored Search. Information Systems Research

Published online in Articles in Advance 02 Aug 2016

http://dx.doi.org/10.1287/isre.2016.0637

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2016, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/YQESEA6A/fulltext/images/bb1272ed11c714b68e47c79642f0a4af5916cd47e5712af0c93ec1eac4aee5de.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Impact of Competing Ads on Click Performance in Sponsored Search

Ashish Agarwal

McCombs School of Business, University of Texas at Austin, Austin, Texas 78712, ashish.agarwal@mccombs.utexas.edu

Tridas Mukhopadhyay

Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, tridas@cmu.edu

ur research examines the impact of competing ads on click performance of an ad in sponsored search. We use a unique data set of 1,267 advertiser keyword pairs with differing ad quality related to 360 keywords from a search engine to evaluate the click performance. We find that competing high-quality ads, appearing above the focal ad, have a lower negative effect on the click performance as compared to competing lowquality ads. We also find that this effect of competing ads varies with the ad position and the type of keyword. In general, the negative effect of competing high-quality ads decreases at low positions as compared to high positions. Furthermore, this decrease in the negative effect of competing high-quality ads is more substantial for specific keywords.

Our results reveal consumer behavior in evaluating different quality ads in sponsored search. More specifically, our results suggest that consumers use the presence of high-quality competing ads as a signal of higher quality of the focal ad. Our findings can help advertisers better evaluate their relative performance for different positions for various types of keywords. This can also help evaluate the efficacy of the auction design mechanism

Keywords: sponsored search; hierarchical Bayesian estimation; online advertising; online auctions; search engine marketing

History: Sanjeev Dewan, Senior Editor; Eric Zheng, Associate Editor. This paper was received on July 10, 2013, and was with the authors 13 months for 3 revisions. Published online in Articles in Advance August 2, 2016.

## 1. Introduction

Digital advertising spend is growing faster than any other form of advertising, and is expected to surge to \$67 billion in the United States in 2016 (eMarketer 2016). Forty-three percent of this ad spend is on sponsored search where advertisers pay to appear in a list alongside the algorithmic search results of a search engine. Sponsored search is widely regarded as one of the most effective forms of advertising because it occurs close to a user’s purchase decision and is matched based on the user’s stated information need. Most search engines including Google, Yahoo, and MSN use auctions to sell their inventory of ad space. In these auctions, advertisers submit bids on their ads for keywords based on their willingness to pay for every click from consumers searching on that (or a closely related) keyword. Search engines use a combination of the submitted bids and ads’ click potential for the keyword to rank the ads.<sup>1</sup> This click potential or quality varies across ads for the same keyword even if they are listed in the same position in separate sponsored search results (Katona and Savary 2010, Leong et al. 2012). A search engine internally measures this capability of an ad to generate clicks for a keyword using the notion of a quality score (Weber and Zheng 2007, Liu et al. 2010, Athey and Ellison 2011). Therefore, an important consideration is how the quality of competing ads influences the click performance of an ad.

In sponsored search, ad quality or the click potential of an ad for a keyword is consumers’ propensity to click on an ad.<sup>2</sup> This is based on the value they expect to get from visiting the related website.<sup>3</sup> However, they have to rely on the ad attributes to form this expectation. As a result, consumers respond differently to different ads while making their clicking decision even if they are listed in the same position in separate sponsored search results (Katona and Savary 2010, Leong et al. 2012). However, consumers are uncertain about the ad quality in this setup (Jeziorski and Segal 2015). Because of this uncertainty, consumers are typically known to sequentially evaluate sponsored search ads starting from the top position where they pay the most attention. Furthermore, because of the search costs of evaluation, fewer customers end up visiting lower positions (Arbatskaya 2007). Previous empirical studies have established that the click performance decays with position (Ghose and Yang 2009, Agarwal et al. 2011, Rutz and Trusov 2011, Rutz et al. 2012, Yao and Mela 2011). However, competing ads appearing before the focal ad can also influence the extent of search and, hence, the position-based click performance of an ad. For example, different competing ads with different click potential or quality can appear above the focal ad. Intuition would suggest that competing ads would negatively impact the click performance of a focal ad. In that case, the question is whether a competing ad with high click potential or quality, has a higher or lower negative impact on the click performance of the focal ad as compared to a competing ad with low quality.

One possibility is that the quality or click potential of the competing ad has no effect because it is the expected quality. However, previous studies (Animesh et al. 2011, Jeziorski and Segal 2015) show that ad attributes of competing ads do influence the click performance of the focal ad. In that case, another possibility is that a high-quality competing ad appearing above may impose a negative externality as users are just interested in acquiring information, and evaluation of a high-quality competing ad is more likely to lead to information satiation as compared to the evaluation of a low-quality competing ad (Jeziorski and Segal 2015). Alternatively, consumers may update their expectation of the quality of the focal ad based on the quality of competing ad appearing above (Athey and Ellison 2011). This learning may result in a lower negative impact of a high-quality competing ad appearing above on the focal ad as compared to a low-quality competing ad. Furthermore, consumers with different search behavior may differ in their learning effects. For example, users, who search more and visit low positions, are more involved and may exhibit a higher learning effect. Thus, the effect of competing ads may vary with position. Additionally, consumers using different keywords may differ in their search behavior and may respond to competing ads differently. For example, consumers using more specific keywords are known to be closer to their purchase decision (Ramlall et al. 2011). As a result, these consumers are likely to be more involved as compared to users who use generic keywords and may demonstrate a higher learning effect. Therefore, it is important to make a distinction between generic and specific keywords in studying the effect of competing ads on the click performance.

The impact of competing ads on the click performance of an ad has not received much attention in the literature barring two exceptions. For example, Jeziorski and Segal (2015) show evidence of higher negative impact of a high-quality competing ad as compared to a low-quality competing ad. However, they do not investigate how the impact varies with the ad position or keyword characteristics. Additionally, they only use four generic keywords in their analysis.<sup>4</sup> Animesh et al. (2011) evaluate the effect of competitive intensity at different positions for ads with different unique selling propositions. However, they identify competition solely based on the match of the unique selling proposition (USP) of the competition with that of the focal ad. Thus, their measure of competition only points to the presence or absence of competition and does not differentiate between different competitors based on their click potential or quality. Furthermore, they do not explore the role of keyword characteristics on the effect of competition.

The goal of this paper is to understand how competing ads influence the click performance of ads in sponsored search. However, to understand the impact of competing ads on click performance we must also consider the ad position and the nature of the keywords used for search (generic versus specific). In our empirical investigation, we analyze a unique panel data set from Yahoo, which catalogs bids, position, and click performance data. For our analysis, we consider a sample of 1,267 advertiser keyword pairs with differing ad quality related to 360 keywords. The resultant ads are displayed in various positions and generate clicks over a period of 93 days for these advertisers. We determine the quality ranking of ads based on their positions and bids for different keywords similar to the quality score measure defined by the search engine. We model the click decisions made by consumers as a function of the quality of competing ads appearing above and use a hierarchical Bayesian approach to account for the heterogeneity across keywords. We also consider the quality of competing ads appearing below each focal ad and account for unobservable advertiser characteristics for each keyword. We account for the endogeneity of the ad position due to the bid decisions made by the advertisers. We also correct for any potential endogeneity bias associated with the ad quality.

We have several key findings. First, our baseline results show that the relative quality of competing ads has an impact on the click performance of advertisers. More specifically, competing ads with higher quality that appear above have a lower negative effect on the click performance as compared to competing ads with lower quality. Second, we find that the effect of competing ads is a function of the position of the focal ad. This suggests that the arrangement of ads is important to determine the performance of an advertiser as a function of position. In general, the negative effect of the high-quality competing ads appearing above decreases with position and the negative effect of the low-quality competing ads increases with position. Finally, we find that this position-based effect of competing ads depends on the type of keyword. For generic keywords, we find that this difference in the effect of competing high- and low-quality ads does not change much with position. However, the difference increases for specific keywords. Specifically, the difference in the negative effect of competing high-quality ads and competing low-quality ads is higher for specific keywords as compared to generic keywords. This suggests that consumers using specific keywords are likely to respond to competing ads differently as compared to consumers using generic keywords.

Overall, our results help to understand consumer response to competing ads in sponsored search. More specifically, our results suggest the possibility of consumer learning in sponsored search as the presence of high-quality competing ads increases the click probability of the focal ad relative to the presence of low-quality competing ads. Furthermore, we show that this learning effect varies with the position and the type of the keyword representing differences in involvement and possibly the learning effect among consumers visiting different positions and using various types of keywords. These findings can help advertisers better evaluate their relative performance for different types of keywords and a variety of positions. We show that advertisers with a highquality ad have an additional incentive to bid high and attain top positions as they would experience a lower performance if preceded by low-quality ads.

Our results also inform the auction design mechanism as we demonstrate that the relative arrangement plays a role in determining the click performance and should be incorporated in the ad ranking mechanism. For example, our analysis suggests that the search engine can improve its revenue for our sample by 39% by listing ads in decreasing order of quality. Furthermore, our results inform existing theoretical work on the relative position-based performance of ads with different qualities.

The rest of the paper is organized as follows. We first review the related literature. Next, we discuss our research questions in light of the prior literature. In Section 4, we describe the data and the definition of key measures. In Section $5 ,$ we discuss the model and the estimation procedure. In Section 6, we explain our results. We discuss the implications of these results and conclude our paper in Section 7.

## 2. Previous Literature

Our work is related to consumer behavior in the sponsored search context with a specific focus on sequential search, the role of ad attributes, and competing ads.

## 2.1. Sequential Search

Prior work in online media has demonstrated that message ordering influences ad persuasion. For example, Hoque and Lohse (1999) find that consumers are more likely to choose advertisements near the beginning of an online directory than they are when using paper directories. Ansari and Mela (2003) have found that the higher position of links in email campaigns can lead to a higher probability of clicking. In the case of search results, there is evidence from eye tracking studies (Granka et al. 2004) to suggest that consumers do indeed focus on the top of the search results. While this can be attributed to attention, the click performance depends on how consumers choose what ads to click.

Consumers tend to associate the ad quality with its position (Jeziorski and Segal 2015) and as a consequence, consumers evaluate ads sequentially from top to bottom. In a sequential search, consumers evaluate the marginal gain in utility against the search cost at each stage (Adam 2001, Kim et al. 2010, Weitzman 1979). If consumers evaluate ads from the top, this would lower the probability of visiting ads in the lower positions. Single advertiser studies (Ghose and Yang 2009, Rutz and Trusov 2011, Agarwal et al. 2011, Rutz et al. 2012) have established that click performance of an ad decays with the position of the ad. This confirms the above user behavior and establishes the role of position in determining the click performance of advertisers. However, these studies do not distinguish between ads and the relative influence of their characteristics on search performance at different positions.

## 2.2. Ad Quality

Another important consideration is how the ad attributes affect the click performance. Consumers click on an ad based on the value they expect to get from the related website. However, they have to rely on the ad attributes to form this expectation. Animesh et al. (2011) establish that click performance of an ad depends on its unique selling proposition. Leong et al. (2012) find that consumers have a brand bias in clicking on search engine results. It is known that a brand serves as a signal of product or service quality (Jacoby et al. 1971, Wernerfelt 1988, Rao and Monroe 1989,

Erdem and Swait 2004). This confirms that consumers do pay attention to factors other than ad position and may demonstrate a propensity to click ads based on ad attributes. A search engine measures this ad capability to generate clicks for a keyword using the notion of a quality score (Liu et al. 2010, Athey and Ellison 2011).

Apart from an ad’s own quality, competing ads can also have an effect. As part of sequential evaluation, consumers are likely to evaluate competing ads appearing above the focal ad by evaluating the ad text. Consumers may also visit the ad site as part of this evaluation. Variation in this competition can influence the click performance of the focal ad. Agarwal et al. (2015) define ad competition based on the number of direct competitors and their Alexa rank and do not find any effect on the click performance of the focal ad after controlling for the ad position. Animesh et al. (2011) define competition in terms of the unique selling proposition such as quality or price information shown in the ad and show that intensity of such competition drives the click performance of an advertiser. Similarly, Jeziorski and Segal (2015) find that advertisers appearing higher up in the search results impose a negative externality on the lower ads and attribute it to information satiation. Additionally, they show that consumers are less likely to click on an ad if they have visited a high-quality competing ad as compared to the scenario where they have visited a low-quality competing ad.<sup>5</sup> On the other hand, Athey and Ellison (2011) suggest that advertisers appearing higher up can exert informational externality as consumers learn about the relevance of ads. However, they empirically do not establish this learning behavior. Dellaert and Haubl (2012) show that users are likely to terminate their search early when they sequentially evaluate a list of recommendations and there is high variability. In the search context, consumers may form an expectation about the quality of ads depending on their position. In that case, it is possible that customers may associate a high position of a low-quality ad with low quality of the focal ad and may not visit the focal ad and other ads appearing in lower positions. However, the impact of this change in the relative arrangement of competing ads on the click performance of an ad is not well established.

Search behavior can also be different across users. The keywords used by consumers can potentially reflect their search behavior. For example, a common belief in the industry is that the use of more specific keywords may reflect a higher proportion of buyers as compared to less specific keywords. Ramlall et al. (2011) confirm that users close to the purchase decision submit longer queries. Furthermore, as the search behavior changes with keywords, the consumer response to competing ads can also vary with keywords. Previous single advertiser studies (Ghose and Yang 2009, Agarwal et al. 2011, Rutz et al. 2012) consider the role of such keyword characteristics on the performance of an advertiser. However, they do not evaluate how keyword characteristics influence the impact of competing ads on the performance of an advertiser.

Thus, prior literature reveals that the user response to the ads in sponsored search depends on their position and on ad attributes. Furthermore, competing ads can also impact the click performance of an ad. However, the effect of the quality of competing ads and its interplay with the position and keyword characteristics on the click performance is not known.

## 3. Theory and Research Questions

Our objective is to evaluate how the click performance of an ad is influenced by the click potential or quality of the competing ads appearing above in sponsored search. Next, we describe a typical consumer search process on a search engine, the evaluation of ads, and our research questions in light of the existing literature.

The consumer search process involves the following steps (Figure 1):

(i) Consumers in different stages of their decision process (Jerath et al. 2014) conduct online search using an appropriate keyword. When consumers see the search results in response to their search keyword, they typically focus their attention at the top (Granka et al. 2004) and they start sequentially evaluating ads from top to bottom.

(ii) For each ad, consumers form their expectations of the ad quality for the product or service related to the keyword based on the ad content. Consumers’ probability of clicking an ad in any position depends on the expected value they can gain from visiting the related website and their search costs (Adam 2001, Kim et al. 2010, Weitzman 1979). Furthermore, for an ad appearing in any position except the top position, consumers would have evaluated one or more competing ads appearing above. They may also consider adjacent competing ads appearing below (Animesh et al. 2011). These competing ads can impose an externality on the focal ad and influence the consumer probability of clicking the ad. Click response can also vary across consumers depending on the stage of their decision process, their quality expectation, and search costs. Finally, consumer click response also depends on how knowledgeable they are.

(iii) After deciding whether or not to click the ad, consumers may continue their search by evaluating another ad or they may start another search session or abort the search process as they move to a different stage in their decision process.

Figure 1 Consumer Search Behavior  
![](/api/attachments/YQESEA6A/fulltext/images/cbb641d553ab326dd16fc09f5b546f27c91ae1669dde4bc536f46ac3f2f468a4.jpg)

Effects of the Quality of Competing Ads Appearing Above. Competing ads can impose a negative externality because of the fulfillment of consumer information needs or satiation (Jeziorski and Segal 2015). A high-quality competing ad is more likely to fulfill a consumer’s information needs leading to a higher negative externality as compared to a lowquality competing ad. Thus, for a given quality of the focal ad, if users see a high-quality competing ad instead of a low-quality competing ad appearing above the focal ad they may be less likely to visit the focal ad because of satiation. However, users may visit the focal ad in the presence of a low-quality competing ad above, with or without visiting the competing ad above.

Consumers can also update their belief about the quality of the focal ad based on the quality of the competing ad appearing above because of sequential evaluation. Athey and Ellison (2011) suggest the possibility of learning as consumers sequentially evaluate ads by clicking. However, consumers may update their belief just by reading the text of the competing ad if they decide not to visit the competing ad appearing above. Such learning from the competing ad may lead to an expectation of higher quality of the focal ad in the presence of a high-quality competing ad as compared to the presence of a low-quality competing ad. As a result, ads may get more clicks if they are preceded by high-quality ads as compared to lowquality ads.

Thus, consumers may either show a learning effect or a satiation effect. Furthermore, there can be heterogeneity in consumer evaluation of ad quality, which can also influence the externality effect. For example, some consumers may have niche preferences and may not agree with the general perception of the ad quality based on the overall propensity of consumers to click the ad. In that case, the externality effects may be reversed for such customers. Similarly, some users with high search costs may not follow the sequential search process and instead visit the ad with the highest expected quality inferred from the ad text. In that case, if the competing ad appearing above has a higher quality than the focal ad they may just visit the competing ad but may not do so if the competing ad has a lower quality than the focal ad. However, only a few consumers are likely to do so as suggested by the observed exponential decay in the click performance with ad position. Additionally, consumers may vary in their learning effects. For example, depending on the stage of their decision process, consumers can vary in their level of involvement (Jerath et al. 2014). Consumers spend more time attending to information as their involvement increases (Celsi and Olson 1988). This higher attention leads to better information processing (MacInnis and Jaworski 1989) and in turn, belief updating (Hogarth and Einhorn 1992). Similarly, differences in the knowledge level of customers would lead to differences in their information processing (Mitchell and Dacin 1996) and subsequent learning.

Table 1 Impact of Competition on Click Performance

<table><tr><td>Negative effect</td><td>Positive effect</td></tr><tr><td rowspan="2">Satiation effectConsumers are less likely to click a focal ad in the presence of a higher quality competing ad appearing above because of satiation (Jeziorski and Segal 2015)</td><td>Learning effectHigher quality competing ad enables the consumer to update her expectation about the quality of the focal ad (Athey and Ellison 2011). In other words, if the quality of a competing ad appearing above is higher, it is likely to increase a consumer&#x27;s expectation about the quality of the focal ad.Position effectConsumers visiting lower positions search more and may be more involved (Schmidt and Spreng 1996). Therefore, we expect more attention to information (Celsi and Olson 1988) and better information processing (MacInnis and Jaworski 1989). This leads to a higher learning effect (Hogarth and Einhorn 1992). In other words, at lower positions consumers are more likely to update their expectations of the focal ad based on the quality of the competing ad.</td></tr><tr><td>Keyword effectConsumers using specific keywords are closer to the purchase decision (Ramlall et al. 2011) and are likely to be more involved (Jerath et al. 2014). Higher involvement leads to better information processing and learning because of more attention to information (Celsi and Olson 1988). As before, consumers are more likely to update their expectation of the focal ad.</td></tr></table>

As the negative and positive externality effect of competing ads can vary across customers, we can only infer the dominant effect across all customers by evaluating the net effect of competing ads on the click performance of the focal ad.

Role of Ad Position. Ad position of the focal ad can also reveal the extent of learning and the impact of competing ads. The extent of search depends on the level of involvement (Schmidt and Spreng 1996). Consumers visiting ads in lower positions, after visiting the ads in higher positions, search more and are likely to be more involved.<sup>6</sup> Thus, consumers with a different extent of search could be heterogeneous in terms of their involvement and subsequent learning. In that case, it is possible that the net impact of learning and negative externality for consumers will vary with ad position. Therefore, we expect the impact of competing ads may also change with the position of the focal ad.

Role of Keyword. Consumers closer to the purchase decision are likely to use longer keywords (Ramlall et al. 2011). As specific words tend to be long, the users of specific keywords may be closer to the purchase decision as compared to users using generic keywords. Additionally, customers closer to the purchase decision are likely to be more involved (Jerath et al. 2014) and demonstrate a higher learning effect as explained earlier. Thus, the users of specific keywords may differ in their learning behavior from the users using generic keywords. This can also have an impact on the consumer response to competing ads at different positions. Table 1 summarizes the potential externality effect of competing ads on the click performance based on the factors discussed above.

Based on the above discussion, it appears that the effect of competing ads on the click performance of an ad would depend not only on the quality of the competing ad but also on the position of the focal ad and the specificity of the keyword used. Therefore, our research attempts to answer the following questions:

(a) How does the click performance of a focal ad change with a higher or lower quality competing ad appearing above? In particular, would the adverse impact of a higher (lower) quality competing ad attenuate or increase at a lower position?

(b) Would the impact of a competing ad on click performance differ depending on whether the keyword is generic or specific? How does the impact of a competing ad for a specific keyword type, generic or specific, change with the position of the focal ad?

## 4. Data Description

Our data set is provided by Yahoo<sup>7</sup> as part of the Yahoo! Research Alliance Webscope program and consists of bids, impressions, and clicks for different positions over 123 days from January 2008 to April 2008 for a large number of keywords and the corresponding advertisers. During the time period of our data panel, Yahoo’s sponsored search design was similar to that of Google in terms of the auction mechanism, ranking rules, and search results.<sup>8</sup>

Each keyword (or a key phrase) in our data set includes one of the following base keywords: “coin,” “laptop,” “cable,” “cruise,” and “car insurance.” These base keywords represent consumer search for different products and services to get information and/or make a purchase. Each keyword in our data includes one or more additional words besides the base keyword. The use of one or more qualifying words with a base keyword, narrows the set of associated products and makes the ad competition more relevant. For example, consumers looking for “business laptop” would see ads showing similar product offerings as compared to consumers searching using the base keyword laptop who may see a much broader set of offerings that cannot be compared meaningfully rendering competition less relevant.

This also enables us to create a data set with a large number of keywords derived from the five base keywords. The keywords in our data set are of five different specificity values and are not branded. We determine the specificity of each keyword based on the data as explained later in the section. In selecting the keywords we adopt the following approach. We only consider those keywords that have data for the entire 123 day period to ensure that keywords are not dropped or are added in the middle of the panel period. We rank keywords in terms of their search volume and click performance for each base-keyword category and specificity combination. We identify 500 such top keywords that are spread equally across all five base-keyword categories and specificity values. This allows us to focus on the typical consumer behavior as these popular keywords would be most commonly used by consumers.

We consider only the last 93 days for our analysis, as some keywords may have just been introduced at the beginning of the panel period for the data set and may not be stable from an auction perspective. We focus on the top seven positions to restrict our analysis to the first page of search results.<sup>9</sup> We also exclude the first position, as there are no competing ads appearing above the top position. We rank advertisers in terms of their quality as explained later.

Our final sample consists of 360 keywords with 1,267 advertiser keyword combinations. Summary statistics for our main sample are shown in Table 2. Next we describe how we determine different quality measures as well as keyword specificity.

## 4.1. Ad Quality

In our context, ad quality represents the click potential of an advertisement for a specific keyword. When a consumer begins a search using a particular keyword, she is more likely to click on an ad with a higher quality. This probability of clicking is based on the value that consumers expect to get from visiting the related website for the product or service associated with the keyword. It is well known that consumers care about product or service quality, vendor reputation, and customer service. Consumers form an expectation about ad quality and decide which website to visit based on the information content in the ad about the product, vendor, brand, etc. For instance, brand serves as a signal of product quality (Jacoby et al. 1971, Wernerfelt 1988, Rao and Monroe 1989, Erdem and Swait 2004). This is especially true in the online setup (Danaher et al. 2003) and consumers are known to have a brand preference in clicking on search engine results (Leong et al. 2012). Furthermore, consumers are likely to associate products with brands only if these are similar to the main product or service offered by the brand (Park et al. 1991). In that case, consumers may have a lower click propensity for an advertiser if the offered product or service is very different from its main product or service. As Amazon.com is an established brand for books and electronics but not for clothes, consumer expectations of Amazon to meet their needs will be high for keywords related to books and electronics but will likely be low for keywords related to clothes.<sup>10</sup> Similarly, consumer expectations for hp.com to meet their needs for a laptop would be higher as compared to their expectation for hp.com to meet their needs for a laptop bag. Thus, keyword specific expected click performance can represent a more refined consumer expectation of quality of the ad site for the associated product or service as compared to aggregate measures such as Alexa rank (Animesh et al. 2010). Note that there can be heterogeneity in the consumer expectation of ad quality depending on their decision process, preferences, and knowledge as explained in our consumer search model. As such, the click propensity or quality of an ad represents the average click propensity across consumers.

Table 2 Summary Statistics

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Impressions</td><td>Impressions for an advertiser keyword pair for a particular position and time</td><td>46.0931</td><td>293</td><td>1</td><td>59,580</td></tr><tr><td>Clicks</td><td>Clicks for an advertiser keyword pair for a particular position and time</td><td>1.28</td><td>9.75</td><td>0</td><td>711</td></tr><tr><td>Position</td><td>Position of advertiser for a keyword at a particular time</td><td>4.33</td><td>1.67</td><td>2</td><td>7</td></tr><tr><td>QualityRank</td><td>Quality Rank of an advertiser for a keyword at a particular time</td><td>3.10</td><td>0.61</td><td>1</td><td>5.16</td></tr><tr><td>QualityRankAbove</td><td>Quality Rank of competing ads appearing one position above</td><td>3.07</td><td>0.59</td><td>1</td><td>4.71</td></tr><tr><td>QualityRankBelow</td><td>Quality Rank of competing ads appearing one position below</td><td>3.09</td><td>0.62</td><td>1</td><td>4.69</td></tr><tr><td> $(QualityRankAbove)_{pos}$ </td><td>Position Weighted Quality Rank of competing ads appearing above</td><td>2.95</td><td>0.54</td><td>1</td><td>4.64</td></tr><tr><td> $(QualityRankBelow)_{pos}$ </td><td>Position Weighted Quality Rank of competing ads appearing below</td><td>3.08</td><td>0.64</td><td>1</td><td>4.64</td></tr><tr><td> $(QualityRank)_{Alt}$ </td><td>Quality Rank based on fixed effect coefficients</td><td>0.46</td><td>0.26</td><td>0</td><td>1</td></tr><tr><td> $(QualityRankAbove)_{Alt}$ </td><td>Quality Rank of competing ad appearing above based on fixed effect coefficients</td><td>0.46</td><td>0.26</td><td>0</td><td>1</td></tr><tr><td> $(QualityRankBelow)_{Alt}$ </td><td>Quality Rank of competing ad appearing below based on fixed effect coefficients</td><td>0.43</td><td>0.27</td><td>0</td><td>1</td></tr><tr><td> $(Quality)_{GSP}$ </td><td>Quality based on GSP auction equilibrium</td><td>1.68</td><td>0.32</td><td>1</td><td>2.99</td></tr><tr><td> $(QualityAbove)_{GSP}$ </td><td>Quality of competing ad appearing above based on GSP auction equilibrium</td><td>1.66</td><td>0.3</td><td>1</td><td>2.98</td></tr><tr><td> $(QualityBelow)_{GSP}$ </td><td>Quality of competing ad appearing below based on GSP auction equilibrium</td><td>1.6</td><td>0.28</td><td>1</td><td>3.02</td></tr><tr><td> $(QualityRank)_{CTR}$ </td><td>Quality Rank based on overall CTR</td><td>35.74</td><td>2.36</td><td>1</td><td>36.68</td></tr><tr><td> $(QualityRankAbove)_{CTR}$ </td><td>Quality Rank of competing ads appearing one position above based on overall CTR</td><td>25.33</td><td>2.09</td><td>1</td><td>26.29</td></tr><tr><td> $(QualityRankBelow)_{CTR}$ </td><td>Quality Rank of competing ads appearing one position below based on overall CTR</td><td>24.77</td><td>1.92</td><td>1</td><td>25.73</td></tr><tr><td>Log(Bid)</td><td>Bids in 1/10th of a cent</td><td>6.18</td><td>0.79</td><td>4.87</td><td>7.47</td></tr><tr><td>Log(OtherBid)</td><td>Bids of other nonrelated keywords</td><td>1.94</td><td>0.73</td><td>0</td><td>4.11</td></tr><tr><td>Log(OtherQualityRank)</td><td>Quality Ranks of other nonrelated keywords</td><td>6.41</td><td>1.04</td><td>0</td><td>7.97</td></tr><tr><td>Time</td><td>Day</td><td>77.83</td><td>26.36</td><td>31</td><td>123</td></tr></table>

$$
\text { QualityRankAbove } _ {k a t} = \frac {\sum \text { Impressions } _ {k b t} \times \text { QualityRank } _ {k b t}}{\sum \text { Impressions } _ {k b t}} \quad \text { where   } b \neq a \text {   and   } \text { Pos } _ {k b t} = \text { Pos } _ {k a t} - 1,
$$

$$
\text { QualityRankBelow } _ {k a t} = \frac {\sum \text { Impressions } _ {k b t} \times \text { QualityRank } _ {k b t}}{\sum \text { Impressions } _ {k b t}} \quad \text { where   } b \neq a \text {   and   } \text { Pos } _ {k b t} = \text { Pos } _ {k a t} + 1,
$$

$$
\text { QualityRankAbove } _ {\text { katpos }} = \frac {\sum \text { Impressions } _ {\text { kbt }} \times \text { QualityRank } _ {\text { kbt }} \times \log (| P o s _ {\text { kbt }} - P o s _ {\text { kat }} |)}{\sum \text { Impressions } _ {\text { kbt }}} \quad \text { where   } b \neq a \text {   and   } P o s _ {\text { kbt }} <   P o s _ {\text { kat }},
$$

$$
\text { QualityRankBelow } _ {k a t p o s} = \frac {\sum \text { Impressions } _ {k b t} \times \text { QualityRank } _ {k b t} \times \text { Log } (| P o s _ {k b t} - P o s _ {k a t} |)}{\sum \text { Impressions } _ {k b t}} \quad \text { where   } b \neq a \text {   and   } P o s _ {k b t} > P o s _ {k a t}.
$$

A search engine captures the click potential or quality of an ad for a keyword using a quality score measure. Search engines use several inputs to determine this quality score including the lagged click performance. However, while doing that they correct for the past position of the ad so that advertisers are not gaming the auction mechanism.<sup>11</sup> Finally, search engines ensure that the actual advertiser site is indeed relevant for the ad by incorporating the landing page quality in the quality score measure. This ensures that, on average, there is no mismatch between the ad and the actual site. Therefore, the quality score measure serves as a good proxy for ad quality in our context.

The actual quality score measure is not available to $\mathrm { { u s . } } ^ { 1 2 }$ As search engines rank ads for every keyword using their quality score for the keyword and bids (Athey and Nekipelov 2012, Liu et al. 2010, Athey and Ellison 2011), we infer this quality from the available ad positions and bids for every keyword. Thus, the position $P o s _ { k a t }$ of an advertiser’s ad a for keyword k at time t can be represented as a function of its $B i d _ { k a t }$ and quality $Q S _ { k a t }$ as follows:

$$
\begin{array}{c} P o s _ {k a t} \propto \alpha_ {k} B i d _ {k a t} ^ {\theta_ {k}} Q S _ {k a t} ^ {\gamma_ {k}}, \quad \text {or} \\ \ln (P o s _ {k a t}) \propto \ln (\alpha_ {k}) + \theta_ {k} \ln (B i d _ {k a t}) + \gamma_ {k} \ln (Q S _ {k a t}). \end{array}
$$

where $\alpha _ { k } , ~ \theta _ { k } ,$ and $\gamma _ { k }$ are keyword specific weights assigned by the search engine.

We can set the quality of a reference ad for a keyword as $Q S _ { k a _ { 0 } }$ and express the quality of other ads as a function of this baseline quality as $\lambda _ { k a t } Q S _ { k a _ { 0 } }$ . In that case, we have

$$
\begin{array}{c} \ln (P o s _ {k a t}) \propto \ln (\alpha_ {k}) + \gamma_ {k} \ln (Q S _ {k a _ {0}}) + \theta_ {k} \ln (B i d _ {k a t}) \\ + \gamma_ {k} \ln (\lambda_ {k a t}), \quad \text {or} \\ \ln (P o s _ {k a t}) = \mu_ {0} ^ {k} + \mu_ {1} ^ {k} \ln (B i d _ {k a t}) + \mu_ {a t} ^ {k} \delta_ {k a} + \varepsilon_ {k a t}, \end{array}
$$

(1)

where $\delta _ { k a }$ is the ad specific dummy for the keyword and $\mu _ { a t } ^ { k }$ is the corresponding coefficient for the keyword k at time t. Note that $\textstyle { \mu _ { a t } ^ { k } }$ is time varying and allows for the possibility that the ad quality may change over time. These changes may reflect ad and specific Web page improvements that may draw more users to the advertiser site for a particular keyword.

We estimate the above equation individually for each of our sample keywords using the position data for all advertisers associated with these sample keywords. For an ad $^ { a , }$ if $\mu _ { a t } ^ { k }$ is negative and significant then the search engine is placing the ad higher than the reference ad after controlling for the effect of the bid. We use the estimates of the ad dummy coefficients for each keyword to determine the relative quality rank of each ad. If the dummy coefficient is not significant for an ad then we assign it the same quality rank as the reference ad. We rank other ads above (below) the reference ad if $\mu _ { a t } ^ { k }$ is negative (positive) and significant. Using the above approach, we estimate quality ranks for ads for each keyword on a daily basis using the position data for the advertisers of the keyword for the past two weeks.<sup>13</sup>

Note that we can observe different positions for every advertiser keyword combination across several time periods. Additionally, we can also observe different positions for the advertiser keyword combination within a time period. The variation in position is due to changes in bids. Even if one advertiser changes its bid for its ad, it can influence the positions of ads for all other advertisers resulting in rich variation in position across advertisers for each of our sample keywords. As a result, we can identify the ad quality for every advertiser keyword combination as a fixed effect parameter on a rolling basis. Also note that the ranking equation captures the essence of the ranking mechanism that is known publicly and does not represent the exact equation used by the search engine. As a result, we can only infer the relative quality ranking of ads and not the true value of the internal quality score. One limitation of this approach is that we do not capture the actual magnitude of the ad quality. As a robustness check, we also evaluate a model where we use the actual values of the coefficient $\mu _ { a t } ^ { k }$ as a measure of quality.

It is possible that an advertiser may change the quality of its ad for a keyword in conjunction with other promotional activities for the related products that are not observable to us or the search engine. The search engine ranking may inadvertently capture the effect of these promotions resulting in a biased ranking of ads. As we estimate the quality ranking for each ad for a keyword as a fixed effect on a rolling basis, the estimate itself is not likely to be biased. However, the value may be adjusted depending on the effect of promotions and is likely to be correlated with the promotions. For example, if there are two competing ads, A and B, our analysis would calculate ranks for both ads in both periods. If advertiser A runs a promotion in certain time periods, the corresponding estimated rank would be higher and would be correlated with promotions. We also correct for this potential endogeneity bias using a suitable instrument for the quality rank as explained in Section 5.2.

Also note that the above approach is just using the search engine’s ranking policy to estimate the quality scores based on submitted bids. However, advertiser bids may be influenced by other advertiser bids. As a robustness test, we also estimate the quality score by considering the generalized second-price (GSP) auction equilibrium, which allows us to account for the possibility of advertiser bidding decisions based on competing bids, and validate our results. However, note that GSP auction equilibrium relies on the assumption that advertisers know the score-weighted bids of their competitors (Athey and Nekipelov 2012). Additionally, in our robustness analysis, we use an alternate measure of quality that is based on the overall CTR performance of the advertiser for the keyword after controlling for the position effect. This is similar to the approach adopted by Jeziorski and Segal (2015).

## 4.2. Ad Quality of Competing Advertisers

To account for the externality imposed by competing ads appearing above the focal ad we compute an externality measure, QualityRankAbove. Externality may also be imposed by ads appearing below the focal ad. To account for this, we compute a related externality measure QualityRankBelow. We know the different positions in which an advertiser’s ad has appeared for each keyword every day as well as the positions of all other competing ads for that keyword on a daily basis. We use this relative appearance of ads in different positions on a daily basis and their quality rank to determine the quality measure for the competing ads. For each advertiser for a keyword on a given day, QualityRankAbove is the average quality rank of all competing ads that have appeared one position above that advertiser’s ad for that keyword on that day. Note that a higher numerical value would indicate a lower average quality. As impressions vary across ads in a given position, we also weigh the quality rank with impressions received by the ad (see Table 2 for the definition). Similarly, QualityRankBelow for an ad is the weighted average quality rank of all ads that have appeared one position below the focal ad on a given day. In our robustness analysis, we use weighted average of quality ranks of all competing ads appearing above or below the focal ad to calculate the quality of competing ads. While doing so, we also weigh each competing ad’s quality rank by its position distance from the focal ad. We validate our results with this alternate externality measure.

Figure 2 Keyword Hierarchy  
![](/api/attachments/YQESEA6A/fulltext/images/e8e51de3582ae9b4ec66ada652d73b52f27b189a329f6ba036c79e526f14c2fa.jpg)

## 4.3. Keyword Specificity

Actual keywords are not available to us.<sup>14</sup> Instead, each word is represented by a unique ID. For example, if the words “laptop,” “personal,” and “business” have been assigned IDs 1, 2, and 3, respectively, then the keywords laptop, business laptop, and personal laptop would be represented as “1,” “12,” and “13” in our data set. To determine keyword specificity we determine parent child linkages between the keywords using matching words. For example, Figure 2 shows the parent child linkages for keywords using the base-keyword laptop. We can determine this easily in our setup because of the number of IDs assigned to each word in a keyword. Using this approach, we generate a hierarchy and determine the number of keywords above each keyword. We call this number the specificity of the keyword (Figure 2). A similar measure of specificity has been used by Agarwal et al. (2011). Note that an alternate measure of keyword specificity is the number of keywords (Ghose and Yang 2009, Yang and Ghose 2010). For most of our keywords, the length of the key phrase is equivalent to the specificity level. Previous studies (Ghose and Yang 2009, Yang and Ghose 2010) have also considered other keyword attributes such as the advertiser brand. In our study, we are interested in user preference for different quality ads for nonbranded keywords as a function of their ad position. So we do not consider branded keywords in our sample.

## 5. Model

We are interested in modeling the click performance of ads for different keywords and how this performance varies as a function of quality of the competing ads. We do not have detailed clickstream data to represent the exact clicking behavior of consumers. Instead, we have the daily aggregate data such as bid, number of impressions, and clicks for each position for each advertiser keyword combination. Prior single advertiser studies in sponsored search (Ghose and Yang 2009, Yang and Ghose 2010, Rutz and Bucklin 2011, Rutz and Trusov 2011, Agarwal et al. 2011) use aggregate data to model the click performance. We extend this framework to account for multiple advertisers in our setup.

Our unit of analysis is a keyword advertiser pair because the search engine auction is keyword specific and advertisers can vary in their performance for their ads for a keyword. Keyword characteristics are an indication of the underlying search behavior, which varies across consumers. For example, the keyword business laptop is less specific and indicates an initial stage of information search, while a more specific keyword like “ultralight business laptop” indicates a more advanced and directed stage of information search. To account for these differences across keywords, we capture how specific a keyword is using the measure of keyword specificity. Besides specificity, there can be additional variables that capture keyword characteristics. For example, the presence of “retailer” or “brand” information captures preference for the retailer or brand. However, in our data set none of the keywords carry brand or retailer information.<sup>15</sup> Another variable that has been used in the past is the “size” of the keyword that indicates the number of words in the keyword. This can capture additional aspects of consumer preference. However, this information is already captured in our “specificity” variable.

We use a hierarchical model to capture the effect of keyword characteristics. This provides a flexible random component specification, allowing us to incorporate observable and unobservable heterogeneity for keywords. Hierarchical models are commonly used to draw inferences on individual level characteristics (Rossi and Allenby 2003). Hierarchical Bayesian (HB) models have also been used to study sponsored search data with the keyword as a unit of analysis (Ghose and Yang 2009, Yang and Ghose 2010, Rutz and Trusov 2011, Agarwal et al. 2011). In our robustness analysis, we also verify our results with a fixed effects approach to account for unobservable keyword heterogeneity. This allows us to account for potential correlation across keywords.

Consumers could be selecting more than one ad. To represent this scenario, we assume that the consumer decision of clicking each ad for a particular keyword is a binary choice. We assume an independent and identically distributed (i.i.d.) extreme value distribution of the error term for individual choices and use a logit model to represent the click probability of ad a for a keyword k at time t. This probability can be represented as

$$
\begin{array}{c} \Lambda_ {k a t} = \frac {\exp (U _ {k a t})}{1 + \exp (U _ {k a t})}, \\ \text { where } U _ {k a t} \text { is   the   latent   utility   of   clicking. } \end{array}
$$

Click decision is influenced by the ad quality as well as the position of the ad. We represent the ad quality using the quality rank measure described earlier. We capture the effect of position using position dummies. These would represent the search costs associated with different positions and position specific priors about the ad quality. We account for the externality effect of competing ads by considering the impact of quality rank of ads that would have appeared above and below the focal ad for a keyword. Finally, we also consider the interaction of the externality with position to capture any position specific effect of externality. As mentioned earlier, we use a hierarchical model to account for the effect of keyword characteristics. For a keyword k at time t, the latent utility of clicking ad a can be expressed as

$$
\begin{array}{r l} & U _ {k a t} = \beta_ {0} ^ {k} + \beta_ {1} ^ {k} \log (Q u a l i t y R a n k _ {k a t}) \\ & \qquad + \beta_ {2} ^ {k} \log (Q u a l i t y R a n k A b o v e _ {k a t}) \\ & \qquad + \beta_ {3} ^ {k} (\log (Q u a l i t y R a n k A b o v e _ {k a t}) \times \log (P o s _ {k a t})) \\ & \qquad + \beta_ {4} ^ {k} \log (Q u a l i t y R a n k B e l o w _ {k a t}) + \beta_ {5} ^ {k} T i m e _ {k t} \\ & \qquad + \sum_ {p o s} \beta_ {p o s} ^ {k} \delta_ {p o s} + \sum_ {a} \beta_ {\mathrm{a}} ^ {k} \delta_ {a} + \varepsilon_ {k a t} ^ {\beta}, \end{array}\tag{2}
$$

$$
\begin{array}{r l} & {\pmb {\beta} ^ {k} = \Delta^ {\beta} \omega_ {k} + u _ {k} ^ {\beta} \quad u _ {k} ^ {\beta} \sim N (0, V ^ {\beta}),} \\ & {\pmb {\beta} ^ {k} = [ \beta_ {0} ^ {k}, \beta_ {1} ^ {k}, \beta_ {2} ^ {k}, \beta_ {3} ^ {k}, \beta_ {4} ^ {k}, \beta_ {5} ^ {k}, \pmb {\beta} _ {p o s} ^ {k}, \pmb {\beta} _ {a} ^ {k} ],} \end{array}
$$

where $Q u a l i t y R a n k _ { k a t }$ is the quality rank of the advertiser’s ad a for the keyword; QualityRankAbove is the weighted average quality rank of competing ads appearing above ad $a ;$ QualityRankBelow is the weighted average quality rank of the competing ads appearing below ad $\dot { a ; } \log ( Q u a l i t y R a n k A b o \bar { v } e _ { k a t } ) \stackrel { - } { \times }$ $\log ( \bar { P o s } _ { k a t } )$ represents the interaction term; $\mathrm { T i m e } _ { k t }$ captures the effect of any time varying dynamics; $\delta _ { p o s }$ is the position specific dummy; $\delta _ { a }$ is the advertiser specific dummy; $\omega _ { k }$ represents keyword specificity and a constant; $\Delta ^ { \ddot { \beta } }$ is a matrix capturing the relationship between the keyword characteristics and the keyword-advertiser coefficients; $u _ { k } ^ { \beta }$ represents the unobservable heterogeneity for the random coefficients, which we assume is normally distributed with a mean 0 and covariance matrix ${ \check { V } } ^ { \beta } ;$ and $\varepsilon _ { k a t } ^ { \beta }$ represents the time varying unobserved attributes for the keyword advertiser combination that are common for all consumers.

Note that the random coefficient specification allows us to capture unobservable effects at the keyword level. The advertiser dummy captures the effect of time invariant unobservables associated with advertisers of a keyword. We also assume that the error terms are independent across positions for a keyword in a given time period. This is a common assumption in empirical research modeling search behavior across multiple listings (Kim et al. 2010, Yang et al. 2014). Furthermore, any correlation between positions is captured by the position dummies as well as the competition.<sup>16</sup> In our robustness analysis, we validate our results with a linear model specification where we also correct for any possible correlation between the error terms for every keyword.

Jeziorski and Segal (2015) use clickstream data to represent consumer behavior and use a substitution parameter to capture the effect of competing ads. As we do not have the clickstream data, we cannot use the same modeling approach. However, in our model any substitution or complementary effect between ads can be captured using the QualityRankAbove and QualityRankBelow variables. Note that it is possible to have two different externality effects: a negative effect due to substitution and a positive effect due to learning as pointed out by Jeziorski and Segal (2015). However, similar to their study, we can only capture the net externality effect of competing ads and cannot separately identify the positive and negative effects.

## 5.1. Endogeneous Ad Position

The ad position is determined by the search engine based on bids submitted by advertisers and their quality. Advertisers may coordinate their bids with promotions. As a result, the position of an ad could be correlated with promotions that are observed by consumers but not by us. We also do not observe regular search results. Yang and Ghose (2010) show complementarity between the click performance of regular search results and organic search results. Any changes in the regular search results would influence the clicks for advertisers. Thus, the position of an ad can be correlated with regular search results. As these variables are not known to us and are included in the error term, it leads to a biased estimate of the position effect.

To correct for the resulting endogeneity bias we use an instrumental variable approach. We model the advertiser bid decision and the search engine ranking decisions that determine the advertiser’s ad positions. Similar approaches have been used by Ghose and Yang (2009), Yang and Ghose (2010), and Agarwal et al. (2011) to account for the endogeneity of position. We define the equation for bid as follows:

$$
\log (B i d _ {k a t}) = \gamma_ {0} ^ {k} + \gamma_ {1} ^ {k} Z _ {k a t} ^ {\gamma} + \sum_ {a} \gamma_ {a} ^ {k} \delta_ {k a} + \varepsilon_ {k a t} ^ {\gamma},\tag{3}
$$

where $Z _ { k a t } ^ { \gamma }$ is the instrumental variable explained below and $\delta _ { k a }$ is the advertiser specific dummy for the keyword to capture the advertiser specific effect. The functional form ensures that bid is nonzero.

We know how keywords are related to each other in a hierarchical fashion (parent child relationship). In that case, for every advertiser keyword pair in our sample, we can determine other keywords that are not related to the same parents with specificity one but are still part of the advertiser’s keyword portfolio. It is very likely that different consumers are using the focal keyword and these other keywords and are likely to have uncorrelated valuations. For example, in Figure 2 we can expect different users to be focusing on “ultralight business laptop” and “cheap personal laptop.” Additionally, for every keyword with specificity one, we consider keywords under other keywords with specificity one as nonrelated keywords. For example, in Figure 2 we can expect different consumers to be focusing on keywords personal laptop and business laptop bag. In that case, if the advertiser is running promotions for these nonrelated keywords, the demand side correlation in valuation can be ruled out to a large extent. In the above example, promotions for products associated with keyword ultralight business laptop are unlikely to influence users’ search for cheap personal laptop. Similarly, promotions for products associated with keyword personal laptop are unlikely to influence searches associated with business laptop bag. Thus, bids for nonrelated keywords are not likely to be correlated with the performance of focal keywords because of consumer valuations. However, as these keywords are part of the advertiser’s portfolio and budget, we can expect cost correlation across bids. In that case, the bids of an advertiser’s ad for nonrelated keywords can be used as an instrument for the bid for the ad for focal keyword.

Note that the consumer valuation can also be correlated if the firm has the same promotions across multiple products. However, this is more likely to be the case for related products. By selecting bids of nonrelated keywords, we minimize the impact of such correlation. This is similar to the approach adopted by Hausman (1996) and Nevo (2001) and more recently Ghose et al. (2012) to use prices of the product in other markets as an instrument for the price of product in the focal market. We also validate the strength and the exogeneity of our instrument as explained later.

A search engine ranks each ad for a keyword based on the related bid as well as the ad quality for that keyword. We represent this as

$$
\begin{array}{r l} & {\log (P o s _ {k a t}) = \alpha_ {0} ^ {k} + \alpha_ {1} ^ {k} \log (B i d _ {k a t})} \\ & {\qquad + \alpha_ {2} ^ {k} \log (Q u a l i t y R a n k _ {k a t})} \\ & {\qquad + \sum_ {a} \alpha_ {a} ^ {k} \delta_ {k a} + \varepsilon_ {k a t} ^ {\alpha}.} \end{array}\tag{4}
$$

Note that this equation is similar to Equation (1), which is used to determine the quality rank. A key difference is that we have replaced the time varying advertiser specific coefficient with the time varying ad quality rank and we account for nonvarying unobserved advertiser attributes using keyword specific advertiser dummy.

## 5.2. Endogeneity of Quality Rank

As advertisers update their ads and websites to improve quality, they may do so along with promotions that are unobservable to us but are observed by consumers. As the search engine ranking is algorithmic it may capture the effect of these promotions while determining the ad quality rank. In that case, the quality rank estimates can be correlated with the error terms. We use the instrumental variable approach to correct for the resulting endogeneity bias. We use the following equation to estimate the ad quality rank based on the instrument:

$$
\log (Q u a l i t y R a n k _ {k a t}) = \theta_ {0} ^ {k} + \theta_ {1} ^ {k} Z _ {k a t} ^ {\theta} + \sum_ {a} \theta_ {a} ^ {k} \delta_ {k a} + \varepsilon_ {k a t} ^ {\theta},\tag{5}
$$

where $Z _ { k a t } ^ { \theta }$ is the instrumental variable explained below and $\delta _ { k a }$ is the advertiser specific dummy for the keyword to capture the advertiser specific effect.

For every keyword advertiser combination in our sample, we consider other nonrelated keywords for that advertiser in the data set and determine the daily average QualityRank of the advertiser’s ads across those keywords. We determine the nonrelated keywords using the same procedure as described earlier. We use the log value of this average daily quality rank of the advertiser’s ads for other nonrelated keywords as an instrument for the quality rank of its ad for the focal keyword. Quality ranks of an advertiser’s ads for different keywords are likely to be correlated from the cost perspective as advertisers coordinate their spending across keywords and can combine their effort to improve their website design for different products. As we account for the advertiser specific effect for each keyword, the consumer valuation for the keyword advertiser pair under consideration is less likely to be correlated with the average consumer valuation. This is similar to the approach adopted by Hausman (1996) and Nevo (2001) to use prices of the product in other markets as an instrument for the price of the product in the focal market. We also validate the strength and the exogeneity of our instrument as explained later.

As the quality measures for competing ads, Quality-RankAbove and QualityRankBelow, are derived using the quality rank of ads, it is possible that these measures will be correlated with unobservables if the quality rank of ads are endogenous. To mitigate the potential endogeneity bias, we construct QualityRank-Above and QualityRankBelow measures based on the quality rank of each ad estimated using the instruments as specified in Equation (5).

## 5.3. Identification and Estimation

The above set of simultaneous equations represents a triangular system and has been addressed by authors in classical econometrics (Lahiri and Schmidt 1978, Hausman 1975, Greene 1999) and Bayesian econometrics (Zellner 1962). Identification comes from the fact that bid and quality are completely determined by the exogenous instruments. For every advertiser keyword combination, our data set provides nonrelated keywords that are part of the advertiser portfolio. Using bids and quality rank of advertiser’s ads for these nonrelated keywords in every time period, we can determine the bid and quality of the advertiser’s ad for the focal keyword in each time period.

Using estimated bid and quality rank for each keyword advertiser combination we can determine the position for the combination in every period. Similarly, using estimated quality rank for each keyword advertiser combination, we can determine the competing measures for the combination in every period. Ad quality, externality measures, and position in turn influence click performance. Furthermore, the relative positions of competing ads change across time periods for every keyword advertiser combination. As a result, we can identify the effect of externality measures on the click performance.

Hausman (1975) and Lahiri and Schmidt (1978) have shown that the parameter estimates for a triangular system can be fully identified using generalized least squares. Zellner (1962) has addressed triangular systems from a Bayesian point of view. Triangular systems have been estimated using the classical approach (Elberse and Eliashberg 2003, Godes and Mayzlin 2004) and more recently in sponsored search using the Bayesian approach (Ghose and Yang 2009, Yang and Ghose 2010, Agarwal et al. 2011, Rutz and Trusov 2011, Rutz et al. 2012).

We use the two-stage least squares approach to correct for the endogeneity bias. We first estimate the bid and the quality equations for each keyword advertiser combination and use the estimated values for bid and quality in the position equation to estimate the parameters of the position equation for each keyword. We use these parameters to estimate the position values that we use in our main model for CTR along with the estimated quality measures. We performed an F -test in the first stage for our instruments. In each case, the F -test value was well over 10, suggesting our instruments are not weak. To explore the quality of our instruments further, we explored the orthogonality of the instruments by inspecting the plots of the marginal posterior distributions for $\begin{array} { r } { \sum _ { k a t } \pmb { \mathcal { E } } _ { k a t } ^ { \beta } } \end{array}$ as suggested by Duan and Mela (2009) and Musalem et al. (2008). We compute the 95% posterior predictive interval to assess whether it excludes zero as a test for rejecting orthogonality. For all our instruments we cannot reject orthogonality, suggesting that our instruments are indeed exogenous.

One possibility is that the quality changes and bid changes may be strongly correlated as both form components of cost for each advertiser. In that case, the model will be underidentified. However, the design changes are less frequent as compared to bid changes as the required effort is very different. Additionally, bid changes are likely to move in both directions while the quality changes are always likely to be in the same direction. Correlation between the instruments for bid and quality is 0.15, which suggests that these decisions are not highly correlated.

We estimate our main model using a Bayesian approach, applying Markov Chain Monte Carlo (MCMC) sampling because of the nonlinear characteristics of our model (Rossi and Allenby 2005). The priors and conditional posteriors of this model are discussed in the online appendix (available as supplemental material at http://dx.doi.org/10.1287/isre.2016.0637). For the HB models, we run the MCMC simulation for 80,000 draws, discarding the first 40,000 as burn-in. To ensure that our parameter estimates are accurate, we simulated the clicks, bids, quality, and positions using our estimates. By repeating the estimation with this simulated data set we were able to recover our parameter estimates. This indicates that our parameters are fully identified.

## 6. Results

## 6.1. Click-Through Rate (CTR)

Table 3 provides the mean values for the posterior distribution of the $\Delta ^ { \beta }$ matrix in Equation (2). The coefficient for the ad quality (QualityRank) is negative and significant. This confirms that low-quality (highquality rank magnitude) ads get a lower click performance as compared to the high-quality ads for a given position. As we derive the quality rank measure using the search engine ranking policy, this validates that the search engine ranks ads for a keyword based on their potential to generate clicks for that keyword.

The coefficient of QualityRankAbove is negative and significant. This suggests that the presence of higher quality competing ads (low value of QualityRank-Above) above will lead to higher click performance for the focal ad as compared to the presence of lower quality competing ads. Consumers are likely to evaluate these competing ads before they visit the focal ad as they sequentially evaluate the ads from top to bottom.<sup>17</sup> The order of evaluation is confirmed by the coefficients of the position dummies, which are increasingly negative (Table 3). Thus, a possible explanation for the observed effect of the competing ads is that consumers may be using the presence of highquality competing ads above to infer that the focal ad is also of high quality. High quality of competing ads makes consumers update their beliefs about the quality of the focal ad (Athey and Ellison 2011). Note that this does not rule out the satiation effect for some consumers, i.e., negative externality is imposed by the competing ad above because of information satiation. Our result only suggests that the learning effect is more dominant.

Table 3 Parameter Estimates for CTR

<table><tr><td></td><td>Intercept</td><td>Specificity</td></tr><tr><td>Constant</td><td>-1.06 (0.2)***</td><td>-0.04 (0.11)</td></tr><tr><td>QualityRank</td><td>-0.32 (0.12)***</td><td>-0.02 (0.1)</td></tr><tr><td>QualityRankAbove</td><td>-2.28 (0.32)***</td><td>-0.29 (0.15)*</td></tr><tr><td>QualityRankBelow</td><td>0.45 (0.2)**</td><td>0.39 (0.15)***</td></tr><tr><td>QualityRankAbove × Position</td><td>-0.53 (0.2)***</td><td>-0.35 (0.12)***</td></tr><tr><td>Pos3</td><td>-0.08 (0.07)</td><td>-0.1 (0.05)**</td></tr><tr><td>Pos4</td><td>-0.25 (0.08)***</td><td>-0.07 (0.05)</td></tr><tr><td>Pos5</td><td>-0.47 (0.08)***</td><td>-0.13 (0.05)***</td></tr><tr><td>Pos6</td><td>-0.35 (0.12)***</td><td>-0.25 (0.07)***</td></tr><tr><td>Pos7</td><td>-0.49 (0.14)***</td><td>-0.1 (0.14)</td></tr><tr><td>Time</td><td>-0.1 (0.16)</td><td>0.05 (0.13)</td></tr></table>

<sup>∗</sup>Statistically significant at 10%; <sup>∗∗</sup>statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

One possibility is that advertisers with low-quality ads bid very high and get high click performance as they show up in high positions. In that case, the measured ad quality and the quality of competition would be reversed and the observed effect would be the satiation effect and not the learning effect. However, we find that even after controlling for the ad position, consumers are more likely to click an ad with high quality. This suggests that our measure of quality does represent the consumer propensity to click and is not driven by the position of ads. In that case, the observed effect of competition is likely to be driven by the dominant learning effect.

The coefficient for the interaction term between QualityRankAbove and position is negative and significant. To further establish this interaction effect, we compute the CTR using the posterior distribution of the keyword advertiser parameter estimates from Equation (2). Figure 3 shows the effect of different quality of competing ads, which appear above the focal ad, on the CTR of the focal ad at high and low positions. Note that we have removed the direct effect of position on the click performance so that we can just compare the effect of competition. The negative effect of the high-quality competing ads appearing above decreases with position and the negative effect of the low-quality competing ads increases with position. A potential explanation is that the learning effect of consumers is stronger at lower positions as compared to higher positions, i.e., consumers are more likely to update their quality expectation of the focal ad at lower positions as compared to higher positions. Consumers with both high and low search intensity, visit the top positions while consumers with high search intensity are more likely to visit lower positions.<sup>18</sup> Consumers searching more are likely to be more involved (Celsi and Olson 1988). This high involvement may lead to high information processing due to high attention (MacInnis and Jaworski 1989) and in turn, lead to more learning (Hogarth and Einhorn 1992). As a consequence, learning can be more pronounced at the lower position resulting in lower negative impact of high-quality competition as compared to the impact of low-quality competition in low positions.

Figure 3 Impact of Competition on CTR as a Function of Position  
![](/api/attachments/YQESEA6A/fulltext/images/b0a600192a4b8fc59f8a3068b31440b2f16c69136150b4d6e70aaad41584b80c.jpg)

The coefficient for the interaction term between the QualityRankAbove position and specificity is negative and significant. This suggests that the externality effect is a function of both position and keyword specificity. Figures 4 and 5 show the effect of competing ad quality at high and low positions for generic and specific keywords, respectively. The difference in CTR in the presence of high-quality competing ads versus low-quality competing ads does not change much with position for generic keywords (Figure 4). This suggests that users using generic keywords do not differ much in terms of their learning even if they are visiting different positions. For specific keywords, the negative effect of high-quality competitor further decreases with position while the negative effect of low-quality competitor increases with position (Figure 5). This suggests that the learning effect is more prominent at lower positions for the users searching using specific keywords. As users of specific keywords are closer to the purchase decision, they are more involved (Jerath et al. 2014) and can better process the competing ad information. As a result, they may demonstrate a higher learning effect. However, our results show that among consumers using specific keywords, only consumers searching the lower positions demonstrate a higher learning effect. This can be attributed to the higher level of involvement of the consumers searching in lower positions.

Figure 4 Impact of Competition on CTR for Generic Keywords  
![](/api/attachments/YQESEA6A/fulltext/images/56613ce86658d09a5d3af55b1a356c61c31e169417641b44c7f2587134449acb.jpg)

The coefficient for QualityRankBelow is positive and significant. This suggests that a higher quality competing ad appearing below will have a more negative impact on the click performance as compared to a lower quality competing ad.<sup>19</sup> The effect of competition below can be coming from regular users who search from top to bottom and also from users searching following a different order. A consumer searching from top to bottom may see the next competing ad while considering the focal ad. A priori, her expectation of the ad quality appearing below is low. In that case, if the quality turns out to be high, it challenges her expectation and may make the consumer uncertain about clicking the focal ad resulting in a lower propensity to click the ad.

Figure 5 Impact of Competition on CTR for Specific Keywords  
![](/api/attachments/YQESEA6A/fulltext/images/c75267a96dd74e9a862e4f8ea0a6cb9ea630de9979a8c24eb933ecd62fc3b0f6.jpg)

Table 4 Parameter Estimates for Bid

<table><tr><td>Variables</td><td colspan="2">Coefficients</td></tr><tr><td>Const</td><td>6.834</td><td>(0.047)***</td></tr><tr><td>OtherBid</td><td>-0.016</td><td>(0.002)***</td></tr></table>

<sup>∗∗∗</sup>Statistically significant at 1%.

Furthermore, users not following a sequential top to bottom approach are not likely to learn anything about the quality of the focal ad by visiting the competition below. The reason they must be visiting the lower positions in the first place would be that they a priori do not expect ads to be arranged in a certain order in terms of quality or they are more certain about the expected quality of different advertisers. So if they encounter a high-quality competing ad below the focal ad then they are less likely to visit the focal ad.

## 6.2. Bid

Table 4 provides the mean values of the beta coefficients from Equation (3). The coefficient for the instrument “other bid,” i.e., average bid for unrelated keywords, is negative and significant. This confirms that the bids submitted by advertisers for different keywords are correlated. As we have selected nonrelated keywords, the source of this correlation is likely to be the common cost factors.

## 6.3. Position

Table 5 provides the mean values for the beta coefficients from Equation (4). The coefficient for quality rank is positive and significant. Thus, after controlling for bids, a low-quality ad (high-quality rank magnitude) is more likely to get a lower position (higher numerical value of the position). This suggests that the search engine evaluates these ads as low-quality ads. This confirms that the advertiser fixed effect is correlated with the internal quality measure used by the search engine. The coefficient for bid is negative and significant. This is reasonable as higher bids should lead to higher positions (lower value of the position).

Table 5 Parameter Estimates for Position

<table><tr><td>Variables</td><td colspan="2">Coefficients</td></tr><tr><td>Const</td><td>1.995</td><td>(0.219)***</td></tr><tr><td>Bid</td><td>-0.225</td><td>(0.038)***</td></tr><tr><td>QualityRank</td><td>0.869</td><td>(0.043)***</td></tr></table>

<sup>∗∗∗</sup>Statistically significant at 1%.

## 6.4. Quality Rank

Table 6 shows the mean coefficient estimates for Equation (5). The coefficient for the instrument based on the average quality rank of nonrelated keywords is positive and significant. This confirms that advertisers coordinate quality improvements of ads for their keywords.

## 6.5. Robustness Tests

We have taken several steps to evaluate the robustness of these results. We use harmonic mean (Newton and Raftery 1994) to calculate the log-marginal density. We report log-marginal densities in Table 7. It shows that our main model provides a better fit as compared to other models. Because of space constraints, detailed descriptions for the related models along with the estimates and other robustness analysis are given in Online Appendix B.

## 6.6. Comparison with Other Research

Our results differ from the observations made by Craswell et al. (2008) for regular search results. Their model a priori assumes that search results impose negative externality on each other. However, their model performs well only near the top listing and does not fit well for lower positions on the same page. Additionally, their results may not directly apply to sponsored search as consumers do not trust the sponsored results (Jansen and Resnick 2006) and may exhibit a different search behavior for ads. Our results may appear to contradict the observation made by Jeziorski and Segal (2015) in that high-quality competition leads to a higher negative effect for their set of keywords. However, our results are not directly comparable to Jeziorski and Segal (2015) as they focus on base keywords and do not consider specific keywords. In our analysis, we have considered keywords with base keywords and one or more qualifying words or modifiers (specificity: 1–5). This allows us to investigate the impact of differences in search behavior for keywords with varying specificity. Furthermore, choosing keywords with one or more qualifying keywords in our case allows us to do a more robust analysis as we can derive appropriate instruments for quality and position using the keyword hierarchy.

Table 6 Parameter Estimates for Quality Rank

<table><tr><td>Variables</td><td>Coefficients</td></tr><tr><td>Const</td><td>0.671 (0.041)***</td></tr><tr><td>OtherQualityRank</td><td>0.004 (0.0018)**</td></tr></table>

<sup>∗∗</sup>Statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

Table 7 Fit for Different Models

<table><tr><td>Models</td><td>Marginal density</td></tr><tr><td>Main model</td><td>-972,699</td></tr><tr><td>Model without interaction terms</td><td>-974,632</td></tr><tr><td>Model with interaction terms with both QualityRankAbove and QualityRankBelow</td><td>-981,681</td></tr><tr><td>Main model using quality based on fixed effects coefficient</td><td>-978,249</td></tr><tr><td>Main model using quality based on GSP auction equilibrium</td><td>-978,764</td></tr><tr><td>Main model using quality based on overall CTR</td><td>-977,627</td></tr></table>

We also conduct a supplemental analysis where we estimate our main model using data only for the base keywords. We estimate the quality of advertisers using a fixed effects approach similar to Jeziorski and Segal (2015). Results are included in Table C1 in the online appendix. The coefficient for QualityRankAbove is not significant. However, the coefficient for the interaction term between QualityRankAbove and position is negative and significant. This suggests that at a higher position, a high-quality competing ad has a higher negative effect on the click performance of the focal ad as compared to a low-quality competing ad. However, at a low position, a high-quality competing ad has a lower negative effect on the click performance as compared to a low-quality competing ad (Figure C1 in the online appendix). This would suggest that satiation is dominant for our base keywords at high positions but learning is dominant at lower positions. Note that this is similar to our main analysis where we find that the learning effect may be increasing at lower positions. For our base keywords, we find evidence of satiation at higher positions. This suggests that satiation plays a dominant role at higher positions when consumers begin their search using generic keywords. A potential explanation can be that consumers visiting the top positions using base keywords may be less involved while seeking information resulting in lower learning effects. As a result, satiation may dominate at the top positions for such keywords.

Our results show a difference in the decay of click performance of ads based on their ad quality. This appears similar to the result obtained by Animesh et al. (2011) who find that ads with quality USP (unique selling proposition) experience a higher decay in click performance as compared to ads with price USP. However, the underlying mechanism is different. In their setup, the outcome can be attributed to differences in the search behavior of consumers interested in quality versus price. Price sensitive consumers are likely to search more as compared to quality sensitive consumers leading to a lower decline in click performance for ads with price USP versus quality USP. In our setup, the result is driven by externality imposed by competing ads. Finally, our result for differences in click decay is due to a specific arrangement of ads in terms of their quality, i.e., only if there is a variation in the quality and ads are arranged either in increasing or decreasing order of quality.

Additionally, Animesh et al. (2011) also find that high intensity of competition leads to lower click performance in top positions for ads with quality as their unique selling proposition. However, they find a positive effect of competition in the lower positions. Additionally, they do not find this effect for ads with price as the USP. The differences in our results for the effect of competition can be attributed to the differences in the measure of competition quality. Their measure of competition based on matching USP may not adequately capture the possibility of users inferring the quality of the focal ads from their evaluation of the competing ads.

## 6.7. Alternate Ranking Mechanism and Search Engine Performance

Our results suggest that the high-quality competing ads appearing above impose lower negative externality on a focal ad as compared to the low-quality competing ads. Thus, we can expect that arranging ads in decreasing order of quality would lead to higher overall click performance. To quantify the impact, we place ads for each keyword in decreasing order of their estimated quality. We determine the externality for each ad based on this ordering. We estimate the click performance using the posterior distribution of the estimated parameters for our main model. We find that the ordering of ads based on their quality score results in a 69% increase in the click volume for our sample keywords.

We do not have the actual cost paid by the advertiser for the click. However, we can estimate the cost per click (CPC) based on the relative ordering of the advertisers for every keyword, their bids, and their estimated quality scores. As we do not have the actual relative ordering of the advertisers for every impression, we use impression weighted bids and positions to infer the actual ordering and estimate CPC accordingly. We also calculate the CPC for the new arrangement where the advertisers’ ads are listed in decreasing order of their quality score. We assume that bids of advertisers do not change with the new ordering. The new arrangement lowers the average CPC by 18% as some low-quality ads are not paying the premium cost for appearing in the top positions. However, this lowering in CPC is outweighed by the increase in clicks. Our analysis suggests that the search engine can improve its revenue for our sample by 39% by listing ads in decreasing order of their quality. Furthermore, the ads with lower click performance due to lower positions also experience lower costs with the new setup, which would reduce the negative impact of the lower click performance.

Search engines can implement this ordering by providing higher weightage to the quality score in the ranking mechanism. However, search engines can do so without changing the pricing mechanism so that advertisers still compete for the top positions by submitting bids according to their valuations.

## 7. Discussion and Conclusion

We evaluate the effect of the click potential or the quality of competing ads on the click performance of ads in sponsored search. We find that high-quality competing ads appearing above a focal ad have a lower negative effect on the click performance of the focal ad as compared to the negative effect of low-quality competing ads. We also find that this effect depends on the ad position and the type of keyword. In general, the high-quality competition has a lower negative effect at a low position of the focal ad as compared to the negative effect at a high position. Furthermore, the effect of competing high-quality advertisers remains unchanged with position for generic keywords but is much lower at low positions as compared to the high positions for specific keywords.

Our paper makes several contributions. Our results inform advertisers about the drivers for click performance for different positions. Yao and Mela (2011) show that advertisers providing higher quality to consumers prefer to bid high to attain top positions as consumers are more likely to visit top positions. We show that a high-quality ad for a keyword has higher incentive to be near the top not just because more people are likely to visit top positions but also because of the externality imposed by other ads. If high- and low-quality ads were to exchange high and low positions, high-quality ads are likely to experience a higher decay in click performance as compared to low quality ads.

Our results suggest that users are likely to show a higher learning effect at lower positions. Fewer consumers are expected to click a high-quality ad in lower positions because of externality. However, because of stronger learning effects, the ones who end up clicking the high-quality ad in lower positions will update their expectations after visiting the website if the ad is of high quality. Furthermore, there is a recency effect in this environment (Agarwal et al. 2011), i.e., consumers who visit an ad in different positions are more likely to buy from it when they visit it in the lower position as compared to the top position. In that case, a high-quality ad can get fewer clicks but more immediate conversions in the lower positions as compared to the top positions. As a result, high-quality advertisers with an objective to maximize return on investment, may be better off at a lower position.

Furthermore, advertisers can more appropriately choose keywords initially from the wide variety of keywords. A common industry approach is to focus on keywords where there are fewer competing ads.<sup>20</sup> However, our results suggest that learning effect plays a role in the click performance, and as a result, advertisers may be better off if they are preceded by highquality ads as compared to low-quality ads. This can be achieved by selecting keywords with high-quality competing ads. For example, advertisers can determine the organic ranks of competitors appearing in the search results for the keyword to determine their quality. If the focal advertiser appears lower than the competing advertisers, then the advertiser can expect consumers to have a higher expectation on the quality of the competing advertisers.

Additionally, our results show that a search engine should consider the externality imposed by competing ads in determining the rankings and the cost per click. Furthermore, the search engine should consider keyword characteristics while determining the weights to be allocated to the advertisers for the externality effect. Ignoring the externality effect leads to a loss in revenue for the search engine at least in the short run as the appearance of low-quality ads at the top reduces the total number of clicks. For example, our analysis suggests that the search engine can improve its revenue for our sample by 39% by listing ads in decreasing order of their quality. However, such a change in the ranking policy should also take into account the bidding and participation behavior of advertisers.

Our paper provides new insights into the consumer click behavior in sponsored search. While previous research in sponsored search (Animesh et al. 2011, Jeziorski and Segal 2015) points to the satiation effect, we show evidence of a learning behavior. Lower negative externality of competing high-quality ads for our keywords suggests that consumers may be updating their beliefs about the relevance of ads based on their evaluation of competing ads. In this respect, we also add to the existing literature on advertising, which has demonstrated learning effects of repeated advertising. We explicate the role of competing ads on learning in the sponsored search context and how this varies with attributes such as ad position and the type of keyword used.

Finally, we inform the existing theory work in the sponsored search by providing evidence of how click through performance varies across advertisers. We show that the actual consumer behavior does not conform to the common assumption in the literature about the independence of ad position from the ad quality. It depends on the arrangement for ads. High-quality ads are often observed in lower positions. Several explanations have been provided for this behavior. Jerath et al. (2011) suggest that this could be because a high-quality ad has a better relative performance in the lower position. Lu et al. (2015) attribute this to strategic bidding behavior or advertiser budget constraints. Our results suggest that the lower observed position of a high-quality ad cannot always be attributed to its relative click performance as high-quality ads will have lower relative performance as compared to low-quality ads at lower positions because of the externality effect.

Our study has several limitations. Our research captures the dominant effect of externality imposed by competing ads across all consumers. However, we do not distinguish between users. Future studies should investigate how learning effects vary across consumers. Such insights can be useful in personalized targeting of customers with sponsored search. We use a measure based on a search engine’s quality score to represent quality of the ad. However, we do not have information about the ad attributes that contribute to this quality. Future studies should investigate the relative impact of the individual ad characteristics on the click performance for different types of keywords. We also do not know the identity of our keywords. As a result, we cannot evaluate how the response to competing ads varies with other keyword characteristics. Future studies should investigate the impact of additional keyword characteristics on the click performance. Finally, we do not have information about the conversions at the advertiser website after consumers click on ads. This is a limitation of any data set obtained from search engines that cannot get conversion information from advertisers. This should not affect our results, as high click performance helps in the branding effort. However, future research should explicitly model the effect of search characteristics and ad quality on the conversion performance.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2016.0637.

## Acknowledgments

The authors would like to thank the senior editor, the associate editor, and the anonymous reviewers for their constructive comments and suggestions.

## References

Adam K (2001) Learning while searching for the best alternative. J. Econom. Theory 101(1):252–281.

Agarwal A, Hosanagar K, Smith MD (2011) Location, location and location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Agarwal A, Hosanagar K, Smith MD (2015) Do organic results help or hurt search performance. Inform. Systems Res. 26(4):695–713.

Animesh A, Ramachandran V, Viswanathan S (2010) Quality uncertainty and adverse selection in online sponsored search markets. Inform. Systems Res. 21(1):190–201.

Animesh A, Viswanathan S, Agarwal R (2011) Competing creatively in sponsored search markets. Inform. Systems Res. 22(1): 153–169.

Ansari A, Mela C (2003) E-customization. J. Marketing Res. 40(2): 131–145.

Arbatskaya M (2007) Ordered search. RAND J. Econom. 38(1): 119–126.

Athey S, Ellison G (2011) Position auctions with consumer search. Quart. J. Econom. 126(3):1213–1270.

Athey S, Nekipelov D (2012) A structural model of sponsored search advertising auctions. Working paper, University of California, Berkeley.

Brynjolfsson E, Dick AA, Smith MD (2009) A nearly perfect market? Differentiation vs. price in consumer choice. Quant. Marketing Econom. 8(1):1–33.

Celsi RL, Olson JC (1988) The role of involvement in attention and comprehension processes. J. Consumer Res. 15(9):210–224.

Craswell N, Zoeter O, Taylor M, Ramsey B (2008) An experimental comparison of click position-bias models. Proc. 2008 Internat. Conf. Web Search Web Data Mining (ACM, New York), 87–94.

Danaher PJ, Wilson IW, Davis RA (2003) A comparison of online and offline consumer brand loyalty. Marketing Sci. 22(4): 461–476.

Dellaert BGC, Haeubl G (2012) Searching in choice mode: Consumer decision processes in product search with recommendations. J. Marketing Res. 49(2):277–288.

Duan JA, Mela C (2009) The role of spatial demand on outlet location and pricing. J. Marketing Res. 46(2):260–278.

Elberse A, Eliashberg J (2003) Demand and supply dynamics for sequentially released products in international markets: The case of motion pictures. Marketing Sci. 22(3):329–354.

Emarketer (2016) U.S. digital display ad spending to surpass search ad spending in 2016. (January 11), http://www.emarketer .com/Article/US-Digital-Display-Ad-Spending-Surpass-Search -Ad-Spending-2016/1013442.

Erdem T, Swait J (2004) Brand credibility, brand consideration, and choice. J. Consumer Res. 31(1):191–198.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Ghose A, Ipeirotis P, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowd-sourced content. Marketing Sci. 31(3):493–520.

Godes D, Mayzlin D (2004) Using online conversations to study word of mouth communication. Marketing Sci. 23(4):545–560.

Granka LA, Joachims T, Gay G (2004) Eye-tracking analysis of user behavior in WWW search. Proc. 27th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 478–479.

Greene W (1999) Econometric Analysis, 4th ed. (Prentice Hall, Upper Saddle River, NJ).

Hausman J (1975) An instrumental variable approach to full information estimators for linear and certain nonlinear econometric models. Econometrica 43(4):727–738.

Hausman J (1996) Valuation of new goods under perfect and imperfect competition. Bresnahan T, Gordon R, eds. The Economics of New Goods, Studies in Income and Wealth, Vol. 58 (National Bureau of Economic Research, Chicago), 209–248.

Hogarth RM, Einhorn HJ (1992) Order effects in belief updating: The belief-adjustment model. Cognitive Psych. 24(1):1–55.

Hoque AY, Lohse GL (1999) An information search cost perspective for designing interfaces for electronic commerce. J. Marketing Res. 36(3):387–394.

iProspect (2006) iProspect search engine user behavior study. White paper, http://district4.extension.ifas.ufl.edu/Tech/TechPubs/ WhitePaper\_2006\_SearchEngineUserBehavior.pdf.

Jacoby J, Olson JC, Haddock RA (1971) Price, brand name, and product composition characteristics as determinants of perceived quality. J. Appl. Psych. 55(6):570–579.

Jansen BJ, Resnick M (2006) An examination of searchers’ perceptions of nonsponsored and sponsored links during ecommerce Web searching. J. Am. Soc. Inform. Sci. Technol. 57(14): 1949–1961.

Jerath K, Ma L, Park YH (2014) Consumer click behavior at a search engine: The role of keyword popularity. J. Marketing Res. 51(4):480–486.

Jerath K, Ma L, Park YH, Srinivasan K (2011) A position paradox in sponsored search auctions. Marketing Sci. 30(4):612–627.

Jeziorski P, Segal RI (2015) What makes them click: Empirical analysis of consumer demand for search advertising. Amer. Econom. J.: Microeconomics 7(3):24–53.

Johnson EJ, Moe WW, Fader PS, Bellman S, Lohse GL (2004) On the depth and dynamics of online search behavior. Management Sci. 50(3):299–308.

Katona Z, Sarvary M (2010) The race for sponsored links: Bidding patterns for search advertising. Marketing Sci. 29(2):199–215.

Kim JB, Albuquerque P, Bronnenberg BJ (2010) Online demand under limited consumer search. Marketing Sci. 29(6):1001–1023.

Lahiri K, Schmidt P (1978) On the estimation of triangular structural systems. Econometrica 46(5):1217–1221.

Leong S, Mishra N, Sadikov E, Zhang L (2012) Domain bias in Web search. Proc. Fifth ACM Internat. Conf. Web Search Data Mining (ACM, New York), 413–422.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1):133–153.

Lu S, Zhu Y, Dukes A (2015) Position auctions with budget constraints: Implications for advertisers and publishers. Marketing Sci. 34(6):897–905.

MacInnis DJ, Jaworski BJ (1989) Information processing from advertisements: Toward an integrative framework. J. Marketing 53(4):1–23.

Mitchell AA, Dacin PA (1996) The assessment of alternative measures of consumer expertise. J. Consumer Res. 23(3):219–239.

Musalem A, Bradlow ET, Raju JS (2008) Who’s got the coupon: Estimating consumer preferences and coupon usage from aggregate information. J. Marketing Res. 45(12):715–730.

Nevo A (2001) Measuring market power in the ready-to-eat cereal industry. Econometrica 69(2):307–342.

Newton MA, Raftery AE (1994) Approximate Bayesian inference with the weighted likelihood bootstrap. J. Royal Statist. Soc.: Ser. B (Methodological) 56(1):3–48.

Park CW, Milberg S, Lawson R (1991) Evaluation of brand extensions: The role of product feature similarity and brand concept consistency. J. Consumer Res. 18(2):185–193.

Ramlall S, Sanders D, Tewkesbury G, Ndzi D (2011) Can keyword length indicate Web users’ readiness to purchase. 2011 World Congress Comput. Sci., Comput. Engrg., Applied Comput.— WORLDCOMP’11, Las Vegas, 1–16.

Rao AR, Monroe KB (1989) The effect of price, brand name, and store name on buyers’ perceptions of product quality: An integrative review. J. Marketing Res. 26(3):351–357.

Rossi PE, Allenby GM (2003) Bayesian statistics and marketing. Marketing Sci. 22(3):304–328.

Rossi PE, Allenby GM (2005) Bayesian Statistics and Marketing (John Wiley and Sons, West Sussex, UK).

Rutz OJ, Bucklin RE (2011) From generic to branded: A model of spillover in paid search advertising. J. Marketing Res. 48(1): 87–102.

Rutz O, Trusov M (2011) Zooming in on paid search ads—A consumer-level model calibrated on aggregated data. Marketing Sci. 30(5):789–800.

Rutz O, Bucklin R, Sonnier GP (2012) A latent instrumental variables approach to modeling keyword conversion in paid search advertising. J. Marketing Res. 49(3):306–319.

Schmidt J, Spreng R (1996) A proposed model of external consumer information search. J. Acad. Marketing Sci. 24(3):246–256.

Weber TA, Zheng ZE (2007) A model of search intermediaries and paid referrals. Inform. Systems Res. 18(4):414–436.

Weitzman M (1979) Optimal search for the best alternative. Econometrica 47(3):641–654.

Wernerfelt B (1988) Umbrella branding as a signal of new product quality: An example of signalling by posting a bond. RAND J. Econom. 19(3):458–466.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

Yang S, Lu S, Lu X (2014) Modeling competition and its impact in paid-search advertising. Marketing Sci. 33(1):134–153.

Yao S, Mela CF (2011) A dynamic model of sponsored search advertising. Marketing Sci. 30(3):447–468.

Zellner A (1962) An efficient method of estimating seemingly unrelated regressions and tests for aggregation bias. J. Amer. Statist. Assoc. 57(298):348–368.
