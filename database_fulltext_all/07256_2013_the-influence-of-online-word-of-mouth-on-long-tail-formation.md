---
otero_id: 7256
otero_key: "3ZR3S7YR"
title: "The influence of online word-of-mouth on long tail formation"
authors: "Bin Gu; Qian Tang; Andrew B. Whinston"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The in<sup>fl</sup>uence of online word-of-mouth on long tail formation

Bin Gu <sup>b</sup>, Qian Tang <sup>a,</sup>⁎, Andrew B. Whinston <sup>a</sup>

<sup>a</sup> Department of Information, Risk, and Operations Management, McCombs School of Business, the University of Texas at Austin, 1 University Station, B6500, Austin, TX 78712, United States <sup>b</sup> Department of Information Systems, W P Carey School of Business, Arizona State University, P O Box 874606, Tempe, AZ 85287, United States

a r t i c l e i n f o

Available online xxxx

Keywords: Long tail Word-of-mouth (WOM) Customer review Information cascade

## a b s t r a c t

The long tail phenomenon has been attributed to both supply side and demand side economies. While the cause on the supply side is well-known, research on the demand side has largely focused on the awareness effect of online information that helps consumers discover new and often niche products. This study expands the demand side factors by showing that online information also in<sup>fl</sup>uences the long tail phenomenon through the informative effect, which affects consumers' evaluation of product quality. We examine the informative effect in the context of online WOM. Two sets of theories suggest opposite directions for the implication of the informative effect. Information search and information cascade literatures indicate that WOM provides additional information to consumers, reduces the occurrence of information cascade, and encourages the formation of long tail. Studies on behavior heuristics, however, suggest that consumers tend to ignore online information inconsistent with their prior beliefs, which leads to a rich-gets-richer effect for popular products and curtail the formation of the long tail. We empirically examine the con<sup>fl</sup>ict by analyzing different impacts of online WOM across product popularity and WOM ratings. Using a panel data collected from Amazon.com, we show that positive reviews improve the sales of popular products more than the sales of niche products, while negative reviews hurt niche products more than popular products. The results are consistent with the prediction of the behavior heuristic and suggest that online WOM restrains the formation of long tail.

Published by Elsevier B.V.

## 1. Introduction

Online retailers have long noticed that the sales of non-hit or niche products account for a signi<sup>fi</sup>cant portion of overall product sales. This phenomenon is known as the long tail [1] and has attracted attention of both industry practitioners and academic researchers. Several factors are conducive to the emergence of the long tail phenomena in online markets. The supply side drivers include lower storage costs, faster distribution and the aggregation of geographically dispersed niche markets [5]. These enable online retailers to carry a far wider range of products than their physical counterparts. On the demand side, studies note that the use of information sharing mechanisms such as recommender systems, co-purchase networks, search tools, and blog sites, enables customers to discover new and niche products more easily and encourages the long tail formation [1,4,5,15,34,42].

Although prior demand side studies focus on how online information increases awareness of less known products, the in<sup>fl</sup>uence of online information often goes beyond helping consumers discover new products. Consumers are known to use a two-stage process in making purchase decisions [28]. In the <sup>fi</sup>rst stage, consumers identify a set of potential products for further consideration. In this stage, consumers use IT-enabled tools both actively and passively to identify products of potential interest. Search tools and recommendation systems help narrow down possible choices according to consumer preferences. In the second stage, consumers obtain detailed information on each product in the consideration set to form a purchase decision. Product awareness created by searching tools and recommendation systems is important in the <sup>fi</sup>rst stage. However, it is the detailed product quality information that ultimately shapes consumers' purchase decisions in the second stage. Such information increasingly comes from online sources such as online WOM. However, little is known on how these information sources in<sup>fl</sup>uence the long tail phenomenon. The goal of this study is to take the <sup>fi</sup>rst step to understand this in<sup>fl</sup>uence.

Two sets of theories suggest opposite directions for the impact of online WOM on the long tail phenomenon. A key challenge for electronic commerce is that customers are often uncertain about product quality before purchase. The lack of information leads to herding where consumers follow the choices of others, as suggested by information search and informational cascade literatures [3]. In an informational cascade, it is optimal for a user to follow predecessors' behavior and ignore his private information. As such, a few “hit” products take up the most sales. Such behavior could lead to “bad” herding where popular products are not necessarily of high quality. One of the key conditions for informational cascade is that users do not have access to the private information of others. However, online review allows consumers to reveal private information, helps future consumers to learn about the true quality before purchase, and reduces the occurrence of “bad” herding [36]. In particular, the arrival of negative WOM could stop the positive informational cascade of a popular but low quality product, while the arrival of positive WOM could stop the negative cascade of an unpopular but high quality product [3]. From this respect, WOM information encourages the formation of the long tail.

However, the opposite is implied by behavior heuristics studies. Behavior heuristics theories believe that individuals are biased in making adjustments to accommodate new information. Information consistent with prior belief often leads to overreaction, while contradictory information leads to under-reaction [26,36]. Since product popularity commonly serves as a starting point for prior belief, consumers tend to overreact to positive WOM on popular products and negative WOM on unpopular products, and underreact to negative WOM on popular products and positive WOM on unpopular products, leading to a rich-get-richer effect. In this respect, WOM constrains the formation of the long tail.

To examine the con<sup>fl</sup>icting hypotheses, we note that the hypotheses suggest that the in<sup>fl</sup>uence of a customer review depends on the interaction between review valence and product popularity. As such, testing the hypotheses requires an analysis at the customer review level instead of the product level. This is in contrast with most prior WOM research that often uses aggregate WOM measures such as average review rating to study the effect of WOM at the product level. Compared to the product level analysis, analysis at the review level allows us to capture consumers' reaction to each speci<sup>fi</sup>c review and how their reaction varies for different combinations of review valence and product popularity. To facilitate the analysis, we use a <sup>fi</sup>rst difference approach. This approach allows us to analyze the in<sup>fl</sup>uence of each customer review on changes in product sales and provides signi<sup>fi</sup>cant <sup>fl</sup>exibility in modeling factors that moderate the in<sup>fl</sup>uence of individual customer reviews. We apply the model to a panel data collected from Amazon.com on 3000 books over 200 days. The results indicate that positive WOM bene<sup>fi</sup>ts popular products more than niche products, while negative WOM hurts niche products more. Our <sup>fi</sup>nding supports the prediction of behavior heuristics theory and suggests that consumers are not fully rational in reacting to incoming customer reviews. Instead, they are biased toward their initial expectation. As a result, online WOM constrains the formation of the long tail.

The rest of the paper is organized as follows. Section 2 is literature review. Section 3 introduces the theoretical background and develops key hypotheses. Section 4 develops a <sup>fi</sup>rst difference model that allows WOM's in<sup>fl</sup>uence to differ across product popularity and WOM valence. Section 5 describes the data collection process. Section 6 presents the empirical results. Section 7 discusses the implication of our <sup>fi</sup>ndings and concludes the study.

## 2. Literature review

## 2.1. Online WOM

Online WOM plays an important role in electronic commerce. A survey of Bizrate.com found that 44% of users consulted opinion sites prior to making a purchase [7]. This survey also found that 59% of respondents considered consumer-generated reviews to be more valuable than expert reviews. A number of studies have been conducted to examine the impact of WOM on consumer purchase decisions [2,9,13,16,17,20,23,30,40,42]. These studies reveal that online WOM has both awareness effect and informative effect. The awareness effect is re<sup>fl</sup>ected in the in<sup>fl</sup>uence of WOM volume on product sales. WOM volume captures the underlying dispersion of WOM within and across online communities and studies show that WOM volume predicts future product sales [13,17,23,27].

The informative effect for product quality, on the other hand, is mainly re<sup>fl</sup>ected in review ratings and their impact on product sales. Zhu and Zhang [41] <sup>fi</sup>nd that online customer reviews are important resource for consumers to seek product quality information. Moon et al. [28] use new movie ratings as a measure of movie performance and argue that positive ratings can enhance the effectiveness of advertising spending to raise movie revenues. Chevalier and Mayzlin [9] compare book sales across two online retailers and <sup>fi</sup>nd that improvement in a book's average review rating at one site leads to an increase in relative sales at that site. Similarly, Zhang et al. [40] study the relationship between movie ratings and box of<sup>fi</sup>ce sales and <sup>fi</sup>nd that online consumer ratings have signi<sup>fi</sup>cant impact on movie revenue. Moe and Trusov [31] decompose the rating effect on sales into a baseline component and a social dynamic component and show both the direct impact of baseline component and the indirect impact through social dynamics in<sup>fl</sup>uence product sales. Clemons et al. [12] suggest that the informative effect of WOM plays a key role in rede<sup>fi</sup>ning a <sup>fi</sup>rm's product strategy. We extend this stream of literature by noting that the in<sup>fl</sup>uence of WOM could vary with the interaction between WOM and product popularity due to economic or behavioral motivations. We also show that such variations could have signi<sup>fi</sup>cant implications for the long tail phenomenon.

Our analysis complements the literature on the informative effect of WOM. For example, Sun [36] models high average rating as an indicator for high product quality and high rating variance as an indicator for niche products, which some consumers love and others hate. She <sup>fi</sup>nds that a higher standard deviation of ratings on Amazon improves a book's relative sales rank when the average rating is lower than 4.1 stars. In contrast, Chintagunta [10] <sup>fi</sup>nd that review variance does not matter after controlling for movie speci<sup>fi</sup>c and market speci<sup>fi</sup>c effects.

Our analysis also complements recent studies that identify factors moderating the in<sup>fl</sup>uence of WOM. Zhu and Zhang [41] claim that online reviews are more in<sup>fl</sup>uential on less popular video games and games whose players have greater Internet experience. Chevalier and Mayzlin [9] reveal that negative WOM is more in<sup>fl</sup>uential than is positive WOM. Chen et al. [8] and Duan et al. [18] <sup>fi</sup>nd that WOM is more in<sup>fl</sup>uential on less popular products. Hu et al. [29] and Chen et al. [8] show the importance of reviewer reputation in determining the in<sup>fl</sup>uence of the review. Moon et al. [28] suggest that positive ratings can enhance the effectiveness of advertising spending to raise movie revenues. We complement these literatures by identifying new moderating factors based on information search and informational cascade theory and behavior heuristic theory. Our hypotheses suggest that consumers infer product quality information from both WOM and product popularity and that whether the two sets of information are consistent with or contradictory to each other could have signi<sup>fi</sup>cant in<sup>fl</sup>uence on consumer purchase decisions.

## 2.2. The long tail

This study also contributes to the emerging literature on the long tail phenomenon. Brynjolfsson et al. [6] <sup>fi</sup>nd that the sales distribution of a retailer's online channel is less concentrated than that of its traditional channels, indicating that a reduction in search costs contributes to the long tail phenomenon. Rahman and Hahn [35] <sup>fi</sup>nd that the long tail phenomenon is more prevalent in search goods than in experience goods, and Wimble et al. [39] <sup>fi</sup>nd the product dispersion of purchases made by households with broadband access is more <sup>fl</sup>attened than that by households without broadband access. Both studies suggest the importance of search costs in the long tail formation. A number of long tail studies take a step further to identify the underlying information sources that facilitate the long tail phenomenon. Oestreicher-Singer and Sundararajan [33] show that the long tail phenomenon is in<sup>fl</sup>uenced by the presence of co-purchase networks which allows online consumers to observe products commonly bought together. Dewan and Ramaprasad [15] <sup>fi</sup>nd that blogging activities lead to more purchases of niche products and contribute to the long tail phenomenon. Goh and Bockstedt [24] show that product sampling plays an important role in the long tail phenomenon.

Prior studies of the long tail phenomenon also reveal the presence of both long tail and superstar phenomenon. Most studies consider the impacts of WOM on popular and unpopular products respectively. Elberse and Oberholzer-Gee [19] analyze the distribution of US video sales from 2000 to 2005 and <sup>fi</sup>nd both the long tail phenomenon where “the number of titles that sell only a few copies increased almost twofold” and superstar phenomenon where “an even smaller number of titles account for the bulk of sales”. Fleder and Hosanagar [21] study the in<sup>fl</sup>uence of product recommendations provided by retailer using collaborate <sup>fi</sup>ltering algorithm and conclude that such recommendation may not promote the sales of less popular products as recommendations are based on historical product sales. Consequently, popular products are more likely to be recommended and purchased. Tucker and Zhang [37] and Duan et al. [18] indicate that the presence of product popularity information signi<sup>fi</sup>cantly increases the sales of popular products. Dellarocas and Narayan [14] suggest that popular products are more likely to be discussed by consumers, which contributes to the superstar phenomenon. Hervas-Drane [28] suggests that consumers with preference for mass market products are more likely to seek WOM because they are more likely to <sup>fi</sup>nd other consumers with similar preference.

Complementary to these studies, we recognize that online information not only increases product awareness but also enables consumers to better evaluate product quality. The in<sup>fl</sup>uence of this informative effect, however, could differ for popular products vs. niche products and affect the formation of the long tail.

## 3. Theoretical background and hypothesis

Prior e-commerce studies have noted that informational cascades often drive consumer purchase decisions. An informational cascade occurs when an individual, having observed the actions of those ahead of him, follows the behavior of predecessors without considering his own private information [3]. Informational cascade in e-commerce arises because each online consumer faces two sources of product quality information. One is product popularity information (e.g. sales rank) provided by online retailers based on historical consumer purchase decisions. Product popularity information is relatively objective. However, the quality that consumers infer from this information may not represent the true product quality since product sales are often in<sup>fl</sup>uenced by other factors such as price or information cascade. The other information source is WOM, or customer reviews in most cases [18]. Customer reviews reveal consumers' perception of product quality directly and thus provide access to the private information of others. However, they are relatively subjective and can be affected by reviewers' characteristics [32]. Consumers combine these two information sources to arrive at purchase decisions. If the two information sources are contradictory to each other, consumer decision is determined by the relative strengths of the two sources. When customer reviews are scarce, consumers are more likely to follow the step of their predecessors, leading to an informational cascade. The increasing availability of customer reviews improves product information quality, leading to a reduction in informational cascades and facilitating the formation of the long tail.

Informational cascade theory also suggests that an information cascade is fragile if predecessors' private information is accessible to successors. In particular, the arrival of new information contradictory to the direction of information cascades can break the informational cascade process [3]. Informational cascade could be either positive or negative, resulting in either extremely popular or unpopular products. Without private information, consumers infer from the observed sales that popular products are likely to be high quality and unpopular products are likely to be low quality. However, as more customer reviews come in, revealing purchasers' private information, rational consumers can infer whether the popularity re<sup>fl</sup>ects the true quality or just “bad” cascades, which cause low quality products to sell well or high quality products to remain unknown. From this point, positive and negative reviews have different impacts on popular and unpopular products. Speci<sup>fi</sup>cally, positive reviews on a popular product con<sup>fi</sup>rm the high quality of the product and thus sustain the informational cascade, while negative reviews on a popular product suggest that the popular product is low quality and can break the informational cascade. On the other hand, positive reviews on an unpopular product indicate that the product is high quality and break the negative informational cascade, while negative reviews on an unpopular product sustain the status quo. As such, positive reviews on hit products and negative reviews on niche products sustain the “good” informational cascade and keep the status quo, while negative reviews on hit products and positive reviews on niche products could stop the “bad” informational cascades, reducing the sales increase on hit products and accelerating the sales increase on niche products. The above analysis suggests that positive reviews would bene<sup>fi</sup>t niche products more, while the negative review would hurt popular products more, leading to a more <sup>fl</sup>attened sales distribution, i.e., the long tail. Accordingly, we propose the following hypothesis:

H1a. The impact of a positive (negative) customer review on niche (popular) products will be greater than its impact on popular (niche) products.

While informational cascade theory suggests the positive impact of WOM on the formation of the long tail, literatures on behavior economics suggests that the impact could be in the opposite direction. According to behavior economics, individuals use various heuristics in information processing and decision making [38]. While informational cascade theory assumes rationality, behavior economics argues that individuals are not perfectly rational. Instead, certain bias exists during the information update process. A commonly used behavior heuristic is anchoring and adjustment, i.e. people make adjustment incrementally from their prior expectation and often make insuf<sup>fi</sup>- cient adjustment when new evidence is inconsistent with their prior expectation [26]. As aforementioned, online consumers have two sources of information: popularity information provided by the websites and product information from customer reviews. Consumers typically form their initial expectations based on popularity information, and then adjust their expectations according to customer reviews. Because of the heuristic bias, consumers tend to ignore information that is inconsistent with their prior beliefs, while they pay more attention to information that is consistent with their beliefs. This bias results in over-reaction to evidence consistent with their expectations and under-reaction to information contradictory to their expectations [34]. Therefore, this stream of theories suggests different impacts of positive and negative reviews on hit and niche products but in a different direction. In particular, a positive review on a popular product con<sup>fi</sup>rms consumers' prior expectation and encourages sales, while a negative review on a popular product tends to be ignored or at least downplayed because it contradicts consumers' initial expectation. For an unpopular product, a negative review con<sup>fi</sup>rms consumers' expectation and discourages sales, while a positive review tends to be ignored or downplayed. As a result, we expect that a positive incremental review have more impact on popular products than on niche products while a negative incremental review hurts niche products more. Therefore, based on behavior heuristics, we derive the opposite hypothesis:

H1b. The impact of a positive (negative) review on popular (niche) products will be greater than its impact on niche (popular) products.

H1a and H1b are two hypotheses derived from two streams of theories (Table 1). By testing the two competing hypotheses, we can test whether online WOM facilitates or inhibits the formation of the long tail and whether consumers are rational or biased in making purchase decisions. If H1a is supported, we can conclude that online WOM contributes to the formation of the long tail and consumers are able to process information rationally. If H1b is supported, we would arrive at the opposite conclusion that online WOM shifts sales distribution against the long tail and consumers are biased toward the starting point in updating their expectations using incoming WOM.

Table 1  
Research hypotheses.

<table><tr><td>Hypothesis</td><td>Positive reviews</td><td>Negative reviews</td></tr><tr><td>H1a: online customer review facilitates long tail formation.</td><td>Impact niche products more</td><td>Impact popular products more</td></tr><tr><td>H1b: online customer review inhibits long tail formation.</td><td>Impact popular products more</td><td>Impact niche products more</td></tr></table>

## 4. Empirical model

A unique challenge in assessing the in<sup>fl</sup>uence of online WOM is that its in<sup>fl</sup>uence is cumulative and long lasting. Product sales today are not only affected by today's customer reviews but also by all previously posted customer reviews about the product. As a result, prior studies often use a variety of aggregation functions to summarize customer reviews to date on a given product as a way to study their in<sup>fl</sup>uence on product sales. An analysis at the aggregate level, however, is not desirable here because the hypotheses indicate that the in<sup>fl</sup>uence of each piece of online customer review could vary depending on the rating and product popularity. To address this empirical challenge, we take a new approach by adopting a <sup>fi</sup>rst-difference model that focuses on the in<sup>fl</sup>uence of the arrival of each customer review on changes in product sales. This approach allows greater <sup>fl</sup>exibility in modeling the in<sup>fl</sup>uence of WOM on product sales. In particular, it allows the in<sup>fl</sup>uence of individual consumer reviews to vary with product popularity, product age, review rating, review volume, and the interactions between WOM and product popularity.

## 4.1. First difference model with heterogeneous influence

While this paper focuses on the informative aspect of WOM, it is necessary to incorporate both awareness and informative effects in the empirical model. In prior literature, the informative and awareness effects are captured by the average review rating and review volume respectively [9] using a log-linear demand function as follows:

$$
\begin{array}{l} L g S a l e s _ {i t} = \beta A v g R a t i n g _ {i t} + \gamma L g N u m O f R e v i e w s _ {i t} + \delta L g P r i c e _ {i t} + \eta X _ {i t} \\ \quad + \mu_ {i} + v _ {t} + \epsilon_ {i t}. \end{array}\tag{1}
$$

In the above equation, β measures the in<sup>fl</sup>uence of review ratings on product sales, capturing the informative effect, while $\gamma$ measures the in<sup>fl</sup>uence of review volume on product sales, capturing the awareness effect. δ assesses the price elasticity. $X _ { i t }$ is a vector containing all the control variables and η captures the in<sup>fl</sup>uence of the control variables. The model also controls for product and time <sup>fi</sup>xed effects.

As we mentioned earlier, Eq. (1) imposes constraints on the relationship between WOM and product sales. In particular, the model implies that each customer review has the same magnitude of in<sup>fl</sup>uence on a product's sales and the in<sup>fl</sup>uence of customer reviews is the same across products with different popularity and age. These assumptions allow parsimony in assessing the overall in<sup>fl</sup>uence of WOM but are overly restrictive to assess the in<sup>fl</sup>uence of individual pieces of WOM. To address this limitation, we propose a new approach to allow more <sup>fl</sup>exibility in estimating the in<sup>fl</sup>uence of WOM. Our objective is to shift the consideration of the aggregate effect of all WOM on a product to focusing on how newly arrived WOM on a given day affects changes in product sales using a <sup>fi</sup>rst difference approach. This approach enables us to cancel out the in<sup>fl</sup>uence of previous WOM and focus on the in<sup>fl</sup>uence of newly arrived WOM. To transform the aggregate level model to the disaggregate level, we start with taking the <sup>fi</sup>rst difference between t and t+1 of Eq. (1).

$$
\begin{array}{l} \Delta L g S a l e s _ {i t} = \beta \Delta A v g R a t i n g _ {i t} + \gamma \Delta L g N u m O f R e v i e w s _ {i t} + \delta \Delta L g P r i c e _ {i t} \\ \qquad + \eta \Delta X _ {i t} + \Delta \mathbf {v} _ {t} + \epsilon_ {i t}. \end{array}\tag{2}
$$

Eq. (2) indicates that, on days without new WOM, changes in average review rating and changes in number of reviews are both zero. In this case, sales changes are entirely driven by changes in product prices, time effect and other changes in the control variables. On the other hand, on days with newly arriving WOM, WOM has two effects on sales changes. First, the arrival of WOM may in<sup>fl</sup>uence average review rating, thus affect future product sales. Second, the very presence of new WOM indicates underlying WOM dispersion that may increase product awareness and affect future product sales. In Eq. (2), β captures the incremental informative effect of WOM, while γ captures the incremental awareness effect of WOM. The <sup>fi</sup>rst-difference approach shifts the focus from the in<sup>fl</sup>uence of overall WOM in Eq. (1) to the in<sup>fl</sup>uence of individual pieces of WOM that arrives on a given day in Eq. (2). This disaggregated approach provides a foundation that allows us to further extend the model to consider how the in<sup>fl</sup>uence of these individual pieces of WOM could be moderated by factors proposed in the hypotheses.

## 4.2. Moderating effect on WOM influence

We <sup>fi</sup>rst extend the model to allow the in<sup>fl</sup>uence of positive reviews and negative reviews to differ. We divide reviews into two categories – negative reviews and positive reviews – based on their in<sup>fl</sup>uence on product average rating. If the arrival of a customer review reduces a product's average review rating, we de<sup>fi</sup>ne it as a negative review. If its rating is greater than the previous average, we de<sup>fi</sup>ne it as a positive review. A positive review will bring an improvement in a product's review rating and a negative one will impose a negative impact on review rating. To allow the in<sup>fl</sup>uences to differ, we split the review rating variable into two variables: one for positive changes in customer reviews rating and the other for negative changes in customer reviews rating.

$$
\left[ \Delta \text { AvgRating } _ {i t} \right] ^ {+} = \left\{ \begin{array}{c} \text { AvgRating } _ {i t}, \text { if   } \text { AvgRating } _ {i t} > 0 \\ 0, \text { otherwise } \end{array} \right.
$$

$$
[ \Delta A v g R a t i n g _ {i t} ] ^ {-} = \left\{ \begin{array}{c} A v g R a t i n g _ {i t}, \text {   if   } A v g R a t i n g _ {i t} <   0 \\ 0, \text {   otherwise   } \end{array} \right..
$$

We use coef<sup>fi</sup>cients $\beta ^ { + }$ and $\beta ^ { - }$ to identify their in<sup>fl</sup>uences:

$$
\begin{array}{c} \Delta L g S a l e s _ {i t} = \beta^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} + \beta^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \\ \qquad + \gamma \Delta L g N u m O f R e v i e w s _ {i t} + \delta \Delta L g P r i c e _ {i t} + \eta \Delta X _ {i t} + \Delta v _ {t} + \epsilon_ {i t}. \end{array}\tag{3}
$$

Hypotheses 1a and 1b suggest that the in<sup>fl</sup>uence of positive reviews and negative reviews is moderated by the interactions between review rating and product popularity. H1a suggests that reviews with rating contradictory to product popularity are more in<sup>fl</sup>uential while H1b suggests that reviews with rating consistent with product popularity are more in<sup>fl</sup>uential. The hypotheses indicate that the in<sup>fl</sup>uence of positive reviews and negative reviews is not constant. Rather, it is a function of product popularity. We therefore extend Eq. (3) by making $\beta ^ { + }$ and $\beta ^ { - }$ functions of product popularity. That is,

$$
\beta^ {+} = \beta_ {1} ^ {+} + \beta_ {2} ^ {+} \times L g S a l e s _ {i, t - 1}\tag{4}
$$

$$
\beta^ {-} = \beta_ {1} ^ {-} + \beta_ {2} ^ {-} \times L g S a l e s _ {i, t - 1}.\tag{5}
$$

Please cite this article as: B. Gu, et al., The in<sup>fl</sup>uence of online word-of-mouth on long tail formation, Decision Support Systems (2012), http:// dx.doi.org/10.1016/j.dss.2012.11.004

Substitute Eqs. (4) and (5) into Eq. (3), we obtain:

$$
\begin{array}{r l} \Delta L g S a l e s _ {i t} & = \beta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} + \beta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} + \beta_ {2} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \\ & \times L g S a l e s _ {i, t - 1} + \beta_ {2} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g S a l e s _ {i, t - 1} \\ & + \gamma \Delta L g N u m O f R e v i e w s _ {i t} + \delta \Delta L g P r i c e _ {i t} + \gamma \Delta L g P r i c e _ {i t} \\ & + \eta \Delta X _ {i t} + \Delta v _ {t} + \epsilon_ {i t}. \end{array} \tag {6}
$$

In Eq. (6), the impact of WOM is able to vary with product popularity and review rating. H1a suggests that βþ be negative and $\beta _ { 2 } ^ { - }$ be positive because informational cascade theory suggests that positive reviews have more in<sup>fl</sup>uence on niche products and negative reviews have more in<sup>fl</sup>uence on popular products. H1b suggests the opposite: $\beta _ { 2 } ^ { + }$ be positive and $\beta _ { 2 } ^ { - }$ be negative because of the in<sup>fl</sup>uence of behavior heuristics.

## 4.3. Control variables

The in<sup>fl</sup>uence of WOM is not only affected by customer review ratings and product popularity but also by other factors. We consider the following variables that may moderate the in<sup>fl</sup>uence of WOM.

## 4.3.1. Review volume

Eq. (6) controls for the awareness effect by including changes in review volume as a control variable. The variable captures the underlying WOM diffusion process. Higher number of reviews suggests more interests from consumers to spread WOM and make others aware of the product. However, increased awareness does not necessarily lead to higher sales. In particular, the in<sup>fl</sup>uence may vary across products with different popularity. A consumer who becomes aware of a popular product is more likely to make a purchase than a consumer who becomes aware of an unpopular product [18]. We therefore add the interaction between changes in review volume and product popularity as a control variable.

$$
\begin{array}{r l} \Delta L g S a l e s _ {i t} & = \beta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} + \beta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} + \beta_ {2} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \\ & \times L g S a l e s _ {i, t - 1} + \beta_ {2} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g S a l e s _ {i, t - 1} \\ & + \gamma_ {1} \Delta L g N u m O f R e v i e w s _ {i t} + \gamma_ {2} \Delta N u m O f R e v i e w s _ {i t} \\ & \times L g S a l e s _ {i, t - 1} + \delta \Delta L g P r i c e _ {i t} + \Delta v _ {t} + \epsilon_ {i t}. \end{array} \tag {7}
$$

## 4.3.2. Product age

Product age could also have a signi<sup>fi</sup>cant moderating effect on the in<sup>fl</sup>uence of WOM. For newly released products, product awareness and knowledge are often generated by vendor marketing campaigns (e.g. newly released movies), news, and press reports (e.g. Apple iPhone). The presence of these alternative information sources reduces the in<sup>fl</sup>uence of WOM. On the other hand, marketing spending for and press interest in products that have been on the market for a long time is often limited. As a result, their sales become more dependent on WOM, which suggest that the in<sup>fl</sup>uence of WOM could increase with product age. To control for the moderating effect of product age, we add interactive terms between product age and WOM rating and WOM volume to Eq. (7).

$$
\begin{array}{r l} \Delta L g S a l e s _ {i t} & = \beta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} + \beta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} + \beta_ {2} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \\ & \times L g S a l e s _ {i, t - 1} + \beta_ {2} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g S a l e s _ {i, t - 1} \\ & + \gamma_ {1} \Delta L g N u m O f R e v i e w s _ {i t} + \gamma_ {2} \Delta L g N u m b e r o f R e v i e w s _ {i t} \\ & \times L g S a l e s _ {i, t - 1} + \theta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \times L g P r o d u c t A g e _ {i t} \\ & + \theta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g P r o d u c t A g e _ {i t} \\ & + \theta_ {2} \Delta L g N u m O f R e v i e w s _ {i t} \times L g P r o d u c t A g e _ {i t} + \delta \Delta L g P r i c e _ {i t} \\ & + \Delta v _ {t} + \epsilon_ {i t}. \end{array} \tag {8}
$$

## 4.3.3. Other control variables

Besides the control variables that moderate the in<sup>fl</sup>uence of WOM, we also add <sup>fi</sup>xed product effect to the <sup>fi</sup>rst difference model to allow different diffusion rates for different products [18]. Our <sup>fi</sup>nal model is as follows:

$$
\begin{array}{r l} \Delta L g S a l e s _ {i t} & = \beta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} + \beta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} + \beta_ {2} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \\ & \quad \times L g S a l e s _ {i, t - 1} + \beta_ {2} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g S a l e s _ {i, t - 1} + \gamma_ {1} \\ & \quad + \gamma_ {2} \Delta L g N u m O f R e v i e w s _ {i t} \times L g S a l e s _ {i, t - 1} + \theta_ {1} ^ {+} [ \Delta A v g R a t i n g _ {i t} ] ^ {+} \\ & \quad \times L g P r o d u c t A g e _ {i t} + \theta_ {1} ^ {-} [ \Delta A v g R a t i n g _ {i t} ] ^ {-} \times L g P r o d u c t A g e _ {i t} \\ & \quad + \theta_ {2} \Delta L g N u m O f R e v i e w s _ {i t} \times L g P r o d u c t A g e _ {i t} + \delta_ {1} \Delta L g P r i c e _ {i t} \\ & \quad + \Delta v _ {t} + \tau_ {i} + \epsilon_ {i t}. \end{array}\tag{9}
$$

## 5. Data

We collected books and user review data daily from Amazon.com using its Electronic Commerce Service (ECS) platform to form a panel data of 3000 books over 220 days. To ensure unbiased sampling, we <sup>fi</sup>rst collect ISBN numbers for all the books sold at Amazon. Amazon's ECS platform imposes a limit on the number of products returned for each query. To circumvent the limit, we leveraged the hierarchy of book categories. For instance, a book on baking bread is classi<sup>fi</sup>ed as follows:

Books > Subject > Cooking; Food & Wine > Baking > Cookies:

Each node in the hierarchy tree is attached with a unique browsing node number. We collected all the children nodes from each parent node recursively to establish the tree structure. We then obtained the list of all leaf nodes of books, attached corresponding ISBN numbers to these books, and deleted any duplications. This approach resulted in a total of over 3,700,000 unique books in a hierarchy tree with over 20,000 nodes. Among all these books, we drew a random sample of 3000 books for which we collected sales and review information on a daily basis.

The static information collected only once for each book includes ISBN, author, and release date. The dynamic information was collected daily for each book from September 2005 to April 2006 for 8 months. The daily information includes sales rank, Amazon price, and customer reviews (rating of each review and average rating for all reviews). We use sales volume to represent the popularity of a product. Amazon, however, only provides sales rank. Recent studies show that Amazon.com sales rank can be mapped into sales using a Pareto function [4,22,25]:

Sales = a × SalesRankb

<sub>ð</sub><sup>10</sup><sub>Þ</sub>

Log transformation of Eq. (10) suggests:

$$
L g S a l e s = l g (a) + b \times l g (S a l e s R a n k)\tag{11}
$$

and thus

$$
\Delta L g S a l e s = b \times \Delta l g (S a l e s R a n k).\tag{12}
$$

We use b=0.871 estimated by Brynjolfsson et al. [4] to calculate sales in this study. Tables 2, 3a, and 3b provide the description, summary statistics and correlations for the key variables used in our model.

## 6. Results

In order to compare our results with the results of previous studies, we <sup>fi</sup>rst present the regression results from the baseline <sup>fi</sup>rst-difference

Please cite this article as: B. Gu, et al., The in<sup>fl</sup>uence of online word-of-mouth on long tail formation, Decision Support Systems (2012), http:// dx.doi.org/10.1016/j.dss.2012.11.004

Table 4  
Table 2  
Description of key variables.

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td> $LgSales_{it}$ </td><td>Log value of the sales volume of book  $i$  at time  $t$ </td></tr><tr><td> $LgPrice_{it}$ </td><td>Log value of the price of book  $i$  at time  $t$ </td></tr><tr><td> $AvgRating_{it}$ </td><td>Average review rating for book  $i$  at time  $t$ </td></tr><tr><td> $[\Delta AvgRating_{it}]^{+a}$ </td><td>=  $\left\{ \begin{array}{c}\Delta AvgRating_{it},\text{ if } \Delta AvgRating_{it} > 0 \\ 0,\text{ otherwise}\end{array} \right.$ </td></tr><tr><td> $[\Delta AvgRating_{it}]^{-}$ </td><td>=  $\left\{ \begin{array}{c}\Delta AvgRating_{it},\text{ if } \Delta AvgRating_{it} < 0 \\ 0,\text{ otherwise}\end{array} \right.$ </td></tr><tr><td> $LgNumOfReviews_{it}$ </td><td>Log value of cumulative total number of reviews for book  $i$  at time  $t$ </td></tr><tr><td> $LgProductAge_{it}$ </td><td>Log value of product age of book  $i$  at time  $t$  measured in days</td></tr></table>

<sup>a</sup> ΔAvgRating <sup>þ</sup> measures the increase in average review rating for book i in period t, while ΔAvgRating <sup>−</sup> measures the decrease in average review rating for book i in period t.

model without the moderating effect (Eq. (2)) in Column 1 of Table 4. To control for possible autocorrelation and heteroscedesitity, we report Newey–West standard errors when applicable. The estimation of Eq. (2) suggests that the coef<sup>fi</sup>cients of the equation are the same as the traditional model used by prior studies, thus making it a good starting point for our analysis. The results show that an increase in review rating has a positive impact on incremental sales and the increase in the number of reviews also improves product sales. Both impacts are statistically signi<sup>fi</sup>cant. This result is consistent with the previous research, indicating that both average review rating and cumulative number of reviews positively affect the sales volume of the title and that price is negatively correlated with the sales.

Earlier WOM studies also show that negative WOM is more in<sup>fl</sup>uential than is positive WOM [9], indicating that the in<sup>fl</sup>uence WOM could vary across WOM valence. We validate this <sup>fi</sup>nding by splitting the variable for changes in average review rating (ΔAvgRating) into two variables, one for positive changes in average rating and the other for negative changes in average rating. The coef<sup>fi</sup>cient on the positive rating change variable indicates the magnitude of the in<sup>fl</sup>uence of positive WOM, while the coef<sup>fi</sup>cient on the negative rating change variable indicates the magnitude of the in<sup>fl</sup>uence of negative WOM. We reanalyze Eq. (2) with the new variables in Column 2 of Table 4. The result con<sup>fi</sup>rms that negative WOM signi<sup>fi</sup>cantly reduces product sales while positive WOM has little in<sup>fl</sup>uence, which is consistent with prior studies.

Our hypotheses are tested based on results in Table 5. column 1 of Table 5 reports the result from Eq. (6), which allows WOM in<sup>fl</sup>uence to vary with the interactions between product popularity and WOM rating and volume. Given the presence of interactive terms with product popularity, the coef<sup>fi</sup>cients on the direct effect of positive and negative WOM represent their in<sup>fl</sup>uences on the sales of the least popular products, while the coef<sup>fi</sup>cients on the interactive terms reveal how the in<sup>fl</sup>uence changes with product popularity. The four coef<sup>fi</sup>cients show that positive WOM has insigni<sup>fi</sup>cant in<sup>fl</sup>uence on the sales of unpopular products but the in<sup>fl</sup>uence of positive WOM increases significantly with product popularity. The result is exactly the opposite for negative WOM. Negative WOM hurts the sales of unpopular products, but the in<sup>fl</sup>uence decreases signi<sup>fi</sup>cantly with product popularity. In addition, the analysis reveals that the in<sup>fl</sup>uence of WOM volume on sales also increases with product popularity. The results provide strong support for predictions from behavior heuristics theory (H1b).

Table 3a  
Summary statistics for key variables

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td> $LgSales_{it}$ </td><td>0.902</td><td>1.553</td><td>-2.630</td><td>10.526</td></tr><tr><td> $LgPrice_{it}$ </td><td>2.704</td><td>0.625</td><td>0.693</td><td>5.700</td></tr><tr><td> $[\Delta AverageRating_{it}]^{+}$ </td><td>0.001</td><td>0.031</td><td>0</td><td>3.000</td></tr><tr><td> $[\Delta AverageRating_{it}]^{-}$ </td><td>-0.002</td><td>0.034</td><td>-2.500</td><td>0</td></tr><tr><td> $LgNumofReviews_{it}$ </td><td>0.921</td><td>2.103</td><td>-2.303</td><td>8.080</td></tr><tr><td> $LgProductAge_{it}$ </td><td>4.034</td><td>3.454</td><td>-6.908</td><td>10.222</td></tr></table>

Table 3b  
Correlations of key variables.

<table><tr><td>Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td> $LgSales_{it}$ </td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $LgPrice_{it}$ </td><td>-0.076</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td> $[ΔAverageRating_{it}]^{+}$ </td><td>0.027</td><td>-0.001</td><td>1</td><td></td><td></td><td></td></tr><tr><td> $[ΔAverageRating_{it}]^{-}$ </td><td>-0.035</td><td>0.000</td><td>0.002</td><td>1</td><td></td><td></td></tr><tr><td> $LgNumofReviews_{it}$ </td><td>0.434</td><td>-0.231</td><td>0.002</td><td>-0.005</td><td>1</td><td></td></tr><tr><td> $LgProductAge_{it}$ </td><td>0.041</td><td>-0.018</td><td>-0.010</td><td>0.007</td><td>0.185</td><td>1</td></tr></table>

To assess the robustness of the analysis, column 2 of Table 5 incorporates product age and the interactions between product age and WOM as control variables (Eq. (9)). These control variables allow the in<sup>fl</sup>uence of WOM to vary with product age. The result in column 2 shows that most coef<sup>fi</sup>cients on these control variables are insignificant and the coef<sup>fi</sup>cients on the interactions between WOM and product popularity remain unchanged.

The result that popular products bene<sup>fi</sup>t more from positive online reviews while niche products suffer more from negative reviews indicates that WOM helps consumers to converge to the most popular books and leads to a rich-get-richer situation. Therefore, our result shows that the informative effect of WOM curtails the formation of long tail. This conclusion is consistent with the prediction of behavior economics that suggests individuals make insuf<sup>fi</sup>cient adjustment when newly arrived information contradicts their prior beliefs. Our study also offers a possible explanation of the presence of superstar phenomenon identi<sup>fi</sup>ed in earlier long tail studies.

## 7. Discussion and conclusion

This paper provides a new perspective on how online information, speci<sup>fi</sup>cally online WOM, in<sup>fl</sup>uences the long tail phenomenon. Most prior studies focus on the awareness effect of online information and suggest that increasing awareness of niche products drives the long tail phenomenon. In this paper, we suggest that online information also in<sup>fl</sup>uences consumers' evaluation of product quality and this informative effect could have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on consumer purchase decisions. Our analysis reveals that consumers are more receptive to positive WOM on popular products and negative WOM on unpopular products. This disparity leads to a rich-get-richer situation, constraining the formation of the long-tail.

First difference model estimation of WOM in<sup>fl</sup>uence.

<table><tr><td></td><td>Model 1</td><td>Model 2</td></tr><tr><td> $\Delta LgPrice_{it}$ </td><td>-0.426 (0.078)***</td><td>-0.426 (0.078)***</td></tr><tr><td> $\Delta AvgRating_{it}$ </td><td>0.045 (0.020)**</td><td></td></tr><tr><td> $[ΔAvgRating_{it}]^{+}$ </td><td></td><td>0.014 (0.031)</td></tr><tr><td> $[ΔAvegRating_{it}]^{-}$ </td><td></td><td>0.071 (0.028)***</td></tr><tr><td> $ΔLnNumOfReviews_{it}$ </td><td>0.058 (0.019)***</td><td>0.066 (0.020)***</td></tr><tr><td>Product fixed effect</td><td>Included</td><td>Included</td></tr><tr><td>Time fixed effect</td><td>Included</td><td>Included</td></tr><tr><td>Autocorrelation parameter</td><td>-0.354 (0.002)***</td><td>-0.354 (0.002)***</td></tr><tr><td>R-square</td><td>12.666%</td><td>12.666%</td></tr><tr><td>Number of observations</td><td>506,051</td><td>506,051</td></tr><tr><td colspan="3">Newey-West standard errors are reported.</td></tr><tr><td colspan="3">*** p&lt;0.01.</td></tr><tr><td colspan="3">** p&lt;0.05.</td></tr><tr><td colspan="3">* p&lt;0.10.</td></tr></table>

Please cite this article as: B. Gu, et al., The in<sup>fl</sup>uence of online word-of-mouth on long tail formation, Decision Support Systems (2012), http:// dx.doi.org/10.1016/j.dss.2012.11.004

Table 5  
Decaying impact with moderating effect: how WOM affect long tail

<table><tr><td>Variables</td><td>Model 3</td><td>Model 4</td></tr><tr><td> $\Delta LgPrice_{it}$ </td><td>-0.424 (0.078)***</td><td>-0.424 (0.078)***</td></tr><tr><td> $[\Delta AvgRating_{it}]^{+}$ </td><td>-0.006 (0.031)</td><td>-0.025 (0.045)</td></tr><tr><td> $[\Delta AvgRating_{it}]^{-}$ </td><td>0.096 (0.040)***</td><td>0.106 (0.043)**</td></tr><tr><td> $[\Delta AvgRating_{it}]^{+} * LgSales_{i,t-1}$ </td><td>0.065 (0.014)***</td><td>0.067 (0.015)***</td></tr><tr><td> $[\Delta AvgRating_{it}]^{-} * LgSales_{i,t-1}$ </td><td>-0.029 (0.013)***</td><td>-0.029 (0.014)**</td></tr><tr><td> $[\Delta AvgRating_{it}]^{+} * LgProductAge_{it}$ </td><td></td><td>0.005 (0.009)</td></tr><tr><td> $[\Delta AvgRating_{it}]^{-} * LgProductAge_{it}$ </td><td></td><td>0.003 (0.008)</td></tr><tr><td> $\Delta LgNumOfReviews_{it}$ </td><td>0.111 (0.014)***</td><td>0.072 (0.032)***</td></tr><tr><td> $\Delta NumOReviews_{it} * LgSales_{i,t-1}$ </td><td>0.040 (0.020)***</td><td>0.044 (0.006)***</td></tr><tr><td> $\Delta NumOReviews_{it} * LgProductAge_{it}$ </td><td></td><td>0.011 (0.006)*</td></tr><tr><td>Product fixed effect</td><td>Included</td><td>Included</td></tr><tr><td>Time fixed effect</td><td>Included</td><td>Included</td></tr><tr><td>Autocorrelation parameter</td><td>-0.354 (0.002)***</td><td>-0.354 (0.002)***</td></tr><tr><td>R-square</td><td>12.680%</td><td>12.682%</td></tr><tr><td>Number of Observations</td><td>506,051</td><td>506,051</td></tr></table>

Newey–West standard errors are reported.  
⁎⁎⁎ pb0.01.  
\*\* $\mathrm { p } { < } 0 . 0 5 .$

While businesses is growing in their ability to use long tail strategies to sell a wider range of goods in smaller quantities [11], our <sup>fi</sup>ndings suggest that the increasing availability of online WOM is against the sales of niche products while supports the sales of popular products. This <sup>fi</sup>nding has important implications for product vendors and retailers. In particular, our <sup>fi</sup>nding suggests that vendors and retailers do not need to worry much about occasional negative reviews on popular products, but they need to take care of unsatis<sup>fi</sup>ed buyers of niche products as negative WOM is particularly damaging to niche products. At the same time, our <sup>fi</sup>nding suggests that it is important for product vendors and retailers to attract positive reviews on popular products as such reviews can further enhanced their sales. Our <sup>fi</sup>ndings also indicate the importance of consumers' initial expectations and the dif<sup>fi</sup>culty of changing consumers' beliefs once expectations have been set. Business can leverage this behavior bias to develop better marketing strategies on advertising, promotion, and customer relationship management. One important implication, for instance, is that existing customers are more tolerant of negative reviews than new customers and thus making new customers satis<sup>fi</sup>ed is essential for business growth.

This study is the <sup>fi</sup>rst to analyze the in<sup>fl</sup>uence of online WOM using behavior heuristics. Most prior studies ignore consumer behavior that may affect the way expectations are formed and decisions are made. Different from the economic assumption that consumers are perfectly rational, behavior heuristics theories suggest that consumers are biased toward their initial expectation when making decisions heuristically. This bias serves as an underlying mechanism driving the in<sup>fl</sup>uence of online WOM on product sales. Extending existing research on WOM, we use the <sup>fi</sup>rst difference approach to provide more <sup>fl</sup>exibility in modeling the impact of WOM on product sales. Our approach focuses on the in<sup>fl</sup>uence of newly generated WOM and allows the in<sup>fl</sup>uence to vary with the interaction between WOM and product popularity. The <sup>fi</sup>ndings provide a more re<sup>fi</sup>ned understanding of the WOM effect.

This study also has some limitations. First, while we develop our hypotheses based on behavior heuristics theory and show that our result is consistent with its prediction, we do not survey consumers for their underlying motivations and there may exist alternative explanations for consumers' biased responses to WOM. Future studies could bene<sup>fi</sup>t from a combination of secondary data from consumer survey to take a more in-depth look at the phenomenon. Second, our analysis focuses on the informative effect of WOM. In reality, WOM in<sup>fl</sup>uences the long tail phenomenon in multiple ways. Notably, Dellarocas and Narayan [14] suggest that consumers are much more likely to discuss popular products, implying that the awareness effect of WOM also favors popular products. Future studies can bene<sup>fi</sup>t from combining multiple effects of WOM and providing a more comprehensive modeling of the in<sup>fl</sup>uence of WOM on the long tail formation. This paper also bears several limitations in the data collection. The data are solely collected from Amazon.com. In future research, using data sets from multiple online retailers can help generalize our research on WOM effects and the long tail phenomenon. In addition, information provision and website design could also have signi<sup>fi</sup>cant impacts on WOM effect and the formation of the long tail. We leave those concerns for future investigation.

## Acknowledgements

The authors would like to thank Xin Zhao for his work on on earlier versions of this paper and participants at the 2008 Conference on Information Systems and Technology (CIST 2008) and the 5th Symposium on Statistical Challenges in Electronic Commerce Research (SCECR 2009) for their valuable feedback.

## References

[1] C. Anderson, The long tail, Wired 12 (10) (2004) 170–177.

[2] S. Basuroy, S.S. Chatterjee, A. Ravid, How critical are critical reviews? The box of<sup>fi</sup>ce effects of <sup>fi</sup>lm critics, star power, and budgets, The Journal of Marketing 67 (4) (2003) 103–117.

[3] S. Bikhchandani, D. Hirshleifer, I. Welch, A theory of fads, fashion, custom, and cultural change as informational cascades, Journal of Political Economy 100 (5) (1992) 992–1026.

[4] E. Brynjolfsson, M.D. Smith, Y.J. Hu, Consumption surplus in the digital economy: estimating the value of increased product variety at online booksellers, Management Science 49 (2003) 1563–1579.

[5] E. Brynjolfsson, M.D. Smith, Y.J. Hu, From niches to riches: anatomy of the long tail, Sloan Management Review 47 (4) (2006) 67–71.

[6] E. Brynjolfsson, M.D. Smith, Y.J. Hu, Goodbye pareto principle, hello long tail: the effect of search costs on the concentration of product sales, in: MIT working paper, 2007.

[7] P.Y. Chen, S. Dhanasobhon, M.D. Smith, All reviews are not created equal: the disaggregate impact of reviews and reviewers at Amazon.com, in: Paper, 55, Heinz Research, 2001, (Available at http://repository.cmu.edu/heinzworks/55).

[8] Y. Chen, S. Fay, Q. Wang, Marketing implications of online consumer product reviews, in: University of Florida Working Paper, 2003.

[9] J. Chevalier, D. Mayzlin, The effect of word of mouth on sales: online book reviews Journal of Marketing Research 43 (2006) 345–354

[10] P.K. Chintagunta, S. Gopinath, S. Venkataraman, The effects of online user reviews on movie box of<sup>fi</sup>ce performance: accounting for sequential rollout and aggregation across local markets, Marketing Science 29 (5) (2010) 944–957

[11] E.K. Clemons, P.F. Nunes, Carrying your long tail: delighting your consumers and managing your operations, Decision Support Systems 51 (4) (2011) 884–893.

[12] E.K. Clemons, G. Gao, L. Hitt, When online reviews meet hyperdifferentiation: a study of the craft beer industry, Journal of Management Information Systems 23 (2) (2006) 149–171.

[13] C. Dellarocas, N.F. Awad, X. Zhang, Exploring the value of online product reviews in forecasting sales: the case of motion pictures, Journal of Interactive Marketing 21 (4) (2007) 23–45.

[14] C. Dellarocas, G. Gao, R. Naraya, Are consumers more likely to contribute online reviews for hit or niche products? Journal of Management Information Systems 27 (2) (2010) 127–158.

[15] S. Dewan, J. Ramaprasad, Impact of blogging on music sales: the long tail effect, in: Working paper, 2007.

[16] T. Dierkes, M. Bichler, R. Krishnan, Estimating the effect of word of mouth on churn and cross-buying in the mobile phone market with Markov logic networks, Decision Support Systems 51 (3) (2011) 361–371.

[17] W. Duan, B. Gu, A.B. Whinston, The dynamics of online word-of-mouth and product sales — an empirical investigation of the movie industry, Journal of Retailing 84 (2) (2008) 233–242.

[18] W. Duan, B. Gu, A.B. Whinston, Information cascades and software adoption on the internet: an empirical investigation, MIS Quarterly 33 (1) (2009) 23–48.

[19] Elberse, F. Oberholzer-Gee, Superstars and underdogs: an examination of the long tail phenomenon in video sales, in: Harvard Business School Working Paper Series, 07-015 2007

[20] J. Eliashberg, S.M. Shugan, Film critics: in<sup>fl</sup>uencers or predictors? The Journal of Marketing 61 (2) (1997) 68–78.

[21] D. Fleder, K. Hosanagar, Blockbuster culture's next rise or fall: the impact of recommender systems on sales diversity, in: Net Institute Working Paper, 2008.

[22] A. Ghose, M.D. Smith, R. Telang, Internet exchanges for used books: an empirical analysis of product cannibalization and welfare, Information Systems Research 17 (1) (2006) 3–19.

[23] D. Godes, D. Mayzlin, Using online conversations to study word-of-mouth communication, Marketing Science 23 (24) (2004) 545–560

[24] K.H. Goh, J. Bockstedt, Unbundling and the long tail: new evidence on the consumption of information goods in: Working Papaer, 2008.

Please cite this article as: B. Gu, et al., The in<sup>fl</sup>uence of online word-of-mouth on long tail formation, Decision Support Systems (2012), http:// dx.doi.org/10.1016/j.dss.2012.11.004

[25] Goolsbee, J. Chevalier, Measuring prices and price competition online: amazon.com and barnesandnoble.com, Quantitative Marketing and Economics 1 (2) (2003) 203–222.

[26] D. Grif<sup>fi</sup>n, A. Tversky, The weighing of evidence and the determinants of con<sup>fi</sup>dence, Cognitive Psychology 24 (1992) 411–435.

[27] B. Gu, J. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales of high-involvement products, Information Systems Research 23 (1) (2012) 182–196.

[28] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4–21.

[29] A. Hervas-Drane, Word of mouth and recommender systems: a theory of the long tail, in: Working Paper, 2008.

[30] N. Hu, L. Liu, J.J. Zhang, Do online reviews affect product sales? The role of reviewer characteristics and temporal effects, Information Technology and Management 9 (3) (2008) 201–214

[31] Y. Liu, Word of mouth for movies: its dynamics and impact on box of<sup>fi</sup>ce revenue The Journal of Marketing 70 (2006) 74–89.

[32] W.W. Moe, M. Trusov, The value of social dynamics in online product ratings forums, Journal of Marketing Research 48 (3) (2011) 444–456.

[33] S. Moon, P.K. Bergey, D. Iacobucci, Dynamic effects among movie ratings, movie revenues, and viewer satisfaction, The Journal of Marketing 74 (1) (2010) 108–121.

[34] G. Oestreicher-Singer, A. Sundararajan, Network structure and the long tail of electronic commerce, in: Working Paper, Stern School of Business, New York University, 2006.

[35] M. Rabin, J.L. Schrag, First impressions matter: a model of con<sup>fi</sup>rmatory bias, Quarterly Journal of Economics 114 (1) (1999) 37–82.

[36] M. Sun, The informational role of consumer disagreement, in: Working paper, 2008.

[37] M. Sun, How does variance of product ratings matter? Management Science 58 (4) (2012) 696–707.

[38] C. Tucker, J. Zhang, How does popularity information affect choices? A <sup>fi</sup>eld experiment, Management Science 57 (5) (2011) 828–842.

[39] Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185 (1974) 1124–1131.

[40] M. Wimble, J. Tripp, B. Phillips, B. Sambamurthy, The moderating role of search costs on long tail, in: Fifth Symposium on Statistical Challenges in Electronic Commerce Research, Pittsburgh, PA, 2009.

[41] X. Zhang, C. Dellarocas, N.F. Awad, The impact of online movie reviews on box of-<sup>fi</sup>ce performance, in: Workshop on Information Systems and Economics (WISE), 2004.

[42] F. Zhu, X. Zhang, Impact of online consumer reviews on sales: the moderating role of product and consumer characteristics, The Journal of Marketing 74 (2) (2010) 133–148.

![](/api/attachments/3ZR3S7YR/fulltext/images/04b1a6114c97cac79e4abceda4070adb8f853630d6df2759b7b9e093cea02adc.jpg)

![](/api/attachments/3ZR3S7YR/fulltext/images/8ff7498cddaa689f17cf5d8dd8c26c9eadd7e2b42435c1a9bc4b0ab8b33af92d.jpg)

![](/api/attachments/3ZR3S7YR/fulltext/images/68b22020b23bdf93300d857d3daa36f24011158b7242b18441789624c43b9ff2.jpg)

Dr. Bin Gu is an associate professor at the W. P. Carey School of Business, Arizona State University. He received his Ph.D. from the Wharton School, University of Pennsylvania. His research focuses on electronic commerce, online social networks, information economics and IT strategy. His work has appeared in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of Retailing, Decision Support Systems and others. Bin's research won the 2012 Emerald Citations of Excellence Award, the 2008 ISR Best Published Paper Award and the Best Paper-in-Track Award of the 2007 International Conference on Information Systems (ICIS).

Ms. Qian Tang is a Ph.D. candidate in the Information, Risk, and Operations Management Department of McCombs School of Business at the University of Texas at Austin. She expects to receive her Ph.D. in 2013. Her research interests include electronic commerce, economics of information systems, social media, online Word of Mouth, reputation, and internet security. Her current research focuses on the issue in social media and internet security.

Dr. Andrew B. Whinston received his Ph.D. at Carnegie Mellon University and is currently a professor at The University of Texas at Austin where he holds the Hugh Roy Cullen Centennial Chair in Business Administration. He is also the director of the Center for Research in Electronic Commerce. He has published extensively on resource allocation issues and is currently working on Internet security He has completed numerous research projects that investigate economics, internet technology, and operations research in the study of information systems issues. In 2011, he was rated as the most in<sup>fl</sup>uential scholar in the Information Systems <sup>fi</sup>eld by the h-index which measures scholarly in<sup>fl</sup>uence.
