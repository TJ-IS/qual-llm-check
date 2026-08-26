---
otero_id: 6794
otero_key: "56R7Y4YC"
title: "Will a supplier benefit from sharing good information with a retailer?"
authors: "Tsan-Ming Choi; Jian Li; Ying Wei"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2013.05.011"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Tsan-Ming Choi <sup>a,</sup>⁎, Jian Li <sup>b</sup>, Ying Wei <sup>c</sup>

<sup>a</sup> Business Division, Institute of Textiles and Clothing, The Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong

<sup>b</sup> School of Economics and Management, Beijing University of Chemical Technology, Beijing 100029, China

<sup>c</sup> Management School, Jinan University, Guangzhou 510632, China

## a r t i c l e i n f o

Article history: Received 10 September 2012 Received in revised form 10 April 2013 Accepted 16 May 2013 Available online 2 June 2013

Keywords: Supply chain management Forecast updating Returns policy

## a b s t r a c t

Information sharing has been known to be crucial in supply chain management. Prior empirical <sup>fi</sup>nding reveals that suppliers in practice tend to help their trading partners improve forecast accuracy. This paper examines this issue and explores the up–down (from an upstream supplier to a downstream retailer) strategic information sharing issues in a two-echelon supply chain. We <sup>fi</sup>rst model a supply chain with forecast updating and returns policy. The forecast updating scheme adopts the Bayesian approach with unknown mean and unknown variance. We then proceed to analytically explore the effects of forecast updating on the supplier and the retailer. Our analysis has revealed that: 1. Demand information with low relevance can lead to a loss to the retailer. 2. In the absence of returns policy, the supplier has an incentive to provide “bad information” which may be harmful to the retailer. 3. The supplier will provide “good information” to the retailer only under the returns policy. 4. With up–down information sharing, win–win coordination can be achieved by using a proper returns policy. Many of these results can supplement and challenge the prior research <sup>fi</sup>ndings that supplier has good incentive to help retailers in improving forecast.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Information sharing between channel members in a supply chain has been shown to be highly important. For example, it can help alleviate the notorious bullwhip effect [17] and enhance many operational decisions such as inventory [28] and pricing. With the advance of modern technology, such as RFID and web-based EDI, supply chain channel agents can conveniently share information for improving their respective operations.

Previous studies have shown that information sharing [18] by retailers generally bene<sup>fi</sup>ts the manufacturers directly [26]. However, whether information shared by manufacturers will always bene<sup>fi</sup>t the retailers is still unclear. Recently, Taylor and Xiao [29] have revealed an insightful and interesting <sup>fi</sup>nding that an upstream manufacturer is bene<sup>fi</sup>ted from selling to a retailer who is a good forecaster.<sup>1</sup> Moreover, prior empirical <sup>fi</sup>nding based on a survey of 120 companies reveals that suppliers in practice put “improving trading partner's forecast accuracy” as top priority [14]. It is hence interesting to explore further the strategic information sharing issues in the supply chain.

At the same time, supply contracts have been shown to be useful in enhancing supply chain performance by dampening the double marginalization effect in the supply chain [6,7]. Among different types of supply contracts, a contract called “returns policy” is commonly adopted in the industry and widely explored in the literature.

Under the returns policy, the supplier promises the retailer to buy back any leftover of its own product by the end of the retail selling season with a partial refund. The returns policy is known to be effective in coordinating supply chains [24] and is one of the most widely seen supply contracts in practice [8,21]. As a result, this paper also examines the use of returns policy in the supply chain with information sharing.

To be speci<sup>fi</sup>c, in this paper, we study a supply chain with one upstream (up) supplier and one downstream (down) retailer.<sup>2</sup> For the upcoming season, the retailer needs to place an order to the supplier in order to secure the needed quantity of a seasonal fashion product. Facing a short selling season and following the lead time requirement, the retailer can place only one order while she can order either early or late (up to a certain time point). If the retailer orders late, she has a chance to improve her forecast regarding the upcoming seasonal product's demand by some market information. In this paper, we consider the situation that the supplier will offer the demand data of a pre-seasonal product to the retailer (and hence we call it “up–down information sharing”). This kind of situation is rather common in various industries such as fashion apparel. For example, if we consider the supplier as the wholesale of<sup>fi</sup>ce of a sportswear brand such as Nike or Adidas, he has the demand data of all kinds of the respective branded products. In order to let the retailer know more about the market trend and popularity of the forthcoming seasonal product, the supplier will usually provide market information regarding the demand of some related pre-seasonal product(s). Following this simple industrial practice, various open research questions hence arise:

(i) Among the many pre-seasonal products, strategically, which one's data should be selected by the supplier and be shared with the retailer?

(ii) Does a pre-seasonal product which is related to the seasonal product in terms of their demand variances but not their means an appropriate choice?

(iii) Would the selection and sharing of a pre-seasonal product's demand information which is bene<sup>fi</sup>cial to the retailer also bene<sup>fi</sup>t the supplier? Alternatively, would the supplier have an incentive to share with the retailer some information which hurts the retailer but bene<sup>fi</sup>ts himself <sup>3</sup>?

(iv) With information sharing, how can the supplier coordinate the supply chain (establish a win–win situation) by using the returns policy?

The objectives and contributions of this paper are to analytically address the above questions and provide managerial insights.

The rest of this paper is organized as follows. Section 2 reviews the three streams of related literature. Section 3 presents the forecast updating model. Section 4 derives the performances of the supply chain and its agents with and without forecast updating. Section 5 explores the effects of forecast updating and information sharing. Section 6 concludes this paper with a discussion on managerial insights. To simplify our exposition, all proofs and detailed derivations are provided in Appendix.

## 2. Literature review

Three streams of work are related to this paper, namely (i) the demand forecast [19] updating model, (ii) the optimal inventory policies with information updating, and (iii) the supply chain coordination mechanisms with information updating. We will review them as follows.

In terms of forecasting the unknown parameters of the demand distribution, Bayesian approach has been widely adopted since the 1950s [12,27]. The idea is to make use of information to obtain the posterior distribution (a-posteriori) from the estimated prior distribution (a-priori). Early works include [1,2,23]. Later on, motivated by the quick response (QR) industrial practice, Iyer and Bergen [16] studied the QR strategy for a manufacturer–retailer supply chain. Using the normal observation process (with known variance) and normal prior demand distribution, they divided the planning horizon into two distinct stages. Information observed in the <sup>fi</sup>rst stage is used to revise the distribution parameters via a Bayesian approach. Following the Bayesian information updating with a conjugate pair, the variance of the demand distribution is assumed to be always decreased after observation. They built models of inventory decisions for both the manufacturer and the retailer. They discussed the bene<sup>fi</sup>ts to each one of them before and after adopting QR. Choi et al. [10] compared two Bayesian models: One follows Iyer and Bergen [16] with the forecast revision on the unknown mean of demand only, the other follows Berger [3] with the forecast revisions on both the unknown mean and unknown variance. They showed that the model in [3] outperforms [16] by allowing more precise information updating. Similar to the above reviewed literature, this paper also employs Bayesian information updating model in examining the supply chain information sharing issues. However, this paper speci<sup>fi</sup>cally focuses on the top–down scenario of information sharing which is different from the majority of the reviewed literature above.

Based on the updated demand information, an important problem is to identify the optimal inventory policy. For example, Gurnani and Tang [15] studied the two-stage ordering problems with forecast revisions and uncertain future ordering cost. They explored the case under which the retailer can place orders from the manufacturer at two distinct time instances. Key insights on the cases with worthless and perfect information are generated following an assumption with the bivariate normal distribution. Another interesting related area is on advance selling [28]. By advance selling, the retailer can better forecast the selling season demand because orders received in the advance selling period is usually correlated with the in-season demand. Despite being an appealing idea, advance selling is recently challenged by the analysis which takes consumer risk preference into account [25]. This paper also studies the inventory decision in the supply chain with information updating. However, the focal point of this paper is mainly on exploring the strategic issue on sharing “good” or bad” information and the respective in<sup>fl</sup>uences on the inventory decisions and supply chain performance. These are some critical issues not yet addressed in the literature and they highlight the important differences between this paper and the above reviewed works.

In a supply chain with information updating, channel coordination becomes an important issue [20]. In particular, it may not be bene<sup>fi</sup>- cial to the manufacturer if he allows the retailer to postpone her ordering decision even though such action allows the retailer to update her forecast and improve her expected pro<sup>fi</sup>t [16]. Chen and Xu [5] considered a seasonal product supply chain with an inherent con-<sup>fl</sup>ict between the retailer and the manufacturer owing to the issue on ordering time postponement (the retailer wants to delay the ordering decision and hence enjoys the bene<sup>fi</sup>ts from information updating while the manufacturer suffers by having insuf<sup>fi</sup>cient production time and even a small expected production quantity). Based on Iyer and Bergen's [16] model, Chen and Xu [5] provided analytical compensations plans with which both the manufacturer and the retailer will be bene<sup>fi</sup>ted after information updating and hence achieve the Pareto improving situation. Other related works in this scope include a study on the backup agreement contract in fashion supply chains [13], the use of a single contract to coordinate a two-stage supply chain inventory model with forecast revision [11], the use of quantity discount contract as an optimal procurement scheme in a supply chain with forecast improvement [29], the coordination mechanism for supply chain with forecast updates and price-dependent demand [7], a thorough discussion on the analytical conditions for different scenarios on supply chain integration with vendor managed inventory system [30], and an analysis of how a two-supplier and one-retailer supply chain with forecast updating can be coordinated [31]. Similar to the above reviewed studies, this paper studies supply chain performance and coordination issues in the presence of the commonly explored returns policy in supply chain management.

Following the above literature, this paper studies analytically a supply chain with a supplier and a retailer selling a seasonal product, employing the widely applied returns policy $[ 2 4 ] . ^ { 4 }$ Forecast updating is conducted by the downstream retailer with the information provided by the upstream supplier. Our analytical <sup>fi</sup>ndings show that: 1. Demand information with low relevance can lead to a poor forecast and even loss in the resulting expected pro<sup>fi</sup>t for the retailer. 2. Bene<sup>fi</sup>ts of forecast updating highly depend on the correlations of both the “average demands and demand variances” of the item under forecast and the observation target, but in different ways. To be speci<sup>fi</sup>c, the bene<sup>fi</sup>ts are especially substantial when the respective means are highly correlated and the respective variances are less correlated. 3. In the absence of returns policy, the upstream supplier has an incentive to provide “bad information” which is harmful to the retailer. The supplier will offer relevant and useful information to the retailer in the presence of returns policy. 4. Win–win coordination can be achieved by the supplier with a proper use of returns policy as well as a good selection of the observation target's information to share with the retailer. To the best of our knowledge, this paper is the <sup>fi</sup>rst one which speci<sup>fi</sup>cally studies the strategic issue of up–down information sharing in a supply chain and reveals the critical role played by the presence of different supply contracts (the returns policy and wholesale pricing). To better show the literature positioning of this paper, we present Table 1.<sup>5</sup>

## 3. Forecast updating model

We construct the basic forecast updating model in this section. We start with two fashion products, one is called the seasonal product S and the other is called the observation target pre-seasonal product O. The demands of S and O are denoted by $D _ { S }$ and $D _ { O } ,$ respectively. In our model, we have two time points: Stage 1 and Stage 2. At Stage 1, we have a prior joint distribution of the mean and the variance for $D _ { S }$ and $D _ { O } .$ From Stage 1 to Stage 2, the supplier collects the observation towards $D _ { O }$ and shares it with the retailer. This observation is used to update the prior joint distribution of D to the posterior one. Fig. 1 illustrates the timeline of the forecast updating model.

In order to generate more analytical insights, we follow the literature [10,16] and assume that the demand of O follows a normal distribution with mean M and variance V, and the demand of S also follows a normal distribution with mean $S _ { M } = ( a _ { M } M + k _ { M } )$ and variance $S _ { V } = a _ { V } V ,$ where $a _ { V } > 0 , a _ { M }$ and $k _ { M }$ are non-negative constants. The presence of $k _ { M }$ implies that there is a basic demand of S which is independent of O's demand. Notice that when $a _ { M }$ is very small, the expected $D _ { S }$ and expected $D _ { O }$ are not highly correlated but their demand variances can still be correlated. One real world situation for the occurrence of this case can be found in the example that we discussed in Section 1. For example, the supplier wholesales a large variety of products and products of different categories (e.g., soccer jersey and basketball shoes) could exhibit rather uncorrelated demand patterns in terms of the expected demand (e.g., the average weekly demand for a soccer jersey can be totally uncorrelated to the average weekly demand for the basketball shoes). However, even for products of different categories, their demand variances are affected by the market situation. This is especially true for consumer products such as fashion apparel, consumer electronics, beauty products, etc. To be speci<sup>fi</sup>c, we take the prior joint distribution of $D _ { O }$ at Stage 1 to be a normal-inverted-gamma distribution with which the mean of demand follows a normal distribution with its variance being a random variable distributed following an invertedgamma distribution (see [3,10])<sup>6</sup>

$$
f _ {1} (M, V) = f _ {N} (M | \mu_ {1}, \tau_ {1} V) f _ {I G} (V | \alpha , \beta_ {1}),\tag{3.1}
$$

where $a > 2 .$

Notice that in (3.1): (i) $\begin{array} { r } { f _ { N } \bigg ( M | \mu _ { 1 } , \tau _ { 1 } V ) = \frac { 1 } { \sqrt { 2 \pi \tau _ { 1 } V } } \exp \left( - \frac { ( M - \mu _ { 1 } ) ^ { 2 } } { 2 \tau _ { 1 } V } \right) } \end{array}$ is the density function of the normal distribution with mean $\mu _ { 1 }$ and variance $\begin{array} { r } { \tau _ { 1 } V ; ( \operatorname { i i } ) f _ { I G } ( V | \alpha , \beta _ { 1 } ) = \frac { \exp \left( - \frac { 1 } { V \beta _ { 1 } } \right) } { \gamma ( \alpha ) ( \beta _ { 1 } ) ^ { \alpha } V ^ { ( \alpha + 1 ) } } } \end{array}$ is the inverted-gamma distribution, where $\begin{array} { r } { \gamma ( \alpha ) = \int _ { 0 } ^ { \infty } t ^ { \alpha - 1 } e ^ { - \mathrm { \Delta } t } d t ; } \end{array}$ (iii) by de<sup>fi</sup>nition of the distribution: $a > 2 ; ( \mathrm { i v } )$ as shown in (3.1), for given V, we know that M is a normally distributed random variable with mean $\mu _ { 1 }$ and variance $\tau _ { 1 } V .$

From Stage 1 to Stage 2, an observation on $D _ { O }$ (called o^, generated by an independent normal observation process with an unknown variance) is available and the retailer can make use of o^ to update the prior joint distribution $f _ { 1 } ( M , V )$ to the posterior joint distribution $f _ { 2 } ( M , V )$ . It is a classic result following the Bayesian conjugate pair with normal process (which is derived by the standard Bayesian approach employing conditional probabilities, see [3] for the details) that the posterior distribution exhibits a very nice closed-form analytical expression given below:

$$
f _ {2} (M, V | \hat {o}) = f _ {N} (M | \mu (\hat {o}), \tau_ {2} V) f _ {I G} (V | \alpha , \beta_ {2} (\hat {o})),\tag{3.2}
$$

where

$$
\mu_ {2} (\hat {o}) = \frac {\mu_ {1} + \tau_ {1} \hat {o}}{\tau_ {1} + 1}, \quad \tau_ {2} = \left[ \frac {1}{\tau_ {1}} + 1 \right] ^ {- 1} = \frac {\tau_ {1}}{1 + \tau_ {1}} <   1, \beta_ {2} (\hat {o}) = \left[ \frac {1}{\beta_ {1}} + \frac {(\mu_ {1} - \hat {o}) ^ {2}}{2 (1 + \tau_ {1})} \right] ^ {- 1}.
$$

Notice that: (i) the posterior joint distribution of $f _ { 2 } ( M , V )$ is still a normal-inverted gamma distribution, (ii) this updating process does not revise the value of $a , ( \mathrm { i i i } ) \mu _ { 2 } ( \hat { o } ) \geq \mu _ { 1 }$ when $\hat { o } \geq \mu _ { 1 }$ , and $\mu _ { 2 } ( \hat { o } ) { < } \mu _ { 1 }$ when $\hat { o } < \mu _ { 1 } , ( \mathrm { i v } ) \tau _ { 2 } < \tau _ { 1 } , ( \mathrm { v } ) \beta _ { 2 } ( \hat { o } ) \leq \beta _ { 1 } [ 3 , 1 0 ]$

With the above well-de<sup>fi</sup>ned prior and posterior distributions for $D _ { O } ,$ the prior and posterior joint distributions of $D _ { S }$ can be expressed as follows,

$$
f _ {1} (S _ {M}, S _ {V}) = f _ {N} \left(S _ {M} | a _ {M} \mu_ {1} + k _ {M}, \frac {a _ {M} ^ {2} \tau_ {1}}{a _ {V}} S _ {V}\right) f _ {I G} \left(S _ {V} | \alpha , \frac {\beta_ {1}}{a _ {V}}\right),\tag{3.3}
$$

$$
f _ {2} (S _ {M}, S _ {V} | \hat {o}) = f _ {N} \left(S _ {M} | a _ {M} \mu_ {2} (\hat {o}) + k _ {M}, \frac {a _ {M} ^ {2} \tau_ {2}}{a _ {V}} S _ {V}\right) f _ {I G} \left(S _ {V} | \alpha , \frac {\beta_ {2} (\hat {o})}{a _ {V}}\right).\tag{3.4}
$$

The literature positioning of this paper.

<table><tr><td></td><td>Information update?</td><td>No. of parameter update</td><td>Demand information acquisition</td><td>Good/bad information issue?</td><td>Single-echelon or multi-echelon?</td><td>Types of contracts</td></tr><tr><td>[1]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[2]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[4]</td><td>No</td><td>0</td><td>-</td><td>-</td><td>Multiple</td><td>Revenue sharing</td></tr><tr><td>[7]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns</td></tr><tr><td>[6]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns</td></tr><tr><td>[5]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns</td></tr><tr><td>[8]</td><td>No</td><td>0</td><td>-</td><td>No</td><td>Multiple</td><td>Rebates &amp; returns</td></tr><tr><td>[10]</td><td>Yes</td><td>2</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[11]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns</td></tr><tr><td>[12]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[13]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Backup agreement</td></tr><tr><td>[15]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[16]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Service level, volume and price commitments</td></tr><tr><td>[20]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Combined contract</td></tr><tr><td>[23]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[24]</td><td>No</td><td>-</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns</td></tr><tr><td>[27]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Single</td><td>-</td></tr><tr><td>[28]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Discount</td></tr><tr><td>[29]</td><td>Yes</td><td>1</td><td>By retail only(and retailer has better forecast).</td><td>No</td><td>Multiple</td><td>Wholesale pricing, quantity discount</td></tr><tr><td>[31]</td><td>Yes</td><td>1</td><td>By retail only</td><td>No</td><td>Multiple</td><td>Returns &amp; order cancellation</td></tr><tr><td>[32]</td><td>Yes</td><td>1</td><td>Forecasting w.r.t. the competing supply chain&#x27;s demand</td><td>No</td><td>Multiple</td><td>Wholesale pricing</td></tr><tr><td>This paper</td><td>Yes</td><td>2</td><td>By supplier only</td><td>Yes</td><td>Multiple</td><td>Returns &amp; wholesale pricing</td></tr></table>

After the observation, similar to [10] the predictive distribution of $D _ { S }$ can be derived to be a t-distribution by the following method (the details are shown in Appendix):

$$
\begin{array}{l} f _ {1} (D _ {S}) = \int_ {0} ^ {\infty} \int_ {- \infty} ^ {\infty} f _ {N} (D _ {S} | S _ {M}, S _ {V}) f _ {N} \left(S _ {M} | a _ {M} \mu_ {1} + k _ {M}, \frac {a _ {M} ^ {2} \tau_ {1}}{a _ {V}} S _ {V}\right) f _ {I G} \left(S _ {V} | \alpha , \frac {\beta_ {1}}{a _ {V}}\right) d S _ {M} d S _ {V} \\ = \int_ {0} ^ {\infty} f _ {N} \left(D _ {S} | a _ {M} \mu_ {1} + k _ {M}, \left(1 + \frac {a _ {M} {} ^ {2} \tau_ {1}}{a _ {V}}\right) S _ {V}\right) f _ {I G} \left(S _ {V} | \alpha , \frac {\beta_ {1}}{a _ {V}}\right) d S _ {V} \\ = f _ {t} \left(D _ {S} | 2 \alpha , a _ {M} \mu_ {1} + k _ {M}, \frac {a _ {V} + a _ {M} ^ {2} \tau_ {1}}{\alpha \beta_ {1}}\right), \end{array} \tag {3.5}
$$

where $f _ { t } ( \cdot | \rho , \nu , \sigma ^ { 2 } )$ is the t-distribution with parameters: degree $\rho ,$ location parameter $\nu ,$ and scale parameter $\sigma ^ { 2 }$ . Notice that these parameters are useful in de<sup>fi</sup>ning the speci<sup>fi</sup>c t-distribution and we will employ them in the derivations of some important performance measures such as the expected gain of information.

Similarly, with o^ obtained at Stage 1, the predictive distribution of $D _ { S }$ is given by,

$$
f _ {2} (D _ {S} | \hat {o}) = f _ {t} \left(D _ {S} | 2 \alpha , a _ {M} \mu_ {2} (\hat {o}) + k _ {M}, \frac {a _ {V} + a _ {M} ^ {2} \tau_ {2}}{\alpha \beta_ {2} (\hat {o})}\right).\tag{3.6}
$$

From the Bayesian updating process outlined above, we know that the observation value o^ affects the posterior variance in our model. Let's explore the impact brought by different o^ on the prior variance and posterior variance of $D _ { S } .$ We represent the prior variance of $D _ { S }$ and the posterior variance of $D _ { S }$ (for given o^) by $S _ { V , 1 }$ and $S _ { V , 2 } | \hat { O } ,$ , respectively. With the marginal prior and posterior distributions for $D _ { S } ,$ we can derive $S _ { V , 1 }$ and $S _ { V , 2 } | \hat { o }$ as follows,

![](/api/attachments/56R7Y4YC/fulltext/images/3d5deec3c5b3521d538a21d9edd5aa5383d7488356e079aa2670ce30ce9aaa8e.jpg)  
Fig. 1. Timeline of the forecast updating model.

$$
S _ {V, 1} = \frac {a _ {V} + a _ {M} ^ {2} \tau_ {1}}{(\alpha - 1) \beta_ {1}},\tag{3.7}
$$

$$
S _ {V, 2} | \hat {o} = \frac {a _ {V} + a _ {M} ^ {2} \tau_ {2}}{(\alpha - 1) \beta_ {2} (\hat {o})}.\tag{3.8}
$$

Proposition 3.1. When the means of $D _ { S }$ and $D _ { O }$ are insignificantly correlated, i.e. $a _ { M } \to 0 ,$ information revision on the demand variance not only does not reduce but may also increase the demand variance, i.e. $S _ { V , 2 } \vert \hat { o } \geq S _ { V , 1 }$

Proposition 3.1 implies an interesting <sup>fi</sup>nding that sometimes observation on $D _ { O }$ cannot improve but even degrade the forecast accuracy with respect to yielding a higher posterior variance of $D _ { S } .$ . One would then wonder under what conditions of $\cdot  { \boldsymbol { a } } _ { M }$ and $a _ { V }$ will lead to signi<sup>fi</sup>cant forecast updating with a reduced (expected) demand variance. De<sup>fi</sup>ne:

$$
\sqrt {H (\alpha)} = \gamma (\alpha + 0. 5) \gamma (\alpha - 0. 5) [ \gamma (\alpha) ] ^ {- 2},\tag{3.9}
$$

$$
A (a _ {M}, a _ {V}) = \sqrt {a _ {V} + a _ {M} ^ {2} \tau_ {1}} - \sqrt {H (\alpha)} \sqrt {a _ {V} + a _ {M} ^ {2} \tau_ {2}},\tag{3.10}
$$

$$
\tilde {a} _ {M} = \sqrt {\frac {(H (\alpha) - 1) a _ {V}}{\tau_ {1} - H (\alpha) \tau_ {2}}},\tag{3.11}
$$

$$
\overline {{a}} _ {V} = \frac {a _ {M} ^ {2} (\tau_ {1} - H (\alpha) \tau_ {2})}{H (\alpha) - 1}.\tag{3.12}
$$

Proposition 3.2. (a) $E _ { \hat { o } } \left[ S _ { V , 2 } | \hat { o } \right] < S _ { V , 1 }$ if and only $i f A ( a _ { M } , a _ { V } ) > 0 .$ . (b) The forecast updating process will lead to a smaller expected demand variance $i f$ and only if (i) $a _ { M } > \tilde { a } _ { M }$ (for a fixed a ), or (ii) $0 < a _ { V } < \overline { { a } } _ { V }$ (for a fixed $a _ { M } )$

Proposition 3.2 gives a very neat analytical result on “when the forecast updating process can lead to a smaller expected demand variance”. This is an important <sup>fi</sup>nding because it means that a blind selection of poor observation target will lead to a poor forecasting result. Here, we speci<sup>fi</sup>cally de<sup>fi</sup>ne a good forecasting target to be the one with a larger $a _ { M }$ and a small a . As a remark, for Proposition 3.2: Please observe that $\mathrm { ( i ) } \sqrt { H ( \alpha ) } > 1$ (see Appendix for the proof), and (ii) to have meaningful analysis and results, we assume that $1 + \tau _ { 1 } > H ( \alpha ) \Leftrightarrow \tau _ { 1 } - H ( \alpha ) \tau _ { 2 } > 0$ . Notice that this assumption is very mild and should always hold in practice because $H ( \alpha )$ is always close to 1 and $\tau _ { 1 }$ is positive.

## 4. Supply chain mode

We then derive the optimal order quantities, expected quantities of goods sold, expected quantities of goods leftover, and expected pro<sup>fi</sup>ts for the retailer under the popular returns policy, with and without the forecast updating on $D _ { S } .$ We <sup>fi</sup>rst de<sup>fi</sup>ne the cost and revenue structure in the supply chain. We consider a single supplier single retailer supply chain selling a newsvendor type of fashion product in a single selling season. The unit product's retail selling price is r, the unit wholesale price is c. Unsold product with the retailer by the end of the selling season can be returned to the supplier at a buyback price of b and will <sup>fi</sup>nally be salvaged by the manufacturer at a unit value of v. The production cost of the product by the manufacturer is m per unit. To avoid trivial cases, we have $r > c > b > \nu ,$ and $c > m > \nu .$ Note that this model is classic and is widely used in the literature (e.g., [24]). De<sup>fi</sup>ne:

$$
s = (r - c) / (r - b),\tag{4.1}
$$

where s is the inventory service level with respect to the classic newsvendor problem's optimal fractile quantity [9].

## 4.1. Without forecast updating

With this simple model, when there is no forecast updating, the retailer will place the order at Stage 1 without making any observation. The retailer needs to determine an inventory level q to maximize the following expected pro<sup>fi</sup>t function $E [ P _ { 1 } ( q ) ]$ .

$$
E [ P _ {1} (q) ] = \int_ {- \infty} ^ {q} r x f _ {1} (x) d x + \int_ {q} ^ {\infty} r q f _ {1} (x) d x + b \int_ {- \infty} ^ {q} (q - x) f _ {1} (x) d x - c q.
$$

The above problem follows the classic newsvendor model and the optimal order quantity is given as follows:

$$
q _ {1} = a _ {M} \mu_ {1} + k _ {M} + F _ {2 \alpha} ^ {- 1} (s) \sqrt {\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) / \alpha \beta_ {1}},\tag{4.2}
$$

where $F _ { 2 \alpha } ^ { - 1 } ( \cdot )$ is the inverse function of $F _ { 2 \alpha } ( \cdot )$ , and $F _ { 2 \alpha } ( \cdot )$ is the cdf of a standardized t-distribution $f _ { t } ( \cdot | 2 \alpha \ , 0 \ , 1 )$

The retailer's expected pro<sup>fi</sup>t with q can hence be derived as follows,

$$
E P _ {1} ^ {R} = (r - c) \left(a _ {M} \mu_ {1} + k _ {M}\right) - \left[ (c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s) \right] \sqrt {\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) / \alpha \beta_ {1}},\tag{4.3}
$$

where $B _ { 2 \alpha } ( s ) = \int \mathbf { \Phi } _ { F _ { 2 \alpha } ^ { - 1 } ( s ) } ^ { \infty } \Bigl [ x - F _ { 2 \alpha } ^ { - 1 } ( s ) \Bigr ] f _ { t } ( x | 2 \alpha , \ 0 , \ 1 ) d x .$

With the optimal order quantity q , the expected quantity of product sold during the season (ES<sup>R</sup>) is: $E S _ { 1 } ^ { R } = \int \mathbf { \Omega } _ { - \infty } ^ { q _ { 1 } } x f _ { 1 } ( x ) d x + \int \mathbf { \Omega } _ { q _ { 1 } } ^ { \infty } q _ { 1 } f _ { 1 } ( x ) d x =$ $( a \mu _ { 1 } + b ) - B _ { 2 \alpha } ( s ) \sqrt { ( a _ { V } + a _ { M } ^ { 2 } \tau _ { 1 } ) / \alpha \beta _ { 1 } }$ , and the expected quantity of unsold product at the end of the selling season, EL<sup>R</sup>, is equal to $q _ { 1 } - E S _ { 1 } ^ { R } ;$

$$
E L _ {1} ^ {R} = \left(F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s)\right) \sqrt {\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) / \alpha \beta_ {1}}.\tag{4.4}
$$

Observe from (4.4) that since $E L _ { 1 } ^ { R } \geq 0 ,$ we have:

$$
\left(F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s)\right) \geq 0.\tag{4.5}
$$

## 4.2. With forecast updating

We now consider the case when the supplier contributes the demand information o^ to the retailer and the retailer can order at Stage 2. Under this case, we can derive the unconditional expected optimal quantity, expected pro<sup>fi</sup>t, expected product leftover as follows (the derivations are included in Appendix).

$$
q _ {2} = a _ {M} \mu_ {1} + k _ {M} + F _ {2 \alpha} ^ {- 1} (s) \sqrt {\frac {H (\alpha) (a _ {V} + a _ {M} ^ {2} \tau_ {2})}{\alpha \beta_ {1}}},\tag{4.6}
$$

$$
E P _ {2} ^ {R} = (r - c) \left(a _ {M} \mu_ {1} + k _ {M}\right) - \left[ (c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s) \right] \sqrt {\frac {H (\alpha) \left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right)}{\alpha \beta_ {1}}},\tag{4.7}
$$

$$
E L _ {2} ^ {R} = \left(F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s)\right) \sqrt {\frac {H (\alpha) \left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right)}{\alpha \beta_ {1}}}.\tag{4.8}
$$

In addition, we can derive the expected pro<sup>fi</sup>ts of the supplier at Stage $1 \ ( E P _ { 1 } ^ { S u p p l i e r } )$ and Stage $2 \ ( E P _ { 2 } ^ { \mathsf { S u p p } l i e r } )$ under the returns policy:

$$
E P _ {1} ^ {\text { Supplier }} = (c - m) q _ {1} ^ {R} - (b - v) E L _ {1} ^ {R},\tag{4.9}
$$

$$
E P _ {2} ^ {\text { Supplier }} = (c - m) q _ {2} ^ {R} - (b - v) E L _ {2} ^ {R}.\tag{4.10}
$$

## 5. Effects of forecast updating

To explore the effects of forecast updating, we <sup>fi</sup>rst de<sup>fi</sup>ne the expected gain from forecast updating for the retailer and the supplier respectively as follows: $\Delta E P ^ { R } = \dot { E } P _ { 2 } ^ { R } - \check { E } P _ { 1 } ^ { R } , \Delta E P ^ { S u p p l i e r } = E P _ { 2 } ^ { S u p p l i e \hat { r } } - E P _ { 1 } ^ { S u p p l i e n }$ . Simple algebra gives (5.1) and (5.2):

$$
\Delta E P ^ {R} = A (a _ {M}, a _ {V}) \left(\frac {(c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s)}{\alpha \beta_ {1}}\right),\tag{5.1}
$$

$$
\Delta E P ^ {\text { Supplier }} = A (a _ {M}, a _ {V}) \left[ (b - v) \left(B _ {2 \alpha} (s) + F _ {2 \alpha} ^ {- 1} (s)\right) - (c - m) F _ {2 \alpha} ^ {- 1} (s) \right].\tag{5.2}
$$

We further de<sup>fi</sup>ne the supply chain surplus as gained by the forecast update in the presence of the returns policy:

$$
\Delta E P ^ {S C} = \Delta E P ^ {R} + \Delta E P ^ {\text { Supplier }}.\tag{5.3}
$$

For a notational purpose, we have the following:

$$
\xi = \frac {(c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s)}{\alpha \beta_ {1}} - (c - m) F _ {2 \alpha} ^ {- 1} (s).\tag{5.4}
$$

Proposition 5.1. (a) For the retailer, forecast updating will bring an expected gain $( i . e . , \Delta E P ^ { R } > 0 )$ if and only if $a _ { M } > \tilde { a } _ { M }$ (for a fixed $\textstyle { a _ { V } } )$ or $0 < a _ { V } < \overline { { a } } _ { V }$ (for a fixed a ). (b) For the retailer, forecast updating will bring an expected loss (i.e. $\Delta E P ^ { R } < 0 )$ if and only if $a _ { M } < \widetilde { a } _ { M }$ (for a fixed a ), or $a _ { V } > \overline { { a } } _ { V }$ (for a fixed a<sub>M</sub>). (c) If a $> \tilde { a } _ { M }$ (for a fixed a<sub>V</sub>), or $0 < a _ { V } < \overline { { a } } _ { V }$ (for a fixed $a _ { M } ) : \partial \Delta E P ^ { R } / \partial a _ { M } > 0$ and $\partial \Delta E P ^ { R } / \partial a _ { V } < 0 .$

Notice that from Propositions 3.2 and 5.1, we can see the interesting linkage that when the expected posterior variance of $D _ { S }$ becomes smaller than its prior variance, the retailer's expected pro<sup>fi</sup>t is also improved after the forecast updating. As a result, the required condition for the retailer's achievements of both a reduction of expected variance of demand and an improvement of expected pro<sup>fi</sup>t via forecast updating is the same.

Proposition 5.2. In the absence of the returns policy $( b = \nu ) ^ { 7 }$ and for a service level $s > 0 . 5 ; ( a ) \ \Delta E P ^ { R }$ and $\Delta E P ^ { S u p p l i e r }$ are negatively correlated. (b) The supplier has an incentive to provide information which is useless or even harmful to the retailer. (c) The supply chain is benefitted (i.e., the supply chain surplus $\Delta E P ^ { S C }$ is strictly positive) if and only $i f A ( a _ { M } , a _ { V } ) \zeta > 0 .$

Proposition 5.2 implies when there is no returns policy and the service level requirement is fairly large (>50%), the supplier has an incentive to share information which bene<sup>fi</sup>ts himself, however, may be useless or even hurt the retailer. Thus, sharing mutually bene<sup>fi</sup>cial information in the supply chain cannot be taken for granted because of the incentive difference between the retailer and the supplier. Proposition 5.2c further presents the analytical conditions under which the whole supply chain system will be bene<sup>fi</sup>tted under the information sharing scheme. Notice from Proposition 5.2b that since $\Delta E P ^ { R }$ and $\Delta E P ^ { S u p p l i e r }$ are negatively correlated, the condition on $A ( a _ { M } , a _ { V } ) \zeta >$ 0 implies that the supply chain will have an expected pro<sup>fi</sup>t gain under the scenario on either (i) the retailer's expected pro<sup>fi</sup>t gain from information update is larger than the respective supplier's expected pro<sup>fi</sup>t loss $( \mathrm { i . e . , } A ( a _ { M } , a _ { V } ) > 0$ and $\zeta > 0 )$ or (ii) the retailer's expected pro<sup>fi</sup>t loss from information update is smaller than the respective supplier's expected pro<sup>fi</sup>t gain $( A ( a _ { M } , a _ { V } ) < 0$ and $\zeta < 0 )$ . As a remark, when the supply chain is bene<sup>fi</sup>tted by information updating: For the case when the supplier suffers a loss, a probable remedial solution is for the retailer to provide a monetary transfer to the supplier.<sup>8</sup>

De<sup>fi</sup>ne: $b _ { \mathrm { m a x } } ^ { \ast } = \underset { b } { \arg \left\{ \left[ ( b - \nu ) \left( B _ { 2 \alpha } ( s ) + F _ { 2 \alpha } ^ { - 1 } ( s ) \right) - ( c - m ) F _ { 2 \alpha } ^ { - 1 } ( s ) \right] = 0 \right\} }$

Proposition 5.3. If $a _ { M } > \tilde { a } _ { M }$ (for a fixed $\boldsymbol { a _ { V } } )$ , or $0 < a _ { V } < \overline { { a } } _ { V }$ (for a fixed $a _ { M } )$ holds: (a) The supplier will achieve a higher expected profit $( i . e . , \Delta E P ^ { S u p p l i e r } > 0 )$ if he sets a returns policy with $\nu < b < r - 2 c .$ (b) The supplier will achieve a higher expected profit $( i . e . , \Delta E P ^ { S u p p l i e r } > 0 )$ if and only if he sets a returns policy with $\nu < b < { b _ { \mathrm { m a x } } } ^ { * }$

In Proposition 5.3a, the condition $\nu < b < r - 2 c$ is a suf<sup>fi</sup>cient but not necessary one while the condition of $\nu < b < { b _ { \mathrm { m a x } } } ^ { * }$ in Proposition 5.3b is necessary and suf<sup>fi</sup>cient. The establishment of the returns policy following $\nu < b < r - 2 c$ is easy and is even independent of the demand distribution. However, the most comprehensive condition for setting the returns policy requires the solving of $b _ { \mathrm { m a x } } ^ { * }$ which is computationally more involved and also dependent of the parameters of the given demand distribution. Following the results from Propositions 5.1 and 5.2, we summarize the key insights in Theorem 5.4 below.

Theorem 5.4. The supplier can create a win–win situation in the supply chain by offering: (i) The demand forecast information with either feature: $a _ { M } > \tilde { a } _ { M }$ (for a fixed $\boldsymbol { a _ { V } } )$ , or $\scriptstyle 0 < a _ { V } < \overline { { a } } _ { V }$ (for a fixed $a _ { M } )$ , and (ii) a returns policy with a buyback price $\nu < b < { b _ { \mathrm { m a x } } } ^ { * }$

As a remark, the analytical results which hold for the returns policy will probably also hold for some other contracts such as revenue sharing. As a matter of fact, Cachon and Lariviere [4] have proven that the revenue sharing contract and the returns policy are basically equivalent in their performance of coordinating the quantity only decision in a two-echelon supply chain with a newsvendor kind of product. As a result, if the revenue sharing contract is present instead of the returns policy, very similar <sup>fi</sup>ndings as shown in this paper should be obtained. For other supply contracts such as target sales rebates contract and quantity <sup>fl</sup>exibility contract, we believe that some similar <sup>fi</sup>ndings on the role played by the supply contracts in information sharing mechanism will be obtained because all these contracts have the feature of enhancing supply chain's performance (i.e., generating surplus by dampening double marginalization effect and incentive differences) and providing a way of allocating the supply chain surplus between the supplier and the retailer. Of course, the speci<sup>fi</sup>c analytical conditions will be different and we postpone the detailed analysis to future research.

## 6. Conclusion and managerial insights

Information sharing has been known to be crucial in supply chain management. As motivated by various industrial practices, this paper analytically explores the information sharing issues, from upstream supplier to downstream retailer, in a two-echelon supply chain. We consider the case where the supplier can offer the demand data of a pre-seasonal product to the retailer so that the retailer, by postponing the ordering time point and incorporating this piece of information into the forecast updating process, can potentially make a better inventory decision. By formally modeling the respective supply chain with a Bayesian forecast updating process and returns policy, we have derived the closed-form expressions of the expected pro<sup>fi</sup>ts for the retailer and the supplier. Effects on information sharing and forecast updating are then investigated. Our analysis has revealed the following insights:

1. Demand information with “low relevance” can lead to a poorer forecast and hence results in an expected loss. This <sup>fi</sup>nding is interesting and it means that if the retailer blindly takes and employs the demand of a pre-seasonal product which is very weakly related to the demand of the seasonal product to revise her forecast, it will not only result in a poor forecast but also an expected loss. This <sup>fi</sup>nding provides an analytical evidence to support the idea of harmful forecast updating with bad information. To the best of our knowledge, this paper is the <sup>fi</sup>rst piece of work which provides an analytical evidence to support this argument.

2. In the presence of returns policy, the expected gain of forecast updating highly depends on the correlations between the item under forecast and the observation target. While this might be expected, we speci<sup>fi</sup>cally examine the correlations in two dimensions, namely the “mean” and the “variance” (between the item under forecast and the observation target). In particular, our <sup>fi</sup>ndings include: (a) When the pre-seasonal product's mean of demand is highly correlated to the seasonal product's mean of demand, the expected gain is high. This gain is actually increasing in the coef<sup>fi</sup>cient a . (b) On the contrary, for the correlation between the two product demands' variances, the smaller the corresponding coef<sup>fi</sup>cient will lead to a bigger expected gain from forecast updating. This gain is decreasing with respect to the value of the coef<sup>fi</sup>cient $a _ { V }$ . The analytical bounds to achieve a positive expected gain of forecast updating for both $a _ { M }$ and $a _ { V }$ are also derived. They provide a good reference for the classi<sup>fi</sup>cation of good and bad pre-seasonal products to be the right information source under the returns policy.

3. An important and interesting topic of this paper is to address the potential incentive difference between the supplier and the retailer. Our analysis has revealed that the supplier's expected gain from offering the demand data of the pre-seasonal product and the retailer's expected gain from making use of this piece of information in revising forecast are negatively correlated in the absence of the returns policy. On the contrary, they are positively correlated only in the presence of the returns policy. Thus, with the returns policy, selecting a pre-seasonal product with a high $A ( a _ { M } , a _ { V } )$ will bene<sup>fi</sup>t both the supplier and the retailer and this gives the incentive for the supplier to offer high quality information (i.e., big $A ( a _ { M } , a _ { V } ) ,$ .

4. In the supply chain that we have explored in this paper, we have shown that win–win coordination can be achieved by using a proper returns policy (with the respective parameters found) and providing demand information from a good pre-seasonal product. The explicit bounds for the parameters have been analytically derived.

For the research limitations, we admit that the <sup>fi</sup>ndings are mainly based on the analytical models we have developed under various assumptions such as the speci<sup>fi</sup>c Bayesian information updating process and prior distribution. In addition, the analysis is conducted on a relatively simple two-echelon supply chain which is an abstract version of the more complex real world supply chain. For future research, it is interesting to extend the model and analysis to more complex supply chain systems (such as the ones with information asymmetry [22]). It is also meaningful to investigate whether it is bene<sup>fi</sup>cial for the supplier to always share real information, or a fake one can be bene<sup>fi</sup>cial under some circumstances. This would address another important perspective of information sharing in supply chain management.

## Appendix

Derivation of (3.5), which follows the approach in [3,10]:

$$
\begin{array}{l} f _ {1} (D _ {S}) = \int_ {0} ^ {\infty} \int_ {- \infty} ^ {\infty} f _ {N} (D _ {S} | S _ {M}, S _ {V}) f _ {N} \bigg (S _ {M} | a _ {M} \mu_ {1} + k _ {M}, \frac {a _ {M} ^ {2} \tau_ {1}}{a _ {V}} S _ {V} \bigg) f _ {I G} \bigg (S _ {V} | \alpha , \frac {\beta_ {1}}{a _ {V}} \bigg) d S _ {M} d S _ {V} \\ = \int_ {0} ^ {\infty} f _ {N} \bigg (D _ {S} | a _ {M} \mu_ {1} + k _ {M}, \bigg (1 + \frac {a _ {M} {} ^ {2} \tau_ {1}}{a _ {V}} \bigg) S _ {V} \bigg) f _ {I G} \bigg (S _ {V} | \alpha \frac {\beta_ {1}}{a _ {V}} \bigg) d S _ {V} \\ = \int_ {0} ^ {\infty} \frac {1}{\sqrt {2 \pi (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V}) S _ {V}}} e ^ {- \frac {[ D _ {S} - (a _ {M} \mu_ {1} + k _ {M}) ] ^ {2}}{2 (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V}) S _ {V}}} \frac {e ^ {- a _ {V} / (S _ {V} \beta_ {1})}}{\Gamma (\alpha) (\beta_ {1} / a _ {V}) ^ {\alpha} S _ {V} ^ {\alpha + 1}} d S _ {V} \\ = \frac {1}{\sqrt {2 \pi (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V})}} \int_ {0} ^ {\infty} e ^ {- \frac {[ D _ {S} - (a _ {M} \mu_ {1} + k _ {M}) ] ^ {2}}{2 (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V}) S _ {V}}} \frac {e ^ {- a _ {V} / (S _ {V} \beta_ {1})}}{\Gamma (\alpha) (\beta^ {\prime} / a _ {V}) ^ {\alpha} S _ {V} ^ {\alpha + 1 . 5}} d W \\ = \frac {1}{\sqrt {2 \pi (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V})}} \int_ {0} ^ {\infty} e ^ {- \left(\frac {[ D _ {S} - (a _ {M} \mu_ {1} + k _ {M}) ] ^ {2}}{2 (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V})} + \frac {a _ {V}}{\beta_ {1}}\right) \left(\frac {1}{S _ {V}}\right)} \\ \frac {1}{\Gamma (\alpha) (\beta_ {1} / a _ {V}) ^ {\alpha} S _ {V} ^ {\alpha + 1 . 5}} d S _ {V} \\ = \frac {1}{\sqrt {2 \pi (1 + a _ {M} {} ^ {2} \tau_ {1} / a _ {V})}} \int_ {0} ^ {\infty} e ^ {- \left(\frac {[ D _ {S} - (a _ {M} \mu_ {1} + k _ {M}) ] ^ {2}}{2 (1 + a _ {M} {} ^ {- 2} \tau_ {1} / a _ {V})} + \frac {a _ {V}}{\beta_ {1}}\right) \left(\frac {1}{S _ {V}}\right)} \\ \frac {1}{\Gamma (\alpha) (\beta_ {1} / a _ {V}) ^ {\alpha} S _ {V} ^ {\alpha + 1 . 5}} d S _ {V}. \end{array}
$$

With the above result and noting that $\int \displaylimits _ { 0 } ^ { \infty } e ^ { - \frac { 1 } { B S _ { V } } }$ $\begin{array} { r } { \frac { 1 } { \Gamma ( \alpha + 0 . 5 ) B ^ { \alpha + 1 / 2 } S _ { V } \alpha + 1 . 5 } d S _ { V } = 1 } \end{array}$ , where $\begin{array} { r } { B = \left( \frac { [ D _ { S } - ( a _ { M } \mu _ { 1 } + k _ { M } ) ] ^ { 2 } } { 2 ( 1 + a _ { M } 2 \tau _ { 1 } / a _ { V } ) } + \frac { a _ { V } } { \beta _ { 1 } } \right) ^ { - 1 } } \end{array}$ , we can express $f _ { 1 } ( D _ { S } )$ as a t-distribution in the following, $f _ { 1 } ( D _ { S } ) =$ $\begin{array} { r } { f _ { t } \Big ( D _ { S } | 2 \alpha , a _ { M } \mu _ { 1 } + k _ { M } , \frac { a _ { V } + a _ { M } ^ { 2 } \tau _ { 1 } } { \alpha \beta _ { 1 } } \Big ) } \end{array}$

Proof of Proposition 3.1. Notice that when $a _ { M } \to 0 ,$ , since $\alpha > 2$ and $\beta _ { 2 } ( \hat { o } ) { \leq } \beta _ { 1 }$ , directly comparing $S _ { V , 1 }$ and $S _ { V , 2 } | \hat { o }$ gives:

$$
\frac {S _ {V , 2} | \hat {o}}{S _ {V , 1}} = \frac {\left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right) \beta_ {1}}{\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) \beta_ {2} (\hat {o})} = \frac {\beta_ {1}}{\beta_ {2} (\hat {o})} \geq 1 \Longleftrightarrow S _ {V, 2} | \hat {o} \geq S _ {V, 1}.\tag{A1.1}
$$

The equal sign in the inequality applies only when $\hat { o } = \mu _ { 1 }$

(Q.E.D.)

## Proof of Proposition 3.2.

a) Since $\begin{array} { r } { f _ { 2 } ( D _ { S } | \hat { o } ) = f _ { t } \Big ( D _ { S } | 2 \alpha , a _ { M } \mu _ { 2 } ( \hat { o } ) + k _ { M } , \frac { a _ { V } + a _ { M } ^ { 2 } \tau _ { 2 } } { \alpha \beta _ { 2 } ( \hat { o } ) } \Big ) } \end{array}$ , the expected variance of $D _ { S } | \hat { o }$ at Stage 2 is given as follows,

$$
\begin{array}{l} E _ {o} ^ {\hat {}} [ S _ {V, 2} | \hat {o} ] = \sqrt {H (\alpha)} \sqrt {\frac {a _ {V} + a _ {M} ^ {2} \tau_ {2}}{\alpha \beta_ {1}}} \\ \text { Thus: } E _ {o} ^ {\hat {}} [ S _ {V, 2} | \hat {o} ] <   S _ {V, 1} \Longleftrightarrow \sqrt {H (\alpha)} \sqrt {\frac {a _ {V} + a _ {M} ^ {2} \tau_ {2}}{\alpha \beta_ {1}}} <   \sqrt {\frac {a _ {V} + a _ {M} ^ {2} \tau_ {1}}{\alpha \beta_ {1}}} \Longleftrightarrow A (a _ {M}, a _ {V}) > 0. \end{array}\tag{Q.E.D.}
$$

b) First of all, from (A1.1), we have: When $a _ { M }  0 , \quad S _ { V , 2 } | \hat { o } >$ $\textstyle S _ { V , 1 } , \forall \hat { o } \neq \mu _ { 1 }$ . Under this case, taking expectation on both sides yields (when $a _ { M } \to 0 ) \colon E _ { \hat { o } } [ S _ { V , 2 } | \hat { o } ] > S _ { V , 1 }$ . Thus, we have

$$
\frac {E _ {\hat {o}} \left[ S _ {V , 2} | \hat {o} \right]}{S _ {V , 1}} > 1 \Rightarrow \sqrt {H (\alpha)} > 1.\tag{A2.1}
$$

Secondly, since $E _ { \hat { o } } \left[ S _ { V , 2 } | \hat { o } \right] < S _ { V , 1 } \Longleftrightarrow \mathsf { A } ( a _ { M } , a _ { V } ) > 0 \Longleftrightarrow \sqrt { a _ { V } + a _ { M } ^ { 2 } \tau _ { 1 } - }$ $\sqrt { H ( \alpha ) } \sqrt { a _ { V } + a _ { M } ^ { 2 } \tau _ { 2 } } > 0 ,$ , by rearranging terms and noticing that $a _ { M } \geq 0 , a _ { V } > 0 ,$ , we have:

$$
\begin{array}{l} \mathrm{A} (a _ {M}, a _ {V}) > 0 \Longleftrightarrow a _ {M} > \tilde {a} _ {M} = \sqrt {\frac {(H (\alpha) - 1) a _ {V}}{\tau_ {1} - H (\alpha) \tau_ {2}}}, \\ \mathrm{A} (a _ {M}, a _ {V}) > 0 \Longleftrightarrow a _ {V} <   \overline {{a}} _ {V} = \frac {a _ {M} ^ {2} (\tau_ {1} - H (\alpha) \tau_ {2})}{H (\alpha) - 1}. \end{array}\tag{Q.E.D.}
$$

Derivations of the unconditional expected values of the posterior optimal ordering quantity, the posterior expected pro<sup>fi</sup>t, and the posterior expected product leftover:

Firstly, notice that at Stage 1, the unconditional distribution of o^ can be derived as follows,

$$
\begin{array}{l} f _ {1} (\hat {o}) = \int_ {0} ^ {\infty} \int_ {- \infty} ^ {\infty} f _ {N} (\hat {o} | M, V) f _ {N} (M | \mu_ {1}, \tau_ {1} V) f _ {I G} (V | \alpha , \beta_ {1}) d M d V \\ = f _ {t} \big (\hat {o} | 2 \alpha , \mu_ {1}, ((1 + \tau_ {1}) / (\alpha \beta_ {1})) \end{array}\tag{A3.1}
$$

Secondly, at Stage 2, the optimal ordering quantity (conditional ono^) is found as,

$$
q _ {2} (\hat {o}) = a _ {M} \mu_ {2} (\hat {o}) + k _ {M} + F _ {2 \alpha} ^ {- 1} (s) \sqrt {\frac {a _ {V} + a _ {M} ^ {2} \tau_ {2}}{\alpha \beta_ {2} (\hat {o})}}.\tag{A3.2}
$$

With $q _ { 2 } ( \hat { o } )$ , the respective optimal expected pro<sup>fi</sup>t at Stage 2 is given by,

$$
\begin{array}{c} E P _ {2} ^ {R} (\hat {o}) = (r - c) (a _ {M} \mu_ {2} (\hat {o}) + k _ {M}) - \Big [ (c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s) \Big ] \\ \sqrt {(a _ {V} + a _ {M} ^ {2} \tau_ {1}) / \alpha \beta_ {2} (\hat {o})}. \end{array}\tag{A3.3}
$$

Similar to the case at Stage 1, we can also derive the expected quantity of goods sold during the season and the expected quantity of product leftover, all conditional on o^ at Stage 2, in the following:

$$
E S _ {2} ^ {R} (\hat {o}) = (a \mu_ {2} (\hat {o}) + b) - \left(B _ {2 \alpha} (s) \sqrt {\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) / \alpha \beta_ {2} (\hat {o})}\right),\tag{A3.4}
$$

$$
E L _ {2} ^ {R} (\hat {o}) = \left[ F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s) \right] \sqrt {\left(a _ {V} + a _ {M} ^ {2} \tau_ {1}\right) / \alpha \beta_ {2} (\hat {o})}.\tag{A3.5}
$$

Taking expectation with respect to o^, we have:

$$
\begin{array}{l} q _ {2} = E _ {\hat {o}} [ q _ {2} (\hat {o}) ] = a _ {M} \mu_ {1} + k _ {M} + F _ {2 \alpha} ^ {- 1} (s) \sqrt {\frac {H (\alpha) \left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right)}{\alpha \beta_ {1}}}, \\ E P _ {2} ^ {R} = E _ {\hat {o}} \left[ E P _ {2} ^ {R} (\hat {o}) \right] = (r - c) (a _ {M} \mu_ {1} + k _ {M}) - \left[ (c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s) \right] \\ \sqrt {\frac {H (\alpha) \left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right)}{\alpha \beta_ {1}}}, \\ E L _ {2} ^ {R} = E _ {\hat {o}} \left[ E L _ {2} ^ {R} (\hat {o}) \right] = \left(F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s)\right) \sqrt {\frac {H (\alpha) \left(a _ {V} + a _ {M} ^ {2} \tau_ {2}\right)}{\alpha \beta_ {1}}}. \end{array}\tag{Q.E.D.}
$$

## Proof of Proposition 5.1.

a) It is straight forward to <sup>fi</sup>nd from the 1st order partial derivative that if $a _ { M } > \tilde { a } _ { M }$ (for a <sup>fi</sup>xed $a _ { V } ) ,$ or $0 < a _ { V } < \overline { { a } } _ { V }$ (for a <sup>fi</sup>xed $a _ { M } ) , \mathrm { A } ( a _ { M } , a _ { V } ) > 0$ which would lead to $\partial \Delta E P ^ { R } / \partial a _ { M } > 0$ and $\partial \Delta E P ^ { R } / \partial a _ { V } < 0 .$

b) First, notice from $\begin{array} { r } { \Delta E P ^ { R } = A ( a _ { M } , a _ { V } ) \left( \frac { ( c - b ) F _ { 2 \alpha } ^ { - 1 } ( s ) + ( r - b ) B _ { 2 \alpha } ( s ) } { \alpha \beta _ { 1 } } \right) } \end{array}$ that

$$
\begin{array}{l} \left(\frac {(c - b) F _ {2 \alpha} ^ {- 1} (s) + (r - b) B _ {2 \alpha} (s)}{\alpha \beta_ {1}}\right) \\ = \left(\frac {(c - b) F _ {2 \alpha} ^ {- 1} (s) + (c - b) B _ {2 \alpha} (s) + (r - c) B _ {2 \alpha} (s)}{\alpha \beta_ {1}}\right) \\ = \frac {(c - b) \left(F _ {2 \alpha} ^ {- 1} (s) + B _ {2 \alpha} (s)\right)}{\alpha \beta_ {1}} + \frac {(r - c) B _ {2 \alpha} (s)}{\alpha \beta_ {1}}. \end{array}\tag{A4.1}
$$

As $( F _ { 2 \alpha } ^ { - 1 } ( s ) + B _ { 2 \alpha } ( s ) ) \ge 0$ (from (3.5)) and $( r - c ) B _ { 2 \alpha } ( s ) > 0 , ( \mathtt { A } 4 . 1 )$ is always positive, we have: $\Delta E P ^ { R } > 0 \ \mathrm { i t }$ and only if $\mathrm { A } ( a _ { M } , a _ { V } ) > 0$ Since $\mathrm { A } ( a _ { M } , a _ { V } ) > 0 \Longleftrightarrow a _ { M } > \tilde { a } _ { M }$ (for a <sup>fi</sup>xed $a _ { V } )$ , or $0 < a _ { V } < \overline { { a } } _ { V }$ (for a <sup>fi</sup>xed $a _ { M } )$ , Proposition 5.1b results.

c) Similar to the proof for part b), with the opposite case. (Q.E.D.)

## Proof of Proposition 5.2.

When $b = v \colon$

(a) We have from (5.1) and (5.2) the following

$$
\Delta E P ^ {R} = A (a _ {M}, a _ {V}) \left(\frac {(c - v) F _ {2 \alpha} ^ {- 1} (s) + (r - v) B _ {2 \alpha} (s)}{\alpha \beta_ {1}}\right),
$$

$$
\Delta E P ^ {\text { Supplier }} = - A (a _ {M}, a _ {V}) (c - m) F _ {2 \alpha} ^ {- 1} (s).
$$

Since $\begin{array} { r } { \left( \frac { ( c - \nu ) F _ { 2 \alpha } ^ { - 1 } ( s ) + ( r - \nu ) B _ { 2 \alpha } ( s ) } { \alpha \beta _ { 1 } } \right) > 0 } \end{array}$ and $F _ { 2 \alpha } ^ { - 1 } ( s ) > 0$ when $s > 0 . 5 ,$ , we conclude that $\Delta E P ^ { R }$ and $\Delta E P ^ { S u p p l i e r }$ are negatively correlated under this service level case.

(b) Since $\Delta E P ^ { S u p p l i e r } = - \ A ( a _ { M } , a _ { V } ) ( c - m ) F _ { 2 \alpha } ^ { - 1 } ( s )$ , which can be negative, the supplier has incentive to provide information which is useless or even harmful to the retailer so that it will be bene<sup>fi</sup>tted.

(c) By de<sup>fi</sup>nition, $\Delta E P ^ { S C } = \Delta E P ^ { R } + \Delta E P ^ { S u p p l i e r }$ . When $b = v ,$ we have: $\Delta E P ^ { S C } = A ( a _ { M } , a _ { V } ) \xi$ . Thus, the supply chain is bene<sup>fi</sup>tted (i.e., the supply chain surplus $\Delta E P ^ { S C }$ is strictly positive) if and only $\mathrm { f } \xi > 0$ and $A ( a _ { M } , a _ { V } ) > 0$ (Q.E.D.)

Proof of Proposition 5.3.

a) First, $\Delta E P ^ { S u p p l i e r } = A ( a _ { M } , a _ { V } ) [ ( b - \nu ) ( B _ { 2 \alpha } ( s ) + F _ { 2 \alpha } ^ { - 1 } ( s ) ) - ( c -$ $m ) F _ { 2 \alpha } ^ { - 1 } ( s ) ]$ . When $a _ { M } > \tilde { a } _ { M }$ (for a <sup>fi</sup>xed $\textstyle { a _ { V } } )$ , or $0 < a _ { V } < \overline { { a } } _ { V }$ holds, ${ \cal A } ( a _ { M } , a _ { V } ) > 0 .$ . Thus, if $[ ( b - \nu ) ( B _ { 2 \alpha } ( s ) + F _ { 2 \alpha } ^ { - 1 } ( s ) ) - ( c - m ) F _ { 2 \alpha } ^ { - 1 } ( s ) ]$ is positive, $\Delta E P ^ { S u p p l i e r }$ is positive. A suf<sup>fi</sup>cient condition to ensure $[ ( b - \nu ) ( B _ { 2 \alpha } ( s ) + F _ { 2 \alpha } ^ { - 1 } ( s ) ) - ( c - m ) F _ { 2 \alpha } ^ { - 1 } ( s ) ]$ to be positive is $s < 0 . 5$ which means $F _ { 2 \alpha } ^ { - 1 } ( s ) < 0 .$ . Since $\begin{array} { r } { s < 0 . 5 \Longleftrightarrow \frac { r - c } { r - b } < 0 . 5 \Longleftrightarrow b < } \end{array}$ r−2c and $b > \nu$ (model requirement), we have $\nu < b < r - 2 c$

b) Following the argument in a), since $b _ { \mathrm { m a x } } ^ { * }$ is the buyback price which makes $[ ( b - \nu ) ( B _ { 2 \alpha } ( s ) + F _ { 2 \alpha } ^ { - 1 } ( s ) ) - ( c - m ) F _ { 2 \alpha } ^ { - 1 } ( s ) ] = 0 ,$ a value of $b > b _ { \mathrm { m a x } } ^ { \mathrm { ~ * ~ } }$ will lead to a negative $\Delta E P ^ { S u p p l i e r }$ . Thus, the necessary and suf<sup>fi</sup>cient range is given by $\nu < b < { b _ { \mathrm { m a x } } } ^ { * } .$ (Q.E.D.)

## References

[1] K.S. Azoury, Bayes solution to dynamic inventory models under unknown demand distribution, Management Science 31 (1985) 1150–1160

[2] K.S. Azoury, B.L. Miller, A comparison of the optimal ordering levels of Bayesian and non-Bavesian inventory models, Management Science 30 (1984) 993–1003

[3] J.O. Berger, Statistical Decision Theory, Foundations, Concepts and Methods, Springer-Verlag, New York, 1980.

[4] G.P. Cachon, M.A. Lariviere, Supply chain coordination with revenue-sharing contracts: strengths and limitations, Management Science 51 (2005) 30–44

[5] J. Chen, L. Xu, Coordination of the supply chain of seasonal products, IEEE Transactions on Systems, Man, and Cybernetics — Part A 31 (2001) 524–532.

[6] H. Chen, J. Chen, Y. Chen, A coordination mechanism for a supply chain with demand information updating, International Journal of Production Economics 103 (2006) 347–361.

[7] H. Chen, Y.H. Chen, C.H. Chiu, T.M. Choi, S. Sethi, Coordination mechanism for supply chain with leadtime consideration and price-dependent demand, European Journal of Operational Research 203 (2010) 70–80.

[8] C.H. Chiu, T.M. Choi, C.S. Tang, Price, rebate, and returns supply contracts for coordinating supply chains with price dependent demands, Production and Operations Management 20 (2011) 81–91.

[9] In: T.M. Choi (Ed.), Handbook of Newsvendor Problems, Springer, New York, 2012.

[10] T.M. Choi, D. Li, H. Yan, Quick response policy with Bayesian information updates, European Journal of Operational Research 170 (2006) 788–808.

[11] K.L. Donohue, Ef<sup>fi</sup>cient supply contract for fashion goods with forecast updating and two production modes Management Science 46 (2000) 1397–1411.

[12] A. Dvoretzky, J. Kiefer, J. Wolfowitz, The inventory problem: II. Case of unknown distributions of demand, Econometrica 20 (1952) 450–466

[13] G.D. Eppen, A.V. Iyer, Backup agreements in fashion buying — the value of upstream <sup>fl</sup>exibility, Management Science 43 (1997) 1469–1484.

[14] J. Fraser, CPFR — status and perspective, in: D. Seifert (Ed.), Collaborative Planning, Forecasting and Replenishment: How to Create a Supply Chain Advantage, AMACOM. N.Y., 2003, pp. 70–93.

[15] H. Gurnani, C.S. Tang, Optimal ordering decisions with uncertain cost and demand forecast updating, Management Science 45 (1999) 1456–1462.

[16] A.V. Iyer, M.E. Bergen, Quick response in manufacturer-retailer channels, Management Science 43 (1997) 559–570.

[17] H.L. Lee, V. Padmanabhan, S. Whang, Information distortion in a supply chain: the bullwhip effect, Management Science 43 (1997) 546–558

[18] H.L. Lee, K.C. So, C.S. Tang, The value of information sharing in a two-level supply chain, Management Science 46 (2000) 626–643.

[19] W.Y. Liang, C.C. Huang, Agent-based demand forecast in multi-echelon supply chain, Decision Support Systems 42 (2006) 390–407.

[20] B. Liu, J. Chen, S. Liu, R. Zhang, Supply-chain coordination with combined contract for a short-life-cycle product, IEEE Transactions on Systems, Man, and Cybernetics — Part A 36 (2006) 53–61.

[21] S.K. Mukhopadhyay, R. Setaputra, A dynamic model for optimal design quality and return policies, European Journal of Operational Research 180 (2007) 1144–1154.

[22] S.K. Mukhopadhyay, X. Yue, X. Zhu, A Stackelberg model of pricing of complementary goods under information asymmetry, International Journal of Production Economics 134 (2009) 424–433

[23] G.R. Murray, E.A. Silver, A Bayesian analysis of the style goods inventory problem, Management Science 12 (1966) 785–797

[24] B.A. Pasternack, Optimal pricing and returns policies for perishable commodities, Marketing Science 4 (1985) 166–176.

[25] A. Prasad, K.E. Stecke, X. Zhao, Advance selling by a newsvendor retailer, Production and Operations Management 20 (2011) 129–142.

[26] S. Raghunathan, Impact of demand correlation on the value of and incentives for information sharing in a supply chain, European Journal of Operational Research 146 (2003) 634–649.

[27] H. Scarf, Bayes solutions of the statistical inventory problem, Annals of Mathematical Statistics 30 (1959) 490–508

[28] C.S. Tang, K. Rajaram, A. Alptekinoglu, J. Ou, The bene<sup>fi</sup>ts of advanced booking discount programs: model and analysis Management Science 50 (2004) 465–478

[29] T.A. Taylor, W. Xiao, Does a manufacturer bene<sup>fi</sup>t from selling to a better forecast retailer? Management Science 56 (2010) 1584–1598.

[30] W.T. Wang, H.M. Wee, H.S.J. Tsao, Revisiting the note on supply chain integration in vendor-managed inventory, Decision Support Systems 48 (2010) 419–420.

[31] D. Yang, T.M. Choi, T. Xiao, T.C.E. Cheng, Coordinating a two-supplier and one-retailer supply chain with forecast updating, Automatica 47 (2011) 1317–1329.

[32] X. Zhang, Y. Zhao, The impact of external demand information on parallel supply chains with interacting demand, Production and Operations Management 19 (2010) 463–479.

![](/api/attachments/56R7Y4YC/fulltext/images/265874b80dff07dadd7278338bd5c5d21c29e2315b69a475db8efb7f426397b2.jpg)

Tsan-Ming Choi is currently an associate professor at The Hong Kong Polytechnic University. His current research interests mainly focus on information systems and supply chain management. He has published over 100 technical papers in leading academic journals including Annals of Operations Research, Automatica, Decision Support Systems European Journal of Operational Research, IEEE Transactions on Automatic Control, Production and Operations Management, Service Science, and several other leading IEEE Transactions and OR/MS journals. He has authored/edited ten research handbooks and guest-edited twelve special issues in academic journals. He is currently an area editor/associate editor/guest editor of Annals of Operations Research, Deci sion Sciences, Decision Support Systems, European Manage-

ment Journal, IEEE Transactions on Systems, Man, and Cybernetics — Systems, Information Sciences, Production and Operations Management, among others

![](/api/attachments/56R7Y4YC/fulltext/images/a5e0f14433ed97ad635ad879a62d35ab56c47373019dcef2d2c8a60c1a9d37e4.jpg)

![](/api/attachments/56R7Y4YC/fulltext/images/c3b3bcc726904154cdae1fc40fbbbc11d9e9b6670a3276754339d4294ff06a0e.jpg)

Jian Li received his Ph.D. degree from Academy of Mathematics and Systems Science, Chinese Academy of Sciences (CAS). He is currently a professor at the School of Economics and Management of Beijing University of Chemical Technology. He has published over 20 papers in leading journals including International Journal of Production Economics and OMEGA. His research interests include supply chain management and risk analysis.

Ying Wei received her Ph.D. from The Chinese University of Hong Kong. She is currently an associate professor at Jinan University, Guangzhou. Her research interests mainly focus on supply chain management and operations management. Her publications have appeared in European Journal of Operational Research, International Journal of Production Economics and other leading journals. She is referee for many high quality journals, such as IIE Transactions, European Journal of Operational Research, International Journal of Production Economics, OMEGA: The International Journal of Management Science, IEEE Transaction on Systems, Man, and Cybernetics, Part A, etc.
