---
otero_id: 4682
otero_key: "JTETNB6S"
title: "Impact of Recommender System on Competition Between Personalizing and Non-Personalizing Firms"
authors: "Abhijeet Ghoshal; Subodha Kumar; Vijay Mookerjee"
year: "2015"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2014.1001276"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Impact of Recommender System on Competition Between Personalizing and Non-Personalizing Firms

Abhijeet Ghoshal, Subodha Kumar & Vijay Mookerjee

To cite this article: Abhijeet Ghoshal, Subodha Kumar & Vijay Mookerjee (2015) Impact of Recommender System on Competition Between Personalizing and Non-Personalizing Firms, Journal of Management Information Systems, 31:4, 243-277, DOI: 10.1080/07421222.2014.1001276

To link to this article: http://dx.doi.org/10.1080/07421222.2014.1001276

![](/api/attachments/JTETNB6S/fulltext/images/0c577a7abd539fd313d25c61022b95459363abf895ebd4ffbf9438af24b4dd6f.jpg)

Published online: 15 Apr 2015.

![](/api/attachments/JTETNB6S/fulltext/images/a1119a140c818087f70bed450ec5527879b5c442c886ea1f8a76a547f0ce3fd2.jpg)

Submit your article to this journal

![](/api/attachments/JTETNB6S/fulltext/images/7b266b241022e66a62e28a6346e55a2327507de7e530e29cabb8f568d3def184.jpg)

Article views: 68

![](/api/attachments/JTETNB6S/fulltext/images/3b16f833fa8cb98b5ca441dffaaf8a599a18d2899b03e933c294287f47a7fea3.jpg)

View related articles

![](/api/attachments/JTETNB6S/fulltext/images/6ef600a95db4830a1bf2db232b6388de7cbe9d2e032054347d88864207a3e650.jpg)

View Crossmark data

# Impact of Recommender System on Competition Between Personalizing and Non-Personalizing Firms

ABHIJEET GHOSHAL, SUBODHA KUMAR, AND VIJAY MOOKERJEE

ABHIJEET GHOSHAL is a postdoctoral research associate in the Department of Business Administration, University of Illinois-Urbana Champaign. He received his Ph.D. from the University of Texas at Dallas. His research interests include operational and economic issues related to recommender systems. His work has appeared in INFORMS Journal on Computing.

SUBODHA KUMAR is the Carol and G. David Van Houten, Jr. ’71 Professor at the Mays Business School, Texas A&M University. He received his Ph.D. from the University of Texas at Dallas. His research interests include quantitative methods and supply chain management. His papers have appeared in a number of journals, including Management Science, Operations Research, Information Systems Research, Journal of Management Information Systems, Production and Operations Management, IIE Transactions, Decision Sciences, IEEE Transactions on Knowledge and Data Engineering, European Journal of Operational Research, and others. He is deputy editor and a department editor of Production and Operations Management, a senior editor of Decision Sciences, an associate editor of Information Systems Research, and serves on the editorial boards of Journal of Database Management and International Journal of Social and Organizational Dynamics in IT.

VIJAY MOOKERJEE is the Charles and Nancy Davidson Chair in Information Systems at the Naveen Jindal School of Management, University of Texas at Dallas. He received his Ph.D. in management with a major in management information systems from Purdue University. His research interests include social networks, managerial issues in information security, optimal software development methodologies, storage and cache management, content delivery systems, and the economic design of expert systems and machine learning systems. He is senior editor of Information Systems Research. He serves as an associate editor of several leading journals, including Decision Support Systems, Management Science, INFORMS Journal on Computing, Information Technology and Management, and Journal of Data Management. He has published in several journals in the areas of information systems, computer science, and operations research.

ABSTRACT: How do recommender systems affect prices and profits of firms under competition? To explore this question, we model the strategic behavior of customers who make repeated purchases at two competing firms: one that provides personalized recommendations and another that does not. When a customer intends to purchase a product, she obtains recommendations from the personalizing firm and uses this recommendation to eventually purchase from one of the firms. The personalizing firm profiles the customer (based on past purchases) to recommend products. Hence, if a customer purchases less frequently from the personalizing firm, the recommendations made to her become less relevant. While considering the impact on the quality of recommendations received, a customer must balance two opposing forces: (1) the lower price charged by the non-personalizing firm, and (2) an additional fit cost incurred when purchasing from the non-personalizing firm and the increased cost due to recommendations of reduced quality in the future. An outcome of the analysis is that the customers should distribute their purchases across both firms to maximize surplus over a planning horizon. Anticipating this response, the firms simultaneously choose prices. We study the sensitivity of the equilibrium prices and profits of the firms with respect to the effectiveness of the recommender system and the profile deterioration rate. We also analyze some interesting variants of the base model in order to study how its key results could be influenced. One of the key takeaways of this research is that the recommender system can influence the price and profit of not only the personalizing firm but also the non-personalizing firm.

KEY WORDS AND PHRASES: recommender systems, duopoly, pricing, dynamic optimization, online competition, Nash equilibrium.

The value of commerce through online shopping has increased dramatically in the past decade. In 2013, U.S. retail e-commerce sales grew by 16.9 percent to reach \$263.3 billion, and accounted for 5.8 percent of total retail sales [50]. Retailing firms with an online storefront often employ recommender systems to provide personalized recommendations to customers (hereafter referred to as personalizing firms) [1, 15, 49]. Some prominent examples of personalizing firms are Amazon.com, Target, Costco, and Home Depot. In 2007, 41 percent of electronic retailers were found to provide personalized services, a value that is estimated to increase over time [28].

Fit costs are often incurred when a large number of items are being sold and the customer cannot evaluate all these items to purchase her ideal product. Recommender systems help consumers quickly to learn about the products that are likely to be ideal for them [21, 34, 40]. Typically, these systems gather knowledge on customer preferences through data collected about them (such as demographics and psychographics) and their past online transactions. Based on this knowledge, recommender systems predict the needs of customers in order to recommend items that best match their current preferences [13, 22, 42]. In other words, the main goal of a recommender system is to help a customer find the item she wishes to purchase and thereby lower the fit cost associated with the purchase. Here, the predictive knowledge gleaned about a customer’s preferences is referred to as the customer’s profile. The profile, for instance, consists of known characteristics of the customer as well as several unknown characteristics that are estimated using the known characteristics and the previous transactions of the customer. Reducing the noise associated with these estimates corresponds to improving the quality of the profile.

Despite their recognized benefits, recommender systems are not always viable for small to medium-sized firms because of the high costs associated with their implementation and use [26]. Hence, many less prominent electronic retailers still sell products without providing personalization services (hereafter referred to as nonpersonalizing firms). For example, the online bookseller Buybooksontheweb.com does not provide personalization services to its customers. Similarly, while iTunes provides personalized recommendations (through their “ Genius” toolbar) for music items, another online firm iomoio.com sells music without doing so. Likewise, movies can be purchased from Amazon (where personalized recommendations are provided) or from fullmovies.com (where recommendation is not provided).

Given that a customer has two choices (a personalizing firm and a non-personalizing firm) to purchase products, it is always beneficial for her to first visit the personalizing firm and use the recommendations provided to her to purchase products from one of the two firms. She can identify a preferred product (among the recommended ones) and decide to purchase that product from the personalizing firm or a similar product from the non-personalizing firm. Such behavior has been reported in the retailing context where customers obtain recommendations from Amazon.com, but use these recommendations to purchase similar products from another firm [7].

Firms that provide differentiated services often charge a price premium [37, 38, 44]. Hence, the prices at the personalizing firms are typically higher [32].<sup>1</sup> However, as discussed earlier, the recommendations are based on the profile quality of the customer, which depends on the transaction history of the customer with the personalizing firm. Hence, if the customer purchases from the non-personalizing firm, the personalizing firm loses the opportunity to improve the customer’s profile. As a result, the usefulness of the future recommendations for the customer may decrease. Thus, in spite of lower prices, the customer may not always purchase from the non-personalizing firm, and instead distribute her purchases across the two firms. Several empirical studies have provided evidence for such behavior by customers where they forgo cheaper products and purchase from the personalizing firm to let the recommender system learn their preferences [37, 44]. Managers and analysts also confirm that today’s customers behave in this manner [53]. Furthermore, the elite firms like Amazon.com inform customers that the quality of their future recommendations improve as they purchase more from the firm [4]. Along these lines, researchers have also noted that customers are aware of this advantage [25].

Based on the above discussion, the basic setting of our problem is as follows. The customer first visits the personalizing firm and uses the firm’s recommendations to find her preferred product. Then, she purchase either the preferred product from the personalizing firm or its substitute from the non-personalizing firm. We allow for the fact that a customer may not be able to find her ideal product at either firm [8]. Instead, the product comes with a fit cost at both firms. Further, the product purchased from the non-personalizing firm may not be exactly the same as her preferred product. Additionally, the customer may need to spend some extra effort to search for a substitute at the non-personalizing firm.

Hence, the customer often incurs an additional cost when purchasing from the non-personalizing firm. Also, as discussed earlier, when the customer purchases from the non-personalizing firm, the personalizing firm loses the information about the customer’s preferences. This may lead to increased fit cost in the future. Hence, while purchasing from the non-personalizing firm, the customer faces a trade-off between increased fit costs for future purchases and the current lower price of the product (net of additional cost). Thus, the optimal strategy for the customer is to distribute her purchases across the two firms, rather than purchasing exclusively from one of the firms. Anticipating the purchase behavior of customers, the two firms engage in a simultaneous move price game.

The fact that the customer may distribute her purchases across the two firms is a consequence of the dynamic nature of the profile. When customer preferences change with time, the profile deteriorates if the opportunity to observe the change is lost by the personalizing firm. On the other hand, the profile improves when the customer purchases at the personalizing firm. The analysis of the problem therefore necessitates a model that can suitably capture the dynamic nature of the phenomenon, that is, the profile can change (improve or deteriorate) with time depending on the manner in which the customer chooses to allocate her purchases across the two firms. First, we consider that the customer does not change the fraction of purchases made at the two firms. Later, we analyze a case in which the customer is able to change her purchase fractions over time. In this case, we use optimal control theory to solve the customer’s dynamic optimization problem (e.g., [18, 20, 31]). Furthermore, in both cases, the solution of the customer’s problem is an input to a static price game between the two firms.

Our analysis in this study provides insights into several questions of managerial interest. With an improvement in the recommender system, customers can shift more of their purchases toward the non-personalizing firm because they can maintain the same profile quality with fewer purchases at the personalizing firm. Thus, the personalizing firm may lose some demand as a result of an improved recommender system. A natural question arises: should the personalizing firm improve its recommender system, and if so, how will this improvement affect the prices charged by the two firms? A related question is: how should the non-personalizing firm react (with respect to its pricing decision) when the recommender system (at the personalizing firm) improves? Also, what happens to the customer’s surplus? By improving its recommender system, the personalizing firm can command higher prices to extract part of the customer’s surplus. Does that reduce the customer’s surplus? Can the customer increase her surplus by being more strategic (i.e., by changing the fractions of her purchases from the two firms with time)?

Another issue of interest is the impact of changing customer preferences: if the preferences change rapidly, how will the prices in the market be affected? A rapid change in customer preferences can be expected to cause the customer to purchase more at the personalizing firm, implying that the personalizing firm should always prefer changing customer preferences. Our analysis reveals that this is not always the case.

## Literature Review

We review the literature in the following streams that are related to our study: (1) personalization and recommender systems, (2) loyalty rewards, and (3) product customization. In this section, we also differentiate our work from past literature and highlight our contributions.

## Personalization and Recommender Systems

Clearly, this stream of research is closely related to our study. Personalization has been an active area of research for more than a decade. For detailed reviews on personalization, see Adomavicius and Tuzhilin [2] and Breese et al. [12]. The studies on personalization mainly analyze the factors that impact the profile qualities of customers and present methodologies for improving the recommender system. However, similar to our study, some researchers have focused on the impact of recommender systems on the search and purchase behavior of customers [e.g., see 11]. In a similar direction, Fleder et al. [17] and Park and Han [39] analyze the effect of recommender systems on diversity of sales. However, in these studies, the question has rarely been: should an existing recommender system be improved? In the current study, we answer this question by exploring changes in the profits and prices of firms with improvement in the recommender system.

A few papers in this stream analyze the interaction between the recommender system and the price charged by the firm, a setup very similar to our research. For example, Aron et al. [5] explore the trade-off between better customization and better prices. In spite of some similarities, our work is very different from that of Aron et al. [5]. First of all, unlike out work, Aron et al. consider a monopolistic firm. Hence, the notion of learning about a preferred product at the personalizing firm and purchasing a similar product from the non-personalizing firm is missing in Aron et al., but is the focus of our study. Second, the customer chooses the customization level in Aron et al. whereas the recommendation quality is endogenous in our model. In a slightly different vein, Nikolaeva and Sriram [36] examine the behavioral aspect of improving the recommendation agent–consumer relationship, utilizing a model of internal information search for unplanned purchases prompted by a recommendation from a collaborative filtering agent. Clearly, this study is different from our research, insofar as we focus on the pricing strategies of the firms when one of the firms provides recommendations using the information from customers’ profiles.

Further, similar to our study, Bergemann and Ozmen [9] and Ozmen [37] consider settings with both personalizing and non-personalizing firms. In their studies, customers are differentiated in two dimensions—the type of product they prefer and flexibility in terms of their choices (i.e., are they rigid or flexible in preferences for their preferred product?). The problem they analyze is how the market is segmented between types of customers (differentiated in the above two dimensions) with an improved recommender system. In our research, however, we consider the impact of profile quality on a customer’s decision to purchase from the two firms. Therefore, the basic setup and the goal of our research differ from that of Bergemann and Ozmen [9] and Ozmen [37]. Finally, Wattal et al. [52] analyze under what conditions the personalization service and product quality are complementary when the personalizing firm competes with a non-personalizing firm. In contrast, we consider that the customer may use the personalizing firm’s recommendation to identify her preferred product and purchase a similar product from the non-personalizing firm.

## Loyalty Rewards

At a conceptual level, loyalty programs are similar to recommendation systems: both provide immediate value to the customer and both can grow with increased patronage. In this domain, Biyalogorsky et al. [10] examine how a firm should strike a balance between loyalty rewards and attractive prices to maximize profit. Lewis [27] provides a framework to measure the influence of loyalty reward programs on consumer retention, whereas Meyer-Waarden [30] studies how loyalty programs induce customers to continue purchasing from the firm. Unlike rewards, however, recommendations are transferable, that is, the customer can use the recommendations provided by a personalizing firm to find similar products at other firms. In addition, unlike rewards, the recommendation quality decreases if fewer purchases are made at the personalizing firm. This happens because a customer’s preferences are usually not static and they change with time.

## Product Customization

The literature on product customization examines the pricing strategies of firms when they offer products that are customized to meet the needs of individual customers. Customization is conceptually similar to personalization in the sense that both customized and personalized products better meet a custmoer’s preferences. In this domain, Dewan et al. [16] study competition between two customizing firms to derive equilibrium prices. Syam et al. [47] also investigate a duopoly in which firms decide whether to customize or not, and if so, how much to customize. Interestingly, they find that both firms should customize on the same product attributes and provide standard features on other attributes. Further, Syam and Kumar [48] find that the firms should offer both standard and customized products to maximize profit. Mendelson et al. [29] also consider two firms—a mass customizing firm that provides products with some delay, and a standard firm that provides standard products without delay. In all these studies, customization is considered in a static sense and its benefits do not depend on a customer’s past purchases at a customizing firm. In addition, unlike recommendations, customers have no way to transfer customization benefits from one firm to another.

## Model and the Solution

In this section, we begin with the customer’s problem, and then study a pricing game between the two firms.

## Customer’s Optimization Problem

We consider a model where the customers purchase products from two competing firms (a non-personalizing firm and a personalizing firm) over a period of time. The customer can either buy the recommended product from the personalizing firm or its close substitute from the non-personalizing firm. Thus, out of all the purchases during the planning horizon (which is normalized to 1), the customer chooses to complete an optimal fraction (<sup>u</sup>) of purchases at the personalizing firm and the remaining fraction $( 1 - u )$ at the non-personalizing firm.

The products purchased by the customer (from either firm) are considered to belong to the same category. Also, the price charged by each firm is considered to be the same across different products in the category. Whereas the prices within a product category may vary slightly, we assume that we are dealing with a product category in which this variation is not substantial and the single-price approximation is reasonable. In practice, several products (such as music items, movies, month’s supply of cosmetics, food supplies, and pet food) belong to the category where the prices are approximately the same (e.g., almost all songs in iTunes are sold at \$0.99) and customers purchase the product repeatedly.

The customer maximizes her long-run surplus (i.e., the difference between her reservation price and the cost) by distributing purchases across the two firms. We next discuss the components of the cost.

## Costs Incurred When Purchasing from the Personalizing Firm

As discussed earlier, the customer typically incurs a fit cost when the product purchased (i.e., her preferred product) is not her ideal product. The fit cost is a function of the profile at the time period of purchase (<sup>t</sup>), denoted by $x ( t ) . ^ { 3 } \mathrm { ~ A ~ }$ better profile (higher <sup>x t</sup> ) lowers the fit cost. Harper et al. [19] conduct experiments on real datasets to show that the quality of recommendations increases in a concave manner with an increase in the customer’s transactions. A similar observation is made by Chen et al. [14] who note that recommendations improve as the customer conducts more transactions with the firm. Based on these results, the fit cost $f ( x )$ as a function of the profile is represented as: $f ( x ) = ( A + x ^ { 2 } - B x ) \geq 0$ and $f ^ { ' } ( x ) =$ $( 2 x - B ) < 0$ , where $A ( > 0 )$ is the maximum fit cost incurred by the customer and $B ( > 0 )$ is a cost reduction factor—a higher value of <sup>B</sup> reduces the cost at a higher rate. Thus, the fit cost is decreasing and convex in the profile. Another cost incurred by the customer is, of course, the price paid for the product (denoted by $q _ { 1 } )$ . Overall, the total cost incurred by the customer when purchasing from the personalizing firm is $\left( A + x ^ { 2 } - B x + q _ { 1 } \right)$

## Costs Incurred When Purchasing from the Non-Personalizing Firm

When purchasing from the non-personalizing firm, the customer needs to exert effort in analyzing the products in an attempt to find her preferred product. Hence, there is an additional search cost incurred in purchasing from the non-personalizing firm. Despite this search cost, the customer may not be able to find her preferred product, and may have to choose a substitute. This can happen when (1) assortments of products sold by the two firms are different, or (2) the personalizing firm customizes some products to make them exclusive (i.e., store brands).<sup>4</sup> As a result, the fit cost of the substitute product (at the non-personalizing firm) may be higher than that of her preferred product (at the personalizing firm).

In summary, there are two additional costs in purchasing from the non-personalizing firm: (1) the search cost, and (2) the increased fit cost. We denote the aggregate of these costs as $\gamma ,$ and refer to it simply as the additional fit cost. Therefore, the total cost incurred by the customer when purchasing from the non-personalizing is $\left( A + x ^ { 2 } - B x + \gamma + q _ { 2 } \right)$ , where $q _ { 2 }$ is the price charged by the non-personalizing firm.

Based on the types of products being recommended, the additional fit cost (γ) can be a constant or can be dependent on the profile quality. For instance, when the recommended products have limited features on which personalization can be done, such as regular grocery items and cosmetics, the additional fit cost is not expected to vary considerably with profile quality and can be approximated to be a constant. On the other hand, in the case of music and movies, tastes of users can be very specific, because they can associate their preferences with a significant number of attributes. In such cases, the personalizing firm can use different attributes to make recommendations [24], and therefore the additional fit cost can vary significantly based on the profile quality. For ease of exposition, we first analyze a case in which the additional fit cost is the same for all customers and is independent of the profile quality. Later, we analyze scenarios in which the additional fit cost is different across customers and is dependent on the profile quality.

## Objective Function and State Equation

A customer’s total cost (a rate) at time period <sup>t</sup> can be written as

$$
u \left(A + x (t) ^ {2} - B x (t) + q _ {1}\right) + (1 - u) \left(A + x (t) ^ {2} - B x (t) + \gamma + q _ {2}\right).\tag{1}
$$

This cost includes the costs incurred at both firms. The customer may purchase multiple products in the time period $t ;$ she may purchase some products from the personalizing firm and the rest from the non-personalizing firm. Here, <sup>u</sup> is effectively the average fraction of purchases from the personalizing firm over the planning horizon. In other words, <sup>u</sup> and $( 1 - u )$ are the rates of purchases (i.e., fractions of purchases) per time period <sup>t</sup> from the personalizing firm and the nonpersonalizing firm, respectively. The costs remain approximately the same over the entire planning horizon, and the customer determines <sup>u</sup> beforehand. Thus, the setup of the model is deterministic. The customer knows these cost functions from prior purchase experiences with the firms.

The customer’s objective is to maximize the present value of total surplus over a planning horizon. The rate of surplus is given by the reservation price (<sup>R</sup>) minus the cost. Since the product considered in our model is purchased repeatedly, it is suitable to consider an infinite horizon formulation with a continuous discount rate $r > 0$ Using Equation (1), the customer’s objective is

$$
\begin{array}{l} \max _ {u} \Bigg \{\int_ {0} ^ {\infty} \Big [ R - u (A + x (t) ^ {2} - B x (t) + q _ {1}) \\ \qquad - (1 - u) (A + x (t) ^ {2} - B x (t) + \gamma + q _ {2}) \Big ] e ^ {- r t} d t \Bigg \}. \end{array}\tag{2}
$$

The objective function value of the customer at any instant <sup>t</sup>, and consequently over the horizon, depends on the quality of her profile $( x ( t ) )$ . As discussed earlier, the personalizing firm creates a profile of the customer based on the data collected about her preferences [1]. In order to collect such data, the personalizing firm usually asks a customer to register when she visits the firm for the first time. For instance, Amazon.com asks its customers to register at the time of first purchase. Later, during subsequent purchases, the personalizing firm tracks the purchases of the customer to learn more about her preferences.

When the customer purchases from the personalizing firm, the firm gets an opportunity to improve her profile. Hence, the rate of improvement in the profile depends on the rate of purchase from the personalizing firm (<sup>u</sup>) and the effectiveness of the recommender system. The search and browsing behavior of the customer may also provide some information regarding her preference. However, relative to the purchase behavior, it carries more noise in the information about preferences. For instance, a customer may search a specific product but eventually not purchase it if she finds out that it is not useful to her [3, 35, 46]. Hence, we do not consider the customer’s search behavior. Similarly, we also do not consider those items that the customer usually does not purchase for herself, such as gifts. These occasional purchases can temporarily impact the profile of the customer; however, with subsequent purchases, their impacts on the profile diminish.

On the other hand, some factors can contribute to the deterioration of the profile. Most important, the preferences of the customer can change with time [23, 41, 51]. For example, a freshman entering college may no longer require school textbooks. Similarly, over time, the music tastes of a customer may change, for example, from soft music to rock music. Hence, the customer’s current profile becomes less relevant with time unless the customer continues to patronize the personalizing firm. When a large amount of useful information about the customer is available (i.e., the profile quality is high), pieces of information can become obsolete with the customer’s changing preferences. Hence, the profile deterioration rate is higher when the profile quality is higher. In contrast, when the profile quality is low, less information is available about the customer. Hence, there is less opportunity for the available information to be obsolete. Therefore, the profile deteriorates at a lower rate when the profile quality is low.

Based on the above discussion, the manner in which the profile changes over time (the state equation) can be written as:

$$
\dot {x} (t) = \alpha u - \beta x (t).\tag{3}
$$

In the above equation, the effectiveness of the recommender system is captured by the parameter ${ \mathfrak { a } } \in ( 0 , 1 ] .$ . The effectiveness depends on two factors: (1) the quality of the algorithm used to recommend, and (2) the data set supplied to the algorithm to learn customer preferences. The rate at which the profile improves depends on the product ${ \bf { a } } \cdot { \boldsymbol { u } } ,$ , whereas the profile deteriorates depending on the profile loss parameter $\beta ( > 0 )$ times the current profile. This loss in profile is analogous to forgetting in advertising models. Table 1 summarizes the main notations used in the model.

Using Equations (2) and (3), we present the surplus maximization problem of the customer as:

$$
\max _ {u} \left\{\int_ {0} ^ {\infty} \left[ R - u (A + x (t) ^ {2} - B x (t) + q _ {1}) - (1 - u) (A + x (t) ^ {2} - B x (t) + \gamma + q _ {2}) \right] e ^ {- r t} d t \right\},
$$

Table 1. Parameters and Variables

<table><tr><td>Symbol</td><td>Definition</td><td>Remarks</td></tr><tr><td> $A$ </td><td>Maximum fit cost</td><td></td></tr><tr><td> $B$ </td><td>Fit cost reduction factor</td><td>Higher  $B$  reduces the fit cost at a higher rate</td></tr><tr><td> $\gamma$ </td><td>Additional fit cost</td><td></td></tr><tr><td> $R$ </td><td>Reservation Price</td><td> $R > 0$ </td></tr><tr><td> $\alpha$ </td><td>Effectiveness of the recommender system</td><td>A higher value indicates that the profile quality increases faster for the same level of  $u$ </td></tr><tr><td> $\beta$ </td><td>Profile loss parameter</td><td>The rate at which the profile loses relevance</td></tr><tr><td> $S$ </td><td>Total surplus of the customer</td><td></td></tr><tr><td> $r$ </td><td>Continuous discount rate</td><td> $r > 0$ </td></tr><tr><td> $u$ </td><td>Rate of purchase from the personalizing firm</td><td>Decision variable for the customer</td></tr><tr><td> $q_{1}$ </td><td>Price charged by the personalizing firm</td><td>Decision variable for the personalizing firm</td></tr><tr><td> $q_{2}$ </td><td>Price charged by the non-personalizing firm</td><td>Decision variable for the non-personalizing firm</td></tr><tr><td> $x(t)$ </td><td>Profile quality</td><td>State variable</td></tr></table>

subject to:

$$
\dot {x} (t) = \alpha u - \beta x (t)
$$

$$
0 \leq u \leq 1.
$$

Solution to the Customer’s Problem

We first solve Equation (3) to find the profile of the customer at time <sup>t</sup>. Equation (3) is a differential equation of first order and the solution of the equation is:

$$
x (t) = \frac {\alpha u}{\beta} \left(1 - e ^ {- \beta t}\right).\tag{4}
$$

It should be clear from the above equation that $\textstyle x \in [ 0 , { \frac { \mathfrak { a } } { \mathfrak { b } } } ]$ . The above expression for $x ( t )$ can be substituted in Equation (2) to obtain the total (discounted) surplus for a customer that can be optimized to find the optimal purchase rate. Therefore, implicitly, <sup>u</sup> is a function of $x ( t )$

Lemma 1: The optimal rate at which customers purchase from the personalizing firm $( 0 \leq u \leq 1 )$ is:

$$
u = \left\{ \begin{array}{l l} \frac {(r + 2 \beta) (B \alpha + (q _ {2} - q _ {1} + \gamma) (r + \beta))}{4 \alpha^ {2}} & i f 0 \leq (B \alpha + (q _ {2} - q _ {1} + \gamma) (r + \beta)) \leq \min \Bigl \{\frac {4 \alpha^ {2}}{r + 2 \beta}, \frac {2 B \alpha \beta}{r + 2 \beta} \Bigr \}; \\ 0 o r 1 & o t h e r w i s e. \end{array} \right.\tag{5}
$$

The proofs are provided in the Appendix. To ensure a duopoly, we impose the condition $0 \leq u \leq 1$ along with $2 x - B \leq 0$ (the fit cost is always decreasing in <sup>x</sup>), which provides the condition presented in Equation (5). When this condition is not satisfied, we have a monopoly (as shown in Lemma 1 when <sup>u</sup> is 0 or 1). The interpretation of this condition follows. If the price of the non-personalizing firm is very low compared to the price of the personalizing firm $( { \mathrm { i . e . , ~ } } ( q _ { 1 } - q _ { 2 } )$ is a large positive number), the non-personalizing firm covers the entire market. On the other hand, when $q _ { 2 }$ is too close to $q _ { 1 }$ , the entire market is covered by the personalizing firm.

As shown in Lemma 3.1.4, the optimal purchase rates from the personalizing and non-personalizing firms (<sup>u</sup> and $1 - u _ { ; }$ , respectively) are functions of the prices charged by the firms. Therefore, we next focus on determining these prices (denoted by $q _ { 1 }$ and $q _ { 2 } )$ in equilibrium.

## The Pricing Problem

We analyze a simultaneous price game between the personalizing firm and the nonpersonalizing firm where both firms maximize their profits. Without any loss of generality, we normalize the unit cost for both firms to be zero. Therefore, maximizing revenue is equivalent to maximizing profit. The profits of the personalizing firm and the non-personalizing firm can be written as

$$
\Pi_ {1} = \int_ {0} ^ {\infty} u q _ {1} e ^ {- r t} d t = u q _ {1} \int_ {0} ^ {\infty} e ^ {- r t} d t, \text {   and   }
$$

$$
\Pi_ {2} = \int_ {0} ^ {\infty} (1 - u) q _ {2} e ^ {- r t} d t = (1 - u) q _ {2} \int_ {0} ^ {\infty} e ^ {- r t} d t.
$$

Since the profit for each firm is a function of both $q _ { 1 }$ and $q _ { 2 }$ , both firms simultaneously obtain Nash equilibrium prices by optimizing the following objective functions:

$$
\max _ {q _ {1}} \Pi_ {1} = \max _ {q _ {1}} \left[ u q _ {1} \int_ {0} ^ {\infty} e ^ {- r t} d t \right], \text { and }
$$

$$
\max _ {q _ {2}} \Pi_ {2} = \max _ {q _ {2}} \left[ (1 - u) q _ {2} \int_ {0} ^ {\infty} e ^ {- r t} d t \right].
$$

Clearly, $\int _ { 0 } ^ { \infty } e ^ { - r t } d t$ is a constant with respect to these maximization problems. Hence, we ignore it in the profit expressions and rewrite the objective functions using Equation (5) as:

$$
\max _ {q _ {1}} \Pi_ {1} = \max _ {q _ {1}} [ u q _ {1} ] = \max _ {q _ {1}} \left[ q _ {1} \left(\frac {(r + 2 \beta) (B \alpha + (q _ {2} - q _ {1} + \gamma) (r + \beta))}{4 \alpha^ {2}}\right) \right], \text { and }\tag{6}
$$

$$
\max _ {q _ {2}} \Pi_ {2} = \max _ {q _ {2}} [ (1 - u) q _ {2} ] = \max _ {q _ {2}} \left[ q _ {2} \left(1 - \frac {(r + 2 \beta) (B \alpha + (q _ {2} - q _ {1} + \gamma) (r + \beta))}{4 \alpha^ {2}}\right) \right].\tag{7}
$$

We use the expressions provided in Equations (6) and (7) to obtain the Nash Equilibrium solution that is presented in the following lemma.

Lemma 2: At the Nash equilibrium, when the conditions for duopoly are satisfied:<sup>5</sup> a. The rate at which customers purchase from the personalizing firm $( u ^ { * } )$ and the steady-state profile quality $( x ^ { * } )$ are:

$$
u ^ {*} = \frac {4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) \gamma}{1 2 \alpha^ {2}},\tag{8}
$$

$$
x ^ {*} = \frac {\alpha u ^ {*}}{\beta} = \frac {4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) \gamma}{1 2 \alpha \beta}.\tag{9}
$$

b. The price and profit of the personalizing firm are:

$$
q _ {1} ^ {*} = \frac {4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) \gamma}{3 (r + \beta) (r + 2 \beta)},\tag{10}
$$

$$
\Pi_ {1} ^ {*} = \frac {(4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) \gamma) ^ {2}}{3 6 \alpha^ {2} (r + \beta) (r + 2 \beta)}.\tag{11}
$$

c. The price and profit of the non-personalizing firm are:

$$
q _ {2} ^ {*} = \frac {8 \alpha^ {2} - B \alpha (r + 2 \beta) - (r + \beta) (r + 2 \beta) \gamma}{3 (r + \beta) (r + 2 \beta)},\tag{12}
$$

$$
\Pi_ {2} ^ {*} = \frac {(8 \alpha^ {2} - B \alpha (r + 2 \beta) - (r + \beta) (r + 2 \beta) \gamma) ^ {2}}{3 6 \alpha^ {2} (r + \beta) (r + 2 \beta)}.\tag{13}
$$

## Insights and Results

In this section, we provide several comparative statics that examine the impact of different parameters on equilibrium prices, profits, customer purchase rate, and steady-state profile quality. However, before we begin this discussion, it is instructive to analyze our model when $\gamma = 0$ . For the rest of the discussion in the paper, we assume that the parameter values satisfy the duopoly conditions.

In our setting, even when $\gamma = 0 ,$ , it is clear that the equilibrium levels of demand at the two firms are not necessarily equal:

$$
u ^ {*} = \frac {1}{3} + \frac {B (r + 2 \beta)}{1 2 \alpha},
$$

$$
1 - u ^ {*} = \frac {2}{3} - \frac {B (r + 2 \beta)}{1 2 \alpha}.
$$

This result shows that the recommendations are indeed a source of differentiation between firms, and despite the fact that customers can use the recommendations provided by one firm to shop at another, the differentiation provided by a recommender system is not dissipated by competition. We next present comparative statics. Based on the results obtained in Lemma 3.2, we provide several insights for managing recommender systems and the associated pricing decisions.

## Impacts of Recommender System Effectiveness and Profile Loss Parameter

The following proposition summarizes the impact of increasing the effectiveness of recommender system (α).

Proposition 1: When the personalizing firm improves its recommender system:

a. Customers purchase more from the non-personalizing firm and the rate of shift of demand decreases, but the steady-state profile quality of the customer improves at an increasing rate:

$$
\frac {d u ^ {*}}{d \alpha} <   0, \frac {d ^ {2} u ^ {*}}{d \alpha^ {2}} > 0.
$$

$$
\frac {d x ^ {*}}{d \alpha} > 0, \frac {d ^ {2} x ^ {*}}{d \alpha^ {2}} > 0.
$$

b. Both firms charge higher prices:

$$
\frac {d q _ {1} ^ {*}}{d \alpha} > 0, \frac {d q _ {2} ^ {*}}{d \alpha} > 0.
$$

c. The profits of both firms increase:<sup>6</sup>

$$
\frac {d \Pi_ {1} ^ {*}}{d \alpha} > 0, \frac {d \Pi_ {2} ^ {*}}{d \alpha} > 0.
$$

First, consider the personalizing firm. Improving the recommender system enables the firm to learn customer choices faster. Therefore, as shown in Proposition 1(a), increasing the effectiveness of the recommendation system improves the profile quality, and therefore the fit cost of the customer decreases. Hence, as shown in Proposition 1(b), the personalizing firm is able to increase its price. There exists anecdotal evidence of price increase with the improved recommender system. For example, within a few months after implementing the “Genius” toolbar (which provides music recommendations), iTunes switched to variable pricing (the new and popular songs were priced higher than other songs) that increased the average prices of the songs [45].

Proposition 1(a) also shows that $u ^ { * }$ decreases as the personalizing firm improves its recommender system. This result can be explained as follows. Since the profile improves with an improvement in the recommender system, the customer can afford to purchase less from the personalizing firm and transfer some demand to the nonpersonalizing firm. However, the customer tempers this demand transfer because, otherwise, the profile would be hurt (see Equation [3]). In equilibrium, the impact of reduced purchase on profile is dominated by the impact of improved recommender system effectiveness. Hence, despite the reduced customer patronage at the personalizing firm, the profile improves with effectiveness of the recommender system. For the profit of the personalizing firm, the positive impact of increased price dominates the negative effect of decreased demand. Therefore, the profit of the personalizing firm increases with the recommender system effectiveness (see Proposition 1[c]).

We now turn our attention to the non-personalizing firm. As shown in Proposition 1(b), the non-personalizing firm also increases its price with an improvement in the recommender system. Also, the customer purchases from the non-personalizing firm at a higher rate (see Proposition 1[a]). Hence, its profit increases with an improvement in the recommender system (as shown in Proposition 1[c]). Conceptually, an improvement in the recommender system increases the differentiation between the two firms. Therefore, the profits of both firms increase. Thus, the non-personalizing firm free-rides on the improved recommendations provided by the personalizing firm. This free-riding phenomenon is also mentioned in the quality literature where improving the quality of one product increases the profit of the competing firm due to increased differentiation between firms [33]. Finally, we experimentally find that the customer’s surplus decreases with an improvement in the recommender system: although the fit cost decreases, both prices increase.

From Equation (4), $\begin{array} { r } { x = \frac { \alpha u } { \beta } } \end{array}$ in the steady-state. Therefore, the impact of profile loss parameter (β) is opposite to the impact of recommender system effectiveness (α). The results are summarized in the following proposition.

## Proposition 2: When the profile loss parameter $\left( \beta \right)$ increases:

a. The customer purchases more from the personalizing firm and the rate of shift of demand increases, but the steady-state profile quality deteriorates at a decreasing rate:

$$
\frac {d u ^ {*}}{d \beta} > 0, \frac {d ^ {2} u ^ {*}}{d \beta^ {2}} > 0.
$$

$$
\frac {d x ^ {*}}{d \beta} <   0, \frac {d ^ {2} x ^ {*}}{d \beta^ {2}} > 0.
$$

b. The prices and profits of both firms decrease:

$$
\frac {d q _ {1} ^ {*}}{d \beta} <   0, \frac {d q _ {2} ^ {*}}{d \beta} <   0.
$$

$$
\frac {d \Pi_ {1} ^ {*}}{d \beta} <   0, \frac {d \Pi_ {2} ^ {*}}{d \beta} <   0.
$$

Further, we experimentally find that the customer’s surplus increases with the profile loss parameter. Clearly, this effect is also opposite to the effect of recommender system effectiveness.

## Increase in Additional Fit Cost

An increase in additional fit cost (γ) can be considered equivalent to a situation in which customers are less able to transfer the benefit of recommendations from the personalizing firm to the other firm. We present the impacts of additional fit cost in the following remark.

## Remark 1: When the additional fit cost $( \gamma )$ increases:

a. The customer purchases more from the personalizing firm and the steady-state profile improves:

$$
\frac {d u ^ {*}}{d \gamma} > 0, \frac {d x ^ {*}}{d \gamma} > 0.
$$

b. The price charged by the personalizing firm (non-personalizing firm) increases (decreases):

$$
\frac {d q _ {1} ^ {*}}{d \gamma} > 0, \frac {d q _ {2} ^ {*}}{d \gamma} <   0.
$$

c. The profit of the personalizing firm (non-personalizing firm) increases (decreases):

$$
\frac {d \Pi_ {1} ^ {*}}{d \gamma} > 0, \frac {d \Pi_ {2} ^ {*}}{d \gamma} <   0.
$$

When $\gamma$ increases, the personalizing firm increases its price to take advantage of the fact that switching to the competing firm has become more difficult. Despite this fact, the customer purchases more from the personalizing firm $( \mathrm { i } . \mathrm { e } . , u ^ { \ast }$ increases) with an increase in $\gamma .$ This increase in $u ^ { * }$ improves the profile and reduces the fit cost incurred at both firms. On the other hand, the nonpersonalizing firm has to reduce its price to make itself more attractive, that ${ \mathrm { i } } \mathbf { s } ,$ to compensate for the increased additional fit cost. However, the reduction in its price is less than the increase in additional fit cost $\begin{array} { r } { ( \mathrm { i . e . , ~ } \left| \frac { \partial { q _ { 2 } ^ { * } } } { \partial { \gamma } } \right| { < } 1 ) } \end{array}$ , because the non-personalizing firm realizes that the customer benefits from the reduced fit cost. Finally, the profit of the personalizing firm increases due to an increase in both the demand $( u ^ { * } )$ and the price $( q _ { 1 } ^ { * } )$ , whereas the profit of the nonpersonalizing firm decreases due to a decrease in both the demand $( 1 - u ^ { * } )$ and the price $( q _ { 2 } ^ { * } )$ . These results are similar to those observed in the switching cost literature. Usually, when the switching cost increases, the firm that imposes the switching cost on the customer benefits, and the profit of the competing firm decreases.

## Variants of the Base Model

In this section, we extend our analysis to consider the following realistic variants of the base model: (1) customer heterogeneity in additional fit cost, (2) additional fit cost dependent on profile, and (3) dynamic customer purchase rate. We begin with the case in which customers are heterogeneous in their additional fit costs.

## Customers Are Heterogeneous in Additional Fit Costs

In our base model, the additional fit cost $( \gamma )$ was the same for all the customers. However, in certain scenarios, it is possible to have different additional fit costs across customers, for example, for certain product categories, it might be easier for web-savvy customers to find a substitute. Hence, in this subsection, we consider that the customers are heterogeneous in their additional fit costs. Since we expect purchase behavior to be different across customers, this analysis might allow the firm to devise customer segmentation and targeting strategies.

In this model, we replace $\gamma$ in the objective function (i.e., Equation [2]) with $k \gamma _ { 1 } ( = \gamma )$ , where $0 \leq \gamma _ { 1 } \leq 1$ is the sensitivity of a customer to the substitution. A customer with no sensitivity $( \mathrm { i } . \mathrm { e } . , \gamma _ { 1 } = 0 )$ would incur zero additional fit cost for substituting a recommended product with one from the non-personalizing firm, whereas a customer with the highest sensitivity $( \mathrm { i } . \mathbf { e } . , \gamma _ { 1 } = 1 )$ would incur an additional fit cost <sup>k</sup>. Hence, <sup>k</sup> is the maximum additional fit cost. The surplus of a customer with sensitivity $\gamma _ { 1 }$ can be written as:

$$
\begin{array}{l} \max _ {u} \Bigg \{\int_ {0} ^ {\infty} (R - [ u (A + x (t) ^ {2} - B x (t) + q _ {1}) \\ + (1 - u) (A + x (t) ^ {2} - B x (t) + k \gamma_ {1} + q _ {2}) ]) e ^ {- r t} d t \Bigg \}, \end{array}
$$

where

$$
\dot {x} (t) = \alpha u - \beta x (t).
$$

As shown earlier, we solve the customer’s surplus maximization problem and find that:<sup>7</sup>

$$
u = \frac {(r + 2 \beta) (B \alpha + (q _ {2} - q _ {1} + k \gamma_ {1}) (r + \beta))}{4 \alpha^ {2}}.\tag{14}
$$

Next, firms solve the pricing game using the customer response, <sup>u</sup>. If the sensitivities of the customers are uniformly distributed between 0 and 1, the profits of personalizing and non-personalizing firms can be written as:

$$
\Pi_ {1} = \int_ {0} ^ {1} u q _ {1} d \gamma_ {1}, \text {   and   } \Pi_ {2} = \int_ {0} ^ {1} (1 - u) q _ {2} d \gamma_ {1}, \text {   respectively. }
$$

The solution to the pricing game with heterogeneous customers is presented below.

Lemma 3: At the Nash equilibrium with heterogeneous customers:<sup>8</sup>

a. The rate at which the customer with sensitivity $\gamma _ { 1 }$ purchases from the personalizing firm is:

$$
u ^ {*} = \frac {4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) k (- 1 + 3 \gamma_ {1})}{1 2 \alpha^ {2}}.\tag{15}
$$

b. Price and profit of the personalizing firm are:

$$
q _ {1} ^ {*} = \frac {8 \alpha^ {2} + 2 B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) k}{6 (r + \beta) (r + 2 \beta)}, \text { and }
$$

$$
\Pi_ {1} ^ {*} = \frac {(8 \alpha^ {2} + 2 B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) k) ^ {2}}{1 4 4 \alpha^ {2} (r + \beta) (r + 2 \beta)}, \text { respectively. }
$$

c. Price and profit of the non-personalizing firm are:

$$
q _ {2} ^ {*} = \frac {1 6 \alpha^ {2} - 2 B \alpha (r + 2 \beta) - (r + \beta) (r + 2 \beta) k}{6 (r + \beta) (r + 2 \beta)}, \text { and }
$$

$$
\Pi_ {2} ^ {*} = \frac {(1 6 \alpha^ {2} - 2 B \alpha (r + 2 \beta) - (r + \beta) (r + 2 \beta) k) ^ {2}}{1 4 4 \alpha^ {2} (r + \beta) (r + 2 \beta)}, \text { respectively. }
$$

The key impact of introducing customer heterogeneity is that it affects the rates at which different kinds of customers purchase from the two firms. This result is outlined in the proposition below.

Proposition 3: When the maximum additional fit cost (<sup>k</sup>) increases, the customers with relatively low sensitivity $\begin{array} { r } { ( \gamma _ { 1 } { < } \gamma _ { 1 t } = \frac { 1 } { 3 } ) } \end{array}$ purchase less from the personalizing firm, whereas other customers (i.e., those with relatively high sensitivity) purchase more from the personalizing firm.

An increase in <sup>k</sup> increases the additional fit cost for all customers except those who have zero sensitivity for substitution. Therefore, holding the prices constant, customers purchase more frequently from the personalizing firm (see Equation [14]). As a reaction, the personalizing firm increases its price and the nonpersonalizing firm reduces its price. In response, less sensitive customers $( \gamma _ { 1 } < \gamma _ { 1 t } )$ start purchasing more from the non-personalizing firm to take advantage of the lower price. On the other hand, the customers with high sensitivity for the substitution $( \gamma _ { 1 } \geq \gamma _ { 1 t } )$ purchase at an increased rate from the personalizing firm to counter the increase in additional fit costs. Thus, additional fit cost heterogeneity leads to natural segmentation in the customer population. It is important for firms to consider this segmentation when designing their promotions. For example, the personalizing firm may give coupons to customers who are likely to shift purchases to the non-personalizing firm. These customers must, of course, be identified as those who have relatively lower additional fit cost. Thus, in addition to the conventional role of learning customer preferences, recommender systems should also aim to track and predict the switching behavior of customers.

## Heterogeneous Customers and Additional Fit Cost Dependent on Profile

So far we have considered that the additional fit cost is not dependent on the profile of the customer. However, in certain scenarios, this cost may be a function of the profile. For example, the substitution might be more difficult when the recommendation is highly personalized (which makes it difficult for the customer to find a similar product at the non-personalizing firm). Hence, in this subsection, we extend our base model to introduce this dependence of additional fit cost on the profile.

Moreover, as in the previous subsection, we consider that customers are heterogeneous in their substitution costs. Specifically, we let, $\gamma = k \gamma _ { 1 } + m \gamma _ { 2 } x .$ , where <sup>m</sup> is referred to as the profile cost increment rate, $\gamma _ { 2 } ~ ( 0 \leq \gamma _ { 2 } \leq 1 )$ is referred to as the sensitivity to the profile cost, and $m \gamma _ { 2 } x$ is referred to as the profile cost. In this case, an improvement in profile quality would increase the additional fit cost, thus making the non-personalizing firm less attractive to the customer. Therefore, the purchase behavior of customers as well as the prices and profits of the firms would be different in this scenario compared to those in the base model. Hence, it will be interesting and useful to analyze them in detail.

Below we show the profit functions of the two firms assuming that the customers are uniformly distributed with parameters $\gamma _ { 1 } \in [ 0 , 1 ]$ and $\gamma _ { 2 } \in [ 0 , 1 ]$ :

$$
\Pi_ {1} = \int_ {0} ^ {1} \int_ {0} ^ {1} u q _ {1} d \gamma_ {1} d \gamma_ {2} \text {   and   } \Pi_ {2} = \int_ {0} ^ {1} \int_ {0} ^ {1} (1 - u) q _ {2} d \gamma_ {1} d \gamma_ {2}.
$$

Using the methods employed in previous sections, we obtain the following solution.

Lemma 4: At Equilibrium:<sup>9</sup>

a. The rate at which the customer with parameters $\gamma _ { 1 }$ and $\gamma _ { 2 }$ purchases from the personalizing firm is:

$$
u ^ {*} = \frac {k (r + \beta) (r + 2 \beta) (- 1 + 3 \gamma_ {1}) + \alpha (4 \alpha + (r + 2 \beta) (B - 3 m \gamma_ {2}))}{6 \alpha (2 \alpha - (r + 2 \beta) m \gamma_ {2})}.\tag{16}
$$

b. Price and profit of the personalizing firm are:

$$
q _ {1} ^ {*} = \frac {k (r + \beta) + 2 \alpha \left(B - \frac {2 \alpha}{r + 2 \beta} + \frac {3 m}{\ln (\alpha) - \ln \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)}\right)}{6 (r + \beta)}, \text { and }
$$

$$
\Pi_ {1} ^ {*} = \frac {\left[ \begin{array}{c} 6 m \alpha (r + 2 \beta) + (k (r + \beta) (r + 2 \beta) + 2 \alpha (- 2 \alpha + B (r + 2 \beta))) \\ \left(\ln (\alpha) - \ln \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right) \end{array} \right] ^ {2}}{7 2 m \alpha (r + \beta) (r + 2 \beta) ^ {2} \left[ \ln (\alpha) - \ln \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right) \right]}, \text {respectively.}
$$

c. Price and profit of the non-personalizing firm are:

$$
q _ {2} ^ {*} = \frac {2 \alpha \left(- B + \frac {2 \alpha}{r + 2 \beta} + \frac {3 k}{\ln (\alpha) - \ln \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)}\right) - k (r + \beta)}{6 (r + \beta)}, \text { and }
$$

$$
\Pi_ {2} ^ {*} = \frac {\left[ \begin{array}{c} - 6 m \alpha (r + 2 \beta) + (k (r + \beta) (r + 2 \beta) + 2 \alpha (- 2 \alpha + B (r + 2 \beta))) \\ (\ln (\alpha) - \ln (\alpha - \frac {1}{2} m (r + 2 \beta))) \end{array} \right] ^ {2}}{7 2 m \alpha (r + \beta) (r + 2 \beta) ^ {2} [ \ln (\alpha) - \ln (\alpha - \frac {1}{2} m (r + 2 \beta)) ]}, \text { respectively. }
$$

The extensive numerical experiments show that the impacts of α, β, and <sup>k</sup> are similar to those in the previous section. The numerical experiments also show that when the profile cost increment rate (<sup>m</sup>) increases, the profits and prices of both firms decrease, and the customers purchase more from the personalizing firm. An increase in <sup>m</sup> leads to an increased additional fit cost for the customer. Therefore, the non-personalizing firm reduces its price to decrease the defection of customers to the personalizing firm. As a reaction, the personalizing firm also reduces its price. For the personalizing firm, the increase in $u ^ { * }$ is not able to offset the loss due to the decrease in its price. Hence, the profit of the personalizing firm decreases with an increase in <sup>m</sup>. For the non-personalizing firm, the profit declines because of a decrease in both demand and price.

Interestingly, an increase in <sup>m</sup> tends to increase differentiation between the firms, but reduces profits for both firms. Situations in which increased differentiation reduces the profit of a firm have been found in other domains of the marketing literature as well. For example, Syam et al. [47] show that in the presence of two firms that can customize products in two attributes, both firms prefer to customize in only one attribute and in the same dimension. If a firm differentiates by customizing in a different dimension, this leads to a price war that hurts both firms.

## Purchase Rate of Customer Varies with Time

In the base model, customers decide on a fixed purchase fraction at each firm. However, it is useful to investigate how the outcomes of interest change when customers are strategic in the sense that they reevaluate their purchase decisions to adjust the purchase fraction over time. Because this variant of the base model is a relaxation, we would, of course, expect customers to benefit by being strategic. Therefore, it will be useful to study the gains achieved by customers and the impact on the pricing strategies of firms. In this model, since both the state variable (profile <sup>x</sup>) and the control variable (fraction of purchases from the personalizing firm, i.e., <sup>u</sup>) vary with time, we use optimal control theory to solve the customer’s problem and derive the optimal rates at which the customers purchase from the two firms. First, we solve the model with additional fit cost as $\gamma = k \gamma _ { 1 }$ and then we consider that the additional fit cost depends on profile quality.

## Additional Fit Cost Not Dependent on Profile Quality

Depending on the initial value of the profile, the customer uses $u ( t ) = 1 \ \mathrm { o r } \ u ( t ) = 0$ during the initial (or transient) phase of the solution. However, once the optimal long-run stationary equilibrium is reached, a steady value is maintained. Hence, in infinite horizon problems, the emphasis is on finding the optimal long-run stationary equilibrium (which is also called a turnpike solution) [6].

In the long-run stationary equilibrium, the profile and the purchase rate become independent of time. Also, the price differential between the two firms (i.e., the extra price paid by the customer for purchasing <sup>u</sup> fraction of products from the personalizing firm = $u ( q _ { 1 } - q _ { 2 } ) )$ equals the switching cost incurred by the customer $( k \gamma _ { 1 } )$ . It is important to emphasize that the long-run stationary equilibrium is not the same as the optimal solution for a static problem because the long-run stationary equilibrium is derived considering a trade-off between the price differential and the switching cost over the entire time horizon [43]. For brevity, we will refer to the optimal long-run stationary equilibrium as the optimal solution, and the values of the control and the profile in this solution will be denoted by ^<sup>u</sup> and ^<sup>x</sup>, respectively. Next, we solve the static game between the two firms using ^<sup>u</sup> as the rate of purchase of a customer from the personalizing firm and $( 1 - \hat { u } )$ as the rate of purchase by the customer from the non-personalizing firm. The results are presented below.

## Lemma 5: At the Nash Equilibrium:<sup>10</sup>

a. The rate at which customer purchases from the personalizing firm is:

$$
\hat {u} = \frac {2 \alpha^ {2} + B \beta \alpha + k \beta (r + \beta) (- 1 + 3 \gamma_ {1})}{6 \alpha^ {2}}.
$$

b. Price and profit of the personalizing firm are:

$$
q _ {1} ^ {*} = \frac {4 \alpha^ {2} + 2 B \beta \alpha + k \beta (r + \beta)}{6 \beta (r + \beta)}, \text {   and   }
$$

$$
\Pi_ {1} ^ {*} = \frac {\left(4 \alpha^ {2} + 2 B \beta \alpha + k \beta (r + \beta)\right) ^ {2}}{7 2 \alpha^ {2} \beta (r + \beta)}, \text {   respectively.   }
$$

c. Price and profit of the non-personalizing firm are:

$$
q _ {2} ^ {*} = \frac {8 \alpha^ {2} - 2 B \beta \alpha - k \beta (r + \beta)}{6 \beta (r + \beta)}, \text {   and   }
$$

$$
\Pi_ {2} ^ {*} = \frac {\left(8 \alpha^ {2} - 2 B \beta \alpha - k \beta (r + \beta)\right) ^ {2}}{7 2 \alpha^ {2} \beta (r + \beta)}, \text { respectively }.
$$

The impacts of recommender system effectiveness, profile loss parameter, and additional fit cost coefficient $( \mathrm { i . e . , \ : a , \ : \beta } ,$ and <sup>k</sup>, respectively) on the prices and profits of the firms remain the same as those discussed in the earlier section. However, unlike the base case, the customer’s surplus might increase with an increase in α based on the condition shown below.

Proposition 4: The customer’s surplus increases with an improvement in the recommender system (increase in α) iff the following condition holds:

$$
\begin{array}{c} \Omega = - 4 \alpha^ {4} (1 1 \beta + r) + 4 \alpha^ {3} B \beta (2 \beta + r) + \alpha (1 - 3 \gamma_ {1}) k \beta^ {2} B (\beta + r) (\beta + 2 r) \\ + \beta^ {2} k ^ {2} (1 - 3 \gamma_ {1}) ^ {2} (r + \beta) ^ {2} (r - \beta) > 0. \end{array}
$$

Intuitively, the customer’s surplus increases with α when α is small (i.e., when $\Omega > 0 )$ At a small value of ${ \mathfrak { a } } ,$ profile quality (^<sup>x</sup>) is small, and therefore the reduction in the fit cost is large (because the fit cost reduces at a decreasing rate, i.e., the fit cost decreases more when ^<sup>x</sup> is small). This reduction in the fit cost is more than the combined increase in the prices of the two firms. On the other hand, when $\Omega < 0$ , the customer’s surplus decreases as the recommender system improves. Figure 1 further illustrates how the customer’s surplus changes with α when $R = 8 0 0 , A = 2 4 0 0 , B = 1 0 9 , \beta = 0 . 0 1 6 ,$ $\gamma _ { 1 } = 0 . 2 5 , k = 1$ , and $r = 0 . 0 3$ . Here, the surplus increases with an increase in α until ${ \mathfrak { a } } = 0 . 5 .$ , and then the surplus decreases with a further increase in α. Therefore, we find that a strategic customer can select the purchase fraction from the two firms in such a way that her surplus increases. In contrast, when the customer keeps $u \ ( \mathrm { a n d \ ( } 1 - u ) )$ constant throughout the planning horizon, her surplus always decreases with an improvement in the recommender system (as already discussed).

![](/api/attachments/JTETNB6S/fulltext/images/419c3c083540b012fa7652a9c909f2d539dfa6356f5a856602995e5f4b938fae.jpg)  
Figure 1. Impact of Recommender System Effectiveness on the Customer’s Surplus

## Additional Fit Cost Dependent on Profile Quality

In this section, we consider that the additional fit cost is dependent on profile (similar to that in in the previous section). Hence, the customers are heterogeneous in parameters $\gamma _ { 1 }$ and $\gamma _ { 2 }$ . Also, they change the fractions of purchases from the two firms over time. We obtain the equilibrium solution in manner similar to that in the earlier scenario. The solution is presented below.

Lemma 6: At the Nash Equilibrium:<sup>11</sup>

a. The rate at which the customer purchases from the personalizing firm is:

$$
\hat {u} = \frac {\beta \left(k (r + \beta) (- 1 + 3 \gamma_ {1}) + \alpha \left(B + \frac {4 \alpha}{r + 2 \beta} - 3 m \gamma_ {2} + \frac {m r}{\beta \ln (\alpha) - \beta \ln \left(- \frac {m r}{2} + \alpha - m \beta\right)}\right)\right)}{3 \alpha (2 \alpha - m (r + 2 \beta) \gamma_ {2})}.\tag{17}
$$

b. Price and profit of the personalizing firm are:

$$
\begin{array}{c} q _ {1} ^ {*} = \frac {k (r + \beta) + 2 \alpha \left(B - \frac {2 \alpha}{r + 2 \beta} + \frac {m (r + 3 \beta)}{\beta \left(\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right)}\right)}{6 (r + \beta)}, \text { and } \\ \Pi_ {1} ^ {*} = \frac {\left(2 m \alpha (r + 2 \beta) (r + 3 \beta) + \beta \binom{k (r + \beta) (r + 2 \beta) +}{2 \alpha (- 2 \alpha + B (r + 2 \beta))}\right)}{\left(\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right) ^ {2}} \\ \hline 3 6 m \alpha \beta (r + \beta) (r + 2 \beta) ^ {3} \left(\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right), \text { respectively }. \end{array}\tag{18}
$$

c. Price and profit of the non-personalizing firm are:

$$
\begin{array}{l} q _ {2} ^ {*} = \frac {- k (r + \beta) + 2 \alpha \biggl (- B + \frac {2 \alpha}{r + 2 \beta} + \frac {m (2 r + 3 \beta)}{\beta \left(\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right)} \biggr)}{6 (r + \beta)}, \text {and} \\ \Pi_ {2} ^ {*} = \frac {\left(2 m \alpha (r + 2 \beta) (2 r + 3 \beta) + \beta \binom{k (r + \beta) (r + 2 \beta) +}{2 \alpha (- 2 \alpha + B (r + 2 \beta))}\right)}{\left(- \operatorname{In} (\alpha) + \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right) ^ {2}} , \text {respectively}. \end{array}
$$

The extensive numerical experiments show that the impacts of ${ \mathfrak { a } } , \ \beta ,$ , and <sup>k</sup> are similar to those in the previous section. Hence, in Proposition 5, we present the impacts of only the profile cost increment rate (<sup>m</sup>).

Proposition 5: When the profile cost increment rate (<sup>m</sup>) increases:

a. The customers purchase more from the personalizing firm, that is, ^<sup>u</sup> increases iff the following condition holds:

$$
(r + 2 \beta) \gamma_ {2} \left(k (r + \beta) (- 1 + 3 \gamma_ {1}) + \alpha \left(\frac {B + \frac {4 \alpha}{r + 2 \beta} - 3 m \gamma_ {2} +}{\frac {m r}{\beta \operatorname{In} (\alpha) - \beta \operatorname{In} \left(- \frac {m r}{2} + \alpha - m \beta\right)}}\right)\right) +
$$

$$
(2 \alpha - m (r + 2 \beta) \gamma_ {2}) \left(- 3 \gamma_ {2} + \frac {r \left(1 + \frac {2 \alpha}{m r - 2 \alpha + 2 m \beta} + \operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right)}{\beta \left(\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)\right) ^ {2}}\right) > 0.
$$

b. The profit of the personalizing firm (-) increases $i f f .$

$$
\left[ \begin{array}{c} 2 m \alpha (r + 2 \beta) (r + 3 \beta) + \beta (k (r + \beta) (r + 2 \beta) + 2 \alpha (- 2 \alpha + B (r + 2 \beta))) \\ \left(\operatorname{In} (\alpha) - \operatorname{In} \bigl (\alpha - \frac {1}{2} m (r + 2 \beta) \bigr)\right) \end{array} \right]
$$

$$
\frac {\left[ \begin{array}{c} 2 m ^ {2} \alpha (r + 2 \beta) ^ {2} (r + 3 \beta) - \\ \binom {m (r + 2 \beta) ^ {2} (4 \alpha^ {2} + 2 B \alpha \beta + k \beta (r + \beta) - 2 m \alpha (r + 3 \beta)) + \beta (- 2 \alpha + m (r + 2 \beta))} {(k (r + \beta) (r + 2 \beta) + 2 \alpha (- 2 \alpha + B (r + 2 \beta))) (\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right))} \\ (\operatorname{In} (\alpha) - \operatorname{In} \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)) \end{array} \right]}{3 6 m ^ {2} \alpha \beta (r + \beta) (r + 2 \beta) ^ {3} (- 2 \alpha + m (r + 2 \beta)) (\operatorname{In} (\alpha) - \ln \left(\alpha - \frac {1}{2} m (r + 2 \beta)\right)) ^ {2}} > 0.
$$

Note that the results in Proposition 5 are different from those in the earlier section. More specifically, when <sup>u</sup> remains constant in time, we experimentally find that with an increase in <sup>m</sup>, <sup>u</sup> increases and the profit of the personalizing firm decreases. However, in the current setting, ^<sup>u</sup> increases with <sup>m</sup> only when the condition in Proposition 5(a) is satisfied. Likewise, the profit of the personalizing firm decreases with an increase in <sup>m</sup> only when the condition in Proposition 5(b) is not satisfied.

![](/api/attachments/JTETNB6S/fulltext/images/2001f56365e13997004d1313784ef58507bca2b58226b32e5d0f7100f331c90b.jpg)

![](/api/attachments/JTETNB6S/fulltext/images/6790a2ceb23f38f23808dcb51abe5800b650cf50bed90108ad28a78d32cd67f4.jpg)  
Figure 2. Impact of Profile Cost Increment Rate on the Rate of Purchase from Personalizing Firm

We illustrate the impact of <sup>m</sup> on $\hat { u }$ in Figure 2 using an example where ${ \mathfrak { a } } = 0 . 7 0 $ $\beta = 0 . 0 0 9$ $r = 0 . 0 1$ $B = 2 4 0$ , and $k = 0 . 8$ . In Figure 2a, where the value of $\gamma _ { 2 }$ is low $( \gamma _ { 2 } = 0 . 1 0 )$ , customers decrease their purchases from the personalizing firm with an increase in $m .$ These customers have a small impact of increased <sup>m</sup> on additional fit cost due to low sensitivity $( \gamma _ { 2 } )$ . Hence, for these customers, the additional fit cost incurred in purchasing more from the non-personalizing firm is overcompensated by lower prices at the non-personalizing firm. On the other hand, customers with higher $\gamma _ { 2 } ~ ( \gamma _ { 2 } = 0 . 1 5 )$ increase their purchases from the personalizing firm with an increase in <sup>m</sup> (Figure 2b), because the additional fit cost increases substantially with <sup>m</sup>.

In Figure 3, we now illustrate the impact of <sup>m</sup> on the profit of the personalizing firm using an example where $\mathbf { \alpha } \mathbf { a } = 0 . 7 0 , \beta = 0 . 0 0 9 , r = 0 . 0 1$ , and $k = 0 . 8$ . The value of <sup>B</sup> is high $( B = 2 6 0 )$ in Figure $^ { 3 \mathrm { a } , }$ and low $( B = 2 4 0 )$ in Figure 3b. When <sup>B</sup> is high (as in Figure 3b), the fit cost of the customer decreases at a higher rate. In this case, when <sup>m</sup> increases, some customers adjust their profile qualities by increasing ^<sup>u</sup> to the extent that the increased additional fit cost (due to a higher value of <sup>m</sup> and <sup>x</sup>) is offset by the reduced fit cost (due to higher value of $B ) _ { }$ . As a result, the customer’s surplus increases significantly. Therefore, the personalizing firm does not need to reduce its price too much. The gain due to increased ^<sup>u</sup> of some customers (who satisfy the condition in Proposition 5[a]) dominates the loss due to the decreased demands of other customers (who do not satisfy the condition) and reduced price. Hence, the profit of the personalizing firm increases with <sup>m</sup> when <sup>B</sup> is high. On the other hand, when <sup>B</sup> is low (as in Figure 3b), the profit of the personalizing firm decreases with an increase in <sup>m</sup>.

![](/api/attachments/JTETNB6S/fulltext/images/d70f411e719cf8572cf5ff8c73d987443dee20f1f171e0a6da1d6b6875a72c02.jpg)

![](/api/attachments/JTETNB6S/fulltext/images/1166e998278f65b533207bb283e34c851ccd64d228e9294e7b4a52ee2421594e.jpg)  
Figure 3. Impact of Profile Cost Increment Rate on the Profit of the Personalizing Firm

## Discussion

In this research, we consider two firms that compete on price: a personalizing firm that provides recommendations to customers based on their profile, and a non-personalizing firm that does not. Given a choice between these two firms, customers distribute their purchases between the two firms to maximize surplus. In doing so, customers trade off the quality of the recommendations (and hence, the fit cost) with the lower price (net of additional fit cost) at the non-personalizing firm. The customer takes advantage of recommendations not only at the personalizing firm but also at the non-personalizing firm. This strategic behavior of customer and its impact on firms have never been studied in the literature, and, to the best of our knowledge, this is the first paper that explores the economic impact of the strategic behavior of customers.

We consider the scenario in which the customer patronizes both firms in equilibrium. When the customers are homogeneous in their additional fit costs, they purchase less frequently at the personalizing firm following an increase in the effectiveness of the recommender system. Despite this, the personalizing firm benefits because it is able to offset the lower demand by charging a higher price. The implication of the above result is that personalization does provide differentiation benefits to the personalizing firm, even though the value gained from recommendations is transferable (either perfectly or by incurring an additional fit cost). We also find that, even in the absence of the additional fit cost, the firms do not charge the same price, that is, the differentiation between the firms does not dissipate. In fact, the recommender system differentiates the two firms.

We find that the non-personalizing firm can free-ride on improved recommendations provided by the personalizing firm and increase its profits. This happens because, with improved recommendations, the customer transacts more frequently with the nonpersonalizing firm. Further, we find that the customer’s surplus decreases with an improvement in the recommender system, despite her improved profile. This happens because the prices at both firms increase with an improvement in the recommender system. Based on these results, we are now able to answer the broad question: should a personalizing firm offer recommendations when the customer is strategic? We find that the recommender system is essentially a source of differentiation between firms that sell similar products. Hence, an improved recommender system benefits not only the personalizing firm but also the non-personalizing firm.

Next, we analyze the impact of change in the profile loss parameter on firms profits. We show that when the customer’s preferences change faster, the prices and profits of both firms decrease. In this case, the customer transacts more frequently with the personalizing firm in order to provide enough opportunities to the recommender system to help it learn her changed preferences. In essence, the effect of an increased profile loss parameter on firms is opposite to that of an increased recommender system. Thus, firms should strive to learn trends in changes in customers’ preferences. In general, this can be accomplished by analyzing customers’ past transactions. Sahoo et al. [41] describe a process of recommendation when customer preferences change.

We also analyze how the changes in additional fit cost impact the purchasing behavior of customers and the prices and profits of firms. Our results show that both price and profit of the personalizing firm (respectively, non-personalizing firm) increase (respectively, decrease) with additional fit cost. Also, as expected, customers purchase more frequently from the personalizing firm as the additional fit cost increases. These results are in line with those observed in the search cost literature. Thus, the non-personalizing firm should take measures that could help to reduce the additional fit cost. For example, the nonpersonalizing firm should update its website to make it user-friendly. Also, it should track the competitor’s catalog (i.e., personalizing firm) and attempt to offer similar products.

We also study several interesting variants of the base model. We consider a scenario in which customers are heterogeneous in their sensitivities toward substitute products, and we find that, by and large, the results of the base case continue to hold for both firms. However, customers with low sensitivity to substitution decrease their purchases from the personalizing firm with an increase in the maximum additional fit cost. This result suggests that when the maximum additional fit cost increases, the personalizing firm could benefit by offering coupons to customers who have low sensitivity to substitution in order to discourage them from migrating to the competitor. We also consider a situation in which customers prefer purchasing from the personalizing firm because of an extra profile cost (equal to the profile cost increment rate times the profile quality). We find that the profits of both firms decrease with an increase in the profile cost increment rate. Thus, firms should try to keep profile costs as low as possible. Firms can accomplish this by keeping their websites user-friendly and by providing enough information so that customers can easily find a substitute product.

Finally, we model a situation in which the customer varies (over time) the fractions of purchases from the two firms. In this case, the profit of the personalizing firm can increase with the profile cost increment rate under certain conditions. Further, in this case, the customer’s surplus can increase with an improvement in the recommender system, whereas it always decreases if customers keep the purchase fractions constant during the planning horizon. Thus, by being strategic, customers can counter the advantage that firms gain through an increase in recommender system effectiveness. Table A1 in Part B of the Appendix summarizes all the results.

## Conclusions and Future Research Directions

This research is a first step in an attempt to analyze the purchase behavior of customers who use the knowledge gained from personalization services at one firm to shop for a low price at another firm. The model in the paper can be extended to include more than two firms. Also, the non-personalizing firm may start providing personalization services, which will change the dynamics in the market. This would be an interesting area for future research. In this type of scenario, firms can choose to remain differentiated by selecting different recommender system effectiveness in order to avoid direct competition. The key idea of the paper can also be extended to other services (e.g., medical services) where the utility of service has a transferable component, but because service quality degrades with time, the customer cannot completely switch to another service provider while simultaneously maintaining service quality.

## NOTES

1. In this study, however, we determine the prices at the two firms endogenously, and allow the price at the personalizing firm to be higher or lower than that at the non-personaliz ing firm. Therefore, our model considers a general scenario.

2. They also consider many other competitions, such as between two personalizing firms and two non-personalizing firms. We do not discuss them as these competitions are not relevant to our research.

3. For notational simplicity, we will suppress (<sup>t</sup>) whenever it does not cause any confusion.

4. For example, different assortments of cosmetics (e.g., different lipstick shades) might be offered by the two firms. Therefore, the shade selected at the personalizing firm may not be available at the non-personalizing firm, and the customer might have to choose a similar (but different) shade. Similarly, the personalizing firm might hold exclusive rights to sell songs from a new album, and therefore the non-personalizing firm might not have those songs. However, the non-personalizing firm possibly offers other songs by the same singer that can be selected as a substitute.

5. Based on the condition shown in Lemma 3.1.4, the parameter values need to satisfy the following condition:

$$
\frac {4 \alpha^ {2} + (r + \beta) (r + 2 \beta) \gamma}{4 \alpha \beta} <   B <   \frac {8 \alpha^ {2} - (r + \beta) (r + 2 \beta) \gamma}{2 \alpha \beta}
$$

in order to maintain a market with duopoly.

6. The result in Proposition 1(c) is obtained by ignoring the operating cost of providing recommendations. If this cost is considered, the profit of the personalizing firm decreases if the increase in revenue due to an improved recommender system is less than the cost.

7. Again, this expression is valid only under the following conditions that are required to maintain a duopoly:

$$
B (\alpha + \eta) + (q _ {2} - q _ {1}) (r + \beta) > 0 \text {   and   } B (\alpha + \eta) + (q _ {2} - q _ {1} + k) (r + \beta) <   \min \left(\frac {4 \alpha^ {2}}{r + 2 \beta}, \frac {2 \alpha B \beta}{r + 2 \beta}\right).
$$

8. The parameters need to satisfy the following conditions in order to maintain a duopoly:

$$
\text {(i)} 4 \alpha^ {2} + B \alpha (r + 2 \beta) - (r + \beta) (r + 2 \beta) k > 0,
$$

<sub>ð</sub><sup>ii</sup><sub>Þ</sub> $- 8 { \bf a } ^ { 2 } + B { \bf a } ( r + 2 \beta ) + 2 ( r + \beta ) ( r + 2 \beta ) { \bf \ } k < 0$ ; and

<sub>ð</sub>iii<sub>Þ</sub> $4 \alpha ^ { 2 } + B \alpha ( r - 4 \beta ) + 2 k ( r + \beta ) ( r + 2 \beta ) < 0 .$

9. The parameters need to satisfy the following conditions for maintaining duopoly:

$$
\text { (i) } 4 \alpha^ {2} + B \alpha (r + 2 \beta) - k (r + \beta) (r + 2 \beta) > 0,
$$

$$
- 8 \alpha^ {2} + B \alpha (r + 2 \beta) + 2 k (r + \beta) (r + 2 \beta) + 3 \alpha (r + 2 \beta) m <   0, \tag {ii}
$$

(iii) $2 \mathsf { a } - m \gamma _ { 2 } ( r + 2 \mathsf { \beta } ) > 0 ,$

(iv) $6 0 \beta B - 3 \beta m ( r + 2 \beta ) > 2 k ( r + \beta ) ( r + 2 \beta ) + 4 \alpha ^ { 2 } + B { \alpha } ( r + 2 \beta ) - 3 m { \alpha } ( r + 2 \beta )$ , and

(v) $6 \alpha \beta B > 2 k ( r + \beta ) ( r + 2 \beta ) + 4 \alpha ^ { 2 } + B \alpha ( r + 2 \beta )$

10. The parameters need to satisfy the following conditions in order to maintain a duopoly:

$$
\text { (i) } 2 \alpha^ {2} + B \beta \alpha - k \beta (r + \beta) > 0,
$$

(ii) $- 4 \alpha ^ { 2 } + B \beta \alpha - 2 k \beta ( r + \beta ) < 0 ,$ and

(iii) $2 { \alpha } ^ { 2 } - 2 B { \alpha } \beta + 2 k \beta ( r + \beta ) < 0 .$

11. The parameters need to satisfy the following conditions for maintaining duopoly:

$$
\text {(i)} 2 k (r + \beta) + \alpha \left(B + \frac {4 \alpha}{r + 2 \beta} + \frac {m r}{\beta \operatorname{In} (\alpha) - \beta \operatorname{In} (\frac {- m r}{2} + \alpha - m \beta)}\right) > 0,
$$

$$
\text {(ii)} 2 k \beta (r + \beta) + \alpha \beta \left(B + \frac {4 \alpha}{r + 2 \beta} + \frac {m r}{\beta \ln (\alpha) - \beta \ln (\frac {- m r}{2} + \alpha - m \beta)}\right) <   6 \alpha^ {2},
$$

$$
\text {(iii)} 2 k \beta (r + \beta) + \alpha \beta \left(B + \frac {4 \alpha}{r + 2 \beta} - 3 + \frac {m r}{\beta \ln (\alpha) - \beta \ln (\frac {- m r}{2} + \alpha - m \beta)}\right) <   6 \alpha^ {2} - 3 a m (r + 2 \beta),
$$

$$
\begin{array}{l} \text {(iv)} \frac {3}{2} B (2 \alpha - m (r + 2 \beta)) > 2 k (r + \beta) + \alpha \Big (B + \frac {4 a}{r + 2 \beta} - 3 + \frac {m r}{\beta \ln (\alpha) - \beta \ln (\frac {- m r}{2} + \alpha - m \beta)} \Big), \\ \text {and} \end{array}
$$

$$
\text {(v)} 3 B \alpha > 2 k (r + \beta) + \alpha \left(B + \frac {4 \alpha}{r + 2 \beta} + \frac {m r}{\beta \ln (\alpha) - \beta \ln (\frac {- m r}{2} + \alpha - m \beta)}\right).
$$

## REFERENCES

1. Adomavicius, G., and Tuzhilin, A. Using data mining methods to build customer profiles. IEEE Computer, 34, 2 (2001), 74–82.

2. Adomavicius, G., and Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, 17, 6 (2005), 734–749.

3. Alam, S.; Dobbie, G.; Riddle, P.; and Koh, Y.S. Analysis of web usage data for clustering based recommender system. Trends in Practical Applications of Agents and Multiagent Systems, Advances in Intelligent Systems and Computing, 221 (2013), 171–179.

4. Amazon Inc. www.amazon.ca/gp/help/customer/display.html?ie=UTF8nodeId= 1162208, (2013) (accessed July 23, 2013).

5. Aron, R.; Sundararajan, A.; and Viswanathan, S. Intelligent agents in electronic markets for information goods: Customization, preference revelation and pricing. Decision Support Systems, 41 (2006),764–786.

6. Arrow, K.J., and Kurz, M. Public Investment, the Rate of Return, and Optimal Fiscal Policy. Baltimore: Johns Hopkins University Press, 1970.

7. Bank, D. A new model—a site-eat-site world: Disappearing profit margins have retailers fretting—and consumers rejoicing. Wall Street Journal, Eastern Ed., July 12, 1999.

8. Beach, L.R. Broadening the definition of decision making: The role of prechoice screening of options. Psychological Science, 4, 4 (1993), 215–220.

9. Bergemann, D., and Ozmen, D. Optimal pricing with recommender systems. Available at http://dirkbergemann.commons.yale.edu/files/2011/01/Paper19\_p1177.pdf (accessed September 26, 2013).

10. Biyalogorsky, E.; Gerstner, E.; and Libai, B. Customer referral management: Optimal reward programs. Marketing Science, 20, 1 (2001), 82–95.

11. Bodapati, A.V. Recommendation systems with purchase data. Journal of Marketing Research, 45, 1 (2008), 77–93.

12. Breese, J.; Heckerman, D.; and Kadie, C. Empirical analysis of predictive algorithms for collaborative filtering. Proceedings of the Fourteenth Conference on Uncertainty in AI. Madison, WI: Morgan Kaufmann, 1998, 43–52.

13. Cao, Y., and Li, Y. An intelligent fuzzy-based recommendation system for consumer electronic products. Expert Systems with Applications, 32 (2007), 230–240.

14. Chen, Y.; Harper, F.M.; Konstan, J.; and Li, S.X. Social comparisons and contributions to online communities: A field experiment on MovieLens. American Economic Review, 100 (2010), 1358–1398.

15. Crum, R. Personalization: Telling e-tail customers what they really want. E-Commerce Times, June 20, 2008.

16. Dewan, R.; Jing, B.; and Seidmann, A. Product customization and price competition on the Internet. Management Science, 49, 8 (2003), 1055–1070.

17. Fleder, D., and Hosanagar, K. Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Science, 55,5 (2009), 697–712.

18. Gutierrez, G.J., and He, X. Life-cycle channel coordination is sues in launching an innovative durable product. Production and Operations Management, 20, 2 (2011), 268–279.

19. Harper, F.M.; Li, X.; Chan, Y., and Konstan, A. An economic model of user rating in an online recommender systems. Proceedings of the Tenth International Conference on User Modeling. Edinburgh 2005, 307–315.

20. He, X.; Prasad, A.; and Sethi, S.P. Co-op advertising and pricing in a stochastic supply chain: Feedback stackelberg strategies. Production and Operations Management, 18, 1 (2009), 78–94.

21. Hinz, O., and Eckert, J. The impact of search and recommendation systems on sales in electronic commerce. Business and Information Systems Engineering, 2, 2 (2002), 67–77.

22. Konstan, J.A., and Riedl, J. Recommender systems: From algorithms to user experience. User Modeling and User-Adapted Interaction, 22, 1–2 (2012), 101–123.

23. Koren, Y. Collaborative filtering with temporal dynamics. Communications of the ACM, 53, 4 (2010), 89–97.

24. Koren, Y.; Bell, R.; and Volinsky, C. Matrix factorization techniques for recommender systems. IEEE Computer, 42, 8, August 2009, 42–49.

25. Kramer, T.; Spolter-Weisfeld, S.; and Thakkar, M. The effect of cultural orientation on consumer responses to personalization. Marketing Science, 26, 2 (2007), 246–258.

26. Leavitt, N. Recommendation technology: Will it boost e-commerce? IEEE Computer, 39, 5, May 2006, 13–16.

27. Lewis, M. The influence of loyaly program and short-term promotions on customer retention. Journal of Marketing Research, 41, 3 (2004), 281–292.

28. Lovett, J. Personalization hat trick: Revenue, loyalty and conversion. E-commerce Times, February 2, 2007.

29. Mendelson, H., and Parlaktürk, A.K. Product-line competition vs. proliferation. Management Science, 54, 12 (2008), 2039–2053.

30. Meyer-Waarden, L. The influence of loyalty programme membership on customer purchase behaviour. European Journal of Marketing, 42, 1/2 (2008), 87–114.

31. Mookerjee, V.; Mookerjee, R.; Bensoussan, A.; and Yue, W.T. When hackers talk: Managing information security under variable attack rates and information dissemination. Information Systems Research, 22, 3 (2011), 606–623.

32. Moon, J.; Chadee, D.; and Tikoo, S. Culture, product type, and price influences on consumer purchase intention to buy personalized products online. Journal of Business Research, 61, 1 (2008), 31–41.

33. Moorthy, K.S. Product and price competition in a duopoly. Marketing Science, 7, 2 (1988), 141–168.

34. Murthi, B.P.S., and Sarkar, S. The role of the management sciences in research on personalization. Management Science, 49, 10 (2003), 1344–1362.

35. Nasraoui, O., and Saka, E. Web usage mining in noisy and ambiguous environments: Exploring the role of concept hierarchies, compression, and robust user profiles. From Web to Social Web: Discovering and Deploying User and Content Profiles Lecture Notes in Computer Science, 4737, (2007), 82–101.

36. Nikolaeva, R., and Sriram, S. The moderating role of consumer and product characteristics on the value of customized on-line recommendations. International Journal of Electronic Commerce, 11, 2 (2006), 101–123.

37. Ozmen, D. Information transmission and recommender systems. Available at http:// www.princeton.edu/smorris/pdfs/PhD/Ozmen.pdf (accessed September 26, 2013).

38. Pathak, B.; Garfinkel, R.; Gopal, R.D.; Venkatesan, R.; and Yin, F. Empirical analysis of the impact of recommender systems on sales. Journal of Management Information Systems, 27 (2010), 159–188.

39. Park, S.H., and Han, S.P. From accuracy to diversity in product recommendations: Relationship between diversity and customer retention. International Journal of Electronic Commerce, 18, 2 (2013), 51–72.

40. Resnick, P., and Varian, H. Recommender systems. Communications of the ACM, 40, 3 (1997), 56–58.

41. Sahoo, N.; Singh, P.; and Mukhopadhyay, T. A hidden Markov model for collaborative filtering. MIS Quarterly, 36, 4 (2012), 1329–1356.

42. Schafer, J.B.; Konstan, J.A.; and Riedl, J. E-commerce recommendation applications. Data Mining and Knowledge Discovery, 5 (2001), 115–153.

43. Sethi, S.P., and Thompson, G.L. Optimal Control Theory: Applications to Management Science and Economics. Boston: Kluwer Academic, 2000.

44. Smith, M.D., and Brynjolfsson, E. Consumer decision-making at an Internet shopbot: Brand still matters. Journal of Industrial Economics, 49, 4 (2001), 541–558.

45. Stone, B. Making sense of new prices on Apple’s iTunes. New York Times, April 7, 2009. 46. Suryavanshi, B.S.; Shiri, N.; and Mudur, S.P. Improving the effectiveness of model based

recommender systems for highly sparse and noisy web usage data. Proceedings of the 2005 IEEE/ WIC/ACM International Conference on Web Intelligence (WIACM05), 2005, 618–621.

47. Syam, N.; Ruan, R.; and Hess, J.D. Customized products: A competitive analysis. Marketing Science, 24, 4 (2005), 569–584.

48. Syam, N., and Kumar, N. On customized goods, standard goods, and competition. Marketing Science, 25, 5 (2006), 525–537.

49. Tam, K.Y., and Ho, S.Y. Web personalization as a persuasion strategy: An elaboration likelihood model perspective. Information Systems Research, 16, 3 (2005), 271–291.

50. U.S. Census Bureau. Quarterly Retail E-commerce Sales: 4th quarter 2013. February 18, 2014. Available at www.census.gov/retail/mrts/www/data/pdf/ec\_current.pdf (accessed March 6, 2014).

51. Villas-Boas, J.M. Consumer learning, brand loyalty, and competition. Marketing Science, 23, 1 (2004), 134–145.

52. Wattal, S.; Telang, R.; and Mukhopadhyay, T. Information personalization in a two dimensional product differentiation model. Journal of Management Information Systems, 26, 2 (2009), 69–95.

53. Yu, E. Consumer electronics retailers at risk of fading into oblivion. April 2012. Available at www.zdnet.com/consumer-electronics-retailers-at-risk-of-fading-into-oblivion-2062304530/ (accessed July 23, 2013).

## Appendix

## Part A

Proofs of Lemmas, Propositions, and Corollaries

A.1 Proof of Lemma 1: By differentiating the solution of Equation (2) with respect to <sup>u</sup> and equating the resulting expression to 0, we obtain the required expression in the lemma. The condition for the duopoly is derived using $0 \leq u \leq 1 , 2 x - B < 0$ , and $\begin{array} { r } { x = \frac { a u } { \beta } } \end{array}$

A.2 Proof of Lemma 2: From Equations (6) and (7), we get:

$$
\frac {d \Pi_ {1}}{d q _ {1}} = \frac {(r + 2 \beta) (B \alpha - 2 q _ {1} (r + \beta) + (r + \beta) (q _ {2} + \gamma))}{4 \alpha^ {2}} = 0, \text { and }\tag{19}
$$

$$
\frac {d \Pi_ {2}}{d q _ {2}} = 1 + \frac {(r + 2 \beta) (- B \alpha + (r + \beta) (q _ {1} - 2 q _ {2} - \gamma))}{4 \alpha^ {2}} = 0.\tag{20}
$$

By solving Equations (19) and (20), we obtain the expressions for $q _ { 1 } ^ { * }$ and $q _ { 2 } ^ { * }$ . Then, using Equation (5), we obtain the optimal value of <sup>u</sup>. Next, we derive the conditions for maintaining a market with duopoly. First, the fit cost should be decreasing and convex. Therefore, $\begin{array} { r } { - B + 2 x \le 0 . \mathrm { A t } t \to \infty , x = \frac { \alpha u } { \mathrm { B } } } \end{array}$ : Hence $\begin{array} { r } { \frac { 2 \alpha u } { \beta } < B , } \end{array}$ and, therefore:

$$
\frac {4 \alpha^ {2} + (r + \beta) (r + 2 \beta) \gamma}{4 \alpha \beta} <   B.\tag{21}
$$

Next, $u < 1$ provides the following condition:

$$
B <   \frac {8 \alpha^ {2} - (r + \beta) (r + 2 \beta) \gamma}{2 \alpha \beta}.\tag{22}
$$

A.3 Proof of Proposition 1:

$$
\frac {d u ^ {*}}{d \alpha} = - \frac {(r + 2 \beta) (B \alpha + 2 (r + \beta) \gamma)}{1 2 \alpha^ {3}} \text {and} \frac {d x ^ {*}}{d \alpha} = \frac {4 \alpha^ {2} - (r + \beta) (r + 2 \beta) \gamma}{1 2 \alpha^ {2} \beta}.
$$

It is evident that $\scriptstyle { \frac { d u ^ { * } } { d \alpha } } < 0$ . Using Equations (21) and (22), we find that $\begin{array} { r } { \frac { d x ^ { * } } { d \alpha } > 0 } \end{array}$ . Next, we obtain:

$$
\frac {d ^ {2} u ^ {*}}{d \alpha^ {2}} = \frac {2 \beta B + r B}{6 \alpha^ {3}} + \frac {(r + \beta) (r + 2 \beta) \gamma}{2 \alpha^ {3}} > 0 \text {and} \frac {d ^ {2} x ^ {*}}{d \alpha^ {2}} = \frac {(r + \beta) (r + 2 \beta) \gamma}{6 \alpha^ {3} \beta} > 0.
$$

From Equations (10) and (11), we find that:

$$
\frac {d q _ {1} ^ {*}}{d \alpha} = \frac {8 \alpha + r B + 2 B \beta}{3 (r + \beta) (r + 2 \beta)}, \text { and }
$$

$$
\frac {d \Pi_ {1} ^ {*}}{d \alpha} = \frac {(4 \alpha^ {2} - (r + \beta) (r + 2 \beta) \gamma) (4 \alpha^ {2} + B \alpha (r + 2 \beta) + (r + \beta) (r + 2 \beta) \gamma)}{1 8 \alpha^ {3} (r + \beta) (r + 2 \beta)}.
$$

From Equations (21) and (22), we obtain $\frac { d q _ { 1 } ^ { * } } { d { \bf a } } > 0$ and $\begin{array} { r } { \frac { d \Pi _ { 1 } ^ { * } } { d { \bf a } } > 0 } \end{array}$ . Now, given that $u ^ { * } { < } 1$ , from Equations (12) and (13), we obtain:

$$
\frac {d q _ {2} ^ {*}}{d \alpha} = \frac {1 6 \alpha - B (r + 2 \beta)}{3 (r + \beta) (r + 2 \beta)}.
$$

Since $\textstyle \left( 1 - u ^ { * } \right) > 0 , \frac { d q _ { 2 } ^ { * } } { d { \bf a } } > 0$ . Since $( 1 - u ^ { * } )$ and $q _ { 2 } ^ { * }$ both increase with increase in ${ \mathfrak { a } } ,$ $\Pi _ { 2 } ^ { * }$ also increases with increase in α.

A.4 Proof of Proposition 2: From Equation (8):

$$
\frac {d u ^ {*}}{d \beta} = \frac {B}{6 \alpha} + \frac {\gamma (3 r + 4 \beta)}{1 2 \alpha^ {2}} > 0 \text { and } \frac {d ^ {2} u ^ {*}}{d \beta^ {2}} = \frac {\gamma}{3 \alpha^ {2}} > 0.\tag{23}
$$

Equation (9) gives:

$$
\frac {d x ^ {*}}{d \beta} = \frac {- 4 \alpha^ {2} + 2 \beta^ {2} \gamma}{1 2 \beta^ {2} \alpha} - \frac {B r}{1 2 \beta^ {2}} - \frac {r ^ {2} \gamma}{1 2 \alpha \beta^ {2}} \text {and} \frac {d ^ {2} x ^ {*}}{d \beta^ {2}} = \frac {2 \alpha}{3 \beta^ {3}} + \frac {B r}{6 \beta^ {3}} + \frac {r ^ {2} \gamma}{6 \alpha \beta^ {3}}.
$$

From Equations (21) and (22), we obtain $- 4 \alpha ^ { 2 } + 2 \beta ^ { 2 } \gamma < 0$ : Therefore, $\begin{array} { r } { \frac { d x ^ { * } } { d \beta } < 0 } \end{array}$ : It is evident that $\textstyle { \frac { d ^ { 2 } x ^ { * } } { d \beta ^ { 2 } } } > 0$ . Next, Equation (10) gives:

$$
\frac {d q _ {1} ^ {*}}{d \beta} = \frac {- \alpha}{3 (r + \beta) ^ {2} (r + 2 \beta) ^ {2}} \left[ B (r + 2 \beta) ^ {2} + 4 \alpha (3 r + 4 \beta) \right].
$$

It is evident that $\begin{array} { r } { \frac { d q _ { 1 } ^ { * } } { d \beta } < 0 } \end{array}$ . Since both <sup>u</sup> and $q _ { 1 } ^ { * }$ decrease with increase in $\beta , \Pi _ { 1 } ^ { * }$ also decreases. From Equations (12), (13), and (23), we obtain:

$$
\frac {d q _ {2} ^ {*}}{d \beta} = \frac {4 \alpha^ {2}}{(r + \beta) ^ {2} (r + 2 \beta)} \left[ - (r + \beta) (r + 2 \beta) \frac {d u}{d \beta} - (1 - u) (3 r + 4 \beta) \right] <   0, \text { and }
$$

$$
\frac {d \Pi_ {2} ^ {*}}{d \beta} = \frac {- (1 - u) [ B r \alpha (r + 2 \beta) + (3 r + 4 \beta) (8 \alpha^ {2} + (r + \beta) (r + 2 \beta) \gamma) ]}{(r + \beta) ^ {2} (r + 2 \beta) ^ {2}} <   0.
$$

A.5 Proof of Remark 1: From Equations (8) and (9):

$$
\frac {d u ^ {*}}{d \gamma} = \frac {(r + 2 \beta) (r + \beta)}{1 2 \alpha^ {2}} > 0 \text { and } \frac {d x ^ {*}}{d \gamma} = \frac {(r + 2 \beta) (r + \beta)}{1 2 \alpha \beta} > 0.
$$

Similarly, from Equations (10), (11), (12), and (13):

$$
\frac {d q _ {1} ^ {*}}{d \gamma} = \frac {1}{3}, \frac {d q _ {2} ^ {*}}{d \gamma} = - \frac {1}{3}, \frac {d \Pi_ {1} ^ {*}}{d \gamma} = \frac {2 u}{3} > 0, \text { and } \frac {d \Pi_ {2} ^ {*}}{d \gamma} = - \frac {2 (1 - \hat {u})}{3} <   0.
$$

A.6 Proofs of Lemma 3 and Lemma 4: The equilibrium solution can be derived by following the steps explained in the proofs of Lemma 3.1.4 and Lemma 3.2. Also, we can derive the conditions for duopoly in a similar manner:

A.7 Proof of Proposition 3: By taking the first order derivative of $u ^ { * }$ in Equation (15) with respect to $k ,$ we get:

$$
\frac {d u ^ {*}}{d k} = \frac {(r + \beta) (r + 2 \beta) (- 1 + 3 \gamma_ {1})}{1 2 \alpha^ {2}}.
$$

By comparing this expression with zero, we can easily derive the desired result.

A.8 Proof of Lemma 5: The customer solves the following surplus maximization problem:

$$
\begin{array}{l} \max _ {u (t)} \int_ {0} ^ {\infty} [ R - u (t) (A + x (t) ^ {2} - B x (t) + q _ {1}) \\ \quad - (1 - u (t)) (A + x (t) ^ {2} - B x (t) + q _ {2} + k \gamma_ {1}) ] e ^ {- r t} d t \end{array}
$$

subject to:

$$
\dot {x} = \alpha u (t) - \beta x (t); 0 \leq u (t) \leq 1.
$$

The Hamiltonian for this problem is:

$$
\begin{array}{l} H = R - \big [ u (t) (A + x (t) ^ {2} - B x (t) + q _ {1}) \\ \qquad + (1 - u (t)) (A + x (t) ^ {2} - B x (t) + k \gamma_ {1} + q _ {2}) \big ] + \lambda (t) (\alpha u (t) - \beta x (t)), \end{array}
$$

where $\lambda ( t )$ is the adjoint variable. Therefore:

$$
H _ {u} = - q _ {1} + k \gamma_ {1} + q _ {2} + \lambda \alpha , \text {   and   } H _ {x} = - 2 x + B - \lambda \beta .\tag{24}
$$

Now the adjoint equation can be written as [see 43]:

$$
\dot {\lambda} = \lambda r - H _ {x} = \lambda (r + \beta) + 2 x - B.\tag{25}
$$

In the long-run stationary equilibrium, all motion ceases and the following conditions must be satisfied $[ 6 , 4 3 ] \colon { \dot { x } } = 0 , { \dot { \lambda } } = 0$ and $H _ { u } = 0$ . Let the values of <sup>x</sup>, <sup>u</sup>, and λ in the long-run stationary equilibrium be ^<sup>x</sup>, ^<sup>u</sup>, and $\hat { \lambda } ,$ , respectively. Now, by setting ${ \dot { x } } = 0$ in Equation (3), the optimal profile can be expressed in terms of $\hat { u }$ as:

$$
\hat {x} = \frac {\alpha \hat {u}}{\beta}.\tag{26}
$$

Next, setting $\dot { \lambda } = 0$ in Equation (25) and $H _ { u } = 0$ in Equation (24) gives:

$$
\hat {u} = \frac {B \beta}{2 \alpha} - \frac {\beta (\beta + r)}{2 \alpha^ {2}} (q _ {1} - q _ {2} - k \gamma_ {1}).\tag{27}
$$

Therefore, from Equation (26):

$$
\hat {x} = \frac {B}{2} - \frac {(\beta + r)}{2 \alpha} (q _ {1} - q _ {2} - k \gamma_ {1}).\tag{28}
$$

Now we need to check the second-order Legendre–Clebsch condition in order to ensure that the objective function is maximized at ^<sup>u</sup> and ^<sup>x</sup> derived above [43]. Hence, from (24) and (25):

$$
\ddot {H} _ {u} = \ddot {\lambda} \alpha \text {   and   } \ddot {\lambda} = (r + \beta) ((r + \beta) \lambda + 2 x - B) + 2 (\alpha u - \beta x).
$$

Therefore,

$$
\ddot {H} _ {u} = \alpha [ (r + \beta) ((r + \beta) \lambda + 2 x - B) + 2 (\alpha u - \beta x) ].
$$

Finally,

$$
\frac {\partial}{\partial u} \left(\ddot {H} _ {u}\right) = 2 \alpha^ {2} \geq 0.
$$

The objectives of the two firms are to maximize the following objective functions:

$$
\max _ {q _ {1}} \Pi_ {1} = \int_ {0} ^ {1} \hat {u} q _ {1} d \gamma_ {1}, \text {   and   } \max _ {q _ {2}} \Pi_ {2} = \int_ {0} ^ {1} (1 - \hat {u}) q _ {2} d \gamma_ {1}.
$$

We can obtain the optimal values of $q _ { 1 }$ and $q _ { 2 } ( \mathrm { i } . \mathrm { e } . , \ : q _ { 1 } ^ { * }$ and $q _ { 2 } ^ { * } ,$ , respectively) by taking the first-order conditions of the objective functions and solving them simultaneously. These optimal values are:

$$
q _ {1} ^ {*} = \frac {4 \alpha^ {2} + 2 B \alpha \beta + k \beta (r + \beta)}{6 \beta (r + \beta)}, \text {   and   } q _ {2} ^ {*} = \frac {8 \alpha^ {2} - 2 B \alpha \beta - k \beta (r + \beta)}{6 \beta (r + \beta)}.\tag{29}
$$

Now we check the conditions for maxima:

$$
\frac {d ^ {2} \Pi_ {1}}{d q _ {1} ^ {2}} = - \frac {\beta (r + \beta)}{\alpha^ {2}} <   0, \text {   and   } \frac {d ^ {2} \Pi_ {2}}{d q _ {2} ^ {2}} = - \frac {\beta (r + \beta)}{\alpha^ {2}} <   0.
$$

Hence, $q _ { 1 } ^ { * }$ and $q _ { 2 } ^ { * }$ (see Equation [29]) provide equilibrium profits for the firms. These profits for personalizing and non-personalizing firms are:

$$
\begin{array}{l} \Pi_ {1} ^ {*} = \frac {(4 \alpha^ {2} + 2 B \alpha \beta + k \beta (r + \beta)) ^ {2}}{7 2 \alpha^ {2} \beta (r + \beta)}, \text { and } \\ \Pi_ {2} ^ {*} = \frac {(8 \alpha^ {2} - 2 B \alpha \beta - k \beta (r + \beta)) ^ {2}}{7 2 \alpha^ {2} \beta (r + \beta)}, \text { respectively }. \end{array}
$$

Next, we derive the conditions for maintaining a market with duopoly. First, the fit cost should be decreasing and convex. Therefore, $2 \hat { x } - B < 0$ for $\boldsymbol { \gamma } _ { 1 } \in [ 0 , 1 ]$ . We know that ^<sup>x</sup> is increasing in $\gamma _ { 1 }$ . Therefore, the limiting case is $2 \hat { x } - B < 0$ for $\gamma _ { 1 } = 1$ Hence, using Equations (28) and (29), we get:

$$
2 \alpha^ {2} - 2 B \alpha \beta + 2 k \beta (r + \beta) <   0.
$$

For $\gamma _ { 1 } = 0 , \ \hat { u } > 0$ . Therefore, from Equations (27) and (29):

$$
2 \alpha^ {2} + B \beta \alpha - k \beta (r + \beta) > 0.
$$

Finally, by setting $\hat { u } < 1$ at $\gamma _ { 1 } = 1$ in Equation (27) and using Equation (29), we get:

$$
- 4 \alpha^ {2} + B \beta \alpha - 2 k \beta (r + \beta) <   0.
$$

A.9 Proof of Proposition 4: Surplus of a customer is:

$$
S = R - \left[ \hat {u} \left(A + \hat {x} ^ {2} - B \hat {x} + q _ {1} ^ {*}\right) + (1 - \hat {u}) \left(A + \hat {x} ^ {2} - B \hat {x} + q _ {2} ^ {*} + k \gamma_ {1}\right) \right].
$$

By differentiating <sup>S</sup> with respect to α using the results in Lemma 5.3.1, we can easily derive the condition given in the proposition.

A.10 Proof of Lemma $_ 6 \colon$ The Hamiltonian for the customer’s problem can be written as:

$$
\begin{array}{l} H = R - \left[ A + x (t) ^ {2} - B x (t) + q _ {1} u (t) + (q _ {2} + k \gamma_ {1} + m \gamma_ {2} x) (1 - u (t)) \right] \\ \quad + \lambda (t) (\alpha u (t) - \beta x (t)). \end{array}
$$

Using this Hamiltonian, we can obtain the equilibrium solution in a manner similar to the earlier scenario. The rest of the proof is similar to the proof of Lemma 5.3.1.

A.11 Proof of Proposition 5: By differentiating ^<sup>u</sup> in Equation (17) and and - in Equation (18) with respect to <sup>m</sup>, we obtain the desired conditions.

## Part B

Table A1. Summary of Results

<table><tr><td></td><td>Increases in the value of parameter</td><td>Results</td></tr><tr><td rowspan="9">Purchase rate does not vary with time</td><td colspan="2">Homogeneous customers</td></tr><tr><td>Recommender system effectiveness</td><td>Decreases the rate of purchase from the personalizing firm, improves profile quality, increases prices and profits of both firms</td></tr><tr><td>Profile loss parameter</td><td>Increases the rate of purchase from the personalizing firm, decreases profile quality, decreases prices and profits of both firms</td></tr><tr><td>Additional fit cost</td><td>Increases the rate of purchase from the personalizing firm, increases the price and profit of the personalizing firm, and decreases the price and profit of the non-personalizing firm</td></tr><tr><td colspan="2">Customers are heterogeneous in the additional fit cost</td></tr><tr><td colspan="2">Additional fit cost does not depend on the profile</td></tr><tr><td>Maximum additional fit cost</td><td>Customers with relatively low sensitivity to substitution purchase less from the personalizing firm, whereas other customers (i.e., those with relatively high sensitivity) purchase more from the personalizing firm</td></tr><tr><td colspan="2">Additional fit cost depends on the profile</td></tr><tr><td>Profile cost increment parameter</td><td>Customers purchase more from the personalizing firm, and profits and prices of both the firms decrease</td></tr><tr><td rowspan="5">Purchase rate varies over time</td><td colspan="2">Customers are heterogeneous in the additional fit cost</td></tr><tr><td colspan="2">Additional fit cost does not depend on the profile</td></tr><tr><td>Recommender system effectiveness</td><td>Customer surplus increases under certain conditions</td></tr><tr><td colspan="2">Additional fit cost depends on the profile</td></tr><tr><td>Profile cost increment parameter</td><td>Customers purchase more from the personalizing firm under certain conditions, and profit of the personalizing firm increases under certain conditions</td></tr></table>
