---
otero_id: 25504
otero_key: "7HWTM4BS"
title: "Product Recommendation and Consumer Search"
authors: "Vidyanand Choudhary; Zhe (James) Zhang"
year: "2023"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2023.2229123"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Product Recommendation and Consumer Search

## Vidyanand Choudhary & Zhe (James) Zhang

To cite this article: Vidyanand Choudhary & Zhe (James) Zhang (2023) Product Recommendation and Consumer Search, Journal of Management Information Systems, 40:3, 752-777, DOI: 10.1080/07421222.2023.2229123

To link to this article: https://doi.org/10.1080/07421222.2023.2229123

![](/api/attachments/7HWTM4BS/fulltext/images/822a44aead159aa5b84a1812344373c8f476ba427694a563f3b26d68c8b66ced.jpg)

View supplementary material ↗

![](/api/attachments/7HWTM4BS/fulltext/images/d41324052186fb9a5ce872236c7da203f3ca1368d0d916cc6bdce4a2b8e37e15.jpg)

Published online: 23 Aug 2023.

![](/api/attachments/7HWTM4BS/fulltext/images/1f500a4ab9486795d33bd5070ff63e2887f6b38248cc45ca114c714f4e2b5f30.jpg)

Submit your article to this journal ↗

![](/api/attachments/7HWTM4BS/fulltext/images/155c742a6c83c82aa50d2d1a47ffa4d1d488e348c73af5a65e0366940d32119e.jpg)

Article views: 1732

![](/api/attachments/7HWTM4BS/fulltext/images/69b1faa0c41d1de1322f85d52804977d8d8d37b0d5d42e36cc6b8afc703b6e32.jpg)

View related articles ↗

![](/api/attachments/7HWTM4BS/fulltext/images/3d86a66eb6c56aea7772c9a2e29de53539a5d58a7dade089a0ceb62358024718.jpg)

View Crossmark data ↗

![](/api/attachments/7HWTM4BS/fulltext/images/5feb9143018a449a1346388b02ae5b2672deb6ee39cce3545ed70b97ba9f0807.jpg)

Citing articles: 11 View citing articles ↗

Check for updates

# Product Recommendation and Consumer Search

Vidyanand Choudhary $^{a}$ and Zhe (James) Zhang $^{b}$

$^{a}$ University of California, Irvine, Irvine, CA, USA; $^{b}$ University of Texas at Dallas, Richardson, TX, USA

## ABSTRACT

We study an online environment where a firm provides strategic product recommendations to consumers. We develop an analytical framework to integrate recommendations into the consumer search process. The firm sells two imperfectly substitutable products with different profit margins and makes a personalized product recommendation to each consumer based on its uncertainty (lack of knowledge) of his preferences. We define recommendation bias as the firm's deliberate decision to recommend a product to a consumer that does not minimize expected misfit cost of the consumer. Consumers can accept the product recommendation, search for the nonrecommended product, or leave the website. We identify five consumer segments based on consumers' responses to the firm's recommendations. We show that the recommendation bias, profit, and consumer surplus depend on the interaction between the firm's uncertainty regarding consumer preferences and consumer search costs. A reduction in its uncertainty about consumers leads to a corresponding increase in the firm's profit but does not necessarily result in a reduction in consumer surplus. An increase in search costs can lead to nonmonotonic changes in the firm's recommendation strategy, causing an increase or decrease in recommendation bias when the firm's uncertainty about consumers is low. Furthermore, the firm's profit can behave non-monotonically with respect to search costs: the firm benefits from an increase in search costs when these costs are small and uncertainty about consumers is low, but it can be adversely affected when search costs are moderate. Interestingly, consumer surplus may increase when search costs increase.

## KEYWORDS

Recommendation bias; consumer search; digital commerce; firm uncertainty; product recommendation; recommendation strategy; search cost; online recommenders; online commerce

## Introduction

Product recommendation systems are personalized sales assistance tools designed to make the product search process easier for consumers. In general, firms and online intermediaries use recommendation systems to provide personalized product or content recommendations that may attract individual consumers. In recent years, these systems have become increasingly popular on online platforms such as YouTube and Netflix. From a consumer perspective, recommendation systems make the product search process easier and less time-consuming. Moreover, a recommendation system could have a profound impact on how business is conducted $[15]$ . Per multiple reports, businesses generally use recommendation systems to favor a certain segment of products in consideration of overall profitability. Given that consumers have the choice of either following product recommendations or individually searching for products, the following questions are of importance: How does a recommendation system affect consumers' product search process, and how does a strategic firm determine which product to recommend?

Past studies have shown that recommendation systems affect consumer product search process $[3, 36]$ . Consumers may not have to search extensively for products if they receive recommendations based on their overall preferences in a scenario where they face many choices. Thus, product recommendations may reduce the time and effort incurred by consumers to search for products. Moreover, one of the main value propositions of recommendation systems is that they provide a consumption experience that is personalized to consumer tastes $[16, 29]$ . For example, YouTube is well-known for providing recommendations for users. After a user logs in, YouTube identifies this individual as someone who is interested in watching movies and recommends videos related to movies. After seeing these recommendations, the user can watch one of the recommendations or search for others using the search engine on YouTube.

Firms can use product recommendations to direct consumers' attention to specific products. Hagiu and Jullien [18] refer to the strategy of manipulating the consumer product search process by providing recommendations about a selection of certain products as search diversion. This strategy is commonly observed in online contexts. For example, online advertising-supported intermediaries, such as online news sites and search engines, display advertisements in prominent places next to the content that is of interest to consumers. One recent account is that Google allegedly manipulated search results by promoting its own services and suppressing competitors [5, 23]. Similar practices are also observed among certain online streaming and retail platforms. Netflix has reportedly used recommendations to drive its subscribers to House of Cards, its own in-house production, regardless of their preferences [10]. Amazon is also known to favor products with higher average revenue in its new product email newsletters sent to users [31]. These industry practices suggest that firms mainly employ recommendations to maximize overall profitability, often by steering consumers away from their preferred products. This bias in product recommendations has a profound impact on the firm's profits and consumers' consumption experiences.

Product recommendations are based on the predictions of consumer preferences. On the technical side, collaborative filtering and matrix factorization methods are the most common techniques of recommendation systems. Amazon in particular uses collaborative filtering as part of their product recommendation system $[30]$ . Matrix factorization methods have gained recognition partly because of successes in the Netflix Prize competition $[41]$ . Despite technical differences in algorithms and design, a common feature among these techniques is how they make use of the opinions of a community of users to predict the preferences of an individual given a potentially overwhelming set of choices. The predictions of individual users' preferences often involve complex computational algorithms and require large volumes of consumer-product data. Through predictive analysis, a firm can obtain a certain level of knowledge about users' preferences and use this knowledge to provide personalized product recommendations to individual users $[17]$ . Thus, the firm's level of knowledge about individual users' preferences affects users' receptions of product recommendations and their consumption experience.

Firms that provide product recommendations may contend with conflicting goals, such as assisting consumers in finding a desirable product versus continually increasing profitability $[12]$ . Conversely, a recommendation system generates faulty recommendations if the prediction about consumer preference is inaccurate. In other words, consumers could receive biased recommendations because the firm has a high level of uncertainty about consumer preferences $[2]$ . Thus, it is imperative to recognize how recommendation bias attributes to the firm's profitability maximization consideration. Furthermore, the rising popularity of recommendation systems that are based on knowledge about users came against the backdrop of public scrutiny about the collection and storage of user data. Existing or proposed regulations about consumer privacy and security specify requirements for companies and organizations on collecting, storing and managing personal data, inevitably increasing the difficulty for the firm's learning about consumers. Hence, understanding how the firm's uncertainty and knowledge about consumers affects the recommendation strategy has profound policy implications.

Understanding a firm's product recommendation strategy is a part of a broader discussion on the consumer information search and acquisition process in fields such as economics, marketing, and information systems. In Bakos [4], the electronic markets system provides a product search function that reduces consumer search costs and improves market efficiency. In recent years, firms have not only reduced consumer search costs via improved product search functionality, but also provided recommendation systems to consumers to improve their product search experience. Due to their popularity, recommendation systems have become a major theme of research [14, 35]; moreover, their impact on the consumer product search process and market structure have also been studied [24]. However, the interaction between product recommendations and consumer search has drawn a minimal amount of attention.

The main objective of this paper is to examine the firm's product recommendation strategy in an analytical framework which integrates product recommendations into the consumer search process. In this framework, the firm makes product recommendations to individual consumers based on a certain level of knowledge about their preferences. We define recommendation bias as the firm's deliberate decision to recommend the product with higher expected misfit cost for consumers. Diverging from the literature, we treat consumers as strategic and heterogeneous in their responses to product recommendations—consumers either accept the recommended product, reject it and search for non-recommended products, or leave the website. Moreover, we focus on the main benefit of product recommendations, which is to reduce the search costs incurred by consumers.

The key contribution of this paper is that we provide a microeconomic framework that examines the relationship between the two technology-mediated channels: recommendations and search. We endogenize the consumers' decision of accepting the recommendation or searching for the non-recommended product in this paper. This novel approach of considering the additional channel of search separates this paper from the recommendation system literature $[27, 28]$ , which largely considers only the channel of recommendations. We find that the level of bias depends on the firm's level of knowledge about consumers' product preferences and search costs. Interestingly, when the firm's level of knowledge about consumers' preferences increases or its uncertainty is reduced, the level of bias in product recommendations can increase or decrease. Moreover, we find that both the firm and consumers benefit when uncertainty is reduced under certain conditions. Lastly, we examine the effects of the interaction between the firm's recommendation strategy and search costs. We find that when search costs increase, the firm benefits but consumers are adversely affected if search costs are small. However, the power dynamics between the firm and consumers reverse if search costs are moderate: the firm is adversely affected but consumers benefit when search costs increase.

## Literature Review

There is a stream of literature which focuses on algorithms and the technical setup of recommendation systems that predict user preferences. Adomavicius and Tuzhilin $[1]$ provide an extensive review of these issues in the information systems literature. There are many recommendation algorithms as well as numerous methods for evaluating these algorithms. Early researchers have used both the proportion of correct and incorrect predictions to measure the viability of a recommendation system $[25]$ . The extant literature uses a variety of measures to evaluate a recommendation system, including the degree to which recommendations cover an entire set of items $[33]$ , the degree to which recommendations are nonobvious $[32]$ , and the probability of signals correctly identifying consumers' true locations $[27, 28]$ . This body of research assumes that recommendation systems are consumer-centric in their ability to recommend products with the highest probability of purchase $[6]$ . In contrast, we consider the case where the firm recommends the product in order to maximize its expected profit.

Despite a large body of extant work on the technical aspects of recommendation systems, there is limited understanding of the economic effects of recommendation systems on the market and in society $[21]$ . There is a growing stream of research focused on its implications in online market contexts. Studies have examined the impact of the use of recommendation systems on sales $[6, 37]$ and future sales $[22]$ , as well as the influence of recommendation systems on consumer choice $[20, 39]$ , consumer search behavior $[24, 42]$ , product demand $[13, 36]$ , competition $[14, 27]$ , and personalization services $[21, 35]$ . These studies take the view that the effects of product recommendations on consumers are homogenous. In our paper, we treat consumers as heterogeneous, model individual consumers' responses to product recommendations, and identify five consumer segments. We also show that the effects of a recommendation system on a firm's profit and consumer surplus depend on its level of uncertainty about consumers.

Similar to a number of other papers in the consumer search literature $[33, 34]$ , our paper builds on the economic theory of search $[40,43]$ . In recent years, a secondary stream has emerged, focusing on consumer search in online environments $[8, 9]$ . Bakos $[4]$ studies the implication of consumer search costs on online sellers' pricing and product strategies and the resulting reduction in market inefficiency. Dukes and Liu $[12]$ examine strategic incentives of an online intermediary in the design of its search environment as a means of reducing search costs. Kuksov and Villas-Boas $[26]$ show that consumers may not conduct an extensive search when there are either too many or too few products because the product search process is costly. These researchers focus on the impact of search costs on competition and how changes in competition affect firms and consumers. In this study, we build on this stream of literature by integrating product recommendations into the consumer search process. We show that in the absence of price competition, changes in search costs can have nonmonotonic effects on a firm's profit and consumer surplus.

Our paper is also related to a growing stream of literature which studies intermediaries' influence on consumers, particularly studies that focus on consumer search and recommendation bias. Hagiu and Jullien [18, 19] and De Corniere and Taylor [11] examine a web-search engine's incentives to divert their users toward a selected set of items due to factors including revenues from advertisements. Bourreau and Gaudin [7] examine biases in recommendations on streaming platforms. In these papers, firms are assumed to perfectly observe consumer preferences, whereas in this paper, the firm is uncertain about consumers' preferences, and this level of uncertainty drives the firm's recommendation strategy.

The majority of the literature examines either the effects of recommendation systems or the effects of search costs and largely ignores the interaction between the two, with the exception of Hagiu and Jullien [18], who study an online intermediary's search diversion strategy. In their paper, the firm recommends one of two stores based on perfect information about consumer preferences and earns a fee when consumers visit a store, even if a consumer does not make a purchase. A consumer incurs search costs when visiting a store whether it is recommended or not. The authors identify conditions under which search diversion is not beneficial to the firm. In contrast, in our paper, the firm earns revenue only when a consumer buys a product; thus, the firm has an incentive to use recommendations in favor of higher margin products. This leads to different results: diverging from their finding that increasing search costs always benefit the firm, we find that increasing search costs can be detrimental to the firm, as consumers may leave a website without buying any product. Moreover, the quality of product recommendations depends on the level of the firm's uncertainty about consumer preferences. Thus, the firm's recommendation strategy depends on the interaction between the firm's uncertainty about consumers and search costs.

## Model

We model a monopolist firm that sells two differentiated products, H and L, on its website. Following Salop's $[38]$ circular city model, we assume that a continuum of heterogeneous consumers is distributed uniformly on a circle of unit circumference, and products H and L are located equidistantly on the circle (H is located at 0 and product L is located at 1/2 in Figure 1. These consumers are indexed by their locations, denoted by x, which represents their preferences for products, and they consume at most one unit of product. We provide a Table of Notation in Appendix 1.

## Profit Margins of the Two Products

Following the recommendation systems and consumer search literature, we do not model price in this paper. Our model applies to many online content providers, such as YouTube, USA Today, and Pandora, which provide content to consumers without a fee for their basic services. Our paper also applies to firms that use a paid-subscription model, such as Netflix, Spotify, and WSJ, as their subscription fees do not change with small changes in consumer search costs or in the levels of uncertainty about consumer locations.

Firms earn different profit margins from products for a variety of reasons. $^{1}$ Without loss of generality, we assume that H is more profitable than L. We normalize the profit margin of H as $\eta_{H}=1$ , and the profit margin of L as $\eta_{L}=y<1$ .

![](/api/attachments/7HWTM4BS/fulltext/images/cfe4c834ee7ae40295a54f09fed419f85006d71c6f9297f1f032ba51604f8b14.jpg)  
Figure 1. Circular city model of consumer locations with the two products (H and L) located at 0 and $\frac{1}{2}$ .

## Consumer Utility

Consumers' misfit cost is linear in the distance between the consumers' ideal locations and the product location. A consumer located at $x$ who consumes product $i, i = H$ or $L$ , derives utility:

$$
u _ {i} (x) = V - d _ {i} (x) t, i \in \{H, L \}\tag{1}
$$

where $d_{i}(x)$ is the distance between the location of the consumer, x, and product i's location, t is the consumer misfit cost parameter, and V is the base utility. A consumer gets higher utility from product H than L if located at $x \leq 1/4$ or $x \geq 3/4$ , or gets higher utility from product L otherwise. Moreover, consumers may leave the website without consuming a product and seek an outside option. We normalize the outside option to zero; therefore, V is the value of the product relative to the outside option.

Consumers have incomplete information about locations of the firm's products. They believe with a certain probability $\beta$ , that the two products are located equidistantly on the circle, and with a probability $(1 - \beta)$ , they could be anywhere (equally likely) on the circle. We denote $\beta$ as the level of informedness of consumers about the true location of the products, where $0 < \beta < 1$ .

## Firm's Uncertainty About Consumers' Location

The firm knows the distribution of consumer locations but has imperfect information about consumer locations $[27, 28]$ . In practice, a firm may gather information about consumers and products, and then employ data mining techniques to predict individual consumers' locations. In our model, the firm can predict the interval within which a consumer is located. We refer to this interval of possible consumer locations as a bucket. Each bucket contains this consumer's true location.

When a consumer arrives at the firm's website, the firm does not know the consumer's true location; instead, the firm observes a bucket associated with that consumer. The width of the bucket is denoted by $r$ ( $0 \leq r \leq 1$ ) and is centered at $b$ (spans from $b - r/2$ to $b + r/2$ ). We use the width of the bucket ( $r$ ) to represent the level of the firm's uncertainty about consumers' location. Increased information and knowledge about consumers can lead to lower uncertainty about consumers' location, which implies a narrower bucket (smaller $r$ ). Figure 2 shows a consumer bucket, $b$ , for a consumer with true location at $x$ . We assume that a consumer's location is equally likely to be at any point in the bucket and the buckets are distributed uniformly on the circle, $b \sim U[0,1]$ . For convenience, we use a horizontal representation of the circular model, as shown on the right side of Figure 2.

![](/api/attachments/7HWTM4BS/fulltext/images/c05ed7de257fd244a62547276fb05fb00b93413df7717a52b8fc31b6dff268ea.jpg)  
Figure 2. Consumer bucket b for a consumer with true location at x.

Advanced data mining techniques or other methods of gathering information about consumer preferences may reduce the firm's uncertainty about consumer locations, and thus leads to narrower consumer buckets. At the limit, the firm has perfect information about consumer locations, which means the width of each bucket is zero, $r = 0$ . In other words, the firm can identify the exact location of individual consumers.

## Personalized Recommendations

The firm provides a product recommendation, H or L, to individual consumers when they arrive at the website. After seeing the recommendation, a consumer assesses the recommended product and realizes its location. $^{2}$ A consumer has three possible responses: 1) accept the recommended product; 2) reject the recommendation, incur a search cost, and then find the non-recommended product; or 3) reject the recommendation, then leave the website without consumption or searching. If a consumer searches for a product and finds out its location, then he incurs costs of identifying the product and assessing the product. $^{3}$ We denote the search costs with c. To simplify the analysis, we normalize the cost of assessing products to zero for both searched and recommended products. $^{4}$ A rational consumer will choose the response that maximizes his surplus.

What do the consumers know about the location of the firm's products? They can observe the location of the recommended product, and they may be able to use that information to estimate the location of the other product. After observing the location of the recommended product (0 if $s = H$ is recommended or 1/2 if $s = L$ is recommended), with probability $\beta$ , consumers correctly infer the location of the non-recommended product as the opposite from the location of the recommended product ( $L$ is at 1/2 if $s = H$ is recommended or $H$ is at 0 if $s = L$ is recommended), and with probability $(1 - \beta)$ they believe the location of the non-recommended product can be anywhere on the circle (i.e., uniformly distributed on the circle). Moreover, in case the search yields a product that is farther away than the distance to the recommended product, it is costless for consumers to recall the recommended product after searching.

When the firm recommends a product s to a consumer, its profit depends on this consumer's response: 1) the profit margin of the recommended product, $\eta_{s}$ , if the consumer accepts the recommendation; 2) the profit margin of the non-recommended product, $\eta_{k}$ , if the consumer rejects s and then searches for and consumes the non-recommended product k; or 3) zero profit if the consumer rejects s and leaves the website, where $s \neq k$ and $s, k \in \{H, L\}$ . The probabilities associated with these responses depend on the product recommendation, location of the bucket, b, and the firm's uncertainty about consumer preferences, r. The firm's expected profit from recommending product s to a consumer in a bucket centered at b is:

$$
E \left(\pi_ {b} (s)\right) = \eta_ {s} \times P r _ {b} (\text { consume } s) + \eta_ {k} \times P r _ {b} (\text { search   and   consume } k),\tag{2}
$$

where $s \neq k$ and $s, k \in \{H, L\}$ .

The firm compares its expected profit from recommending H and that from L to a particular bucket b, $E(\pi_{b}(H))$ and $E(\pi_{b}(L))$ , and recommends the product, $s_{b}$ , that leads to a higher expected profit (i.e., $s_{b} = H$ if $E(\pi_{b}(H)) > E(\pi_{b}(L))$ , and $s_{b} = L$ otherwise). We assume that the firm follows a Pareto optimal strategy by recommending the product that leads to higher consumer surplus when the expected profits of recommending H and L are equal. This recommendation strategy leads to the highest total profit for the firm. The firm's expected total profit from providing personalized recommendations to individual consumers is:

$$
E (\pi) = \int_ {0} ^ {1} E (\pi_ {b} (s _ {b})) d b
$$

Given the firm's recommendation of product $s$ , a consumer derives utility from the recommended product $u_{s}$ upon purchasing it. If the consumer rejects the recommendation $s$ and searches and consumes the non-recommended product $k$ , then he obtains utility net of search costs, $u_{k} - c$ . If he leaves the website without consuming either product, then he obtains zero utility. The expected surplus of a consumer bucket centered at $b$ with a product recommendation of $s$ is:

$$
\begin{array}{c} E (C S _ {b} (s)) = u _ {s} \times P r _ {b} (\text { consumes }) + (u _ {k} - c) \times P r _ {b} (\text { searchandconsumek }), \\ \text { where } s \neq k \text { ands }, k \in \{H, L \} \end{array}\tag{3}
$$

Summing the expected surplus from all consumer buckets following the firm's recommendation strategy, we get expected consumer surplus:

$$
E (C S) = \int_ {0} ^ {1} E (C S _ {b} (s _ {b})) d b
$$

## Timeline

The firm observes a bucket of locations associated with a consumer who visits the firm's website and recommends a product, $H$ or $L$ , to the consumer. After observing the product recommendation, the consumer chooses one of the three responses: to consume the recommended product, to search for the non-recommended product, or to leave the website. If the consumer searches for the non-recommended product, then she will make a consumption decision after finding the non-recommended product. Finally, the firm realizes its profit margin of the consumed product.

## Bias in Product Recommendations

A consumer-centric and unbiased recommendation strategy would always recommend the product that minimizes consumers' expected misfit costs based on the firm's imperfect knowledge about consumers' preferences. Recall that recommendation bias is the firm's deliberate decision to recommend a product to a consumer that does not minimize the expected misfit cost of the consumer. Bias is recommending H to a consumer with a bucket 1/4 < b < 3/4, or recommending L to a consumer with a bucket b < 1/4 or b > 3/4. We quantify the level of bias in recommendations as follows:

$$
B i a s = \int_ {0} ^ {1 / 4} I [ b, L ] d b + \int_ {1 / 4} ^ {3 / 4} I [ b, H ] d b + \int_ {3 / 4} ^ {1} I [ b, L ] d b
$$

Here, $I[b,s]=1$ if a consumer bucket centered at b receives a product recommendation of s, or $I[b,s]=0$ , otherwise.

We assume 2V < t < 4V. When t < 4V, the market is fully covered by the two products. If $t \geq 4V$ , each consumer obtains positive utility from at most one product (the preferred product). In this case, the recommendation strategy has little influence on product consumption since consumers either consume their preferred products or leave the website. Conversely, when t > 2V, consumers have strong product preferences – consumers who are at the location of their preferred product derive negative utility from the other product. If $t \leq 2V$ , all consumers will consume a product even if the recommendation is the product further away. In this case, the firm's recommendation strategy is trivial: recommending product H to all consumers.

## Analysis

In this section, we first identify consumer segments based on consumer responses to the firm's product recommendations. Second, we characterize the firm's optimal recommendation strategy. Lastly, we examine the effects of the firm's uncertainty about consumer locations and consumer search costs on its recommendation bias, expected profit, and consumer surplus.

## Consumer Segments

Consumers have three possible responses to a product recommendation. Consumers who are close to the location of this product accept the recommendation because they receive higher utility compared to leaving the website or searching for the non-recommended product. The remaining consumers who are located farther away from the recommended product reject it, leading to two possible responses. Among the consumers rejecting the recommendation, some who are far away from the recommended product may realize an incremental gain in expected utility from searching for the non-recommended product. Thus, they search for the non-recommended product after rejecting the recommended product. Other consumers may not get positive utility from the recommended product or an incremental gain in expected utility from searching for the non-recommended product when search costs are not small. Thus, they reject the recommendation and leave without making a purchase.

Based on their responses to product recommendations, we group consumers into three types: Indifferent, Loyal, and Averse, respectively. We refer to consumers who are located halfway between the two products and have no incremental gain in the expected utility from searching for their preferred products as Indifferent consumers. They also gain positive utility of either of the two products; thus, they accept the recommendation regardless of the product being recommended. Additionally, we refer to consumers who have a strong preference to their preferred product (the closer product) and get high incremental gains in utility from searching if they receive a recommendation of the non-preferred product as Loyal consumers. They accept the recommendation if their preferred product (the closer product) is recommended or they search for this product otherwise; thus, they always consume their preferred product either via the recommendation or search. Finally, when the search costs are not small, leaving the website becomes an attractive option for consumers. We refer to consumers, who are located between the Loyal and the Indifferent consumers when search costs are significant, as Averse consumers. They derive lower utility from the preferred product than Loyal consumers but incur higher misfit to the nonpreferred product than Indifferent consumers. Thus, they leave the website without searching for their preferred product if they receive a recommendation of their nonpreferred product.

We describe the ranges of these consumer segments in Lemma 1. Note that the ranges of consumer segments from 1/2 to 1 are symmetric to those from 0 and 1/2 described in Lemma 1. (All proofs are in the Online Supplemental Appendix.)

\- LEMMA 1 (Consumer segments): For consumer locations within 0 and $\frac{1}{2}$ :

(a) when the search costs are small ( $c_0 < c \leq c_1$ ), the Loyal consumer segments are located from 0 to $x_{LH}$ and $x_{HL}$ to 1/2 and the Indifferent consumer segment is located from $x_{LH}$ and $x_{HL}$ , where $c_0 = (t^2 - 4V^2)(1 - \beta)/(4t)$ , $c_1 = V(1 + \beta) - V^2(1 - \beta)/t - t\beta/2$ , $x_{HL} = 1/4 + (4ct + (4V^2 - t^2)(1 - \beta))/(4t^2(1 + \beta))$ and $x_{LH} = 1/2 - x_{HL}$ ;

(b) when the search costs are moderate ( $c_1 < c \leq c_2$ ), the Loyal consumer segments are located from 0 to $x_{LO}$ and from $x_{HO}$ to 1/2, the Averse consumer segments are located from $x_{LO}$ to $x_L$ and from $x_H$ to $x_{HO}$ , and the Indifferent consumer segment is located from $x_L$ and $x_H$ , where $c_2 = V(t - V(1 - \beta)) / t$ , $x_H = V / t$ , $x_{HO} = 1/2 - (V(t - V(1 - \beta)) - ct)$

$$
/ (t ^ {2} \beta), x _ {L} = 1 / 2 - x _ {H} a n d x _ {L O} = 1 / 2 - x _ {H O}.
$$

We note that, when search costs are insignificant, $c \leq c_{0}$ , all consumers are Loyal: a consumer accepts the recommendation only if his preferred product is recommended, and always rejects the recommendation and searches for his preferred product otherwise. This implies that product recommendations are inherently ineffective in influencing consumers' product search decisions. Conversely, when search costs are large, $c \geq c_{2}$ , a consumer either leaves the website or accepts the recommendation if his non-preferred product is recommended. This means that consumers would never search after receiving a product recommendation. Neither of these two cases matches the characteristics of the consumers' behaviors observed in business practices. Therefore, our analysis only focuses on cases where search costs are significant but not large (i.e., $c_{0} < c < c_{2}$ ), because it is when product recommendations can be effective in influencing consumers' product search decisions and consumers' decision to search depending on the recommendations they receive.

We label the consumer segments with Indifferent, Loyal to H, Averse to L, Averse to H, and Loyal to L, and illustrate these consumer segments from 0 to 1/2 in the small search cost case, $c_{0} < c <= c_{1}$ , and the moderate search cost case, $c_{1} < c < c_{2}$ , in Figure 3. The size of these consumer segments changes with search costs. When search costs are small, increasing search costs leads to the expansion of the Indifferent segment ( $x_{LH}$ decreases and $x_{LH}$ increases). This means more consumers are inclined to accept recommendations. Moreover, when search costs are moderate, increasing search costs leads to the expansion of the Averse to L segment and Averse to H segment ( $x_{LO}$ decreases and $x_{HO}$ increases). This means more consumers could leave the website.

A consumer could be in more than one of these segments since the firm is uncertain about consumer locations. Figure 4 illustrates that, for a consumer who is associated with a bucket centered at b, the true location of the consumer could be in the Indifferent segment or Averse segments when uncertainty is low, or could be in all five segments when uncertainty is high. The probability of this consumer being in one of the five segments is represented by the proportion of the bucket overlapping with the segment. We denote the probability of this consumer being in the Loyal to H, Averse to L, Indifferent, Averse to H, and Loyal to L segments as $Pr_{b}(Loyal_{H})$ , $Pr_{b}(Averse_{L})$ , $Pr_{b}(Indiferent)$ , $Pr_{b}(Averse_{H})$ , and $Pr_{b}(Loyal_{L})$ , respectively.

Figure 3. Locations of the consumer segments from 0 to $\frac{1}{2}$ .  
![](/api/attachments/7HWTM4BS/fulltext/images/7e9b60ecff0a2c63f13426ae40ae5dabc9913b3dcbdc0d9f6771aa4c4347a76a.jpg)  
Figure 4. A consumer with a bucket, which is centered at b and ranges from $(b-r/2)$ to $(b+r/2)$ , spans over Indifferent and Averse to H consumer segments when search costs are moderate.

## Optimal Personalized Recommendation Strategy

The firm's product personalized recommendation strategy depends on the expected profit of recommending $H$ and that of recommending $L$ to individual consumers. Based on the probabilities of a consumer belonging to the various consumer segments, the firm calculates the expected profits of recommending $H$ and that of recommending $L$ to this consumer. The expected profit of recommending a product to a consumer stated in Equation (2) yields the following two equations with respect to the probabilities of this consumer belonging to one of the five consumer segments:

$$
E \left(\pi_ {b} (H)\right) = P r _ {b} \left(L o y a l _ {H}\right) + P r _ {b} \left(A v e r s e _ {L}\right) + P r _ {b} \left(I n d i f f e r e n t\right) + P r _ {b} \left(L o y a l _ {L}\right) y\tag{4}
$$

$$
E \left(\pi_ {b} (L)\right) = P r _ {b} \left(L o y a l _ {H}\right) + P r _ {b} \left(I n d i f f e r e n t\right) y + P r _ {b} \left(A v e r s e _ {H}\right) y + P r _ {b} \left(L o y a l _ {L}\right) y
$$

We define $b^{*}$ as the marginal consumer such that the firm should recommend $H(S_{b} = H)$ to consumers with buckets, $0 \leq b < b^{*}$ or $1 - b^{*} < b \leq 1$ , and recommend $L(S_{b} = L)$ to consumers with buckets $b^{*} \leq b \leq 1 - b^{*}$ . In other others, $b^{*}$ represents the firm's optimal recommendation strategy: the number of consumers receiving the recommendation of $H$ increases if $b^{*}$ increases or decreases if $b^{*}$ decreases.

Alternatively, the firm can recommend both products to all consumers. After seeing the recommendations, consumers assess both products and realize the product locations without incurring any search cost, and then they consume the product that leads to the higher utility. We refer to this non-personalized recommendation strategy as the benchmark case. We compare the firm's profit of personalized recommendation strategy for a product to individual consumers with the profit of the benchmark case and report the firm's optimal personalized recommendation strategy in Proposition 1. (We report the expression of $b^{*}$ and the corresponding conditions in the Online Supplemental Appendix.)

\- PROPOSITION 1 (Optimal personalized recommendation strategy): When the profit margin of product $L$ is low ( $y < (4V - t)/(2V)$ ):

(a) the firm should recommend $H$ to consumers who are associated with a bucket centered at $b$ , $0 \leq b < b^{*}$ , or $1 - b^{*} < b \leq 1$ , and recommend $L$ to the remaining consumers when the uncertainty about consumer locations is low ( $r < r_{s}$ if $c_{0} < c \leq c_{1}$ or $r < r_{m}$ if $c_{1} < c < c_{2}$ );

(b) the firm should recommend H to all consumers when the uncertainty about consumer locations is high ( $r \geq r_{s}$ if $c_{0} < c \leq c_{1}$ or $r \geq r_{m}$ if $c_{1} < c < c_{2}$ ).

The level of bias in recommendations depends on the firm's uncertainty about consumer locations. One would expect bias to be a side effect of the firm having too much information, hence expect bias to be higher when the firm has little uncertainty about consumers' locations. However, our result shows that the level of bias in the recommendations is uninformed. The level of bias is the highest, that is, recommending $H$ to all consumers, if the firm is highly uncertain about consumer locations. Otherwise, the firm recommends $H$ to some consumers and $L$ to the remaining consumers when uncertainty about consumers is low.

To understand why this occurs, we explore how the firm's incentives to recommend $H$ to consumers change with respect to its uncertainty about consumer locations and consumer search costs. When search costs are small, no consumer would leave the website since they are either Indifferent or Loyal consumers. Thus, the firm recommends H to consumers who are likely to be Indifferent to recommendations or Loyal to H. In theory, the firm has other strategies which produce the same profit. In such cases, the firm follows the Pareto optimal strategy, recommending L to consumers who are located close to L when the expected profit of recommending H and that of recommending L are the same, and recommending H to the remaining consumers. Thus, the firm recommends L to consumers if their buckets are completely in the Loyal to L segment and recommends H otherwise. On the other hand, when uncertainty about consumer locations is high, the firm is unsure about consumers' responses to a recommendation or whether a consumer is close to H or close to L. Thus, the firm recommends H since it is more profitable to do so.

When search costs are moderate, the Averse consumers leave the website if the farther product is recommended. In this case, the firm's recommendation strategy is driven by two forces: 1) the greedy force, which pushes the firm to recommend $H$ to all consumers since it is more profitable than $L$ ; and 2) the market share maximizing force, which pushes the firm to minimize the probability of consumers leaving the website by recommending $H$ or $L$ . The firm's recommendation strategy hinges on the balance of these two forces. Setting the two expected profits equal in (3), we have $\frac{Pr_b(Averse_H) - Pr_b(Averse_L)}{Pr_b(Indifferent) + Pr_b(Averse_H)} = 1 - y$ .

We denote $M(b)=\frac{Pr_{b}(Averse_{H})-Pr_{b}(Averse_{L})}{Pr_{b}(Indifferent)+Pr_{b}(Averse_{H})}$ as the proxy for the market share maximizing force and 1-y as the proxy for the greedy force with respect to a consumer in bucket b. The market share maximizing force is strong when a consumer is more likely to be in the Averse to H segment than to be in the Averse to L segment. When the market share maximizing force is stronger than the greedy force, the firm recommends L to the consumer, and recommends H otherwise. Note that $M(b)$ does not include $Pr_{b}(Loyal_{H})$ or $Pr_{b}(Loyal_{L})$ because these two segments always consume H or L, respectively.

When search costs are moderate and uncertainty about consumer locations is high, the market share maximizing force is weak: the probabilities of a consumer leaving the website after receiving a recommendation of $H\left(Pr_{b}(Averse_{H})\right)$ and that of receiving a recommendation of L $(Pr_{b}(Averse_{L}))$ are similar in magnitude. Thus, the firm should recommend H to all. Conversely, when search costs are moderate and uncertainty is low, the market share maximizing force is stronger for consumers who are located close to L: for these consumers, the probability of leaving the website after receiving a recommendation of H is higher than that of receiving a recommendation of L. Therefore, the firm should recommend L to these consumers when the market share maximizing force prevails, and recommend H to the remaining consumers.

From Proposition 1, it is apparent that the firm's recommendation strategy depends on the interaction of search costs and the firm's uncertainty about consumers. Moreover, since $1/4 \leq b^{*} < 1/2$ , the consumers who the firm perceives to have lower expected misfit with $H$ than with $L$ always receive a recommendation of $H$ . This also means that some consumers who have lower expected misfit with $L$ than with $H$ receive a biased recommendation. Therefore, we can represent the level of bias in recommendations as a function of the firm's optimal recommendation strategy (i.e., $bias = 2b^{*} - 1/2$ ). It is clear that the level of bias in recommendations increases if $b^{*}$ increases, or decreases if $b^{*}$ decreases.

The firm is better off by strategically recommending a product to individual consumers than recommending both products to all consumers when the profit margin of L is low (i.e., $y < (4V - t)/(2V)$ ). In the benchmark case where the firm recommends both products to all consumers, they realize the product locations and consume their preferred products (no consumer leaves the website without consumption). This means that consumers, who are in the Indifferent segment and closer to L, consume L, even though they could consume H if the firm made personalized recommendations of H to them, leading to a loss of 1 - y in profit per consumer. The loss in profit from these consumers is more than the loss of consumers who are Averse to H and leave the website after receiving the personalized recommendation of H if the profit margin of L is low.

We limit the analysis from now on to the cases where it is optimal for the firm to strategically recommend one product to individual consumers (i.e., profit margin of Product $L$ is low, $y < (4V - t) / (2V)$ ). Next, we analyze the impact of the firm's uncertainty and consumer search costs on the recommendation strategy, profit, and consumer surplus.

## Effect of Firm's Uncertainty About Consumer Locations

Recall that the lower the uncertainty about consumer locations, the shorter the width of a consumer bucket. Thus, consumers' probabilities of belonging to various consumer segments can change when uncertainty decreases. Moreover, the ways in which changes in consumers' probabilities of belonging to various segments affect the firm's recommendation strategy depend on search costs. When search costs are small, the number of consumers who are likely to be in the Loyal to $L$ segment decreases as uncertainty decreases. When search costs are moderate, the market share maximizing force $M(b)$ changes for some consumers, even though the greedy force does not change with decreasing uncertainty. Thus, a decrease in uncertainty about consumers alters the balance of the two forces.

Moreover, when the uncertainty is high ( $r \geq r_s$ if $c_0 < c \leq c_1$ or $r \geq r_m$ if $c_1 < c < c_2$ ), the firm recommends $H$ to all consumers (Proposition 1). A small increase in uncertainty does not alter the dominance of the greedy force over the market share maximizing force. Thus, the firm does not change its strategy of recommending $H$ to all consumers. We summarize the effects of the firm's uncertainty on its recommendation strategy when the personalized recommendation strategy is optimal ( $y < (4V - t)/(2V)$ ) and when the uncertainty is not high ( $r < r_s$ if $c_0 < c \leq c_1$ or $r < r_m$ if $c_1 < c < c_2$ ) in Proposition 2.

\- PROPOSITION 2 (Impact of uncertainty on bias in recommendations when the firm's personalized recommendation strategy is optimal and uncertainty is not high): When uncertainty about consumer locations decreases (r decreases), the level of bias in recommendations:

(a) decreases i) if search costs are small ( $c_{0}<c\leq c_{1}$ ) and the uncertainty is not high ( $r<r_{s}$ ); or ii) if search costs are moderate ( $c_{1}<c<c_{2}$ ), uncertainty is not high ( $0<r\leq r_{1}$ or $r_{3}<r\leq r_{m}$ ), and the profit margin of L is low (y<1/2);

(b) increases if search costs are moderate ( $c_1 < c < c_2$ ), the uncertainty is not high ( $0 < r \leq r_1$ or $r_3 < r \leq r_m$ ), and the profit margin of $L$ is moderate ( $1/2 < y < (4V - t)/(2V)$ ).

Reduction in uncertainty about consumer locations allows the firm to better predict consumers' responses to product recommendations. Thus, one may expect the level of bias in the firm's recommendation strategy to increase with increased information about consumers. In other words, the firm should introduce more biased recommendations (deliberately recommend $H$ to more consumers) as its knowledge of consumer location improves. However, we find that the level of bias in recommendations can decrease with a reduction in the firm's uncertainty about consumer location (Proposition 2, part a). One could also attribute bias in recommendations to the firm's uncertainty about consumer locations and expect bias to decrease when it decreases. But we find that the firm increases the level of bias in recommendations and deliberately recommends $H$ to more consumers when the uncertainty reduces. The apparent discord in the results indicates the complex effects of the firm's uncertainty about consumers on bias in the recommendations.

First, we explain why the impact of the uncertainty about consumers' locations on the firm's recommendation strategy is subject to the magnitude of search costs. When search costs are small and uncertainty is low, as discussed previously, the firm should recommend $L$ to a consumer who is certain to be in the Loyal to $L$ segment. Intuitively, the number of these consumers increases as uncertainty decreases. Therefore, the firm recommends $L$ to more consumers and recommends $H$ to fewer consumers, and thus the level of bias in recommendations decreases (Proposition 2, part a.i).

Now, we explain the effects of the uncertainty about consumers on the firm's recommendation strategy in the case where search costs are moderate (Proposition 2, parts a.ii and b). The effects of uncertainty on the location of the marginal consumer $(b^{*})$ depend on the strength of the greedy force when uncertainty is low and search costs are moderate. When the greedy force is stronger ( $y$ is low, i.e., $1/2 < y$ ), the marginal consumer moves closer to $L$ . This implies that the marginal consumer is more likely to be in the Averse to $H$ segment. When uncertainty decreases, the firm is more certain that this marginal consumer belongs to the Averse to $H$ segment. This strengthens the market share maximizing force and drives the firm to decrease the number of recommendations of $H$ . This means that the level of bias in recommendations decreases. Conversely, when the greedy force is weak ( $y$ is moderate, i.e., $1/2 < y < (4V - t)/(2V)$ ), the marginal consumer is more likely to be away from the Averse to $H$ segment. Therefore, when uncertainty decreases, the firm is more certain that this consumer does not belong to the Averse to $H$ segment, and its risk of the consumer's leaving the website without consumption is lowered. Under these conditions, a weakening of the market share maximizing force can drive the firm to increase the number of consumers getting a recommendation of $H$ . Thus, the level of bias in recommendations increases.

In Figure 5, we show the effects of the uncertainty about consumers on the level of bias in firm's recommendation strategy when search costs are moderate. Recall that when the uncertainty about consumers is large (i.e., $r > r_m$ ), the firm's optimal strategy is to recommend $H$ to all consumers (Proposition 1), resulting in a discontinuity in the level of bias at $r = r_m = 0.48$ in Figure 5. It is evident that a decrease in uncertainty leads to an increase in the level of bias when the uncertainty is small ( $r < r_m$ ), whereas there is no change in the level of bias when the uncertainty is large ( $r > r_m$ ).

Changes in the firm's uncertainty about consumers' preferences affect both the firm and the consumers. One could expect the firm's profit to increase when uncertainty decreases. However, the effect of decreasing uncertainty on consumers is not definitive. Conversely, consumers can benefit from a decrease in uncertainty, as the firm can better target consumers with recommendations and fewer consumers search or leave the website. Additionally, consumers can be adversely affected when they are located close to $L$ but consume $H$ because it is recommended. We summarize the effects of uncertainty on the firm's profit and consumer surplus in Proposition 3.

![](/api/attachments/7HWTM4BS/fulltext/images/b2eaaa199707e0724808bbaf83c90d6996b625b688af47263c558722633303d9.jpg)  
Figure 5. Level of bias in recommendations with respect to changing uncertainty about consumers (from r = 0.3 to r = 0.7) when search costs are moderate where t = 5.1, V = 2, c = 1.6, y = 0.56, and $\beta = 0.5$ .

\- PROPOSITION 3 (Impact of uncertainty on profit and consumer surplus): When the uncertainty about consumers decreases:

(a) the firm's profit weakly increases; and

(b) consumer surplus increases i) if search costs are small ( $c_0 < c \leq c_1$ ) and the uncertainty is low ( $r < r_s$ ); or ii) if search costs are moderate ( $c_1 < c < c_2$ ), the uncertainty is low ( $0 < r \leq r_1$ ), and the profit margin of $L$ is low ( $y < 1/2$ ).

This proposition shows that the firm and consumers are not in a zero-sum game. One may think the firm's profit increases at the expense of consumers since the firm is able to extract more surplus from consumers when it has more knowledge about their preferences (uncertainty about consumers decreases). On the contrary, we find that both the firm and consumers can be better off with a decrease in the former's uncertainty when it is well informed about consumer preferences. It is surprising that this win-win situation takes place when the firm has extensive information about individual consumers' product preferences.

To understand this result, recall that the firm recommends H to fewer consumers as uncertainty decreases when search costs are small and the uncertainty about consumers is low, as shown in Proposition 2, part a.i. This means that more consumers receive a recommendation of their preferred product: some consumers in the Loyal to L segment receive a recommendation of L instead of H. This reduction in search costs leads to an increase in consumer surplus.

When search costs are moderate, there are three possible effects of increasing the firm's ability to target consumers: 1) the number of consumers who search decreases, 2) the number of consumers who leave the website decreases, and 3) some consumers experience an increase in misfit costs. The effects 1 and 2 always increase consumer surplus whereas effect 3 decreases consumer surplus. When uncertainty decreases, the firm recommend $L$ to more consumers if search costs are moderate ( $c_1 < c < c_2$ ), uncertainty is low ( $0 < r \leq r_1$ ), and the profit margin $L$ is low ( $y < 1/2$ ), as shown in Proposition 2, part a.ii. When the firm recommends $L$ to more consumers, effects 1 and 2 prevail, leading to an increase in consumer surplus. Conversely, both effects 1 and 2 lead to higher overall demand when the firm's uncertainty decreases. In addition, the firm is better able to target consumers in the Indifferent segment with recommendations of $H$ when uncertainty decreases. Thus, an increase in demand and better targeting of the Indifferent consumers contribute to an increase in the firm's profit. We illustrate the effects of uncertainty on consumer surplus when consumer search costs are moderate, uncertainty is low, and the profit margin $L$ is low in Figure 6.

## Effects of Consumer Search Costs

Scholars and practitioners often associate the advent of electronic marketplaces with decreasing consumer search costs. In the presence of a recommendation system, search costs affect the firm's recommendation strategy since the size of some consumer segments changes when search costs decrease (the sizes of the Indifferent, Averse to H, and Loyal to L segments when the search cost is moderate are different from those when the search cost is small in Figure 3). We summarize the effects of search costs on the firm's recommendation strategy in Proposition 4.

![](/api/attachments/7HWTM4BS/fulltext/images/63d7e73c5e18dfd80f1c4a6f7107c02da35abd2c940b33b26673f03c0b285bdc.jpg)  
Figure 6. Consumer surplus with respect to changing uncertainty about consumers (from r = 0 to r = 0.2) and search costs are moderate where t = 5.1, V = 2, c = 1.6, y = 0.48, and $\beta = 0.5$ .

\- PROPOSITION 4 (Impact of search costs on recommendation strategy): When search costs decrease, the level of bias in recommendations:

(a) decreases when search costs are small and the uncertainty about consumers is low $c_{0}<c\leq c_{1}$ and $r\leq r_{s}$ ;

(b) weakly increases when search costs are moderate and uncertainty about consumers is low ( $c_{1} < c < c_{2}$ and $r \leq r_{m}$ );

(c) does not change when uncertainty is high ( $r > r_s \cap c_0 < c \leq c_1$ ) $\cup (r > r_m \cap c_1 < c < c_2)$ ).

It is interesting that the level of the bias changes non-monotonically with search costs when the uncertainty about consumers is low. What drives this non-monotonic behavior? When search costs are small and uncertainty is low, the firm's recommendation strategy is driven by the number of consumers that belong to the Loyal to L segment as search costs increase. As discussed previously, the firm recommends L to consumers when it is certain consumers belong to the Loyal to L segment. Moreover, when search costs decrease, the width of the Loyal to L segment increases. Thus, the firm increases the number of recommendations of L, and the level of bias decreases.

As discussed previously, the firm's strategy depends on the balance of the greedy force and the market share maximizing force when search costs are moderate and uncertainty is low. In this case, the firm's recommendation strategy is driven by the shrinking of the Averse to $H$ segment as search costs decrease. Thus, the marginal consumer is less likely to be Averse to $H$ , which leads to weakening of the market share maximizing force. Therefore, the firm recommends $H$ to more consumers as search costs decrease, and the level of bias increases. We represent the effects of search costs on the level of bias in recommendations in Figure 7.

Lastly, we explain why a decrease in search costs does not affect the firm's recommendation strategy when uncertainty is high. When uncertainty is low and search costs are small, the firm is not certain about any consumer being in the Loyal to $L$ segment. Thus, the firm does not change the strategy of recommending $H$ to all consumers with a small decrease in search costs. Conversely, when search costs are moderate and uncertainty is high, the firm's recommendation strategy is dictated by the greedy force. Under these conditions, the greedy force dominates the market share maximizing force. Thus, a small change in search costs does not alter the balance of these two forces, and therefore the firm does not change the strategy of recommending $H$ to all consumers.

Decreasing search costs lead to changes in the firm's recommendation strategy, as well as changes in the firm's profit and consumer surplus. We summarize our findings of the effects of search costs on the firm's profit and consumer surplus in Proposition 5.

![](/api/attachments/7HWTM4BS/fulltext/images/d8dbd93fcd90a76d9e965c203a8aefef9de9f5ebeb2c43ad3da071e1306958f4.jpg)  
Figure 7. Level of the bias in recommendations with respect to changing consumer search costs (with critical values $c_{0}=0.245$ , $c_{1}=1.333$ and $c_{2}=1.608$ ) where t=5.1, V=2, r=0.2, y=0.45, and $\beta=0.5$ .

\- PROPOSITION 5 (Impact of search costs on profit and consumer surplus): When the consumer search costs decrease:

(a) the firm's profit decreases and consumer surplus increases when search costs are small ( $c_0 < c \leq c_1$ );

(b) the firm's profit weakly increases and consumer surplus can decrease when search costs are moderate ( $c_{1} < c < c_{2}$ ).

The common wisdom is that decreasing consumer search costs benefits consumers but hurts the firm since consumers are more likely to search instead of accepting the recommendation. On the contrary, we find that this can be reversed: the firm may benefit but consumers can be adversely affected due to a decrease in search costs when search costs are moderate. More significantly, Proposition 5 suggests the power dynamics between the firm and consumers shifts when search costs decrease: the firm may benefit at the expense of the consumers when search costs are moderate, whereas the consumers benefit at the expense of the firm when search costs are low.

First, we explain the effects of search costs on the firm's profit. Changes in the search costs have a direct impact on consumers' responses to product recommendation, and in turn have an indirect effect on the firm's recommendation strategy. When search costs are small, the firm is adversely affected by a decrease in search costs, as more consumers will reject the firm's recommendations and search. However, when search costs are moderate, the dynamic is different, as some consumers choose to leave the website without consuming a product. When search costs decrease, fewer consumers will leave the website. This leads to an increase in profit and weakens the market share maximizing force, which drives the firm to recommend $H$ to more consumers, causing a further increase in profit. The direct and the indirect impacts of changing search costs lead to the non-monotonic effect of search costs on the firm's profit.

![](/api/attachments/7HWTM4BS/fulltext/images/5a29de5f7ad2e663dcf9b0816f8b707bc56274c489f829c7c60a9ef0312f2a9f.jpg)

![](/api/attachments/7HWTM4BS/fulltext/images/3304a73c98b40b7d37090400ddb1fa0fb982af595377e08bb351ec48ad9beda1.jpg)  
Figure 8. a) Profit and b) consumer surplus with respect to changing search costs (with critical values $c_{0}=0.245$ , $c_{1}=1.333$ and $c_{2}=1.608$ ) where t=5.1, V=2, r=0.2, y=0.56, and $\beta=0.5$ .

Second, the direct and the indirect impacts of changing search costs also affect the consumers. When search costs are moderate, lowering the search costs entices more consumers to search, and fewer consumers leave without consuming a product. This increases consumer surplus. However, having fewer consumers leaving the website leads to the firm's recommending $H$ to more consumers, hurting their utility. This lowers consumer surplus. Figure 8a and 8b show that the expected profit increases but consumer surplus decrease with decreasing search costs when search costs are moderate. Moreover, we show that reducing consumer search costs can lead to a zero-sum game situation where the firm benefits in the expense of consumers when the search costs are moderate. Furthermore, the firm has a minimal amount of incentive to reduce the consumer search costs, though it benefits consumers, when the search costs are small. This result highlights that the firm and consumers may never agree on the provisioning of online search tools that reduces the consumers' search costs.

Much of the consumer search literature finds that decreasing search costs positively affects consumers while hurting firms. The key difference between our paper and the extant literature is the interaction between recommendations and search costs. An increase in search costs reduces competition in Bakos $[4]$ , whereas in our paper, the firm can change its strategy to recommend a lower profit margin product to more consumers to keep them from leaving the website when search costs are moderate. This benefits the consumers but reduces the firm's profit. Branco et al. $[8]$ show that when search costs increase, consumers' willingness to pay can decrease. This can lead the firm to decrease its price, causing consumer surplus to increase. In contrast, in our paper, search costs affect the firm's recommendation strategy, and the increase in consumer surplus is due to a decrease in total consumer search and misfit costs stemming from changes in the firm's recommendation strategy. Moreover, the nonmonotonic effect of search costs on the firm's profit, that is the profit first increases and then decreases as the search costs reduces (c decreases) suggests that an optimal level of search costs could exist for the firm in the presence of recommendation system.

## Modeling Extensions

## Extension 1: Multiple Periods

In the main model, consumers come to the firm's website for one period. In this extension, consumers come to the firm's website for multiple periods. In the first period, some consumers consume the recommended product without searching for the non-recommended product. In this case, the consumers know only the exact location of the recommended product and make the same consumption decision in the subsequent periods. If a consumer does not consume the recommendation, she will either search for the nonrecommended product or leave. In the subsequent periods, she does not gain any information about product location from recommendation, since she already knew the locations of the two products, or she already left. This means that consumers' consumption decisions remain the same in the following periods as in the first period. Consumers only need to search, if they choose to, in the first period, whereas they derive the utility of consuming the same product in multiple periods. Effectively, compared to the main model, the search costs reduce (on a per period basis) in the multiple-period setting. Having more periods means more reduction of the search costs.

Reducing the search costs leads to changes in the firm's bias in recommendation strategy. Based on Proposition 4, the effects of reducing search cost can lead to an increase or a decrease in bias. If the search costs are low in the main model, then the bias is lower when there are multiple periods. Nonetheless, the bias can be higher or lower in the case where there are multiple periods than that in the main model, if the search costs are large or moderate in the main model. If it is less likely for a consumer to leave the website without a search in the multiple-period setting than in the main model, then the risk for the firm to lose the profit margin by recommending the high profit-margin product over the low profit-margin product is lower. In this case, the level of bias is higher when there are multiple periods than in the main model.

## Extension 2: Multiple Products

In the main model, the firm has two products available on the website. In Extension 2, the firm has multiple (more than two) products. First, we start with the case where the firm has three products that are located on the circle. When the firm recommends one of the products to a consumer, the consumer realizes the location of the recommended product. However, the consumers are still uncertain about the locations of the other two non-recommended products. Specifically, they know with $\beta$ probability that each of the other two products are located $1/3$ distance from the recommended products, but they don't know which one is at the right and which one is on the left, and with $(1 - \beta)$ probability the other two products can be anywhere on the circle. Moreover, when consumers make the first search, then they learn one product's location and may end up searching again to discover the location of the third product. To compare with the main model of two products (under which, consumers at most search once), consumers could make one more search. Therefore, we would expect the presence of more than two products leads to more product search than in the case where are two products. Because search is costly, more product search means consumers incur higher search costs than the main model. More products on the website means higher consumer search costs.

Increasing the search costs lead to changes in the firm's bias in recommendation strategy. Based on Proposition 4, the effects of higher search costs can lead to an increase or a decrease in bias. If the search costs are moderate in the main model, then the bias is lower when there are multiple products. Nonetheless, the bias can be higher or lower in the case where there are multiple products than that in the main model, if the search costs are small in the main model. If it is more likely for a consumer to consume the recommended product without a search in the multiple-product setting than in the main model due to increasing search costs, then the firm has higher an incentive to recommend the high profit-margin product over the low profit-margin product. In this case, the level of bias is higher when there are multiple products than in the main model.

## Discussion and Conclusion

Using an analytical model incorporating the level of the firm's uncertainty about consumer preferences, we find that the firm has an incentive to make biased recommendations to direct consumers to the product that yields a higher profit margin. One key result is that, contrary to expectations, the level of bias in recommendations can decrease when the firm's uncertainty about consumer locations decreases. The firm's uncertainty about consumer locations can decrease if it is able to gather more data about consumer browsing or purchase behavior or by collecting information on their income and total spending. It is important to note that this reduction in bias occurs when search costs are low for consumers. When consumers have the ability to search for alternatives on their own, the firm is better incentivized to make unbiased recommendations. We also find that consumer surplus can increase when the firm manages to reduce uncertainty about consumers and can better target consumer product preferences via product recommendations. Thus, this is not a zero-sum game and it is possible for both the firm and the consumers to benefit from greater data sharing. This may explain why readers of USA Today receive relevant recommendations for online news articles and users of Netflix receive satisfactory recommendations for movies.

The effects of the firm's uncertainty about consumers on consumer surplus raise concerns about the extent of data gathering about users. Regulations such as Europe's General Data Protection Regulation (GDPR) protect user data and privacy and make it more difficult for firms to gain precise information about consumers. Our result about the positive effects of reducing uncertainty about consumers on consumer surplus highlights that indiscriminately restricting the use of consumer data could thwart opportunities to provide greater benefit to consumers. This implies that the regulations and policies that specify limits to the use of consumer data should be crafted carefully.

Our paper offers insights for online firms that provide personalized recommendations and search tools to users. The results showing that the level of bias in recommendations depends on search costs highlight the interactive relationship between search costs and recommendation strategy. The effect of search costs on the level of bias is nonmonotone implying that firms need to adjust their recommendation strategy with changes in search costs (e.g., due to improving search technology).

Our model has some limitations. First, we assume a symmetric case about products that consumers have the same valuation for both products (same V). Analysis of the asymmetric cases could highlight additional forces that the firm needs to consider in its personalized recommendation strategy. Second, we assume that consumers must assess the product before consuming the product. It is an interesting future research question to endogenize consumers' assessment decision. Future research can also consider product popularity in the firm's recommendation strategy or heterogeneity in the popularity of different products. Future research can also focus on the impact of recommendation systems on product diversity with respect to search costs and precision.

## Notes

For example, products may be sourced from different suppliers. In the case of online media streaming, Netflix and Spotify pay different royalties to content production studios. It has been reported that Netflix pays a large amount of royalties to third-party content providers. In contrast, Netflix pays smaller royalties to studios for its own original programming. In addition, providers such as Netflix pay for the Internet bandwidth and server capacity that support streaming services on their platforms. For example, Netflix may incur a higher cost to support the streaming of high definition (HD) content of a longer duration than that of non-HD content of a shorter duration. Moreover, YouTube and USA Today generate revenue from advertisements that are displayed on their platforms, and the advertising revenue depends on the rating and number of views.

2 For example, customers of Netflix often receive emails from Netflix which include recommendations for content that they have not viewed yet. This saves time and effort for customers. Furthermore, consumers would still need to assess the product location (e.g., examining the product information, regardless of the product being recommended or not recommended by the firm before consumption).

3 Consumers incur both costs if they search for the non-recommended product. This is consistent with Fleder and Hosanagar [13, p. 706], who argue that recommendation systems facilitate “the ease of clicking a recommended item versus continuing to search through a firm’s website.”

4 The non-zero cost of assessing both products would increase the relative attractiveness of the outside option without affecting the relative attractiveness of recommendation versus search. Since we already define V as the relative attractiveness of the product for the outside option, this assumption does not change our results.

## Acknowledgments

We thank the Guest Editors, Rob Kauffman and Atanu Lahiri, for their constructive comments and guidance throughout the review process.

## Notes on contributors

Vidyanand Choudhary (VeeCee@uci.edu) is a professor at the Paul Merage School of Business, University of California, Irvine and a Senior Editor of Production and Operations Management. Previously, he served as the Associate Dean for Undergraduate programs and Senior Associate Dean at the Merage School. He conducts research in the area of Economics of Information Systems. His research has been published in various journals such as Management Science and Information Systems Research.

Zhe (James) Zhang (jameszhangzhe@utdallas.edu; corresponding author) is an associate professor of Information Systems in the Naveen Jindal School of Management at the University of Texas at Dallas. He studies how IT and the Internet have digitally transformed products and markets, and how firms should respond to this paradigm shift. His papers have been published in various journals such as Information Systems Research, MIS Quarterly, and Production and Operations Management.

## References

1. Adomavicius, G.; and Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 17, 6 (2005), 734–749.

2. Adomavicius, G.; Bockstedt, J.; Curley, S. P.; Zhang, J.; and Ransbotham, S. The hidden side effects of recommendation systems. MIT Sloan Management Review, 60, 2 (2019), 13–15.

3. Anderson, C. The Long Tail: Why the Future of Business Is Selling Less of More. New York: Hyperion Books, 2008.

4. Bakos, J.Y. Reducing buyer search costs: Implications for electronic marketplaces. Management Science, 43, 12 (1997), 1676–1692.

5. Barnett, E. Google warned by EU's antitrust inquiry of “search manipulation concerns.” The Telegraph, (2012). https://www.telegraph.co.uk/technology/google/9281639/Google-warned-by-EUs-antitrust-inquiry-of-search-manipulation-concerns.html (accessed on February 26, 2023).

6. Bodapati, A. Recommendation systems with purchase data. Journal of Marketing Research, 45, 1 (2008), 77–93.

7. Bourreau, M.; and Gaudin, G. Streaming platform and strategic recommendation bias. Journal of Economics & Management Strategy, 31, 1 (2022), 25–47.

8. Branco, F.; Sun, M.; and Villas-Boas, J. M. Optimal search for product information. Management Science, 58, 11 (2012), 2037–2056.

9. Brynjolfsson, E.; and Smith, M.D. Frictionless commerce? A comparison of Internet and conventional firms. Management Science, 46, 4 (2000), 563–585.

10. Carr, D. Giving viewers what they want. The New York Times, (2013). https://www.nytimes.com/2013/02/25/business/media/for-house-of-cards-using-big-data-to-guarantee-its-popularity.html (accessed on February 26, 2023).

11. De Corniere, A.; and Taylor, G. Integration and search engine bias. The RAND Journal of Economics, 45, 3 (2014), 576–597.

12. Dukes, A.; and Liu, L. Online shopping intermediaries: The strategic design of search environments. Management Science, 62, 4 (2016), 1064–1077.

13. Fleder, D.; and Hosanagar, K. Blockbuster culture's next rise or fall: The impact of recommender systems on sales diversity. Management Science, 55, 5 (2009), 697–712.

14. Ghoshal, A.; Kumar, S.; and Mookerjee, V. Impact of recommender system on competition between personalizing and non-personalizing firms. Journal of Management Information Systems, 31, 4 (2015), 243–277.

15. Ghoshal, A.; Menon, S.; and Sarkar, S. Recommendations using information from multiple association rules: A probabilistic approach. Information Systems Research, 26, 3 (2015), 532–551.

16. Ghoshal, A.; Mookerjee, V.; and Sarkar, S. Recommendations and cross-selling: Pricing strategies when personalizing firms cross-sell. Journal of Management Information Systems, 38, 2 (2021), 430–456.

17. Guo, J.; Zhang, W.; Fan, W.; and Li, W. Combining geographical and social influences with deep learning for personalized point-of-interest recommendation. Journal of Management Information Systems, 35, 4 (2018), 1121–1153.

18. Hagiu, A.; and Jullien, B. Why do intermediaries divert search? The RAND Journal of Economics, 42, 2 (2011), 337–362.

19. Hagiu, A.; and Jullien, B. Search diversion and platform competition. International Journal of Industrial Organization, 33 (2014), 48–60.

20. Häubl, G.; and Trifts, V. Consumer decision making in online shopping environments: The effects of interactive decision aids. Marketing Science, 19, 1 (2000), 4–21.

21. Hosanagar, K.; Fleder, D.; Lee, D.; and Buja, A. Will the global village fracture into tribes? Recommender systems and their effects on consumer fragmentation. Management Science, 60, 4 (2014), 805–823.

22. Johar, M.; Mookerjee, V.; and Sarkar, S. Selling vs. profiling: Optimizing the offer set in web-based personalization. Information Systems Research, 25, 2 (2014), 285–306.

23. Kanter, J. Yelp joins critics of European Union antitrust settlement with Google. The New York Times (2014). https://www.nytimes.com/2014/07/09/technology/yelp-joins-critics-of-european-union-settlement-with-google.html (accessed on February 26, 2023).

24. Kim, J.B.; Albuquerque, P.; and Bronnenberg, B. J. Online demand under limited consumer search. Marketing Science, 29, 6 (2010), 1001–1023.

25. Konstan, J.A.; Miller, B.N.; Maltz, D.; Herlocker, J.L.; Gordon, L.R.; and Riedl, J. GroupLens: Applying collaborative filtering to Usenet News. Communications of the ACM, 40, 3 (1997), 77–87.

26. Kuksov, D.; and Villas-Boas, J.M. When more alternatives lead to less choice. Marketing Science, 29, 3 (2010), 507–524.

27. Li, L.; Chen, J.; and Raghunathan, S. Recommender system rethink: Implications for an electronic marketplace with competing manufacturers. Information Systems Research, 29, 4 (2018), 1003–1023.

28. Li, L.; Chen, J.; and Raghunathan, S. Informative role of recommender systems in electronic marketplaces: A boon or a bane for competing sellers. MIS Quarterly, 44, 4 (2020), 1957–1985.

29. Liang, T.; Lai, H.; and Ku, Y. Personalized content recommendation and user satisfaction: Theoretical synthesis and empirical findings. Journal of Management Information Systems, 23, 3 (2006), 45–70.

30. Linden, G.; Smith, B.; and York, J. Amazon. com recommendations: Item-to-item collaborative filtering. IEEE Internet Computing, 7, 1 (2003), 76–80.

31. Mangalindan, J.P. Amazon's recommendation secret. Fortune (2012). https://fortune.com/2012/07/30/amazons-recommendation-secret/ (accessed on February 26, 2023).

32. McNee, S. M.; Albert, I.; Cosley, D.; Gopalkrishnan, P.; Lam, S.K.; Rashid, A.M.; and Riedl, J. On the recommending of citations for research papers. Proceedings of the 2002 ACM Conference on Computer Supported Cooperative Work, (2002), 116–125.

33. Moorthy, S.; Ratchford, B.T.; and Talukdar, D. Consumer information search revisited: Theory and empirical analysis. Journal of Consumer Research, 23, 4 (1997), 263–277.

34. Moraga-González, J.L.; Sándor, Z.; and Wildenbeest, M.R. Prices and heterogeneous search costs. The RAND Journal of Economics, 48, 1 (2017), 125–146.

35. Murthi, B.P.S.; and Sarkar, S. The role of the management sciences in research on personalization. Management Science, 49, 10 (2003), 1344–1362.

36. Oestreicher-Singer, G.; and Sundararajan, A. Recommendation networks and the long tail of electronic commerce. MIS Quarterly, 36, 1 (2012), 65–83.

37. Pathak, B.; Garfinkel, R.; Gopal, R.D.; Venkatesan, R.; and Yin, F. Empirical analysis of the impact of recommender systems on sales. Journal of Management Information Systems, 27, 2 (2010), 159–188.

38. Salop, S.C. Monopolistic competition with outside goods. The Bell Journal of Economics, 10, 1 (1979), 141–156.

39. Senecal, S.; and Nantel, J. The influence of online product recommendations on consumers' online choices. Journal of Retailing, 80, 2 (2004), 159–169.

40. Stigler, G.J. The economics of information. Journal of Political Economy, 69, 3 (1961), 213–225.

41. Takács, G.; Pilászy, I.; Németh, B.; and Tikk, D. Matrix factorization and neighbor-based algorithms for the Netflix Prize problem. Proceedings of the 2008 ACM Conference on Recommender Systems, (2008), pp. 267–274.

42. Tam, K.Y.; and Ho, S.Y. Understanding the impact of web personalization on user information processing and decision outcomes. MIS Quarterly, 30, 4 (2006), 865–890.

43. Weitzman, M.L. Optimal search for the best alternative. Econometrica: Journal of the Econometric Society, (1979), 641–654.

## Appendix

Table A1. Table of notation.

<table><tr><td>Notation</td><td>Definition</td><td>Comments</td></tr><tr><td>x</td><td>Consumer locations.</td><td>Consumers&#x27; locations represent their preferences for products</td></tr><tr><td> $\eta_{H}, \eta_{L}$ </td><td>Product profit margins.</td><td>Product H is more profitable than Product L.</td></tr><tr><td>V</td><td>Consumers&#x27; value of the product relative to the outside option.</td><td>A consumer&#x27;s utility of a product is V if the consumer and the product are in the same location.</td></tr><tr><td>t</td><td>Consumer&#x27;s misfit cost parameter.</td><td>Consumer&#x27;s misfit cost increases when t increases.</td></tr><tr><td>β</td><td>Consumers&#x27; belief about the product locations.</td><td>Consumers believe that with a certain probability β, the two products are located equidistantly on the circle, and with a probability (1-β), they could be anywhere on the circle (equally likely to be anywhere on the circle).</td></tr><tr><td>c</td><td>Consumers&#x27; search costs.</td><td>A consumer incurs costs of identifying the product and assessing the product if he searches for a product and finds out its location after rejecting the firm&#x27;s recommendation.</td></tr><tr><td>r</td><td>The width of the consumer bucket.</td><td>The parameter r represents the range of possible locations for the consumer. This also represents the level of the firm&#x27;s uncertainty about consumers&#x27; location. In a limiting case, where r=0, the firm knows consumers&#x27; exact locations.</td></tr><tr><td>b</td><td>The center of the consumer bucket.</td><td>We use parameter b to refer to a consumer&#x27;s bucket.</td></tr><tr><td>s</td><td>The firm&#x27;s product recommendations to individual consumers.</td><td>If s=H, then the firm recommends H; and if s=L, then the firm recommends L.</td></tr><tr><td>E( $\pi_{b}(s)$ )</td><td>The firm&#x27;s expected profit from recommending product s to a consumer in a bucket centered at b.</td><td>The expected profit takes into consideration the probabilities of the consumer accepting and consuming the recommended product s, leaving the website, and consuming the other product after the search; and the profit margins of the consumed products.</td></tr><tr><td>E( $CS_{b}(s)$ )</td><td>The expected surplus of a consumer bucket centered at b with a product recommendation of s.</td><td>The expected surplus takes into consideration the probabilities of the consumer accepting and consuming the recommended product s, leaving the website, and consuming the other product after the search; and the consumer utility from each of these responses.</td></tr><tr><td>E(π)</td><td>The firm&#x27;s expected total profit from providing personalized recommendations to individual consumers.</td><td></td></tr><tr><td>E(CS)</td><td>Consumer surplus following the firm&#x27;s recommendation strategy.</td><td></td></tr><tr><td>Bias</td><td>The level of bias in recommendations following firm&#x27;s recommendation strategy.</td><td>Level of bias measures the number of consumers who are closer to H but receive product recommendations of L, or consumers who are closer to L but receive product recommendation of H.</td></tr></table>
