---
otero_id: 7380
otero_key: "TDJNCWVU"
title: "Competitive Pricing Strategies for Software and SaaS Products"
authors: "Zan Zhang"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2020.103367"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Competitive Pricing Strategies for Software and SaaS Products

![](/api/attachments/TDJNCWVU/fulltext/images/eae6314018d114dc3e445909a417e4eecbb1a0f6c6c6211e714dc7d681301a78.jpg)

Zan Zhang

School of Economics and Management, Beihang University, Beijing 100191, PR China

## A R T I C L E I N F O

Keywords: pricing competitive strategy customer segments price discrimination game theory

## A B S T R A C T

We study the pricing strategies for a software firm and an entrant software-as-a-service (SaaS) firm in two customer markets: the market composed of the incumbent’s past customers and the market of new customers. We build a game theoretical model to investigate how user costs and the quality differential between products affect firms’ pricing in different customer markets. Our findings show that it is not always optimal for the software firm to price discriminate between its old users and the new customers. The entrant firm would be better off acquiring only the new customers when the SaaS quality is sufficiently low.

## 1. Introduction

It is a common practice in software industry that the same products are charged different prices to specific customers based on whether they purchased the previous version, which is known as upgrade pricing. Many long-established software companies offer an upgrade product at a discounted price to their existing customers of previous version. How ever, some companies have also abandoned upgrade pricing and sell a product at the same price to all customers instead. For example, with Office 2010, Microsoft no longer offered discount to customers who have a validated copy of Office 2007 or Office 2003 and intend to buy Office 2010. This implies that upgrade pricing is not a one-size-fit-all strategy for software firms.

In particular, when facing the encroachment of a SaaS (software-asa-service) product that would compete with the incumbent’s new version of software, the incumbent should decide whether to adopt upgrade pricing. On one hand, for the customers who own an old version of the incumbent’s software, purchasing the new version not only re quires an additional direct payment, but also may entail large hidden costs of software upgrade including costs of consultation, debugging, and data migration. This is especially true for organizations that upgrade the enterprise software such as ERP (Enterprise Resource Planning) or CRM (Customer Relationship Management) software. The average cost of ERP software upgrade is estimated to range from a few thousand to hundreds of thousands of dollars, depending on the size and the type of business.<sup>1</sup>

On the other hand, the entry of the SaaS product is a threat to the incumbent’s software in both the new customer market and the in cumbent’s old user market. One of the key drivers that contribute to the surge in the SaaS solution is its low costs [1]. The SaaS applications are hosted and managed by the provider, and therefore have fewer imple mentation costs. A typical SaaS deployment does not require any hard ware and can run over the existing Internet access infrastructure. By contrast, the traditional software applications are hosted by customers and, in general, require greater efforts and resources to deploy and manage, which typically include hardware deployment, servers, backup, and people services. According to Gartner, customers that purchase software applications can spend up to four times the initial licensing fee to deploy and manage their software.<sup>2</sup>

Although a rich stream of research provides insights into the upgrade pricing from different perspectives, the majority of literature has focused on the monopolistic firm and quite limited research examines firms’ competitive pricing in different customer segments. In this paper, we study a product market with a traditional software firm that faces the encroachment of a SaaS firm. As a response to entry, the software firm offers a new version of its existing software. To entice the new customers and its previous customers to buy the new version, the incumbent sets prices based on their purchase history. While it is a common practice for the software providers to use the upgrade pricing, it remains unclear whether this strategy always generates higher profit when customers are cost sensitive. We investigate how user costs and the quality differential between products affect firms’ pricing strategies and identify conditions under which the entrant firm should avoid aggressive competition with the incumbent for the incumbent’s previous customers.

The rest of the paper is structured as follows. We review the related literature in Section 2. Section 3 specifies the model setup. Section 4 present the equilibrium analysis in low and high switching cost envi ronments. Section 5 extends the basic model by considering user mar kets with unequal sizes. The conclusions come in Section 6.

## 2. Literature Review

There is a significant body of literature on pricing strategies of in formation goods, such as subscription-based pricing [2], pay-per-use pricing [3], behavior-based pricing [4], and free trial strategy [5]. Mehra et al. [6] integrate a competitive upgrade discount pricing into the competition between firms that offer a software product upgrade. Caillaud and De Nijs [7] analyze an infinite competition model with overlapping generations of customers. Huang et al. [8] examine the promotion and pricing decision of a firm that sells innovative products to strategic customers. Zhang et al. [9] analyze the pay-as-you-go model of the cloud services in the presence of security risk. Chen et al. [10] consider the reservation-based and the utilization-based pricing schemes used by service providers in the cloud industry. We contribute to this stream of literature by investigating how firms compete in price when they have unequal market positions.

Another stream of literature related to our work focuses on software upgrade. Bala and Carr [11] investigate upgrade pricing for a monop olistic firm. Zhang and Seidmann [12] examine the optimal policy to license software in the context of software upgrade: perpetual licensing, subscription licensing or a hybrid approach. Zhu and Zhou [13] focus on the head-to-head competition between nonprofit open-source software and propriety software. Mehra et al. [14] study the product life-cycle management of package software and address the issue of optimal up grade intervals. Ceryan et al. [15] provide an analysis of how offering product upgrades impacts optimal price selection. Guo and Chen [16] demonstrate a positive influence of consumers’ strategic behavior on the demand of the second-generation product. Most of the literature in this stream has analyzed product upgrade in a monopoly setting. Relatively limited work considers the issue of competitive product upgrades especially in the context of user costs. Furthermore, most of the existing studies assume that consumers are heterogeneous in their valuations of product quality. In our model, consumers are more concerned about the cost incurred in deploying the products due to their limited budget. The consumers with high cost sensitivity have low willingness to adopt the products compared with those with low sensitivity.

The third stream of literature compares SaaS solutions and the on premises solutions. August et al. [17] examine a monopoly firm’s ver sioning decisions about whether to offer SaaS alternative in addition to the on-premises version. Ma and Seidmann [18] focus on SaaS pro vider’s ability to offer economies of scale and its inability to fully customized. Li et al. [19] study a software vendor’s decision on three licensing models including on-premises, SaaS and hybrid. Guo and Ma [20] analyze the price competition and show that the software vendor’s pricing strategies depend on the SaaS quality improvement rate and the network effect. Feng et al. [21] examine the optimal entry strategy for SaaS providers. Our work differs in that we consider the behavior of different user generations with respect to product adoption and provide an analysis of how firms price in different customer markets. We further identify conditions under which the incumbent software firm can improve profit by charging the same price to all the customers.

## 3. Model

Consider a market with two firms. Firm i is a software provider, which has a user of mass 1. Firm e is an entrant SaaS provider. We call the consumers who purchased from firm i before firm e enters the old users (OU). When firm e encroaches, the consumer market grows and new customers (NU) with mass 1 enter the market. Hence, there are two types of consumers—OU and NU—in the market with the entry of firm e.

Firm i’s initial software provides a maximum utility v to its old users. Following with firm e’s entry, firm i releases a new version of the soft ware, which provides a maximum utility $\nu + \varDelta$ to consumers. Δ is assumed to be large enough so that there exist old users who will up grade. Firm e’s SaaS application provides a maximum utility $\nu + \beta \Delta .$ . The value of $( \beta - 1 )$ measures the quality differential between firm e’s SaaS application and firm i’s upgrade. Firm e has a quality advantage over firm i i $\vdots \beta > 1$ and a quality disadvantage $\mathrm { i f } \ \beta < 1$ . Firm e charges a price $p _ { e }$ to consumers. Firm i offers an upgrade price $p _ { u }$ to its old users and a market price p to the new customers.

Consumes are heterogeneous in their cost sensitivity, which is assumed to be uniformly distributed over [0, 1]. The consumers who buy firm i’s software have to install the product in-house and maintain it using their IT recourses. Let c denote the cost incurred in deploying firm i’s new version of product. A consumer with cost sensitivity θ gets a disutility θc from implementing this new version. A higher value of θ means a more cost sensitive customer. Firm i’s old users face a potential upgrade cost αc if they upgrade to the new version, which may be caused by the need to upgrade the hardware configuration and reinstall the compatible software. Without loss of generality, we normalize the implementation cost c to 1. The old users face a switching cost s if they move to firm e’s SaaS product. The switching cost captures the efforts required to move data from the in-house server to the SaaS provider’s servers. For firm i’s old users with sensitivity, upgrading to the new version of software yields a disutility of θa, and switching to firm e’s SaaS application yields a disutility of θs. The consumers who buy from firm e may also experience a disutility t since there are few options for customization and the users must generally accept the SaaS product as provided due to its multi-tenancy nature. Table 1 summarizes the no tations used in our model.

## 3.1. Consumer Options

Both the old users and the new customers have to decide which product to buy following the encroachment of firm e. We assume com plete information to consumers so that they know firms’ prices and product quality. The consumers’ options and the corresponding payoff are listed as follows.

The consumers in the QU market can choose to upgrade to the new version (upgrade), switch to firm e (switch), or keep using the old version (keep). The strategy space of old users is denoted by $S _ { o } = (  { \mathrm { O U } } \{ u p g r a d e _ {  { \mathrm { : } } }$ switch, keep}). The old users get a surplus of $U _ { u } = \nu + \Delta - p _ { u } - \theta c$ α from upgrading to firm i’s new version, and a surplus of $U _ { s } = \nu + \beta \Delta - t -$ p − θs from switching to firm e’s SaaS product. The users who keep using the old product derive a reservation utility of $U _ { k } = \nu .$

The consumers in the NU market also have three options: buy firm i’s new version (new), buy firm e’s SaaS product (SaaS), or buy nothing (inactive). The strategy space of new customers is denoted by $S _ { n } = \left( \mathrm { N U } \right\{$ new, SaaS, inactive}). The customers get a surplus of $U _ { i } = \nu + \Delta - p _ { i } - \theta$ from buying firm i’s new version and a surplus of $U _ { e } = \nu + \beta \Delta - p _ { e } - t$

## Table 1

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
v The reservation utility from using firm i's old version of software
 $\Delta$  The quality differential between firm i's upgrade and its old version.
 $\beta$  The quality of firm e's SaaS application relative to that of firm i's upgrade
 $\alpha$  Upgrade cost
s Switching cost
 $\theta$  Consumers' cost sensitivity
t Disutility from using the SaaS application
 $p_{u}$  Upgrade price of firm i's new version
 $p_{i}$  Market price of firm i's new version
 $p_{e}$  Price of firm e's SaaS product
</div>

from buying firm e’s SaaS. The utility of the outside option is normalized to zero. The strategy space of both OU and NU is denoted by $s =$ (OU{upgrade, switch, keep}, NU{new, SaaS, inactive} ).

## 3.2. Market Segmentation Analysis

In the OU market, the consumers with lower cost sensitivity choose to upgrade to the new version or switch to firm e, while those with higher cost sensitivity keep using the old version. The following three relations characterize consumer’ s optimal purchasing strategy:

$$
U _ {s} > U _ {u} \Leftrightarrow \theta > \frac {p _ {e} + t - p _ {u} - \Delta (\beta - 1)}{\alpha - s} i f s <   a a n d \theta
$$

$$
<   \frac {p _ {e} + t - p _ {u} - \Delta (\beta - 1)}{\alpha - s} o t h e r w i s e,\tag{1}
$$

$$
U _ {s} > U _ {k} \Leftrightarrow \theta <   \frac {\Delta - t - p _ {e}}{s},\tag{2}
$$

$$
U _ {u} > U _ {k} \Leftrightarrow \theta <   \frac {\Delta - p _ {u}}{\alpha}.\tag{3}
$$

Switching to firm e arises if and only $\begin{array} { r } { \mathrm { i f } \frac { p _ { e } + t - p _ { u } - \Delta ( \beta - 1 ) } { \alpha - s } < \theta < \frac { \Delta - t - p _ { e } } { s } } \end{array}$ when s < a or $\theta < \frac { p _ { e } + t - p _ { u } - \Delta ( \beta - 1 ) } { \alpha - s }$ when $s > a .$ . When the upgrade cost is higher than the switching cost, the consumers with very low cost sensitivity adopt the strategy upgrade. In this scenario, the marginal consumer who is indifferent between the upgrade strategy and the switch strategy is given by $\begin{array} { r } { \theta _ { 1 } ^ { L o } = \frac { p _ { e } + t - p _ { u } - \Delta ( \beta - 1 ) } { \alpha - s } } \end{array}$ , and the marginal consumer who is indif ferent between the switch strategy and the keep strategy is given by $\theta _ { 2 } ^ { L o } = $ $\frac { \Delta - t - p _ { e } } { s }$ . Therefore, firm i gains a demand of $\mathbf { \partial } \theta _ { 1 } ^ { L o }$ from OU market, and firm e gains a demand of $\left( \theta _ { 2 } ^ { L o } - \theta _ { 1 } ^ { L o } \right)$ . When the switching cost is higher than the upgrade cost, the consumers with very low cost sensitivity adopt the switch strategy. In this case, the marginal consumer who is indifferent between the switch strategy and the upgrade strategy is $\theta _ { 1 } ^ { H o } = { }$ $\frac { p _ { u } - p _ { e } - t + \Delta ( \beta - 1 ) } { s - \alpha } _ { 3 }$ , and the marginal consumer who is indifferent between the upgrade strategy and the keep strategy is $\begin{array} { r } { \theta _ { 2 } ^ { H o } = \frac { \Delta - p _ { u } } { \alpha } } \end{array}$ . Firm i gains a de mand of $\left( \theta _ { 2 } ^ { H o } - \theta _ { 1 } ^ { H o } \right)$ from the OU market, and firm e gains a demand of $\theta _ { 1 } ^ { H o }$

On the other hand, in the NU market, the consumers with low cost sensitivity buy from firm i, while those with high cost sensitivity buy from firm e or nothing. It can be easily shown that the strategy inactive is dominated by the strategy SaaS if $\beta \Delta > p _ { e } + t - \nu .$ The marginal con sumer who is indifferent between buying the products is $\theta ^ { n } = p _ { e } +$ $t - p _ { i } - \Delta ( \beta - 1 )$ . Firm i gains a demand of θ<sup>n</sup> from NU market and firm e gains a demand of $( 1 - \theta ^ { n } )$

## 4. Equilibrium Analysis

## 4.1. Competition under Low Switching Cost $( s < \alpha )$

We first analyze the competition when the switching cost is relatively low. There are two possible segmentations in OU market. In the first case, $\theta _ { 1 } ^ { L o } < \theta _ { 2 } ^ { L o }$ ; in other word, some old users find it profitable to switch to firm e, as illustrated in Fig. 1(a). In this case, the old users whose cost sensitivity is lower than $\theta _ { 1 } ^ { L o }$ choose the strategy upgrade, the users whose cost sensitivity is higher than $\theta _ { 2 } ^ { o }$ choose the strategy keep, while those in between adopt the strategy switch. Since $\begin{array} { r } { \frac { \partial \left( \theta _ { 2 } ^ { L o } - \theta _ { 1 } ^ { L o } \right) } { \partial \beta } = \frac { \varDelta } { \alpha - s } > 0 } \end{array}$ , the condi tion $\begin{array} { r } { \beta > \frac { s ( \Delta - p _ { u } ) + \alpha ( t + p _ { e } ) } { \Delta \alpha } } \end{array}$ is required to ensure $\theta _ { 1 } ^ { L o } < \theta _ { 2 } ^ { L o }$ so that the switching customers exist. The intuition is that if the quality of firm $e \mathrm { { } } s$ SaaS application is sufficiently low, no consumer has an incentive to switch to firm e from firm i’s old product, even if the cost in switching is very low. Thus, in the OU market firm i gains an upgrade demand $\theta _ { 1 } ^ { L o }$ , and firm e gains a demand θ<sup>Lo</sup><sub>2</sub> $\theta _ { 1 } ^ { L o }$

(a)  
![](/api/attachments/TDJNCWVU/fulltext/images/b7b43c9af42974404986f8fd08e88ff98de722a71de7eeef0474c2e7fe5c4600.jpg)  
Fig. 1. Segmentation in OU market when $s < \alpha .$

On the other hand, if $\begin{array} { r } { \beta < \frac { s ( \Delta - p _ { u } ) + \alpha ( t + p _ { e } ) } { \Delta \alpha } } \end{array}$ , we have $\theta _ { 1 } ^ { L o } > \theta _ { 2 } ^ { L o }$ . This implies that some users who would otherwise switch to firm e if the SaaS application has a high quality now derive higher surplus from upgrad ing, and some users who would otherwise stick to the old product also prefer to upgrade to the high version, resulting in a market structure consisting of no switching customers. Fig. 1(b) depicts the correspond ing segmentation in the OU market where only two consumer segments (upgrade, keep) exist. In this case, the marginal user, who derives the same surplus from the strategy upgrade and the strategy keep, is denoted by $\theta ^ { L O }$ and $\begin{array} { r } { \theta ^ { L O } = \frac { \Delta - p _ { u } } { \alpha } } \end{array}$ . The users with $\theta < \theta ^ { L O }$ choose the strategy up grade, while those with $\mid > \theta ^ { L O }$ choose the strategy keep. Therefore, firm i obtains a demand of $\theta ^ { L O }$ , and firm e obtains no demand in OU market.

## 4.1.1. Firms’ Profit Maximization

Each firm selects price to maximize the overall profit in the OU and NU markets. We find that the equilibrium outcomes depends largely on the quality differential between the SaaS and software applications. When the value of β is large, firm e’s SaaS application acquires some old users. When the value of β is low, the old users have no incentive to move to firm e, and they choose to upgrade to the new version or keep using the initial one. In the former case, the firms competes directly with each other in the OU and NU markets, while in the latter, the firms compete only in the NU market. Specifically, when $\begin{array} { r } { \beta > \frac { s ( \Delta - p _ { u } ) + \alpha ( t + p _ { e } ) } { \Delta \alpha } } \end{array}$ <sup>)</sup>, both firms serve customers in OU and NU markets, as shown in Fig. 1(a). In this case. firm i determines $p _ { u }$ and $p _ { i }$ to maximize its overall profit $\pi _ { i } =$ $p _ { u } \theta _ { 1 } ^ { L o } + p _ { i } \theta ^ { n }$ , and firm e determines p to maximize its overall profit $\pi _ { e } ~ =$ p $\cdot \left( \theta _ { 2 } ^ { L o } - \theta _ { 1 } ^ { L o } \right) + p _ { e } ( 1 - \theta ^ { n } )$ , where $\begin{array} { r } { \theta _ { 1 } ^ { L o } = \frac { p _ { e } + t - p _ { u } - \varDelta \left( \beta - 1 \right) } { \alpha - s } , \theta _ { 2 } ^ { L o } = \frac { \Delta - t - p _ { e } } { s } } \end{array}$ , and $\theta ^ { n } = p _ { e } + t - p _ { i } - \Delta ( \beta - 1 )$ . Maximizing the two firms’ profits simulta neously yields the equilibrium prices. The closed form expressions for prices and profits under the condition $\beta _ { 1 } ^ { L } < \beta < \beta _ { 2 } ^ { L }$ , which is required to preserve the market structure in this equilibrium, where $\beta _ { 1 } ^ { L D } =$ $\frac { ( a - s ) ( 2 a t + s ( t + 1 ) ( 2 a - s ) + \Delta s ( 2 s - a ) { \it \Psi } ) + a s ( \Delta + t ) } { \Delta ( 2 \alpha - s ) ( \alpha s + a - s ^ { 2 } { \it \Psi } ) }$ and $\begin{array} { r } { \beta _ { 2 } ^ { L D } = \frac { s ( a - s ) ( 3 + 3 s - ( \Delta - 2 t ) ) - s ( \Delta - 3 a ) + 2 a t } { 2 \Delta ( \alpha s + a - s ^ { 2 } ) } , } \end{array}$ are given by

$$
p _ {u} ^ {*} = p _ {i} ^ {*} = \frac {a (t + \Delta (1 - \beta)) + (a - s) (\Delta + s (\Delta - \beta \Delta + t + 1))}{4 \alpha + 3 s (\alpha - s) - s},\tag{4}
$$

$$
p _ {e} ^ {*} = \frac {(a - s) (\beta \Delta (s + 1) - s (\Delta + t - 2)) - s (\Delta - t) + a (\beta \Delta - 2 t)}{4 \alpha + 3 s (\alpha - s) - s},
$$

$$
\pi_ {i} ^ {*} = \frac {a - s + 1}{a - s} (p _ {i} ^ {*}) ^ {2},\tag{5}
$$

$$
\pi_ {e} ^ {*} = \frac {a s - s ^ {2} + a}{s (a - s)} \left(p _ {e} ^ {*}\right) ^ {2}.
$$

The equilibrium outcome shows that the upgrade price that firm i charges to the old users is equal to the price charged to the customers in the NU market. In other words, firm i will not price discriminate be tween the customers who upgrade and those who buy its product for the first time.

When $\beta > \beta _ { 2 } ^ { L }$ , there exists a corner solution where all of the cus tomers who would otherwise keep using the initial version of software now switch to the SaaS application. The equilibrium prices and profits are given in the following.

$$
p _ {u} ^ {*} = p _ {i} ^ {*} = \frac {2 (a - s) + (1 + a - s) (\Delta (1 - \beta) + t)}{3 (1 + a - s)},\tag{6}
$$

$$
p _ {e} ^ {*} = \frac {4 (a - s) + (1 + a - s) (\Delta (\beta - 1) - t)}{3 (1 + a - s)},\tag{7}
$$

$$
\pi_ {i} ^ {*} = \frac {(2 (a - s) + (1 + a - s) (\Delta (1 - \beta) + t)) ^ {2}}{9 (1 + a - s) ^ {2} (a - s)},
$$

$$
\pi_ {e} ^ {*} = \frac {(4 (a - s) + (1 + a - s) (\Delta (\beta - 1) - t)) ^ {2}}{9 (1 + a - s) ^ {2} (a - s)}.
$$

Now consider the case in which the quality of SaaS application is sufficiently low $( \beta < \beta _ { 1 } ^ { L } )$ that none of the old users switch to firm $e ,$ as illustrated in Fig. 1(b). In this case, firm i serves both the OU and NU markets, and firm e serves only the NU market. The firms’ profits are given by $\pi _ { i } = p _ { u } \theta ^ { L o } + p _ { i } \theta ^ { n }$ , and $\pi _ { e } = p _ { e } ( 1 - \theta ^ { n } ) _ { \it : }$ , where $\begin{array} { r } { \theta ^ { L o } = \frac { \Delta - p _ { u } } { \alpha } } \end{array}$ and $\theta ^ { n } =$ $p _ { e } + t - p _ { i } - \Delta ( \beta - 1 )$ . Solving for $p _ { u } , p _ { i } ,$ , and $p _ { e }$ simultaneously yields the equilibrium outcomes. Consequently, we have

$$
p _ {u} ^ {*} = \frac {1}{2} \Delta ,\tag{8}
$$

$$
p _ {i} ^ {*} = \frac {1}{3} (1 + t + \Delta (1 - \beta)),\tag{9}
$$

$$
p _ {e} ^ {*} = \frac {1}{3} (2 - t + \Delta (\beta - 1)),\tag{10}
$$

$$
\pi_ {i} ^ {*} = \frac {1}{3 6 a} \left(9 \Delta^ {2} + 4 a (1 + t + \Delta (1 - \beta)) ^ {2}\right),
$$

$$
\pi_ {e} ^ {*} = \frac {1}{9} (2 - t + \Delta (\beta - 1)) ^ {2}.
$$

We can see that when firm i has a dominant position in its OU market, the optimal pricing strategy for firm i is to price discriminate between old users and new users, which contrasts with that in the equilibrium when the firms compete in both the OU and NU markets.

Proposition 1.. Under low switching cost $( s < a )$ , the equilibrium out comes have the following properties:

(1)For low quality of firm e’s SaaS application, none of the old users switch to firm $e ,$ and firm i price discriminates between the old and new users. The equilibrium prices are given in Eqs. (8)-(10).

(a)  
![](/api/attachments/TDJNCWVU/fulltext/images/cb80802db0f3251c83420e153f277b8135dc78b1f139fa701eeda5027310c739.jpg)  
Fig. 2. Impact of switching cost in the scenario where $s < \alpha .$

(2)For medium quality of firm $e ' s$ SaaS application, firm i charges the same price to all customers and firm e gains customers in OU and NU mar kets. The equilibrium prices are given in Eqs. (4) and (5).

(3)For high quality of firm e’s SaaS application, none of the old users will keep using the initial version of software. Firm i charges the same price to all customers and firm e gains customers in both markets. The equilibrium prices are given in Eqs. (6) and (7).

Proposition 1 shows that it is not always optimal for firm i to price discriminate between the customers who purchased from it and the customers who did not. If the quality of firm $e \mathrm { { } s }$ application is suffi ciently low, firm i is better off offering different prices to its old users and the new ones. Otherwise, it is better for firm i to set a single price to all the customers. Because a higher switching cost or a lower product quality makes firm $e \mathrm { { s } }$ SaaS application less attractive to firm i’s old users, firm e’s pricing and customer acquisition strategies depend largely on the values of s and β. Specifically, firm $e \mathrm { { s } }$ price and profit are in dependent of switching cost if the quality of its SaaS product is low enough. Fig. 2(a) illustrates the variation of firms’ profits with respect to the switching cost in the case when all three consumer segments (up grade, switch, keep) exist in the OU market. From Fig. 2 we can observe that as the switching cost increases, firm e’s profit decreases, and firm i’s profit may increase or decrease. When its new version has a quality advantage over the SaaS product $( \mathrm { i . e . , } \beta < 1 )$ , firm i’s profit increases in the switching cost, as shown in Fig. 2(a). However, when neither product is inherently superior $( \mathrm { i } . { \mathsf { e } } . , \beta = 1 )$ , we can see from Fig. 2(b) that both firms’ profits reduce as the switching cost becomes larger. This implies that the switching cost intensifies the price competition when the maximum utilities that the firms’ products provide are identical.

## 4.1.2. Competition under High Switching Cost $( s > \alpha )$

In this section, we analyze the competition when the switching cost is higher than the upgrade cost. The old users’ preferences for the three strategies—switch, upgrade, keep—are illustrated in Fig. 3, depending on the quality differential of the products. Fig. 3(a) shows a case in which the SaaS application has a significant quality advantage such that some old users prefer to buy from firm e even though they face a high switching cost. Since $\begin{array} { r } { \theta _ { 1 } ^ { H o } = \frac { p _ { u } - p _ { e } - t + \Delta ( \beta - 1 ) } { s - \alpha } } \end{array}$ and $\begin{array} { r } { \frac { \partial \theta _ { 1 } ^ { H o } } { \partial \beta } = \frac { \Delta } { s - \alpha } > 0 . } \end{array}$ , the condi tion $\begin{array} { r } { \beta > \frac { p _ { e } - p _ { u } + t + \Delta } { \Delta } } \end{array}$ should be satisfied to ensure that the switching cus tomers exist. The old users with cost sensitivity $\begin{array} { r } { \theta > \theta _ { 2 } ^ { H o } = \frac { \Delta - p _ { u } } { a } } \end{array}$ choose the strategy keep, and the users with sensitivity $\theta _ { 1 } ^ { H o } < \theta < \theta _ { 2 } ^ { H o }$ choose the strategy upgrade. In this case, firm i gets a demand of $\theta _ { 2 } ^ { H o } - \theta _ { 1 } ^ { H o }$ in the OU market and a demand of $\theta ^ { n }$ in the NU market, and firm e gets a demand of $\theta _ { 1 } ^ { H o }$ in the OU market and a demand $\ o { \mathsf { f } } 1 - \theta ^ { n }$ in the NU market. On the other hand, when the quality of SaaS application is low such that $\beta < \frac { p _ { e } - p _ { u } + t + \Delta } { \Delta }$ , there exist no customers switching from firm i’s old product to firm e. In other words, the strategy switch is dominated by the strategy upgrade for the old users with low cost sensitivity. The old users with cost sensitivity $\begin{array} { r } { \theta < \theta ^ { H O } = \frac { \Delta - p _ { u } } { a } } \end{array}$ upgrade to firm i’s new version, and the other old users get higher surplus from using the old version, as shown in Fig. 3(b). Thus, firm i obtains a total demand of $\left( { \boldsymbol { \theta } } ^ { H O } + { \boldsymbol { \theta } } ^ { n } \right)$ , and firm e only obtains a demand of $( 1 - \theta ^ { n } )$ from the NU market.

(b)  
![](/api/attachments/TDJNCWVU/fulltext/images/6e23a7e158ab1b7f89373c8fc6e22afcbb46122b8da9874b0399a3b7109fd1a3.jpg)  
Note. The parameter values are $a = 0 . 8 , \beta = 0 . 6 , \Delta = 1 ,$ and $t = 0 . 0 1$ for (a), and a = 0.8, β = 1, Δ = 0.8, and t = 0.01 for (b).

![](/api/attachments/TDJNCWVU/fulltext/images/f1ce3a4e189773822f1e7c954ee5bbc280685718fe38b2cffc78169b8d55f003.jpg)  
Fig. 3. Segmentation in OU market when $s > \alpha .$

## 4.1.3. Firms’ Profit Maximization

We first consider the case in which the quality of firm e’s product is sufficiently high such that both firms gains customers in the OU and NU markets. Firm i determines $p _ { u }$ and $p _ { i }$ to maximize its overall profit $\pi _ { i } =$ $p _ { u } \big ( \theta _ { 2 } ^ { H o } - \theta _ { 1 } ^ { H o } \big ) + p _ { i } \theta ^ { n }$ . Firm e sets $p _ { e }$ to maximize its overall profit $\pi _ { e } =$ $p _ { e } \theta _ { 1 } ^ { H o } + p _ { e } ( 1 - \theta ^ { n } )$ , where $\begin{array} { r } { \theta _ { 1 } ^ { H o } = \frac { p _ { u } - p _ { e } - t + \Delta ( \beta - 1 ) } { s - \alpha } , \theta _ { 2 } ^ { H o } = \frac { \Delta - p _ { u } } { a } } \end{array}$ , and $\theta ^ { n } = p _ { e } -$ + $t - p _ { i } - \Delta ( \beta - 1 )$ ). Maximizing the firms’ profit functions with respect to their prices, we obtain the equilibrium prices and profits when $\beta _ { 1 } ^ { H } < \beta < \beta _ { 2 } ^ { H }$ , where $\begin{array} { r } { \beta _ { 1 } ^ { H } = \ \frac { 2 s ( \Delta + t ) + ( s - a ) ( \Delta ( a + s ) + 2 ( 2 s - a ) ( t + 1 ) + 2 t ) } { 2 \Delta ( s - a + 1 ) ( 2 s - a ) } } \end{array}$ , and $\beta _ { 2 } ^ { H } =$ $\frac { ( s - a ) ( 6 a s + 2 a t - \Delta a - 3 \Delta s ) - 4 \Delta s - 4 a ^ { 2 } + 1 0 a s + 2 a t } { 2 \Delta a ( s - a + 1 ) } \cdot$

$$
p _ {u} ^ {*} = \frac {(s - \alpha) (\Delta (3 s + 2 - a (2 \beta + 1)) + 2 a (t + 1)) - 2 \Delta (a \beta - s) + 2 a t}{2 ((3 s + 1) (s - a) + 3 s)},\tag{11}
$$

$$
p _ {i} ^ {*} = \frac {2 s (s - \alpha) (\Delta (1 - \beta) + t + 1) + s \Delta (3 - 2 \beta) + 2 s t - \Delta a}{2 ((3 s + 1) (s - a) + 3 s)},\tag{12}
$$

$$
p _ {e} ^ {*} = \frac {(s - a) ((s + 1) (\Delta \beta - t) + s (2 - \Delta)) + s \Delta (\beta - 1) - s t}{(3 s + 1) (s - a) + 3 s},\tag{13}
$$

$$
\pi_ {i} ^ {*} = \frac {s}{a (s - a)} \left(p _ {u} ^ {*}\right) ^ {2} + \left(p _ {i} ^ {*}\right) ^ {2},
$$

$$
\pi_ {e} ^ {*} = \frac {s - a + 1}{(s - a)} (p _ {e} ^ {*}) ^ {2}.
$$

Now consider the case when none of the customers are willing to switch to firm e due to the low quality of its SaaS application $( \beta < \beta _ { 1 } ^ { H } )$ Firm e sets $p _ { e }$ to maximize its profit obtained in the NU market. The firms’ profit functions are given by $\pi _ { i } = p _ { u } \theta ^ { H o } + p _ { i } \theta ^ { n }$ , and $\pi _ { e } =$ $p _ { e } ( 1 - \theta ^ { n } )$ , where $\begin{array} { r } { \theta ^ { H o } = \frac { \Delta - p _ { u } } { \alpha } } \end{array}$ and $\theta ^ { n } = p _ { e } + \ t - p _ { i } - \Delta ( \beta - 1 )$ . Solving simultaneously for $p _ { u } , p _ { i } ,$ , and $p _ { e }$ yields the equilibrium outcomes as follows:

$$
p _ {u} ^ {*} = \frac {1}{2} \Delta ,\tag{14}
$$

$$
p _ {i} ^ {*} = \frac {1}{3} (1 + t + \Delta (1 - \beta)),\tag{15}
$$

$$
p _ {e} ^ {*} = \frac {1}{3} (2 - t + \Delta (\beta - 1)),\tag{16}
$$

$$
\begin{array}{l} \pi_ {i} ^ {*} = \frac {1}{3 6 a} \big (9 \Delta^ {2} + 4 a (1 + t + \Delta (1 - \beta)) ^ {2} \big), \\ \pi_ {e} ^ {*} = \frac {1}{9} (2 - t + \Delta (\beta - 1)) ^ {2}. \end{array}
$$

We can see that when no switching occurs in the market, the closed form expressions for the equilibrium outcomes under high switching cost are the same as that under low switching cost.

Proposition 2.. When the market is characterized by high switching cost $( s > a ) ,$ , in equilibrium, the incumbent software firm sets different prices for the new customers and its old users.

Contrast with firm i’s pricing strategy under low switching cost, Proposition 2 shows that firm i should practice price discrimination between customers under high switching cost, no matter whether its upgrade is inherently superior to its competitor’s product. This could be explained by the significant effect of lock-in caused by the high switching cost to firm i’s old users. The equilibrium outcomes are summarized in Proposition 3, which also shows that firm e could attract some of firm i’s old customers even if they incur a relatively high cost from switching.

Proposition 3.. Under high switching cost $( s > a ) _ { i }$ , the equilibrium outcome has the following properties:

(1) For high quality of firm e’s SaaS application, firm i’s old users with low cost sensitivity will switch to firm e. The equilibrium prices are given in Eqs.(11)-(13).

(2) For low quality of firm e’s SaaS application, none of the old users will switch to firm e. The equilibrium prices are given in Eqs. (14)-(16).

We use a numerical example to illustrate the variations of profit with respect to the switching cost when all three consumer segments (switch, upgrade, keep) exist in high switching cost environments. The numerical results are shown in Fig. 4. We can see that the firms’ profits increase with the switching cost, which implies that the switching cost mitigates the price competition between the products. This pattern re mains unchanged with various parameter values we tried. This result seems counterintuitive because the traditional wisdom tells us that an increase in the switching cost hurts the new firm’s profit. When con sumers have different sensitivities to the costs, an increased switching cost discourages more old users from moving to firm e. Since the firms derive profits from two customer segments, the increase in firm e’s profit from the NU market more than offsets its loss in the OU market due to the increased switching cost, consequently resulting in a higher profit for firm e.

![](/api/attachments/TDJNCWVU/fulltext/images/23edf7eb6418b6f3a5f25961c17be80feafd1ae52702200ceaa2b166651f7b0d.jpg)  
Fig. 4. Impact of switching cost in the scenario where s > α. Note. The parameter values are $a = 0 . 5 , \beta = 1 . 2 , \Delta = 0 . 8 ,$ and $t = 0 . 0 1$

## 5. Competition when the Sizes of OU and NU markets are Unequal

In the basic model, the market size of the new customers is assumed to be equal to that of firm i’s old users. In this section, the size of the new users is denoted by N and the size of the old users is normalized to 1. We investigate how the difference in the sizes of OU and NU markets affects firms’ pricing decisions. As in the basic model, there are two scenarios to consider in this extension. The market segmentation and the indifferent points could be obtained in the same way as in Section 4. So in what follows, we rule out the detailed derivatives and only present the outcomes.

Case L1: Under low switching cost $( s < a )$ , when all three consumer segments (upgrade, switch, keep) in the OU market exist, the firms’ profit functions are given by $\pi _ { i } = p _ { u } \theta _ { 1 } ^ { L o } + N p _ { i } \theta ^ { n }$ and $\pi _ { e } = p _ { e } \big ( \theta _ { 2 } ^ { L o } - \theta _ { 1 } ^ { L o } \big ) +$ $N p _ { e } ( 1 - \theta ^ { n } )$ . Solving simultaneously for $p _ { u } , p _ { i } ,$ , and $p _ { e } { \mathrm { : } }$ , we get the equi librium prices and profits:

$$
p _ {u} ^ {*} = p _ {i} ^ {*} = \frac {(\Delta + N s (t + 1)) (a - s) + a t + \Delta (1 - \beta) (N a s - N s ^ {2} + a)}{3 N s (a - s) + 4 a - s},\tag{17}
$$

$$
p _ {e} ^ {*} = \frac {(2 \Delta + N s (2 - t)) (a - s) - t (2 a - s) + \Delta (\beta - 1) (N a s - N s ^ {2} + 2 a - s)}{3 N s (a - s) + 4 a - s},\tag{18}
$$

$$
\pi_ {i} ^ {*} = \frac {N (a - s) + 1}{a - s} \bigl (p _ {i} ^ {*} \bigr) ^ {2},
$$

$$
\pi_ {e} ^ {*} = \frac {N s (a - s) + a}{s (a - s)} \left(p _ {e} ^ {*}\right) ^ {2}.
$$

Case L2: When none of the old users switch to firm e and thus two consumer segments (upgrade, keep) exist in the OU market, the firms profit functions are $\pi _ { i } = p _ { u } \theta ^ { L o } + N p _ { i } \theta ^ { n }$ and $\pi _ { e } = N p _ { e } ( 1 - \theta ^ { n } )$ . Maximizing the profits yields the equilibrium outcomes as follows:

$$
p _ {u} ^ {*} = \frac {1}{2} \Delta ,\tag{19}
$$

$$
p _ {i} ^ {*} = \frac {1}{3} (1 + t + \Delta (1 - \beta)),\tag{20}
$$

$$
p _ {e} ^ {*} = \frac {1}{3} (2 - t + \Delta (\beta - 1)),\tag{21}
$$

$$
\pi_ {i} ^ {*} = \frac {1}{3 6 a} (4 N a (1 + t + \Delta (1 - \beta)) ^ {2} + 9 \Delta^ {2}),
$$

$$
\pi_ {e} ^ {*} = \frac {1}{9} N (2 - t + \Delta (\beta - 1)) ^ {2}.
$$

Next consider the competition under high switching cost $( s > a )$ . Case H1: When all the consumer segments (switch, upgrade, keep) exist, the firms’ profit functions are $\pi _ { i } = p _ { u } \big ( \theta _ { 2 } ^ { H o } - \theta _ { 1 } ^ { H o } \big ) + N p _ { i } \theta ^ { n }$ and $\pi _ { e } =$ $p _ { e } \theta _ { 1 } ^ { H o } + N p _ { e } ( 1 - \theta ^ { n } )$ . Solving for $p _ { u } , p _ { i } ,$ , and $p _ { e } ,$ we have

$$
p _ {u} ^ {*} = \frac {(s - a) (3 \Delta N (s - a) + 2 a N (t + 1) + 4 \Delta) + 2 a t + \Delta s (1 - \beta) (N a - N s - 1)}{6 N s (s - a) - 2 a + 8 s},\tag{22}
$$

$$
p _ {i} ^ {*} = \frac {(\Delta + 2 N s (t + 1)) (s - a) + 2 s t + \Delta s (1 - \beta) (N a - N s - 1)}{3 N s (s - a) - a + 4 s},\tag{23}
$$

$$
p _ {e} ^ {*} = \frac {(\Delta + N s (2 - t)) (s - a) - t (2 s - a) + \Delta (\beta - 1) ((s - a) (N s + 1) + s)}{3 N s (s - a) - a + 4 s},\tag{24}
$$

$$
\pi_ {i} ^ {*} = \frac {s}{a (s - a)} \left(p _ {u} ^ {*}\right) ^ {2} + N \left(p _ {i} ^ {*}\right) ^ {2},
$$

$$
\pi_ {e} ^ {*} = \frac {1 + N (s - a)}{s - a} \left(p _ {e} ^ {*}\right) ^ {2}.
$$

Case H2: When the switching cost is sufficiently high such that even the customers with very low cost sensitivity have no incentive to switch to the SaaS application, firm e captures consumers only from the NU market. In this case, the equilibrium prices are the same as that given in Eqs. (19)–(21). From the above equilibrium market outcomes, we can summarize the firm i’s pricing strategies under different conditions, as shown in Proposition 4.

Proposition 4. . Under high switching cost, firm i charges different prices to its old users and the new customers in equilibrium. Under low switching cost, firm i charges the same price to all customers when its old users have an incentive to switch.

When the switching cost is high, firm i will price discriminate be tween customers in the OU and NU markets, and when the switching cost is low, firm i is incentivized to set the same price for all the cus tomers under certain conditions. This finding is similar to the that derived from the basic model. Figs. 5 and 6 illustrate the impact of N on firms’ profits under low and high switching costs. We can see that the firms’ profits increase in N. Comparing firm e’s profits in Cases L1 and $L 2 ,$ we observe from Fig. 5 that, firm e’s profit in Case L2 is higher than that in Case L1 when N is small and lower than that in Case L1 when N is large; firm i’s profit in Case L2 is higher than the profit it gains in Case L1. Fig. 6 shows a similar result that under high switching cost, firm e gains a higher profit in Case H2 when N is small and in Case H1 when N is large. This implies that when the sizes of old users and new users are not equal, firm e would be better off acquiring only the new customers if the size of NU market is sufficiently large; however, if the size of the NU market is small relative to that of the OU market, it is better for firm e to acquire customers from the two customer markets. This result is in accordance with the practical observation that NetSuite takes great efforts to induce the customers of Microsoft to switch to its SaaS-based solutions.

$$
\begin{array}{c} \text {- firm i (Case L1) - firm e (Case L1)} \\ \text {- firm i (Case L2) - firm e (Case L2)} \end{array}
$$

![](/api/attachments/TDJNCWVU/fulltext/images/4af606d10acae00bb407fb6e27780f917c9e97e529c85b82fd417599477d10d2.jpg)  
Fig. 5. Impact of N on profits under low switching cost. Note. The parameter values are $a = 0 . 8 , \beta = 1 , \Delta = 0 . 6 , s = 0 . 5 ,$ and $t = 0 . 0 1$

![](/api/attachments/TDJNCWVU/fulltext/images/c7aca754cb33a2832f3c753d4f374ff21aa3360eac171b0fd75023a6a81444b5.jpg)  
Fig. 6. Impact of N on profits under high switching cost.  
Note. The parameter values are a = 0.5, β = 1, Δ = 0.6, s = 0.8, and t = 0.01.

## 6. Conclusions

In this paper, we analyze pricing decisions for firms by taking into account the behavior of different user generations with respect to product adoption. The incumbent provides a new version of its initial software to compete with the SaaS product and charges different prices to different customer segments. Consumers are cost sensitive and base their purchase decisions on firms’ prices, the product quality, and the levels of related costs.

Our main contribution to the existing literature on competitive pricing strategies is threefold. First, we demonstrate how the upgrade cost and switching cost affect consumer purchase behavior leading to the incumbent’s dominant position in the market of its previous cus tomers. Second, we demonstrate that it might be wise for the software firm to compete with the entrant SaaS provider by setting the same price for all the customers, no matter whether they have purchased the in cumbent’s previous version. There exist conditions where charging different prices to different customer segments benefits the incumbent. If the users’ switching cost is higher than their upgrade cost, the soft ware firm should price discriminate between its old users and the new customers; otherwise, the software firm would be better off setting the same price for all customers when the quality of the SaaS product is not very high or very low relative to the quality of the incumbent’s upgrade. Third, we contribute to the existing literature by identifying circum stances wherein the entrant firm should avoid aggressive competition with the incumbent for the incumbent’s old customers and instead attract the customers in the untapped market.

The current analysis has limitations. We consider only one version of product for the traditional software firm to compete with the SaaS application. An interesting situation could be one where the traditional software firm also offers a SaaS version of its software. Clearly, the SaaS product of the traditional software firm and that of a pure SaaS firm must be differentiated in some way to avoid Bertrand competition. Another limitation of our work is that we focus on a static game and do not formally address how the inherited customer relationships are determined. The future work could study firms’ pricing strategies in a dynamic game of incomplete information.

## CRediT authorship contribution statement

Zan Zhang: Conceptualization, Methodology, Software, Visualiza tion, Writing - review & editing.

## Acknowledgement

This work was supported by the National Natural Science Foundation of China (No. 72001012).

## References

[1] M. Rhyman, Five reasons why switching to SaaS will be the best investment you make this year, Forbes (May 15) (2017)

[2] V. Choudhary, Comparison of software quality under perpetual licensing and software as a service, Journal of Management Information Systems 24 (2) (2007) 141–165.

[3] S. Balasubramanian, S. Bhattacharya, V.V. Krishnan, Pricing information goods: A strategic analysis of the selling and pav-per-use mechanisms, Marketing Science 34 (2) (2015) 218–234.

[4] K.J. Li, S. Jain, Behavior-based pricing: An analysis of the impact of peer-induced fairness, Management Science 62 (9) (2016) 2705–2721.

[5] A. Mehra, R.L. Saha, Utilizing public betas and free trials to launch a software product, Production and Operations Management 27 (11) (2018) 2025–2037.

[6] A. Mehra, R. Bala, R. Sankaranarayanan, Competitive behavior-based price discrimination for software upgrades, Information Systems Research 23 (1) (2012) 60–74.

[7] B. Caillaud, R. De Nijs, Strategic loyalty reward in dynamic price discrimination, Marketing Science 33 (5) (2014) 725–742

[8] Y. Huang, B. Gokpinar, C.S. Tang, O.S. Yoo, Selling innovative products in the presence of externalities, Production and Operations Management 27 (7) (2018)

[9] Z. Zhang, G.F. Nan, Y. Tan, Cloud service vs. on-premises software: Competition under security risk and product customization. Information Systems Research (2020). Online: June.

[10] S. Chen, H. Lee, K. Moinzadeh, Pricing schemes in cloud computing: Utilizationbased vs. reservation-based, Production and Operations Management 28 (1) (2019) 82–102.

[11] R. Bala, S. Carr, Pricing software upgrades: The role of product improvement and user costs, Production and Operations Management 18 (5) (2009) 560–580.

[12] J. Zhang, A. Seidmann, Perpetual versus subscription licensing under quality uncertainty and network externality effects, Journal of Management Information Systems 27 (1) (2010) 39–68

[13] K.X. Zhu. Z.Z. Zhou, Research note—Lock-in strategy in software competition Open-source software ys, proprietary software. Information Systems Research 23 (2) (2012) 536–545.

[14] A. Mehra. A. Seidmann. P. Moiumder. Product life-cycle management of packaged software. Production and Operations Management 2 (3) (2014) 366–378

[15] O. Ceryan, I. Duenyas, O. Sahin, Dynamic pricing and replenishment with customer upgrades, Production and Operations Management 27 (4) (2018) 663–679.

[16] Z. Guo, J. Chen, Multigeneration product diffusion in the presence of strategic consumers, Information Systems Research 29 (1) (2018) 206–224.

[17] T. August, M.F. Niculescu, H. Shin, Cloud implications on software network structure and security risks, Information Systems Research 25 (3) (2014) 489–510

[18] D. Ma, A. Seidmann, Analyzing software as a service with per-transaction charges,

[19] S.L. Li, H.K. Cheng, Y. Duan, Y.C. Yang, A study of enterprise software licensing models, Journal of Management Information Systems 34 (1) (2017) 177–205.

[20] Z. Guo, D. Ma, A model of competition between perpetual software and software as a service, Management Information Systems Quarterly 42 (1) (2018) 101–120

[21] H. Feng, Z. Jiang, D. Liu, Quality, pricing, and release time: Optimal market entry strategy for new software-as-a-service Vendors, Management Information Systems Quarterly 42 (1) (2018) 333–353.

Zan Zhang (zanzhang@buaa.edu.cn) is a post doc at the School of Economics and Man agement, Beihang University, China. She received her Ph.D. from the College of Man agement and Economics, Tianjin University. Her research interests include economics of information systems, network economics, and e-commerce, She has published in Infor mation Systems Research, Journal of Management Information Systems, Information Sciences, among others.
