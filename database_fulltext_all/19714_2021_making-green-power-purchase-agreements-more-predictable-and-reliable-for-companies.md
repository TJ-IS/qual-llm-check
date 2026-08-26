---
otero_id: 19714
otero_key: "CKMCDPZ2"
title: "Making green power purchase agreements more predictable and reliable for companies"
authors: "Yashar Ghiassi-Farrokhfal; Wolfgang Ketter; John Collins"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113514"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Making green power purchase agreements more predictable and reliable for companies

![](/api/attachments/CKMCDPZ2/fulltext/images/3d2785f58443a1a051d97c1d39e26da38b4f9f62e45424cc6806600ed8144e39.jpg)

Yashar Ghiassi-Farrokhfal <sup>a,\*</sup>, Wolfgang Ketter <sup>a,b</sup>, John Collins <sup>c</sup>

<sup>a</sup> Department of Technology and Operation Management, Rotterdam School of Management, Erasmus University, Rotterdam 3062 PA, Netherland

<sup>b</sup> Institute of Energy Economics, Faculty of Economics, Management, and Social Sciences, University of Cologne, 50969 Cologne, Germany

<sup>c</sup> University of Minnesota, 200 SE Union Street, MN 55455 Minneapolis, USA

## A R T I C L E I N F O

Keywords: Power purchase agreement Battery storage Renewable energy Decision tree

## A B S T R A C T

To comply with sustainability goals, many companies buy green energy to serve their energy demand. This is typically done by engaging in bilateral power purchase agreements (PPA) with renewable energy producers (REP). A PPA can be flexibly structured, but the core principle is that a buyer (company) agrees to buy future energy production of a seller (REP) at an agreed-upon fixed price. PPAs are financially attractive for sellers, providing price certainty, unlike trading in electricity markets. However, PPAs can bring quantity uncertainty for buyers due to the uncertainty of future green energy delivery. This uncertainty in the long-term endangers sustainability targets, and in the short-term complicates reliable and cost-efficient demand matching. Thus, multiple strategies have been used in PPAs to encourage sellers to provide accurate and good-faith predictions of their short-term and longer-term future production. Yet, it has been shown that REPs can have incentives to misreport predicted values. This has discouraged some companies from engaging in PPAs. In this paper, we first investigate how PPA structure and pricing can incentivize REPs to provide more reliable predictions. This shifts the risk of production uncertainty to REPs, increasing the chance that REPs adopt batteries. We further study how having batteries for REPs affects their own revenue as well as the reliability of their energy predictions for buyers. We use analytical and simulation approaches to propose a decision tree for a win-win PPA structure, which improves reliability for buyers while maintaining profitability for REPs.

## 1. Introduction

Companies with large energy consumption are under pressure to reduce their carbon footprints. More than half of Fortune 500 companies have committed a fraction of their energy demand to be served by renewable energy sources [1]. Most companies cannot (or prefer not to) install sufficiently large renewable energy generators (e.g., solar panels and wind turbines) themselves, due to land restrictions and other complexities. Instead, they commonly engage in bilateral contracts, called power purchase agreements (PPA), with renewable energy pro ducers (REP) to buy their energy production. PPAs are becoming increasingly popular among companies. The total energy contracted through PPAs increased by 40% in 2019, accounting for more than 10% of the overall annual new renewable energy capacity [2].

PPAs are used for various types of bilateral energy trading, depending on the types of sellers and buyers [3]. In particular, a renewable-based corporate PPA is a bilateral contract between an energyconsuming company, who commits to buy future energy generation of a REP for predetermined agreed-upon prices [4].<sup>1</sup> Such a contract is financially attractive to REPs (as sellers), particularly to finance their generation facilities. This is because a PPA brings price certainty for the future uncertain energy generation of REPs (unlike facing uncertain electricity market prices). Buyers (Companies) are primarily attracted to PPAs to meet sustainability targets. However, the production uncer tainty of REPs in PPAs can bring financial and technical challenges for buyers [5]. Indeed, as companies continue to increase their sustain ability targets, production uncertainty in PPAs becomes more detri mental, and this has discouraged many companies from participating in PPAs [1].

The energy uncertainty that buyers are facing in PPAs endangers their sustainability targets over the long term and complicates serving their energy demand in the short term. Buyers in PPAs need estimates of future energy availability from REPs to plan for the most reliable and economical backup procurement, such as trading in day-ahead elec tricity markets. Typically, sellers in PPAs must provide estimates of their expected available generation, perhaps by hiring forecasting consultants [6]. It has been observed that even in the simplest form of production uncertainty (On/Off), sellers might misreport their energy availability to buyers as a risk-sharing and revenue-maximizing strategy [7]. Thus, one can expect that misreporting might also exist for renewable-based corporate PPA with much larger consequences for buyers. To prevent this, buyers in PPAs are typically given the right to audit sellers at any time. This right of auditing acts as a lever to prevent the costly mis reporting behavior of REPs and to encourage more accurate prediction reports [6,8]. However, this might not be sufficient, especially because auditing is costly for buyers and it cannot happen frequently enough to prevent rapid and costly mismatches. Thus, it is essential to find other incentives for REPs to provide their best estimates of future production.

Pricing and structural mechanisms in PPA contracts can encourage REPs to provide more reliable predictions. Indeed, there are many design options in PPAs that, if chosen properly, can attract potential sellers and buyers [6,8,9]. As PPA structures incorporate stricter mechanisms against inaccurate predictions, REPs may find storage to be an attractive investment decision to improve their revenue [10]. For buyers, storage is expected to help REPs provide more reliable pre dictions. These two objectives are not necessarily aligned. Thus, in the presence of storage, it is important to find win-win contractual solutions that simultaneously benefit buyers by improving energy prediction reliability, and REPs by improving revenue. Despite the fact that contractual solutions can improve energy predictions in PPAs, little is known about how they should be chosen, especially in the presence of storage. Indeed, according to PWC [5], the lack of knowledge on how to strategically set up a PPA is the main barrier that prevents companies from engaging in them. In a CDP questionnaire [1], 44% of companies express that they struggle with translating their targets into PPA terms.

Inspired by this research gap, we outline a win-win contractual so lution for a PPA that improves prediction reliability for the buyer while maintaining financial attractiveness for the REP. Our contractual solu tion entails recommendations for PPA pricing mechanisms and struc tural choices. We provide a decision tree that recommends how to structure a PPA in a win-win fashion. In particular, in the case the REP owns storage, the proposed decision tree determines PPA pricing mechanisms and structures that encourage storage to be used in a way to benefit both the REP (by improving revenue) and the buyer (by receiving more reliable predictions). We show how other PPA pricing and structure choices can encourage REPs to systematically over/under report their future production.

Our work falls into the category of model-driven decision support systems, which are based on quantitative mathematical modelling accompanied by limited data/information from the system to recom mend the best decisions [11,12]. We study the problem using both simulation and formal analysis, benefiting from the strengths of each approach. Our work contributes to the state of the art in multiple di mensions. First, we focus on an under-studied feature in the PPA liter ature and provide a promising solution for it. To be more precise, this is the first study to focus on the problem of energy reliability in PPAs fo buyers, formulating win-win contractual solutions. Second, we advance the literature on renewable-based PPAs by analyzing the impact of storage on REP behavior and how it is affected by PPA structure and pricing. Third, we use and extend the theory of ‘stochastic network calculus’ (SNC) to understand the impact of storage sizes on PPAs. Under some simplifying assumptions, our formal analysis shows that increasing storage size can improve the buyer’s utility from the PPA at a faster rate than it improves the seller’s utility. This implies that REPs might have incentives to expand their battery sizes to the extent that it is profitable for themselves, but possibly deteriorates value for buyers. This suggests that PPAs should entail limitations on storage sizes used by REPs to help storage be used in a win-win fashion. We also formulate such storage sizes under simplifying assumptions. Fourth, combining our simulation and analytical findings, we develop a decision tree for the pricing and structure of a win-win PPA structure.

The remainder of the paper is organized as follows. In the next sec tion, we review the related literature. In Section 3, we discuss the PPA model. We formulate how PPA pricing and mechanisms affect the re ported predictions and revenue of REPs without storage in Section 4 and with storage in Section 5. Under some simplifying assumptions, in Sec tion 6, we analytically study the asymptotic impact of storage sizes on the energy reliability for buyers and profitability for REPs. We com plement these findings by being more extensive and more accurate through simulation and numerical examples in Section 7. We provide a summary of implications and present our proposed decision tree for a win-win PPA structure in Section 8. Finally, we conclude the paper in Section 9.

## 2. Related literature

PPAs are among the important features of electricity markets. They are used for many different purposes, such as economic development, reducing prices, managing uncertainties in delivery, and/or prices [3]. Among all types of PPAs, renewable-based PPAs are increasingly drawing attention [6,8]. In a renewable-based PPA, the seller is a REP, but different entities can act as the buyer. Some studies consider a profitseeking energy trader as the buyer, which buys energy from a REP with fixed prices and trades it in the electricity market with uncertain prices [13,14]. Other studies consider a corporate PPA, in which the buyer is a company, seeking to use green energy to serve its energy demand [15]. The objectives and settings of these two types of buyers (trader versus company) differ substantially. In this work, we focus on renewablebased corporate-PPAs.

The literature on PPAs can be categorized by perspective. Most studies focus on the seller’s perspective (e.g., [13]) and fewer on the buyer’s perspective (e.g., [7,15]). In this work, we combine the buyer’s perspective (in terms of energy reliability) and the seller’s perspective (in terms of financial attractiveness) to propose a win-win PPA structure. Existing literature also considers a variety of decision variables. Some studies assume the PPA structure is given and operating/investment strategies are decision variables. For example, for a given PPA, Lei and Sandborn [13] obtain the most profitable schedules for wind turbine predictive maintenance operations from the seller’s standpoint. Other research focuses on designing features of PPAs to align with the seller’s or the buyer’s targets. For example, Tranberg et al. [14] provide a scoredriven model to improve predictions of Value-At-Risk of a PPA for the buyer through pricing mechanisms. Our work falls in this category. Finally, the literature can also be classified in terms of single/multi-PPA scenarios. We envisage a scenario in which a company participates in one PPA with a REP to serve part of its energy demand. While most literature focuses on single PPA scenarios (e.g., [7,13]), there are also scenarios in which both companies and REPs engage in multiple PPAs, simultaneously (e.g., [16]).

Our work is the first attempt to use the flexibility of the PPA struc tures to address the problem of prediction reliability of PPAs for buyers in a win-win fashion. To the best of our knowledge, it is also the first attempt to investigate how REP storage investment can affect the pre diction reliability for buyers, and how PPA structure can be used to create win-win solutions. Perhaps the closest research to our work in terms of setting and objectives is by Wu and Babich [7], which considers the unit-contingent PPA approach. They envisage an energy trading company as the buyer and a (non-renewable) power plant with two states of availability (On/Off) as the seller. Assuming asymmetric supply availability information, they show that the seller has an incentive to misreport its supply availability. While this work conceptually re sembles ours, there are major differences. First, only the seller knows the realized energy generation. The buyer can pay to audit the seller to check for possible misreporting. However, in our application, the actual predicted value is not visible to the buyer, but the realized deliverable value is. Second, we use PPA pricing mechanisms as the solution, while they use auditing as the solution. Third, accounting for a REP (as the seller) with storage is an important and relevant new element in our work.

Our work also relates to the literature addressing the challenges of selling intermittent supply in forward markets, where mismatches with realized values are adjusted in real-time markets. This problem exists in general commodity markets [17] as well as gas [18] and electricity markets [19]. The challenge of integrating REPs with uncertain pro duction into existing electricity markets has drawn significant attention in the research community (e.g., [20–24]). Some studies consider coupling renewables with natural gas power producers [25,26] or de mand response [27] to hedge against their uncertainty. Our work also relates to studies focused on using energy storage to hedge against the uncertainty of renewables. Energy storage can be used for multiple ap plications and purposes. For example, storage can be used indepen dently for price arbitrage (e.g., [28–30]). In addition to arbitrage, when storage is coupled with REPs who participate in electricity markets, it can also be used for hedging against production uncertainty [31]. The optimal bidding strategy and charging schedule of storage to maximize profit in such cases can be addressed with dynamic programming (e.g., [21,32]). Even though there are some similarities between the REP trading in a PPA and in electricity markets, there are major differences between the two. For example, in a PPA, prices in the agreement are predetermined, while in electricity markets there is price uncertainty and the possibility of price arbitrage. Moreover, the buyer in a PPA is known and unchanged throughout the entire PPA term, but this is not the case in an electricity market. These, among other fundamental dif ferences in the problem setting, make it infeasible to apply the literature on one case to the other.

## 3. Power purchase agreement (PPA) model

We envisage a renewable-based corporate-PPA in which a company commits to buying future energy generation of a REP. We adopt a classical renewable-based PPA structure [6,13]: the REP provides a prediction of future energy deliveries (aka forward commitment) to the buyer. For each unit of forward commitment, the buyer pays the REP a fixed “unit forward” price $c _ { d }$ (see Appendix B for notation). Once the actual available energy is realized, financial adjustments will be applied. The REP will pay a penalty price of $\overbar { c } _ { s }$ (typically larger than $c _ { d } )$ per unit of energy shortage and will receive (from the buyer) a rebate of $c _ { e }$ (typi cally smaller than c ) per unit of excess energy.

Buyers need to receive these predictions at both long-term and shortterm intervals, respectively, to ensure that they satisfy their long-term carbon emission reduction targets and to plan for the simplest and most economical set up to serve their short-term energy demand mis matches. By the definition of the World Business Council for Sustainable Development (WBCSD) [10], deviation from short-term estimates of energy generation is called “shape risk”, and deviation from the overall generation at the end of PPA is called “volume risk”. Since energy pro curement is more costly and complicated on short notice, renewablebased PPAs are adopting more short-term strategies to urge REPs to provide short-term predictions and in good faith [6]. Indeed, short-term deviation (shape risk) becomes more important as companies adopt more ambitious sustainability targets, covering a larger share of their demand through PPAs. For this reason. we focus on short-term deviation and energy reliability consequences for companies. However, our analysis and results can be extended to long-term deviations as well. Moreover, a recent study suggests that the contract length of PPAs might decrease (to make it more reliable for buvers) [15]. in which case the difference between the shape risks and volume risks will be diminished.

Without loss of generality, we study one billing period that starts at time 0 and is valid till time T. At the beginning of this billing period, the REP is required to provide estimates of future energy generation at each upcoming time interval τ in the billing period. In a typical PPA, the REP is required to provide hourly predictions $( \tau = 1 h )$ [6] since most buyers use the day-ahead electricity market as their energy back up to complete their energy demand procurement. This means that the buyer in a PPA needs to predict and to plan for hourly energy demand based on pre dictions received from the REP. We use a discrete-time model, where t is the time index and $t = 0 , 1 , . . . , \lceil T / \tau \rceil$

We denote $W _ { t }$ and $\widetilde { W } _ { t }$ as the actual available and the predicted values of the REP energy delivery at time t. The predicted value has a relative estimation error of ε. This is expressed as

$$
W _ {t} = (1 + \varepsilon) \widetilde {W} _ {t},\tag{1}
$$

where $\varepsilon \ge \ - 1$ to ensure $W _ { t } \geq 0 .$ . We further assume that $\widetilde { W } _ { t }$ is an un biased estimate, $\mathbb { E } ( \varepsilon ) = 0 .$ . Given $\widetilde { W } _ { t ; }$ , the REP reports (as the forward commitment to the buyer) its future energy delivery at time t to be $w _ { t } .$ The REP might over/under-report its future energy delivery if it is profitable to do so. This can be expressed as

$$
w _ {t} = (1 + \delta_ {t}) \widetilde {W} _ {t},\tag{2}
$$

where $\delta _ { t } \geq \ - 1$ (to ensure $w _ { t } \geq 0 )$ is called the quantity adjustment and represents the margin by which the REP adjusts its forward commitment with respect to its (private) predicted value to increase profit. PPAs should entail an upper bound $\delta _ { t } ^ { m a x }$ on the over-commitments of REPs $\delta _ { t }$ $\leq \delta _ { t } ^ { m a x }$ . We refer to the optimal choice of $\delta _ { t }$ that the profit-maximizing REP chooses as its forward behavior. The upper bound typically reflects the rated capacity of the renewable energy facility. We also define the following special case of forward behavior:

Definition 1. True Estimated Commitment (TEC): In a PPA, we say that the REP provides the True Estimated Commitment (TEC) as its forward commitment for a future delivery time t if it matches the un biased predicted energy availability for that time (i.e., $\pmb { w } _ { t } = \widetilde { \pmb { W } } _ { t } = \mathbb { E } [ \pmb { W } _ { t } ]$ and $\delta _ { t } = 0 )$

Using the definitions and notation above, the total expected revenue of the REP for the delivery at time t, accounting for the forward commitment and deviations after realization, is

$$
\Pi_ {t} = c _ {d} w _ {t} - c _ {s} \mathbb {E} [ [ w _ {t} - W _ {t} ] ^ {+} ] + c _ {e} \mathbb {E} [ [ W _ {t} - w _ {t} ] ^ {+} ],\tag{3}
$$

where $[ x ] ^ { + } = \operatorname* { m a x } { ( 0 , x ) }$ for any $x . ^ { 2 }$ The first term in $\operatorname { E q . }$ . (3) corresponds to the forward commitment. The second and third terms, respectively, represent the penalty of the energy shortage and rebate of the energy surplus of the realized energy with respect to the forward commitment.

Depending on the type of PPA (e.g., synthetic or physical [15]), the type and availability of backup energy supplies, and the ratio of the total demand to be served with the green energy through a certain PPA, companies have different tolerances to absorb the surplus energy beyond forward commitments. For example, if the company has the flexibility to take surplus energy on short notice, it might be willing to do so by paying small rebates $( c _ { e } > 0 )$ . In contrast, if the company serves a large share of its demand through a PPA, there will not be much space to absorb the surplus unplanned energy. In this case, the company might choose to either reject the surplus energy entirely or take it for free. In both cases, there is no rebate $( c _ { e } = 0 )$ . We call PPAs with no rebate and with a rebate, respectively, as with curtailed revenue (w-c) and without curtailed revenue (wo-c) agreements:

Definition 2. With/Without curtailed revenue (w-c)/(wo-c) agreements: In a wo-c agreement, the buyer accepts and pays a rebate $( c _ { e } > 0 )$ for the overproduction of the REP beyond its forward commit ments. In a w-c agreement, the buyer chooses to either reject the surplus energy entirely or take it for free $( c _ { e } = 0 )$ .

For the sake of simplicity of notation, we define the energy shortage price ratio $r _ { s }$ and the excess energy price ratio $r _ { e } ,$ respectively, as

$$
r _ {s} = \frac {c _ {s}}{c _ {d}} \quad \text { and } \quad r _ {e} = \frac {c _ {e}}{c _ {d}}.\tag{4}
$$

According to Definition $^ { 2 , }$ we have $r _ { e } > 0$ and $r _ { e } = 0 ,$ respectively, in a wo-c agreement and a w-c agreement. No-payment for overproduction, implemented in w-c agreements, encourages the REP to be more greedy in its forward commitments. Because, if the REP under-commits, there will be no rebate after realization. Combining these definitions with Eq. (3), yields:

$$
\Pi_ {t} = c _ {d} \widetilde {W} _ {t} (1 + \delta_ {t} - r _ {s} \mathbb {E} [ [ \delta_ {t} - \varepsilon ] ^ {+} ] + r _ {e} \mathbb {E} [ [ \varepsilon - \delta_ {t} ] ^ {+} ]),\tag{5}
$$

where $r _ { e } = 0$ and $r _ { e } > 0 ,$ respectively, in a w-c and a wo-c agreement. To simplify notation and without loss of generality, we normalize $\Pi _ { t }$ with respect to the average revenue of the REP in a hypothetical pay-as-you-$g _ { 0 }$ scenario $( c _ { d } \widetilde { W } _ { t } )$ . We define the relative expected revenue $R _ { t }$ to be

$$
R _ {t} = \frac {\Pi_ {t} - c _ {d} \widetilde {W} _ {t}}{c _ {d} \widetilde {W} _ {t}}.\tag{6}
$$

Note that $R _ { t } = 0$ occurs when the REP has the same revenue as in a pay-as-you-go scenario with the same $c _ { d } .$ Thus, the value of $R _ { t }$ for a given $c _ { d }$ implies how much and in what direction the production uncertainty risk is affecting the REP profit. In our PPA setting, the REP is the one who should be responsible for production uncertainty, which translates into revenue loss for the REP compared to the pay-as-you-go scenario (i.e., $R _ { t }$ $\leq 0 )$ . The case where $R _ { t } > 0$ infers that the financial consequences of production uncertainty are shifted more to the buyer, which is consid ered to be a win-lose scenario in our setting.

We assume that the REP is risk-neutral and thus, sets the quantity adjustment $\delta _ { t }$ in a way to maximize $R _ { t } .$ Depending on the estimation error and PPA prices, the REP might sometimes over/under-commit, if it helps improve $R _ { t } .$ . Thus, three cases can happen, each of which might be a favorable choice for the buyer, depending on the underlying conditions:

$\delta _ { t } < 0$ (under-commitment): In this case, the forward commitment is below the predicted value. This, on average, leaves extra energy to be taken by the buyer after realization. If the buyer contracts only for a fraction of its total energy demand (and not all of it) in the PPA and leaves some margins to take extra energy in real-time at lower prices, $\delta _ { t } < 0$ could be a favorable REP behavior from the buyer’s point of view.

$\delta _ { t } > 0$ (over-commitment): In this case, the forward commitment exceeds the predicted value. Thus, on average, the buyer needs to provide additional supplies to serve this unexpected energy shortage. If the cost of energy procurement from external suppliers is less than the penalty prices received from the REP for energy shortage, this case could be a favorable case for the buyer.

$\delta _ { t } = 0$ (TEC): In this case, the forward commitment is equal to the predicted available energy (Definition 1). This case, on average, has the least amount of energy adjustment after realization. This is a favorable case when the buyer prefers to have the minimum energy adjustments in real-time and plans most of its energy procurement ahead of time.

In the next section, we formulate REP revenue and forward behavior as a function of PPA pricing and structure.

## 4. REPs without storage

## 4.1. Formulating REP forward behavior

The optimal forward (energy) commitment for a risk-neutral REP is the one that maximizes the (relative) revenue $R _ { t } .$ It is clear from Eq. (5) that the optimal forward commitment for a REP without energy storage is ephemeral, meaning that the optimal energy commitment at time t only depends on the events at that particular time and not earlier or later time instants. Thus, we safely drop the time index t during a single billing period. Combining Eqs. $\left( 5 \right) - \left( 6 \right)$ , with some manipulations, we can express the relative expected revenue of a REP without storage as below (Proof in Appendix A.1):

Lemma 1. The relative expected revenue of a REP with quantity adjust ment δ is given by

$$
R = \delta - r _ {s} \int_ {- 1} ^ {\delta} \mathbb {P} (\varepsilon <   y) d y + r _ {e} \int_ {\delta} ^ {\infty} \mathbb {P} (\varepsilon > y) d y\tag{7}
$$

in a wo-c agreement. In a w-c agreement, the last term in Eq. (7) is omitted $( r _ { e } = 0 )$ . The optimal quantity adjustment $\delta ^ { * }$ of the REP, with which R in Lemma 1 is maximized (called forward behavior), is expressed in the following theorem (Proof in Appendix A.2):

Theorem 1. The forward behavior of a risk-neutral REP without storage, in terms of the optimal quantity adjustment, is given by

$$
\delta^ {*} = \left\{ \begin{array}{l l} \delta^ {m a x} & r _ {e} \leq r _ {s} <   1 \\ m i n \bigg (\mathcal {F} _ {\varepsilon} ^ {- 1} \bigg (\frac {1 - r _ {e}}{r _ {s} - r _ {e}} \bigg), \delta^ {m a x} \bigg) & r _ {e} \leq 1 \leq r _ {s} \\ - 1 & 1 <   r _ {e} \leq r _ {s} \end{array} \right.\tag{8}
$$

where $\mathcal { F } _ { \varepsilon }$ is the cumulative distribution function of ε and we assume $r _ { e }$ $\leq r _ { s } .$ Theorem 1 infers that increasing $r _ { s } ,$ in general, encourages the REP to be more conservative in its forward commitments as stated in the following corollary.

Corollary 1. The optimal quantity adjustment of the REP is mono tonically non-increasing in $r _ { s } .$

Proof. The proof is straightforward from Eq. (8).

Inserting the optimal quantity adjustment from Theorem 1 in Lemma 1. the optimal R can be obtained accordingly. We also consider the theoretical special case of a perfectly predictable REP for which $\varepsilon = 0 .$ Note that this is not a practical case (as REP generation always has uncertainty), but is used as a benchmark to study the impact of uncer tainty. This is characterized as follows:

Corollary 2. The forward behavior (optimal quantity adjustment) of a perfectly predictable REP in either a wo-c or a w-c agreement is $\delta ^ { * } =$ $\delta ^ { m a x } \mathbb { I } ( r _ { s } < 1 )$ , which leads to $R ^ { ' } = ( 1 - r _ { s } ) \delta ^ { m a x } \mathbb { I } ( r _ { s } < 1 )$ , where $\mathbb { I } ( x ) = 1$ if x is true and zero, otherwise.

Proof. The proof is immediate by setting $\varepsilon = 0$ in Eq. (5) and maximizing for δ, when $\delta \leq \delta ^ { m a x }$ . Comparing Theorem 1 with Corollary 2 shows that the forward behavior of the REP is not affected by production uncertainty, $\mathrm { i f } r _ { s } < 1$ . However, this is no loner the case, whe $. r _ { s } \ge 1$ . I $: r _ { s }$ $\geq 1 _ { : }$ , for a perfectly predictable REP, we will have $\delta ^ { * } = R ^ { * } = 0 .$ . Thus, in this case, the values of $\delta ^ { * }$ and $R ^ { * }$ for a REP with uncertainty reflect the impact of production uncertainty on each of them.

## 4.2. Visualizing and understanding PPA price zones

In this section, we visualize the results of Lemma 1, Theorem 1, and Corollary 2 to get more insights on how PPA structure and pricing impact the revenue and forward behavior of REPs. To make the visu alizations more tractable in this section, we assume tha $f _ { \varepsilon }$ is symmetric over $\varepsilon = 0$ (hence, $- 1 \leq \varepsilon \leq 1 )$ . We show later, in the numerical ex amples, that removing this simplifying symmetric assumption does not change the results noticeably for reasonable estimation errors. We further set $\delta ^ { m a x } = 1$ in this section, for the sake of simplicity of visualizations.

Given tha $t f _ { \varepsilon }$ is symmetric and according to Eq. (8), TEC (i.e., $\delta ^ { * } = 0 )$ occurs when $r _ { s } = 2$ and $r _ { s } = 2 - r _ { e } ,$ respectively, for a w-c and a wo-c agreement. Moreover, given that both ε and δ are limited to the range $^ { \mathrm { o f } \ [ - 1 , 1 ] }$ , the optimal quantity adjustment when $r _ { s } \to \infty$ converges to $^ { - 1 }$ for both PPA structures (w-c and wo-c). These observations are illustrated in Fig. 1b. In this graph, we indicate the pattern of a pre dictable REP with a solid ‘line’ and that of a REP with uncertainty with a dotted line. Solid ‘points’ indicate distribution-independent values.

We can also study the pattern of the optimal R as a function of $r _ { s * }$ From Lemma 1, we know that R is monotonically non-increasing in $r _ { s } ;$ and so is $R ^ { * }$ . For any $r _ { s } < 1$ due to the symmetric property $\operatorname { o f } f _ { \varepsilon }$ and the fact that $\mathfrak { d } , \varepsilon \in [ - 1 , 1 ] ,$ , the optimal R for both market structures reduces t $\mathrm { ~  ~ \nabla ~ } ) \mathrm { ~  ~ 1 ~ } - r _ { s } .$ Combining all of the above observations, we can illustrate $R ^ { * }$ versus $r _ { s }$ as in Fig. 1a. As shown in Fig. 1, comparing a perfectly pre dictable REP with a REP with uncertainty, we can identify three price zones, based on $r _ { s }$ and $r _ { e } .$

• Zone 1: $( r _ { s } \le$ 1): In this zone, production uncertainty does not affect the forward behavior. The REP with or without uncertainty overcommits to the maximum possible value $\delta ^ { m a x }$ (here, $\delta ^ { m a x } = 1 )$ . Its relative revenue is positive $( R ^ { * } > 0 )$ and linearly decreasing in $r _ { s * }$

• Zone 2: (wo-c: $1 \leq r _ { s } \leq 2 - r _ { e } ,$ w-c: $1 \leq r _ { s } \leq 2 ) \colon$ In this zone, pro duction uncertainty leads to over-commitment $( \delta ^ { * } > 0 \mathrm { \ v s . \ } \delta ^ { * } = 0 )$ and revenue loss $( R ^ { * } \leq 0 \mathrm { v s } . R ^ { * } = 0 )$

• Zone 3: (wo-c: $r _ { s } \ge 2 - r _ { e } ,$ w-c: $r _ { s } \ge 2 ) \colon$ In this zone, production uncertainty leads to under-commitment $( \delta ^ { * } < 0 \mathrm { \ v s . } \ \delta ^ { * } = 0 )$ and revenue loss $( R ^ { * } \leq 0$ vs. $R ^ { * } = 0 )$ .

In summary, Zone 1 is a win-lose PPA pricing zone in which the REP is the winner. In Zone-1 the REP gains more revenue than in a pay-asyou-go scenario $( R ^ { * } > 0 )$ , which means the uncertainty risk is shifted to the buyer. Moreover, the reported prediction by the REP $( \delta ^ { * } = 1 )$ is entirely unreliable/unrealistic for the buyer. A win-win PPA structure can happen in either Zone 2 or Zone 3, depending on the preferences of the buyer in terms of the target value of $\delta ^ { * }$ . In particular, if the buyer favors TEC $( \delta ^ { * } = 0 )$ , the PPA price ratio should be at the border between Zone 2 and Zone $3 ( \mathrm { i . e . , }$ wo-c: $r _ { s } = 2 - r _ { e } , \mathrm { w } \mathrm { - c } ; r _ { s } = 2 ) )$ for a win-win PPA structure. This can be generalized to include other target values of $\delta ^ { * } \colon$ In the absence of storage, the PPA can be set up in a way that the REP is incentivized to behave in favor of the buyer. In this paper, such a price ratio is referred to as the optimal PPA price ratio in a storage-less sce nario, denoted by $p ^ { * }$ and defined below:

Definition 3. Optimal price ratio in a storage-less scenario $( p ^ { * } ) \colon$ In a PPA, suppose that the buyer desires that the REP quantity adjustment to be $\delta ^ { * }$ . Then, the corresponding PPA price setting $p ^ { * }$ is any pair $( r _ { s } , r _ { e } )$ that incentivizes the REP to optimally choose the desired quantity adjustment $\delta ^ { * } .$ . For example, in the case that TEC $( \mathrm { i . e . , ~ } \delta ^ { * } = 0 )$ is favorable to the buyer, the optimal price setting $p ^ { * }$ is any pair $( r _ { s } , r _ { e } )$ that satisfies $r _ { s } + r _ { e } = 2$ and $r _ { s } = 2 ,$ , respectively, in a wo-c and a w-c agreement.

We observe that REP forward behavior $( \delta ^ { * } )$ and relative revenue (R\*) do not depend on the absolute values of prices such as $c _ { d } , c _ { s } ,$ , and $c _ { e } ,$ but rather on their ratios $r _ { s }$ and $r _ { e } .$ However, REP absolute revenue (Π) linearly scales with the absolute value of fixed price c . Thus, if the REP does not find the revenue $R ^ { * }$ corresponding to a $p ^ { * }$ value sufficiently attractive, c can be used as an extra lever to keep both the REP and the buyer happy, accounting for all energy reliability and profitability concerns.

In this section, we assumed that the REP does not own storage. However, storage can be used to increase predictability and could thereby diminish REP over/under-commitment. In the next section, we explore the circumstances in which adding a battery to the REP en courages its forward commitments to be closer to TEC. Additionally, we investigate how PPA pricing and structure should be set up in a win-win manner if the REP owns battery storage.

## 5. REPs with battery storage

Suppose that the REP in a PPA owns a battery and uses it to improve its profit. The optimal operating strategy of the storage is static and is as illustrated in $\mathrm { F i g }$ . 2a and elaborated below. The available realized en ergy $W _ { t }$ is primarily used to account for the forward energy commitment $w _ { t } .$ Denote $E _ { d , }$ the part of realized energy, which is used to serve the forward commitment, $\mathrm { i . e . , } \ E _ { d , \ t } = \ \operatorname* { m i n } \ ( w _ { t } , W _ { t } )$ . The leftover available energy is $E _ { i , ~ t } = [ W _ { t } - w _ { t } ] ^ { + }$ , which is primarily stored in the battery. However, the battery might not have enough space to store $E _ { i , \astrosun }$ or part of it. Denote $b _ { t }$ and $B ,$ respectively, the energy content (at time t) and the total battery capacity. Thus, the energy to be stored in the battery at time t, denoted by $E _ { c , \ t }$ is.

$$
E _ {c, t} = \min \left(D B - b _ {t - 1}, \overline {{{{E}}}} ^ {c h}, \eta^ {c h} [ W _ {t} - w _ {t} ] ^ {+}\right)\tag{9}
$$

where $\overline { { E } } ^ { c h }$ is the maximum charging rate of the battery within one time unit, D is the depth of discharge which is the fraction of the battery that is recommended (by the manufacturer) to be used to enhance its life time, and $\eta ^ { c h } \leq 1$ is the charging efficiency. The rest of the surplus energy that cannot be taken by the battery, denoted by $E _ { e , \ t }$ , given by

$$
E _ {e, t} = E _ {i, t} - E _ {c, t} / \eta^ {c h}\tag{10}
$$

is taken by the buyer with paying $c _ { e }$ per unit of energy in a wo-c agreement and with no extra payment in a w-c agreement. To serve the forward commitment, the primary source is the available energy $E _ { d , }$ $t \cdot \operatorname { I f }$ not sufficient, the second priority is using the energy stored in the battery. Thus, the energy to be withdrawn from the battery is

$$
E _ {b, t} = \min \left(\left(w _ {t} - E _ {d, t}\right) / \eta^ {d c}, \overline {{{{E}}}} ^ {d c}, b _ {t - 1}\right)\tag{11}
$$

where $\overline { { E } } ^ { d c }$ is the maximum energy that can be discharged in one time unit and $\eta ^ { d c } \leq 1$ is the discharging efficiency. If there is not enough energy in the battery, the rest of the energy mismatch $E _ { s , \ t } , \mathrm { g i v e n }$ by

$$
E _ {s, t} = w _ {t} - E _ {d, t} - \eta^ {d c} E _ {b, t}\tag{12}
$$

is the energy shortage that the REP needs to pay for $( c _ { s }$ per unit) as a penalty. We can also express $b _ { t }$ in terms of $w _ { t } , \ W _ { t } ,$ and $b _ { t - 1 }$ by the following recursive equation (see Fig. 2a):

$$
b _ {t} = E _ {c, t} - E _ {b, t} + b _ {t - 1}.\tag{13}
$$

The cost of using batteries for REPs is modeled as the levelized cost of storage $\left( \mathrm { L C O S } \right) c _ { b } ,$ defined as the cost of withdrawing one unit of energy from the battery.<sup>3</sup> Similarly, we define the battery LCOS price ratio as

$$
r _ {b} = \frac {c _ {b}}{c _ {d}}.\tag{14}
$$

Thus, the expected revenue of the REP with a battery in a wo-c agreement is given by

$$
\Pi_ {t} = c _ {d} w _ {t} - c _ {s} \mathbb {E} \left[ E _ {s, t} \right] - c _ {b} \mathbb {E} \left[ E _ {b, t} \right] + c _ {e} \mathbb {E} \left[ E _ {e, t} \right]\tag{15}
$$

![](/api/attachments/CKMCDPZ2/fulltext/images/261169f0bd202754611788074c7c5a3bed45560ffe972ca881cb8fc346d49e12.jpg)

![](/api/attachments/CKMCDPZ2/fulltext/images/e8c204ce4576f4fe628540610ba3303a430e868ddd40731365f028551e63b601.jpg)  
(b) Optimal δ vs. $r _ { s }$

(a) Optimal R vs. $r _ { s }$  
Fig. 1. The impact of PPA structure and pricing on $R ^ { * }$ and $\delta ^ { * } .$ The solid line is a perfectly predictable REP and the dotted line is a REP with uncertain energy generation. The solid points are independent of $f _ { \varepsilon } .$ In this figure, we assume $\delta ^ { m a x } = 1$ and $f _ { \varepsilon }$ is symmetric over 0.  
![](/api/attachments/CKMCDPZ2/fulltext/images/8af36dc437438b11f2203e9157bfaf1b92d033186d8fd6a285e4e6caa80f6d66.jpg)  
Fig. 2. A REP with a battery storage, participating in a PPA.

For a w-c agreement, $c _ { e } = 0 ,$ , which means that the last term in $\operatorname { E q } .$ (15) must be dropped.

The second term in Eq. (15) is creating a time correlation and memory. To be more precise, the battery energy content $b _ { t }$ is recursively dependent on $b _ { t - 1 } .$ . Thus, revenue maximization is no longer ephemeral in the presence of a battery. As a result, analytically computing the optimal forward commitments in the case that the REP owns a battery is much more challenging.

## 6. Analyzing the impact of storage sizes

In this section, we provide some analytical insights on how storage sizing can impact REP forward behavior and revenue. We use the theory of ‘stochastic network calculus’ (SNC), which is shown to be a great stochastic modelling approach for energy applications (compared to other most common stochastic modelings in this context), being robust to uncertainties [33].

In this section (only), for the sake of tractability of derivations, we make some simplifying assumptions (as described below). Note that the target of this section is only to provide some general (albeit concrete) understanding of the impact of storage sizes on PPAs. Accounting for all details makes the derivations non-tractable, and it is not expected to dramatically change the conclusions on the asymptotic derivations in this section (as also observed by accurate numerical examples in the next section). Providing more comprehensive analysis and considering all cases are deferred to Section $^ { 7 , }$ where we use simulation to account for all these additional complexities.

• The simplified setting for the analytical approach: In this section, we assume the more likely favorable scenario for companies in PPAs:

The REP is incentivized to under-commit in a w-c agreement, in which the buyer agrees to either reject the surplus unreported energy in real-time or take it for free. In this scenario, the buyer favors the pricing strategies to be in Zone 3. We assume that the REP owns an ideal storage (or equivalently, a battery with no imperfection), meaning that $D = 1 , \overline { { E } } ^ { c h } = \overline { { E } } ^ { d c } = \infty$ and $\eta ^ { c h } = \eta ^ { d c } = 1$ . We make a simplifying assumption that the estimated renewable energy at any time t is time-independent during the billing period $( \mathrm { i . e . , } \ \widetilde { W } _ { t } = \widetilde { W } ) .$ Furthermore, the estimation errors $\varepsilon _ { t }$ for any time t are iid random variables with double exponential distribution (Eq. (21)), where, $W _ { t } = \widetilde { W } ( 1 + \varepsilon _ { t } )$ . The iid assumption of the errors infers that renew able energy is assumed to be approximated by a stationary process for the time horizon under study. We disregard truncating the dis tribution on the boundaries.<sup>4</sup>

To formulate R, we map the problem of the energy content of an ideal storage device to the problem of buffer content in data networks. This mapping, illustrated in Fig. 2b, has been recently used in other energy applications to formulate other energy metrics ([34,35]). In this anal ogy, an ideal storage device of size B to store energy is mapped to a data buffer of size K to store data. The input data traffic to this buffer at any time t is $A _ { t }$ and a total amount of $S _ { t }$ data units from the buffer can be processed (served) at time t. The data that cannot be served at the time of arrival must be stored in the buffer to be served later. The buffer content denoted by q at time t can be expressed by

$$
q _ {t} = \min (K, [ q _ {t - 1} + A _ {t} - S _ {t} ] ^ {+})\tag{16}
$$

This can be mapped to the storage deficit state of charge $b _ { t } ^ { d } ,$ , which is the unused capacity of the storage at any time t. Under the setting of this section, we have $b _ { t } ^ { d } = B - b _ { t }$ or more precisely,

$$
b _ {t} ^ {d} = \min \bigl (B, \left[ w _ {t} - W _ {t} + b _ {t - 1} ^ {d} \right] ^ {+} \bigr)\tag{17}
$$

Comparing the energy deficit formulation in Eq. (17) with buffer content formulation in Eq. (16), we can map the storage size B to the buffer size $K ,$ the energy deficit $b ^ { d }$ to the buffer content $q ,$ the forward commitment w to the input traffic $A ,$ , and the available energy W to the service rate S. Using this mapping, for large battery sizes, R is formulated below (proof in Appendix A.3):

Theorem 2. Under the settings described in Section $^ { 6 , }$ the asymptotic value of R (when B is large) for a REP with quantity adjustment $\delta \ < \ 0$ is approximately<sup>5</sup>:

$$
R = \delta - \frac {(r _ {s} - r _ {b}) e ^ {- \theta \overline {{B}}}}{\theta} - \frac {r _ {b}}{2 \lambda} e ^ {\lambda \delta},\tag{18}
$$

where $\begin{array} { r } { \overline { { B } } = \frac { B } { w } } \end{array}$ is the battery size in terms of the number of time units the battery can store the available energy and $\begin{array} { r } { \theta = \frac { - 2 \lambda ^ { 2 } \delta } { 2 + \lambda ^ { 2 } \delta ^ { 2 } } } \end{array}$ Note, however, that LCOS should satisfy the following general necessary condition of storage profitability to be used by the REP (proof in Appendix A.4):

Lemma 2. A necessary condition for storage to be profitable for the REP in w-c and wo-c agreements are, respectively, $r _ { b } \leq r _ { s }$ and $r _ { b } \le r _ { s } - r _ { e } .$

Optimizing the closed-form formulation of R from Theorem 2 over $\delta ,$ Theorem 3 formulates the forward behavior of a REP with an ideal storage system (proof in Appendix A.5).

Theorem 3. Under the settings described in Section $^ { 6 , }$ the asymptotic optimal quantity adjustment of a REP with an ideal storage system of size $B ,$ when B is large is approximately

$$
\delta^ {*} = - \frac {1}{\lambda^ {2} \overline {{B}}} \mathbb {W} \left(\frac {2 \lambda^ {2} \overline {{B}} ^ {2} (r _ {s} - r _ {b})}{2 - r _ {b}}\right)\tag{19}
$$

where W is the Lambert W function. To effectively design a PPA, in which the REP owns storage, we should know how increasing the stor age size affects the REP revenue and forward behavior. These are needed $^ { \mathrm { t o , } }$ respectively, project the REP incentives on investing in storage and to know how the storage size transforms REP forward behavior. This is presented below (proof in Appendix A.6).

Corollary 3. Under the settings described in Section 6 and assuming that the necessary condition for profitability in Lemma 2 holds $( \mathrm { i } . \mathrm { e } . , r _ { b } <$ $r _ { s } ) ,$ both $\delta ^ { * }$ and $R ^ { * }$ are monotonically non-decreasing in the storage size, respectively, varying in the range of $[ \delta _ { m i n } , 0 ]$ and $[ R _ { m i n } , R _ { m a x } ]$ , starting from their lower bounds (when $\overline { { B } } = 0 )$ , converging to the upper bounds (when B increases) with respective convergence rates of $\Theta \left( \overline { { B } } ^ { - 1 } l o g \overline { { B } } \right)$ and $\Theta \Big ( l o g ^ { - 1 } \Big ( \overline { { B } } \Big ) \Big )$ . The lower and upper bounds are given by $\delta _ { m i n } =$

$$
\frac {1}{\lambda} \log \left(\frac {2}{r _ {s}}\right), R _ {\min} = \frac {\log \left(\frac {2}{r _ {s}}\right) - 1}{\lambda}, \text {   and   } R _ {\max} = - \frac {r _ {b}}{2 \lambda}.
$$

Based on Corollary $3 , R _ { m a x }$ is the best that can be achieved by adding storage. Corollary 3 also shows that adding storage to REPs in Zone $^ { 3 , }$ incites them to behave arbitrarily close to TEC. According to Corollary $^ { 3 , }$ the rate of convergence of the forward behavior to TEC $\scriptstyle ( \Theta \left( { \overline { { B } } } ^ { - 1 } l o g { \overline { { B } } } \right) )$ ) is faster than their revenue increments (Θ $\left( l o g ^ { - 1 } \left( \overline { { B } } \right) \right) \mathrm { ] }$ ) as the storage size increases. The faster rate of improvement in $\delta ^ { * }$ than in $R ^ { * }$ is also observed in Section 7.

We examine the accuracy of R in Theorem $2 , \delta ^ { * }$ in Theorem $^ { 3 , }$ and validity of Corollary 3, by a comparison with simulation results. Denote $\delta _ { m i n }$ and $\delta _ { T 3 } ,$ respectively, the optimal δ in a storage-less scenario (from Corollary 3) and the optimal asymptotic δ when B is large (from Theo rem 3). With this notation and the fact that $\delta ^ { * }$ is monotonically nondecreasing in B, for any $\overline { B }$ we have $\delta ^ { * } \geq$ max $( \delta _ { m i n } , \delta _ { T 3 } )$ , where the inequality turns to equality for $\overline { { B } } = 0$ and $\overline { { B } } \to \infty$ . Similarly, we have $R ^ { * }$ $\geq$ max $( R _ { m i n } , R _ { T 2 } )$ , where $R _ { m i n }$ is the optimal R when $\overline { { B } } = 0$ (formulated in Corollary 3) and $R _ { T 2 }$ is the optimal R when $\overline { { B } } \to \infty ,$ obtained by replacing $\delta _ { T 3 }$ in Theorem 2. Moreover, the inequality $( R ^ { * } \geq$ max $( R _ { m i n } .$ $R _ { T 2 } ) )$ turns to equality for $\overline { { B } } = 0$ and $\overline { { B } } \to \infty ,$

We compare these theoretical results with simulation in Fig. 3 for λ $= 5 , r _ { s } = 3 ,$ , and $r _ { b } = 0 . 5$ . The curves denoted by ‘Analysis’ in Fig. 3a and Fig. 3b are, respectively, max $( R _ { m i n } , R _ { T 2 } )$ for $R ^ { * }$ and max $( \delta _ { m i n } , \delta _ { T 4 } )$ for $\delta ^ { * } .$ . Fig. 3 shows that the theoretical results for $\overline { { B } } = 0$ and $\overline { { B } } \to \infty$ (and even for medium values of $\overline { { B } } )$ for both $R ^ { * }$ and $\delta ^ { * }$ are highly accurate. Please note that the values of $\delta ^ { * }$ and $R ^ { * }$ from Theorem 3 and Theorem 2 are asymptotic results, supposed to be accurate when B is large and yet we observe high accuracy with medium values of B in Fig. 3.

According to Section $^ { 3 , }$ a buyer that has some margins to take surplu unplanned renewable energy with zero or little rebates prefers that the REP under-commits with some target value of $\delta < 0 . { } ^ { 6 }$ To align the REP forward behavior accordingly, when the REP uses storage, the results of this section suggest that the storage size must be restricted. This is because the REP revenue improvement (as storage size increases) grows at a slower rate than changing its forward behavior (see Corollary 3). Thus, there is a point after which increasing storage size still helps improve REP revenue, but δ exceeds and diverges from the buyer’s target δ. In such scenarios, PPA should entail limitations on the maximum allowable storage size that the REP can use, to align the REP forward behavior with the buyer’s target δ.

Given a target forward behavior $\delta < 0 _ { : }$ , the maximum storage size allowed for the REP should be a function of PPA prices. Below, we formulate such a storage size as a by-product of Theorem 3 (proof in Appendix $\mathsf { A } . 7 )$

Corollary 4. Under the settings described in Section $^ { 6 , }$ , the optimal storage size for the REP to choose a certain (a small) $\delta < 0$ is

$$
\overline {{B}} = \left\{ \begin{array}{c c} 0 & \text {   if   } \frac {1}{\lambda} \log \left(\frac {2}{r _ {s}}\right) \geq \delta \\ \frac {1}{\delta \lambda^ {2}} \mathbb {W} _ {- 1} \left(\frac {- \delta^ {2} \lambda^ {2} (2 - r _ {b})}{2 (r _ {s} - r _ {b})}\right) & \text {   if   } \frac {1}{\lambda} \log \left(\frac {2}{r _ {s}}\right) <   \delta \end{array} \right.\tag{20}
$$

where $\mathbb { W } _ { - 1 }$ is the negative branch of the Lambert W function. Corollary 4 suggests that there should be some additional terms in PPAs on storage sizes when REPs use storage. For example, Eq. (20) can be served as the maximum allowable storage size to keep the REP forward behavior below a target value δ.

## 7. Numerical examples

We assume that an energy-consuming company engages in a PPA with a REP who owns a solar PV farm with a capacity of 5 MW. Ac cording to the PPA, the REP should provide hourly predictions for future delivery time and applies financial adjustments (as discussed in Section 3) after realization. We use one year (2018) of the solar power production data set from a field in the United States with hourly reso lution and we linearly scale that data set, resembling a solar PV farm with a capacity of 5 MW. We assume that the REP has an estimation of the available energy at a future time slot with an exponential tail-bound estimation error with parameter λ. To be more precise, the relative estimation error ε in Eq. (1) has the following distribution

![](/api/attachments/CKMCDPZ2/fulltext/images/d0531317395aec0f5f0579e00bbda9a29569c07e7401fb2ec4c791f165c4e0b2.jpg)  
(a) 'Analysis' R\* := max(Rmin, RT2)

![](/api/attachments/CKMCDPZ2/fulltext/images/f4392596942886e31f8751884be84396d04229f1874c2a18c9db500e4c2ac0c9.jpg)  
(b) Analysis' δ\* := max(δmin, δT3)  
Fig. 3. Comparing analytical results with simulation $( \lambda = 5 , r _ { s } = 3 , r _ { b } = 0 . 5 )$ . As expected, the ‘Analysis’ is accurate when $\overline { { B } } = 0$ and $\overline { { B } } \to \infty .$ . For moderate ${ \overline { { B } } } ,$ still high accuracy is observed.

$$
f _ {\varepsilon} (x) = \frac {\lambda}{2} e ^ {- \lambda | x |}\tag{21}
$$

which is truncated to be always $x \ge ~ - 1$ , ensuring that actual available energy is non-negative.<sup>7</sup> The REP might also own a Li-ion battery storage. The battery size, denoted by ${ \overline { { B } } } ,$ is represented in terms of the number of hours the battery can store the long-term average energy generation of the REP $\begin{array} { r } { ( \mathrm { i . e . , } \ \sum _ { t = 1 } ^ { T } \widetilde { W } _ { t } } \end{array}$ for a large T). The other physical properties of the Li-ion battery are set to be $\eta ^ { c h } = \eta ^ { d c } = 0 . 9 5 , \overline { { { E } } } ^ { c h } = \overline { { { B } } } ,$ ${ \overline { { E } } } ^ { d c } = { \overline { { B } } } ,$ and $D = 0 . 8$ . We study the problem from multiple different angles as described in the following subsections. Unless otherwise stated, in this sections, we set $\lambda = 2 , r _ { b } = 0 . 5$ and $r _ { e } = 0 . 8 .$ . Please note that with this value of $r _ { e } = 0 . 8 ,$ Zone 2 is characterized as 1 $\leq r _ { s } \leq 1 . 2$ and $1 \leq r _ { s } \leq 2 ,$ respectively, for a wo-c and a w-c agreement. Similarly, Zone $^ { 3 , }$ is characterized as $r _ { s } \ge 1 . 2$ and $r _ { s } \ge 2 ,$ , respectively, for a wo-c and a wc agreement. Zone 1 is characterized as $r _ { s } \le 1$ for both w-c and wo-c agreements.

## 7.1. The impact of PPA structure and pricing

Fig. 4 illustrates the optimal R and δ as a function of energy shortage price ratio $r _ { s \ast }$ We compare a storage-less scenario $\left( \overline { { B } } \right) = 0 )$ with a battery equipped scenario $( \overline { { B } } = 5 H )$ . Multiple observations can be made from Fig. 4 on the forward behavior and the profitability of REPs.

For the special case of a storage-less scenario $( \overline { { B } } = 0 ) , \mathrm { F i g . ~ } 4$ verifies the theoretical results on the general trends of $R ^ { * }$ ad $\delta ^ { * }$ in Section $^ { 4 , }$ which are illustrated in Fig. 1. Note, however, that in this simulation, we have a non-symmetric estimation error, whereas a symmetric one was assumed in the theoretical results in Section 4. This shows that without the symmetric assumption, the results in Section 4 do not change dramatically. In particular, corroborating the theoretical results in Section $^ { 4 , }$ in a storage-less scenario, TEC $( \delta ^ { * } = 0 )$ is happening at the border of Zone 2 and Zone $^ { 3 , }$ which is $r _ { s } = 1 . 2$ and $r _ { s } = 2 ,$ respectively, for a wo-c and a w-c agreement.

Comparing the storage-less scenario in a w-c agreement with that in a wo-c agreement $( ^ { \cdot } \overline { { B } } = 0 , w - c ^ { , } { \mathrm { a n d } } ^ { \cdot } \overline { { B } } = 0 , w o - c ^ { , } )$ in Fig. $^ { 4 , }$ shows that not paying for surplus energy, as in a w-c agreement, leads to a sub stantial revenue loss for the REP and encourages it to be more greedy in its forward commitments in both Zones 2 and 3. Though, it has no noticeable impact on either profitability or forward behavior in Zone 1. The impact of no-payment for surplus energy on both revenue and for ward behavior becomes more pronounced as $r _ { s }$ increases.

Fig. 4a shows that adding a battery can compensate (to a good extent) the REP revenue loss due to uncertainty in both wo-c and w-c agreements, with a much more pronounced impact in a w-c agreement. In terms of REP forward behavior, from Fig. 4b, we observe that adding a battery has different effects in a w-c agreement, depending on the PPA price zone. In Zone $^ { 2 , }$ adding a battery encourages the REP to be less greedy in its forward commitments.<sup>8</sup> This means that with no payment for surplus energy, adding a battery to the REP always encourages REP forward behavior to be closer to TEC. Comparing the REP revenue and bidding strategies in a w-c with and without storage in Zone 3, reveal that adding storage encourages the REP forward behavior to move to wards TEC at a faster rate than its impact on the REP revenue gain (compare Fig. 4a and b). This corroborates the analytical results in Section 6 and Corollary 3

## 7.2. The impact of the battery size

In Fig. 5, we examine the impact of battery sizes on the REP behavior and revenue. We set $r _ { s } = 1 . 1$ and $r _ { s } = 3 _ { \mathrm { : } }$ , representing operating points in Zone 2 and Zone $^ { 3 , }$ respectively. We exclude the less interesting case of Zone 1 in this example, because this zone leads to a win-lose PPA structure (as shown in Section 4.2). We vary the battery size B to observe its impact on R and δ and discuss some of those observations below.

In Zone 2 (here, $r _ { s } = 1 . 1 )$ adding a battery has a different impact on quantity adjustments in a w-c agreement compared to a wo-c agreement (according to Fig. 5b): Adding a battery to the REP in Zone 2 in a w-c agreement, encourages the REP to be less greedy on its forward com mitments (closer to TEC). In contrast, adding a battery to the REP in Zone 2 in a wo-c agreement encourages it to be more greedy (deviating from TEC). Please note that as the battery size increases, the optimal quantity adjustment increases in a wo-c agreement and decreases in a wc agreement; for large enough battery sizes they converge to each other. Fig. 5a shows that the impact of adding batteries on improving REP revenue is not significant in Zone 2.

In Zone $3 \ : ( \mathrm { h e r e } , r _ { s } = 3 )$ and in the absence of batteries $( B = 0 )$ , the wc structure helps prevent under-commitment and encourages the for ward behavior to be closer to TEC, but leads to a substantial revenue loss if the REP does not have a battery. Fig. 5a shows that adding a battery extremely helps improve the REP revenue in a w-c agreement. Batteries also improve the revenue of the REP in a wo-c agreement in Zone 3, but the additional revenue is not as considerable as in a w-c agreement. Fig. 5b shows that the impact of the battery on improving the REP for ward behavior (from the buyer’s point of view) in Zone 3 is even larger than its impact on REP revenue improvement (compare it with Fig. 5a). As the battery size increases, the additional improvement in terms of quantity adjustment converges faster to its saturated value than the improvement in revenue. Thus, the REP might have an incentive to invest in larger batteries to gain in revenue, but this does not help the buyer.

![](/api/attachments/CKMCDPZ2/fulltext/images/b330ca3ce70b37303909d82cd9f13f3bc784797fbe1a13507e4b253f8fc5e571.jpg)

![](/api/attachments/CKMCDPZ2/fulltext/images/bfadfdcf1059f877cd9364f8bbf5b32acb2c4410c19f7f12b6da4b1227c2abe4.jpg)  
Fig. 4. $R ^ { * }$ (a: left) and δ\* (b: right) as functions of energy shortage price ratio r with $( \overline { { B } } = 5 H )$ and without a battery $( \overline { { B } } = 0 )$ in both w-c and wo-c agreements.

![](/api/attachments/CKMCDPZ2/fulltext/images/9c0eea2e682a715b07fa76b76f5621978b6cfb83cb68282e8e470869aa650a75.jpg)

![](/api/attachments/CKMCDPZ2/fulltext/images/ff0346175cbb080b323288ca1796f618a62e683c7825835295ce9115d54a4f1d.jpg)  
Fig. 5. R\* (a: left) and δ\* (b: right) as functions of battery size B with energy shortage price ratios $r _ { s } = 1 . 1 , 3$ in both w-c and wo-c agreements.

## 8. Summary of implications

The buyer in a PPA might prefer that the REP under-commits, overcommits, or chooses TEC, depending on the cost and complexities of handling surplus or shortage. PPA prices and structure, if chosen prop erly, can incentivize the REP to behave according to the buyer’s preferences. Designing such a win-win PPA structure should also ac count for the existence and size of the REP battery and its impact on the buyer and the REP. Accordingly and based on our earlier findings, we summarize the impact of batteries on REP revenue and behavior in Table 1. In Zone 1, batteries do not have a noticeable impact on either the REP revenue or the REP behavior. In Zone 2, adding batteries slightly improves the revenue of the REP in both w-c and wo-c agreements. The impact of batteries on quantity adjustments of the REP is stronger and in opposite directions for a w-c and a wo-c agreement. In a w-c agreement, batteries help steer the REP forward behavior towards TEC. In contrast, in a wo-c agreement, batteries encourage the REP to become more greedy and deviate farther from TEC. Finally, Zone 3 is the only zone in which batteries significantly improve the REP revenue as well as the quantity adjustment for both w-c and wo-c agreements. From both analysis and simulation results, we learn that the rate of improvement is slower in revenue gain than in quantity adjustments. Thus, battery sizes must be kept limited in a win-win PPA. Beyond a certain threshold, investing in larger battery sizes increases the revenue of the REP, but might not help improve the quantity adjustments (to benefit the buyer) any further.

Effects of adding batteries on (1) the REP (seller) revenue and (2) the company (buyer) quantity adjustment.

<table><tr><td rowspan="2"></td><td colspan="2">Zone 1</td><td colspan="2">Zone 2</td><td colspan="2">Zone 3</td></tr><tr><td>w-c</td><td>wo-c</td><td>w-c</td><td>wo-c</td><td>w-c</td><td>wo-c</td></tr><tr><td>REP (Seller)</td><td>~0</td><td>~0</td><td>+</td><td>+</td><td>++</td><td>++</td></tr><tr><td>Company (Buyer)</td><td>~0</td><td>~0</td><td>++</td><td>-</td><td>+++</td><td>+++</td></tr></table>

These observations lead to guidelines for structuring a win-win PPA (see Fig. 6). The design of such a PPA is highly dependent on whether the REP owns storage. If the REP does not own storage, then the price ratios used in the PPA can be fine-tuned to incentivize the REP to report for ward commitments according to the buyer’s preference for under/over commitment. This means that $r _ { s }$ and $r _ { e }$ can be set according to $p ^ { * }$ (see Definition 3). Finally, the forward unit price $c _ { d }$ (See Section 4.1) can be adjusted to make the PPA financially attractive for the REP.

If the REP owns storage, a PPA should limit the size of storage to maintain financial attractiveness for the buyer. In a win-win scenario, storage is used to simultaneously improve the REP revenue and to align the REP behavior with the buyer’s preferences. If the buyer favors that the REP under-commits $( \delta \le 0 )$ , then a win-win PPA structure is to set the PPA price ratios in Zone 3 and to enforce a maximum limit on the battery size. Corollary 4 sheds light on what the shape and functional ities of such maximum allowable battery sizes are. If the buyer prefers that the REP over-commits $\left( \delta \ge 0 \right)$ , a win-win PPA structure is to set the PPA price ratios in Zone 2. In this case, under a w-c agreement, there should be a limit on the minimum battery size, while under a wo-c agreement, there should be a limit on the maximum battery size.

## 9. Conclusions

Companies are actively seeking ways to reduce their carbon foot prints. Corporate Power Purchase Agreements (PPA), bilateral contracts between renewable energy producers (REP) and companies, are among the most convenient and popular solutions. While REPs benefit from the price certainty of PPAs, these contracts might bring energy production uncertainty to the companies. In this work, we investigated how to use the design flexibility of PPAs to set up a win-win strategy for buyers and sellers.

We found that the parameters of a PPA can be chosen to reduce supply uncertainty risks to satisfy the buyer, while maintaining financial attractiveness to the REP. To be more precise, we first showed how PPA pricing and structure can affect the behavior of a profit-maximizing REP with and without battery storage. Then, we developed a decision tree that shows how to select pricing and storage limitations that will incentivize the REP to behave in a way that is desirable to the buyer, yet profitable for themselves.

We used both simulation and analytical approaches to reach our conclusions. We provided a closed-form solution for a general scenario when the REP does not own battery storage, and under some simplifying assumptions when the REP owns battery storage. For the latter case, we apply the theory of stochastic network calculus (SNC) to model the behavior and the revenue of the REPs in a PPA. Our derivations showed that, depending on the buyer’s preferences, increasing the battery size can have a stronger impact on improving REP behavior to the advantage of the buyer than on REP profitability, with respective rates of $\Theta ( \log ^ { - 1 } ( B ) )$ ) and Θ(B<sup>−</sup> <sup>1</sup> log (B)), where B is the battery size. This suggests that in the presence of storage, some limitations on storage size should be considered in a win-win PPA structure. Our simulation studies confirmed this theoretical observation and further gave a more holistic view of the impact of different PPA pricing and structures on the revenue and behavior of REPs.

This work can be extended by considering other relevant practical scenarios. For example, here we assumed that the REP is risk-neutral, only the REP owns storage, the buyer is a company (and not an en ergy trader), and there is one PPA. Modifying any of these assumptions will represent a different and perhaps another practical application and can be a possibility for future work.

![](/api/attachments/CKMCDPZ2/fulltext/images/a559028c27f69ed86516de9af7e0a24240c2a741da509f59ccd2a7ff2c5c3e7b.jpg)  
Fig. 6. Decision making tree for setting up a win-win PPA structure. Notation. B?: Does the REP own a battery storage? δ?: Does the buyer prefer over-commitment $\left( \delta \ge 0 \right)$ or under-commitment $( \delta \leq 0 ) ? , Z _ { 2 } , Z _ { 3 } , p ^ { * } ;$ ; pricing in Zone 2. Zone 3. and optimal pricing. $B \geq B ^ { m i n } , B \leq B ^ { m a x } , \bar { B } = 0 :$ (Respectively) The battery size should be larger than a certain value, to be smaller than a certain value, and to be zero

## Appendix A. Proofs

## A.1. Proof of Lemma 1

We first introduce and prove the following lemma:

Lemma A.1.1 If X is a non-negative real valued random variable, for any $q > 0 ;$ , we have

$$
\mathbb {E} \left[ [ q - X ] ^ {+} \right] = \int_ {0} ^ {q} \mathbb {P} (X <   x) d x\tag{22}
$$

$$
\mathbb {E} \left[ \left[ X - q \right] ^ {+} \right] = \int_ {q} ^ {\infty} \mathbb {P} (X > x) d x.\tag{23}
$$

Proof of Lemma A.1.1. We prove the first equality (Eq. (22)). The proof of the second equality is similar and omitted due to the space limit. Let $f _ { X }$ be the distribution function of X. Then,

$$
\begin{array}{c} \mathbb {E} [ [ q - X ] ^ {+} ] = \int_ {0} ^ {q} (q - u) f _ {X} (u) d u \\ = \int_ {0} ^ {q} \int_ {0} ^ {q - u} f _ {X} (u) d s d u = \int_ {0} ^ {\infty} \int_ {0} ^ {q - s} f _ {X} (u) d u d s \\ = \int_ {0} ^ {q} \mathbb {P} (X <   q - s) d s = \int_ {0} ^ {q} \mathbb {P} (X <   x) d x \end{array}
$$

where we use a change of variable $x = q - s$ in the last line. Combining $\operatorname { E q } . \ ( 3 )$ and Lemma A.1.1, yields

$$
\Pi = c _ {d} w - c _ {s} \int_ {0} ^ {w} \mathbb {P} (W <   x) d x + c _ {e} \int_ {w} ^ {\infty} \mathbb {P} (W > x) d x\tag{24}
$$

Changing variable x with $( 1 + y ) \widetilde { W }$ and replacing W and w from Eqs. (1–2), yields

$$
\Pi = c _ {d} \widetilde {W} \left[ (1 + \delta) - r _ {s} \int_ {0} ^ {\delta} \mathbb {P} (\varepsilon <   y) d y + r _ {e} \int_ {\delta} ^ {\infty} \mathbb {P} (\varepsilon > y) d y \right]\tag{25}
$$

Inserting this into the definition of R in Eq. (6) completes the proof.

## A.2. Proof of Theorem 1

In a w-c agreement, the last term in Eq. (7) is removed and hence,

$$
R = \delta - r _ {s} \int_ {- 1} ^ {\delta} \mathbb {P} (\varepsilon <   y) d y\tag{26}
$$

Thus, the optimal quantity adjustment for the REP (δ\*) is the solution to the following

$$
\left. \frac {\partial R}{\partial \delta} \right| _ {\delta = \delta^ {*}} = 1 - r _ {s} \mathbb {P} (\varepsilon <   \delta^ {*}) = 0\tag{27}
$$

which is equal to Eq. (8), accounting also for the boundary conditions − $\begin{array} { r } { - 1 \le \delta \le \delta ^ { m a x } } \end{array}$ and $\varepsilon \ge - 1$ . In a wo-c agreement, R is given by the complete form of Eq. (7). The optimal quantity adjustment, is obtained by setting the first derivative of R (with respect to δ) to zero. This is

$$
\left. \frac {\partial R}{\partial \delta} \right| _ {\delta = \delta^ {*}} = 1 - r _ {s} \mathbb {P} (\varepsilon <   \delta^ {*}) - r _ {e} \mathbb {P} (\varepsilon > \delta^ {*}) = 1 - r _ {e} - (r _ {s} - r _ {e}) \mathbb {P} (\varepsilon <   \delta^ {*}) = 0\tag{28}
$$

which leads to Eq. (8) considering the boundary conditions $- 1 \leq \delta \leq \delta ^ { m a x }$ and $\varepsilon \ge \mathbf { \varepsilon } - 1$ and assuming $r _ { e } \leq r _ { s } .$

## A.3. Proof of Theorem 2

We use the buffer-battery analogy, illustrated in Fig. 2b. For a buffer with size K, the queue length $q _ { t }$ at any time t, is given by Eq. (16), where A and $S _ { t } ,$ are respectively, the input traffic and service rate at time t. When buffer size K is large, the buffer overflow, the amount of input traffic that must be dropped because the buffer is ful $( \mathrm { i . e . , ~ } [ A _ { t } - S _ { t } + q _ { t - 1 } - K ] ^ { + } )$ , can be approximated by [35]:

$$
\left[ A _ {t} - S _ {t} + q _ {t - 1} - K \right] ^ {+} \approx \left[ \sup _ {0 \leq s \leq t} \left(A (s, t) - S (s, t) - K\right) \right] ^ {+},\tag{29}
$$

where $( s , t )$ represents the cumulative values in $\begin{array} { r } { [ s + 1 , t ] ; \mathrm { e } . g . , A ( s , t ) = \sum _ { \tau = s + 1 } ^ { t } A _ { \tau } } \end{array}$

Comparing the energy deficit formulation in $\mathbf { E q . } ( 1 7 )$ with buffer content formulation in Eq. (16), we can map the energy storage size B to the buffer size $K ,$ the energy deficit $\mathbf { \widehat { \mathbf { \phi } } } _ { b } ^ { d }$ to the buffer content $q ,$ the forward commitment w to the input traffic $A ,$ and the available energy W to the service rate S. In this mapping, the energy shortage $( \mathrm { i . e . , } E _ { s , t } = [ w _ { t } - W _ { t } + b _ { t - 1 } ^ { d } - B ] ^ { + } )$ is mapped to the buffer overflow, formulated in Eq. (29) (see Fig. 2a). Applying this mapping to Eq. (29), yields

$$
E _ {s, t} \approx \left[ \sup _ {0 \leq s \leq t} \left(w (s, t) - W (s, t) - B\right) \right] ^ {+},\tag{30}
$$

Accordingly, to make our derivation more tractable, we rewrite Eq. (47) as

$$
\Pi_ {t} = c _ {d} w _ {t} - \left(c _ {s} - c _ {b}\right) \mathbb {E} \left[ E _ {s, t} \right] - c _ {b} \mathbb {E} \left[ w _ {t} - W _ {t} \right] ^ {+}\tag{31}
$$

From Eq. (31), we find that we need to compute $\mathbb { E } [ [ w _ { t } - W _ { t } ] ^ { + } ]$ and $\mathbb { E } \big [ E _ { s , t } \big ]$ to formulate Π. Given the distribution of ε from Eq. (21), we have

$$
\mathbb {E} \left[ \left[ w _ {t} - W _ {t} \right] ^ {+} \right] = \frac {\widetilde {W}}{2 \lambda} e ^ {- \lambda | \delta |}\tag{32}
$$

and $\mathbb { E } \big [ E _ { s , t } \big ]$ is formulated in Lemma A.3.1, below. Combining Eq. (32), Lemma A.3.1, Eq. (31), and $\operatorname { E q } .$ (6) with some manipulations, leads to Eq. (18) and this completes the proof.

Lemma A.3.1. $\mathbb { E } \big [ E _ { s , t } \big ]$ in Eq. (30) can be approximated by

$$
\mathbb {E} \big [ E _ {s, t} \big ] \approx \frac {\widetilde {W} e ^ {- \theta \overline {{B}}}}{\theta}.\tag{33}
$$

where $\begin{array} { r } { \overline { { B } } = \frac { B } { w } } \end{array}$ and

$$
\theta = \frac {- 2 \lambda^ {2} \delta}{2 + \lambda^ {2} \delta^ {2}}.\tag{34}
$$

Proof of Lemma A.31. To formulate E $\left[ E _ { s , t } \right]$ , we first compute the CCDF of Y for some $y > 0$

$$
\begin{array}{l} \mathbb {P} \left(E _ {s, t} > y\right) = \mathbb {P} \left(\sup _ {0 \leq s \leq t} (w (s, t) - W (s, t) - B). > y\right) \\ = \mathbb {P} \left(\sup _ {0 \leq s \leq t} \left(\widetilde {W} \sum_ {\tau = s + 1} ^ {t} (\delta - \varepsilon_ {\tau})\right) > B + y\right) \\ = \mathbb {P} \left(\sup _ {0 \leq s \leq t} \left(\sum_ {\tau = s + 1} ^ {t} (\delta - \varepsilon_ {\tau})\right) > \overline {{B}} + \bar {y}\right) \end{array}\tag{35}
$$

where $\varepsilon _ { \tau }$ is assumed to be an iid random variable at any time τ with double exponential distribution as presented in Eq. (21). Moreover, $\begin{array} { r } { \overline { { B } } = \frac { B } { w } a n d \overline { { y } } = \frac { y } { w } . } \end{array}$ . For a fixed $\theta > 0$ and any $0 \leq n \leq t ,$ define $X _ { n }$ to be

$$
X _ {n} = e ^ {\theta \sum_ {\tau = t - n} ^ {t} (\delta - \varepsilon_ {\tau})}\tag{36}
$$

Combining $\operatorname { E q . }$ (35) and $\operatorname { E q } . \ ( 3 6 )$ , we have

$$
\mathbb {P} \big (E _ {s, t} > y \big) = \mathbb {P} \left(\sup _ {0 \leq n \leq t} X _ {n} > e ^ {\theta (\overline {{B}} + \bar {y})}\right)\tag{37}
$$

For any $\delta < 0 ,$ , the following shows that $X _ { n }$ is a super-martingale

$$
\mathbb {E} \left[ X _ {n + 1} \mid X _ {0}, \dots , X _ {n} \right] = \mathbb {E} \left[ e ^ {\theta \sum_ {\tau = t - n - 1} ^ {t} (\delta - \varepsilon_ {\tau})} \mid X _ {0}, \dots , X _ {n} \right]\tag{38}
$$

$$
= X _ {n} \mathbb {E} \left[ e ^ {\theta (\delta - \varepsilon_ {\tau - n - 1})} \right] \leq X _ {n},\tag{39}
$$

where in the second line, we used the fact that $\delta < 0$ and $\scriptstyle { \varepsilon _ { \tau - n - 1 } }$ is a symmetric random variable over 0 and hence, $\mathbb { E } \big [ e ^ { \theta ( \delta - \varepsilon _ { \tau - n - 1 } ) } \big ] \leq 1$ . Using Doob’s inequality in a similar way as used by [36] and exploiting the fact that $X _ { n }$ is a supermartingale, we compute a tight upper bound on Eq. (35):

$$
\mathbb {P} \bigg (s u p _ {0 \leq n \leq t} X _ {n} > e ^ {\theta (\overline {{B}} + \overline {{y}})} \bigg) \leq \mathbb {E} [ X _ {0} ] e ^ {- \theta (\overline {{B}} + \overline {{y}})}\tag{40}
$$

From Eq. (36), we know that $\mathbb { E } [ X _ { 0 } ] = 1$ . The upper bound in Eq. (40) can be tightened by optimizing over $\theta ,$ which is a free parameter. It has been shown by [36] that if θ is the solution to:

$$
\mathbb {E} \left[ e ^ {\theta (\delta - \varepsilon)} \right] = 1\tag{41}
$$

the upper bound in $\operatorname { E q . }$ . (40) will be tight enough to be used as an approximation of the right hand side of $\operatorname { E q . }$ (40). Such a $\theta > 0 ,$ , satisfying Eq. (41),

always uniquely exists, because

$$
\left. \frac {\partial \mathbb {E} \left[ e ^ {\theta (\delta - \varepsilon)} \right]}{\partial \theta} \right| _ {\theta = 0} \leq 0\tag{42}
$$

and $\mathbb { E } \big [ e ^ { \theta ( \delta - \varepsilon ) } \big ] \big | _ { \theta = 0 } = 0$ and $\mathbb { E } \big [ e ^ { \theta ( \delta - \varepsilon ) } \big ] \big | _ { \theta = \infty } > 0$ . Using the standard double exponential distribution function o $\mathrm { : } f _ { \varepsilon }$ from Eq. (21), we also have

$$
\mathbb {E} \left[ e ^ {- \theta \varepsilon} \right] = \frac {1}{2} \left[ \frac {\lambda}{\lambda - \theta} + \frac {\lambda}{\lambda + \theta} \right] = \frac {\lambda^ {2}}{\lambda^ {2} - \theta^ {2}}\tag{43}
$$

Replacing this in Eq. (41) and replacing $e ^ { \theta \delta }$ by the first three terms of its Taylor’s series, yields

$$
1 + \delta \theta + \delta^ {2} \theta^ {2} / 2 \approx 1 - \theta^ {2} / \lambda^ {2} \Rightarrow \theta \approx \frac {- 2 \lambda^ {2} \delta}{2 + \lambda^ {2} \delta^ {2}}\tag{44}
$$

Thus,

$$
\mathbb {P} \left(E _ {s, t} > y\right) \approx e ^ {- \theta (\overline {{B}} + \bar {y})}\tag{45}
$$

Accordingly, we can compute $\mathbb { E } \big [ E _ { s , t } \big ]$ as follows, which completes the proof of Lemma A.31:

$$
\begin{array}{l} \mathbb {E} \left[ E _ {s, t} \right] = \mathbb {E} [ s u p _ {0 \leq s \leq t} \{w (t - s) - W (s, t) - B \} ] \\ = \int_ {0} ^ {\infty} \mathbb {P} \big (E _ {s, t} > y \big) d y \stackrel {{\overline {{y}} := y / \widetilde {W}}} {{=}} \widetilde {W} \int_ {0} ^ {\infty} \mathbb {P} \left(\frac {E _ {s , t}}{\widetilde {W}} > \overline {{y}}\right) d \overline {{y}} \\ \approx \widetilde {W} \int_ {0} ^ {\infty} e ^ {- \theta (\overline {{B}} + \overline {{y}})} d \overline {{y}} = \frac {\widetilde {W} e ^ {- \theta \overline {{B}}}}{\theta}. \end{array}\tag{46}
$$

## A.4. Proof of Lemma 2

Under the assumption of ideal storage, and some manipulations, $\operatorname { E q } .$ . (15) will be reduced to

$$
\Pi_ {t} = c _ {d} w _ {t} - \left(c _ {s} - c _ {b}\right) \mathbb {E} \left[ w _ {t} - W _ {t} - b _ {t - 1} \right] ^ {+} - c _ {b} \mathbb {E} \left[ w _ {t} - W _ {t} \right] ^ {+} + c _ {e} \mathbb {E} \left[ \left[ W _ {t} - w _ {t} - b _ {t - 1} ^ {d} \right] ^ {+} \right].\tag{47}
$$

Inserting these revenue formulations in Eq. (6), we get the corresponding R values.

In a w-c agreement, storing and restoring one unit of energy costs $c _ { b } ,$ , but saves $c _ { s }$ compared to the case where there is no storage. Thus, the necessary condition for the profitability of the storage in w-c agreements is $c _ { s } > c _ { b }$ or equivalently $r _ { b } < r _ { s } .$ . In a wo-c agreement, each unit of energy in storage has been added to storage at a time when there was energy surplus beyond forward commitments of the REP. At that time, without storage, this unit of energy would have received $c _ { e }$ according to the PPA. Storing this unit of energy in the storage costs $c _ { b } .$ At a later time when withdrawn from storage to compensate for an energy shortage occasion, this unit of energy saves $c _ { s }$ of the penalty with respect to a storage-less scenario. Accounting for all costs and revenue, the necessary condition of storage profitability in wo-c agreements is $c _ { b } < c _ { s } - c _ { e } \mathrm { o r } , r _ { b } < r _ { s } - r _ { e }$

## A.5. Proof of Theorem 3

From θ formulation in Theorem $^ { 2 , }$ for small values of $\delta < 0 ,$ we can approximate θ by $\begin{array} { r } { \operatorname* { l i m } _ { \delta \to 0 ^ { - } } \theta = - \delta \lambda ^ { 2 } } \end{array}$ . Inserting this in Theorem $^ { 2 , }$ yields

$$
R = \delta + \frac {\left(r _ {s} - r _ {b}\right)}{\delta \lambda^ {2}} e ^ {\delta \lambda^ {2} \overline {{B}}} - \frac {r _ {b}}{2 \lambda} e ^ {\lambda \delta}\tag{48}
$$

Taking the first derivative of R with respect to $\delta ,$ we have

$$
\frac {\partial R}{\partial \delta} = 1 + \frac {\overline {{B}} (r _ {s} - r _ {b})}{\delta} e ^ {\delta \lambda^ {2} \overline {{B}}} - \frac {r _ {s} - r _ {b}}{\lambda^ {2} \delta^ {2}} e ^ {\delta \lambda^ {2} \overline {{B}}} - \frac {r _ {b}}{2} e ^ {\lambda \delta}\tag{49}
$$

Given that $\delta \to 0 ^ { - }$ , the last term in Eq. (49) can be approximated by - $- \frac { r _ { b } } { 2 \lambda } .$ Moreover, assuming that $\overline { B }$ is large enou $^ { \mathrm { g h , } }$ we can ignore the third term in Eq. (49) compared to the second term. Incorporating all of these approximation, Eq. (49) can be approximated by

$$
\frac {\partial R}{\partial \delta} \approx 1 + \frac {\overline {{B}} (r _ {s} - r _ {b})}{\delta} e ^ {\delta^ {*} \lambda^ {2} \overline {{B}}} - \frac {r _ {b}}{2}\tag{50}
$$

Hence, the optimal δ can be obtained by setting the leftover of $\operatorname { E q . }$ (50) to zero, which is

$$
\delta^ {*} e ^ {- \delta^ {*} \lambda^ {2} \overline {{B}}} = \frac {2 \overline {{B}} (r _ {s} - r _ {b})}{2 - r _ {b}}\tag{51}
$$

Solving $\operatorname { E q . }$ . (51) for $\delta ^ { * }$ , gives us $\operatorname { E q } .$ . (19), and this completes the proof.

## A.6. Proof of Corollary 3

We first prove that $R ^ { * }$ and $\delta ^ { * }$ are monotonically non-decreasing in B and then prove the boundary conditions:

• Proving that $R ^ { * }$ and $\delta ^ { * }$ are monotonically non-decreasing in B:

Please first note that B and $\overline { B }$ only differ by a positive scalar; hence, a monotonic behavior with respect to B implies the same with respect to ${ \overline { { B } } } .$ In a w-c agreement, b is the only parameter that varies by B in $\mathbf { E q . } \left( 4 7 \right)$ ) and is monotonically non-decreasing in B. Thus, the REP expected revenue from Eq. (47) (and so is R) is non-decreasing in B since $c _ { s } > c _ { b }$ . Since R is monotonically non-decreasing in ${ \overline { { B } } } ,$ so is $R ^ { * }$ , which is the maximum value of R for a fixed B.

To prove the non-decreasing trend of $\delta ^ { * }$ as B increases, we use contradiction. Consider two storage sizes $B _ { 1 }$ and $B _ { 2 }$ where, $B _ { 2 } > B _ { 1 }$ . Suppose that $\delta _ { 1 } { } ^ { * }$ and $\delta _ { 2 } { } ^ { * }$ are, respectively, the optimum quantity adjustment under $B _ { 1 }$ and $B _ { 2 } .$ Also $w _ { 1 } { } ^ { * }$ and $w _ { 2 } ^ { * }$ are, respectively, the corresponding energy com mitments to $\delta _ { 1 } { } ^ { * }$ and $\delta _ { 2 } { } ^ { * }$ and define $\Delta = w _ { 1 } { ^ { * } } - w _ { 2 } { ^ { * } }$ . By the contradiction assumption, ${ \delta _ { 2 } } ^ { * } < { \delta _ { 1 } } ^ { * } \left( \mathrm { i } . \mathrm { e } . , \Delta > 0 \right)$ . The expected revenue of REP with $B = B _ { 2 }$ is larger in $\delta _ { 2 } { } ^ { * }$ than in ${ { \delta } _ { 1 } } ^ { * }$ , which means that the different of expected revenue between $w = w _ { 2 } { ^ * }$ and $w = w _ { 1 } { } ^ { * }$ must be positive

$$
\left. \Pi \right| _ {B = B _ {2}, w = w _ {2} ^ {*}} - \left. \Pi \right| _ {B = B _ {2}, w = w _ {1} ^ {*}} = - c _ {d} \Delta + a _ {1} c _ {b} \Delta + a _ {2} (c _ {s} - c _ {b}) \Delta > 0\tag{52}
$$

for some $a _ { 1 }$ and $^ { a _ { 2 } , }$ where $0 < a _ { 2 } < a _ { 1 } \leq 1$ from Eq. (47). From Eq. (52), the difference between the expected revenues with $w = w _ { 2 } ^ { * }$ and $w = w _ { 1 } { } ^ { * }$ , when $B = B _ { 1 }$ is

$$
\left. \Pi \right| _ {B = B _ {1}, w = w _ {2} ^ {*}} - \left. \Pi \right| _ {B = B _ {1}, w = w _ {1} ^ {*}} = - c _ {d} \Delta + a _ {1} c _ {b} \Delta + a _ {3} (c _ {s} - c _ {b}) \Delta > 0\tag{53}
$$

for some $a _ { 3 } ,$ where $0 < a _ { 2 } < a _ { 3 } < a _ { 1 } \leq$ 1 from Eq. (47). This means that with the original storage size $B _ { 1 } , R$ is larger at $\delta _ { 2 } { } ^ { * }$ than at ${ { \delta } _ { 1 } } ^ { * }$ and this contradicts the assumption and proves the claim.

• Proving the boundary conditions:

$\begin{array} { r } { \mathbf { \nabla } \cdot \overline { { B } } = 0 : } \end{array}$ In a storage-less scenario, where $\begin{array} { r } { \overline { { B } } = 0 , } \end{array}$ , the relative expected revenue of the REP in a w-c agreement can be obtained from Eq. (8) with $\begin{array} { r } { f _ { \varepsilon } ( \pmb { x } ) = \frac { \lambda } { 2 } e ^ { - \lambda | \pmb { x } | } } \end{array}$ (which is the assumption on $f _ { \varepsilon }$ in this section) is given by

$$
\delta_ {m i n} = \frac {1}{\lambda} \log \left(\frac {2}{r _ {s}}\right)\tag{54}
$$

Replacing this optimal commitment in Lemma 1 in a w-c agreement, we have

$$
R _ {m i n} = \delta_ {m i n} - \frac {r _ {s}}{2 \lambda} e ^ {\lambda \delta_ {m i n}} = \frac {1}{\lambda} \left(\log \left(\frac {2}{r _ {s}}\right) - 1\right)\tag{55}
$$

•B→∞: When B is large, we have

$$
\begin{array}{c} \frac {l i m}{\overline {{B}} \to \infty}   \delta^ {*} = - \frac {l i m}{\overline {{B}} \to \infty}   \frac {1}{\lambda^ {2} \overline {{B}}}   \mathbb {W} \left(\frac {2 \lambda^ {2} \overline {{B}} ^ {2} (r _ {s} - r _ {b})}{2 - r _ {b}}\right) \\ = - \frac {l i m}{\overline {{B}} \to \infty}   \frac {1}{\lambda^ {2} \overline {{B}}}   \Theta \Big (l o g \Big (\overline {{B}} ^ {2} \Big) \Big) = - \frac {l i m}{\overline {{B}} \to \infty}   \underbrace {\Theta \left(\frac {l o g \Big (\overline {{B}} \Big)}{\overline {{B}}}\right)} _ {\text { Conv. rate }} = 0 \end{array}\tag{56}
$$

where we use the fact that $\mathbb { W } \bigg ( \overline { { B } } ^ { 2 } \bigg ) = O \bigg ( l o g \overline { { B } } \bigg )$ . Replacing this in Theorem $^ { 2 , }$ yields

$$
\lim _ {\overline {{B}} \rightarrow \infty} R ^ {*} = \lim _ {\overline {{B}} \rightarrow \infty} \left(\delta^ {*} - \left(r _ {s} - r _ {b}\right) \frac {e ^ {- \theta \overline {{B}}}}{\theta} - \frac {r _ {b}}{2 \lambda} e ^ {- \lambda \delta^ {*}}\right)\tag{57}
$$

Since $\begin{array} { r } { \delta ^ { * } = \Theta \Bigg ( \frac { l o g \left( \overline { { B } } \right) } { \overline { { B } } } \Bigg ) } \end{array}$ from Eq. (56), we have

$$
\theta = \frac {- \delta^ {*} \lambda^ {2}}{2 + \delta^ {* 2} \lambda^ {2}} = \Theta \left(\frac {\log (\overline {{B}})}{\overline {{B}}}\right)\tag{58}
$$

Replacing Eq. (58) in Eq. (57), yields

$$
\lim _ {\overline {{B}} \rightarrow \infty} R ^ {*} = \lim _ {\overline {{B}} \rightarrow \infty} \left(\Theta \left(\frac {\log (\overline {{B}})}{\overline {{B}}}\right) - (r _ {s} - r _ {b}) \Theta \left(\log^ {- 1} (\overline {{B}})\right) - \frac {r _ {b}}{2 \lambda} e ^ {- \lambda \Theta \left(\frac {\log (\overline {{B}})}{\overline {{B}}}\right)}\right)
$$

$$
= \lim _ {\overline {{B}} \rightarrow \infty} \left(\underbrace {\Theta (\log^ {- 1} (\overline {{B}}))} _ {\text { Conv.   rate }} - \frac {r _ {b}}{2 \lambda}\right) = - \frac {r _ {b}}{2 \lambda}\tag{59}
$$

and this completes the proof.

## A.7. Proof of Corollary 4

Denote δ and $\delta ^ { * } { } _ { ; }$ , respectively, the target and the optimal quantity adjustments. Thus, we must have $\delta ^ { * } \geq \delta .$ The optimal quantity adjustment of a REP with storage from Eq. (19). $\begin{array} { r } { \mathrm { I f } \frac { 1 } { \lambda } l o g \bigg ( \frac { 2 } { r _ { s } } \bigg ) > \delta , } \end{array}$ then according to Corollar $3 , \delta ^ { * } \geq \delta$ for any value of B and hence, the minimum storage needed is ${ \overline { { B } } } =$ 0. Otherwise, the right-hand-side of Eq. (19) must be equal to the target quantity adjustment δ to find the minimum required storage size. This means that we should equate the right-hand-side of Eq. (19) to δ and solve it for B, which i

$$
\overline {{{B}}} = \frac {1}{\delta \lambda^ {2}} \mathbb {W} _ {- 1} \left(\frac {- \delta^ {2} \lambda^ {2} (2 - r _ {b})}{2 (r _ {s} - r _ {b})}\right)\tag{60}
$$

where $\mathbb { W } _ { - 1 }$ is the negative branch of the Lambert W function and this completes the proof.

## Appendix B. Table of notation

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $c_d$ </td><td>Price per unit of energy for forward commitments ($/Wh)</td></tr><tr><td> $c_s$ </td><td>Penalty price for each unit of energy shortage w.r.t. the forward commitments ($/Wh)</td></tr><tr><td> $c_e$ </td><td>Rebate price for each unit of excess energy w.r.t. the forward commitments ($/Wh)</td></tr><tr><td> $c_b$ </td><td>Price of battery deficiency (per unit of energy flux) ($/Wh)</td></tr><tr><td> $r_s$ </td><td>Energy shortage price ratio ( $c_s/c_d$ )</td></tr><tr><td> $r_e$ </td><td>Excess energy price ratio ( $c_e/c_d$ )</td></tr><tr><td> $r_b$ </td><td>Battery LCOS price ratio ( $c_b/c_d$ )</td></tr><tr><td> $w_t$ </td><td>Energy forward commitment for a future time t (Wh)</td></tr><tr><td> $W_t$ </td><td>Realized available energy at time t (Wh)</td></tr><tr><td> $\tilde{W}_t$ </td><td>Estimated available energy at time t (Wh)</td></tr><tr><td> $\varepsilon$ </td><td>Relative estimation error</td></tr><tr><td> $(\delta_{t}^*) \delta_t$ </td><td>(Optimal) Quantity adjustment at time t</td></tr><tr><td> $p^*$ </td><td>Optimal PPA price ratio in a storage-less scenario (Definition 3)</td></tr><tr><td> $\delta_{t}^{max}$ </td><td>Maximum allowable quantity adjustment at time t</td></tr><tr><td> $\Pi_t$ </td><td>Expected overall revenue of the REP for the delivery time t ($)</td></tr><tr><td> $(R^*) R$ </td><td>(Optimal) expected relative REP revenue</td></tr><tr><td> $B(\overline{B})$ </td><td>Battery size in Wh (in terms of the number of time units it can store average supply)</td></tr><tr><td> $b_t(b_t^d)$ </td><td>Battery (deficit) state of charge at time t (Wh)</td></tr><tr><td> $\eta^{ch}(\eta^{dc})$ </td><td>Charging (Discharging) efficiency</td></tr><tr><td> $\overline{E}^{ch}(\overline{E}^{dc})$ </td><td>Maximum charging (discharging) energy intake (output) in one time unit (Wh)</td></tr><tr><td>D</td><td>Depth of discharge</td></tr><tr><td> $E_{d,t}$ </td><td>Part of realized energy used to account for the forward commitment at time t (Wh)</td></tr><tr><td> $E_{e,t}$ </td><td>Excess energy beyond forward commitments to be taken by the buyer at time t (Wh)</td></tr><tr><td> $E_{s,t}$ </td><td>Energy shortage below forward commitments observed by the buyer at time t (Wh)</td></tr><tr><td> $E_{c,t}(E_{b,t})$ </td><td>Energy to be charged (discharged) to (from) the battery at time t (Wh)</td></tr><tr><td> $f_{\varepsilon}(\mathcal{F}_{\varepsilon})$ </td><td>Probability distribution function (cumulative distribution function) of  $\varepsilon$ </td></tr><tr><td>PPA</td><td>Power purchase agreement</td></tr><tr><td>REP</td><td>Renewable energy producer</td></tr><tr><td>w-c (wo-c)</td><td>PPA with-(without-)curtailing payment for surplus energy</td></tr><tr><td>TEC</td><td>True estimate commitment</td></tr><tr><td>LCOS</td><td>Levelized cost of storage</td></tr></table>

## References

[1] CDP and WWF and C, Investments and Ceres, How the largest us companies are capturing business value while addressing climate change?, in: Tech. Rep. Power Forward 3.0. 2018. Feb. https://c402277.ssl.cf1.rackcdn.com/publications/1049/ files/origina.

[2] Bloomberg NEF. Corporate Clean Energy Buving Leapt 44% in 2019. Sets New Record. https://about.bnef.com/blog/. 2020.

[3] P. Wallace, Long-term power purchase agreements: the factors that influence contract design, in: Research Handbook on International and Comparative Sale of Goods Law, Edward Elgar Publishing, 2019.

[4] C. Aslan, T. Irwin, Power to the fiscal ? An exploration of the use of credit ratings to estimate the expected cost of a guarantee of a power-purchase agreement. in: Tech. Rep. Policy Research working paper: WPS 9271, World Bank Group, 2020. Jun.

[5] PWC, Corporate Renewable Energy Procurement Survey Insights. https://www.een ews net/assets/2017/05/11/document ew 02 pdf, 2016

[6] Delmarva Power & Light Company, Renewable Wind Energy Power Purchase Agreement. http://www.delmarva.com/uploadedFiles/wwwdelmarvacom/A ESPPA pdf 2008

[7] O.Q. Wu, V. Babich, Unit-contingent power purchase agreement and asymmetric information about plant outage, Manuf. Serv. Oper. Manag. 14 (2) (2012) 165–353.

[8] CORE International Inc, Namibia IPP and Investment Market Framework Technical Assistance: Annex X Model PPA for Medium Scale IPPs. https://library.ppp knowledgelab.org/PPPIRC/documents/1601/download. 2006

[9] World Bank Group, Sample Power Purchase Agreement. https://ppp.worldbank.or g/public-private-partnership/library/power-purchase-agreement-ppa-example-1, 2007.

[10] World Business Council for Sustainable Development, Purchase Agreement Structures. https://www.wbcsd.org/contentwbc/download/4468/60118. 2018

[11] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decis. Support. Syst. 43 (3) (2007) 1044–1061.

[12] A. Mattiussi, M. Rosano, P. Simeoni, A decision support system for sustainable energy supply combining multi-objective and multi-attribute analysis: an australian case study, Decis. Support. Syst. 57 (2014) 150–159.

[13] X. Lei, P.A. Sandborn, Maintenance scheduling based on remaining useful life predictions for wind farms managed using power purchase agreements, Renew. Energy 116 (2018).188–198

[14] B. Tranberg, R.T. Hansen, L. Catania, Managing volumetric risk of long-term power purchase agreements, Energy Econ. 85 (2020) 104567.

[15] A. Trivella, Decision Making Under Uncertainty in Sustainable Energy Operations and Investments. Ph.D. thesis. Technical University of Denmark. Lyngby. Denmark 2018.

[16] A. Trivella, S. Nadarajah, S.-E. Fleten, D. Mazieres, D. Pisinger, Managing Shutdown Decisions in Merchant Commodity and Energy Production: A Social Commerce Perspective, Accepted in: Manufacturing & Service Operations Management, 2020, https://doi.org/10.1287/msom.2019.0850.

[17] B. Allaz, Oligopoly, uncertainty and strategic forward transactions, Int. J. Ind. Organ. 10 (2) (1992) 297–308.

[18] N. Secomandi, S. Kekre, Optimal energy procurement in spot and forward markets, Manuf. Serv. Oper. Manag. 16 (2) (2014) 270–282.

[19] K. Ito, M. Reguant, Sequential markets, market power, and arbitrage, Am. Econ. Rev. 106 (7) (2016) 1921–1957.

[20] H. Zhang, F. Gao, J. Wu, K. Liu, X. Liu, Optimal bidding strategies for wind power producers in the day-ahead electricity market, Energies 5 (11) (2012) 4804–4823.

[21] N. Lohndorf, ¨ S. Minner, Optimal day-ahead trading and storage of renewable energies—an approximate dynamic programming approach, Energy Syst. 1 (1) (2010) 61–77.

[22] J.M. Morales, A.J. Conejo, H. Madsen, P. Pinson, M. Zugno, Trading stochastic production in electricity pools, in: Integrating Renewables in Electricity Markets, no. 205 in International Series in Operations Research & Management Science, Springer, US, 2014, pp. 205–242.

[23] M. Al-Gwaiz, X. Chao, O.Q. Wu, Understanding how generation flexibility and renewable energy affect Power market competition, Manuf. Serv. Oper. Manag. 19 (1) (2016) 114–131.

[24] O.Q. Wu, R. Kapuscinski, Curtailing intermittent generation in electrical systems, Manuf. Serv. Oper. Manag. 15 (4) (2013) 578–595.

[25] D. D’Achiardi, N. Aguiar, S. Baros, V. Gupta, A.M. Annaswamy, Reliability contracts between renewable and natural gas power producers, IEEE Trans. Control Netw. Syst. 6 (3) (2019) 1075–1085.

[26] N. Aguiar, V. Gupta, P.P. Khargonekar, A real options market-based approach to increase penetration of renewables, IEEE Trans. Smart Grid 11 (2) (2020) 1691–1701.

[27] A. Roos, T.F. Bolkesjø, Value of demand flexibility on spot and reserve electricity markets in future power system with increased shares of variable renewable energy, Energy 144 (2018) 207–217.

[28] Y.H. Zhou, A. S-W, N. Secomandi, S. Smith, Electricity trading and negative prices: storage vs. disposal, Manag. Sci. 62 (3) (2015) 880–898.

[29] D.R. Jiang, W.B. Powell, Optimal hour-ahead bidding in the real-time electricity market with battery storage using approximate dynamic programming, INFORMS J. Comput. 27 (3) (2015) 525–543.

[30] M.T. Kahlen, W. Ketter, J. van Dalen, Electric vehicle virtual power plant dilemma: grid balancing versus customer mobility, Prod. Oper. Manag. 27 (11) (2018) 2054–2070.

[31] Y. Ghiassi-Farrokhfal, W. Ketter, J. Collins, Designing a battery-friendly electricity market, in: International Conference on Information Systems (ICIS), 2017.

[32] J.H. Kim, W.B. Powell, Optimal energy commitments with storage and intermittent supply, Oper. Res. 59 (6) (2011) 1347–1360.

[33] F. Kazhamiaka, Y. Ghiassi-Farrokhfal, S. Keshav, C. Rosenberg, Comparison of different approaches for solar PV and storage sizing, IEEE Trans. Sustain. Comp. (2019), https://doi.org/10.1109/TSUSC.2019.2946246.

[34] Y. Ghiassi-Farrokhfal, S. Keshav, C. Rosenberg, Toward a realistic performance analysis of storage systems in smart grids. JEEE Trans. Smart Grid 6 (1) (2015) 402-410.

[35] S. Singla, Y. Ghiassi-Farrokhfal, S. Keshav, Using storage to minimize carbon footprint of diesel generators for unreliable grids. JEEE Trans. Sustain. Energy 5 (4) (2014).1270–1277

[36] F. Poloczek, F. Ciucu, Service-martingales: Theory and applications to the delay analysis of random access protocols, in: IEEE Conference on Computer Communications (INFOCOM), 2015, pp. 945–953.

Yashar Ghiassi-Farrokhfal is an Assistant Professor at the Department of Technology and Operations Management at the Rotterdam School of Management of the Erasmus

University. Additionally, he is the academic director of Smart Cities and Smart Energy at the Erasmus Center for Data Analytics (ECDA). He holds a PhD degree in Electrical and Computer Engineering from University of Toronto, Canada and was a postdoctoral researcher at the Computer Science department of University of Waterloo, Canada. His research interests include modelling energy systems for investment and operational de cisions, Microgrids, electric vehicles, integrating renewable energy and dealing with its uncertainty, energy storage modelling, market mechanisms at retail, wholesale, and bilateral levels. Because of his academic background. he has a multi-disciplinary approach and as a result, has published in top journals across different disciplines including: Energy Economics (Applied Energy), Data Analytics (Journal of Cleaner Production, International Journal of Energy Research), Computer Science/Electrical Engineering (IEEE Transactions on Sustainable Computing, IEEE Transactions on Smart Grids, IEEE Transactions on Sus tainable Energy). He has also been actively connecting research communities across these disciplines to learn from each other. He does so by serving as a co-chair, an associate editor, and a member of technical program committees in most popular conferences in each discipline such as ACM e-Energy, International Conference on Information Systems (ICIS), Workshop on Information Technologies and Systems (WITS), IEEE smartgridcomm, etc.

Professor Wolfgang Ketter is Director of the Institute of Energy Economics and Chaired Professor of Information Systems, University of Cologne. He is also Academic Director of the Erasmus Centre for Data Analytics and Director of the Erasmus Centre for Future En ergy Business at the Rotterdam School of Management, Erasmus University, where he is Professor of Next Generation Information Systems. He leads a team of interdisciplinary researchers in discovering how we can rapidly exploit advances in computing power to create a faster, more sustainable transition to clean energy and mobility. Ketter is advancing a new paradigm that builds communities of researchers who learn from each other in fast-paced competitive environments that model important societal challenges, such as the future of energy markets. He is co-founder of one of the world’s largest AIdriven market simulation platforms. PowerTAC . As fellow and member of the WEF Global Future Council on Mobility and Energy Policy Advisor to the German government, his focus is on developing collaboration with business and policymakers to field-test digitalization of the energy landscape in projects such as the EU’s Ruggedized smart-city initiative and the Rotterdam Port Energy Cooperative. He has served as editor for ISR and MISQ.

John Collins started his career in 1969, working as an electrical engineer at a large industrial firm in product development and corporate research, where he was awarded 16 patents. He left in 1997 to work as an independent consultant in software engineering and technology analysis, and to return to school for his Doctorate in Computer Science at the University of Minnesota. After completing his Ph.D. in 2002, he joined the faculty as a Lecturer, and as Director of the professional Masters program in Software Engineering. Retired from the University since 2013, Collins remains an active researcher, working with colleagues and students in Rotterdam and Cologne, focused on electricity markets and the challenges of sustainability. In addition to his professional career, Collins has served on the Hudson Wisconsin School Board (1982-88). the Board of Directors for the Association fot Trading Agent Research (2006-09), and the University of Minnesota Science & Engi neering Curriculum and Review Committee (2004-08). He is currently President of the Friends of Willow River and Kinnickinnic State Parks, and a District Director of the St. Croix Electric Cooperative in Wisconsin.
