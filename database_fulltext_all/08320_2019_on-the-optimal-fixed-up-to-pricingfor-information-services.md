---
otero_id: 8320
otero_key: "QV6EE6Q9"
title: "On the Optimal Fixed-Up-To Pricingfor Information Services"
authors: "Shinyi Wu; Paul Pavlou"
year: "2019"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00574"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Optimal Fixed-Up-To Pricing for Information Services

Shinyi Wu<sup>1</sup>, Paul Pavlou<sup>2</sup>

<sup>1</sup>Arizona State University, USA, shinyi.wu@asu.edu <sup>2</sup>The University of Houston, USA, pavlou@bauer.uh.edu

## Abstract

Fixed-up-to (FUT) pricing allows consumers to purchase a fixed usage amount of an information service for a certain fixed price chosen from a set of options. In this study, we derive an optimal analytical solution for FUT pricing without imposing the strong single-crossing assumption. Further, we illustrate the analytical solution by leveraging mixed integer nonlinear programming to derive an optimal FUT pricing scheme for information services and also investigate when and by how much FUT pricing improves upon commonly used “flat rate” pricing. Our numerical results show that FUT pricing improves the service provider’s profits while enhancing social welfare when consumers face different maximum consumption-level bounds. Notably, in terms of optimal pricing, our numerical results show that the consumers’ maximum consumption-level bounds are more important than their utility functions. Most importantly, our results show that FUT pricing performs better than flat rate pricing under conditions of incomplete information. Finally, we empirically show that it is not necessary to treat over-the-limit rates as a decision variable in terms of optimal FUT pricing since both FUT pricing and three-part tariffs are reasonable approximations of nonlinear pricing in terms of both firm profits and social welfare. We conclude with a discussion of theoretical and practical implications for the design of optimal FUT pricing in terms of enhancing firm profits, consumer surplus, and social welfare.

Keywords: Pricing, Nonlinear Mixed Integer Programming, Information Services, Fixed-Up-To (FUT) Pricing.

Hsing Kenneth Cheng was the accepting senior editor. This research article was submitted on January 19, 2017, and underwent three revisions.

## 1. Introduction

Identifying the best pricing strategies for information services is a major problem for firms, given the wide variety of information services available, such as ondemand web services, mobile services, voice, cellular data, SMS/MMS, and cable TV. One of the most salient and unique characteristics of information services is that with enough capacity, the marginal cost of offering information services is negligible (nearzero or zero). Thus, flat rate pricing is a more attractive strategy for firms than usage-based pricing (e.g., Oi, 1971; Fishburn, Odlyzko, & Siders, 1997; Essegaier, Gupta, & Zhang, 2002; Randhawa & Kumar, 2008; Wu & Banker, 2010; Cachon & Feldman, 2011). However, a relatively recent pricing scheme that is increasingly used by information service providers in practice is termed “fixed-up-to (FUT)” pricing. For example, Verizon Wireless offers cellular data plans using FUT pricing options of \$30 (1GB), \$45 (3GB), \$60 (6GB), \$80 (12GB); Disney Cruise Lines offers onboard Internet plans offering plans at \$19 (100MB), \$39 (300MB), \$89 (1000MB). <sup>1</sup> FUT pricing is different from flat rate pricing, traditional pure usagebased pricing (without a subscription fee), and twopart tariff pricing (usage-based pricing plus a subscription fee) in that FUT pricing allows consumers to select their desired level of consumption from a “menu” of price options.

FUT pricing has a number of benefits for both firms and consumers, compared to usage-based pricing. FUT pricing reduces utility variance by bundling plan units, thus satisfying diverse consumer needs and potentially enhancing firm profits. FUT pricing also has a key advantage over flat rate pricing; by having more than one price point, FUT pricing also allows firms to efficiently accommodate heterogeneous consumer needs, potentially increasing total social welfare (combination of firm profit and consumer surplus). However, since FUT menu pricing is generally more difficult than flat rate pricing to implement in practice, it is useful to understand “when” and “by how much” FUT pricing can perform better than flat rate pricing in terms of firm profits, consumer surplus, and social welfare. Therefore, we aim at deriving an optimal solution for FUT menu pricing to both extend the literature on the pricing of information services and also to enhance managerial practice by testing our model with sophisticated analytical and empirical techniques.

FUT menu pricing resembles traditional quantity discount pricing for physical goods (e.g., Monahan, 1984; Lee & Rosenblatt, 1986; Munson & Rosenblatt, 1998; Corbett & Groote, 2000; Shin & Benton, 2004) in the sense that the unit price for a larger plan is often discounted. However, in contrast to its popularity for information services, flat rate pricing is not as popular for physical goods, perhaps because of the positive marginal cost associated with each unit of a physical good. As a result, despite the practical importance of optimally pricing information services to maximize firm profit while minimizing deadweight loss, there is no clear guidance from the literature on quantity discounts that firms can use to determine when to use flat rate pricing versus FUT pricing. In managerial practice, many firms indeed struggle to find the best strategies to price their information services, evidenced by the wide variety of pricing strategies used by various firms. For example, Cox

Communications charges a monthly flat rate for its Internet services. Netflix similarly uses a monthly flat rate pricing for its unlimited streaming service. In contrast, Celebrity Cruises uses FUT pricing menu for onboard Internet access, while Verizon Wireless uses FUT pricing for its cellular data service.

However, it remains unclear how the design of FUT pricing menus can be optimized, and the effects of FUT pricing on firm profits and consumer surplus have not been adequately examined in either theory or practice.<sup>2</sup> In this study, we aim to derive an optimal FUT pricing strategy for monopoly information service providers. In practice, there are numerous monopoly information service providers. For example, leading social networking sites such as Facebook and Twitter have secured a unique monopoly position for the types of information services they offer. While many of these sites currently offer their services to consumers free of charge, the strategic reasons for doing so perhaps are to attract traffic, build network externalities, and adopt an advertising-supported business model. They may decide to charge consumers for their services in the future.<sup>3</sup> Another example is Gogo Inflight Internet, which has successfully created a monopoly environment on airplanes, since passengers on most airlines do not have access to any other Internet services while flying. Similarly, Internet services offered on many cruise ships are examples of monopoly information services providers. In the area of online auctions, eBay is a local monopolist. In multiple regions that offer a single cable TV provider, cable companies also enjoy monopoly power, and are often criticized for poor services and skyrocketing rates. Therefore, the assumption of a monopoly information service provider is valid in many practical real-life contexts.

In the literature on the pricing of information services, Masuda and Whang (2006) were among the first to analytically study FUT pricing. However, although they analytically derived an optimal FUT menu for two types of consumers, they had to employ a strict singlecrossing assumption. While this assumption is convenient for analytical work, it is unlikely to hold in practice, as the authors acknowledge (p. 252). In the current study, we extend the pricing literature by analytically demonstrating that FUT pricing could be more profitable even when the single-crossing assumption does not hold. Then, we include consumer heterogeneity assumptions in our general model and use a mixed integer nonlinear program (MINLP) to identify the optimal FUT pricing strategy for information services. By using a numerical solution approach, we can examine the performance of FUT pricing in typical practical scenarios that are not tractable analytically, such as scenarios without the strict single-crossing assumption and those with more than two consumer types. We then extend the pricing literature by examining the performance of FUT pricing not only in terms of firm profits, but also in terms of consumer surplus and social welfare.

Information service providers seldom understand the exact nature of their consumers’ utilities in practice, and this uncertainty is best captured by utility distribution forecasts. While it is possible for an information service provider to amply forecast some general consumer utility distributions, identifying precise consumer utilities is very costly in practice. We thus examine the value of complete information concerning consumer utility on the performance of FUT pricing, while our MINLP numerical solution provides direct insight into this important and practical topic.

Finally, following Masuda and Whang (2006), we initially assume that all FUT consumers will stay within their allowed usage amounts most of the time. Masuda and Whang argue that over-the-limit rates do not play a critical role, as long as they are high enough. In practice, high over-the-limit rates are used as a penalty for over-the-limit usage, and they are typically at least 3-4 times more than the average rates of the allotted plan (e.g., in Verizon Wireless plans). We question whether this practice is a good idea or whether firms should also treat over-the-limit rates as decision variables and employ a “three-part tariff”—comprising plan price, usage allotment, and an over-the-limit rate. We conclude our analysis by examining how FUT pricing and a three-part tariff perform compared to a nonlinear pricing scheme, in which each usage level is charged a different and nonlinear price.

In sum, the following research questions guide our study:

1. When is FUT pricing a better option (compared to the popular flat rate pricing), and by how much? Simply knowing whether FUT pricing is better may not be sufficient because FUT menu pricing is generally more difficult to implement in practice.

2. If consumers have heterogeneous preferences, how well does FUT pricing perform over flat rate pricing in terms of overall social welfare (firm profits combined with consumer surplus)?

3. Does incomplete information really matter for FUT pricing? Or conversely, how much is complete information about consumer utility worth in terms of FUT pricing?

4. Should firms treat over-the-limit rates as decision variables, and how do FUT pricing and three-part tariffs perform, as compared to nonlinear pricing schemes?

Our results indicate that for optimal FUT menu pricing, the maximum consumption-level bound is more important than the consumers’ utility functions. In our study, regardless of their utility functions, when consumers have different maximum consumptionlevel bounds, FUT pricing dominates flat rate pricing in terms of both the firm’s profits and social welfare. Our results also show that FUT pricing clearly dominates flat rate pricing under incomplete information, and that FUT pricing performs equally well as the three-part tariff in terms of both firm profits and social welfare, which are both reasonably good approximations of nonlinear pricing. Taken together, this study contributes to the pricing literature on information services by guiding the design of FUT pricing and showing its positive effects on firm profits and social welfare.

The paper proceeds as follows: Section 2 reviews the literature on the pricing of information services. Section 3 presents our base model formulation, followed by the general model in Section 4. We present numerical results and case analyses in Section 5, followed by implications for theory and practice in Section 6.

## 2. Literature Review

We review the pricing literature in the context of information services, starting with the earlier literature on computer services in the early 1980s, followed by networked and Internet services in the 1990s, and concluding with some relevant research on information services in the late 1990s and 2000s.

Early on, Mendelson (1985) and Mendelson and Whang (1990) used queuing models in the pricing of computer services. Dewan and Mendelson (1990) studied congestion pricing with user delay costs in service facilities. Also, Stahl and Whinston (1994) developed an economic model for client-server computing pricing with priority classes, while MacKie-Mason and Varian (1995) used dynamic auctions to price the Internet. Dewan (1996) examined the computer service pricing under a variety of control structures. However, none of these studies considered FUT pricing for the pricing of IT-related services.

Gupta, Stahl, and Whinston (1996, 1997) developed an optimal pricing model for networked services. In their model, the authors ensured that incoming service requests could only be submitted when their utility is higher than the congestion-based price and loss of utility (such as additional waiting cost) imposed on the job requests already in the system. Gupta, Jukic, Parameswaran, Stahl, and Whinston (1997) and Gupta, Jukic, Stahl, and Whinston (2000) combined a congestion pricing scheme and demand estimation to ensure that their pricing scheme is incentive compatible. Konana, Gupta, and Whinston (2000) studied dynamic priority pricing and showed that it outperforms other priority rules. Nadiminti, Mukhopadhyay, and Kriebel (2002) studied resource allocation with asymmetric information and negative externalities. Afeche and Mendelson (2004) developed a novel generalized delay cost model that is interdependent of consumer value. Bhargava and Sun (2008) examined how performance-contingent pricing schemes with long-term statistical performance guarantees can be applied to many IT services. Finally, Gupta, Jukic, Stahl, and Whinston (2011) studied longterm network capacity investments under different pricing strategies. Again, all these studies mostly focused on congestion-based negative externality pricing and did not consider FUT pricing.

Extending the literature on the pricing of IT-related services (e.g., computing and networked), several recent studies have examined different popular pricing schemes specifically for information services. The most relevant studies to our work are Fishburn et al. (1997), Essegaier et al. (2002), Sundararajan (2004) and Masuda and Whang (2006). Fishburn et al. (1997) studied flat rate and usage-based pricing, and they showed that flat rate pricing is generally better than usage-based pricing for a monopoly information service provider. Nevertheless, they simplified their analytical model with some quite restrictive assumptions. For instance, they assumed that consumers decide on the amount of the information service they want to buy and stick to it before checking the price, which is unlikely to apply in practice. However, it is not clear whether their results would generalize to the more general downward sloping demand functions, which are considered in this study for FUT pricing. Essegaier et al. (2002) also considered flat rate pricing and usage-based pricing, and they showed that flat rate pricing is a sustainable pricing structure once the industry has sufficient capacity. However, as in Fishburn et al. (1997), they also assumed that consumer usage is inelastic to price changes. In addition, the authors assumed that both heavy and light consumers have the same total reservation price for the same service. This could be a questionable assumption, as consumers usually have quite different and diminishing marginal utility for each unit of information service they use. Although they extended their model by adopting the same unit reservation price for these two consumer types, their assumption still did not capture the fact that consumers usually have different and diminishing marginal utility for each unit of service they use. We explicitly include consumer heterogeneity and diminishing marginal utilities in our model. Sundararajan (2004) considered fixed-fee and nonlinear usage-based pricing to show that when there are contract administration costs, a monopoly service provider can increase its profits by offering fixed-fee pricing coupled with usage-based pricing. Still, while they suggested that a service provider could increase its profits by adopting two pricing schemes simultaneously, the results were solely based on a utility function that satisfied the Spence-Mirrlees single-crossing property (Fudenberg & Tirole, 1993), which enabled the service provider to segment consumers profitably through consumer selfselection. However, if the single-crossing property does not hold, it is not clear if the two schemes together would enhance profits.

In the literature, Masuda and Whang (2006) were among the first to analytically study FUT pricing. Their seminal paper inaugurated a literature on the pricing of information services, which includes work by Choudhary (2010), Huang and Sundararajan (2011), and Bagh and Bhargava (2013), among others. However, although Masuda and Whang analytically derived an optimal FUT menu for two types of consumers, they had to employ the strict singlecrossing assumption. While this assumption is convenient for analytical work, it is unlikely to hold in practice, as the authors do acknowledge (p. 252). Extending Masuda and Whang, we first seek to analytically show that FUT pricing could be more profitable, even when the single-crossing assumption does not hold. Second, by including consumer heterogeneity assumptions in our general model, we also use a mixed integer nonlinear program (MINLP) to identify the optimal FUT pricing strategy for information services. One of the major contributions of our general model is its ability to accommodate many types of consumers without any auxiliary consumer utility assumption, notably the single-crossing property.

## 3. The Base Model

We first construct the base model for the FUT pricing problem. We assume there are only two types of consumers in the market; this assumption is relaxed in the next section with a more general model. Suppose there are high-type and (1- ) low-type consumers, and the firm cannot distinguish between these two types of consumers (i.e., third-degree price discrimination is not possible in practice, and the firm has to go with second-degree price discrimination based on consumer self-selection).

Following Wu and Banker (2010), since consumers have limited time, energy, attention, and diminishing marginal utility, we assume that they face certain upper bounds when using information services, and their utility will typically stay the same beyond these bounds. This is a reasonable assumption, as virtually all information services have this property and no consumer can continue to consume a service without limit. For example, consumers cannot consume a timebased information service, such as voice communication, for more than 24 hours a day. Given limited transmission rates of the device used, traffic volume in each period is also naturally bounded for any data transmission service. SMS/MMS has the same property, as the number of uses in each period is bounded by the total time available given a positive time requirement for each use.

The high-type consumer has the utility of $U _ { H }$ for the service at and beyond her maximum consumptionlevel bound $L _ { H } ,$ which is greater than the utility, $U _ { L } ,$ , of a low-type consumer for the service at and beyond her maximum consumption-level bound $L _ { L } .$ In other words, we assume $U _ { H } > U _ { L }$ and $L _ { H } > L _ { L }$ . Building upon previous literature, we first assume a consumer’s utility for the service within her maximum consumption-level bound increases linearly from 0 to $U _ { H }$ or $U _ { L }$ , though we will relax this assumption in the general model as well.

Following Fishburn et al. (1997), Sundararajan (2004), and Wu and Banker (2010), we assume that the marginal cost of offering the information service is negligible; in the pricing literature, the marginal cost of information services is often modeled as negligible because system capacity is usually fixed and cannot be changed in the short term. A firm only faces a large “marginal cost” when it needs to increase capacity, but this is a separate long-term investment decision a firm

$$
\begin{array}{l}{U _ {H} \frac {T _ {H}}{L _ {H}} - P _ {H} \geq 0 \rightarrow P _ {H} \leq U _ {H} \frac {T _ {H}}{L _ {H}}}\\{U _ {H} \frac {T _ {H}}{L _ {H}} - P _ {H} \geq U _ {H} \frac {T _ {L}}{L _ {H}} - P _ {L} \rightarrow P _ {H} \leq U _ {H} \frac {T _ {H} - T _ {L}}{L _ {H}} + P _ {L}}\end{array}
$$

Similarly, for a low-type consumer to buy $( P _ { L } , T _ { L } )$ , we must assure the consumer that the net surplus from buying $( P _ { L } , T _ { L } )$ is greater than that from not buying at

$$
U _ {L} \frac {T _ {L}}{L _ {L}} - P _ {L} \geq 0 \rightarrow P _ {L} \leq U _ {L} \frac {T _ {L}}{L _ {L}}
$$

$$
U _ {L} \frac {T _ {L}}{L _ {L}} - P _ {L} \geq U _ {L} \min \left\{\frac {T _ {H}}{L _ {L}}, 1 \right\} - P _ {H} \rightarrow P _ {L} \leq P _ {H} - U _ {L} [ \min \left\{\frac {T _ {H}}{L _ {L}}, 1 \right\} - \frac {T _ {L}}{L _ {L}} ]
$$

would make; with a new larger capacity, the marginal cost would again become negligible. As such, it can be assumed that the short-term marginal costs of the information service provider can always be kept negligible. Capacity constraints, in fact, are more likely to affect flat rate pricing where capacity demand is likely to be higher.

Given that there are only two types of consumers (high-type and low-type), the firm will offer, at most two FUT plans: one plan with price $P _ { H }$ and plan units $T _ { H } ,$ which is intended to be sold to high-type consumers, and a second plan with price $P _ { L }$ and plan units $T _ { L }$ to be sold to low-type consumers. For simplicity, we write these two plans as $( P _ { H , } T _ { H } )$ and $( P _ { L } , T _ { L } )$ . Since consumers have the same utility beyond their maximum consumption-level bound, it is not necessary to design plans beyond those consumption bounds. In other words, we should have: $P _ { H } \leq U _ { H }$ $P _ { L } \leq U _ { L } , T _ { H } \leq L _ { H }$ and $T _ { L } \leq L _ { L }$ . It is also reasonable that $P _ { H } \geq P _ { L }$ and $T _ { H } \geq T _ { L }$

Following these assumptions, a high-type consumer will realize a net surplus $U _ { H } \frac { T _ { H } } { L _ { H } } - P _ { H }$ from buying $( P _ { H } ,$ $T _ { H } ) ;$ and realize a net surplus $U _ { H } \frac { T _ { L } } { { { L } _ { H } } } - { { P } _ { L } }$ from buying $( P _ { L } , T _ { L } )$ , since we assume a consumer’s utility for the service within the maximum consumption-level bound increases linearly from 0. We can then derive the firm’s optimal strategy. Assuming that these two plans $( P _ { H } , T _ { H } )$ and $( P _ { L } , T _ { L } )$ are offered, a high-type consumer will buy $( P _ { H } , T _ { H } ) .$ , if and only if, her net surplus from buying $\left( P _ { H } , \ T _ { H } \right)$ is greater than that yielded by not buying any plan (zero utility) or from buying $( P _ { L } , T _ { L } )$ That is, the following two constraints must hold for the high-type consumer to buy $( P _ { H } , T _ { H } )$

(1) H prefers buying $( P _ { H } , T _ { H } )$ to not buying any plan;

(2) H prefers buying $( P _ { H } , T _ { H } )$ to buying $( P _ { L } , T _ { L } )$

all (zero utility) and from buying $( P _ { H } , T _ { H } )$ . That is, the following two constraints must hold for the low-type consumer to buy $( P _ { L } , T _ { L } ) \mathrm { : }$

(3) L prefers buying $( P _ { L } , T _ { L } )$ to not buying;

(4) L prefers buying $( P _ { L } , T _ { L } )$ to buying $( P _ { H } , T _ { H } )$

![](/api/attachments/QV6EE6Q9/fulltext/images/855bd90973957b19ad17eb1733d54d31ea41e0b358d911393b3f03cfea2c358d.jpg)  
Figure 1. With Single Crossing Property

It is in the firm’s interest to increase these prices as much as possible; thus, in general, one of the first two above inequalities, (1) and (2), will be binding, and one of the latter two above inequalities, (3) and (4), will also be binding.

When $\frac { U _ { H } } { L _ { H } } > \frac { U _ { L } } { L _ { L } }$ (with single-crossing property; see Figure 1), by using proof by contradiction, we can show that constraints (2) and (3) are binding:

$$
\begin{array}{r} P _ {H} = U _ {H} \frac {T _ {H} - T _ {L}}{L _ {H}} + P _ {L} \\ P _ {L} = U _ {L} \frac {T _ {L}}{L _ {L}} \end{array}
$$

The firm’s profit function is thus:

$$
\begin{array}{r l} & {\pi = \alpha P _ {H} + (1 - \alpha) P _ {L}} \\ & {\qquad = \alpha \left(U _ {H} \frac {T _ {H} - T _ {L}}{L _ {H}} + U _ {L} \frac {T _ {L}}{L _ {L}}\right)} \\ & {\qquad + (1 - \alpha) U _ {L} \frac {T _ {L}}{L _ {L}}} \end{array}
$$

The firm will then choose $T _ { H }$ and T<sub>L</sub> to maximize its profit. Since: $\begin{array} { r } { \frac { \partial \pi } { \partial T _ { H } } = \alpha \left( \frac { U _ { H } } { L _ { H } } \right) > 0 } \end{array}$ , it is optimal that $T _ { H }$ $= L _ { H }$ . In addition, $\begin{array} { r } { \frac { \partial \pi } { \partial T _ { L } } = - \alpha \frac { U _ { H } } { L _ { H } } + \frac { U _ { L } } { L _ { L } } } \end{array}$ . When $- \alpha \frac { U _ { H } } { L _ { H } } +$ $\begin{array} { r } { \frac { U _ { L } } { L _ { L } } < 0 \ \mathrm { ( i . e . } } \end{array}$ , there are many high-type consumers as: $\begin{array} { r } { \frac { \tilde { U _ { H } } } { L _ { H } } > \frac { U _ { L } } { L _ { L } } ) , T _ { L } = O = P _ { L } } \end{array}$ is optimal. In other words, the firm’s optimal strategy is to focus on high-type consumers only and offer flat rate pricing at $P _ { H } = U _ { H }$ (i.e., leave low-type consumers out of the market). However, when $\begin{array} { r } { - \alpha \frac { U _ { H } } { L _ { H } } + \frac { U _ { L } } { L _ { L } } \ge 0 } \end{array}$ (i.e., there are not enough high-type consumers, as $\begin{array} { r } { \frac { U _ { H } } { L _ { H } } > \frac { U _ { L } } { L _ { L } } ) , T _ { L } = L _ { L } } \end{array}$ is optimal. In other words, the firm’s optimal strategy would be to provide two FUT plans $( P _ { H } , T _ { H } )$ and $( P _ { L } ,$ $T _ { L } ) \colon$

$$
\begin{array}{c} P _ {H} = U _ {H} \frac {L _ {H} - L _ {L}}{L _ {H}} + U _ {L} \\ T _ {H} = L _ {H} \\ P _ {L} = U _ {L} \\ T _ {L} = L _ {L} \end{array}
$$

Proposition 1 (with single-crossing property, $\frac { U _ { H } } { L _ { H } } > \frac { U _ { L } } { L _ { L } } ) \colon$ When α is small enough, so that $\begin{array} { r } { - \alpha \frac { U _ { H } } { L _ { H } } + \frac { U _ { L } } { L _ { L } } \ge 0 } \end{array}$ the optimal strategy for the firm is to offer two FUT plans: $\begin{array} { r } { ( P _ { H } , \ T _ { H } ) = ( U _ { H } \frac { L _ { H } - L _ { L } } { L _ { H } } + U _ { L } , L _ { H } ) } \end{array}$ and $( P _ { L } , \ T _ { L } ) = ( U _ { L } , L _ { L } )$ . Otherwise, flat rate pricing would be superior.

While Proposition 1 is similar to Masuda and Whang’s (2006) Theorem 1, we used it to lay the theoretical comparison basis for Propositions 2 and 3 below. The strong assumption of Masuda and Whang’s Theorem 1 is the single-crossing assumption. Masuda and Whang state that “this single-crossing assumption is admittedly strong, but standard in the mechanism design literature, because it significantly simplifies the notation and analysis (Fudenberg & Tirole 1993),” (p. 248); that “Theorem 1 depends heavily on the singlecrossing properties of valuation functions $V _ { i } ^ { \mathfrak { n } } ( \mathfrak { p } . 2 5 0 )$ ; and that “in particular, the single-crossing assumption is unlikely to hold” (p. 252).

![](/api/attachments/QV6EE6Q9/fulltext/images/46d42d5635f4217d7e0c9a5a6d3008caeec22fbfd794fb6b76f8052fec87db59.jpg)  
Figure 2. Without the Single Crossing Property

On the other hand, when $\frac { U _ { H } } { L _ { H } } \leq \frac { U _ { L } } { L _ { L } }$ (without singlecrossing property; see Figure 2), we can show that, through proof by contradiction, the constraints (1) and (2) are binding:

$$
P _ {H} = U _ {H} \frac {T _ {H}}{L _ {H}}
$$

$$
P _ {L} = U _ {L} \frac {T _ {L}}{L _ {L}}
$$

The firm’s profit function is thus given by:

$$
\pi = \alpha P _ {H} + (1 - \alpha) P _ {L} = \alpha U _ {H} \frac {T _ {H}}{L _ {H}} + (1 - \alpha) U _ {L} \frac {T _ {L}}{L _ {L}}
$$

In this case, the firm will then choose $T _ { H }$ and $T _ { L }$ to maximize its profit. Since $\begin{array} { r } { \frac { \partial \pi } { \partial T _ { H } } = \alpha \left( \frac { U _ { H } } { L _ { H } } \right) > 0 , T _ { H } = L _ { H } } \end{array}$ is optimal. Similarly, since $\begin{array} { r } { \frac { \partial \pi } { \partial T _ { L } } = ( 1 - \alpha ) \frac { U _ { L } } { L _ { L } } > 0 , T _ { L } = } \end{array}$ $L _ { L }$ is optimal. It is interesting to note that the firm’s optimal strategy is to always offer two FUT plans $( P _ { H } ,$ $T _ { H } )$ and $( P _ { L } , T _ { L } )$ , regardless of the relative proportions of consumers, when the single-crossing assumption does not hold:

$$
\begin{array}{c} {P _ {H} = U _ {H}} \\ {T _ {H} = L _ {H}} \end{array}
$$

$$
\begin{array}{c} {P _ {L} = U _ {L}} \\ {T _ {L} = L _ {L}} \end{array}
$$

Proposition 2 (without single-crossing property, $\frac { { \boldsymbol { U } } _ { H } } { L _ { H } } \leq \frac { { \boldsymbol { U } } _ { L } } { L _ { L } } )$ Regardless of the relative proportions of consumers, the optimal strategy for the firm is to always offer two FUT plans: $( P _ { H } , T _ { H } ) = ( U _ { H } , L _ { H } )$ and $( P _ { L } , T _ { L } ) = ( U _ { L } , L _ { L } )$

While Masuda and Whang (2006) show that the structure of a FUT plan is optimal, we still do not know what the optimal FUT plan is when the single-crossing assumption does not hold. To our knowledge, Proposition 2 is the first that theoretically shows the optimality of FUT pricing without the strong singlecrossing assumption, and it is thus proposed to be a useful contribution to the pricing literature.

So far, we have assumed $L _ { H } \ > \ L _ { L } .$ To further understand the role that the maximum consumptionlevel bound plays in FUT pricing, it is interesting to investigate the case in which $L _ { H } = L = L _ { L }$ . When consumers have the same maximum consumptionlevel bound, both Figures 1 and 2 will actually converge to Figure 3; accordingly, the optimal solution will converge to the following proposition (by replacing $L _ { H } = L _ { L } = L$ in Proposition 1).

![](/api/attachments/QV6EE6Q9/fulltext/images/e6b4cb31f6e1a5f3e45ecc2d7ca29fc9dd852e2a30a073a6cd9b3c4b012b01d3.jpg)  
Figure 3. The Same Maximum Consumption-Level Bound

Proposition 3 (when consumers have the same maximum consumption-level bound):

When α is small enough, so that: $- \alpha U _ { H } + U _ { L } \ge 0$ the optimal strategy for the firm is to offer flat rate pricing $P = U _ { L }$ to accommodate both consumer types. Otherwise, the firm should offer flat rate pricing $P = U _ { H }$ to accommodate high-type consumers only.

Extending Masuda and Whang (2006), the analyses from our base model suggest that the maximum consumptionlevel bounds play a critical role in FUT pricing. Specifically, the value of Proposition 3 is that (together with Propositions 1 and 2) it demonstrates the pivotal role that the maximum consumption-level bound plays in FUT pricing. If consumers have different maximum consumption-level bounds, even without the singlecrossing assumption, FUT pricing is still a more profitable strategy. However, if consumers have the same maximum consumption-level bounds, even with the different utility function slopes $\frac { U _ { H } } { L } > \frac { U _ { L } } { L }$ , offering flat rate pricing would be optimal. While the insight from our base model is most likely to hold in the case of multiple types of consumers (which is still useful for offering guidance on how to design an optimal FUT strategy), in practice, the actual implementation of the model and decisions on how many plans to offer and at what prices when there are more than two types of consumers, can be challenging. Indeed, a pricing problem of this sort (when there are more than two consumer types) can be very complicated and is usually not solvable in closed-form, even when imposing the very restrictive single-crossing property (which ensures that consumers can be sorted). However, in reality, consumer types can easily go beyond two types and consumers can have very different utility functions. To address this void, in the following section we extend our base model to accommodate more than two types of consumers, and we address some practical constraints commonly observed in practice in order to guide firms on deciding whether, when, and how to effectively use FUT pricing to market their information services under many practical scenarios and parameters, specifically: (1) consumer heterogeneity and various consumer preferences, (2) incomplete information, and (3) efficiency loss compared to three-part tariff and nonlinear pricing.

## 4. The General Model

In practice, many information service providers offer FUT pricing menu from which consumers can choose. For example, Gogo Inflight Internet offers the following menu options: \$5 (1-hour), \$16 (24-hour domestic), \$28 (24-hour global), and \$59.95 (unlimited monthly). Carnival Cruise Line offers a Wi-Fi service on its cruise ships with the following options: \$159 (480 minutes), \$89 (240 minutes), \$59 (120 minutes), and \$29 (45 minutes). Neither of these companies allow over-the-limit usage beyond the preselected plan. Our general model is constructed from the information service provider’s viewpoint by considering J different plans for I consumer types (market segments). The decision problem of information service providers is determining how many plans to offer and how to price these plans in order to maximize profits, subject to consumer participation and incentive compatibility constraints.

Table 1 lists the notations used to model FUT pricing as a mixed integer nonlinear program. Note that S<sub>i</sub> and $X _ { i j }$ are not the decision variables of the information service provider, but of the equilibrium outcome and decision variables of the consumers. They are called “Intermediate Variables” in Table 1 because we incorporate the consumers’ surplus optimization decisions as constraints in our models. Accordingly, although they are not the decision variables of the information service provider, they are still treated as the optimization arguments in our model.

Table 1. Model Notations

<table><tr><td>Given Parameters</td></tr><tr><td>C: System capacity. To maintain a reasonable service quality, the information service provider must set the largest aggregate demand the system can handle. It is defined as a multiple of the largest individual demand possible.</td></tr><tr><td>F: Marginal menu cost if the information service provider adds one more plan to the pricing menu.</td></tr><tr><td>I: The market has I types of consumers.</td></tr><tr><td>J: The information service provider is considering J different possible plans.</td></tr><tr><td>Li: Maximum consumption-level bound for consumer type i. It is defined as a percentage of the largest individual demand.</td></tr><tr><td>Mj: Marginal cost, if any, of providing plan j to a consumer.</td></tr><tr><td>Ni: Number of type i consumers.</td></tr><tr><td>Tj: Plan units for plan j. It is defined as a percentage of the largest individual demand possible.</td></tr><tr><td>Uij: The utility a type i consumer can get from plan j.</td></tr><tr><td>Decision Variables or Intermediate Variables</td></tr><tr><td>Pj: Price for plan j.</td></tr><tr><td>Si: Consumer surplus for consumer type i.</td></tr><tr><td>Xij: A decision variable. 1 if consumer type i chooses to buy plan j, and zero otherwise.</td></tr><tr><td>Yj: A decision variable. 1 if the information service provider chooses to offer plan j, and zero otherwise.</td></tr></table>

Also note that in our model, we do not consider the service provider’s initial fixed cost of providing the service to each consumer, as this kind of one-time expense may not be as important as a monthly fee, considering the long-term relationship between the service provider and its subscribers. This is, perhaps, the reason that virtually all wireless service providers offer free or discounted phones to attract new consumers.

Similarly, we do not consider the initial cost incurred for the consumer to initially enroll in the information service, such as the purchase of high-end 4G mobile devices in 4G LTE wireless service scenarios. In any case, this one-time fee actually does not affect the optimization problem because it can be easily absorbed by the consumer’s utility function. The decision problem of information service providers is as follows:

$$
\max _ {P _ {j}, S _ {i}, X _ {i j}, Y _ {j}} \sum_ {i = 1, \dots I} \sum_ {j = 1, \dots I} N _ {i} \left(P _ {j} - M _ {j}\right) X _ {i j} - \sum_ {j = 1, \dots I} F Y _ {j}\tag{1}
$$

s.t.

$$
S _ {i} = \sum_ {j = 1, \dots J} \left(U _ {i j} - P _ {j}\right) X _ {i j}, \quad i = 1, \dots , I\tag{2}
$$

$$
S _ {i} \geq \left(U _ {i j} - P _ {j}\right) Y _ {j}, \quad i = 1, \dots , I; j = 1, \dots , J\tag{3}
$$

$$
\left(U _ {i j} - P _ {j}\right) X _ {i j} \geq 0, \quad i = 1, \dots , I; j = 1, \dots , J\tag{4}
$$

$$
\sum_ {j = 1, \dots , J} X _ {i j} \leq 1, \quad i = 1, \dots , I\tag{5}
$$

$$
X _ {i j} \leq Y _ {j}, \quad i = 1, \dots , I; j = 1, \dots , J\tag{6}
$$

$$
\sum_ {i = 1, \ldots , I} \sum_ {j = 1, \ldots , J} N _ {i} X _ {i j} T _ {j} \leq C\tag{7}
$$

$$
P _ {j} \leq \left(\max _ {i} U _ {i j}\right) Y _ {j}, \quad j = 1, \dots , J\tag{8}
$$

$$
P _ {j} \geq 0, \quad j = 1, \dots , J\tag{9}
$$

$$
S _ {i} \geq 0, \quad i = 1, \dots , I\tag{10}
$$

$$
X _ {i j} = 0 \text {   or   } 1, \quad i = 1, \dots , I; j = 1, \dots , J\tag{11}
$$

$$
Y _ {j} = 0 \text {   or   } 1, \quad j = 1, \dots , J.\tag{12}
$$

The objective function (1) maximizes the total net profit of the information service provider. This is calculated by the summation of profits obtained from each type of consumer minus the menu cost (if any) incurred by the information service provider. Note that information service providers may incur a positive marginal cost $M _ { j }$ (either a fixed cost or a variable cost depending on the plan units) for their information services. A fixed marginal cost might mean that a firm would have the same processing and operational costs to collect money in each period from each consumer, regardless of service plan, while a variable marginal cost might mean that there is a positive monitoring cost for the service provider to keep track of consumer usage that increases according to the number of plan units.

The following constraints are imposed: Constraint (2) defines consumer surplus as the difference between consumer i’s utility and the price of her chosen plan. Constraint (3) ensures that consumers will maximize their consumer surplus S<sub>i</sub> when choosing their plans. This can be done by ensuring that the consumer surplus from a customer’s chosen plan is higher than or equal to the consumer surplus from any other plan offered by the information service provider (incentive compatibility constraints). Constraint (4) ensures that consumers only choose a plan with a nonnegative surplus (individual rationality constraints), i.e., if $P _ { j } >$ $U _ { i j } ,$ then $X _ { i j }$ cannot be 1. Constraint (5) ensures that all consumers choose one plan at most. Constraint (6) ensures that consumers can only choose plans that are offered by the (monopolist) information service provider. Constraint (7) ensures that in order to maintain a reasonable quality of service, the largest aggregate demand the system could possibly handle is within the system’s capacity. Note that while system capacity is defined as a multiple of the largest individual demand possible, the plan units for different plans considered by the service provider (T<sub>j</sub>) and the maximum consumption-level bounds for different consumer types $( L _ { i } )$ are defined as percentages of the largest individual demand possible. For example, for a time-based information service (e.g., voice communication), the largest individual demand possible could be 24 hours multiplied by 30 days per month. Please note that 100% of the largest individual demand possible is actually equivalent to unlimited usage in the context of flat rate pricing as this is the ultimate upper bound of any individual demand. Constraint (8) sets an upper bound on plan price. It is unreasonable to set a price that no consumer is interested in paying. Constraints (9) and (10) are nonnegativity constraints for plan price and consumer surplus. Finally, Constraints (11) and (12) enforce the integer property of the decision variables with respect to consumer choices and plan offerings.

Please note that the consumer utility will stay the same beyond the bound $L _ { i } ;$ ; thus, $L _ { i }$ is actually captured by $U _ { i j } .$ As a result, while Constraints (2) to (4) would ensure that each consumer will purchase the best plan for him or herself, the service provider only needs to keep track of consumer usage and disable the service when the purchased plan units are used up. Thus, mathematically, we do not need a constraint to enforce L<sub>i</sub> separately.

To successfully solve an optimization problem analytically, we must basically resort to differentiation. However, this is generally limited to cases where the function is differentiable. In our objective function, we have 0-1 integer decision variables even in a product term with another continuous decision variable, which makes it nonlinear and nondifferentiable. Together with the constraints the objective function is subject to, it is not feasible to derive a closed-form solution for our MINLP. In fact, MINLP has traditionally been categorized as among the most difficult programs to solve by operations research scholars. In order to solve this complicated mixed integer nonlinear program for Equations 1-12, we formulated the model in GAMS format and we used the BARON solver on the NEOS Server (http://neos.mcs.anl.gov). The computational results are presented below.

## 5. Numerical Results and Case Analyses

Generally speaking, it is difficult, if not completely impossible, to derive the optimal FUT menu options analytically with more than two consumer types, even with the single-crossing assumption. One of the major contributions of our numerical solution approach is that our general model can accommodate multiple types of consumers without any auxiliary consumer utility assumption. While we can analytically show the pivotal role of the maximum consumption-level bounds in FUT pricing and derive an optimal FUT pricing menu under the condition of two types of consumers even without the single-crossing assumption (base model), we adopt a numerical solution approach to test the generalizability of our base model and explore more realistic settings without any assumptions to examine the optimal structure of FUT pricing and its relative performance effects (firm profit, consumer surplus, and social welfare) as compared to the more popular flat rate pricing under different conditions. We consider two forms of consumer heterogeneity: First, following our base model, we still assume that consumers may have different maximum consumption-level bounds (captured by parameter L<sub>i</sub>). Second, we assume that consumers may have different utility distributions across the information service (e.g., uniform distributions with different parameters). This is basically the same as consumers having different slopes for their utility functions in our base model. By having different maximum consumption-level bounds and utility distributions across the service, these assumptions implicitly assume the consumers may have different budget constraints, which is a realistic assumption in practice.

## 5.1. A Detailed Illustrative Example: In-Flight Internet Connection

As an example, we consider the case of an airline wanting to provide in-flight Internet services on one of its long-distance routes. In this example, we first randomly generate a test example and use it to demonstrate how an optimal FUT pricing menu can be a profitable alternative to flat rate pricing.

The major assumptions and parameters used in this example are listed below:

System capacity C is assumed to be 500 times the largest individual demand possible. In the case of inflight Internet, the largest individual demand possible would be the total duration of the flight, i.e., it is possible that some consumers may use the in-flight Internet connection throughout the entire duration of the flight.

The marginal menu cost F is assumed to be 500 units. In other words, the airline may face a trade-off between offering more plans to possibly capture more consumer types and confusing consumers with too many plans.

We assume five consumer types (I = 5) on the flight, and assume the airline considers 10 different plans (J = 10) with plan units at 10% increments $( T _ { I } = 1 0 \% , T _ { 2 }$ $= 2 0 \% , T _ { 3 } = 3 0 \% , T _ { 4 } = 4 0 \% , T _ { 5 } = 5 0 \% , T _ { 6 } = 6 0 \% , T _ { 7 } =$ 70%, $T _ { 8 } = 8 0 \% , \ : T _ { 9 } = 9 0 \%$ , and $T _ { I O } = 1 0 0 \% )$ of the largest individual demand possible (the duration of the flight) respectively.<sup>4</sup>

Maximum consumption-level bounds for each consumer type are randomly generated between 1% and 100% of the largest individual demand possible (flight duration) with L<sub>1</sub> = 36%, L<sub>2</sub> = 83%, L<sub>3</sub> = 61%, $L _ { 4 } = 2 6 \%$ and $L _ { 5 } = 6 3 \%$ (i.e., Consumer Type 2 are heavy users while Consumer Type 4 are lighter users).

Marginal cost of providing different plans to the consumers M<sub>j</sub> is assumed to be negligible.

The number of consumers within each type on the flight is assumed to be equal with $N _ { I } = 1 0 0 , N _ { 2 } = 1 0 0$ N<sub>3</sub> = 100, N<sub>4</sub> = 100 and N<sub>5</sub> = 100.

The utility that a type i consumer can derive from plan j, U<sub>ij</sub>, is randomly generated as follows: For Consumer Type 1, since $L _ { I } = 3 6 \%$ , we first randomly generated 36 numbers between 1 and 10, and then sorted them in a descending fashion to represent Consumer Type 1’s utility for the first 36% of the largest individual demand possible. We then accumulated the utility values to get Consumer Type 1’s utility function. We assume utility will stay the same beyond bound $L _ { I } =$ 36%. We did the same to generate the utility functions for the other four consumer types to clearly indicate a diminishing marginal utility.

As seen in Table 2 and Figure 4, the single-crossing assumption, which was required in Masuda and Whang (2006) to derive the closed form solution, is violated at several places in this example.

Table 2. The Utility that Consumer Type i Can Get from Plan j

<table><tr><td></td><td>Consumer Type 1</td><td>Consumer Type 2</td><td>Consumer Type 3</td><td>Consumer Type 4</td><td>Consumer Type 5</td></tr><tr><td>Plan 1 (10%)</td><td>87</td><td>91</td><td>93</td><td>88</td><td>96</td></tr><tr><td>Plan 2 (20%)</td><td>146</td><td>171</td><td>169</td><td>139</td><td>183</td></tr><tr><td>Plan 3 (30%)</td><td>181</td><td>242</td><td>232</td><td>149</td><td>254</td></tr><tr><td>Plan 4 (40%)</td><td>187</td><td>306</td><td>277</td><td>149</td><td>308</td></tr><tr><td>Plan 5 (50%)</td><td>187</td><td>359</td><td>305</td><td>149</td><td>345</td></tr><tr><td>Plan 6 (60%)</td><td>187</td><td>394</td><td>317</td><td>149</td><td>369</td></tr><tr><td>Plan 7 (70%)</td><td>187</td><td>418</td><td>318</td><td>149</td><td>372</td></tr><tr><td>Plan 8 (80%)</td><td>187</td><td>428</td><td>318</td><td>149</td><td>372</td></tr><tr><td>Plan 9 (90%)</td><td>187</td><td>431</td><td>318</td><td>149</td><td>372</td></tr><tr><td>Plan 10 (100%)</td><td>187</td><td>431</td><td>318</td><td>149</td><td>372</td></tr></table>

![](/api/attachments/QV6EE6Q9/fulltext/images/30c75d1c8d1a32a6aca6d1cda487eaf692ab27fd52825f87005ca7168cf199d3.jpg)  
Figure 4. Utility Functions of Different Consumer Types

## 5.1.1. Flat Rate Pricing Strategy

When a firm offers flat rate pricing to a consumer in order to attract a given consumer type, the flat rate should not be higher than this consumer type’s highest utility. For example, to sell the service to Consumer Type 1 in our example, the flat rate of the service should not be higher than 187 units. Also, because we assume that all consumers within a market segment have the same utility function, the demand curve is a step function and the possible optimal values of the flat rate are 187, 431, 318, 149, and 372 units. To find the optimal flat rate for the service, we simply compute and compare all profits that can be derived from these possible values of the flat rate. Given the particular setting described above, the airline would offer the service at 318 units. This price point would offer the highest profit level for the airline at 94,900 units, and Consumer Types 2, 3, and 5 would buy the service while Consumer Types 1 and 4 would not purchase the service.

## 5.1.2. Optimal FUT Pricing Strategy

However, given these parameters, can the airline do better by offering a FUT menu? If so, how many plans should it offer? At what plan units and prices?

We formulated the model for this test example and solved it using the BARON solver on the NEOS Server, and found the optimal FUT pricing menu: the airline should offer four plans—Plans 2, 5, 6, and 10, priced at 139, 275, 299, and 336 units, respectively. With this FUT menu offering, our model predicts that Consumer Types 1 and 4 will buy Plan 2, Consumer Type 3 will buy Plan 5, Consumer Type 5 will buy Plan 6, and Consumer Type 2 will continue to buy the highest-end plan (Plan 10). Note that with multiple plans, the airline can raise the price of its highest-end, all-you-can-use plan (Plan 10, 100%) from 318 to 336 units (but not more than 336 units, so that this plan remains attractive compared to other plans), and Consumer Types 1 and 4 are predicted to now enter the market by buying the lowest-end plan offered (results are shown in Table 3). The profit level achieved with optimal FUT pricing is now 116,800 units (versus 94,900 for flat rate pricing), or 23.08% more than the highest net profit when only flat rate pricing was offered.

## 5.1.3. Social Welfare

Based on this example, optimal FUT pricing has two social welfare implications. First, the firm can increase profits by using optimal FUT pricing. In this case, profit improvements come from two sources: market expansion (i.e., Consumer Types 1 and 4 will now purchase the service) and a higher price for the highestend plan (i.e., Consumer Type 2 is willing to pay more). Although revenues from Consumer Types 3 and 5 decrease because they select cheaper plans in this scenario, any revenue loss is compensated by higher revenues from the other consumer types. Second, optimal FUT pricing can reduce deadweight loss by accommodating more consumers in the market, thus resulting in higher consumer surplus. In this case, total consumer surplus increases by 20.96% and total social welfare increases by 22.76%; accordingly, the airline earns more and more consumers enjoy the benefits of the information service. In other words, optimal FUT pricing can be a “win-win” situation for both the firm and its consumers, enhancing social surplus.

Table 3. Flat Rate Pricing versus Optimal FUT Pricing

<table><tr><td></td><td>Consumer Type 1</td><td>Consumer Type 2</td><td>Consumer Type 3</td><td>Consumer Type 4</td><td>Consumer Type 5</td></tr><tr><td>Flat Rate Pricing Strategy</td><td>Not Buy</td><td>Buy</td><td>Buy</td><td>Not Buy</td><td>Buy</td></tr><tr><td>Optimal FUT Pricing Strategy</td><td>Buy Plan 2</td><td>Buy Plan 10</td><td>Buy Plan 5</td><td>Buy Plan 2</td><td>Buy Plan 6</td></tr></table>

## 5.2. Consumer Heterogeneity and Preferences on Optimal FUT Pricing

To account for consumer heterogeneity and consumer preferences, we examine the efficiency gains due to optimal FUT pricing (versus flat rate pricing) for different consumer preferences. Since no archival data are readily available, we rely on randomly generated data in our numerical experiments. Similar to our detailed example earlier, we first assume that there are five groups of consumers $\left( I \ = \ 5 \right)$ comprising 100 people each; all consumers in each group have homogeneous preferences, and the firm is still considering ten different plans $( J = 1 0 )$ . We compare the performance of different pricing schemes by changing the shape of the consumer utility functions: maximum consumption-level bounds for each consumer type (L<sub>i</sub>) and parameters for the per-percentusage utility distribution. Note that we use $\mathrm { U } ( a , b )$ to denote a uniform distribution over the interval [a,b]. Specifically, we use these parameters to randomly generate $U _ { i j }$ (the utility that a type i consumer can get from plan j), similar to our example. Again, we assume that the marginal menu cost F is 500, and the marginal cost of providing different plans to consumers $M _ { j }$ is 0. First, we consider the case when consumers have different maximum consumption-level bounds $( L _ { i } ) _ { \dag }$ even though their utilities are drawn from the same utility distribution (and may have similar utility function slope).

We hold the distribution fixed (uniform) and show results for three, four, and five different consumer segments (in which each segment is characterized by different values of $L _ { i } )$ (Table 4). To preserve the similarity to our detailed example, we still consider 10 possible plans and assume there are 100 consumers for each type (i.e., if there are three values for $L _ { i } ,$ there are 300 consumers). We average the results of 10 randomly generated instances for each case. As shown in Table 4, when consumers have different maximum consumption-level bounds but the same utility distribution, there are firm profit and social welfare improvements derived from using the optimal FUT pricing strategy, even though consumer surplus is not always improved. Flat rate pricing requires the price offered for the single all-you-can-use plan to be kept relatively low to attract more consumers (lower price → more consumers); otherwise, the service provider would only target high-end consumers (higher price → fewer consumers). By using optimal FUT pricing, the service provider can offer multiple plans to maximize consumers inclusion in the market; thus, firm profit and social welfare can both increase substantially.

We then examine cases in which different consumer types have different consumer utility distributions only $( \mathrm { i . e . }$ , consumers may have different utility function slopes). Specifically, all consumer types have the same $L _ { i } ,$ and utilities for different consumer types are randomly drawn from different utility distributions.

Table 4. Heterogeneous Consumer Types: Different $\mathbf { } L _ { i _ { 9 } }$ Identical Utility Distribution

<table><tr><td></td><td> $L_1=33\%,L_2=67\%$  $L_3=100\%$ </td><td> $L_1=25\%,L_2=50\%$  $L_3=75\%,L_4=100\%$ </td><td> $L_1=20\%,L_2=40\%$  $L_3=60\%,L_4=80\%$  $L_5=100\%$ </td></tr><tr><td>Consumer's utility for each percent usage</td><td>U (1,10)</td><td>U (1,10)</td><td>U (1,10)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. no. of plans offered by optimal FUT pricing</td><td>3</td><td>3.8</td><td>4.3</td></tr><tr><td>Avg. (FUT profit / Flat rate profit)</td><td>124.20%</td><td>129.73%</td><td>127.19%</td></tr><tr><td>StDev. (FUT profit / Flat rate profit)</td><td>(3.22%)</td><td>(3.78%)</td><td>(5.15%)</td></tr><tr><td>Avg. (FUT consumer surplus / Flat rate consumer surplus)</td><td>62.41%</td><td>106.99%</td><td>134.42%</td></tr><tr><td>StDev. (FUT consumer surplus / Flat rate consumer surplus)</td><td>(13.19%)</td><td>(42.61%)</td><td>(114.27%)</td></tr><tr><td>Avg. (FUT social welfare / Flat rate social welfare)</td><td>110.94%</td><td>122.87%</td><td>120.60%</td></tr><tr><td>StDev. (FUT social welfare / Flat rate social welfare)</td><td>(3.04%)</td><td>(11.78%)</td><td>(12.51%)</td></tr><tr><td></td><td>U (9,10); U (7,8)U (5,6)</td><td>U (9,10); U (7,8)U (5,6); U (3,4)</td><td>U (9,10); U (7,8)U (5,6); U (3,4)U (1,2)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Maximum consumption-level bound Li</td><td>50%</td><td>50%</td><td>50%</td></tr><tr><td>Avg. no. of plans offered by optimal FUT pricing</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Avg. (FUT profit / Flat rate profit)StDev. (FUT profit / Flat rate profit)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td></tr><tr><td>Avg. (FUT consumer surplus / Flat rate consumer surplus)StDev. (FUT consumer surplus / Flat rate consumer surplus)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td></tr><tr><td>Avg. (FUT social welfare / Flat rate social welfare)StDev. (FUT social welfare / Flat rate social welfare)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td></tr></table>

Table 5. Heterogeneous Consumer Types: Identical L<sub>i</sub>, Different Utility Distributions

Interestingly, as shown in Table 5, when different consumer types have different utility distributions but the same $L _ { i } ,$ optimal FUT pricing does no better than flat rate pricing, which is consistent with our base model results. However, when different consumer types have different $L _ { i }$ and different utility distributions (Table 6), optimal FUT pricing strategy once again outperforms flat rate pricing in terms of firm profit and social welfare, sometimes at the expense of a lower consumer surplus. This suggests that the heterogeneity in $L _ { i }$ plays a critical role in the performance of the optimal FUT pricing strategy. Thus, we empirically observe:

Finding 1: Following our base model results, in terms of the optimal FUT pricing scheme, the heterogeneity of the maximum consumptionlevel bound is more important than the heterogeneity of the consumer utility distribution (the slope of the utility function).

Differences in L<sub>i</sub> enable a clear separation of consumer types, and thus support price discrimination with different usage plans; however, the same is not true for differences in utility distribution (utility function slope) in which a separation of types through nonlinear pricing is less feasible. For consumer types with different $L _ { i } ,$ optimal FUT pricing strategy dominates flat rate pricing strategy in terms of both firm profits and social welfare, regardless of whether the utilities are randomly drawn from the same or different distributions in our examples.

To further study the role of $L _ { i } ,$ we randomly draw both $L _ { i }$ and utilities of each percent usage and repeat the same comparison for different pricing schemes. In other words, we first randomly pick an integer $L _ { i }$ between 1 and 100 for each consumer type, and then generate $L _ { i }$ random numbers from U(1,10) to represent utilities for the first $L _ { i }$ percent of the largest individual demand possible of each consumer type. We then accumulate them to get each consumer type’s utility function. Again, we assume utility stays the same beyond bound L<sub>i</sub> and 10 randomly generated instances were averaged for each case, as shown in Table 7.

Table 6. Heterogeneous Consumer Types: Different $L _ { i }$ and Different Utility Distributions

<table><tr><td></td><td> $L_1=33\%;L_2=67\%$  $L_3=100\%;U(9,10)$ U (7,8); U (5,6)</td><td> $L_1=25\%;L_2=50\%$  $L_3=75\%;L_4=100\%$ U (9,10); U (7,8)U (5,6); U (3,4)</td><td> $L_1=20\%;L_2=40\%$  $L_3=60\%;L_4=80\%$  $L_5=100\%;U(9,10)$ U (7,8); U (5,6)U (3,4); U (1,2)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. no. of plans offered by optimal FUT pricing</td><td>3</td><td>2</td><td>2</td></tr><tr><td>Avg. (FUT profit / Flat rate profit)StDev. (FUT profit / Flat rate profit)</td><td>135.08%(1.12%)</td><td>122.02%(0.22%)</td><td>122.05%(0.45%)</td></tr><tr><td>Avg. (FUT consumer surplus / Flat rate consumer surplus)StDev. (FUT consumer surplus / Flat rate consumer surplus)</td><td>4.20%(5.34%)</td><td>100.00%(0.00%)</td><td>100.00%(0.00%)</td></tr><tr><td>Avg. (FUT social welfare / Flat rate social welfare)StDev. (FUT social welfare / Flat rate social welfare)</td><td>128.99%(0.26%)</td><td>120.34%(0.14%)</td><td>120.34%(0.20%)</td></tr></table>

Table 7. Improvement of FUT Pricing Strategy (Uniform Distributed $L _ { i } )$

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td></tr><tr><td>Consumer&#x27;s utility for each percent usage</td><td>U(1,10)</td><td>U(1,10)</td><td>U(1,10)</td></tr><tr><td>No. of consumer types I</td><td>3</td><td>4</td><td>5</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. no. of plans offered by optimal FUT pricing</td><td>2.6</td><td>3</td><td>3.2</td></tr><tr><td>Avg. (FUT profit / Flat rate profit)</td><td>112.62%</td><td>116.94%</td><td>119.39%</td></tr><tr><td>StDev. (FUT profit / Flat rate profit)</td><td>(8.08%)</td><td>(12.63%)</td><td>(15.03%)</td></tr><tr><td>Avg. (FUT consumer surplus / Flat rate consumer surplus)</td><td>137.81%</td><td>112.29%</td><td>133.17%</td></tr><tr><td>StDev. (FUT consumer surplus / Flat rate consumer surplus)</td><td>(124.44%)</td><td>(50.27%)</td><td>(82.78%)</td></tr><tr><td>Avg. (FUT social welfare / Flat rate social welfare)</td><td>106.00%</td><td>112.29%</td><td>112.21%</td></tr><tr><td>StDev. (FUT social welfare / Flat rate social welfare)</td><td>(8.41%)</td><td>(7.45%)</td><td>(10.01%)</td></tr></table>

As shown in Table 7, if consumers differ in their maximum consumption-level bound $L _ { i } ,$ offering them several FUT plans is much more profitable than flat rate pricing. The profit improvement of optimal FUT pricing comes both from market expansion (by serving more consumer types) and also from price discrimination (by offering different plans and prices for different consumer types). In our examples, both average consumer surplus and social welfare improve with optimal FUT pricing. By selling to more consumers, deadweight loss is reduced and social welfare increases. When there are only a few different consumer types, deadweight loss may be small. Again, this shows that FUT pricing is profit-enhancing and socially efficient when consumers have different maximum consumption-level bounds.

## 5.3. Incomplete Information on Optimal FUT Pricing

Our base model shows how an information service provider may design an optimal FUT pricing menu when consumer utilities are known ex ante, even without the single-crossing property. Our general model also shows how optimal FUT pricing may be used by the information service provider to increase its profits and social welfare. Nevertheless, in practice, service providers seldom understand consumer utilities perfectly, and this uncertainty is, at most, generally captured by some consumer utility distribution forecasts. How can a firm hence take advantage of optimal FUT pricing when all it has is distribution forecasts of these parameter values? While it is reasonable for a service provider to predict utility distributions, acquiring exact consumer utility values is likely to be much costlier. The question that naturally arises is how much is perfect information about consumer utility worth? Conversely, does incomplete information concerning consumer utility really matter?

Our numerical solution approach based on our general model enables us to investigate this question directly by considering the three cases in Table 6. For each case in Table 6, we drew random utilities for each percent usage and used these values to determine an optimal FUT pricing menu. The process was repeated 10 times for each case. As a result, for each case in Table 6, ten FUT menus were derived. For each of these ten menus, we then drew another 10 sets of random utilities and applied the predetermined FUT menu to the new data to assess performance. We chose the most profitable FUT menu among these 10 menus and determined its average profit against 10 new sets of random utilities, denoted as FUT2. We used these 10 new sets of random utilities as given parameters to derive the optimal FUT profits, denoting the average profit from these 10 instances as FUT1. Accordingly, FUT1 represents the optimal average profit when the FUT pricing menu is set after consumer utilities are known (i.e., perfect information of exact utilities), whereas FUT2 represents the realized average profit when the FUT menu is set before consumer utilities are known (i.e., incomplete information of exact utilities). We conducted similar calculations for flat rate pricing, and the best average profit against those 10 utility sets used in both FUT1 and FUT2 is designated as FLATRATE. We express the performance comparison as a fraction of FUT1 profits (perfect information, FUT pricing) because FUT1 profits represent the highest possible profits under all schemes and conditions we considered. These comparisons are summarized in Table 8.

Table 8. Relative Profits under Incomplete Information

<table><tr><td></td><td>Case 1 in Table 6</td><td>Case 2 in Table 6</td><td>Case 3 in Table 6</td></tr><tr><td>FUT2/FUT1</td><td>93.26 %</td><td>96.11 %</td><td>94.40 %</td></tr><tr><td>FLATRATE/FUT1</td><td>72.85 %</td><td>80.25 %</td><td>80.23 %</td></tr></table>

As shown in the “FUT2/FUT1” row of Table 8, although incomplete information is clearly costly, the predetermined FUT pricing menu can reasonably approximate the optimal average profit achievable when consumer utilities are known beforehand. Furthermore, as shown in Table 8, flat rate pricing suffers more from incomplete information than FUT pricing does (smaller fractions of the optimal average profit achievable with perfect information FUT1). Hence, FUT pricing is still the better choice, even with incomplete information. The finding that FUT pricing suffers less from incomplete information than flat rate pricing does suggests that FUT pricing is an attractive pricing strategy when there is uncertainty about consumer utilities, which, in practice, is commonly the case.

Finding 2: FUT pricing performs better than flat rate pricing under incomplete information scenarios. Moreover, compared to FUT pricing, flat rate pricing suffers more from incomplete information.

## 5.4. Efficiency Loss Compared to Threepart Tariff and Nonlinear Pricing

Thus far, following Masuda and Whang (2006), we have assumed that all consumers will stay within the amount of allowed usage units in their chosen plans most of the time in both our base and our general models. Masuda and Whang argue that over-the-limit rates do not play a critical role as long as they are high enough. A practical question to extend Masuda and Whang is: Should firms treat over-the-limit rates as decision variables (i.e., should they employ a “threepart tariff” comprising plan price, plan allotment, and over-the-limit rate)? Also, how do FUT pricing and three-part tariffs perform compared to a nonlinear pricing scheme where each usage level is charged a different and nonlinear price? While it is difficult to answer these research questions analytically, our numerical solution approach allows us to examine them directly. We first construct the model for the three-part tariff pricing problem (Table 9 defines our notations):

Table 9. Model Notations for Three-Part Tariff and Nonlinear Pricing

<table><tr><td>Parameters</td></tr><tr><td>C: System capacity. To maintain a reasonable service quality, the information service provider must set the largest aggregate demand the system can handle. It is defined as a multiple of the largest individual demand possible.</td></tr><tr><td>F: Marginal menu cost if the information service provider adds one more plan to the menu.</td></tr><tr><td>I: The market has I types of consumers.</td></tr><tr><td>J: The information service provider is considering J different possible plans.</td></tr><tr><td>Li: Maximum consumption-level bound for consumer type I, defined as a percentage of the largest individual demand possible.</td></tr><tr><td>Mk: Marginal cost, if any, of providing k % of the largest individual demand possible of the information service to a consumer.</td></tr><tr><td>Ni: Number of type i consumers.</td></tr><tr><td>Tj: Plan units for plan j. It is defined as a percentage of the largest individual demand possible.</td></tr><tr><td>Uik: The utility a type i consumer can get from consuming k percent of the largest individual demand possible of the information service.</td></tr><tr><td>Decision Variables or Intermediate Variables</td></tr><tr><td>Oj: Over-the-limit rate for plan j, i.e. the unit price for each additional percent of usage over Tj when the consumer chooses plan j.</td></tr><tr><td>Pj: Price for plan j.</td></tr><tr><td>Rk: Given all plans offered by the information service provider, the most economical rate the consumer must pay for consuming k% of the largest individual demand possible of the information service, including the plan price and the over-the-limit charge, if any.</td></tr><tr><td>Si: Consumer surplus for consumer type i.</td></tr><tr><td>Xik: The decision variable which is one if consumer type i chooses to consume k % of the largest individual demand possible of the information service, and zero otherwise.</td></tr><tr><td>Yj: A decision variable; one if the information service provider chooses to offer plan j, and zero otherwise.</td></tr><tr><td>Zjk: The decision variable which is one if Rk is defined/calculated by plan j, and zero otherwise.</td></tr></table>

$$
\max _ {O _ {j}, P _ {j}, R _ {k}, S _ {i}, X _ {i k}, Y _ {j}, Z _ {j k}} \sum_ {i = 1, \dots I} \sum_ {k = 1, \dots 1 0 0} N _ {i} \left(R _ {k} - M _ {k}\right) X _ {i k} - \sum_ {j = 1, \dots J} F Y _ {j}\tag{1}
$$

$$
S _ {i} = \sum_ {k = 1, \dots 1 0 0} \left(U _ {i k} - R _ {k}\right) X _ {i k}, i = 1, \dots , I\tag{2}
$$

$$
S _ {i} \geq U _ {i k} - R _ {k}, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0\tag{3}
$$

$$
\left(U _ {i k} - R _ {k}\right) X _ {i k} \geq 0, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0\tag{4}
$$

$$
\sum_ {k = 1, \dots , 1 0 0} X _ {i k} \leq 1, \quad i = 1, \dots , I\tag{5}
$$

$$
R _ {k} = \sum_ {j = 1, \dots , J} P _ {j} Z _ {j k}, \quad k = 1, \dots , T _ {I}\tag{6-1}
$$

$$
R _ {k} = \sum_ {j = 2, \dots , J} P _ {j} Z _ {j k} + \sum_ {j = 1} \left[ P _ {j} + (k - T _ {j}) O _ {j} \right] Z _ {j k}, k = T _ {I} + 1, \dots , T _ {2}\tag{6-2}
$$

$$
R _ {k} = \sum_ {j = 3, \dots J} P _ {j} Z _ {j k} + \sum_ {j = 1, \dots 2} \left[ P _ {j} + (k - T _ {j}) O _ {j} \right] Z _ {j k}, k = T _ {2} + 1, \dots , T _ {3}\tag{6-3}
$$

$$
R _ {k} = \sum_ {j = J} P _ {j} Z _ {j k} + \sum_ {j = 1, \dots J - 1} \left[ P _ {j} + (k - T _ {j}) O _ {j} \right] Z _ {j k}, k = T _ {J - l} + 1, \dots , T _ {J}\tag{6-J}
$$

$$
R _ {k} Y _ {j} \leq P _ {j}, \quad k = 1, \dots , T _ {I}; j = 1, \dots , J\tag{7-1}
$$

$$
R _ {k} Y _ {j} \leq P _ {j}, \quad k = T _ {1} + 1, \dots , T _ {2}; j = 2, \dots , J\tag{7-2}
$$

$$
R _ {k} Y _ {j} \leq P _ {j}, \quad k = T _ {2} + 1, \dots , T _ {3}; j = 3, \dots , J\tag{7-3}
$$

$$
R _ {k} Y _ {j} \leq P _ {j}, \quad k = T _ {J - 1} + 1, \dots , T _ {J}; j = J\tag{7-J}
$$

$$
R _ {k} Y _ {j} \leq P _ {j} + (k - T _ {j}) O _ {j}, k = T _ {1} + 1, \dots , T _ {2}; j = 1\tag{8-1}
$$

$$
R _ {k} Y _ {j} \leq P _ {j} + (k - T _ {j}) O _ {j}, k = T _ {2} + 1, \dots , T _ {3}; j = 1, \dots , 2\tag{8-2}
$$

$$
R _ {k} Y _ {j} \leq P _ {j} + (k - T _ {j}) O _ {j}, k = T _ {3} + 1, \dots , T _ {4}; j = 1, \dots , 3\tag{8-3}
$$

$$
R _ {k} Y _ {j} \leq P _ {j} + (k - T _ {j}) O _ {j}, k = T _ {J - 1} + 1, \dots , T _ {J}; j = 1, \dots , J - 1\tag{8-J-1}
$$

$$
\sum_ {j = 1, \dots , J} Z _ {j k} = 1, \quad k = 1, \dots , 1 0 0\tag{9}
$$

$$
Z _ {j k} \leq Y _ {j}, \quad j = 1, \dots , J; k = 1, \dots , 1 0 0\tag{10}
$$

$$
\sum_ {i = 1, \dots I} \sum_ {k = 1, \dots 1 0 0} N _ {i} \frac {k}{1 0 0} X _ {i k} \leq C\tag{11}
$$

$$
\left(\max _ {i} U _ {i 1 0 0}\right) Y _ {j} \geq O _ {j} \geq 0, j = 1, \dots , J\tag{12}
$$

$$
\left(\max _ {i} U _ {i 1 0 0}\right) Y _ {j} \geq P _ {j} \geq 0, j = 1, \dots , J\tag{13}
$$

$$
\left(\max _ {i} U _ {i 1 0 0}\right) \geq R _ {k} \geq 0, \quad k = 1, \dots , 1 0 0\tag{14}
$$

$$
U _ {i 1 0 0} \geq S _ {i} \geq 0, \quad i = 1, \dots , I\tag{15}
$$

$$
X _ {i k} = 0 \text {   or   } 1, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0\tag{16}
$$

$$
Y _ {j} = 0 \text {   or   } 1, \quad j = 1, \dots , J\tag{17}
$$

$$
Z _ {j k} = 0 \text {   or   } 1, \quad j = 1, \dots , J; k = 1, \dots , 1 0 0.\tag{18}
$$

The objective function (Equation 1) maximizes the total net profit of the information service provider. This is calculated by the sum of profits obtained from each consumer type minus the menu cost, if any, incurred by the provider. The following constraints are imposed: Constraint (2) defines consumer surplus as the difference between consumer $i \ ' \mathrm { s }$ utility and the most economical rate of her chosen consumption level. Constraint (3) ensures that consumers will maximize their consumer surplus $S _ { i }$ when choosing their consumption levels. Constraint (4) ensures that consumers only choose a consumption level with a nonnegative surplus (individual rationality constraints), i.e., if $R _ { k } > U _ { i k }$ , then $X _ { i k }$ cannot be 1. Constraint (5) ensures that all consumers choose one consumption level at most. Constraints (6-1) \~ (6-J) define the most economical rate the consumer must pay for consuming $k$ percent of the largest individual demand possible of the information service as either “the plan price of one of the plans with plan units greater than or equal to $k ^ { \dprime }$ or “the plan price plus any over-the-limit charge of one of the plans with plan units smaller than or equal to $k . ^ { \mathfrak { n } }$ Constraints (7-1) \~ (7-J) ensure that given all plans offered by the service provider (those with $Y _ { j } = 1 )$ , the most economical rate the consumer must pay for consuming k percent of the largest individual demand possible of the information service must be smaller than or equal to the plan prices of those plans with plan units greater than or equal to $k ,$ while constraints (8-1) \~ (8-J-1) ensure that given all plans offered by the provider (those with $Y _ { j } = 1 )$ , the most economical rate the consumer must pay for

$$
\max _ {R _ {k}, S _ {i}, X _ {i k}} \sum_ {i = 1, \dots I} \sum_ {k = 1, \dots 1 0 0} N _ {i} \left(R _ {k} - M _ {k}\right) X _ {i k}
$$

s.t.

$$
S _ {i} = \sum_ {k = 1, \dots 1 0 0} \left(U _ {i k} - R _ {k}\right) X _ {i k}, i = 1, \dots , I\tag{1}
$$

$$
S _ {i} \geq U _ {i k} - R _ {k}, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0\tag{2}
$$

$$
\left(U _ {i k} - R _ {k}\right) X _ {i k} \geq 0, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0\tag{3}
$$

(4)

$$
\sum_ {k = 1, \dots , 1 0 0} X _ {i k} \leq 1, \quad i = 1, \dots , I\tag{5}
$$

$$
\sum_ {i = 1, \dots I} \sum_ {k = 1, \dots 1 0 0} N _ {i} \frac {k}{1 0 0} X _ {i k} \leq C
$$

$$
\left(\max _ {i} U _ {i 1 0 0}\right) \geq R _ {k} \geq 0, \quad k = 1, \dots , 1 0 0\tag{11}
$$

$$
U _ {i 1 0 0} \geq S _ {i} \geq 0, \quad i = 1, \dots , I
$$

We also construct the model for nonlinear pricing in which each possible usage level is charged a different (nonlinear) price. This is actually a much simplified version of the three-part tariff, achieved by removing the menu cost term in the objective function and removing constraints (6) \~ (10), (12), (13), (17) and (18):

$$
X _ {i k} = 0 \text {   or   } 1, \quad i = 1, \dots , I; k = 1, \dots , 1 0 0.\tag{14}
$$

consuming k percent of the largest individual demand possible of the information service must be smaller than or equal to the plan price, plus any over-the-limit charge of those plans with plan units smaller than or equal to k. Constraint (9) ensures that the most economical rate the consumer must pay for consuming k percent of the largest individual demand possible of the information service is defined by exactly one plan, defined by constraints (6-1) \~ (6-J). Constraint (10) ensures that the most economical rate the consumer must pay for consuming k percent of the largest individual demand possible of the information service can only be defined by those plans offered by the provider. Constraint (11) ensures that to maintain a reasonable quality of service, the largest aggregate demand the system could possibly handle is within the system’s capacity. Constraints (12) \~ (15) are upper and lower bounds for the over-the-limit rate, plan price, usage rate, and consumer surplus. Basically, the largest consumer utility forms the upper bounds of these decision variables. Finally, constraints (16) \~ (18) enforce the integer property of the decision variables with respect to consumer choices, plan offerings and rate definition/calculation.

(15)

(16)

Similar to our earlier formulation, we consider cases when consumers have different maximum consumption-level bounds (L<sub>i</sub>), even though their utilities are drawn from the same utility distribution. Specifically, we hold the distribution fixed (uniform) and show results below for 3, 4, and 5 different consumer segments (in which each segment is characterized by different values of $L _ { i } )$ . We still assume 100 consumers for each type (i.e., if there are 3 values for $L _ { i } ,$ there are 300 consumers), and the firm still considers ten different plans $( J = 1 0 )$ . To have a fair comparison, we assume the marginal menu cost to be 0 for all pricing schemes. We average the results of 10 randomly generated instances for each case as the original formulation. Due to the complexity of the three-part tariff model and the computer resource limits enforced by the BARON solver on the NEOS Server (http://neos.mcs.anl.gov), we could only test cases allowing consumers to choose consumption levels at 5% increments (i.e., 5%, 10%, 15%,..., 100%), rather than, for example, 1% increments. However, valuable insights are still available in the context of this setting.

We first compare the firm profits, consumer surplus, and social welfare of flat rate pricing and FUT pricing versus a three-part tariff. As shown in Table 10, FUT performs almost equally well as the three-part tariff context in terms of firm profits and consumer surplus. However, because the consumer surplus makes up a smaller relative portion, FUT generates about the same social welfare as the three-part tariff. In other words, from both the firm and society point of view, treating over-the-limit rates as decision variables may not be necessary, especially given the additional complexities associated with a three-part tariff. We also notice that in the optimal three-part tariff design, setting high over-the-limit rates as a penalty to discourage overthe-limit usage may not be necessary and, as a result, consumers do sometimes overuse.

Finding 3: While FUT pricing may leave higher consumer surplus, FUT pricing performs almost equally well relative to the three-part tariff, in terms of both (a) firm profits and (b) social welfare.

Finding 4: Treating over-the-limit rates as decision variables may not be necessary in terms of FUT pricing and the three-part tariff.

Finding 5: In the optimal three-part tariff design, setting high over-the-limit rates as a penalty to discourage over-the-limit usage may not be necessary and as a result, consumers do sometimes overuse.

We also compare firm profits, consumer surplus, and social welfare of flat rate pricing, FUT pricing, and three-part tariff versus nonlinear pricing. As shown in Table 11, FUT pricing and three-part tariff are both reasonably good approximations of nonlinear pricing in terms of both firm profit and social welfare. Therefore:

Finding 6: Both FUT pricing and three-part tariff are reasonably good approximations of nonlinear pricing in which each possible usage level is charged a different (non-linear) price, in terms of both (a) firm profits and (b) social welfare.

To further test the generalization of our findings, we randomly draw both $L _ { i }$ [with U(1,100)] and consumer utilities [with U(1,10)], and repeat the same comparison for different pricing schemes. As shown in Tables 12 and 13, our Findings 3-6 are still supported, even when both $L _ { i }$ and consumer utilities are randomly generated. As a result, we have a certain degree of confidence that our findings are generalizable.

Table 10. Efficiency Loss of Flat Rate and FUT Schemes Compared to Three-Part Tariff Pricing

<table><tr><td></td><td> $L_1 = 33\%, L_2 = 67\%$  $L_3 = 100\%$ </td><td> $L_1 = 25\%, L_2 = 50\%$  $L_3 = 75\%, L_4 = 100\%$ </td><td> $L_1 = 20\%, L_2 = 40\%$  $L_3 = 60\%, L_4 = 80\%$  $L_5 = 100\%$ </td></tr><tr><td>Consumer&#x27;s utility for each 5% usage</td><td>U(1,10)</td><td>U(1,10)</td><td>U(1,10)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. (Flat rate profit / Three-part tariff profit)</td><td>78.09%</td><td>77.51%</td><td>76.19%</td></tr><tr><td>Avg. (Flat rate consumer surplus / Three-part tariff consumer surplus)</td><td>308.42%</td><td>226.06%</td><td>236.37%</td></tr><tr><td>Avg. (Flat rate social welfare / Three-part tariff social welfare)</td><td>90.76%</td><td>90.77%</td><td>88.90%</td></tr><tr><td>Avg. (FUT profit / Three-part tariff profit)</td><td>99.94%</td><td>100.00%</td><td>99.92%</td></tr><tr><td>Avg. (FUT consumer surplus / Three-part tariff consumer surplus)</td><td>123.66%</td><td>97.67%</td><td>111.99%</td></tr><tr><td>Avg. (FUT social welfare / Three-part tariff social welfare)</td><td>100.78%</td><td>99.96%</td><td>100.55%</td></tr></table>

Table 11. Efficiency Loss of Flat Rate, FUT, and Three-Part Tariff Schemes Compared to Nonlinear Pricing

<table><tr><td></td><td> $L_1=33\%,L_2=67\%$  $L_3=100\%$ </td><td> $L_1=25\%,L_2=50\%$  $L_3=75\%,L_4=100\%$ </td><td> $L_1=20\%,L_2=40\%$  $L_3=60\%,L_4=80\%$  $L_5=100\%$ </td></tr><tr><td>Consumer&#x27;s utility for each 5% usage</td><td>U(1,10)</td><td>U(1,10)</td><td>U(1,10)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. (Flat rate profit / Nonlinear profit)</td><td>77.79%</td><td>77.27%</td><td>75.66%</td></tr><tr><td>Avg. (Flat rate consumer surplus / Nonlinear consumer surplus)</td><td>226.91%</td><td>231.50%</td><td>198.11%</td></tr><tr><td>Avg. (Flat rate social welfare / Nonlinear social welfare)</td><td>89.43%</td><td>90.66%</td><td>87.04%</td></tr><tr><td>Avg. (FUT profit / Nonlinear profit)</td><td>99.55%</td><td>99.67%</td><td>99.23%</td></tr><tr><td>Avg. (FUT consumer surplus / Nonlinear consumer surplus)</td><td>96.06%</td><td>99.81%</td><td>92.45%</td></tr><tr><td>Avg. (FUT social welfare / Nonlinear social welfare)</td><td>99.23%</td><td>99.84%</td><td>98.41%</td></tr><tr><td>Avg. (Three-part tariff profit / Nonlinear profit)</td><td>99.61%</td><td>99.67%</td><td>99.30%</td></tr><tr><td>Avg. (Three-part tariff consumer surplus / Nonlinear consumer surplus)</td><td>88.33%</td><td>102.64%</td><td>83.72%</td></tr><tr><td>Avg. (Three-part tariff social welfare / Nonlinear social welfare)</td><td>98.51%</td><td>99.89%</td><td>97.87%</td></tr></table>

Table 12. Efficiency Loss of Flat Rate and FUT Schemes Compared to Three-Part Tariff Pricing

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td></tr><tr><td>Consumer&#x27;s utility for each 5% usage</td><td>U(1,10)</td><td>U(1,10)</td><td>U(1,10)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. (Flat rate profit / Three-part tariff profit)</td><td>86.17%</td><td>85.60%</td><td>84.31%</td></tr><tr><td>Avg. (Flat rate consumer surplus / Three-part tariff consumer surplus)</td><td>196.54%</td><td>178.36%</td><td>128.86%</td></tr><tr><td>Avg. (Flat rate social welfare / Three-part tariff social welfare)</td><td>94.78%</td><td>92.37%</td><td>88.66%</td></tr><tr><td>Avg. (FUT profit / Three-part tariff profit)</td><td>100.00%</td><td>99.87%</td><td>99.49%</td></tr><tr><td>Avg. (FUT consumer surplus / Three-part tariff consumer surplus)</td><td>98.13%</td><td>96.02%</td><td>100.86%</td></tr><tr><td>Avg. (FUT social welfare / Three-part tariff social welfare)</td><td>99.66%</td><td>99.53%</td><td>99.57%</td></tr></table>

Table 13. Efficiency Loss of Flat Rate, FUT, and Three-Part Tariff Schemes Compared to Nonlinear Pricing

<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td></tr><tr><td>Consumer&#x27;s utility for each 5% usage</td><td>U(1,10)</td><td>U(1,10)</td><td>U(1,10)</td></tr><tr><td>No. of total consumers</td><td>300</td><td>400</td><td>500</td></tr><tr><td>No. of plans considered J</td><td>10</td><td>10</td><td>10</td></tr><tr><td>Avg. (Flat rate profit / Nonlinear profit)</td><td>85.57%</td><td>83.71%</td><td>82.93%</td></tr><tr><td>Avg. (Flat rate consumer surplus / Nonlinear consumer surplus)</td><td>190.68%</td><td>183.27%</td><td>189.08%</td></tr><tr><td>Avg. (Flat rate social welfare / Nonlinear social welfare)</td><td>94.24%</td><td>90.48%</td><td>88.16%</td></tr><tr><td>Avg. (FUT profit / Nonlinear profit)</td><td>99.37%</td><td>97.69%</td><td>97.86%</td></tr><tr><td>Avg. (FUT consumer surplus / Nonlinear consumer surplus)</td><td>92.60%</td><td>200.81%</td><td>120.31%</td></tr><tr><td>Avg. (FUT social welfare / Nonlinear social welfare)</td><td>99.06%</td><td>97.47%</td><td>99.00%</td></tr><tr><td>Avg. (Three-part tariff profit / Nonlinear profit)</td><td>99.37%</td><td>97.81%</td><td>98.19%</td></tr><tr><td>Avg. (Three-part tariff consumer surplus / Nonlinear consumer surplus)</td><td>94.60%</td><td>203.73%</td><td>115.53%</td></tr><tr><td>Avg. (Three-part tariff social welfare / Nonlinear social welfare)</td><td>99.40%</td><td>97.85%</td><td>98.93%</td></tr></table>

## 6. Discussion and Conclusions

## 6.1. Contributions and Implications for Theory and Research

To survive in today’s challenging information economy, firms must be creative in designing their pricing strategies for information services. Many service providers charge a flat rate for their services. For example, most, if not all, cable TV firms charge a flat monthly fee. Google has employed flat rate pricing for its SaaS services. Google Apps is free for the Basic Edition, but it charges a flat price of \$50 per year for its Premier Edition. While popular flat rate pricing has been studied extensively in the literature and has been shown to be generally superior to usage-based pricing (in fact, traditional two-part tariffs that charge a subscription fee are increasingly infrequently observed in practice), it may not be the optimal pricing scheme in terms of firm profits and social welfare. While flat rate pricing encourages unlimited consumption, thus challenging capacity constraints, FUT pricing is an emerging pricing scheme increasingly used by information service providers, such as mobile providers in the US, that prevents unlimited consumption and capacity constraints. However, prior research has not prescribed how information service providers should strategically use FUT pricing. Accordingly, extending the literature on the pricing of information services, our paper aims to fill this gap by examining the optimal design of FUT pricing and contributing not only to the literature on information services, but also to practice in terms of optimally pricing information services. Our study makes the following contributions along with their corresponding implications:

First, in our base model, we relax the strict singlecrossing assumption and derive the optimal FUT menu when they are two types of consumers. By using mixed integer nonlinear programming (MINLP), our general model helps firms determine their optimal FUT pricing menu for information services (i.e., what plans to offer and what prices to charge). Our general model accommodates any number of heterogeneous consumer types and any utility functions—something infeasible by using analytical approaches. By comparing the firm profits, consumer surplus, and social welfare of two of the most popular pricing schemes for information services, FUT and flat rate pricing, under various real-life consumer preference scenarios that are often difficult to examine analytically, this study helps us determine when FUT pricing is a better option and by how much. This information is more important than simply knowing whether FUT pricing is better in theory because, in practice, FUT menu pricing is generally more difficult to implement than flat rate pricing.

Second, this study offers a set of propositions and empirical findings that enhance our understanding of FUT pricing. For example, our analytical and numerical results both indicate that, when it comes to optimal FUT pricing, the maximum consumption-level bound is more important than the slope of the consumer utility functions. In our examples, regardless of utility functions, if consumers have different maximum consumption-level bounds, FUT pricing clearly dominates flat rate pricing and enhances social welfare. Our study invokes interesting practical implications because it is relatively cheaper and easier to ask a real-life consumer whether he or she positively values an additional percent usage or for how many units he or she is willing to pay, than to ask a consumer for his or her exact utility of service usage. Simply put, the amount of a service a consumer is interested in is much easier and cheaper to acquire by firms in practice, than is the consumer’s entire utility function.

Third, with our numerical FUT pricing model, we can study the efficiency loss due to incomplete information and identify the optimal pricing scheme under different incomplete information conditions. Incomplete information has not been adequately studied in the literature on the pricing of information services, perhaps because of the difficulty to analytically derive a model without numerical solutions. Our analyses show that flat rate pricing suffers more from incomplete information than FUT pricing, and FUT pricing still performs better than flat rate pricing even if the exact consumer utilities are unknown. This finding demonstrates that FUT pricing is still effective under incomplete information scenarios, which occur frequently in practice.

Fourth, our numerical solution approach also allows us to study whether firms should treat over-the-limit rates as decision variables. Our analyses show that FUT pricing performs almost equally well as three-part tariff pricing, in terms of both firm profit and social welfare, and they are both reasonably good approximations of the nonlinear pricing in which each possible usage level is charged a different nonlinear price, in terms of both firm profit and social welfare. In summary, these findings suggest that treating overthe-limit rates as decision variables in the optimization problem may not be necessary in practice.

Finally, our research also contributes by extending the literature on the pricing of information goods (e.g., digital songs, movies, books, or news), in which every unit is different, and the pricing of information services (e.g., Internet services, mobile services, or SMS/MMS), in which every unit is identical. Traditionally, academics and managers have treated the pricing of information goods and information services differently. Indeed, they often focus on either the pricing of information goods (e.g., Bakos & Brynjolfsson, 1999; Chuang & Sirbu, 1999; Hitt &

Chen, 2005; Varian, 2000; Wu, Hitt, Chen, & Anandalingam, 2008; Wu & Chen, 2008; Schlereth & Skiera, 2012) or the pricing of information services (e.g., Essegaier et al., 2002; Masuda & Whang, 2006; Schlereth, Stepanchuk, & Skiera, 2010; Chen & Wu, 2013), but do not examine both categories together. This distinct treatment is also evident in practice. While FUT pricing is a popular choice in the context of information services (like mobile phone services), there are far fewer similar pricing practices for information goods (such as digital songs, digital games, apps). However, we would like to point out that customized bundle pricing in the context of any information goods (Hitt & Chen, 2005; Wu et al., 2008) is, in practice, very similar to FUT pricing in the context of information services. Accordingly, customized bundle pricing is a pricing strategy that allows consumers to select a fixed number of different information goods of their own choice from the pool of goods offered for a fixed price, while FUT pricing allows consumers to select a fixed amount of identical information service units for a fixed price. To our knowledge, we are the first to point out this important similarity that brings together these two distinct pricing schemes (pricing of information services and pricing of information goods). In doing so, we aim at opening new avenues for these two traditionally distinct pricing schemes to learn from each other.

## 6.2. Contributions and Implications for Practice

This research also makes a managerial contribution by helping firms better price their information services. For example, our study shows that Internet service providers (ISPs) can potentially increase their profit levels with optimal FUT pricing. Some Internet addicts may be online constantly, whereas others may only use the Internet sporadically. In other words, consumers have very different maximum consumption-level bounds. The current subscription approach (flat rate pricing) adopted by most ISPs may inevitably exclude many light users from the market. Our analyses suggest that when consumers differ in the maximum consumption-level bound, FUT pricing is more efficient in terms of both firm profit and social welfare. These findings have clear and actionable implications for firms to strategically market their information services in different contexts.

Our model can help managers design optimal FUT pricing menus for their information services, offering guidance on what plans to offer and what prices to charge. Prudent managers could evaluate the performance of their candidate FUT pricing menu against many simulated parameter estimates before actually adopting any FUT menu. Based on the law of large numbers, when many test samples are used, the “average” will be close to the true mean and the variance will decrease as the number of runs increases. These average results can give managers good insights/guidelines on how well their predetermined FUT menus will perform and what profit levels they can expect in the end. We reused the three best FUT menus from Table 6 to demonstrate this idea. Specifically, we performed 10,000 test runs, respectively, and the improvements in average profits, consumer surplus, and social welfare (compared to flat rate pricing) are shown in Figure 5. As Figure 5 reveals, the average results converge very well as the number of runs increases, suggesting that useful insights can be gained and that these predetermined FUT menus perform well in the end. Again, these findings offer specific guidance to managers to help them better price their information services.

While it is generally assumed that the utility function of each consumer type is known in the literature (e.g., Masuda & Whang, 2006), and we assume the knowledge of the utility of each percent usage in our test examples, our assumption does not need to be stricter, since the utility of each percent usage can be easily derived if the whole utility function is known. Furthermore, while for each consumer type in our test examples, we use the same utility distribution for each percent usage for the convenience of generating random percent usage utilities (to randomly construct the whole utility function), using utility distribution for each percent usage is not a necessary assumption in our model. Also, we can certainly use different distributions on different parts of the utility function. In fact, our model can essentially accommodate any utility function, with or without using a utility distribution for each percent usage. In some cases, the same type of consumers may not have exactly the same maximum consumption-level bound $L _ { i }$ and percent usage utility estimates, even though these values are drawn from the same distributions. Thus, same type of consumers may make different surplus optimization decisions and our model can still accommodate them as different types. In other words, we can assume we have $\sum _ { i = 1 , . . . , I } N$ different types of consumers with only

one consumer in each type. Firms can then randomly draw the parameter values from their distributions to represent consumers and accordingly run the model to derive the optimal solution (shown above).

![](/api/attachments/QV6EE6Q9/fulltext/images/e5249c84de66e49c3b41191466dfb1a63ff9c84e70c6053f20c5b21bf63a2468.jpg)  
Figure 5. Average Results Converge as the Number of Runs Increases

## 6.3. Concluding Remarks

This study shows that FUT menu pricing is a promising pricing scheme for information services in practice. As shown in our numerical examples, optimal FUT pricing can even be a “win-win” situation for both the firm (in terms of firm profits) and its customers (in terms of consumer surplus). We cover multiple practical scenarios for FUT pricing (consumer heterogeneity and preferences, incomplete information, and efficiency loss) to advance the literature on the pricing of information services. In doing so, we hope not only to extend Masuda and Whang’s (2006) theoretical analysis of FUT pricing (which was restricted to the single-crossing assumption) to more practical, real-world applications that can inform managerial practice, but we also aim to entice future research to further explore the potential of FUT pricing in several other contexts to potentially maximize social welfare by helping firms increase their profits, by helping consumers enhance their surplus, and by helping society avoid deadweight loss from the suboptimal pricing of information services.

## References

Afeche, P., & Mendelson, H. (2004). Pricing and priority auctions in queuing systems with a generalized delay cost structure. Management Science, 50(7) 869-882.

Bagh, A., & Bhargava, H. (2013). How to price discriminate when tariff size matters. Marketing Science, 32(1) 111-126.

Bakos, Y., & Brynjolfsson, E. (1999). Bundling information goods: Pricing, profits and efficiency. Management Science, 45(12) 1613- 1630.

Bhargava, H., & Sun, D. (2008). Pricing under quality of service uncertainty: Market segmentation via statistical QoS guarantees. European Journal of Operational Research, 191(3) 1189-1203.

Cachon, G., & Feldman, P. (2011). Pricing services subject to congestion: Charge per-use fees or sell subscriptions? Manufacturing & Service Operations Management, 13(2) 244-260.

Chen, P., & Wu, S. (2013. The impact and implications of on-demand services on market structure. Information Systems Research, 24(3) 750-767.

Chuang, C. I., & Sirbu, M. A. (1999). Optimal bundling strategy for digital information goods: Network delivery of articles and subscriptions. Information Economics and Policy, 11(2), 147- 176.

Corbett, C., & Groote, X. (2000). A supplier’s optimal quantity discount policy under asymmetric information. Management Science, 46(3) 444- 450.

Dewan, S. (1996). Pricing computer services under alternative control structures: Tradeoffs and trends. Information Systems Research, 7(3) 301-307.

Dewan, S., & Mendelson, H. (1990). User delay costs and internal pricing for a service facility. Management Science, 36(12) 1502-1517.

Essegaier, S., Gupta, S., & Zhang, Z. J. (2002). Pricing access services. Marketing Science, 21(2) 139- 159.

Fishburn, P.C., Odlyzko, A. M., & Siders, R. C. (1997). Fixed fee versus unit pricing for information goods: Competition, equilibria, and price wars. Proceedings of the Conference on Internet Publishing and Beyond: Economics of Digital Information and Intellectual Property.

Fudenberg, D., & J. Tirole. (1993). Game theory. Cambridge, MA: The MIT Press.

Gupta, A., Stahl, D. O., & Whinston, A. (1996). An economic approach to networked computing with priority classes. Journal of Organizations and Computational Electronic Commerce, 6(1) 71-95.

Gupta, A., Stahl, D. O., & Whinston, A. B. (1997). A stochastic equilibrium model of Internet pricing. Journal of Economics and Dynamic Control, 21 697-722.

Gupta, A., Jukic, B., Parameswaran, M., Stahl, D., & Whinston, A. (1997). Streamlining the digital economy: How to avert a tragedy of the commons. IEEE Internet Computer, 1(6) 38-46.

Gupta, A., Jukic, B., Stahl, D., & Whinston, A. (2000). Extracting consumers’ private information for implementing incentive-compatible Internet traffic pricing. Journal of Management Information Systems, 17(1) 9-29.

Gupta, A., Jukic, B., Stahl, D., & Whinston, A. (2011). An analysis of incentives for network infrastructure investment under different pricing strategies. Information Systems Research, 22(2) 215-232.

Hitt, L. M., & Chen, P. (2005). Bundling with customer self-selection: A simple approach to bundling low marginal cost goods. Management Science, 51(10), 1481-1493.

Huang, K., & Sundararajan, A. (2011). Pricing digital goods: Discontinuous costs and shared infrastructure. Information Systems Research, 22(4) 721-738.

Konana, P., Gupta, A., & Whinston, A. (2000). Integrating user preferences and real-time workload in electronic commerce. Information Systems Research, 11(2) 177-196.

Lee, H, & Rosenblatt, M. (1986). A generalized quantity discount pricing model to increase supplier’s profits. Management Science, 32(9) 1177-1185.

MacKie-Mason, J., & Varian, H. (1995). Pricing the Internet. In B. Kahin (Ed.), Public access to the Internet (pp. 269-314). Cambridge, MA: MIT Press.

Masuda, Y., & Whang, S. (2006). On the optimality of fixed-up-to tariff for telecommunications services. Information Systems Research, 17(3), 247-253.

Mendelson, H. (1985). Pricing computer services: Queuing effects. Communications of the ACM, 28(3), 312-321.

Mendelson, H., & Whang S. (1990). Optimal incentive-compatible priority pricing for the

m/m/1 queue. Operations Research, 38(5) 870- 883.

Monahan, J. (1984). A quantity discount pricing model to increase vendor profits. Management Science, 30(6) 720-726.

Munson, C., & M. Rosenblatt. (1998). Theories and realities of quantity discounts: An exploratory study. Production and Operations Management, 7(4) 352-369.

Nadiminti, R., Mukhopadhyay, T., & Kriebel, C. (2002). Research report: Intrafirm resource allocation with asymmetric information and negative externalities. Information Systems Research, 13(4) 428-434.

Oi, W. Y. (1971). A Disneyland dilemma: Two-part tariffs for a Mickey Mouse monopoly. Quarterly Journal of Economics, 85(1), 77-96.

Randhawa, R., & Kumar, S. (2008). Usage restriction and subscription services: Operational benefits with rational users. Manufacturing & Service Operations Management, 10(3) 429-447.

Schlereth, C., & Skiera, B. (2012). Measurement of consumer preferences for bucket pricing plans with different service attributes. International Journal of Research in Marketing, 29(2) 167- 180.

Schlereth, C., Stepanchuk, T., Skiera, B. (2010). Optimization and analysis of the profitability of tariff structures with two-part tariffs. European

Journal of Operational Research, 206(3) 691- 701.

Shin, H., & Benton, W. (2004). Quantity discountbased inventory coordination: Effectiveness and critical environmental factors. Production and Operations Management, 13(1) 63-76.

Stahl, D., & Whinston, A. (1994). An economic approach to client-server computing with priority classes. In W. W. Cooper & A. B. Whinston (Eds.), New Directions in computational economics. Boston, MA: Kluwer Academic Publishers, Boston, 71-95.

Sundararajan, A. (2004). Nonlinear pricing of information goods. Management Science, 50(12), 1660-1673.

Varian, H. R. (2000). Buying, sharing and renting information goods, Journal of Industrial Economics, 48(4) 473-488.

Wu, S., & R. Banker. (2010). Best pricing strategy for information services. Journal of the Association for Information Systems, 11(6) 339-366.

Wu, S., & Chen, P. (2008). Versioning and piracy control for digital information goods. Operations Research, 56(1) 157-172.

Wu, S., L. Hitt, P. Chen, & Anandalingam, G. (2008). Customized bundle pricing for information goods: A nonlinear mixed integer programming approach. Management Science, 54(3) 608- 622.

## Appendix A: Additional Analyses

## A1. Marginal Menu Cost and Optimal FUT Pricing

In the paper, we assumed negligible marginal menu cost when offering multiple service plans to consumers. To relax this assumption, we investigate the relationship between the number of optimal FUT plans and the marginal menu cost F. To perform this analysis, we consider a case with the following parameters:

$$
I = 5, J = 10, L _ {1} = 20 \%, L _ {2} = 40 \%, L _ {3} = 60 \%, L _ {4} = 80 \%, L _ {5} = 100 \%, M _ {j} = 0, N _ {i} = 100.
$$

The consumer percent usage utilities are randomly drawn from U(1,10), as before. We fix all random utilities generated throughout the analysis but gradually increase the marginal menu cost F from 0 to 20,000. As shown in Table A1, when there is zero marginal menu cost, offering different plans to all consumer types is optimal. However, as the marginal menu cost increases (both in terms of possible firm’s overhead cost and also in terms of possible cognitive overload for consumers), the optimal number of FUT plans offered decreases, as expected. It is interesting to note that the number of optimal FUT plans tends to be relatively small as the marginal menu cost increases (dropping from five to two). Moreover, when the marginal menu cost is very high, flat rate pricing (plan 10, 100%) is the only viable plan.

Finding 1: The number of optimal FUT plans decreases and tends to be relatively small as the marginal menu cost increases. When the marginal menu cost is very high, flat rate pricing is the only viable plan.

Table A1. Relationship of the Number of Optimal FUT Plans and the Marginal Menu Cost

<table><tr><td></td><td>F = 0</td><td>F = 5000</td><td>F = 10000</td><td>F = 15000</td><td>F = 20000</td></tr><tr><td>No. of optimal FUT plans offered</td><td>5</td><td>2</td><td>2</td><td>2</td><td>1</td></tr><tr><td>Profit improvement from flat rate pricing to optimal FUT pricing</td><td>28.14%</td><td>17.16%</td><td>12.14%</td><td>6.46%</td><td>0.00%</td></tr><tr><td>Consumer surplus improvement from flat rate pricing to optimal FUT pricing</td><td>402.27%</td><td>243.18%</td><td>243.18%</td><td>220.45%</td><td>0.00%</td></tr><tr><td>Social welfare improvement from flat rate pricing to optimal FUT pricing</td><td>45.14%</td><td>28.00%</td><td>23.85%</td><td>17.97%</td><td>0.00%</td></tr></table>

## A2. Marginal Cost and Optimal FUT Pricing

In the main paper, we assumed a negligible marginal cost M<sub>j</sub> when offering a plan to a consumer. Relaxing this assumption, we examine the relationship between the number of optimal FUT plans and marginal cost M<sub>j</sub>. Specifically, we reuse the same parameters and random utilities generated in the previous subsection. However, we fix the marginal menu cost F at zero, while changing the marginal cost. We consider two types of marginal cost M<sub>j</sub>: variable marginal cost for each plan, which is dependent on plan units T<sub>j</sub>, and fixed marginal cost for each plan, which is independent of plan units T<sub>j</sub>.

We first consider the case when marginal cost for each plan is fixed (M<sub>f</sub>) regardless of units in the plan (Table A2). For example, this could correspond to the case when it costs the same processing and operational cost to collect money in each period from each consumer, regardless of service plan. As shown earlier, when the marginal cost is negligible, service providers would be willing to offer several FUT plans. Nonetheless, when fixed marginal cost is high, service providers have less incentive to provide small size plans. Therefore, as shown in Table A2, when fixed marginal cost increases, the number of optimal FUT plans decreases.

Because of this finding, FUT pricing excludes consumers with small utilities, which negatively affects consumer surplus and total social welfare. Nevertheless, it is interesting to note that in this particular case, FUT pricing is quite robust and constantly outperforms flat rate pricing in terms of profits, even when fixed marginal cost is high. As fixed marginal cost increases further (last column of Table A2), service providers are willing to offer only flat rate pricing because this is the only profitable plan, while service providers can still use flat rate pricing to extract all consumer surplus (i.e., zero consumer surplus as indicated by N.A.) for very high fixed marginal cost.

Finding 2: If marginal cost is dominated by a fixed component, then, as marginal cost increases, the number of optimal FUT plans decreases.

Finding 3: Facing fixed marginal cost, FUT pricing is quite robust as it constantly outperforms flat rate pricing in terms of profits, even when the fixed marginal cost is high.

Table A2. Relationship of the Number of Optimal FUT Plans and the Fixed Marginal Cost

<table><tr><td></td><td> $M_{f}=0$ </td><td> $M_{f}=100$ </td><td> $M_{f}=200$ </td><td> $M_{f}=300$ </td><td> $M_{f}=400$ </td><td> $M_{f}=500$ </td></tr><tr><td>No. of optimal FUT plans offered</td><td>5</td><td>2</td><td>2</td><td>2</td><td>2</td><td>1</td></tr><tr><td>Profit improvement from flat rate pricing to optimal FUT pricing</td><td>28.14%</td><td>4.83%</td><td>4.96%</td><td>8.02%</td><td>20.97%</td><td>0.00%</td></tr><tr><td>Consumer surplus improvement from flat rate pricing to optimal FUT pricing</td><td>402.27%</td><td>177.27%</td><td>-59.09%</td><td>-59.09%</td><td>-59.09%</td><td>N.A.</td></tr><tr><td>Social welfare improvement from flat rate pricing to optimal FUT pricing</td><td>45.14%</td><td>14.71%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td><td>0.00%</td></tr></table>

We also examine the case when the marginal cost increases with the plan units Tj. This may correspond to cases like in-flight phone services provided by airlines. We consider the same case as analyzed in Table A2, but now the marginal cost is a function of Tj. As shown in Table A3, our results show that the performance of flat rate pricing is sensitive to per-unit marginal cost. Flat rate pricing performs significantly worse than FUT pricing, even with small per-unit marginal cost. This may explain why airlines do not offer unlimited in-flight phone calls. On the other hand, the number of optimal FUT plans is not sensitive to per-unit marginal cost, even when the per-unit marginal cost is high. Nevertheless, when the per-unit marginal cost increases further, the demands for larger plans become negligible (since the price for large plans will be too high or the service provider will not offer them at all). Besides, when variable marginal cost is over or equal to 5Tj in this case, flat rate pricing is no longer viable, with negligible firm profits, consumer surplus and total social welfare (the last column of Table A3).

Table A3. Relationship of the Number of Optimal FUT Plans and Variable Marginal Cost

<table><tr><td></td><td> $M_{j}=0T_{j}$ </td><td> $M_{j}=1T_{j}$ </td><td> $M_{j}=2T_{j}$ </td><td> $M_{j}=3T_{j}$ </td><td> $M_{j}=4T_{j}$ </td><td> $M_{j}=5T_{j}$ </td></tr><tr><td>No. of optimal FUT plans offered</td><td>5</td><td>4</td><td>4</td><td>3</td><td>3</td><td>3</td></tr><tr><td>Profit improvement from flat rate pricing to optimal FUT pricing</td><td>28.14%</td><td>32.04%</td><td>45.04%</td><td>80.56%</td><td>259.68%</td><td>5283.33%</td></tr><tr><td>Consumer surplus improvement from flat rate pricing to optimal FUT pricing</td><td>402.27%</td><td>170.45%</td><td>170.45%</td><td>70.45%</td><td>-47.73%</td><td>N.A.</td></tr><tr><td>Social welfare improvement from flat rate pricing to optimal FUT pricing</td><td>45.14%</td><td>39.97%</td><td>54.75%</td><td>79.35%</td><td>179.17%</td><td>5633.33%</td></tr></table>

Finding 4: Flat rate pricing is very sensitive to per-unit marginal cost. Flat rate pricing performs significantly worse than FUT pricing, even with small per-unit marginal cost.

Finding 5: The number of optimal FUT plans is not very sensitive to the per-unit marginal cost.

## About the Authors

Shinyi Wu is an associate professor of information systems at the W. P. Carey School of Business of Arizona State University. He received his PhD in operations and information management and MS in operations research both from the Wharton School of the University of Pennsylvania, and his MBA and BBA in information management from National Taiwan University. His research interests include strategic pricing of information goods and services, telecommunications and efficient allocation of wireless network resources, and business analytics. His work has been published in leading journals such as Management Science, Operations Research, Information Systems Research, Journal of the Association for Information Systems, and European Journal of Operational Research.

Paul A. Pavlou is the Dean of the C. T. Bauer College of Business at the University of Houston and is also the Cullen Distinguished Chair of Information Sciences. Paul received his PhD from the University of Southern California. He was ranked #1 in the world in publications in the top two information systems journals (MISQ & ISR) in 2010-2016. His research has been cited over 42,000 times by Google Scholar, and he was recognized among the “World’s Most Influential Scientific Minds” by Thomson Reuters, based on an analysis of “highly cited” authors in Economics & Business for 2002-2012. Paul has won several Best Paper recognitions for his research, including the Sheth Foundation nomination for the “Long-Term Contribution to Marketing” in the Journal of Marketing in 2019, the Maynard Award nomination for the “Most Significant Contribution to Marketing” in the Journal of Marketing in 2015, and the ISR Best Paper award in 2007. He has also received about \$2,000,000 in grants from funding agencies such as the National Science Foundation (NSF). Paul’s research spans several disciplines (information systems, marketing, strategy, operations, decision sciences), focusing on data science, analytics, artificial intelligence, digital business strategy, and research methods. His research has appeared in Management Information Systems Quarterly, Information Systems Research, Journal of Marketing, Journal of Marketing Research, Journal of the Academy of Marketing Science, Decision Sciences, Journal of Management Information Systems, Journal of the Association of Information Systems, among other outlets.
