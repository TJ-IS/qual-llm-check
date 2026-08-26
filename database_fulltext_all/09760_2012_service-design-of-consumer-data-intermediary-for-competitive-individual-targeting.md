---
otero_id: 9760
otero_key: "WZEZFBMF"
title: "Service design of consumer data intermediary for competitive individual targeting"
authors: "Xia Zhao"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.08.015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Service design of consumer data intermediary for competitive individual targeting

Xia Zhao ⁎

Bryan School of Business and Economics, University of North Carolina at Greensboro, United State

## a r t i c l e i n f o

Article history: Received 11 May 2012 Received in revised form 6 July 2012 Accepted 17 August 2012 Available online 25 August 2012

Keywords: Target marketing Individual targeting Customer data intermediaries Information economics

## a b s t r a c t

Individual targeting, a marketing strategy that <sup>fi</sup>rms target individual consumers with tailored offers, is currently a widespread practice. Customer data intermediaries (CDIs) have emerged recently to help <sup>fi</sup>rms learn their prospective customers and launch their target marketing campaigns. This paper uses a common-value auction framework to study how a CDI designs and differentiates its information services to help two competing <sup>fi</sup>rms identify and target valuable customers. We characterize the <sup>fi</sup>rms' equilibrium target marketing strategies. The results show that the CDI serves one <sup>fi</sup>rm exclusively in unpromising markets where the proportion of valuable customers is relatively low, and provides both <sup>fi</sup>rms with differentiated services in promising markets where the proportion of valuable customers is relatively high. In addition, the CDI differentiates its services less when the proportion of valuable customers is higher.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The past decade has witnessed the boom of target marketing based on consumer data [10,11]. For example, retailers provide checkout coupons to consumers based on their past purchases. Phone carriers (e.g., AT&T) often lure customers by offering them personalized checks depending on consumers' calling history. Credit card companies (e.g., American Express) usually issue preapproved credit cards to customers with good credit scores. Banks (e.g., Bank of American) often promote diverse <sup>fi</sup>nancial products with free trials based on their clients' account information.

Customer data intermediaries (CDIs) have emerged to help <sup>fi</sup>rms implement target marketing. CDIs collect individual-level customer data through various online and of<sup>fl</sup>ine channels and facilitate <sup>fi</sup>rms to target individual customers with tailored advertisements or promotional incentives. For example, Catalina Marketing discovers consumers' shopping habits using data collected through its network of 24,000 U.S. and 8000 international merchandiser stores, and provides its clients various target marketing services, such as checkout coupons, quick cash and shopping lists.<sup>1</sup> DoubleClick tracks Web users by name and address as they move from one website to the next, and helps <sup>fi</sup>rms deliver targeted banner advertisements.<sup>2</sup> Pancras and Sudhir [15] summarize major CDIs and their services. The CDI services signi<sup>fi</sup>cantly improve the effectiveness of target marketing campaigns. For example, the average redemption rate of Catalina Marketing incentives (coupons) is about 6.3%, more than eight times greater than other non shopperdriven traditional promotional methods.<sup>3</sup> As <sup>fi</sup>rms compete aggressively using target marketing, CDIs play an important role in shaping the <sup>fi</sup>rms competition.

Considering the growing importance of CDIs, there is a need to study CDIs' businesses from strategic perspectives. In different markets, CDIs employ signi<sup>fi</sup>cantly diverse business strategies [15]. Some CDIs offer their services on an exclusive basis and others offer on a nonexclusive basis. For example, Catalina only sells its services exclusively, but Abacus and I-Behavior sell on a nonexclusive basis to any catalog marketer or specialty retailer. It is important to understand what drives such diversity in CDIs' businesses. In addition, when the CDIs offer nonexclusive services, the CDIs often offer services with differential levels of service differentiation. Therefore, it is worthwhile to examine how the CDI's service differentiation in<sup>fl</sup>uences market competition and how the CDI makes strategic decisions on service differentiation.

The purpose of this paper is to examine the impact of CDI services on <sup>fi</sup>rm competition and explain the diversity of CDIs' business strategies. We develop a model in which a CDI may help two competing <sup>fi</sup>rms identify and target valuable prospective customers. Compared to the <sup>fi</sup>rms, the CDI can better segment prospective customers based on the data it collects. With the CDI's services of customer segmentation, <sup>fi</sup>rms can better tailor promotional incentives to different customer segments. Using this model, we examine the CDI's selling strategy of its services. In particular, when should the CDI offer the service to only one <sup>fi</sup>rm exclusively and when should the CDI serve both <sup>fi</sup>rms? If the CDI serves both <sup>fi</sup>rms, how should it differentiate its services between <sup>fi</sup>rms? Because the CDI's service strategies in<sup>fl</sup>uence the <sup>fi</sup>rms' competition, our model also characterizes how <sup>fi</sup>rms compete using target marketing.

The existing research on <sup>fi</sup>rm competition with target marketing largely focuses on horizontally differentiated <sup>fi</sup>rms (e.g., [3,4,8,9, 12,13,16,17]). The individual-level customer information is used to discover the customers' brand preferences (i.e., horizontal preferences). This study, in contrast, considers the individual-level information about customers' heterogeneous preferences to the product itself (i.e., vertical preferences). Our model captures the competition between two <sup>fi</sup>rms selling identical products. Therefore, the valuable customers are equally valuable to both <sup>fi</sup>rms, and the <sup>fi</sup>rms' competition exhibits the features of common-value auction (e.g., [6,14]). The focus on the customer's product preference, instead of the brand preference, enables us to gain useful insights that are not captured in the existing literature. For example, the existing literature generally suggests that the decrease in information asymmetry among <sup>fi</sup>rms softens their competition for each other's loyal customers (who are valuable to only one <sup>fi</sup>rm), but intensi<sup>fi</sup>es their competition for comparison shoppers (common-value customers) when <sup>fi</sup>rms can better distinguish comparison shoppers from loyal customers (e.g., [3]). However, our study reveals that the decrease in information asymmetry among <sup>fi</sup>rms does not always intensify their competition for common-value customers.

This study also relates to the research on quality differentiation of information product/service. The existing literature has well explored this issue from the standpoints of monopolist sellers (e.g., [1,19]) or competing sellers (e.g., [5,21]). However, quality differentiation by the information intermediary has received relatively less attention. Bhargava and Choudhary [2] show that an information intermediary can provide quality-differentiated services and bene<sup>fi</sup>t from positive cross-network effects. Weber and Zhang [22] consider how a search intermediary provides differentiated paid referral services through the design of search ranking. These models, in line with most of traditional quality differentiation models, assume that the users have heterogeneous preferences to product quality. In contrast, our model considers the case that <sup>fi</sup>rms (i.e., users) are ex ante homogeneous and the <sup>fi</sup>rm heterogeneity is completely endogenized by the intermediary (i.e., the CDI) through service differentiation. Our model illustrates a different strategic effect of quality differentiation, i.e., the CDI's service design in<sup>fl</sup>uences the competition between homogeneous <sup>fi</sup>rms in target marketing. A similar issue has been explored in the studies on referral infomediaries (e.g., [4,7]). These models, however, only consider the use of service exclusivity as a differentiation approach. Our model also considers the use of non-exclusive services with differentiated information quality as a differentiation approach. In addition, this study also explores how market conditions in<sup>fl</sup>uence CDIs' business strategies. Our model considers both the promising markets where the majority of prospective customers are valuable customers and the unpromising markets where the majority of prospective customers are non-valuable customers. The analysis characterizes how the CDI's service strategies are dependent on the market conditions. The results help explain the diversity of CDIs' strategies across different markets, and also provide managerial implications on the CDI businesses in different markets.

The <sup>fi</sup>ndings of this study are as follows. The study <sup>fi</sup>nds that when the CDI provides <sup>fi</sup>rms more similar information about the commonvalue customer (i.e., less differentiated services), the <sup>fi</sup>rms' competition may be softened. Although some prior studies (e.g., [3]) also suggest that information similarity may soften <sup>fi</sup>rm competition, their analyses are based on the models with ex ante differentiated <sup>fi</sup>rms. Our model generates this <sup>fi</sup>nding in the setting where <sup>fi</sup>rms are ex ante homogeneous and the <sup>fi</sup>rm differentiation is completely endogenized by the CDI. Our model also characterizes when the decrease in information asymmetry between <sup>fi</sup>rms softens the competition and when it intensi<sup>fi</sup>es the competition. This insight generates important implications for the CDI's service strategies. When the CDI serves both <sup>fi</sup>rms, adjusting the service differentiation between <sup>fi</sup>rms allows the CDI to maintain a desirable level of <sup>fi</sup>rm competition and maximize its pro<sup>fi</sup>t from selling information services to <sup>fi</sup>rms. Based on the results of <sup>fi</sup>rm competition, the study characterizes the optimal service strategies for the CDI. The analysis suggests that in unpromising markets where the proportion of valuable customers is relatively small (i.e., the proportion of valuable customers is lower than ${ \sqrt { 3 } } / 3 )$ , the CDI serves only one <sup>fi</sup>rm exclusively. However, in promising markets where the proportion of valuable customers is relatively large (i.e., the proportion of valuable customers is higher than ${ \sqrt { 3 } } / 3 )$ , the CDI serves both <sup>fi</sup>rms but provides differentiated services. The study also characterizes the optimal degree of service differentiation.

The rest of the paper is organized as follows. Section 2 explains the model setup. Section 3 examines the <sup>fi</sup>rms' competition and Section 4 characterizes the service strategies of the CDI. Section 5 concludes the paper.

## 2. Model setup

We model a case where two <sup>fi</sup>rms, <sup>fi</sup>rm 1 and 2, compete in acquiring a group of prospective customers. A prospective customer, once acquired by a <sup>fi</sup>rm, can bring the <sup>fi</sup>rm sales revenue over her lifetime business relationship with the <sup>fi</sup>rm. We assume that there are two types of customers: valuable customers and non-valuable customers. We use V to denote the customer value. A valuable customer, once acquired by a <sup>fi</sup>rm, can generate a positive amount of revenue $R > 0$ for the <sup>fi</sup>rm. Therefore, the value of a valuable customer is $V { = } R$ for the <sup>fi</sup>rm. A non-valuable customer, in contrast, does not generate any revenue for the <sup>fi</sup>rm, i.e., $V { = } 0$ . We let $T \in \{ H , L \}$ denote the type of a customer with $T { = } H$ representing a valuable customer and $T = L$ representing a non-valuable customer. λ is used to denote the prior probability that a prospective customer is valuable, and $0 { < } \lambda { \le } 1$

Firms compete for prospective customers by offering them promotional incentives. Examples of promotional incentives include target coupons, price discounts or other nonmonetary bene<sup>fi</sup>ts. We use $m _ { i } ( i { \in } \{ 1 , 2 \} )$ to represent the monetary value of <sup>fi</sup>rm i's targeted promotional incentives. In this model, it is assumed that the two <sup>fi</sup>rms sell identical products/services and the prospective customers have no brand preference. The customers are acquired by the <sup>fi</sup>rm which offers them the higher promotional incentives. This also implies that the value of customers is the same to both <sup>fi</sup>rms. Therefore, our model exhibits the features of common-value auctions (e.g., [6,14]) and distinguishes from the traditional models of target marketing competition (e.g., [3,4]). Without loss of generality, the model can be simpli<sup>fi</sup>ed as that the two <sup>fi</sup>rms compete for a representative prospective customer who is valuable with a prior probability of λ.

We assume that <sup>fi</sup>rms do not directly observe whether or not the prospective customer is valuable. A CDI can help <sup>fi</sup>rms identify the customer value and improve their targetability. The CDI, armed with vast individual-level customer data collected from multiple sources, is more capable to estimate the value of the prospective customer. For example, if the data shows that the customer has been active in purchasing over the past few months, this customer is more likely to be a valuable customer. Otherwise, the customer is more likely to be a non-valuable customer. We model the case where the CDI provides customer segmentation services to <sup>fi</sup>rms. Speci<sup>fi</sup>cally, the CDI classi<sup>fi</sup>es the customer into one of two segments, a high segment for valuable customer or a low segment for non-valuable customers. The CDI's customer segmentation service generates value by allowing the <sup>fi</sup>rm to be more informative about the customer value. That is, if the <sup>fi</sup>rm observes that the customer is classi<sup>fi</sup>ed into the high (low) segment, it should become more con<sup>fi</sup>dent that this customer is valuable (non-valuable). With the CDI's service of customer segmentation, the <sup>fi</sup>rm can customize its promotional incentives sent to each segment.

We use S to denote the customer segmentation service that the CDI provides to <sup>fi</sup>rm 1. S has two potential values, h and $l , \ S = h$ means that the CDI classi<sup>fi</sup>es the customer into the high segment for firm $1 , S = l$ means that the CDI classi<sup>fi</sup>es the customer into the low segment for <sup>fi</sup>rm 1. We use Pr(h) and Pr(l) to denote the probability that the customer is classi<sup>fi</sup>ed into the high segment $( \mathrm { i } . \mathrm { e } . , S = h )$ for <sup>fi</sup>rm 1 and the probability that the customer is classi<sup>fi</sup>ed into the low segment $( \mathrm { i } . \mathbf { e } . , S = l )$ for <sup>fi</sup>rm 1, respectively.

Note that the customer segmentation S may not be completely accurate. That is, it is possible that the valuable (non-valuable) customer is incorrectly classi<sup>fi</sup>ed into the low (high) segment. We use ψ to denote the probability that the valuable customer is correctly classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1, and use ϕ to denote the probability that the non-valuable customer is incorrectly classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1. Therefore, the CDI can increase the information accuracy of the customer segmentation S by increasing ψ and decreasing ϕ, e.g. the CDI can analyze more historical data and/or apply more strict criteria to select valuable customers. We assume that

$$
\psi > \phi .\tag{1}
$$

The assumption (1) ensures that the segmentation S provides useful information for <sup>fi</sup>rm 1. To see that, note that we have

$$
P r (h) = \lambda \psi + (1 - \lambda) \phi \text {   and   } P r (l) = \lambda (1 - \psi) + (1 - \lambda) (1 - \phi).\tag{2}
$$

Using the Bayes rule, we can derive the following posterior beliefs.

$$
\begin{array}{l} P (H | h) = \frac {\lambda \psi}{P r (h)}, P (L | h) = 1 - P (H | h), \\ P (L | l) = \frac {(1 - \lambda) (1 - \phi)}{P r (l)}, P (H | l) = 1 - P (L | l). \end{array}
$$

where $P ( H | h ) \ ( P ( L | h ) )$ is the posterior probability that the prospective customer is a valuable (non-valuable) customer given that the customer is classi<sup>fi</sup>ed into the high segment $( \mathrm { i } . \mathrm { e } . , S { = } h )$ for <sup>fi</sup>rm 1, and $P ( L | l )$ $( P ( H | l ) )$ is the posterior probability that the prospective customer is a non-valuable (valuable) customer given that the customer is classi<sup>fi</sup>ed into the low segment $( \mathrm { i } . \mathrm { e } . , S { = } l )$ for <sup>fi</sup>rm 1.<sup>4</sup> The assumption (1) ensures the following inequalities hold.

$$
P (H | h) > \lambda \text {   and   } P (L | l) > 1 - \lambda .\tag{3}
$$

Inequalities (3) indicate that the posterior probability of a highsegment (low-segment) customer being valuable (non-valuable) is higher than the prior probability, $\lambda \left( 1 - \lambda \right)$ ). Therefore, the CDI's segmentation provides <sup>fi</sup>rm 1 with useful information about the customer's value. We use $E [ V | S ] ~ ( S \in \{ h , l \} )$ to denote the expected customer value for <sup>fi</sup>rm 1 given S.

$$
E [ V | h ] = R P (H | h) \text {   and   } E [ V | l ] = R P (H | l).
$$

In addition to <sup>fi</sup>rm 1, the CDI decides whether or not to serve <sup>fi</sup>rm 2. If the CDI serves both <sup>fi</sup>rms, it may differentiate its services. For example, if the CDI uses less data and less sophisticated business intelligence techniques in serving <sup>fi</sup>rm $^ { 2 , }$ the customer segmentation for <sup>fi</sup>rm 2 can be less accurate than that for <sup>fi</sup>rm 1. To capture the potential service differentiation, we use $\tilde { S }$ to denote the customer segmentation for <sup>fi</sup>rm $2 . { \tilde { S } }$ has two potential values, $\tilde { h }$ and $\tilde { l } . \tilde { S } = \tilde { h } ( \tilde { S } = \tilde { l } )$ <sup>¼ ¼</sup>means that the CDI classi<sup>fi</sup>es the prospective customer into the high (low) segment for <sup>fi</sup>rm 2. Without loss of generality, we assume that when the CDI differentiates services, the customer segmentation S for <sup>fi</sup>rm 1 is always more accurate than the customer segmentation S<sup>˜</sup> for <sup>fi</sup>rm 2. Speci<sup>fi</sup>cally, we use $P r \Big ( \tilde { h } | S \Big )$ and $P r \Big ( \tilde { l } | S \Big )$ to denote the probabilities of $\tilde { S } = \tilde { h }$ and $\tilde { S } = \tilde { l }$ respectively, conditional on the value of S. $P r \Big ( \tilde { h } | S \Big )$ and $P r \Big ( \tilde { l } \vert S \Big )$ are de<sup>fi</sup>ned as follows.

$$
P r \Big (\tilde {h} | h \Big) = P r \Big (\tilde {l} | l \Big) = \frac {1 + \zeta}{2}, P r \Big (\tilde {l} | h \Big) = P r \Big (\tilde {h} | l \Big) = \frac {1 - \zeta}{2}.\tag{4}
$$

where $\zeta \in [ 0 , 1 ]$ is the similarity factor. It captures to what extent the segmentation $\tilde { S }$ is similar to the segmentation $S . ^ { 5 }$

$\operatorname { I f } { \zeta } = 1$ , the segmentation S<sup>˜</sup> is the same as S. In this case, the CDI's services to both <sup>fi</sup>rms are not differentiated. I $\scriptstyle { \mathrm { f } } 0 < \zeta < 1$ , when $S = h ,$ it is more likely that $\tilde { S } = \tilde { h }$ . In other words, when a customer is classi-<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1, she is more likely to also be classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 2. Similarly, when $S { = } l , $ it is more likely that $\tilde { S } = \tilde { l } .$ However, as long as $\zeta < 1$ , the segmentation S<sup>˜</sup> is less <sup>¼</sup>accurate than the segmentation $S _ { * }$ When $\zeta = 0 ,$ given any value of $S ,$ we have $\tilde { S } = \tilde { h }$ or <sup>˜</sup>l with $1 / 2$ probability. This essentially means that <sup>¼</sup>the segmentation $\tilde { S }$ provides no useful customer information to <sup>fi</sup>rm 2. Therefore, we can consider $\zeta = 0$ as the case that the CDI does not serve <sup>fi</sup>rm $2 \ ( \mathrm { i . e . }$ , the CDI serves <sup>fi</sup>rm 1 exclusively), and <sup>fi</sup>rm 2 just uses the prior probability to estimate the customer value.

Given a $\tilde { S } { \in } \{ \tilde { h } , \tilde { l } \}$ , the expected value of the customer to <sup>fi</sup>rm 2 can be represented as

$$
E \Big [ V | \tilde {S} \Big ] = P \Big (h | \tilde {S} \Big) E \Big [ V | h \Big ] + P \Big (l | \tilde {S} \Big) E \Big [ V | l \Big ],\tag{5}
$$

where $P \Big ( h | \tilde { S } \Big )$ and $P \big ( l | \tilde { S } \big )$ are posterior probabilities of $S = h$ and $S = l$ respectively, given a $\tilde { S } { \in } \{ \tilde { h } , \tilde { l } \}$ . Using the Bayes' rule, we have

$$
\begin{array}{l} P \Big (h | \tilde {S} \Big) = \frac {P r \Big (\tilde {S} | h \Big) P r (h)}{P r \Big (\tilde {S} | h \Big) P r (h) + P r \Big (\tilde {S} | l \Big) P r (l)} \text { and } \\ P \Big (l | \tilde {S} \Big) = \frac {P r \Big (\tilde {S} | l \Big) P r (l)}{P r \Big (\tilde {S} | l \Big) P r (l) + P r \Big (\tilde {S} | h \Big) P r (h)}. \end{array}\tag{6}
$$

It is worth noting that we have $P \Big ( T | \tilde { S } \Big ) = P r ( T | h ) P \Big ( h | \tilde { S } \Big )$ 十 $P r ( T | l ) P \Big ( l | \tilde { S } \Big )$ , where $T = \{ H , L \}$ . This suggests that $P \Big ( H | \tilde { h } \Big ) \leq P ( H | h )$ and $P \Big ( L | \tilde { l } \Big ) \leq P ( L | l )$ . In other words, <sup>fi</sup>rm 1's information is more accurate than <sup>fi</sup>rm 2. In addition, we have $\frac { \partial P \Big ( H | \tilde { h } \Big ) } { \partial \zeta } > 0 \mathrm { a n d } \frac { \partial P \Big ( L | \tilde { l } \Big ) } { \partial \zeta } > 0$ . This means that an increase of ζ increases the accuracy of <sup>fi</sup>rm 2's information. With some algebra (more details in the Appendix $\mathsf { A } )$ , we can show the following relationships.

Remark 1.

$$
E [ V | l ] \leq E [ V | \tilde {l} ] \leq E [ V ] \leq E [ V | \tilde {h} ] \leq E [ V | h ]
$$

The Remark suggests that the segmentation $\tilde { S }$ is less accurate than the segmentation S in indicating the value of a customer. Table 1 summarizes the notation of this model.

Before we present the model analysis, we <sup>fi</sup>rst use a numerical example to illustrate the model setup. This numerical example will be used throughout the paper to explain the results. Suppose that $R =$ 10. The value of the prospective customer is therefore either $V { = } 1 0$ or $V { = } 0 .$ . In other words, a valuable customer brings a revenue income

Table 1 Notations of the model.

<table><tr><td>Notations</td><td>Description</td></tr><tr><td> $T = \{H,L\}$ </td><td>The type of the perspective customer.  $T = H (T=L)$  indicates a valuable (non-valuable) customer.</td></tr><tr><td> $R$ </td><td>The revenue that a firm can generate from the valuable customer.</td></tr><tr><td> $V$ </td><td>The value of the prospective customer.  $V = R (V=0)$  for the valuable (non-valuable) customer.</td></tr><tr><td> $\lambda$ </td><td>The prior probability that the prospective customer is valuable.</td></tr><tr><td> $m_i, i = \{1,2\}$ </td><td>The promotional incentive that firm  $i$  offers to the prospective customer.</td></tr><tr><td> $\psi$ </td><td>The probability that the CDI correctly classifies a valuable customer into the high segment for firm 1.</td></tr><tr><td> $\phi$ </td><td>The probability that the CDI incorrectly classifies a non-valuable customer into the high segment for firm 1.</td></tr><tr><td> $S = \{h, l\}$ </td><td>The segmentation for firm 1.  $S = h (S=1)$  means the customer is classified into the high (low) segment for firm 1.</td></tr><tr><td> $\tilde{S} = \left\{ \tilde{h}, \tilde{l} \right\}$ </td><td>The segmentation for firm 2.  $\tilde{S} = \tilde{h} (\tilde{S} = \tilde{l})$  means the customer is classified into the high (low) segment for firm 2.</td></tr><tr><td> $\Pr(h)$  (or  $\Pr(l)$ )</td><td>The probability that the CDI classifies the customer into the high (or low) segment for firm 1.</td></tr><tr><td> $\Pr(\tilde{h}|S)(orPr(\tilde{l}|S))$ </td><td>Given the segmentation  $S (S=\{h, l\})$  for firm 1, the probability that the CDI classifies the customer into the high (or low) segment for firm 2.</td></tr><tr><td> $P(h|\tilde{S})(orP(l|\tilde{S}))$ </td><td>Given the segmentation  $\tilde{S}(\tilde{S} = \{\tilde{h}, \tilde{l}\})$  for firm 2, the posterior probability that the CDI classifies the customer into the high (or low) segment for firm 1.</td></tr><tr><td> $\zeta$ </td><td>The level of similarity between the segmentation services to these two firms.  $\zeta = 1$  means the services to these two firms are not differentiated;  $\zeta = 0$  means that the CDI serves only firm 1 exclusively.</td></tr><tr><td> $E[V|h]$  (or  $E[V|l]$ )</td><td>The expected value of the customer if the customer is classified into the high (or low) segment for firm 1.</td></tr><tr><td> $E[V|\tilde{h}](orE[V|\tilde{l}])$ </td><td>The expected value of the customer if the customer is classified into the high (or low) segment for firm 2.</td></tr><tr><td> $\pi_i$ </td><td>The expected profit of firm  $i$  in competition (exclusive of the payment to the CDI for the segmentation service).</td></tr><tr><td> $\Pi$ </td><td>The profit of the CDI from selling services to firms.</td></tr></table>

10 to the <sup>fi</sup>rm over her lifetime relationship with the <sup>fi</sup>rm, whereas a non-valuable customer brings zero revenue. Suppose that $\psi { = } 0 . 8$ and $\phi = 0 . 2$ . That is, if the customer is valuable (non-valuable), the CDI correctly classi<sup>fi</sup>es this customer into the high segment (low segment) for <sup>fi</sup>rm 1 with a probability 0.8. Therefore, suppose that $\lambda =$ 0.6 (i.e., the prior probability of valuable customer is 0.6), we have $P r ( h ) = \lambda \psi + ( 1 - \lambda ) \phi = 0 . 5 6 ( \mathrm { i . e . }$ ., with a probability 0.56, the CDI classi<sup>fi</sup>es the customer into the high-segment for <sup>fi</sup>rm 1). If <sup>fi</sup>rm 1 observes that S=h (i.e., a high-segment customer), it expects (using the Bayes' Rule) that the customer is a valuable customer with a posterior probability $\frac { \lambda \psi } { P r ( h ) } = 0 . 8 5 7 > \lambda = 0 . 6 .$ . The expected value of the customer is $E [ V | h ] = 8 . 5 7$ . On the other hand, if <sup>fi</sup>rm 1 observes $S { = } l \left( \mathrm { i . e . } \right.$ , a low-segment customer), it expects that the customer is a valuable customer with a posterior probability $\begin{array} { r } { 1 - \frac { ( 1 - \lambda ) ( 1 - \phi ) } { P r ( l ) } = 0 . 2 7 3 < 1 - \lambda = } \end{array}$ 0:4: The expected value of the customer is $E [ V | l ] = 2 . 7 3 < E [ V | h ]$

Suppose that the CDI provides a differential service S<sup>˜</sup> to <sup>fi</sup>rm 2 with a similarity factor $\zeta = 0 . 5 .$ . Then we have $P r \Big ( \tilde { h } | h \Big ) = P r \Big ( \tilde { l } | l \Big ) =$ $\frac { 1 + \zeta } { 2 } = 0 . 7 5$ . This means that if the CDI classi<sup>fi</sup>es the customer into the high segment (low segment) for <sup>fi</sup>rm 1, it also classi<sup>fi</sup>es this customer into the high segment (low segment) for <sup>fi</sup>rm 2 with a probability 0.75. Therefore, according to Eq. (6), when <sup>fi</sup>rm 2 observes $\begin{array} { r } { \widetilde { S } = \widetilde { h } \ ( \mathrm { i } . \mathrm { e } . } \end{array}$ , a high-segment customer), it expects that the customer <sup>¼</sup>is also a high-segment customer for <sup>fi</sup>rm 1 with a posterior probability $P \Big ( h | \tilde { h } \Big ) = 0 . 7 9$ . Firm 2 thus expects the value of the customer to be $E \big [ V | \tilde { h } \big ] = 7 . 3 6$ . When <sup>fi</sup>rm 2 observes $\tilde { S } = \tilde { l } ( \mathrm { i . e . , }$ , a low-segment customer), it expects that the customer is also a low-segment customer for <sup>fi</sup>rm 1 with a posterior probability $P \Big ( l | \tilde { l } \Big ) = 0 . 7 0$ : Firm 2 thus expects the value of the customer to be $E \Big [ V | \tilde { l } \Big ] = 4 . 4 7 < E \Big [ V | \tilde { h } \Big ]$ . Note that we have $E [ V | l ] < E { \Big [ } V | { \tilde { l } } { \Big ] } < E [ V ] = 6 < E { \Big [ } V | { \tilde { h } } { \Big ] } < E [ V | h ]$ , which means that the segmentation S for <sup>fi</sup>rm 1 is more accurate in revealing the customer value than the segmentation $\tilde { S }$ for <sup>fi</sup>rm 2.

The timing of events is as follows. First, the CDI designs the segmentation S for <sup>fi</sup>rm 1 by determining ψ and ϕ. In addition to <sup>fi</sup>rm 1, the CDI decides whether or not to also serve <sup>fi</sup>rm 2. If the CDI also serves <sup>fi</sup>rm 2, it determines $\zeta$ to differentiate the segmentation S<sup>˜</sup> for <sup>fi</sup>rm 2 from the segmentation S for <sup>fi</sup>rm 1. The CDI also determines how much to charge each <sup>fi</sup>rm. After determining all these details, the CDI makes take-it-or-leave-it offers to <sup>fi</sup>rms. Second, <sup>fi</sup>rms determine whether to accept the CDI's offers and use the CDI's services. Firms who use the CDI's services observe the customer segmentation (<sup>fi</sup>rm 1 observes the customer segmentation S and <sup>fi</sup>rm 2, if served, observes the customer segmentation S<sup>˜</sup>). Third, <sup>fi</sup>rms simultaneously decide their promotional incentives sent to the prospective customer, $m _ { i } ,$ where $i = 1 , 2 .$ . Finally, the customer patronizes the <sup>fi</sup>rm which offers the higher promotional incentive. The value of the customer is realized for the winning <sup>fi</sup>rm. We assume that everything is common knowledge except the customer's value V and the <sup>fi</sup>rms' segmentations S and ${ \tilde { S } } .$ . In practice, CDIs such as Catalina Marketing often keep their service speci<sup>fi</sup>cations transparent (e.g., the length of transaction history used in data analysis, redemption rate of target marketing services). Therefore, we assume that <sup>fi</sup>rms can assess the service quality and differentiation (i.e., ψ, ϕ, and ζ).

## 3. Firm competition

Following backward induction, we <sup>fi</sup>rst consider the <sup>fi</sup>rms' competition given the customer segmentations, and then consider the CDI's strategies based on the equilibrium of <sup>fi</sup>rm competition. In this section, we derive the Bayesian Nash Equilibrium of the <sup>fi</sup>rms' competition. In the competition, <sup>fi</sup>rm i chooses its promotional incentive, m , to maximize its expected pro<sup>fi</sup>t, denoted by $\pi _ { i } , i = 1 , 2$

When $\zeta = 1$ , <sup>fi</sup>rms' segmentations are exactly the same. Therefore, <sup>fi</sup>rms engage in a Bertrand competition. Firms both offer $m = E [ V | l ]$ when $S = \tilde { S } = l$ and $m { = } E [ V | h ]$ when $S = \tilde { S } = h$ . We next focus on <sup>¼ ¼</sup>the equilibria when $0 { \le } { \zeta } { < } 1$ <sup>¼ ¼</sup>. We <sup>fi</sup>nd that no pure-strategy equilibrium exists for the <sup>fi</sup>rms' competition. Suppose that <sup>fi</sup>rm 2 offers a deterministic promotional incentive m . Firm 1 always offers a promotional incentive higher than $m _ { 2 } { \mathrm { ~ i f ~ } } E [ V | S ] > m _ { 2 } .$ . As a result, <sup>fi</sup>rm 2 can only acquire the customer when $E [ V | S ] \leq m _ { 2 }$ and make a nonpositive pro<sup>fi</sup>t. This is a typical case of Winner's Curse. The only equilibrium is a mixed-strategy equilibrium. In marketing, mixed strategies can be interpreted as the frequent dispersion of <sup>fi</sup>rms' sales offers or promotions [18]. The proof of no pure-strategy equilibrium is in the Appendix A.

Let $G _ { 1 } ( m | S ) = P r ( m _ { 1 } \leq m | S )$ denote the equilibrium cumulative distribution function (CDF) of <sup>fi</sup>rm 1's promotional incentive conditional on its customer segmentation S. Let $G _ { 2 } \Big ( m | \tilde { S } \Big ) = P r \Big ( m _ { 2 } \leq m | \tilde { S } \Big )$ denote the equilibrium CDF of <sup>fi</sup>rm 2's promotional incentive conditional on its customer segmentation S<sup>˜</sup>. Firm 1's expected pro<sup>fi</sup>t when offering $m _ { 1 } ,$ conditional on S, can be represented as

$$
\begin{array}{l} \pi_ {1} (m _ {1} | S) = P r \Big (\tilde {h} | S \Big) G _ {2} \Big (m _ {1} | \tilde {h} \Big) \Big (E \Big [ V | S \Big ] - m _ {1} \Big) \\ \qquad + P r \Big (\tilde {l} | S \Big) G _ {2} \Big (m _ {1} | \tilde {l} \Big) \Big (E \Big [ V | S \Big ] - m _ {1} \Big). \end{array}\tag{7}
$$

The <sup>fi</sup>rst term in the right-hand side (RHS) of Eq. (7) is <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t when the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm $\bar { 2 } ( \mathrm { i } . \mathsf { e } . , \ \tilde { S } = \tilde { h } )$ . The second term is <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t <sup>¼</sup>when the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 2 $( \mathrm { i } . \mathsf { e } . , \tilde { S } = \tilde { l } ) .$ . Similarly, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t when offering m , con-<sup>¼</sup>ditional on S<sup>˜</sup>, can be represented as

$$
\begin{array}{c} \pi_ {2} \Big (m _ {2} | \tilde {S} \Big) = P \Big (h | \tilde {S} \Big) G _ {1} \Big (m _ {2} | h \Big) \Big (E \Big [ V | h \Big ] - m _ {2} \Big) \\ + P \Big (l | \tilde {S} \Big) G _ {1} \Big (m _ {2} | l \Big) \Big (E \Big [ V | l \Big ] - m _ {2} \Big). \end{array}\tag{8}
$$

The <sup>fi</sup>rst term in the RHS of Eq. (8) is <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t when the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1 $( \mathrm { i } . \mathrm { e } . , S { = } h )$ The second term is <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t when the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm $1 \ ( \mathrm { i . e . , } \ S = l )$ . Proposition 1 characterizes the equilibrium distributions of <sup>fi</sup>rms' promotional incentives when $P r ( h ) \leq P r ( l ) \ ( \mathrm { i . e . }$ , for <sup>fi</sup>rm 1, the customer is more likely to be classi<sup>fi</sup>ed into the low segment than into the high segment).

Proposition 1. When $P r ( h ) { \leq } P r ( l )$ and $0 { \le } \zeta { < } 1$

1. If the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 1 $( \mathrm { i } . \mathbf { e } . , S = l )$ , <sup>fi</sup>rm 1 offers a promotional incentive $m _ { 1 } = E [ V | l ] ;$

2. If the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 2 $( \mathrm { i } . \mathsf { e } . , \tilde { S } = \tilde { l } )$ , <sup>fi</sup>rm 2 offers a promotional incentive $m _ { 2 } = E [ V | l ] ;$

<sup>¼</sup>3. If the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1 $( \mathrm { i . e . , } S = h )$ , <sup>fi</sup>rm 1 offers a randomized promotional incentive with the CDF

$$
G _ {1} (m | h) = \frac {P (l | \tilde {h}) (m - E [ V | l ])}{P (h | \tilde {h}) (E [ V | h ] - m)}, m \in [ E [ V | l ], E [ V | \tilde {h} ] ].
$$

(b) Firms’ Promotional Incentives When Pr(h) Pr(l)>  
![](/api/attachments/WZEZFBMF/fulltext/images/5f2133ef1766bdc258d74503fd70c79e2e9fdbee9c48e4e56531d27fbfc28203.jpg)

4. If the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 2 $( \mathrm { i } . \mathsf { e } . , \ \tilde { S } = \tilde { h } )$ , <sup>fi</sup>rm 2 offers a randomized promotional incentive <sup>¼</sup>with the CDF

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - E [ V | \tilde {h} ] - P r (\tilde {I} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}, m \in [ E [ V | I ], E [ V | \tilde {h} ] ].
$$

To help understand how <sup>fi</sup>rms compete given the customer segmentations, we use a numerical example to illustrate Proposition 1. In this example, we use the same speci<sup>fi</sup>cations as in the numerical example in the previous section. Speci<sup>fi</sup>cally, $R = 1 0 , \psi = 0 . 8 , \phi =$ 0.2, and $\zeta = 0 . 5$ . Therefore, we have $P r \Big ( \tilde { h } | h \Big ) = P r \Big ( \tilde { l } | l \Big ) = 0 . 7 5 .$ . We let $\lambda { = } 0 . 4 ~ ( \mathrm { i . e . }$ , the prior probability of valuable customer is 0.4). We therefore have $P r ( h ) = 0 . 4 4$ , i.e., with a probability 0.44, the customer is classi<sup>fi</sup>ed into the high-segment for <sup>fi</sup>rm 1. Note that $P r ( h ) < P r ( l ) = 0 . 5 6$ . With this $P r ( h )$ , we can derive the following expected values

$$
E [ V | h ] = 7. 2 7; E [ V | l ] = 1. 4 3; E [ V | \tilde {h} ] = 5. 5 4; E [ V | \tilde {l} ] = 2. 6 2,
$$

and CDFs

$$
\begin{array}{l} G _ {1} (m | h) = \frac {0 . 4 2 (m - 1 . 4 3)}{7 . 2 7 - m}; G _ {2} \Big (m | \tilde {h} \Big) \\ = \frac {2 . 3 0 - 0 . 3 3 (7 . 2 7 - m)}{7 . 2 7 - m}, m \in [ 1. 4 3, 5. 5 4 ]. \end{array}
$$

Fig. 1(a) depicts the supports of <sup>fi</sup>rms' promotional incentive distributions when $P r ( h ) { \leq } P r ( l )$ . As Proposition 1 shows, when $S { = } l ,$ <sup>fi</sup>rm 1 expects that the customer value is $E [ V | l ] = 1 . 4 3$ . Firm 1 is thus unwilling to offer any promotional incentive higher than 1.43. Because the lowest expected value of the customer across <sup>fi</sup>rms 1 and 2 is also 1.43 and both <sup>fi</sup>rms compete for the customer, <sup>fi</sup>rm 1's promotional incentive for the customer is always $m _ { 1 } = 1 . 4 3$ and <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is zero. When $S = h$ , <sup>fi</sup>rm 1's expected value for the consumer is $E [ V | h ] = 7 . 2 7$ , which is higher than $E \Big [ V | \tilde { h } \Big ]$ and $E \lceil V  \tilde { l } \rceil$ . Therefore, <sup>fi</sup>rm 1 is more willing to win this customer than <sup>fi</sup>rm 2. In equilibrium, <sup>fi</sup>rm 1 randomizes its promotional incentive in such a way that <sup>fi</sup>rm 2 earns a zero expected pro<sup>fi</sup>t.

![](/api/attachments/WZEZFBMF/fulltext/images/bf7ecf78afc63f4b69c62ea1333c3e4481fe50336c8fe2a7af1846af08aa6f08.jpg)  
Fig. 1. The equilibrium of <sup>fi</sup>rm competition

Now let us consider <sup>fi</sup>rm 2's strategies. When ${ \boldsymbol { \tilde { S } } } = { \boldsymbol { \tilde { l } } } ,$ <sup>fi</sup>rm 2 expects that the customer value is $E \Big [ V | \tilde { l } \Big ] = 2 . 6 2 > E [ V | l ]$ . We <sup>fi</sup>nd that <sup>fi</sup>rm 2's equilibrium strategy is also to offer a deterministic promotional incentive $m _ { 2 } = E [ V | l ] = 1 . 4 3$ . Firm 2 gives up the competition because of its information disadvantage. When the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 1 $( S = l ) ,$ <sup>fi</sup>rm 2 can win for sure if it offers $m _ { 2 } > 1 . 4 3$ . However, it is very likely that <sup>fi</sup>rm 2 acquires a non-valuable customer and its expected pro<sup>fi</sup>t is negative. In this case, <sup>fi</sup>rm 2 may suffer from the Winner's Curse. On the other hand, when the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1 $( S = h )$ , <sup>fi</sup>rm 1 will compete aggressively for this customer and randomize its promotional incentive in a way that <sup>fi</sup>rm 2 cannot make a positive expected pro<sup>fi</sup>t. Therefore, when $\tilde { S } = \tilde { l } ,$ <sup>fi</sup>rm 2 cannot do better than offering $m _ { 2 } = E [ V | l ] = 1 . 4 3$ (and making zero expected pro<sup>fi</sup>t).

When ${ \boldsymbol { \tilde { S } } } = { \boldsymbol { \tilde { h } } } ,$ <sup>fi</sup>rm 2 randomizes its promotional incentive. The <sup>¼</sup>upper bound of the <sup>fi</sup>rms' promotional incentive distributions is 5.54 because $E \Big [ V | \tilde { h } \Big ] = 5 . 5 4$ is the highest expected value for <sup>fi</sup>rm 2. In the mixed-strategy equilibrium, <sup>fi</sup>rm 1 and <sup>fi</sup>rm 2 randomize their promotional incentive over the same support [1.43,5.54]. Fig. 2 depicts the CDFs of <sup>fi</sup>rms' promotional incentives $G _ { 1 } ( m | h )$ and $G _ { 2 } \Big ( m | \tilde { h } \Big )$ . Note that $G _ { 2 } \Big ( m | \tilde { h } \Big )$ has a mass point at the lower bound $m { = } 1 . 4 3$ . This means that <sup>fi</sup>rm 2 provides $m _ { 2 } = 1 . 4 3$ with a positive probability of 0.06.

Next, we consider the case when $P r ( h ) { > } P r ( l )$ (i.e., for <sup>fi</sup>rm 1, the customer is more likely to be classi<sup>fi</sup>ed into the high segment than into the low segment). Eq. (2) indicates that $P r ( h ) { > } P r ( l )$ occurs if and only if $2 \lambda > \frac { 1 - 2 \phi } { \psi - \phi } .$ . Also, when $\phi > 0 . 5$ , we always have $P r ( h ) >$ $P r ( l )$ . This means that we have $P r ( h ) { > } P r ( l )$ when ϕ is suf<sup>fi</sup>ciently large. Proposition 2 characterizes the equilibrium distributions of <sup>fi</sup>rms' promotional incentives when $P r ( h ) { > } P r ( l )$

Proposition 2. When $P r ( h ) { > } P r ( l )$ and $0 { \le } { \zeta } { < } 1$

1. If the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 1 $( \mathrm { i } . \mathbf { e } . , S = l )$ , <sup>fi</sup>rm 1 offers a promotional incentive $m _ { 1 } = E [ V | l ] ;$

2. If the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 2 $( \mathrm { i } . \mathsf { e } . , \ \tilde { S } = \tilde { l } )$ , <sup>fi</sup>rm 2 offers a randomized promotional incentive with the CDF

$$
G _ {2} (m | \tilde {l}) = \frac {E [ V | h ] - \overline {{m}}}{P r (\tilde {l} | h) (E [ V | h ] - m)}, m \in [ E [ V | l ], \hat {m} ].
$$

![](/api/attachments/WZEZFBMF/fulltext/images/e645f7c1d65778396846760ba4e6e1ca178c9d370bdf4cc8f770a0e9648968ae.jpg)  
Fig. 2. Examples of the cumulative distribution functions of <sup>fi</sup>rms' promotional incentives when $\mathrm { P r } ( h ) { \leq } \mathrm { P r } ( l )$

3. If the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1 $( \mathrm { i } . \mathrm { e } . , S { = } h )$ , <sup>fi</sup>rm 1 offers a randomized promotional incentive with the CDF

$$
G _ {1} (m | h) = \left\{ \begin{array}{l} \frac {P \big (l | \tilde {l} \big) \left(m - E [ V | l ]\right)}{P \big (h | \tilde {l} \big) \left(E \big [ V | h \big ] - m\right)}, m \in [ E [ V | l ], \hat {m} ]; \\ \frac {E \big [ V | \tilde {h} \big ] - \overline {{m}} - P \big (l | \tilde {h} \big) \left(E \big [ V | l \big ] - m\right)}{P \big (h | \tilde {h} \big) \left(E \big [ V | h \big ] - m\right)}, m \in [ \hat {m}, \overline {{m}} ]. \end{array} \right.
$$

4. If the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 2 $( \mathrm { i } . \mathsf { e } . , \tilde { S } = \tilde { h } )$ , <sup>fi</sup>rm 2 offers a randomized promotional incentive <sup>¼</sup>with the CDF

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - \overline {{m}} - P r (\tilde {l} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}, m \in [ \hat {m}, \overline {{m}} ].
$$

where the cutoff levels, m^ and m, are given in the Appendix A. To explain Proposition 2, we use a numerical example again. We use the same speci<sup>fi</sup>cations as in the numerical example for Proposition 1. Speci<sup>fi</sup>cally, $R = 1 0 , \psi = 0 . 8 , \phi = 0 . 2$ , and $\zeta = 0 . 5 .$ We let $\lambda { = } 0 . 6$ (i.e., the prior probability of valuable customer is 0.6). We therefore have $P r ( h ) = 0 . 5 6 > P r ( l ) = 0 . 4 4$ . With this $P r ( h )$ , we can derive the following values

$$
\begin{array}{l} E \Big [ V | h \Big ] = 8. 5 7; E \Big [ V | l \Big ] = 2. 7 3; E \Big [ V | \tilde {h} \Big ] = 7. 3 6; E \Big [ V | \tilde {l} \Big ] = 4. 4 7; \\ \hat {m} = 2. 8 6; \overline {{m}} = 7. 1 4, \end{array}
$$

and CDFs

$$
\begin{array}{l} G _ {2} (m | \tilde {l}) = \frac {5 . 7 1}{8 . 5 7 - m}, m \in [ 2. 7 3, 2. 8 6 ]. \\ G _ {2} (m | \tilde {h}) = \frac {0 . 3 3 m - 0 . 9 4}{8 . 5 7 - m}, m \in [ 2. 8 6, 7. 1 4 ]. \\ G _ {1} (m | h) = \left\{ \begin{array}{l} \frac {2 . 3 6 (m - 2 . 7 3)}{8 . 5 7 - m}, m \in [ 2. 7 3, 2. 8 6 ]; \\ \frac {0 . 2 6 m - 0 . 4 4}{8 . 5 7 - m}, m \in [ 2. 8 6, 7. 1 4 ]. \end{array} \right.. \end{array}
$$

Fig. 1(b) depicts the supports of <sup>fi</sup>rms' promotional incentive distributions when $P r ( h ) { > } P r ( l )$ . As Proposition 2 shows, when $S { = } l ,$ <sup>fi</sup>rm 1 expects that the customer value is $E [ V | l ] = 2 . 7 3$ and therefore offers $m _ { 1 } = 2 . 7 3$ . When $S = h ,$ <sup>fi</sup>rm 1 competes less aggressively than it does in the case where $P r ( h ) { \leq } P r ( l )$ . In particular, the upper bound of the <sup>fi</sup>rms' promotional incentives is ${ \overline { { m } } } = 7 . 1 4 .$ , which is lower than $E \Big [ V | \tilde { h } \Big ] = 7 . 3 6$ (i.e., the upper bound when $P r ( h ) { \leq } P r ( l ) )$

In Proposition 2, <sup>fi</sup>rm 2 also randomizes its promotional incentive for its low-segment customer. When $\tilde { S } = \tilde { l } ,$ , <sup>fi</sup>rm 2 no longer <sup>fi</sup>nds it <sup>¼</sup>optimal to offer a promotional incentive $m _ { 2 } = E [ V | l ] = 2 . 7 3$ . Instead, <sup>fi</sup>rm 2 competes with <sup>fi</sup>rm 1 by randomizing its promotional incentive over the support $[ E [ V | l ] , \hat { m } ] = [ 2 . 7 3 , 2 . 8 6 ]$ . However, in equilib-<sup>½ ½ - ¼j - ½ -</sup>rium, <sup>fi</sup>rm 2 still earns a zero expected pro<sup>fi</sup>t in competing for its low-segment customer. This is because <sup>fi</sup>rm 1 has information advantage and randomizes its promotional incentive in such a way that <sup>fi</sup>rm 2 cannot gain a positive expected pro<sup>fi</sup>t from its low-segment customer. Fig. 3 shows the CDF of <sup>fi</sup>rm 2's promotional incentive when $\tilde { S } = \tilde { l } ,$ i.e., $G _ { 2 } \left( m | \tilde { l } \right)$ . Note that $G _ { 2 } \left( m | \tilde { l } \right)$ has a mass point at $m _ { 2 } = E [ V | l ] = 2 . 7 3$ . This means that when $\tilde { S } = \tilde { l } ,$ <sup>fi</sup>rm 2 provides $m _ { 2 } = 2 . 7 3$ with a positive probability of 0.977.

Proposition 2 indicates that when <sup>fi</sup>rm 1 randomizes its promotional incentive to its high-segment customers $( \mathrm { i . e . , } S { = } h )$ , the equilibrium distribution function $G _ { 1 } ( m | h )$ is kinked at m^ $= 2 . 8 6$ . This is caused by the difference between the customer segmentation for <sup>fi</sup>rm 1 and that for <sup>fi</sup>rm 2. The high-segment customer for <sup>fi</sup>rm 1 may be classi<sup>fi</sup>ed into either the high segment $( \mathrm { i } . \mathsf { e } . , \tilde { S } = \tilde { h } )$ or low segment $( \mathrm { i } . \mathsf { e } . , \tilde { S } = \tilde { l } )$ for <sup>fi</sup>rm 2. Firm 2 randomizes its promotional incentives over $[ E [ V | l ] , \hat { m } ]$ when $\tilde { S } = \tilde { l }$ and over $[ \hat { m } , \overline { { m } } ]$ when ${ \tilde { S } } = { \tilde { h } } .$ . Firm 1's promotional incentives targeting its high segment have to compete with these two types of <sup>fi</sup>rm 2's promotional incentives. Therefore, $G _ { 1 } ( m | h )$ is kinked at m^ . Fig. 3 shows the CDF of <sup>fi</sup>rm 1's promotional incentive when $S = h$ , i. $\therefore , G _ { 1 } ( m | h )$ , and the CDFs of <sup>fi</sup>rm 2's promotional incentive, $G _ { 2 } \Big ( m | \tilde { h } \Big )$ and $G _ { 2 } \Big ( m | \tilde { l } \Big )$

![](/api/attachments/WZEZFBMF/fulltext/images/3b2d9718c568f1b70563ec57199c95d83a68c3293e45ca27f4d1396f410d3f3f.jpg)  
Fig. 3. Examples of the cumulative distribution functions of <sup>fi</sup>rms' promotional incentives when Pr(h)>Pr(l).

Next, we consider the <sup>fi</sup>rms' expected pro<sup>fi</sup>ts in competition. We use $\pi _ { 1 }$ and $\pi _ { 2 }$ to denote the expected pro<sup>fi</sup>ts of <sup>fi</sup>rm 1 and <sup>fi</sup>rm $^ { 2 , }$ respectively. Proposition 3 summarizes the equilibrium pro<sup>fi</sup>ts of <sup>fi</sup>rms in competition.

Proposition 3. When $0 { \le } { \zeta } { < } 1$ , in equilibrium,

1. If $P r ( h ) { \leq } P r ( l )$ , <sup>fi</sup>rm 1 makes a positive expected pro<sup>fi</sup>t $\pi _ { 1 } =$ $P r ( h ) \Big ( E [ V | h ] { - } E \Big | V | \tilde { h } \Big ] \Big )$ <sup></sup>, and <sup>fi</sup>rm 2 makes zero expected pro<sup>fi</sup>t;

2. If $P r ( h ) > P r ( l )$ , <sup>fi</sup>rm 1 makes a positive expected pro<sup>fi</sup>t $\pi _ { 1 } =$ $P r ( h ) ( E [ V | h ] - \overline { { m } } )$ . Firm 2 makes a positive expected pro<sup>fi</sup>t $\pi _ { 2 } =$ $P r \Big ( \tilde { h } \Big ) \Big ( E \Big | V | \tilde { h } \Big ] - \overline { { m } } \Big )$ when $\zeta > 0$ , and a zero expected pro<sup>fi</sup>t when $\zeta = 0 ;$

3. Firm 1's expected pro<sup>fi</sup>t is always higher than <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t.

Proposition 3 illustrates and compares <sup>fi</sup>rms' expected pro<sup>fi</sup>ts. When $P r ( h ) { \leq } P r ( l )$ , only <sup>fi</sup>rm 1 earns a positive expected pro<sup>fi</sup>t in competition. We ignore the trivial case of $\pi _ { 1 } = 0 \mathrm { w h e n } P r ( h ) = 0 ( \mathrm { i . e . } ,$ , the customer is never classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1). Note that compared to <sup>fi</sup>rm 2, <sup>fi</sup>rm 1 has more accurate customer segmentation, and thus better information about the customer. Therefore, it earns a positive information rent in competition. Such <sup>fi</sup>nding is consistent with the existing literature on common-value auctions with asymmetrically informed bidders [6].

When $P r ( h ) { > } P r ( l )$ , however, Proposition 3.2 illustrates that both <sup>fi</sup>rms earn positive expected pro<sup>fi</sup>ts in competition when $0 { < } \zeta { < } 1$ . In other words, both <sup>fi</sup>rms reap information rents when the CDI serves both of them but provides differentiated services. Note that even though the customer segmentation for <sup>fi</sup>rm 2 is not as accurate as that for <sup>fi</sup>rm 1, <sup>fi</sup>rm 1 does not directly observe the segmentation outcome for <sup>fi</sup>rm 2. Thus <sup>fi</sup>rm 2's information about the customer is also private information although this information is not as good as <sup>fi</sup>rm 1's private information. Firm 2 can therefore earn information rent from this private information. Proposition 3.3 shows that <sup>fi</sup>rm 1's information rent is always higher than that of <sup>fi</sup>rm 2. This result is intuitive since <sup>fi</sup>rm 1 has better customer information than <sup>fi</sup>rm 2.

Proposition 3 presents an important insight on the competition between two <sup>fi</sup>rms with asymmetric information. Firm 2, even though less informed, also has private information. However, whether <sup>fi</sup>rm 2 can reap information rent from this private information is dependent on <sup>fi</sup>rm 1's information, i.e., whether the condition $P r ( h ) { > } P r ( l )$ holds. When $P r ( h ) { \leq } P r ( l )$ , <sup>fi</sup>rm 1 competes aggressively and strives to win the customer when $S = h ,$ , regardless of whether it is a high-segment or low-segment customer for <sup>fi</sup>rm 2. In the mixed-strategy equilibrium, <sup>fi</sup>rm 1 randomizes its promotional incentives in such a way that <sup>fi</sup>rm 2 cannot make any positive expected pro<sup>fi</sup>t in the competition when $\tilde { S } = \tilde { h } \ \mathrm { o r } \ \tilde { S } = \tilde { l } .$ However, when $P r ( h ) { > } P r ( l )$ , <sup>fi</sup>rm 1 competes less aggressively and focuses on winning <sup>fi</sup>rm 2's low-segment customer. In other words, since <sup>fi</sup>rm 1 identi<sup>fi</sup>es this customer as a valuable customer most of the time, <sup>fi</sup>rm 1 would like to take the chance that <sup>fi</sup>rm 2 may not identify this customer in the same way as <sup>fi</sup>rm 1. By doing so, <sup>fi</sup>rm 1 saves its expenditure on promotional incentive although it will more likely lose the competition. In the mixed-strategy equilibrium, <sup>fi</sup>rm 1 randomizes its promotional incentives in such a way that <sup>fi</sup>rm 2 cannot make positive expected pro<sup>fi</sup>t in the competition when ${ \tilde { S } } = { \tilde { l } } .$ . However, if the customer happens to be in <sup>fi</sup>rm 2's high-segment $( \tilde { S } = \tilde { h } )$ , the less aggressiveness of <sup>fi</sup>rm 1 enables <sup>fi</sup>rm 2 to make a positive expected pro<sup>fi</sup>t $E \lceil V  \tilde { h } \rceil - \overline { { m } }$ when $0 { < } \zeta { < } 1$ . That is why <sup>fi</sup>rm 2's overall expected pro<sup>fi</sup>t is $\pi _ { 2 } =$ $P r \Big ( \tilde { h } \Big ) \left( E \Big | V | \tilde { h } \Big ] - \overline { { m } } \right)$

Proposition 3 captures the case where $0 { \le } \zeta { < } 1 . \operatorname { I f } \zeta { = } 1$ , the customer segmentations for <sup>fi</sup>rm 1 and for <sup>fi</sup>rm 2 are the same and there is no service differentiation. In this case, <sup>fi</sup>rms have the same information about the value of the customer. They engage in a head-to-head competition and neither makes a positive pro<sup>fi</sup>t $( { \mathrm { i . e . , } } \pi _ { 1 } { = } \pi _ { 2 } { = } 0 )$ . In this regard, the service differentiation helps <sup>fi</sup>rms avoid the destructive head-to-head competition.

We next examine how service differentiation in<sup>fl</sup>uences the <sup>fi</sup>rm pro<sup>fi</sup>ts in competition. The degree of service differentiation is captured by ζ. When ζ increases, the customer segmentations for the two <sup>fi</sup>rms become more similar. Thus, the increase of $\boldsymbol { \zeta }$ reduces the service differentiation between <sup>fi</sup>rms. Proposition 4 characterizes how the change in $\zeta$ in<sup>fl</sup>uences the <sup>fi</sup>rms' expected pro<sup>fi</sup>ts.

## Proposition 4.

1. When $P r ( h ) { \leq } P r ( l )$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is always decreasing in $\zeta ;$ firm $2 \%$ expected pro<sup>fi</sup>t is always zero;

2. When $P r ( h ) { > } P r ( l )$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is increasing in ζ when $\zeta { \in } [ 0 , \operatorname* { m a x } \{ 0 , \zeta _ { 1 } \} ]$ and decreasing in $\zeta$ when $\zeta { \in } [ \operatorname* { m a x } \{ 0 , \zeta _ { 1 } \} , 1 ]$ , <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t is increasing in ζ when $\zeta \in [ 0 , \zeta _ { 2 } ]$ and decreasing in $\zeta$ when $\zeta \in [ \zeta _ { 2 } , 1 ] ,$ . The cutoff levels $\zeta _ { 1 } = \frac { \gamma - 2 \sqrt { ( 2 \gamma - 1 ) ( 1 - \gamma ) } } { 3 \gamma - 2 } <$ $\zeta _ { 2 } = \frac { 1 - 2 \sqrt { ( 1 - \gamma ) } } { 4 \gamma - 3 }$ , where $\gamma = P r ( h )$

When $P r ( h ) { \leq } P r ( l )$ , only <sup>fi</sup>rm 1 makes a positive expected pro<sup>fi</sup>t in competition (see Proposition 3). When ζ increases, <sup>fi</sup>rm 2's information is more similar to <sup>fi</sup>rm 1's information. A higher $\zeta$ leads <sup>fi</sup>rm 2 to be more con<sup>fi</sup>dent that its high-segment customer is more likely to be a high-segment customer for <sup>fi</sup>rm 1. Therefore, <sup>fi</sup>rm 2 is more willing to compete for its high-segment customer. Consequently, <sup>fi</sup>rms compete more head-to-head and <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t decreases.

When $P r ( h ) { > } P r ( l )$ , both <sup>fi</sup>rms make positive expected pro<sup>fi</sup>ts in competition when $\zeta { > } 0 . \tt A g a i n$ , the increase in ζ results in less service differentiation and more similar information for <sup>fi</sup>rms. However, Proposition 4.2 shows that <sup>fi</sup>rms' pro<sup>fi</sup>ts are not monotonically decreasing in $\zeta .$ This is because the change in ζ generates two countervailing effects on <sup>fi</sup>rm 2's competitive aggressiveness. In addition to the effect we discussed in the above paragraph, a higher ζ also generates another effect—when $\zeta$ increases, <sup>fi</sup>rm 2 is also more con<sup>fi</sup>dent that its lowsegment customer is more likely to be a low-segment customer for <sup>fi</sup>rm 1. Therefore, <sup>fi</sup>rm 2 is less willing to compete for its low-segment customer. In the case of $P r ( h ) { \leq } P r ( l )$ , only the <sup>fi</sup>rst effect exists.

Therefore <sup>fi</sup>rms' pro<sup>fi</sup>ts are never increasing in $\zeta .$ In the case of $P r ( h ) { > } P r ( l )$ , both effects exist. Whether or not <sup>fi</sup>rm 2 becomes more aggressive in general depends on the tradeoff between these two countervailing forces. When ζ is small enough, the likelihood that the customer is classi<sup>fi</sup>ed into the low segment for <sup>fi</sup>rm 2 is relatively high and thus the <sup>fi</sup>rst force is dominant. As a result, the increase in $\zeta$ makes <sup>fi</sup>rm 2 less aggressive in general. The <sup>fi</sup>rms' competition is softened. When ζ is large enough, the likelihood that the customer is classi-<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 2 is relatively high and thus the second force is dominant. As a result, the increase in $\zeta$ makes <sup>fi</sup>rm 2 more aggressive in general. The <sup>fi</sup>rms' competition is intensi<sup>fi</sup>ed.

We next illustrate the impact of information similarity $\zeta$ on the competition intensity using <sup>fi</sup>rms' expected promotional incentives. When <sup>fi</sup>rms compete more (less) aggressively, they offer higher (lower) promotional incentives. The <sup>fi</sup>rms' expected promotional incentives, $E [ m _ { 1 } ]$ and $E [ m _ { 2 } ]$ , can be used to capture the <sup>fi</sup>rms' competitive aggressiveness. $E [ m _ { 1 } ]$ and $E [ m _ { 2 } ]$ are the average levels of <sup>fi</sup>rms' promotional incentives, weighted by the probability distributions of mixed-strategies $\left( G _ { 1 } ( m | S ) \right.$ and $G _ { 2 } \left( m | \tilde { S } \right)$ and the probabilities of segmentation outcomes (Pr(S) and $P r \big ( \tilde { S } \big ) ;$ . Firms 1 and 2's overall expected promotional incentives are respectively

$$
\begin{array}{l} E \Big [ m _ {1} \Big ] = P r (h) E \Big [ m _ {1} | h \Big ] + P r (l) E \Big [ m _ {1} | l \Big ], \\ E \Big [ m _ {2} \Big ] = P r (\tilde {h}) E \Big [ m _ {2} | \tilde {h} \Big ] + P r (\tilde {l}) E \Big [ m _ {2} | \tilde {l} \Big ]. \end{array}
$$

When $P r ( h ) { \leq } P r ( l )$ , <sup>fi</sup>rms 1 and 2's expected promotional incentives given a signal are respectively

$$
E [ m _ {1} | h ] = \int_ {E [ V | l ]} ^ {E [ V | \tilde {h} ]} m d G _ {1} (m | h) \text {   and   } E [ m _ {1} | l ] = E [ V | l ],
$$

$$
\begin{array}{l} E \Big [ m _ {2} | \tilde {h} \Big ] = \int_ {E [ V | l ]} ^ {E [ V | \tilde {h} ]} m d G _ {2} \Big (m | \tilde {h} \Big) \\ \qquad + G _ {2} \Big (m | \tilde {h} \Big) \big | _ {m = E [ V | l ]} E \Big [ V | l \Big ] \\ \qquad \text { and } E \Big [ m _ {2} | \tilde {l} \Big ] = E \Big [ V | l \Big ]. \end{array}
$$

When $P r ( h ) { > } P r ( l )$ , <sup>fi</sup>rms 1 and $2 \%$ expected promotional incentives given a signal are respectively

$$
E [ m _ {1} | h ] = \int_ {E [ V | l ]} ^ {\hat {m}} m d G _ {1} (m | h) + \int_ {\hat {m}} ^ {\overline {{m}}} m d G _ {1} (m | h) \text {   and   } E [ m _ {1} | l ] = E [ V | l ],
$$

$$
\begin{array}{c} E \Big [ m _ {2} | \tilde {h} \Big ] = \int_ {\hat {m}} ^ {\overline {{m}}} m d G _ {2} \Big (m | \tilde {h} \Big) \\ \text { and } E \Big [ m _ {2} | \tilde {l} \Big ] \\ = \int_ {E [ V | l ]} ^ {\hat {m}} m d G _ {2} \Big (m | \tilde {l} \Big) + G _ {2} \Big (m | \tilde {l} \Big) \Big | _ {m = E [ V | l ]} E \Big [ V | l \Big ]. \end{array}
$$

Fig. 4 illustrates how $E [ m _ { 1 } ]$ and E[m ] change with $\zeta .$ The parameter speci<sup>fi</sup>cations used in Fig. 4 are consistent with those in the numerical examples for Propositions 1 and 2. Speci<sup>fi</sup>cally, $R = 1 0$ $\psi = 0 . 8$ , and $\phi = 0 . 2 .$ We use $\lambda { = } 0 . 4$ for Fig. $4 ( \mathsf { a } )$ and $\lambda { = } 0 . 8$ for Fig. 4(b) to better illustrate the effect. Fig. $4 ( \mathsf { a } )$ shows that both $E [ m _ { 1 } ]$ and E[m ] are always increasing in $\zeta$ when $P r ( h ) { \leq } P r ( l )$ ). Firms compete more aggressively when the level of information asymmetry becomes lower. Fig. 4(b) shows that both E[m ] and E[m ] are <sup>fi</sup>rst decreasing and then increasing in $\zeta$ when $P r ( h ) { > } P r ( l )$ . This indicates when $\zeta$ is small, the increase of $\zeta$ makes both <sup>fi</sup>rms less aggressive in offering promotional incentives. In other words, the increase of $\zeta$ softens the competition. This explains why both <sup>fi</sup>rms' expected pro<sup>fi</sup>ts are increasing in $\zeta$ when $\zeta$ is small. When ζ is large, the increase of $\zeta$ makes both <sup>fi</sup>rms more aggressive in offering promotional incentives. In other words, the increase of $\zeta$ intensi<sup>fi</sup>es the competition. This explains why both <sup>fi</sup>rms' expected pro<sup>fi</sup>ts are decreasing in $\zeta$ when $\zeta$ is large.

![](/api/attachments/WZEZFBMF/fulltext/images/2d85333b3c5cadfc2b21d178dc7e915f92875f7b168975603e32b518cdf962a8.jpg)

(b) Pr(h) > Pr(l)  
![](/api/attachments/WZEZFBMF/fulltext/images/09d32ef8ef3fc57d91fa63f9af3043a7ca3ac7712db611b6058512c2da80b002.jpg)  
Fig. 4. Firms' expected promotional incentives as a funtion $\operatorname { o f } \zeta .$

## 4. CDI service design

In this section, we consider the CDI's strategies in providing services of customer segmentation to <sup>fi</sup>rms. Given the competition equilibrium characterized in the previous sections, we consider the CDI's decision on the optimal level of similarity factor $\zeta . \ \mathrm { I f } \ \zeta = 0 , \ \tilde { S }$ does not provide additional information to <sup>fi</sup>rm 2 and <sup>fi</sup>rm 2 only knows the prior probability of valuable customer. It is equivalent to the case that the CDI serves <sup>fi</sup>rm 1 exclusively. If $\scriptstyle \phantom { + } 0 < \zeta < 1$ , <sup>fi</sup>rms have different information about the customer. It can be considered as the case that the CDI serves both <sup>fi</sup>rms but provides differentiated services. $\operatorname { I f } { \zeta } = 1$ the CDI serves both <sup>fi</sup>rms and there is no service differentiation. As a result, <sup>fi</sup>rms have the same information about the customer.

If the CDI only serves one <sup>fi</sup>rm, it can make a take-it-or-leave-it offer to <sup>fi</sup>rm 1 at a price $\pi _ { 1 }$ and let <sup>fi</sup>rm 1 decide whether or not to accept it. If <sup>fi</sup>rm 1 does not accept it, the CDI makes the same offer to <sup>fi</sup>rm 2. In equilibrium, <sup>fi</sup>rm 1 accepts the offer. The logic is as follows. As Proposition 3 shows, the <sup>fi</sup>rm with private information makes a positive pro<sup>fi</sup>t and the <sup>fi</sup>rm without private information makes zero pro<sup>fi</sup>t. If <sup>fi</sup>rm 1 rejects the offer but <sup>fi</sup>rm 2 accepts $\operatorname { i t } ,$ <sup>fi</sup>rm 1 becomes the <sup>fi</sup>rm without private information and will earn zero pro<sup>fi</sup>t in competition. If neither <sup>fi</sup>rm accepts the offer and hence neither <sup>fi</sup>rm has private information, the competition becomes Bertrand competition and both <sup>fi</sup>rms make a zero pro<sup>fi</sup>t. Therefore, <sup>fi</sup>rm 1 is willing to accept the offer. In equilibrium, the CDI earns a pro<sup>fi</sup>t $\scriptstyle { I I = \pi _ { 1 } }$ . In other words, the CDI appropriates all the surplus.

If the CDI serves both <sup>fi</sup>rms, in line with the existing literature (e.g., [4,20]), the CDI can make take-it-or-leave-it offers sequentially to the two <sup>fi</sup>rms. The CDI offers <sup>fi</sup>rm 1 a price $\pi _ { 1 }$ and then offers <sup>fi</sup>rm 2 a price $\pi _ { 2 } .$ . If one <sup>fi</sup>rm rejects the offer and the other <sup>fi</sup>rm accepts the offer, the rejecting <sup>fi</sup>rm becomes the <sup>fi</sup>rm without private information and makes a zero pro<sup>fi</sup>t in competition. If neither <sup>fi</sup>rm accepts the offer, again, the competition becomes Bertrand competition and both <sup>fi</sup>rms make a zero pro<sup>fi</sup>t. Therefore, both <sup>fi</sup>rms are willing to accept the offer. In equilibrium, the CDI's pro<sup>fi</sup>t is

$$
\Pi = \pi_ {1} + \pi_ {2}.\tag{9}
$$

The CDI again appropriates all the surplus. Proposition 5 illustrates the impact of the similarity factor $\zeta$ on the CDI's pro<sup>fi</sup>t.

## Proposition 5.

1. When $P r ( h ) { \leq } P r ( l )$ , the CDI's expected pro<sup>fi</sup>t is always decreasing in $\zeta .$

2. When $P r ( h ) { > } P r ( l )$ , the CDI's expected pro<sup>fi</sup>t is increasing in ζ when $\zeta { \in } [ 0 , \operatorname* { m a x } \{ 0 , \zeta _ { 0 } \} ]$ and decreasing in $\zeta$ when $\zeta { \in } [ \operatorname* { m a x } \{ 0 , \zeta _ { 0 } \} , 1 ]$ where $\zeta _ { 0 } = \frac { - 1 + 2 \gamma + \gamma ^ { 2 } - 2 \sqrt { ( 2 \gamma - 1 ) ( 1 - \gamma ) ( 4 \gamma ^ { 2 } + \gamma - 1 ) } } { 1 1 \gamma ^ { 2 } - 1 2 \gamma + 3 }$ and $\gamma = P r ( h )$ Moreover, $\zeta _ { 0 }$ satis<sup>fi</sup>es that $\zeta _ { 1 } { < } \zeta _ { 0 } { < } \zeta _ { 2 } .$

When $P r ( h ) { \leq } P r ( l )$ , Proposition 3 shows that only <sup>fi</sup>rm 1 earns a positive expected pro<sup>fi</sup>t in competition. Therefore, using a take-itor-leave-it offer, the CDI can appropriate <sup>fi</sup>rm 1's surplus and earn $\scriptstyle { I I = \pi _ { 1 } }$ . The CDI's expected pro<sup>fi</sup>t is always decreasing in $\zeta$ because as Proposition 4 shows, <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t (excluding the service fee) is decreasing in $\zeta .$ As a result, the CDI will choose $\zeta = 0 ,$ i.e., the CDI serves <sup>fi</sup>rm 1 exclusively and thus maximizes the information difference between <sup>fi</sup>rms.

When $P r ( h ) { > } P r ( l )$ , <sup>fi</sup>rms may both earn positive expected pro<sup>fi</sup>ts in the competition. By making take-it-or-leave-it offers to both <sup>fi</sup>rms, the CDI can appropriate both <sup>fi</sup>rms' surplus and the CDI's pro<sup>fi</sup>t is $\begin{array} { r } { I I = \pi _ { 1 } + \pi _ { 2 } . } \end{array}$ As Proposition 4 shows, when ζ is small enough, the increases of $\zeta$ may soften the <sup>fi</sup>rms' competition. When $\zeta$ is large enough, the increase of $\zeta$ intensi<sup>fi</sup>es the <sup>fi</sup>rms' competition. As a result, the CDI may bene<sup>fi</sup>t by serving both <sup>fi</sup>rms and maintaining an intermediate level of service differentiation. Proposition 5 indicates that when $\zeta _ { 0 } > 0 ,$ the CDI should serve both <sup>fi</sup>rms and differentiate the services by choosing the similarity factor $\zeta _ { 0 }$

It is worth remarking that $\frac { d \zeta _ { 0 } } { d \gamma } > 0 ,$ , i.e., the optimal level of similarity is increasing in $P r ( h )$ (note that $\gamma = P r ( h ) ,$ ). In other words, when it is more likely that the customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1, the CDI makes the two <sup>fi</sup>rms' services more similar. The rationale is that, on average, both <sup>fi</sup>rms pro<sup>fi</sup>t from the high-segment customer but not from the low-segment customer in the competition. When Pr(h) increases, by making <sup>fi</sup>rm 2's customer segmentation more similar to that of <sup>fi</sup>rm 1, the CDI can also make the customer more likely to be classi<sup>fi</sup>ed as the high-segment customer for <sup>fi</sup>rm 2. In this way, the CDI improves <sup>fi</sup>rm 2's pro<sup>fi</sup>tability and eventually appropriates more surplus from <sup>fi</sup>rm 2.

Proposition 6 characterizes how the CDI's service differentiation strategies are based on $P r ( h )$

Proposition 6. When $\begin{array} { r } { P r ( h ) { \le } \frac { \sqrt { 3 } } { 3 } , } \end{array}$ the CDI only serves <sup>fi</sup>rm 1. When $P r ( h ) > \frac { \sqrt { 3 } } { 3 } ,$ , the CDI serves both <sup>fi</sup>rms and chooses a similarity factor $\zeta _ { 0 }$ (as de<sup>fi</sup>ned in Proposition 5) to differentiate the services to <sup>fi</sup>rms.

From Proposition 5, the optimal ζ for the CDI is zero when $P r ( h ) { \leq } \frac { 1 } { 2 } ,$ and is $\boldsymbol { \mathrm { m a x } } \{ 0 , \zeta _ { 0 } \}$ when $P r ( h ) > \frac { 1 } { 2 } .$ The condition $\zeta _ { 0 } > 0$ requires that $\begin{array} { r } { P r ( h ) > \frac { \sqrt { 3 } } { 3 } . } \end{array}$ Therefore, when $0 { \leq } P r ( h ) { \leq } { \frac { \sqrt { 3 } } { 3 } } ,$ the CDI chooses $\zeta = 0 ,$ i.e., only offering an exclusive service to <sup>fi</sup>rm 1. When $\begin{array} { r } { P r ( h ) > \frac { \sqrt { 3 } } { 3 } , } \end{array}$ the CDI chooses $\zeta = \zeta _ { 0 } > 0 ,$ , i.e., the CDI serves both <sup>fi</sup>rms and differentiates the services to <sup>fi</sup>rms.

We use a numerical example to illustrate the CDI's service differentiation. Consistent with the previous numerical examples, we assume that $R = 1 0 , \psi = 0 . 8$ , and $\phi = 0 . 2$ . Fig. 5 shows how the CDI's optimal $\zeta$ changes with $P r ( h )$ . The CDI chooses $\zeta = 0 \ ( \mathrm { i . e . }$ ., serving only <sup>fi</sup>rm 1) when $P r ( h ) { \leq } \frac { \sqrt { 3 } } { 3 }$ . When $P r ( h ) > \frac { \sqrt { 3 } } { 3 }$ , the optimal $\zeta _ { 0 }$ is increasing in $P r ( h )$

Next we consider how the CDI maximizes its pro<sup>fi</sup>t by controlling the information accuracy of its services. Based on Proposition 3 and Eq. (9), the CDI's pro<sup>fi</sup>t can be represented as

$$
\begin{array}{l} \Pi = \pi_ {1} + \pi_ {2} \\ = \left\{ \begin{array}{c l} P r (h) \Big (E [ V | h ] - E [ V | \tilde {h} ] \Big), & \text { when } P r (h) \leq \frac {1}{2} \\ P r (h) \Big (E [ V | h ] - \overline {{m}} \Big) + P r (\tilde {h}) \Big (E [ V | \tilde {h} ] - \overline {{m}} \Big), & \text { when } P r (h) > \frac {1}{2}. \end{array} \right. \end{array}\tag{10}
$$

The CDI chooses ψ, $\phi ,$ and $\zeta$ to maximize its pro<sup>fi</sup>t. By adjusting ψ and ϕ, the CDI controls Pr(h) (i.e., the probability that the prospective customer is classi<sup>fi</sup>ed into the high segment for <sup>fi</sup>rm 1) because $P r ( h ) = \lambda \psi + ( 1 - \lambda ) \phi$ (please see Eq. (2)). Therefore, when ψ and ϕ are determined, the values of $P r ( h )$ and E[V|h] in $\operatorname { E q . }$ (10) are determined. By adjusting $\zeta ,$ the CDI controls to what extent the segmentation for <sup>fi</sup>rm 2 is different from the segmentation for <sup>fi</sup>rm 1 (please see Eq. (4)). When ζ is determined in addition to ψ and ϕ, the values of $E \Big [ V | \tilde { h } \Big ] , P r \Big ( \tilde { h } \Big )$ and m in Eq. (10) are also determined. As Propositions 5 and 6 indicate, the optimal ζ for the CDI is essentially dependent on $P r ( h )$ . Therefore, when ψ and ϕ are determined, the optimal ζ is also determined. The CDI's decision variables are ψ and $\phi .$ The CDI's problem is

$$
\begin{array}{l} \max _ {\{\psi , \phi \}} \Pi \\ \text { s.t.0\leq\phi<  \psi\leq 1.} \end{array}\tag{11}
$$

Proposition 7 shows how the CDI's service design depends on the market composition λ.

## Proposition 7.

1. When $0 { < } \lambda { \leq } \frac { \sqrt { 3 } } { 3 }$ , the CDI chooses $\psi = 1 , \phi = 0$ and $\zeta = 0 ;$

2. When $\frac { \sqrt { 3 } } { 3 } < \lambda \leq 1$ , the CDI chooses $\psi = 1 , \phi = 0$ and $\zeta = \zeta _ { 0 }$ in differentiating the services to <sup>fi</sup>rms.

The CDI maximizes its pro<sup>fi</sup>t by choosing $\psi = 1$ and $\phi = 0 .$ . This result is independent of the market composition λ. This implication is that if possible, the CDI always maximizes the information accuracy for the high-quality service, S. It is not optimal for CDIs to restrict the length of transaction history data for use for the high-quality services. As CDIs collect more consumer data over time, they should improve the accuracy of its target services using all available data when the cost of data storage and processing is controllable.

![](/api/attachments/WZEZFBMF/fulltext/images/8a72cc59c00d8bd513de1a83a73460fea9eb7db2117a497c91cbdcde11f4b1ab.jpg)  
Fig. 5. The optimal similarity factor $\zeta _ { 0 }$ of <sup>fi</sup>rm 2's customer segmentation.

![](/api/attachments/WZEZFBMF/fulltext/images/c81a86d6dec6f28609e98dcf316982da3835f76cc9cc1c45fc6877a33de10a0f.jpg)  
Fig. 6. The CDI's pro<sup>fi</sup>t.

Fig. 6 depicts the CDI's pro<sup>fi</sup>t. As λ increases, it is more likely that the consumer is valuable. However, the CDI's pro<sup>fi</sup>t's is not always increasing in λ even though the CDI's pro<sup>fi</sup>t comes from the valuable consumer via the <sup>fi</sup>rms. Another important factor which in<sup>fl</sup>uences the CDI's pro<sup>fi</sup>t is the competition intensity between <sup>fi</sup>rms. When $\lambda < \frac { \sqrt { 3 } } { 3 } ,$ the CDI only serves <sup>fi</sup>rm 1 exclusively and <sup>fi</sup>rm 2 has no information. Firm 1's information advantage is increasing in λ when $\lambda { \in } \left[ 0 , \frac { 1 } { 2 } \right]$ and decreasing in λ when $\lambda { \in } \left( \frac { 1 } { 2 } , \frac { \sqrt { 3 } } { 3 } \right]$ . Note that when $\lambda = { \frac { 1 } { 2 } } ,$ the market is most uncertain to the uninformed <sup>fi</sup>rm (i.e., <sup>fi</sup>rm 2) and the <sup>fi</sup>rms' competition intensity is lowest. Therefore, the CDI's pro<sup>fi</sup>t is quasiconcave in λ, achieving the maximum level when $\lambda = { \frac { 1 } { 2 } } .$

When $\lambda > { \frac { \sqrt { 3 } } { 3 } } ,$ , we have $\begin{array} { r } { P r ( h ) > \frac { \sqrt { 3 } } { 3 } . } \end{array}$ The CDI serves both <sup>fi</sup>rms and chooses a positive $\zeta _ { 0 }$ in differentiating the services to <sup>fi</sup>rms. The information disadvantage of <sup>fi</sup>rm 2 is mitigated as λ increases because the market becomes less uncertain and the CDI also provides the informative segmentation service to <sup>fi</sup>rm 2. This hurts <sup>fi</sup>rm 1's expected revenue. But the CDI's pro<sup>fi</sup>t may be increasing in λ because <sup>fi</sup>rm 2 is able to make a positive pro<sup>fi</sup>t, which may bring up the total pro<sup>fi</sup>t, in the competition. As λ approaches one, <sup>fi</sup>rm 1's information advantage diminishes because the market has little uncertainty. Consequently, the CDI's pro<sup>fi</sup>t approaches zero.

## 5. Concluding remarks

This paper studies the case where two <sup>fi</sup>rms compete in acquiring prospective customers using promotional incentives, and a CDI can provide services of customer segmentation to help <sup>fi</sup>rms better identify the value of customers. The results show that even when <sup>fi</sup>rms compete for common-value customers, they may not always compete more aggressively when they have more similar customer information. This feature of market competition provides the CDI an opportunity to serve competing <sup>fi</sup>rms. When the data service of the CDI focuses on revealing the consumers' attitudes towards the products (i.e., vertical preferences) not the brands (i.e., the horizontal preferences), e.g., in the markets for new products/services, the CDI can still soften the competition by providing <sup>fi</sup>rms with more similar information about the prospective customers.

This study also shows how the CDI can use service differentiation to endogenously create heterogeneity between <sup>fi</sup>rms and in<sup>fl</sup>uence <sup>fi</sup>rm competition. Prior analytical study has examined the use of service exclusivity to differentiate <sup>fi</sup>rms [4]. This study considers both service exclusivity and service differentiation. By providing services with different informational accuracy, the CDI can <sup>fi</sup>ne-tune the degree of <sup>fi</sup>rm differentiation when it serves multiple <sup>fi</sup>rms. The analysis in this study suggests that the CDI may adopt service exclusivity or service differentiation under different market conditions. Speci<sup>fi</sup>- cally, in unpromising markets where the majority of customers are non-valuable, the analysis suggests that it is better for the CDI to use service exclusivity. In promising markets where the majority of customers are valuable, it is better for the CDI to serve both <sup>fi</sup>rms with differentiated information services. The use of both service exclusivity and service differentiation provides the CDI more <sup>fl</sup>exibility to in<sup>fl</sup>uence the <sup>fi</sup>rms' competition.

The study also provides many other opportunities for future research. First, this study presents the insight on how the CDI uses its service to endogenously differentiate between competing <sup>fi</sup>rms. Future research may incorporate the exogenous horizontal differentiation between <sup>fi</sup>rms and consider the CDI's service strategies for ex ante heterogeneous <sup>fi</sup>rms. Such analysis with various types of <sup>fi</sup>rm differentiation may generate additional insights on the CDI's service design. Second, future research may empirically test the relationship between the market conditions and the CDI's business strategies, as predicted by this study. Third, future research may consider target marketing instruments other than targeted promotional incentives, such as targeted advertising and targeted lowest-price guarantee. Studies on the mix of these marketing strategies could generate important insights on how CDIs in<sup>fl</sup>uence <sup>fi</sup>rm competition.

## Appendix A. Proof

A.1. Proof of remark

$$
E [ V | l ] \leq E [ V | \tilde {l} ] \leq E [ V ] \leq E [ V | \tilde {h} ] \leq E [ V | h ]
$$

Proof. The customer's expected values given $S = h$ and $S = l$ are respectively

$$
E [ V | h ] = R P (H | h) \text {   and   } E [ V | l ] = R P (H | l).
$$

Since $\psi > \phi ,$ we have that $P ( H | h ) > P ( H | l )$ and $E [ V | h ] { \ge } E [ V | l ] .$ Also, since $E [ V ] = P r ( h ) E [ V | h ] + P r ( l ) E [ V | l ]$ , we have

$$
E [ V | l ] \leq E [ V ] \leq E [ V | h ].\tag{A.1}
$$

Similarly, for <sup>fi</sup>rm 2, we have the following expected values

$$
\begin{array}{l} E \Big [ V | \tilde {h} \Big ] = P \Big (h | \tilde {h} \Big) E \Big [ V | h \Big ] + P \Big (l | \tilde {h} \Big) E \Big [ V | l \Big ], \\ E \Big [ V | \tilde {l} \Big ] = P \Big (h | \tilde {l} \Big) E \Big [ V | h \Big ] + P \Big (l | \tilde {l} \Big) E \Big [ V | l \Big ]. \end{array}
$$

where $P \Big ( h | \tilde { h } \Big ) , P \Big ( h | \tilde { l } \Big ) , P \Big ( l | \tilde { h } \Big )$ , and $P \Big ( l | \tilde { l } \Big )$ are given by

$$
\begin{array}{c} P \Big [ h | \tilde {h} \Big ] = \frac {P r \Big (\tilde {h} | h \Big) P r (h)}{P r \Big (\tilde {h} | h \Big) P r (h) + P r \Big (\tilde {h} | l \Big) P r (l)} = \frac {(1 + \zeta) (\psi \lambda + \phi (1 - \lambda))}{(1 + \zeta) (\psi \lambda + \phi (1 - \lambda)) + (1 - \zeta) (1 - \psi \lambda - \phi (1 - \lambda))}, \\ P \Big [ l | \tilde {h} \Big ] = 1 - P \Big [ h | \tilde {h} \Big ], \\ P \Big [ h | \tilde {l} \Big ] = \frac {P r \Big (\tilde {l} | h \Big) P r (h)}{P r \Big (\tilde {l} | h \Big) P r (h) + P r \Big (\tilde {l} | l \Big) P r (l)} = \frac {(1 - \zeta) (\psi \lambda + \phi (1 - \lambda))}{(1 - \zeta) (\psi \lambda + \phi (1 - \lambda)) + (1 + \zeta) (1 - \psi \lambda - \phi (1 - \lambda))}, \\ P \Big [ l | \tilde {l} \Big ] = 1 - P \Big [ h | \tilde {l} \Big ]. \end{array}
$$

Since $E [ V | h ] \geq E [ V | l ] ,$ , we have

$$
E [ V | l ] \leq E [ V | \tilde {h} ] \leq E [ V | h ] \text {   and   } E [ V | l ] \leq E [ V | \tilde {l} ] \leq E [ V | h ].\tag{A.2}
$$

Comparing $P \Big [ h | \tilde { h } \Big ]$ and $P \big [ h | \tilde { l } \big ]$ , we have $P \Big [ h | \tilde { h } \Big ] \geq P \Big [ h | \tilde { l } \Big ]$ and therefore $E \Big [ V | \tilde { h } \Big ] \geq E \Big [ V | \tilde { l } \Big ]$ . Since $E [ V ] = P r \Big ( \tilde { h } \Big ) E \Big [ V | \tilde { h } \Big ] + P r \Big ( \tilde { l } \Big ) E \Big [ V | \tilde { l } \Big ]$ , we have

$$
E \left[ V | \tilde {l} \right] \leq E [ V ] \leq E [ V | \tilde {h} ].\tag{A.3}
$$

Combining Eqs. (A.1), (A.2) and (A.3), we have

$$
E \Big [ V | l \Big ] \leq E \Big [ V | \tilde {l} \Big ] \leq E \Big [ V \Big ] \leq E \Big [ V | \tilde {h} \Big ] \leq E \Big [ V \Big | h \Big ].
$$

## A.2. Proof of no pure-strategy equilibrium

Proof. Suppose that <sup>fi</sup>rm 1 and <sup>fi</sup>rm 2 offer deterministic promotional incentives. Let $m _ { h }$ and $m _ { l }$ denote <sup>fi</sup>rm 1's promotional incentive to its high-segment customer and low-segment customer, respectively. Let m ˜ and m ˜ denote <sup>fi</sup>rm $2 \%$ promotional incentive to its high-segment customer and low-segment customer, respectively. According to Remark 1, the expected value of the prospective customer is at most E[V|h]. There fore, we have $m _ { S } \le E [ V | h ] \ ( S = \{ h , l \} )$ and $m _ { \tilde { S } } \leq E [ V | h ] ~ ( \tilde { S } = \left\{ \tilde { h } , \tilde { l } \right\} )$ . Also, the expected value of the prospective customer is at least E[V|l]. Since <sup>fi</sup>rms compete for the customer, we have $m _ { S } { \geq } E [ V | l ]$ and $m \tilde { s } { \geq } E [ V | l ]$

Next we consider all possible cases that <sup>fi</sup>rms offer deterministic promotional incentives and show that none of them can be an equilibrium. (1) Suppose that <sup>fi</sup>rm 2's deterministic promotional incentives satisfy that $E [ V | l ] { \le } m _ { \tilde { l } } { < } m _ { \tilde { h } } { \le } E [ V | h ]$ . Firm 1's best response promotional incentives are $m _ { h } = m _ { \tilde { h } } + \varepsilon \mathrm { o r } m _ { \tilde { l } } + \varepsilon ,$ , and $m _ { l } { < } m _ { l }$ . When <sup>fi</sup>rm 1 responds with $m _ { h } = m _ { \tilde { h } } + \varepsilon ,$ <sup>½ j -fi</sup>rm 2 wins the customer only when the expected <sup>¼ þ</sup>value of the customer is $E [ V | l ]$ <sup>¼ þ</sup>, and thus <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t is negative. When <sup>fi</sup>rm 1 responds with $m _ { h } = m _ { \tilde { l } } + \varepsilon ,$ <sup>fi</sup>rm 2 can always increase its expected pro<sup>fi</sup>t by decreasing m˜ and just beating $m _ { h } .$ . Therefore, such deterministic $\left( m _ { \tilde { h } } , m _ { \tilde { l } } \right)$ cannot be in any equilibrium;

(2) Suppose that <sup>fi</sup>rm $2 ^ { \prime } s$ deterministic promotional incentives satisfy that $E [ V | l ] \le m _ { \tilde { h } } < m _ { \tilde { l } } \le E [ V | h ]$ . Firm 1's best-response promotional incentives are $m _ { h } = m _ { \tilde { h } } + \varepsilon \mathrm { o r } m _ { \tilde { l } } + \varepsilon ,$ and $m _ { l } { < } m _ { \tilde { h } }$ . When <sup>fi</sup>rm 1 responds with $m _ { h } = m _ { \tilde { l } } + \varepsilon ,$ <sup>fi</sup>rm 2 wins the customer only when the expected value of the customer is $E [ V | l ] ,$ and thus its expected pro<sup>fi</sup>t is negative. If <sup>fi</sup>rm 1 responds with $m _ { h } = m _ { \tilde { h } } + \varepsilon ,$ , <sup>fi</sup>rm 2 can always be better off by decreasing m and just beating $m _ { h } .$ . Therefore, such deterministic $\left( m _ { \tilde { h } } , m _ { \tilde { l } } \right)$ cannot be in any equilibrium;

(3) Suppose that <sup>fi</sup>rm 2's deterministic promotional incentives satisfy that $E [ V | l ] { < } m _ { \tilde { h } } = m _ { \tilde { l } } = \tilde { m } { < } E [ V | h ]$ . Firm 1's best-response promotional incentives are $m _ { h } = \tilde { m } + \varepsilon ,$ and $m _ { l } { < } \tilde { m }$ . Firm 2 wins the customer only when the expected value of the customer is E[V|l], and thus its expected pro<sup>fi</sup>t is negative. Therefore, such deterministic $\left( m _ { \tilde { h } } , m _ { \tilde { l } } \right)$ cannot be in any equilibrium;

(4) Suppose that <sup>fi</sup>rm 2's deterministic promotional incentives satisfy that $m _ { \tilde { h } } = m _ { \tilde { l } } = E [ V | h ]$ . Firm 1's best-response promotional incentives are $m _ { h } { \le } E [ V | h ]$ , and $m _ { l } { < } E [ V | h ] .$ . In this case, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t is always negative. Therefore, such deterministic $\left( m _ { \tilde { h } } , m _ { \tilde { l } } \right)$ cannot be in any equilibrium;

(5) Suppose that <sup>fi</sup>rm 2's deterministic promotional incentives satisfy that $m _ { \tilde { h } } = m _ { \tilde { l } } = E [ V | l ] .$ . Firm 1's best-response promotional incentives are $m _ { h } = E [ V | l ] + \varepsilon ,$ and $m _ { l } { \le } E [ V | l ]$ . <sup>fi</sup>rm 2 can always be better off by raising $m _ { \tilde { h } }$ and just beating $m _ { h } .$ Therefore, such deterministic $\left( m _ { \tilde { h } } , m _ { \tilde { l } } \right)$ cannot be in any equilibrium;

(6) Suppose that <sup>fi</sup>rm 1's deterministic promotional incentives satisfy that $m _ { h } = m _ { l } = E [ { \boldsymbol { V } } | l ]$ . Firm 2's best-response promotional incentives are $m _ { \tilde { h } } = m _ { \tilde { l } } = E [ V | l ] + \varepsilon .$ Firm 1 can always be better off by raising $m _ { h }$ and just beating firm 2's best-response. Therefore, such deterministid $( m _ { h } , m _ { l } )$ cannot be in any equilibrium;

(7) Suppose that <sup>fi</sup>rm 1's deterministic promotional incentives satisfy that $E [ V | l ] < m _ { h } < E \left[ V \middle | \tilde { h } \right]$ , and $m _ { l } = E [ { \boldsymbol { V } } | l ]$ . Firm $2 ^ { \prime } s$ best-response promotional incentives are $m _ { h } = m _ { h } + \varepsilon$ or $E [ V | l ] ,$ , and $p _ { \tilde { l } } = m _ { h } + \varepsilon$ or $E [ V | l ]$ . When <sup>fi</sup>rm 2 responds with $m _ { \tilde { h } } = m _ { h } + \varepsilon \mathrm { o r } m _ { \tilde { l } } = p _ { h } + \varepsilon ,$ , <sup>fi</sup>rm 1 can always be better off by raising $m _ { h }$ and overbidding m and m . When <sup>fi</sup>rm 2 responds with $m _ { \tilde { h } } = m _ { \tilde { l } } = E [ V | l ]$ , <sup>fi</sup>rm 1 can always be better off by lowering $m _ { h }$ and just overbidding m and m . Therefore, such deterministic $( m _ { h } , m _ { l } )$ cannot be in any equilibrium;

(8) Suppose that <sup>fi</sup>rm 1's deterministic promotional incentives satisfy that $E \big [ V \big | \tilde { h } \big ] \leq m _ { h } \leq E [ V | h ]$ , and $m _ { l } = E [ { \boldsymbol { V } } | l ]$ ]. Firm 2's best-response promotional incentives are $m _ { \tilde { h } } = m _ { \tilde { l } } = E [ V | l ]$ . Firm 1 can always be better off by decreasing $m _ { h }$ and just beating $m _ { h }$ and m˜. Therefore, such de terministic $( m _ { h } , m _ { l } )$ cannot be in any equilibrium

Considering $( 1 ) \AA - \left( 8 \right)$ , we conclude that there is no pure-strategy equilibrium.

## A.3. Proof of Proposition 1

Proof. Let $\pi _ { 1 } ( m _ { 1 } | h )$ and $\pi _ { 1 } ( m _ { 1 } | l )$ denote <sup>fi</sup>rm 1's expected pro<sup>fi</sup>ts of offering a promotional incentive $m _ { 1 }$ for its high-segment customer $( S = h )$ and its low-segment customer $( S = l )$ respectively. Let $\pi _ { 2 } \Big ( m _ { 2 } \Big | \tilde { h } \Big )$ and $\pi _ { 2 } \Big ( m _ { 2 } \Big | \tilde { l } \Big )$ denote <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t of offering a promotional incen tive $m _ { 2 }$ for its high-segment customer $( \tilde { S } = \tilde { h } )$ and its low-segment customer $( \tilde { S } = \tilde { l } )$ respectively.

For the mixed-strategy equilibrium, we <sup>fi</sup>rst consider the support ranges of <sup>fi</sup>rms' randomized promotional incentives. Let $\overline { { m } } _ { 1 S }$ and $m _ { 1 S }$ denote <sup>fi</sup>rm 1's upper bound and lower bound of promotional incentives respectively for its customer in the two segments $S { \in } \{ h , l \} .$ . Let $\overline { { m } } _ { 2 \widetilde { \varsigma } }$ and $m _ { 2 \tilde { S } }$ denote <sup>fi</sup>rm 2's upper bound and lower bound of promotional incentives respectively for its customer in the two segments, $\tilde { S } { \in } \{ \tilde { h } , \tilde { \bar { l } } \}$ . Regarding the values of these bounds, we can immediately conclude three boundary conditions:

Boundary Condition 1: $\underline { { m } } _ { 1 S } \underline { { > } } E [ V | l ] , \underline { { m } } _ { 2 \tilde { S } } \underline { { > } } E [ V | l ]$ . Since the lowest expected value is $E [ V | l ]$ and <sup>fi</sup>rms compete with each other to win the con sumer, no one will offer lower than E[V|l] .

Boundary Condition $2 \colon \overline { { { m } } } _ { 1 S } \underline { { { < } } } E [ V | S ] , \ : \overline { { { m } } } _ { 2 \tilde { S } } \underline { { { < } } } E \lceil V \rceil \tilde { S } |$ . That ${ \mathrm { i } } s ,$ a <sup>fi</sup>rm will not offer a promotional incentive higher than its expected value of the customer.

Boundary Condition 3: max $\{ \overline { { { m } } } _ { 1 h } , \overline { { { m } } } _ { 1 l } \} = m a x \{ \overline { { { m } } } _ { 2 \tilde { h } } , \overline { { { m } } } _ { 2 \tilde { l } } \}$

Lemma A1. Firm 1 always offers a deterministic promotional incentive $E [ V | l ]$ for its low-segment customer $( S { = } l )$ . In other word, $\underline { m } _ { 1 l } = \overline { m } _ { 1 l } = E [ V | l ]$

Proof. For its low-segment customer $( S = l ) ,$ , <sup>fi</sup>rm 1's expected value of the customer is E[V|l]. Firm 1 will not offer any promotional incentive above E[V|l]. That is, $\overline { { m } } _ { 1 l } { \leq } E [ V | l ]$ . Boundary Condition 1 indicates that $\underline { m } _ { 1 l } { \geq } E [ V | l ]$ . Therefore, we can conclude that $\underline { m } _ { 1 l } = \overline { m } _ { 1 l } = E [ V | l ]$ and <sup>fi</sup>rm 1 offers a <sup>½ j -</sup>deterministic promotional incentive to its low-segment customer $( S { = } l )$ <sup>j -</sup>. That is, $G _ { 1 } ( m | l ) = \{ 0 , m { < } E [ V | l ] 1 , m { \geq } ~ E [ V | l ]$ . In this case, <sup>fi</sup>rm 1 makes a zero expected pro<sup>fi</sup>t from the low-segment, i.e., $\pi _ { 1 } ( m _ { 1 } | l ) = 0$

Using the result of Lemma A1, we can simplify Boundary Condition 3 tom $\tilde { \mathbf { \Gamma } } _ { 1 h } = m a x \{ \overline { { m } } _ { 1 h } , \overline { { m } } _ { 1 l } \} = m a x \{ \overline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } \}$ and the <sup>fi</sup>rms' pro<sup>fi</sup>t functions as

$$
\pi_ {1} (m _ {1} | h) = \operatorname * {P r} (\tilde {h} | h) G _ {2} (m _ {1} | \tilde {h}) (E [ V | h ] - m _ {1}) + \operatorname * {P r} (\tilde {l} | h) G _ {2} (m _ {1} | \tilde {l}) (E [ V | h ] - m _ {1}),\tag{A.4}
$$

$$
\pi_ {2} \left(m _ {2} \mid \tilde {h}\right) = P (h \mid \tilde {h}) G _ {1} \left(m _ {2} \mid h\right) \left(E [ V | h ] - m _ {2}\right) + P (l \mid \tilde {h}) \left(E [ V | l ] - m _ {2}\right),\tag{A.5}
$$

$$
\pi_ {2} \left(m _ {2} | \tilde {l}\right) = P (h | \tilde {l}) G _ {1} (m _ {2} | h) (E [ V | h ] - m _ {2}) + P (l | \tilde {l}) (E [ V | l ] - m _ {2}).\tag{A.6}
$$

Lemma A2. Firm 2's upper bound of the promotional incentive for its low-segment customer $( \tilde { S } = \tilde { l } )$ is also its lower bound of the promotional incentive for its high-segment customer $( \tilde { S } = \tilde { h } )$ . We define this level as m^ , i.e., m^ $\underline { m } _ { 2 \tilde { h } } = \overline { m } _ { 2 \tilde { l } } .$

Proof. We <sup>fi</sup>rst prove that we cannot have $\underline { { m } } _ { 2 \widetilde { h } } { < } \overline { { m } } _ { 2 \widetilde { l } }$ and then prove that we cannot have $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } } .$

Suppose $\underline { m } _ { 2 \tilde { h } } { < } \overline { m } _ { 2 \tilde { l } } .$ . The supports of $G _ { 2 } \Big ( m | \tilde { h } \Big ) \mathrm { a n d } G _ { 2 } \Big ( m | \tilde { l } \Big )$ overlap on $[ \underline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } ]$ . In the mixed-strategy equilibrium, from a high-segment customer $( \tilde { S } = \tilde { h } )$ , <sup>fi</sup>rm 2 always makes a constant expected pro<sup>fi</sup>t $\pi _ { 2 } \Big ( m _ { 2 } | \tilde { h } \Big )$ when offering any promotional incentive $m _ { 2 } { \in } [ \underline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } ]$ . Similarly, from a low-segment customer $( \tilde { S } = \tilde { l } )$ , <sup>fi</sup>rm 2 always makes a constant expected pro<sup>fi</sup>t $\pi _ { 2 } \left( m _ { 2 } | { \tilde { l } } \right)$ when offering any promotional incentive $m _ { 2 } { \in } [ \underline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } ]$ Therefore, $\pi _ { 2 } \Big ( m _ { 2 } | \tilde { h } \Big ) - \pi _ { 2 } \Big ( m _ { 2 } | \tilde { l } \Big )$ should be constant for any $m _ { 2 } { \in } [ \underline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } ]$

$$
\begin{array}{l} \pi_ {2} (m _ {2} | \tilde {h}) - \pi_ {2} (m _ {2} | \tilde {l}) = \Big (P \Big (h | \tilde {h} \Big) - P \Big (h | \tilde {l} \Big) \Big) G _ {1} (m _ {2} | h) (E [ V | h ] - m _ {2}) \\ \qquad + \Big (P \Big (l | \tilde {h} \Big) - P \Big (l | \tilde {l} \Big) \Big) (E [ V | l ] - m _ {2}) \\ \qquad = \Big (P \Big (h | \tilde {h} \Big) - P \Big (h | \tilde {l} \Big) \Big) \binom{G _ {1} (m _ {2} | h) E [ V | h ] (7)}{+ (1 - G _ {1} (m _ {2} | h)) m _ {2} - E [ V | l ]}. \end{array}\tag{A.7}
$$

$\pi _ { 2 } \Big ( m _ { 2 } | \tilde { h } \Big ) - \pi _ { 2 } \Big ( m _ { 2 } | \tilde { l } \Big )$ being constant requires that $G _ { 1 } ( m _ { 2 } | h ) E [ V | h ] + ( 1 - G _ { 1 } ( m _ { 2 } | h ) ) m _ { 2 } - E [ V | l ]$ is also constant, Suppose that $G _ { 1 } ( m _ { 2 } | h ) E [ V | h ] + ( 1 -$ $G _ { 1 } ( m _ { 2 } | h ) ) m _ { 2 } - E [ V | l ] = C$ for any $m _ { 2 } { \in } [ \underline { { m } } _ { 2 \tilde { h } } , \overline { { m } } _ { 2 \tilde { l } } ]$ , we have $G _ { 1 } ( m _ { 2 } | h ) = \frac { C + E [ V | l ] - m _ { 2 } } { E [ V | h ] - m _ { 2 } } \operatorname { a n d } \frac { d G _ { 1 } ( m _ { 2 } | h ) } { d m _ { 2 } } = \frac { C + E [ V | l ] - E [ V | h ] } { \left( E [ V | h ] - m _ { 2 } \right) ^ { 2 } }$ . Since $m _ { 2 } { < } E [ V | h ] ,$ , we have

$G _ { 1 } ( m _ { 2 } | h ) E [ V | h ] + ( 1 - G _ { 1 } ( m _ { 2 } | h ) ) m _ { 2 } { < } E [ V | h ]$ and hence $C { < } E [ V | h ] - E [ V | l ] .$ . Therefore, $\frac { d G _ { 1 } ( m _ { 2 } | h ) } { d m _ { 2 } } = \frac { C + E [ V | l ] - E [ V | h ] } { \left( E [ V | h ] - m _ { 2 } \right) ^ { 2 } } < 0 \ \cdot$ , which indicates that the cumulative probability function $G _ { 1 } ( m _ { 2 } | h )$ is decreasing. However, this cannot be true since a cumulative probability function is nondecreasing. Therefore, we cannot have $\underline { { m } } _ { 2 \widetilde { h } } { < } \overline { { m } } _ { 2 \widetilde { l } }$

We next prove that we cannot have $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } } .$ . Suppose $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } } .$ When $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } } ,$ , there is a gap between the supports for $G _ { 2 } \left( m | { \tilde { h } } \right)$ and $G _ { 2 } \left( m | \tilde { l } \right)$ . As a result, <sup>fi</sup>rm 1 will never offer a promotional incentive $m _ { 1 } { \in } ( \overline { { m } } _ { 2 \tilde { l } } , \underline { { m } } _ { 2 \tilde { h } } )$ . Firm 1 will not offer $m _ { 1 } = \underline { m } _ { 2 \tilde { h } }$ either. This is because $\overline { { m } } _ { 2 \widetilde { l } }$ and $\underline { m } _ { 2 \tilde { h } }$ lead to the same probability of winning but <sup>fi</sup>rm 1 pays more at $\underline { m } _ { 2 \tilde { h } }$ . As a result, <sup>fi</sup>rm 2 will also never offer $m _ { 2 } = \underline { m } _ { 2 \tilde { h } }$ , which contradicts the fact that $\underline { m } _ { 2 \tilde { h } }$ is <sup>fi</sup>rm 2's lower bound of randomization. Therefore, we cannot have $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } }$

Overall, we exclude both $\underline { { m } } _ { 2 \tilde { h } } { < } \overline { { m } } _ { 2 \tilde { l } }$ and $\underline { m } _ { 2 \tilde { h } } > \overline { m } _ { 2 \tilde { l } } .$ . The only possibility is $\underline { m } _ { 2 \tilde { h } } = \overline { m } _ { 2 \tilde { l } } .$

Lemma A3. m is not lower than the lower bound of promotional incentive distribution of^ firm 1 for its high-segment customer $( S = h ) , \mathrm { i . e . , } \hat { m } \geq \underline { m } _ { 1 h }$

Proof. Suppose $\hat { m } { < } m _ { 1 h } .$ . If <sup>fi</sup>rm 2 offers any promotional incentive $m _ { 2 } \in ( \hat { m } , \underline { { { m } } } _ { 1 h } )$ , it only wins the customer when the customer is classi<sup>fi</sup>ed as a low-segment customer for <sup>fi</sup>rm 1 $( S { = } l )$ and hence earns a negative pro<sup>fi</sup>t. Therefore, $\hat { m } \ge \underline { m } _ { 1 h }$

Lemma A4. Firm 1's upper bound of promotional incentive for its high-segment customer $( S = h )$ is equal to firm 2's upper bound of promotional incentive for firm 2's high-segment $( \tilde { S } = \tilde { h } )$ . We define this level as $\overline { { m } } _ { 1 }$ . There is no mass point at m for both firms' promotional incentive distributions. That is, $\overline { { { m } } } _ { 1 } \triangleq \overline { { { m } } } _ { 1 h } = \overline { { { m } } } _ { 2 \widetilde { h } } \ a n d \ G _ { 1 } ( \overline { { { m } } } _ { 1 } | h ) = G _ { 2 } \Big ( \overline { { { m } } } _ { 1 } | \widetilde { h } \Big ) = 1 .$

Proof. It is straightforward that $\overline { { { m } } } _ { 2 \tilde { h } } = \overline { { { m } } } _ { 1 h } .$ . We de<sup>fi</sup>ne $\overline { { m } } _ { 1 } \triangleq \overline { { m } } _ { 1 h } = \overline { { m } } _ { 2 \tilde { h } }$ . From Boundary Condition 2, we have $\overline { { m } } _ { 1 } { \leq } E { \left[ V | \tilde { h } \right] }$

We next prove that <sup>fi</sup>rms put no mass point at $\overline { { m } } _ { 1 }$ . Suppose that <sup>fi</sup>rm 2 puts a mass point at m . Firm 1 has an incentive to increase $m _ { 1 } \mathrm { t o } \overline { { m } } _ { 1 }$ + ε to beat <sup>fi</sup>rm 2. Therefore, $\overline { { m } } _ { 1 }$ is not the upper bound of <sup>fi</sup>rms' promotional incentives.

Suppose <sup>fi</sup>rm 2 does not have a mass point atm but <sup>fi</sup>rm 1 does. We have $G _ { 1 } ( \overline { { m } } _ { 1 } | h ) { < } 1 . \operatorname { I f } \overline { { m } } _ { 1 } { < } E \Big [ V | \tilde { h } \Big ]$ , <sup>fi</sup>rm 2 has an incentive to increase $m _ { 2 } \tan _ { 1 } + \varepsilon$ to beat <sup>fi</sup>rm 1. Therefore, $\overline { { m } } _ { 1 }$ is not the upper bound of <sup>fi</sup>rms' promotional incentives. $\mathrm { I f } \overline { { m } } _ { 1 } = E \Big \vert V \vert \tilde { h } \Big \vert$ <sup>i</sup>, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t when offering $\overline { { m } } _ { 1 }$ is

$$
\begin{array}{l} \pi_ {2} \Big (\overline {{m}} _ {1} | \tilde {h} \Big) = P \Big (h | \tilde {h} \Big) G _ {1} (\overline {{m}} _ {1} | h) (E [ V | h ] - \overline {{m}} _ {1}) + P \Big (l | \tilde {h} \Big) (E [ V | l ] - \overline {{m}} _ {1}), \\ \qquad <   P \Big (h | \tilde {h} \Big) (E [ V | h ] - \overline {{m}} _ {1}) + P \Big (l | \tilde {h} \Big) (E [ V | l ] - \overline {{m}} _ {1}), \\ \qquad = E \Big [ V | \tilde {h} \Big ] - \overline {{m}} _ {1} \\ \qquad = 0. \end{array}
$$

In other words, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t is negative. Therefore, we cannot have <sup>fi</sup>rm 1 putting a mass point at $\overline { { m } } _ { 1 }$ either.

$$
G _ {1} (\overline {{m}} _ {1} | h) = G _ {2} \left(\overline {{m}} _ {1} | \tilde {h}\right) = 1
$$

So far, we can conclude that:

1. The support for $G _ { 2 } \left( m | \tilde { l } \right) \mathrm { i } s \left[ \underline { { m } } _ { 2 \tilde { l } } , \hat { m } \right]$

2. The support for $G _ { 2 } \left( m | { \tilde { h } } \right) { \mathrm { i s } } [ { \hat { m } } , { \overline { { m } } } _ { 1 } ] ;$

3. The support for $G _ { 1 } ( m | h ) { \mathrm { ~ i s ~ } } [ { \underline { { m } } } _ { 1 h } , { \overline { { m } } } _ { 1 } ] .$

We next consider <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t in competition. We <sup>fi</sup>rst show that $\pi _ { 2 } \Big ( m | \tilde { l } \Big ) = 0 ,$ , i.e., <sup>fi</sup>rm 2 cannot make a positive expected pro<sup>fi</sup>t when ${ \boldsymbol { \tilde { S } } } = { \boldsymbol { \tilde { l } } } .$ We next consider <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t when $\tilde { S } = \tilde { h }$ . Prior literature suggests that when competing with a better-informed <sup>¼ ¼</sup>competitor, the less-informed competitor earns a zero expected pro<sup>fi</sup>t in the mixed-strategy equilibrium (e.g. Engelbrecht-Wiggans et al. 1983). We use this key <sup>fi</sup>nding to form two conjectures on the expected pro<sup>fi</sup>ts of <sup>fi</sup>rm 2 (the less informed <sup>fi</sup>rm) when $\tilde { S } = \tilde { h }$

Lemma A5.

$$
\pi_ {2} (m | \tilde {l}) = 0.
$$

Proof. Suppose $\pi _ { 2 } \left( m | \tilde { l } \right) > 0$ . From Eq. (A.6), we have

$$
\pi_ {2} \left(\underline {{m}} _ {2 \tilde {l}} | \tilde {l}\right) = P (h | \tilde {l}) G _ {1} \left(\underline {{m}} _ {2 \tilde {l}} | h\right) (E [ V | h ] - \underline {{m}} _ {2 \tilde {l}}) + P (l | \tilde {l}) (E [ V | l ] - \underline {{m}} _ {2 \tilde {l}}) > 0.
$$

Considering Boundary Conditions 1 and 2, we have $P \left( l | l \right) \left( E [ V | l ] - \underline { { m } } _ { 2 \tilde { l } } \right) \leq 0$ . Therefore, to satisfy $\pi _ { 2 } \Big ( \underline { { m } } _ { 2 \tilde { l } } | \tilde { l } \Big ) > 0$ , we must have $G _ { 1 } \left( \underline { { m } } _ { 2 \tilde { l } } | h \right) > 0$ $G _ { 1 } \left( \underline { { m } } _ { 2 \tilde { l } } | h \right)$ is positive only when either of the following cases is true: (1) $\underline { { { m } } } _ { 1 h } { < } \underline { { { m } } } _ { 2 \tilde { l } } ; ( 2 ) \underline { { { m } } } _ { 1 h } = \underline { { { m } } } _ { 2 \tilde { l } }$ and <sup>fi</sup>rm 1 has a mass point at $\underline { m } _ { 2 \tilde { l } } .$ We next show that the <sup>fi</sup>rst case $\underline { m } _ { 1 h } { < } \underline { m } _ { 2 \tilde { l } }$ cannot be true. If $\underline { m } _ { 1 h } < \underline { m } _ { 2 \tilde { l } }$ is true, <sup>fi</sup>rm 1 makes a zero expected pro<sup>fi</sup>t when offering $m _ { 1 } = \underline { m } _ { 1 h }$ and S=h. However, Boundary Condition 2 suggests that <sup>fi</sup>rm 2 always offers a promotional incentivem $\le E \left[ V | \tilde { h } \right]$ , which is lower than E[V|h]. When S= h, <sup>fi</sup>rm 1 can make a positive pro<sup>fi</sup>t at least by offeringm $ _ { 1 } = E \Big \lceil V \| \tilde { h } \Big \rceil + \varepsilon$ . Therefore, <sup>fi</sup>rm 1 should make a positive pro<sup>fi</sup>t at ${ \underline { { m } } } _ { 1 h }$ when S=h. Therefore, the case, Xm $. 1 h ^ { < } \ : \underline { { m } } _ { 2 \tilde { l } } ,$ , cannot be true.

We next show that the second case, i.e., $\underline { m } _ { 1 h } = \underline { m } _ { 2 \tilde { l } }$ and <sup>fi</sup>rm 1 has a mass point at $\underline { m } _ { 2 \tilde { l } }$ cannot be true. Because <sup>fi</sup>rms cannot both have a mass point at a boundary simultaneously in equilibrium, if <sup>fi</sup>rm 1 has a mass point at $\underline { m } _ { 1 h } = \underline { m } _ { 2 \tilde { l } } ,$ we must have $G _ { 2 } \bigg ( \underline { m } _ { 1 h } | \tilde { h } \bigg ) = 0$ and $G _ { 2 } \Big ( \underline { { m } } _ { 1 h } | \tilde { l } \Big ) = 0$ Considering Eq. (A.4), we have

$$
\pi_ {1} \left(\underline {{m}} _ {1 h} | h\right) = P r (\tilde {h} | h) G _ {2} \left(\underline {{m}} _ {1 h} | \tilde {h}\right) \left(E [ V | h ] - \underline {{m}} _ {1 h}\right) + P r (\tilde {l} | h) G _ {2} \left(\underline {{m}} _ {1 h} | \tilde {l}\right) \left(E [ V | h ] - \underline {{m}} _ {1 h}\right).
$$

If $\dot { G } _ { 2 } \Bigl ( \underline { m } _ { 1 h } | \tilde { h } \Bigr ) = 0 \mathrm { a n d } G _ { 2 } \Bigl ( \underline { m } _ { 1 h } | \tilde { l } \Bigr ) = 0 ,$ , we must have that $\pi _ { 1 } ( \underline { { m } } _ { 1 h } | h ) \mathrm { i }$ s always zero and therefore <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t when $S = h$ is always zero. However, this cannot be true as we proved above. Therefore, the second case cannot be true.

In conclusion, <sup>fi</sup>rm 2 must make a zero expected pro<sup>fi</sup>t when $\tilde { S } = \tilde { l } , \mathrm { i . e . , } \pi _ { 2 } \Big ( m | \tilde { l } \Big ) = 0$

Next, we develop the following conjectures:

Conjecture 1: For $m _ { 2 } { \in } [ \underline { { { m } } } _ { 2 \tilde { l } } , \hat { m } ] , \pi _ { 2 } \Big ( m _ { 2 } { \vert } \tilde { l } \Big ) = 0$ and for $m _ { 2 } { \in } [ \hat { m } , \overline { { { m } } } _ { 1 } ] , ~ \pi _ { 2 } \Big ( m _ { 2 } { \vert } \tilde { h } \Big ) = 0$ . In other words, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>ts from its low-segment customer $( \tilde { S } = \tilde { l } )$ and high-segment customer $( \tilde { S } = \tilde { h } )$ are always zero;

Conjecture 2: For $m _ { 2 } { \in } \bigl [ \underline { { m } } _ { 2 l } ; \hat { m } \bigr ] , \pi _ { 2 } \Bigl ( m _ { 2 } | \tilde { l } \Bigr ) = 0 \mathrm { a n d f o r } m _ { 2 } { \in } [ \hat { m } , \overline { { m } } _ { 1 } ] , \pi _ { 2 } \Bigl ( m _ { 2 } | \tilde { h } \Bigr ) > 0$ : In other words, <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t from its low-segment customer $( \tilde { S } = \tilde { l } )$ is always zero, but that from its high-segment customer $( \tilde { S } = \tilde { h } )$ may be zero or positive.

We will <sup>fi</sup>rst use Conjecture 1 to derive the equilibrium in Proposition 1. Conjecture 2 will be used to derive the equilibrium in Proposition 2. Based on Coniecture 1 we have $\pi _ { 2 } \Bigl ( m | \tilde { h } \Bigr ) = P \Bigl ( h | \tilde { h } \Bigr ) G _ { 1 } ( m | h ) ( E [ V | h ] - m ) + P \Bigl ( l | \tilde { h } \Bigr ) ( E [ V | l ] - m ) = 0$ (please see Eq. (5)), we have

$$
G _ {1} (m | h) = \frac {P (l | \tilde {h}) (m - E [ V | l ])}{P (h | \tilde {h}) (E [ V | h ] - m)}.\tag{A.8}
$$

Lemma A6.

$$
\overline {{m}} _ {1} = E \left[ V \mid \tilde {h} \right].
$$

Proof. By Lemma A4 and (A.8), we have $\begin{array} { r } { G _ { 1 } ( \overline { { m } } _ { 1 } | h ) = \frac { P \left( l | \tilde { h } \right) ( \overline { { m } } _ { 1 } - E [ V | l ] ) } { P \left( h | \tilde { h } \right) ( E [ V | h ] - \overline { { m } } _ { 1 } ) } = 1 } \end{array}$ . Therefore, $\overline { { { m } } } _ { 1 } = P \Big ( h | \tilde { h } \Big ) E [ V | h ] + P \Big ( l | \tilde { h } \Big ) E [ V | l ] = E \Big [ V | \tilde { h } \Big ]$

Lemma A7. $\hat { m } = \overline { { { m } } } _ { 2 \tilde { l } } = \underline { { { m } } } _ { 2 \tilde { h } } = \underline { { { m } } } _ { 1 h } = E [ V | l ]$ and $G _ { 1 } ( m | h ) | _ { m = E [ V | l ] } = 0 .$

Proof. Suppose $\underline { m } _ { 1 h } > E [ V | l ]$ . From Lemma A3, we must have m^ ≥ $\underline { m } _ { 1 h } > E [ V | l ]$ . We plug (A.8) into (A.6) and replace m with m^ , we have

$$
\begin{array}{l} \pi_ {2} \Big (\hat {m} | \tilde {l} \Big) = P \Big (h | \tilde {l} \Big) \frac {P \Big (l | \tilde {h} \Big) (\hat {m} - E [ V | l ])}{P \Big (h | \tilde {h} \Big) (E [ V | h ] - \hat {m})} (E [ V | h ] - \hat {m}) + P \Big (l | \tilde {l} \Big) (E [ V | l ] - \hat {m}) \\ = \left(\frac {P \Big (h | \tilde {l} \Big) P \Big (l | \tilde {h} \Big) - P \Big (l | \tilde {l} \Big) P \Big (h | \tilde {h} \Big)}{P \Big (h | \tilde {h} \Big)}\right) (\hat {m} - E [ V | l ]). \end{array}
$$

Because $P \Big ( h | \tilde { l } \Big ) P \Big ( l | \tilde { h } \Big ) { < } P \Big ( l | \tilde { l } \Big ) P \Big ( h \Big | \tilde { h } \Big )$ , we have $\pi _ { 2 } \left( \hat { m } | \tilde { l } \right) { < } 0$ . This contradicts the fact that $\pi _ { 2 } \left( \hat { m } | \tilde { l } \right) { \geq } 0$ . To ensure that $\pi _ { 2 } \Big ( \hat { m } | \tilde { l } \Big ) = 0$ ; we must have $\hat { m } = E [ V | l ]$ . Then we also have $\underline { { { m } } } _ { 1 h } = \underline { { { m } } } _ { 2 \tilde { h } } = \overline { { { m } } } _ { 2 \tilde { l } } = E [ V | l ]$ . It is easy to verify that $G _ { 1 } ( \underline { { m } } _ { 1 h } | h ) = 0$ . Therefore, $G _ { 1 } ( m | h )$ has no mass point at ${ \underline { { m } } } _ { 1 h } .$ . We can conclude that <sup>fi</sup>rm 2 offers $m _ { 2 } = E [ { \cal { V } } | l ]$ to its low-segment customer $( S = \tilde { l } )$ . That is, $G _ { 2 } \Big ( m | \tilde { l } \Big ) = \{ 0 , m { \it \mathrm { < } } E [ V | l ] 1$ ; m≥E V l :

We can rewrite <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t from its high-segment customer, given any promotional incentive, as

$$
\pi_ {1} (m _ {1} | h) = \operatorname * {P r} (\tilde {h} | h) G _ {2} (m _ {1} | \tilde {h}) (E [ V | h ] - m _ {1}) + \operatorname * {P r} (\tilde {l} | h) (E [ V | h ] - m _ {1}).\tag{A.9}
$$

Using Lemma A4 and A6, we can conclude that <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is $\pi _ { 1 } ( m _ { 1 } | h ) = E [ V | h ] { - } E \big [ V | \tilde { h } \big ]$ from its high-segment customer. There fore, we have

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - E [ V | \tilde {h} ] - P r (\tilde {l} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}.\tag{A.10}
$$

Combining the results in Lemma A1, Lemma A7, Eq. (9), and Eq. (11), when $P r ( h ) { \leq } P r ( l )$ and $\zeta < 1$ , the <sup>fi</sup>rms' equilibrium strategies can be characterized as follows:

1. For its low-segment customer (S = l), <sup>fi</sup>rm 1 offers E[V|l];

2. For its low-segment customer (S<sup>˜</sup> <sup>˜</sup>l), <sup>fi</sup>rm 2 offers E[V|l];

3. For its high-segment customer $( S = h )$ , the CDF of <sup>fi</sup>rm 1's promotional incentive is

$$
G _ {1} (m | h) = \frac {P (l | \tilde {h}) (m - E [ V | l ])}{P (h | \tilde {h}) (E [ V | h ] - m)}, m \in \left[ E [ V | l ], E [ V | \tilde {h} ] \right];
$$

4. For its high-segment customer $( S = \tilde { h } )$ , the CDF of <sup>fi</sup>rm 2's promotional incentive is

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - E [ V | \tilde {h} ] - P r (\tilde {l} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}, m \in [ E [ V | l ], E [ V | \tilde {h} ] ].
$$

We can verify that $G _ { 1 } ( m | h ) \Big | _ { m = E \left[ V | \tilde { h } \right] } \leq 1 , G _ { 1 } \left( m | h \right) \big | _ { m = E \left[ V | l \right] } \geq 0 , G _ { 2 } \left( m | \tilde { h } \right) \Big | _ { m = E \left[ V | \tilde { h } \right] } \leq 1 ,$ , and $G _ { 2 } \Big ( m | \tilde { h } \Big ) \Big | _ { m = E | V | l | } \geq 0$ hold if and only if $P r ( h ) { \leq } P r ( l )$ . In other words, $P r ( h ) { \leq } P r ( l )$ <sup>¼</sup>is a suf<sup>fi</sup>cient and necessary condition of the existence of this equilibrium.

## A.4. Proof of Proposition 2

Proof. We consider the case $P r ( h ) { > } P r ( l )$ . In the proof of Proposition 1, we used Conjecture 1 to derive the equilibrium. We also showed that the equilibrium in Proposition 1 exists if and only if $P r ( h ) { \leq } P r ( l )$ . In the following proof, we will use Conjecture 2 to derive the equilibrium when $P r ( h ) { > } P r ( l )$

We will show that there exists a mixed-strategy equilibrium that <sup>fi</sup>rm 2 randomizes over $[ \hat { m } , \overline { { m } } ]$ for its high-segment customer and over Xm ; m^ for its low-segment customer. Firm 1 randomizes over $[ \underline { { m } } _ { 2 } , \overline { { m } } ]$ for its high-segment customer. The cutoff levels ${ \underline { { m } } } _ { 2 }$ ; m^ and m are to <sup>½ -</sup>be determined

Lemma A5 indicates that $\pi _ { 2 } \Big ( m _ { 2 } | \tilde { l } \Big ) = 0 , \mathrm { i . e . }$ , in the mixed-strategy equilibrium, <sup>fi</sup>rm 2 earns zero expected pro<sup>fi</sup>t from its low-segment customer. From $\pi _ { 2 } \Bigl ( m _ { 2 } | \tilde { l } \Bigr ) = P \Bigl ( h | \tilde { l } \Bigr ) G _ { 1 } ( m _ { 2 } | h ) ( E [ V | h ] - m _ { 2 } ) + P \Bigl ( l | \tilde { l } \Bigr ) \times ( E [ V | l ] - m _ { 2 } ) = 0 , m { \in } [ \underline { { m } } _ { 2 } , \hat { m } ] ,$ , we have

$$
G _ {1} (m | h) = \frac {P (l | \tilde {l}) (m - E [ V | l ])}{P (h | \tilde {l}) (E [ V | h ] - m)}, m \in [ \underline {{m}} _ {2}, \hat {m} ].\tag{A.11}
$$

Considering Lemma A4 and the constant expected pro<sup>fi</sup>ts of <sup>fi</sup>rms in the mixed-strategy equilibrium, we have

$$
\begin{array}{l} \pi_ {2} \Big (m _ {2} | \tilde {h} \Big) = P \Big (h | \tilde {h} \Big) G _ {1} (m _ {2} | h) (E [ V | h ] - m _ {2}) + P \Big (l | \tilde {h} \Big) (E [ V | l ] - m _ {2}) = E \Big [ V | \tilde {h} \Big ] - \overline {{m}}, m \in [ \hat {m}, \overline {{m}} ], \\ \pi_ {1} (m _ {1} | h) = P r \Big (\tilde {h} | h \Big) G _ {2} \Big (m _ {1} | \tilde {h} \Big) (E [ V | h ] - m _ {1}) + P r \Big (\tilde {l} | h \Big) (E [ V | h ] - m _ {1}) = E [ V | h ] - \overline {{m}}, m \in [ \hat {m}, \overline {{m}} ], \\ \pi_ {1} (m _ {1} | h) = P r \Big (\tilde {l} | h \Big) G _ {2} \Big (m _ {1} | \tilde {l} \Big) (E [ V | h ] - m _ {1}) = E [ V | h ] - \overline {{m}}, m \in [ \underline {{m}} _ {2}, \hat {m} ]. \end{array}
$$

We therefore can derive

$$
G _ {1} (m | h) = \frac {E [ V | \tilde {h} ] - \overline {{m}} - P (l | \tilde {h}) (E [ V | l ] - m)}{P (h | \tilde {h}) (E [ V | h ] - m)}, m \in [ \hat {m}, \overline {{m}} ],\tag{A.12}
$$

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - \overline {{m}} - P r (\tilde {l} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}, m \in [ \hat {m}, \overline {{m}} ],\tag{A.13}
$$

and

$$
G _ {2} (m | \tilde {l}) = \frac {E [ V | h ] - \overline {{m}}}{P r (\tilde {l} | h) (E [ V | h ] - m)}, m \in [ \underline {{m}} _ {2}, \hat {m} ].\tag{A.14}
$$

We next derive m^ and m. In the mixed-strategy equilibrium, we should have $\pi _ { 1 } ( { \hat { m } } | h ) = \pi _ { 1 } ( { \overline { { m } } } | h )$ and $\pi _ { 2 } \Big ( \hat { m } | \tilde { h } \Big ) = \pi _ { 2 } \Big ( \overline { { { m } } } | \tilde { h } \Big )$ , which can be expressed as follows,

$$
P r \Big (\tilde {l} | h \Big) (E [ V | h ] - \hat {m}) = E [ V | h ] - \overline {{m}},\tag{A.15}
$$

$$
P \Big (h | \tilde {h} \Big) G _ {1} (\hat {m} | h) (E [ V | h ] - \hat {m}) + P \Big (l | \tilde {h} \Big) (E [ V | l ] - \hat {m}) = E \Big [ V | \tilde {h} \Big ] - \overline {{m}},\tag{A.16}
$$

where $G _ { 1 } ( \hat { m } | h ) = \frac { P \Big ( l | \hat { l } \Big ) ( \hat { m } - E [ V | l ] ) } { P \Big ( h | \hat { l } \Big ) ( E [ V | h ] - \hat { m } ) }$ from Eq. (A.12). Jointly solving Eqs. (A.15) and (A.16), we have

$$
\hat {m} = \frac {P (h | \tilde {h}) P (l | \tilde {l}) E [ V | l ] + P (h | \tilde {l}) (P (h | \tilde {h}) - P r (\tilde {h} | h)) E [ V | h ]}{(P (h | \tilde {h}) P (l | \tilde {l}) - P (h | \tilde {l}) P (l | \tilde {h}) + P (h | \tilde {l}) P r (\tilde {l} | h))},\tag{A.17}
$$

$$
\overline {{m}} = \frac {\left\{ \begin{array}{c} \big (P r \big (\tilde {h} | h \big) P \big (h | \tilde {h} \big) P \big (l | \tilde {l} \big) - P r \big (\tilde {h} | h \big) P \big (h | \tilde {l} \big) P \big (l | \tilde {h} \big) + P r \big (\tilde {l} | h \big) P \big (h | \tilde {l} \big) P \big (h | \tilde {h} \big) \big) E [ V | h ] \\ + P r \big (\tilde {l} | h \big) P \big (h | \tilde {h} \big) P \big (l | \tilde {l} \big) E [ V | l ] \end{array} \right\}}{P \big (h | \tilde {h} \big) P \big (l | \tilde {l} \big) - P \big (h | \tilde {l} \big) P \big (l | \tilde {h} \big) + P \big (h | \tilde {l} \big) P r \big (\tilde {l} | h \big)}.\tag{A.18}
$$

We next verify that $E [ V | l ]$ is the lower bound of $G _ { 1 } ( m | h )$ and $G _ { 2 } \Big ( m | \tilde { l } \Big )$ , and $\mathrm { o n l y } G _ { 2 } \Big ( m | \tilde { l } \Big )$ has a mass point at E[V|l]. From Eqs. (A.11) and (A.13), we have

(1) When $m _ { 1 } { = } E [ V | l ] , G _ { 1 } ( m _ { 1 } | h ) { = } 0$ and when $m _ { 2 } { = } E [ V | l ] , G _ { 2 } \Big ( m _ { 2 } | \tilde { l } \Big ) > 0 ;$

(2) If $\underline { m } _ { 2 } > E [ V | l ]$ , we have $G _ { 1 } ( \underline { { m } } _ { 2 } | h ) > 0$ and $G _ { 2 } \left( { \underline { { m } } } _ { 2 } | \tilde { l } \right) > 0 .$ Because <sup>fi</sup>rms cannot both have a mass point at the lower bound, this cannot be true. Therefore, in equilibrium, $\underline { { { m } } } _ { 2 } = E [ V | l ] , G _ { 1 } ( \underline { { { m } } } _ { 2 } | h ) = 0$ and $G _ { 2 } \left( { \underline { { m } } } _ { 2 } | \tilde { l } \right) > 0 .$ . Only <sup>fi</sup>rm 2 has a mass point at the lower bound.

Combining the results in Lemma A1, Eqs. (A.11), (A.12), (A.13) and (A.14), when $P r ( h ) { > } P r ( l )$ and $\zeta < 1$ , the <sup>fi</sup>rms' equilibrium strategies can be characterized as follows:

1. For its low-segment customer $( S = l ) .$ , <sup>fi</sup>rm 1 offers E[V|l];

2. For its low-segment customer $( \tilde { S } = \tilde { l } )$ , <sup>fi</sup>rm 2's promotional incentive follows the CDF

$$
G _ {2} (m | \tilde {l}) = \frac {E [ V | h ] - \overline {{m}}}{P r (\tilde {l} | h) (E [ V | h ] - m)}, m \in [ E [ V | l ], \hat {m} ];
$$

3. For its high-segment customer $( S = h )$ , <sup>fi</sup>rm 1's promotional incentive follows the CDF

$$
G _ {1} (m | h) = \left\{ \begin{array}{c} \frac {P (l | \tilde {l}) (m - E [ V | l ])}{P (h | \tilde {l}) (E [ V | h ] - m)}, m \in [ E [ V | l ], \hat {m} ]; \\ \frac {E [ V | \tilde {h} ] - \overline {{m}} - P (l | \tilde {h}) (E [ V | l ] - m)}{P (h | \tilde {h}) (E [ V | h ] - m)}, m \in [ \hat {m}, \overline {{m}} ]; \end{array} \right.
$$

4. For its high-segment customer $( S = \tilde { h } )$ , <sup>fi</sup>rm 2's promotional incentive follows the CDF

$$
G _ {2} (m | \tilde {h}) = \frac {E [ V | h ] - \overline {{m}} - P r (\tilde {l} | h) (E [ V | h ] - m)}{P r (\tilde {h} | h) (E [ V | h ] - m)}, m \in [ \hat {m}, \overline {{m}} ].
$$

We can verify that $G _ { 1 } ( m | h ) | _ { m - m } \leq 1 , G _ { 1 } ( m | h ) | _ { m - E [ V | ] } \geq 0 , G _ { 2 } \Bigl ( m | \widehat { l } \Bigr ) | _ { m - m } \leq 1 , G _ { 2 } \Bigl ( m | \widehat { l } \Bigr ) | _ { m - E [ V | ] } \geq 0 , G _ { 2 } \Bigl ( m | \widetilde { h } \Bigr ) | _ { m - m } \leq 1 , G _ { 2 } \Bigl ( m | \widetilde { h } \Bigr ) | _ { m - m } \geq 0 , \overline { { m } } \leq E \Bigl [ V | \widetilde { h } \Bigr ]$ and $\hat { m } > E [ V | l ]$ hold if and only if $P r ( h ) { > } P r ( l )$ . In other words, $P r ( h ) { > } P r ( l )$ is a suf<sup>fi</sup>cient and necessary condition of the existence of the second <sup>½ -j</sup>equilibrium.

We can conclude that the equilibrium in Proposition 1 exists if and only if $P r ( h ) { \leq } P r ( l )$ , and the equilibrium in Proposition 2 exists if and only if $P r ( h ) { > } P r ( l )$ . Therefore, given a pair of $P r ( h )$ and ${ P r } ( l )$ , there is only one equilibrium. In other words, these two equilibria we derived are unique.

To further con<sup>fi</sup>rm that the equilibria in Proposition 1 and Proposition 2 are unique equilibria, we consider a potential alternative equilibrium when $\zeta = 0 . { \mathrm { W h e n } } \zeta = 0 ,$ , <sup>fi</sup>rm 2 has no useful information. Firm 2 can completely ignores its information in competition, i.e., random izes promotional incentive $m _ { 2 }$ independent on S<sup>˜</sup>. Using the similar analysis, we can characterize the equilibrium of <sup>fi</sup>rm competition as follows:

1. For its low-segment customer $( S { = } l )$ , <sup>fi</sup>rm 1 offers E[V|l];

2. For its high-segment customer (S=h), <sup>fi</sup>rm 1's promotional incentive follows the CDF

$$
G _ {1 0} (m | h) = \frac {\operatorname* {P r} (l) (m - E [ V | l ])}{\operatorname* {P r} (h) (E [ V | h ] - m)}, m \in [ E [ V | l ], E [ V ] ];
$$

3. Firm 2's promotional incentive follows the CDF

$$
G _ {2 0} (m) = \frac {E [ V | h ] - E [ V ]}{E [ V | h ] - m}, m \in [ E [ V | l ], E [ V ] ].
$$

We can show that $G _ { 1 0 } ( m | h )$ is equivalent to $G _ { 1 } ( m | h ) | _ { \zeta = 0 }$ and $G _ { 2 0 } ( m | h )$ is equivalent to <sup>1</sup> $\begin{array} { r } { G _ { 2 } \Big ( m | \tilde { h } \Big ) | \zeta = 0 + \frac { 1 } { 2 } G _ { 2 } \Big ( m | \tilde { l } \Big ) | \zeta = 0 } \end{array}$ . Therefore, we can con<sup>fi</sup>rm that given a pair of Pr(h) and ${ P r } ( l )$ , only a unique equilibrium exists.

## A.5. Proof of Proposition 3

Proof. We <sup>fi</sup>rst consider the case when $P r ( h ) { \leq } P r ( l )$ (or equivalently, $P r ( h ) { \leq } \frac { 1 } { 2 } )$ . For notational simplicity, we let $\gamma = P r ( h )$ . For its low-segment customer $( S { = } l )$ <sup>ð Þ</sup>, <sup>fi</sup>rm 1 offers a deterministic promotional incentive and its expected pro<sup>fi</sup>t from the low-segment customer is zero. For its high-segment customer $( S = h )$ , <sup>fi</sup>rm 1 randomizes its promotional incentive following Eq. (A.8) and its expected pro<sup>fi</sup>t is $E [ V | h ] { - } E { \left[ V | \tilde { h } \right] }$ <sup>i</sup>. Overall, when $0 < \gamma \leq \frac { 1 } { 2 }$ and $0 { \le } { \zeta } { < } 1$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is

$$
\pi_ {1} = \operatorname * {P r} (h) \left(E [ V | h ] - E [ V | \tilde {h} ]\right) = \frac {\gamma (1 - \gamma) (1 - \zeta)}{1 - \zeta + 2 \zeta \gamma} (E [ V | h ] - E [ V | l ]) > 0.\tag{A.19}
$$

$\pi _ { 1 } = 0$ when $\gamma = 0 ,$ i.e., the customer will never be classi<sup>fi</sup>ed in the high segment for <sup>fi</sup>rm 1. This case is trivial. We ignore the discussion on this case in the study. We generally say <sup>fi</sup>rm 1 makes a positive pro<sup>fi</sup>t when $P r ( h ) { \leq } P r ( l )$ . Firm 2's expected pro<sup>fi</sup>t from a customer is always zero regardless of the customer's segmentation. Therefore, $\pi _ { 2 } = 0$

We next consider the case when $P r ( h ) { > } P r ( l )$ (or equivalently, $\textstyle \cdot \gamma > { \frac { 1 } { 2 } } )$ . For its low-segment customer, <sup>fi</sup>rm 1 offers a deterministic promotional incentive and its expected pro<sup>fi</sup>t is zero. For its high-segment customer, <sup>fi</sup>rm 1 randomizes the promotional incentive following Eqs (A.11) and (A.12), and its expected pro<sup>fi</sup>t is $E [ V | h ] - { \overline { { m } } }$ . When $\begin{array} { r } { \gamma > \frac { 1 } { 2 } } \end{array}$ and $0 { \le } { \zeta } { < } 1$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is

$$
\pi_ {1} = P r (h) (E [ V | h ] - \overline {{m}}) = \frac {\gamma (1 - \gamma) (1 - \zeta) (1 + \zeta)}{(2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1} (E [ V | h ] - E [ V | l ]) > 0.
$$

Firm 2 earns nothing from its low-segment customer in expectation, but makes a positive expected pro<sup>fi</sup>t $E \Big [ V | \tilde { h } \Big ] - \overline { { m } }$ from its high-segment cus tomer. Therefore, when $\begin{array} { r } { \gamma > \frac { 1 } { 2 } } \end{array}$ and $0 { \le } { \zeta } { < } 1$ , <sup>fi</sup>rm 2's overall expected pro<sup>fi</sup>t is

$$
\pi_ {2} = P r (\tilde {h}) (E [ V | \tilde {h} ] - \overline {{m}}) = \frac {2 (2 \gamma - 1) (1 - \gamma) (1 - \zeta) \zeta}{(2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1} (E [ V | h ] - E [ V | l ]) \geq 0.
$$

When $\zeta = 0 , \pi _ { 2 } = 0$ . When $\zeta > 0 , \pi _ { 2 } > 0 .$ . We can also verify that $\pi _ { 1 } > \pi _ { 2 }$

## A.6. Proof of Proposition 4

Proof. When $P r ( h ) { \leq } P r ( l )$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is $\pi _ { 1 } = \frac { \gamma ( 1 - \gamma ) ( 1 - \zeta ) } { 1 - \zeta + 2 \zeta \gamma } ( E [ V | h ] - E [ V | l ] )$ . The <sup>fi</sup>rst-order derivative of $\pi _ { 1 }$ w.r.t. $\zeta$ is

$$
\frac {\partial \pi_ {1}}{\partial \zeta} = \frac {- 2 \gamma^ {2} (1 - \gamma)}{(1 - \zeta + 2 \zeta \gamma) ^ {2}} (E [ V | h ] - E [ V | l ]) <   0.
$$

When $P r ( h ) { > } P r ( l )$ , <sup>fi</sup>rm 1's expected pro<sup>fi</sup>t is $\begin{array} { r } { \tau _ { 1 } = \frac { \gamma ( 1 - \gamma ) ( 1 - \zeta ) ( 1 + \zeta ) } { ( 2 \gamma - 1 ) \zeta ^ { 2 } + 2 ( 2 - 3 \gamma ) \zeta + 1 } ( E [ V | h ] - E [ V | l ] ) } \end{array}$ and <sup>fi</sup>rm 2's expected pro<sup>fi</sup>t isπ $= \frac { 2 ( 2 \gamma - 1 ) ( 1 - \gamma ) ( 1 - \zeta ) \zeta } { ( 2 \gamma - 1 ) \zeta ^ { 2 } + 2 ( 2 - 3 \gamma ) \zeta + 1 } \times$ $( E [ V | h ] { - } E [ V | l ] )$ . The <sup>fi</sup>rst-order derivative of $\pi _ { 1 }$ and $\pi _ { 2 }$ w.r.t. ζ are respectively

$$
\frac {\partial \pi_ {1}}{\partial \zeta} = \frac {2 \gamma (1 - \gamma) ((3 \gamma - 2) \zeta^ {2} - 2 \gamma \zeta + 3 \gamma - 2)}{((2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1) ^ {2}} (E [ V | h ] - E [ V | I ]),
$$

$$
\frac {\partial \pi_ {2}}{\partial \zeta} = \frac {2 (2 \gamma - 1) (1 - \gamma) ((4 \gamma - 3) \zeta^ {2} - 2 \zeta + 1)}{((2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1) ^ {2}} (E [ V | h ] - E [ V | I ]).
$$

We <sup>fi</sup>nd that:

(1) $\begin{array} { r }  \frac { \partial \pi _ { 1 } > 0 \mathrm { ~ i f ~ } \zeta \in [ 0 , m a x \{ 0 , \zeta _ { 1 } \} ] , } \end{array}$ and $\begin{array} { r } { \frac { \partial \pi _ { 1 } < 0 \mathrm { ~ i f ~ } \zeta \in ( m a x \{ 0 , \zeta _ { 1 } \} , 1 ] } { \partial \zeta } \dag \mathrm { ~ \qquad } } \end{array}$ where $\zeta _ { 1 } = \frac { \gamma - 2 \sqrt { ( 2 \gamma - 1 ) ( 1 - \gamma ) } } { 3 \gamma - 2 } . \zeta _ { 1 } \leq 1$ always holds.

(2) $\begin{array} { r } { \frac { \partial \pi _ { 2 } } { \partial \zeta } { \geq } 0 \ \mathrm { i f } \ \zeta { \in } [ 0 , \zeta _ { 2 } ] , } \end{array}$ , and <sup>∂π</sup>2<sub>∂ζ</sub> b0 $\mathrm { i f } \ \zeta \in ( \zeta _ { 2 } , 1 ]$ where $\zeta _ { 2 } = \frac { 1 - 2 \sqrt { ( 1 - \gamma ) } } { 4 \gamma - 3 } . 0 { \leq } \zeta _ { 2 } { \leq } 1$ always holds.

## A.7. Proof of Proposition 5

Proof. The CDI's expected pro<sup>fi</sup>t is $I I { = } \pi _ { 1 } { + } \pi _ { 2 }$

When $P r ( h ) { \leq } P r ( l )$

$$
\Pi = \pi_ {1} = \frac {\gamma (1 - \gamma) (1 - \zeta)}{1 - \zeta + 2 \zeta \gamma} (E [ V | h ] - E [ V | l ])
$$

The <sup>fi</sup>rst-order-derivative of Π w.r.t. $\zeta$ is

$$
\frac {\partial \Pi}{\partial \zeta} = \frac {\partial \pi_ {1}}{\partial \zeta} <   0
$$

When $P r ( h ) { > } P r ( l )$

$$
\begin{array}{c} \Pi = \frac {\gamma (1 - \gamma) (1 - \zeta) (1 + \zeta)}{(2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1} (E [ V | h ] - E [ V | l ]) \\ \qquad + \frac {2 (2 \gamma - 1) (1 - \gamma) (1 - \zeta) \zeta}{(2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1} (E [ V | h ] - E [ V | l ]) \\ \qquad = \frac {(1 - \gamma) (1 - \zeta) (5 \gamma \zeta - 2 \zeta + \gamma)}{(2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1} (E [ V | h ] - E [ V | l ]). \end{array}
$$

The <sup>fi</sup>rst-order-derivative of Π w.r.t. $\zeta$ is

$$
\frac {\partial \Pi}{\partial \zeta} = 2 (1 - \gamma) \frac {\left(\left(1 1 \gamma^ {2} - 1 2 \gamma + 3\right) \zeta^ {2} + (- 2 \gamma^ {2} - 4 \gamma + 2) \zeta + 3 \gamma^ {2} - 1\right)}{\left((2 \gamma - 1) \zeta^ {2} + 2 (2 - 3 \gamma) \zeta + 1\right) ^ {2}} (E [ V | h ] - E [ V | I ]).
$$

Therefore, $\scriptstyle { \frac { \partial I I } { \partial \zeta } } \geq 0$ when $\zeta { \in } [ 0 , m a x \{ 0 , \zeta _ { 0 } \} ]$ and $\scriptstyle { \frac { \partial I I < 0 } { \partial \zeta } }$ when $\zeta { \in } ( m a x \{ 0 , \zeta _ { 0 } \} , 1 ]$ ] wher $\begin{array} { r } { \zeta _ { 0 } = \frac { - 1 + 2 \gamma + \gamma ^ { 2 } - 2 \sqrt { ( 2 \gamma - 1 ) ( 1 - \gamma ) ( 4 \gamma ^ { 2 } + \gamma - 1 ) } } { 1 1 \gamma ^ { 2 } - 1 2 \gamma + 3 } . } \end{array}$ . Note that $\zeta _ { 0 } \leq 1$ always holds.

## A.8. Proof of Proposition 6

Proof. When $P r ( h ) { \leq } P r ( l )$ , the CDI's expected pro<sup>fi</sup>t is always decreasing in $\zeta .$ Therefore, the CDI will always choose $\zeta = 0 .$ . In another word, the CDI only serves <sup>fi</sup>rm 1.

When $P r ( h ) { > } P r ( l )$ , the CDI's expected pro<sup>fi</sup>t is increasing in $\zeta$ when $\zeta { \in } [ 0 , m a x \{ 0 , \zeta _ { 0 } \} ]$ and decreasing in $\zeta$ when $\zeta { \in } ( m a x \{ 0 , \zeta _ { 0 } \} , 1 ]$ . The CDI will choose $\zeta = m a x \{ 0 , \zeta _ { 0 } \} . \zeta _ { 0 } > 0$ requires that γ $> { \frac { \sqrt { 3 } } { 3 } } .$ . Therefore, the CDI serves two <sup>fi</sup>rms and set $\zeta = \zeta _ { 0 }$ when $\gamma > { \frac { \sqrt { 3 } } { 3 } } .$ Otherwise, it only serves <sup>fi</sup>rm 1. It can also be veri<sup>fi</sup>ed that $\frac { d \zeta _ { 0 } } { d \gamma } > 0$ when $\gamma > \frac { \sqrt { 3 } } { 3 } .$

## A.9. Proof of Proposition 7

Proof. Substitute the optimal similarity factor $\zeta _ { 0 }$ into Π, we have the following expected pro<sup>fi</sup>ts.

(1) When $\gamma { \le } \frac { \sqrt { 3 } } { 3 } ,$

$$
\zeta^ {*} = 0 \text {   and   } \Pi = \gamma (1 - \gamma) (E [ V | h ] - E [ V | l ]).
$$

The CDI's problem of pro<sup>fi</sup>t maximization can be represented as

$$
\begin{array}{l} \max _ {\psi , \phi} \Pi = \gamma (1 - \gamma) \left(\frac {\lambda \psi}{\lambda \psi + (1 - \lambda) \phi} - \frac {\lambda (1 - \psi)}{\lambda (1 - \psi) + (1 - \lambda) (1 - \phi)}\right) R \\ s. t. \quad \gamma \leq \frac {\sqrt {3}}{3}, 0 \leq \phi <   \psi \leq 1 \end{array}
$$

Differentiate Π w.r.t. ψ and ϕ, we have

$$
\frac {\partial \Pi}{\partial \psi} = \lambda (1 - \lambda) R > 0, \frac {\partial \Pi}{\partial \phi} = - \lambda (1 - \lambda) R <   0.
$$

Therefore, the CDI will choose $\psi = 1$ and $\phi = 0 \mathrm { w h e n } \lambda { \leq } \frac { \sqrt { 3 } } { 3 } .$ . When $\lambda > { \frac { \sqrt { 3 } } { 3 } } ,$ we let $\begin{array} { r } { \psi = \frac { \frac { \sqrt { 3 } } { 3 } - ( 1 - \Lambda ) \phi } { \lambda } . } \end{array}$ . Differentiate Π w.r.t. $\phi ,$ we have

$$
\frac {\partial \Pi}{\partial \phi} = - (1 - \lambda) R <   0.
$$

Therefore, the CDI will choose $\phi = 0$ and $\begin{array} { r } { \psi = \frac { \sqrt { 3 } } { 3 \lambda } . } \end{array}$

<sup>¼</sup>The potential optimal solutions are as follows.

(a) when $\lambda { \leq } \frac { \sqrt { 3 } } { 3 } , \{ \psi = 1 , \phi = 0 \} ;$

(b) when $\begin{array} { r } { \lambda > \frac { \sqrt { 3 } } { 3 } , \left\{ \psi = \frac { \sqrt { 3 } } { 3 \lambda } , \phi = 0 \right\} } \end{array}$

(2) When $\begin{array} { r } { \gamma > \frac { \sqrt { 3 } } { 3 } , } \end{array}$

$$
\begin{array}{l} \zeta^ {*} = \frac {- 1 + 2 \gamma + \gamma^ {2} - 2 \sqrt {(2 \gamma - 1) (1 - \gamma) (4 \gamma^ {2} + \gamma - 1)}}{1 1 \gamma^ {2} - 1 2 \gamma + 3} \\ \text { and } \Pi = \frac {(1 - \gamma) (1 - \zeta^ {*}) (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma)}{(2 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \zeta^ {*} + 1} (E [ V | h ] - E [ V | l ]). \end{array}
$$

The CDI's pro<sup>fi</sup>t maximization problem can be represented as

$$
\begin{array}{l} \max _ {\psi , \phi} \Pi = \frac {(1 - \gamma) (1 - \zeta^ {*}) (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma)}{(2 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \zeta^ {*} + 1} \\ \qquad \times \left(\frac {\lambda \psi}{\lambda \psi + (1 - \lambda) \phi} - \frac {\lambda (1 - \psi)}{\lambda (1 - \psi) + (1 - \lambda) (1 - \phi)}\right) R \\ s. t. \qquad \gamma \geq \frac {\sqrt {3}}{3}, 0 \leq \phi <   \psi \leq 1 \end{array}
$$

where $\zeta ^ { * } = \frac { - 1 + 2 \gamma + \gamma ^ { 2 } - 2 \sqrt { ( 2 \gamma - 1 ) ( 1 - \gamma ) \left( 4 \gamma ^ { 2 } + \gamma - 1 \right) } } { 1 1 \gamma ^ { 2 } - 1 2 \gamma + 3 } .$

Let $\begin{array} { r } { \boldsymbol { A } = \frac { ( 1 - \gamma ) ( 1 - \xi ^ { * } ) ( 5 \gamma \xi ^ { * } - 2 \xi ^ { * } + \gamma ) } { ( 2 \gamma - 1 ) \left( \xi ^ { * } \right) ^ { 2 } + 2 ( 2 - 3 \gamma ) \xi ^ { * } + 1 } \Biggl ( \frac { \lambda \psi } { \lambda \psi + ( 1 - \lambda ) \phi } - \frac { \lambda ( 1 - \psi ) } { \lambda ( 1 - \psi ) + ( 1 - \lambda ) ( 1 - \phi ) } \Biggr ) \boldsymbol { R } + \mu _ { 1 } ( \lambda \psi + ( 1 - \lambda ) \phi - \frac { \sqrt { 3 } } { 3 } ) } \end{array}$ , where $\mu _ { 1 }$ is Lagrange multiplier. From the Envelop Theorem, we have

$$
\begin{array}{l} \frac {\partial \Lambda}{\partial \psi} = \frac {\partial \Pi}{\partial \gamma} \frac {\partial \gamma}{\partial \psi} + \frac {\partial \Pi}{\partial \psi} + \lambda \mu_ {1}, \\ \frac {\partial \Lambda}{\partial \phi} = \frac {\partial \Pi}{\partial \gamma} \frac {\partial \gamma}{\partial \phi} + \frac {\partial \Pi}{\partial \phi} + (1 - \lambda) \mu_ {1}. \end{array}
$$

$$
\text { where } \frac {\partial \Pi}{\partial \gamma} = \frac {(1 - \zeta^ {*}) ((5 \zeta^ {*} + 1) ((2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) - (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma) ((4 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 6 \gamma) \zeta^ {*} + 1)) (\psi - \phi) (1 - \lambda) \lambda}{((2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) ^ {2}} R.
$$

$$
\begin{array}{l} \frac {\partial \Lambda}{\partial \psi} = \frac {(1 - \zeta^ {*}) ((5 \zeta^ {*} + 1) ((2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) - (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma) ((4 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 6 \gamma) \zeta^ {*} + 1)) (\psi - \phi) (1 - \lambda)}{((2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) ^ {2}} \lambda^ {2} R \\ + \frac {(1 - \zeta^ {*}) (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma) (1 - \lambda) \lambda}{((2 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \zeta^ {*} + 1) \gamma} R + \lambda \mu_ {1} = 0 \end{array}
$$

$$
\begin{array}{l} \frac {\partial \Lambda}{\partial \phi} = \frac {(1 - \zeta^ {*}) ((5 \zeta^ {*} + 1) ((2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) - (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma) ((4 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 6 \gamma) \zeta^ {*} + 1)) (\psi - \phi) (1 - \lambda)}{(2 \gamma - 1) \gamma (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \gamma \zeta^ {*} + \gamma) ^ {2}} \lambda (1 - \lambda) R \\ - \frac {(1 - \zeta^ {*}) (5 \gamma \zeta^ {*} - 2 \zeta^ {*} + \gamma) (1 - \lambda) \lambda}{((2 \gamma - 1) (\zeta^ {*}) ^ {2} + 2 (2 - 3 \gamma) \zeta^ {*} + 1) \gamma} R + (1 - \lambda) \mu_ {1} = 0 \end{array}
$$

Considering the constraints $\psi \leq 1$ and $\phi \geq 0 ,$ we have the following solutions:

(c) $\mathrm { { f } } \ \mu _ { 1 } = 0 , \{ \psi = 1 , \phi = 0 \} ;$

(d) $\begin{array} { r } { \mathrm { I f } \ \dot { \mu } _ { 1 } > 0 , \ \Big \{ \psi = 1 , \phi = \frac { \sqrt { 3 } - \lambda } { ( 1 - \lambda ) } \Big \} } \end{array}$

Based on all the cases (a)–(d), for any speci<sup>fi</sup>c λ, the optimal solution that gives the highest pro<sup>fi</sup>t Π for the CDI is $\{ \psi = 1 , \phi = 0 \}$

## References

[1] H. Bhargava, V. Choudhary, Information goods and vertical differentiation, Journal of Management Information Systems 18 (2) (2001) 85–102.

[2] H. Bhargava, V. Choudhary, Economics of an information intermediary with aggregation bene<sup>fi</sup>ts, Information Systems Research 15 (1) (2004) 22–36.

[3] Y. Chen, C. Narasimhan, Z.J. Zhang, Individual marketing with imperfect targetability, Marketing Science 20 (1) (2001) 23–41.

[4] Y. Chen, G. Iyer, V. Padmanabhan, Referral informediaries, Marketing Science 21 (4) (2002) 412–434.

[5] V. Choudhary, A. Ghose, T. Mukhopadhyay, U. Rajan, Personalized pricing and quality differentiation, Management Science 51 (7) (2005) 1120–1130

[6] R. Engelbrecht-Wiggans, P.R. Milgrom, R.J. Weber, Competitive bidding and proprietary information, Journal of Mathematical Economics 11 (1983) 161–169.

[7] A. Ghose, T. Mukhopadhyay, U. Rajan, Impact of internet referral services on the supply chain, Information Systems Research 18 (3) (2007) 300–319.

[8] G. Iyer, D. Soberman, Markets for product modi<sup>fi</sup>cation information, Marketing Science 19 (3) (2000) 203–225

[9] G. Iyer, D. Soberman, J.M. Villas Boas, The targeting of advertising, Marketing Science 24 (3) (2005) 461–476.

[10] K. Li, T. C. Du, Building a targeted mobile advertising system for location-based services, forthcoming at Decision Support Systems.

[11] Y-M. Li, Y-L. Shiu, A diffusion mechanism for social advertising over microblogs, forthcoming at Decision Support Systems.

[12] Q. Liu, K. Serfes, Customer information sharing among rival <sup>fi</sup>rms, European Economic Review 50 (2006) 1571–1600.

[13] Y. Liu, Z.J. Zhang, The bene<sup>fi</sup>ts of personalized pricing in a channel, Marketing Science 25 (1) (2006) 97–105

[14] P.R. Milgrom, R.J. Weber, The value of information in a sealed-bid auction, Journal of Mathematical Economics 10 (1982) 105–114.

[15] J. Pancras, K. Sudhir, Optimal marketing strategies for a customer data intermediary, Journal of Marketing Research XLIV (2007) 560–578.

[16] G. Shaffer, Z.J. Zhang, Competitive coupon targeting, Marketing Science 14 (4) (1995) 395–416.

[17] G. Shaffer, Z.J. Zhang, Competitive one-to-one promotions, Management Science 48 (9) (2002) 1143–1160.

[18] R.H. Varian, A model of sales, American Economic Review 70 (4) (1980) 651–659.

[19] H.R. Varian, Versioning information goods, in: B. Kahin, H.R. Varian (Eds.), Internet Publishing and Beyond: The Economics of Digital Information and Intellectual Property, MIT Press, Cambridge, MA, 2001, pp. 190–202.

[20] J.M. Villas-Boas, Sleeping with the enemy: should competitor share the same advertising agency? Marketing Science 13 (2) (1994) 190–202.

[21] S. Wattal, R. Telang, T. Mukhopadhyay, Information personalization in a two-dimentional product differentiation model, Journal of Management Information Systems 26 (2) (2009) 69–95.

[22] T.A. Weber, Z. Zhang, A model of search intermediaries and paid referrals, Information Systems Research 18 (4) (2007) 414–436

Dr. Xia Zhao is an assistant professor of Information Systems at the Bryan School of Business and Economics, the University of North Carolina at Greensboro. She received her Ph.D. degree in Management Science and Information Systems from the McCombs School of Business at the University of Texas at Austin. Her research interests include online advertising, information security, electronic commerce and IT governance. She has published papers in Journal of Management Information Systems, Decision Support Systems, IEEE Computer, International Journal of Electronic Commerce, Information Systems Frontier and many conference proceedings.
