---
otero_id: 25458
otero_key: "HTT6JP26"
title: "Platform Policies and Sellers’ Competition in Agency Selling in the Presence of Online Quality Misrepresentation"
authors: "Jingchuan Pu; Tingting Nian; Liangfei Qiu; Hsing Kenneth Cheng"
year: "2022"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.2023410"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Platform Policies and Sellers’ Competition in Agency Selling in the Presence of Online Quality Misrepresentation

Jingchuan Pu, Tingting Nian, Liangfei Qiu & Hsing Kenneth Cheng

To cite this article: Jingchuan Pu, Tingting Nian, Liangfei Qiu & Hsing Kenneth Cheng (2022) Platform Policies and Sellers’ Competition in Agency Selling in the Presence of Online Quality Misrepresentation, Journal of Management Information Systems, 39:1, 159-186, DOI: 10.1080/07421222.2021.2023410

To link to this article: https://doi.org/10.1080/07421222.2021.2023410

![](/api/attachments/HTT6JP26/fulltext/images/b849daef056b19441cb6cce9b042f2bf87626cdd46dd56de1ba351e876e9630b.jpg)

View supplementary material

![](/api/attachments/HTT6JP26/fulltext/images/e0c84327dc2c079466024f0690b4b621beb9fd68ba7ca68eab27e738851ae669.jpg)

Published online: 11 Apr 2022.

![](/api/attachments/HTT6JP26/fulltext/images/4eba4060109fb2f5c6908d2b1dda398715c2a47f99af386b4be5f222394d9f8f.jpg)

Submit your article to this journal

![](/api/attachments/HTT6JP26/fulltext/images/a5dff56747e10b5ff2da005b9b09dfad5d7fee53ca160bdc37565cb6474b259d.jpg)

Article views: 342

![](/api/attachments/HTT6JP26/fulltext/images/7513c6f0d8c5af6f79c1164b31966979367e00c4e1e5aa482aa068e61d2afb36.jpg)

View related articles

![](/api/attachments/HTT6JP26/fulltext/images/6653ee9405f2cd4e8671575a9287fa1b5204e9f0e821ac4b95b4d06602c2c558.jpg)

View Crossmark data

Check for updates

# Platform Policies and Sellers’ Competition in Agency Selling in the Presence of Online Quality Misrepresentation

Jingchuan Pu<sup>a</sup>, Tingting Nian<sup>b</sup>, Liangfei Qiu <sup>a</sup>, and Hsing Kenneth Cheng<sup>a</sup>

<sup>a</sup>Department of Information Systems and Operations Management, Warrington College of Business, University of Florida, Gainesville, FL, USA; <sup>b</sup>The Paul Merage School of Business, University of California, Irvine, Irvine, CA, USA

## ABSTRACT

On e-commerce platforms, consumers rely heavily on online reviews, sales volume, and social media discussions to infer product quality. As a result, the past decade has witnessed an explosive growth of sellerinitiated misrepresentation of quality through fake reviews, fake sales, and fake posts. We develop an analytical model to investigate sellers’ competition in quality misrepresentation in agency pricing and the platform’s policies. The platform can discourage sellers’ quality misrepresentations by increasing the cost of misrepresentation or implementing a more lenient product return policy. We find that while a stricter anti-misrepresentation policy deters the misrepresentation of the high-quality seller, such a strategy may unintendedly incentivize the low-quality seller to misrepresent the quality more. Furthermore, increasing return leniency deters low-quality seller’s misrepresentation in a wider range of market conditions than increasing the misrepresentation cost. We show sellers’ online quality misrepresentation behaviors in a competitive setting, and our results have practical implications for platform policies.

## KEYWORDS

E-commerce platforms; quality misrepresentation; agency selling; product returns; online reviews; platform policies; analytical modeling; online platforms

## Introduction

On e-commerce platforms, information on peer consumers’ activities (e.g., sales and clicks volume) and opinions (e.g., online reviews and discussions on social media) can help potential consumers better assess product quality [13]. With such information playing a critical role in consumers’ purchase decisions, it is increasingly common for sellers to hire freelancers or companies to misrepresent product quality by manipulating product reviews, sales, or clicks on the platforms [41, 44]. The average cost of posting one five-star review can be as low as \$1.29 [67] and it only takes hours to uncover more than 10,000 unverified reviews on 24 pairs of headphones on the Amazon marketplace [9]. Moreover, sellers on the Amazon marketplace are willing to pay \$10,000 a month to generate fake sales or clicks [52], and five hundred million sales in 2013 are found to be fake on Taobao, the largest online marketplace in China [71]. In an extreme case, 99.73 percent of the sellers on an undisclosed online marketplace have fake sales [70]. Google and other advertising platforms also face an increase in fraudulent trafic. Adobe finds that about 28 percent of trafic across thousands of its clients’ websites is potentially from fake clicks. Many sellers are experts on using fake sales or clicks to get the “Amazon Choice” badge (a badge signaling good quality) [54, 67].

A platform is usually a two-sided, or multi-sided market, in which the platform enables interactions between users on each side [64]. On the one hand, the platform earns profit, such as commissions of users’ transactions on the platform [11, 60]. On the other hand, the platform needs to improve the quality of services on the platform and maintain the reliability of information from each side [6, 56]. In this light, the platform can have multiple objectives, and how to prioritize one over the others depends on other factors (not within this study’s scope), such as the stage of the platform or its competitive environment. For instance, Amazon originally allows the sellers to generate reviews by sending free products to incentivize customers and positively bias customers’ opinions, possibly because doing so can increase sellers’ revenue and help Amazon earn profit [59]. The incentivized reviews enable the sellers to misrepresent the product quality [63]. In October 2016, Amazon implemented a strict policy and completely banned the incentivized reviews, to build a reliable review system with authentic reviews [57]. To maintain the integrity of the information provided to consumers, apart from making profits from the commissions, platforms implement diferent measures to discourage sellers’ quality misrepresentation [2, 38]. TripAdvisor allows consumers to flag suspicious reviews. Amazon, Walmart, Yelp, and other e-commerce platforms try to tackle the problem by developing advanced algorithms to detect fake reviews and fight against fake sales [67].

Given the ubiquity of quality misrepresentation, we focus on the following questions: under what market conditions will competing sellers choose to misrepresent the quality signals? What is the impact of the existence of quality misrepresentation on the competing sellers and platform? When sellers choose to compete on prices and misrepresentation levels, how do anti-misrepresentation strategies afect the competing sellers and platforms?

To answer these questions, we develop an analytical model in which two sellers compete for consumers that are heterogeneous in their horizontal preferences, denoted by seller H, who sells a high-quality product and seller L, who sells a low-quality product. The two sellers compete on the same platform, deciding prices and whether, and to what extent, to manipulate the quality signals of their products. The platform acts as a marketplace and adopts an agency pricing model for these two sellers. The platform takes a proportion of the sellers’ revenues as a commission fee [46, 53].

Sellers encounter the cost when they manipulate the quality signals, such as the cost of registering fake accounts, the transaction fees of fake sales, and the cost of hiring freelancers. Another natural cost of quality misrepresentation is that fake information will inevitably increase product returns. Consumers might be misled by the manipulated quality information at the pre-purchase stage, but they can assess the quality more accurately after receiving the product. That is, a systematic discrepancy between the perceived quality and the actual quality leads to more product returns. Therefore, the platform can either increase the misrepresentation cost or adopt a more lenient return policy to discourage quality misrepresentation.

Our analyses capture the current practice where sellers compete in both price [42] and misrepresentation in the online marketplace [71]. In the existing studies that analyze sellers quality misrepresentation in a monopoly setting [20] or a competitive setting where sellers only compete on misrepresentation level [19, 49], sellers’ misrepresentation levels always decrease as the cost of misrepresentation increases. However, we analyze a more realistic situation where sellers compete on both price and quality misrepresentation, finding the misrepresentation level of the low-quality seller can increase with the misrepresentation cost under certain market conditions.

Moreover, to the best of our knowledge, no prior work has investigated the product return policy as a tool for the platforms to discourage quality misrepresentation. Adopting a more lenient return policy does not directly increase the cost of quality misrepresentation, but it discourages such behavior because the greater discrepancy between the ex-ante perceived quality (misleading quality information) and the actual quality naturally leads to more product returns.

Our findings ofer some important managerial implications. First, we find that when the level of return policy leniency is suficiently low, both sellers choose to misrepresent quality and the cases where only one seller chooses to manipulate are not pure-strategy Nash equilibria. The result reminds the platforms of the importance of a lenient return policy, as all sellers are potentially incentivized to manipulate quality signals if consumers are reluctant to return products. Second, we find that quality misrepresentation has diferent impacts on the competing sellers. While the high-quality seller can benefit from the existence of quality misrepresentation under certain market conditions, the low-quality seller’s profit is always lower than that of the case where there is no quality misrepresentation. Third, we show that stricter anti-misrepresentation strategies may unexpectedly incentivize the low-quality seller to invest more on manipulating quality information. Although the platform can make quality misrepresentation more expensive for sellers, creating a direct cost efect, there is also an indirect competition efect: both sellers use quality misrepresentation as a competitive tool, and an increase in cost simultaneously afects both sellers’ decisions about misrepresentation levels and prices. While the direct cost efect always dominates the indirect competition efect for the high-quality seller, the indirect competition efect can dominate the direct cost efect for the low-quality seller. Forth, increasing return leniency can deter low-quality seller’s quality misrepresentation level in a wider range of market conditions than increasing the misrepresentation cost. Last but not least, our results suggest that the platform shall choose anti-misrepresentation strategies based on its specific objective. Taken together, the results provide important and useful guidance to practitioners on the quality misrepresentation of diferent sellers, and the efects of anti-misrepresentation strategies.

## Literature Review

## Quality Misrepresentation

Many online platforms and online marketplaces (e.g., Amazon and eBay) are characterized by information asymmetry, which leaves great room for the sellers to manipulate information so as to cater to their own interests. Sellers may provide no information, partial information, or even false information about the product attributes. Providing false quality claims can be a highly efective way to create an incorrect belief about the product, making consumers believe that the product quality is higher than it truly is [31]. Compared to the substantial literature on truthful quality disclosure [27], the body of research focusing on firms’ incentives to manipulate information is relatively smaller [26].

Studies in the fields of information systems (IS) and marketing consistently show that online quality signals are influential information sources. Consumers rely heavily on online reviews, sales, clicks, and discussions on social media to evaluate products because these attributes are treated as convincing signals of product quality [23, 75]. It is unsurprising, then, that business owners have been found to strategically manipulate these quality signals [40]. For instance, Mayzlin et al. [49] compare online review ratings across two platforms (Expedia and TripAdvisor), finding that competitive conditions are associated with the intensity of fake reviews. Movie studios also manipulate social media sentiment around the time movies are released, and manipulation is more likely to occur for independent productions and low-budget movies [44]. In an extreme case, Wang et al. [70] show that 99.73 percent of the sellers on one undisclosed platform have posted fake sales to manipulate this quality signal.

The great influence of quality signals on consumers and the prevalence of quality misrepresentation have prompted scholars to examine sellers’ incentives and strategies for quality misrepresentation [20, 48]. Although previous studies provide some important results about sellers’ misrepresentations of quality, they mainly focus on the monopoly case [20] or the case where sellers only compete on quality misrepresentation [19, 49]. To the best of our knowledge, no previous study examines a scenario where the sellers compete on both quality misrepresentation and retail price. Our analyses indicate that in the agency pricing regime, when there are strategic interactions between sellers’ price decisions and quality misrepresentation decisions, the existence of quality misrepresentation (and the platform’s anti-misrepresentation strategies) can have very diferent (even opposing) efects on the diferent competing sellers.

## Product Return Policy

One consumer response to quality misrepresentation is to return the purchased product because of the dissatisfaction stemming from the gap between the ex-ante perceived quality and the actual quality experienced in the post-purchase stage. Prior research has identified several factors that explain consumers’ dissatisfaction, such as defects, product incompatibility with user needs, and deficiencies in product performance relative to customer expectation [25]. Che [10] and Shulman et al. [66] establish the optimal refund policies for product returns based on consumers’ post-purchase utility realization. Several other papers highlight diferent functions of product return policies. Lenient return policies, despite leading to increases in product returns [17], could reduce the perceived purchase risk, increase purchases in the short run [4] and in the long run [58]. Finally, Su [68] shows the efects of return policies on supply chain performance and demonstrates that return policies may distort incentives under common supply contracts.

Studies in the IS literature have found that the number of product returns in online purchases is positively related to the level of disconfirmation of pre-purchase expectations [18, 33]. For example, Sahoo et al. [65] show that the precision of information from product reviews (number of reviews and helpful reviews) can influence the return probabilities. De et al. [18] indicate that product-oriented web technologies can decrease product returns by mitigating the diference between consumers’ pre-purchase evaluation and their postpurchase realization. Similarly, using IT artifacts, presenting more product-related information [33], and using ofline channels [39] can help reduce product returns by decreasing the discrepancy between consumers’ pre- and post-purchase evaluations.

The answers to our research questions cannot simply be inferred from the extant literature on product return policies. In our research context, the product return is not due to product misfit or consumer uncertainty but the systematic gap between the perceived quality (manipulated by the sellers) and the true quality. While existing studies focus on the efects of return policies on firms’ performance and how to reduce product returns by mitigating consumers’ uncertainty, we examine the function of return policies in discouraging the sellers’ misrepresentation behaviors.

## Model Setup

We focus on the agency model in this study to reflect the current practice of sellers deciding both prices and quality misrepresentation levels in the online marketplace. Following the literature [50, 72], we assume the market to be fully covered. In our model, the high- and low-quality sellers compete in retail prices and misrepresentation levels to reach the end consumers. Consumers are heterogeneous in their preferences for products’ horizontal attribute, and there are no repeat purchases. The platform serves as a marketplace and charges sellers a portion of sales revenue as the commission fee. Table 1 provides a list of the notations used in the model.

## Consumer

We consider a unit mass of consumers who purchase either the product H or the product L. The consumers decide which product to purchase based on their net utility, which consists of three parts: the perceived product quality, the misfit cost incurred from the diference between the consumer’s preferred and purchased product, and the product price. We model consumers’ tastes with a variation of the linear city model [34] and assume that two products are located at location zero and one of a line of unit length. Consumer’s preference for the horizontal attribute is uniformly distributed on [0, 1], where consumer’s location represents their ideal product in terms of product fit. Therefore, a consumer located at x receives a utility of $U _ { H } ( \boldsymbol { x } ) = \ q _ { H } - t \boldsymbol { x } - p _ { H }$ from product H, or $U _ { L } ( x ) = \ q _ { L } - t ( 1 - x ) -$ ${ \boldsymbol { { \mathit { P } } } } { \boldsymbol { L } }$ from product L. The misfit cost rate t is associated with the degree of substitution of these two products [24]. $q _ { H }$ and $q _ { L }$ are the perceived qualities of products H and $L ,$ and $ { p _ { H } }$ and ${  { p _ { L } } }$ are the retail prices of products H and $L ,$ respectively.

Table 1. Summary of notations.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $p_{H}, p_{L}$ </td><td>Retail prices of high-quality and low-quality products</td></tr><tr><td> $q_{H}, q_{L}$ </td><td>Actual quality of products</td></tr><tr><td> $e_{H}, e_{L}$ </td><td>Quality misrepresentation levels of high-quality and low-quality sellers</td></tr><tr><td> $q_{L}', q_{H}'$ </td><td>Perceived quality of products</td></tr><tr><td> $I_{H}, I_{L}$ </td><td>Indicators to represent whether high-quality and low-quality sellers choose to manipulate product quality information</td></tr><tr><td> $U_{H}, U_{L}$ </td><td>Consumers&#x27; perceived net utility from high-quality and low-quality products</td></tr><tr><td>t</td><td>Misfit cost rate</td></tr><tr><td> $\eta$ </td><td>The ratio of low-quality product&#x27;s quality to high-quality product&#x27;s quality</td></tr><tr><td>x</td><td>A consumer&#x27;s location on the Hotelling line</td></tr><tr><td>r</td><td>Commission rate in the agency model</td></tr><tr><td> $\Delta q$ </td><td>Initial quality difference between high-quality and low-quality products</td></tr><tr><td>a</td><td>Cost coefficient of misrepresentation</td></tr><tr><td>k</td><td>Leniency of the platform&#x27;s return policy</td></tr></table>

The true qualities of these two products are $q _ { H }$ and $q _ { L }$ , where $q _ { H } > q _ { L }$ . To enhance consumers’ perceived product quality, each seller can choose to manipulate the product quality information through posting fake reviews, generating fake sales and clicks, or manipulating opinions on social media [28]. We denote the levels of such efort of the sellers as $e _ { H }$ and $e _ { L } .$ . We use an indicator function to track whether the seller manipulates the quality signals, such as online reviews, sales information, and popularity information. The indicator function is set to 1 if the seller misrepresents quality, and 0 otherwise. The indicators, $I _ { H }$ and $I _ { L } ,$ , are endogenous variables according to sellers’ profit maximization process. To simplify our analysis and highlight our main analytical insights, we assume that consumers’ perceived qualities for products H and L are $q _ { H } ^ { ' } = q _ { H } + I _ { H } \cdot e _ { H }$ and $q _ { L } ^ { ' } = ~ q _ { L } + ~ I _ { L } \cdot e _ { L }$ . Consumers make their purchase decisions based on perceived qualities $q _ { H } ^ { ' }$ and $q _ { L } ^ { ' }$ rather than the true qualities $q _ { H }$ and $q _ { L }$ , since existing empirical evidence consistently shows that consumers rely heavily on the reviews, sales, and clicks to learn about product quality because these attributes are treated as informative signals of product quality [47]. For example, 90 percent of the customers who read online reviews state that their purchasing decisions are influenced by the reviews [21]. Moreover, product sales volume and the number of product page visits facilitate observational learning: consumers learn the product or service quality via the decisions of previous customers [62, 73]. Consumers prefer products with more favorable reviews [13] and a larger sales volume [8, 35].

## Product Demand and Product Return

Consumers observe both prices and quality signals of products on the platform and make purchase decisions. Consumers perceive the product quality through reviews, sales or clicks volume, and discussions in social media; therefore, quality misrepresentations afect consumers’ perceived product quality with misleading information. A marginal consumer $x ^ { * }$ is indiferent between products H and L. That is, consumers located in $[ 0 , x ^ { * } ]$ choose H and consumers located in $[ x ^ { * } , 1 ]$ choose L. The location of the marginal consumer is given as follows:

$$
q _ {H} + I _ {H} \cdot e _ {H} - t x ^ {*} - p _ {H} = q _ {L} + I _ {L} \cdot e _ {L} - t (1 - x ^ {*}) - p _ {L}
$$

where $q _ { L } = \eta q _ { H }$ , and $\eta$ is the ratio of product L’s quality to product H’s quality. Therefore, the demand for products H and L can be respectively described as:

$$
\begin{array}{l} D _ {H} = x ^ {*} = \frac {1}{2} + \frac {\Delta q + (I _ {H} \cdot e _ {H} - I _ {L} \cdot e _ {L}) - (p _ {H} - p _ {L})}{2 t}, \\ D _ {L} = 1 - x ^ {*} = \frac {1}{2} - \frac {\Delta q + (I _ {H} \cdot e _ {H} - I _ {L} \cdot e _ {L}) - (p _ {H} - p _ {L})}{2 t}, \end{array}\tag{1}
$$

where

$$
\Delta q = q _ {H} - q _ {L} = (1 - \eta) q _ {H}.
$$

Although consumers are misled by the manipulated quality information at the prepurchase, they can assess the quality more accurately after purchasing the product. That is, there is a systematic discrepancy between prior expectations and actual quality: the actual quality is less than the ex-ante perceived quality. This expectation disconfirmation is a diference between quality misrepresentation and truthful advertisement or quality improvement, as the former can inevitably cause an increase in product returns, whereas the latter two will not.

We assume that the number of consumers who will return their purchased products is an increasing function of the discrepancy between ex-ante perceived quality and ex-post actual quality. This assumption is consistent with the expectation–disconfirmation paradigm in the IS and marketing literature [51, 55, 69]. Based on this paradigm, customer satisfaction has three main antecedents: prior expectations, ex-post quality, and disconfirmation. We introduce these three key constructs in the analysis of quality misrepresentation and product returns. In the consumer satisfaction literature, prior expectations have been conceptualized as beliefs about product quality formed by consumers’ prior experiences and exposure to firms’ marketing eforts [55]. In our model, if a seller chooses to misrepresent quality, prior expectation about quality is captured by $q _ { i } + { e _ { i } } . ^ { 1 }$ Ex-post quality is defined as consumers’ post-usage evaluation of the actual product quality; in our context, $q _ { i } .$ . Disconfirmation is defined as discrepancies between consumers’ expectations and the expost quality. Consumers’ expectations will be negatively disconfirmed if the product performs worse than expected, leading to a lower level of consumer satisfaction [55]. In our context, disconfirmation is represented by: $q _ { i } + e _ { i } - q _ { i } = e _ { i } , i \in \{ H , ~ L \}$ . A greater level of disconfirmation leads to a lower level of consumer satisfaction and a higher level of product returns. This relationship is also consistent with the empirical findings on product returns [18, 33]. Therefore, in our analyses, the number of product returns is modeled as an increasing function of disconfirmation.

Specifically, in our model, the discrepancy between ex-ante perceived quality and actual quality is the level of quality misrepresentation: $e _ { i } , i \in \{ H , ~ L \}$ , and the number of product returns is given by $f [ e _ { i } ]$ . For simplicity, we assume that $f [ \cdot ]$ is a linear and increasing function:

$$
f [ e _ {i} ] = k * e _ {i}\tag{2}
$$

where $k > 0$ . The parameter k captures the leniency of the platform’s return policy: a larger value of k means that the platform eases the return process (and thus indicates a higher level of product returns given the same level of the discrepancy).

## Sellers

In the marketplace, two sellers share a portion r of their revenue with the platform as a commission fee in the agency model. Following prior literature, we assume the commission fee to be exogenous in the model [1, 30, 37]. The profit functions for sellers H and L can be described as:

$$
\begin{array}{r l} & {\pi_ {H} = (1 - r) p _ {H} (D _ {H} - I _ {H} \cdot f [ e _ {H} ]) - I _ {H} \cdot \alpha e _ {H} ^ {2};} \\ & {\pi_ {L} = (1 - r) p _ {L} (D _ {L} - I _ {L} \cdot f [ e _ {L} ]) - I _ {L} \cdot \alpha e _ {L} ^ {2},} \end{array}\tag{3}
$$

![](/api/attachments/HTT6JP26/fulltext/images/33c24e905bcde7117e05beccde654046c77880781a01f0eacf618fa1bd187bdc.jpg)

where the quadratic term $\alpha e _ { i } ^ { 2 }$ represents seller i’s cost of manipulating quality information, and α is the cost coeficient of quality misrepresentation. The cost of quality misrepresentation includes posting fake reviews, generating fake sales and clicks, registering fake accounts, and reputation cost [49].

Our model setup captures some unique features of sellers’ quality misrepresentation activities and platforms’ anti-misrepresentation strategies. Our model captures the following two diferent anti-misrepresentation strategies of platforms.

(1) Increase the cost coeficient of quality misrepresentation, α. This refers to the platform’s ability to increase the cost of writing fake reviews or posting fake sales (including reputation-related costs: if a seller is caught misrepresenting quality, it will sufer damage to its reputation). For example, when the platform adopts stricter rules for registering an account, the marginal cost of posting fake reviews or fake sales is higher. In practice, many platforms have started requiring the verification code at the user login or review posting page, increasing the cost of registering fake accounts or of posting fake reviews and sales.

(2) Implement a more lenient product return policy, k. An increased k value means that the platform has eased the return process for consumers, such as by auto-preparing the return label or implementing a full-refund policy. In our model, product return is a natural disincentive for sellers to manipulate quality signals: if a seller conducts quality misrepresentation at a higher level, consumers will be less satisfied after purchasing a product, resulting in more returns.

## Sequence of Events in the Game

The timing of the game is illustrated in Figure 1. In Stage 1, the two sellers decide whether to misrepresent product quality, and at the same time, they decide the level of quality misrepresentation (if any) as well as the retail prices, $ { p _ { H } }$ and ${ { \mathit { P L } } }$ . To analyze all of the potential choices of the sellers, we consider four possible cases: both H and L do not manipulate quality signals (Case 1, $I _ { H } = 0$ and $I _ { L } = 0 )$ ; only H misrepresents quality (Case 2, $I _ { H } = 1$ and $I _ { L } = 0 )$ ; only L misrepresents quality (Case 3, $I _ { H } = 0$ and $I _ { L } = 1 )$ ; and both H and L misrepresent quality (Case 4, $I _ { H } = 1$ and $I _ { L } = 1 )$ . Table 2 presents the four cases. In Stage 2, consumers observe the retail prices as well as quality signals, and make purchase decisions by utility comparison.

Pricing and Misrepresentation Stage (Stage 1)

Case 1

Sellers observe each others'quality misrepresentation decisions, and simultaneously announce prices as well as misrepresentation levels (if any).

Case 2

Case 3

Case 4

Demand and Profit Realization Stage (Stage 2)

Consumers observe the prices as well as quality signals, and make a purchase decision.

Figure 1. Two-stage game with sellers’ quality misrepresentation behaviors.

Table 2. Sellers’ quality misrepresentation behaviors.

<table><tr><td>Case 1:H and L do not misrepresent quality. $I_{H} = 0$  and  $I_{L} = 0$ </td><td>Case 2:Only H misrepresents quality. $I_{H} = 1$  and  $I_{L} = 0$ </td></tr><tr><td>Case 3:Only L misrepresents quality. $I_{H} = 0$  and  $I_{L} = 1$ </td><td>Case 4:Both H and L misrepresent quality. $I_{H} = 1$  and  $I_{L} = 1$ </td></tr></table>

We use backward induction to deduce the equilibrium of the players’ actions in each stage. In Stage 2, consumers purchase their preferred product, after considering the products’ prices, the perceived product quality, and their intrinsic preference for products H and L. The demand functions are realized as in Eq. (1). In Stage 1, anticipating the consumers’ decisions, sellers decide whether to misrepresent the quality, and the optimal prices as well as misrepresentation levels (if any) at the same time. We use the first-order condition to solve sellers’ profit maximization problem, based on profit functions in Eq. (3). We focus on the interesting cases where competition plays a role in the equilibrium. Therefore, we assume that the parameters are such that the following conditions hold, to ensure the participation constraints are met for consumers (i.e., the full market coverage assumption) and two sellers $( \mathrm { i . e . , } \ p _ { i } , \ e _ { i } ,$ and $\pi _ { i }$ are positive) in the four cases.

$$
\text {   Assumption   } A 1: (\mathrm{i}) \alpha > \frac {(1 - r) (1 - k t) (1 - 2 k t)}{6 t} \text {   and   } \Delta q <   \frac {6 \alpha t - (1 - r) (1 - k t) (1 - 2 k t)}{2 \alpha + k (1 - r) (1 - 2 k t)};
$$

$$
\text {(ii)} q _ {H} > \frac {3 t}{1 + \eta}. ^ {2}
$$

$$
\text {   Assumption   A2:   } k <   \frac {1}{2 t}.
$$

A1(i) ensures that the cost of quality misrepresentation is not too small, and the initial quality diference is not extremely large, such that every seller has the incentive to participate in our analyses.<sup>3</sup> This assumption allows us to focus on the role of competition between the sellers since, otherwise, one seller will be driven out of the market (and then it becomes a monopoly case). A1(ii) ensures that the product quality is high enough that the market is fully covered, and the marginal consumer’s utility is positive. This assumption makes sure there is competition between the sellers since otherwise, the two sellers become local monopolists. This group of assumptions is common for horizontal models as they allow us to focus on the important role of competition between sellers [32, 45] and highlight the cases relevant to our research questions.

A2 ensures that k is not extremely high such that quality misrepresentation still exists on the platform, and the number of consumers who return products does not exceed market share. It is worth noting that this is not a strict condition since the total product demand is normalized to one in our analysis.<sup>4</sup> While the platform can have a more lenient return policy and increase k by adopting an easier return process or adopting a free return policy, consumers still encounter unavoidable frictions such as traveling to the post ofice, worrying about returns getting lost in the mail, or waiting for the refund.<sup>5</sup> In other words, k is normally not extremely high in practice.

## Analysis

## Impact of Quality Misrepresentation

In this subsection, we seek the pure-strategy Nash equilibria of four cases in Table 2 to examine sellers’ incentives to misrepresent quality. We first characterize the equilibria of diferent cases. In the benchmark case (Case 1; denoted by the superscript C1), the sellers do not misrepresent product quality; In Case 2 and Case 3 (denoted by superscripts C2 and C3, respectively), only one seller misrepresents product quality (H or L). The seller that manipulates product quality signals optimizes its misrepresentation level and retail price, and the other seller only decides the optimal retail price; In Case 4 (denoted by superscript C4), both sellers misrepresent product quality. The detailed calculations and equilibrium results are in the Online Supplemental Appendix A.

After obtaining the equilibrium in each case, we seek a pure-strategy Nash equilibrium for these four cases. A case is considered a pure-strategy Nash equilibrium when neither seller has an incentive to deviate to the other case(s). The findings are summarized in Lemma 1:

Lemma 1. When sellers decide whether to misrepresent its quality, their equilibrium quality misrepresentation choices can be characterized as follows:

(a) Case 1 is a pure-strategy Nash equilibrium, and neither seller chooses to misrepresent quality $( i . e . , \pi _ { L } ^ { C 1 * } \stackrel { . } { \geq } \pi _ { L } ^ { C 3 * } , \pi _ { H } ^ { C 1 * } \geq \pi _ { H } ^ { C 2 * } )$ if and only $i f k \geq { \bar { k } } ;$

(b) Case 4 is a pure-strategy Nash equilibrium, and both sellers choose to misrepresent quality $( i . e . , \pi _ { L } ^ { C 4 * } \overset { ^ { \cdot } } { \geq } \pi _ { L } ^ { C 2 * } , \pi _ { H } ^ { C 4 * } \overset { ^ { \cdot } } { \geq } \pi _ { H } ^ { C 3 * } )$ if and only $i f k \leq \overline { { k } } ;$

(c) Cases 2 and 3 are not pure-strategy Nash equilibria

(Note: Online Supplemental Appendix A includes the detailed equilibrium profits and case comparisons),

where threshold values <sup>�</sup>k and $\overline { { \overline { { k } } } }$ are the functions of parameters $( \alpha , t , r ) . \overline { { \overline { { k } } } } > \overline { { k } }$ always holds.

Detailed definitions of threshold values are available in the Online Supplemental Appendix A unless indicated otherwise. All threshold values are checked with the feasible region to ensure validity. In this study, the “feasible region” means the parameter value that satisfies Assumptions A1 and A2.

Figure 2 illustrates one example of the sellers’ quality misrepresentation choices, assuming $t = 0 . 2$ and $r = 0 . 2$ . The horizontal axis represents the cost coeficient of misrepresentation (α). The vertical axis represents the leniency of the return policy (k). By assumption A1, the gray area is not a feasible region. Based on Lemma 1(a), when the leniency of return policy is higher than a threshold $( k \geq \bar { k } )$ , sellers’ optimal strategy is to stay at the benchmark case and do not misrepresent quality (Region I and Region III). When the return policy leniency is lower than a threshold $( k < \overline { { \overline { { k } } } } )$ , both sellers would misrepresent quality (Region II and Region III). Multiple equilibria are common in the game theory [3, 15]. In our setting, the multiple equilibria exist because the conditions that ensure Case 1 is a pure-strategy Nash equilibrium (i $. \mathrm { e } . , \pi _ { L } ^ { C 1 * } \geq \pi _ { L } ^ { C 3 * } , \pi _ { H } ^ { C 1 * } \geq \pi _ { H } ^ { C 2 * } )$ and the conditions that ensure Case 4 is a pure-strategy Nash equilibrium (i.e., $\pi _ { L } ^ { C 4 * } \geq \pi _ { L } ^ { C 2 * } , \pi _ { H } ^ { C 4 * } \geq \pi _ { H } ^ { C 3 * } )$ are not mutually exclusive. Because Cases 2 and 3 are not Nash equilibria, we analyze the impact of quality misrepresentation by comparing the equilibrium outcomes in Cases 1 and 4. In the Online

![](/api/attachments/HTT6JP26/fulltext/images/0e16021c61feb6665ae90eb3635f8ce096818edd7385c9347ccbc26c5e68f59c.jpg)  
Figure 2. Equilibrium quality misrepresentation choices for diferent α and k. Note: Plot for $t = 0 . 2$ $r = 0 . 2$

Supplemental Appendix B, we also examine other possible cases where sellers misrepresent product quality in a negative way, and our analyses show that these cases are not Nash equilibria.

Proposition 1: In Case 4, when both sellers misrepresent quality, seller H conducts a higher level of quality misrepresentation than seller $L \ ( i . e . , e _ { H } ^ { C \dot { 4 } * } > e _ { L } ^ { C 4 * } )$

In a competitive environment, sellers determine their misrepresentation levels by considering the potential benefits brought by misrepresentation. One seller is more incentivized if it can charge a higher price than its opponent. Formally, the equilibrium price and misrepresentation level are positively related (i.e., $\begin{array} { r } { e _ { i } ^ { C 4 * } = \frac { p _ { i } ^ { C 4 * } ( 1 - r ) ( 1 - 2 k t ) } { 4 \alpha t } ) } \end{array}$ . In our context, the high-quality seller can charge an even higher price by keeping and expanding its quality advantage (i.e., $p _ { H } ^ { C 4 * } > p _ { L } ^ { C 4 * } )$

The intuition is similar to analyses of the scenario where sellers pre-determine their retail prices without considering quality misrepresentation. Following the research of Dellarocas [19], we examine the model where the retail prices are pre-determined $( \mathrm { i } . \mathrm { e } . , p _ { H } ^ { C 1 * }$ and $p _ { L } ^ { C 1 * } )$ and the equilibrium misrepresentation levels are determined by maximizing $\pi _ { H } ^ { C 4 } | ( p _ { H } =$ $p _ { H } ^ { C 1 * } , p _ { L } = p _ { L } ^ { C 1 * } )$ and $\pi _ { L } ^ { C 4 } | ( p _ { H } = p _ { H } ^ { C 1 * } , p _ { L } = p _ { L } ^ { C 1 * } )$ . We denote the equilibrium misrepresentation levels in this case as $\stackrel { \sim } { e } _ { H } ^ { C 4 * }$ and $\widetilde { e _ { L } ^ { C 4 * } }$ . Consistent with our results, $\begin{array} { r } { \widetilde { e _ { H } ^ { C 4 * } } = \frac { ( 1 - r ) ( 1 - 2 k t ) p _ { H } ^ { C 1 * } } { 4 \alpha t } } \end{array}$ is always higher than $\begin{array} { r } { \widetilde { e _ { L } ^ { C 4 * } } = \frac { ( 1 - r ) ( 1 - 2 k t ) p _ { L } ^ { C 1 * } } { 4 \alpha t } } \end{array}$ because $p _ { H } ^ { C 1 * } > p _ { L } ^ { C 1 * }$ . In other words, the equilibrium misrepresentation level of the high-quality seller is higher than that of the low-quality seller.

However, apart from the decisions of quality misrepresentation described in Dellarocas [19], our analyses also consider the strategic interaction between price decisions and quality misrepresentation decisions. In our analyses, the high-quality seller is more incentivized to manipulate quality signals because a higher level of quality misrepresentation can potentially be transferred into a higher retail price. The equilibrium quality diference can be underestimated if such strategic interaction is overlooked (i.e., $e _ { H } ^ { C 4 * } - e _ { L } ^ { C 4 * } { > } \widetilde { e _ { H } ^ { C 4 * } } - \widetilde { e _ { L } ^ { C 4 * } } )$

Proposition 1 implies that because of quality misrepresentation, at the equilibrium of Case 4, the diference between the perceived qualities,

$$
\dot {q} _ {H} ^ {\prime} - \dot {q} _ {L} ^ {\prime} = \left(q _ {H} + e _ {H} ^ {C 4 *}\right) - \left(q _ {L} + e _ {L} ^ {C 4 *}\right) = \Delta q \bigg [ 1 + \frac {(1 - r) (1 - 2 k t)}{6 \alpha t - (1 - r) (1 - k t) (1 - 2 k t)} \bigg ]\tag{4}
$$

is larger than the actual quality diference $q _ { H } - q _ { L } = \Delta q .$ Compared to the benchmark case, the high-quality seller enjoys a higher level of quality advantage in Case 4. In the next proposition, we compare the benchmark equilibrium with the results in Case 4, and thereby examine the impact of quality misrepresentation.

Proposition 2 (Case 4 vs. Case 1 for Sellers): Compared to the benchmark case (Case $I ) , ( \mathsf { a } )$ the equilibrium profit of seller H is higher in Case 4 (i.e., $\pi _ { H } ^ { C 4 * } > \pi _ { H } ^ { C 1 * } )$ if and only if $\Delta q { > } \dot { \Delta q }$ and $k < \bar { k } ;$ (b) the equilibrium profit of seller L is always lower in Case 4 $( i . e . , \pi _ { L } ^ { C 4 * } < \pi _ { L } ^ { C 1 * } )$ .

Quality misrepresentation provides the sellers with an opportunity to promote their products by increasing product quality in the eyes of consumers. However, its impact varies with diferent sellers, as the high-quality seller uses quality misrepresentation to expand its quality advantage (Proposition 1). On the one hand, the high-quality seller can utilize this quality advantage to charge a higher price, compared to its price in the benchmark case. On the other hand, the high-quality seller needs to lower its price to make up for the product returns caused by its quality misrepresentation. When the quality diference is suficiently large (see Eq. (4)), and the return policy leniency is low (i.e., a relatively small number of sales is returned), the high-quality seller would charge a higher price in Case 4. Therefore, the equilibrium price of seller H is higher in Case 4 (i.e., $p _ { H } ^ { C 4 * } > p _ { H } ^ { C 1 * } )$ if and only if the original quality diference is high. However, the low-quality seller has to set a lower price in Case 4, compared to its price in the benchmark case, since it sufers from a larger quality disadvantage and also needs to decrease the price to accommodate the product returns caused by quality misrepresentation. In other words, the equilibrium price of seller L is always lower in Case 4 $( \mathrm { i . e . , } p _ { L } ^ { C 4 * } < p _ { L } ^ { C 1 * } )$

The comparison between the sellers’ profits in Case 4 and Case 1 follows a similar logic. When the quality diference is suficiently large and the return policy leniency is low, for the high-quality seller, the benefit gained from the expanded quality advantage exceeds the loss from product returns and misrepresentation cost. However, the profit of the low-quality seller is lower in Case 4 because it sufers from a greater quality disadvantage in equilibrium, as well as the misrepresentation cost and product returns caused by the quality misrepresentation.

When the return policy is less lenient $( \mathrm { i . e . , } k < \bar { k } )$ , the result is a prisoner’s dilemma for the sellers with respect to the choice of quality misrepresentation if the quality diference is suficiently small $( \mathrm { i . e . , } \ \varDelta q < \widetilde { \varDelta q } )$ . That is, when the return policy is less lenient, although there are gains to each seller from manipulating the quality signals if the other seller does not, the equilibrium with both sellers misrepresenting quality generates a loss for both sellers. Quality misrepresentation by one seller translates to opposing changes in competition for these two sellers, and that provides a potential incentive to misrepresent quality if the return policy is less lenient. It also provides an incentive for the other seller to misrepresent if one seller has already manipulated the quality signals. However, when both sellers conduct quality misrepresentation, the relative gain from consumers’ higher perceived product quality is limited because competition forces them to lower their prices, and the gain from quality misrepresentation cannot ofset its cost for both sellers.

Interestingly, when the return policy is less lenient $( \mathrm { i . e . , } \ k < \ \bar { k } )$ , although both sellers would choose to misrepresent quality in Case 4, the high-quality seller’s profit can be greater than its profit in the benchmark case when the quality diference is high enough (i.e., $\Delta q { > } \widetilde { \Delta q } ) . ^ { 6 }$ The result reflects the importance of the interaction between price decisions and quality misrepresentation decisions. In our context, the high-quality seller can efectively gain a quality advantage by conducting quality misrepresentation and charging a higher retail price at the same time. Therefore, when the equilibrium quality diference is large enough, and the return policy is less lenient, for the high-quality seller, the expanded quality advantage and higher price gained from the quality misrepresentation can ofset its cost from quality misrepresentation.

Proposition 3 (Case 4 vs. Case 1 for Platform): Compared to the benchmark case (Case 1), the equilibrium profit of the platform is higher in Case $4 \ { \overset { \cdot } { ( } i . e . , \pi _ { R } ^ { C 4 * } > \pi _ { R } ^ { C 1 * } ) }$ if and only $i f \Delta q { > } \tilde { \Delta q }$ and $k < \hat { k }$

Lemma 1 indicates that if the platform’s objective is to eliminate the quality misrepresentation, the platform should adopt a lenient return policy $( \mathrm { i } . \mathrm { e } . , \ k > \overline { { k } } )$ . Moreover, Proposition 3 implies that the platform benefits from the sellers’ quality misrepresentation only if the sellers’ initial quality diference is large $( \mathrm { i . e . , } \varDelta q > \widehat { \Delta q } )$ and the return policy is not extremely lenient $( \mathrm { i . e . , } k < \hat { k } )$ . We can also show that $\hat { k } > m a x \left[ \overline { { k } } , \overline { { \overline { { k } } } } \right]$ . Therefore, depending on its main purpose and the market condition, the platform can have diferent levels of return leniency. If the sellers’ initial quality diference is small or the platform’s main purpose is to avoid quality misrepresentation, then the platform should adopt a lenient return policy to completely deter the sellers from misrepresenting the quality. However, if the sellers’ initial quality diference is large or the platform’s main purpose is to earn more profit, the platform would tolerate a certain level of quality misrepresentation with a strict return policy and gain more profit in Case 4.

## Impact of Anti-Misrepresentation Strategies

The objective of this paper is to understand (i) the impact of quality misrepresentation on sellers with products of difering quality, and (ii) the impact of anti-misrepresentation strategies on diferent sellers’ quality misrepresentation levels and profits when sellers compete in both the retail price and manipulation level. The previous subsection has analyzed the first question by examining the equilibrium in diferent cases and comparing Case 1 with Case 4. The results indicate that because sellers compete on both the misrepresentation level and price, the existence of quality misrepresentation can have diferent (even opposing) efects on the competing sellers with products of difering quality.

In the following propositions, we discuss how sellers’ equilibrium misrepresentation levels and profits may change with the strictness of anti-misrepresentation strategies. In this discussion, we highlight the role of strategic interactions between price and misrepresentation competition in driving the quality misrepresentation of diferent sellers.

Proposition 4 (Anti-misrepresentation Strategies and Misrepresentation Levels):

(a) As the cost coeficient of misrepresentation $( i . e . , \alpha )$ increases, the equilibrium misrepresentation level of seller H decreases $\begin{array} { r } { ( i . e . , \ \frac { \partial e _ { H } ^ { C 4 * } } { \partial \alpha } < 0 ) ; } \end{array}$ ; The equilibrium misrepresentation level of seller L increases $( i . e . , \ \frac { \partial e _ { L } ^ { C 4 * } } { \partial \alpha } > 0 )$ if and only $\begin{array} { r } { i f \Delta q > \frac { [ 6 \alpha t - ( 1 - r ) ( 1 - 2 k t ) ( 1 - k t ) ] ^ { 2 } } { 3 t [ 2 \alpha + k ( 1 - r ) ( 1 - 2 k t ) ] ^ { 2 } } } \end{array}$

(b) As the return policy leniency of the platform $( i . e . , k )$ increases, The equilibrium misrepresentation level of seller H decreases $\begin{array} { r } { ( i . e . , \ \frac { \partial e _ { H } ^ { C 4 * } } { \partial k } < 0 ) . } \end{array}$ ; The equilibrium misrepresentation level of seller L increases $( i . e . , \ \frac { \partial e _ { L } ^ { C 4 * } } { \partial k } > 0 )$ if and only $\begin{array} { r } { i f \Delta q > \frac { \left[ 4 \alpha t + \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \right] \left[ 6 \alpha t - \left( 1 - r \right) \left( 1 - 2 k t \right) \left( 1 - k t \right) \right] ^ { 2 } } { t \left[ 1 2 \alpha t + \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \right] \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 2 } } } \end{array}$

A higher marginal cost of misrepresentation, α, represents the platform’s implementation of stricter rules on manipulating quality information and registering fake accounts. A more lenient return policy, $k ,$ represents the platform’s implementation of an easier process for consumers to return products, such as by auto-preparing the return label or implementing a full-refund policy. The first part of Proposition $\mathsfit { 4 } ( \mathsfit { a } )$ and 4(b) is consistent with our intuition: The equilibrium misrepresentation level of the high-quality seller decreases with the misrepresentation cost and return policy leniency. However, surprisingly, as the anti-misrepresentation strategies become stricter, the low-quality seller may increase the misrepresentation level when the quality diference is suficiently large.

To understand the role of misrepresentation cost in shaping sellers’ incentives to misrepresent quality, we begin with the illustration of two groups of efects: (i) the direct cost efect and (ii) the indirect competition efect. How increasing misrepresentation cost afects sellers’ misrepresentation levels depends on the strength and direction of these two efects. For the direct cost efect, if one seller conducts quality misrepresentation without thinking about its opponent’s decisions, an increase in marginal misrepresentation cost naturally disincentivizes its misrepresentation level. Suppose only one seller misrepresents quality, and its opponent does not (i.e., Case 2 or Case 3): stricter anti-misrepresentation strategies would always discourage quality misrepresentation $\begin{array} { r } { ( \mathrm { i . e . , ~ } \frac { \partial e _ { L } ^ { C 3 * } } { \partial \alpha } < 0 } \end{array}$ and $\begin{array} { r } { \frac { \partial e _ { H } ^ { C 2 * } } { \partial \alpha } < 0 ; \ \frac { \partial e _ { L } ^ { C 3 * } } { \partial k } < 0 } \end{array}$ and $\frac { \partial e _ { H } ^ { C 2 * } } { \partial k } < 0 )$

As to the indirect competition efect, sellers use both quality misrepresentation and price as competitive tools, and an increase in the cost of quality misrepresentation will afect the incentives to misrepresent quality and the setting of retail prices for both sellers. Therefore, when one seller adjusts its misrepresentation level with an increase in the misrepresentation cost, it needs to strategically consider its opponent’s response to its misrepresentation behaviors. For instance, Figure 3 shows one seller’s best response as a function of the other seller’s misrepresentation level (the response function). The downward-sloping curve also indicates that when one seller misrepresents more, its opponent seller would misrepresent quality less in response. Therefore, sellers compete in quality misrepresentation with the objective of obtaining a competitive advantage and increasing retail prices.

![](/api/attachments/HTT6JP26/fulltext/images/348476a0c37fb4e21d0b2ff7fd93afd346907278e228044a55c84975b706da4b.jpg)  
Figure 3. Best response curves of sellers’ misrepresentation level. Note: Plot for r ¼ 0:1; α ¼ 0:45; t ¼ 0:3; $q _ { H } = 0 . 5 1$ ， $\eta = 0 . 8$ 2 $k = 0 . 8 $

When efect (i) dominates efect (ii), we would observe that the sellers’ misrepresentation levels decrease with the common misrepresentation cost. In contrast, if efect (ii) dominates efect (i), we would observe sellers’ equilibrium misrepresentation levels increase with the misrepresentation cost. As described in Proposition 1, the high-quality seller has a higher misrepresentation level in the equilibrium, and it sufers more from the direct cost efect than the low-quality seller does. Therefore, an increase in misrepresentation costs may cause the high-quality seller to have a higher tendency to decrease its misrepresentation level. In other words, efect (i) is more likely to dominate efect (ii) for the high-quality seller. In our model, sellers simultaneously decide the misrepresentation levels. In such a simultaneous game, one seller does not observe its opponent’s misrepresentation level in advance but knows the best response curves. Anticipating that the high-quality seller tends to decrease its misrepresentation level, the low-quality seller has an incentive to increase its quality misrepresentation level because of efect (ii). When the initial quality diference is large enough, efect (ii) dominates efect (i) for the low-quality seller.<sup>7</sup>

An anti-misrepresentation strategy can have opposing efects on diferent sellers, according to our analyses, which capture the fact that sellers can adjust their prices when they misrepresent product quality. In the following examination, we use the cost coeficient of quality misrepresentation $( \mathrm { i . e . , ~ } \alpha )$ as the example to illustrate this idea, and the analyses on return policy leniency (i.e., k) follow a similar logic. Specifically, the impact of the misrepresentation cost (i.e., α) on the equilibrium misrepresentation levels can be written as follows:

$$
\begin{array}{l} \frac {\partial e _ {i} ^ {C 4 *}}{\partial \alpha} = \frac {\frac {\partial p _ {i} ^ {C 4 *}}{\partial \alpha} (1 - r) (1 - 2 k t)}{4 \alpha t} - \frac {p _ {i} ^ {C 4 *} (1 - r) (1 - 2 k t)}{4 \alpha^ {2} t} \\ = \frac {(1 - r) (1 - 2 k t)}{4 \alpha^ {2} t} \left[ \frac {\partial p _ {i} ^ {C 4 *}}{\partial \alpha} \alpha - p _ {i} ^ {C 4 *} \right], \end{array}
$$

where $ { p _ { i } ^ { C 4 * } }$ and $e _ { i } ^ { C 4 * }$ are the equilibrium prices and misrepresentation levels, respectively. Because $\frac { ( 1 - r ) ( 1 - 2 k t ) } { 4 \alpha ^ { 2 } t }$ is positive, the sign of $\frac { \partial e _ { i } ^ { C 4 * } } { \partial \alpha }$ depends on the magnitude of the misrepresentation-cost-price elasticity $\frac { \partial p _ { i } ^ { C 4 * } } { \partial \alpha } \big / \frac { p _ { i } ^ { C 4 * } } { \alpha }$ . If $\frac { \partial p _ { i } ^ { C 4 * } } { \partial \alpha } / \frac { p _ { i } ^ { C 4 * } } { \alpha } < 1 $ , then $\frac { \partial e _ { i } ^ { C 4 * } } { \partial \alpha } < 0 ;$ ; if $\frac { \partial p _ { i } ^ { C 4 * } } { \partial \alpha } / \frac { p _ { i } ^ { C 4 * } } { \alpha } > 1$ , then $\frac { \partial e _ { i } ^ { C 4 * } } { \partial \alpha } > 0$ . The misrepresentation-cost-price elasticity can be interpreted as the magnitude of misrepresentation cost changes that are passed on to prices. As explained in our previous discussion on the indirect competition efect, an increase in the misrepresentation cost, α, may cause the high-quality seller to have a higher tendency to decrease its misrepresentation level, and the best response for the low-quality seller would be to increase its misrepresentation. Therefore, the perceived quality diference between the two products shrinks, and the low-quality seller may be able to charge a higher price, which is captured by the misrepresentation-cost-price elasticity. In other words, a larger misrepresentation-cost-price elasticity, $\frac { \partial p _ { i } ^ { C 4 * } } { \partial \alpha } \big / \frac { p _ { i } ^ { C 4 * } } { \alpha }$ , is an indicator of the positive impact of the misrepresentation cost on the misrepresentation level.

Our findings demonstrate the importance of capturing the current practice of sellers using both price and quality misrepresentation as competitive tools. Although the previous studies have considered competition in misrepresentation levels, the pricing decisions in their models are largely fixed [48, 49] and do not interact with quality misrepresentation decisions [19]. That means there is no strategic interaction between price decisions and quality misrepresentation decisions in the previous studies. For example, if we follow Dellarocas [19], where the retail prices are pre-determined without considering quality misrepresentation (i.e., $\begin{array} { r } { p _ { H } ^ { C 1 * } = t + \frac { 1 } { 3 } \Delta q } \end{array}$ and $\begin{array} { r } { p _ { L } ^ { C 1 * } = t - \frac { 1 } { 3 } \varDelta q ) } \end{array}$ , we would obtain the equilibrium misrepresentation levels as $\begin{array} { r } { \widetilde { e _ { H } ^ { C 4 * } } = \frac { ( 1 - r ) ( 1 - 2 k t ) p _ { H } ^ { C 1 * } } { 4 \alpha t } } \end{array}$ and $\begin{array} { r } { \widetilde { e _ { L } ^ { C 4 * } } = \frac { ( 1 - r ) ( 1 - 2 k t ) p _ { L } ^ { C 1 * } } { 4 \alpha t } } \end{array}$ . It is evident that the quality misrepresentation level always decreases with the misrepresentation cost for both sellers (i.e., $\frac { \partial e _ { H } ^ { C 4 * } } { \partial \alpha } < 0$ and $\begin{array} { r } { \frac { \partial e _ { L } ^ { C 4 * } } { \partial \alpha } < 0 ; \frac { \partial e _ { H } ^ { C 4 * } } { \partial k } < 0 } \end{array}$ and $\frac { \partial e _ { L } ^ { C 4 * } } { \partial k } < 0 )$

Our findings in Proposition 4 have important implications for e-commerce platforms’ antimisrepresentation strategies. A stricter anti-misrepresentation strategy may counterintuitively incentivize the low-quality seller to increase its misrepresentation level in the presence of misrepresentation and price competition. In Figure 4, we provide numerical examples for the relationship between the misrepresentation level $( e _ { i } ^ { C 4 * } )$ and misrepresentation cost $( \alpha ) \colon e _ { H } ^ { C 4 * }$ decreases with the misrepresentation cost $\alpha ,$ but $e _ { L } ^ { C 4 * }$ may increase with α. In Figure 5, we provide numerical examples for the relationship between the misrepresentation level $( e _ { i } ^ { C 4 * } )$ and return leniency (k): $e _ { H } ^ { C 4 * }$ decreases with the return policy leniency $k ,$ but e<sup>C4</sup> $e _ { L } ^ { C 4 * }$ may increase with k.

![](/api/attachments/HTT6JP26/fulltext/images/37094a8cf19a3c6e0fd24bc8a4f10327a6b697b3b3f4031d67b478f786072442.jpg)  
Figure 4. Misrepresentation Level and Cost Coeficient of Misrepresentation. Note: Plot for $r = 0 . 1 , t =$ 0:3; $q _ { H } = 0 . 5 1$ $\eta = 0 . 8$ $k = 0 . 8 $ . The starting point of the horizontal axis is set to meet the parameters conditions.

![](/api/attachments/HTT6JP26/fulltext/images/3044db41faa7acd2fe942dad6105d25bd107e1603afba26f3879d42d1c1a4be0.jpg)  
Figure 5. Misrepresentation level and return policy leniency. Note: Plot for $r = 0 . 1 , t = 0 . 3$ $q _ { H } = 0 . 5 1$ ， $\eta = 0 . 8 , a = 0 . 4 5$ . The starting point of the horizontal axis is set to meet the parameters’ conditions.

Following Dellarocas [19] and Mayzlin et al. [49], we analyze the efect of sellers’ competition in a product market with horizontal diferentiation. For platforms (or departments of a platform) selling electronic products, such as digital cameras, the horizontal diferentiation might be small. However, for the platforms (or departments of a platform) selling clothing and shoes, the horizontal diferentiation could be relatively large, which fits the setting of our model: Competing sellers are suficiently diferentiated in their horizontal attributes, and consumers have suficiently diverse tastes for horizontal attributes. Our model and results can broadly enrich the IS research on product markets with horizontal diferentiation [14, 16, 22, 36, 43] by showing how anti-misrepresentation strategies afect diferent competing sellers in such a market.

Our next proposition discusses the impact of the anti-misrepresentation strategies on sellers’ equilibrium profits.

Proposition 5 (Anti-misrepresentation Strategies and Sellers’ Profits):

(a) As the cost coeficient of misrepresentation $( i . e . , \alpha )$ increases, the profit of seller H decreases $( i . e . , \ \frac { \partial \pi _ { H } ^ { C 4 * } } { \partial \alpha } < 0 )$ if and only $\begin{array} { r } { i f \Delta q > \frac { \left[ 6 \alpha t - \left( 1 - r \right) \left( 1 - 2 k t \right) \left( 1 - k t \right) \right] ^ { 2 } \left[ 2 \alpha \left( 1 + 6 k t \right) - k \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \right] } { \left[ 2 \alpha t \left( 5 - 2 k t \right) - \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \left( 1 - k t \right) \right] \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 2 } } } \end{array}$ ; The profit of seller L always increases $( i . e . , \ \frac { \partial \pi _ { L } ^ { C 4 * } } { \partial \alpha } > 0 )$

(b) As the return policy leniency $( i . e . , k )$ increases, the profit of seller H decreases $( i . e . , \frac { \partial \pi _ { H } ^ { C 4 * } } { \partial k } < 0 )$ if and only $\begin{array} { r } { i f \Delta q > \frac { \left[ 6 \alpha t - ( 1 - r ) \left( 1 - 2 k t \right) \left( 1 - k t \right) \right] ^ { 2 } \left[ 4 \alpha t \left( 6 k t - 1 \right) + \overline { { ( 1 - r ) ( 1 - 2 k t ) ^ { 3 } } } \right] } { \left[ 4 \alpha t \left( 3 - 2 k t \right) - \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 3 } \right] \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 2 } } } \end{array}$ ; The profit of seller L always increases $( i . e . , \ \frac { \partial \pi _ { L } ^ { C 4 * } } { \partial k } > 0 )$

As stated in Proposition 4, the high-quality seller’s misrepresentation level tends to decrease with the anti-misrepresentation strategies (α and k), and the low-quality seller’s misrepresentation level is less likely to decrease. Therefore, the quality advantage that the high-quality seller enjoys would decrease with anti-misrepresentation strategies (i.e., $\begin{array} { r } { \frac { \partial \left( q _ { H } ^ { ^ { \prime } } - q _ { L } ^ { ^ { \prime } } \right) } { \partial \alpha } < 0 } \end{array}$ and $\frac { \partial \big ( q _ { H } ^ { ^ { \prime } } - q _ { L } ^ { ^ { \prime } } \big ) } { \partial k } < 0 )$ . The high-quality seller tends to set a lower price to react to this decreased quality advantage. Meanwhile, the increased marginal misrepresentation cost or return volume encourages the seller to set a higher retail price to pass the increased cost to the consumers. Thus, when the quality diference in the equilibrium is suficiently large and the driving force of lowering its price dominates, the high-quality seller’s product price tends to decrease. On the other hand, the low-quality seller tends to set a higher retail price because the increased misrepresentation cost mitigates its quality disadvantage with its opponent, and the higher retail price can also help compensate for the higher marginal misrepresentation cost. Also, the mitigated quality diference shifts the sellers’ market share such that high-quality seller’s market share decreases and the low-quality seller’s market share increases (i.e., $\textstyle { \frac { \partial x ^ { C 4 * } } { \partial \alpha } } < 0$ and $\textstyle { \frac { \partial x ^ { C 4 * } } { \partial k } } < 0 )$ (see the proof for Proposition 5 in the Online Supplemental Appendix A).

The impact of the anti-misrepresentation policies on sellers’ profits has especially interesting implications: In the presence of the Hotelling-type competition, a stricter antimisrepresentation strategy is beneficial to the low-quality seller and can be detrimental to the high-quality seller when the quality diference is suficiently large. The underlying intuition is related to Proposition 4. As the anti-misrepresentation policies get stricter, anticipating the high-quality seller has a high tendency to decrease its misrepresentation level, the low-quality seller is likely to take the chance to mitigate the quality disadvantage in the competition.

Apart from the impact of anti-misrepresentation policies on diferent sellers, another interesting aspect to examine is the overall efects of anti-misrepresentation strategies on the total misrepresentation level $( \mathrm { i . e . , } e _ { H } ^ { C 4 * } + e _ { L } ^ { C 4 * } )$

Proposition 6 (Total Misrepresentation Level): The total level of quality misrepresentation decreases with the misrepresentation cost $\begin{array} { r } { ( i . e . , \ \frac { \partial ( e _ { H } ^ { C 4 * } + e _ { L } ^ { C 4 * } ) } { \partial \alpha } < 0 ) } \end{array}$ and the return policy leniency $( i . e . , \ \frac { \partial ( e _ { H } ^ { C 4 * } + e _ { L } ^ { C 4 * } ) } { \partial k } < 0 )$ .

Proposition 6 indicates that although increasing return policy leniency or increasing misrepresentation cost has diferent (or even opposing) impacts on diferent sellers, these anti-misrepresentation strategies can efectively lower the overall quality misrepresentation level.

In the next proposition, we compare the efectiveness of the two anti-misrepresentation strategies in deterring seller L’s quality misrepresentation. According to Propositions 4, the anti-misrepresentation strategies reduce L’s quality misrepresentation level under certain market conditions: $\frac { \partial e _ { L } ^ { * } } { \partial \alpha } < 0$ when $\begin{array} { r } { \Delta q < \overline { { \Delta q } } _ { 1 } = \frac { \left[ 6 \alpha t - \left( 1 - r \right) \left( 1 - 2 k t \right) \left( 1 - k t \right) \right] ^ { 2 } } { 3 t \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 2 } } } \end{array}$ and $\frac { \partial e _ { L } ^ { * } } { \partial k } < 0$ when $\begin{array} { r } { \Delta q < \overline { { \Delta q } } _ { 2 } = \frac { \left[ 4 \alpha t + \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \right] \left[ 6 \alpha t - \left( 1 - r \right) \left( 1 - 2 k t \right) \left( 1 - k t \right) \right] ^ { 2 } } { t \left[ 1 2 \alpha t + \left( 1 - r \right) \left( 1 - 2 k t \right) ^ { 2 } \right] \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 2 } } } \end{array}$ . Importantly, we find that $\overline { { \varDelta q } } _ { 1 } < \overline { { \varDelta q } } _ { 2 }$ always hold, suggesting that the second strategy, adopting a more lenient return policy, can deter quality misrepresentation of the low-quality firm in a wider range of market conditions.

Proposition 7 (Diferent Anti-Misrepresentation Strategies on Misrepresentation Levels):

(a) Among the two anti-misrepresentation strategies, adopting a more lenient return policy (i.e., k) can deter seller L’s misrepresentation level in a wider range of market conditions than increasing the manipulation cost $( i . e . , \alpha ) .$ . That is, $\overline { { \varDelta q } } _ { 1 } < \overline { { \varDelta q } } _ { 2 }$

(b) Comparing to having a more lenient return policy $( i . e . , k ) ,$ , increasing the cost coeficient of misrepresentation $( i . e . , \alpha )$ discourages the total quality misrepresentation more if and only if $\alpha < \alpha ^ { * }$ , where $\begin{array} { r } { \alpha ^ { * } = \frac { ( 1 - 2 k t ) \left[ 1 + 2 k t + r ( \bar { 1 } - 2 k t ) \right] } { 4 t } } \end{array}$

Proposition 7(a) implies that increasing k can deter seller L’s quality misrepresentation in a wider range of market conditions than increasing α. In Figure 6, we describe a numerical example and draw the upper bounds of quality diference such that the two antimanipulation strategies can restrict seller $L 3$ quality misrepresentation level. The numerical example further confirms that increasing k can deter seller L’s quality misrepresentation level in a wider range of market conditions than increasing α.

Proposition 7(b) indicates that adopting higher misrepresentation cost is more efective in discouraging the total misrepresentation level than incorporating a more lenient return policy if the misrepresentation cost is low. However, when the misrepresentation cost is already high, adopting a more lenient return policy can be more efective. The result can guide the platform’s choice on the anti-misrepresentation strategies based on the extent of the total misrepresentation level change. Specifically, when the current misrepresentation cost is low, the platform can keep increasing the misrepresentation cost exclusively to discourage the overall manipulation behaviors. However, when the misrepresentation cost is increased to a certain level $( \mathrm { i } . \mathrm { e } . , \alpha ^ { * } )$ , starting to incorporate a more lenient return policy can be more efective in decreasing the total misrepresentation level than only increasing the misrepresentation cost.

![](/api/attachments/HTT6JP26/fulltext/images/056482a48ae842573f6e46b2e94df67981ce809a362b8ed60cc0c9f45a75c3e0.jpg)  
Cost Coefficient of Quality Misrepresentation (α)  
Figure 6. Comparison of anti-review-manipulation strategies. Note: Plot for $r = 0 . 1 , t = 0 . 3$ $q _ { H } = 0 . 5 1 , \ \eta = 0 . 8 , k = 0 . 8$ . The starting point of the horizontal axis is set to meet the parameters conditions.

Proposition 8 (Platform’s Profit and Total Profit):

(a) As the cost coeficient of misrepresentation $( i . e . , \alpha )$ increases, the platform’s profit increases $( i . e . , \ \frac { \partial \pi _ { R } ^ { C 4 * } } { \partial \alpha } > 0 )$ if and only $i f k > { \hat { k } }$ and $\begin{array} { r } { \Delta q < \sqrt { \frac { k \left[ 6 \alpha t - ( 1 - r ) ( 1 - k t ) ( 1 - 2 k t ) \right] ^ { 3 } } { ( 1 - k t ) \left[ 2 \alpha + k ( 1 - r ) ( 1 - 2 k t ) \right] ^ { 3 } } } . } \end{array}$ , and the total profit of the platform and the sellers increases $\begin{array} { r } { ( i . e . , \ \frac { \partial ( \pi _ { R } ^ { C 4 * } + \pi _ { H } ^ { C 4 * } + \pi _ { L } ^ { C 4 * } ) } { \partial \alpha } > 0 ) } \end{array}$ if and only $i f k > \overline { { \overline { { k } } } }$ and $\begin{array} { r } { \Delta q < \sqrt { \frac { k [ 6 \alpha t - ( 1 - r ) ( 1 - k t ) ( 1 - 2 k t ) ] ^ { 3 } \big [ k ( 1 - r ) ^ { 2 } ( 1 - 2 k t ) ^ { 3 } - 2 \alpha ( 1 - 2 k t ) ( 1 - r + 2 k ( 3 + r ) t ) \big ] } { ( 1 - 2 k t ) [ 2 \alpha + k ( 1 - r ) ( 1 - 2 k t ) ] ^ { 3 } \big [ 2 \alpha t ( 5 - 2 k t + r ( 3 - 6 k t ) ) - ( 1 - r ) ^ { 2 } ( 1 - 2 k t ) ^ { 2 } ( 1 - k t ) \big ] } } . } \end{array}$

(b) As the return policy leniency $( i . e . , k )$ increases, the platform’s profit increases $( i . e . , \frac { \partial \pi _ { R } ^ { C 4 * } } { \partial k } > 0 )$ if and only $i f k { > } \tilde { k }$ and $\begin{array} { r } { \Delta q < \sqrt { \frac { ( 4 k t - 1 ) \left[ 6 \alpha t - ( 1 - r ) ( 1 - k t ) ( 1 - 2 k t ) \right] ^ { 3 } } { t ( 3 - 4 k t ) \left[ 2 \alpha + k ( 1 - r ) ( 1 - 2 k t ) \right] ^ { 3 } } } ; } \end{array}$ , and the total profit of the platform and the sellers increases $\begin{array} { r } { ( i . e . , \quad \frac { \partial ( \pi _ { R } ^ { C 4 * } + \pi _ { H } ^ { C 4 * } + \pi _ { L } ^ { C 4 * } ) } { \partial k } > 0 ) } \end{array}$ if and only $i f { \bf \nabla } k > { \bf \ddot { k } }$ and $\begin{array} { r } { \Delta q < \sqrt { \frac { [ 6 \alpha t - ( 1 - r ) ( 1 - k t ) ( 1 - 2 k t ) ] ^ { 3 } \left[ 4 \alpha t \left( 1 + r - 2 k ( 3 + r ) t \right) - \left( 1 - r \right) ^ { 2 } \left( 1 - 2 k t \right) ^ { 3 } \right] } { t \left[ 2 \alpha + k \left( 1 - r \right) \left( 1 - 2 k t \right) \right] ^ { 3 } \left[ 4 \alpha t \left( - 3 + 2 k t - r ( 3 - 6 k t ) \right) + \left( 1 - r \right) ^ { 2 } \left( 1 - 2 k t \right) ^ { 3 } \right] } } , } \end{array}$

Proposition 8 shows that the efects of anti-misrepresentation strategies on the platform’s profit are not monotonic. Specifically, as the platform’s profit consists of a portion of both sellers’ profits, a stricter anti-misrepresentation strategy gives rise to two opposing forces. The first is the demand shifting efect. Increasing the cost coeficient of misrepresentation or increasing return policy leniency mitigates the equilibrium quality diference, leading to a higher level of demand for L and a lower level of demand for H $( \mathrm { i . e . , }$ the Proof for Proposition 4). Since H’s retail price is higher than $L ^ { \prime } s ,$ , this efect hurts the platform because its profit depends on the product price. The second force is the return-decreasing efect. Having a stricter anti-misrepresentation strategy can decrease the total misrepresentation level (i.e., Proposition 5) and lead to fewer product returns. This efect benefits the platform because its profit is related to the total amount of products sold. When the return policy leniency is suficiently high and the quality diference is relatively low $( \mathrm { i } . \mathrm { e } . , p _ { H } ^ { C 4 * }$ and $p _ { L } ^ { C 4 * }$ are not extremely diferent), the return-decreasing efect dominates the demand-shifting efect and having a stricter anti-misrepresentation strategy benefits the platform.

When we examine the total profits of the platform and sellers, the efects of antimisrepresentation strategies are not monotonic either. Specifically, whether increasing the misrepresentation cost or increasing return leniency increases the total benefits depends on the magnitude of return-decreasing efect and the demand-shifting efect.

As discussed earlier, the platform can have two objectives—one is to earn the profit from the commissions and the other is to deter sellers’ quality misrepresentation. If the platform prioritizes the former, implementing stricter anti-misrepresentation interventions is beneficial to the platform only if the return leniency exceeds a certain threshold $( k > \hat { k } )$ and the quality diference between H and L is suficiently low. Having stricter antimisrepresentation strategies decreases return but also shifts demand from H to L. If the return leniency is low or the quality advantage that H enjoys over L is quite large, the decrease in profits resulted from demand-shifting dominates the increase in profits resulted from decreased returns. Therefore, the platform’s profit may decrease as a result. In such a scenario, having stricter anti-misrepresentation strategies may not be aligned with platform’s objective to make profits. However, if the platform prioritizes deterring quality misrepresentation, having stricter anti-misrepresentation strategies will help deter quality misrepresentation (Proposition 6), and the platform can examine the market conditions to choose the specific anti-misrepresentation strategy (Proposition 7).

## Extensions

## Alternative Modeling Approaches for the Cost of Quality Misrepresentation

In this subsection, we extend our analyses by relaxing some assumptions on misrepresentation cost. First, one unique aspect of quality misrepresentation is that the perceived (manipulated) quality signals can only be persuasive in the pre-purchase stage and the inevitable misrepresentation cost is product returns. In the main analyses, we model the number of product returns by following the expectation–disconfirmation paradigm. In the Online Supplemental Appendix C, we consider an alternative product return function such that consumers consider returning products only if their post-purchase utility is negative [10, 68].

Second, in our main analyses, we assume that both sellers encounter the same misrepresentation cost (i.e., α). In the Online Supplemental Appendix D, we relax this assumption and consider the scenario where sellers encounter a diferent misrepresentation cost. Specifically, we consider a scenario where misrepresenting low quality to a higher quality (for L) is easier than misrepresenting a high quality to an even higher quality (for H), and a scenario where misrepresenting a low quality to be high quality (for L) is more dificult than stretching a high quality to an even higher quality (for H). In this extension, we show that H does not always conduct a higher misrepresentation level than L, and whether one seller earns more profit in Case 4 (compared to Case 1) also depends on the relative misrepresentation cost.

Third, in the Online Supplemental Appendix E, we extend our analyses by considering a scenario where sellers encounter an additional hassle cost when the product returns take place. We further examine scenarios where the additional cost of product return only happens to one seller (either H or L). Our analyses show that which seller is afected by the anti-misrepresentation strategy more depends on the specific strategy (i.e., increasing α or k), who sufers from the additional hassle cost (i.e., H or L), and the initial quality diference (i.e., Δq).

Forth, in our main analyses, when product return takes place, we assume that the platform would refund the sellers the associated commission fees (in Eq. (3)) because such an assumption better reflects the real-world practice<sup>8</sup> and helps us emphasize the efect of competition in the quality misrepresentation setting. In Online Supplemental Appendix F, we consider the scenario where the platform retains all commission fees from the returned product.

Finally, in Online Supplemental Appendix G, we adopt a cost function with both linear and quadratic components [48]. Our main results are robust to these alternative cost assumptions.

## Alternative Modeling Approaches for Market Setups

First, in our main analyses, we focus on the efect of sellers’ competition on price and quality misrepresentation level, and we model consumers’ quality perception by adding the quality misrepresentation level to the original quality. In Online Supplemental Appendix H, we examine our main results by modeling the consumers’ quality perception process as a Bayesian learning process [48, 61, 73, 74]. Second, in our main analyses, we assume that the market is fully covered, and the total demand (a unit mass of consumer base) is not influenced by the quality misrepresentation activities on the platform. In Online Supplemental Appendix I, we verify our results by considering a negative externality of quality misrepresentation on the total demand where the total demand on the platform decreases with the total quality misrepresentation [12]. The main results derived with these alternative market setups are consistent with those in our main analyses.

## Managerial Implications

The prevalence of online quality misrepresentation has provided an unprecedented challenge for e-commerce platforms. Our analytical findings have the following implications, which provide guidance for the implementation of anti-misrepresentation strategies on platforms.

Will all sellers choose to manipulate the quality information? Our analyses indicate that whether sellers choose to manipulate the quality information depends on the platform’s return policy leniency. When the return policy is not so lenient, both sellers would choose to manipulate the quality information. However, the cases where only one seller chooses to manipulate are not Nash equilibria. The result implies that platforms need to seriously consider adopting more lenient return policies and smoothing the return process, as all sellers are potentially incentivized to manipulate the quality signals in competition if consumers are reluctant to return products.

Does a stricter anti-misrepresentation strategy always reduce quality misrepresentation? Our results show that although a stricter anti-misrepresentation strategy, such as greater misrepresentation costs or a more lenient product return policy, will reduce the misrepresentation level of the high-quality seller, the misrepresentation level of the low-quality seller may increase. Our findings highlight that platforms should take the sellers’ competition into account: A stricter anti-misrepresentation strategy can afect the incentives of both high-quality and low-quality sellers simultaneously and may unexpectedly incentivize low-quality sellers to manipulate more. Platforms should consider the pros and cons of implementing a stricter antimisrepresentation strategy, especially when the quality diference between the competing sellers is large.

What is a better strategy to deter quality misrepresentation? Our analysis suggests that in terms of the efective range of market conditions, adopting a more lenient return policy might be a more efective strategy to deter quality misrepresentation of the lowquality seller than increasing the cost of misrepresentation. In terms of the reduced level of misrepresentation, adopting higher misrepresentation cost is more efective than incorporating a more lenient return policy if the misrepresentation cost is low.

In general, our findings remind practitioners that a stricter anti-misrepresentation strategy is not a panacea for all misrepresentation problems. The bottom line is that in online marketplaces where sellers compete on both price and quality misrepresentation, the platform should be fully aware of the market conditions under which a stricter antimisrepresentation strategy may increase certain sellers’ misrepresentation behaviors.

## Conclusions

In this study, we examine the impact of seller-initiated quality misrepresentation under the agency pricing regime, with particular attention to the strategic interaction between sellers pricing decisions and their quality misrepresentation decisions. We find that the case where both sellers choose not to manipulate and the case where both sellers choose to manipulate quality signals are pure-strategy Nash equilibria. However, the cases where only one seller chooses to manipulate are not equilibria. Furthermore, our analyses indicate that the impact of quality misrepresentation and anti-misrepresentation strategies on diferent sellers varies. In the case where both sellers compete on prices and quality signals, the platform’s stricter anti-misrepresentation strategy (i.e., increasing misrepresentation cost and adopting a more lenient product return policy) will reduce the misrepresentation level of the high-quality seller, but may unintendedly increase the misrepresentation level of the lowquality seller. Moreover, a stricter anti-misrepresentation strategy is beneficial to the lowquality seller but can be detrimental to the high-quality seller. Our results also indicate that increasing return leniency can deter low-quality seller’s quality misrepresentation level in a wider range of market conditions than increasing the misrepresentation cost. Last, but not least, our results shed light on the efects of diferent anti-misrepresentation strategies based on the platforms’ diferent objectives. These results have important implications for the sellers and platforms.

There are several possible extensions that present future research opportunities. First, the role of quality misrepresentation is modeled here as an increase in consumers’ perceived quality because we focus on the efect of sellers’ competition in price and the quality misrepresentation level. Experienced consumers or strategic consumers [29], however, may recognize the manipulated quality signals and leave a platform or even form a lower level of quality perception because they stop trusting it. Future studies could analyze how diferent consumers react to manipulated quality information. Second, in our model, we only consider positive quality misrepresentation by the sellers. However, it would be of interest to examine the impact of negative quality misrepresentation from competitors. Third, to highlight our focus, our analyses only consider product returns as a natural cost of quality misrepresentation. A future study, though, could also consider uncertainty-caused product returns in the analyses. Forth, this study assumes that the commission fee is exogenously given to highlight our focus and ensure analytical tractability. A future study could make it an endogenous decision variable for the platform in numerical analyses. Finally, due to our model limitation, we are not able to derive the consumer surplus and social welfare, which can be an interesting aspect for future study.

## Notes

1. We assume that consumers do not know that the quality signals are manipulated at the prepurchase stage [49]. This assumption is consistent with practice. For example, the accuracy of individuals’ lie-truth judgments is found to be only 54 percent [5]. Since all product returns are caused by expectation disconfirmation, consumers are not able to anticipate the product return at the pre-purchase stage.

2. This condition can also be illustrated as $\Delta q > \frac { 3 t ( 1 - \eta ) } { 1 + \eta }$ ; The feasible region of Δq (or $q _ { H } )$ always exists because $\begin{array} { r } { \frac { 6 \alpha t - ( 1 - r ) ( 1 - k t ) ( 1 - 2 k t ) } { 2 \alpha + k ( 1 - r ) ( 1 - 2 k t ) } > \frac { 3 t ( 1 - \eta ) } { 1 + \eta } } \end{array}$ always holds.

3. This assumption is aligned with the reality. For example, electronic marketplaces normally list the products with similar average rating and popularity in the same recommendation list [45].

4. If we set the total demand as $D ^ { \check { T } }$ , Assumption A2 would be accordingly updated as $\begin{array} { r } { k < \frac { D ^ { T } } { 2 t } } \end{array}$

5. For example, Narvar investigates on consumers’ satisfaction with the online product return process. The survey collected in 2019 shows that a substantial portion of online shoppers do not find the returns process easy, and only 60 percent of consumers indicate they are satisfied with their recent return.

See https://see.narvar.com/Consumer\_Report-Returns\_LP.html (last accessed on May 8th, 2020).

6. If we follow Dellarocas [19] and adopt a model where the retail prices are pre-determined as $ { p _ { H } ^ { C 1 * } }$ and $p _ { L } ^ { C 1 * }$ , both sellers would sufer from the prisoner’s dilemma. In such case, $\widetilde { \pi _ { H } ^ { C 4 * } } < \pi _ { H } ^ { C 1 * }$ and $\pi _ { L } ^ { C 4 * } < \pi _ { L } ^ { C 1 * }$ always hold. The detailed proof is in the Online Supplemental Appendix A.

7. In the equilibrium results, high initial quality diference also stands for high perceived quality diference between the two products in the equilibrium (see Eq. (4)).

8. For example, Amazon specifies that for the media orders, it credits back all the original orderrelated fees to sellers. For the non-media orders, only a small portion of original order-related fees will be retained (up to \$5) by Amazon. See https://sellercentral.amazon.com/gp/help/ external/G21531?language=en\_US (last accessed on May 8, 2020).

9. In economics, an externality is the cost or benefit that afects a third party who does not choose to incur that cost or benefit [7]. We focus on the negative externality, which is the activity that imposes a negative efect on an unrelated third party. In our context, a seller’s manipulation activity can hurt the other seller’s demand on the same platform. The negative externality in this setting is that even if a focal seller does not involve much in quality misrepresentation, consumers may quit the platform and do not purchase the product of the focal seller because the misrepresentation level of its competitor on the platform is high.

## Disclosure Statement

No potential conflict of interest was reported by the authors.

## Notes on contributors

Jingchuan Pu (jingchuan@ufl.edu) is an assistant professor in the Department of Information Systems and Operations Management, Warrington College of Business, University of Florida. He was an assistant professor at Smeal College of Business, Pennsylvania State University. He received his Ph.D. in Information Systems from University of Florida. Dr. Pu’s research focuses on social media (public and corporate), fintech, and e-commerce. His work has appeared in premier academic journals, such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and Production and Operations Management.

Tingting Nian (tnian@uci.edu) is an assistant professor of Information Systems and a Hellman fellow in the Paul Merage School of Business at University of California at Irvine. She received her Doctoral degree in Information Systems from the Leonard N. Stern School of Business, New York University.

Dr. Nian has received several grants and awards from institutions including Think Forward Initiative, Hellman Foundation, Wharton Customer Analytics Initiative and INFORMS. Her work has appeared in Management Science, MIS Quarterly, and Information Systems Research.

Liangfei Qiu (liangfei.qiu@warrington.ufl.edu; corresponding author) is the PricewaterhouseCoopers Associate Professor in the Department of Information Systems and Operations Management, Warrington College of Business, University of Florida. He received his Ph.D. from University of Texas at Austin. Dr. Qiu’s research focuses on prediction markets, social networks and social media platforms, telecommunications networks, and economics of information systems. His work has appeared in premier academic journals, such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly and, Production and Operations Management. He serves as Associate Editor at MIS Quarterly, Senior Editor at Production and Operations Management, and Associate Editor at Decision Support Systems.

Hsing Kenneth Cheng (hkcheng@ufl.edu) is the John B. Higdon Eminent Scholar and Department Chair in the Department of Information Systems and Operations Management, Warrington College of Business, University of Florida. He received his Ph.D. from University of Rochester. Dr. Cheng’s research interests focus on analyzing the impact of Internet technology on software development and marketing, and on information systems policy issues. His work has appeared in premier academic journals, such as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, and Production and Operations Management.

## ORCID

Liangfei Qiu http://orcid.org/0000-0002-8771-9389

## References

1. Abhishek, V.; Jerath, K.; and Zhang, Z.J. Agency selling or reselling? Channel structures in electronic retailing. Management Science, 62, 8 (2015), 2259–2280.

2. Ba, S.; Whinston, A.B.; and Zhang, H. Building trust in online auction markets through an economic incentive mechanism. Decision Support Systems, 35, 3 (2003), 273–286.

3. Banks, J.S.; and Sobel, J. Equilibrium selection in signaling games. Econometrica, 55, 3 (1987), 647–661.

4. Bechwati, N.N.; and Siegal, W.S. The impact of the prechoice process on product returns. Journal of Marketing Research, 42, 3 (2005), 358–367.

5. Bond Jr, C.F.; and DePaulo, B.M. Accuracy of deception judgments. Personality and Social Psychology Review, 10, 3 (2006), 214–234.

6. Boudreau, K.J., and Hagiu, A. Platform rules: Multi-sided platforms as regulators. In A. Gawer () (ed.), Platforms, Markets and Innovation. Edward Elgar Publishing. 2009, Cheltenham, UK: pp.163–191.

7. Buchanan, J.; and Stubblebine, W.C. Externality. Economica, 29, 116 (1962), 371–384.

8. Cai, H.; Chen, Y.; and Fang, H. Observational learning: Evidence from a randomized natural field experiment. American Economic Review, 99, 3 (2009), 864–882.

9. Carbone, C. Amazon has a major problem with thousands of fake reviews, Report claims. Fox News, April 16, 2018February 7, 2022. https://www.foxnews.com/tech/amazon-has-a-majorproblem-with-thousands-of-fake-reviews-report-claims .

10. Che, Y.-K. Customer return policies for experience goods. The Journal of Industrial Economics, 44, 1 (1996), 17–24.

11. Chen, L.; Nan, G.; and Li, M. wholesale pricing or agency pricing on online retail platforms: The efects of customer loyalty. International Journal of Electronic Commerce, 22, 4 (2018), 576–608.

12. Cheng, H.K.; Liu, Y.; and Tang, Q. The impact of network externalities on the competition between open source and proprietary software. Journal of Management Information Systems, 27, 4 (2011), 201–230.

13. Chevalier, J.A.; and Mayzlin, D. The efect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43, 3 (2006), 345–354.

14. Chiang, I.R.; and Jhang-Li, J.H. Delivery consolidation and service competition among internet service providers. Journal of Management Information Systems, 31, 3 (2014), 254–286.

15. Cho, I.K.; and Kreps, D.M. Signaling games and stable equilibria. The Quarterly Journal of Economics, 102, 2 (1987), 179–221.

16. Cho, S.; Qiu, L.; and Bandyopadhyay, S. Vertical integration and zero-rating interplay: An economic analysis of ad-supported and ad-free digital content. Journal of Management Information Systems, 37, 4 (2020), 988–1014.

17. Davis, S.; Gerstner, E.; and Hagerty, M. Money back guarantees in retailing: Matching products to consumer tastes. Journal of Retailing, 71, 1 (1995), 7–22.

18. De, P.; Hu, Y.; and Rahman, M.S. Product-oriented web technologies and product returns: An exploratory study. Information Systems Research, 24, 4 (2013), 998–1010.

19. Dellarocas, C. Strategic Manipulation of Internet Opinion Forums: Implications for Consumers and Firms. Working Paper2004. February 7, 2022.https://ssrn.com/abstract= 585404 .

20. Dellarocas, C. Strategic manipulation of internet opinion forums: Implications for consumers and firms. Management Science, 52, 10 (2006), 1577–1593.

21. Dimensional Research. The Impact of Customer Service on Customer Lifetime Value. Dimensional Research, 2013. February 7, 2022. https://www.zendesk.com/resources/customerservice-and-lifetime-customer-value/ .

22. Fan, M., Kumar, S.; and Whinston, A.B. Selling or advertising: Strategies for providing digital media online. Journal of Management Information Systems, 24, 3 (2007), 143–166.

23. Fang, B., Zheng, Z.; Ye, Q.; and Goes, P.B. Social influence and monetization of freemium social games. Journal of Management Information Systems, 36, 3 (2019), 730–754.

24. Feng, Y.; Guo, Z.; and Chiang, W.Y.K. Optimal digital content distribution strategy in the presence of the consumer-to-consumer channel. Journal of Management Information Systems, 25, 4 (2009), 241–270.

25. Ferguson, M.; Guide Jr, V.D.R.; and Souza, G.C. Supply chain coordination for false failure returns. Manufacturing & Service Operations Management, 8, 4 (2006), 376–393.

26. Gardete, P. M. Cheap-talk advertising and misrepresentation in vertically diferentiated markets. Marketing Science, 32, 4 (2013), 609–621.

27. Gu, Z. J.; and Xie, Y. Providing fit-revealing information in the competitive market. Management Science, 59, 5 (2013), 1196–1212.

28. Guo, Z. Optimal decision making for incentive-based word-of-mouth marketing. Decision Support Systems, 52, 2 (2012), 373–383.

29. Guo, Z.; and Chen, J. Multigeneration product difusion in the presence of strategic consumers. Information Systems Research, 29, 1 (2018), 206–224.

30. Hao, L.; and Fan, M. An analysis of pricing models in the electronic book market. MIS Quarterly, 38, 4 (2014), 1017–1032.

31. Hastak, M.; and Mazis, M.B. Deception by implication: A typology of truthful but misleading advertising and labeling claims. Journal of Public Policy & Marketing, 30, 2 (2011), 157–167.

32. Ho, Y.C.; Ho, Y.J.; and Tan, Y. Online cash-back shopping: Implications for consumers and e-businesses. Information Systems Research, 28, 2 (2017), 250–264.

33. Hong, Y.; and Pavlou, P.A. Product fit uncertainty in online markets: Nature, efects, and antecedents. Information Systems Research, 25, 2 (2014)., 328–344.

34. Hotelling, H. Stability in competition. Economic Journal, 39, 153 (1929), 41–57.

35. Hsieh, J.K.; and Li, Y.J. Will you ever trust the review website again? The importance of source credibility. International Journal of Electronic Commerce, 24, 2 (2020), 255–275.

36. Jiang, Y.; and Guo, H. Design of consumer review systems and product pricing. Information Systems Research, 26, 4 (2015), 714–730.

37. Khouja, M.; and Liu, X. A retailer’s decision to join a promotional event of an e-commerce platform. International Journal of Electronic Commerce, 24, 2 (2020), 184–210.

38. Kim, D.J.; Ferrin, D.L.; and Rao, H.R. Trust and satisfaction, two stepping stones for successful e-commerce relationships: A longitudinal exploration. Information Systems Research, 20, 2 (2009), 237–257.

39. Kumar, A.; Mehra, A.; and Kumar, S. Why do stores drive online sales? Evidence of underlying mechanisms from a multichannel retailer. Information Systems Research, 30, 1 (2019), 319–338.

40. Kumar, N.; Venugopal, D.; Qiu, L.; and Kumar, S. Detecting anomalous online reviewers: An unsupervised approach using mixture models. Journal of Management Information Systems, 36, 4 (2019), 1313–1346.

41. Kumar, N.; Venugopal, D.; Qiu, L.; and Kumar, S. Detecting review manipulation on online platforms with hierarchical supervised learning. Journal of Management Information Systems, 35, 1 (2018), 350–380.

42. Kwark, Y.; Chen, J.; and Raghunathan, S. Platform or wholesale? A strategic tool for online retailers to benefit from third-party information. MIS Quarterly, 41, 3 (2017), 763–785.

43. Lee, H.C. (Brian); and Li, X. Impact of online word of mouth on channel disintermediation for information goods. Journal of Management Information Systems, 35, 3 (2018), 964–993.

44. Lee, S.Y.; Qiu, L.; and Whinston, A. Sentiment manipulation in online platforms: An analysis of movie tweets. Production and Operations Management, 27, 3 (2018), 393–416.

45. Li, L.; Chen, J.; and Raghunathan, S. Advertising role of recommender systems in electronic marketplaces: A boon or a bane for competing sellers? MIS Quarterly, 44, 4 (2020), 1957–1985.

46. Li, Q.; Wang, Q.; and Song, P. The efects of agency selling on reselling on hybrid retail platforms. International Journal of Electronic Commerce, 23, 4 (2019), 524–556.

47. Luo, X.; Zhang, J.J.; Gu, B.; and Phang, C. Expert blogs and consumer perceptions of competing brands. MIS Quarterly, 41, 2 (2013), 371–395.

48. Mayzlin, D. Promotional chat on the internet. Marketing Science, 25, 2 (2006), 155–163.

49. Mayzlin, D.; Dover, Y.; and Chevalier, J. Promotional reviews: An empirical investigation of online review manipulation. American Economic Review, 104, 8 (2014), 2421–2455.

50. McGuire, T.W.; and Staelin, R. An industry equilibrium analysis of downstream vertical integration. Marketing Science, 2, 2 (1983), 161–191.

51. McKinney, V.; Yoon, K.; and Zahedi, F.M. The measurement of web-customer satisfaction: An expectation and disconfirmation approach. Information Systems Research, 13, 3 (2002), 296–315.

52. Miranda, L. Some Amazon sellers are paying \$10,000 a month to trick their way to the top. Buzzfeed News, April 24. February 7, 2022, 2019, https://www.buzzfeednews.com/article/ leticiamiranda/amazon-marketplace-sellers-black-hat-scams-search-rankings .

53. Nan, G.; Yao, L.; Ho, Y.C.; Li, Z.; and Li, M. An economic analysis of platform protection in the presence of content substitutability. Journal of Management Information Systems, 36, 3 (2019), 1002–1036.

54. Nicolucci, D. War is on: How to fight unfair competition on Amazon. Linkedin, November 21, February 7, 2022. 2018. https://www.linkedin.com/pulse/war-how-fight-unfair-competitionamazon-davide-nicolucci/ .

55. Oliver, R.L. A cognitive model of the antecedents and consequences of satisfaction decisions. Journal of Marketing Research, 17, 4 (1980), 460–469.

56. Parker, G.; and Van Alstyne, M. Innovation, openness, and platform control. Management Science, 64, 7 (2018), 3015–3032.

57. Perez, S. Amazon bans incentivized reviews tied to free or discounted products. February 7, 2022, 2016.https://techcrunch.com/2016/10/03/amazon-bans-incentivized-reviews-tied-tofree-or-discounted-products/

58. Petersen, J. A.; and Kumar, V. Are product returns a necessary evil? Antecedents and consequences. Journal of Marketing, 73, 3 (2009), 35–51.

59. Pu, J.; Kwark, Y.; Han, S.; Gu, B.; and Ye, Q. The double-edged sword of expert reviewer programs: The efects of ofering expert reviewer status on review generation. Seoul: Proceedings of the International Conference on Information Systems (ICIS), 2017, pp. 1–17.

60. Pu, X.; Sun, S.; and Shao, J. Direct selling, reselling, or agency selling? Manufacturer’s online distribution strategies and their impact. International Journal of Electronic Commerce, 24, 2 (2020), 232–254.

61. Qiu, L.; Cheng, K. H.; and Pu, J. Hidden profiles in corporate prediction markets: The impact of public information precision and social interactions. MIS Quarterly, 41, 4 (2017), 1249–1273.

62. Qiu, L.; Shi, Z.; and Whinston, A.B. Learning from your friends’ check-ins: An empirical study of location-based social networks. Information Systems Research, 29, 4 (2018), 1044–1061.

63. ReviewMeta. Analysis of 7 Million Amazon reviews: Customers who receive free or discounted item much more likely to write positive review. ReviewMeta. February 7, 2022, 2016. https:// reviewmeta.com/blog/analysis-of-7-million-amazon-reviews-customers-who-receive-free-ordiscounted-item-much-more-likely-to-write-positive-review

64. Rochet, J.C.; and Tirole, J. Two-sided markets: A progress report. RAND Journal of Economics, 37, 3 (2006), 645–667.

65. Sahoo, N.; Dellarocas, C.; and Srinivasan, S. The impact of online product reviews on product returns. Information Systems Research, 29, 3 (2018), 723–738.

66. Shulman, J.D.; Coughlan, A.T.; and Savaskan, R.C. Optimal reverse channel structure for consumer product returns. Marketing Science, 29, 6 (2010), 1071–1085.

67. Stevens, L., and Emont, J. How sellers trick Amazon to boost sales. The Wall Street Journal, July 28, 2018. February 7, 2022. https://www.wsj.com/articles/how-sellers-trick-amazon-toboost-sales-1532750493

68. Su, X. Consumer returns policies and supply chain performance. Manufacturing & Service Operations Management, 11, 4 (2008), 595–612.

69. Van Osselaer, S.M.; and Alba, J.W. Consumer learning and brand equity. Journal of Consumer Research, 27, 1 (2000), 1–16.

70. Wang, L.; Mo, J., and Li, B. An empirical investigation of sales cheating efect in e-commerce. In Proceedings of the International Conference on Information Systems (ICIS), San Francisco, 2018, pp. 1–9.

71. Wong, G.; Chu, K.; and Osawa, J. Inside Alibaba, the sharp-elbowed world of Chinese e-Commerce. The Wall Street Journal February 7, 2022, March 2, 2018.https://www.wsj.com/ articles/inside-alibaba-the-sharp-elbowed-world-of-chinese-e-commerce-1425332447

72. Xin, M.; and Choudhary, V. IT investment under competition: The role of implementation failure. Management Science, 65, 4 (2019), 1909-1925.

73. Zhao, X.; Tian, J.; and Xue, L. Herding and software adoption: A re-examination based on post-adoption software discontinuance. Journal of Management Information Systems, 37, 2 (2020), 484–509.

74. Zhao, X.; and Xue, L. Competitive target advertising and consumer data sharing. Journal of Management Information Systems, 29, 3 (2012), 189–222.

75. Zhou, W.; and Duan, W. Do professional reviews afect online user choices through user reviews? An empirical study. Journal of Management Information Systems, 33, 1 (2016), 202–228.
