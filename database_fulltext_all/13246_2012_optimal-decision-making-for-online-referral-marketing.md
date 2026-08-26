---
otero_id: 13246
otero_key: "SBVZC7J2"
title: "Optimal decision making for online referral marketing"
authors: "Zhiling Guo"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal decision making for online referral marketing

Zhiling Guo

Department of Information Systems, City University of Hong Kong, Tat Chee Avenue, Kowloon, Hong Kong

## a r t i c l e i n f o

Article history: Received 12 August 2010 Received in revised form 3 September 2011 Accepted 18 September 2011 Available online 28 September 2011

Keywords: Dynamic pricing Word of mouth Referral marketing Optimal control

## a b s t r a c t

Widely available web 2.0 technologies not only bring rich and interactive user experiences, but also easily help users advertise products or services on their own blogs and social network webpages. Online referral marketing, for example, is a business practice that rewards customers who successfully refer other customers to a website or upon completion of a sale usually via their own social contacts. The referral rewards come in different forms such as shopping vouchers, redeemable points, discounts, prizes, cash payments, etc. We develop an analytical model to evaluate the business potential of incorporating an online referral marketing program into the <sup>fi</sup>rm's product selling strategies. Under different demand dynamics, we investigate the optimal decision making including the pricing and referral strategies to maximize the seller's pro<sup>fi</sup>tability. We <sup>fi</sup>nd that, under simple decision making environment such as <sup>fi</sup>xed product price and myopic strategy, different demand dynamics yield the same prediction of the referral payment, which turns out to be a static policy. However, under complex market situations, both the optimal product pricing and referral offering critically depend on the demand side dynamics. Under the nonlinear demand dynamics, the referral payment is an all-or-nothing decision throughout the product selling horizon. In contrast, under the linear demand assumption, the referral payment can be partially offered in initial phase of the product introduction. We further offer some managerial insights to guide practical implementation of the online referral marketing strategy.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Although the rapid development of digital technologies has easily transformed loyal customers to brand advocates, the idea of offering rewards to motivate current customers to refer other customers is not new. PayPal offered <sup>fi</sup>nancial incentive to have members recommend members. The company acquired more than three million users in its <sup>fi</sup>rst nine months of operation. Many telecommunication companies offer discounts and vouchers to customers who help them recruit new subscribers. Credit card companies offer coupons, redeemable points or cash rewards to those customers when a referred friend signs up a service. Today, increasingly more referral reward programs have been designed to motivate consumers or other businesses to refer products or services to potential customers. The most prominent is the af<sup>fi</sup>liate marketing used by Amazon and Google advertising, in which a business rewards their af<sup>fi</sup>liates for each visitor or customer brought about by the af<sup>fi</sup>liate's marketing efforts.

As opposed to traditional marketing strategies that use business-toconsumer communication to disseminate information about a product or service, new marketing practices take advantage of consumerto-consumer connections. RadicalBuy (http://apps.facebook.com radicalbuy/) was an innovative Facebook application that empowers individual users to effortlessly set up their own virtual storefront in Facebook and share their items anywhere on the web. In addition to its fundamental buying and selling functions, it allows users to list and sell friends' items to earn commission. Although RadicalBuy.com and all widget services were discontinued in November 2010, the novel aspect of this business model is the combination of social networking with consumer-to-consumer commerce. Referral in online social networks is effective because it carries immediate credibility, which has much more impact than a direct mail or advertising campaign, especially for a niche business. The enhanced word of mouth (WOM) effect in social networks helps create solid sales opportunities that are unavailable in traditional selling channels. It is among the easiest, most cost-effective ways to gain new business leads.

As the Internet empowers consumers to share ideas and spread of word of mouth, online channels are increasingly recognized as an important vehicle to in<sup>fl</sup>uence the adoption and use of products and services. New online referral strategies leverage consumer-toconsumer interactivity, taking new forms such as blogs, news groups, product reviews, and social networking sites. Available information technologies have also changed the landscape of many marketing activities, expanding the reach of individual sellers to customers. For example, an online seller can easily set up a system that seamlessly integrates referrals into her marketing plan. The seller can offer referrals for other online customers by using Web analytics applications, such as Microsoft FastCounter Pro, to easily track user traf<sup>fi</sup>c. Such software not only automates the referral process, but tells which sites are referring the most lucrative traf<sup>fi</sup>c, so the seller can make the most of af<sup>fi</sup>liate links to cost effectively grow their business.

Since a referral reward is only offered when a referral turns into a sale, a referral strategy is recognized as an effective business marketing strategy because of the “pay for performance” incentive. While the potential of referral to effectively reach out to a broad set of users is attracting considerable attention, the business value of this approach is yet demonstrated. On the one hand, tangible referral rewards can motivate existing consumers to introduce new customers to the business at a low acquisition cost. On the other hand, rewards can sometimes be given to customers who would have recommended the product anyway, leading to a waste of advertising resources. Even if a high referral reward may increase the likelihood of making referrals, the seller has to trade off the bene<sup>fi</sup>t of additional sales and the total cost of referral payment. The fact that formal referral programs are only offered in certain products or markets shows that this strategy may not always be bene<sup>fi</sup>cial. There needs to be a better understanding of the contexts in which online referral program works. This paper aims to bridge this research gap.

In this paper, we develop an analytical framework to help managers make optimal decisions in their online referral marketing practice. Based upon the seminal Bass diffusion model [1], we explicitly consider the use of referral reward to in<sup>fl</sup>uence WOM marketing. The seller's optimal decision has to trade off the gain through the additional sales generated by enhanced WOM marketing and the cost of making referral payment. We <sup>fi</sup>nd that, under simple decision making environment such as <sup>fi</sup>xed product price and myopic strategy, different demand dynamics yield the same prediction of the referral payment, which turns out to be a static policy. However, under complex market situations, both the optimal product pricing and referral payment critically depend on the demand side dynamics. Under the nonlinear demand dynamics, the referral offering is an all-or-nothing decision throughout the product selling horizon. In contrast, under the linear demand assumption, referral reward can be partially offered in initial phase of the product introduction. These <sup>fi</sup>ndings provide important guidelines to implement the online referral marketing strategy.

The rest of the paper is structured as follows. Section 2 presents a brief literature review. In Section 3, we introduce our analytical framework based on widely adopted demand models in the literature. As a benchmark model, we analyze the optimal pricing strategy without referral reward in Section 4. In Section 5, we study the optimal referral strategy under the case of <sup>fi</sup>xed product price. Section 6 investigates the optimal mix of pricing and referral payment schemes. Section 7 further offers more marketing insights based on a numerical study. We summarize our results and provide managerial insights in Section 8.

## 2. Literature review

Traditionally, WOM marketing refers to the passing of information from person to person [24]. The computer mediated environment has signi<sup>fi</sup>cantly expanded the scale and scope of in<sup>fl</sup>uence. One particularly cost-effective way of disseminating the marketing message is called e-referral marketing, in which consumers are willing to become promoters of a product or service and spread the word to their friends. E-referral marketing is a speci<sup>fi</sup>c form of viral marketing (the word “viral” suggests that information spreads automatically [23]). Viral marketing also belongs to one category of online word-of-mouth marketing [13], which is referred to as electronic or e-word-of-mouth (e-WOM) marketing [10]. The e-WOM marketing effort may not only increase brand awareness, but motivate direct purchases.

Since referral is an effective marketing strategy of introducing new customers at a low acquisition cost, companies are increasingly aware of the need to manage customer referral reward programs [3]. Based on data in the insurance industry, Law [16] identi<sup>fi</sup>ed that trust, including credibility and benevolence, is the key element in the process of developing closer relational strength and shared value. Building upon theory of customer satisfaction, Biyalogorsky et al. [2] studied the optimal combination of reward and price that will lead to the most pro<sup>fi</sup>table referrals. They found that the optimal mix of price and referral reward falls into three regions and critically depend on customer delight. When customers are easy to delight, then lowering prices without referral may be optimal. If customer delight threshold is in an intermediate level, a seller should use a reward to complement a low-price strategy. When the delight threshold is very high, the seller should forsake the referral strategy all together. Though interesting, their model is a static model that does not answer such practical questions as how to adjust the optimal mix of price and referral reward as new market conditions emerge.

In a dynamic setting, prior studies have examined the diffusion of innovations and the transmission of ideas in social networks [17]. Due to the reduced communication cost, increased reach of in<sup>fl</sup>uence, and the <sup>fl</sup>exibility to deploy a variety of in<sup>fl</sup>uence strategies through information technologies, online networks become a considerably compelling channel for knowledge-sharing and information transfer. Because information spreads rapidly on the Internet, viral marketing campaigns have the potential to reach large number of customers in a short period of time [5]. Companies are interested in understanding how marketers can in<sup>fl</sup>uence the process through marketing activities. Van der Lans et al. [22] developed a viral branching dynamic model for predicting the spread of electronic word of mouth. The model is applied to a real world campaign and is used to evaluate alternative business scenarios.

Dynamic models for durable new product introduction can be traced back to the original work of the Bass diffusion model [1]. Subsequent works in the diffusion of innovation literature examined optimal dynamic pricing strategies in the presence of WOM [12]. Majority of marketing research in this line focuses on pricing as single decision variable. No insight is offered about how to set product price and referral reward simultaneously to optimize performance. An increasing number of studies in Information Systems (IS) literature focus on dynamic models in the context of open source software diffusion [25], knowledge management adoption and assessment [11], diffusion of innovation within social networks [15], and measuring in<sup>fl</sup>uence in customer networks [14]. We develop a model to investigate how a seller should use a combination of referral reward and product pricing strategy to determine the optimal product introduction and subsequent market development. Our model sheds new light on both marketing and IS literature by considering how referral reward would in<sup>fl</sup>uence online WOM communication and the likelihood of purchase in networked markets. The dynamic nature of our model also suggests changing strategies for more effective customer referral management, which enriches the existing literature that largely rely on static analysis.

## 3. Market dynamics and decision models

In this section, we formulate our analytical model based on two speci<sup>fi</sup>cations of demand dynamics that are widely used in the marketing literature. To establish a performance benchmark, we <sup>fi</sup>rst present a base model and analyze the seller's pricing strategy when solely relying on the traditional WOM communication (call it the base model or the traditional marketing model). We then consider a monopolist seller who can potentially use an online referral marketing campaign to promote a new product through its tangible reward program (call it the referral marketing model). A complete summary of notation is provided in Appendix A.

## 3.1. Assumptions

Assume the population size is N. In our dynamic model, the state of the system at time t is the total number of sales by time t, or the number of customers who have already adopted the product at time t. We denote it as x(t) in the base model and $z ( t )$ in the online referral marketing model.

The sales rate or demand dynamics governs the system evolution over time. De<sup>fi</sup>ne the sales rate at time t as the likelihood of purchase $P ( t )$ multiplied by the demand rate $q ( t )$ , where $q ( t )$ is the quantity demanded by consumers at time t. In the following, we describe the likelihood of purchase and two possible demand dynamics.

## 3.1.1. Likelihood of purchase

Under the traditional WOM marketing, the classical Bass model provides intuitively appealing assumptions to model the likelihood of purchase [1]. According to Bass, the total likelihood of purchase among the population is $P ( t ) = \alpha + \gamma x ( t )$ , where $\alpha { > } 0$ is interpreted as coef<sup>fi</sup>cient of innovation and $\gamma { > } 0$ the coef<sup>fi</sup>cient of imitation. Accordingly, consumers can be classi<sup>fi</sup>ed into two groups. The <sup>fi</sup>rst group of consumers are innovators who make independent purchase decisions with probability α. The second group of consumers are imitators whose purchase decisions are in<sup>fl</sup>uenced by the action of their peer consumers. Therefore, the likelihood of purchase in the second group, γx(t), is proportionally affected by the number of consumers who have already purchased the product. The imitation effect is also known as the WOM effect in the literature. Note that the choice of α and γ should ensure that $\alpha + \gamma N { \leq } 1$ so that the condition $0 < P ( t ) \leq 1$ can be satis<sup>fi</sup>ed.

Under the online referral marketing model, the seller offers a per unit referral payment $m ( t ) { > } 0$ for consumers who have successfully referred other consumers to buy the product. The traditional WOM effect γ is therefore enhanced to $\gamma + \beta m ( t )$ , where parameter β measures how effective the referral payment can motivate WOM marketing. We call it the coef<sup>fi</sup>cient of referral. The additional term βm(t) re<sup>fl</sup>ects the total market responsiveness to the online referral marketing strategy. That is, as the referral effectiveness factor β or the referral payment m(t) increases, the likelihood of purchase by imitators increases. Note that, when $m ( t ) = 0 ,$ , the online referral marketing strategy degenerates to the traditional WOM marketing strategy. Again, we need to ensure that $0 < \alpha + ( \gamma + \beta m ( t ) ) N \le 1$ . Solving this inequality we have $\begin{array} { r } { m ( t ) { \le } \frac { 1 } { \beta } \left( \frac { 1 - \alpha } { N } - \gamma \right) } \end{array}$

## 3.1.2. Linear demand dynamics

Assume that each consumer will only demand one unit of the product. Recall the population size is N. It can be interpreted as the maximum market potential. Since x(t) is the number of customers who have already adopted the product at time t in the traditional marketing model, $N - x ( t )$ is the remaining market potential, i.e., the time-varying remaining market potential that can be captured when price is set to zero.

Linear demand functions have been used in various static analysis [18] and dynamic models [19,8,9]. Let p(t) be the product selling price at time t. Following [9], we adopt the following linear demand function: $q ( t ) = N - x ( t ) - \theta p ( t )$ . Note here that the coef<sup>fi</sup>cient θ measures the price sensitivity to demand.

Denote ${ \dot { \boldsymbol { x } } } ( t ) = { \frac { d { \boldsymbol { x } } ( t ) } { d t } }$ as the instantaneous sales rate at time t under the traditional WOM marketing strategy. The demand dynamics can be expressed as the following differential equation:

$$
\dot {x} (t) = (\alpha + \gamma x (t)) (N - x (t) - \theta p (t)),\tag{1}
$$

Similarly, let z(t) and ${ \dot { z } } ( t ) = { \frac { d z ( t ) } { d t } }$ be the total cumulative sales and the instantaneous sales rate at time t, respectively, under the online referral marketing strategy. z(t) consists of both online referralbased sales and sales naturally occur under traditional WOM communication. Denote $y ( t )$ and ${ \dot { y } } ( t ) = { \frac { d y ( t ) } { d t } }$ as the cumulative sales and instantaneous sales rate at time t through the online referral program, respectively.

Based on consumer utility theory, Chiang and Guo [4] have shown that all WOM sales would be incentive-based sales when consumers do not discount their referral utility. That is, if there is no negative consequence associated with making money through referral, consumers would simply prefer to get paid rather than not being rewarded. This can happen when the business is completely run online such as software that requires special installation or digital music that is distributed through a peer-to-peer system. The seller can easily and reliably track and monitor the WOM communication, so the seller may reward all WOM sales accordingly. The demand dynamics can be expressed as:

$$
\left\{ \begin{array}{l} \dot {y} (t) = (\gamma + \beta m (t)) z (t) (N - z (t) - \theta p (t)) \\ \dot {z} (t) = (\alpha + (\gamma + \beta m (t)) z (t)) (N - z (t) - \theta p (t)) \end{array} \right.\tag{2}
$$

Note that there is an enhancement in the WOM sales brought by the online referral program. The higher the referral offering, the more likely early adopters would actively promote the word-ofmouth sales. So the total sales would increase. When m(t) is zero, the online referral demand dynamics (2) degenerates to the traditional marketing demand dynamics (1).

## 3.1.3. Nonlinear demand dynamics

Nonlinear demand function can be expressed in different forms, such as quadratic and exponential. In the marketing literature, the following demand dynamics has been assumed by [20,7,12], among others.

$$
\dot {x} (t) = e ^ {- s p (t)} (\alpha + \gamma x (t)) (N - x (t)),\tag{3}
$$

where parameter s measures the demand elasticity that is proportional to price. This is the demand dynamics under the traditional WOM marketing strategy.

Similarly, under the online referral marketing strategy, the market demand model is expressed as:

$$
\left\{ \begin{array}{l} \dot {y} (t) = e ^ {- s p (t)} (\gamma + \beta m (t)) z (t) (N - z (t)) \\ \dot {z} (t) = e ^ {- s p (t)} (\alpha + (\gamma + \beta m (t)) z (t)) (N - z (t)) \end{array} \right.\tag{4}
$$

The following table summarizes our model setup under different market scenarios.

## 3.2. Decision models

As shown in Table 1, we consider two decision models. The base model refers to the traditional WOM marketing where no referral reward is offered by the seller. The online referral marketing model refers to the business practice that a <sup>fi</sup>rm offers referral payment to consumers as an effort to enhance WOM marketing.

In the base model, subject to the demand dynamics (1) and (3), the seller's objective is to choose the optimal pricing strategy p(t) to maximize her overall discounted pro<sup>fi</sup>t over a <sup>fi</sup>nite planning horizon T:

$$
\pi_ {B} = \underset {p (t)} {\text { Max }} \int_ {0} ^ {T} e ^ {- \rho t} p (t) \dot {x} (t) d t\tag{5}
$$

Model setup under different demand dynamics and marketing strategies.

<table><tr><td>Demand dynamics</td><td>Linear demand rate</td><td>Nonlinear demand rate</td></tr><tr><td>Base model $\dot{x}(t) = P(t)q(t)$ </td><td> $P(t) = \alpha + \gamma x(t)$  $q(t) = N - x(t) - \theta p(t)$ </td><td> $P(t) = \alpha + \gamma x(t)$  $q(t) = e^{-sp(t)} (N - x(t))$ </td></tr><tr><td>Referral model $\dot{z}(t) = P(t)q(t)$ </td><td> $P(t) = \alpha + (\gamma + \beta m(t))z(t)$  $q(t) = N - z(t) - \theta p(t)$ </td><td> $P(t) = \alpha + (\gamma + \beta m(t))z(t)$  $q(t) = e^{-sp(t)} (N - z(t))$ </td></tr></table>

The seller's objective in the online referral marketing model is to choose an optimal pricing strategy $p ( t )$ and a referral payment $m ( t )$ that collectively maximize her overall discounted pro<sup>fi</sup>t over a <sup>fi</sup>nite planning horizon T, subject to the demand dynamics in Eqs. (2) or (4):

$$
\pi_ {R} = \underset {p (t), m (t)} {\text { Max }} \int_ {0} ^ {T} e ^ {- \rho t} (p (t) \dot {z} (t) - m (t) \dot {y} (t)) d t\tag{6}
$$

where $\rho { \ge } 0$ is the discount rate that is used to calculate the present discounted value of pro<sup>fi</sup>t. If the <sup>fi</sup>rm prefers pro<sup>fi</sup>t to be earned in the current period rather than in future periods, the discount rate $\rho { > } 0 .$ A higher discount rate implies that the <sup>fi</sup>rm prefers more pro<sup>fi</sup>ts to be earned now than later.

Also note that, in the seller's objective function in $\operatorname { E q . } ( 6 ) ,$ , the <sup>fi</sup>rst term is the gross pro<sup>fi</sup>t rate and the second term is the referral payment rate. We do not explicitly model the cost of production. For physical products, we may interpret p(t) as the desired pro<sup>fi</sup>t margin (the unit selling price minus the constant unit production cost) by the seller. For digital products, since almost all production related costs are sunk cost, we assume the marginal production cost is zero.

We employ the optimal control method to analyze the model. In Section 4, we focus on optimal pricing in the base model where no referral payment is offered. In Sections 5 and 6, we analyze the optimal referral scheme under <sup>fi</sup>xed and dynamic pricing strategies, respectively, in the online referral marketing model.

## 4. The base model

In the base model the seller optimizes total discounted pro<sup>fi</sup>t characterized by Eq. (5). We compare two pricing strategies: myopic and forward-looking. At any time, a myopic pricing strategy maximizes the instantaneous pro<sup>fi</sup>t without considering the impact of current strategy on the pro<sup>fi</sup>t in future periods. In contrast, a forward-looking pricing strategy takes into account the effect of current period sales on future demand growth and market pro<sup>fi</sup>tability. Generally speaking, the forward-looking strategy outperforms the myopic strategy because it considers the inter-temporal strategic tradeoff. We use the myopic pricing as a benchmark to compare with the forward-looking pricing strategy. The performance difference can be seen as the bene<sup>fi</sup>t of strategic planning and system thinking in a dynamic environment rather than a static analysis at any decision point.

## 4.1. Myopic pricing

Following the new product introduction literature, we assume there is no demand at the beginning of the planning horizon $( \mathrm { i } . \mathsf { e } . , x ( 0 ) = 0 )$ The following table compares the pricing and sales patterns under the two demand assumptions. Calculation of these results is presented in Appendix B.

We see that the myopic pricing strategy is different under different demand dynamics, formally stated in the following Proposition.

Pricing and sales patterns under myopic strategy.

<table><tr><td>Characteristics</td><td>Linear demand</td><td>Nonlinear demand</td></tr><tr><td>Optimal price at  $t$ </td><td> $p_{l}^{m}(t)=\frac{N}{2\theta}-\frac{1-e^{-\frac{(\alpha+\gamma N)t}{2}}}{2\theta\left(\frac{1}{N}+\frac{\gamma}{\alpha}e^{-\frac{(\alpha+\gamma N)t}{2}}\right)}$ </td><td> $P_{n}^{m}(t)=\frac{1}{s}$ </td></tr><tr><td>Cumulative sales at  $t$ </td><td> $x_{l}^{m}(t)=\frac{1-e^{-\frac{(\alpha+\gamma N)t}{2}}}{\frac{1}{N}+\frac{\gamma e^{-\frac{(\alpha+\gamma N)t}{2}}}{2}}$ </td><td> $x_{n}^{m}(t)=\frac{1-e^{-\frac{\alpha+\gamma N}{e}}}{\frac{1}{N}+\frac{\gamma e^{-\frac{\alpha+\gamma N}{e}}}{\alpha}}$ </td></tr><tr><td>Cum. sales at max. diffusion rates</td><td> $\hat{x}_{l}^{m}=\frac{N}{2}-\frac{\alpha}{2\gamma}$ </td><td> $\hat{x}_{n}^{m}=\frac{N}{2}-\frac{\alpha}{2\gamma}$ </td></tr><tr><td>Sales peak time</td><td> $\hat{t}_{l}^{m}=\frac{2ln\frac{\gamma N}{\alpha}}{\alpha+\gamma N}\ln\frac{\gamma N}{\alpha}$ </td><td> $\hat{t}_{n}^{m}=\frac{e}{\alpha+\gamma N}\ln\frac{\gamma N}{\alpha}$ </td></tr></table>

Proposition 1. If the demand rate is linear, the myopic pricing strategy follows a monotonically decreasing pattern over time; if the demand rate is nonlinear, the myopic pricing adopts a constant pricing strategy.

Although the pricing strategy is different, the sales rate peaks when the cumulative sales reach the same level. Since $e { > } 2 ,$ , comparing the sales peak times we see that the sales peaks earlier under the nonlinear demand. So the market penetration is more aggressive under the nonlinear demand.

## 4.2. Forward-looking pricing

The following proposition characterizes the pricing pattern under forward-looking pricing. For the special case in which the <sup>fi</sup>rm does not discount future pro<sup>fi</sup>ts at a positive rate $( \mathrm { i } . \mathrm { e } . , \rho { = } 0 )$ , we can derive the following results.

Proposition 2. a) If the demand rate is linear, the optimal pricing path has the following properties:

1) $I f \propto < \frac { \gamma N } { 2 } ,$ then the optimal price increases when $\begin{array} { r } { x { < } \frac { N - \theta p } { 3 } - \frac { 2 \alpha } { 3 \nu } , } \end{array}$ and decreases when $\chi > \frac { N - \theta p } { 3 } \ : - \frac { 2 \alpha } { 3 \gamma }$ . The price will peak at the point $\begin{array} { r } { \hat { x } _ { l } ^ { f } = \frac { N - \theta p } { 3 } - \frac { 2 \alpha } { 3 \gamma } . } \end{array}$

2) $\begin{array} { r } { I f \propto \ge \frac { \gamma N } { 2 } , } \end{array}$ then the optimal price decreases monotonically.

b) If the demand rate is nonlinear, the optimal pricing path has the fol lowing properties:

1) $I f \alpha { < } \gamma N ,$ then the optimal price increases when $\scriptstyle x ( t ) < { \frac { 1 } { 2 } } \ \left( N - { \frac { \alpha } { \gamma } } \right)$ and decreases when $\scriptstyle x ( t ) > { \frac { 1 } { 2 } } \ \left( N - { \frac { \alpha } { \gamma } } \right)$ . The price will peak at the point $\begin{array} { r } { \hat { x } _ { n } ^ { f } = \frac { 1 } { 2 } \left( N - \frac { \alpha } { \gamma } \right) } \end{array}$ where the maximum market penetration also occurs.

2) $I f \alpha { \geq } \gamma N ,$ then the optimal price decreases monotonically.

Comparing a) and b) in Proposition 2 we <sup>fi</sup>nd that $\hat { x } _ { n } ^ { f } { > } \hat { x } _ { l } ^ { f } .$ . It implies that at the time of price peaks, the cumulative sales in market with nonlinear demand is higher than that with linear demand.

We also see that the pricing pattern critically depends on the relationship between the coef<sup>fi</sup>cient of innovation, coef<sup>fi</sup>cient of imitation, and the total market potential. When the imitation effect is relatively high (i.e., $\frac { \alpha } { \gamma } < \frac { N } { 2 } )$ , there is a price increasing period under both linear and nonlinear demand dynamics. When the innovation effect is relatively high $( \mathrm { i } . { \mathsf { e } } . , \quad \frac { \alpha } { v } { > } N )$ , the optimal price decreases under both linear and nonlinear demand dynamics. However, when the imitation effect is intermediate, $( \mathrm { i . e . , ~ } \frac { N } { 2 } < \frac { \alpha } { \gamma } < N )$ , then the optimal pricing curve monotonically decreases in markets with linear demand assumption but <sup>fi</sup>rst increases and then decreases in markets with nonlinear demand assumption. This is in sharp contrast to the myopic pricing strategies characterized in Proposition 1.

Dean [6] discussed two pricing strategies for the innovating <sup>fi</sup>rm to adopt before facing eventual competition. A skim pricing policy offers high initial prices followed by lower prices. A penetration pricing policy uses low initial prices to get into mass market early. Dolan and Jeuland [7] further found that, during the period of monopoly, a skim pricing policy is optimal if the demand curve is stable over time. In contrast, a penetration pricing policy is optimal if a durable good's demand is characterized by a diffusion process. If the total market size N is large enough or the market imitation effect is relatively large, conditions in Proposition 2 a1) and b1) hold. Our model suggests a penetration pricing strategy. Furthermore, our results show that, if the seller adopts a skim pricing policy, then very likely the market innovation effect is relatively large or the seller follows a myopic strategy under linear demand dynamics.

## 5. Online referral marketing with <sup>fi</sup>xed price

In reality, many product prices are relatively stable over time. The seller may use other marketing tools such as coupons and promotions to effectively in<sup>fl</sup>uence sales. In this section, we assume the product price is <sup>fi</sup>xed and examine the seller's optimal referral payment strategy under the two demand assumptions. The <sup>fi</sup>xed price assumption will be relaxed in the next section.

## 5.1. Myopic strategy

Assume the product selling price is <sup>fi</sup>xed at p over the entire planning horizon. The seller considers varying referral payment to in<sup>fl</sup>uence WOM and its effect on sales. It turns out that the optimal myopic strategy is characterized by a static policy under both the linear and the nonlinear demand dynamics, formally stated in the following proposition.

Proposition 3. If the product price is fixed, then the myopic referral strategy is a static policy determined by

$$
m ^ {m} (t) = \frac {p}{2} - \frac {\gamma}{2 \beta}\tag{7}
$$

under both linear and nonlinear demand dynamics.

Note that the condition m $! ^ { m } ( t ) { \geq } 0$ requires that $\begin{array} { r } { p { \geq } \frac { \gamma } { \beta } . } \end{array}$ Holding other factors constant, this suggests that the product unit price should be high enough to justify a formal referral program. Moreover, the threshold $\frac { \gamma } { \beta }$ increases as $\beta$ decreases. It further implies that, if the online referral marketing is not very responsive to market demand dynamics, only high price products can afford a referral marketing campaign.

It is a coincidence that the myopic referral strategy is the same under the two demand dynamics. This is in contrast to the optimal myopic pricing strategies in Section 4.1. Interestingly, under different demand dynamics, the myopic seller who would adopt different pricing strategies may come up with the same referral policy.

## 5.2. Forward-looking strategy

A forward-looking seller will consider the impact of earlier adoption on later sales. The seller's optimization problem is characterized in Eq. (6) subject to demand dynamics speci<sup>fi</sup>ed in Eqs. (2) and (4), respectively. Denote $Z ^ { - 1 }$ as the inverse function of the cumulative sales $z ( t )$ . We have the following proposition.

Proposition 4. a) Under the linear demand assumption, suppose $N { > } { \theta } p + { \frac { \alpha } { \gamma } }$ and $z ( T ) { > } \frac { N { - } { \Theta } p } { 2 }$ , there exists $\widetilde t _ { l } { \in } ( 0 , T )$ such that the optimal referral payment is non-increasing fort∈ $[ 0 , \tilde { t } _ { l }$ and non-decreasing for $t \in \left( \tilde { t } _ { l } , T \right]$ , where

$$
\tilde {t} _ {l} = Z ^ {- 1} \left[ \frac {N - \theta p}{2} - \frac {2 \beta (\rho \mu_ {l} + (\theta p + \mu_ {l}) \alpha)}{(\gamma + \beta (\theta p + \mu_ {l})) ^ {2}} \right].\tag{8}
$$

b) Under the nonlinear demand assumption, suppose $N { > } \frac { \alpha } { \gamma }$ and $z ( T ) { > } { \frac { N } { 2 } } ,$ there exists $\widetilde t _ { n } \in ( 0 ,$ ; T such that the optimal referral payment is nonincreasing for $t \in [ 0 , \tilde { t } _ { n } )$ and non-decreasing for $t { \in } ( \tilde { t } _ { n } , T ]$ , where

$$
\tilde {t} _ {n} = Z ^ {- 1} \left[ \frac {N}{2} - \frac {2 \beta \left(e ^ {s p} \rho \mu_ {n} + (p + \mu_ {n}) \alpha\right)}{(\gamma + \beta (p + \mu_ {n})) ^ {2}} \right].\tag{9}
$$

Proposition 4a) implies that, as long as the planning horizon is long enough for suf<sup>fi</sup>cient market penetration $( \mathrm { i } . \mathrm { e } . , z ( T ) { > } \frac { N - \theta p } { 2 } )$ , and the total market potential is large enough $( N { > } 6 p + { \frac { \alpha } { \gamma } } )$ , the optimal referral payment will generally feature a decreasing and then increasing pattern (non-monotonically). The insight for the decreasing trend at the beginning is to offer high incentive for initial market development. The intuition for the increasing trend near the end of the selling horizon is to pick up the remaining market potential.

Although the conditions are different under different demand dynamics, the optimal referral payment pattern is similar. Generally a forward-looking seller would decrease referral payment at the initial phase of market development, but increase the referral payment near the end of the selling horizon. The referral payment tends to be low in the middle of the product planning horizon. As opposed to the <sup>fi</sup>rst increasing and then decreasing pricing path characterized by Proposition 2, the incentive payment path characterized by Proposition 4 shows the reverse trend. Of course, the conditions are quite different as well.

## 6. Optimal pricing and referral strategies

It is well documented in the literature that elegant closed form solutions to complicated optimal control problems are few [21]. Since the system dynamics are very complicated under the general model, we are only able to derive analytical insights under certain conditions. Proposition 5 characterizes the relationship between the optimal pricing and referral payment paths under the myopic strategy. Under the nonlinear demand assumption, Proposition 6 states conditions under which the online referral marketing model is preferable to the base model. Proposition 7 states market conditions where both the optimal price and referral payment increase. Finally, we use a numerical example to show that the pricing and referral strategies could dramatically differ under different demand assumptions.

Proposition 5. Under the myopic strategy, the rate of change in referral payment is half of the rate of change in price $\begin{array} { r } { ( i . e . , \dot { m } = \frac { \dot { p } } { 2 } ) } \end{array}$ under both linear and nonlinear demand dynamics.

This result shows that the myopic seller will synchronize her strategic pricing and referral payment. When price increases (decreases), the referral payment increases (decreases) at the same time. The rate of change for referral payment is half of the scale of the rate of change for product price. This <sup>fi</sup>nding is consistent with the current business practice. The rate for af<sup>fi</sup>liates doing af<sup>fi</sup>liate marketing nowadays is about 10–60% of the item price. When the item price changes, so does the referral payment. The change in item price affects the change in referral payment with a prede<sup>fi</sup>ned percentage.

Apparently, the myopic referral strategy is simple to be executed in practice, but may not be optimal. The following proposition states some properties for the forward-looking strategy.

Proposition 6. Under the nonlinear demand assumption, $i f \beta { \leq } s \gamma ,$ , then it is optimal not to offer referral payment; $i f \beta > s \gamma ,$ then it is optimal to offer referral payment. Moreover, the referral marketing program has the following feature:

a) the referral payment $m ( t )$ monotonically increases over the entire planning horizon;

b) the price $p ( t )$ monotonically increases when t ${ \Sigma } Z ^ { - 1 } \left( \frac { N } { 2 } - \frac { \alpha } { \gamma } \right)$

Proposition 6 predicts that the strategy to use referral marketing critically depends on three key parameters: the coef<sup>fi</sup>cient of referral effectiveness $\beta ,$ the demand elasticity s, and the imitation coef<sup>fi</sup>cient γ. In general, if β is strongly responsive such that its effect is greater than the multiplicative effect of sγ, then it is optimal to adopt the referral marketing campaign over the entire product planning horizon. Moreover, the referral offering increases as the market is further penetrated. The non-decreasing referral payment shows the synergy between the nonlinear demand dynamics and the referral-based WOM sales.

In contrast, when the response to referral is not strong enough $( \mathrm { i } . \mathsf { e } . , \beta { < } s \gamma )$ , then it is optimal not to launch the referral marketing program. The intuition is that the seller <sup>fi</sup>nds it impossible to generate enough referral-based WOM sales to counterbalance its referral payment.

If deciding to use the referral marketing strategy, the seller would increase both the product price and the referral payment in the initial stage of market development. The increasing trend at least continues until the market penetration reaches almost half of the total market potential. This pricing pattern is consistent with the penetration pricing strategy discussed in the marketing literature.

Generally, $p ( t )$ exhibits a <sup>fi</sup>rst increasing, then decreasing pattern. Although it is impossible to derive clean analytical solutions, our numerical study shows that the price curve is well behaved. The increase and decrease are monotonic, and the peak time is unique.

Fig. 1 illustrates the optimal pricing and referral strategies (left panel) and sales dynamics (right panel) under the linear (denoted as L) and nonlinear demand (denoted as N) assumptions. The <sup>fi</sup>gure is plotted with parameter values $\alpha { = } 0 . 6 , \beta { = } 0 . 0 6 , \gamma { = } 0 . 0 8 , \rho { = } 0 . 1$ $s = 0 . 4 , N = 1 0 ,$ , and $T = 1 0$ . The total cumulative sales under the linear and nonlinear demand dynamics are 9.13 and 8.76, respectively. The total discounted pro<sup>fi</sup>ts are 30.52 and 24.91, respectively.

We see that, although both the cumulative sales patterns and the incremental sales rate patterns are similar under the two demand assumptions, the pricing and referral payment strategies are quite different. In this example, it is pro<sup>fi</sup>table to offer referral payment. Consistent with the prediction of Proposition 6 for nonlinear demand dynamics, it is optimal to increase referral over the entire product planning horizon. Under the linear demand assumption, in contrast, the optimal referral scheme started at similar level, decreased over time, and dropped to zero around T=2. The seller did not <sup>fi</sup>nd it bene<sup>fi</sup>cial to offer referral payment in later stage of the planning horizon.

The pricing patterns are also different. Under the linear demand dynamics, the optimal pricing strategy is to decrease the product price over the entire product planning horizon. Under the nonlinear demand dynamics, however, the price <sup>fi</sup>rst increases when the total number of cumulative sales is low, and then decreases.

Note that Fig. 1 is just for illustrative purpose. We demonstrate that, although the sales patterns might be similar, the pricing and referral strategies could dramatically differ under different demand dynamics. Other pricing and sales patterns exist. In next section, we systematically analyze the impact of key model parameters on the pricing and sales patterns as well as pro<sup>fi</sup>ts through sensitivity analysis.

## 7. Numerical study

In this section, we perform sensitivity analysis by focusing on some key model parameters. We not only look at how the optimal price and referral payment paths change when the parameter values change, but investigate their impact on pro<sup>fi</sup>t and sales. Furthermore, we quantify the bene<sup>fi</sup>t of adopting referral marketing over the base model without referral marketing. Although parameter values in this numerical study are chosen for illustrative convenience, their combination is comprehensive enough to represent typical scenarios of interest. The parametric choices enable us to present major qualitative insights of our analytical models.

## 7.1. Sensitivity analysis on key parameters

Recall that α, β, and γ are parameters that affect the conditional probabilities of purchase, and θ and s affect the demand rate. Fig. 2 compares the price and referral payment dynamics under both the linear and the nonlinear demand models when these key parameters change. The base model is $N = 1 0 , \ T = 1 0 , \ s = 0 . 5 , \ \theta = 0 . 1 , \alpha = 0 . 1$ $\gamma { = } 0 . 0 5$ , and $\gamma / \beta = 0 . 5$ . The total cumulative sales and discounted pro<sup>fi</sup>t are recorded in Table 3.

We see that when the coef<sup>fi</sup>cient of innovation α increases, the initial price increases but the initial referral payment decreases under the linear demand dynamics. In contrast, although the initial price increases, the referral payment keeps unchanged under the nonlinear demand dynamics. Both the discounted pro<sup>fi</sup>t and the cumulative sales increase under both demand assumptions. This implies that the referral payment should decrease as the market innovation effect becomes stronger.

When the coef<sup>fi</sup>cient of imitation γ decreases, the price variation decreases over the entire product planning horizon, and the referral payment increases under the linear demand assumption. In comparison, although the price variation decreases under the nonlinear demand assumption, the referral payment decreases rather than increases. Both the discounted pro<sup>fi</sup>t and the cumulative sales decrease under both demand dynamics. The intuition is that, although the optimal referral payment may increase or decrease under different demand assumptions, the seller will make less pro<sup>fi</sup>t and sales if the market WOM effect is weak.

When the demand sensitivity coef<sup>fi</sup>cient θ or the demand elasticity s increases, both price and referral payment tend to decrease. The discounted pro<sup>fi</sup>t and the cumulative sales decrease as well. The same trend is observed for both the linear and nonlinear demand dynamics.

## 7.2. With or without online referral marketing

In this section, we show that the bene<sup>fi</sup>t of adopting the online referral marketing varies across different parameters that affect the market dynamics. Table 4 compares cases under three lengths of the selling horizon $( T = \{ 5 , 1 0 , 2 0 \} )$ ), three levels of initial adoption (x(0) or $z ( 0 ) = \{ 0 , 2 0 \% N , 5 0 \% N \} )$ , and two market sizes $( N = \{ 1 0 , 1 0 0 \} )$ ). The relative WOM γ/α={0.1, 1}, representing low or high effect, and the coef<sup>fi</sup>cient of referral $\beta = \{ 0 . 0 0 0 5 , 0 . 0 0 5 , 0 . 0 5 \}$ , representing low, medium, and high effects. We present four operational characteristics including switching time (T\_Switch), sales peak time (T\_Peak), <sup>fi</sup>nal market share measured by total cumulative sales divided by total market size (S\_Percent), and pro<sup>fi</sup>t ratio measured by total discounted pro<sup>fi</sup>t of the referral marketing model divided by that of the base model (P\_Ratio).

![](/api/attachments/SBVZC7J2/fulltext/images/064f65976b155241810d34f2a391cd1d06922e2d93969f058bbe60ccc59e6fd0.jpg)

![](/api/attachments/SBVZC7J2/fulltext/images/090a197059944cdbe2ed31f9ba31f5651e3d1f64fb3b4540107c038a2919b82d.jpg)  
Fig. 1. Comparison of pricing and sales patterns: linear vs. nonlinear demand dynamics

![](/api/attachments/SBVZC7J2/fulltext/images/5adaf8c894964f5b0540c8d9ebecd16e76c1fde3a7ca46cb8c481ae9af09a606.jpg)

![](/api/attachments/SBVZC7J2/fulltext/images/359716d5f72c09e4d6dce8b62cbb2153585567db9f10d2ffe53ef5089052ff58.jpg)

![](/api/attachments/SBVZC7J2/fulltext/images/3ab8e52c1a97b851d87448de6652aca98d74ce8455e163c8997f704c51b1b07e.jpg)

![](/api/attachments/SBVZC7J2/fulltext/images/15fe235d08bfd913493a994e8fa3ad67dba343ffedc8c602d4b05c999583678b.jpg)  
Fig. 2. Price and incentive payment: linear vs. nonlinear demand dynamics.

We observe that generally large market shows greater bene<sup>fi</sup>t than smaller market. In addition, the referral marketing model is more ef<sup>fi</sup>cient in large market with high WOM effect, especially when the initial market is not well developed and when the WOM response to referral is not weak. It can yield as high as 25 times more of the total pro<sup>fi</sup>t than that in the base model (see P\_Ratio in the Table).

Due to the intense market competition, many types of consumer products have very short life cycles. Our numerical results show that the referral marketing strategy can generate more pro<sup>fi</sup>t than the base model when the selling horizon is short.

## 8. Summary and concluding remarks

In this paper we theoretically analyze the optimal pricing and referral reward strategies under different demand side dynamics. Although the sales patterns are similar, we <sup>fi</sup>nd the price and referral payment strategies differ dramatically. If the seller decides not to employ an online referral marketing program, then a myopic seller would adopt a constant pricing strategy under the nonlinear demand dynamics and a monotonic decreasing pricing strategy under the linear demand dynamics. The forward-looking pricing pattern critically depends on the ratio of the innovation coef<sup>fi</sup>cient and the imitation coef<sup>fi</sup>cient. If the ratio is small (i.e., the imitation effect is strong), a forward-looking seller would prefer a penetration pricing policy in which price <sup>fi</sup>rst increases and then decreases.

Under the <sup>fi</sup>xed product price, if the seller decides to employ a referral marketing strategy, then the myopic referral payment policy is a static policy under both the linear and the nonlinear demand dynamics. In contrast to their different pricing strategies, the myopic seller would adopt the same referral policy. The forward-looking referral strategy is similar under different demand dynamics. Generally, the optimal referral payment would decrease in initial phase of market development but increase near the end of the selling horizon. This is in sharp contrast with the myopic strategy.

If both price and referral strategies change over time, then a myopic seller would choose the rate of change in referral payment as half of the rate of change in price under both the linear and the nonlinear demand dynamics. A forward-looking seller's optimal strategy critically depends on the demand assumptions. Under the nonlinear demand dynamics, if the demand is responsive to referral payment, then it is optimal to adopt a referral marketing program throughout the entire planning period. Moreover, the optimal referral payment increases over time. If the demand is not responsive enough, then it is optimal not to adopt the referral marketing campaign. Under the linear demand assumption, the prediction is quite different. The referral payment can be decreasing. More importantly, offering referral payment is not an all-or-nothing decision. It can be optimal to only adopt referral marketing in initial phase of product introduction but rely on traditional WOM marketing for the rest of the product life cycle.

Sales and pro<sup>fi</sup>t under linear and nonlinear demand.

<table><tr><td rowspan="2">Demand dynamics</td><td colspan="4">Discounted profit</td><td colspan="4">Cumulative sales</td></tr><tr><td>Base</td><td> $\alpha \uparrow$ </td><td> $\gamma \downarrow$ </td><td> $\theta(s) \uparrow$ </td><td>Base</td><td> $\alpha \uparrow$ </td><td> $\gamma \downarrow$ </td><td> $\theta(s) \uparrow$ </td></tr><tr><td>Linear</td><td>46.12</td><td>54.07</td><td>26.83</td><td>20.28</td><td>8.49</td><td>8.78</td><td>4.97</td><td>7.76</td></tr><tr><td>Nonlinear</td><td>9.98</td><td>14.89</td><td>4.41</td><td>3.86</td><td>7.66</td><td>8.24</td><td>3.23</td><td>6.49</td></tr></table>

Table 4  
Comparison of referral marketing model vs. the base model.

<table><tr><td rowspan="2">Initial z(0) (x(0))</td><td rowspan="2">Metrics</td><td colspan="3">Small Mkt/High WOM/High β</td><td colspan="3">Large Mkt/High WOM/Medium β</td><td colspan="3">Large Mkt/Low WOM/Low β</td></tr><tr><td>T=5</td><td>10</td><td>20</td><td>T=5</td><td>10</td><td>20</td><td>T=5</td><td>10</td><td>20</td></tr><tr><td rowspan="4">0</td><td>T_Switch</td><td>NA</td><td>NA</td><td>11.68</td><td>NA</td><td>NA</td><td>16.47</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>T_Peak</td><td>5.0(3.06)</td><td>4.18(4.59)</td><td>3.83(5.61)</td><td>1.28(3.25)</td><td>1.28(4.42)</td><td>1.29(14.86)</td><td>5.0(5.0)</td><td>10.0(10.0)</td><td>4.29(0)</td></tr><tr><td>S_Percent</td><td>0.88(0.49)</td><td>0.69(0.55)</td><td>0.92(0.88)</td><td>0.85(0.04)</td><td>0.94(0.26)</td><td>0.98(0.72)</td><td>0.36(0.12)</td><td>0.57(0.21)</td><td>0.82(0.43)</td></tr><tr><td>P_Ratio</td><td>1.42</td><td>1.24</td><td>1.19</td><td>25.51</td><td>9.70</td><td>6.71</td><td>1.79</td><td>1.77</td><td>1.66</td></tr><tr><td rowspan="4">20%N</td><td>T_Switch</td><td>NA</td><td>NA</td><td>8.26</td><td>NA</td><td>NA</td><td>15.21</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>T_Peak</td><td>5.0(5.0)</td><td>0.61(3.27)</td><td>0.61(2.45)</td><td>0.1(3.27)</td><td>0.07(6.19)</td><td>0.14(13.66)</td><td>5.0(3.67)</td><td>0.61(0)</td><td>0.41(0)</td></tr><tr><td>S_Percent</td><td>0.62(0.53)</td><td>0.79(0.75)</td><td>0.95(0.94)</td><td>0.88(0.47)</td><td>0.95(0.70)</td><td>0.99(0.92)</td><td>0.56(0.31)</td><td>0.72(0.41)</td><td>0.86(0.58)</td></tr><tr><td>P_Ratio</td><td>1.19</td><td>1.11</td><td>1.11</td><td>2.80</td><td>2.25</td><td>2.19</td><td>2.43</td><td>2.13</td><td>2.00</td></tr><tr><td rowspan="4">50%N</td><td>T_Switch</td><td>NA</td><td>4.06</td><td>3.87</td><td>NA</td><td>NA</td><td>13.33</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>T_Peak</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td><td>0.0(0.0)</td></tr><tr><td>S_Percent</td><td>0.77(0.76)</td><td>0.89(0.88)</td><td>0.97(0.97)</td><td>0.91(0.74)</td><td>0.96(0.87)</td><td>0.99(0.97)</td><td>0.72(0.58)</td><td>0.81(0.65)</td><td>0.90(0.76)</td></tr><tr><td>P_Ratio</td><td>1.03</td><td>1.03</td><td>1.03</td><td>1.77</td><td>1.59</td><td>1.60</td><td>2.17</td><td>1.91</td><td>1.82</td></tr></table>

Our model also offers several managerial insights. Our numerical studies show that the referral marketing strategy has great potential in large markets with strong WOM effect, especially for short life cycle products when the initial market is not developed.

One limitation of this study is that we do not consider the consumer's willingness to make referral and the behavior of a referred customer. We only take into account the effects of price and referral reward on the probabilities of buying and referring. In reality, a referred customer makes a purchasing decision when the surplus from buying is nonnegative. A customer makes a recommendation when the expected surplus from recommending the product exceeds the cost of referring other consumers. In future study, we may endogenize these decision factors and build models based on consumer utility theory. In addition, real world data can be collected to validate our model predictions.

## Acknowledgments

The author is indebted to the editor and anonymous referees for valuable comments. The author thanks Kevin Chiang for helpful discussions on initial ideas, models, as well as insights shared with this research.

## Appendix A. Notation table

<table><tr><td>Parameters</td><td>Interpretation</td></tr><tr><td> $\alpha$ </td><td>Coefficient of innovation</td></tr><tr><td> $\gamma$ </td><td>Coefficient of imitation</td></tr><tr><td> $\beta$ </td><td>Coefficient of referral</td></tr><tr><td> $\theta$ </td><td>Demand responsiveness to price in the liner demand model,  $\theta >0$ </td></tr><tr><td>s</td><td>Price elasticity in the nonlinear demand model</td></tr><tr><td> $\rho$ </td><td>Discount rate for profit</td></tr><tr><td>N</td><td>The population size (or maximum market potential)</td></tr><tr><td>x(t)</td><td>Cumulative sales in the traditional WOM marketing model</td></tr><tr><td> $\dot{x}(t)$ </td><td>Instantaneous sales rates in the traditional WOM marketing model</td></tr><tr><td>y(t)</td><td>Cumulative referral-based sales in the referral marketing model</td></tr><tr><td> $\dot{y}(t)$ </td><td>Instantaneous referral-based sales rates in the referral marketing model</td></tr><tr><td>z(t)</td><td>Total cumulative sales in the referral marketing model</td></tr><tr><td> $\dot{z}(t)$ </td><td>Total instantaneous sales in the referral marketing model</td></tr><tr><td>p(t)</td><td>Per unit selling price</td></tr><tr><td>m(t)</td><td>Per unit referral payment in referral marketing model</td></tr><tr><td>T</td><td>Finite planning horizon</td></tr></table>

## Appendix B. Proof of Table 2

1) The linear demand dynamics:

Under the myopic pricing strategy, the monopolist maximizes the instantaneous pro<sup>fi</sup>t. The optimization problem under linear demand dynamics can be expressed as:

$$
\begin{array}{l l} \underset {p (t)} {\text { Max }} & p (t) \dot {x} (t) \\ s. t. & \dot {x} (t) = (\alpha + \gamma x (t)) (N - x (t) - \theta p (t)) \end{array}\tag{10}
$$

Solving for $p ( t )$ we obtain $\begin{array} { r } { p _ { l } ^ { m } ( t ) = \frac { N - x ( t ) } { 2 \Theta } . } \end{array}$

Substituting $p _ { l } ^ { m } ( t )$ into x t˙ and separating variables yields $\int _ { 0 } ^ { x } \frac { 2 d x ( t ) } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } = \int _ { 0 } ^ { t }$ dt. Using the method of partial fraction to integrate the left-hand-side, we write $\begin{array} { r } { \frac { 1 } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } = \frac { A } { \alpha + \gamma x ( t ) } + \frac { B } { N - x ( t ) } , } \end{array}$ , where $\begin{array} { r } { A = \frac { 1 } { N + \frac { \alpha } { \gamma } } , B = \frac { 1 } { \alpha + \gamma N } . } \end{array}$ . Since $\begin{array} { r } { \frac { 1 } { \alpha + \gamma N } \displaystyle \int _ { 0 } ^ { x } \frac { d \gamma x } { \alpha + \gamma x } = \frac { 1 } { \alpha + \gamma N } l n ( \alpha + \gamma x ) , \frac { 1 } { \alpha + \gamma N } \displaystyle \int _ { 0 } ^ { x } \frac { d x } { N - x } = } \end{array}$ $\begin{array} { r } { - \frac { 1 } { \alpha + \gamma N } l n ( N - x ) } \end{array}$ , we have $\int _ { 0 } ^ { x } { \frac { 2 d x ( t ) } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } } = { \textstyle { \frac { 2 } { \alpha + \gamma N } } } l n { \frac { \alpha + \gamma x } { N - x } }$ . Therefore, $\begin{array} { r } { l n \frac { \alpha + \gamma x } { N - x } = \frac { \alpha + \gamma N } { 2 } ( t + c ) . \mathrm { O r } , \frac { \alpha + \gamma x } { N - x } = K e ^ { \frac { \alpha + \gamma N } { 2 } t } } \end{array}$ . Since $x ( 0 ) = 0 ,$ , we have $\begin{array} { r } { K = \frac { \alpha } { N } . } \end{array}$ Solving the equation for x(t) we have $\begin{array} { r } { x ( t ) = \frac { 1 - e ^ { - \frac { ( \alpha + \gamma N ) t } { 2 } } } { \frac { 1 } { N } + \frac { \gamma } { \alpha } e ^ { - \frac { ( \alpha + \gamma N ) t } { 2 } } } . } \end{array}$

Substituting x(t) into $p _ { l } ^ { m } ( t )$ we have $\begin{array} { r } { p _ { l } ^ { m } ( t ) = \frac { N } { 2 \Theta } - \frac { 1 - e ^ { - \frac { ( \alpha + \gamma N ) t } { 2 } } } { 2 \Theta \left( \frac { 1 } { N } + \frac { \gamma } { \alpha } e ^ { - \frac { ( \alpha + \gamma N ) t } { 2 } } \right) } \cdot } \end{array}$

Since the diffusion rate is at a maximum when $\ddot { x } = 0 ,$ differentiating x˙ and solving for x we have $\begin{array} { r } { \hat { x } _ { l } ^ { m } = \frac { N } { 2 } - \frac { \alpha } { 2 \nu } } \end{array}$ .

Substituting $\ v { \hat { x } } _ { l } ^ { m }$ into x(t) we <sup>fi</sup>nd the sales peak time $\begin{array} { r } { \hat { t } _ { l } ^ { m } = \frac { 2 l n \frac { \gamma N } { \alpha } } { \alpha + \gamma N } . } \end{array}$ 2) The nonlinear demand dynamics;

Under the myopic pricing strategy, the optimization problem is:

$$
\begin{array}{l l} \underset {p (t)} {\text { Max }} & p (t) \dot {x} (t) \\ s. t. & \dot {x} (t) = e ^ {- s p (t)} (\alpha + \gamma x (t)) (N - x (t)) \end{array}\tag{11}
$$

Solving for $p ( t )$ we obtain $\begin{array} { r } { p _ { n } ^ { m } = \frac { 1 } { s } . } \end{array}$

Substituting $p _ { n } ^ { m }$ into x t˙ and separating variables yields $\int _ { 0 } ^ { x } \frac { e d x ( t ) } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } = \int _ { 0 } ^ { t } c$ t. Using the method of partial fraction to integrate the left-hand-side, we write $\begin{array} { r } { \frac { 1 } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } = \frac { A } { \alpha + \gamma x ( t ) } + \frac { B } { N - x ( t ) } , } \end{array}$ where $\begin{array} { r } { A = \frac { 1 } { N + \frac { \alpha } { \gamma } } , B = \frac { 1 } { \alpha + \gamma N } . } \end{array}$ Since $\begin{array} { r } { \frac { 1 } { \alpha + \gamma N } \displaystyle \int _ { 0 } ^ { \alpha } \frac { d \gamma x } { \alpha + \gamma x } = \frac { 1 } { \alpha + \gamma N } l n ( \alpha + \gamma x ) } \end{array}$ $\begin{array} { r } { \frac { 1 } { \alpha + \gamma N } \displaystyle \int _ { 0 } ^ { x } \frac { d x } { N - x } = - \frac { 1 } { \alpha + \gamma N } l n ( N - x ) } \end{array}$ , we have $\int _ { 0 } ^ { x } { \frac { e d x ( t ) } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } } = { \frac { e } { \alpha + \gamma N } }$ $l n { \frac { \alpha + \gamma x } { N - x } }$ . Therefore, l $\begin{array} { r } { n \frac { \alpha + \gamma x } { N - x } = \frac { \alpha + \gamma N } { e } ( t + c ) . \ 0 \mathrm { r } , \ \frac { \alpha + \gamma x } { N - x } = K e ^ { \frac { \alpha + \gamma N } { e } t } } \end{array}$ . Since x $( 0 ) = 0$ , we have $\begin{array} { r } { K = \frac { \alpha } { N } . } \end{array}$ Solving the equation for x we obtain $\begin{array} { r } { x _ { n } ^ { m } ( t ) = \frac { 1 - e ^ { - \frac { \alpha + \gamma N } { e } t } } { \frac { 1 } { N } + \frac { \gamma } { \alpha } e ^ { - \frac { \alpha + \gamma N } { e } t } } . } \end{array}$

The maximum penetration rate occurs at $\ddot { x } = 0$ , differentiating x˙ and solving for x we have $\begin{array} { r } { \hat { x } _ { n } ^ { m } = \frac { N } { 2 } - \frac { \alpha } { 2 \nu } . } \end{array}$

Substituting $\hat { x } _ { n } ^ { m }$ into $x _ { n } ^ { m } ( t )$ we have $\begin{array} { r } { \hat { t } _ { n } ^ { m } = \frac { e } { \alpha + \gamma N } l n \frac { \gamma N } { \alpha } } \end{array}$

## Appendix C. Proof of propositions

Without causing confusion, we suppress the time argument in the following proofs when appropriate.

Proof of Proposition 1

Proof of Proposition 1 immediately follows from the calculation of the optimal myopic prices under the linear and nonlinear demand dynamics in Table 2.

## Proof of Proposition 2

a) The optimization problem under the linear demand dynamics is:

$$
\begin{array}{l l} \underset {p (t), m (t)} {\text { Max }} & \int_ {0} ^ {T} e ^ {- \rho t} p (t) \dot {x} (t) d t \\ s. t. & \dot {x} (t) = (\alpha + \gamma x (t)) (N - x (t) - \theta p (t)) \end{array}\tag{12}
$$

De<sup>fi</sup>ne the current value Hamiltonian of the optimization problem as

$$
H (x, p, \lambda_ {l}, t) = (p + \lambda_ {l}) (\alpha + \gamma x) (N - \theta p - x),\tag{13}
$$

where $\lambda _ { l }$ is the costate variable.

Without discount of pro<sup>fi</sup>t, the <sup>fi</sup>rst order condition with respect to $\lambda _ { l }$ yields

$$
\dot {\lambda} _ {l} = - (p + \lambda_ {l}) [ - \alpha + \gamma (N - \theta p - 2 x) ].\tag{14}
$$

The <sup>fi</sup>rst order necessary condition for price satis<sup>fi</sup>es $\begin{array} { r } { p = \frac { N - { { x } - { { \lambda } _ { l } } \theta } } { { { 2 } \theta } } . } \end{array}$ . Furthermore, $\begin{array} { r } { \dot { p } = - \frac { 1 } { 2 \Theta } \left( \dot { x } + \dot { \bf { \hat { h } } } \Theta \right) = - \frac { 1 } { 2 \Theta } ( \hat { N } - x - \Theta p ) [ 2 \alpha - \gamma ( N - \Theta p - 3 x ) ] } \end{array}$ Therefore, $\scriptstyle { \dot { p } } > 0$ <sup>2θ</sup> when $2 \alpha - \gamma ( N - \theta p - 3 x ) < 0$ . That is, if $\begin{array} { r } { x { < } \frac { N - \theta p } { 3 } - \frac { 2 \alpha } { 3 \gamma } , } \end{array}$ then $\dot { p } { > } 0$ and the optimal price increases; if $\begin{array} { r } { \chi { > } \frac { N - \theta p } { 3 } - \frac { 2 \alpha } { 3 \gamma } , } \end{array}$ then $\scriptstyle { \dot { p } } < 0$ and the optimal price decreases. The conditionαb <sup>γN</sup> is obtained by examining the necessary condition $\frac { N - \theta p } { 3 } - \frac { 2 \alpha } { 3 \gamma } { > } 0$

b) The optimization problem under the nonlinear demand dynamics is:

$$
\begin{array}{l l} \underset {p (t), m (t)} {\text { Max }} & \int_ {0} ^ {T} e ^ {- \rho t} p (t) \dot {x} (t) d t \\ s. t. & \dot {x} (t) = e ^ {- s p (t)} (\alpha + \gamma x (t)) (N - x (t)) \end{array}\tag{15}
$$

De<sup>fi</sup>ne the current value Hamiltonian of the optimization problem as

$$
H (x, p, \lambda_ {n}, t) = (p + \lambda_ {n}) e ^ {- s p} (\alpha + \gamma x) (N - x),\tag{16}
$$

where $\lambda _ { n }$ is the costate variable.

Without discount of pro<sup>fi</sup>t, the system dynamics is controlled by the following system of differential equations:

$$
\dot {\lambda} _ {n} = - e ^ {- s p} (p + \lambda_ {n}) (- \alpha + \gamma (N - 2 x))\tag{17}
$$

$$
\dot {x} = e ^ {- s p} (\alpha + \gamma x) (N - x)\tag{18}
$$

The <sup>fi</sup>rst order necessary condition for price satisfies

$$
p = \frac {1}{s} - \lambda_ {n}.\tag{19}
$$

Combining Eqs. (17), (18), and (19) we have

$$
\frac {\dot {\lambda} _ {n}}{\dot {x}} = - \frac {\gamma (N - 2 x) - \alpha}{s (\alpha + \gamma x) (N - x)}.\tag{20}
$$

By integration and solving for λ, we get $\begin{array} { r } { \Lambda _ { n } ( t ) = \frac { 1 } { s } \ l n \frac { ( \alpha + \gamma x ( T ) ) ( N - x ( T ) ) } { ( \alpha + \gamma x ( t ) ) ( N - x ( t ) ) } } \end{array}$ Differentiating Eq. (19) with respect to t we get $\dot { p } = - \dot { \lambda } _ { n }$

Substituting Eqs. (19) into (17) yields

$$
\dot {\lambda} _ {n} = - e ^ {- s p} \frac {1}{s} [ - \alpha + \gamma (N - 2 x) ].\tag{21}
$$

Examining the sign in $\operatorname { E q . } ( 2 1 )$ and the fact that $\dot { p } = - \dot { \lambda } _ { n }$ we have the results for the pricing pattern. The condition αbγN is obtained by examining the necessary condition $\frac { 1 } { 2 } ~ \left( N - \frac { \alpha } { \gamma } \right) { > } 0$

## Proof of Proposition 3

The myopic policy maximizes the instantaneous pro<sup>fi</sup>t subject to the demand dynamics (2) and (4). The optimization problem under the linear demand dynamics is:

$$
\begin{array}{l l} \underset {m (t)} {\text {Max}} & p \dot {z} (t) - m (t) \dot {y} (t) \\ s. t. & \begin{array}{l} \dot {z} (t) = (\alpha + (\gamma + \beta m (t)) z (t)) (N - z (t) - \theta p) \\ \dot {y} (t) = (\gamma + \beta m (t)) z (t) (N - z (t) - \theta p) \end{array} \end{array}\tag{22}
$$

The optimization problem under the nonlinear demand dynamics is

$$
\begin{array}{l l} \underset {m (t)} {\text { Max }} & p \dot {z} (t) - m (t) \dot {y} (t) \\ s. t. & \dot {z} (t) = e ^ {- s p} (\alpha + (\gamma + \beta m (t)) z (t)) (N - z (t)) \\ & \dot {y} (t) = e ^ {- s p} (\gamma + \beta m (t)) z (t) (N - z (t)) \end{array}\tag{23}
$$

Write the <sup>fi</sup>rst order condition with respect to $m ( t )$ we <sup>fi</sup>nd that the myopic referral in Eqs. (22) and (23) are the same as follows:

$$
m _ {l} ^ {m} (t) = m _ {n} ^ {m} (t) = \frac {p}{2} - \frac {\gamma}{2 \beta}.\tag{24}
$$

Proof of Proposition 4

a) The linear demand dynamics:

De<sup>fi</sup>ne the current value Hamiltonian of the optimization problem as:

$$
\begin{array}{c} H (z, m, \mu_ {l}, t) = (p + \mu_ {l}) (\alpha + (\gamma + \beta m) z) (N - z - \theta p) \\ - m (\gamma + \beta m) z (N - z - \theta p), \end{array}\tag{25}
$$

where $\mu _ { l }$ is the costate variable.

The <sup>fi</sup>rst order necessary condition for referral m(t) satis<sup>fi</sup>es

$$
m ^ {*} (t) = \frac {p + \mu_ {l} (t)}{2} - \frac {\gamma}{2 \beta}.\tag{26}
$$

Substituting m(t) into the necessary condition for optimality we have

$$
\begin{array}{l} \dot {\mu} _ {l} = \rho \mu_ {l} - \frac {\partial H}{\partial z} \\ \qquad = \rho \mu_ {l} - \left[ - \frac {\alpha}{\beta} (\gamma + 2 \beta m ^ {*}) + \frac {1}{\beta} (\gamma + \beta m ^ {*}) ^ {2} (N - \theta p - 2 z) \right]. \end{array}\tag{27}
$$

By integration we derive

$$
\mu_ {l} = \int_ {t} ^ {T} e ^ {- \rho (\tau - t)} \left[ - \frac {\alpha}{\beta} (\gamma + 2 \beta m ^ {*}) + \frac {1}{\beta} (\gamma + \beta m ^ {*}) ^ {2} (N - \theta p - 2 z) \right] d \tau .\tag{28}
$$

Setting ${ \dot { \mu } } _ { l } = 0$ we have the switching point uniquely determined by

$$
\tilde {z} _ {l} = \frac {N - \theta p}{2} - \frac {2 \beta (\rho \mu_ {l} + (\theta p + \mu_ {l}) \alpha)}{(\gamma + \beta (\theta p + \mu_ {l})) ^ {2}}.\tag{29}
$$

Denote the inverse function as $Z ^ { - 1 }$ . The terminal condition $\mu _ { l } ( T ) =$ 0 and $z ( T ) { > } \frac { N { - } 6 p } { 2 }$ imply that $\dot { \mu } _ { l } ( T ) { > } 0$

Under mild condition $N { \geq } { \mathsf { 6 } } p + { \frac { \alpha } { v } }$ (this condition will easily hold when the market is suf<sup>fi</sup>ciently large) we can verify that $\textstyle { \frac { 1 } { \mathrm { ( } \gamma + } }$ βm $) [ ( \gamma + \beta m ^ { * } ) ( N - \theta p ) - \alpha ] - \alpha m > 0 .$ . Therefore, if $\mu _ { l } ( 0 ) { \leq } 0 ,$ , by (27) we have $\dot { \mu } _ { l } ( 0 ) < 0$ . Since μ is continuous on [0, T], there must exist $\tilde { t } \in ( 0 , T )$ such that ${ \dot { \bf \mu } } _ { l } ( { \tilde { t } } ) = 0$

If $\mu _ { l } ( 0 ) { > } 0 ,$ , then $\begin{array} { r } { \mu _ { q } \Big ( Z ^ { - 1 } \Big ( \frac { N - 0 p } { 2 } \Big ) \Big ) = \displaystyle \int _ { 0 } ^ { T } e ^ { - \Theta \big ( \tau - Z ^ { - 1 } \big ( \frac { N - 6 p } { 2 } \big ) \big ) } \left[ - \frac { \alpha } { \beta } ( \gamma + 2 \beta m ^ { * } ) \right] } \end{array}$ dτb0 implies that there exists $\scriptstyle { \overline { { t } } } \in \left( 0 , Z ^ { - 1 } \left( { \frac { N - \theta p } { 2 } } \right) \right)$ such that $\begin{array} { r } { \dot { \mu } _ { l } ( t ) = \frac { \mu \left( Z ^ { - 1 } \left( \frac { N - \theta p } { 2 } \right) \right) - \mu ( 0 ) } { Z ^ { - 1 } \left( \frac { N - \theta p } { 2 } \right) - 0 } < 0 . } \end{array}$ . Since $\dot { \mu } _ { l } \left( \overline { { t } } \right) < 0$ and ${ \bf \dot { \mu } } _ { l } ( T ) { \bf > } 0$ , there exists t<sup>˜</sup>∈ t ; T such that $\dot { \mu } _ { l } ( \tilde { t } ) = 0$

b) The nonlinear demand dynamics:

De<sup>fi</sup>ne the current value Hamiltonian of the optimization problem as:

$$
\begin{array}{c} H (z, m, \mu_ {n}, t) = (p + \mu_ {n}) e ^ {- s p} (\alpha + (\gamma + \beta m) z) (N - z) \\ - m e ^ {- s p} (\gamma + \beta m) z (N - z), \end{array}\tag{30}
$$

where $\mu _ { n }$ is the costate variable.

The <sup>fi</sup>rst order necessary condition for referral m(t) satis<sup>fi</sup>es

$$
m (t) = \frac {p + \mu_ {n}}{2} - \frac {\gamma}{2 \beta}.\tag{31}
$$

Substituting m(t) into the necessary condition for optimality we have

$$
\begin{array}{l} \dot {\mu} _ {n} = \rho \mu_ {n} - \frac {\partial H}{\partial z} \\ = \rho \mu_ {n} - e ^ {- s p} \left[ - \frac {\alpha}{\beta} (\gamma + 2 \beta m ^ {*}) + \frac {1}{\beta} (\gamma + \beta m ^ {*}) ^ {2} (N - 2 z) \right]. \end{array}\tag{32}
$$

By integration we derive

$$
\mu_ {n} = \int_ {t} ^ {T} e ^ {- s p - \rho (\tau - t)} \left[ - \frac {\alpha}{\beta} \left(\gamma + 2 \beta m ^ {*}\right) + \frac {1}{\beta} \left(\gamma + \beta m ^ {*}\right) ^ {2} (N - 2 z) \right] d \tau .\tag{33}
$$

Setting $\dot { \mu } _ { n } = 0$ we have the switching point uniquely determined by

$$
\tilde {z} _ {n} = \frac {N}{2} - \frac {2 \beta \left(e ^ {s p} \rho \mu_ {n} + (p + \mu_ {n}) \alpha\right)}{(\gamma + \beta (p + \mu_ {n})) ^ {2}}.\tag{34}
$$

The terminal condition $\mu _ { n } ( T ) = 0$ and $z ( T ) { > } \frac { N } { 2 }$ imply that $\dot { \mu } _ { n } ( T ) > 0$ Under mild condition $N { \geq } { \frac { \alpha } { \gamma } }$ we can verify that $- \frac { \alpha } { \beta }$ $( \gamma + 2 \beta m ^ { * } ) + \frac { 1 } { \beta } \left( \gamma + \beta m ^ { * } \right) ^ { 2 } N { > } 0$ . Therefore, if $\mu _ { n } ( 0 ) { \leq } 0$ , by Eq. (32) we have $\dot { \mu } _ { n } ( 0 ) < 0$ . Since $\mu _ { \textit { n } }$ is continuous on [0, T], there must exist $\tilde { t } \in ( 0 , T )$ such that $\dot { \mu } _ { n } ( \widetilde { t } ) = 0$

一 $\mathrm { ~ f ~ } \mu _ { n } ( 0 ) { > } 0 ,$ , then $\overset { \iota \setminus , \ } { \mu } _ { n } \bigl ( Z ^ { - 1 } \left( \frac { N } { 2 } \right) \bigr ) = \int _ { 0 } ^ { \mathsf T } e ^ { - s p - \mathsf {  { \rho } } \left( \tau - Z ^ { - 1 } \left( \frac { N } { 2 } \right) \right) } \ \left\lceil - \frac { \alpha } { \beta } ( \gamma + 2 \beta m ^ { * } ) \right\rceil$ dτb0, there exists $\overline { { t } } \in ( 0 , Z ^ { - 1 } ( \frac { N } { 2 } ) )$ such that $\begin{array} { r } { \dot { \mu } _ { l } ( t ) = \frac { \mu \left( Z ^ { - 1 } \left( \frac { N } { 2 } \right) \right) - \mu ( 0 ) } { Z ^ { - 1 } \left( \frac { N } { 2 } \right) - 0 } < 0 . } \end{array}$ Since $\dot { \mu } _ { l } ( t ) < 0$ and $\dot { \mu } _ { l } ( T ) { > } 0$ , there exists $\widetilde t \in \left( \overline { { t } } , T \right)$ such that ${ \dot { \bf { \mu } } } _ { l } ( { \tilde { t } } ) = 0$

Proof of Proposition 5

Under the linear demand dynamics, a myopic seller chooses optimal $p ( t )$ and m(t) simultaneously to optimize the instantaneous profit rate in the following objective function:

$$
\begin{array}{c} p (t) (\alpha + (\gamma + \beta m (t)) z (t)) (N - z (t) - \theta p (t)) \\ - m (t) (\gamma + \beta m (t)) z (t) (N - z (t) - \theta p (t)). \end{array}\tag{35}
$$

First order conditions with respect to $p ( t )$ and $m ( t )$ yield:

$$
\left\{ \begin{array}{c} N - z (t) + \frac {m (t) (\gamma + \beta m (t)) z (t)}{\alpha + (\gamma + \beta m (t)) z (t)} = 2 \theta p (t) \\ m (t) = \frac {p (t)}{2} - \frac {\gamma}{2 \beta} \end{array} \right.\tag{36}
$$

We have $\begin{array} { r } { \dot { m } ( t ) = \frac { \dot { p } ( t ) } { 2 } } \end{array}$

Similarly, under the nonlinear demand dynamics, a myopic seller chooses optimal $p ( t )$ and $m ( t )$ simultaneously to optimize the following instantaneous pro<sup>fi</sup>t rate:

$$
\begin{array}{c} p (t) e ^ {- s p (t)} [ \alpha + (\gamma + \beta m (t)) z (t) ] (N - z (t)) \\ - m (t) e ^ {- s p (t)} (\gamma + \beta m (t)) z (t) (N - z (t)). \end{array}\tag{37}
$$

First order conditions with respect to $p ( t )$ and $m ( t )$ yield:

$$
\left\{ \begin{array}{l} p (t) = \frac {1}{s} \left[ 1 - \frac {\sqrt {\beta^ {2} z (t) ^ {2} + 4 \alpha s ^ {2} (\alpha + \gamma z (t))} - 2 \alpha s - \gamma s z (t)}{\beta z (t)} \right] \\ m (t) = \frac {p (t)}{2} - \frac {\gamma}{2 \beta} \\ \text { Hence, we have } \dot {m} (t) = \frac {\dot {p} (t)}{2}. \end{array} \right.\tag{38}
$$

Proof of Proposition 6

De<sup>fi</sup>ne the current value Hamiltonian of the optimization problem $( \operatorname { E q } . 6 )$ as

$$
H = (p + \phi_ {n}) e ^ {- s p} [ \alpha + (\gamma + \beta m) z ] (N - z) - m e ^ {- s p} (\gamma + \beta m) z (N - z).\tag{39}
$$

The system dynamics is determined by the following two differential equations:

$$
\dot {\phi} _ {n} = - e ^ {- s p} [ (N - 2 z) (\gamma + \beta m) (p + \phi_ {n} - m) - \alpha (p + \phi_ {n}) ]\tag{40}
$$

$$
\dot {z} = e ^ {- s p} (N - z) [ \alpha + (\gamma + \beta m) z ]\tag{41}
$$

The necessary conditions for optimal price and referral are given by

$$
\left\{ \begin{array}{l} p (t) = \frac {1}{s} - \phi_ {n} - \frac {2 \alpha}{\beta z} - \frac {\gamma}{\beta} + \frac {\sqrt {\beta^ {2} z ^ {2} + 4 \alpha s ^ {2} (\alpha + \gamma z)}}{s \beta z} \\ m (t) = \frac {p + \phi_ {n}}{2} - \frac {\gamma}{2 \beta} \end{array} \right..\tag{42}
$$

Differentiating $p ( t )$ and $m ( t )$ with respect to t, we have

$$
\left\{ \begin{array}{l} \dot {p} (t) = - \dot {\phi} _ {n} + \frac {2 \alpha}{\beta z ^ {2}} \left(1 - \frac {s \gamma z + 2 s \alpha}{\sqrt {\beta^ {2} z ^ {2} + 4 \alpha s ^ {2} (\alpha + \gamma z)}}\right) \dot {z} \\ \dot {m} (t) = \frac {\dot {p}}{2} + \frac {\dot {\phi} _ {n}}{2} = \frac {\alpha}{\beta z ^ {2}} \left(1 - \frac {s \gamma z + 2 s \alpha}{\sqrt {\beta^ {2} z ^ {2} + 4 \alpha s ^ {2} (\alpha + \gamma z)}}\right) \dot {z} \end{array} \right.\tag{43}
$$

Substituting p(t) into the expression of m(t) in Eq. (42) we have

$$
m (t) = \frac {\beta z - 2 s \alpha - 2 s \gamma z + \sqrt {\beta^ {2} z ^ {2} + 4 \alpha s ^ {2} (\alpha + \gamma z)}}{2 s \beta z}.\tag{44}
$$

Based on Eq. (4), the constraint $m ( t ) { > } 0$ requires that β N sγ. If $\beta { \leq } s \gamma ,$ then $m = 0$ . We can further verify that, when $\beta { > } s \gamma ,$ the coef<sup>fi</sup>- cient before ż is positive. Therefore, $\dot { m } ( t ) { > } 0$

Substituting Eq. (44) into Eq. (40) and rearrange terms we have

$$
\dot {\phi} _ {n} = - e ^ {- s p} \left[ (N - 2 z) \frac {\beta^ {2} (p + \phi_ {n}) ^ {2} + \gamma^ {2}}{4 \beta} + (p + \phi_ {n}) \left(\frac {(N - 2 z) \gamma}{2} - \alpha\right) \right].\tag{45}
$$

Based on Eq. (42) we have $\begin{array} { r } { p ^ { * } + \Phi _ { n } = 2 m ^ { * } + \frac { \gamma } { \beta } . } \end{array}$ Substituting Eq. (4) into the expression, together with the condition βNsγ we can verify that $p + \phi _ { n } { > } 0$ . From Eq. (45) we see that $\scriptstyle \phi _ { n } < 0$ when $p + \phi _ { n } { > } 0$ and $\begin{array} { r } { z ( t ) { \le } \frac { N } { 2 } - \frac { \alpha } { \gamma } . } \end{array}$ . Since the term $\begin{array} { r } { \frac { 2 \alpha } { \beta z ^ { 2 } } \left( 1 - \frac { s \gamma z + 2 s \alpha } { \sqrt { \beta ^ { 2 } z ^ { 2 } + 4 \alpha s ^ { 2 } ( \alpha + \gamma z ) } } \right) \dot { z } \geq 0 } \end{array}$ , we conclude from Eq. (43) that the optimal price $\dot { p } ( t ) { > } 0$

## References

[1] F.M. Bass, A new-product growth model for consumer durables, Management Science 15 (1) (1969) 215–227.

[2] E. Biyalogorsky, E. Gerstner, B. Libai, Customer referral management: optimal reward programs, Marketing Science 20 (1) (2001) 82–95

[3] F.A. Buttle, Word of mouth: understanding and managing referral marketing, Journal of Strategic Marketing 6 (1998) 241–254.

[4] K.W. Chiang, Z. Guo, Leveraging the digital network for incentive-based product diffusion, Working paper, 2010.

[5] A. De Bruyn, G.L. Lilien, A multi-stage model of word-of-mouth in<sup>fl</sup>uence through viral marketing, International Journal of Research in Marketing 25 (3) (2008) 151–163.

[6] J. Dean, Pricing pioneering products, Journal of Industrial Economics 17 (1969) 165–179.

[7] R.J. Dolan, A.P. Jeuland, Experience curves and dynamic demand models: implications for optimal pricing strategies, Journal of Marketing 45 (1981) 52–62.

[8] J. Eliashberg, A. Jeuland, The impact of competitive entry in a developing market upon dynamic pricing strategies, Marketing Science 5 (1986) 20–36.

[9] J. Eliashberg, R. Steinberg, Marketing–production decisions in an industrial channel of distribution, Management Science 33 (1987) 981–1000.

[10] S. Helm, Viral marketing: establishing customer relationships by ‘word of mouse’, Electronic Markets 10 (3) (2000) 158–161.

[11] Y.H. Huang, S.C.T. Chou, G.H. Tzeng, Knowledge management adoption and assessment for SMEs by a novel MCDM approach, Decision Support Systems 51 (2) (2011) 270–291.

[12] S. Kalish, Monopolist pricing with dynamic demand and production cost, Marketing Science 2 (2) (1983) 135–159.

[13] E. Kelly, This is one virus that you want to spread, Fortune (2000) 297–300

[14] C. Kiss, M. Bichler, Identi<sup>fi</sup>cation of in<sup>fl</sup>uencers — measuring in<sup>fl</sup>uence in customer networks, Decision Support Systems 46 (1) (2008) 233–253.

[15] L. Kuandykov, M. Sokolov, Impact of social neighborhood on diffusion of innovation S-curve, Decision Support Systems 48 (4) (2010) 531–535.

[16] M. Law, Customer referral management: the implications of social networks, The Service Industries Journal 28 (5) (2008) 669–683

[17] V. Mahajan, R.A. Peterson, Models for Innovation Diffusion, Sage Publications, Beverly Hills, 1985

[18] T.W. McGuire, R. Staelin, An industry equilibrium analysis of downstream vertical integration, Marketing Science 2 (2) (1983) 161–191.

[19] D. Pekelman, Simultaneous price–production decisions, Operations Research 22 (4) (1974) 788–794.

[20] B. Robinson, C. Lakhani, Dynamic price models for new-product planning, Management Science 21 (10) (1975) 1113–1122.

[21] S.P. Sethi, G.L. Thompson, Optimal Control Theory: Applications to Management Science and Economics, Springer, New York, NY, 2000.

[22] R. Van der Lans, G. van Bruggen, J. Eliashberg, B. Wierenga, A viral branching model for predicting the spread of electronic word of mouth, Marketing Science 29 (2) (2010) 348–365.

[23] D.J. Watts, J. Peretti, Viral marketing for the real world, Harvard Business Review 85 (2007) 22–23.

[24] R.A. Westbrook, Product/consumption-based affective responses and postpurchase processes, Journal of Marketing Research 24 (3) (1987) 258–270.

[25] M.A. Zaffar, R.M. Kumar, K. Zhao, Diffusion dynamics of open source software: an agent-based computational economics approach, Decision Support Systems Research 51 (3) (2011) 597–608.

Zhiling Guo is an Assistant Professor in Information Systems at City University of Hong Kong. She received her Ph.D. in Management Science and Information Systems from The University of Texas at Austin in 2005. Dr. Guo's general research interests are in economics of information systems, IS-OM interface, and IS-marketing interface. Her current research focuses on market mechanism design, supply chain information sharing, and e-commerce channel strategies. Dr. Guo's papers have been published or accepted for publication in journals including Management Science, Information Systems Research, Decision Support Systems, Journal of Management Information Systems, Journal of the Association for Information Systems and European Journal of Operational Research.
