---
otero_id: 8620
otero_key: "H8M2M9C9"
title: "A system for pricing the sales distribution from blockbusters to the long tail"
authors: "Cenk Koçaş; Can Akkan"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.06.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A system for pricing the sales distribution from blockbusters to the long tail

Cenk Koçaş ⁎<sup>,1</sup>, Can Akkan <sup>2</sup>

Sabancı University, Faculty of Management, YBF 1076 Orhanlı, 34956 Tuzla, İstanbul, Turkey

## a r t i c l e i n f o

Article history: Received 11 September 2015 Received in revised form 6 June 2016 Accepted 6 June 2016 Available online xxxx

Keywords: The long tail Sales rank distribution Popularity Pricing Competitive price promotions Pricing decision support systems

## a b s t r a c t

The long tail of retailing has been both a challenge and an opportunity for online retailers. This article provides guidelines for enhanced decision making strategies in pricing dependent on popularity, cross-sales quantity and reservation prices. Our model shows that if customer willingness to pay, or reservation price, is higher for less popular items in a category, a unique optimal price path exists which requires deep discounts on popular items. However, if the reservation price is lower for less popular items, the optimal price path is conditional on the profitability of cross-selling and the potential loss from the business of loyal customers. Analyzing data on books, songs and movies from Amazon.com, we provide empirical support for our model findings. An analysis of the same set of movies available both as instant videos and DVDs allow us control for unobserved product characteristics and yields contradictory price paths along the sales rank distribution with increasing prices for DVDs and decreasing prices for streaming movies, as predicted by our model.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

A peculiarity in pricing strategies of Apple and Amazon.com marks apparent divergent strategies. Apple prices its songs sold at iTunes store at three fixed prices, such that the more popular songs are the most expensive (\$1.29), the majority moderately expensive (\$0.99) and obscure songs least expensive (\$0.69), whereas Amazon.com offers its best seller books at considerable discounts and niche books at no discount. A survey of Amazon.com's top 100 best-selling books on October 18, 2011, reveals an average discount of 47.8% off the list price.

Should any online retailer price its more popular items, that is, its superstars, at a discount or at a premium in a given category? How should an online retailer price its niche products, which make up the long tail of sales distribution? Should the retailer follow Apple's song pricing strategy and sell its superstar products at 46% premium over its cheapest offerings, or should it follow Amazon.com's book pricing strategy and offer a 50% discount off regular price on its superstar products in any given product category (e.g., movies, games, applications)? Is the pricing strategy dependent on certain category characteristics, such that both Apple's and Amazon.com's strategies are relevant given category characteristics? In this research, we provide a competitive model of pricing for multi-product retailers that accounts for sales rank-dependent reservation prices for products and sales rank-dependent sales and cross-sales of products to answer these questions.

Every retailer manages a sales distribution that contains a few hit (superstar, blockbuster, or best seller) products that make up the majority of sales and many niche or long tail products that can also have substantial effects on sales [1,7,9]. In the cardinal sales to ordinal sales rank distribution, which takes the form of a power law distribution, the fat head consists of the superstar products; the blockbusters. The niche products make up the long tail of the sales distribution. In between the fat head and the long tail is a chunky middle, with characteristics of both ends but extremities of neither. In today's online markets, customers empowered by search capabilities and guided by recommender systems can easily navigate to all product pages [6,19,34,38]. How can retailers enhance their DSS and maximize their profits by determining the relative prices of the fat head, chunky middle and long tail products?

We consider an oligopolistic market of complete information in which multi-product retailers compete in the sales of homogeneous goods of varying popularity. We use the term “popularity” to capture the sales rank of a product. A product's popularity has three potential influences in our model. First, the perceived value, or the customer valuation of an item may be a function of the item's popularity, i.e., its sales rank. For example, popularity can have a positive effect on the perceived value of the product and can increase the reservation price an average customer would be willing to pay for the product [18]. Second, the position of the product on the best seller list directly influences the sales quantity [7,9]. According to the power law shape, popular items sell disproportionately more and long tail items sell disproportionately less. Third, popular items not only sell more copies but also help sell other items because of their traffic-generating capabilities [13,25]. Therefore, popularity pays in both sales and cross-sales.

Following Varian [42], we model these three influences and their interactions in a competitive price promotions setting and describe the conditions that a DSS should account for. Our model findings reveal that the optimal prices of popular versus niche products depend on both the sales potential and the perceived value of products, both of which depend on the sales rank. The sales potential determines not only the profit potential from a product but also the profit potential from the cross-sales of other merchandise. Therefore, a superstar with a high perceived value and corresponding reservation price should be sold at a higher price than an average product, but it should be sold at a lower price than an average product in a competitive environment if the high price risks its own and cross-sales profit potential. Thus, different categories can require different pricing strategies along the sales distribution. For example, books, as a category, may call for discounted bestsellers, while music, as a category, may benefit from discounting the long tail, as our model and empirical analysis demonstrate. Note that a decision support system for relative prices generates suggestions on percentage discounts across the sales distribution where premium prices correspond to no discounts and the lowest prices correspond to deepest discounts.

## 2. Literature review

The Internet has created a landslide in terms of products available to consumers [1,8,12], and recommendation engines and search tools can be fine-tuned to direct customers' attention to any product [6,19,38,39]. What remains unanswered is how decision making can be improved to manage the products in the fat head, the chunky middle or the long tail of the sales distribution [26,28]. Although pricing online, in which DSS plays an influential role, remains an important topic [32,33,43], pricing online as it applies to this sales distribution has received scant attention (see [39] for an exception). Brynjolfsson [5] calls for research that would examine how retailers should price niche products versus superstars.

The economics of superstars and the potential of the long tail have been two widely discussed and contrasted theories. Research on the economics of superstars and the long tail has treated them as contrasting theories rather than as complementary. Rather than seeing them as two competing theories, we join Brynjolfsson [5] and contend that the economics of superstars and the potential of the long tail should be analyzed as part of an integrated research agenda.

The superstar phenomenon was first introduced to describe the few top performers that reach a majority of the audience and achieve the most profits [40]. Superstars are the few products that emerge mainly from blockbuster strategies of suppliers [18] and create the so-called winner-take-all markets [21] in which blockbuster products dominate sales. On the other side of sales rankings are niche products. Anderson [1] was the first to introduce the notion of the long tail, in which niche products are found more easily with the help of recommendation engines and search capabilities and thus selling less of more niches may be as viable as selling more of a few superstars. All other products reside in-between the superstars and the niche products; these products are modestly popular and modestly obscure at the same time and make up a significant proportion of sales.

Significant evidence indicates that the relationship between a product's sales rank and sales quantity can be represented by a power law (i.e., Pareto law) [7,9]. The sales of both superstars and niche products may also influence the sales of one another. The purchase of a single product can lead to additional purchases as a result of economies of scale, such as traveling, shipping or handling costs [31, 38], or psychological factors, such as the shopping momentum effect [16] or a windfall effect [24]. This cross-selling potential leads to lossleader pricing [31]. Thus, if customers buy superstars and long tail products in the same transaction, their prices should be linked [5]. In the context of the sales distribution, it is also suggested that long tail products may offer higher profit margins than superstars, which are often used as loss leaders [18].

Online sales are also greatly shaped by the customer reviews on products. It is widely accepted that online customer reviews are a good overall proxy of word-of-mouth communication [45]. Prevalent research in marketing, economics and information systems has assessed the correlation between consumer reviews and sales [2,10,11,14,17,22, 23,36]. We assume that customers use review and rating information on products to reach a customer valuation of the item considered. In our model and empirical analysis, we link the average customer rating and reservation price (customer valuation), where a customer can infer the product's relative value on viewing consumer reviews and average customer ratings which in turn may influence his or her reservation price [30,35,44]. We consequently refer to a customer's valuation for a product as the reservation price he or she is willing to pay for the product. Hence, we assume that the customer valuation and reservation price for a product with high rating is higher compared to a product with lower rating. In this article, we examine how decision support systems could improve pricing for products of various sales ranks as the shape of the reservation price curve (as a function of the sales rank R) changes.

In the next section, we develop a model with the aim to answer the following research questions: (i) Should a retailer charge a premium for, or offer a discount on the niche products in the long tail? (ii) How should the blockbusters be priced? (iii) How does customer valuation of products combined with sales as well as cross-sales of products affect prices? (iv) How does this influence evolve along the sales distribution?

## 3. Model

The model we use is an extension of Varian's model [42], and we consider an oligopoly with three retailers. An oligopolistic model captures the severity of competition more robustly than a duopolistic model and is therefore preferred. Table 1 provides a list of variables. Each retailer sells a focal product P to two segments of customers, one that price compares and the other that is loyal to the retailer. Pricecomparing customers buy product P from the retailer that lists it for less as long as the price is below their reservation price r. Loyal customers buy the focal product P from the retailer to which they are loyal. Following Varian, we assume a one-shot game of complete information where retailers choose prices of product P to maximize profits.

We introduce three extensions to Varian's [45] market structure. First, we assume that an α proportion of price-comparing buyers of product P also immediately buy the common outside product O from the same retailer. Note that the results of the model hold for all αϵ(0,1] and we set α=1 for brevity. We introduce this extension to capture the cross-selling effect of popularity, in which traffic generation is the key factor. The price of product O is exogenous to the model and the same across retailers. We assume no fixed costs and zero marginal cost, so that both p, the price of focal product P, and o, the price of outside product O, also represent profit margins for the respective products.

Second, we allow the sales quantity to be a function of sales rank. This extension is a result of popularity and the resulting traffic, reasons which are external to the model. We use a simplified version of Brynjolfsson, Hu and Smith [7] and Chevalier and Goolsbee [9] models and assume that sales rank R is linked to sales quantity due to customers who price compare for the focal product P as $\begin{array} { r } { \mathrm { Q } = \frac { 1 } { \mathrm { R } } . ^ { 3 } } \end{array}$

In the third extension, we allow the reservation price r for product P to vary with the sales rank R (i.e., we treat the reservation price as r[R]). By making no a priori assumptions but allowing for a decreasing, constant and increasing reservation price r[R], we can capture the

C. Koçaş, C. Akkan / Decision Support Systems xxx (2016) xxx–xxx

Table 1  
Variables and definitions used in the model.

<table><tr><td>R</td><td>Sales rank (i.e., 1, 2, 3, ... 1000... 1,000,000... M)</td></tr><tr><td>Q=1/R</td><td>Number of price comparison shoppers of a product with sales rank R</td></tr><tr><td>r</td><td>Reservation price (constant)</td></tr><tr><td>r[R]</td><td>Reservation price as a function of sales rank R</td></tr><tr><td>pi</td><td>Price of focal product P at retailer i</td></tr><tr><td>o</td><td>Price of outside good O</td></tr><tr><td>L</td><td>Retailer loyal segment size</td></tr><tr><td>F[p]</td><td>Cumulative distribution function of price p</td></tr><tr><td>pmin</td><td>Lowest possible quoted price in the mixed strategy</td></tr><tr><td>p[R]</td><td>Average price as a function of sales rank R</td></tr><tr><td>M</td><td>Total number of products in sales ranking</td></tr></table>

characteristics of many product categories. Formally, retailers in our model compete for the sale of the focal product P, which has a sales rank R, where R is determined either externally (by third-party rankings, such as Billboard Top 100 or The New York Times best seller list) or internally (by one of the retailers). Therefore, this sales rank for product P is common knowledge across both retailers and customers.

Accordingly, there are $\textstyle Q = { \frac { 1 } { R } }$ customers who shop for the focal product with sales rank R, where Q follows a power law distribution (Brynjolfsson, Hu and Smith [7]; Chevalier and Goolsbee [9]. Note that Qϵ(0,1]. These <sup>1</sup> shoppers price-compare for product P and buy it from the retailer that offers it for less. These customers are informed about the price of product P at all retailers through price comparison tools, advertisements or news [31], and choose the retailer to patronize according to this information.

Having visited the retailer to purchase product P, these $\textstyle { \frac { 1 } { \mathsf { R } } }$ customers also buy an outside product O with their purchase of product P as in [16]. These customers do not price-compare for product O but rather buy it as an impulse purchase [3] or under a shopping momentum effect of the first purchase [16]. This cross-selling creates a link between the price of the focal good and the profitability from an outside good [13].

Again, as in Varian [42] and Narasimhan [37], each retailer also sells product P to L loyal customers of its own, Lϵ(0,1]. We also assume that a βϵ[0,1] proportion of L loyal customers buy the outside good O when they buy product P from their preferred retailer. However, this β proportion does not affect the optimization process or the optimum price for product P; therefore, we set $\beta = 0$ for simplicity—again, this exclusion does not alter the model results. However, we assume that the price of O that is cross-sold to the price-comparing shoppers of P is identical across all three retailers. Furthermore, we assume that the sales to loyal customers is independent of the sales rank R relative to the sales to price-comparing shoppers. That is, if Q were $\frac { 1 } { R ^ { \mu } }$ and L were $\frac { 1 } { R ^ { \theta } } ,$ this relative independence implies that μNθ. Popular products are, by definition, traffic generators, and traffic in our paper is indicated by price-comparing customers. This relative independence assumption thus ensures that product popularity affects sales to price-comparing customers more strongly than sales to loyal customers. In our model, we assume that $\mu { = } 1$ and θ=0 for simplicity.

## 3.1. Model specification

The general profit function of Retailer i is given by

$$
E \pi_ {i} = \frac {1}{R} (p _ {i} + o) P r o b (p _ {i} <   p _ {- i}) + L p _ {i},
$$

where $P r o b ( p _ { i } < p _ { - i } )$ is the probability the price comparison shoppers will choose Retailer i. In this case, Retailer i sells both the focal good P and the outside good O to the $\textstyle { \frac { 1 } { R } }$ customers. Independent of the price of product P, Retailer i sells the focal good P to its L loyal customers, creating the profit $L { p _ { i } } .$ Denoting $F _ { j } [ p ]$ as the cumulative distribution function of Retailer j's prices for product P, which is set to be same for all retailers, we can rewrite the profit function for Retailer i as

$$
E \pi_ {i} = \frac {1}{R} (p _ {i} + o) (1 - F _ {j} [ p ]) ^ {2} + L p _ {i}.
$$

Thus, with this augmented model, we take into consideration both the additional profitability of an outside good and the sales rank of the focal product. Next, we analyze the general case of a reservation price r. Note that because r is a function of only R, we first treat the special case of constant r.

Proposition 1. When the reservation price is constant, the optimal pricing strategy for an oligopolistic retailer is to randomize prices between the reservation price r and $\begin{array} { r } { p _ { m i n } = \frac { L R r - o } { 1 + L R } . } \end{array}$ . Formally, the retailers symmetric profit-maximizing strategy is given by the mixed strategy:

$$
F [ p ] = 1 - \sqrt {\frac {L (r - p)}{(o + p)}} \quad , p \in \left[ \frac {L R r - o}{1 + L R}, r \right]
$$

The average price of the strategy is given by

$$
\begin{array}{l} \overline {{p}} [ R ] = \frac {(o + r)}{2} \left(\frac {- 2 o}{(o + r)} + \gamma \sqrt {L R}\right), \quad \text { where } \gamma \in (0, \pi) \text { equals } \frac {\pi}{2} \\ \qquad + A r c T a n \left(\frac {1 - L R}{2 \sqrt {L R}}\right). \end{array}
$$

Proof. All proofs appear in the Appendix.

Proposition 1 demonstrates how competitive prices are shaped by the key variables in our model. Although this competitive pricing game has no pure strategy equilibriums, the mixed strategy equilibrium provides a clear sketch of minimum, maximum and average prices of the product in the competitive market. Fig. 1 illustrates the minimum, maximum and average prices as a function of the sales rank R for some typical demonstration values of parameters $L = 1 , o = 5$ and $r = 1$ . The general shape of the curve is not sensitive to these values. As Fig. 1 demonstrates, both $p _ { \mathrm { m i n } }$ and average price, $\overline { { p } } [ R ]$ follow a power law pattern with respect to the sales rank of the product. Note that, even with mixed rather than pure strategy prices, we can analyze a price path along the sales distribution by observing this average value of prices ${ \overline { { p } } } [ R ]$ along the sales ranks. Fig. 1 also illustrates the pricing implications of our model for products of different sales ranks. As we present in Proposition 2 and prove subsequently, Fig. 1 shows that p R is an increasing function of the sales rank R if the perceived value of the product as embodied by the reservation price r does not vary with the sales rank.

Fig. 2 displays the cumulative distribution functions of the randomized prices for some sales ranks for the previously specified parameter

C. Koçaş, C. Akkan / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/H8M2M9C9/fulltext/images/a6f2e49055aaf56340233580e89b00a50f884335f69b60217b1e94675ee9e45e.jpg)  
Fig. 1. The upper and lower limits of the price support and the average price as a function of the sales rank.

values. Note that each graph in Fig. 2 is a distribution function representation of a vertical slice from Fig. 1 at sales rank R equaling 1, 2, 5, 10, 100 and 1000.

Also note that the lower boundary of the strategy set given by $\begin{array} { r } { p _ { m i n } = \frac { L R r - o } { 1 + L R } } \end{array}$ can be both negative and positive as Fig. 2 also demonstrates. This lower bound, $p _ { \mathrm { { m i n } } } ,$ is a loss-making price when ${ \frac { o } { r } } { > } L R ,$ where <sup>o</sup> is the relative profitability of the outside good compared with the reservation price of the focal good, and LR, is the inertia to reduce prices of the focal good. A large loyal segment or a low sales rank increases this inertia.

## 3.2. Non-decreasing reservation price

Next, we analyze the optimal pricing behavior of oligopolistic retailers along the sales distribution.

Proposition 2. p R is a strictly increasing function if the reservation price is independent of the sales rank, R.

Proposition 2 provides an initial perspective; when customer valuation of the product is independent of the sales rank, optimal prices of popular products are lower than the optimal prices of obscure products. Therefore, a retailer should sell its superstars at a discount and its long tail products at a premium, not because the long tail products are perceived as more valuable but because selling more superstars is more profitable given the cross-selling profits their sales generate. Although the perceived value of both the superstars and the long tail products are the same, the resulting prices of the long tail products are higher. This reasoning also carries to the products in the middle of the sales distribution. Consequently, we expect retailers to discount superstars, offer shallower discounts for products in the chunky middle and offer the long tail products at nominal prices.

Unsurprisingly, this result also applies to the case in which the reservation price is an increasing function of the sales rank R. Already deserving premium prices, an increase in the perceived value of the long tail products only confirms that they should be priced higher than the chunky middle products, which have higher prices than the blockbusters. We formally present this case as a corollary. We refer to

![](/api/attachments/H8M2M9C9/fulltext/images/7989d1fbf8df7a07dadafb71b8dbb80012b88462f4a236e589474d2f890f4b92.jpg)  
Fig. 2. Cumulative distribution function as popularity (sales rank) varies.

Please cite this article as: C. Koçaş, C. Akkan, A system for pricing the sales distribution from blockbusters to the long tail, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.008

the reservation price as a function of the sales rank R as r[R] in the rest of the article.

Corollary 1. p R is a strictly increasing function if r[R] is also an increasing function.

The reasoning is straightforward. Two forces act on the prices of niche products. First, a product with a higher reservation price should be priced higher. Second, because of their limited cross-selling potential, retailers have no motivation to reduce prices of niche products, whereas they do reduce the prices of superstars. Thus, niche products with no cross-selling potential should have higher prices. Because both arguments operate in the same direction, when the r[R] is an increasing function, profit-maximizing retailers price the products in the long tail at a nominal level while reducing the prices for the superstars in the fat head and keeping the prices of the products in the chunky middle in between.

We can summarize the findings so far as $\begin{array} { r } { \frac { \partial r [ R ] } { \partial R } \geq 0 \Rightarrow \frac { \partial \overline { { p } } [ R ] } { \partial R } < 0 . } \end{array}$ That is, for any non-decreasing r[R], superstars are offered at the lowest prices and products in the long tail are offered at the highest prices.

## 3.3. Decreasing reservation price

Next, we show that when r[R] is a decreasing function of popularity, there is a set of conditions related to the price of the outside good, o, and retailer loyal segment size, L, for which p R is decreasing. We show specifically that when the profitability of cross-selling is low and the potential loss from the business of loyal customers is high, a profitmaximizing retailer should price its popular products at higher prices than its long tail products.

Proposition 3. When r[R] is decreasing and $| R \frac { \partial r [ R ] } { \partial R } |$ is sufficiently large, there is a region defined by low prices for the outside good, O, and high levels of retailer loyal segment size, L, for which p R is decreasing.

With Proposition 3, we demonstrate a general set of conditions that may alter the slope of p R completely so that superstars are offered at higher average prices and the products in the long tail are offered at lower average prices. Proposition 3 shows that when customers value a product more because it is enjoyed by others, this valuation can be great enough to warrant higher prices for the more popular product. However, determining the consequent optimal average price path is not a trivial matter. Several conditions must be satisfied: a retailer should price the long tail lower than the fat head only when all the following conditions are met:

• The more popular product is perceived as more valuable.

• The rate of decline in perceived value is high down the best seller list, especially for the top few superstars.

• The potential profit to be generated from a cross-sale opportunity is low.

• The number of loyal customers is high.

Note that Apple meets all these conditions for its MP3 songs category and also follows the strategy of pricing the superstars at a premium and the niche products at a discount. Thus, Proposition 3 achieves some face validity. We provide further empirical support for Proposition 3 in the empirical section.

Corollary 2. Despite a decreasing r[R], if the retailer's loyal segment size is small enough and the price of the outside good is high enough, then p R is increasing.

As Proposition 3 and Corollary 2 demonstrate, the term $| R \frac { \partial r [ R ] } { \partial R }$ is crucial in determining the shape of p R . The interaction between the sales rank and the slope of r[R] with respect to the sales rank at any point determines the slope of the optimal average price function, p R . To analyze this interaction further and to examine the shapes of the average price functions that may emerge, we present two more propositions employing different decay rates for the reservation price functions, r[R].

![](/api/attachments/H8M2M9C9/fulltext/images/ca3ad7d6b0cecb80d73e47b57f815b671e7218e381b29e1a06c60de491923570.jpg)  
Fig. 3. The conditions for an increasing/decreasing average price function of sales rank, given r R 1 <sup>1</sup>.

Proposition 4 presents the case of a r[R] with polynomial decay and Proposition 5 examines a linear decay.<sup>4</sup>

Proposition 4. When the r[R] is a polynomially decaying function, p R is decreasing (increasing) in the region characterized by low (high) prices for the outside good, o, and high (low) levels of loyal segment size, L. For intermediate (o, L) combinations, p R is convex.

Proposition 4's prescription for a decreasing p R is similar to that of Proposition 3, and its prescription for a increasing p R is similar to that of Corollary 2. Specifying a functional form for r[R] in Proposition 4 enables us to observe the exact region in which Proposition 3 holds. We depict this region in Fig. 3.

Fig. 3 depicts the region in which even convex p R may occur for sales ranks up to 1 million. In the dark gray region, up to sales rank 1 million, p R is always a decreasing function. In the light gray region, p R is a convex function reaching a minimum at some sales rank less than 1 million. In the white region,p R is always an increasing function for ranks less than 1 million. Thus, in addition to increasing p R resulting from parameter values favoring cross-selling (high o and low L) as well as decreasing p R resulting from parameter values not favoring cross-selling (low o and high L), a polynomially decaying r[R] can also lead to an optimal pricing strategy in which p R is convex.

Proposition 5. When r[R] is a linear decaying function, p R is always concave. That is, p R is always increasing for the very top sellers. For low (high) values of the price of the outside good, o, and high (low) levels of loyal segment size, L, there are less (more) top-ranked products for which p R is increasing before it starts to decrease.

For a linear decay r[R], the optimal pricing strategy always calls for discounted top-ranked superstars, and therefore the prices of the few top-ranked items are always lower than the prices of the products in the following ranks. We summarize the findings of Propositions 2 to 5 and Corollaries 1 and 2 in Fig. 4. As the second panel of Fig. 4 depicts, for a decreasing r[R], the optimal average price path, p R can be increasing or decreasing as well as convex or concave, depending on the values of o, L and the decay rate of r[R]. Later, in the empirical section, we analyze four separate product categories to gain a better understanding of the conditions and results we present in Fig. 4.

C. Koçaş, C. Akkan / Decision Support Systems xxx (2016) xxx–xxx  
![](/api/attachments/H8M2M9C9/fulltext/images/6e1c1968956f5b8744ad36f9c29b00cd27a9131e348de7b8142ca9f46694eda0.jpg)  
Fig. 4. A summary of the model findings from Propositions 1–5 and Corollaries 1 and 2.

## 4. Empirical support

Next, we compare the model predictions with data from four different product categories of Amazon.com: MP3 songs, books, movies on DVD and online streaming movies. Our model provides the optimal price path p R for given reservation price functions r[R], and therefore we first categorize the four product categories with respect to the slopes of the average customer reviews along the sales rank, which we use as a proxy for r[R]. Our model predicts certain shapes for p R for different values of the loyal segment size, L, and price of the outside good, o. In comparing the product categories with respect to these two parameters, L and o, we present four hypotheses. Finally, we test the hypotheses using pricing data from the four categories.

## 4.1. Data

We collected the sales rank and price information of books, MP3 songs and movies of various sales ranks from Amazon.com to test our model. We adopt a data collection methodology, which resembles the browsing behavior of a typical customer. Specifically, we used a web agent to collect data on books, movies and MP3 songs that were accessible to customers for browsing, where the lists are by default ranked with respect to Amazon.com's sales popularity.

## 4.1.1. Books

A web agent collected all books made available for sale on Amazon. com during the most recent 90-day period on April 25, 2011. The total number of hardcover and paperback books in this group was approximately 9000 books. We collected data from books in 28 categories, which resulted in data on a total of 18,895 books including duplicates. The removal of duplicates and formats other than paperbacks and hardcover books yielded a sample of 6076 books.

## 4.1.2. Movies

A web agent collected data from the Amazon.com DVD store on November 17–19, 2012. Amazon had 503,152 DVD titles available for browsing in 27 genres, and we collected data from all genres with an average coverage rate of 2% for any genre resulting in a sample size of 10,453 titles. The removal of duplicates, collections, television series, titles not available from Instant Videos and titles not sold by Amazon.com resulted in a sample size of 2440 titles, each of which was available for purchase either as a DVD or through streaming from Amazon Instant Video service.

## 4.1.3. MP3 songs

A web agent collected data from Amazon.com's MP3 music store on 7147 MP3 songs on November 17, 2012. There were 21,494,274 songs available for browsing in 22 genres, so the average coverage rate was 0.03%. The removal of duplicates and free songs resulted in a sample size of 6352.

## 4.2. Selection of statistical methods

In our empirical analysis, we deal with three variables: the standardized price and the average customer review as our two dependent variables and the sales rank of a given product as the independent variable. We briefly review the characteristics of the dependent variables and the statistical methods to be used next.

To be able to make comparisons across the items in any given category, we use standardized prices. We standardize the prices of books and DVDs with respect to the list prices as stated on the product pages. To standardize the prices of Instant Video titles, we use two alternative reference prices: both the maximum price Amazon.com charges its customers for any instant movie in our sample, which is \$14.99, or the list price of the DVD. Therefore, we calculate two standardized prices for instant movies, Movie\_Instant\_1 uses \$14.99 and Movie\_Instant\_2 uses the list price of the DVD. For songs, we use a standardization method similar to Movie\_Instant\_1, because there are no list prices for songs. Songs from the MP3 store are available at price points of \$.50, \$.69, \$.79, \$.89, \$.99, \$1.09, \$1.19 and \$1.29, so we use the maximum price of \$1.29 as the reference price and standardize all prices by dividing them by \$1.29. Table 2 provides the summary statistics of this data set.

The standardized prices are ratio scaled in nature; that is, they are based on the division of a ratio-scaled list price to a ratio-scaled maximum price. As is the case with prices, however, retailers provide a limited number of quoted prices. Although there are 1430 different prices for books and 1416 different prices for movies, as mentioned previously, there are just 8 different prices for MP3s.

Researchers have long debated about how to classify measurements and whether levels of measurement can be a successful guide for choosing data analysis type [4,41]. Most researchers treat even Likert scales, which are technically ordinal scales, as continuous variables and use normal theory statistics with them, though research claims that for five or more categories, there is relatively little harm in doing this [29, 46]. Given that the dependent variable is ratio scaled and there are eight categories in our MP3 data set, a linear regression seems appropriate; however, the limited number of quoted prices could also call for an ordered logit. We check and see that our data sets all satisfy the requirements of linear regression and hence it seems appropriate for us to use linear regression in our empirical analysis. Moreover, to ensure robustness, especially in the MP3 category, we also analyze our data using ordered logit for all categories and report the results. The results of the binomial theory approach and normal theory approach are consistent and therefore provide validity to the results of all categories.

Our dependent variable average customer review is ordinal scaled in nature. Therefore, the appropriate statistical method to use would be ordered logit, the results for which we report subsequently. However, given how Amazon collects and customers use average customer reviews, the variable can also be considered continuous. Average customer reviews are typically reported in decimal points (e.g., 3.8 stars), so the common treatment of average customer reviews is almost interval scaled. For robustness, we therefore report the results for both linear regression and ordered logit in the analysis of average customer reviews. We see that the results are consistent across methodologies.

## 4.3. Reservation prices across the sales rank distribution

Amazon.com uses a five-point system to collect the customer reviews of its products. The average customer review is the mean rating across customers who have reviewed the product. We use the average customer review as a proxy for reservation prices to observe how customer valuation of products—that is, the reservation price, r[R]—varies across the sales rank distribution. We estimate the equation

$$
\text { Average   customer   review } = \alpha + \beta_ {1} \text { sales   rank } + \varepsilon
$$

using both a simple regression and an ordered logit for each of the four product categories. The standardized slope coefficient of the simple regression and its significance are, by definition, identical to the Pearson correlation coefficient and its significance, and therefore we present this coefficient as the correlation coefficient in Table 3. The table also reports the unstandardized slope coefficient of the ordered logit and its significance. Note that because our data have identical sets of movies on DVD and Instant Video, movies in both formats share the same coefficients.

The slope coefficient of the books category is positive and significant at the 0.05 level for both linear and logistic regressions, which suggests that for our sample, the r[R] of books is increasing. This finding is in line with Forman, Ghose and Wiesenfeld's [20] finding of a significant correlation between sales rank and average customer review. Customers value popular books less than they value less popular books. The slope coefficients of the movie and MP3 song categories are negative and significant at the 0.01 level. The finding for MP3 songs is similar to that in Dewan and Ramaprasad's [15] study, which shows a negative relationship between sales rank and average customer review. In our sample, the r[R] of movies in both DVD and streaming video formats is decreasing. Customers value popular movies more than less popular movies. Last, the r[R] of MP3 songs is also a decreasing function of sales rank. Thus, customers value popular songs more than less popular songs.

## 4.4. Model predictions

Our model results prescribe pricing strategies along the sales rank distribution for different input parameter sets. Proposition 2 and Corollary 1 predict an increasing p R for an increasing r[R]. Among the product categories we examine, books are the only category with an increasing r[R]; thus, our model predicts an increasing p R . Therefore, in the regression

Std:price $\mathbf { \beta } = \alpha + \beta _ { 1 }$ sales rank ε

Summary statistics for the data set from Amazon.com

<table><tr><td rowspan="2"></td><td colspan="3">Avg. customer review</td><td colspan="3">Sales rank</td><td colspan="5">Standardized prices</td></tr><tr><td>Book</td><td>Movie</td><td>Song</td><td>Book</td><td>Movie</td><td>Song</td><td>Book</td><td>Movie-DVD</td><td>Movie Instant 1</td><td>Movie Instant 2</td><td>Song</td></tr><tr><td>Valid</td><td>2742</td><td>2436</td><td>4871</td><td>4531</td><td>2435</td><td>6341</td><td>6076</td><td>2440</td><td>2440</td><td>2440</td><td>6352</td></tr><tr><td>Missing</td><td>3334</td><td>4</td><td>1481</td><td>1545</td><td>5</td><td>11</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Mean</td><td>4.461</td><td>4.056</td><td>4.621</td><td>1,037,063</td><td>19,200</td><td>5184</td><td>0.846</td><td>0.626</td><td>0.578</td><td>0.719</td><td>0.804</td></tr><tr><td>Median</td><td>4.556</td><td>4.200</td><td>5.000</td><td>380,495</td><td>11,469</td><td>3479</td><td>0.860</td><td>0.646</td><td>0.555</td><td>0.667</td><td>0.767</td></tr><tr><td>Std. Dev.</td><td>0.557</td><td>0.520</td><td>0.669</td><td>1,639,411</td><td>22,804</td><td>15,620</td><td>0.159</td><td>0.176</td><td>0.125</td><td>0.284</td><td>0.103</td></tr><tr><td>Min</td><td>1.792</td><td>1.800</td><td>1.000</td><td>1</td><td>4</td><td>1</td><td>0.168</td><td>0.143</td><td>0.111</td><td>0.100</td><td>0.388</td></tr><tr><td>Max</td><td>5.000</td><td>5.000</td><td>5.000</td><td>1,014,3554</td><td>15,9545</td><td>687324</td><td>1.000</td><td>0.999</td><td>1.000</td><td>2.511</td><td>1.000</td></tr></table>

Please cite this article as: C. Koçaş, C. Akkan, A system for pricing the sales distribution from blockbusters to the long tail, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.008

Table 3  
OLS and ordered logit coefficients, model predictions and hypotheses.

<table><tr><td rowspan="2"></td><td colspan="2">Ordinary least squares</td><td colspan="2">Ordered logit</td><td colspan="4">Hypothesis</td></tr><tr><td>ACR-rank correlation ( $\beta_1$ )</td><td>F value</td><td> $\beta_1$ </td><td>Chi-square</td><td>Reservation price function r[R] is...</td><td>Cross-sales potential</td><td>Predicted relationship</td><td>H:</td></tr><tr><td>Books</td><td>0.04**</td><td>3.97**</td><td>8.87 E-8***</td><td>8.10***</td><td>Increasing</td><td>High</td><td>+</td><td>H1</td></tr><tr><td>MP3 Songs</td><td>-0.046***</td><td>10.18***</td><td>-3.45 E-6***</td><td>5.95***</td><td>Decreasing</td><td>Low</td><td>-</td><td>H2</td></tr><tr><td>Instant Movies</td><td>-0.117***</td><td>33.75***</td><td>-7.06 E-6***</td><td>17.46***</td><td>Decreasing</td><td>Low</td><td>-</td><td>H3</td></tr><tr><td>DVD Movies</td><td>-0.117***</td><td>33.75***</td><td>-7.06 E-6***</td><td>17.46***</td><td>Decreasing</td><td>High</td><td>+</td><td>H4</td></tr></table>

<sup>⁎</sup> p b 0.10, <sup>⁎⁎</sup> p b 0.05, <sup>⁎⁎⁎</sup> p b 0.01.

we expect to find a positive sign for coefficient $\beta _ { 1 }$ for the book category. Because p R is the average standardized price along the sales rank, R, we state Hypothesis 1 accordingly:

H1. The average standardized price is an increasing function of the sales rank for the book category. Therefore, price and sales rank are positively correlated.

Our model prediction for a non-decreasing r[R] is strict; that is, an increasing p R must follow. However, our model predictions for a decreasing r[R] are also dependent on the cross-sales potential in the category. Specifically, our model predicts that if the cross-sales potential is low, p R will be decreasing, as Proposition 3 claims and Propositions 4 and 5 demonstrate. Next we briefly discuss the cross-sale potential in the categories with decreasing r[R]; MP3 songs, instant movies and DVD movies.

The profitability of cross-sales of an outside good is category-specific because the characteristics of the shopping environment and the potential for cross-sales vary across categories. In the Amazon.com context, both online music and streaming movies have their own shopping cart/checkout systems and, as such, only allow for a cross-selling opportunity within the category, if any. Furthermore, in both categories, purchase of additional content is highly unlikely because immediate consumption of the first purchase is possible. For example, in the song category, the purchase of a song may lead to the purchase of one or more songs, due to a shopping momentum effect [16]; however, the customer has no economies-of-scale motivations because digital downloads do not require handling, processing, or shipping costs. Similarly, in the streaming videos category, buying multiple titles yields no economies-of-scale benefits. Furthermore, given that a movie is likely to be viewed immediately after purchase, a shopping momentum effect is even less likely to lead to the purchase of two or more instant movies in the same transaction. Thus, by design, unless the consumer switches to a traditional shopping cart, the likelihood of cross-selling is limited. However, because the checkout processes are separate, switching to a traditional shopping cart is no different than switching to another online store and shopping and checking out. Thus, the profit potential from cross-sales is relatively low for digitally purchased and streamed content such as MP3 songs and instant movies.

However, the profit potential from cross-sales is relatively significant for a physical product that must be shipped. From the economies-of-scale argument (e.g., Amazon.com offers free shipping on orders of \$25 or more), the shopping momentum effect [16], or a windfall effect [24], movies on DVD, books and music CDs have a relatively positive cross-sales potential.

The size of the loyal segment determines the inertia a retailer would face when reducing the price of products to increase profits from crosssales. Because loyal customers purchase the product without price comparison, a price reduction on any product already assigns a loss in profitability from the loyal segment. Thus, we would expect to observe discounting only in categories in which the cross-selling potential is significant enough to overcome the loss from the loyal segment sales.

We can determine the profitability of cross-selling for the three categories for which we observe a decreasing r[R] according to the differences in their characteristics as they influence cross-selling based on the discussion above. Specifically, we expect a relatively low crosssales potential in the MP3 song category and instant video category and a high cross-sales potential in the DVD movie category. Thus:

H2. The average standardized price is a decreasing function of the sales rank for the MP3 songs category. Therefore, price and sales rank are negatively correlated.

H3. The average standardized price is a decreasing function of the sales rank for the Instant video category. Therefore, price and sales rank are negatively correlated.

H4. The average standardized price is an increasing function of the sales rank for the DVD movies category. Therefore, price and sales rank are positively correlated.

Note that the availability of the same set of movies in two formats, Instant Video and DVD, each with a different level of cross-sales profitability, provides a unique opportunity to test our model predictions. Thus, testing hypotheses 3 and 4 with data on the same products provides a robust test of our model that accounts for any productlevel effects. Table 3 summarizes our hypotheses.

To test hypotheses 1–4, we estimate the equation

Std:price $= \alpha + \beta _ { 1 }$ sales rank  ε

using both a simple linear regression and an ordered logit.

The results of the statistical tests appear in Table 4. Because the standardized slope coefficient in the simple linear regression is identical to the Pearson correlation coefficient, we present this coefficient as the correlation coefficient in Table 4. The table also reports the unstandardized slope coefficient of the ordered logit and its significance.

The results of both the simple linear regression and the ordered logit are consistent with each other and supportive of our model. We find that for books, the average standardized price is an increasing function, as our model predicts and in support of previous findings [20]. We also find that for movies that are instantly available through Amazon.com's streaming service, Instant Videos and for MP3 songs, the average standardized price is a decreasing function, as our model predicts. Recall that we use two maximum prices for standardizing the prices of instant movies: Movie\_Instant\_1 uses \$14.99, and Movie\_Instant\_2 uses the list price of the DVD. The findings are significant for MP3 songs and Movie\_Instant\_2 at the 0.01 level, while for Movie\_Instant\_1, the sign of the slope coefficient is not significant. We also find that the average standardized price function is increasing for the DVD movies category, as expected. This finding is also significant at the 0.01 level.

The findings of the empirical analysis provide strong support for our model. An increasing r[R] leads to an increasing price path in the books category, while a decreasing r[R] leads to a decreasing price path in the MP3 songs category. However, our test of movies, which Amazon.com offers in various formats, provides the strongest support for our model. By focusing on the same set of movies in two different formats, we are able to control for the possible effect of unobserved movie characteristics on both customer reviews and prices. For streaming movies, we expect decreasing standardized prices along the sales rankings because the cross-selling potential of an instant movie is almost negligible compared with the physical format DVD. By comparing the same set of 2435 movies available as both DVDs and streaming videos, we find that though r[R] is decreasing, the average price path has a positive slope for DVDs, while the slope is negative for streaming videos. As our model predicts, the lack of cross-selling potential for instant movies leads to higher prices for popular products with higher average customer reviews. The same popular movies in DVD format, however, are priced lower than the less popular DVD movies, despite the same slope for the average customer reviews, because of the cross-selling potential of the DVDs.

OLS and ordered logit model results.

<table><tr><td rowspan="2"></td><td colspan="2">Ordinary least squares</td><td colspan="2">Ordered logit</td><td colspan="2">Hypothesis</td></tr><tr><td>Price-sales rank correlation</td><td>F value</td><td> $\beta_1$ </td><td>Chi-square</td><td>Predicted linear relationship</td><td>Observed significant relationship</td></tr><tr><td>Books</td><td>0.345***</td><td>613.32***</td><td>5.55 E-7***</td><td>722.11***</td><td>+</td><td>+</td></tr><tr><td>MP3 songs</td><td>-0.039***</td><td>9.68***</td><td>-5.79 E-6***</td><td>10.53***</td><td>-</td><td>-</td></tr><tr><td>Instant Movies1</td><td>-0.003</td><td>0.025</td><td>1.37 E-7</td><td>0.005</td><td>-</td><td>N/A</td></tr><tr><td>Instant Movies2</td><td>-0.104***</td><td>26.54***</td><td>-6.69 E-6***</td><td>18.81***</td><td>-</td><td>-</td></tr><tr><td>DVD movies</td><td>0.147***</td><td>53.96***</td><td>1.24 E-5***</td><td>63.54***</td><td>+</td><td>+</td></tr></table>

<sup>⁎</sup> p b 0.10, <sup>⁎⁎</sup> p b 0.05, <sup>⁎⁎⁎</sup> p b 0.01.

## 5. Conclusion

Online retailing has enabled customers to browse practically unlimited selections to find music, books and movies. When sales, as well as traffic generation promise and reservation prices, depend on the popularity of items, oligopolistic retailers managing vast catalogs face both opportunities and challenges. How can a retailer enhance its pricing systems to determine the relative levels of prices across the distribution to account for the dynamics of own and cross-sales of items with popularity-dependent reservation prices? Our modeling effort distinguishes two separate forces that a pricing DSS should incorporate. The first force is the profitability of selling and cross-selling. The optimal pricing strategy that accounts for both own and cross-sales of items mandates a power law of prices that calls for disproportionate discounts on the superstars and diminishing but positive discounts on the middle and long tail items. The second force is the profitability from potential margins. A higher reservation price commanded by a popular or niche item enables the extraction of a premium that may increase or decrease along the sales distribution.

Our model findings show that any non-decreasing reservation price function yields an optimal pricing strategy in which retailers price superstars lower than any non-hit item. Our analysis of the average customer reviews of books along the sales rank reveals such nondecreasing reservation prices. Consequently, our empirical section supports the model prediction of an increasing price path for the book category.

A decreasing reservation price though cannot specify in and of itself the price path to emerge. A negligible potential loss from discounting to loyal customers and a category and shopping environment conducive to cross-selling of additional items may still give way to an increasing price path despite decreasing reservation prices. Our empirical analysis of the DVD movies fits with this set of circumstances. However, a significant potential loss from discounting to the loyal segment and a category and shopping environment unfavorable to cross-selling both lead to premium-priced superstars and obscure and deeply discounted niche products. Our empirical analysis of the MP3 songs and streaming movies shows that our model predicts the price path that emerges successfully in this set of circumstances.

The two categories of similar content in different formats further demonstrate the predictive power of our model. By focusing on the same set of movies in two different formats, we are able to control for the possible effect of unobserved product characteristics on both customer reviews and prices. By analyzing the same set of movies available both as instant videos and DVDs, both of which share a common decreasing reservation price path, our model illuminates how a hit movie can be available both for streaming at a premium and at a discount as a DVD and why obscure DVD movies cost more than the streaming version of the movie.

An alternative explanation of lower average prices on popular books and DVDs is the economies-of-scale argument. Because physical inventory is involved, higher volume leads to lower unit costs, which in turn lead to lower unit prices of popular items. In contrast, the cost structure of streaming videos is very different, in that it is subject to a separate rights agreement with the copyright owner; furthermore, it is natural to assume that popular content would command a higher royalty. Thus, for more popular items, there are no economies of scale but higher unit costs. While we conjecture that this argument has some effect on prices, industry reports show that the effect size of economies of scale in book retailing is almost negligible. Industry reports state retailer margins of 36%–50% on book list prices, claiming that printing, storage and physical distribution traditionally account for less than one-sixth of the total price of a book [27]. Consequently, economies-of-scale gains on storage and physical distribution (less than one-sixth the price of a book) have an almost negligible effect on prices, compared with the 36%–50% margin that the retailer gains by employing dynamic pricing based on demand. Similarly, on its investor relations page, Netflix announces streaming content margins of 40%, demonstrating the degree to which prices are uncoupled from licensing fees, not only for physical products that could benefit from economies of scale but also for digital content. Thus, although economies of scale or licensing fee arguments could account for some of the results obtained in our empirical analysis, the demand-side arguments seem to be more influential.

Cross-selling in general is not necessarily confined to just one customer; that is, the purchase of a product by a consumer may trigger the purchase of the same product by other customers in the same social circle. This leads to two types of cross-selling: retailer specific and product specific. This social influence on cross-selling is product specific, in that it is likely to have an effect on the sales and pricing of the product in general. However, because we focus on retailer-specific pricing of products and assume markets with many sellers, both in theory and in reality, we ignore this social influence in this paper. However, further research incorporating this product-centric cross-selling perspective could improve our understanding of pricing further.

Assuming a common reservation price for the entire market is a limitation of our model. Retailers do benefit from segmentation and targeting, which would enable them to manage separate groups of customers with different reservation price functions. A second limitation of our work is our use of data sets on products as they would be observable to browsing customers. Further research should use random data sets. And finally, our model assumes that both the price of the outside good and the sales rank are exogenous to the model. Allowing for an outside good with endogenous prices would improve our understanding of the pricing along the sales ranks tremendously. However, such endogeneity could complicate analysis significantly so future research should also explore ways to simplify the problem environment to obtain closed form solutions to allow for comparative statics. Empirical analyses that examine the dependence of prices of both popular and long tail products and sales ranks on one another would also provide further insight.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http://dx. doi.org/10.1016/j.dss.2016.06.008.

## References

[1] C. Anderson, The Long Tail: Why the Future of Business is Selling Less of More, first ed. Hyperion, New York, 2006.

[2] T. Bao, T.L.S. Chang, Why Amazon uses both the New York Times best seller list and customer reviews: an empirical study of multiplier effects on product sales from multiple earned media, Decision Support Systems 67 (2014) 1–8.

[3] R.F. Baumeister, Yielding to temptation: self-control failure, impulsive purchasing, and consumer behavior, Journal of Consumer Research 28 (4) (2002) 670–676.

[4] E.F. Borgatta, G.W. Bohrnstedt, Level of measurement—once over again, Sociological Methods & Research 9 (2) (1980) 147–160.

[5] E. Brynjolfsson, Long tails vs. superstars: the effect of information technology on product variety and sales concentration patterns, Information Systems Research 21 (4) (2010) 736–747.

[6] E. Brynjolfsson, Y. Hu, D. Simester, Goodbye Pareto principle, hello long tail: the effect of search costs on the concentration of product sales, Management Science 57 (8) (2011) 1373–1386.

[7] E. Brynjolfsson, Y. Hu, M.D. Smith, Consumer surplus in the digital economy: estimating the value of increased product variety at online booksellers, Management Science 49 (11) (2003) 1580–1596.

[8] E. Brynjolfsson, Y. Hu, M.D. Smith, From niches to riches: anatomy of the long tail, MIT Sloan Management Review 47 (4) (2006) 67–71.

[9] J. Chevalier, A. Goolsbee, Measuring prices and price competition online: Amazon com and BarnesandNoble com Ouantitative Marketing and Economics 1 (2) (2003) 203.

[10] J.A. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews, Journal of Marketing Research 43 (3) (2006) 345–354.

[11] E.K. Clemons, G.D. Gao, L.M. Hitt, When online reviews meet hyperdifferentiation: a study of the craft beer industry, Journal of Management Information Systems 23 (2) (2006) 149–171.

[12] E.K. Clemons, P.F. Nunes, Carrying your long tail: delighting your consumers and managing your operations, Decision Support Systems 51 (4) (2011) 884–893.

[13] P. DeGraba, The loss leader is a turkey: targeted discounts from multi-product competitors, International Journal of Industrial Organization 24 (3) (2006) 613–628.

[14] C. Dellarocas, X. Zhang, N.F. Awad, Exploring the value of online product reviews in forecasting sales: the case of motion pictures. Journal of Interactive Marketing 21 (4) (2007) 23–45.

[15] S. Dewan, J. Ramaprasad, Music blogging, online sampling, and the long tail, Information Systems Research 23 (3) (2012) 1056 1067.

[16] R. Dhar, J. Huber, U. Khan, The shopping momentum effect, Journal of Marketing Research 44 (3)(2007) 370–378

[17] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales—an empirical investigation of the movie industry, Journal of Retailing 84 (2) (2008) 233–242.

[18] A. Elberse, Should you invest in the long tail? Harvard Business Review 86 (7–8) (2008) 88–97.

[19] D. Fleder, K. Hosanagar, Blockbuster culture's next rise or fall: the impact of recommender systems on sales diversity, Management Science 55 (5) (2009) 697-712.

[20] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Information Systems Research 19 (3) (2008) 291–313.

[21] R.H. Frank, P.J. Cook, The Winner-Take-All Society: How More and More Americans Compete for Ever Fewer and Bigger Prizes, Encouraging Economic Waste, Income Inequality, and an Impoverished Cultural Life, Free Press, New York, 1995.

[22] D. Godes, J.C. Silva, Sequential and temporal dynamics of online opinion, Marketing Science 31 (3) (2012) 448–473.

[23] B. Gu, J. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales of high-involvement products, Information Systems Research 23 (1) (2012) 182–196 (281–283).

[24] C.M. Heilman, K. Nakamoto, A.G. Rao, Pleasant surprises: consumer response to unexpected in-store coupons, Journal of Marketing Research 39 (2) (2002) 242–252.

[25] J.D. Hess, E. Gerstner, Loss leader pricing and rain check policy, Marketing Science (1986–1998) 6 (4) (1987) 358–374.

[26] O. Hinz, J. Eckert, B. Skiera, Drivers of the long tail phenomenon: an empirical analysis, Journal of Management Information Systems 27 (4) (2011) 43–69.

[27] G.d.P.J.P. Simon, Statistical, Ecosystems and Competitiveness Analysis of the Media and Content Industries, The Book Publishing Industry, 2012.

[28] B.J. Jiang, K. Jerath, K. Srinivasan, Firm strategies in the “mid tail” of platform-based retailing, Marketing Science 30 (5) (2011) 757–775.

[29] D.R. Johnson, J.C. Creech, Ordinal measures in multiple indicator models—a simulation study of categorization error, American Sociological Review 48 (3) (1983) 398–407.

[30] S. Kalish, P. Nelson, A comparison of ranking, rating and reservation price measurement in conjoint analysis, Marketing Letters 2 (4) (1991) 327–335.

[31] R. Lal, C. Matutes, Retail pricing and advertising strategies, Journal of Business 67 (3) (1994) 345-370

[32] X. Li, L.M. Hitt, Price effects in online product reviews: an analytical model and empirical analysis, MIS Quarterly 34 (4) (2010) 809–831.

[33] M. Lin, S.J. Li, A.B. Whinston, Innovation and price competition in a two-sided market, Journal of Management Information Systems 28 (2) (2011) 171–202.

[34] J. Lu, D.S. Wu, M.S. Mao, W. Wang, G.Q. Zhang, Recommender system application developments: a survey, Decision Support Systems 74 (2015) 12–32.

[35] D. Mayzlin, Promotional chat on the Internet, Marketing Science 25 (2) (2006) 155–163,201.

[36] W.W. Moe, D.A. Schweidel, Online product opinions: incidence, evaluation, and evolution, Marketing Science 31 (3) (2012) 372–386.

[37] C. Narasimhan, Competitive promotional strategies, Journal of Business 61 (4) (1988) 427–449.

[38] G. Oestreicher-Singer, A. Sundararajan, Recommendation networks and the long tail of electronic commerce, MIS Quarterly 36 (1) (2012) 65–83.

[39] B. Pathak, R. Garfinkel, R.D. Gopal, R. Venkatesan, F. Yin, Empirical analysis of the impact of recommender systems on sales, Journal of Management Information Systems 27 (2) (2010) 159–188.

[40] S. Rosen, The economics of superstars, The American Economic Review 71 (5) (1981) 845.

[41] J.T. Townsend, F.G. Ashby, Measurement scales and statistics—the misconception misconceived, Psychological Bulletin 96 (2) (1984) 394–401.

[42] H.R. Varian, A model of sales, American Economic Review 70 (4) (1980) 651–659.

[43] L.Z. Xu, J.Q. Chen, A. Whinston, Oligopolistic pricing with online search, Journal of Management Information Systems 27 (3) (2010) 111–141.

[44] K.Z.K. Zhang, S.J. Zhao, C.M.K. Cheung, M.K.O. Lee, Examining the influence of online reviews on consumers' decision-making: a heuristic-systematic model, Decision Support Systems 67 (2014) 78–89.

[45] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, Journal of Marketing 74 (2) (2010) 133–148.

[46] B.D. Zumbo, D.W. Zimmerman, Is The selection of statistical-methods governed by level of measurement, Canadian Psychology-Psychologie Canadienne 34 (4) (1993) 390–400.

Cenk Kocas. PhD. is an Associate Professor of Marketing at the School of Management of Sabancı University, Istanbul, Turkey, His research interests are game theoretical models of price promotions, stochastic service systems and application of theory from economics. marketing and operations research in e-commerce and information systems research. He obtained his PhD in Management from the Krannert Graduate School of Management, Purdue University, Indiana. His work has appeared in journals such as the Journal of Marketing, International Journal of Electronic Commerce, International Journal of Industrial Organization, Journal of Management Information Systems and Marketing Letters.

Can Akkan, PhD, is an Associate Professor of Operations Management and Associate Dean at Sabancı University School of Management. His research interests are production scheduling, project scheduling and design, planning of discrete parts manufacturing systems, networks and social media dynamics. He holds a PhD degree in Operations Research from Cornell University. His work has appeared in journals such as the European Journal of Operational Research, Journal of the Operational Research Society, International Journal of Production Research and Journal of Logic & Algebraic Programming.
