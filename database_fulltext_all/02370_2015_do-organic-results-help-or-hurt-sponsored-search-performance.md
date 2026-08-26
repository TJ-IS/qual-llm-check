---
otero_id: 2370
otero_key: "265M4QYC"
title: "Do Organic Results Help or Hurt Sponsored Search Performance?"
authors: "Ashish Agarwal; Kartik Hosanagar; Michael D. Smith"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0593"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.130.211.199] On: 15 September 2016, At: 10:46 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/265M4QYC/fulltext/images/e084bd9ce4eebdccdea586b4ccd6c07ba08576d46848f5be485a1f5664ae955d.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Do Organic Results Help or Hurt Sponsored Search Performance?

Ashish Agarwal, Kartik Hosanagar, Michael D. Smith

## To cite this article:

Ashish Agarwal, Kartik Hosanagar, Michael D. Smith (2015) Do Organic Results Help or Hurt Sponsored Search Performance?. Information Systems Research 26(4):695-713. http://dx.doi.org/10.1287/isre.2015.0593

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/265M4QYC/fulltext/images/d07e52f91461323b97669a0b9c44b07ee954e890a629da5281bf37942fc342a7.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Do Organic Results Help or Hurt Sponsored Search Performance?

Ashish Agarwal

McCombs School of Business, University of Texas, Austin, Texas 78712, ashish.agarwal@mccombs.utexas.edu

Kartik Hosanagar

Operations, Information and Decisions, The Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104, kartikh@wharton.upenn.edu

Michael D. Smith School of Information Systems and Management, Heinz College, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, mds@cmu.edu

W<sup>e</sup> <sup>study</sup> <sup>the</sup> <sup>impact</sup> <sup>of</sup> <sup>changes</sup> <sup>in</sup> <sup>the</sup> <sup>competitors’</sup> <sup>listings</sup> <sup>in</sup> <sup>organic</sup> <sup>search</sup> <sup>results</sup> <sup>on</sup> <sup>the</sup> <sup>performance</sup> of sponsored search advertisements. Using data from an online retailer’s keyword advertising campaign, we measure the impact of organic competition on both click-through rate and conversion rate of sponsored search advertisements. We find that an increase in organic competition leads to a decrease in the click performance of sponsored advertisements. However, organic competition helps the conversion performance of sponsored ads and leads to higher revenue. We also find that organic competition has a higher negative effect on click performance than does sponsored competition. Our results inform advertisers on how the presence of organic results influences the performance of their sponsored advertisements. Specifically, we show that organic competition acts as a substitute for clicks, but has a complementary effect on the conversion performance.

Keywords: sponsored search; organic search; ad placement; hierarchical Bayesian estimation; online advertising; online auctions; search engine marketing

History: Alok Gupta, Senior Editor; De Liu, Associate Editor. This paper was received on October 5, 2012, and was with the authors 12.5 months for 3 revisions.

## 1. Introduction

Internet advertising is currently growing faster than any other form of advertising and is expected to grow from \$104 billion in 2013 to \$160 billion in 2016 (Lunden 2014). Forty percent of this advertising spending occurs on sponsored search, where advertisers pay to appear alongside the regular or organic search results of a search engine. A search engine functions as a twosided market, providing a relevant match between information providers and consumers. Most search engines, including Google, Yahoo!, and MSN, use auctions to sell their advertising inventory. In these auctions, advertisers submit bids for keywords based on their willingness to pay for a click from a consumer searching on that (or a closely related) keyword. Search engines use a combination of the submitted bid and expected click performance to set the position (rank) of the advertisement in the sponsored search results. Understanding the drivers of advertiser performance is important for both advertiser bidding strategies and the search engine’s ranking mechanism.

An important consideration in determining the performance of sponsored ads is the role of competition. Prominently placed ads by direct competitors are likely to impact the performance of a sponsored search ad because users are more likely to compare an advertiser with its direct competitors before making purchases.<sup>1</sup> Furthermore, organic results are also likely to influence sponsored search performance given that many studies suggest that consumers pay more attention to organic results compared to sponsored search results. For example, eye-tracking studies show that more users are focused on organic results compared to sponsored results (Sherman 2005). Thus, we expect that prominently placed organic results by direct competitors will impact sponsored search performance. Although advertisers recognize that competitors’ organic listings are relevant, very little has been formally established about how organic competition impacts click and conversion performance of sponsored search ads. Our paper addresses this question. We define organic competition as the prominent organic listings that directly compete with an advertiser for product sales. The level of organic competition for a sponsored search advertiser varies across keywords in its campaign and also changes for a keyword over time. These variations may be driven by differences in the number of competitors across products (and therefore keywords) or simply by changes in their relative organic positions or both.

Existing studies on advertising in general and sponsored search in particular are not unanimous regarding even the direction of impact of organic competition, let alone the magnitude of its impact. With regard to click performance, one possibility is that higher levels of organic competition would further draw user attention away from the sponsored listings. For example, consumers may spend more time evaluating organic competition if the number of competitors increases or if these competitors are placed more prominently in the organic listings (Leong et al. 2012). This would lower the click performance of sponsored advertisements due to the added cost of evaluating higher organic competition. Alternatively, an increase in organic competition can make users aware of the relevance of sponsored ads. In that case, the presence of relevant competitors in the organic results may signal a higher quality of ads, thereby leading to an increase in the click propensity for a sponsored search ad. Some theoretical studies in sponsored search suggest such complementary effects of competition. For example, Athey and Ellison (2011) suggest that users may learn about the relevance of ads from organic results, and Kempe and Mahdian (2008) suggest that low-quality organic listings may turn the user away from ads.

However, existing empirical evidence is sparse and mixed. Jeziorski and Segal (2015) show that higher competition from sponsored advertisements leads to lower marginal utility of the advertiser and to lower click propensity. Similarly, higher organic competition might lower the click performance of ads just like sponsored competition. On the other hand, Danescu-Niculescu-Mizil et al. (2010) find that an increase in the click probability of a top organic listing is also accompanied by an increase in the click probability of the top sponsored listing, irrespective of the identity of the firm, suggesting that a complementary effect might exist between organic and sponsored results. However, the authors do not account for unobservable keyword characteristics, and it is therefore unclear whether the result is driven by true complementarity or simply by unobserved consumer preferences for keywords rather than actual consumer response to an increase in the organic competition. Finally, Yang and Ghose (2010) find that an advertiser’s own organic listing has a complementary effect on its own sponsored listing: an increase in the click probability of an organic listing of an advertiser increases the click probability of its sponsored listing. They attribute this result to the positive opinion generated by an advertiser’s organic listing. Whether the same effect applies for increased organic competition is an open empirical question. Thus, it is not clear whether organic competition takes user attention away from a sponsored search ad, thereby reducing its clicks, or helps generate trust and thereby increases clicks for sponsored search advertisements.

Additionally, studies in the literature have only considered the effect of organic listings on click-throughs, not conversions. A priori, it would appear that post click conversion should not be affected by the variation in competition because prescreening information may be irrelevant in subsequent search behavior (Chakravarti et al. 2006). Thus, user conversion may be influenced more by the information presented on the landing page for an ad than by the information evaluated prior to clicking on the ad. However, the learning effect can also help drive conversions. Buyers are more involved compared with other consumers (Moe 2003) and may demonstrate a higher learning effect. As a result, the presence of relevant direct competitors may cause a buying consumer to perceive the advertiser to be of higher quality and thereby increase the probability of conversion. Finally, the sequence in which results are evaluated can also influence the conversion performance. It is well known that primacy (a preference for a product that was evaluated first) and recency (a preference for the most recently evaluated product) affect both brand and product recall in many environments. If more competitors show up in the prominent positions, then consumers are more likely to visit the advertiser toward the end of their search In that case, a primacy effect may cause conversion rates to drop when dominant competitors appearing in organic results are evaluated earlier. By contrast, some studies show that in sequential choice environments, consumers are disproportionately influenced by the attractiveness of the most recently evaluated product. In sponsored search environments, recency effects play a role for the top few positions (Agarwal et al. 2011). In that case, higher organic competition can cause conversion rates to increase due to a recency effect. Thus, it is possible that changes in organic competition might affect conversion rates as well. Table 1 summarizes the relevant literature and the likely impacts suggested by these papers.

In the present paper, we analyze how competition from prominent organic listings of direct competitors impacts click and conversion performance in sponsored search. We use a field experiment to generate a unique panel data set of daily clicks, orders, and costs for multiple keywords in a sponsored search advertising campaign for an online retailer. Our experiment systematically varies the bids on ads to achieve a wide range of positions in the list of sponsored search results. We also use a Web crawler to capture competitors’ organic and sponsored search results displayed alongside our advertisements. We account for potential endogeneity in our measure of organic competition and validate our results with alternative measures of competition and several other robustness measures.

Table 1 Impact of Organic Competition on Propensity to Click and Convert

<table><tr><td></td><td>Click-through rate</td><td>Conversion rate</td></tr><tr><td>Negative effect</td><td>Message orderingConsumers more likely to visit the advertiser toward the end due to increase in organic competition and less likely to click due to satiation (Jeziorski and Segal 2015)</td><td>Message orderingConsumers more likely to visit the advertiser toward the end due to increase in organic competition and less likely to convert due to primacy effects (Pieters and Bijmolt 1997)</td></tr><tr><td>Positive effect</td><td>Awareness and learningHigh competition makes consumers aware of the relevance of sponsored ads (Liu et al. 2015, Sahni 2015) and update their belief about the quality of focal advertiser (Athey and Ellison 2011)</td><td>Message orderingConsumers more likely to visit the advertiser toward the end due to increase in organic competition and more likely to convert due to recency effects (Wedel and Pieters 2000)Awareness and learningHigh competition makes consumers aware of the relevance of sponsored ads (Liu et al. 2015, Sahni 2015) and update their belief about the quality of focal advertiser (Athey and Ellison 2011)Buying consumers more likely to learn and update their belief about the quality of focal ad due to higher involvement (Moe 2003) and subsequent learning (Park and Hastak 1994, Wood and Lynch 2002).Buying consumers more likely to recall competition while visiting focal ad site (Kent and Allen 1994) and more likely to learn in the presence of higher competition</td></tr><tr><td>No impact</td><td></td><td>Consumers do not rely on prescreening information and buy from the best listing (Chakravarti et al. 2006)</td></tr></table>

We have three main findings. First, we find that click performance of ads decreases with an increase in organic competition. This suggests that organic competition imposes a negative externality on sponsored search performance. Second, we find that conversion rate and revenues increase with greater organic competition. In the presence of increased organic competition, buyers visiting a sponsored ad are more likely to buy from the ad, potentially due to higher quality perception of ads in the presence of high quality organic competition. Third, we find that organic competition has a higher impact on the performance of ads compared to sponsored competition. Users may trust organic results more than sponsored results (Jansen and Resnick 2006) and, as a result, may be more responsive to changes in organic competition compared to the changes in sponsored competition. In short, our results show that organic competition acts as a substitute for clicks, but has a complementary effect on conversion performance. Overall, the findings of this study extend the understanding of consumer behavior in sponsored search and yield important implications for advertisers and search engines.

The rest of this paper is organized as follows. We first review the related literature and provide the theoretical background (§2). In §3, we describe the data and the definition of competition measures. In §4, we discuss the model and the estimation procedure. In §5, we explain our results. We discuss the implications of our results and conclude the paper in §6.

## 2. Theoretical Background

Our research is most closely related to the literature on consumers’ online search and purchase behavior, with an emphasis on the impact of message ordering and competition. Our research is also related to the literature on advertiser performance in sponsored search. We draw from these two literatures to explain the potential impact of organic competition on sponsored search performance.

## 2.1. Consumers’ Online Search and Purchase Behavior

A specific aspect of search behavior that our work relates to is the order of messages and its implications on search and consumer choice. Prior work in traditional media has demonstrated that message ordering influences ad persuasion (Rhodes et al. 1979, Brunel and Nelson 2003). Similar results have been shown in online environments. Hoque and Lohse (1999) found that consumers are more likely to choose advertisements near the beginning of an online directory than they are when using paper directories. Ansari and Mela (2003) found that in an email campaign, higher position listings lead to a higher probability of clicking. There is also evidence that ordering of sponsored search results impacts performance. For example, Ghose and Yang (2009) found that the click-through rate (CTR) of an advertisement decreases with position.

Sponsored search performance is also affected by the intensity of competition, which may not be fully reflected in an ad’s relative position. Animesh et al. (2011) define competition in terms of the quality of competitors who are advertising alongside a focal ad and show that higher intensity of such competition lowers the click performance of an advertiser. Similarly, Jeziorski and Segal (2015) find that advertisers appearing higher up in the search results impose a negative externality on the lower ads and attribute it to information satiation.

Although these studies focus on ad position and competition intensity vis-à-vis sponsored search competitors, both the level of competition and the order in which an ad is evaluated are impacted by organic competitors as well. Using eye-tracking analysis, Granka et al. (2004) find that users generally investigate search results sequentially, from top to bottom and left to right. This suggests that a sponsored search ad appearing on the right-hand side is likely to be reviewed after the organic results appearing to the left and above the sponsored search ad. In that case, any variation in organic competition can impact competitive intensity as well as the order in which results are evaluated and, in turn, an ad’s click and conversion performance. Even if sponsored ads appear above the organic listings, they receive less attention compared to the top organic listings (Danescu-Niculescu-Mizil et al. 2010).

In terms of click performance, one possibility is that an increase in organic competition negatively impacts CTRs of sponsored ads in much the same way that an increase in sponsored competition does; that is, satiation through competing products in the organic results may imply that fewer consumers will reach and click the sponsored search ad. However, an increase in organic competition can make consumers aware of the relevance of sponsored ads to their search. There is evidence of such positive spillover of competition (Liu et al. 2015, Sahni 2015) on a firm, as advertising by competition makes users aware of the relevance of a category and consider other products in the category. As a result, consumers may update their belief about the quality of the sponsored ad in the presence of high organic competition. Athey and Ellison (2011) suggest the possibility of such Bayesian updating as consumers sequentially evaluate ads. This is particularly important in analyzing the interplay between organic and sponsored results because consumers are known to trust organic results more than sponsored search results (Jansen and Resnick 2006). As a result, consumers may learn about the quality of ads based on their evaluation of prominent competing listings including competitors’ organic listings. Furthermore, Dellaert and Haubl (2012) show that users are likely to terminate their search early when they sequentially evaluate a list of recommendations and there is a high variability or poor accuracy. In the search context, consumers may form an expectation about ad relevance based on the presence of organic competition, and greater organic competition may lead to higher click performance for a sponsored ad.

Advertiser revenues depend not only on clicks but also on conversion/purchase probability after clicking on an ad. One possibility is that organic competition has no impact on purchase probability conditional on clicking. Some studies show that consumers tend to deemphasize prescreening information in their search process (Chakravarti et al. 2006). This suggests that the criteria used for selecting an advertisement may not affect the final purchase as much as information obtained after visiting the website. Thus, if a consumer discounts all prescreening information and buys from the website that maximizes her utility, the conversion rate may not be affected by competition.

Alternatively, buying consumers may form expectations about the quality of a sponsored ad based on previously evaluated listings, and this can influence their purchase behavior conditional on clicking the ad. As mentioned earlier, consumers may demonstrate a learning effect based on their evaluation of organic competition. Furthermore, buying consumers are more likely to be involved compared to browsing consumers (Moe 2003). Such high involvement leads to better retrieval of information (Park and Hastak 1994), and high attention leads to superior learning (Wood and Lynch 2002). Thus, buying consumers may show a higher learning effect compared with consumers just collecting information and may be more likely to update their belief about the quality of sponsored ad in the presence of high competition. In that case, high trust for organic results (Jansen and Resnick 2006) may cause buyers to value an ad more in the presence of higher organic competition, leading to a higher conversion rate conditional on clicking. Additionally, this learning effect can depend on the user’s ability to recall competitors and their attributes. When a consumer visits the site associated with an ad, to compare attributes of all of the evaluated listings, she has to recall competing brands and their attributes from previously visited sites in the search results. Kent and Allen (1994) find that it is easier to recall a familiar brand than an unfamiliar brand. In sponsored search, consumers are more likely to be familiar with direct competitors appearing in prominent organic positions. Thus, we can expect that a consumer is more likely to recall prominent organic competition and update her belief about the quality of the advertiser.

Finally, sequential evaluation can also influence conversion performance conditional on clicking. It is well known that consumers cannot perfectly recall product information from all evaluated products and websites, and the sequence in which they evaluate these choices can affect their purchase decisions. An increase in organic competition associated with a focal advertiser would draw more user attention to these competitors’ listings. If this reduces the CTR of the focal ad, it also implies that consumers who do end up clicking the focal ad are more likely to click the ad toward the end of their search. Traditional advertising studies have demonstrated primacy effects in the recall of brand and product information (e.g., Pieters and Bijmolt 1997). If the primacy effect plays a role, then consumers may be more likely to go back to the competitors’ organic listings to buy from these listings. This can result in a conversion rate that decreases with increased organic competition for a given position of the advertiser. However, recency effects might help the sponsored ads in the presence of higher organic competition. Wyer and Srull (1986) show recency effects under conditions of high information load. Wedel and Pieters (2000) also find a recency effect in the recall of advertisements in a print magazine. Häubl et al. (2010) show that in the context of sequential choice, consumers are disproportionately influenced by the attractiveness of the most recently evaluated product. This suggests that the consumers who are likely to buy are more likely to do so from the website they evaluate last rather than the website they evaluate early in their sequential search. Agarwal et al. (2011) find that the conversion rate for ads increases with position for the top few positions, which they attribute to such a recency effect. Organic competition may have a similar effect at a particular ad position. If higher organic competition leads buyers to visit a sponsored ad later, then consumers may be more likely to buy from the sponsored ad in the presence of higher organic competition.

We summarize the relevant theories and the predictions that emerge from these theories in Table 1. In summary, there is a strong reason to believe that organic competition will impact the performance of sponsored search ads, but the nature of this impact is not obvious.

## 2.2. Sponsored Search Markets

Existing work in sponsored search has focused on auction design, consumer behavior, and advertiser strategy. In terms of work on auction design from the search engine’s perspective, Edelman et al. (2007) compute the equilibria of the generalized second price sponsored search auction and demonstrate that this auction, unlike the Vickrey–Clarke–Groves mechanism, is not incentive compatible. Weber and Zheng (2007) compare the performance of various ad-ranking mechanisms, finding that a yield-optimized auction, with ranking based on a combination of the submitted bid and ad relevance, provides the highest revenue to the search engine. Dellarocas (2012) evaluates the double marginalization issue associated with sponsored search auctions and suggests that the current design can lead to a lower consumer surplus as well as social surplus. Xu et al. (2011) evaluate the impact of endogenous pricing on the advertiser incentives for bidding. Liu et al.

(2010) study the impact of different ranking policies and minimum bids on the bidding outcome when the advertisers differ in their click potential or preference. Liu and Viswanathan (2014) evaluate the performance of the different pay-for-performance pricing schemes in online advertising in the presence of information asymmetry. These studies do not focus on the organic competition and its impact on the auction design.

In terms of consumer behavior, Ghose and Yang (2009) and Agarwal et al. (2011) study the impact of ad position on click and conversion performance. Rutz and Trusov (2011) study the impact of ad textual properties on consumer click propensity. However, none of these studies considers the impact of organic results on consumer behavior. In their theoretical work, Katona and Sarvary (2010) assume a preference for organic results on the part of consumers, and Jansen and Resnick (2006) find results consistent with a negative bias for sponsored search ads relative to organic search results. Xu et al. (2012) investigate the bidding incentive of different advertisers in the presence of organic listings. Yang and Ghose (2010) find complementarity between an advertiser’s own organic listing and its sponsored listing. However, these papers do not consider the impact of competitors’ organic listings on sponsored search results. Additionally, while modeling clicks, Yang and Ghose (2010) do not explicitly study the effect of organic results on the conversion performance of sponsored ads. Prior research suggests that consumer conversion behavior can differ significantly from their click behavior (Agarwal et al. 2011).

In terms of work on advertiser strategies, several recent studies have focused on optimal bidding strategies for advertisers (Feldman et al. 2007, Xu et al. 2012, Hosanagar and Cherapanov 2008, Abhishek and Hosanagar 2013). Zhang and Feng (2011) show that advertisers may engage in cyclical bid adjustments, and equilibrium bidding prices may follow a cyclical pattern. However, none of these studies explicitly investigates the impact of organic competition on advertiser revenues and profitability. Animesh et al. (2011) show that competitive intensity has a different impact on click performance depending on the differentiation of the advertiser. This highlights the importance of studying competitive intensity. Our work complements these studies on sponsored search markets by evaluating the impact of organic competition on ad performance and demonstrating the value of that insight for advertisers.

## 3. Data

Our main data set was generated through a field experiment with a pet product company’s sponsored search ad campaign on Google. The data were generated by submitting randomized bids for several keywords and measuring consumer response in terms of clicks and orders for varying organic competition associated with the ads corresponding to the keywords. Next, we explain our experimental design and how we construct our measure of competition.

To evaluate organic competition for a sponsored search ad, we consider prominent organic results of direct competitors that are likely to compete for attention with the sponsored search ad. Prior research suggests that consumers evaluate search results from top to bottom and left to right and pay greater attention to organic results compared to sponsored results (Granka et al. 2004). In that case, consumers considering an ad are very likely to pay attention to organic results appearing at the same level or above and to the left of the ad. As a result, we consider the relevant organic competition for an advertiser to be competitors’ organic listings that appear at the same level or above and to the left of the advertiser’s ad for a keyword.<sup>2</sup>

To study the effect of organic competition on click and conversion performance of sponsored search ads, we can evaluate ad performance as a function of the variation in the organic competition across keywords. However, variation in competition across keywords and over time may not be truly exogenous. The extent of direct organic competition for a keyword may reflect consumer demand and advertiser fit with the keyword. If consumers are more likely to respond to product listings for a given keyword or at a given time (say during the holidays), then the search engine may be more likely to show several product listings in organic results, and competitors may also be more likely to invest in search engine optimization to drive higher placement in organic search. Thus, high levels of organic competition for a keyword may be a result of consumer preferences rather than the other way around. This makes the identification of the effect of organic competition difficult. To address this challenge, we attempt to create variation in organic competition for each keyword to establish the effect of organic competition.

Organic competition for a keyword may change over time in response to exogenous website changes made by the corresponding firms or because of endogenous strategic decisions by firms in response to consumer demand. Ideally, we want to drive some exogenous variation in the number and intensity of competitors. Although it is hard for us to introduce random changes in organic results, we can achieve such variation in organic competition for an ad by varying the ad position over time. For example, Figure 1 shows the competitors’ organic listings for two different positions of the focal advertiser at two different points in time. The number and the relative positions of competitors organic listings appearing above and to the left of the focal ad are different for the two ad positions. Thus, consumers visiting the sponsored ad at different positions are likely to evaluate different levels of organic competition, which means that the click and conversion performance of an ad can be evaluated as a function of the organic competition after controlling for the effect of the ad position. We achieve this variation in the ad position and the corresponding organic competition by randomizing bids for each ad. Randomized bids allow us to rotate the ads associated with the experimental keywords across multiple positions on the results page and measure consumer response in terms of clicks and orders as a function of organic competition for a wide range of ad positions. Although this approach allows us to focus on organic competition appearing above or at the same level as a focal advertiser, it does not capture the effect of organic competition appearing in other positions. This is a limitation of our approach.

Our experiment keywords were chosen randomly from a set of keywords in the campaign that had generated clicks and at least one order for the retailer in the past 60 days. We used Google’s keyword tool to determine the range of bids for each keyword. The bid range was wide enough for each keyword to ensure that corresponding ads could be placed in various slots available on the first page. Additionally, we ensured that the ad for a keyword appeared in a particular position for several days. All sponsored search data came from Google’s advertiser dashboard. In addition, we used an automated Web crawler to determine the organic results that consumers would see in response to search queries corresponding to the experimental keywords.<sup>3</sup>

Google allows advertisers to use “broad,” “exact,” or “phrase” match for their keywords. An “exact” match ensures that the search query exactly matches the chosen keywords. However, that is not true for a “broad” match or a “phrase” match. For example, if the advertiser bids on a keyword “shirt” with a broad match, its ad can be shown in response to all search queries that include the word “shirt.” However, if the advertiser specifies an “exact” match, then its ad will be shown only for a search query “shirt.” One issue with “broad” and “phrase” match keywords is that the exact set of competitors may vary based on the search query. In the example above, if the advertiser bids on the keyword “shirt” with a broad match, then its ad can potentially be matched with 800 key phrases according to Google Adwords (e.g., “red shirt,” “formal shirt”). In that case, we will not know the actual key phrases for which the ad was shown and the corresponding organic results.<sup>4</sup> To ensure that we can replicate the search results corresponding to the keywords, we only used keywords with an “exact” match in our sample. This ensures that we know the actual search term that was used by the consumer and therefore can replicate the organic results that the consumer would most likely have seen.

Figure 1 (Color online) Competing Organic and Sponsored Listings for Different Positions of the Focal Advertiser  
![](/api/attachments/265M4QYC/fulltext/images/fc204a7a7afa5aa89ac0fb0b703d97be49463fbfbd29c3aff8586a7af9831330.jpg)

Organic search results for every keyword can include listings of websites selling related products as well as listings for purely information-oriented sites such as wikis and information portals. We identify competitors’ listings as listings that are selling a product similar to that of our focal advertiser. Sponsored search results can also include advertisers who are not selling similar products. We eliminate such advertisers. For example, an advertiser offering “dog care” may show up as a sponsored ad for “dog food,” and we do not consider it as a competitor for an advertiser selling dog food. We determined 136 competitors’ organic results and 108 other organic results for our keywords appearing above or at the same level as our advertiser’s ad. We also determined 89 competitors’ sponsored results and 30 other sponsored results, and we verified the list of competitors with our advertiser.

We represent organic competition and sponsored competition in terms of the daily cumulative number of competitors’ listings for each type appearing at the same level or above the focal ad (see Figure 1). Consumers may place more attention on a competitor listed very high relative to a competitor appearing lower in the listings. As a result, we weigh each competitor’s listing by its position to account for the relative prominence of the listing. Furthermore, the intensity of competition will be higher if the organic competition includes competitors with a high perceived quality versus a scenario where the organic competition has competitors with relatively low perceived quality. For example, if a listing from a brand with higher perceived quality appears higher, it can have a greater impact on user choice compared to a listing of competitors with lower perceived quality. To account for such a differential effect of competing sites, we normalize the position of a listing with a measure of a competitor’s perceived quality. Following the literature, we use the Alexa rank obtained from Alexa.com as the measure of perceived quality for competitor listings appearing in organic and sponsored search results (Brynjolfsson and Smith 2000, Palmer 2002, Animesh et al. 2010). The Alexa rank is computed based on Alexa.com’s estimate of daily unique visitors and page views for the website.<sup>5</sup> Daily unique visitors capture the number of visitors, and page views capture the engagement of these visitors. Websites are ranked based on an Alexa.com proprietary function that combines the number of visitors and page views. Note that the Alexa rank may vary over time, and we use the average Alexa rank of each website during the panel period of the experiment to represent the perceived quality of the website. Therefore, we specify the level of competition for each type of listing as

$$
\text { Competition } _ {k t} = \sum_ {C _ {k t}} \frac {\log (\text { AlexaRank } _ {F})}{\text { Pos } _ {C _ {k t}} \times \log (\text { AlexaRank } _ {C _ {k t}})},
$$

where $P o s _ { C _ { k t } }$ is the position of the listing of competitor C for keyword k at time $t , A l e x a R a n k _ { C _ { k t } }$ is its average Alexa rank for the panel period, and AlexaRank<sub>F</sub> is the Alexa rank of the focal advertiser.

Thus, a lower position (higher numerical value) of a competitor’s listing will result in a lower contribution to the measure of competition. Similarly, lower quality of a competitor’s listing (higher numerical value of the Alexa rank) would lead to a lower contribution. To ensure that our results are robust to our measure of competition, we also consider simpler alternative measures of organic competition and sponsored competition. These include measures based only on the competitor’s position in the organic results $( \mathrm { i . e . , }$ no Alexa rank) and only on the competitor’s perceived quality (i.e., no position). These measures are defined in §4. Our results are qualitatively similar for all three measures and are described in $\ S { \dot { 5 } } .$

To account for other factors that may influence consumer click behavior on sponsored results, we also capture the quality score measure maintained by Google and available to the advertiser (the listed quality (LQ) score). This measure represents the click propensity of an advertiser and is calculated by Google based on several metrics, including the relative CTR of the advertiser for the keyword and the relative quality of the ad and landing page. Google uses a sliding window to determine the value of the quality score. However, this value remained unchanged during the course of the experiment for our keywords.

Our resulting data set consists of 1,440 observations of daily impressions, clicks, and orders for 36 keywords over a 40-day period from June 2009 to July 2009. Table 2 provides summary statistics for our data, and Table 3 provides the correlation matrix for our main variables. Note that the observations represent daily aggregate data for advertisements corresponding to the sample keywords for our advertiser, and that the data set is typical of the information received by sponsored search advertisers. Advertisers do not receive individual-level impressions or click data and do not have information on the performance of competing advertisements.

## 4. Simultaneous Model

Consider an advertiser placing bids for a keyword to ensure its advertisements are visible in the list of sponsored results for queries related to that keyword.

Table 2 Keyword Performance Summary Statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Impressions</td><td>72.8</td><td>159</td><td>1</td><td>1,666</td></tr><tr><td>Click</td><td>1.1</td><td>2.2</td><td>0</td><td>24</td></tr><tr><td>Orders</td><td>0.03</td><td>0.2</td><td>0</td><td>3</td></tr><tr><td>AdPos</td><td>3.47</td><td>1.7</td><td>1</td><td>9.78</td></tr><tr><td>Organic</td><td>0.15</td><td>0.36</td><td>0</td><td>1</td></tr><tr><td>Organic_Comp normalized by position and Alexa Rank</td><td>0.78</td><td>0.54</td><td>0</td><td>3.08</td></tr><tr><td>Organic_Comp normalized by position</td><td>0.82</td><td>0.53</td><td>0</td><td>2.69</td></tr><tr><td>Organic_Comp normalized by Alexa Rank</td><td>1.7</td><td>1.52</td><td>0</td><td>10.1</td></tr><tr><td>IVOrganic</td><td>0.42</td><td>0.23</td><td>0.1</td><td>2.34</td></tr><tr><td>Sponsored_Comp normalized by position and Alexa Rank</td><td>1.79</td><td>0.89</td><td>0</td><td>5.59</td></tr><tr><td>Sponsored_Comp normalized by position</td><td>1.82</td><td>0.95</td><td>0</td><td>4.43</td></tr><tr><td>Sponsored_Comp normalized by Alexa Rank</td><td>3.28</td><td>2.1</td><td>0</td><td>11.4</td></tr><tr><td>IVSponsored</td><td>1.49</td><td>1</td><td>0.13</td><td>5.19</td></tr><tr><td>LQScore</td><td>8</td><td>1.5</td><td>6</td><td>10</td></tr><tr><td>Brand</td><td>0.6</td><td>0.5</td><td>0</td><td>1</td></tr><tr><td>Specificity</td><td>0.4</td><td>0.7</td><td>0</td><td>1</td></tr><tr><td>Bid</td><td>0.5</td><td>0.3</td><td>0.08</td><td>2</td></tr></table>

The search engine uses this bid, and the expected ad performance, to determine the advertisement’s position in the list of sponsored search ads. The search engine also shows the corresponding organic results. Consumers see the organic results and advertisements and decide to click on some of the ads, and subsequently decide whether to make a purchase. Thus, the search engine’s decisions influence both the position of our advertiser’s and the competitors’ listings in organic and sponsored results. We simultaneously model consumers’ click-through and conversion behavior, and use an instrumental variable (IV) approach to address the endogeneity of ad position and competition measures.

## 4.1. Click-Through Rate per Impression

A consumer’s choice of clicking on an advertisement can be modeled in terms of the latent utility of clicking. This in turn depends on the position of the advertisement and the quality of the advertiser, as well as the competition from organic and sponsored results. Consumers are expected to search sequentially from top to bottom (Ghose and Yang 2009). An ad’s position influences its click performance. A lower position may lead to a perception of lower quality because consumers are used to evaluating ads in the decreasing order of quality. Furthermore, consumers can be influenced by the extent of competition appearing above the focal advertisement. As mentioned earlier, we count the total number of competitors while accounting for the position and the Alexa rank of the listing.<sup>6</sup>

Table 3 Correlation Matrix

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td><td>(13)</td><td>(14)</td><td>(15)</td></tr><tr><td>(1) Impressions</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Clicks</td><td>0.42</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Orders</td><td>0.10</td><td>0.22</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) AdPos</td><td>0.16</td><td>-0.08</td><td>-0.02</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Organic</td><td>0.08</td><td>-0.03</td><td>-0.04</td><td>0.15</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) Organic_Comp normalized by position and Alexa Rank</td><td>-0.06</td><td>-0.06</td><td>0.01</td><td>0.16</td><td>0.00</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7) Organic_Comp normalized by position</td><td>-0.09</td><td>-0.02</td><td>0.01</td><td>0.07</td><td>-0.05</td><td>0.87</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8) Organic_Comp normalized by Alexa Rank</td><td>-0.03</td><td>-0.11</td><td>0.01</td><td>0.54</td><td>0.07</td><td>0.72</td><td>0.54</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(9) IVOrganic</td><td>-0.06</td><td>-0.06</td><td>-0.02</td><td>0.38</td><td>-0.09</td><td>0.57</td><td>0.62</td><td>0.63</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(10) Sponsored_Comp normalized by position and Alexa Rank</td><td>0.11</td><td>-0.10</td><td>0.00</td><td>0.49</td><td>0.20</td><td>0.17</td><td>0.11</td><td>0.35</td><td>0.19</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(11) Sponsored_Comp normalized by position</td><td>0.16</td><td>-0.02</td><td>0.03</td><td>0.51</td><td>0.17</td><td>0.14</td><td>0.17</td><td>0.31</td><td>0.28</td><td>0.85</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(12) Sponsored_Comp normalized by Alexa Rank</td><td>0.11</td><td>-0.11</td><td>-0.02</td><td>0.71</td><td>0.21</td><td>0.20</td><td>0.12</td><td>0.51</td><td>0.31</td><td>0.84</td><td>0.72</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(13) IVSponsored</td><td>0.27</td><td>0.03</td><td>0.03</td><td>0.52</td><td>0.15</td><td>0.12</td><td>0.14</td><td>0.31</td><td>0.24</td><td>0.65</td><td>0.77</td><td>0.67</td><td>1.00</td><td></td><td></td></tr><tr><td>(14) LQScore</td><td>-0.20</td><td>0.05</td><td>0.00</td><td>-0.14</td><td>-0.06</td><td>0.24</td><td>0.31</td><td>0.04</td><td>0.16</td><td>-0.02</td><td>-0.05</td><td>-0.07</td><td>-0.05</td><td>1.00</td><td></td></tr><tr><td>(15) Bid</td><td>0.21</td><td>0.25</td><td>0.16</td><td>0.17</td><td>-0.02</td><td>-0.05</td><td>-0.09</td><td>0.05</td><td>0.02</td><td>0.06</td><td>0.15</td><td>0.08</td><td>0.32</td><td>-0.14</td><td>1.00</td></tr></table>

We use the quality score measure provided by the search engine to account for other factors, such as ad relevance and the quality of the landing page. The advertiser’s own listing can appear in the organic results for certain keywords and can influence the performance of the sponsored listing (Yang and Ghose 2010). We control for this by using a dummy variable that is set to one if the advertiser’s organic listing appears on the first page and set to zero otherwise.<sup>7</sup>

Our unit of analysis is a keyword because the search engine auction is keyword specific. Keyword characteristics are an indication of underlying search behavior, which varies across consumers. For example, the keyword “dog food” is less specific and likely indicates an initial stage of information search, whereas more specific keywords (e.g., “natural dog food,” “Freshpet dog food rolls”) likely indicate a more advanced and directed stage of information search. To account for these differences across keywords, we capture how specific a keyword is using two different measures: “specificity” and “brand.” The specificity of a keyword is based on the nearness of its landing page to the product. Advertisers organize their websites in a hierarchical fashion to accommodate the search intent of users and to reduce their search cost. Levels in the hierarchy represent product categories, subcategories, and products. When consumers are routed through a search engine, the landing page coincides with a level in the website hierarchy that is chosen based on the search intent of the consumer as reflected in the keyword. We define specificity as the level in the product hierarchy of the advertiser. For example, a top-level keyword such as “pet food” would have the specificity value of zero, a second-level keyword representing products such as “dog food” would have the specificity value of one, and so on. Figure 2 shows the hierarchy for pet food in a representative website in the pet food market and the associated specificity levels. Brand is indicated by the presence of a well-recognized manufacturer brand name in the key phrase.<sup>8</sup> This approach for representing keyword heterogeneity is similar to the one adopted by Agarwal et al. (2011), Ghose and Yang (2009), and Yang and Ghose (2010).

We use a hierarchical model to capture the effect of keyword characteristics. This provides a flexible random component specification that allows us to incorporate both observable and unobservable keywordspecific heterogeneity, given the small number of observations for each keyword. This approach allows us to do a within-keyword analysis and ensure that the effect of organic competition is not confounded by the unobserved heterogeneity across keywords. Furthermore, hierarchical models are commonly used to draw inferences on individual-level characteristics (e.g., Rossi and Allenby 2003). Hierarchical Bayesian (HB) models were also recently applied to study sponsored search data with keywords as a unit of analysis (Ghose and Yang 2009, Yang and Ghose 2010, Agarwal et al. 2011, Rutz et al. 2012).

Figure 2 Website Hierarchy for Pet Food Website  
![](/api/attachments/265M4QYC/fulltext/images/d407b0f5cc1e18740aa9a1cbbc01a7af75e36ea064d9896a649fe4f1b01bfb58.jpg)

In our model, we assume an independent and identically distributed (i.i.d.) extreme value distribution of the error term for individual choices and use a logit model to represent the click probability for a keyword k at time t as follows:

$$
\Lambda_ {k, t} ^ {C T R} = \frac {\exp (U _ {k t} ^ {C T R})}{1 + \exp (U _ {k t} ^ {C T R})},\tag{1}
$$

where $\mathbf { U } _ { k t } ^ { C T R }$ is the latent utility of clicking. For a keyword k at time $t ,$ the latent utility of clicking can be expressed as

$$
\begin{array}{r l} & U _ {k t} ^ {C T R} = \theta_ {0} ^ {k} + \theta_ {1} ^ {k} A d P o s _ {k t} + \theta_ {2} ^ {k} O r g a n i c \_ C o m p _ {k t} \\ & \qquad + \theta_ {3} ^ {k} S p o n s o r e d \_ C o m p _ {k t} + \theta_ {4} O r g a n i c _ {k t} \\ & \qquad + \theta_ {5} L Q S c o r e _ {k t} + \theta_ {\text {Time}} T i m e _ {k t} + \varepsilon_ {k t} ^ {\theta}, \\ & \boldsymbol {\theta} ^ {k} = \Delta^ {\theta} z _ {k} + u _ {k} ^ {\theta} \quad u _ {k} ^ {\theta} \sim N (0, V ^ {\theta}), \end{array}\tag{2}
$$

where AdPos represents the position of the ad in the sponsored search results, Organic\_Comp is competition in organic results, Sponsored\_Comp is competition in sponsored results, Organic is a dummy indicating whether the advertiser’s organic listing appears on the top page for keyword k and time t, LQScore is the quality score of the ad, Time controls for time dynamics in the auction, $\varepsilon _ { k t } ^ { \theta }$ represents the time varying unobserved keyword attributes that are common for all consumers, $z _ { k }$ represents keyword specific characteristics brand and specificity, $\Delta ^ { \theta ^ { \dagger } }$ is a matrix capturing the relationship between keyword characteristics and the mean values of coefficients, and $u _ { k } ^ { \theta }$ represents the unobservable heterogeneity for each keyword, which we assume is normally distributed with a mean 0 and covariance matrix $\dot { V } ^ { \theta }$

We consider random coefficients for our main variables of interest, which are also varying for each keyword. For the control variables, we assume that the variation in response across keywords is captured by the coefficient of the constant term. This approach is commonly used in the random coefficient models because it leads to no change in the model parameters for the variables of interest (Duan and Mela 2009, Ghose and Yang 2009, Yang and Ghose 2010).

## 4.2. Conversion Rate per Click

Conversion rate (probability) refers to the fraction of clicks that generate orders. A consumer’s choice of buying conditional on clicking would depend on the position to account for the recall effects as observed in previous research (Ghose and Yang 2009, Agarwal et al. 2011). It is possible that the complementarity of the advertiser’s own organic listing has an effect on the conversion performance as well. The conversion behavior would also be influenced by the competition and the quality score (Ghose and Yang 2009).

Assuming an i.i.d. extreme value distribution of the error term for individual choices, we can express the conversion probability as

$$
\Lambda_ {k t} ^ {C O N V} = \frac {\exp (U _ {k t} ^ {C O N V})}{1 + \exp (U _ {k t} ^ {C O N V})},\tag{3}
$$

where $U _ { k t } ^ { C O N V }$ is the latent utility of conversion, which may depend on the position of the advertisement. As above, organic and sponsored competition can influence the conversion probability. For keyword k at time $t ,$ this latent utility can be expressed as

$$
\begin{array}{r l} & U _ {k t} ^ {C O N V} = \beta_ {0} ^ {k} + \beta_ {1} ^ {k} A d P o s _ {k t} + \beta_ {2} ^ {k} O r g a n i c \_ C o m p _ {k t} \\ & \qquad + \beta_ {3} ^ {k} S p o n s o r e d \_ C o m p _ {k t} + \beta_ {4} O r g a n i c _ {k t} \\ & \qquad + \beta_ {5} L Q S c o r e _ {k t} + \beta_ {\text {Time}} T i m e _ {k t} + \varepsilon_ {k t} ^ {\beta}, \\ & \boldsymbol {\beta} ^ {k} = \Delta^ {\beta} z _ {k} + u _ {k} ^ {\beta} \quad u _ {k} ^ {\beta} \sim N (0, V ^ {\beta}). \end{array}\tag{4}
$$

We also include controls for the time dynamics.

## 4.3. Ad Position

The search engine determines the position of an advertisement for a keyword based on the product of the current bid and the quality of the advertisement relative to competing ads. As mentioned earlier, this relative quality measure is called the “quality score” and is available to advertisers through Google. The dependence of ad position on bid and quality score introduces two sources of endogeneity: that related to the advertiser’s bid decision and that related to the search engine’s ad position decision. Advertisers can influence the position of their advertisements by changing their bids (for example, to optimize performance). As a consequence, position is endogenously determined. Furthermore, search engines might assign advertisers to specific positions that yield the search engine the highest revenues.

To control for this potential endogeneity, we have to account for the advertiser’s bid choices as well as the position assigned by the search engine. In our setup, bids were randomized for the sample keywords. Thus, the bid amounts are, by design, exogenous during the field experiment, taking away any strategic effect of our advertiser. Using a wide range of random bids also ensures that even if other advertisers are bidding using their own objective functions, the advertisements in our experiment are exposed to consumers over a wide range of positions.

Endogeneity is also introduced because search engines use ad performance data to compute an ad’s position. To account for this, we use an IV approach and model ad position as a function of the randomized bid. Because a search engine uses both bid and quality score to determine an ad’s position, we also account for the effect of quality score. Similar approaches were used by Ghose and Yang (2009) and Agarwal et al. (2011). As a result, we express the ad position for a keyword k at time t as

$$
\begin{array}{c} \ln (A d P o s _ {k t}) = \gamma_ {0} ^ {k} + \gamma_ {1} ^ {k} \ln (b i d _ {k, t}) + \gamma_ {2} (L Q S c o r e _ {k t}) \\ \qquad + \gamma_ {\text {Time}} T i m e _ {k t} + \varepsilon_ {k t} ^ {\gamma}, \\ \boldsymbol {\gamma} ^ {k} = \Delta^ {\gamma} z _ {k} + u _ {k} ^ {\gamma} \text {and} u _ {k} ^ {\gamma} \sim N (0, V ^ {\gamma}). \end{array}\tag{5}
$$

Note that the position of the advertisement is the daily average position and is a continuous variable. This functional form ensures that the bid and the listed quality score, LQScore, are required to determine the ad position.

## 4.4. Organic Competition

Firms continuously strive to improve their sites to increase their relevance, and thereby improve their position in search results for different keywords. However, they can also do this systematically in response to unobservable time-varying demand patterns. These demand patterns can be different for unique products and the corresponding keywords. For example, a particular product may increase in popularity over time. In that case, the consumer click and conversion behavior for the related keyword would be driven by the increase in the preference for the product. At the same time, firms might improve their organic ranking to respond to this increase in demand. As a result, the organic competition for the focal advertiser would also increase for that keyword. Thus, both consumer response and organic competition would be correlated with the unobservable demand for the keyword and the underlying product. As a consequence, the effect of organic competition on click and conversion performance can be biased.

Because we consider only those competitors’ listings that appear above or at the same level of our focal advertiser, the randomization of bids and the subsequent positions ensures that the competitors’ organic listings are also randomized to a large extent. However for a given ad position, the organic competition is still changing somewhat, and the changes could be correlated with time-varying unobservable demand shocks. We use an IV approach to account for this potential endogeneity bias. For every keyword in our sample, we consider the competing firms in the organic listings and determine the average organic position for each competitor for other nonrelated keywords.<sup>9</sup> These nonrelated keywords refer to nonrelated products that are not likely to share the same consumer valuation as the products associated with the focal keywords.

We use this average organic position for each competitor for a keyword to compute the instrumental variable for its organic competition as follows:

$$
I V _ {k t} = \sum_ {C} \frac {1}{(1 / n _ {k _ {c} ^ {\prime}}) \sum_ {k _ {c} ^ {\prime}} P o s _ {k _ {c} ^ {\prime} t}},
$$

where $P o s _ { k _ { c } ^ { \prime } t }$ is the organic position for a nonrelated keyword $k _ { c } ^ { \prime }$ at time t of the competitor C associated with keyword $k ,$ and $n _ { k _ { c } ^ { \prime } }$ is the number of nonrelated keywords for competitor C.

Our IV exploits the notion that the kinds of website changes that lead to improvements in one section of a website also contribute to improvements in other sections of the website; that is, better organic placement for one section of the website through such website improvements will be correlated to improvements in organic placements for another section, even if these sections offer very different products with very different demand patterns. As a result, we would expect correlations between the positions of the organic listing of nonrelated keywords while expecting consumer valuations for these keywords to be largely independent. We use the website hierarchy of our advertiser (Figure 2) to determine the nonrelated keywords for each of our sample keywords. Keywords are associated with different products in the website hierarchy. For each sample keyword, we pick keywords that are associated with nonrelated products from a different part of the website hierarchy. For a keyword related to a particular type of pet, we consider nonrelated keywords as keywords that are associated with a different pet. For example, “cat food” is not related to “dog food” or “dog food rolls.” However, it is related to “canned cat food” and “raw cat food.” This approach allows us to pick keywords that are less likely to be correlated in consumer valuations.

Note that the consumer valuation can be correlated if the firm has the same promotions across multiple products. However, this is more likely to be the case for related products. By selecting the position of nonrelated keywords, we minimize the impact of such correlation. This is similar to the approach adopted by Hausman (1996), Nevo (2001), and, more recently, Ghose et al. (2012) to use prices of the product in other markets as an instrument. As explained below, we also validate the strength and the exogeneity of our instrument and verify our results with two alternative instruments.

Using this approach, organic competition can be specified as a function of the IV variable as follows:

$$
\begin{array}{c} O r g a n i c \_ C o m p _ {k t} = \alpha_ {0} ^ {k} + \alpha_ {1} ^ {k} I V O r g a n i c _ {k t} \\ \qquad + \alpha_ {\text {Time}} T i m e _ {k t} + \varepsilon_ {k t} ^ {\alpha}, \\ \boldsymbol {\alpha} ^ {k} = \Delta^ {\alpha} z _ {k} + u _ {k} ^ {\alpha} \text {and} u _ {k} ^ {\alpha} \sim N (0, V ^ {\alpha}), \end{array}\tag{6}
$$

where $I V O r g a n i c _ { k t }$ is the instrument described above.

Finally, because the position of the advertisement as well as organic competition are endogenous, the unobservable time varying keyword attributes for the equations representing consumer decisions will be correlated with error terms for the equations representing position and organic competition. As such, we use the following distribution to account for correlation between the error terms:

$$
\left[ \begin{array}{c} \varepsilon_ {k t} ^ {\beta} \\ \varepsilon_ {k t} ^ {\theta} \\ \varepsilon_ {k t} ^ {\gamma} \\ \varepsilon_ {k t} ^ {\alpha} \end{array} \right] \sim N (0, \Omega), \quad \text {where} \Omega = \left[ \begin{array}{c c c c} \Omega_ {1 1} & \Omega_ {1 2} & \Omega_ {1 3} & \Omega_ {1 4} \\ \Omega_ {2 1} & \Omega_ {2 2} & \Omega_ {2 3} & \Omega_ {2 4} \\ \Omega_ {3 1} & \Omega_ {3 2} & \Omega_ {3 3} & \Omega_ {3 4} \\ \Omega_ {4 1} & \Omega_ {4 2} & \Omega_ {4 3} & \Omega_ {4 4} \end{array} \right].\tag{7}
$$

## 4.5. Identification

The above set of simultaneous equations represent a triangular system, which has been addressed by authors in classical (Lahiri and Schmidt 1978, Hausman 1975, Greene 1999) and Bayesian econometrics (Zellner 1962). It can be represented as follows:

$$
\begin{array}{c} U _ {k t} ^ {C T R} = f (A d P o s i t i o n, O r g a n i c C o m p e t i t i o n, X _ {1}, \varepsilon_ {k t} ^ {\theta}), \\ U _ {k t} ^ {C O N V} = f (A d P o s i t i o n, O r g a n i c C o m p e t i t i o n, X _ {2}, \varepsilon_ {k t} ^ {\beta}), \\ A d P o s i t i o n = f (X _ {3}, \varepsilon_ {k t} ^ {\gamma}), \\ O r g a n i c C o m p e t i t i o n = f (X _ {4}, \varepsilon_ {k t} ^ {\alpha}). \end{array}
$$

In this setup, Ad Position (AdPos) and Organic Competition (Organic\_Comp) are endogenous, whereas the variables $X _ { 1 } { - } X _ { 4 }$ are exogenous. Identification arises from the fact that position is determined by the exogenous variables: bid and LQScore. As noted above, the bid for each keyword is randomized (exogenous) in our setup, and LQScore is a value internally calculated by the search engine for each keyword, and remains stable for the short period of our experiment, unless the advertisers change their ads or landing pages to influence the quality score. Similarly, organic competition is completely determined by the instrumental variable, which is not correlated with the error term. Position and organic competition in turn influence click and conversion performance.

Thus, the rank and order conditions are satisfied for identification purposes (Greene 1999). Lahiri and Schmidt (1978) showed that the parameter estimates for a triangular system can be fully identified using generalized least squares. Hausman (1975) showed that the likelihood function for a triangular system is the same as for seemingly unrelated regressions. Zellner (1962) addressed triangular systems from a Bayesian point of view and showed that the posterior probability distribution function is the same as in a seemingly unrelated regressions setting. Triangular systems have been estimated using the classical approach (Elberse and Eliashberg 2003, Godes and Mayzlin 2004), and more recently in sponsored search using the Bayesian approach (Ghose and Yang 2009, Yang and Ghose 2010, Agarwal et al. 2011).

We estimate the model using a Bayesian approach, applying Markov Chain Monte Carlo (MCMC) sampling because of the nonlinear characteristics of our model (Rossi and Allenby 2005). A more detailed discussion of the priors and conditional posteriors of this model is given in Online Appendix A (available as supplemental material at http://dx.doi.org/10.1287/ isre.2015.0593). For the HB models, we run the MCMC simulation for 80,000 draws and discard the first 40,000 as burn-in. To ensure that our parameter estimates are accurate, we simulate the clicks, orders, ad position, and organic competition using our estimates. By repeating the estimation with this simulated data set, we were able to recover our parameter estimates, indicating that our parameters are fully identified.

We performed an F -test in the first stage for our instruments. In each case, the F -test value was well over 10, suggesting our instruments are not weak. To explore the quality of our instruments further, we explored the orthogonality of the instruments by inspecting the plots of the marginal posterior distributions for $\begin{array} { r } { Z _ { k t } \varepsilon _ { k a t } ^ { \theta } } \end{array}$ and $Z _ { k t } \varepsilon _ { k a t } ^ { \beta } ,$ as suggested by Duan and Mela (2009) and Musalem et al. (2008). We compute the 95% posterior predictive interval to assess whether it excludes zero as a test for rejecting orthogonality. We find that all of the intervals contain zero, which suggests that the error term is not correlated with the instrument.

4.5.1. Models with Alternative Measures of Competition. We also consider two other measures of organic and sponsored competition. For a keyword at time t, we consider the total number of competitors listings appearing at the same level or above the focal advertiser normalized by their position, as follows:

$$
C o m p e t i t i o n _ {k t} = \sum_ {C _ {k t}} \frac {1}{P o s _ {C _ {k t}}},
$$

where $P o s _ { C _ { k t } }$ is the position of the listing of competitor $C$ for keyword k at time t. This is a simpler measure of competition to ensure that our use of AlexaRank is not affecting our results.

We also use another measure of competition where we consider the sum of listings of each type appearing at the same level or above the focal advertiser normalized by their Alexa rank as follows:

$$
\text { Competition } _ {k t} = \sum_ {C _ {k t}} \frac {\log (\text { AlexaRank })}{\log (\text { AlexaRank } _ {C _ {k t}})},
$$

where AlexaRan $\tau _ { C _ { k t } }$ is the Alexa rank of the listing of competitor C for keyword k at time t.

## 5. Results

## 5.1. Click-Through Rate

Table 4 provides the mean values for the posterior distribution of the $\Delta ^ { \theta }$ matrix and the covariance matrix $V ^ { \theta }$ from Equation (2). The coefficient for organic competition (Organic\_Comp) is significant and negative for all models. This suggests that consumers clicking on our advertiser’s ads are negatively influenced by the organic results and are less likely to click in the presence of higher organic competition. This empirically validates the assumption made in the literature about the negative impact of organic results on sponsored search performance (Katona and Sarvary 2010). Our results show that competitors’ organic listings may act as substitutes, not complements, as suggested by Danescu-Niculescu-Mizil et al. (2010). The presence of higher organic competition may lower attention to sponsored search and, as a result, lead to a decrease in click performance. This also suggests that even if consumers may learn about the quality of the ad based on the higher level of competition, it does not help the click performance of ads.

The coefficient for ad position (AdPos) is negative and significant, indicating that click performance decays with position. This is similar to the findings in the extant literature (Ghose and Yang 2009, Yang and Ghose 2010) and shows that CTR decays with the position of the ad.

The coefficient for sponsored competition (Sponsored\_Comp) is not significant. This suggests that after controlling for position, sponsored competition does not impact the performance of ads. Some of the impact of sponsored competition is already captured in ad position. Any additional information that is conveyed by a variation in attributes such as the perceived quality of the sponsored competition (or their relative position) does not impose any externality on the click performance. Note that we use the same parameters to define both organic and sponsored competition. This suggests that organic competition has a higher impact on click performance than does sponsored competition. It is possible that position captures some effect of the number of sponsored competitors, and that is why we do not see an effect. We separately verify the relative impact of organic and sponsored competition in the robustness analysis without controlling for the effect of ad position. Our result also appears to contradict the observation made by Jeziorski and Segal (2015) where they show that higher sponsored competition decreases the click performance even after controlling for the effect of position. A key difference is that they use the expected click performance of competing ads for the keyword to measure the strength of competition, whereas we rely on relative position and the overall perceived quality of the competitors’ sponsored listings to determine this value. Thus, our results suggest that consumers place more attention on these attributes of relative position and perceived quality for organic results than they do for sponsored results.

Table 4 Estimates for the CTR

<table><tr><td></td><td>Cumulative competition normalized by position and Alexa rank</td><td>Cumulative competition normalized by position</td><td>Cumulative competition normalized by Alexa rank</td></tr><tr><td>Const</td><td>-4.22 (0.55)***</td><td>-4.35 (0.63)***</td><td>-4.84 (0.32)***</td></tr><tr><td>AdPos</td><td>-1.42 (0.18)***</td><td>-1.67 (0.16)***</td><td>-1.06 (0.21)***</td></tr><tr><td>Organic_Comp</td><td>-0.41 (0.15)***</td><td>-0.27 (0.14)**</td><td>-0.23 (0.11)**</td></tr><tr><td>Sponsored_Comp</td><td>-0.17 (0.12)</td><td>-0.01 (0.15)</td><td>-0.08 (0.08)</td></tr><tr><td>Organic</td><td>-0.2 (0.2)</td><td>-0.16 (0.1)</td><td>-0.2 (0.17)</td></tr><tr><td>LQScore</td><td>0.3 (0.06)***</td><td>0.32 (0.05)***</td><td>0.34 (0.03)***</td></tr><tr><td>Time</td><td>-0.01 (0.0)***</td><td>-0.011 (0.002)***</td><td>-0.013 (0.002)***</td></tr><tr><td>Brand</td><td>0.25 (0.51)</td><td>-0.17 (0.47)</td><td>0.24 (0.39)</td></tr><tr><td>Specificity</td><td>-0.51 (0.65)</td><td>-0.45 (0.66)</td><td>0.35 (0.64)</td></tr><tr><td>Organic_Comp × Brand</td><td>-0.09 (0.36)</td><td>0.14 (0.31)</td><td>0.02 (0.23)</td></tr><tr><td>Sponsored_Comp × Brand</td><td>-0.01 (0.29)</td><td>0.12 (0.27)</td><td>-0.05 (0.19)</td></tr><tr><td>Organic_Comp × Specificity</td><td>0.64 (0.42)</td><td>0.69 (0.37)*</td><td>0.13 (0.28)</td></tr><tr><td>Sponsored_Comp × Specificity</td><td>0.55 (0.37)</td><td>0.42 (0.36)</td><td>0.08 (0.24)</td></tr></table>

<sup>∗</sup>Statistically significant at 10%; <sup>∗∗</sup>statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

The coefficient for Organic is insignificant. This is potentially because very few keywords in our sample have the advertiser’s own listing in the organic search result. Additionally, the organic listing of the advertiser is always below the sponsored ad, and it is possible that consumers are not paying attention to the organic listing. The coefficient of LQScore is positive and significant, indicating that keywords with a higher LQScore have higher CTRs than other keywords. This is consistent with expectations because LQScore accounts for factors such as ad quality.

Finally, brand and keyword specificity have no significant impact on the click performance of keywords. The interaction of brand and specificity with organic competition or sponsored competition is also not significant. This suggests that the observed effects of organic and sponsored competition on CTR performance do not vary with keyword characteristics such as brand and specificity.

## 5.2. Conversion Rate

Table 5 provides the mean values for the posterior distribution of the ã<sup></sup> matrix and the covariance matrix V <sup></sup> in Equation (4). The coefficient for Organic\_Comp is significant and positive, implying that the conversion rate improves with organic competition. Any variation in the brand and specificity of keywords does not change this outcome.<sup>10</sup>

It is interesting to note that even though CTR decreases with organic competition, consumers who make it to our advertiser’s website by clicking on the ad are more likely to buy in the presence of higher organic competition. In Table 1, we outlined two potential explanations for this observation. The first is awareness and learning effects. Consumers become aware of the relevance of the sponsored ads due to high organic competition. They can learn from the competition and update their quality perception of the advertiser (Athey and Ellison 2011). This may be particularly important in sponsored search because consumers are known to have a negative bias against sponsored search results (Jansen and Resnick 2006), and therefore the presence of high quality organic competition may lead the buyers to trust the sponsored ads more.

Another potential explanation for the increase in conversion rate with organic competition is the recency effect. It is well known that the sequence of evaluation impacts a consumer’s purchase decision through primacy (Pieters and Bijmolt 1997) and recency effects (Wedel and Pieters 2000). An increase in organic competition may imply that consumers who do visit our advertiser’s website tend to do so toward the end of their search. Having evaluated several promising alternatives, they may be buying from the most recently evaluated option. To determine if recency bias also plays a role in conversion, we estimate our model with an interaction term between organic competition and the ad position. A recency effect, if present, should lead to a higher effect of organic competition at lower ad positions because consumers are more likely to evaluate the focal advertiser toward the end when it appears in the lower position. However, our results show that the interaction term has no effect (Table 6). This suggests that the increase in conversion performance is unlikely to be driven by the recency effect, and thus awareness and learning effects may be more relevant in our setting than recency effects are. Combined with the CTR results, we conclude that competing organic results lead to fewer consumers visiting the sponsored search advertiser’s website, but that consumers who do visit the website are more likely to purchase the product because of their evaluation of competitors’ organic listings. Our results also show that learning effects are indeed higher for buying consumers compared to consumers seeking information, and as a result lead to an opposite effect of competition on the click and conversion performance.

Table 5 Estimates for the CONV

<table><tr><td></td><td>Cumulative competition normalized by position and Alexa rank</td><td>Cumulative competition normalized by position</td><td>Cumulative competition normalized by Alexa rank</td></tr><tr><td>Const</td><td>-2.75 (0.68)***</td><td>-3.58 (0.53)***</td><td>-2.73 (0.44)***</td></tr><tr><td>AdPos</td><td>0.81 (0.28)***</td><td>0.54 (0.21)***</td><td>0.35 (0.26)</td></tr><tr><td>Organic_Comp</td><td>0.7 (0.18)***</td><td>0.62 (0.19)***</td><td>0.29 (0.12)**</td></tr><tr><td>Sponsored_Comp</td><td>-0.27 (0.17)</td><td>0.23 (0.15)</td><td>0.08 (0.09)</td></tr><tr><td>Organic</td><td>0.17 (0.25)</td><td>0.3 (0.2)</td><td>0.11 (0.2)</td></tr><tr><td>LQScore</td><td>-0.01 (0.06)</td><td>-0.12 (0.05)**</td><td>-0.02 (0.04)</td></tr><tr><td>Time</td><td>-0.01 (0.0)**</td><td>-0.001 (0.004)</td><td>-0.008 (0.002)***</td></tr><tr><td>Brand</td><td>-0.77 (0.58)</td><td>1.41 (0.52)***</td><td>0.95 (0.48)**</td></tr><tr><td>Specificity</td><td>-0.25 (1.01)</td><td>3.62 (0.82)***</td><td>2.09 (0.64)***</td></tr><tr><td>Organic_Comp × Brand</td><td>1.27 (0.42)***</td><td>0.43 (0.41)</td><td>0.3 (0.27)</td></tr><tr><td>Sponsored_Comp × Brand</td><td>-0.31 (0.39)</td><td>-0.32 (0.44)</td><td>-0.11 (0.23)</td></tr><tr><td>Organic_Comp × Specificity</td><td>0.52 (0.49)</td><td>0.04 (0.47)</td><td>-0.12 (0.35)</td></tr><tr><td>Sponsored_Comp × Specificity</td><td>0.58 (0.45)</td><td>-0.48 (0.38)</td><td>-0.18 (0.26)</td></tr></table>

<sup>∗∗</sup>Statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

Table 6 Effect of Organic Competition at Different Ad Positions

<table><tr><td></td><td colspan="2">CTR</td><td colspan="2">CONV</td></tr><tr><td>Const</td><td>-3.62</td><td>(0.57)***</td><td>-1.84</td><td>(0.88)**</td></tr><tr><td>AdPos</td><td>-1.21</td><td>(0.2)***</td><td>0.63</td><td>(0.22)***</td></tr><tr><td>Organic_Comp</td><td>-0.29</td><td>(0.15)**</td><td>0.74</td><td>(0.2)***</td></tr><tr><td>Sponsored_Comp</td><td>-0.11</td><td>(0.13)</td><td>-0.01</td><td>(0.26)</td></tr><tr><td>Organic</td><td>-0.04</td><td>(0.03)</td><td>0.06</td><td>(0.03)*</td></tr><tr><td>LQScore</td><td>0.239</td><td>(0.044)***</td><td>-0.374</td><td>(0.079)***</td></tr><tr><td>Time</td><td>-0.012</td><td>(0.004)***</td><td>-0.031</td><td>(0.003)***</td></tr><tr><td>Brand</td><td>-0.52</td><td>(0.56)</td><td>0.29</td><td>(0.64)</td></tr><tr><td>Specificity</td><td>-0.13</td><td>(0.72)</td><td>3.56</td><td>(0.81)***</td></tr><tr><td>Organic_Comp × Brand</td><td>-0.02</td><td>(0.35)</td><td>0.77</td><td>(0.49)</td></tr><tr><td>Sponsored_Comp × Brand</td><td>-0.07</td><td>(0.31)</td><td>0.03</td><td>(0.41)</td></tr><tr><td>Organic_Comp × Specificity</td><td>0.35</td><td>(0.44)</td><td>-0.19</td><td>(0.54)</td></tr><tr><td>Sponsored_Comp × Specificity</td><td>-0.02</td><td>(0.36)</td><td>0.16</td><td>(0.46)</td></tr><tr><td>AdPos × Organic_Comp</td><td>-0.05</td><td>(0.32)</td><td>-0.42</td><td>(0.32)</td></tr></table>

<sup>∗</sup>Statistically significant at 10%; <sup>∗∗</sup>statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

The coefficient for AdPos is positive and significant, indicating that, on average, conversion rate increases with position. This result is similar to the finding by Agarwal et al. (2011) and suggests that users visiting lower positions are more likely to buy than users visiting the top position. Note that this holds for only the top few positions, which is the case for our data set (which only contains the top 10 positions).

The coefficient for sponsored competition is not significant. This suggests that after controlling for ad position, buyers may not be influenced by the presence of higher sponsored competition. This is similar to the finding for CTR.

## 5.3. Ad Position and Organic Competition

Table 7 provides the mean values for the posterior distribution of the ã<sup></sup> matrix and V <sup></sup> from Equation (5).

In these results, higher bids lead to a higher current position (lower value of position). This is reasonable because bid is one of the primary inputs used to compute ad position, and higher values of bids should move the ad higher in the list of returned results. The coefficient for LQScore is negative and significant. Thus, a higher LQScore also leads to a higher current position. This is expected because a higher LQScore for a keyword should help the ad be placed higher in the sponsored results. Table 8 provides the mean values for the posterior distribution of the ã<sup></sup> matrix and V <sup></sup> from Equation (6). As expected, the coefficient for the instrument for organic competition is positive and significant.

Finally, Table 9 shows the covariance between unobservables for CTR, CONV, ad position, and organic competition from Equation (7). Covariance between the unobservables for CONV and CTR is statistically significant. This indicates that the unknown factors influencing consumer clicks also influence subsequent conversion behavior. The covariance between the unobservables for CTR or CONV and organic competition is also statistically significant. Because error terms for CTR and CONV are also correlated, this suggests that the unobservables influencing Organic\_Comp are affecting both CTR and CONV. Similarly, the covariance between the unobservables for Organic\_Comp and AdPos are statistically significant. This suggests that the unobservables influencing position are also influencing CTR and CONV, meaning that position and Organic\_Comp are endogenous and the proposed simultaneous equation model helps to capture the effect of this endogeneity.

We have taken several steps to evaluate the robustness of these results. Because of space constraints, detailed descriptions for the related models along with the estimates are given in Online Appendix B.

Table 7 Estimates for the Ad Position

<table><tr><td></td><td>Cumulative competition normalized by position and Alexa rank</td><td>Cumulative competition normalized by position</td><td>Cumulative competition normalized by Alexa rank</td></tr><tr><td>Const</td><td>1.03 (0.16)***</td><td>1.01 (0.17)***</td><td>0.99 (0.16)***</td></tr><tr><td>Log (Bid)</td><td>-0.45 (0.08)***</td><td>-0.45 (0.08)***</td><td>-0.45 (0.08)***</td></tr><tr><td>LQScore</td><td>-0.049 (0.01)***</td><td>-0.048 (0.02)***</td><td>-0.045 (0.01)***</td></tr><tr><td>Time</td><td>-0.002 (0.0)***</td><td>-0.12 (0.05)**</td><td>-0.002 (0.0)***</td></tr></table>

<sup>∗∗</sup>Statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

Table 8 Estimates for the Organic Competition

<table><tr><td></td><td>Cumulative competition normalized by position and Alexa rank</td><td>Cumulative competition normalized by position</td><td>Cumulative competition normalized by Alexa rank</td></tr><tr><td>Const</td><td>0.07 (0.17)</td><td>0.17 (0.16)</td><td>0.49 (0.38)</td></tr><tr><td>Organic_Comp IV</td><td>1.86 (0.21)***</td><td>1.63 (0.17)***</td><td>4.36 (0.49)***</td></tr><tr><td>Time</td><td>-0.004 (0.0)***</td><td>-0.005 (0.0)***</td><td>-0.006 (0.0)***</td></tr></table>

<sup>∗∗∗</sup>Statistically significant at 1%.

Figure 3 Impact of Organic Competition on Ad Performance  
![](/api/attachments/265M4QYC/fulltext/images/a1c606fdf477b5388b371633e216820c6185a05f59df479fc3d23e56701cca1c.jpg)

5.4. Revenue as a Function of Organic Competition To determine the overall effect of organic competition on revenue, we calculate revenue using the posterior distribution of the CTR and CONV coefficients for each keyword (assuming a \$10 average value of the associated products). We find that revenue increases with organic competition. Figure 3 shows clicks and orders as a function of organic competition for the average ad position for a keyword in our sample. A potential explanation for increases in revenue with increased competition is that buyers clicking the advertiser listing end up buying from the advertiser much more in the presence of higher organic competition. This can counter the negative effect of fewer consumers visiting the ad in the presence of higher organic competition.

## 5.5. Impact of Organic Competition on Keyword

Performance Prediction and Keyword Selection Our results suggest that click performance and revenue associated with keywords are influenced by organic competition. Using the additional organic competition information, advertisers can more accurately predict the performance of keywords. For illustration, we estimate the parameters of our main model both with and without organic competition using the first four weeks of our panel data as the estimation sample. We use the remaining two weeks as the holdout period and use these parameter estimates to predict the clicks and orders for the holdout period. We compare these predicted values with the actual values in the holdout sample. We find that the use of organic competition reduces the prediction error by 9% for clicks and 5% for orders.

Additionally, advertisers can prioritize the most suitable keywords by allocating appropriate budgets and thereby improve their profitability using the organic competition information. For illustration, we estimate the profitability of the portfolio of our sample keywords with and without the use of organic competition information. The estimated profit for a keyword can be expressed as

$$
\pi = I \times (C T R \times C O N V \times R P O - C T R \times C P C),
$$

where I is the expected number of ad impressions; CTR is the click-through rate, or the fraction of ad impressions that generate clicks; CONV is the conversion rate per click, or the fraction of clicks that generate orders; RPO is the revenue per order; and CPC is the average cost per click charged to an advertiser.

We use the relationship between the search engine position and the advertiser’s bid (Equation (5)) to determine the cost. For a given bid and position $j ,$ we assume that the actual cost per click is the bid for position j + 1. We use the posterior distribution of the parameter estimates for CONV and CTR and the position equations to compute profits for each keyword with and without the organic competition information. Because the position of the advertisement as well as the competition for each keyword keeps changing, we use the average position as well as the average competition for each keyword to predict the expected profit for that keyword. Figure C1 in Online Appendix C shows the change in CTR, CONV, and profitability of our sample keywords with and without incorporating organic competition information. Then we allocate the budget across these keywords by weighing each keyword by its relative profitability under the two scenarios of estimating profitability with and without organic competition information.<sup>11</sup> We compare the performance of the advertiser portfolio based on the budget allocation decision with and without organic competition.<sup>12</sup> We find that for all of our sample keywords, the advertiser can improve the performance by 6% by making budget choices using organic competition information.

Table 9 Estimates for the Covariance Matrix ì

<table><tr><td></td><td>CONV</td><td>CTR</td><td>Pos</td><td>Organic_Comp</td></tr><tr><td colspan="5">Cumulative competition normalized by position and Alexa rank</td></tr><tr><td>CONV</td><td>0.37 (0.06)***</td><td>-0.036 (0.015)**</td><td>0.00 (0.009)</td><td>-0.005 (0.014)</td></tr><tr><td>CTR</td><td></td><td>0.232 (0.02)***</td><td>0.007 (0.008)</td><td>0.02 (0.008)**</td></tr><tr><td>Pos</td><td></td><td></td><td>0.064 (0.003)***</td><td>-0.005 (0.002)**</td></tr><tr><td>Organic_Comp</td><td></td><td></td><td></td><td>0.087 (0.004)***</td></tr><tr><td colspan="5">Cumulative competition normalized by position</td></tr><tr><td>CONV</td><td>0.477 (0.036)***</td><td>-0.035 (0.017)**</td><td>-0.007 (0.012)</td><td>0.004 (0.02)</td></tr><tr><td>CTR</td><td></td><td>0.259 (0.018)***</td><td>0.009 (0.007)</td><td>0.023 (0.01)**</td></tr><tr><td>Pos</td><td></td><td></td><td>0.064 (0.003)***</td><td>-0.007 (0.002)***</td></tr><tr><td>Organic_Comp</td><td></td><td></td><td></td><td>0.087 (0.004)***</td></tr><tr><td colspan="5">Cumulative competition normalized by Alexa rank</td></tr><tr><td>CONV</td><td>0.403 (0.031)***</td><td>-0.092 (0.016)***</td><td>-0.009 (0.008)</td><td>-0.071 (0.027)***</td></tr><tr><td>CTR</td><td></td><td>0.224 (0.019)***</td><td>0.004 (0.006)</td><td>0.06 (0.035)*</td></tr><tr><td>Pos</td><td></td><td></td><td>0.064 (0.003)***</td><td>0.056 (0.006)***</td></tr><tr><td>Organic_Comp</td><td></td><td></td><td></td><td>0.588 (0.024)***</td></tr></table>

<sup>∗</sup>Statistically significant at 10%; <sup>∗∗</sup>statistically significant at 5%; <sup>∗∗∗</sup>statistically significant at 1%.

## 6. Discussion and Conclusion

In our research, we analyze how competing organic results affect the performance of sponsored search advertisements. Although we know that consumers pay a lot of attention to organic results, very little has been formally established on the impact of organic competition on sponsored search performance. Ours is the first research we are aware of to systematically investigate the impact of competition in organic results on sponsored search performance.

To do this, we use a unique data set derived from a field experiment with an online retailer’s advertising campaign on Google. In this experiment, we systematically (and exogenously) vary the advertiser’s bid to drive variation in the organic results of direct competitors likely to compete with an advertiser’s sponsored ad for consumers’ attention. We also use a Web crawler to capture the search results from competitors returned by these keywords. We analyze our data using a hierarchical Bayesian model and accounting for the endogeneity of ad position and organic competition. We also control for the effect of sponsored competition.

Our results show that increased organic competition leads to a decrease in the CTR of our retailer’s ads appearing on the right-hand side. However, these changes may help the conversion rate of the retailer’s ads. Furthermore, we find that sponsored competition has no impact on conversion performance, and has a less negative impact on click-through performance as compared to the organic competition.

Our study provides key managerial insights for advertisers. Many websites do not appear in organic results, or appear only for a few keywords, and rely heavily on sponsored search to advertise their products. Competitors can improve their organic ranking by investing in search engine optimization to make their pages more relevant for search results. Given that branding is driven primarily by clicks (Rutz and Bucklin 2012), whereas transactional revenues are driven by conversions, advertisers interested only in branding may want to focus on keywords with lower organic competition. Conversion performance, however, can be helped by higher organic competition for the top page results. Thus, advertisers should consider different responses to competition, depending on the objective of their advertising campaign. Advertisers focus a lot on sponsored search competition, and our results show that they can improve sponsored search performance by also analyzing organic competition. For example, we find that our focal advertiser can improve the profitability of the sample keywords by 6% by considering the impact of organic competition in estimating the performance of keywords and allocating the budgets accordingly.

Our findings also have implications for search engines. Our results suggest that advertisers will get fewer clicks for their ads if the ads are shown in the presence of strong organic competition. However, advertisers are also likely to get higher revenue in the presence of strong organic competition. Thus, advertisers with a branding objective may have a lower valuation for keywords with high organic competition, whereas those with a conversion objective might value such keywords. In that case, search engines should suggest appropriate keywords to the advertisers based on the advertiser objectives. This would ensure lower mismatch between advertisers and keywords and would increase advertiser participation and, in turn, increase the search engine revenue. Furthermore, search engines should recognize that conversion performance may not mirror click performance, and thus CTRs alone may not be sufficient as performance measures for ads.

Finally, our results inform the academic literature regarding the effect of competition in sponsored search environments in several ways. First, we show that organic competition has a greater impact on ad performance than sponsored competition. Furthermore, CTR is negatively influenced by an increase in organic competition, whereas conversion rate is positively influenced by this increase. Thus, prior findings that show a complementary effect of an advertiser’s own organic listing applies to the competing organic listings as well for conversions but not for clicks. Second, our results suggest that existing bid optimization approaches should also consider the role of organic competition in evaluating advertiser performance. Much of the prior literature on bid optimization has ignored the impact of organic listings.

As with any empirical analysis, there are several limitations of our study. Our results explain some information search behavior of consumers at an aggregate level, but the aggregate nature of our data limits our ability to account for the actions of individual consumers. This calls for future research using click-stream data to empirically evaluate the behavior of different types of consumers in sponsored search environments.

Additionally, our analysis of orders is based on measurements conducted by the SEM firm employed by the advertiser, wherein consumer action is tracked during the entire search session. This potentially underreports sales resulting from an advertisement, because consumers may click on an advertisement and visit the advertiser’s landing page without converting, but return later (even using a different search engine query) to then buy the product. In these instances, the future purchases are not properly attributed to the original keyword. Furthermore, we restrict our analysis to keywords where advertisers chose to display ads with an “exact” match. Future studies should validate these results for ads with a “broad” or “phrase” match. We also note that our results are based on the analysis of field experiment data from a single retailer. Future studies should validate the results for other types of products and retailers.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0593.

## Acknowledgments

The authors would like to thank the senior editor, associate editor, and the anonymous reviewers for their constructive comments and suggestions.

## References

Abhishek V, Hosanagar K (2013) Optimal bidding in multi-item multi-slot sponsored search auctions. Oper. Res. 61(4):855–873.

Agarwal A, Hosanagar K, Smith MD (2011) Location, location and location: An analysis of profitability of position in online advertising markets. J. Marketing Res. 48(6):1057–1073.

Animesh A, Ramachandran V, Viswanathan S (2010) Quality uncertainty and adverse selection in online sponsored search markets. Inform. Systems Res. 21(1):190–201.

Animesh A, Viswanathan S, Agarwal R (2011) Competing creatively in sponsored search markets. Inform. Systems Res. 22(1):153–169.

Ansari A, Mela C (2003) E-customization. J. Marketing Res. 40(2): 131–145.

Athey S, Ellison G (2011) Position auctions with consumer search. Quart. J. Econom. 126(3):1213–1270.

Brunel FF, Nelson MR (2003) Message order effects and gender differences in advertising persuasion. J. Advertising Res. 43(3): 330–341.

Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of Internet and conventional retailers. Management Sci. 46(4):563–585.

Chakravarti A, Janiszewski C, Ulkumen G (2006) The neglect of pre-screening information. J. Marketing Res. 63(11):642–653.

Danescu-Niculescu-Mizil C, Broder AZ, Gabrilovich E, Josifovski V, Pang B (2010) Competing for users’ attention: On the interplay between organic and sponsored search results. Proc. 19th Internat. Conf. World Wide Web, 291–300.

Dellaert BGC, Haubl G (2012) Searching in choice mode: Consumer decision processes in product search with recommendations. J. Marketing Res. 49(2):277–288.

Dellarocas C (2012) Double marginalization in performance-based advertising: Implications and solutions. Management Sci. 58(6): 1178–1195.

Duan JA, Mela C (2009) The role of spatial demand on outlet location and pricing. J. Marketing Res. 46(2):260–278.

Ebbes P, Wedel M, Böckenholt U, Steerneman T (2005) Solving and testing for regressor-error (in)dependence when no instrumental variables are available: With new evidence for the effect of education on income. Quant. Marketing Econom. 3(4):365–392.

Edelman B, Ostrovsky M, Schwarz M (2007) Internet advertising and the generalized second-price auction: Selling billions of dollars worth of keywords. Amer. Econom. Rev. 97(1):242–259.

Elberse A, Eliashberg J (2003) Demand and supply dynamics for sequentially released products in international markets: The case of motion pictures. Marketing Sci. 22(3):329–354

Feldman J, Muthukrishnan S, Pal M, Stein C (2007) Budget optimization in search-based advertising auctions. Proc. 8th ACM Conf. Electronic Commerce, San Diego, 40–49.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Ghose A, Ipeirotis PG, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Godes D, Mayzlin D (2004) Using online conversations to study word of mouth communication. Marketing Sci. 23(4):545–560.

Granka LA, Joachims T, Gay G (2004) Eye-tracking analysis of user behavior in WWW search. Proc. 27th Annual Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval, Sheffield, UK, 478–479.

Greene W (1999) Econometric Analysis, 4th ed. (Prentice Hall, Upper Saddle River, NJ).

Häubl G, Benedict GCD, Bas D (2010) Tunnel vision: Local behavioral influences on consumer decisions in product search. Marketing Sci. 29(3):438–455.

Hausman J (1975) An instrumental variable approach to full information estimators for linear and certain nonlinear econometric models. Econometrica 43(4):727–738.

Hausman J (1996) Valuation of new goods under perfect and imperfect competition. Bresnahan T, Gordon R, eds. The Economics of New Goods, Studies in Income and Wealth, Vol. 58 (National Bureau of Economic Research, Chicago), 209–248.

Hoque AY, Lohse GL (1999) An information search cost perspective for designing interfaces for electronic commerce. J. Marketing Res. 36(3):387–394.

Hosanagar K, Cherapanov V (2008) Optimal bidding in stochastic budget constrained slot auctions. Proc. 9th ACM Conf. Electronic Commerce, Chicago, 20.

Jansen BJ, Resnick M (2006) An examination of searchers’ perceptions of nonsponsored and sponsored links during ecommerce Web searching. J. Amer. Soc. Inform. Sci. Tech. 57(14):1949–1961.

Jeziorski P, Segal I (2015) What makes them click: Empirical analysis of consumer demand for search advertising. Amer. Econom. J. 7(3):24-53.

Katona Z, Sarvary M (2010) The race for sponsored links: Bidding patterns for search advertising. Marketing Sci. 29(2):199–215.

Kempe D, Mahdian M (2008) A cascade model for externalities in sponsored search. Papadimitriou C, Zhang S, eds. Internet and Network Economics, Lecture Notes Comput. Sci., Vol. 5385 (Springer-Verlag, Berlin Heidelberg), 585–596.

Kent RJ (1993) Competitive versus noncompetitive clutter in television advertising. J. Advertising Res. 33(2):40–46.

Kent RJ, Allen CT (1994) Competitive interference effects in consumer memory for advertising: The role of brand familiarity. J. Marketing 58(3):97–105.

Lahiri K, Schmidt P (1978) On the estimation of triangular structural systems. Econometrica 46(5):1217–1221.

Leong S, Mishra N, Sadikov E, Zhang L (2012) Domain bias in Web search. Proc. Fifth ACM Internat. Conf. Web Search and Data Mining, 413–422.

Liu D, Viswanathan S (2014) Information asymmetry and hybrid advertising. J. Marketing Res. 51(5):609–624.

Liu D, Chen J, Whinston AB (2010) Ex-ante information and design of keyword auctions. Inform. Systems Res. 21(1):133–153.

Liu Q, Steenburgh TJ, Gupta S (2015) The cross attributes flexible substitution logit: Uncovering category expansion and share impacts of marketing instruments. Marketing Sci. 34(1): 144–159.

Lunden I (2014) Internet ad spend to reach \$121B in 2014, 23% of \$537B total ad spend, ad tech boosts display. Techcrunch (April 7), http://techcrunch.com/2014/04/07/internet-ad-spend -to-reach-121b-in-2014-23-of-537b-total-ad-spend-ad-tech-gives -display-a-boost-over-search/.

Moe WW (2003) Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. J. Consumer Psych. 13(1–2):29–40.

Musalem A, Bradlow ET, Raju JS (2008) Who’s got the coupon: Estimating consumer preferences and coupon usage from aggregate information. J. Marketing Res. 45(12):715–730.

Nevo A (2001) Measuring market power in the ready-to-eat cereal industry. Econometrica 69(2):307–342.

Palmer JW (2002) Web site usability, design, and performance metrics. Inform. Systems Res. 13(2):150–167.

Park JW, Hastak M (1994) Memory-based product judgments: Effects of involvement at encoding and retrieval. J. Consumer Res. 21(3):534–547.

Pieters RGM, Bijmolt THA (1997) Consumer memory for television advertising: A field study of duration, serial position, and competition effects. J. Consumer Res. 23(4):362–373.

Rhodes EW, Teferman NB, Cook E, Schwartz D (1979) T-scope tests of yellow pages advertising. J. Advertising Res. 19(2):49–52.

Rossi PE, Allenby GM (2003) Bayesian statistics and marketing. Marketing Sci. 22(3):304–328.

Rossi PE, Allenby GM (2005) Bayesian Statistics and Marketing (John Wiley and Sons, Hoboken, NJ).

Rutz O, Bucklin R (2012) From generic to branded: A model of spillovers in paid search advertising. J. Marketing Res. 48(1): 87–102.

Rutz O, Trusov M (2011) Zooming in on paid search ads—A consumer-level model calibrated on aggregated data. Marketing Sci. 30(5):789–800.

Rutz O, Bucklin R, Sonnier GP (2012) A latent instrumental variables approach to modeling keyword conversion in paid search advertising. J. Marketing Res. 49(3):306–319.

Sahni N (2015) Advertising spillovers: Field-experiment evidence and implications for returns from advertising. Stanford University Graduate School of Business Research Paper 14-15, Stanford, CA.

Sherman C (2005) A new f-word for Google search results. Search Engine Watch (March 7), http://searchenginewatch.com/sew/ news/2066806/a-new-f-word-google-search-results.

Weber TA, Zheng ZE (2007) A model of search intermediaries and paid referrals. Inform. Systems Res. 18(4):414–436.

Wedel M, Pieters R (2000) Eye fixations on advertisements and memory for brands: A model and findings. Marketing Sci. 19(4):297–312.

Wood SL, Lynch JG Jr (2002) Prior knowledge and complacency in new product learning. J. Consumer Res. 29(3):416–426.

Wyer RS, Srull TK (1986) Human cognition in its social context. Psych. Rev. 93(3):322–359.

Xu L, Chen J, Whinston AB (2011) Price competition and endogenous valuation in search advertising. J. Marketing Res. 48(3):566–586.

Xu L, Chen J, Whinston AB (2012) Interplay between organic listing and sponsored bidding in search advertising. Inform. Systems Res. 23(4):1284–1302.

Yang S, Ghose A (2010) Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Sci. 29(4):602–623.

Zellner A (1962) An efficient method of estimating seemingly unrelated regressions and tests for aggregation bias. J. Amer. Statist. Assoc. 57(298):348–368.

Zhang X, Feng J (2011) Cyclical bid adjustments in search-engine advertising. Management Sci. 57(9):1703–1719.
