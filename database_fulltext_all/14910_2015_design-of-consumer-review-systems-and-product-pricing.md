---
otero_id: 14910
otero_key: "H4MT43JU"
title: "Design of Consumer Review Systems and Product Pricing"
authors: "Yabing Jiang; Hong Guo"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0594"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.93.16.3] On: 01 November 2015, At: 02:01 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## HSR

## Information Systems Research

![](/api/attachments/H4MT43JU/fulltext/images/3a50feab8bc32ecbcc4e1fff3ce02f6edde355448c85e300a72ebc5f10e5e985.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Design of Consumer Review Systems and Product Pricing

Yabing Jiang, Hong Guo

To cite this article:

Yabing Jiang, Hong Guo (2015) Design of Consumer Review Systems and Product Pricing. Information Systems Research

Published online in Articles in Advance 05 Oct 2015

http://dx.doi.org/10.1287/isre.2015.0594

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/H4MT43JU/fulltext/images/a4ad292d0d4565dea38e69cb6be823761a24990cc88518e9fdc76b547dab949b.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Design of Consumer Review Systems and Product Pricing

Yabing Jiang

Lutgert College of Business, Florida Gulf Coast University, Fort Myers, Florida 33965, yjiang@fgcu.edu

Hong Guo

Mendoza College of Business, University of Notre Dame, Notre Dame, Indiana 46556, hguo@nd.edu

onsumer review systems have become an important marketing communication tool through which consumers share and learn product information. Although there is abundant evidence that consumer reviews have a significant impact on product sales, the design of consumer review systems and its impact on review outcomes and product sales have not yet been well examined. This paper analyzes firms’ review system design and product pricing strategies. We formally model two review system design decisions—what rating scale cardinality to use and whether to offer granular review reports. We show that firms’ optimal design and pricing strategies critically depend on contextual characteristics such as product valuation, product mainstream level, and consumer misfit cost. Our results suggest that it is beneficial to host a review system only when the product valuation is higher than a threshold. Furthermore, firms should choose low rating scale cardinality for niche products and high rating scale cardinality for mainstream products. When consumers’ misfit cost is relatively high, including granular reports in the review system enables firms to attract the favorable consumer segment. Different pricing strategies should be deployed during the initial sale period for different product types. For niche products, firms are advised to adopt lower-bound pricing for high-quality products to take advantage of the positive word of mouth. For mainstream products, firms are advised to adopt upper-bound pricing for high-quality products to enjoy the direct profit from the initial sale period, even after taking into account the negative impact of high price on consumer reviews.

Keywords: economics of IS; electronic commerce; consumer reviews; online word-of-mouth systems; product uncertainty

History: Alok Gupta, Senior Editor; De Liu, Associate Editor. This paper was received on June 5, 2012, and was with the authors 18 months for 4 revisions. Published online in Articles in Advance.

## Introduction

With the prevalence of the Internet and the success of e-commerce, consumers increasingly resort to the Web to gather information about products of interest before making their purchasing decisions. Consumer reviews (user-generated product reviews) represent one of the most popular and influential information sources in shaping consumers’ purchasing behavior. According to a recent study by E-tailing Group (2010), 71% of online shoppers stated that consumer reviews have the greatest impact on their product researching experience. In response, many firms have adopted consumer review systems as a marketing communication tool to facilitate consumer sharing and learning about their products (Chen and Xie 2008). Both firms and consumers benefit from such review systems. Prospective customers can read reviews from previous customers to learn more about the products and make more informed purchasing decisions. Consumer review systems also help firms improve customer services, lower return rates, increase conversions from browsers to buyers, and better respond to consumer needs through product improvement, logistic planning, assortment, and price adjustment (Mangalindan 2007, Fowler 2009).

Existing literature has shown that consumer reviews have significant impact on product sales. However, little is known about the impact of the design of review systems on customer review outcomes and product sales. This paper analytically studies a firm’s review system design decisions regarding when to offer a review system, what type of rating scales to use, whether to present reports with specific product attribute ratings in the review system, and how product and consumer characteristics moderate these design decisions. We formally derive the firm’s optimal pricing strategy together with its review system design decisions and examine the strategic interaction between these decisions.

We observe different review system design choices among popular online consumer review systems. IMDb allows customers to rate a movie on a scale of 1 to 10, whereas many retailers such as Amazon,

## Figure 1 (Color online) An Example of Granular Review Reports

![](/api/attachments/H4MT43JU/fulltext/images/1c27e7701cac27035981459ccc5b4e8b5629d69e55f304ebe5f3f25fa65b8148.jpg)

L.L.Bean, Macy’s, Target, and Walmart let customers rate a product on a scale of 1 to 5, and YouTube’s “like/dislike” button enables a binary positive or negative rating. We refer to these types of rating scales as “rating scale cardinality.” Whether and how the rating scale cardinality affects customer reviews and consumers’ perception of the reviewed products are still open research questions.

Other than the overall product rating, we also observe that, recently, more and more retailers have begun to seek additional reviews about specific product attributes. Because one of the major concerns of online shopping is that consumers cannot touch and feel the product or try it on, providing specific attribute ratings can help potential consumers better evaluate how well the product might fit their personal preferences. Figure 1 shows an example of product attribute reviews. In addition to displaying the overall 4.5/5 average rating, it also shows customers’ rating on the length and width of the reviewed boots as well as how many reviewers think the boots are comfortable, durable, performing as expected, etc. We refer to such aggregated reports with specific product attribute ratings as “granular reports.” They are easy to comprehend and convenient to access for consumers, and they enable consumers to learn more about the products than from the overall rating alone. Because of consumers’ diversified personal tastes and preferences, these wide-fitting boots may be considered a good fit by some consumers, but a bad fit by others. As a result, customers will have less postpurchase “surprises” about the boots and their attributes.

Depending on products, review systems hosted by L.L.Bean, Macy’s, Target, and Walmart invite customers to further rate a prespecified set of product attributes, such as appearance, comfort, ease of use, style, true to color, true to size, etc. However, not all sites offer such granular reports, and even for sites that do offer them, they are not provided for all products. This indicates that whether to provide granular reports is a review system design choice, and firms may choose differently for different products.

This paper makes three key contributions to the literature of consumer product reviews: First, we formally model a firm’s two design decisions regarding its review systems (what rating scale cardinality to use and whether to offer granular reports) and analyze the impact of these two design features on consumer ratings and the firm’s profit. Second, whereas most of the consumer review literature focuses on the rating interpretation process, we take a holistic approach and analyze both the consumer rating process (of past customers) and the rating interpretation process (of future consumers). Third, we analyze the interaction between the firm’s pricing and its review system design decisions and examine how contextual factors—product valuation, product mainstream level, and consumer misfit cost—affect the firm’s optimal decisions.

Our results suggest that it is beneficial for a firm to host a review system only when the product valuation is higher than a threshold. If they decide to host a review system, firms should choose low rating scale cardinality (such as like/dislike) for niche products and high rating scale cardinality (such as 10 stars) for mainstream products. In addition, different pricing strategies should be deployed during the initial sale period for different product types. For niche products, firms are advised to set a low price in the early sales period for high-valuation items to take advantage of the positive word-of-mouth effect in the later period. For mainstream products, firms are advised to set a high price for high-valuation items to enjoy the direct profit from the initial sale period, even after taking into account the negative impact of high price on consumer reviews.

We show that providing granular review reports can help firms reduce consumer product fit uncertainty and enable firms to target a favorable consumer segment with a higher price and reduced operational costs such as returns (Mangalindan 2007, Fowler 2009). Firms should apply this strategy to attract the favorable consumer segment when misfit cost is relatively high. These results have important implications for the design of online consumer review systems and firms’ corresponding pricing strategies.

This paper proceeds as follows: we review related literatures in the subsequent section. We next propose a model of online consumer review systems. In the following two sections, we analyze the firm’s pricing and review system design decisions in a baseline model without granular review reports and an extended model with granular review reports. Finally, we conclude with managerial implications and directions for future research.

## Literature Review

Online word-of-mouth systems, such as reputation systems, product review systems, and online referral systems, have been widely studied in the fields of marketing and information systems. Researchers have identified different roles of online word-of-mouth systems. One research stream views online word-ofmouth systems as a reputation mechanism (Dellarocas 2003, Bakos and Dellarocas 2011), and papers in this research stream focus on building trust and reducing seller uncertainty. Another research stream views online word-of-mouth systems as a marketing communication tool (Godes and Mayzlin 2004; Chen and Xie 2005, 2008; Dimoka et al. 2012), and papers in this research stream focus on communicating product information to consumers and reducing their uncertainty about products. This paper takes the product information view of online word-of-mouth systems and studies one particular type of such systems— online consumer review systems. Hence, our review next focuses on literature relating to consumer review systems.

Consumer review systems have been studied both empirically and analytically in the literature. Prior empirical research has often focused on studying whether online consumer reviews affect consumers’ purchasing decisions by examining the correlation between general review outcomes (such as mean rating and review volume) and product sales. For example, Chevalier and Mayzlin (2006), Clemons et al. (2006), and Zhu and Zhang (2010) find that mean rating is positively related to sales. Dellarocas et al. (2007) show that consumer reviews increase the accuracy of forecasting box office revenue. Similarly, Liu (2006) finds that consumer reviews offer significant explanatory power for box office revenue, and most of the explanatory power comes from the review volume. Duan et al. (2008) find that a movie’s box office revenue and mean consumer rating significantly influence the volume of consumer reviews, and the volume of consumer reviews, in turn, significantly influences the box office revenue. Although mean rating and review volume are commonly used review outcomes in these studies (Dellarocas et al. 2007, 2010; Duan et al. 2008; Gao et al. 2015), some also include additional review outcomes such as textual review content (Archak et al. 2011), percentages of one-star and five-star ratings (Chevalier and Mayzlin 2006, Hu et al. 2009), standard deviation (Clemons et al. 2006), and coefficient of variance (Zhu and Zhang 2010). However, these empirical papers do not study firms’ review system design decisions, and instead they treat the review system design as given. For example, most of the review systems being studied have a five-star rating scale (Chevalier and Mayzlin 2006; Dellarocas et al. 2007, 2010; Forman et al. 2008; Hu et al. 2009; Archak et al. 2011; Gao et al. 2015), whereas some use a rating scale cardinality of 10 (Duan et al. 2008, Zhu and Zhang 2010). Archak et al. (2011) also show that textual review can be used to learn consumers’ preferences for different product features and to help predict product sales. However, none of these papers looks into the impact of granular review reports, a recently emerged design feature of consumer review systems in e-commerce.

Empirical studies have also shown that many contextual factors such as product and consumer characteristics moderate the impact of consumer reviews on sales, such as product mainstream level (Zhu and Zhang 2010, Sun 2012), product publicity and product age (Archak et al. 2011), reviewer identity (Forman et al. 2008), consumer Internet experience (Zhu and Zhang 2010), etc. However, little is known of firms’ strategic responses to specific contextual conditions and how firms’ strategic decisions affect consumer reviews. To fill this gap, we formally model three contextual characteristics in this paper—product valuation, product mainstream level, and consumer misfit cost—and study their impact on a firm’s pricing and review system design decisions.

Analytical research has shown that firms offer review systems to facilitate consumer learning of products (Chen and Xie 2008, Kuksov and Xie 2010, Sun 2012). Whereas this stream of research has usually considered firms’ pricing decisions and the impact of other market factors such as product cost, market growth, and the composition of expert and novice consumers, less attention has been paid to firms’ review system design choices. Chen and Xie (2008) view consumer reviews as an imperfect signal of whether the product is a match or mismatch, and they do not model the firm’s choice of rating scale cardinality. In a two-period model, Kuksov and Xie (2010) investigate a firm’s strategy of enhancing customer ratings by either decreasing price or offering frills, or doing both. They adopt a binary rating model and do not consider whether the cardinality of rating scales has an impact on consumer learning and the firm’s strategy. Sun (2012) considers a review system of continuous rating scale and perfect customer learning and focuses on demonstrating the impact of the interaction between the variance of the ratings and the average rating on product sales. These analytical papers do not study firms’ review system design decisions and their interaction with firms’ other decisions such as pricing, which is the focus of this paper.

From the system design perspective, this paper is related to the literature on information systems design. Design of information systems has been shown to have a significant impact on firms’ operations and performance for business-to-business electronic markets (Basu and Hevner 1992), online referral marketing programs (Guo 2012), procurement auction systems (Greenwald et al. 2010), keyword auction systems (Liu et al. 2010), bundle trading markets (Guo et al. 2012), and software development systems (Ji et al. 2005, 2011). This paper further expands the information systems design literature to the domain of online consumer review systems.

## Model

## Firm and Consumers

We consider a monopolist firm selling a product and study the firm’s review system design choices and its pricing strategies in a two-period model. There are two independent groups of identical consumers, with one group arriving in the first period and the other arriving in the second period. The total number of consumers in each period is normalized to one. At the beginning of the first period, the firm makes its pricing and review system design decisions. Because the firm may charge different prices in the two periods, first-period consumers may choose to purchase in the first period or wait to purchase in the second period. If the firm chooses to host an online product review system, customers who purchase in the first period may post their product reviews, and consumers in the second period can learn from these reviews before making their purchasing decisions. Each consumer only demands one unit of the product in her lifetime, and there is no activity after the second period.

Consumers have a common valuation v for the product, but are heterogeneous in terms of their preferences for different product attributes, i.e., consumer taste preference. Without loss of generality, we use a unit line to represent the relative distance between consumer taste preference and the product. A consumer with a relative distance $x \in [ 0 , 1 ]$ incurs a misfit cost of tx, where t is the unit consumer misfit cost. Hence, a consumer with a higher x incurs a higher misfit cost, and we use $v - t x$ to represent consumers’ different willingness to pay for the product. Although consumers, in general, uniformly prefer high-quality to low-quality products, they may attach different levels of importance to different dimensions of quality, such as comfort or durability. Here we use product fit to capture how the product matches consumers’ overall taste preferences for both horizontal and quality-related product attributes. We model the density function of consumer misfit distribution as $f ( x ) = \overleftarrow { \theta } + 2 x ( 1 - \theta )$ , where $0 \leq \theta \leq 2$ represents the product mainstream level. Figure 2 illustrates three examples of consumer misfit distribution, which correspond to three product types with different mainstream levels. For $\theta = 1$ , the density function $f ( x ) = 1$ represents a uniform distribution and corresponds to neutral products. For $0 \leq \theta < 1$ , more consumers have a long distance to the product (high product misfit), and therefore this product type corresponds to niche products with narrow appeal. For $\bar { 1 \mathbf { \eta } } < \theta \leq 2 ,$ more

## Figure 2 Examples of Consumer Misfit Distribution

![](/api/attachments/H4MT43JU/fulltext/images/44e93da9ce6b4d569794e89b9a1c08722ea3a7b5a635bee56ce9e106362c6f23.jpg)

consumers have a short distance to the product (low product misfit), and therefore this product type corresponds to mainstream products with broad appeal.

The firm knows its product valuation v, but it does not know individual consumers’ misfit because it does not know their taste preferences. Consumers, on the other hand, know product mainstream level  and their own taste preferences, but they do not know product valuation v or how the product fits their specific tastes (i.e., their own misfit) before consumption. However, consumers share common prior beliefs that product valuation v is uniformly distributed on $[ \underline { { v } } , \bar { v } ] ,$ where $\bar { v } > \underline { { v } } > 0 ,$ , and their own misfit x is distributed on 0 1 according to the density function f x.

In summary, consumers have two types of product uncertainty—valuation uncertainty and misfit uncertainty. Before consumption, consumers’ expected product valuation is $\hat { v } = \bar { ( } \underline { { v } } + \bar { v } ) / 2$ , and their expected product misfit is $\begin{array} { r } { \hat { x } = \int _ { 0 } ^ { 1 } x f ( x ) d x = ( 4 - \theta ) / 6 , \mathrm { i . e . , } } \end{array}$ they have a higher expected misfit for niche products and a lower expected misfit for mainstream products.

## Design of Consumer Review Systems

When the firm hosts an online review system, secondperiod consumers can learn more about the product from reviews and update their beliefs on product valuation and fit accordingly. In terms of review system design, the firm needs to decide the cardinality of rating scales and whether to offer granular reports. We use $s \in Z$ and $s \geq 2$ to denote the cardinality of rating scales. For example, $s = 2$ corresponds to the case of two rating levels such as “like/dislike,” and $s = 5$ corresponds to the case of five rating levels such as the commonly used five-star rating.

In addition to asking customers to give an overall rating, a review system can also invite customers to evaluate specific product attributes $( \mathrm { e . g . , }$ L.L.Bean and $\mathrm { M a c y ' s ) }$ and display both the overall rating and the attribute-specific ratings on the product pages.<sup>1</sup> Because attribute-specific reviews enable second-period consumers to learn more about the product, they can refine their beliefs on product fit. By choosing whether to offer such granular reports, the firm can influence second-period consumers’ perception of the product fit. To model this second design feature, we use $k = 0 ,$ 1 to represent the firm’s binary decision of whether or not to offer product attribute ratings and $g = 2 , 3 , \dots , G$ to represent the granularity of review reports. Prior studies in online product reviews found that information of product attributes contained in product reviews helps reduce consumers’ uncertainty of product fit (Archak et al. 2011, Hong and Pavlou 2014). So here we assume that granular review reports allow second-period consumers to learn more about the product such that they form more refined beliefs on product misfit. Specifically, depending on their misfit, second-period consumers update their beliefs on product misfit as distributed over g different segments: $[ 0 , 1 / g ]$ $( 1 / g , 2 / g ] , \ldots , ( ( g - 1 ) / g , 1 ]$ , respectively. Granularity $g$ is the number of partitions, and a more granular review report (with a higher $g )$ corresponds to a finer partition of second-period consumers’ updated beliefs on product misfit.

Table 1 Notations

In the next two subsections, we will discuss the first-period consumers’ rating process and the secondperiod consumers’ rating interpretation process. Specifically, we will show how the firm’s design choices of the product review system affect consumers’ belief updating on product valuation and product fit.

## Consumer Rating Process

We use $p _ { i }$ to represent the product price, $\hat { v } _ { i }$ to represent consumers’ expected product valuation, and $\hat { x } _ { i }$ to represent their expected misfit in period i, where $i = 1 , 2 .$ . In the first period, consumers’ expected misfit is $\hat { x } _ { 1 } = ( 4 - \theta ) / 6 _ { r }$ , and their expected product valuation is $\hat { v } _ { 1 } = ( \bar { v } + \underline { { v } } ) / 2$ . Thus, first-period consumers’ prepurchase expected utility is given by $\hat { u } _ { 1 } = \hat { v } _ { 1 } - t \hat { x } _ { 1 } - p _ { 1 }$ After consumption, customers learn the true product valuation and how well the product fits their tastes. The realized utility for a customer with misfit x is $\boldsymbol { u } ( \boldsymbol { x } ) = \boldsymbol { v } - t \boldsymbol { x } - p _ { 1 }$ . Table 1 summarizes the notation of this paper.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $v$ </td><td>True valuation of the product</td></tr><tr><td> $\underline{v}$  and  $\bar{v}$ </td><td>Lower bound and upper bound of consumers&#x27; prepurchase perceived product valuation; consumers share a common prepurchase belief that the product valuation  $v$  is uniformly distributed between  $\underline{v}$  and  $\bar{v}$ </td></tr><tr><td> $\hat{v}_{i}$ </td><td>Consumers&#x27; prepurchase expected product valuation in period  $i$ </td></tr><tr><td> $t$ </td><td>Consumers&#x27; unit misfit cost</td></tr><tr><td> $x$ </td><td>Product misfit of a particular consumer, i.e., the relative distance between her taste preference and the product;  $0 \leq x \leq 1$ </td></tr><tr><td> $f(x)$ </td><td>Probability density function of consumer misfit distribution</td></tr><tr><td> $F(x)$ </td><td>Cumulative distribution function of consumer misfit distribution</td></tr><tr><td> $\theta$ </td><td>Product mainstream level  $0 \leq \theta \leq 2$ , where  $1 < \theta \leq 2$  correspond to mainstream products,  $0 \leq \theta < 1$  correspond to niche (narrow-appeal) products, and  $\theta = 1$  corresponds to neutral products</td></tr><tr><td> $\hat{x}_{i}$ </td><td>Consumers&#x27; prepurchase expected product misfit in period  $i$ </td></tr><tr><td> $\hat{u}_{i}$ </td><td>Consumers&#x27; prepurchase expected utility in period  $i$ </td></tr><tr><td> $u(x)$ </td><td>First-period customer  $x$ &#x27;s postpurchase utility</td></tr><tr><td> $w(x)$ </td><td>Utility score of a customer based on her postpurchase utility  $u(x)$ </td></tr><tr><td> $B(\cdot)$ </td><td>Customers&#x27; utility of reviewing the product</td></tr><tr><td> $R(\cdot)$ </td><td>Rating function</td></tr><tr><td> $\varepsilon$ </td><td>Customers&#x27; propensity to review the product</td></tr><tr><td> $p_{i}$ </td><td>Price of the product in period  $i$ </td></tr><tr><td> $\bar{p}_{1}$ </td><td>Maximum first-period price and  $\bar{p}_{1} = (\bar{v} + \underline{v})/2 - t(4 - \theta)/6$ </td></tr><tr><td> $s$  and  $\bar{s}$ </td><td>Cardinality of rating scales with  $2 \leq s \leq \bar{s}$ ,  $s \in Z$ , and  $\bar{s}$  being the maximum rating scale cardinality</td></tr><tr><td> $k$ </td><td>Firm&#x27;s binary decision of whether to offer granular review reports;  $k = 0, 1$ </td></tr><tr><td> $g$ </td><td>Granularity of review reports;  $g = 2, 3, \ldots, G$ </td></tr><tr><td> $\mu(\cdot)$ </td><td>Mean rating</td></tr><tr><td> $n(\cdot)$ </td><td>Review volume</td></tr><tr><td> $m(\cdot)$ </td><td>Sum of weighted rating levels, which is the numerator of mean rating  $\mu(\cdot)$ </td></tr><tr><td> $\alpha$ </td><td>Review reliance parameter</td></tr><tr><td> $\beta$ </td><td>Distribution adjustment parameter in second-period consumers&#x27; belief updating on product valuation</td></tr><tr><td> $\pi_{i}$ </td><td>Firm&#x27;s profit in period  $i$ </td></tr><tr><td> $\pi$ </td><td>Firm&#x27;s total profit of two periods</td></tr></table>

When the firm offers the review system, first-period customers rate the product based on their postpurchase net utilities. Customers give neutral/positive/ negative ratings for the product if their postpurchase utilities are zero/positive/negative, respectively. Netutility-based rating behavior has been empirically tested (Li and Hitt 2010), and net utilities have been adopted in modeling consumer rating behavior (Kuksov and Xie 2010, Hao et al. 2011). To simplify the exposition, we normalize product ratings to a unit line segment where the highest rating is 1, the lowest rating is $0 ,$ and other rating levels are evenly spaced out along the unit line segment. Thus, in a system with rating scale cardinality s, the available rating levels correspond to points $0 , \dot { 1 } / ( s - 1 ) , \dots , ( s - 2 ) / ( s - 1 )$ , and 1 on the unit line. We next transform customers’ net utility from $u ( x ) \in \mathbb { R }$ to a utility score $w ( x ) \in ( 0 , 1 )$ according to a logistic function $^ 2 \ \mathrm { i . e . , } \ w ( x ) = e ^ { u ( x ) } / ( e ^ { u ( x ) } + 1 ) =$ $1 / ( 1 + e ^ { t x + \breve { p } _ { 1 } - v } )$ , so that customers’ utility scores have the same scale as product ratings.

Customers consider the trade-off between review benefits and costs to decide whether to review the product. Customers generally derive benefits from reviewing the product, which may originate from multiple sources. Dichter (1966) and subsequent researchers (Engel et al. 1993, Sundaram et al. 1998) identified four main motives for consumers to engage in traditional word-of-mouth communication: product involvement, self-involvement, other involvement, and message involvement. Hennig-Thurau et al. (2004) built on Dichter’s (1966) framework and categorized the benefits of engaging in electronic word-of-mouth communication into five utilities: focus-related utility, consumption utility, approval utility, moderatorrelated utility, and homeostase utility. They further found that desire for social interaction, desire for economic incentives, concern for other consumers, and the potential to enhance self-worth are the primary factors that motivate consumers to articulate themselves online. We use a to denote customers’ benefit from reviewing the product.<sup>3</sup>

Customers also incur costs associated with reviewing the product. For a given customer with utility score w4x5, she will choose an available rating level $r / ( s - 1 )$ that most closely matches her utility score w4x5 on the unit line. In doing so, the customer incurs a computational cost of comparing all available rating levels and selecting the most appropriate rating level that reflects her evaluation of the product. Research on consumer choice behavior has shown that the difficulty of choice and the required cognitive effort increase in the number of alternatives considered (Shugan 1980, Bettman et al. 1998). Hence, we assume that this computational cost, denoted by c4s5, is nondecreasing in rating scale cardinality s.

However, even this best-matching rating level $r / ( s - 1 )$ may not accurately reflect the consumer’s true evaluation of the product. Following the literature in horizontal product differentiation (Anderson et al. 1992), we assume that a consumer incurs a disutility from a mismatch between her utility score $w ( x )$ and the closest available rating level $r / ( s - 1 )$ , and this disutility increases in the distance between w4x5 and $r / ( s - 1 )$ . We refer to this disutility as mismatch cost, denoted by $b | r / ( s - 1 ) - w ( x ) |$ , where b is a mismatch scale parameter.

Summarizing the above components, we have customers’ utility function from reviewing the product $B ( x ) = a \stackrel { . } { - } b | r / ( s - 1 ) - w ( x ) | - c ( s ) \stackrel { . } { }$ , where $r =$ arg $\begin{array} { r } { \operatorname* { m i n } _ { i = 0 , \dots , s - 1 } \{ | i / ( s - 1 ) - w ( x ) | \} } \end{array}$ . We define

$$
c (s) = \left\{ \begin{array}{l l} c _ {1}, & s \leq \bar {s}, \\ c _ {2}, & s > \bar {s}, \end{array} \right.
$$

where $c _ { 1 }$ and $c _ { 2 }$ are constants with $c _ { 1 } < a < c _ { 2 }$ . Thus, when $s > \bar { s } , \ a < c ( s ) = c _ { 2 } .$ , it becomes overwhelming for customers to rate, and $B ( x ) < 0$ for all customers. Hence, we only observe limited options of rating scales in practice.<sup>4</sup> The existence of such an upper bound s¯ captures consumers’ limited cognitive capacity to evaluate alternatives (Miller 1956, Baddeley 1992). When $s \leq { \bar { s } } ,$ we use parameter $\varepsilon =$ $( a - c _ { 1 } ) / \dot { b } > 0$ to measure customers’ propensity to review the product. Customers with a utility score satisfying $| { \bar { r / ( s - 1 ) } } - w ( x ) | \leq \varepsilon$ have a nonnegative rating utility and will rate the product as $r / ( \bar { s } - 1 )$ Consequently, the following rating function captures customers’ rating behavior:

$$
R (x) = \left\{ \begin{array}{l l} \frac {r}{s - 1}, & \text { if } \left| \frac {r}{s - 1} - w (x) \right| \leq \varepsilon , \\ \text { does   not   rate }, & \text { otherwise }. \end{array} \right.\tag{1}
$$

This rating function creates a mapping between each customer’s misfit and the rating level she chooses.<sup>5</sup>

A customer will choose to rate the product if and only if her utility from reviewing the product is nonnegative. As a result, not all customers rate the product, since rating costs outweigh rating benefits for some customers. Additionally, customers with extremely high or extremely low net utility are more likely to rate.<sup>6</sup> This property is consistent with empirical findings (Dellarocas and Narayan 2006, Hu et al. 2009, Gao et al. 2015). Hu et al. (2009) refer to customers’ tendency to rate the product when they are extremely satisfied (rate to brag) or unsatisfied (rate to moan) as the brag-and-moan effect, which results in the underreporting bias of customers with moderate views.

The overall rating results are captured by mean rating $\mu ( p _ { 1 } , s )$ and rating volume $n { \bar { ( } } p _ { 1 } , s { ) }$ , which are characterized in the online appendix (available as supplemental material at http://dx.doi.org/10.1287/ isre.2015.0594).<sup>7</sup>

## Rating Interpretation Process

After observing review outcomes, second-period consumers will update their beliefs on product valuation and product fit. We first discuss second-period consumers’ belief updating on product valuation. Specifically, second-period consumers’ updated belief on product valuation is based on both their nonreviewbased belief $\hat { v } _ { \mathrm { N R } }$ and review-based belief $\hat { v } _ { \mathrm { R } }$ . Without considering review results, second-period consumers’ belief on product valuation is the same as their prior belief and, thus, the nonreview-based belief $\hat { v } _ { \mathrm { N R } } =$ $( { \bar { v } } + \underline { { v } } ) / 2$

As for the review-based belief $\hat { v } _ { \mathrm { R } } ,$ it depends on review outcomes and is defined as $\hat { v } _ { \mathrm { { R } } } = \underline { { v } } + \bar { [ \mu ( p _ { 1 } , s ) + }$ $\beta ( 1 - \theta ) ] ( \bar { v } - \underline { { v } } )$ . Because first-period customers rate the product based on their postpurchase net utility, second-period consumers know that mean rating $\mu ( p _ { 1 } , s )$ signals the mean net utility of first-period customers. Holding everything else constant, a higher mean rating corresponds to a higher mean net utility, indicating a higher product valuation. This is captured by $\underline { { v } } + \mu ( p _ { 1 } , s ) ( \bar { v } - \underline { { v } } )$ in the $\hat { v } _ { \scriptscriptstyle \mathrm { R } }$ function.

Additionally, given the same product valuation and the same first-period price, for mainstream products, first-period customers’ overall product misfit is lower, and thus the mean rating is higher, whereas for niche products, first-period customers’ overall product misfit is higher, and thus the mean rating is lower. Knowing that product mainstream level affects the mean rating, second-period consumers will factor this into their belief updating on product valuation. Because of limited rationality, second-period consumers are incapable of perfectly computing the impact of product mainstream level on mean rating and therefore cannot derive the true value of v. However, they can include an imperfect adjustment term $\beta ( 1 - \theta ) ( \bar { v } - \underline { { v } } )$ in the $\hat { v } _ { \mathrm { R } }$ function, where $\beta \geq 0$ is a distribution adjustment parameter, to account for the impact of product mainstream level. With this imperfect distribution adjustment, second-period consumers would adjust the mean rating downward when updating their beliefs on product valuation for mainstream products, adjust the mean rating upward for niche products, and make no adjustment for neutral products. There exists a perfect ${ \hat { \beta } } ,$ at which consumers’ review-based beliefs on product valuation $\hat { v } _ { \mathrm { R } }$ are the same as the true product valuation v. Since consumers’ belief adjustment is imperfect, we assume that $0 \leq \beta \leq \hat { \beta } ,$ which implies that $0 \leq \mu ( p _ { 1 } , s ) + \beta ( 1 - \theta ) \leq 1$ for all . The specific feasible range of $\beta$ is discussed in the online appendix.

Accordingly, second-period consumers update their beliefs on product valuation as follows:

$$
\hat {v} _ {2} = \alpha n (p _ {1}, s) \hat {v} _ {\mathrm{R}} + [ 1 - \alpha n (p _ {1}, s) ] \hat {v} _ {\mathrm{NR}},\tag{2}
$$

where $\alpha \in [ 0 , 1 ]$ is a review reliance parameter that converts review volume $n ( p _ { 1 } , s )$ into the weight associated with review-based belief. This belief updating process is consistent with prior studies in combining forecasts (Bates and Granger 1969, Clemen 1989), and similar modeling approaches of consumers’ belief updating mechanism have been adopted in recent studies of product reviews (Kwark et al. 2014). For a given $\alpha ,$ more weight is given to the review results if there are more reviews.<sup>8</sup>

In addition to updating their beliefs on product valuation, second-period consumers may also update their beliefs on product fit based on granular review reports. When the firm offers granular review reports, attribute-specific ratings in these reports reveal more information about the product. As a result, secondperiod consumers can get a better idea about product fit. Since consumers have different preferences for product attributes, attribute-specific ratings may convince some consumers that the product is a better fit for their tastes and others that the product is a worse fit. For example, when the granularity level of review reports is $g = 2$ , consumers who like the revealed attribute ratings will consider the product a better fit, and their updated belief is that product misfit x is distributed on a more refined range of $[ 0 , \textstyle { \frac { 1 } { 2 } } ]$ compared to their prior belief of 601 17. Consumers who dislike the revealed attribute ratings will consider the product a worse fit, and their updated belief is that product misfit x is distributed on a more refined range of 4 <sup>1</sup> 1 17.

For the general case of granularity level $g = 2 , 3 ,$ $\cdots , G ,$ second-period consumers form different and more refined beliefs that product misfits for these g segments are distributed over $[ 0 , 1 / g ] , ( 1 / g , 2 / g ] , \ldots ,$ $( ( g - 1 ) / g , 1 ]$ , respectively. The corresponding expected product misfits for these g segments are

$$
\begin{array}{c} \frac {1}{F (1 / g)} \int_ {0} ^ {1 / g} x f (x) d x, \\ \frac {1}{F (2 / g) - F (1 / g)} \int_ {1 / g} ^ {1 / g} x f (x) d x, \ldots , \\ \frac {1}{1 - F ((g - 1) / g)} \int_ {(g - 1)} ^ {1} x f (x) d x, \end{array}
$$

respectively.

In the next two sections, we study the firm’s review system design problem in a baseline model, in which consumers only learn from overall ratings, and an extended model, in which consumers also learn from product attribute reviews.<sup>9</sup>

## Analysis of Baseline Model— A Review System Without Granular Review Reports

In this section, we analyze a review system that only solicits and displays consumers’ overall product ratings, assuming the firm does not offer granular review reports $( k = 0 )$ . The firm’s design decisions include whether to offer the review system and the optimal rating scale cardinality $s ,$ if it decides to offer the review system at all.

## First-Period Consumers’ Purchase Decision

In the first period, anticipating consumers’ prepurchase expected utility function $\hat { u } _ { 1 } = \hat { v } _ { 1 } - t \hat { x } _ { 1 } - p _ { 1 } ,$ the firm sets its price $p _ { 1 } \leq \bar { p } _ { 1 } = \hat { v } _ { 1 } - t \hat { x } _ { 1 }$ to achieve positive sales, where the maximum price $\bar { p } _ { 1 }$ is determined by consumers’ prepurchase expected gross utility. We assume that consumers’ prepurchase expected gross utility is nonnegative, i.e., the expected valuation is higher than the expected misfit cost. This assumption ensures that it is feasible for the firm to set a positive price and achieve positive sales.

Forward-looking first-period consumers choose either to purchase in the first period or wait until the second period. If they decide to wait, then there is no sale in the first period, and therefore no product reviews are available. In the second period, the waiting first-period consumers and newly arrived secondperiod consumers share the same expectations about the product, since these two consumer groups are identical.<sup>10</sup> As a result, the firm will charge a secondperiod price such that all consumers’ expected net utility is zero. If first-period consumers decide to purchase in the first period, their expected net utility is nonnegative, since the first-period price satisfies $p _ { 1 } \leq \bar { p } _ { 1 }$ . Therefore, rational first-period consumers will purchase in the first period, rather than wait, because their net utility of purchasing in the first period is no worse than waiting.

## Properties of Review Outcomes and Consumers Belief Updating

After purchase, first-period customers learn their realized utility, given by $u ( x ) = v - t x - p _ { 1 }$ . Depending on their utility from reviewing the product $B ( x )$ , customers with $\dot { B } ( x ) \ge 0$ will rate the product according to the rating function $R ( x )$ defined in Equation (1). Lemma 1 summarizes the properties of two main review outcomes—rating volume $n ( p _ { 1 } , s )$ and mean rating $\mu ( p _ { 1 } , s )$ . The proofs of all lemmas and propositions are relegated to the online appendix.

Lemma 1 (Properties of Mean Rating and Review Volume)<sub>.</sub>

(a) Mean rating, $\mu ( p _ { 1 } , s ) ,$ , decreases in the first-period price $p _ { 1 }$ and increases in the product valuation v for all products.

(b) For mainstream products, $n ( p _ { 1 } , s )$ decreases in $p _ { 1 }$ and increases in v; for niche products, review volume, $n ( p _ { 1 } , s )$ , increases in the first-period price $p _ { 1 }$ and decreases in the product valuation v; and for neutral products, $n ( p _ { 1 } , s )$ is independent of $p _ { 1 }$ and v.

(c) Review volume, $n ( p _ { 1 } , s )$ , increases in rating scale cardinality s for all products.

(d) Mean rating, $\mu ( p _ { 1 } , s )$ , increases in rating scale cardinality s if the product valuation is lower than a threshold, $i . e . , v \le V _ { s } ,$ and decreases in s otherwise for all products. The value of $V _ { s }$ is defined in the online appendix.

Lemma 1 shows that first-period price $p _ { 1 }$ and product valuation v have opposite effects on mean rating $\mu ( p _ { 1 } , s )$ and review volume $n ( p _ { 1 } , s )$ . This is because their respective effects on customers’ net utility are opposite to each other. Here, we focus on explaining the effects of product valuation as the reverse holds for first-period price. We know that first-period customers rate the product based on their net utility and mean rating reflects their mean net utility. Since all customers’ net utility increases in product valuation $v ,$ their mean net utility and hence mean rating $\mu ( p _ { 1 } , s )$ increase in product valuation v.

The impact of product valuation on review volume $n ( p _ { 1 } , s )$ , on the other hand, varies across different product types. Recall that customers choose whether to rate the product and at what rating level, according to $B ( x )$ , their utility from reviewing the product. Holding everything else constant, an increase in product valuation leads to a higher net utility for all customers, which may change individual customers’ decision to rate the product. Specifically, an increase in product valuation has both a volume-increasing effect and a volume-decreasing effect, because with a higher net utility, more customers will choose positive ratings and fewer customers will choose negative ratings. For mainstream products, more consumers have a low product misfit and rate the product positively. Consequently, the volume-increasing effect dominates the volume-decreasing effect, so the total review volume increases in product valuation for mainstream products. By contrast, for niche products, more consumers have a high product misfit and rate the product negatively. Consequently, the volume-decreasing effect dominates the volume-increasing effect, so the total review volume decreases in product valuation for niche products. For neutral products, consumer misfit is uniformly distributed, and thus the volumeincreasing effect and the volume-decreasing effect of increasing product valuation cancel each other out. Therefore, product valuation has no impact on the total review volume for neutral products.

The impact of rating scale cardinality s on review volume $n ( p _ { 1 } , s )$ and mean rating $\mu ( p _ { 1 } , s )$ can also be explained by examining customers’ utility from reviewing the product B4x5. When rating scale cardinality increases, more rating levels are available for customers to choose from. Some customers who previously chose not to rate because of a negative $\hat { B } ( x )$ may now rate the product, because they can now find a rating level that better reflects their own evaluation of the product. Consequently, when rating scale cardinality increases, more customers will have a nonnegative utility from reviewing the product, leading to a higher review volume.

The impact of rating scale cardinality s on mean rating $\mu ( p _ { 1 } , s )$ is more complex, and its direction is contingent on product valuation v. We know that mean rating reflects the weighted average of rating levels selected by customers. Each rating level is weighted by its corresponding review volume and the total weight is the total review volume. In other words, mean rating $\mu ( p _ { 1 } , s )$ is the ratio of $m ( p _ { 1 } , s )$ , the sum of weighted rating levels, and $n ( p _ { 1 } , s )$ , the review volume. As discussed above, when rating scale cardinality increases, some customers will choose newly available rating levels, which can be positive, neutral, or negative. As a result, mean rating can increase or decrease. When rating scale cardinality increases from s to $s + 1 ,$ its impact on mean rating is determined by the relative strength of two terms—the product of review volume and change in the sum of weighted rating levels versus the product of the sum of weighted rating levels and change in review volume, i.e., $n ( p _ { 1 } , s ) [ \bar { m } ( p _ { 1 } , s + 1 ) - m ( \bar { p _ { 1 } } , s ) ]$ versus $m ( p _ { 1 } , s ) [ n ( p _ { 1 } , s + 1 ) - n ( p _ { 1 } , s ) ]$ . The first term decreases in $v ,$ whereas the second term increases in v. Thus, when product valuation v is lower than a threshold,<sup>11</sup> the first term dominates, leading to a higher mean rating.

Second-period consumers can learn from review outcomes, $\mathrm { i . e . , } \ n ( p _ { 1 } , s )$ and $\mu ( p _ { 1 } , s )$ , and the properties of their updated belief on product valuation are described in Lemma 2.

Lemma 2 (Properties of the Second-Period Consumers’ Expectation on Product Valuation)<sub>.</sub>

Second-period consumers’ expectation on product valuation $( \hat { v } _ { 2 } )$

(a) increases in product valuation (v) and decreases in first-period price $( p _ { 1 } ) ;$

(b) increases in the rating scale cardinality (s) for mainstream products, decreases in s for niche products, and is independent of s for neutral products;

(c) increases in the product mainstream level () and decreases in the unit misfit cost (t);

(d) increases in the review reliance (5 when the product valuation is higher than a threshold, i.e., $v \geq V _ { \alpha } ,$ and decreases in  otherwise; and

(e) decreases in the misfit distribution adjustment parameter () for mainstream products and increases in $\beta$ for niche products.

The value of $V _ { \alpha }$ is defined in the online appendix.

Because product valuation v and first-period price $p _ { 1 }$ have opposite effects on customers’ net utility, a higher product valuation or a lower first-period price will lead to a higher postpurchase net utility, resulting in a higher mean rating (as shown in Lemma 1). Holding everything else constant, second-period consumers view a higher mean rating as a signal for a higher product valuation. They then update their beliefs on product valuation upward, which leads to the result of Lemma 2(a).

The impact of rating scale cardinality s on second-period consumers’ expectation of product valuation $\hat { v } _ { 2 }$ takes effect through affecting both mean rating and review volume. For niche products, since more consumers have a high product misfit, the volumes for low rating levels are greater than those for high rating levels. By contrast, for mainstream products, since more consumers have a low product mis-$\mathrm { f i t } ,$ the volumes for high rating levels are greater than those for low rating levels. This property in volume-weighted ratings is captured in the last term of $m ( p _ { 1 } , s )$ , the sum of weighted rating levels. The net impact of rating scale cardinality s on $\hat { v } _ { 2 }$ is eventually determined by this term. Specifically, for niche products, the volume-weighted low ratings dominate, and thus this term is negative, and $\hat { v } _ { 2 }$ decreases in s. For mainstream products, the volume-weighted high ratings dominate, and thus this term is positive and $\hat { v } _ { 2 }$ increases in s. Therefore, the overall effect of s on $\hat { v } _ { 2 }$ depends on product mainstream level .

Because review reliance  represents how much second-period consumers rely on product reviews when updating their belief on product valuation, a higher  indicates a higher weight on the review-based belief compared to the nonreview-based belief. The review-based belief coincides with the nonreviewbased belief when $\textstyle \mu ( p _ { 1 } , s ) + \beta ( 1 - \theta ) - { \frac { 1 } { 2 } } = 0$ 1 which corresponds to a threshold on product valuation. When the true product valuation is higher than this threshold, the review-based belief $\boldsymbol { \hat { v } } _ { \mathrm { R } }$ is higher than the nonreview-based belief $\boldsymbol { \hat { v } } _ { \mathrm { N R } } ,$ , and thus increasing review reliance  leads to a higher updated belief $\hat { v } _ { 2 } .$

For a given product valuation and first-period price, consumers’ expectation of the product valuation is negatively related to the unit misfit cost. This relationship is due to the fact that consumer ratings reflect their net utility, which is affected by both the product valuation and misfit. When unit misfit cost decreases, first-period customers enjoy a higher postpurchase net utility and thus rate the product more positively. As a result, second-period consumers observe an increase in overall rating and therefore form a higher expectation for the product valuation. Since consumers incur a lower overall misfit cost for mainstream products, their perception of the product valuation is higher for mainstream products, holding everything else constant. Thus, consumers’ expectation of the product valuation is positively related to the product mainstream level. Partially rational consumers anticipate this effect and hence discount the signal in their belief updating process through the distribution adjustment parameter $\beta .$ . For mainstream products, the adjustment term shifts consumers’ belief downward to reflect the impact of low misfit on customer ratings. For niche products, the adjustment term shifts consumers’ belief upward to reflect the impact of high misfit on customer ratings. Hence, second-period consumers’ beliefs on product valuation decrease in $\beta$ for mainstream products and increase in $\beta$ for niche products.

## Optimal Product Pricing

As second-period consumers learn from review outcomes and update their beliefs on product valuation and product misfit, their prepurchase expected utility is $\hat { u } _ { 2 } ^ { \top } = \hat { v } _ { 2 } - t \hat { x } _ { 2 } - p _ { 2 }$ . The firm then sets $\dot { p } _ { 2 } = \hat { v } _ { 2 } - t \hat { x } _ { 2 }$ such that consumers’ expected net utility is zero. Since all first-period consumers purchase in the first period, the first-period profit is $\pi _ { 1 } = p _ { 1 } ;$ because all secondperiod consumers purchase in the second period, the second-period profit is $\pi _ { 2 } = p _ { 2 } = \hat { v } _ { 2 } - t \hat { x } _ { 2 }$ . In a review system without granular review reports, the firm’s decision problem can be specified as

$$
\begin{array}{l l} \max _ {p _ {1}, s} & \pi (p _ {1}, s) = \pi_ {1} + \pi_ {2} = p _ {1} + \hat {v} _ {2} - t \hat {x} _ {2} \\ \text {s.t.} & 0 \leq p _ {1} \leq \bar {p} _ {1}, \\ & 2 \leq s \leq \bar {s},   s \in Z. \end{array}\tag{3}
$$

The firm sets its first-period price and selects the rating scale cardinality for the review system to maximize its total profit over the two periods. The firm’s first-period price has two countervailing effects on its overall profit. Increasing the first-period price directly increases the firm’s first-period profit, but indirectly decreases its second-period profit through its impact on customer reviews. Specifically, second-period consumers’ updated belief on product valuation is at its maximum when the firm offers the product for free $( p _ { 1 } = 0 )$ , and it is at its minimum when the firm sets the price to the maximum possible price $( p _ { 1 } = \bar { p } _ { 1 } )$ such that all first-period consumers have a prepurchase expected utility of zero and still purchase. The firm aims to balance these two countervailing effects to maximize its total profit. The resulting optimal pricing strategy depends on product and consumer characteristics, such as product valuation, product mainstream level, consumer unit misfit cost, review reliance, and distribution adjustment. Proposition 1 summarizes the optimal pricing strategy when the firm chooses to provide a review system.

Proposition 1 (Optimal Pricing in the First Period in the Presence of a Review System)<sub>.</sub>

(a) For a mainstream product ( > 15, if the product valuation is high with

$$
v > \bar {p} _ {1} + \frac {t \alpha \theta (\bar {v} - \underline {{v}}) - t ^ {2}}{2 \alpha (\theta - 1) (\bar {v} - \underline {{v}})} - 2 \beta (C _ {1} + C _ {2}) (\theta - 1),
$$

it is optimal for the firm to charge $p _ { 1 } ^ { * } = \bar { p } _ { 1 }$ in the first period; if the product valuation is medium with

$$
\begin{array}{l} \frac {t \alpha \theta (\bar {v} - \underline {{v}}) - t ^ {2}}{2 \alpha (\theta - 1) (\bar {v} - \underline {{v}})} - 2 \beta (C _ {1} + C _ {2}) (\theta - 1) \\ \qquad \leq v \leq \bar {p} _ {1} + \frac {t \alpha \theta (\bar {v} - \underline {{v}}) - t ^ {2}}{2 \alpha (\theta - 1) (\bar {v} - \underline {{v}})} - 2 \beta (C _ {1} + C _ {2}) (\theta - 1), \end{array}
$$

it is optimal to charge

$$
p _ {1} ^ {*} = v + 2 \beta (C _ {1} + C _ {2}) (\theta - 1) - \frac {t \alpha \theta (\bar {v} - \underline {{v}}) - t ^ {2}}{(2 \alpha (\theta - 1) (\bar {v} - \underline {{v}})};
$$

if the product valuation is low with

$$
v <   \frac {t \alpha \theta (\bar {v} - \underline {{v}}) - t ^ {2}}{2 \alpha (\theta - 1) (\bar {v} - \underline {{v}})} - 2 \beta (C _ {1} + C _ {2}) (\theta - 1),
$$

it is optimal to offer it for free in the first period.

(b) For a niche product ( < 15, if the product valuation is high with

$$
v > \frac {\bar {p} _ {1}}{2} + \frac {t ^ {2} - t \alpha \theta (\bar {v} - \underline {{v}})}{2 \alpha (1 - \theta) (\bar {v} - \underline {{v}})} + 2 \beta (C _ {1} + C _ {2}) (1 - \theta),
$$

it is optimal for the firm to offer it for free in the first period; if the product valuation is low with

$$
v \leq \frac {\bar {p} _ {1}}{2} + \frac {t ^ {2} - t \alpha \theta (\bar {v} - \underline {{v}})}{2 \alpha (1 - \theta) (\bar {v} - \underline {{v}})} + 2 \beta (C _ {1} + C _ {2}) (1 - \theta),
$$

it is optimal to charge ${ p } _ { 1 } ^ { * } = \bar { p } _ { 1 }$

(c) For a neutral product $( \theta = 1 )$ , if the misfit cost is high relative to the product uncertainty $t > \alpha ( \bar { v } - \underline { { v } } )$ , it is optimal for the firm to charge $p _ { 1 } ^ { * } = \bar { p } _ { 1 } ,$ otherwise, it is optimal to offer the product for free in the first period.

The values of $\dot { C } _ { 1 }$ and $C _ { 2 }$ are defined in the online appendix.

The direct effect of the first-period price on the firm’s profit is straightforward $\bar { ( \partial \pi _ { 1 } / \partial p _ { 1 } = 1 ) }$ . The indirect effect of the first-period price on the firm’s profit is more nuanced. Overall, the second-period profit decreases in the first-period price for all products $( \partial \pi _ { 2 } / \partial p _ { 1 } < 0 )$ . However, product characteristics (mainstream level  and product valuation v) moderate the magnitude of this indirect effect $( | \partial \pi _ { 2 } / \partial p _ { 1 } | )$ Specifically, increasing product valuation amplifies the indirect effect for niche products $( \partial | \partial \pi _ { 2 } / \partial p _ { 1 } | / \partial v$ ${ > } 0$ when $\theta < 1 )$ , whereas it diminishes the indirect effect for mainstream products $\left( \partial | \partial \pi _ { 2 } / \partial p _ { 1 } | / \partial v < 0 \right.$ when $\theta > 1 )$ . For neutral products, product valuation has no impact on the indirect effect $( \partial | \partial \pi _ { 2 } / \partial p _ { 1 } | / \partial v$ $= 0$ when $\theta { = } 1 )$ , and the magnitude of the indirect effect is determined by unit misfit, valuation uncertainty, and consumers’ reliance on reviews $( | \partial \pi _ { 2 } / \partial p _ { 1 } | = \alpha ( \bar { v } - \underline { { v } } ) / t )$ . The firm balances the direct and indirect effects of the first-period price on the firm’s total profit and adopts three possible pricing strategies—lower-bound, upper-bound, and interior pricing strategies.

The lower-bound pricing strategy refers to offering the product for free either through charging zero price or through providing coupons, rebates, and other promotional benefits. It is optimal for the firm to adopt lower-bound pricing for high-value niche products, low-value mainstream products, and low-misfit neutral products since the negative indirect effect of first-period price on second-period profit dominates the positive direct effect of first-period price on first-period profit. The upper-bound pricing strategy refers to charging the maximum possible price $\bar { p } _ { 1 }$ at which all consumers still participate. It is optimal for the firm to adopt upper-bound pricing for low-value niche products, high-value mainstream products, and high-misfit neutral products since the positive direct effect dominates the negative indirect effect. The interior pricing strategy refers to charging a price between the lower and upper bounds. It is optimal for the firm to adopt interior pricing only for medium-value mainstream products, and at this interior price, the positive direct effect equals the negative indirect effect. Figures 3(a), 3(b), and 4 illustrate the firm’s different pricing strategies for niche, neutral, and mainstream products, respectively.

For niche and mainstream products, the firm’s optimal pricing decision depends on all parameter values. However, since for consumers only the product valuation is unobservable, here (and thereafter) we choose to present the firm’s decision as a response to different product valuation levels, whereas the corresponding threshold of product valuation depends on other parameters. For example, for a mainstream product, the threshold for upper-bound pricing increases in review reliance () and valuation uncertainty $( \bar { v } - \underline { { v } } )$ but decreases in the distribution adjustment parameter ( ). For a niche product, the threshold for lowerbound pricing decreases in review reliance () and valuation uncertainty $( \bar { v } - \underline { { v } } )$ , but increases in the distribution adjustment parameter ( ).

Figure 3 Firm’s Optimal Strategy for Niche and Neutral Products in the Baseline Model  
![](/api/attachments/H4MT43JU/fulltext/images/70a02fea7ddc182d392887d481d347c3e0f9c2b3ed7ea07eacc1dc08bb979ca8.jpg)

(b) Neutral products  
![](/api/attachments/H4MT43JU/fulltext/images/9790f426e43da1a0eb3b91c754085a83aff0f906e049432bc54188e8d6b23772.jpg)  
Notes. Panels (a) $( \theta = 0 . 8 )$ and (b) ( 1) are based on parameter values $\varepsilon = 0 . 0 3 , \underline { { v } } = 5 , \bar { v } = 1 0 0 ,$ and $\alpha = 1$ . Other parameter values generate qualitatively the same results. We focus on the shaded area within the bold lines where all rating levels are rated. For niche products, $s ^ { * } = 2$ , and for neutral products, $S ^ { * } \in \{ 2 , 3 , \ldots , \bar { s } \}$ . The parameter space can be partitioned into three regions based on the firm’s pricing and review system offering decisions: region L, $p _ { 1 } ^ { * } = 0 ;$ region U, $p _ { 1 } ^ { * } = \bar { p } _ { 1 } ;$ ; region O, no review system is offered.

Figure 4 Firm’s Optimal Strategy for Mainstream Products in the Baseline Model  
![](/api/attachments/H4MT43JU/fulltext/images/b2367791dd20f86e42da31f125eb531ce41054033f1b564adabd9c45f3bd3255.jpg)  
Notes. Figure 4 is based on parameter values $\varepsilon = 0 . 0 3 , \vee = 5 , \bar { V } = 1 0 0 , \alpha = 1 , \beta = 0 ,$ , and $\theta = 2 .$ . Other parameter values generate qualitatively the same results. We focus on the shaded area within the bold lines where all rating levels are rated. For all mainstream products $\pmb { S } ^ { * } = \bar { \pmb { S } } = 1 0$ . The parameter space can be partitioned into four regions based on the firm’s pricing and review system offering decisions: region L, $p _ { 1 } ^ { * } = 0 ;$ region I, $0 < p _ { 1 } ^ { * } < \bar { p } _ { 1 }$ ; region U, $p _ { 1 } ^ { * } = \bar { p } _ { 1 } ^ { \ }$ region O, no review system is offered.

We find that the firm’s pricing strategies serve different objectives. Through upper-bound pricing, the firm pursues the maximum first-period profit. Here the firm takes advantage of the information asymmetry on product valuation by charging the maximum possible price in the first period. Through lower-bound pricing, the firm aims to maximize second-period profit by sacrificing its first-period profit. Specifically, the firm manipulates the firstperiod price to its lowest possible level to signal a higher product value to future consumers through the review system.

## Optimal Design of the Review System

Product reviews serve as an information source for consumers to learn about the product. The firm may influence this learning by deciding whether to offer the review system and, if it decides to offer the review system, selecting the optimal rating scale cardinality s. If the firm decides not to offer the review system, second-period consumers’ beliefs of the product valuation and the product fit are the same as those of first-period consumers. Therefore, the firm will charge the same price in both periods such that consumers’ expected utility is zero, i.e., $p _ { 1 } = p _ { 2 } = \bar { p } _ { 1 } = \hat { v } _ { 1 } - t \hat { x } _ { 1 } =$ $( \bar { v } + \underline { { v } } ) / 2 - ( t ( 4 - \theta ) ) / 6 ,$ , and the firm gets a total profit of $\pi = \pi _ { 1 } + \pi _ { 2 } = \bar { v } + \underline { { v } } - ( t ( 4 - \theta ) ) / 3$ . If the firm decides to offer the review system, then it will decide the optimal first-period price and rating scale cardinality s. The firm then compares the profit levels with and without the review system and makes its review system offering decision. Proposition 2 summarizes the firm’s optimal design choices of the review system.

Proposition 2 (Firm’s review system offering decision and optimal rating scale cardinality)<sub>.</sub>

(a) For a mainstream product $( \theta > 1 )$ , it is optimal for the firm to offer a review system with a rating scale cardinality $s ^ { * } = \bar { s } ,$ the maximum number of rating levels, $i f v > v _ { 2 } ;$ otherwise, it is optimal for the firm not to offer a review system.

(b) For a niche product $( \theta < 1 )$ , it is optimal for the firm to offer a review system with a rating scale cardinality $s ^ { * } = 2 ,$ , the minimum number of rating levels, if $v > v _ { 0 } ;$ otherwise, it is optimal for the firm not to offer a review system.

(c) For a neutral product $( \theta = 1 ) .$ , it is optimal for the firm to offer a review system and rating scale cardinality s has no impact on the firm’s profit, $i f v > v _ { 1 } ;$ otherwise, it is optimal for the firm not to offer a review system.

The values of $v _ { 0 } , \ v _ { 1 } ,$ and $v _ { 2 }$ are defined in the online appendix.

Figures 3 and 4 visualize the market conditions for the firm’s overall optimal strategy in the baseline model (Propositions 1 and 2) based on two contextual characteristics—unit misfit cost t and product valuation v. We find that it is optimal for the firm not to host a review system (region O in Figures 3 and 4) when the product valuation is lower than a threshold, which depends on product and consumer characteristics. In addition, if the firm decides to offer the review system, its optimal design for rating scale cardinality is contingent on the product mainstream level. For mainstream products, higher rating scale cardinality has a positive effect on second-period consumers’ perception of product valuation (as shown in Lemma 2), which leads to a higher second-period profit and thus a higher overall profit for a given firstperiod price. Therefore, it is optimal for the firm to offer the maximum number of rating levels. By contrast, for niche products, higher rating scale cardinality has a negative effect on second-period consumers’ perception of product valuation. Therefore, it is optimal for the firm to offer the minimum number of rating levels. For neutral products, the firm’s profit is independent of the rating scale cardinality, and therefore the optimal rating scale cardinality could be any integer between 2 and s¯.

## Analysis of Extended Model— A Review System with Granular Review Reports

In this section, we analyze a review system that provides both overall ratings and granular review reports. As consumers learn more about the product through granular review reports, they update their beliefs on product fit accordingly. The firm’s design decisions include whether to offer the review system and, if it decides to offer the review system, the optimal rating scale cardinality and whether to offer granular review reports.

## Formulation

Second-period consumers’ belief updating on product valuation in the extended model is the same as that defined in Equation (2) of the baseline model. If the firm decides to offer granular reports, i.e., k = 1, then second-period consumers form different updated beliefs as product misfit is distributed over $[ { \bar { 0 } } , 1 / g ] ,$ $( 1 / g , 2 / g ] , \bar { , } \ldots , ( ( g - 1 ) / g , 1 ] .$ , respectively. Here, we focus on analyzing the case of $g = 2$ . We describe the solution procedure for granular report offering decision k for the general case of $g = 2 , 3 , \dots , G$ in the online appendix.<sup>12</sup>

When the firm offers granular reports, secondperiod consumers will update their beliefs as product misfit x is distributed on either 601 <sup>1</sup> 7 or $\textstyle { \left( { \frac { 1 } { 2 } } , 1 \right] }$ Since consumers in the latter segment have a higher expected misfit cost, to serve all consumers, the firm has to lower its second-period price compared to the case without granular reports $( k = 0 )$ . Thus, the option of offering granular reports and serving all consumers is dominated by the option of not offering granular reports. Therefore, when the firm offers granular reports, it will only serve the favorable consumer segment 601 <sup>1</sup> 7 with an expected misfit of $\hat { x } _ { 2 } ( k = 1 ) =$ $\begin{array} { r } { ( 1 / F ( 1 / 2 ) ) \int _ { 0 } ^ { 1 / 2 } x f ( x ) d x . } \end{array}$ , and sets the second-period price to $p _ { 2 } ( \ddot { k } = 1 ) = \hat { v } _ { 2 } - t \hat { x } _ { 2 } ( k = 1 )$ . The firm simultaneously decides the product price and the two design choices (k and s) to maximize its total profit, which is formulated as follows:

$$
\max _ {p _ {1}, k, s} \pi (p _ {1}, k, s) = \max _ {p _ {1}, s} \bigl \{\pi (p _ {1}, k = 1, s), \pi (p _ {1}, k = 0, s) \bigr \}
$$

$$
\mathrm{s.t.} 0 \leq p _ {1} \leq \bar {p} _ {1},
$$

$$
k = 0, 1,
$$

$$
2 \leq s \leq \bar {s}, s \in Z,\tag{4}
$$

where

$$
\pi (p _ {1}, k = 1, s) = p _ {1} + F (1 / 2) [ \hat {v} _ {2} (p _ {1}, s) - t \hat {x} _ {2} (k = 1) ]
$$

and

$$
\pi (p _ {1}, k = 0, s) = p _ {1} + \hat {v} _ {2} (p _ {1}, s) - t \hat {x} _ {2} (k = 0).
$$

We next explore the properties of the two design choices in Lemma 3.

Lemma 3 (Properties of Rating Scale Cardinality and Granular Report Offering Decisions)<sub>.</sub>

(a) Given the firm’s choice of first-period price $p _ { 1 }$ and granular report offering decision k, the optimal rating scale cardinality is $s ^ { * } = \bar { s }$ for mainstream products $( \theta > 1 )$ and $s ^ { * } = 2$ for niche products $( \theta < 1 ) ;$ s has no impact on the firm’s profit for neutral products $( \theta = 1 )$

(b) Given the firm’s choices of first-period price $p _ { 1 }$ and rating scale cardinality s, if the product valuation is relatively low $( v < D _ { 0 } + p _ { 1 }$ for niche products, $v < D _ { 1 } + p _ { 1 }$ for neutral products, and $v < D _ { 2 } + p _ { 1 }$ for mainstream products), it is optimal for the firm to offer granular reports $( k ^ { * } = 1 )$ and only serve consumers in $[ 0 , { 1 } / { 2 } ]$ in the second period; otherwise, it is optimal for the firm not to offer granular reports $( k ^ { * } = 0 )$ and serve all consumers in the second period.

The values of $D _ { 0 } , D _ { 1 } ,$ and $D _ { 2 }$ are defined in the online appendix.

As shown in Lemma 3, given any first-period price and granular report offering decisions, the firm selects the optimal rating scale cardinality based on product mainstream level. Given any first-period price and rating scale cardinality, the firm offers product attribute reviews when the product valuation is less than a threshold, which is dependent on product and consumer characteristics and price. Since its review system design decisions interact with its pricing decisions, the firm has to take into account this interaction when making its design choices.

## Optimal Design of the Review System and Product Pricing

In this subsection, we are interested in determining the firm’s optimal first-period price $p _ { 1 } ,$ , whether to offer the review system, and, if so, the optimal rating scale cardinality s and whether to offer granular report k. We also derive the corresponding market conditions, which are defined by contextual characteristics such as unit misfit cost t, product valuation $v ,$ and product mainstream level .

Figure 5 Firm’s Optimal Strategy for Neutral Products in the Extended Model  
![](/api/attachments/H4MT43JU/fulltext/images/7a0190c4ec556c70288aff24539a2d22c894725c0042e22acd72031a0dfc8fb7.jpg)  
Notes. Figure 5 is based on parameter values $\varepsilon = 0 . 0 3 , \vee = 5 , \bar { V } = 1 0 0 , \alpha = 1 , \mathsf { a n d } \theta = 1$ . Other parameter values generate qualitatively the same results. We focus on the shaded area within the bold lines where all rating levels are rated. For niche products, $s ^ { * } = 2 ,$ and for neutral products, $S ^ { * } \in \{ 2 , 3 , \ldots , \bar { s } \}$ The parameter space can be partitioned into four regions based on the firm’s pricing, review system offering, and granular review report offering decisions: region L0, $p _ { 1 } ^ { * } = 0$ and $k ^ { * } = 0 ;$ ; region U0, $p _ { 1 } ^ { * } = \bar { p } _ { 1 }$ and $k ^ { * } = 0 ;$ ; region U1, $\bar { p } _ { 1 } ^ { * } = \bar { p } _ { 1 }$ and $k ^ { * } = 1 ;$ ; region O, no review system is offered.

For niche and mainstream products, the optimal solutions become overly complex, and no closed-form analytical expression for the separating market conditions can be obtained. Thus, we present the firm’s optimal solutions only for neutral products here in Proposition 3.

Proposition 3 (Optimal Pricing, Review System Offering, and Design Choices for Neutral Prod-<sup>ucts)</sup>. For neutral products $( \theta = 1 )$ , the firm’s optimal pricing, review system offering, and design choices are as follows:

• It is optimal for the firm not to offer a review system $i f v \leq V _ { 1 }$

• It is optimal for the firm to offer a review system and rating scale cardinality has no impact on the firm’s profit $i f v > V _ { 1 }$ . When the firm offers a review system, the firm’s optimal first-period price and review system design choices are

(L1) $p _ { 1 } ^ { * } = 0$ and $k ^ { * } = 1 \mathrm { ~ } i f \mathrm { ~ } v \leq D _ { 1 }$ and $t < \alpha \big ( \bar { v } - \underline { { v } } \big ) / 2$ (L0) p∗ 0 and $k ^ { * } = 0 \mathrm { ~ } i f \mathrm { ~ } v > D _ { 1 }$ and $t < ( \alpha ( \bar { v } - \underline { { v } } ) ) / 2 ,$ $o r \ v > D _ { 3 }$ and $\alpha ( \bar { v } - \underline { { v } } ) / 2 \leq t \leq \alpha ( \bar { v } - \underline { { v } } )$

(U1) $p _ { 1 } ^ { * } = ( \bar { v } + \underline { { v } } - t ) / 2$ and $k ^ { * } = 1 \mathrm { ~ } i f \mathrm { ~ } v \le D _ { 3 }$ and $\alpha ( \bar { v } - \underline { { v } } ) / 2 \le t \le \alpha ( \bar { v } - \underline { { v } } )$ , or $v \le D _ { 1 } + \bar { p } _ { 1 }$ and $t >$ v<sub>¯</sub> <sub>−</sub> v,

(U0) $p _ { 1 } ^ { * } = ( \bar { v } + \underline { { v } } - t ) / 2$ and $k ^ { * } = 0 \mathrm { ~ } i f \mathrm { ~ } v > D _ { 1 } + \bar { p } _ { 1 }$ and $t > \alpha ( \bar { v } - \underline { { v } } )$

The values of $V _ { 1 } , D _ { 1 } ,$ , and $D _ { 3 }$ are defined in the online appendix.

Proposition 3 describes the firm’s optimal pricing and review system design decisions for neutral products, which depend critically on product and consumer characteristics as shown in Figure 5.

Since the firm’s decisions regarding pricing, review system offering, and rating scale cardinality are similar to those of the baseline model, here we focus on discussing the firm’s decision to offer granular reports (k 1). When the unit misfit cost is high relative to product valuation (region U1 in Figure 5), the firm offers granular reports and serves only the favorable customer segment. The firm’s granular report offering decision, k, interacts with its pricing decision. By providing review reports based on specific product attributes, the firm gains the capabilities of segmenting the second-period consumer market and better managing its second-period profit. These gained capabilities alleviate the negative effect of first-period price on second-period profit. As a result, the firm adopts the upper-bound pricing strategy in a greater parameter space when it offers granular reports (k 1) in the review system. The firm’s optimal pricing strategy and review system design choices for niche products are similar to those for neutral products; hence, those are not presented here.

For mainstream products, we demonstrate the firm’s optimal strategies through numerical analysis, since closed-form analytical expressions of the separating market conditions cannot be obtained. Figure 6 presents the firm’s optimal strategy for mainstream products. The moderating effect of contextual characteristics (v and t) on the firm’s granular report offering decision is the same as that for niche and neutral products. Specifically, for a given product valuation $v ,$ as unit misfit cost t increases, the firm moves from not offering to offering granular review reports (e.g., regions I0 I1 in Figure 6). Meanwhile, the moderating effect of contextual characteristics (v and t) on the firm’s pricing decision is the opposite of that for niche and neutral products. Specifically, for a given unit misfit cost t, as product valuation v increases, the firm moves from lower-bound pricing, to interior pricing, to upper-bound pricing (e.g., regions $\mathrm { L } 0 $ I0 <sub>→</sub> U0 in Figure 6).

Figure 6 Firm’s Optimal Strategy for Mainstream Products in the Extended Model  
![](/api/attachments/H4MT43JU/fulltext/images/bb85d5b66b3170c30a729098e9900cdcf174361b82b04cab6a193a436be53433.jpg)  
Notes. Figure 6 is based on parameter values $\varepsilon = 0 . 0 3 , \vee = 5 , \bar { V } = 1 0 0 , \alpha = 1 , \beta = 0 ,$ , and  2. Other parameter values generate qualitatively the same results. We focus on the shaded area within the bold lines where all rating levels are rated. For all mainstream products, $s ^ { * } = \bar { s } = 1 0$ . The parameter space can be partitioned into six regions based on the firm’s pricing, review system offering, and granular review report offering decisions: region $\mathsf { L } 0 , p _ { 1 } ^ { * } = 0$ and $k ^ { * } = 0 ;$ region I0, $0 < p _ { 1 } ^ { * } < \bar { p } _ { 1 }$ and $k ^ { * } = 0 ;$ region U0, $p _ { 1 } ^ { * } = \bar { p } _ { 1 }$ and $k ^ { * } = 0 ;$ region I1, $0 < p _ { 1 } ^ { * } < \bar { p } _ { 1 }$ and $k ^ { * } = 1 ;$ region U1, $p _ { 1 } ^ { * } = \bar { p } _ { 1 }$ and $k ^ { * } = 1 ;$ region O, no review system is offered.

## Concluding Remarks

Consumer review systems have become an important marketing communication tool for firms to facilitate consumer sharing and consumer learning about their products. We study the design of such review systems and examine the impact of review system design features on past customers’ reviews and future customers’ purchasing decisions. To explore the information role of consumer review systems, we explicitly depict both consumer rating and rating interpretation processes and model two types of product uncertainty—valuation uncertainty and misfit uncertainty. Extending prior literature, we formally model review system design as a firm’s strategic decision and examine its impact on consumer learning. We show that to fully benefit from consumer review systems, firms need to understand the mechanism of consumer reviews, actively participate in the design of review systems, and, most important, integrate the review system design choices with other operational decisions such as pricing.

In addition, when making pricing and review system design decisions, firms should carefully evaluate market conditions such as how the true product valuation matches their consumers’ perception, whether their products appeal to a mass market or a niche market, and how much consumers value the fit of the product. We find that for low-value products, information revealed through the review system may hurt the firms. Hence, a review system is valuable only when the true product valuation is higher than a threshold.

From the implementation perspective, it is beneficial for firms to display review outcomes for some products but not for others. Another important finding is that different types of products benefit from different kinds of review system design. Currently, most existing consumer review systems (e.g., Amazon, Etsy, L.L.Bean, Macy’s, Target, and Walmart) use the fivestar rating scale. However, our findings suggest that the “like/dislike” type of system is good for niche products, whereas the “1 to 10 stars” type of system is good for mainstream products. Neutral products can use any rating scale cardinality. Hence, based on firms’ dominant product offerings, they should choose appropriate rating scale cardinalities accordingly. For example, for sites like Etsy that mainly offer handmade, customized products $( \mathrm { i . e . , }$ niche products), it may be more beneficial to adopt the “like/dislike” type of review system.

Recently, more and more retailers have begun to offer product attribute reviews to provide consumers easily accessible product information to mitigate the lack of the touch-and-feel experience in online shopping. We incorporate granular review reports as a design feature in our model and investigate firms’ strategic offering decisions. When consumer misfit cost is low, firms are advised to offer only overall ratings and no product attribute reviews in the review system. On the other hand, when consumer misfit cost is high, firms are advised to solicit and present product attribute reviews in the review system to reduce consumer uncertainty on product fit and attract the favorable consumer segment. For example, we observe that firms often display granular review reports for products such as clothing and shoes because the lack of a touch-and-feel experience for consumers leads to a higher uncertainty on product fit and, therefore, a lower likelihood to commit to the purchase. For these products, granular review reports offered by retailers (e.g., L.L.Bean, Macy’s, Target, and Walmart) can further inform consumers on numerous product attributes, such as true color, fit to body shape, material, comfort level, style, etc. Consequently, these granular review reports can reduce consumers’ uncertainty on product fit such that only those who consider the products a good fit will purchase. However, we also observe that these retailers do not offer such granular review reports for all product categories that they carry. This kind of producttype-based review system design choice (i.e., whether to offer granular review reports) is consistent with our findings.

Because customers’ postpurchase net utility is affected by product price, firms can influence customer reviews by manipulating first-period price. We often see customers commenting that the product is worth the price paid. Firms may adopt the lowerbound pricing to enhance consumer reviews to maximize their second-period profit. By contrast, firms may take advantage of information asymmetry on product valuation by charging the maximum possible price in the first period to pursue the maximum first-period profit. However, because different types of products benefit from different review system design features, firms should take into account the interaction between pricing and design decisions while choosing the optimal pricing strategy for each product type.

Although this work has several limitations, it sheds light on firms’ review system design and product pricing decisions and opens several directions for future research. In the consumer rating process, we only consider customers’ postpurchase net utility and cognitive cost of reviewing the product as the main drivers for their review propensity. We also assume the benefit of reviewing the product is the same for all customers. Existing literature on review propensity has identified other relevant factors such as firms’ marketing efforts (Dellarocas and Narayan 2006), product availability (Dellarocas and Narayan 2006, Dellarocas et al. 2010), product popularity (Dellarocas et al. 2010), product controversy (Dellarocas and Narayan 2006), and previously posted reviews (Dellarocas et al. 2010, Moe and Schweidel 2012). The current review propensity model can be extended to incorporate these factors. Future work can allow the review benefit to vary across different products and different customers based on these factors. In the rating interpretation process, there might be other relevant contextual factors such as consumers’ online experience and reviewer identity. Experienced consumers may learn more from product reviews than novice consumers. Reviews written by verified customers may be perceived differently from those written by anonymous users.

This paper studies the optimal design of sellermanaged consumer review systems. It would be interesting to investigate the optimal design problem if the consumer review system were managed by a third party. In addition, strategic consumers may view the firm’s review system design choice as a signal for product characteristics and adjust their beliefs accordingly. Future work can study the impact of such strategic consumer behavior on the firm’s strategies.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2015.0594.

## Acknowledgments

The authors thank the senior editor, the associate editor, three anonymous reviewers, and seminar participants at the 2012 INFORMS Annual Meeting, 2012 International Conference on Information Systems, and 2013 Hawaii International Conference on System Sciences for their helpful comments and suggestions. They also thank the Networks, Electronic Commerce, and Telecommunications Institute for funding a part of this research.

## References

Anderson SP, De Palma A, Thisse JF (1992) Discrete Choice Theory of Product Differentiation (MIT Press, Cambridge, MA).

Archak N, Ghose A, Ipeirotis PG (2011) Deriving the pricing power of product features by mining consumer reviews. Management Sci. 57(8):1485–1509.

Baddeley A (1992) Working memory. Science 255(5044):556–559.

Bakos Y, Dellarocas C (2011) Cooperation without enforcement? A comparative analysis of litigation and online reputation as quality assurance mechanisms. Management Sci. 57(11): 1944–1962.

Basu A, Hevner AR (1992) The analysis and design of embedded knowledge-based systems using box structure methods. J. Management Inform. Systems 8(4):117–146.

Bates JM, Granger CWJ (1969) The combination of forecasts. Oper. Res. Quart. 20(4):451–468.

Bettman JR, Luce MF, Payne JW (1998) Constructive consumer choice processes. J. Consumer Res. 25(3):187–217.

Chen Y, Xie J (2005) Third-party product review and firm marketing strategy. Marketing Sci. 24(2):218–240.

Chen Y, Xie J (2008) Online consumer reviews: A new element of marketing communications mix. Management Sci. 54(3): 477–491.

Chevalier JA, Mayzlin D (2006) The effect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Clemen RT (1989) Combining forecasts: A review and annotated bibliography. Internat. J. Forecasting 5(4):559–583.

Clemons EK, Gao G, Hitt LM (2006) When online reviews meet hyperdifferentiation: A study of the craft beer industry. J. Management Inform. Systems 23(2):149–171.

Dellarocas C (2003) The digitization of word of mouth: Promise and challenges of online feedback mechanisms. Management Sci. 49(10):1407–1424.

Dellarocas C (2006) Strategic manipulation of Internet opinion forums: Implications for consumers and firms. Management Sci. 52(10):1577–1593.

Dellarocas C, Narayan R (2006) A statistical measure of a population’s propensity to engage in post-purchase online word-ofmouth. Statist. Sci. 21(2):277–285.

Dellarocas C, Gao G, Narayan R (2010) Are consumers more likely to contribute online reviews for hit or niche products? J. Management Inform. Systems 27(2):127–157.

Dellarocas C, Zhang XM, Awad NF (2007) Exploring the value of online product reviews in forecasting sales: The case of motion pictures. J. Interactive Marketing 21(4):23–45.

Dichter E (1966) How word-of-mouth advertising works. Harvard Bus. Rev. 44(6):147–166.

Dimoka A, Hong Y, Pavlou PA (2012) On product uncertainty in online markets: Theory and evidence. MIS Quart. 36(2): 395–426.

Duan W, Gu B, Whinston AB (2008) The dynamics of online wordof-mouth and product sales—An empirical investigation of the movie industry. J. Retailing 84(2):233–242.

Engel JF, Blackwell RD, Miniard PW (1993) Consumer Behavior (Dryden Press, Fort Worth, TX).

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3): 291–313.

Fowler GA (2009) What do you think? Companies are learning to make the most out of customers’ online reviews of their products. Wall Street J. (October 12). http://www.wsj.com/articles/ SB10001424052970204488304574429141682175478

Franses PH, Paap R (2001) Quantitative Models in Marketing Research (Cambridge University Press, Cambridge, UK).

Gao G, Greenwood B, Agarwal R, McCullough J (2015) The information value of online physician ratings. MIS Quart. 39(3):565–589.

Godes D, Mayzlin D (2004) Using online conversations to study word-of-mouth communication. Marketing Sci. 23(4):545–560.

Greenwald A, Kannan K, Krishnan R (2010) On evaluating information revelation policies in procurement auctions: A Markov decision process approach. Inform. Systems Res. 21(1):15–36.

Guo Z (2012) Optimal decision making for online referral marketing. Decision Support Systems 52(2):373–383.

Guo Z, Koehler GJ, Whinston AB (2012) A computational analysis of bundle trading markets design for distributed resource allocation. Inform. Systems Res. 23(3-part-1):823–843.

Hao L, Li X, Tan Y, Xu J (2011) The economic value of ratings in app market. Working paper, University of Notre Dame, Notre Dame, IN.

Hennig-Thurau T, Gwinner KP, Walsh G, Gremler DD (2004) Electronic word-of-mouth via consumer-opinion platforms: What motivates consumers to articulate themselves on the Internet? J. Interactive Marketing 18(1):38–52.

Hong Y, Pavlou PA (2014) Product fit uncertainty in online markets: Nature, effects, and antecedents. Inform. Systems Res. 25(2): 328–344.

Hu N, Zhang J, Pavlou PA (2009) Overcoming the J-shaped distribution of product reviews. Comm. ACM 52(10):144–147.

Ji Y, Mookerjee VS, Sethi SP (2005) Optimal software development: A control theoretic approach. Inform. Systems Res. 16(3): 292–306.

Ji Y, Kumar S, Mookerjee VS, Sethi SP, Yeh D (2011) Optimal enhancement and lifetime of software systems: A control theoretic analysis. Production Oper. Management 20(6):889–904.

Kuksov D, Xie Y (2010) Pricing, frills, and customer ratings. Marketing Sci. 29(5):925–943.

Kwark Y, Chen J, Raghunathan S (2014) Online product reviews: Implications for retailers and competing manufacturers. Inform. Systems Res. 25(1):93–110.

Li X, Hitt LM (2010) Price effects in online product reviews: An analytical model and empirical analysis. MIS Quart. 34(4):809–831.

Liu D, Chen J, Whinston AB (2010) Ex ante information and the design of keyword auctions. Inform. Systems Res. 21(1):133–153.

Liu Y (2006) Word-of-mouth for movies: Its dynamics and impact on box office revenue. J. Marketing 70(3):74–89.

Malhotra NK (1984) The use of linear logit models in marketing research. J. Marketing Res. 21(1):20–31.

Mangalindan M (2007) Web stores tap product reviews. Wall Street J. (September 11), http://www.wsj.com/articles/SB11894 6406034923071.

Mayzlin D (2006) Promotional chat on the Internet. Marketing Sci. 25(2):155–163.

Miller GA (1956) The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychol. Rev. 63(2):81–97.

Moe WW, Schweidel DA (2012) Online product opinions: Incidence, evaluation, and evolution. Marketing Sci. 31(3):372–386.

Shugan SM (1980) The cost of thinking. J. Consumer Res. 7(2):99–111.

Sullivan EA (2008) Consider your source. Marketing News 42(3): 16–19.

Sun M (2012) How does the variance of product ratings matter? Management Sci. 58(4):696–707.

Sundaram DS, Mitra K, Webster C (1998) Word-of-mouth communications: A motivational analysis. Adv. Consumer Res. 25: 527–531.

E-tailing Group, The (2010) The 2010 social shopping study. Accessed May 3, 2015, http://www.e-tailing.com/content/?p =1193.

Zhu F, Zhang X (2010) Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. J. Marketing 74(2):133–148.
