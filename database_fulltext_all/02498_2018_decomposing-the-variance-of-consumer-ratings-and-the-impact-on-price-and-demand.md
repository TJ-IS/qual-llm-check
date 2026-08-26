---
otero_id: 2498
otero_key: "QY4572H4"
title: "Decomposing the Variance of Consumer Ratings and the Impact on Price and Demand"
authors: "Steffen Zimmermann; Philipp Herrmann; Dennis Kundisch; Barrie R. Nault"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0764"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [185.216.93.30] On: 11 December 2018, At: 16:34 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/QY4572H4/fulltext/images/56173a5713b69f707e4c86668b2178c50ecba7ff2933a146e79e05f82336aa46.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Decomposing the Variance of Consumer Ratings and the Impact on Price and Demand

Steffen Zimmermann, Philipp Herrmann, Dennis Kundisch, Barrie R. Nault

To cite this article: Steffen Zimmermann, Philipp Herrmann, Dennis Kundisch, Barrie R. Nault (2018) Decomposing the Variance of Consumer Ratings and the Impact on Price and Demand. Information Systems Research

Published online in Articles in Advance 11 Dec 2018

https://doi.org/10.1287/isre.2017.0764

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Decomposing the Variance of Consumer Ratings and the Impact on Price and Demand

Stefen Zimmermann,<sup>a</sup> Philipp Herrmann,<sup>b</sup> Dennis Kundisch,<sup>b</sup> Barrie R. Nault<sup>c</sup>

<sup>a</sup> School of Management, University of Innsbruck, 6020 Innsbruck, Austria; <sup>b</sup> Faculty of Business and Economics, Paderborn University, 33098 Paderborn, Germany; <sup>c</sup> Haskayne School of Business, University of Calgary, Calgary, Alberta T2N 1N4, Canada Contact: stefen.zimmermann@uibk.ac.at, http://orcid.org/0000-0003-4619-0228 (SZ); philipp\_herrmann@hotmail.de (PH); dennis.kundisch@wiwi.uni-paderborn.de (DK); nault@ucalgary.ca, http://orcid.org/0000-0001-7856-885X (BRN)

Received: August 27, 2016 Revised: July 20, 2017; October 10, 2017 Accepted: October 12, 2017 Published Online in Articles in Advance: December 11, 2018

https://doi.org/10.1287/isre.2017.0764

Copyright: © 2018 INFORMS

Abstract. Consumer ratings play a decisive role in purchases by online shoppers. Although the efects of the average and the number of consumer ratings on future product pricing and demand have been studied with some conclusive results, the efects of the variance of these ratings are less well understood. We develop a model where we decompose the variance of consumer ratings into two sources: taste diferences about search and experience attributes of a durable good, and quality diferences among instances of this good in the form of product failure. We find that (i) optimal price increases and demand decreases in variance caused by taste diferences, (ii) optimal price and demand decrease in variance caused by quality diferences, and (iii) when holding the average rating as well as the total variance constant, for products with low total variance, both price and demand increase in the relative share of variance caused by taste diferences. Counter to intuition, we demonstrate that risk-averse consumers may prefer a higher-priced product with a higher variance in ratings when deciding between two similar products with the same average rating.

History: Dr. Giri Kumar Tayi, Senior Editor; Dr. Marius (Florin) Niculescu, Associate Editor. Funding: This work was partially supported by the German Research Foundation within the Collaborative Research Centre On-The-Fly Computing [SFB 901/2] and by the Social Sciences and Humanities Research Council of Canada.

Keywords: consumer rating • variance • taste diferences • quality diferences • e-commerce

## 1. Introduction

Most products on the market can be described by search and experience attributes (Nelson 1981). Search attributes can be determined by inspection or by examining product specifications from the manufacturer without the necessity of use (Shapiro 1983). Examples of search attributes for a set of headphones are the color or technical features such as active noise cancellation. In contrast, experience attributes, such as the wearing comfort or the sound characteristics of headphones, can hardly be known before using a product (Klein 1998, Nelson 1981, Wei and Nault 2013). Through Web 2.0, the need to use a product to assess experience attributes has fundamentally changed due to consumer ratings gathered and presented on e-commerce platforms. In particular, consumer ratings ofer a form of peer learning, also called electronic word of mouth (see, e.g., Dellarocas 2003), among consumers by enabling prospective consumers to learn from other consumers’ experiences (Wu et al. 2015). Consequently, experience attributes are transformed by consumer ratings into attributes that can be searched. Thus, prospective consumers can learn how a given product performs on experience attributes by examining consumer ratings without the necessity of use (Chen and Xie 2008, Hong et al. 2012, Kwark et al. 2014). An example is the sound characteristics of headphones. Without consumer ratings, assessing this attribute requires using the actual device. By having consumer ratings available, the sound characteristics of headphones can be inferred from the experiences of other consumers (e.g., whether a specific type of headphones have a strong or a light bass).

Even if consumers can infer experience attributes from consumer ratings, there still remains uncertainty if products are characterized by inconsistent quality (i.e., inconsistent quality goods). Inconsistent quality goods are characterized by the fact that for some instances of a product, the quality of search and experience attributes deviates from the intended quality. Such inconsistent quality can be observed by browsing through consumer ratings. For instance, by browsing through consumer ratings of a specific type of headphones (see Amazon 2015), consumers can observe that for some instances the cord broke after a relatively short period of use, while for other instances it did not break. This means that consumers can make inferences from consumer ratings about the probability of product failure. What they cannot learn from consumer ratings is whether their individual instance of the product (i.e., the actual set of headphones they buy) will fail. Thus, the actual quality of an individual instance of an inconsistent quality good—regardless of the number of available ratings—cannot be determined through examining consumer ratings. The distinctions we make between diferent types of products and their attributes are shown in Table 1.

Table 1. Diferent Types of Products and Product Attributes

<table><tr><td>Attribute type</td><td>Definition</td><td>Consistent quality goods</td><td>Inconsistent quality goods</td></tr><tr><td>Search attributes</td><td>The set of attributes that can be determined without product use through examining the product specifications provided by the manufacturer</td><td>The quality of search attributes is consistent among instances of a consistent quality good (i.e., search attributes do not fail).</td><td>The quality of search attributes differs among instances of an inconsistent quality good (i.e., search attributes may fail).</td></tr><tr><td>Experience attributes</td><td>The set of attributes that can be determined only through product use. As soon as meaningful consumer ratings are available, these attributes can be determined without use through examining these ratings.</td><td>The quality of experience attributes is consistent among instances of a consistent quality good (i.e., experience attributes do not fail).</td><td>The quality of experience attributes differs among instances of an inconsistent quality good (i.e., experience attributes may fail).</td></tr></table>

As consumer ratings help consumers “to mitigate the uncertainty about the quality of a product and about its fit to consumers’ needs” (Kwark et al. 2014, p. 93), it is not surprising that 90% of all purchase decisions are influenced by consumer ratings (Drewnicki 2013) and the most popular feature of Amazon.com is its consumer ratings (Harmon 2004). Consumer ratings are most commonly provided in the form of a star (or comparable numerical) rating (indicating the valence of the consumer rating) and a textual review. The information contained in the textual reviews is summarized by the star rating system, typically ranging from one (lowest rating) to five (highest rating) on most e-commerce websites. Bar charts often show the distribution of the star ratings, with the average rating displayed prominently beneath the product name (e.g., on Amazon.com, Bestbuy.com, Target.com, and Walmart.com). Thus, consumers can see at a glance the average rating from other consumers and the extent to which opinions about the product difer (variance). Elements of this variance can be caused by taste diferences about search and experience attributes such as the color or the sound of headphones (i.e., some consumers like the color or the sound while others do not), or by quality diferences among instances of a product in the form of product failure (i.e., some instances of the considered headphones fail, while others do not).

Among the literature that has recently emerged on consumer ratings, several studies find that both the absolute number of posted consumer ratings and the average consumer rating increase demand. Fewer studies (e.g., Clemons et al. 2006, Hong et al. 2012,

Sun 2012) explicitly analyze the efect of the variance of online consumer ratings on price and demand, and, to the best of our knowledge, none explicitly decomposes the variance into diferent sources. This is important because what information is encoded in this variance is still an open research question (Markopoulos and Clemons 2013).

We consider durable goods where variance in consumer ratings can be caused by taste and quality diferences to answer the following research question: Does the variance of consumer ratings caused by taste diferences and quality diferences diferentially afect price and demand?

To determine the efects of the diferent sources of variance of consumer ratings on price and demand, we construct a model featuring a monopoly retailer and consumers that difer in taste and risk aversion. We analyze two types of durable goods (see Table 1).

1. Consistent quality goods. To connect with the existing literature, in particular with Sun (2012), we analyze consistent quality goods, where the variance of consumer ratings is solely caused by taste diferences.

2. Inconsistent quality goods. More importantly, we analyze inconsistent quality goods, where the variance of consumer ratings is caused by taste diferences and quality diferences in the form of product failure.

Our analysis yields the following main results: First, a higher variance caused by taste diferences always signals that a product is liked by some consumers but less liked by others and results in a higher price and lower demand. Second, a higher variance caused by quality diferences signals that there is higher failure risk associated with the product, resulting in a lower price and lower demand. Third, holding the average rating and the total variance constant, increasing the relative share of variance caused by taste diferences may lead to an increase in both price and demand. Through this mechanism, price and demand can increase with an increasing total variance. We demonstrate, therefore, that risk-averse consumers may prefer a higher-priced product with a higher total variance in ratings when deciding between two similar products with the same average rating.

## 2. Related Literature

A substantial portion of the related literature on the efects of consumer ratings empirically examines the efects of average consumer ratings and the number of consumer ratings on sales of products from diferent product categories. A more comprehensive review of this portion of related literature can be found in Babic Rosario et al. (2016). In summary, some authors have found that an increase in average ratings has a positive efect on the sales of books (e.g., Chevalier and Mayzlin 2006, Sun 2012, Li and Hitt 2008), hotel bookings (e.g., Ye et al. 2011), and movies (e.g., Dellarocas et al. 2007), whereas others fail to find such an efect both for books (e.g., Chen et al. 2004) and for movies (e.g., Duan et al. 2008). For the total number of ratings, the literature shows a positive efect on sales (e.g., Chen et al. 2004, Chevalier and Mayzlin 2006, Duan et al. 2008), whereas Godes and Mayzlin (2004) do not find any such efect.

There are several studies that find consumer ratings impact prices, mostly in service industries. In the hotel industry, Lewis and Zervas (2016) find high-rated hotels increase prices and low-rated hotels decrease prices. In online accommodation sharing—Airbnb— prices have been found to increase after an accumulation of positive ratings, where the positive ratings are understood to establish good reputations (Gutt and Herrmann 2015; Ikkala and Lampinen 2014, 2015; Teubner et al. 2017). For a sample of Chicago restaurants, Bai et al. (2017) found that local restaurants with high ratings and a high number of reviews were more likely to initiate daily deals. There is also speculation that the addition of consumer reviews of airlines on TripAdvisor may lead to higher customer willingness to pay for a seat rated as excellent (Economist 2016).

Fewer studies have empirically studied the efect of the variance of consumer ratings on prices and sales (Babic Rosario et al. 2016), and the results are inconclusive. Clemons et al. (2006) find that the variance of consumer ratings is associated with higher growth in sales in hyperdiferentiated markets such as the craft beer industry. Taking the number of published reviews as a proxy for sales, Lu et al. (2014) also find a significant positive correlation between the variance of consumer ratings and sales of hotel rooms via online travel agencies. In contrast, Ye et al. (2009) find a significant negative correlation, and Ye et al. (2011) find no significant correlation between the variance of consumer ratings and hotel bookings. Also Chintagunta et al. (2010) do not find a significant correlation between sales and the variance of consumer ratings for movie box ofice sales. In an experiment and in an empirical study using data from Amazon and eBay from products in the electronics category, Wu et al. (2013) find that if a consumer is risk averse toward product uncertainty, then a consumer’s willingness to pay for a product with a higher variance of consumer ratings is lower.

One of the very few studies that analyze the efects of the variance of consumer ratings on sales analytically is that by Hong et al. (2012). The authors distinguish search and experience products and find that, for a pure search product, when the number of consumer ratings increases, the variance of ratings decreases. In contrast, for a product that is primarily characterized by experience attributes, when the number of consumer ratings increases, the variance of ratings may increase depending on how dominant these experience attributes are.

Most closely related to our approach, Sun (2012) analytically models the informational role of the variance of consumer ratings in price and demand. In this model, consumers are risk neutral, and all products can be described by product quality and mismatch costs. Products with a high mismatch cost are products for which only some consumers have a strong liking while others have a substantial dislike, whereas products with a low mismatch cost appeal to a broad audience. In the paper by Sun (2012), a high average rating indicates a high product quality, whereas a high variance of ratings is associated with a high mismatch cost, where the variance of consumer ratings is solely caused by taste diferences. The variance of ratings can help consumers to determine whether a product’s average rating is low because of its low product quality or because of its high mismatch cost. In the case of a low rating due to a high mismatch cost, some consumers still buy the product because they know that the product matches their taste and that they will not incur a mismatch cost. In this way, a higher variance can increase the demand for a product. Sun (2012) empirically tests the predictions from her analytical model using data for books sold on Amazon.com and Barnesandnoble.com, finding a positive efect of the variance of consumer ratings for books with a low average rating.

In our analytical model, we build on the results from Sun (2012) and others that have a similar model setup (e.g., Chen and Xie 2008, Li and Hitt 2010). We depart from the extant literature by distinguishing taste diferences and quality diferences as separate sources of the variance of consumer ratings and analyze how they differentially afect price and demand for durable goods.

## 3. Notation and Assumptions

Our assumptions pertain to a number of diferent factors relating to, first, consumer heterogeneity; second, product characteristics; and third, consumer rating behavior. These are presented in turn.

Assumption 1 (Consumer Heterogeneity). Consumers are heterogeneous in taste and in risk aversion. Taste and risk aversion are independent.

In line with Sun (2012) and Herrmann et al. (2015), we assume that consumers are heterogeneous in their taste for specific product attributes. We represent consumer taste by τ, which is uniformly distributed between zero and one, that is, $\tau \sim U [ 0 , 1 ]$

We further assume that consumers in e-commerce are risk averse. This assumption is justified by results from laboratory experiments (e.g., Holt and Laury 2002) as well as from surveys among online shoppers (e.g., Bhatnagar et al. 2000). For example, Bhatnagar et al. (2000) find that the likelihood of purchasing on the Internet decreases with product and financial risk. Consumers are also heterogeneous in risk aversion. We denote consumer risk aversion through a risk premium, θ, which is uniformly distributed between zero and one, that is, $\theta \sim U [ 0 , \dot { 1 }$ <sup>]</sup>. Independent tastes and risk premiums are represented by a square with edge length 1 (see Figure 1), where the line segment [AB] represents consumers’ tastes, and the line segment [AC] represents consumers’ risk premiums.

A consumer’s taste is equal to the position on the taste axis, and a consumer’s risk premium is equal to the position on the risk premium axis. For example, a consumer located in A is risk neutral and has taste matched perfectly with the product, whereas a consumer located in E has a high risk premium and taste slightly mismatched with the product.

Our model has two periods, and in each period a unit mass of consumers is uniformly distributed within this square. In the product difusion literature, the widely recognized Bass (1969) model and the even more widely recognized Rogers (1962) difusion of innovations work separate innovators from imitators (Bass 1969) and innovators and early adopters from the early majority, the late majority, and laggards (Rogers 1962). Following this prior seminal research and using the terminology from Bass (1969), in our model, firstperiod consumers are innovators that have a strong preference to adopt new products early, rely primarily on their own expectations, and are unafected by word of mouth through the number or prior purchasers or by consumer ratings. Second-period consumers are imitators that prefer to mitigate their product uncertainty through examining peer opinions, such as consumer ratings by innovators (see, e.g., Li and Hitt 2010), that serve as an informed version of word of mouth.

Figure 1. Consumer Taste and Risk Premium  
![](/api/attachments/QY4572H4/fulltext/images/5cd940ead38c1963ed565dee972f866ef85348f272eb83fc25e0f642b1be2a69.jpg)

To keep our analysis tractable, innovators that do not purchase in the first period exit the market and do not spill over to the second period in our main model (Subsections 4.1 and 4.2). This formulation is in line with other literature analyzing consumer ratings such as Chen and Xie (2008) or Li and Hitt (2008). In Subsection 4.3, we extend our main model by numerically analyzing the efect of innovators that spill over to the second period.

According to Bass (1969) and Rogers (1962), the number of imitators is typically higher than the number of innovators. Consequently, we introduce a scaling factor, $k \in ( 1 , \infty )$ , that we use to scale the unit mass of imitators relative to the unit mass of innovators. Bass (1969) and Rogers (1962) also suggest that imitators have a lower risk tolerance (i.e., a higher risk premium) than innovators. Hence, we introduce a scaling factor, $z \in ( 1 , \infty )$ , that we use to scale the risk premium of imitators.

Although we refer to the Bass (1969) terminology and definitions to separate innovators from imitators, our mathematical model is fundamentally diferent from the Bass (1969) model. The Bass (1969) model is a model of exposure, consistent with its roots in epidemiology as a model of the spread of disease, where in each time t some proportion of innovators and of imitators are exposed to disease and fall ill. Asymptotically, the population is exposed and falls ill, or, in the Bass (1969) sense, purchases the product. Price and promotion can be used to change the time path, but the asymptotic property remains. In contrast, we model consumer choice where some innovators in the first period and some imitators in the second period after learning from consumer ratings find the price too high to purchase and exit the market.

Assumption 2. (Product Characteristics). Each product is characterized by a positive matched quality, positive or zero mismatch costs, and a failure rate between zero and one. Mismatch costs are limited by the matched quality of a product.

Assumption 2 defines products by three characteristics: matched quality, mismatch costs, and failure rate. Matched quality represents the general product quality and determines how much an ideal consumer (i.e., a consumer with a perfectly matched taste) enjoys a product that does not fail during its typical period of usage. Matched quality reflects search attributes that can be obtained from product specifications, such as the availability of an active noise cancellation feature in a set of headphones, and experience attributes that can be obtained from consumer ratings, such as how well the noise cancellation works while worn in an airplane or train. Both influence the general product quality. We denote matched quality as v and assume that $v \in R ^ { + }$ Mismatch costs are the same as in Sun (2012) and reflect search attributes such as the color of the headphones and experience attributes such as the sound characteristics of the headphones “that would have an influence on how much consumers would difer in their enjoyment of the product” (Sun 2012, p. 697). We denote mismatch costs as x and assume that x <sup>∈</sup> <sup>[</sup>0, v<sup>]</sup>. Mismatch costs negatively afect consumers’ enjoyment of a product depending on individual consumer tastes. For example, some consumers love the sound of headphones that have a strong bass, while others dislike a strong bass. Products with attributes that result in mismatch costs of close to zero are a perfect fit for all consumers (i.e., typical mass-market products such as blank paper), while products with attributes that result in high mismatch costs are a perfect fit for just a small group of consumers (i.e., typical niche products such as management information systems textbooks). In contrast to Sun (2012), we assume that mismatch costs are limited by the matched quality of a product. Thus, even consumers that maximally dislike all attributes that result in mismatch costs would receive nonnegative enjoyment from the product if they were to obtain it for free.

Finally, we allow for inconsistent quality goods. As defined in the introduction, inconsistent quality goods are characterized by some product instances that fail and create unacceptable experiences (Sridhar and Srinivasan 2012) while other product instances do not fail. This fact is captured by the third product characteristic, failure rate, $f \in [ 0 , 1 ]$ , that accounts for the likelihood of failure during a product’s typical useful life (Bardey 2004). Products with a failure rate of zero never fail during their typical useful life (distinctive of consistent quality goods), and products with a failure rate of one always fail during this period.

In the first period, publicly available product specifications from the product manufacturer provide the dominant source of product information. These specifications represent certain search attributes and are used by innovators to build expectations about the uncertain experience attributes and potential quality issues of a product resulting in expected matched quality $v _ { e } ,$ expected mismatch costs $\scriptstyle x _ { e } ,$ , and expected failure rate $f _ { e }$ . As we do not consider screening mechanisms or reputational efects of the manufacturer, all innovators and the retailer have the same information from the product manufacturer and any remaining information asymmetries are negligible. Consequently, innovators and the retailer are homogeneous in their expectations of product characteristics, and we do not assume any relationship between $v _ { e } , x _ { e } ,$ and $f _ { e } .$ . In the second period, imitators and the retailer learn from consumer ratings of innovators and can determine the product characteristics realized matched quality $v _ { r } ,$ realized mismatch costs $\scriptstyle x _ { r } ,$ and realized failure rate $f _ { r }$ that may difer from the expectations.

Assumption 3. (Consumer Rating Behavior). All purchasing innovators with extreme experiences (positive or negative) publish honest consumer ratings. Purchasing innovators that experience product failure publish a consumer rating of zero.

Since the 1960s, marketing researchers have reported that innovators are very keen to talk about their experiences with a product. For example, Engel et al. (1969, p. 15) write that “there seems to be no question that the first users of a new product or service are active in the word-of-mouth channel.” In contrast to Sun (2012), we do not require that all purchasing innovators express their experiences with a product via consumer ratings. However, we suppose that soon after a product launch, at least all innovators with extreme experiences publish a consumer rating. This is consistent with the empirically observed underreporting bias (Hu et al. 2017), meaning that “consumers with extreme ratings (positive or negative) are more likely to report their reviews than consumers with moderate ratings” (Hu et al. 2017, p. 450). Furthermore, the published consumer ratings are honest and correspond to the actual utility derived from the consumption of the product. Consequently, there is no external manipulation of consumer ratings as discussed in Mayzlin (2006) or Luca and Zervas (2016), and consumer ratings are continuous in our model. The typically provided star rating systems on e-commerce platforms represent a discretization of our model.

Our latter part of Assumption 3 can be justified by Sridhar and Srinivasan (2012). They propose that a consumer who experiences product failure (i.e., unacceptable product experience) in the face of other consumers’ positive ratings then experiences high normative conflict. Paraphrasing (Sridhar and Srinivasan 2012, p. 74), in such a situation, the consumer, “already dissatisfied because of the product failure, may be motivated to provide an even lower rating to rectify the ‘incorrect’ (according to personal experience) rating on the review website.” We further analyzed different inconsistent quality goods using a text-mining approach and found that the vast majority of consumers post a one-star rating (representing a rating of zero in our model) if the textual review is associated with failure. Details of this analysis are available from the authors.

We summarize our notation in Table 2.

Table 2. Notation

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Symbol Definition
v Matched quality,  $v \in R^{+}$ 
x Mismatch costs,  $x \in [0, v]$ 
f Failure rate,  $f \in [0, 1]$ $\tau$  Consumer taste,  $\tau \sim U[0, 1]$ $\theta$  Consumer risk premium,  $\theta \sim U[0, 1]$ 
k Scaling factor to scale the unit mass of imitators,  $k \in (1, \infty)$ 
z Scaling factor to scale the risk premium of imitators,  $z \in (1, \infty)$
</div>

## 4. Model Analysis

We consider a two-period model with a monopoly retailer and risk-averse consumers. The sequence of events is illustrated in Figure 2.

In the first period, a unit mass of innovators enters the market. Each innovator demands at most one unit, as is the case with durable goods. The retailer sets a profit-maximizing price $p _ { 1 } ,$ and innovators decide whether to purchase based on their expectations of the uncertain product characteristics. Finally, purchasing innovators post honest ratings.

In the second period, k unit masses of imitators enter the market. Imitators and the retailer observe the ratings of innovators and learn about the product characteristics. Based on this information, the retailer sets a profit-maximizing price $p _ { 2 }$ that may difer from $p _ { 1 } ,$ and imitators decide whether to purchase. We take retailers as myopic in the first period as they cannot forecast consumer ratings and, thus, how consumer ratings of innovators may influence second-period price. Dynamic pricing can be observed for almost all products sold on Amazon.com (see price trackers such as Keepa.com or Camelcamelcamel.com), and there is evidence that retailers dynamically adjust prices in response to consumer ratings (see Related Literature).

Figure 2. Sequence of Events  
```txt
First period (launch phase)
1. Innovators enter the market
2. The retailer sets a profit-maximizing price for the product based on its expectations about product characteristics
3. Innovators decide whether to purchase the product based on the price and their expectations about product characteristics
4. Purchasing innovators publish honest ratings about the product (only true for extreme experiences)

Second period
1. Imitators enter the market
2. The retailer observes consumer ratings of innovators and sets a profit-maximizing price for the product based on the observed consumer ratings
3. Imitators observe consumer ratings of innovators and decide whether to purchase the product based on the price and the observed consumer ratings
```

In the following, we separately analyze consistent quality goods (i.e., products that do not fail) and inconsistent quality goods (i.e., products that may fail).

## 4.1. Consistent Quality Goods

Consistent quality goods are characterized solely by matched quality and mismatch costs (i.e., failure rate equals zero), and the variance of consumer ratings is caused solely by taste diferences on search and experience attributes.

4.1.1. First Period. Innovators make their purchase decisions based on their expectations of v and x, which are denoted by $v _ { e }$ and $x _ { e } ,$ respectively. The expected net utility of innovators is

$$
u _ {1} = v _ {e} - x _ {e} \tau - p _ {1}.
$$

Note that the uncertainty associated with experience attributes could be modeled as a separate risk component in the utility function. As this uncertainty is eliminated through consumer ratings for imitators, it has no efect on the qualitative nature of our results. For the sake of simplicity, we do not consider this uncertainty in the utility function of innovators for consistent quality goods or for inconsistent quality goods later.

Solving $v _ { e } - x _ { e } \tau - p _ { 1 } = 0$ for τ yields the taste of the indiferent innovator, which we denote with $\tilde { \tau } _ { 1 } =$ $( v _ { e } - p _ { 1 } ) / x _ { e }$ . All innovators with $\tau \leq \tilde { \tau } _ { 1 }$ purchase, and all innovators with $\tau > \tilde { \tau } _ { 1 }$ do not. As τ is uniformly distributed between zero and one and there is a unit mass of innovators in the market, first-period demand $D _ { 1 }$ is equal to $\tilde { \tau } _ { 1 }$

Knowing this demand, the retailer can maximize profits by solving ma $\mathsf { x } _ { p _ { 1 } } p _ { 1 } D _ { 1 }$ . This leads to the optimal first-period price and demand:

$$
p _ {1} ^ {*} = \frac {v _ {e}}{2} \quad \text { and } \quad D _ {1} ^ {*} = \frac {v _ {e}}{2 x _ {e}}.\tag{1}
$$

At least all purchasing innovators with extreme experiences (i.e., all the innovators with τ <sup></sup> 0 and $\tau = D _ { 1 } ^ { * } )$ and possibly all other purchasing innovators, publish an honest rating. Our ratings are based on the experienced gross utility $v _ { r } - \tau x$ of innovators as proposed by Sun (2012).

Knowing that tastes are uniformly distributed in $[ 0 , D _ { 1 } ^ { * } ] .$ , imitators can resolve the underreporting bias and infer all potential ratings that are uniformly distributed between $[ v _ { r } - D _ { 1 } ^ { * } x _ { r } , v _ { r } ]$ . Given this uniform distribution of ratings, the average rating M and the variance of ratings $V$ can be computed, respectively, as

$$
M = v _ {r} - 0. 5 D _ {1} ^ {*} x _ {r} \quad \mathrm{and} \quad V = \frac {D _ {1} ^ {* 2} x _ {r} ^ {2}}{1 2}.\tag{2}
$$

4.1.2. Second Period. By considering the average and the variance of ratings, imitators learn about experience attributes and mitigate their uncertainty about product characteristics. Imitators can directly derive the realized product characteristics $v _ { r }$ and $x _ { r }$ by rearranging (2):

$$
v _ {r} = M + \sqrt {3 V} \quad \text { and } \quad x _ {r} = \frac {\sqrt {1 2 V}}{D _ {1} ^ {*}}.\tag{3}
$$

After deriving $v _ { r }$ and $x _ { r }$ , imitators have no remaining uncertainty about experience attributes. Given this information, the net utility for imitators is

$$
u _ {2} = v _ {r} - x _ {r} \tau - p _ {2}.
$$

Based on $u _ { 2 } ,$ the retailer can derive the taste of the indiferent imitator as a function of the second-period product price $p _ { 2 } \colon \tilde { \tau } _ { 2 } = ( v _ { r } - p _ { 2 } ) / x _ { r }$ . As taste is uniformly distributed among imitators, and the mass of imitators is scaled by the factor $k ,$ second-period demand $D _ { 2 }$ is equal to $k \tilde { \tau } _ { 2 }$ . Knowing this demand, the retailer can again maximize profits by solving ma $\mathsf { \ K } _ { p _ { 2 } } p _ { 2 } D _ { 2 }$ . This leads to the optimal second-period levels of price and demand:

$$
p _ {2} ^ {*} = \frac {v _ {r}}{2} \quad \text { and } \quad D _ {2} ^ {*} = \frac {k v _ {r}}{2 x _ {r}}.\tag{4}
$$

Using (3), optimal price and demand can be rewritten in terms of M and ${ \bar { V } } { : }$

$$
p _ {2} ^ {*} = \frac {M}{2} + \frac {\sqrt {3 V}}{2} \quad \text { and } \quad D _ {2} ^ {*} = \frac {k D _ {1} ^ {*}}{4} \left(\frac {M}{\sqrt {3 V}} + 1\right).\tag{5}
$$

Based on these representations of $p _ { 2 } ^ { * }$ and $D _ { 2 } ^ { * } ,$ the following proposition details the efects of M and V on optimal price and demand for consistent quality goods. (All proofs of the propositions are in the appendix.)

Proposition 1. For consistent quality goods, price and demand both increase with the average rating, and price increases and demand decreases with the variance of ratings.

The intuition behind Proposition 1 is as follows. First, a high average rating is a credible signal of a high product quality (see (3)). Thus, the retailer charges a higher price and consumers have a higher demand for a product with a higher quality (see (4)). The first part of Proposition 1 represents a theoretical confirmation of the empirical findings of Chevalier and Mayzlin (2006), Sun (2012), Li and Hitt (2008), and Dellarocas et al. (2007) that found a positive impact of average consumer ratings on sales for books and movies, both of which are consistent quality goods that are characterized by search and experience attributes and typically do not fail.

Second, a high variance of ratings indicates a high product quality and high mismatch costs (see (3)). This means that an imitator with taste that closely matches the product enjoys such a product more than a product with a low variance of ratings. The retailer charges a higher price to all imitators to skim the higher willingness to pay of imitators with tastes that closely match the product. This higher price deters imitators with tastes that do not closely match the product, resulting in a lower demand (see (4)). Figure 3 illustrates the response of second-period price and demand to changes in the variance of ratings.

Figure 3. Optimal Price and Demand for Consistent Quality Goods  
![](/api/attachments/QY4572H4/fulltext/images/35d66a8e722e07e8e9e90d9ce93ef654693651aa5570ae8b980bb5368e6385e4.jpg)

In contrast to Sun (2012), we do not find that a higher variance of ratings may also increase second-period demand. In Sun’s (2012) model, a necessary condition for such an efect is that the average rating M is negative. From (2), we know that a negative average rating means that $x _ { r } > 2 v _ { r } / D _ { 1 } ^ { * }$ . Demand $D _ { 1 }$ has a maximum of 1, which implies that $x _ { r } > 2 v _ { r }$ . This would mean that the enjoyment of an innovator with taste $\tau = 1$ is at most $- v _ { r }$ if $p _ { 1 } = 0$ . As most products do not exhibit such characteristics, our second assumption rules out the possibility of M being negative by assuming x is nonnegative, $x \in [ 0 , v ]$

Comparing prices across periods, our analysis for consistent quality goods further shows that a discounted second-period price in response to the average rating and variance of ratings results from an overestimation of matched quality, $v _ { e } > v _ { \ i }$ (see (1) and (4)), in the first period.

## 4.2. Inconsistent Quality Goods

Inconsistent quality goods are not only characterized by matched quality and mismatch costs, but additionally by a failure rate. For these products, the variance of consumer ratings is caused not only by taste diferences but also by quality diferences in the form of product failure.

4.2.1. First Period. Innovators make their purchase decisions based on expected matched quality $v _ { e } ,$ expected mismatch costs $x _ { e } ,$ , and expected failure rate $f _ { e } .$ Innovators with taste τ and risk premium θ have the expected net utility

$$
u _ {1} = (v _ {e} - x _ {e} \tau) (1 - f _ {e}) - p _ {1} - f _ {e} \theta .\tag{6}
$$

The first part of the right-hand side of (6) is equal to the expected net utility of a risk-neutral innovator. The last term in (6) captures a risk-averse innovators’s negative utility caused by the risk that the product fails. Our modeling of consumer risk does not make any assumptions about the specific form of risk aversion such as hyperbolic absolute risk aversion or constant absolute risk aversion. Our only assumption is that consumers do not like the possibility of their product failing.

Given $u _ { 1 } ,$ we can derive the taste of a risk-neutral innovator that is indiferent between purchasing and not purchasing the product, $\tilde { \tau } _ { 1 } ^ { \theta = 0 } .$ , and the risk premium of an indiferent innovator with a perfectly matched taste, ${ \widetilde { \theta } } _ { 1 } ^ { \tau = 0 }$

$$
\tilde {\tau} _ {1} ^ {\theta = 0} = \frac {v _ {e} (1 - f _ {e}) - p _ {1}}{x _ {e} (1 - f _ {e})} \quad \text { and } \quad \tilde {\theta} _ {1} ^ {\tau = 0} = \frac {v _ {e} (1 - f _ {e}) - p _ {1}}{f _ {e}}.
$$

Because of the independence of taste and risk premium, first-period demand $D _ { \uparrow }$ equals $0 . 5 \tilde { \tau } _ { 1 } ^ { \theta = 0 } \tilde { \theta } _ { 1 } ^ { \tau = 0 } \stackrel { \bullet } { ( \mathrm { i . e . , } }$ the area of the triangle $[ A , \tilde { \tau } _ { 1 } ^ { \theta = 0 } , \tilde { \theta } _ { 1 } ^ { \tau = 0 } ]$ in Figure 4), meaning that all innovators with a taste/risk premium pair that is located below the linear function of indifferent innovators purchase the product, and all others do not and exit the market.

In terms of $v _ { e } , x _ { e } ,$ and $f _ { e } ,$ first-period demand can be written as

$$
D _ {1} = \frac {(v _ {e} (1 - f _ {e}) - p _ {1}) ^ {2}}{2 f _ {e} x _ {e} (1 - f _ {e})}.
$$

Based on this demand, the retailer maximizes profits by choosing first-period price ma $\mathsf { \ K } _ { p _ { 1 } } p _ { 1 } D _ { 1 }$ . This results in optimal first-period price and demand:

$$
p _ {1} ^ {*} = \frac {v _ {e} (1 - f _ {e})}{3} \quad \text { and } \quad D _ {1} ^ {*} = \frac {2 v _ {e} ^ {2} (1 - f _ {e})}{9 f _ {e} x _ {e}}.\tag{7}
$$

Innovators that purchase and publish a rating base this rating on their experienced gross utility $\boldsymbol { v } _ { r } - \boldsymbol { x } _ { r } \boldsymbol { \tau }$ if the consumed product does not fail and a rating of zero if it does. If all purchasing innovators publish a rating, then this results in a rating distribution where $1 - \bar { f _ { r } } \%$ of purchasing innovators publish a rating of $\boldsymbol { v } _ { r } - \boldsymbol { x } _ { r } \boldsymbol { \tau }$ for products that do not fail, and $f _ { r } \%$ publish a rating of zero for products that fail. For products that do not fail, ratings are triangularly distributed between $v _ { r } - \tilde { \tau } _ { 1 } ^ { \theta = 0 } x _ { r }$ and $v _ { r }$ with mode at v (see the triangular distribution in Figure 5 with the solid hypotenuse).

Figure 4. First-Period Demand for Inconsistent Quality Goods  
![](/api/attachments/QY4572H4/fulltext/images/bbcbfe42d1abd1c2f394cc0a5f72419fc5be072732615b36070abfe4fa97c6fe.jpg)

Figure 5. Rating Distribution for Inconsistent Quality Goods  
![](/api/attachments/QY4572H4/fulltext/images/b56d4587d17a7bca2aae17121dd5f268263fa86a2cdbc155086a4ca0f7b3e4a8.jpg)

Our explanation for this specific shape of the rating distribution is as follows. Those innovators that publish a rating of $v _ { r }$ have a taste of $\tau = 0$ . Thus, the number of ratings of $v _ { r }$ equals the indiferent risk premium for these innovators, $\tilde { \theta } _ { 1 } ^ { \tau = 0 }$ . For decreasing ratings, the indiferent risk premium and, therefore, the number of ratings decrease. The lower bound of ratings for products that do not fail is the rating of the indiferent imitator with a risk premium of zero, $v _ { r } - \tilde { \tau } _ { 1 } ^ { \theta = 0 } x _ { r }$ . Thus, the mode of the triangular distribution must be at $v _ { r } ,$ and the number of ratings strictly decreases with increasing taste down to a rating of $v _ { r } - \tilde { \tau } _ { 1 } ^ { \theta = 0 } x _ { r } . \mathrm { A }$ decreasing number of consumer ratings from high ratings to low ratings can also be observed empirically and is explained by the so called acquisition bias (Hu et al. 2017), meaning that “consumers with a favorable predisposition toward a product are more likely to purchase a product” (Hu et al. 2017, p. 450).

Considering the underreporting bias (see Assumption 3), a mass of innovators $b \in [ 0 , 1 - f _ { r } ]$ with mediocre experiences may not publish ratings (see the area between the solid hypotenuse and the dashed line in Figure 5). However, all innovators with extreme experiences publish ratings. In our model, extreme experiences are represented by a perfectly matched taste $( \mathrm { i . e . , }$ a rating of $v _ { r } ) .$ , a perfectly mismatched taste $( \mathrm { i . e . , }$ a rating of $\bar { v _ { r } } - \tilde { \tau } _ { 1 } ^ { \theta = 0 } x _ { r } )$ , or product failure $( \mathrm { i . e . }$ , a rating of zero). Even in this case, imitators can observe the corners of the triangular distribution and resolve the underreporting bias (Hu et al. 2017).

The resulting rating distribution has the typical J shape, which has been found for almost all products sold on Amazon.com (Hu et al. 2017). This empirical consistency provides evidence that helps justify our assumptions.

In contrast to consistent quality goods, the enjoyment of inconsistent quality goods depends not on only two, but on three product characteristics. Thus, it is not suficient to consider only the average and the variance of ratings to derive the relevant product characteristics from the rating distribution. For example, based solely on the average and the variance of the rating distribution, imitators cannot distinguish whether a mediocre average rating and a positive variance are caused by taste diferences, quality diferences, or a combination of these attributes. However, by decomposing the total variance into variance caused by taste diferences and variance caused by quality diferences, imitators and the retailer can distinguish between these cases. Variance caused by taste diferences, denoted as $V _ { t } ,$ can be derived by disregarding all negative ratings that are caused by product failure and computing the variance of the triangular distribution on the right in Figure 5. As we have only two sources of variance, the variance caused by quality diferences, denoted as $V _ { q } ,$ must be equal to the diference between the total variance and the variance caused by taste diferences. The terms $M ,$ $V _ { t } ,$ and $V _ { q }$ can be computed, respectively, as

$$
\begin{array}{l} M = \left(v _ {r} - \frac {\tilde {\tau} _ {1} ^ {\theta = 0} x _ {r}}{3}\right) (1 - f _ {r}), \quad V _ {t} = \frac {\left(\tilde {\tau} _ {1} ^ {\theta = 0}\right) ^ {2} x _ {r} {} ^ {2} (1 - f _ {r})}{1 8}, \\ \text { and } \quad V _ {q} = \frac {(1 - f _ {r}) f _ {r} (3 v _ {r} - \tilde {\tau} _ {1} ^ {\theta = 0} x _ {r}) ^ {2}}{9}. \end{array} \tag {8}\tag{8}
$$

4.2.2. Second Period. Based on $M , V _ { t } ,$ and $V _ { q } ,$ imitators learn about the product. A product with a rating distribution with large M, large $V _ { t } ,$ and small $V _ { q }$ suggests that the product has a high matched quality and substantial mismatch costs but only a small failure rate. A product with large M, small $\dot { V _ { t } } ,$ and large $V _ { q }$ has a high matched quality with a substantial failure rate but low mismatch costs. Imitators derive $v _ { r } , x _ { r }$ , and $f _ { r }$ for inconsistent quality goods by rearranging (8):

$$
\begin{array}{l} v _ {r} = M + \frac {V _ {q} + \sqrt {2 V _ {t} (M ^ {2} + V _ {q})}}{M}, \quad x _ {r} = \frac {3 \sqrt {2 V _ {t} (M ^ {2} + V _ {q})}}{M \tilde {\tau} _ {1} ^ {\theta = 0}}, \\ \text { and } \quad f _ {r} = \frac {V _ {q}}{M ^ {2} + V _ {q}}. \end{array} \tag {9}
$$

After deriving $v _ { r } , \ x _ { r } ,$ and $f _ { r } ,$ imitators have no remaining uncertainty about the product characteristics. They know the exact matched quality and mismatch costs of the product and, therefore, how well the product matches their tastes. Even if imitators know the exact failure rate of the product, they do not know whether their individual product will fail. Thus, the expected net utility for imitators is

$$
u _ {2} = (v _ {r} - x _ {r} \tau) (1 - f _ {r}) - p _ {2} - f _ {r} z \theta ,
$$

where the term $f _ { r } z \theta$ captures the risk associated with product failure. Based on the net utility, the retailer can derive second-period demand. Compared to the first period, second-period demand $D _ { 2 }$ is scaled by k and equals $0 . 5 k \widetilde { \tau } _ { 2 } ^ { \theta = 0 } \widetilde { \tilde { \theta } } _ { 2 } ^ { \tau = 0 }$ . In terms of $v _ { r } , x _ { r } ,$ and $f _ { r } ,$ secondperiod demand can be written as

$$
D _ {2} = \frac {k (v _ {r} (1 - f _ {r}) - p _ {2}) ^ {2}}{2 f _ {r} z x _ {r} (1 - f _ {r})}.\tag{10}
$$

Based on this demand, the retailer again maximizes profits by choosing second-period price: ma $\mathsf { \ K } _ { p _ { 2 } } p _ { 2 } D _ { 2 }$ This results in optimal second-period price and demand:

$$
p _ {2} ^ {*} = \frac {v _ {r} (1 - f _ {r})}{3} \quad \text { and } \quad D _ {2} ^ {*} = \frac {2 k v _ {r} ^ {2} (1 - f _ {r})}{9 f _ {r} z x _ {r}}.\tag{11}
$$

Using (9), optimal price and demand can be rewritten as functions of $M , V _ { t } ,$ and $V _ { q } { \mathrm { : } }$ :

$$
\begin{array}{c} p _ {2} ^ {*} = \frac {M}{3} + \frac {M \sqrt {2 V _ {t} (M ^ {2} + V _ {q})}}{3 (M ^ {2} + V _ {q})} \quad \text {and} \\ D _ {2} ^ {*} = \frac {M k \tilde {\tau} _ {1} ^ {\theta = 0} \sqrt {2 (M ^ {2} + V _ {q})} (\sqrt {2 V _ {t}} + \sqrt {M ^ {2} + V _ {q}}) ^ {2}}{2 7 z V _ {q} \sqrt {V _ {t}}}. \end{array}\tag{12}
$$

Based on these representations of $p _ { 2 } ^ { * }$ and $D _ { 2 } ^ { * } ,$ we derive the efects of the average rating, variance caused by taste diferences, and variance caused by quality differences on optimal price and demand in the next three propositions.

Proposition 2. For inconsistent quality goods, price and demand both increase with the average rating.

The intuition for Proposition 2 is similar to the intuition underlying the first part of Proposition 1 for consistent quality goods. A high average rating acts as a credible signal of a high product quality (i.e., high matched quality and low failure rate; see (9)). Therefore, price and demand both increase with the average rating (see (11)).

Proposition 3. For inconsistent quality goods, price increases and demand decreases with the variance caused by taste diferences.

A high variance of ratings caused by taste diferences indicates a product with high mismatch costs. Again, this means that an imitator with a perfectly matched taste enjoys such a product more (i.e., the product has a higher matched quality) than a product with low variance caused by taste diferences (see (9)). Thus, the retailer charges a higher price to skim the higher willingness to pay of imitators with tastes that closely match the product. This higher price deters some imitators with tastes that do not closely match the product and, therefore, results in a lower demand (see (11)). Figure 6 illustrates the relationship between price and demand, and the variance caused by taste diferences.

Figure 6. Optimal Price and Demand for Inconsistent Quality Goods—Variance Caused by Taste Diferences  
![](/api/attachments/QY4572H4/fulltext/images/5e066e59494e601812df9d8699de04f52bf1a5f346ebf6d32ff5a26a16ac9e3c.jpg)  
Proposition 4. For inconsistent quality goods, (a) price decreases with variance caused by quality diferences; (b) if the variance caused by quality diferences is suficiently low, then demand decreases with variance caused by quality diferences; (c) if the variance caused by quality diferences is sufficiently high and the variance caused by taste diferences is suficiently low, then demand increases with variance caused by quality diferences.

A high variance of ratings caused by quality differences indicates a high failure rate (see (9)). A high failure rate is a signal of quality issues with the product and consequently the retailer sets a lower price (see (11)). A high failure rate also has a direct negative efect on demand as imitators do not like products with potential quality issues. If this direct negative efect of failure rate on demand outweighs the indirect positive efect through a lower price (i.e., if $V _ { q } < 2 M ^ { \bar { 2 } } ;$ see proof of Proposition 4 in the appendix), then demand decreases with the variance caused by quality diferences. Figure 7 illustrates the relationship between optimal price and demand and variance caused by quality diferences for a product with $V _ { a } < 2 M ^ { 2 }$

If the indirect positive efect of failure rate through a lower price outweighs the direct negative efect (i.e., if $V _ { q } > 2 M ^ { 2 }$ and $V _ { t } < ( ( M ^ { 2 } + V _ { q } ) ( - 2 M ^ { 2 } + V _ { q } ) ^ { 2 } ) /$ $( 2 ( 2 M ^ { 2 } + { \dot { V } } _ { q } ) ^ { 2 } ) ;$ see proof of Proposition 4 in the appendix), then demand increases in the variance caused by quality diferences. However, in a typical five-star rating system with one indicating the lowest and five indicating the highest rating, the condition $V _ { q } > 2 M ^ { 2 }$ is not valid.

Figure 7. Optimal Price and Demand for Inconsistent Quality Goods—Variance Caused by Quality Diferences  
![](/api/attachments/QY4572H4/fulltext/images/28abdcbb0e6214b644d7f355cb785733dd92d3f1f9d31dab907bd5d2f8efc14b.jpg)

Comparing prices across periods, our analysis for inconsistent quality goods further shows that a discounted second-period price in response to the average rating and the two parts of the variance of ratings results from an overestimation of matched quality, $v _ { e } > v _ { r }$ , and/or an underestimation of the failure rate, $f _ { e } < f _ { r }$ (see (7) and (11)), in the first period.

In our analyses so far, we have investigated the efects from increasing one part of the variance (e.g., variance caused by taste diferences) while the other part of the variance (e.g., variance caused by quality diferences) stays constant. To further analyze diferent decompositions of a constant total variance, we substitute $V _ { t }$ by $V - V _ { q }$ in (12). This means that an increase of variance caused by taste diferences goes along with a decrease of variance caused by quality diferences, but the total variance stays constant. With this substitution, optimal price and demand can be written as

$$
\begin{array}{l} p _ {2} ^ {*} = \frac {M}{3} + \frac {M \sqrt {2 (V - V _ {q}) (M ^ {2} + V _ {q})}}{3 (M ^ {2} + V _ {q})} \quad \text {and} \\ D _ {2} ^ {*} = \frac {M k \tilde {\tau} _ {1} ^ {\theta = 0} \sqrt {2 (M ^ {2} + V _ {q})} (\sqrt {2 (V - V _ {q})} + \sqrt {M ^ {2} + V _ {q}}) ^ {2}}{2 7 z V _ {q} \sqrt {V - V _ {q}}}. \end{array}\tag{13}
$$

Based on these representations of $p _ { 2 } ^ { * }$ and $D _ { 2 ^ { \prime } } ^ { * }$ we derive the efects of diferent shares of variance caused by taste diferences (quality diferences) on optimal price and demand in the next proposition.

Proposition 5. For inconsistent quality goods and a constant total variance, (a) price increases (decreases) with an increasing relative share of variance caused by taste differences (quality diferences); (b) if the total variance is suficiently low, then demand increases (decreases) with an increasing share of variance caused by taste diferences (quality diferences); (c) if the total variance is suficiently high, then demand decreases (increases) with an increasing share of variance caused by taste diferences (quality diferences).

The intuition for Proposition 5 is as follows. An increasing relative share of variance caused by taste differences is necessarily associated with a decreasing relative share of variance caused by quality diferences. Again, a higher variance of ratings caused by taste diferences indicates a product with higher mismatch costs. Similar to Proposition $^ { 3 , }$ an imitator with a perfectly matched taste enjoys such a product more than a product with lower variance caused by taste diferences. Thus, the retailer charges a higher price to skim the higher willingness to pay of imitators with tastes that closely match the product. At the same time, a lower variance caused by quality diferences indicates a lower failure rate. This leads to a further increase of the price as the retailer associates fewer quality issues with the product.

Holding the average rating constant, a lower failure rate makes the product more attractive to risk-averse consumers. If the total variance is lower than a threshold, $V < \underline { { V } }$ , where $\underline { { V } }$ is defined in the proof of Proposi-<sup>¯ ¯</sup>tion 5 (see the appendix), then the direct positive efect of the lower failure rate on demand is greater than the indirect negative efect of a higher price on demand. Thus, in this case, both price and demand increase in the share of variance caused by taste diferences. Alternatively, if the total variance is higher than a threshold, $V > \bar { V } .$ , where $\bar { V }$ is also defined in the proof of Proposition 5, then the direct positive efect of the lower failure rate on demand is smaller than the indirect negative efect through price. In this case, the total efect of an increasing share of variance caused by taste diferences on demand is negative.

Figure 8 illustrates the response of optimal price and demand to changes in the decomposition of the variance of consumer ratings for $V \overset { \widehat { } } { < } \underline { V }$ in the left-hand graph and $V > \bar { V }$ in the right-hand graph.

Through the mechanism described in Proposition 5(b), price and demand can increase with total variance of consumer ratings, which is illustrated in the following numerical example.

4.2.3. Numerical Example. To get realistic values for the average rating and variance of ratings, we scale the risk premium of innovators by $z _ { 1 } = 2 5 0$ . To represent the higher risk aversion of imitators, we scale their risk premium by $z _ { 2 } = 5 0 0$ . Furthermore, we take the number of imitators as four times higher than the number of innovators by setting $k = 4 .$ . The shaded area in Figure 9 illustrates optimal demand for products with an average rating of $\bar { 4 } , \mathsf { a }$ total variance of ratings between 1 and 1.5, and varying shares of variance caused by taste diferences. For these values, $V < \underline V$ holds, and, consequently, an increasing relative share of variance caused by taste diferences leads to an increase in demand (see Proposition 5(b)). Thus, the lower bound of the shaded area represents demand for products with the lowest possible relative share of $V _ { t } ,$ and the upper bound represents demand for products with the highest possible relative share of $V _ { t } .$

The point marked with A in Figure 9 represents a product with expected product characteristics of $v _ { e } =$ $\bar { 5 } . 5 0 , x _ { e } = 4 . 1 5 ,$ , and $f _ { e } = 0 . 0 2 0$ . The realized product characteristics of product A are $v _ { r } = 5 . 3 0 , x _ { r } = 4 . 1 0$ , and $f _ { r } = 0 . 0 2 3$ . The resulting total variance is 1.1, which is composed of approximately 64% of variance caused by taste diferences and 36% of variance caused by quality diferences. This results in an optimal price of 1.73 and a demand of 0.5. The solid black line in Figure 9 represents products with the same optimal price as product A $( \hat { p _ { 2 } ^ { * } } = 1 . 7 3 )$ . As optimal price increases in the relative share of variance caused by taste differences (see Proposition 5(a)), all products above the solid black line have higher prices compared to product A. Thus, holding the average rating constant and increasing the total variance of ratings, we find higher optimal prices and higher demand for products in the top right-hand quadrant from point $\mathrm { A } .$ Comparing the worst possible variance composition, marked with B $( D _ { 2 } ^ { * } = 0 . 4 3 , \ p _ { 2 } ^ { * } = 1 . 6 6 )$ , and the best possible variance composition, marked with $\mathsf { C } ( D _ { 2 } ^ { * } { = } 1 . 3 \mathsf { \bar { 4 } } , p _ { 2 } ^ { * } { = } 1 . 8 8 )$ , illustrates that product C with 50% higher total variance has a 13% higher price, and a more than three times higher demand compared to product B. This comparison demonstrates that the source of variance of consumer ratings substantially influences product prices and sales, and that risk-averse consumers may prefer products with a higher price and a higher total variance.

Figure 8. Optimal Price and Demand for Inconsistent Quality Goods—Changes in the Composition of the Variance  
![](/api/attachments/QY4572H4/fulltext/images/d43cd309c99f7394498cad2bde5187b52e978d6b74b77de13d48a2a061af06cc.jpg)

![](/api/attachments/QY4572H4/fulltext/images/6598db441da4fdcc83b0733356126b8e604202bd4598a1892aa8e04156339020.jpg)

Figure 9. Demand for Products with Diferent Variance Compositions  
![](/api/attachments/QY4572H4/fulltext/images/c9bf2e35b59f3dc3e4d7d74fe52b5a8fa2e45136e5c29106a1d7d7866c26f36c.jpg)

## 4.3. Model Extension: Inconsistent Quality Goods with Overlapping Innovators

In our main model, we assume that innovators who do not purchase in the first period exit the market. In this model extension, we relax this assumption and allow nonpurchasing innovators from the first period to reconsider purchasing the same product in the second period $( \mathrm { i . e . , }$ spillover) and extend the mass of imitators in the second period. We take these overlapping innovators as innovators in the second period. Thus, overlapping innovators remain unafected by consumer ratings and, even though consumer ratings are available in the second period, continue to decide based on their expectations of product characteristics. Allowing overlapping innovators to become imitators in the second period would contradict Bass (1969) and Rogers (1962), which both take innovators and imitators as mutually exclusive consumer groups with diferent characteristics in several dimensions, including elements that drive taste and risk preferences evidenced in the risk premium. For there to be overlapping innovators in the second period requires that the retailer reduces the price from first to second period $( p _ { 2 } ^ { * } < p _ { 1 } ^ { * } )$ . Overlapping innovators may only purchase the product in the second period if they can take advantage of a lower second-period price. Consequently, the demand function for overlapping innovators is given by

$$
D _ {\text {spill}} = \max \left[ 0, \frac {(v _ {e} (1 - f _ {e}) - p _ {2}) ^ {2}}{2 f _ {e} x _ {e} (1 - f _ {e})} - \frac {(v _ {e} (1 - f _ {e}) - p _ {1} ^ {*}) ^ {2}}{2 f _ {e} x _ {e} (1 - f _ {e})} \right].\tag{14}
$$

The behavior of innovators is not strategic, as they do not know in the first period the direction of a potential price change that depends on the magnitude and direction of the deviation of expected product characteristics from realized product characteristics. To consider overlapping innovators in the second-period demand function, (10) has to be extended by (14), yielding

$$
D _ {2} = \frac {k (v _ {r} (1 - f _ {r}) - p _ {2}) ^ {2}}{2 f _ {r} z x _ {r} (1 - f _ {r})} + D _ {\mathrm{spill}}.\tag{15}
$$

The demand function in (15) represents a kinked demand curve with the kink at ${ p } _ { 2 } = { p } _ { 1 } ^ { * }$ . To maximize profits $( \mathrm { i . e . , \ m a x } _ { p _ { 2 } } p _ { 2 } D _ { 2 } )$ , the retailer determines an optimal second-period price with no spillover, ${ p } _ { 2 , n s } ^ { * } ,$ and an optimal second-period price with spillover, $p _ { 2 , w s } ^ { * } ,$ and chooses the price that results in higher profits. This retailer behavior is represented by the max function in (14).

The resulting optimal second-period price and demand can be expressed as functions of ${ \bar { M } } , V _ { t } ,$ and $V _ { q }$ by using (9). As the resulting equations and derivatives for optimal second-period price and demand with spillover cannot be simplified to yield clear analytical results, we numerically analyze the efects of overlapping innovators on our results from the main model.

4.3.1. Numerical Analysis. Our numerical analysis proceeds in two steps. First, we analyze the circumstances when a spillover takes place. Second, we analyze whether Propositions 2 to 5 of our main model also hold with overlapping innovators.

Figure 10. Numerical Analysis for Overlapping Innovators, $v _ { e }$ and $x _ { e }$ Varied  
![](/api/attachments/QY4572H4/fulltext/images/4af6ba138464bb6e6219026668c3fa417202cd175be6fb1cf059baa18075d4ad.jpg)

Step 1. For the numerical analysis, we set all realized product characteristics to $0 . 5 ( \mathrm { i . e . } , v _ { r } = x _ { r } = f _ { r } = 0 . 5 )$ , the number of imitators to be four times higher than the number of innovators $( \mathrm { i } . \mathrm { e } . , k = 4 )$ , and the risk tolerance of innovators to be two times higher than the risk tolerance of imitators $( \mathrm { i } . \mathrm { e } . , z = 2 )$ . As the expected product characteristics of innovators define the optimal firstperiod price (see (7)) and the mass of overlapping innovators (see (14)), we vary the expected product characteristics between 0 and 1. The results are illustrated in the graphs in Figures 10 and 11.

In the graph in Figure $1 0 , v _ { e }$ and $x _ { e }$ are varied between 0 and 1. The area IV represents combinations of $v _ { e }$ and $x _ { e }$ that are not defined as we assume $x \leq v$ in our model. The area VI represents combinations where the indiferent consumers are not defined in the first period $( \mathrm { i . e . , } \tilde { \tau } _ { 1 } ^ { \theta = 0 } \ni [ 0 , 1 ]$ or $\tilde { \theta } _ { 1 } ^ { \tau = 0 } \ni [ 0 , 1 ] ,$ ), and the areas V represents where this is the case for the second period $( \mathrm { i . e . , ~ } \tilde { \tau } _ { 2 } ^ { \theta = 0 } \ni [ 0 , 1 ]$ or $\tilde { \theta } _ { 2 } ^ { \tau = 0 } \ni [ 0 , 1 ] )$ . The area I represents combinations of $v _ { e }$ and $x _ { e }$ that result in an optimal first-period price that is lower than the optimal secondperiod price $( \mathrm { i . e . , } p _ { 1 } ^ { \ast } < p _ { 2 } ^ { \ast } )$ and, thus, where innovators do not spill over (no spillover, case (a)). This is not surprising, as in these cases the realized matched quality of $v _ { r } = 0 . 5$ is (much) higher than the expected matched quality, and consequently, the retailer increases the price from the first to second period after imitators and the retailer learn about the actual matched quality by observing consumer ratings. The area II represents combinations of $v _ { e }$ and $x _ { e }$ where a spillover would generate a candidate solution for optimal price and demand in the lower part of the kinked demand curve $( \mathrm { i . e . } , p _ { 2 , w s } ^ { \ast } < p _ { 1 } ^ { \ast } )$ . Interestingly, in this area, the retailer chooses the profit-maximizing price with no spillover $( \mathbf { i . e . } , p _ { 2 , n s } ^ { \ast } \geq p _ { 1 } ^ { \ast } )$ , as this price results in higher profits (no spillover, case (b)). This higher price means that the profits from a higher price charged to imitators is greater than the forgone profits from a lower price yielding higher demand from imitators plus the innovators that spill over.

Finally, the area III represents combinations where it is profit maximizing for the retailer to choose an optimal second-period price that is lower than the optimal first-period price $( \mathrm { i . e . } , p _ { 2 , w s } ^ { \ast } < p _ { 1 } ^ { \ast } )$ and generate overlapping innovators (spillover). This means that the area III represents combinations where innovators spill over between periods and purchase the product in the second period. In the upper right corner of the area III this is not surprising, as the realized matched quality is (much) lower compared to the expected matched quality. Naturally, the optimal price set by the retailer in the first period is higher than that in the second period even without considering the potential for innovators to spill over (i.e., $p _ { 1 } ^ { * } > p _ { 2 , n s } ^ { * } > p _ { 2 , w s } ^ { * } )$ . In the lower part of the area III, we have the interesting situation that without considering innovators that spill over between periods, the optimal second-period price would be higher than the optimal first-period price. However, because of the potential extra demand from innovators that spill over to the second period, the retailer sets a lower second-period price and increases profits from the higher demand from innovators that spill over into the second period (i.e., $p _ { 2 , n s } ^ { * } > p _ { 1 } ^ { * } > p _ { 2 , w s } ^ { * } )$

Interpretations of the two graphs in Figure 11 are analogous. In the left graph, $v _ { e }$ and $f _ { e }$ are varied, and in the right graph, $x _ { e }$ and $f _ { e }$ are varied. The locations of the diferent feasible areas I (no spillover, case (a)), II (no spillover, case (b)), and III (spillover) are primarily driven by the expected failure rate in both graphs: if the expected failure rate is high, then there is be no spillover, as the retailer sets a higher second-period price because of the comparably lower realized failure rate.

Step 2. For all parameter combinations represented by the areas III in Figures 10 and 11, we analyze whether our Propositions 2 to 5 of the main model also hold for the case with overlapping innovators. Therefore, we incrementally increased, ceteris paribus, the average rating, $M ,$ to test Proposition $2 ;$ the variance caused by taste diferences, ${ \bar { V } } _ { t } ,$ to test Proposition $3 ;$ the variance caused by quality diferences, $V _ { q } ,$ to test Proposition $4 ;$ and the relative share of variance caused by taste diferences, $V _ { t } / V ,$ to test Proposition 5. By analyzing the respective efects on optimal second-period price and demand, we find that for all parameter combinations represented by the areas III, Propositions 2, $3 , 4 ( \mathsf { a } ) , 4 ( \mathsf { b } ) , \mathsf { \bar { 5 } ( \mathsf { a } ) }$ , and $5 ( \mathrm { c } )$ of the main model also hold for the case with overlapping innovators. In Table 3 we illustrate this procedure using the parameter settings $v _ { e } = v _ { r } = x _ { e } = \bar { x _ { r } } = f _ { e } = f _ { r } = 0 . 5$ as an example.

Figure 11. Numerical Analysis for Overlapping Innovators, $x _ { e } , f _ { e }$ (Left Panel) and $v _ { e } , f _ { e }$ (Right Panel) Varied  
![](/api/attachments/QY4572H4/fulltext/images/6834799a43bc7fddba8ab6e58c27f2ce900c912736f1154c6c5e9c78b9f821c0.jpg)

![](/api/attachments/QY4572H4/fulltext/images/f39dfb76e299d94b71c694f573d847f97da1792f19dfee999116ac4bb40bbf6a.jpg)  
I No spillover (case (a)) III Spillover  
II No spillover (case (b)) IV Not defined (x > v) VI Not defined $( \tilde { \tau } _ { 1 } ^ { \theta = 0 } \ni [ 0 , 1 ] \mathrm { o r } \tilde { \theta } _ { 1 } ^ { \tau = 0 } \ni [ 0 , 1 ] )$  
V Not defined $( \tilde { \tau } _ { 2 } ^ { \theta = 0 } \ni [ 0 , 1 ] \mathrm { o r } \tilde { \theta } _ { 2 } ^ { \tau = 0 } \ni [ 0 , 1 ] )$

For our aforementioned numerical analysis, we chose a product where Proposition 5(c) holds in the main model, and we found that Proposition 5(c) also holds in the model extension with overlapping innovators. As our counterintuitive result that risk-averse consumers may prefer a higher-priced product with a higher total variance results from Proposition 5(b), we further analyze a product where the condition for Proposition 5(b) $\left( \mathrm { i . e . , } \bar { V } < \underline { { V } } \right)$ holds in the main model. This is the case for product A in our numerical example of the main model (see Figure 9), which we now extend by allowing innovators to spill over to the second period.

4.3.2. Numerical Example Extension. To recapitulate, product A has an average rating of $M = 4$ and a total variance of $V = 1 . 1$ , which is composed of 64% variance caused by taste diferences and 36% variance caused by quality diferences. These numbers, the resulting optimal first-period price and demand, and the optimal second-period price and demand with and without spillover are illustrated in the row “Initial setting” of Table 4.

We again incrementally increase the average rating, the variance caused by taste diferences, the variance caused by quality diferences, and the relative share of variance caused by taste diferences. Reassuringly, we find that the directions of the efects on optimal second-period price and demand are the same with and without spillover for product A. By this extension of our numerical example into the case where innovators spill over to the second period, we find that there are products with a suficiently low total variance, where optimal second-period price and demand increase with an increasing relative share of variance caused by taste diferences (Proposition 5(b)).

In addition to the aforementioned numerical analyses, we analyzed numerous other parameter combinations for multiple products and found that the propositions of our main model hold for almost all products when innovators spill over (details are available from the authors). We found only a few extreme cases where our propositions do not hold across the board. These extreme cases can be categorized broadly into two groups. The first group comprises cases with extreme realized failure rates of close to one, something that can hardly be observed in practice. The second group comprises cases where the realized matched quality and realized mismatch costs are small $( { \bf e . g . } , v _ { r } =$ $x _ { r } = 0 . 1 )$ and expected matched quality and expected mismatch costs are much higher $( { \bf e . g . } , \ v _ { e } = x _ { e } = 1 )$ Again, such cases can rarely be observed in practice. Overall, based on our numerical analyses, we find that our results from the main model hold for the model extension allowing a potential spillover of innovators in the second period over a wide range of realistic values.

<table><tr><td rowspan="2">What is changed</td><td rowspan="2">M</td><td rowspan="2"> $V_t$ </td><td rowspan="2"> $V_q$ </td><td rowspan="2">V</td><td rowspan="2"> $V_t/V$ </td><td rowspan="2"> $V_q/V$ </td><td rowspan="2"> $p_1^*$ </td><td rowspan="2"> $D_1^*$ </td><td colspan="2">No spillover</td><td colspan="2">Spillover</td><td rowspan="2">Result</td><td rowspan="2">Does proposition (P) hold also with spillover?</td></tr><tr><td> $p_{2,ns}^*$ </td><td> $D_{2,ns}^*$ </td><td> $p_{2,ws}^*$ </td><td> $D_{2,ws}^*$ </td></tr><tr><td>Initial setting</td><td>4.0000</td><td>0.7118</td><td>0.3883</td><td>1.1000</td><td>0.6470</td><td>0.3530</td><td>1.7967</td><td>0.3175</td><td>1.7263</td><td>0.5028</td><td>1.3476</td><td>0.70341</td><td></td><td></td></tr><tr><td>M+1%</td><td>4.0400</td><td>0.7118</td><td>0.3883</td><td>1.1000</td><td>0.6470</td><td>0.3530</td><td>1.7967</td><td>0.3175</td><td>1.7397</td><td>0.5205</td><td>1.3615</td><td>0.72136</td><td> $p_{2,ws}^*$  increases</td><td>P2 holds</td></tr><tr><td>M+5%</td><td>4.2000</td><td>0.7118</td><td>0.3883</td><td>1.1000</td><td>0.6470</td><td>0.3530</td><td>1.7967</td><td>0.3175</td><td>1.7934</td><td>0.5962</td><td>1.4183</td><td>0.79786</td><td> $D_{2,ws}^*$  increases</td><td></td></tr><tr><td>M+10%</td><td>4.4000</td><td>0.7118</td><td>0.3883</td><td>1.1000</td><td>0.6470</td><td>0.3530</td><td>1.7967</td><td>0.3175</td><td>1.8604</td><td>0.7022</td><td>1.4914</td><td>0.90466</td><td></td><td></td></tr><tr><td> $V_t + 1\%$ </td><td>4.0000</td><td>0.7189</td><td>0.3883</td><td>1.1072</td><td>0.6429</td><td>0.3507</td><td>1.7967</td><td>0.3175</td><td>1.7283</td><td>0.5014</td><td>1.3480</td><td>0.70204</td><td> $p_{2,ws}^*$  increases</td><td>P3 holds</td></tr><tr><td> $V_t + 5\%$ </td><td>4.0000</td><td>0.7473</td><td>0.3883</td><td>1.1356</td><td>0.6267</td><td>0.3419</td><td>1.7967</td><td>0.3175</td><td>1.7360</td><td>0.4962</td><td>1.3494</td><td>0.69676</td><td> $D_{2,ws}^*$  decreases</td><td></td></tr><tr><td> $V_t + 10\%$ </td><td>4.0000</td><td>0.7829</td><td>0.3883</td><td>1.1712</td><td>0.6077</td><td>0.3315</td><td>1.7967</td><td>0.3175</td><td>1.7455</td><td>0.4901</td><td>1.3512</td><td>0.69060</td><td></td><td></td></tr><tr><td> $V_q + 1\%$ </td><td>4.0000</td><td>0.7118</td><td>0.3922</td><td>1.1039</td><td>0.6447</td><td>0.3517</td><td>1.7967</td><td>0.3175</td><td>1.7263</td><td>0.4979</td><td>1.3455</td><td>0.69853</td><td> $p_{2,ws}^*$  decreases</td><td>P4(a) holds</td></tr><tr><td> $V_q + 5\%$ </td><td>4.0000</td><td>0.7118</td><td>0.4077</td><td>1.1195</td><td>0.6358</td><td>0.3469</td><td>1.7967</td><td>0.3175</td><td>1.7261</td><td>0.4795</td><td>1.3374</td><td>0.67993</td><td> $D_{2,ws}^*$  decreases</td><td>P4(b) holds</td></tr><tr><td> $V_q + 10\%$ </td><td>4.0000</td><td>0.7118</td><td>0.4271</td><td>1.1389</td><td>0.6250</td><td>0.3409</td><td>1.7967</td><td>0.3175</td><td>1.7258</td><td>0.4584</td><td>1.3277</td><td>0.65858</td><td></td><td></td></tr><tr><td> $V_t/V + 1 \text{ pp}$ </td><td>4.0000</td><td>0.7228</td><td>0.3773</td><td>1.1000</td><td>0.6570</td><td>0.3430</td><td>1.7967</td><td>0.3175</td><td>1.7295</td><td>0.5148</td><td>1.3542</td><td>0.71561</td><td> $p_{2,ws}^*$  increases</td><td>P5(a) holds</td></tr><tr><td> $V_t/V + 5 \text{ pp}$ </td><td>4.0000</td><td>0.7668</td><td>0.3333</td><td>1.1000</td><td>0.6970</td><td>0.3030</td><td>1.7967</td><td>0.3175</td><td>1.7419</td><td>0.5717</td><td>1.3826</td><td>0.77304</td><td> $D_{2,ws}^*$  increases</td><td>P5(b) holds</td></tr><tr><td> $V_t/V + 10 \text{ pp}$ </td><td>4.0000</td><td>0.8218</td><td>0.2783</td><td>1.1000</td><td>0.7470</td><td>0.2530</td><td>1.7967</td><td>0.3175</td><td>1.7570</td><td>0.6695</td><td>1.4239</td><td>0.87171</td><td></td><td></td></tr></table>

<sub>pp,</sub> <sub>per</sub><sup>centage</sup> <sup>poi</sup>  
Table 4. Numerical Example Extension Results for Overlapping Innovators

<table><tr><td rowspan="2">What is changed</td><td rowspan="2">M</td><td rowspan="2"> $V_s$ </td><td rowspan="2"> $V_q$ </td><td rowspan="2">V</td><td rowspan="2"> $V_t/V$ </td><td rowspan="2"> $V_q/V$ </td><td rowspan="2"> $p_1^*$ </td><td rowspan="2"> $D_1^*$ </td><td colspan="2">No spillover</td><td colspan="2">Spillover</td><td rowspan="2">Result</td><td rowspan="2">Does proposition (P) hold also with spillover?</td></tr><tr><td> $p_{2,ns}^*$ </td><td> $D_{2,ns}^*$ </td><td> $p_{2,ws}^*$ </td><td> $D_{2,ws}^*$ </td></tr><tr><td>Initial setting</td><td>0.19444</td><td>0.00309</td><td>0.03781</td><td>0.04090</td><td>0.07547</td><td>0.92453</td><td>0.08333</td><td>0.11111</td><td>0.08333</td><td>0.22222</td><td>0.06651</td><td>0.29290</td><td></td><td></td></tr><tr><td>M+1%</td><td>0.19639</td><td>0.00309</td><td>0.03781</td><td>0.04090</td><td>0.07547</td><td>0.92453</td><td>0.08333</td><td>0.11111</td><td>0.08407</td><td>0.22733</td><td>0.06714</td><td>0.29805</td><td> $p_{2,ws}^*$  increases</td><td>P2 holds</td></tr><tr><td>M+5%</td><td>0.20417</td><td>0.00309</td><td>0.03781</td><td>0.04090</td><td>0.07547</td><td>0.92453</td><td>0.08333</td><td>0.11111</td><td>0.08702</td><td>0.24875</td><td>0.06971</td><td>0.31962</td><td> $D_{2,ws}^*$  increases</td><td></td></tr><tr><td>M+10%</td><td>0.21389</td><td>0.00309</td><td>0.03781</td><td>0.04090</td><td>0.07547</td><td>0.92453</td><td>0.08333</td><td>0.11111</td><td>0.09067</td><td>0.27783</td><td>0.07300</td><td>0.34883</td><td></td><td></td></tr><tr><td> $V_t+1\%$ </td><td>0.19444</td><td>0.00312</td><td>0.03781</td><td>0.04093</td><td>0.07541</td><td>0.92383</td><td>0.08333</td><td>0.11111</td><td>0.08343</td><td>0.22161</td><td>0.06653</td><td>0.29228</td><td> $p_{2,ws}^*$  increases</td><td>P3 holds</td></tr><tr><td> $V_t+5\%$ </td><td>0.19444</td><td>0.00324</td><td>0.03781</td><td>0.04105</td><td>0.07519</td><td>0.92105</td><td>0.08333</td><td>0.11111</td><td>0.08379</td><td>0.21925</td><td>0.06662</td><td>0.28991</td><td> $D_{2,ws}^*$  decreases</td><td></td></tr><tr><td> $V_t+10\%$ </td><td>0.19444</td><td>0.00340</td><td>0.03781</td><td>0.04120</td><td>0.07491</td><td>0.91760</td><td>0.08333</td><td>0.11111</td><td>0.08424</td><td>0.21650</td><td>0.06672</td><td>0.28713</td><td></td><td></td></tr><tr><td> $V_q+1\%$ </td><td>0.19444</td><td>0.00309</td><td>0.03819</td><td>0.04127</td><td>0.07478</td><td>0.91606</td><td>0.08333</td><td>0.11111</td><td>0.08329</td><td>0.22143</td><td>0.06645</td><td>0.29210</td><td> $p_{2,ws}^*$  decreases</td><td>P4(a) holds</td></tr><tr><td> $V_q+5\%$ </td><td>0.19444</td><td>0.00309</td><td>0.03970</td><td>0.04279</td><td>0.07214</td><td>0.88368</td><td>0.08333</td><td>0.11111</td><td>0.08311</td><td>0.21843</td><td>0.06622</td><td>0.28908</td><td> $D_{2,ws}^*$  decreases</td><td>P4(b) holds</td></tr><tr><td> $V_q+10\%$ </td><td>0.19444</td><td>0.00309</td><td>0.04159</td><td>0.04468</td><td>0.06908</td><td>0.84629</td><td>0.08333</td><td>0.11111</td><td>0.08289</td><td>0.21504</td><td>0.06594</td><td>0.28565</td><td></td><td></td></tr><tr><td> $V_t/V+1 pp$ </td><td>0.19444</td><td>0.00350</td><td>0.03740</td><td>0.04090</td><td>0.08547</td><td>0.91453</td><td>0.08333</td><td>0.11111</td><td>0.08458</td><td>0.21568</td><td>0.06685</td><td>0.28630</td><td> $p_{2,ws}^*$  increases</td><td>P5(a) holds</td></tr><tr><td> $V_t/V+5 pp$ </td><td>0.19444</td><td>0.00513</td><td>0.03576</td><td>0.04090</td><td>0.12547</td><td>0.87453</td><td>0.08333</td><td>0.11111</td><td>0.08902</td><td>0.19955</td><td>0.06822</td><td>0.26998</td><td> $D_{2,ws}^*$  decreases</td><td>P5(c) holds</td></tr><tr><td> $V_t/V+10 pp$ </td><td>0.19444</td><td>0.00718</td><td>0.03372</td><td>0.04090</td><td>0.17547</td><td>0.82453</td><td>0.08333</td><td>0.11111</td><td>0.09385</td><td>0.19067</td><td>0.06993</td><td>0.26093</td><td></td><td></td></tr><tr><td colspan="15">Note. pp, percentage point(s).</td></tr></table>

Table 3. Numerical Results for Overlapping Innovators for ve  vr  xe  xr  fe  fr  0.5

## 5. Conclusion

Online shopping has significantly changed the way people purchase products. Rating systems, which enable consumers to observe the distribution of ratings awarded by other consumers, have contributed to this change. Significant literature has emerged that seeks to understand the efects of diferent aspects of these rating systems—such as number, average, and variance—on product prices and consumer demand. Previous literature that analyzed the role of the variance of consumer ratings concentrated on ratings for products where the variance was caused solely by taste differences on search attributes and experience attributes (Sun 2012). However, a high variance of consumer ratings may also depend on quality diferences among instances of the product, such as whether a product fails. Our work makes an initial contribution toward understanding how the variance caused by taste diferences and quality diferences diferentially afects product price and demand.

We propose a model where both taste and quality diferences may cause variance in consumer ratings. We find that a higher variance caused by taste differences indicates that a product closely matches the tastes of some consumers and less closely matches the tastes of others, resulting in a higher price and lower demand. A higher variance caused by quality diferences suggests an unreliable product and is therefore associated with a lower price and lower demand. Our most surprising result is that for products with low variance, holding the average rating as well as the total variance of ratings constant while increasing the share of the variance caused by taste diferences increases optimal price and demand. Thus, counter to intuition, price and demand are capable of increasing concomitantly with a rise in the total variance of consumer ratings. Given the same average rating for two similar products, risk-averse consumers may prefer the higherpriced product with the higher total variance of ratings. Thus, our results suggest that considering taste differences and quality diferences as separate sources of variance in consumer ratings may be important when empirically analyzing the efects of consumer ratings on product pricing and consumer demand.

Our findings have important managerial implications. First, if retailers were to consider the composition of the variance of consumer’s ratings, then they could improve their sales forecasts and increase profits by adjusting their inventories accordingly to satisfy demand or by charging higher prices for those products for which a relatively larger share of the variance is caused by taste diferences. Second, they could implement mechanisms to explicitly communicate information about the decomposition of the variance to allow more consumers to use this important information in their decision making, which would further reduce uncertainty consumers have in e-commerce. There is empirical evidence that strongly suggests that consumers are able to digest information about rating distributions (e.g., Clemons et al. 2006, Sun 2012). Today, consumers can only indirectly infer this information by analyzing specific aspects of the ratings distribution, such as a peak in one-star ratings or by reading through the textual consumer reviews for a specific product. As a first step to making this information directly available, retailers may provide additional information on the percentage of the most negative consumer ratings caused by product failure. Retailers could collect this information by asking each consumer posting a negative rating whether it is based on product failure or on taste mismatch.

As with all research, the current study has limitations that present opportunities for future research. First, in our model, the two consumer groups (innovators and imitators) do not exhibit strategic behavior. However, consumers may consider the timing of purchase, and, hence, the timing of the consumer’s purchase decision could be endogenized (see, e.g., Guo and Villas-Boas 2007, Sun 2012). Sun (2012) allows for strategic behavior in an extension of her baseline model but finds qualitatively the same results compared to not allowing strategic behavior. Whether this also holds for the model proposed in this article remains to be analyzed. Second, pressure from regulators or consumer groups may cause retailers to consider a unique price across both periods that accounts for how consumers respond to ratings. Such a model would incorporate expectations of consumer ratings, and interesting insights may be gained regarding the balance of demand between innovators and imitators.

Third, our results suggest that consumers and retailers would benefit from information about the decomposition of the variance of consumer ratings, that is, which proportion of the variance is caused by taste diferences and which by quality diferences, although this information is sometimes revealed by the textual reviews. However, products sometimes have too many consumer reviews for consumers and retailers to read them all. To solve this issue, researchers could develop text-mining approaches or semantic techniques (e.g., as in Archak et al. 2011) that can identify the shares of variance caused by taste and quality diferences. Finally, our model generates testable predictions regarding the efect of the variance of consumer ratings on product price and consumer demand. The sign of this efect depends to a large degree on the source of this variance. This provides an interesting direction for further research, especially for field studies and experiments that investigate the efects of the variance of consumer ratings that consider the different sources of variance.

## Acknowledgments

The authors thank participants at the International Conference on Information Systems (2015), the INFORMS Conference on Information Systems and Technology (2015), and the workshops IS Design and Economic Behavior (2016) and Theory in Economics of Information Systems (2017) for valuable feedback. They also thank Dominik Gutt for his assistance in performing text mining on textual reviews and Jeanette Burman for helpful comments and editing.

## Appendix. Proofs of Propositions

Proof of Proposition 1. Diferentiating the optimal price and demand with respect to M and $V$ gives

$$
\begin{array}{l} \frac {\partial p _ {2} ^ {*}}{\partial M} = \frac {1}{2}, \quad \frac {\partial p _ {2} ^ {*}}{\partial V} = \frac {3}{4 \sqrt {3 V}}, \quad \frac {\partial D _ {2} ^ {*}}{\partial M} = \frac {k D _ {1} ^ {*}}{4 \sqrt {3 V}}, \quad \text { and } \\ \frac {\partial D _ {2} ^ {*}}{\partial V} = - \frac {3 M k D _ {1} ^ {*}}{8 (3 V) ^ {3 / 2}}. \end{array}
$$

Recall that $M , V ,$ and $D _ { 1 } ^ { * }$ are positive by definition. Thus, we have

$$
\frac {\partial p _ {2} ^ {*}}{\partial M} > 0, \quad \frac {\partial p _ {2} ^ {*}}{\partial V} > 0, \quad \frac {\partial D _ {2} ^ {*}}{\partial M} > 0, \quad \text { and } \quad \frac {\partial D _ {2} ^ {*}}{\partial V} <   0. \quad \text { Q.E.D. }
$$

Proof of Proposition 2. Rearranging (12) and diferentiating optimal price and demand with respect to M yields

$$
\frac {\partial p _ {2} ^ {*}}{\partial M} = \frac {\sqrt {2 V _ {t}} V _ {q}}{3 (M ^ {2} + V _ {q}) ^ {3 / 2}} + \frac {1}{3}
$$

and

$$
\begin{array}{r l} & {\frac {\partial D _ {2} ^ {*}}{\partial M} = \frac {k \tilde {\tau} _ {1} ^ {\theta = 0}}{2 7 z V _ {q}} \bigg (\sqrt {\frac {2 (M ^ {2} + V _ {q})}{V _ {t}}} + 2 \bigg)} \\ & {\qquad \cdot \bigg (V _ {q} + 4 M ^ {2} + \sqrt {2 V _ {t} (M ^ {2} + V _ {q})} + M ^ {2} \sqrt {\frac {2 V _ {t}}{M ^ {2} + V _ {q}}} \bigg).} \end{array}
$$

As M, $V _ { t } , V _ { q } , \tilde { \tau } _ { 1 } ^ { \theta = 0 } ,$ , k, and z are positive by definition, we have

$$
\frac {\partial p _ {2} ^ {*}}{\partial M} > 0 \quad \text { and } \quad \frac {\partial D _ {2} ^ {*}}{\partial M} > 0. \quad \text { Q.E.D. }
$$

Proof of Proposition 3. Rearranging (12) and diferentiating optimal price and demand with respect to $V _ { t }$ yields

$$
\frac {\partial p _ {2} ^ {*}}{\partial V _ {t}} = \frac {\sqrt {2} M}{6 \sqrt {V _ {t} (M ^ {2} + V _ {q})}}
$$

and

$$
\frac {\partial D _ {2} ^ {*}}{\partial V _ {t}} = - \frac {M k \tilde {\tau} _ {1} ^ {\theta = 0} \sqrt {2 V _ {t} (M ^ {2} + V _ {q})} (M ^ {2} + V _ {q} - 2 V _ {t})}{5 4 z V _ {q} V _ {t} ^ {2}}.
$$

As $M , V _ { t } , V _ { q } , k ,$ , and z are positive by definition, we have $\partial p _ { 2 } ^ { * } / \partial V _ { t } > 0$ . The sign of ${ \partial D _ { 2 } ^ { * } } / { \partial V _ { t } }$ depends solely on $( M ^ { 2 } +$ $V _ { q } \mathrm { ~ - ~ } 2 V _ { t } )$ , which is positive if $V _ { t } \stackrel { - } { < } M ^ { 2 } / 2 + \stackrel { . } { V } _ { q } / 2 .$ . From Assumption 2 we have $x \leq v$ . Rewriting this inequality in terms of $M , V _ { q } ,$ and $V _ { t }$ by using (9) and simplifying leads to $V _ { t } < ( \tilde { \tau } _ { 1 } ^ { \theta = 0 } ) ^ { 2 } ( \stackrel { \cdot \cdot } { M ^ { 2 } } + V _ { q } ) \stackrel { \cdot \cdot } { / } 2 ( \stackrel { \cdot \cdot } { \tilde { \tau } _ { 1 } ^ { \theta = 0 } } - \stackrel { \cdot \cdot } { 3 } ) ^ { 2 }$ . As $\tilde { \tau } _ { 1 } ^ { \theta = 0 } \stackrel { \cdot } { \in } [ 0 , 1 ] .$ , this contradicts $V _ { t } > M ^ { 2 } / 2 + \stackrel { \prime } { V _ { q } } / 2$ . Thus, $\partial D _ { 2 } ^ { * } / \partial \bar { V _ { t } } < 0$ . Q.E.D.

Proof of Proposition 4. Rearranging (12) and diferentiating optimal price and demand with respect to $V _ { q }$ yields

$$
\frac {\partial p _ {2} ^ {*}}{\partial V _ {q}} = - \frac {M ^ {2} V _ {t}}{3 (M ^ {2} + V _ {q}) ^ {2} \sqrt {(2 M ^ {2} V _ {t}) / (M ^ {2} + V _ {q})}}
$$

and

$$
\begin{array}{l} \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} \\ = - \frac {k \tilde {\tau} _ {1} ^ {\theta = 0} (8 M ^ {3} V _ {t} + \sqrt {\frac {2 M ^ {2} V _ {t}}{M ^ {2} + V _ {q}}} (2 M ^ {4} - V _ {q} ^ {2} + 2 V _ {q} V _ {t} + M ^ {2} V _ {q} + 4 M ^ {2} V _ {t}))}{5 4 z V _ {q} ^ {2} V _ {t}}. \end{array}\tag{A.1}
$$

For $( \mathsf { a } ) ,$ , as $M , V _ { t } ,$ , and $V _ { q }$ are positive by definition, we have $\partial p _ { 2 } ^ { * } / \partial V _ { q } < 0 .$

The sign of $\partial D _ { 2 } ^ { * } / \partial V _ { q }$ depends on the sign of the numerator of (A.1) and especially on the sign of the term in parentheses:

$$
8 M ^ {3} V _ {t} + \sqrt {\frac {2 M ^ {2} V _ {t}}{M ^ {2} + V _ {q}}} (2 M ^ {4} - V _ {q} ^ {2} + 2 V _ {q} V _ {t} + M ^ {2} V _ {q} + 4 M ^ {2} V _ {t}).\tag{A.2}
$$

For (b), (A.2) is positive if $2 M ^ { 4 } - V _ { q } ^ { 2 } + 2 V _ { q } V _ { t } + M ^ { 2 } V _ { q } +$ $4 M ^ { 2 } V _ { t } > 0$ . Solving this inequality for $V _ { q } ^ { ' } ,$ we get $V _ { a } < 2 M ^ { 2 }$ as a suficient condition for $( A \cdot 2 ) > { \dot { 0 } }$ and $\partial ^ { \aa } D _ { 2 } ^ { * } / \partial { \bar { V } } _ { q } < \dot { 0 }$

For $( \mathrm { c } ) ,$ , a necessary condition that (A.2) becomes negative is that $V _ { q } > 2 M ^ { 2 }$ . Taking $V _ { q } > 2 M ^ { 2 }$ and solving $( A . 2 ) = 0$ for $V _ { t }$ gives

$$
V _ {t} = \frac {(M ^ {2} + V _ {q}) (- 2 M ^ {2} + V _ {q}) ^ {2}}{2 (2 M ^ {2} + V _ {q}) ^ {2}}.
$$

As (A.2) is strictly increasing in $V _ { t } ,$ we have $\partial D _ { 2 } ^ { * } / \partial V _ { q } > 0$ if

$$
V _ {q} > 2 M ^ {2} \quad \mathrm{and} \quad V _ {t} <   \frac {(M ^ {2} + V _ {q}) (- 2 M ^ {2} + V _ {q}) ^ {2}}{2 (2 M ^ {2} + V _ {q}) ^ {2}}.\tag{Q.E.D.}
$$

Proof of Proposition 5. To analyze the efect of the relative share of $V _ { q }$ (which is the complement of the relative share of $V _ { t } )$ , we diferentiate (13) with respect to $V _ { q } .$ . Rearranging terms we have

$$
\frac {\partial p _ {2} ^ {*}}{\partial V _ {q}} = - \frac {\sqrt {2} M ^ {2} (M ^ {2} + V)}{6 (M ^ {2} + V _ {q}) ^ {2} \sqrt {(M ^ {2} (V - V _ {q})) / (M ^ {2} + V _ {q})}}
$$

and

$$
\begin{array}{l} \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} = \Lambda \left(M ^ {2} V _ {q} + V _ {q} ^ {2} + \frac {2 V _ {q} (V - V _ {q}) ^ {2}}{M ^ {2} + V _ {q}} - (V - V _ {q}) \left(4 (V - V _ {q}) \right. \right. \\ \left. \left. + 2 M ^ {2} + 4 M ^ {2} \sqrt {2 \frac {V - V _ {q}}{M ^ {2} + V _ {q}}} + V _ {q}\right)\right), \end{array} \tag {A.3}
$$

where

$$
\Lambda = \frac {\sqrt {2} M k \tilde {\tau} _ {1} ^ {\theta = 0}}{5 4 z V _ {q} ^ {2} \sqrt {((V - V _ {q}) ^ {3}) / (M ^ {2} + V _ {q})}} > 0.
$$

For (a), as $V _ { q }$ is by definition always smaller than $V ,$ we have $\partial p _ { 2 } ^ { * } / \partial V _ { q } < 0$ and, vice versa, $\partial p _ { > } ^ { * } \bar { / } \partial V _ { t } > 0$

For (b) and (c), our approach is to define segments of V and then address the behavior of (A.3) within the upper and lower segments. As $\Lambda > 0 ,$ , the sign of $( \mathrm { A } . 3 )$ depends only on the sign of the long term in parentheses:

$$
\begin{array}{l} M ^ {2} V _ {q} + V _ {q} ^ {2} + \frac {2 V _ {q} (V - V _ {q}) ^ {2}}{M ^ {2} + V _ {q}} \\ \qquad - (V - V _ {q}) \bigg (4 (V - V _ {q}) + 2 M ^ {2} + 4 M ^ {2} \sqrt {2 \frac {V - V _ {q}}{M ^ {2} + V _ {q}}} + V _ {q} \bigg). \end{array}\tag{A.4}
$$

We have that (A.4) is strictly increasing in $V _ { q }$ for $V _ { q } \in [ 0 , V ]$ and strictly decreasing in $V .$

From Assumption 2 that $x _ { r } \in [ 0 , v _ { r } ]$ and our definition of taste with $\tilde { \tau } _ { 2 } ^ { \theta = 0 } \in [ 0 , 1 ]$ , we get lower and upper bounds for $V _ { q } .$ To calculate the lower bound for $V _ { q } ,$ , we take the upper bound of mismatch costs ${ x _ { r } = v _ { r } }$ . For this case, $V _ { t }$ is maximal and, consequently, $V _ { q }$ is minimal for a constant total variance. Using the equations for $v _ { r }$ and $x _ { r }$ from $( 9 ) ,$ , substituting $V _ { t }$ by $V - V _ { q } ,$ , setting $x _ { r } = v _ { r }$ , and solving for $V _ { q } ,$ , we get the lower bound of $V _ { q } .$ To calculate the upper bound for $V _ { q } ,$ we use the taste of the indiferent second-period consumer with zero risk premium, $\tilde { \tau } _ { 2 } ^ { \theta = 0 } = ( v _ { r } ( 1 - f _ { r } ) \mathring { - p } _ { 2 } ) / ( x _ { r } ( 1 - f _ { r } ) )$ . Using the equations for $v _ { r } , x _ { r } ,$ , and $f _ { r }$ from (9) and the equation for $p _ { 2 }$ from (12), substituting $V _ { t }$ by $V \mathrm { ~ - ~ } V _ { q } ,$ , and diferentiating $\widetilde { \tau } _ { 2 } ^ { \theta = 0 }$ with respect to $V _ { q } ,$ , we find that $\widetilde { \tau } _ { 2 } ^ { \theta = \mathrm { { 0 } } }$ is strictly increasing in $V _ { q } .$ . Thus, we take the upper bound of $\widetilde { \tau } _ { \gamma } ^ { \theta = 0 } = 1$ and solve the equation for $V _ { q }$ to get the upper bound of $V _ { q }$ . The resulting lower and upper bounds for $V _ { q }$ are given by

$$
\begin{array}{c} V _ {q} ^ {l} = V - \frac {(\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} (M ^ {2} + V)}{3 ((\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} - 4 \tilde {\tau} _ {1} ^ {\theta = 0} + 6)} \leq V _ {q} \\ \leq \frac {(4 V - 2 M ^ {2}) (\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} - 3 6 V \tilde {\tau} _ {1} ^ {\theta = 0} + 8 1 V}{6 (\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} - 3 6 \tilde {\tau} _ {1} ^ {\theta = 0} + 8 1} = V _ {q} ^ {u}. \end{array}
$$

Both $V _ { q } ^ { l }$ and $V _ { q } ^ { u }$ are increasing in $V .$

Suppose $\mathrm { ( A . 4 ) }$ and, therefore, (A.3) are equal to zero. Inserting $V _ { q } ^ { u }$ and $V _ { a } ^ { l } ,$ respectively, into (A.4) and setting (A.4) $= 0 ,$ , we solve for $V$ and obtain

$$
\underline {{V}} = \frac {2 M ^ {2} (\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} (4 \tilde {\tau} _ {1} ^ {\theta = 0} - 2 7)}{(2 \tilde {\tau} _ {1} ^ {\theta = 0} - 9) ^ {2} (4 \tilde {\tau} _ {1} ^ {\theta = 0} - 9)} \text {   for   the   upper   bound   of   } V _ {q}, V _ {q} ^ {u}
$$

and

$$
\bar {V} = \frac {M ^ {2} (\tilde {\tau} _ {1} ^ {\theta = 0}) ^ {2} (\tilde {\tau} _ {1} ^ {\theta = 0} - 9 / 2)}{(2 \tilde {\tau} _ {1} ^ {\theta = 0} - 3) (\tilde {\tau} _ {1} ^ {\theta = 0} - 3) ^ {2}} \text {   for   the   lower   bound   of   } V _ {q}, V _ {q} ^ {l}
$$

To show that $\bar { V } \geq \underline { { V } } .$ , we subtract $\underline { V }$ from $\bar { V } .$ By rearranging terms we get

$$
M ^ {2} \left(\tilde {\tau} _ {1} ^ {\theta = 0}\right) ^ {2} \left(\frac {\tilde {\tau} _ {1} ^ {\theta = 0} - 4 , 5}{\left(\tilde {\tau} _ {1} ^ {\theta = 0} - 3\right) ^ {2} \left(2 \tilde {\tau} _ {1} ^ {\theta = 0} - 3\right)} + \frac {5 4 - 8 \tilde {\tau} _ {1} ^ {\theta = 0}}{\left(9 - 2 \tilde {\tau} _ {1} ^ {\theta = 0}\right) ^ {2} \left(4 \tilde {\tau} _ {1} ^ {\theta = 0} - 9\right)}\right) \geq 0. \tag {A.5}
$$

As $M ^ { 2 } ( \tilde { \tau } _ { 1 } ^ { \theta = 0 } ) ^ { 2 }$ is positive, the sign of (A.5) depends only on the two terms in parentheses. The first term is strictly positive, and the second term is strictly negative. However, for each and every $\tilde { \tau } _ { 1 } ^ { \theta = 0 } \in [ 0 , 1 ]$ , the first term has a greater absolute value compared to the second term. Consequently, we have $\bar { V } \geq { \underline { { V } } }$ (the equality results from the case where $\tilde { \tau } _ { 1 } ^ { \theta = 0 } = 0 )$

<sup>¯</sup>Thus, we have three segments of the total variance: low, $V < \underline V ;$ medium, $\underline { { { V } } } \leq V \leq \breve { \bar { V } } ;$ and high, $\bar { V } < V$ . The delimiters <sup>¯ ¯</sup>of the segments, V<sup>¯</sup> and $\smash { \underline { { V } } _ { \varepsilon } }$ , are each defined by two conditions: $\partial D _ { 2 } ^ { * } / \partial V _ { q } ^ { - } = 0$ <sup>¯</sup>(defined by (A.3) and (A.4)) and $V _ { q } = V _ { q } ^ { l }$ or $V _ { q } =$ $V _ { q } ^ { u }$ , respectively.

For (b), when the total variance is low, $V < \underline V$ . Suppose $V _ { q } = V _ { q } ^ { u }$ . Then, because $V _ { q } ^ { u }$ is increasing in $V ,$ the resulting $V _ { q } ^ { \dot { u } }$ is lower, and (A.4) is increasing in $V _ { q } .$ . Consequently, (A.4) and, hence, (A.3) are negative at $V _ { q } = V _ { q } ^ { \dot { u } }$

$$
\left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} \right| _ {V _ {q} = V _ {q} ^ {u}} <   0 \implies \left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {t}} \right| _ {V _ {q} = V _ {q} ^ {u}} > 0.
$$

As $\partial D _ { 2 } ^ { * } / \partial V _ { q }$ is increasing in $V _ { q } ,$ we have

$$
\left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} \right| _ {V _ {q} <   V _ {q} ^ {u}} <   0 \implies \left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {t}} \right| _ {V _ {q} <   V _ {q} ^ {u}} > 0.
$$

For (c), when the total variance is high, $\bar { V } < V$ . Suppose $V _ { q } = V _ { q } ^ { l }$ . Then, because $V _ { q } ^ { l }$ is increasing in $V ,$ the resulting $V _ { q } ^ { \dot { l } }$ is higher, and (A.4) is increasing in $V _ { q } .$ . Using the same reasoning as in (b) above, (A.4) and, hence, (A.3) are positive at $V _ { q } = \breve { V _ { q } ^ { l } } .$

$$
\left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} \right| _ {V _ {q} = V _ {q} ^ {l}} > 0 \implies \left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {t}} \right| _ {V _ {q} = V _ {q} ^ {l}} <   0.
$$

And with $\partial D _ { 2 } ^ { * } / \partial V _ { q }$ is increasing in $V _ { q } ,$ , we have

$$
\left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {q}} \right| _ {V _ {q} > V _ {q} ^ {l}} > 0 \implies \left. \frac {\partial D _ {2} ^ {*}}{\partial V _ {t}} \right| _ {V _ {q} > V _ {q} ^ {l}} <   0. \quad \text { Q.E.D. }
$$

## References

Amazon (2015) Customer reviews: Beats urBeats in-ear headphone. Accessed September 11, 2018, http://www.amazon .com/product-reviews/B00F5OOQ5Q/ref<sup></sup>psdc\_2266981011\_r0 \_B00F5OOQ5Q?\_encoding=UTF8&showViewpoints=1.

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Babic Rosario A, Sotgiu F, De Valck K, Bĳmolt TH (2016) The efect of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric factors. J. Marketing Res. 53(3): 297–318.

Bai X, Marsden JR, Ross WT Jr, Wang G (2017) How e-WOM and local competition drive local retailers’ decisions about daily deal oferings. Decision Support Systems 101:82–94.

Bardey D (2004) A paradoxical risk aversion efect on the consumers’ demand for quality. Recherches économiques de Louvain 70(1): 109–115.

Bass FM (1969) A new product growth for model consumer durables. Management Sci. 15(5):215–227.

Bhatnagar A, Misra S, Rao HR (2000) On risk, convenience, and Internet shopping behavior. Comm. ACM 43(11):98–105.

Chen P-YS, Wu S, Yoon J (2004) The impact of online recommendations and consumer feedback on sales. Proc. Internat. Conf. Inform. Systems, 711–724.

Chen Y, Xie J (2008) Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management Sci. 54(3):477–491.

Chevalier J, Mayzlin D (2006) The efect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Chintagunta PK, Gopinath S, Venkataraman S (2010) The efects of online user reviews on movie box ofice performance: Accounting for sequential rollout and aggregation across local markets. Marketing Sci. 29(5):944–957.

Clemons E, Gao G, Hitt LM (2006) When online reviews meet hyperdiferentiation: A study of the craft beer industry. J. Management Inform. Systems 23(2):149–171.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Dellarocas C, Zhang XM, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Drewnicki N (2013) Survey: 90% say positive reviews impact purchase decisions. Accessed September 11, 2018, http://www .reviewpro.com/survey-zendesk-mashable-dimensional-research -90-say-positive-reviews-impact-purchase-decisions-26016#sthash .c9enKPvk.dpuf.

Duan W, Gu B, Whinston A (2008) Do online reviews matter? An empirical investigation of panel data. Decision Support Systems 45(4):1007–1016.

Economist (2016) Will customer ratings for airlines prove as important as those of hotels? (July 12), https://www.economist.com/ blogs/gulliver/2016/07/under-reviewed.

Engel JF, Kegerreis RJ, Blackwell RD (1969) Word-of-mouth communication by the innovator. J. Marketing 33(3):15–19.

Godes D, Mayzlin D (2004) Using online conversations to study word of mouth communication. Marketing Sci. 23(4):545–560.

Guo L, Villas-Boas JM (2007) Consumers stockpiling and price competition in diferentiated markets. J. Econom. Management Strategy 16(4):827–858.

Gutt D, Herrmann P (2015) Sharing means caring? Hosts’ price reaction to rating visibility. Proc. 23rd Eur. Conf. Inform. Systems.

Harmon A (2004) Amazon glitch unmasks war of reviewers. New York Times (February 14, 2004), http://www.nytimes.com/2004/ 02/14/us/amazon-glitch-unmasks-war-of-reviewers.html.

Herrmann P, Kundisch D, Zimmermann S, Nault BR (2015) How do diferent sources of the variance of consumer ratings matter? Proc. Internat. Conf. Inform. Systems.

Holt CA, Laury SK (2002) Risk aversion and incentive efects. Amer. Econom. Rev. 92(5):1644–1655.

Hong Y, Chen P, Hitt LM (2012) Measuring product type with dynamics of online product review variance. Proc. Internat. Conf. Inform. Systems.

Hu N, Pavlou PA, Zhang J (2017) On self-selection biases in online product reviews. MIS Quart. 41(2):449–471.

Ikkala T, Lampinen A (2014) Defining the price of hospitality: Networked hospitality exchange via Airbnb. Proc. 17th ACM Conf. Comput. Supported Cooperative Work Soc. Comput. (ACM, New York), 173–176.

Ikkala T, Lampinen A (2015) Monetizing network hospitality: Hospitality and sociability in the context of Airbnb. Proc. 18th ACM Conf. Comput. Supported Cooperative Work Soc. Comput. (ACM, New York), 1033–1044.

Klein L (1998) Evaluating the potential of interactive media through a new lens: Search versus experience goods. J. Bus. Res. 41(3): 195–203.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Lewis G, Zervas G (2016) The welfare impact of consumer reviews: A case study of the hotel industry. Working paper, Microsoft Research and NBER.

Li X, Hitt LM (2008) Self-selection and information role of online product reviews. Inform. Systems Res. 19(4):456–474.

Li X, Hitt LM (2010) Price efects in online product reviews: An analytical model and empirical analysis. MIS Quart. 34(4): 809–831.

Lu Q, Ye Q, Law R (2014) Moderating efects of product heterogeneity between online word-of-mouth and hotel sales. J. Electronic Commerce Res. 15(1):1–12.

Luca M, Zervas G (2016) Fake it till you make it: Reputation, competition, and Yelp review fraud. Management Sci. 62(12): 3412–3427.

Markopoulos PM, Clemons E (2013) Reducing buyers uncertainty about taste-related product attributes. J. Management Inform. Systems 30(2):269–299.

Mayzlin D (2006) Promotional chat on the internet. Marketing Sci. 25(2):155–163.

Nelson P (1981) Consumer information and advertising. Galatin M, Leiter RD, eds. Economics of Information (Springer, Dordrecht), 42–77.

Rogers EM (1962) Difusion of Innovation (Free Press, New York).

Shapiro C (1983) Optimal pricing of experience goods. Bell J. Econom. 14(2):497–507.

Sridhar S, Srinivasan R (2012) Social influence efects in online product ratings. J. Marketing 76(5):70–88.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Teubner T, Hawlitschek F, Dann D (2017) Price determinants on AirBnB: How reputation pays of in the sharing economy. J. Self-Governance Management Econom. 5(4):53–80.

Wei D, Nault B (2013) Experience information goods: Version-toupgrade. Decision Support Systems 56:494–501.

Wu C, Che H, Chan TY, Lu X (2015) The economic value of online reviews. Marketing Sci. 34(5):739–754.

Wu J, Wu Y, Sun J, Yang Z (2013) User reviews and uncertainty assessment: A two stage model of consumers’ willingness-topay in online markets. Decision Support Systems 55:175–185.

Ye Q, Law R, Gu B (2009) The impact of online user reviews on hotel room sales. Internat. J. Hospitality Management 28(1):180–182.

Ye Q, Law R, Gu B, Chen W (2011) The influence of user-generated content on traveler behavior: An empirical investigation on the efects of e-word-of-mouth to hotel online bookings. Comput. Human Behav. 27(2):634–639.
