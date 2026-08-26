---
otero_id: 14808
otero_key: "ZT2SZDDK"
title: "Scores vs. stars: A regression discontinuity study of online consumer reviews"
authors: "Wenche Wang; Fan Li; Zelong Yi"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Scores vs. stars: A regression discontinuity study of online consumer reviews

Authors: Wenche Wang, Fan Li, Zelong Yi

![](/api/attachments/ZT2SZDDK/fulltext/images/706a329f7c444e76ebc255e1fbc81dafe59e9ead08e5a5cdd9333f8d297cf52a.jpg)

PII: S0378-7206(17)30054-X

DOI: https://doi.org/10.1016/j.im.2018.08.002

Reference: INFMAN 3099

To appear in: INFMAN

Received date: 22-1-2017

Revised date: 31-7-2018

Accepted date: 9-8-2018

Please cite this article as: Wang W, Li F, Yi Z, Scores vs. stars: A regression discontinuity study of online consumer reviews, Information and Management (2018), https://doi.org/10.1016/j.im.2018.08.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Scores vs. Stars: A Regression Discontinuity Study of Online Consumer Reviews

Wenche Wang, Ph.D, Assistant Professor

Sport Management, School of Kinesiology

University of Michigan

wwenche@umich.edu

1402 Washington Heights, Ann Arbor, MI, 48109

(734)-763-3292

Fan Li, Ph.D, Associate Professor

China Center for Special Economic Zone Research, Shenzhen University

lifan@szu.edu.cn

Nanhai Ave 3688, Shenzhen, Guangdong, China, 518060

+86-755-2653-0621

Zelong Yi, Ph.D, Assistant Professor

Department of Transportation Economics and Logistics Management

College of Economics, Shenzhen University

yizl@szu.edu.cn

Nanhai Ave 3688, Shenzhen, Guangdong, China, 518060

+86-755-2653-4229

Wenche Wang

Sport Management, School of Kinesiology, University of Michigan, wwenche@umich.edu

Wenche Wang is an Assistant Professor in Sport Management at the University of Michigan. She obtained her Ph.D in Economics from the University of Florida. Her research interests include electronic commerce, consumer search behavior, two-sided markets, sport analytics, economics of sports, business analytics, and antitrust policy. Her works have been published in Review of Industrial Organization, Managerial and Decision Economics, Antitrust Bulletin, and University of Miami Law Review.

## Fan Li

China Center for Special Economic Zone Research, Shenzhen University, lifan@szu.edu.cn

Fan Li is an associate professor at China Center for Special Economic Zone Research at Shenzhen University. She received her Ph.D in Economics from the University of Florida. Her research interests include the economics of information system, electronic commerce, regulatory economics, and energy economics. Her papers have been published in Decision Sciences, OMEGA, Eastern Economic Journal, China Industrial Economics, Water Resources Management, Water Policy, Reform Reference, Journal of Business and Industrial Marketing, and Economics Perspectives.

## Zelong Yi\*

\* Corresponding author.

Department of Transportation Economics and Logistics Management, College of Economics, Shenzhen University, yizl@szu.edu.cn

Zelong Yi is an Assistant Professor in the Department of Transportation Economics and Logistics Management in the College of Economics at Shenzhen University. He holds a Ph.D in Operations Management from Hong Kong University of Science and Technology. His research focuses on supply chain management, consumer behavior, and information economics. His works have been published in Production and Operations Management, Decision Sciences, OMEGA, etc.

## Abstract

#

With the rising popularity of consumer reviews, the design of the review system becomes increasingly crucial for e-commerce platforms and online retailers in their business decisionmakings. Though the relationship between consumer reviews and sales has been extensively studied, only few studies have been conducted on the effects of different review designs. In this paper, we collect detailed review data from Meituan.com, a popular Chinese shopping website, to examine the effects of numerical presentation of consumer reviews (detailed to one decimal place) and graphical presentation of consumer reviews (in half-stars) on sales. By using a regression discontinuity design, we find that while consumer review scores may affect sales positively, the star presentation can create negative, rather than positive, jumps at cutoffs. Consumers restrict their attention to a star category; therefore, the “best” sellers in a lower star category are better off than the “worst” sellers in a higher star category. The incentive for review manipulation is strongly reduced, which in the long run will create trust and confidence for the review system as well as the sellers. For those sellers that are just below the cutoffs, simply crossing over the cutoffs would not lead to higher sales. Instead, they will have to substantially improve their service quality to attract consumers.

Keywords: E-commerce; consumer review; regression discontinuity

## 1. Introduction

Consumer review systems have been widely used in online shopping websites. They allow consumers to share their experience and leave comments about the products and services. Consumer reviews are valuable information that may reduce product and service uncertainties for future customers. Sellers, therefore, can strategically establish reputation through consumer reviews (Dellarocas, 2003; Bakos and Dellarocas 2011) or use the review system as a marketing communication tool (Godes and Mayzlin, 2004; Chen and Xie, 2005, 2008; Dimoka et al., 2012; Jiang and Guo, 2015).

There is a large empirical literature on the effect of consumer reviews on sales. If consumer reviews influence sales by updating consumers’ knowledge about products and services and therefore changing their preferences, then higher review scores would improve sales (Chevalier and Mayzlin, 2006; Moretti, 2011). Negative feedbacks, on the other hand, may drive sellers out of the market (Cabral and Hortaçsu, 2010). If the role of consumer reviews is to raise awareness, then the volume of reviews, rather than the actual review scores, will have a stronger impact on sales (Godes and Mayzlin, 2004; Liu, 2006; Duan et al., 2008). In this case, even negative reviews can increase publicity for unknown sellers and therefore increase sales as well (Berger et al., 2010).

Another area of research on consumer review lies on the design of review system. Most Issues such as consumer review participation (Lu et al., 2010), information overload and conflicting reviews (Chen and Tseng, 2011), and the relationship between review ratings and review usefulness (Mudambi and Schuff, 2010; Pan and Zhang, 2011; Chua and Banerjee, 2015) have been explored. Others focus on the business strategic implication of the review design. Jiang and Guo (2015) analytically examine the design of consumer review systems, in particular, the scale rating and granular rating, as part of a firm’s business strategy.

Consumer reviews are usually presented in numerical and/or graphical forms. The former may be more precise, but the latter is more vivid to consumers. The graphical presentation of

#

consumer review is very common in online shopping websites.<sup>1</sup> It is clean and straightforward that can help consumers easily identify the quality of the product. The graphical presentation of reviews is usually in the form of stars. Most online stores present consumer reviews only in stars, such as Macy’s.com and Walmart.com, while some use reviews in both numerical and graphical presentations, such as Amazon.com, Bestbuy.com, and eBay.com.<sup>2</sup> To our best knowledge, there has yet to be any empirical work that examines the effects of different designs of review systems.

In this paper, we contribute to the consumer review literature by performing empirical analyses on two presentations of consumer reviews. We compare the effect of numerical presentation (detailed to one decimal place) to that of graphical presentation (in half-stars). A regression discontinuity approach is adopted because of the special structure of the star review system: exogenous cutoffs based on the average review scores. We find that when both score and star reviews are available to consumers, these two presentations affect sales in strikingly different ways. Though review scores may continue to have positive impact on sales, their impact is weakened because of the presence of star reviews. Moreover, our results suggest that there exist negative, rather than positive, discontinuities in sales when a seller moves up in the star category.

The different effects of the two review presentations on sales provide insights on consumers’ product selection process as well as how they process information. Graphical presentations are more interesting and therefore can quickly capture consumers’ attention. Consumers first select a star category to which they will later restrict their choices. Consumers’ decisions on which star

#

or half-star to choose may depend on their tastes, expectations, and previous shopping experience. For example, if consumers have had good experience with a 4-star store, they may only look at stores that are in the 4-star category. In the search for hotels, for instance, consumers do not necessarily always look for the 5-star hotels. Instead, they may choose among the 3-star or 3.5-star ones where they had a good stay before and which they expect to be more affordable. Once consumers decide on a star or a half-star category, they prefer stores with higher review scores to stores with lower review scores. Consequently, the highest-rated stores in a lower star category might receive larger sales than the lowest-rated stores in a higher star category. This product selection process is depicted in Figure 1. Our study provides a new explanation to a negative relationship between online reviews and sales. Other than the awareness effect, how consumers process information and thereby select product may also result in a negative impact of consumer reviews on sales.

Our surprising findings also draw important implications to the optimal consumer review design. Consumer review manipulation has been a concern on the internet market (Dellarocas, 2003; Hu et al., 2012; Mayzlin et al. 2014; Tadelis, 2016; Luca and Zervas, 2016). Our findings suggest that the incentive for review manipulation can be greatly reduced by simply adjusting the way consumer reviews are presented. If reviews are available in both numerical and graphical forms, sellers that are just below the star cutoffs would be worse off if they manipulate reviews to move to a higher star category.<sup>3</sup> Thus, there will be no incentive for the marginal sellers to write fake reviews. When review manipulation is discouraged by nature, more trust from the consumers for the review system will be established. Because sellers that are just below the cutoffs will no longer be able to take advantage of the sharp increase in stars through review manipulation, more efforts in improving product and service quality will be induced to improve sales.

![](/api/attachments/ZT2SZDDK/fulltext/images/7cd15ac0c56f15b46888b64579568c57dbcf0b17580c8e25715bc23f89abd24d.jpg)  
Figure 1. Consumers’ Product Selection Process

The rest of the paper is organized as follows. In section 2, we provide a brief description about the website, Meituan.com, from which we collected the data. We also provide summary statistics of our data. Section 3 discusses the identification strategy and tests the validity of our design. Section 4 presents the empirical results, and section 5 concludes the paper.

## 2. Data

Our data are collected from Meituan.com, a popular Chinese group buying website. <sup>4</sup> Meituan.com was founded in 2010 and has become one of the dominant group buying websites

#

in China, thus securing the largest market share. The rapid development in mobile technology in the past decade saw a shift from online shopping on desktops or laptops to the more convenient smartphone application shopping. Although Meituan.com sells promotion vouchers through both mobile application service and its website, most of its revenue is generated from its mobile application.<sup>5</sup>

Similar to Groupon.com in the U.S., service items such as restaurant vouchers and travel vouchers are particularly popular in group purchasing websites. We select Karaoke (KTV) vouchers in Shenzhen, China as our subject of study<sup>6</sup>. Compared to restaurants and tours, KTVs have a smaller degree of product differentiation and therefore receive more objective reviews. The KTV vouchers are also more standardized and can be easily categorized with observed characteristics.<sup>7</sup> We collect three sets of data: store information, promotion information, and each individual consumer review.

## 2.1. Consumer Review System on Meituan.com

Meituan.com is the first group buying website in China that allows consumers to post reviews after their purchases. Meituan.com lists every single consumer review, including both a score on a scale of 0 to 5 and the detailed text review. Meituan.com also aggregates the reviews and presents an average score along with stars associated with the average score for each store and each promotion. These aggregate statistics are shown on the search result page. In the website’s mobile application, though the score is specific to one decimal place, the stars are only specific to half-stars. As it is shown in Figure 2, a store with 4.5 average rating and a store with 4.6 average rating both receive 4.5 stars, while a store with 4.7 average rating gets 5 stars. If consumers pay closer attention to the actual score, the change of sales from a 4.5 rating store to a 4.6 rating store should not be significantly different from the change from a 4.6 rating store to a 4.7 rating store. If instead, consumers pay closer attention to the star presentation, the increase in average review score is likely to create a discontinuity in sales.

![](/api/attachments/ZT2SZDDK/fulltext/images/562b5d09bf232ed5172428bbe832b5da36902cfcd555b3295f2a04ab44ffb74c.jpg)  
Figure 2. Examples of Meituan.com Search Results

## 2.2. Summary Statistics

Our original dataset contains approximately 1.6 million consumer reviews that span 4,973 KTV promotions in 381 different KTVs. More than half of the reviews are general store reviews, while the rest are promotion-specific reviews. In terms of time horizon, our dataset spans from the date of the first KTV group purchasing promotion to the date of data collection. <sup>8</sup> In our sample, the earliest promotion ended on December 29, 2010 and the earliest consumer review was made on September 1, 2012.

Among the 4,973 group purchasing promotions in the full sample, 3367 have ended sales.<sup>9</sup> Our analyses focus on the completed promotions because the total sales can be observed<sup>10</sup>. Table 1 presents the summary statistics in KTV, promotion, and consumer levels for the sample of completed promotions. An average of 9800 number of vouchers had been sold for each KTV on Meituan.com, and the promotions enjoy a mean sale of approximately 570. This large volume of sales confirms the popularity of Meituan.com. The promotions usually grant large discounts<sup>11</sup>, averaging a striking 80%. Consumers actively participate in writing reviews; approximately 44% of the consumers left reviews for their purchases.<sup>12</sup> Overall, consumers are very satisfied with their purchases, leaving an average review score of 3.6 out of 5. Consumers also tend to provide useful reviews, reflected by the number of photos posted by the consumers, the number of words in the text review, and the number of sentences.

Table 1. Summary Statistics for the Sample of Completed Promotions

<table><tr><td></td><td>Obs.</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Store Information</td></tr><tr><td>Total Sales</td><td>352</td><td>9800.83</td><td>24010.28</td><td>0</td><td>366,571</td></tr><tr><td>Number of Reviews</td><td>352</td><td>2712.14</td><td>4739.57</td><td>0</td><td>67,104</td></tr><tr><td>Ave. Review Rating</td><td>352</td><td>3.84</td><td>0.56</td><td>3</td><td>5</td></tr><tr><td>Number of Photos</td><td>352</td><td>48.49</td><td>80.34</td><td>1</td><td>1,062</td></tr><tr><td>Self-Introduction</td><td>352</td><td>0.72</td><td>0.45</td><td>0</td><td>1</td></tr><tr><td>Chained KTV</td><td>352</td><td>0.19</td><td>0.39</td><td>0</td><td>1</td></tr><tr><td colspan="6">Promotion Information</td></tr><tr><td>Sales Price</td><td>3,367</td><td>153.26</td><td>234.30</td><td>0.01</td><td>4,999</td></tr><tr><td>Value of Promotion</td><td>3,367</td><td>757.83</td><td>868.57</td><td>26.00</td><td>32,888</td></tr><tr><td>Promotion Discount</td><td>3,367</td><td>0.80</td><td>0.16</td><td>0.07</td><td>1</td></tr><tr><td>Promotion Sales</td><td>3,367</td><td>568.28</td><td>1835.45</td><td>0.00</td><td>41,116</td></tr><tr><td>Number of Reviews</td><td>1,878</td><td>249.15</td><td>537.45</td><td>0.00</td><td>5,874</td></tr><tr><td>Average Review Score</td><td>1,878</td><td>3.60</td><td>0.74</td><td>1</td><td>5</td></tr><tr><td colspan="6">Consumer Review Information</td></tr><tr><td>Consumer Rating</td><td>1,147,915</td><td>4.09</td><td>1.11</td><td>1</td><td>5</td></tr><tr><td>No. of Photos Posted</td><td>1,148,118</td><td>1.03</td><td>1.62</td><td>0</td><td>15</td></tr><tr><td>Earnest Reviews</td><td>1,148,118</td><td>0.01</td><td>0.10</td><td>0</td><td>1</td></tr><tr><td>No. of Stores Responded</td><td>1,148,118</td><td>0.15</td><td>0.35</td><td>0</td><td>1</td></tr></table>

time of data collection. Though consumers usually write reviews during or shortly after their visit to the KTVs, there is a varying gap in time between their voucher purchases and their actual KTV visits.

<table><tr><td>Number of Words</td><td>1,148,118</td><td>21.09</td><td>26.67</td><td>1</td><td>512</td></tr><tr><td>Number of Sentences</td><td>1,148,118</td><td>1.41</td><td>1.62</td><td>0</td><td>249</td></tr><tr><td>Store Specific Review</td><td>1,148,118</td><td>0.50</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>Promotion Specific Review</td><td>1,148,118</td><td>0.33</td><td>0.47</td><td>0</td><td>1</td></tr></table>

Note: 1. Data are collected from Meituan.com.  
2. Store information statistics are based on store level, promotion information statistics are based on promotion level, and consumer review information statistics are based on individual review level. 3. Reviews are rated on a scale of 0 to 5.

The consumer review statistics presented in Table 1 are aggregated on the basis of the time of data collection; therefore, these statistics may contain reviews that were posted after the sales of the promotions ended. We calculate the average consumer rating for each promotion and its associated KTV rating at the time the promotion sale ended. The statistics are summarized in Table 2. Because a number of reviews were made after the promotion sales ended, a large number of promotions do not have an average promotion score in the sample. In particular, in the early years of the website, i.e., between 2010 and 2012, only six promotions received any review before sales ended. On the other hand, as long as a KTV has ever been reviewed, it will have an overall store rating. Most of the promotions in our sample, therefore, did have their associated KTV ratings before the end of the promotion sales.

Table 2. Calculated Average Reviews

<table><tr><td colspan="3"></td><td>Obs.</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td colspan="3">Associated KTV Average Rating</td><td>3,144</td><td>4.12</td><td>0.44</td><td>1</td><td>5</td></tr><tr><td colspan="3">Promotion Average Rating</td><td>1,801</td><td>4.10</td><td>1.05</td><td>1</td><td>5</td></tr><tr><td colspan="8">Note: 1. Each observation is a promotion.2. Average KTV rating is the average consumer reviews for the entire KTV when the promotion sale ended.3. Average promotion rating describes the average consumer review for the promotion when the promotion sale ended.</td></tr></table>

Consumers usually leave high review scores; both the average KTV rating and average promotion rating are above 4. Compared with the statistics in Table 1, consumers who wrote reviews early tend to be more satisfied with the promotions. We do, however, observe some promotions and KTVs that receive extremely low ratings. Though the final average promotion reviews better reflect the actual quality of the promotion, the reviews that were written and posted after the promotion ended have little direct impact on the demand of the current promotion. In the rest of the paper, we use the calculated consumer reviews to conduct our analyses and focus on KTV average rating rather than promotion average rating because of the larger sample size.<sup>13</sup>

## 3. Identification Strategy

Because Meituan.com’s star ratings are based on exogenous cutoffs from the average review scores, we are able to employ a regression discontinuity approach to examine the effects of the two review presentation systems. Though regression discontinuity design has been widely used in policy studies, it has only recently been applied in the literature of industrial economics and ecommerce. Anderson and Magruder (2012) and Luca (2016) both study Yelp.com’s star reviews on restaurant sales and find positive jumps at the half-star cutoffs.<sup>14</sup> While Yelp.com shows only stars to represent consumers’ evaluations, Meituan.com reports both stars and scores. Thus, we are able to capture the effects of both review presentations. Compared to the existing literature, one major advantage of our data is that we observe both sales and consumer review information from the same website. Most papers have to rely on third party sales data, which can be affected by multiple review sources. We can, therefore, more confidently draw inferences on the effects of consumer reviews on sales.

The detailed conversion from the average consumer review score to numerical and graphical presentations on Meituan.com is shown in Table 3.<sup>15</sup>

Table 3. Score to Star Conversion

<table><tr><td>Actual Average Score</td><td>Average Score (Presented)</td><td>Star</td></tr><tr><td>[4.65-5.0)</td><td>{4.7, 4.8, 4.9, 5.0}</td><td>5</td></tr><tr><td>[4.25-4.65)</td><td>{4.3, 4.4, 4.5, 4.6}</td><td>4.5</td></tr><tr><td>[3.65-4.25)</td><td>{3.7, 3.8, 3.9, 4.0, 4.1, 4.2}</td><td>4</td></tr><tr><td>[3.25-3.65)</td><td>{3.3, 3.4, 3.5, 3.6}</td><td>3.5</td></tr><tr><td>[2.65-3.25)</td><td>{2.7, 2.8, 2.9, 3.0, 3.1, 3.2}</td><td>3</td></tr><tr><td>[2.25-2.65)</td><td>{2.3, 2.4, 2.5, 2.6}</td><td>2.5</td></tr><tr><td>[1.65-2.25)</td><td>{1.7, 1.8, 1.9, 2.0, 2.1, 2.2}</td><td>2</td></tr><tr><td>[1.25-1.65)</td><td>{1.3, 1.4, 1.5, 1.6}</td><td>1.5</td></tr><tr><td>[1-1.25)</td><td>{1.0, 1.1, 1.2}</td><td>1</td></tr></table>

##

To use regression discontinuity to study the effects of consumer reviews on sales, the first step is to visualize the effects. Because promotions differ in how long they were available for sale, longer sales duration will very likely lead to larger volume of sales. Thus, we use daily sales instead of total sales to conduct our analyses. Daily sales is defined as total sales divided by sales duration. Though the sales start date is not directly observable, the start date of each voucher is a very close proxy for the date when the promotion sale began. Sales duration, measured in days, therefore, is defined as the difference between the sales end date and sales start date, which is proxied by the voucher’s valid-from date. <sup>16</sup> Because consumers generally leave very high reviews, we have very few observations for low ratings. Figure 3 provides a scatter plot of the relationship between promotion daily sales and KTV average rating for KTVs that were rated 3 or above at the time the promotion sale ended. The plot is weighted by the number of observations at given KTV ratings.

![](/api/attachments/ZT2SZDDK/fulltext/images/cf86bce8d80351ac29343cacb53441191ac5a50ea25d84763075f69603bf86aa.jpg)  
Figure 3. Scatter Plot for Daily Promotion Sales

While there appears to be a generally increasing pattern in daily sales between 3.5 and 4.25, there is an obvious downward fall at the 4.25 cutoff. The relationship between ratings and daily sales no longer looks positive between 3.25 and 3.5 or between 4.65 and 4.75. To further observe and study the effects of consumer reviews, both the numerical score and the star presentation, we graph daily sales and average consumer ratings for a smaller interval at each individual cutoff in Figure 4.

![](/api/attachments/ZT2SZDDK/fulltext/images/188bfe03e9ddf20476104e29adf455d5d0f10ed442232cf264fe4a3013a0c456.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/63c9d4a494c328241fb1767bd9829705236225e70cf910667acffa8f54275800.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/c4af6031d9c966c6b60fd0852c575cadf3e02eba52f8f1f4d6caa0b868ed3522.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/37f999f26865282dabd7c53f4cddc46bd5701fe009b6de7373d7f8116c23168c.jpg)  
Figure 4. Scatter Plot and Fitted Value for Daily Promotion Sales at Individual Cutoffs

Figure 4 provides a more straightforward depiction of the relationship between daily sales and KTV average ratings. Though consumer reviews in general positively affect daily sales, there is a surprising negative discontinuity at every cutoff. Cutoff 4.65 seems to experience the largest negative jump while at the 3.65 cutoff, the slope changes drastically. Descriptive evidence suggests an obvious negative effect of stars on sales. These descriptive findings contradict the conventional wisdom and may require sound econometric techniques to prove the significance of the effects.

## 3.1. Testing the Validity of A Regression Discontinuity Design

A common concern in a regression discontinuity design is the problem of endogenous cutoffs. There can be two types of endogeneity: Meituan.com may set the cutoffs in such a way to allow certain sellers to be on one side of the cutoffs than the other; sellers can also manipulate reviews in order to cross over the cutoffs. For the first concern, because the cutoffs are consistent across all the stores from different industries across cities in the entire country, it is unlikely that Meituan.com could set the cutoffs in such a way to favor certain sellers from the relatively small KTV industry. For the second concern, if sellers manipulate consumer reviews in order to cross over to the other side of the cutoffs, selection bias will arise and a regression discontinuity design cutoffs, there should be some discontinuities in the number of observations at the cutoffs. Figure 5 graphs the density of the KTV Rating variable. While most of the observations are in the range between 4 and 4.5, no obvious jump at the cutoffs can be visualized in the graph. We further apply the sorting test proposed by McCrary (2008), and the test statistics confirm that there is no significant jump in the density of the KTV ratings at the cutoffs 4.65, 4.25, or 3.65.<sup>17</sup> The McCrary sorting test results are presented in the Appendix.

![](/api/attachments/ZT2SZDDK/fulltext/images/e69a3ee0ac984beac1d6b6ae2f4a98156ddcd127dc2807cc147e86aa78a05c53.jpg)  
Figure 5. Density by Average KTV Rating

![](/api/attachments/ZT2SZDDK/fulltext/images/159b87df52f2a2abdd307d9921500560b54b368bb4613f7acdc4fdcd35c8e373.jpg)

One may also be concerned that it is price rather than consumer review that causes the discontinuity in sales. Thus, if there exists any discontinuity in prices at the cutoffs, the regression discontinuity design would be called into question. Figure 6 suggests that there is no such discontinuity in price. Promotions were sold at different prices with different KTV ratings. No obvious relationship can be detected between price and consumer reviews. We further graph discount and KTV rating. Again, there does not seem to be any obvious jump in prices at the star cutoffs.

![](/api/attachments/ZT2SZDDK/fulltext/images/217041588ac9daeae1e6310dfd0683bcdfc239e10ffee157e0c20ac11bca11ec.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/12741611a00904619dc1ad01fe02d24d43564bcb081bf533c58f8251a71c9029.jpg)  
Figure 6. Average Promotion Price and Discount by Average KTV Rating

## 3.2. Econometric Model

The following model is specified to test the effects of consumer reviews under two different consumer review presentation designs on promotion daily sales<sup>18</sup>:

$$
S a l e _ {i j} = \beta_ {0} + \beta_ {1} L (P r i c e _ {i j}) + \beta_ {2} I (R _ {i j t} > \bar {R}) + \beta_ {3} R _ {i j t} + \beta_ {4} R _ {i j t} \times I (R _ {i j t} > \bar {R}) + \beta_ {5} X _ {i j} + \epsilon_ {i j t}.
$$

In this specification, $S a l e _ { i j }$ is the number of vouchers sold per day for promotion ?? from KTV ?? and $P r i c e _ { i j }$ is the associated promotion price. Because KTVs may have multiple promotions ending at different times, we use subscript ?? to identify the time when the sales of the promotion ended. $R _ { i j t }$ is the average consumer review when the promotion ended at time ??. The magnitude of the discontinuities due to the star presentation is captured by the coefficient on the dummy variable $I ( R _ { i } > \bar { R } )$ . Each of the dummy variables is assigned a value of one if the average rating falls into each of the score ranges specified in Table 3. The interaction term, $R _ { i t } \times$ $I ( R _ { i t } > \bar { R } )$ allows the average rating to affect daily sales differently on either side of each cutoff. We also control for a number of promotion and KTV specific characteristics, specified as the vector $X _ { i j }$ . Promotion characteristics include the length of the promotion, whether the promotion includes food or drink<sup>19</sup>, whether the promotion can be used in the evening, on weekend, or on holidays, whether the promotion includes free Wi-Fi service and free parking, whether the voucher can be used in any other KTVs within the KTV chain, and whether it can be combined with other promotions or coupons, as well as whether reservation is required before the KTV visit. We also include the month in which the promotion ended as promotion characteristics to capture any season-specific effects. KTV characteristics include the district in which the KTV is located in, the total number of vouchers sold by time ??, whether the KTV provides a detailed description of the store on Meituan.com, the number of photos posted by the KTV on

Meituan.com, whether the KTV belongs to any KTV chain, and the number of KTVs the chain has, as well as the interaction between chain and the number of stores within the chain.

## 4. Empirical Results

In this section, we first present benchmark analyses using ordinary least squares (OLS) and weighted least squares to estimate the effect of consumer reviews on sales. We then present our main results using a regression discontinuity design based on the model specified in Section 3.2. A robustness discussion of our results is provided at the end of the section.

## 4.1.Benchmark Analyses

We first run linear regressions as comparisons for the regression discontinuity estimates. Table 4 presents the estimates from the benchmark OLS regressions for daily sales and weighted least square estimates for total sales. The benchmark analyses implicitly assume that consumers use average review scores alone to evaluate a store and a promotion. The benchmark estimates on KTV average rating are statistically significant in Column (2) but not significant in Column (1). The results do confirm that both daily sales and weighted total sales are significantly decreasing in price.

Table 4. Benchmark Least Square Regression Estimates for Sales

<table><tr><td>Variables</td><td>(1)Daily Sale</td><td>(2)Total Sales(Weighted by Sales Duration)</td></tr><tr><td>KTV Average Rating</td><td>-0.39(-0.52)</td><td>236.74*(1.94)</td></tr><tr><td>Log (Price)</td><td>-1.84***</td><td>-474.66***</td></tr><tr><td></td><td>(-7.81)</td><td>(-8.94)</td></tr><tr><td>Promotion Characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>KTV Characteristics</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>2,988</td><td>2,988</td></tr><tr><td>R-Square</td><td>0.16</td><td>0.37</td></tr></table>

Note: 1. The coefficients for the total sales analyses are obtained from weighted least square regressions. 2. T-statistics are reported in parentheses. Significance levels are denoted with asterisks: \* p<0.1, \*\*p<0.05, and \*\*\*p<0.01.

## 4.2.Main Results

Regression discontinuity analyses are performed at four cutoffs, 3.25, 3.65, 4.25, and 4.65. As a first step, we pool all the cutoffs and include the entire sample in the regression as our primary results. In the pooled estimations, the variable ???????? is defined as a discrete variable that runs from 1 to 9 to capture all nine possible star ratings.<sup>20</sup> Table 5 presents the regression discontinuity estimates at pooled cutoffs. The estimated coefficients on the cutoffs represent the impacts of additional half-stars on sales. The sum of the estimated coefficients on KTV average rating and the interaction term represent the effect of average ratings on sales, which can be different on the two sides of the cutoffs.

Table 5. Regression Discontinuity Estimated for Daily Sales at Pooled Cutoffs

<table><tr><td colspan="2">Variables</td></tr><tr><td>Log (Price)</td><td>-1.83***</td></tr><tr><td></td><td>(-9.57)</td></tr><tr><td>Star</td><td>-3.10**</td></tr><tr><td></td><td>(-2.12)</td></tr><tr><td>KTV Average Rating</td><td>0.71</td></tr><tr><td></td><td>(0.33)</td></tr><tr><td>Star×Rating</td><td>0.36</td></tr><tr><td></td><td>(1.33)</td></tr><tr><td>Promotion Characteristics</td><td>Yes</td></tr></table>

##

<table><tr><td>KTV Characteristics</td><td>Yes</td></tr><tr><td>Observations</td><td>2,988</td></tr><tr><td>R-Square</td><td>0.16</td></tr><tr><td colspan="2">Note: 1.Assignment of stars is based on cutoffs at 0.25 and 0.65.2. T-statistics are reported in parentheses. Significance levels are denoted with asterisks: * p&lt;0.1, **p&lt;0.05, and ***p&lt;0.01.</td></tr></table>

The results in Table 5 present a very different story compared to the one in Table 4. The star presentation of consumer reviews affects sales negatively. A half-star increase in store rating will decrease daily KTV voucher sales by more than three. As can be seen from the magnitudes of the estimates, the graphical presentation of consumer reviews has a stronger effect on sales than score presentation. Indeed, neither the KTV average rating nor the interaction term between star and rating is statistically significant in this specification. Pooling all the cutoffs may average out the effects from individual cutoffs resulting in insignificant effect. Thus, we turn our attention to the estimates at individual cutoffs presented in Table 6.

The subsamples for the regression discontinuity analyses at individual cutoffs are chosen with a bandwidth of 0.35 for the 4.65 and 3.65 cutoffs and a bandwidth of 0.4 for the 4.25 and 3.25 cutoffs.<sup>21</sup> Table 6 provides empirical evidence that confirms our earlier descriptive findings: moving up half a star, decreases, rather than increases a promotion’s daily sales. In general, moving from 4.5 to 5 stars results in 3.4 less sales a day (Columns 1); moving from 4 to 4.5 stars leads to 2.26 less transactions a day (Columns 2); moving from 3 to 3.5 stars decreases daily sales by a stunning 8.87 (Columns 4); and the discontinuity at the 3.65 cutoff is not statistically significant. Our results contradict with the findings of Luca (2016) and Anderson and Magruder (2012).

It is important to note that though star presentation creates negative jumps at 3 out of the 4 cutoffs, consumer review scores do not have statistically significant impact on sales except in the subsample for the 3.25 cutoff. Note that the estimate of KTV average rating is positive and statistically significant without controlling for KTV and promotion characteristics. It does become insignificant when the KTV and promotion characteristics are controlled. This suggests that KTV and promotion characteristics disentangle the positive effect of KTV rating on sales. In fact, Anderson and Magruder (2012) also find an insignificant effect of Yelp.com ratings on restaurant reservation after restaurant characteristics are controlled in the regression discontinuity design.

Table 6. Regression Discontinuity Estimates for Daily Sales at Individual Cutoffs

<table><tr><td>Variables</td><td>(1)Cutoff=4.65</td><td>(2)Cutoff=4.25</td><td>(3)Cutoff=3.65</td><td>(4)Cutoff=3.25</td></tr><tr><td>Log (Price)</td><td>-2.07***(-7.94)</td><td>-1.95***(-8.34)</td><td>-0.70***(-4.97)</td><td>-1.31**(-2.43)</td></tr><tr><td>KTV Average Rating</td><td>6.12(0.93)</td><td>5.18(1.55)</td><td>-0.23(-0.16)</td><td>28.63**(2.01)</td></tr><tr><td>5 Stars(cutoff=4.65)</td><td>-3.40*(-1.66)</td><td></td><td></td><td></td></tr><tr><td>Rating × 5 Stars</td><td>3.10(0.42)</td><td></td><td></td><td></td></tr><tr><td>4.5 Stars(cutoff=4.25)</td><td></td><td>-2.26*(-1.74)</td><td></td><td></td></tr><tr><td>Rating × 4.5 Stars</td><td></td><td>-3.37(-0.53)</td><td></td><td></td></tr><tr><td>4 Stars(cutoff=3.65)</td><td></td><td></td><td>-0.08(-0.17)</td><td></td></tr><tr><td>Rating × 4 Stars</td><td></td><td></td><td>3.80**(2.28)</td><td></td></tr><tr><td>3.5 Stars(cutoff=3.25)</td><td></td><td></td><td></td><td>-8.87***(-2.51)</td></tr><tr><td>Rating × 3.5 Stars</td><td></td><td></td><td></td><td>-30.71**(-2.02)</td></tr><tr><td>Promotion</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td colspan="5">Characteristics</td></tr><tr><td colspan="5">KTV</td></tr><tr><td>Characteristics</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>1,135</td><td>2,151</td><td>886</td><td>357</td></tr><tr><td>R-Square</td><td>0.15</td><td>0.20</td><td>0.21</td><td>0.40</td></tr></table>

Note: 1.The bandwidth for regressions (1) and (3) is 0.35 and the bandwidth for regressions (2) and (4) is 0.4. 2. T-statistics are reported in parentheses. Significance levels are denoted in asterisks: \* p<0.1, \*\*p<0.05, and \*\*\*p<0.01. 3. The average rating variable and interaction term between rating and cutoff are jointly significant in models (1) and (3) in 0.01 significance level.

#

Compared with the benchmark results in Table 4, the regression discontinuity estimates in Table 6 present a more complete story on how consumers’ reviews affect sales. By accounting the star presentation effect separately, we can obtain further insight on how consumers process information and select products.

Intuitively, one may expect that graphical presentation enhances the effect of numerical review and would lead to positive jumps at the cutoffs. Our results show that the difference between the effects of the two review presentations is beyond the scope of magnitude. The question, therefore, is why would moving up a star category decrease, rather than increase sales? To understand this result, we need to investigate how consumers process these two pieces of information. In the mobile application era, consumers are faced with thousands of selections but are subject to more restrictive time constraints. Those who use mobile apps are less likely to have time to carefully go over the details of each store and promotion to make their purchasing decisions. When both types of presentations are available, graphical presentation is more powerful due to the visualization effect. Consumers first narrow down their choices by the their previous purchasing experience. Once they restrict their attention to the stores in a certain star category, they choose a promotion based on the actual review score as well as other store and promotion characteristics. This two-stage selection process leads to the different effects of the review presentations. Unlike on Yelp.com where average review score is not readily available to consumers, the availability of both star and score presentations on Meituan.com allows consumers to conduct this two-stage selection. This is precisely why we obtain results that are different from the existing literature.

It is also worth noting that for KTVs that receive an average rating higher than 3.3, the impact of price on sales increases as the consumer review score increases. Traditionally, one may expect that consumers would be willing to pay higher prices for products of better quality, leading to smaller price effects as reviews improve. Our results, however, suggest that the price effects are stronger for higher quality products than lower quality ones. The consumers who choose a higher star range are likely to evaluate every aspect of the product more carefully than those who choose a lower star range. Thus, the increasing effect of price indeed further confirms our conclusion that consumers conduct a two-step selection based on consumer reviews.

## 4.3. Robustness Checks

We conduct several robustness checks to reinforce the validity of our results. One concern about our data is that sellers may set a limit on either time or quantity that would restrict the total number of sales. If consumer demand exceeds the quantity of the promotions supplied by the issue, we run Tobit regressions on total sales, weighted by the duration of sales at five different values of right-censoring (Amemiya, 1973).<sup>22</sup> The specification of the Tobit analyses follows our benchmark analysis presented in Table 4. The Tobit results are available in the Appendix. The estimated standard errors for the Tobit regressions are substantially larger than the estimated root mean squared error of the weighted least square regression<sup>23</sup>. This suggests that the weighted least square regression is preferred to the Tobit regressions with our data.

We also use the promotion average rating instead of the KTV average rating to perform similar analyses. The results are consistent with the results presented in Table 6.

![](/api/attachments/ZT2SZDDK/fulltext/images/4c1c4b9387a5538ca41a8d08092224480eb7e406e31ecf24c819e6bf6b7067f0.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/0e9f614b9fdbe59fd1827c340e27051f67084dc28d7443ca9315aadb9efb7885.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/93df51201a1927ab4bed4049226756704ae657ff2ea87b3c27b2c51ed022d1ab.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/af3cdc583c3e4ce548a15f3454ac15c482c2855d421767caba224a8462ff8ca5.jpg)

## Figure 7. Kernel Method – Local Linear Regression Fit for Daily Promotion Sales at Individual Cutoffs

Furthermore, we run robust bias-corrected estimations (Calonico et al., 2014) to obtain the nonparametric local-polynomial regression discontinuity treatment effect point estimates. Figure 7 below provides the graphical results of the estimates and suggests similar negative discontinuities at cutoffs 4.65, 4.25, and 3.25 as well as insignificant discontinuity at the 3.65 cutoff.<sup>24</sup> The nonparametric estimations confirm the robustness of our results. It is important to note that because a regression discontinuity design only estimates the local treatment effect and therefore relies heavily on observations very close to the cutoffs, nonparametric methods are sometimes less precise than parametric methods with a smaller sample size. Therefore, we interpret our results based on the parametric estimates shown in Table 6.

## 5. Conclusion

In this paper, we use a regression discontinuity design to study the effects of numerical presentation and graphical presentation of consumer reviews on sales. Our result shows that while consumer review scores may affect sales positively, the star presentation can create negative jumps at the cutoffs of star categories. We suggest that when consumers are exposed to both numerical and graphical presentations of reviews, they will first process the graphical information because it is more vivid and straightforward. Once they narrow down their choices, their final decisions are determined positively by the numerical review and other product characteristics.

Our findings provide very important implications for the design of consumer review system and information presentation. While existing literature documents strong evidence on the positive relationship between review scores and sales and raises concerns on the incentives for review manipulation, our results suggest that simply providing two types of presentation would reduce or even eliminate such an incentive. In a review system where only graphical presentation is available, moving up a category will allow sellers to be viewed as providing better quality products and services. More importantly, they will be treated the same as all the other sellers in the same category. Therefore, crossing over the cutoffs will benefit the sellers and create a strong incentive for them to manipulate reviews. However, when both numerical and graphical presentations are available, moving up a star category would change the seller’s ranking within the category. If consumers restrict their choices to a given group, for example, the highest rated 4-star seller would be better off than the lowest rated 4.5-star seller. The incentive for a seller to manipulate reviews is then strongly reduced. Sellers that are just below the cutoffs will no longer be able to exert minimum effort simply to cross over the cutoffs to create a substantial sales increase. More efforts to significantly improve product and service qualities to achieve larger sales will be induced or the sellers would likely lose sales.

Our results suggest that presenting both numerical and graphical reviews is more efficient than presenting graphical review alone. This presentation provides more information, and more notably, it allows consumers to conduct a two-step selection. This selection will ultimately reduce incentive to manipulate reviews which, in the long run, will lead to a greater trust and confidence for the review system as well as the sellers on the website.

Although we restrict our attention to KTV vouchers in this research, our findings provide categories. The effect identified in our paper may not be as significant for products with a high degree of differentiation and for products where review scores do not matter as much to consumers. For example, if consumers evaluate restaurants based on the photos posted by the previous consumers, then the star vs. score effect will be weakened. Similarly, for products such as video games, movies, and books that have a high degree of horizontal product differentiation, consumers may prefer to read the text reviews to get more detailed information rather than the rating scores or stars.

Anderson, M., and J. Magruder, (2012). Learning from the Crowd: Regression Discontinuity Estimates of the Effects of An Online Review Database. The Economic Journal. 122: 957-989. Bakos, Y. and C. Dellarocas, (2011). Cooperation without Enforcement? A Comparative Analysis of Litigation and Online Reputation as Quality Assurance Mechanisms. Management Science. 57(11): 1944-1962.

##

## References

Amemiya, T., (1973). Regression Analysis when the Dependent Variable is Truncated Normal. Econometrica. 41(6): 997-1016.

Anand, K.S. and R. Aron, (2003). Group Buying on the Web: A Comparison of Price Discovery Mechanisms. Management Science. 49(11): 1546-1562.

Berger, J., A.T. Sorensen, and S. J. Rasmussen, (2010). Positive Effects of Negative Publicity: When Negative Reviews Increase Sales. Marketing Science. 29(5): 815-827.

Cabral, L. and A. Hortaçsu, (2010). The Dynamics of Seller Reputation: Evidence from eBay. Journal of Industrial Economics. 58(1): 54-78.

Calonico, S., M.D. Cattaneo, and R. Titiunik, (2014). Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs. Econometrica. 82: 2295-2326.

Chen, C. and Y-D. Tseng, (2011). Quality Evaluation of Product Reviews Using an Information Quality Framework. Decision Support Systems. 50(4): 755-768.

Chen, Y. and J. Xie, (2005). Third-party Product Review and Firm Marketing Strategy.

Marketing Science. 24(2): 218-240.

Chen, Y. and J. Xie, (2008). Online Consumer Reviews: A New Element of Marketing

Communications Mix. Management Science. 54(3): 477-491.

Chevalier, J. A. and D. Mayzlin, (2006). The Effect of Word of Mouth on Sales: Online

Book Reviews. Journal of Marketing Research. 43(3):345-354.

Chua, A. and S. Banerjee, (2015). Understanding Review Helpfulness as A Function of

Reviewer Reputation, Review Rating, and Review Depth. Journal of the Association of

Information Science and Technology. 66(2): 354-362.

Dellarocas, C., (2003). The Digitization of Word of Mouth: Promise and Challenges of Online

Feedback Mechanisms. Management Science. 49(10): 1407-1424.

Dimoka, A., Y. Hong, and P.A. Pavlou, (2012). On Product Uncertainty in Online Markets:

Theory and Evidence. MIS Quarterly. 36(2): 395-426.

Duan, W., G. Gu, and A. Whinston, (2008). Do Online Reviews Matter? An Empirical

Investigation of Panel Data. Decision Support Systems. 45(4): 1007-1016.

Godes, D. and D. Mayzlin, (2004). Using Online Conversations to Study Word-of-Mouth

Communication. Marketing Science. 23(4): 545-560.

Hu, N., I. Bose, N.S. Koh, and L. Liu, (2012). Manipulation of Online Reviews: An Analysis of

Ratings, Readability, and Sentiments. Decision Support Systems. 52(3):674-684.

Imbens, G. W. and T. Lemieux (2008). Regression Discontinuity Designs: A Guide to Practice.

Journal of Econometrics. 142: 615-635.

Liu, Y. (2006). Word of Mouth for Movies: Its Dynamics and Impact on Box Office Revenue. Journal of Marketing, 70(3): 74-89.

Lu, Y., P. Tsaparas, A. Ntoulas, and L. Polanyi, (2010). Exploiting Social Context for Review Raleigh: 691-700. R

Luca, M. (2016). Reviews, Reputation, and Revenue: The Case of Yelp.com. Harvard Business School, Working Paper 12–016.

Luca, M. and G. Zervas (2016). Fake It Till You Make It: Reputation, Competition, and Yelp Review Fraud. Management Science. 62(12): 3412-3427.

Information Systems Research. 26(4): 714-730.

Mayzlin, D., Y. Dover, and J. Chevalier. (2014). Promotional Reviews: An Empirical Investigation of Online Review Manipulation. American Economic Review. 104(8): 2421-2455.

McCrary, J. (2008). Manipulation of the Running Variable in the Regression Discontinuity Design: A Density Test. Journal of Econometrics. 142(2): 698-714.

Moretti, E (2011). Social Learning and Peer Effects in Consumption: Evidence from Movie Sales, Review of Economics Studies. 78(1): 356-393.

Mudambi, S. and D. Schuff. (2010). What Makes A Helpful Online Review? A Study of Customer Reviews on Amazon.com. MIS Quarterly. 34(1): 185-200.

Pan, Y. and J. Zhang. Born Unequal: A Study of the Helpfulness of User-generated Product Reviews. Journal of Retailing. 87(4): 598-612.

Tadelis, S. (2016). Reputation and Feedback Systems in Online Platform Markets. Annual Review of Economics. 8: 321-340.

Yang, Y-C., H.K. Cheng, C. Ding, and S. Li. (2016). To Join or Not to Join Group Purchasing Organization: A Vendor’s Decision. Forthcoming European Journal of Operational Research.

## Appendix

Table A. Tobit Regression Estimates for Total Sales

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td rowspan="2">KTV Average Rating</td><td>46.91***</td><td>49.27***</td><td>64.71***</td><td>90.06***</td><td>119.73***</td></tr><tr><td>(3.75)</td><td>(3.77)</td><td>(4.01)</td><td>(4.30)</td><td>(3.70)</td></tr><tr><td rowspan="2">Log(Price)</td><td>-90.41***</td><td>-95.05***</td><td>-120.14***</td><td>-160.48***</td><td>-238.53***</td></tr><tr><td>(-21.90)</td><td>(-22.05)</td><td>(-22.75)</td><td>(-23.62)</td><td>(-23.04)</td></tr><tr><td>Promotion Characteristics</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>KTV Characteristics</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>2,988</td><td>2,988</td><td>2,988</td><td>2,988</td><td>2,988</td></tr><tr><td>Value of Right-censoring</td><td>568</td><td>602</td><td>823</td><td>1,228</td><td>2,344</td></tr><tr><td>Number of Right-censored</td><td>652</td><td>630</td><td>472</td><td>315</td><td>157</td></tr><tr><td>Pseudo R-Square</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td><td>0.04</td></tr></table>

Note: 1. The estimated results of the Tobit regressions in Columns (1) to (5) use the mean, the 80th percentile, the 85th percentile, the 90th percentile, and the 95th percentile of total sales as the right-censored values, respectively.  
2. The coefficients for the total sales analyses are weighted by the duration of sales.  
3. T-statistics are reported in parentheses. Significance levels are denoted in asterisks: \* p<0.1, \*\*p<0.05, and \*\*\*p<0.01.  
Testing Potential Sorting Problem at Cutoffs

![](/api/attachments/ZT2SZDDK/fulltext/images/2c97c36e88b81ad55fa2907654e356dfcb8ee62d65dce2d9c5e308f1e994b121.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/f6cdb4db8c58e5672cbeddf22faafd5ebd218fabccc365273d58cc012375d62d.jpg)

![](/api/attachments/ZT2SZDDK/fulltext/images/95cae1b545edd8bcef43e50b1eb626ab87cefba71a9ea9606298d810a6d5843d.jpg)  
Figure 8. McCrary Sorting Test

![](/api/attachments/ZT2SZDDK/fulltext/images/c448226a885d7f772219d382f114e9c2c506308178ca95ed43a715889db147ee.jpg)

The top two graphs as well the left graph on the bottom show that the log differences in the density below and above the cutoffs are small and statistically insignificant. This provides statistical evidence that there is no sorting problem at the cutoffs and confirms the validity of the regression discontinuity design. The last graph, however, suggests a significant log difference. This result is likely to be due to the small number of observations on the lefthand side of the cutoffs. There are only 90 observations on the left-hand side of the cutoff but 292 observations on the right-hand side of the cutoff based on a 0.4 bandwidth. More generally, there are only 116 promotions that receive an average rating at 3.25 or below.
