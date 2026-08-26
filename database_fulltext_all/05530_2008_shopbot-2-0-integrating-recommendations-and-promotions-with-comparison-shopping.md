---
otero_id: 5530
otero_key: "PMXHQHVK"
title: "Shopbot 2.0: Integrating recommendations and promotions with comparison shopping"
authors: "Robert Garfinkel; Ram Gopal; Bhavik Pathak; Fang Yin"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.05.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Shopbot 2.0: Integrating recommendations and promotions with comparison shopping

Robert Garfinkel <sup>a,1</sup>, Ram Gopal <sup>a,2</sup>, Bhavik Pathak <sup>b,3</sup>, Fang Yin <sup>a,</sup>⁎

<sup>a</sup> Department of Operations and Information Management, University of Connecticut, Storrs, CT 06269, United States

<sup>b</sup> Department of Decision Sciences, Indiana University South Bend, South Bend, IN 46634, United States

## a r t i c l e i n f o

Article history: Received 17 September 2007 Received in revised form 5 March 2008 Accepted 21 May 2008 Available online 3 June 2008

Keywords: Recommender systems Sales promotions Shopbots Online retailing

## a b s t r a c t

The current generation of shopbots reduce consumer search costs associated with determining the best purchase price and place to buy a product predetermined by the shopper. In order to provide better service to shoppers, the service horizon of these shopbots can be extended in several dimensions. In this paper, we suggest that shopbots can integrate retail promotions and incorporate recommender systems in order to provide greater values to their users. Although the majority of online retailers already provide recommender systems, we show that pro<sup>fi</sup>t maximizing retailers may not always provide transparent recommendations and argue that shopbots are in the better position to offer such recommendations. We develop integer programming models for shopbots to integrate sales promotions and product recommendations. We validate our model by using product recommendation data from two popular online retailers, Amazon.com and Buy.com, to show that our model provides recommendations that offer better value to the price sensitive shopbot customers.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Shopbots or comparison shopping agents, which are websites providing online comparison shopping services to millions of shoppers every day, have been helping reduce the search cost of price and retailer-related information on the Web, and thereby improving market ef<sup>fi</sup>ciency. They allow shoppers to search for and compare prices and inventory information of goods across a large number of sellers. Some shopbots also provide information on sellers' service quality. Research on shopbots has focused on technical issues such as shopbot interface [12], consumer behavior issues such as price sensitivity and brand loyalty [5,18], and retailer behavior issues such as price dispersion and competition [5,10,17].

The service currently provided by the majority of shopbots is relatively narrow in the sense that it only allows shoppers to compare prices of a single product of which they are already aware. The service horizon of shopbots could possibly be expanded in several dimensions. For example, since current shopbots focus almost exclusively on searches for a single item, models for <sup>fi</sup>nding the best price for a bundle of items have been proposed [8]. Such models may reduce the search costs for those shoppers who are interested in purchasing a bundle of items. Another possible dimension to expand the shopbot service horizon could be to integrate sales promotion information into the search results presented to shoppers. As business to consumer electronic commerce continues to grow and the competition among online retailers becomes more intense, retailers turn to various strategies to attract sales on the Web. One common strategy is to offer promotions to compete with other retailers on prices. For example, many retailers offer free shipping for a minimum purchase. “Dollaroff” and “percentage-off” promotions for a minimum purchase are also very common among online retailers. As shopbots are particularly appealing to price sensitive shoppers [15] who usually seek various sales promotions, it would increase the value of shopbot service to shoppers to integrate sales promotion information into the price quotes presented by shopbots.

![](/api/attachments/PMXHQHVK/fulltext/images/87641d521485a26015462e9f21ec36b96896338df415bc3c8f42ca397022d6cb.jpg)  
Fig. 1. A book webpage from Amazon.com.

Yet another possible way to expand shopbots service is to incorporate recommender systems. The proliferation of SKUs at various online retailers has made shoppers' product selection problem more complex. Online retailers have started providing value-added services such as product reviews and ratings as well as recommendations in order to facilitate shoppers' purchase decision making. These different forms of digital word of mouth reduce the uncertainty that is associated with the purchase of unfamiliar products, especially those products for which quality is dif<sup>fi</sup>cult or impossible to evaluate before purchase and usage. Given the high volume of traf<sup>fi</sup>c to popular shopbot websites, integration of consumer-centric, product-speci<sup>fi</sup>c decision support systems, such as recommender systems, into shopbots may provide more value to the shoppers by reducing their product-speci<sup>fi</sup>c search costs. None of the popular shopbots provides state-ofthe-art recommender service similar to those provided by major e-tailors such as Amazon. Therefore, this research proposes an approach based on integer programming to integrate both sales promotion information and product recommendation service with current price comparison service of shopbots to create a next generation shopping agent, which we term shopbots 2.0. Next, we use a simple example from the recommender system implemented by Amazon.com to illustrate our approach to integrating promotions and recommender systems with shopbots and to provide context for the discussion in later sections.

Amazon.com<sup>4</sup> has become the dominant player in the online book industry with a market share of more than 60% [11]. Amazon.com was also among the <sup>fi</sup>rst online retailers to offer recommendations. On every product page as shown in Fig. 1, the pricing, availability, and version information are listed <sup>fi</sup>rst for a given book (the base item). Then a single recommended item (hereafter termed best bet) is offered under “Better Together”, along with the total price of the twobook package. Furthermore, a group of <sup>fi</sup>ve related books (hereafter termed choice set) is also provided under the title “Customers who bought this item also bought”. The items in the choice set are those that were purchased the most by other shoppers who also purchased the base item. The order of the items in the choice set is transparently determined by a published recommendation algorithm in order of the relatedness of those items to the base item. Therefore, when the best bet is a member of the choice set, the resulting two-book bundle consists of strongly related books. Selecting a best bet is a business decision of Amazon.com and is therefore not transparent to the customer. Simply selecting a best bet from the choice set may increase the probability of it being sold, but it may not ful<sup>fi</sup>ll the possible pro<sup>fi</sup>t maximization objective of a retailer. As a pro<sup>fi</sup>t maximizing economic agent, Amazon.com may select a best bet that may provide maximum pro<sup>fi</sup>tability based on the contribution from a candidate best bet and probability of it being sold. We will see that there are many instances in which the best bet does not come from the choice set, as illustrated in Fig. 2.

![](/api/attachments/PMXHQHVK/fulltext/images/c53ab242826d1f4b9485b26cc189519e0bb801904d404d79a4159ab0e7182cf4.jpg)  
Fig. 2. The best bet is not from the choice set.

While many online retailers offer savings in the form of promotions as well as using recommender services, we will see that there are many instances in which the latter do not consider the former in their decision making. In particular, based on our observation of Amazon.com, when the best bet comes from the choice set its selection is based purely on its relatedness score. In many situations, an item from the choice set that is slightly different in terms of its relatedness but, combined with the base item, takes advantage of current promotions, could have been the best bet, and would undoubtedly have been more appealing to price sensitive shoppers.

For example, for the book “The Blind Side” as the base item, Amazon's best bet is “Money Ball”, which is <sup>fi</sup>rst in the choice set. However, the total order value of these two books is \$24.88, twelve cents less than the minimum order amount to qualify for free shipping, and thus a shopper would have to pay \$29.86 in total including the shipping cost of \$4.98.

This leaves open the possibility of selecting another item from the choice set costing as little as thirteen cents more and thus saving almost <sup>fi</sup>ve dollars.<sup>5</sup> However, if the base item is purchased with the book “Losers” from the choice set, the total cost is only \$25.62 with free shipping. Obviously, if the shopper is price sensitive, and the relatedness of the two recommended items are not too different from each other, which is very likely since both are from the choice set, recommending the second item would more likely lead to a sale. Since there are many different types of promotions offered by retailers such as x dollars off order of y dollars or more and buy one product and get another for free, etc., it is a non-trivial task to identify the optimal recommendation that would provide the most value for shoppers. We develop an integer programming model to solve this problem. It would also be interesting to see whether the outcome of our solution would result in signi<sup>fi</sup>cant possible savings for shoppers compared to the recommendation yielded by current recommender systems.

In summary, we introduce a new research perspective for shopbots: the possibility of integrating recommendations partially based on retailer sales promotions into current shopbots services. We motivate our research by observing the current practice of retailer recommendations. We also argue that shopbots are in the best position to integrate the two, and we provide an integer programming model that could be implemented for such integration. The potential savings are veri<sup>fi</sup>ed using a data set assembled from online book retailers. The remainder of the paper proceeds as follows. Related literature and industry background are discussed in Section 2. Section 3 presents an integer programming model to optimize the recommendations for shopbots and the empirical valida tion of the model and conclusions are given in Section 4.

## 2. Recommender systems and the online book industry

Following the seminal paper of Nelson [14], there has been a rich literature on consumer behavior in purchasing experience goods such as books, movies, and concerts, for which it is relatively easier to assess quality after actual consumption. The basic theme of the theory is that since it is usually very costly, and sometimes even impossible, to evaluate the quality of experience goods, shoppers turn to other sources of information on product quality when making purchase decisions. Empirical studies have shown the impact of product information on demand from various sources such as pricing [2], advertising [15], and expert reviews [4,16]. Since the explosion of Internet usage, this line of research has expanded to study the impact of digital word of mouth [3] and even peer-to-peer <sup>fi</sup>le sharing [9].

Online recommendation systems can be considered to be another source of product quality information that is based on the past purchasing/browsing behavior of shoppers. It bears close resemblance to word of mouth. However, in contrast to the lack of control of word of mouth, a retailer has full control over what algorithm to use for the recommendation system and how to present the recommendations. One is not required to purchase a product before reviewing it. Recommendations differ in that they are typically made based on actual purchases, and therefore can be considered to be more objective than customer reviews and ratings.

Shoppers follow two-stage decision making while purchasing a book. The <sup>fi</sup>rst stage consists of <sup>fi</sup>nding a preferred book among many alternatives and in the second stage shoppers seek the best place to purchase a book and usually this decision is based on price. Books are experience goods during the <sup>fi</sup>rst stage of decision making and quasi-commodity in the second stage of decision making [6]. Recommender systems assist shoppers in the <sup>fi</sup>rst stage of decision making and hence in the context of our work, we consider books as experience goods. As a typical example of experience goods, books have been the object of numerous studies on electronic commerce theory and practice because of the homogeneity of the product across different retailers, and the large number of products available for sampling. These are also the reasons for choosing books as the object of observation in this study. In addition, there is one more feature of books that is uniquely appealing in the current context. Recommended items for books are almost always other books, which makes it easier to compare across different retailers. In contrast, recommendations for other products could be from completely different product categories across different retailers.

The effectiveness of recommendations has been studied extensively, based on various technical measures of the accuracy of recommendations. However, these measures do not re<sup>fl</sup>ect the business value of recommendations to shoppers [1]. While the relatedness of a recommended item to the base item should be an important criterion of the usefulness of the recommendation, its appeal to a shopper is also crucial. If, for instance, a shopper decides not to purchase the best bet, its business value is zero no matter how closely it is related to the base item. On the other hand, if an item that is a little less related to the base item but much more appealing to the shopper is substituted, it would more likely result in a sale. To many shoppers, the appeal of an item is very much related to the price of, and potential savings resulting from its purchase.

The Amazon free shipping example of the previous section shows that recommendations provided by retailers may not be fully aligned with other initiatives and incentives to maximize their value to shoppers. Although there could be many measures of the appeal of an item to a shopper, we believe that price and resulting savings are always among the most important ones for homogeneous products like books. In general the items in the choice set are not very different in terms of how related they are to the base item. Thus, when the best bet comes from the choice set, it may be possible to choose an alternative member of that choice set to increase the value of the recommendation to a shopper by conserving relatedness and simultaneously yielding <sup>fi</sup>nancial bene<sup>fi</sup>ts.

Retailers as pro<sup>fi</sup>t maximizers may also adopt a recommendation strategy to select alternate best bets from outside of the choice sets. For instance they may be interested in cross-selling slow-moving items by tagging them along with fast-moving items. Retailers could also use the best bet to provide a subtle way for publishers or authors to promote their own books [7,13]. In order to understand such strategies, we collected Amazon.com's recommendation data to run a logistic regression. The binary dependent variable indicates whether the best bet is from the choice set (value is one) or not. The independent variables are sales rank, list price, Amazon price, number of reviews, and average star ratings of the base item. Here, the sales rank of a book is a number specifying the relative position of a book in terms of its sales quantity on Amazon.com, number of reviews is the total number of customer feedbacks received for a product on Amazon.com, average star ratings is the aggregated rating for a product, on the scale of 1 to 5, provided by customers. We ran the regression on the top 100, 500, and 1000 books on a randomly chosen day. The results are shown in Table 1.

Table 1 Results of logistic regressions (\*\*p b .01; \*p b .05)

<table><tr><td>Dependent variable</td><td colspan="3">Best bet is from the choice set</td></tr><tr><td rowspan="2">Sales rank</td><td>0.0173*</td><td>0.00415**</td><td>0.00249**</td></tr><tr><td>(0.00799)</td><td>(0.000825)</td><td>(0.000338)</td></tr><tr><td rowspan="2">List price</td><td>-0.2705</td><td>-0.1499**</td><td>-0.1486**</td></tr><tr><td>(0.1617)</td><td>(0.0543)</td><td>(0.0482)</td></tr><tr><td rowspan="2">Amazon price</td><td>0.4001</td><td>0.2071*</td><td>0.2260**</td></tr><tr><td>(0.2799)</td><td>(0.0891)</td><td>(0.0803)</td></tr><tr><td rowspan="2">No. of reviews</td><td>-0.00211**</td><td>-0.00084**</td><td>-0.00049**</td></tr><tr><td>(0.000735)</td><td>(0.000286)</td><td>(0.000158)</td></tr><tr><td rowspan="2">No. of stars</td><td>-0.0222</td><td>0.0828</td><td>0.3598*</td></tr><tr><td>(0.4659)</td><td>(0.2037)</td><td>(0.1666)</td></tr><tr><td>Number of observations</td><td>100</td><td>477</td><td>949</td></tr><tr><td>Likelihood ratio</td><td>27.826</td><td>64.9157</td><td>112.7013</td></tr><tr><td>Chi-square</td><td>(p&lt;.0001)</td><td>(p&lt;.0001)</td><td>(p&lt;.0001)</td></tr><tr><td>Odds ratio estimate for sales rank</td><td>1.017</td><td>1.004</td><td>1.002</td></tr></table>

The coef<sup>fi</sup>cients for sales rank and number of reviews are signi<sup>fi</sup>cant across the three regressions, indicating that the more popular a base item book is (lower sales rank and higher number of reviews), the more likely that the corresponding best bet will come from outside of the choice set. It is important to note here that as the sales rank speci<sup>fi</sup>es the relative position of the book in terms of the sales quantity, lower sales rank implies higher sales quantity and hence more popularity. The impact gets stronger as popularity increases. The odds ratio measures the marginal increase in probability per unit increase of rank, which is 1.7% for the top 100, 0.4% for the top 500, and 0.2% for the top 1000 ranked books. These results suggest that there exists a correlation between the popularity of the base item and the likelihood that items not necessarily related to the base item being recommended. Even though we cannot identify the real motive behind such business practice, it is obvious that retailers do not always recommend the most related items.

## 3. Choosing the optimal best bet from the choice set

Since discounts and promotions can be of various types, such as: free shipping; <sup>fi</sup>xed amount or <sup>fi</sup>xed percentage of price reduction for a bundle; or “buy one get one for free”, the problem of <sup>fi</sup>nding an “optimal” best bet for a price sensitive shopper is complex. We provide an integer programming model to solve this problem. The model can be implemented by any entity to provide additional service to shoppers. In particular we argue that shopbots are in an ideal position to provide this value-added service to millions of shoppers.

## 3.1. Savings are possible

When best bets are chosen from the choice set, the default choice for Amazon.com is always the top book in the list. To verify that savings can result by relaxing that restriction, we collected data from Amazon.com during June 2005. First, we calculated the baseline savings resulting from the Amazon best buy as the difference between the list prices and the prices charged by Amazon (henceforth called retailer prices) for the bundle. Then, starting from the top of the choice set, we calculated the savings resulting from purchasing the bundle of the base itemwith each item in the choice set. If the savings were higher than the baseline savings, this item was marked as an alternate best bet. The shipping cost is included in the calculation of savings. We also restricted the alternate bundles to those with total cost no greater than the baseline bundle total cost, so that the resulting extra savings are comparable to the baseline savings. The only available promotion during the data collection period was free shipping for a minimum purchase of \$25.

We did the above analysis for the top 100 selling books on a randomly chosen day. Out of these 100 books, we found alternate best buys with greater savings for 62 books. The average savings from purchasing the alternate bundle were \$14.98, which is signi<sup>fi</sup>cantly higher than the average baseline savings of \$12.07. These results show that there exists the possibility of modifying best buys to increase savings while maintaining a high degree of usefulness as measured by relatedness.

## 3.2. The role of shopbots

The current generation of shopbots provide price and retailer based search-cost solutions to primarily price sensitive shoppers. They are not designed to take into account either promotions or recommendations. That is, through their Web searches, they are not able to tell the shoppers which items are recommended by various retailers to go with the requested item. More critically, even with access to retailers' recommendations, they are not designed to <sup>fi</sup>nd the best price among all retailers that takes into account all of the promotions that are available, while restricting the purchase to the base item plus a recommended item. This provides a great opportunity for improving shopbot design by incorporating both mechanisms – promotions and recommendations – into current shopbot services.

In contrast, even though retailers could implement the same mechanism in their recommender systems, as indicated earlier this might not be in their own best interest in terms of pro<sup>fi</sup>t maximization. Retailers might recommend items based on concerns other than the relatedness of items, such as inventory clearance, targeted promotions of writers or books, etc. On the other hand, since shopbots do not possess or sell the items but only provide information that may lead to sales, shopbots can always provide such recommendations based on relatedness and promotions to shoppers. Furthermore, since each retailer's recommendations are uniquely based on the historical data each retailer possesses, recommendations are likely to vary across retailers. Shopbots can aggregate recommendations from different retailers to provide a more accurate prediction. Based on the same logic, shopbots might even be able to integrate a customer's purchase data from different retailers, which also leads to potentially more accurate prediction. In addition, shopbot shoppers are shown to be particularly price sensitive [5]. Therefore, we introduce a new research perspective for shopbots: the possible role of shopbots to integrate recommendations and sales promotions into their current service.

## 3.3. An integer programming model

Next we develop an integer programming model that is meant to be implemented by a shopbot to combine various promotions with recommendations to maximize the savings of recommended items to shoppers. The model is speci<sup>fi</sup>c to a given retailer, so that the overall model for a shopbot should consist of a number of independent models, one for each retailer since the base item is a singleton.

## 3.3.1. Promotion

Here we enumerate three of the most common types of promotions offered by retailers. These are incorporated into the integer programming model. Naturally, other promotion types could be modeled as well.

Free Items: One free item can be received for any order that consists of at least another given number of purchased items, and where at least a certain amount of money is spent.

“Dollars off” coupons: A minimum purchase amount gets the shopper a coupon that can be used against the purchase price of all items.

Free shipping: A minimum purchase amount gets the shopper free shipping.

## 3.3.2. An integer programming model

Here are the constraints and objective function developed for Amazon. Let the items in the choice set be indexed by ia $\{ 1 , \cdots , n \}$ and let $x _ { i }$ be a binary variable indicating whether or not the $i ^ { t h }$ book is purchased and paid for, and similarly f indicates whether that book is chosen to be received free. The retailer price of the ith book in the choice set is $p _ { i } ,$ while $p _ { 0 }$ is the price of the base item.

The following constraint holds if the shopper speci<sup>fi</sup>es that no more than u books should be purchased, including the base book;

$$
\sum_ {i = 1} ^ {n} x _ {i} \leq u - 1\tag{1}
$$

The following deal with three types of promotions.

Free items:

A book cannot be both paid for and free;

$$
x _ {i} + f _ {i} \leq 1, i = 1, \dots , n\tag{2}
$$

No more than one free book can be received per order;

$$
\sum_ {i = 1} ^ {n} f _ {i} \leq 1\tag{3}
$$

At least A books must be purchased in order to qualify for a free book;

$$
1 + \sum_ {i = 1} ^ {n} x _ {i} \geq A \sum_ {i = 1} ^ {n} f _ {i}\tag{4}
$$

The total amount spent must be at least as great as the price of the free book;

$$
p _ {0} + \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \geq \sum_ {i = 1} ^ {n} p _ {i} f _ {i}\tag{5}
$$

Dollars off coupons: There is a set of “dollar-off” coupons, indexed by $k { = } 1 , { \ldots } , { \ell } ,$ where an order of total expenditure no less than $t _ { k }$ dollars yields a cost reduction of $d _ { k }$ dollars off the total price. Let $y _ { k }$ be a binary variable indicating whether or not the kth coupon is used.

No more than one coupon can be received per order;

$$
\sum_ {k = 1} ^ {\ell} y _ {k} \leq 1\tag{6}
$$

There is a minimum purchase amount to qualify for each coupon;

$$
p _ {0} + \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \geq \sum_ {k = 1} ^ {\ell} t _ {k} y _ {k}\tag{7}
$$

Free shipping: Let z be a binary variable indicating whether or not the shipping is free. If the total value of the order exceeds F dollars then shipping is free, otherwise the shipping cost is <sup>fi</sup>xed at s dollars.

$$
\sum_ {i = 1} ^ {n} p _ {i} x _ {i} - \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} \geq F z - p _ {0}\tag{8}
$$

Overall budget: The maximum amount that the shopper is willing to pay is b dollars;

$$
p _ {0} + \sum_ {i = 1} ^ {n} p _ {i} x _ {i} - \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} + s z \leq b\tag{9}
$$

Objective: Let $L _ { i }$ denote the list price of the ith book. The objective for the shopper's economic gain maximization is to maximize the total savings from the list price plus any savings from applicable promotions;

$$
\max \sum_ {i = 1} ^ {n} (L _ {i} - p _ {i}) x _ {i} + \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} + s z + \sum_ {i = 1} ^ {n} L _ {i} f _ {i}\tag{10}
$$

The overall integer programming problem for Amazon is given below.

$$
\max \sum_ {i = 1} ^ {n} (L _ {i} - p _ {i}) x _ {i} + \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} + s z + \sum_ {i = 1} ^ {n} L _ {i} f _ {i}\tag{11}
$$

s.t.

$$
\sum_ {i = 1} ^ {n} x _ {i} \leq u - 1\tag{12}
$$

$$
\sum_ {i = 1} ^ {n} p _ {i} x _ {i} - \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} + s z \leq b - p _ {0}\tag{13}
$$

$$
\sum_ {k = 1} ^ {\ell} t _ {k} y _ {k} - \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \leq p _ {0}\tag{14}
$$

$$
\sum_ {k = 1} ^ {\ell} y _ {k} \leq 1\tag{15}
$$

$$
F z + \sum_ {k = 1} ^ {\ell} d _ {k} y _ {k} - \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \leq p _ {0}\tag{16}
$$

$$
x _ {i} + f _ {i} \leq 1, i = 1, \dots , n\tag{17}
$$

$$
\sum_ {i = 1} ^ {n} f _ {i} \leq 1\tag{18}
$$

$$
A \sum_ {i = 1} ^ {n} f _ {i} - \sum_ {i = 1} ^ {n} x _ {i} \leq 1\tag{19}
$$

$$
\sum_ {i = 1} ^ {n} p _ {i} f _ {i} - \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \leq p _ {0}\tag{20}
$$

$$
z, x _ {i}, f _ {i}, y _ {k} \text { binary }, i = 1, \dots , n, k = 1, \dots , \ell\tag{21}
$$

Here n is the size of the choice set and is typically a small number. The additional $n { + } \ell { + } 1$ variables are speci<sup>fi</sup>c to the Amazon model. The same distinction can be made for the constraints. There are a total of n + 8 constraints, but any of these could be <sup>fl</sup>exible based on the desires of the shopper. The most robust, that do not deal with any particular kind of promotion, are the constraints (12) that limit the number of items purchased and some variation of the budget constraint (13).

Some retailers also offer percent-off coupons. Usually, dollars off coupons are not stackable with any other coupons, including percent-off coupons. Therefore, we can replace dollar-off coupon constraints with percent-off coupon constraints and get a new formulation, which is provided in Eqs. (22)–(26) in Appendix A.

In the formulation (11)–(21) we assume <sup>fi</sup>xed shipping costs per order. The shipping cost structure of many retailers includes both <sup>fi</sup>xed and variable charges. For example, Amazon.com charges \$3.99 for the <sup>fi</sup>rst item and \$0.99 for each additional item as long as the total order value is less than \$25. In the presence of both <sup>fi</sup>xed and variable shipping charges, our objective function and some of the constraints become nonlinear. A formulation for <sup>fi</sup>xed and variable shipping cost is provided in Appendix B.

## 3.4. Computational results from Amazon and Buy.com

It would be interesting to see how much savings can result from the model (11)–(21) and whether the savings are signi<sup>fi</sup>cant. We tested the previous model using data collected from both Amazon.com and another online retailer Buy.com. We chose Buy.com as another data source because it offered various dollar-off coupons (\$5 off \$25, \$7.50 off \$50, and \$10 off \$70) as well as free shipping during the data collection period, which allows us to test our model with more forms of promotions. Amazon.com only offered free shipping promotion during the data collection period. Neither offered any free item promotion so constraints (17)–(20) did not apply.

We <sup>fi</sup>rst collected data of the top 100 ranking books from Amazon in June, 2005. These data include the title, list price, and actual price of the base item, and the price of recommended item and choice set items. Data were also collected from Buy.com for the same books. However, Buy.com did not provide a choice set for 13 books so the actual sample size is 87.

For each book we determine the benchmark savings of the current best bet as the difference between the sum of the list prices of the two books (base item and best bet) and the total order cost (including shipping if the purchase does not qualify for free shipping). We then solve the integer programming model using all the choice set items and restricting the budget to be no more than the total order cost under the current best bet. We also limit the maximum number of items to be 5 although only in two cases is more than one item recommended by the integer programming solution. The resulting savings are compared to the benchmarks and are summarized in Table 2.

Table 2 Savings of our best bets

<table><tr><td rowspan="2"></td><td colspan="2">Amazon.com</td><td colspan="2">Buy.com</td></tr><tr><td>Benchmark</td><td>Our RS</td><td>Benchmark</td><td>Our RS</td></tr><tr><td>Sample size</td><td>87</td><td></td><td>46</td><td></td></tr><tr><td>Number of books recommended</td><td>1</td><td>1</td><td>1</td><td>1 (43), 2 (3)</td></tr><tr><td>Average order value</td><td>30.91</td><td>30.04</td><td>28.73</td><td>24.49</td></tr><tr><td>Max order value</td><td>87.29</td><td>87.29</td><td>61.59</td><td>53.97</td></tr><tr><td>Min order value</td><td>20.96</td><td>11.98</td><td>16.53</td><td>16.40</td></tr><tr><td>Average savings</td><td>12.19</td><td>16.23</td><td>15.67</td><td>21.45</td></tr><tr><td>Max savings</td><td>58.49</td><td>58.49</td><td>28.40</td><td>35.46</td></tr><tr><td>Min savings</td><td>-4.98</td><td>-3.99</td><td>4.41</td><td>4.54</td></tr></table>

The average savings from our best bets for Amazon.com (\$16.23) are 33% higher than the benchmark (\$12.19) with a slightly lower average actual cost. The savings for Buy.com are 37% higher with actual cost 15% lower than the benchmark. Both differences are statistically signi<sup>fi</sup>cant at p b .001 level. Note that negative savings can occur if the retailer price is higher than the list price.

In our method, best bets in a recommendation bundle need not to be the most related item, hence there is a tradeoff between savings and relatedness. However, these recommendations are for price sensitive shopbot consumers. These shoppers will be more responsive to the recommendations that offer more savings than those that are more related as long as the recommendations are not completely unrelated to their interests. As such, these recommendations are selected from the top n related items so as long as this n remains within some threshold value. Thus the recommendations generated from our model will not be completely unrelated to the shopper's interests.

## 4. Conclusions

In this research we study how to enhance the business value of recommendations by incorporating various sales promotion mechanisms into recommendations so that a synergy can be formed among the two. We explore the potential misalignment between sales promotions and recommendations in the online book industry by showing that recommendations could have been modi<sup>fi</sup>ed to be more appealing to certain shoppers while preserving the relatedness of the recommendations.

We point out the potential con<sup>fl</sup>ict between retailers' incentives to provide recommendations and shoppers' desire to <sup>fi</sup>nd related items. On the one hand, retailers want to enhance shopping experience and increase customer loyalty by providing accurate recommendations. On the other hand, as pro<sup>fi</sup>t maximizers, retailers do have the incentive to modify recommendations to either convey quality related information to shoppers or serve their own operational purposes such as inventory clearance through cross-selling. Using the limited data, we show that the action of modifying recommendations is correlated with the ranking of base items, therefore suggesting that retailers are taking advantage of the popularity of base items for their own economic goal. In a separate research on the impact of recommendations on sales, it is found that demand elasticity of recommendations does not change when the best bet recommended items are not from the choice set vs. when they are from the choice set. This provides feasibility to retailers if they do wish to utilize recommendations for their operational purposes without negatively affecting the perceived trustworthiness of the outcome of recommender systems.

In contrast, shopbots are in a better position to serve the interests of shoppers due to their role of infomediary. Shopbots do not own and sell items but only provide information that facilitates transactions. Therefore, shopbots recommender systems are impartial in the sense that they would not bene<sup>fi</sup>t from recommending items that are not based on the relatedness of items. Furthermore, shopbots have access to data from multiple retailers and therefore they can provide more accurate recommendations. We propose that shopbots could become the integrator of recommendations and sales promotions even though none of these are part of the services they currently provide. An integer programming model is developed that can be implemented by a shopbot to solve for the optimal recommendations. Using data from two major online retailers, this model is shown to generate signi<sup>fi</sup>cant savings for shoppers.

Coming back to what retailers can do to align the recommendations with their own economic goals, one implication of the current research is that retailers could bene<sup>fi</sup>t from customized recommendations for different customer segments or preferences. For price sensitive shoppers, retailers could implement the same model we propose for shopbots to generate recommendations that would more likely lead to actual sales. For shoppers who are willing to pay more to get a real <sup>fi</sup>t for their taste, it could be bene<sup>fi</sup>cial to recommend the items based purely on relatedness. When the need of moving slow inventory items becomes paramount, retailers could use recommendations as a mechanism to be combined with existing price discounts. In this case, the shopbot model can be used as a base for retailers to design their discount strategy so that the effect of promotions are not negated but strengthened by recommendations.

Note that our integer programming model is based on maximization of potential savings to cater to the need of dealhunting shoppers. Therefore, it might not be in the best interest of those shoppers who are willing to pay more for a better-matched recommendation. This is a limitation of our research. However, we believe it would not be too dif<sup>fi</sup>cult to modify the objective function and constraints so that it satis<sup>fi</sup>es other needs of shoppers as well, which could result in multiple con<sup>fi</sup>gurations of the same recommender systems.

One possible extension to the current study is to introduce measures of business values of recommendations from the retailer's perspective, such as pro<sup>fi</sup>t of the recommended bundle, or reduction in inventory cost. This will enable retailers to better align the recommendations with their own economic goals. Another interesting direction for future research is to study the reaction of shoppers to those modi<sup>fi</sup>ed recommendations. Speci<sup>fi</sup>cally, if the modi<sup>fi</sup>ed recommendations do increase the demand for the recommended items, retailers should consider using recommendations for their own bene<sup>fi</sup>t. Also do different types of shoppers react differently to modi<sup>fi</sup>ed recommendations? The <sup>fi</sup>ndings could help any recommender systems customize their recommendations.

## Appendix A. Constraints for percent-off coupon

In the case of a percent-off coupon with α off the total value over $G ,$ our formulation will be changed as follows.

$$
\max \sum_ {i = 1} ^ {n} (L _ {i} - p _ {i}) x _ {i} + \alpha \sum_ {i = 1} ^ {n} p _ {i} x _ {i} + \sum_ {i = 1} ^ {n} L _ {i} f _ {i} + s z\tag{22}
$$

will be the new objective function. The following will replace Eqs. (12), (13), (14), and (16) respectively.

Maximum items in a recommendation bundle:

$$
\sum_ {i = 1} ^ {n} x _ {i} \leq u - 1\tag{23}
$$

Budget constraint:

$$
\sum_ {i = 1} ^ {n} p _ {i} (1 - \alpha) x _ {i} + s z \leq b - p _ {0}\tag{24}
$$

Percent-off eligibility constraint:

$$
\sum_ {i = 1} ^ {n} p _ {i} x _ {i} \geq G - p _ {0}\tag{25}
$$

Free shipping eligibility constraint:

$$
\sum_ {i = 1} ^ {n} p _ {i} (1 - \alpha) x _ {i} \geq F (1 - z) - p _ {0}\tag{26}
$$

We can determine the optimal solution for Eq. (11) and then solve Eq. (22). If we <sup>fi</sup>nd a feasible solution for Eq. (22), then we will further compare the solutions from Eq. (22) and select the one that provides greater savings.

Appendix B. Non-linear shipping promotions

$$
\text { Max } \sum_ {i = 1} ^ {n} (L _ {i} - p _ {i}) x _ {i} + \sum_ {k = 1} ^ {l} d _ {k} y _ {k} - \left(s + v \sum_ {i = 1} ^ {n} x _ {i}\right) z + \sum_ {i = 1} ^ {n} L _ {i} f _ {i}\tag{27}
$$

s.t.

Maximum items in a recommendation bundle:

$$
\sum_ {i = 1} ^ {n} x _ {i} \leq u - 1\tag{28}
$$

Consumer's budgetary constraint:

$$
\sum_ {i = 1} ^ {n} p _ {i} x _ {i} - \sum_ {k = 1} ^ {l} d _ {k} y _ {k} + \left(s + v \sum_ {i = 1} ^ {n} x _ {i}\right) z \leq b - p _ {0}\tag{29}
$$

Discount eligibility constraint:

$$
p _ {0} + \sum_ {i = 1} ^ {n} p _ {i} x _ {i} \geq \sum_ {k = 1} ^ {l} t _ {k} y _ {k}\tag{30}
$$

Coupon stackability constraint:

$$
\sum_ {k = 1} ^ {l} y _ {k} \leq 1\tag{31}
$$

Free shipping eligibility constraint:

$$
\sum_ {i = 1} ^ {n} p _ {i} x _ {i} - \sum_ {k = 1} ^ {l} d _ {k} y _ {k} \geq F (1 - z) - p _ {0}\tag{32}
$$

Buy-A-get-one-free constraints remain the same as Eqs. (17)– (20).

When a retailer offers both types of coupons, we need to solve the variable shipping costs case in two stages and for the second stage, a model similar to Eqs. (22)–(26) can be formulated. As can be seen from the formulation our objective function (27) as well as consumer budget constraint (29) has become nonlinear in the presence of variable shipping costs.

## References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender systems: a survey of the state-of-the-art and possible extensions IEEE Transactions on Knowledge and Data Engineering 17 (6) (2005) 734–749.

[2] R.E. Caves, D.P. Greene, Brands' quality levels, prices, and advertising outlays: empirical evidence on signals and information costs, International Journal of Industrial Organization 14 (1) (1996) 29–52.

[3] J.A. Chevalier, D. Mayzlin, The Effect of Word of Mouth on Sales: Online Book Reviews, 2004.

[4] J. Eliashberg, S.M. Shugan, Film critics: in<sup>fl</sup>uencers or predictors? Journal of Marketing 61 (2) (1997) 68–78.

[5] G. Ellison, S.F. Ellison, Search, Obfuscation, and Price Elasticities on the Internet, 2004.

[6] J.M. de Figueiredo, Finding sustainable pro<sup>fi</sup>tability in electronic commerce, Sloan Management Review 41 (4) (2000) 41–52.

[7] L.J. Flynn, Like This? You'll Hate That. (Not All Web Recommendations Are Welcome.), New York Times, 2006 pp. 1; Section C; Column 2; Business/Financial Desk.

[8] R. Gar<sup>fi</sup>nkel, R.D. Gopal, A.K. Tripathi, F. Yin, Design of a bundle shopbot, Decision Support Systems 42 (3) (2006) 1974–1986.

[9] R.D. Gopal, S. Bhattacharjee, G.L. Sanders, Do artists bene<sup>fi</sup>t from online music sharing? Journal of Business 79 (3) (2006) 1503–1533.

[10] G. Iyer, A. Pazgal, Internet shopping agents: virtual co-location and competition, Marketing Science 22 (1) (2003) 85–106.

[11] S. Latcovich, H. Smith, Pricing, sunk costs, and market structure online: evidence from book retailing, Oxford Review of Economic Policy 17 (2) (2001) 217–234.

[12] A.L. Montgomery, K. Hosanagar, R. Krishnan, K.B. Clay, Designing a better shopbot, Management Science 50 (2) (2004) 189–206.

[13] Y.Q. Mui, Wal-Mart blames web site incident on employee's error, Washington Post, 2006 pp. Financial D01.

[14] P. Nelson, Information and consumer behavior, The Journal of Political Economy 78 (2) (1970) 311–329

[15] P. Nelson, Advertising as Information, The Journal of Political Economy 82 (4) (1974) 729–754.

[16] D.A. Reinstein, C.M. Snyder, The in<sup>fl</sup>uence of expert reviews on consumer demand for experience goods: a case study of movie critics, Journal of Industrial Economics 53 (1) (2005) 27–51.

[17] M.D. Smith, The impact of shopbots on electronic markets, Journal of the Academy of Marketing Science 30 (4) (2002) 442–450.

[18] M.D. Smith, E. Brynjolfsson, Consumer decision making at an internet shopbot: brand still matters, The Journal of Industrial Economics 49 (4) (2001) 541–558.

![](/api/attachments/PMXHQHVK/fulltext/images/e75c0b3051a09644db7c5f2e8982e0efc9ef5185859188c95f39619796fe2ce4.jpg)

Dr. Robert Gar<sup>fi</sup>nkel is a professor in the Operations and Information Management Department of the School of Business at the University of Connecticut. His work on a variety of problems in operations research, mainly involving combinatorial optimization, has appeared in such journals as: Operations Research; Management Science; Informs Journal on Computing; Decision Support Systems,

and Mathematical Programming. His current research has focused heavily on the problem of optimally balancing valid security concerns against the desire to provide users of a database with valuable information. Other ongoing research streams include: improving ef<sup>fi</sup>ciency in hospital settings; design of markets for grid computing; construction of recommender systems for shopbots; optimization problems in micro<sup>fl</sup>uidic systems; and optimization in vehicle routing. He is also coauthor of the book Integer Programming with George Nemhauser.

![](/api/attachments/PMXHQHVK/fulltext/images/3006852238c9cb81ac0d7541663186539c57a566cdc19c90d11a78078ab2cdb3.jpg)

Dr. Ram D. Gopal is currently the GE Endowed Professor of Business and an Ackerman Research Scholar. His current research interests are in the areas of data security, privacy and valuation, database management, intellectual property rights and economics of software and music piracy, online market design and performance evaluation, economics of online advertising, technology integration, and

business impacts of technology. His research has appeared in Management Science, Operations Research, INFORMS Journal on Computing, Information Systems Research, Journal of Business, Journal of Law and Economics, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings. He currently serves as the Ph.D. director for the department and is on the editorial board of Information Systems Research, Journal of Database Management, Information Systems Frontiers, and Journal of Management Sciences.

![](/api/attachments/PMXHQHVK/fulltext/images/07f277d47cdc6d4796768fd0287be715d4c6a286199bae61f5bbd23e60407ce4.jpg)

Dr. Bhavik Pathak is an assistant professor of Decision Sciences at the School of Business and Economics at Indiana University South Bend. Dr. Pathak received his Ph.D. in Operations and Information Management from the University of Connecticut in 2006. Dr. Pathak's teaching interests are in the areas of electronic commerce, decision support systems, management information systems, and data mining. Dr.

Pathak's research interests are in the areas of electronic commerce, online recommender systems, social networking, shopbots, and online promotions. His research has been published in the Journal of Retailing, Communications of the AIS, and Industrial Management and Data Systems.

![](/api/attachments/PMXHQHVK/fulltext/images/e0b7c0d08d14def7473446177d3fdabfc7528b36fe0a5fbf1eb557fd529e6db3.jpg)

Dr. Fang Yin is an Assistant Professor in the Operations and Information Management Department of the School of Business at the University of Connecticut. His research interests are in the business value of IT investment, online sales promotion, shopbots design, and online recommender systems. He has published in MIS Quarterly, Decision Support Systems, Journal of Retailing, Sloan Management

Review, and several other journals. He holds a Ph.D. from the University of Texas at Austin.
