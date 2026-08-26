---
otero_id: 6096
otero_key: "85FXB7GY"
title: "Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction"
authors: "Jie Liu; Rui Dai; Xueqi (David) Wei; Yongbing Li"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.06.018"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction

Jie Liu <sup>a</sup>, Rui Dai <sup>a,</sup>⁎, Xueqi (David) Wei <sup>a</sup>, Yongbing Li <sup>b</sup>

<sup>a</sup> Department of IM & IS, School of Management, Fudan University, 200433, Shanghai, China

<sup>b</sup> Department of Industrial Economics, School of Management, Fudan University, 200433, Shanghai, China

## a r t i c l e i n f o

Article history: Received 9 April 2015 Received in revised form 1 May 2016 Accepted 24 June 2016 Available online xxxx

Keywords: Name-your-own-price NYOP Information revelation Haggling willingness Customer segmentation Decision-making process

## a b s t r a c t

Information revelation has become increasingly popular among name-your-own-price (NYOP) providers as a strategy to influence buyers' behavior and facilitate the transaction success rate in industrial practice. However, the mechanism underlying how disclosed information affects a bidder's decision-making process, as well as the consequent bidding results, remains unknown. In this study, we adopted an adapted dynamic choice model to simulate the bidders' decision process, which led to our proposal of a novel mechanism to explain how speci c price information affects bidders' willingness to pay, expectation on threshold price and haggling willingness. The relationship model was then tested using real transaction data from the Shanghai Steel Transaction Center, one of the biggest steel spot transaction platforms in China that employs the NYOP pricing system. Our empirical results showed that a bidder's haggling behavior can be influenced by both personal transaction experience and revealed environmental information; therefore, sellers who intend to hinder haggling behavior can choose to reveal list price information that is more consistent with their bidders' internal reference price. Interestingly, we also found that haggling behavior may not always be harmful because it can enhance the bidders' net utility under certain conditions. Analysis of the combined effects on customer behavior—when more than one kind of relevant price information is disclosed—showed that additional market condition information (i.e., market price fluctuation) has a moderating effect on how current revealed list price information influences a bidder's decision. Thus, by very slightly increasing threshold price, sellers can facilitate haggling in order to increase customer utility in a volatile market. In summary, our study investigated an approach to understand a customer's behavior under different price information environments in the NYOP context. The results indicate that platform providers can implement various information revelation strategies to facilitate dynamic adjustment in the threshold price by sellers to maximize their profits.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Name-your-own-price (NYOP) has become an increasingly popular strategy in industrial practice and as a topic of academic research since it was first introduced by priceline. In NYOP bidding participants are allowed to provide their own quotes for prices of various products. The eventual transaction is made at the quoted price, if it is not lower than the secret threshold price set by the sellers. Otherwise, the transaction is either terminated (as in the single-bid model) or the bidder is asked to provide another quote (as in the repeat-bidding model). NYOP has been well adopted throughout many industries, including online travel and software retail, as well as for B2B transactions. Customers have responded positively to the opportunity for negotiating a price, while sellers have been attracted by the flexibility of setting a threshold price that can be dynamically adjusted according to current market conditions. However, the various bidding experiences and heterogeneous customer types mean that participants might respond significantly different to NYOP.

Scholars and practitioners have sought to understand customer behaviors in NYOP, following various approaches. Some of the earliest studies investigated the influence of customers' individual-specific factors, such as bidding experience and socio-demographic variables [11] or emotional factors [5]. As customers become more strategic and informed, however, the NYOP bidding settings evolved into the more complex forms in practice currently. One direct approach used by sellers to affect participants' bidding behavior involves modifying transaction processes and rules, such as the amount of quotes allowed [8,31], the frequency at which the threshold price changes [7] and whether the adaptive threshold price policy is permitted [14]. Although process adjustment is sometimes effective, it may also lead to negative publicity.

Amazon's dynamic pricing strategy, which uses buyers' profiles to charge different prices, is a widely criticized example, and the company had to invest huge effort to earn back its reputation [1].

Information revelation is an alternative that has been applied to influence NYOP market results. Priceline.com uses this approach, disclosing to customers the current median retail price as a reference. Other sellers have chosen to reveal their products' list price, while still others have published the bidding procedures and rules that were previously opaque to buyers. Compared to directly altering transaction processes and rules, the effect of information revelation is more complex. Whether and how specific information revelation affects a customer's decision and contributes to better bidding outcome is vital, but remains under-researched. Therefore, we provide here an approach to demonstrate how NYOP customers respond to different revealed price information.

Prior research has discussed disclosed information specific to the product [32], the price [37] and the bidding mechanism [10,14,34]. Although some important conclusions have been drawn from the final bidding results related to specific disclosed information, the decision processes of bidders facing distinct bidding environments have not been studied in depth.

With the aim of obtaining real transaction data that reflects participants' bidding decisions—and the effects of information revelation—we utilized the Shanghai Steel Transaction Center (shgt.com), which is recognized as one of the top Chinese steel spot transaction platforms. In its first year, shgt.com had a trading volume of more than three million tons; since then, about twenty thousand buyers have registered in the platform. Most of the buyers identify as self-employed steel traders or small metal-processing companies.

The shgt.com platform allows for implementation of various pricing schemes, including posted price channel and NYOP. In its NYOP setting, customers are allowed to quote three times, at most, in one bargaining. The list price is always disclosed to buyers, representing a major difference from traditional NYOP settings. Moreover, additional information concerning the congeneric products' average transaction price history is also revealed in the platform; this latter strategy was implemented at about half a year after the platform's launch. The transaction price history shows bidders how the average price of congeneric products fluctuates recently (Fig. 1).

In this study we applied an adapted dynamic choice model proposed by [6,8,11,14,31] to simulate participants' decision process. Previous studies have demonstrated frictional cost as the key element in determining customers' haggling behavior (i.e., whether and how to increase quotes with the notification of whether the prior quote is accepted). Rational bidders facing positive frictional cost are expected to increase quotes at a decreasing rate. However, in NYOP practice, irrational behaviors following increasing or constant increment patterns abound [18,32]; unfortunately, this phenomenon cannot be explained by the existing frictional cost framework. This gap between theory and practice results from the fact that the frictional cost model considers frictional cost as the only factor affecting customers' haggling behavior. In line with the results from [15,16] that demonstrated that information revealed by sellers also affects bidders' behavior, we hypothesized that bidders' haggling willingness is affected by both frictional cost and extra information utility. Our investigations reveal that customer information utility is largely influenced by information revealed by NYOP sellers; in particular, bidders with the same frictional cost show different haggling patterns in distinct information environments. Furthermore, we examined the current revealed list price and the customer internal reference information as direct factors affecting customers' haggling willingness and final bidding results. Our results validated the moderating effect of price fluctuation shown by extra-disclosed price history information.

Since all these types of information are available to NYOP sellers, the findings from this study provide these sellers with a better understanding about and prediction ability for participants' bidding behavior, which will allow them to more appropriately set threshold price and facilitate the disclosure of price information that will maximize profits. Transaction platforms may also benefit as these findings can help guide design of the information disclosure mechanism that will facilitate the transaction success rate and bidder's utility.

The remainder of this paper is organized as follows. In Section 2, we review the related literature on the NYOP decision-making process and haggling behavior and on the effect of information revelation. Section 3 then builds up a research model and puts forward research questions for future study. Section 4 sets up the relationship model concerning bidders' decisions and revealed information. In Section 5, we present the data and methodology. Section 6 explains the empirical results and Section 7 closes with a discussion of our conclusions and the implications for the future of the field.

## 2. Literature review

## 2.1. Decision process and bidding behavior in NYOP

Prior research has examined customers' bidding behavior in several NYOP settings. Hann and Terwiesch [11]) were the first to introduce the concept of frictional cost, which they define as the disutility a customer faces when asking for an extra quote in an NYOP auction. Using a dynamic choice model, the authors demonstrated how rational bidders

![](/api/attachments/85FXB7GY/fulltext/images/a4c6a66b7ef284a733b0884933177eaaee179c9084c2ba474085eecec30ed496.jpg)  
Fig. 1. Information revelation use of congeneric products' average price history.

Please cite this article as: J. Liu, et al., Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.018

would quote with the aim of maximizing their expected net utility. Whether customers' bidding experience and socio-demographic variables are related to frictional cost was also examined. Following this research by Hann and Terwiesch, Spann et al. [31] compared the bidding behavior and profit implications of the single-bid model with those of the repeated bidding model. Furthermore, Ding et al. [5] argued that customers not only aim to maximize their economic surplus, but also have an expected excitement of winning and frustration at losing a bid. The authors confirm that customers' bidding behavior is affected by their previous bidding results.

According to the frictional cost model, theoretically, rational bidders should always employ a strictly decreasing bid increment strategy because in later quotes bidders must increase bids at a slower pace to balance the continuously increasing frictional cost. The rigorous proof and mathematical relationship between consecutive quotes are presented in Appendix A of [14]. However, this is counterfactual because the concave bidding pattern has been shown to account for only a small percentage of NYOP practice in the real world [18,32]. The disconnect between theory and practice may be explained by the fact that the previous studies have considered frictional cost as the sole factor affecting customers' haggling behavior, while other environmental factors with potential to influence utility have been largely, if not completely, ignored.

## 2.2. Haggling motivation in online auction and NYOP

Haggling behavior exists in many NYOP settings that permit repeat quoting. Consistent with Hann and Terwiesch [11], Terwiesch et al. [33] also considered frictional cost as the only factor influencing haggling behavior. Furthermore, Joo et al. [18] found that hagglers who employ a constant bid increment strategy and a decreasing bid increment (i.e., concave) strategy save more, while those who employ an increasing bid increment strategy (i.e., convex) fare no better. Therefore, hagglers trade off between the potential economic utility and frictional cost, both of which result from extra haggling.

In game theory, players haggle in response to and to overcome their lack of information. Through the haggling process, players are able learn their opponent's valuation, which then helps them to make a better decision and acquire a higher expected payoff [21]. Besides the economic utility of extra information that originates from haggling, the noneconomic benefit has also been addressed in the literature. According to Westbrook and Black [35], negotiation itself can be motivating for customers, whereby acquiring products through the haggling process becomes more appealing. This phenomenon can be attributed to customers' “smart-shopping feelings” [29] related to gaining a discount through a haggling endeavor and helps to avoid the feeling of regret that would otherwise manifest after finding out that bargaining opportunities existed for transacting at a lower price [23]. The haggling process provides customers with a feeling of achievement [17], particularly that they obtained a better price through their practice of haggling. However, the noneconomic utility that the haggling process presents to bidders has been addressed rarely in the NYOP literature.

## 2.3. Role of revealed information in NYOP

Previous research findings have emphasized the role that disclosed information plays in the NYOP mechanism. Hann et al. and Hinz et al. [10,14] showed that the revelation of adaptive threshold policy improves seller's profit as well as customer's utility and satisfaction, and Fay and Laran [7] attributed the difference of the bidding's monotonicity to price threshold variability. Wang et al. [34] examined how customers would perform in the presence of an upper-bound (UB), lower-bound (LB) or at the interval of threshold price respectively when the customer is able to choose between NYOP and a list price channel.

Other papers have reported on the influence of price information, which is the most important indicator for buyers to valuate products and threshold price. Wolk and Spann [37] examined the singlebidding scenario, using the adaptation level theory to test how the bid value would be affected by various reference prices [13]. According to adaptation level theory, the decision-maker generates their adaptation level based on the past stimuli and judges the effectiveness of a new stimulus according to that adaptation level. The conclusions reported by Helson [13] were also shown as valid for B2B purchasing environments. In particular, Bruno et al. [3] showed that the way in which customers react to a current price is dependent upon the previous prices they have paid. Moreover, Bruno et al. [3] confirmed that B2B customers adjust their decisions according to their transaction-specific perception of how good the price is by comparing it with their internal reference prices (IRPs). IRP is individual-specific and often constructed based upon a customer's previous purchasing history [12,20].

## 3. Model development and research questions

Joo et al. [18] showed that hagglers can save more by employing a constant or decreasing bid increment. However, our search of the literature has found no prior research that explored what kinds of bidders adopt such strategies. In the current study, we employed a dynamic choice model [6,8,11,14,31] to investigate how environmental information factors affect the bidders' decision-making process, and thus their bidding behavior.

Although business metrics are widely used throughout the literature describing studies of the B2B transaction, we still chose to adopt a utility model to capture the major characteristics of customer decision processes and behavior patterns. According to Zhang et al. and Wilson [36,39], the main differences between the B2B transaction and the business-to-consumer (B2C) transaction lie in three aspects. First, B2B transactions are always characterized with higher variable cost of goods and variable order size. Second, the decision process in the B2B environment is affected by the existing long-term relationship [19,24] between major buyers and providers. Third, because B2B purchasing agents are usually professionally trained and B2B transactions happen repeatedly, business customers typically make inter-related decisions. The first two characteristics do not fit within our current research environment, since they only allow for small sized spot transactions. Besides, the majority of participants in our research environment are self-employed steel traders, most of which only have a couple of employees and trade between several channels. The long-term relationship, then, barely exists between buyers and sellers in the transactionfocused spot market and thus has no impact on our model setting. Finally, in our research environment the inter-related decisions are depicted by our reference price demonstration. In fact, Bruno et al. [3] have already successfully used the utility model to explain reference price effects in the B2B environment. The utility model is also the most popular used pricing strategy for application service providers, who in most cases sign short-term, standard contracts with many small- and medium-sized enterprises [27].

Consider a B2B NYOP platform in which a list price LP is always revealed and a bidder is allowed to quote at most three rounds for a product. Fig. 2 illustrates how a bidder will interact with the system under such a setting. After logging in to the platform (entering a user ID and password), a bidder can suggest a price for one of the featured products on the basis of a seller-revealed posted price or to transact directly on the list price. If the bidder then chooses to suggest a quote that is lower than the list price, the quote is automatically compared with the threshold price TP; the bidder is then immediately notified whether or not the offer was successful (i.e., the quote is above or equal to the threshold price). A bidder who fails the first bid is allowed to increase their offer by submitting a second (then third) offer. Except for the successful bidding case, this haggling behavior ends either with the bidders' three quote opportunities being used up or with the bidder deciding to no longer increase their offer, thereby terminating the haggling process.

![](/api/attachments/85FXB7GY/fulltext/images/a7e1ae640d9ed3b1687bdb6a8e8773eaeaeb2707bcecdedbcb74cbfacef79092.jpg)  
Fig. 2. Customer interaction with the platform under the focal NYOP setting.

Following Hann and Terwiesch, Ding et al., and Fay [5,6,11], we assumed that the expectation of threshold price is uniformly distributed among intervals [denoted by ‘LB’ and ‘UB’]. The bidder's willingness to pay is denoted by ‘WTP’. The customer first places a bid [denoted by ‘QUOTE1’]. If QUOTE1 is not less than the threshold price, the transaction is concluded at price QUOTE1. Otherwise, the quote is rejected automatically by the system and the customer is asked to try another quote until all three chances [denoted by ‘QUOTE ’, where i = 1, 2, 3] are used or the customer terminates the process. TP remains unchanged during the three bids and it should be lower than the posted price LP.

Following Hinz et al. [14], we used an expected net utility maximization model to simulate the offers that rational bidders would make. The bidder's expected net utility [ENU] was then calculated ${ \mathsf { a s \ delta } } ^ { \mathrm { t - 1 } } ( \mathsf { W T P \mathrm { ~ - ~ } }$ QUOTE<sub>t</sub>), where t = 1, 2, 3. Here, δ represented how a bidder valued the utility of winning a bid at the same price between two consecutive quotes. Bidders with higher δ can gain higher net utility from the later transaction, making them relatively more willing to haggle. If QUOTE<sub>t</sub> b TP (t = 1, 2, 3), the bidder's net utility is zero.

Previous research has attributed the variance of δ to the diversity of frictional cost that customers face when given an extra quote opportunity. This diversity may originate from distinct social background, financial status, etc. As demonstrated in Fig. $3 , \mathrm { Q U O T E _ { 1 } } + \mathrm { Q U O T E _ { 3 } } < 2 \mathrm { Q U O T E _ { 2 } }$ always holds true if, and only if, δ b 1. We can thus infer that a bidder facing a positive frictional cost (δ b 1) will theoretically always follow a concave bidding pattern. The conclusion also applies in bidding scenarios permitting n quotes at most; since $2 0 \mathrm { U O T E } _ { j } = 0 \mathrm { U O T E } _ { j } - \mathrm { _ { 1 } } + \delta \mathrm { Q U O T E } _ { j + 1 } + ( 1 -$ δ)WTP [14], the $2 \mathrm { Q U O T E } _ { j } - \mathrm { Q U O T E } _ { j } - \mathrm { _ { 1 } \dot { - } Q U O T E } _ { j } + _ { 1 }$ equals to (1 − $\delta ) ( \mathsf { W I P } - \mathsf { Q U O T E } _ { j \mathrm { ~ + ~ } 1 } )$ , in which the direction is determined by the value of δ.

However, the rational concave bidding pattern only accounts for a small percentage in NYOP practice [18,32]. This gap between theory and practice is caused by the limitation of the discount factor δ. Only the situation that δ b 1 was tested [7,11] because they just take one influencing factor i.e., frictional cost into consideration. However, the noneconomic utility of extra information brought about by extra quotes was nearly ignored.

The objective of bargaining lies in learning the opponent's value through the information discovery process [21]. In NYOP settings, bidders haggle to learn more information about the threshold price. As pointed out by Hann and Terwiesch [11], rejected offers can be regarded as valuable information that serves to reduce the seller's information rent. Although the economic utility has been considered in the form of expected lower transaction price, the benefit that extra haggling brings about extends beyond economic. The neglected noneconomic benefit includes the excitement of being a smart-shopper [29]. Compared to concluding a transaction at the first quote, some bidders prefer haggling more because it makes them feel they have taken the most use of the opportunities to get as low a transaction price as possible. Successful transactions obtained through a tough haggling process impress upon the bidders the idea that they are equipped with sophisticated bargaining skills [17] and not being taken advantage of

![](/api/attachments/85FXB7GY/fulltext/images/a462fb92c04598d82eb2792d24aa110c35343eb8f391e58f642db4d3f39f33b5.jpg)  
Fig. 3. Haggling process of a rational NYOP bidder.

Please cite this article as: J. Liu, et al., Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.018

J. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/85FXB7GY/fulltext/images/b88117ac68628d17db21169978da02e44bbf29ccf82bdcaaf71802fe264c589e.jpg)  
Fig. 4. Factors influencing the bidder's haggling willingness coefficient.

by the providers. As Sherry [28] once stated: “dickering is linked to feelings of competence and mastery.”

Therefore, we argue that δ is affected by both noneconomic utility of extra information as well as frictional cost, as demonstrated in Fig. 4. Here, we introduce the concept that the haggling willingness coefficient (δ) can act as an extension of the discount factor, following the fact that haggling willingness is determined by both the factors cited above. Therefore, in our study, δ was allowed to serve as an “inflator” of utility rather than merely a “deflator” as it has been in prior studies in the literature. In addition, in order to maintain consistency with the prior research, we also treated δ as a multiplicative term of the bidder's utility function. To the best of our knowledge, all prior research has focused on the frictional cost aspect, while the factors that influence bidder's haggling utility are under-researched. A more clear and comprehensive understanding of how haggling willingness is determined will help us to better predict bidding behavior.

Since bidders haggle for both economic and noneconomic utility related to lack of information [21], it is reasonable to infer that a bidder's decision information acquired from the providers' disclosure will play a major role in how the haggling willingness is influenced. Therefore, we launched our research by investigating how the haggling willingness coefficient is affected by environmental information revealed by sellers. Two scenarios with different information revelation were considered, including one with only real-time list price revealed to customers (denoted by Scenario 1) and the other with the extra product average transaction price history also being disclosed (denoted by Scenario 2, as shown in Fig. 1). Additionally, we also subdivided the customers into different types according to how they valuated specific products, opportunity cost of time, and attitude towards risk. Distinct customer types are supposed to behave differently in regards to their haggling willingness and thus the final bidding outcome. The following key research questions were addressed by this study:

1. How does the real-time list price information revealed by NYOP sellers affect a bidder's haggling willingness coefficient and thus their bidding behavior?

2. How does the extra price transaction history information revealed by NYOP sellers affect a bidder's haggling willingness coefficient and thus their bidding behavior?

3. How does customer type affect a bidder's haggling willingness and thus their bidding behavior?

## 4. Impact of information revelation on bidding behavior

## 4.1. Impact of current list price on customer haggling behavior

Since lacking information about threshold price is a major factor underlying bidder haggling, we can infer that bidders are more willing to haggle when the information they have to predict threshold price is less effective or when the threshold interval is harder to estimate. Otherwise, if the information available to the customer is reliable enough to make good decisions, they will care more about the frictional cost aspect rather than the information utility aspect of haggling.

In Scenario 1, bidders make judgment using the current list price information and their own transaction experience. According to adaptation level theory [13], customers will generate their own adaptation level (i.e., internal reference prices from previous transaction history). The internal reference price is an individual-specific indicator, which plays a major role on purchasing decisions and is often constructed based upon the customer's observed prices on previous purchase occasions [12]. When customers participate in a new purchasing opportunity, they will face new stimuli (i.e., current list price). The new stimuli will be perceived as effective and assimilated only if it is already close to the adaptation level [13]. This aspect also applies to the B2B environment. Bruno et al. [3] showed that the way in which customers react to current price is dependent upon previous prices they have paid; ultimately, the authors confirmed that B2B customers adjust their decisions according to their transaction-specific perception of how good the price is by comparing it with their internal reference prices.

Specifically, bidders will choose whether to assimilate the list price (new stimuli) according to their internal reference prices (adaptation level). If the real-time list price is close to the bidder's internal reference price, it will be more likely for the bidders to deem the current information as useful and effective. Since the value of information lies in its capacity to reduce uncertainty, bidders under such a certain circumstance will have little incentive to haggle for more information since haggling itself is costly. Otherwise, a giant deviation between the internal reference price and external reference price (real-time list price) will motivate bidders to haggle more.

## 4.2. Impact of customer type on haggling behavior

Different customers have distinct features, such as the time cost of the opportunity and the bidder's risk attitudes towards losing a bid. Customer differentiation is a common and effective approach to studying customer characteristics and making corresponding strategies. We subdivide NYOP customers from three dimensions i.e., how they valuate specific products, opportunity cost and attitude towards risk, based on which we define customer type as a class of customers with the same prior [9]. The higher type represents the higher valuation put on specific product categories, the higher opportunity cost of time and the characteristic of being more averse to risk.

There exist some connections between customer type and frictional cost. Frictional cost is one concrete measurement concerning specific aspects of customer type in the form of haggling disutility. However, customer type in our classification is also concerned with a customer's valuation of a specific product, providing an extra explanation of the customer's distinct willingness to pay and expectation for the threshold price. Besides, since detailed individual-specific information, such as socio-demographic backgrounds and financial status [11], is not easy to acquire in some circumstances (e.g. B2B purchasing and some B2C bidding environments with rigorous privacy protection), it is difficult for sellers to use this kind of information as reference for how bidders will behave. Higher type bidders that incur more frictional costs are less likely to haggle, while lower type bidders typically care more for moneysaving than time cost and risk of scoop, resulting in higher haggling willingness.

## 4.3. Impact on customer's willingness to pay

Customer's willingness to pay is the customer's real-time valuation of a specific product, which is both individual-specific and environmentrelated in our research settings.

List price represents the product's market price that is determined by the entire market equilibrium. Since customers can easily resell the product under such a list price, it affects the product's profit margin to a large extent. The higher the list price is, the more profit that customers can make given the same purchasing price. B2B customers always have higher willingness to pay on products with higher list price.

Individual-specific factors may also affect a customer's WTP. Customers may value a product with the same list price differently. A higher type customer who is prone to valuing a specific product higher and to suffering greater opportunity cost has higher WTP.

## 4.4. Impact on customer's expectation about the LB of threshold price

Another bidding related variable that affects the bidding result is customers' expectation of the LB of threshold price. Although prior literature rarely discusses what factors affect the LBs, we can easily infer that list price is a major contributor as it sets an important baseline of lowest possible price that bidders can bargain over. The higher the list price is, the higher the product's market value and popularity. As a consequence, products with higher list price have a higher lowest possible threshold price.

In addition, different customers might have different LB expectations when facing the same list price. The higher type customer is more risk averse and thus will be more conservative and discreet in their prediction of the lowest possible threshold price, thereby contributing to a higher expectation of the LB of threshold price.

## 4.5. Impact of transaction price history on customer decision making

In Scenario 2, the recent 6-days' daily average transaction prices of congeneric products are disclosed to NYOP bidders. The additional information will give insight to customers on the entire market's transaction performance, which may affect a bidder's judgment about the usefulness of reference prices. When the transaction history shows a greater degree of price fluctuation, it is more likely that bidders will believe that their own transaction history and list price information are unreliable and useless for the current decision making. As a result, the bidder will be less likely to use them as the effective references. In other words, additional price fluctuation information moderates the effects of existing information on both the haggling willingness coefficient and a bidder's expectation of the LB of threshold price. Meanwhile, since the list price always represents the market price, regardless of whether it is fluctuating wildly, the willingness to pay by a specific customer under the same list price will remain stable.

Specifically, as bidders believe that the consistency of reference prices is less useful in the presence of bigger price fluctuation while the main effect of reference prices' consistency on haggling willingness is negative, we argue that the main effect will be positively moderated by price fluctuation. Similarly, the effect of list price on bidder's expectation of the LB of threshold price is negatively moderated by the price fluctuation.

## 4.6. Covariates

As Bruno et al. [3] point out, B2B customers are firms that have their own customers, whose preferences most likely result from the preference-dependent behavior of the industrial buyers. Since our dataset covers a relatively long period of time, we decided to take the change of the entire downstream value chain's preference into consideration. Under different market preferences, the same customer might behave totally differently. Therefore, we chose to include the domestic steel spot market quotation—directly determined by the downstream value chain's preference—as the control in our model to ensure that change in customers' behavior due to the entire market preference change was efficiently considered.

The whole relationship model encompassing the NYOP bidders' decision-making factors and the related revealed information is illustrated in Fig. 5.

In Scenario 1, the system of models examined is as follows.

$$
\begin{array}{l} \delta = a 0 + a 1 * R e f \_ C o n s i s t e n c y + a 2 * C u s t o m e r \_ T y p e + a 3 \\ \quad * M k t \_ Q u o t a t i o n + e 1 \dots \dots . \end{array}\tag{1}
$$

$$
W T P = b 0 + b 1 * L P + b 2 * C u s t o m e r \_ T y p e + b 3 * M k t \_ Q u o t a t i o n + e 2\tag{2}
$$

$$
L B = c 0 + c 1 * L P + c 2 * C u s t o m e r \_ T y p e + c 3 * M k t \_ Q u o t a t i o n + e 3\tag{3}
$$

The moderating effects of market price information are also examined in Scenario 2.

$$
\begin{array}{r l} \delta & = a 4 + a 5 * R e f \_ C o n s i s t e n c y + a 6 * C u s t o m e r \_ T y p e + a 7 * P r i c e \_ F l u c t \\ & * R e f \_ C o n s i s t e n c y + a 8 * M k t \_ Q u o t a t i o n + e 4 \end{array}\tag{4}
$$

$$
\begin{array}{r l} W T P & = b 4 + b 5 * L P + b 6 * C u s t o m e r \_ T y p e + b 7 \\ & * M k t \_ Q u o t a t i o n + e 5 \quad \dots \dots . \end{array}\tag{5}
$$

![](/api/attachments/85FXB7GY/fulltext/images/51c339b4fedb04a075b0414f02e919472f1615f245a297c837701ac9829ed392.jpg)  
Fig. 5. Customer's decision-making factors and relationship in NYOP setting.

Please cite this article as: J. Liu, et al., Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.018

J. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

$$
\begin{array}{l} L B = c 4 + c 5 * L P + c 6 * C u s t o m e r \_ T y p e + c 7 * P r i c e \_ F l u c t * L P + c 8 \\ * M k t \_ Q u o t a t i o n + e 6 \dots \dots . \end{array}\tag{6}
$$

## 5. Data, measurement and methodology

We obtained the transaction data from a large Chinese steel spot transaction platform that allows both NYOP and direct purchasing. The platform first employed the information revelation strategy in Scenario 1 and then changed to that of Scenario 2 at half a year later. After excluding a provider that adopted a fixed threshold price policy over time and observations that had random missing values, we had 5221 observations for Scenario 1 and 1064 observations for Scenario 2. Each observation includes product information, the customer's three quotes, the temporal list price, bidding time and temporal average transaction price history of congeneric products revealed by sellers (in Scenario 2). The complete transaction history of all bidders on this platform is also available.

## 5.1. Measurement

We divided all products into 12 categories according to the platform's classification system. Products of the same category are substitutable to some extent. The metrics of internal reference price and customer type were calculated based upon this classification.

## 5.1.1. Customer type

Since detailed individual information, such as socio-demographic backgrounds and financial status [11], is often unobtainable in today's business environment, we attempted to construct a validation instrument of customer type from the purchasing histories. Generally speaking, the higher customer types who faced the same list price showed a higher possibility of transacting at a lower discount because of their higher valuation of the product, greater time cost and more averse attitude towards risk. In contrast, the lower customer type was more price-sensitive and prone to transact with a higher discount. Therefore, customer's average price discount subtracting out the effect of list price is the good instrument of customer type.

We first calculated the customer's transaction price discount relative to the original list price. We regarded those customers who purchased directly as the highest type, who valued a product so highly or had such huge time cost that they were not even willing to haggle once. A bidder's type for a specific product at some time point equates to his or her own average transaction price premium of the same product category weighted by products' weights. Suppose that at time point t a customer already has n successful transactions in the same product category at prices $\mathrm { P } _ { 1 } , \mathrm { P } _ { 2 } , \ldots .$ Pn respectively; then, the corresponding list price will be $\operatorname { L P } _ { i } ,$ with the weight of each product denoted by $W _ { i } , i = 1 , 2 , . . . . . , n$ . The customer type at time point t is then calculated as follows:

$$
\text { CUSTOMER\_TYPEt } = \sum_ {1} ^ {n} W _ {i} \frac {P _ {i} - L P _ {i}}{L P _ {i}} / \sum_ {1} ^ {n} W _ {i}
$$

## 5.1.2. Internal reference price

Operationally, the internal reference price is often constructed based upon the customer's observed price from previous purchase occasions [12]. Since IRP is constantly updated according to new stimuli, we measured the IRP using the weighted average transaction price in a moving window of three successful NYOP transactions that had occurred prior to the focal auction [26,38]. Suppose at time point t, the recent three successful transactions prices on the same product category for the focal bidder are $\mathrm { P } _ { 1 } , \mathrm { P } _ { 2 }$ and ${ \mathrm { P } } _ { 3 } ,$ and the corresponding weight of each product is denoted by $W _ { i } , i = 1 , 2 , 3$ , then the internal reference price of the focal customer at time point t will be calculated as $\mathrm { I R P } _ { t } =$ $\textstyle \sum _ { 1 } ^ { 3 } W _ { i } P _ { i } / \sum _ { 1 } ^ { 3 } W _ { i } .$

## 5.1.3. Consistency of reference prices

Consistency of reference prices is measured by subtracting the absolute deviation value from the list price related to the customer's internal reference price. The bigger the absolute value is, the less consistency that current list price and internal reference price have.

Ref Consistency LP−IRP

## 5.1.4. Price fluctuation

We measured the degree of market price fluctuation using relative price variability. Relatively, market price variability is calculated using the coefficient of variance of the revealed market prices. The bigger relative variability ${ \mathrm { i } } s ,$ the more fluctuant the bidders will believe the market quotation is.

$$
P r i c e \_ F l u c t = \frac {S t a n d a r d d e v i a t i o n o f r e v e a l e d m a r k e t p r i c e s}{M e a n o f r e v e a l e d m a r k e t p r i c e s}
$$

## 5.1.5. Domestic steel spot market quotation

We used the MySpic index of the domestic steel spot market [25] that is provided by the Shanghai Bulk Commodity Information Center in order to the measure domestic steel spot market quotation. The Shanghai Bulk Commodity Information Center is the biggest thirdparty steel price information provider in China. The price index is compiled according to the daily transaction prices of major online and offline domestic steel spot markets. These prices are weighted by product popularity and transaction volume, as well as steel production from major steel corporations. The index is recognized as a fair indicator and can be used for current steel spot market quotation; the data can be obtained from http://www.mysteel.net/myspic.html.

## 5.2. Methodology

Customers' quotes are determined by three factors, including customer WTP, the expected LB of threshold price, and haggling willingness δ. Specifically,

$$
\begin{array}{c} E N U _ {t} = M A X \{0, M A X _ {Q U O T E t} \{P r o b (Q U O T E _ {t} \geq T P > Q U O T E _ {t - 1} | Q U O T E _ {t - 1} <   T P) \delta^ {t - 1} \\ (W T P - Q U O T E _ {t}) + P r o b (Q U O T E _ {t} <   T P | Q U O T E _ {t - 1} <   T P) E N U _ {t + 1} \} \} \end{array} \dots \dots\tag{7}
$$

Solving the first-order conditions of the above Bellman equations for $t = 1 , 2 , 3 ,$ , we have

$$
Q U O T E _ {1} = \frac {(4 - \delta) L B + (4 - 3 \delta) W T P}{8 - 4 \delta} \quad \dots \dots\tag{8}
$$

$$
Q U O T E _ {2} = \frac {L B + (3 - 2 \delta) W T P}{4 - 2 \delta} \quad \dots \dots\tag{9}
$$

$$
Q U O T E _ {3} = \frac {L B + (7 - 4 \delta) W T P}{8 - 4 \delta} \quad \dots \dots\tag{10}
$$

WTP, LB and δ are latent variables and were not observed in our research setting. In line with Hann and Terwiesch and Spann et al. [11,31], we first solved the following optimization problem to acquire these imputed customer characteristics.

$$
\min _ {W T P, L B, \delta} \sum_ {i = 1} ^ {3} (Q U O T E _ {i} - Q U O T E _ {i} (W T P, L B, \delta)) ^ {2} \quad \dots \dots\tag{11}
$$

Since all bidders are allowed to quote three times at most, the above optimization problem has been reduced to a system of nonlinear equations. The predicted bidding values using imputed customer characteristics completely explain the variance of actual quotes.

J. Liu et al. / Decision Support Systems xxx (2016) xxx–xxx

Table 1  
Descriptive statistics of δ in both scenarios.

<table><tr><td>Scenario</td><td>δ&lt;1</td><td>δ=1</td><td>δ&gt;1</td></tr><tr><td>1</td><td>16.24%</td><td>67.46%</td><td>16.30%</td></tr><tr><td>2</td><td>16.73%</td><td>61.47%</td><td>21.80%</td></tr></table>

## 6. Empirical results

As shown in Table 1, bidders will not always follow the strictly concave bidding pattern inferred from previous theories. A constant increment bidding pattern accounted for the majority in our bidding environments (67.46% in Scenario 1 and 61.47% in Scenario 2). This profile was mainly caused by the practical bidding setting, which provided quick feedback to bidders and encouraged them to bid in multiples of ten. Besides, there existed a considerable amount of increasing increment patterns, the number of which was roughly equal to the δ less than 1 cases. The findings from statistical analysis provided convincing proof of the existence of other factors, besides frictional cost, that affects the bidders' haggling pattern. In addition, the proportion represented by the increasing increment pattern is even higher in Scenario 2, where extra market information was revealed.

The descriptive statistics for customers' bidding behavior, list price information, market quotation and customer characteristics are presented in Table 2. The average platform list price decreased over the period of the entire investigation; the trend can be explained by either the entry of small traders providing cheaper products or the rapid development of the Shanghai Steel Transaction Platform itself. More importantly, when this study was conducted the overall Chinese steel market was still suffering the aftermath of the steel trader crisis that had occurred in 2012. The entry of small traders and the depression of market have reduced the bargaining space and excluded certain low type buyers, in accordance with the fact that customer type has increased substantially in Scenario 2. Besides, the products' list prices deviate greater from customers' adaptation level in Scenario 2 for the same reasons.

We present the regression results for both scenarios in Table 3. The statement that greater reference prices' consistency (as measured by smaller absolute value of |IRP-LP|) leads to lower haggling willingness was supported by the results in both Scenario 1 (a1 = 0.0000165, $p = 0 . 0 4 )$ and Scenario 2 $( \mathsf { a } 5 = 0 . 0 0 0 1 3 2 , p = 0 . 0 0 0 )$ . We also found strong evidence in Scenario 1 (a2 = −1.398, p = 0.000) to support the statement that haggling willingness is negatively affected by customer type. Unfortunately, in Scenario 2 (where additional market price information is revealed) the coefficient of customer type on haggling willingness did not reach the threshold for a statistically significant difference $( \mathbf { a 6 } = - 0 . 0 6 4 1 , p < 0 . 0 5 = 0 . 9 4 1 )$ . The results served to validate our basic model in which haggling willingness was expected to be influenced not only by frictional cost but also by reference prices. More consistency of reference prices could therefore increase reference effectiveness, reducing the relative utility of extra information and decreasing haggling willingness. However, the overall explanatory power on δ was relatively low, as compared to a previous study [11]. This finding likely reflects the bidding design in which customers were encouraged to quote in multiples of ten, possibly deviating from their real optimal quotes.

We also verified in both scenarios that the expected LB of threshold price and willingness to pay were both positively influenced by list price and customer type. The overall explanatory power for LB was extremely high in Scenario 1 $( R ^ { 2 } = 9 6 . 0 4 \% )$ , and the moderating effect even increased $R ^ { 2 }$ to 98.75% in Scenario 2. As to willingness to pay, the $R ^ { 2 }$ of regressions on list price and customer type ranged from 98.83% to 99.67%. These results supported the choice of our measurement of customer type as an efficient metric, which allowed for appropriate classification of NYOP bidders according to their behavior differences. Besides, since information factors influencing willingness to pay and bidder's expectation about lowest threshold price have never been examined empirically in the previous literature, our model has proposed a novel feasible way to explain them.

Next, we extended the model by adding the additional revealed information variables. If the influence of reference price consistency on haggling willingness and the effect of list price on the LB are respectively positively and negatively moderated by the fluctuation of additional market information, we expected coefficients a7 and c7 to both be negative since a smaller absolute value of |LP-IRP| indicates a greater reference prices' consistency. As before, we reached the conclusion that the basic influence of reference prices on LB or haggling willingness was moderated by new information revelation

The basic model and extended model were verified by our empirical study. We used the fitted values to examine the overall prediction power on customer bidding values. Using the fitted value of (WTP, LB, δ) calculated by formula 1–6, we were able to calculate the fitted value of QUOTE (i = 1, 2, 3). Then, we regressed each real quote on the corresponding fitted value. The mean absolute percent error (MAPE) of each model is listed in Table 4.

The MAPE values presented in Table 4 show that our models are valid and represent an accurate prediction of customers' bidding behavior in the focal steel spot platform.

## 7. Discussion

Customer behavior has been extensively studied by NYOP scholars and practitioners, but most of the research has focused on the bidding mechanism and the final results. Here, we provide a new approach and explore the innate link between the customer decision-making process and the environmental price information revealed by NYOP

Descriptive statistics of bidding behavior and customer characteristics.

<table><tr><td>Scenario</td><td>Variable</td><td>Median</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td rowspan="7">1</td><td>δ</td><td>1</td><td>0.9811</td><td>0.258079</td><td>0.037037</td><td>1.5</td></tr><tr><td>WTP</td><td>4006</td><td>4152.228</td><td>740.1525</td><td>2910</td><td>15,300</td></tr><tr><td>LB</td><td>3920</td><td>4071.453</td><td>715.0452</td><td>2550</td><td>14,500</td></tr><tr><td>Customer_Type</td><td>-0.021388</td><td>-0.023146</td><td>0.0117735</td><td>-0.066117</td><td>0</td></tr><tr><td>List_Price</td><td>4100</td><td>4224.889</td><td>760.9738</td><td>3000</td><td>16,500</td></tr><tr><td>Ref_Consistency</td><td>168.85</td><td>279.9678</td><td>443.6471</td><td>0</td><td>2767.89</td></tr><tr><td>Mkt_Quotation</td><td>3671.9</td><td>3711.774</td><td>105.2752</td><td>3577.3</td><td>4011.3</td></tr><tr><td rowspan="8">2</td><td>δ</td><td>1</td><td>0.9963</td><td>0.2736</td><td>0.25</td><td>1.5</td></tr><tr><td>WTP</td><td>3749.5</td><td>3846.824</td><td>570.3635</td><td>2940</td><td>7780</td></tr><tr><td>LB</td><td>3680</td><td>3777.658</td><td>558.1992</td><td>2790</td><td>7700</td></tr><tr><td>Customer_Type</td><td>-0.016847</td><td>-0.017237</td><td>0.0099949</td><td>-0.056922</td><td>0</td></tr><tr><td>List_Price</td><td>3800</td><td>3878.30</td><td>569.63</td><td>2960</td><td>7800</td></tr><tr><td>Ref_Consistency</td><td>224.84</td><td>305.8505</td><td>315.30</td><td>0</td><td>2771.02</td></tr><tr><td>Pri_Fluct</td><td>0.631237</td><td>1.609</td><td>3.11</td><td>0</td><td>19.4485</td></tr><tr><td>Mkt_Quotation</td><td>3499.4</td><td>3502.709</td><td>30.262</td><td>3463.7</td><td>3574.5</td></tr></table>

Please cite this article as: J. Liu, et al., Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.018

Regression analysis of Scenario 1 and Scenario 2.

<table><tr><td colspan="2">Scenario 1</td><td colspan="2">Scenario 2</td></tr><tr><td> $\Delta$ </td><td></td><td> $\Delta$ </td><td></td></tr><tr><td>a0</td><td>0.969***(7.61)</td><td>a4</td><td>-0.990 (-1.02)</td></tr><tr><td>a1(Ref_Consistency)</td><td>0.0000165*(2.02)</td><td>a5 (Ref_Consistency)</td><td>0.000132***(4.51)</td></tr><tr><td>a2(Customer_Type)</td><td>-1.398***(-4.58)</td><td>a6 (Customer_Type)</td><td>-0.0641 (-0.07)</td></tr><tr><td></td><td></td><td>a7 (Price_Fluct * Customer_Type)</td><td>-0.000175**(-3.23)</td></tr><tr><td> $R^{2}$ </td><td>0.53%</td><td> $R^{2}$ </td><td>2.86%</td></tr><tr><td>WTP</td><td></td><td>WTP</td><td></td></tr><tr><td>b0</td><td>360.1***(8.63)</td><td>b4</td><td>182.0 (1.55)</td></tr><tr><td>b1(LP)</td><td>0.968***(639.77)</td><td>b5 (LP)</td><td>1.003***(573.94)</td></tr><tr><td>b2(Customer_Type)</td><td>1459.9***(15.23)</td><td>b6 (Customer_Type)</td><td>491.8***(4.58)</td></tr><tr><td> $R^{2}$ </td><td>98.83%</td><td> $R^{2}$ </td><td>99.67%</td></tr><tr><td>LB</td><td></td><td>LB</td><td></td></tr><tr><td>c0</td><td>453.0***(6.12)</td><td>c4</td><td>-156.2 (-0.69)</td></tr><tr><td>c1(LP)</td><td>0.924***(344.01)</td><td>c5 (LP)</td><td>0.979***(267.52)</td></tr><tr><td>c2(Customer_Type)</td><td>2039.1***(11.99)</td><td>c6 (Customer_Type)</td><td>520.7*(2.52)</td></tr><tr><td></td><td></td><td>c7 (Price_Fluct*LP)</td><td>-0.000442**(-3.06)</td></tr><tr><td> $R^{2}$ </td><td>96.04%</td><td> $R^{2}$ </td><td>98.75%</td></tr><tr><td>N</td><td>5521</td><td>N</td><td>1064</td></tr></table>

\*p b 0.05, \*\*p b 0.01, \*\*\*p b 0.001 and t statistics in parentheses.

providers; the data will help to guide design of various information policies that influence customer decisions in practice.

Using an adapted dynamic choice model proposed and applied by Hann and Terwiesch, Fay, Spann et al., Fay, and Hinz et al. [6,8,11,14,31], we have analyzed the original motivations that hinder or facilitate a customer's haggling willingness. How distinct environmental price information affects the haggling decision, and thus the quoting outcomes, was also examined. We used variables from the customer's purchasing history to construct an efficient instrument of customer type, which will allow for better prediction of customer behavior. Using purchasing history rather than individual-specific information, such as socio-demographic backgrounds and financial status [11], as the foundation for customer classification is quite important in circumstances such as B2B purchasing, where the latter is not easy to acquire. The conclusion of how customer type can affect haggling willingness, expected LB of threshold price and WTP indirectly demonstrates the importance of customer type classification.

We adopted adaptation level theory [13] and tested consistency of the current revealed information and customer internal reference information as one major factor that affects customer's haggling willingness and final bidding results. Sellers can thus adjust list price according to a customer's transaction history and encourage customers to haggle less and quickly transact at a price that can be easily accepted. We also examined the influence of market price history, which has a vital function in informing customers about the usefulness of the current price information they are given. The results show us that it is the consistency rather than the amount of information that inhibits the customers' haggling willingness and promotes a faster transaction. Market information should be appropriately revealed, so that customers can filter out credible reference price and make rational choices. In addition, the bigger proportion of high haggling willingness in fluctuant market indicates that providers applying dynamic pricing strategy can increase threshold price even slightly, ending up with transactions with more haggling and higher customer utility in a volatile market. It is worth mentioning here that this dynamic pricing strategy should be employed within a company along with proper information revelation.

One limitation of the paper is that we assume that customer types, opportunity cost and risk averse factor are aligned in the same way, which restricts the generalizability of the paper. Besides, since formula 11 has three parameters to estimate while our research setting only allows three quotes at most in one bargaining, only the biddings with exact three quotes can be used to estimate (WTP, LB, δ) while the ones which are successful or aborted after one or two quotes are omitted. This omission might generate selection bias if the customers who transact more quickly perform differently from those who are more likely to haggle. Also, we do not examine how information revelation affects customer satisfaction, as the key of maintaining customer loyalty and long-term profitability [4,22], which could be meticulously studied in future research.

MAPE of regression models of real quotes on the fitted value.

<table><tr><td>Scenario</td><td>QUOTE1</td><td>QUOTE2</td><td>QUOTE3</td></tr><tr><td>1</td><td>1.78</td><td>1.54</td><td>1.34</td></tr><tr><td>2</td><td>0.94</td><td>0.76</td><td>0.61</td></tr></table>

## Acknowledgments

We thank the National Natural Science Foundation of China (Project No. 71272077, 71490721 and 71490723) and the E-Commerce Research Center at the School of Management of Fudan University for support.

## References

[1] W. Baker, E. Lin, M. Marn, C. Zawada, Getting prices right on the web, McKinsey Quarterly 10 (2) (2001) 1–20.

[3] H. Bruno, C. Hai, S. Dutta, Role of reference price on price and quantity: insights from business-to-business markets, Journal of Marketing Research 49 (5) (2012) 640-654.

[4] M. Campbell, Perceptions of price unfairness: antecedents and consequences, Journal of Marketing Research 36 (2) (1999) 187 199.

[5] M. Ding, J. Eliashberg, J. Huber, S. Ritesh, Emotional bidders—an analytical and experimental examination of consumers' behavior in a priceline-like reverse auction, Management Science 51 (3) (2005) 352–364.

[6] S. Fay, Competitive reasons for the name-your-own-price channel, Marketing Letters 20 (3) (2009) 277–293.

[7] S. Fay, J. Laran, Implications of expected changes in the seller's price in name-yourown-price auctions, Management Science 55 (11) (2009) 1783–1796.

[8] S. Fay, Partial-repeat-bidding in the name-your-own-price channel, Marketing Science 23 (3) (2004) 407–418.

[9] X. Huang, G. Sošic, Name-your-Own-Price as a Competitive Distribution Channel in the Presence of Posted Prices, Social Science Electronic Publishing 2010 04-10

[10] I. Hann, O. Hinz, M. Spann, Dynamic Pricing in Name-your-Own-Price Channels: Bidding Behavior Seller Profit and Price Acceptance Workshop on Information Systems and Economics, 2006.

[11] I. Hann, C. Terwiesch, Measuring frictional cost of online transaction: the case of a NYOP-retailer, Management Science 49 (11) (2003) 1563–1579.

[12] B. Hardie, E. Johnson, P. Fader, Modeling loss aversion and reference dependence effects on brand choice, Marketing Science 12 (3) (1993) 378–394

[13] H. Helson, Adaptation Level Theory, Harper and Row Publishers, Inc, New York 1964.

[14] O. Hinz I Hann M. Spann Price discrimination in e-commerce? An examination of dynamic pricing in name-your-own price markets, Mis quarterly 35 (1) (2011) 81-98

Please cite this article as: J. Liu, et al., Information revelation and customer decision-making process of repeat-bidding name-your-own-price auction, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.06.018

[15] O. Hinz, M. Spann, Managing information diffusion in name-your-own-price auctions, Decision Support Systems 49 (4) (2010) 474–485.

[16] O. Hinz, M. Spann, The impact of information diffusion on bidding behavior in secret price auction, Information Systems Research 19 (3) (2008) 351–368.

[17] M. Jones, P. Trocchia, D. Mothersbaugh, Noneconomic motivations for price haggling: an exploratory study, Advances in Consumer Research 24 (1997) 388–391.

[18] M. Joo, T. Mazumdar, S. Raj, Bidding strategies and consumer savings in NYOP auctions, Journal of Retailing 88 (1) (2012) 180–188.

[20] M. Kalwani, H. Rinne, Y. Sugita, C. Yim, A price expectations model of customer brand choice, Journal of Marketing Research 27 (8) (1990) 251–262.

[21] P. Klemperer, Auctions: Theory and Practice, Economics Group, Nuffield College, University of Oxford, Economics Papers, 2004.

[22] A. Lo, J. Lynch, R. Staelin, How to attract customers by giving them the short end of the stick, Journal of Marketing Research 44 (1) (2006) 128–141.

[23] G. Loomes, R. Sugden, A rationale for preference reversal, American Economic Review 73 (3) (1983) 428–432.

[24] R. Morgan, S. Hunt, The commitment–trust theory of relationship marketing, Journal of Marketing 58 (3) (1994) 20–38.

[25] MySpic index of domestic steel spot market, http://www.mysteel.net/myspic.html

[26] K. Rajendran, G. Tellis, Contextual and temporal components of reference price Journal of Marketing Research 58 (1) (1994) 22–34.

[27] A. Schwarz, B. Jayatilaka, R. Hirschheim, T. Goles, A conjoint approach to understanding IT application services outsourcing, Journal of the Association for Information Systems 10 (10) (2009) 748–781.

[28] J. Sherry, A sociocultural analysis of a Midwestern flea market, Journal of Consumer Research 17 (1990) 13–30.

[29] R. Schindler, The excitement of getting a bargain: some hypotheses concerning the origins and effects of smart-shopper feelings, Advances in Consumer Research 16 (1) (1989) 447–453.

[31] M. Spann, B. Skiera, B. Schäfers, Measuring individual frictional costs and willingness-to-pay via name-your-own-price mechanisms, Journal of Interactive Marketing 18 (4) (2004) 22–36

[32] M. Spann, G. Tellis, Does the internet promote better consumer decisions? The case of name-your-own-price auctions, Journal of Marketing 70 (1) (2006) 65–78.

[33] C. Terwiesch, S. Savin, I. Hann, Online haggling at a name-your-own-price retailer: theory and application, Management Science 51 (3) (2005) 339–351.

[34] T. Wang, Y. Michael, A. Hu, H. Wei, Name-your-own-price seller's information revelation strategy with the presence of list-price channel Flectronic Markets 20 (2010 119–129.

[35] R. Westbrook, W. Black, A motivation-based shopper typology, Journal of Retailing 61 (1) (1985) 78-103

[36] D. Wilson, Why divide consumer and organizational buyer behavior? European Journal of Marketing 34 (7) (2000) 780–791.

[37] A. Wolk, M. Spann, The effects of reference prices on bidding behavior in interactive pricing mechanisms, Journal of Interactive Marketing 22 (4) (2008) 2–18.

[38] M. Yadav, K. Seiders, Is the price right? Understanding contingent processing in reference price formation, Journal of Retailing 74 (99) (1998) 311–329.

[39] Z. Zhang, O. Netzer, A. Ansari, Dynamic Targeted Pricing in b2b Settings, Social Science Electronic Publishing, 2011.

Jie Liu (liujie@fudan.edu.cn) is a Professor of Information Management and Information Systems at the School of Management of Fudan University in Shanghai, China. He received his Ph.D. from Tongji University in Shanghai, China. He has been visiting Ecole nationale des ponts et chausses in Paris, France, and the University of California at Los Angeles, the University of California-Berkeley, and Stanford University. Jie Liu's current research interests are electronic commerce, innovation management. His research has been published or accepted in the Journal of Computers, Tsinghua Business Review, etc.

Rui Dai (rdai13@fudan.edu.cn) is a Ph.D. Candidate in the Department of Information Management and Information Systems, Fudan University, China. His research interests include dynamic pricing, electronic commerce and data mining. He has presented his paper at IEEE International Conference on Digital Ecosystems and Technology (DEST), Doctoral Forum of China Association for Information Systems (CNAIS) etc

Xueqi (David) Wei (weixueqi@fudan.edu.cn) is an Associate Professor in the Department of Information Management and Information Systems at Fudan University. He received his Ph.D. from the Haskayne School of Business at the University of Calgary in 2008. His re search interests include Information Goods, IT Impact on Capacity Utilization, IT Business Value, E-Business, Management of Technology, Economics of Information Systems and Theory Building in Information Systems. Dr. Wei has published articles in academic journals such as Production & Operations Management, Decision Support Systems, Entrepreneurship Research Journal, International Journal of Software Engineering and Computing, and Systems Engineering: Theory & Practice and presented at several international conferences and workshops such as the INFORMS Conference on Information Systems and Technology (CIST), International Conference on Information Systems (ICIS) etc.

Yongbing Li (yongbingli13@fudan.edu.cn) is a Ph.D. candidate in the Department of In dustrial Economics at Fudan University, China. He obtained his bachelor degree in Statistics at Fudan University. His research interests include Industrial Policy, Pricing, Bilateral Market and Corporate Governance.
