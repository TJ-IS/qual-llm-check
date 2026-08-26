---
otero_id: 5070
otero_key: "4EFAVQYY"
title: "Managing the Versions of a Software Product Under Variable and Endogenous Demand"
authors: "Kutsal Doğan; Yonghua Ji; Vijay S. Mookerjee; Suresh Radhakrishnan"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0275"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/4EFAVQYY/fulltext/images/7e7659b4237577ad26d5b78c06041f4316f66b02e21843077ab7453f5889cd20.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Managing the Versions of a Software Product Under Variable and Endogenous Demand

Kutsal Doğan, Yonghua Ji, Vijay S. Mookerjee, Suresh Radhakrishnan,

## To cite this article:

Kutsal Doğan, Yonghua Ji, Vijay S. Mookerjee, Suresh Radhakrishnan, (2011) Managing the Versions of a Software Product Under Variable and Endogenous Demand. Information Systems Research 22(1):5-21. http://dx.doi.org/10.1287/isre.1090.0275

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/4EFAVQYY/fulltext/images/90f288623013f01ed009ef7fe7f56cab57da494aae3c7c9e22a8072ce1d55151.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Managing the Versions of a Software Product Under Variable and Endogenous Demand

Kutsal Do ˘gan

Graduate School of Business, Özye ˘gin University, Altunizade, 34662 Istanbul, Turkey, kutsal.dogan@ozyegin.edu.tr

Yonghua Ji

School of Business, University of Alberta, Edmonton, Alberta T6G 2R6, Canada, yji@ualberta.ca

Vijay S. Mookerjee, Suresh Radhakrishnan

School of Management, University of Texas at Dallas, Richardson, Texas 75080 {vijaym@utdallas.edu, sradhak@utdallas.edu}

oftware product versioning (i.e., upgrading the product after its initial release) is a widely adopted practice Sfollowed by leading software providers such as Microsoft, Oracle, and IBM. Unlike conventional durable goods, software products are relatively easy to upgrade, making upgrades a strategic consideration in commer cial software production. We consider a two-period model with a monopoly software provider who develops and releases a software product to the market. Unlike previous research, we consider demand variability and endogeneity to determine the functionality of the software in the first and second periods. Demand endogeneity is the impact of the word-of-mouth effect that positively relates the features in the initial release of the product to its demand in the second period. We also determine the design effort that should be spent in the first period to prepare for upgrading the product in the second period—upgrade design effort—to tap into the possible future demand. Results show that the upgrade design effort can be lower or higher when there is more market demand uncertainty. We also show that the features of the product in its initial release and upgrade design effort can be complements as well as substitutes, depending on the strength of the word-of-mouth effect. The results in this paper provide insights into how demand-side factors (market demand variability or demand endogeneity) can influence supply-side decisions (initial features and upgrade design effort). A key insight of the analysis is that a high word-of-mouth effect helps manage the product in the face of demand variability.

Key words: software upgrades; demand endogeneity; upgrade design effort; demand variability; upgrade strategy

History: Seungjin Whang, Senior Editor; Giri Kumar Tayi, Associate Editor. This paper was received on January 16, 2008, and was with the authors 3 months for 2 revisions. Published online in Articles in Advance January 27, 2010.

## 1. Introduction

A useful characteristic of software products is that not all features need to be released simultaneously. Instead, there is the possibility of offering additional features as upgrades to an existing product. An upgrade is an enhanced version of an existing software product. Offering upgrades or improved versions is a viable means to enhance software functionality, eliminate bugs, and bring consumers up to date with new technology. For example, users of older Windows versions such as Windows 98, Windows Me, and Windows 2000 can upgrade to Windows XP and benefit from improved reliability and functionality; the same is true for upgrading from Windows XP to Vista.

Our study considers a monopolistic software provider introducing a software product in the face of market demand variability. The nature of demand variability for software products is highlighted, for example, in the personal finance software market. In 1985, Intuit’s Chief Executive Officer Scott Cook estimated California’s market demand for offline home finance software at roughly a quarter million units. This estimate was deemed to be optimistic, because at that time, the home banking industry’s goal was to create 50,000 consumers (see Forbes, November 15, 1984); however, in 1995, the personal finance software market demand was roughly 7 million (San Francisco Chronicle, May 22, 1995), which ex post indicates that Scott Cook’s estimate was too pessimistic.

Two aspects of this example are to be noted: first, the market demand for software products has variability and can increase dramatically, and second, the variability of market demand creates the potential to use aspects of software product design as a strategic tool. The software provider can delay the set of features to offer in a product until more accurate information on demand is available. Software production often involves large up-front costs that may not be recovered unless market demand is sufficiently high. By releasing upgrades only when future demand is known more precisely, software providers can avoid potential losses when the market demand is not favorable. While upgrading is also possible for physical products (e.g., by recalling the product to a manufacturing facility), doing so is likely to be much less cumbersome in the case of software products. In addition, the nature of a physical product may require that a customer buy an entirely new product rather than an upgrade for the existing product; however, for software products, customers can buy upgrades and incorporate them into the existing product with relative ease. Consequently, the potential for using software upgrades as a mechanism to tap into future potential is viable in many software production settings. Software providers can therefore use software upgrades as a strategic mechanism, enabling them to extract additional value.

However, delaying the delivery of product features to future upgrades has a downside because the features of a software product in one release can affect its future demand. Our model considers this possibility by allowing demand endogeneity across multiple releases of a software product: if the initial product has useful features, the demand for a future product or upgrade is likely to be positively impacted by these initial features. The idea is twofold: first, with more features in the initial release, the initial customers are likely to convey the usefulness of these features to more customers, and second, a product with more features in the initial release is likely to be perceived of higher quality—a higher quality today leads to a higher demand tomorrow (Shapiro 1982). In the presence of word-of-mouth referrals, more initial features lead to an increase in demand in the second period. To provide an example of this effect in the software industry, we draw on a real case of an in-house software organization within a large aerospace company that custom developed a complex engineering design system for its internal clients. At the initial release of the system, it was not clear how popular it would be among the design engineers, i.e., there was considerable demand variability; however, the system was a huge success, and numerous upgrades were released over the next several years. Our conversations with key software developers, including the project lead, revealed two important facts. First, the features chosen in each release affected the buzz generated about the software among its users, i.e., the level of demand in the next release was influenced by the set of features offered in the current release. Second, a significant amount of development effort—estimated by the project lead to be about 60% of the total effort—could have been saved if the system architecture during the initial release and each subsequent release was designed with an eye toward potential upgrades.<sup>1</sup>

Note also that the word-of-mouth effect can influence the variance of the future demand. A product with a higher word-of-mouth effect is likely to have higher-demand variability, because each user is more likely to discuss the product with other potential users. Thus, a larger word-of-mouth effect should cause more variability. Future demand variability can also be caused by other independent factors such as changes in consumer preferences, income levels, economic factors, and so on. In the home financing software example, it may be argued that future demand is influenced by changes in external factors such as computer literacy or access to personal computers at home rather than the specific set of features present in the current release of the software. Our research question is: In the presence of demand endogeneity and variability, how can strategic upgrade concerns be accommodated in the design of the software during its initial release, and, in particular, how does this potential affect software development decisions in the future?

## 1.1. Model Summary

We consider a two-period model where a monopolist software provider introduces the product with an initial set of features, and has the possibility of offering additional features during the second period in the form of an upgrade when more information on the second-period demand is available. The firstperiod demand is nonstochastic but the second-period demand is uncertain. In particular, the second-period demand can either be low, moderate, or high. The magnitude of the second-period demand is influenced by the initial features through the word-ofmouth effect. The second-period demand variance is determined by two parameters: uncertainty and spread. Demand uncertainty refers to the probability that the demand will be low, moderate, or high. Demand spread refers to the difference between high and low demand. Software development costs consist of three components: a fixed development cost, a variable cost for constructing each individual feature, and a feature integration cost ensuring that the product features work together to provide the desired functionality. Software development costs are incurred in both the first and second periods, depending on the initial features and the upgrades. In addition, there is a software design effort cost in the first period; the design effort in the first period helps reduce upgrade costs to both the software provider and the users in the second period.<sup>2</sup>

The primary tension in the model is that of striking a balance between development cost and upgrade design cost in the initial release of a product in the face of demand variability and the word-of-mouth effect. Software upgrades allow the software provider to distribute the software development and integration costs over the two periods, delaying the decision to incorporate additional features until better demand information is obtained. If a development investment during the first period leads to a product with high initial features, the software provider may not be able to recover this investment if the secondperiod demand turns out to be low. To counter this risk, the software provider can offer fewer features in the initial release by investing in relatively less development effort and more upgrade design effort; however, offering too few features in the initial release can lead to lower demand and profits in the second period because of the word-of-mouth effect. This tension leads to insights into the following aspects: (1) how the word-of-mouth effect influences the optimum balance between the initial features and the upgrades, (2) how the optimum balance of the initial features and upgrades influence the optimum design effort, and (3) how the information of the secondperiod demand and demand variability influence the initial features, upgrades, and design effort.

## 1.2. Main Results and Managerial Insights

In the context of our model, there are four potential upgrade strategies: never upgrade, upgrade-for-high demand, upgrade-for-moderate-and-high demand, and always upgrade. To discuss the intuition behind these strategies, we introduce the notion of the probability/likelihood that upgrades are provided. If the optimum strategy is never upgrade (always upgrade), then the likelihood of an upgrade is zero (one). If the optimum strategy is upgrade-for-high demand (upgrade-for-moderate-and-high demand), then the probability of an upgrade is the probability of high demand (the sum of the probability of high demand and the probability of moderate demand). Thus the likelihood of upgrades for the four strategies listed in increasing order is never-upgrade, upgrade-for-high demand, upgrade-for-moderate-and-high demand, and always upgrade.<sup>3</sup> The key results are summarized below. The first three results pertain to how the initial features and the upgrade design effort change across the upgrade strategies, and the last two results provide insights into the optimum upgrade strategy. In particular, in the last two results, we show how the demand variability and the word-of-mouth effect interact to determine the optimum upgrade strategy.

(1) The optimum upgrade design effort increases with the likelihood of upgrade: the upgrade design effort is lowest (highest) for the never- (always-) upgrade strategy. The intuition for this result is that when upgrades are more likely, the design effort cost incurred in the first period is less likely to be “wasted.”

(2) The initial features decrease with the likelihood of upgrade: the initial features are lowest (highest) for the always- (never-) upgrade strategy. If the likelihood of upgrade is high, the software provider can wait for the demand information and introduce additional features in upgrades. In doing so, the development cost can be incurred based on the second-period demand. Consider a setting where the level of low demand is zero, i.e., no customer is interested in the product. If the software provider introduces a product with some initial features and the low demand occurs, then the development cost is wasted. The wait for the demand information (“wait-and-see” approach) helps the software provider reduce such waste. In essence, the software provider copes with the second-period demand variability by delaying the decision on particular features until more information on demand is available. This occurs only when the word-of-mouth effect is sufficiently low, i.e., when the initial features do not influence the second-period demand by much.

(3) When the word-of-mouth effect is sufficiently high, the initial features increase with the likelihood of upgrade, which is the opposite of (2) above. When the word-of-mouth effect is high, offering more initial features will boost the second-period demand. This effect of boosting the second-period demand dominates the gain from delaying features to cope with demand variability. Thus, more initial features are provided if the likelihood of an upgrade is high, and vice versa.

(4) Consider the case when the word-of-mouth effect is small. On the one hand, if the second-period demand variability is high, it is beneficial for the software provider to offer fewer initial features (see (2) above). Therefore, providing upgrades for moderate and high demand is optimum. On the other hand, if the future demand variability is low, the software provider should offer more initial features and offer upgrades only when the demand is high. Thus, highdemand variability leads to a higher likelihood that upgrades will be offered and vice versa.

(5) When the word-of-mouth effect is high, the above intuition does not hold. In this case, it is optimum to offer the maximum possible initial features. Hence, when the word-of-mouth effect is high, the variability of demand does not affect the initial features offered. This reinforces the intuition in (3) above: when the word-of-mouth effect is high, second-period demand variability is less of a concern.

## 2. Related Work

Ellison and Fudenberg (2000) develop a two-period model to study a monopoly software provider’s incentive to provide upgrades. They show that a monopolistic software provider may introduce upgrades even when it is not socially optimal to do so. Some of the modeling concepts we use in this paper resemble their setting. Specifically, the twoperiod setup and modeling of the adoption costs of users are similar. Nevertheless, the focus of Ellison and Fudenberg’s (2000) paper is on the effects of software upgrades on social welfare. Our study is different in two important respects. First, in contrast to our model, Ellison and Fudenberg (2000) assume that the future market demand is known for certain. Second, in their study, the features of the software product in the two periods are assumed to be exogenously given, while the number of features is endogenously determined. In our study, the future demand is uncertain. Offering software upgrades is a mechanism to cope with future demand variability. We also allow the second-period demand to be influenced by the firstperiod decision on initial features through a word-ofmouth effect.

Padmanabhan et al. (1997) study a product upgrade problem by explicitly considering the product development cost in a competitive environment. Consumers and software providers have asymmetric information on product network externality, and upgrades serve as a signaling mechanism. The work of Padmanabhan et al. (1997) does not consider market demand variability. In our study, software upgrades serve as a strategy to cope with demand variability to maximize profit. On the other hand, our focus is on monopoly markets.

Raghunathan (2000) applies segmentation theory to study the problem of new software introduction; however, the focus of his study is on marketing different editions of a software product to different segments of the market; these editions are simultaneously released to the market. For example, the XP version of Windows has the Professional Edition, Home Edition, Tablet PC Edition, and so on. Instead, our work applies to the successive release of different versions of a software product. The focus here is on the economic analysis of market demand variability in the context of software development. In contrast to Raghunathan (2000), our work applies to planning across periods and studies the role of demand variability in staged software development. Although it may be interesting to investigate the use of upgrades as a customer segmentation mechanism, our work avoids customer heterogeneity and focuses on the use of software upgrades as a means to manage demand variability.

A number of papers have considered the effect of real options on information technology (IT) investment decisions (Dos Santos 1991, Kumar 1996, Taudes 1998). Dos Santos (1991) introduces an options approach to evaluate investments in sequentially linked IT projects. Sullivan et al. (1999) apply options theory to analyze important principles in software design and engineering, such as information hiding and incremental development. Benaroch and Kauffman (2000) study the deployment of point-ofsale (POS) debit services by the Yankee 24 banking network in New England and demonstrate how real options analysis can provide a powerful tool for evaluating real-world IT investments. Upgrade design effort is similar to a real option; however, our main focus is on strategic software upgrades, not on real options.

The portion of our problem formulation dealing with the allocation of product features to the initial and upgrade releases of a software product has similarities to the issues faced in designing software samples, or feature-limited evaluation versions of software products. Specifically, the determination of the optimal number of features to be included in a software sample to influence the success of the commercial version of the product is similar to the trade-off between the initial and upgraded product (Cakanyildirim and Dalgic 2002, Chellappa and Shivendu 2005, Faugère and Tayi 2007, Manica et al. 2007); however, we note that samples are often distributed free and used as a promotion tool. A sample distributed in this sense cannot exist without the associated commercial product; thus the sample is not a revenue source and it cannot be treated as a separate version, unlike the initial release of a software product. Therefore the design issues we discuss do not arise in designing software samples.

The rest of this paper is organized as follows. We present our model in the next section, describe the solution technique in $\ S 4 ,$ and analyze and present the important results in $\ S \ S 5$ and 6. We summarize the study and provide some concluding remarks in $\ S 7 .$

## 3. The Model

We consider a two-period model where the monopolist software provider decides on the features of a product in each period. A typical release process requires concurrent activities and decisions ranging from production to product pricing. Our model focuses on the production choices under demand variability. We describe the details of the model below.

## 3.1. Product Features

The software provider introduces the initial product features $\left( q _ { 1 } \right)$ in period 1 with the possibility of offering additional features $( q _ { 2 } )$ in period 2: thus the $q _ { 2 }$ features correspond to the upgrade. We assume that there is a maximum number of features that can be offered in each period, i.e., $q _ { 1 } \in [ 0 , q _ { 1 } ^ { \mathrm { m a x } } ]$ and $q _ { 2 } \in$ $\left[ 0 , q _ { 2 } ^ { \mathrm { m a x } } \right]$ . This is reasonable because supplying limitless features may be difficult if not impossible.

3.2. Market Structure and Demand Variability The market demand for period i is denoted $x _ { i }$ for $i = 1 , 2 $ , and $x _ { 2 }$ is uncertain. In particular, $x _ { 2 }$ may be low (L), medium (M), or high (H): $x _ { 2 } \in \{ x _ { 2 } ^ { \mathrm { L } } , x _ { 2 } ^ { \mathrm { M } } , \mathbf { \bar { \ } } x _ { 2 } ^ { \mathrm { H } } \}$ The second-period demand is assumed to consist of two components: a deterministic and a stochastic component. In particular, the second-period demand is given as

$$
x _ {2} ^ {j} = \bar {x} _ {2} + \lambda q _ {1} + (\lambda \alpha + \zeta) D ^ {j}\tag{1}
$$

for $D ^ { j } = 1 , 0 , - 1$ for $j = H , M , L$ . The deterministic portion is given by $\bar { x } _ { 2 } + \lambda q _ { 1 } .$ , and thus is partially endogenous; specifically, $\lambda q _ { 1 }$ depends on the initial features $( q _ { 1 } )$ that are chosen in period 1. These initial features attract customers in period 2, depending on the word-of-mouth parameter . When the word-ofmouth effect is large,  is large and vice versa. With more features in the initial release of the product, the initial customers will refer the product to other potential users, thereby increasing the demand in the second period.<sup>4</sup> The exogenous parameter (x<sub>¯</sub> - represents the lower bound when there is no word-of-mouth effect.<sup>5</sup>

The second-period demand can be high (H), medium (M), or low (L) with probabilities $\mathrm { P r } ^ { j }$ for $j = H , M , L$ . The total spread of the demand is $2 ( \lambda \alpha + \zeta ) ;$ in the high-(low-)demand realization, the magnitude of demand is the deterministic component plus (minus) the stochastic component, whereas for moderate demand, the magnitude is the deterministic portion alone. In addition to affecting the level of moderate demand, the word-of-mouth effect also influences the variance of the second-period demand through a herding parameter . For a given value of , a higher value of results in a higher spread of the second-period demand. The parameter is used to represent herding behavior associated with positive or negative consumer perceptions of a product. Such behavior has been observed in previous studies on how consumers react to and spread product referral information (Biyalogorsky et al. 2001). When the word-of-mouth effect is higher, regardless of whether the current customers are sharing negative or positive referrals with other customers (who are currently unaware of the product), the second-period demand will likely vary more compared to the case where the word-of-mouth effect is lower. We capture this effect with the herding parameter, . In §6.4, we also discuss an alternative model where the word-of-mouth effect could be different. The parameter  is the demand spread independent of the word-of-mouth effect. This parameter reflects shocks to the demand level based on factors such as the economic conditions or changing customer preferences $( \mathrm { i . e . , }$ essentially all factors other than the initial product features). Finally, to capture demand uncertainty, we assume a symmetric distribution with $\mathrm { P r } ^ { \mathrm { M } } = p$ and $\mathrm { P r } ^ { \mathrm { H } } = \mathrm { P r } ^ { \mathrm { L } } = ( \dot { 1 } - p ) / 2$ . Thus the distribution of demand is mean preserving and the variance changes because of either a change in $p$ or $\zeta . ^ { 6 }$

At the beginning of period 2, the software provider acquires precise information on the second-period demand that is used to choose the upgrade strategy.<sup>7</sup>

Depending on the information on market demand in period $\overline { { \textbf { 2 } } } ( x _ { 2 } )$ , the upgrades can vary, i.e., $q _ { 2 } \in$ $\{ q _ { 2 } ^ { \mathrm { L } } , q _ { 2 } ^ { \mathrm { M } } , q _ { 2 } ^ { \mathrm { H } } \}$

## 3.3. Upgrade Design Effort

The software provider can take steps during the initial development process to lower the cost of introducing an upgrade. These steps, referred to as upgrade design effort (denoted by y), include modular design of system functions, adherence to software engineering standards, clear design and coding documentation, and an easily modifiable user interface. Upgrade design effort also includes adopting standards and tools to support high-level design and documentation that make it easier to enhance the system in the face of new or changing requirements. The upgrade design effort expended in period 1 reduces the cost needed to offer additional features in period 2.<sup>8</sup>

## 3.4. Cost Structure

Consistent with prior literature (Moorthy and Png 1992, Padmanabhan et al. 1997), the cost of developing software is assumed to consist of three components. The first component is the fixed development cost denoted by $K .$ The second component is the cost of developing product features, which is assumed to be linear in features and is given by $b _ { 1 } q .$ . The third component is the cost of integrating the product features, which is assumed to be quadratic in features and is given by $b _ { 2 } q ^ { 2 }$ . This quadratic form is shown to be a good fit (Mookerjee and Chiang 2002) and captures the fact that features interact with one another in a software product. Therefore the software provider incurs a cost $K _ { i } + b _ { 1 } q _ { i } + b _ { 2 } q _ { i } ^ { 2 }$ to develop the software with $q _ { i }$ features in period i

Besides the cost of actually developing the product features, there is the cost of upgrading design effort. This design cost is modeled using a quadratic cost function $( a y ^ { 2 } )$ to represent the increasing difficulty of providing additional advanced design effort $( y )$ . The first and second-period costs $( C _ { 1 }$ and $C _ { 2 } )$ are given by

$$
\begin{array}{c} C _ {1} = K _ {1} + b _ {1} q _ {1} + b _ {2} q _ {1} ^ {2} + a y ^ {2} \quad \text { and } \\ C _ {2} = K _ {2} (1 - \beta y) + b _ {1} q _ {2} + b _ {2} (q _ {1} + q _ {2}) ^ {2} - b _ {2} q _ {1} ^ {2}, \text { respectively. } \end{array}
$$

The total software development and upgrade design cost in the first period $( \bar { C } _ { 1 } )$ consist of the direct development cost and the upgrade design effort cost. The total software development cost in the second period is $C _ { 2 }$ if an upgrade is offered. The fixed development cost in the second period, $K _ { 2 } ( 1 - \beta y )$ , captures the benefit of the design effort y invested in period 1, where $\beta y < 1$ for all $y > 0$ . If no design effort is chosen in period 1 $( y = 0 )$ , then the second-period fixed development cost is $K _ { 2 }$ . The design effort introduced in the first period reduces the fixed development cost in the second period. For example, good documentation in the first period can reduce the effort to understand and enhance the existing system (Lethbridge et al. 2003). Clearly, some of the design effort could affect the current development costs. That is, y could influence the costs in period 1 as well. To isolate the strategic upgrade effect, we only focus on the part of design effort that affects future costs (i.e., future development and use). The cost of upgrade design effort is sunk and produces benefits only if an upgrade is offered. Empirical evidence shows that upfront effort spent on software process improvements, product planning, high-level design, and architecture has significant positive impact on software quality and leads to savings in system development (Harter et al. 2000, Krishnan et al. 2000). Also, good documentation of the existing system helps to reduce the effort to understand and enhance it (Lethbridge et al. $2 0 0 3 ) . ^ { 9 }$ It is also possible that design effort affects the integration costs in the second period by impacting the integration cost coefficient $b _ { 2 }$ . We do not consider this aspect to keep the model tractable. If design effort is allowed to reduce future integration costs, this will result in more design effort and make upgrades more likely; however, the relative ordering and differences across upgrade strategies will be unaffected and the results will be qualitatively similar. The cost of developing additional product features $( q _ { 2 } )$ for the upgrade is given by $b _ { 1 } q _ { 2 }$ . The cost of integrating all the features $( q _ { 1 } + q _ { 2 } )$ in the upgraded product is $b _ { 2 } ( q _ { 1 } + q _ { 2 } ) ^ { 2 }$ minus $( b _ { 2 } q _ { 1 } ^ { 2 } )$ , because the initial product features have already been made consistent with respect to one another.

## 3.5. Customers and Demand Structure

Customers are assumed to be homogeneous and may buy one unit of the product. In period 2, the customers from period 1 may upgrade if an upgrade is offered and is valuable. The new customers in period 2 can buy either the upgraded product or the initial release if an upgrade is not available. We assume that the software provider removes the initial release of the product from the market when the upgrade is offered.

The customer’s utility depends on features and is given by $\theta q .$ . The customer is assumed to incur a cost (c- to set up and learn the product. The customers who purchase the initial release incur an additional cost $c _ { u }$ if they upgrade in the second period. The design effort $y$ makes it easier for customers to adapt to the upgrade. This spillover benefit of the design effort on the customer’s upgrade cost is given by $c _ { u } = c _ { 0 } ( 1 - \gamma y )$ , where !y < 1 for all $y > 0 .$ 10 The upgrade cost is $c _ { 0 }$ if there is no upgrade design effort in period 1. The parameter ! influences the extent to which design effort can potentially reduce the upgrade costs $c _ { u } .$

## 3.6. Product Pricing and Customer Net Utility

Because consumers are assumed to be homogeneous, price is not used as an instrument to segment the market. Our focus is on the software design process and its relationship to the uncertainty of demand in the second period.<sup>11</sup> The software provider charges a price of $P _ { 1 }$ for the product with features $q _ { 1 }$ in period 1 and a price $P _ { 2 }$ for the upgraded product with product features $( q _ { 1 } + q _ { 2 } )$ in period 2. The software provider charges $P _ { u }$ for the upgrade; customers who purchase the product in period 1 can buy the upgrade at an additional price of $P _ { u }$ . The prices depend on the customer utility associated with the initial product, the utility associated with the upgrade, and the utility associated with the upgraded product for period 2 customers. The total net utility for the period 1 customers $\left( u _ { 1 } \right)$ is the net utility of using the product with the initial product features for two periods. If there is no upgrade, this is the only customer net utility to consider. In the second case when there is an upgrade, the additional net utility that a period 1 customer gets by purchasing the upgrade is $\bar { u } _ { \mathrm { u p g r a d e } } . ^ { 1 2 }$ Finally, there is the net utility of period 2 customers $\left( u _ { 2 } \right)$ . These customer utilities are related to prices as follows:

$$
\begin{array}{c} u _ {1} = (1 + \delta) \theta q _ {1} - c - P _ {1}, \\ u _ {\text { upgrade }} = \theta q _ {2} - c _ {u} - P _ {u} = \theta q _ {2} - c _ {0} (1 - \gamma y) - P _ {u}, \\ \text { and } \quad u _ {2} = \theta (q _ {1} + q _ {2}) - c - P _ {2}. \end{array}
$$

In the utility representations above, the first term represents the intrinsic utility of using the software product with $\{ q _ { 1 } , q _ { 2 } , q _ { 1 } + q _ { 2 } \}$ product features, respectively. Because customers who purchase the initial release use the product in both periods, the secondperiod utility is discounted using the discount factor (#). The second term represents the customer’s cost of setup and learning, and the last term is the price paid. The software provider sets prices to extract the customer surplus as follows:

$$
\begin{array}{c} P _ {1} ^ {*} = (1 + \delta) \theta q _ {1} - c, \\ P _ {u} ^ {*} = \theta q _ {2} - c _ {0} (1 - \gamma y), \quad \text {and} \quad P _ {2} ^ {*} = \theta (q _ {1} + q _ {2}) - c. \end{array}
$$

We next formulate the software provider’s problem.

## 4. Formulation and Optimization of Software Provider’s Problem

The provider chooses the initial features $( q _ { 1 } ) ,$ upgrades $( q _ { 2 } )$ if an upgrade is offered, and design effort (y-. Note that $q _ { 1 }$ and $y$ are chosen at the beginning of period 1, and $q _ { 2 }$ is chosen at the beginning of period 2, when demand information becomes available. The first-period decisions are made optimally in the sense that the possible second-period outcomes are considered. We solve the software provider’s problem by backward induction. A glossary of the notation used in this paper is provided in a table in the online appendix.<sup>13</sup>

## 4.1. Software Provider’s Upgrade Decision in the Second Period

The second-period profit is given by

$$
\pi_ {2 U} ^ {j} = P _ {2} (q _ {1}, q _ {2} ^ {j}) x _ {2} ^ {j} + P _ {u} (q _ {1}, q _ {2} ^ {j}, y) x _ {1} - C _ {2} (q _ {1}, q _ {2} ^ {j}, y)
$$

if an upgrade is provided. The first term is the revenue from the second-period customers purchasing the upgraded product, and the second term is the revenue from the upgrades sold to the first-period customers. The last term is the cost of developing the upgrade with $q _ { 2 } ^ { j }$ features. In substituting the price and cost functions, we get

$$
\begin{array}{r} \pi_ {2 U} ^ {j} = [ \theta (q _ {1} + q _ {2} ^ {j}) - c ] x _ {2} ^ {j} + [ \theta q _ {2} ^ {j} - c _ {0} (1 - \gamma y) ] x _ {1} \\ - K _ {2} (1 - \beta y) - b _ {1} q _ {2} ^ {j} - 2 b _ {2} q _ {1} q _ {2} ^ {j} - b _ {2} (q _ {2} ^ {j}) ^ {2}. \end{array}\tag{2}
$$

The second-period profit when there are no upgrades is given by $\bar { \pi } _ { 2 N U } ^ { j } = \bar { P } _ { 2 } ( q _ { 1 } , q _ { 2 } ^ { j } = 0 ) x _ { 2 } ^ { j } = ( \theta q _ { 1 } - c ) x _ { 2 } ^ { j }$ . Therefore the incremental profit $( \Delta \pi _ { 2 } ^ { J } )$ from offering an upgrade in the second period is given by

$$
\begin{array}{r} \Delta \pi_ {2} ^ {j} = \pi_ {2 U} ^ {j} - \pi_ {2 N U} ^ {j} = \theta q _ {2} ^ {j} (x _ {1} + x _ {2} ^ {j}) - c _ {0} (1 - \gamma y) x _ {1} \\ - K _ {2} (1 - \beta y) - b _ {1} q _ {2} ^ {j} - 2 b _ {2} q _ {1} q _ {2} ^ {j} - b _ {2} (q _ {2} ^ {j}) ^ {2}. \end{array}\tag{3}
$$

The second-period problem for the software provider involves choosing $q _ { 2 } ^ { j }$ for $j = H , M , L$ so as to maximize $\Delta \pi _ { 2 } ^ { j } .$ . The first-order condition for the optimum $q _ { 2 } ^ { j }$ for any given $q _ { 1 }$ and y is given by<sup>14</sup>

$$
\begin{array}{c} {[ \partial \Delta \pi_ {2} ^ {j} / \partial q _ {2} ^ {j} ] = \theta (x _ {1} + \bar {x} _ {2} + \lambda q _ {1} + D ^ {j} (\lambda \alpha + \zeta)) - b _ {1}} \\ {- 2 b _ {2} q _ {1} - 2 b _ {2} q _ {2} ^ {j} = 0.} \end{array}\tag{4}
$$

The optimum upgrade $q _ { 2 } ^ { j * }$ for each demand realization $j = H , M , I$ is the solution to (4); the expression is provided in the online appendix. Substituting the optimum upgrade in (3), the optimum incremental profit $\Delta \pi _ { 2 } ^ { j * }$ is obtained and is also shown in the online appendix.

For the upgrade to be optimum, the software provider’s incremental second-period profit should be positive; a necessary condition for the upgrade to occur is $\Delta \pi _ { 2 } ^ { j * } > 0$ . An important observation that will help identify the potential upgrade strategy is that for any given pair of $q _ { 1 }$ and y, we have $\Delta \bar { \pi } _ { 2 } ^ { \mathrm { { \breve { H } * } } } >$ $\Delta \pi _ { 2 } ^ { \mathrm { M } * } > \Delta \bar { \pi } _ { 2 } ^ { \mathrm { L } * }$ . Therefore the software provider will always upgrade at a higher level of the second-period demand if it is profitable to do so at a lower level. This leads to four possible strategies for upgrades.<sup>15</sup> We denote $\Omega \in \{ \mathrm { N , \bar { H } , M H , A } \}$ as the upgrade strategy space, where N denotes that the software provider never provides an upgrade $( 0 > \Delta \pi _ { 2 } ^ { \mathrm { H * } } > ^ { \bullet } \Delta \pi _ { 2 } ^ { \mathrm { M * } } >$ $\Delta \pi _ { 2 } ^ { \mathrm { L } * } )$ , H denotes that the software provider offers an upgrade only if the demand is high $( \Delta \pi _ { 2 } ^ { \mathrm { H * } } >$ $0 > \bar { \Delta } \pi _ { 2 } ^ { \mathrm { M } * } > \Delta \pi _ { 2 } ^ { \bar { \mathrm { L } } * } )$ , MH denotes that the software provider offers an upgrade when the demand is either medium or high $( \grave { \Delta \pi _ { 2 } ^ { \mathrm { H * } } } > \Delta \pi _ { 2 } ^ { \mathrm { M * } } > 0 > \Delta \pi _ { 2 } ^ { \mathrm { L * } } )$ , and A denotes that the software provider always offers an upgrade $( \Delta \pi _ { 2 } ^ { \mathrm { H * } } > \Delta \pi _ { 2 } ^ { \mathrm { M * } } > ^ { \bullet } \Delta \pi _ { 2 } ^ { \mathrm { L * } } > 0 )$ . We define an indicator variable $z ^ { \Omega } \in \{ 0 , 1 \} ,$ , where $z ^ { \Omega } = 1$ if the software provider’s best strategy is ) and $z ^ { \Omega } = 0$ otherwise. Using this notation, the expected incremental profit function is given by

$$
\begin{array}{r} E [ \Delta \pi_ {2} | \Omega ] = \mathrm{Pr} ^ {\mathrm{H}} \Delta \pi_ {2} ^ {\mathrm{H}} (z ^ {\mathrm{H}} + z ^ {\mathrm{MH}} + z ^ {\mathrm{A}}) \\ + \mathrm{Pr} ^ {\mathrm{M}} \Delta \pi_ {2} ^ {\mathrm{M}} (z ^ {\mathrm{MH}} + z ^ {\mathrm{A}}) \\ + \mathrm{Pr} ^ {\mathrm{L}} \Delta \pi_ {2} ^ {\mathrm{L}} z ^ {\mathrm{A}} + \pi_ {2 N U} z ^ {N}. \end{array}
$$

The first term represents the software provider’s profit when the second-period demand is high and an upgrade is offered by the software provider. Note that in three of the strategies (H, MH, A), the software provider achieves a positive incremental profit by offering an upgrade when the demand is high. Similarly, the second term implies that the software provider offers an upgrade at the medium demand level in two of its strategies (MH, A), and finally, the third term implies that an upgrade is offered at the low demand in only one strategy profile (A). We proceed with the software provider’s optimum decision.

## 4.2. Software Provider’s First-Period Decisions, Total Profit, and Upgrade Strategy

The total expected profit for a given strategy ) is given by

$$
\pi^ {\Omega} = \pi_ {1} + \delta E [ \Delta \pi_ {2} | \Omega ].\tag{5}
$$

The first term represents the profit of the first period: $\pi _ { 1 } = P _ { 1 } ( q _ { 1 } ) x _ { 1 } - \bar { C } _ { 1 }$ . The second term represents the expected profit for the second period. The software provider’s problem is represented in the following program:

Program

$$
\underset {q _ {1}, y, z ^ {\Omega}} {\text {Max}} \pi^ {\Omega}
$$

subject to $z ^ { \Omega } \Delta \pi _ { 2 } ^ { j * } > 0 ~ \mathrm { f o r } ~ \forall j \in j ^ { \Omega }$

$$
z ^ {\Omega} \Delta \pi_ {2} ^ {j *} \leq 0 \quad \mathrm{for} \forall j \notin j ^ {\Omega}\tag{OPTS1}
$$

(OPTS2)

$$
\sum_ {\Omega \in \{\mathrm{N,H,MH,A} \}} z ^ {\Omega} = 1\tag{OPTZ}
$$

$$
q _ {1}, q _ {2} ^ {j *}, y > 0 \quad \mathrm{for} \forall j \in j ^ {\Omega}
$$

$$
\begin{array}{r l} & z ^ {\Omega} \in \{0, 1 \} \\ & \qquad \mathrm{for} \forall \Omega \in \{\mathrm{N}, \mathrm{H}, \mathrm{MH}, \mathrm{A} \}, \end{array}\tag{FEAS}
$$

(ZF)

where $j ^ { \Omega }$ is the set of demand levels (j- at which the software provider offers an upgrade for its given strategy profile $( \Omega ) \colon j ^ { \Omega } \equiv \partial \mathrm { i f } \tilde { \Omega } \equiv N , j ^ { \Omega } \equiv \{ \breve { \mathrm { H } } \}$ if $\Omega \equiv \ddot { H } , j ^ { \hat { \Omega } } \equiv \{ M , H \}$ if $\Omega \equiv M H ,$ , and $j ^ { \Omega } \equiv \{ M , H , L \}$ if $\Omega \equiv A$ . Constraints (OPTS1) and (OPTS2) define the optimum incremental second-period profits as discussed with the strategy choice ). Constraint (OPTZ) requires that only one of the four strategies is optimum, constraint (FEAS) ensures that the optimum features and upgrade design effort are feasible (greater than zero), and constraint (ZF) ensures that the value $z ^ { \Omega }$ is feasible. For any given strategy, the optimum interior $q _ { 1 }$ and y satisfy the following firstorder conditions: $\partial \pi / \partial q _ { 1 } = 0$ and $\partial \pi / \partial y = 0 . ^ { \textrm { \tiny 1 6 } }$ The expressions of optimum $q _ { 1 }$ and y are presented in the online appendix. We next provide some results and insights from analyzing the model.

## 5. Analyses of the Solutions to the Program

While characterizing a closed-form solution is complex, we proceed in steps. First, we examine the relationship between the first- and second-period product features. Next, we examine the impact of the wordof-mouth effect - on the optimum features for each strategy to provide insights on the relationship among the initial features, upgrades, and upgrade design effort.

## 5.1. First- and Second-Period Product Features: Substitutes or Complements?

An interesting question in software development is the relationship between features across successive releases of a product. Are the initial features and upgrades substitutes? That is, when the initial features are high, are the upgrades low and vice versa? The answer to the above question depends on the word-of-mouth effect (). Recall that the word-ofmouth effect captures the impact of the first-period product features on the mean second-period demand as well as the demand variability. Proposition 1 provides an answer to this question.<sup>17</sup>

Proposition 1. (1) If the word-of-mouth effect is sufficiently low, the optimum initial features and upgrades are substitutes. Technically, if $\lambda < [ \dot { 2 b } _ { 2 } / \theta ] .$ , then $[ d q _ { 2 } ^ { * } / d q _ { 1 } ^ { * } ] < 0$

(2) If the word-of-mouth effect is sufficiently high, the optimum initial features and upgrades are complements. Technically, if $\lambda > [ 2 b _ { 2 } / \theta ]$ , then $[ d q _ { 2 } ^ { * } / d q _ { 1 } ^ { * } ] > 0$

To understand the above results, let us first consider the extreme case when there is no word-of-mouth effect $( \lambda = 0 )$ . In this case, Proposition 1.1 applies and the initial features and upgrades are substitutes: if one increases, the other decreases. Given that there is no word-of-mouth effect, the initial features do not influence the second-period demand, and there is no benefit in terms of an increased second-period demand to providing more initial features. In such a scenario, the total cost of the initial features and upgrades across the two periods needs to be balanced; because the cost of features is increasing and convex, splitting the features over the two periods is optimum. Thus, this is a cost side effect. Loosely speaking, the software provider has a notion of the fixed total features desired in the product given the total expected demand. This fixed set of features is allocated to each of the two periods: if more is allocated to the first period, less is allocated to the second period and vice versa.

Next, consider the case where the word-of-mouth effect is large enough that Proposition 1.2 applies. In this case, more initial features, on average, result in a higher second-period demand. Therefore the software provider finds it beneficial to have more initial features. However, because of the increase in the second-period expected demand, the likelihood of offering upgrades also increases. As a consequence, the initial features and upgrades become complements. Note that the word-of-mouth effect needs to be sufficiently large to offset the cost side effect implied by Proposition 1.1.

## 5.2. The Impact of Word-of-Mouth Effect on Initial Product Features

We next consider the impact of the word-of-mouth effect on the initial features of the product.

Proposition 2. (1) If the word-of-mouth effect is sufficiently high, offering the maximum possible initial features is optimum. Technically, if $\lambda \ge ( b _ { 2 } / \delta \theta )$ , then $q _ { 1 } ^ { \Omega * } = q _ { 1 } ^ { \mathrm { m a x } }$ for all ).

(2) If the word-of-mouth effect is moderate, the initial features increase with the likelihood of providing an upgrade. Technically, $i f \ ( b _ { 2 } / \delta \theta ) > \lambda \geq ( 2 b _ { 2 } / \theta )$ , then $q _ { \scriptscriptstyle 1 } ^ { \mathrm { A } * } > q _ { \scriptscriptstyle 1 } ^ { \mathrm { M H } * } > q _ { \scriptscriptstyle 1 } ^ { \mathrm { H } * } > q _ { \scriptscriptstyle 1 } ^ { \mathrm { N } * }$

(3) If the word-of-mouth effect is sufficiently low, the initial features decrease with the likelihood of providing an upgrade. Technically, $i f \lambda < \operatorname * { m i n } \{ ( 2 b _ { 2 } / \theta ) , ( \dot { b _ { 2 } } / \dot { \delta } \theta ) \}$ , then $q _ { 1 } ^ { \mathrm { A } * } < q _ { 1 } ^ { \mathrm { M H } * } < q _ { 1 } ^ { \mathrm { H } * } < q _ { 1 } ^ { \mathrm { N } * }$

Proposition 2.1 shows that if the word-of-mouth effect is sufficiently high, the maximum possible initial features should be provided (a corner solution). This is intuitive: if the initial features strongly impact the second-period demand, the software provider loads as many features as possible in the initial product.<sup>18</sup>

Proposition 2.2 shows that for moderate levels of the word-of-mouth effect, it is optimum to provide the highest number of initial features if upgrade strategy A is optimum, followed by upgrade strategy MH, H, and N in that order. Consider upgrade strategy A. Because the upgrade strategy is to offer upgrades in the second period even if the demand is low, the software provider decreases the impact of a bad draw of demand in the second period by providing more initial features. This protection from the bad draw is made possible because the word-of-mouth effect is large. Compared to upgrade strategy A, in strategy MH, the necessity of protecting the impact of the bad draw of demand is not high, because no upgrades will be offered when the demand is low. Therefore the initial features in the first period are lower in strategy MH than in strategy A.

Proposition 2.3 shows that the ordering of the values of the initial features switches when the wordof-mouth effect is low. To see the intuition for this result, consider a setting where $\lambda = 0 .$ . In this case, the initial features do not directly impact the secondperiod demand. It follows that it is not possible to protect against a bad draw of demand by choosing a high enough number of initial features. The optimum initial features decision is driven by cost considerations: as the expected number of features offered in the second period decreases, more features can be offered in the initial release of the product. The notion of a “fixed number of total features” discussed in Proposition 1.1 applies. Therefore, when no upgrades are offered in the second period, more initial features are offered. The software provider’s expected upgrade features decrease as we move from a strategy with higher likelihood of offering an upgrade (example, MH) to one with less likelihood of offering an upgrade (example, H).

## 5.3. Initial Product Features and Upgrade Design Effort: Substitutes or Complements?

We first show that the optimum upgrade design effort increases as we move from a strategy with less likelihood of offering an upgrade (example H) to one with a higher likelihood of offering an upgrade (example MH). This is made precise in the following proposition.

Proposition 3. The optimum upgrade design effort increases as the software provider offers upgrades for a wider range of second-period demand levels. Technically, $y ^ { \mathrm { A } * } > y ^ { \mathrm { M } \breve { \mathrm { H } } * } > ^ { ^ { } } y ^ { \mathrm { H } * } > y ^ { \mathrm { N } ^ { * } }$

Proposition 3 shows that as the software provider becomes more likely to offer upgrades, it prepares for the upgrade by investing more in design. However, taken with Proposition $2 ,$ we see that the relationship between the software provider’s design and product development efforts is intricate. The two could be substitutes as well as complements. The key is the level of word-of-mouth effect. Using the results of Propositions 2 and 3, we make the following observation that summarizes the impact of the word-ofmouth effect on the relationship between design and development effort.

Observation. The first-period product features and upgrade design effort could be substitutes or complements. Specifically,

(1) When the word-of-mouth effect is sufficiently low, the initial features and upgrade design effort are substitutes. Technically, if  < min $\{ ( 2 b _ { 2 } / \stackrel {  } { \theta } ) , ( b _ { 2 } / \delta \theta ) \}$ then $q _ { \bot \cdot } ^ { \mathrm { A } * } < q _ { 1 } ^ { \mathrm { M H } * } < \bar { q } _ { 1 } ^ { \mathrm { H } * } < q _ { 1 } ^ { \mathrm { N } * }$ and $y ^ { \mathrm { A * } } > y ^ { \mathrm { M H * } } >$ $y ^ { \mathrm { H * } } > \dot { y } ^ { \mathrm { N * } }$

(2) When the word-of-mouth effect is sufficiently high, the initial features and upgrade design effort are complements. Technically, if $\lambda \ge \operatorname* { m i n } \dot  \{ ( 2 b _ { 2 } / \theta )$ $\left( b _ { 2 } / \delta \theta \right) \left\{ \begin{array} { r l } \end{array} \right.$ , then $q _ { 1 } ^ { \mathrm { A } * } \geq q _ { 1 } ^ { \mathrm { M H } * } \geq q _ { 1 } ^ { \mathrm { H } * } \geq q _ { 1 } ^ { \mathrm { N } * }$ and $y ^ { \mathrm { A * } } > y ^ { \mathrm { \bar { M H } * } } >$ $y ^ { \mathrm { H * } } > y ^ { \mathrm { N * } }$

The above observation shows that the development efforts spent on the initial features and on the upgrade design are substitutes when the word-ofmouth effect is low. If the software product is such that the word-of-mouth effect is low, the software provider will reduce the quantity of initial features when it is more likely to offer upgrades. Nevertheless, to prepare for a more likely upgrade, the provider will increase its upgrade design effort. This substitution effect is reversed for a sufficiently high level of word-of-mouth effect where the two efforts become complements.

## 6. Characterizing the Optimum Upgrade Strategy

We proceed to characterize the optimum upgrade strategy ()-, the solution to the program. We focus on the H and MH strategies to gain insights into how the word-of-mouth effect and demand variability affect the optimum strategy and the decision variables. An important ingredient for strategic upgrade is that waiting for and obtaining precise demand information has to be valuable and enhance the profits by influencing the decisions. Focusing on strategies H and MH enables the comparison of strategies when information is valuable. To see this, note that with the never-upgrade strategy (N), information on future demand is not used. The upgrade design effort and initial features are by definition not contingent on the second-period demand. As such, we do not consider strategy N. At the other extreme is the alwaysupgrade strategy A. In this case, the information on future demand is always valuable and there is a clear strategic upgrade effect. Including upgrade design strategy A in our analysis would involve more complicated analysis without providing additional insights on upgrade design effort.<sup>19</sup>

We make some technical assumptions to ensure that strategies A and N are not optimum, and ensure that an interior solution to the program can be obtained for strategies H and MH.

Assumption 1 (A1). The demand spread is sufficiently large, i.e., $\zeta > x _ { 1 } + \bar { x } _ { 2 } - \lambda \cdot \alpha - b _ { 1 } / \theta + ( \lambda - 2 b _ { 2 } / \theta ) \cdot q _ { 1 } ^ { \mathrm { A } * } ,$ where $q _ { 1 } ^ { \mathrm { A * } }$ is given in the online appendix.

Assumption A1 ensures that upgrade strategy A is not optimum. If the demand spread parameter (- is high, it follows that the low-demand realization $( x _ { 2 } ^ { \mathrm { L } } )$

in the second period is very small. Assumption A1 requires $x _ { 2 } ^ { \mathrm { L } }$ to be sufficiently small such that the incremental profit in the second period when the low demand is realized is negative. As such, providing an upgrade is not optimum when the low demand is realized. An important aspect to note here is that Assumption A1 also implies that the word-of-mouth effect () is not too large and as such, Assumption A1 implicitly implies that Proposition 2.3 occurs.<sup>20</sup>

Lemma 1. Providing upgrades always (strategy A) is not optimum if the demand spread parameter (- is sufficiently high (when Assumption A1 holds).

Assumption 2 (A2). The following inequality holds: $K _ { 2 } < [ \theta ^ { 2 } ( x _ { 1 } + \bar { x } _ { 2 } + D ^ { j } ( \lambda \alpha + \bar { \zeta } ) - b _ { 1 } \bar { / } \theta + \bar { ( \lambda - 2 } b _ { 2 } / \theta )$ $q _ { 1 } ^ { \mathrm { N U * } } ) ^ { 2 } / 4 b _ { 2 } ] - c _ { 0 } x _ { 1 } ,$ where $q _ { 1 } ^ { \mathrm { N U * } }$ is given in the online appendix.

Assumption A2 ensures that the never-upgrade strategy is not optimum. When the upgrade cost $K _ { 2 }$ is sufficiently small, the additional profit the provider gains from upgrades is positive at least for the highdemand realization. As such, providing an upgrade in the high-demand case is always profitable and never providing an upgrade is not optimum when the cost parameter $K _ { 2 }$ is sufficiently low. This is stated in Lemma 2.

Lemma 2. Never providing upgrades (strategy N) is not optimum if the design cost parameter is sufficiently low (when Assumption A2 holds).

Assumption 3 (A3). The following inequality holds: $\delta ( K _ { 2 } \beta + \gamma c _ { 0 } x _ { 1 } ) / ( 2 a ) < \operatorname* { m i n } ( 1 / \beta , 1 / \gamma )$

Assumption A3 requires that the fixed development cost in the second period $( K _ { 2 } )$ and customer setup and learning cost $( c _ { 0 } )$ are not too large. The benefit of the design effort arises from mitigating the secondperiod fixed development cost and the customer setup cost. If the fixed development cost or the customer setup cost is very large, the optimum design effort can be the maximum possible value to mitigate the fixed development cost or the customer setup cost to the utmost. By requiring that the design cost parameter a is not too small, Assumption A3 ensures that the optimum design effort is not a corner solution. This is stated in Lemma 3.

Lemma 3. The optimum design effort $( y ^ { \Omega * } )$ is interior when Assumption A3 holds.

We next proceed to examine the optimum upgrade strategies H and MH under Assumptions A1–A3.

## 6.1. Optimum Upgrade Strategy

We first examine the impact of the second-period demand variability on the software provider’s choice between strategies H and MH. Our interest is in the impact of the demand spread parameter $\zeta .$ .

Proposition 4. If the word-of-mouth effect is low or moderate and

(1) If the second-period demand spread is low, upgrade strategy H is optimum. Technically, if $\zeta < \zeta ^ { * }$ and $a > a ^ { * }$ then $\Breve { z ^ { \mathrm { H } } } = 1$

(2) If the second-period demand spread is high, upgrade strategy MH is optimum. Technically, $i f \zeta > \zeta ^ { * }$ and $a > a ^ { * } ,$ , then $z ^ { \mathrm { M H } } = 1$

The expressions for $\zeta ^ { * }$ and $a ^ { * }$ are provided in the online appendix.

Note that the demand spread parameter $\zeta$ can be used as a measure of demand variability because the demand variance is high (low) when the demand spread is high (low) in our mean-preserving demand setting. Proposition 4 shows that when the demand variance is high, more upgrades are likely and vice versa. From Proposition $^ { 2 , }$ we know that fewer initial features are provided and more upgrades are provided in MH than in H. There are two cost considerations of delaying the features: (1) the word-of-mouth effect of the initial features is lower, leading to lower second-period revenues, and (2) there is a second-period fixed cost to be incurred. The second-period fixed cost is partly mitigated by the design effort because the design effort is higher in strategy MH (Proposition 3). The trade-off between the benefit of delaying the features to acquire more precise information and the above-mentioned costs of doing so determines the optimum upgrade strategy. When the demand spread parameter $\zeta$ is large, it is clear that providing upgrades when the high-demand realization occurs is profitable. The extra expected profit in the high-demand realization also makes it optimum to upgrade when the demand is moderate.

Another way of interpreting this insight is from the perspective of the value of information. To implement strategy MH, the software provider requires information on the high-, medium-, and low-demand realizations. However, to implement strategy H, the software provider requires only coarse information because information on whether moderate or low demand occurred is not relevant. Therefore the value of information is much higher for strategy MH when compared to strategy H. When the spread is high, the precise information the software provider acquires about the second-period demand is more valuable. Strategy MH benefits more from this increased information value and the software provider delays the introduction of features to the second period. The value of information covers the increased costs of strategy MH discussed above.

When the word-of-mouth effect is high, the software provider’s choice between the two alternative strategies is not impacted by the spread. The following proposition summarizes this result.

Proposition 5. If the word-of-mouth effect is high $( \lambda \ge b _ { 2 } / ( \delta \theta ) )$ , the choice between upgrade strategies H and MH does not depend on the second-period demand spread parameter $\zeta .$

Proposition 5 shows that spread becomes irrelevant if the software provider can impact the second-period demand considerably through initial features. In this case, the software provider offers the maximum initial features and there is no trade-off between the initial features and upgrades (Proposition 1.2). The only remaining trade-off is between the second-period fixed costs and second-period revenue. If the fixed development cost is low (high) enough, the optimum upgrade strategy is MH (H). More importantly, the demand spread is not relevant.

This result provides two important insights for software engineering. First, the result is relevant in settings where the supply of requisite skilled labor places hard constraints on the initial features. In essence, if it is not possible to incorporate many features in the initial release because of lack of manpower, i.e., $q _ { 1 } ^ { \mathrm { m a x } }$ is sufficiently small, the demand spread need not be considered for upgrades. Second, when the word-of-mouth effect is sufficiently large, the demand spread need not be considered for upgrades either. This is likely to happen with products with large network externality effects such as a word processor.

In addition to the fact that the optimum choice is not affected by the spread parameter $\zeta ,$ the optimum choice between strategies MH and H will not revert back to H once it is MH. If strategy MH has higher profit than strategy H for any given level of the word-of-mouth effect, the dominance of strategy MH will continue for higher values of the word-of-mouth effect. This is stated in the following corollary.

Corollary 1. If the word-of-mouth effect is high $( \lambda \ge b _ { 2 } / ( \delta \theta ) )$ , the profit difference between upgrade strategies MH and H is strictly increasing in the word-ofmouth-effect .

## 6.2. Optimum Upgrade Design Effort

Next, we examine the impact of uncertainty (p) on the optimum upgrade design effort. Note that as $p$ increases, uncertainty decreases because the medium demand becomes more likely and the two extreme demand levels become less likely. Proposition 6 provides the result.

Proposition 6. (1) When upgrade strategy H is optimum, upgrade design effort increases with the uncertainty of the second-period demand. Technically, $i f z ^ { \mathrm { H } } = 1$ , then $\dot { \partial } y ^ { \mathrm { H * } } / \partial p < 0$

(2) When upgrade strategy MH is optimum, upgrade design effort decreases with the uncertainty of secondperiod demand. Technically, $i f z ^ { \mathrm { M H } } = 1$ , then $\partial { \bf { \bar { y } } } ^ { \mathrm { M { \bar { H } } * } } / \partial p > 0 .$

Proposition 6.1 shows that when upgrade strategy H is optimum, the software provider’s upgrade design effort increases with the uncertainty in the second-period demand. The intuition here is that for upgrade strategy H, the value of information is low (see the discussion of Proposition 4) and the increase in uncertainty is mitigated through the design effort. The high-demand level is more likely to occur as uncertainty increases $( p$ decreases) and more upgrade effort is optimum, leading to a higher $y ^ { \mathrm { H * } }$ . Proposition 6.2 shows that if upgrade strategy MH is optimum, the upgrade design effort decreases with the uncertainty in the second-period demand, the exact opposite of what happens in the upgrade strategy H. When the optimum upgrade strategy is MH, the value of information is high. Consequently, increase in uncertainty is not mitigated through the design effort. Because the low-demand level is more likely to occur as uncertainty increases $( p$ decreases), less upgrade effort is invested, leading to a lower $y ^ { \mathrm { M H * } }$ This provides an important insight into software design effort. Specifically, the effect of increases in uncertainty depends on the optimum upgrade strategy. If upgrades are optimum for high-demand realizations, then upgrade effort is positively related to increases in uncertainty; and if upgrades are optimum for demand realizations that are moderate, upgrade effort is negatively related to increases in uncertainty.

## 6.3. An Illustration of the Strategic Upgrade Effect

We provide numerical examples for the following reasons. We relax Assumptions A1 and A2 to illustrate that insights gleaned from the previous propositions apply to more general settings where all upgrade strategies are possible. We also provide additional insights into the impact of uncertainty and demand spread on the choice of upgrade strategy. Furthermore, we highlight the real options effect: as the uncertainty increases, the expected profit from upgrade strategies also increases. Our objective is to provide additional insights with the numerical examples that were not possible to deduce analytically.

For the numerical examples, we consider the following baseline values that are scaled from our experience with software projects: $a = 0 . 1 , b _ { 1 } = 5 , 0 0 0 ,$ $\stackrel { \textstyle > } { b _ { 2 } } = 1 0 0 , c = 0 . 5 , c _ { 0 } = 0 . 5 , \stackrel { \textstyle > } { x } _ { 1 } = 0 . 5 \times 1 0 ^ { 6 } , \stackrel { \textstyle > } { x } _ { 2 } = 1 . 5 \times 1 0 ^ { 6 }$ $K _ { 1 } = 1 0 ^ { 6 } , \ K _ { 2 } = 0 . 5 \times 1 0 ^ { 6 } , \ \alpha = 1 0 0 , \ \beta = 1 0 ^ { - 3 } , \ \delta = 0 . 8 _ { I }$ $\gamma = 1 0 ^ { - 3 } , \lambda = 2 , 0 0 0 , \theta = 0 . 0 2 ,$ and $s = 1 0 ^ { 6 }$ . The relevant parameters are chosen such that the fixed development cost $( K _ { 1 } )$ , feature creation cost $( b _ { 1 } q _ { 1 } )$ , integration cost $( b _ { 2 } q _ { 1 } ^ { 2 } )$ , and learning cost $( c ( x _ { 1 } + \delta ( x _ { 2 } + \lambda q _ { 1 } ) ) )$ are comparable in magnitude at around 10<sup>6</sup> (Matson et al. 1994). This also makes the base demand because of the word-of-mouth effect $( \lambda q _ { 1 } )$ comparable in magnitude to the second-period mean demand $( \bar { x } _ { 2 } ) ,$ which is chosen to be around three times the original demand $x _ { 1 } .$ The discount rate $( \delta = 0 . 8 )$ is chosen to be 25%, representative of a situation where an upgrade is offered within two or three years. The optimum values of the first-period features (q - vary between 100 and 300 in this example.

We first study the effect of demand spread (- and the word-of-mouth effect (- on the software provider’s profit and plot the results in Figure 1. As the demand spread () increases, the optimum upgrade strategy changes from N, to $\mathbf { H } ,$ and then to MH. This trend matches the results from Proposition 4, which states that the optimum upgrade strategy changes from H to MH when the spread  becomes large enough. The always-upgrade strategy A is never optimum in this example because the low demand in the second period is too small to provide an upgrade. The never-upgrade strategy N is the benchmark where the software provider does not consider upgrades. In this scenario, the software provider makes the development decision in the first period based purely on the expected second-period demand without considering the option to upgrade. This strategy is optimum only when the demand spread is low and the profit will remain the same regardless of the demand spread. That is why the profit curve is flat initially. When  becomes sufficiently high, it is important to consider the strategic value of investing in design effort: investing in upgrade design effort creates flexibility for the software provider to offer upgrades. By delaying the development decision until more precise information on market demand is available, software upgrades provide a device for software providers to enhance profits and cope with demand spread. As shown in Figure 1, such strategic thinking becomes more profitable as $\zeta$ increases.

Figure 1 Impact of Demand Spread - and Word-of-Mouth Effect  on the Provider’s Profit  
![](/api/attachments/4EFAVQYY/fulltext/images/a002b31d3798cb380d10746b1fae1994b27732cfbcebd98daa982e839fa70c6c.jpg)  
Note. Solid line:  2000; dotted line:  1500

In Figure 1, we have also examined the impact of the word-of-mouth effect  on the optimum upgrade strategy. The dotted line represents the profit curve with $\bar { \lambda } = 1 , 5 0 0$ and the solid line represents one with $\lambda = 2 , 0 0 0$ . As  goes from 1,500 to 2,000, the software provider’s expected profit shifts up: a higher is more beneficial to the software provider. Also, a higher  makes the H strategy optimum even for a high . To see why, we first have $q _ { 1 } ^ { \mathrm { M H * } } < q _ { 1 } ^ { \mathrm { H * } }$ both from our numerical results and Proposition 2.3, which holds in this case. Therefore, an increase of  by the same amount leads to a higher incremental profit for H than for MH strategy. An insight from this result is that, as the word-of-mouth effect increases, software providers should focus on creating higher future demand through the word-of-mouth effect rather than on trying to plan for upgrades over a wide range of demand realizations, i.e., software providers might need to switch from MH to H when  increases. This insight appears to run counter to the intuition when the word-of-mouth effect is relatively high. Note that when the word-of-mouth effect is relatively high, Proposition 2.1 holds. In that case, as the word-ofmouth effect increases, the optimum choice between strategies MH and H will not revert back to H once it is MH, as shown in the corollary of Proposition 5. The trade-offs are intricate here and need to be carefully analyzed. When the word-of-mouth effect is low, as it is in this example, Proposition 2.3 applies; the upgrade strategy needs to weigh the word-of-mouth effect more heavily.

We also examine the impact of the probability of demand uncertainty (p) on the upgrade profit. The dotted line represents the case where $p = 0 . 2$ and the solid line $p = 0 . 3$ . A lower p means that demand is concentrated less at the medium demand level and there is more demand uncertainty. As we can see in Figure 2, demand uncertainty increases as p goes from 0.3 to 0.2 and the software provider’s expected profit increases. It may seem counterintuitive that the software provider’s expected profit is higher when there is more uncertainty, although the expected demand is the same. The explanation is based on the real options effect (Dixit and Pindyck 1993). As p decreases, the likelihood of high demand increases. If the software provider chooses the upgrade design effort and features by considering upgrades as a strategic tool, then delaying the upgrades until demand is realized creates value. Thus, upgrades are a real option and the cost of the option is the upgrade design effort: the software provider incurs an upgrade effort cost (the cost of the option) and if the high demand occurs (the option is in the money), then the software provider offers upgrades. Consequently, the profits increase as the uncertainty increases.

Figure 2 Impact of Demand Spread - and Uncertainty Probability p on the Provider’s Profit  
![](/api/attachments/4EFAVQYY/fulltext/images/ffb4c748c3e9f524ae535353b4682dba2c26a25490e59e708dec576cdae68bdc.jpg)  
Note. Solid line: $p = 0 . 3 ;$ dotted line: $p = 0 . 2$

## 6.4. Limitations and Extensions

Recall that our demand model is aggregate in nature: there is a pool of customers who adopt the initial product and a separate pool of potential customers who may adopt the upgraded product. The second-period demand level is partially impacted by the word-of-mouth effect through herding behavior. Thus, in our aggregate demand model, the variance of the second-period demand always increases with the word-of-mouth effect. This is consistent with the main motivating example—the aerospace firm we discussed in the introduction.

It is conceivable, however, that in an individual customer-level model, the word-of-mouth effect may reduce demand variance. Consider a market in which there is a pool of potential second-period customers of size n each with a positive probability $( P _ { r } )$ of purchasing the upgrade. Suppose that existing customers talk to each other and create a buzz about the product and increase each potential customer’s probability of purchase. Because the variance of demand is equal to $n P _ { r } ( 1 - P _ { r } )$ , it is easy to see that the word-ofmouth effect would, by increasing the purchase probability, increase the variance for low values of the probability of purchase $( P _ { r } < 1 / 2 )$ and decrease the variance for high values of the probability of purchase $( P _ { r } > 1 / 2 ) . ^ { 2 1 }$ Even though individual customerlevel modeling is not how we construct demand, it is important to discuss the implications of buzz generated among customers when they discuss new products. Because our aggregate approach does not model the probability of individual purchase, we resort to a proxy model to explore this alternative and summarize the results of this model in the online appendix. In Proposition $^ { 4 , }$ we find that as the expressions for the optimal initial and upgrade features change, so does the cutoff value of the demand spread parameter $( \zeta ^ { * } ) ;$ however, the statements and the proofs of our main propositions and observations continue to hold as before. In our current model, both the wordof-mouth effect and the demand spread parameter  increase the total demand variance In the alternative model, because a high word-of-mouth effect could possibly decrease the demand variance, the regions of optimality for the various upgrade strategies change. In this case, the word-of-mouth effect and demand spread parameters will act in opposite directions. The impact of this change is best explained using Table 1 provided in the next section. In the case that the wordof-mouth effect reduces the demand variance, the cutoff value for the demand spread parameter goes up and the shift to strategy MH from strategy H requires a higher value of the demand spread parameter . Therefore, while our results do change in the alternative model when the word-of-mouth effect reduces the demand variance, the change occurs in a predictable and expected manner.

## 7. Discussion and Conclusions

We examined a two-period software release upgrade model where the initial features, upgrades, and upgrade design efforts for a software product are chosen in a strategic manner. We summarize our main results in Table $1 . ^ { 2 2 }$ First, we relate the optimum upgrade strategy to the word-of-mouth effect and the demand spread parameters ( and -. Then, we report how the optimum values of the initial product features $( q _ { 1 } ^ { * } )$ and the upgrade design effort (y∗- change accordingly.

The optimum strategy moves from H to MH when either of the two parameters ( or $\zeta )$ increases. This is because of the increase in the value of information from using software upgrades strategically; the value of information increases when the demand spread $\zeta$ increases. With more variability, it is worth more to wait for precise demand information. It becomes clear why the same happens when the word-ofmouth parameter  increases by noting that the wordof-mouth parameter increases the variance of the demand. Thus, its impact on the optimum upgrade strategy is similar to that of the spread parameter, as Table 1 clearly shows.

Table 1 Summary of the Optimum Upgrade Stragegies

<table><tr><td rowspan="2">Word-of-mouth effect (λ)</td><td colspan="2">Variability (ζ)</td><td rowspan="2">Relationship of  $q_{1}^{*}$  and  $y^{*}$ </td><td rowspan="2"></td></tr><tr><td>High</td><td>Low</td></tr><tr><td>High</td><td> $\Omega^{*} = MH$  $q_{1}^{*} = \max$  $y^{*} = \text{high}$ </td><td> $\Omega^{*} = MH$  $q_{1}^{*} = \max$  $y^{*} = \text{high}$ </td><td>Complements</td><td>Prop. 2.1Prop. 3Prop. 5</td></tr><tr><td>Medium</td><td> $\Omega^{*} = MH$  $q_{1}^{*} = \text{high}$  $y^{*} = \text{high}$ </td><td> $\Omega^{*} = H$  $q_{1}^{*} = \text{low}$  $y^{*} = \text{low}$ </td><td></td><td>Prop. 2.2Prop. 3</td></tr><tr><td>Low</td><td> $\Omega^{*} = MH$  $q_{1}^{*} = \text{low}$  $y^{*} = \text{high}$ Prop. 4.2</td><td> $\Omega^{*} = H$  $q_{1}^{*} = \text{high}$  $y^{*} = \text{low}$ Prop. 4.1</td><td>Substitutes</td><td>Prop. 2.3Prop. 3</td></tr></table>

Under the condition that the demand spread is low, the strategy H is optimum when the wordof-mouth effect is low or moderate, while strategy MH is optimum when the word-of-mouth effect is high. However, when the demand variability is high, regardless of the size of the word-of-mouth effect, the firm should offer upgrades for both medium- and high-demand levels. In the relationship between the initial features and new features in the upgrade, the demand endogeneity (the impact of initial features on future demand through the word-of-mouth effect) plays a key role. The initial features and upgrade features are complements and move in consonance when the demand endogeneity is sufficiently high (corresponding to Rows 1 and 2 of Table 1), and become substitutes when the demand endogeneity is sufficiently low (Row 3). We also find that when the demand endogeneity is sufficiently small, the software provider can reduce the quantity of initial features when it is more likely that upgrades will be offered. To prepare for a more likely upgrade, the provider will increase upgrade design effort (Row 3). This substitution effect is reversed for sufficiently high levels of endogeneity where the two effort quantities (development and upgrade design) become complements (Rows 1 and 2). Overall, we show that incorporating strategic upgrades in software design decisions, and choosing initial features and upgrade levels accordingly, have the potential to enhance the software provider’s profits considerably.

We note the important implications of this study. From a software engineering perspective, we find that development and upgrade design decisions depend crucially on market conditions: on the one hand, when future demand is sensitive to the current success of the product, more features are offered, and more interestingly the level of upgrade design effort is also increased. Therefore, software providers offering products where buzz is important should invest more in upgrade design effort. On the other hand, when the demand is more of a function of external factors such as economic conditions or changing customer characteristics, a more traditional view of software production applies where upgrade design effort is sacrificed for the sake of providing more features. Overall, these findings highlight the link between production-side and demand-side forces in commercial software design. From a strategy perspective, software providers must pay careful attention to both the level of demand variability and the upgrade strategy being pursued to decide on the level of upgrade design effort. As such, the level of upgrade design effort as a function of the demand variability cannot be evaluated in isolation of the upgrade strategy. Both these implications, namely, the software engineering perspective and the strategy perspective, are ultimately a result of the intricate impact of demand endogeneity on the production and commercialization of software.

The optimum upgrade strategy studied in this paper provides some useful empirical implications. Our analysis cautions that comparing the profitability across two software products with different future demand variability. If the future demand spread is large for one product and small for another, then the optimum upgrade strategies will need to be different. When the demand spread is high, our findings indicate that the strategy to offer upgrades when the demand is moderate and high yields a higher profit than that of providing upgrades only when the demand is high. Thus, choosing upgrade strategies simply by comparing the profits without controlling for the variance in demand may result in inappropriate conclusions.

Another important insight for managers is the role played by the word-of-mouth effect on software engineering decisions. A high value of the word-of-mouth effect acts to increase the mean value of the secondperiod demand, but at the same time also increases the spread of this demand. Managers should therefore pay particular attention to this factor because it can significantly impact the functionality of the product during its initial release, as well as the likelihood of whether or not an upgrade will be offered. Overall, the word-of-mouth effect acts to counter the presence of variability in the second-period demand. The main implication of this finding is that product management decisions such as advertising and promotions should be undertaken in cohort with software engineering decisions.

We note some limitations of this study. The model we studied collapsed the future into the second period approximating a world where the future obviously consists of many periods. However, two-period models are usually adequate to generate important insights that will likely carry over to a multiperiod setting. Also, a two-period model is more realistic when software providers can predict only the nearterm future. For example, although the joint planning of Windows 98 and Vista would have been useful, such an activity is almost infeasible given how rapidly IT can change over time. As a case in point, it is well known that Microsoft had to scrap the original codebase for Windows 98 and start the Vista development anew. Another limitation is that the market is assumed to consist of customers who are homogeneous in their evaluation of product features. A challenging extension is to jointly consider customer heterogeneity and demand variability, taking us into the situation of planning the simultaneous release of product editions in addition to planning sequential versions.

The model in the current study can be extended to study the management of software product lines where the focus has been on reusing software components (Yacoub 2002). It is more expensive to build individual components that can be reused in related software products; however, the reward of the successful reuse of software components could be remarkable: improving system reliability, increasing productivity, and reducing product cycle time. The decision of how much effort to put into building reusable components has to depend on factors such as the portfolio of the product line and the future growth of related software products, and can be examined as part of the strategic upgrade potential. Specifically, should reusable components be part of the initial release or a later release?

Another avenue for future research relates to organizational issues such as incentives driving the behavior of programmers and software providers. For example, how should a software provider’s performance be evaluated when the cost of investing in upgrade design effort has to come from the development budget of current projects (Lynex and Layzell 1998)? Also, as the practice of outsourcing software projects becomes more prevalent, developers for existing and future projects could be different. How can a company design a contract to provide appropriate incentives to the current developers in terms of sharing the strategic upgrade benefits that could arise in the future, so that the current developers are willing to invest upgrade design efforts for the benefit of future projects?

The model can be further extended to examine a duopoly setting with two software providers. In this case, the word-of-mouth effect and demand variability can be made interdependent across two products. In a competitive market, each firm’s allocation of the product features over two periods and the distribution of each firm’s development and upgrade design efforts would be restricted by its rival’s actions. The duopoly setting would limit the firm’s ability to control demand uncertainty, but would provide new insights into how the initial features and upgrades can be used for both competitive as well as software engineering reasons.

## 8. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

The authors thank Senior Editor Seungjin Whang, the associate editor, and anonymous reviewers for their valuable comments that have led to many significant improvements to this paper.

## References

Benaroch, M., R. J. Kauffman. 2000. Justifying electronic banking network expansion using real options analysis. MIS Quart. 24(2) 197–225.

Biyalogorsky, E., E. Gerstner, B. Libai. 2001. Customer referral management: Optimal reward programs. Marketing Sci. 20(1) 82–95.

Cakanyildirim, M., T. Dalgic. 2002. Using demonstration to promote information products. Working paper, University of Texas at Dallas. http://www.utdallas.edu/ metin/Research/ demonstration.pdf.

Chellappa, R. K., S. Shivendu. 2005. Pricing and sampling strategies for digital experience goods in vertically segmented markets. Inform. Systems Res. 16(4) 400–417.

Desai, P., S. Kekre, S. Radhakrishnan, K. Srinivasan. 2001. Product differentiation and commonality in design: Balancing revenue and cost drivers. Management Sci. 47(1) 37–51.

Dixit, A. K., R. S. Pindyck. 1993. Real Options Under Uncertainty. Princeton University Press, Princeton, NJ.

Dos Santos, B.L. 1991. Justifying investment in new information technologies. J. Management Inform. Systems 7(4) 71–89.

Ellison, G., D. Fudenberg. 2000. The neo-luddite’s lament: Excessive upgrades in the software industry. RAND J. Econom. 31(2) 253–272.

Faugère, C., G. K. Tayi. 2007. Designing free software samples: A game-theoretic approach. Inform. Tech. Management 8(4) 263–278.

Forbes. 1984. The hard sell; American consumers will try almost anything once. (November 5).

Harter, D. E., M. S. Krishnan, S. A. Slaughter. 2000. Effects of process maturity on quality, cycle time, and effort in software product development. Management Sci. 46(4) 451–466.

Krishnan, M. S., S. Kekre, C. H. Kriebel, T. Mukhopadhyay. 2000. An empirical analysis of productivity and quality in software products. Management Sci. 46(6) 745–759.

Kumar, R. 1996. A note on project risk and option values of investments in information technologies. J. Management Inform. Systems 13(1) 187–193.

Lethbridge, T., J. Singer A. Forward. 2003. How software engineers use documentation: The state of the practice. IEEE Software 20(6) 35–39.

Lynex, A., P. J. Layzell. 1998. Organizational considerations for soft ware reuse. Ann. Software Engrg. 5 105–124.

Manica, D., S. Menon, V. Mookerjee. 2007. Design of an optimal software demonstration. Working paper, University of Texas at Dallas.

Matson, J. E., B. E. Barrett, J. M. Mellichamp. 1994. Software development cost estimation using function points. IEEE Trans. Software Engrg. 20(4) 275–287.

Mookerjee, V., R. Chiang. 2002. A dynamic coordination policy for software system construction. IEEE Trans. Software Engrg. 28(7) 684–694.

Moorthy, K., I. Png. 1992. Market segmentation, cannibalization, and the time of product introduction. Management Sci. 38(3) 345–359.

Padmanabhan, V., S. Rajiv, K. Srinivasan. 1997. New products, upgrades, and new releases: A rational for sequential product introduction. J. Marketing Res. 34 456–472.

Raghunathan, S. 2000. Software editions: An application of segmentation theory to the packaged software market. J. Management Inform. System 17(1) 87–113.

Shapiro, C. 1982. Consumer information, product quality, and seller reputation. Bell J. Econom. 13(1) 20–35.

San Francisco Chronicle. 1995. Online banking race begins. (May 22).

Sullivan, K. J., P. Chalasani, S. Jha, V. Sazawal. 1999. Software design as an investment activity: A real options perspective. L. Trigeorgis, ed. Real Options and Business Strategy: Applications to Decision Making. Risk Books, London.

Taudes, A. 1998. Software growth options. J. Management Inform. Systems 15(5) 165–185.

Wall Street Journal. 1993. Strategic shift: A slump in car sales forces Nissan to start cutting swollen costs. (March 3).

Yacoub, S. 2002. Performance analysis of component-based applications. G. Chastek, ed. Proc. Second Internat. Conf. Software Product Lines (SPLC), San Diego, Lecture Notes in Computer Science, Vol. 2379. Springer-Verlag, Berlin, 299–315.
