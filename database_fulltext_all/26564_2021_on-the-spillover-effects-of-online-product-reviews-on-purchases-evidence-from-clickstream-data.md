---
otero_id: 26564
otero_key: "SSGCSW9H"
title: "On the Spillover Effects of Online Product Reviews on Purchases: Evidence from Clickstream Data"
authors: "Young Kwark; Gene Moo Lee; Paul A. Pavlou; Liangfei Qiu"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0998"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Spillover Effects of Online Product Reviews on Purchases: Evidence from Clickstream Data

Young Kwark,<sup>a</sup> Gene Moo Lee,<sup>b</sup> Paul A. Pavlou,<sup>c</sup> Liangfei Qiu<sup>a</sup>

<sup>a</sup> Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>b</sup> Sauder School of Business, University of British Columbia, Vancouver, British Columbia V6T 1Z2, Canada; <sup>c</sup>C. T. Bauer College of Business, University of Houston, Houston, Texas 77204

Contact: young.kwark@warrington.u<sup>fl</sup>.edu, https://orcid.org/0000-0002-5574-1717 (YK); gene.lee@sauder.ubc.ca, https://orcid.org/0000-0003-0657-6898 (GML); pavlou@bauer.uh.edu, https://orcid.org/0000-0002-8830-5727 (PAP); liangfei.qiu@ warrington.u<sup>fl</sup>.edu, https://orcid.org/0000-0002-8771-9389 (LQ)

Received: May 31, 2017<sub>Revised:</sub> May 17, 2018; October Accepted: Published Online in Articles in Advance: May 14, 2021

https://doi.org/10.1287/isre.2021.0998

Copyright:

Abstract. We study the spillover effects of the online reviews of other covisited products on the purchases of a focal product using clickstream data from a large retailer. The proposed spillover effects are moderated by (a) whether the related (covisited) products are complementary or substitutive, (b) the choice of media channel (mobile or personal computer (PC)) used, (c) whether the related products are from the same or a different brand, (d) consumer experience, and (e) the variance of the review ratings. To identify complementary and substitutive products, we develop supervised machine-learning models based on product characteristics, such as product category and brand, and novel text-based similarity measures. We train and validate the machine-learning models using product pair labels from Amazon Mechanical Turk. Our results show that the mean rating of substitutive (complementary) products has a negative (positive) effect on purchasing of the focal product. Interestingly, the magnitude of the spillover effects of the mean ratings of covisited (substitutive and complementary) products is signi<sup>fi</sup>cantly larger than the effects on the focal product, especially for complementary products. The spillover effect of ratings is stronger for consumers who use mobile devices versus PCs. We <sup>fi</sup>nd the negative effect of the mean ratings of substitutive products across different brands on purchasing of a focal product to be signi<sup>fi</sup>cantly higher than within the same brand. Lastly, the effect of the mean ratings is stronger for less experienced consumers and for ratings with lower variance. We discuss implications on leveraging the spillover effect of the online product reviews of related products to encourage online purchases.

History: Xiaoquan (Michael) Zhang, Senior Editor; Jungpil Hahn, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0998.

Keywords: online product reviews substitutive products complementary products brand spillover WOM spillover topic modeling machine learning

## 1. Introduction

The surge of electronic commerce has given rise to usergenerated product information or “word-of-mouth” (WOM) communication in the form of online product reviews, which received much attention from academics and practitioners alike. There is a rich body of literature on the effect of online product reviews on aggregate product sales (demand) (e.g., Chevalier and Mayzlin 2006). This is because consumers often rely on online product reviews written by other consumers to reduce product uncertainty (e.g., Dimoka et al. 2012), and the effect of online product reviews on a focal product’s sales has been well documented in the literature (e.g., Chevalier and Mayzlin 2006, Zhu and Zhang 2010, Hu et al. 2017).

Although the process in which a consumer considers a number of related products on the same shopping trip, called “market basket choice,” is well established in the literature (e.g., Manchanda et al. 1999, Russell and Petersen 2000), the literature on online product reviews has ignored that, when consumers search for products, they do not only consider the online reviews of the focal product of interest, but they also consider the online reviews of other related products. Despite the well-known effects of related products on the purchase of a focal product (e.g., Shocker et al. 2004), to our knowledge, there is lack of research on the spillover<sup>1</sup> effects of online product reviews of other related products on a consumer’s purchasing of a focal product.<sup>2</sup> Because of the association among products that are viewed together in a consumer’s consideration set (market basket), we examine how the consumer’s purchasing decision is in<sup>fl</sup>uenced by the online reviews of other related, covisited products using clickstream data.<sup>3</sup>

The literature has viewed online product reviews as an in<sup>fl</sup>uential signal for inferring product quality (e.g., Aggarwal et al. 2012, Ho-Dac et al. 2013, Luo et al. 2017). However, the signaling role of mean ratings across related products has not been explored. In this paper, we study the spillover effect of online reviews on sales based on (a) whether the related (covisited) products are complementary or substitutive, (b) the choice of media channel (mobile or personal computer (PC)) used, (c) whether the related products are from the same or a different brand, (d) consumer experience, and (e) review variance. Although spillover effects across products (e.g., advertising spillovers) have attracted attention (e.g., Libai et al. 2009, Anderson and Simester 2013, Peres and Van den Bulte 2014, Lewis and Nguyen 2015), including WOM communication (e.g., Parker and Gatignon 1994, Libai et al. 2009, Krishnan et al. 2012), to our knowledge, the spillover effect of online product reviews among related products on purchases has not been examined. Extending the literature on online reviews, we examine the spillover role of online reviews of related products in a consumer’s consideration set (market basket), which are covisited during a consumer’s online session, in the purchase of a focal product. We extend the works on the average aggregated effect of online reviews on the sales of competing products (Jabr and Zheng 2014) and on perceptions among substitutive products (Luo et al. 2017) by showing the spillover role of online product reviews of substitutive and complementary products.

We aim at answering two research questions. (1) How do the online product reviews of other related products in a consumer’s consideration set affect purchasing of a focal product? (2) How do (a) the association among products (i.e., complementary or substitutive), (b) media channel, (c) brand, (d) consumer experience, and (e) review variance moderate the role of the ratings of related products in the purchase of a focal product?

To classify related (complementary and substitutive) product pairs among tens of thousands of products in hundreds of thousands of individual user sessions, we build supervised machine-learning models based on product characteristics (e.g., brand match and category match) and novel text-based similarity measures (e.g., product name similarity and functional similarity). To quantify the functional similarity of pairwise products, we use topic modeling on the focal product descriptions. To train and validate our machine-learning models, we use product pair labels (e.g., substitutive, complementary, and unrelated) from Amazon Mechanical Turk (AMT). We conduct extensive crossvalidation tests with various product features and similarity measures and different classi<sup>fi</sup>cation algorithms. Crossvalidation evaluation results show that the model can achieve up to 99.64%, 95.75%, and 98.99% in predicting substitutive, complementary, and unrelated products, respectively.

Using the instrumental variable (IV) estimation approach and the economic de<sup>fi</sup>nition of price elasticity, we further con<sup>fi</sup>rm the validity of our proposed measures for effectively categorizing complementary and substitutive products.

Our results show a signi<sup>fi</sup>cant negative spillover of online product reviews for substitutive products and a signi<sup>fi</sup>cant positive spillover effect for complementary products in the purchase of a focal product. Notably, the magnitude of the spillover effects of related products is larger than that of the focal product. Interestingly, we <sup>fi</sup>nd a signi<sup>fi</sup>cantly higher spillover effect of the mean rating of online reviews viewed on mobile devices compared with PCs. We also <sup>fi</sup>nd a signi<sup>fi</sup>cantly higher negative spillover effect of online product reviews for substitutive products from different brands than those of the same brands, whereas we do not <sup>fi</sup>nd signi<sup>fi</sup>cant brand differences in the positive spillover effect for complementary products. Finally, the spillover role of the mean ratings is stronger among less experienced consumers and for the ratings that have a lower variance.

Our study also has managerial implications for online review strategies. The effect of online reviews cannot be determined in isolation as consumer purchasing decisions are interrelated across products. Our results call for an in-depth analysis of the spillover effects of reviews across covisited products and understanding of crossproduct linkages. Also, the spillover effects are stronger within the same brand, which emphasizes the bene<sup>fi</sup>t of deploying same-brand products in one’s consideration. It is also noteworthy for marketers that less experienced consumers rely more on online product reviews. Finally, the stronger spillover effect on mobile devices (versus PCs) casts light on strategies across media channels, encouraging managers to leverage the consumers’ narrow attention when using mobile devices for the presentation of mean ratings.

## 2. Literature Review

Our work aims to contribute to the literature on online reviews. There has been extensive research on the effect of online product reviews, a common form of user-generated content, on the sales of a focal product (e.g., Clemons et al. 2006, Forman et al. 2008, Archak et al. 2011, Goes et al. 2014).<sup>4</sup> Studies, in general, have shown various effects of online product reviews (Godes and Mayzlin 2004, Chevalier and Mayzlin 2006, Dellarocas et al. 2007). It was shown that the effect of online product reviews exists because consumers rely on them to reduce product uncertainty (e.g., Dimoka et al. 2012, Hong and Pavlou 2014). Finally, sellers strategically respond to online product reviews (e.g., Chen and Xie 2005, 2008; Dellarocas 2006; Kwark et al. 2014), and marketers consider online product reviews to be another important component of their overall marketing mix (e.g., Chen and Xie 2005, 2008; Godes and Mayzlin 2009; Libai et al. 2013). Studies also discuss <sup>fi</sup>rm strategies stimulating (Luca and Zervas 2016, Burtch et al. 2018, Khern-am-nuai et al. 2018) and responding to (Ho et al. 2017, Liu et al. 2017, Li 2018, Feng et al. 2019) online reviews.

There is a rich body of literature on the effect of online product reviews on aggregate sales (demand). Several characteristics of online product reviews were shown to be in<sup>fl</sup>uential on sales: rating valence (e.g., Chevalier and Mayzlin 2006, Clemons et al. 2006, Duan et al. 2008), volume of ratings (e.g., Liu 2006), variance (Clemons et al. 2006), text reviews (Archak et al. 2011), reviewer identity (Forman et al. 2008), and product and consumer characteristics (Zhu and Zhang 2010). Further, recent research has examined the role of characteristics of online reviews and product type in review helpfulness (Mudambi and Schuff 2010), negative emotions embedded in online product reviews on review helpfulness (Yin et al. 2014), how online product reviews reduce product uncertainty (Hong and Pavlou 2014), interactions of online product reviews with promotional marketing (Lu et al. 2013) and product recommendations (Jabr and Zheng 2014, Lee and Hosanagar 2016), herding behavior in online product reviews (Duan et al. 2009, Lee et al. 2015), and potential bias formed in the generation of online product reviews (Li and Hitt 2008, Hu et al. 2017) plus other factors that were shown to affect the posting, generation, development, and potential biases of online product reviews (e.g., Dellarocas et al. 2010, Zhu and Zhang 2010, Rice 2012, Goes et al. 2014, Gao et al. 2015).

Studies consider online reviews as a signal (e.g., Aggarwal et al. 2012, Ho-Dac et al. 2013, Luo et al. 2017). In contrast to <sup>fi</sup>rm-sponsored signals (e.g., advertising), online reviews can be viewed as credible signals of product quality, showing a signi<sup>fi</sup>cant effect on consumers’ purchase decisions (e.g., Ho-Dac et al. 2013). The valence (mean rating) of online product reviews is regarded as an in<sup>fl</sup>uential predictor of product sales (e.g., Dellarocas et al. 2007, Chintagunta et al. 2010). We also focus on the mean rating of online reviews, which denotes the overall evaluation score of a product. Studies mostly <sup>fi</sup>nd that the higher the mean rating of online reviews, the more positive the consumer attitudes are toward the product, which leads to higher sales (e.g., Chevalier and Mayzlin 2006, Clemons et al. 2006, Duan et al. 2008, Zhu and Zhang 2010, Lu et al. 2013).

Notably, there are two closely related papers to our study: First, Jabr and Zheng (2014) de<sup>fi</sup>ned a competing product using the retailer’s recommendation feature and showed a positive effect of the online reviews of competing books on the sales rank of books. Extending this study that focused on the average effect of online reviews on aggregate sales (overall demand), we examine the role of online reviews in an individual consumer’s purchasing decision. We extend the analysis to complementary products. Our clickstream data allow us to specify an individual consumer’s consideration set to analyze the role of the reviews of the products in her consideration set in her purchase decision. Second, Luo et al. (2017) found a negative relationship between a brand’s expert blogs and consumer perceptions of competing brands. Their <sup>fi</sup>ndings showed the effect of blog opinions on consumers’ perceptions of the brands of substitutive products. We extend the literature by examining the role of online reviews for the same and different brands of both substitutive and complementary products on consumer purchases. Lastly, we show a set of key moderating factors that reinforce or attenuate the effect of the mean ratings on purchases, namely media channel, brand, consumer experience, and review variance. Overall, we extend the literature by examining the spillover role of online reviews of related (substitutive and complementary) products in an individual consumer’s purchase of a focal product and the reinforcing or attenuating factors on the spillover effect. It is important to explore the effects of online reviews across related products because consumers often use the star ratings of the related products as contextual information to interpret the average star rating of the focal product (e.g., Tversky and Simonson 1993). The behavioral economics literature (e.g., Tversky and Kahneman 1991) argues that people tend to focus on the difference from the contextual reference points and judge related aspects in a relative way. Figure 1 illustrates the underlying mechanism suggested in this paper for justifying the proposed role of online reviews in forming the purchase intention of the focal product.

The spillover effect of online product reviews is found from the demand substitution/complement effect and the crossproduct rating effect; the former can be explained by a chain of effects (1) and (2), whereas the latter by the reference point effect associated with effects (3) and (4). For example, in the context of substitutive products, the former explains that as the ratings of the related products increase, the purchase intention for them increases (rating effect), and thus, the purchase intention for the focal product decreases (demand effect). For the latter, the ratings of the related products can be used as contextual information to interpret the rating of the focal product. To illustrate, suppose a focal product has a four-star average rating. The purchase intention for the product will be higher (lower) when its substitutive product has three (four) stars.

Figure 1. (Color online) Illustration of the Focal and Spillover Effects of Online Product Ratings  
![](/api/attachments/SSGCSW9H/fulltext/images/a122833e097b6a012c6bdbb502812b7bd14bd3493d2f4fd0af320ed418ace87e.jpg)

A few marketing studies show the existence of advertising spillovers (Anderson and Simester 2013), brand scandals (Roehm and Tybout 2006), and product recalls (Borah and Tellis 2016). WOM spillover among consumers is shown on WOM externalities (Peres and Van den Bulte 2014), new product diffusion (e.g., Libai et al. 2009), seeded marketing campaigns (Chae et al. 2016), marketing communications (Ahluwalia et al. 2001), and product growth (Krishnan et al. 2012). We extend these studies by examining the effect of mean ratings across related (substitutive and complementary) products while <sup>fi</sup>nding a large set of moderators (i.e., brand, media channel, consumer experience, and review variance).

## 3. Theory and Hypotheses

First, the role of the mean rating of online product reviews of substitutive and complementary products in the purchase of the focal product is discussed (Hypotheses 1a and 1b). Second, the different role of the rating of online product reviews in the purchase of the focal product depending on the media channel (PC or mobile device) is hypothesized (Hypotheses 2a and 2b). Third, the role of the mean rating of online reviews of substitutive and complementary products of the same versus different brands, in the purchase of the focal product, is hypothesized (Hypotheses 3a and 3b). Finally, we hypothesize the roles of consumer experience (Hypothesis 4) and the variance of review ratings (Hypothesis 5) for substitutive and complementary products in the purchase of a focal product.

## 3.1. Complementary/Substitutive Products and Product Purchases

Prior studies have viewed consumer-generated reviews as signals of product quality (e.g., Aggarwal et al. 2012, Ho-Dac et al. 2013, Luo et al. 2017). Rather than traditional marketing signals sent by companies, such as advertising and product warranties, consumers generally consider reviews as more credible signals of product quality, which in turn, in<sup>fl</sup>uence their purchase decisions. It is natural that a consumer considers many products to <sup>fi</sup>nd a product with the highest utility for her by reading reviews from other consumers. Information search and evaluation of product alternatives are considered key processes for purchase decisions (e.g., Blackwell et al. 2001). When consumers search for information on products, signals about related products can in<sup>fl</sup>uence the relative perception of product quality for the focal product of interest.

Substitutes are products that a consumer perceives as similar or comparable and may replace each other. Complements are products that the coexistence of other products is affected by their purpose and exhibit a reinforcing effect on each other (Shocker et al. 2004). In the economics literature, products are substitutes if demand for a product increases when the price of another increases (i.e., positive crosselasticity of demand). Products are complements if the demand for a product decreases when the price of another product increases (Mas-Colell et al. 1995). A negative (positive) relationship in demand changes among substitutive (complementary) products has been found. Marketing activities, such as promotions, for one product negatively (positively) can affect other substitutive (complementary) products (e.g., Mulhern and Leone 1991, Walters 1991, Chintagunta and Haldar 1998, Manchanda et al. 1999, Kamakura and Kang 2007).

The mean rating of product reviews is shown to positively affect product demand. For substitutive products, however, this effect may be the opposite. Because a higher mean rating implies a better product evaluation and signals a higher product quality, the relative attractiveness of substitutive products may be undermined, thus shifting the preference against the focal substitutive product (Luo et al. 2017). On the other hand, a highly rated product can increase the needs of its complementary products as they bene<sup>fi</sup>t from joint consumption. Promoting a product, therefore, leads to higher (lower) sales of complementary (substitutive) products (e.g., Mulhern and Leone 1991, Walters 1991).

In sum, given the positive association between the mean rating of online reviews and product demand plus the negative (positive) relationship of substitutive (complementary) products in a consumer’s purchase decision, we expect the negative (positive) role of the mean rating of online reviews of substitutive (complementary) products on the focal product purchase. Thus, we hypothesize:

Hypothesis 1a. The mean review ratings of substitutive products have a negative role in the purchase of a focal product.

Hypothesis 1b. The mean review ratings of complementary products have a positive role in the purchase of a focal product.

## 3.2. The Moderating Role of Media Channel

Extending Hypotheses 1a and 1b, we posit that the signaling role of the mean rating of online product reviews on mobile devices can be larger than that on PCs. The effect of signals is affected by the consumer’s attention and the visibility and clarity of the signal (Connelly et al. 2011). Mobile devices are popular for online shopping; still, their limited functionalities, small screen size, and high search costs (e.g., Ghose et al. 2013, Burtch and Hong 2014) reduce the overall amount of information that consumers can access, thus limiting learning effectiveness (Maniar et al. 2008). People often consider only a subset of salient signals, especially when they cannot easily process multiple signals. Hence, consumers tend to make purchasing decisions by focusing on the quantitative features of online reviews (e.g., mean review ratings) rather than scrutinizing all available signals (e.g., review text) (Maslowska et al. 2017). A user interface on small mobile screens makes it dif<sup>fi</sup>cult for consumers to locate information, thus leading to higher ranking effects (e.g., links that appear at the top of the screen are more likely to be clicked on mobile phones than PCs) because more cognitive effort is required for information processing (e.g., Nunamaker et al. 1987, Ghose et al. 2013). Therefore, mobile users should rely more on the mean rating compared with PC users, making the role of the mean rating more in<sup>fl</sup>uential on mobile devices compared with traditional PCs.

In a similar vein, practitioners <sup>fi</sup>nd that mobile advertising becomes powerful with a lack of clutter on the page and the proportionally larger advertising units to the screen because of the easy retrieval of signals (Butcher 2010). In addition, mobile users are more likely to be on the move or multitasking, which may pressure them to examine less information for decision making (e.g., Svenson et al. 1985, Entin et al. 1990). This pressure narrows the consumers’ focus and makes them rely on a few signals on mobile devices as their primary information source (Ariely 2016). Thanks to this effect, mobile campaigns were up to <sup>fi</sup>ve times more effective than comparable PC campaigns in shifting brand awareness, attitudes, and purchase intentions (Butcher 2010). Mobile advertising also shows a strong positive effect on consumer attitudes and behaviors (e.g., Barwise and Strong 2002, Tsang et al. 2004, Drossos et al. 2007, Bart et al. 2014, Luo et al. 2014). Overall, we expect the role of product review ratings to be more salient to mobile consumers because consumers with less capacity for information processing tend to rely more on the mean rating as a key signal. In sum, we expect that when consumers view a product on a mobile device, the effect of the online ratings will be stronger. Therefore, when a consumer searches on a mobile device versus a PC, the spillover role of the mean rating of online product reviews in her purchasing decision will be stronger. We thus hypothesize:

Hypothesis 2a. The mean review ratings of substitutive products have a stronger negative role in the focal product purchase of consumers of mobile devices than of PCs.

Hypothesis 2b. The mean review ratings of complementary products have a stronger positive role in the focal product purchase of consumers of mobile devices than of PCs.

## 3.3. The Moderating Role of Brand

A brand is de<sup>fi</sup>ned as a name, term, sign, symbol, or design, which is intended to identify the goods/services of one seller and to differentiate them from those of competitors (Kotler 1997, p. 443). A brand is a signal because it symbolizes a <sup>fi</sup>rm’s past and present marketing strategies. Brands can be strong and effective signals of product quality, and the signals can be transferred within products of the same brand (e.g., Wernerfelt 1988, Aaker 1991, Erdem and Swait 1998). In general, studies show that consumers’ product quality perceptions are negatively correlated across brands and positively correlated within the same brand (e.g., Erdem 1998, Seetharaman et al. 2005). For instance, the blog opinion of a focal brand has a negative effect on consumer perceptions of the competing brands because it may undermine consumer perceptions of competing brands (Luo et al. 2017, Song et al. 2019). Promotions of one brand can increase its own sales at the expense of competing brands (e.g., Dodson et al. 1978, Kumar and Leone 1988, Mulhern and Leone 1991, Walters 1991). With favorable reviews of a brand, consumers’ preference over the focal brand is enhanced (Aggarwal et al. 2012). The substitutive nature of competing products can accelerate the customer’s propensity to select the superior product among substitutive products, further shifting the preference against competing brands. The negative signaling effect among substitutive products can be weaker within the same brand because of the reciprocal effect on each other among same-branded products. The effect of advertising can be positive among products of the same brand, further increasing the sales of unadvertised products of the same brands (e.g., Aaker 1996). Therefore, we expect the negative spillover role of the mean review rating of substitutive products on the purchase of a focal product to be more salient across different brands than within the same brand.

The positive relationship among complementary products has been shown (e.g., Walters 1991, Chintagunta and Haldar 1998, Manchanda et al. 1999). Because of the reciprocal nature in consumer needs, complementary products are promoted jointly, and retailers often offer a group of products as a bundle (e.g., Guiltinan 1987, Eppen et al. 1991, Gaeth et al. 1991). Brand signals can further enhance this positive effect among same-brand products. However, the strength of the complementarity among products can vary. Studies have shown that complementary products across brands may work as substitutes to each other (e.g., Mulhern and Leone 1991, Walters 1991, Seetharaman et al. 2005, Kamakura and Kang 2007). Although complementary products generally exhibit choice dependence within a market basket, the lack of a bond among products across different brands may reduce their complementarity. Thus, the additional needs created by the signal from online reviews can be weaker across different brands. In contrast, when complementary products belong to the same brand, we expect a stronger positive effect of the mean review rating because of the quality signal’s transfer within the same brand. Studies <sup>fi</sup>nd product quality perceptions to be correlated when products belong to the same brand (e.g., Erdem 1998, Erdem and Winer 1999, Seetharaman et al. 2005). Within the same brand, the positive effect of promotion exists across the sales of complementary products (e.g., Mulhern and Leone 1991, Walters 1991, Kamakura and Kang 2007) because it is easier to adopt products by reducing product uncertainty when products belong to the same brand (Erdem 1998, Erdem and Sun 2002). Information about a product acts as diagnostic signals in a consumer’s purchasing decision for other products of the same brand because they reinforce the meaning of brand (Aaker 1991, Keller 1993) and spill over from one product to another within the same brand (e.g., Aaker 1996, Balachander and Ghose 2003). In sum, we expect the positive spillover role of the mean review rating among complementary products to act as a stronger signal of product quality within the same brand versus across different brands. We thus propose:

Hypothesis 3a. The negative role of the mean review ratings of substitutive products in the purchase of the focal product is larger among different brands than within the same brand with the focal product.

Hypothesis 3b. The positive role of the mean review ratings of complementary products in the purchase of the focal product is larger within the same brand than across different brands with the focal product.

## 3.4. The Moderating Role of Consumer Experience

Consumers read online product reviews to reduce uncertainty (e.g., product quality not being as promised). Consumers who face higher uncertainty because of lack of prior knowledge and experience rely more on signals to infer product quality (Archak et al. 2011, Ho-Dac et al. 2013). That is, higher uncertainty raises the effect of signals. Less experienced consumers are likely to perceive higher uncertainty and thus, rely more on signals from online reviews (e.g., Archak et al. 2011, Kwark et al. 2014). Studies on job recruiting have shown that the signaling effect is greater when job seekers know less about the organizations (Rynes et al. 1991). Similarly, we argue that the effect of the mean rating should be higher for consumers with little knowledge resulting from their limited experience. Accordingly, we theorize that for less experienced consumers, the negative (positive) signaling effect of the mean rating of online reviews of substitutive (complementary) products on the purchase of a focal product should be stronger. We thus propose:

Hypothesis 4. The mean review ratings of (a) substitutive and (b) complementary products have a stronger (a) negative and (b) positive role in a focal product purchase among less experienced consumers.

## 3.5. The Moderating Role of the Variance of Review Ratings

Although online reviews are considered a credible source of product quality, the signaling effect of the mean ratings should be more effective when the ratings are more consistent. In the literature, signal consistency, the degree to which each brand signal re<sup>fl</sup>ects the intended whole, refers to the stability with low variation of brand signals over time and across elements of the marketing mix (Erdem and Swait 1998). That is, when brand signals are consistent across strategies over time, a stronger brand image can be built. Studies <sup>fi</sup>nd that consensus among critics’ reviews reduces evaluation uncertainty of product quality, increasing the effect over consumer perceptions (e.g., Basuroy et al. 2006). In the context of online reviews, as the variance of ratings increases, the heterogeneity of quality perceptions increases. We posit that this heterogeneity, re<sup>fl</sup>ected as a variance of ratings, attenuates the effect of the mean ratings as a signal. Thus, as ratings have a greater variance, the negative (positive) role of the mean rating of online reviews of substitutive (complementary) products on the purchase of the focal product should be stronger. We therefore propose:

Hypothesis 5. The mean review ratings of (a) substitutive and (b) complementary products have a stronger (a) negative and (b) positive role in a focal product purchase when the mean ratings have lower variance.

## 4. Method

## 4.1. Clickstream Data

Our data set was provided by a large UK online retailer. The clickstream data provide complete website visits (including product page views, reviews views, and purchases) from individual consumers, giving us an opportunity to analyze how the online product reviews (of both focal and related products) affect customer’s purchase behavior at the individual level. The data set is divided into two partitions based on two product categories: home/garden and technology. Table 1 provides a description of the two data sets.

First, the home/garden data contain information on 97,852 unique consumers browsing product descriptions and reviews of 25,662 products in 229,577 web sessions in a two-month period. A consumer can visit multiple product pages in a shopping session (an online session expires after 30 minutes of inactivity), and there are 493,928 product-session observations. Second, the technology data include records on 60,695 consumers accessing 7,393 product pages in 118,051 sessions. There are 202,454 product-sessions. To capture purchases across products (e.g., market basket), we identi<sup>fi</sup>ed covisited products within a single session. For home/garden products, on average, a consumer accessed 2.15 products in a session, and each session lasted about an hour. For technology products, on average, consumers spent less time (25 minutes) and checked 1.71 products in a session. A signi<sup>fi</sup>cant fraction of sessions (43% in home/garden and 34% in technology) involved multiple products. This empirically motivates our study to examine the spillover effects of online reviews among covisited products. A consumer’s product covisiting behavior can be driven by many means: (i) browsing products in retailer-curated product category pages (55.9%), (ii) searching related products using the in-site search engine (25.7%), and (iii) reaching the page of a related product through the recommendation link on the focal product page (13.5%). Consumers can also reach a speci<sup>fi</sup>c product page from other channels, such as the retailer’s home page (2.1%), promotion pages (1.4%), or special offers (0.5%). If a consumer visits only one product in a shopping session, the mean rating of its related products would be a missing value, and these sessions were dropped from the sample.

Table 1. Clickstream Data Description

<table><tr><td>Variables</td><td>Home/garden</td><td>Technology</td></tr><tr><td># of consumers</td><td>97,852</td><td>60,695</td></tr><tr><td># of products</td><td>25,662</td><td>7,393</td></tr><tr><td># of sessions</td><td>229,577</td><td>118,051</td></tr><tr><td># of product-session pairs</td><td>493,928</td><td>202,454</td></tr><tr><td># of sessions with multiple products</td><td>100,675 (43.85%)</td><td>40,572 (34.37%)</td></tr><tr><td>Avg. session duration (minutes)</td><td>57.57</td><td>25.37</td></tr><tr><td># of products per session (min)</td><td>1</td><td>1</td></tr><tr><td># of products per session (max)</td><td>213</td><td>72</td></tr><tr><td># of products per session (average)</td><td>2.151</td><td>1.715</td></tr><tr><td># of products per session (standard deviation)</td><td>2.362</td><td>1.525</td></tr></table>

## 4.2. Machine Learning-Based Identi<sup>fi</sup>cation of Substitutive and Complementary Products

Our study aims to estimate the spillover effects of review ratings of substitute and complementary products. Thus, a key issue is the identi<sup>fi</sup>cation of the product relationship (e.g., substitutive, complementary, or unrelated). Given the massive scale of the data, we need to develop a scalable approach to classify a pair of products into a substitutive, complementary, or unrelated relationship. As proposed in related literature (e.g., Lee et al. 2020, Shin et al. 2020), we develop a supervised machine-learning approach to address this challenge. First, we collected product relationship classi<sup>fi</sup>cation labels of 16,000 product pairs using AMT. Then, using the label data as the training set, we built supervised machine-learning models using various classi<sup>fi</sup>cation algorithms. We constructed features from the product name, category, brand, textual description, past visit records, and reviews. Extensive crossvalidation experiments show that the trained models can accurately classify substitutive (F-1 scores of 98.86% and 99.64%, respectively), complementary (87.41% and 95.75%), respectively, and unrelated products (98.99% and 97.48%, respectively) for home/garden and technology products. The method was also validated with the economic de<sup>fi</sup>nition of price elasticity (Mas-Colell et al. 1995) (Section 5.5). Lastly, we used the product relationship labels from AMT and predictions in measuring the mean review ratings of substitute or complementary products for a focal product. The detailed procedure is described in Online Appendix B.

## 4.3. Variable Construction

Given the identi<sup>fi</sup>cation of substitutive and complementary product pairs, we constructed relevant variables. The unit of analysis is (user, product, session) triplet. Each variable was constructed from web visits from each individual user session. The dependent variable is purchase, indicating if the user purchased the focal product in the session. The key independent variable is mean rating; the volume of online product reviews was treated as a control variable. We also controlled for the price of the focal product and the other products covisited within the same session. We used a dummy variable, mobile, to control for the device type used in the session. The key variables are described in Table 2, and the full list is given in Online Appendix C.

For the purchase dummy variable, the purchase probabilities were 4.2% and 3.7% for home/garden and technology, respectively. Data show that most rating variables have high averages: The mean ratings of home/ garden and technology products are 4.07 and 4.27, respectively. Skewed distributions are observed from the review volume (vol\_focal): A home/garden product has 76.54 total reviews, on average, with a standard deviation of 162. A product in the technology category has 50.22 reviews, on average, with a 91.81 standard deviation. The most popular home/garden and technology products have 1,829 and 866 reviews, respectively, whereas there are 14,243 home/garden (55.5%) and 3,974 technology (53.8%) products with no reviews, thus no numeric review ratings. We require all products in our analysis to have review ratings and thus, removed those products with no reviews from our sample.<sup>5</sup> In terms of the price data (e.g., price\_focal, price\_subs, price\_comp), we observed that, on average, the technology products (£126.38) were more expensive than the home/garden products (£64.11). There were observations with £0 price tag because of various marketing/ promotion events. The most expensive items cost £999.99 and £2,399.9 in the home/garden and technology categories, respectively. Please note that mobile observations included user activities from tablets (e.g., iPad). We observed more mobile device usage for the home/ garden (35%) than for the technology (28.7%) products. Detailed summary statistics are in Online Appendix C.

Table 2. Primary Variables

<table><tr><td>Variables</td><td>Descriptions</td></tr><tr><td>purchase</td><td>Whether a consumer purchases a product in an online session (unit: 0, 1)</td></tr><tr><td>rating_focal</td><td>Mean rating of focal product (range: 1~5; for all rating variables)</td></tr><tr><td>vol_focal</td><td>Mean volume of focal product reviews (range: 0+)</td></tr><tr><td>vol_subs</td><td>Mean volume of reviews of substitutive products (range: 0+)</td></tr><tr><td>vol_comp</td><td>Mean volume of reviews of complementary products (range: 0+)</td></tr><tr><td>rating_subs</td><td>Mean rating of substitutive products</td></tr><tr><td>rating_comp</td><td>Mean rating of complementary products</td></tr><tr><td>rating_subs_samebrand</td><td>Mean rating of substitutes produced by the same brand</td></tr><tr><td>rating_comp_diffbrand</td><td>Mean rating of complements produced by the same brand</td></tr><tr><td>rating_subs_diffbrand</td><td>Mean rating of substitutes produced by different brands</td></tr><tr><td>rating_comp_diffbrand</td><td>Mean rating of complements produced by different brands</td></tr><tr><td>var_focal_viewed</td><td>Variance of ratings of viewed reviews of focal product at product viewing time</td></tr><tr><td>var_subs_viewed</td><td>Mean of viewed rating variance of substitute products viewed by consumer</td></tr><tr><td>var_comp_viewed</td><td>Mean of viewed rating variance of complementary products viewed by consumer</td></tr><tr><td>price_focal</td><td>Price of focal product (unit: £)</td></tr><tr><td>price_comp</td><td>Mean price of complements of focal product (unit: £)</td></tr><tr><td>price_subs</td><td>Mean price of substitutes of focal product (unit: £)</td></tr><tr><td>sess_count_samecate</td><td>Number of previous online sessions in the same subcategory</td></tr><tr><td>purchases_samecate</td><td>Number of previous purchases in the same subcategory</td></tr><tr><td>mobile</td><td>Whether a mobile device is used in an online session (unit: 0, 1)</td></tr><tr><td>rating_subs_mobile</td><td>rating_subs × mobile</td></tr><tr><td>rating_comp_mobile</td><td>rating_comp × mobile</td></tr><tr><td>days_since_first_dt</td><td>Number of days since focal product was introduced in the retail site</td></tr></table>

## 5. Data Analysis and Empirical Results 5.1. The Spillover Effects of Online Reviews

We summarize our empirical models. First, we focus on the overall effects of the mean review rating of substitutive and complementary products in Equation (1) (Hypotheses 1a and 1b). Second, we examine the moderating role of the channel in Equations (2) and (3) (Hypotheses 2a and 2b). Third, we examine the moderating role of the brand in Equation (4) (Hypotheses 3a and 3b). Then, we investigate consumer uncertainty and review congruence (Hypothesis 4). Finally, we con<sup>fi</sup>rm the validity of our machine learning-based measures of substitutes/ complements and address price endogeneity issues. We conducted several robustness checks to address potential endogeneity concerns in Online Appendix A.

Our benchmark econometric speci<sup>fi</sup>cation is a linear probability model:<sup>6</sup>

$$
\begin{array}{r l} p u r c h a s e _ {i, j, t} = & a _ {i} + v _ {j} + \beta_ {0} + \beta_ {1} r a t i n g \_ f o c a l _ {i, j, t} + \beta_ {2} v o l \_ f o c a l _ {i, j, t} \\ & + \beta_ {3} r a t i n g \_ s u b s _ {i, j, t} + \beta_ {4} r a t i n g \_ c o m p _ {i, j, t} \\ & + \text {time dummies} + \varepsilon_ {i, j, t}, \end{array}\tag{1}
$$

where i represents a consumer, j represents a product page viewed by a consumer in an online session, and t represents an online shopping session. The binary dependent variable, $p u r c h a s e _ { i , j , t } ,$ indicates whether consumer i purchases product j in the session t (purchase: one, not purchase: zero); $a _ { i }$ is the <sup>fi</sup>xed effect of a consumer capturing unobserved individual heterogeneity; $v _ { j }$ is product <sup>fi</sup>xed effect; rating $f o c a l _ { i , j , t }$ is the mean rating of the focal product that consumer i views in the session t, which measures the direct impact of the focal product’s WOM; and vol $\mathrm { \Sigma } _ { f o c a l _ { i , j , t } }$ is the volume of the focal product reviews. We controlled for time dummies including week of a year and day of a week. We are particularly interested in coef<sup>fi</sup>cients rating $\AA _ { - s u b s _ { i , j , t } }$ and $r a t i n g \_ c o m p _ { i , j , t } ,$ which are the mean rating of the substitutes and complements of product $j ,$ respectively. In the estimation, we used robust t statistics to treat unknown heteroskedasticity and cluster correlations in the error terms. In our context, the same consumers are involved in different shopping sessions. Failure to control for within-cluster error correlations could understate true standard errors (e.g., Cameron et al. 2008).

Our <sup>fi</sup>xed effects estimation results for Equation (1) are presented in columns (1) and (3) (home/garden category) of Table 3 and in columns (2) and (4) (technology category) of Table 3. The results show that the coef<sup>fi</sup>cient of rating\_subs is negative and signi<sup>fi</sup>cant, whereas the coef<sup>fi</sup>cient of rating\_comp is positive and signi<sup>fi</sup>cant. These <sup>fi</sup>ndings suggest that the mean rating of substitutes (complements) has a negative (positive) role in the purchase probability of the focal product. In sum, these <sup>fi</sup>ndings support Hypotheses 1a and 1b, respectively. Other than statistical signi<sup>fi</sup>cance, we also looked at the practical signi<sup>fi</sup>cance of the coef<sup>fi</sup>cients. For instance, in column (3) of Table 3, the coef<sup>fi</sup>cient on rating\_comp is 0.00385, which means that if rating\_comp increases by one, the focal product purchase probability will increase by 0.385%. At <sup>fi</sup>rst glance, the magnitude seems modest. However, the average purchase probability is only 4.2% in the home/garden data. Therefore, if rating\_comp increases by one, on average, the purchase probability of a focal product will increase from 4.2% to 4.585% (4.2%

Table 3. The Spillover Effects of Online Product Reviews

<table><tr><td>Variables</td><td>(1) Fixed effects Home</td><td>(2) Fixed effects Technology</td><td>(3) Fixed effects Home</td><td>(4) Fixed effects Technology</td><td>(5) Brand effects Home</td><td>(6) Brand effects Technology</td></tr><tr><td>rating_focal</td><td>0.000867* [1.893]</td><td>0.000200 [0.278]</td><td>0.000796* [1.723]</td><td>0.000478 [0.657]</td><td>0.00199** [2.297]</td><td>0.00103 [0.886]</td></tr><tr><td>vol_focal</td><td>2.38e-05*** [9.619]</td><td>2.84e-05*** [4.387]</td><td>2.75e-05*** [8.594]</td><td>2.92e-05*** [3.018]</td><td>1.07e-05*** [3.889]</td><td>2.08e-05*** [2.834]</td></tr><tr><td>rating_subs</td><td>-0.00579*** [-14.18]</td><td>-0.00364*** [-5.799]</td><td>-0.00607*** [-14.16]</td><td>-0.00355*** [-5.482]</td><td></td><td></td></tr><tr><td>rating_comp</td><td></td><td></td><td>0.00385*** [5.820]</td><td>0.00222** [2.176]</td><td></td><td></td></tr><tr><td>vol_subs</td><td></td><td></td><td>1.33e-05** [2.390]</td><td>5.05e-06 [0.356]</td><td></td><td></td></tr><tr><td>vol_comp</td><td></td><td></td><td>-3.77e-07 [-0.0342]</td><td>-7.55e-06 [-0.408]</td><td></td><td></td></tr><tr><td>rating_subs_samebrand</td><td></td><td></td><td></td><td></td><td>-0.000806** [-2.089]</td><td>-0.000629* [-1.819]</td></tr><tr><td>rating_comp_samebrand</td><td></td><td></td><td></td><td></td><td>0.00423*** [2.973]</td><td>0.00443*** [3.226]</td></tr><tr><td>rating_subs_diffbrand</td><td></td><td></td><td></td><td></td><td>-0.00655*** [-11.60]</td><td>-0.00297*** [-3.861]</td></tr><tr><td>rating_comp_diffbrand</td><td></td><td></td><td></td><td></td><td>0.00306*** [3.919]</td><td>0.000376 [0.297]</td></tr><tr><td>price focal</td><td></td><td></td><td></td><td></td><td>-5.95e-05*** [-3.777]</td><td>-2.39e-05* [-1.900]</td></tr><tr><td>price_subs</td><td></td><td></td><td></td><td></td><td>-0.000142*** [-7.060]</td><td>-4.64e-05*** [-2.836]</td></tr><tr><td>price_comp</td><td></td><td></td><td></td><td></td><td>-1.56e-05 [-0.489]</td><td>-3.04e-05 [-1.462]</td></tr><tr><td>Observations</td><td>370,466</td><td>169,102</td><td>21,159</td><td>17,254</td><td>21,159</td><td>17,254</td></tr><tr><td>R2</td><td>0.138</td><td>0.0145</td><td>0.167</td><td>0.0994</td><td>0.227</td><td>0.132</td></tr></table>

Note. Cluster robust t statistics are in brackets.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

0.385%), which represents a 9.2% (0.385/4.2) increase in purchase probability. If we look at a 0.5-standard deviation increase in the average rating of substitute products (home/garden category), the purchase likelihood decreases from 4.2% to 4%. At <sup>fi</sup>rst glance, the economic impact (0.2% point increase or decrease) may not seem large. However, even a 0.2% point increase in purchase likelihood would be substantial given millions of purchases in large online retail platforms, such as Amazon or the platform in our study. Our data show that there are 97,852 unique consumers and 493,928 productsession observations in a two-month period. The focal platform is one of the largest online retailers in the United Kingdom with 29 million yearly customers as of 2016. Therefore, an estimate is that a 0.2% point increase or decrease involves 1,756,601 purchase orders annually $( = ~ 4 9 3 , 9 2 8 \times 0 . 2 ^ { \circ } / \circ \times \frac { 2 9 , 0 0 \bar { 0 } , 0 0 0 } { 9 7 , 8 5 2 } \times \frac { 1 2 } { 2 } )$ for the online platform, which is economically signi<sup>fi</sup>cant. As expected, we found that the coef<sup>fi</sup>cient of rating\_ focal is positive and signi<sup>fi</sup>cant, which re<sup>fl</sup>ects the role of online product reviews. Furthermore, the volume of reviews, vol\_focal, also has a positive effect. A possible reason is that a large volume of reviews may reduce the uncertainty inherent in product purchases. In columns (3) and (4) in Table 3, we also controlled for the mean volume of the product reviews of substitutes/ complements (vol\_subs/vol\_comp) to fully capture the spillover role of online product reviews. Other than the linear probability model, we also conducted a logit regression and a <sup>fi</sup>xed effects logit regression, and we found that the results remained robust (Online Appendix A, Table A.1). Our estimation results show that the effect of the ratings for other products on the focal product purchase is even stronger than that for the focal product. A possible explanation is that the spillover effect is the combination of demand substitution effect and crossproduct rating effect (i.e., reference/ contextual point effect) illustrated in Figure 1. We also analytically show this result as in Online Appendix D. With the demand substitution effect only, the spillover effect has no difference; however, the spillover effect, combined with the reference/contextual point effect, can be larger than the focal effect.

## 5.2. The Moderating Effect of Channel (Mobile Vs. PC)

According to our clickstream data, PC users, on average, read more product information (22.8 question and answer (Q&A) entries and 8.3 reviews) than mobile users (16.1 Q&A entries and 7.2 reviews). This may be because of the fact that PCs provide better accessibility in product exploration than mobile devices. In fact, our data show that PC users leveraged more exploration functions (0.11 pagination, 0.12 read all, and 0.015 sort) compared with mobile users (0.09 pagination, 0.067 read all, and 0.005 sort).<sup>7</sup> These <sup>fi</sup>ndings motivate us to formally investigate how the spillover effect is moderated by channel (mobile or PC). To examine these issues, we added interaction terms in Equation (1) and obtained the following speci<sup>fi</sup>cations:

$$
\begin{array}{l} p u r c h a s e _ {i, j, t} = a _ {i} + v _ {j} + \beta_ {0} + \beta_ {1} r a t i n g \_ f o c a l _ {i, j, t} + \beta_ {2} v o l \_ f o c a l _ {i, j, t} \\ \quad + \beta_ {3} m o b i l e _ {i, j, t} + \beta_ {4} r a t i n g \_ s u b s _ {i, j, t} \\ \quad + \beta_ {5} r a t i n g \_ c o m p _ {i, j, t} + \beta_ {6} r a t i n g \_ s u b s \_ m o b i l e _ {i, j, t} \\ \quad + \beta_ {7} r a t i n g \_ c o m p \_ m o b i l e _ {i, j, t} + \text {time dummies} \\ \quad + \varepsilon_ {i, j, t}, \end{array}\tag{2}
$$

where mobile is whether a mobile device is used in the session and rating\_subs\_mobile and rating\_comp\_mobile are interaction terms rating\_subs mobile and rating\_ comp mobile, respectively.

The coef<sup>fi</sup>cients of the interactions terms in Equation (2) specify how the spillover effect is moderated by whether the product information and reviews are viewed on a mobile or a PC. Self-selection bias may exist: A consumer with certain time-invariant characteristics may be more likely to use a mobile device than a PC. However, by controlling for individual <sup>fi</sup>xed effects, a (Equation (2)), self-selection bias is less of a concern.

Estimation results are shown in columns (1) and (2) (Table 4). Both coef<sup>fi</sup>cients of rating\_subs\_mobile are negative, whereas both coef<sup>fi</sup>cients of rating\_comp\_mobile are positive, supporting Hypotheses 2a and 2b, respectively. Estimation results show that for consumers who use mobile devices, the spillover effect of online reviews is much stronger: The negative role of the online reviews of substitutes is two to three times larger; the positive role of the online reviews of complements is about two times larger. The moderating role of channel is more prominent in the home/garden category than in the technology category. These results imply that mobile devices make the spillover effect of online reviews more pronounced than PCs, which can be explained in our mechanisms of spillover effect (Figure 1): The crossproduct rating effect (based on reference points) is stronger for mobile consumers, which leads to a stronger overall spillover effect. The reason is that the small screen size and high search cost of mobile devices reduce the overall amount of information that consumers can access. Hence, consumers tend to focus more on the salient, quantitative features of reviews (e.g., mean review ratings) as a contextual reference point rather than analyzing all available signals (e.g., review text).

A potential explanation of the lower signi<sup>fi</sup>cant moderating effect of a mobile device in the technology category is that consumers browsing technology products tend to be more tech savvy, and thus, their increase in the cognitive cost of using small screens may be less than the increase in cognitive cost for home/garden products. Additionally, we can consider home/garden products as experience goods and technology products as search goods. In contrast to experience goods, a search good is a product/service with features and characteristics easily evaluated before purchase. Therefore, there is less of a need for consumers to look at the detailed review content for technology than for home/garden products, and hence, the moderating effect of mobile devices in the technology category is less signi<sup>fi</sup>cant.

To further investigate the role of mobile channel in signal strength, we estimate the following model:

$$
\begin{array}{l} p u r c h a s e _ {i, j, t} = a _ {i} + v _ {j} + \beta_ {0} + \beta_ {1} r a t i n g \_ f o c a l _ {i, j, t} + \beta_ {2} v o l \_ f o c a l _ {i, j, t} \\ \quad + \beta_ {3} m o b i l e _ {i, j, t} + \beta_ {4} r a t i n g \_ s u b s _ {i, j, t} \\ \quad + \beta_ {5} r a t i n g \_ c o m p _ {i, j, t} + \beta_ {6} r a t i n g \_ s u b s \_ m o b i l e _ {i, j, t} \\ \quad + \beta_ {7} r a t i n g \_ c o m p \_ m o b i l e _ {i, j, t} + \beta_ {8} v a r \_ f o c a l \_ v i e w e d _ {i, j, t} \\ \quad + \beta_ {9} v a r \_ s u b \_ v i e w e d _ {i, j, t} + \beta_ {1 0} v a r \_ c o m p \_ v i e w e d _ {i, j, t} \\ \quad + \beta_ {1 1} (v a r \_ s u b \_ v i e w e d _ {i, j, t} \times m o b i l e _ {i, j, t}) \\ \quad + \beta_ {1 2} (v a r \_ c o m p \_ v i e w e d _ {i, j, t} \times m o b i l e _ {i, j, t}) \\ \quad + \text {time dummies} + \varepsilon_ {i, j, t}, \end{array}\tag{3}
$$

Table 4. The Moderating Role of Mobile Devices

<table><tr><td>Variables</td><td>(1) Mobile (home)</td><td>(2) Mobile (technology)</td><td>(3) Mobile (home)</td><td>(4) Mobile (technology)</td></tr><tr><td>rating_focal</td><td>0.000832* [1.811]</td><td>0.000417 [0.575]</td><td>0.00107* [1.914]</td><td>0.00124* [1.825]</td></tr><tr><td>vol_focal</td><td>2.35e-05*** [9.528]</td><td>2.80e-05*** [4.332]</td><td>3.34e-05*** [3.482]</td><td>2.34e-05*** [3.654]</td></tr><tr><td>rating_subs</td><td>-0.00367*** [-9.336]</td><td>-0.00269*** [-4.505]</td><td>-0.000627 [-1.254]</td><td>-0.000814 [-1.032]</td></tr><tr><td>rating_comp</td><td>0.00312*** [5.229]</td><td>0.00239*** [2.586]</td><td>0.00427*** [3.658]</td><td>0.00322*** [3.423]</td></tr><tr><td>rating_subs_mobile</td><td>-0.00682*** [-6.705]</td><td>-0.00366** [-2.149]</td><td>-0.00684*** [-3.226]</td><td>-0.00552*** [-2.932]</td></tr><tr><td>rating_comps_mobile</td><td>0.00253** [2.169]</td><td>0.00143 [0.463]</td><td>-0.00471 [-0.788]</td><td>-0.00317 [-0.532]</td></tr><tr><td>var_focal_viewed</td><td></td><td></td><td>-0.00765*** [-8.432]</td><td>-0.00625*** [-7.351]</td></tr><tr><td>var_subs_viewed</td><td></td><td></td><td>0.00565*** [4.874]</td><td>0.00487*** [4.334]</td></tr><tr><td>var_comp_viewed</td><td></td><td></td><td>-8.67e-05 [-0.0553]</td><td>-6.17e-05 [-0.0454]</td></tr><tr><td>var_subs_viewed × mobile</td><td></td><td></td><td>-0.00527** [-2.212]</td><td>-0.00453** [-2.117]</td></tr><tr><td>var_comp_viewed × mobile</td><td></td><td></td><td>0.000337 [0.0591]</td><td>0.000254 [0.0482]</td></tr><tr><td>Observations</td><td>21,159</td><td>17,254</td><td>21,159</td><td>17,254</td></tr></table>

Note. Cluster robust t statistics are in brackets.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.  
purchase<sub>i,j,t -</sub> a<sub>i +</sub> v<sub>j +</sub> β <sub>+</sub> β rating focal<sub>i,j,t +</sub> β vol focal<sub>i,j,t</sub>

where var\_focal\_viewed is the variance of ratings of the focal product’s review viewed by the consumer at the shopping session and var\_subs\_viewed (var\_ comp\_viewed) is the average of viewed rating variance of substitute (complementary) products viewed by the consumer. Estimation results are shown in columns (3) and (4) of Table 4. We <sup>fi</sup>nd that using mobile devices tends to increase the impact of average rating and reduce the impact of the variance of ratings. The intuition is that the small screen size of mobile devices makes the signal of review rating more salient and makes the signal of variance of review ratings less salient: Consumers can directly see the average review ratings of substitutive products on the product page; however, they need to exert more cognitive and physical effort by scrolling down a list of individual reviews shown on the smaller screens of mobile phones and examining the variance of review ratings.

## 5.3. The Moderating Role of Brand

In the next estimation, we examine the role of the same brand versus different brands (Equation (3)):

<sub>+</sub> β rating subs samebrand<sub>i,j,t</sub>

<sub>+</sub> β rating comp samebrand<sub>i,j,t</sub>

<sub>+</sub> β<sub>5</sub>rating subs diffbrand<sub>i,j,t</sub>

<sub>+</sub> β rating comp diffbrand<sub>i,j,t +</sub> β price focal<sub>i,j,t</sub>

<sub>+</sub> β<sub>8</sub>price subs<sub>i,j,t</sub> <sub>+</sub> β<sub>9</sub>price comp<sub>i,j,t</sub>

<sub>+</sub> time dummies <sub>+</sub> ε<sub>i,j,t</sub>,

(4)

where rating\_subs\_samebrand (rating\_comp\_samebrand) is the mean rating of substitutes (complements) produced by the same brand, rating\_subs\_diffbrand (rating\_comp\_- diffbrand) is the mean rating of the substitutes (complements) produced by different brands, price\_focal is the price of the focal product, and price\_subs (price\_comp) is the mean price of the substitutes (complements) of the focal product.

In column (5) of Table 3, we present the estimation results for the home/garden category. We found that both the focal product’s mean rating and review volume have positive effects on the purchase of the focal product, which is consistent with the literature. Coef<sup>fi</sup>cients rating\_subs\_diffbrand and rating\_subs\_ samebrand are negative and signi<sup>fi</sup>cant, whereas coef<sup>fi</sup>- cients rating\_comp\_diffbrand and rating\_comp\_samebrand are positive and signi<sup>fi</sup>cant. We conducted statistical tests on whether the coef<sup>fi</sup>cient on rating\_subs\_diffbrand equals that on rating\_subs\_samebrand and whether the coef<sup>fi</sup>cient on rating\_comp\_diffbrand equals that on rating\_ comp\_samebrand. The test results show that (i) rating\_ subs\_diffbrand has a signi<sup>fi</sup>cantly larger negative role than rating\_subs\_samebrand, which implies that the negative spillover role of the online reviews of substitutive products from different brands is signi<sup>fi</sup>cantly higher than that of the same brand, supporting Hypothesis 3a. They also show that (ii) rating\_comp\_diffbrand is not statistically different from rating\_comp\_samebrand, and the implication is that the positive spillover role of the online reviews of complementary products from different brands is not statistically different from the role of the online reviews of complementary products within the same brand, thus not supporting Hypothesis 3b.

One explanation is that there are two positive effects of review ratings of a complementary product in the purchase of another product for products within the same brand—the complementary role from copurchasing and the transferred value within the same brand. In the home/garden category, the role of the transferred value in the same brand can be weak. Summarizing our results, we show that the magnitude of the spillover role of online product reviews depends on whether the product is a substitute or a complement and whether the product belongs in the same or in a different brand. Column (6) of Table 3 shows the results for the technology category, which are consistent with those in the home/ garden category.

## 5.4. The Moderating Effect of Consumer Experience and Rating Variance

Next, we examine the effect of consumer experience using the following equation (Equation (5)):

$$
\begin{array}{r l} p u r c h a s e _ {i, j, t} = & a _ {i} + v _ {j} + \beta_ {0} + \beta_ {1} r a t i n g \_ f o c a l _ {i, j, t} + \beta_ {2} v o l \_ f o c a l _ {i, j, t} \\ & + \beta_ {3} r a t i n g \_ s u b s _ {i, j, t} + \beta_ {4} r a t i n g \_ c o m p _ {i, j, t} \\ & + \beta_ {5} e x p e r i e n c e _ {i, t} + \beta_ {6} (e x p e r i e n c e _ {i, t} \times r a t i n g \_ s u b s _ {i, j, t}) \\ & + \beta_ {7} (e x p e r i e n c e _ {i, t} \times r a t i n g \_ c o m p _ {i, j, t}) \\ & + \text {time dummies} + \varepsilon_ {i, j, t}, \end{array}\tag{5}
$$

where experience is measured by two variables: (i) sess\_count\_samecate: the number of previous online sessions in the same subcategory; and (ii) purchases\_samecate: the number of previous purchases in the same subcategory. A unique advantage of our clickstream data is that we can measure consumer experience using their browsing history $( \mathrm { e . g . , }$ the number of previous shopping sessions and the number of previous purchases in a speci<sup>fi</sup>c product subcategory). We <sup>fi</sup>nd consistent results in Table 5: In all regressions, the impact of the review rating of substitutive products on the focal product purchase is signi<sup>fi</sup>cantly smaller (less negative) for more experienced consumers. In other words, more experienced consumers are less affected by review ratings. This <sup>fi</sup>nding can be explained in our proposed mechanisms of the spillover effect (Figure 1): The crossproduct rating effect (based on reference points) is stronger for less experienced consumers, which leads to a stronger overall spillover effect of ratings. Experienced consumers typically have more channels to infer product quality. Hence, there is less need for them to rely on the review rating of substitutive products as signals to evaluate similar products, and they weigh less on the review ratings as a contextual reference point. In contrast, consumers who face higher uncertainty because of lack of prior experience might rely more on signals from online reviews to infer product quality, and the evaluation of alternatives would matter more.

Table 5. Moderating Effect of Consumer Experience

<table><tr><td>Variables</td><td>(1) Home (experience = sess_count_samecate)</td><td>(2) Technology (experience = sess_count_samecate)</td><td>(3) Home (experience = purchases_samecate)</td><td>(4) Technology (experience = purchases_samecate)</td></tr><tr><td>rating_focal</td><td>0.000453[0.630]</td><td>0.000421[0.451]</td><td>0.000533[0.623]</td><td>0.000386[0.524]</td></tr><tr><td>vol_focal</td><td>2.92e-05***[4.450]</td><td>2.62e-05***[4.238]</td><td>2.95e-05***[4.524]</td><td>2.74e-05***[4.154]</td></tr><tr><td>experience</td><td>-0.00673***[-2.723]</td><td>-0.00685***[-2.712]</td><td>-0.00541[-1.125]</td><td>-0.00657[-1.335]</td></tr><tr><td>rating_subs</td><td>-0.00332***[-5.128]</td><td>-0.00375***[-5.664]</td><td>-0.00286***[-4.347]</td><td>-0.00282***[-4.134]</td></tr><tr><td>rating_subs × experience</td><td>0.00184***[3.225]</td><td>0.00183***[2.975]</td><td>0.00426***[2.865]</td><td>0.00392***[2.834]</td></tr><tr><td>rating_comp</td><td>0.00275***[2.834]</td><td>0.00254***[2.802]</td><td>0.00321***[3.231]</td><td>0.00321***[3.253]</td></tr><tr><td>rating_comp × experience</td><td>-0.00161**[2.142]</td><td>-0.00183**[2.213]</td><td>-0.00388*[1.785]</td><td>-0.00365*[1.703]</td></tr><tr><td>Observations</td><td>21,159</td><td>17,254</td><td>21,159</td><td>17,254</td></tr></table>

Note. Robust t statistics are in brackets.  
\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

We investigate the effect of rating variance using the following regression equation (Equation (6)):

$$
\begin{array}{r l} p u r c h a s e _ {i, j, t} & = a _ {i} + v _ {j} + \beta_ {0} + \beta_ {1} r a t i n g \_ f o c a l _ {i, j, t} + \beta_ {2} v o l \_ f o c a l _ {i, j, t} \\ & \quad + \beta_ {3} r a t i n g \_ s u b s _ {i, j, t} + \beta_ {4} r a t i n g \_ c o m p _ {i, j, t} \\ & \quad + \beta_ {5} v a r \_ f o c a l \_ v i e w e d _ {i, j, t} + \beta_ {6} v a r \_ s u b s \_ v i e w e d _ {i, j, t} \\ & \quad + \beta_ {7} v a r \_ c o m p \_ v i e w e d _ {i, j, t} + \beta_ {8} (v a r \_ s u b s \_ v i e w e d _ {i, j, t} \\ & \quad \times r a t i n g \_ s u b s _ {i, j, t}) + \beta_ {9} (v a r \_ c o m p \_ v i e w e d _ {i, j, t} \\ & \quad \times r a t i n g \_ c o m p _ {i, j, t}) + t i m e d u m m i e s + \varepsilon_ {i, j, t}. \end{array}\tag{6}
$$

Estimation results are shown in Table 6. We <sup>fi</sup>nd that the viewed variance of ratings plays a key moderating role. When the variance of viewed review rating of substitutive products $( v a r \_ s u b s \_ v i e w e d _ { i , j , t } )$ is lower, the effect of review rating of substitutive products becomes stronger (more negative), implying that the signaling effect is larger as it stems from more consistent opinions.

Table 6. Moderating Effect of Rating Variance

<table><tr><td>Variables</td><td>(1) Home</td><td>(2) Technology</td></tr><tr><td>rating_focal</td><td>0.00293**[2.862]</td><td>0.00212**[2.523]</td></tr><tr><td>var_focal_viewed</td><td>-0.00532***[-10.11]</td><td>-0.00884***[-12.33]</td></tr><tr><td>vol_focal</td><td>5.12e-05***[4.336]</td><td>3.12e-05***[4.652]</td></tr><tr><td>rating_subs</td><td>-0.00452***[-3.935]</td><td>-0.00373***[-3.805]</td></tr><tr><td>var_subs_viewed</td><td>-0.00315[-0.422]</td><td>-0.00213[-0.526]</td></tr><tr><td>rating_subs × var_subs_viewed</td><td>0.00227***[3.743]</td><td>0.00156***[3.523]</td></tr><tr><td>rating_comp</td><td>0.00417***[3.624]</td><td>0.00374***[3.325]</td></tr><tr><td>var_comp_viewed</td><td>0.0213**[2.452]</td><td>0.0152**[2.336]</td></tr><tr><td>rating_comp × var_comp_viewed</td><td>-0.00442***[-3.132]</td><td>-0.00512***[-3.074]</td></tr><tr><td>Observations</td><td>21,159</td><td>17,254</td></tr></table>

\*\*p < 0.05; \*\*\*p < 0.01.  
Note. Robust t statistics are in brackets.

As discussed earlier and also shown in Figure 1, the role of mean review ratings as a contextual reference point can also be stronger as the magnitude of the signaling effect increases. Similarly, when the variance of viewed review rating of complementary products is lower, the effect of the review rating of complementary products becomes stronger (more positive).

## 5.5. Robustness Checks

In our model, prices may be endogenous because prices may change in response to demand and vice versa. To address this potential price endogeneity and to con<sup>fi</sup>rm the validity of our machine learning-based classi<sup>fi</sup>cation of substitutes/complements, we estimated Online Appendix A, Equation A1 and present the results in Online Appendix A.

Another potential concern in our previous regression model is that the mean review ratings of substitutive and complementary products may be endogenously determined. To address this potential endogeneity concern, we used a more exogenous IV following Jabr and Zheng (2014). Speci<sup>fi</sup>cally, our proposed IV for a product’s review rating is the review ratings of other products posted by the same reviewers. The intuition is that an online review re<sup>fl</sup>ects both the reviewer’s evaluation on the product and her personal predisposition for the rating. Predisposition captures a reviewer’s idiosyncratic tendency to write a speci<sup>fi</sup>c review and can be estimated by examining the reviewer’s previous reviews. Note that the predisposition should be uncorrelated with product characteristics because the measure is constructed before the reviewer posts her product review. Therefore, our new IV should be exogenous. We instrumented for $r a t i n g \_ s u b s _ { i , j , t }$ and $r a t i n g \_ c o m p _ { i , j , t }$ using the mean review ratings of other products posted by the same reviewers. The estimation results are shown in columns (5) and (6) of Table A.2 in Online Appendix A. We <sup>fi</sup>nd that our results are robust: The mean rating of substitutes (complements) has a negative (positive) role in the purchase probability of the focal product. We also checked the coef<sup>fi</sup>cients on price\_subs (price\_comp) at the product pairwise level in Table A.3 in Online Appendix A.

## 6. Contributions and Implications for Theory and Practice 6.1. Key Findings

First, we <sup>fi</sup>nd that the mean review rating of substitutive (complementary) products has a negative (positive) role in the purchase probability of a focal product. Second, the spillover role of online product reviews is moderated by brand, channel media, consumer experience, and review rating variance; speci<sup>fi</sup>cally, the negative spillover role of the mean rating of substitutive products across different brands is signi<sup>fi</sup>cantly higher than those within the same brand. Additionally, the spillover role of the mean ratings of online product reviews is signi<sup>fi</sup>cantly higher for consumers on mobile devices versus PCs. Table 7 shows the practical signi<sup>fi</sup>- cance of the spillover effects estimated in our main regressions. It is worth noting that the average purchase probabilities in home/garden or technology data are about 4.2% and 3.7%, respectively (thus, the increase/ decrease in purchase probability is based on dividing by 4.2 and 3.7, respectively). In the interpretation of the practical signi<sup>fi</sup>cance effects in Table 7, we focus on the change (increase/decrease) in the average purchase probability of a focal product shaped by the online reviews of substitutes and complements from the same or different brands. In sum, a one-star rating increase in substitutes leads to a 9%–14% decrease in the purchase probability of a focal product; a one-star rating increase in complements leads to a 6%–9% increase in the purchase probability of a focal product.

Table 7. Practical (Economic) Signi<sup>fi</sup>cance of the Spillover Effects

<table><tr><td>Regression (Table 3)</td><td>Independent variable</td><td>Category</td><td>Coefficient</td><td>Change in purchase probability</td></tr><tr><td>Column (3)</td><td>Rating of substitutes</td><td>Home</td><td>-0.00607</td><td>14.5% decrease</td></tr><tr><td>Column (4)</td><td>Rating of substitutes</td><td>Technology</td><td>-0.00355</td><td>9.6% decrease</td></tr><tr><td>Column (3)</td><td>Rating of complements</td><td>Home</td><td>0.00385</td><td>9.2% increase</td></tr><tr><td>Column (4)</td><td>Rating of complements</td><td>Technology</td><td>0.00222</td><td>6% increase</td></tr></table>

Note. The <sup>fi</sup>gures state the magnitude of the spillover effects when an independent variable (rating) increases by one.

## 6.2. Contributions and Implications for Theory

We contribute to the literature on online product reviews and user-generated content by examining the spillover role of online product reviews among complementary and substitutive products in a consumer’s purchasing decision. Studies have shown the mean rating to be a strong predictor of product sales for a single focal product. Recent studies have examined the effect of online reviews on consumers’ perceptions (Luo et al. 2017) and on sales rank among competing products (Jabr and Zheng 2014). To our knowledge, however, this is the <sup>fi</sup>rst study to show the spillover effect of the mean review rating of other related (i.e., both substitutive and complementary) products in an individual consumer’s purchase of a focal product. First, we <sup>fi</sup>nd a negative (positive) spillover role of online reviews among substitutive (complementary) products, whereas the extent of the spillover effect depends on media channels, brand, consumer experience, and variance of ratings. The literature mostly focuses on the prediction of aggregate product sales from the review ratings. We extend the literature by showing the role of the review ratings in an individual consumer’s purchasing decision in a covisited consideration set, and we show that the spillover effects of the ratings substantially depend on the association of the covisited products.

Second, we contribute to the literature on mobile devices by examining the role of spillover across the channels. We <sup>fi</sup>nd the spillover effect to be notably more salient on mobile devices versus PCs because of the on-the-go mindset and the limited search, making it more dif<sup>fi</sup>cult for consumers to locate and process multiple signals. Our <sup>fi</sup>ndings show that consumers rely on quantitative ratings more on mobile devices, extending the prior work on higher cognitive efforts and the ranking effect of mobile devices (Ghose et al. 2013). We complement the understanding in the literature by <sup>fi</sup>nding that a higher cognitive effort on mobile devices makes the role of the mean ratings and its spillover effect across related products more pronounced.

Third, we show the spillover role of online product reviews within the same and across different brands. The literature has stressed the role of brands (e.g., Lovett et al. 2013, Tirunillai and Tellis 2014, Luo et al. 2017). However, studies on the role of brands on an individual consumer’s purchase decision, together with the spillover role of online product reviews, have been limited. Our results show that the mean review rating of the products in a consumer’s market basket has a spillover effect on each other, and this effect depends on the relation among products (substitutive/complementary) and among brands (same/different). We extend the literature on brand spillover by showing the overall negative role of the rating spillover for substitutive products and the larger negative role among different (versus the same) brands. We also <sup>fi</sup>nd a positive role of the rating spillover for complementary products, albeit that the difference among the same versus different brands is not supported. We attribute these results to the functional similarity across products in the consumers’ minds. The value transfer within the same brand in the spillover role of the online product reviews may be high in substitutive products because of the perceived similar functions within a same brand, which may offset the competitive substitution effects and derive a signi<sup>fi</sup>cant difference between same or different brands for substitutive products. The brand literature focuses on the effect of marketing promotions or publicity on demand changes of a limited set of products. We extend the literature by showing the effect of consumer-generated reviews on an individual consumer’s purchasing decision among covisited products.

## 6.3. Implications for Practice and the Design of Online Product Review Systems

Marketing practitioners have viewed WOM or usergenerated content as in<sup>fl</sup>uential marketing tools. We show that the role of the mean review rating can spill over across other products in a consumer’s market basket and that this spillover role is different across media channels (mobile or PC) and across products of the same versus different brands. Our result on media channels, the salient impact of review ratings on mobile media, suggests the unequal importance of mean ratings across media channels and needs for a differentiated design of marketing messages across devices. In addition, the perception of brands and the effect of WOM across brands have been key factors for marketers to leverage the marketing mix. Therefore, our paper also contributes to marketing practitioners by helping to understand these brand effects on consumers’ decisions. Additionally, we reveal that the impact of the review ratings differs in terms of an individual consumer’s experience and the variance of the review ratings. Retailers often use data about consumer activities and product reviews for sales prediction and tailored recommendations. In this regard, our results help retailers better leverage the nuanced role of the review ratings.

Finally, our study has managerial implications for marketing practitioners to stand out from the competition by leveraging online reviews, shedding light on how to take account of the spillover effects to design better online review systems. For instance, online reviews of a focal product may enhance or hurt the sales of other substitutive or complementary products, and brands and channel media can moderate this spillover effect. Retailers may want to differently feature the online ratings of substitutive or complementary products, which also can be tailored for different channel media and consumers of different experience levels. Given our <sup>fi</sup>ndings, retailers can redesign their review systems to enable consumers to write comparative reviews, where multiple substitutive products purchased can be evaluated together. The market basket information from copurchased complementary products also can inform other consumers of the synergy among the products, boosting their demand. It can also be useful to dynamically generate a comparative review page that outlines the online reviews of other products in the consumer’s consideration set or product recommendations.

## 6.4. Methodological Contributions

The effects of substitutive and complementary products have been well studied in the economics and marketing literature (e.g., Shocker et al. 2004, Seetharaman et al. 2005); however, the empirical measurement of substitutive and complementary products has not been well developed. The literature de<sup>fi</sup>nes substitutive and complementary products based on the functional similarity of products in consumers’ usage and simultaneous needs across multiple products. To identify related (complementary and substitutive) products, we developed and validated a machine-learning approach to classify the relationship of product pairs (e.g., substitutive, complementary, or unrelated) using product description similarity and other product characteristics. Compared with the conventional method using the product category match, our approach minimizes misclassi<sup>fi</sup>cation errors because product features are algorithmically extracted from the product descriptions. Also, the topic modeling algorithm converts each product textual description into a distribution of multiple product features. In other words, a product can be categorized into multiple categories with different weights. Finally, the product similarity values produced by our method are continuous. Thus, we can measure to which degree a pair of products is a substitute or complementary to each other, instead of making a binary call.

## 6.5. Limitations

First, our empirical investigation is limited to each product category (technology or home/garden). Each category has a large number of different subcategories under which the number of products is also large, but intercategory relationship is not captured by our data. Second, our measure of complements and substitutes is not complete. For instance, a notepad can serve as a complement to a laptop, but at the same time, it can be a substitute. Similarly, our model may not identify the products that have low (high) similarity in their functions but can work as substitutes (complements). An example includes an e-book reader for a home movie theater. Third, our result does not capture the longterm effect. In our analysis, the products covisited only in a session (e.g., within an hour) are considered. That is, our results should not apply to consumer decisions over multiple sessions and the effect across sessions. A structural model may better characterize the individual-level decision making but also puts excessive restrictions on the underlying mechanism. However, dealing with a large number of consumers and products, our reduced form approach provides robust results and signi<sup>fi</sup>cantly reduces the computational burden from a large set of choices. Fourth, the observed strong spillover effect in our context is a combination of two underlying mechanisms: demand substitution/complement effect and crossproduct rating effect. A future research direction is to use experimental methods to empirically separate these two mechanisms. Finally, our measure of online product reviews is limited to quantitative ratings, not stretched to review text. Therefore, the distinction between ratings and review text (Pavlou and Dimoka 2006) in purchasing decisions and the net effect of the online reviews are not captured.

## 6.6. Concluding Remark

Using clickstream data, we specify a consumer’s consideration set and offer a more complete picture on how online product reviews operate across products at the individual consumer level. Speci<sup>fi</sup>cally, we examine whether and how the ratings of substitute and complementary products a consumer views affect her likelihood of purchasing a focal product. Prior literature has focused on the direct impact of online reviews on the sales of an individual product. We show that online ratings of other products have a strong spillover effect on a focal product purchase, much stronger compared with the effect of ratings of the same product, and this spillover effect is moderated by brand, channel media, consumer experience, and the variance of the review ratings. Our results extend the burgeoning literature on online product reviews across different products, and they offer theoretical insights and practical recommendations to design effective online product review systems.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their detailed and constructive comments. They thank Wharton Customer Analytics Initiative for providing the data set and Bolat Khojayev and Raymond Situ for their research assistance. All authors contributed equally to the paper, and the order of authorship is alphabetical.

## Endnotes

<sup>1</sup> Borah and Tellis (2016) used the term perverse halo as the phenomenon where negative chatter about one product spills over into a negative chatter for another product, and they used the term “spillover” interchangeably. In this paper, we use the generic term “spillover” to capture the extent to which the online reviews of one product may affect the consumers’ perceptions/beliefs/purchases of related products. Speci<sup>fi</sup>cally, we examine whether, how, and why there is a spillover role of the online reviews of related products in an individual consumer’s purchasing of a focal product. Us ing a randomized <sup>fi</sup>eld experiment, Anderson and Simester (2013) quantify the impact of competitors’ advertising on sales at a focal retailer. Customers only in the treatment group received targeted direct mail advertisements from the focal retailer’s close competitors. Borah and Tellis (2016) examine whether product recalls of one brand hurt or help rival brands using vector autoregression models. They focus on Granger causality instead of causality in microeconometrics. Jabr and Zheng (2014) analyze the effect of online reviews on sales ranks of competing products using an approach of instrumental variables. Following Jabr and Zheng (2014), we also adopt instrumental variables to identify spillover effects in our study.

<sup>2</sup> For instance, when a consumer wants to purchase an high-de<sup>fi</sup>nition light-emitting diode TV, it is likely that she searches many TVs with similar speci<sup>fi</sup>cations that match her preferences and interests to <sup>fi</sup>nd the best TV among all substitutive TVs. She is also likely to search for TV wall brackets and/or sound bars together, which complement the use of the focal TV.

<sup>3</sup> Clickstream data of individual consumers who shop on a retailer’s website allow us to observe complete records of the products each consumer has viewed and the online product reviews of these products, enabling us to clearly de<sup>fi</sup>ne a consumer’s consideration set and examine whether the online product reviews of other related (substitutive or complementary) products that attract the consumer’s attention affect her likelihood of purchasing a focal product.

4 There is also an emerging literature on the diffusion of user-generated content on digital networks (Susarla et al. 2012), consumer attention through a recommendation network (Oestreicher-Singer and Sundararajan 2012a, b; Lin et al. 2017), and celebrity endorsement through co\purchase recommendation networks (Carmi et al. 2012). Overall, these papers focus on the propagation of the digital content or opinion throughout the network and the effect of placement of visible product networks on the contagion process (e.g., network proximity). In this study, we focus on online product reviews viewed by individual consumers and the effect on their purchase decision.

<sup>5</sup> It is worth noting that this is not a typical missing data issue: It is not the case that consumers have left online product reviews, but we cannot observe them. For our research purpose, products with no reviews are irrelevant. Similar to our study, limiting data sample to products with a suf<sup>fi</sup>cient number of reviews is widely adopted in the literature on online product reviews (e.g., Chevalier and Mayzlin 2006, Forman et al. 2008, Li and Hitt 2008).

<sup>6</sup> Because of the large number of products in our sample, the standard demand estimation model is not computational feasible. Also, a typical concern in estimating demand-side models is price endogeneity. We address this concern using the instrumental variable approach. We have conducted the Hausman tests, and the <sup>fi</sup>xed effects model is favored over the random effects model.

<sup>7</sup> The “pagination” function lets consumers view different pages of reviews, the “read-all” function lets them read all the reviews in a single page, and the “sort” function lets them sort the reviews by recency and numeric ratings.

## References

Aaker DA (1991) Managing Brand Equity (The Free Press, New York).

Aaker DA (1996) Building Strong Brands (The Free Press, New York).

Aggarwal R, Gopal R, Gupta A, Singh H (2012) Putting money where the mouths are: The relation between venture <sup>fi</sup>nancing and eWOM. Inform. Systems Res. 23(3):976–992.

Ahluwalia R, Unnava HR, Burnkrant RE (2001) The moderating role of commitment on the spillover effect of marketing communications. J. Marketing Res. 38(4):458–470.

Anderson ET, Simester D (2013) Advertising in a competitive market: The role of product standards, customer learning, and switching costs. J. Marketing Res. 50(4):489–504.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Ariely D (2016) Time pressure: Behavioral science considerations for mobile marketing. Accessed August 10, 2016, https://think .storage.googleapis.com/docs/time-pressure-behavioral-science -considerations-mobile-marketing.pdf.

Balachander S, Ghose S (2003) Reciprocal spillover effects: A strategic bene<sup>fi</sup>t of brand extensions. J. Marketing 67(1):4–13.

Bart Y, Stephen AT, Sarvary M (2014) Which products are best suited to mobile advertising? A <sup>fi</sup>eld study of mobile display advertising effects on consumer attitudes and intentions. J. Marketing Res. 51(3):270–285.

Barwise P, Strong C (2002) Permission-based mobile advertising. J. Interactive Marketing 16(1):14–24.

Basuroy S, Desai KK, Talukdar D (2006) An empirical investigation of signaling in the motion picture industry. J. Marketing Res. 43 (2):287–295.

Blackwell RD, Miniard PW, Engel JF (2001) Consumer Behavior, 9th ed. (Harcourt College Publishers, Fort Worth, TX).

Borah A, Tellis GJ (2016) Halo (spillover) effects in social media: Do product recalls of one brand hurt or help rival brands? J. Marketing Res. 53(2):143–160.

Burtch G, Hong Y (2014) What happens when word of mouth goes mobile? Proc. Internat. Conf. Inform. Systems (Auckland, New Zealand).

Burtch G, Hong Y, Bapna R, Griskevicius V (2018) stimulating online reviews by combining <sup>fi</sup>nancial incentives and social norms. Management Sci. 64(5):2065–2082.

Butcher D (2010) Mobile ad campaigns 5 times more effective than online: InsightExpress study. Marketing Dive (February 5), https://www.marketingdive.com/ex/mobilemarketer/cms/news/ research/5308.html.

Cameron AC, Gelbach JB, Miller DL (2008) Bootstrap-based improvements for inference with clustered errors. Rev. Econom. Statist. 90(3):414–427.

Carmi E, Oestreicher-Singer G, Sundararajan A (2012) Is Oprah contagious? Identifying demand spillovers in online networks. identifying demand spillovers in online networks. NET Institute Working Paper 10-18. Preprint, submitted August 31, http://dx.doi.org/10.2139/ssrn.1694308.

Chae I, Stephen A, Bart Y, Yao D (2016) Spillover effects in seeded word-of-mouth marketing campaigns. Marketing Sci. 36(1):89–104.

Chen Y, Xie J (2005) Third-party product review and <sup>fi</sup>rm marketing strategy. Marketing Sci. 24(2):218–240.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Haldar S (1998) Investigating purchase timing behavior in two related product categories. J. Marketing Res. 35(1): 43–53.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The effects of online user reviews on movie box of<sup>fi</sup>ce performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Clemons EK, Gao G, Hitt LM (2006) When online reviews meet hyper differentiation: A study of the craft beer industry. J. Man agement Inform. Systems 23(2):149–171.

Connelly BL, Certo ST, Ireland RD, Reutzel CR (2011) Signaling theory: A review and assessment. J. Management 37(1):39–67.

Dellarocas C (2006) Strategic manipulation of internet opinion forums: Implications for consumers and <sup>fi</sup>rms. Management Sci. 52(10):1577–1593.

Dellarocas C, Gao G, Narayan R (2010) Are consumers more likely to contribute online reviews for hit or niche products? J. Management Inform. Systems 27(2):127–157.

Dellarocas C, Zhang X, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. Management Inform. Systems Quart. 36(2):395–426.

Dodson J, Tybout A, Sternthal B (1978) Impact of deals and deal retraction on brand switching. J. Marketing Res. 15(1):72–81.

Drossos D, Giaglis GM, Lekakos G, Kokkinaki F, Stavraki MG (2007) Determinants of effective SMS advertising: An experimental study. J. Interactive Advertising 7(2):16–27.

Duan W, Gu B, Whinston AB (2008) The dynamics of online wordof-mouth and product sales: An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Duan W, Gu B, Whinston AB (2009) Informational cascades and software adoption on the internet: An empirical investigation. Management Inform. Systems Quart. 33(1):23–48.

Entin EE, Serfaty D (1990) Information gathering and decision making under stress. Report No. TR-454, Alphatech Inc, Burlington, MA.

Eppen GD, Hanson WA, Martin RK (1991) Bundling–new products, new markets, low risk. Sloan Management Rev. 32(4):7–14.

Erdem T (1998) An empirical analysis of umbrella branding. J. Marketing Res. 35(3):339–351.

Erdem T, Sun B (2002) An empirical Investigation of the spillover effects of advertising and sales promotions in umbrella branding. J. Marketing Res. 39(4):408–420.

Erdem T, Swait J (1998) Brand equity as a signaling phenomenon. J. Consumer Psych. 7(2):131–157.

Erdem T, Winer RS (1999) Econometric modeling of competition: A multi-category choice-based mapping approach. J. Econometrics 89(1):159–175.

Feng J, Li X, Zhang X(M) (2019) Online product reviews-triggered dynamic pricing: Theory and evidence. Inform. Systems Res. 30 (4):1107–1123.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Gaeth GJ, Lewin IP, Chakraborty G, Levin AM (1991) Consumer evaluation of multi-product bundles: An information integration analysis. Marketing Lett. 2(1):47–58.

Gao G, Greenwood BN, Agarwal R, McCullough JS (2015) Vocal minority and silent majority: How do online ratings re<sup>fl</sup>ect population perceptions of quality? Management Inform. Systems Quart. 39(3):565–589.

Ghose A, Goldfarb A, Han SP (2013) How is the mobile internet different? Search costs and local activities. Inform. Systems Res. 24 (3):613–631.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Godes D, Mayzlin D (2009) Firm-created word-of-mouth communication: Evidence from a <sup>fi</sup>eld test. Marketing Sci. 28(4):721–739.

Goes PB, Lin M, Yeung CA (2014) Popularity effect in user-generated content: Evidence from online product reviews. Inform. Systems Res. 25(2):222–238

Guiltinan JP (1987) The price bundling of services: A normative framework. J. Marketing 51(2):74–85.

Ho YC, Wu J, Tan Y (2017) Discon<sup>fi</sup>rmation effect on online rating behavior: A structural model. Inform. Systems Res. 28(3):626–642.

Ho-Dac NN, Carson SJ, Moore WL (2013) The effects of positive and negative online customer reviews: Do brand strength and category maturity matter? J. Marketing 77(6):37–53.

Hong Y(K), Pavlou PA (2014) Product <sup>fi</sup>t uncertainty in online markets: Nature, effects, and antecedents. Inform. Systems Res. 25(2): 328–344.

Hu N, Pavlou PA, Zhang J (2017) On self-selection biases in online product reviews. Management Inform. Systems Quart. 41(2):449–471.

Jabr W, Zheng Z (2014) Know yourself and know your enemy: An analysis of <sup>fi</sup>rm recommendations and consumer reviews in a competitive environment. Management Inform. Systems Quart. 38(3):635–654.

Kamakura WA, Kang W (2007) Chain-wide and store-level analysis for cross-category management. J. Retailing 83(2):159–170.

Keller KL (1993) Conceptualizing, measuring, and managing consumer-based brand equity. J. Marketing 57(1):1–22.

Khern-am-nuai W, Kannan K, Ghasemkhani H (2018) Extrinsic versus intrinsic rewards for contributing reviews in an online platform. Inform. Systems Res. 29(4):871–892.

Kotler P (1997) Marketing Management, 7th ed. (Prentice Hall, Upper Saddle River, NJ).

Krishnan T, Seetharaman PB, Vakratsas D (2012) The multiple roles of interpersonal communication in new product growth. Internat. J. Res. Marketing 29(3):292–305.

Kumar V, Leone R (1988) Measuring the effect of retail store promotions on brand and store substitution. J. Marketing Res. 25(2): 178–185.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Lee D, Hosanagar K (2016) When do recommender systems work the best? Horrocks I, Zhao BY, eds. The moderating effects of product attributes and consumer reviews on recommender performance. Proc. 25th Internat. Conf. World Wide Web (International World Wide Web Conferences Steering Committee, Geneva, Switzerland), 85–97.

Lee YJ, Hosanagar K, Tan Y (2015) Do i follow my friends or the crowd? Information cascades in online movie ratings. Management Sci. 61(9):2241–2258.

Lee GM, He S, Lee J, Whinston AB (2020) Matching mobile applications for cross-promotion. Inform. Systems Res. 31(3): 865–891.

Lewis RA, Nguyen D (2015) Display advertising’s competitive spillovers to consumer search. Quant. Marketing Econom. 13(2):93–115.

Li X (2018) Impact of average rating on social media endorsement: The moderating role of rating dispersion and discount threshold. Inform. Systems Res. 29(3):739–754.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Libai B, Muller E, Peres R (2009) The role of within-brand and cross-brand communications in competitive growth. J. Marketing 73(3):19–34.

Libai B, Muller E, Peres R (2013) Decomposing the value of wordof-mouth seeding programs: Acceleration vs. expansion. J. Marketing Res. 50(2):161–176.

Lin Z, Goh KY, Heng CS (2017) The demand effects of product recommendation networks: An empirical analysis of network diversity and stability. Management Inform. Systems Quart. 41(2): 397–426.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box of<sup>fi</sup>ce revenue. J. Marketing 70(3):74–89.

Liu Y, Feng J, Liao X (2017) When online reviews meet sales volume information: Is more or accurate information always better? Inform. Systems Res. 28(4):723–743.

Lovett MJ, Peres R, Shachar R (2013) On brands and word of mouth. J. Marketing Res. 50(4):427–444.

Lu X, Ba S, Huang L, Feng Y (2013) Promotional marketing or word-of-mouth? Evidence from online restaurant reviews. Inform. Systems Res. 24(3):596–612.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and yelp review fraud. Management Sci. 62(12):3412–3427.

Luo X, Andrews M, Fang Z, Phang C (2014) Mobile targeting. Management Sci. 60(7):1738–1756.

Luo X, Zhang J, Gu B, Phang C (2017) Expert blogs and consumer perceptions of competing brands. Management Inform. Systems Quart. 41(2):371–395.

Manchanda P, Ansari A, Gupta S (1999) The “shopping basket”: A model for multicategory purchase incidence decisions. Marketing Sci. 18(2):95–114.

Maniar N, Bennett E, Hand S, Allan G (2008) The effect of mobile phone screen size on video based learning. J. Software 3(4):51–61.

Mas-Colell A, Whinston MD, Green JR (1995) Microeconomic Theory (Oxford University Press, New York).

Maslowska E, Malthouse EC, Viswanathan V (2017) Do customer reviews drive purchase decisions? The moderating roles of review exposure and price. Decision Support Systems 98 (2017):1–9.

Mudambi SM, Schuff D (2010) What makes a helpful online review? A study of customer reviews on amazon.com. Management Inform. Systems Quart. 34(1):185–200.

Mulhern FJ, Leone RP (1991) Implicit price bundling of retail products: A multiproduct approach to maximizing store pro<sup>fi</sup>tability. J. Marketing 55(4):63–76.

Nunamaker JF Jr, Applegate LM, Konsynski BR (1987) Facilitating group creativity: Experience with a group decision support system. J. Management Inform. Systems 3(4):5–19.

Oestreicher-Singer G, Sundararajan A (2012a) Recommendation networks and the long tail of electronic commerce. Management Inform. Systems Quart. 36(1):65–83.

Oestreicher-Singer G, Sundararajan A (2012b) The visible hand? Demand effects of recommendation networks in electronic markets. Management Sci. 58(11):1963–1981.

Parker P, Gatignon H (1994) Specifying competitive effects in diffusion models: An empirical analysis. Internat. J. Res. Marketing 11(1):17–39.

Pavlou PA, Dimoka A (2006) The nature and role of feedback text comments in online marketplaces: Implications for trust building, price premiums, and seller differentiation. Inform. Systems Res. 17(4):391–412.

Peres R, Van den Bulte C (2014) When to take or forgo new product exclusivity: Balancing protection from competition against word-of-mouth spillover. J. Marketing 78(2):83–100.

Rice SC (2012) Reputation and uncertainty in online markets: An experimental study. Inform. Systems Res. 23(2):436–452.

Roehm ML, Tybout AM (2006) When will a brand scandal spill over, and how should competitors respond? J. Marketing Res. 43(3):366–373.

Russell GJ, Petersen A (2000) Analysis of cross-category dependence in market basket selection. J. Retailing 76(3):367–392.

Rynes SL, Bretz RD, Gerhart B (1991) The importance of recruitment in job choice: A different way of looking. Personality Psych. 44(3): 487–521.

Seetharaman PB, Chib S, Ainslie A, Boatwright P, Chan T, Gupta S, Mehta N, Rao V, Strijnev A (2005) Models of multi-category choice behavior. Marketing Lett. 16(3-4):239–254.

Shin D, He S, Lee GM, Whinston AB, Cetintas S, Lee K-C (2020) Enhancing social media analysis with visual data analytics: A deep learning approach. Management Inform. Systems Quart. 44 (4):1459–1492.

Shocker AD, Bayus BL, Kim N (2004) Product complements and substitutes in the real world: The relevance of “other products.” J. Marketing 68(1):28–40.

Song R, Kim H, Lee GM, Jang S (2019) Does deceptive marketing pay? The evolution of consumer sentiment surrounding a pseudo-product-harm crisis. J. Bus. Ethics 158(2019):743– 761.

Susarla A, Oh JH, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. Systems Res. 23(1):23–41.

Svenson O, Edland A, Karlsson G (1985) The effect of verbal and numerical information and time stress on judgements of the attractiveness of decision alternatives. Methlie LB, Sprague R, eds. Knowledge Representation for Decision Support Systems (Elsevier Science Ltd, Amsterdam), 134–144.

Tirunillai S, Tellis GJ (2014) Mining marketing meaning from online chatter: Strategic brand analysis of big data using latent Dirichlet allocation. J. Marketing Res. 51(4):463–479.

Tsang MM, Ho SC, Liang T (2004) Consumer attitudes toward mobile advertising: An empirical study. Internat. J. Electronic Commerce 8(3):65–78.

Tversky A, Kahneman D (1991) Loss aversion in riskless choice: A reference-dependent model. Quart. J. Econom. 106(4):1039–1061.

Tversky A, Simonson I (1993) Context-dependent preferences. Man agement Sci. 39(10):1179–1189.

Walters RG (1991) Assessing the impact of retail price promotions on product substitution, complementary purchase, and interstore sales displacement. J. Marketing 55(2):17–28.

Wernerfelt B (1988) Umbrella branding as a signal of new product quality: An example of signaling by posting a bond. RAND J. Econom. 19(3):458–466.

Yin D, Bond SD, Zhang H (2014) Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews. Management Inform. Systems Quart. 38(2): 539–560.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
