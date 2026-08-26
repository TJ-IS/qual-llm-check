---
otero_id: 12878
otero_key: "MDFAF8WD"
title: "Estimating Network Effects in Two-Sided Markets"
authors: "Oliver Hinz; Thomas Otter; Bernd Skiera"
year: "2020"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2019.1705509"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Estimating Network Effects in Two-Sided Markets

Oliver Hinz, Thomas Otter & Bernd Skiera

To cite this article: Oliver Hinz, Thomas Otter & Bernd Skiera (2020) Estimating Network Effects in Two-Sided Markets, Journal of Management Information Systems, 37:1, 12-38, DOI: 10.1080/07421222.2019.1705509

To link to this article: https://doi.org/10.1080/07421222.2019.1705509

![](/api/attachments/MDFAF8WD/fulltext/images/f21c4763b28c9bf641f5559fdad3946ac0df4b7a275af07ff6d6cc1ea79b6f5c.jpg)

Published online: 01 Mar 2020.

![](/api/attachments/MDFAF8WD/fulltext/images/6596ae7a9292d5cc28ace7e50efdca60826c8958f64ccd376a055680f16301d5.jpg)

Submit your article to this journal

![](/api/attachments/MDFAF8WD/fulltext/images/63b8e63d88be02f8ec4a189656f62f3eeae81453f49045d6e7d222fd7a5bdb86.jpg)

Article views: 11

![](/api/attachments/MDFAF8WD/fulltext/images/fb06a1ac6ac6cc7c60c6ebe1824754c25157e72a15c1af067206e2481dcf266b.jpg)

View related articles

![](/api/attachments/MDFAF8WD/fulltext/images/e814037a996cd63201b050730e5efd3e5dfcfc4dd237f9f26b8e9b2ba84802e6.jpg)

View Crossmark data

Check for updates

# Estimating Network E<sup>f</sup>ects in Two-Sided Markets

Oliver Hinz<sup>a</sup>, Thomas Otter<sup>a</sup>, and Bernd Skiera<sup>b</sup>

<sup>a</sup>Faculty of Business and Economics, Goethe University Frankfurt, Frankfurt am Main, Germany; <sup>b</sup>Faculty of Business and Economics, Goethe University Frankfurt (& Professorial Fellow at Deakin University, Australia), Frankfurt am Main, Germany

## ABSTRACT

The proliferation of the Internet has enabled platform intermediaries to create two-sided markets in many industries. Time-series data on the number of customers on both sides of the markets allow platform intermediaries for estimating the direction and magnitude of network e<sup>f</sup>ects, which can then support growth predictions and subsequent information technology (IT) or marketing investment decisions. This article investigates the conditions under which this estimation of sameside and cross-side network e<sup>f</sup>ects should distinguish between its impact on the number of new customers (i.e., acquisition) and existing customers (i.e., their activity). The authors propose an in<sup>fl</sup>ux-out<sup>fl</sup>ow model for doing so and conduct a simulation study to benchmark the new model against the traditional model. Further they compare the models in an illustrative empirical study in which they study the growth of an Internet auction platform. The results show that this separation of e<sup>f</sup>ects is bene<sup>fi</sup>cial because the existing customers on both sides of the market can in<sup>fl</sup>uence the acquisition and dropout of other customers asymmetrically. The paper thus makes an important contribution that should impact the way how researchers and business practitioners measure network e<sup>f</sup>ects in two-sided markets.

## KEYWORDS

Two-sided markets; electronic commerce; online intermediaries; customer churn; customer acquisition; platform economy

## Motivation

In two-sided markets, an intermediary provides a platform for interactions between two distinct customer populations [35, 38]. For example, the intermediaries Amazon, Taobao. com, and eBay use their platforms to enable transactions between sellers and buyers; and the intermediary Monster.com brings together employers and employees. These two-sided markets are not an entirely new phenomenon: In medieval times, for example, city councils provided marketplaces as platforms for farmers to o<sup>f</sup>er their products to buyers. Yet, the rise of what Shapiro and Varian [40] label the “network economy” has resulted in a plethora of two-sided markets due to the widespread use of the Internet ([3, 5, 13]; for comprehensive overviews on both online and o<sup>fl</sup>ine two-sided markets, see Parker and Van Alstyne [32]).

Such markets facilitate di<sup>f</sup>erent kinds of network e<sup>f</sup>ects: Cross-side network e<sup>f</sup>ects describe the situation whereby the presence of many sellers attracts more buyers to the market (e.g., eBay) and vice versa [26, 42]. In contrast, same-side network e<sup>f</sup>ects capture the interplay within one customer population. Same-side and cross-side e<sup>f</sup>ects can sometimes go in di<sup>f</sup>erent directions: For example, more buyers make an auction platform less attractive for buyers because of the heightened competition, but more attractive for sellers because of the increase in demand.

Companies typically have access to data — in particular, time-series data — on the development of the number of customers on the two market sides, which can help companies estimate the direction and magnitude of network e<sup>f</sup>ects. Such knowledge can support growth predictions, as well as the information technologies (IT) and marketing investment decisions that follow. Yet, measuring network e<sup>f</sup>ects remains a troublesome task, and the literature to date has examined, at best, 2 × 2 = 4 kinds of network e<sup>f</sup>ects, that is, a same-side and a crossside network e<sup>f</sup>ect for each of the two market sides.

However, network e<sup>f</sup>ects arise from a variety of mechanisms. For example, on the one hand, a larger number of customers can lead to a wider range of o<sup>f</sup>erings or more word-of -mouth within and across both market sides, which can increase the attractiveness of the market. On the other hand, the same situation can also lead to a decrease in attractiveness because of stronger competition among customers on one market side. Furthermore, such e<sup>f</sup>ects can di<sup>f</sup>er for new and existing customers. For example, word-of-mouth generated by existing customers (hereafter called the installed base) might a<sup>f</sup>ect the acquisition of new customers more strongly than the activity of existing customers. As another example, disclosing a large number of buyers on an auction platform might attract new buyers because such a large number serves as an indicator of the attractiveness of the market, but existing buyers might churn because of the expected increase in competition that is as a result of a higher number of buyers.

The research to date (as we will show in Table 1) has mainly investigated the sum of these two e<sup>f</sup>ects by assessing the net change in the number of customers on one side of the market. Thus, instead of examining changes in the number of newly acquired customers and the number of churning customers separately, they simply examine the sum of both, that is, the change in the number of total customers.

More technically speaking, the market grows on both sides because of an in<sup>fl</sup>ux (which constitutes the number of new customers) and shrinks because of an out<sup>fl</sup>ow (which constitutes the dropout, or churn, of existing customers) [19]. However, investments in IT can have asymmetric e<sup>f</sup>ects on in<sup>fl</sup>ux and out<sup>fl</sup>ow; thus, jointly estimating them may inaccurately summarize both e<sup>f</sup>ects because the growth in the number of new and existing customers may di<sup>f</sup>er across time. Yet, it is important to have knowledge of the separate e<sup>f</sup>ects because organizations usually assign di<sup>f</sup>erent units to acquire and retain customers on the two market sides [4].

In this paper, we develop a new model, the in<sup>fl</sup>ux-out<sup>fl</sup>ow model, which allows for asymmetric network e<sup>f</sup>ects<sup>1</sup>; that is, dropout and acquisition present di<sup>f</sup>erent e<sup>f</sup>ects on each market side. This model is unique because it is the <sup>fi</sup>rst to conceptually and empirically estimate eight network e<sup>f</sup>ects (two kinds of same-side network e<sup>f</sup>ects, two kinds of crossside network e<sup>f</sup>ects, and two kinds of e<sup>f</sup>ects on in<sup>fl</sup>ux and out<sup>fl</sup>ow). We show under which circumstances this model should be preferred over the standard model (hereafter labeled the “net change model”), which does not distinguish between network e<sup>f</sup>ects on the acquisition and dropout of customers. We use a simulation study and an empirical study to compare the in<sup>fl</sup>ux-out<sup>fl</sup>ow model with the net change model, <sup>fi</sup>nding that the former performs signi<sup>fi</sup>- cantly better, on average, with respect to estimating the true parameters.

<table><tr><td rowspan="2">Author(s)</td><td rowspan="2">Main research topic(s)</td><td rowspan="2">Industry/data set(s)</td><td rowspan="2">Economic dependent variable(s)</td><td colspan="3">Considers</td></tr><tr><td>CNE</td><td>SNE</td><td>Influx vs. Outflow</td></tr><tr><td>Brynjolfsson and Kemerer [6]</td><td>Installed base on price</td><td>Spreadsheet software</td><td>Prices</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Gandal, Kende, and Rob [17]</td><td>Hardware, prices and software on diffusion</td><td>CD players and titles</td><td>Change in variety and sales</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Shankar and Bayus [39]</td><td>Network strength in competition</td><td>Video game consoles</td><td>Network strength</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Asvanund, Clay, Krishnan, and Smith [2]</td><td>Incremental value of additional users</td><td>Peer-to-peer networks</td><td>Network value</td><td>No</td><td>Yes</td><td>(Yes) using proxy</td></tr><tr><td>Nair, Chintagunta, and Dubé [31]</td><td>Indirect network effects in competition</td><td>PDAs and software</td><td>Hardware demand, software provision</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Rysman [36]</td><td>Importance of cross-side network effects</td><td>Yellow Pages</td><td>Consumer and advertiser demand</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Clements and Ohashi [11]</td><td>Indirect NEs, hardware diffusion</td><td>Video game systems</td><td>Hardware and software adoption</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Ackerberg and Gowrisankaran [1]</td><td>NEs for banks and customers</td><td>ACH banking</td><td>Number of transactions</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Mantrala, Naik, Sridhar, and Thorson [30]</td><td>Marketing invest on profits</td><td>Newspapers</td><td>Subscriptions, ad revenue, sales</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Rysman [37]</td><td>Card usage and acceptance</td><td>Payment card transactions</td><td>Choice of favorite network</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Wilbur [45]</td><td>Ads on audience size and vice versa</td><td>TV ads</td><td>Viewer and advertiser demand</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Liu [28]</td><td>Pricing strategies</td><td>Video game consoles</td><td>Software and hardware demand</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Tucker and Zhang [42]</td><td>Installed base on listing behavior</td><td>Classifieds platform</td><td>Number of listings</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Sridhar, Mantrala, Naik, and Thorson [41]</td><td>Optimal marketing invests with cross-side network effects</td><td>Local newspaper</td><td>Demand from both sides</td><td>Yes</td><td>(Yes)</td><td>No</td></tr><tr><td>Chao and Derdenger [7]</td><td>Network effects on optimal price structure</td><td>Portable game consoles</td><td>Associated prices</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Lee [27]</td><td>Effect of vertical integration</td><td>Video game industry</td><td>Demand from both sides</td><td>Yes</td><td>No</td><td>No</td></tr><tr><td>Voigt and Hinz [43]</td><td>Network effects on revenue; revenue-optimal user split</td><td>Online dating platform</td><td>Revenue</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Chu and Manchanda [10]</td><td>Quantification of CNE and SNE</td><td>C2C platform</td><td>Growth of installed bases</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>This Paper</td><td>Separation of influx and outflow with respect to network effects</td><td>B2C platform</td><td>Growth of installed bases</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

Table 1. empirical studies estimating various kinds of network efects.

## Related Work

Network e<sup>f</sup>ects exist if an additional user in a market (alternatively called a “platform”) a<sup>f</sup>ects the value that existing customers derive from that market. If that value increases, then network e<sup>f</sup>ects are positive, and vice versa. Products such as phones and e-mail constitute one-sided markets that exhibit a positive network e<sup>f</sup>ect because the value of those products for a user increases with the number of interactions that occur with other users of the platform.

Two-sided markets are interorganizational information systems that provide two user populations (e.g., buyers and sellers) with rules and processes to identify potential users with whom to interact, select a speci<sup>fi</sup>c trading partner, and execute transactions [9]. Through these interactions, user populations create value [38]. Unlike one-sided markets, two-sided markets o<sup>f</sup>er interactions between two distinct user populations [14]. Usually, a user interacts only with users of the other market side (e.g., transactions between a buyer and a seller), although they can also in<sup>fl</sup>uence their own market side both positively (e.g., by providing advice) or negatively (e.g., by increasing competition) [8, 46]. Thus, researchers usually examine four network e<sup>f</sup>ects in two-sided markets: one same-side network e<sup>f</sup>ect for both market sides, as well as two cross-side network e<sup>f</sup>ects.

As Table 1 depicts, researchers have intensively studied network e<sup>f</sup>ects in recent years. Mainly <sup>fi</sup>nding that the estimated cross-side network e<sup>f</sup>ects are positive, scholars have then derived their impact on demand [17, 31, 36] and prices [6, 7]. Chu and Manchanda [10] contend that previous works have often concentrated on the bene<sup>fi</sup>ts (or costs) that users realize from the addition of users from either the same or the other market side, but not simultaneously from both sides. As a consequence, many studies estimate cross-side network e<sup>f</sup>ects but do not consider same-side network e<sup>f</sup>ects [6] or they instead rely on a proxy such as lagged sales for a potential same-side network e<sup>f</sup>ect [41]. However, more recent research underscores the strong in<sup>fl</sup>uence of same-side network e<sup>f</sup>ects in the market. The few studies that have investigated both types of network e<sup>f</sup>ects (see Table 1) focus on their implications for sales [42] or revenue [2].

Our study builds upon Chu and Manchanda [10] by exploring the impact of same- and cross-side network e<sup>f</sup>ects on a platform’s growth, while adding several important aspects. First, Chu and Manchanda [10] examined network e<sup>f</sup>ects in a consumer-to-consumer (C2C) market, whereas we investigate a business-to-consumer (B2C) market. Second, and more importantly, we distinguish between network e<sup>f</sup>ects that a<sup>f</sup>ect the acquisition of new users and those that a<sup>f</sup>ect the activity of existing users. Results from other settings highlight the importance of this distinction: Iyengar et al. [23] analyzed peer e<sup>f</sup>ects among physicians (which is similar to a one-sided market) and found that such e<sup>f</sup>ects have a di<sup>f</sup>erent impact on trial (comparable to our understanding of acquisition) and repeat purchases (comparable to the activity of existing users). Although they mainly studied social contagion processes, the distinction they made between the drivers might also be applicable to markets with network e<sup>f</sup>ects. Finally, our study examines the circumstances under which this distinction between di<sup>f</sup>erent network e<sup>f</sup>ects presents bene<sup>fi</sup>ts for platform operators.

Table 1 underscores that most studies in the area of two-sided markets do not distinguish between network e<sup>f</sup>ects on the acquisition of new customers and the dropout of existing customers. Interestingly, studies such as Ackerberg and Gowrisankaran [1] assumed that users will endlessly utilize a technology or platform once they have adopted it. As such, their participation increases the network e<sup>f</sup>ects without any temporal limitation, which is a strong assumption according to Wattal et al. [44] . Researchers typically make this assumption when their data is solely at the market level, such as with sales data of video game consoles [27]. Clements and Ohashi [11] are among the few who consider the possibility, at least in a robustness test, that the installed base depreciates at an annual rate of 5 percent.

If analysts have access to individual customers’ transactional data — which is increasingly the case — then they can consider the dropout of individual customers. Chu and Manchanda [10] did so for one of the two market sides. They used an activity-adjusted proxy for the number of sellers, but continued to use the cumulative number of registrations as a proxy for the number of buyers, even though buyers who registered years ago might have already churned or become inactive. Nevertheless, the authors’ use of an activity-adjusted proxy for one market side is a substantial step forward for accommodating dropouts.

Table 1 shows that previous research in the area of two-sided markets provides important insights, but does not distinguish between the eight kinds of network e<sup>f</sup>ects outlined herein. The insights of Iyengar et al. [23] indicate that a subtler distinction might be required in a setting in which di<sup>f</sup>erent features a<sup>f</sup>ect the processes that determine growth. For example, some features of a two-sided platform can create initial trust that motivates new customers to join the platform. These features are highly important for the acquisition of new customers, but less so for existing customers. Other features, meanwhile, may only a<sup>f</sup>ect existing customers who already use the platform. If a model to predict platform growth does not separate between these e<sup>f</sup>ects, then the estimation results can be biased and lead to less e<sup>f</sup>ective management decisions. In the next section, we discuss the importance of separating the network e<sup>f</sup>ects in two-sided markets and then analyze the conditions under which a separation should be preferred over a joint consideration.

## Theoretical Considerations for Separating Network E<sup>f</sup>ects in Two-Sided Markets and Results of a Simulation Study

## Analysis of Importance of Separating Network E<sup>f</sup>ects in Two-Sided Markets

Empirically inferring network e<sup>f</sup>ects requires econometric and causal identi<sup>fi</sup>cation, as well as supporting statistical information. When conclusions depend upon the statistical signi<sup>fi</sup>cance of measured e<sup>f</sup>ects — as they should — the amount of statistical information in the system under study is important. Typically, platform intermediaries possess only a limited number of observations (e.g., weekly observations of the number of customers on both sides of the market; changes in the number of customers on a weekly basis). As a result, the length of the observation period is limited.

Thus, in empirical, non-experimental studies of network e<sup>f</sup>ects, the data are, by de<sup>fi</sup>nition, outside the analyst’s control. However, in the context of two-sided markets, the analyst has a choice between separately or jointly modeling the in<sup>fl</sup>ux of new buyers (sellers) and the out<sup>fl</sup>ow of existing buyers (sellers). Jointly modeling them requires just two equations (one for the net change of buyers and one for the net change of the sellers) that characterize the market dynamics and equilibrium market size. Modeling them separately — our suggested approach — also yields the number of buyers and sellers, but it requires four separate equations: two equations for the in<sup>fl</sup>ux of new buyers and the out<sup>fl</sup>ow of existing buyers, and two for the in<sup>fl</sup>ux and out<sup>fl</sup>ow of sellers.

In the following, we discuss the advantages and disadvantages of modeling jointly versus separately. We show that jointly considering the decisions may result in a loss of statistical information under rather general conditions because summarizing the number of new and lost buyers into a net change in the number of customers may decrease the signal to noise ratio in the data. For example, if a measured cause exerts its in<sup>fl</sup>uence such that a larger number of new buyers tend to coincide with a larger number of lost buyers and vice versa, then the systematic variance in the net change will be low. At the same time, the error variance may increase by forming net changes. Thus, joint consideration generally obfuscates the independent in<sup>fl</sup>uence of causes on the number of new and lost buyers. Consider the situation where the installed base of buyers attracts even more new buyers (e.g., because of positive word-of-mouth created by existing buyers’ positive experience with the platform), but buyers on the platform actually compete for the same product, as is the case in an auction. In this example, an increase in the number of acquired buyers and lost buyers may balance out to suggest that network e<sup>f</sup>ects are not important in this market. Formally, we investigate the following proposition:

Proposition 1: The influx-outflow model better estimates network efects if the influx and outflow of one market side correlate positively (i.e., they even out).

Example: In<sup>fl</sup>ux = 2 new customers, Out<sup>fl</sup>ow = 2 lost customers, thus no change in the number of customers. In this example, the in<sup>fl</sup>ux-out<sup>fl</sup>ow model would be superior.

In contrast, if network e<sup>f</sup>ects positively (negatively) in<sup>fl</sup>uence in<sup>fl</sup>ux, but negatively (positively) in<sup>fl</sup>uence out<sup>fl</sup>ow, then their joined e<sup>f</sup>ect will be better measured by analyzing net changes. An example would be same-side network e<sup>f</sup>ects that may simultaneously decrease the in<sup>fl</sup>ux and increase the out<sup>fl</sup>ow of buyers, such as a gaming platform that links game publishers and gamers. Existing gamers’ positive word-of-mouth attracts new gamers, and the resulting increase in the number of gamers makes the platform more valuable because gamers have more gamers to play with; this increase in value reduces the out<sup>fl</sup>ow of gamers. Stated di<sup>f</sup>erently, a joint consideration leads to more variance in the network e<sup>f</sup>ect of interest, leading to proposition 2:

Proposition 2: The net change model better estimates network efects if influx and outflow of one market side correlate negatively.

Example: Some variable causes expected In<sup>fl</sup>ux = 2 of new customers and expected Out<sup>fl</sup>ow = 2 of lost customers to change to In<sup>fl</sup>ux = 4 and Out<sup>fl</sup>ow = 0, i.e., a change by 2 customers each, and in opposite directions. The resulting change in the number of customers of course increases from 0 to +4 customers. In this example, the net change model would be superior.

Note that the in<sup>fl</sup>ux-out<sup>fl</sup>ow model and the net-change model are identical in the limiting case of a deterministic growth-process. In this case, we can exactly solve for the parameters of either model and compute the exact net-change model parameters from the in<sup>fl</sup>ux-out<sup>fl</sup>ow model parameters by di<sup>f</sup>erencing deterministic in<sup>fl</sup>ux-out<sup>fl</sup>ow equations, assuming known functional forms. However, the in<sup>fl</sup>ux-out<sup>fl</sup>ow parameters generally cannot be recovered from the net-change parameters. The practically important di<sup>f</sup>erence between the two formulations arises when the growth-process is not deterministic. In this case, depending on the relationship between unobservables a<sup>f</sup>ecting growth and the link between observed variables and growth, either formulation may be more statistically e<sup>fi</sup>cient, that is, result in more reliable inference given the data. In the following, we prove propositions 1 and 2 for the case of linearly additive error structures. While a general proof is beyond the scope of this paper, we <sup>fi</sup>rst note that the empirical literature measuring network e<sup>f</sup>ects heavily relies on linear models. Second, we generalize beyond linear additivity in our simulation study because we also use multiplicative error terms.

## Proof

For non-positive correlations between unobservables a<sup>f</sup>ecting in<sup>fl</sup>ux $\left( \varepsilon _ { I n } \right)$ and out<sup>fl</sup>ow $( \varepsilon _ { O u t } )$ (on either market side), the variance of the error process in the di<sup>f</sup>erence between In<sup>fl</sup>ux and Out<sup>fl</sup>ow is larger than the variance of the individual error processes by elementary covariance algebra: var $\mathbf { \Psi } ( \Delta \varepsilon ) = \mathrm { v a r } ( \varepsilon _ { I n } - \varepsilon _ { O u t } ) = \mathrm { v a r } ( \varepsilon _ { I n } ) + \mathrm { v a r } ( \varepsilon _ { O u t } ) - 2 \mathrm { c o v } ( \varepsilon _ { I n } , \varepsilon _ { O u t } )$ . At the same time, the covariance between an explanatory variable x (a<sup>f</sup>ecting in<sup>fl</sup>ux linearly with coe<sup>fi</sup>cient $\delta _ { I n }$ and out<sup>fl</sup>ow with coe<sup>fi</sup>cient $\delta _ { O u t } )$ and the di<sup>f</sup>erence between in<sup>fl</sup>ux and out<sup>fl</sup>ow, i.e., $( \delta _ { I n } - \delta _ { O u t } ) \mathbf { v a r } ( x )$ will decrease relative to the covariance with in<sup>fl</sup>ux $\delta _ { I n } \mathbf { v a r } ( x )$ (out<sup>fl</sup>ow $\delta _ { O u t } \mathbf { v a r } ( x ) )$ , whenever $\left( \delta _ { I n } \delta _ { O u t } \right) > 0 .$ , i.e., x increases (or decreases) both in<sup>fl</sup>ux and out<sup>fl</sup>ow. Now, because the statistical information about parameters is a function of the signal (explained variance) to noise (unexplained variance) ratio the net change model will be less statistically e<sup>fi</sup>cient, i.e., will yield less reliable estimates of the in<sup>fl</sup>uence of $\mathbf { X } ,$ proving proposition 1.

However, for covariates $B u y e r s _ { t - 1 }$ and $S e l l e r s _ { t - 1 }$ , we often have $\left( { \delta } _ { I n } { \delta } _ { O u t } \right) < 0$ . For example, more buyers in the past may increase the in<sup>fl</sup>ow of (new) sellers, while decreasing the out<sup>fl</sup>ow of (existing) sellers. Thus, before considering unexplained variance from unobservables, the net-change model results in a stronger signal about the in<sup>fl</sup>uence of the installed base of buyers that proves proposition 2. Thus, determining whether the in<sup>fl</sup>uxout<sup>fl</sup>ow approach or the net change model is more e<sup>fi</sup>cient depends on the datagenerating values in the error process and the mean structure.

Finally, classical statistical inference for parameters in four equations rather than two increases the risk of false positives and false negatives, assuming everything else equal. For example, repeated application of a particular criterion for statistical signi<sup>fi</sup>cance may result in “signi<sup>fi</sup>cance by chance.” A more parsimonious description of the system (using only two equations for modeling net changes) is more easily handled in a classical framework. Thus:

Proposition 3: The net change model is superior because it has a lower risk to false positively detect non-existing network efects, which is relevant if same-side network efects are not present on at least one market side.

In the following sections, we further investigate our propositions in a simulation study with a multiplicative error structure and an empirical study.

## Simulating Two-Sided Markets

## Setup of Simulation Study

To test our theoretical considerations, we implemented a large-scaled simulation in C# and R. To this end, we created 84,672 markets by systematically varying the strength of the di<sup>f</sup>erent network e<sup>f</sup>ects and the error level, as shown in Table 2.

We assume that a decision-maker or data scientist uses weekly data from the past year (from T – 52 to T) to calibrate both the net change and the in<sup>fl</sup>ux-out<sup>fl</sup>ow models, with the aim of forecasting the development of the installed base (i.e., the number of customers on both market sides) over the next 52 weeks (from T to T + 52). We then compared the models’ performance. The results help us better understand when di<sup>f</sup>erences between the modeling approaches occur and under which circumstances one approach outperforms the other.

The number of sellers in each of the 104 weeks (two years) is given by:

$$
\text { Sellers } _ {t} = \text { Sellers } _ {t - 1} + \text { InfluxSellers } _ {t} - \text { OutflowSellers } _ {t}\tag{1}
$$

with

$$
\text { InfluxSellers } _ {t} = \left(\delta_ {1} \cdot \text { Buyers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {1}\right) + \left(\delta_ {2} \cdot \text { Sellers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {2}\right)\tag{2}
$$

$$
\text { OutflowSellers } _ {t} = \left(\delta_ {3} \cdot \text { Buyers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {3}\right) + \left(\delta_ {4} \cdot \text { Sellers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {4}\right),\tag{3}
$$

where $\delta _ { 1 }$ is the cross-side network e<sup>f</sup>ect from (existing) buyers on the number of acquired (new) sellers; $\delta _ { 2 }$ is the same-side network e<sup>f</sup>ect from (existing) sellers on the number of acquired (new) sellers; $\delta _ { 3 }$ is the cross-side network e<sup>f</sup>ect from (existing) buyers on the out<sup>fl</sup>ow of sellers, and $\delta _ { 4 }$ is the same-side network e<sup>f</sup>ect from sellers on the out<sup>fl</sup>ow of sellers. $E _ { I - 4 }$ constitute errors given by random numbers that are ${ \sim } N ( 0 , x )$ distributed. We systematically varied x to determine the in<sup>fl</sup>uence of di<sup>f</sup>erent sizes of the error on the prediction accuracy.

Experimental design of simulation study.

<table><tr><td>Experimental Factors</td><td>Number of Factor Levels</td><td>Values for Each Factor Level</td></tr><tr><td>Number of sellers in t = 0</td><td>1</td><td>50</td></tr><tr><td>Number of buyers in t = 0</td><td>1</td><td>500</td></tr><tr><td>Parameter of impact of buyers on seller influx δ1</td><td>2</td><td>.001/.0015</td></tr><tr><td>Parameter of impact of sellers on seller influx δ2</td><td>6</td><td>-.03/-.02/-.01/0/.01/.02</td></tr><tr><td>Parameter of impact of buyers on seller outflow δ3</td><td>2</td><td>.001/.0015</td></tr><tr><td>Parameter of impact of sellers on seller outflow δ4</td><td>6</td><td>.03/.02/.01/0/-.01/-.02</td></tr><tr><td>Parameter of impact of sellers on buyer influx δ5</td><td>2</td><td>.01/.015</td></tr><tr><td>Parameter of impact of buyers on buyer influx δ6</td><td>7</td><td>-.003/-.002/-.001/0/.001/.002/.003</td></tr><tr><td>Parameter of impact of sellers on buyer outflow δ7</td><td>2</td><td>.01/.015</td></tr><tr><td>Parameter of impact of buyers on buyer outflow δ8</td><td>7</td><td>-.003/-.002/-.001/0/.001/.002/.003</td></tr><tr><td>Random error (E1–E4, each drawn separately)</td><td>3</td><td>Low/Medium/High</td></tr><tr><td>Number of replications</td><td>1</td><td></td></tr><tr><td>Number of simulated markets</td><td></td><td>1·1·2·6·2·6·2·7·2·7·3·1 = 84,672</td></tr></table>

The number of buyers is given by:

$$
\text { Buyers } _ {t} = \text { Buyers } _ {t - 1} + \text { InfluxBuyers } _ {t} - \text { OutflowBuyers } _ {t}\tag{4}
$$

with

$$
\text { InfluxBuyers } _ {t} = \left(\delta_ {5} \cdot \text { Sellers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {5}\right) + \left(\delta_ {6} \cdot \text { Buyers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {6}\right)\tag{5}
$$

$$
\text { OutflowBuyers } _ {t} = \left(\delta_ {7} \cdot \text { Sellers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {7}\right) + \left(\delta_ {8} \cdot \text { Buyers } _ {t - 1}\right) \cdot \left(1 + \mathrm{E} _ {8}\right),\tag{6}
$$

where $\delta _ { 5 }$ is the cross-side network e<sup>f</sup>ect from (existing) sellers on the number of acquired (new) buyers; $\delta _ { 6 }$ is the same-side network e<sup>f</sup>ect from (existing) buyers on the number of acquired (new) buyers; $\delta _ { 7 }$ is the cross-side network e<sup>f</sup>ect from (existing) sellers on the out<sup>fl</sup>ow of buyers, and $\delta _ { 8 }$ is the same-side network e<sup>f</sup>ect from (existing) buyers on the out<sup>fl</sup>ow of buyers. Again, $E _ { 5 - 8 }$ constitute errors given by random numbers that are ${ \sim } N ( 0 , x )$ distributed.

The net change, that is, the change in the respective number of sellers or buyers, is thus:

$$
\Delta S e l l e r s _ {t} = S e l l e r s _ {t} - S e l l e r s _ {t - 1} = I n f l u x S e l l e r s _ {t} - O u t f l o w S e l l e r s _ {t}\tag{7}
$$

$$
\Delta \text { Buyers } _ {t} = \text { Buyers } _ {t} - \text { Buyers } _ {t - 1} = \text { InfluxBuyers } _ {t} - \text { OutflowBuyers } _ {t}\tag{8}
$$

Both models use the observations of the <sup>fi</sup>rst 52 weeks to estimate their parameters and estimate all equations jointly; a seemingly unrelated regression (SUR) is used to account for potential contemporaneous cross-equation error correlation. The in<sup>fl</sup>ux-out<sup>fl</sup>ow model estimates four equations with Out<sup>fl</sup>owSellers, In<sup>fl</sup>uxSellers, Out<sup>fl</sup>owBuyers, and In<sup>fl</sup>uxBuyers as dependent variables.

The net change model likewise estimates the parameters of the following two equations:

$$
\widehat {\Delta S e l l e r s} _ {t} = \beta_ {1} \cdot B u y e r s _ {t - 1} + \beta_ {2} \cdot S e l l e r s _ {t - 1} + \varepsilon_ {t}\tag{9}
$$

$$
\widehat {\Delta B u y e r s} _ {t} = \beta_ {3} \cdot S e l l e r s _ {t - 1} + \beta_ {4} \cdot B u y e r s _ {t - 1} + \varepsilon_ {t}\tag{10}
$$

We then used the estimated parameters to predict the number of buyers and sellers in each of the following 52 weeks and determine the mean absolute percentage error (MAPE) in the last week (i.e., in week T + 52).

## Results

The results outlined in Table 3 demonstrate that the in<sup>fl</sup>ux-out<sup>fl</sup>ow model leads to better predictions, on average, than the net change model. The average values of the MAPE are 38.6 percent better for the buyer (=1 – 16.12 percent/11.63 percent) and 95.6 percent better for the seller (=1 – 48.02 percent/24.55 percent) side. We also compared the predictions in each of the 84,672 markets. They were equally good in 39,087 markets (46.16 percent) for the number of buyers, better in 24,570 markets (29.02 percent) and worse in 21,015 markets (24.82 percent). The respective results for the number of sellers were equally good in 39,248 markets (46.35 percent), better in 23,177 (27.37 percent) and worse in 22,247 markets (26.27 percent). Thus, the in<sup>fl</sup>ux-out<sup>fl</sup>ow model performs on average signi<sup>fi</sup>cantly better. The Wilcoxon signed-rank test also supports this conclusion (p < .01 for both market sides).

Comparison of predictions of net change model and in<sup>fl</sup>ux-out<sup>fl</sup>ow model.

<table><tr><td></td><td>Number of Observations</td><td>Avg. MAPE of Number of Buyers (percent)</td><td>Avg. MAPE of Number of Sellers (percent)</td><td>Better for Number of Buyers (percent)</td><td>Better for Number of Sellers (percent)</td></tr><tr><td>Net change model</td><td>84,672</td><td>16.12</td><td>48.02</td><td>24.82</td><td>26.27</td></tr><tr><td>Influx-outflow model</td><td>84,672</td><td>11.63</td><td>24.55</td><td>25.95</td><td>27.37</td></tr></table>

Notes: MAPE, Mean Average Percentage Error.  
The di<sup>f</sup>erence between 100 percent and the two cells re<sup>fl</sup>ecting the share of models that are better for either the net change or the in<sup>fl</sup>ux-out<sup>fl</sup>ow model re<sup>fl</sup>ects the share of predictions that are equally good. For buyers, it is 49.23 percent = 100 percent – 24.82 percent – 25.95 percent, and for sellers, it is 46.36 percent = 100 percent – 26.27 percent – 27.37 percent.

## Test of Hypotheses

We also tested our hypotheses by examining the determinants of a binary outcome variable that is 1 if the MAPE of the net change model is as good or better than the in<sup>fl</sup>uxout<sup>fl</sup>ow model and 0 otherwise. In contrast to a measure such as MAPE, outliers do not in<sup>fl</sup>uence this binary measure. We then estimated a logistic regression with robust standard errors to examine the e<sup>f</sup>ect of asymmetric same-side network e<sup>f</sup>ects, nonexistent same-side network e<sup>f</sup>ects, and the error levels on the prediction accuracy for the two market sides. Table 4 presents the results.

Proposition 1 posits that if the out<sup>fl</sup>ow and in<sup>fl</sup>ux of one market side are positively correlated $( \mathrm { i } . \mathrm { e } . , \delta _ { 2 }$ and $\delta _ { 4 }$ have the same signs so that $\delta _ { 2 } \cdot \delta _ { 4 } \geq 0 )$ , then the in<sup>fl</sup>ux-out<sup>fl</sup>ow model is preferable. The negative parameters of the asymmetric same-side net e<sup>f</sup>ect on buyer/ seller side strongly support this proposition $( p < . 0 5$ for both market sides). Moreover, the positive parameter of the constant supports Proposition $2 \left( p < . 0 1 \right)$ , which posits that the net change model is superior if out<sup>fl</sup>ow and in<sup>fl</sup>ux of one market side correlate negatively.

Furthermore, if same-side network e<sup>f</sup>ects are nonexistent $( \mathrm { i . e . , i f } \delta _ { 6 } + \delta _ { 8 } = 0 \mathrm { o r } \delta _ { 2 } + \delta _ { 4 } = 0 ) _ { }$ then the standard net change model is better because of the positive parameters of the variable “no same-side net e<sup>f</sup>ect” on both buyer and seller sides (p < .01 for both market sides). This result supports Proposition 3. We also observe that the in<sup>fl</sup>ux-out<sup>fl</sup>ow model is preferable if the error level increases (p < .01 for both market sides).

Results of logistic regression that explains when net change model predicts at least as <sup>Table 4.</sup>good as in<sup>fl</sup>ux-out<sup>fl</sup>ow-model.

<table><tr><td>Variable</td><td>(1) Buyer Side</td><td>(2) Seller Side</td></tr><tr><td>Asymmetric same-side net effect on buyer side (0/1)(=1 if δ6 and δ8 have same signs, i.e., δ6 · δ8 ≥ 0, =0 otherwise)</td><td>-0.190***(0.016)</td><td>-0.037**(0.016)</td></tr><tr><td>Asymmetric same-side net effect on seller side (0/1)(=1 if δ2 and δ4 have same signs, i.e., δ2 · δ4 ≥ 0, =0 otherwise)</td><td>-0.145***(0.015)</td><td>-0.359***(0.016)</td></tr><tr><td>No same-side net effect on buyer side (0/1)(=1 if δ6 + δ8 = 0, =0 otherwise)</td><td>0.425***(0.062)</td><td>0.122**(0.057)</td></tr><tr><td>No same-side NE on seller side (0/1)(=1 if δ2 + δ4 = 0, =0 otherwise)</td><td>1.292***(0.071)</td><td>0.374***(0.055)</td></tr><tr><td>Error level</td><td>-0.012***(0.000)</td><td>-0.006***(0.000)</td></tr><tr><td>Constant</td><td>1.966***(0.029)</td><td>1.643***(0.029)</td></tr><tr><td>Wald Chi $^{2}$ </td><td>1,996.23</td><td>950.01</td></tr></table>

Notes: Robust standard errors in parentheses. $^ { * } \mathsf { p } < . 1 , ^ { * * } \mathsf { p } < . 0 5 , ^ { * * * } \mathsf { p } < . 0 1 , \mathsf { N } = 8 4 , 6 7 2$ . Binary dependent variable is 1 if MAPE net change model ≤ MAPE in<sup>fl</sup>ux-out<sup>fl</sup>ow model.

Comparison of average mean absolute percentage error (MAPE) in di<sup>f</sup>erent scenarios for measurement error.

<table><tr><td rowspan="2"></td><td colspan="2">Avg. MAPE/Number of Buyers</td><td colspan="2">Avg. MAPE/Number of Sellers</td></tr><tr><td>Net Change Model (percent)</td><td>Influx-Outflow Model (percent)</td><td>Net Change Model (percent)</td><td>Influx-Outflow Model (percent)</td></tr><tr><td>Scenario 1</td><td>14.81</td><td>10.94</td><td>42.59</td><td>23.90</td></tr><tr><td>Scenario 2</td><td>14.01</td><td>10.29</td><td>39.66</td><td>22.59</td></tr><tr><td>Scenario 3</td><td>16.19</td><td>12.07</td><td>46.29</td><td>25.75</td></tr></table>

## Robustness Check

In non-contractual settings, such as the one that we will cover in our empirical study, we have to proxy the number of customers on both market sides by applying heuristics that make use of the activity of each customer. In that setting, the proxies for the installed bases can su<sup>f</sup>er from measurement errors, which can introduce either an additional error or even a systematic bias. This bias result could lead to an under- or overestimation of the installed bases.

To assess the impact of the di<sup>f</sup>erent type of measurement errors, we extended our simulation and analyzed the following three scenarios:

(1) Measurement error E on number of buyers and sellers with E\~N(0, 0.01) each (=adding measurement noise)

(2) Measurement error E on number of buyers and sellers with E\~N(0, 0.01) and adding 5 percent of the installed base on each market side (=measurement noise plus systematic overestimation)

(3) Measurement error E on number of buyers and sellers with E\~N(0, 0.01) and subtracting 5 percent of the installed bases on each market side (=measurement noise plus systematic underestimation)

Table 5 shows that the existence of this type of measurement error does not favor any of the two competing models, and thus it should not impact our main conclusions. Please note that an underestimation always leads to higher MAPEs because MAPE can take on values larger than 1.

## Illustrative Empirical Study

## Description of the Two-Sided Market

We used data from an intermediary that operates a two-sided market to illustrate the di<sup>f</sup>erence between the two models. The intermediary — which we refer to here as “Platform.com” because we cannot, for con<sup>fi</sup>dentiality reasons, disclose the actual name — provides an e-commerce platform for buyers and sellers. On Platform.com, professional sellers o<sup>f</sup>er their products (e.g., consumer electronics, household appliances, jewelry, watches, cosmetics, etc.) to buyers. All products o<sup>f</sup>ered by sellers are new and in original packaging, and the prices already include value-added tax and shipping costs. The professional sellers must utilize a nickname pro<sup>fi</sup>le on Platform.com rather than disclose their identity so that there is no indication where buyers can <sup>fi</sup>nd the sellers’ online shop, which helps reduce cannibalization with other channels that sellers use.

Platform.com charges sellers a fee of 3 percent of the transaction price; there are no listing fees for sellers. Buyers can use the platform for free. Platform.com applies a continuous double-auction pricing mechanism so that prices re<sup>fl</sup>ect the relation between demand and supply. The product, however, is only sold if the highest bid surpasses the seller’s threshold. This continuous double-auction pricing mechanism resembles that of stock exchanges and makes Platform.com unique in the industry. Although Platform.com has had media coverage, it does not invest in costlier IT feature extensions or marketing activities such as promotions or advertising. Instead, it relies on organic growth through network e<sup>f</sup>ects fostered by improving its functionalities — particularly those listed in Table 6.

## Description of Data

Our illustrative empirical study uses the data on all 102,096 transactions completed between buyers and sellers on Platform.com over a time period of more than four years. We used weekly data (covering 211 weeks) as the unit of analysis. Our proposed model requires determining the number of (existing) buyers and sellers, the number of new buyers and sellers (i.e., in<sup>fl</sup>ux), and the number of lost buyers and sellers (i.e., out<sup>fl</sup>ow).

Investments of Platform.com.

<table><tr><td>Investment</td><td>Targeted Market Side(s)</td><td>Release Date</td><td>Description</td></tr><tr><td>Introduction video</td><td>Buyers</td><td>t = 79</td><td>The introduction video provides an easy first access for buyers by explaining the buying process on Platform.com, from searching for a product to completing the order.</td></tr><tr><td>New tools</td><td>Sellers</td><td>t = 89</td><td>New tools for sellers include statistical functionalities to analyze the current market situation at Platform.com. For instance, sellers can compare products offered on the platform or automate trading activities.</td></tr><tr><td>Platform.com button</td><td>Buyers Sellers</td><td>t = 98</td><td>The Platform.com button is a logo of the intermediary, which professional sellers can integrate into their own online shops. If a potential buyer clicks on this button, a link will forward the buyer to the products this seller offers on Platform.com.</td></tr><tr><td>Automated processing</td><td>Sellers</td><td>t = 118</td><td>A new API enables the automated processing of transactions. The API operates through XML messages exchanged between sellers and Platform.com via HTTP, based on Representational State Transfer architecture. Thus, sellers using many different types of e-commerce shop systems can use the API, regardless of operating systems or programming languages utilized.</td></tr><tr><td>Product news</td><td>Buyers Sellers</td><td>t = 130</td><td>Product news keeps buyers up-to-date regarding new products offered by sellers. The intermediary provides information and technical details for recently launched products that can be purchased on Platform.com.</td></tr><tr><td>“Trusted Shop” seal</td><td>Buyers</td><td>t = 165</td><td>Platform.com is certified with the “trusted shop” seal. A company that is specialized in certifying e-commerce shops provides confirmation to buyers that the buying process via Platform.com is secure and reliable. The certification comprises more than 100 criteria, including data security, customer service and price transparency. The certifying company also provides a money-back guarantee (e.g., in case of nondelivered products or credit card fraud).</td></tr><tr><td>Evaluation system</td><td>Buyers Sellers</td><td>t = 183</td><td>The evaluation system enables buyers to post their experiences with products and thereby facilitate the purchase decision for other buyers. On the web pages for each specific product, buyers can write comments and use a rating system.</td></tr><tr><td>Payment methods</td><td>Buyers Sellers</td><td>t = 186</td><td>The new payment methods include direct debit, instant bank transfer, payment via an online payment platform, and credit cards such as Visa, MasterCard and American Express. Buyers can choose from these new payment methods after price negotiations have concluded successfully. Prior to the introduction of the new payment methods, buyers only could pay in advance via an account managed by Platform.com.</td></tr></table>

## In<sup>fl</sup>ux, Out<sup>fl</sup>ow, and Number of Customers in Noncontractual Settings

Calculating the number of customers is straightforward if the platform intermediary has contractual relationships with its customers, such as if buyers and sellers pay a monthly or quarterly fee to use a platform. If, for example, women and men pay a monthly fee for using a heterosexual dating platform, then we could easily determine the number of customers by simply counting the number of contracts with women and men.

The number of customers is less evident in non-contractual settings, where no recurring fee governs the relationship between a platform intermediary and its customers. As such, the out<sup>fl</sup>ow (i.e., the churn, sometime also called “death”) is not observed because customers are not required to inform the intermediary that they no longer want to use the platform [21]. Such an observed output occurs for Platform.com: Sellers pay per transaction, and buyers complete transactions without being charged by the platform. If, for example, a buyer has not made any transactions for a long period of time, then the intermediary has no knowledge of whether the buyer is still using the platform or has become permanently inactive. Even if a buyer might not make a transaction for a long period of time, then the buyer can still have a nonzero probability of making another transaction [34].

Still, analysts could use models of “customer base analysis,” which essentially model that each customer is active (“alive”) for an (uncertain) number of periods and then becomes permanently inactive (“dead”). Fader and Hardie [15] nicely describe a company’s customer base as a “leaky bucket” whose contents are continually “dripping away” and outline that customer base analysis models do an excellent job of capturing customer “leakage” by estimating the probability of being active. The sum of the respective probabilities across customers can then be used to determine the number of existing customers (here also called active customers) in each period.

In settings where one can observe repeat-buying behavior but cannot observe customer dropout, the BG/NBD approach o<sup>f</sup>ers excellent data-<sup>fi</sup>tting capabilities [16] while being easy to calculate [33]. Although the BG/NBD models were developed to determine the number of buyers and explain their repeated purchases, these models can also serve to determine the number of sellers and their repeated sales in a two-sided market.<sup>2</sup> To do so, we view the sales as repeated instances of transactions that follow certain characteristics inherent in a given seller. A seller who has frequently made transactions in the past but has not done so in some time has a higher probability of being permanently inactive than another seller who has made at least a few transactions.<sup>3</sup> Still, we must assess the appropriateness of the BG/NBD model for this new application area, which we do in the following section.

## Results of the BG/NBD Model

We used the p(Alive)-function in the R-package “Buy-’Til-You-Die” (BTYD) [12], which uses BG/NBD model parameters and a customer’s past transaction behavior to calculate the probability that this customer will be alive at a given point. We summed the individual probabilities to be alive in each week using the transaction data and the BG/NBD model to determine the weekly number of customers for both market sides. The total number of buyers rose from 5 in t = 1 to 60,444 buyers at the end of the observation period, and the number of sellers increased from 3 at t = 1 to about 203 sellers at the end of the observation period (Figure 1).

Thus, one seller serves an average of about 297 buyers in t = 211. Figure 1 also reveals that the platform <sup>fi</sup>rst focused on the development of the seller side, which paid o<sup>f</sup> in later phases. Figure 1 shows an acceleration of growth, especially on the seller side in the pre-Christmas season (around t = 85, t = 137 and t = 190), when buyers and sellers have a higher probability of making transactions. As a result, we controlled for this seasonal e<sup>f</sup>ect.

We can derive the number of new buyers and sellers from the database because Platform.com assigns a speci<sup>fi</sup>c ID number to each buyer and seller in the time period of the trial (i.e., when an individual buyer or seller makes the <sup>fi</sup>rst transaction). Consequently, we can calculate the number of lost buyers (OutflowBuyers ) and sellers (OutflowSellers<sub>t</sub>) by comparing the total number of buyers and sellers and the number of new buyers InfluxBuyers<sub>t</sub> and sellers InfluxSellers<sub>t</sub> in di<sup>f</sup>erent time periods, expressed with the following equations:

$$
\text { OutflowBuyers } _ {t} = \text { Buyers } _ {t - 1} - \text { Buyers } _ {t} + \text { InfluxBuyers } _ {t}\tag{11}
$$

$$
\text { OutflowSellers } _ {t} = \text { Sellers } _ {t - 1} - \text { Sellers } _ {t} + \text { InfluxSellers } _ {t}\tag{12}
$$

We used Equations (11) and (12) to calculate the descriptive statistics for the number of (existing) buyers and sellers, for the in<sup>fl</sup>ux of (new) buyers and sellers, and for the out<sup>fl</sup>ow of (lost) buyers and sellers. Table 7 shows the detailed descriptive statistics for a selected number of weeks (i.e., for t = 50, 100, 150, and 200).

Our data show that, on average, Platform.com gained 309 new buyers per week and about 20 buyers became permanently inactive each week. Therefore, the intermediary has been growing at a net rate of 291 buyers per week. On the seller side, Platform.com gained an average of 1.6 sellers per week while .7 sellers became permanently inactive. These numbers translate into a growth rate of about .9 sellers every week. Thus, the platform grew on both market sides.

![](/api/attachments/MDFAF8WD/fulltext/images/8d883d27c3c13b1a88947752c1bd57c437836ec856d2875f850f1716f2a69ccc.jpg)  
Development of observed number of buyers and seller over time.

Description of the number of buyers and sellers in di<sup>f</sup>erent weeks.

<table><tr><td rowspan="2">Periodt(Week)</td><td colspan="3">Buyers</td><td colspan="3">Sellers</td></tr><tr><td>Total (BG/NBD)</td><td>Influx (ID Number)</td><td>Outflow (Calculation)</td><td>Total (BG/NBD)</td><td>Influx (ID Number)</td><td>Outflow (Calculation)</td></tr><tr><td>50</td><td>780.85</td><td>+9.00</td><td>-2.34</td><td>23.03</td><td>+/-0</td><td>-.51</td></tr><tr><td>100</td><td>3,049.47</td><td>+80.00</td><td>-.78</td><td>58.97</td><td>+1.00</td><td>-.64</td></tr><tr><td>150</td><td>16,518.58</td><td>+425.00</td><td>-40.03</td><td>129.29</td><td>+2.00</td><td>-2.07</td></tr><tr><td>200</td><td>53,052.47</td><td>+666.00</td><td>-85.51</td><td>203.08</td><td>+2.00</td><td>-4.54</td></tr><tr><td>Mean</td><td>12,920.56</td><td>+309.00</td><td>-19.48</td><td>85.10</td><td>+1.64</td><td>-.70</td></tr></table>

## Evaluation of Goodness of Fit

Using simulations and an empirical application, Fader et al. [16] showed that the BG/NBD model delivers good results. Likewise, we also test its goodness of <sup>fi</sup>t for our data set by comparing its predictions with the number of buyers and sellers that actually buy and sell. We determined the number of buyers and sellers for every period t by checking whether focal customers conducted a transaction in all periods from t + 1 until t = 211. We compared this observed number of buyers (sellers) with the predicted numbers of the BG/ NBD model. Note that this forward-looking approach represents a heuristic because we cannot observe an in<sup>fi</sup>nite time horizon; we can only observe 211 – t number of periods. This heuristic yields more valid outcomes if t is small (i.e., for early weeks) because future purchases are then observed in more weeks. Stated di<sup>f</sup>erently, the validity of our heuristic to evaluate the goodness of <sup>fi</sup>t decreases for estimates near the end of the observation period due to the right truncation of our data.

The correlation between the numbers predicted by the BG/NBD model and our heuristic is .9916 $\left( p < . 0 1 \right)$ for sellers and .8035 (p < .01) for buyers. The observed numbers of buyers and sellers drops dramatically when we move to the end of our data set; this drop is more severe for the buyer side because our buyers have a lower purchase frequency than our sellers. If we restrict our correlation analyses to the <sup>fi</sup>rst three years (weeks 1–156, such that about one year of data is left for observing purchases), then the correlation between the BG/NBD model and the heuristic is .9957 $\left( p < . 0 1 \right)$ for sellers and .9484 for buyers $\left( p < . 0 1 \right)$ . Thus, these results indicate that the BG/NBD model is a valid proxy for the latent unobservable number of customers, which has the major advantage of being able to handle right-truncated data.

## Identi<sup>fi</sup>cation Strategy

In most industries, inferring network e<sup>f</sup>ects in two-sided markets is di<sup>fi</sup>cult because researchers only have access to time-series data such as price and sales. This setting holds for technologically intensive goods as well because price and costs generally decrease over time due to technological advances, whereas quantity increases over time. These correlations make it di<sup>fi</sup>cult to identify network e<sup>f</sup>ects because we cannot determine whether the increasing quantities are due to positive network e<sup>f</sup>ects or simply due to lower prices [18].

It is even more di<sup>fi</sup>cult to identify the network e<sup>f</sup>ects, and thereby estimate the intertwined growth process, when time-varying factors can in<sup>fl</sup>uence the size of both market sides [29].

By disentangling dropout and acquisition on both market sides, and observing these changes as weekly variables, we eliminate the problem of identi<sup>fi</sup>cation from a mathematical point of view. We can use a simple time-series model with lagged variables of the number of customers (here, seller $N _ { ~ t - I } ^ { S }$ and buyers $N _ { ~ t - I } ^ { B } )$ . One problem that arises, however, is that unobservable variables can in<sup>fl</sup>uence one or both market sides, which could lead to an omitted variable bias that restricts causal identi<sup>fi</sup>cation. Thus, we dedicate the following section to dealing with this possible bias and the resulting endogeneity.

## Omitted Variable Bias and Endogeneity

The problems of endogeneity and omitted variable bias are quite common in these types of time-series models [18]. For example, suppose the estimated model for new buyers ignores the omitted variable $\gamma \cdot X _ { t }$ such that the true model is Equation (13):

$$
I n f l u x B u y e r s _ {t} = \alpha_ {B, N} + \beta_ {1, B, N} \cdot S e l l e r s _ {t - 1} + \beta_ {2, B, N} \cdot B u y e r s _ {t - 1} + \gamma \cdot X _ {t} + \varepsilon_ {t, B, N}.\tag{13}
$$

If Equation (13) is the true model and the estimation omits $\gamma { \cdot } X _ { t } ,$ then the error term will be:

$$
\varepsilon_ {t, B, N} = \gamma \cdot X _ {t} + \omega_ {t, B, N}.\tag{14}
$$

Such an error term violates the assumption of a regression model that $X _ { t }$ and $\varepsilon _ { t }$ are uncorrelated, which can lead to an omitted variable bias if $X _ { t }$ is correlated with included regressors. In the case of buyer and seller growth in two-sided Internet platforms, there could be time-varying factors that can be neither observed nor measured (e.g., trust toward the online shopping industry).

Let us, for example, assume that the omitted variable $X _ { t }$ describes the number of users on the Internet at time t, $I n f l u x B u y e r s _ { t }$ describes the number of new buyers, and both numbers grow over time due to the growing popularity of the Internet. This simultaneous growth would lead to $\gamma > 0$ . If we do not control for $X _ { t } ,$ then this omission will lead to biased parameter estimates. The parameters of other variables such as $S e l l e r s _ { t - 1 }$ would absorb this in<sup>fl</sup>uence, which could result, for instance, in an overestimation of the crossside network e<sup>f</sup>ect’s positive in<sup>fl</sup>uence.

To address this problem of endogeneity, we added various control variables on the market, industry and company levels that might also in<sup>fl</sup>uence the acquisition of buyers and sellers and their decisions to leave the platform. On the market level, we controlled for the gross domestic product (GDP), which might in<sup>fl</sup>uence both sides of the market. Further, to control for strong seasonal e<sup>f</sup>ects around Christmas [25], we included a variable that marks the Christmas trade season in the di<sup>f</sup>erent years.

On the industry level, we included the weekly advertising expenditure of the leading B2C auction platform eBay, which may directly a<sup>f</sup>ect the behavior of buyers on Platform. com. We expect that high advertising expenditures of eBay may decrease in<sup>fl</sup>ux and increase out<sup>fl</sup>ow during that particular week on Platform.com. Because only professional sellers utilize Platform.com, we do not expect eBay’s advertising behavior to exert such a direct and immediate impact on the seller side. With respect to the company level, we controlled for some media coverage that Platform.com received during the observation period using binary variables for that particular week (note that the platform itself did not engage in advertising or promotion activities during the observation period).

Although these control variables cover a wide range of potential in<sup>fl</sup>uences, spurious correlations can still occur and thus lead to an omitted variable bias. At this stage, data analysts typically try to <sup>fi</sup>nd instrumental variables that are correlated with the variable of interest but are uncorrelated with the error term. However, suitable instrumental variables are notoriously hard to <sup>fi</sup>nd [22]. Furthermore, because we model being alive as a probability that becomes continuously smaller with subsequent inactivity, we cannot use any exogenous shock as an instrument. We therefore address the problem of potentially omitted variables by equipping our model with additional proxy variables that capture omitted in<sup>fl</sup>uences and absorb them from the error term.

Conceptually, we suppose the following relationships. If there are omitted variables that in<sup>fl</sup>uence the number of buyers on Platform.com (e.g., number of online shoppers, Internet connection speed, advances in technology, trust in online shopping), then these variables must also in<sup>fl</sup>uence the number of buyers of other noncompeting B2C online shops. We therefore use the weekly number of orders from an unrelated (one-sided) B2C online shop as a proxy variable to capture these omitted in<sup>fl</sup>uences. If, for example, the number of online shoppers (buyers) increases over time, then this e<sup>f</sup>ect would equally in<sup>fl</sup>uence the growth on Platform.com and the number of orders at the noncompeting B2C online shop. The proxy variables can also capture negative in<sup>fl</sup>uences like media coverage about, say, general security concerns in e-commerce.

There might also be omitted variables on the seller side, such as variations in the number of startup online shops due to regulatory or <sup>fi</sup>scal changes. We used the number of sellers on a price comparison site as a proxy for omitted variables that may also in<sup>fl</sup>uence the seller side on Platform.com. These additional control and proxy variables lead to the model illustrated in Figure 2.

Table 8 summarizes the descriptive statistics for the dataset.

## Results of Illustrative Empirical Study

## Results of In<sup>fl</sup>ux-Out<sup>fl</sup>ow Model

After including our control and proxy variables, we used the in<sup>fl</sup>ux-out<sup>fl</sup>ow model to estimate the e<sup>f</sup>ect of the installed base, that is, the number of (existing) buyers and sellers on the in<sup>fl</sup>ux and out<sup>fl</sup>ow of (new and lost) buyers and sellers. Speci<sup>fi</sup>cally, we estimated all four equations (i.e., the e<sup>f</sup>ect on the in<sup>fl</sup>ux of buyers and sellers as well as the out<sup>fl</sup>ow) simultaneously, using seemingly unrelated regressions (SUR) with maximum-likelihood estimation while correcting for both heteroskedasticity (using robust standard errors) and autocorrelation.

Table 9 summarizes the results based on N = 210 observations (because we analyzed the growth between t = 211 time periods). The chi-squared statistics for all four equations allow for rejecting the null hypothesis that the parameters are jointly zero $\left( p < . 0 0 1 \right)$ .

We observed a positive cross-side network e<sup>f</sup>ect of +6.374 $\left( \boldsymbol { p } < . 0 1 \right)$ from the number of sellers on the number of new buyers, which means that more sellers make Platform.com more attractive for new buyers. More precisely, an additional seller in t – 1 led to the weekly acquisition of six additional buyers. Furthermore, the results revealed a negative same-side network e<sup>f</sup>ect of –.021 $\left( p < . 0 5 \right)$ from the number of buyers on new buyers, in accordance with theory.

Market Environment  
![](/api/attachments/MDFAF8WD/fulltext/images/911a00c3923aaf79b178bc19edc1c09cc04f9e7e11febc341c0476ad46195c76.jpg)  
Overview about control and proxy variables in model.

Descriptive statistics.

<table><tr><td></td><td>Mean</td><td>Std. Dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Number of sellers</td><td>85.10</td><td>66.35</td><td>3</td><td>204.45</td></tr><tr><td>Number of buyers</td><td>12,920.56</td><td>17527.63</td><td>13</td><td>60,443.93</td></tr><tr><td>All IT Investments</td><td></td><td></td><td>0</td><td>1</td></tr><tr><td>Media coverage</td><td>.028436</td><td>.1666102</td><td>0</td><td>1</td></tr><tr><td>eBay Advertising</td><td>63,7245.8</td><td>49,8280.2</td><td>0</td><td>25,48116</td></tr><tr><td>Gross Domestic Product (GDP)</td><td>107.4462</td><td>2.887706</td><td>102.37</td><td>111.88</td></tr><tr><td>Sellers&#x27; side, number of sellers of other platform</td><td>602.15</td><td>477.34</td><td>0</td><td>1,388.42</td></tr><tr><td>Buyers&#x27; side, number of orders on other platform</td><td>322.65</td><td>83.66</td><td>147</td><td>605</td></tr></table>

For the second dependent variable, the out<sup>fl</sup>ow of buyers, we observed that an increase in the number of buyers increased the out<sup>fl</sup>ow of buyers (+.002, $\textstyle P < . 0 5 )$ . This network e<sup>f</sup>ect can stem from a high level of competition among buyers.

On the seller side, the number of sellers decreased the number of acquired sellers (–0.062, $\textstyle P < . 0 5 )$ . Furthermore, the number of buyers had no signi<sup>fi</sup>cant e<sup>f</sup>ect on the acquisition of new sellers $\left( p > . 1 \right)$ . This result indicates that, in this early phase of a startup, sellers are more persuaded by other factors when deciding to try out this new platform, and thus management is justi<sup>fi</sup>ed in <sup>fi</sup>rst focusing on the acquisition of sellers. Table 9 also shows that a higher number of sellers increased the out<sup>fl</sup>ow of sellers $( + . 1 6 9 , p < . 0 1 )$ and more buyers decreased the out<sup>fl</sup>ow of sellers $( - 0 . 0 0 2 , p < . 0 1 )$

Overall, these results demonstrate face validity. We found signi<sup>fi</sup>cant parameters for six of eight network e<sup>f</sup>ects, and the missing two may conceivably play no role in the focal market. The results indicate an interrelated growth process of customer populations in two-sided markets through cross-side and same-side network e<sup>f</sup>ects.

Results of estimation of in<sup>fl</sup>ux-out<sup>fl</sup>ow model.

<table><tr><td>Variable</td><td>Influx of Buyers in tCoeff. (SE)</td><td>Outflow of Buyers in tCoeff. (SE)</td><td>Influx of Sellers in tCoeff. (SE)</td><td>Outflow of Sellers in tCoeff. (SE)</td></tr><tr><td>Number of sellers in t - 1</td><td>6.374**(2.325)</td><td>.102(.274)</td><td>-.062*(.022)</td><td>.169**(.031)</td></tr><tr><td>Number of buyers in t - 1</td><td>-.021*(.009)</td><td>.002*(.001)</td><td>-.0000(.0001)</td><td>-.0002**(.000)</td></tr><tr><td>Introduction video</td><td>-133.869(69.805)</td><td>.450(5.188)</td><td>1.826*(.715)</td><td>-1.502*(.643)</td></tr><tr><td>New tools</td><td>47.620(54.659)</td><td>-4.646(6.720)</td><td>.592(.711)</td><td>-.799(.697)</td></tr><tr><td>Platform.com button</td><td>-144.998**(54.568)</td><td>-.926(6.395)</td><td>.163(.677)</td><td>-2.496**(.617)</td></tr><tr><td>Automated processing</td><td>-51.380(33.092)</td><td>-3.037(7.921)</td><td>.156(.694)</td><td>-1.136(.764)</td></tr><tr><td>Product news</td><td>375.284**(102.260)</td><td>-3.865(11.320)</td><td>1.427*(.706)</td><td>.047(.094)</td></tr><tr><td>&quot;Trusted Shop&quot; seal</td><td>406.761**(85.181)</td><td>-1.103(9.569)</td><td>2.876*(1.178)</td><td>-3.375**(1.019)</td></tr><tr><td>Evaluation system</td><td>63.113(103.101)</td><td>-17.731(11.882)</td><td>3.941**(.763)</td><td>.772(1.050)</td></tr><tr><td>Payment methods</td><td>161.475(126.833)</td><td>-17.414(14.493)</td><td>.443(.965)</td><td>-1.552(1.269)</td></tr><tr><td>Media coverage</td><td>31.786(40.664)</td><td>-3.101(5.145)</td><td>.208(.754)</td><td>.331(.426)</td></tr><tr><td>eBay Advertising</td><td>-.0000(.0000)</td><td>-.0000(.0000)</td><td></td><td></td></tr><tr><td>GDP</td><td>-1.625(10.030)</td><td>-.715(1.371)</td><td>.319*(.141)</td><td>-.504**(.129)</td></tr><tr><td>Sellers&#x27; side, number of sellers of other platform in t</td><td></td><td></td><td>.004(.002)</td><td>-.006**(.002)</td></tr><tr><td>Buyers&#x27; side, number of orders on other platform in t</td><td>.505(.272)</td><td>.008(.003)</td><td></td><td></td></tr><tr><td>Intercept</td><td>-145.419(985.517)</td><td>72.854(134.383)</td><td>-32.585*(14.355)</td><td>49.700**(13.033)</td></tr><tr><td>Time controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>90.40 percent</td><td>80.22 percent</td><td>47.30 percent</td><td>40.97 percent</td></tr><tr><td>Adjusted  $R^2$ </td><td>88.89 percent</td><td>77.06 percent</td><td>39.17 percent</td><td>31.87 percent</td></tr></table>

Notes: SE, robust standard errors. N = 211.  
\*p < .05, \*\*p < .01, two−tailed signi<sup>fi</sup>cance.

## E<sup>f</sup>ect of Investments into Platform Functionality

The data set also allowed us to evaluate the e<sup>f</sup>ect of di<sup>f</sup>erent investments into the platform’s functionality which has been found to be an important driver for platform growth [24] and which could unearth valuable insights for other companies that aim to grow a two-sided market in the B2C domain. The in<sup>fl</sup>ux-out<sup>fl</sup>ow model makes it possible to understand the subtle in<sup>fl</sup>uences of the new functionalities on the acquisition and dropout of customers on both market sides. This understanding is of particular importance when di<sup>f</sup>erent organizational units are not only responsible for customer retention and customer acquisition, but also serve as pro<sup>fi</sup>t centers that must account for their investments.

The product news functionality improvement involves presenting information and technical details for recently launched products that can be purchased on Platform.com. New buyers and new sellers greatly appreciate this feature because it increases the acquisition of both buyers (+375.284, $ { p } < . 0 1 )$ and sellers (+1.427, $ { p } < . 0 5 )$

The “Trusted Shop” seal functionality improvement signi<sup>fi</sup>cantly simpli<sup>fi</sup>es the acquisition of buyers (+406.761, $p < . 0 1 )$ and sellers (+2.876, $\textstyle P < . 0 5 )$ . In this case, a certi<sup>fi</sup>cation company con<sup>fi</sup>rms the security of making transactions on Platform.com, reducing information asymmetries regarding the security and reliability of the intermediary for both market sides. Moreover, the seal also decreases the likelihood of losing sellers (–3.375, $\boldsymbol { p } <$ .01). In short, it constitutes one of the most e<sup>f</sup>ective functionality investments.

By incorporating user feedback, the evaluation system attracts new sellers (+3.941, $\boldsymbol { p } <$ .01) by helping prospective sellers observe activity on the other market side before they put their products on Platform.com. This ability to observe activity reduces information asymmetry for sellers by making the number of buyers easier to assess.

In sum, it appears that investments in trust (either in products on sales, in the platform itself or in the counterpart on the other market side) made the largest contribution to market growth. Our results thus suggest that companies should invest in this area if they want to achieve market growth.

The introduction of the Platform.com button turns out to be a double-edged sword: Professional sellers could integrate this optional button into their own online shop, but doing so revealed the seller’s identity to prospective buyers more easily. Thus, they could start to haggle with and buy from the seller’s online shop directly, thereby bypassing Platform.com and its 3 percent selling fee. This feature made it more di<sup>fi</sup>cult for Platform. com to acquire new buyers (–144.998, $p < . 0 1 )$ , but reduced the out<sup>fl</sup>ow of sellers (−2.496, $p < . 0 1 )$

Our analysis of the various investments in the platform shows that they a<sup>f</sup>ected the seller and buyer sides di<sup>f</sup>erently, as re<sup>fl</sup>ected in di<sup>f</sup>erent impacts on the activity and acquisition inherent to the two market sides. The standard net change model, in contrast, does not illuminate how the new features impact the market population exactly (i.e., whether they a<sup>f</sup>ect the in<sup>fl</sup>ux of new customers or the out<sup>fl</sup>ow of existing customers).

While we controlled for the e<sup>f</sup>ect of media coverage and eBay advertising, we did not <sup>fi</sup>nd that these factors had any in<sup>fl</sup>uence on the dependent variables. Meanwhile, our control variable for the macroeconomic development revealed that Platform.com can more easily acquire new sellers (+.319, $\textit { p } < \ . 0 5 )$ and decrease the out<sup>fl</sup>ow of sellers (–.504, $p < . 0 1 ,$ ) when the economy is growing (i.e., when GDP increases). These results seem plausible.

The proxy variables also point to some interesting <sup>fi</sup>ndings. On the seller side, we observe that some latent e<sup>f</sup>ect must be occurring that simultaneously a<sup>f</sup>ect the seller side of Platform.com and the sellers on the price comparison site. If the number of sellers on the price comparison site increases, then the weakly signi<sup>fi</sup>cant parameters suggest that it is also easier for Platform.com to acquire new sellers $( + . 0 0 4 , p < . 1 )$ . Likewise, the seller out<sup>fl</sup>ow at Platform.com also decreases with an increasing number of sellers on the price comparison site $( - . 0 0 6 , p < . 0 1 )$ . These e<sup>f</sup>ects seem plausible and could be interpreted as the general growth of e-commerce with a lower <sup>fl</sup>uctuation.

We further observe an e<sup>f</sup>ect of the proxy variable on the buyers’ side: If the number of orders at the noncompeting B2C shop goes up, then the number of new buyers on Platform.com will increase (+.505, p < .1). The growth of the market can explain this relationship.

The signi<sup>fi</sup>cant e<sup>f</sup>ects of the proxy variables re<sup>fl</sup>ect the presence of latent e<sup>f</sup>ects that in<sup>fl</sup>uence e-commerce in general. The signi<sup>fi</sup>cance of both proxy variables reveals that they work as intended and capture some otherwise omitted in<sup>fl</sup>uences. Although we acknowledge that we cannot fully rule out other uncontrolled e<sup>f</sup>ects that might in<sup>fl</sup>uence and consequently bias our results to some extent, we also note that the core intent of this paper is to provide an illustrative application of our arguments rather than to provide an exact measurement.

## Results of Net Change Model

In summary, Platform.com faces a market with asymmetric network e<sup>f</sup>ects on customer in<sup>fl</sup>ux and out<sup>fl</sup>ow. We conceptually argued that a summation of in<sup>fl</sup>ux and out<sup>fl</sup>ow can lead to problems in measuring network e<sup>f</sup>ects. To substantiate this claim, we also estimated the net change model: Table 10 lists its estimates. As theoretically expected, the installed base of buyers (–.023, p < .05) negatively a<sup>f</sup>ects the net change of buyers and the installed base of sellers has a positive in<sup>fl</sup>uence on the net change of buyers (6.299, $\hbar <$ .01). The analysis does not reveal a signi<sup>fi</sup>cant negative e<sup>f</sup>ect of the installed base of buyers on the net change of sellers; therefore, decision-makers could thus — depending on the chosen cuto<sup>f</sup> level for signi<sup>fi</sup>cance — wrongly conclude that the installed base of buyers exerts no e<sup>f</sup>ect on the seller side. However, the results from the in<sup>fl</sup>ux-out<sup>fl</sup>ow model in Table 9 show that this conclusion is not true: A higher number of buyers actually leads to a lower out<sup>fl</sup>ow of sellers.

The low $\mathrm { R } ^ { 2 } s$ of the net change model also indicate that the joint consideration engenders a loss of important information, which becomes even more evident if we calculate the growth from t = 12 to t = 211 using the estimates of the net change and in<sup>fl</sup>ux-out<sup>fl</sup>ow models.<sup>4</sup> Figure 3 shows that, even over a period of nearly four years, the <sup>fi</sup>t of the growth estimates remained good when we used the in<sup>fl</sup>ux-out<sup>fl</sup>ow model. The MAPE on the buyer side was only 2.1 percent at the end of the observation period, and although it is higher on the seller side, it is still tolerable (16.0 percent).

The net change model’s <sup>fi</sup>t of the growth is clearly inferior to the in<sup>fl</sup>ux-out<sup>fl</sup>ow model, as depicted by Figure 4. The growth estimates achieved a good <sup>fi</sup>t for about 1.5 years, but the lack of subtle information about network e<sup>f</sup>ects led to a substantial deviation between the observed and predicted installed bases.

## Conclusions

Our literature review shows that researchers have mainly focused on the cross-side network e<sup>f</sup>ects of installed bases because they only had access to very aggregated data (e.g., sales data on market level; [6,17]). Consequently, these early works made two simpli<sup>fi</sup>cations: First, they assumed that every sold unit adds one unit to the installed base and thus stays active in the market in<sup>fi</sup>nitely. However, we all know, for example, that CD players or videogame consoles get broken or replaced with newer versions or people sign up for a platform and become inactive after some time. To account for this, some researchers have relied on robustness checks to ascertain that the installed base depreciates at di<sup>f</sup>erent annual rates (see [11] as an example). With better datasets that are usually available these days, researchers should use more accurate measures for the installed bases.

Results of estimation of net change model.

<table><tr><td>Variable</td><td>Net Change of BuyersCoeff. (SE)</td><td>Net Change of SellersCoeff. (SE)</td></tr><tr><td>Number of sellers in t - 1</td><td>6.299**(2.273)</td><td>-.231**(.041)</td></tr><tr><td>Number of buyers in t - 1</td><td>-.023*(.009)</td><td>.000(.000)</td></tr><tr><td>Media coverage</td><td>-34.737(39.383)</td><td>-.121(.889)</td></tr><tr><td>Introduction video</td><td>-133.924(72.056)</td><td>3.321**(.910)</td></tr><tr><td>New tools</td><td>51.313(54.706)</td><td>1.385(.948)</td></tr><tr><td>Platform.com button</td><td>-144.301**(31.996)</td><td>2.664**(.946)</td></tr><tr><td>Automated processing</td><td>.47.75931.996</td><td>1.305(1.117)</td></tr><tr><td>Product news</td><td>378.746**(101.934)</td><td>1.392(1.120)</td></tr><tr><td>&quot;Trusted Shop&quot; seal</td><td>407.429**(84.300)</td><td>6.239**(1.516)</td></tr><tr><td>Evaluation system</td><td>79.603(110.228)</td><td>3.165**(1.122)</td></tr><tr><td>Payment methods</td><td>178.352(130.645)</td><td>1.985(1.450)</td></tr><tr><td>Media coverage</td><td>34.737(39.383)</td><td>-.121(.889)</td></tr><tr><td>eBay advertising</td><td>.0000(.0000)</td><td></td></tr><tr><td>Gross Domenstric Product (GDP)</td><td>-1.301(10.137)</td><td>.822**(.176)</td></tr><tr><td>Sellers&#x27; side, number of sellers on other Platform in t</td><td></td><td>.009**(.002)</td></tr><tr><td>Buyers&#x27; side, number of orders on other platform in t</td><td>.515(.271)</td><td></td></tr><tr><td>Intercept</td><td>-182.393(997.956)</td><td>-82.159**(17.871)</td></tr><tr><td>Time controls</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>88.81%</td><td>37.87 percent</td></tr><tr><td>Adjusted  $R^2$ </td><td>87.05 percent</td><td>28.35 percent</td></tr></table>

Notes: SE, robust standard errors. N = 211. \*p < .05, \*\*p< .01, two−tailed signi<sup>fi</sup>cance.

Second, previous research only rarely accounted for same-side network e<sup>f</sup>ects, e.g., that there is also competition on one or both market sides. In line with theory, our results suggest that same-side network e<sup>f</sup>ects can indeed be negative and thus have an in<sup>fl</sup>uence on the growth of the market as well. This result supports the <sup>fi</sup>nding of Asvanund et al. [2] that a growing number of P2P network users can also lead to network congestion and thus identi<sup>fi</sup>ed a negative same-side network e<sup>f</sup>ect.

Furthermore, previous research does not consider the nuanced impact that network e<sup>f</sup>ects can have on acquisition and churn/inactivity, that is, the in<sup>fl</sup>ux and out<sup>fl</sup>ow. Only Asvanund et al. [2] showed that a larger installed base can lead to an increased availability of songs in P2P communities, which can generate network growth as well as network congestion (due to a higher number of users), which can cause existing users to churn.

![](/api/attachments/MDFAF8WD/fulltext/images/da9eeae16b078c3e3b9b032881cdc73184479c65ff38a002e52a7a876293de94.jpg)  
Comparison of predicted and observed number of sellers and buyers of in<sup>fl</sup>ux-out<sup>fl</sup>ow model.

![](/api/attachments/MDFAF8WD/fulltext/images/82ed951e83d545aa8419e11ef1c495e2f20888189ec8bca0651f3099499cfda8.jpg)  
Comparison of predicted and observed number of sellers and buyers of net change model.

In general, we expect that more detailed data sets will become available in the near future and allow for more sophisticated analyses. In this article, we therefore propose a model that not only distinguishes between cross-side and same-side network e<sup>f</sup>ects, but also allows for network e<sup>f</sup>ects that can have an asymmetric impact on the acquisition of new customers and the out<sup>fl</sup>ow of existing customers. We thereby contribute to the stream of literature that empirically measures network e<sup>f</sup>ects and the growth of two-sided markets. Our <sup>fi</sup>ndings show that network e<sup>f</sup>ects can have an impact on the interrelated growth process of the two customer populations. We <sup>fi</sup>nd that the installed base of sellers positively in<sup>fl</sup>uences the acquisition of buyers (positive cross-side network e<sup>f</sup>ect), but negatively in<sup>fl</sup>uences the acquisition and activity of sellers (negative same-side network e<sup>f</sup>ects). Meanwhile, the installed base of buyers decreases the out<sup>fl</sup>ow of sellers (positive cross-side network e<sup>f</sup>ect), but negatively in<sup>fl</sup>uences the activity and acquisition of buyers, potentially due to greater competition (negative same-side network e<sup>f</sup>ect).

A large number of papers have measured positive cross-side network e<sup>f</sup>ects (see Table 1), but only Asvanund et al. [2], Tucker and Zhang [42], Voigt and Hinz [43], and Chu and Manchanda [10] have provided empirical evidence for in<sup>fl</sup>uential same-side network e<sup>f</sup>ects, which tend to be often negative due to competition e<sup>f</sup>ects. This paper provides more empirical evidence in this regard.

However, our results are more nuanced, as we examined not only the joint e<sup>f</sup>ects, but the speci<sup>fi</sup>c in<sup>fl</sup>uences on acquisition and churn. By doing so, we found that the installed base of buyers did not in<sup>fl</sup>uence the acquisition of sellers, which could be expected when taking subtle details on market mechanisms into account. In our empirical illustration, prospective sellers who are considering joining the platform cannot — as “outsiders” — reliably assess the size of the other market side. Thus, there must obviously be reasons other than cross-side network e<sup>f</sup>ects that spur sellers to join the platform early on.

A detailed analysis of the impact of IT investments reveals that investments that increase trust (in the platform operator, in products, and in participants on the other market side) can help to grow the platform. Such an analysis revivi<sup>fi</sup>es the idea proposed by Nair et al. [31], who assessed the impact of investments in hardware and software for growing networked markets.

Methodologically, we showed that separately modeling the in<sup>fl</sup>ux of new customers and the out<sup>fl</sup>ow of existing customers on each market side produces more reliable statistical inferences, on average, than modeling the net changes in the numbers of buyers and sellers. Thus, we advocate a model that employs more parameters to achieve greater statistical e<sup>fi</sup>ciency.

Our results suggest that it is especially preferable to employ the in<sup>fl</sup>ux-out<sup>fl</sup>ow model in two-sided markets if one expects a positive (negative) same-side network e<sup>f</sup>ect on acquisition, but a negative (positive) same-side network e<sup>f</sup>ect on the activity of that market side. The theory we outlined suggests that such a setting is likely in markets with competition among same-side customers (e.g., auction markets), in which case data scientists should use the proposed in<sup>fl</sup>ux-out<sup>fl</sup>ow model. Our empirical study also supports this recommendation.

In contrast, the net change model is preferable for markets in which the installed base of the same side positively in<sup>fl</sup>uences both acquisition and activity of the same side. This setting is more common for two-sided markets of gamers and game publishers (i.e., more gamers make it easier to acquire new gamers, as well as they may increase the activity of all gamers).

The paper’s insights for two-sided markets can also be transferred to one-sided markets, as there are special cases where the cross-side network e<sup>f</sup>ects are zero and the analysis focuses just on one equation. Even for this special case, our analysis recommends distinguishing between in<sup>fl</sup>ux and out<sup>fl</sup>ow.

In sum, this paper and in particular the presented in<sup>fl</sup>ux-out<sup>fl</sup>ow model should impact the way how researchers and business practitioners alike should measure network e<sup>f</sup>ects in two-sided markets. Our analyses show that the use of detailed information, that is, the nuanced in<sup>fl</sup>ow and out<sup>fl</sup>ow of customers, could be helpful to arrive at informed measures for network e<sup>f</sup>ects in the platform economy.

## Notes

1. In the context of this paper, “asymmetric network e<sup>f</sup>ects” mean that the installed base of customers makes it easier to acquire new customers (in<sup>fl</sup>ow), but harder to keep existing customers (out<sup>fl</sup>ow) and vice versa.

2. In principle, such models could also make use of other signals such as messages that buyers share in forums or online social networks [20] or user-generated content in general. Plattform.com did not allow such interactions to circumvent the bypassing of the platform. Purchases are however in all cases the strongest and most credible signal that can be used to infer the installed bases for market participants. Therefore, the majority of models in the area of “customer base analysis” use this information.

3. A platform operator could also use other signals of activity as an input for sellers’ churn model, such as the creation of o<sup>f</sup>ers or activities in the back end of the system. Unfortunately, we do not have access to such data, which prevents us from using this promising alternative approach to model the number of sellers.

4. We assume constant network e<sup>f</sup>ects over time, which is a commonly made assumption.

## Acknowledgements

We also thank Tim Kraemer for helping us to start this project and for his support throughout the earlier phases of this project.

## Funding

This work has been [co-]funded by the DFG as part of the CRC 1053 MAKI and by the e<sup>fl</sup> – the Data Science Institute at Goethe University Frankfurt.

## References

1. Ackerberg, D.A.; and Gowrisankaran, G. Quantifying equilibrium network externalities in the ACH banking industry. RAND Journal of Economics, 37, 3 (2006), 738–761.

2. Asvanund, A.; Clay, K.; Krishnan, R.; and Smith, M.D. An empirical analysis of network externalities in peer-to-peer music-sharing networks. Information Systems Research, 15, 2 (2004), 155–174.

3. Bakos, Y.; and Katsamakas, E. Design and ownership of two-sided networks: Implications for Internet platforms. Journal of Management Information Systems, 25, 2 (2008), 171–202.

4. Blattberg, R.C.; and Deighton, J. Manage marketing by the customer equity test. Harvard Business Review 74, 1996, 136–144.

5. Brunswicker, S.; Almirall, E.; and Majchrzak, A. Optimizing and satis<sup>fi</sup>cing: The Interplay between platform architecture and producers’ design strategies for platform performance. MIS Quarterly, 43, 4 (2019), 1249–1277.

6. Brynjolfsson, E.; and Kemerer, C.F. Network externalities in microcomputer software: An econometric analysis of the spreadsheet market. Management Science, 42, 12 (1996), 1627–1647.

7. Chao, Y.; and Derdenger, T. Mixed bundling in two-sided markets in the presence of installed base e<sup>f</sup>ects. Management Science, 59, 8 (2013), 1904–1926.

8. Chircu, A.M.; and Kau<sup>f</sup>man, R.J. Limits to value in electronic commerce-related IT investments. Journal of Management Information Systems, 17, 2 (2000), 59–80.

9. Choudhury, V.; Hartzel, K.S.; and Konsynski, B.R. Uses and consequences of electronic markets: An empirical investigation in the aircraft parts industry. MIS Quarterly, 22, 4 (1998), 471–507.

10. Chu, J.; and Manchanda, P. Quantifying cross and direct network e<sup>f</sup>ects in online consumer-to-consumer platforms. Marketing Science, 35, 6 (2016), 870–893.

11. Clements, M.T.; and Ohashi, H. Indirect network e<sup>f</sup>ects and the product cycle: Video games in the US, 1994–2002. Journal of Industrial Economics, 53, 4 (2005), 515–542.

12. Dziurzynski, L.; McCarthy, D.; and Wadsworth, E. BTYD-package: Implementing buy ’til you die models. 2012. https://rdrr.io/cran/BTYD/man/BTYD-package.html.

13. Ellison, G.; and Fisher Ellison, S. Lessons about markets from the Internet. Journal of Economic Perspectives, 19, 2 (2005), 139–158.

14. Evans, D.S.; and Schmalensee, R. Paying with Plastic: The Digital Revolution in Buying and Borrowing. Cambridge: MIT Press, 2005.

15. Fader, P.S.; and Hardie, B.G.S. The Pareto/NBD is Not a lost-for-good model. 2014. Accessed on 17 January 2020: http://brucehardie.com/notes/031/.

16. Fader, P.S.; Hardie, B.G.S.; and Lee, K.L. “Counting your customers” the easy way: An alternative to the Pareto/NBD Model. Marketing Science, 24, 2 (2005), 275–284.

17. Gandal, N.; Kende, M.; and Rob, R. The dynamics of technological adoption in hardware/ software systems: The case of compact disc players. RAND Journal of Economics, 31, 1 (2000), 43–61.

18. Gowrisankaran, G.; and Stavins, J. Network Externalities and technology adoption: Lessons from electronic payments. RAND Journal of Economics, 35, 2 (2004), 260–276.

19. Haenlein, M. Social interactions in customer churn decisions: The impact of relationship directionality. International Journal of Research in Marketing, 30, 3 (2013), 236–248.

20. Heimbach, I.; and Hinz, O. The impact of sharing mechanism design on content sharing in online social networks. Information Systems Research, 29, 3 (2018), 592–611.

21. Hinz, O., Eckert, J., and Skiera, B. Drivers of the long tail phenomenon: An empirical analysis. Journal of Management Information Systems, 27, 4 (2011), 43–70.

22. Hinz, O.; Hill, S.; and Kim, J.-Y. TV’s Dirty little secret: The negative e<sup>f</sup>ect of popular TV on online auction sales. MIS Quarterly, 40, 3 (2016), 623–644.

23. Iyengar, R.; Van den Bulte, C.; and Lee, J.Y. Social contagion in new product trial and repeat. Marketing Science, 34, 3 (2015), 408–429.

24. Jung, D.; Kim, B.C.; Park, M.; and Straub, D.W. Innovation and policy support for two-sided market platforms: Can government policy makers and executives optimize both societal value and pro<sup>fi</sup>ts? Information Systems Research, 30, 3 (2019), 1037–1050.

25. Kapoor, S.G.; Madhok, P.; and Wu, S.M. Modeling and forecasting sales data by time series analysis. Journal of Marketing Research, 18, 1 (1981), 94–100.

26. Kau<sup>f</sup>man, R.J.; and Weber, T.A. Social in<sup>fl</sup>uence and networked business interaction. Journal of Management Information Systems, 36, 4 (2019), 1040–1042.

27. Lee, R.S. Vertical integration and exclusivity in platform and two-sided markets. American Economic Review, 103, 7 (2013), 2960–3000.

28. Liu, H. Dynamics of pricing in the video game console market: Skimming or penetration? Journal of Marketing Research, 47, 3 (2010), 428–443.

29. Manski, C.F. Identification Problems in the Social Sciences. Cambridge: Harvard University Press, 1999.

30. Mantrala, M.K.; Naik, P.A.; Sridhar, S.; and Thorson, E. Uphill or downhill? Locating the <sup>fi</sup>rm on a pro<sup>fi</sup>t function. Journal of Marketing, 71, 2 (2007), 26–44.

31. Nair, H.; Chintagunta, P.; and Dubé, J.-P. Empirical analysis of indirect network e<sup>f</sup>ects in the market for personal digital assistants. Quantitative Marketing and Economics, 2, 1 (2004), 23–58.

32. Parker, G.G.; and Van Alstyne, M.W. Two-Sided Network E<sup>f</sup>ects: A theory of information product design. Management Science, 51, 10 (2005), 1494–1504.

33. Platzer, M.; and Reutterer, T. Ticking away the moments: Timing regularity helps to better predict customer activity. Marketing Science, 35, 5 (2016), 779–799.

34. Reinartz, W.J.; and Kumar, V. The impact of customer relationship characteristics on pro<sup>fi</sup>table lifetime duration. Journal of Marketing, 67, 1 (2003), 77–99.

35. Rochet, J.-C.; and Tirole, J. Two-sided markets: A progress report. RAND Journal of Economics, 37, 3 (2006), 645–667.

36. Rysman, M. Competition between networks: A study of the market for yellow pages. Review of Economic Studies, 71, 2 (2004), 483–512.

37. Rysman, M. An empirical analysis of payment card usage. Journal of Industrial Economics, 55, 1 (2007), 1–36.

38. Rysman, M. The economics of two-sided markets. Journal of Economic Perspectives, 23, 3 (2009), 125–143.

39. Shankar, V.; and Bayus, B.L. Network e<sup>f</sup>ects and competition: An empirical analysis of the home video game industry. Strategic Management Journal, 24, 4 (2003), 375–384.

40. Shapiro, C.; and Varian, H.R. Information Rules: A Strategic Guide to the Network Economy. Boston: Harvard Business School Press, 1999.

41. Sridhar, S.; Mantrala, M.K.; Naik, P.A.; and Thorson, E. Dynamic marketing budgeting for platform <sup>fi</sup>rms: Theory, evidence, and application. Journal of Marketing Research, 48, 6 (2011), 929–943.

42. Tucker, C.; and Zhang, J. Growing two-sided networks by advertising the user base: A <sup>fi</sup>eld experiment. Marketing Science, 29, 5 (2010), 805–814.

43. Voigt, S.; and Hinz, O. Network e<sup>f</sup>ects in two-sided markets: Why a 50/50 user split is not necessarily revenue-optimal. Business Research, 8, 1 (2015), 139–170.

44. Wattal, S.; Racherla, P.; and Mandviwalla, M. Network externalities and technology use: A quantitative analysis of intraorganizational blogs. Journal of Management Information Systems, 27, 1 (2010), 145–174.

45. Wilbur, K.C. A two-sided, empirical model of television advertising and viewing markets. Marketing Science, 27, 3 (2008), 356–378.

46. Yoo, B.; Choudhary, V.; and Mukhopadhyay, T. A model of neutral B2B intermediaries. Journal of Management Information Systems, 19, 3 (2002), 43–68.

## About the Authors

Oliver Hinz (ohinz@wiwi.uni-frankfurt.de; corresponding author) is Professor of Information Systems and Information Management at Goethe University Frankfurt, Germany. He is interested in research at the intersection of technology and markets. His work has been published in such journals as Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Journal of Marketing, and Decision Support Systems, and in a number of proceedings the leading IS conferences.

Thomas Otter (otter@marketing.uni-frankfurt.de) is Professor of Marketing at Goethe University. His research focuses on Bayesian modeling with application to marketing. He has worked in the areas of conjoint measurement, choice modeling, and assessing the e<sup>f</sup>ectiveness of marketing actions when the actions are endogenous to the system. Dr. Otter’s papers have been published in Journal of Marketing Research, Marketing Science, Quantitative Marketing and Economics, Journal of Business & Economic Statistics, and other journals. He is co-editor of Quantitative Marketing and Economics and member of the editorial review boards of Marketing Science other journals.

Bernd Skiera (skiera@skiera.de) holds the Chair of Electronic Commerce at Goethe University and is also Professorial Fellow at Deakin University. Australia. His interests include e-commerce, marketing analytics, online marketing, customer management, and integration platforms as a service (iPaas). Dr. Skiera has published in such journals such as Management Science, Journal of Management Information Systems. Marketing Science, Journal of Marketing Research, and others. He was a recipient of an ERC Advanced Grant in 2019.
