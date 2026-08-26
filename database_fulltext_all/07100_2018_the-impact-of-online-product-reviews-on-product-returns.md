---
otero_id: 7100
otero_key: "5EJJ9W3T"
title: "The Impact of Online Product Reviews on Product Returns"
authors: "Nachiketa Sahoo; Chrysanthos Dellarocas; Shuba Srinivasan"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0736"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.49.5.35] On: 19 June 2018, At: 00:33 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## H4R ms Research

## Information Systems Research

![](/api/attachments/5EJJ9W3T/fulltext/images/fd0659379fae434d5f283fc9661c7c106ba4a3c822eb28eef9625aabe7ac5210.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## The Impact of Online Product Reviews on Product Returns

Nachiketa Sahoo, Chrysanthos Dellarocas, Shuba Srinivasan

Nachiketa Sahoo, Chrysanthos Dellarocas, Shuba Srinivasan (2018) The Impact of Online Product Reviews on Product Returns. Information Systems Research

Published online in Articles in Advance 15 Jun 2018

https://doi.org/10.1287/isre.2017.0736

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Impact of Online Product Reviews on Product Returns

Nachiketa Sahoo,<sup>a</sup> Chrysanthos Dellarocas,<sup>a</sup> Shuba Srinivasan<sup>a</sup>

<sup>a</sup> Questrom School of Business, Boston University, Boston, Massachusetts 02215

Contact: nachi@bu.edu, http://orcid.org/0000-0002-6827-8493 (NS); dell@bu.edu, http://orcid.org/0000-0001-6105-0130 (CD); ssrini@bu.edu, http://orcid.org/0000-0002-0024-5169 (SS)

Received: April 6, 2015 Revised: March 24, 2016; November 14, 2016; March 26, 2017 Accepted: April 11, 2017 Published Online in Articles in Advance: June 15, 2018

https://doi.org/10.1287/isre.2017.0736

Copyright: © 2018 INFORMS

Abstract. Although many researchers in information systems and marketing have studied the efect of product reviews on sales, few have looked at their efect on product returns. We hypothesize that, by reducing product uncertainty, product reviews afect the probability of product returns. We elaborate this hypothesis starting with an analytical model that examines how changes in valence and precision of information from product reviews influence the purchase and return probabilities of risk-averse, but rational, consumers. We then empirically test our hypotheses using a transaction-level data set from a multichannel, multibrand North American specialty retailer. Harnessing diferent consumers’ purchases and returns of the same products, but with varying sets of product reviews over two years, we show that the availability of more reviews and the presence of more “helpful” reviews, as voted by consumers, lead to fewer product returns—after controlling for customer, product, and other context-related factors. Analyzing the purchase behavior of the consumers, we find that when fewer product reviews are available, consumers buy more substitutes in conjunction with a product, potentially to mitigate their uncertainty. Purchase of substitutes, in turn, leads to more product returns. Finally, leveraging a discontinuity in the displayed average ratings, we find that when products are shown with an average rating that is higher than the true rating, they are returned more often. These results support the predictions of our theoretical model—unbiased online reviews indeed help consumers make better purchase decisions, leading to lower product returns; biasing reviews upward results in more returns. The presence of online reviews has important cost implications for the firm beyond the cost of reprocessing the returns; we observe that when consumers return products, they are more likely to write online reviews and that these reviews are more negative than reviews that follow a nonreturned purchase.

History: Sanjeev Dewan, Senior Editor; Wenjing Duan, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0736.

Keywords: product returns • product reviews • quality of purchase decision • regression discontinuity

## 1. Introduction

According to a recent Wall Street Journal article, one out of every three purchases at online retailers is returned (Banjo 2013). The problem is worse for shoes and fashion goods, where more than 50% of the online purchases are typically returned (Ofek et al. 2011, Flood 2013). Product returns afect the bottom line of manufacturers and retailers to the tune of over \$100 billion annually or 3.8% of their revenue.<sup>1</sup> Despite these costs, most retailers continue to ofer consumers the option to return products, to induce them to make purchases in the presence of uncertainty.

The high cost of returns has prompted retailers to provide customers with as much useful information as possible (via new technologies, such as zoom features, color swatches, alternative photos, etc.) to help them make informed purchase decisions and avoid returns (De et al. 2013). However, extant research has not yet investigated the efect of an important and increasingly prevalent source of information on product returns— namely, online product reviews. Practitioners, such as BazaarVoice, note that the presence of consumergenerated product reviews can reduce return rates by 20.4% and that product return rates decline with more reviews.<sup>2</sup> Such industry claims have not been confirmed in academic research. We fill this gap by ofering what we believe is the first academic study to address this question: Do consumer-generated product reviews lead to lower product returns?

A large literature (see Section 2) has established that online reviews increase sales. What has not been established is that reviews help consumers make better purchase decisions, as evidenced by fewer returns. A central challenge in making causal inferences related to product returns from product reviews is endogeneity: the quality of a product afects both its probability of return and the volume and content of consumer reviews that are written about it. We overcome this challenge with the help of a unique transaction-level data set from a multichannel, multibrand North American specialty retailer. Within this data, we observe the same products being purchased and returned over time. The set of reviews that are available, however, changes from purchase to purchase. This allows us to account for unobserved product heterogeneity and establish a causal link between product reviews and returns.

We propose a framework that operationalizes overall product uncertainty and its efect on product returns. We hypothesize that, by reducing the uncertainty about the products at the time of purchase, product reviews reduce their probability of the eventual return. Specifically, we posit that the higher the precision of information contained in reviews, the lower the probability of the product being returned. Next, we empirically test the predictions of our theoretical model. Our empirical results are consistent with the predictions of our theoretical model. Specifically, we find that higher review volume, lower ratings dispersion, and the presence of more reviews that have been voted as “helpful” by customers are all associated with a lower probability of return, after controlling for a variety of customer-, product-, and channel-related factors. We also find that the purchase of substitutes leads to more product returns. Leveraging a discontinuity in the displayed average ratings, we find that when products are shown with an average rating that is higher than the true rating, they are returned more often. Finally, when consumers return products, they are more likely to write online reviews that are more negative than those that follow a nonreturned purchase. Our findings suggest that, for the most part, the information contained in online reviews helps mitigate product uncertainty and leads to better purchase decisions.

The paper proceeds as follows. After a description of related work (Section 2), we propose an analytical model, based on which we ofer predictions on the impact of consumer-generated reviews on product returns (Section 3.1). Next in Section 3.2, we describe our conceptual framework and discuss the key constructs related to our propositions. In Section 4, we describe the application context, data set, and variable definitions. Then, we propose our econometric model, present our key findings, and ofer validation checks confirming the robustness of the findings (Section 5). We conclude the paper with a summary of findings and a discussion of implications for practitioners and academics (Section 6).

## 2. Overview of Related Work

There are two streams of literature that are relevant to our research focus. The first stream examines product reviews, whereas the second investigates product returns.

Over the past decade, the literatures of information systems and marketing have devoted a lot of attention to the study of online product reviews (see, for example, Dellarocas 2003 and Li and Hitt 2008). Several studies have examined the relationship between online reviews and sales. For example, in an online experiment, Senecal and Nantel (2004) find that participants who consulted product recommendations selected these products twice as often as those who did not consult recommendations. Chevalier and Mayzlin (2006) find that online consumer ratings significantly influence product sales in the market for books and that customers read review text in addition to the reviews’ summary statistics. More recently, Luca (2011) finds that a one-star increase in a restaurant’s Yelp rating leads to a 5%–9% increase in revenues.

Other studies have looked more deeply into the impact of diferent characteristics of the review on sales. Dhanasobhon et al. (2007) find that more helpful reviews and highlighted reviews have a stronger impact on sales than do other reviews. Zhu and Zhang (2010) find that the impact of reviews on sales is stronger for less-popular products and for customers who have greater Internet experience. Forman et al. (2008) find that reviews containing reviewers’ identitydescriptive information are voted as being helpful by the customers and influence sales. Archak et al. (2011) demonstrate that the text of reviews impacts sales above and beyond the corresponding numerical rating. We outline some of the prominent work studying the efect of product reviews on consumer behavior in Table 1.

The wealth of positive results on how reviews impact sales is accompanied by a dearth of results on whether reviews lead to “good” purchase decisions. In fact, several authors (Dellarocas and Wood 2008, Hu et al. 2009)have looked at sources of bias in online reviews and have speculated that such irregularities might confuse and mislead consumers. Some have attempted to provide insight into the efect of reviews on the quality of purchase decisions indirectly by examining how later reviews relate to earlier reviews for the same product, and hypothesizing that purchase mistakes tied to early reviews can explain these relationships (Li and Hitt 2008, Godes and Silva 2012). To our knowledge, no one has looked at the relationship between the body of reviews available to the consumer at the time of a given purchase decision and a relatively direct signal of that decision’s quality: whether that product was returned.

Meanwhile, a number of papers in the marketing literature have studied product returns. They have shown that consumers use the return policies of the firm to make purchase decisions (Petersen and Kumar 2009, Shah et al. 2012). Consumers value more lenient return policies, and the ability to return increases overall sales (Wood 2001). A number of marketing and product-specific variables, present at the time of purchase, afect product returns. For example, Hess and Mayhew (1997) show that return rates vary across product categories with some having return rates as high as 25% (e.g., shoes) and others having virtually no returns (e.g., socks). From a marketing-mix perspective, products purchased at lower prices (Anderson et al. 2009) and on sale (Petersen and Kumar 2009) are less likely to be returned because of the perceived value of such purchases. In a multichannel setting, retailers need to consider the cross-channel impact of product returns—e.g., purchases in an ofline store that might be returned in an online store (Ofek et al. 2011). Collectively, these papers suggest that when drawing inferences on expected demand, it is important to consider both purchases and returns to better assess the net impact on revenues.

Table 1. The Efect of Reviews on Demand and Consumer Behavior

<table><tr><td>Publication</td><td>Key data used</td><td>Focal effect</td><td>Implication for quality of purchase decision</td></tr><tr><td>Chevalier and Mayzlin (2006)</td><td>Book sales rank and reviews across Amazon and Barnes &amp; Noble</td><td>Higher ratings increase sales</td><td></td></tr><tr><td>Li and Hitt (2008)</td><td>Weekly sales rank and reviews with timestamp on Amazon</td><td>Book ratings generally decline over time; self-selection of reviewers could cause rating oscillation</td><td>Positively biased ratings by early adopters could cause purchase mistakes for later buyers</td></tr><tr><td>Forman et al. (2008)</td><td>Monthly book sales rank and reviews with reviewer identity information</td><td>Disclosure of reviewer identity information increases helpfulness of the reviews and sales</td><td>Consumers&#x27; indication that a review was helpful might improve their purchase decision making, although it is not tested</td></tr><tr><td>Zhu and Zhang (2010)</td><td>Monthly sales of games across consoles and game reviews from consumers</td><td>Reviews increase sales, by raising consumers&#x27; ex ante utility, for less popular and online products</td><td></td></tr><tr><td>Luca (2011)</td><td>Quarterly restaurant revenues and Yelp rating</td><td>Higher ratings increase revenue</td><td></td></tr><tr><td>Archak et al. (2011)</td><td>Sales rank and product reviews</td><td>Opinions within review text affect sales rank above and beyond the volume and valence of the reviews</td><td></td></tr><tr><td>Sun (2012)</td><td>Analytical results; book sales rank and reviews on Amazon and Barnes &amp; Noble</td><td>Variance in ratings increases sales of moderately rated products</td><td></td></tr><tr><td>Godes and Silva (2012)</td><td>Book reviews with timestamp on Amazon</td><td>Produced ratings increase with the age of the book and decrease with the volume of reviews</td><td>Information overload from more reviews could cause purchase mistakes—one of the explanations for a negative effect of review volume on valence of new reviews</td></tr></table>

A growing number of researchers in information systems have devoted attention to information technology (IT) artifacts that reduce product returns. Using consumer survey data, Hong and Pavlou (2014) show that participation in online product forums reduces the product fit uncertainty, whereas the use of online media on product pages reduces product quality uncertainty. Both of these activities in turn reduce product return. De et al. (2013) have studied the efect of diferent online product inspection technologies on product return. Using a data set that has detailed information on individual customers’ technology usage prior to purchase, they show that the use of an online zoom tool is associated with fewer product returns, while the use of alternative photos of a product is associated with higher product returns.

Despite the continued interest in both product returns and product reviews, we are unaware of any study that looks into the impact of online reviews on product returns. This is a significant gap in the literature because online reviews have been a primary source of product information on e-commerce sites for over two decades. Our study fills this gap.

## 3. Theoretical Framework

In this section, we develop an analytical model of a rational, but risk-averse, customer to examine how information from online product reviews afects return probabilities. From the model, we produce a set of theoretical predictions that guide our empirical analysis in Section 5. We examine the impact of two constructs on return probabilities: (1) precision of product quality and fit information, and (2) prior uncertainty of product quality and fit. Then, we discuss a set of product, product review, and contextual variables that could afect these two constructs, and through that, afect the probability of product return.

## 3.1. A Model of Product Returns

We begin by generalizing the model of purchase decision proposed by Anderson et al. (2009) to include risk-averse consumers. Given the value, $z ,$ of a product for a consumer, we assume that it yields utility according to an exponential utility function, $U ( z ) \overset { \cdot } { = }$ $( 1 - e ^ { - \alpha z } ) \bar { / } \alpha , \alpha \ge 0$ . This function describes a risk-averse consumer but converges to a risk-neutral one, $U ( z ) = z ,$ as $\alpha \to 0$ . We consider a consumer i who is contemplating whether to purchase an item $j .$ After purchase, she has the option to keep or return the item, each option producing a diferent level of value given by

$$
\begin{array}{r} z _ {i j | \mathrm{keep}} = y _ {i j} + \theta_ {i j} + \varepsilon_ {i j}, \\ z _ {i j | \mathrm{return}} = - r _ {i j}, \end{array}
$$

where $y _ { i j }$ denotes the consumer’s expected value from the quality of the product, $\theta _ { i j }$ denotes the consumer’s expected value from the fit of product j to consumer i’s taste, and $r _ { i j } \geq 0$ is the cost of returning the product.<sup>3</sup> Term $\varepsilon _ { i j }$ is a normally distributed econometric error term, capturing the consumer’s idiosyncratic need, that is known to the consumer before purchase but remains unknown to the econometrician. Its precision is normalized to one.

We assume that product quality and fit are unknown to the consumer before purchase. Each consumer has normally distributed prior beliefs about product quality. Furthermore, through prepurchase research, she obtains a signal of quality, $x _ { i j } ,$ with precision $\rho _ { i j } .$ . This signal abstracts all of the quality information that the consumer obtains by reading reviews about the product online, browsing product pages, examining the product in a retail store, etc. We assume that $x _ { i j }$ follows a normal distribution centered at the product’s true quality. The fit variable, $\theta _ { i j } ,$ captures the unique subjective dimensions of the product, whose appeal difers from one consumer to another. Each consumer, similarly, has normally distributed prior beliefs about product fit. During product research, each consumer obtains a signal of fit $\phi _ { i j }$ whose precision we denote by $\omega _ { i j } .$ . This signal abstracts all of the information that the consumer obtains about product fit by reading the text of reviews about the product online, examining the product, etc. Consumers combine their prior beliefs about quality and fit with the signals they obtain to derive posterior beliefs $y _ { i j }$ and $\theta _ { i j } ,$ respectively.

We model a forward-looking consumer who purchases only if the expected utility is positive after taking into account the probability and the cost of returns. For such a consumer, the following result is proven in Online Appendix B.

Proposition 1. If return costs are suficiently high, each of the following reduces the probability of product returns:

(i) A more precise quality signal.

(ii) A more precise fit signal.

(iii) Lower prior uncertainty about product quality.

(iv) Lower prior uncertainty about product fit.

(v) A higher valence of the quality signal.

Consequences of Incorrect Signal Interpretation. Proposition 1 assumes that customers correctly interpret the precision and valence of the various signals that are available to them. In practice, this is not always the case. Claims about a product made on a website might be overblown. Reviews might be biased (Hu et al. 2009, Mayzlin et al. 2012) and ratings rounded up to the next star or decimal point (Luca 2011). Consumers do not always perceive these irregularities before purchase (Hu et al. 2012). The following result is proven in Online Appendix B:

Proposition 2. Relative to the case when customers correctly interpret the information available to them:

(i) If they erroneously assign higher valence to a quality signal, return probabilities increase.

(ii) When return costs are suficiently high and customers suficiently risk averse, if they erroneously assign higher precision to a quality or fit signal, return probabilities increase.

Purchase and return of substitutes to mitigate uncertainty. So far, we have analyzed the purchase of only one product in isolation. However, when consumers are uncertain about the products available in an online store, which is likely when less product reviews are available, they might purchase more than one substitutable product with the intention of returning all but one that meets their need. In fact, many businesses, such as Zappos and Warby Parker, have assimilated such purchase behavior into their business model where they encourage consumers to order multiple substitutable products of which the consumer might keep only one and return the rest (Ferrell and Fraedrich 2016, Warby Parker 2017). Extending our analysis to such a scenario, we arrive at the following result (the proof is provided in Online Appendix B):

Proposition 3. In environments with both quality and fit uncertainty, unit demand consumers may find it optimal to purchase $n > 1$ substitute products with the intention of keeping the best one and returning the rest. The optimal number of substitute products to purchase is monotonically increasing with the amount of uncertainty that exists in the system.

## 3.2. Conceptual Framework

In accordance with the analytical model of Section 3.1, we propose that the overall uncertainty about a product has two components: the quality uncertainty is the consumer’s dificulty in evaluating product quality and predicting how a product will perform in the future (e.g., Dimoka et al. 2012, Ghose 2009), while the fit uncertainty is the degree to which a consumer cannot assess whether a product’s attributes match her preference (Hong and Pavlou 2014, Kwark et al. 2014). It is possible to have low (high) product quality uncertainty but high (low) fit uncertainty. For example, with clothing from a familiar retailer, the consumer may be certain about quality but may not be sure if the particular style fits her well, particularly when purchased online. Overall, both quality and fit uncertainties would drive overall product uncertainty.

Online consumers with such product uncertainties turn to online product reviews for a rich source of quality and fit information. There are two aspects to a collection of product reviews: the numeric ratings that primarily provide the product quality information and the review text that, given the quality information by the ratings, additionally provides information that can be used to assess fit.

3.2.1. Numeric Ratings as a Source of Quality Information. The average (arithmetic mean) of the ratings submitted for a product is often displayed prominently on retailer websites and used by consumers to quickly gauge the quality of the product. It is one of the most important factors in purchase decisions. However, other aspects of a collection of ratings matter as well. The standard error of a population mean is inversely proportional to the number of aggregated observations and is directly proportional to the standard deviation of those observations. Therefore, ratings from a larger number of reviews and lower dispersion (standard deviation) of the ratings should increase the precision of the quality signal that is conveyed by the average product rating. According to Proposition 1(i), either situation should decrease the probability of return.

According to Proposition 1(v), if average ratings represent a product’s true quality, higher ratings are expected to result in fewer returns. However, if the displayed average is biased upward, for example, because of noise, manipulation or rounding errors, it can lead some consumers to purchase who would not have otherwise; those purchases would be more likely to be returned when the consumers observe the true quality after purchase. This efect, captured in Proposition 2(i), predicts that the probability of product returns ought to increase when the displayed average rating is higher than the true average rating.

3.2.2. Review Text as a Source of Fit Information. Given that numeric ratings capture the vertical aspect of the value, or the quality, of the product, the additional information contained in the review text is primarily useful for consumers to assess whether the specific attributes of the product match their own unique preferences—hence, about the fit. Reviews with similar ratings can difer significantly in the amount of information their texts provide. Some could merely reinforce the numeric ratings capturing quality, whereas others could provide rich details that help consumers evaluate product fit. Retailers recognize the value of such details. Therefore, most retailers collect votes from their consumers on whether they found a review helpful and highlight the most helpful reviews on the product page. In information theory parlance, the availability of more helpful reviews that contain fit information translates to a fit signal with higher precision. Therefore, according to Proposition 1(ii), the presence of more reviews that have been designated as helpful should reduce the probability of product return.

When additional attributes about reviewers are available, making them less anonymous and more trustworthy, consumers assign higher weights to the reviews written by such reviewers (Forman et al. 2008). In information-theoretic terms, this translates to assigning a higher precision to the signals derived from the review text of such reviewers, thus influencing the posterior distribution more. One such attribute is the reviewer’s status on the review platform. Firms often reward consumers who contribute a significant amount of reviews with badges to encourage others to write reviews as well. Reviews from such more-experienced reviewers could be more reliable—or at least construed to be so. If reviews from such “top reviewers” (as designated by the retailer) indeed contribute a more precise signal of fit, it would add to the precision of the overall fit signal and, according to Proposition 1(ii), reduce the probability of return. However, if such reviews are not as precise as what consumers consider them to be, according to Proposition 2(ii), they would increase the probability of return.

3.2.3. Control Variables. There are several factors related to promotions and discounts, product return costs, and a customer’s preexisting uncertainty about a purchase that need to be controlled for to precisely measure the efect of product reviews on product returns. We discuss these factors below.

Return Cost. Sometimes retailers charge a shipping fee or restocking fee for returned items. Even when the retailer does not charge such a fee, there is some unobserved cost associated with the hassle of taking the product back to the store or packing and shipping it to the seller. This cost can be higher for bulkier products and increases with the customer’s distance from a physical store. These costs can decrease the probability of a customer returning a product even if the product does not quite meet her expectations. If the purchased product is cheap enough, a customer might not deem it worth returning considering the associated hassle cost. Therefore, factors that afect the hassle cost and the price of the product must be controlled for to accurately estimate the impact of online product reviews on product returns.

Prior Uncertainty about Quality and Fit. Certain types of products are hard to evaluate for quality and fit. Clothing items, in particular, have a large number of hard-to-describe attributes that consumers care about.

Moreover, consumers difer in their preference regarding the values of many such attributes. The dificulty in fully describing the relevant attributes of a product online could increase online consumers’ prior uncertainty about both quality and fit. According to Proposition 1(iii and iv), given the same amount and quality of product review information, we expect that these inherently complex products with high degree of quality and fit uncertainty will be returned more often.

Contextual Uncertainty. A customer’s need for a product and her levels of uncertainty could vary from one purchase to another. A firm can get some indication of this from a customer’s online activities prior to purchase. For example, if a customer is browsing many different products, it might indicate that the customer is unsure about the product she is about to purchase. On the other hand, if a customer is using keyword searches to locate a product, she might more precisely know the type of product she wants. The former is likely to increase the probability of product return, whereas the latter can decrease it. Similarly, if a customer is viewing a product online repeatedly, it might indicate that the customer is very interested in the product or has some uncertainty about the product (De et al. 2013). Such online activities prior to purchase could be used to control for the level of uncertainty the customer has at the time of purchase.

A consumer can mitigate the product quality and fit uncertainty by interacting with the product in a physical store. This interaction can generate additional quality and fit information, increasing the precision of the prepurchase signals received by the consumer. Therefore, according to Proposition 1(I and ii), products purchased in a physical store would have a lower probability of being returned. In a similar vein, consumers who primarily shop in physical stores might be more familiar with the product oferings of the retailer. By Proposition 1(iii and iv), these primarily ofline shoppers would have lower prior uncertainty about the products, and hence a lower probability of returning their purchases.

Marketing and Customer Controls. Additionally, common marketing variables (such as product price, whether the product is ofered on discount, whether the purchase was made on a holiday, etc.) and customer variables (age, gender, distance from store, frequency, and recency of purchases) could afect the probability of a product being returned. They need to be controlled for as well. Table 2 and Figure 1 summarizes the three focal constructs and how they afect the product return.

## 4. Empirical Context and Data Description

We validate the predictions of our theoretical model using a transaction-level data set from a multichannel, multibrand North American specialty retailer. This is a specialty retailer, like Gap, whose products are sold only through company-owned stores. We collect data from three brands of the company, which we refer to as brands A, B, and C. Brand $\scriptstyle \mathrm { A , }$ an upscale brand, sells women’s apparel, accessories, and decorative home items, primarily targeting women in their early 30s. Brand B sells women’s clothing and accessories targeting women in their 20s. Brand C is the flagship brand of the retailer that sells trendy apparel and accessories for men and women as well as some home furniture. Brand C targets a wider segment of female customers. The three brands are largely managed independently. They have separate websites. Each brand has hundreds of brick-and-mortar stores across the United States and Canada.

Table 2. Categorization of Variables

<table><tr><td>Constructs and variables</td><td>Hypothesized effect on return probability</td></tr><tr><td colspan="2">1. Quality information—Proposition 1(i)</td></tr><tr><td>Number of reviews</td><td>-</td></tr><tr><td>Dispersion of ratings</td><td>+</td></tr><tr><td>Average rating</td><td>-</td></tr><tr><td colspan="2">2. Fit Information—Proposition 1(ii)</td></tr><tr><td>Helpful reviews</td><td>-</td></tr><tr><td>Review length</td><td>-</td></tr><tr><td>Reviews by “top reviewers”</td><td>-</td></tr></table>

The data set was collected over two years from July 2010 to June 2012. It consists of information about products, product reviews, customers, purchases, and additional customer touch-point data such as consumer-level browsing and searching activities on the retailer’s website. Product information includes category, description, and individual reviews with time stamp. The website allows visitors to indicate whether they found a particular review to be helpful. In addition, the company designates a fraction of the reviewers as top reviewers based on the volume of reviews they have contributed. This is displayed as a badge next to each product review written by these top reviewers. The “helpful votes” and “reviewer badges” were also collected with the data set.

Our data set includes 14,000 randomly selected customers from each brand. The customer data includes age, gender, zip code, and distances to the nearest store for each brand. In addition, we have a record of the products customers browsed and online searches they performed with time stamps. All purchases and returns made by customers in the data set, whether ofline or online, are recorded as well. Such transaction data include the items purchased, price paid, promotions applied, purchase location, and whether the purchase was returned. Each promotional email sent to each of these customers was recorded with time stamps as well. Table 3 presents the key descriptive statistics of the data.

Figure 1. Conceptual Framework on How Review, Product, and Customer Characteristics Afect Product Returns  
![](/api/attachments/5EJJ9W3T/fulltext/images/dc4feb2b20c25aae51022c564154eca452168b1363e1959e179ac05d21368310.jpg)

The brands difer in their purchase and return shipping policies. Brands A and B charge a shipping fee for all online purchases, except when ofering free shipping. Brand C does not charge shipping fees for orders over a certain dollar amount. All three brands allow returns of the unused products for any reason, as well as returns of used products if they are defective. When products are returned within 30 days of purchase, the purchase price is refunded via the original method of payment. Beyond 30 days, a store credit is issued. When products are returned by mail, brands A and B charge for return shipping, whereas brand C does not. All three brands allow customers to return purchased products at a physical store without incurring any shipping or handling charges. None of the brands charge a restocking fee for returned products.

Table 3. Data Description

<table><tr><td>Brand</td><td>A</td><td>B</td><td>C</td></tr><tr><td>Customers (overlapping set, total of 42,000)</td><td>25,965</td><td>14,050</td><td>29,793</td></tr><tr><td>Products</td><td>38,706</td><td>11,863</td><td>58,502</td></tr><tr><td>Products with reviews</td><td>16,866</td><td>5,972</td><td>23,088</td></tr><tr><td>Reviews</td><td>188,019</td><td>45,469</td><td>152,143</td></tr><tr><td>Average ratings of products</td><td>4.22</td><td>4.21</td><td>4.08</td></tr><tr><td>Product views</td><td>3,407,929</td><td>1,145,285</td><td>3,548,747</td></tr><tr><td>Search</td><td>39,357</td><td>34,600</td><td>132,750</td></tr><tr><td>Purchases</td><td>550,399</td><td>79,864</td><td>423,662</td></tr><tr><td>Returns</td><td>86,931</td><td>6,378</td><td>32,603</td></tr><tr><td>Emails received by customers</td><td>3,425,126</td><td>1,750,944</td><td>5,358,220</td></tr></table>

Using this data set, we operationalize the constructs described in Section 3.2. Table 4 provides the detailed definition of these variables.

Before describing the econometric model, we show a few plots that visually depict how returns vary by product categories, distance from the store, and product reviews. Figure 2(a) shows that return rates vary substantially across categories. Although, on average, about 18% of purchases get returned, clothes, for which fit is important, are returned more often (22%) than furniture (7%), which could be more inconvenient to return. Figure 2(b) plots the average fractions

Table 4. Variable Definitions

<table><tr><td>Variable names</td><td>Description</td><td>Time-variant?</td></tr><tr><td>Product return</td><td>The dependent variable: was the purchase returned?</td><td></td></tr><tr><td>Number of reviews</td><td>Number of reviews (in 100s) available for the product at the time of purchase</td><td>Yes</td></tr><tr><td>Dispersion of ratings</td><td>Standard deviation of the ratings on the product at the time of purchase</td><td>Yes</td></tr><tr><td>Helpful reviews</td><td>Fraction of reviews on the product that are deemed helpful by consumers</td><td>Yes</td></tr><tr><td>By “top reviewers”</td><td>Fraction of reviews that are from “top reviewers,” determined by the firm based on the volume of review contribution</td><td>Yes</td></tr><tr><td>Review length</td><td>Average number of words in the reviews for product</td><td>Yes</td></tr><tr><td>Control variables</td><td></td><td></td></tr><tr><td>Category</td><td>The category of the product; one of: Accessories, Clothing, Home-and-Furniture, Miscellaneous</td><td>No</td></tr><tr><td>In-store purchase</td><td>Was the product purchased in a physical store?</td><td>Yes</td></tr><tr><td>Offline shopper</td><td>Did the consumer make more than half of her total purchases offline?</td><td>No</td></tr><tr><td>Valence of reviews</td><td>Average rating of the product at the time of purchase</td><td>Yes</td></tr><tr><td>Repeated browses</td><td>Number of times the consumer browsed the product in the two weeks leading up to the purchase</td><td>Yes</td></tr><tr><td>Keyword searches</td><td>Number of keyword searches the consumer performed in the two weeks leading up to the purchase</td><td>Yes</td></tr><tr><td>Products browsed</td><td>Number of distinct products browsed by the consumer in the two weeks leading up to the purchase</td><td>Yes</td></tr><tr><td>Retail Price</td><td>List price in USD</td><td>No</td></tr><tr><td>Discount</td><td>Price discount the customer on particular purchase, computed from the list price and the purchase price of the product</td><td>Yes</td></tr><tr><td>Holiday</td><td>Was the product purchased during a holiday week?</td><td>Yes</td></tr><tr><td>Time to purchase in years</td><td>Elapsed time since the start of the data collection to the time of purchase, to control for the time trend effect</td><td>Yes</td></tr><tr><td>Promo</td><td>Was a promotion applied to this purchase?</td><td>Yes</td></tr><tr><td>Emails</td><td>Number of emails delivered to the customer in the two weeks leading up to the purchase</td><td>Yes</td></tr><tr><td>Brand</td><td>A brand dummy</td><td>No</td></tr><tr><td>Recency</td><td>Negative of the number of days since the last purchase made by the consumer</td><td>Yes</td></tr><tr><td>Frequency (per year)</td><td>Number of products purchased by the consumer per year</td><td>No</td></tr><tr><td>Age &gt;36</td><td>Is the consumer over the age 36 (median age)?</td><td>No</td></tr><tr><td>Male</td><td>Is the consumer male?</td><td>No</td></tr><tr><td>Distance</td><td>The distance of the consumer&#x27;s home from the nearest physical store of the purchased brand</td><td>No</td></tr></table>

of products returned by customers who live at a certain distance from the store. The four bars of the figure correspond to the quartiles of the distance distribution. This figure shows that the probability of the product return decreases with the customer’s distance from the nearest store. Figure 2(c) shows the fraction of purchases returned against the average ratings of each product. Like Figure 2(b), the four bars of the figure correspond to the quartiles of the ratings distribution. We observe that returns decline as average ratings increase. Finally, in Figure 2(d) we plot, for each product, the fraction of the purchases that are returned against the total number of reviews the product has. The straight line is a simple linear model fit to the data. The solid curve is a nonparametric regression line using penalized regression splines (Fox and Weisberg 2010). We can see a decreasing trend of the fraction returned as the number of reviews on the product increases. A number of factors beyond the three shown here, such as product quality, price, etc., afect the probability of return. To get a precise estimate of the efect of variables of interest, we need a more complete econometric model that controls for all of these other factors.

## 5. Empirical Analysis

## 5.1. Econometric Model and Main Results

A key challenge in ascribing a change in product returns to the availability of product information when only a cross-sectional data set is available is that the quality of the product afects both the probability of product returns and the product reviews: good products become popular and also tend to have more and better reviews from consumers. We overcome this challenge with the help of this unique data set where we observe the same products being purchased and returned over time. The set of reviews available on the products changes from purchase to purchase. This allows us to control for unobserved product-specific characteristics that could afect the product return probabilities and to establish a causal link between the available reviews and product returns. We also observe the same consumers purchasing and potentially returning multiple times over the data collection period of two years. This, in turn, allows us to control for the consumers’ unique tendencies to return a purchase that are not explained by their observed attributes.

Figure 2. Impact of Diferent Factors of Product Returns  
(a) Return rate by product category  
![](/api/attachments/5EJJ9W3T/fulltext/images/e23860ff7e8281fd32c24aa9b67abcac6c96b204fd1d7f185866e1478f9a5367.jpg)

(c) Return rate by average rating  
![](/api/attachments/5EJJ9W3T/fulltext/images/f1f13e3d9d3d4b5230c90ec420af1a208630682f587cf3b734bbaa3fb8400b49.jpg)

To isolate the impact of online product reviews on the probability of product return, we only analyze those returns resulting from purchases where a consumer has browsed the product online before purchase. We estimate three purchase-level logistic regression models for product returns, each with a binary dependent variable indicating whether the purchased product was returned or not. We exclude purchases that have taken place in the last month of the data collection window to allow each purchase sufficient time to be returned. According to the data provider, almost all product returns take place within one month of purchase. The explanatory variables are those defined in Table 4. Several variables of interest, such as number of reviews, helpfulness of the reviews, whether the purchase occurred online or ofline, etc., vary from purchase to purchase. The three logistic regression models are as follows:

(b) Return rate by distance from store  
![](/api/attachments/5EJJ9W3T/fulltext/images/5b01a6319fbb6bd25010ead43f1497973c487a82f9bd976eb53e53987ec3dae9.jpg)

(d) Return rate by review volume  
![](/api/attachments/5EJJ9W3T/fulltext/images/dafabd2e342f4c720e80a8f4e92f4a544a0dc4aa0e079cd11b3d565e19f8b524.jpg)

$$
r e t _ {i j} ^ {t} \sim \alpha_ {j} + \sum_ {k} z _ {i j, k} ^ {t} \gamma_ {k},\tag{Model (1)}
$$

$$
r e t _ {i j} ^ {t} \sim \alpha_ {i} + \sum_ {k} z _ {i j, k} ^ {t} \gamma_ {k},\tag{Model (2)}
$$

$$
r e t _ {i j} ^ {t} \sim \alpha_ {i} + \alpha_ {j} + \sum_ {k} z _ {i j, k} ^ {t} \gamma_ {k},
$$

(Model (3))

where $r e t _ { i j } ^ { t }$ is a binary variable indicating whether consumer i returned product j that she purchased at time $t , \ \alpha _ { j }$ is the product-specific fixed intercept to control for product-specific unobserved characteristics that afects return probability, $\alpha _ { i }$ is the consumerspecific fixed intercept to control for the consumers’ unique tendencies to return after purchase, $z _ { i j , k } ^ { t }$ is the kth explanatory variable. The superscript t is used to indicate that the variables could vary from purchase to purchase (e.g. number of reviews). To control for both product- and consumer-specific unobserved heterogeneity, we estimate a third model with both productand consumer-specific fixed intercepts. The estimates from all three models are presented in Table 5.

Table 5. Model Estimates Controlling for Customer- and Product-Specific Fixed Efects

<table><tr><td rowspan="3">Variables</td><td colspan="2">(1)</td><td colspan="2">(2)</td><td colspan="2">(3)</td></tr><tr><td colspan="2">Product fixed effect</td><td colspan="2">Customer fixed effect</td><td colspan="2">Customer and product fixed effects</td></tr><tr><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td></tr><tr><td>Number of reviews</td><td>-0.1545</td><td>(0.0646)*</td><td>-0.2056</td><td>(0.0565)***</td><td>-0.2229</td><td>(0.0895)*</td></tr><tr><td>Number of  $reviews^2$ </td><td>0.0178</td><td>(0.0103)†</td><td>0.0216</td><td>(0.0093)*</td><td>0.0205</td><td>(0.0142)</td></tr><tr><td>Valence of reviews</td><td>-0.1314</td><td>(0.0254)***</td><td>-0.1401</td><td>(0.0242)***</td><td>-0.2088</td><td>(0.0374)***</td></tr><tr><td>Dispersion of ratings</td><td>0.0053</td><td>(0.0371)</td><td>0.0357</td><td>(0.0348)</td><td>0.1028</td><td>(0.0533)†</td></tr><tr><td>Helpful reviews</td><td>-0.2575</td><td>(0.0584)***</td><td>-0.1072</td><td>(0.0536)*</td><td>-0.2208</td><td>(0.0836)**</td></tr><tr><td>By “top reviewers”</td><td>0.0981</td><td>(0.0717)</td><td>-0.0617</td><td>(0.0656)</td><td>0.2028</td><td>(0.1019)*</td></tr><tr><td>Review length</td><td>0.0020</td><td>(0.0007)**</td><td>-0.0002</td><td>(0.0006)</td><td>0.0013</td><td>(0.0010)</td></tr><tr><td>Time to purchase (in years)</td><td>-0.0242</td><td>(0.0466)</td><td>-0.0141</td><td>(0.0464)</td><td>-0.0509</td><td>(0.0712)</td></tr><tr><td>In-store purchase</td><td>-0.6458</td><td>(0.0416)***</td><td>-0.9532</td><td>(0.0500)***</td><td>-1.2342</td><td>(0.0669)***</td></tr><tr><td>List price</td><td></td><td></td><td>0.0056</td><td>(0.0003)***</td><td></td><td></td></tr><tr><td>Discount</td><td>-0.3925</td><td>(0.0585)***</td><td>-0.9650</td><td>(0.0708)***</td><td>-1.0858</td><td>(0.1002)***</td></tr><tr><td>Holiday</td><td>-0.0128</td><td>(0.0341)</td><td>-0.0136</td><td>(0.0387)</td><td>0.0393</td><td>(0.0518)</td></tr><tr><td>Repeated browses</td><td>-0.0146</td><td>(0.0106)</td><td>-0.0603</td><td>(0.0120)***</td><td>-0.0754</td><td>(0.0154)***</td></tr><tr><td>Products browsed</td><td>0.0055</td><td>(0.0004)***</td><td>0.0034</td><td>(0.0006)***</td><td>0.0036</td><td>(0.0008)***</td></tr><tr><td>Keyword searches</td><td>0.0034</td><td>(0.0056)</td><td>-0.0093</td><td>(0.0073)</td><td>-0.0158</td><td>(0.0100)</td></tr><tr><td>Recency</td><td>0.0013</td><td>(0.0002)***</td><td>-0.0008</td><td>(0.0003)**</td><td>-0.0011</td><td>(0.0004)*</td></tr><tr><td>Promo</td><td>0.1752</td><td>(0.0354)***</td><td>-0.0036</td><td>(0.0436)</td><td>-0.0212</td><td>(0.0598)</td></tr><tr><td>Offline shopper</td><td>-0.4632</td><td>(0.0319)***</td><td></td><td></td><td></td><td></td></tr><tr><td>Frequency (per year)</td><td>-0.0021</td><td>(0.0003)***</td><td></td><td></td><td></td><td></td></tr><tr><td>Age &gt; 36</td><td>-0.0624</td><td>(0.0283)*</td><td></td><td></td><td></td><td></td></tr><tr><td>Male</td><td>-0.3981</td><td>(0.0627)***</td><td></td><td></td><td></td><td></td></tr><tr><td>Distance</td><td>-0.0004</td><td>(0.0001)**</td><td></td><td></td><td></td><td></td></tr><tr><td>Accessories (baseline)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Clothing</td><td></td><td></td><td>0.4158</td><td>(0.0417)***</td><td></td><td></td></tr><tr><td>Home item or furniture</td><td></td><td></td><td>-0.8364</td><td>(0.0727)***</td><td></td><td></td></tr><tr><td>Misc</td><td></td><td></td><td>0.3694</td><td>(0.1519)*</td><td></td><td></td></tr><tr><td>Brand A (baseline)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brand B</td><td></td><td></td><td>-0.4173</td><td>(0.0851)***</td><td></td><td></td></tr><tr><td>Brand C</td><td></td><td></td><td>-0.3356</td><td>(0.0709)***</td><td></td><td></td></tr><tr><td>Number of consumers</td><td>8,614</td><td></td><td>2,693</td><td></td><td>2,441</td><td></td></tr><tr><td>Number of products</td><td>3,971</td><td></td><td>7,936</td><td></td><td>3,436</td><td></td></tr><tr><td>Number of transactions</td><td>47,392</td><td></td><td>36,749</td><td></td><td>27,587</td><td></td></tr></table>

<sup>∗</sup> p < 0.05; <sup>∗∗</sup> p < 0.01; <sup>∗∗∗</sup> p < 0.001; <sup>†</sup> p < 0.1.

## 5.2. Discussion of Key Findings

We first discuss the findings around the constructs of precision of quality and fit information from online reviews; then, we discuss the efects of the control variables.

5.2.1. Information from Online Product Reviews. The number of reviews available at the time of purchase has a significant negative efect on the probability of product returns. This supports the hypothesis that the more information customers have from online reviews at the time of purchase, the lower is the probability of product return. However, there is a diminishing efect of additional reviews as seen from the quadratic term. Computing the marginal efects for the model with both consumer- and product-specific intercepts (Model (3) in Table 5), we find that, for 10 additional available reviews on a product, the probability of product return reduces by 1.01% (relative to the base probability of product return). For comparison of efect sizes, using the same model, we find that 0.1 higher average ratings leads to 0.94% lower probability of return.

The two variables that indicate the quality of reviews, Helpful reviews and By “top reviewers,” have an interesting impact on product returns. Products with reviews that are deemed helpful by other consumers are less likely to be returned, while products with reviews from company-identified top reviewers could lead to a higher probability of return. From Model (3), on computing the marginal efects, we find that a 10% increase in “helpful” reviews is associated with a 0.44% decrease in probability of return, whereas a 10% increase in reviews from “top reviewers” is associated with a 0.24% increase in the probability of return. These contrasting results suggest that, while reviews deemed helpful by peers are likely to help customers make a better purchase decision, those written by the “top reviewers,” typically determined based on their volume of contribution, result in purchases that could be returned more often than average. Therefore, these latter reviews may not provide as precise a signal of quality as consumers expect them to; highlighting them does not help either the consumer or the retailer.

Collectively, we find strong support for the predictions in Proposition 1(i) and (ii): the availability of more reviews and the presence of more reviews rated as “helpful” by peers reduce the probability of product returns. By contrast, the presence of more reviews by top reviewers seems to be associated with an increase in the probability of return. Per Proposition 2(ii), it seems that reviews written by top reviewers may not provide as reliable information for product quality as consumers may assume.

Models (1) and (3) in Table 5 control for all productspecific factors that can afect the return rate of a product, such as product quality, uncertainty of fit of a specific product, and any diference in shipping cost or policy for diferent products, since they include a product-specific intercept. Even after controlling for this unobserved product heterogeneity, we find that the time-varying average rating has a negative efect on the probability of return—i.e., when a product has a higher rating, it is less likely to be returned than when the same product has a lower rating. This could be a result of variation in product quality over time captured in changing average rating of the product, which afects the probability of return as per Proposition 2(v).

## 5.2.2. Efects of Control Variables.

Prior Uncertainty. As noted in Proposition 1(iii and iv), we expect complex product categories with subjective aspects to have higher probabilities of product return. Indeed, we find that products with lower fit uncertainty, such as furniture and home items, have a lower probability of return relative to products with higher fit uncertainty, such as clothing (Model (2) in Table 5).

Factors Afecting the Cost of Returns. Factors that afect return costs, such as a customer’s distance from the store, or the category of the products, are all controlled for in Model (3). We can obtain insight into how they afect product returns by examining Models (1) and (2). From Model (1), we find that the distance of the customer from the store has a significant negative efect on the product return. Similarly, from Model (2), we see that furniture, which is likely to be bulkier, is also less likely to be returned than accessories or clothing. Examining the efect of price from the same model, we find that more expensive items have a higher probability of being returned. For such products, the monetary value of the return could justify incurring the cost associated with the hassle of returning the products. We also find that purchases where the customer had received a discount are less likely to be returned, perhaps because of the perceived value of such purchases being higher because of the deal.

Purchase Context–Specific Uncertainty. As noted earlier, the number of diferent products that a consumer browses when contemplating a purchase can reflect the level of uncertainty of the customer at the given purchase occasion. We find that it has a positive efect on product return—i.e., the more products consumers browse before purchase, the more likely they are to return the purchased product. On the other hand, we find that repeated browsing has a negative efect on the return probability. This could be a result of the customer gathering more information about the product, which reduces the probability of return, or it could indicate a higher level of interest in the product because the customer expects more utility from this product. Both of these factors can reduce the probability of return.

In-store purchases, where the consumer has more opportunity to examine the product and get more information about product fit and quality, are less likely to be returned. As hypothesized in Section 3.2.3, we find that customers who shop predominantly ofline have lower probabilities of product return (even when they purchase online) compared with predominantly online shoppers since the former group has a greater potential to become familiar with the products given their frequent retail store visits (see Model (1) in Table 5).

## 5.3. Efect of a Valence Higher than the True Quality

Average ratings can have a powerful influence on consumers’ prepurchase expectations. According to whether they are accurate or biased signals of product quality, they can inform, but also mislead, consumers. When they are misleadingly high, they could result in a higher probability of product return (Proposition 2(i)). To test this hypothesis, we perform a regression discontinuity analysis over the true average ratings of the products at the time of purchase (Luca 2011, Anderson and Magruder 2012).

Average ratings are rounded to the first decimal place when displayed on the retailer’s website. For example, if the ratings average falls in <sup>[</sup>4.25, 4.35<sup>)</sup>, it is displayed as 4.3, but if it falls in <sup>[</sup>4.15, 4.25<sup>)</sup> it is displayed as 4.2. This allows us to compare two sets of product purchases with similar average ratings— around the “cut point” 4.25 in this example—where one was shown with a 0.1 higher rating. Since the rounding process is exogenous to other factors that afect product returns, the display of 0.1 higher average rating can be used as a random treatment to study its impact on the probability of product returns. To compare products that are of roughly equal quality, we only consider the purchases of products with average ratings within 0.03 of the cut point. We first estimate a simple model to measure the efect of this treatment by controlling for consumer and product fixed efect and the true continuous average rating

$$
r e t _ {i j} ^ {t} \sim \alpha_ {i} + \alpha_ {j} + a v \_ r a t i n g _ {i j} + d i s c o n t i n u i t y _ {i j} ^ {t}, (\text { Model   (4) })
$$

where $d i s c o n t i n u i t y _ { i j } ^ { t }$ is one if the average rating, $a v \_ r a t i n g _ { i j } ,$ , is rounded up for display; zero otherwise. The efect of discontinuity was positive and significant at 0.186 (standard error <sup></sup> 0.077). Two additional robustness checks—one with all of the variables used in Table 5 (Model (3)) and another with a quadratic term of true average rating—lead to treatment efects similar in both magnitude and significance. Falsification tests where the cut point is shifted by <sup>±</sup>0.02 remove the significance of the discontinuity. These tests, shown in Table 15 (Online Appendix C), provide evidence that the discontinuity can be used as a random treatment. The direction of the treatment efect supports Proposition 2(i): when a higher (than justified) average rating is shown, or consumers perceive a product to be of higher quality than it actually is, it increases the probability of return.

## 5.4. Purchases of Substitutes and Their Efect on Return

While shopping online, when there is uncertainty about the products being considered, customers could buy multiple substitutable products, with the intention of returning all but a few of those after direct physical evaluation. Analyzing the purchase and eventual return of such substitutes under availability of diferent amounts of information from reviews could shed light on one of the mechanisms through which higher returns occur. To examine this phenomenon, we construct the following two hypotheses:

(a) When less product information is available from online reviews—i.e., in the presence of fewer and less helpful reviews—we expect more purchase of substitutable products in an order; and

(b) When more substitutable products are purchased in an order, those products have a higher probability of being returned.

Each product in our data set has a class label associated with it: “Athletic Shoes,” “Bags/Totes,” “Belts,” “Blazers & Jackets,” etc. These are finer product groups than the categories (“Accessories,” “Clothes,” “Furniture,” etc.) shown in Table 4 and Figure 2(a). Any two products purchased in the same order that belong to the same class can be considered to be substitutes for each other. There are 173 such classes among the products in our analysis. Using these class labels, we divide the purchases in each order into groups of products that belong to unique classes.

To test the first hypothesis, we use the number of substitutes purchased in each (order, class) group, measured as the total number of products purchased in each (order, class)—1, as the dependent variable. The average of the review variables and attributes of products in each (order, class) are used as explanatory variables. We estimate a Poisson regression to examine the efect of review and product attributes on the purchase of substitutes.

To test the second hypothesis, we estimate a logistic regression model with a binary dependent variable indicating whether any of the products purchased in an (order, class) was returned. In addition to product attributes and review variables, the explanatory variables include the number of substitutable products that were purchased in that (order, class) group (Substitutes). We control for the unobserved heterogeneity of product class by using class fixed efects and for the order-specific unobservable factors that could lead to more or fewer purchases in an order by using the total number of products purchased in the order (Number of products).

We find that when there are fewer reviews available, consumers buy more substitutes (Table 6). This supports the prediction of Proposition 3. Furthermore, when they buy more substitutable products, the probability that some of them are returned is higher. In addition, when they purchase products in-store, they buy fewer substitutes. These two efects collectively suggest that, when there is less product information available, consumers could be buying more substitutes with an intention to return some of them as a way to mitigate their product uncertainty. We also observe that the efect of volume and valence of reviews on product return remain negative and significant. This implies that the efect of reviews on reducing product uncertainty goes above and beyond their efect in reducing the purchase (and return) of substitutable items.

Table 6. Purchase of Substitutable Products, and Their Efect on Return

<table><tr><td rowspan="2">Variables</td><td colspan="2">Purchase of substitutes</td><td colspan="2">Effect of substitutes on return</td></tr><tr><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td></tr><tr><td>Number of reviews</td><td>-0.0678</td><td>(0.0159)***</td><td>-0.0605</td><td>(0.0198)**</td></tr><tr><td>Valence of reviews</td><td>0.0092</td><td>(0.0137)</td><td>-0.1102</td><td>(0.0194)***</td></tr><tr><td>Helpful reviews</td><td>0.0318</td><td>(0.0304)</td><td>0.0619</td><td>(0.0447)</td></tr><tr><td>Time to purchase (in years)</td><td>-0.0334</td><td>(0.0230)</td><td>-0.0697</td><td>(0.0331)*</td></tr><tr><td>In-store purchase</td><td>-0.0539</td><td>(0.0216)*</td><td>-0.4550</td><td>(0.0315)***</td></tr><tr><td>Number of products</td><td>0.1221</td><td>(0.0015)***</td><td>-0.0187</td><td>(0.0042)***</td></tr><tr><td>List price</td><td>-0.0011</td><td>(0.0003)***</td><td>0.0025</td><td>(0.0003)***</td></tr><tr><td>Substitutes</td><td></td><td></td><td>0.4912</td><td>(0.0186)***</td></tr></table>

<sup>∗</sup>p < 0.05; <sup>∗∗</sup>p < 0.01; <sup>∗∗∗</sup>p < 0.001.

## 5.5. The Efect of Return on Subsequent Reviews

Product returns have many immediate costs for retailers: the cost of the reverse logistics, depreciation of the product when resold (if the returned product can be resold at all), etc. However, there is another significant cost that may not be immediately noticed: the potential for negative word-of-mouth following a return. Studies of review production have found that when a consumer’s experience with a product departs significantly from the expectation set up by earlier reviews, the consumer is more likely to write a review (Wu and Huberman 2008). Since product returns occur when a customer’s realized value from the product is much lower than her expectation, enough to ofset the cost of return, we hypothesize that returned purchases are more likely to be followed by a review. Such reviews are likely to be more negative than reviews that follow a nonreturned purchase. We find evidence of this in our data set among the reviews written by the customers after their purchases (Table 7).

When customers return a product, they are 35% more likely to leave a review, and those reviews are 21% more negative compared to when the product is not returned. In fact, the average ratings may not immediately convey the severity of the negative wordof-mouth. Because average ratings in the upper half of the rating scale occur more often than the lower half, a 3.6 average rating is at the 19th percentile of all of the product-browses, whereas 4.54 is at the 70th percentile. Although a small fraction of transactions result in reviews, the published reviews typically stay with the product until it is removed from the website— afecting the purchase decision of all of the online consumers afterward. Therefore, the negative word-ofmouth generated from the returned purchases has the potential to impart a much wider and enduring cost on the brand than the immediate cost of processing a return.

## 5.6. Robustness Checks

5.6.1. Efect of Free Shipping. During our data collection period, brand C ofered free shipping for orders over a certain dollar amount. This creates an incentive for consumers to add a few additional items to the order to meet the minimum requirements for free shipping. These additional items could result in more returns if the consumer did not really need them. We examine if such behavior is present and if our found efect of reviews on return are robust to such behavior. If such behavior is present, it would cause higher return among orders that are just above the free shipping requirement, compared to orders that are just under. Therefore, we start by comparing return rates for online orders that are just above the requirement for free shipping (\$FS) and those that are just under (Table 8). We examined several bands around the \$FS.

Table 7. Returned Purchases Are More Likely to be Followed by a Review, and Those Reviews Are Significantly More Negative

<table><tr><td></td><td>Average ratings</td><td>Rating probability</td><td>No. of reviews</td><td>No. of purchases</td></tr><tr><td>Not returned</td><td>4.54 (0.03)</td><td>0.009 (0.0004)</td><td>533</td><td>59,483</td></tr><tr><td>Returned</td><td>3.60 (0.11)</td><td>0.012 (0.0010)</td><td>144</td><td>11,897</td></tr></table>

Table 8. Return Rate Above and Below the Minimum for Free Shipping

<table><tr><td>Band ($)</td><td>No. of purchases in ($FS – band, $FS)</td><td>Fraction returned</td><td>No. of purchases in ($FS, FS + band)</td><td>Fraction returned</td></tr><tr><td>1</td><td>76</td><td>0.171</td><td>178</td><td>0.051</td></tr><tr><td>3</td><td>260</td><td>0.142</td><td>713</td><td>0.058</td></tr><tr><td>5</td><td>335</td><td>0.164</td><td>1,443</td><td>0.077</td></tr><tr><td>10</td><td>623</td><td>0.186</td><td>2,759</td><td>0.084</td></tr></table>

Note. This includes only the online orders of brand C, as they are the only purchases afected by free shipping.

We find that purchases in the orders just above \$FS are less likely to be returned than those in the orders that are just under the \$FS. This suggests that the outlined behavior where customers could be adding a few items to obtain free shipping and then returning most of those items, potentially in a physical store, does not seem to be prevalent with this brand. We do see that there are more purchases that are “just above” the \$FS than there are “just under” for each brand. This could be a result of consumers adding more products to the orders close to \$FS to get the free shipping—it just does not seem to lead to more returns.

To check whether our results are robust to consumers’ behavior around free shipping, we reestimate the model using only the online purchases but now adding a dummy variable (“Above”) indicating whether the order value was up to \$5 more than the \$FS. Since, the return rate in orders that are “just under” is statistically similar to all other online orders, we do not include an indicator variable for that. The results are similar to those in Table 5, suggesting that our primary results are robust to such behavior (Table 12 in Online Appendix C). As one would expect based on Table 8, whether the order is “just above” \$FS has a negative efect on the probability of return.

5.6.2. Correlated Tendency to Return in the Same Order. Consumers could purchase multiple products in one order. Since our analysis is done at the level of each product in the order, there is a possibility that the return probabilities of purchases in the same order are correlated. This could happen because of a spillover efect from one product to others in the same order. This could also happen because if the customer is returning one of the products in the order by taking it to the store or by packing it to ship back to the retailer, the hassle associated with returning other items in the same order is lower. To examine if there is an efect of a return of another product in the same order, we consider the subset of orders that contain more than one item. Each observation still corresponds to a single item in an order. Yet this time, we include an additional explanatory variable indicating whether any other item in the same order was returned (“Another return”). We find that the variable “Another return” has a significant positive efect on the probability of return, which suggests that if one product in an order is returned, the consumer is more likely to return other products in the same order (Table 13 in Online Appendix C). However, the efects of number of reviews and helpfulness of the reviews are similar to those in Table 5, thus they are robust to such correlated tendency to return.

5.6.3. Accounting for Consumers’ Experience in Purchase and Return. As customers become more experienced with the brand, their propensity to return might change. As they purchase or return more products from the brand, they could develop a better understanding of the products ofered, which could lead to better purchase decisions. On the other hand, they could become more comfortable with the process of returning the product, leading to an increasing tendency to return any single purchase. To check if the results are robust to the efect of past return experience, we include the total number of products a consumer has returned at the time of each purchase (“Total returns”). We find that when the consumer heterogeneity is controlled for by including consumer fixed efects, the efect of the total number of returns made by a consumer in the past on the return of any individual purchase is insignificant (Table 14 in Online Appendix C). The efects of the number of reviews and helpful reviews are similar to those in Table 5—the main findings are robust to the inclusion of consumers’ prior purchase experience.

5.6.4. Two-Stage Model to Account for Selection Bias. The estimated model in Section 5.1 is based on purchase events only. So, the results are valid for purchases that have already taken place. However, factors that afect the probability of return could also afect the probability of purchase. To estimate the impact of reviews on the purchase as well as the subsequent return, we estimate a two-stage probit model for both the purchase and the return decision (Heckman 1979). We construct a data set where each row corresponds to a product browse by a consumer. If the consumer purchases a product at any time after browsing the product, we note the product as purchased. If a consumer browses a product, but during the rest of the data collection period never purchases ${ \mathrm { i t } } ,$ it is noted as browsed but not purchased. The first stage of the model (selection equation) models the purchase of the browsed products. All of the variables in Table 4 were used except In-store, discount, and Promo because these variables are only available if a purchase took place. On the other hand, the Emails variable was used only in the purchase equation to impose Exclusion restriction and aid in identification (De et al. 2013). The last day of browsing for a given (consumer, product) pair was used to compute the time-variant variables. The purchase equation is the following:

$$
p _ {i j} ^ {t} = 1 \left[ \sum_ {k} z _ {i j, k} ^ {t} \gamma_ {k} + v > 0 \right],
$$

where $p _ { i j } ^ { t }$ is a binary variable indicating whether consumer i purchased product j. The superscript t indicates the time of the purchase, which is used to construct the transaction-specific time-varying explanatory variables; $z _ { i j , k } ^ { t }$ is the kth explanatory variable; v is the probit error term for the purchase model. If $p _ { i j } ^ { t } = 1$ , the product return decision (outcome equation) is given by

$$
r _ {i j} ^ {t} = 1 \left[ \sum_ {k} x _ {i j, k} ^ {t} \beta_ {k} + u > 0 \right],
$$

where $r _ { i j } ^ { t }$ is a binary variable indicating whether consumer i returned product $j , x _ { i j , k } ^ { t }$ are the explanatory variables for the outcome equation, and u is the probit error term for the product return model.

The results of the two-stage model are presented in Table 9. The efects on the product returns are consistent with the findings in Section 5.2. The twostage model also provides insights into customer purchase behavior. Products with more reviews from firm-identified “top reviewers” are more likely to be purchased, although they are not less likely to be returned. Taking into account the efect on return, a 10% increase in the number of helpful reviews (peer designated) results in 1.52% increase in net sales, whereas a 10% increase in the number of reviews from the top reviewers (firm designated) leads to only 0.2% increase in net sales. We also find that factors that are associated with higher uncertainty about products lead to lower purchase.

## 6. Summary and Implications

The efect of online reviews on sales has been widely studied, while their efect on product returns has not yet been explored in the literature. This paper ofers an information-theoretic framework that operationalizes overall product uncertainty and its efect on product returns. It utilizes a multibrand, multichannel longitudinal data set, encompassing various customer touch points, to study the efect of online product reviews on the returns of a purchased product. Our main findings are the following:

Table 9. Two-Stage Model of Purchase and Return

<table><tr><td rowspan="2">Variables</td><td colspan="2">Purchase equation</td><td colspan="2">Return equation</td></tr><tr><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td></tr><tr><td>(Intercept)</td><td>-2.2410</td><td>(0.0219)***</td><td>1.3650</td><td>(0.1900)***</td></tr><tr><td>Number of reviews</td><td>0.1697</td><td>(0.0085)***</td><td>-0.1643</td><td>(0.0214)***</td></tr><tr><td>Number of  $reviews^2$ </td><td>-0.0175</td><td>(0.0015)***</td><td>0.0169</td><td>(0.0037)***</td></tr><tr><td>Valence of reviews</td><td>0.0854</td><td>(0.0038)***</td><td>-0.1166</td><td>(0.0098)***</td></tr><tr><td>Dispersion of ratings</td><td>-0.0394</td><td>(0.0051)***</td><td>0.0257</td><td>(0.0135) $^†$ </td></tr><tr><td>Helpful reviews</td><td>0.1661</td><td>(0.0083)***</td><td>-0.1504</td><td>(0.0222)***</td></tr><tr><td>By “top reviewers”</td><td>0.0415</td><td>(0.0096)***</td><td>-0.0304</td><td>(0.0238)</td></tr><tr><td>Review length</td><td>0.0003</td><td>(0.0001)*</td><td>0.0005</td><td>(0.0003)*</td></tr><tr><td>In-store purchase</td><td></td><td></td><td>-0.2375</td><td>(0.0229)***</td></tr><tr><td>List price</td><td>-0.0019</td><td>(0.0001)***</td><td>0.0028</td><td>(0.0001)***</td></tr><tr><td>Discount</td><td></td><td></td><td>-0.2050</td><td>(0.0256)***</td></tr><tr><td>Holiday</td><td>0.0338</td><td>(0.0058)***</td><td>-0.0255</td><td>(0.0143) $^†$ </td></tr><tr><td>Repeated browses</td><td>0.1399</td><td>(0.0019)***</td><td>-0.0912</td><td>(0.0088)***</td></tr><tr><td>Products browsed</td><td>-0.0043</td><td>(0.0001)***</td><td>0.0045</td><td>(0.0002)***</td></tr><tr><td>Keyword searches</td><td>0.0239</td><td>(0.0010)***</td><td>-0.0134</td><td>(0.0029)***</td></tr><tr><td>Recency</td><td>-0.0002</td><td>(0.0000)***</td><td>0.0005</td><td>(0.0001)***</td></tr><tr><td>Emails received</td><td>0.0076</td><td>(0.0003)***</td><td>0.0562</td><td>(0.0153)***</td></tr><tr><td>Accessories (baseline)</td><td></td><td></td><td></td><td></td></tr><tr><td>Clothing</td><td>-0.0043</td><td>(0.0063)</td><td>0.1398</td><td>(0.0189)***</td></tr><tr><td>Home items or furniture</td><td>0.0411</td><td>(0.0091)***</td><td>-0.3542</td><td>(0.0336)***</td></tr><tr><td>Misc</td><td>-0.0347</td><td>(0.0256)</td><td>0.0810</td><td>(0.0605)</td></tr><tr><td>Brand A (baseline)</td><td></td><td></td><td></td><td></td></tr><tr><td>Brand B</td><td>-0.0326</td><td>(0.0086)***</td><td>-0.2027</td><td>(0.0290)***</td></tr><tr><td>Brand C</td><td>-0.1296</td><td>(0.0065)***</td><td>-0.1395</td><td>(0.0282)***</td></tr><tr><td>Frequency (per year)</td><td>0.0035</td><td>(0.0001)***</td><td>-0.0029</td><td>(0.0002)***</td></tr><tr><td>Age &gt; 36</td><td>0.0442</td><td>(0.0048)***</td><td>-0.0504</td><td>(0.0121)***</td></tr><tr><td>Male</td><td>0.0091</td><td>(0.0090)</td><td>-0.1344</td><td>(0.0273)***</td></tr><tr><td>Distance</td><td>-0.00008</td><td>(0.00001)***</td><td>-0.00006</td><td>(0.00005)</td></tr><tr><td>Offline shopper</td><td>0.0069</td><td>(0.0051)</td><td>-0.1736</td><td>(0.0176)***</td></tr><tr><td>Number of consumers</td><td>13,582</td><td></td><td></td><td></td></tr><tr><td>Number of products</td><td>12,949</td><td></td><td></td><td></td></tr><tr><td>Number of transactions</td><td>61,954</td><td></td><td></td><td></td></tr><tr><td>Number of product views</td><td>1,319,561</td><td></td><td></td><td></td></tr></table>

<sup>∗∗</sup> p < 0.01; <sup>∗∗∗</sup> p < 0.001; <sup>†</sup> p < 0.1.

• The number of reviews available at the time of purchase has a significant negative efect on the probability of return, after controlling for product quality, customer characteristics, and the context-specific customer uncertainty that might vary from one purchase occasion to another.

• Both helpful reviews and reviews by top reviewers increase sales. However, more (peer-designated) helpful reviews reduce returns, whereas more reviews by (firmdesignated) top reviewers might increase returns.

• When fewer reviews are available, consumers buy more substitutes. Furthermore, when they buy more substitutes, the probability that some of them are returned is higher. These two efects collectively suggest that, when less product information is available, consumers could be buying more substitutes, with an intention to return some of those, as a way to mitigate their uncertainty.

• When ratings are biased upward, or consumers perceive a product to be of higher quality than it actually is, it leads to a higher probability of return.

• Returned transactions are 35% more likely to be followed by a review, and those reviews are 21% more negative, relative to transactions for nonreturned products.

Our study has implications for academics, practitioners, and consumers. For academics, we contribute to an enhanced understanding of product returns, thereby quality of purchase decision, by incorporating, for the first time, the efects of online information provision in the form of reviews and their characteristics, online consumer searching and browsing, and the impact of return costs. Although there have been quite a few recent studies that have examined the impact of reviews and online search on sales, to our knowledge, no one has yet studied their impact on quality of purchase decision. Using a large and unique retailer transaction data set, we contribute new empirical findings that substantiate the insights from our proposed theoretical model of purchase and return behavior. The richness of our empirical setting allows us to establish a causal link between online product reviews and product returns.

Our study also contributes to the discourse about the reliability and usefulness of online review information for consumers. As previously discussed (see Section 2), researchers have identified several irregularities in the patterns of review provision, ranging from reporting bias to outright manipulation of reviews by firms. It has been speculated that such irregularities may mislead consumers who rely on online reviews to make purchases. Our study is the first to look at the impact of reviews on returns and thus allows us to infer whether consumers regret purchase decisions made, at least partly, based on the product reviews. We find that higher valence and volume of reviews, as well as the presence of more reviews that were judged to be “helpful” by peers, not only lead to more purchases but also to fewer returns. Therefore, at least in the context of our empirical study, reviews appear to ofer reliable and helpful product information.

For practitioners, the findings in this paper are important because they underscore the importance of providing online product reviews to consumers. Our results on two types of reviews, peer-designated helpful reviews versus firm-designated based on contribution volume of the writers, suggest that retailers should be careful when endorsing customer written reviews and, when in doubt, trust helpfulness indicators provided by other customers. Additionally, when fewer product reviews are available, consumers buy more substitutes, which leads to more product returns. With respect to prepurchase product browsing behavior, our key findings (browse of more products linked to higher return and repeated browses linked to lower return) suggest that diferent types of browsing behavior could be used as an early indicator of eventual return of the purchase. Finally, when consumers return products, they are more likely to write online reviews; these reviews are more negative than reviews that follow a nonreturned purchase; the negative word-of-mouth generated from the returned purchases has the potential to impart an unanticipated but enduring cost to the retailer. As such, a takeaway is that retailers should encourage consumers to share their experiences with products via online consumer reviews. Such proactive product information provision strategies could boost sales, reduce product return, and reduce the negative word-of-mouth that follows product returns.

## Acknowledgments

The authors are grateful to the Wharton Customer Analytics Initiative for making this data set available.

## Endnotes

<sup>1</sup> Product returns are costly for a variety of reasons: the costs of unpacking, checking the product’s condition, repacking, restocking, and issuing a refund to the customer. Often, the online retailer also agrees to pay the return shipping costs and must deal with products returned that cannot be resold.

<sup>2</sup> See, for example, “PETCO slashes return rates with BazaarVoice ratings and reviews,” http://www.businesswire.com/news/home/ 20070626005416/en/PETCO-Slashes-Return-Rates-Bazaarvoice -Ratings-Reviews.

<sup>3</sup> This specification does not explicitly include the disutility of product cost. We assume that it is factored into $y _ { i j } .$

## References

Anderson ET, Hansen K, Simester D (2009) The option value of returns: Theory and empirical evidence. Marketing Sci. 28(3): 405–423.

Anderson M, Magruder J (2012) Learning from the crowd: Regression discontinuity estimates of the efects of an online review database. Econom. J. 122(563):957–989.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Banjo S (2013) Rampant returns plague e-retailers. Wall Street Journal (December 23). allthingsd.com/20131223/rampant-returns -plague-e-retailers.

Chevalier JA, Mayzlin D (2006) The efect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

De P, Hu Y, Rahman MS (2013) Product-oriented web technologies and product returns: An exploratory study. Inform. Systems Res. 24(4):998–1010.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Dellarocas C, Wood CA (2008) The sound of silence in online feedback: Estimating trading risks in the presence of reporting bias. Management Sci. 54(3):460–476.

Dhanasobhon S, Chen P-Y, Smith M, Chen P-Y (2007) An analysis of the diferential impact of reviews and reviewers at Amazon.com. ICIS 2007 Proc. 94. http://aisel.aisnet.org/icis2007/94.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 36(2):395–426.

Ferrell OC, Fraedrich J, Ferrell L (2016) Business Ethics: Ethical Decision Making and Cases (Cengage Learning, Stamford, CT).

Flood G (2013) U.K. online retailers struggle with product returns. InformationWeek, http://www.informationweek.com/e -commerce/uk-online-retailers-struggle-with-product-returns/ d/d-id/1108423.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3):291–313.

Fox J, Weisberg S (2010) An R Companion to Applied Regression (Sage, Thousand Oaks, CA).

Ghose A (2009) Internet exchanges for used goods: An empirical analysis of trade patterns and adverse selection. MIS Quart. 33(2):263–291.

Godes D, Silva JC (2012) Sequential and temporal dynamics of online opinion. Marketing Sci. 31(3):448–473.

Heckman JJ (1979) Sample selection bias as a specification error. Econometrica 47(1):153–161.

Hess JD, Mayhew GE (1997) Modeling merchandise returns in direct marketing. J. Interactive Marketing 11(2):20–35.

Hong Y, Pavlou PA (2014) Product fit uncertainty in online markets: Nature, efects, and antecedents. Inform. Systems Res. 25(2): 328–344.

Hu N, Zhang J, Pavlou PA (2009) Overcoming the J-shaped distribution of product reviews. Comm. ACM 52(10):144–147.

Hu N, Bose I, Koh NS, Liu L (2012) Manipulation of online reviews: An analysis of ratings, readability, and sentiments. Decision Support Systems 52(3):674–684.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Luca M (2011) Reviews, reputation, and revenue: The case of Yelp.com. Working paper, Harvard Business School, Boston.

Mayzlin D, Dover Y, Chevalier J (2014) Promotional reviews: An empirical investigation of online review manipulation. Amer. Econom. Rev. 104(8):2421–2455.

Ofek E, Katona Z, Sarvary M (2011) “Bricks and clicks”: The impact of product returns on the strategies of multichannel retailers. Marketing Sci. 30(1):42–60.

Petersen JA, Kumar V (2009) Are product returns a necessary evil? Antecedents and consequences. J. Marketing 73(3):35–51.

Senecal S, Nantel J (2004) The influence of online product recommendations on consumers’ online choices. J. Retailing 80(2):159–169.

Shah D, Kumar V, Qu Y, Chen S (2012) Unprofitable cross-buying: Evidence from consumer and business markets. J. Marketing 76(3):78–95.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Warby Parker (2017) Home try-on. https://www.warbyparker.com/ home-try-on.

Wood SL (2001) Remote purchase environments: The influence of return policy leniency on two-stage decision processes. J. Marketing Res. 38(2):157–169.

Wu F, Huberman BA (2008) How public opinion forms. Papadimitriou C, Zhang S, eds. 4th Internat. Workshop Internet Network Econom., WINE 2008, Lecture Notes Comput. Sci., Vol. 5385 (Springer, Berlin), 334–341.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
