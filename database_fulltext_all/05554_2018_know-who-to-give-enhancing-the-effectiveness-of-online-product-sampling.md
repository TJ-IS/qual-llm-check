---
otero_id: 5554
otero_key: "G8ZDA392"
title: "Know who to give: Enhancing the effectiveness of online product sampling"
authors: "Xianghua Lu; Chee Wei Phang; Sulin Ba; Xinlin Yao"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.11.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Know who to give: Enhancing the effectiveness of online product sampling☆

Xianghua Lu <sup>a</sup>, Chee Wei Phang <sup>a,</sup>⁎, Sulin Ba <sup>b</sup>, Xinlin Yao <sup>a</sup>

<sup>a</sup> School of Management, Fudan University, Shanghai, China, 200433

<sup>b</sup> School of Business, University of Connecticut, Storrs, CT, USA

## a r t i c l e i n f o

Article history: Received 21 February 2017 Received in revised form 7 November 2017 Accepted 12 November 2017 Available online 20 November 2017

Keywords: Product sampling Consumer heterogeneity Latent class modeling E-commerce Brand sales

## a b s t r a c t

Product sampling is an established marketing strategy to increase product exposure and sales, and its use has recently been extended online. Online product sampling affords the advantages of reaching mass audiences, as well as opportunities for firms to select promising sample recipients. In this study, we leverage on the data from an online platform's early effort in administering online product sampling campaigns, whereby sample recipients were randomly selected from among the consumers who indicated interest in the product sample. This affords a relatively “clean” environment for us to investigate the behaviors of consumers in terms of their subsequent purchase-making after being given a product sample, with minimal biases arising from purposive selection issues. We find that, overall, receiving a product sample could increase the consumers' purchase probability by around 300%. Furthermore, the effects vary among different type of consumers. Specifically, average consumers who have few or moderate experience on the platform demonstrated highest purchase probability compared to mature shoppers and also “opportunists”, after they received a product sample. This study contributes to the literature by unveiling consumer heterogeneity in response to online product sampling when receiving a sample, and provides guidance to firms' decision-making in targeting potential consumers so as to better economize on these campaigns.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Product sampling is a widely employed marketing strategy for a variety of physical products such as food and beverages, cosmetics, housewares, and personal care products. A sampling campaign allows consumers to experience the product first-hand thus reducing uncertainty associated with the product, and has been shown to be effective in promoting the sales of the product [1–4] as well as the brand concerned<sup>1</sup> [5]. With the burgeoning of e-commerce, product sampling is being increasingly administered online. For example, Pinchme.com in the U.S., gotry.in in India, and try.taobao.com and Yihaodian.com in China, allow brands to offer product samples to their consumers online.

With product sampling moved online, the cost of administration becomes lower and the scale of reach greatly increases. A typical online sampling campaign usually involves three steps: (1) brands post a free sample offer on an online platform, displaying pictures and information of the product concerned; (2) whoever visits the platform and see the offer may apply for the sample and provide their information (e.g., shipping address) before the offer expires; (3) the platform (or the brand) selects the applicants and sends out the sample. This process affords opportunities to select more promising sample recipients from among the applicants, e.g., those who may be more likely to make subsequent purchases after receiving the product sample.

However, our understanding of how the selection should be made to enhance the effectiveness of online product sampling is currently lacking owing to at least two reasons. First, previous literature on product sampling in the offline context offers limited insights into this issue as they mostly employed aggregate data in their investigation due likely to data constraints in this context (e.g., [1–3,5,6]). Specifically, they can only focus on whether product sampling increases overall sales, without being able to take into account who among those receiving a product sample contributed to the sales and their characteristics. Second, strategic selection choices are likely made by existing platforms or brands administering the product sampling campaigns [2], e.g., giving product samples mostly to innovators or loyal/frequent consumers. This makes it difficult to truly discern what kinds of consumers are indeed more (or less) profitable to be selected as sample recipients.

In this study, we collaborated with a leading e-commerce platform in China, and tapped into the unique opportunity that they just started their online product sampling section. During this initial period, they decided to rely on random drawing to give out product samples as they hope to gain more systematic knowledge of selecting recipients based on consumer behavioral data collected at this stage. The random drawing approach implies that the sample recipients are likely to come from heterogeneous backgrounds in the absence of specific selection criteria, which affords a relatively “clean” setting for us to analyze what kinds of consumers are more/less promising for giving out the product samples. For instance, if the selected recipients consist mainly of loyal consumers, this would preclude the possibilities of identifying other profitable consumer segments, as well as those less promising ones who should not be selected. Our dataset collected during this period involved N100,000 sample applicants who applied for 401 product samples. The e-commerce platform also allowed us to track the consumers' ex-post purchase behavior (anonymized) for two months after the sampling campaigns.

We developed a Probit binary choice model to test the effects of product sample's application outcomes on applicants' purchase behavior. A Latent Class Model (LCM) is further utilized to ex-post identify distinct consumer segments that demonstrate different post-sampling purchase behaviors, which can be used to support subsequent target strategy of online product sampling. LCM is an approach that identifies latent subgroups, or patterns across individuals from a population, based on observed variables (e.g., individual characteristics) that explain the unobserved heterogeneity within the phenomenon of interest (post-sampling purchase in this case) ([7–9]).

The results indicate that the receipt of product sample could overall increase the brand purchase probability by around 300%. Based on the LCM analysis, it is further unveiled that there are three subgroups of consumers that emerge from the sample applicants: 1) average consumers who have moderate experience on the e-commerce platform, and tended to apply for the samples less frequently (54.68% of the sample); 2) seasoned consumers on the platform with rich shopping experience, and who are less likely to respond to the marketing activity (30.75% of the sample); 3) opportunistic consumers who are keen on applying for product samples, yet their ex-post purchase level was very low (14.58% of the sample). Taken together, our results, as will be explained in greater details later, suggest that the third group of consumers appear less profitable and constitutes those whom marketers should avoid, while the first and second groups are those whom marketers may want to pay more attention to.

The findings from our research may contribute to the literature in the following ways. First, our research demonstrates how individual consumers' purchase behavior is affected by whether their application for a product sample is successful or unsuccessful. While the positive effect of receiving a product sample is important to understand, there is a need to also account for the negative repercussions from consumers who indicate an interest in a product sample yet are denied access to it. By taking these consumers into consideration, our study offers a more complete understanding of the effects of product sampling, afforded by our dataset from the online product sampling context that captured consumer purchase behavior at the individual level. This is in contrast to previous literature that mostly relied on aggregate data, and focused on whether product sampling increases consumer purchase as a whole without examining whom among the consumers contributed more/less to the purchase (e.g., [1–3,5,6]).

Second, we unveil the major types of consumer characteristics and show which of them are more and less profitable as sample recipients in terms of their likelihood of subsequent purchase-making. Specifically, three types of consumers each with their distinct characteristics emerge from the LCM analysis. These insights are enabled by our unique dataset, which was collected from a period during which our corporate partner just started their online product sampling section and selected sample recipients using a random drawing rather than a purposive selection approach. The generated insights enhance our understanding of the characteristics of consumers to whom the offering of product samples is particularly effective (or ineffective), and help marketers and brands in targeting more profitable consumers in giving out product samples in their future campaigns.

In the following sections, we begin by discussing the conceptual background of this study.

## 2. Conceptual background

## 2.1. The online product sampling context

With online product sampling becoming a popular marketing strategy, there has been an increasing number of online platforms that engage in administering sampling campaigns. Among them, some platforms just provide sample delivery service (e.g., Pinchme.com), while consumers cannot purchase the sampled products on the platform. Others operate as an e-commerce marketplace with online sampling offered (e.g., try.taobao.com). Consumers can directly make purchase online if they are interested in the products offered for sampling. In this study, we focus on the latter type of online platforms, i.e., online shopping platforms with product sampling offered whereby consumers can make purchase of the products concerned. While these platforms are somewhat similar with offline markets where consumers can try out a product before making a purchase, the online platforms are advantageous in that firms can track each consumer's shopping behavior after the sampling, and more importantly identify profitable consumers to better economize on their product sampling campaigns.

It is also important to note that our focal context of online product sampling involves physical products, and differs from the sampling of digital goods such as music and software that have been more widely investigated in the extant literature [6,10–12]. Unlike digital products that can be easily copied and distributed, the sampling of physical products usually involves the delivery of full-sized products of some monetary value to a physical address. This makes the sampling of physical products attractive to the consumers, and also increases the likelihood that consumers may feel obliged to purchase such products after receiving the sample due to feelings such as gratitude and reciprocity [5,13,14].

## 2.2. Research on physical product sampling

Little research has investigated the effectiveness of online physical product sampling campaigns. Among the few exceptions, Hui et al. [15] conducted a survey to examine consumers' willingness to participate in and their satisfaction with online product sampling in New Zealand, but the insights offered by their study are limited by individuals' self-reported data. Given the growing popularity of online physical product sampling campaigns, the existing research is far from adequate. Therefore, our paper aims to quantify the impact of online product sampling success on individual consumers' purchase behavior, with a view to unveil heterogeneity in the consumers through the LCM technique.

Research on physical product sampling in the offline context may provide some insights. Specifically, several explanations have been offered with regard to why physical product sampling could be effective. For instance, offering free product samples has been noted to reduce product uncertainty for consumers by serving as a direct source of information, thereby leading to a greater effect on sales compared to indirect experiences provided through advertising [16]. This may be particularly valuable for physical products, of which many of their features can only be conveyed via sampling experience [16–18]. For most consumers, free sampling provides their first usage experience with a brand, and may thus become a critical factor in determining their brand beliefs and purchase intentions [19,20].

Apart from uncertainty reduction, product sampling may also influence consumer purchase via a self-perception shaping mechanism [21–

23]. In a sampling campaign, consumers who are open to receiving a sample may go through a process of forming self-perception, as someone who is interested in trying out and subsequently using the product [3,24]. This increases the likelihood of them purchasing the product when opportunity arises in future.

In addition, the sampling campaign itself may also channel its effects to other consumers, besides the impacts on consumers who sampled a product. As Wright and Lynch [20] propose, offering product samples signals a brand's confidence in its product quality. In other words, even if consumers cannot obtain the free samples, they may infer from the sampling campaign that the brand involved is of high quality.

Nevertheless, there could be potential negative effects of product sampling as well. Specifically, the trial experience provided by a product sample may not always be positive; in the event of a negative disconfirmation, i.e., the trial experience does not meet ones' expectation, it could result in consumers' poor attitude towards the product and thus undermine their intention to purchase it subsequently. This is especially true when consumers are exposed to ads containing exaggerated claims about the product prior to sampling it, as previous research shows [25]. Thus, brands should be careful in exposing consumers to appropriate ad claims prior to their product sampling campaign, so as to set consumer expectation right, and more fundamentally, offering their high-quality products for sampling.

In general, however, most of the prior literature have indicated a positive effect of physical product sampling on sales (e.g., [1–3,5,6]). Yet, they have mostly investigated the sales effect of product sampling at an aggregated level, which does not lend itself to uncovering consumer heterogeneity and their different responses to online product sampling.

## 2.3. Research on consumer heterogeneity and online product sampling

As previous marketing research suggests, consumer responses to marketing campaigns are tied to individual factors, such as motivations, demographics, and purchase experiences [26–30]. An understanding of such individual factors could help marketers in targeting the more profitable consumers to better economize on their online physical product sampling campaigns.

For example, the motives of consumers applying for a product sample could directly affect their attitudes towards the application results. If their application for a product sample is driven by a need to seek information about the sampled product or brand, sample applicants may only apply for the product sample they are interested in. If they did receive the sample, they are more likely to test the product quality seriously for subsequent purchase considerations, and eventually buy more if they are satisfied with the products sampled. In contrast, for consumers who just want to seek gratification, they may treat the applications of a product sample merely as gambling for “free gift” [31–33], and care less about the sampled product per se. The low cost of online sample application also allows them to apply multiple times without incurring much cost. For this type of consumers, their purchase behavior may be less affected by the application outcomes.

Purchase experience may be another important factor that could affect consumers' responses to marketing activities [27,29]. As indicated in Moschis and Moore [28], younger consumers tend to respond more positively to television advertising than do their older counterparts, because they have less purchase experience. In the context of online shopping, seasoned shoppers, given their greater exposure to and experiences with marketing activities, are likely to be less affected by these campaigns. If they receive a product sample, they may treat it as just “another” promotion. As a result, they may feel less indebted to the receipt of a product sample compared to novice shoppers. For shoppers who have less experience, they may respond more favorably to online sampling campaigns because upon the receipt of a product sample, their indebted feeling is stronger, and thus has a greater tendency to purchase the product in future.

In this study, we empirically explore how the sample application results affect applicants' purchase behavior in random drawing-based product sampling, and how the impacts vary according to consumer characteristics.

## 3. Data

## 3.1. Research context

We obtain the data of online physical product sampling and consumers' purchase behavior from a leading e-commerce platform in China. The e-commerce platform sells a variety of physical products, ranging from grocery and household products, clothing, electrical appliances, toys, to cosmetic and healthcare products. In October 2012, the platform launched an online product sampling section, which allows firms to offer free product samples to the platform users. A sampling campaign typically runs for one week, during which consumers need to submit an application for a product sample with their shipping information. The sample would be mailed to the successful applicants after the campaign ended. We collected the data during the initial implementation of the online product sampling section. During that period, recipients of the samples were selected randomly.<sup>2</sup> Based on the random drawing assignments, we are able to assess the effects of receiving/not receiving a product sample on individuals' subsequent purchase behavior, and the major subgroups and their characteristics.

As shown in Fig. 1, the platform creates a unique webpage for each sampling product to display the campaign information (e.g., sample quantity and the current number of sample applicants), brand information, application button, and a purchase link.

## 3.2. Descriptive analysis

Our study covers the applicants' purchase behavior of all the 401 products that offered free samples from October 2012 to August 2013. During this period, a total of 122,003 consumers applied for product samples on the online platform. On average, each consumer applied for 2.3 samples. Therefore, our final study sample includes 284,252 cross-sectional observations organized by applicant id and product id. We collected consumers' brand purchase information within two months after the end of each sampling campaign.<sup>3</sup> For example, if a sample application ends on Jan 1st 2013, we collected all its applicants' purchase behavior from Jan 1st to Mar 1st. We also collected consumers' purchase amount information on the whole platform two months before the application. The main variables of this study are defined and described in Table 1 below.

As Table 1 shows, the average price of the products with a sample offer was RMB 285 (approximately USD 42). Among them, 42% were new products that had never been sold on the platform before (IS\_PNew), and 55% were fast-moving consumer goods (PFMCG). FMCG products are defined as products that are sold quickly at a relatively low cost. We include this variable because we believe the purchase behavior of FMCG and durable goods or large appliances could be different. The brand awareness of products could also impact the purchase, thus we also try to control this effect by coding the quantity of news information about a brand using Baidu.com (the leading search engine in China) during the observation period. In addition, we collected the average rating of each product on the focal platform to control for the impacts of WOM on purchase.

![](/api/attachments/G8ZDA392/fulltext/images/e115bf5976b7a22705ea61a1e8a6b7aa3031615dd29dede174c3904209195950.jpg)  
Fig. 1. Example webpage of product sampling campaign

We calculated applicants' sample-receiving and purchase behavior based on each application. On average, 3% of the applicants successfully received a product sample. 7% of the applicants would purchase products from the sampling brand; however, the purchase ratio of the sampled products was only 1%. It needs to be noted that in this study we are more interested in the applicants' purchase behavior involving the sampled product's brand rather than the sampled product per se. There are several reasons for this choice: (1) sampled products usually belong to a product series. For example, a sampled product offered by a brand may be a diaper of a certain size. Consumers may not buy the diaper of the particular size again after sampling; instead they may choose diapers of other sizes from the same brand. Previous studies on product sampling [1–3] also used the sales of brands rather than of products as the focal outcome; (2) in our research context, the platform is designed to encourage consumers to buy more products from a brand by including a highlighted “brand link” at the right side of the sampling page (see Fig. 1). A large number (44.8%) of visitors were found to click on this link when they were viewing the sampling page and might buy the products of this brand; (3) related to the previous point, prior research suggests that consumers form brand perceptions after they have tried out a product from a brand, and tend to extend the perceptions to other products offered by the brand [34–36]. In addition, consumers may use the product attributes (e.g., price, rating) to infer the brand's other products and make purchase decision on those products [37].

For instance, the price and rating of a product bought may be used to infer the quality of other products offered by the same brand; 4) from the brands' perspective, they are not only interested in the sales of the sampled products, but also the value of the cross sales stimulated by their sampling campaign. Thus, the use of brand purchase as the dependent variable is deemed reasonable.

While the sample applicants applied for 2.3 samples on average, the maximum number is 391, indicating that some applicants were quite active in applying for product samples. Also the application number was not normally distributed. Around 73.6% of applicants applied for product samples only once. In addition, the average tenure of the applicants on this platform (duration) was 458 days. We also coded applicants' geographical addresses based on their city of residence with four dummy variables, ranging from 1 to 4 to correspond to large to small cities/towns (1 being the largest cities such as Beijing and Shanghai; 2 representing big cities such as the capital of each province; 4 being a rural area of China including small towns or villages, while the rest of the medium and small cities were represented by 3, with a mean of 2.01 (i.e., most of the consumers live in medium and big cities)).

We compared the brand purchase rate between recipients and nonrecipients of product samples at consumer per product level. The result shows that the sample recipients overall made more brand purchases than non-recipients at consumer-product level (19.6% vs. 6.38%), which is around a 307.8% increase. We also measured the purchase rate at consumer level. If consumers applied more than one products, we aggregate their purchases at consumer level. The third row of Table 2 suggests that the purchase ratio of these consumers is 50.1%, which is also around 317% higher than those who did not receive any sample. We also compared the difference in purchase frequency (how many times consumers ever bought this brand) between the two groups. We could learn that at both the consumer-product and consumer levels, the purchase frequencies of those who received a sample (1.059 and 6.025 respectively) were again much higher than that of those who did not received a sample (0.126 and 0.172 respectively).

Table 1  
Variable definition and summary statistics.

<table><tr><td>Variable</td><td>Definition</td><td>Mean</td><td>SD.</td><td>Min.</td><td>Max.</td></tr><tr><td colspan="6">Product characteristics</td></tr><tr><td> $PPrice_j$ </td><td>Price of  $product_j$ </td><td>285.082</td><td>582.507</td><td>9.9</td><td>5000</td></tr><tr><td> $PFMCG_j$ </td><td>Is  $product_j$  a Fast Moving Consumer Goods</td><td>0.549</td><td>0.498</td><td>0</td><td>1</td></tr><tr><td> $IS_PNew_j$ </td><td>Is the  $product_j$  a new product on this platform</td><td>0.419</td><td>0.493</td><td>0</td><td>1</td></tr><tr><td> $Avg\_rating_j$ </td><td>The average rating of  $product_j$  on this platform during the observation period.</td><td>4.685</td><td>0.268</td><td>1.5</td><td>5</td></tr><tr><td> $Num\_news_j$ </td><td>Quantity of news information concerning a brand, collected from Baidu.com (the leading search engine in China) during the observation period</td><td>293.45</td><td>1154.21</td><td>0</td><td>13,600</td></tr><tr><td colspan="6">Applicant characteristics</td></tr><tr><td> $CCity_i$ </td><td>City dummy of  $consumer_{i}$ ; 1–4 indicate large to small cities (1 being the largest and 4 being the smallest)</td><td>2.006</td><td>1.166</td><td>1</td><td>4</td></tr><tr><td> $CDuration_i$ </td><td>The duration of  $consumer_i$  on the platform as a consumer, as of August 23, 2013</td><td>458.318</td><td>333.41</td><td>7.982</td><td>1868</td></tr><tr><td> $CTappliednum_i$ </td><td>The total number of sample applications</td><td>38.984</td><td>81.247</td><td>1</td><td>391</td></tr><tr><td> $CLavel_i$ </td><td>The membership level of the consumer, computed by the platform mainly based on purchase amount</td><td>10.499</td><td>5.765</td><td>0</td><td>20</td></tr><tr><td colspan="6">Application characteristics</td></tr><tr><td> $Buy\_Brand_{ij}$ </td><td>Did  $consumer_i$  buy  $product_j$ &#x27;s brand after the application</td><td>0.07</td><td>0.25</td><td>0</td><td>1</td></tr><tr><td> $Buy\_Product_{ij}$ </td><td>Did  $consumer_i$  buy  $product_j$  after the application</td><td>0.01</td><td>0.10</td><td>0</td><td>1</td></tr><tr><td> $Sample\_Received_{ij}$ </td><td>Did  $consumer_i$  receive the sample of  $product_j$ </td><td>0.03</td><td>0.18</td><td>0</td><td>1</td></tr><tr><td> $Appliednum_{ij}$ </td><td>The number of times  $consumer_i$  applied for other products prior to applying for product j.</td><td>15.717</td><td>41.159</td><td>0</td><td>390</td></tr><tr><td> $B\_2Mamount_{ij}$ </td><td>The purchase amount of  $consumer_i$  in the last two months before this application</td><td>619.720</td><td>1113.586</td><td>0</td><td>29,863.62</td></tr></table>

Purchase rate comparison between recipients and non-recipients.

<table><tr><td></td><td>Recipients</td><td>Non-recipients</td></tr><tr><td colspan="3">Panel A: Purchase rate</td></tr><tr><td>Consumer-product level</td><td>0.196(0.398)307.8%</td><td>0.0638(0.244)100%</td></tr><tr><td>Consumer level</td><td>0.501(0.500)317.1%</td><td>0.158(0.364)100%</td></tr><tr><td colspan="3">Panel B: Purchase frequency</td></tr><tr><td>Consumer-product level</td><td>1.059(6.377)840.5%</td><td>0.126(0.704)100%</td></tr><tr><td>Consumer level</td><td>6.025(49.197)3502.9%</td><td>0.172(0.423)100%</td></tr></table>

Note: Standard deviations are in parentheses.

## 4. Econometric model

We model consumers' brand purchase behavior as being influenced by sampling campaigns after controlling the impacts of products characteristics and applicants' characteristics.

## 4.1. Latent class model

We use a Probit model to capture the brand purchase binary response (i.e., buy or not) within two months after the sampling campaign. Specifically, for a consumer i who applied for a sample of a product j, we use Buy\_Bran $d _ { i j }$ to denote the consumers' binary response and $u _ { i j }$ to denote the latent utility. Therefore, $y _ { i j }$ is defined as

$$
y _ {i j} = B u y \_ B r a n d _ {i j} = \left\{ \begin{array}{l l} 1, & \text { if } u _ {i j} > 0 \\ 0, & \text { if } u _ {i j} \leq 0 \end{array} \right.\tag{1}
$$

We specify consumers i's latent utility of purchasing brand of sampled product j as dependent on the consumer's characteristics and other factors as follows. Our focal variable is Sample\_Received , i.e. consumer i received the sample of product j or not. $X _ { i j }$ stands for the covariates of consumer i when s/he applied the sample of product j. We have two types of covariates: The first are those that capture the application and purchase history of consumer i before making the focal application, i.e. Appliednum<sub>ij</sub>, $B \_ { 2 M a m o u n t _ { i j } . }$ The second are those related to the product characteristics such as PPrice, PFMCG, IS\_PNew, Avg\_rating, Num\_news etc.

$$
u _ {i j} = \beta \mathrm{X} _ {i j} + \varepsilon_ {i j}\tag{2}
$$

To capture the unobserved consumer heterogeneity, we adopt a latent class model. As previously explained, latent class model (LCM) is a data un-mixing procedure that attempts to explain the observed association between variables by introducing unobservable underlying classes (clusters) [7,9]. It distinguishes subgroups of cases from a number of variables and covariates or demographic variables, such that the underlying segments from the general population can be identified. LCM has been widely employed in previous studies to segment consumers [38,39,45] or product management [40]. In this study, we specify consumers' class-specific coefficients $\beta _ { c }$ to capture heterogeneity across consumers in their responses to the sampling campaign. Conditional on consumer i belonging to class c, the probability that consumer i buys the brand of sampled product follows the Probit model, i.e.,

$$
\operatorname * {P r} \left(y _ {i j} = 1 | c l a s s _ {i} = c\right) = \Phi \left(\beta_ {c} X _ {i j}\right)\tag{3}
$$

We further take the multinomial Probit form measuring the probability of consumer i belonging to class c. We allow the class membership to be dependent on consumer specific variables $Z _ { i } ,$ including variables such as CCity, CDuration, CLevel, and CTappliednum.<sup>4</sup>

$$
\operatorname * {P r} (c l a s s _ {i} = c) = \Phi (\theta_ {c} Z _ {i})\tag{4}
$$

We employ city, consumers' tenure/duration as a customer on the platform, their membership level attained (calculated by the platform based mainly on their historical purchase amount), and their number of application(s) made as variables for the latent class modeling for two reasons: 1) these variables reflect a combination of consumer characteristics including their consumption environment (large or small city) that may determine their exposure to product or promotional information, and their states of being with the platform (tenure/duration, membership level attained) as well as related to the sample application itself (number of applications made); 2) they are used in place of other factors such as consumer motivations that can only be psychologically assessed through survey or interview which is challenging to implement, and consumer demographics such as age, gender, and income that are likely to be withheld by consumers due to privacy concerns. Thus, it may be more viable for companies to leverage on the variables investigated to perform classification of the consumers.

The unconditional probability that consumer i buys the brand of sampled product is:

$$
\operatorname * {P r} \left(y _ {i j} = 1 \mid \text { class } _ {i} = c\right) F _ {i j, c} = \operatorname * {P r} \left(y _ {i j} = 1\right) = \sum_ {c = 1} ^ {C} \operatorname * {P r} (\text { class } _ {i} = c)\tag{5}
$$

With the above equations, we obtain the log likelihood function as

$$
\begin{array}{l} L \left(\beta_ {c}, \theta_ {c} \mid X _ {1 i j}, Z _ {i}\right) = \prod_ {i = 1} ^ {n} \prod_ {j = 1} ^ {k} \left(F _ {i j, c}\right) ^ {y _ {i j} = 1} \left(1 - F _ {i j, c}\right) ^ {y _ {i j} = 0} \\ \ln L = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {k} \left(y _ {i j} * \ln \Phi \left(F _ {i j, c}\right) + \left(1 - y _ {i j}\right) * \ln \Phi \left(1 - F _ {i j, c}\right)\right) \end{array}\tag{6}
$$

## 4.2. Endogeneity of receiving product sample

A critical issue in the model estimation is the potential endogeneity issue associated with consumers' receiving a sample (i.e., for focal variable Sample $. R e c e i v e d _ { i j } )$ because consumers who were selected to receive a sample may be more likely to buy the product for some potential unobserved reasons. Although in our case, the e-commerce platform claims that they assigned the samples randomly and did not select sample recipients strategically at initial stage, this bias may still exist for some unobservable reasons (e.g., unconscious or humaninherent biases during the execution). To account for this potential endogeneity issue, we run propensity score matching to alleviate the potential bias between the two groups.

Propensity score matching (PSM) is a statistical matching technique that attempts to reduce the bias due to confounding variables that could be found in an estimate of the treatment effect obtained from simply comparing outcomes among units that received the treatment versus those that did not [41]. PSM attempts to mimic randomization between recipients and non-recipients by creating a group of recipients that is comparable on all observed covariates to a group of non-recipients. We use the observed explanatory variables, including prior purchase amount, number of applied samples, as well as the consumers' characteristics as the covariates, and employ Logit function to calculate the propensity scores for each applicant with these covariates, and then match the recipients and non-recipients with similar propensity score.

After the application of the PSM, 1691 unmatched non-receiving applications were dropped from our observations to avoid potential bias, resulting in improvement in the balance between the two groups along the key variables. As can be seen from Table 3, the t-test of all the variables between the two groups are not significant.

## 5. Estimations results and discussion

## 5.1. Model comparison

We run the latent class model by setting the number of class c = 1 − 5. Table 4 reports the results of model fit comparison. We found the lowest AIC and BIC values when the number of segments = 3, suggesting that there are three latent classes of the applicants' brand purchase behavior in response to online sampling campaigns.

## 5.2. Estimation results

Before we report the results of LCM, we first estimate the baseline model with only one segmentation. That is, we treat all the applicants' responses as homogenous. The results are shown in the first column of Table 5. We can see that the coefficient of Sample\_Received is positive and significant, suggesting that on average the receipt of a product sample could increase the purchase probability of the sampled brand. In terms of the sample's product characteristics, price, new product, and FMCG product have negative impacts on applicants' brand purchase behavior, while the average rating and brand awareness have a positive effect.

Next, we report and discuss the estimation results of the latent class model with three consumer segments. The estimation of latent class model yields two parts of results: First is the estimation of β in Eq. (2). The results of the latent class model reveal that the applicants could be classified into three segments with their estimated coefficients, i.e. the individuals who share similar coefficients are identified as the same sub-group with a finite mixture specification. The second part of the results is the value of θin Eq. (4). For the identification purpose, we set the θ of segment 1 as the baseline, and interpret θ of the other two segments in terms of the relative value compared to segment 1. In the following, we explain the applicants' different responses to online product sampling and discuss their classification.

Table 3  
t-Test results of main variables between sample receivers and non-receivers.

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Matched (Yes/No)</td><td colspan="2">Mean</td><td rowspan="2">bias (%)</td><td rowspan="2">t-Test</td></tr><tr><td>Receivers</td><td>Non-receivers</td></tr><tr><td rowspan="2">Appliednumij</td><td>No</td><td>26.116</td><td>15.345</td><td>23.4</td><td>24.85***</td></tr><tr><td>Yes</td><td>26.116</td><td>27.048</td><td>-2.0</td><td>-1.29</td></tr><tr><td rowspan="2">B_2Mamountij</td><td>No</td><td>886.590</td><td>610.170</td><td>21.3</td><td>23.57***</td></tr><tr><td>Yes</td><td>886.590</td><td>882.820</td><td>0.3</td><td>0.17</td></tr><tr><td rowspan="2">CCityi</td><td>No</td><td>2.017</td><td>2.005</td><td>1.0</td><td>0.99</td></tr><tr><td>Yes</td><td>2.017</td><td>2.003</td><td>1.2</td><td>0.82</td></tr><tr><td rowspan="2">CTaplliednumi</td><td>No</td><td>73.979</td><td>37.732</td><td>38.7</td><td>42.46***</td></tr><tr><td>Yes</td><td>73.979</td><td>77.873</td><td>-4.2</td><td>-2.48*</td></tr><tr><td rowspan="2">CDurationi</td><td>No</td><td>565.980</td><td>454.460</td><td>32.7</td><td>31.79***</td></tr><tr><td>Yes</td><td>565.980</td><td>569.890</td><td>-1.1</td><td>-0.75</td></tr><tr><td rowspan="2">CLveli</td><td>No</td><td>13.982</td><td>10.375</td><td>64.6</td><td>59.73***</td></tr><tr><td>Yes</td><td>13.982</td><td>13.929</td><td>0.9</td><td>0.67</td></tr></table>

Table 4  
Model comparison results.

<table><tr><td>Model</td><td>S = 1</td><td>S = 2</td><td>S = 3</td><td>S = 4</td><td>S = 5</td></tr><tr><td>Log likelihood</td><td>193,940</td><td>108,190</td><td>102,780</td><td>105,220</td><td>119,180</td></tr><tr><td>AIC</td><td>387,894</td><td>216,414</td><td>205,614</td><td>210,514</td><td>238,454</td></tr><tr><td>BIC</td><td>387,968</td><td>216,593</td><td>205,899</td><td>210,904</td><td>238,950</td></tr></table>

The lowest value of each row was in bold to indicate that S = 3 was the best model.

As shown in Table 5, the impact of receiving a free sample is significant only in the first segment of applicants after taking consumers' heterogeneity into account. In other words, free sampling was effective for these applicants in inducing their further purchase, but not for the other two types of applicants. The coefficient of Sample\_Received is not statistically significant for the other two segments. In this regard, the applicants in the first segment appear to be the most desirable consumers whom brands may want to target in their future online product sampling campaigns.

We also find differences in other coefficients across the three segments. For example, the coefficients of the previous application number and successful application number are negative for the second and third segments, indicating that the previous experience of applying for product samples have a negative effect on the purchase behavior of these applicants. The effect might be due to the possible gambling mentality of these two groups, i.e., the applicants tend to treat their product sample application as a gamble rather than with the intention to try out something they are really interested in. Interestingly, previous purchase amount may demotivate applicants in the first and second segments to make subsequent purchase. It could be that the large amount of previous products purchased decreased their shopping needs, which makes sense for most consumers. The sample's products characteristics such as price, new product, FMCG and average rating have similar impacts across all the three segments. However, the effect of brand awareness is significant only for the third segment, suggesting that consumers in this segment are more interested in popular brands than other consumers.

## 5.3. Applicants' classification

The value of θ at Table 5 discloses the difference of individual characteristics across three segments. Compared with the first segment and second segment, the city value of the third segment is significantly smaller, suggesting that these applicants are more likely from larger cities. In addition, the total sample application number shows different patterns; specifically, the applicants in the third segment applied for significantly more samples than the first segment. In order to better depict the characteristics of the applicants in each segment, we list the mean value of the main variables of the three segments in Table 6.

The results in Table 6 suggest that applicants in the first segment (S1) are not heavy buyers on the online platform because their average purchase level is the lowest among the three segments, and their duration of being a consumer on the platform is also the shortest. Moreover, their total number of applications for a sample is the smallest among the three segments. While the applicants in this segment exhibited features of less-experienced shoppers on the platform, they demonstrated a strong tendency to purchase if they received the product sample. As shown in Table 6, their purchase ratio of brand (50.91%) is much higher than that of the other two segments (11.28% and 8.7%) when they received the sample. The difference is quite astonishing as the first segment applicants have about 6 times higher purchase probability than that of the third segment, and 4.5 times higher than that of the second segment (S2). We believe these consumers are the average consumers who have moderate shopping experience on the online platform. For these consumers, receiving a product sample would have an especially large impact on their purchase consideration by reducing product uncertainty for them. However, it is also important to note that when these consumers did not receive the product sample, they would become less inclined to make a purchase, as indicated by their small purchase ratio (4.96%). The denial of access to product sample might make these consumers feel particularly disappointed, thus discouraging their purchase making [25,42].

Table 6  
Table 5 Estimation results of latent class model.

<table><tr><td rowspan="2">Variables</td><td rowspan="2">One segmentation baseline model</td><td colspan="3">Three-segment model</td></tr><tr><td>Segment 1</td><td>Segment 2</td><td>Segment 3</td></tr><tr><td> $\beta$ </td><td></td><td></td><td></td><td></td></tr><tr><td>Sample_Received</td><td>0.1236***(0.0030)</td><td>0.3767***(0.0740)</td><td>-0.0054(0.0037)</td><td>0.0291(0.0394)</td></tr><tr><td>Appliednum</td><td>-0.0273**(0.0118)</td><td>-0.002(0.0334)</td><td>-0.1905***(0.0651)</td><td>-0.0451***(0.0128)</td></tr><tr><td>B_2Mamount</td><td>-0.0643***(0.0055)</td><td>-1.3740***(0.1217)</td><td>-0.1745***(0.0239)</td><td>0.0259***(0.0068)</td></tr><tr><td>PPrice</td><td>-0.3508***(0.0180)</td><td>-0.4897***(0.0495)</td><td>-0.3420***(0.0219)</td><td>-0.2624***(0.0385)</td></tr><tr><td>PFMCG</td><td>-0.1150***(0.0040)</td><td>-0.1089***(0.0065)</td><td>-0.1588***(0.0064)</td><td>-0.0884***(0.0120)</td></tr><tr><td>IS_PNew</td><td>-0.3732***(0.0047)</td><td>-0.3866***(0.0092)</td><td>-0.5539***(0.0069)</td><td>-0.2703***(0.0129)</td></tr><tr><td>Avg_rating</td><td>0.1211***(0.0114)</td><td>0.2191***(0.0302)</td><td>0.0955***(0.0148)</td><td>0.017(0.0141)</td></tr><tr><td>Num_news</td><td>0.0102***(0.0031)</td><td>0.0006(0.0052)</td><td>0.0088(0.0055)</td><td>0.0373***(0.0097)</td></tr><tr><td>Constant</td><td>-1.6775***(0.0059)</td><td>-2.4295***(0.0470)</td><td>-1.2525***(0.0103)</td><td>-1.8518***(0.0198)</td></tr><tr><td> $\theta$ </td><td></td><td></td><td></td><td></td></tr><tr><td>CCity</td><td></td><td></td><td>0.0778***(0.0037)</td><td>-0.0677***(0.0082)</td></tr><tr><td>CDuration</td><td></td><td></td><td>0.4627***(0.0039)</td><td>0.0445***(0.0082)</td></tr><tr><td>CLevel</td><td></td><td></td><td>0.0075(0.0040)</td><td>1.2767***(0.0176)</td></tr><tr><td>CTappliednum</td><td></td><td></td><td>0.8706***(0.0133)</td><td>2.3627**(0.0132)</td></tr><tr><td>Constant</td><td></td><td></td><td>-0.2158***(0.0053)</td><td>-2.2455***(0.0158)</td></tr><tr><td>Percentage</td><td>100%</td><td>54.68%</td><td>30.75%</td><td>14.58%</td></tr><tr><td>Observation</td><td>280,761</td><td>153,520</td><td>86,334</td><td>40,935</td></tr><tr><td>Rho</td><td></td><td>0.424***</td><td></td><td></td></tr><tr><td>-LLikelihood</td><td>193,940</td><td>102,780</td><td></td><td></td></tr></table>

Standard errors in parentheses  
<sup>⁎</sup>p b 0.05, <sup>⁎⁎</sup>p b 0.01, <sup>⁎⁎⁎</sup>p b 0.001

The applicants in the second segment (S2) have the longest shopping experience on this online platform, and are heavy buyers with the highest purchase level. In addition, the number of times they applied for a sample is higher than that of the average shoppers. However, whether a product sample is received does not appear to have a strong impact on their purchase behavior. Their purchase ratios when they received vs. when they did not receive a product sample were quite close (11.28% vs. 10.3%). These consumers might be very mature shoppers who have rich shopping experience on the online platform. Furthermore, they were fairly unaffected by whether their application for a product sample was successful; such stability could mean that these seasoned consumers just enjoy the shopping process and might see applying for a product sample as an additional source of potential shopping gratification, being familiar with various marketing tactics. Thus, whether a product sample is obtained does not matter much to them.

Consumer segment comparison.

<table><tr><td rowspan="2"></td><td colspan="2">Segment 1</td><td colspan="2">Segment 2</td><td colspan="2">Segment 3</td></tr><tr><td>Mean</td><td>SE</td><td>Mean</td><td>SE</td><td>Mean</td><td>SE</td></tr><tr><td>CCity</td><td>2.0452</td><td>0.003</td><td>2.0744</td><td>0.0041</td><td>1.6839</td><td>0.0049</td></tr><tr><td>CDuration</td><td>377.717</td><td>0.6582</td><td>566.9927</td><td>1.416</td><td>493.073</td><td>1.55</td></tr><tr><td>CLvel</td><td>12.9027</td><td>0.0229</td><td>12.9662</td><td>0.0168</td><td>20.14</td><td>0.0116</td></tr><tr><td>CTappliednum</td><td>8.5992</td><td>0.0403</td><td>16.0649</td><td>0.1508</td><td>199.7322</td><td>0.4746</td></tr><tr><td>Purchase ratio if sample received</td><td>0.5091</td><td>0.0168</td><td>0.1128</td><td>0.0035</td><td>0.087</td><td>0.0342</td></tr><tr><td>Purchase ratio if sample not received</td><td>0.0496</td><td>0.0006</td><td>0.103</td><td>0.0011</td><td>0.0417</td><td>0.001</td></tr><tr><td>Overall purchase ratio</td><td>0.0522</td><td>0.0006</td><td>0.1039</td><td>0.001</td><td>0.0417</td><td>0.001</td></tr></table>

For the applicants in the third segment (S3), whether they received the sample or not would also not impact their purchase decision significantly. By looking into their characteristics, the applicants in this segment are more likely to reside in big cities, and share similar characteristics in terms of purchase level and shopping experience, except the notably higher total application number. They applied about 23 times more than the applicants in the first and second segments. We thus label this segment as “opportunists”, who applied for product sample primarily for their monetary value [33], but not for reasons related to experiencing the product. The mean value of their purchase ratio after receiving a sample is the lowest among all the applicants (8.7%). In view of these results, it is important for online platforms or brands to recognize such type of applicants, and try to avoid giving product samples to them in future (or exclude them from the random drawing).

## 5.4. Robustness check

We checked the robustness of our results using different alternative specifications. Two fixed effects are included to examine if the results still hold after controlling for the heterogeneity of products category and sampling time. The left side of Table 7 reports the results after including the fixed effects of product category. The 401 products in our dataset is classified into 18 categories by the platform; thus, we generate 17 product category dummies to control for the fixed effects of products. The right side of Table 7 is the results after controlling for 11 monthly dummies of the sampling campaign period. We could see that the percentage of each segment is slightly changed, while the whole results pattern remains consistent with our main results.

Table 7 Robustness check results.

<table><tr><td rowspan="2"></td><td colspan="4">Model with the fixed effects of product category</td><td colspan="4">Model with the fixed effects of sampling time</td></tr><tr><td>Baseline Model</td><td>Segment 1</td><td>Segment 2</td><td>Segment 3</td><td>Baseline Model</td><td>Segment 1</td><td>Segment 2</td><td>Segment 3</td></tr><tr><td colspan="9"> $\beta$ </td></tr><tr><td>Sample_Received</td><td>0.0918***(0.0033)</td><td>0.325***(0.0087)</td><td>-0.0046(0.0044)</td><td>0.0313(0.0406)</td><td>0.0152***(0.0007)</td><td>0.083***(0.0030)</td><td>-0.0007(0.0007)</td><td>0.0048(0.0061)</td></tr><tr><td>Appliednum</td><td>-0.0403*(0.0178)</td><td>0.007(0.0132)</td><td>-0.1651*(0.0841)</td><td>-0.0476***(0.0131)</td><td>-0.0013**(0.0004)</td><td>-0.0002(0.0014)</td><td>-0.0051***(0.0013)</td><td>-0.0005**(0.0002)</td></tr><tr><td>B_2Mamount</td><td>-0.049***(0.0056)</td><td>-0.4536***(0.0665)</td><td>-0.0545**(0.0198)</td><td>0.0189**(0.0070)</td><td>-0.0059***(0.0004)</td><td>-0.034***(0.0025)</td><td>-0.0107***(0.0021)</td><td>0.0022***(0.0006)</td></tr><tr><td>PPrice</td><td>-0.134***(0.0085)</td><td>-0.1514***(0.0146)</td><td>-0.1199***(0.0118)</td><td>-0.153***(0.0287)</td><td>-0.0165***(0.0002)</td><td>-0.013***(0.0003)</td><td>-0.0285***(0.0007)</td><td>-0.0103***(0.0006)</td></tr><tr><td>PFMCG</td><td>-0.176***(0.0144)</td><td>-0.1873***(0.0214)</td><td>-0.1732***(0.0249)</td><td>-0.266***(0.0349)</td><td>-0.0161***(0.0005)</td><td>-0.0112***(0.0006)</td><td>-0.0286***(0.0011)</td><td>-0.0086***(0.0010)</td></tr><tr><td>IS_PNew</td><td>-0.295***(0.0051)</td><td>-0.2864***(0.0085)</td><td>-0.4089***(0.0078)</td><td>-0.215***(0.0140)</td><td>-0.0408***(0.0004)</td><td>-0.0302***(0.0005)</td><td>-0.0783***(0.0011)</td><td>-0.022***(0.0010)</td></tr><tr><td>Avg_rating</td><td>0.068***(0.0067)</td><td>0.0863***(0.0118)</td><td>0.0697***(0.0100)</td><td>0.0215(0.0139)</td><td>0.0062***(0.0003)</td><td>0.0062***(0.0003)</td><td>0.0069***(0.0005)</td><td>0.0008(0.0006)</td></tr><tr><td>Num_news</td><td>0.042***(0.0034)</td><td>0.0334***(0.0051)</td><td>0.0460***(0.0056)</td><td>0.072***(0.0104)</td><td>0.0002(0.0006)</td><td>-0.0004(0.0007)</td><td>-0.0014(0.0015)</td><td>0.0051**(0.0018)</td></tr><tr><td>Fixed effect</td><td>included</td><td>included</td><td>included</td><td>included</td><td>included</td><td>included</td><td>included</td><td>included</td></tr><tr><td>Constant</td><td>-1.743***(0.0141)</td><td>-2.0081***(0.0308)</td><td>-1.5216***(0.0251)</td><td>-1.628***(0.0356)</td><td>0.0668***(0.0005)</td><td>0.0518***(0.0010)</td><td>0.1139***(0.0013)</td><td>0.0412***(0.0018)</td></tr><tr><td colspan="9"> $\theta$ </td></tr><tr><td>CCity</td><td></td><td></td><td>0.0686***(0.0039)</td><td>-0.0484***(0.008)</td><td></td><td></td><td>0.926***(0.0043)</td><td>-0.094***(0.0125)</td></tr><tr><td>CDuration</td><td></td><td></td><td>0.4658***(0.0039)</td><td>0.0455***(0.082)</td><td></td><td></td><td>0.559***(0.0046)</td><td>0.1913***(0.0125)</td></tr><tr><td>CLevel</td><td></td><td></td><td>0.0069(0.004)</td><td>1.2889***(0.0177)</td><td></td><td></td><td>-0.0045(0.0047)</td><td>2.065***(0.0288)</td></tr><tr><td>CTappliednum</td><td></td><td></td><td>0.8657***(0.0117)</td><td>2.376***(0.0134)</td><td></td><td></td><td>0.8513***(0.0068)</td><td>3.488**(0.0208)</td></tr><tr><td>Constant</td><td></td><td></td><td>-2.122***(0.0045)</td><td>-2.402***(0.4949)</td><td></td><td></td><td>-0.313***(0.0053)</td><td>-3.467***(0.0269)</td></tr><tr><td>Percentage</td><td>100%</td><td>57.25%</td><td>28.00%</td><td>14.75%</td><td>100%</td><td>51.42%</td><td>29.30%</td><td>20.28%</td></tr><tr><td>Observation</td><td>280,761</td><td>160,736</td><td>78,613.1</td><td>41,412</td><td>280,761</td><td>144,367</td><td>82,263</td><td>56,938</td></tr><tr><td>Rho</td><td></td><td>0.517***</td><td></td><td></td><td></td><td>0.448***</td><td></td><td></td></tr></table>

Standard errors in parentheses  
<sup>⁎</sup>p b 0.05, <sup>⁎⁎</sup>p b 0.01, <sup>⁎⁎⁎</sup>p b 0.001

## 5.5. Post-hoc analysis

From the results above, it is obvious that “opportunists” should be avoided for sending product samples. However, the targeting strategy for the segment 1 (S1) and segment 2 (S2) consumers is not straightforward. It seems a good strategy to distribute more product samples to the average shoppers (S1) given their favorable purchase responses after receiving a product sample, but is this so? Per the current implementation by the online platform, the average success ratio of sample applications was set at 3% (i.e., out of 100 applications, 3 applicants were selected to receive a product sample). Based on this success ratio, the average purchase rate of S1 consumers was 6.34% (i.e., 50.91% ∗ 3% + 4.96% ∗ 97%), and that of S2 consumers was 10.36% (i.e., 11.28% ∗ 3% + 10.3% ∗ 97%). Thus, we can see that the average purchase rate of S2 was substantially higher than that of S1 due to the large magnitude of negative repercussion of consumers in S1 who did not receive a product sample. Following this, it turns out that a better strategy is to target consumers in the S2 segment.

Still, what if the platform increases the success ratio of sample applications? To assess this, we examine the purchase rate of consumers in S1 and S2 at different success ratios (see Table 8). We could see from Table 8 that when the success ratio is set below 12%, targeting consumers in the S2 segment yield higher purchase rate. When the success ratio is set at 12% or above, however, the resulting purchase rate of consumers in S1 starts exceeding that of consumers in S2. In these conditions (success ratio ≥ 12%), targeting consumers in the S1 segment becomes a better strategy. Thus, it can be seen that which segments of consumers to target is not straightforward, and depends on how the platform or brand concerned set the success ratio of sample applications.

Assessment of overall purchase rates with changes in application success ratios.

<table><tr><td>Sample application Success ratio</td><td>Purchase rate of S1</td><td>Purchase rate of S2</td></tr><tr><td>0.03</td><td>0.0634</td><td>0.1033</td></tr><tr><td>0.04</td><td>0.0680</td><td>0.1034</td></tr><tr><td>0.05</td><td>0.0726</td><td>0.1035</td></tr><tr><td>0.06</td><td>0.0772</td><td>0.1036</td></tr><tr><td>0.07</td><td>0.0818</td><td>0.1037</td></tr><tr><td>0.08</td><td>0.0864</td><td>0.1038</td></tr><tr><td>0.09</td><td>0.0910</td><td>0.1039</td></tr><tr><td>0.1</td><td>0.0956</td><td>0.1040</td></tr><tr><td>0.11</td><td>0.1001</td><td>0.1041</td></tr><tr><td>0.12</td><td>0.1047</td><td>0.1042</td></tr><tr><td>0.13</td><td>0.1093</td><td>0.1043</td></tr></table>

## 6. Conclusion

The recent use of the online product sampling strategy comes with it important questions to answer as well as opportunities that can be leveraged at the same time. In this study, our objectives have been to provide answers to 1) how online product sampling campaigns alter consumers' brand purchase behavior, 2) differences of such an impact between those who received the samples and those who did not, and 3) the heterogeneity in consumers with regard to their responses to the sampling campaigns. The attainment of these objectives is enabled by our unique dataset obtained from an e-commerce platform that just launched their product sampling section. During this initial period, the platform randomly drew the sample recipients from among the applicants, and tracked individual consumer's purchase behavior. These findings have several useful theoretical and managerial implications, as discussed below.

## 6.1. Theoretical and managerial implications

Online product sampling is an under-explored research area given that it is an emerging marketing strategy with a relatively short history. This study contributes to the body of knowledge about online product sampling, and guide the practitioners involved (online platforms and brands) in two major aspects.

First, we extend the research on product sampling by investigating its effects at an individual-level. Prior literature has mainly examined product sampling effect on sales at an aggregate level (e.g., [1–3,5,6]). By contrast, our research investigates individual-level sales impact of product sampling afforded by the online context that makes tracking individual responses to sampling campaigns viable, which could measure the effectiveness of sampling campaign more precisely, and in turn may help brands improve the sampling management.

Second, we also extend the emerging online sampling research by examining the use of this strategy for physical products rather than digital products that have been the focus of online sampling research thus far [6,10–12,43]. With brands increasingly see online platforms as a promising channel to administer product sampling given their reach and information-capturing capabilities, our research can offer valuable empirical insights to guide this strategy.

Third, afforded by our individual-level data, our research provides a comparison of the purchase responses between those received a product sample and who did not. The large and significant difference unveiled suggests that while consumers who received a product sample are indeed motivated to purchase from the brand subsequently, the negative repercussion of those who did not receive one (a large portion of the applicants) needs to be noted as well. Following from this, it makes sense to understand what characteristics of consumers, among the applicants, are more likely to be sensitive to receiving a product sample in terms of their subsequent purchase behavior.

Specifically, our analyses highlight three distinct types of consumers with respect to how they responded to sample application as well as their characteristics. As may be expected, there is a group of consumers who are keen on applying for product samples but are unmoved by the outcome in their subsequent purchase decisions. Thus, mangers may want to first tease out this group of consumers and avoid/minimize the provision of product samples to them. Apart from these “opportunist”, two other groups of consumers emerge from among the sample applicants, who can be differentiated based mainly on their tenure with the online platform and their level of purchase made.

Intuition may suggest that the loyal customers (i.e., those with longer tenure and who have purchased more) are likely the ones who would respond most favorably to the receipt of a product sample. However, our empirical analysis suggests otherwise – it is the relatively new consumers with moderate purchase level who are particularly responsive to receiving a product sample. Compared to the former (older customers), these latter customers made significantly greater purchase after receiving a sample, yet they also tend more to reduce their purchase if they were denied access to it. Thus, managers may want to be particularly attentive to these customers when they administer online product sampling and decide who to give a sample. This finding, while not totally in line with intuition, is not unexplainable - the seasoned customers may have become more immune to marketing tactics on the platform, and regard the online product sampling as just another tactic used. Therefore, whether a product sample is received does not give to them as strong a stimulus as to the newer customers.

Nevertheless, our further analyses show that after evening out both purchase increase (with receipt of product sample) and purchase decrease (when no product sample is received), it is still more profitable overall to give product samples to the older customer group. This is because while giving product samples to the newer customer group can bring greater purchase, since inevitably not all customers can get a sample, the negative repercussion of reduced sales from those not receiving a sample is also more pronounced in this group. Given that unhappy customers are prone to leave, managers may want to take considerations beyond just overall purchase increase. Our analyses suggest that by setting the success ratio (i.e., the percentage of customers who can get a sample if they applied for it) to be higher (12% compared to the original mere 3% in our study's context), the overall purchase increase of targeting the newer customer group becomes higher (vis-à- vis targeting the older customer group) while also minimizing the risk of creating “unhappy” customers given their particularly high sensitivity to receiving a product sample. While beyond the scope of this study, the decision is certainly also dependent on the cost of providing more product samples. Our research provide a way for the managers to consider how to best economize their online product sampling campaigns, which is a complicated decision that is situation-dependent.

In general, our findings above unveil salient consumer heterogeneity that helps answer the questions of “who should get product samples?” and “how to identify them?”, and caution a “one size fits all” strategy in administering online product sampling. We also demonstrate a viable method (LCM) for platforms or brands to differentiate the applicants, and select the more profitable consumers to maximize the payoff of online product sampling campaigns should they intend to do so. Given the convenience of collecting data in the online context, platforms/brands can utilize this method to understand their consumers more accurately, and then make better decisions to improver payback from their sampling campaigns as a whole.

In summary, our research provides clear guidance based on empirical analyses for how firms may strategically select sample recipients [2], and offers a more complete understanding of the effects of online product sampling on individual consumers' purchase behavior. The insights generated are timely and valuable for marketers on how to better economize on online physical product sampling, for which knowledge about its administration and exploitation is currently lacking [44].

## 6.2. Limitations

This study has limitations that need to be noted. First, it might have been more ideal to identify the class of each consumer in LCM based on the demographic information such as age, gender, and income. However, due to confidentiality issues such individual information is not available to the researchers. Also such information is prone be inaccurate as consumers may prefer not giving their actual demographics such as income to the company owing to privacy concerns. In this study, we examine consumer characteristics that can be accurately observed and tracked on the e-commerce platform such as their tenure/duration with the platform, city, and purchase history. Nonetheless, if accurate consumers' demographic information can somehow be obtained in future research, further insights may be uncovered.

Second, we employ consumers' brand purchase as the dependent variable in this study. However, the platform only provides the information on whether the consumers purchased the sampled brand after the application; detailed transaction information such as when and what purchase was made is beyond access. Future research may extend our study by delving deeper into the detailed purchase behaviors, and provide a more comprehensive understanding of the effects of online product sampling.

Finally, while our research unveils consumer heterogeneity according to their different responses to online sampling, the reasons behind such differences remain unclear. Future research may employ methods such as surveys and interviews to uncover the psychological rationales associated with different types of consumers such as their underlying motivations.

## References

[1] A. Heiman, B. McWilliams, Z. Shen, D. Zilberman, Learning and forgetting: modeling optimal product sampling over time, Manag. Sci. 47 (4) (2001) 532–546.

[2] D. Jain, V. Mahajan, E. Muller, An approach for determining optimal product sampling for the diffusion of a new product, J. Prod. Innov. Manag. 12 (2) (1995) 124–135.

[3] H.B. Lammers, The effect of free samples on immediate consumer purchase, J. Consum. Mark. 8 (2) (1991) 31–37.

[4] C.A. Scott, The effects of trial and incentives on repeat purchase behavior, J. Mark. Res. (1976)263-269

[5] K. Bawa, R. Shoemaker, The effects of free sample promotions on incremental brand sales Mark Sci. 23 (3) (2004).345-363

[6] W. Zhou, W. Duan, The impact of free sampling of information goods on the dynamics of online word-of-mouth and retail sales, AMCIS 2012 Proceedings, 2012.

[7] P.E. Green, F.J. Carmone, D.P. Wachspress, Consumer segmentation via latent class analysis, J. Consum. Res. 3 (3) (1976) 170–174.

[8] S.C. Roesch, M. Villodas, F. Villodas, Latent class/profile analysis in maltreatment research: a commentary on Nooner et al., Pears et al., and looking beyond, Child Abuse Negl, 34 (3)(2010) 155–160.

[9] M. Wedel, W.A. Kamakura, Market Segmentation: Concepts and Methodological Foundations Kluwer Academic Boston 20o0

[10] H.K. Cheng, Y. Liu, Optimal software free trial strategy: the impact of network externalities and consumer uncertainty, Inf. Syst. Res. 23 (2) (2012) 488–504.

[11] N. Hu, L. Liu, I. Bose, J. Shen, Does sampling influence consumers in online retailing of digital music? IseB 8 (4) (2010) 357–377.

[12] C.A. Wang, X.M. Zhang, Sampling of information goods, Decis. Support. Syst. 48 (1) (2009) 14–22.

[13] K.N.T. Dodd, D.A. Laverie, Gratuity purchasing at wineries: an investigation of the determining factors, Int. J. Wine Bus. Res. 19 (4) (2007) 239–256.

[14] J.F. Sherry, Gift giving in anthropological perspective, J. Consum. Res. 10 (1983) 157–168.

[15] W.W. Hui, J. Paynter, A. Everett, Online Product Promotion & Trial Effectiveness, Proceedings of the 3rd International Conference on Electronic Business, ICEB, Singapore 2003, pp. 94–96.

[16] D. McGuiness, M. Brennan, P. Gendall, An empirical test of product sampling and couponing, J. Mark. Res. Soc. 37 (2) (1995) 159–170

[17] A.K. Ghosh, Chakraborty and Ghosh D.B., Improving brand performance by altering Consumers' brand uncertainty, J. Prod. Brand Manag. 4 (5) (1995) 14–20.

[18] C.W. Park, H. Assael, S. Chaiy, Mediating roles of trial and learning on involvement associated characteristics, J. Consum. Mark. 4 (1987) 25–34.

[19] DeAnna S. Kempf, Robert E. Smith, Consumer processing of product trial and the influence of prior advertising: a structural modeling approach, J. Mark. Res. 35 (August) (1998) 325–338.

[20] A.A. Wright, J.G. Lynch Jr., Communication effects of advertising versus direct experience when both search and experience attributes are present, J. Consum. Res. (1995) 708-718

[21] J.M. Burger, The foot-in-the-door compliance procedure: a multiple-process analysis and review. Personal. Soc. Psychol. Rey, 3 (4) (1999) 303–325.

[22] C. Seligman, M. Bush, K. Kirsch, Relationship between compliance in the foot-in-thedoor paradigm and size of first request, J. Pers. Soc. Psychol. 33 (5) (1976) 517.

[23] M. Snyder, M.R. Cunningham, To comply or not comply: testing the self-perception explanation of the"foot-in-the-door" phenomenon, J. Pers. Soc. Psychol. 31 (1) (1975) 64.

[24] D.J. Bem, Self-perception theory, Adv. Exp. Soc. Psychol. 6 (1972) 1–62.

[25] L.J. Marks, M.A. Kamins, The use of product sampling and advertising: effects of sequence of exposure and degree of advertising claim exaggeration on consumers' belief strength, belief con dence, and attitudes, J. Mark. Res. (1988) 266–281.

[26] J.A. Bargh, Losing consciousness: automatic influences on consumer judgment, behavior, and motivation, J. Consum. Res. 29 (3) (2002) 280–285.

[27] Z. Jie, F. Xiao, O.R. Liu, Online consumer search depth: theories and new findings, J. Manag. Inf. Syst. 23 (3) (2006) 71–95.

[28] G.P. Moschis, R.L. Moore, A longitudinal study of television advertising effects, J. Consum. Res. 9 (3) (1982) 279–286.

[29] M.A.H. Saleh, B. Alothman, L. Alhoshan, Impact of gender, age and income on Consumers' purchasing responsiveness to free-product samples, Res. J. Int. Stud. 26 (2013) 83–94.

[30] D. Vakratsas, T. Ambler, How advertising works: what do we really know? J. Mark. 63 (1) (1999) 26–43.

[31] X. Fang, J.C. Mowen, Examining the trait and functional motive antecedents of four gambling activities: slot machines, skilled card games, sports betting, and promotional games, J. Consum. Mark. 26 (2) (2009) 121–131.

[32] E.B. Selby, W. Beranek, Sweepstakes contests: analysis, strategies, and survey, Am. Econ, Rev, 71 (1) (1981) 189–195

[33] E.M. Tauber, Why do people shop? J. Mark. 36 (4) (1972) 46–49.

[34] D.A. Aaker, K.L. Keller, Consumer evaluations of brand extensions, J. Mark. 54 (1) (1990) 27–41.

[35] L.L. Berry, Cultivating service brand equity, J. Acad. Mark. Sci. 28 (1) (2000) 128–137.

[36] R.H. Fazio, M.P. Zanna, Attitudinal qualities relating to the strength of the attitudebehavior relationship, J. Exp. Soc. Psychol. 14 (4) (1978) 398–408.

[37] P. Tuominen, Managing brand equity, Finnish J. Bus. Econ. 48 (1) (1999) 65–100.

[38] A. Bhatnagar, S. Ghose, A latent class segmentation analysis of e-shoppers, J. Bus. Res. 57 (7) (2004) 758–767.

[39] U. Konuş, P.C. Verhoef, S.A. Neslin, Multichannel shopper segments and their covariates, J. Retail. 84 (4) (2008) 398–413.

[40] E. Díaz, C. Koutra, Evaluation of the persuasive features of hotel chains websites: a latent class segmentation analysis, Int. J. Hosp. Manag. 34 (2013) 338–347.

[41] P.R. Rosenbaum, B.R. Donald, The central role of the propensity score in observational studies for causal effects, Biometrika 70 (1) (1983) 41–55.

[42] P.A. Goering, Effects of product trial on consumer expectations, demand, and prices, J. Consum. Res. 12 (1) (1985) 74–82.

[43] M. Peitz, P. Waelbroeck, Why the music industry may gain from free downloading—the role of sampling, Int. J. Ind. Organ. 24 (5) (2006) 907–913.

[44] X. Yao, X. Lu, C.W. Phang, S. Ba, Dynamic sales impacts of online physical product sampling, Info. Manage. 54 (5) (2017) 599–612.

[45] A. Bhatnagar, S. Ghose, Segmenting consumers based on the benefits and risks of In ternet shopping, J. Bus. Res. 57 (12) (2004) 1352–1360.

Xianghua Lu is a professor in the Department of Information Management and Information Systems, School of management, Fudan University, Shanghai. She received her Ph.D degree from Fudan University, China. Her research interests include Internet Marketing, E-commerce and IT management. Her research work has been published in academic journals such as Marketing Science, Information Systems Research, Journal of Management Information System, Information & Management and other academic journals

Chee Wei Phang is a professor in the Department of Information Management and Information Systems at Fudan University China. After completing his Ph D. at the National University of Singapore, he joined Fudan University in December 2008. His research interests include online social media, mobile commerce, and IT in public sector. His works have appeared in top-tier journals including the Management Science, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, IEEE Transactions on Engi neering Management, Journal of Association for Information Systems, Information & Management et al.

Sulin Ba is a professor of Information Systems at the School of Business at the University of Connecticut. She holds a Ph.D. from the University of Texas at Austin. Her current research interests include e-service, online Word-of-mouth, online price dispersion, digital health communities, and pricing of virtual goods in virtual worlds. She has published in Management Science, Information Systems Research, MIS Quarterly, Journal of Management Informa tion Systems, Production and Operations Management, Decision Support Systems, and other academic journals.

Xinlin Yao is currently a PhD candidate in the Department of Information Management and Information Systems, School of Management of Fudan University. His research interests are in the areas of electronic commerce and social media. He has published in Information & management, and other academic conferences.
